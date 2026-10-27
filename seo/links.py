"""Internal links: where pages should link to each other but don't.

Weekly. No API key needed (Search Console data, when present, sets priorities).

1. Crawl every sitemap page and read its main content (breadcrumbs, menus,
   header and footer removed), noting which other pages it links to.
2. Give each page "names" a reader would use for its subject: the first part
   of its H1 ("Jacob Riis: The Photographer..." -> "Jacob Riis"), its slug
   ("square-deal" -> "square deal"), and any extra names in
   config/link_aliases.yml. Names shared by too many pages are dropped.
3. Wherever a page's text mentions another page's name without linking to it,
   that's a suggested link, with the sentence it belongs in.
4. Count inbound content links per page; flag orphans (none) and pages that
   are mentioned far more often than linked.
5. For the focus sections (default /tr), find pairs of pages about similar
   things (TF-IDF word overlap) with no link either way.

Priority favours links pointing at pages Google already shows (impressions),
especially those ranking 4-20, where an extra internal link helps most.

Writes links.json
"""
from __future__ import annotations

import math
import re
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from . import common as C

LEADING = re.compile(r"^(the|a|an)\s+", re.I)
SPLIT = re.compile(r"\s*(?::|\s[–—-]\s|\|)\s*")
GENERIC = {"overview", "home", "about", "history", "faq", "quotes", "timeline", "tickets", "visit", "events",
           "calendar", "podcast", "video", "videos", "photos", "gallery", "news", "press", "support", "donate"}


def path_of(url: str) -> str:
    return urlparse(url).path.rstrip("/") or "/"


def parse(html: str, url: str, host: str) -> dict:
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main") or soup.body or soup
    for t in main.find_all(["nav", "header", "footer", "aside", "script", "style", "noscript", "form"]):
        t.decompose()
    for t in main.select(".breadcrumb, [aria-label=breadcrumb], .visually-hidden"):
        t.decompose()
    h1 = main.find("h1")
    h1_text = h1.get_text(" ", strip=True) if h1 else (soup.title.get_text(" ", strip=True) if soup.title else "")
    links, raw = set(), {}
    for a in main.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith(("mailto:", "tel:", "javascript:", "#")):
            continue
        u = urljoin(url, href)
        pu = urlparse(u)
        if pu.scheme in ("http", "https") and pu.netloc.endswith(host):
            links.add(path_of(u))
            raw.setdefault(pu.path or "/", a.get_text(" ", strip=True)[:80])
        a.replace_with(" ⁣ ")   # mark link text as already-linked so it isn't matched again
    paras = []
    for el in main.find_all(["p", "li", "td", "blockquote"]):
        t = re.sub(r"\s+", " ", el.get_text(" ", strip=True))
        if len(t) > 20:
            paras.append(t)
    return {"h1": h1_text, "links": links, "raw_links": raw, "paras": list(dict.fromkeys(paras))}


def names_for(path: str, h1: str, suffix: str) -> list[str]:
    out = []
    if h1:
        h = h1.replace(suffix, "").strip()
        first = SPLIT.split(h)[0]
        for cand in (first, h if len(h.split()) <= 6 else None):
            if cand:
                out.append(LEADING.sub("", cand).strip(" .,'\""))
    slug = path.rsplit("/", 1)[-1]
    if "-" in slug and not re.search(r"\d", slug):
        out.append(slug.replace("-", " "))
    # a short slug name ("national park") is dropped when the H1 gives a more
    # specific name containing it ("Theodore Roosevelt National Park")
    out = [n for n in out if not any(n.lower() != o.lower() and n.lower() in o.lower() and len(o.split()) <= 6 for o in out[:-1])
           or n == out[0]]
    good = []
    for n in dict.fromkeys(out):
        words = n.split()
        if len(words) >= 2 and len(words) <= 7 and n.lower() not in GENERIC:
            good.append(n)
    return good


TITLES = {"the", "a", "an", "president", "governor", "commissioner", "colonel", "general", "senator", "mr", "mrs", "dr",
          "secretary", "assemblyman", "young", "old", "his", "her", "their", "our", "and", "of"}


