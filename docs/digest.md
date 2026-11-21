# trlibrary.com search & AI visibility digest
Generated 2026-11-21T13:23:11+00:00 from https://seo.labs.trlibrary.com. Full data: see 'Raw data' at the end.

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
48 tasks (2 search, 23 audit, 6 internal links, 15 structured data, 2 AI visibility); 12 with FiveJars or blocked. Ranked by severity x the Google audience of the pages involved. Full lists, every page, and step-by-step Drupal recipes: https://seo.labs.trlibrary.com/data/work_queue.json

### This week's moves
1. **Broken internal addresses: add 301 redirects** (`links:broken`): high priority; pages involved get 4,102 Google impressions (28 days). Start with: /about/trustees/edward-okeefe.
2. **Pages ranking well that people skip: rewrite title and description** (`search:low_ctr`): medium priority; pages involved get 312,837 Google impressions (28 days). Start with: /tr/presidency/roosevelt-corollary; /tr/presidency/brownsville; /visit/hours.
3. **Searches AI assistants run where trlibrary.com isn't on page one** (`ai:searches_we_miss`): medium priority; affects the whole site. Start with: "Badlands Dinosaur Museum Dickinson official site" (run by ChatGPT); "Bismarck Mandan attractions Fort Abraham Lincoln State Park North Dakota I-94" (run by ChatGPT); "Bonanzaville West Fargo museum official site" (run by ChatGPT).

### What else we checked (and why it can wait)
- Restaurant and store hours are listed as the museum's hours (`schema:sitewide:mixed_hours`): FiveJars work; send as a ticket
- TR history section pages: add CollectionPage markup (template, all pages at once) (`schema:tr_hubs`): FiveJars work; send as a ticket
- Same topic on two pages (merge or differentiate) (`links:duplicate_topics`): needs a decision first (merge or archive)
- Strengthen pages ranking just off the top for searches people make (`search:striking_distance`): same area as a move this week (search); next in line
- Add internal links where pages already mention each other (`links:add`): same area as a move this week (internal links); next in line
- Pages nothing links to (`links:orphans`): same area as a move this week (internal links); next in line
- Get onto pages AI cites that leave the Library out (`ai:ask_to_be_added`): same area as a move this week (ai visibility); next in line
- No H1 heading (`audit:h1_missing`): smaller reach (20,557 Google impressions vs 4,102 for this week's moves)

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
| 1 | Restaurant and store hours are listed as the museum's hours | structured data | FiveJars | 1 | to do | schema:sitewide:mixed_hours |
| 2 | TR history section pages: add CollectionPage markup (template, all pages at once) | structured data | FiveJars | 55 | to do | schema:tr_hubs |
| 3 | Broken internal addresses: add 301 redirects | internal links | TRPL | 1 | to do | links:broken |
| 4 | Same topic on two pages (merge or differentiate) | internal links | TRPL | 20 | needs approval | links:duplicate_topics |
| 5 | Pages ranking well that people skip: rewrite title and description | search | TRPL | 5 | to do | search:low_ctr |
| 6 | Strengthen pages ranking just off the top for searches people make | search | TRPL | 16 | to do | search:striking_distance |
| 7 | Add internal links where pages already mention each other | internal links | TRPL | 576 | to do | links:add |
| 8 | Pages nothing links to | internal links | TRPL | 45 | to do | links:orphans |
| 9 | Searches AI assistants run where trlibrary.com isn't on page one | ai visibility | TRPL | 49 | to do | ai:searches_we_miss |
| 10 | Get onto pages AI cites that leave the Library out | ai visibility | TRPL | 7 | to do | ai:ask_to_be_added |
| 11 | No H1 heading | audit | TRPL | 29 | to do | audit:h1_missing |
| 12 | Same title as another page | audit | TRPL | 32 | to do | audit:title_duplicate |
| 13 | Turn on IndexNow so Bing and Copilot see changes within hours | audit | FiveJars | 1 | to do | setup:indexnow |
| 14 | Missing Open Graph tags | audit | TRPL | 10 | to do | audit:og_missing |
| 15 | Same title as another page (Video pages: fix once in the video template) | audit | FiveJars | 32 | to do | audit:title_duplicate:template |
| 16 | Links that go through a redirect | internal links | TRPL | 72 | to do | links:via_redirect |
| 17 | Related pages that don't link to each other | internal links | TRPL | 27 | to do | links:related |
| 18 | Heading levels skip (e.g. H2 straight to H4) | audit | TRPL | 147 | to do | audit:heading_skip |
| 19 | Sitemap lists a /node/ URL instead of a readable path | audit | TRPL | 35 | to do | audit:unaliased_url |
| 20 | No meta description (Video pages: fix once in the video template) | audit | FiveJars | 17 | to do | audit:meta_missing:template |
| 21 | Missing Open Graph tags (Video pages: fix once in the video template) | audit | FiveJars | 17 | to do | audit:og_missing:template |
| 22 | More than 4 clicks from the homepage | audit | TRPL | 112 | to do | audit:deep_page |
| 23 | Title over 60 characters, not counting the site-name suffix | audit | TRPL | 91 | to do | audit:title_too_long |
| 24 | Same meta description as another page | audit | TRPL | 44 | to do | audit:meta_duplicate |
| 25 | Title under 15 characters, not counting the site-name suffix | audit | TRPL | 140 | to do | audit:title_too_short |
| 26 | No meta description | audit | TRPL | 9 | to do | audit:meta_missing |
| 27 | More than one H1 | audit | TRPL | 10 | to do | audit:h1_multiple |
| 28 | Under 150 words of body text | audit | TRPL | 237 | to do | audit:thin_content |
| 29 | Title over 60 characters, not counting the site-name suffix (Video pages: fix once in the video template) | audit | FiveJars | 173 | to do | audit:title_too_long:template |
| 30 | Sitemap lists a URL that redirects | audit | TRPL | 5 | to do | audit:redirect_in_sitemap |

### Task details (TRPL can do these now)
**3. Broken internal addresses: add 301 redirects** (`links:broken`, 1 items)
- How: Configuration > Search and metadata > URL redirects > Add redirect: From = broken path, To = target, 301. If Drupal warns the path looks valid, submit again. Bulk: import redirects.csv. Also fix the link on the source page when the target is known.
- Done when: The old address returns 301 to the target
  - `/about/trustees/edward-okeefe`, 4,102 impr., -> /podcast/good-citizen/edward-okeefe (high)

**4. Same topic on two pages (merge or differentiate)** (`links:duplicate_topics`, 20 items)
- How: Two pages compete for one subject. Pick the stronger page (clicks, depth), move anything unique onto it, then archive the other and add a 301 from its alias and /node/NID. Get approval first; draft before publishing.
- Done when: One page per topic; the other 301s to it
  - `/tr/tr-mount-rushmore`, 163,511 impr., mount rushmore: /tr/tr-mount-rushmore vs /tr/legacy/mount-rushmore
  - `/tr/rise-to-power/san-juan-hill`, 47,894 impr., rough riders: /tr/rise-to-power/san-juan-hill vs /tr/rise-to-power/rough-riders
  - `/tr/people/alice-longworth`, 26,667 impr., alice roosevelt longworth: /tr/people/alice-longworth vs /tr/people/alice-longworth/complex-legacy
  - `/tr/people/booker-t-washington`, 14,517 impr., booker t washington: /tr/people/booker-t-washington vs /tr/presidency/booker-t-washington
  - `/tr/new-york-politics/alice-lee`, 12,554 impr., alice hathaway lee roosevelt: /tr/new-york-politics/alice-lee vs /tr/people/alice-lee
  - `/tr/new-york-politics/alice-lee`, 12,554 impr., alice lee: /tr/new-york-politics/alice-lee vs /tr/people/alice-lee
  - `/tr/rise-to-power/edith-roosevelt`, 11,429 impr., edith roosevelt: /tr/rise-to-power/edith-roosevelt vs /tr/people/edith-roosevelt
  - `/tr/quotes/misquotes`, 9,311 impr., common misquotes: /tr/quotes/misquotes vs /tr/myths/misquotes
  - ...and 12 more in work_queue.json

**5. Pages ranking well that people skip: rewrite title and description** (`search:low_ctr`, 5 items)
- How: Edit the node (/node/NID/edit) > 'Customize meta tags'. Basic tags: Page title '<title> | [site:name]' (page part 60 characters or fewer) and Description (120-155 characters). Set Open Graph og:title/og:description and Twitter card title/description to match. Save with 'Save' (keeps the moderation state). If the save seems to do nothing, look for a validation error further down the form.
- Done when: Click-through rate rises at the same position (change log before/after)
  - `/tr/presidency/roosevelt-corollary`, 144,460 impr.
  - `/tr/presidency/brownsville`, 113,422 impr.
  - `/visit/hours`, 28,328 impr.
  - `/tr/rise-to-power/rough-riders`, 17,759 impr.
  - `/programs`, 8,868 impr.

**6. Strengthen pages ranking just off the top for searches people make** (`search:striking_distance`, 16 items)
- How: Open the page and make it the best answer to that exact search: use the search's words in the title or a heading, answer it plainly in the first paragraph, add the specifics people want (facts already on the site), and link to it from 2-3 related pages. Don't rewrite a page that already ranks in the top 3 for its main search.
- Done when: Average position for the search improves over the next 4 weeks (change log before/after)
  - `/tr/presidency/brownsville`, 110,285 impr., "brownsville affair" #4.3, move up from #4 to about #3, upside ~12131 clicks/28d
  - `/tr/presidency/roosevelt-corollary`, 2,864 impr., "roosevelt corollary definition" #4.4, move up from #4 to about #3, upside ~313 clicks/28d
  - `/tr/presidency/roosevelt-corollary`, 1,546 impr., "roosevelt corollary definition us history" #5.8, move up from #6 to about #3, upside ~169 clicks/28d
  - `/tr/presidency/roosevelt-corollary`, 1,134 impr., "the roosevelt corollary" #4.0, move up from #4 to about #3, upside ~120 clicks/28d
  - `/project/living-building-challenge`, 1,075 impr., "living building challenge" #6.3, move up from #6 to about #3, upside ~115 clicks/28d
  - `/quiz/muckrakers`, 1,912 impr., "muckrakers" #10.2, move up from #10 to about #5, upside ~111 clicks/28d
  - `/tr/rise-to-power/rough-riders/who-were-they`, 1,884 impr., "rough riders" #10.2, move up from #10 to about #5, upside ~110 clicks/28d
  - `/tr/rise-to-power/rough-riders`, 831 impr., "who were the rough riders" #6.5, move up from #6 to about #3, upside ~87 clicks/28d
  - ...and 8 more in work_queue.json

**7. Add internal links where pages already mention each other** (`links:add`, 576 items)
- How: Open the source page's Layout. Edit the text block that contains the context sentence and turn the [[bracketed]] words into a link to the target path (relative, e.g. /tr/tr-shot). Don't write new sentences just to hold a link. Save the block, then Save layout.
- Done when: The link appears on the source page; the target's links-in count rises next week
  - `/tr/timeline`, 47,114 impr., [[William Howard Taft]] -> /tr/people/william-howard-taft; [[River of Doubt]] -> /tr/post-presidency/river-of-doubt; [[Edith Roosevelt]] -> /tr/rise-to-power/edith-roosevelt
  - `/visit/exhibits/main`, 5,629 impr., [[River of Doubt]] -> /tr/post-presidency/river-of-doubt; [[Alice Hathaway Lee]] -> /tr/new-york-politics/alice-lee; [[Booker T. Washington]] -> /tr/people/booker-t-washington
  - `/podcast/good-citizen/edward-okeefe`, 299 impr., [[executive power]] -> /tr/presidency/executive-power; [[Nobel Peace Prize]] -> /tr/presidency/nobel-peace-prize; [[Eleanor Roosevelt]] -> /tr/people/eleanor
  - `/tr/presidency/white-house-family`, 2,153 impr., [[Edith Roosevelt]] -> /tr/rise-to-power/edith-roosevelt; [[governor of New York]] -> /tr/rise-to-power/governor; [[Kermit Roosevelt]] -> /tr/people/kermit
  - `/tr/thanksgiving`, 224 impr., [[Henry Cabot Lodge]] -> /tr/people/henry-cabot-lodge; [[River of Doubt]] -> /tr/post-presidency/river-of-doubt; [[Alice Hathaway Lee]] -> /tr/new-york-politics/alice-lee
  - `/tr/thanksgiving-timeline`, 354 impr., [[River of Doubt]] -> /tr/post-presidency/river-of-doubt; [[Alice Lee]] -> /tr/new-york-politics/alice-lee; [[Pine Knot]] -> /tr/homes-and-places/pine-knot
  - `/tr`, 12,102 impr., [[Ted Jr]] -> /tr/people/ted-jr; [[Alice Hathaway Lee]] -> /tr/new-york-politics/alice-lee; [[Booker T. Washington]] -> /tr/people/booker-t-washington
  - `/tr/family/family-tree`, 31,579 impr., [[Kermit Roosevelt]] -> /tr/people/kermit; [[Sagamore Hill]] -> /tr/homes-and-places/sagamore-hill; [[Quentin Roosevelt]] -> /tr/people/quentin
  - ...and 258 more in work_queue.json

**8. Pages nothing links to** (`links:orphans`, 45 items)
- How: Add 2-3 links to this page from the pages listed under 'link from' (each has the sentence and words to link).
- Done when: At least two pages link in
  - `/tr/pre-presidency-political-accomplishments`, 52,329 impr.
  - `/tr/10-myths-teddy-bear`, 14,812 impr.
  - `/tr/fake-quotes`, 14,015 impr.
  - `/programs`, 7,532 impr.
  - `/research/books-by-roosevelt`, 6,196 impr.
  - `/tr/5-big-adventures`, 5,700 impr.
  - `/join-us`, 5,282 impr.
  - `/tr/tr-save-the-bison`, 3,713 impr.
  - ...and 37 more in work_queue.json

**9. Searches AI assistants run where trlibrary.com isn't on page one** (`ai:searches_we_miss`, 49 items)
- How: These are the searches the assistants ran before answering a question where they left the Library out. Find the trlibrary.com page that should answer each one (or note that none does). Strengthen that page for the search: say it in the title or a heading and answer it in the first paragraph, with facts already on the site. If no page fits, propose one.
- Done when: trlibrary.com ranks top 10 for the search (Search Console) and the next AI run cites it
  - `Badlands Dinosaur Museum Dickinson official site`, run by ChatGPT; we rank nowhere
  - `Bismarck Mandan attractions Fort Abraham Lincoln State Park North Dakota I-94`, run by ChatGPT; we rank nowhere
  - `Bonanzaville West Fargo museum official site`, run by ChatGPT; we rank nowhere
  - `Dakota Territory Air Museum Minot official site`, run by ChatGPT; we rank nowhere
  - `Dakota Thunder Jamestown buffalo sculpture 'World's largest buffalo' Dakota Thunder Jamestown location I-94 exit`, run by ChatGPT; we rank nowhere
  - `Dwight D. Eisenhower Presidential Library Abilene Kansas official site`, run by ChatGPT; we rank nowhere
  - `Enchanted Highway Regent North Dakota distance from I-94`, run by ChatGPT; we rank nowhere
  - `Fargo Air Museum official site`, run by ChatGPT; we rank nowhere
  - ...and 32 more in work_queue.json

**10. Get onto pages AI cites that leave the Library out** (`ai:ask_to_be_added`, 7 items)
- How: Read the page. If it's a list of things to do or a travel guide that names nearby attractions, find the author or the update/contact link and ask to be added, with a two-sentence blurb (what the Library is, why it's worth the stop, about 3 1/2 hours) and a photo. Draft the note for approval; nothing goes out without it.
- Done when: The page names the Library (next weekly run re-reads it)
  - `https://www.mystateparks.com/parks/nd-fort-abraham-lincoln-state-park`, other, cited in 1 answers; names Painted Canyon, Theodore Roosevelt National Park, Medora Musical
  - `https://www.avivadirectory.com/Regional/North-America/United-States/States/North-Dakota/Cities-Towns/Valley-City`, other, cited in 1 answers; names Painted Canyon, Theodore Roosevelt National Park, Medora Musical
  - `https://visitfargo.com/attractions/museums_history`, other, cited in 1 answers; names Painted Canyon, Theodore Roosevelt National Park, Medora Musical
  - `https://plainsart.org/about`, other, cited in 1 answers; names North Dakota Cowboy Hall of Fame
  - `https://ndmoa.com/plan-your-visit`, other, cited in 1 answers; names North Dakota Cowboy Hall of Fame
  - `https://www.bonanzaville.org`, other, cited in 1 answers; names North Dakota Cowboy Hall of Fame
  - `https://dakotaterritoryairmuseum.com`, other, cited in 1 answers; names North Dakota Cowboy Hall of Fame

**11. No H1 heading** (`audit:h1_missing`, 29 pages)
- How: Open the page's Layout (/node/NID/layout). Make sure the top section shows the page title block (Content fields > Title), which renders as the H1; or change the first heading in the top text block to Heading 1. Save layout.
- Done when: Exactly one H1
  - `/tr/presidency/executive-actions/action`, 12,071 impr., no H1
  - `/tr/presidency/executive-actions/story`, 5,380 impr., no H1
  - `/grand-opening/photos/july4`, 870 impr., no H1
  - `/visit/maps/campus`, 744 impr., no H1
  - `/visit/planner`, 557 impr., no H1
  - `/research/family-tree`, 326 impr., no H1
  - `/grand-opening/photos/july2`, 128 impr., no H1
  - `/membership/neighbor`, 120 impr., no H1
  - ...and 21 more in work_queue.json

**12. Same title as another page** (`audit:title_duplicate`, 32 pages)
- How: Edit the node (/node/NID/edit) > 'Customize meta tags'. Basic tags: Page title '<title> | [site:name]' (page part 60 characters or fewer) and Description (120-155 characters). Set Open Graph og:title/og:description and Twitter card title/description to match. Save with 'Save' (keeps the moderation state). If the save seems to do nothing, look for a validation error further down the form.
- Done when: No other page has the same title
  - `/visit/exhibits/kennerly`, 4,080 impr., HELD (recently changed), title "In the Room: David Hume Kennerly Photo Exhibition" (49 chars), same as /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf
  - `/project/native-plant-project`, 776 impr., HELD (recently changed), title "Native Plant Project" (20 chars), same as /video/view/1SqdaUrbU7U
  - `/events/teddycon`, 558 impr., HELD (recently changed), title "Theodore Roosevelt Convention (#TeddyCon)" (41 chars), same as /event/24
  - `/visit/accessibility`, 207 impr., title "Accessibility" (13 chars), same as /visit/faq/accessibility
  - `/alexander-hamilton-speaks`, 132 impr., title "Alexander Hamilton Speaks" (25 chars), same as /hamilton-speaks-the-study
  - `/press/clips`, 117 impr., title "In the News" (11 chars), same as /video/in-the-news
  - `/gwti-250`, 64 impr., title "From Precedent to Power: Teaching Executive Authority Through George Washington and Theodore Roosevelt" (102 chars), same as /calendar/special-event/precedent-power-teaching-executive-authority-through-george-washington-and
  - `/node/246`, 43 impr., title "Book Talk: Candice Millard's The River of Doubt" (47 chars), same as /video/view/dRIXs_adw7U
  - ...and 24 more in work_queue.json

**14. Missing Open Graph tags** (`audit:og_missing`, 10 pages)
- How: Edit the node (/node/NID/edit) > 'Customize meta tags'. Basic tags: Page title '<title> | [site:name]' (page part 60 characters or fewer) and Description (120-155 characters). Set Open Graph og:title/og:description and Twitter card title/description to match. Save with 'Save' (keeps the moderation state). If the save seems to do nothing, look for a validation error further down the form.
- Done when: og:title and og:description are present
  - `/visit/teddy-trail`, 867 impr., HELD (recently changed)
  - `/birthdaycard`, 35 impr.
  - `/rsvp/midwinter`, 23 impr.
  - `/project/how-the-library-works`, 13 impr.
  - `/quiz/who-was-tr`, 11 impr.
  - `/quiz/the-boardwalk`, 1 impr.
  - `/quiz/badlands-family`, 1 impr.
  - `/quiz/native-plant-project`, 1 impr.
  - ...and 2 more in work_queue.json

