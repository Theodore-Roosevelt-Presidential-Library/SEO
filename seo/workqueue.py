"""Work queue: turn the audit, internal-link and structured-data findings
into tasks an AI assistant (or a person) can actually carry out.

The other jobs find problems. This one says, for each problem:
  * which pages, biggest Search Console audience first
  * who can fix it: the TRPL team in Drupal, or FiveJars (template/config)
  * how, step by step, in trlibrary.com's Drupal
  * how to tell it worked (the check the next weekly run makes)

It also bundles everything for one page into a single "page job", so an
assistant opens a page once and fixes its meta tags, headings, links and
markup together.

Built from JSON the other jobs already wrote (audit, links, schema, gsc,
changes). No API keys. Writes work_queue.json; the digest renders it.
"""
from __future__ import annotations

import math
from collections import defaultdict
from urllib.parse import urlparse

from . import common as C

TRPL = "TRPL (Drupal admin)"
FIVEJARS = "FiveJars (template or config)"

# How to make each kind of change on trlibrary.com. Written for an assistant
# with Drupal admin access (browser) or a person following along.
RECIPES = {
    "meta": "Edit the node (/node/NID/edit) > 'Customize meta tags'. Basic tags: Page title '<title> | [site:name]' "
            "(page part 60 characters or fewer) and Description (120-155 characters). Set Open Graph og:title/og:description "
            "and Twitter card title/description to match. Save with 'Save' (keeps the moderation state). If the save seems to do "
            "nothing, look for a validation error further down the form.",
    "h1_missing": "Open the page's Layout (/node/NID/layout). Make sure the top section shows the page title block (Content fields > "
                  "Title), which renders as the H1; or change the first heading in the top text block to Heading 1. Save layout.",
    "h1_multiple": "Open the Layout. Keep one H1 (normally the page title block). In any text block whose heading is set to "
                   "Heading 1, change it to Heading 2. Save layout.",
    "chain": "Configuration > Search and metadata > URL redirects: find the redirects for this address and point the first one straight "
             "at the final page. Update any links on the site that use the old address.",
    "canonical": "Edit the node > 'Customize meta tags' > Advanced > Canonical URL: clear it (Drupal then uses the page's own address) "
                 "or set it to the live page it should point to.",
    "headings": "Open the Layout. In the text blocks, change the heading levels so they step down one at a time (H2 under the page "
                "title, H3 under an H2). Headings used just for size should be styled text instead.",
    "deep": "Link to the page from its section's hub page or a related, well-visited page, so people (and crawlers) reach it in "
            "three or four clicks.",
    "alias": "Edit the node > URL alias: give it a readable path that fits its section; save. The /node/NID address keeps working "
             "and the sitemap will list the readable one. "
             "(The lasting fix is FiveJars keeping unaliased /node/ URLs out of the XML sitemap.)",
    "sitemap": "This sitemap URL redirects to another page. Edit the old node > XML sitemap > Inclusion: Excluded, or archive the "
               "node if it's retired (a 301 stays in place).",
    "thin": "Only for pages people find in Google. Add useful, verified copy from the page's own subject (what it is, why it "
            "matters, what to do next, links to related pages). Never invent facts; draft for review.",
    "link": "Open the source page's Layout. Edit the text block that contains the context sentence and turn the [[bracketed]] "
            "words into a link to the target path (relative, e.g. /tr/tr-shot). Don't write new sentences just to hold a link. "
            "Save the block, then Save layout.",
    "orphan": "Add 2-3 links to this page from the pages listed under 'link from' (each has the sentence and words to link).",
    "related": "These two pages cover the same subject without linking to each other. Add one natural link each way, "
               "in the paragraph where the shared subject comes up.",
    "duplicate_topic": "Two pages compete for one subject. Pick the stronger page (clicks, depth), move anything unique onto it, "
                       "then archive the other and add a 301 from its alias and /node/NID. Get approval first; draft before publishing.",
    "redirect": "Configuration > Search and metadata > URL redirects > Add redirect: From = broken path, To = target, 301. "
                "If Drupal warns the path looks valid, submit again. Bulk: import redirects.csv. Also fix the link on the source page "
                "when the target is known.",
    "via_redirect": "Edit the link on each source page so it points straight at the final address.",
    "schema_article": "Edit the node > 'Customize meta tags' > Schema.org Article: @type Article; headline = the page title; "
                      "description = the meta description; about = Theodore Roosevelt; author and publisher = the Library; "
                      "dateModified = [node:changed:html_datetime]. Don't paste raw JSON-LD into a text block (it's stripped).",
    "schema_person": "Edit the node > 'Customize meta tags' > Schema.org Person: name, description, image, and sameAs "
                     "(Wikipedia/Wikidata only when verified).",
    "schema_event": "Edit the node > 'Customize meta tags' > Schema.org Event: name, startDate/endDate (ISO 8601 with a colon in the "
                    "offset, e.g. 2026-12-04T18:00:00-06:00), location = the Library, offers (price, ticket URL) only from the page.",
    "striking": "Open the page and make it the best answer to that exact search: use the search's words in the title or a heading, "
                "answer it plainly in the first paragraph, add the specifics people want (facts already on the site), and link to it "
                "from 2-3 related pages. Don't rewrite a page that already ranks in the top 3 for its main search.",
    "outreach": "Read the page. If it's a list of things to do or a travel guide that names nearby attractions, find the author or the "
                "update/contact link and ask to be added, with a two-sentence blurb (what the Library is, why it's worth the stop, "
                "about 3 1/2 hours) and a photo. Draft the note for approval; nothing goes out without it.",
    "fanout": "These are the searches the assistants ran before answering a question where they left the Library out. Find the "
              "trlibrary.com page that should answer each one (or note that none does). Strengthen that page for the search: "
              "say it in the title or a heading and answer it in the first paragraph, with facts already on the site. If no page fits, "
              "propose one.",
    "global": "Sitewide (Global) meta tags: change them only through Configuration > Development > Configuration synchronization > "
              "Import > Single item (Simple configuration, metatag.metatag_defaults.global), then clear all caches. Never save the "
              "Global defaults form itself: it drops fields.",
    "fivejars": "Write it up as a Basecamp to-do for FiveJars: what's wrong, example URLs, the ready-to-paste JSON-LD or setting, "
                "and how to check it.",
}

