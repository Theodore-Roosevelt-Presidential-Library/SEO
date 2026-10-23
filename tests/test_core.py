import json
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


def test_tips_provider_choice(monkeypatch):
    for k in ("GEMINI_API_KEY", "ANTHROPIC_API_KEY", "OPENAI_API_KEY", "PERPLEXITY_API_KEY"):
        monkeypatch.delenv(k, raising=False)
    cfg = C.config()
    assert tips.choose_provider(cfg) is None
    monkeypatch.setenv("GEMINI_API_KEY", "g")
    assert tips.choose_provider(cfg) == ("gemini", "g", cfg["ai_visibility"]["providers"]["gemini"]["model"])
    monkeypatch.setenv("ANTHROPIC_API_KEY", "a")
    assert tips.choose_provider(cfg)[0] == "gemini"  # preference order wins
    monkeypatch.delenv("GEMINI_API_KEY")
    assert tips.choose_provider(cfg)[:2] == ("anthropic", "a")


def test_gemini_call_shape(monkeypatch):
    sent = {}

    class R:
        status_code = 200
        def json(self):
            return {"candidates": [{"content": {"parts": [{"text": "thinking...", "thought": True}, {"text": '{"summary": "ok"}'}]}}]}

    class S:
        def post(self, url, **kw):
            sent.update(url=url, **kw)
            return R()

    monkeypatch.setattr(C, "session", lambda *a, **k: S())
    assert tips.call_llm("gemini", "k", "gemini-2.5-pro", "brief") == {"summary": "ok"}
    assert "systemInstruction" in sent["json"] and sent["params"] == {"key": "k"}


def test_gemini_retired_model_retry():
    calls = []

    class R:
        def __init__(self, code, text=""):
            self.status_code, self.text = code, text

    class S:
        def post(self, url, **kw):
            calls.append(url)
            if "old-model" in url:
                return R(404, '{"error": {"message": "no longer available. Please update your code to use models/new-model-2 for"}}')
            return R(200)

    r = C.gemini_post(S(), "k", "old-model", {})
    assert r.status_code == 200 and "new-model-2" in calls[-1] and len(calls) == 2


def test_digest_builds_without_data(tmp_path, monkeypatch):
    from seo import digest
    monkeypatch.setattr(C, "DATA_DIR", tmp_path / "data")
    digest.run()
    assert (tmp_path / "llms.txt").read_text().startswith("# TRPL Search & AI Visibility")
    assert "## Raw data" in (tmp_path / "digest.md").read_text()


def test_tips_fallback(monkeypatch):
    calls = []

    def fake(provider, key, model, user, max_tokens=4000):
        calls.append(provider)
        if provider == "gemini":
            raise tips.ProviderError("gemini", 429, "Gemini 429: quota")
        return {"summary": "ok"}

    monkeypatch.setattr(tips, "call_llm", fake)
    w = tips.Writer([("gemini", "g", "gm"), ("anthropic", "a", "am")])
    assert w.call("x")[1] == "anthropic"
    assert w.call("y")[1] == "anthropic"
    assert calls == ["gemini", "anthropic", "anthropic"]  # Gemini dropped after first failure
    assert w.dropped == ["Gemini (429)"]


def test_tips_no_fallback_on_bad_json(monkeypatch):
    def fake(provider, *a, **k):
        raise ValueError("No JSON in model reply")
    monkeypatch.setattr(tips, "call_llm", fake)
    w = tips.Writer([("gemini", "g", "gm"), ("anthropic", "a", "am")])
    try:
        w.call("x")
    except ValueError:
        pass
    assert len(w.queue) == 2  # a bad reply doesn't drop the provider


def _q(query, impressions, position, ctr=0.005, prev=None):
    return {"query": query, "impressions": impressions, "position": position, "ctr": ctr, "clicks": 1,
            "prev_impressions": prev or impressions}