**16. Links that go through a redirect** (`links:via_redirect`, 72 items)
- How: Edit the link on each source page so it points straight at the final address.
- Done when: Links point at the final address
  - `/grand-opening/talks`, -> /
  - `/calendar/daily-activity/david-hume-kennerly-exhibition`, -> /calendar/daily-activity/room-sixty-years-front-lines-history
  - `/support-trpl`, -> /support
  - `/press`, -> /about/press
  - `/latest-news`, -> /about/press
  - `/donate`, -> /support
  - `/project/native-plants`, -> /project/native-plant-project
  - `/mission`, -> /about/mission
  - ...and 64 more in work_queue.json

**17. Related pages that don't link to each other** (`links:related`, 27 items)
- How: These two pages cover the same subject without linking to each other. Add one natural link each way, in the paragraph where the shared subject comes up.
- Done when: Each page links to the other
  - `/tr/family/family-tree`, 122,688 impr., <-> /tr/family/fdr-connection
  - `/tr/presidency-timeline`, 99,419 impr., <-> /tr/timeline
  - `/tr/complex-legacy/imperialism`, 76,260 impr., <-> /tr/rise-to-power/spanish-american-war
  - `/tr/complex-legacy/imperialism`, 51,307 impr., <-> /tr/presidency/foreign-policy
  - `/tr/post-presidency/bull-moose/platform`, 46,272 impr., <-> /tr/speeches/confession-of-faith
  - `/tr/post-presidency/bull-moose/platform`, 45,667 impr., <-> /tr/speeches/new-nationalism
  - `/tr/family/children`, 43,057 impr., <-> /tr/family/family-tree
  - `/tr/post-presidency/bull-moose`, 35,921 impr., <-> /tr/speeches/new-nationalism
  - ...and 19 more in work_queue.json

**18. Heading levels skip (e.g. H2 straight to H4)** (`audit:heading_skip`, 147 pages)
- How: Open the Layout. In the text blocks, change the heading levels so they step down one at a time (H2 under the page title, H3 under an H2). Headings used just for size should be styled text instead.
- Done when: Heading levels step down one at a time
  - `/podcast/good-citizen/senator-chris-murphy`, 163,693 impr.
  - `/`, 84,556 impr.
  - `/tr/presidency-timeline`, 52,305 impr.
  - `/tr/timeline`, 47,114 impr.
  - `/podcast/good-citizen/karl-rove-historic-redemption-hard-work-politics-and-essential-nature`, 37,993 impr.
  - `/visit/hours`, 28,328 impr.
  - `/project`, 27,382 impr.
  - `/podcast/good-citizen/bill-kristol`, 26,474 impr.
  - ...and 139 more in work_queue.json

### Page jobs: everything to fix on one page, busiest pages first
| Page | Impr. | Fixes | Links to add | Markup |  |
|---|---|---|---|---|---|
| /tr/tr-mount-rushmore | 184445 | – | [[executive power]] -> /tr/presidency/executive-power | – | held |
| /podcast/good-citizen/senator-chris-murphy | 163693 | deep_page, heading_skip, meta_duplicate | [[step into the arena]] -> /vote | – |  |
| /tr/family/fdr-connection | 91109 | – | [[Assistant Secretary of the Navy]] -> /tr/rise-to-power/assistant-navy-secretary | – | held |
| / | 84556 | title_too_long, heading_skip | [[Elkhorn Ranch]] -> /tr/badlands/elkhorn-ranch; [[Medora, North Dakota]] -> /tr/badlands/medora | – |  |
| /tr/presidency/bully-pulpit | 52893 | – | [[Doris Kearns Goodwin]] -> /podcast/good-citizen/doris-kearns-goodwin-presidential-stories-trpl-and-enduring-lessons-theodore | – | held |
| /tr/presidency-timeline | 52305 | heading_skip | [[Nobel Peace Prize]] -> /tr/presidency/nobel-peace-prize | – | held |
| /tr/pre-presidency-political-accomplishments | 49964 | – | [[Naval War of 1812]] -> /tr/new-york-politics/naval-war-of-1812 | – | held |
| /tr/timeline | 47114 | heading_skip | [[William Howard Taft]] -> /tr/people/william-howard-taft; [[River of Doubt]] -> /tr/post-presidency/river-of-doubt; [[Edith Roosevelt]] -> /tr/rise-to-power/edith-roosevelt | – | held |
| /visit | 46415 | – | [[Badlands landscape]] -> /tr/badlands/landscape; [[Medora, North Dakota]] -> /tr/badlands/medora; [[Enchanted Highway]] -> /visit/itineraries/enchanted-highway | – | held |
| /tr/tr-importance | 40539 | – | [[Leonard Wood]] -> /tr/people/leonard-wood; [[national forests]] -> /tr/presidency/conservation/national-forests; [[Theodore Roosevelt National Park]] -> /tr/homes-and-places/tr-national-park | – | held |
| /bullet-speech | 38314 | deep_page, h1_multiple | – | – | held |
| /podcast/good-citizen/karl-rove-historic-redemption-hard-work-politics-and-essential-nature | 37993 | deep_page, heading_skip | – | – | held |
| /visit/directions | 36271 | – | [[Little Missouri River]] -> /visit/little-missouri-river | – | held |
| /tr/complex-legacy/imperialism | 34807 | – | [[Assistant Secretary of the Navy]] -> /tr/rise-to-power/assistant-navy-secretary; [[Rough Riders]] -> /tr/rise-to-power/san-juan-hill | – | held |
| /tr/family/family-tree | 31579 | – | [[Kermit Roosevelt]] -> /tr/people/kermit; [[Sagamore Hill]] -> /tr/homes-and-places/sagamore-hill; [[Quentin Roosevelt]] -> /tr/people/quentin | – | held |

### Waiting on FiveJars or blocked (already ticketed; check whether they've landed, don't re-ask)
- Sitewide markup doesn't link to the Library's Wikipedia entry (`schema:sitewide:sameas`): blocked, the per-page sameAs field is capped at 255 characters; FiveJars asked to raise it. Wikidata is in place; Wikipedia and Bluesky go back in once it's raised
- No admission information in the markup (`schema:sitewide:admission`)
- Good Citizen episodes: add PodcastEpisode markup (template, all pages at once) (`schema:podcast_episode`)
- Video pages: add VideoObject markup (template, all pages at once) (`schema:videos`)
- Trip itineraries: add TouristTrip markup (template, all pages at once) (`schema:itineraries`)
- Good Citizen podcast page: add PodcastSeries markup (template, all pages at once) (`schema:podcast_series`)
- Video playlists: add ItemList / VideoObject markup (template, all pages at once) (`schema:video_playlists`)
- 267 pages have dates without a colon in the time zone (`schema:sitewide:date_format`)
- 91 articles are labelled og:type “website” (`schema:sitewide:og_type`)
- Pages with Q&A: add FAQPage markup (template, all pages at once) (`schema:faq`)
- Press releases: add Article / NewsArticle markup (template, all pages at once) (`schema:press`)
- Trustee profiles: add Person / ProfilePage markup (template, all pages at once) (`schema:trustees`)


