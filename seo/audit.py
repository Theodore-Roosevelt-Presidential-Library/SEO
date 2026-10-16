"""Site audit: crawls every URL in the sitemap and checks on-page SEO and
AI-readiness basics. No API key needed.

Writes:
  audit/pages.json    one row per URL: facts + issues
  audit/summary.json  health score, issue counts, site-wide checks
  audit/history.json  health score over time
"""
from __future__ import annotations

import re
import time
import urllib.robotparser
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from . import common as C

SEVERITY_WEIGHT = {"high": 25, "medium": 10, "low": 3}

ISSUE_TEXT = {
    "http_error": ("high", "Page returns an error status"),
    "noindex": ("high", "Page is in the sitemap but tells search engines not to index it"),
    "title_missing": ("high", "No <title>"),
    "redirect_in_sitemap": ("medium", "Sitemap lists a URL that redirects"),
    "unaliased_url": ("medium", "Sitemap lists a /node/ URL instead of a readable path"),
    "title_duplicate": ("medium", "Same title as another page"),
    "meta_missing": ("medium", "No meta description"),
    "h1_missing": ("medium", "No H1 heading"),
    "canonical_mismatch": ("medium", "Canonical tag points to a different URL"),
    "og_missing": ("medium", "Missing Open Graph tags"),
    "title_too_long": ("low", "Title over 60 characters, not counting the site-name suffix"),
    "title_too_short": ("low", "Title under 15 characters, not counting the site-name suffix"),
    "meta_too_long": ("low", "Meta description over 160 characters"),
    "meta_too_short": ("low", "Meta description under 70 characters"),
    "meta_duplicate": ("low", "Same meta description as another page"),
    "h1_multiple": ("low", "More than one H1"),
    "canonical_missing": ("low", "No canonical tag"),
    "img_alt_missing": ("low", "Images without alt text"),
    "thin_content": ("low", "Under 150 words of body text"),
    "no_structured_data": ("low", "No structured data (JSON-LD)"),
    "slow": ("low", "Took over 3 seconds to respond"),
}

QUESTION_RE = re.compile(r"^(who|what|when|where|why|how|is|are|can|do|does|should|which)\b.*\??$", re.I)


# ---------- sitemap ----------

def sitemap_urls(sess, url: str, seen: set | None = None) -> list[str]:
    seen = seen or set()
    if url in seen:
        return []
    seen.add(url)
    r = sess.get(url, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, "xml")
    if soup.find("sitemapindex"):
        out = []
        for loc in soup.select("sitemap > loc"):
            out += sitemap_urls(sess, loc.text.strip(), seen)
        return out
    return [loc.text.strip() for loc in soup.select("url > loc")]


# ---------- page parsing ----------

def parse_page(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "lxml")

    def meta(attr, name):
        tag = soup.find("meta", attrs={attr: name})
        return (tag.get("content") or "").strip() if tag else None

    title = soup.title.get_text(" ", strip=True) if soup.title else None
    canonical = soup.find("link", rel=lambda v: v and "canonical" in v)
    robots = (meta("name", "robots") or "").lower()

    jsonld_types = []
    for s in soup.find_all("script", type="application/ld+json"):
        jsonld_types += re.findall(r'"@type"\s*:\s*"([^"]+)"', s.string or "")

    h1s = [h.get_text(" ", strip=True) for h in soup.find_all("h1")]
    h2s = [h.get_text(" ", strip=True) for h in soup.find_all(["h2", "h3"])]

    imgs = soup.find_all("img")
    # alt="" is the correct marker for a decorative image, so only a missing
    # alt attribute counts as a problem.
    no_alt = [i for i in imgs if i.get("alt") is None and i.get("role") != "presentation"]

    body = soup.find("main") or soup.body or soup
    for t in body.find_all(["script", "style", "noscript", "nav", "header", "footer", "form"]):
        t.decompose()
    text = re.sub(r"\s+", " ", body.get_text(" ", strip=True))
    words = len(text.split())

    host = urlparse(url).netloc
    internal = set()
    for a in soup.find_all("a", href=True):
        u = urljoin(url, a["href"])
        if urlparse(u).netloc == host:
            internal.add(u.split("#")[0])

    return {
        "title": title,
        "meta_description": meta("name", "description"),
        "h1": h1s,
        "headings": h2s[:40],
        "question_headings": sum(1 for h in h2s if QUESTION_RE.match(h)),
        "canonical": canonical.get("href") if canonical else None,
        "noindex": "noindex" in robots,
        "og_title": meta("property", "og:title"),
        "og_description": meta("property", "og:description"),
        "og_image": meta("property", "og:image"),
        "lang": (soup.html.get("lang") if soup.html else None),
        "jsonld_types": sorted(set(jsonld_types)),
        "images": len(imgs),
        "images_no_alt": len(no_alt),
        "words": words,
        "internal_links": len(internal),
        "first_text": text[:300],
    }