def test_curate_adds_caps_and_retires(monkeypatch):
    from seo import curate
    cfg = C.config()
    tcfg = {"keywords": {"max_auto": 3, "add_per_week": 2, "min_impressions": 100, "positions": [4, 30], "min_words": 2,
                         "min_weeks": 0, "graduate_top3_weeks": 2, "fade_impressions": 50, "cooldown_weeks": 12},
            "ai_prompts": {"max_auto": 2, "add_per_week": 1, "min_impressions": 100, "graduate_weeks": 2},
            "exclude": ["karl rove"], "goals": ""}
    queries = [_q("karl rove podcast", 9000, 9), _q("badlands museum hours", 800, 8), _q("medora winter things", 600, 12),
               _q("how long is the scenic loop drive", 500, 6), _q("theodore", 5000, 10), _q("tr library tickets", 900, 7)]
    st = curate.curate({"keywords": [], "prompts": [], "log": []}, cfg, tcfg, queries, [], [], ai_filter=lambda *a: None)
    kws = [k["keyword"] for k in st["keywords"]]
    assert "karl rove podcast" not in kws          # excluded
    assert "theodore" not in kws                   # one word
    assert "tr library tickets" not in kws         # branded
    assert len(kws) == 2                            # add_per_week cap
    assert [p["text"] for p in st["prompts"]] == ["How long is the scenic loop drive?"]

    # a second run the same week adds nothing more
    st = curate.curate(st, cfg, tcfg, queries, [], [], ai_filter=lambda *a: None)
    assert len(st["keywords"]) == 2 and len(st["prompts"]) == 1

    # graduation: two weekly checks in the top 3; fading: impressions dry up
    won, faded = st["keywords"][0]["keyword"], st["keywords"][1]["keyword"]
    hist = [{"gsc": {won: 2.5}}, {"gsc": {won: 1.8}}]
    q2 = [_q(won, 900, 2), _q(faded, 10, 15)]
    st = curate.curate(st, cfg, tcfg, q2, hist, [], ai_filter=lambda *a: None)
    status = {k["keyword"]: k["status"] for k in st["keywords"]}
    assert status[won] == "graduated" and status[faded] == "retired"

    # cooldown: a retired keyword isn't re-added even if it qualifies again
    for e in st["log"]:
        e["date"] = "2000-01-01"   # pretend the adds were long ago so the weekly cap resets
    st = curate.curate(st, cfg, tcfg, [_q(faded, 900, 9)], [], [], ai_filter=lambda *a: None)
    assert sum(1 for k in st["keywords"] if k["keyword"] == faded) == 1


def test_curate_uses_ai_filter():
    from seo import curate
    tcfg = {"keywords": {"add_per_week": 5, "min_impressions": 100, "min_words": 2},
            "ai_prompts": {"add_per_week": 2, "min_impressions": 100}, "exclude": [], "goals": "g"}
    queries = [_q("badlands museum hours", 800, 8), _q("random celebrity news", 900, 9), _q("what to do near medora", 700, 7)]

    def fake(cands, goals, want_prompts):
        if want_prompts:
            return [{"query": "what to do near medora", "question": "What should I do near Medora, North Dakota?", "group": "Trip planning"}]
        return [{"query": "badlands museum hours", "group": "Visit", "why": "visit intent"}]

    st = curate.curate({"keywords": [], "prompts": [], "log": []}, C.config(), tcfg, queries, [], [], ai_filter=fake)
    assert [k["keyword"] for k in st["keywords"]] == ["badlands museum hours"]
    assert st["keywords"][0]["group"] == "Auto: Visit"
    assert st["prompts"][0]["text"] == "What should I do near Medora, North Dakota?"


def test_perplexity_agent_parsing():
    sent = []

    class R:
        def __init__(self, code, data=None, text=""):
            self.status_code, self._d, self.text = code, data, text
        def json(self):
            return self._d

    class S:
        def post(self, url, **kw):
            sent.append((url, kw["json"]))
            if url.endswith("/v1/responses"):
                return R(404, text="not found")
            return R(200, {"output": [
                {"type": "search_results", "results": [{"url": "https://www.nps.gov/thro"}, {"url": "https://www.trlibrary.com/visit"}]},
                {"type": "message", "content": [{"type": "output_text", "text": "Visit the Library [2].", "annotations": []}]}]})

    out = C.perplexity_agent(S(), "k", "What to see near TRNP?", model="fast")
    assert out["text"] == "Visit the Library [2]."
    assert out["citations"] == ["https://www.nps.gov/thro", "https://www.trlibrary.com/visit"]
    assert sent[-1][0].endswith("/v1/agent") and sent[-1][1] == {"input": "What to see near TRNP?", "preset": "fast"}


