"""Change log (config/changes.yml): what was changed on the site, and did it work?

- held_paths(): pages changed within hold_days. Opportunities and the AI
  recommendations skip them, so the tool doesn't re-recommend a fix that's
  already live but not yet visible in 28-day Search Console numbers.
- build(): for each changed page, Search Console clicks, impressions, CTR and
  position for the 28 days before the change vs the days since (per-day
  averages too, since the "after" window is shorter at first). Run daily by the
  gsc job; writes changes.json.
"""
from __future__ import annotations

import datetime as dt
from urllib.parse import urlparse

from . import common as C

BEFORE_DAYS = 28


def path_of(url_or_path: str) -> str:
    p = urlparse(url_or_path).path if "://" in url_or_path else url_or_path
    return (p or "/").rstrip("/") or "/"


def load() -> dict:
    try:
        d = C.load_yaml("changes.yml")
    except FileNotFoundError:
        return {"hold_days": 28, "changes": []}
    out = []
    for c in d.get("changes") or []:
        try:
            day = c["date"] if isinstance(c["date"], dt.date) else dt.date.fromisoformat(str(c["date"]))
        except (KeyError, ValueError):
            continue
        kind = c.get("kind") or []
        out.append({"date": day, "page": "*" if str(c.get("page")) == "*" else path_of(str(c.get("page") or "/")),
                    "kind": kind if isinstance(kind, list) else [kind], "what": c.get("what", "")})
    return {"hold_days": int(d.get("hold_days", 28)), "changes": out}


def held_paths(today: dt.date | None = None, log: dict | None = None) -> set[str]:
    """Paths changed within hold_days (sitewide '*' entries never hold a page)."""
    log = log or load()
    today = today or C.today()
    cutoff = today - dt.timedelta(days=log["hold_days"])
    return {c["page"] for c in log["changes"] if c["page"] != "*" and c["date"] > cutoff}


def by_page(log: dict) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for c in sorted(log["changes"], key=lambda c: c["date"], reverse=True):
        out.setdefault(c["page"], []).append(c)
    return out


def _window(rows: list[dict], days: int) -> dict | None:
    if days <= 0:
        return None
    clicks = sum(r["clicks"] for r in rows)
    impr = sum(r["impressions"] for r in rows)
    pos = sum(r["position"] * r["impressions"] for r in rows) / impr if impr else None
    return {"days": days, "clicks": clicks, "impressions": impr,
            "ctr": round(clicks / impr, 4) if impr else None, "position": round(pos, 1) if pos else None,
            "clicks_per_day": round(clicks / days, 1), "impressions_per_day": round(impr / days, 1)}


def compare(before: dict | None, after: dict | None) -> dict:
    """Change in per-day clicks/impressions and in CTR/position (position: negative = better)."""
    if not before or not after:
        return {}
    pct = lambda a, b: round((a - b) / b, 3) if b else None  # noqa: E731
    return {"clicks_per_day": pct(after["clicks_per_day"], before["clicks_per_day"]),
            "impressions_per_day": pct(after["impressions_per_day"], before["impressions_per_day"]),
            "ctr_points": round((after["ctr"] - before["ctr"]) * 100, 2) if after["ctr"] is not None and before["ctr"] is not None else None,
            "position": round(after["position"] - before["position"], 1) if after["position"] and before["position"] else None}


def build(gsc=None, site: str = "", end: dt.date | None = None, today: dt.date | None = None) -> dict:
    """gsc: a seo.gsc.GSC client (or None: the list is written without numbers)."""
    log = load()
    today = today or C.today()
    end = end or today
    held = held_paths(today, log)
    watching, sitewide = [], []
    for page, entries in by_page(log).items():
        if page == "*":
            sitewide += [{"date": c["date"].isoformat(), "kind": c["kind"], "what": c["what"]} for c in entries]
            continue
        changed = entries[0]["date"]          # most recent change to this page
        row = {"page": page, "changed": changed.isoformat(), "days_since": (today - changed).days,
               "held": page in held, "held_until": (changed + dt.timedelta(days=log["hold_days"])).isoformat(),
               "changes": [{"date": c["date"].isoformat(), "kind": c["kind"], "what": c["what"]} for c in entries]}
        if gsc is not None:
            url = site.rstrip("/") + page
            b_start, b_end = changed - dt.timedelta(days=BEFORE_DAYS), changed - dt.timedelta(days=1)
            a_start = changed + dt.timedelta(days=1)
            try:
                filt = [{"dimension": "page", "operator": "equals", "expression": url}]
                rows = gsc.query(b_start, end, ["date"], filters=filt) if a_start <= end else \
                    gsc.query(b_start, b_end, ["date"], filters=filt)
                before = [r for r in rows if b_start.isoformat() <= r["date"] <= b_end.isoformat()]
                after = [r for r in rows if a_start.isoformat() <= r["date"] <= end.isoformat()]
                row["before"] = _window(before, BEFORE_DAYS)
                row["after"] = _window(after, (end - a_start).days + 1) if a_start <= end else None
                row["change"] = compare(row["before"], row["after"])
            except Exception as e:  # noqa: BLE001
                row["error"] = str(e)[:200]
        watching.append(row)
    watching.sort(key=lambda r: r["changed"], reverse=True)
    return {"updated": C.now_iso(), "hold_days": log["hold_days"], "data_through": end.isoformat(),
            "note": "Before = the 28 days before the change; after = the days since, up to the latest settled Search Console day. "
                    "Compare per-day numbers; a week or two after a change is still early.",
            "held_back": sorted(held), "watching": watching, "sitewide": sitewide}


def run(gsc=None, site: str = "", end: dt.date | None = None) -> dict:
    out = build(gsc, site, end)
    C.write_json("changes.json", out)
    return out
