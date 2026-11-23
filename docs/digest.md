# trlibrary.com search & AI visibility digest
Generated 2026-11-23T13:12:39+00:00 from https://seo.labs.trlibrary.com. Full data: see 'Raw data' at the end.

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
51 tasks (2 search, 23 audit, 6 internal links, 18 structured data, 2 AI visibility); 12 with FiveJars or blocked. Ranked by severity x the Google audience of the pages involved. Full lists, every page, and step-by-step Drupal recipes: https://seo.labs.trlibrary.com/data/work_queue.json

### This week's moves
1. **Broken internal addresses: add 301 redirects** (`links:broken`): high priority; pages involved get 4,281 Google impressions (28 days). Start with: /orders/613/tickets; /orders/613/calendar; /events/613/detail/6a04cbc9b396e88c8b5609dd.
2. **The Theodore Roosevelt entity has 2 values to fix** (`schema:sitewide:tr_entity_values`): medium priority; affects the whole site. Start with: Every /tr page repeats this entity, so a wrong or missing value repeats on all of them. alternateName lacks “Teddy Roosevelt” · award holds several honors in one string; list each one separately.
3. **Pages ranking well that people skip: rewrite title and description** (`search:low_ctr`): medium priority; pages involved get 307,886 Google impressions (28 days). Start with: /tr/presidency/roosevelt-corollary; /tr/presidency/brownsville; /visit/hours.

### What else we checked (and why it can wait)
- Restaurant and store hours are listed as the museum's hours (`schema:sitewide:mixed_hours`): FiveJars work; send as a ticket
- Same topic on two pages (merge or differentiate) (`links:duplicate_topics`): needs a decision first (merge or archive)
- Strengthen pages ranking just off the top for searches people make (`search:striking_distance`): same area as a move this week (search); next in line
- Add internal links where pages already mention each other (`links:add`): same area as a move this week (internal links); next in line
- Pages nothing links to (`links:orphans`): same area as a move this week (internal links); next in line
- Searches AI assistants run where trlibrary.com isn't on page one (`ai:searches_we_miss`): smaller reach (0 Google impressions vs 4,281 for this week's moves)
- No H1 heading (`audit:h1_missing`): smaller reach (23,893 Google impressions vs 4,281 for this week's moves)
- TR history section pages: add Article / CollectionPage markup (template, all pages at once) (`schema:tr_hubs`): FiveJars work; send as a ticket

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
| 1 | Broken internal addresses: add 301 redirects | internal links | TRPL | 8 | to do | links:broken |
| 2 | Restaurant and store hours are listed as the museum's hours | structured data | FiveJars | 1 | to do | schema:sitewide:mixed_hours |
| 3 | The Theodore Roosevelt entity has 2 values to fix | structured data | TRPL | 1 | to do | schema:sitewide:tr_entity_values |
| 4 | Same topic on two pages (merge or differentiate) | internal links | TRPL | 20 | needs approval | links:duplicate_topics |
| 5 | Pages ranking well that people skip: rewrite title and description | search | TRPL | 5 | to do | search:low_ctr |
| 6 | Strengthen pages ranking just off the top for searches people make | search | TRPL | 18 | to do | search:striking_distance |
| 7 | Add internal links where pages already mention each other | internal links | TRPL | 575 | to do | links:add |
| 8 | Pages nothing links to | internal links | TRPL | 42 | to do | links:orphans |
| 9 | Searches AI assistants run where trlibrary.com isn't on page one | ai visibility | TRPL | 35 | to do | ai:searches_we_miss |
| 10 | No H1 heading | audit | TRPL | 29 | to do | audit:h1_missing |
| 11 | TR history section pages: add Article / CollectionPage markup (template, all pages at once) | structured data | FiveJars | 1 | to do | schema:tr_hubs |
| 12 | Get onto pages AI cites that leave the Library out | ai visibility | TRPL | 2 | to do | ai:ask_to_be_added |
| 13 | Same title as another page | audit | TRPL | 32 | to do | audit:title_duplicate |
| 14 | Turn on IndexNow so Bing and Copilot see changes within hours | audit | FiveJars | 1 | to do | setup:indexnow |
| 15 | Missing Open Graph tags | audit | TRPL | 10 | to do | audit:og_missing |
| 16 | Same title as another page (Video pages: fix once in the video template) | audit | FiveJars | 32 | to do | audit:title_duplicate:template |
| 17 | The live llms.txt has drifted from the site: 19 pages to add | structured data | TRPL | 1 | to do | schema:sitewide:llms_drift |
| 18 | 251 articles use the site logo as their Article image | structured data | FiveJars | 1 | to do | schema:sitewide:article_image |
| 19 | Links that go through a redirect | internal links | TRPL | 73 | to do | links:via_redirect |
| 20 | Related pages that don't link to each other | internal links | TRPL | 27 | to do | links:related |
| 21 | Heading levels skip (e.g. H2 straight to H4) | audit | TRPL | 149 | to do | audit:heading_skip |
| 22 | Took over 3 seconds to respond | audit | FiveJars | 134 | to do | audit:slow |
| 23 | Sitemap lists a /node/ URL instead of a readable path | audit | TRPL | 35 | to do | audit:unaliased_url |
| 24 | No meta description (Video pages: fix once in the video template) | audit | FiveJars | 17 | to do | audit:meta_missing:template |
| 25 | Missing Open Graph tags (Video pages: fix once in the video template) | audit | FiveJars | 17 | to do | audit:og_missing:template |
| 26 | More than 4 clicks from the homepage | audit | TRPL | 135 | to do | audit:deep_page |
| 27 | Title over 60 characters, not counting the site-name suffix | audit | TRPL | 90 | to do | audit:title_too_long |
| 28 | Same meta description as another page | audit | TRPL | 44 | to do | audit:meta_duplicate |
| 29 | No meta description | audit | TRPL | 9 | to do | audit:meta_missing |
| 30 | Title under 15 characters, not counting the site-name suffix | audit | TRPL | 139 | to do | audit:title_too_short |

### Task details (TRPL can do these now)
**1. Broken internal addresses: add 301 redirects** (`links:broken`, 8 items)
- How: Configuration > Search and metadata > URL redirects > Add redirect: From = broken path, To = target, 301. If Drupal warns the path looks valid, submit again. Bulk: import redirects.csv. Also fix the link on the source page when the target is known.
- Done when: The old address returns 301 to the target
  - `/orders/613/tickets`, 536 impr., -> https://access.trlibrary.com/orders/613/tickets (high)
  - `/orders/613/calendar`, 86 impr., -> https://access.trlibrary.com/orders/613/calendar (high)
  - `/events/613/detail/6a04cbc9b396e88c8b5609dd`, -> https://access.trlibrary.com/events/613/detail/6a04cbc9b396e88c8b5609dd (high)
  - `/about/trustees/edward-okeefe`, 3,554 impr., -> /podcast/good-citizen/edward-okeefe (high)
  - `/auth/613/members`, 33 impr., -> https://access.trlibrary.com/auth/613/members (high)
  - `/events/613/detail/6a4a8cb76c7bf23066004d67`, -> https://access.trlibrary.com/events/613/detail/6a4a8cb76c7bf23066004d67 (high)
  - `/place/land/badlands`, -> /quiz/badlands (medium)
  - `/membership/613/join`, 72 impr., -> /membership (low)

**3. The Theodore Roosevelt entity has 2 values to fix** (`schema:sitewide:tr_entity_values`, 1 items)
- How: Edit the meta tags of the “Who was TR” hub page (Schema.org Person). The values are set once there and FiveJars' code prints them on every /tr page. Check names and dates against the Historical Accuracy Standard before saving.
- Done when: The issue no longer appears in schema.json after the next weekly run

**4. Same topic on two pages (merge or differentiate)** (`links:duplicate_topics`, 20 items)
- How: Two pages compete for one subject. Pick the stronger page (clicks, depth), move anything unique onto it, then archive the other and add a 301 from its alias and /node/NID. Get approval first; draft before publishing.
- Done when: One page per topic; the other 301s to it
  - `/tr/tr-mount-rushmore`, 192,319 impr., mount rushmore: /tr/tr-mount-rushmore vs /tr/legacy/mount-rushmore
  - `/tr/rise-to-power/san-juan-hill`, 49,966 impr., rough riders: /tr/rise-to-power/san-juan-hill vs /tr/rise-to-power/rough-riders
  - `/tr/people/alice-longworth`, 26,148 impr., alice roosevelt longworth: /tr/people/alice-longworth vs /tr/people/alice-longworth/complex-legacy
  - `/tr/people/booker-t-washington`, 21,656 impr., booker t washington: /tr/people/booker-t-washington vs /tr/presidency/booker-t-washington
  - `/tr/new-york-politics/alice-lee`, 13,232 impr., alice hathaway lee roosevelt: /tr/new-york-politics/alice-lee vs /tr/people/alice-lee
  - `/tr/new-york-politics/alice-lee`, 13,232 impr., alice lee: /tr/new-york-politics/alice-lee vs /tr/people/alice-lee
  - `/tr/rise-to-power/edith-roosevelt`, 11,015 impr., edith roosevelt: /tr/rise-to-power/edith-roosevelt vs /tr/people/edith-roosevelt
  - `/tr/quotes/misquotes`, 11,013 impr., common misquotes: /tr/quotes/misquotes vs /tr/myths/misquotes
  - ...and 12 more in work_queue.json

**5. Pages ranking well that people skip: rewrite title and description** (`search:low_ctr`, 5 items)
- How: Edit the node (/node/NID/edit) > 'Customize meta tags'. Basic tags: Page title '<title> | [site:name]' (page part 60 characters or fewer) and Description (120-155 characters). Set Open Graph og:title/og:description and Twitter card title/description to match. Save with 'Save' (keeps the moderation state). If the save seems to do nothing, look for a validation error further down the form.
- Done when: Click-through rate rises at the same position (change log before/after)
  - `/tr/presidency/roosevelt-corollary`, 141,111 impr.
  - `/tr/presidency/brownsville`, 113,284 impr.
  - `/visit/hours`, 26,300 impr.
  - `/programs`, 9,562 impr.
  - `/tr/rise-to-power/rough-riders`, 17,629 impr.

**6. Strengthen pages ranking just off the top for searches people make** (`search:striking_distance`, 18 items)
- How: Open the page and make it the best answer to that exact search: use the search's words in the title or a heading, answer it plainly in the first paragraph, add the specifics people want (facts already on the site), and link to it from 2-3 related pages. Don't rewrite a page that already ranks in the top 3 for its main search.
- Done when: Average position for the search improves over the next 4 weeks (change log before/after)
  - `/tr/presidency/brownsville`, 110,120 impr., "brownsville affair" #4.1, move up from #4 to about #3, upside ~12113 clicks/28d
  - `/tr/presidency/roosevelt-corollary`, 2,811 impr., "roosevelt corollary definition" #4.7, move up from #5 to about #3, upside ~307 clicks/28d
  - `/tr/presidency/roosevelt-corollary`, 1,481 impr., "roosevelt corollary definition us history" #5.9, move up from #6 to about #3, upside ~162 clicks/28d
  - `/tr/rise-to-power/rough-riders/who-were-they`, 2,389 impr., "rough riders" #10.0, move up from #10 to about #5, upside ~139 clicks/28d
  - `/quiz/muckrakers`, 2,366 impr., "muckrakers" #10.2, move up from #10 to about #5, upside ~136 clicks/28d
  - `/tr/presidency/roosevelt-corollary`, 1,208 impr., "roosevelt corollary to the monroe doctrine" #4.1, move up from #4 to about #3, upside ~129 clicks/28d
  - `/project/living-building-challenge`, 1,091 impr., "living building challenge" #6.1, move up from #6 to about #3, upside ~117 clicks/28d
  - `/tr/presidency/roosevelt-corollary`, 1,086 impr., "the roosevelt corollary" #4.1, move up from #4 to about #3, upside ~113 clicks/28d
  - ...and 10 more in work_queue.json

**7. Add internal links where pages already mention each other** (`links:add`, 575 items)
- How: Open the source page's Layout. Edit the text block that contains the context sentence and turn the [[bracketed]] words into a link to the target path (relative, e.g. /tr/tr-shot). Don't write new sentences just to hold a link. Save the block, then Save layout.
- Done when: The link appears on the source page; the target's links-in count rises next week
  - `/tr/timeline`, 47,813 impr., [[William Howard Taft]] -> /tr/people/william-howard-taft; [[River of Doubt]] -> /tr/post-presidency/river-of-doubt; [[Roosevelt family]] -> /tr/family
  - `/visit/exhibits/main`, 5,799 impr., [[Booker T. Washington]] -> /tr/people/booker-t-washington; [[River of Doubt]] -> /tr/post-presidency/river-of-doubt; [[Roosevelt family]] -> /tr/family
  - `/tr/presidency/white-house-family`, 2,185 impr., [[Edith Roosevelt]] -> /tr/rise-to-power/edith-roosevelt; [[Sagamore Hill]] -> /tr/rise-to-power/sagamore-hill; [[governor of New York]] -> /tr/rise-to-power/governor
  - `/podcast/good-citizen/edward-okeefe`, 302 impr., [[executive power]] -> /tr/presidency/executive-power; [[Nobel Peace Prize]] -> /tr/presidency/nobel-peace-prize; [[Eleanor Roosevelt]] -> /tr/people/eleanor
  - `/tr/thanksgiving`, 400 impr., [[River of Doubt]] -> /tr/post-presidency/river-of-doubt; [[Henry Cabot Lodge]] -> /tr/people/henry-cabot-lodge; [[Pine Knot]] -> /tr/homes-and-places/pine-knot
  - `/tr/birthday`, 812 impr., [[Alice Hathaway Lee]] -> /tr/new-york-politics/alice-lee; [[Sagamore Hill]] -> /tr/rise-to-power/sagamore-hill; [[Governor of New York]] -> /tr/rise-to-power/governor
  - `/tr/family/family-tree`, 34,105 impr., [[Sagamore Hill]] -> /tr/rise-to-power/sagamore-hill; [[Kermit Roosevelt]] -> /tr/people/kermit; [[Quentin Roosevelt]] -> /tr/people/quentin
  - `/tr/thanksgiving-timeline`, 410 impr., [[River of Doubt]] -> /tr/post-presidency/river-of-doubt; [[Pine Knot]] -> /tr/homes-and-places/pine-knot; [[Alice Lee]] -> /tr/new-york-politics/alice-lee
  - ...and 259 more in work_queue.json

**8. Pages nothing links to** (`links:orphans`, 42 items)
- How: Add 2-3 links to this page from the pages listed under 'link from' (each has the sentence and words to link).
- Done when: At least two pages link in
  - `/tr/pre-presidency-political-accomplishments`, 47,482 impr.
  - `/tr/10-myths-teddy-bear`, 16,311 impr.
  - `/tr/fake-quotes`, 14,704 impr.
  - `/programs`, 9,562 impr.
  - `/join-us`, 6,774 impr.
  - `/research/books-by-roosevelt`, 6,213 impr.
  - `/tr/5-big-adventures`, 5,391 impr.
  - `/tr/tr-save-the-bison`, 3,893 impr.
  - ...and 34 more in work_queue.json

**9. Searches AI assistants run where trlibrary.com isn't on page one** (`ai:searches_we_miss`, 35 items)
- How: These are the searches the assistants ran before answering a question where they left the Library out. Find the trlibrary.com page that should answer each one (or note that none does). Strengthen that page for the search: say it in the title or a heading and answer it in the first paragraph, with facts already on the site. If no page fits, propose one.
- Done when: trlibrary.com ranks top 10 for the search (Search Console) and the next AI run cites it
  - `Bonanzaville West Fargo Cass County Historical Society museum`, run by ChatGPT; we rank nowhere
  - `Chateau de Mores Medora museum`, run by ChatGPT; we rank nowhere
  - `Chateau de Mores State Historic Site Medora North Dakota activities Maah Daah Hey Trail`, run by ChatGPT; we rank nowhere
  - `Chateau de Mores State Historic Site Medora hours activities North Dakota State Historical Society`, run by ChatGPT; we rank nowhere
  - `Dakota Dinosaur Museum Dickinson Dickinson Museum Center official site`, run by ChatGPT; we rank nowhere
  - `Dakota Territory Air Museum Minot official site`, run by ChatGPT; we rank nowhere
  - `Fort Union Trading Post National Historic Site Williston North Dakota`, run by ChatGPT; we rank nowhere
  - `Maah Daah Hey Trail Medora trailhead mountain biking hiking`, run by ChatGPT; we rank nowhere
  - ...and 27 more in work_queue.json

**10. No H1 heading** (`audit:h1_missing`, 29 pages)
- How: Open the page's Layout (/node/NID/layout). Make sure the top section shows the page title block (Content fields > Title), which renders as the H1; or change the first heading in the top text block to Heading 1. Save layout.
- Done when: Exactly one H1
  - `/tr/presidency/executive-actions/action`, 14,767 impr., no H1
  - `/tr/presidency/executive-actions/story`, 6,267 impr., no H1
  - `/grand-opening/photos/july4`, 912 impr., no H1
  - `/visit/maps/campus`, 724 impr., no H1
  - `/research/family-tree`, 361 impr., no H1
  - `/visit/planner`, 352 impr., no H1
  - `/membership/neighbor`, 111 impr., no H1
  - `/private-events/spaces`, 67 impr., no H1
  - ...and 21 more in work_queue.json

**12. Get onto pages AI cites that leave the Library out** (`ai:ask_to_be_added`, 2 items)
- How: Read the page. If it's a list of things to do or a travel guide that names nearby attractions, find the author or the update/contact link and ask to be added, with a two-sentence blurb (what the Library is, why it's worth the stop, about 3 1/2 hours) and a photo. Draft the note for approval; nothing goes out without it.
- Done when: The page names the Library (next weekly run re-reads it)
  - `https://www.bonanzaville.org`, other, cited in 1 answers; names other places
  - `https://business.jamestownchamber.com/list/member/north-american-bison-discovery-center-71`, other, cited in 1 answers; names other places

**13. Same title as another page** (`audit:title_duplicate`, 32 pages)
- How: Edit the node (/node/NID/edit) > 'Customize meta tags'. Basic tags: Page title '<title> | [site:name]' (page part 60 characters or fewer) and Description (120-155 characters). Set Open Graph og:title/og:description and Twitter card title/description to match. Save with 'Save' (keeps the moderation state). If the save seems to do nothing, look for a validation error further down the form.
- Done when: No other page has the same title
  - `/visit/exhibits/kennerly`, 4,184 impr., HELD (recently changed), title "In the Room: David Hume Kennerly Photo Exhibition" (49 chars), same as /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf
  - `/project/native-plant-project`, 660 impr., HELD (recently changed), title "Native Plant Project" (20 chars), same as /video/view/1SqdaUrbU7U
  - `/events/teddycon`, 550 impr., HELD (recently changed), title "Theodore Roosevelt Convention (#TeddyCon)" (41 chars), same as /event/24
  - `/visit/accessibility`, 194 impr., title "Accessibility" (13 chars), same as /visit/faq/accessibility
  - `/alexander-hamilton-speaks`, 142 impr., title "Alexander Hamilton Speaks" (25 chars), same as /hamilton-speaks-the-study
  - `/press/clips`, 118 impr., title "In the News" (11 chars), same as /video/in-the-news
  - `/gwti-250`, 61 impr., title "From Precedent to Power: Teaching Executive Authority Through George Washington and Theodore Roosevelt" (102 chars), same as /calendar/special-event/precedent-power-teaching-executive-authority-through-george-washington-and
  - `/node/246`, 55 impr., title "Book Talk: Candice Millard's The River of Doubt" (47 chars), same as /video/view/dRIXs_adw7U
  - ...and 24 more in work_queue.json

**15. Missing Open Graph tags** (`audit:og_missing`, 10 pages)
- How: Edit the node (/node/NID/edit) > 'Customize meta tags'. Basic tags: Page title '<title> | [site:name]' (page part 60 characters or fewer) and Description (120-155 characters). Set Open Graph og:title/og:description and Twitter card title/description to match. Save with 'Save' (keeps the moderation state). If the save seems to do nothing, look for a validation error further down the form.
- Done when: og:title and og:description are present
  - `/visit/teddy-trail`, 845 impr., HELD (recently changed)
  - `/birthdaycard`, 40 impr.
  - `/rsvp/midwinter`, 26 impr.
  - `/quiz/who-was-tr`, 16 impr.
  - `/project/how-the-library-works`, 13 impr.
  - `/quiz/the-boardwalk`, 4 impr.
  - `/quiz/native-plant-project`, 2 impr.
  - `/quiz/badlands-family`, 1 impr.
  - ...and 2 more in work_queue.json