# Audit issue code -> (owner, recipe, done-when, minimum Search Console impressions for a page to be listed in the markdown)
AUDIT = {
    "meta_missing":        (TRPL, "meta", "The page has a meta description of 120-155 characters", 0),
    "og_missing":          (TRPL, "meta", "og:title and og:description are present", 0),
    "title_duplicate":     (TRPL, "meta", "No other page has the same title", 0),
    "meta_duplicate":      (TRPL, "meta", "No other page has the same description", 0),
    "meta_too_short":      (TRPL, "meta", "Description is 120-155 characters", 0),
    "title_too_long":      (TRPL, "meta", "Page part of the title is 60 characters or fewer", 50),
    "title_too_short":     (TRPL, "meta", "Page part of the title is 15-60 characters and says what the page is", 50),
    "h1_missing":          (TRPL, "h1_missing", "Exactly one H1", 0),
    "h1_multiple":         (TRPL, "h1_multiple", "Exactly one H1", 0),
    "thin_content":        (TRPL, "thin", "150+ words of body text", 200),
    "unaliased_url":       (TRPL, "alias", "The sitemap lists a readable path instead of /node/NID", 0),
    "redirect_in_sitemap": (TRPL, "sitemap", "The sitemap no longer lists the redirecting URL", 0),
    "slow":                (FIVEJARS, "fivejars", "Responds in under 3 seconds", 0),
    "redirect_chain":      (TRPL, "chain", "The address redirects once, straight to the final page", 0),
    "canonical_conflict":  (TRPL, "canonical", "The canonical tag points to a live, indexable page (usually the page itself)", 0),
    "heading_skip":        (TRPL, "headings", "Heading levels step down one at a time", 50),
    "deep_page":           (TRPL, "deep", "The page is 4 or fewer clicks from the homepage", 50),
}
META_CODES = {k for k, v in AUDIT.items() if v[1] == "meta"}

# Schema content groups an editor can fill per node with the Schema.org Metatag fields on the node form.
PER_NODE_SCHEMA = {"tr_articles": "schema_article", "tr_people": "schema_article", "tr_speeches": "schema_article",
                   "staff": "schema_person", "trustees": "schema_person", "event": "schema_event"}
# Sitewide structured-data issues the TRPL team can fix through the Global meta tags.
SITEWIDE_TRPL = {"stale_description", "sameas", "mixed_hours"}

