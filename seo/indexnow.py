"""IndexNow: tell Bing (and the other IndexNow engines) the moment a page changes.

Bing's index feeds Microsoft Copilot and much of ChatGPT's web search, so a
changed page can show up in AI answers days sooner. Google doesn't use IndexNow.

Setup (once, by FiveJars or in Drupal): install the IndexNow module, or serve a
key file at https://www.trlibrary.com/<key>.txt whose content is the key.
Then put the key in config/site.yml (indexnow.key). It isn't secret: the
protocol publishes it on the site.

Daily: every page listed in config/changes.yml in the last few days is
submitted once. Writes indexnow.json (what was sent, and when).
No-op until the key is set and its file is live.
"""
from __future__ import annotations

import datetime as dt

from . import changes as CH, common as C

ENDPOINTS = ["https://api.indexnow.org/indexnow", "https://www.bing.com/indexnow"]


def pending(log: dict, sent: set[str], today: dt.date, days: int, site: str) -> list[str]:
    cutoff = today - dt.timedelta(days=days)
    out = []
    for c in log["changes"]:
        if c["page"] == "*" or c["date"] < cutoff:
            continue
        url = site.rstrip("/") + c["page"]
        key = f"{c['date'].isoformat()} {url}"
        if key not in sent:
            out.append(url)
    return list(dict.fromkeys(out))


def run() -> None:
    cfg = C.config()
    ix = cfg.get("indexnow") or {}
    key = (ix.get("key") or "").strip()
    site = cfg["site"]["url"]
    if not key:
        C.set_status("indexnow", "skipped", "No IndexNow key yet: see the work queue task 'Turn on IndexNow'.")
        return
    sess = C.session()
    key_url = f"{site.rstrip('/')}/{key}.txt"
    r = sess.get(key_url, timeout=20)
    if r.status_code != 200 or r.text.strip() != key:
        C.set_status("indexnow", "error", f"Key file {key_url} isn't live (HTTP {r.status_code}); nothing submitted.")
        return
    state = C.read_json("indexnow.json", {}) or {}
    sent = set(state.get("sent_keys", []))
    log = CH.load()
    today = C.today()
    urls = pending(log, sent, today, int(ix.get("days", 3)), site)
    if not urls:
        C.set_status("indexnow", "ok", "Nothing new to submit")
        return
    body = {"host": C.domain_of(site), "key": key, "keyLocation": key_url, "urlList": urls[:10000]}
    res = None
    for ep in ENDPOINTS:
        try:
            res = sess.post(ep, json=body, timeout=20)
        except Exception as e:  # noqa: BLE001
            res = None
            err = str(e)
            continue
        if res.status_code in (200, 202):
            break
    if res is None or res.status_code not in (200, 202):
        C.set_status("indexnow", "error", f"IndexNow refused the submission: {res.status_code if res is not None else err}")
        return
    cutoff = today - dt.timedelta(days=int(ix.get("days", 3)))
    for c in log["changes"]:
        if c["page"] != "*" and c["date"] >= cutoff:
            sent.add(f"{c['date'].isoformat()} {site.rstrip('/') + c['page']}")
    hist = (state.get("history") or [])[-200:] + [{"date": today.isoformat(), "urls": urls, "status": res.status_code}]
    C.write_json("indexnow.json", {"updated": C.now_iso(), "sent_keys": sorted(sent)[-2000:], "history": hist})
    C.set_status("indexnow", "ok", f"Submitted {len(urls)} changed page(s) to IndexNow")