## Data freshness
| Source | State | Updated | Details |
|---|---|---|---|
| audit | ok | 2026-11-16T12:44:06+00:00 | Crawled 1136 pages, health 95/100 |
| ranks | ok | 2026-11-16T12:51:54+00:00 | 40 keywords checked |
| opportunities | ok | 2026-11-21T13:22:58+00:00 | 16 striking-distance queries, 5 low-CTR pages; 144 recently changed pages held back |
| gsc | ok | 2026-11-21T13:22:58+00:00 | 22298 queries, 2972 pages (2026-10-22 to 2026-11-18); 270 changed pages tracked |
| ai_visibility | error | 2026-11-16T12:58:33+00:00 | 46 answers from ChatGPT, Gemini, Perplexity; 23 failed: Perplexity 403: {"error":{"message":"The Agent API requires paid credits. Sign-up credits and Perplexity Pro or Max subscriptions do not count. Add cr |
| tips | ok | 2026-11-16T13:18:28+00:00 | Gemini wrote tips for 8 pages |
| digest | ok | 2026-11-20T13:24:07+00:00 | llms.txt, digest.md and digest.json rebuilt |
| checkout | ok | 2026-11-21T13:23:11+00:00 | Checkout completion n/a; steps not tracked: view_item, add_to_cart, begin_checkout, add_payment_info |
| curate | ok | 2026-11-16T12:44:38+00:00 | 20 discovered keywords and 8 discovered questions tracked; 7 changes today |
| ux | ok | 2026-11-16T13:12:26+00:00 | 80 pages; PageSpeed on 78; AI task check by gemini (gemini-3.8-flash); GA4 on; Clarity off; 2 errors, e.g. PageSpeed /visit/maps: PageSpeed 500: {   "error": {     "code": 500,     "message": "Lighthouse returned error: PAGE_HUNG. Lighthouse was unable to reliably load the URL you requeste |
| links | ok | 2026-11-16T13:14:05+00:00 | 1170 pages crawled; 1 broken internal links (redirects proposed); 658 suggested links; 45 orphan pages; 27 related pairs without links |
| schema | ok | 2026-11-16T13:15:28+00:00 | 293/889 content pages have their own markup; 6 sitewide issues |
| indexnow | skipped | 2026-11-21T13:23:11+00:00 | No IndexNow key yet: see the work queue task 'Turn on IndexNow'. |

## Google Search (Search Console)
2026-10-22 to 2026-11-18 vs the prior 28 days: **41,003 clicks** (prior 46,732), 2,935,759 impressions (prior 2,382,399), CTR 1.4% (prior 2.0%), average position 5.7 (prior 6.1). Branded clicks 9470, non-branded 10801, search term hidden by Google 20732.

### Top non-branded searches (people who didn't search our name)
| Search | Clicks | Impr. | Pos. |
|---|---|---|---|
| brownsville affair | 2 | 110285 | 4.3 |
| chris murphy | 16 | 79945 | 12 |
| square deal | 150 | 49347 | 3.4 |
| karl rove | 56 | 30775 | 8.6 |
| senator chris murphy | 12 | 25486 | 12.9 |
| roosevelt corollary | 55 | 23269 | 3.8 |
| jacob riis | 157 | 22126 | 8.7 |
| bill kristol | 6 | 20380 | 11.6 |
| bully pulpit | 56 | 19916 | 3.3 |
| chris murphy senator | 10 | 18881 | 12.6 |
| theodore roosevelt | 46 | 15827 | 4.5 |
| the man in the arena | 232 | 12545 | 5.7 |
| theo elections | 4 | 12401 | 6.7 |
| mount rushmore | 9 | 11262 | 10.8 |
| roosevelt family | 13 | 11223 | 3 |
| mount rushmore presidents | 31 | 11189 | 4.1 |
| man in the arena | 71 | 10943 | 7.4 |
| alice roosevelt | 61 | 10574 | 6.9 |
| kermit roosevelt | 17 | 9598 | 7.7 |
| bull moose party | 58 | 9135 | 3.2 |
| sen chris murphy | 7 | 8819 | 10.6 |
| who is on mount rushmore | 8 | 8231 | 6.9 |
| senator murphy | 5 | 7536 | 12.3 |
| alice roosevelt longworth | 17 | 7112 | 7.5 |
| teddy roosevelt | 38 | 6659 | 7 |

### Top pages
| Page | Clicks | Prior | Impr. | Pos. |
|---|---|---|---|---|
| / | 6157 | 9471 | 64680 | 6.2 |
| /?utm_source=gbp&utm_medium=organic | 2318 | 4339 | 17540 | 4 |
| /tickets?utm_source=gbp&utm_medium=organic | 2008 | 3901 | 16568 | 3.8 |
| /tr/family/fdr-connection | 1963 | 1142 | 91109 | 3 |
| /tickets | 1750 | 5105 | 43566 | 3 |
| /tr/speeches/man-in-the-arena | 1485 | 356 | 53358 | 5.4 |
| /tr/presidency/square-deal | 1327 | 463 | 118072 | 3.4 |
| /tr/presidency/trust-busting | 1207 | 903 | 77985 | 3.2 |
| /visit | 921 | 1891 | 46412 | 2.8 |
| /tr/people/jacob-riis | 617 | 343 | 77221 | 6.1 |
| /bullet-speech | 607 | 734 | 38314 | 3.7 |
| /tr/presidency/ten-facts | 575 | 298 | 15453 | 3.7 |
| /tr/quotes | 560 | 617 | 20771 | 3.9 |
| /tr/presidency/food-and-drug | 512 | 24 | 54084 | 5.1 |
| /tr/presidency/panama-canal | 468 | 200 | 76587 | 4.8 |
| /tr/tr-mount-rushmore | 463 | 509 | 184445 | 6.1 |
| /tr/family/family-tree | 412 | 335 | 31579 | 5.2 |
| /tr/presidency/roosevelt-corollary | 405 | 197 | 144460 | 4.2 |
| /tr/tr-importance | 387 | 367 | 40536 | 4.8 |
| /tr/fake-quotes | 379 | 327 | 14895 | 6.2 |
| /tr/rise-to-power/san-juan-hill | 374 | 375 | 32772 | 3.6 |
| /visit/directions | 354 | 741 | 36271 | 3.1 |
| /tr/pre-presidency-political-accomplishments | 353 | 681 | 49964 | 5.7 |
| /tr/complex-legacy/imperialism | 351 | 170 | 34807 | 5.2 |
| /tr/presidency-timeline | 330 | 322 | 52305 | 4.4 |

## Opportunities (ranked)
_Upside is sized against a realistic next step (a few places up, not #1), minus the clicks the page already gets, using a rough industry click-through curve; overlapping searches for one page aren't added twice. Use it to rank opportunities, never as a forecast, and say how the gain would happen: a new ranking, a higher position, or more clicks at the same position._

### Striking distance: ranking 4-20 with demand; strengthen the page for the exact search
| Search | Page | Pos. | Impr. | How | Upside |
|---|---|---|---|---|---|
| brownsville affair | /tr/presidency/brownsville | 4.3 | 110285 | move up from #4 to about #3 | 12131 |
| roosevelt corollary definition | /tr/presidency/roosevelt-corollary | 4.4 | 2864 | move up from #4 to about #3 | 313 |
| roosevelt corollary definition us history | /tr/presidency/roosevelt-corollary | 5.8 | 1546 | move up from #6 to about #3 | 169 |
| the roosevelt corollary | /tr/presidency/roosevelt-corollary | 4 | 1134 | move up from #4 to about #3 | 120 |
| living building challenge | /project/living-building-challenge | 6.3 | 1075 | move up from #6 to about #3 | 115 |
| muckrakers | /quiz/muckrakers | 10.2 | 1912 | move up from #10 to about #5 | 111 |
| rough riders | /tr/rise-to-power/rough-riders/who-were-they | 10.2 | 1884 | move up from #10 to about #5 | 110 |
| who were the rough riders | /tr/rise-to-power/rough-riders | 6.5 | 831 | move up from #6 to about #3 | 87 |
| quanah parker | /tr/people/quanah-parker | 9.7 | 1243 | move up from #10 to about #5 | 72 |
| who were the rough riders | /tr/rise-to-power/rough-riders/who-were-they | 4.4 | 631 | move up from #4 to about #3 | 67 |
| rough riders | /tr/rise-to-power/rough-riders | 7.6 | 1144 | move up from #8 to about #5 | 62 |
| teddy roosevelt presidential library | /calendar/specialty-tour/tr-deep-dive-tour?source=ev | 10.5 | 808 | move up from #10 to about #5 | 45 |
| theodore roosevelt library | /?utm_source=gbp&utm_medium=organic | 4.2 | 1141 | move up from #4 to about #3 | 42 |
| theodore roosevelt presidential library photos | /grand-opening/photos/july4 | 9.1 | 787 | move up from #9 to about #5 | 42 |
| what message did the roosevelt corollary send to the rest of the world? the us had the most powerful navy in the world. the us was in charge of the western hemisphere. the us did not want to be involved in other countries’ affairs. the us had the strongest economy in the world. | /tr/presidency/roosevelt-corollary | 6.3 | 382 | move up from #6 to about #3 | 41 |

### Ranking well but skipped: rewrite title/meta description
| Page | Pos. | CTR | Typical | Upside |
|---|---|---|---|---|
| /tr/presidency/roosevelt-corollary | 4.2 | 0.3% | 8.0% | 11152 |
| /tr/presidency/brownsville | 4.3 | 0.1% | 8.0% | 9006 |
| /visit/hours | 2.2 | 1.2% | 16.0% | 4204 |
| /tr/rise-to-power/rough-riders | 6.4 | 0.4% | 4.5% | 732 |
| /programs | 4.1 | 0.1% | 8.0% | 701 |

### Search words missing from the ranking page's title
| Search | Page | Current title | Missing | Impr. |
|---|---|---|---|---|
| roosevelt corollary definition us history | /tr/presidency/roosevelt-corollary | Roosevelt Corollary to the Monroe Doctrine, Explained / Theodore Roosevelt Presidential Library | definition, us, history | 1546 |
| teddy roosevelt museum | / | Theodore Roosevelt Presidential Library / Medora, North Dakota | teddy, museum | 769 |
| what message did the roosevelt corollary send to the rest of the world? the us had the most powerful navy in the world. the us was in charge of the western hemisphere. the us did not want to be involved in other countries’ affairs. the us had the strongest economy in the world. | /tr/presidency/roosevelt-corollary | Roosevelt Corollary to the Monroe Doctrine, Explained / Theodore Roosevelt Presidential Library | message, did, send, rest, world, us, had, most, powerful, navy, world, us, was, charge, western, hemisphere, us, did, not, want, involved, other, countries, affairs, us, had, strongest, economy, world | 382 |
| trpl | / | Theodore Roosevelt Presidential Library / Medora, North Dakota | trpl | 373 |
| roosevelt corollary simple definition | /tr/presidency/roosevelt-corollary | Roosevelt Corollary to the Monroe Doctrine, Explained / Theodore Roosevelt Presidential Library | simple, definition | 372 |

### Losing clicks vs prior 28 days (check seasonality first)
| Type | Search/page | Clicks | Prior | Change |
|---|---|---|---|---|
| query | theodore roosevelt presidential library | 3357 | 7293 | -54.0% |
| page | /tickets | 1750 | 5105 | -65.7% |
| page | / | 6157 | 9471 | -35.0% |
| page | /?utm_source=gbp&utm_medium=organic | 2318 | 4339 | -46.6% |
| page | /tickets?utm_source=gbp&utm_medium=organic | 2008 | 3901 | -48.5% |
| query | teddy roosevelt presidential library | 1107 | 2588 | -57.2% |
| page | /visit | 921 | 1891 | -51.3% |
| query | teddy roosevelt library | 1243 | 2207 | -43.7% |
| page | /tr/square-deal | 309 | 1075 | -71.3% |
| query | theodore roosevelt library | 798 | 1212 | -34.2% |
| page | /visit/directions | 354 | 741 | -52.2% |
| page | /visit/hours | 330 | 695 | -52.5% |
| page | /tr/pre-presidency-political-accomplishments | 353 | 681 | -48.2% |
| query | roosevelt presidential library | 191 | 433 | -55.9% |
| query | roosevelt library | 148 | 341 | -56.6% |

### Our pages competing for the same search
| Search | Impr. | Pages |
|---|---|---|
| square deal | 64444 | /tr/presidency/square-deal (pos 3.7), /tr/square-deal (pos 5.4) |
| roosevelt family | 15279 | /tr/family/family-tree (pos 3.3), /tr/family (pos 8.4) |
| bull moose party | 9477 | /tr/post-presidency/bull-moose (pos 3.2), /tr/post-presidency/bull-moose/platform (pos 3.6) |
| kermit roosevelt | 8960 | /podcast/good-citizen/kermit-roosevelt-iii (pos 7.7), /about/trustees/kermit-roosevelt (pos 7.1) |
| roosevelt library | 4291 | /tickets (pos 4.7), / (pos 3.6), /visit (pos 2.8), /tickets?utm_source=gbp&utm_medium=organic (pos 1.5) |
| teddy roosevelt museum | 3082 | / (pos 1.6), /tickets (pos 2.0), /visit (pos 2.0), /video/view/Vf8ee-gccpc (pos 4.6) |
| rough riders | 3028 | /tr/rise-to-power/rough-riders/who-were-they (pos 10.2), /tr/rise-to-power/rough-riders (pos 7.6) |
| bamie roosevelt | 2835 | /tr/people/bamie (pos 6.7), /tr/early-life/siblings (pos 7.4), /tr/people/bamie/political-adviser (pos 13.6), /tr/people (pos 13.2) |
| martha bulloch roosevelt | 2819 | /tr/early-life/mother (pos 2.6), /tr/people/mittie (pos 7.2) |
| the square deal | 2755 | /tr/presidency/square-deal (pos 3.0), /tr/square-deal (pos 2.8) |
| what was the square deal | 2092 | /tr/presidency/square-deal (pos 1.7), /tr/square-deal (pos 1.3) |
| square deal definition | 1629 | /tr/presidency/square-deal (pos 1.3), /tr/square-deal (pos 2.2) |
| teddy roosevelt shot | 1511 | /tr/tr-shot (pos 3.6), /bullet-speech (pos 3.1) |
| roosevelt | 1489 | /tr/tr-importance (pos 3.1), /tr/tr-shot (pos 3.0), /tr/family/fdr-connection (pos 3.7) |
| when did theodore roosevelt die | 1472 | /tr/timeline (pos 4.3), /tr/post-presidency/death (pos 7.2) |

## Tracked keywords (dataforseo+gsc)
| Keyword | Group | Volume | GSC pos. | Google rank | AI Overview | Cites us | Above us |
|---|---|---|---|---|---|---|---|
| theodore roosevelt presidential library | Visit | 90500 | 1.3 | – | False | False | google.com, google.com, google.com |
| things to do in medora nd | Visit | 1600 | 1.8 | – | False | False | google.com, google.com, google.com |
| medora north dakota attractions | Visit | 1600 | – | – | True | False | google.com, google.com, google.com |
| things to do near theodore roosevelt national park | Visit | 50 | 1 | – | False | False | google.com, google.com, google.com |
| museums in north dakota | Visit | 320 | 3 | – | True | False | google.com, google.com, google.com |
| north dakota road trip | Visit | 140 | 8.1 | – | True | False | google.com, google.com, google.com |
| medora nd hotels | Visit | 8100 | 4.3 | – | False | False | google.com, google.com, google.com |
| badlands north dakota | Visit | 5400 | 10 | – | True | False | google.com, google.com, google.com |
| theodore roosevelt | History | 450000 | 6.3 | – | True | False | google.com, google.com, google.com |
| theodore roosevelt north dakota | History | 320 | 6 | – | False | False | google.com, google.com, google.com |
| theodore roosevelt badlands | History | 140 | 1.4 | – | True | True | google.com, google.com, google.com |
| elkhorn ranch | History | 2900 | 9.1 | – | True | False | google.com, google.com, google.com |
| maltese cross cabin | History | 720 | 32.4 | – | False | False | google.com, google.com, google.com |
| theodore roosevelt conservation | History | 590 | 6.2 | – | True | False | google.com, google.com, google.com |
| presidential libraries | Presidential libraries | 14800 | 5.9 | – | False | False | google.com, google.com, google.com |
| newest presidential library | Presidential libraries | 210 | 1.9 | – | True | False | google.com, google.com, google.com |
| presidential library road trip | Presidential libraries | – | – | – | True | False | google.com, google.com, google.com |
| theodore roosevelt quotes | Learning | 6600 | 3.1 | – | True | True | google.com, google.com, google.com |
| theodore roosevelt man in the arena | Learning | 2400 | 4.3 | – | True | False | google.com, google.com, google.com |
| theodore roosevelt podcast | Learning | 10 | – | – | True | True | google.com, google.com, google.com |
| teddy roosevelt national park | Auto: Visit | 74000 | 9.9 | – | False | False | google.com, google.com, google.com |
| enchanted highway | Auto: Visit | 9900 | 9.8 | – | False | False | google.com, google.com, google.com |
| mount rushmore presidents | Auto: Visit | 27100 | 4 | – | True | False | google.com, google.com, google.com |
| teddy roosevelt | Auto: History | 450000 | 6.8 | – | False | False | google.com, google.com, google.com |
| theodore roosevelt died | Auto: History | 5400 | 4.6 | – | True | False | google.com, google.com, google.com |
| brownsville affair | Auto: History | 590 | 4.7 | – | True | True | google.com, google.com, google.com |
| roosevelt corollary | Auto: History | 33100 | 4.1 | – | True | True | google.com, google.com, google.com |
| jacob riis | Auto: History | 33100 | 9.1 | – | False | False | google.com, google.com, google.com |
| alice roosevelt longworth | Auto: Family | 27100 | 8 | – | False | False | google.com, google.com, google.com |
| bull moose party | Auto: History | 9900 | 3 | – | True | True | google.com, google.com, google.com |
| alice roosevelt | Auto: Family | 27100 | 7 | – | False | False | google.com, google.com, google.com |
| man in the arena | Auto: Learning | 18100 | 7.2 | – | True | False | google.com, google.com, google.com |
| kermit roosevelt | Auto: Family | 12100 | 7.8 | – | False | False | google.com, google.com, google.com |
| who is on mount rushmore | Auto: Learning | 18100 | 6.9 | – | True | False | google.com, google.com, google.com |
| quentin roosevelt | Auto: Family | 9900 | 11.3 | – | False | False | google.com, google.com, google.com |
| alice hathaway lee roosevelt | Auto: History | 9900 | 5.9 | – | False | False | google.com, google.com, google.com |
| american imperialism | Auto: Learning | 12100 | 7 | – | True | False | google.com, google.com, google.com |
| archibald roosevelt | Auto: History | 5400 | 7.8 | – | False | False | google.com, google.com, google.com |
| booker t washington | Auto: History | 110000 | 12.6 | – | False | False | google.com, google.com, google.com |
| bully pulpit meaning | Auto: Learning | 4400 | 4.4 | – | True | True | google.com, google.com, google.com |

## AI assistant visibility
| Engine | Model | Mentions us | Cites trlibrary.com |
|---|---|---|---|
| ChatGPT | gpt-5-mini | 47.8% | 47.8% |
| Gemini | gemini-3.8-flash | 30.4% | 17.4% |
| Perplexity | fast | – | – |

### Question by question
Some answers failed this week: perplexity: Perplexity 403: {"error":{"message":"The Agent API requires paid credits. Sign-up credits and Perplexity Pro or Max subscriptions do not cou

**I'm visiting Theodore Roosevelt National Park. What else should I see nearby?** (Trip planning)
- ChatGPT: mentioned, #8 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Chateau de Mores, North Dakota Cowboy Hall of Fame, Medora Musical, Maah Daah Hey Trail, Painted Canyon, Elkhorn Ranch. Described as: "([trlibrary.com](https://www.trlibrary.com/visit/national-park/elkhorn-ranch?utm_source=openai)) … ([trlibrary.com](https://www.trlibrary.com/visit/itineraries/enchanted-highway?utm_source=openai))" Sources: discovermedora.com, medorand.org, ndtourism.com, history.nd.gov, en.wikipedia.org, trlibrary.com
- Gemini: NOT mentioned. Also named: Theodore Roosevelt National Park, Medora Musical, Maah Daah Hey Trail, Elkhorn Ranch. Sources: none

**What are the best things to do in Medora, North Dakota?** (Trip planning)
- ChatGPT: mentioned, #5 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Painted Canyon, Medora Musical, Pitchfork Steak Fondue, Chateau de Mores, North Dakota Cowboy Hall of Fame, Maah Daah Hey Trail. Described as: "- Visit the Theodore Roosevelt Presidential Library: the new TR Presidential Library opened in 2026 near Medora and is now a major museum attraction about Roosevelt’s life and ties to the Badlands. … ([trlibrary.com](https://www.trlibrary.com/?utm_source=openai))" Sources: nps.gov, medora.com, trlibrary.com, history.nd.gov, parkrec.nd.gov, ndtourism.com
- Gemini: mentioned, #5 among attractions. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Medora Musical, Pitchfork Steak Fondue, North Dakota Cowboy Hall of Fame, Maah Daah Hey Trail. Described as: "Visit the Theodore Roosevelt Presidential Library" Sources: nd.gov, ndtourism.com, discovermedora.com, visitdickinson.com

**Plan a 3-day road trip through western North Dakota. What are the must-see stops?** (Trip planning)
- ChatGPT: mentioned, #5 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Chateau de Mores, Medora Musical, Maah Daah Hey Trail. Described as: "([trlibrary.com](https://www.trlibrary.com/visit/itineraries/enchanted-highway?utm_source=openai))" Sources: nps.gov, ndtourism.com, visitwatfordcity.com, travelmath.com, trlibrary.com, medora.com
- Gemini: NOT mentioned. Also named: Theodore Roosevelt National Park, Medora Musical, Painted Canyon, Chateau de Mores, Pitchfork Steak Fondue, Maltese Cross Cabin. Sources: none

**We're driving from Mount Rushmore to Theodore Roosevelt National Park. What's worth stopping for?** (Trip planning)
- ChatGPT: mentioned, #3 among attractions, cites trlibrary.com. Also named: Mount Rushmore, Painted Canyon, Theodore Roosevelt National Park. Described as: "([trlibrary.com](https://www.trlibrary.com/visit/itineraries/sturgis-medora?utm_source=openai)) … - Plan time to drive the South Unit scenic loop, walk some short trails, and visit the Painted Canyon Visitor Center or the Theodore Roosevelt Presidential Library in town." Sources: medora.com, blackhillsvacations.com, travelmath.com, en.wikipedia.org, wall-badlands.com, assets.simpleviewinc.com
- Gemini: NOT mentioned. Also named: Mount Rushmore, Theodore Roosevelt National Park, Chateau de Mores, Pitchfork Steak Fondue, Medora Musical. Sources: none

**What are the best stops along I-94 in North Dakota?** (Trip planning)
- ChatGPT: NOT mentioned. Also named: Painted Canyon, Theodore Roosevelt National Park, Medora Musical. Sources: ndtourism.com, mystateparks.com, en.wikipedia.org, avivadirectory.com, visitfargo.com
- Gemini: NOT mentioned. Also named: Theodore Roosevelt National Park, Painted Canyon, Medora Musical, Chateau de Mores. Sources: none

**Fun things to do with kids in the North Dakota Badlands?** (Trip planning)
- ChatGPT: mentioned, #4 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Painted Canyon, Medora Musical, Maah Daah Hey Trail. Described as: "([trlibrary.com](https://www.trlibrary.com/visit/activities?utm_source=openai))" Sources: home.nps.gov, ndtourism.com, medora.com, en.wikipedia.org, medorand.org, trlibrary.com
- Gemini: NOT mentioned. Also named: Theodore Roosevelt National Park, Painted Canyon, Maltese Cross Cabin, Medora Musical, Pitchfork Steak Fondue, Chateau de Mores, North Dakota Cowboy Hall of Fame. Sources: none

**What can we do indoors in Medora if the weather is bad?** (Trip planning)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Also named: Chateau de Mores, North Dakota Cowboy Hall of Fame. Described as: "- Theodore Roosevelt Presidential Library — a large, new indoor museum with multi-room exhibits (plan 2–4 hours). … ([trlibrary.com](https://www.trlibrary.com/visit/activities?utm_source=openai))" Sources: trlibrary.com, history.nd.gov, medora.com, northdakotacowboy.org
- Gemini: NOT mentioned. Also named: North Dakota Cowboy Hall of Fame, Chateau de Mores, Theodore Roosevelt National Park, Maltese Cross Cabin. Sources: medorand.org, medora.com, wanderlog.com, fargomom.com, youtube.com

**What are the best museums in North Dakota?** (Museums)
- ChatGPT: NOT mentioned. Also named: North Dakota Cowboy Hall of Fame. Sources: statemuseum.nd.gov, plainsart.org, ndmoa.com, bonanzaville.org, ndtourism.com, dakotaterritoryairmuseum.com
- Gemini: NOT mentioned. Also named: North Dakota Cowboy Hall of Fame, Theodore Roosevelt National Park, Chateau de Mores. Sources: none

**What is the newest presidential library in the United States?** (Museums)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Described as: "Short answer: the Theodore Roosevelt Presidential Library in Medora, North Dakota — it opened on July 4, 2026, making it the newest presidential library in the U.S. … ([trlibrary.com](https://www.trlibrary.com/about/press/press-releases/theodore-roosevelt-presidential-library-opening-celebrations-july-4-2026?utm_source=openai))" Sources: trlibrary.com, abc7chicago.com, node210155-env-6616231.j.layershift.co.uk
- Gemini: mentioned, #1 among attractions, cites trlibrary.com. Described as: "Newest Presidential Library: **Theodore Roosevelt Presidential Library** (Opened July 4, 2026) … Unlike modern post-Hoover libraries, it is operated privately by the Theodore Roosevelt Presidential Library Foundation rather than NARA, with Roosevelt's official papers historically housed at the Library of Congress." Sources: youtube.com, trlibrary.com, wikipedia.org, ap.org, archives.gov

**Which presidential libraries are worth visiting?** (Museums)
- ChatGPT: NOT mentioned. Sources: nps.gov, reaganlibrary.gov, archives.gov, clintonlibrary.gov, bushcenter.org, lbjlibrary.org
- Gemini: NOT mentioned. Sources: none

**Where can I learn about Theodore Roosevelt's life in North Dakota?** (History)
- ChatGPT: NOT mentioned. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Painted Canyon, Elkhorn Ranch, Chateau de Mores. Sources: none
- Gemini: mentioned, #4 among attractions. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Elkhorn Ranch, Chateau de Mores, North Dakota Cowboy Hall of Fame. Described as: "* **Theodore Roosevelt Presidential Library (Medora, ND)**" Sources: nd.gov

**What historic sites are connected to Theodore Roosevelt?** (History)
- ChatGPT: NOT mentioned. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Elkhorn Ranch, Mount Rushmore. Sources: nps.gov, npgallery.nps.gov, amnh.org, home.nps.gov
- Gemini: mentioned, #5 among attractions. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Elkhorn Ranch, Mount Rushmore. Described as: "* **Theodore Roosevelt Presidential Library (Medora, North Dakota):** Established near the Badlands to house his personal papers, digital archives, and exhibits on his conservation legacy." Sources: none

**Is the Theodore Roosevelt Presidential Library worth visiting?** (Brand)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Medora Musical. Described as: "Short answer: Yes—for many visitors the Theodore Roosevelt Presidential Library in Medora, ND is worth a trip. … ([trlibrary.com](https://www.trlibrary.com/?utm_source=openai))" Sources: trlibrary.com, snohetta.prezly.com, tripadvisor.com
- Gemini: mentioned, #1 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Chateau de Mores, Medora Musical. Described as: "The **Theodore Roosevelt Presidential Library** in **Medora, North Dakota** is widely considered **well worth visiting**—particularly if you pair it with a broader trip to Theodore Roosevelt National Park and the surrounding Badlands. … If you are a fan of presidential history, conservation, or innovative architecture, the Theodore Roosevelt Presidential Library is an exceptional cultural destination." Sources: ndtourism.com, nationalreview.com, trlibrary.com, reddit.com, eastwingmagazine.com, medora.com

**How much time do I need at the Theodore Roosevelt Presidential Library?** (Brand)
- ChatGPT: mentioned, #2 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park. Described as: "([trlibrary.com](https://www.trlibrary.com/visit/faq/during-your-visit)) … ([trlibrary.com](https://www.trlibrary.com/visit/faq/during-your-visit))" Sources: trlibrary.com
- Gemini: mentioned, #1 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park. Described as: "For a visit to the **Theodore Roosevelt Presidential Library** in Medora, North Dakota, plan to spend around **3 to 3.5 hours**." Sources: trlibrary.com, visitdickinson.com, nd.gov, reddit.com

**How much are tickets to the Theodore Roosevelt Presidential Library and when is it open?** (Brand)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Described as: "([trlibrary.com](https://www.trlibrary.com/tickets)) … ([trlibrary.com](https://www.trlibrary.com/visit/hours))" Sources: trlibrary.com
- Gemini: mentioned, #1 among attractions, cites trlibrary.com. Described as: "The **Theodore Roosevelt Presidential Library** is located in Medora, North Dakota." Sources: trlibrary.com, wikipedia.org, ndtourism.com

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
- ChatGPT: NOT mentioned. Also named: Mount Rushmore. Sources: none
- Gemini: NOT mentioned. Also named: Mount Rushmore. Sources: none

**What is the meaning and origin of the term bully pulpit in American politics?** (Auto: History)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Described as: "([trlibrary.com](https://www.trlibrary.com/tr/presidency/bully-pulpit?utm_source=openai))" Sources: etymonline.com, worldwidewords.org, trlibrary.com
- Gemini: NOT mentioned. Sources: none

**What was the Roosevelt Corollary to the Monroe Doctrine and why does it matter?** (Auto: History)
- ChatGPT: NOT mentioned. Sources: none
- Gemini: NOT mentioned. Sources: none

### Sites AI assistants cite most
trlibrary.com (15), ndtourism.com (9), medora.com (7), nps.gov (6), history.nd.gov (4), en.wikipedia.org (4), medorand.org (3), nd.gov (3), discovermedora.com (2), npgallery.nps.gov (2), visitwatfordcity.com (2), travelmath.com (2), home.nps.gov (2), northdakotacowboy.org (2), archives.gov (2)

### Searches the assistants ran before answering
Searches the assistants ran before answering. 'Google' is trlibrary.com's Search Console position for the same search (last 28 days); none means the site doesn't show for it, or too rarely to report. A search we don't rank for is a page to strengthen or write. 147 different searches: we rank top 10 for 1, lower for 0, not at all for 146.

| Search the assistant ran | Engines | In answers missing us | trlibrary.com in Google |
|---|---|---|---|
| Badlands Dinosaur Museum Dickinson official site | ChatGPT | 1 | – |
| Bismarck Mandan attractions Fort Abraham Lincoln State Park North Dakota I-94 | ChatGPT | 1 | – |
| Bonanzaville West Fargo museum official site | ChatGPT | 1 | – |
| Dakota Territory Air Museum Minot official site | ChatGPT | 1 | – |
| Dakota Thunder Jamestown buffalo sculpture 'World's largest buffalo' Dakota Thunder Jamestown location I-94 exit | ChatGPT | 1 | – |
| Dwight D. Eisenhower Presidential Library Abilene Kansas official site | ChatGPT | 1 | – |
| Enchanted Highway Regent North Dakota distance from I-94 | ChatGPT | 1 | – |
| Fargo Air Museum official site | ChatGPT | 1 | – |
| Fargo attractions along I-94 Fargo Moorhead stops "Plains Art Museum" "Red River Zoo" | ChatGPT | 1 | – |
| Fort Abraham Lincoln State Park Mandan near I-94 'Fort Abraham Lincoln' 'Custer's house' 'On-A-Slant Mandan Indian Village' 'Mandan' | ChatGPT | 1 | – |
| Franklin D. Roosevelt Presidential Library and Museum Hyde Park official site | ChatGPT | 1 | – |
| George W. Bush Presidential Center Dallas official site | ChatGPT | 1 | – |
| Gerald R. Ford Presidential Library Ann Arbor and Gerald R. Ford Museum Grand Rapids official sites | ChatGPT | 1 | – |
| Harry S. Truman Presidential Library and Museum Independence Missouri official site | ChatGPT | 1 | – |
| Herbert Hoover Presidential Library and Museum West Branch Iowa official site | ChatGPT | 1 | – |
| I-94 North Dakota best stops attractions Theodore Roosevelt National Park Medora | ChatGPT | 1 | – |
| Jamestown North Dakota National Buffalo Museum and attraction I-94 | ChatGPT | 1 | – |
| John F. Kennedy Presidential Library and Museum Boston official site | ChatGPT | 1 | – |
| Lyndon B. Johnson Presidential Library Austin official site LBJ Ranch | ChatGPT | 1 | – |
| McKenzie County Heritage Park & Oil Museum Watford City official site | ChatGPT | 1 | – |

### Pages AI cites when it leaves the Library out
Pages cited in answers that left the Library out. 'Mentions the Library' comes from reading the page once (blank = not read or couldn't be read). A list that names other attractions but not the Library is the cheapest fix: ask to be added. 28 answers left the Library out. Citations by type: reference 19, other 15, partner 7, list or guide 1, social 1.

| Page | Type | Answers | Mentions the Library | Attractions it helped name |
|---|---|---|---|---|
| https://www.ndtourism.com/best-places/8-things-see-and-do-theodore-roosevelt-national-park | partner | 1 | – | Painted Canyon, Theodore Roosevelt National Park, Medora Musical |
| https://www.ndtourism.com/regent/attractions-entertainment/family-fun/enchanted-highway | partner | 1 | – | Painted Canyon, Theodore Roosevelt National Park, Medora Musical |
| https://www.ndtourism.com/beach/attractions-entertainment/arts-attractions/prairie-fire-pottery | partner | 1 | – | Painted Canyon, Theodore Roosevelt National Park, Medora Musical |
| https://www.ndtourism.com/dickinson/attractions-entertainment/educational-attractions/dickinson-museum-center | partner | 1 | – | Painted Canyon, Theodore Roosevelt National Park, Medora Musical |
| https://www.mystateparks.com/parks/nd-fort-abraham-lincoln-state-park | other | 1 | NO | Painted Canyon, Theodore Roosevelt National Park, Medora Musical |
| https://en.wikipedia.org/wiki/Salem_Sue | reference | 1 | NO | Painted Canyon, Theodore Roosevelt National Park, Medora Musical |
| https://www.ndtourism.com/jamestown/attractions-entertainment/educational-attractions/worlds-largest-buffalo-monument | partner | 1 | – | Painted Canyon, Theodore Roosevelt National Park, Medora Musical |
| https://www.avivadirectory.com/Regional/North-America/United-States/States/North-Dakota/Cities-Towns/Valley-City | other | 1 | NO | Painted Canyon, Theodore Roosevelt National Park, Medora Musical |
| https://visitfargo.com/attractions/museums_history | other | 1 | NO | Painted Canyon, Theodore Roosevelt National Park, Medora Musical |
| https://statemuseum.nd.gov | reference | 1 | NO | North Dakota Cowboy Hall of Fame |
| https://plainsart.org/about | other | 1 | NO | North Dakota Cowboy Hall of Fame |
| https://ndmoa.com/plan-your-visit | other | 1 | NO | North Dakota Cowboy Hall of Fame |
| https://www.bonanzaville.org | other | 1 | NO | North Dakota Cowboy Hall of Fame |
| https://www.ndtourism.com/fargo/attractions-entertainment/aviation-flight/fargo-air-museum | partner | 1 | – | North Dakota Cowboy Hall of Fame |
| https://dakotaterritoryairmuseum.com | other | 1 | NO | North Dakota Cowboy Hall of Fame |
| https://www.dickinsongov.com/museum-center | other | 1 | – | North Dakota Cowboy Hall of Fame |
| https://northdakotacowboy.org | other | 1 | – | North Dakota Cowboy Hall of Fame |
| https://www.history.nd.gov/historicsites/pembina | reference | 1 | – | North Dakota Cowboy Hall of Fame |
| https://www.visitwatfordcity.com/usrfiles/MCT-Visitors-Guide-2025.pdf | list or guide | 1 | – | North Dakota Cowboy Hall of Fame |
| https://www.nps.gov/places/franklin-d-roosevelt-presidential-library-and-museum.htm | reference | 1 | – |  |

**Ask to be added** (cited by AI, lists other things, doesn't mention the Library):
- https://www.mystateparks.com/parks/nd-fort-abraham-lincoln-state-park (other; cited in 1 answers)
- https://www.avivadirectory.com/Regional/North-America/United-States/States/North-Dakota/Cities-Towns/Valley-City (other; cited in 1 answers)
- https://visitfargo.com/attractions/museums_history (other; cited in 1 answers)
- https://plainsart.org/about (other; cited in 1 answers)
- https://ndmoa.com/plan-your-visit (other; cited in 1 answers)
- https://www.bonanzaville.org (other; cited in 1 answers)
- https://dakotaterritoryairmuseum.com (other; cited in 1 answers)

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
Crawled 1136 of 1175 sitemap URLs. Health 95/100, AI readiness 61/100. llms.txt on trlibrary.com: yes. AI crawlers blocked in robots.txt: none. 406 pages have page-specific structured data (sitewide on every page: BreadcrumbList, EntryPoint, GeoCoordinates, ImageObject, ListItem, OpeningHoursSpecification, PostalAddress, SearchAction, WebSite).

| Severity | Issue | Pages | Examples |
|---|---|---|---|
| medium | Same title as another page | 69 | /node/240, /node/241, /node/244, /node/245, /node/249 |
| medium | Sitemap lists a /node/ URL instead of a readable path | 35 | /node/240, /node/241, /node/244, /node/245, /node/249 |
| medium | No H1 heading | 29 | /birthdaycard, /project/how-the-library-works, /rsvp/midwinter, /about/reports/2024-annual-report, /privacy |
| medium | Missing Open Graph tags | 27 | /birthdaycard, /project/how-the-library-works, /rsvp/midwinter, /quiz/the-boardwalk, /video/view/-QfzHHXPYqM |
| medium | No meta description | 26 | /birthdaycard, /project/how-the-library-works, /rsvp/midwinter, /quiz/the-boardwalk, /video/view/-QfzHHXPYqM |
| medium | Sitemap lists a URL that redirects | 5 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /calendar/special-event/book-signing-and-meet-greet-kennerly-balkowitsch-and-ziemendorf, /event/24 |
| low | Title over 60 characters, not counting the site-name suffix | 264 | /node/240, /node/241, /node/244, /node/245, /node/249 |
| low | Under 150 words of body text | 237 | /birthdaycard, /project/how-the-library-works, /node/240, /node/241, /node/244 |
| low | Heading levels skip (e.g. H2 straight to H4) | 151 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /calendar/special-event/book-signing-and-meet-greet-kennerly-balkowitsch-and-ziemendorf, /node/589 |
| low | Title under 15 characters, not counting the site-name suffix | 145 | /birthdaycard, /quiz/the-boardwalk, /visit/survey, /video/view/Y3jQTzNVVFY, /video/view/YJ_qzszUZUA |
| low | Same meta description as another page | 131 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /calendar/special-event/book-signing-and-meet-greet-kennerly-balkowitsch-and-ziemendorf, /event/24 |
| low | More than 4 clicks from the homepage | 112 | /node/240, /node/241, /node/244, /node/245, /node/249 |
| low | Meta description under 70 characters | 18 | /video/view/Y3jQTzNVVFY, /video/view/YJ_qzszUZUA, /video/view/Lk8bs9ilpLI, /video/view/0NiRkijqLGw, /video/view/NoLhSWhiCpA |
| low | More than one H1 | 10 | /support/matching-gifts, /about/mission, /about/foundation, /impact, /project |
| low | Took over 3 seconds to respond | 3 | /video/view/-hAbH24Ia_w, /video/view/-TNqu1aIePM, /video/view/BF6ZHFqp2Qg |

## Recently changed pages (held back from recommendations for 28 days)
Before = the 28 days before the change; after = the days since, up to the latest settled Search Console day. Compare per-day numbers; a week or two after a change is still early.

| Page | Changed | What | Clicks/day before → after | CTR | Position |
|---|---|---|---|---|---|
| /tickets | 2026-11-16 | Title 'Tickets and Admission: Timed Entry and Prices'; prices, 3½ hours and discounts in d | 69.0 → 46.0 | 4.2% → 3.9% | 3.0 → 3.0 |
| /tr/presidency/nobel-peace-prize | 2026-11-16 | Title 'Why Theodore Roosevelt Won the Nobel Peace Prize'; Portsmouth and first American No | 2.4 → 3.5 | 0.6% → 0.6% | 4.5 → 4.0 |
| /tr/presidency/foreign-policy | 2026-11-16 | Title 'Theodore Roosevelt’s Foreign Policy: The Big Stick Era'; Panama Canal and Great Whi | 3.0 → 7.0 | 0.6% → 0.6% | 4.7 → 5.4 |
| /visit/itineraries/enchanted-highway | 2026-11-16 | Title adds 'North Dakota' | 0.6 → 1.0 | 0.5% → 0.5% | 8.2 → 8.5 |
| /visit/itineraries/sturgis-medora | 2026-11-16 | Removed past rally dates ('runs 7–16 August 2026' → 'Every August') | 0.0 → 0.0 | 0.0% → 0.0% | 7.8 → 8.0 |
| /visit/itineraries/presidential-libraries | 2026-11-16 | Hoover museum: 'reopens on 6 August 2026' → 'has reopened after a $20 million renovation' | 0.6 → 1.0 | 1.6% → 2.6% | 6.9 → 8.2 |
| /visit/scenic-drives | 2026-11-16 | Loop drive: dropped 'late 2025' from reopening | 0.1 → 0.0 | 0.8% → 0.0% | 7.8 → 7.5 |
| /tr/rise-to-power/spanish-american-war | 2026-11-09 | Title 'Theodore Roosevelt and the Spanish-American War'; Navy/Rough Riders description | 6.4 → 11.7 | 0.5% → 0.7% | 5.7 → 5.5 |
| /tr/presidency/food-and-drug | 2026-11-09 | Title 'Pure Food and Drug Act and Meat Inspection Act of 1906'; drops '1905 novel' | 10.6 → 21.2 | 0.9% → 1.1% | 5.3 → 4.7 |
| /tr/people/archibald | 2026-11-09 | Title 'Archibald Roosevelt: TR’s Son Wounded in Two World Wars' | 0.1 → 0.3 | 0.1% → 0.2% | 7.4 → 7.4 |
| /visit/lodging | 2026-11-09 | Title 'Medora Hotels, Cabins and Campgrounds'; names Hotel 1883 | 4.8 → 2.6 | 0.9% → 0.5% | 7.7 → 7.4 |
| /join-us | 2026-11-09 | Title 'Join Us: Become a Member, Volunteer or Work Here'; first description and OG tags | 0.0 → 0.1 | 0.0% → 0.1% | 4.4 → 3.2 |
| /visit/exhibits/kennerly | 2026-11-09 | Title 'In the Room: David Hume Kennerly Photo Exhibition'; first description and OG tags | 2.3 → 2.8 | 2.4% → 1.7% | 6.5 → 5.4 |
| /about/trustees/kermit-roosevelt | 2026-11-09 | Title 'Kermit Roosevelt, Library Trustee' (was duplicate of /tr/people/kermit) | 0.4 → 0.1 | 0.5% → 0.1% | 6.9 → 6.6 |
| /about/trustees/douglas-brinkley | 2026-11-09 | Title 'Douglas Brinkley, Library Trustee' (was duplicate of podcast page) | 0.1 → 0.1 | 0.4% → 0.2% | 10.2 → 13.0 |
| /contact | 2026-11-09 | Title 'Contact Us: Phone, Address and Message Form'; phone and address in description | 1.9 → 2.2 | 1.0% → 1.6% | 2.9 → 3.1 |
| /visit/tickets/plan-ahead | 2026-11-09 | Description no longer leads with summer; removed '2026 is the Library's first year' | 0.6 → 0.2 | 1.3% → 0.6% | 6.7 → 7.5 |
| /llms.txt | 2026-11-09 | Added 'Key facts for visitors' (address, 3½ hours, year-round, tickets, indoor, not the FD | 0.0 → 0.0 | – → – | – → – |
| /about/press/press-releases | 2026-11-03 | Press releases: og:type article, NewsArticle author/publisher/description, ISO dates with  | 0.0 → 0.0 | 0.0% → – | 11.0 → – |
| /podcast/good-citizen | 2026-11-03 | Podcast episodes: og:type article | 1.3 → 0.9 | 1.5% → 1.1% | 7.1 → 7.7 |
| /about/trustees | 2026-11-03 | Trustee Person markup: memberOf the Library | 1.9 → 1.6 | 9.8% → 10.4% | 9.0 → 6.9 |
| /tr/presidency | 2026-11-03 | Published Oct 18 draft plus 2 internal links (Taft, midnight forests) | 0.9 → 4.2 | 0.6% → 1.0% | 6.3 → 5.2 |
| /tr/timeline | 2026-11-03 | Added 6 internal links from Links to add; Title 'Theodore Roosevelt's Life Timeline: Key D | 7.8 → 7.7 | 0.5% → 0.4% | 7.4 → 6.6 |
| /visit/exhibits/main | 2026-11-03 | Added 6 internal links from Links to add | 2.8 → 1.5 | 1.8% → 0.8% | 6.5 → 5.9 |
| /tr/teddy-nickname | 2026-11-03 | Added 6 internal links from Links to add; Merged /tr/myths/teddy-name into this page; new  | 4.8 → 5.4 | 0.8% → 0.8% | 4.4 → 4.7 |
| /tr/presidency-timeline | 2026-11-03 | Added 6 internal links from Links to add; Title 'When Was Theodore Roosevelt President? 19 | 11.5 → 11.5 | 0.6% → 0.6% | 4.6 → 4.5 |
| /tr/people/henry-cabot-lodge | 2026-11-03 | Added 6 internal links from Links to add | 1.1 → 1.4 | 0.2% → 0.3% | 6.5 → 6.5 |
| /tr/family/family-tree | 2026-11-03 | Added 5 internal links from Links to add | 14.2 → 15.8 | 1.5% → 1.2% | 5.2 → 4.9 |
| /tr/presidency/white-house-family | 2026-11-03 | Added 4 internal links from Links to add | 0.2 → 0.5 | 0.3% → 0.6% | 6.6 → 7.4 |
| /podcast/good-citizen/doris-kearns-goodwin-presidential-stories-trpl-and-enduring-lessons-theodore | 2026-11-03 | Added 5 internal links from Links to add | 0.3 → 0.3 | 0.8% → 0.9% | 8.8 → 9.0 |
| /tr/legacy/rankings | 2026-11-03 | Added 5 internal links from Links to add | 5.0 → 7.6 | 1.5% → 1.8% | 5.6 → 6.2 |
| /podcast/good-citizen/edward-okeefe | 2026-11-03 | Added 4 internal links from Links to add | 0.1 → 0.1 | 0.8% → 1.5% | 8.2 → 7.6 |
| /podcast/good-citizen/call-adventure-charlie-melcher-ed-okeefe-and-brand-new-theodore-roosevelt | 2026-11-03 | Added 6 internal links from Links to add | 0.3 → 0.0 | 1.1% → 0.0% | 7.4 → 7.1 |
| /tr/for-educators/high-school | 2026-11-03 | Added 6 internal links from Links to add | 0.8 → 0.7 | 1.8% → 1.4% | 7.0 → 6.7 |
| /about/press/press-releases/theodore-roosevelts-groundbreaking-firsts-and-feats-celebration | 2026-11-03 | Added 6 internal links from Links to add | 0.1 → 0.3 | 1.1% → 1.3% | 4.7 → 6.1 |
| /tr/rise-to-power/ten-facts | 2026-11-03 | Added 6 internal links from Links to add | 3.3 → 4.9 | 1.6% → 2.6% | 5.3 → 4.1 |
| /tr/presidency/ten-facts | 2026-11-03 | Added 5 internal links from Links to add | 15.5 → 21.3 | 2.8% → 4.0% | 3.9 → 3.8 |
| /events/teddycon | 2026-11-03 | Added 6 internal links from Links to add | 3.4 → 0.2 | 8.8% → 1.1% | 3.8 → 6.0 |
| /tr/badlands-timeline | 2026-11-03 | Added 6 internal links from Links to add | 5.7 → 6.3 | 2.0% → 2.2% | 5.5 → 5.4 |
| /tr/family/fdr-connection | 2026-11-03 | Added 4 internal links from Links to add; Title 'How Were Theodore and Franklin Roosevelt  | 60.9 → 66.8 | 1.9% → 2.1% | 3.2 → 2.9 |
| /research/archives | 2026-11-03 | Added 5 internal links from Links to add | 1.7 → 1.4 | 2.5% → 2.0% | 7.7 → 8.1 |
| /tr/speeches/new-nationalism | 2026-11-03 | Added 5 internal links from Links to add | 1.7 → 0.3 | 2.0% → 0.6% | 5.6 → 7.5 |
| /tr/presidency/elections | 2026-11-03 | Added 4 internal links from Links to add; Title '1904 Presidential Election: Roosevelt's M | 4.5 → 6.8 | 0.6% → 1.2% | 5.9 → 5.4 |
| /tr/legacy/the-library | 2026-11-03 | Added 5 internal links from Links to add | 1.2 → 0.3 | 1.0% → 1.1% | 5.0 → 4.8 |
| /tr/post-presidency/ten-facts | 2026-11-03 | Added 5 internal links from Links to add | 0.4 → 0.3 | 1.0% → 0.8% | 5.5 → 5.6 |
| /visit/medora/history | 2026-11-03 | Added 5 internal links from Links to add; North Dakota quote aligned to the 1918 Volwiler  | 1.2 → 0.7 | 1.2% → 1.3% | 7.4 → 7.8 |
| /tr/fake-quotes | 2026-11-03 | Added 3 internal links from Links to add | 11.7 → 12.7 | 2.0% → 2.2% | 6.8 → 6.2 |
| /tr/kids-timeline | 2026-11-03 | Added 5 internal links from Links to add; Title 'Theodore Roosevelt for Kids: A Timeline o | 2.5 → 2.5 | 0.7% → 0.9% | 9.4 → 10.7 |
| /tr/tr-mount-rushmore | 2026-11-03 | Added 3 internal links from Links to add; Title 'Mount Rushmore Presidents: Why Theodore R | 16.0 → 15.2 | 0.4% → 0.2% | 5.5 → 6.4 |
| /visit/directions | 2026-11-03 | Added 4 internal links from Links to add; Title 'Directions to Medora from I-94 and Nearby | 21.1 → 7.9 | 1.2% → 0.8% | 2.7 → 3.5 |
| /tr/books-and-writings/autobiography | 2026-11-03 | Added 4 internal links from Links to add | 1.1 → 1.3 | 1.3% → 1.7% | 5.7 → 4.9 |
| /tr/pre-presidency-political-accomplishments | 2026-11-03 | Added 4 internal links from Links to add; Title 'What Did Theodore Roosevelt Do Before He  | 20.5 → 13.1 | 1.1% → 0.8% | 5.6 → 5.7 |
| /tr/books-and-writings/complete-list | 2026-11-03 | Added 4 internal links from Links to add | 0.2 → 0.1 | 1.9% → 0.8% | 5.4 → 5.0 |
| /tr/quotes/leadership | 2026-11-03 | Added 5 internal links from Links to add | 3.6 → 2.8 | 3.0% → 2.8% | 5.4 → 5.4 |
| /tr/speeches/inaugural | 2026-11-03 | Added 4 internal links from Links to add | 0.5 → 0.9 | 0.5% → 0.6% | 5.7 → 5.9 |
| /podcast/good-citizen/candice-millard | 2026-11-03 | Added 2 internal links from Links to add | 0.4 → 0.4 | 0.3% → 0.3% | 9.3 → 10.1 |
| /tr/people/eleanor | 2026-11-03 | Added 4 internal links from Links to add | 0.4 → 1.4 | 0.5% → 0.6% | 6.9 → 7.3 |
| /tr/people/bill-sewall | 2026-11-03 | Added 4 internal links from Links to add | 0.6 → 0.5 | 2.2% → 1.1% | 5.5 → 5.2 |
| /tr/post-presidency/quentin | 2026-11-03 | Added 4 internal links from Links to add | 1.0 → 1.3 | 0.4% → 0.7% | 9.5 → 9.2 |
| /tr/quotes/conservation | 2026-11-03 | Added 2 internal links from Links to add | 3.4 → 4.1 | 1.9% → 2.8% | 5.3 → 5.0 |
| /podcast/good-citizen/karl-rove-historic-redemption-hard-work-politics-and-essential-nature | 2026-11-03 | Added 3 internal links from Links to add | 1.8 → 3.9 | 0.1% → 0.3% | 9.2 → 7.4 |
| /tr/early-life/siblings | 2026-11-03 | Added 3 internal links from Links to add | 1.2 → 1.3 | 1.2% → 0.9% | 6.3 → 5.9 |
| /tr/early-life/ten-facts | 2026-11-03 | Added 4 internal links from Links to add | 0.4 → 0.3 | 3.6% → 2.1% | 5.4 → 5.7 |
| /tr/people/kermit | 2026-11-03 | Added 4 internal links from Links to add | 0.2 → 0.5 | 0.4% → 0.4% | 8.6 → 8.7 |
| /tr/legacy | 2026-11-03 | Added 3 internal links from Links to add | 0.1 → 0.1 | 0.8% → 0.8% | 8.8 → 7.2 |
| /tr/people/bamie | 2026-11-03 | Added 3 internal links from Links to add | 0.2 → 0.5 | 0.5% → 0.6% | 6.0 → 6.9 |
| /tr/early-life | 2026-11-03 | Added 3 internal links from Links to add | 5.2 → 8.6 | 0.9% → 1.8% | 6.7 → 6.7 |
| /podcast/good-citizen/jeffrey-rosen | 2026-11-03 | Added 3 internal links from Links to add | 0.2 → 0.3 | 0.3% → 0.4% | 10.2 → 10.8 |
| /tr/complex-legacy/imperialism | 2026-11-03 | Added 2 internal links from Links to add | 8.3 → 14.2 | 1.0% → 1.0% | 5.2 → 5.1 |
| /tr/strenuous-life/hunter | 2026-11-03 | Added 3 internal links from Links to add | 1.2 → 1.5 | 0.9% → 1.2% | 5.6 → 5.2 |
| /tr/tr-shot | 2026-11-03 | Added 3 internal links from Links to add; Title 'Why Was Theodore Roosevelt Shot? The 1912 | 11.4 → 8.8 | 0.9% → 1.1% | 4.0 → 4.4 |
| /visit/itineraries/chicago-badlands | 2026-11-03 | Added 2 internal links from Links to add; Visit length and restaurant name | 0.8 → 0.5 | 1.6% → 1.2% | 6.9 → 6.7 |
| /tr/post-presidency/death | 2026-11-03 | Added 3 internal links from Links to add | 2.8 → 5.9 | 0.5% → 0.7% | 5.5 → 4.8 |
| /tr/new-york-politics/alice-lee | 2026-11-03 | Added 3 internal links from Links to add | 3.0 → 3.8 | 0.8% → 0.9% | 5.5 → 5.3 |
| /tr/square-deal | 2026-11-03 | Added 2 internal links from Links to add; Archived (node 278); 301 to /tr/presidency/squar | 31.8 → 0.1 | 0.8% → 0.9% | 3.9 → 1.8 |
| /tr/rise-to-power/edith-roosevelt | 2026-11-03 | Added 3 internal links from Links to add | 1.5 → 1.5 | 0.4% → 0.4% | 6.9 → 8.7 |
| /tr/presidency/conservation/midnight-forests | 2026-11-03 | Added 3 internal links from Links to add | 1.1 → 1.7 | 1.3% → 1.9% | 5.1 → 5.0 |
| /tr/quotes/misquotes | 2026-11-03 | Added 3 internal links from Links to add | 5.5 → 7.4 | 2.6% → 2.2% | 4.0 → 4.2 |
| /tr/post-presidency/man-in-the-arena | 2026-11-03 | Added 3 internal links from Links to add; Title 'TR's 1910 European Tour and the Man in th | 1.6 → 1.3 | 0.8% → 1.2% | 7.5 → 7.2 |
| /visit/activities | 2026-11-03 | Added 3 internal links from Links to add; Visit length and restaurant name | 0.5 → 0.5 | 0.9% → 1.6% | 5.3 → 6.9 |
| /tr/conservation/by-the-numbers | 2026-11-03 | Added 3 internal links from Links to add | 1.6 → 2.7 | 0.6% → 1.1% | 5.1 → 4.5 |
| /tr/presidency/conservation/gifford-pinchot | 2026-11-03 | Added 2 internal links from Links to add | 1.6 → 2.7 | 0.6% → 1.0% | 4.4 → 4.0 |
| /tr/early-life/family-roots | 2026-11-03 | Added 3 internal links from Links to add | 1.5 → 3.0 | 0.8% → 1.3% | 4.8 → 5.1 |
| /podcast/good-citizen/live-trpl-1-doris-kearns-goodwin-finding-hope-history | 2026-11-03 | Added 3 internal links from Links to add | 0.1 → 0.1 | 0.7% → 1.0% | 8.8 → 9.8 |
| /tr/homes-and-places/sagamore-hill | 2026-11-03 | Added 2 internal links from Links to add | 0.4 → 0.4 | 0.7% → 0.3% | 7.0 → 7.6 |
| /tr/presidency/conservation/national-monuments | 2026-11-03 | Added 3 internal links from Links to add | 0.9 → 1.4 | 0.8% → 1.1% | 5.5 → 5.3 |
| /tr/presidency/white-house-family/pets | 2026-11-03 | Added 3 internal links from Links to add | 2.2 → 3.2 | 1.2% → 1.9% | 5.1 → 4.5 |
| /visit/teddy-trail | 2026-11-03 | Added 3 internal links from Links to add | 0.3 → 0.5 | 1.2% → 1.6% | 6.4 → 9.4 |
| /visit/exhibits | 2026-11-03 | Added 3 internal links from Links to add; Title: Exhibits: Roosevelt’s Life in Eight Chapt | 3.8 → 0.5 | 0.6% → 0.2% | 3.5 → 5.4 |
| /tr/people | 2026-11-03 | Added 3 internal links from Links to add | 0.8 → 0.3 | 0.4% → 0.5% | 7.4 → 7.9 |
| /about/trustees/doris-kearns-goodwin | 2026-11-03 | Added 3 internal links from Links to add | 0.2 → 0.2 | 0.8% → 0.5% | 16.0 → 14.1 |
| /tr/people/william-howard-taft | 2026-11-03 | Added 3 internal links from Links to add | 1.8 → 4.6 | 0.3% → 0.5% | 5.7 → 5.2 |
| /about/press/press-releases/theodore-roosevelt-presidential-library-opening-celebrations-july-4-2026 | 2026-11-03 | Added 3 internal links from Links to add | 1.9 → 1.5 | 2.9% → 2.6% | 4.4 → 5.7 |
| /tr | 2026-11-03 | Added 3 internal links from Links to add | 0.3 → 0.5 | 0.1% → 0.1% | 6.9 → 5.3 |
| /tr/post-presidency | 2026-11-03 | Added 3 internal links from Links to add | 1.8 → 2.1 | 2.6% → 2.1% | 4.2 → 4.1 |
| /tr/new-york-politics/double-tragedy | 2026-11-03 | Added 3 internal links from Links to add | 0.5 → 1.6 | 1.6% → 1.9% | 4.4 → 4.7 |
| /tr/quotes/family | 2026-11-03 | Added 2 internal links from Links to add | 0.3 → 0.9 | 2.3% → 3.0% | 6.2 → 5.8 |
| /tr/people/alice-lee | 2026-11-03 | Added 3 internal links from Links to add | 0.1 → 1.1 | 0.3% → 1.6% | 8.8 → 8.4 |
| /about/press/press-releases/harold-hamm-donates-50-million-trpl | 2026-11-03 | Added 2 internal links from Links to add | 1.7 → 0.3 | 10.5% → 3.2% | 3.1 → 5.6 |
| /tr/people/theodore-sr | 2026-11-03 | Added 2 internal links from Links to add | 0.4 → 0.9 | 0.2% → 0.7% | 6.5 → 5.8 |
| /about/press/press-releases/roosevelt-family-acquires-903-acres-trpl | 2026-11-03 | Added 2 internal links from Links to add | 0.6 → 0.3 | 7.0% → 5.6% | 4.2 → 5.6 |
| /tr/legacy/mount-rushmore | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.8 | 0.2% → 0.4% | 7.1 → 6.7 |
| /tr/conservation/quotes | 2026-11-03 | Added 3 internal links from Links to add | 0.5 → 2.0 | 1.4% → 1.3% | 4.9 → 4.8 |
| /visit/itineraries/north-on-29 | 2026-11-03 | Added 2 internal links from Links to add | 0.3 → 0.2 | 0.8% → 0.7% | 7.2 → 7.5 |
| /tr/rise-to-power/police-commissioner | 2026-11-03 | Added 2 internal links from Links to add | 1.8 → 1.7 | 1.7% → 1.6% | 5.7 → 5.5 |
| /tr/legacy/words-he-coined | 2026-11-03 | Added 2 internal links from Links to add | 0.9 → 0.9 | 0.6% → 0.7% | 6.4 → 6.7 |
| /tr/myths/misquotes | 2026-11-03 | Added 2 internal links from Links to add | 1.1 → 1.9 | 1.1% → 1.6% | 5.2 → 6.3 |
| /tr/quotes | 2026-11-03 | Added 2 internal links from Links to add | 21.7 → 17.1 | 2.3% → 2.4% | 10.7 → 3.8 |
| /tr/presidency/first-term | 2026-11-03 | Added 2 internal links from Links to add | 0.5 → 1.1 | 1.7% → 2.2% | 6.5 → 5.6 |
| /visit/itineraries/13-day-denver-wyoming | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.8% → 0.0% | 8.9 → 8.6 |
| /tr/family/children | 2026-11-03 | Added 2 internal links from Links to add; Title 'Theodore Roosevelt's Children: Alice, Ted | 4.2 → 7.5 | 1.1% → 1.7% | 4.2 → 3.6 |
| /visit/shopping | 2026-11-03 | Added 2 internal links from Links to add | 5.0 → 4.3 | 2.2% → 3.8% | 5.0 → 7.9 |
| /tr/family | 2026-11-03 | Added 2 internal links from Links to add | 1.1 → 1.6 | 0.4% → 0.3% | 8.0 → 8.0 |
| /tr/for-educators/middle-school | 2026-11-03 | Added 2 internal links from Links to add | 0.6 → 1.3 | 2.2% → 3.3% | 6.5 → 6.3 |
| /visit/medora | 2026-11-03 | Added 1 internal link from Links to add | 1.1 → 0.3 | 0.7% → 0.3% | 4.5 → 4.9 |
| /tr/rise-to-power/buffalo-soldiers | 2026-11-03 | Added 1 internal link from Links to add | 1.6 → 1.5 | 0.7% → 0.6% | 5.2 → 5.0 |
| /tr/early-life/harvard | 2026-11-03 | Added 2 internal links from Links to add | 0.9 → 2.5 | 1.0% → 1.8% | 5.4 → 5.2 |
| /tr/elkhorn | 2026-11-03 | Added 2 internal links from Links to add | 1.6 → 1.7 | 0.8% → 1.0% | 8.0 → 7.9 |
| /podcast/good-citizen/ted-leonsis | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.1 | 0.2% → 0.1% | 10.0 → 8.8 |
| /tr/presidency/conservation/national-parks | 2026-11-03 | Added 2 internal links from Links to add | 6.9 → 7.9 | 0.9% → 1.2% | 6.0 → 5.3 |
| /bullet-speech | 2026-11-03 | Added 1 internal link from Links to add; Title 'The Bullet Speech: Roosevelt's Assassinati | 24.4 → 22.5 | 1.7% → 1.5% | 3.7 → 3.6 |
| /tr/early-life/mother | 2026-11-03 | Added 2 internal links from Links to add | 0.3 → 0.3 | 0.3% → 0.4% | 5.1 → 4.5 |
| /tr/post-presidency/river-of-doubt | 2026-11-03 | Added 2 internal links from Links to add | 2.6 → 4.8 | 0.6% → 0.8% | 7.5 → 7.6 |
| /tr/post-presidency/african-safari | 2026-11-03 | Added 2 internal links from Links to add | 1.2 → 1.1 | 1.3% → 1.4% | 5.9 → 6.0 |
| /tr/post-presidency/new-nationalism | 2026-11-03 | Added 2 internal links from Links to add | 1.8 → 2.1 | 0.7% → 0.8% | 4.5 → 4.6 |
| /tr/presidency/conservation/reclamation | 2026-11-03 | Added 2 internal links from Links to add | 3.3 → 2.8 | 0.8% → 0.9% | 4.2 → 3.6 |
| /tr/5-big-adventures | 2026-11-03 | Added 2 internal links from Links to add | 2.0 → 1.5 | 1.0% → 0.7% | 6.5 → 5.9 |
| /tr/rise-to-power/san-juan-hill | 2026-11-03 | Added 2 internal links from Links to add; Title uses 'Battle of San Juan Hill' | 14.8 → 13.6 | 1.4% → 1.1% | 3.7 → 3.6 |
| /tr/presidency/conservation/bird-reserves | 2026-11-03 | Added 2 internal links from Links to add | 0.8 → 0.7 | 1.5% → 0.9% | 5.4 → 4.5 |
| /podcast/good-citizen/douglas-brinkley | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.1 | 0.1% → 0.2% | 11.9 → 13.5 |
| /tr/people/corinne | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.3 | 0.2% → 0.6% | 4.3 → 3.0 |
| /podcast/good-citizen/eric-liu | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.3 | 0.3% → 1.4% | 7.8 → 6.2 |
| /tr/quotes/strenuous-life | 2026-11-03 | Added 1 internal link from Links to add | 1.8 → 2.6 | 1.3% → 1.3% | 6.3 → 6.4 |
| /tr/quotes/citizenship | 2026-11-03 | Added 2 internal links from Links to add | 1.9 → 2.3 | 1.7% → 1.8% | 5.8 → 5.8 |
| /tr/elkhorn-timeline | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.0 | 1.3% → 0.0% | 8.1 → 6.9 |
| /tr/people/edith-roosevelt | 2026-11-03 | Added 2 internal links from Links to add | 0.4 → 0.1 | 0.7% → 0.2% | 11.3 → 12.0 |
| /visit/roosevelt-in-medora | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.8% → 0.0% | 7.4 → 11.2 |
| /podcast/good-citizen/meg-whitman | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.3 | 0.1% → 0.2% | 11.4 → 11.2 |
| /tr/speeches/strenuous-life | 2026-11-03 | Added 1 internal link from Links to add | 2.7 → 2.3 | 1.9% → 2.3% | 5.7 → 5.4 |
| /tr/people/quentin | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.4 | 0.4% → 0.8% | 8.5 → 8.5 |
| /tr/post-presidency/world-war-i | 2026-11-03 | Added 2 internal links from Links to add | 0.2 → 1.1 | 0.5% → 1.2% | 5.4 → 5.4 |
| /tr/rise-to-power/sagamore-hill | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.3 | 0.9% → 0.1% | 6.9 → 8.7 |
| /tr/new-york-politics/convention-1884 | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.6 | 0.9% → 1.6% | 6.7 → 7.1 |
| /about/press/press-releases/sarah-and-ross-perot-jr-foundation-gifts-5-million-theodore-roosevelt | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.1 | 0.9% → 3.2% | 6.4 → 8.7 |
| /about/press/press-releases/theodore-roosevelt-presidential-library-welcomes-doris-kearns-goodwin | 2026-11-03 | Added 2 internal links from Links to add | 0.0 → 0.0 | 0.7% → 0.0% | 5.3 → 9.8 |
| /about/foundation | 2026-11-03 | Added 1 internal link from Links to add | 2.5 → 2.0 | 3.7% → 3.8% | 5.5 → 6.0 |
| /visit/eat | 2026-11-03 | Added 2 internal links from Links to add | 5.8 → 1.9 | 2.7% → 1.7% | 7.2 → 7.6 |
| /visit/maps | 2026-11-03 | Added 1 internal link from Links to add | 1.7 → 0.4 | 0.5% → 1.3% | 3.9 → 3.6 |
| /tr/post-presidency/assassination-attempt | 2026-11-03 | Added 2 internal links from Links to add | 0.8 → 1.4 | 0.6% → 0.9% | 8.0 → 6.8 |
| /research | 2026-11-03 | Added 2 internal links from Links to add | 1.1 → 0.9 | 3.4% → 3.6% | 5.5 → 5.6 |
| /tr/presidency/white-house-family/white-house-gang | 2026-11-03 | Added 2 internal links from Links to add | 0.0 → 0.2 | 1.9% → 3.1% | 6.0 → 4.9 |
| /tr/presidency/conservation/governors-conference | 2026-11-03 | Added 2 internal links from Links to add | 0.3 → 0.6 | 3.4% → 6.7% | 4.8 → 4.0 |
| /tr/rise-to-power/jacob-riis | 2026-11-03 | Added 1 internal link from Links to add | 1.7 → 3.7 | 0.6% → 1.1% | 4.9 → 4.7 |
| /tr/strenuous-life/explorer | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.1 | 1.1% → 0.3% | 5.0 → 5.1 |
| /tr/presidency/race | 2026-11-03 | Added 2 internal links from Links to add | 3.8 → 4.5 | 1.2% → 1.5% | 4.4 → 3.7 |
| /visit/itineraries | 2026-11-03 | Added 1 internal link from Links to add; Link to the I-94 guide | 2.7 → 1.8 | 1.6% → 1.2% | 6.5 → 7.0 |
| /tr/presidency/executive-power | 2026-11-03 | Added 2 internal links from Links to add | 2.9 → 11.1 | 1.5% → 1.8% | 4.1 → 4.0 |
| /tr/presidency/conservation/national-forests | 2026-11-03 | Added 2 internal links from Links to add | 0.5 → 0.5 | 0.8% → 0.4% | 6.0 → 5.8 |
| /visit/itineraries/black-hills-loop | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.3 | 1.0% → 1.1% | 8.3 → 8.0 |
| /visit/itineraries/7-day-billings-bismarck | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.1 | 0.5% → 0.2% | 8.6 → 8.4 |
| /tr/10-myths-teddy-bear | 2026-11-03 | Added 1 internal link from Links to add | 5.2 → 4.8 | 0.8% → 0.9% | 5.5 → 6.5 |
| /tr/post-presidency/bull-moose/platform | 2026-11-03 | Added 1 internal link from Links to add | 8.6 → 9.3 | 0.7% → 0.5% | 5.0 → 4.2 |
| /tr/for-educators/elementary | 2026-11-03 | Added 1 internal link from Links to add | 1.2 → 1.1 | 2.5% → 2.4% | 6.2 → 6.0 |
| /tr/people/alice-longworth | 2026-11-03 | Added 1 internal link from Links to add; Title 'Alice Roosevelt Longworth: Theodore Roosev | 3.7 → 5.5 | 0.4% → 0.5% | 8.0 → 6.7 |
| /tr/tr-save-the-bison | 2026-11-03 | Added 1 internal link from Links to add | 2.1 → 2.5 | 1.5% → 1.7% | 5.1 → 5.2 |
| /tr/presidency/trust-busting | 2026-11-03 | Added 1 internal link from Links to add; Title 'What Was Trust-Busting? Roosevelt Takes On | 36.2 → 43.9 | 1.3% → 1.6% | 3.4 → 3.2 |
| /tr/complex-legacy | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.4 | 1.7% → 1.0% | 6.0 → 5.2 |
| /podcast/good-citizen/susan-berfield | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.1 | 0.5% → 0.3% | 5.6 → 5.7 |
| /tr/badlands/bad-lands-cow-boy | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.1 | 0.3% → 0.3% | 8.6 → 6.8 |
| /tr/presidency/great-white-fleet | 2026-11-03 | Added 1 internal link from Links to add; Title 'The Great White Fleet: Roosevelt's Global  | 6.6 → 11.4 | 0.7% → 1.1% | 4.1 → 3.3 |
| /tr/badlands/ten-facts | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.9 | 1.1% → 1.6% | 5.1 → 4.8 |
| /podcast/good-citizen/susannah-cahalan | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.5 | 0.2% → 0.3% | 9.2 → 9.9 |
| /tr/presidency/bully-pulpit | 2026-11-03 | Added 1 internal link from Links to add; Title 'The Bully Pulpit: Meaning, Origin, and Exa | 5.7 → 13.3 | 0.6% → 0.6% | 4.6 → 3.4 |
| /tr/speeches/man-in-the-arena | 2026-11-03 | Added 1 internal link from Links to add; Title 'Man in the Arena Speech: Citizenship in a  | 25.7 → 62.5 | 2.3% → 3.1% | 5.2 → 5.6 |
| /tr/complex-legacy/eugenics | 2026-11-03 | Added 1 internal link from Links to add | 3.5 → 3.9 | 2.9% → 3.0% | 4.2 → 4.0 |
| /tr/people/jacob-riis | 2026-11-03 | Added 1 internal link from Links to add; Title and description aimed at 'who was Jacob Rii | 16.4 → 23.9 | 0.5% → 0.9% | 6.6 → 5.9 |
| /tr/badlands/maltese-cross | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.0 | 3.1% → 0.0% | 6.5 → 6.6 |
| /tr/people/elliott | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.2 | 0.0% → 1.0% | 9.4 → 9.9 |
| /tr/rise-to-power/vice-presidency | 2026-11-03 | Added 1 internal link from Links to add | 1.9 → 2.7 | 0.7% → 0.8% | 5.4 → 4.8 |
| /tr/family/elliott-roosevelt | 2026-11-03 | Added 1 internal link from Links to add | 1.1 → 1.9 | 0.5% → 0.8% | 7.5 → 7.3 |
| /tr/badlands | 2026-11-03 | Added 1 internal link from Links to add; Link to where-to-see | 0.1 → 0.1 | 1.1% → 1.3% | 5.3 → 7.9 |
| /podcast/good-citizen/carly-fiorina | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.4% → 0.0% | 8.7 → 10.6 |
| /tr/badlands/medora | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.1 | 0.4% → 0.2% | 7.8 → 8.8 |
| /virtual | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 5.1% → 0.0% | 6.3 → 9.6 |
| /tr/books-and-writings/reader | 2026-11-03 | Added 1 internal link from Links to add | 1.2 → 1.0 | 1.9% → 1.8% | 5.2 → 5.0 |
| /tr/complex-legacy/race | 2026-11-03 | Added 1 internal link from Links to add | 0.9 → 2.0 | 0.9% → 0.8% | 4.9 → 4.4 |
| /tr/people/john-muir | 2026-11-03 | Added 1 internal link from Links to add | 1.0 → 1.1 | 0.5% → 0.6% | 7.2 → 6.6 |
| /tr/complex-legacy/equestrian-statue | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.4 | 1.5% → 0.7% | 5.5 → 5.6 |
| /tr/people/ethel | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.5 | 0.3% → 0.6% | 7.8 → 7.0 |
| /tr/rise-to-power/becoming-president | 2026-11-03 | Added 1 internal link from Links to add | 1.4 → 2.9 | 0.3% → 0.6% | 5.3 → 4.7 |
| /tr/people/ted-jr | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.6 | 0.1% → 0.1% | 10.2 → 9.9 |
| /tr/people/mittie | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.5 | 0.6% → 0.6% | 7.5 → 6.8 |
| /podcast/good-citizen/katherine-gehl | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.3 | 1.1% → 2.0% | 8.2 → 8.7 |
| /visit/itineraries/7-day-bismarck-rapid-city | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.4 | 0.4% → 0.5% | 8.1 → 8.3 |
| /tr/early-life/childhood-illness | 2026-11-03 | Added 1 internal link from Links to add | 2.3 → 4.1 | 1.8% → 2.2% | 4.0 → 3.5 |
| /tr/presidency/square-deal | 2026-11-03 | Added 1 internal link from Links to add; Truncated description fixed; Three Cs heading; Sp | 20.7 → 62.5 | 0.6% → 1.4% | 4.4 → 3.0 |
| /tr/presidency/conservation/john-muir | 2026-11-03 | Added 1 internal link from Links to add | 3.2 → 4.5 | 1.1% → 1.5% | 4.5 → 4.0 |
| /tr/myths | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.4 | 0.5% → 4.8% | 8.0 → 7.1 |
| /tr/early-life/young-naturalist | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.3 | 0.9% → 1.7% | 4.9 → 5.2 |
| /tr/presidency/cabinet | 2026-11-03 | Added 1 internal link from Links to add | 1.0 → 2.2 | 1.1% → 1.6% | 5.0 → 5.3 |
| /tr/people/booker-t-washington | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 2.0 | 0.2% → 0.3% | 9.4 → 8.1 |
| /project/design | 2026-11-03 | Added 1 internal link from Links to add | 5.5 → 2.9 | 3.7% → 2.4% | 4.5 → 5.1 |
| /tr/early-life/family-travels | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.3 | 1.4% → 1.2% | 5.2 → 5.5 |
| /podcast/good-citizen/adam-met-climate-action-musical-stardom-and-art-building-movement | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 11.5 → 11.8 |
| /tr/conservation | 2026-11-03 | Added 1 internal link from Links to add | 1.1 → 1.3 | 1.0% → 1.3% | 7.2 → 7.4 |
| /tr/speeches/confession-of-faith | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 1.6 | 1.1% → 2.1% | 7.0 → 8.0 |
| /podcast/good-citizen/senator-mitt-romney-formative-moments-presidential-leadership-and-question | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.1 | 0.1% → 0.2% | 7.7 → 7.7 |
| /tr/homes-and-places | 2026-11-03 | Added 1 internal link from Links to add | 1.2 → 1.3 | 1.1% → 1.3% | 5.9 → 5.4 |
| /tr/early-life/civil-war | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.5 | 0.6% → 1.0% | 5.1 → 4.2 |
| /tr/early-life/day-in-the-life | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.1 | 0.6% → 0.6% | 6.9 → 8.2 |
| /visit/national-park | 2026-11-03 | Added 1 internal link from Links to add; Visit length, restaurant name; link to where-to-s | 4.4 → 2.8 | 0.6% → 0.5% | 8.1 → 8.7 |
| /tr/people/gifford-pinchot | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.6 | 0.9% → 0.7% | 6.3 → 5.9 |
| /tr/post-presidency/bull-moose | 2026-11-03 | Added 1 internal link from Links to add | 5.6 → 6.4 | 0.6% → 0.5% | 4.6 → 4.5 |
| /visit/hiking | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.1 | 0.7% → 0.3% | 7.1 → 7.5 |
| /beam-signing-ceremony | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.1 | 0.0% → 2.2% | 7.9 → 5.1 |
| /project/native-plant-project | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.6 | 0.9% → 3.4% | 4.6 → 6.8 |
| /tr/homes-and-places/tr-national-park | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 1.0 | 0.7% → 1.0% | 7.1 → 8.3 |
| /visit/hunting-fishing | 2026-11-03 | Added 1 internal link from Links to add | 0.8 → 1.4 | 1.1% → 1.9% | 7.3 → 6.8 |
| /about/mission | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.1 | 2.3% → 0.7% | 4.7 → 2.7 |
| /tr/rise-to-power/civil-service | 2026-11-03 | Added 1 internal link from Links to add | 2.1 → 1.6 | 0.6% → 0.3% | 5.3 → 5.4 |
| /tr/badlands/elkhorn-ranch | 2026-11-03 | Added 1 internal link from Links to add | 0.6 → 0.9 | 0.8% → 0.9% | 7.6 → 6.9 |
| /visit/stargazing | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.3 | 1.3% → 1.1% | 6.2 → 6.1 |
| /podcast/good-citizen/dr-vivek-murthy-loneliness-staying-human-and-what-true-success-looks | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.2 | 1.0% → 1.9% | 10.4 → 19.0 |
| /podcast/good-citizen/secretary-deb-haaland | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 2.1 | 0.9% → 1.3% | 7.5 → 7.3 |
| /visit/itineraries/river-road | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.1 | 0.7% → 1.1% | 7.3 → 6.9 |
| /tr/presidency/white-house-workers | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.6 | 1.4% → 0.9% | 6.5 → 7.3 |
| /podcast/good-citizen/matthew-barzun | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.9% → 0.0% | 8.5 → 8.7 |
| /tr/early-life/father | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.5 | 0.5% → 0.4% | 6.7 → 7.6 |
| /visit/camping | 2026-11-03 | Added 1 internal link from Links to add | 0.8 → 0.5 | 1.4% → 0.8% | 7.5 → 7.2 |
| /tr/presidency/conservation/antiquities-act | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 1.1 | 0.9% → 0.6% | 6.1 → 5.9 |
| /visit/trolley | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.1 | 1.6% → 0.8% | 6.9 → 7.8 |
| /tr/badlands/landscape | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.7 | 0.6% → 1.1% | 5.9 → 6.1 |
| /visit/little-missouri-river | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.3 | 1.1% → 0.8% | 7.8 → 6.5 |
| /podcast/good-citizen/ben-jealous | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 10.2 → 11.6 |
| /podcast/good-citizen/dan-harris | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 8.8 → 8.2 |
| /visit/outdoors | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.4 | 1.4% → 2.9% | 6.6 → 5.8 |
| /visit/biking | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.1 | 2.1% → 0.9% | 7.3 → 9.0 |
| /visit/wildlife | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.3 | 0.6% → 1.0% | 7.8 → 7.8 |
| /project | 2026-11-03 | Added 1 internal link from Links to add; Title 'Building the Library: Design, Values and S | 5.0 → 1.7 | 0.5% → 0.2% | 2.4 → 2.5 |
| /tr/people/leonard-wood | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.9 | 0.2% → 0.5% | 8.8 → 6.5 |
| /podcast/good-citizen/katharine-hayhoe | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.1 | 0.0% → 1.3% | 8.5 → 7.6 |
| /visit/itineraries/weekend-drives/fargo | 2026-11-03 | Added 1 internal link from Links to add | 0.6 → 0.3 | 1.1% → 0.9% | 5.0 → 5.5 |
| /about/press/press-releases/trplf-elects-spencer-zwick-board | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 1.6% → 0.0% | 4.3 → 3.9 |
| /visit/itineraries/weekend-drives/bismarck | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.7 | 1.0% → 2.0% | 5.1 → 4.4 |
| /tr/presidency/second-term | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.6 | 1.8% → 2.0% | 6.0 → 4.4 |
| /tr/books-and-writings | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.4 | 0.8% → 1.6% | 8.7 → 9.1 |
| /tr/badlands/frontier-life | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.2 | 0.8% → 0.7% | 6.5 → 6.1 |
| /about/trustees/beth-laski | 2026-11-03 | Added 1 internal link from Links to add | 0.8 → 0.3 | 8.2% → 4.1% | 9.8 → 9.2 |
| /about/press/press-releases/theodore-roosevelt-presidential-library-launches-good-citizen-podcast | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 5.9 → 6.0 |
| /about/presidential-library-system | 2026-11-03 | Added 1 internal link from Links to add | 0.6 → 0.4 | 2.3% → 1.1% | 6.2 → 6.6 |
| /about/press/press-releases/trplf-announces-100-million-commitments-unlocks-50-million-state | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 2.8% → 0.0% | 4.9 → 3.4 |
| /tr/new-york-politics | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.1 | 0.9% → 0.6% | 7.0 → 6.9 |
| /tr/tr-importance | 2026-11-03 | Title 'What Was Theodore Roosevelt Known For?'; typo fix | 12.9 → 16.1 | 1.0% → 1.0% | 4.9 → 4.8 |
| /visit | 2026-10-27 | Title: Plan Your Visit: Tickets, Hours and Directions; Visit length: about three and a hal | 57.3 → 28.3 | 2.5% → 1.9% | 2.7 → 2.9 |
| /tr/presidency/panama-canal | 2026-10-27 | Title and description: Theodore Roosevelt and the Panama Canal, 1903–1914 | 8.2 → 18.4 | 0.4% → 0.7% | 5.2 → 4.7 |
| /tr/presidency/railroad-regulation | 2026-10-27 | Title names the Hepburn Act and Elkins Act | 3.9 → 5.5 | 0.4% → 0.7% | 4.0 → 3.6 |
| /tr/presidency/coal-strike | 2026-10-27 | Title uses 'Anthracite Coal Strike of 1902' | 7.9 → 9.1 | 0.9% → 1.1% | 4.2 → 3.0 |
| /visit/groups | 2026-10-27 | Visit length changed from about three hours to about three and a half hours | 0.1 → 0.0 | 0.6% → 1.2% | 6.5 → 6.5 |
| /visit/faq/tickets | 2026-10-27 | 'Buy tickets' link fixed (was /visit/tickets, a 404); 301 /visit/tickets -> /tickets | 2.0 → 0.9 | 4.3% → 2.8% | 6.3 → 4.8 |
| /visit/faq | 2026-10-27 | Tickets link fixed (was /visit/tickets, a 404) | 2.1 → 0.5 | 0.8% → 1.6% | 4.7 → 7.1 |

## Drafted recommendations (Gemini (gemini-3.8-flash), 2026-11-16T13:15:58+00:00)
_1 AI claims were dropped because the live page contradicted them._

**AI visibility:** ChatGPT consistently points travelers to the Library for Medora trips, while Gemini largely skips it outside direct name searches.
- Add an I-94 corridor guide showing driving times from Bismarck and Glendive, Medora access, and how to fit a 3 1/2 hour stop into a cross-state drive. (medium effort; trlibrary.com/visit/itineraries/i-94-road-trip): Both engines completely overlook the Library on I-94 queries, relying on Painted Canyon and state tourism listings instead.
- Clarify time recommendations on the visitor FAQ page to state clearly that a full visit takes about 3 1/2 hours. (low effort; trlibrary.com/visit/faq/during-your-visit): ChatGPT currently cites 2 to 4 hours on indoor activity answers, which shortchanges the trail walks and exhibit galleries.
- Request updated attraction profiles on North Dakota Tourism and local partner portals to categorize the site as a premier state museum and indoor destination. (medium effort; ndtourism.com and discovermedora.com partner listings): Gemini pulls museum and rainy day results heavily from ndtourism.com, medora.com, and medorand.org rather than the main site.

**/tickets**: The tickets page covers pricing and tours but misses crucial planning details like the 3 1/2-hour visit duration, leaving visitors and search engines unclear on how to schedule timed-entry slots.
- Title: Tickets & Admission: Timed Entry, Passes & Tours
- Meta: Book timed-entry tickets to the Theodore Roosevelt Presidential Library in Medora. Check admission prices, reserve specialty tours, and plan your visit.
- Verify: Confirm that admission allows same-day re-entry if visitors leave to hike or dine before returning to indoor galleries.

**/tr/presidency/nobel-peace-prize**: Directly answer the high-volume query 'why did Theodore Roosevelt win the Nobel Peace Prize' near the top of the page and clarify his historic status as the first American Nobel laureate.
- Title: Theodore Roosevelt's Nobel Peace Prize
- Meta: Why did Theodore Roosevelt win the Nobel Peace Prize? Discover how his mediation ended the Russo-Japanese War and made him the first American laureate.
- Verify: Confirm whether 'Teddy' is acceptable to use sparingly in informational copy to capture user search variants according to communications team guidelines.

**/tr/presidency/foreign-policy**: Tighten the over-length title and truncated meta description to target high-intent search queries, and add structured answer summaries for common questions about Roosevelt's actions in Latin America and Asia.
- Title: Theodore Roosevelt Foreign Policy: The Big Stick Era
- Meta: See how Theodore Roosevelt built a global power through Big Stick diplomacy, naval might, and peacemaking. Explore key events and his lasting world impact.
- Verify: Verify whether the Dominican Republic intervention is explicitly referenced elsewhere on trlibrary.com before including it in the summary draft.; Confirm that the 'Man in the Arena' quote under the Roosevelt Corollary heading was placed by editorial error and can be relocated.

**/tr/rise-to-power/rough-riders**: The page ranks on page one for major definitional searches like 'who were the rough riders' and 'what did the rough riders do' but lacks a crisp summary definition at the very top, while accidentally repeating two entire sections on training and the voyage to Cuba.
- Title: Who Were the Rough Riders? TR's 1st Volunteer Cavalry
- Meta: Who were the Rough Riders? Discover how Theodore Roosevelt led cowboys and Ivy Leaguers from training in Texas to the charge up Kettle Hill in Cuba.
- Verify: Verify that all names, dates, and troop designations in the added summary (1st U.S. Volunteer Cavalry, 1898, Spanish-American War, Camp Wood, Las Guasimas, Kettle Hill, 10th Cavalry, Santiago, Montauk Point) match approved historical records.

**/programs**: Expand the thin, under-150-word text with clear descriptions of in-person Medora events and digital resources, helping travelers planning Badlands visits and educators find useful programming.
- Title: Programs, Events & Educational Resources
- Meta: Explore educational programs, podcasts, films, and live events in Medora and online. Find classroom tools, upcoming talks, and Badlands gatherings.
- Verify: Confirm whether educational materials and quizzes are available on site in Medora or solely online.; Check whether live talks and screenings run year-round or operate on a seasonal schedule.

**/tr/presidency/conservation**: Capitalize on the page's top search query ('what did roosevelt do which had never been done before in conservation') by grouping his historic conservation firsts into an explicit, scannable section.
- Title: Theodore Roosevelt Conservation: Parks, Forests, Legacy
- Meta: Explore how Theodore Roosevelt protected roughly 230 million acres, founded the Forest Service, and created the first bird reserves. See the full record.
- Verify: Confirm whether Pelican Island is formally recognized as the country's first federal bird reservation or if existing text ('beginning with Pelican Island (1903)') should remain the exact phrasing.

**/tr/presidency/booker-t-washington**: Shorten the title to eliminate SERP truncation and add concise summary callouts answering why the 1901 dinner occurred to win featured snippets and AI answers for high-volume historical queries.
- Title: Booker T. Washington's White House Dinner
- Meta: Discover why Theodore Roosevelt invited Booker T. Washington to the White House in October 1901, the fierce backlash that followed, and what it meant.
- Verify: Confirm whether any planned future physical exhibits at the Medora Library address the 1901 dinner before linking this article to on-site visitor experiences.

**/tr/strenuous-life/athletics**: Optimize title and metadata around high-volume queries like 'theodore roosevelt boxing' and fitness, and address popular search topics such as wrestling and his Harvard athletics directly in subheadings.
- Title: Theodore Roosevelt Boxing, Fitness & Athletics
- Meta: From childhood asthma to White House boxing and jiu-jitsu, discover how Theodore Roosevelt built his iron constitution through relentless physical training.
- Verify: Verify the historical details and frequency of Roosevelt's wrestling practice during and before his presidency to ensure accurate framing in the wrestling text addition.; Verify Roosevelt's specific sports and gym routine while a student at Harvard College.

## Visitor experience (/visit pages)
Findability 47/100, mobile speed 53/100, accessibility 96/100, average reading grade 8.3, 0 facts that disagree between pages.

### Can a first-time visitor find what they need?
| Page | Score | Missing or buried | Biggest fix |
|---|---|---|---|
| /visit | 82 | directions, food | Add clear parking instructions alongside the driving directions, and move essential practical details like dining and accessibility higher on the page. |
| /visit/accessibility | 29 | hours, price, buy, visit_length, food | Add the recommended 3 1/2 hour visit length so guests with mobility, stamina, or sensory considerations can effectively plan their day. |
| /visit/directions | 61 | visit_length, accessibility, food | State in the drive-time and road-trip planner sections that visitors should budget about 3 1/2 hours for the Library itself so drivers can plan their stops accurately. |
| /visit/eat | 14 | hours, price, buy, directions, visit_length, accessibility | Add quick-jump navigation or category filters near the top of the downtown dining list so mobile visitors can quickly find meals without scrolling past twelve separate venues. |
| /visit/faq | 75 |  | Add direct, expandable answers or quick-reference callouts for top visitor questions like hours, location, and the 3 1/2 hour visit length so mobile readers do not have to click through multiple subpages. |
| /visit/faq/tickets | 44 | hours, visit_length | Add ticket prices directly to the page so visitors can see admission costs before clicking into the checkout system. |
| /visit/groups | 29 | hours, price, directions, accessibility, food | Add base ticket prices and bus drop-off or parking details so group organizers can build an accurate budget and itinerary. |
| /visit/hours | 68 | visit_length, accessibility | Move the three-and-a-half-hour visit recommendation and the 90-minute last-entry cutoff up to the top of the page so guests know when to arrive before scrolling seasonal tables. |
| /visit/lodging | 58 | directions, food | Add quick-jump anchor links at the top for Hotels, Cabins, Campgrounds, and Dickinson so mobile visitors can jump straight to their preferred stay without endless scrolling. |
| /visit/maps | 43 | visit_length, accessibility, food | Add a quick-reference campus key beside the map that notes parking locations, accessible paths, and the recommended 3 1/2 hour visit time. |
| /visit/tickets/plan-ahead | 14 | hours, price, directions, visit_length, accessibility, food | Add essential visit basics—including operating hours, ticket prices, and the recommended 3 1/2-hour visit length—directly above the reservation tool. |

### Slowest pages on mobile
| Page | Speed /100 | Load (s) |
|---|---|---|
| /visit/itineraries/one-day | 22 | 5.4 |
| /visit/itineraries/roosevelt-triangle | 27 | 17.2 |
| /visit/national-park | 27 | 13.8 |
| /visit/roosevelt-in-medora | 27 | 13.3 |
| /visit/itineraries/10-day-denver-salt-lake-city | 28 | 11 |
| /visit/itineraries/13-day-denver-wyoming | 28 | 7 |
| /visit/directions | 29 | 6.2 |
| /visit/stargazing | 29 | 13.3 |

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
1 broken internal addresses (2 links), 658 links worth adding, 45 pages with no links in, 20 topics with two pages, 38 broken outside links (LinkChecker scan 2026-11-16 04:28 UTC).

### Broken links on trlibrary.com: 301 redirects to add
Add a 301 redirect in Drupal (Configuration > Search and metadata > URL redirects) from each broken address to redirect_to; bulk import: https://seo.labs.trlibrary.com/data/redirects.csv. High confidence = safe; check medium/low first. Ticket-store paths should also be corrected on the page to the full access.trlibrary.com address.

| Broken | Status | Redirect to | Confidence | Links | Why |
|---|---|---|---|---|---|
| /about/trustees/edward-okeefe | 404 | /podcast/good-citizen/edward-okeefe | high | 2 | live page with the same name |

### Links to add (highest value first; the [[bracketed]] words become the link)
| On page | Context | Link to |
|---|---|---|
| /tr/legacy/rankings | Roosevelt’s enduring popularity is carved in granite at [[Mount Rushmore]], beside Washington, Jefferson, and Lincoln. (National Park Service) | /tr/tr-mount-rushmore |
| /tr/timeline | …velt had declared he would not run again, promoting the presidency of his cabinet member, [[William Howard Taft]] during the 1908 election. When Roosevelt returned home from his African safari in 1910, h… | /tr/people/william-howard-taft |
| /tr/tr-mount-rushmore | Learn more about Theodore Roosevelt and his concept of [[executive power]] with this Inquiry Design Model (IDM) lesson plan. | /tr/presidency/executive-power |
| /tr/timeline | …r, a Brazilian military officer suggested descending an unknown river: Rio da Dúvida, the [[River of Doubt]]. Together Roosevelt, his Brazilian counterpart expedition leader, Cândido Mariano da Silv… | /tr/post-presidency/river-of-doubt |
| /tr/presidency-timeline | …ssia and Japan, the Russo-Japanese War ended in September 1905. Roosevelt was awarded the [[Nobel Peace Prize]] for his successful negotiations. He was not able to accept the prize in person. Instead, … | /tr/presidency/nobel-peace-prize |
| /tr/teddy-nickname | How much do you know about [[Theodore Roosevelt's early life]]? | /tr/early-life |
| /tr/timeline | Theodore and [[Edith Roosevelt]]’s first child, Theodore Jr. “Ted,” was born at the family home at Sagamore Hill in Oyster… | /tr/rise-to-power/edith-roosevelt |
| /tr/timeline | … 1905. Just over a year later, 48-year-old Roosevelt became the first American to win the [[Nobel Peace Prize]], announced on December 10, 1906. Roosevelt was not able to collect the prize himself and … | /tr/presidency/nobel-peace-prize |
| /tr/timeline | …tille Day—July 14, 1918—near Chamery, France. For several days after Quentin’s death, the [[Roosevelt family]] only knew that he had been reported missing. After learning of his death, 59-year-old The… | /tr/family |
| /tr/people/henry-cabot-lodge | …osevelt, deserved party loyalty. Lodge also believed that some of Roosevelt's ideas about [[executive power]] and Progressive reform were too radical for his tastes. Yet Lodge also remained personall… | /tr/presidency/executive-power |
| /tr/timeline | … Service under the Department of Agriculture. Theodore Roosevelt, then 46 years old, made [[Gifford Pinchot]] the first US Chief Forester. Throughout his presidency, Roosevelt was dedicated to the he… | /tr/presidency/conservation/gifford-pinchot |
| /tr/fake-quotes | Learn more about Theodore Roosevelt and his concept of [[executive power]] with this Inquiry Design Model (IDM) lesson plan. | /tr/presidency/executive-power |
| /tr/presidency/foreign-policy | …ility to intervene in world affairs became mainstream American thinking. The assertion of [[executive power]] in foreign policy—the president's ability to act boldly without waiting for Congressional… | /tr/presidency/executive-power |
| /tr/homes-and-places/white-house | Decorations for [[Alice Roosevelt]]'s White House wedding, February 1906. (Frances Benjamin Johnston / Library of Congress) | /tr/people/alice-longworth |
| /visit/exhibits/main | …eded reviving: he went looking for the wildest thing he could find. What he found was the [[River of Doubt]] — an uncharted Amazon tributary so unknown that no map could tell him where it went or wh… | /tr/post-presidency/river-of-doubt |
| /teach-tr | Learn about the [[Panama Canal]] and Theodore Roosevelt’s connection to the canal with this resource packet containing 13 … | /tr/presidency/panama-canal |
| /tr/timeline | … of four children, Theodore Roosevelt was born at 28 East 20th Street in New York City to [[Theodore Sr]]. “Thee” and Martha “Mittie” Bulloch Roosevelt. Born into a wealthy family, Roosevelt grew… | /tr/people/theodore-sr |
| /tr/presidency | [[Booker T. Washington]], October 1901 | /tr/people/booker-t-washington |
| /tr/rise-to-power/vice-presidency | The MacNaughton Cottage at Tahawus, where the [[Roosevelt family]] vacationed in the Adirondacks in the summer of 1901. (Harvard College Library) | /tr/family |
| /visit/exhibits/main | …12 — a work so rigorous the Navy would later place a copy on every ship. He fell hard for [[Alice Hathaway Lee]], courting her with headlong devotion until she agreed to marry him on his twenty-second b… | /tr/new-york-politics/alice-lee |
| /tr/teddy-nickname | …repressible small boy to his face as Mr. Roosevelt emerged from the Yosemite [hiking with [[John Muir]]]. This hail is said to have met with a prompt Presidential veto.” | /tr/people/john-muir |
| /visit/exhibits/main | … from them. On race, Roosevelt was, in his own era and ours, a divided figure. He invited [[Booker T. Washington]] to dine at the White House and stood by Minnie Cox, the first Black postmaster in Mississ… | /tr/people/booker-t-washington |
| /tr/presidency/ten-facts | Roosevelt protected some 230 million acres of public land; here he stands with naturalist [[John Muir]] at Glacier Point in Yosemite, 1903. (Library of Congress) | /tr/people/john-muir |
| /visit/exhibits/main | At the center of it is [[Edith Roosevelt]] , whose steady hand shaped both the house and the role. She led a major renovation that g… | /tr/rise-to-power/edith-roosevelt |
| /tr/timeline | …sidency, Roosevelt was dedicated to the health and wellbeing of forests, establishing 150 [[national forests]]. | /tr/presidency/conservation/national-forests |
| /visit/exhibits/main | …er. He helped end a war between Russia and Japan and became the first American to win the [[Nobel Peace Prize]] . At home, he laid groundwork for the federal safeguards that would become the FDA, champ… | /tr/presidency/nobel-peace-prize |
| /tr/complex-legacy/race | [[Booker T. Washington]], the era’s most prominent African American leader, whom Roosevelt invited to dine at the … | /tr/people/booker-t-washington |
| /podcast/good-citizen/live-trpl-2-johnny-morris-and-gov-kelly-armstrong-conservation-commerce-and | …n Juan Hill, leading his troops. I mean, yesterday morning when the first breakout of the [[Spanish American war]] were there in conflict in Cuba. And I was also reminded, my dad's birthday was July 13th,… | /tr/rise-to-power/spanish-american-war |
| /tr/presidency/conservation/national-forests | …appropriations bill on March 4. The episode demonstrated Roosevelt's sophistication about [[executive power]]: when Congress threatened to strip his authority, he moved decisively to lock in his cons… | /tr/presidency/executive-power |
| /visit/exhibits/main | The Republican establishment had shipped him off to the [[vice presidency]] to sideline him. When McKinley was killed, the man they couldn't control suddenly held th… | /tr/rise-to-power/vice-presidency |
| /visit/exhibits/main | Look up. In the windows above, the house comes alive: silhouettes of the [[Roosevelt family]], and the very adventures Theodore is reading play out across the glass — the stories fill… | /tr/family |
| /tr/conservation/quotes | …d the early environmental movement. But Roosevelt provided something those voices lacked: [[executive power]], political courage, and the will to act decisively despite opposition. He transformed con… | /tr/presidency/executive-power |
| /tr/homes-and-places/sagamore-hill | … Roosevelt family at Sagamore Hill in 1903: Theodore and Edith with their children Alice, [[Ted Jr]]., Kermit, Ethel, Archie and Quentin. (Harvard College Library) | /tr/people/ted-jr |
| /tr/timeline | …edition on the continent of Africa on March 23, 1909, with a party that included his son, [[Kermit Roosevelt]]. The elder Roosevelt was 50 years old. The expedition spent almost a full year in British… | /tr/people/kermit |
| /tr/family/fdr-connection | Franklin Roosevelt as [[Assistant Secretary of the Navy]] in 1913, holding the same post Theodore had occupied sixteen years earlier (Library of Co… | /tr/rise-to-power/assistant-navy-secretary |
| /tr/speeches/confession-of-faith | …cans by taking a more cautious approach to conservation, to antitrust enforcement, and to [[executive power]] generally. Progressives believed that Taft had betrayed Roosevelt's legacy. They demanded… | /tr/presidency/executive-power |
| /visit/exhibits/main | … 5 national parks, and 4 national game preserves. He created the U.S. Forest Service with [[Gifford Pinchot]], signed the Antiquities Act, and set aside Pelican Island as the first federal bird reser… | /tr/presidency/conservation/gifford-pinchot |
| /tr/people/gifford-pinchot | …legal channels and Congressional consultation. This fundamental difference in approach to [[executive power]] became the axis of conflict, and it placed Pinchot in an impossible position. | /tr/presidency/executive-power |
| /tr/presidency/conservation/gifford-pinchot | …st King.” Pinchot's creed — conservation as the “wise use” of resources — set him against [[John Muir]]'s call to preserve such places untouched. (Library of Congress) | /tr/people/john-muir |
| /tr/rise-to-power/rough-riders | The regiment was based in San Antonio, Texas, at Camp Wood, where Roosevelt and Colonel [[Leonard Wood]] set about the work of transforming diverse individuals into a functioning military unit. … | /tr/people/leonard-wood |

### Pages nothing links to
| Page | Title | Impr. |
|---|---|---|
| /tr/pre-presidency-political-accomplishments | WHAT WERE THEODORE ROOSEVELT’S FIVE SIGNIFICANT ACCOMPLISHMENTS PRIOR TO BECOMING PRESIDENT? | 52329 |
| /tr/10-myths-teddy-bear | TOP 10 MYTHS ABOUT THEODORE ROOSEVELT + THE INVENTION OF THE TEDDY BEAR | 14812 |
| /tr/fake-quotes | DID TR REALLY SAY THAT? | 14015 |
| /programs | Programs | 7532 |
| /research/books-by-roosevelt | TR's Published Books | 6196 |
| /tr/5-big-adventures | TR’S FIVE BIG POST-PRESIDENTIAL ADVENTURES | 5700 |
| /join-us | Join Us | 5282 |
| /tr/tr-save-the-bison | DID THEODORE ROOSEVELT SAVE THE BISON? | 3713 |
| /visit/medora/history | History of Medora | 2195 |
| /research/archives | Archives | 1900 |
| /visit/teddy-trail | The Teddy Trail | 878 |
| /visit/exhibits/artificial-intelligence | Artificial Intelligence and Responsible Stewardship | 677 |
| /events/teddycon | Theodore Roosevelt Convention (#TeddyCon) | 588 |
| /visit/weather | Weather | 371 |
| /digital-guide | Free Digital Guide | 349 |
| /research/family-tree | Theodore Roosevelt Family Tree / Theodore Roosevelt Presidential Library | 232 |
| /vote | Step Into the Arena | 230 |
| /visit/roosevelt-in-medora | Roosevelt in Medora | 221 |
| /visit/groups | Group Reservations | 162 |
| /tr/badlands/timeline | The Badlands Years: 1883–1887 Timeline | 153 |
| /alexander-hamilton-speaks | Alexander Hamilton Speaks | 133 |
| /support/heritage-society | The TRPL HERITAGE SOCIETY | 118 |
| /beam-signing-ceremony | Beam Signing Ceremony | 86 |
| /visit/groups/field-trips | Field Trips | 66 |
| /impact |  | 64 |

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
| ten facts | /tr/rise-to-power/ten-facts, /tr/badlands/ten-facts, /tr/early-life/ten-facts |
| elliott roosevelt | /tr/family/elliott-roosevelt, /tr/people/elliott |
| martha "mittie" bulloch roosevelt | /tr/early-life/mother, /tr/people/mittie |
| sagamore hill | /tr/homes-and-places/sagamore-hill, /tr/rise-to-power/sagamore-hill |
| 7-day trip | /visit/itineraries/7-day-bismarck-rapid-city, /visit/itineraries/7-day-billings-bismarck |
| teaching theodore roosevelt | /tr/for-educators/high-school, /tr/for-educators/elementary, /tr/for-educators/middle-school |

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
293 of 889 content pages carry their own markup (33%); 6 sitewide issues (1 high). llms.txt on trlibrary.com: yes (draft: https://seo.labs.trlibrary.com/data/site-llms.txt).

Most fixes are one change to a Drupal template per content type (ask FiveJars); the JSON-LD examples are built from a real page. Values starting 'TODO:' must be filled from the page's own fields, never guessed.

### Sitewide issues
| Severity | Issue | Fix |
|---|---|---|
| high | Sitewide markup doesn't link to the Library's Wikipedia entry | Add these to sameAs in the sitewide schema. |
| medium | Restaurant and store hours are listed as the museum's hours | Keep only museum hours on the Library entity. Give the restaurant and the store their own entities (Restaurant, Store) with their hours, linked with containsPlace. |
| medium | No admission information in the markup | Add admission offers (and isAccessibleForFree: false) to the Library entity. |
| medium | 35 unaliased /node/ URLs are in the sitemap | Ask FiveJars to leave unaliased /node/ URLs out of the XML sitemap. |
| low | 267 pages have dates without a colon in the time zone | In the Drupal schema templates, format dateModified, datePublished, endDate, startDate with the PHP date format “c” (e.g. 2020-10-27T06:00:00-06:00). |
| low | 91 articles are labelled og:type “website” | Set og:type to “article” on /tr, press release and podcast templates (Drupal Metatag). |

### By content type (biggest gaps first)
| Content type | Should carry | Pages | Has it | Incomplete | Fix |
|---|---|---|---|---|---|
| Video pages | VideoObject | 409 | 0 | 0 | Add VideoObject JSON-LD to the video view template from the stored YouTube data (title, description, thumbnail, publish date, duration). |
| Good Citizen episodes | PodcastEpisode | 72 | 0 | 0 | Add PodcastEpisode JSON-LD to the podcast episode template (title, summary, release date, Simplecast player). |
| TR history section pages | CollectionPage | 55 | 0 | 0 | Add CollectionPage JSON-LD to the /tr section landing template. |
| Trip itineraries | TouristTrip | 20 | 0 | 0 | Add TouristTrip JSON-LD to the itinerary template, listing each stop. Check the drafted stop list: it's taken from the page headings. |
| Video playlists | ItemList / VideoObject | 39 | 0 | 0 | Add ItemList of VideoObject JSON-LD to the playlist template. Drupal already stores each video's YouTube data, including its publish date (uploadDate). |
| Press releases | Article / NewsArticle | 19 | 19 | 19 | Add NewsArticle JSON-LD to the press release template, using the release date field. |
| Trustee profiles | Person / ProfilePage | 13 | 13 | 13 | Add ProfilePage + Person JSON-LD (role: Trustee) to the trustee template. |
| Pages with Q&A | FAQPage | 20 | 19 | 0 | Add FAQPage JSON-LD to the accordion paragraph type: when every item's title is a question, output each as Question/Answer. One template change covers every FAQ page. |
| Good Citizen podcast page | PodcastSeries | 1 | 0 | 0 | Add PodcastSeries JSON-LD to the podcast landing page. |
| Calendar events | Event | 28 | 28 | 1 | Add Event JSON-LD to the Event content type template, filled from the event's date, time, price and ticket fields. One template change covers every event. |
| Staff profiles | Person / ProfilePage | 42 | 42 | 0 | Add ProfilePage + Person JSON-LD to the staff member template (name, job title, photo). |
| TR history articles | Article | 159 | 159 | 0 | Add Article JSON-LD to the /tr article template with about = Theodore Roosevelt (the sitewide #theodore-roosevelt entity) and dateModified from the node's changed date. |
| TR history: people | Article | 26 | 26 | 0 | Add Article JSON-LD to the /tr people template, with an 'about' Person; a field for the person's Wikidata link makes it precise. |
| TR history: speeches | Article | 6 | 6 | 0 | Add Article JSON-LD with an 'about' CreativeWork (the speech, author: Theodore Roosevelt). |

## Ticket checkout (GA4, rates only)
Checkout completion – (prior –); store visitors who buy 19% (prior 41%); ticket page to store 44%. Steps the store doesn't report: view_item, add_to_cart, begin_checkout, add_payment_info.

Store frustration signals (last 3 days, Clarity): dead clicks 9.3% of sessions, rage clicks 0.2%, quick backs 6.8%, scroll depth 48.5%.

| Store page | Dead % | Rage % | Quick back % | Scroll % |
|---|---|---|---|---|
| calendar/special-event/america-beautiful-film-screening | 0 | 0 | 0 | 20 |
| tickets | 0 | 0 | 0 | 5 |
| membership/join | 0 | 0 | 0 | 100 |
| private-events/inquiry | 0 | 0 | 0 | 65 |
| orders/tickets | 0 | 0 | 0 | 91.5 |
| private-events | 0 | 0 | 0 | 24 |
| checkout/confirm | 11.8 | 0 | 0 | 99.4 |
| tr/family/family-tree | 0 | 0 | 0 | 61.6 |
| visit/directions | 0 | 0 | 100 | 64 |
| search | 0 | 0 | 100 | 100 |
| rsvp/holidayopenhouse | 0 | 0 | 0 | 100 |
| project/living-building-challenge | 0 | 0 | 0 | 78 |
| support/donor-advised-fund | 0 | 0 | 0 | 100 |
| orders/forms | 0 | 0 | 0 | 100 |
| / | 100 | 0 | 0 | 16 |
| calendar/special-event/elkhorn-evenings | 0 | 0 | 0 | 93.5 |
| midwinter-table | 0 | 0 | 0 | 27 |
| tr/presidency/race | 0 | 0 | 0 | 42.6 |
| visit/groups | 33.3 | 0 | 0 | 70.3 |
| about/press/press-releases/theodore-roosevelts-groundbreaking-firsts-and-feats-celebration | 0 | 0 | 0 | 92.5 |
| video/view/qrwdZmqFO5A | 100 | 0 | 0 | 68 |
| tr/presidency/executive-actions/action | 0 | 0 | 0 | 91 |
| video/view/1nogFWdneOw | 0 | 0 | 50 | 81.1 |
| tr/rise-to-power/spanish-american-war | 16.7 | 0 | 0 | 39.8 |
| calendar | 0 | 0 | 0 | 71 |
| tr/people | 0 | 0 | 0 | 37 |
| tr/quotes | 0 | 0 | 0 | 55 |
| quiz/pets | 0 | 0 | 0 | 100 |
| bullet-speech | 10 | 0 | 0 | 41.5 |
| calendar/special-event | 0 | 0 | 0 | 7 |
| tr/pre-presidency-political-accomplishments | 30 | 0 | 0 | 45.4 |
| tr/people/william-howard-taft | 33.3 | 0 | 0 | 49.8 |
| video/view/cztQVr_fAz4 | 0 | 0 | 0 | 30 |
| tr/presidency/conservation/gifford-pinchot | 33.3 | 0 | 0 | 63 |
| auth/members | 0 | 0 | 0 | 100 |
| staff-members/rachel-moats | 0 | 0 | 0 | 67 |
| checkout/process | 50 | 0 | 0 | 100 |
| visit/maps | 0 | 0 | 0 | 30 |
| tr | 33.3 | 0 | 33.3 | 75.7 |
| visit/lodging/availability | 0 | 0 | 0 | 27 |
| tr/rise-to-power/boone-and-crockett | 0 | 0 | 0 | 35 |
| tr/presidency/square-deal | 14.3 | 0 | 0 | 31.1 |
| tr/presidency/trust-busting | 10 | 0 | 0 | 41.7 |
| tr/fake-quotes | 5.6 | 0 | 0 | 28.8 |
| podcast/good-citizen/karl-rove-historic-redemption-hard-work-politics-and-essential-nature | 0 | 0 | 0 | 34.3 |
| calendar/special-event/butchery-workshop | 0 | 0 | 0 | 62 |
| project | 15.4 | 0 | 30.8 | 82.3 |
| volunteer | 0 | 0 | 0 | 99 |
| visit/itineraries | 0 | 0 | 0 | 65 |
| visit/hours | 0 | 0 | 0 | 34 |
| visit | 3 | 0 | 12.1 | 37.2 |
| visit/wildlife | 0 | 0 | 0 | 34 |
| holidaytrees | 0 | 0 | 0 | 49.2 |
| orders/calendar | 6.2 | 0 | 75 | 91.5 |
| tr/post-presidency/new-nationalism | 0 | 0 | 0 | 18 |
| video/view/sVxuv_VO03Y | 33.3 | 0 | 0 | 51 |
| tr/rise-to-power/vice-presidency | 0 | 0 | 0 | 37 |
| calendar/special-event/holiday-open-house | 0 | 0 | 20 | 91.7 |
| tr/legacy/mount-rushmore | 0 | 0 | 0 | 16 |
| tr/tr-mount-rushmore | 16.7 | 0 | 0 | 41.9 |
| tr/people/leonard-wood | 0 | 0 | 0 | 23.5 |
| tr/badlands-timeline | 0 | 0 | 0 | 59 |
| podcast/good-citizen/richard-haass | 0 | 0 | 0 | 5 |
| tr/people/john-muir | 0 | 0 | 0 | 22 |
| video/playlist/PL-sck-PjBiFelZ6jvE62RfVlRvbicBsoS | 0 | 0 | 0 | 87 |
| staff-members/jeremy-beam | 0 | 0 | 0 | 92 |
| holiday-2026 | 14.3 | 0 | 0 | 61.7 |
| visit/planner | 0 | 0 | 0 | 9 |
| tr/for-educators/middle-school | 0 | 0 | 33.3 | 52.4 |
| tr/speeches/man-in-the-arena | 20.6 | 0 | 0 | 49.9 |
| video/view/FH2iglgaMZE | 0 | 0 | 0 | 88 |
| tr/elkhorn | 0 | 0 | 0 | 86 |
| tr/badlands/where-to-see | 0 | 0 | 0 | 23 |
| tr/family/fdr-connection | 4.2 | 0 | 4.2 | 29.6 |
| about/press/press-releases/harold-hamm-donates-50-million-trpl | 0 | 0 | 0 | 98 |
| visit/accessibility | 0 | 0 | 0 | 20 |
| tr/rise-to-power/jacob-riis | 0 | 0 | 0 | 33 |
| tr/early-life/mother | 100 | 0 | 0 | 88 |
| video/view/sUIbk8egtC0 | 0 | 0 | 0 | 32 |
| visit/faq | 0 | 0 | 0 | 49 |
| tr/presidency/great-white-fleet | 20 | 0 | 0 | 44.2 |
| tr/presidency/foreign-policy | 0 | 0 | 0 | 8 |
| about/press/press-releases/theodore-roosevelt-presidential-library-opening-celebrations-july-4-2026 | 0 | 0 | 0 | 38 |
| about/press/press-releases/confluence-named-landscape-architect-record | 0 | 0 | 0 | 100 |
| support/benefactor-societies | 0 | 0 | 0 | 20 |
| visit/groups/field-trips | 0 | 0 | 50 | 40.7 |
| visit/one-medora | 0 | 0 | 0 | 98 |
| tr/presidency-timeline | 20 | 0 | 0 | 36.6 |
| tr/early-life | 9.1 | 0 | 18.2 | 62.6 |
| video/view/eb2v8aZvyfQ | 0 | 0 | 0 | 37 |
| support | 0 | 0 | 0 | 24 |
| tr/presidency/booker-t-washington | 0 | 0 | 0 | 20.3 |
| visit/faq/tickets | 0 | 0 | 0 | 100 |
| tr/family/children | 20 | 0 | 0 | 56 |
| tr/people/ted-jr | 0 | 0 | 0 | 15 |
| tr/complex-legacy/imperialism | 0 | 0 | 0 | 36.6 |
| video/view/GpKHsBZXubE | 0 | 0 | 16.7 | 62.6 |
| video/view/-mcN1M3ZEps | 0 | 0 | 0 | 39 |
| teach-tr | 0 | 0 | 100 | 100 |
| tr/presidency/railroad-regulation | 14.3 | 0 | 0 | 38.1 |
| tr/people/eleanor | 0 | 0 | 0 | 9 |
| visit/stargazing/northern-lights | 50 | 0 | 0 | 43.3 |
| tr/presidency | 0 | 0 | 10 | 37.5 |
| membership/detail | 0 | 0 | 33.3 | 97.1 |
| calendar/specialty-tour | 0 | 0 | 0 | 97 |
| tr/presidency/strenuous-life-in-office | 0 | 0 | 0 | 12 |
| tr/kids-timeline | 0 | 0 | 0 | 4 |
| visit/camping | 0 | 0 | 0 | 9 |
| tr/presidency/conservation/national-monuments | 0 | 0 | 0 | 39 |
| staff-members/cj-von-buchwald-wright | 0 | 0 | 0 | 65 |
| about/foundation | 0 | 0 | 0 | 71.2 |
| tr/new-york-politics/convention-1884 | 100 | 0 | 0 | 21 |
| tr/badlands/medora | 0 | 0 | 50 | 45.7 |
| tr/complex-legacy/equestrian-statue | 0 | 0 | 0 | 73 |
| tr/presidency/conservation/john-muir | 100 | 0 | 0 | 70 |
| membership | 0 | 0 | 0 | 92 |
| tr/post-presidency/death | 25 | 0 | 0 | 76.8 |
| about/trustees/vaughn-williams | 0 | 0 | 0 | 87 |
| podcast/good-citizen/live-trpl-3-arthur-brooks-and-robbie-lauf-strenuous-life-and-search-happiness | 0 | 0 | 0 | 16 |
| tr/presidency/conservation | 0 | 0 | 0 | 57.4 |
| visit/maps/campus | 0 | 0 | 0 | 100 |
| tr/rise-to-power/edith-roosevelt | 100 | 0 | 0 | 96 |
| about/press/press-releases/theodore-roosevelt-presidential-library-welcomes-new-trustees-ahead-2026 | 0 | 0 | 0 | 94 |
| tr/rise-to-power/sagamore-hill | 0 | 0 | 0 | 84 |
| tr/post-presidency | 0 | 0 | 0 | 69.5 |
| contact | 10 | 0 | 0 | 76.5 |
| calendar/special-event/visit-santa-claus | 0 | 0 | 0 | 30 |
| tr/badlands | 0 | 0 | 0 | 33 |
| tr/presidency/elections | 0 | 0 | 0 | 12.5 |
| tr/post-presidency/bull-moose | 14.3 | 0 | 0 | 63.4 |
| about/trustees/dick-boyce | 50 | 0 | 0 | 81.5 |
| tr/quotes/citizenship | 0 | 0 | 0 | 28.8 |
| tr/10-myths-teddy-bear | 0 | 0 | 0 | 85.8 |
| tr/badlands/first-trip | 0 | 0 | 0 | 58.2 |
| visit/exhibits/artificial-intelligence | 0 | 0 | 0 | 94 |
| staff-members/addison-olson | 0 | 0 | 0 | 74 |
| membership/renew/detail | 0 | 0 | 0 | 64 |
| podcast/good-citizen | 0 | 0 | 20 | 11.8 |
| tr/speeches/first-annual-message | 0 | 0 | 0 | 58 |
| staff-members/clancy-griggs | 0 | 0 | 0 | 95 |
| visit/tours | 16.7 | 0 | 0 | 59.6 |
| about/press | 0 | 0 | 0 | 98 |
| tr/speeches | 40 | 0 | 0 | 80.3 |
| visit/faq/during-your-visit | 0 | 0 | 0 | 73 |
| visit/eat | 50 | 0 | 0 | 45.7 |
| visit/national-park/trip-planner | 0 | 0 | 0 | 96.5 |
| video/view/W9sq8PuGQVo | 0 | 0 | 0 | 62.2 |
| tr/speeches/inaugural | 0 | 0 | 0 | 42 |
| newsletter | 0 | 0 | 0 | 100 |
| quiz/badlands-wildlife-family | 100 | 0 | 0 | 99 |
| tr/badlands/boat-thieves | 50 | 0 | 0 | 39.5 |
| about/trustees | 0 | 0 | 16.7 | 57.6 |
| rsvp/midwinter | 100 | 0 | 0 | 99 |
| tr/rise-to-power/buffalo-soldiers | 16.7 | 0 | 16.7 | 55.8 |
| about/mission | 0 | 0 | 0 | 74.3 |
| visit/medora-traditions | 0 | 0 | 0 | 85 |
| tr/presidency/panama-canal | 23.1 | 0 | 0 | 30.9 |
| private-events/spaces | 0 | 0 | 0 | 100 |
| membership/renew | 0 | 0 | 33.3 | 99 |
| visit/activities | 0 | 0 | 100 | 15 |
| tr/presidency/roosevelt-corollary | 16.7 | 0 | 0 | 36.7 |
| calendar/daily-activity/free-final-hour | 0 | 0 | 0 | 28 |
| tr/people/bamie | 0 | 0 | 0 | 49 |
| tr/new-york-politics/alice-lee | 0 | 0 | 0 | 35 |
| tr/presidency/bully-pulpit](https://www.trlibrary.com/tr/presidency/bully-pulpit | 0 | 0 | 0 | 69 |
| tr/presidency/ten-facts | 17.4 | 0 | 0 | 52.8 |
| staff-members/kristie-skunberg | 0 | 0 | 0 | 94 |
| tr/conservation | 0 | 0 | 0 | 59.5 |
| tr/strenuous-life | 0 | 0 | 0 | 48 |
| tr/people/quentin | 0 | 0 | 0 | 93 |
| about/trustees/david-saggau | 0 | 0 | 0 | 71 |
| tr/new-york-politics/assembly | 100 | 0 | 0 | 59.5 |
| staff-members/nicole-turchin | 0 | 0 | 0 | 69 |
| about/trustees/beth-laski | 0 | 0 | 0 | 82.5 |
| research | 0 | 0 | 100 | 54 |
| about/trustees/john-palfrey | 0 | 0 | 0 | 92.5 |
| video/view/wAknvXeHzSc | 0 | 0 | 0 | 46 |
| visit/maps/print | 0 | 0 | 0 | 26 |
| calendar/specialty-tour/theodore-roosevelt-and-american-empire-tour | 0 | 0 | 0 | 40 |
| membership/neighbor | 0 | 0 | 0 | 50.5 |
| membership/profile | 0 | 0 | 50 | 100 |
| tr/presidency/brownsville | 20 | 0 | 0 | 26.9 |
| private-events/catering | 100 | 0 | 0 | 99 |
| staff-members | 0 | 0 | 100 | 56 |
| staff-members/jolene-procive | 0 | 0 | 0 | 67 |
| tr/books-and-writings/complete-list | 0 | 0 | 0 | 21.5 |
| programs | 0 | 0 | 50 | 81.7 |
| calendar/medora | 0 | 0 | 0 | 91 |
| about | 0 | 0 | 0 | 42 |
| tr/presidency/executive-power | 22.2 | 0 | 0 | 28.9 |
| quiz | 0 | 0 | 0 | 53.5 |
| events/detail | 0 | 0 | 0 | 100 |
| visit/tickets/plan-ahead | 0 | 0 | 0 | 44.2 |
| video/view/fPZD2xLBXZs | 0 | 0 | 50 | 36.7 |
| tr/rise-to-power/san-juan-hill | 6.7 | 0 | 0 | 23.5 |
| tr/rise-to-power/ten-facts | 0 | 0 | 0 | 34.2 |
| about/careers | 0 | 0 | 0 | 49.7 |
| tr/timeline | 83.3 | 16.7 | 0 | 61.5 |
| tr/speeches/new-nationalism | 0 | 0 | 0 | 27 |
| digital-guide | 0 | 0 | 100 | 70.3 |
| tr/holidays | 0 | 0 | 0 | 77 |
| tr/legacy/teddy-bear | 0 | 0 | 0 | 29.3 |
| podcast/good-citizen/ted-leonsis | 0 | 0 | 0 | 9 |
| tr/thanksgiving-timeline | 0 | 0 | 0 | 51 |
| tr/conservation/quotes | 0 | 0 | 0 | 29 |
| tr/legacy | 0 | 0 | 0 | 67 |
| staff-members/candace-stock | 0 | 0 | 0 | 76 |
| tr/post-presidency/quentin | 33.3 | 0 | 0 | 95.3 |
| about/presidential-library-system | 0 | 0 | 0 | 40.5 |
| tr/people/elliott | 0 | 0 | 0 | 92 |
| visit/exhibits | 20 | 0 | 40 | 85.6 |
| tr/rise-to-power/becoming-president | 0 | 0 | 0 | 18.3 |
| tr/tr-shot | 16.7 | 0 | 0 | 31.5 |
| tr/family/elliott-roosevelt | 0 | 0 | 0 | 99 |
| tr/post-presidency/bull-moose/platform | 20 | 0 | 0 | 42.8 |
| beam-signing-ceremony | 0 | 0 | 0 | 7 |
| holiday | 0 | 0 | 0 | 100 |
| tr/speeches/confession-of-faith | 0 | 0 | 0 | 31 |
| visit/outdoors | 0 | 0 | 0 | 17 |
| tr/homes-and-places/white-house | 0 | 0 | 0 | 91 |
| tr/for-educators/elementary | 0 | 0 | 0 | 41 |
| tr/presidency/bully-pulpit | 0 | 0 | 0 | 38.6 |
| video/view/bNpkcnRSmmQ | 20 | 0 | 0 | 28.7 |
| tr/rise-to-power/rough-riders | 25 | 0 | 25 | 24 |
| visit/scenic-drives | 0 | 0 | 0 | 15.5 |
| tr/presidency/cabinet | 0 | 0 | 0 | 22.2 |
| tr/strenuous-life/hunter | 0 | 0 | 0 | 9.6 |
| visit/itineraries/sturgis-medora | 0 | 0 | 0 | 12 |
| tr/family | 33.3 | 0 | 33.3 | 53 |
| podcast/good-citizen/call-adventure-charlie-melcher-ed-okeefe-and-brand-new-theodore-roosevelt | 0 | 0 | 0 | – |
| video/view/o7X2oPGLGq8 | 0 | 0 | 0 | 48 |
| tr/people/booker-t-washington | 0 | 0 | 0 | 62.3 |
| video/view/2AWoe6mRBus | 0 | 0 | 0 | 100 |
| video/view/zRPJAdE-IBI | 0 | 0 | 0 | 73 |
| staff-members/amy-mccann | 0 | 0 | 0 | 83 |
| tickets/terms | 0 | 0 | 0 | 14 |
| staff-members/chris-blackwell | 0 | 0 | 0 | 100 |
| video/view/15dkv17Wk38 | 0 | 0 | 0 | 18 |
| join-us | 0 | 0 | 0 | 61 |
| tr/presidency/conservation/antiquities-act | 0 | 0 | 0 | 11 |
| tr/early-life/father | 0 | 0 | 0 | 47 |
| visit/shopping | 0 | 0 | 0 | 6 |
| staff-members/alice-wynd | 0 | 0 | 0 | 67 |
| video/view/3y-8aHZr0Nk | 0 | 0 | 0 | 46 |
| user/login | 0 | 0 | 0 | 100 |
| about/trustees/doris-kearns-goodwin | 0 | 0 | 0 | 74 |
| tr/people/medora-de-mores | 0 | 0 | 0 | 43.3 |
| quiz/immigration-era | 0 | 0 | 0 | 47 |
| tr/presidency/executive-actions/story | 0 | 0 | 0 | 23 |
| tr/early-life/childhood-illness | 33.3 | 0 | 0 | 62.7 |
| tr/complex-legacy/race | 0 | 0 | 0 | 63 |
| video/view/3i6j26fH7JE | 0 | 0 | 50 | 32 |
| staff-members/marcie-woehl | 0 | 0 | 0 | 97 |
| tr/myths/misquotes | 0 | 0 | 0 | 9 |
| tr/badlands/winter-of-1887 | 0 | 0 | 0 | 55 |
| tr/legacy/rankings | 0 | 0 | 0 | 40 |
| tr/for-educators/high-school | 100 | 0 | 0 | 100 |
| visit/lodging | 50 | 0 | 25 | 80 |
| tr/quotes/misquotes | 12.5 | 0 | 0 | 32.4 |
| tr/family/roosevelt-women | 0 | 0 | 0 | 32 |
| tr/presidency/conservation/reclamation | 0 | 0 | 0 | 42.8 |
| podcast/good-citizen/kermit-roosevelt-iii | 0 | 0 | 0 | 15 |
| video/playlist/PLSaoXk08gMqQ | 0 | 0 | 0 | 99 |
| brand | 0 | 0 | 0 | 100 |
| tr/rise-to-power | 0 | 0 | 25 | 44.8 |
| tr/for-educators | 0 | 0 | 50 | 55 |
| visit/itineraries/conservation | 50 | 0 | 0 | 85.5 |
| tr/post-presidency/river-of-doubt | 0 | 0 | 0 | 3 |
| tr/complex-legacy | 0 | 0 | 100 | 25 |
| visit/exhibits/kennerly | 0 | 0 | 0 | 55.5 |
| tr/speeches/strenuous-life | 0 | 0 | 0 | 57.8 |
| tr/new-york-politics | – | – | – | 45.5 |

## Tracking changes made automatically
Rules and caps: config/tracking.yml. Keep an item permanently by copying it into config/keywords.yml or config/ai_prompts.yml; block it via tracking.yml exclude.

| Date | Change | Type | Item | Why |
|---|---|---|---|---|
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
| 2026-11-09 | added | keyword | who is on mount rushmore | position 6.7, 5233 impressions/28d; High-volume discovery query connecting Theodore Roosevelt's legacy to national landmark travel. |
| 2026-11-09 | added | keyword | kermit roosevelt | position 7.4, 9187 impressions/28d; Theodore Roosevelt's son and companion on the African and Amazon expeditions. |
| 2026-11-09 | added | keyword | man in the arena | position 6.1, 7558 impressions/28d; Theodore Roosevelt's most famous civic passage; core entry point for civic education. |
| 2026-11-09 | added | keyword | alice roosevelt | position 8.1, 11847 impressions/28d; High-volume search on Theodore Roosevelt's eldest daughter and White House icon. |
| 2026-11-02 | added | question | Which presidents are carved on Mount Rushmore, and why was Theodore Roosevelt included? | from the Google search "who is on mount rushmore"; High-volume inquiry connecting Roosevelt to regional Northern Plains travel and heritage. |

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
