# trlibrary.com search & AI visibility digest
Generated 2026-11-12T13:25:59+00:00 from https://seo.labs.trlibrary.com. Full data: see 'Raw data' at the end.

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
47 tasks (2 search, 23 audit, 5 internal links, 15 structured data, 2 AI visibility); 13 with FiveJars or blocked. Ranked by severity x the Google audience of the pages involved. Full lists, every page, and step-by-step Drupal recipes: https://seo.labs.trlibrary.com/data/work_queue.json

### This week's moves
1. **Add internal links where pages already mention each other** (`links:add`): medium priority; pages involved get 251,288 Google impressions (28 days). Start with: /tr/timeline; /visit/exhibits/main; /podcast/good-citizen/edward-okeefe.
2. **Pages ranking well that people skip: rewrite title and description** (`search:low_ctr`): medium priority; pages involved get 82,617 Google impressions (28 days). Start with: /tickets; /tr/rise-to-power/rough-riders; /tr/presidency/foreign-policy.
3. **Searches AI assistants run where trlibrary.com isn't on page one** (`ai:searches_we_miss`): medium priority; affects the whole site. Start with: "Badlands Dinosaur Museum Dickinson North Dakota family activities" (run by ChatGPT); "Badlands National Park NPS scenic drive Ben Reifel Visitor Center official site" (run by ChatGPT); "Badlands National Park scenic loop Wall Drug Minuteman Missile National Historic Site official sites" (run by ChatGPT).