def test_ux_readability_and_task_check():
    import re as _re
    from seo import ux
    html = """<html><body><header><a href="/tickets">Tickets</a></header><main><h1>Hours</h1>
    <p>The Library is open daily. Plan to spend about three and a half hours.</p>
    <ul><li>Monday to Friday 9 to 5</li><li>Weekends 9 to 6</li></ul>
    <p><a href="https://access.trlibrary.com/orders/613">Buy tickets</a></p></main></body></html>"""
    rd = ux.readability(html, "https://www.trlibrary.com/visit/hours", _re.compile(r"access\.trlibrary\.com|/tickets\b"))
    assert rd["words_before_ticket_link"] is not None and rd["words_before_ticket_link"] > 10   # header link ignored
    assert rd["grade_level"] < 8 and ux.reading_label(rd["grade_level"]) == "easy"
    assert "# Hours" in rd["text"]

    class W:
        def call(self, user):
            assert "When is the Library open?" in user and "Buy tickets -> https://access" in user
            return ({"tasks": {"hours": {"status": "top", "note": "first line"}, "price": {"status": "linked"},
                               "food": {"status": "not_relevant"}},
                     "facts": {"hours": "Monday to Friday 9 to 5"}, "biggest_fix": "Add prices."}, "gemini", "m")

    tc = ux.task_check(W(), "u", rd, {"hours": "When is the Library open?", "price": "How much?", "food": "Food?", "buy": "Buy?"})
    assert tc["tasks"]["buy"]["status"] == "missing"            # not returned -> missing
    assert tc["findability"] == round(100 * (1 + 0.75 + 0) / 3)  # not_relevant excluded


def test_checkout_rates_never_expose_counts():
    from seo import checkout
    counts = {"store_visit": 1000, "add_to_cart": 400, "begin_checkout": 300, "purchase": 240}
    r = checkout.rates(counts, ["view_item", "add_to_cart", "begin_checkout", "add_payment_info", "purchase"], 30)
    assert r["checkout_completion"] == 0.8 and r["store_conversion"] == 0.24
    assert r["missing_steps"] == ["view_item", "add_payment_info"]
    flat = json.dumps(r)
    for n in ("1000", "400", "300", "240"):
        assert n not in flat                                      # no raw counts in public output
    small = checkout.rates({"store_visit": 12, "begin_checkout": 5, "purchase": 4}, ["begin_checkout", "purchase"], 30)
    assert small["checkout_completion"] == "low volume" and small["store_conversion"] == "low volume"


def test_clarity_store_friction(monkeypatch):
    from seo import checkout
    url_resp = [
        {"metricName": "DeadClickCount", "information": [
            {"sessionsCount": "500", "sessionsWithMetricPercentage": 22.5, "Url": "https://access.trlibrary.com/orders/613/calendar?eventId=699756534428678a27bde26f"},
            {"sessionsCount": "300", "sessionsWithMetricPercentage": 10.0, "Url": "https://access.trlibrary.com/checkout/613/forms"}]},
        {"metricName": "ScrollDepth", "information": [{"averageScrollDepth": 61.2, "URL": "https://access.trlibrary.com/checkout/613/forms"}]},
        {"metricName": "Traffic", "information": [{"totalSessionCount": "800"}]}]
    overall_resp = [{"metricName": "DeadClickCount", "information": [{"sessionsCount": "800", "sessionsWithMetricPercentage": 20.5}]}]

    class R:
        status_code = 200
        def __init__(self, d): self.d = d
        def json(self): return self.d

    class S:
        def get(self, url, params=None, **kw):
            return R(url_resp if params.get("dimension1") else overall_resp)

    monkeypatch.setattr(C, "session", lambda *a, **k: S())
    monkeypatch.setenv("CLARITY_STORE_API_TOKEN", "t")
    f, err = checkout.store_friction()
    assert err is None and f["overall"] == {"dead_clicks": 20.5}
    assert f["pages"]["orders/calendar"] == {"dead_clicks": 22.5}
    assert f["pages"]["checkout/forms"] == {"dead_clicks": 10.0, "scroll_depth": 61.2}
    assert "800" not in json.dumps(f) and "500" not in json.dumps(f)   # no session counts published


