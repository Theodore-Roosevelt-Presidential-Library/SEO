# trlibrary.com structured data: requests for FiveJars

**From:** Matt Briney, TRPL · **Date:** November 3, 2026
**Basecamp:** Retainer Backlog (new features)
**Live findings:** https://seo.labs.trlibrary.com/#schema (re-checked weekly)

TRPL handled the Metatag settings on our side today (list at the end). The items below need template, module or server work. They're in priority order. Every example is a draft built from a live page: please check the field mapping and fill in anything marked TODO.

All markup should reference the existing sitewide entities by `@id`:

- Library: `https://www.trlibrary.com/#organization`
- Website: `https://www.trlibrary.com/#website`
- Theodore Roosevelt: `https://www.trlibrary.com/tr/#person` (now defined in full on every Basic page; see below)

---

## 0. Please pull today's config changes into the repo first

These Metatag defaults were changed on production through **Configuration synchronization → Single import**. Please export them into the codebase before the next deploy so a config import doesn't undo them:

- `metatag.metatag_defaults.global`: Wikipedia added to Organization `sameAs`
- `metatag.metatag_defaults.node__page`: new Schema.org Person group for Theodore Roosevelt (`@id` `https://www.trlibrary.com/tr/#person`, name, alternate name, birth and death dates, job title, Wikipedia and Wikidata `sameAs`)
- `metatag.metatag_defaults.node__press_release`: `og:type` article, author and publisher, description, and dates switched to the `custom:c` format; `dateModified` now uses `changed` instead of `created`
- `metatag.metatag_defaults.node__podcast` (new): `og:type` article
- `metatag.metatag_defaults.node__board_member`: `memberOf` → `#organization`

**Note on the Person stub:** /tr pages already printed a bare `{"@type":"Person","@id":".../tr/#person"}` from your code. It now shares its `@id` with the full Metatag Person, so the two merge. When you build item 1, keep using that `@id` and drop the stub.

---

## 1. Article markup on /tr pages (highest value): about 190 pages

/tr pages share the Basic page content type with /visit and /about pages, so Metatag bundle defaults can't target them. Please output Article JSON-LD on Basic pages whose path starts with `/tr/` (excluding the section hubs in item 2), and set `og:type` to `article` on the same pages.

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "@id": "https://www.trlibrary.com/tr/badlands/bad-lands-cow-boy#main",
  "headline": "[node:title]",
  "url": "[node:url:absolute]",
  "description": "[node:summary or meta description]",
  "image": "[share image]",
  "dateModified": "[node:changed, PHP format c → 2026-10-28T08:34:37-06:00]",
  "author": {"@id": "https://www.trlibrary.com/#organization"},
  "publisher": {"@id": "https://www.trlibrary.com/#organization"},
  "about": {"@id": "https://www.trlibrary.com/tr/#person"},
  "isPartOf": {"@id": "https://www.trlibrary.com/#website"}
}
```

Two variants:

- **/tr/people/\*** (26 pages): `about` is the person the page covers: `{"@type":"Person","name":"Alice Hathaway Lee Roosevelt","sameAs":[Wikipedia, Wikidata]}`. A plain-text **Wikidata URL** field on the node would make this precise. TRPL can fill it in.
- **/tr/speeches/\*** (6 pages): `about` is the speech: `{"@type":"CreativeWork","name":"Confession of Faith (1912)","author":{"@id":"https://www.trlibrary.com/tr/#person"}}`.

Check: https://www.trlibrary.com/tr/badlands/bad-lands-cow-boy has one Article whose `about` resolves to TR, and `og:type` is article.

## 2. CollectionPage on /tr section hubs: 55 pages

These are the hub pages (`/tr`, `/tr/badlands`, `/tr/presidency`, and so on). The Schema.org WebPage submodule isn't enabled; output it from code or enable `schema_web_page`.

```json
{"@context":"https://schema.org","@type":"CollectionPage","@id":"https://www.trlibrary.com/tr#main",
 "name":"[title]","url":"[url]","description":"[summary]","image":"[share image]",
 "about":{"@id":"https://www.trlibrary.com/tr/#person"},"isPartOf":{"@id":"https://www.trlibrary.com/#website"}}
