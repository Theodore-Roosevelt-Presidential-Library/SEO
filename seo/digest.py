"""Machine-readable outputs so an AI assistant (or a script) can read the
dashboard without running its JavaScript.

Writes (all under docs/, served by Pages):
  llms.txt          entry point for AI tools: what's here, where, and the house rules
  digest.md         one-page ranked briefing in Markdown (best for AI tools)
  data/digest.json  the same content as structured JSON (best for scripts)

Built only from the JSON the other jobs already wrote. No API keys needed.
"""
from __future__ import annotations

from . import common as C
from .audit import ISSUE_TEXT

BASE = "https://seo.labs.trlibrary.com"
N = 15  # rows per list in the digest

HOUSE_RULES = [
    "Suggestions are drafts for the communications team; nothing is published automatically.",
    "Never invent historical facts, dates, names, prices or hours. Use only what the page already says, or flag it for verification.",
    "Never quote or paraphrase Theodore Roosevelt. Say 'consider a verified TR quote about X' instead.",
    "Voice: friendly, plain, concrete (a knowledgeable park ranger, not a professor). Keep 'we/our/us' to a minimum.",
    "No specific years in visitor copy; write seasons as months.",
    "A Library visit takes about 3 1/2 hours. Never present a shorter visit as typical.",
    "Nonpartisan: no current political figures or debates.",
    "Page titles: the site appends ' | Theodore Roosevelt Presidential Library' automatically; suggest only the page-specific part, 60 characters or fewer.",
    "Meta descriptions: 120-155 characters with a reason to click.",
    "Website changes are made in Drupal Layout Builder by the TRPL team; bugs and features go to the developers (FiveJars).",
]

RAW_FILES = {
    "status.json": "Which data sources are on, last run time, errors",
    "gsc/summary.json": "Search Console totals, last 28 days vs prior 28",
    "gsc/daily.json": "Clicks/impressions/CTR/position per day (~16 months)",
    "gsc/queries.json": "Every search query (last 28 days) with prior-period clicks",
    "gsc/pages.json": "Every page with search traffic (last 28 days)",
    "gsc/query_pages.json": "Query x page pairs, top 10,000 by impressions",
    "opportunities.json": "Ranked opportunity lists (striking distance, low CTR, missing-in-title, declining, cannibalization)",
    "ranks/latest.json": "Tracked keywords: Search Console position, live Google rank, AI Overview presence",
    "ai/latest.json": "Full AI-assistant answers to the weekly travel/history questions, with citations",
    "ai/history.json": "Weekly AI mention and citation rates",
    "audit/summary.json": "Site audit: health score, issue counts, robots.txt AI-crawler access, structured data",
    "audit/pages.json": "Per-page audit: title, meta, H1, canonical, OG tags, word count, issues",
    "tips.json": "AI-drafted page recommendations and the AI-visibility brief",
    "tracking.json": "Keywords and AI questions the system discovered, graduated or retired, with reasons",
}


def _r(x, n=1):
    return None if x is None else round(x, n)


