# trlibrary.com search & AI visibility digest
Generated 2026-11-07T13:22:08+00:00 from https://seo.labs.trlibrary.com. Full data: see 'Raw data' at the end.

## How to use this
This briefing is for doing the work, not only describing it. An assistant pointed here has four jobs, in this order:

1. **Work queue** (next section): audit fixes, internal links and structured data, ranked, each with the pages, who can fix it (the TRPL team in Drupal, or FiveJars), the Drupal steps and how to check it worked. Propose the exact change for the top TRPL tasks; once approved, carry it out (or package it for FiveJars).
2. **Drafted recommendations**: titles, descriptions and content for pages with search upside.
3. **Opportunities**: pages to strengthen, merge or rewrite.
4. **AI visibility and visitor experience**: what AI assistants say about the Library and where /visit pages fall short.

House rules for any change:

- Nothing on trlibrary.com changes without the communications team's approval. Once approved, make the change (if you have Drupal access) or hand it over ready to paste; never stop at a recommendation when a work-queue task can be carried out.
- After any change, log it in config/changes.yml (date, page, kind, what) so the next run holds the page and reports before/after numbers.
- Pages listed under 'Recently changed' were just edited: don't recommend changing them again until their hold ends; judge them by the before/after numbers.
- Never invent historical facts, dates, names, prices or hours. Use only what the page already says, or flag it for verification.
- Never quote or paraphrase Theodore Roosevelt. Say 'consider a verified TR quote about X' instead.
- Voice: friendly, plain, concrete (a knowledgeable park ranger, not a professor). Keep 'we/our/us' to a minimum.
- No specific years in visitor copy; write seasons as months.
- A Library visit takes about 3 1/2 hours. Never present a shorter visit as typical.
- Nonpartisan: no current political figures or debates.
- Page titles: the site appends ' | Theodore Roosevelt Presidential Library' automatically; suggest only the page-specific part, 60 characters or fewer.
- Meta descriptions: 120-155 characters with a reason to click.
- Recommend selectively: lead with one to three moves (start from 'This week's moves'), then a short 'what else we checked' list, each with a one-line reason it can wait.
- Size gains honestly: name how the gain happens (a new ranking, a higher position, or more clicks at the same position); a page that already ranks already gets some clicks; upside figures rank options and are never forecasts.
- Website changes are made in Drupal Layout Builder by the TRPL team; bugs and features go to the developers (FiveJars).

## Work queue: what to fix next, who fixes it, and how
51 tasks (2 search, 21 audit, 5 internal links, 23 structured data, 0 AI visibility); 18 with FiveJars or blocked. Ranked by severity x the Google audience of the pages involved. Full lists, every page, and step-by-step Drupal recipes: https://seo.labs.trlibrary.com/data/work_queue.json

### This week's moves
1. **Restaurant and store hours are listed as the museum's hours** (`schema:sitewide:mixed_hours`): medium priority; affects the whole site. Start with: The museum entity carries 15 hours entries, including restaurant, store hours. Machines can't tell which hours mean the museum is open.
2. **Add internal links where pages already mention each other** (`links:add`): medium priority; pages involved get 537,291 Google impressions (28 days). Start with: /tr/timeline; /visit/exhibits/main; /tr/family/family-tree.
3. **Strengthen pages ranking just off the top for searches people make** (`search:striking_distance`): medium priority; pages involved get 111,431 Google impressions (28 days). Start with: /podcast/good-citizen/senator-chris-murphy for "chris murphy" (#12.5, ); /podcast/good-citizen/bill-kristol for "bill kristol" (#11.7, ); /podcast/good-citizen/kermit-roosevelt-iii for "kermit roosevelt" (#7.4, ).

### What else we checked (and why it can wait)
- TR history articles: fill Article on the busiest pages now (per page, until the template lands) (`schema:tr_articles:per_node`): same area as a move this week (structured data); next in line
- TR history: people: fill Article on the busiest pages now (per page, until the template lands) (`schema:tr_people:per_node`): same area as a move this week (structured data); next in line
- Pages nothing links to (`links:orphans`): same area as a move this week (internal links); next in line
- Same topic on two pages (merge or differentiate) (`links:duplicate_topics`): needs a decision first (merge or archive)
- Pages ranking well that people skip: rewrite title and description (`search:low_ctr`): same area as a move this week (search); next in line
- TR history: speeches: fill Article on the busiest pages now (per page, until the template lands) (`schema:tr_speeches:per_node`): same area as a move this week (structured data); next in line
- Same title as another page (`audit:title_duplicate`): smaller reach (14,185 Google impressions vs 111,431 for this week's moves)
- No H1 heading (`audit:h1_missing`): smaller reach (6,138 Google impressions vs 111,431 for this week's moves)

**How to work it**
1. Pick tasks from the top of the queue (or a page job, to do everything on one page at once). Pages marked held changed recently and are being measured: leave their titles, descriptions and copy alone (adding markup or links to them is fine).
2. Write the exact change: new title/description, the sentence with the link, the markup fields, the redirect. Use only facts already on the page.
3. Get approval from the communications team before changing the live site. Merges, archiving and anything sitewide always need approval.
4. If you have Drupal admin access, make TRPL-owned changes yourself using the recipe. Content changes to a page can be saved as a draft first.
5. For FiveJars-owned tasks, write a Basecamp to-do: what's wrong, example URLs, the ready-to-paste JSON-LD or setting, how to check.
6. Check the live page afterwards (view source for meta tags and JSON-LD; follow redirects with curl).
7. Log each change in config/changes.yml (date, page, kind, what) so the next run holds the page and reports before/after numbers.

| # | Task | Area | Who | Pages/items | Status | Id |
|---|---|---|---|---|---|---|
| 1 | Restaurant and store hours are listed as the museum's hours | structured data | TRPL | 1 | to do | schema:sitewide:mixed_hours |
| 2 | TR history articles: fill Article on the busiest pages now (per page, until the template lands) | structured data | TRPL | 15 | to do | schema:tr_articles:per_node |
| 3 | Add internal links where pages already mention each other | internal links | TRPL | 572 | to do | links:add |
| 4 | TR history: people: fill Article on the busiest pages now (per page, until the template lands) | structured data | TRPL | 15 | to do | schema:tr_people:per_node |
| 5 | Pages nothing links to | internal links | TRPL | 50 | to do | links:orphans |
| 6 | Same topic on two pages (merge or differentiate) | internal links | TRPL | 20 | needs approval | links:duplicate_topics |
| 7 | Strengthen pages ranking just off the top for searches people make | search | TRPL | 30 | to do | search:striking_distance |
| 8 | Pages ranking well that people skip: rewrite title and description | search | TRPL | 5 | to do | search:low_ctr |
| 9 | TR history: speeches: fill Article on the busiest pages now (per page, until the template lands) | structured data | TRPL | 6 | to do | schema:tr_speeches:per_node |
| 10 | Same title as another page | audit | TRPL | 37 | to do | audit:title_duplicate |
| 11 | No H1 heading | audit | TRPL | 29 | to do | audit:h1_missing |
| 12 | Missing Open Graph tags | audit | TRPL | 11 | to do | audit:og_missing |
| 13 | No meta description | audit | TRPL | 10 | to do | audit:meta_missing |
| 14 | Turn on IndexNow so Bing and Copilot see changes within hours | audit | FiveJars | 1 | to do | setup:indexnow |
| 15 | Sitemap lists a URL that redirects | audit | TRPL | 5 | to do | audit:redirect_in_sitemap |
| 16 | Same title as another page (Video pages: fix once in the video template) | audit | FiveJars | 32 | to do | audit:title_duplicate:template |
| 17 | Links that go through a redirect | internal links | TRPL | 72 | to do | links:via_redirect |
| 18 | No meta description (Video pages: fix once in the video template) | audit | FiveJars | 17 | to do | audit:meta_missing:template |
| 19 | Missing Open Graph tags (Video pages: fix once in the video template) | audit | FiveJars | 17 | to do | audit:og_missing:template |
| 20 | Related pages that don't link to each other | internal links | TRPL | 49 | to do | links:related |
| 21 | Title over 60 characters, not counting the site-name suffix | audit | TRPL | 90 | to do | audit:title_too_long |
| 22 | Sitemap lists a /node/ URL instead of a readable path | audit | TRPL | 35 | to do | audit:unaliased_url |
| 23 | Same meta description as another page | audit | TRPL | 43 | to do | audit:meta_duplicate |
| 24 | Title under 15 characters, not counting the site-name suffix | audit | TRPL | 144 | to do | audit:title_too_short |
| 25 | More than one H1 | audit | TRPL | 10 | to do | audit:h1_multiple |
| 26 | Under 150 words of body text | audit | TRPL | 239 | to do | audit:thin_content |
| 27 | Title over 60 characters, not counting the site-name suffix (Video pages: fix once in the video template) | audit | FiveJars | 173 | to do | audit:title_too_long:template |
| 28 | Same meta description as another page (Video pages: fix once in the video template) | audit | FiveJars | 82 | to do | audit:meta_duplicate:template |
| 29 | Meta description under 70 characters | audit | TRPL | 2 | to do | audit:meta_too_short |
| 30 | Meta description under 70 characters (Video pages: fix once in the video template) | audit | FiveJars | 16 | to do | audit:meta_too_short:template |

### Task details (TRPL can do these now)
**1. Restaurant and store hours are listed as the museum's hours** (`schema:sitewide:mixed_hours`, 1 items)
- How: Keep only museum hours on the Library entity. Give the restaurant and the store their own entities (Restaurant, Store) with their hours, linked with containsPlace. Sitewide (Global) meta tags: change them only through Configuration > Development > Configuration synchronization > Import > Single item (Simple configuration, metatag.metatag_defaults.global), then clear all caches. Never save the Global defaults form itself: it drops fields. The Global Organization fields have no containsPlace: TRPL can trim the hours to museum hours only; the Restaurant and Store entities need FiveJars.
- Done when: The issue no longer appears in schema.json after the next weekly run
- Paste: `{"containsPlace": [{"@type": "Restaurant", "name": "TODO: restaurant name", "servesCuisine": "TODO: cuisine", "openingHoursSpecification": "TODO: restaurant hours"}, {"@type": "Store", "name": "TODO: store name", "openingHoursSpecification": "TODO: store hours"}]}`

**2. TR history articles: fill Article on the busiest pages now (per page, until the template lands)** (`schema:tr_articles:per_node`, 15 items)
- How: Edit the node > 'Customize meta tags' > Schema.org Article: @type Article; headline = the page title; description = the meta description; about = Theodore Roosevelt; author and publisher = the Library; dateModified = [node:changed:html_datetime]. Don't paste raw JSON-LD into a text block (it's stripped).
- Done when: Pages carry Article markup (schema.json 'TR history articles' shows them as done)
  - `/tr/presidency/roosevelt-corollary`, 133,223 impr.
  - `/tr/presidency/brownsville`, 117,631 impr.
  - `/tr/presidency/square-deal`, 98,664 impr.
  - `/tr/family/fdr-connection`, 89,289 impr.
  - `/tr/presidency/trust-busting`, 76,021 impr.
  - `/tr/presidency/panama-canal`, 63,571 impr.
  - `/tr/post-presidency/bull-moose/platform`, 37,279 impr.
  - `/tr/rise-to-power/spanish-american-war`, 34,033 impr.
  - ...and 7 more in work_queue.json

**3. Add internal links where pages already mention each other** (`links:add`, 572 items)
- How: Open the source page's Layout. Edit the text block that contains the context sentence and turn the [[bracketed]] words into a link to the target path (relative, e.g. /tr/tr-shot). Don't write new sentences just to hold a link. Save the block, then Save layout.
- Done when: The link appears on the source page; the target's links-in count rises next week
  - `/tr/timeline`, 42,769 impr., [[Panama Canal]] -> /tr/presidency/panama-canal; [[Citizenship in a Republic]] -> /tr/speeches/man-in-the-arena; [[Great White Fleet]] -> /tr/presidency/great-white-fleet
  - `/visit/exhibits/main`, 4,402 impr., [[Brownsville affair]] -> /tr/presidency/brownsville; [[Square Deal]] -> /tr/presidency/square-deal; [[Panama Canal]] -> /tr/presidency/panama-canal
  - `/tr/family/family-tree`, 26,389 impr., [[Elliott Roosevelt]] -> /tr/family/elliott-roosevelt; [[Alice Roosevelt Longworth]] -> /tr/people/alice-longworth; [[Alice Hathaway Lee]] -> /tr/new-york-politics/alice-lee
  - `/tr/people/henry-cabot-lodge`, 13,585 impr., [[Bully Pulpit]] -> /tr/presidency/bully-pulpit; [[William Howard Taft]] -> /tr/people/william-howard-taft; [[River of Doubt]] -> /tr/post-presidency/river-of-doubt
  - `/podcast/good-citizen/doris-kearns-goodwin-presidential-stories-trpl-and-enduring-lessons-theodore`, 958 impr., [[square deal]] -> /tr/presidency/square-deal; [[Man in the Arena]] -> /tr/speeches/man-in-the-arena; [[Alice Roosevelt]] -> /tr/people/alice-longworth
  - `/tr/presidency-timeline`, 54,330 impr., [[Roosevelt Corollary]] -> /tr/presidency/roosevelt-corollary; [[Panama Canal]] -> /tr/presidency/panama-canal; [[Great White Fleet]] -> /tr/presidency/great-white-fleet
  - `/tr/teddy-nickname`, 17,092 impr., [[Roosevelt Corollary]] -> /tr/presidency/roosevelt-corollary; [[teddy bear]] -> /tr/legacy/teddy-bear; [[Square Deal]] -> /tr/presidency/square-deal
  - `/tr/legacy/rankings`, 9,512 impr., [[Mount Rushmore]] -> /tr/tr-mount-rushmore; [[Panama Canal]] -> /tr/presidency/panama-canal; [[bully pulpit]] -> /tr/presidency/bully-pulpit
  - ...and 244 more in work_queue.json

**4. TR history: people: fill Article on the busiest pages now (per page, until the template lands)** (`schema:tr_people:per_node`, 15 items)
- How: Edit the node > 'Customize meta tags' > Schema.org Article: @type Article; headline = the page title; description = the meta description; about = Theodore Roosevelt; author and publisher = the Library; dateModified = [node:changed:html_datetime]. Don't paste raw JSON-LD into a text block (it's stripped).
- Done when: Pages carry Article markup (schema.json 'TR history: people' shows them as done)
  - `/tr/people/jacob-riis`, 82,408 impr.
  - `/tr/people/alice-longworth`, 28,252 impr.
  - `/tr/people/william-howard-taft`, 16,225 impr.
  - `/tr/people/henry-cabot-lodge`, 13,585 impr.
  - `/tr/people/ted-jr`, 12,447 impr.
  - `/tr/people/booker-t-washington`, 5,728 impr.
  - `/tr/people/john-muir`, 5,105 impr.
  - `/tr/people/theodore-sr`, 4,947 impr.
  - ...and 7 more in work_queue.json

**5. Pages nothing links to** (`links:orphans`, 50 items)
- How: Add 2-3 links to this page from the pages listed under 'link from' (each has the sentence and words to link).
- Done when: At least two pages link in
  - `/tr/tr-mount-rushmore`, 114,372 impr., link from: /visit/directions ([[Mount Rushmore]]); /tr/legacy/rankings ([[Mount Rushmore]])
  - `/tr/pre-presidency-political-accomplishments`, 54,085 impr.
  - `/tr/tr-importance`, 38,657 impr.
  - `/tr/10-myths-teddy-bear`, 22,351 impr.
  - `/tr/fake-quotes`, 16,886 impr.
  - `/about/trustees/edward-okeefe`, 7,614 impr., link from: /podcast/good-citizen/call-adventure-charlie-melcher-ed-okeefe-and-brand-new-theodore-roosevelt ([[Edward O’Keefe]])
  - `/research/books-by-roosevelt`, 5,923 impr.
  - `/tr/5-big-adventures`, 5,692 impr.
  - ...and 42 more in work_queue.json

**6. Same topic on two pages (merge or differentiate)** (`links:duplicate_topics`, 20 items)
- How: Two pages compete for one subject. Pick the stronger page (clicks, depth), move anything unique onto it, then archive the other and add a 301 from its alias and /node/NID. Get approval first; draft before publishing.
- Done when: One page per topic; the other 301s to it
  - `/tr/tr-mount-rushmore`, 114,941 impr., mount rushmore: /tr/tr-mount-rushmore vs /tr/legacy/mount-rushmore
  - `/tr/rise-to-power/san-juan-hill`, 37,760 impr., rough riders: /tr/rise-to-power/san-juan-hill vs /tr/rise-to-power/rough-riders
  - `/tr/people/alice-longworth`, 27,947 impr., alice roosevelt longworth: /tr/people/alice-longworth vs /tr/people/alice-longworth/complex-legacy
  - `/tr/new-york-politics/alice-lee`, 12,345 impr., alice hathaway lee roosevelt: /tr/new-york-politics/alice-lee vs /tr/people/alice-lee
  - `/tr/new-york-politics/alice-lee`, 12,345 impr., alice lee: /tr/new-york-politics/alice-lee vs /tr/people/alice-lee
  - `/tr/rise-to-power/edith-roosevelt`, 12,019 impr., edith roosevelt: /tr/rise-to-power/edith-roosevelt vs /tr/people/edith-roosevelt
  - `/tr/quotes/misquotes`, 8,668 impr., common misquotes: /tr/quotes/misquotes vs /tr/myths/misquotes
  - `/tr/presidency/conservation/gifford-pinchot`, 7,877 impr., gifford pinchot: /tr/presidency/conservation/gifford-pinchot vs /tr/people/gifford-pinchot
  - ...and 12 more in work_queue.json

**7. Strengthen pages ranking just off the top for searches people make** (`search:striking_distance`, 30 items)
- How: Open the page and make it the best answer to that exact search: use the search's words in the title or a heading, answer it plainly in the first paragraph, add the specifics people want (facts already on the site), and link to it from 2-3 related pages. Don't rewrite a page that already ranks in the top 3 for its main search.
- Done when: Average position for the search improves over the next 4 weeks (change log before/after)
  - `/podcast/good-citizen/senator-chris-murphy`, 35,618 impr., "chris murphy" #12.5, None, upside ~3911 clicks/28d
  - `/podcast/good-citizen/bill-kristol`, 15,174 impr., "bill kristol" #11.7, None, upside ~1662 clicks/28d
  - `/podcast/good-citizen/kermit-roosevelt-iii`, 7,381 impr., "kermit roosevelt" #7.4, None, upside ~780 clicks/28d
  - `/podcast/good-citizen/senator-chris-murphy`, 6,206 impr., "senator chris murphy" #12.9, None, upside ~681 clicks/28d
  - `/video/view/Vf8ee-gccpc`, 4,654 impr., "teddy roosevelt library" #4.6, None, upside ~492 clicks/28d
  - `/tr/people/archibald`, 3,899 impr., "archibald roosevelt" #7.6, None, upside ~428 clicks/28d
  - `/podcast/good-citizen/matthew-continetti`, 3,805 impr., "matthew continetti" #10.3, None, upside ~417 clicks/28d
  - `/podcast/good-citizen/senator-chris-murphy`, 2,824 impr., "sen chris murphy" #10.0, None, upside ~309 clicks/28d
  - ...and 22 more in work_queue.json

**8. Pages ranking well that people skip: rewrite title and description** (`search:low_ctr`, 5 items)
- How: Edit the node (/node/NID/edit) > 'Customize meta tags'. Basic tags: Page title '<title> | [site:name]' (page part 60 characters or fewer) and Description (120-155 characters). Set Open Graph og:title/og:description and Twitter card title/description to match. Save with 'Save' (keeps the moderation state). If the save seems to do nothing, look for a validation error further down the form.
- Done when: Click-through rate rises at the same position (change log before/after)
  - `/video/view/Vf8ee-gccpc`, 19,431 impr.
  - `/tr/rise-to-power/spanish-american-war`, 32,600 impr.
  - `/tr/presidency/food-and-drug`, 19,765 impr.
  - `/contact`, 6,860 impr.
  - `/visit/lodging`, 17,880 impr.

**9. TR history: speeches: fill Article on the busiest pages now (per page, until the template lands)** (`schema:tr_speeches:per_node`, 6 items)
- How: Edit the node > 'Customize meta tags' > Schema.org Article: @type Article; headline = the page title; description = the meta description; about = Theodore Roosevelt; author and publisher = the Library; dateModified = [node:changed:html_datetime]. Don't paste raw JSON-LD into a text block (it's stripped).
- Done when: Pages carry Article markup (schema.json 'TR history: speeches' shows them as done)
  - `/tr/speeches/man-in-the-arena`, 34,737 impr.
  - `/tr/speeches/strenuous-life`, 3,949 impr.
  - `/tr/speeches/inaugural`, 2,435 impr.
  - `/tr/speeches/new-nationalism`, 2,181 impr.
  - `/tr/speeches/first-annual-message`, 1,328 impr.
  - `/tr/speeches/confession-of-faith`, 1,308 impr.

**10. Same title as another page** (`audit:title_duplicate`, 37 pages)
- How: Edit the node (/node/NID/edit) > 'Customize meta tags'. Basic tags: Page title '<title> | [site:name]' (page part 60 characters or fewer) and Description (120-155 characters). Set Open Graph og:title/og:description and Twitter card title/description to match. Save with 'Save' (keeps the moderation state). If the save seems to do nothing, look for a validation error further down the form.
- Done when: No other page has the same title
  - `/calendar/daily-activity/room-sixty-years-front-lines-history`, 3,102 impr., title "In the Room: Sixty Years on the Front Lines of History" (54 chars), same as /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf
  - `/about/trustees/kermit-roosevelt`, 2,714 impr., title "Kermit Roosevelt" (16 chars), same as /tr/people/kermit
  - `/visit/exhibits/kennerly`, 1,881 impr., title "In the Room: Sixty Years on the Front Lines of History" (54 chars), same as /calendar/daily-activity/room-sixty-years-front-lines-history, /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly
  - `/tr/people/kermit`, 1,572 impr., HELD (recently changed), title "Kermit Roosevelt" (16 chars), same as /about/trustees/kermit-roosevelt
  - `/project/native-plant-project`, 1,517 impr., HELD (recently changed), title "Native Plant Project" (20 chars), same as /video/view/1SqdaUrbU7U
  - `/events/teddycon`, 1,022 impr., HELD (recently changed), title "Theodore Roosevelt Convention (#TeddyCon)" (41 chars), same as /event/24
  - `/about/trustees/douglas-brinkley`, 841 impr., title "Douglas Brinkley" (16 chars), same as /podcast/good-citizen/douglas-brinkley
  - `/podcast/good-citizen/douglas-brinkley`, 808 impr., HELD (recently changed), title "Douglas Brinkley" (16 chars), same as /about/trustees/douglas-brinkley
  - ...and 29 more in work_queue.json

**11. No H1 heading** (`audit:h1_missing`, 29 pages)
- How: Open the page's Layout (/node/NID/layout). Make sure the top section shows the page title block (Content fields > Title), which renders as the H1; or change the first heading in the top text block to Heading 1. Save layout.
- Done when: Exactly one H1
  - `/visit/planner`, 2,209 impr., no H1
  - `/tr/presidency/executive-actions/story`, 1,012 impr., no H1
  - `/grand-opening/photos/july2`, 733 impr., no H1
  - `/visit/maps/campus`, 696 impr., no H1
  - `/grand-opening/photos/july4`, 549 impr., no H1
  - `/tr/presidency/executive-actions/action`, 325 impr., no H1
  - `/membership/neighbor`, 141 impr., no H1
  - `/research/family-tree`, 100 impr., no H1
  - ...and 21 more in work_queue.json

**12. Missing Open Graph tags** (`audit:og_missing`, 11 pages)
- How: Edit the node (/node/NID/edit) > 'Customize meta tags'. Basic tags: Page title '<title> | [site:name]' (page part 60 characters or fewer) and Description (120-155 characters). Set Open Graph og:title/og:description and Twitter card title/description to match. Save with 'Save' (keeps the moderation state). If the save seems to do nothing, look for a validation error further down the form.
- Done when: og:title and og:description are present
  - `/join-us`, 2,742 impr.
  - `/visit/exhibits/kennerly`, 1,881 impr.
  - `/visit/teddy-trail`, 724 impr., HELD (recently changed)
  - `/birthdaycard`, 19 impr.
  - `/project/how-the-library-works`, 6 impr.
  - `/rsvp/midwinter`
  - `/quiz/the-boardwalk`
  - `/quiz/badlands-family`
  - ...and 3 more in work_queue.json

**13. No meta description** (`audit:meta_missing`, 10 pages)
- How: Edit the node (/node/NID/edit) > 'Customize meta tags'. Basic tags: Page title '<title> | [site:name]' (page part 60 characters or fewer) and Description (120-155 characters). Set Open Graph og:title/og:description and Twitter card title/description to match. Save with 'Save' (keeps the moderation state). If the save seems to do nothing, look for a validation error further down the form.
- Done when: The page has a meta description of 120-155 characters
  - `/join-us`, 2,742 impr.
  - `/visit/exhibits/kennerly`, 1,881 impr.
  - `/birthdaycard`, 19 impr.
  - `/project/how-the-library-works`, 6 impr.
  - `/rsvp/midwinter`
  - `/quiz/the-boardwalk`
  - `/quiz/badlands-family`
  - `/quiz/badlands-wildlife-family`
  - ...and 2 more in work_queue.json

**15. Sitemap lists a URL that redirects** (`audit:redirect_in_sitemap`, 5 pages)
- How: This sitemap URL redirects to another page. Edit the old node > XML sitemap > Inclusion: Excluded, or archive the node if it's retired (a 301 stays in place).
- Done when: The sitemap no longer lists the redirecting URL
  - `/event/24`, 1,592 impr.
  - `/calendar/special-event/gallery-david-hume-kennerly`, 134 impr.
  - `/calendar/special-event/artist-talk-room-david-hume-kennerly`, 80 impr.
  - `/calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf`, 19 impr.
  - `/calendar/special-event/book-signing-and-meet-greet-kennerly-balkowitsch-and-ziemendorf`, 8 impr.

### Page jobs: everything to fix on one page, busiest pages first
| Page | Impr. | Fixes | Links to add | Markup |  |
|---|---|---|---|---|---|
| /podcast/good-citizen/senator-chris-murphy | 134479 | meta_duplicate | [[high school]] -> /tr/for-educators/high-school; [[in the room]] -> /visit/exhibits/kennerly | – |  |
| /tr/presidency/roosevelt-corollary | 133223 | – | – | Article | held |
| /tr/tr-mount-rushmore | 127083 | – | [[Square Deal]] -> /tr/presidency/square-deal; [[Panama Canal]] -> /tr/presidency/panama-canal; [[Nobel Peace Prize]] -> /tr/presidency/nobel-peace-prize | – | held |
| /tr/presidency/brownsville | 117631 | – | – | Article | held |
| /tr/presidency/square-deal | 98664 | – | [[executive power]] -> /tr/presidency/executive-power | Article | held |
| /tr/family/fdr-connection | 89289 | – | [[Elliott Roosevelt]] -> /tr/family/elliott-roosevelt; [[William Howard Taft]] -> /tr/people/william-howard-taft; [[executive power]] -> /tr/presidency/executive-power | Article | held |
| /tr/people/jacob-riis | 82408 | – | – | Article | held |
| /tr/presidency/trust-busting | 76021 | – | [[William Howard Taft]] -> /tr/people/william-howard-taft | Article | held |
| /tr/presidency/panama-canal | 63571 | – | – | Article | held |
| /tickets | 60408 | title_too_short | – | – |  |
| /tr/presidency-timeline | 54330 | – | [[Roosevelt Corollary]] -> /tr/presidency/roosevelt-corollary; [[Panama Canal]] -> /tr/presidency/panama-canal; [[Great White Fleet]] -> /tr/presidency/great-white-fleet | – | held |
| /tr/pre-presidency-political-accomplishments | 53718 | – | [[governor of New York]] -> /tr/rise-to-power/governor; [[New York State Assembly]] -> /tr/new-york-politics/assembly; [[Civil War]] -> /tr/early-life/civil-war | – | held |
| /visit/directions | 49314 | – | [[Mount Rushmore]] -> /tr/tr-mount-rushmore; [[Plan ahead]] -> /visit/tickets/plan-ahead; [[Theodore Roosevelt National Park]] -> /visit/national-park | – | held |
| /tr/timeline | 42769 | – | [[Panama Canal]] -> /tr/presidency/panama-canal; [[Citizenship in a Republic]] -> /tr/speeches/man-in-the-arena; [[Great White Fleet]] -> /tr/presidency/great-white-fleet | – | held |
| /podcast/good-citizen/karl-rove-historic-redemption-hard-work-politics-and-essential-nature | 42373 | – | [[Henry Cabot Lodge]] -> /tr/people/henry-cabot-lodge; [[Civil War]] -> /tr/early-life/civil-war; [[Assistant Secretary of the Navy]] -> /tr/rise-to-power/assistant-navy-secretary | – | held |

### Waiting on FiveJars or blocked (already ticketed; check whether they've landed, don't re-ask)
- Sitewide markup doesn't link to the Library's Wikipedia entry (`schema:sitewide:sameas`): blocked, the per-page sameAs field is capped at 255 characters; FiveJars asked to raise it. Wikidata is in place; Wikipedia and Bluesky go back in once it's raised
- 249 pages point to a Theodore Roosevelt entity that is never defined (`schema:sitewide:tr_entity`)
- www.trlibrary.com has no llms.txt (`schema:sitewide:llms_txt`)
- No admission information in the markup (`schema:sitewide:admission`)
- TR history articles: add Article markup (template, all pages at once) (`schema:tr_articles`)
- TR history section pages: add CollectionPage markup (template, all pages at once) (`schema:tr_hubs`)
- Good Citizen episodes: add PodcastEpisode markup (template, all pages at once) (`schema:podcast_episode`)
- TR history: people: add Article markup (template, all pages at once) (`schema:tr_people`)
- TR history: speeches: add Article markup (template, all pages at once) (`schema:tr_speeches`)
- Video pages: add VideoObject markup (template, all pages at once) (`schema:videos`)
- Trip itineraries: add TouristTrip markup (template, all pages at once) (`schema:itineraries`)
- Good Citizen podcast page: add PodcastSeries markup (template, all pages at once) (`schema:podcast_series`)
- Video playlists: add ItemList / VideoObject markup (template, all pages at once) (`schema:video_playlists`)
- 22 pages have dates without a colon in the time zone (`schema:sitewide:date_format`)
- 277 articles are labelled og:type “website” (`schema:sitewide:og_type`)
- Pages with Q&A: add FAQPage markup (template, all pages at once) (`schema:faq`)
- Press releases: add Article / NewsArticle markup (template, all pages at once) (`schema:press`)
- Trustee profiles: add Person / ProfilePage markup (template, all pages at once) (`schema:trustees`)


## Data freshness
| Source | State | Updated | Details |
|---|---|---|---|
| audit | ok | 2026-11-02T12:32:16+00:00 | Crawled 1130 pages, health 96/100 |
| ranks | ok | 2026-11-02T12:38:36+00:00 | 30 keywords checked |
| opportunities | error | 2026-11-07T13:22:01+00:00 | 'est_extra_clicks' |
| gsc | ok | 2026-11-07T13:22:00+00:00 | 23019 queries, 2114 pages (2026-10-08 to 2026-11-04); 249 changed pages tracked |
| ai_visibility | error | 2026-11-02T12:44:59+00:00 | 38 answers from ChatGPT, Gemini, Perplexity; 19 failed: Perplexity 403: {"error":{"message":"The Agent API requires paid credits. Add paid credit at https://console.perplexity.ai to upgrade your organizatio |
| tips | ok | 2026-11-02T13:09:25+00:00 | Gemini wrote tips for 8 pages |
| digest | ok | 2026-11-06T13:22:29+00:00 | llms.txt, digest.md and digest.json rebuilt |
| checkout | ok | 2026-11-07T13:22:08+00:00 | Checkout completion n/a; steps not tracked: view_item, add_to_cart, begin_checkout, add_payment_info |
| curate | ok | 2026-11-02T12:33:01+00:00 | 10 discovered keywords and 4 discovered questions tracked; 7 changes today |
| ux | ok | 2026-11-02T12:59:15+00:00 | 79 pages; PageSpeed on 77; AI task check by gemini (gemini-3.8-flash); GA4 on; Clarity off; 2 errors, e.g. PageSpeed /visit/maps: PageSpeed 500: {   "error": {     "code": 500,     "message": "Lighthouse returned error: PAGE_HUNG. Lighthouse was unable to reliably load the URL you requeste |
| links | ok | 2026-11-02T13:01:07+00:00 | 1164 pages crawled; 0 broken internal links (redirects proposed); 1176 suggested links; 50 orphan pages; 49 related pairs without links |
| schema | ok | 2026-11-02T13:02:49+00:00 | 101/883 content pages have their own markup; 8 sitewide issues |
| indexnow | skipped | 2026-11-07T13:22:08+00:00 | No IndexNow key yet: see the work queue task 'Turn on IndexNow'. |

## Google Search (Search Console)
2026-10-08 to 2026-11-04 vs the prior 28 days: **43,034 clicks** (prior 55,730), 2,666,280 impressions (prior 2,344,330), CTR 1.6% (prior 2.4%), average position 5.9 (prior 6.5). Branded clicks 13713, non-branded 9913, search term hidden by Google 19408.

### Top non-branded searches (people who didn't search our name)
| Search | Clicks | Impr. | Pos. |
|---|---|---|---|
| brownsville affair | 1 | 114884 | 5.3 |
| chris murphy | 6 | 68795 | 12.2 |
| square deal | 129 | 59152 | 3.5 |
| karl rove | 29 | 34825 | 9.4 |
| roosevelt corollary | 51 | 23033 | 4.4 |
| jacob riis | 104 | 21332 | 9.9 |
| bill kristol | 8 | 18332 | 11.5 |
| senator chris murphy | 6 | 17575 | 13 |
| chris murphy senator | 9 | 13871 | 12.7 |
| theodore roosevelt | 59 | 13377 | 7.5 |
| theo elections | 4 | 13234 | 6.7 |
| alice roosevelt | 46 | 11519 | 8.2 |
| kermit roosevelt | 35 | 9295 | 7.3 |
| alice roosevelt longworth | 14 | 8771 | 8.5 |
| roosevelt family | 23 | 8719 | 3.7 |
| bull moose party | 53 | 8131 | 4 |
| bully pulpit | 24 | 8109 | 2.9 |
| mount rushmore presidents | 27 | 8041 | 4.6 |
| sen chris murphy | 5 | 7691 | 10.7 |
| man in the arena | 53 | 6988 | 5.8 |
| the man in the arena | 89 | 6940 | 5.7 |
| alice hathaway lee roosevelt | 9 | 6217 | 5.9 |
| teddy roosevelt | 40 | 6001 | 6.3 |
| henry cabot lodge | 6 | 5761 | 7 |
| senator murphy | 1 | 5641 | 12.2 |

### Top pages
| Page | Clicks | Prior | Impr. | Pos. |
|---|---|---|---|---|
| / | 8128 | 12350 | 84247 | 7.1 |
| /?utm_source=gbp&utm_medium=organic | 5743 | 914 | 37355 | 3.8 |
| /tickets | 3055 | 7649 | 58712 | 3.2 |
| /tr/family/fdr-connection | 1743 | 818 | 89289 | 3.2 |
| /visit | 1313 | 3011 | 59225 | 2.7 |
| /tr/presidency/trust-busting | 1040 | 763 | 76021 | 3.3 |
| /tr/speeches/man-in-the-arena | 829 | 269 | 34737 | 5.1 |
| /tr/square-deal | 794 | 1128 | 100167 | 3.9 |
| /tr/presidency/square-deal | 700 | 350 | 98664 | 4.2 |
| /bullet-speech | 664 | 744 | 40335 | 3.6 |
| /tr/quotes | 603 | 705 | 26341 | 10.6 |
| /visit/directions | 551 | 1140 | 49314 | 2.7 |
| /tr/pre-presidency-political-accomplishments | 539 | 553 | 53718 | 5.5 |
| /tr/people/jacob-riis | 476 | 283 | 82407 | 6.6 |
| /visit/hours | 460 | 1157 | 43910 | 2.4 |
| /tr/presidency/ten-facts | 453 | 170 | 15704 | 3.9 |
| /tr/tr-mount-rushmore | 442 | 870 | 127083 | 5.6 |
| /tr/rise-to-power/san-juan-hill | 411 | 242 | 30908 | 3.7 |
| /tr/family/family-tree | 393 | 218 | 26389 | 5.3 |
| /tr/fake-quotes | 358 | 416 | 15809 | 6.7 |
| /tr/tr-importance | 344 | 318 | 37382 | 4.9 |
| /tr/presidency-timeline | 329 | 315 | 54330 | 4.5 |
| /tr/presidency/panama-canal | 326 | 88 | 63571 | 4.9 |
| /tr/tr-shot | 308 | 332 | 35971 | 4.1 |
| /tr/presidency/roosevelt-corollary | 304 | 148 | 133223 | 4.7 |

## Opportunities (ranked)
_Estimated extra clicks use a rough industry click-through curve. Treat them as a way to rank opportunities, not a forecast._

### Striking distance: ranking 4-20 with demand; strengthen the page for the exact search
| Search | Page | Pos. | Impr. | How | Upside |
|---|---|---|---|---|---|
| chris murphy | /podcast/good-citizen/senator-chris-murphy | 12.5 | 35618 | – | 3911 |
| karl rove | /podcast/good-citizen/karl-rove-historic-redemption-hard-work-politics-and-essential-nature | 9.4 | 30455 | – | 3326 |
| bill kristol | /podcast/good-citizen/bill-kristol | 11.7 | 15174 | – | 1662 |
| alice roosevelt | /tr/people/alice-longworth | 8.1 | 10476 | – | 1104 |
| theo elections | /tr/presidency/elections | 6.4 | 9232 | – | 1012 |
| alice roosevelt longworth | /tr/people/alice-longworth | 8.4 | 9045 | – | 982 |
| kermit roosevelt | /podcast/good-citizen/kermit-roosevelt-iii | 7.4 | 7381 | – | 780 |
| senator chris murphy | /podcast/good-citizen/senator-chris-murphy | 12.9 | 6206 | – | 681 |
| alice hathaway lee roosevelt | /tr/new-york-politics/alice-lee | 5.8 | 6071 | – | 662 |
| henry cabot lodge | /tr/people/henry-cabot-lodge | 7 | 5815 | – | 634 |
| edith roosevelt | /tr/rise-to-power/edith-roosevelt | 6.4 | 5281 | – | 570 |
| quentin roosevelt | /tr/post-presidency/quentin | 10.9 | 4987 | – | 546 |
| great white fleet | /tr/presidency/great-white-fleet | 5.6 | 5189 | – | 545 |
| man in the arena | /tr/speeches/man-in-the-arena | 4.9 | 4973 | – | 503 |
| teddy roosevelt library | /video/view/Vf8ee-gccpc | 4.6 | 4654 | – | 492 |

### Ranking well but skipped: rewrite title/meta description
| Page | Pos. | CTR | Typical | Upside |
|---|---|---|---|---|
| /tr/presidency/great-white-fleet | 4.3 | 0.6% | 8.0% | 2045 |
| /tr/tr-importance | 5 | 0.9% | 6.0% | 1937 |
| /tr/post-presidency/bull-moose/platform | 5.1 | 0.7% | 6.0% | 1872 |
| /video/view/Vf8ee-gccpc | 3.8 | 0.4% | 8.0% | 1477 |
| /tr/presidency/bully-pulpit | 4.7 | 0.6% | 6.0% | 1413 |
| /tr/rise-to-power/spanish-american-war | 5.9 | 0.5% | 4.5% | 1317 |
| /tr/post-presidency/bull-moose | 4.6 | 0.6% | 6.0% | 1225 |
| /tr/family/family-tree | 5.2 | 1.5% | 6.0% | 1197 |
| /tr/complex-legacy/imperialism | 5.1 | 0.9% | 6.0% | 1187 |
| /tr/speeches/man-in-the-arena | 5.2 | 2.1% | 6.0% | 1127 |
| /tr/timeline | 7.6 | 0.5% | 3.0% | 1064 |
| /tr/presidency/conservation/national-parks | 6.1 | 0.8% | 4.5% | 850 |
| /tr/presidency/ten-facts | 4 | 2.7% | 8.0% | 817 |
| /tr/presidency/elections | 5.9 | 0.6% | 4.5% | 808 |
| /tr/presidency/conservation/reclamation | 4.2 | 0.9% | 8.0% | 806 |

### Search words missing from the ranking page's title
| Search | Page | Current title | Missing | Impr. |
|---|---|---|---|---|
| theo elections | /tr/presidency/elections | The Election of 1904: Roosevelt's Mandate and Fateful Promise / Theodore Roosevelt Presidential Library | theo | 9232 |
| carl rove | /podcast/good-citizen/karl-rove-historic-redemption-hard-work-politics-and-essential-nature | Karl Rove: Historic Redemption, the Hard Work of Politics, and the Essential Nature of Americans / Theodore Roosevelt Presidential Library | carl | 2064 |
| when did teddy roosevelt die | /tr/timeline | Timeline of TR’s Life / Theodore Roosevelt Presidential Library | did, teddy, die | 1521 |
| what was theodore roosevelt known for | /tr/tr-importance | Why is Theodore Roosevelt Important? / Theodore Roosevelt Presidential Library | was, known | 1280 |
| when did theodore roosevelt die | /tr/timeline | Timeline of TR’s Life / Theodore Roosevelt Presidential Library | did, die | 1086 |
| bill crystal | /podcast/good-citizen/bill-kristol | Bill Kristol / Theodore Roosevelt Presidential Library | crystal | 896 |
| theodore franklin | /tr/family/family-tree | The Roosevelt Family Tree / Theodore Roosevelt Presidential Library | franklin | 867 |
| hotel 1883 medora nd | /visit/lodging | Lodging / Theodore Roosevelt Presidential Library | hotel, 1883, medora, nd | 863 |
| do what you can with what you have where you are | /tr/fake-quotes | Did TR Really Say That? / Theodore Roosevelt Presidential Library | have | 843 |
| president rankings | /tr/legacy/rankings | TR in Presidential Rankings: A Consistent Top Tier / Theodore Roosevelt Presidential Library | president | 809 |
| how did teddy roosevelt die | /tr/post-presidency/death | Death at Sagamore Hill: January 6, 1919 / Theodore Roosevelt Presidential Library | did, teddy, die | 786 |
| where was theodore roosevelt born | /tr/timeline | Timeline of TR’s Life / Theodore Roosevelt Presidential Library | was, born | 744 |
| young teddy roosevelt | /tr/early-life | Theodore Roosevelt's Early Life / Theodore Roosevelt Presidential Library | young, teddy | 735 |
| hotel 1883 | /visit/lodging | Lodging / Theodore Roosevelt Presidential Library | hotel, 1883 | 733 |
| how old was teddy roosevelt when he became president | /tr/timeline | Timeline of TR’s Life / Theodore Roosevelt Presidential Library | old, was, teddy, he, became, president | 703 |

### Losing clicks vs prior 28 days (check seasonality first)
| Type | Search/page | Clicks | Prior | Change |
|---|---|---|---|---|
| page | /tickets?utm_source=gbp&utm_medium=organic | 180 | 13386 | -98.7% |
| page | /tickets | 3646 | 8583 | -57.5% |
| page | / | 8695 | 13567 | -35.9% |
| query | theodore roosevelt presidential library | 5705 | 9962 | -42.7% |
| query | teddy roosevelt presidential library | 1975 | 4219 | -53.2% |
| page | /visit | 1474 | 3583 | -58.9% |
| query | teddy roosevelt library | 1813 | 3403 | -46.7% |
| query | theodore roosevelt library | 1131 | 2623 | -56.9% |
| page | /visit/hours | 507 | 1342 | -62.2% |
| page | /visit/directions | 628 | 1282 | -51.0% |
| page | /tr/tr-mount-rushmore | 454 | 916 | -50.4% |
| query | roosevelt library | 263 | 587 | -55.2% |
| query | roosevelt library north dakota | 279 | 572 | -51.2% |
| query | roosevelt presidential library | 316 | 580 | -45.5% |
| page | /visit/eat | 170 | 364 | -53.3% |

### Our pages competing for the same search
| Search | Impr. | Pages |
|---|---|---|
| square deal | 77571 | /tr/square-deal (pos 4.5), /tr/presidency/square-deal (pos 5.2) |
| theodore roosevelt | 16686 | / (pos 12.4), /bullet-speech (pos 3.0), /tr/family/fdr-connection (pos 3.0), /tr/tr-shot (pos 3.0) |
| kermit roosevelt | 10278 | /podcast/good-citizen/kermit-roosevelt-iii (pos 7.4), /about/trustees/kermit-roosevelt (pos 7.2) |
| roosevelt family | 10096 | /tr/family/family-tree (pos 3.2), /tr/family (pos 4.9), /tr/family/fdr-connection (pos 1.6) |
| bull moose party | 6899 | /tr/post-presidency/bull-moose (pos 3.1), /tr/post-presidency/bull-moose/platform (pos 6.7) |
| the man in the arena | 5546 | /tr/speeches/man-in-the-arena (pos 5.1), /tr/post-presidency/man-in-the-arena (pos 8.6) |
| teddy roosevelt museum | 4092 | / (pos 1.8), /tickets (pos 2.4), /visit (pos 2.4), /video/view/Vf8ee-gccpc (pos 5.8) |
| the square deal | 3777 | /tr/square-deal (pos 2.2), /tr/presidency/square-deal (pos 6.2) |
| presidential library medora | 2263 | / (pos 1.2), /visit (pos 1.8), /tickets (pos 1.8), /visit/hours (pos 1.8) |
| bamie roosevelt | 2047 | /tr/early-life/siblings (pos 7.2), /tr/people/bamie (pos 6.1), /quiz/mothers-day (pos 10.1), /tr/people (pos 12) |
| what was a square deal | 1967 | /tr/square-deal (pos 1.5), /tr/presidency/square-deal (pos 7.8) |
| teddy roosevelt shot | 1854 | /tr/tr-shot (pos 2.3), /bullet-speech (pos 5.3) |
| theodore roosevelt museum | 1718 | / (pos 1.9), /tickets (pos 2.3), /visit (pos 2.3), /visit/directions (pos 3.4) |
| square deal definition us history | 1512 | /tr/square-deal (pos 1.6), /tr/presidency/square-deal (pos 4.9) |
| teddy roosevelt assassination attempt | 1470 | /bullet-speech (pos 1.9), /tr/tr-shot (pos 6.0) |

## Tracked keywords (dataforseo+gsc)
| Keyword | Group | Volume | GSC pos. | Google rank | AI Overview | Cites us | Above us |
|---|---|---|---|---|---|---|---|
| theodore roosevelt presidential library | Visit | 74000 | 1.1 | 10 | True | False | google.com, google.com, google.com |
| things to do in medora nd | Visit | 1600 | 2.7 | – | True | False | google.com, google.com, google.com |
| medora north dakota attractions | Visit | 1600 | – | – | False | False | google.com, facebook.com, google.com |
| things to do near theodore roosevelt national park | Visit | 50 | – | – | False | False | google.com, google.com, facebook.com |
| museums in north dakota | Visit | 320 | 7.2 | – | False | False | google.com, tripadvisor.ca, google.com |
| north dakota road trip | Visit | 140 | 7.8 | – | True | False | thewalkingtourists.com, google.com, google.com |
| medora nd hotels | Visit | 8100 | 6.4 | – | True | True | expedia.com, google.com, cntraveler.com |
| badlands north dakota | Visit | 5400 | 2 | – | True | False | google.com, google.com, google.com |
| theodore roosevelt | History | 246000 | 9 | – | False | False | google.com, google.com, trumpwhitehouse.archives.gov |
| theodore roosevelt north dakota | History | 320 | 6.2 | – | False | False | google.com, google.com, google.com |
| theodore roosevelt badlands | History | 140 | 6 | – | True | True | nps.gov, nps.gov, google.com |
| elkhorn ranch | History | 2900 | 8.9 | – | False | False | google.com, fws.gov, google.com |
| maltese cross cabin | History | 720 | 65.5 | – | False | False | facebook.com, google.com, google.com |
| theodore roosevelt conservation | History | 590 | 8.1 | – | True | False | trcp.org, google.com, google.com |
| presidential libraries | Presidential libraries | 14800 | 5.3 | – | False | False | georgewbushlibrary.gov, google.com, eisenhowerlibrary.gov |
| newest presidential library | Presidential libraries | 210 | 1.9 | 17 | True | True | google.com, google.com, facebook.com |
| presidential library road trip | Presidential libraries | – | – | 4 | True | False | google.com, google.com, google.com |
| theodore roosevelt quotes | Learning | 6600 | 3.1 | 3 | True | True | goodreads.com, google.com |
| theodore roosevelt man in the arena | Learning | 2400 | 5.4 | – | True | False | google.com, google.com, google.com |
| theodore roosevelt podcast | Learning | 10 | – | 15 | True | True | google.com, google.com, google.com |
| teddy roosevelt national park | Auto: Visit | 8100 | 9.1 | – | False | False | google.com, google.com, google.com |
| enchanted highway | Auto: Visit | 9900 | 8.7 | – | True | False | google.com, tripadvisor.co.nz, theflashnites.com |
| mount rushmore presidents | Auto: Visit | 27100 | 4.7 | – | True | False | gettyimages.com, google.com, google.com |
| teddy roosevelt | Auto: History | 165000 | 6.1 | – | False | False | google.com, google.com, theodoreroosevelt.org |
| theodore roosevelt died | Auto: History | 5400 | 5.2 | – | True | True | google.com, en.wikipedia.org, google.com |
| brownsville affair | Auto: History | 480 | 5.6 | – | True | False | instagram.com, google.com, pioneergirl.com |
| roosevelt corollary | Auto: History | 33100 | 4.7 | – | True | True | gilderlehrman.org, google.com, google.com |
| jacob riis | Auto: History | 33100 | 10.2 | – | False | False | google.com, artsandculture.google.com, nytimes.com |
| alice roosevelt longworth | Auto: Family | 27100 | 8.5 | – | False | False | google.com, google.com, google.com |
| bull moose party | Auto: History | 9900 | 4.4 | – | True | False | google.com, google.com, google.com |

## AI assistant visibility
| Engine | Model | Mentions us | Cites trlibrary.com |
|---|---|---|---|
| ChatGPT | gpt-5-mini | 68.4% | 57.9% |
| Gemini | gemini-3.8-flash | 31.6% | 21.1% |
| Perplexity | fast | – | – |

### Question by question
Some answers failed this week: perplexity: Perplexity 403: {"error":{"message":"The Agent API requires paid credits. Add paid credit at https://console.perplexity.ai to upgrade your o

**I'm visiting Theodore Roosevelt National Park. What else should I see nearby?** (Trip planning)
- ChatGPT: mentioned, #5 among attractions, cites trlibrary.com. Also named: Chateau de Mores, North Dakota Cowboy Hall of Fame, Painted Canyon, Elkhorn Ranch, Maah Daah Hey Trail, Medora Musical. Described as: "([trlibrary.com](https://www.trlibrary.com/visit/national-park/elkhorn-ranch?utm_source=openai))" Sources: medorand.org, home.nps.gov, trlibrary.com, nps.gov, medora.com, parkrec.nd.gov
- Gemini: NOT mentioned. Also named: Theodore Roosevelt National Park, Elkhorn Ranch, North Dakota Cowboy Hall of Fame, Medora Musical, Pitchfork Steak Fondue, Maah Daah Hey Trail. Sources: none

**What are the best things to do in Medora, North Dakota?** (Trip planning)
- ChatGPT: mentioned, #4 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Painted Canyon, Medora Musical, Pitchfork Steak Fondue, Maah Daah Hey Trail, Chateau de Mores, North Dakota Cowboy Hall of Fame. Described as: "- Theodore Roosevelt Presidential Library: a major, immersive museum just outside town (opened in 2026). … ([trlibrary.com](https://www.trlibrary.com/?utm_source=openai))" Sources: nps.gov, medora.com, trlibrary.com, history.nd.gov, medorand.org
- Gemini: NOT mentioned. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Medora Musical, Pitchfork Steak Fondue, North Dakota Cowboy Hall of Fame, Maah Daah Hey Trail. Sources: none

**Plan a 3-day road trip through western North Dakota. What are the must-see stops?** (Trip planning)
- ChatGPT: mentioned, #5 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Painted Canyon, Maltese Cross Cabin, Medora Musical, Maah Daah Hey Trail. Described as: "- Theodore Roosevelt Presidential Library (new major attraction at Medora — opened 2026) — strongly worth a stop if you’re in Medora. … ([trlibrary.com](https://www.trlibrary.com/?utm_source=openai))" Sources: flattestroute.com, nps.gov, medora.com, peacegardenalmanac.com, home.nps.gov, rome2rio.com
- Gemini: NOT mentioned. Also named: Theodore Roosevelt National Park, Medora Musical, Chateau de Mores, North Dakota Cowboy Hall of Fame, Pitchfork Steak Fondue, Maltese Cross Cabin, Painted Canyon. Sources: none

**We're driving from Mount Rushmore to Theodore Roosevelt National Park. What's worth stopping for?** (Trip planning)
- ChatGPT: NOT mentioned. Also named: Mount Rushmore, Theodore Roosevelt National Park, Maah Daah Hey Trail. Sources: medora.com, gfp.sd.gov, en.wikipedia.org, crazyhorsememorial.org, recreation.gov, deadwood.com
- Gemini: NOT mentioned. Also named: Mount Rushmore, Theodore Roosevelt National Park, Chateau de Mores, North Dakota Cowboy Hall of Fame, Pitchfork Steak Fondue, Medora Musical. Sources: none

**What are the best stops along I-94 in North Dakota?** (Trip planning)
- ChatGPT: mentioned, #4 among attractions. Also named: Theodore Roosevelt National Park, Painted Canyon, Medora Musical. Described as: "- Medora / Theodore Roosevelt National Park (South Unit) — gateway to the Painted Canyon overlooks, short rim hikes, abundant badlands scenery, the Medora Musical and the new Theodore Roosevelt Presidential Library area." Sources: nps.gov, ndtourism.com, dickinsongov.com, roadsideamerica.com, discoverjamestownnd.com, maps.roadtrippers.com
- Gemini: NOT mentioned. Also named: Painted Canyon, Theodore Roosevelt National Park, Maltese Cross Cabin, Chateau de Mores, Medora Musical, Pitchfork Steak Fondue. Sources: none

**Fun things to do with kids in the North Dakota Badlands?** (Trip planning)
- ChatGPT: mentioned, #3 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Painted Canyon, Maah Daah Hey Trail. Described as: "([trlibrary.com](https://www.trlibrary.com/visit/activities?utm_source=openai)) … ([trlibrary.com](https://www.trlibrary.com/visit/activities?utm_source=openai))" Sources: home.nps.gov, trlibrary.com, mdhta.com, ndtourism.com, visitdickinson.com, littlewilderness.co
- Gemini: NOT mentioned. Also named: Theodore Roosevelt National Park, Painted Canyon, Medora Musical, Pitchfork Steak Fondue, Maltese Cross Cabin, North Dakota Cowboy Hall of Fame, Chateau de Mores, Maah Daah Hey Trail. Sources: none

**What can we do indoors in Medora if the weather is bad?** (Trip planning)
- ChatGPT: mentioned, #3 among attractions, cites trlibrary.com. Also named: North Dakota Cowboy Hall of Fame, Chateau de Mores, Medora Musical, Pitchfork Steak Fondue. Described as: "- Theodore Roosevelt Presidential Library — a new/expanded indoor museum experience near Medora with multi‑gallery exhibits; plan on a few hours. … ([trlibrary.com](https://www.trlibrary.com/?utm_source=openai))" Sources: medora.com, history.nd.gov, trlibrary.com, discovermedora.com
- Gemini: NOT mentioned. Also named: North Dakota Cowboy Hall of Fame, Chateau de Mores, Theodore Roosevelt National Park, Medora Musical. Sources: medora.com, carltonautstraveltips.com, medorand.org, heatherscompass.com, thewellwornshoes.com, fargomom.com

**What are the best museums in North Dakota?** (Museums)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Described as: "- Theodore Roosevelt Presidential Library / Visitor complex (Medora area) — a major new TR center and exhibits about Roosevelt’s Badlands years and conservation legacy. … ([trlibrary.com](https://www.trlibrary.com/visit/activities?utm_source=openai))" Sources: statemuseum.nd.gov, plainsart.org, ndmoa.com, bonanzaville.org, dickinsongov.com, trlibrary.com
- Gemini: NOT mentioned. Also named: North Dakota Cowboy Hall of Fame, Theodore Roosevelt National Park, Chateau de Mores. Sources: none

**What is the newest presidential library in the United States?** (Museums)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Described as: "The Theodore Roosevelt Presidential Library in Medora, North Dakota — it opened to the public on July 4, 2026. … ([trlibrary.com](https://www.trlibrary.com/about/press/press-releases/theodore-roosevelt-presidential-library-opening-celebrations-july-4-2026?utm_source=openai))" Sources: trlibrary.com
- Gemini: mentioned, #1 among attractions. Also named: Theodore Roosevelt National Park. Described as: "* **Theodore Roosevelt Presidential Library (Medora, North Dakota)**: Opened on **July 4, 2026**, this facility is built into the North Dakota Badlands near Theodore Roosevelt National Park. … Similarly, the Theodore Roosevelt Presidential Library is independent, as Theodore Roosevelt served before the Presidential Libraries Act (his physical papers are primarily housed at the Library of Congress)." Sources: fastcompany.com, wikipedia.org, cbsnews.com, obama.org

**Which presidential libraries are worth visiting?** (Museums)
- ChatGPT: mentioned, #1 among attractions. Described as: "Roosevelt Presidential Library & Museum — Hyde Park, NY" Sources: none
- Gemini: mentioned, #1 among attractions. Described as: "Roosevelt Presidential Library and Museum (Hyde Park, New York)" Sources: none

**Where can I learn about Theodore Roosevelt's life in North Dakota?** (History)
- ChatGPT: mentioned, #4 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Elkhorn Ranch, Maltese Cross Cabin. Described as: "- Theodore Roosevelt Presidential Library (Medora) — a museum in/near Medora that tells Roosevelt’s life story with exhibits focused on his Badlands years; it’s sited to pair with visits to the park and the Maltese Cross Cabin. … ([trlibrary.com](https://www.trlibrary.com/?utm_source=openai))" Sources: nps.gov, home.nps.gov, trlibrary.com, theodorerooseveltcenter.org, statemuseum.nd.gov
- Gemini: mentioned, #4 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Elkhorn Ranch, Chateau de Mores, North Dakota Cowboy Hall of Fame. Described as: "* **The Theodore Roosevelt Presidential Library (Medora, ND)**" Sources: trlibrary.com, ndtourism.com, wikipedia.org, theodorerooseveltcenter.org, dsuheritagefoundation.org, bigsea.co

**What historic sites are connected to Theodore Roosevelt?** (History)
- ChatGPT: NOT mentioned. Also named: Theodore Roosevelt National Park, Elkhorn Ranch, Maltese Cross Cabin. Sources: none
- Gemini: NOT mentioned. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Elkhorn Ranch, Mount Rushmore. Sources: none

**Is the Theodore Roosevelt Presidential Library worth visiting?** (Brand)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Medora Musical. Described as: "history, the outdoors, or museum experiences that connect place and story, the Theodore Roosevelt Presidential Library in Medora, ND is worth a visit. … ([trlibrary.com](https://www.trlibrary.com/visit/exhibits/main?utm_source=openai))" Sources: prnewswire.com, trlibrary.com, snohetta.prezly.com
- Gemini: mentioned, #1 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Medora Musical. Described as: "**Yes, the Theodore Roosevelt Presidential Library is well worth a visit**, especially if you are interested in American history, innovative architecture, or are already planning a trip to the Northern Plains." Sources: nd.gov, ndtourism.com, wikipedia.org, trlibrary.com, visitdickinson.com

**How much time do I need at the Theodore Roosevelt Presidential Library?** (Brand)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Also named: Medora Musical. Described as: "([trlibrary.com](https://www.trlibrary.com/visit/hours?utm_source=openai)) … ([trlibrary.com](https://www.trlibrary.com/visit/faq/tickets?utm_source=openai))" Sources: trlibrary.com
- Gemini: mentioned, #1 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park. Described as: "You should plan to spend about **3 to 4 hours** (roughly a half-day) at the Theodore Roosevelt Presidential Library in Medora, North Dakota." Sources: peacegardenalmanac.com, shebuystravel.com, ndtourism.com, trlibrary.com, nd.gov

**How much are tickets to the Theodore Roosevelt Presidential Library and when is it open?** (Brand)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Described as: "([trlibrary.com](https://www.trlibrary.com/tickets)) … ([trlibrary.com](https://www.trlibrary.com/visit/hours))" Sources: trlibrary.com
- Gemini: mentioned, #1 among attractions, cites trlibrary.com. Described as: "The **Theodore Roosevelt Presidential Library** in Medora, North Dakota, operates with the following admission prices and hours:" Sources: ndtourism.com, trlibrary.com, peacegardenalmanac.com

**What were Theodore Roosevelt's major accomplishments, conservation work, and legacy?** (Auto: History)
- ChatGPT: NOT mentioned. Sources: none
- Gemini: NOT mentioned. Also named: Mount Rushmore. Sources: none

**Can you explain Theodore Roosevelt's Square Deal domestic policy and its main goals?** (Auto: History)
- ChatGPT: NOT mentioned. Sources: none
- Gemini: NOT mentioned. Sources: none

**What years was Theodore Roosevelt in office, and what were the major milestones of his administration?** (Auto: History)
- ChatGPT: NOT mentioned. Sources: none
- Gemini: NOT mentioned. Sources: none

**Which presidents are carved on Mount Rushmore, and why was Theodore Roosevelt included?** (Auto: History)
- ChatGPT: NOT mentioned. Also named: Mount Rushmore. Sources: none
- Gemini: NOT mentioned. Also named: Mount Rushmore. Sources: none

### Sites AI assistants cite most
trlibrary.com (15), ndtourism.com (9), nps.gov (7), home.nps.gov (6), medora.com (6), medorand.org (4), history.nd.gov (3), peacegardenalmanac.com (3), wikipedia.org (3), parkrec.nd.gov (2), dickinsongov.com (2), visitdickinson.com (2), discovermedora.com (2), statemuseum.nd.gov (2), theodorerooseveltcenter.org (2)

## Site audit
Crawled 1130 of 1169 sitemap URLs. Health 96/100, AI readiness 60/100. llms.txt on trlibrary.com: no. AI crawlers blocked in robots.txt: none. 404 pages have page-specific structured data (sitewide on every page: BreadcrumbList, EntryPoint, GeoCoordinates, ImageObject, ListItem, OpeningHoursSpecification, PostalAddress, SearchAction, WebSite).

| Severity | Issue | Pages | Examples |
|---|---|---|---|
| medium | Same title as another page | 74 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /calendar/special-event/book-signing-and-meet-greet-kennerly-balkowitsch-and-ziemendorf, /visit/exhibits/kennerly |
| medium | Sitemap lists a /node/ URL instead of a readable path | 35 | /node/240, /node/241, /node/244, /node/245, /node/249 |
| medium | Missing Open Graph tags | 32 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /calendar/special-event/book-signing-and-meet-greet-kennerly-balkowitsch-and-ziemendorf, /birthdaycard |
| medium | No meta description | 31 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /calendar/special-event/book-signing-and-meet-greet-kennerly-balkowitsch-and-ziemendorf, /birthdaycard |
| medium | No H1 heading | 29 | /birthdaycard, /project/how-the-library-works, /rsvp/midwinter, /privacy, /newsletter |
| medium | Sitemap lists a URL that redirects | 5 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /calendar/special-event/book-signing-and-meet-greet-kennerly-balkowitsch-and-ziemendorf, /event/24 |
| low | Title over 60 characters, not counting the site-name suffix | 263 | /node/240, /node/241, /node/244, /node/245, /node/249 |
| low | Under 150 words of body text | 239 | /birthdaycard, /project/how-the-library-works, /node/240, /node/241, /node/244 |
| low | Title under 15 characters, not counting the site-name suffix | 149 | /birthdaycard, /quiz/the-boardwalk, /join-us, /video/view/Y3jQTzNVVFY, /video/view/YJ_qzszUZUA |
| low | Same meta description as another page | 126 | /event/24, /video/view/Y3jQTzNVVFY, /video/view/YJ_qzszUZUA, /video/view/-udCxePoWgE, /video/view/1ftA6rWo1NA |
| low | Meta description under 70 characters | 18 | /video/view/Y3jQTzNVVFY, /video/view/YJ_qzszUZUA, /video/view/Lk8bs9ilpLI, /video/view/0NiRkijqLGw, /video/view/NoLhSWhiCpA |
| low | More than one H1 | 10 | /support/matching-gifts, /about/careers, /about/mission, /about/foundation, /impact |
| low | Took over 3 seconds to respond | 3 | /video/view/gjy4XjgMEVU, /video/view/GHM7Y66lCBk, /video/view/CGc6w5ryVHk |

## Recently changed pages (held back from recommendations for 28 days)
Before = the 28 days before the change; after = the days since, up to the latest settled Search Console day. Compare per-day numbers; a week or two after a change is still early.

| Page | Changed | What | Clicks/day before → after | CTR | Position |
|---|---|---|---|---|---|
| /tr/presidency | 2026-11-03 | Published Oct 18 draft plus 2 internal links (Taft, midnight forests) | 0.9 → 3.0 | 0.6% → 0.8% | 6.3 → 5.4 |
| /tr/timeline | 2026-11-03 | Added 6 internal links from Links to add; Title 'Theodore Roosevelt's Life Timeline: Key D | 7.8 → 11.0 | 0.5% → 0.5% | 7.4 → 5.3 |
| /visit/exhibits/main | 2026-11-03 | Added 6 internal links from Links to add | 2.8 → 4.0 | 1.8% → 2.0% | 6.5 → 6.2 |
| /tr/teddy-nickname | 2026-11-03 | Added 6 internal links from Links to add; Merged /tr/myths/teddy-name into this page; new  | 4.8 → 3.0 | 0.8% → 0.4% | 4.4 → 3.7 |
| /tr/presidency-timeline | 2026-11-03 | Added 6 internal links from Links to add; Title 'When Was Theodore Roosevelt President? 19 | 11.5 → 19.0 | 0.6% → 0.7% | 4.6 → 4.0 |
| /tr/people/henry-cabot-lodge | 2026-11-03 | Added 6 internal links from Links to add | 1.1 → 5.0 | 0.2% → 0.8% | 6.5 → 6.0 |
| /tr/family/family-tree | 2026-11-03 | Added 5 internal links from Links to add | 14.2 → 17.0 | 1.5% → 1.7% | 5.2 → 5.8 |
| /tr/presidency/white-house-family | 2026-11-03 | Added 4 internal links from Links to add | 0.2 → 0.0 | 0.3% → 0.0% | 6.6 → 7.3 |
| /podcast/good-citizen/doris-kearns-goodwin-presidential-stories-trpl-and-enduring-lessons-theodore | 2026-11-03 | Added 5 internal links from Links to add | 0.3 → 1.0 | 0.8% → 2.6% | 8.8 → 7.6 |
| /tr/legacy/rankings | 2026-11-03 | Added 5 internal links from Links to add | 5.0 → 16.0 | 1.5% → 2.3% | 5.6 → 5.5 |
| /podcast/good-citizen/edward-okeefe | 2026-11-03 | Added 4 internal links from Links to add | 0.1 → 0.0 | 0.8% → 0.0% | 8.2 → 7.7 |
| /podcast/good-citizen/call-adventure-charlie-melcher-ed-okeefe-and-brand-new-theodore-roosevelt | 2026-11-03 | Added 6 internal links from Links to add | 0.3 → 0.0 | 1.1% → 0.0% | 7.4 → 11.6 |
| /tr/for-educators/high-school | 2026-11-03 | Added 6 internal links from Links to add | 0.8 → 2.0 | 1.8% → 3.0% | 7.0 → 6.6 |
| /about/press/press-releases/theodore-roosevelts-groundbreaking-firsts-and-feats-celebration | 2026-11-03 | Added 6 internal links from Links to add | 0.1 → 0.0 | 1.1% → 0.0% | 4.7 → 4.1 |
| /tr/rise-to-power/ten-facts | 2026-11-03 | Added 6 internal links from Links to add | 3.3 → 9.0 | 1.6% → 2.9% | 5.3 → 3.5 |
| /tr/presidency/ten-facts | 2026-11-03 | Added 5 internal links from Links to add | 15.5 → 19.0 | 2.8% → 2.3% | 3.9 → 3.5 |
| /events/teddycon | 2026-11-03 | Added 6 internal links from Links to add | 3.4 → 1.0 | 8.8% → 3.5% | 3.8 → 8.7 |
| /tr/badlands-timeline | 2026-11-03 | Added 6 internal links from Links to add | 5.7 → 4.0 | 2.0% → 1.5% | 5.5 → 4.8 |
| /tr/family/fdr-connection | 2026-11-03 | Added 4 internal links from Links to add; Title 'How Were Theodore and Franklin Roosevelt  | 60.9 → 78.0 | 1.9% → 1.8% | 3.2 → 3.1 |
| /research/archives | 2026-11-03 | Added 5 internal links from Links to add | 1.7 → 3.0 | 2.5% → 6.1% | 7.7 → 7.0 |
| /tr/speeches/new-nationalism | 2026-11-03 | Added 5 internal links from Links to add | 1.7 → 0.0 | 2.0% → 0.0% | 5.6 → 6.9 |
| /tr/presidency/elections | 2026-11-03 | Added 4 internal links from Links to add; Title '1904 Presidential Election: Roosevelt's M | 4.5 → 6.0 | 0.6% → 0.5% | 5.9 → 6.2 |
| /tr/legacy/the-library | 2026-11-03 | Added 5 internal links from Links to add | 1.2 → 0.0 | 1.0% → 0.0% | 5.0 → 4.3 |
| /tr/post-presidency/ten-facts | 2026-11-03 | Added 5 internal links from Links to add | 0.4 → 0.0 | 1.0% → 0.0% | 5.5 → 4.9 |
| /visit/medora/history | 2026-11-03 | Added 5 internal links from Links to add; North Dakota quote aligned to the 1918 Volwiler  | 1.2 → 0.0 | 1.2% → 0.0% | 7.4 → 7.2 |
| /tr/fake-quotes | 2026-11-03 | Added 3 internal links from Links to add | 11.7 → 17.0 | 2.0% → 2.7% | 6.8 → 5.7 |
| /tr/kids-timeline | 2026-11-03 | Added 5 internal links from Links to add; Title 'Theodore Roosevelt for Kids: A Timeline o | 2.5 → 0.0 | 0.7% → 0.0% | 9.4 → 9.1 |
| /tr/tr-mount-rushmore | 2026-11-03 | Added 3 internal links from Links to add; Title 'Mount Rushmore Presidents: Why Theodore R | 16.0 → 19.0 | 0.4% → 0.3% | 5.5 → 5.7 |
| /visit/directions | 2026-11-03 | Added 4 internal links from Links to add; Title 'Directions to Medora from I-94 and Nearby | 21.1 → 5.0 | 1.2% → 0.5% | 2.7 → 2.9 |
| /tr/books-and-writings/autobiography | 2026-11-03 | Added 4 internal links from Links to add | 1.1 → 2.0 | 1.3% → 3.1% | 5.7 → 4.5 |
| /tr/pre-presidency-political-accomplishments | 2026-11-03 | Added 4 internal links from Links to add; Title 'What Did Theodore Roosevelt Do Before He  | 20.5 → 26.0 | 1.1% → 0.9% | 5.6 → 5.1 |
| /tr/books-and-writings/complete-list | 2026-11-03 | Added 4 internal links from Links to add | 0.2 → 0.0 | 1.9% → 0.0% | 5.4 → 5.6 |
| /tr/quotes/leadership | 2026-11-03 | Added 5 internal links from Links to add | 3.6 → 4.0 | 3.0% → 2.9% | 5.4 → 5.4 |
| /tr/speeches/inaugural | 2026-11-03 | Added 4 internal links from Links to add | 0.5 → 0.0 | 0.5% → 0.0% | 5.7 → 5.7 |
| /podcast/good-citizen/candice-millard | 2026-11-03 | Added 2 internal links from Links to add | 0.4 → 1.0 | 0.3% → 0.3% | 9.3 → 11.0 |
| /tr/people/eleanor | 2026-11-03 | Added 4 internal links from Links to add | 0.4 → 1.0 | 0.5% → 0.5% | 6.9 → 6.6 |
| /tr/people/bill-sewall | 2026-11-03 | Added 4 internal links from Links to add | 0.6 → 0.0 | 2.2% → 0.0% | 5.5 → 4.7 |
| /tr/post-presidency/quentin | 2026-11-03 | Added 4 internal links from Links to add | 1.0 → 1.0 | 0.4% → 0.4% | 9.5 → 8.9 |
| /tr/quotes/conservation | 2026-11-03 | Added 2 internal links from Links to add | 3.4 → 7.0 | 1.9% → 4.5% | 5.3 → 4.5 |
| /podcast/good-citizen/karl-rove-historic-redemption-hard-work-politics-and-essential-nature | 2026-11-03 | Added 3 internal links from Links to add | 1.8 → 3.0 | 0.1% → 0.1% | 9.2 → 9.3 |
| /tr/early-life/siblings | 2026-11-03 | Added 3 internal links from Links to add | 1.2 → 0.0 | 1.2% → 0.0% | 6.3 → 5.3 |
| /tr/early-life/ten-facts | 2026-11-03 | Added 4 internal links from Links to add | 0.4 → 1.0 | 3.6% → 2.0% | 5.4 → 4.2 |
| /tr/people/kermit | 2026-11-03 | Added 4 internal links from Links to add | 0.2 → 0.0 | 0.4% → 0.0% | 8.6 → 8.0 |
| /tr/legacy | 2026-11-03 | Added 3 internal links from Links to add | 0.1 → 1.0 | 0.8% → 2.2% | 8.8 → 2.6 |
| /tr/people/bamie | 2026-11-03 | Added 3 internal links from Links to add | 0.2 → 1.0 | 0.5% → 1.9% | 6.0 → 8.4 |
| /tr/early-life | 2026-11-03 | Added 3 internal links from Links to add | 5.2 → 14.0 | 0.9% → 2.0% | 6.7 → 4.8 |
| /podcast/good-citizen/jeffrey-rosen | 2026-11-03 | Added 3 internal links from Links to add | 0.2 → 0.0 | 0.3% → 0.0% | 10.2 → 8.9 |
| /tr/complex-legacy/imperialism | 2026-11-03 | Added 2 internal links from Links to add | 8.3 → 13.0 | 1.0% → 0.7% | 5.2 → 5.2 |
| /tr/strenuous-life/hunter | 2026-11-03 | Added 3 internal links from Links to add | 1.2 → 1.0 | 0.9% → 0.7% | 5.6 → 5.2 |
| /tr/tr-shot | 2026-11-03 | Added 3 internal links from Links to add; Title 'Why Was Theodore Roosevelt Shot? The 1912 | 11.4 → 6.0 | 0.9% → 0.5% | 4.0 → 4.2 |
| /visit/itineraries/chicago-badlands | 2026-11-03 | Added 2 internal links from Links to add; Visit length and restaurant name | 0.8 → 0.0 | 1.6% → 0.0% | 6.9 → 6.0 |
| /tr/post-presidency/death | 2026-11-03 | Added 3 internal links from Links to add | 2.8 → 4.0 | 0.5% → 0.4% | 5.5 → 4.6 |
| /tr/new-york-politics/alice-lee | 2026-11-03 | Added 3 internal links from Links to add | 3.0 → 2.0 | 0.8% → 0.5% | 5.5 → 5.3 |
| /tr/square-deal | 2026-11-03 | Added 2 internal links from Links to add; Archived (node 278); 301 to /tr/presidency/squar | 31.8 → 0.0 | 0.8% → 0.0% | 3.9 → 1.6 |
| /tr/rise-to-power/edith-roosevelt | 2026-11-03 | Added 3 internal links from Links to add | 1.5 → 4.0 | 0.4% → 1.1% | 6.9 → 7.0 |
| /tr/presidency/conservation/midnight-forests | 2026-11-03 | Added 3 internal links from Links to add | 1.1 → 4.0 | 1.3% → 3.6% | 5.1 → 5.9 |
| /tr/quotes/misquotes | 2026-11-03 | Added 3 internal links from Links to add | 5.5 → 6.0 | 2.6% → 2.1% | 4.0 → 3.8 |
| /tr/post-presidency/man-in-the-arena | 2026-11-03 | Added 3 internal links from Links to add; Title 'TR's 1910 European Tour and the Man in th | 1.6 → 2.0 | 0.8% → 1.5% | 7.5 → 6.6 |
| /visit/activities | 2026-11-03 | Added 3 internal links from Links to add; Visit length and restaurant name | 0.5 → 0.0 | 0.9% → 0.0% | 5.3 → 9.4 |
| /tr/conservation/by-the-numbers | 2026-11-03 | Added 3 internal links from Links to add | 1.6 → 7.0 | 0.6% → 2.0% | 5.1 → 4.4 |
| /tr/presidency/conservation/gifford-pinchot | 2026-11-03 | Added 2 internal links from Links to add | 1.6 → 6.0 | 0.6% → 1.8% | 4.4 → 4.2 |
| /tr/early-life/family-roots | 2026-11-03 | Added 3 internal links from Links to add | 1.5 → 3.0 | 0.8% → 1.6% | 4.8 → 5.0 |
| /podcast/good-citizen/live-trpl-1-doris-kearns-goodwin-finding-hope-history | 2026-11-03 | Added 3 internal links from Links to add | 0.1 → 1.0 | 0.7% → 6.2% | 8.8 → 8.8 |
| /tr/homes-and-places/sagamore-hill | 2026-11-03 | Added 2 internal links from Links to add | 0.4 → 2.0 | 0.7% → 2.7% | 7.0 → 8.7 |
| /tr/presidency/conservation/national-monuments | 2026-11-03 | Added 3 internal links from Links to add | 0.9 → 1.0 | 0.8% → 0.7% | 5.5 → 4.6 |
| /tr/presidency/white-house-family/pets | 2026-11-03 | Added 3 internal links from Links to add | 2.2 → 2.0 | 1.2% → 0.9% | 5.1 → 4.0 |
| /visit/teddy-trail | 2026-11-03 | Added 3 internal links from Links to add | 0.3 → 0.0 | 1.2% → 0.0% | 6.4 → 6.7 |
| /visit/exhibits | 2026-11-03 | Added 3 internal links from Links to add; Title: Exhibits: Roosevelt’s Life in Eight Chapt | 3.8 → 1.0 | 0.6% → 0.6% | 3.5 → 4.6 |
| /tr/people | 2026-11-03 | Added 3 internal links from Links to add | 0.8 → 0.0 | 0.4% → 0.0% | 7.4 → 7.4 |
| /about/trustees/doris-kearns-goodwin | 2026-11-03 | Added 3 internal links from Links to add | 0.2 → 1.0 | 0.8% → 3.1% | 16.0 → 10.4 |
| /tr/people/william-howard-taft | 2026-11-03 | Added 3 internal links from Links to add | 1.8 → 3.0 | 0.3% → 0.3% | 5.7 → 5.2 |
| /about/press/press-releases/theodore-roosevelt-presidential-library-opening-celebrations-july-4-2026 | 2026-11-03 | Added 3 internal links from Links to add | 1.9 → 0.0 | 2.9% → 0.0% | 4.4 → 4.2 |
| /tr | 2026-11-03 | Added 3 internal links from Links to add | 0.3 → 1.0 | 0.1% → 0.3% | 6.9 → 4.9 |
| /tr/post-presidency | 2026-11-03 | Added 3 internal links from Links to add | 1.8 → 2.0 | 2.6% → 1.4% | 4.2 → 3.1 |
| /tr/new-york-politics/double-tragedy | 2026-11-03 | Added 3 internal links from Links to add | 0.5 → 0.0 | 1.6% → 0.0% | 4.4 → 3.2 |
| /tr/quotes/family | 2026-11-03 | Added 2 internal links from Links to add | 0.3 → 1.0 | 2.3% → 2.6% | 6.2 → 5.2 |
| /tr/people/alice-lee | 2026-11-03 | Added 3 internal links from Links to add | 0.1 → 0.0 | 0.3% → 0.0% | 8.8 → 7.9 |
| /about/press/press-releases/harold-hamm-donates-50-million-trpl | 2026-11-03 | Added 2 internal links from Links to add | 1.7 → 0.0 | 10.5% → 0.0% | 3.1 → 2.6 |
| /tr/people/theodore-sr | 2026-11-03 | Added 2 internal links from Links to add | 0.4 → 4.0 | 0.2% → 2.4% | 6.5 → 5.0 |
| /about/press/press-releases/roosevelt-family-acquires-903-acres-trpl | 2026-11-03 | Added 2 internal links from Links to add | 0.6 → 1.0 | 7.0% → 25.0% | 4.2 → 8.8 |
| /tr/legacy/mount-rushmore | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 2.0 | 0.2% → 1.2% | 7.1 → 7.4 |
| /tr/conservation/quotes | 2026-11-03 | Added 3 internal links from Links to add | 0.5 → 0.0 | 1.4% → 0.0% | 4.9 → 5.5 |
| /visit/itineraries/north-on-29 | 2026-11-03 | Added 2 internal links from Links to add | 0.3 → 0.0 | 0.8% → 0.0% | 7.2 → 6.8 |
| /tr/rise-to-power/police-commissioner | 2026-11-03 | Added 2 internal links from Links to add | 1.8 → 0.0 | 1.7% → 0.0% | 5.7 → 5.8 |
| /tr/legacy/words-he-coined | 2026-11-03 | Added 2 internal links from Links to add | 0.9 → 0.0 | 0.6% → 0.0% | 6.4 → 7.4 |
| /tr/myths/misquotes | 2026-11-03 | Added 2 internal links from Links to add | 1.1 → 1.0 | 1.1% → 0.6% | 5.2 → 5.1 |
| /tr/quotes | 2026-11-03 | Added 2 internal links from Links to add | 21.7 → 21.0 | 2.3% → 2.4% | 10.7 → 4.3 |
| /tr/presidency/first-term | 2026-11-03 | Added 2 internal links from Links to add | 0.5 → 1.0 | 1.7% → 1.7% | 6.5 → 4.4 |
| /visit/itineraries/13-day-denver-wyoming | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.8% → 0.0% | 8.9 → 8.1 |
| /tr/family/children | 2026-11-03 | Added 2 internal links from Links to add; Title 'Theodore Roosevelt's Children: Alice, Ted | 4.2 → 11.0 | 1.1% → 2.4% | 4.2 → 3.0 |
| /visit/shopping | 2026-11-03 | Added 2 internal links from Links to add | 5.0 → 2.0 | 2.2% → 2.6% | 5.0 → 8.5 |
| /tr/family | 2026-11-03 | Added 2 internal links from Links to add | 1.1 → 0.0 | 0.4% → 0.0% | 8.0 → 7.4 |
| /tr/for-educators/middle-school | 2026-11-03 | Added 2 internal links from Links to add | 0.6 → 2.0 | 2.2% → 4.0% | 6.5 → 5.5 |
| /visit/medora | 2026-11-03 | Added 1 internal link from Links to add | 1.1 → 0.0 | 0.7% → 0.0% | 4.5 → 4.3 |
| /tr/rise-to-power/buffalo-soldiers | 2026-11-03 | Added 1 internal link from Links to add | 1.6 → 2.0 | 0.7% → 0.8% | 5.2 → 4.9 |
| /tr/early-life/harvard | 2026-11-03 | Added 2 internal links from Links to add | 0.9 → 2.0 | 1.0% → 1.6% | 5.4 → 5.5 |
| /tr/elkhorn | 2026-11-03 | Added 2 internal links from Links to add | 1.6 → 2.0 | 0.8% → 1.2% | 8.0 → 7.1 |
| /podcast/good-citizen/ted-leonsis | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 1.0 | 0.2% → 0.4% | 10.0 → 9.4 |
| /tr/presidency/conservation/national-parks | 2026-11-03 | Added 2 internal links from Links to add | 6.9 → 4.0 | 0.9% → 0.4% | 6.0 → 5.2 |
| /bullet-speech | 2026-11-03 | Added 1 internal link from Links to add; Title 'The Bullet Speech: Roosevelt's Assassinati | 24.4 → 25.0 | 1.7% → 1.3% | 3.7 → 3.5 |
| /tr/early-life/mother | 2026-11-03 | Added 2 internal links from Links to add | 0.3 → 0.0 | 0.3% → 0.0% | 5.1 → 4.4 |
| /tr/post-presidency/river-of-doubt | 2026-11-03 | Added 2 internal links from Links to add | 2.6 → 7.0 | 0.6% → 1.0% | 7.5 → 6.9 |
| /tr/post-presidency/african-safari | 2026-11-03 | Added 2 internal links from Links to add | 1.2 → 1.0 | 1.3% → 1.8% | 5.9 → 7.0 |
| /tr/post-presidency/new-nationalism | 2026-11-03 | Added 2 internal links from Links to add | 1.8 → 0.0 | 0.7% → 0.0% | 4.5 → 4.0 |
| /tr/presidency/conservation/reclamation | 2026-11-03 | Added 2 internal links from Links to add | 3.3 → 5.0 | 0.8% → 1.0% | 4.2 → 3.8 |
| /tr/5-big-adventures | 2026-11-03 | Added 2 internal links from Links to add | 2.0 → 0.0 | 1.0% → 0.0% | 6.5 → 5.7 |
| /tr/rise-to-power/san-juan-hill | 2026-11-03 | Added 2 internal links from Links to add; Title uses 'Battle of San Juan Hill' | 14.8 → 14.0 | 1.4% → 0.9% | 3.7 → 3.8 |
| /tr/presidency/conservation/bird-reserves | 2026-11-03 | Added 2 internal links from Links to add | 0.8 → 0.0 | 1.5% → 0.0% | 5.4 → 6.0 |
| /podcast/good-citizen/douglas-brinkley | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.1% → 0.0% | 11.9 → 11.2 |
| /tr/people/corinne | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.0 | 0.2% → 0.0% | 4.3 → 3.4 |
| /podcast/good-citizen/eric-liu | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.0 | 0.3% → 0.0% | 7.8 → 6.1 |
| /tr/quotes/strenuous-life | 2026-11-03 | Added 1 internal link from Links to add | 1.8 → 4.0 | 1.3% → 1.9% | 6.3 → 6.2 |
| /tr/quotes/citizenship | 2026-11-03 | Added 2 internal links from Links to add | 1.9 → 3.0 | 1.7% → 2.4% | 5.8 → 5.6 |
| /tr/elkhorn-timeline | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.0 | 1.3% → 0.0% | 8.1 → 7.4 |
| /tr/people/edith-roosevelt | 2026-11-03 | Added 2 internal links from Links to add | 0.4 → 1.0 | 0.7% → 1.7% | 11.3 → 12.5 |
| /visit/roosevelt-in-medora | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.8% → 0.0% | 7.4 → 9.7 |
| /podcast/good-citizen/meg-whitman | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 0.1% → 0.0% | 11.4 → 10.5 |
| /tr/speeches/strenuous-life | 2026-11-03 | Added 1 internal link from Links to add | 2.7 → 4.0 | 1.9% → 4.2% | 5.7 → 3.7 |
| /tr/people/quentin | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.0 | 0.4% → 0.0% | 8.5 → 11.3 |
| /tr/post-presidency/world-war-i | 2026-11-03 | Added 2 internal links from Links to add | 0.2 → 1.0 | 0.5% → 1.3% | 5.4 → 4.3 |
| /tr/rise-to-power/sagamore-hill | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.0 | 0.9% → 0.0% | 6.9 → 8.0 |
| /tr/new-york-politics/convention-1884 | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.0 | 0.9% → 0.0% | 6.7 → 6.3 |
| /about/press/press-releases/sarah-and-ross-perot-jr-foundation-gifts-5-million-theodore-roosevelt | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.9% → 0.0% | 6.4 → 11.0 |
| /about/press/press-releases/theodore-roosevelt-presidential-library-welcomes-doris-kearns-goodwin | 2026-11-03 | Added 2 internal links from Links to add | 0.0 → 0.0 | 0.7% → 0.0% | 5.3 → 3.6 |
| /about/foundation | 2026-11-03 | Added 1 internal link from Links to add | 2.5 → 3.0 | 3.7% → 5.1% | 5.5 → 4.3 |
| /visit/eat | 2026-11-03 | Added 2 internal links from Links to add | 5.8 → 1.0 | 2.7% → 0.9% | 7.2 → 6.8 |
| /visit/maps | 2026-11-03 | Added 1 internal link from Links to add | 1.7 → 1.0 | 0.5% → 3.7% | 3.9 → 3.0 |
| /tr/post-presidency/assassination-attempt | 2026-11-03 | Added 2 internal links from Links to add | 0.8 → 1.0 | 0.6% → 0.8% | 8.0 → 5.7 |
| /research | 2026-11-03 | Added 2 internal links from Links to add | 1.1 → 0.0 | 3.4% → 0.0% | 5.5 → 4.2 |
| /tr/presidency/white-house-family/white-house-gang | 2026-11-03 | Added 2 internal links from Links to add | 0.0 → 0.0 | 1.9% → – | 6.0 → – |
| /tr/presidency/conservation/governors-conference | 2026-11-03 | Added 2 internal links from Links to add | 0.3 → 0.0 | 3.4% → 0.0% | 4.8 → 4.0 |
| /tr/rise-to-power/jacob-riis | 2026-11-03 | Added 1 internal link from Links to add | 1.7 → 7.0 | 0.6% → 1.3% | 4.9 → 4.5 |
| /tr/strenuous-life/explorer | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.0 | 1.1% → 0.0% | 5.0 → 4.1 |
| /tr/presidency/race | 2026-11-03 | Added 2 internal links from Links to add | 3.8 → 4.0 | 1.2% → 1.0% | 4.4 → 3.5 |
| /visit/itineraries | 2026-11-03 | Added 1 internal link from Links to add; Link to the I-94 guide | 2.7 → 4.0 | 1.6% → 2.5% | 6.5 → 6.2 |
| /tr/presidency/executive-power | 2026-11-03 | Added 2 internal links from Links to add | 2.9 → 13.0 | 1.5% → 1.9% | 4.1 → 3.7 |
| /tr/presidency/conservation/national-forests | 2026-11-03 | Added 2 internal links from Links to add | 0.5 → 0.0 | 0.8% → 0.0% | 6.0 → 6.6 |
| /visit/itineraries/black-hills-loop | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 1.0 | 1.0% → 3.3% | 8.3 → 6.5 |
| /visit/itineraries/7-day-billings-bismarck | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 0.5% → 0.0% | 8.6 → 8.0 |
| /tr/10-myths-teddy-bear | 2026-11-03 | Added 1 internal link from Links to add | 5.2 → 8.0 | 0.8% → 1.5% | 5.5 → 5.8 |
| /tr/post-presidency/bull-moose/platform | 2026-11-03 | Added 1 internal link from Links to add | 8.6 → 14.0 | 0.7% → 0.4% | 5.0 → 3.9 |
| /tr/for-educators/elementary | 2026-11-03 | Added 1 internal link from Links to add | 1.2 → 3.0 | 2.5% → 4.7% | 6.2 → 6.1 |
| /tr/people/alice-longworth | 2026-11-03 | Added 1 internal link from Links to add; Title 'Alice Roosevelt Longworth: Theodore Roosev | 3.7 → 2.0 | 0.4% → 0.2% | 8.0 → 7.7 |
| /tr/tr-save-the-bison | 2026-11-03 | Added 1 internal link from Links to add | 2.1 → 3.0 | 1.5% → 1.5% | 5.1 → 4.7 |
| /tr/presidency/trust-busting | 2026-11-03 | Added 1 internal link from Links to add; Title 'What Was Trust-Busting? Roosevelt Takes On | 36.2 → 62.0 | 1.3% → 1.5% | 3.4 → 3.1 |
| /tr/complex-legacy | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.0 | 1.7% → 0.0% | 6.0 → 7.1 |
| /podcast/good-citizen/susan-berfield | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 1.0 | 0.5% → 7.1% | 5.6 → 6.1 |
| /tr/badlands/bad-lands-cow-boy | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 0.3% → 0.0% | 8.6 → 6.7 |
| /tr/presidency/great-white-fleet | 2026-11-03 | Added 1 internal link from Links to add; Title 'The Great White Fleet: Roosevelt's Global  | 6.6 → 19.0 | 0.7% → 1.4% | 4.1 → 3.1 |
| /tr/badlands/ten-facts | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.0 | 1.1% → 0.0% | 5.1 → 4.1 |
| /podcast/good-citizen/susannah-cahalan | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.0 | 0.2% → 0.0% | 9.2 → 10.6 |
| /tr/presidency/bully-pulpit | 2026-11-03 | Added 1 internal link from Links to add; Title 'The Bully Pulpit: Meaning, Origin, and Exa | 5.7 → 15.0 | 0.6% → 0.6% | 4.6 → 3.4 |
| /tr/speeches/man-in-the-arena | 2026-11-03 | Added 1 internal link from Links to add; Title 'Man in the Arena Speech: Citizenship in a  | 25.7 → 73.0 | 2.3% → 3.3% | 5.2 → 5.7 |
| /tr/complex-legacy/eugenics | 2026-11-03 | Added 1 internal link from Links to add | 3.5 → 4.0 | 2.9% → 3.1% | 4.2 → 3.6 |
| /tr/people/jacob-riis | 2026-11-03 | Added 1 internal link from Links to add; Title and description aimed at 'who was Jacob Rii | 16.4 → 36.0 | 0.5% → 1.0% | 6.6 → 6.0 |
| /tr/badlands/maltese-cross | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.0 | 3.1% → 0.0% | 6.5 → 5.6 |
| /tr/people/elliott | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 9.4 → 8.6 |
| /tr/rise-to-power/vice-presidency | 2026-11-03 | Added 1 internal link from Links to add | 1.9 → 2.0 | 0.7% → 0.4% | 5.4 → 4.9 |
| /tr/family/elliott-roosevelt | 2026-11-03 | Added 1 internal link from Links to add | 1.1 → 2.0 | 0.5% → 0.8% | 7.5 → 6.7 |
| /tr/badlands | 2026-11-03 | Added 1 internal link from Links to add; Link to where-to-see | 0.1 → 0.0 | 1.1% → 0.0% | 5.3 → 10.8 |
| /podcast/good-citizen/carly-fiorina | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.4% → 0.0% | 8.7 → 4.1 |
| /tr/badlands/medora | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.4% → 0.0% | 7.8 → 7.2 |
| /virtual | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 5.1% → 0.0% | 6.3 → 9.8 |
| /tr/books-and-writings/reader | 2026-11-03 | Added 1 internal link from Links to add | 1.2 → 0.0 | 1.9% → 0.0% | 5.2 → 4.7 |
| /tr/complex-legacy/race | 2026-11-03 | Added 1 internal link from Links to add | 0.9 → 4.0 | 0.9% → 1.6% | 4.9 → 4.7 |
| /tr/people/john-muir | 2026-11-03 | Added 1 internal link from Links to add | 1.0 → 0.0 | 0.5% → 0.0% | 7.2 → 6.5 |
| /tr/complex-legacy/equestrian-statue | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 1.0 | 1.5% → 1.8% | 5.5 → 5.1 |
| /tr/people/ethel | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.0 | 0.3% → 0.0% | 7.8 → 7.9 |
| /tr/rise-to-power/becoming-president | 2026-11-03 | Added 1 internal link from Links to add | 1.4 → 4.0 | 0.3% → 0.6% | 5.3 → 4.4 |
| /tr/people/ted-jr | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.0 | 0.1% → 0.0% | 10.2 → 10.3 |
| /tr/people/mittie | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.0 | 0.6% → 0.0% | 7.5 → 6.0 |
| /podcast/good-citizen/katherine-gehl | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 1.1% → 0.0% | 8.2 → 8.2 |
| /visit/itineraries/7-day-bismarck-rapid-city | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 1.0 | 0.4% → 1.5% | 8.1 → 8.1 |
| /tr/early-life/childhood-illness | 2026-11-03 | Added 1 internal link from Links to add | 2.3 → 2.0 | 1.8% → 1.0% | 4.0 → 3.6 |
| /tr/presidency/square-deal | 2026-11-03 | Added 1 internal link from Links to add; Truncated description fixed; Three Cs heading; Sp | 20.7 → 87.0 | 0.6% → 1.3% | 4.4 → 2.8 |
| /tr/presidency/conservation/john-muir | 2026-11-03 | Added 1 internal link from Links to add | 3.2 → 6.0 | 1.1% → 1.4% | 4.5 → 3.8 |
| /tr/myths | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.5% → 0.0% | 8.0 → 7.2 |
| /tr/early-life/young-naturalist | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.9% → 0.0% | 4.9 → 5.3 |
| /tr/presidency/cabinet | 2026-11-03 | Added 1 internal link from Links to add | 1.0 → 0.0 | 1.1% → 0.0% | 5.0 → 5.6 |
| /tr/people/booker-t-washington | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.0 | 0.2% → 0.0% | 9.4 → 9.7 |
| /project/design | 2026-11-03 | Added 1 internal link from Links to add | 5.5 → 2.0 | 3.7% → 1.4% | 4.5 → 5.1 |
| /tr/early-life/family-travels | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 1.4% → 0.0% | 5.2 → 4.9 |
| /podcast/good-citizen/adam-met-climate-action-musical-stardom-and-art-building-movement | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 11.5 → 13.8 |
| /tr/conservation | 2026-11-03 | Added 1 internal link from Links to add | 1.1 → 1.0 | 1.0% → 0.9% | 7.2 → 7.1 |
| /tr/speeches/confession-of-faith | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 2.0 | 1.1% → 2.6% | 7.0 → 7.8 |
| /podcast/good-citizen/senator-mitt-romney-formative-moments-presidential-leadership-and-question | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.1% → 0.0% | 7.7 → 6.9 |
| /tr/homes-and-places | 2026-11-03 | Added 1 internal link from Links to add | 1.2 → 1.0 | 1.1% → 0.7% | 5.9 → 5.7 |
| /tr/early-life/civil-war | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 0.6% → 0.0% | 5.1 → 5.1 |
| /tr/early-life/day-in-the-life | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.6% → 0.0% | 6.9 → 8.6 |
| /visit/national-park | 2026-11-03 | Added 1 internal link from Links to add; Visit length, restaurant name; link to where-to-s | 4.4 → 2.0 | 0.6% → 0.4% | 8.1 → 9.0 |
| /tr/people/gifford-pinchot | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 1.0 | 0.9% → 1.4% | 6.3 → 6.7 |
| /tr/post-presidency/bull-moose | 2026-11-03 | Added 1 internal link from Links to add | 5.6 → 10.0 | 0.6% → 0.4% | 4.6 → 4.4 |
| /visit/hiking | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.0 | 0.7% → 0.0% | 7.1 → 6.3 |
| /beam-signing-ceremony | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 7.9 → 5.9 |
| /project/native-plant-project | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.0 | 0.9% → 0.0% | 4.6 → 6.7 |
| /tr/homes-and-places/tr-national-park | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 2.0 | 0.7% → 1.7% | 7.1 → 8.5 |
| /visit/hunting-fishing | 2026-11-03 | Added 1 internal link from Links to add | 0.8 → 2.0 | 1.1% → 3.6% | 7.3 → 5.6 |
| /about/mission | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.0 | 2.3% → 0.0% | 4.7 → 3.1 |
| /tr/rise-to-power/civil-service | 2026-11-03 | Added 1 internal link from Links to add | 2.1 → 1.0 | 0.6% → 0.2% | 5.3 → 5.8 |
| /tr/badlands/elkhorn-ranch | 2026-11-03 | Added 1 internal link from Links to add | 0.6 → 0.0 | 0.8% → 0.0% | 7.6 → 6.2 |
| /visit/stargazing | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.0 | 1.3% → 0.0% | 6.2 → 4.7 |
| /podcast/good-citizen/dr-vivek-murthy-loneliness-staying-human-and-what-true-success-looks | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 1.0% → 0.0% | 10.4 → 9.7 |
| /podcast/good-citizen/secretary-deb-haaland | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 9.0 | 0.9% → 1.4% | 7.5 → 7.3 |
| /visit/itineraries/river-road | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.7% → 0.0% | 7.3 → 8.4 |
| /tr/presidency/white-house-workers | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 1.4% → 0.0% | 6.5 → 7.1 |
| /podcast/good-citizen/matthew-barzun | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.9% → 0.0% | 8.5 → 9.0 |
| /tr/early-life/father | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 0.5% → 0.0% | 6.7 → 7.2 |
| /visit/camping | 2026-11-03 | Added 1 internal link from Links to add | 0.8 → 0.0 | 1.4% → 0.0% | 7.5 → 7.9 |
| /tr/presidency/conservation/antiquities-act | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 0.9% → 0.0% | 6.1 → 7.0 |
| /visit/trolley | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.0 | 1.6% → 0.0% | 6.9 → 7.7 |
| /tr/badlands/landscape | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.0 | 0.6% → 0.0% | 5.9 → 5.3 |
| /visit/little-missouri-river | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.0 | 1.1% → 0.0% | 7.8 → 5.0 |
| /podcast/good-citizen/ben-jealous | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 10.2 → 12.0 |
| /podcast/good-citizen/dan-harris | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 8.8 → 10.5 |
| /visit/outdoors | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 1.4% → 0.0% | 6.6 → 4.1 |
| /visit/biking | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 1.0 | 2.1% → 8.3% | 7.3 → 7.7 |
| /visit/wildlife | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 0.6% → 0.0% | 7.8 → 7.0 |
| /project | 2026-11-03 | Added 1 internal link from Links to add; Title 'Building the Library: Design, Values and S | 5.0 → 2.0 | 0.5% → 0.2% | 2.4 → 2.7 |
| /tr/people/leonard-wood | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.2% → 0.0% | 8.8 → 6.3 |
| /podcast/good-citizen/katharine-hayhoe | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 8.5 → 8.7 |
| /visit/itineraries/weekend-drives/fargo | 2026-11-03 | Added 1 internal link from Links to add | 0.6 → 1.0 | 1.1% → 2.6% | 5.0 → 4.5 |
| /about/press/press-releases/trplf-elects-spencer-zwick-board | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 1.6% → 0.0% | 4.3 → 4.1 |
| /visit/itineraries/weekend-drives/bismarck | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.0 | 1.0% → 0.0% | 5.1 → 3.5 |
| /tr/presidency/second-term | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 2.0 | 1.8% → 8.0% | 6.0 → 3.7 |
| /tr/books-and-writings | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 0.8% → 0.0% | 8.7 → 6.5 |
| /tr/badlands/frontier-life | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 0.8% → 0.0% | 6.5 → 5.4 |
| /about/trustees/beth-laski | 2026-11-03 | Added 1 internal link from Links to add | 0.8 → 1.0 | 8.2% → 16.7% | 9.8 → 2.3 |
| /about/press/press-releases/theodore-roosevelt-presidential-library-launches-good-citizen-podcast | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 5.9 → 2.0 |
| /about/presidential-library-system | 2026-11-03 | Added 1 internal link from Links to add | 0.6 → 0.0 | 2.3% → 0.0% | 6.2 → 6.2 |
| /about/press/press-releases/trplf-announces-100-million-commitments-unlocks-50-million-state | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 2.8% → 0.0% | 4.9 → 4.1 |
| /tr/new-york-politics | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.9% → 0.0% | 7.0 → 7.3 |
| /tr/tr-importance | 2026-11-03 | Title 'What Was Theodore Roosevelt Known For?'; typo fix | 12.9 → 15.0 | 1.0% → 0.8% | 4.9 → 4.4 |
| /visit | 2026-10-27 | Title: Plan Your Visit: Tickets, Hours and Directions; Visit length: about three and a hal | 57.3 → 31.1 | 2.5% → 1.8% | 2.7 → 3.0 |
| /tr/presidency/panama-canal | 2026-10-27 | Title and description: Theodore Roosevelt and the Panama Canal, 1903–1914 | 8.2 → 15.5 | 0.4% → 0.6% | 5.2 → 4.7 |
| /tr/presidency/railroad-regulation | 2026-10-27 | Title names the Hepburn Act and Elkins Act | 3.9 → 5.8 | 0.4% → 0.6% | 4.0 → 3.4 |
| /tr/presidency/coal-strike | 2026-10-27 | Title uses 'Anthracite Coal Strike of 1902' | 7.9 → 6.9 | 0.9% → 0.8% | 4.2 → 2.9 |
| /visit/groups | 2026-10-27 | Visit length changed from about three hours to about three and a half hours | 0.1 → 0.1 | 0.6% → 4.0% | 6.5 → 5.2 |
| /visit/faq/tickets | 2026-10-27 | 'Buy tickets' link fixed (was /visit/tickets, a 404); 301 /visit/tickets -> /tickets | 2.0 → 1.1 | 4.3% → 3.3% | 6.3 → 4.9 |
| /visit/faq | 2026-10-27 | Tickets link fixed (was /visit/tickets, a 404) | 2.1 → 0.6 | 0.8% → 1.7% | 4.7 → 6.7 |
| /tr/presidency/brownsville | 2026-10-20 | Title 'The Brownsville Affair of 1906: What Happened and Why'; Medal of Honor claim and da | 0.9 → 2.3 | 0.0% → 0.1% | 6.3 → 4.5 |
| /tr/presidency/roosevelt-corollary | 2026-10-20 | Title 'Roosevelt Corollary to the Monroe Doctrine, Explained'; stray second H1 section rem | 6.6 → 14.7 | 0.2% → 0.3% | 5.4 → 4.2 |
| /visit/hours | 2026-10-20 | Title 'Hours in Medora: Seasonal Schedule and Last Entry'; visit-length bullet | 27.0 → 13.8 | 1.2% → 1.1% | 2.7 → 2.2 |
| /tr/myths/teddy-name | 2026-10-20 | Archived; 301 to /tr/teddy-nickname | 0.2 → 0.3 | 1.2% → 0.5% | 6.2 → 5.3 |
| / | 2026-10-20 | Description mentions 'Teddy' | 353.1 → 269.4 | 3.8% → 9.4% | 8.0 → 6.6 |
| /visit/itineraries/one-day | 2026-10-20 | Visit length and restaurant name | 3.5 → 2.1 | 4.1% → 3.7% | 3.9 → 3.9 |
| /visit/itineraries/4-days-north-dakota | 2026-10-20 | Visit length and restaurant name | 0.7 → 0.7 | 1.4% → 1.7% | 7.6 → 7.1 |
| /visit/itineraries/seattle-badlands | 2026-10-20 | Visit length and restaurant name | 0.1 → 0.1 | 1.2% → 0.6% | 6.7 → 8.0 |
| /visit/i-94 | 2026-10-20 | New page: Best Stops on I-94 in North Dakota | 0.0 → 0.0 | – → 0.0% | – → 11.0 |
| /tr/badlands/where-to-see | 2026-10-20 | New page: Where to See Theodore Roosevelt's North Dakota | 0.0 → 0.0 | – → – | – → – |

## Drafted recommendations (Gemini (gemini-3.8-flash), 2026-11-02T13:05:54+00:00)
_2 AI claims were dropped because the live page contradicted them._

**AI visibility:** ChatGPT reliably recommends the Library for Medora trips and museum queries, while Gemini overlooks it entirely on regional travel itineraries and both engines miss it on Roosevelt history questions.
- Build road-trip landing pages highlighting drive times between Mount Rushmore, the Black Hills, and Medora, noting the 3 1/2 hour library visit. (medium effort; trlibrary.com/visit/road-trips): Both engines fail to connect travel between Mount Rushmore and Theodore Roosevelt National Park with a stop at the Library.
- Coordinate with North Dakota Tourism (ndtourism.com) and Medora partner sites to add Library entries to family, indoor, and rainy-day directories. (low effort; ndtourism.com and medora.com): Gemini draws heavily from ndtourism.com and medora.com for itinerary answers, causing it to miss the Library across standard travel prompts.
- Publish educational overview pages detailing Roosevelt's life, his conservation milestones, and his presidency. (high effort; trlibrary.com/history): AI engines currently rely on general encyclopedia pages and NPS sites for historical questions, bypassing the Library completely.

**/tr/people/alice-longworth**: High search volume targets Alice as Theodore Roosevelt's daughter and queries about her life and death; clarifying her identity immediately under the title and adding structured quick facts will capture high-intent search traffic and AI summaries.
- Title: Alice Roosevelt Longworth: TR's Outspoken Daughter
- Meta: Explore the life of Alice Roosevelt Longworth, TR's rebellious daughter: White House antics, global diplomacy, and six decades of sharp Washington wit.
- Verify: Verify whether the exact day and month of Alice Roosevelt Longworth's death in 1980 is available in Library records if the team wishes to display more than the year 1980.

**/tr/post-presidency/bull-moose/platform**: Searchers frequently look for basic definitions of the Bull Moose Party and its core beliefs, but the page opens without a quick, direct definition before diving into deep policy analysis.
- Title: Bull Moose Party Platform: 1912 Progressive Beliefs
- Meta: Explore the Bull Moose Party platform of 1912, from women's suffrage and labor laws to direct democracy. See the bold beliefs that reshaped American policy.
- Verify: Confirm that the suggested draft definition text accurately reflects the Library's educational guidelines for describing third parties in US history.

**/tr/presidency/great-white-fleet**: Optimize the page for high-volume definition and purpose queries by shortening the title to under 60 characters and adding a concise definition summary block near the top.
- Title: The Great White Fleet: Roosevelt's Global Voyage
- Meta: Discover why Theodore Roosevelt sent sixteen white battleships on a 43,000-mile world voyage and how the daring journey reshaped American diplomacy.
- Verify: Verify the draft statement that the fleet traveled to twenty ports across six continents (matches existing page text).; Verify whether all sixteen battleships were commissioned battleships of the Atlantic Fleet during the entire departure.; Verify dates: departure on December 16, 1907, and return on February 22, 1909 (matches existing page text).

**/tr/speeches/man-in-the-arena**: Capture high-intent searches for the full speech and its meaning by adding a dedicated transcript download link and an explicit summary of the core message.
- Title: Man in the Arena Speech: Citizenship in a Republic
- Meta: Explore Theodore Roosevelt's famous Man in the Arena passage from his 1910 Sorbonne speech, discover its enduring meaning, and read the full address.
- Verify: Confirm that the Theodore Roosevelt Center at Dickinson State University offers a direct link or downloadable PDF of the complete 'Citizenship in a Republic' transcript before adding direct download links.

**/tr/tr-importance**: This page captures strong search volume for what Theodore Roosevelt was known for and accomplished, but it currently lacks a dedicated summary section answering those high-intent queries directly and omits any connection to visiting the Library in Medora.
- Title: What Was Theodore Roosevelt Known For?
- Meta: Discover what Theodore Roosevelt accomplished, from leading the Rough Riders and protecting 230 million acres of public land to reforming food safety laws.
- Verify: Confirm whether the Library's connection to Theodore Roosevelt National Park should be specifically referenced in visitor-facing context on this page.

**/tr/timeline**: High-volume searches target specific biographical questions like TR's birthplace, early life, and age upon taking office; adding a quick-facts summary at the top and section jump-links will capture these searchers and feed AI answer engines immediately.
- Title: Theodore Roosevelt Timeline: Life and Key Milestones
- Meta: Explore the key dates of Theodore Roosevelt’s life, from his New York childhood and Badlands ranching to the presidency. Walk through his journey here.
- Verify: Verify that all drafted dates and family details (October 27, 1858; September 8, 1883; September 14, 1901; age 42) match the Library's preferred timeline copy.; Verify whether the timeline's final entries include his death date and location, as queries regarding his death receive heavy search traffic but were not in the provided excerpt.

**/tr/presidency/bully-pulpit**: This page attracts thousands of searches for basic definitions and examples of the 'bully pulpit,' but buries the definition in running text. Adding a direct, clear definition and an explicit 'examples' structure will capture high-volume definition queries and AI answer engines.
- Title: The Bully Pulpit: Meaning, Origin, and Examples
- Meta: What did Theodore Roosevelt mean by 'bully pulpit'? Discover the definition, why 'bully' meant 'wonderful,' and how TR used the press to shape the nation.
- Verify: Confirm that nineteenth-century colloquial usage of 'bully' as slang for 'first-rate' or 'excellent' aligns with Library historical standards before publishing definition copy.

**/tr/presidency/elections**: Shorten and front-load the page title to capture dominant 1904 presidential election search traffic, and add explicit summary panels for election candidates, vote counts, and key facts to answer AI search and direct user queries.
- Title: 1904 Presidential Election: Roosevelt's Mandate
- Meta: Discover how Theodore Roosevelt won the 1904 presidential election in a landslide over Alton B. Parker, and why his victory-night pledge changed history.
- Verify: Verify whether Henry G. Davis was Alton B. Parker's official vice-presidential running mate in 1904 before adding him to candidate callout copy.

## Visitor experience (/visit pages)
Findability 44/100, mobile speed 49/100, accessibility 94/100, average reading grade 8.2, 0 facts that disagree between pages.

### Can a first-time visitor find what they need?
| Page | Score | Missing or buried | Biggest fix |
|---|---|---|---|
| /visit | 79 | directions, accessibility, food | Add clear parking instructions to the Directions section and cut the overwhelming directory of regional links at the bottom. |
| /visit/accessibility | 35 | hours, price, buy | Add stroller policy details alongside the wheelchair guidance, as parents frequently check accessibility pages for stroller access. |
| /visit/directions | 61 | visit_length, accessibility, food | Add the recommended 3 1/2-hour visit duration near the top driving section so travelers can properly plan driving stopovers. |
| /visit/eat | 42 | hours, directions, visit_length, accessibility | Add a link or note clarifying Library opening hours and that a typical visit takes about 3 1/2 hours. |
| /visit/faq | 75 |  | Answer the top core questions directly on this hub page—including opening hours, admission prices, and the recommended 3 1/2 hour visit time—so visitors do not have to click through multiple subpages. |
| /visit/faq/tickets | 35 | hours, visit_length, accessibility | State ticket prices and admission tiers directly on this page so visitors do not have to leave the FAQ to learn costs. |
| /visit/groups | 32 | hours, price, directions, accessibility, food | Add essential arrival logistics for tour planners, specifically daily operating hours, bus parking directions, and group drop-off instructions. |
| /visit/hours | 68 | visit_length, accessibility | – |
| /visit/lodging | 14 | hours, price, buy, directions, visit_length, accessibility, food | Add quick jump links at the top so mobile visitors can tap directly to hotels, cabins, or campgrounds without scrolling through an exhaustive directory. |
| /visit/maps | 43 | visit_length, accessibility, food | Add notes on stroller and wheelchair accessibility for the boardwalk and state that exploring the campus takes about 3 1/2 hours. |
| /visit/tickets/plan-ahead | 0 | hours, price, buy, directions, visit_length, accessibility, food | Add the interactive ticket reservation tool alongside links to essential visit details like pricing, operating hours, and directions. |

### Slowest pages on mobile
| Page | Speed /100 | Load (s) |
|---|---|---|
| /visit/itineraries/roosevelt-triangle | 16 | 60.8 |
| /visit/planner | 24 | 8.2 |
| /visit/itineraries/10-day-denver-salt-lake-city | 25 | 52.8 |
| /visit/hiking | 27 | 7.1 |
| /visit/roosevelt-in-medora | 27 | 15.9 |
| /visit/itineraries/weekend-drives | 29 | 17 |
| /visit/directions | 31 | 5.4 |
| /visit/hours | 33 | 12.5 |

### Accessibility problems found
- ARIA `tooltip` elements do not have accessible names.
- Background and foreground colors do not have a sufficient contrast ratio.
- Elements use prohibited ARIA attributes
- Elements with an ARIA `[role]` that require children to contain a specific `[role]` are missing some or all of those required children.
- Heading elements are not in a sequentially-descending order
- Image elements do not have `[alt]` attributes
- Links do not have a discernible name
- List items (`<li>`) are not contained within `<ul>`, `<ol>` or `<menu>` parent elements.
- Touch targets do not have sufficient size or spacing.
- `<frame>` or `<iframe>` elements do not have a title
- `[role]`s are not contained by their required parent element

## Internal links and broken links
0 broken internal addresses (0 links), 1176 links worth adding, 50 pages with no links in, 20 topics with two pages, 42 broken outside links (LinkChecker scan 2026-11-02 04:24 UTC).

### Broken links on trlibrary.com: 301 redirects to add
Add a 301 redirect in Drupal (Configuration > Search and metadata > URL redirects) from each broken address to redirect_to; bulk import: https://seo.labs.trlibrary.com/data/redirects.csv. High confidence = safe; check medium/low first. Ticket-store paths should also be corrected on the page to the full access.trlibrary.com address.

_None._

### Links to add (highest value first; the [[bracketed]] words become the link)
| On page | Context | Link to |
|---|---|---|
| /visit/directions | …cts three iconic destinations of the American West: the Library in Medora, North Dakota , [[Mount Rushmore]] in South Dakota , and Yellowstone National Park in Wyoming . | /tr/tr-mount-rushmore |
| /tr/legacy/rankings | Roosevelt’s enduring popularity is carved in granite at [[Mount Rushmore]], beside Washington, Jefferson, and Lincoln. (Dean Franklin, CC BY-SA) | /tr/tr-mount-rushmore |
| /visit/itineraries | …r and Olympic — along with Devils Tower , the first national monument in the country, and [[Mount Rushmore]]. | /tr/tr-mount-rushmore |
| /tr/legacy/the-library | … is being called the "Theodore Roosevelt Triangle," composed of the Presidential Library, [[Mount Rushmore]] (about four and a half hours south), and Yellowstone National Park (about seven hours wes… | /tr/tr-mount-rushmore |
| /research/archives | …s in this collection include correspondence from Gutzon Borglum regarding the creation of [[Mount Rushmore]], letters examining national politics, and items relating to the history of the Rough Ride… | /tr/tr-mount-rushmore |
| /visit/itineraries/7-day-billings-bismarck | …ed. The route runs through Yellowstone, over the Beartooth Highway, past Devils Tower and [[Mount Rushmore]], and into the North Dakota Badlands that made him. | /tr/tr-mount-rushmore |
| /visit/itineraries/black-hills-loop | …feet wide. Iron Mountain Road covers seventeen miles of tunnels deliberately cut to frame [[Mount Rushmore]], with pigtail bridges spiralling down the grade. In between, Wind Cave protects both the … | /tr/tr-mount-rushmore |
| /visit/itineraries/chicago-badlands | Swing south through the Black Hills. From Medora it is about 5 hours to [[Mount Rushmore]] , Custer State Park and Wind Cave National Park , which Roosevelt made the eighth nationa… | /tr/tr-mount-rushmore |
| /visit/itineraries/north-on-29 | … through the Black Hills rather than back down I 29 — Devils Tower, Custer State Park and [[Mount Rushmore]] are all within reach of the drive south. Our ⁣ covers that ground in detail. | /tr/tr-mount-rushmore |
| /podcast/good-citizen/call-adventure-charlie-melcher-ed-okeefe-and-brand-new-theodore-roosevelt | … I became intrigued is the Roosevelts aren't sitting there saying, "And now here is where [[Mount Rushmore]] II shall be held." I didn't know that could have been what the disposition was that this … | /tr/tr-mount-rushmore |
| /tr/family/fdr-connection | Eleanor Roosevelt was born in 1884, the daughter of [[Elliott Roosevelt]], Theodore's younger brother. Elliott had been brilliant, athletic, and promising in youth… | /tr/family/elliott-roosevelt |
| /tr/legacy/mount-rushmore | [[Mount Rushmore]], the colossal monument carved into the Black Hills of South Dakota, features four preside… | /tr/tr-mount-rushmore |
| /visit/itineraries/13-day-denver-wyoming | Marvel at [[Mount Rushmore]] . | /tr/tr-mount-rushmore |
| /tr/tr-mount-rushmore | …projecting power abroad. His work as a trustbuster, conservationist, and champion of the “[[Square Deal]]” represented the country’s maturity—a confident, reform-minded nation ready to lead the w… | /tr/presidency/square-deal |
| /tr/legacy | The Library, [[Mount Rushmore]], Yellowstone | /tr/tr-mount-rushmore |
| /tr/presidency-timeline | …at the United States would oppose any further colonization in the Western Hemisphere. The [[Roosevelt Corollary]] went a step further, stating that, if necessary, the United States would intervene to res… | /tr/presidency/roosevelt-corollary |
| /tr/tr-mount-rushmore | …oosevelt transformed the United States into a world power. He oversaw construction of the [[Panama Canal]], which linked the Atlantic and Pacific Oceans, and negotiated peace in the Russo-Japanese… | /tr/presidency/panama-canal |
| /tr/family/family-tree | [[Elliott Roosevelt]] (1860–1894), Theodore's younger brother, handsome and athletic but morally troubled. His … | /tr/family/elliott-roosevelt |
| /tr/complex-legacy/imperialism | …on extended well beyond the Philippines. In 1904, he articulated what became known as the [[Roosevelt Corollary]] to the Monroe Doctrine. The original Monroe Doctrine, issued by President James Monroe in… | /tr/presidency/roosevelt-corollary |
| /tr/early-life | …8; nearly lost to asthma; a bedroom museum builder, taxidermy student, and Nile traveler. [[Ten facts]] that map the road to Harvard and beyond. | /tr/rise-to-power/ten-facts |
| /tr/10-myths-teddy-bear | … history blend truth, legend, and charm quite like the tale of Theodore Roosevelt and the [[teddy bear]]. On November 14, 1902, during a hunting trip in Mississippi, Roosevelt refused to shoot a… | /tr/legacy/teddy-bear |
| /tr/teddy-nickname | …im approachable. Children who would never study the intricacies of the Square Deal or the [[Roosevelt Corollary]] still know “Teddy” as the president who saved a bear. The nickname has humanized him for … | /tr/presidency/roosevelt-corollary |
| /tr/presidency-timeline | …great achievement of Theodore Roosevelt’s presidency was facilitating the building of the [[Panama Canal]], a 50-mile-long canal that connected the Atlantic Ocean and the Pacific Ocean. Roosevelt … | /tr/presidency/panama-canal |
| /tr/teddy-nickname | …to make Roosevelt more popular, particularly after the creation of a now familiar toy—the [[teddy bear]]. | /tr/legacy/teddy-bear |
| /tr/timeline | …t in office to travel to a foreign country. When he visited the construction site for the [[Panama Canal]], he rode in a large steam shovel on November 16, 1906, a moment captured by a well-known … | /tr/presidency/panama-canal |
| /tr/presidency/ten-facts | …raordinarily popular, and it has remained a staple of American childhood ever since. The "[[teddy bear]]" is one of the most widely recognized symbols of Roosevelt's presidency, yet it emerged f… | /tr/legacy/teddy-bear |
| /tr/teddy-nickname | …ized: it has made him approachable. Children who would never study the intricacies of the [[Square Deal]] or the Roosevelt Corollary still know “Teddy” as the president who saved a bear. The nick… | /tr/presidency/square-deal |
| /tr/post-presidency/death | … Workers expressed sorrow for the man who had championed their interests and fought for a [[square deal]] for the ordinary citizen. Conservationists mourned the loss of the man who had preserved … | /tr/presidency/square-deal |
| /tr/complex-legacy/imperialism | …arilla, who represented French interests and stood to profit enormously from a successful [[Panama Canal]] deal, engaged in active lobbying—and it was Bunau-Varilla, a Frenchman, who signed the Ha… | /tr/presidency/panama-canal |
| /tr/presidency/elections | …at violated the law, embarked on an ambitious conservation program, and begun work on the [[Panama Canal]]. Roosevelt had also proved his political acumen by building a coalition that united the p… | /tr/presidency/panama-canal |
| /tr/rise-to-power/buffalo-soldiers | The [[Brownsville incident]] became notorious. Civil rights activists and supporters of the African American community… | /tr/presidency/brownsville |
| /tr/presidency-timeline | Theodore Roosevelt displayed America’s power to the world when he sent the [[Great White Fleet]], a force of 16 battleships, to sail around the world. The fleet’s journey lasted 14 month… | /tr/presidency/great-white-fleet |
| /tr/timeline | …st famous speech was given at the Sorbonne in Paris, France, on April 23, 1910. Entitled “[[Citizenship in a Republic]],” it is more popularly known as the “Man in the Arena” speech from its most famous line: … | /tr/speeches/man-in-the-arena |
| /tr/timeline | … a 14-month circumnavigation of the globe. Later known as President Theodore Roosevelt’s “[[Great White Fleet]]” due to their white paint, the ships traveled around the world until February 22, 1909—ju… | /tr/presidency/great-white-fleet |
| /tr/myths/misquotes | …l others have been altered from their original form. This page addresses some of the most [[common misquotes]] and provides the accurate information available. | /tr/quotes/misquotes |
| /visit/exhibits/main | …ort a federal anti-lynching law, stayed silent after the 1906 Atlanta riots, and — in the [[Brownsville affair]] — dishonorably discharged an entire regiment of Black soldiers without trial, staining hi… | /tr/presidency/brownsville |
| /tr/strenuous-life/hunter | The [[teddy bear]] story reveals something important about Roosevelt's character. Despite his reputation as … | /tr/legacy/teddy-bear |
| /tr/legacy/rankings | …, mediating the Russo-Japanese War (for which he won the Nobel Peace Prize), building the [[Panama Canal]], and asserting American interests globally. Whether one approves of American imperialism … | /tr/presidency/panama-canal |
| /tr/presidency-timeline | Theodore Roosevelt ran for his second term in the [[election of 1904]] with running mate Charles W. Fairbanks of Indiana against Democrat Alton B. Parker and ru… | /tr/presidency/elections |
| /tr/legacy/words-he-coined | Perhaps Roosevelt's most important political phrase was "the [[Square Deal]]"—his promise to American citizens that government would ensure fair dealing among all cla… | /tr/presidency/square-deal |

### Pages nothing links to
| Page | Title | Impr. |
|---|---|---|
| /tr/tr-mount-rushmore | WHY IS THEODORE ROOSEVELT ON MOUNT RUSHMORE? | 114372 |
| /tr/pre-presidency-political-accomplishments | WHAT WERE THEODORE ROOSEVELT’S FIVE SIGNIFICANT ACCOMPLISHMENTS PRIOR TO BECOMING PRESIDENT? | 54085 |
| /tr/tr-importance | WHY IS THEODORE ROOSEVELT IMPORTANT? | 38657 |
| /tr/10-myths-teddy-bear | TOP 10 MYTHS ABOUT THEODORE ROOSEVELT + THE INVENTION OF THE TEDDY BEAR | 22351 |
| /tr/fake-quotes | DID TR REALLY SAY THAT? | 16886 |
| /about/trustees/edward-okeefe | Edward O’Keefe | 7614 |
| /research/books-by-roosevelt | TR's Published Books | 5923 |
| /tr/5-big-adventures | TR’S FIVE BIG POST-PRESIDENTIAL ADVENTURES | 5692 |
| /tr/tr-save-the-bison | DID THEODORE ROOSEVELT SAVE THE BISON? | 4053 |
| /visit/medora/history | History of Medora | 2925 |
| /programs | Programs | 2357 |
| /research/archives | Archives | 1981 |
| /join-us | Join Us | 1464 |
| /events/teddycon | Theodore Roosevelt Convention (#TeddyCon) | 1153 |
| /visit/exhibits/kennerly | In the Room: Sixty Years on the Front Lines of History | 796 |
| /visit/exhibits/artificial-intelligence | Artificial Intelligence and Responsible Stewardship | 735 |
| /visit/maps/campus | Campus Map / Theodore Roosevelt Presidential Library | 601 |
| /visit/teddy-trail | The Teddy Trail | 566 |
| /digital-guide | Free Digital Guide | 435 |
| /visit/roosevelt-in-medora | Roosevelt in Medora | 363 |
| /visit/groups | Group Reservations | 307 |
| /tr/presidency/white-house-workers | White House Workers | 292 |
| /visit/weather | Weather | 250 |
| /support/heritage-society | The TRPL HERITAGE SOCIETY | 194 |
| /tr/presidency/executive-actions/story | Executive Actions Story / Theodore Roosevelt Presidential Library | 181 |

### Same topic, two pages
| Topic | Pages |
|---|---|
| mount rushmore | /tr/tr-mount-rushmore, /tr/legacy/mount-rushmore |
| rough riders | /tr/rise-to-power/san-juan-hill, /tr/rise-to-power/rough-riders |
| alice roosevelt longworth | /tr/people/alice-longworth, /tr/people/alice-longworth/complex-legacy |
| alice hathaway lee roosevelt | /tr/new-york-politics/alice-lee, /tr/people/alice-lee |
| alice lee | /tr/new-york-politics/alice-lee, /tr/people/alice-lee |
| edith roosevelt | /tr/rise-to-power/edith-roosevelt, /tr/people/edith-roosevelt |
| common misquotes | /tr/quotes/misquotes, /tr/myths/misquotes |
| gifford pinchot | /tr/presidency/conservation/gifford-pinchot, /tr/people/gifford-pinchot |
| booker t washington | /tr/presidency/booker-t-washington, /tr/people/booker-t-washington |
| ten facts | /tr/rise-to-power/ten-facts, /tr/badlands/ten-facts, /tr/early-life/ten-facts |
| elliott roosevelt | /tr/family/elliott-roosevelt, /tr/people/elliott |
| 7-day trip | /visit/itineraries/7-day-bismarck-rapid-city, /visit/itineraries/7-day-billings-bismarck |
| martha "mittie" bulloch roosevelt | /tr/early-life/mother, /tr/people/mittie |
| teaching theodore roosevelt | /tr/for-educators/elementary, /tr/for-educators/high-school, /tr/for-educators/middle-school |
| sagamore hill | /tr/homes-and-places/sagamore-hill, /tr/rise-to-power/sagamore-hill |

### Broken links to other websites (fix on the page; /video/ ones come from YouTube descriptions)
| Link | Status | On pages | Video page |
|---|---|---|---|
| https://www.theodorerooseveltcenter.org/digital-library/resource-type/diary | 404 | /tr/new-york-politics/double-tragedy, /tr/people/bill-sewall | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/foreign-policy | 404 | /tr/complex-legacy/imperialism, /tr/presidency/panama-canal | False |
| https://abcnews.go.com/US/wireStory/reconstructed-road-opens-grand-views-theodore-roosevelt-national-127851476 | 404 | /press/clips | False |
| https://abcnews.go.com/US/wireStory/theodore-roosevelt-library-opening-visitors-pack-bag-north-126510433 | 404 | /press/clips | False |
| https://apps.apple.com/us/app/rangers-wanted/id6446949837 | 404 | /rangers-wanted | False |
| https://nam12.safelinks.protection.outlook.com/?url=https%3A%2F%2Ftedxfargo.us7.list-manage.com%2Ftrack%2Fclick%3Fu%3D42126281e0ac794ca800574d6%26id%3Df7ebdfb4ff%26e%3D1462c24ed9&data=05%7C02%7C%7C35bcbf6698764ab622a208dcb6cfbeee%7Cc3f9fd833dac4d1ea4c3573c4fcf9600%7C0%7C0%7C638586250598216425%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=nXcwCuy9%2FDCyUR0Q0K6LYfUovy2c365RPeUeFVqxr8c%3D&reserved=0 | 404 | /node/30 | False |
| https://nationaltoday.com/us/nd/medora-nd/news/2026/04/01/theodore-roosevelt-presidential-library-nears-completion/ | 404 | /press/clips | False |
| https://play.google.com/store/apps/details?id=com.trpl.rangerswanted&pcampaignid=web_share | 404 | /rangers-wanted | False |
| https://www.am1100theflag.com/show-episodes/74671-the-steve-hallstrom-show-episode-174-trump-is-selling-bibles-but-should-he-be | 404 | /press/clips | False |
| https://www.argusleader.com/story/news/2025/07/09/theodore-roosevelt-presidential-library-expected-to-open-in-july-2026/84505352007/ | 402 | /press/clips | False |
| https://www.detroitnews.com/story/opinion/2024/01/17/zito-t-r-s-presidential-library-comes-to-life-in-north-dakota/72251603007/ | 402 | /press/clips | False |
| https://www.fargomoorhead.org/teddy-roosevelt-trail/ | 404 | /visit/teddy-trail | False |
| https://www.kvrr.com/2026/06/30/bill-makes-presidential-library-official-home-for-theodore-roosevelt-artifacts-authorizes-funding/ | 404 | /press/clips | False |
| https://www.nationalparkstraveler.org/2026/06/trump-and-burgum-visit-north-dakota-open-theodore-roosevelt-presidential-library | 503 | /press/clips | False |
| https://www.nd.gov/dpi/sites/www/files/documents/Academic%20Support/2023%20ELA%20Content%20Standards-final.pdf | 404 | /teach-tr | False |
| https://www.palmbeachdailynews.com/story/news/2026/04/06/palm-beach-civic-leader-to-lead-theodore-roosevelt-library-debut/89402604007/ | 402 | /press/clips | False |
| https://www.thebaltimorepost.com/2024/12/01/fox-news-massive-theodore-roosevelt-presidential-library-to-open-in-north-dakota-badlands/ | 404 | /press/clips | False |
| https://www.thecivicseason.com/event/virtual-taste-of-history-drink-through-teddy-roosevelts-life-with-historical-cocktails-and-mocktails/ | 404 | /node/205 | False |
| https://www.thehenryford.org/collections-and-research/digital-collections/artifact/246899 | 404 | /research/archives | False |
| https://www.theodorerooseveltcenter.org/Blog/Item/Signature | 404 | /tr/teddy-nickname | False |
| https://www.theodorerooseveltcenter.org/Get-Involved/Events/2024%20Theodore%20Roosevelt%20Symposium | 404 | /node/31 | False |
| https://www.theodorerooseveltcenter.org/Research/Collections/America%20Collection | 404 | /research/archives | False |
| https://www.theodorerooseveltcenter.org/Research/Collections/Dr.%20Danny%20O.%20Crew%20Theodore%20Roosevelt%20Sheet%20Music%20Collection | 404 | /research/archives | False |
| https://www.theodorerooseveltcenter.org/Research/Collections/Fritz%20R%20Gordner%20Collection | 404 | /research/archives | False |
| https://www.theodorerooseveltcenter.org/Research/Collections/Gregory%20A.%20Wynn%20Theodore%20Roosevelt%20Collection | 404 | /research/archives | False |
| https://www.theodorerooseveltcenter.org/Research/Collections/Mike%20Thompson%20Theodore%20Roosevelt%20Postcard%20Collection | 404 | /research/archives | False |
| https://www.theodorerooseveltcenter.org/Research/Digital-Library/Record?libID=o286112. | 404 | /tr/tr-mount-rushmore | False |
| https://www.theodorerooseveltcenter.org/digital-library/o299999 | 404 | /tr/presidency/panama-canal | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/americas/panama | 404 | /tr/presidency/panama-canal | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/capitalism-and-labor/interstate-commerce | 404 | /tr/presidency/railroad-regulation | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/capitalism-and-labor/pure-food-drug-act | 404 | /tr/presidency/food-and-drug | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/culture-and-society/the-strenuous-life | 404 | /tr/presidency/strenuous-life-in-office | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/locations/badlands | 404 | /tr/post-presidency/final-visit-medora | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/locations/medora | 404 | /tr/post-presidency/final-visit-medora | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/people/harvey-wiley | 404 | /tr/presidency/food-and-drug | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/personal-life/family-and-friends/kermit | 404 | /tr/post-presidency/man-in-the-arena | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/politics-and-government/citizenship-in-a-republic | 404 | /tr/post-presidency/man-in-the-arena | False |
| https://www.theodorerooseveltcenter.org/media/Images/Blog/2019/Roosevelt_submarine-1024x854-2.jpg | 404 | /tr/presidency-timeline | False |
| https://www.theodorerooseveltcenter.org/subject/progressive-party | 404 | /tr/people/william-howard-taft | False |
| https://www.usatoday.com/story/news/politics/2026/07/01/roosevelt-library-set-to-open-to-public-on-independence-day/90714775007/ | 402 | /press/clips | False |

## Structured data (schema.org) for search engines and AI tools
101 of 883 content pages carry their own markup (11%); 8 sitewide issues (3 high). llms.txt on trlibrary.com: no (draft: https://seo.labs.trlibrary.com/data/site-llms.txt).

Most fixes are one change to a Drupal template per content type (ask FiveJars); the JSON-LD examples are built from a real page. Values starting 'TODO:' must be filled from the page's own fields, never guessed.

### Sitewide issues
| Severity | Issue | Fix |
|---|---|---|
| high | Sitewide markup doesn't link to the Library's Wikipedia entry | Add these to sameAs in the sitewide schema. |
| high | 249 pages point to a Theodore Roosevelt entity that is never defined | Define the entity once in the sitewide @graph (so every page carries it). This is the single highest-value change for the /tr section. |
| high | www.trlibrary.com has no llms.txt | Review the draft, then ask FiveJars to serve it at https://www.trlibrary.com/llms.txt. |
| medium | Restaurant and store hours are listed as the museum's hours | Keep only museum hours on the Library entity. Give the restaurant and the store their own entities (Restaurant, Store) with their hours, linked with containsPlace. |
| medium | No admission information in the markup | Add admission offers (and isAccessibleForFree: false) to the Library entity. |
| medium | 35 unaliased /node/ URLs are in the sitemap | Ask FiveJars to leave unaliased /node/ URLs out of the XML sitemap. |
| low | 22 pages have dates without a colon in the time zone | In the Drupal schema templates, format dateModified, datePublished, endDate, startDate with the PHP date format “c” (e.g. 2020-10-27T06:00:00-06:00). |
| low | 277 articles are labelled og:type “website” | Set og:type to “article” on /tr, press release and podcast templates (Drupal Metatag). |

### By content type (biggest gaps first)
| Content type | Should carry | Pages | Has it | Incomplete | Fix |
|---|---|---|---|---|---|
| TR history articles | Article | 159 | 0 | 0 | Add Article JSON-LD to the /tr article template with about = Theodore Roosevelt (the sitewide #theodore-roosevelt entity) and dateModified from the node's changed date. |
| Video pages | VideoObject | 409 | 0 | 0 | Add VideoObject JSON-LD to the video view template from the stored YouTube data (title, description, thumbnail, publish date, duration). |
| Good Citizen episodes | PodcastEpisode | 67 | 0 | 0 | Add PodcastEpisode JSON-LD to the podcast episode template (title, summary, release date, Simplecast player). |
| TR history section pages | CollectionPage | 55 | 0 | 0 | Add CollectionPage JSON-LD to the /tr section landing template. |
| TR history: people | Article | 26 | 0 | 0 | Add Article JSON-LD to the /tr people template, with an 'about' Person; a field for the person's Wikidata link makes it precise. |
| Trip itineraries | TouristTrip | 20 | 0 | 0 | Add TouristTrip JSON-LD to the itinerary template, listing each stop. Check the drafted stop list: it's taken from the page headings. |
| Video playlists | ItemList / VideoObject | 39 | 0 | 0 | Add ItemList of VideoObject JSON-LD to the playlist template. Drupal already stores each video's YouTube data, including its publish date (uploadDate). |
| TR history: speeches | Article | 6 | 0 | 0 | Add Article JSON-LD with an 'about' CreativeWork (the speech, author: Theodore Roosevelt). |
| Press releases | Article / NewsArticle | 19 | 19 | 19 | Add NewsArticle JSON-LD to the press release template, using the release date field. |
| Trustee profiles | Person / ProfilePage | 14 | 14 | 14 | Add ProfilePage + Person JSON-LD (role: Trustee) to the trustee template. |
| Pages with Q&A | FAQPage | 20 | 19 | 0 | Add FAQPage JSON-LD to the accordion paragraph type: when every item's title is a question, output each as Question/Answer. One template change covers every FAQ page. |
| Good Citizen podcast page | PodcastSeries | 1 | 0 | 0 | Add PodcastSeries JSON-LD to the podcast landing page. |
| Calendar events | Event | 26 | 26 | 1 | Add Event JSON-LD to the Event content type template, filled from the event's date, time, price and ticket fields. One template change covers every event. |
| Staff profiles | Person / ProfilePage | 42 | 42 | 0 | Add ProfilePage + Person JSON-LD to the staff member template (name, job title, photo). |

## Ticket checkout (GA4, rates only)
Checkout completion – (prior –); store visitors who buy 34% (prior 42%); ticket page to store 60%. Steps the store doesn't report: view_item, add_to_cart, begin_checkout, add_payment_info.

Store frustration signals (last 3 days, Clarity): dead clicks 14.1% of sessions, rage clicks 0.1%, quick backs 30.5%, scroll depth 78.6%.

| Store page | Dead % | Rage % | Quick back % | Scroll % |
|---|---|---|---|---|
| membership/join | 0 | 0 | 0 | 100 |
| orders/tickets | 0 | 0 | 0 | 60.9 |
| private-events/inquiry | 0 | 0 | 0 | 100 |
| events/detail | 0 | 0 | 0 | 100 |
| tickets | 0 | 0 | 0 | 8 |
| auth/members | 20 | 0 | 10 | 98.7 |
| private-events/spaces | 0 | 0 | 0 | 78.3 |
| checkout/confirm | 6.4 | 0 | 3.8 | 99 |
| tr/family/family-tree | 0 | 0 | 0 | 43 |
| orders/calendar | 0 | 0 | 33.4 | 90.3 |
| membership/profile | 0 | 0 | 50 | 100 |
| checkout/process | 75 | 0 | 0 | 100 |
| membership/detail | 2.5 | 0 | 27.1 | 94 |
| calendar/special-event/butchery-workshop | 0 | 0 | 0 | 79 |
| calendar/special-event/america-beautiful-film-screening | 0 | 0 | 0 | 17 |
| orders/forms | 0 | 0 | 0 | 100 |
| legal/terms | 0 | 0 | 0 | 100 |
| pay-balance/zHzouHxtKvA0DicuSJZToQP2jk26raCjMd_NHkngVmh-u5lWZ1yhNSTDRCb9rGnh | 100 | 0 | 0 | 100 |
| search | 0 | 0 | 0 | 56 |
| tr/rise-to-power/san-juan-hill | 0 | 0 | 0 | 24.5 |
| tr/people | 0 | 0 | 0 | 64 |
| calendar | 0 | 0 | 0 | 47 |
| midwinter-table | 0 | 0 | 0 | 84 |
| tr/badlands/elkhorn-ranch | 0 | 0 | 0 | 79.3 |
| about/careers | 0 | 0 | 0 | 52.5 |
| tr/timeline | 0 | 0 | 0 | 100 |
| tr/badlands/landscape | 0 | 0 | 100 | 70 |
| calendar/partners | 0 | 0 | 0 | 97 |
| tr/presidency/square-deal | 25 | 0 | 0 | 31 |
| tr/presidency/trust-busting | 0 | 0 | 0 | 17 |
| tr/fake-quotes | 0 | 0 | 0 | 5 |
| project | 0 | 0 | 0 | 100 |
| quiz | 0 | 0 | 0 | 16 |
| contact | 0 | 0 | 0 | 100 |
| visit/hours | 0 | 0 | 0 | 73 |
| visit/exhibits | 0 | 0 | 0 | 62 |
| membership/renew | 0 | 0 | 58.4 | 96 |
| calendar/special-event/elkhorn-evenings | 0 | 0 | 0 | 66 |
| holiday-2026 | 0 | 0 | 0 | 78 |
| visit/planner | 0 | 0 | 0 | 100 |
| / | 0 | 0 | 25 | 11.2 |
| visit/outdoors | 0 | 0 | 0 | 87 |
| visit | 0 | 0 | 0 | 15 |
| tr/speeches/man-in-the-arena | 0 | 0 | 0 | 29 |
| tr/10-myths-teddy-bear | 0 | 0 | 0 | 65.2 |
| calendar/specialty-tour/badlands-landscape-tour | 0 | 0 | 0 | 33.5 |
| quiz/who-was-tr | 100 | 0 | 0 | 76 |
| podcast/good-citizen | 0 | 0 | 0 | 15 |
| visit/faq | 0 | 0 | 0 | 100 |
| tr/presidency/great-white-fleet | 0 | 0 | 0 | 12.3 |
| tr/rise-to-power/police-commissioner | 0 | 0 | 0 | 71.5 |
| quiz/badlands-wildlife-family | 0 | 0 | 0 | 85 |
| tr/early-life | 0 | 0 | 0 | 31 |
| pay-balance/Pn5WSCU6c-ybMe6AsQSrgvmYHJttEulS_yyKlwHZ1En95cuSYdaGIRv3qIY1ApJJ | 0 | 0 | 0 | 100 |
| quiz/myths-expert | 100 | 0 | 0 | 76 |
| tr/early-life/childhood-illness | 0 | 0 | 0 | 100 |
| teach-tr | 0 | 0 | 0 | 10.5 |
| newsletter | 0 | 0 | 0 | 100 |
| quiz/conservation | 100 | 0 | 0 | 83 |
| membership | 0 | 0 | 0 | 93 |
| research | 0 | 0 | 0 | 78 |
| visit/faq/getting-here | 100 | 0 | 0 | 100 |
| tr/presidency/executive-actions | 0 | 0 | 0 | 5 |
| membership/upgrade | 0 | 0 | 0 | 100 |
| pay-balance/FCmNSQE26iTUN5JctAPrgNZPK5gE9HIBq-brCWdmOHfn9pmgOGuO-CMEATymlBbs | 0 | 0 | 0 | 100 |
| rangers-wanted | 0 | 0 | 100 | 37.3 |
| brand | 0 | 0 | 0 | 100 |
| tr/rise-to-power | 0 | 0 | 0 | 85 |
| tr/post-presidency/bull-moose | 50 | 0 | 0 | 92 |
| tr/quotes | 0 | 0 | 0 | 47 |
| private-events | 0 | 0 | 0 | 45 |
| tr/quotes/citizenship | 0 | 0 | 0 | 19 |
| tr/family/fdr-connection | 0 | 0 | 0 | 4 |
| tr/new-york-politics | 0 | 0 | 0 | 100 |
| tr/birthday-timeline | 0 | 0 | 0 | 96 |
| tr/presidency/first-term | 0 | 0 | 0 | 36 |
| visit/tours | 0 | 0 | 0 | 100 |
| about/press | 0 | 0 | 0 | 88.8 |
| user/login | 0 | 0 | 0 | 100 |
| video/view/W9sq8PuGQVo | 0 | 0 | 0 | 41.5 |
| pay-balance/41vq7qWK0gFKMwzG8gV1F4Nba0TY0Awfwc-K5UJ7Sj8lm6P5ZT_a3IC1_x1l7FvO | 50 | 0 | 0 | 80.7 |
| visit/itineraries/seattle-badlands | 0 | 0 | 0 | 23 |
| project/native-plant-project | 0 | 0 | 0 | 95 |
| tr/rise-to-power/buffalo-soldiers | 0 | 0 | 0 | 34 |
| staff-members/susan-sarna | 0 | 0 | 0 | 88 |
| pay-balance/42w5U23b9Cj9ffGiwG-P7EAIYuIYao8fOrk08fQstQzuofJ7uPtu810fpVYCmeu1 | 50 | 0 | 0 | 100 |
| tr/presidency/panama-canal | 0 | 0 | 0 | 3 |
| tr/complex-legacy/eugenics | 0 | 0 | 0 | 15 |
| visit/exhibits/main | 0 | 0 | 0 | 63 |
| tr/presidency/roosevelt-corollary | 0 | 0 | 0 | 49 |
| visit/maps | 0 | 0 | 0 | 86 |
| signature-experiences | 0 | 0 | 0 | 100 |
| visit/directions | 0 | 0 | 0 | 23.7 |
| about/trustees/hilary-hamm | 50 | 0 | 0 | 96 |
| calendar/special-event | 0 | 0 | 16.7 | 75.3 |
| impact | 0 | 0 | 0 | 34 |
| project/design | 0 | 0 | 0 | 99 |
| tr/new-york-politics/assembly | 0 | 0 | 0 | 68 |
| visit/faq/accessibility | 0 | 0 | 100 | 84.3 |
| staff-members/matt-briney | 0 | 0 | 0 | 100 |
| staff-members | 0 | 0 | 0 | 12 |

## Tracking changes made automatically
Rules and caps: config/tracking.yml. Keep an item permanently by copying it into config/keywords.yml or config/ai_prompts.yml; block it via tracking.yml exclude.

| Date | Change | Type | Item | Why |
|---|---|---|---|---|
| 2026-11-02 | added | question | Which presidents are carved on Mount Rushmore, and why was Theodore Roosevelt included? | from the Google search "who is on mount rushmore"; High-volume inquiry connecting Roosevelt to regional Northern Plains travel and heritage. |
| 2026-11-02 | added | question | What years was Theodore Roosevelt in office, and what were the major milestones of his administration? | from the Google search "when was theodore roosevelt president"; Core presidential timeline search; establishes authority on his administration. |
| 2026-11-02 | added | keyword | bull moose party | position 4.4, 6818 impressions/28d; Roosevelt's historic 1912 third-party presidential campaign |
| 2026-11-02 | added | keyword | alice roosevelt longworth | position 8.5, 9143 impressions/28d; Roosevelt's eldest daughter and a prominent public figure in her own right |
| 2026-11-02 | added | keyword | jacob riis | position 10.2, 20915 impressions/28d; Key Progressive Era ally and close associate during Roosevelt's New York years |
| 2026-11-02 | added | keyword | roosevelt corollary | position 4.7, 23395 impressions/28d; Major foreign policy doctrine central to Roosevelt's presidency and US history curricula |
| 2026-11-02 | added | keyword | brownsville affair | position 5.6, 111795 impressions/28d; Key civil rights controversy from Theodore Roosevelt's presidency |
| 2026-10-26 | added | question | Can you explain Theodore Roosevelt's Square Deal domestic policy and its main goals? | from the Google search "what was the square deal"; Signature domestic policy topic essential for student research and civic education. |
| 2026-10-26 | added | question | What were Theodore Roosevelt's major accomplishments, conservation work, and legacy? | from the Google search "what was theodore roosevelt known for"; Core overview query establishing the Library as the authoritative source on Roosevelt's life and achievements. |
| 2026-10-26 | added | keyword | theodore roosevelt died | position 5.5, 2618 impressions/28d; Foundational biographical search regarding the end of Roosevelt's life. |
| 2026-10-26 | added | keyword | teddy roosevelt | position 8.8, 7588 impressions/28d; High-volume core biographical search for Roosevelt's life, career, and legacy. |
| 2026-10-26 | added | keyword | mount rushmore presidents | position 4.8, 5953 impressions/28d; Regional heritage travelers connecting Theodore Roosevelt to Dakota Black Hills and Badlands itineraries. |
| 2026-10-26 | added | keyword | enchanted highway | position 8.6, 2123 impressions/28d; Major North Dakota travel attraction relevant to Badlands visitors and road trip planners. |
| 2026-10-26 | added | keyword | teddy roosevelt national park | position 8.6, 2000 impressions/28d; Key regional trip-planning search directly adjacent to the Library in Medora. |

## Raw data
All JSON, refreshed daily (Search Console) and weekly (everything else):

- https://seo.labs.trlibrary.com/data/changes.json: Change log: pages changed recently (held back from recommendations) with Search Console before/after numbers
- https://seo.labs.trlibrary.com/data/indexnow.json: IndexNow submissions: changed pages sent to Bing and other engines, by date
- https://seo.labs.trlibrary.com/data/work_queue.json: Work queue: every audit, internal-link and structured-data fix as a task with pages, owner (TRPL or FiveJars), Drupal steps and a done-when check, plus page jobs that bundle all fixes for one page
- https://seo.labs.trlibrary.com/data/status.json: Which data sources are on, last run time, errors
- https://seo.labs.trlibrary.com/data/gsc/summary.json: Search Console totals, last 28 days vs prior 28
- https://seo.labs.trlibrary.com/data/gsc/daily.json: Clicks/impressions/CTR/position per day (~16 months)
- https://seo.labs.trlibrary.com/data/gsc/queries.json: Every search query (last 28 days) with prior-period clicks
- https://seo.labs.trlibrary.com/data/gsc/pages.json: Every page with search traffic (last 28 days)
- https://seo.labs.trlibrary.com/data/gsc/query_pages.json: Query x page pairs, top 10,000 by impressions
- https://seo.labs.trlibrary.com/data/opportunities.json: Ranked opportunity lists (striking distance, low CTR, missing-in-title, declining, cannibalization)
- https://seo.labs.trlibrary.com/data/ranks/latest.json: Tracked keywords: Search Console position, live Google rank, AI Overview presence
- https://seo.labs.trlibrary.com/data/ai/latest.json: Full AI-assistant answers to the weekly travel/history questions, with citations
- https://seo.labs.trlibrary.com/data/ai/history.json: Weekly AI mention and citation rates
- https://seo.labs.trlibrary.com/data/audit/summary.json: Site audit: health score, issue counts, robots.txt AI-crawler access, structured data
- https://seo.labs.trlibrary.com/data/audit/pages.json: Per-page audit: title, meta, H1, canonical, OG tags, word count, issues
- https://seo.labs.trlibrary.com/data/tips.json: AI-drafted page recommendations and the AI-visibility brief
- https://seo.labs.trlibrary.com/data/ux/latest.json: Visitor experience on /visit pages: PageSpeed, accessibility, readability, AI task checks, conflicting facts, GA4/Clarity behaviour
- https://seo.labs.trlibrary.com/data/checkout/latest.json: Ticket-store checkout completion rates from GA4 (rates only)
- https://seo.labs.trlibrary.com/data/links.json: Internal links: broken internal links with proposed 301 redirects, links to add, orphan pages, duplicate topics, related unlinked pages, broken outside links
- https://seo.labs.trlibrary.com/data/redirects.csv: Proposed 301 redirects in Drupal Redirect import format (source,destination,language,status_code,confidence)
- https://seo.labs.trlibrary.com/data/schema.json: Structured data: schema.org coverage by content type, missing properties, sitewide markup issues, ready-to-paste JSON-LD
- https://seo.labs.trlibrary.com/data/site-llms.txt: Draft llms.txt for www.trlibrary.com, built from the sitemap (for review before publishing)
- https://seo.labs.trlibrary.com/data/tracking.json: Keywords and AI questions the system discovered, graduated or retired, with reasons