def inside_longer_name(text: str, start: int) -> bool:
    """True when the match continues a longer proper noun, e.g. "Yosemite National
    Park" or "Indian Civil Service", so a short name shouldn't be linked there."""
    before = text[:start].rstrip()
    m = re.search(r"([A-Z][\w'’.-]*)$", before)
    if not m or before.endswith((".", "!", "?", ":", "—", "(", "\"", "“")):
        return False
    word = m.group(1).strip(".").lower()
    if word in TITLES:
        return False
    # previous word starts a sentence? then it's just capitalised, not part of a name
    pre = before[: m.start()].rstrip()
    return not (pre == "" or pre.endswith((".", "!", "?", ":", "\"", "“", "—")))


def continues_into_name(text: str, end: int) -> bool:
    """True when a capitalised word follows, e.g. "Bully Pulpit Golf Course"."""
    after = text[end:]
    m = re.match(r"\s+([A-Z][a-z]+)", after)
    return bool(m) and not after.startswith((",", ".", ";", ":"))


def snippet(text: str, start: int, end: int, width: int = 90) -> str:
    a, b = max(0, start - width), min(len(text), end + width)
    return ("…" if a else "") + text[a:start] + "[[" + text[start:end] + "]]" + text[end:b] + ("…" if b < len(text) else "")


def tfidf_pairs(docs: dict, linked: set, top: int = 100, min_sim: float = 0.25) -> list[dict]:
    """Similar pages with no link either way (cosine similarity on TF-IDF)."""
    toks = {p: Counter(w for w in C.content_words(t) if len(w) > 3) for p, t in docs.items()}
    df = Counter(w for c in toks.values() for w in c)
    n = len(toks)
    vec = {}
    for p, c in toks.items():
        v = {w: (1 + math.log(f)) * math.log(n / df[w]) for w, f in c.items() if df[w] < n * 0.5 and df[w] > 1}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1
        vec[p] = {w: x / norm for w, x in v.items()}
    paths = sorted(vec)
    out = []
    for i, a in enumerate(paths):
        va = vec[a]
        for b in paths[i + 1:]:
            if (a, b) in linked or (b, a) in linked:
                continue
            vb = vec[b]
            small, big = (va, vb) if len(va) < len(vb) else (vb, va)
            sim = sum(x * big.get(w, 0) for w, x in small.items())
            if sim >= min_sim:
                shared = sorted((w for w in small if w in big), key=lambda w: -(small[w] * big[w]))[:5]
                out.append({"a": a, "b": b, "similarity": round(sim, 3), "shared_words": shared})
    return sorted(out, key=lambda r: -r["similarity"])[:top]


# ---------- broken internal links -> 301 redirect suggestions ----------

def _slug_words(path: str) -> list[str]:
    return [w for w in re.split(r"[-_/.]+", path.lower()) if w and w not in ("html", "htm", "php", "index", "www")]


