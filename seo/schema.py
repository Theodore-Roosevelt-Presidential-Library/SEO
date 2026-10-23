"""Structured data: schema.org markup that helps search engines and AI tools
understand what each page is.

Weekly. No API key needed.

1. Read every sitemap page and note the schema.org types it already carries
   (beyond the sitewide Museum/WebSite block and breadcrumbs every page has).
2. Sort pages into content types (FAQ, event, podcast episode, press release,
   staff profile, TR history article, itinerary, video playlist...) and say
   which schema.org type each should carry. Most fixes belong in one Drupal
   template per content type, so results are grouped that way.
3. For each content type, write ready-to-paste JSON-LD built from a real page.
   FAQ markup is written in full for every page, since the questions differ.
4. Check the sitewide block for things AI tools repeat or rely on: stale
   wording ("opens July 4, 2026"), Wikipedia/Wikidata links, current opening
   hours, admission info, and whether trlibrary.com has an llms.txt (drafts one).

Writes schema.json and site-llms.txt (a draft llms.txt for www.trlibrary.com).
"""
from __future__ import annotations

import datetime as dt
import json
import re
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from . import common as C

# Types every page carries from the sitewide block. A page only "has
# structured data of its own" when it carries something beyond these.
SITEWIDE = {"Museum", "Library", "TouristAttraction", "WebSite", "BreadcrumbList", "ListItem",
            "ImageObject", "OpeningHoursSpecification", "PostalAddress", "GeoCoordinates",
            "SearchAction", "EntryPoint", "Organization"}
ICON_WORDS = re.compile(r"^(keyboard_arrow_\w+|expand_\w+|add|remove|chevron_\w+)\s*")
TODO = "TODO: "


def path_of(url: str) -> str:
    return urlparse(url).path.rstrip("/") or "/"


def iso(ts: str | None) -> str | None:
    """'2025-08-29T02:04:54-0600' -> '2025-08-29T02:04:54-06:00'."""
    if not ts:
        return None
    return re.sub(r"([+-]\d{2})(\d{2})$", r"\1:\2", ts.strip())


def jsonld_types(obj) -> set[str]:
    out = set()
    if isinstance(obj, dict):
        t = obj.get("@type")
        out |= set(t) if isinstance(t, list) else ({t} if t else set())
        for v in obj.values():
            out |= jsonld_types(v)
    elif isinstance(obj, list):
        for v in obj:
            out |= jsonld_types(v)
    return out


def all_nodes(obj) -> list[dict]:
    """Every JSON-LD object (dict with @type or @id), however deeply nested."""
    out = []
    if isinstance(obj, dict):
        if "@type" in obj or "@id" in obj:
            out.append(obj)
        for v in obj.values():
            out += all_nodes(v)
    elif isinstance(obj, list):
        for v in obj:
            out += all_nodes(v)
    return out


def type_set(node: dict) -> set:
    t = node.get("@type")
    return set(t) if isinstance(t, list) else ({t} if t else set())


# Properties each type needs to be useful (Google's required/recommended set, trimmed).
NEEDS = {
    "Event": ["name", "startDate", "location", "description", "image", "offers", "organizer"],
    "NewsArticle": ["headline", "datePublished", "author", "publisher", "image"],
    "Article": ["headline", "datePublished", "dateModified", "author", "publisher", "image", "about"],
    "PodcastEpisode": ["name", "datePublished", "partOfSeries", "associatedMedia", "description"],
    "Person": ["name", "image"],
    "ProfilePage": ["mainEntity"],
    "FAQPage": ["mainEntity"],
    "TouristTrip": ["name", "description", "itinerary"],
    "CollectionPage": ["name", "about"],
    "VideoObject": ["name", "thumbnailUrl", "uploadDate", "description", "embedUrl"],
    "ItemList": ["itemListElement"],
}
DATE_KEYS = ("startDate", "endDate", "datePublished", "dateModified", "uploadDate")
BASIC_OFFSET = re.compile(r"T\d{2}:\d{2}(:\d{2})?[+-]\d{4}$")


def missing_props(nodes: list[dict], expect: set) -> list[str] | None:
    """Properties missing from the best node of an expected type (None if no such node)."""
    best = None
    for n in nodes:
        hit = type_set(n) & expect
        if not hit:
            continue
        need = NEEDS.get(sorted(hit)[0], [])
        if sorted(hit)[0] == "Person" and n.get("worksFor") is None and n.get("memberOf") is None:
            need = need + ["worksFor/memberOf"]
        miss = [k for k in need if not n.get(k)]
        if best is None or len(miss) < len(best):
            best = miss
    return best


def clean(text: str, limit: int = 0) -> str:
    t = re.sub(r"\s+", " ", text or "").strip()
    return (t[: limit - 1].rsplit(" ", 1)[0] + "…") if limit and len(t) > limit else t


