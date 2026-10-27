"""Visitor Experience: how easy the /visit pages are to use.

For every sitemap URL under ux.section (default /visit):
  - Google PageSpeed Insights, mobile: performance, accessibility, best practices,
    lab Core Web Vitals, real-user field data when Chrome has enough visits, and
    the specific accessibility checks that fail.
  - Readability: reading ease, grade level, long paragraphs, and how far down the
    first ticket link sits.
  - GA4 behaviour (when GA4_PROPERTY_ID is set): views, engagement rate,
    average engagement time, bounce rate.
  - Microsoft Clarity (when CLARITY_API_TOKEN is set): rage clicks, dead clicks,
    scroll depth, quick back-outs (last 3 days; that's all Clarity's API gives).
For the key pages, an AI (any configured key) reads the page as a first-time
visitor and checks whether each visitor task is answered near the top, buried,
only linked, or missing; it also extracts stated facts (hours, prices, visit
length) so pages that disagree with each other get flagged.

Optional keys: PAGESPEED_API_KEY (raises Google's free quota so all pages are
checked), GA4_PROPERTY_ID (variable), CLARITY_API_TOKEN, any AI key.

Writes ux/latest.json and ux/history.json.
"""
from __future__ import annotations

import json
import re
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from . import common as C, verify as V

PSI = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
class QuotaExhausted(RuntimeError):
    pass


TASK_SCORE = {"top": 1.0, "linked": 0.75, "buried": 0.5, "missing": 0.0}


# ---------- page text & readability ----------

def _syllables(word: str) -> int:
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups) - (1 if w.endswith("e") and len(groups) > 1 else 0)
    return max(1, n)


def readability(html: str, url: str, ticket_re: re.Pattern) -> dict:
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main") or soup.body or soup
    for t in main.find_all(["script", "style", "noscript", "nav", "header", "footer", "form"]):
        t.decompose()
    paras = [p.get_text(" ", strip=True) for p in main.find_all(["p", "li"]) if p.get_text(strip=True)]
    text = " ".join(paras) or main.get_text(" ", strip=True)
    words = re.findall(r"[A-Za-z][A-Za-z'\-]*", text)
    # each paragraph or list item ends a sentence even without a full stop
    # (otherwise bulleted lists read as one giant sentence)
    sentences = max(1, sum(max(1, len(re.findall(r"[.!?]+(\s|$)", p))) for p in paras) if paras
                    else len(re.findall(r"[.!?]+(\s|$)", text)))
    syl = sum(_syllables(w) for w in words)
    nw = max(1, len(words))
    flesch = 206.835 - 1.015 * (nw / sentences) - 84.6 * (syl / nw)
    grade = 0.39 * (nw / sentences) + 11.8 * (syl / nw) - 15.59

    # how many words a visitor reads before the first ticket link
    words_before, seen = None, 0
    for el in main.descendants:
        if getattr(el, "name", None) == "a" and el.get("href") and ticket_re.search(el["href"]):
            words_before = seen
            break
        if isinstance(el, str):
            seen += len(el.split())
    return {
        "words": len(words),
        "reading_ease": round(flesch, 1) if words else None,
        "grade_level": round(grade, 1) if words else None,
        "long_paragraphs": sum(1 for p in paras if len(p.split()) > 80),
        "words_before_ticket_link": words_before,
        # full main text incl. divs, tables, tabs and accordions (see verify.main_text)
        "text": V.main_text(html, 24000),
        "links": [a.get_text(" ", strip=True)[:60] + " -> " + a["href"][:120]
                  for a in main.find_all("a", href=True) if a.get_text(strip=True)][:60],
    }


def reading_label(grade: float | None) -> str:
    """By US school grade level. Visitor copy should aim for grade 8 or lower."""
    if grade is None:
        return "–"
    return "easy" if grade <= 8 else "plain" if grade <= 10 else "fairly hard" if grade <= 12 else "hard"


# ---------- PageSpeed Insights ----------