SEVERITY = {"high": 3, "medium": 2, "low": 1}


def _score(severity: str, audience: float) -> float:
    """Rank tasks: severity x reach. Reach is the Search Console impressions of the
    pages the task touches (log scale, so one huge page doesn't swamp everything)."""
    return SEVERITY.get(severity, 1) * (1 + math.log10(1 + max(audience, 0)))


def _path(u: str) -> str:
    p = urlparse(u or "").path
    return (p.rstrip("/") or "/") if p else (u or "")


def _template_page(path: str) -> str | None:
    """Pages whose title/description come from a template, not an editor."""
    if path.startswith("/video/view/"):
        return "Video pages take their title and description from YouTube data in a template"
    return None


def build() -> dict:
    apages = C.read_json("audit/pages.json", []) or []
    gsc = C.read_json("gsc/pages.json", []) or []
    lk = C.read_json("links.json") or {}
    sc = C.read_json("schema.json") or {}
    chg = C.read_json("changes.json") or {}

    imp = defaultdict(int)
    for r in gsc:
        imp[_path(r["page"])] += r.get("impressions", 0)
    held = {r["page"] for r in chg.get("watching", []) if r.get("held")}
    site_total = sum(imp.values())

    tasks: list[dict] = []
    jobs: dict = defaultdict(lambda: {"fixes": [], "links_to_add": [], "markup": None})

    # ---- 1. Audit issues ----
    by_code = defaultdict(list)
    for p in apages:
        if (p.get("status") or 200) >= 400:
            continue
        path = _path(p["url"])
        for code in p.get("issues", []):
            if code not in AUDIT:
                continue
            if (p.get("redirected") or p.get("noindex")) and code not in ("redirect_in_sitemap", "redirect_chain", "unaliased_url"):
                continue
            by_code[code].append((path, p))
    for code, rows in by_code.items():
        owner, recipe, done, min_imp = AUDIT[code]
        editor_rows, template_rows = [], []
        for path, p in rows:
            (template_rows if code in META_CODES and _template_page(path) else editor_rows).append((path, p))
        for group_rows, grp_owner, grp_recipe, note in (
                (editor_rows, owner, recipe, None),
                (template_rows, FIVEJARS, "fivejars", "Video pages: fix once in the video template")):
            if not group_rows:
                continue
            items = []
            for path, p in sorted(group_rows, key=lambda r: -imp.get(r[0], 0)):
                it = {"page": path, "impressions": imp.get(path, 0)}
                if code in META_CODES:
                    it["title"] = p.get("title")
                    it["title_length"] = p.get("title_core_length")
                    it["meta_description"] = p.get("meta_description")
                if code.endswith("_duplicate"):
                    it["same_as"] = [_path(u) for u in (p.get("duplicates") or {}).get(code, [])][:5]
                if code.startswith("h1"):
                    it["h1"] = p.get("h1")
                if code == "thin_content":
                    it["words"] = p.get("words")
                if code == "heading_skip":
                    it["skips"] = p.get("heading_skips")
                if code == "deep_page":
                    it["clicks"] = p.get("click_depth")
                if code == "canonical_conflict":
                    it["canonical"] = p.get("canonical")
                    it["problem"] = p.get("canonical_problem")
                if code == "redirect_chain":
                    it["hops"] = p.get("redirect_hops")
                    it["final"] = _path(p.get("final_url") or "")
                if path in held and code in META_CODES:
                    it["held"] = True
                items.append(it)
            label = C_ISSUE.get(code, code)
            tasks.append({
                "id": f"audit:{code}" + (":template" if grp_owner == FIVEJARS and code in META_CODES else ""),
                "area": "audit", "title": label + (f" ({note})" if note else ""), "owner": grp_owner,
                "severity": C_SEV.get(code, "low"), "count": len(items),
                "how": RECIPES[grp_recipe], "done_when": done,
                "min_impressions_to_list": min_imp, "pages": items,
                "impact": _score(C_SEV.get(code, "low"), sum(i["impressions"] for i in items[:25] if i["impressions"] >= min_imp)),
            })
            if grp_owner == TRPL:
                for it in items:
                    if it["impressions"] >= min_imp and not it.get("held"):
                        jobs[it["page"]]["fixes"].append({"issue": code, "label": label, "how": recipe})

    # ---- 2. Internal links ----
    sugg = lk.get("suggestions", [])
    by_source = defaultdict(list)
    for s in sugg:
        by_source[s["source"]].append(s)
    link_items = []
    for src, rows in sorted(by_source.items(), key=lambda kv: -sum(r["score"] for r in kv[1])):
        rows = sorted(rows, key=lambda r: -r["score"])[:6]
        link_items.append({"page": src, "impressions": imp.get(src, 0), "value": round(sum(r["score"] for r in rows), 1),
                           "links": [{"words": r["phrase"], "to": r["target"], "context": r["snippet"]} for r in rows]})
        for r in rows[:5]:
            jobs[src]["links_to_add"].append({"words": r["phrase"], "to": r["target"], "context": r["snippet"]})
    if link_items:
        tasks.append({"id": "links:add", "area": "internal_links", "title": "Add internal links where pages already mention each other",
                      "owner": TRPL, "severity": "medium", "count": sum(len(x["links"]) for x in link_items),
                      "how": RECIPES["link"], "done_when": "The link appears on the source page; the target's links-in count rises next week",
                      "pages": link_items, "impact": _score("medium", sum(x["impressions"] for x in link_items[:25]))})

    orph = []
    for o in sorted(lk.get("orphans", []), key=lambda o: -(o.get("impressions") or 0)):
        froms = [s for s in sugg if s["target"] == o["page"]]
        froms = sorted(froms, key=lambda r: -r["score"])[:3]
        orph.append({"page": o["page"], "title": o.get("title"), "impressions": o.get("impressions") or 0,
                     "link_from": [{"page": r["source"], "words": r["phrase"], "context": r["snippet"]} for r in froms]})
    if orph:
        tasks.append({"id": "links:orphans", "area": "internal_links", "title": "Pages nothing links to",
                      "owner": TRPL, "severity": "medium", "count": len(orph), "how": RECIPES["orphan"],
                      "done_when": "At least two pages link in", "pages": orph,
                      "impact": _score("medium", sum(x["impressions"] for x in orph[:25]))})

    rel = [{"page": r["a"], "other": r["b"], "a_title": r.get("a_title"), "b_title": r.get("b_title"),
            "similarity": r.get("similarity"), "impressions": imp.get(r["a"], 0) + imp.get(r["b"], 0)}
           for r in lk.get("related_unlinked", [])]
    if rel:
        tasks.append({"id": "links:related", "area": "internal_links", "title": "Related pages that don't link to each other",
                      "owner": TRPL, "severity": "low", "count": len(rel), "how": RECIPES["related"],
                      "done_when": "Each page links to the other", "pages": sorted(rel, key=lambda r: -r["impressions"]),
                      "impact": _score("low", sum(r["impressions"] for r in rel[:25]))})

    dup = []
    for t in lk.get("duplicate_topics", []):
        pg = t.get("pages", [])
        ims = [x or 0 for x in (t.get("impressions") or [imp.get(p, 0) for p in pg])]
        dup.append({"topic": t.get("name"), "page": pg[0] if pg else "", "pages": pg, "impressions_each": ims,
                    "impressions": sum(ims or [0])})
    if dup:
        tasks.append({"id": "links:duplicate_topics", "area": "internal_links", "title": "Same topic on two pages (merge or differentiate)",
                      "owner": TRPL, "severity": "medium", "count": len(dup), "how": RECIPES["duplicate_topic"],
                      "done_when": "One page per topic; the other 301s to it", "needs_approval": True,
                      "pages": sorted(dup, key=lambda r: -r["impressions"]),
                      "impact": _score("medium", sum(r["impressions"] for r in dup[:10]))})

    broken = lk.get("broken_internal", [])
    if broken:
        tasks.append({"id": "links:broken", "area": "internal_links", "title": "Broken internal addresses: add 301 redirects",
                      "owner": TRPL, "severity": "high", "count": len(broken), "how": RECIPES["redirect"],
                      "done_when": "The old address returns 301 to the target",
                      "pages": [{"page": b["broken"], "redirect_to": b.get("redirect_to"), "confidence": b.get("confidence"),
                                 "why": b.get("why"), "linked_from": [s["page"] for s in b.get("sources", [])[:5]],
                                 "impressions": imp.get(_path(b["broken"]), 0)} for b in broken],
                      "impact": _score("high", sum(imp.get(s["page"], 0) for b in broken for s in b.get("sources", [])))})
    via = lk.get("links_through_redirects", [])
    if via:
        tasks.append({"id": "links:via_redirect", "area": "internal_links", "title": "Links that go through a redirect",
                      "owner": TRPL, "severity": "low", "count": len(via), "how": RECIPES["via_redirect"],
                      "done_when": "Links point at the final address",
                      "pages": [{"page": v["link"], "goes_to": v["goes_to"], "linked_from": v.get("sources", [])[:8], "impressions": 0}
                                for v in via], "impact": _score("low", sum(imp.get(x, 0) for v in via for x in v.get("sources", [])))})

    # ---- 2b. Search opportunities (Search Console) ----
    opp = C.read_json("opportunities.json") or {}
    sd = [r for r in opp.get("striking_distance", []) if _path(r["page"]) not in held][:30]
    if sd:
        tasks.append({"id": "search:striking_distance", "area": "search",
                      "title": "Strengthen pages ranking just off the top for searches people make",
                      "owner": TRPL, "severity": "medium", "count": len(sd), "how": RECIPES["striking"],
                      "done_when": "Average position for the search improves over the next 4 weeks (change log before/after)",
                      "pages": [{"page": _path(r["page"]), "impressions": r["impressions"], "search": r["query"],
                                 "position": r["position"], "mechanism": r.get("mechanism"), "upside": r.get("est_extra_clicks")}
                                for r in sd],
                      "impact": _score("medium", sum(r["impressions"] for r in sd[:25]))})
    low = [r for r in opp.get("low_ctr", []) if _path(r["page"]) not in held][:20]
    if low:
        tasks.append({"id": "search:low_ctr", "area": "search", "title": "Pages ranking well that people skip: rewrite title and description",
                      "owner": TRPL, "severity": "medium", "count": len(low), "how": RECIPES["meta"],
                      "done_when": "Click-through rate rises at the same position (change log before/after)",
                      "pages": [{"page": _path(r["page"]), "impressions": r["impressions"], "position": r["position"],
                                 "ctr": r.get("ctr"), "mechanism": r.get("mechanism"), "upside": r.get("est_extra_clicks")}
                                for r in low],
                      "impact": _score("medium", sum(r["impressions"] for r in low[:25]))})

    # ---- 3. AI visibility: where assistants look, and lists that leave the Library out ----
    ai = C.read_json("ai/latest.json") or {}
    gs = ai.get("gap_sources") or {}
    targets = gs.get("add_us_targets") or []
    if targets:
        tasks.append({"id": "ai:ask_to_be_added", "area": "ai_visibility", "title": "Get onto pages AI cites that leave the Library out",
                      "owner": TRPL, "severity": "medium", "count": len(targets), "how": RECIPES["outreach"],
                      "done_when": "The page names the Library (next weekly run re-reads it)",
                      "pages": [{"page": t["url"], "impressions": 0, "type": t["type"], "answers": t["answers"],
                                 "named": t.get("attractions_named")} for t in targets],
                      "impact": _score("medium", 5000 * sum(t["answers"] for t in targets))})
    fo = [x for x in (ai.get("fanout") or {}).get("searches", []) if x.get("in_gap_answers")
          and (not x.get("google") or (x["google"].get("position") or 99) > 10)]
    if fo:
        tasks.append({"id": "ai:searches_we_miss", "area": "ai_visibility",
                      "title": "Searches AI assistants run where trlibrary.com isn't on page one",
                      "owner": TRPL, "severity": "medium", "count": len(fo), "how": RECIPES["fanout"],
                      "done_when": "trlibrary.com ranks top 10 for the search (Search Console) and the next AI run cites it",
                      "pages": [{"page": x["search"], "impressions": (x.get("google") or {}).get("impressions") or 0,
                                 "google": x.get("google"), "engines": x["engines"], "questions": x["questions"][:2]} for x in fo[:40]],
                      "impact": _score("medium", 3000 * sum(x["in_gap_answers"] for x in fo[:20]))})

    # ---- 4. Structured data ----
    for f in sc.get("sitewide", []):
        if f["id"] == "node_urls":  # same fix as the audit's unaliased_url task
            continue
        own = TRPL if f["id"] in SITEWIDE_TRPL else FIVEJARS
        tasks.append({"id": f"schema:sitewide:{f['id']}", "area": "structured_data", "title": f["title"], "owner": own,
                      "severity": f.get("severity", "medium"), "count": 1,
                      "how": (f.get("fix") or "") + " " + RECIPES["global" if own == TRPL else "fivejars"]
                             + (" The Global Organization fields have no containsPlace: TRPL can trim the hours to museum hours only; "
                                "the Restaurant and Store entities need FiveJars." if f["id"] == "mixed_hours" else ""),
                      "snippet": f.get("snippet"), "detail": f.get("detail"),
                      "done_when": "The issue no longer appears in schema.json after the next weekly run",
                      "pages": [], "impact": _score(f.get("severity", "medium"), site_total)})
    for g in sc.get("groups", []):
        missing = [i["path"] for i in g.get("items", []) if not i.get("done")]
        incomplete = g.get("incomplete", 0)
        if not missing and not incomplete:
            continue
        rows = sorted(({"page": p, "impressions": imp.get(p, 0)} for p in missing), key=lambda r: -r["impressions"])
        ex = g.get("example") or {}
        base = {"area": "structured_data", "severity": "medium", "count": len(missing) or incomplete,
                "example_page": ex.get("path"), "example_jsonld": ex.get("jsonld"),
                "missing_properties": g.get("property_gaps") or {},
                "done_when": f"Pages carry {g['schema_type']} markup (schema.json '{g['label']}' shows them as done)"}
        tasks.append({**base, "id": f"schema:{g['key']}", "title": f"{g['label']}: add {g['schema_type']} markup (template, all pages at once)",
                      "owner": FIVEJARS, "how": g.get("drupal", "") + " " + RECIPES["fivejars"], "pages": rows,
                      "impact": _score("medium", sum(r["impressions"] for r in rows[:25]))})
        field = PER_NODE_SCHEMA.get(g["key"])
        if field and rows:
            top = [r for r in rows if r["impressions"] > 0][:15]
            if top:
                tasks.append({**base, "id": f"schema:{g['key']}:per_node", "title": f"{g['label']}: fill {g['schema_type']} on the busiest pages now (per page, until the template lands)",
                              "owner": TRPL, "how": RECIPES[field], "count": len(top), "pages": top,
                              "impact": _score("medium", sum(r["impressions"] for r in top)) + 0.5})
                for r in top:
                    jobs[r["page"]]["markup"] = {"type": g["schema_type"], "how": field}

    if not ((C.config().get("indexnow") or {}).get("key")):
        tasks.append({"id": "setup:indexnow", "area": "audit", "title": "Turn on IndexNow so Bing and Copilot see changes within hours",
                      "owner": FIVEJARS, "severity": "medium", "count": 1,
                      "how": "Ask FiveJars to install and enable the Drupal IndexNow module (it pings Bing, Yandex and others whenever "
                             "a node is saved) or to serve a key file at https://www.trlibrary.com/<key>.txt. Then put the key in "
                             "config/site.yml (indexnow.key) so the SEO tool also submits pages logged in changes.yml. "
                             + RECIPES["fivejars"],
                      "done_when": "The key file is live and the daily run reports 'Submitted N changed page(s)'",
                      "pages": [], "impact": _score("medium", site_total) * 0.6})
    wq = (C.config().get("work_queue") or {})
    ticketed, skip = set(wq.get("ticketed") or []), set(wq.get("skip") or [])
    blocked = wq.get("blocked") or {}
    tasks = [t for t in tasks if t["id"] not in skip]
    for t in tasks:
        if t["id"] in blocked:
            t["status"], t["blocked_by"] = "blocked", blocked[t["id"]]
        else:
            t["status"] = "with FiveJars" if t["id"] in ticketed else ("needs approval" if t.get("needs_approval") else "to do")
    tasks.sort(key=lambda t: (t["status"] in ("with FiveJars", "blocked"), -t["impact"]))
    for i, t in enumerate(tasks, 1):
        t["rank"] = i
        t["impact"] = round(t["impact"], 1)

    for t in tasks:
        t["reach"] = sum(p.get("impressions") or 0 for p in t["pages"][:25]) if t["pages"] else None
    moves, what_else = pick_moves(tasks)

    page_jobs = []
    for page, j in jobs.items():
        n = len(j["fixes"]) + len(j["links_to_add"]) + (1 if j["markup"] else 0)
        if n and imp.get(page, 0) > 0:
            page_jobs.append({"page": page, "impressions": imp.get(page, 0), "held": page in held, **j})
    page_jobs.sort(key=lambda r: -r["impressions"])

    by_owner = defaultdict(int)
    for t in tasks:
        by_owner[t["owner"]] += 1
    return {
        "generated": C.now_iso(),
        "summary": {"tasks": len(tasks), "by_owner": dict(by_owner),
                    "by_area": {a: sum(1 for t in tasks if t["area"] == a) for a in ("search", "audit", "internal_links", "structured_data", "ai_visibility")},
                    "page_jobs": len(page_jobs), "held_pages": len(held)},
        "moves": moves,
        "what_else": what_else,
        "workflow": WORKFLOW,
        "recipes": RECIPES,
        "tasks": tasks,
        "page_jobs": page_jobs[:60],
    }