def build() -> dict:
    status = C.read_json("status.json", {}) or {}
    gs = C.read_json("gsc/summary.json")
    queries = C.read_json("gsc/queries.json", []) or []
    pages = C.read_json("gsc/pages.json", []) or []
    opp = C.read_json("opportunities.json", {}) or {}
    ranks = C.read_json("ranks/latest.json")
    ai = C.read_json("ai/latest.json")
    audit = C.read_json("audit/summary.json")
    apages = C.read_json("audit/pages.json", []) or []
    tips = C.read_json("tips.json")
    tracking = C.read_json("tracking.json")

    d: dict = {
        "generated": C.now_iso(),
        "site": C.config()["site"]["url"],
        "dashboard": BASE,
        "sources": {k: {"state": v.get("state"), "updated": v.get("updated"), "message": v.get("message")} for k, v in status.items()},
        "house_rules": HOUSE_RULES,
    }

    if gs:
        cur, prev = gs["current_totals"], gs["previous_totals"]
        d["search"] = {
            "period": gs["period"], "previous_period": gs["previous"],
            "totals": cur, "previous_totals": prev,
            "branded_clicks": gs.get("branded_clicks"), "nonbranded_clicks": gs.get("nonbranded_clicks"),
            "unattributed_clicks": gs.get("unattributed_clicks"),
            "top_queries": [{"query": q["query"], "clicks": q["clicks"], "prev_clicks": q.get("prev_clicks"),
                             "impressions": q["impressions"], "ctr": q["ctr"], "position": q["position"],
                             "branded": q.get("branded")}
                            for q in sorted(queries, key=lambda r: -r["clicks"])[:25]],
            "top_nonbranded_queries": [{"query": q["query"], "clicks": q["clicks"], "impressions": q["impressions"], "position": q["position"]}
                                       for q in sorted((q for q in queries if not q.get("branded")), key=lambda r: -r["impressions"])[:25]],
            "top_pages": [{"page": p["page"], "clicks": p["clicks"], "prev_clicks": p.get("prev_clicks"),
                           "impressions": p["impressions"], "ctr": p["ctr"], "position": p["position"]}
                          for p in sorted(pages, key=lambda r: -r["clicks"])[:25]],
        }

    if opp:
        d["opportunities"] = {k: opp.get(k, [])[:N] for k in
                              ("striking_distance", "low_ctr", "missing_in_title", "declining", "cannibalization")}
        d["opportunities"]["note"] = opp.get("note")

    if ranks:
        d["rankings"] = {"updated": ranks.get("updated"), "source": ranks.get("source"), "keywords": [
            {"keyword": k["keyword"], "group": k["group"], "volume": k.get("volume"),
             "gsc_position": (k.get("gsc") or {}).get("position"),
             "google_rank": (k.get("serp") or {}).get("rank"),
             "ai_overview": (k.get("serp") or {}).get("ai_overview"),
             "ai_overview_cites_us": (k.get("serp") or {}).get("ai_overview_cites_us"),
             "ranking_above_us": [t["domain"] for t in (k.get("serp") or {}).get("top", [])
                                  if not (k.get("serp") or {}).get("rank") or t["rank"] < k["serp"]["rank"]][:3]}
            for k in ranks.get("keywords", [])]}

    if ai:
        prompts = {p["id"]: p for p in ai.get("prompts", [])}
        res = [r for r in ai.get("results", []) if not r.get("error")]
        d["ai_visibility"] = {
            "updated": ai.get("updated"),
            "engines": {v["label"]: {"model": v["model"], "mention_rate": v.get("mention_rate"), "cite_rate": v.get("cite_rate")}
                        for v in ai.get("providers", {}).values()},
            "by_question": [{
                "id": pid, "group": p.get("group"), "question": p["text"],
                "answers": [{"engine": ai["providers"][r["provider"]]["label"], "mentioned": r["mentioned"],
                             "cited_trlibrary": r["cited_us"], "position_among_attractions": r.get("position"),
                             "also_mentioned": r.get("peers", []), "how_described": r.get("excerpt") or None,
                             "sources": r.get("cited_domains", [])[:6]}
                            for r in res if r["prompt_id"] == pid]}
                for pid, p in prompts.items()],
            "top_cited_domains": ai.get("top_cited_domains", [])[:15],
            "errors": list(dict.fromkeys(f"{r['provider']}: {' '.join(r['error'].split())[:140]}" for r in ai.get("results", []) if r.get("error")))[:3],
        }

    if audit:
        by_issue: dict = {}
        for p in apages:
            for i in p.get("issues", []):
                by_issue.setdefault(i, []).append(p["url"])
        d["audit"] = {
            "updated": audit.get("updated"), "crawled": audit.get("crawled"), "sitemap_urls": audit.get("sitemap_urls"),
            "health_score": audit.get("score"), "ai_readiness_score": audit.get("ai_score"),
            "llms_txt_on_trlibrary": audit.get("llms_txt"),
            "ai_crawlers_allowed": (audit.get("robots") or {}).get("bots"),
            "sitewide_structured_data": audit.get("sitewide_structured_data"),
            "pages_with_page_specific_structured_data": audit.get("page_specific_structured_data"),
            "issues": [{"code": i["code"], "severity": i["severity"], "label": i["label"], "pages": i["pages"],
                        "examples": by_issue.get(i["code"], [])[:10]} for i in audit.get("issues", [])],
            "weakest_pages": [{"url": p["url"], "score": p["score"], "issues": p["issues"], "title": p.get("title")}
                              for p in apages[:20]],
        }

    if tips:
        d["recommendations"] = {
            "updated": tips.get("updated"), "written_by": f"{tips.get('provider_label', 'AI')} ({tips.get('model')})",
            "ai_brief": tips.get("ai_brief"),
            "pages": [{k: p.get(k) for k in ("page", "summary", "title", "meta_description", "content_additions",
                                              "ai_readiness", "technical", "needs_verification", "checks")}
                      for p in tips.get("pages", [])],
        }

    if tracking:
        d["tracking"] = {
            "discovered_keywords": [{"keyword": k["keyword"], "group": k.get("group"), "added": k["added"], "reason": k.get("reason")}
                                    for k in tracking.get("keywords", []) if k.get("status") == "active"],
            "discovered_questions": [{"question": p["text"], "added": p["added"], "reason": p.get("reason")}
                                     for p in tracking.get("prompts", []) if p.get("status") == "active"],
            "recent_changes": tracking.get("log", [])[:15],
            "how_to_change": "Rules and caps: config/tracking.yml. Keep an item permanently by copying it into config/keywords.yml or config/ai_prompts.yml; block it via tracking.yml exclude.",
        }

    d["raw_files"] = {f"{BASE}/data/{k}": v for k, v in RAW_FILES.items()}
    return d


