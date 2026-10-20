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
