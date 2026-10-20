"""AI-written recommendations (works with Gemini, Claude, ChatGPT or Perplexity).

1. Page tips: for the pages with the most upside, the model reads the live page,
   its Search Console queries and its audit issues, and suggests a new title,
   meta description, content additions and AI-readiness fixes in TRPL voice.
2. AI visibility brief: the model reads the latest AI-answer results and lists
   the highest-value actions to get the Library recommended more often.

Uses the first available key in tips.prefer (config/site.yml): GEMINI_API_KEY,
ANTHROPIC_API_KEY, OPENAI_API_KEY or PERPLEXITY_API_KEY. Everything it writes is a DRAFT for human review;
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


KEYS = {"gemini": "GEMINI_API_KEY", "anthropic": "ANTHROPIC_API_KEY",
        "openai": "OPENAI_API_KEY", "perplexity": "PERPLEXITY_API_KEY"}
LABELS = {"gemini": "Gemini", "anthropic": "Claude", "openai": "ChatGPT", "perplexity": "Perplexity"}


def call_llm(provider: str, key: str, model: str, user: str, max_tokens: int = 4000) -> dict:
    """Send the house-rules system prompt + a brief to whichever model is configured; return parsed JSON."""
    sess = C.session()
    if provider == "gemini":
        r = C.gemini_post(sess, key, model, {
            "systemInstruction": {"parts": [{"text": SYSTEM}]},
            "contents": [{"role": "user", "parts": [{"text": user}]}],
            # no maxOutputTokens: Gemini's thinking tokens count against it and can truncate the JSON
            "generationConfig": {"responseMimeType": "application/json", "temperature": 0.4}}, timeout=300)
        ok = r.status_code == 200
        if ok:
            cand = (r.json().get("candidates") or [{}])[0]
            text = "".join(p.get("text", "") for p in (cand.get("content") or {}).get("parts", []) if not p.get("thought"))
    elif provider == "anthropic":
        r = sess.post("https://api.anthropic.com/v1/messages", timeout=300,
                      headers={"x-api-key": key, "anthropic-version": "2023-06-01"},
                      json={"model": model, "max_tokens": max_tokens, "system": SYSTEM,
                            "messages": [{"role": "user", "content": user}]})
        ok = r.status_code == 200
        if ok:
            text = "".join(b.get("text", "") for b in r.json().get("content", []) if b.get("type") == "text")
    elif provider in ("openai", "perplexity"):
        url = "https://api.openai.com/v1/chat/completions" if provider == "openai" else "https://api.perplexity.ai/chat/completions"
        body = {"model": model, "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]}
        if provider == "openai":
            body["response_format"] = {"type": "json_object"}
        r = sess.post(url, timeout=300, headers={"Authorization": f"Bearer {key}"}, json=body)
        ok = r.status_code == 200
        if ok:
            text = r.json()["choices"][0]["message"]["content"]
    else:
        raise ValueError(f"Unknown provider {provider}")
    if not ok:
        raise ProviderError(provider, r.status_code, f"{LABELS[provider]} {r.status_code}: {r.text[:200]}")
    return parse_json(text)


class ProviderError(RuntimeError):
    def __init__(self, provider: str, status: int, msg: str):
        super().__init__(msg)
        self.provider, self.status = provider, status


# Statuses that mean "this provider can't serve us right now" (bad key, no credit,
# quota, retired model, outage), so the run should move on to the next provider.
# Anything else (e.g. a reply that isn't valid JSON) only fails that one page.
FALLBACK_STATUSES = {401, 402, 403, 404, 429, 500, 502, 503, 529}


def available_providers(cfg: dict) -> list[tuple[str, str, str]]:
    """Every provider in tips.prefer that has a key, in order: (provider, key, model)."""
    tcfg = cfg.get("tips", {})
    vis_models = cfg.get("ai_visibility", {}).get("providers", {})
    out = []
    for p in tcfg.get("prefer", ["gemini", "anthropic", "openai", "perplexity"]):
        key = C.env(KEYS.get(p, ""))
        model = (tcfg.get("models") or {}).get(p) or (vis_models.get(p) or {}).get("model")
        if key and model:
            out.append((p, key, model))
    return out


def choose_provider(cfg: dict) -> tuple[str, str, str] | None:
    """First provider in tips.prefer that has a key."""
    av = available_providers(cfg)
    return av[0] if av else None


class Writer:
    """Calls the preferred provider; if it's out of credit, rate-limited or down,
    drops it for the rest of the run and moves to the next one in tips.prefer."""

    def __init__(self, providers: list[tuple[str, str, str]]):
        self.queue = list(providers)
        self.dropped: list[str] = []
        self.used: list[str] = []

    def call(self, user: str) -> tuple[dict, str, str]:
        last = None
        while self.queue:
            provider, key, model = self.queue[0]
            try:
                result = call_llm(provider, key, model, user)
                if provider not in self.used:
                    self.used.append(provider)
                return result, provider, model
            except ProviderError as e:
                if e.status not in FALLBACK_STATUSES:
                    raise
                last = e
                C.log(f"{LABELS[provider]} unavailable ({e.status}); trying the next provider")
                self.dropped.append(f"{LABELS[provider]} ({e.status})")
                self.queue.pop(0)
        raise last or RuntimeError("No AI provider available")


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
    providers = available_providers(cfg)
    if not providers:
        C.set_status("tips", "skipped", "Add any one of GEMINI_API_KEY, ANTHROPIC_API_KEY, OPENAI_API_KEY or PERPLEXITY_API_KEY to turn on written recommendations.")
        return
    w = Writer(providers)
    out = {"updated": C.now_iso(), "pages": [], "ai_brief": None, "errors": []}

    for url in pick_pages(cfg):
        try:
            t, prov, model = w.call(page_brief(url, cfg))
            out["pages"].append({"page": url, "written_by": f"{LABELS[prov]} ({model})", **validate(t)})
        except Exception as e:  # noqa: BLE001
            out["errors"].append(f"{url}: {e}"[:300])

    brief = ai_brief()
    if brief:
        try:
            out["ai_brief"], prov, model = w.call(brief)
            out["ai_brief"]["written_by"] = f"{LABELS[prov]} ({model})"
        except Exception as e:  # noqa: BLE001
            out["errors"].append(f"AI brief: {e}"[:300])

    used = w.used or [providers[0][0]]
    first = next(p for p in providers if p[0] == used[0])
    out.update(provider=used[0], provider_label=" + ".join(LABELS[p] for p in used),
               model=", ".join(m for p, _, m in providers if p in used) or first[2],
               fallbacks=w.dropped)

    C.write_json("tips.json", out)
    note = f"; skipped {', '.join(w.dropped)}" if w.dropped else ""
    if out["errors"] and not out["pages"]:
        C.set_status("tips", "error", out["errors"][0] + note)
        raise C.JobError("tips failed")
    C.set_status("tips", "error" if out["errors"] else "ok",
                 f"{out['provider_label']} wrote tips for {len(out['pages'])} pages{note}"
                 + (f"; {len(out['errors'])} failed" if out["errors"] else ""))


if __name__ == "__main__":
    run()