# ---------- Markdown ----------

def _table(rows: list[dict], cols: list[tuple[str, str]]) -> str:
    if not rows:
        return "_None._\n"
    out = ["| " + " | ".join(h for _, h in cols) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        cells = []
        for k, _ in cols:
            v = r.get(k)
            if isinstance(v, float):
                v = f"{v:.1%}" if k in ("ctr", "expected_ctr", "change", "mention_rate", "cite_rate") else f"{v:g}"
            if isinstance(v, list):
                v = ", ".join(map(str, v))
            cells.append(str("–" if v is None else v).replace("|", "/").replace("\n", " "))
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out) + "\n"


def _short(u: str) -> str:
    return (u or "").replace("https://www.trlibrary.com", "") or "/"


def to_markdown(d: dict) -> str:
    L = [f"# trlibrary.com search & AI visibility digest",
         f"Generated {d['generated']} from {d['dashboard']}. Full data: see 'Raw data' at the end.\n",
         "## How to use this",
         "Read top to bottom: the biggest, cheapest wins come first in each section. When you suggest copy, follow these house rules:\n"]
    L += [f"- {r}" for r in d["house_rules"]]
    L.append("\n## Data freshness")
    L.append(_table([{"source": k, **v} for k, v in d["sources"].items()],
                    [("source", "Source"), ("state", "State"), ("updated", "Updated"), ("message", "Details")]))

    s = d.get("search")
    if s:
        t, p = s["totals"], s["previous_totals"]
        L += ["## Google Search (Search Console)",
              f"{s['period']['start']} to {s['period']['end']} vs the prior 28 days: "
              f"**{t['clicks']:,} clicks** (prior {p['clicks']:,}), {t['impressions']:,} impressions (prior {p['impressions']:,}), "
              f"CTR {t['ctr']:.1%} (prior {p['ctr']:.1%}), average position {t['position']} (prior {p['position']}). "
              f"Branded clicks {s.get('branded_clicks')}, non-branded {s.get('nonbranded_clicks')}, search term hidden by Google {s.get('unattributed_clicks', 'n/a')}.\n",
              "### Top non-branded searches (people who didn't search our name)",
              _table(s["top_nonbranded_queries"], [("query", "Search"), ("clicks", "Clicks"), ("impressions", "Impr."), ("position", "Pos.")]),
              "### Top pages",
              _table([{**x, "page": _short(x["page"])} for x in s["top_pages"]],
                     [("page", "Page"), ("clicks", "Clicks"), ("prev_clicks", "Prior"), ("impressions", "Impr."), ("position", "Pos.")])]

    o = d.get("opportunities")
    if o:
        L += ["## Opportunities (ranked)", f"_{o.get('note')}_\n",
              "### Striking distance: ranking 4-20 with demand; strengthen the page for the exact search",
              _table([{**x, "page": _short(x["page"])} for x in o["striking_distance"]],
                     [("query", "Search"), ("page", "Page"), ("position", "Pos."), ("impressions", "Impr."), ("est_extra_clicks", "Upside")]),
              "### Ranking well but skipped: rewrite title/meta description",
              _table([{**x, "page": _short(x["page"])} for x in o["low_ctr"]],
                     [("page", "Page"), ("position", "Pos."), ("ctr", "CTR"), ("expected_ctr", "Typical"), ("est_extra_clicks", "Upside")]),
              "### Search words missing from the ranking page's title",
              _table([{**x, "page": _short(x["page"])} for x in o["missing_in_title"]],
                     [("query", "Search"), ("page", "Page"), ("title", "Current title"), ("missing_words", "Missing"), ("impressions", "Impr.")]),
              "### Losing clicks vs prior 28 days (check seasonality first)",
              _table([{**x, "item": _short(x["item"])} for x in o["declining"]],
                     [("kind", "Type"), ("item", "Search/page"), ("clicks", "Clicks"), ("prev_clicks", "Prior"), ("change", "Change")]),
              "### Our pages competing for the same search",
              _table([{"query": x["query"], "impressions": x["impressions"],
                       "pages": [f"{_short(pp['page'])} (pos {pp['position']})" for pp in x["pages"]]} for x in o["cannibalization"]],
                     [("query", "Search"), ("impressions", "Impr."), ("pages", "Pages")])]

    r = d.get("rankings")
    if r:
        L += [f"## Tracked keywords ({r['source']})",
              _table(r["keywords"], [("keyword", "Keyword"), ("group", "Group"), ("volume", "Volume"), ("gsc_position", "GSC pos."),
                                     ("google_rank", "Google rank"), ("ai_overview", "AI Overview"),
                                     ("ai_overview_cites_us", "Cites us"), ("ranking_above_us", "Above us")])]

    a = d.get("ai_visibility")
    if a:
        L += ["## AI assistant visibility",
              _table([{"engine": k, **v} for k, v in a["engines"].items()],
                     [("engine", "Engine"), ("model", "Model"), ("mention_rate", "Mentions us"), ("cite_rate", "Cites trlibrary.com")]),
              "### Question by question"]
        if a.get("errors"):
            L.append("Some answers failed this week: " + "; ".join(a["errors"]) + "\n")
        for q in a["by_question"]:
            if not q["answers"]:
                continue
            L.append(f"**{q['question']}** ({q['group']})")
            for ans in q["answers"]:
                state = "mentioned" + (f", #{ans['position_among_attractions']} among attractions" if ans["position_among_attractions"] else "") \
                    + (", cites trlibrary.com" if ans["cited_trlibrary"] else "") if ans["mentioned"] else "NOT mentioned"
                extra = f" Also named: {', '.join(ans['also_mentioned'])}." if ans["also_mentioned"] else ""
                desc = f" Described as: \"{ans['how_described']}\"" if ans["how_described"] else ""
                L.append(f"- {ans['engine']}: {state}.{extra}{desc} Sources: {', '.join(ans['sources']) or 'none'}")
            L.append("")
        L += ["### Sites AI assistants cite most", ", ".join(f"{dm} ({n})" for dm, n in a["top_cited_domains"]) + "\n"]

    au = d.get("audit")
    if au:
        bots = au.get("ai_crawlers_allowed") or {}
        blocked = [b for b, ok in bots.items() if not ok]
        L += ["## Site audit",
              f"Crawled {au['crawled']} of {au['sitemap_urls']} sitemap URLs. Health {au['health_score']}/100, AI readiness {au['ai_readiness_score']}/100. "
              f"llms.txt on trlibrary.com: {'yes' if au['llms_txt_on_trlibrary'] else 'no'}. "
              f"AI crawlers blocked in robots.txt: {', '.join(blocked) or 'none'}. "
              f"{au.get('pages_with_page_specific_structured_data')} pages have page-specific structured data "
              f"(sitewide on every page: {', '.join(au.get('sitewide_structured_data') or [])}).\n",
              _table([{**i, "examples": [_short(u) for u in i["examples"][:5]]} for i in au["issues"]],
                     [("severity", "Severity"), ("label", "Issue"), ("pages", "Pages"), ("examples", "Examples")])]

    rec = d.get("recommendations")
    if rec:
        L += [f"## Drafted recommendations ({rec['written_by']}, {rec['updated']})"]
        b = rec.get("ai_brief") or {}
        if b:
            L.append(f"**AI visibility:** {b.get('headline', '')}")
            for x in b.get("actions", []):
                L.append(f"- {x.get('action')} ({x.get('effort')} effort; {x.get('where')}): {x.get('why')}")
            L.append("")
        for p in rec["pages"]:
            L.append(f"**{_short(p['page'])}**: {p.get('summary') or ''}")
            if (p.get("title") or {}).get("suggested"):
                L.append(f"- Title: {p['title']['suggested']}")
            if (p.get("meta_description") or {}).get("suggested"):
                L.append(f"- Meta: {p['meta_description']['suggested']}")
            if p.get("needs_verification"):
                L.append(f"- Verify: {'; '.join(p['needs_verification'])}")
            L.append("")

    tr = d.get("tracking")
    if tr and tr["recent_changes"]:
        L += ["## Tracking changes made automatically", tr["how_to_change"] + "\n",
              _table(tr["recent_changes"], [("date", "Date"), ("action", "Change"), ("kind", "Type"), ("item", "Item"), ("reason", "Why")])]

    L += ["## Raw data", "All JSON, refreshed daily (Search Console) and weekly (everything else):\n"]
    L += [f"- {u}: {desc}" for u, desc in d["raw_files"].items()]
    return "\n".join(L) + "\n"


