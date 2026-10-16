"""Claude-written recommendations.

1. Page tips: for the pages with the most upside, Claude reads the live page,
   its Search Console queries and its audit issues, and suggests a new title,
   meta description, content additions and AI-readiness fixes in TRPL voice.
2. AI visibility brief: Claude reads the latest AI-answer results and lists
   the highest-value actions to get the Library recommended more often.

Needs ANTHROPIC_API_KEY. Everything it writes is a DRAFT for human review;
anything touching history is flagged for verification and nothing is
published automatically.

Writes tips.json
"""
from __future__ import annotations

import json
import re

from bs4 import BeautifulSoup

from . import common as C
from .audit import ISSUE_TEXT

SYSTEM = """You are an SEO and AI-search adviser for the Theodore Roosevelt Presidential Library (trlibrary.com) in Medora, North Dakota. You suggest improvements to the Library's own web pages. A communications team member reviews everything before it is used.

House rules for any copy you draft:
- Voice: friendly, plain, vivid; a knowledgeable park ranger, never a professor. No museum-speak, jargon or vague superlatives ("world-class", "transformative journey"). Be concrete.
- Keep "we/our/us" to a minimum.
- Never write a specific year into visitor copy (it goes stale); write seasons as months.
- A visit to the Library takes about 3 1/2 hours. Never suggest a shorter visit is typical or enough.
- Nonpartisan. No current political figures or debates.
- Never invent facts. Do not state historical dates, names, events, prices, hours or figures unless they already appear in the page text you were given.
- Never quote or paraphrase Theodore Roosevelt. If a quote would help, say "consider adding a verified TR quote about X".
- Anything you suggest that touches history or a factual claim goes in needs_verification.
- Titles: the site adds " | Theodore Roosevelt Presidential Library" automatically, so suggest only the page-specific part: 60 characters or fewer, most important words first, no suffix.
- Meta descriptions: 120-155 characters, includes a reason to click.

Reply with JSON only, no prose before or after."""

PAGE_SCHEMA = """{
 "summary": "one or two sentences: the single biggest opportunity on this page",
 "title": {"suggested": "...", "why": "..."},
 "meta_description": {"suggested": "...", "why": "..."},
 "content_additions": [{"for_query": "search query or AI question this serves", "suggestion": "what to add and where", "draft": "optional short draft copy"}],
 "ai_readiness": [{"suggestion": "...", "why": "..."}],
 "technical": [{"suggestion": "...", "why": "..."}],
 "needs_verification": ["any claim in your drafts that must be checked before publishing"]
}"""

AI_SCHEMA = """{
 "headline": "one sentence on where the Library stands in AI answers",
 "how_described": "how the engines describe the Library when they do mention it; note anything inaccurate",
 "gaps": [{"theme": "type of question where the Library is missing", "who_shows_up_instead": "...", "prompt_ids": ["..."]}],
 "actions": [{"action": "...", "why": "...", "effort": "low|medium|high", "where": "trlibrary.com page, listing, or outside site"}],
 "inaccuracies": [{"engine": "...", "claim": "...", "correction_source": "which official page should state the right fact"}]
}"""


def call_claude(key: str, model: str, user: str, max_tokens: int = 2500) -> dict:
    sess = C.session()
    r = sess.post("https://api.anthropic.com/v1/messages", timeout=240,
                  headers={"x-api-key": key, "anthropic-version": "2023-06-01"},
                  json={"model": model, "max_tokens": max_tokens, "system": SYSTEM,
                        "messages": [{"role": "user", "content": user}]})
    if r.status_code != 200:
        raise RuntimeError(f"Claude {r.status_code}: {r.text[:200]}")
    text = "".join(b.get("text", "") for b in r.json().get("content", []) if b.get("type") == "text")
    return parse_json(text)


def parse_json(text: str) -> dict:
    text = re.sub(r"^```(json)?|```$", "", text.strip(), flags=re.M).strip()
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < 0:
        raise ValueError("No JSON in model reply")
    return json.loads(text[start:end + 1])


def page_text(url: str) -> dict:
    r = C.session().get(url, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "lxml")
    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    md = soup.find("meta", attrs={"name": "description"})
    body = soup.find("main") or soup.body or soup
    for t in body.find_all(["script", "style", "noscript", "nav", "header", "footer", "form"]):
        t.decompose()
    lines = []
    for el in body.find_all(["h1", "h2", "h3", "p", "li"]):
        t = el.get_text(" ", strip=True)
        if t:
            lines.append(("# " if el.name in ("h1", "h2", "h3") else "") + t)
    return {"title": title, "meta": (md.get("content") or "") if md else "", "text": "\n".join(dict.fromkeys(lines))[:8000]}


def validate(t: dict) -> dict:
    flags = []
    title = (t.get("title") or {}).get("suggested") or ""
    title = title.split(" | Theodore Roosevelt Presidential Library")[0]
    meta = (t.get("meta_description") or {}).get("suggested") or ""
    if len(title) > 60:
        flags.append(f"Suggested title is {len(title)} characters (limit 60)")
    if meta and not 100 <= len(meta) <= 160:
        flags.append(f"Suggested meta description is {len(meta)} characters (aim for 120-155)")
    if re.search(r"\b(18|19|20)\d\d\b", title + " " + meta):
        flags.append("Suggestion contains a year: check it against the page and the no-years rule")
    t["checks"] = flags
    return t


