"""Why AI assistants answer the way they do.

Two analyses on top of the weekly AI answers (seo/ai_visibility.py):

1. Fan-out searches. Before answering, ChatGPT, Claude, Gemini (and sometimes
   Perplexity) run their own web searches. Those searches decide which pages
   get read and cited. We keep them and look each one up in Search Console:
   if trlibrary.com doesn't rank for the search the assistant ran, it's unlikely
   to be the page the assistant reads. No extra API calls.

2. Sources cited when the Library is missing. For "gap" answers (another
   attraction named, the Library not), each cited source is sorted by type:
   our own page, a list or travel guide, a review or booking site, a forum,
   a reference site, news, a partner, or another attraction's own site. For
   the most-cited outside pages we read the page once and check whether it
   mentions the Library. Each type points to a different fix: get added to
   the list, improve our page, answer the forum thread, or write the page
   that's missing.
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

from . import common as C

# Domain -> type. Matched on the end of the hostname. config/site.yml
# ai_visibility.source_types adds to or overrides these.
DOMAIN_TYPES = {
    "wikipedia.org": "reference", "britannica.com": "reference", "nps.gov": "reference", "loc.gov": "reference",
    "si.edu": "reference", "history.com": "reference", "theodorerooseveltcenter.org": "reference",
    "theodoreroosevelt.org": "reference", "whitehouse.gov": "reference", "millercenter.org": "reference",
    "archives.gov": "reference", "wikidata.org": "reference", "nd.gov": "reference", "ndstudies.gov": "reference",
    "reddit.com": "forum", "quora.com": "forum", "stackexchange.com": "forum",
    "tripadvisor.com": "review or booking", "yelp.com": "review or booking", "expedia.com": "review or booking",
    "booking.com": "review or booking", "viator.com": "review or booking", "getyourguide.com": "review or booking",
    "google.com": "review or booking", "airbnb.com": "review or booking", "hotels.com": "review or booking",
    "facebook.com": "social", "instagram.com": "social", "youtube.com": "social", "tiktok.com": "social", "x.com": "social",
    "nytimes.com": "news", "washingtonpost.com": "news", "apnews.com": "news", "cnn.com": "news", "foxnews.com": "news",
    "usatoday.com": "news", "npr.org": "news", "bismarcktribune.com": "news", "inforum.com": "news",
    "thedickinsonpress.com": "news", "kfyrtv.com": "news", "smithsonianmag.com": "news",
    "crazyhorsememorial.org": "attraction", "walldrug.com": "attraction", "medoramusical.com": "attraction",
    "nationalcowboymuseum.org": "attraction", "ndcowboy.org": "attraction",
    "ndtourism.com": "partner", "medora.com": "partner", "travelnorthdakota.com": "partner",
}
LIST_PATH = re.compile(r"(best|top-?\d*|things-to-do|must-see|guide|itinerary|road-?trip|day-trip|bucket|hidden-gems|places-to)", re.I)
TYPE_ACTION = {
    "list or guide": "Ask to be added: find the author or an update/contact link; offer a short blurb and a photo.",
    "review or booking": "Keep the Library's listing complete and current on this site (photos, hours, description, category).",
    "forum": "Answer helpfully where the community allows it, as the Library, with a link only when it answers the question.",
    "reference": "Make sure the facts there are right; for Wikipedia, suggest edits on the talk page with sources (no self-promotion).",
    "news": "Pitch a story or update; news pages that list attractions get reused by AI answers for months.",
    "partner": "Ask the partner to name and link the Library on this page.",
    "attraction": "No action on their page. Check that our own page answers the same question as well.",
    "owned": "Our page is being read. Make sure it answers the question near the top.",
    "social": "Low priority: AI rarely relies on social pages for recommendations.",
    "other": "Read the page: if it's a list of things to do, ask to be added.",
}


def _norm(q: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s']", " ", (q or "").lower())).strip()


def _host(u: str) -> str:
    h = (urlparse(u).hostname or "").lower()
    return h[4:] if h.startswith("www.") else h


def source_type(url: str, our_domain: str, peer_domains: dict, overrides: dict) -> str:
    host = _host(url)
    if not host:
        return "other"
    if host.endswith(our_domain):
        return "owned"
    table = {**DOMAIN_TYPES, **(overrides or {})}
    for dom, typ in sorted(table.items(), key=lambda kv: -len(kv[0])):
        if host == dom or host.endswith("." + dom):
            return typ
    for dom in peer_domains:
        if host == dom or host.endswith("." + dom):
            return "attraction"
    path = urlparse(url).path
    if host.endswith(".gov") or host.endswith(".edu"):
        return "reference"
    if LIST_PATH.search(path):
        return "list or guide"
    return "other"


def _gap(r: dict) -> bool:
    return not r.get("error") and not r.get("mentioned")


def fanout(results: list[dict], prompts: list[dict], gsc_queries: list[dict], labels: dict) -> dict:
    """Every search an assistant ran, with where trlibrary.com ranks for it in Google."""
    gsc_exact = {_norm(q["query"]): q for q in gsc_queries if q.get("query")}
    gsc_words = defaultdict(list)
    for q in gsc_queries:
        if q.get("query"):
            gsc_words[frozenset(C.content_words(q["query"]))].append(q)
    ptext = {p["id"]: p["text"] for p in prompts}
    rows: dict = {}
    for r in results:
        for q in r.get("searches") or []:
            k = _norm(q)
            if not k:
                continue
            row = rows.setdefault(k, {"search": q.strip(), "engines": set(), "questions": set(), "times": 0, "in_gap_answers": 0})
            row["engines"].add(labels.get(r["provider"], r["provider"]))
            row["questions"].add(r["prompt_id"])
            row["times"] += 1
            row["in_gap_answers"] += 1 if _gap(r) else 0
    out = []
    for k, row in rows.items():
        g, how = gsc_exact.get(k), "exact"
        if not g:
            cands = gsc_words.get(frozenset(C.content_words(k))) or []
            g, how = (max(cands, key=lambda x: x.get("impressions", 0)), "same words") if cands else (None, None)
        out.append({
            "search": row["search"], "engines": sorted(row["engines"]), "times": row["times"],
            "questions": [ptext.get(i, i) for i in sorted(row["questions"])], "in_gap_answers": row["in_gap_answers"],
            "google": ({"query": g["query"], "position": g.get("position"), "impressions": g.get("impressions"),
                        "clicks": g.get("clicks"), "match": how} if g else None),
        })
    out.sort(key=lambda x: (-x["in_gap_answers"], -x["times"], x["search"]))
    ranked = [x for x in out if x["google"]]
    return {
        "note": "Searches the assistants ran before answering. 'Google' is trlibrary.com's Search Console position for the same "
                "search (last 28 days); none means the site doesn't show for it, or too rarely to report. A search we don't rank "
                "for is a page to strengthen or write.",
        "answers_with_searches": sum(1 for r in results if r.get("searches")),
        "searches": out[:200],
        "summary": {"unique": len(out), "we_rank_top10": sum(1 for x in ranked if (x["google"]["position"] or 99) <= 10),
                    "we_rank_lower": sum(1 for x in ranked if (x["google"]["position"] or 99) > 10),
                    "not_ranking": len(out) - len(ranked)},
    }


def _page_mentions(sess, url: str, brand_re) -> bool | None:
    try:
        r = sess.get(url, timeout=20, allow_redirects=True)
        if r.status_code != 200 or "html" not in r.headers.get("content-type", ""):
            return None
        return bool(brand_re.search(re.sub(r"<[^>]+>", " ", r.text)))
    except Exception:  # noqa: BLE001
        return None


def gap_sources(results: list[dict], prompts: list[dict], brand_re, our_domain: str, cfg: dict, sess, labels: dict,
                read_pages: int = 15) -> dict:
    """Sources cited in answers that leave the Library out."""
    av = cfg.get("ai_visibility", {}) or {}
    overrides = av.get("source_types") or {}
    peer_domains = {d: name for name, d in (av.get("peer_domains") or {}).items()} if isinstance(av.get("peer_domains"), dict) else {}
    gaps = [r for r in results if _gap(r)]
    ptext = {p["id"]: p["text"] for p in prompts}
    by_url: dict = {}
    for r in gaps:
        for u in dict.fromkeys(r.get("citations") or []):
            if not u.startswith("http"):
                continue
            pu = urlparse(u)
            q = "&".join(x for x in pu.query.split("&") if x and not x.lower().startswith(("utm_", "srsltid=")))
            key = f"{pu.scheme}://{pu.netloc}{pu.path}".rstrip("/") + (f"?{q}" if q else "")
            row = by_url.setdefault(key, {"url": key, "domain": _host(key), "answers": 0, "engines": set(), "questions": set(),
                                          "attractions_named": Counter()})
            row["answers"] += 1
            row["engines"].add(labels.get(r["provider"], r["provider"]))
            row["questions"].add(ptext.get(r["prompt_id"], r["prompt_id"]))
            row["attractions_named"].update(r.get("peers") or [])
    rows = sorted(by_url.values(), key=lambda x: -x["answers"])
    for row in rows:
        row["type"] = source_type(row["url"], our_domain, peer_domains, overrides)
    to_read = [row for row in rows if row["type"] not in ("owned", "attraction", "social")][:read_pages]
    with ThreadPoolExecutor(max_workers=6) as ex:
        for row, hit in zip(to_read, ex.map(lambda x: _page_mentions(sess, x["url"], brand_re), to_read)):
            row["mentions_library"] = hit
    by_type = Counter()
    for row in rows:
        by_type[row["type"]] += row["answers"]
    out_rows = [{"url": r["url"], "domain": r["domain"], "type": r["type"], "answers": r["answers"],
                 "engines": sorted(r["engines"]), "questions": sorted(r["questions"])[:5],
                 "attractions_named": [n for n, _ in r["attractions_named"].most_common(4)],
                 "mentions_library": r.get("mentions_library"), "action": TYPE_ACTION.get(r["type"], TYPE_ACTION["other"])}
                for r in rows[:60]]
    return {
        "note": "Pages cited in answers that left the Library out. 'Mentions the Library' comes from "
                "reading the page once (blank = not read or couldn't be read). A list that names other attractions but not the "
                "Library is the cheapest fix: ask to be added.",
        "gap_answers": len(gaps),
        "by_type": dict(by_type.most_common()),
        "type_actions": TYPE_ACTION,
        "sources": out_rows,
        "add_us_targets": [r for r in out_rows if r["type"] in ("list or guide", "news", "partner", "other")
                           and r.get("mentions_library") is False][:15],
    }