def page_title(title: str, suffix: str) -> str:
    """The page-specific part of a title. Google is free to cut off the
    sitewide " | Library name" suffix, so length is judged without it."""
    t = (title or "").strip()
    if suffix and t.endswith(suffix) and len(t) > len(suffix):
        t = t[: -len(suffix)].rstrip(" |–-")
    return t


def check_page(p: dict, title_suffix: str = "") -> list[str]:
    """Return a list of issue codes for one crawled page."""
    issues = []
    if p.get("status", 200) >= 400:
        return ["http_error"]
    if p.get("redirected"):
        issues.append("redirect_in_sitemap")
    if "/node/" in urlparse(p["url"]).path:
        issues.append("unaliased_url")
    if p.get("noindex"):
        issues.append("noindex")
    t = page_title(p.get("title") or "", title_suffix)
    if not t:
        issues.append("title_missing")
    elif len(t) > 60:
        issues.append("title_too_long")
    elif len(t) < 15:
        issues.append("title_too_short")
    m = p.get("meta_description") or ""
    if not m:
        issues.append("meta_missing")
    elif len(m) > 160:
        issues.append("meta_too_long")
    elif len(m) < 70:
        issues.append("meta_too_short")
    if not p.get("h1"):
        issues.append("h1_missing")
    elif len(p["h1"]) > 1:
        issues.append("h1_multiple")
    can = p.get("canonical")
    if not can:
        issues.append("canonical_missing")
    elif C.norm_url(urljoin(p["final_url"], can)) != C.norm_url(p["final_url"]):
        issues.append("canonical_mismatch")
    if not (p.get("og_title") and p.get("og_description") and p.get("og_image")):
        issues.append("og_missing")
    if p.get("images_no_alt"):
        issues.append("img_alt_missing")
    if p.get("words", 0) < 150:
        issues.append("thin_content")
    if not p.get("jsonld_types"):
        issues.append("no_structured_data")
    if p.get("seconds", 0) > 3:
        issues.append("slow")
    return issues


def page_score(issues: list[str]) -> int:
    return max(0, 100 - sum(SEVERITY_WEIGHT[ISSUE_TEXT[i][0]] for i in issues))


def ai_ready(p: dict, sitewide_types: set | None = None) -> dict:
    """Simple AI-readiness flags. These are signals, not guarantees.
    Structured data only counts if it describes this page (Event, Article,
    FAQPage...), not the sitewide organisation schema every page carries."""
    flags = {
        "structured_data": bool(set(p.get("jsonld_types") or []) - (sitewide_types or set())),
        "meta_description": bool(p.get("meta_description")),
        "question_headings": p.get("question_headings", 0) > 0,
        "substantial_text": p.get("words", 0) >= 300,
        "clear_h1": len(p.get("h1") or []) == 1,
    }
    flags["score"] = round(100 * sum(flags.values()) / len(flags))
    return flags


# ---------- crawl ----------

def fetch(sess, url: str, timeout: int) -> dict:
    t0 = time.time()
    row = {"url": url}
    try:
        r = sess.get(url, timeout=timeout, allow_redirects=True)
        row.update(
            status=r.status_code,
            final_url=r.url,
            redirected=bool(r.history),
            redirect_hops=len(r.history),
            seconds=round(time.time() - t0, 2),
        )
        if r.status_code < 400 and "html" in r.headers.get("content-type", ""):
            row.update(parse_page(r.text, r.url))
    except Exception as e:  # noqa: BLE001
        row.update(status=599, final_url=url, error=str(e)[:200], seconds=round(time.time() - t0, 2))
    return row


def robots_check(sess, site: str, bots: list[str]) -> dict:
    out = {"url": urljoin(site, "/robots.txt"), "bots": {}}
    try:
        txt = sess.get(out["url"], timeout=20).text
        rp = urllib.robotparser.RobotFileParser()
        rp.parse(txt.splitlines())
        for b in bots:
            out["bots"][b] = rp.can_fetch(b, urljoin(site, "/visit"))
        out["sitemap_listed"] = "sitemap:" in txt.lower()
    except Exception as e:  # noqa: BLE001
        out["error"] = str(e)[:200]
    return out