def _item_text(t: dict, p: dict) -> str:
    if p.get("search"):
        return f"{p['page']} for \"{p['search']}\" (#{p.get('position')}, {p.get('mechanism') or ''})"
    if p.get("engines"):
        return f"\"{p['page']}\" (run by {', '.join(p['engines'])})"
    return p.get("page") or ""


def pick_moves(tasks: list[dict], n: int = 3) -> tuple[list[dict], list[dict]]:
    """Research broadly, recommend selectively: the top open task from up to three
    different areas becomes 'this week's moves'; the next few get a one-line reason
    they didn't make the cut."""
    moves, areas = [], set()
    for t in tasks:
        if t["status"] != "to do" or t["owner"] != TRPL or t["area"] in areas:
            continue
        areas.add(t["area"])
        moves.append({"task": t["id"], "rank": t["rank"], "area": t["area"], "title": t["title"],
                      "start_with": [_item_text(t, p) for p in t["pages"][:3]] or [t.get("detail") or "one sitewide change (see How)"],
                      "why": f"{t['severity']} priority; " + (f"pages involved get {t['reach']:,} Google impressions (28 days)"
                                                               if t.get("reach") else "affects the whole site"),
                      "how": t["how"], "done_when": t["done_when"]})
        if len(moves) == n:
            break
    floor = min((t["reach"] for t in tasks if t["id"] in {m["task"] for m in moves} and t.get("reach")), default=None)
    what_else = []
    for t in tasks:
        if t["id"] in {m["task"] for m in moves}:
            continue
        if t["status"] == "with FiveJars":
            why = "already with FiveJars; check whether it has landed"
        elif t["status"] == "blocked":
            why = "blocked: " + t.get("blocked_by", "")
        elif t["status"] == "needs approval":
            why = "needs a decision first (merge or archive)"
        elif t["owner"] != TRPL:
            why = "FiveJars work; send as a ticket"
        elif t["area"] in areas:
            why = f"same area as a move this week ({t['area'].replace('_', ' ')}); next in line"
        else:
            why = (f"smaller reach ({(t.get('reach') or 0):,} Google impressions vs {floor:,} for this week's moves)" if floor
                   else "lower priority than this week's moves")
        what_else.append({"task": t["id"], "title": t["title"], "why_not_now": why})
        if len(what_else) == 8:
            break
    return moves, what_else