# ---------- page extraction ----------

def extract(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "lxml")
    blocks = []
    for s in soup.find_all("script", type="application/ld+json"):
        try:
            blocks.append(json.loads(s.string or ""))
        except (json.JSONDecodeError, TypeError):
            blocks.append({"@type": "INVALID"})
    meta = {}
    for m in soup.find_all("meta"):
        k = m.get("property") or m.get("name")
        if k and m.get("content"):
            meta.setdefault(k, m["content"])
    main = soup.find("main") or soup.body or soup
    h1 = main.find("h1")

    faq = []
    for acc in main.select("[data-custom-accordion]"):
        btn = acc.select_one("[data-custom-accordion-button]")
        body = acc.select_one("[data-custom-accordion-body]")
        if btn and body:
            q = clean(ICON_WORDS.sub("", clean(btn.get_text(" "))))
            a = clean(body.get_text(" "))
            if q.endswith("?") and a:
                faq.append((q, a))
    for d in main.find_all("details"):
        s = d.find("summary")
        if s:
            q = clean(s.get_text(" "))
            s.extract()
            a = clean(d.get_text(" "))
            if q.endswith("?") and a:
                faq.append((q, a))
    faq = list(dict.fromkeys(faq))

    videos = []
    for a in main.find_all("a", href=re.compile(r"/video/view/[\w-]{11}")):
        vid = re.search(r"/video/view/([\w-]{11})", a["href"]).group(1)
        title = clean(a.get_text(" "))
        if title and vid not in {v[0] for v in videos}:
            videos.append((vid, title))

    headings = [clean(h.get_text(" ")) for h in main.find_all(["h2", "h3"])]
    nodes = all_nodes(blocks)
    return {
        "nodes": nodes,
        "defined_ids": sorted({n["@id"] for n in nodes if n.get("@id") and set(n) - {"@id", "@type", "@context"}}),
        "stub_ids": sorted({n["@id"] for n in nodes if n.get("@id") and not set(n) - {"@id", "@type", "@context"}}),
        "url": url,
        "types": sorted(jsonld_types(blocks)),
        "blocks": blocks,
        "title": clean(meta.get("og:title") or (h1.get_text(" ") if h1 else "") or (soup.title.string if soup.title else "")),
        "h1": clean(h1.get_text(" ")) if h1 else "",
        "description": clean(meta.get("description") or meta.get("og:description") or ""),
        "image": meta.get("og:image"),
        "og_type": meta.get("og:type"),
        "modified": iso(meta.get("og:updated_time") or meta.get("article:modified_time")),
        "published": iso(meta.get("article:published_time")),
        "times": [t["datetime"] for t in main.find_all("time", datetime=True)
                  if re.match(r"\d{4}-\d{2}-\d{2}", t["datetime"])],
        "simplecast": next((f["src"].split("?")[0] for f in soup.find_all("iframe", src=True)
                            if "simplecast.com" in f["src"]), None),
        "faq": faq,
        "videos": videos,
        "headings": [h for h in headings if 3 < len(h) < 90],
    }


# ---------- JSON-LD builders (one per content type) ----------

def _base(p: dict, typ: str, org: str, name_key: str = "name") -> dict:
    d = {"@context": "https://schema.org", "@type": typ, "@id": p["url"] + "#main", name_key: p["title"],
         "url": p["url"]}
    if p["description"]:
        d["description"] = p["description"]
    if p["image"] and "metatags/logo" not in p["image"]:
        d["image"] = p["image"]
    return d