def llms_txt(d: dict) -> str:
    s, au, a = d.get("search"), d.get("audit"), d.get("ai_visibility")
    snap = []
    if s:
        snap.append(f"- Google: {s['totals']['clicks']:,} clicks, avg position {s['totals']['position']} (28 days to {s['period']['end']})")
    if au:
        snap.append(f"- Site audit: health {au['health_score']}/100, AI readiness {au['ai_readiness_score']}/100")
    if a:
        rates = [f"{k} {v['mention_rate']:.0%}" for k, v in a["engines"].items() if v.get("mention_rate") is not None]
        snap.append("- AI assistants mentioning the Library: " + (", ".join(rates) if rates else "no answers in the latest run (see digest for errors)"))
    return f"""# TRPL Search & AI Visibility

> How www.trlibrary.com (Theodore Roosevelt Presidential Library, Medora, North Dakota) performs in Google Search and in AI assistants, with ranked opportunities and drafted fixes. Refreshed daily (Search Console) and weekly (site audit, rankings, AI answers, recommendations). Last built {d['generated']}.

The dashboard at {BASE}/ is rendered with JavaScript. AI tools should read the digest below instead.

## Start here
- [Digest (Markdown)]({BASE}/digest.md): one-page ranked briefing: search totals, top opportunities, tracked keywords, AI-assistant answers, audit issues, drafted recommendations, and house rules for suggesting copy
- [Digest (JSON)]({BASE}/data/digest.json): the same content as structured data

## Snapshot
{chr(10).join(snap) or '- Data sources are still being connected.'}

## Raw data
{chr(10).join(f'- [{k}]({BASE}/data/{k}): {v}' for k, v in RAW_FILES.items())}

## House rules for suggesting changes
{chr(10).join('- ' + r for r in HOUSE_RULES)}

## Optional
- [Source code and configuration](https://github.com/Theodore-Roosevelt-Presidential-Library/SEO): tracked keywords in config/keywords.yml, AI questions in config/ai_prompts.yml
"""


def run() -> None:
    d = build()
    C.write_json("digest.json", d)
    docs = C.DATA_DIR.parent
    (docs / "digest.md").write_text(to_markdown(d), encoding="utf-8")
    (docs / "llms.txt").write_text(llms_txt(d), encoding="utf-8")
    C.set_status("digest", "ok", "llms.txt, digest.md and digest.json rebuilt")


if __name__ == "__main__":
    run()