def pagespeed(sess, url: str, key: str | None) -> dict:
    params = [("url", url), ("strategy", "mobile"), ("category", "performance"),
              ("category", "accessibility"), ("category", "best-practices")]
    if key:
        params.append(("key", key))
    for attempt in range(3):
        r = sess.get(PSI, params=params, timeout=120)
        if r.status_code == 429 and "per day" in r.text:
            raise QuotaExhausted("PageSpeed daily quota used up" + ("" if key else "; add a free PAGESPEED_API_KEY"))
        if r.status_code == 429 and attempt < 2:
            time.sleep(30 * (attempt + 1))
            continue
        break
    if r.status_code != 200:
        raise RuntimeError(f"PageSpeed {r.status_code}: {r.text[:160]}")
    d = r.json()
    lh = d.get("lighthouseResult", {})
    cats, audits = lh.get("categories", {}), lh.get("audits", {})

    def score(c):
        s = (cats.get(c) or {}).get("score")
        return None if s is None else round(s * 100)

    a11y_fails = []
    for ref in (cats.get("accessibility") or {}).get("auditRefs", []):
        a = audits.get(ref["id"], {})
        if a.get("score") == 0 and ref.get("weight", 0) > 0:
            a11y_fails.append(a.get("title", ref["id"]))
    field = (d.get("loadingExperience") or {})
    fm = field.get("metrics") or {}

    def fv(k):
        return (fm.get(k) or {}).get("percentile")

    return {
        "performance": score("performance"), "accessibility": score("accessibility"),
        "best_practices": score("best-practices"),
        "lcp_s": round((audits.get("largest-contentful-paint") or {}).get("numericValue", 0) / 1000, 1) or None,
        "cls": round((audits.get("cumulative-layout-shift") or {}).get("numericValue", 0), 3),
        "tbt_ms": round((audits.get("total-blocking-time") or {}).get("numericValue", 0)),
        "a11y_failures": a11y_fails[:8],
        "field": {"overall": field.get("overall_category"), "lcp_ms": fv("LARGEST_CONTENTFUL_PAINT_MS"),
                  "inp_ms": fv("INTERACTION_TO_NEXT_PAINT"),
                  "cls": (fv("CUMULATIVE_LAYOUT_SHIFT_SCORE") or 0) / 100 if fv("CUMULATIVE_LAYOUT_SHIFT_SCORE") is not None else None}
        if fm and field.get("id", "").rstrip("/") == url.rstrip("/") else None,
        "origin_field": (d.get("originLoadingExperience") or {}).get("overall_category"),
    }


# ---------- AI task check ----------

TASK_PROMPT = """You are testing a page of trlibrary.com (Theodore Roosevelt Presidential Library, Medora, North Dakota) as a first-time visitor planning a trip, reading on a phone.

Page: {url}
Page text, complete, in reading order (headings marked with #; text inside tabs and accordions included):
{text}

Links on the page (text -> URL):
{links}

For each visitor task below, judge THIS page only:
- "top": answered clearly in the first screen or two of text
- "buried": answered, but far down or hard to spot
- "linked": not answered here, but an obvious link leads to the answer
- "missing": neither answered nor clearly linked
- "not_relevant": a visitor on this page wouldn't expect it

Tasks:
{tasks}

Also copy the exact facts the page states (verbatim, or null if not stated): opening hours, ticket prices, recommended visit length, street address, parking.

Return JSON only:
{{"tasks": {{"<task id>": {{"status": "top|buried|linked|missing|not_relevant", "note": "under 20 words: where it is or what's missing"}}}},
  "facts": {{"hours": null, "prices": null, "visit_length": null, "address": null, "parking": null}},
  "biggest_fix": "one sentence: the single change that would help a visitor most on this page"}}"""

CONFLICT_PROMPT = """These facts were copied word for word from different trlibrary.com visitor pages. Find real contradictions (different hours, prices, visit lengths, addresses) and ignore differences in wording, completeness or seasonal detail that don't conflict.

{facts}

Return JSON only: {{"conflicts": [{{"fact": "hours|prices|visit_length|address|parking", "pages": ["/path", "/path"], "detail": "what disagrees, under 30 words"}}]}}"""


def task_check(writer, url: str, rd: dict, tasks: dict, facts: dict | None = None) -> dict:
    user = TASK_PROMPT.format(url=url, text=rd["text"], links="\n".join(rd["links"]) or "(none)",
                              tasks="\n".join(f"- {k}: {v}" for k, v in tasks.items()))
    res, prov, model = writer.call(user)
    res = res if isinstance(res, dict) else {}
    if facts:  # drop claims the live page contradicts
        res = V.check_task_result(res, facts)
    t = res.get("tasks") or {}
    clean = {k: {"status": (t.get(k) or {}).get("status", "missing"), "note": (t.get(k) or {}).get("note", "")} for k in tasks}
    relevant = [v["status"] for v in clean.values() if v["status"] in TASK_SCORE]
    return {"tasks": clean, "facts": res.get("facts") or {}, "biggest_fix": res.get("biggest_fix"),
            "dropped_claims": res.get("dropped_claims") or [],
            "findability": round(100 * sum(TASK_SCORE[s] for s in relevant) / len(relevant)) if relevant else None,
            "checked_by": f"{prov} ({model})"}