def build_faq(p, ctx):
    return {"@context": "https://schema.org", "@type": "FAQPage", "@id": p["url"] + "#faq", "url": p["url"],
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": clean(a, 1200)}} for q, a in p["faq"]]}


def build_event(p, ctx):
    d = _base(p, "Event", ctx["org"])
    d["startDate"] = p["times"][0] if p["times"] else TODO + "start date and time, e.g. 2026-11-14T10:00:00-07:00"
    if len(p["times"]) > 1:
        d["endDate"] = p["times"][1]
    d.update({"eventStatus": "https://schema.org/EventScheduled",
              "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
              "location": {"@id": ctx["org"]}, "organizer": {"@id": ctx["org"]},
              "offers": {"@type": "Offer", "url": TODO + "ticket link", "price": TODO + "price, 0 if free",
                         "priceCurrency": "USD", "availability": "https://schema.org/InStock"}})
    return d


def build_episode(p, ctx):
    d = _base(p, "PodcastEpisode", ctx["org"])
    d["partOfSeries"] = {"@type": "PodcastSeries", "name": ctx["podcast_name"], "url": ctx["podcast_url"]}
    d["datePublished"] = p["published"] or TODO + "release date, e.g. 2025-05-28"
    if p["simplecast"]:
        d["associatedMedia"] = {"@type": "MediaObject", "embedUrl": p["simplecast"]}
    d["publisher"] = {"@id": ctx["org"]}
    return d


def build_series(p, ctx):
    d = _base(p, "PodcastSeries", ctx["org"])
    d["publisher"] = {"@id": ctx["org"]}
    return d


def build_news(p, ctx):
    d = _base(p, "NewsArticle", ctx["org"], "headline")
    d["datePublished"] = p["published"] or TODO + "release date"
    if p["modified"]:
        d["dateModified"] = p["modified"]
    d["author"] = {"@id": ctx["org"]}
    d["publisher"] = {"@id": ctx["org"]}
    return d


JOB = re.compile(r"\bis (?:the |a |an )?(.{3,80}?) (?:at|of|for) the Theodore Roosevelt", re.I)


def build_person(p, ctx, trustee=False):
    person = {"@type": "Person", "name": p["h1"] or p["title"]}
    if p["image"] and "metatags/logo" not in p["image"]:
        person["image"] = p["image"]
    if trustee:
        person["memberOf"] = {"@type": "OrganizationRole", "roleName": "Trustee",
                              "memberOf": {"@id": ctx["org"]}}
    else:
        m = JOB.search(p["description"])
        person["jobTitle"] = m.group(1) if m else TODO + "job title"
        person["worksFor"] = {"@id": ctx["org"]}
    if p["description"]:
        person["description"] = p["description"]
    return {"@context": "https://schema.org", "@type": "ProfilePage", "@id": p["url"] + "#main",
            "url": p["url"], "mainEntity": person}


def build_trustee(p, ctx):
    return build_person(p, ctx, trustee=True)


def build_article(p, ctx, about=None):
    d = _base(p, "Article", ctx["org"], "headline")
    if p["modified"]:
        d["dateModified"] = p["modified"]
    d["author"] = {"@id": ctx["org"]}
    d["publisher"] = {"@id": ctx["org"]}
    d["about"] = about or {"@id": ctx["tr_id"]}
    d["isPartOf"] = {"@id": ctx["site_id"]}
    return d


def build_tr_person(p, ctx):
    name = re.split(r"\s*(?::|\s[–—-]\s)\s*", p["h1"] or p["title"])[0]
    return build_article(p, ctx, about={"@type": "Person", "name": name,
                                        "sameAs": [TODO + f"Wikipedia and Wikidata links for {name}"]})


def build_speech(p, ctx):
    return build_article(p, ctx, about={"@type": "CreativeWork", "name": p["h1"] or p["title"],
                                        "author": {"@id": ctx["tr_id"]}})


def build_hub(p, ctx):
    d = _base(p, "CollectionPage", ctx["org"])
    d["about"] = {"@id": ctx["tr_id"]}
    d["isPartOf"] = {"@id": ctx["site_id"]}
    return d


def build_trip(p, ctx):
    d = _base(p, "TouristTrip", ctx["org"])
    d["provider"] = {"@id": ctx["org"]}
    stops = [h for h in p["headings"] if not re.search(r"\b(plan|tips?|share|related|more|faq|print)\b", h, re.I)][:15]
    if stops:
        d["itinerary"] = {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "item": {"@type": "TouristDestination", "name": s}}
            for i, s in enumerate(stops)]}
    return d


def build_video(p, ctx):
    vid = p["url"].rstrip("/").rsplit("/", 1)[-1]
    d = _base(p, "VideoObject", ctx["org"])
    d.update({"thumbnailUrl": p["image"] or f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
              "embedUrl": f"https://www.youtube.com/embed/{vid}",
              "uploadDate": p["published"] or TODO + "YouTube publish date", "publisher": {"@id": ctx["org"]}})
    return d


def build_playlist(p, ctx):
    site = ctx["site"]
    return {"@context": "https://schema.org", "@type": "ItemList", "@id": p["url"] + "#videos",
            "name": p["h1"] or p["title"], "url": p["url"],
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": {
                "@type": "VideoObject", "name": t, "url": urljoin(site, f"/video/view/{v}"),
                "embedUrl": f"https://www.youtube.com/embed/{v}",
                "thumbnailUrl": f"https://i.ytimg.com/vi/{v}/hqdefault.jpg",
                "uploadDate": TODO + "YouTube publish date"}} for i, (v, t) in enumerate(p["videos"][:25])]}