**17. The live llms.txt has drifted from the site: 19 pages to add** (`schema:sitewide:llms_drift`, 1 items)
- How: Edit the sections at /admin/content/llms-txt/sections: add the new pages under their heading and remove or repoint the links that left the sitemap. The draft has the wording for each new line.
- Done when: The issue no longer appears in schema.json after the next weekly run

**19. Links that go through a redirect** (`links:via_redirect`, 73 items)
- How: Edit the link on each source page so it points straight at the final address.
- Done when: Links point at the final address
  - `/holidays`, -> /holiday-2026
  - `/grand-opening/talks`, -> /
  - `/calendar/daily-activity/david-hume-kennerly-exhibition`, -> /calendar/daily-activity/room-sixty-years-front-lines-history
  - `/support-trpl`, -> /support
  - `/press`, -> /about/press
  - `/latest-news`, -> /about/press
  - `/donate`, -> /support
  - `/project/native-plants`, -> /project/native-plant-project
  - ...and 65 more in work_queue.json

### Page jobs: everything to fix on one page, busiest pages first
| Page | Impr. | Fixes | Links to add | Markup |  |
|---|---|---|---|---|---|
| /tr/tr-mount-rushmore | 188297 | – | [[executive power]] -> /tr/presidency/executive-power | – | held |
| /podcast/good-citizen/senator-chris-murphy | 163247 | deep_page, heading_skip, meta_duplicate | – | – |  |
| /tr/family/fdr-connection | 91305 | – | [[Assistant Secretary of the Navy]] -> /tr/rise-to-power/assistant-navy-secretary | – | held |
| / | 79314 | title_too_long, heading_skip | [[Elkhorn Ranch]] -> /tr/badlands/elkhorn-ranch | – |  |
| /tr/presidency/bully-pulpit | 55514 | – | [[Doris Kearns Goodwin]] -> /about/trustees/doris-kearns-goodwin | – | held |
| /tr/presidency-timeline | 52003 | heading_skip | [[Nobel Peace Prize]] -> /tr/presidency/nobel-peace-prize | – | held |
| /tr/timeline | 47813 | heading_skip | [[William Howard Taft]] -> /tr/people/william-howard-taft; [[River of Doubt]] -> /tr/post-presidency/river-of-doubt; [[Roosevelt family]] -> /tr/family | – | held |
| /tr/pre-presidency-political-accomplishments | 47482 | – | [[Naval War of 1812]] -> /tr/new-york-politics/naval-war-of-1812 | – | held |
| /visit | 44809 | – | [[Badlands landscape]] -> /tr/badlands/landscape; [[Medora, North Dakota]] -> /tr/badlands/medora | – | held |
| /tr/tr-importance | 41023 | – | [[Leonard Wood]] -> /tr/people/leonard-wood; [[national forests]] -> /tr/presidency/conservation/national-forests; [[Theodore Roosevelt National Park]] -> /tr/homes-and-places/tr-national-park | – | held |
| /bullet-speech | 38822 | deep_page, h1_multiple | – | – | held |
| /tr/complex-legacy/imperialism | 35535 | – | [[Assistant Secretary of the Navy]] -> /tr/rise-to-power/assistant-navy-secretary; [[Rough Riders]] -> /tr/rise-to-power/san-juan-hill | – | held |
| /podcast/good-citizen/karl-rove-historic-redemption-hard-work-politics-and-essential-nature | 34860 | deep_page, heading_skip | – | – | held |
| /visit/directions | 34417 | – | [[Little Missouri River]] -> /visit/little-missouri-river | – | held |
| /tr/family/family-tree | 34105 | – | [[Sagamore Hill]] -> /tr/rise-to-power/sagamore-hill; [[Kermit Roosevelt]] -> /tr/people/kermit; [[Quentin Roosevelt]] -> /tr/people/quentin | – | held |

### Waiting on FiveJars or blocked (already ticketed; check whether they've landed, don't re-ask)
- Sitewide markup doesn't link to the Library's Wikipedia entry (`schema:sitewide:sameas`): blocked, the per-page sameAs field is capped at 255 characters; FiveJars asked to raise it. Wikidata is in place; Wikipedia and Bluesky go back in once it's raised
- No admission information in the markup (`schema:sitewide:admission`)
- Good Citizen episodes: add PodcastEpisode markup (template, all pages at once) (`schema:podcast_episode`)
- Video pages: add VideoObject markup (template, all pages at once) (`schema:videos`)
- Trip itineraries: add TouristTrip markup (template, all pages at once) (`schema:itineraries`)
- Good Citizen podcast page: add PodcastSeries markup (template, all pages at once) (`schema:podcast_series`)
- Video playlists: add ItemList / VideoObject markup (template, all pages at once) (`schema:video_playlists`)
- 273 pages have dates without a colon in the time zone (`schema:sitewide:date_format`)
- 91 articles are labelled og:type “website” (`schema:sitewide:og_type`)
- Pages with Q&A: add FAQPage markup (template, all pages at once) (`schema:faq`)
- Press releases: add Article / NewsArticle markup (template, all pages at once) (`schema:press`)
- Trustee profiles: add Person / ProfilePage markup (template, all pages at once) (`schema:trustees`)


