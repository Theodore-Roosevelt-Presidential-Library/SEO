# SEO: Search & AI Visibility for trlibrary.com

A SEMrush-style dashboard built for one site, trlibrary.com. GitHub Actions collects the data and GitHub Pages serves the dashboard at **https://seo.labs.trlibrary.com**.

| Tab | What it shows | Source | Needs a key? |
|---|---|---|---|
| Overview | Clicks, impressions, CTR, position, site health, AI mention rate, quick wins | All of the below | – |
| Search | Every search and page from the last 28 days, compared with the prior 28 | Google Search Console | Yes |
| Opportunities | Striking-distance searches, high-ranking pages people skip, search words missing from titles, falling pages, pages competing with each other | Search Console + audit | No (uses the others) |
| Rankings | Tracked keywords: Search Console position, live Google rank, AI Overview presence and whether it cites us, who ranks above us, monthly volume | Search Console + DataForSEO | DataForSEO optional |
| AI Visibility | Weekly answers from ChatGPT, Gemini, Perplexity and Claude to real travel and history questions: mentioned or not, rank among nearby attractions, sources cited | Each AI's API | Yes, any one |
| Site Audit | Crawls every sitemap URL for titles, descriptions, H1s, canonicals, Open Graph, alt text, thin pages, redirects, `/node/` URLs, AI-crawler access in robots.txt, llms.txt and structured data | trlibrary.com itself | No |
| Recommendations | Claude's drafts of new titles, meta descriptions and content additions for the highest-upside pages, plus a weekly brief on AI visibility | Anthropic API | Yes |
| Setup | Whether each source is on, when it last ran, and any error | – | – |

**Schedule:**
- Daily, around 7am Mountain: Search Console and opportunities.
- Mondays, around 6am Mountain: everything else.

Each source switches on as soon as its secret exists. If a source has no key, it's skipped, and the Setup tab says why.

## One-time setup

### 1. Turn on Pages
Go to **Settings → Pages**. Set Source to **Deploy from a branch**, Branch to `main`, and folder to `/docs`. The custom domain `seo.labs.trlibrary.com` comes from `docs/CNAME`. The wildcard `*.labs.trlibrary.com` DNS already points at the org's Pages, so no DNS change is needed. Tick **Enforce HTTPS** once the certificate is issued.

### 2. Allow Actions to commit
Go to **Settings → Actions → General → Workflow permissions** and select **Read and write permissions**.

### 3. Add secrets
Add these under **Settings → Secrets and variables → Actions → New repository secret**. Each one is optional, so add them in any order.

**Google Search Console** (`GSC_SERVICE_ACCOUNT_JSON`). This is the most valuable one, and it's free.
1. In Google Cloud Console, pick or create a project and enable the **Google Search Console API**.
2. Under **IAM & Admin → Service accounts**, create a service account. No roles are needed.
3. On that account, go to **Keys → Add key → JSON** and download the file.
4. In Search Console, open the trlibrary.com property. Go to **Settings → Users and permissions → Add user**, paste the service account's email address, and choose **Restricted** permission.
5. Paste the entire contents of the JSON file as the secret value.
6. Check `gsc_property` in `config/site.yml`. Use `sc-domain:trlibrary.com` for a Domain property, or `https://www.trlibrary.com/` for a URL-prefix property.

**DataForSEO** (`DATAFORSEO_LOGIN`, `DATAFORSEO_PASSWORD`). This adds live Google ranks, AI Overview tracking and search volumes. It's pay-as-you-go: sign up at dataforseo.com and copy the API login and password from the dashboard. At about 20 keywords a week this should cost a few dollars a month, but check their current pricing.

**AI assistants** (any of `OPENAI_API_KEY`, `GEMINI_API_KEY`, `PERPLEXITY_API_KEY`, `ANTHROPIC_API_KEY`):
- OpenAI: platform.openai.com
- Gemini: aistudio.google.com
- Perplexity: perplexity.ai/settings/api
- Anthropic: console.anthropic.com

Fifteen questions across four assistants is 60 calls a week. Model names live in `config/site.yml`. If the Setup tab reports "model not found", update the name there.

**Recommendations** (`ANTHROPIC_API_KEY`) uses the same key as Claude above.

### 4. First run
Go to **Actions → Weekly refresh → Run workflow**. It takes about five minutes. The dashboard updates once the commit lands.

## Changing what's tracked
All tracking is controlled by three files in `config/`. Edit them on GitHub; the next run picks up the changes.
- `config/keywords.yml`: the searches tracked on the Rankings tab, in groups.
- `config/ai_prompts.yml`: the questions asked to AI assistants. Keep each `id` stable so its history continues.
- `config/site.yml`:
  - brand names counted as a "mention"
  - nearby attractions to compare against
  - audit settings (pages to skip, the title suffix to ignore)
  - model names

## Editorial guardrails
Recommendations are drafts, and nothing is published automatically. The instructions Claude receives (`seo/tips.py`) require it to:
- write in house voice, with minimal "we/our"
- keep years out of visitor copy
- keep the 3½-hour visit standard
- stay nonpartisan
- never invent historical facts
- never quote or paraphrase TR

Anything touching history is listed under **Verify before publishing**. Suggested titles and descriptions are length-checked, and any that contain a year are flagged.

## Data and privacy
The repo and dashboard are public. They hold:
- site performance data: search terms, clicks and rankings
- public AI answers
- audit results

They hold no personal data. Google already withholds rare searches from Search Console for privacy.

## Running locally
```bash
pip install -r requirements.txt pytest
python -m pytest -q tests
python -m seo.run audit                 # no keys needed
GSC_SERVICE_ACCOUNT_JSON="$(cat key.json)" python -m seo.run gsc opportunities
python -m http.server -d docs 8000      # then open http://localhost:8000
```
Job names: `gsc`, `audit`, `ranks`, `ai_visibility`, `opportunities`, `tips`, or the bundles `daily` and `weekly`.

## Layout
```
config/            what to track (edit these)
seo/               Python collectors and analysis, run by Actions
docs/              the dashboard (static HTML/JS) served by Pages
docs/data/         JSON written by the jobs (committed by Actions)
.github/workflows/ daily.yml, weekly.yml, tests.yml
```