# Content types, matched in order. "expect" = schema.org types that count as done.
GROUPS = [
    {"key": "event", "label": "Calendar events", "match": r"^/calendar/[^/]+/[^/]+$", "expect": {"Event"},
     "build": build_event, "why": "Lets Google and AI assistants answer 'what's happening at the Library this weekend' with the date, time and ticket link.",
     "drupal": "Add Event JSON-LD to the Event content type template, filled from the event's date, time, price and ticket fields. One template change covers every event."},
    {"key": "podcast_episode", "label": "Good Citizen episodes", "match": r"^/podcast/good-citizen/[^/]+$",
     "expect": {"PodcastEpisode"}, "build": build_episode,
     "why": "Ties each episode to the Good Citizen series and its guest so AI tools can cite the right episode.",
     "drupal": "Add PodcastEpisode JSON-LD to the podcast episode template (title, summary, release date, Simplecast player)."},
    {"key": "podcast_series", "label": "Good Citizen podcast page", "match": r"^/podcast(/good-citizen)?$",
     "expect": {"PodcastSeries"}, "build": build_series, "why": "Names the show as a podcast series.",
     "drupal": "Add PodcastSeries JSON-LD to the podcast landing page."},
    {"key": "press", "label": "Press releases", "match": r"^/(about/)?press/press-releases/.+", "expect": {"NewsArticle", "Article"},
     "build": build_news, "why": "Gives each release a publish date, so AI answers don't mix up old and new announcements.",
     "drupal": "Add NewsArticle JSON-LD to the press release template, using the release date field."},
    {"key": "staff", "label": "Staff profiles", "match": r"^/staff-members/[^/]+$", "expect": {"ProfilePage", "Person"},
     "build": build_person, "why": "Tells AI tools who holds which role at the Library.",
     "drupal": "Add ProfilePage + Person JSON-LD to the staff member template (name, job title, photo)."},
    {"key": "trustees", "label": "Trustee profiles", "match": r"^/about/trustees/[^/]+$", "expect": {"ProfilePage", "Person"},
     "build": build_trustee, "why": "Tells AI tools who sits on the Board.",
     "drupal": "Add ProfilePage + Person JSON-LD (role: Trustee) to the trustee template."},
    {"key": "tr_people", "label": "TR history: people", "match": r"^/tr/people/[^/]+$", "expect": {"Article"},
     "build": build_tr_person, "why": "Marks each page as an article about a specific person in TR's life, linked to their Wikipedia/Wikidata entry.",
     "drupal": "Add Article JSON-LD to the /tr people template, with an 'about' Person; a field for the person's Wikidata link makes it precise."},
    {"key": "tr_speeches", "label": "TR history: speeches", "match": r"^/tr/speeches/[^/]+$", "expect": {"Article"},
     "build": build_speech, "why": "Marks the page as being about a specific TR speech, authored by TR.",
     "drupal": "Add Article JSON-LD with an 'about' CreativeWork (the speech, author: Theodore Roosevelt)."},
    {"key": "tr_articles", "label": "TR history articles", "match": r"^/tr/[^/]+/.+", "expect": {"Article"},
     "build": build_article, "why": "The /tr section is the Library's richest content for AI answers. Article markup says who published it, when it was updated, and that it's about Theodore Roosevelt (linked to his Wikidata entry).",
     "drupal": "Add Article JSON-LD to the /tr article template with about = Theodore Roosevelt (the sitewide #theodore-roosevelt entity) and dateModified from the node's changed date."},
    {"key": "tr_hubs", "label": "TR history section pages", "match": r"^/tr(/[^/]+)?$", "expect": {"CollectionPage"},
     "build": build_hub, "why": "Marks the section pages as collections about TR.",
     "drupal": "Add CollectionPage JSON-LD to the /tr section landing template."},
    {"key": "itineraries", "label": "Trip itineraries", "match": r"^/visit/itineraries/[^/]+$", "expect": {"TouristTrip"},
     "build": build_trip, "why": "AI trip planners can pick up each itinerary as a ready-made route with its stops.",
     "drupal": "Add TouristTrip JSON-LD to the itinerary template, listing each stop. Check the drafted stop list: it's taken from the page headings."},
    {"key": "videos", "label": "Video pages", "match": r"^/video/view/[\w-]{11}$", "expect": {"VideoObject"},
     "build": build_video, "why": "Video markup lets search and AI tools show and cite the Library's videos, with title, length and date.",
     "drupal": "Add VideoObject JSON-LD to the video view template from the stored YouTube data (title, description, thumbnail, publish date, duration)."},
    {"key": "video_playlists", "label": "Video playlists", "match": r"^/video/playlist/.+", "expect": {"ItemList", "VideoObject"},
     "build": build_playlist, "why": "Each playlist page can list its videos so search and AI tools see them as videos, not just links.",
     "drupal": "Add ItemList of VideoObject JSON-LD to the playlist template. Drupal already stores each video's YouTube data, including its publish date (uploadDate)."},
]
FAQ_GROUP = {"key": "faq", "label": "Pages with Q&A", "expect": {"FAQPage"}, "build": build_faq,
             "why": "Questions and answers are exactly what AI tools quote. FAQ markup hands them the question and the Library's own answer, word for word.",
             "drupal": "Add FAQPage JSON-LD to the accordion paragraph type: when every item's title is a question, output each as Question/Answer. One template change covers every FAQ page."}