def test_links_names_and_redirects():
    from seo import links
    assert links.names_for("/tr/people/jacob-riis", "Jacob Riis: The Photographer Who Opened Roosevelt's Eyes", "") == ["Jacob Riis", "jacob riis"]
    assert links.names_for("/visit/national-park", "Theodore Roosevelt National Park", "") == ["Theodore Roosevelt National Park"]
    t = "The valley within Yosemite National Park was dammed."
    assert links.inside_longer_name(t, t.index("National Park"))
    t = "When Roosevelt served as Civil Service Commissioner"
    assert not links.inside_longer_name(t, t.index("Civil Service"))
    t = "The Bully Pulpit Golf Course is nearby"
    assert links.continues_into_name(t, t.index("Pulpit") + len("Pulpit"))
    live = {"/tr", "/tr/people/ted-jr", "/tr/badlands", "/tr/people/alice-longworth", "/"}
    s = links.suggest_redirect
    assert s("/tr/people/ted-jr.html", live, {}, {})["to"] == "/tr/people/ted-jr"
    assert s("/tr/people/ted-jr.html", live, {}, {})["confidence"] == "high"
    assert s("/tr/badlands/overview", live, {}, {})["to"] == "/tr/badlands"
    assert s("/tr/people/alice-roosevelt", live, {"alice roosevelt": ["/tr/people/alice-longworth"]}, {})["to"] == "/tr/people/alice-longworth"
    assert s("/orders/613/tickets", live, {}, {})["to"] == "https://access.trlibrary.com/orders/613/tickets"
    assert s("/tr/zzz/nothing-like-it", live, {}, {})["confidence"] == "low"


def test_links_parse_marks_linked_text_and_skips_nav():
    from seo import links
    html = """<html><body><main><nav><a href="/tr">Theodore Roosevelt</a></nav><h1>Henry Cabot Lodge</h1>
    <p>Lodge met <a href="/tr/people/jacob-riis">Jacob Riis</a> and later backed the Square Deal in the Senate.</p>
    <p><a href="https://example.com">Outside</a> and <a href="/tr/old-page.html">old</a></p></main></body></html>"""
    d = links.parse(html, "https://www.trlibrary.com/tr/people/henry-cabot-lodge", "trlibrary.com")
    assert d["h1"] == "Henry Cabot Lodge"
    assert "/tr" not in d["links"]                      # breadcrumb/nav ignored
    assert "/tr/people/jacob-riis" in d["links"] and "/tr/old-page.html" in d["raw_links"]
    assert "Jacob Riis" not in d["paras"][0] and "Square Deal" in d["paras"][0]


# ---------- structured data ----------
from seo import schema  # noqa: E402

FAQ_HTML = """<html><head><meta property="og:title" content="Tickets"><meta property="og:type" content="website">
<script type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":["Museum","Library"],"@id":"https://www.trlibrary.com/#organization","name":"X"},{"@type":"Person","@id":"https://www.trlibrary.com/tr/#person"}]}</script></head>
<body><main><h1>Tickets</h1>
<div data-custom-accordion><h2><button data-custom-accordion-button><span>keyboard_arrow_up</span> How do I buy tickets?</button></h2>
<div data-custom-accordion-body><p>Online or at the Welcome Desk.</p></div></div>
<div data-custom-accordion><h2><button data-custom-accordion-button>Can I park an RV?</button></h2>
<div data-custom-accordion-body><p>Yes, in the RV lot.</p></div></div>
<div data-custom-accordion><h2><button data-custom-accordion-button>Parking</button></h2><div data-custom-accordion-body><p>Free.</p></div></div>
</main></body></html>"""