### What else we checked (and why it can wait)
- Restaurant and store hours are listed as the museum's hours (`schema:sitewide:mixed_hours`): FiveJars work; send as a ticket
- Same topic on two pages (merge or differentiate) (`links:duplicate_topics`): needs a decision first (merge or archive)
- Pages nothing links to (`links:orphans`): same area as a move this week (internal links); next in line
- Get onto pages AI cites that leave the Library out (`ai:ask_to_be_added`): same area as a move this week (ai visibility); next in line
- Same title as another page (`audit:title_duplicate`): smaller reach (12,977 Google impressions vs 82,617 for this week's moves)
- Strengthen pages ranking just off the top for searches people make (`search:striking_distance`): same area as a move this week (search); next in line
- Missing Open Graph tags (`audit:og_missing`): smaller reach (7,874 Google impressions vs 82,617 for this week's moves)
- No meta description (`audit:meta_missing`): smaller reach (7,042 Google impressions vs 82,617 for this week's moves)

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
| 2 | Same topic on two pages (merge or differentiate) | internal links | TRPL | 20 | needs approval | links:duplicate_topics |
| 3 | Add internal links where pages already mention each other | internal links | TRPL | 579 | to do | links:add |
| 4 | Pages nothing links to | internal links | TRPL | 45 | to do | links:orphans |
| 5 | Pages ranking well that people skip: rewrite title and description | search | TRPL | 4 | to do | search:low_ctr |
| 6 | Searches AI assistants run where trlibrary.com isn't on page one | ai visibility | TRPL | 63 | to do | ai:searches_we_miss |
| 7 | Get onto pages AI cites that leave the Library out | ai visibility | TRPL | 2 | to do | ai:ask_to_be_added |
| 8 | Same title as another page | audit | TRPL | 37 | to do | audit:title_duplicate |
| 9 | Strengthen pages ranking just off the top for searches people make | search | TRPL | 9 | to do | search:striking_distance |
| 10 | Missing Open Graph tags | audit | TRPL | 12 | to do | audit:og_missing |
| 11 | No meta description | audit | TRPL | 11 | to do | audit:meta_missing |
| 12 | No H1 heading | audit | TRPL | 29 | to do | audit:h1_missing |
| 13 | Turn on IndexNow so Bing and Copilot see changes within hours | audit | FiveJars | 1 | to do | setup:indexnow |
| 14 | Same title as another page (Video pages: fix once in the video template) | audit | FiveJars | 32 | to do | audit:title_duplicate:template |
| 15 | Links that go through a redirect | internal links | TRPL | 72 | to do | links:via_redirect |
| 16 | No meta description (Video pages: fix once in the video template) | audit | FiveJars | 17 | to do | audit:meta_missing:template |
| 17 | Missing Open Graph tags (Video pages: fix once in the video template) | audit | FiveJars | 17 | to do | audit:og_missing:template |
| 18 | Heading levels skip (e.g. H2 straight to H4) | audit | TRPL | 146 | to do | audit:heading_skip |
| 19 | Related pages that don't link to each other | internal links | TRPL | 27 | to do | links:related |
| 20 | Title over 60 characters, not counting the site-name suffix | audit | TRPL | 92 | to do | audit:title_too_long |
| 21 | More than 4 clicks from the homepage | audit | TRPL | 112 | to do | audit:deep_page |
| 22 | Sitemap lists a /node/ URL instead of a readable path | audit | TRPL | 35 | to do | audit:unaliased_url |
| 23 | Same meta description as another page | audit | TRPL | 43 | to do | audit:meta_duplicate |
| 24 | Title under 15 characters, not counting the site-name suffix | audit | TRPL | 144 | to do | audit:title_too_short |
| 25 | Sitemap lists a URL that redirects | audit | TRPL | 5 | to do | audit:redirect_in_sitemap |
| 26 | More than one H1 | audit | TRPL | 10 | to do | audit:h1_multiple |
| 27 | Under 150 words of body text | audit | TRPL | 237 | to do | audit:thin_content |
| 28 | Title over 60 characters, not counting the site-name suffix (Video pages: fix once in the video template) | audit | FiveJars | 173 | to do | audit:title_too_long:template |
| 29 | Took over 3 seconds to respond | audit | FiveJars | 3 | to do | audit:slow |
| 30 | Same meta description as another page (Video pages: fix once in the video template) | audit | FiveJars | 82 | to do | audit:meta_duplicate:template |

### Task details (TRPL can do these now)
**2. Same topic on two pages (merge or differentiate)** (`links:duplicate_topics`, 20 items)
- How: Two pages compete for one subject. Pick the stronger page (clicks, depth), move anything unique onto it, then archive the other and add a 301 from its alias and /node/NID. Get approval first; draft before publishing.
- Done when: One page per topic; the other 301s to it
  - `/tr/tr-mount-rushmore`, 135,448 impr., mount rushmore: /tr/tr-mount-rushmore vs /tr/legacy/mount-rushmore
  - `/tr/rise-to-power/san-juan-hill`, 43,340 impr., rough riders: /tr/rise-to-power/san-juan-hill vs /tr/rise-to-power/rough-riders
  - `/tr/people/alice-longworth`, 28,558 impr., alice roosevelt longworth: /tr/people/alice-longworth vs /tr/people/alice-longworth/complex-legacy
  - `/tr/new-york-politics/alice-lee`, 12,401 impr., alice hathaway lee roosevelt: /tr/new-york-politics/alice-lee vs /tr/people/alice-lee
  - `/tr/new-york-politics/alice-lee`, 12,401 impr., alice lee: /tr/new-york-politics/alice-lee vs /tr/people/alice-lee
  - `/tr/rise-to-power/edith-roosevelt`, 11,918 impr., edith roosevelt: /tr/rise-to-power/edith-roosevelt vs /tr/people/edith-roosevelt
  - `/tr/people/booker-t-washington`, 10,816 impr., booker t washington: /tr/people/booker-t-washington vs /tr/presidency/booker-t-washington
  - `/tr/quotes/misquotes`, 8,895 impr., common misquotes: /tr/quotes/misquotes vs /tr/myths/misquotes
  - ...and 12 more in work_queue.json

**3. Add internal links where pages already mention each other** (`links:add`, 579 items)
- How: Open the source page's Layout. Edit the text block that contains the context sentence and turn the [[bracketed]] words into a link to the target path (relative, e.g. /tr/tr-shot). Don't write new sentences just to hold a link. Save the block, then Save layout.
- Done when: The link appears on the source page; the target's links-in count rises next week
  - `/tr/timeline`, 42,853 impr., [[William Howard Taft]] -> /tr/people/william-howard-taft; [[River of Doubt]] -> /tr/post-presidency/river-of-doubt; [[Edith Roosevelt]] -> /tr/rise-to-power/edith-roosevelt
  - `/visit/exhibits/main`, 4,805 impr., [[River of Doubt]] -> /tr/post-presidency/river-of-doubt; [[Alice Hathaway Lee]] -> /tr/new-york-politics/alice-lee; [[Edith Roosevelt]] -> /tr/rise-to-power/edith-roosevelt
  - `/podcast/good-citizen/edward-okeefe`, 345 impr., [[high school]] -> /tr/for-educators/high-school; [[Roosevelt family]] -> /tr/family; [[executive power]] -> /tr/presidency/executive-power
  - `/podcast/good-citizen/doris-kearns-goodwin-presidential-stories-trpl-and-enduring-lessons-theodore`, 936 impr., [[high school]] -> /tr/for-educators/high-school; [[in the room]] -> /visit/exhibits/kennerly; [[the man in the arena]] -> /tr/post-presidency/man-in-the-arena
  - `/tr/presidency/white-house-family`, 1,955 impr., [[Edith Roosevelt]] -> /tr/rise-to-power/edith-roosevelt; [[governor of New York]] -> /tr/rise-to-power/governor; [[Roosevelt White House]] -> /tr/homes-and-places/white-house
  - `/tr`, 8,205 impr., [[Bully Pulpit]] -> /tr/presidency/bully-pulpit; [[high school]] -> /tr/for-educators/high-school; [[Ted Jr]] -> /tr/people/ted-jr
  - `/tr/thanksgiving-timeline`, 184 impr., [[River of Doubt]] -> /tr/post-presidency/river-of-doubt; [[Alice Lee]] -> /tr/new-york-politics/alice-lee; [[Pine Knot]] -> /tr/homes-and-places/pine-knot
  - `/tr/family/family-tree`, 23,449 impr., [[Kermit Roosevelt]] -> /tr/people/kermit; [[Sagamore Hill]] -> /tr/homes-and-places/sagamore-hill; [[Quentin Roosevelt]] -> /tr/people/quentin
  - ...and 286 more in work_queue.json

**4. Pages nothing links to** (`links:orphans`, 45 items)
- How: Add 2-3 links to this page from the pages listed under 'link from' (each has the sentence and words to link).
- Done when: At least two pages link in
  - `/tr/pre-presidency-political-accomplishments`, 53,774 impr.
  - `/tr/10-myths-teddy-bear`, 17,070 impr.
  - `/tr/fake-quotes`, 15,351 impr.
  - `/tr/5-big-adventures`, 6,211 impr.
  - `/research/books-by-roosevelt`, 6,050 impr.
  - `/programs`, 4,684 impr.
  - `/tr/tr-save-the-bison`, 3,841 impr.
  - `/join-us`, 3,140 impr., link from: /podcast/good-citizen/meg-whitman ([[join us]]); /programs ([[Join us]])
  - ...and 37 more in work_queue.json

**5. Pages ranking well that people skip: rewrite title and description** (`search:low_ctr`, 4 items)
- How: Edit the node (/node/NID/edit) > 'Customize meta tags'. Basic tags: Page title '<title> | [site:name]' (page part 60 characters or fewer) and Description (120-155 characters). Set Open Graph og:title/og:description and Twitter card title/description to match. Save with 'Save' (keeps the moderation state). If the save seems to do nothing, look for a validation error further down the form.
- Done when: Click-through rate rises at the same position (change log before/after)
  - `/tickets`, 52,106 impr.
  - `/tr/rise-to-power/rough-riders`, 12,982 impr.
  - `/tr/presidency/foreign-policy`, 9,507 impr.
  - `/tr/presidency/nobel-peace-prize`, 8,022 impr.

**6. Searches AI assistants run where trlibrary.com isn't on page one** (`ai:searches_we_miss`, 63 items)
- How: These are the searches the assistants ran before answering a question where they left the Library out. Find the trlibrary.com page that should answer each one (or note that none does). Strengthen that page for the search: say it in the title or a heading and answer it in the first paragraph, with facts already on the site. If no page fits, propose one.
- Done when: trlibrary.com ranks top 10 for the search (Search Console) and the next AI run cites it
  - `Badlands Dinosaur Museum Dickinson North Dakota family activities`, run by ChatGPT; we rank nowhere
  - `Badlands National Park NPS scenic drive Ben Reifel Visitor Center official site`, run by ChatGPT; we rank nowhere
  - `Badlands National Park scenic loop Wall Drug Minuteman Missile National Historic Site official sites`, run by ChatGPT; we rank nowhere
  - `Bismarck North Dakota Heritage Center & State Museum hours location 'Exit 159' I-94 'ND Heritage Center'`, run by ChatGPT; we rank nowhere
  - `Bonanzaville West Fargo museum website`, run by ChatGPT; we rank nowhere
  - `Crazy Horse Memorial visitor center hours Crazy Horse official site`, run by ChatGPT; we rank nowhere
  - `Custer State Park Wildlife Loop Sylvan Lake Needles Highway official site`, run by ChatGPT; we rank nowhere
  - `Deadwood South Dakota historic main street attractions Deadwood tourism official site`, run by ChatGPT; we rank nowhere
  - ...and 32 more in work_queue.json

**7. Get onto pages AI cites that leave the Library out** (`ai:ask_to_be_added`, 2 items)
- How: Read the page. If it's a list of things to do or a travel guide that names nearby attractions, find the author or the update/contact link and ask to be added, with a two-sentence blurb (what the Library is, why it's worth the stop, about 3 1/2 hours) and a photo. Draft the note for approval; nothing goes out without it.
- Done when: The page names the Library (next weekly run re-reads it)
  - `https://mdhta.com`, other, cited in 2 answers; names Theodore Roosevelt National Park, Pitchfork Steak Fondue, Medora Musical, Maah Daah Hey Trail
  - `https://www.blackhillsbadlands.com/plan/itineraries/summer-scenic-drives-northern-hills`, other, cited in 1 answers; names Mount Rushmore, Theodore Roosevelt National Park, Painted Canyon

**8. Same title as another page** (`audit:title_duplicate`, 37 pages)
- How: Edit the node (/node/NID/edit) > 'Customize meta tags'. Basic tags: Page title '<title> | [site:name]' (page part 60 characters or fewer) and Description (120-155 characters). Set Open Graph og:title/og:description and Twitter card title/description to match. Save with 'Save' (keeps the moderation state). If the save seems to do nothing, look for a validation error further down the form.
- Done when: No other page has the same title
  - `/visit/exhibits/kennerly`, 2,854 impr., HELD (recently changed), title "In the Room: Sixty Years on the Front Lines of History" (54 chars), same as /calendar/daily-activity/room-sixty-years-front-lines-history, /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly
  - `/about/trustees/kermit-roosevelt`, 2,273 impr., HELD (recently changed), title "Kermit Roosevelt" (16 chars), same as /tr/people/kermit
  - `/tr/people/kermit`, 1,911 impr., HELD (recently changed), title "Kermit Roosevelt" (16 chars), same as /about/trustees/kermit-roosevelt
  - `/calendar/daily-activity/room-sixty-years-front-lines-history`, 1,765 impr., title "In the Room: Sixty Years on the Front Lines of History" (54 chars), same as /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf
  - `/project/native-plant-project`, 1,236 impr., HELD (recently changed), title "Native Plant Project" (20 chars), same as /video/view/1SqdaUrbU7U
  - `/about/trustees/douglas-brinkley`, 834 impr., HELD (recently changed), title "Douglas Brinkley" (16 chars), same as /podcast/good-citizen/douglas-brinkley
  - `/podcast/good-citizen/douglas-brinkley`, 754 impr., HELD (recently changed), title "Douglas Brinkley" (16 chars), same as /about/trustees/douglas-brinkley
  - `/events/teddycon`, 642 impr., HELD (recently changed), title "Theodore Roosevelt Convention (#TeddyCon)" (41 chars), same as /event/24
  - ...and 29 more in work_queue.json

**9. Strengthen pages ranking just off the top for searches people make** (`search:striking_distance`, 9 items)
- How: Open the page and make it the best answer to that exact search: use the search's words in the title or a heading, answer it plainly in the first paragraph, add the specifics people want (facts already on the site), and link to it from 2-3 related pages. Don't rewrite a page that already ranks in the top 3 for its main search.
- Done when: Average position for the search improves over the next 4 weeks (change log before/after)
  - `/tickets`, 1,646 impr., "roosevelt library" #4.3, move up from #4 to about #3, upside ~157 clicks/28d
  - `/quiz/muckrakers`, 2,447 impr., "muckrakers" #10.0, move up from #10 to about #5, upside ~143 clicks/28d
  - `/calendar/specialty-tour/architecture-and-sustainability-tour`, 2,385 impr., "theodore roosevelt presidential library" #9.7, move up from #10 to about #5, upside ~142 clicks/28d
  - `/tr/rise-to-power/rough-riders`, 814 impr., "rough riders" #6.5, move up from #6 to about #3, upside ~84 clicks/28d
  - `/tr/rise-to-power/rough-riders`, 750 impr., "who were the rough riders" #6.4, move up from #6 to about #3, upside ~80 clicks/28d
  - `/calendar/specialty-tour/architecture-and-sustainability-tour`, 1,125 impr., "teddy roosevelt library" #7.6, move up from #8 to about #5, upside ~65 clicks/28d
  - `/tr/rise-to-power/rough-riders/who-were-they`, 1,072 impr., "rough riders" #10.5, move up from #10 to about #5, upside ~62 clicks/28d
  - `/project/living-building-challenge`, 1,082 impr., "living building challenge" #7.0, move up from #7 to about #5, upside ~61 clicks/28d
  - ...and 1 more in work_queue.json

**10. Missing Open Graph tags** (`audit:og_missing`, 12 pages)
- How: Edit the node (/node/NID/edit) > 'Customize meta tags'. Basic tags: Page title '<title> | [site:name]' (page part 60 characters or fewer) and Description (120-155 characters). Set Open Graph og:title/og:description and Twitter card title/description to match. Save with 'Save' (keeps the moderation state). If the save seems to do nothing, look for a validation error further down the form.
- Done when: og:title and og:description are present
  - `/join-us`, 4,150 impr., HELD (recently changed)
  - `/visit/exhibits/kennerly`, 2,854 impr., HELD (recently changed)
  - `/visit/teddy-trail`, 832 impr., HELD (recently changed)
  - `/birthdaycard`, 25 impr.
  - `/project/how-the-library-works`, 13 impr.
  - `/rsvp/midwinter`
  - `/quiz/the-boardwalk`
  - `/quiz/badlands-family`
  - ...and 4 more in work_queue.json

**11. No meta description** (`audit:meta_missing`, 11 pages)
- How: Edit the node (/node/NID/edit) > 'Customize meta tags'. Basic tags: Page title '<title> | [site:name]' (page part 60 characters or fewer) and Description (120-155 characters). Set Open Graph og:title/og:description and Twitter card title/description to match. Save with 'Save' (keeps the moderation state). If the save seems to do nothing, look for a validation error further down the form.
- Done when: The page has a meta description of 120-155 characters
  - `/join-us`, 4,150 impr., HELD (recently changed)
  - `/visit/exhibits/kennerly`, 2,854 impr., HELD (recently changed)
  - `/birthdaycard`, 25 impr.
  - `/project/how-the-library-works`, 13 impr.
  - `/rsvp/midwinter`
  - `/quiz/the-boardwalk`
  - `/quiz/badlands-family`
  - `/quiz/badlands-wildlife-family`
  - ...and 3 more in work_queue.json

**12. No H1 heading** (`audit:h1_missing`, 29 pages)
- How: Open the page's Layout (/node/NID/layout). Make sure the top section shows the page title block (Content fields > Title), which renders as the H1; or change the first heading in the top text block to Heading 1. Save layout.
- Done when: Exactly one H1
  - `/tr/presidency/executive-actions/story`, 1,648 impr., no H1
  - `/visit/planner`, 1,533 impr., no H1
  - `/tr/presidency/executive-actions/action`, 1,301 impr., no H1
  - `/visit/maps/campus`, 760 impr., no H1
  - `/grand-opening/photos/july4`, 662 impr., no H1
  - `/grand-opening/photos/july2`, 487 impr., no H1
  - `/research/family-tree`, 155 impr., no H1
  - `/membership/neighbor`, 117 impr., no H1
  - ...and 21 more in work_queue.json

**15. Links that go through a redirect** (`links:via_redirect`, 72 items)
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

**18. Heading levels skip (e.g. H2 straight to H4)** (`audit:heading_skip`, 146 pages)
- How: Open the Layout. In the text blocks, change the heading levels so they step down one at a time (H2 under the page title, H3 under an H2). Headings used just for size should be styled text instead.
- Done when: Heading levels step down one at a time
  - `/podcast/good-citizen/senator-chris-murphy`, 146,075 impr.
  - `/`, 110,702 impr.
  - `/tr/presidency-timeline`, 54,306 impr.
  - `/podcast/good-citizen/karl-rove-historic-redemption-hard-work-politics-and-essential-nature`, 47,194 impr.
  - `/tr/timeline`, 42,853 impr.
  - `/visit/hours`, 37,341 impr.
  - `/project`, 27,833 impr.
  - `/podcast/good-citizen/bill-kristol`, 26,359 impr.
  - ...and 138 more in work_queue.json

**19. Related pages that don't link to each other** (`links:related`, 27 items)
- How: These two pages cover the same subject without linking to each other. Add one natural link each way, in the paragraph where the shared subject comes up.
- Done when: Each page links to the other
  - `/tr/family/family-tree`, 113,663 impr., <-> /tr/family/fdr-connection
  - `/tr/presidency-timeline`, 97,159 impr., <-> /tr/timeline
  - `/tr/complex-legacy/imperialism`, 66,255 impr., <-> /tr/rise-to-power/spanish-american-war
  - `/tr/post-presidency/bull-moose/platform`, 40,542 impr., <-> /tr/speeches/new-nationalism
  - `/tr/post-presidency/bull-moose/platform`, 40,165 impr., <-> /tr/speeches/confession-of-faith
  - `/tr/complex-legacy/imperialism`, 38,288 impr., <-> /tr/presidency/foreign-policy
  - `/tr/post-presidency/bull-moose`, 36,728 impr., <-> /tr/speeches/new-nationalism
  - `/tr/family/children`, 34,234 impr., <-> /tr/family/family-tree
  - ...and 19 more in work_queue.json

### Page jobs: everything to fix on one page, busiest pages first
| Page | Impr. | Fixes | Links to add | Markup |  |
|---|---|---|---|---|---|
| /podcast/good-citizen/senator-chris-murphy | 146075 | heading_skip, deep_page, meta_duplicate | [[high school]] -> /tr/for-educators/high-school; [[in the room]] -> /visit/exhibits/kennerly; [[step into the arena]] -> /vote | – |  |
| /tr/tr-mount-rushmore | 144374 | – | [[executive power]] -> /tr/presidency/executive-power | – | held |
| / | 110702 | heading_skip | [[Elkhorn Ranch]] -> /tr/badlands/elkhorn-ranch | – | held |
| /tr/family/fdr-connection | 90214 | – | [[Assistant Secretary of the Navy]] -> /tr/rise-to-power/assistant-navy-secretary | – | held |
| /tickets | 59224 | title_too_short | – | – |  |
| /tr/presidency-timeline | 54306 | heading_skip | [[Nobel Peace Prize]] -> /tr/presidency/nobel-peace-prize | – | held |
| /tr/pre-presidency-political-accomplishments | 53709 | – | [[Civil War]] -> /tr/early-life/civil-war; [[Naval War of 1812]] -> /tr/new-york-politics/naval-war-of-1812 | – | held |
| /visit | 53667 | – | [[Badlands landscape]] -> /tr/badlands/landscape | – | held |
| /podcast/good-citizen/karl-rove-historic-redemption-hard-work-politics-and-essential-nature | 47194 | heading_skip, deep_page | [[Civil War]] -> /tr/early-life/civil-war | – | held |
| /visit/directions | 43869 | – | [[Little Missouri River]] -> /visit/little-missouri-river | – | held |
| /tr/timeline | 42853 | heading_skip | [[William Howard Taft]] -> /tr/people/william-howard-taft; [[River of Doubt]] -> /tr/post-presidency/river-of-doubt; [[Edith Roosevelt]] -> /tr/rise-to-power/edith-roosevelt | – | held |
| /bullet-speech | 39927 | deep_page, h1_multiple | [[frequently asked questions]] -> /visit/faq | – | held |
| /tr/tr-importance | 38748 | – | [[national forests]] -> /tr/presidency/conservation/national-forests; [[Leonard Wood]] -> /tr/people/leonard-wood; [[Theodore Roosevelt National Park]] -> /tr/homes-and-places/tr-national-park | – | held |
| /visit/hours | 37341 | heading_skip | – | – | held |
| /tr/presidency/bully-pulpit | 36561 | – | [[Doris Kearns Goodwin]] -> /podcast/good-citizen/doris-kearns-goodwin-presidential-stories-trpl-and-enduring-lessons-theodore | – | held |

### Waiting on FiveJars or blocked (already ticketed; check whether they've landed, don't re-ask)
- Sitewide markup doesn't link to the Library's Wikipedia entry (`schema:sitewide:sameas`): blocked, the per-page sameAs field is capped at 255 characters; FiveJars asked to raise it. Wikidata is in place; Wikipedia and Bluesky go back in once it's raised
- No admission information in the markup (`schema:sitewide:admission`)
- TR history section pages: add CollectionPage markup (template, all pages at once) (`schema:tr_hubs`)
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
| audit | ok | 2026-11-09T12:32:33+00:00 | Crawled 1135 pages, health 95/100 |
| ranks | ok | 2026-11-09T12:38:04+00:00 | 35 keywords checked |
| opportunities | ok | 2026-11-12T13:25:30+00:00 | 9 striking-distance queries, 4 low-CTR pages; 143 recently changed pages held back |
| gsc | ok | 2026-11-12T13:25:29+00:00 | 22624 queries, 2300 pages (2026-10-13 to 2026-11-09); 263 changed pages tracked |
| ai_visibility | error | 2026-11-09T12:43:57+00:00 | 42 answers from ChatGPT, Gemini, Perplexity; 21 failed: Perplexity 403: {"error":{"message":"The Agent API requires paid credits. Add paid credit at https://console.perplexity.ai to upgrade your organizatio |
| tips | ok | 2026-11-09T13:03:11+00:00 | Gemini wrote tips for 8 pages |
| digest | ok | 2026-11-11T13:28:28+00:00 | llms.txt, digest.md and digest.json rebuilt |
| checkout | ok | 2026-11-12T13:25:59+00:00 | Checkout completion n/a; steps not tracked: view_item, add_to_cart, begin_checkout, add_payment_info |
| curate | ok | 2026-11-09T12:33:22+00:00 | 15 discovered keywords and 6 discovered questions tracked; 7 changes today |
| ux | ok | 2026-11-09T12:57:05+00:00 | 80 pages; PageSpeed on 78; AI task check by gemini (gemini-3.8-flash); GA4 on; Clarity off; 2 errors, e.g. PageSpeed /visit/maps: PageSpeed 500: {   "error": {     "code": 500,     "message": "Lighthouse returned error: PAGE_HUNG. Lighthouse was unable to reliably load the URL you requeste |
| links | ok | 2026-11-09T12:58:43+00:00 | 1169 pages crawled; 0 broken internal links (redirects proposed); 746 suggested links; 45 orphan pages; 27 related pairs without links |
| schema | ok | 2026-11-09T13:00:05+00:00 | 292/888 content pages have their own markup; 6 sitewide issues |
| indexnow | skipped | 2026-11-12T13:25:59+00:00 | No IndexNow key yet: see the work queue task 'Turn on IndexNow'. |

## Google Search (Search Console)
2026-10-13 to 2026-11-09 vs the prior 28 days: **42,010 clicks** (prior 52,419), 2,780,655 impressions (prior 2,356,487), CTR 1.5% (prior 2.2%), average position 5.8 (prior 6.5). Branded clicks 11958, non-branded 10239, search term hidden by Google 19813.

### Top non-branded searches (people who didn't search our name)
| Search | Clicks | Impr. | Pos. |
|---|---|---|---|
| brownsville affair | 1 | 116995 | 4.9 |
| chris murphy | 7 | 68690 | 12.2 |
| square deal | 146 | 63469 | 3.4 |
| karl rove | 49 | 38809 | 9 |
| roosevelt corollary | 55 | 23423 | 4.1 |
| senator chris murphy | 8 | 22664 | 13 |
| jacob riis | 130 | 22253 | 9.6 |
| bill kristol | 8 | 20233 | 11.6 |
| chris murphy senator | 10 | 18036 | 12.6 |
| theodore roosevelt | 53 | 13684 | 7.4 |
| theo elections | 4 | 13356 | 6.7 |
| bully pulpit | 31 | 11262 | 3 |
| alice roosevelt | 51 | 10518 | 7.6 |
| mount rushmore presidents | 33 | 9481 | 4.4 |
| kermit roosevelt | 34 | 9183 | 7.6 |
| bull moose party | 63 | 8944 | 3.4 |
| the man in the arena | 134 | 8704 | 5.8 |
| man in the arena | 51 | 8449 | 6.6 |
| sen chris murphy | 6 | 8135 | 10.7 |
| alice roosevelt longworth | 11 | 7494 | 8.4 |
| senator murphy | 3 | 6758 | 12.4 |
| alice hathaway lee roosevelt | 11 | 5997 | 5.9 |
| teddy roosevelt | 39 | 5989 | 6.4 |
| who is on mount rushmore | 7 | 5931 | 6.9 |
| henry cabot lodge | 6 | 5922 | 7.1 |

### Top pages
| Page | Clicks | Prior | Impr. | Pos. |
|---|---|---|---|---|
| / | 7251 | 11263 | 78037 | 7.2 |
| /?utm_source=gbp&utm_medium=organic | 4441 | 2216 | 30137 | 3.9 |
| /tickets | 2509 | 6739 | 52106 | 3.1 |
| /tr/family/fdr-connection | 1796 | 951 | 90214 | 3.1 |
| /tr/presidency/trust-busting | 1148 | 785 | 77950 | 3.3 |
| /visit | 1144 | 2518 | 53663 | 2.7 |
| /tr/presidency/square-deal | 1003 | 406 | 113951 | 3.9 |
| /tr/speeches/man-in-the-arena | 985 | 297 | 41517 | 5.3 |
| /tickets?utm_source=gbp&utm_medium=organic | 893 | 8115 | 7118 | 3.7 |
| /bullet-speech | 677 | 725 | 39927 | 3.7 |
| /tr/square-deal | 643 | 1132 | 87232 | 3.9 |
| /tr/quotes | 581 | 702 | 24411 | 8.7 |
| /tr/people/jacob-riis | 547 | 320 | 84730 | 6.4 |
| /tr/presidency/ten-facts | 518 | 194 | 16064 | 3.8 |
| /tr/pre-presidency-political-accomplishments | 505 | 583 | 53709 | 5.6 |
| /tr/tr-mount-rushmore | 467 | 782 | 144374 | 5.6 |
| /visit/directions | 454 | 1016 | 43869 | 2.8 |
| /tr/rise-to-power/san-juan-hill | 426 | 269 | 32063 | 3.6 |
| /visit/hours | 407 | 929 | 37341 | 2.3 |
| /tr/presidency/panama-canal | 401 | 107 | 69951 | 4.9 |
| /tr/family/family-tree | 387 | 281 | 23449 | 5.7 |
| /tr/presidency/roosevelt-corollary | 376 | 146 | 143745 | 4.4 |
| /tr/fake-quotes | 347 | 383 | 14746 | 6.5 |
| /tr/tr-importance | 342 | 336 | 38745 | 4.9 |
| /tr/presidency-timeline | 332 | 324 | 54306 | 4.4 |

## Opportunities (ranked)
_Upside is sized against a realistic next step (a few places up, not #1), minus the clicks the page already gets, using a rough industry click-through curve; overlapping searches for one page aren't added twice. Use it to rank opportunities, never as a forecast, and say how the gain would happen: a new ranking, a higher position, or more clicks at the same position._

### Striking distance: ranking 4-20 with demand; strengthen the page for the exact search
| Search | Page | Pos. | Impr. | How | Upside |
|---|---|---|---|---|---|
| roosevelt library | /tickets | 4.3 | 1646 | move up from #4 to about #3 | 157 |
| muckrakers | /quiz/muckrakers | 10 | 2447 | move up from #10 to about #5 | 143 |
| theodore roosevelt presidential library | /calendar/specialty-tour/architecture-and-sustainability-tour?source=ev | 9.7 | 2385 | move up from #10 to about #5 | 142 |
| rough riders | /tr/rise-to-power/rough-riders | 6.5 | 814 | move up from #6 to about #3 | 84 |
| who were the rough riders | /tr/rise-to-power/rough-riders | 6.4 | 750 | move up from #6 to about #3 | 80 |
| teddy roosevelt library | /calendar/specialty-tour/architecture-and-sustainability-tour?source=ev | 7.6 | 1125 | move up from #8 to about #5 | 65 |
| rough riders | /tr/rise-to-power/rough-riders/who-were-they | 10.5 | 1072 | move up from #10 to about #5 | 62 |
| living building challenge | /project/living-building-challenge | 7 | 1082 | move up from #7 to about #5 | 61 |
| who were the rough riders | /tr/rise-to-power/rough-riders/who-were-they | 4.8 | 596 | move up from #5 to about #3 | 61 |

### Ranking well but skipped: rewrite title/meta description
| Page | Pos. | CTR | Typical | Upside |
|---|---|---|---|---|
| /tickets | 3.1 | 4.8% | 11.0% | 3220 |
| /tr/rise-to-power/rough-riders | 6.4 | 0.3% | 4.5% | 543 |
| /tr/presidency/foreign-policy | 4.7 | 0.6% | 6.0% | 512 |
| /tr/presidency/nobel-peace-prize | 4.6 | 0.6% | 6.0% | 436 |

### Search words missing from the ranking page's title
| Search | Page | Current title | Missing | Impr. |
|---|---|---|---|---|
| ed o'keefe | /about/trustees/edward-okeefe | Edward O’Keefe / Theodore Roosevelt Presidential Library | ed, o'keefe | 648 |
| enchanted highway north dakota | /visit/itineraries/enchanted-highway | The Enchanted Highway: Giants on the Prairie / Theodore Roosevelt Presidential Library | north, dakota | 510 |
| tr library | /tickets | Tickets / Theodore Roosevelt Presidential Library | tr | 348 |

### Losing clicks vs prior 28 days (check seasonality first)
| Type | Search/page | Clicks | Prior | Change |
|---|---|---|---|---|
| page | /tickets?utm_source=gbp&utm_medium=organic | 893 | 8115 | -89.0% |
| page | /tickets | 2509 | 6739 | -62.8% |
| query | theodore roosevelt presidential library | 4356 | 8495 | -48.7% |
| page | / | 7251 | 11263 | -35.6% |
| query | teddy roosevelt presidential library | 1556 | 3241 | -52.0% |
| page | /visit | 1144 | 2518 | -54.6% |
| query | teddy roosevelt library | 1448 | 2768 | -47.7% |
| query | theodore roosevelt library | 929 | 1807 | -48.6% |
| page | /visit/directions | 454 | 1016 | -55.3% |
| page | /visit/hours | 407 | 929 | -56.2% |
| page | /tr/square-deal | 643 | 1132 | -43.2% |
| page | /tr/tr-mount-rushmore | 467 | 782 | -40.3% |
| query | roosevelt presidential library | 237 | 523 | -54.7% |
| query | roosevelt library | 192 | 464 | -58.6% |
| query | roosevelt library north dakota | 246 | 429 | -42.7% |

### Our pages competing for the same search
| Search | Impr. | Pages |
|---|---|---|
| square deal | 88445 | /tr/square-deal (pos 4.6), /tr/presidency/square-deal (pos 4.3) |
| theodore roosevelt | 14774 | /tr/timeline (pos 4.6), / (pos 12.9), /bullet-speech (pos 3.0), /tr/family/fdr-connection (pos 3.0) |
| roosevelt library | 5396 | /tickets (pos 4.3), / (pos 3.5), /visit (pos 3.2), /visit/directions (pos 3.7) |
| the square deal | 3387 | /tr/square-deal (pos 2.4), /tr/presidency/square-deal (pos 4.5) |
| teddy roosevelt museum | 2999 | / (pos 1.7), /tickets (pos 2.1), /visit (pos 2.2), /visit/hours (pos 2.5) |
| martha bulloch roosevelt | 2751 | /tr/early-life/mother (pos 3.2), /tr/people/mittie (pos 7.6) |
| what was the square deal | 2441 | /tr/square-deal (pos 1.4), /tr/presidency/square-deal (pos 2.2) |
| square deal definition | 1955 | /tr/square-deal (pos 2.3), /tr/presidency/square-deal (pos 1.4) |
| bamie roosevelt | 1915 | /tr/early-life/siblings (pos 7.0), /tr/people/bamie (pos 6.8), /tr/people (pos 14.7), /tr/new-york-politics/double-tragedy (pos 5.8) |
| presidential library medora | 1904 | / (pos 1.2), /visit (pos 1.7), /tickets (pos 1.8), /visit/hours (pos 1.8) |
| rough riders | 1886 | /tr/rise-to-power/rough-riders/who-were-they (pos 10.5), /tr/rise-to-power/rough-riders (pos 6.5) |
| teddy roosevelt shot | 1828 | /tr/tr-shot (pos 2.7), /bullet-speech (pos 4.4) |
| when did theodore roosevelt die | 1433 | /tr/timeline (pos 4.6), /tr/post-presidency/death (pos 7.2) |
| theodore franklin | 1393 | /tr/family/family-tree (pos 6.6), /tr/family/fdr-connection (pos 6.0) |
| theodore roosevelt museum | 1350 | / (pos 1.7), /tickets (pos 2.2), /visit (pos 2.1), /?utm_source=gbp&utm_medium=organic (pos 1.6) |

## Tracked keywords (dataforseo+gsc)
| Keyword | Group | Volume | GSC pos. | Google rank | AI Overview | Cites us | Above us |
|---|---|---|---|---|---|---|---|
| theodore roosevelt presidential library | Visit | 74000 | 1.2 | – | False | False | google.com, google.com, google.com |
| things to do in medora nd | Visit | 1600 | 2.2 | – | False | False | google.com, google.com, google.com |
| medora north dakota attractions | Visit | 1600 | – | – | False | False | google.com, google.com, google.com |
| things to do near theodore roosevelt national park | Visit | 50 | 1 | – | True | False | google.com, google.com, google.com |
| museums in north dakota | Visit | 320 | 4.6 | – | False | False | google.com, google.com, google.com |
| north dakota road trip | Visit | 140 | 7.9 | – | True | False | google.com, google.com, google.com |
| medora nd hotels | Visit | 8100 | 5.4 | – | False | False | google.com, google.com, google.com |
| badlands north dakota | Visit | 5400 | 10 | – | True | False | google.com, google.com, google.com |
| theodore roosevelt | History | 246000 | 7.4 | – | False | False | google.com, google.com, google.com |
| theodore roosevelt north dakota | History | 320 | 6.4 | – | False | False | google.com, google.com, google.com |
| theodore roosevelt badlands | History | 140 | 8.9 | – | True | True | google.com, google.com, google.com |
| elkhorn ranch | History | 2900 | 8.9 | – | True | False | google.com, google.com, google.com |
| maltese cross cabin | History | 720 | 45 | – | True | False | google.com, google.com, google.com |
| theodore roosevelt conservation | History | 590 | 7.2 | – | True | False | google.com, google.com, google.com |
| presidential libraries | Presidential libraries | 14800 | 5.2 | – | False | False | google.com, google.com, google.com |
| newest presidential library | Presidential libraries | 210 | 1.7 | – | True | False | google.com, google.com, google.com |
| presidential library road trip | Presidential libraries | – | – | – | True | False | google.com, google.com, google.com |
| theodore roosevelt quotes | Learning | 6600 | 3.2 | – | True | True | google.com, google.com, google.com |
| theodore roosevelt man in the arena | Learning | 2400 | 4.8 | – | True | False | google.com, google.com, google.com |
| theodore roosevelt podcast | Learning | 10 | – | – | True | True | google.com, google.com, google.com |
| teddy roosevelt national park | Auto: Visit | 8100 | 9.8 | – | False | False | google.com, google.com, google.com |
| enchanted highway | Auto: Visit | 9900 | 8.4 | – | True | False | google.com, google.com, google.com |
| mount rushmore presidents | Auto: Visit | 27100 | 4.5 | – | True | True | google.com, google.com, google.com |
| teddy roosevelt | Auto: History | 165000 | 6.2 | – | False | False | google.com, google.com, google.com |
| theodore roosevelt died | Auto: History | 5400 | 4.8 | – | True | False | google.com, google.com, google.com |
| brownsville affair | Auto: History | 480 | 5.1 | – | True | False | google.com, google.com, google.com |
| roosevelt corollary | Auto: History | 33100 | 4.2 | – | True | True | google.com, google.com, google.com |
| jacob riis | Auto: History | 33100 | 9.7 | – | False | False | google.com, google.com, google.com |
| alice roosevelt longworth | Auto: Family | 27100 | 8.5 | – | False | False | google.com, google.com, google.com |
| bull moose party | Auto: History | 9900 | 3.7 | – | True | True | google.com, google.com, google.com |
| alice roosevelt | Auto: Family | 27100 | 8.1 | – | False | False | google.com, google.com, google.com |
| man in the arena | Auto: Learning | 18100 | 6.1 | – | True | False | google.com, google.com, google.com |
| kermit roosevelt | Auto: Family | 12100 | 7.4 | – | False | False | google.com, google.com, google.com |
| who is on mount rushmore | Auto: Learning | 18100 | 6.7 | – | True | False | google.com, google.com, google.com |
| quentin roosevelt | Auto: Family | 9900 | 11.2 | – | False | False | google.com, google.com, google.com |

## AI assistant visibility
| Engine | Model | Mentions us | Cites trlibrary.com |
|---|---|---|---|
| ChatGPT | gpt-5-mini | 38.1% | 28.6% |
| Gemini | gemini-3.8-flash | 23.8% | 19.0% |
| Perplexity | fast | – | – |

### Question by question
Some answers failed this week: perplexity: Perplexity 403: {"error":{"message":"The Agent API requires paid credits. Add paid credit at https://console.perplexity.ai to upgrade your o

**I'm visiting Theodore Roosevelt National Park. What else should I see nearby?** (Trip planning)
- ChatGPT: mentioned, #5 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Chateau de Mores, North Dakota Cowboy Hall of Fame, Medora Musical, Elkhorn Ranch, Maah Daah Hey Trail. Described as: "- Theodore Roosevelt Presidential Library (new facility near Medora with exhibits about TR and the badlands). … ([trlibrary.com](https://www.trlibrary.com/visit/activities?utm_source=openai))" Sources: medorand.org, trlibrary.com, parkplanning.nps.gov, en.wikipedia.org, ndtourism.com, visitdickinson.com
- Gemini: NOT mentioned. Also named: Theodore Roosevelt National Park, Medora Musical, Pitchfork Steak Fondue, North Dakota Cowboy Hall of Fame, Maah Daah Hey Trail, Elkhorn Ranch. Sources: none

**What are the best things to do in Medora, North Dakota?** (Trip planning)
- ChatGPT: mentioned, #5 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Painted Canyon, Medora Musical, Pitchfork Steak Fondue, Chateau de Mores, North Dakota Cowboy Hall of Fame, Maltese Cross Cabin, Maah Daah Hey Trail. Described as: "4) Visit the Theodore Roosevelt Presidential Library … ([trlibrary.com](https://www.trlibrary.com/visit/activities?utm_source=openai))" Sources: nps.gov, medora.com, trlibrary.com, history.nd.gov, home.nps.gov
- Gemini: NOT mentioned. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Medora Musical, Pitchfork Steak Fondue, Chateau de Mores, North Dakota Cowboy Hall of Fame, Maah Daah Hey Trail. Sources: none

**Plan a 3-day road trip through western North Dakota. What are the must-see stops?** (Trip planning)
- ChatGPT: NOT mentioned. Also named: Theodore Roosevelt National Park, Painted Canyon, North Dakota Cowboy Hall of Fame, Pitchfork Steak Fondue, Medora Musical, Maah Daah Hey Trail. Sources: nps.gov, discovermedora.com, mdhta.com, ndtourism.com
- Gemini: NOT mentioned. Also named: Painted Canyon, Chateau de Mores, North Dakota Cowboy Hall of Fame, Pitchfork Steak Fondue, Medora Musical, Theodore Roosevelt National Park, Maltese Cross Cabin. Sources: none

**We're driving from Mount Rushmore to Theodore Roosevelt National Park. What's worth stopping for?** (Trip planning)
- ChatGPT: NOT mentioned. Also named: Mount Rushmore, Theodore Roosevelt National Park, Painted Canyon. Sources: gfp.sd.gov, crazyhorsememorial.org, blackhillsbadlands.com, travelsouthdakota.com, home.nps.gov, visitrapidcity.com
- Gemini: NOT mentioned. Also named: Mount Rushmore, Theodore Roosevelt National Park, Medora Musical. Sources: none

**What are the best stops along I-94 in North Dakota?** (Trip planning)
- ChatGPT: NOT mentioned. Also named: Theodore Roosevelt National Park, Painted Canyon, Medora Musical. Sources: home.nps.gov, ndtourism.com, dickinsongov.com, atlasobscura.com, statemuseum.nd.gov, maps.roadtrippers.com
- Gemini: NOT mentioned. Also named: Painted Canyon, Theodore Roosevelt National Park, Maltese Cross Cabin, Chateau de Mores, Medora Musical, Pitchfork Steak Fondue. Sources: none

**Fun things to do with kids in the North Dakota Badlands?** (Trip planning)
- ChatGPT: NOT mentioned. Also named: Theodore Roosevelt National Park, Pitchfork Steak Fondue, Medora Musical, Maah Daah Hey Trail. Sources: nps.gov, ndtourism.com, discovermedora.com, foundation.medora.com, mdhta.com, visitdickinson.com
- Gemini: NOT mentioned. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Painted Canyon, Medora Musical, Pitchfork Steak Fondue, North Dakota Cowboy Hall of Fame. Sources: none

**What can we do indoors in Medora if the weather is bad?** (Trip planning)
- ChatGPT: NOT mentioned. Also named: Theodore Roosevelt National Park. Sources: none
- Gemini: NOT mentioned. Also named: North Dakota Cowboy Hall of Fame, Chateau de Mores, Theodore Roosevelt National Park. Sources: medorand.org, medora.com, discovermedora.com, nd.gov, wanderlog.com, perceptionillusion.com

**What are the best museums in North Dakota?** (Museums)
- ChatGPT: NOT mentioned. Also named: North Dakota Cowboy Hall of Fame, Theodore Roosevelt National Park, Chateau de Mores. Sources: history.nd.gov, plainsart.org, ndmoa.com, bonanzaville.org, ndtourism.com, dakotaterritoryairmuseum.com
- Gemini: NOT mentioned. Also named: North Dakota Cowboy Hall of Fame. Sources: none

**What is the newest presidential library in the United States?** (Museums)
- ChatGPT: mentioned, #1 among attractions. Described as: "Short answer: the Theodore Roosevelt Presidential Library in Medora, North Dakota — it opened July 4, 2026." Sources: morningstar.com, cbsnews.com, smu.edu
- Gemini: mentioned, #1 among attractions. Also named: Theodore Roosevelt National Park. Described as: "* **Theodore Roosevelt Presidential Library (Medora, North Dakota):** Opened to the public on **July 4, 2026**." Sources: youtube.com, wikipedia.org, cbsnews.com

**Which presidential libraries are worth visiting?** (Museums)
- ChatGPT: mentioned, #1 among attractions. Described as: "Roosevelt Presidential Library & Museum — Hyde Park, NY" Sources: none
- Gemini: mentioned, #1 among attractions. Described as: "Roosevelt Presidential Library and Museum** *(Hyde Park, New York)*" Sources: none

**Where can I learn about Theodore Roosevelt's life in North Dakota?** (History)
- ChatGPT: mentioned, #4 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Elkhorn Ranch, Maltese Cross Cabin, Chateau de Mores, Medora Musical. Described as: "- Theodore Roosevelt Presidential Library (Medora) — a new, immersive museum in Medora with exhibits about Roosevelt’s Dakota years and later life. … ([trlibrary.com](https://www.trlibrary.com/?utm_source=openai))" Sources: home.nps.gov, nps.gov, theodorerooseveltcenter.org, trlibrary.com, statemuseum.nd.gov, medora.com
- Gemini: mentioned, #4 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Elkhorn Ranch, Chateau de Mores. Described as: "* **Theodore Roosevelt Presidential Library (Medora, ND)**" Sources: trlibrary.com, prnewswire.com, discovermedora.com, nd.gov, theodorerooseveltcenter.org, ndtourism.com

**What historic sites are connected to Theodore Roosevelt?** (History)
- ChatGPT: NOT mentioned. Also named: Theodore Roosevelt National Park, Elkhorn Ranch, Maltese Cross Cabin. Sources: none
- Gemini: NOT mentioned. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin, Elkhorn Ranch, Mount Rushmore. Sources: none

**Is the Theodore Roosevelt Presidential Library worth visiting?** (Brand)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Maltese Cross Cabin. Described as: "Short answer: Yes—most visitors and major reviewers say the Theodore Roosevelt Presidential Library (opened July 4, 2026) is worth a stop, especially if you care about Theodore Roosevelt, conservation history, striking architecture, or are already visiting Theodore Roosevelt National Park. … ([trlibrary.com](https://www.trlibrary.com/visit/faq/during-your-visit?utm_source=openai))" Sources: snohetta.com, trlibrary.com, peacegardenalmanac.com, monorepo-sample1.nyt.net
- Gemini: mentioned, #1 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park, Maah Daah Hey Trail, Medora Musical. Described as: "Whether the **Theodore Roosevelt Presidential Library** is worth visiting depends largely on your travel style and interests, but for most travelers—especially history enthusiasts, architecture fans, and national park visitors—**it is well worth the trip.**" Sources: ndtourism.com, medora.com, ap.org, visitdickinson.com, cnn.com, trlibrary.com

**How much time do I need at the Theodore Roosevelt Presidential Library?** (Brand)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Described as: "([trlibrary.com](https://www.trlibrary.com/visit/faq)) … ([trlibrary.com](https://www.trlibrary.com/visit/faq))" Sources: peacegardenalmanac.com, trlibrary.com
- Gemini: mentioned, #1 among attractions, cites trlibrary.com. Also named: Theodore Roosevelt National Park. Described as: "You should plan to spend about **3.5 to 4 hours** at the Theodore Roosevelt Presidential Library in Medora, North Dakota." Sources: trlibrary.com, medora.com, nd.gov, cnn.com, visitdickinson.com, ndtourism.com

**How much are tickets to the Theodore Roosevelt Presidential Library and when is it open?** (Brand)
- ChatGPT: mentioned, #1 among attractions, cites trlibrary.com. Described as: "([trlibrary.com](https://www.trlibrary.com/tickets)) … ([trlibrary.com](https://www.trlibrary.com/visit/hours))" Sources: trlibrary.com
- Gemini: NOT mentioned. Sources: trlibrary.com

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

**What years was Theodore Roosevelt president, and what were the dates of his administration?** (Auto: History)
- ChatGPT: NOT mentioned. Sources: none
- Gemini: NOT mentioned. Sources: none

**Which four presidents are on Mount Rushmore, and why was Theodore Roosevelt included among them?** (Auto: History)
- ChatGPT: NOT mentioned. Also named: Mount Rushmore. Sources: none
- Gemini: NOT mentioned. Also named: Mount Rushmore. Sources: none

### Sites AI assistants cite most
trlibrary.com (10), ndtourism.com (9), nps.gov (6), medora.com (6), discovermedora.com (5), visitdickinson.com (4), home.nps.gov (4), nd.gov (4), medorand.org (2), history.nd.gov (2), mdhta.com (2), dickinsongov.com (2), statemuseum.nd.gov (2), cbsnews.com (2), theodorerooseveltcenter.org (2)

### Searches the assistants ran before answering
Searches the assistants ran before answering. 'Google' is trlibrary.com's Search Console position for the same search (last 28 days); none means the site doesn't show for it, or too rarely to report. A search we don't rank for is a page to strengthen or write. 127 different searches: we rank top 10 for 1, lower for 1, not at all for 125.

| Search the assistant ran | Engines | In answers missing us | trlibrary.com in Google |
|---|---|---|---|
| Badlands Dinosaur Museum Dickinson North Dakota family activities | ChatGPT | 1 | – |
| Badlands National Park NPS scenic drive Ben Reifel Visitor Center official site | ChatGPT | 1 | – |
| Badlands National Park scenic loop Wall Drug Minuteman Missile National Historic Site official sites | ChatGPT | 1 | – |
| Bismarck North Dakota Heritage Center & State Museum hours location 'Exit 159' I-94 'ND Heritage Center' | ChatGPT | 1 | – |
| Bonanzaville West Fargo museum website | ChatGPT | 1 | – |
| Crazy Horse Memorial visitor center hours Crazy Horse official site | ChatGPT | 1 | – |
| Custer State Park Wildlife Loop Sylvan Lake Needles Highway official site | ChatGPT | 1 | – |
| Deadwood South Dakota historic main street attractions Deadwood tourism official site | ChatGPT | 1 | – |
| Dickinson Museum Center 'I-94' 'Dickinson ND' attractions 'Badlands Dinosaur Museum' 'Joachim Museum' 'Prairie Outpost' | ChatGPT | 1 | – |
| Dickinson Museum Center Dickinson ND attractions | ChatGPT | 1 | – |
| Enchanted Highway Regent North Dakota location how to get from Medora distance | ChatGPT | 1 | – |
| Enchanted Highway Regent North Dakota official site | ChatGPT | 1 | – |
| Enchanted Highway distance from I-94 Regent North Dakota | ChatGPT | 1 | – |
| Enchanted Highway official site North Dakota tourism 'Enchanted Highway' site | ChatGPT | 1 | – |
| Fort Abraham Lincoln State Park On-A-Slant Indian Village Museum McLean County site | ChatGPT | 1 | – |
| Fort Union Trading Post National Historic Site Williston NPS | ChatGPT | 1 | – |
| Is Theodore Roosevelt National Park an International Dark Sky Park 'International Dark-Sky Association' Theodore Roosevelt | ChatGPT | 1 | – |
| Jamestown World's Largest Buffalo Dakota Thunder National Buffalo Museum Frontier Village 'Jamestown ND' 'I-94' 'exit' | ChatGPT | 1 | – |
| Knife River Indian Villages National Historic Site NPS location and attractions | ChatGPT | 1 | – |
| Little Missouri National Grassland North Dakota BLM | ChatGPT | 1 | – |

### Pages AI cites when it leaves the Library out
Pages cited in answers that left the Library out. 'Mentions the Library' comes from reading the page once (blank = not read or couldn't be read). A list that names other attractions but not the Library is the cheapest fix: ask to be added. 29 answers left the Library out. Citations by type: other 27, reference 20, partner 13, list or guide 2, attraction 1, owned 1.

| Page | Type | Answers | Mentions the Library | Attractions it helped name |
|---|---|---|---|---|
| https://www.ndtourism.com/regent/attractions-entertainment/family-fun/enchanted-highway | partner | 3 | – | Theodore Roosevelt National Park, Painted Canyon, Medora Musical, North Dakota Cowboy Hall of Fame |
| https://mdhta.com | other | 2 | NO | Theodore Roosevelt National Park, Pitchfork Steak Fondue, Medora Musical, Maah Daah Hey Trail |
| https://www.nps.gov/npgallery/GetAsset/257b1284-d776-43d5-9a8f-863023a2e520 | reference | 2 | – | Theodore Roosevelt National Park, Painted Canyon, North Dakota Cowboy Hall of Fame, Pitchfork Steak Fondue |
| https://www.nps.gov/thro/planyourvisit/south-unit.htm | reference | 1 | NO | Theodore Roosevelt National Park, Painted Canyon, North Dakota Cowboy Hall of Fame, Pitchfork Steak Fondue |
| https://discovermedora.com/do | other | 1 | yes | Theodore Roosevelt National Park, Painted Canyon, North Dakota Cowboy Hall of Fame, Pitchfork Steak Fondue |
| https://www.ndtourism.com/dickinson/attractions-entertainment/educational-attractions/dickinson-museum-center | partner | 1 | – | Theodore Roosevelt National Park, Painted Canyon, North Dakota Cowboy Hall of Fame, Pitchfork Steak Fondue |
| https://www.nps.gov/knri/planyourvisit/basicinfo.htm | reference | 1 | NO | Theodore Roosevelt National Park, Painted Canyon, North Dakota Cowboy Hall of Fame, Pitchfork Steak Fondue |
| https://www.nps.gov/fous | reference | 1 | NO | Theodore Roosevelt National Park, Painted Canyon, North Dakota Cowboy Hall of Fame, Pitchfork Steak Fondue |
| https://www.ndtourism.com/8-ways-be-awed-enchanted-highway | partner | 1 | – | Theodore Roosevelt National Park, Painted Canyon, North Dakota Cowboy Hall of Fame, Pitchfork Steak Fondue |
| https://www.nps.gov/thro/planyourvisit/cottonwood-campground.htm?fullweb=1 | reference | 1 | NO | Theodore Roosevelt National Park, Painted Canyon, North Dakota Cowboy Hall of Fame, Pitchfork Steak Fondue |
| https://www.nps.gov/thro/planyourvisit/juniper-campground.htm | reference | 1 | NO | Theodore Roosevelt National Park, Painted Canyon, North Dakota Cowboy Hall of Fame, Pitchfork Steak Fondue |
| https://www.nps.gov/yell/planyourvisit/safety-press.htm | reference | 1 | NO | Theodore Roosevelt National Park, Painted Canyon, North Dakota Cowboy Hall of Fame, Pitchfork Steak Fondue |
| https://gfp.sd.gov/parks/detail/custer-state-park | reference | 1 | NO | Mount Rushmore, Theodore Roosevelt National Park, Painted Canyon |
| https://crazyhorsememorial.org/visit/plan-your-visit | attraction | 1 | – | Mount Rushmore, Theodore Roosevelt National Park, Painted Canyon |
| https://www.blackhillsbadlands.com/plan/itineraries/summer-scenic-drives-northern-hills | other | 1 | NO | Mount Rushmore, Theodore Roosevelt National Park, Painted Canyon |
| https://www.travelsouthdakota.com/iconic-landmarks/deadwood/things-to-do | list or guide | 1 | – | Mount Rushmore, Theodore Roosevelt National Park, Painted Canyon |
| https://home.nps.gov/badl/planyourvisit/scenic-driving.htm | reference | 1 | – | Mount Rushmore, Theodore Roosevelt National Park, Painted Canyon |
| https://www.visitrapidcity.com/plan-your-trip/sample-itineraries/badlands-western-plains | other | 1 | – | Mount Rushmore, Theodore Roosevelt National Park, Painted Canyon |
| https://www.nps.gov/mimi/planyourvisit/directions.htm | reference | 1 | – | Mount Rushmore, Theodore Roosevelt National Park, Painted Canyon |
| https://home.nps.gov/thro/planyourvisit/car.htm | reference | 1 | – | Theodore Roosevelt National Park, Painted Canyon, Medora Musical |

**Ask to be added** (cited by AI, lists other things, doesn't mention the Library):
- https://mdhta.com (other; cited in 2 answers)
- https://www.blackhillsbadlands.com/plan/itineraries/summer-scenic-drives-northern-hills (other; cited in 1 answers)

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
Crawled 1135 of 1174 sitemap URLs. Health 95/100, AI readiness 60/100. llms.txt on trlibrary.com: yes. AI crawlers blocked in robots.txt: none. 405 pages have page-specific structured data (sitewide on every page: BreadcrumbList, EntryPoint, GeoCoordinates, ImageObject, ListItem, OpeningHoursSpecification, PostalAddress, SearchAction, WebSite).

| Severity | Issue | Pages | Examples |
|---|---|---|---|
| medium | Same title as another page | 74 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /calendar/special-event/book-signing-and-meet-greet-kennerly-balkowitsch-and-ziemendorf, /visit/exhibits/kennerly |
| medium | Sitemap lists a /node/ URL instead of a readable path | 35 | /node/240, /node/241, /node/244, /node/245, /node/249 |
| medium | Missing Open Graph tags | 33 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /calendar/special-event/book-signing-and-meet-greet-kennerly-balkowitsch-and-ziemendorf, /birthdaycard |
| medium | No meta description | 32 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /calendar/special-event/book-signing-and-meet-greet-kennerly-balkowitsch-and-ziemendorf, /birthdaycard |
| medium | No H1 heading | 29 | /birthdaycard, /project/how-the-library-works, /rsvp/midwinter, /about/reports/2024-annual-report, /privacy |
| medium | Sitemap lists a URL that redirects | 5 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /calendar/special-event/book-signing-and-meet-greet-kennerly-balkowitsch-and-ziemendorf, /event/24 |
| low | Title over 60 characters, not counting the site-name suffix | 265 | /node/240, /node/241, /node/244, /node/245, /node/249 |
| low | Under 150 words of body text | 237 | /birthdaycard, /project/how-the-library-works, /node/240, /node/241, /node/244 |
| low | Heading levels skip (e.g. H2 straight to H4) | 150 | /calendar/special-event/gallery-david-hume-kennerly, /calendar/special-event/artist-talk-room-david-hume-kennerly, /calendar/special-event/artist-panel-kennerly-balkowitsch-and-ziemendorf, /calendar/special-event/book-signing-and-meet-greet-kennerly-balkowitsch-and-ziemendorf, /visit/exhibits/kennerly |
| low | Title under 15 characters, not counting the site-name suffix | 149 | /birthdaycard, /join-us, /quiz/the-boardwalk, /visit/survey, /video/view/Y3jQTzNVVFY |
| low | Same meta description as another page | 126 | /event/24, /video/view/Y3jQTzNVVFY, /video/view/YJ_qzszUZUA, /node/205, /podcast/good-citizen/douglas-brinkley |
| low | More than 4 clicks from the homepage | 112 | /node/240, /node/241, /node/244, /node/245, /node/249 |
| low | Meta description under 70 characters | 18 | /video/view/Y3jQTzNVVFY, /video/view/YJ_qzszUZUA, /video/view/Lk8bs9ilpLI, /video/view/0NiRkijqLGw, /video/view/NoLhSWhiCpA |
| low | More than one H1 | 10 | /support/matching-gifts, /about/mission, /about/foundation, /impact, /project |
| low | Took over 3 seconds to respond | 3 | /video/view/N40FrDWTYfk, /tr/books-and-writings/reader, /visit/itineraries/13-day-denver-wyoming |

## Recently changed pages (held back from recommendations for 28 days)
Before = the 28 days before the change; after = the days since, up to the latest settled Search Console day. Compare per-day numbers; a week or two after a change is still early.

| Page | Changed | What | Clicks/day before → after | CTR | Position |
|---|---|---|---|---|---|
| /tr/rise-to-power/spanish-american-war | 2026-11-09 | Title 'Theodore Roosevelt and the Spanish-American War'; Navy/Rough Riders description | 6.4 → – | 0.5% → – | 5.7 → – |
| /tr/presidency/food-and-drug | 2026-11-09 | Title 'Pure Food and Drug Act and Meat Inspection Act of 1906'; drops '1905 novel' | 10.6 → – | 0.9% → – | 5.3 → – |
| /tr/people/archibald | 2026-11-09 | Title 'Archibald Roosevelt: TR’s Son Wounded in Two World Wars' | 0.1 → – | 0.1% → – | 7.4 → – |
| /visit/lodging | 2026-11-09 | Title 'Medora Hotels, Cabins and Campgrounds'; names Hotel 1883 | 4.8 → – | 0.9% → – | 7.7 → – |
| /join-us | 2026-11-09 | Title 'Join Us: Become a Member, Volunteer or Work Here'; first description and OG tags | 0.0 → – | 0.0% → – | 4.4 → – |
| /visit/exhibits/kennerly | 2026-11-09 | Title 'In the Room: David Hume Kennerly Photo Exhibition'; first description and OG tags | 2.3 → – | 2.4% → – | 6.5 → – |
| /about/trustees/kermit-roosevelt | 2026-11-09 | Title 'Kermit Roosevelt, Library Trustee' (was duplicate of /tr/people/kermit) | 0.4 → – | 0.5% → – | 6.9 → – |
| /about/trustees/douglas-brinkley | 2026-11-09 | Title 'Douglas Brinkley, Library Trustee' (was duplicate of podcast page) | 0.1 → – | 0.4% → – | 10.2 → – |
| /contact | 2026-11-09 | Title 'Contact Us: Phone, Address and Message Form'; phone and address in description | 1.9 → – | 1.0% → – | 2.9 → – |
| /visit/tickets/plan-ahead | 2026-11-09 | Description no longer leads with summer; removed '2026 is the Library's first year' | 0.6 → – | 1.3% → – | 6.7 → – |
| /llms.txt | 2026-11-09 | Added 'Key facts for visitors' (address, 3½ hours, year-round, tickets, indoor, not the FD | 0.0 → – | – → – | – → – |
| /about/press/press-releases | 2026-11-03 | Press releases: og:type article, NewsArticle author/publisher/description, ISO dates with  | 0.0 → 0.0 | 0.0% → – | 11.0 → – |
| /podcast/good-citizen | 2026-11-03 | Podcast episodes: og:type article | 1.3 → 0.8 | 1.5% → 1.1% | 7.1 → 7.8 |
| /about/trustees | 2026-11-03 | Trustee Person markup: memberOf the Library | 1.9 → 1.7 | 9.8% → 12.8% | 9.0 → 6.0 |
| /tr/presidency | 2026-11-03 | Published Oct 18 draft plus 2 internal links (Taft, midnight forests) | 0.9 → 2.2 | 0.6% → 0.5% | 6.3 → 5.1 |
| /tr/timeline | 2026-11-03 | Added 6 internal links from Links to add; Title 'Theodore Roosevelt's Life Timeline: Key D | 7.8 → 7.5 | 0.5% → 0.5% | 7.4 → 6.6 |
| /visit/exhibits/main | 2026-11-03 | Added 6 internal links from Links to add | 2.8 → 1.8 | 1.8% → 1.0% | 6.5 → 5.9 |
| /tr/teddy-nickname | 2026-11-03 | Added 6 internal links from Links to add; Merged /tr/myths/teddy-name into this page; new  | 4.8 → 5.2 | 0.8% → 0.8% | 4.4 → 4.6 |
| /tr/presidency-timeline | 2026-11-03 | Added 6 internal links from Links to add; Title 'When Was Theodore Roosevelt President? 19 | 11.5 → 10.7 | 0.6% → 0.5% | 4.6 → 4.4 |
| /tr/people/henry-cabot-lodge | 2026-11-03 | Added 6 internal links from Links to add | 1.1 → 1.7 | 0.2% → 0.4% | 6.5 → 6.7 |
| /tr/family/family-tree | 2026-11-03 | Added 5 internal links from Links to add | 14.2 → 15.7 | 1.5% → 1.9% | 5.2 → 6.1 |
| /tr/presidency/white-house-family | 2026-11-03 | Added 4 internal links from Links to add | 0.2 → 0.5 | 0.3% → 0.6% | 6.6 → 8.1 |
| /podcast/good-citizen/doris-kearns-goodwin-presidential-stories-trpl-and-enduring-lessons-theodore | 2026-11-03 | Added 5 internal links from Links to add | 0.3 → 0.2 | 0.8% → 0.5% | 8.8 → 9.3 |
| /tr/legacy/rankings | 2026-11-03 | Added 5 internal links from Links to add | 5.0 → 9.8 | 1.5% → 2.2% | 5.6 → 5.9 |
| /podcast/good-citizen/edward-okeefe | 2026-11-03 | Added 4 internal links from Links to add | 0.1 → 0.0 | 0.8% → 0.0% | 8.2 → 7.8 |
| /podcast/good-citizen/call-adventure-charlie-melcher-ed-okeefe-and-brand-new-theodore-roosevelt | 2026-11-03 | Added 6 internal links from Links to add | 0.3 → 0.0 | 1.1% → 0.0% | 7.4 → 7.8 |
| /tr/for-educators/high-school | 2026-11-03 | Added 6 internal links from Links to add | 0.8 → 0.7 | 1.8% → 1.6% | 7.0 → 6.7 |
| /about/press/press-releases/theodore-roosevelts-groundbreaking-firsts-and-feats-celebration | 2026-11-03 | Added 6 internal links from Links to add | 0.1 → 0.2 | 1.1% → 1.0% | 4.7 → 6.7 |
| /tr/rise-to-power/ten-facts | 2026-11-03 | Added 6 internal links from Links to add | 3.3 → 5.8 | 1.6% → 2.7% | 5.3 → 3.9 |
| /tr/presidency/ten-facts | 2026-11-03 | Added 5 internal links from Links to add | 15.5 → 20.5 | 2.8% → 3.8% | 3.9 → 3.8 |
| /events/teddycon | 2026-11-03 | Added 6 internal links from Links to add | 3.4 → 0.3 | 8.8% → 1.5% | 3.8 → 6.1 |
| /tr/badlands-timeline | 2026-11-03 | Added 6 internal links from Links to add | 5.7 → 4.7 | 2.0% → 2.2% | 5.5 → 4.9 |
| /tr/family/fdr-connection | 2026-11-03 | Added 4 internal links from Links to add; Title 'How Were Theodore and Franklin Roosevelt  | 60.9 → 62.7 | 1.9% → 1.8% | 3.2 → 3.0 |
| /research/archives | 2026-11-03 | Added 5 internal links from Links to add | 1.7 → 2.2 | 2.5% → 3.0% | 7.7 → 7.7 |
| /tr/speeches/new-nationalism | 2026-11-03 | Added 5 internal links from Links to add | 1.7 → 0.5 | 2.0% → 1.3% | 5.6 → 6.5 |
| /tr/presidency/elections | 2026-11-03 | Added 4 internal links from Links to add; Title '1904 Presidential Election: Roosevelt's M | 4.5 → 6.7 | 0.6% → 1.1% | 5.9 → 5.7 |
| /tr/legacy/the-library | 2026-11-03 | Added 5 internal links from Links to add | 1.2 → 0.5 | 1.0% → 1.4% | 5.0 → 5.0 |
| /tr/post-presidency/ten-facts | 2026-11-03 | Added 5 internal links from Links to add | 0.4 → 0.3 | 1.0% → 1.0% | 5.5 → 5.4 |
| /visit/medora/history | 2026-11-03 | Added 5 internal links from Links to add; North Dakota quote aligned to the 1918 Volwiler  | 1.2 → 1.0 | 1.2% → 1.8% | 7.4 → 7.3 |
| /tr/fake-quotes | 2026-11-03 | Added 3 internal links from Links to add | 11.7 → 9.7 | 2.0% → 2.1% | 6.8 → 6.1 |
| /tr/kids-timeline | 2026-11-03 | Added 5 internal links from Links to add; Title 'Theodore Roosevelt for Kids: A Timeline o | 2.5 → 1.5 | 0.7% → 0.5% | 9.4 → 9.9 |
| /tr/tr-mount-rushmore | 2026-11-03 | Added 3 internal links from Links to add; Title 'Mount Rushmore Presidents: Why Theodore R | 16.0 → 17.0 | 0.4% → 0.3% | 5.5 → 5.7 |
| /visit/directions | 2026-11-03 | Added 4 internal links from Links to add; Title 'Directions to Medora from I-94 and Nearby | 21.1 → 8.3 | 1.2% → 0.8% | 2.7 → 3.5 |
| /tr/books-and-writings/autobiography | 2026-11-03 | Added 4 internal links from Links to add | 1.1 → 1.2 | 1.3% → 1.8% | 5.7 → 4.7 |
| /tr/pre-presidency-political-accomplishments | 2026-11-03 | Added 4 internal links from Links to add; Title 'What Did Theodore Roosevelt Do Before He  | 20.5 → 15.0 | 1.1% → 0.9% | 5.6 → 5.6 |
| /tr/books-and-writings/complete-list | 2026-11-03 | Added 4 internal links from Links to add | 0.2 → 0.0 | 1.9% → 0.0% | 5.4 → 4.9 |
| /tr/quotes/leadership | 2026-11-03 | Added 5 internal links from Links to add | 3.6 → 3.0 | 3.0% → 3.0% | 5.4 → 5.0 |
| /tr/speeches/inaugural | 2026-11-03 | Added 4 internal links from Links to add | 0.5 → 0.8 | 0.5% → 0.4% | 5.7 → 5.7 |
| /podcast/good-citizen/candice-millard | 2026-11-03 | Added 2 internal links from Links to add | 0.4 → 0.7 | 0.3% → 0.4% | 9.3 → 10.8 |
| /tr/people/eleanor | 2026-11-03 | Added 4 internal links from Links to add | 0.4 → 0.8 | 0.5% → 0.4% | 6.9 → 7.1 |
| /tr/people/bill-sewall | 2026-11-03 | Added 4 internal links from Links to add | 0.6 → 0.7 | 2.2% → 2.1% | 5.5 → 5.5 |
| /tr/post-presidency/quentin | 2026-11-03 | Added 4 internal links from Links to add | 1.0 → 1.2 | 0.4% → 0.7% | 9.5 → 9.1 |
| /tr/quotes/conservation | 2026-11-03 | Added 2 internal links from Links to add | 3.4 → 3.3 | 1.9% → 2.5% | 5.3 → 4.7 |
| /podcast/good-citizen/karl-rove-historic-redemption-hard-work-politics-and-essential-nature | 2026-11-03 | Added 3 internal links from Links to add | 1.8 → 5.7 | 0.1% → 0.3% | 9.2 → 7.7 |
| /tr/early-life/siblings | 2026-11-03 | Added 3 internal links from Links to add | 1.2 → 1.0 | 1.2% → 0.9% | 6.3 → 5.5 |
| /tr/early-life/ten-facts | 2026-11-03 | Added 4 internal links from Links to add | 0.4 → 0.3 | 3.6% → 1.6% | 5.4 → 5.4 |
| /tr/people/kermit | 2026-11-03 | Added 4 internal links from Links to add | 0.2 → 0.5 | 0.4% → 0.7% | 8.6 → 8.6 |
| /tr/legacy | 2026-11-03 | Added 3 internal links from Links to add | 0.1 → 0.3 | 0.8% → 1.8% | 8.8 → 5.0 |
| /tr/people/bamie | 2026-11-03 | Added 3 internal links from Links to add | 0.2 → 0.2 | 0.5% → 0.3% | 6.0 → 8.2 |
| /tr/early-life | 2026-11-03 | Added 3 internal links from Links to add | 5.2 → 7.3 | 0.9% → 1.5% | 6.7 → 5.9 |
| /podcast/good-citizen/jeffrey-rosen | 2026-11-03 | Added 3 internal links from Links to add | 0.2 → 0.2 | 0.3% → 0.4% | 10.2 → 10.2 |
| /tr/complex-legacy/imperialism | 2026-11-03 | Added 2 internal links from Links to add | 8.3 → 14.3 | 1.0% → 1.1% | 5.2 → 4.9 |
| /tr/strenuous-life/hunter | 2026-11-03 | Added 3 internal links from Links to add | 1.2 → 0.8 | 0.9% → 0.7% | 5.6 → 5.2 |
| /tr/tr-shot | 2026-11-03 | Added 3 internal links from Links to add; Title 'Why Was Theodore Roosevelt Shot? The 1912 | 11.4 → 11.3 | 0.9% → 1.3% | 4.0 → 4.3 |
| /visit/itineraries/chicago-badlands | 2026-11-03 | Added 2 internal links from Links to add; Visit length and restaurant name | 0.8 → 0.5 | 1.6% → 1.2% | 6.9 → 6.5 |
| /tr/post-presidency/death | 2026-11-03 | Added 3 internal links from Links to add | 2.8 → 3.0 | 0.5% → 0.4% | 5.5 → 5.0 |
| /tr/new-york-politics/alice-lee | 2026-11-03 | Added 3 internal links from Links to add | 3.0 → 3.5 | 0.8% → 0.9% | 5.5 → 5.4 |
| /tr/square-deal | 2026-11-03 | Added 2 internal links from Links to add; Archived (node 278); 301 to /tr/presidency/squar | 31.8 → 0.2 | 0.8% → 0.9% | 3.9 → 1.8 |
| /tr/rise-to-power/edith-roosevelt | 2026-11-03 | Added 3 internal links from Links to add | 1.5 → 2.0 | 0.4% → 0.6% | 6.9 → 7.9 |
| /tr/presidency/conservation/midnight-forests | 2026-11-03 | Added 3 internal links from Links to add | 1.1 → 2.2 | 1.3% → 2.8% | 5.1 → 5.4 |
| /tr/quotes/misquotes | 2026-11-03 | Added 3 internal links from Links to add | 5.5 → 5.5 | 2.6% → 2.1% | 4.0 → 4.6 |
| /tr/post-presidency/man-in-the-arena | 2026-11-03 | Added 3 internal links from Links to add; Title 'TR's 1910 European Tour and the Man in th | 1.6 → 1.2 | 0.8% → 1.5% | 7.5 → 6.9 |
| /visit/activities | 2026-11-03 | Added 3 internal links from Links to add; Visit length and restaurant name | 0.5 → 0.7 | 0.9% → 2.0% | 5.3 → 7.0 |
| /tr/conservation/by-the-numbers | 2026-11-03 | Added 3 internal links from Links to add | 1.6 → 3.0 | 0.6% → 1.3% | 5.1 → 4.4 |
| /tr/presidency/conservation/gifford-pinchot | 2026-11-03 | Added 2 internal links from Links to add | 1.6 → 2.7 | 0.6% → 1.1% | 4.4 → 3.9 |
| /tr/early-life/family-roots | 2026-11-03 | Added 3 internal links from Links to add | 1.5 → 2.0 | 0.8% → 1.0% | 4.8 → 5.4 |
| /podcast/good-citizen/live-trpl-1-doris-kearns-goodwin-finding-hope-history | 2026-11-03 | Added 3 internal links from Links to add | 0.1 → 0.2 | 0.7% → 1.5% | 8.8 → 10.8 |
| /tr/homes-and-places/sagamore-hill | 2026-11-03 | Added 2 internal links from Links to add | 0.4 → 0.3 | 0.7% → 0.5% | 7.0 → 6.9 |
| /tr/presidency/conservation/national-monuments | 2026-11-03 | Added 3 internal links from Links to add | 0.9 → 1.5 | 0.8% → 1.0% | 5.5 → 5.4 |
| /tr/presidency/white-house-family/pets | 2026-11-03 | Added 3 internal links from Links to add | 2.2 → 3.2 | 1.2% → 1.8% | 5.1 → 4.5 |
| /visit/teddy-trail | 2026-11-03 | Added 3 internal links from Links to add | 0.3 → 0.3 | 1.2% → 1.4% | 6.4 → 6.8 |
| /visit/exhibits | 2026-11-03 | Added 3 internal links from Links to add; Title: Exhibits: Roosevelt’s Life in Eight Chapt | 3.8 → 0.3 | 0.6% → 0.2% | 3.5 → 5.6 |
| /tr/people | 2026-11-03 | Added 3 internal links from Links to add | 0.8 → 0.3 | 0.4% → 0.7% | 7.4 → 7.0 |
| /about/trustees/doris-kearns-goodwin | 2026-11-03 | Added 3 internal links from Links to add | 0.2 → 0.2 | 0.8% → 0.5% | 16.0 → 14.3 |
| /tr/people/william-howard-taft | 2026-11-03 | Added 3 internal links from Links to add | 1.8 → 3.0 | 0.3% → 0.4% | 5.7 → 5.2 |
| /about/press/press-releases/theodore-roosevelt-presidential-library-opening-celebrations-july-4-2026 | 2026-11-03 | Added 3 internal links from Links to add | 1.9 → 2.0 | 2.9% → 3.0% | 4.4 → 5.7 |
| /tr | 2026-11-03 | Added 3 internal links from Links to add | 0.3 → 0.3 | 0.1% → 0.1% | 6.9 → 5.2 |
| /tr/post-presidency | 2026-11-03 | Added 3 internal links from Links to add | 1.8 → 1.2 | 2.6% → 1.2% | 4.2 → 3.7 |
| /tr/new-york-politics/double-tragedy | 2026-11-03 | Added 3 internal links from Links to add | 0.5 → 2.0 | 1.6% → 2.8% | 4.4 → 4.7 |
| /tr/quotes/family | 2026-11-03 | Added 2 internal links from Links to add | 0.3 → 0.7 | 2.3% → 2.3% | 6.2 → 5.6 |
| /tr/people/alice-lee | 2026-11-03 | Added 3 internal links from Links to add | 0.1 → 1.2 | 0.3% → 2.2% | 8.8 → 8.0 |
| /about/press/press-releases/harold-hamm-donates-50-million-trpl | 2026-11-03 | Added 2 internal links from Links to add | 1.7 → 0.2 | 10.5% → 2.7% | 3.1 → 3.3 |
| /tr/people/theodore-sr | 2026-11-03 | Added 2 internal links from Links to add | 0.4 → 1.0 | 0.2% → 0.8% | 6.5 → 5.8 |
| /about/press/press-releases/roosevelt-family-acquires-903-acres-trpl | 2026-11-03 | Added 2 internal links from Links to add | 0.6 → 0.5 | 7.0% → 7.9% | 4.2 → 5.1 |
| /tr/legacy/mount-rushmore | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 1.0 | 0.2% → 0.7% | 7.1 → 7.3 |
| /tr/conservation/quotes | 2026-11-03 | Added 3 internal links from Links to add | 0.5 → 2.2 | 1.4% → 1.4% | 4.9 → 4.9 |
| /visit/itineraries/north-on-29 | 2026-11-03 | Added 2 internal links from Links to add | 0.3 → 0.2 | 0.8% → 0.6% | 7.2 → 7.5 |
| /tr/rise-to-power/police-commissioner | 2026-11-03 | Added 2 internal links from Links to add | 1.8 → 2.5 | 1.7% → 2.5% | 5.7 → 5.2 |
| /tr/legacy/words-he-coined | 2026-11-03 | Added 2 internal links from Links to add | 0.9 → 1.0 | 0.6% → 0.8% | 6.4 → 7.2 |
| /tr/myths/misquotes | 2026-11-03 | Added 2 internal links from Links to add | 1.1 → 1.3 | 1.1% → 1.3% | 5.2 → 5.8 |
| /tr/quotes | 2026-11-03 | Added 2 internal links from Links to add | 21.7 → 15.0 | 2.3% → 2.1% | 10.7 → 4.1 |
| /tr/presidency/first-term | 2026-11-03 | Added 2 internal links from Links to add | 0.5 → 0.3 | 1.7% → 0.6% | 6.5 → 5.6 |
| /visit/itineraries/13-day-denver-wyoming | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.8% → 0.0% | 8.9 → 8.4 |
| /tr/family/children | 2026-11-03 | Added 2 internal links from Links to add; Title 'Theodore Roosevelt's Children: Alice, Ted | 4.2 → 7.5 | 1.1% → 1.8% | 4.2 → 3.5 |
| /visit/shopping | 2026-11-03 | Added 2 internal links from Links to add | 5.0 → 5.2 | 2.2% → 5.2% | 5.0 → 7.6 |
| /tr/family | 2026-11-03 | Added 2 internal links from Links to add | 1.1 → 1.8 | 0.4% → 0.5% | 8.0 → 7.4 |
| /tr/for-educators/middle-school | 2026-11-03 | Added 2 internal links from Links to add | 0.6 → 0.5 | 2.2% → 1.5% | 6.5 → 5.7 |
| /visit/medora | 2026-11-03 | Added 1 internal link from Links to add | 1.1 → 0.2 | 0.7% → 0.2% | 4.5 → 4.1 |
| /tr/rise-to-power/buffalo-soldiers | 2026-11-03 | Added 1 internal link from Links to add | 1.6 → 1.3 | 0.7% → 0.6% | 5.2 → 4.9 |
| /tr/early-life/harvard | 2026-11-03 | Added 2 internal links from Links to add | 0.9 → 2.5 | 1.0% → 1.9% | 5.4 → 5.0 |
| /tr/elkhorn | 2026-11-03 | Added 2 internal links from Links to add | 1.6 → 2.0 | 0.8% → 1.3% | 8.0 → 7.7 |
| /podcast/good-citizen/ted-leonsis | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.3 | 0.2% → 0.2% | 10.0 → 8.5 |
| /tr/presidency/conservation/national-parks | 2026-11-03 | Added 2 internal links from Links to add | 6.9 → 6.3 | 0.9% → 1.0% | 6.0 → 5.4 |
| /bullet-speech | 2026-11-03 | Added 1 internal link from Links to add; Title 'The Bullet Speech: Roosevelt's Assassinati | 24.4 → 24.5 | 1.7% → 1.7% | 3.7 → 3.6 |
| /tr/early-life/mother | 2026-11-03 | Added 2 internal links from Links to add | 0.3 → 0.0 | 0.3% → 0.0% | 5.1 → 4.6 |
| /tr/post-presidency/river-of-doubt | 2026-11-03 | Added 2 internal links from Links to add | 2.6 → 5.5 | 0.6% → 1.0% | 7.5 → 7.2 |
| /tr/post-presidency/african-safari | 2026-11-03 | Added 2 internal links from Links to add | 1.2 → 1.7 | 1.3% → 2.3% | 5.9 → 5.8 |
| /tr/post-presidency/new-nationalism | 2026-11-03 | Added 2 internal links from Links to add | 1.8 → 1.5 | 0.7% → 0.6% | 4.5 → 4.5 |
| /tr/presidency/conservation/reclamation | 2026-11-03 | Added 2 internal links from Links to add | 3.3 → 2.2 | 0.8% → 0.7% | 4.2 → 3.9 |
| /tr/5-big-adventures | 2026-11-03 | Added 2 internal links from Links to add | 2.0 → 1.0 | 1.0% → 0.4% | 6.5 → 5.9 |
| /tr/rise-to-power/san-juan-hill | 2026-11-03 | Added 2 internal links from Links to add; Title uses 'Battle of San Juan Hill' | 14.8 → 14.2 | 1.4% → 1.2% | 3.7 → 3.6 |
| /tr/presidency/conservation/bird-reserves | 2026-11-03 | Added 2 internal links from Links to add | 0.8 → 0.3 | 1.5% → 0.4% | 5.4 → 5.0 |
| /podcast/good-citizen/douglas-brinkley | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.2 | 0.1% → 0.5% | 11.9 → 12.8 |
| /tr/people/corinne | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.7 | 0.2% → 1.3% | 4.3 → 3.1 |
| /podcast/good-citizen/eric-liu | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.0 | 0.3% → 0.0% | 7.8 → 5.6 |
| /tr/quotes/strenuous-life | 2026-11-03 | Added 1 internal link from Links to add | 1.8 → 2.7 | 1.3% → 1.4% | 6.3 → 6.3 |
| /tr/quotes/citizenship | 2026-11-03 | Added 2 internal links from Links to add | 1.9 → 2.5 | 1.7% → 2.4% | 5.8 → 5.5 |
| /tr/elkhorn-timeline | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.0 | 1.3% → 0.0% | 8.1 → 7.7 |
| /tr/people/edith-roosevelt | 2026-11-03 | Added 2 internal links from Links to add | 0.4 → 0.2 | 0.7% → 0.4% | 11.3 → 13.8 |
| /visit/roosevelt-in-medora | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.8% → 0.0% | 7.4 → 8.8 |
| /podcast/good-citizen/meg-whitman | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.5 | 0.1% → 0.4% | 11.4 → 11.0 |
| /tr/speeches/strenuous-life | 2026-11-03 | Added 1 internal link from Links to add | 2.7 → 2.3 | 1.9% → 2.5% | 5.7 → 5.2 |
| /tr/people/quentin | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.3 | 0.4% → 1.3% | 8.5 → 8.1 |
| /tr/post-presidency/world-war-i | 2026-11-03 | Added 2 internal links from Links to add | 0.2 → 0.5 | 0.5% → 0.7% | 5.4 → 5.4 |
| /tr/rise-to-power/sagamore-hill | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.0 | 0.9% → 0.0% | 6.9 → 7.1 |
| /tr/new-york-politics/convention-1884 | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.3 | 0.9% → 1.2% | 6.7 → 5.3 |
| /about/press/press-releases/sarah-and-ross-perot-jr-foundation-gifts-5-million-theodore-roosevelt | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.9% → 0.0% | 6.4 → 6.0 |
| /about/press/press-releases/theodore-roosevelt-presidential-library-welcomes-doris-kearns-goodwin | 2026-11-03 | Added 2 internal links from Links to add | 0.0 → 0.0 | 0.7% → 0.0% | 5.3 → 17.6 |
| /about/foundation | 2026-11-03 | Added 1 internal link from Links to add | 2.5 → 2.2 | 3.7% → 4.3% | 5.5 → 5.5 |
| /visit/eat | 2026-11-03 | Added 2 internal links from Links to add | 5.8 → 2.0 | 2.7% → 1.7% | 7.2 → 7.9 |
| /visit/maps | 2026-11-03 | Added 1 internal link from Links to add | 1.7 → 0.2 | 0.5% → 0.6% | 3.9 → 3.4 |
| /tr/post-presidency/assassination-attempt | 2026-11-03 | Added 2 internal links from Links to add | 0.8 → 2.7 | 0.6% → 2.2% | 8.0 → 6.3 |
| /research | 2026-11-03 | Added 2 internal links from Links to add | 1.1 → 0.8 | 3.4% → 3.0% | 5.5 → 4.9 |
| /tr/presidency/white-house-family/white-house-gang | 2026-11-03 | Added 2 internal links from Links to add | 0.0 → 0.0 | 1.9% → 0.0% | 6.0 → 5.9 |
| /tr/presidency/conservation/governors-conference | 2026-11-03 | Added 2 internal links from Links to add | 0.3 → 0.5 | 3.4% → 6.2% | 4.8 → 3.1 |
| /tr/rise-to-power/jacob-riis | 2026-11-03 | Added 1 internal link from Links to add | 1.7 → 4.0 | 0.6% → 1.1% | 4.9 → 4.4 |
| /tr/strenuous-life/explorer | 2026-11-03 | Added 2 internal links from Links to add | 0.1 → 0.0 | 1.1% → 0.0% | 5.0 → 4.6 |
| /tr/presidency/race | 2026-11-03 | Added 2 internal links from Links to add | 3.8 → 3.8 | 1.2% → 1.3% | 4.4 → 3.7 |
| /visit/itineraries | 2026-11-03 | Added 1 internal link from Links to add; Link to the I-94 guide | 2.7 → 2.7 | 1.6% → 1.8% | 6.5 → 6.7 |
| /tr/presidency/executive-power | 2026-11-03 | Added 2 internal links from Links to add | 2.9 → 10.0 | 1.5% → 1.8% | 4.1 → 3.9 |
| /tr/presidency/conservation/national-forests | 2026-11-03 | Added 2 internal links from Links to add | 0.5 → 0.2 | 0.8% → 0.1% | 6.0 → 5.6 |
| /visit/itineraries/black-hills-loop | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.3 | 1.0% → 1.2% | 8.3 → 7.8 |
| /visit/itineraries/7-day-billings-bismarck | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 0.5% → 0.0% | 8.6 → 8.4 |
| /tr/10-myths-teddy-bear | 2026-11-03 | Added 1 internal link from Links to add | 5.2 → 5.0 | 0.8% → 1.1% | 5.5 → 6.0 |
| /tr/post-presidency/bull-moose/platform | 2026-11-03 | Added 1 internal link from Links to add | 8.6 → 9.5 | 0.7% → 0.5% | 5.0 → 4.1 |
| /tr/for-educators/elementary | 2026-11-03 | Added 1 internal link from Links to add | 1.2 → 1.0 | 2.5% → 2.5% | 6.2 → 5.9 |
| /tr/people/alice-longworth | 2026-11-03 | Added 1 internal link from Links to add; Title 'Alice Roosevelt Longworth: Theodore Roosev | 3.7 → 4.5 | 0.4% → 0.5% | 8.0 → 7.1 |
| /tr/tr-save-the-bison | 2026-11-03 | Added 1 internal link from Links to add | 2.1 → 3.5 | 1.5% → 2.6% | 5.1 → 5.0 |
| /tr/presidency/trust-busting | 2026-11-03 | Added 1 internal link from Links to add; Title 'What Was Trust-Busting? Roosevelt Takes On | 36.2 → 45.5 | 1.3% → 1.7% | 3.4 → 3.2 |
| /tr/complex-legacy | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.0 | 1.7% → 0.0% | 6.0 → 6.2 |
| /podcast/good-citizen/susan-berfield | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.2 | 0.5% → 1.0% | 5.6 → 5.8 |
| /tr/badlands/bad-lands-cow-boy | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.2 | 0.3% → 0.9% | 8.6 → 7.2 |
| /tr/presidency/great-white-fleet | 2026-11-03 | Added 1 internal link from Links to add; Title 'The Great White Fleet: Roosevelt's Global  | 6.6 → 12.7 | 0.7% → 1.3% | 4.1 → 3.3 |
| /tr/badlands/ten-facts | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 1.5 | 1.1% → 2.9% | 5.1 → 4.9 |
| /podcast/good-citizen/susannah-cahalan | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.5 | 0.2% → 0.4% | 9.2 → 10.2 |
| /tr/presidency/bully-pulpit | 2026-11-03 | Added 1 internal link from Links to add; Title 'The Bully Pulpit: Meaning, Origin, and Exa | 5.7 → 10.5 | 0.6% → 0.5% | 4.6 → 3.3 |
| /tr/speeches/man-in-the-arena | 2026-11-03 | Added 1 internal link from Links to add; Title 'Man in the Arena Speech: Citizenship in a  | 25.7 → 50.3 | 2.3% → 2.5% | 5.2 → 6.1 |
| /tr/complex-legacy/eugenics | 2026-11-03 | Added 1 internal link from Links to add | 3.5 → 4.0 | 2.9% → 3.5% | 4.2 → 4.1 |
| /tr/people/jacob-riis | 2026-11-03 | Added 1 internal link from Links to add; Title and description aimed at 'who was Jacob Rii | 16.4 → 26.7 | 0.5% → 1.0% | 6.6 → 6.0 |
| /tr/badlands/maltese-cross | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.0 | 3.1% → 0.0% | 6.5 → 6.7 |
| /tr/people/elliott | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 9.4 → 9.1 |
| /tr/rise-to-power/vice-presidency | 2026-11-03 | Added 1 internal link from Links to add | 1.9 → 3.0 | 0.7% → 0.8% | 5.4 → 4.9 |
| /tr/family/elliott-roosevelt | 2026-11-03 | Added 1 internal link from Links to add | 1.1 → 2.0 | 0.5% → 0.9% | 7.5 → 7.2 |
| /tr/badlands | 2026-11-03 | Added 1 internal link from Links to add; Link to where-to-see | 0.1 → 0.3 | 1.1% → 2.8% | 5.3 → 7.6 |
| /podcast/good-citizen/carly-fiorina | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.4% → 0.0% | 8.7 → 7.7 |
| /tr/badlands/medora | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.2 | 0.4% → 0.6% | 7.8 → 8.1 |
| /virtual | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 5.1% → 0.0% | 6.3 → 7.4 |
| /tr/books-and-writings/reader | 2026-11-03 | Added 1 internal link from Links to add | 1.2 → 1.0 | 1.9% → 2.0% | 5.2 → 5.4 |
| /tr/complex-legacy/race | 2026-11-03 | Added 1 internal link from Links to add | 0.9 → 2.2 | 0.9% → 1.0% | 4.9 → 4.9 |
| /tr/people/john-muir | 2026-11-03 | Added 1 internal link from Links to add | 1.0 → 0.7 | 0.5% → 0.4% | 7.2 → 6.4 |
| /tr/complex-legacy/equestrian-statue | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.2 | 1.5% → 0.3% | 5.5 → 5.4 |
| /tr/people/ethel | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.2 | 0.3% → 0.2% | 7.8 → 7.4 |
| /tr/rise-to-power/becoming-president | 2026-11-03 | Added 1 internal link from Links to add | 1.4 → 2.5 | 0.3% → 0.5% | 5.3 → 4.2 |
| /tr/people/ted-jr | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.7 | 0.1% → 0.1% | 10.2 → 10.2 |
| /tr/people/mittie | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.5 | 0.6% → 0.7% | 7.5 → 6.8 |
| /podcast/good-citizen/katherine-gehl | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.5 | 1.1% → 4.9% | 8.2 → 8.7 |
| /visit/itineraries/7-day-bismarck-rapid-city | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.3 | 0.4% → 0.5% | 8.1 → 8.5 |
| /tr/early-life/childhood-illness | 2026-11-03 | Added 1 internal link from Links to add | 2.3 → 5.2 | 1.8% → 3.0% | 4.0 → 3.5 |
| /tr/presidency/square-deal | 2026-11-03 | Added 1 internal link from Links to add; Truncated description fixed; Three Cs heading; Sp | 20.7 → 78.7 | 0.6% → 1.5% | 4.4 → 3.0 |
| /tr/presidency/conservation/john-muir | 2026-11-03 | Added 1 internal link from Links to add | 3.2 → 4.3 | 1.1% → 1.3% | 4.5 → 4.0 |
| /tr/myths | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.3 | 0.5% → 7.1% | 8.0 → 4.8 |
| /tr/early-life/young-naturalist | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.2 | 0.9% → 1.0% | 4.9 → 4.0 |
| /tr/presidency/cabinet | 2026-11-03 | Added 1 internal link from Links to add | 1.0 → 1.7 | 1.1% → 1.2% | 5.0 → 5.3 |
| /tr/people/booker-t-washington | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 1.7 | 0.2% → 0.4% | 9.4 → 8.1 |
| /project/design | 2026-11-03 | Added 1 internal link from Links to add | 5.5 → 3.2 | 3.7% → 2.5% | 4.5 → 5.2 |
| /tr/early-life/family-travels | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.7 | 1.4% → 3.5% | 5.2 → 4.2 |
| /podcast/good-citizen/adam-met-climate-action-musical-stardom-and-art-building-movement | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 11.5 → 12.7 |
| /tr/conservation | 2026-11-03 | Added 1 internal link from Links to add | 1.1 → 1.3 | 1.0% → 1.5% | 7.2 → 7.5 |
| /tr/speeches/confession-of-faith | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 1.3 | 1.1% → 2.0% | 7.0 → 7.8 |
| /podcast/good-citizen/senator-mitt-romney-formative-moments-presidential-leadership-and-question | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.2 | 0.1% → 0.3% | 7.7 → 7.3 |
| /tr/homes-and-places | 2026-11-03 | Added 1 internal link from Links to add | 1.2 → 1.0 | 1.1% → 0.9% | 5.9 → 5.4 |
| /tr/early-life/civil-war | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.5 | 0.6% → 1.2% | 5.1 → 4.3 |
| /tr/early-life/day-in-the-life | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.2 | 0.6% → 1.7% | 6.9 → 8.4 |
| /visit/national-park | 2026-11-03 | Added 1 internal link from Links to add; Visit length, restaurant name; link to where-to-s | 4.4 → 3.7 | 0.6% → 0.6% | 8.1 → 8.5 |
| /tr/people/gifford-pinchot | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.3 | 0.9% → 0.5% | 6.3 → 5.9 |
| /tr/post-presidency/bull-moose | 2026-11-03 | Added 1 internal link from Links to add | 5.6 → 9.3 | 0.6% → 0.7% | 4.6 → 4.1 |
| /visit/hiking | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.2 | 0.7% → 0.3% | 7.1 → 7.7 |
| /beam-signing-ceremony | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 7.9 → 5.5 |
| /project/native-plant-project | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 0.8 | 0.9% → 4.9% | 4.6 → 7.2 |
| /tr/homes-and-places/tr-national-park | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 1.2 | 0.7% → 1.3% | 7.1 → 7.8 |
| /visit/hunting-fishing | 2026-11-03 | Added 1 internal link from Links to add | 0.8 → 1.3 | 1.1% → 1.6% | 7.3 → 6.4 |
| /about/mission | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.0 | 2.3% → 0.0% | 4.7 → 2.7 |
| /tr/rise-to-power/civil-service | 2026-11-03 | Added 1 internal link from Links to add | 2.1 → 1.2 | 0.6% → 0.2% | 5.3 → 5.5 |
| /tr/badlands/elkhorn-ranch | 2026-11-03 | Added 1 internal link from Links to add | 0.6 → 0.7 | 0.8% → 0.9% | 7.6 → 6.4 |
| /visit/stargazing | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.0 | 1.3% → 0.0% | 6.2 → 5.6 |
| /podcast/good-citizen/dr-vivek-murthy-loneliness-staying-human-and-what-true-success-looks | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.3 | 1.0% → 3.6% | 10.4 → 15.3 |
| /podcast/good-citizen/secretary-deb-haaland | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 3.7 | 0.9% → 1.4% | 7.5 → 7.3 |
| /visit/itineraries/river-road | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.2 | 0.7% → 1.2% | 7.3 → 7.0 |
| /tr/presidency/white-house-workers | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.2 | 1.4% → 0.4% | 6.5 → 7.3 |
| /podcast/good-citizen/matthew-barzun | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.9% → 0.0% | 8.5 → 9.3 |
| /tr/early-life/father | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.5 | 0.5% → 0.4% | 6.7 → 6.9 |
| /visit/camping | 2026-11-03 | Added 1 internal link from Links to add | 0.8 → 0.7 | 1.4% → 1.1% | 7.5 → 7.1 |
| /tr/presidency/conservation/antiquities-act | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.8 | 0.9% → 1.2% | 6.1 → 6.2 |
| /visit/trolley | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.0 | 1.6% → 0.0% | 6.9 → 7.8 |
| /tr/badlands/landscape | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.3 | 0.6% → 0.6% | 5.9 → 5.5 |
| /visit/little-missouri-river | 2026-11-03 | Added 1 internal link from Links to add | 0.4 → 0.2 | 1.1% → 0.5% | 7.8 → 7.2 |
| /podcast/good-citizen/ben-jealous | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 10.2 → 11.7 |
| /podcast/good-citizen/dan-harris | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 8.8 → 8.8 |
| /visit/outdoors | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.2 | 1.4% → 1.0% | 6.6 → 6.2 |
| /visit/biking | 2026-11-03 | Added 1 internal link from Links to add | 0.3 → 0.2 | 2.1% → 1.4% | 7.3 → 8.4 |
| /visit/wildlife | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.2 | 0.6% → 0.5% | 7.8 → 7.2 |
| /project | 2026-11-03 | Added 1 internal link from Links to add; Title 'Building the Library: Design, Values and S | 5.0 → 2.2 | 0.5% → 0.2% | 2.4 → 2.5 |
| /tr/people/leonard-wood | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.8 | 0.2% → 0.6% | 8.8 → 6.2 |
| /podcast/good-citizen/katharine-hayhoe | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 8.5 → 8.3 |
| /visit/itineraries/weekend-drives/fargo | 2026-11-03 | Added 1 internal link from Links to add | 0.6 → 0.5 | 1.1% → 1.3% | 5.0 → 5.2 |
| /about/press/press-releases/trplf-elects-spencer-zwick-board | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 1.6% → 0.0% | 4.3 → 4.0 |
| /visit/itineraries/weekend-drives/bismarck | 2026-11-03 | Added 1 internal link from Links to add | 0.5 → 1.0 | 1.0% → 3.4% | 5.1 → 4.0 |
| /tr/presidency/second-term | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.3 | 1.8% → 1.6% | 6.0 → 4.5 |
| /tr/books-and-writings | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.2 | 0.8% → 0.7% | 8.7 → 9.2 |
| /tr/badlands/frontier-life | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.3 | 0.8% → 1.2% | 6.5 → 6.2 |
| /about/trustees/beth-laski | 2026-11-03 | Added 1 internal link from Links to add | 0.8 → 0.5 | 8.2% → 7.0% | 9.8 → 11.5 |
| /about/press/press-releases/theodore-roosevelt-presidential-library-launches-good-citizen-podcast | 2026-11-03 | Added 1 internal link from Links to add | 0.0 → 0.0 | 0.0% → 0.0% | 5.9 → 3.5 |
| /about/presidential-library-system | 2026-11-03 | Added 1 internal link from Links to add | 0.6 → 0.0 | 2.3% → 0.0% | 6.2 → 6.5 |
| /about/press/press-releases/trplf-announces-100-million-commitments-unlocks-50-million-state | 2026-11-03 | Added 1 internal link from Links to add | 0.2 → 0.0 | 2.8% → 0.0% | 4.9 → 3.8 |
| /tr/new-york-politics | 2026-11-03 | Added 1 internal link from Links to add | 0.1 → 0.0 | 0.9% → 0.0% | 7.0 → 7.2 |
| /tr/tr-importance | 2026-11-03 | Title 'What Was Theodore Roosevelt Known For?'; typo fix | 12.9 → 11.3 | 1.0% → 0.8% | 4.9 → 4.9 |
| /visit | 2026-10-27 | Title: Plan Your Visit: Tickets, Hours and Directions; Visit length: about three and a hal | 57.3 → 29.5 | 2.5% → 1.8% | 2.7 → 2.9 |
| /tr/presidency/panama-canal | 2026-10-27 | Title and description: Theodore Roosevelt and the Panama Canal, 1903–1914 | 8.2 → 16.9 | 0.4% → 0.6% | 5.2 → 4.7 |
| /tr/presidency/railroad-regulation | 2026-10-27 | Title names the Hepburn Act and Elkins Act | 3.9 → 5.8 | 0.4% → 0.7% | 4.0 → 3.5 |
| /tr/presidency/coal-strike | 2026-10-27 | Title uses 'Anthracite Coal Strike of 1902' | 7.9 → 7.5 | 0.9% → 0.9% | 4.2 → 2.9 |
| /visit/groups | 2026-10-27 | Visit length changed from about three hours to about three and a half hours | 0.1 → 0.1 | 0.6% → 2.0% | 6.5 → 5.7 |
| /visit/faq/tickets | 2026-10-27 | 'Buy tickets' link fixed (was /visit/tickets, a 404); 301 /visit/tickets -> /tickets | 2.0 → 1.2 | 4.3% → 3.6% | 6.3 → 4.7 |
| /visit/faq | 2026-10-27 | Tickets link fixed (was /visit/tickets, a 404) | 2.1 → 0.6 | 0.8% → 1.8% | 4.7 → 6.9 |
| /tr/presidency/brownsville | 2026-10-20 | Title 'The Brownsville Affair of 1906: What Happened and Why'; Medal of Honor claim and da | 0.9 → 2.2 | 0.0% → 0.1% | 6.3 → 4.4 |
| /tr/presidency/roosevelt-corollary | 2026-10-20 | Title 'Roosevelt Corollary to the Monroe Doctrine, Explained'; stray second H1 section rem | 6.6 → 15.2 | 0.2% → 0.3% | 5.4 → 4.1 |
| /visit/hours | 2026-10-20 | Title 'Hours in Medora: Seasonal Schedule and Last Entry'; visit-length bullet | 27.0 → 13.0 | 1.2% → 1.1% | 2.7 → 2.2 |
| /tr/myths/teddy-name | 2026-10-20 | Archived; 301 to /tr/teddy-nickname | 0.2 → 0.2 | 1.2% → 0.5% | 6.2 → 5.3 |
| / | 2026-10-20 | Description mentions 'Teddy' | 353.1 → 247.9 | 3.8% → 9.3% | 8.0 → 6.7 |
| /visit/itineraries/one-day | 2026-10-20 | Visit length and restaurant name | 3.5 → 1.9 | 4.1% → 3.6% | 3.9 → 3.9 |
| /visit/itineraries/4-days-north-dakota | 2026-10-20 | Visit length and restaurant name | 0.7 → 0.7 | 1.4% → 1.8% | 7.6 → 7.3 |
| /visit/itineraries/seattle-badlands | 2026-10-20 | Visit length and restaurant name | 0.1 → 0.1 | 1.2% → 0.9% | 6.7 → 8.2 |
| /visit/i-94 | 2026-10-20 | New page: Best Stops on I-94 in North Dakota | 0.0 → 0.0 | – → 0.0% | – → 6.0 |
| /tr/badlands/where-to-see | 2026-10-20 | New page: Where to See Theodore Roosevelt's North Dakota | 0.0 → 0.0 | – → – | – → – |

## Drafted recommendations (Gemini (gemini-3.8-flash), 2026-11-09T13:00:56+00:00)
_4 AI claims were dropped because the live page contradicted them._

**AI visibility:** The Library reliably surfaces on direct branded queries and general Medora recommendations on ChatGPT, but vanishes completely from regional road trips, family itineraries, indoor activities, and broader historical searches.
- Publish an itinerary guide connecting an I-94 road trip and Black Hills drives to a 3 1/2 hour stop in Medora. (medium effort; trlibrary.com/visit/itineraries): AI engines rely heavily on state tourism guides and travel blogs for road-trip queries, where the Library is currently absent.
- Create dedicated web copy highlighting indoor gallery experiences, climate-controlled spaces, and family-friendly exploration. (low effort; trlibrary.com/visit/families): ChatGPT and Gemini direct travelers to Chateau de Mores and the Cowboy Hall of Fame whenever rain, heat, or kids are mentioned.
- Request partner updates on North Dakota Tourism (ndtourism.com) and Medora Chamber (medorand.org) to feature the Library in museum and indoor attraction directories. (medium effort; ndtourism.com and medorand.org partner listings): These regional travel domains are the primary sources cited by AI engines for North Dakota museum and badlands searches.
- Add educational resource pages detailing Roosevelt's conservation policies, Badlands years, and presidency. (high effort; trlibrary.com/learn): Engines pull answers for historical prompts from educational domains, bypassing the Library entirely for TR biographical queries.

**/tr/rise-to-power/spanish-american-war**: Shorten the oversized title to target high-volume search queries and add a concise summary answering Roosevelt's exact wartime roles to capture high-intent informational queries and AI overviews.
- Title: Theodore Roosevelt and the Spanish-American War
- Meta: See how Theodore Roosevelt shaped the Spanish-American War, from readying the Navy to fighting in Cuba, launching him toward the presidency.
- Verify: Verify that the draft summary describing Roosevelt's three wartime roles accurately reflects the historical consensus and page scope.; Verify whether 'From the Archives' was intended to embed digital assets directly or link out to the TR Center.

**/visit/lodging**: Expand the brief title and truncated meta description to target high-volume searches for Medora ND hotels, and add clear pacing details explaining how to pair an overnight stay with a 3 1/2 hour Library visit.
- Title: Hotels & Lodging in Medora, ND
- Meta: Find hotels, cabins, and campgrounds in Medora, ND near Theodore Roosevelt National Park. Compare places to stay and book early for summer.
- Verify: Confirm that the Medora Stageline Trolley routes and listed hotel stops remain accurate and operating as described.

**/tr/presidency/food-and-drug**: The page ranks near the top of page one for high-volume definition and comparison queries, but it lacks a concise summary box distinguishing the Pure Food and Drug Act from the Meat Inspection Act to capture featured snippets and AI answers.
- Title: Pure Food and Drug Act of 1906 & Meat Inspection
- Meta: See how Upton Sinclair's The Jungle and Dr. Wiley's Poison Squad pushed Theodore Roosevelt to sign the Pure Food and Drug Act of 1906, creating the FDA.
- Verify: Verify that the enactment date of June 30, 1906 applies equally to both the Meat Inspection Act and the Pure Food and Drug Act as referenced in the text.; Check that Bureau of Chemistry is accurately cited as the sole enforcement arm specified in the 1906 act.

**/contact**: Expand the thin contact text with clear directions, location context in Medora, and practical visitor guidance so both searchers and AI engines get direct answers to address, phone, and trip inquiries.
- Title: Contact, Address & Location in Medora
- Meta: Find the address, phone number, and mailing details for the Theodore Roosevelt Presidential Library in Medora, North Dakota. Reach out or plan your trip.
- Verify: Verify whether 701-892-6070 is the primary general public visitor phone line or an administrative line.; Verify the exact URL and link text for the referenced hours page.

**/tr/people/archibald**: Add an easy-to-scan quick facts section to capture biographical queries like Archie's nickname and year of death, while aligning subheadings to match high-volume searches for 'Archie Roosevelt.'
- Title: Archie Roosevelt: TR's Son Wounded in Two World Wars
- Meta: Discover Archibald 'Archie' Roosevelt: TR's third son, wounded in both world wars, and the only soldier rated fully disabled twice. Read his story.
- Verify: Confirm middle name 'Bulloch' and whether he had four children, including Archibald Jr., with Grace.; Confirm exact month and year of Archie Roosevelt's death in 1979 if added to the text.

**/tr/rise-to-power/rough-riders**: Add a clear definition and summary at the top of the page answering who the Rough Riders were and what they did to capture top-ranking search snippets and AI overviews.
- Title: The Rough Riders: Who They Were and What They Did
- Meta: Who were the Rough Riders? Discover how 1,000 cowboys, miners, and Ivy League athletes trained in Texas and charged into history in Cuba.
- Verify: Verify that the official designation was the 1st U.S. Volunteer Cavalry and that it was raised in 1898 for the Spanish-American War.; Verify that the regiment disembarked at Daiquiri and disbanded at Montauk Point in September 1898 as stated in the draft summary.

**/visit/itineraries/enchanted-highway**: Turn this roadside itinerary into an essential regional road-trip connector between Bismarck, the Enchanted Highway, and Medora, highlighting how the 32-mile sculpture drive naturally pairs with a 3 1/2-hour visit to the Theodore Roosevelt Presidential Library.
- Title: Enchanted Highway Road Trip Guide: Map & Stops
- Meta: Plan your drive along North Dakota's Enchanted Highway to Regent. See all 7 giant scrap-metal sculptures, then head west to Medora. Get driving tips.
- Verify: Confirm that pairing the morning Enchanted Highway drive with an afternoon 3 1/2-hour visit to the Theodore Roosevelt Presidential Library fits current public access schedules.

**/about/trustees/kermit-roosevelt**: Expand Kermit Roosevelt's brief biography to explain his active role on the Board of Trustees and disambiguate him from his historical namesake relatives.
- Title: Kermit Roosevelt, Trustee
- Meta: Read the bio of Kermit Roosevelt, University of Pennsylvania law professor, novelist, and Theodore Roosevelt Presidential Library trustee.
- Verify: Confirm Kermit Roosevelt's official board title and start date at the Theodore Roosevelt Presidential Library.; Confirm whether Kermit Roosevelt should be formally styled as Kermit Roosevelt III on trustee listings.

## Visitor experience (/visit pages)
Findability 42/100, mobile speed 56/100, accessibility 96/100, average reading grade 8.3, 0 facts that disagree between pages.

### Can a first-time visitor find what they need?
| Page | Score | Missing or buried | Biggest fix |
|---|---|---|---|
| /visit | 82 | directions, food | Add clear parking instructions to the Directions section so drivers arriving in Medora know exactly where to park. |
| /visit/accessibility | 29 | hours, price, buy, visit_length, food | Explicitly state whether strollers are permitted alongside wheelchairs across pathways, exhibits, and the boardwalk. |
| /visit/directions | 68 | visit_length, accessibility | State upfront that visitors should allow about 3 1/2 hours at the Library so travelers can accurately budget their driving and arrival schedules. |
| /visit/eat | 14 | hours, price, buy, directions, visit_length, accessibility | Add a prominent link back to main visitor planning info—including Library hours, tickets, and parking—and clarify which downtown Medora eateries close outside the summer season. |
| /visit/faq | 75 |  | Add direct answers to top questions—like typical visit length, hours, and parking—directly on this hub page instead of sending visitors down multiple subpage links. |
| /visit/faq/tickets | 25 | hours, price, visit_length | Add standard ticket prices and note that visits take about 3 1/2 hours so visitors can plan their budget and schedule before starting checkout. |
| /visit/groups | 32 | hours, price, directions, accessibility, food | Add essential logistics for group coordinators, including daily operating hours, motorcoach parking, and bus drop-off instructions. |
| /visit/hours | 68 | visit_length, accessibility | Place the 3.5-hour visit length and 90-minute last-entry cutoff at the very top so mobile visitors understand timing before sorting through seasonal tables. |
| /visit/lodging | 25 | hours, price, directions, visit_length, accessibility, food | Advise visitors to allow at least 3 1/2 hours for the Library when choosing how many nights to book in Medora. |
| /visit/maps | 43 | visit_length, accessibility, food | Add an immediate mobile-friendly map preview with key amenities like parking, restrooms, accessible routes, and the 3 1/2 hour recommended visit pace. |
| /visit/tickets/plan-ahead | 0 | hours, price, buy, directions, visit_length, accessibility, food | Embed the working ticket calendar and add essential visit basics, including daily hours and the typical 3 1/2 hour visit length. |

### Slowest pages on mobile
| Page | Speed /100 | Load (s) |
|---|---|---|
| /visit/itineraries/roosevelt-triangle | 26 | 17.8 |
| /visit/stargazing | 26 | 16.9 |
| /visit/itineraries/dinosaurs | 28 | 7.6 |
| /visit/itineraries/7-day-billings-bismarck | 29 | 7 |
| /visit/itineraries/10-day-denver-salt-lake-city | 30 | 38.7 |
| /visit/itineraries/weekend-drives | 30 | 18.2 |
| /visit/shopping | 31 | 7 |
| /visit/activities | 32 | 5.1 |

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
0 broken internal addresses (0 links), 746 links worth adding, 45 pages with no links in, 20 topics with two pages, 41 broken outside links (LinkChecker scan 2026-11-09 04:24 UTC).

### Broken links on trlibrary.com: 301 redirects to add
Add a 301 redirect in Drupal (Configuration > Search and metadata > URL redirects) from each broken address to redirect_to; bulk import: https://seo.labs.trlibrary.com/data/redirects.csv. High confidence = safe; check medium/low first. Ticket-store paths should also be corrected on the page to the full access.trlibrary.com address.

_None._

### Links to add (highest value first; the [[bracketed]] words become the link)
| On page | Context | Link to |
|---|---|---|
| /tr/legacy/rankings | Roosevelt’s enduring popularity is carved in granite at [[Mount Rushmore]], beside Washington, Jefferson, and Lincoln. (National Park Service) | /tr/tr-mount-rushmore |
| /podcast/good-citizen/senator-chris-murphy | …ganized the neighborhood touch football games. When there was a dress code imposed at our [[high school]], I was the kid who everybody looked to go protest at the teacher's meeting, and I loved o… | /tr/for-educators/high-school |
| /tr/timeline | …velt had declared he would not run again, promoting the presidency of his cabinet member, [[William Howard Taft]] during the 1908 election. When Roosevelt returned home from his African safari in 1910, h… | /tr/people/william-howard-taft |
| /tr/tr-mount-rushmore | Learn more about Theodore Roosevelt and his concept of [[executive power]] with this Inquiry Design Model (IDM) lesson plan. | /tr/presidency/executive-power |
| /tr/timeline | …r, a Brazilian military officer suggested descending an unknown river: Rio da Dúvida, the [[River of Doubt]]. Together Roosevelt, his Brazilian counterpart expedition leader, Cândido Mariano da Silv… | /tr/post-presidency/river-of-doubt |
| /tr/timeline | Theodore and [[Edith Roosevelt]]’s first child, Theodore Jr. “Ted,” was born at the family home at Sagamore Hill in Oyster… | /tr/rise-to-power/edith-roosevelt |
| /tr/teddy-nickname | How much do you know about [[Theodore Roosevelt's early life]]? | /tr/early-life |
| /podcast/good-citizen/senator-chris-murphy | …y hand and say, I'd like to be a part of this. I'd like to run for office. I'd like to be [[in the room]] making decisions. And so I didn't wait. I have never ever looked back because I still do … | /visit/exhibits/kennerly |
| /tr/presidency-timeline | …ssia and Japan, the Russo-Japanese War ended in September 1905. Roosevelt was awarded the [[Nobel Peace Prize]] for his successful negotiations. He was not able to accept the prize in person. Instead, … | /tr/presidency/nobel-peace-prize |
| /tr/timeline | …tille Day—July 14, 1918—near Chamery, France. For several days after Quentin’s death, the [[Roosevelt family]] only knew that he had been reported missing. After learning of his death, 59-year-old The… | /tr/family |
| /tr/timeline | … 1905. Just over a year later, 48-year-old Roosevelt became the first American to win the [[Nobel Peace Prize]], announced on December 10, 1906. Roosevelt was not able to collect the prize himself and … | /tr/presidency/nobel-peace-prize |
| /tr/timeline | … Service under the Department of Agriculture. Theodore Roosevelt, then 46 years old, made [[Gifford Pinchot]] the first US Chief Forester. Throughout his presidency, Roosevelt was dedicated to the he… | /tr/presidency/conservation/gifford-pinchot |
| /tr/quotes/strenuous-life | — Speech at the dedication of a new [[high school]] building, Philadelphia, November 22, 1902 · ⁣ | /tr/for-educators/high-school |
| /podcast/good-citizen/ted-leonsis | …, who's also Greek, was 10 years younger than my dad. She grew up in Lowell and she was a [[high school]] grad as well. We rented an apartment on 44th Street between fifth and sixth avenues in Br… | /tr/for-educators/high-school |
| /podcast/good-citizen/candice-millard | …d cancer. One of the many, many things I learned, she's, by the way, she's graduated from [[high school]] this year, we're incredibly lucky. One of the many things I learned from that is how litt… | /tr/for-educators/high-school |
| /tr/timeline | … of four children, Theodore Roosevelt was born at 28 East 20th Street in New York City to [[Theodore Sr]]. “Thee” and Martha “Mittie” Bulloch Roosevelt. Born into a wealthy family, Roosevelt grew… | /tr/people/theodore-sr |
| /tr/homes-and-places/white-house | Decorations for [[Alice Roosevelt]]'s White House wedding, February 1906. (Frances Benjamin Johnston / Library of Congress) | /tr/people/alice-longworth |
| /tr/speeches/first-annual-message | Roosevelt used the [[bully pulpit]] to carry his vision to the public and build support for his agenda. He speaks here to a l… | /tr/presidency/bully-pulpit |
| /tr/fake-quotes | Learn more about Theodore Roosevelt and his concept of [[executive power]] with this Inquiry Design Model (IDM) lesson plan. | /tr/presidency/executive-power |
| /tr/people/henry-cabot-lodge | …osevelt, deserved party loyalty. Lodge also believed that some of Roosevelt's ideas about [[executive power]] and Progressive reform were too radical for his tastes. Yet Lodge also remained personall… | /tr/presidency/executive-power |
| /teach-tr | Learn about the [[Panama Canal]] and Theodore Roosevelt’s connection to the canal with this resource packet containing 13 … | /tr/presidency/panama-canal |
| /visit/exhibits/main | …eded reviving: he went looking for the wildest thing he could find. What he found was the [[River of Doubt]] — an uncharted Amazon tributary so unknown that no map could tell him where it went or wh… | /tr/post-presidency/river-of-doubt |
| /visit/exhibits/main | …12 — a work so rigorous the Navy would later place a copy on every ship. He fell hard for [[Alice Hathaway Lee]], courting her with headlong devotion until she agreed to marry him on his twenty-second b… | /tr/new-york-politics/alice-lee |
| /tr/rise-to-power/vice-presidency | The MacNaughton Cottage at Tahawus, where the [[Roosevelt family]] vacationed in the Adirondacks in the summer of 1901. (Harvard College Library) | /tr/family |
| /tr/presidency/foreign-policy | …ility to intervene in world affairs became mainstream American thinking. The assertion of [[executive power]] in foreign policy—the president's ability to act boldly without waiting for Congressional… | /tr/presidency/executive-power |
| /tr/teddy-nickname | …repressible small boy to his face as Mr. Roosevelt emerged from the Yosemite [hiking with [[John Muir]]]. This hail is said to have met with a prompt Presidential veto.” | /tr/people/john-muir |
| /visit/exhibits/main | At the center of it is [[Edith Roosevelt]] , whose steady hand shaped both the house and the role. She led a major renovation that g… | /tr/rise-to-power/edith-roosevelt |
| /tr/presidency/ten-facts | Roosevelt protected some 230 million acres of public land; here he stands with naturalist [[John Muir]] at Glacier Point in Yosemite, 1903. (Library of Congress) | /tr/people/john-muir |
| /visit/exhibits/main | The Republican establishment had shipped him off to the [[vice presidency]] to sideline him. When McKinley was killed, the man they couldn't control suddenly held th… | /tr/rise-to-power/vice-presidency |
| /podcast/good-citizen/live-trpl-2-johnny-morris-and-gov-kelly-armstrong-conservation-commerce-and | …n Juan Hill, leading his troops. I mean, yesterday morning when the first breakout of the [[Spanish American war]] were there in conflict in Cuba. And I was also reminded, my dad's birthday was July 13th,… | /tr/rise-to-power/spanish-american-war |
| /podcast/good-citizen/meg-whitman | …e been some real pearls of wisdom in here, and I really appreciate you taking the time to [[join us]]. | /join-us |
| /visit/exhibits/main | Look up. In the windows above, the house comes alive: silhouettes of the [[Roosevelt family]], and the very adventures Theodore is reading play out across the glass — the stories fill… | /tr/family |
| /tr/timeline | …sidency, Roosevelt was dedicated to the health and wellbeing of forests, establishing 150 [[national forests]]. | /tr/presidency/conservation/national-forests |
| /podcast/good-citizen/richard-haass | …read or write or count. Why do we think it's somehow acceptable to let them graduate from [[high school]] or college not understanding why democracy matters? One of the reasons American democracy… | /tr/for-educators/high-school |
| /podcast/good-citizen/leah-hunt-hendrix | …sure that I was always volunteering. I mean, I volunteered at Rikers Island when I was in [[high school]]. But a lot of the women's space was sometimes disconnected from specific solutions to eco… | /tr/for-educators/high-school |
| /programs | [[Join us]] live—online and in person. | /join-us |
| /podcast/good-citizen/doris-kearns-goodwin-presidential-stories-trpl-and-enduring-lessons-theodore | …And I think if there's any, one thing I'd love to do right now is to have every kid after [[high school]] go to a different part of America and have a common mission that they're working on in th… | /tr/for-educators/high-school |
| /visit/exhibits/main | …er. He helped end a war between Russia and Japan and became the first American to win the [[Nobel Peace Prize]] . At home, he laid groundwork for the federal safeguards that would become the FDA, champ… | /tr/presidency/nobel-peace-prize |
| /tr/homes-and-places/sagamore-hill | … Roosevelt family at Sagamore Hill in 1903: Theodore and Edith with their children Alice, [[Ted Jr]]., Kermit, Ethel, Archie and Quentin. (Harvard College Library) | /tr/people/ted-jr |
| /tr/presidency | [[Booker T. Washington]], October 1901 | /tr/people/booker-t-washington |

### Pages nothing links to
| Page | Title | Impr. |
|---|---|---|
| /tr/pre-presidency-political-accomplishments | WHAT WERE THEODORE ROOSEVELT’S FIVE SIGNIFICANT ACCOMPLISHMENTS PRIOR TO BECOMING PRESIDENT? | 53774 |
| /tr/10-myths-teddy-bear | TOP 10 MYTHS ABOUT THEODORE ROOSEVELT + THE INVENTION OF THE TEDDY BEAR | 17070 |
| /tr/fake-quotes | DID TR REALLY SAY THAT? | 15351 |
| /tr/5-big-adventures | TR’S FIVE BIG POST-PRESIDENTIAL ADVENTURES | 6211 |
| /research/books-by-roosevelt | TR's Published Books | 6050 |
| /programs | Programs | 4684 |
| /tr/tr-save-the-bison | DID THEODORE ROOSEVELT SAVE THE BISON? | 3841 |
| /join-us | Join Us | 3140 |
| /visit/medora/history | History of Medora | 2639 |
| /research/archives | Archives | 1861 |
| /events/teddycon | Theodore Roosevelt Convention (#TeddyCon) | 829 |
| /visit/teddy-trail | The Teddy Trail | 775 |
| /visit/exhibits/artificial-intelligence | Artificial Intelligence and Responsible Stewardship | 726 |
| /digital-guide | Free Digital Guide | 404 |
| /visit/roosevelt-in-medora | Roosevelt in Medora | 306 |
| /visit/weather | Weather | 290 |
| /visit/groups | Group Reservations | 231 |
| /vote | Step Into the Arena | 205 |
| /support/heritage-society | The TRPL HERITAGE SOCIETY | 153 |
| /research/family-tree | Theodore Roosevelt Family Tree / Theodore Roosevelt Presidential Library | 125 |
| /alexander-hamilton-speaks | Alexander Hamilton Speaks | 123 |
| /tr/badlands/timeline | The Badlands Years: 1883–1887 Timeline | 101 |
| /beam-signing-ceremony | Beam Signing Ceremony | 91 |
| /impact |  | 75 |
| /visit/groups/field-trips | Field Trips | 75 |

### Same topic, two pages
| Topic | Pages |
|---|---|
| mount rushmore | /tr/tr-mount-rushmore, /tr/legacy/mount-rushmore |
| rough riders | /tr/rise-to-power/san-juan-hill, /tr/rise-to-power/rough-riders |
| alice roosevelt longworth | /tr/people/alice-longworth, /tr/people/alice-longworth/complex-legacy |
| alice hathaway lee roosevelt | /tr/new-york-politics/alice-lee, /tr/people/alice-lee |
| alice lee | /tr/new-york-politics/alice-lee, /tr/people/alice-lee |
| edith roosevelt | /tr/rise-to-power/edith-roosevelt, /tr/people/edith-roosevelt |
| booker t washington | /tr/people/booker-t-washington, /tr/presidency/booker-t-washington |
| common misquotes | /tr/quotes/misquotes, /tr/myths/misquotes |
| gifford pinchot | /tr/presidency/conservation/gifford-pinchot, /tr/people/gifford-pinchot |
| ten facts | /tr/rise-to-power/ten-facts, /tr/badlands/ten-facts, /tr/early-life/ten-facts |
| elliott roosevelt | /tr/family/elliott-roosevelt, /tr/people/elliott |
| martha "mittie" bulloch roosevelt | /tr/early-life/mother, /tr/people/mittie |
| 7-day trip | /visit/itineraries/7-day-bismarck-rapid-city, /visit/itineraries/7-day-billings-bismarck |
| teaching theodore roosevelt | /tr/for-educators/elementary, /tr/for-educators/high-school, /tr/for-educators/middle-school |
| sagamore hill | /tr/homes-and-places/sagamore-hill, /tr/rise-to-power/sagamore-hill |

### Broken links to other websites (fix on the page; /video/ ones come from YouTube descriptions)
| Link | Status | On pages | Video page |
|---|---|---|---|
| https://www.theodorerooseveltcenter.org/encyclopedia/foreign-policy | 404 | /tr/complex-legacy/imperialism, /tr/presidency/panama-canal | False |
| https://abcnews.go.com/US/wireStory/reconstructed-road-opens-grand-views-theodore-roosevelt-national-127851476 | 404 | /press/clips | False |
| https://abcnews.go.com/US/wireStory/theodore-roosevelt-library-opening-visitors-pack-bag-north-126510433 | 404 | /press/clips | False |
| https://nam12.safelinks.protection.outlook.com/?url=https%3A%2F%2Ftedxfargo.us7.list-manage.com%2Ftrack%2Fclick%3Fu%3D42126281e0ac794ca800574d6%26id%3Df7ebdfb4ff%26e%3D1462c24ed9&data=05%7C02%7C%7C35bcbf6698764ab622a208dcb6cfbeee%7Cc3f9fd833dac4d1ea4c3573c4fcf9600%7C0%7C0%7C638586250598216425%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=nXcwCuy9%2FDCyUR0Q0K6LYfUovy2c365RPeUeFVqxr8c%3D&reserved=0 | 404 | /node/30 | False |
| https://nationaltoday.com/us/nd/medora-nd/news/2026/04/01/theodore-roosevelt-presidential-library-nears-completion/ | 404 | /press/clips | False |
| https://www.am1100theflag.com/show-episodes/74671-the-steve-hallstrom-show-episode-174-trump-is-selling-bibles-but-should-he-be | 404 | /press/clips | False |
| https://www.argusleader.com/story/news/2025/07/09/theodore-roosevelt-presidential-library-expected-to-open-in-july-2026/84505352007/ | 402 | /press/clips | False |
| https://www.detroitnews.com/story/opinion/2024/01/17/zito-t-r-s-presidential-library-comes-to-life-in-north-dakota/72251603007/ | 402 | /press/clips | False |
| https://www.fargomoorhead.org/teddy-roosevelt-trail/ | 404 | /visit/teddy-trail | False |
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
| https://www.theodorerooseveltcenter.org/encyclopedia/nature-and-conservation | 404 | /tr/homes-and-places/pine-knot | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/people/harvey-wiley | 404 | /tr/presidency/food-and-drug | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/personal-life/elkhorn-ranch | 404 | /tr/post-presidency/final-visit-medora | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/personal-life/family-and-friends/kermit | 404 | /tr/post-presidency/man-in-the-arena | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/politics-and-government/citizenship-in-a-republic | 404 | /tr/post-presidency/man-in-the-arena | False |
| https://www.theodorerooseveltcenter.org/encyclopedia/presidency | 404 | /tr/family/fdr-connection | False |
| https://www.theodorerooseveltcenter.org/media/Images/Blog/2019/Roosevelt_submarine-1024x854-2.jpg | 404 | /tr/presidency-timeline | False |
| https://www.theodorerooseveltcenter.org/timelines/roosevelt-badlands | 404 | /tr/people/marquis-de-mores | False |
| https://www.usatoday.com/story/news/politics/2026/07/01/roosevelt-library-set-to-open-to-public-on-independence-day/90714775007/ | 402 | /press/clips | False |
| https://www.usatoday.com/story/news/politics/2026/07/01/trump-dedicates-new-theodore-roosevelt-library/90760301007/ | 402 | /press/clips | False |

## Structured data (schema.org) for search engines and AI tools
292 of 888 content pages carry their own markup (33%); 6 sitewide issues (1 high). llms.txt on trlibrary.com: yes (draft: https://seo.labs.trlibrary.com/data/site-llms.txt).

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
| Trustee profiles | Person / ProfilePage | 14 | 14 | 14 | Add ProfilePage + Person JSON-LD (role: Trustee) to the trustee template. |
| Pages with Q&A | FAQPage | 20 | 19 | 0 | Add FAQPage JSON-LD to the accordion paragraph type: when every item's title is a question, output each as Question/Answer. One template change covers every FAQ page. |
| Good Citizen podcast page | PodcastSeries | 1 | 0 | 0 | Add PodcastSeries JSON-LD to the podcast landing page. |
| Calendar events | Event | 26 | 26 | 1 | Add Event JSON-LD to the Event content type template, filled from the event's date, time, price and ticket fields. One template change covers every event. |
| Staff profiles | Person / ProfilePage | 42 | 42 | 0 | Add ProfilePage + Person JSON-LD to the staff member template (name, job title, photo). |
| TR history articles | Article | 159 | 159 | 0 | Add Article JSON-LD to the /tr article template with about = Theodore Roosevelt (the sitewide #theodore-roosevelt entity) and dateModified from the node's changed date. |
| TR history: people | Article | 26 | 26 | 0 | Add Article JSON-LD to the /tr people template, with an 'about' Person; a field for the person's Wikidata link makes it precise. |
| TR history: speeches | Article | 6 | 6 | 0 | Add Article JSON-LD with an 'about' CreativeWork (the speech, author: Theodore Roosevelt). |

## Ticket checkout (GA4, rates only)
Checkout completion – (prior –); store visitors who buy 28% (prior 42%); ticket page to store 54%. Steps the store doesn't report: view_item, add_to_cart, begin_checkout, add_payment_info.

Store frustration signals (last 3 days, Clarity): dead clicks 15.2% of sessions, rage clicks 0.6%, quick backs 32.6%, scroll depth 78.5%.

| Store page | Dead % | Rage % | Quick back % | Scroll % |
|---|---|---|---|---|
| orders/tickets | 25 | 0 | 0 | 89 |
| membership/join | 0 | 0 | 0 | 60.5 |
| checkout/process | 50 | 0 | 0 | 100 |
| private-events/spaces | 100 | 0 | 0 | 99 |
| orders/calendar | 0 | 0 | 0 | 73.5 |
| checkout/confirm | 7.6 | 0 | 8.3 | 99.1 |
| events/detail | 0 | 0 | 0 | 100 |
| calendar/special-event/elkhorn-evenings | 0 | 0 | 0 | 96 |
| orders/forms | 0 | 0 | 0 | 100 |
| membership/detail | 0 | 0 | 1.7 | 94.5 |
| midwinter-table | 0 | 0 | 0 | 100 |
| visit/faq/rules-safety | 0 | 0 | 0 | 96 |
| tr/badlands/elkhorn-ranch | 0 | 0 | 0 | 5 |
| about/careers | 0 | 0 | 0 | 60.5 |
| auth/members | 50 | 0 | 0 | 100 |
| tr | 0 | 0 | 0 | 9 |
| membership/profile | 0 | 0 | 50 | 99.5 |
| tr/legacy/teddy-bear | 100 | 0 | 0 | 14 |
| tr/presidency/square-deal | 0 | 0 | 0 | 25 |
| tr/presidency/trust-busting | 20 | 0 | 0 | 58.9 |
| search | 0 | 0 | 0 | 100 |
| visit/wildlife | 0 | 0 | 0 | 100 |
| visit/exhibits | 0 | 0 | 50 | 56.5 |
| tr/tr-shot | 0 | 0 | 0 | 52 |
| membership/renew | 0 | 0 | 0 | 100 |
| staff-members/jeremy-beam | 0 | 0 | 0 | 92 |
| visit/planner | 0 | 0 | 0 | 100 |
| / | 0 | 0 | 0 | 100 |
| tr/for-educators/middle-school | 0 | 0 | 0 | 96 |
| visit | 0 | 0 | 0 | 38.3 |
| tr/speeches/man-in-the-arena | 33.3 | 0 | 0 | 70 |
| visit/faq | 0 | 0 | 0 | 63 |
| tr/rise-to-power/rough-riders | 0 | 0 | 0 | 52 |
| visit/scenic-drives | 0 | 0 | 0 | 99 |
| calendar/special-event | 0 | 0 | 0 | 83.4 |
| visit/activities | 100 | 0 | 0 | 35 |
| tickets | 0 | 0 | 0 | 7 |
| tr/early-life | 50 | 0 | 0 | 50.2 |
| support | 0 | 0 | 0 | 32 |
| visit/faq/tickets | 0 | 0 | 0 | 83.5 |
| tr/family/children | 0 | 0 | 0 | 81 |
| tr/myths | 0 | 0 | 0 | 80 |
| tr/presidency | 0 | 0 | 0 | 23 |
| calendar | 0 | 0 | 33.3 | 50.7 |
| staff-members/marcie-woehl | 0 | 0 | 0 | 95 |
| pay-balance/92V1G6OArFSfCjVtLeWEoDvBog3FRE9sL32OWk-cM7E9lS_goYPEJ66OsI7FilF1 | 100 | 0 | 0 | 100 |
| about/foundation | 0 | 0 | 100 | 37 |
| tr/myths/misquotes | 0 | 0 | 0 | 93 |
| legal/terms | 0 | 0 | 0 | 100 |
| tr/presidency/executive-actions/story | 0 | 0 | 0 | 22 |
| membership | 0 | 0 | 0 | 76.5 |
| podcast/good-citizen/carly-fiorina | 0 | 0 | 0 | 6 |
| contact | 0 | 0 | 0 | 96 |
| tr/presidency/conservation/reclamation | 0 | 0 | 0 | 38 |
| visit/directions/ev-charging | 0 | 0 | 0 | 26 |
| about/trustees | 0 | 0 | 0 | 96 |
| tr/rise-to-power | 0 | 0 | 0 | 50 |
| tr/quotes | 0 | 0 | 50 | 81 |
| tr/quotes/citizenship | 0 | 0 | 100 | 22 |
| staff-members/addison-olson | 100 | 0 | 0 | 100 |
| tr/family/fdr-connection | 0 | 0 | 0 | 4 |
| calendar/special-event/america-beautiful-film-screening | 0 | 0 | 0 | 12 |
| tr/speeches/first-annual-message | 0 | 0 | 0 | 85 |
| tr/quotes/leadership | 0 | 0 | 0 | 95 |
| about/trustees/theodore-roosevelt-v | 100 | 0 | 0 | 100 |
| tr/presidency/coal-strike | 0 | 0 | 0 | 10 |
| about/press | 0 | 0 | 0 | 80.3 |
| tr/speeches | 0 | 0 | 0 | 63.5 |
| user/login | 0 | 0 | 0 | 100 |
| video/view/W9sq8PuGQVo | 0 | 0 | 0 | 61 |
| tr/presidency/food-and-drug | 0 | 0 | 0 | 6 |
| tr/tr-importance | 0 | 0 | 0 | 60.5 |
| tr/presidency/panama-canal | 0 | 0 | 0 | 25 |
| video | 0 | 0 | 0 | 95 |
| pay-balance/wz7pBMk7BjmipyeTK02Dg6zliYK_wgEit5rTI6h1q3cIZmlrUoUAP7MWUIix3f5Z | 0 | 0 | 0 | 100 |
| video/playlist/PLWdA8F0rSmNg | 0 | 0 | 0 | 100 |
| legal/privacy | 0 | 0 | 0 | 10 |
| project/sustainability | 0 | 0 | 0 | 27 |
| visit/medora | 0 | 0 | 0 | 12 |
| visit/maps | 0 | 0 | 0 | 45 |
| tr/people/corinne | 0 | 0 | 0 | 13.7 |
| project/design | 0 | 0 | 0 | 53 |
| private-events | 0 | 0 | 0 | 95 |
| private-events/catering | 33.3 | 0 | 0 | 90 |
| research | 0 | 0 | 0 | 47 |
| tr/early-life/family-roots | 0 | 0 | 100 | 56 |

## Tracking changes made automatically
Rules and caps: config/tracking.yml. Keep an item permanently by copying it into config/keywords.yml or config/ai_prompts.yml; block it via tracking.yml exclude.

| Date | Change | Type | Item | Why |
|---|---|---|---|---|
| 2026-11-09 | added | question | Which four presidents are on Mount Rushmore, and why was Theodore Roosevelt included among them? | from the Google search "what presidents are on mount rushmore"; Connects Roosevelt to a major regional monument and invites context on his national significance. |
| 2026-11-09 | added | question | What years was Theodore Roosevelt president, and what were the dates of his administration? | from the Google search "when was teddy roosevelt president"; Foundational timeline query for TR's presidency. |
| 2026-11-09 | added | keyword | quentin roosevelt | position 11.2, 4775 impressions/28d; Theodore Roosevelt's youngest son, killed in action during World War I. |
| 2026-11-09 | added | keyword | who is on mount rushmore | position 6.7, 5233 impressions/28d; High-volume discovery query connecting Theodore Roosevelt's legacy to national landmark travel. |
| 2026-11-09 | added | keyword | kermit roosevelt | position 7.4, 9187 impressions/28d; Theodore Roosevelt's son and companion on the African and Amazon expeditions. |
| 2026-11-09 | added | keyword | man in the arena | position 6.1, 7558 impressions/28d; Theodore Roosevelt's most famous civic passage; core entry point for civic education. |
| 2026-11-09 | added | keyword | alice roosevelt | position 8.1, 11847 impressions/28d; High-volume search on Theodore Roosevelt's eldest daughter and White House icon. |
| 2026-11-02 | added | question | Which presidents are carved on Mount Rushmore, and why was Theodore Roosevelt included? | from the Google search "who is on mount rushmore"; High-volume inquiry connecting Roosevelt to regional Northern Plains travel and heritage. |
| 2026-11-02 | added | question | What years was Theodore Roosevelt in office, and what were the major milestones of his administration? | from the Google search "when was theodore roosevelt president"; Core presidential timeline search; establishes authority on his administration. |
| 2026-11-02 | added | keyword | bull moose party | position 4.4, 6818 impressions/28d; Roosevelt's historic 1912 third-party presidential campaign |
| 2026-11-02 | added | keyword | alice roosevelt longworth | position 8.5, 9143 impressions/28d; Roosevelt's eldest daughter and a prominent public figure in her own right |
| 2026-11-02 | added | keyword | jacob riis | position 10.2, 20915 impressions/28d; Key Progressive Era ally and close associate during Roosevelt's New York years |
| 2026-11-02 | added | keyword | roosevelt corollary | position 4.7, 23395 impressions/28d; Major foreign policy doctrine central to Roosevelt's presidency and US history curricula |
| 2026-11-02 | added | keyword | brownsville affair | position 5.6, 111795 impressions/28d; Key civil rights controversy from Theodore Roosevelt's presidency |
| 2026-10-26 | added | question | Can you explain Theodore Roosevelt's Square Deal domestic policy and its main goals? | from the Google search "what was the square deal"; Signature domestic policy topic essential for student research and civic education. |

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
