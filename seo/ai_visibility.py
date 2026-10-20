"""AI visibility: asks ChatGPT, Gemini, Perplexity and Claude the prompts in
config/ai_prompts.yml (with web search on, like a real user would get) and
records whether the Library is mentioned, how it is described, where it
falls among nearby attractions, and which sources each engine cites.

Each engine is optional and switches on when its key is present:
  OPENAI_API_KEY, GEMINI_API_KEY, PERPLEXITY_API_KEY, ANTHROPIC_API_KEY

Writes:
  ai/latest.json   every prompt x engine result from the latest run
  ai/history.json  weekly mention / citation rates
"""
from __future__ import annotations

import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

from . import common as C

KEYS = {
    "openai": "OPENAI_API_KEY",
    "gemini": "GEMINI_API_KEY",
    "perplexity": "PERPLEXITY_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
}
LABELS = {"openai": "ChatGPT", "gemini": "Gemini", "perplexity": "Perplexity", "anthropic": "Claude"}


# ---------- engine calls: each returns {"text": str, "citations": [url, ...]} ----------

def ask_openai(sess, key, model, prompt):
    sess.headers.update({"Authorization": f"Bearer {key}"})
    last = None
    for tool in ("web_search", "web_search_preview"):
        r = sess.post("https://api.openai.com/v1/responses", timeout=180,
                      json={"model": model, "input": prompt, "tools": [{"type": tool}]})
        if r.status_code == 200:
            break
        last = r
    else:
        raise RuntimeError(f"OpenAI {last.status_code}: {last.text[:200]}")
    text, cites = [], []
    for item in r.json().get("output", []):
        if item.get("type") != "message":
            continue
        for c in item.get("content", []):
            if c.get("type") == "output_text":
                text.append(c.get("text", ""))
                cites += [a.get("url") for a in c.get("annotations", []) if a.get("url")]
    return {"text": "\n".join(text), "citations": cites}


def ask_gemini(sess, key, model, prompt):
    r = C.gemini_post(sess, key, model, {"contents": [{"parts": [{"text": prompt}]}], "tools": [{"google_search": {}}]}, timeout=180)
    if r.status_code != 200:
        raise RuntimeError(f"Gemini {r.status_code}: {r.text[:200]}")
    cand = (r.json().get("candidates") or [{}])[0]
    text = "".join(p.get("text", "") for p in (cand.get("content") or {}).get("parts", []))
    cites = []
    for ch in (cand.get("groundingMetadata") or {}).get("groundingChunks", []):
        web = ch.get("web") or {}
        # Gemini returns redirect URLs; the title is usually the source domain.
        title = (web.get("title") or "").strip()
        cites.append(f"https://{title}/" if re.fullmatch(r"[\w.-]+\.[a-z]{2,}", title) else web.get("uri"))
    return {"text": text, "citations": [c for c in cites if c]}


def ask_perplexity(sess, key, model, prompt):
    r = sess.post("https://api.perplexity.ai/chat/completions", timeout=180,
                  headers={"Authorization": f"Bearer {key}"},
                  json={"model": model, "messages": [{"role": "user", "content": prompt}]})
    if r.status_code != 200:
        raise RuntimeError(f"Perplexity {r.status_code}: {r.text[:200]}")
    d = r.json()
    text = d["choices"][0]["message"]["content"]
    cites = d.get("citations") or [s.get("url") for s in d.get("search_results") or []]
    return {"text": text, "citations": [c for c in cites if c]}


def ask_anthropic(sess, key, model, prompt):
    r = sess.post("https://api.anthropic.com/v1/messages", timeout=240,
                  headers={"x-api-key": key, "anthropic-version": "2023-06-01"},
                  json={"model": model, "max_tokens": 2048,
                        "tools": [{"type": "web_search_20250305", "name": "web_search", "max_uses": 5}],
                        "messages": [{"role": "user", "content": prompt}]})
    if r.status_code != 200:
        raise RuntimeError(f"Claude {r.status_code}: {r.text[:200]}")
    text, cites, searched = [], [], []
    for b in r.json().get("content", []):
        if b.get("type") == "text":
            text.append(b.get("text", ""))
            cites += [c.get("url") for c in b.get("citations") or [] if c.get("url")]
        elif b.get("type") == "web_search_tool_result" and isinstance(b.get("content"), list):
            searched += [x.get("url") for x in b["content"] if x.get("url")]
    return {"text": "".join(text), "citations": cites or searched}


