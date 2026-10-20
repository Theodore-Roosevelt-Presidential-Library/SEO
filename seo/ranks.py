"""Keyword rank tracking.

Always: matches the tracked keywords in config/keywords.yml against Search
Console (free, real data for our own site).
With DATAFORSEO_LOGIN + DATAFORSEO_PASSWORD: also pulls the live Google
results page for each keyword (who ranks above us, whether an AI Overview
appears and whether it cites trlibrary.com) and monthly search volumes.

Writes:
  ranks/latest.json   one row per tracked keyword
  ranks/history.json  weekly rank snapshots
  ranks/volumes.json  cached search volumes
"""
from __future__ import annotations

import datetime as dt

from . import common as C

DFS = "https://api.dataforseo.com/v3"


def tracked_keywords() -> list[dict]:
    groups = C.load_yaml("keywords.yml").get("groups", {})
    out, seen = [], set()
    for g, kws in groups.items():
        for k in kws or []:
            k = str(k).strip().lower()
            if k and k not in seen:
                seen.add(k)
                out.append({"keyword": k, "group": g})
    # plus keywords the system discovered (see seo/curate.py, config/tracking.yml)
    from .curate import active_keywords
    for k in active_keywords():
        if k["keyword"] not in seen:
            seen.add(k["keyword"])
            out.append({"keyword": k["keyword"], "group": k.get("group", "Auto: Discovered"), "auto": True})
    return out


def parse_serp(result: dict, our_domain: str) -> dict:
    items = result.get("items") or []
    organic = [i for i in items if i.get("type") == "organic"]
    ours = next((i for i in organic if C.domain_of(i.get("url", "")).endswith(our_domain)), None)
    aio = next((i for i in items if i.get("type") == "ai_overview"), None)
    aio_refs = []
    if aio:
        for ref in aio.get("references") or []:
            aio_refs.append(C.domain_of(ref.get("url", "")) or ref.get("domain", ""))
        for sub in aio.get("items") or []:
            for ref in sub.get("references") or []:
                aio_refs.append(C.domain_of(ref.get("url", "")) or ref.get("domain", ""))
    return {
        "rank": ours.get("rank_group") if ours else None,
        "url": ours.get("url") if ours else None,
        "top": [
            {"rank": i.get("rank_group"), "domain": C.domain_of(i.get("url", "")), "url": i.get("url"), "title": i.get("title")}
            for i in organic[:10]
        ],
        "features": sorted({i.get("type") for i in items if i.get("type") != "organic"}),
        "ai_overview": bool(aio),
        "ai_overview_cites_us": any(r.endswith(our_domain) for r in aio_refs),
        "ai_overview_sources": sorted(set(r for r in aio_refs if r))[:15],
    }


def _dfs_post(sess, path: str, payload: list) -> dict:
    r = sess.post(f"{DFS}{path}", json=payload, timeout=120)
    r.raise_for_status()
    data = r.json()
    if data.get("status_code") != 20000:
        raise RuntimeError(f"DataForSEO: {data.get('status_message')}")
    task = (data.get("tasks") or [{}])[0]
    if task.get("status_code") != 20000:
        raise RuntimeError(f"DataForSEO task: {task.get('status_message')}")
    return task


def refresh_volumes(sess, keywords: list[str], rcfg: dict) -> dict:
    cache = C.read_json("ranks/volumes.json", {}) or {}
    fetched = cache.get("fetched")
    fresh = fetched and (C.today() - dt.date.fromisoformat(fetched)).days < rcfg.get("volume_refresh_days", 30)
    missing = [k for k in keywords if k not in cache.get("volumes", {})]
    if fresh and not missing:
        return cache["volumes"]
    task = _dfs_post(sess, "/keywords_data/google_ads/search_volume/live", [{
        "keywords": keywords, "location_code": rcfg.get("location_code", 2840),
        "language_code": rcfg.get("language_code", "en"),
    }])
    vols = {r["keyword"].lower(): r.get("search_volume") for r in task.get("result") or []}
    C.write_json("ranks/volumes.json", {"fetched": C.today().isoformat(), "volumes": vols})
    return vols


def run() -> None:
    cfg = C.config()
    rcfg = cfg.get("ranks", {})
    our = C.domain_of(cfg["site"]["url"])
    kws = tracked_keywords()
    gsc_q = {r["query"].lower(): r for r in (C.read_json("gsc/queries.json", []) or [])}

    login, pw = C.env("DATAFORSEO_LOGIN"), C.env("DATAFORSEO_PASSWORD")
    sess = None
    vols: dict = (C.read_json("ranks/volumes.json", {}) or {}).get("volumes", {})
    errors = []
    if login and pw:
        sess = C.session()
        sess.auth = (login, pw)
        try:
            vols = refresh_volumes(sess, [k["keyword"] for k in kws], rcfg)
        except Exception as e:  # noqa: BLE001
            errors.append(f"volumes: {e}")

    rows = []
    for k in kws:
        g = gsc_q.get(k["keyword"])
        row = {
            **k,
            "volume": vols.get(k["keyword"]),
            "gsc": {"position": g["position"], "clicks": g["clicks"], "impressions": g["impressions"]} if g else None,
            "serp": None,
        }
        if sess:
            try:
                task = _dfs_post(sess, "/serp/google/organic/live/advanced", [{
                    "keyword": k["keyword"], "location_code": rcfg.get("location_code", 2840),
                    "language_code": rcfg.get("language_code", "en"), "depth": rcfg.get("depth", 30),
                    "device": "desktop",
                }])
                row["serp"] = parse_serp((task.get("result") or [{}])[0], our)
            except Exception as e:  # noqa: BLE001
                errors.append(f"{k['keyword']}: {e}")
        rows.append(row)

    C.write_json("ranks/latest.json", {"updated": C.now_iso(), "source": "dataforseo+gsc" if sess else "gsc", "keywords": rows})
    C.upsert_history("ranks/history.json", {
        "date": C.today().isoformat(),
        "serp": {r["keyword"]: (r["serp"] or {}).get("rank") for r in rows} if sess else {},
        "gsc": {r["keyword"]: (r["gsc"] or {}).get("position") for r in rows},
    })
    if not sess:
        C.set_status("ranks", "skipped", "Showing Search Console positions only. Add DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD for live Google results.")
    elif errors:
        C.set_status("ranks", "error", "; ".join(errors)[:400])
        raise C.JobError("ranks had errors")
    else:
        C.set_status("ranks", "ok", f"{len(rows)} keywords checked")


if __name__ == "__main__":
    run()