def suggest_redirect(broken: str, live: set, name_index: dict, titles: dict) -> dict:
    """Best live destination for a broken internal path, with a confidence level."""
    import difflib
    p = broken.split("?")[0].split("#")[0]
    # 0. ticket-store paths written without the store's domain (ACME lives on access.trlibrary.com)
    if re.match(r"^/(orders|events|checkout|auth|cart|forms)/\d+", p):
        return {"to": "https://access.trlibrary.com" + broken, "confidence": "high",
                "why": "ticket-store link missing its domain (access.trlibrary.com); better still, fix the link itself"}
    # 1. trivial variants: .html/.htm/.php, /index, trailing slash, case
    cand = re.sub(r"(/index)?(\.html?|\.php)?/?$", "", p, flags=re.I) or "/"
    for c in (cand, cand.lower()):
        if c in live and c != p:
            return {"to": c, "confidence": "high", "why": "same page without the file extension / trailing part"}
    # 1b. the last part of the address is exactly a live page's name somewhere else
    #     (/visit/tickets -> /tickets). Live pages outside the sitemap count too.
    last = cand.rsplit("/", 1)[-1].lower()
    if last and last not in ("overview", "index", "home", "main", "timeline"):
        # shortest address wins (a top-level /tickets beats /visit/faq/tickets), then same section
        same_name = sorted((x for x in live if x != cand and x.rsplit("/", 1)[-1].lower() == last),
                           key=lambda x: (x.count("/"), not x.startswith("/" + cand.strip("/").split("/")[0] + "/"), x))
        if same_name:
            clear = len(same_name) == 1 or same_name[0].count("/") < same_name[1].count("/")
            return {"to": same_name[0], "confidence": "high" if clear else "medium",
                    "why": "live page with the same name" + (f" (also: {', '.join(same_name[1:3])})" if len(same_name) > 1 else "")}
    # 2. "<section>/overview" or "<section>/index" -> the section's landing page
    parent = cand.rsplit("/", 1)[0] or "/"
    if cand.rsplit("/", 1)[-1] in ("overview", "index", "home", "main", "timeline") and parent in live:
        return {"to": parent, "confidence": "medium", "why": "section landing page"}
    # 3. slug names a subject we have a page for ("alice-roosevelt" -> Alice Roosevelt Longworth)
    words = " ".join(_slug_words(cand.rsplit("/", 1)[-1]))
    if words in name_index:
        return {"to": name_index[words][0], "confidence": "medium", "why": f"page about \"{words}\""}
    # 4. closest live URL in the same section by slug similarity
    sec = "/" + cand.strip("/").split("/")[0]
    pool = [x for x in live if x.startswith(sec)] or list(live)
    best = difflib.get_close_matches(cand.lower(), pool, n=1, cutoff=0.72)
    # only accept it if the last parts share a whole word (stops /tr/biography -> /tr/birthday)
    if best and not set(_slug_words(cand.rsplit("/", 1)[-1])) & set(_slug_words(best[0].rsplit("/", 1)[-1])):
        best = []
    if best:
        return {"to": best[0], "confidence": "medium" if difflib.SequenceMatcher(None, cand.lower(), best[0]).ratio() > 0.85 else "low",
                "why": f"closest address: {titles.get(best[0], '')[:60]}"}
    # 5. fall back to the nearest existing parent
    while parent not in live and parent != "/":
        parent = parent.rsplit("/", 1)[0] or "/"
    return {"to": parent, "confidence": "low", "why": "no matching page; nearest section (or remove the link / create the page)"}


def check_paths(sess, base: str, paths: list[str], workers: int = 6) -> dict:
    """Live status for internal paths that aren't in the sitemap."""
    def one(p):
        try:
            r = sess.get(urljoin(base, p), timeout=20, allow_redirects=True)
            return p, {"status": r.status_code, "final": path_of(r.url), "redirected": bool(r.history)}
        except Exception as e:  # noqa: BLE001
            return p, {"status": 599, "error": str(e)[:100]}
    with ThreadPoolExecutor(max_workers=workers) as ex:
        return dict(ex.map(one, paths))


def linkchecker_external(url: str, video_pattern: str) -> dict | None:
    """External broken links from the LinkChecker tool (links.labs.trlibrary.com)."""
    try:
        r = C.session().get(url, timeout=60)
        r.raise_for_status()
        d = r.json()
    except Exception as e:  # noqa: BLE001
        return {"error": f"LinkChecker results unavailable: {e}"[:200]}
    vid = re.compile(video_pattern)
    rows = []
    for kind in ("broken_links", "warning_links"):
        for x in d.get(kind, []):
            if x.get("internal"):
                continue
            srcs = [s.get("page") if isinstance(s, dict) else s for s in x.get("sources", [])]
            rows.append({"url": x.get("url"), "status": x.get("status"), "error": x.get("error"),
                         "kind": "broken" if kind == "broken_links" else "warning",
                         "sources": [path_of(u) for u in srcs if u][:10],
                         "from_video_pages": all(vid.search(path_of(u)) for u in srcs if u) and bool(srcs)})
    rows.sort(key=lambda r: (r["from_video_pages"], r["kind"] != "broken", -len(r["sources"])))
    return {"generated_at": d.get("generated_at"), "pages_crawled": (d.get("summary") or {}).get("pages_crawled"),
            "external": rows, "internal_reported": sum(1 for x in d.get("broken_links", []) if x.get("internal"))}


