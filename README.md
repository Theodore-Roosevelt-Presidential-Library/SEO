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
| Recommendations | AI-drafted new titles, meta descriptions and content additions for the highest-upside pages, plus a weekly brief on AI visibility | Gemini, Claude, ChatGPT or Perplexity | Yes, any one |
| Setup | Whether each source is on, when it last ran, and any error | – | – |

**Schedule:**
- Daily, around 7am Mountain: Search Console and opportunities.
- Mondays, around 6am Mountain: everything else.

Each source switches on as soon as its secret exists. If a source has no key, it's skipped, and the Setup tab says why.

## One-time setup

### 0. Install the workflows
Move the three files in `setup/workflows/` into `.github/workflows/`, then delete the empty `setup/` folder. From the repo folder, run:
```bash
mkdir -p .github/workflows && git mv -f setup/workflows/*.yml .github/workflows/ 2>/dev/null || mv setup/workflows/*.yml .github/workflows/
```

### 1. Turn on Pages
Go to **Settings → Pages**. Set Source to **Deploy from a branch**, Branch to `main`, and folder to `/docs`. The custom domain `seo.labs.trlibrary.com` comes from `docs/CNAME`. The wildcard `*.labs.trlibrary.com` DNS already points at the org's Pages, so no DNS change is needed. Tick **Enforce HTTPS** once the certificate is issued.

### 2. Allow Actions to commit
Go to **Settings → Actions → General → Workflow permissions** and select **Read and write permissions**.

### 3. Add secrets
Add these under **Settings → Secrets and variables → Actions → New repository secret**. Each one is optional, so add them in any order.

**Google Search Console** (free, and the most valuable source). GitHub signs in to Google with a short-lived token (Workload Identity Federation), so no key file is ever created. That matters because TRPL's Google Cloud organization blocks service account keys (`iam.disableServiceAccountKeyCreation`), which is Google's secure default.

1. In Google Cloud Console, pick the project and enable two APIs: **Google Search Console API** and **IAM Service Account Credentials API**.
2. Under **IAM & Admin → Service accounts**, create a service account (for example, `seo-dashboard`). No roles are needed. Copy its email address.
3. In Search Console, open the trlibrary.com property. Go to **Settings → Users and permissions → Add user**, paste the service account's email address, and choose **Restricted**.
4. Open Cloud Shell (the `>_` icon in the Cloud Console) and run the commands below, filling in your project ID. They only allow GitHub Actions runs from this repo to use the service account.
   ```bash
   PROJECT_ID=your-project-id
   SA=seo-dashboard@$PROJECT_ID.iam.gserviceaccount.com
   REPO=Theodore-Roosevelt-Presidential-Library/SEO
   PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')

   gcloud iam workload-identity-pools create github --project=$PROJECT_ID --location=global --display-name="GitHub Actions"
   gcloud iam workload-identity-pools providers create-oidc github-repos --project=$PROJECT_ID --location=global \
     --workload-identity-pool=github --issuer-uri=https://token.actions.githubusercontent.com \
     --attribute-mapping="google.subject=assertion.sub,attribute.repository=assertion.repository" \
     --attribute-condition="assertion.repository=='$REPO'"
   gcloud iam service-accounts add-iam-policy-binding $SA --project=$PROJECT_ID \
     --role=roles/iam.workloadIdentityUser \
     --member="principalSet://iam.googleapis.com/projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/github/attribute.repository/$REPO"

   echo "GCP_WIF_PROVIDER = projects/$PROJECT_NUMBER/locations/global/workloadIdentityPools/github/providers/github-repos"
   echo "GCP_SERVICE_ACCOUNT = $SA"
   ```
5. In the repo, go to **Settings → Secrets and variables → Actions → Variables** (the Variables tab, not Secrets). Add `GCP_WIF_PROVIDER` and `GCP_SERVICE_ACCOUNT` with the two values the last commands printed. These aren't secret.
6. Check `gsc_property` in `config/site.yml`. Use `sc-domain:trlibrary.com` for a Domain property, or `https://www.trlibrary.com/` for a URL-prefix property.

If your Google organization does allow key creation, a JSON key pasted into the secret `GSC_SERVICE_ACCOUNT_JSON` also works. Workload Identity Federation is the safer option.

**DataForSEO** (`DATAFORSEO_LOGIN`, `DATAFORSEO_PASSWORD`). This adds live Google ranks, AI Overview tracking and search volumes. It's pay-as-you-go: sign up at dataforseo.com and copy the API login and password from the dashboard. At about 20 keywords a week this should cost a few dollars a month, but check their current pricing.

**AI assistants** (any of `OPENAI_API_KEY`, `GEMINI_API_KEY`, `PERPLEXITY_API_KEY`, `ANTHROPIC_API_KEY`):
- OpenAI: platform.openai.com
- Gemini: aistudio.google.com
- Perplexity: perplexity.ai/settings/api
- Anthropic: console.anthropic.com

Fifteen questions across four assistants is 60 calls a week. Model names live in `config/site.yml`. If the Setup tab reports "model not found", update the name there.

**Recommendations** need no extra key. They use whichever AI key you've added, Gemini first by default. Change the order with `tips.prefer` in `config/site.yml`.