def test_schema_extract_faq_and_stub_ids():
    p = schema.extract(FAQ_HTML, "https://www.trlibrary.com/visit/faq/tickets")
    assert p["faq"] == [("How do I buy tickets?", "Online or at the Welcome Desk."), ("Can I park an RV?", "Yes, in the RV lot.")]
    assert "https://www.trlibrary.com/tr/#person" in p["stub_ids"]
    assert "https://www.trlibrary.com/#organization" in p["defined_ids"]
    j = schema.build_faq(p, {})
    assert j["@type"] == "FAQPage" and len(j["mainEntity"]) == 2
    json.dumps(j)  # serialisable


def test_schema_classify_and_missing_props():
    p = schema.extract(FAQ_HTML, "https://www.trlibrary.com/tr/badlands/maltese-cross")
    keys = [g["key"] for g in schema.classify("/tr/badlands/maltese-cross", p)]
    assert keys == ["faq", "tr_articles"]
    assert [g["key"] for g in schema.classify("/tr/speeches/new-nationalism", {"faq": []})] == ["tr_speeches"]
    assert [g["key"] for g in schema.classify("/calendar/special-event/x", {"faq": []})] == ["event"]
    nodes = [{"@type": "NewsArticle", "headline": "h", "datePublished": "2020-10-27T06:00:00-0600", "image": "i"}]
    assert schema.missing_props(nodes, {"NewsArticle"}) == ["author", "publisher"]
    assert schema.missing_props(nodes, {"Event"}) is None
    assert schema.BASIC_OFFSET.search("2020-10-27T06:00:00-0600") and not schema.BASIC_OFFSET.search("2020-10-27T06:00:00-06:00")


def test_schema_sitewide_checks():
    import datetime as dt
    home = {"blocks": [{"@graph": [
        {"@type": ["Museum"], "@id": "o", "description": "Library in Medora. Opens July 4, 2026.",
         "sameAs": ["https://x.com/a"],
         "openingHoursSpecification": [{"description": "Fall restaurant hours", "validFrom": "2026-09-14", "validThrough": "2026-11-30"}]},
        {"@type": "WebSite", "description": "Official site"}]}]}
    ctx = {"site": "https://www.trlibrary.com/", "tr_id": "https://www.trlibrary.com/tr/#person",
           "lib_wikipedia": "https://en.wikipedia.org/wiki/X", "lib_wikidata": "https://www.wikidata.org/wiki/Q1",
           "tr_wikipedia": None, "tr_wikidata": "https://www.wikidata.org/wiki/Q33866"}
    extras = {"llms_status": 404, "node_urls": 0, "node_examples": [], "video_view_in_sitemap": 5, "video_views_linked": 5,
              "website_og": 0, "dangling": {"https://www.trlibrary.com/tr/#person": ["/tr/a"] * 30}, "bad_dates": []}
    ids = [f["id"] for f in schema.sitewide_checks(home, ctx, dt.date(2026, 10, 22), extras)]
    assert {"stale_description", "sameas", "tr_entity", "mixed_hours", "admission", "llms_txt"} <= set(ids)
    assert "hours_gap" not in ids
    ids = [f["id"] for f in schema.sitewide_checks(home, ctx, dt.date(2026, 6, 1), extras)]
    assert "stale_description" not in ids and "hours_gap" in ids


def test_schema_llms_draft():
    pages = {"/visit": {"title": "Plan Your Visit", "description": "Hours and tickets"},
             "/tr/badlands": {"title": "Badlands", "description": ""}, "/privacy": {"title": "Privacy", "description": ""}}
    txt = schema.llms_draft("TRPL", "https://www.trlibrary.com/", "Summary.", pages)
    assert txt.startswith("# TRPL\n\n> Summary.")
    assert "- [Plan Your Visit](https://www.trlibrary.com/visit): Hours and tickets" in txt
    assert "/privacy" not in txt