WORKFLOW = [
    "Pick tasks from the top of the queue (or a page job, to do everything on one page at once). Pages marked held changed recently and are being measured: leave their titles, descriptions and copy alone (adding markup or links to them is fine).",
    "Write the exact change: new title/description, the sentence with the link, the markup fields, the redirect. Use only facts already on the page.",
    "Get approval from the communications team before changing the live site. Merges, archiving and anything sitewide always need approval.",
    "If you have Drupal admin access, make TRPL-owned changes yourself using the recipe. Content changes to a page can be saved as a draft first.",
    "For FiveJars-owned tasks, write a Basecamp to-do: what's wrong, example URLs, the ready-to-paste JSON-LD or setting, how to check.",
    "Check the live page afterwards (view source for meta tags and JSON-LD; follow redirects with curl).",
    "Log each change in config/changes.yml (date, page, kind, what) so the next run holds the page and reports before/after numbers.",
]

C_SEV: dict = {}
C_ISSUE: dict = {}
try:  # labels and severities from the audit job
    from .audit import ISSUE_TEXT as _IT
    C_SEV.update({k: v[0] for k, v in _IT.items()})
    C_ISSUE.update({k: v[1] for k, v in _IT.items()})
except Exception:  # pragma: no cover
    pass


def run() -> dict:
    q = build()
    C.write_json("work_queue.json", q)
    return q
