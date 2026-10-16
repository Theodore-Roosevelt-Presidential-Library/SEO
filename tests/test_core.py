import os
import tempfile

os.environ.setdefault("SEO_DATA_DIR", tempfile.mkdtemp())

from seo import ai_visibility, audit, common as C, opportunities, ranks, tips  # noqa: E402

HTML = """<html lang="en"><head><title>Visit | Theodore Roosevelt Presidential Library</title>
<meta name="description" content="Plan a visit to the Library in Medora, North Dakota: hours, tickets, directions and what to expect inside.">
<link rel="canonical" href="https://www.trlibrary.com/visit">
<meta property="og:title" content="Visit"><meta property="og:description" content="x"><meta property="og:image" content="y.jpg">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Museum"}</script></head>
<body><header>nav stuff</header><main><h1>Plan your visit</h1><h2>How long does a visit take?</h2>
<p>""" + "word " * 320 + """</p><img src="a.jpg" alt=""><img src="b.jpg"></main></body></html>"""


def test_parse_and_check_page():
    p = audit.parse_page(HTML, "https://www.trlibrary.com/visit")
    assert p["title"].startswith("Visit")
    assert p["jsonld_types"] == ["Museum"]
    assert p["question_headings"] == 1
    assert p["images_no_alt"] == 1  # alt="" is fine, missing alt is not
    assert p["words"] > 300
    p.update(url="https://www.trlibrary.com/visit", final_url="https://www.trlibrary.com/visit", status=200, seconds=0.4)
    issues = audit.check_page(p)
    assert issues == ["img_alt_missing"]
    assert audit.page_score(issues) == 97
    assert audit.ai_ready(p)["score"] == 100


def test_check_page_problems():
    p = {"url": "https://www.trlibrary.com/node/12", "final_url": "https://www.trlibrary.com/node/12", "status": 200,
         "title": "", "h1": [], "canonical": "https://www.trlibrary.com/other", "words": 10}
    issues = audit.check_page(p)
    for code in ("unaliased_url", "title_missing", "meta_missing", "h1_missing", "canonical_mismatch", "og_missing", "thin_content"):
        assert code in issues
    assert audit.check_page({"url": "u", "status": 404}) == ["http_error"]


def test_norm_url():
    assert C.norm_url("https://www.trlibrary.com/visit/") == C.norm_url("https://trlibrary.com/visit")


def test_opportunities():
    qp = [
        {"query": "medora museum", "page": "https://www.trlibrary.com/visit", "clicks": 5, "impressions": 900, "ctr": 0.0056, "position": 7.2},
        {"query": "medora museum", "page": "https://www.trlibrary.com/about", "clicks": 2, "impressions": 400, "ctr": 0.005, "position": 9.0},
        {"query": "tr library hours", "page": "https://www.trlibrary.com/visit", "clicks": 10, "impressions": 500, "ctr": 0.02, "position": 2.1},
    ]
    pages = [{"page": "https://www.trlibrary.com/visit", "clicks": 15, "impressions": 1400, "ctr": 0.011, "position": 3.0, "prev_clicks": 40}]
    queries = [{"query": "medora museum", "clicks": 7, "impressions": 1300, "ctr": 0.005, "position": 7.8, "prev_clicks": 20}]
    audit_pages = [{"url": "https://www.trlibrary.com/visit", "title": "Plan Your Visit"}]
    out = opportunities.build(qp, queries, pages, audit_pages)
    assert out["striking_distance"][0]["query"] == "medora museum"
    assert out["low_ctr"][0]["page"].endswith("/visit")
    assert any(r["query"] == "medora museum" for r in out["missing_in_title"])
    assert out["cannibalization"][0]["query"] == "medora museum"
    assert {d["kind"] for d in out["declining"]} == {"query", "page"}
    assert out["page_scores"][0]["page"].endswith("/visit")


def test_ai_analyse():
    text = ("Start at Theodore Roosevelt National Park. Then see the Medora Musical. "
            "The Theodore Roosevelt Presidential Library opened in Medora and is a great stop.")
    peers = {"Theodore Roosevelt National Park": ["Theodore Roosevelt National Park"], "Medora Musical": ["Medora Musical"]}
    r = ai_visibility.analyse(text, ["https://www.trlibrary.com/visit", "https://nps.gov/thro"],
                              C.brand_regex(["Theodore Roosevelt Presidential Library", "trlibrary.com"]), peers, "trlibrary.com")
    assert r["mentioned"] and r["cited_us"]
    assert r["position"] == 3
    assert r["peers"] == ["Theodore Roosevelt National Park", "Medora Musical"]
    assert "Presidential Library opened" in r["excerpt"]
    r2 = ai_visibility.analyse("Visit the national park.", [], C.brand_regex(["Theodore Roosevelt Presidential Library"]), {}, "trlibrary.com")
    assert not r2["mentioned"] and r2["position"] is None


def test_brand_regex_does_not_match_inside_words():
    rx = C.brand_regex(["TR Library"])
    assert rx.search("the TR Library is open")
    assert not rx.search("the STR Library")


def test_parse_serp():
    result = {"items": [
        {"type": "ai_overview", "references": [{"url": "https://www.trlibrary.com/visit"}, {"url": "https://www.nps.gov/thro"}]},
        {"type": "organic", "rank_group": 1, "url": "https://www.nps.gov/thro", "title": "TRNP"},
        {"type": "organic", "rank_group": 2, "url": "https://www.trlibrary.com/", "title": "TRPL"},
        {"type": "people_also_ask"},
    ]}
    s = ranks.parse_serp(result, "trlibrary.com")
    assert s["rank"] == 2 and s["ai_overview"] and s["ai_overview_cites_us"]
    assert s["features"] == ["ai_overview", "people_also_ask"]


def test_tips_json_and_validate():
    t = tips.parse_json('```json\n{"title": {"suggested": "' + "x" * 70 + '"}, "meta_description": {"suggested": "Open 2027"}}\n```')
    v = tips.validate(t)
    assert len(v["checks"]) == 3


def test_upsert_history():
    C.upsert_history("t/h.json", {"date": "2026-01-01", "v": 1})
    C.upsert_history("t/h.json", {"date": "2026-01-01", "v": 2})
    h = C.upsert_history("t/h.json", {"date": "2026-01-08", "v": 3})
    assert [r["v"] for r in h] == [2, 3]