ASK = {"openai": ask_openai, "gemini": ask_gemini, "perplexity": ask_perplexity, "anthropic": ask_anthropic}


# ---------- analysis ----------

def analyse(text: str, citations: list[str], brand_re, peers: dict, our_domain: str) -> dict:
    m = brand_re.search(text or "")
    peer_hits = {}
    for name, aliases in peers.items():
        pm = C.brand_regex(aliases).search(text or "")
        if pm:
            peer_hits[name] = pm.start()
    position = None
    if m:
        position = 1 + sum(1 for off in peer_hits.values() if off < m.start())
    excerpt = ""
    if m:
        sentences = re.split(r"(?<=[.!?])\s+|\n+", text)
        hits = [s.strip() for s in sentences if brand_re.search(s)]
        excerpt = " … ".join(hits[:2])[:500]
    domains = [C.domain_of(u) for u in citations]
    return {
        "mentioned": bool(m),
        "cited_us": any(d.endswith(our_domain) for d in domains),
        "position": position,
        "peers": sorted(peer_hits, key=peer_hits.get),
        "excerpt": excerpt,
        "cited_domains": list(dict.fromkeys(d for d in domains if d)),
    }


def rates(rows: list[dict]) -> dict:
    ok = [r for r in rows if not r.get("error")]
    n = len(ok)
    return {
        "n": n,
        "mention_rate": round(sum(r["mentioned"] for r in ok) / n, 3) if n else None,
        "cite_rate": round(sum(r["cited_us"] for r in ok) / n, 3) if n else None,
    }


def run() -> None:
    cfg = C.config()
    pcfg = cfg.get("ai_visibility", {}).get("providers", {})
    active = {p: C.env(k) for p, k in KEYS.items() if C.env(k) and p in pcfg}
    if not active:
        C.set_status("ai_visibility", "skipped", "Add any of OPENAI_API_KEY, GEMINI_API_KEY, PERPLEXITY_API_KEY or ANTHROPIC_API_KEY to start tracking AI answers.")
        return
    prompts = C.load_yaml("ai_prompts.yml").get("prompts", [])
    brand_re = C.brand_regex(cfg.get("brand_terms", []))
    peers = cfg.get("peer_entities", {})
    our = C.domain_of(cfg["site"]["url"])

    # At most two calls in flight per engine, so free-tier rate limits aren't tripped.
    import threading
    gates = {p: threading.Semaphore(2) for p in active}

    def job(args):
        prov, p = args
        with gates[prov]:
            return _job(prov, p)

    def _job(prov, p):
        sess = C.session()
        model = pcfg[prov]["model"]
        try:
            ans = ASK[prov](sess, active[prov], model, p["text"])
            res = analyse(ans["text"], ans["citations"], brand_re, peers, our)
            return {"prompt_id": p["id"], "provider": prov, "model": model, **res,
                    "citations": ans["citations"][:20], "text": ans["text"][:6000]}
        except Exception as e:  # noqa: BLE001
            return {"prompt_id": p["id"], "provider": prov, "model": model, "error": str(e)[:300],
                    "mentioned": False, "cited_us": False}

    jobs = [(prov, p) for prov in active for p in prompts]
    with ThreadPoolExecutor(max_workers=6) as ex:
        results = list(ex.map(job, jobs))

    by_prov = {p: rates([r for r in results if r["provider"] == p]) for p in active}
    cited = Counter(d for r in results for d in r.get("cited_domains", []))
    C.write_json("ai/latest.json", {
        "updated": C.now_iso(),
        "providers": {p: {"label": LABELS[p], "model": pcfg[p]["model"], **by_prov[p]} for p in active},
        "prompts": prompts,
        "results": results,
        "top_cited_domains": cited.most_common(25),
    })
    C.upsert_history("ai/history.json", {
        "date": C.today().isoformat(),
        "overall": rates(results),
        "providers": by_prov,
        "prompts": {p["id"]: {r["provider"]: r["mentioned"] for r in results if r["prompt_id"] == p["id"]} for p in prompts},
    })
    errs = [r for r in results if r.get("error")]
    msg = f"{len(results) - len(errs)} answers from {', '.join(LABELS[p] for p in active)}"
    if errs and len(errs) == len(results):
        C.set_status("ai_visibility", "error", errs[0]["error"])
        raise C.JobError("all AI calls failed")
    C.set_status("ai_visibility", "error" if errs else "ok", msg + (f"; {len(errs)} failed: {errs[0]['error'][:150]}" if errs else ""))


if __name__ == "__main__":
    run()
