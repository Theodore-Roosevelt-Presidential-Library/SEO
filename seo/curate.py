"""Self-managing tracking lists.

Each week, after Search Console data arrives:
  1. Retire discovered keywords that have WON (held the top 3) or FADED (searches dried up).
  2. Retire discovered AI questions that have WON (every assistant mentions the Library).
  3. Add new keywords from searches where we rank 4-30 with real demand.
  4. Add new AI questions from question-style Google searches.

Your own lists (config/keywords.yml, config/ai_prompts.yml) are never touched.
Discovered items live in docs/data/tracking.json, capped by config/tracking.yml,
and every add/retire is logged with a reason.

If any AI key is set, an AI filter screens candidates against the Library's goals
and rewrites searches into natural assistant questions. Without a key, simple rules
are used.
"""
from __future__ import annotations

import datetime as dt
import re

from . import common as C

QUESTION_START = re.compile(r"^(who|what|when|where|why|how|is|are|can|do|does|should|which|best|things to do|places to)\b", re.I)


def _weeks_since(iso: str) -> float:
    try:
        return (C.today() - dt.date.fromisoformat(iso[:10])).days / 7
    except Exception:  # noqa: BLE001
        return 999


def _norm(text: str) -> frozenset:
    return frozenset(w.rstrip("s") for w in C.content_words(text))


def _slug(text: str) -> str:
    return "auto-" + re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:50]


def load_state() -> dict:
    st = C.read_json("tracking.json") or {}
    st.setdefault("keywords", [])
    st.setdefault("prompts", [])
    st.setdefault("log", [])
    return st


def active_keywords() -> list[dict]:
    """Discovered keywords currently tracked (used by ranks.py)."""
    return [k for k in load_state()["keywords"] if k.get("status") == "active"]


def active_prompts() -> list[dict]:
    """Discovered AI questions currently tracked (used by ai_visibility.py)."""
    return [p for p in load_state()["prompts"] if p.get("status") == "active"]


def _added_this_week(st: dict, kind: str) -> int:
    return sum(1 for e in st["log"] if e["action"] == "added" and e["kind"] == kind and _weeks_since(e["date"]) < 1)


def _log(st: dict, action: str, kind: str, item: str, reason: str) -> None:
    st["log"].insert(0, {"date": C.today().isoformat(), "action": action, "kind": kind, "item": item, "reason": reason})
    st["log"] = st["log"][:200]


# ---------- AI filter (optional) ----------

def _ai_filter(candidates: list[dict], goals: str, want_prompts: bool) -> list[dict] | None:
    """Ask whichever AI is configured to keep only on-mission searches and, for prompts,
    rewrite them as natural questions. Returns None if no AI is available or it fails."""
    from . import tips
    providers = tips.available_providers(C.config())
    if not providers or not candidates:
        return None
    lines = "\n".join(f'- "{c["query"]}" ({c["impressions"]} impressions, position {c["position"]})' for c in candidates)
    if want_prompts:
        task = ("For each search worth tracking, write the question a traveler, student or teacher would type into an AI "
                "assistant (ChatGPT, Gemini) that should lead it to recommend or cite the Library. Do not mention the Library "
                "by name unless the search did. Group is one of: Trip planning, Museums, History, Brand.\n"
                'Return {"keep": [{"query": "...", "question": "...", "group": "...", "why": "short reason"}]}')
    else:
        task = ('Return {"keep": [{"query": "...", "group": "short group name like Visit, History, Learning", "why": "short reason"}]}')
    user = f"""The Library's goals: {goals}

Candidate Google searches that bring impressions to trlibrary.com:
{lines}

Keep only searches worth tracking for those goals; drop names of podcast guests or modern public figures, off-topic searches, and near-duplicates (keep the best-worded one). {task}"""
    try:
        res, _, _ = tips.Writer(providers).call(user)
        keep = res.get("keep") if isinstance(res, dict) else None
        return keep if isinstance(keep, list) else None
    except Exception as e:  # noqa: BLE001
        C.log(f"AI filter unavailable, using rules only: {e}")
        return None