# ---------- GA4 & Clarity ----------

def ga4_pages(section: str, host: str) -> dict:
    ga = C.GA4.from_env()
    if not ga:
        return {}
    rows = ga.report(["pagePath"], ["screenPageViews", "engagementRate", "userEngagementDuration", "activeUsers", "bounceRate"],
                     dim_filter=C.ga4_and(C.ga4_filter("hostName", host), C.ga4_filter("pagePath", section, "BEGINS_WITH")))
    out = {}
    for r in rows:
        path = r["pagePath"].split("?")[0].rstrip("/") or "/"
        o = out.setdefault(path, {"views": 0, "_eng": 0.0, "_users": 0, "_er": [], "_br": []})
        o["views"] += r.get("screenPageViews") or 0
        o["_eng"] += r.get("userEngagementDuration") or 0
        o["_users"] += r.get("activeUsers") or 0
        o["_er"].append(((r.get("engagementRate") or 0), r.get("screenPageViews") or 0))
        o["_br"].append(((r.get("bounceRate") or 0), r.get("screenPageViews") or 0))
    for o in out.values():
        w = sum(v for _, v in o["_er"]) or 1
        o["engagement_rate"] = round(sum(x * v for x, v in o.pop("_er")) / w, 3)
        o["bounce_rate"] = round(sum(x * v for x, v in o.pop("_br")) / w, 3)
        o["avg_engagement_s"] = round(o.pop("_eng") / o["_users"]) if o["_users"] else None
        o.pop("_users")
        o["views"] = int(o["views"])
    return out


def clarity_pages(section: str) -> tuple[dict, str | None]:
    """Website Clarity project (CLARITY_API_TOKEN), per /visit page."""
    tok = C.env("CLARITY_API_TOKEN")
    if not tok:
        return {}, None
    try:
        per_url, _ = C.clarity_insights(tok)
    except Exception as e:  # noqa: BLE001
        return {}, str(e)[:200]
    return {path: v for (_, path), v in per_url.items() if path.startswith(section)}, None


# ---------- main ----------