def classify(path: str, page: dict) -> list[dict]:
    out = [FAQ_GROUP] if len(page["faq"]) >= 2 else []
    for g in GROUPS:
        if re.search(g["match"], path):
            out.append(g)
            break
    return out


# ---------- sitewide checks ----------

def sitewide_checks(home: dict, ctx: dict, today: dt.date, extras: dict) -> list[dict]:
    out = []
    org = next((n for b in home["blocks"] for n in (b.get("@graph", [b]) if isinstance(b, dict) else [])
                if isinstance(n, dict) and "Museum" in (n.get("@type") if isinstance(n.get("@type"), list) else [n.get("@type")])), None)
    site = next((n for b in home["blocks"] for n in (b.get("@graph", [b]) if isinstance(b, dict) else [])
                 if isinstance(n, dict) and n.get("@type") == "WebSite"), None)
    if not org:
        return [{"id": "no_org", "severity": "high", "title": "No sitewide Museum/Organization markup found",
                 "detail": "The homepage carries no schema.org description of the Library.", "fix": "Restore the sitewide JSON-LD block."}]

    # stale "opens/opening <date>" wording
    stale = []
    for label, node in (("Library", org), ("Website", site or {})):
        desc = node.get("description", "")
        for m in re.finditer(r"\b(opens?|opening|will open)\b[^.]*?(\w+ \d{1,2}, \d{4})", desc, re.I):
            try:
                when = dt.datetime.strptime(m.group(2), "%B %d, %Y").date()
            except ValueError:
                continue
            if when <= today:
                stale.append(f"{label}: “{desc}”")
    if stale:
        out.append({"id": "stale_description", "severity": "high",
                    "title": "Sitewide description still says the Library is about to open",
                    "detail": " · ".join(stale),
                    "fix": "Update the description in the sitewide schema (Drupal Metatag/Schema settings) to present tense, "
                           "e.g. “Presidential library and museum in Medora, North Dakota, dedicated to the life, legacy, and ideals of Theodore Roosevelt. Opened July 4, 2026.” "
                           "AI tools copy this sentence into answers."})

    same = " ".join(org.get("sameAs", []) or [])
    missing = [n for n, pat in (("Wikipedia", "wikipedia.org"), ("Wikidata", "wikidata.org")) if pat not in same]
    if missing:
        add = [u for u in (ctx["lib_wikipedia"], ctx["lib_wikidata"]) if u and
               (("wikipedia" in u and "Wikipedia" in missing) or ("wikidata" in u and "Wikidata" in missing))]
        out.append({"id": "sameas", "severity": "high",
                    "title": f"Sitewide markup doesn't link to the Library's {' or '.join(missing)} entry",
                    "detail": "sameAs lists only social accounts. Wikipedia and Wikidata links are how search engines and AI tools "
                              "confirm that trlibrary.com is the same Theodore Roosevelt Presidential Library they know about.",
                    "fix": "Add these to sameAs in the sitewide schema.",
                    "snippet": {"sameAs": add}})

    for ref, ps in sorted(extras.get("dangling", {}).items(), key=lambda x: -len(x[1])):
        is_tr = ref == ctx["tr_id"]
        out.append({"id": "tr_entity" if is_tr else "dangling",
                    "severity": "high" if is_tr and len(ps) > 20 else "medium",
                    "title": (f"{len(ps)} pages point to a Theodore Roosevelt entity that is never defined" if is_tr
                              else f"{len(ps)} pages point to {ref}, which is never defined"),
                    "detail": (f"Every /tr page says it's about {ref}, but no page says who that is: no name, no Wikidata link. "
                               "To a machine it's an empty placeholder, so the link to the real Theodore Roosevelt is lost."
                               if is_tr else "The markup references this entity by @id, but no page gives it a name or details."),
                    "fix": ("Define the entity once in the sitewide @graph (so every page carries it). This is the single "
                            "highest-value change for the /tr section." if is_tr else "Define the entity where it's referenced."),
                    "snippet": ({"@type": "Person", "@id": ref, "name": "Theodore Roosevelt",
                                 "alternateName": ["TR", "Teddy Roosevelt"], "birthDate": "1858-10-27", "deathDate": "1919-01-06",
                                 "jobTitle": "26th President of the United States",
                                 "sameAs": [u for u in (ctx["tr_wikipedia"], ctx["tr_wikidata"]) if u]} if is_tr else None),
                    "examples": ps[:5]})
    if extras.get("bad_dates"):
        bd = extras["bad_dates"]
        kinds = sorted({k for _, k, _ in bd})
        out.append({"id": "date_format", "severity": "low",
                    "title": f"{len({p for p, _, _ in bd})} pages have dates without a colon in the time zone",
                    "detail": f"For example {bd[0][1]} \u201c{bd[0][2]}\u201d on {bd[0][0]}. Strict ISO 8601 wants \u201c-06:00\u201d, "
                              "and some validators reject the short form.",
                    "fix": f"In the Drupal schema templates, format {', '.join(kinds)} with the PHP date format \u201cc\u201d "
                           "(e.g. 2020-10-27T06:00:00-06:00)."})
    hours = org.get("openingHoursSpecification", []) or []
    covered = False
    for h in hours:
        try:
            if dt.date.fromisoformat(h.get("validFrom", "1900-01-01")) <= today <= dt.date.fromisoformat(h.get("validThrough", "2999-12-31")):
                covered = True
        except ValueError:
            continue
    if hours and not covered:
        out.append({"id": "hours_gap", "severity": "high", "title": "No opening hours in the markup cover today",
                    "detail": f"None of the {len(hours)} hours entries is valid for {today.isoformat()}.",
                    "fix": "Add the current season's hours to the sitewide schema."})
    mixed = sorted({w for h in hours for w in ("restaurant", "store", "shop", "café", "cafe")
                    if w in (h.get("description") or "").lower()})
    if mixed:
        out.append({"id": "mixed_hours", "severity": "medium",
                    "title": "Restaurant and store hours are listed as the museum's hours",
                    "detail": f"The museum entity carries {len(hours)} hours entries, including {', '.join(mixed)} hours. "
                              "Machines can't tell which hours mean the museum is open.",
                    "fix": "Keep only museum hours on the Library entity. Give the restaurant and the store their own entities "
                           "(Restaurant, Store) with their hours, linked with containsPlace.",
                    "snippet": {"containsPlace": [{"@type": "Restaurant", "name": TODO + "restaurant name",
                                                   "servesCuisine": TODO + "cuisine", "openingHoursSpecification": TODO + "restaurant hours"},
                                                  {"@type": "Store", "name": TODO + "store name",
                                                   "openingHoursSpecification": TODO + "store hours"}]}})
    if not any(k in org for k in ("offers", "makesOffer", "priceRange", "isAccessibleForFree")):
        out.append({"id": "admission", "severity": "medium", "title": "No admission information in the markup",
                    "detail": "“How much are tickets?” is one of the most common visitor questions. The markup has no price or ticket link.",
                    "fix": "Add admission offers (and isAccessibleForFree: false) to the Library entity.",
                    "snippet": {"isAccessibleForFree": False, "publicAccess": True,
                                "makesOffer": [{"@type": "Offer", "name": "General admission", "price": TODO + "adult price",
                                                "priceCurrency": "USD", "url": urljoin(ctx["site"], "/visit/tickets")}]}})
    if extras["llms_status"] != 200:
        out.append({"id": "llms_txt", "severity": "high", "title": "www.trlibrary.com has no llms.txt",
                    "detail": "llms.txt is a plain-text guide that tells AI tools what the site covers and which pages matter. "
                              "A draft built from the sitemap is attached.",
                    "fix": "Review the draft, then ask FiveJars to serve it at https://www.trlibrary.com/llms.txt.",
                    "file": "data/site-llms.txt"})
    if extras["node_urls"]:
        out.append({"id": "node_urls", "severity": "medium",
                    "title": f"{extras['node_urls']} unaliased /node/ URLs are in the sitemap",
                    "detail": "These are duplicate addresses for pages that have proper URLs (or old, unpublished-looking items). "
                              "They waste crawler time and split signals between two addresses.",
                    "fix": "Ask FiveJars to leave unaliased /node/ URLs out of the XML sitemap.",
                    "examples": extras["node_examples"]})
    if extras["video_view_in_sitemap"] == 0 and extras["video_views_linked"]:
        out.append({"id": "video_sitemap", "severity": "medium",
                    "title": "Individual video pages aren't in the sitemap",
                    "detail": f"Playlist pages link to {extras['video_views_linked']} /video/view/ pages, but none are in the sitemap, "
                              "so search engines and AI crawlers may never find individual videos.",
                    "fix": "Add /video/view/ pages to the sitemap (or a video sitemap), each with VideoObject markup."})
    if extras["website_og"]:
        out.append({"id": "og_type", "severity": "low",
                    "title": f"{extras['website_og']} articles are labelled og:type “website”",
                    "detail": "Social and AI previews treat them as generic pages rather than articles.",
                    "fix": "Set og:type to “article” on /tr, press release and podcast templates (Drupal Metatag)."})
    order = {"high": 0, "medium": 1, "low": 2}
    return sorted(out, key=lambda f: order[f["severity"]])