# ---------- main ----------

def curate(st: dict, cfg: dict, tcfg: dict, queries: list[dict], ranks_hist: list[dict],
           ai_hist: list[dict], ai_filter=_ai_filter) -> dict:
    kc, pc = tcfg.get("keywords", {}), tcfg.get("ai_prompts", {})
    excl = [re.compile(p, re.I) for p in tcfg.get("exclude", [])]
    branded = [t.lower() for t in cfg.get("branded_query_terms", [])]
    gsc_q = {q["query"].lower(): q for q in queries}

    # ---- retire keywords ----
    for k in st["keywords"]:
        if k.get("status") != "active" or _weeks_since(k["added"]) < kc.get("min_weeks", 4):
            continue
        recent = [h.get("gsc", {}).get(k["keyword"]) for h in ranks_hist[-kc.get("graduate_top3_weeks", 4):]]
        if len(recent) >= kc.get("graduate_top3_weeks", 4) and all(p is not None and p <= 3 for p in recent):
            k.update(status="graduated", retired=C.today().isoformat(), retire_reason="held the top 3")
            _log(st, "graduated", "keyword", k["keyword"], f"top 3 for {len(recent)} weekly checks")
            continue
        impr = (gsc_q.get(k["keyword"]) or {}).get("impressions", 0)
        if impr < kc.get("fade_impressions", 75):
            k.update(status="retired", retired=C.today().isoformat(), retire_reason=f"searches dried up ({impr} impressions)")
            _log(st, "retired", "keyword", k["keyword"], f"only {impr} impressions in 28 days")

    # ---- retire prompts ----
    gw = pc.get("graduate_weeks", 4)
    for p in st["prompts"]:
        if p.get("status") != "active" or _weeks_since(p["added"]) < gw:
            continue
        weeks = [h.get("prompts", {}).get(p["id"]) for h in ai_hist[-gw:]]
        if len(weeks) >= gw and all(w and all(w.values()) for w in weeks):
            p.update(status="graduated", retired=C.today().isoformat(), retire_reason="every assistant mentions us")
            _log(st, "graduated", "question", p["text"], f"mentioned by every assistant {gw} weeks running")

    # ---- candidates ----
    manual_kw = {_norm(k) for g in (C.load_yaml("keywords.yml").get("groups") or {}).values() for k in (g or [])}
    manual_pr = {_norm(p["text"]) for p in C.load_yaml("ai_prompts.yml").get("prompts", [])}

    def blocked(text: str, kind: str, cooldown: int) -> bool:
        if any(r.search(text) for r in excl):
            return True
        items = st["keywords"] if kind == "keyword" else st["prompts"]
        field = "keyword" if kind == "keyword" else "source_query"
        for it in items:
            if _norm(it.get(field, "")) == _norm(text):
                if it.get("status") == "active" or _weeks_since(it.get("retired") or "1900-01-01") < cooldown:
                    return True
        return False

    lo, hi = kc.get("positions", [4, 30])
    from .opportunities import expected_ctr
    kw_cands = []
    for q in queries:
        text = q["query"].lower()
        if (lo <= q["position"] <= hi and q["impressions"] >= kc.get("min_impressions", 300)
                and len(C.content_words(text)) >= kc.get("min_words", 2)
                and not any(b in text for b in branded) and _norm(text) not in manual_kw
                and not blocked(text, "keyword", kc.get("cooldown_weeks", 12))):
            score = q["impressions"] * max(0.0, expected_ctr(3) - q["ctr"])
            if q.get("prev_impressions") and q["impressions"] > 1.5 * q["prev_impressions"]:
                score *= 1.5  # rising
            kw_cands.append({**q, "query": text, "score": round(score)})
    # collapse near-duplicates, keep the strongest
    seen, uniq = set(), []
    for c in sorted(kw_cands, key=lambda c: -c["score"]):
        n = _norm(c["query"])
        if n not in seen:
            seen.add(n)
            uniq.append(c)
    kw_cands = uniq[:40]

    active_k = [k for k in st["keywords"] if k.get("status") == "active"]
    room = min(kc.get("add_per_week", 5) - _added_this_week(st, "keyword"), kc.get("max_auto", 25) - len(active_k))
    if room > 0 and kw_cands:
        kept = ai_filter(kw_cands, tcfg.get("goals", ""), False)
        if kept is not None:
            by_q = {c["query"]: c for c in kw_cands}
            picks = [(by_q[k["query"].lower()], k.get("group") or "Discovered", k.get("why") or "")
                     for k in kept if isinstance(k, dict) and k.get("query", "").lower() in by_q]
        else:
            picks = [(c, "Discovered", "") for c in kw_cands]
        for c, group, why in picks[:room]:
            reason = f"position {c['position']}, {c['impressions']} impressions/28d" + (f"; {why}" if why else "")
            st["keywords"].append({"keyword": c["query"], "group": f"Auto: {group}", "status": "active",
                                   "added": C.today().isoformat(), "reason": reason, "score": c["score"]})
            _log(st, "added", "keyword", c["query"], reason)

    # ---- prompt candidates ----
    pr_cands = []
    for q in queries:
        text = q["query"].lower()
        if (q["impressions"] >= pc.get("min_impressions", 150) and QUESTION_START.search(text)
                and len(text.split()) >= 3 and C.content_words(text) and not any(b in text for b in branded)
                and _norm(text) not in manual_pr and not blocked(text, "prompt", pc.get("cooldown_weeks", 12))):
            pr_cands.append({**q, "query": text})
    pr_cands = sorted(pr_cands, key=lambda c: -c["impressions"])[:25]
    active_p = [p for p in st["prompts"] if p.get("status") == "active"]
    room = min(pc.get("add_per_week", 2) - _added_this_week(st, "question"), pc.get("max_auto", 8) - len(active_p))
    if room > 0 and pr_cands:
        kept = ai_filter(pr_cands, tcfg.get("goals", ""), True)
        if kept is not None:
            picks = [(k["query"].lower(), k.get("question") or "", k.get("group") or "Discovered", k.get("why") or "")
                     for k in kept if isinstance(k, dict) and k.get("question")]
        else:  # rules only: use the search itself, phrased as a question
            picks = [(c["query"], c["query"][:1].upper() + c["query"][1:].rstrip("?") + "?", "Discovered", "") for c in pr_cands]
        existing_ids = {p["id"] for p in st["prompts"]}
        for src, question, group, why in picks:
            if room <= 0:
                break
            pid = _slug(question)
            if pid in existing_ids or _norm(question) in manual_pr:
                continue
            reason = f"from the Google search \"{src}\"" + (f"; {why}" if why else "")
            st["prompts"].append({"id": pid, "group": group, "text": question, "source_query": src, "status": "active",
                                  "added": C.today().isoformat(), "reason": reason, "auto": True})
            _log(st, "added", "question", question, reason)
            room -= 1

    st["updated"] = C.now_iso()
    return st


def run() -> None:
    queries = C.read_json("gsc/queries.json")
    if not queries:
        C.set_status("curate", "skipped", "Waiting for Search Console data before discovering new keywords and questions.")
        return
    st = curate(load_state(), C.config(), C.load_yaml("tracking.yml"), queries,
                C.read_json("ranks/history.json", []) or [], C.read_json("ai/history.json", []) or [])
    C.write_json("tracking.json", st)
    today = C.today().isoformat()
    changes = [e for e in st["log"] if e["date"] == today]
    ak = sum(1 for k in st["keywords"] if k["status"] == "active")
    ap = sum(1 for p in st["prompts"] if p["status"] == "active")
    C.set_status("curate", "ok", f"{ak} discovered keywords and {ap} discovered questions tracked; {len(changes)} changes today")


if __name__ == "__main__":
    run()
