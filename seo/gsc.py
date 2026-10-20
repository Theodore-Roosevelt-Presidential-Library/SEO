"""Google Search Console collector.

Signs in as a Google Cloud service account that is a user on the Search
Console property. Preferred: keyless Workload Identity Federation (repo
variables GCP_WIF_PROVIDER + GCP_SERVICE_ACCOUNT; the workflow's auth step
sets GOOGLE_APPLICATION_CREDENTIALS). Fallback: a JSON key in the secret
GSC_SERVICE_ACCOUNT_JSON, for Google orgs that allow key creation.

Writes:
  gsc/daily.json        clicks/impressions/ctr/position per day (~16 months)
  gsc/summary.json      last 28 days vs the 28 days before
  gsc/queries.json      top queries, last 28 days, with previous-period numbers
  gsc/pages.json        top pages, last 28 days, with previous-period numbers
  gsc/query_pages.json  query x page pairs (feeds opportunities + tips)
  gsc/devices.json      split by device
"""
from __future__ import annotations

import datetime as dt
import json
from urllib.parse import quote

from . import common as C

SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"
API = "https://searchconsole.googleapis.com/webmasters/v3/sites/{site}/searchAnalytics/query"
LAG_DAYS = 3  # Search Console data settles after ~2-3 days


def _token(sa_json: str | None) -> str:
    """Key file if one was supplied; otherwise Application Default Credentials,
    which is what keyless Workload Identity Federation sets up in Actions."""
    import google.auth
    import google.auth.transport.requests as gtr
    from google.oauth2 import service_account

    if sa_json:
        creds = service_account.Credentials.from_service_account_info(json.loads(sa_json), scopes=[SCOPE])
    else:
        creds, _ = google.auth.default(scopes=[SCOPE])
    creds.refresh(gtr.Request())
    return creds.token


class GSC:
    def __init__(self, token: str, prop: str):
        self.s = C.session()
        self.s.headers["Authorization"] = f"Bearer {token}"
        self.url = API.format(site=quote(prop, safe=""))

    def query(self, start: dt.date, end: dt.date, dims: list[str], limit: int = 25000) -> list[dict]:
        rows, start_row = [], 0
        while True:
            body = {
                "startDate": start.isoformat(),
                "endDate": end.isoformat(),
                "dimensions": dims,
                "rowLimit": min(limit - len(rows), 25000),
                "startRow": start_row,
                "dataState": "final",
            }
            r = self.s.post(self.url, json=body, timeout=60)
            if r.status_code != 200:
                raise RuntimeError(f"Search Console API {r.status_code}: {r.text[:300]}")
            batch = r.json().get("rows", [])
            for b in batch:
                row = {d: k for d, k in zip(dims, b.get("keys", []))}
                row.update(
                    clicks=int(b.get("clicks", 0)),
                    impressions=int(b.get("impressions", 0)),
                    ctr=round(b.get("ctr", 0.0), 4),
                    position=round(b.get("position", 0.0), 1),
                )
                rows.append(row)
            if len(batch) < body["rowLimit"] or len(rows) >= limit:
                return rows
            start_row += len(batch)


def _totals(rows: list[dict]) -> dict:
    clicks = sum(r["clicks"] for r in rows)
    impr = sum(r["impressions"] for r in rows)
    # impression-weighted average position
    pos = sum(r["position"] * r["impressions"] for r in rows) / impr if impr else 0
    return {
        "clicks": clicks,
        "impressions": impr,
        "ctr": round(clicks / impr, 4) if impr else 0,
        "position": round(pos, 1),
    }


def _merge_prev(cur: list[dict], prev: list[dict], key: str) -> list[dict]:
    p = {r[key]: r for r in prev}
    out = []
    for r in cur:
        o = p.get(r[key])
        r = dict(r)
        r["prev_clicks"] = o["clicks"] if o else 0
        r["prev_impressions"] = o["impressions"] if o else 0
        r["prev_position"] = o["position"] if o else None
        out.append(r)
    return out


def run() -> None:
    cfg = C.config()
    sa = C.env("GSC_SERVICE_ACCOUNT_JSON")
    if not sa and not C.env("GOOGLE_APPLICATION_CREDENTIALS"):
        C.set_status("gsc", "skipped", "Set up Google sign-in (Workload Identity Federation, see README) to turn on Search Console data.")
        return
    prop = cfg["site"]["gsc_property"]
    try:
        g = GSC(_token(sa), prop)
        end = C.today() - dt.timedelta(days=LAG_DAYS)
        start = end - dt.timedelta(days=27)
        p_end = start - dt.timedelta(days=1)
        p_start = p_end - dt.timedelta(days=27)

        daily = g.query(end - dt.timedelta(days=480), end, ["date"])
        daily.sort(key=lambda r: r["date"])
        C.write_json("gsc/daily.json", daily)

        q_cur = g.query(start, end, ["query"], limit=5000)
        q_prev = g.query(p_start, p_end, ["query"], limit=5000)
        pg_cur = g.query(start, end, ["page"], limit=5000)
        pg_prev = g.query(p_start, p_end, ["page"], limit=5000)
        qp = g.query(start, end, ["query", "page"], limit=25000)
        dev = g.query(start, end, ["device"])

        cur_days = [r for r in daily if start.isoformat() <= r["date"] <= end.isoformat()]
        prev_days = [r for r in daily if p_start.isoformat() <= r["date"] <= p_end.isoformat()]

        branded = [t.lower() for t in cfg.get("branded_query_terms", [])]
        def is_branded(q: str) -> bool:
            ql = q.lower()
            return any(t in ql for t in branded)

        q_rows = _merge_prev(sorted(q_cur, key=lambda r: -r["impressions"]), q_prev, "query")
        for r in q_rows:
            r["branded"] = is_branded(r["query"])

        summary = {
            "property": prop,
            "updated": C.now_iso(),
            "period": {"start": start.isoformat(), "end": end.isoformat()},
            "previous": {"start": p_start.isoformat(), "end": p_end.isoformat()},
            "current_totals": _totals(cur_days),
            "previous_totals": _totals(prev_days),
            "branded_clicks": sum(r["clicks"] for r in q_rows if r["branded"]),
            "nonbranded_clicks": sum(r["clicks"] for r in q_rows if not r["branded"]),
            "query_count": len(q_cur),
            "page_count": len(pg_cur),
        }
        C.write_json("gsc/summary.json", summary)
        C.write_json("gsc/queries.json", q_rows)
        C.write_json("gsc/pages.json", _merge_prev(sorted(pg_cur, key=lambda r: -r["impressions"]), pg_prev, "page"))
        C.write_json("gsc/query_pages.json", sorted(qp, key=lambda r: -r["impressions"]))
        C.write_json("gsc/devices.json", dev)
        C.set_status("gsc", "ok", f"{len(q_cur)} queries, {len(pg_cur)} pages ({start} to {end})")
    except Exception as e:  # noqa: BLE001
        C.set_status("gsc", "error", str(e)[:400])
        raise C.JobError(str(e)) from e


if __name__ == "__main__":
    run()