def pick_pages(cfg: dict) -> list[str]:
    tcfg = cfg.get("tips", {})
    n, min_impr = tcfg.get("max_pages", 8), tcfg.get("min_impressions", 50)
    pages_impr = {r["page"]: r["impressions"] for r in C.read_json("gsc/pages.json", []) or []}
    opp = (C.read_json("opportunities.json", {}) or {}).get("page_scores", [])
    picked = [r["page"] for r in opp if pages_impr.get(r["page"], 0) >= min_impr][:n]
    if len(picked) < n:  # top up with weak, important pages from the audit
        skip = re.compile(r"/(quiz|video|staff-members|node|calendar|podcast)/")
        for p in C.read_json("audit/pages.json", []) or []:
            u = p.get("final_url") or p["url"]
            if p.get("status", 0) < 400 and not skip.search(u) and u not in picked and p["score"] < 85:
                picked.append(u)
            if len(picked) >= n:
                break
    return picked


def page_brief(url: str, cfg: dict) -> str:
    pg = page_text(url)
    nu = C.norm_url(url)
    queries = [r for r in C.read_json("gsc/query_pages.json", []) or [] if C.norm_url(r["page"]) == nu][:25]
    audit = next((p for p in C.read_json("audit/pages.json", []) or [] if C.norm_url(p.get("final_url") or p["url"]) == nu), {})
    issues = [ISSUE_TEXT[i][1] for i in audit.get("issues", [])]
    q_lines = "\n".join(f"- \"{q['query']}\": position {q['position']}, {q['impressions']} impressions, {q['clicks']} clicks" for q in queries) or "- (no Search Console data yet)"
    ai = C.read_json("ai/latest.json", {}) or {}
    missed = sorted({p["text"] for p in ai.get("prompts", []) for r in ai.get("results", [])
                     if r["prompt_id"] == p["id"] and not r.get("mentioned") and not r.get("error")})[:10]
    return f"""Page: {url}
Current title: {pg['title']}
Current meta description: {pg['meta'] or '(none)'}
Structured data types on page: {', '.join(audit.get('jsonld_types', [])) or 'none'}
Audit issues: {', '.join(issues) or 'none'}

Search queries this page shows up for (last 28 days):
{q_lines}

AI assistant questions where the Library was NOT mentioned this week (only use if relevant to this page):
{chr(10).join('- ' + m for m in missed) or '- (no AI visibility data yet)'}

Page text (headings marked with #):
{pg['text']}

Suggest improvements for this page. Return JSON in exactly this shape:
{PAGE_SCHEMA}"""


def ai_brief() -> str | None:
    ai = C.read_json("ai/latest.json")
    if not ai:
        return None
    lines = []
    for p in ai["prompts"]:
        for r in [r for r in ai["results"] if r["prompt_id"] == p["id"] and not r.get("error")]:
            lines.append(json.dumps({
                "prompt_id": p["id"], "question": p["text"], "engine": ai["providers"][r["provider"]]["label"],
                "mentioned": r["mentioned"], "cited_trlibrary": r["cited_us"], "position_among_attractions": r.get("position"),
                "also_mentioned": r.get("peers", []), "how_described": r.get("excerpt", ""),
                "sources_cited": r.get("cited_domains", [])[:8],
            }, ensure_ascii=False))
    return f"""Below are this week's answers from AI assistants to travel and history questions, one JSON object per answer.

{chr(10).join(lines)}

Most-cited source domains overall: {', '.join(d for d, _ in ai.get('top_cited_domains', [])[:15])}

Write a brief for the communications team. Return JSON in exactly this shape:
{AI_SCHEMA}"""


def run() -> None:
    cfg = C.config()
    key = C.env("ANTHROPIC_API_KEY")
    if not key:
        C.set_status("tips", "skipped", "Add the ANTHROPIC_API_KEY secret to turn on written recommendations.")
        return
    model = cfg.get("tips", {}).get("model", "claude-sonnet-5-5")
    out = {"updated": C.now_iso(), "model": model, "pages": [], "ai_brief": None, "errors": []}

    for url in pick_pages(cfg):
        try:
            t = validate(call_claude(key, model, page_brief(url, cfg)))
            out["pages"].append({"page": url, **t})
        except Exception as e:  # noqa: BLE001
            out["errors"].append(f"{url}: {e}"[:300])

    brief = ai_brief()
    if brief:
        try:
            out["ai_brief"] = call_claude(key, model, brief, max_tokens=3000)
        except Exception as e:  # noqa: BLE001
            out["errors"].append(f"AI brief: {e}"[:300])

    C.write_json("tips.json", out)
    if out["errors"] and not out["pages"]:
        C.set_status("tips", "error", out["errors"][0])
        raise C.JobError("tips failed")
    C.set_status("tips", "error" if out["errors"] else "ok",
                 f"Tips for {len(out['pages'])} pages" + (f"; {len(out['errors'])} failed" if out["errors"] else ""))


if __name__ == "__main__":
    run()
