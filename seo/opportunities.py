"""Rules-based opportunities from Search Console + the site audit.
No API key needed (it uses whatever data the other jobs have produced).

Writes opportunities.json with these lists:
  striking_distance  queries ranking 4-20 with real demand: a push could reach the top 3
  low_ctr            pages ranking well but getting few clicks: title/description rewrite
  missing_in_title   high-impression queries the ranking page's title doesn't mention
  declining          queries and pages losing clicks vs the previous 28 days
  cannibalization    queries where two or more of our pages compete
  page_scores        every page ranked by total opportunity (feeds the tips job)
  held_back          pages left out because they changed recently (config/changes.yml);
                     their 28-day numbers still mostly describe the old version
"""
from __future__ import annotations

from collections import defaultdict

from . import changes as CH, common as C

# Rough organic click-through rate by position (industry averages, desktop+mobile blend).
# Only used to estimate *relative* upside; not a forecast.
CTR_CURVE = {1: 0.28, 2: 0.16, 3: 0.11, 4: 0.08, 5: 0.06, 6: 0.045, 7: 0.035, 8: 0.03, 9: 0.025, 10: 0.02}


def expected_ctr(pos: float) -> float:
    p = max(1, round(pos))
    return CTR_CURVE.get(p, 0.01 if p <= 20 else 0.003)


def build(query_pages, queries, pages, audit_pages, min_impr: int = 30) -> dict:
    audit_by = {C.norm_url(p.get("final_url") or p["url"]): p for p in audit_pages or []}

    # striking distance
    sd = []
    for r in query_pages:
        if 4 <= r["position"] <= 20 and r["impressions"] >= min_impr:
            gain = r["impressions"] * (expected_ctr(3) - r["ctr"])
            if gain > 0:
                sd.append({**r, "est_extra_clicks": round(gain)})
    sd.sort(key=lambda r: -r["est_extra_clicks"])

    # low CTR for position
    low = []
    for r in pages:
        if r["position"] <= 8 and r["impressions"] >= min_impr * 3:
            exp = expected_ctr(r["position"])
            if r["ctr"] < exp * 0.5:
                low.append({**r, "expected_ctr": exp, "est_extra_clicks": round(r["impressions"] * (exp - r["ctr"]))})
    low.sort(key=lambda r: -r["est_extra_clicks"])

    # query not reflected in the ranking page's title
    mit = []
    best_page = {}
    for r in query_pages:  # sorted by impressions desc
        best_page.setdefault(r["query"], r)
    for q, r in best_page.items():
        if r["impressions"] < min_impr * 2:
            continue
        a = audit_by.get(C.norm_url(r["page"]))
        title = (a or {}).get("title") or ""
        if not a or not title:
            continue
        words = C.content_words(q)
        tw = set(C.content_words(title))
        missing = [w for w in words if w not in tw and w.rstrip("s") not in tw]
        if words and len(missing) / len(words) >= 0.5:
            mit.append({**r, "title": title, "missing_words": missing})
    mit.sort(key=lambda r: -r["impressions"])

    # declining
    dec = []
    for kind, rows, key in (("query", queries, "query"), ("page", pages, "page")):
        for r in rows:
            pc = r.get("prev_clicks", 0)
            if pc >= 10 and r["clicks"] < pc * 0.7:
                dec.append({"kind": kind, "item": r[key], "clicks": r["clicks"], "prev_clicks": pc,
                            "change": round((r["clicks"] - pc) / pc, 3), "position": r["position"],
                            "prev_position": r.get("prev_position")})
    dec.sort(key=lambda r: r["clicks"] - r["prev_clicks"])

    # cannibalization
    by_q = defaultdict(list)
    for r in query_pages:
        if r["impressions"] >= min_impr / 3:
            by_q[r["query"]].append(r)
    can = []
    for q, rows in by_q.items():
        if len(rows) >= 2:
            tot = sum(x["impressions"] for x in rows)
            if tot >= min_impr * 2 and rows[1]["impressions"] >= tot * 0.2:
                can.append({"query": q, "impressions": tot,
                            "pages": [{"page": x["page"], "impressions": x["impressions"], "position": x["position"]} for x in rows[:4]]})
    can.sort(key=lambda r: -r["impressions"])

    # page-level roll-up
    score = defaultdict(lambda: {"est_extra_clicks": 0, "reasons": set()})
    for r in sd:
        s = score[r["page"]]; s["est_extra_clicks"] += r["est_extra_clicks"]; s["reasons"].add("striking_distance")
    for r in low:
        s = score[r["page"]]; s["est_extra_clicks"] += r["est_extra_clicks"]; s["reasons"].add("low_ctr")
    for r in mit:
        score[r["page"]]["reasons"].add("missing_in_title")
    page_scores = sorted(
        ({"page": p, "est_extra_clicks": v["est_extra_clicks"], "reasons": sorted(v["reasons"])} for p, v in score.items()),
        key=lambda r: -r["est_extra_clicks"],
    )

    return {
        "striking_distance": sd[:150],
        "low_ctr": low[:60],
        "missing_in_title": mit[:80],
        "declining": dec[:80],
        "cannibalization": can[:50],
        "page_scores": page_scores[:200],
    }


def hold_back(out: dict, held: set[str], log: dict | None = None) -> dict:
    """Remove recently changed pages from the fix-it lists; flag them in 'declining'
    (a drop right after a change is worth seeing) and in 'cannibalization'."""
    changed_on = {p: e[0]["date"].isoformat() for p, e in CH.by_page(log or CH.load()).items() if p in held}
    held_rows: dict = {}
    for key in ("striking_distance", "low_ctr", "missing_in_title", "page_scores"):
        keep = []
        for r in out.get(key, []):
            p = CH.path_of(r["page"])
            if p in held:
                h = held_rows.setdefault(p, {"page": r["page"], "changed": changed_on.get(p), "lists": []})
                if key not in h["lists"]:
                    h["lists"].append(key)
            else:
                keep.append(r)
        out[key] = keep
    for r in out.get("declining", []):
        if r["kind"] == "page" and CH.path_of(r["item"]) in held:
            r["changed"] = changed_on.get(CH.path_of(r["item"]))
    for r in out.get("cannibalization", []):
        for p in r["pages"]:
            if CH.path_of(p["page"]) in held:
                p["changed"] = changed_on.get(CH.path_of(p["page"]))
    out["held_back"] = sorted(held_rows.values(), key=lambda r: r["page"])
    return out


def run() -> None:
    qp = C.read_json("gsc/query_pages.json")
    if not qp:
        C.set_status("opportunities", "skipped", "Waiting for Search Console data.")
        return
    out = build(qp, C.read_json("gsc/queries.json", []), C.read_json("gsc/pages.json", []),
                C.read_json("audit/pages.json", []))
    log = CH.load()
    out = hold_back(out, CH.held_paths(log=log), log)
    out["updated"] = C.now_iso()
    out["note"] = "Estimated extra clicks use a rough industry click-through curve. Treat them as a way to rank opportunities, not a forecast."
    C.write_json("opportunities.json", out)
    C.set_status("opportunities", "ok", f"{len(out['striking_distance'])} striking-distance queries, {len(out['low_ctr'])} low-CTR pages"
                 + (f"; {len(out['held_back'])} recently changed pages held back" if out["held_back"] else ""))


if __name__ == "__main__":
    run()