```

## 3. PodcastEpisode on Good Citizen episodes (67) and PodcastSeries on /podcast/good-citizen (1)

The installed Schema.org Metatag module has no PodcastEpisode type. The Podcast content type now has `og:type` article (done).

```json
{"@context":"https://schema.org","@type":"PodcastEpisode",
 "@id":"https://www.trlibrary.com/podcast/good-citizen/adam-met-climate-action-musical-stardom-and-art-building-movement#main",
 "name":"[title]","url":"[url]","description":"[summary]","image":"[field_image]",
 "datePublished":"TODO: release date field, format c",
 "partOfSeries":{"@id":"https://www.trlibrary.com/podcast/good-citizen#main"},
 "associatedMedia":{"@type":"MediaObject","embedUrl":"[Simplecast player URL from field_podcast_embed_code]"},
 "publisher":{"@id":"https://www.trlibrary.com/#organization"}}
```

```json
{"@context":"https://schema.org","@type":"PodcastSeries","@id":"https://www.trlibrary.com/podcast/good-citizen#main",
 "name":"Good Citizen Podcast","url":"https://www.trlibrary.com/podcast/good-citizen",
 "description":"[page summary]","image":"[share image]","publisher":{"@id":"https://www.trlibrary.com/#organization"}}
```

If there's no release-date field, please tell us which field the episode date should come from.

## 4. VideoObject on video pages (409) and ItemList on playlists (39)

Drupal already stores each video's YouTube data. Please output, using format c for dates and ISO 8601 for duration:

- `/video/view/{id}`: `VideoObject` with name, description, `thumbnailUrl`, `embedUrl`, `uploadDate` (YouTube publish date), `duration`, and publisher `#organization`.
- `/video/playlist/{id}`: `ItemList` of `ListItem` → `VideoObject` (same fields), with `position` in playlist order.

Example: https://www.trlibrary.com/video/view/-QfzHHXPYqM

## 5. Split the restaurant and store hours out of the Library's hours

The Organization's `openingHoursSpecification` is generated dynamically and carries 15 entries, including "retail store" and "restaurant" hours. Search and AI tools read all of them as museum hours. Please:

- keep only museum hours on `#organization`;
- add `containsPlace` with a `Restaurant` (Salt + Scoria) and a `Store` (the Library store), each with its own hours from the same source.

This needs a change in the dynamic hours plugin, so it can't be done from Metatag.

## 6. Admission in the Library's markup

Add to `#organization`: `"isAccessibleForFree": false`, `"publicAccess": true`, and `makesOffer` → `Offer` (General admission, `priceCurrency` USD, `url` https://www.trlibrary.com/tickets). **TRPL to confirm the price figures.** Better still, pull them from the ticketing source so they don't go stale.

## 7. Serve /llms.txt

Please serve a plain-text file at https://www.trlibrary.com/llms.txt (`Content-Type: text/plain`). Draft: https://seo.labs.trlibrary.com/data/site-llms.txt. TRPL will review the draft before it goes live.

## 8. Smaller items

- **Unaliased /node/ URLs in the XML sitemap (35):** e.g. /node/205, /node/213, /node/22. Please leave unaliased nodes out of the sitemap.
- **Optional:** the accordion block on /benefactor-society-qas is an older block type without the "FAQ schema" checkbox that the newer Accordion block has. Either add the checkbox to that block type, or TRPL will rebuild the page with the current Accordion block.

---

## Already done by TRPL (no action needed beyond item 0)

- The sitewide description is in the present tense, and Wikidata and Wikipedia are in `sameAs`.
- Theodore Roosevelt is defined in full (on Basic pages), so the /tr `about` references now resolve.
- Press releases: `og:type` article; author and publisher set; `datePublished`/`dateModified` now in strict ISO format (`-06:00`).
- Podcast episodes: `og:type` article.
- Trustees: `memberOf` the Library.

## How we'll check

The SEO tool re-reads every page weekly (Monday) and moves each item to done when the live JSON-LD matches. You can also check any page at https://validator.schema.org.