def run() -> None:
    cfg = C.config()
    a = cfg.get("audit", {})
    site = cfg["site"]["url"]
    sess = C.session(a.get("user_agent"))
    try:
        urls = sitemap_urls(sess, cfg["site"]["sitemap"])
        excl = [re.compile(p) for p in a.get("exclude_patterns", [])]
        total_in_sitemap = len(urls)
        urls = [u for u in dict.fromkeys(urls) if not any(p.search(u) for p in excl)][: a.get("max_pages", 1500)]
        C.log(f"Crawling {len(urls)} of {total_in_sitemap} sitemap URLs")

        with ThreadPoolExecutor(max_workers=a.get("workers", 6)) as ex:
            pages = list(ex.map(lambda u: fetch(sess, u, a.get("timeout_seconds", 20)), urls))

        suffix = a.get("title_suffix", "")
        for p in pages:
            p["issues"] = check_page(p, suffix)
            if p.get("title"):
                p["title_core_length"] = len(page_title(p["title"], suffix))
        ok_pages = [p for p in pages if p.get("status", 0) < 400]
        type_counts = Counter(t for p in ok_pages for t in set(p.get("jsonld_types", [])))
        sitewide = {t for t, n in type_counts.items() if ok_pages and n >= 0.9 * len(ok_pages)}

        # duplicates across the site
        by_title, by_meta = defaultdict(list), defaultdict(list)
        for p in pages:
            if p.get("title") and not p.get("noindex"):
                by_title[p["title"].strip().lower()].append(p)
            if p.get("meta_description"):
                by_meta[p["meta_description"].strip().lower()].append(p)
        for group, code in ((by_title, "title_duplicate"), (by_meta, "meta_duplicate")):
            for dupes in group.values():
                if len(dupes) > 1:
                    for p in dupes:
                        p["issues"].append(code)
                        p.setdefault("duplicates", {})[code] = [d["url"] for d in dupes if d is not p][:5]

        for p in pages:
            p["score"] = page_score(p["issues"])
            p["ai"] = ai_ready(p, sitewide) if p.get("status", 0) < 400 else None

        counts = Counter(i for p in pages for i in p["issues"])
        llms = sess.get(urljoin(site, "/llms.txt"), timeout=20)
        summary = {
            "updated": C.now_iso(),
            "site": site,
            "sitemap_urls": total_in_sitemap,
            "crawled": len(pages),
            "score": round(sum(p["score"] for p in pages) / len(pages)) if pages else 0,
            "ai_score": round(sum(p["ai"]["score"] for p in pages if p["ai"]) / max(1, sum(1 for p in pages if p["ai"]))),
            "issues": [
                {"code": c, "severity": ISSUE_TEXT[c][0], "label": ISSUE_TEXT[c][1], "pages": n}
                for c, n in sorted(counts.items(), key=lambda kv: (-SEVERITY_WEIGHT[ISSUE_TEXT[kv[0]][0]], -kv[1]))
            ],
            "status_codes": dict(Counter(str(p.get("status")) for p in pages)),
            "slowest": sorted(({"url": p["url"], "seconds": p.get("seconds", 0)} for p in pages), key=lambda r: -r["seconds"])[:10],
            "robots": robots_check(sess, site, a.get("ai_bots", [])),
            "llms_txt": llms.status_code == 200 and "html" not in llms.headers.get("content-type", ""),
            "structured_data_types": dict(type_counts.most_common(25)),
            "sitewide_structured_data": sorted(sitewide),
            "page_specific_structured_data": sum(1 for p in ok_pages if p["ai"]["structured_data"]),
            "title_suffix": suffix,
        }
        C.write_json("audit/pages.json", sorted(pages, key=lambda p: p["score"]))
        C.write_json("audit/summary.json", summary)
        C.upsert_history("audit/history.json", {"date": C.today().isoformat(), "score": summary["score"],
                                                "ai_score": summary["ai_score"], "crawled": len(pages)})
        C.set_status("audit", "ok", f"Crawled {len(pages)} pages, health {summary['score']}/100")
    except Exception as e:  # noqa: BLE001
        C.set_status("audit", "error", str(e)[:400])
        raise C.JobError(str(e)) from e


if __name__ == "__main__":
    run()