## Data freshness
| Source | State | Updated | Details |
|---|---|---|---|
| audit | ok | 2026-11-23T12:38:39+00:00 | Crawled 1149 pages, health 95/100 |
| ranks | ok | 2026-11-23T12:44:16+00:00 | 45 keywords checked |
| opportunities | ok | 2026-11-23T12:52:20+00:00 | 18 striking-distance queries, 5 low-CTR pages; 142 recently changed pages held back |
| gsc | ok | 2026-11-23T12:33:08+00:00 | 22494 queries, 2964 pages (2026-10-24 to 2026-11-20); 270 changed pages tracked |
| ai_visibility | error | 2026-11-23T12:52:20+00:00 | 46 answers from ChatGPT, Gemini, Perplexity; 23 failed: Perplexity 403: {"error":{"message":"The Agent API requires paid credits. Sign-up credits and Perplexity Pro or Max subscriptions do not count. Add cr |
| tips | ok | 2026-11-23T13:12:39+00:00 | Gemini wrote tips for 8 pages |
| digest | ok | 2026-11-22T13:22:52+00:00 | llms.txt, digest.md and digest.json rebuilt |
| checkout | ok | 2026-11-23T13:09:24+00:00 | Checkout completion n/a; steps not tracked: view_item, add_to_cart, begin_checkout, add_payment_info |
| curate | ok | 2026-11-23T12:38:58+00:00 | 25 discovered keywords and 8 discovered questions tracked; 5 changes today |
| ux | ok | 2026-11-23T13:06:11+00:00 | 82 pages; PageSpeed on 80; AI task check by gemini (gemini-3.8-flash); GA4 on; Clarity off; 2 errors, e.g. PageSpeed /visit/maps: PageSpeed 500: {   "error": {     "code": 500,     "message": "Lighthouse returned error: PAGE_HUNG. Lighthouse was unable to reliably load the URL you requeste |
| links | ok | 2026-11-23T13:07:42+00:00 | 1184 pages crawled; 8 broken internal links (redirects proposed); 682 suggested links; 42 orphan pages; 27 related pairs without links |
| schema | ok | 2026-11-23T13:09:00+00:00 | 352/900 content pages have their own markup; 9 sitewide issues |
| indexnow | skipped | 2026-11-22T13:22:52+00:00 | No IndexNow key yet: see the work queue task 'Turn on IndexNow'. |

## Google Search (Search Console)
2026-10-24 to 2026-11-20 vs the prior 28 days: **40,684 clicks** (prior 45,822), 2,936,788 impressions (prior 2,415,331), CTR 1.4% (prior 1.9%), average position 5.7 (prior 6.1). Branded clicks 8938, non-branded 10918, search term hidden by Google 20828.

### Top non-branded searches (people who didn't search our name)
| Search | Clicks | Impr. | Pos. |
|---|---|---|---|
| brownsville affair | 1 | 110120 | 4.1 |
| chris murphy | 16 | 79113 | 12 |
| square deal | 153 | 46190 | 3.4 |
| karl rove | 56 | 28279 | 8.4 |
| senator chris murphy | 15 | 25812 | 12.9 |
| roosevelt corollary | 52 | 22950 | 3.8 |
| jacob riis | 164 | 21603 | 8.5 |
| bully pulpit | 53 | 21376 | 3.3 |
| bill kristol | 6 | 20200 | 11.7 |
| chris murphy senator | 10 | 18936 | 12.6 |
| theodore roosevelt | 46 | 16705 | 4.4 |
| mount rushmore | 9 | 14123 | 11.2 |
| roosevelt family | 14 | 13843 | 3.1 |
| the man in the arena | 250 | 12532 | 5.6 |
| mount rushmore presidents | 32 | 11341 | 4.1 |
| man in the arena | 92 | 11284 | 7.3 |
| alice roosevelt | 62 | 10646 | 6.9 |
| theo elections | 3 | 10167 | 6.5 |
| kermit roosevelt | 18 | 9684 | 7.7 |
| bull moose party | 59 | 8999 | 3.2 |
| sen chris murphy | 6 | 8873 | 10.6 |
| who is on mount rushmore | 9 | 8157 | 6.9 |
| senator murphy | 5 | 7602 | 12.3 |
| alice roosevelt longworth | 17 | 7009 | 7.5 |
| teddy roosevelt | 41 | 6846 | 6.9 |

### Top pages
| Page | Clicks | Prior | Impr. | Pos. |
|---|---|---|---|---|
| / | 5858 | 9250 | 62423 | 6.2 |
| /tickets?utm_source=gbp&utm_medium=organic | 2254 | 3030 | 18476 | 3.8 |
| /tr/family/fdr-connection | 2019 | 1195 | 91305 | 2.9 |
| /?utm_source=gbp&utm_medium=organic | 1902 | 4755 | 14602 | 4 |
| /tickets | 1597 | 4797 | 41784 | 3 |
| /tr/speeches/man-in-the-arena | 1564 | 401 | 54163 | 5.3 |
| /tr/presidency/square-deal | 1399 | 471 | 117589 | 3.3 |
| /tr/presidency/trust-busting | 1185 | 959 | 77126 | 3.2 |
| /visit | 896 | 1763 | 44807 | 2.8 |
| /bullet-speech | 607 | 706 | 38821 | 3.7 |
| /tr/people/jacob-riis | 601 | 367 | 74324 | 6 |
| /tr/presidency/ten-facts | 576 | 345 | 15254 | 3.7 |
| /tr/presidency/food-and-drug | 563 | 25 | 57800 | 5 |
| /tr/quotes | 547 | 607 | 20223 | 3.9 |
| /tr/presidency/panama-canal | 473 | 222 | 75691 | 4.7 |
| /tr/tr-mount-rushmore | 469 | 500 | 188297 | 6.3 |
| /tr/family/family-tree | 411 | 349 | 34105 | 5.1 |
| /tr/presidency/roosevelt-corollary | 400 | 208 | 141111 | 4.2 |
| /tr/tr-importance | 395 | 372 | 41020 | 4.7 |
| /tr/fake-quotes | 371 | 316 | 14704 | 6.1 |
| /tr/pre-presidency-political-accomplishments | 366 | 645 | 47482 | 5.6 |
| /tr/rise-to-power/san-juan-hill | 361 | 397 | 32337 | 3.6 |
| /tr/complex-legacy/imperialism | 351 | 173 | 35535 | 5.3 |
| /tr/presidency-timeline | 342 | 313 | 52003 | 4.4 |
| /visit/directions | 324 | 718 | 34417 | 3.2 |

## Opportunities (ranked)
_Upside is sized against a realistic next step (a few places up, not #1), minus the clicks the page already gets, using a rough industry click-through curve; overlapping searches for one page aren't added twice. Use it to rank opportunities, never as a forecast, and say how the gain would happen: a new ranking, a higher position, or more clicks at the same position._

### Striking distance: ranking 4-20 with demand; strengthen the page for the exact search
| Search | Page | Pos. | Impr. | How | Upside |
|---|---|---|---|---|---|
| brownsville affair | /tr/presidency/brownsville | 4.1 | 110120 | move up from #4 to about #3 | 12113 |
| roosevelt corollary definition | /tr/presidency/roosevelt-corollary | 4.7 | 2811 | move up from #5 to about #3 | 307 |
| roosevelt corollary definition us history | /tr/presidency/roosevelt-corollary | 5.9 | 1481 | move up from #6 to about #3 | 162 |
| rough riders | /tr/rise-to-power/rough-riders/who-were-they | 10 | 2389 | move up from #10 to about #5 | 139 |
| muckrakers | /quiz/muckrakers | 10.2 | 2366 | move up from #10 to about #5 | 136 |
| roosevelt corollary to the monroe doctrine | /tr/presidency/roosevelt-corollary | 4.1 | 1208 | move up from #4 to about #3 | 129 |
| living building challenge | /project/living-building-challenge | 6.1 | 1091 | move up from #6 to about #3 | 117 |
| the roosevelt corollary | /tr/presidency/roosevelt-corollary | 4.1 | 1086 | move up from #4 to about #3 | 113 |
| roosevelt reservation | /tr/presidency/executive-actions/action?id=proc-758 | 6 | 756 | move up from #6 to about #3 | 82 |
| quanah parker | /tr/people/quanah-parker | 9.9 | 1393 | move up from #10 to about #5 | 81 |
| define roosevelt corollary | /tr/presidency/roosevelt-corollary | 4.1 | 702 | move up from #4 to about #3 | 77 |
| rough riders | /tr/rise-to-power/rough-riders | 8.2 | 1112 | move up from #8 to about #5 | 63 |
| who were the rough riders | /tr/rise-to-power/rough-riders/who-were-they | 4.4 | 552 | move up from #4 to about #3 | 59 |
| who were the rough riders | /tr/rise-to-power/rough-riders | 6.6 | 850 | move up from #7 to about #5 | 47 |
| teddy roosevelt presidential library | /calendar/specialty-tour/tr-deep-dive-tour?source=ev | 10.5 | 808 | move up from #10 to about #5 | 45 |

### Ranking well but skipped: rewrite title/meta description
| Page | Pos. | CTR | Typical | Upside |
|---|---|---|---|---|
| /tr/presidency/roosevelt-corollary | 4.2 | 0.3% | 8.0% | 10894 |
| /tr/presidency/brownsville | 4.1 | 0.1% | 8.0% | 8983 |
| /visit/hours | 2.2 | 1.2% | 16.0% | 3890 |
| /programs | 4 | 0.1% | 8.0% | 755 |
| /tr/rise-to-power/rough-riders | 6.4 | 0.4% | 4.5% | 723 |

### Search words missing from the ranking page's title
| Search | Page | Current title | Missing | Impr. |
|---|---|---|---|---|
| roosevelt corollary definition us history | /tr/presidency/roosevelt-corollary | Roosevelt Corollary to the Monroe Doctrine, Explained / Theodore Roosevelt Presidential Library | definition, us, history | 1481 |
| teddy roosevelt museum | / | Theodore Roosevelt Presidential Library / Medora, North Dakota | teddy, museum | 759 |
| roosevelt reservation | /tr/presidency/executive-actions/action?id=proc-758 | Executive Action / Theodore Roosevelt Presidential Library | reservation | 756 |
| what message did the roosevelt corollary send to the rest of the world? the us had the most powerful navy in the world. the us was in charge of the western hemisphere. the us did not want to be involved in other countries’ affairs. the us had the strongest economy in the world. | /tr/presidency/roosevelt-corollary | Roosevelt Corollary to the Monroe Doctrine, Explained / Theodore Roosevelt Presidential Library | message, did, send, rest, world, us, had, most, powerful, navy, world, us, was, charge, western, hemisphere, us, did, not, want, involved, other, countries, affairs, us, had, strongest, economy, world | 411 |
| trpl | / | Theodore Roosevelt Presidential Library / Medora, North Dakota | trpl | 380 |
| roosevelt corollary simple definition | /tr/presidency/roosevelt-corollary | Roosevelt Corollary to the Monroe Doctrine, Explained / Theodore Roosevelt Presidential Library | simple, definition | 366 |
| what did roosevelt do which had never been done before in conservation? | /tr/presidency/conservation | Roosevelt and Conservation / Theodore Roosevelt Presidential Library | did, had, never, been, done, before | 321 |

### Losing clicks vs prior 28 days (check seasonality first)
| Type | Search/page | Clicks | Prior | Change |
|---|---|---|---|---|
| query | theodore roosevelt presidential library | 3179 | 6880 | -53.8% |
| page | / | 5858 | 9250 | -36.7% |
| page | /tickets | 1597 | 4797 | -66.7% |
| page | /?utm_source=gbp&utm_medium=organic | 1902 | 4755 | -60.0% |
| query | teddy roosevelt presidential library | 1051 | 2490 | -57.8% |
| query | teddy roosevelt library | 1194 | 2089 | -42.8% |
| page | /visit | 896 | 1763 | -49.2% |
| page | /tr/square-deal | 235 | 1028 | -77.1% |
| query | theodore roosevelt library | 731 | 1209 | -39.5% |
| page | /visit/directions | 324 | 718 | -54.9% |
| page | /visit/hours | 317 | 637 | -50.2% |
| page | /tr/pre-presidency-political-accomplishments | 366 | 645 | -43.3% |
| query | roosevelt presidential library | 182 | 401 | -54.6% |
| query | roosevelt library | 145 | 315 | -54.0% |
| query | roosevelt library north dakota | 172 | 339 | -49.3% |

### Our pages competing for the same search
| Search | Impr. | Pages |
|---|---|---|
| square deal | 58692 | /tr/presidency/square-deal (pos 3.6), /tr/square-deal (pos 5.6) |
| roosevelt family | 18675 | /tr/family/family-tree (pos 3.3), /tr/family (pos 8.3) |
| bull moose party | 9345 | /tr/post-presidency/bull-moose (pos 3.2), /tr/post-presidency/bull-moose/platform (pos 3.6) |
| kermit roosevelt | 8963 | /podcast/good-citizen/kermit-roosevelt-iii (pos 7.6), /about/trustees/kermit-roosevelt (pos 6.7) |
| roosevelt library | 5001 | /tickets (pos 4.8), / (pos 3.6), /visit (pos 2.9), /programs (pos 2.9) |
| rough riders | 3501 | /tr/rise-to-power/rough-riders/who-were-they (pos 10.0), /tr/rise-to-power/rough-riders (pos 8.2) |
| bamie roosevelt | 3161 | /tr/people/bamie (pos 6.6), /tr/early-life/siblings (pos 7.4), /tr/people/bamie/political-adviser (pos 12.7), /tr/people (pos 13.2) |
| teddy roosevelt museum | 3079 | / (pos 1.6), /tickets (pos 2.0), /visit (pos 2.0), /video/view/Vf8ee-gccpc (pos 4.7) |
| martha bulloch roosevelt | 2780 | /tr/early-life/mother (pos 2.8), /tr/people/mittie (pos 7.1) |
| the square deal | 2548 | /tr/presidency/square-deal (pos 2.5), /tr/square-deal (pos 3.0) |
| what was the square deal | 2019 | /tr/presidency/square-deal (pos 1.6), /tr/square-deal (pos 1.3) |
| teddy | 1685 | /tr/10-myths-teddy-bear (pos 10.3), /tr/teddy-nickname (pos 6.7) |
| square deal definition | 1540 | /tr/presidency/square-deal (pos 1.4), /tr/square-deal (pos 2.2) |
| teddy roosevelt shot | 1500 | /bullet-speech (pos 2.9), /tr/tr-shot (pos 3.7) |
| when did theodore roosevelt die | 1483 | /tr/timeline (pos 4.2), /tr/post-presidency/death (pos 7.3) |

## Tracked keywords (dataforseo+gsc)
| Keyword | Group | Volume | GSC pos. | Google rank | AI Overview | Cites us | Above us |
|---|---|---|---|---|---|---|---|
| theodore roosevelt presidential library | Visit | 90500 | 1.4 | – | True | False | google.com, google.com, google.com |
| things to do in medora nd | Visit | 1600 | 1.7 | – | True | False | google.com, google.com, google.com |
| medora north dakota attractions | Visit | 1600 | – | – | False | False | google.com, google.com, google.com |
| things to do near theodore roosevelt national park | Visit | 50 | 1 | – | True | False | google.com, google.com, google.com |
| museums in north dakota | Visit | 320 | – | – | True | False | google.com, google.com, google.com |
| north dakota road trip | Visit | 140 | 8.3 | – | True | False | google.com, google.com, google.com |
| medora nd hotels | Visit | 8100 | 4.3 | – | True | False | google.com, google.com, google.com |
| badlands north dakota | Visit | 5400 | 10 | – | True | False | google.com, google.com, google.com |
| theodore roosevelt | History | 450000 | 4.4 | – | False | False | google.com, google.com, google.com |
| theodore roosevelt north dakota | History | 320 | 6.1 | – | False | False | google.com, google.com, google.com |
| theodore roosevelt badlands | History | 140 | 1.6 | – | True | True | google.com, google.com, google.com |
| elkhorn ranch | History | 2900 | 9.8 | – | True | False | google.com, google.com, google.com |
| maltese cross cabin | History | 720 | 11.4 | – | False | False | google.com, google.com, google.com |
| theodore roosevelt conservation | History | 590 | 6 | – | True | False | google.com, google.com, google.com |
| presidential libraries | Presidential libraries | 14800 | 5.7 | – | True | False | google.com, google.com, google.com |
| newest presidential library | Presidential libraries | 210 | 1.6 | – | True | False | google.com, google.com, google.com |
| presidential library road trip | Presidential libraries | – | – | – | True | False | google.com, google.com, google.com |
| theodore roosevelt quotes | Learning | 6600 | 3.1 | – | True | True | google.com, google.com, google.com |
| theodore roosevelt man in the arena | Learning | 2400 | 4 | – | True | False | google.com, google.com, google.com |
| theodore roosevelt podcast | Learning | 10 | – | – | True | True | google.com, google.com, google.com |
| teddy roosevelt national park | Auto: Visit | 74000 | 9.3 | – | False | False | google.com, google.com, google.com |
| enchanted highway | Auto: Visit | 9900 | 9.1 | – | True | False | google.com, google.com, google.com |
| mount rushmore presidents | Auto: Visit | 27100 | 4.1 | – | True | True | google.com, google.com, google.com |
| teddy roosevelt | Auto: History | 450000 | 6.9 | – | False | False | google.com, google.com, google.com |
| theodore roosevelt died | Auto: History | 5400 | 4 | – | True | False | google.com, google.com, google.com |
| brownsville affair | Auto: History | 590 | 4.1 | – | True | True | google.com, google.com, google.com |
| roosevelt corollary | Auto: History | 33100 | 3.8 | – | True | True | google.com, google.com, google.com |
| jacob riis | Auto: History | 33100 | 8.5 | – | True | True | google.com, google.com, google.com |
| alice roosevelt longworth | Auto: Family | 27100 | 7.5 | – | True | True | google.com, google.com, google.com |
| bull moose party | Auto: History | 9900 | 3.2 | – | True | True | google.com, google.com, google.com |
| alice roosevelt | Auto: Family | 27100 | 6.9 | – | False | False | google.com, google.com, google.com |
| man in the arena | Auto: Learning | 18100 | 7.3 | – | True | False | google.com, google.com, google.com |
| kermit roosevelt | Auto: Family | 12100 | 7.7 | – | True | True | google.com, google.com, google.com |
| who is on mount rushmore | Auto: Learning | 18100 | 6.9 | – | True | False | google.com, google.com, google.com |
| quentin roosevelt | Auto: Family | 9900 | 11 | – | True | False | google.com, google.com, google.com |
| alice hathaway lee roosevelt | Auto: History | 9900 | 5.7 | – | True | True | google.com, google.com, google.com |
| american imperialism | Auto: Learning | 12100 | 6.9 | – | True | False | google.com, google.com, google.com |
| archibald roosevelt | Auto: History | 5400 | 7.8 | – | True | False | google.com, google.com, google.com |
| booker t washington | Auto: History | 110000 | 12.5 | – | True | False | google.com, artsandculture.google.com, google.com |
| bully pulpit meaning | Auto: Learning | 4400 | 3.9 | – | True | False | google.com, google.com, google.com |
| mt rushmore presidents | Auto: History | 8100 | 4.2 | – | True | True | google.com, google.com, google.com |
| roosevelt river | Auto: History | 1600 | 9 | – | True | False | google.com, google.com, google.com |
| henry cabot lodge | Auto: History | 9900 | 7.5 | – | False | False | google.com, google.com, google.com |
| rough riders | Auto: History | 33100 | 9.5 | – | True | False | google.com, google.com, google.com |
| edith roosevelt | Auto: History | 9900 | 9.1 | – | True | True | google.com, google.com, google.com |

## AI assistant visibility
| Engine | Model | Mentions us | Cites trlibrary.com |
|---|---|---|---|
| ChatGPT | gpt-5-mini | 43.5% | 43.5% |
| Gemini | gemini-3.8-flash | 26.1% | 21.7% |
| Perplexity | fast | – | – |

### Question by question
Some answers failed this week: perplexity: Perplexity 403: {"error":{"message":"The Agent API requires paid credits. Sign-up credits and Perplexity Pro or Max subscriptions do not cou

**I'm visiting Theodore Roosevelt National Park. What else should I see nearby?** (Trip planning)
- ChatGPT: mentioned, #3 among attractions, cites trlibrary.com. Also named: Elkhorn Ranch, Pitchfork Steak Fondue, Chateau de Mores, Painted Canyon, Maah Daah Hey Trail, Medora Musical. Described as: "- Theodore Roosevelt Presidential Library — new, on a butte just west of Medora (about 1–1.5 miles from the South Unit entrance); makes an easy half‑day visit. … ([trlibrary.com](https://www.trlibrary.com/?utm_source=openai))" Sources: medorand.org, trlibrary.com, history.nd.gov, nps.gov, parkrec.nd.gov, ndtourism.com
- Gemini: NOT mentioned. Also named: Theodore Roosevelt National Park, North Dakota Cowboy Hall of Fame, Medora Musical, Pitchfork Steak Fondue, Maah Daah Hey Trail. Sources: none

**What are the best things to do in Medora, North Dakota?** (Trip planning)
- ChatGPT: NOT mentioned. Also named: Theodore Roosevelt National Park, Medora Musical, Pitchfork Steak Fondue, Maah Daah Hey Trail, Chateau de Mores, North Dakota Cowboy Hall of Fame, Painted Canyon. Sources: home.nps.gov, medora.com, ndtourism.com, history.nd.gov, foundation.medora.com, en.wikipedia.org
- Gemini: mentioned, #3 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Medora Musical, Pitchfork Steak Fondue, Chateau de Mores, North Dakota Cowboy Hall of Fame, Maah Daah Hey Trail. Described as: "Visit the Theodore Roosevelt Presidential Library … The **Theodore Roosevelt Presidential Library** is an architectural marvel integrated seamlessly into the badlands terrain." Sources: medora.com, nd.gov, discovermedora.com, trlibrary.com

**Plan a 3-day road trip through western North Dakota. What are the must-see stops?** (Trip planning)
- ChatGPT: mentioned, #2 among attractions, cites trlibrary.com. Also named: Painted Canyon, Chateau de Mores, North Dakota Cowboy Hall of Fame, Theodore Roosevelt National Park, Medora Musical, Maah Daah Hey Trail. Described as: "([trlibrary.com](https://www.trlibrary.com/visit/scenic-drives?utm_source=openai)) … ([trlibrary.com](https://www.trlibrary.com/visit/scenic-drives?utm_source=openai))" Sources: trlibrary.com, medorand.org, nps.gov, medora.com, traveltheparks.com, ndtourism.com
- Gemini: NOT mentioned. Also named: Chateau de Mores, North Dakota Cowboy Hall of Fame, Theodore Roosevelt National Park, Pitchfork Steak Fondue, Medora Musical. Sources: none

**We're driving from Mount Rushmore to Theodore Roosevelt National Park. What's worth stopping for?** (Trip planning)
- ChatGPT: mentioned, #6 among attractions, cites trlibrary.com. Also named: Mount Rushmore, Theodore Roosevelt National Park, Painted Canyon, Chateau de Mores, Medora Musical. Described as: "([trlibrary.com](https://www.trlibrary.com/visit/scenic-drives?utm_source=openai))" Sources: trippy.com, gfp.sd.gov, crazyhorsememorial.org, nps.gov, visitrapidcity.com, walldrug.com
- Gemini: NOT mentioned. Also named: Mount Rushmore, Theodore Roosevelt National Park. Sources: none

**What are the best stops along I-94 in North Dakota?** (Trip planning)
- ChatGPT: mentioned, #5 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Medora Musical, Painted Canyon. Described as: "([trlibrary.com](https://www.trlibrary.com/visit/i-94?utm_source=openai)) … ([trlibrary.com](https://www.trlibrary.com/visit/i-94?utm_source=openai))" Sources: trlibrary.com, ndtourism.com, en.wikipedia.org, bismarckminibuscompany.com, atlasobscura.com, realjourneytravels.com
- Gemini: NOT mentioned. Also named: Painted Canyon, Theodore Roosevelt National Park, Chateau de Mores, Medora Musical. Sources: none

**Fun things to do with kids in the North Dakota Badlands?** (Trip planning)
- ChatGPT: mentioned, #5 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Painted Canyon, Maah Daah Hey Trail, Medora Musical. Described as: "([trlibrary.com](https://www.trlibrary.com/visit/hiking?utm_source=openai))" Sources: govinfo.gov, home.nps.gov, nps.gov, medora.com, ndtourism.com, mdhta.com
- Gemini: NOT mentioned. Also named: Theodore Roosevelt National Park, Painted Canyon, Medora Musical, Pitchfork Steak Fondue, Maltese Cross Cabin, Chateau de Mores, North Dakota Cowboy Hall of Fame. Sources: none

**What can we do indoors in Medora if the weather is bad?** (Trip planning)
- ChatGPT: NOT mentioned. Also named: Theodore Roosevelt National Park. Sources: none
- Gemini: NOT mentioned. Also named: North Dakota Cowboy Hall of Fame, Chateau de Mores, Theodore Roosevelt National Park, Maltese Cross Cabin, Medora Musical. Sources: medorand.org, medora.com, wanderlog.com, ndtourism.com, vacationmedora.com

**What are the best museums in North Dakota?** (Museums)
- ChatGPT: NOT mentioned. Sources: statemuseum.nd.gov, ndtourism.com, bonanzaville.org, business.jamestownchamber.com, en.wikipedia.org, nps.gov
- Gemini: NOT mentioned. Also named: North Dakota Cowboy Hall of Fame, Theodore Roosevelt National Park, Chateau de Mores, Maltese Cross Cabin. Sources: reddit.com, dickinsongov.com, ndtourism.com, medora.com, visitdickinson.com, causeiq.com

**What is the newest presidential library in the United States?** (Museums)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Described as: "The newest presidential library is the Theodore Roosevelt Presidential Library in Medora, North Dakota — it opened on July 4, 2026. … ([trlibrary.com](https://www.trlibrary.com/about/press/press-releases/theodore-roosevelt-presidential-library-opening-celebrations-july-4-2026?utm_source=openai))" Sources: trlibrary.com, en.wikipedia.org, hoover.archives.gov
- Gemini: mentioned, #1 among attractions. Also named: Theodore Roosevelt National Park. Described as: "Newest Presidential Library Facility: **Theodore Roosevelt Presidential Library**" Sources: cnn.com, youtube.com, cbsnews.com, wikipedia.org, obama.org, obamalibrary.gov

**Which presidential libraries are worth visiting?** (Museums)
- ChatGPT: NOT mentioned. Sources: none
- Gemini: NOT mentioned. Sources: none

**Where can I learn about Theodore Roosevelt's life in North Dakota?** (History)
- ChatGPT: mentioned, #5 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Elkhorn Ranch, Maltese Cross Cabin, Chateau de Mores, Painted Canyon. Described as: "([trlibrary.com](https://www.trlibrary.com/tr/badlands/where-to-see?utm_source=openai)) … - Theodore Roosevelt Presidential Library (Medora area) — museum/exhibits focused on Roosevelt’s life and legacy in the Badlands (and programming tied to the park and region)." Sources: nps.gov, trlibrary.com, medora.com, theodorerooseveltcenter.org, history.nd.gov
- Gemini: mentioned, #1 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Elkhorn Ranch, Chateau de Mores. Described as: "* **Theodore Roosevelt Presidential Library (Medora):**" Sources: trlibrary.com, discovermedora.com

**What historic sites are connected to Theodore Roosevelt?** (History)
- ChatGPT: NOT mentioned. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Elkhorn Ranch, Mount Rushmore. Sources: nps.gov, home.nps.gov
- Gemini: NOT mentioned. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Elkhorn Ranch, Mount Rushmore. Sources: none

**Is the Theodore Roosevelt Presidential Library worth visiting?** (Brand)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Medora Musical. Described as: "Short answer: Yes — for most visitors who care about Theodore Roosevelt, conservation history, or the North Dakota Badlands, the Theodore Roosevelt Presidential Library in Medora is worth a visit. … ([trlibrary.com](https://www.trlibrary.com/?utm_source=openai))" Sources: trlibrary.com, governor.nd.gov, peacegardenalmanac.com, nd.gov
- Gemini: mentioned, #1 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Medora Musical, Chateau de Mores. Described as: "**Yes, the Theodore Roosevelt Presidential Library is well worth visiting**, particularly if you pair it with a trip to Theodore Roosevelt National Park and the surrounding North Dakota Badlands. … If you appreciate American history, modern architecture, or the national park system, the TR Presidential Library is an exceptional stop that delivers an experience far beyond typical museum exhibits." Sources: eastwingmagazine.com, shebuystravel.com, trlibrary.com, nd.gov, youtube.com, aaqeastend.com

**How much time do I need at the Theodore Roosevelt Presidential Library?** (Brand)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park. Described as: "([trlibrary.com](https://www.trlibrary.com/visit/faq/during-your-visit?utm_source=openai)) … ([trlibrary.com](https://www.trlibrary.com/visit/tours?utm_source=openai))" Sources: trlibrary.com
- Gemini: mentioned, #1 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park. Described as: "For a visit to the **Theodore Roosevelt Presidential Library** in Medora, North Dakota, plan for about **3.5 to 4 hours**:" Sources: trlibrary.com, medora.com, nd.gov

**How much are tickets to the Theodore Roosevelt Presidential Library and when is it open?** (Brand)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Described as: "([trlibrary.com](https://www.trlibrary.com/tickets)) … (Winter hours begin Dec 1.) ([trlibrary.com](https://www.trlibrary.com/visit/hours?utm_source=openai))" Sources: trlibrary.com
- Gemini: mentioned, #1 among attractions, cites trlibrary.com. Also named: Maah Daah Hey Trail. Described as: "Admission details and operating hours for the **Theodore Roosevelt Presidential Library** (located in Medora, North Dakota) are detailed below:" Sources: trlibrary.com, museumsatlas.com, ndtourism.com

**What were Theodore Roosevelt's major accomplishments, conservation work, and legacy?** (Auto: History)
- ChatGPT: NOT mentioned. Also named: Mount Rushmore. Sources: none
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

**What years was Theodore Roosevelt president, and what were the dates of his administration?** (Auto: History)
- ChatGPT: NOT mentioned. Sources: none
- Gemini: NOT mentioned. Sources: none

**Which four presidents are on Mount Rushmore, and why was Theodore Roosevelt included among them?** (Auto: History)
- ChatGPT: NOT mentioned. Sources: none
- Gemini: NOT mentioned. Also named: Mount Rushmore. Sources: none

**What is the meaning and origin of the term bully pulpit in American politics?** (Auto: History)
- ChatGPT: NOT mentioned. Sources: dictionary.com, etymonline.com, cgi.pbs.org
- Gemini: NOT mentioned. Sources: none

**What was the Roosevelt Corollary to the Monroe Doctrine and why does it matter?** (Auto: History)
- ChatGPT: NOT mentioned. Sources: none
- Gemini: NOT mentioned. Sources: none

### Sites AI assistants cite most
trlibrary.com (15), ndtourism.com (10), medora.com (10), nps.gov (7), home.nps.gov (5), en.wikipedia.org (5), nd.gov (4), medorand.org (3), history.nd.gov (3), mdhta.com (2), discovermedora.com (2), visitdickinson.com (2), youtube.com (2), parkrec.nd.gov (1), foundation.medora.com (1)

### Searches the assistants ran before answering
Searches the assistants ran before answering. 'Google' is trlibrary.com's Search Console position for the same search (last 28 days); none means the site doesn't show for it, or too rarely to report. A search we don't rank for is a page to strengthen or write. 127 different searches: we rank top 10 for 2, lower for 0, not at all for 125.

| Search the assistant ran | Engines | In answers missing us | trlibrary.com in Google |
|---|---|---|---|
| Bonanzaville West Fargo Cass County Historical Society museum | ChatGPT | 1 | – |
| Chateau de Mores Medora museum | ChatGPT | 1 | – |
| Chateau de Mores State Historic Site Medora North Dakota activities Maah Daah Hey Trail | ChatGPT | 1 | – |
| Chateau de Mores State Historic Site Medora hours activities North Dakota State Historical Society | ChatGPT | 1 | – |
| Dakota Dinosaur Museum Dickinson Dickinson Museum Center official site | ChatGPT | 1 | – |
| Dakota Territory Air Museum Minot official site | ChatGPT | 1 | – |
| Fort Union Trading Post National Historic Site Williston North Dakota | ChatGPT | 1 | – |
| Maah Daah Hey Trail Medora trailhead mountain biking hiking | ChatGPT | 1 | – |
| Medora Musical Burning Hills Amphitheatre schedule Pitchfork Fondue medora.com | ChatGPT | 1 | – |
| Mount Rushmore Theodore Roosevelt connection NPS | ChatGPT | 1 | – |
| National Buffalo Museum Jamestown official site | ChatGPT | 1 | – |
| North Dakota Heritage Center & State Museum Bismarck official site | ChatGPT | 1 | – |
| Pembina State Museum North Dakota museum | ChatGPT | 1 | – |
| Pitchfork Steak Fondue Medora details what is it Pitchfork Steak Fondue medora.com | ChatGPT | 1 | – |
| Plains Art Museum Fargo official site | ChatGPT | 1 | – |
| Roger Maris Museum Fargo museum | ChatGPT | 1 | – |
| Sagamore Hill National Historic Site NPS official site | ChatGPT | 1 | – |
| Sagamore Hill National Historic Site Theodore Roosevelt details NPS | ChatGPT | 1 | – |
| Saint-Gaudens National Historical Park Theodore Roosevelt connection | ChatGPT | 1 | – |
| Scandinavian Heritage Park Minot museum | ChatGPT | 1 | – |

### Pages AI cites when it leaves the Library out
Pages cited in answers that left the Library out. 'Mentions the Library' comes from reading the page once (blank = not read or couldn't be read). A list that names other attractions but not the Library is the cheapest fix: ask to be added. 30 answers left the Library out. Citations by type: partner 14, reference 13, other 11, list or guide 1, forum 1.

| Page | Type | Answers | Mentions the Library | Attractions it helped name |
|---|---|---|---|---|
| https://medora.com | partner | 2 | yes | North Dakota Cowboy Hall of Fame, Chateau de Mores, Theodore Roosevelt National Park, Maltese Cross Cabin |
| https://ndtourism.com | partner | 2 | – | North Dakota Cowboy Hall of Fame, Chateau de Mores, Theodore Roosevelt National Park, Maltese Cross Cabin |
| https://home.nps.gov/thro/planyourvisit/south-unit.htm | reference | 1 | NO | Theodore Roosevelt National Park, Medora Musical, Pitchfork Steak Fondue, Maah Daah Hey Trail |
| https://medora.com/showcase | partner | 1 | yes | Theodore Roosevelt National Park, Medora Musical, Pitchfork Steak Fondue, Maah Daah Hey Trail |
| https://medora.com/pitchforksteakfondue | partner | 1 | yes | Theodore Roosevelt National Park, Medora Musical, Pitchfork Steak Fondue, Maah Daah Hey Trail |
| https://www.ndtourism.com/articles/maah-daah-hey-trail | partner | 1 | – | Theodore Roosevelt National Park, Medora Musical, Pitchfork Steak Fondue, Maah Daah Hey Trail |
| https://www.history.nd.gov/historicsites/chateau | reference | 1 | NO | Theodore Roosevelt National Park, Medora Musical, Pitchfork Steak Fondue, Maah Daah Hey Trail |
| https://medora.com/attractions-activities | partner | 1 | yes | Theodore Roosevelt National Park, Medora Musical, Pitchfork Steak Fondue, Maah Daah Hey Trail |
| https://foundation.medora.com/wp-content/uploads/2025/12/2025-Summer-Notes-from-the-Trail-compressed.pdf | partner | 1 | – | Theodore Roosevelt National Park, Medora Musical, Pitchfork Steak Fondue, Maah Daah Hey Trail |
| https://en.wikipedia.org/wiki/Medora%2C_North_Dakota | reference | 1 | yes | Theodore Roosevelt National Park, Medora Musical, Pitchfork Steak Fondue, Maah Daah Hey Trail |
| https://statemuseum.nd.gov/sites/default/files/StateMuseumBrochure.pdf | reference | 1 | – |  |
| https://www.ndtourism.com/fargo/attractions-entertainment/arts-attractions/plains-art-museum | partner | 1 | – |  |
| https://www.bonanzaville.org | other | 1 | NO |  |
| https://business.jamestownchamber.com/list/member/north-american-bison-discovery-center-71 | other | 1 | NO |  |
| https://en.wikipedia.org/wiki/Badlands_Dinosaur_Museum | reference | 1 | NO |  |
| https://www.ndtourism.com/minot/attractions-entertainment/aviation-flight/dakota-territory-air-museum | partner | 1 | – |  |
| https://www.ndtourism.com/minot/attractions-entertainment/educational-attractions/scandinavian-heritage-park | partner | 1 | – |  |
| https://www.nps.gov/places/fort-union-trading-post-national-historic-site.htm | reference | 1 | – |  |
| https://www.ndtourism.com/grand-forks/attractions-entertainment/arts-attractions/north-dakota-museum-art | partner | 1 | – |  |
| https://westacres.com/attractions/roger-maris-museum/museum | other | 1 | – |  |

**Ask to be added** (cited by AI, lists other things, doesn't mention the Library):
- https://www.bonanzaville.org (other; cited in 1 answers)
- https://business.jamestownchamber.com/list/member/north-american-bison-discovery-center-71 (other; cited in 1 answers)

What to do by type:
- **list or guide**: Ask to be added: find the author or an update/contact link; offer a short blurb and a photo.
- **review or booking**: Keep the Library's listing complete and current on this site (photos, hours, description, category).
- **forum**: Answer helpfully where the community allows it, as the Library, with a link only when it answers the question.
- **reference**: Make sure the facts there are right; for Wikipedia, suggest edits on the talk page with sources (no self-promotion).
- **news**: Pitch a story or update; news pages that list attractions get reused by AI answers for months.
- **partner**: Ask the partner to name and link the Library on this page.
- **attraction**: No action on their page. Check that our own page answers the same question as well.
- **owned**: Our page is being read. Make sure it answers the question near the top.
- **social**: Low priority: AI rarely relies on social pages for recommendations.
- **other**: Read the page: if it's a list of things to do, ask to be added.

## Site audit
Crawled 1149 of 1189 sitemap URLs. Health 95/100, AI readiness 61/100. llms.txt on trlibrary.com: yes. AI crawlers blocked in robots.txt: none. 412 pages have page-specific structured data (sitewide on every page: BreadcrumbList, EntryPoint, GeoCoordinates, ImageObject, ListItem, OpeningHoursSpecification, PostalAddress, SearchAction, WebSite).

| Severity | Issue | Pages | Examples |
|---|---|---|---|
| medium | Same title as another page | 69 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /node/240, /node/241 |
| medium | Sitemap lists a /node/ URL instead of a readable path | 35 | /node/240, /node/241, /node/244, /node/245, /node/249 |
| medium | No H1 heading | 29 | /birthdaycard, /project/how-the-library-works, /rsvp/midwinter, /about/reports/2024-annual-report, /privacy |
| medium | Missing Open Graph tags | 27 | /birthdaycard, /project/how-the-library-works, /rsvp/midwinter, /quiz/the-boardwalk, /video/view/-QfzHHXPYqM |
| medium | No meta description | 26 | /birthdaycard, /project/how-the-library-works, /rsvp/midwinter, /quiz/the-boardwalk, /video/view/-QfzHHXPYqM |
| medium | Sitemap lists a URL that redirects | 5 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /calendar/special-event/book-signing-and-meet-greet-kennerly-balkowitsch-and-ziemendorf, /event/24 |
| low | Title over 60 characters, not counting the site-name suffix | 263 | /node/240, /node/241, /node/244, /node/245, /node/249 |
| low | Under 150 words of body text | 238 | /birthdaycard, /project/how-the-library-works, /node/240, /node/241, /node/244 |
| low | Heading levels skip (e.g. H2 straight to H4) | 153 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /calendar/special-event/book-signing-and-meet-greet-kennerly-balkowitsch-and-ziemendorf, /node/589 |
| low | Title under 15 characters, not counting the site-name suffix | 144 | /birthdaycard, /quiz/the-boardwalk, /visit/survey, /video/view/YJ_qzszUZUA, /video/view/Y3jQTzNVVFY |
| low | Took over 3 seconds to respond | 137 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /video/view/iZNTkHl0WUM, /video/view/YJ_qzszUZUA |
| low | More than 4 clicks from the homepage | 135 | /node/240, /node/241, /node/244, /node/245, /node/249 |
| low | Same meta description as another page | 131 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /calendar/special-event/book-signing-and-meet-greet-kennerly-balkowitsch-and-ziemendorf, /event/24 |
| low | Meta description under 70 characters | 18 | /video/view/YJ_qzszUZUA, /video/view/Y3jQTzNVVFY, /video/view/Lk8bs9ilpLI, /video/view/0NiRkijqLGw, /video/view/NoLhSWhiCpA |
| low | More than one H1 | 10 | /support/matching-gifts, /about/mission, /about/foundation, /impact, /project |

## Recently changed pages (held back from recommendations for 28 days)
Before = the 28 days before the change; after = the days since, up to the latest settled Search Console day. Compare per-day numbers; a week or two after a change is still early.

| Page | Changed | What | Clicks/day before → after | CTR | Position |
|---|---|---|---|---|---|
| /tickets | 2026-11-16 | Title 'Tickets and Admission: Timed Entry and Prices'; prices, 3½ hours and discounts in d | 69.0 → 43.8 | 4.2% → 3.7% | 3.0 → 3.0 |
| /tr/presidency/nobel-peace-prize | 2026-11-16 | Title 'Why Theodore Roosevelt Won the Nobel Peace Prize'; Portsmouth and first American No | 2.4 → 2.8 | 0.6% → 0.6% | 4.5 → 3.9 |
| /tr/presidency/foreign-policy | 2026-11-16 | Title 'Theodore Roosevelt’s Foreign Policy: The Big Stick Era'; Panama Canal and Great Whi | 3.0 → 6.5 | 0.6% → 0.6% | 4.7 → 5.5 |
| /visit/itineraries/enchanted-highway | 2026-11-16 | Title adds 'North Dakota' | 0.6 → 0.5 | 0.5% → 0.3% | 8.2 → 8.1 |
| /visit/itineraries/sturgis-medora | 2026-11-16 | Removed past rally dates ('runs 7–16 August 2026' → 'Every August') | 0.0 → 0.2 | 0.0% → 1.4% | 7.8 → 7.5 |
| /visit/itineraries/presidential-libraries | 2026-11-16 | Hoover museum: 'reopens on 6 August 2026' → 'has reopened after a $20 million renovation' | 0.6 → 0.5 | 1.6% → 1.3% | 6.9 → 7.7 |
| /visit/scenic-drives | 2026-11-16 | Loop drive: dropped 'late 2025' from reopening | 0.1 → 0.0 | 0.8% → 0.0% | 7.8 → 7.0 |
| /tr/rise-to-power/spanish-american-war | 2026-11-09 | Title 'Theodore Roosevelt and the Spanish-American War'; Navy/Rough Riders description | 6.4 → 11.1 | 0.5% → 0.7% | 5.7 → 5.6 |
| /tr/presidency/food-and-drug | 2026-11-09 | Title 'Pure Food and Drug Act and Meat Inspection Act of 1906'; drops '1905 novel' | 10.6 → 22.1 | 0.9% → 1.1% | 5.3 → 4.6 |
| /tr/people/archibald | 2026-11-09 | Title 'Archibald Roosevelt: TR’s Son Wounded in Two World Wars' | 0.1 → 0.3 | 0.1% → 0.1% | 7.4 → 7.5 |
| /visit/lodging | 2026-11-09 | Title 'Medora Hotels, Cabins and Campgrounds'; names Hotel 1883 | 4.8 → 2.3 | 0.9% → 0.5% | 7.7 → 7.4 |
| /join-us | 2026-11-09 | Title 'Join Us: Become a Member, Volunteer or Work Here'; first description and OG tags | 0.0 → 0.1 | 0.0% → 0.0% | 4.4 → 3.2 |
| /visit/exhibits/kennerly | 2026-11-09 | Title 'In the Room: David Hume Kennerly Photo Exhibition'; first description and OG tags | 2.3 → 2.7 | 2.4% → 1.8% | 6.5 → 5.5 |
| /about/trustees/kermit-roosevelt | 2026-11-09 | Title 'Kermit Roosevelt, Library Trustee' (was duplicate of /tr/people/kermit) | 0.4 → 0.1 | 0.5% → 0.1% | 6.9 → 6.1 |
| /about/trustees/douglas-brinkley | 2026-11-09 | Title 'Douglas Brinkley, Library Trustee' (was duplicate of podcast page) | 0.1 → 0.1 | 0.4% → 0.2% | 10.2 → 12.9 |
| /contact | 2026-11-09 | Title 'Contact Us: Phone, Address and Message Form'; phone and address in description | 1.9 → 1.8 | 1.0% → 1.3% | 2.9 → 3.0 |
| /visit/tickets/plan-ahead | 2026-11-09 | Description no longer leads with summer; removed '2026 is the Library's first year' | 0.6 → 0.2 | 1.3% → 0.5% | 6.7 → 7.7 |
| /llms.txt | 2026-11-09 | Added 'Key facts for visitors' (address, 3½ hours, year-round, tickets, indoor, not the FD | 0.0 → 0.0 | – → – | – → – |
| /about/press/press-releases | 2026-11-03 | Press releases: og:type article, NewsArticle author/publisher/description, ISO dates with  | 0.0 → 0.0 | 0.0% → – | 11.0 → – |
| /podcast/good-citizen | 2026-11-03 | Podcast episodes: og:type article | 1.3 → 0.8 | 1.5% → 1.1% | 7.1 → 7.6 |
| /about/trustees | 2026-11-03 | Trustee Person markup: memberOf the Library | 1.9 → 1.5 | 9.8% → 9.9% | 9.0 → 6.8 |
| /tr/presidency | 2026-11-03 | Published Oct 18 draft plus 2 internal links (Taft, midnight forests) | 0.9 → 4.4 | 0.6% → 1.0% | 6.3 → 5.3 |
| /tr/timeline | 2026-11-03 | Added 6 internal links from Links to add; Title 'Theodore Roosevelt's Life Timeline: Key D | 7.8 → 7.7 | 0.5% → 0.4% | 7.4 → 6.6 |
| /visit/exhibits/main | 2026-11-03 | Added 6 internal links from Links to add | 2.8 → 1.6 | 1.8% → 0.8% | 6.5 → 6.0 |
| /tr/teddy-nickname | 2026-11-03 | Added 6 internal links from Links to add; Merged /tr/myths/teddy-name into this page; new  | 4.8 → 5.5 | 0.8% → 0.8% | 4.4 → 4.7 |
| /tr/presidency-timeline | 2026-11-03 | Added 6 internal links from Links to add; Title 'When Was Theodore Roosevelt President? 19 | 11.5 → 11.9 | 0.6% → 0.6% | 4.6 → 4.5 |
| /tr/people/henry-cabot-lodge | 2026-11-03 | Added 6 internal links from Links to add | 1.1 → 1.4 | 0.2% → 0.3% | 6.5 → 6.4 |
| /tr/family/family-tree | 2026-11-03 | Added 5 internal links from Links to add | 14.2 → 15.4 | 1.5% → 1.1% | 5.2 → 4.9 |
| /tr/presidency/white-house-family | 2026-11-03 | Added 4 internal links from Links to add | 0.2 → 0.5 | 0.3% → 0.5% | 6.6 → 7.5 |
| /podcast/good-citizen/doris-kearns-goodwin-presidential-stories-trpl-and-enduring-lessons-theodore | 2026-11-03 | Added 5 internal links from Links to add | 0.3 → 0.3 | 0.8% → 0.9% | 8.8 → 9.0 |
| /tr/legacy/rankings | 2026-11-03 | Added 5 internal links from Links to add | 5.0 → 7.9 | 1.5% → 1.8% | 5.6 → 6.2 |
| /podcast/good-citizen/edward-okeefe | 2026-11-03 | Added 4 internal links from Links to add | 0.1 → 0.2 | 0.8% → 1.8% | 8.2 → 7.6 |
| /podcast/good-citizen/call-adventure-charlie-melcher-ed-okeefe-and-brand-new-theodore-roosevelt | 2026-11-03 | Added 6 internal links from Links to add | 0.3 → 0.1 | 1.1% → 0.4% | 7.4 → 7.1 |
| /tr/for-educators/high-school | 2026-11-03 | Added 6 internal links from Links to add | 0.8 → 0.8 | 1.8% → 1.4% | 7.0 → 6.9 |
| /about/press/press-releases/theodore-roosevelts-groundbreaking-firsts-and-feats-celebration | 2026-11-03 | Added 6 internal links from Links to add | 0.1 → 0.4 | 1.1% → 1.5% | 4.7 → 6.2 |
| /tr/rise-to-power/ten-facts | 2026-11-03 | Added 6 internal links from Links to add | 3.3 → 5.0 | 1.6% → 2.7% | 5.3 → 4.2 |
| /tr/presidency/ten-facts | 2026-11-03 | Added 5 internal links from Links to add | 15.5 → 22.1 | 2.8% → 4.0% | 3.9 → 3.7 |
| /events/teddycon | 2026-11-03 | Added 6 internal links from Links to add | 3.4 → 0.2 | 8.8% → 1.2% | 3.8 → 5.8 |
| /tr/badlands-timeline | 2026-11-03 | Added 6 internal links from Links to add | 5.7 → 6.0 | 2.0% → 2.2% | 5.5 → 5.4 |
| /tr/family/fdr-connection | 2026-11-03 | Added 4 internal links from Links to add; Title 'How Were Theodore and Franklin Roosevelt  | 60.9 → 69.0 | 1.9% → 2.1% | 3.2 → 2.9 |
| /research/archives | 2026-11-03 | Added 5 internal links from Links to add | 1.7 → 1.5 | 2.5% → 2.1% | 7.7 → 7.9 |
| /tr/speeches/new-nationalism | 2026-11-03 | Added 5 internal links from Links to add | 1.7 → 0.2 | 2.0% → 0.5% | 5.6 → 7.4 |
| /tr/presidency/elections | 2026-11-03 | Added 4 internal links from Links to add; Title '1904 Presidential Election: Roosevelt's M | 4.5 → 6.6 | 0.6% → 1.2% | 5.9 → 5.3 |
| /tr/legacy/the-library | 2026-11-03 | Added 5 internal links from Links to add | 1.2 → 0.5 | 1.0% → 1.6% | 5.0 → 4.8 |
| /tr/post-presidency/ten-facts | 2026-11-03 | Added 5 internal links from Links to add | 0.4 → 0.5 | 1.0% → 1.5% | 5.5 → 5.9 |
| /visit/medora/history | 2026-11-03 | Added 5 internal links from Links to add; North Dakota quote aligned to the 1918 Volwiler  | 1.2 → 0.6 | 1.2% → 1.2% | 7.4 → 7.9 |
| /tr/fake-quotes | 2026-11-03 | Added 3 internal links from Links to add | 11.7 → 12.5 | 2.0% → 2.2% | 6.8 → 6.2 |
| /tr/kids-timeline | 2026-11-03 | Added 5 internal links from Links to add; Title 'Theodore Roosevelt for Kids: A Timeline o | 2.5 → 2.5 | 0.7% → 0.9% | 9.4 → 10.6 |
| /tr/tr-mount-rushmore | 2026-11-03 | Added 3 internal links from Links to add; Title 'Mount Rushmore Presidents: Why Theodore R | 16.0 → 16.0 | 0.4% → 0.2% | 5.5 → 6.6 |
| /visit/directions | 2026-11-03 | Added 4 internal links from Links to add; Title 'Directions to Medora from I-94 and Nearby | 21.1 → 7.6 | 1.2% → 0.8% | 2.7 → 3.5 |
| /tr/books-and-writings/autobiography | 2026-11-03 | Added 4 internal links from Links to add | 1.1 → 1.2 | 1.3% → 1.7% | 5.7 → 4.9 |
| /tr/pre-presidency-political-accomplishments | 2026-11-03 | Added 4 internal links from Links to add; Title 'What Did Theodore Roosevelt Do Before He  | 20.5 → 13.5 | 1.1% → 0.8% | 5.6 → 5.6 |
| /tr/books-and-writings/complete-list | 2026-11-03 | Added 4 internal links from Links to add | 0.2 → 0.1 | 1.9% → 1.4% | 5.4 → 5.0 |
| /tr/quotes/leadership | 2026-11-03 | Added 5 internal links from Links to add | 3.6 → 2.5 | 3.0% → 2.5% | 5.4 → 5.3 |
| /tr/speeches/inaugural | 2026-11-03 | Added 4 internal links from Links to add | 0.5 → 0.9 | 0.5% → 0.7% | 5.7 → 6.1 |
| /podcast/good-citizen/candice-millard | 2026-11-03 | Added 2 internal links from Links to add | 0.4 → 0.4 | 0.3% → 0.3% | 9.3 → 10.0 |
| /tr/people/eleanor | 2026-11-03 | Added 4 internal links from Links to add | 0.4 → 1.4 | 0.5% → 0.5% | 6.9 → 7.3 |
| /tr/people/bill-sewall | 2026-11-03 | Added 4 internal links from Links to add | 0.6 → 0.4 | 2.2% → 1.0% | 5.5 → 5.2 |
| /tr/post-presidency/quentin | 2026-11-03 | Added 4 internal links from Links to add | 1.0 → 1.2 | 0.4% → 0.6% | 9.5 → 9.3 |
| /tr/quotes/conservation | 2026-11-03 | Added 2 internal links from Links to add | 3.4 → 4.4 | 1.9% → 2.9% | 5.3 → 4.9 |
| /podcast/good-citizen/karl-rove-historic-redemption-hard-work-politics-and-essential-nature | 2026-11-03 | Added 3 internal links from Links to add | 1.8 → 3.6 | 0.1% → 0.3% | 9.2 → 7.3 |
| /tr/early-life/siblings | 2026-11-03 | Added 3 internal links from Links to add | 1.2 → 1.2 | 1.2% → 0.8% | 6.3 → 6.1 |
| /tr/early-life/ten-facts | 2026-11-03 | Added 4 internal links from Links to add | 0.4 → 0.3 | 3.6% → 1.9% | 5.4 → 5.8 |
| /tr/people/kermit | 2026-11-03 | Added 4 internal links from Links to add | 0.2 → 0.4 | 0.4% → 0.3% | 8.6 → 8.7 |
| /tr/legacy | 2026-11-03 | Added 3 internal links from Links to add | 0.1 → 0.1 | 0.8% → 0.7% | 8.8 → 6.9 |
| /tr/people/bamie | 2026-11-03 | Added 3 internal links from Links to add | 0.2 → 0.5 | 0.5% → 0.6% | 6.0 → 6.7 |
| /tr/early-life | 2026-11-03 | Added 3 internal links from Links to add | 5.2 → 9.2 | 0.9% → 1.8% | 6.7 → 6.6 |
| /podcast/good-citizen/jeffrey-rosen | 2026-11-03 | Added 3 internal links from Links to add | 0.2 → 0.2 | 0.3% → 0.4% | 10.2 → 10.8 |
| /tr/complex-legacy/imperialism | 2026-11-03 | Added 2 internal links from Links to add | 8.3 → 13.8 | 1.0% → 1.0% | 5.2 → 5.1 |
| /tr/strenuous-life/hunter | 2026-11-03 | Added 3 internal links from Links to add | 1.2 → 1.5 | 0.9% → 1.1% | 5.6 → 5.1 |
| /tr/tr-shot | 2026-11-03 | Added 3 internal links from Links to add; Title 'Why Was Theodore Roosevelt Shot? The 1912 | 11.4 → 8.8 | 0.9% → 1.1% | 4.0 → 4.4 |
| /visit/itineraries/chicago-badlands | 2026-11-03 | Added 2 internal links from Links to add; Visit length and restaurant name | 0.8 → 0.5 | 1.6% → 1.2% | 6.9 → 6.7 |
| /tr/post-presidency/death | 2026-11-03 | Added 3 internal links from Links to add | 2.8 → 6.0 | 0.5% → 0.8% | 5.5 → 4.7 |
| /tr/new-york-politics/alice-lee | 2026-11-03 | Added 3 internal links from Links to add | 3.0 → 3.8 | 0.8% → 0.9% | 5.5 → 5.3 |
| /tr/square-deal | 2026-11-03 | Added 2 internal links from Links to add; Archived (node 278); 301 to /tr/presidency/squar | 31.8 → 0.1 | 0.8% → 0.9% | 3.9 → 1.8 |
| /tr/rise-to-power/edith-roosevelt | 2026-11-03 | Added 3 internal links from Links to add | 1.5 → 1.5 | 0.4% → 0.4% | 6.9 → 8.8 |
| /tr/presidency/conservation/midnight-forests | 2026-11-03 | Added 3 internal links from Links to add | 1.1 → 1.6 | 1.3% → 1.8% | 5.1 → 5.0 |
| /tr/quotes/misquotes | 2026-11-03 | Added 3 internal links from Links to add | 5.5 → 7.8 | 2.6% → 2.3% | 4.0 → 4.2 |
| /tr/post-presidency/man-in-the-arena | 2026-11-03 | Added 3 internal links from Links to add; Title 'TR's 1910 European Tour and the Man in th | 1.6 → 1.2 | 0.8% → 1.0% | 7.5 → 7.2 |
| /visit/activities | 2026-11-03 | Added 3 internal links from Links to add; Visit length and restaurant name | 0.5 → 0.5 | 0.9% → 1.4% | 5.3 → 6.8 |
| /tr/conservation/by-the-numbers | 2026-11-03 | Added 3 internal links from Links to add | 1.6 → 2.6 | 0.6% → 1.1% | 5.1 → 4.4 |
| /tr/presidency/conservation/gifford-pinchot | 2026-11-03 | Added 2 internal links from Links to add | 1.6 → 2.4 | 0.6% → 0.9% | 4.4 → 4.1 |
| /tr/early-life/family-roots | 2026-11-03 | Added 3 internal links from Links to add | 1.5 → 3.1 | 0.8% → 1.4% | 4.8 → 5.0 |
| /podcast/good-citizen/live-trpl-1-doris-kearns-goodwin-finding-hope-history | 2026-11-03 | Added 3 internal links from Links to add | 0.1 → 0.1 | 0.7% → 0.9% | 8.8 → 9.8 |
| /tr/homes-and-places/sagamore-hill | 2026-11-03 | Added 2 internal links from Links to add | 0.4 → 0.4 | 0.7% → 0.3% | 7.0 → 7.5 |
| /tr/presidency/conservation/national-monuments | 2026-11-03 | Added 3 internal links from Links to add | 0.9 → 1.4 | 0.8% → 1.0% | 5.5 → 5.4 |
| /tr/presidency/white-house-family/pets | 2026-11-03 | Added 3 internal links from Links to add | 2.2 → 3.3 | 1.2% → 1.9% | 5.1 → 4.6 |
| /visit/teddy-trail | 2026-11-03 | Added 3 internal links from Links to add | 0.3 → 0.4 | 1.2% → 1.4% | 6.4 → 9.2 |
| /visit/exhibits | 2026-11-03 | Added 3 internal links from Links to add; Title: Exhibits: Roosevelt’s Life in Eight Chapt | 3.8 → 0.7 | 0.6% → 0.3% | 3.5 → 5.4 |
| /tr/people | 2026-11-03 | Added 3 internal links from Links to add | 0.8 → 0.4 | 0.4% → 0.6% | 7.4 → 7.9 |
| /about/trustees/doris-kearns-goodwin | 2026-11-03 | Added 3 internal links from Links to add | 0.2 → 0.2 | 0.8% → 0.6% | 16.0 → 14.2 |
| /tr/people/william-howard-taft | 2026-11-03 | Added 3 internal links from Links to add | 1.8 → 4.8 | 0.3% → 0.5% | 5.7 → 5.1 |
| /about/press/press-releases/theodore-roosevelt-presidential-library-opening-celebrations-july-4-2026 | 2026-11-03 | Added 3 internal links from Links to add | 1.9 → 1.6 | 2.9% → 2.8% | 4.4 → 5.5 |
| /tr | 2026-11-03 | Added 3 internal links from Links to add | 0.3 → 0.5 | 0.1% → 0.1% | 6.9 → 5.2 |
| /tr/post-presidency | 2026-11-03 | Added 3 internal links from Links to add | 1.8 → 2.1 | 2.6% → 2.1% | 4.2 → 4.1 |
| /tr/new-york-politics/double-tragedy | 2026-11-03 | Added 3 internal links from Links to add | 0.5 → 1.5 | 1.6% → 1.7% | 4.4 → 4.8 |
| /tr/quotes/family | 2026-11-03 | Added 2 internal links from Links to add | 0.3 → 0.9 | 2.3% → 2.8% | 6.2 → 5.9 |
| /tr/people/alice-lee | 2026-11-03 | Added 3 internal links from Links to add | 0.1 → 1.1 | 0.3% → 1.5% | 8.8 → 8.4 |
| /about/press/press-releases/harold-hamm-donates-50-million-trpl | 2026-11-03 | Added 2 internal links from Links to add | 1.7 → 0.4 | 10.5% → 4.3% | 3.1 → 5.5 |
| /tr/people/theodore-sr | 2026-11-03 | Added 2 internal links from Links to add | 0.4 → 0.9 | 0.2% → 0.7% | 6.5 → 5.9 |
| /about/press/press-releases/roosevelt-family-acquires-903-acres-trpl | 2026-11-03 | Added 2 internal links from Links to add | 0.6 → 0.4 | 7.0% → 7.4% | 4.2 → 5.5 |
| /tr/legacy/mount-rushmore | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.8 | 0.2% → 0.4% | 7.1 → 6.5 |
| /tr/conservation/quotes | 2026-11-03 | Added 3 internal links from Links to add | 0.5 → 1.9 | 1.4% → 1.2% | 4.9 → 4.8 |
| /visit/itineraries/north-on-29 | 2026-11-03 | Added 2 internal links from Links to add | 0.3 → 0.2 | 0.8% → 0.6% | 7.2 → 7.5 |
| /tr/rise-to-power/police-commissioner | 2026-11-03 | Added 2 internal links from Links to add | 1.8 → 1.6 | 1.7% → 1.5% | 5.7 → 5.5 |
| /tr/legacy/words-he-coined | 2026-11-03 | Added 2 internal links from Links to add | 0.9 → 1.1 | 0.6% → 0.8% | 6.4 → 6.5 |
| /tr/myths/misquotes | 2026-11-03 | Added 2 internal links from Links to add | 1.1 → 2.0 | 1.1% → 1.8% | 5.2 → 6.2 |
| /tr/quotes | 2026-11-03 | Added 2 internal links from Links to add | 21.7 → 17.8 | 2.3% → 2.5% | 10.7 → 3.8 |
| /tr/presidency/first-term | 2026-11-03 | Added 2 internal links from Links to add | 0.5 → 1.2 | 1.7% → 2.4% | 6.5 → 5.9 |
| /visit/itineraries/13-day-denver-wyoming | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.8% → 0.0% | 8.9 → 8.5 |
| /tr/family/children | 2026-11-03 | Added 2 internal links from Links to add; Title 'Theodore Roosevelt's Children: Alice, Ted | 4.2 → 8.5 | 1.1% → 1.9% | 4.2 → 3.6 |
| /visit/shopping | 2026-11-03 | Added 2 internal links from Links to add | 5.0 → 4.3 | 2.2% → 3.9% | 5.0 → 8.0 |
| /tr/family | 2026-11-03 | Added 2 internal links from Links to add | 1.1 → 1.6 | 0.4% → 0.3% | 8.0 → 7.9 |
| /tr/for-educators/middle-school | 2026-11-03 | Added 2 internal links from Links to add | 0.6 → 1.4 | 2.2% → 3.6% | 6.5 → 6.3 |
| /visit/medora | 2026-11-03 | Added 1 internal link from Links to add | 1.1 → 0.3 | 0.7% → 0.3% | 4.5 → 5.0 |
| /tr/rise-to-power/buffalo-soldiers | 2026-11-03 | Added 1 internal link from Links to add | 1.6 → 1.6 | 0.7% → 0.7% | 5.2 → 4.9 |
| /tr/early-life/harvard | 2026-11-03 | Added 2 internal links from Links to add | 0.9 → 2.4 | 1.0% → 1.7% | 5.4 → 5.2 |
| /tr/elkhorn | 2026-11-03 | Added 2 internal links from Links to add | 1.6 → 1.6 | 0.8% → 0.9% | 8.0 → 7.9 |
| /podcast/good-citizen/ted-leonsis | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.1 | 0.2% → 0.1% | 10.0 → 8.8 |
| /tr/presidency/conservation/national-parks | 2026-11-03 | Added 2 internal links from Links to add | 6.9 → 8.0 | 0.9% → 1.2% | 6.0 → 5.3 |
| /bullet-speech | 2026-11-03 | Added 1 internal link from Links to add; Title 'The Bullet Speech: Roosevelt's Assassinati | 24.4 → 22.2 | 1.7% → 1.5% | 3.7 → 3.6 |
| /tr/early-life/mother | 2026-11-03 | Added 2 internal links from Links to add | 0.3 → 0.4 | 0.3% → 0.4% | 5.1 → 4.7 |
| /tr/post-presidency/river-of-doubt | 2026-11-03 | Added 2 internal links from Links to add | 2.6 → 4.4 | 0.6% → 0.7% | 7.5 → 7.6 |
| /tr/post-presidency/african-safari | 2026-11-03 | Added 2 internal links from Links to add | 1.2 → 1.2 | 1.3% → 1.4% | 5.9 → 6.2 |
| /tr/post-presidency/new-nationalism | 2026-11-03 | Added 2 internal links from Links to add | 1.8 → 2.1 | 0.7% → 0.8% | 4.5 → 4.6 |
| /tr/presidency/conservation/reclamation | 2026-11-03 | Added 2 internal links from Links to add | 3.3 → 2.7 | 0.8% → 0.9% | 4.2 → 3.6 |
| /tr/5-big-adventures | 2026-11-03 | Added 2 internal links from Links to add | 2.0 → 1.4 | 1.0% → 0.7% | 6.5 → 5.9 |
| /tr/rise-to-power/san-juan-hill | 2026-11-03 | Added 2 internal links from Links to add; Title uses 'Battle of San Juan Hill' | 14.8 → 13.7 | 1.4% → 1.1% | 3.7 → 3.6 |
| /tr/presidency/conservation/bird-reserves | 2026-11-03 | Added 2 internal links from Links to add | 0.8 → 0.7 | 1.5% → 1.0% | 5.4 → 4.5 |
| /podcast/good-citizen/douglas-brinkley | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.1 | 0.1% → 0.2% | 11.9 → 13.6 |
| /tr/people/corinne | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.3 | 0.2% → 0.5% | 4.3 → 3.0 |
| /podcast/good-citizen/eric-liu | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.3 | 0.3% → 1.5% | 7.8 → 6.3 |
| /tr/quotes/strenuous-life | 2026-11-03 | Added 1 internal link from Links to add | 1.8 → 2.5 | 1.3% → 1.3% | 6.3 → 6.4 |
| /tr/quotes/citizenship | 2026-11-03 | Added 2 internal links from Links to add | 1.9 → 2.1 | 1.7% → 1.6% | 5.8 → 5.9 |
| /tr/elkhorn-timeline | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.0 | 1.3% → 0.0% | 8.1 → 6.9 |
| /tr/people/edith-roosevelt | 2026-11-03 | Added 2 internal links from Links to add | 0.4 → 0.1 | 0.7% → 0.2% | 11.3 → 11.9 |
| /visit/roosevelt-in-medora | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.8% → 0.0% | 7.4 → 11.3 |
| /podcast/good-citizen/meg-whitman | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.3 | 0.1% → 0.2% | 11.4 → 11.2 |
| /tr/speeches/strenuous-life | 2026-11-03 | Added 1 internal link from Links to add | 2.7 → 2.3 | 1.9% → 2.3% | 5.7 → 5.3 |
| /tr/people/quentin | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.5 | 0.4% → 0.9% | 8.5 → 8.5 |
| /tr/post-presidency/world-war-i | 2026-11-03 | Added 2 internal links from Links to add | 0.2 → 1.1 | 0.5% → 1.1% | 5.4 → 5.5 |
| /tr/rise-to-power/sagamore-hill | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.3 | 0.9% → 0.1% | 6.9 → 8.6 |
| /tr/new-york-politics/convention-1884 | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.6 | 0.9% → 1.5% | 6.7 → 7.3 |
| /about/press/press-releases/sarah-and-ross-perot-jr-foundation-gifts-5-million-theodore-roosevelt | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.1 | 0.9% → 2.9% | 6.4 → 8.1 |
| /about/press/press-releases/theodore-roosevelt-presidential-library-welcomes-doris-kearns-goodwin | 2026-11-03 | Added 2 internal links from Links to add | 0.0 → 0.0 | 0.7% → 0.0% | 5.3 → 9.7 |
| /about/foundation | 2026-11-03 | Added 1 internal link from Links to add | 2.5 → 2.1 | 3.7% → 3.9% | 5.5 → 5.8 |
| /visit/eat | 2026-11-03 | Added 2 internal links from Links to add | 5.8 → 2.0 | 2.7% → 1.8% | 7.2 → 7.6 |
| /visit/maps | 2026-11-03 | Added 1 internal link from Links to add | 1.7 → 0.4 | 0.5% → 1.3% | 3.9 → 3.6 |
| /tr/post-presidency/assassination-attempt | 2026-11-03 | Added 2 internal links from Links to add | 0.8 → 1.2 | 0.6% → 0.7% | 8.0 → 6.9 |
| /research | 2026-11-03 | Added 2 internal links from Links to add | 1.1 → 0.8 | 3.4% → 3.5% | 5.5 → 5.7 |
| /tr/presidency/white-house-family/white-house-gang | 2026-11-03 | Added 2 internal links from Links to add | 0.0 → 0.2 | 1.9% → 2.3% | 6.0 → 4.9 |
| /tr/presidency/conservation/governors-conference | 2026-11-03 | Added 2 internal links from Links to add | 0.3 → 0.5 | 3.4% → 6.0% | 4.8 → 4.1 |
| /tr/rise-to-power/jacob-riis | 2026-11-03 | Added 1 internal link from Links to add | 1.7 → 3.5 | 0.6% → 1.0% | 4.9 → 4.7 |
| /tr/strenuous-life/explorer | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.1 | 1.1% → 0.3% | 5.0 → 5.2 |
| /tr/presidency/race | 2026-11-03 | Added 2 internal links from Links to add | 3.8 → 4.4 | 1.2% → 1.5% | 4.4 → 3.7 |
| /visit/itineraries | 2026-11-03 | Added 1 internal link from Links to add; Link to the I-94 guide | 2.7 → 1.7 | 1.6% → 1.1% | 6.5 → 7.1 |
| /tr/presidency/executive-power | 2026-11-03 | Added 2 internal links from Links to add | 2.9 → 10.8 | 1.5% → 1.7% | 4.1 → 4.1 |
| /tr/presidency/conservation/national-forests | 2026-11-03 | Added 2 internal links from Links to add | 0.5 → 0.5 | 0.8% → 0.4% | 6.0 → 5.8 |
| /visit/itineraries/black-hills-loop | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.3 | 1.0% → 1.0% | 8.3 → 8.0 |
| /visit/itineraries/7-day-billings-bismarck | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.1 | 0.5% → 0.2% | 8.6 → 8.4 |
| /tr/10-myths-teddy-bear | 2026-11-03 | Added 1 internal link from Links to add | 5.2 → 4.9 | 0.8% → 0.8% | 5.5 → 6.7 |
| /tr/post-presidency/bull-moose/platform | 2026-11-03 | Added 1 internal link from Links to add | 8.6 → 9.2 | 0.7% → 0.5% | 5.0 → 4.2 |
| /tr/for-educators/elementary | 2026-11-03 | Added 1 internal link from Links to add | 1.2 → 1.0 | 2.5% → 2.3% | 6.2 → 6.0 |
| /tr/people/alice-longworth | 2026-11-03 | Added 1 internal link from Links to add; Title 'Alice Roosevelt Longworth: Theodore Roosev | 3.7 → 5.1 | 0.4% → 0.5% | 8.0 → 6.6 |
| /tr/tr-save-the-bison | 2026-11-03 | Added 1 internal link from Links to add | 2.1 → 2.6 | 1.5% → 1.7% | 5.1 → 5.2 |
| /tr/presidency/trust-busting | 2026-11-03 | Added 1 internal link from Links to add; Title 'What Was Trust-Busting? Roosevelt Takes On | 36.2 → 44.4 | 1.3% → 1.6% | 3.4 → 3.2 |
| /tr/complex-legacy | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.4 | 1.7% → 1.0% | 6.0 → 5.0 |
| /podcast/good-citizen/susan-berfield | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.1 | 0.5% → 0.3% | 5.6 → 5.7 |
| /tr/badlands/bad-lands-cow-boy | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.1 | 0.3% → 0.3% | 8.6 → 6.8 |
| /tr/presidency/great-white-fleet | 2026-11-03 | Added 1 internal link from Links to add; Title 'The Great White Fleet: Roosevelt's Global  | 6.6 → 10.9 | 0.7% → 1.1% | 4.1 → 3.2 |
| /tr/badlands/ten-facts | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.8 | 1.1% → 1.4% | 5.1 → 5.0 |
| /podcast/good-citizen/susannah-cahalan | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.5 | 0.2% → 0.3% | 9.2 → 10.0 |
| /tr/presidency/bully-pulpit | 2026-11-03 | Added 1 internal link from Links to add; Title 'The Bully Pulpit: Meaning, Origin, and Exa | 5.7 → 13.2 | 0.6% → 0.6% | 4.6 → 3.4 |
| /tr/speeches/man-in-the-arena | 2026-11-03 | Added 1 internal link from Links to add; Title 'Man in the Arena Speech: Citizenship in a  | 25.7 → 63.6 | 2.3% → 3.1% | 5.2 → 5.4 |
| /tr/complex-legacy/eugenics | 2026-11-03 | Added 1 internal link from Links to add | 3.5 → 4.2 | 2.9% → 3.2% | 4.2 → 4.0 |
| /tr/people/jacob-riis | 2026-11-03 | Added 1 internal link from Links to add; Title and description aimed at 'who was Jacob Rii | 16.4 → 22.9 | 0.5% → 0.9% | 6.6 → 5.8 |
| /tr/badlands/maltese-cross | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.0 | 3.1% → 0.0% | 6.5 → 6.6 |
| /tr/people/elliott | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.2 | 0.0% → 0.9% | 9.4 → 9.9 |
| /tr/rise-to-power/vice-presidency | 2026-11-03 | Added 1 internal link from Links to add | 1.9 → 2.5 | 0.7% → 0.8% | 5.4 → 4.8 |
| /tr/family/elliott-roosevelt | 2026-11-03 | Added 1 internal link from Links to add | 1.1 → 1.8 | 0.5% → 0.8% | 7.5 → 7.3 |
| /tr/badlands | 2026-11-03 | Added 1 internal link from Links to add; Link to where-to-see | 0.1 → 0.1 | 1.1% → 1.1% | 5.3 → 7.6 |
| /podcast/good-citizen/carly-fiorina | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.4% → 0.0% | 8.7 → 10.4 |
| /tr/badlands/medora | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.1 | 0.4% → 0.4% | 7.8 → 8.5 |
| /virtual | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 5.1% → 0.0% | 6.3 → 9.4 |
| /tr/books-and-writings/reader | 2026-11-03 | Added 1 internal link from Links to add | 1.2 → 1.1 | 1.9% → 1.9% | 5.2 → 4.9 |
| /tr/complex-legacy/race | 2026-11-03 | Added 1 internal link from Links to add | 0.9 → 2.4 | 0.9% → 0.9% | 4.9 → 4.4 |
| /tr/people/john-muir | 2026-11-03 | Added 1 internal link from Links to add | 1.0 → 1.1 | 0.5% → 0.6% | 7.2 → 6.6 |
| /tr/complex-legacy/equestrian-statue | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.4 | 1.5% → 0.6% | 5.5 → 5.6 |
| /tr/people/ethel | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.5 | 0.3% → 0.5% | 7.8 → 7.0 |
| /tr/rise-to-power/becoming-president | 2026-11-03 | Added 1 internal link from Links to add | 1.4 → 2.6 | 0.3% → 0.5% | 5.3 → 4.8 |
| /tr/people/ted-jr | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.8 | 0.1% → 0.1% | 10.2 → 9.9 |
| /tr/people/mittie | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.4 | 0.6% → 0.5% | 7.5 → 6.7 |
| /podcast/good-citizen/katherine-gehl | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.4 | 1.1% → 2.2% | 8.2 → 8.6 |
| /visit/itineraries/7-day-bismarck-rapid-city | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.4 | 0.4% → 0.5% | 8.1 → 8.3 |
| /tr/early-life/childhood-illness | 2026-11-03 | Added 1 internal link from Links to add | 2.3 → 4.1 | 1.8% → 2.2% | 4.0 → 3.5 |
| /tr/presidency/square-deal | 2026-11-03 | Added 1 internal link from Links to add; Truncated description fixed; Three Cs heading; Sp | 20.7 → 61.7 | 0.6% → 1.4% | 4.4 → 3.0 |
| /tr/presidency/conservation/john-muir | 2026-11-03 | Added 1 internal link from Links to add | 3.2 → 4.3 | 1.1% → 1.4% | 4.5 → 4.1 |
| /tr/myths | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.4 | 0.5% → 4.1% | 8.0 → 7.6 |
| /tr/early-life/young-naturalist | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.4 | 0.9% → 1.7% | 4.9 → 5.3 |
| /tr/presidency/cabinet | 2026-11-03 | Added 1 internal link from Links to add | 1.0 → 2.1 | 1.1% → 1.6% | 5.0 → 5.2 |
| /tr/people/booker-t-washington | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 2.1 | 0.2% → 0.3% | 9.4 → 7.9 |
| /project/design | 2026-11-03 | Added 1 internal link from Links to add | 5.5 → 3.1 | 3.7% → 2.5% | 4.5 → 5.1 |
| /tr/early-life/family-travels | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.3 | 1.4% → 1.1% | 5.2 → 5.6 |
| /podcast/good-citizen/adam-met-climate-action-musical-stardom-and-art-building-movement | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 11.5 → 11.5 |
| /tr/conservation | 2026-11-03 | Added 1 internal link from Links to add | 1.1 → 1.1 | 1.0% → 1.1% | 7.2 → 7.4 |
| /tr/speeches/confession-of-faith | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 1.7 | 1.1% → 2.2% | 7.0 → 8.3 |
| /podcast/good-citizen/senator-mitt-romney-formative-moments-presidential-leadership-and-question | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.1 | 0.1% → 0.2% | 7.7 → 8.2 |
| /tr/homes-and-places | 2026-11-03 | Added 1 internal link from Links to add | 1.2 → 1.5 | 1.1% → 1.5% | 5.9 → 5.4 |
| /tr/early-life/civil-war | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.5 | 0.6% → 1.0% | 5.1 → 4.2 |
| /tr/early-life/day-in-the-life | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.1 | 0.6% → 0.5% | 6.9 → 8.6 |
| /visit/national-park | 2026-11-03 | Added 1 internal link from Links to add; Visit length, restaurant name; link to where-to-s | 4.4 → 2.6 | 0.6% → 0.4% | 8.1 → 8.8 |
| /tr/people/gifford-pinchot | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.5 | 0.9% → 0.6% | 6.3 → 5.8 |
| /tr/post-presidency/bull-moose | 2026-11-03 | Added 1 internal link from Links to add | 5.6 → 7.2 | 0.6% → 0.6% | 4.6 → 4.6 |
| /visit/hiking | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.1 | 0.7% → 0.2% | 7.1 → 7.5 |
| /beam-signing-ceremony | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.1 | 0.0% → 1.7% | 7.9 → 5.6 |
| /project/native-plant-project | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.6 | 0.9% → 3.6% | 4.6 → 6.8 |
| /tr/homes-and-places/tr-national-park | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 1.1 | 0.7% → 1.1% | 7.1 → 8.3 |
| /visit/hunting-fishing | 2026-11-03 | Added 1 internal link from Links to add | 0.8 → 1.2 | 1.1% → 1.7% | 7.3 → 6.8 |
| /about/mission | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.1 | 2.3% → 0.7% | 4.7 → 2.7 |
| /tr/rise-to-power/civil-service | 2026-11-03 | Added 1 internal link from Links to add | 2.1 → 1.6 | 0.6% → 0.3% | 5.3 → 5.4 |
| /tr/badlands/elkhorn-ranch | 2026-11-03 | Added 1 internal link from Links to add | 0.6 → 0.8 | 0.8% → 0.9% | 7.6 → 7.0 |
| /visit/stargazing | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.3 | 1.3% → 1.3% | 6.2 → 6.4 |
| /podcast/good-citizen/dr-vivek-murthy-loneliness-staying-human-and-what-true-success-looks | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.2 | 1.0% → 1.7% | 10.4 → 20.3 |
| /podcast/good-citizen/secretary-deb-haaland | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 1.8 | 0.9% → 1.2% | 7.5 → 7.1 |
| /visit/itineraries/river-road | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.2 | 0.7% → 1.4% | 7.3 → 7.0 |
| /tr/presidency/white-house-workers | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.6 | 1.4% → 0.9% | 6.5 → 7.3 |
| /podcast/good-citizen/matthew-barzun | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.9% → 0.0% | 8.5 → 8.4 |
| /tr/early-life/father | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.5 | 0.5% → 0.4% | 6.7 → 7.6 |
| /visit/camping | 2026-11-03 | Added 1 internal link from Links to add | 0.8 → 0.5 | 1.4% → 0.8% | 7.5 → 7.3 |
| /tr/presidency/conservation/antiquities-act | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 1.2 | 0.9% → 0.6% | 6.1 → 5.9 |
| /visit/trolley | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.1 | 1.6% → 0.7% | 6.9 → 7.7 |
| /tr/badlands/landscape | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.6 | 0.6% → 1.1% | 5.9 → 6.1 |
| /visit/little-missouri-river | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.5 | 1.1% → 1.2% | 7.8 → 6.4 |
| /podcast/good-citizen/ben-jealous | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 10.2 → 11.3 |
| /podcast/good-citizen/dan-harris | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 8.8 → 8.2 |
| /visit/outdoors | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.4 | 1.4% → 3.0% | 6.6 → 5.8 |
| /visit/biking | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.2 | 2.1% → 1.2% | 7.3 → 9.0 |
| /visit/wildlife | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.3 | 0.6% → 0.9% | 7.8 → 7.7 |
| /project | 2026-11-03 | Added 1 internal link from Links to add; Title 'Building the Library: Design, Values and S | 5.0 → 1.6 | 0.5% → 0.2% | 2.4 → 2.5 |
| /tr/people/leonard-wood | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.9 | 0.2% → 0.5% | 8.8 → 6.5 |
| /podcast/good-citizen/katharine-hayhoe | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.1 | 0.0% → 1.2% | 8.5 → 7.3 |
| /visit/itineraries/weekend-drives/fargo | 2026-11-03 | Added 1 internal link from Links to add | 0.6 → 0.4 | 1.1% → 1.0% | 5.0 → 5.6 |
| /about/press/press-releases/trplf-elects-spencer-zwick-board | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 1.6% → 0.0% | 4.3 → 4.0 |
| /visit/itineraries/weekend-drives/bismarck | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.7 | 1.0% → 2.1% | 5.1 → 4.3 |
| /tr/presidency/second-term | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.5 | 1.8% → 1.8% | 6.0 → 4.5 |
| /tr/books-and-writings | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.4 | 0.8% → 1.6% | 8.7 → 9.0 |
| /tr/badlands/frontier-life | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.2 | 0.8% → 0.6% | 6.5 → 6.1 |
| /about/trustees/beth-laski | 2026-11-03 | Added 1 internal link from Links to add | 0.8 → 0.2 | 8.2% → 3.6% | 9.8 → 8.4 |
| /about/press/press-releases/theodore-roosevelt-presidential-library-launches-good-citizen-podcast | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 5.9 → 6.0 |
| /about/presidential-library-system | 2026-11-03 | Added 1 internal link from Links to add | 0.6 → 0.4 | 2.3% → 1.2% | 6.2 → 6.7 |
| /about/press/press-releases/trplf-announces-100-million-commitments-unlocks-50-million-state | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 2.8% → 0.0% | 4.9 → 3.5 |
| /tr/new-york-politics | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.1 | 0.9% → 0.5% | 7.0 → 6.9 |
| /tr/tr-importance | 2026-11-03 | Title 'What Was Theodore Roosevelt Known For?'; typo fix | 12.9 → 16.5 | 1.0% → 1.0% | 4.9 → 4.8 |
| /visit | 2026-10-27 | Title: Plan Your Visit: Tickets, Hours and Directions; Visit length: about three and a hal | 57.3 → 27.9 | 2.5% → 1.9% | 2.7 → 2.9 |
| /tr/presidency/panama-canal | 2026-10-27 | Title and description: Theodore Roosevelt and the Panama Canal, 1903–1914 | 8.2 → 18.1 | 0.4% → 0.7% | 5.2 → 4.7 |
| /tr/presidency/railroad-regulation | 2026-10-27 | Title names the Hepburn Act and Elkins Act | 3.9 → 5.4 | 0.4% → 0.7% | 4.0 → 3.6 |
| /tr/presidency/coal-strike | 2026-10-27 | Title uses 'Anthracite Coal Strike of 1902' | 7.9 → 9.4 | 0.9% → 1.1% | 4.2 → 3.0 |
| /visit/groups | 2026-10-27 | Visit length changed from about three hours to about three and a half hours | 0.1 → 0.0 | 0.6% → 1.1% | 6.5 → 7.0 |
| /visit/faq/tickets | 2026-10-27 | 'Buy tickets' link fixed (was /visit/tickets, a 404); 301 /visit/tickets -> /tickets | 2.0 → 0.9 | 4.3% → 2.8% | 6.3 → 4.7 |
| /visit/faq | 2026-10-27 | Tickets link fixed (was /visit/tickets, a 404) | 2.1 → 0.4 | 0.8% → 1.5% | 4.7 → 7.3 |

## Drafted recommendations (Gemini (gemini-3.8-flash), 2026-11-23T13:09:24+00:00)
**AI visibility:** The Library reliably wins direct searches and driving routes on ChatGPT, but drops off the map for rainy-day visits, museum lists, and most Gemini travel prompts.
- Add an indoor guide covering shelter from bad weather, gallery routes, and quiet spaces for a full 3 1/2 hour stay. (medium effort; trlibrary.com/visit): Neither engine mentions the Library when travelers ask for indoor or bad-weather plans in Medora.
- Coordinate with regional partners to update attraction listings and travel roundups. (low effort; medora.com and ndtourism.com listings): Gemini relies heavily on medora.com, medorand.org, and ndtourism.com, but frequently misses the Library on general Medora inquiries.
- Publish a trail-to-exhibit page connecting the grounds to Maltese Cross Cabin and Elkhorn Ranch. (medium effort; trlibrary.com/visit): Prompts about historic Roosevelt landmarks bypass the Library entirely in favor of National Park Service cabins.

**/tr/presidency/brownsville**: With over 110,000 search impressions and almost no clicks for 'brownsville affair', the page needs an urgent metadata rewrite and a concise 'at a glance' summary answering what happened, why Roosevelt acted, and how the soldiers were exonerated.
- Title: Brownsville Affair: Roosevelt and the 25th Infantry
- Meta: Explore the 1906 Brownsville Affair, when Roosevelt discharged 167 Black soldiers without trial, and see how the injustice was overturned 66 years later.
- Verify: Verify that the term 'Brownsville raid' and 'Brownsville affray' are acceptable naming variants aligned with Library interpretive guidelines.; Confirm the exact dates (August 13–14, 1906), soldier count (167), and the 1972/1973 exoneration and compensation details before publishing newly formatted summaries.

**/tr/presidency/roosevelt-corollary**: This page earns over 22,000 impressions a month for 'roosevelt corollary' and related definition queries, but suffers a very low click-through rate because it buries a plain, direct definition beneath background history.
- Title: Roosevelt Corollary: Definition, Summary & History
- Meta: What was the Roosevelt Corollary? Get a clear definition, see how it altered the Monroe Doctrine, and learn why it sparked decades of debate.
- Verify: Verify whether the drafted summary accurately reflects the Library's educational guidelines on describing the 1904 Annual Message and the Monroe Doctrine.

**/visit/hours**: Fix broken heading hierarchy across seasonal schedules and make indoor/bad-weather operating details clearer so AI search engines can easily parse daily opening times and seasonal closures.
- Title: Hours and Seasonal Schedule in Medora
- Meta: Find seasonal museum, restaurant, and shop hours in Medora, North Dakota. Plan about 3 1/2 hours for your visit, with last entry 90 minutes before close.
- Verify: Verify whether Earth Day free admission applies every year or was intended specifically for a single anniversary event.; Verify whether the outdoor boardwalk has posted sunrise-to-sunset hours or remains accessible 24 hours daily.

**/programs**: Expand the thin, under-150-word body copy with specific descriptions of available media and educational offerings, and introduce clear heading hierarchy so search engines and AI assistants recognize the Library's active public programming.
- Title: Programs, Podcasts & Events
- Meta: Listen to the Good Citizen Podcast, explore classroom lessons, and find live events in Medora and online at the Theodore Roosevelt Presidential Library.
- Verify: Confirm whether live talks and indoor community presentations in Medora require tickets or advance registration.; Verify whether classroom materials and quizzes are available for free download by families and teachers.

**/tr/rise-to-power/rough-riders**: Add a crisp, direct definition of the Rough Riders at the top of the page to capture high-volume informational queries like 'who were the rough riders' and feed AI summary answer boxes.
- Title: Rough Riders: Theodore Roosevelt's 1st Volunteer Cavalry
- Meta: Meet the Rough Riders: over 1,000 cowboys, athletes, and scouts led by Theodore Roosevelt in Cuba. Explore the battles that made the regiment legendary.
- Verify: Verify that the draft summary accurately states the regiment numbered more than 1,000 men and was commanded by Leonard Wood and Theodore Roosevelt.; Verify that the draft claims regarding Las Guasimas, Kettle Hill, Santiago, and Roosevelt's rise to the New York governorship match the Library's preferred historical framing.

**/tr/presidency/conservation**: The page ranks on page one for queries asking what Roosevelt did that had never been done before in conservation, but it buries his unprecedented firsts across separate cards instead of answering the question directly.
- Title: Theodore Roosevelt Conservation: Parks, Forests & Wildlife
- Meta: Discover how Theodore Roosevelt protected 230 million acres of public land, doubled the national parks, and created the first federal bird reserves.
- Verify: That Pelican Island was the nation's first federal bird reserve.; That Devils Tower was the first national monument.; That the 1908 Governors' Conference was the first time all governors were gathered at the White House for natural resources.; That roughly 230 million acres is the total public land protected under Roosevelt.

**/tr/strenuous-life/athletics**: This page already ranks well for Roosevelt's fitness and boxing queries, but it can capture significantly more search traffic by organizing his specific workout habits and athletic feats into clear, scannable sections that directly answer search queries.
- Title: Theodore Roosevelt: Boxing, Fitness, and Sports
- Meta: Explore Theodore Roosevelt’s daily workout habits, White House boxing bouts, and jiu-jitsu training. See how he built his iron constitution.
- Verify: Verify whether any specific calisthenics or weightlifting exercises are documented beyond the general 'gym work, running, boxing, lifting' mentioned in the current text before publishing expanded workout details.

**/tr/presidency/booker-t-washington**: Shorten the oversized title to align with high-volume search queries around the White House dinner, and add a concise summary answering why the dinner was significant to capture high-impression student and research queries.
- Title: Booker T. Washington's White House Dinner with Roosevelt
- Meta: In 1901, Theodore Roosevelt invited Booker T. Washington to dinner. Learn how one White House meal sparked public fury and tested executive power.
- Verify: Confirm that the draft wording regarding the dinner date (October 16, 1901) and Booker T. Washington being the first African American invited to dine at the White House matches the Library's historical interpretation standards.; Verify that William Crum and Minnie Cox references in the body text are sufficiently contextualized if expanded into standalone callouts.

## Visitor experience (/visit pages)
Findability 47/100, mobile speed 52/100, accessibility 97/100, average reading grade 8.3, 0 facts that disagree between pages.

### Can a first-time visitor find what they need?
| Page | Score | Missing or buried | Biggest fix |
|---|---|---|---|
| /visit | 79 | directions, accessibility, food | Add clear parking instructions alongside the driving directions so arriving visitors know where to leave their vehicles. |
| /visit/accessibility | 29 | hours, price, buy, visit_length | Note the recommended 3 1/2 hour visit length so guests with mobility or sensory needs can plan their stamina and schedule accordingly. |
| /visit/directions | 61 | visit_length, accessibility, food | State early in the driving directions that a visit takes about 3 1/2 hours so road-trippers can budget enough time. |
| /visit/eat | 20 | hours, price, directions, accessibility | Add quick-jump filter links (such as breakfast, quick bites, family meals, and sweets) above the long list of town restaurants so phone users do not have to scroll endlessly. |
| /visit/faq | 75 |  | Add direct answers to the top three visitor questions—hours, admission, and recommended visit length—right on this page so readers do not have to click through multiple subpages. |
| /visit/faq/tickets | 29 | hours, directions, visit_length, accessibility | Add a question stating ticket prices and categories so visitors know admission costs without having to begin the checkout process. |
| /visit/groups | 29 | hours, price, directions, accessibility, food | Add baseline ticket prices and motorcoach parking details so group leaders can budget and plan their arrival before submitting a reservation form. |
| /visit/hours | 71 | visit_length, accessibility | Move the three-and-a-half-hour recommended visit length and the 90-minute last entry rule to the top of the page so guests can plan when to arrive before closing. |
| /visit/lodging | 58 | directions, food | Add a quick-reference distance or transit note beside each lodging option showing exactly how to reach the Library from that property. |
| /visit/maps | 50 | visit_length, accessibility, food | Add clear orientation copy noting that a typical visit takes about 3 1/2 hours, along with explicit details on wheelchair accessibility and parking locations. |
| /visit/tickets/plan-ahead | 14 | hours, price, directions, visit_length, accessibility, food | Add essential planning details alongside the booking calendar, including ticket prices, daily operating hours, and the recommended 3 1/2 hour visit time. |

### Slowest pages on mobile
| Page | Speed /100 | Load (s) |
|---|---|---|
| /visit/itineraries/roosevelt-triangle | 17 | 16.3 |
| /visit/itineraries/10-day-denver-salt-lake-city | 24 | 39.2 |
| /visit/roosevelt-in-medora | 27 | 14 |
| /visit/lodging | 28 | 6.1 |
| /visit/stargazing | 30 | 13 |
| /visit/itineraries/enchanted-highway | 31 | 7 |
| /visit/itineraries/trs-badlands | 31 | 5.8 |
| /visit/itineraries/weekend-drives | 31 | 17.1 |

### Accessibility problems found
- ARIA `tooltip` elements do not have accessible names.
- Background and foreground colors do not have a sufficient contrast ratio.
- Elements use prohibited ARIA attributes
- Elements with an ARIA `[role]` that require children to contain a specific `[role]` are missing some or all of those required children.
- Heading elements are not in a sequentially-descending order
- Links do not have a discernible name
- List items (`<li>`) are not contained within `<ul>`, `<ol>` or `<menu>` parent elements.
- Touch targets do not have sufficient size or spacing.
- `<frame>` or `<iframe>` elements do not have a title
- `[role]`s are not contained by their required parent element

## Internal links and broken links
8 broken internal addresses (42 links), 682 links worth adding, 42 pages with no links in, 20 topics with two pages, 38 broken outside links (LinkChecker scan 2026-11-16 04:28 UTC).

### Broken links on trlibrary.com: 301 redirects to add
Add a 301 redirect in Drupal (Configuration > Search and metadata > URL redirects) from each broken address to redirect_to; bulk import: https://seo.labs.trlibrary.com/data/redirects.csv. High confidence = safe; check medium/low first. Ticket-store paths should also be corrected on the page to the full access.trlibrary.com address.

| Broken | Status | Redirect to | Confidence | Links | Why |
|---|---|---|---|---|---|
| /orders/613/tickets | 403 | https://access.trlibrary.com/orders/613/tickets | high | 19 | access denied: probably an unpublished page that is still linked. Publish it, or redirect: ticket-store link missing its domain (access.trlibrary.com); better still, fix the link itself |
| /orders/613/calendar | 403 | https://access.trlibrary.com/orders/613/calendar | high | 15 | access denied: probably an unpublished page that is still linked. Publish it, or redirect: ticket-store link missing its domain (access.trlibrary.com); better still, fix the link itself |
| /events/613/detail/6a04cbc9b396e88c8b5609dd | 403 | https://access.trlibrary.com/events/613/detail/6a04cbc9b396e88c8b5609dd | high | 2 | access denied: probably an unpublished page that is still linked. Publish it, or redirect: ticket-store link missing its domain (access.trlibrary.com); better still, fix the link itself |
| /about/trustees/edward-okeefe | 404 | /podcast/good-citizen/edward-okeefe | high | 2 | live page with the same name |
| /auth/613/members | 403 | https://access.trlibrary.com/auth/613/members | high | 1 | access denied: probably an unpublished page that is still linked. Publish it, or redirect: ticket-store link missing its domain (access.trlibrary.com); better still, fix the link itself |
| /events/613/detail/6a4a8cb76c7bf23066004d67 | 403 | https://access.trlibrary.com/events/613/detail/6a4a8cb76c7bf23066004d67 | high | 1 | access denied: probably an unpublished page that is still linked. Publish it, or redirect: ticket-store link missing its domain (access.trlibrary.com); better still, fix the link itself |
| /place/land/badlands | 403 | /quiz/badlands | medium | 1 | access denied: probably an unpublished page that is still linked. Publish it, or redirect: live page with the same name (also: /tr/badlands) |
| /membership/613/join | 403 | /membership | low | 1 | access denied: probably an unpublished page that is still linked. Publish it, or redirect: no matching page; nearest section (or remove the link / create the page) |

### Links to add (highest value first; the [[bracketed]] words become the link)
| On page | Context | Link to |
|---|---|---|
| /tr/legacy/rankings | Roosevelt’s enduring popularity is carved in granite at [[Mount Rushmore]], beside Washington, Jefferson, and Lincoln. (National Park Service) | /tr/tr-mount-rushmore |
| /tr/tr-mount-rushmore | Learn more about Theodore Roosevelt and his concept of [[executive power]] with this Inquiry Design Model (IDM) lesson plan. | /tr/presidency/executive-power |
| /tr/timeline | …velt had declared he would not run again, promoting the presidency of his cabinet member, [[William Howard Taft]] during the 1908 election. When Roosevelt returned home from his African safari in 1910, h… | /tr/people/william-howard-taft |
| /tr/timeline | …r, a Brazilian military officer suggested descending an unknown river: Rio da Dúvida, the [[River of Doubt]]. Together Roosevelt, his Brazilian counterpart expedition leader, Cândido Mariano da Silv… | /tr/post-presidency/river-of-doubt |
| /tr/timeline | …tille Day—July 14, 1918—near Chamery, France. For several days after Quentin’s death, the [[Roosevelt family]] only knew that he had been reported missing. After learning of his death, 59-year-old The… | /tr/family |
| /tr/presidency-timeline | …ssia and Japan, the Russo-Japanese War ended in September 1905. Roosevelt was awarded the [[Nobel Peace Prize]] for his successful negotiations. He was not able to accept the prize in person. Instead, … | /tr/presidency/nobel-peace-prize |
| /tr/timeline | … 1905. Just over a year later, 48-year-old Roosevelt became the first American to win the [[Nobel Peace Prize]], announced on December 10, 1906. Roosevelt was not able to collect the prize himself and … | /tr/presidency/nobel-peace-prize |
| /tr/timeline | Theodore and [[Edith Roosevelt]]’s first child, Theodore Jr. “Ted,” was born at the family home at Sagamore Hill in Oyster… | /tr/rise-to-power/edith-roosevelt |
| /tr/presidency/foreign-policy | …ility to intervene in world affairs became mainstream American thinking. The assertion of [[executive power]] in foreign policy—the president's ability to act boldly without waiting for Congressional… | /tr/presidency/executive-power |
| /tr/teddy-nickname | How much do you know about [[Theodore Roosevelt's early life]]? | /tr/early-life |
| /tr/fake-quotes | Learn more about Theodore Roosevelt and his concept of [[executive power]] with this Inquiry Design Model (IDM) lesson plan. | /tr/presidency/executive-power |
| /tr/people/henry-cabot-lodge | …osevelt, deserved party loyalty. Lodge also believed that some of Roosevelt's ideas about [[executive power]] and Progressive reform were too radical for his tastes. Yet Lodge also remained personall… | /tr/presidency/executive-power |
| /tr/presidency | [[Booker T. Washington]], October 1901 | /tr/people/booker-t-washington |
| /tr/timeline | … Service under the Department of Agriculture. Theodore Roosevelt, then 46 years old, made [[Gifford Pinchot]] the first US Chief Forester. Throughout his presidency, Roosevelt was dedicated to the he… | /tr/presidency/conservation/gifford-pinchot |
| /tr/complex-legacy/race | [[Booker T. Washington]], the era’s most prominent African American leader, whom Roosevelt invited to dine at the … | /tr/people/booker-t-washington |
| /tr/rise-to-power/vice-presidency | The MacNaughton Cottage at Tahawus, where the [[Roosevelt family]] vacationed in the Adirondacks in the summer of 1901. (Harvard College Library) | /tr/family |
| /visit/exhibits/main | … from them. On race, Roosevelt was, in his own era and ours, a divided figure. He invited [[Booker T. Washington]] to dine at the White House and stood by Minnie Cox, the first Black postmaster in Mississ… | /tr/people/booker-t-washington |
| /visit/exhibits/main | …eded reviving: he went looking for the wildest thing he could find. What he found was the [[River of Doubt]] — an uncharted Amazon tributary so unknown that no map could tell him where it went or wh… | /tr/post-presidency/river-of-doubt |
| /tr/homes-and-places/white-house | Decorations for [[Alice Roosevelt]]'s White House wedding, February 1906. (Frances Benjamin Johnston / Library of Congress) | /tr/people/alice-longworth |
| /visit/exhibits/main | Look up. In the windows above, the house comes alive: silhouettes of the [[Roosevelt family]], and the very adventures Theodore is reading play out across the glass — the stories fill… | /tr/family |
| /tr/timeline | …ore and Edith Roosevelt’s first child, Theodore Jr. “Ted,” was born at the family home at [[Sagamore Hill]] in Oyster Bay, New York. As Roosevelt referred to him in a letter to his sister Corinne a… | /tr/rise-to-power/sagamore-hill |
| /tr/presidency/conservation/national-forests | …appropriations bill on March 4. The episode demonstrated Roosevelt's sophistication about [[executive power]]: when Congress threatened to strip his authority, he moved decisively to lock in his cons… | /tr/presidency/executive-power |
| /teach-tr | Learn about the [[Panama Canal]] and Theodore Roosevelt’s connection to the canal with this resource packet containing 13 … | /tr/presidency/panama-canal |
| /tr/timeline | …sidency, Roosevelt was dedicated to the health and wellbeing of forests, establishing 150 [[national forests]]. | /tr/presidency/conservation/national-forests |
| /tr/timeline | … of four children, Theodore Roosevelt was born at 28 East 20th Street in New York City to [[Theodore Sr]]. “Thee” and Martha “Mittie” Bulloch Roosevelt. Born into a wealthy family, Roosevelt grew… | /tr/people/theodore-sr |
| /visit/exhibits/main | …er. He helped end a war between Russia and Japan and became the first American to win the [[Nobel Peace Prize]] . At home, he laid groundwork for the federal safeguards that would become the FDA, champ… | /tr/presidency/nobel-peace-prize |
| /visit/exhibits/main | …12 — a work so rigorous the Navy would later place a copy on every ship. He fell hard for [[Alice Hathaway Lee]], courting her with headlong devotion until she agreed to marry him on his twenty-second b… | /tr/new-york-politics/alice-lee |
| /tr/family/family-tree | …osevelt and Edith with five of their children (Kermit, Ted, Ethel, Archie and Quentin) at [[Sagamore Hill]], 1907. Alice, already married, is not in the picture. (Library of Congress) | /tr/rise-to-power/sagamore-hill |
| /tr/teddy-nickname | …repressible small boy to his face as Mr. Roosevelt emerged from the Yosemite [hiking with [[John Muir]]]. This hail is said to have met with a prompt Presidential veto.” | /tr/people/john-muir |
| /visit/exhibits/main | At the center of it is [[Edith Roosevelt]] , whose steady hand shaped both the house and the role. She led a major renovation that g… | /tr/rise-to-power/edith-roosevelt |
| /tr/homes-and-places/sagamore-hill | … Roosevelt family at Sagamore Hill in 1903: Theodore and Edith with their children Alice, [[Ted Jr]]., Kermit, Ethel, Archie and Quentin. (Harvard College Library) | /tr/people/ted-jr |
| /visit/exhibits/main | The Republican establishment had shipped him off to the [[vice presidency]] to sideline him. When McKinley was killed, the man they couldn't control suddenly held th… | /tr/rise-to-power/vice-presidency |
| /tr/presidency/ten-facts | Roosevelt protected some 230 million acres of public land; here he stands with naturalist [[John Muir]] at Glacier Point in Yosemite, 1903. (Library of Congress) | /tr/people/john-muir |
| /tr/people/gifford-pinchot | …legal channels and Congressional consultation. This fundamental difference in approach to [[executive power]] became the axis of conflict, and it placed Pinchot in an impossible position. | /tr/presidency/executive-power |
| /tr/speeches/confession-of-faith | …cans by taking a more cautious approach to conservation, to antitrust enforcement, and to [[executive power]] generally. Progressives believed that Taft had betrayed Roosevelt's legacy. They demanded… | /tr/presidency/executive-power |
| /tr/timeline | …edition on the continent of Africa on March 23, 1909, with a party that included his son, [[Kermit Roosevelt]]. The elder Roosevelt was 50 years old. The expedition spent almost a full year in British… | /tr/people/kermit |
| /tr/rise-to-power/assistant-navy-secretary | …sevelt's tenure. It illustrated a principle that would guide Roosevelt's understanding of [[executive power]] throughout his life: a subordinate with clear convictions and the opportunity to act coul… | /tr/presidency/executive-power |
| /tr/rise-to-power/rough-riders | The regiment was based in San Antonio, Texas, at Camp Wood, where Roosevelt and Colonel [[Leonard Wood]] set about the work of transforming diverse individuals into a functioning military unit. … | /tr/people/leonard-wood |
| /tr/family/fdr-connection | Franklin Roosevelt as [[Assistant Secretary of the Navy]] in 1913, holding the same post Theodore had occupied sixteen years earlier (Library of Co… | /tr/rise-to-power/assistant-navy-secretary |
| /podcast/good-citizen/live-trpl-4-first-lady-modern-presidency-panel-hosted-kjersti-armstrong | … example, she was the first First Lady to travel abroad with her husband. That was to the [[Panama Canal]]. I mean, she did come into the White House and helped and ushered in a modern era. She wa… | /tr/presidency/panama-canal |

### Pages nothing links to
| Page | Title | Impr. |
|---|---|---|
| /tr/pre-presidency-political-accomplishments | WHAT WERE THEODORE ROOSEVELT’S FIVE SIGNIFICANT ACCOMPLISHMENTS PRIOR TO BECOMING PRESIDENT? | 47482 |
| /tr/10-myths-teddy-bear | TOP 10 MYTHS ABOUT THEODORE ROOSEVELT + THE INVENTION OF THE TEDDY BEAR | 16311 |
| /tr/fake-quotes | DID TR REALLY SAY THAT? | 14704 |
| /programs | Programs | 9562 |
| /join-us | Join Us | 6774 |
| /research/books-by-roosevelt | TR's Published Books | 6213 |
| /tr/5-big-adventures | TR’S FIVE BIG POST-PRESIDENTIAL ADVENTURES | 5391 |
| /tr/tr-save-the-bison | DID THEODORE ROOSEVELT SAVE THE BISON? | 3893 |
| /visit/medora/history | History of Medora | 1858 |
| /research/archives | Archives | 1810 |
| /visit/teddy-trail | The Teddy Trail | 845 |
| /visit/exhibits/artificial-intelligence | Artificial Intelligence and Responsible Stewardship | 650 |
| /events/teddycon | Theodore Roosevelt Convention (#TeddyCon) | 550 |
| /vote | Step Into the Arena | 406 |
| /visit/weather | Weather | 397 |
| /research/family-tree | Theodore Roosevelt Family Tree / Theodore Roosevelt Presidential Library | 361 |
| /digital-guide | Free Digital Guide | 294 |
| /tr/badlands/timeline | The Badlands Years: 1883–1887 Timeline | 227 |
| /alexander-hamilton-speaks | Alexander Hamilton Speaks | 142 |
| /visit/groups | Group Reservations | 125 |
| /support/heritage-society | The TRPL HERITAGE SOCIETY | 102 |
| /beam-signing-ceremony | Beam Signing Ceremony | 93 |
| /impact |  | 65 |
| /visit/groups/field-trips | Field Trips | 65 |
| /gwti-250 | From Precedent to Power: Teaching Executive Authority Through George Washington and Theodore Roosevelt | 61 |

### Same topic, two pages
| Topic | Pages |
|---|---|
| mount rushmore | /tr/tr-mount-rushmore, /tr/legacy/mount-rushmore |
| rough riders | /tr/rise-to-power/san-juan-hill, /tr/rise-to-power/rough-riders |
| alice roosevelt longworth | /tr/people/alice-longworth, /tr/people/alice-longworth/complex-legacy |
| booker t washington | /tr/people/booker-t-washington, /tr/presidency/booker-t-washington |
| alice hathaway lee roosevelt | /tr/new-york-politics/alice-lee, /tr/people/alice-lee |
| alice lee | /tr/new-york-politics/alice-lee, /tr/people/alice-lee |
| edith roosevelt | /tr/rise-to-power/edith-roosevelt, /tr/people/edith-roosevelt |
| common misquotes | /tr/quotes/misquotes, /tr/myths/misquotes |
| gifford pinchot | /tr/presidency/conservation/gifford-pinchot, /tr/people/gifford-pinchot |
| sagamore hill | /tr/rise-to-power/sagamore-hill, /tr/homes-and-places/sagamore-hill |
| ten facts | /tr/rise-to-power/ten-facts, /tr/badlands/ten-facts, /tr/early-life/ten-facts |
| elliott roosevelt | /tr/family/elliott-roosevelt, /tr/people/elliott |
| martha "mittie" bulloch roosevelt | /tr/early-life/mother, /tr/people/mittie |
| teaching theodore roosevelt | /tr/for-educators/high-school, /tr/for-educators/elementary, /tr/for-educators/middle-school |
| 7-day trip | /visit/itineraries/7-day-bismarck-rapid-city, /visit/itineraries/7-day-billings-bismarck |

### Broken links to other websites (fix on the page; /video/ ones come from YouTube descriptions)
| Link | Status | On pages | Video page |
|---|---|---|---|
| https://www.theodorerooseveltcenter.org/subject/conservation | 404 | /tr/conservation/by-the-numbers, /tr/conservation/by-the-numbers.html, /tr/conservation/quotes, /tr/conservation/quotes.html | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/foreign-policy | 404 | /tr/complex-legacy/imperialism, /tr/presidency/panama-canal | False |
| https://abcnews.go.com/US/wireStory/reconstructed-road-opens-grand-views-theodore-roosevelt-national-127851476 | 404 | /press/clips | False |
| https://abcnews.go.com/US/wireStory/theodore-roosevelt-library-opening-visitors-pack-bag-north-126510433 | 404 | /press/clips | False |
| https://nam12.safelinks.protection.outlook.com/?url=https%3A%2F%2Ftedxfargo.us7.list-manage.com%2Ftrack%2Fclick%3Fu%3D42126281e0ac794ca800574d6%26id%3Df7ebdfb4ff%26e%3D1462c24ed9&data=05%7C02%7C%7C35bcbf6698764ab622a208dcb6cfbeee%7Cc3f9fd833dac4d1ea4c3573c4fcf9600%7C0%7C0%7C638586250598216425%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=nXcwCuy9%2FDCyUR0Q0K6LYfUovy2c365RPeUeFVqxr8c%3D&reserved=0 | 404 | /node/30 | False |
| https://nationaltoday.com/us/nd/medora-nd/news/2026/04/01/theodore-roosevelt-presidential-library-nears-completion/ | 404 | /press/clips | False |
| https://softpower.ug/roosevelt-africa-trail-moves-from-shared-history-to-us-uganda-economic-action/ | 500 | /press/clips | False |
| https://www.am1100theflag.com/show-episodes/74671-the-steve-hallstrom-show-episode-174-trump-is-selling-bibles-but-should-he-be | 404 | /press/clips | False |
| https://www.argusleader.com/story/news/2025/07/09/theodore-roosevelt-presidential-library-expected-to-open-in-july-2026/84505352007/ | 402 | /press/clips | False |
| https://www.detroitnews.com/story/opinion/2024/01/17/zito-t-r-s-presidential-library-comes-to-life-in-north-dakota/72251603007/ | 402 | /press/clips | False |
| https://www.fargomoorhead.org/teddy-roosevelt-trail/ | 404 | /visit/teddy-trail | False |
| https://www.kvrr.com/2024/08/14/gov-burgum-marks-a-significant-milestone-for-theodore-roosevelt-presidential-library/ | 404 | /press/clips | False |
| https://www.nationalparkstraveler.org/2026/06/trump-and-burgum-visit-north-dakota-open-theodore-roosevelt-presidential-library | 503 | /press/clips | False |
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
| https://www.theodorerooseveltcenter.org/encyclopedia/native-americans | 404 | /tr/complex-legacy/native-americans | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/people/harvey-wiley | 404 | /tr/presidency/food-and-drug | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/politics-and-government/citizenship-in-a-republic | 404 | /tr/post-presidency/man-in-the-arena | False |
| https://www.theodorerooseveltcenter.org/media/Images/Blog/2019/Roosevelt_submarine-1024x854-2.jpg | 404 | /tr/presidency-timeline | False |
| https://www.theodorerooseveltcenter.org/subject/progressive-party | 404 | /tr/people/william-howard-taft | False |
| https://www.usatoday.com/story/news/politics/2026/07/01/roosevelt-library-set-to-open-to-public-on-independence-day/90714775007/ | 402 | /press/clips | False |
| https://www.usatoday.com/story/news/politics/2026/07/01/trump-dedicates-new-theodore-roosevelt-library/90760301007/ | 402 | /press/clips | False |
| https://www.usatoday.com/videos/news/local/2026/07/20/griffins-26-m-gift-renames-roosevelt-wing/90984868007/ | 402 | /press/clips | False |

## Structured data (schema.org) for search engines and AI tools
352 of 900 content pages carry their own markup (39%); 9 sitewide issues (1 high). llms.txt on trlibrary.com: yes (draft: https://seo.labs.trlibrary.com/data/site-llms.txt).

Most fixes are one change to a Drupal template per content type (ask FiveJars); the JSON-LD examples are built from a real page. Values starting 'TODO:' must be filled from the page's own fields, never guessed.

### Sitewide issues
| Severity | Issue | Fix |
|---|---|---|
| high | Sitewide markup doesn't link to the Library's Wikipedia entry | Add these to sameAs in the sitewide schema. |
| medium | Restaurant and store hours are listed as the museum's hours | Keep only museum hours on the Library entity. Give the restaurant and the store their own entities (Restaurant, Store) with their hours, linked with containsPlace. |
| medium | No admission information in the markup | Add admission offers (and isAccessibleForFree: false) to the Library entity. |
| medium | 35 unaliased /node/ URLs are in the sitemap | Ask FiveJars to leave unaliased /node/ URLs out of the XML sitemap. |
| medium | The Theodore Roosevelt entity has 2 values to fix | Edit the meta tags of the “Who was TR” hub page (Schema.org Person). The values are set once there and FiveJars' code prints them on every /tr page. Check names and dates against the Historical Accuracy Standard before saving. |
| low | 273 pages have dates without a colon in the time zone | In the Drupal schema templates, format dateModified, datePublished, endDate, startDate with the PHP date format “c” (e.g. 2020-10-27T06:00:00-06:00). |
| low | The live llms.txt has drifted from the site: 19 pages to add | Edit the sections at /admin/content/llms-txt/sections: add the new pages under their heading and remove or repoint the links that left the sitemap. The draft has the wording for each new line. |
| low | 251 articles use the site logo as their Article image | Map the Article image to the page's share image (og:image), falling back to the logo only when a page has none. |
| low | 91 articles are labelled og:type “website” | Set og:type to “article” on /tr, press release and podcast templates (Drupal Metatag). |

### By content type (biggest gaps first)
| Content type | Should carry | Pages | Has it | Incomplete | Fix |
|---|---|---|---|---|---|
| Video pages | VideoObject | 414 | 0 | 0 | Add VideoObject JSON-LD to the video view template from the stored YouTube data (title, description, thumbnail, publish date, duration). |
| Good Citizen episodes | PodcastEpisode | 72 | 0 | 0 | Add PodcastEpisode JSON-LD to the podcast episode template (title, summary, release date, Simplecast player). |
| Trip itineraries | TouristTrip | 20 | 0 | 0 | Add TouristTrip JSON-LD to the itinerary template, listing each stop. Check the drafted stop list: it's taken from the page headings. |
| Video playlists | ItemList / VideoObject | 40 | 0 | 0 | Add ItemList of VideoObject JSON-LD to the playlist template. Drupal already stores each video's YouTube data, including its publish date (uploadDate). |
| Press releases | Article / NewsArticle | 19 | 19 | 19 | Add NewsArticle JSON-LD to the press release template, using the release date field. |
| Trustee profiles | Person / ProfilePage | 12 | 12 | 12 | Add ProfilePage + Person JSON-LD (role: Trustee) to the trustee template. |
| Pages with Q&A | FAQPage | 21 | 20 | 0 | Add FAQPage JSON-LD to the accordion paragraph type: when every item's title is a question, output each as Question/Answer. One template change covers every FAQ page. |
| Good Citizen podcast page | PodcastSeries | 1 | 0 | 0 | Add PodcastSeries JSON-LD to the podcast landing page. |
| TR history section pages | Article / CollectionPage | 55 | 54 | 0 | Add CollectionPage JSON-LD to the /tr section landing template. |
| Calendar events | Event | 28 | 28 | 1 | Add Event JSON-LD to the Event content type template, filled from the event's date, time, price and ticket fields. One template change covers every event. |
| Staff profiles | Person / ProfilePage | 42 | 42 | 0 | Add ProfilePage + Person JSON-LD to the staff member template (name, job title, photo). |
| TR history articles | Article | 164 | 164 | 0 | Add Article JSON-LD to the /tr article template with about = Theodore Roosevelt (the sitewide #theodore-roosevelt entity) and dateModified from the node's changed date. |
| TR history: people | Article | 27 | 27 | 0 | Add Article JSON-LD to the /tr people template, with an 'about' Person; a field for the person's Wikidata link makes it precise. |
| TR history: speeches | Article | 6 | 6 | 0 | Add Article JSON-LD with an 'about' CreativeWork (the speech, author: Theodore Roosevelt). |

## Ticket checkout (GA4, rates only)
Checkout completion – (prior –); store visitors who buy 18% (prior 41%); ticket page to store 43%. Steps the store doesn't report: view_item, add_to_cart, begin_checkout, add_payment_info.

Store frustration signals (last 3 days, Clarity): dead clicks 6.5% of sessions, rage clicks 0.3%, quick backs 7.1%, scroll depth 46.3%.

| Store page | Dead % | Rage % | Quick back % | Scroll % |
|---|---|---|---|---|
| calendar/special-event/america-beautiful-film-screening | 0 | 0 | 0 | 12 |
| checkout/process | 0 | 0 | 0 | 83 |
| holiday-2026 | 0 | 0 | 0 | 12 |
| orders/tickets | 0 | 0 | 0 | 98.8 |
| holidaytrees | 0 | 0 | 0 | 91 |
| checkout/confirm | 0 | 0 | 22.2 | 97.4 |
| tickets | 0 | 0 | 0 | 6 |
| search | 0 | 0 | 0 | 60 |
| tr/family/family-tree | 0 | 0 | 0 | 57.5 |
| midwinter-table | 0 | 0 | 0 | 23 |
| calendar/special-event/elkhorn-evenings | 0 | 0 | 0 | 63 |
| orders/forms | 0 | 0 | 0 | 100 |
| video/view/L08bDsNwOOE | 0 | 0 | 0 | 73 |
| contact | 0 | 0 | 0 | 55.1 |
| private-events | 0 | 0 | 0 | 18 |
| support | 0 | 0 | 0 | 15 |
| bullet-speech | 0 | 0 | 0 | 18 |
| tr/presidency/race | 0 | 0 | 0 | 64.3 |
| tr/quotes | 0 | 0 | 100 | 87.5 |
| visit/exhibits/kennerly | 0 | 0 | 0 | 100 |
| calendar | 0 | 0 | 0 | 26 |
| about/press/press-releases/theodore-roosevelts-groundbreaking-firsts-and-feats-celebration | 0 | 0 | 0 | 85 |
| calendar/special-event/butchery-workshop | 0 | 0 | 0 | 77 |
| / | 3 | 0 | 11.9 | 27.9 |
| video/view/1nogFWdneOw | 0 | 0 | 0 | 71.2 |
| tr/rise-to-power/spanish-american-war | 50 | 0 | 0 | 30 |
| visit/medora | 0 | 0 | 0 | 67 |
| video/view/FH2iglgaMZE | 0 | 0 | 0 | 88 |
| membership/join | 0 | 0 | 0 | 65 |
| tr/people | 0 | 0 | 0 | 12 |
| calendar/specialty-tour | 0 | 0 | 0 | 82 |
| quiz/pets | 0 | 0 | 0 | 100 |
| visit/itineraries/black-hills-loop | 0 | 0 | 0 | 58.5 |
| video/view/gPqE13bB8YI | 0 | 0 | 0 | 32 |
| visit/national-park | 0 | 0 | 100 | 97 |
| tr/pre-presidency-political-accomplishments | 50 | 0 | 0 | 19.3 |
| tr/people/william-howard-taft | 20 | 0 | 0 | 50.6 |
| visit/gateway-trails | 0 | 0 | 0 | 6 |
| auth/members | 20 | 0 | 0 | 99.4 |
| tr | 0 | 0 | 0 | 89 |
| tr/rise-to-power/boone-and-crockett | 0 | 0 | 0 | 35 |
| tr/presidency/square-deal | 7.7 | 7.7 | 0 | 18.7 |
| visit/stargazing/northern-lights | 0 | 0 | 0 | 19 |
| tr/presidency/trust-busting | 0 | 0 | 0 | 4 |
| tr/fake-quotes | 0 | 0 | 0 | 29.6 |
| podcast/good-citizen/karl-rove-historic-redemption-hard-work-politics-and-essential-nature | 0 | 0 | 0 | 87 |
| project | 33.3 | 0 | 16.7 | 57.5 |
| volunteer | 0 | 0 | 0 | 97 |
| visit/hours | 0 | 0 | 0 | 73.6 |
| visit/wildlife | 0 | 0 | 0 | 7 |
| visit/camping | 0 | 0 | 0 | 9 |
| tr/post-presidency/new-nationalism | 0 | 0 | 0 | 100 |
| visit/hunting-fishing | 0 | 0 | 0 | 4 |
| visit/one-medora | 0 | 0 | 0 | 19 |
| tr/tr-mount-rushmore | 20 | 0 | 0 | 45.3 |
| tr/badlands-timeline | 0 | 0 | 0 | 16 |
| video/playlist/PL-sck-PjBiFfu9EhF15jUS48bssBq1RQK | 0 | 0 | 0 | 88 |
| staff-members/jeremy-beam | 0 | 0 | 0 | 92 |
| visit/planner | 0 | 0 | 0 | 9 |
| tr/speeches/man-in-the-arena | 27.8 | 0 | 0 | 41.3 |
| calendar/daily-activity/family-crafting-time | 0 | 0 | 0 | 34 |
| video/view/Vp3hmGIYdzk | 0 | 0 | 100 | 54 |
| about/press/press-releases/harold-hamm-donates-50-million-trpl | 0 | 0 | 0 | 98 |
| visit/accessibility | 0 | 0 | 0 | 42 |
| tr/rise-to-power/jacob-riis | 0 | 0 | 0 | 43 |
| visit/faq | 0 | 0 | 0 | 44 |
| tr/presidency/great-white-fleet | 50 | 0 | 0 | 57.3 |
| tr/presidency/foreign-policy | 0 | 0 | 0 | 92 |
| about/press/press-releases/theodore-roosevelt-presidential-library-opening-celebrations-july-4-2026 | 0 | 0 | 0 | 66 |
| visit/groups/field-trips | 0 | 0 | 100 | 68 |
| video/playlist/PLSaoXk08gMqQ | 0 | 0 | 0 | 86 |
| tr/early-life | 0 | 0 | 0 | 41.4 |
| tr/presidency/booker-t-washington | 0 | 0 | 0 | 11 |
| tr/family/children | 20 | 0 | 0 | 61.2 |
| tr/complex-legacy/imperialism | 0 | 0 | 0 | 58.8 |
| video/view/GpKHsBZXubE | 0 | 0 | 14.3 | 59.1 |
| video/view/-mcN1M3ZEps | 0 | 0 | 0 | 39 |
| quiz/presidency | 0 | 0 | 0 | 100 |
| visit/biking | 100 | 0 | 0 | 63 |
| teach-tr | 0 | 0 | 100 | 10 |
| tr/presidency/railroad-regulation | 0 | 0 | 0 | 53.5 |
| video/view/lPnE-bKve_U | 0 | 0 | 100 | 23 |
| tr/presidency | 0 | 0 | 0 | 51.5 |
| membership/detail | 0 | 0 | 0 | 100 |
| tr/homes-and-places/tr-national-park | 0 | 0 | 0 | 10 |
| staff-members/cj-von-buchwald-wright | 0 | 0 | 0 | 65 |
| about/foundation | 0 | 0 | 33.3 | 63.7 |
| tr/presidency/executive-actions | 0 | 0 | 0 | 26.5 |
| visit | 3.5 | 0 | 17.2 | 38.5 |
| tr/complex-legacy/equestrian-statue | 100 | 0 | 0 | 54.5 |
| calendar/special-event/visit-santa-claus | 0 | 0 | 0 | 32 |
| membership | 0 | 0 | 20 | 69.5 |
| tr/post-presidency/death | 0 | 0 | 0 | 84.3 |
| orders/calendar | 20 | 0 | 70 | 93 |
| tr/presidency/conservation | 0 | 0 | 0 | 46.5 |
| tr/birthday-timeline | 0 | 0 | 0 | 31 |
| tr/rise-to-power/edith-roosevelt | 50 | 0 | 0 | 91 |
| tr/post-presidency | 0 | 0 | 0 | 56 |
| visit/directions | 0 | 0 | 0 | 15.4 |
| tr/presidency-timeline | 0 | 0 | 0 | 13 |
| tr/badlands | 0 | 0 | 0 | 24 |
| tr/presidency/elections | 0 | 0 | 0 | 15 |
| tr/post-presidency/bull-moose | 33.3 | 0 | 0 | 46.7 |
| visit/faq/tickets | 0 | 0 | 0 | 100 |
| tr/quotes/citizenship | 0 | 0 | 0 | 14.1 |
| staff-members/addison-olson | 0 | 0 | 0 | 74 |
| tr/early-life/family-travels | 0 | 0 | 0 | 5 |
| tr/family/fdr-connection | 0 | 0 | 0 | 44 |
| membership/renew/detail | 0 | 0 | 0 | 64 |
| staff-members/sarah-mellor | 0 | 0 | 0 | 76 |
| podcast/good-citizen | 0 | 0 | 0 | 14 |
| tr/speeches/first-annual-message | 0 | 0 | 0 | 98 |
| podcast/good-citizen/anna-jane-joyner | 0 | 0 | 0 | 12 |
| visit/tours | 0 | 0 | 0 | 65.6 |
| about/press | 0 | 0 | 0 | 29 |
| tr/speeches | 25 | 0 | 0 | 86.9 |
| tr/quotes/strenuous-life | 0 | 0 | 0 | 23 |
| rsvp/holidayopenhouse | 0 | 0 | 0 | 100 |
| visit/faq/during-your-visit | 0 | 0 | 16.7 | 69.1 |
| visit/national-park/trip-planner | 0 | 0 | 0 | 96.5 |
| calendar/specialty-tour/architecture-and-sustainability-tour | 0 | 0 | 0 | 86 |
| video/view/W9sq8PuGQVo | 0 | 0 | 0 | 27 |
| tr/badlands/boat-thieves | 100 | 0 | 0 | 67 |
| about/trustees | 0 | 0 | 0 | 95 |
| tr/rise-to-power/buffalo-soldiers | 20 | 0 | 20 | 62.7 |
| about/mission | 0 | 0 | 0 | 64 |
| staff-members/susan-sarna | 0 | 0 | 0 | 32 |
| visit/medora-traditions | 0 | 0 | 0 | 100 |
| tr/presidency/panama-canal | 25 | 0 | 0 | 19.2 |
| podcast/good-citizen/leah-hunt-hendrix | 0 | 0 | 0 | 8 |
| membership/renew | 0 | 0 | 25 | 95.6 |
| tr/presidency/roosevelt-corollary | 0 | 0 | 0 | 60 |
| newsletter | 0 | 0 | 0 | 91 |
| visit/eat | 14.3 | 0 | 0 | 35.6 |
| tr/people/bamie | 0 | 0 | 0 | 49 |
| tr/new-york-politics/alice-lee | 50 | 0 | 0 | 51.3 |
| tr/presidency/ten-facts | 0 | 0 | 0 | 41.9 |
| tr/conservation | 0 | 0 | 0 | 49 |
| tr/strenuous-life | 0 | 0 | 0 | 48 |
| tr/people/quentin | 100 | 0 | 0 | 23 |
| about/trustees/david-saggau | 0 | 0 | 0 | 100 |
| staff-members/danielle-sahlin | 0 | 0 | 0 | 77 |
| research | 0 | 0 | 0 | 84.3 |
| about/trustees/john-palfrey | 33.3 | 0 | 0 | 91 |
| visit/maps/print | 0 | 0 | 0 | 26 |
| calendar/specialty-tour/theodore-roosevelt-and-american-empire-tour | 0 | 0 | 0 | 38 |
| tr/presidency/brownsville | 0 | 0 | 0 | 38.3 |
| tr/early-life/family-roots | 0 | 0 | 0 | 98 |
| staff-members/matt-briney | 0 | 0 | 0 | 67 |
| staff-members | 0 | 0 | 11.1 | 57 |
| programs | 0 | 0 | 50 | 76.3 |
| calendar/medora | 0 | 0 | 0 | 95 |
| about/trustees/victoria-chambers | 0 | 0 | 0 | 89 |
| calendar/daily-activity/free-final-hour | 0 | 0 | 0 | 37 |
| about | 0 | 0 | 0 | 42 |
| tr/people/edith-roosevelt | 0 | 0 | 0 | 67 |
| tr/presidency/executive-power | 0 | 0 | 0 | 18.2 |
| visit/tickets/plan-ahead | 25 | 0 | 50 | 31.8 |
| podcast/good-citizen/george-packer-patriotism-democratic-values-and-turning-fiction | 0 | 0 | 0 | 55 |
| membership/profile | 0 | 0 | 0 | 100 |
| video/view/fPZD2xLBXZs | 0 | 0 | 0 | 49 |
| tr/rise-to-power/san-juan-hill | 0 | 0 | 0 | 41.2 |
| tr/10-myths-teddy-bear | 0 | 0 | 0 | 61 |
| about/careers | 0 | 0 | 0 | 59.8 |
| tr/timeline | 66.7 | 33.3 | 0 | 98.6 |
| digital-guide | 0 | 0 | 0 | 14 |
| tr/legacy/teddy-bear | 0 | 0 | 0 | 25 |
| podcast/good-citizen/ted-leonsis | 0 | 0 | 0 | 9 |
| quiz | 0 | 0 | 0 | 25 |
| tr/presidency/executive-actions/action | 100 | 0 | 0 | 95 |
| tr/legacy | 0 | 0 | 0 | 22 |
| tr/post-presidency/quentin | 100 | 0 | 0 | 100 |
| about/presidential-library-system | 0 | 0 | 0 | 40.5 |
| visit/exhibits | 0 | 0 | 0 | 65.8 |
| tr/rise-to-power/becoming-president | 0 | 0 | 0 | 53.5 |
| tr/tr-shot | 0 | 0 | 0 | 12.8 |
| tr/post-presidency/bull-moose/platform | 20 | 0 | 0 | 46.6 |
| beam-signing-ceremony | 0 | 0 | 0 | 7 |
| visit/outdoors | 0 | 0 | 0 | 56 |
| support/matching-gifts | 0 | 0 | 0 | 46 |
| tr/for-educators/elementary | 0 | 0 | 0 | 41 |
| tr/presidency/bully-pulpit | 0 | 0 | 25 | 47.8 |
| calendar/specialty-tour/badlands-landscape-tour | 0 | 0 | 0 | 71 |

## Tracking changes made automatically
Rules and caps: config/tracking.yml. Keep an item permanently by copying it into config/keywords.yml or config/ai_prompts.yml; block it via tracking.yml exclude.

| Date | Change | Type | Item | Why |
|---|---|---|---|---|
| 2026-11-23 | added | keyword | edith roosevelt | position 9.1, 4761 impressions/28d; Essential to Roosevelt family history and her tenure as First Lady. |
| 2026-11-23 | added | keyword | rough riders | position 9.5, 3493 impressions/28d; Core topic in Roosevelt's military service and national rise to fame. |
| 2026-11-23 | added | keyword | henry cabot lodge | position 7.5, 5934 impressions/28d; Key political ally, lifelong friend, and confidant central to Roosevelt's career and correspondence. |
| 2026-11-23 | added | keyword | roosevelt river | position 9.0, 4526 impressions/28d; Captures interest in Roosevelt's scientific and exploratory expedition through the Amazon basin. |
| 2026-11-23 | added | keyword | mt rushmore presidents | position 4.2, 4069 impressions/28d; Connects Roosevelt to fellow presidents carved on Mount Rushmore, directly relevant to regional visitors and historical context. |
| 2026-11-16 | added | question | What was the Roosevelt Corollary to the Monroe Doctrine and why does it matter? | from the Google search "what is the roosevelt corollary"; Key presidential foreign policy doctrine essential for student and teacher research. |
| 2026-11-16 | added | question | What is the meaning and origin of the term bully pulpit in American politics? | from the Google search "what is the bully pulpit"; Core civic education concept coined by Roosevelt regarding presidential communication. |
| 2026-11-16 | added | keyword | bully pulpit meaning | position 4.4, 1506 impressions/28d; Famous concept coined by Theodore Roosevelt; valuable for civic education and presidential history. |
| 2026-11-16 | added | keyword | booker t washington | position 12.6, 2226 impressions/28d; Key historical figure tied directly to TR's presidency and landmark 1901 White House dinner. |
| 2026-11-16 | added | keyword | archibald roosevelt | position 7.8, 3188 impressions/28d; Direct member of TR's immediate family; supports the Library's role as the authority on the Roosevelt family. |
| 2026-11-16 | added | keyword | american imperialism | position 7.0, 3552 impressions/28d; Major curriculum topic tied directly to Theodore Roosevelt's presidency and foreign policy. |
| 2026-11-16 | added | keyword | alice hathaway lee roosevelt | position 5.9, 6064 impressions/28d; Core topic for TR's early life, family history, and his formative move to the Dakota Badlands. |
| 2026-11-09 | added | question | Which four presidents are on Mount Rushmore, and why was Theodore Roosevelt included among them? | from the Google search "what presidents are on mount rushmore"; Connects Roosevelt to a major regional monument and invites context on his national significance. |
| 2026-11-09 | added | question | What years was Theodore Roosevelt president, and what were the dates of his administration? | from the Google search "when was teddy roosevelt president"; Foundational timeline query for TR's presidency. |
| 2026-11-09 | added | keyword | quentin roosevelt | position 11.2, 4775 impressions/28d; Theodore Roosevelt's youngest son, killed in action during World War I. |

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