def run() -> None:
    cfg = C.config()
    u = cfg.get("ux", {})
    site, section = cfg["site"]["url"], u.get("section", "/visit")
    host = urlparse(site).netloc
    skip = [re.compile(p) for p in u.get("skip_patterns", [])]
    ticket_re = re.compile(u.get("ticket_link_pattern", r"/tickets\b"))
    psi_key = C.env("PAGESPEED_API_KEY")
    key_pages = [p.rstrip("/") or "/" for p in u.get("key_pages", [])]
    tasks = u.get("tasks", {})

    from .audit import sitemap_urls
    sess = C.session(cfg.get("audit", {}).get("user_agent"))
    try:
        urls = [x for x in dict.fromkeys(sitemap_urls(sess, cfg["site"]["sitemap"]))
                if urlparse(x).path.startswith(section) and not any(s.search(urlparse(x).path) for s in skip)]
    except Exception as e:  # noqa: BLE001
        C.set_status("ux", "error", f"sitemap: {e}"[:300])
        raise C.JobError(str(e)) from e
    paths = {x: urlparse(x).path.rstrip("/") or "/" for x in urls}
    psi_urls = urls if psi_key else [x for x in urls if paths[x] in key_pages]

    pages: dict = {}
    for x in urls:
        try:
            r = sess.get(x, timeout=30)
            pages[x] = {"path": paths[x], "url": x, "status": r.status_code,
                        **({"readability": readability(r.text, x, ticket_re),
                            "_facts": V.page_facts(r.text, ticket_re)} if r.status_code < 400 else {})}
        except Exception as e:  # noqa: BLE001
            pages[x] = {"path": paths[x], "url": x, "status": 599, "error": str(e)[:120]}

    errors = []

    stop = {"quota": None}

    def do_psi(x):
        if stop["quota"]:
            return x, None, None
        try:
            return x, pagespeed(C.session(), x, psi_key), None
        except QuotaExhausted as e:
            stop["quota"] = str(e)
            return x, None, None
        except Exception as e:  # noqa: BLE001
            return x, None, str(e)[:160]
    with ThreadPoolExecutor(max_workers=u.get("pagespeed_workers", 3)) as ex:
        for x, res, err in ex.map(do_psi, psi_urls):
            if res:
                pages[x]["pagespeed"] = res
            elif err:
                errors.append(f"PageSpeed {paths[x]}: {err}")
    if stop["quota"]:
        errors.insert(0, stop["quota"])

    # AI task checks on key pages
    from . import tips
    providers = tips.available_providers(cfg)
    checked_by = None
    if providers and tasks:
        writer = tips.Writer(providers)
        for x in urls:
            if paths[x] in key_pages and pages[x].get("readability"):
                try:
                    pages[x]["task_check"] = task_check(writer, x, pages[x]["readability"], tasks, pages[x].get("_facts"))
                    checked_by = pages[x]["task_check"]["checked_by"]
                except Exception as e:  # noqa: BLE001
                    errors.append(f"Task check {paths[x]}: {e}"[:200])
        facts = {pages[x]["path"]: pages[x]["task_check"]["facts"] for x in urls if pages[x].get("task_check")}
        conflicts = []
        if len(facts) > 1:
            try:
                res, _, _ = writer.call(CONFLICT_PROMPT.format(facts=json.dumps(facts, ensure_ascii=False, indent=1)))
                conflicts = (res or {}).get("conflicts") or []
            except Exception as e:  # noqa: BLE001
                errors.append(f"Fact consistency: {e}"[:200])
    else:
        conflicts = []

    # GA4 + Clarity
    ga = {}
    try:
        ga = ga4_pages(section, host)
    except Exception as e:  # noqa: BLE001
        errors.append(str(e)[:200])
    cl, cl_err = clarity_pages(section)
    if cl_err:
        errors.append(cl_err)
    for p in pages.values():
        p.pop("_facts", None)
        if p["path"] in ga:
            p["ga4"] = ga[p["path"]]
        if p["path"] in cl:
            p["clarity"] = cl[p["path"]]
        if p.get("readability"):
            p["readability"].pop("text", None)
            p["readability"].pop("links", None)
            p["readability"]["label"] = reading_label(p["readability"]["grade_level"])

    rows = list(pages.values())

    def avg(vals):
        vals = [v for v in vals if v is not None]
        return round(sum(vals) / len(vals)) if vals else None
    task_status: dict = {}
    for p in rows:
        for k, v in ((p.get("task_check") or {}).get("tasks") or {}).items():
            task_status.setdefault(k, {}).setdefault(v["status"], 0)
            task_status[k][v["status"]] += 1
    summary = {
        "pages": len(rows),
        "pagespeed_checked": sum(1 for p in rows if p.get("pagespeed")),
        "performance": avg((p.get("pagespeed") or {}).get("performance") for p in rows),
        "accessibility": avg((p.get("pagespeed") or {}).get("accessibility") for p in rows),
        "findability": avg((p.get("task_check") or {}).get("findability") for p in rows),
        "reading_ease": avg((p.get("readability") or {}).get("reading_ease") for p in rows),
        "grade_level": (lambda v: round(sum(v) / len(v), 1) if v else None)(
            [p["readability"]["grade_level"] for p in rows if (p.get("readability") or {}).get("grade_level") is not None]),
        "hard_to_read": sum(1 for p in rows if (p.get("readability") or {}).get("label") in ("fairly hard", "hard")),
        "conflicts": len(conflicts),
        "claims_dropped": sum(len((p.get("task_check") or {}).get("dropped_claims") or []) for p in rows),
        "origin_field": next(((p.get("pagespeed") or {}).get("origin_field") for p in rows if (p.get("pagespeed") or {}).get("origin_field")), None),
        "task_status": task_status,
    }
    out = {"updated": C.now_iso(), "section": section, "tasks": tasks, "checked_by": checked_by,
           "sources": {"pagespeed": "all pages" if psi_key else "key pages only (add PAGESPEED_API_KEY for all)",
                       "ga4": bool(ga), "clarity": bool(cl), "ai_task_check": bool(checked_by)},
           "summary": summary, "conflicts": conflicts, "pages": sorted(rows, key=lambda p: p["path"]),
           "errors": errors[:20]}
    C.write_json("ux/latest.json", out)
    C.upsert_history("ux/history.json", {"date": C.today().isoformat(), **{k: summary[k] for k in
                     ("performance", "accessibility", "findability", "grade_level", "conflicts")}})
    msg = (f"{len(rows)} pages; PageSpeed on {summary['pagespeed_checked']}; "
           f"{'AI task check by ' + checked_by if checked_by else 'no AI task check'}; "
           f"GA4 {'on' if ga else 'off'}; Clarity {'on' if cl else 'off'}")
    failed = not summary["pagespeed_checked"] and not checked_by
    C.set_status("ux", "error" if failed else "ok", msg + (f"; {len(errors)} errors, e.g. {errors[0]}" if errors else ""))


if __name__ == "__main__":
    run()