# ---------- llms.txt draft ----------

LLMS_SECTIONS = [
    ("Plan a visit", r"^/visit(/|$)"), ("Theodore Roosevelt: life and legacy", r"^/tr(/|$)"),
    ("Good Citizen podcast", r"^/podcast(/|$)"), ("Calendar", r"^/calendar(/|$)"),
    ("Press", r"^/(about/)?press(/|$)"), ("About the Library", r"^/(about|support|membership|research)(/|$)"),
]


def llms_draft(site_name: str, site: str, summary: str, pages: dict, limit_per_section: int = 40) -> str:
    lines = [f"# {site_name}", "", f"> {summary}", "",
             "Official website of the Theodore Roosevelt Presidential Library in Medora, North Dakota: "
             "visitor information, the Library's history of Theodore Roosevelt, events, and the Good Citizen podcast.", ""]
    used = set()
    for label, pat in LLMS_SECTIONS:
        items = sorted((p for p in pages if re.search(pat, p) and p not in used), key=lambda p: (p.count("/"), p))
        if not items:
            continue
        lines += [f"## {label}", ""]
        for p in items[:limit_per_section]:
            d = pages[p]
            desc = clean(d["description"], 120)
            lines.append(f"- [{d['title'] or p}]({urljoin(site, p)})" + (f": {desc}" if desc else ""))
            used.add(p)
        lines.append("")
    lines += ["## Optional", "", f"- [Video library]({urljoin(site, '/video')}): talks, programs and short histories", ""]
    return "\n".join(lines)