### 4. First run
Go to **Actions → Weekly refresh → Run workflow**. It takes about five minutes. The dashboard updates once the commit lands.

## For AI tools (llms.txt)
The dashboard is drawn with JavaScript, so AI assistants that fetch it see an empty page. Every run also writes plain-text versions:
- **https://seo.labs.trlibrary.com/llms.txt**: the entry point. It says what's here, gives a snapshot, links every data file, and lists the house rules for suggesting copy.
- **https://seo.labs.trlibrary.com/digest.md**: a one-page ranked briefing (about 25 KB) that an AI tool can read in a single fetch.
- **https://seo.labs.trlibrary.com/data/digest.json**: the same content as structured data, for scripts.

To use it, tell Claude (or any assistant): "Read https://seo.labs.trlibrary.com/llms.txt and tell me the five best ways to improve our SEO this week."

## Self-managing tracking
Each week the tool adds promising keywords and AI questions on its own, and retires ones that are done. Your files `config/keywords.yml` and `config/ai_prompts.yml` are never changed.

- **Adding keywords:** searches where trlibrary.com ranks 4–30 with real demand (300+ impressions in 28 days, two or more words, non-branded). They're ranked by how many extra clicks a top-3 spot would bring, with a boost for rising searches.
- **Adding AI questions:** question-style Google searches ("what was the square deal", "things to do near medora"). If any AI key is set, the AI rewrites each one the way a traveler or student would ask an assistant.
- **AI filter:** when any AI key is set, candidates are screened against the goals in `config/tracking.yml`, so off-mission searches such as podcast guests' names are dropped. Without a key, only the rules and the exclude list apply.
- **Retiring:**
  - A keyword **graduates** after four weekly checks in the top 3.
  - A keyword is **retired** when its searches dry up.
  - A question **graduates** once every assistant has mentioned the Library four weeks running.
  - Retired items can't come back for 12 weeks.
- **Caps** (all in `config/tracking.yml`):
  - At most 25 discovered keywords and 8 discovered questions at once.
  - At most 5 new keywords and 2 new questions a week.
- **Your controls:**
  - To keep an item for good, copy it into `keywords.yml` or `ai_prompts.yml`.
  - To block an item or a pattern, add it under `exclude` in `tracking.yml`.
- **Where to see it:** every change and its reason is listed under "What the system changed" on the Rankings and AI Visibility tabs, and in `digest.md`.

Added keywords raise DataForSEO costs by about half a cent per keyword per week, so 25 discovered keywords add about $0.55 a month.

## Visitor Experience and Checkout tabs

**Visitor Experience** checks every page under `/visit` once a week:
- **Speed and accessibility:** Google PageSpeed scores on a phone, real-visitor load times where Chrome has enough data, and the specific accessibility checks that fail.
- **Reading level:** grade level (aim for 8) and how far down the first ticket link sits.
- **Visitor tasks:** on the key pages, an AI (any configured key) reads the page as a first-time visitor and checks whether it answers the basics: hours, price, where to buy, directions and parking, visit length, accessibility, food. Each is marked found near the top, buried, linked, or missing.
- **Contradictions:** it collects the facts each page states and flags pages that disagree, such as different hours.

Key pages and tasks are set in `config/site.yml` under `ux`.

**Checkout** measures the ticket store (`access.trlibrary.com`, run by ACME) from GA4: how many store visitors add tickets, start checkout and buy. Only **rates** are published, never visitor or order counts or revenue. Rates based on fewer than 30 people show as "low volume". If the store doesn't report a step to GA4, the tab lists it so it can be raised with ACME.

### Setup
1. **PageSpeed (`PAGESPEED_API_KEY`, required):** Google's keyless quota is shared and usually used up.
   - In Google Cloud Console (project `civic-depth-505307-c4`), enable the **PageSpeed Insights API**.
   - Go to **APIs & Services → Credentials → Create credentials → API key**, and restrict the key to the PageSpeed Insights API.
   - Add it as the secret `PAGESPEED_API_KEY`.
2. **GA4 (`GA4_PROPERTY_ID` variable):**
   - In Google Cloud, enable the **Google Analytics Data API**.
   - In GA4, go to **Admin → Property access management**, add `seo-dashboard@civic-depth-505307-c4.iam.gserviceaccount.com` as a **Viewer**.
   - Copy the numeric **Property ID** from **Admin → Property details** and add it as the repo **variable** `GA4_PROPERTY_ID`.

   This turns on the Checkout tab and the engagement columns on Visitor Experience.
3. **Microsoft Clarity (`CLARITY_API_TOKEN`, optional):** in Clarity, open the trlibrary.com project and go to **Settings → Data Export → Generate new API token**. Add it as the secret `CLARITY_API_TOKEN`. This adds rage clicks, dead clicks and scroll depth for the last three days, which is all Clarity's API provides.

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
Recommendations are drafts, and nothing is published automatically. Whichever model writes them gets the same instructions (`seo/tips.py`), which require it to:
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
gcloud auth application-default login --scopes=https://www.googleapis.com/auth/webmasters.readonly,https://www.googleapis.com/auth/cloud-platform
GOOGLE_APPLICATION_CREDENTIALS=~/.config/gcloud/application_default_credentials.json python -m seo.run gsc opportunities
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