def run() -> None:
    cfg = C.config()
    lc = cfg.get("links", {})
    site = cfg["site"]["url"]
    host = C.domain_of(site)
    suffix = cfg.get("audit", {}).get("title_suffix", "").strip(" |")
    excl = [re.compile(p) for p in lc.get("exclude_patterns", [])]
    focus = lc.get("focus_sections", ["/tr"])
    alias_cfg = C.load_yaml("link_aliases.yml") if (C.CONFIG_DIR / "link_aliases.yml").exists() else {}
    aliases = alias_cfg.get("aliases", {}) or {}
    never = {n.lower() for n in alias_cfg.get("never_link", []) or []}

    from .audit import sitemap_urls
    sess = C.session(cfg.get("audit", {}).get("user_agent"))
    try:
        all_urls = list(dict.fromkeys(sitemap_urls(sess, cfg["site"]["sitemap"])))
    except Exception as e:  # noqa: BLE001
        C.set_status("links", "error", f"sitemap: {e}"[:300])
        raise C.JobError(str(e)) from e

    def fetch(u):
        try:
            r = sess.get(u, timeout=25)
            if r.status_code < 400 and "html" in r.headers.get("content-type", ""):
                return path_of(r.url), parse(r.text, r.url, host)
        except Exception:  # noqa: BLE001
            pass
        return path_of(u), None
    with ThreadPoolExecutor(max_workers=cfg.get("audit", {}).get("workers", 6)) as ex:
        all_pages = {p: d for p, d in ex.map(fetch, all_urls) if d}
    live = {path_of(u) for u in all_urls} | set(all_pages)
    # link suggestions only for content pages (not video, quiz, calendar...)
    pages = {p: d for p, d in all_pages.items() if not any(x.search(p) for x in excl)}

    # Search Console: impressions and position per page (for priority)
    gsc = {}
    for r in C.read_json("gsc/pages.json", []) or []:
        gsc[path_of(r["page"])] = r

    # ---- names -> target pages ----
    by_name = defaultdict(list)
    for p, d in pages.items():
        for n in names_for(p, d["h1"], suffix) + list(aliases.get(p, []) or []):
            if n.lower() not in never:
                by_name[n.lower()].append(p)
    unknown_aliases = [p for p in aliases if p not in pages]
    def section(p):
        return "/" + p.strip("/").split("/")[0] if p != "/" else "/"
    duplicates = []
    name_target = {}       # name -> candidate pages, best first
    for n, ps in by_name.items():
        ps = sorted(dict.fromkeys(ps), key=lambda p: (-(gsc.get(p, {}).get("impressions") or 0), len(p)))
        name_target[n] = ps
        # two pages in the same section about the same subject = likely duplicate content
        per_sec = defaultdict(list)
        for p in ps:
            per_sec[section(p)].append(p)
        for sec_pages in per_sec.values():
            if len(sec_pages) > 1:
                duplicates.append({"name": n, "pages": sec_pages,
                                   "impressions": [gsc.get(p, {}).get("impressions") for p in sec_pages]})

    def resolve(name, source):
        """Same name, different pages (TR's son Kermit vs a trustee named Kermit):
        prefer the page in the source's own section, else the best-performing one."""
        cands = name_target[name]
        same = [c for c in cands if section(c) == section(source)]
        return (same or cands)[0]

    # ---- broken internal links (every page, including video/quiz/calendar) ----
    unknown = defaultdict(list)       # raw path -> [(source, link text)]
    for p, d in all_pages.items():
        for raw_path, text in d["raw_links"].items():
            if path_of(raw_path) not in live and not re.search(r"\.(pdf|jpe?g|png|gif|webp|svg|docx?|xlsx?|zip|mp3|mp4)$|^/(sites|system|user|admin|core|themes|modules)/", raw_path, re.I):
                unknown[raw_path].append((p, text))
    # live pages that aren't in the sitemap (e.g. /tickets): known extras plus any linked path that works
    extra = [p for p in lc.get("extra_live_paths", ["/tickets", "/donate", "/membership", "/search"]) if p not in live]
    status = check_paths(sess, site, sorted(set(unknown) | set(extra))[: lc.get("max_unknown_links_checked", 600) + len(extra)])
    live_extra = {path_of(p) for p, st in status.items() if st.get("status") == 200 and not st.get("redirected")} | \
                 {st["final"] for st in status.values() if st.get("status") == 200 and st.get("final")}
    live = live | live_extra
    titles = {p: d["h1"] for p, d in all_pages.items()}
    name_index = {n: v for n, v in name_target.items()}
    broken, via_redirect = [], []
    for raw_path, srcs in unknown.items():
        st = status.get(raw_path)
        if not st:
            continue
        if st["status"] >= 400:
            sug = suggest_redirect(raw_path, live, name_index, titles)
            if st["status"] in (401, 403):
                sug["why"] = "access denied: probably an unpublished page that is still linked. Publish it, or redirect: " + sug["why"]
            broken.append({"broken": raw_path, "status": st["status"], "redirect_to": sug["to"], "confidence": sug["confidence"],
                           "why": sug["why"], "to_title": titles.get(sug["to"], ""),
                           "sources": [{"page": s, "link_text": t} for s, t in srcs][:15], "source_count": len(srcs)})
        elif st.get("redirected") and st.get("final") != path_of(raw_path):
            via_redirect.append({"link": raw_path, "goes_to": st["final"], "sources": [s for s, _ in srcs][:10]})
    conf_rank = {"high": 0, "medium": 1, "low": 2}
    broken.sort(key=lambda b: (conf_rank[b["confidence"]], -b["source_count"]))
    with open(C.data_path("redirects.csv"), "w", encoding="utf-8") as fh:
        # Drupal Redirect module import format (redirect_import): source,destination,language,status_code
        fh.write("source,destination,language,status_code,confidence\n")
        for b in broken:
            dest = b["redirect_to"] if b["redirect_to"].startswith("http") else "internal:" + b["redirect_to"]
            fh.write(f"{b['broken'].lstrip('/')},{dest},und,301,{b['confidence']}\n")
    ext = linkchecker_external(lc.get("linkchecker_results", "https://links.labs.trlibrary.com/results.json"),
                               lc.get("video_pattern", r"^/video/")) if lc.get("linkchecker_results", True) else None

    # drop names that turn up on too many pages (too generic to link)
    docs = {p: " ".join(d["paras"]) for p, d in pages.items()}
    max_share = lc.get("max_phrase_share", 0.2)
    if name_target:
        big = re.compile(r"(?<![\w-])(" + "|".join(sorted(map(re.escape, name_target), key=len, reverse=True)) + r")(?![\w-])", re.I)
        seen_on = Counter()
        for p, t in docs.items():
            for n in {m.group(1).lower() for m in big.finditer(t)}:
                seen_on[n] += 1
        too_common = {n for n, c in seen_on.items() if c > max(5, max_share * len(docs))}
        for n in too_common:
            name_target.pop(n, None)
    else:
        too_common = set()

    # ---- missing links ----
    inlinks = Counter()
    for p, d in pages.items():
        for t in d["links"]:
            if t != p and t in pages:
                inlinks[t] += 1
    suggestions = []
    mentions = Counter()
    if name_target:
        rx = re.compile(r"(?<![\w-])(" + "|".join(sorted(map(re.escape, name_target), key=len, reverse=True)) + r")(?![\w-])", re.I)
        per_source = lc.get("max_suggestions_per_source", 10)
        for p, d in pages.items():
            found = {}
            for para in d["paras"]:
                if para.lstrip().startswith("\u2063"):
                    continue      # a "related links" list item: already a link
                for m in rx.finditer(para):
                    if inside_longer_name(para, m.start()) or continues_into_name(para, m.end()):
                        continue
                    target = resolve(m.group(1).lower(), p)
                    if target == p or target in d["links"] or target in found:
                        continue
                    found[target] = (m.group(1), snippet(para, m.start(), m.end()))
                    mentions[target] += 1
            for target, (phrase, snip) in list(found.items()):
                g = gsc.get(target, {})
                impr, pos = g.get("impressions") or 0, g.get("position")
                score = 1 + math.log10(impr + 1)
                if pos and 4 <= pos <= 20:
                    score *= 1.5              # a nudge here can move it onto page one / into the top 3
                if any(target.startswith(f) for f in focus):
                    score *= 1.2
                if inlinks[target] <= 1:
                    score *= 1.3              # barely linked pages benefit most
                src_impr = (gsc.get(p, {}).get("impressions") or 0)
                score *= 1 + 0.2 * math.log10(src_impr + 1)
                suggestions.append({"source": p, "target": target, "target_title": pages[target]["h1"], "phrase": phrase,
                                    "snippet": snip, "score": round(score, 2), "target_impressions": impr,
                                    "target_position": pos, "target_inlinks": inlinks[target]})
        # cap per source page, keep the strongest
        kept, per = [], Counter()
        for s in sorted(suggestions, key=lambda s: -s["score"]):
            if per[s["source"]] < per_source:
                kept.append(s)
                per[s["source"]] += 1
        suggestions = kept

    # ---- inbound link table / orphans ----
    table = []
    for p, d in pages.items():
        g = gsc.get(p, {})
        table.append({"page": p, "title": d["h1"], "inlinks": inlinks[p], "outlinks": len([t for t in d["links"] if t in pages and t != p]),
                      "unlinked_mentions": mentions[p], "impressions": g.get("impressions"), "position": g.get("position"),
                      "section": section(p)})
    orphans = sorted([r for r in table if r["inlinks"] == 0 and r["page"] != "/"], key=lambda r: -(r["impressions"] or 0))

    # ---- related pages with no link either way (focus sections) ----
    linked = {(p, t) for p, d in pages.items() for t in d["links"]}
    related = []
    for f in focus:
        fdocs = {p: t for p, t in docs.items() if p.startswith(f) and len(t) > 400}
        related += tfidf_pairs(fdocs, linked, top=lc.get("related_pairs", 80))
    for r in related:
        r["a_title"], r["b_title"] = pages[r["a"]]["h1"], pages[r["b"]]["h1"]

    by_section = defaultdict(lambda: {"pages": 0, "inlinks": 0, "orphans": 0, "suggestions": 0})
    for r in table:
        s = by_section[r["section"]]
        s["pages"] += 1
        s["inlinks"] += r["inlinks"]
        s["orphans"] += r["inlinks"] == 0
    for s in suggestions:
        by_section[section(s["source"])]["suggestions"] += 1
    sections = sorted(({"section": k, **v, "avg_inlinks": round(v["inlinks"] / v["pages"], 1)} for k, v in by_section.items()),
                      key=lambda r: -r["pages"])

    out = {
        "updated": C.now_iso(),
        "focus_sections": focus,
        "summary": {"pages": len(pages), "suggestions": len(suggestions), "orphans": len(orphans),
                    "names_tracked": len(name_target), "names_too_common": len(too_common),
                    "duplicate_topics": len(duplicates),
                    "avg_inlinks": round(sum(inlinks.values()) / max(1, len(pages)), 1)},
        "suggestions": suggestions[:600],
        "orphans": orphans[:200],
        "pages": sorted(table, key=lambda r: (r["inlinks"], -(r["impressions"] or 0)))[:1500],
        "related_unlinked": related,
        "duplicate_topics": sorted(duplicates, key=lambda d: -sum(x or 0 for x in d["impressions"]))[:100],
        "sections": sections,
        "unknown_alias_pages": unknown_aliases,
        "broken_internal": broken,
        "links_through_redirects": via_redirect[:200],
        "external": ext,
    }
    out["summary"].update(broken_internal=len(broken), broken_internal_instances=sum(b["source_count"] for b in broken),
                          redirects_high_confidence=sum(1 for b in broken if b["confidence"] == "high"),
                          external_broken=sum(1 for r in (ext or {}).get("external", []) if r["kind"] == "broken" and not r["from_video_pages"]),
                          external_broken_video=sum(1 for r in (ext or {}).get("external", []) if r["kind"] == "broken" and r["from_video_pages"]),
                          linkchecker_scan=(ext or {}).get("generated_at"))
    C.write_json("links.json", out)
    C.set_status("links", "ok", f"{len(all_pages)} pages crawled; {len(broken)} broken internal links (redirects proposed); "
                 f"{len(suggestions)} suggested links; {len(orphans)} orphan pages; {len(related)} related pairs without links")


if __name__ == "__main__":
    run()