# ---------- job ----------

def run() -> None:
    cfg = C.config()
    sd = cfg.get("structured_data", {}) or {}
    site = cfg["site"]["url"].rstrip("/") + "/"
    skip = [re.compile(p) for p in sd.get("skip_patterns", ["/print$", "/quiz/", "/search"])]
    ent = sd.get("entities", {}) or {}
    ctx = {"site": site, "org": urljoin(site, "/#organization"), "site_id": urljoin(site, "/#website"),
           "tr_id": urljoin(site, sd.get("tr_entity_id", "/tr/#person")),
           "lib_wikipedia": (ent.get("library") or {}).get("wikipedia"),
           "lib_wikidata": (ent.get("library") or {}).get("wikidata"),
           "tr_wikipedia": (ent.get("tr") or {}).get("wikipedia"),
           "tr_wikidata": (ent.get("tr") or {}).get("wikidata"),
           "podcast_name": sd.get("podcast_name", "Good Citizen"),
           "podcast_url": urljoin(site, sd.get("podcast_path", "/podcast/good-citizen"))}

    from .audit import sitemap_urls
    sess = C.session(cfg.get("audit", {}).get("user_agent"))
    try:
        urls = list(dict.fromkeys(sitemap_urls(sess, cfg["site"]["sitemap"])))
    except Exception as e:  # noqa: BLE001
        C.set_status("schema", "error", f"sitemap: {e}"[:300])
        raise C.JobError(str(e)) from e
    node_urls = [u for u in urls if re.search(r"/node/\d+", u)]
    fetch_urls = [u for u in urls if u not in node_urls and not any(x.search(path_of(u)) for x in skip)]

    def fetch(u):
        try:
            r = sess.get(u, timeout=25)
            if r.status_code < 400 and "html" in r.headers.get("content-type", ""):
                return path_of(r.url), extract(r.text, r.url)
        except Exception:  # noqa: BLE001
            pass
        return path_of(u), None
    with ThreadPoolExecutor(max_workers=cfg.get("audit", {}).get("workers", 6)) as ex:
        pages = {p: d for p, d in ex.map(fetch, fetch_urls) if d}
    if not pages:
        C.set_status("schema", "error", "no pages could be read")
        raise C.JobError("no pages")

    try:
        llms_status = sess.get(urljoin(site, "/llms.txt"), timeout=20).status_code
    except Exception:  # noqa: BLE001
        llms_status = None

    groups = defaultdict(lambda: {"items": []})
    for p, d in sorted(pages.items()):
        own = sorted(set(d["types"]) - SITEWIDE)
        for g in classify(p, d):
            ok = bool(set(own) & g["expect"])
            item = {"path": p, "title": d["title"], "has": own, "done": ok}
            if ok:
                miss = missing_props(d["nodes"], g["expect"]) or []
                if miss:
                    item["missing_props"] = miss
            if g is FAQ_GROUP:
                item["questions"] = len(d["faq"])
                if not ok:
                    item["jsonld"] = g["build"](d, ctx)
            groups[g["key"]]["items"].append(item)
            if not ok and "example" not in groups[g["key"]]:
                groups[g["key"]]["example"] = {"path": p, "jsonld": g["build"](d, ctx)}

    out_groups = []
    for g in [FAQ_GROUP] + GROUPS:
        data = groups.get(g["key"])
        if not data:
            continue
        items = data["items"]
        done = sum(i["done"] for i in items)
        gaps = defaultdict(int)
        for i in items:
            for k in i.get("missing_props", []):
                gaps[k] += 1
        out_groups.append({
            "incomplete": sum(1 for i in items if i.get("missing_props")),
            "property_gaps": dict(sorted(gaps.items(), key=lambda x: -x[1])),
            "key": g["key"], "label": g["label"], "schema_type": " / ".join(sorted(g["expect"])),
            "why": g["why"], "drupal": g["drupal"], "pages": len(items), "done": done, "missing": len(items) - done,
            "example": data.get("example"), "items": items,
        })
    # Order by value to AI answers, not just page count: TR history and Q&A are what
    # assistants quote most; individual YouTube videos already have markup on YouTube.
    weight = {"tr_articles": 3, "tr_people": 3, "tr_speeches": 3, "tr_hubs": 2, "faq": 3, "event": 3,
              "podcast_episode": 2, "podcast_series": 2, "itineraries": 2, "press": 2, "staff": 1,
              "trustees": 1, "videos": 0.5, "video_playlists": 0.5}
    out_groups.sort(key=lambda g: (-(g["missing"] + 0.3 * g["incomplete"]) * weight.get(g["key"], 1), g["label"]))

    article_paths = [p for p in pages if re.match(r"^/(tr/[^/]+/.+|(about/)?press/press-releases/.+|podcast/good-citizen/.+)", p)]
    playlist_links = {v for p, d in pages.items() if p.startswith("/video/playlist/") for v, _ in d["videos"]}
    extras = {
        "llms_status": llms_status,
        "node_urls": len(node_urls), "node_examples": node_urls[:8],
        "video_view_in_sitemap": sum(1 for u in urls if "/video/view/" in u),
        "video_views_linked": len(playlist_links),
        "website_og": sum(1 for p in article_paths if pages[p]["og_type"] == "website"),
    }
    defined = {i for d in pages.values() for i in d["defined_ids"]}
    dangling = defaultdict(list)
    for p, d in pages.items():
        for i in d["stub_ids"]:
            if i not in defined:
                dangling[i].append(p)
    extras["dangling"] = {i: ps for i, ps in dangling.items()}
    bad_dates = []
    for p, d in pages.items():
        for n in d["nodes"]:
            for k in DATE_KEYS:
                v = n.get(k)
                if isinstance(v, str) and BASIC_OFFSET.search(v):
                    bad_dates.append((p, k, v))
    extras["bad_dates"] = bad_dates
    home = pages.get("/") or extract(sess.get(site, timeout=25).text, site)
    today = C.today()
    findings = sitewide_checks(home, ctx, today, extras)

    summary_line = next((n.get("description") for b in home["blocks"] if isinstance(b, dict)
                         for n in b.get("@graph", [b]) if isinstance(n, dict) and "Museum" in str(n.get("@type"))), "")
    summary_line = re.sub(r"\s*Opens July 4, 2026\.?", " Opened July 4, 2026.", summary_line or "").strip() or \
        "Presidential library and museum in Medora, North Dakota, dedicated to Theodore Roosevelt."
    draft = llms_draft(cfg["site"]["name"], site, summary_line, pages)
    C.data_path("site-llms.txt").write_text(draft, encoding="utf-8")

    total = sum(g["pages"] for g in out_groups if g["key"] != "faq")
    done = sum(g["done"] for g in out_groups if g["key"] != "faq")
    with_own = sum(1 for d in pages.values() if set(d["types"]) - SITEWIDE)
    result = {
        "generated": C.now_iso(),
        "summary": {
            "pages_read": len(pages), "pages_with_own_markup": with_own,
            "typed_pages": total, "typed_pages_done": done,
            "coverage_pct": round(100 * done / total) if total else None,
            "faq_pages": len(groups.get("faq", {}).get("items", [])),
            "faq_questions": sum(i.get("questions", 0) for i in groups.get("faq", {}).get("items", [])),
            "sitewide_issues": len(findings), "high": sum(f["severity"] == "high" for f in findings),
            "llms_txt": llms_status == 200,
        },
        "sitewide": findings,
        "groups": out_groups,
        "llms_txt_draft": "data/site-llms.txt",
    }
    C.write_json("schema.json", result)
    s = result["summary"]
    C.set_status("schema", "ok", f"{s['typed_pages_done']}/{s['typed_pages']} content pages have their own markup; "
                 f"{s['sitewide_issues']} sitewide issues", pages=len(pages))
