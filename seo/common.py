"""Shared helpers: config, data files, run status, HTTP session."""
from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT / "config"
DATA_DIR = Path(os.environ.get("SEO_DATA_DIR", ROOT / "docs" / "data"))


# ---------- config ----------

def load_yaml(name: str) -> dict:
    with open(CONFIG_DIR / name, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def config() -> dict:
    return load_yaml("site.yml")


def env(name: str) -> str | None:
    val = os.environ.get(name, "").strip()
    return val or None


# ---------- time ----------

def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def today() -> dt.date:
    return dt.datetime.now(dt.timezone.utc).date()


# ---------- data files ----------

def data_path(rel: str) -> Path:
    p = DATA_DIR / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def read_json(rel: str, default=None):
    p = DATA_DIR / rel
    if not p.exists():
        return default
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def write_json(rel: str, obj) -> Path:
    p = data_path(rel)
    tmp = p.with_suffix(p.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        # Big files are written compactly to keep daily commits (and the repo) small.
        big = isinstance(obj, list) and len(obj) > 500
        json.dump(obj, fh, ensure_ascii=False, indent=None if big else 1,
                  separators=(",", ":") if big else None)
        fh.write("\n")
    tmp.replace(p)
    return p


def upsert_history(rel: str, row: dict, key: str = "date", keep: int = 400) -> list:
    """Append a row to a history list, replacing any row with the same key."""
    hist = read_json(rel, []) or []
    hist = [r for r in hist if r.get(key) != row.get(key)]
    hist.append(row)
    hist.sort(key=lambda r: r.get(key, ""))
    hist = hist[-keep:]
    write_json(rel, hist)
    return hist


# ---------- run status (drives the "Setup" panel on the dashboard) ----------

class JobError(RuntimeError):
    """Raised after a job has recorded its own error status."""


def set_status(job: str, state: str, message: str = "", **extra) -> None:
    """state: ok | skipped | error"""
    status = read_json("status.json", {}) or {}
    status[job] = {"state": state, "message": message, "updated": now_iso(), **extra}
    write_json("status.json", status)
    log(f"[{job}] {state}: {message}")


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


# ---------- HTTP ----------

def session(user_agent: str | None = None) -> requests.Session:
    s = requests.Session()
    s.headers["User-Agent"] = user_agent or "TRPL-SEO/1.0 (+https://seo.labs.trlibrary.com)"
    adapter = requests.adapters.HTTPAdapter(pool_connections=16, pool_maxsize=16, max_retries=2)
    s.mount("https://", adapter)
    s.mount("http://", adapter)
    return s


# ---------- text helpers ----------

def domain_of(url: str) -> str:
    host = urlparse(url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def norm_url(url: str) -> str:
    """Normalise a URL for matching across GSC, sitemap and crawl."""
    u = urlparse(url.strip())
    host = u.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = u.path or "/"
    if len(path) > 1 and path.endswith("/"):
        path = path[:-1]
    return f"{host}{path}"


def brand_regex(terms: list[str]) -> re.Pattern:
    parts = sorted((re.escape(t) for t in terms), key=len, reverse=True)
    return re.compile(r"(?<![\w.])(" + "|".join(parts) + r")(?![\w])", re.I)


STOPWORDS = set("""a an and are at be by can do for from how i in is it me my near
of on or the to what when where which who why with you your best top things
""".split())


def content_words(text: str) -> list[str]:
    return [w for w in re.findall(r"[a-z0-9']+", text.lower()) if w not in STOPWORDS and len(w) > 1]


GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"


def gemini_post(sess, key: str, model: str, body: dict, timeout: int = 240):
    """POST to Gemini. If Google says the model is retired and names a
    replacement ("...use models/NAME..."), retry once with that model."""
    import time
    for attempt in range(4):
        r = sess.post(GEMINI_URL.format(model=model), params={"key": key}, json=body, timeout=timeout)
        if r.status_code not in (429, 503) or attempt == 3:
            break
        # Rate limited: wait as long as Google asks (retryDelay "NNs"), else back off.
        m = re.search(r'"retryDelay":\s*"(\d+)', r.text)
        wait = min(int(m.group(1)) + 2, 90) if m else 20 * (attempt + 1)
        log(f"Gemini {r.status_code}; waiting {wait}s before retrying")
        time.sleep(wait)
    if r.status_code == 404:
        m = re.search(r"use models/([\w.\-]+)", r.text)
        if m and m.group(1) != model:
            log(f"Gemini model {model} retired; retrying with {m.group(1)}. Update config/site.yml.")
            r = sess.post(GEMINI_URL.format(model=m.group(1)), params={"key": key}, json=body, timeout=timeout)
    return r


def perplexity_agent(sess, key: str, text: str, preset: str = "fast", model: str | None = None,
                     instructions: str | None = None, timeout: int = 240) -> dict:
    """Perplexity's Agent API (replaced Sonar / chat-completions). Returns
    {"text": answer, "citations": [urls]}. Tries /v1/responses (named in
    Perplexity's error message), then /v1/agent (named in their docs)."""
    body: dict = {"input": text}
    if model and model not in ("sonar", "sonar-pro", "fast"):
        body["model"] = model      # e.g. "openai/gpt-5.6-luna" to pin a specific model
    else:
        body["preset"] = preset    # fast | low | medium | high | xhigh
    if instructions:
        body["instructions"] = instructions
    headers = {"Authorization": f"Bearer {key}"}
    r = None
    for path in ("/v1/responses", "/v1/agent"):
        r = sess.post(f"https://api.perplexity.ai{path}", json=body, headers=headers, timeout=timeout)
        if r.status_code == 400 and instructions and "instructions" in r.text:
            # older/stricter schema: fold the instructions into the input instead
            body.pop("instructions", None)
            body["input"] = f"{instructions}\n\n{text}"
            r = sess.post(f"https://api.perplexity.ai{path}", json=body, headers=headers, timeout=timeout)
        if r.status_code not in (404, 405):
            break
    if r.status_code != 200:
        raise RuntimeError(f"Perplexity {r.status_code}: {r.text[:200]}")
    d = r.json()
    texts, cites = [], []
    for item in d.get("output") or []:
        if item.get("type") == "message":
            for c in item.get("content") or []:
                if c.get("type") == "output_text":
                    texts.append(c.get("text", ""))
                    cites += [a.get("url") for a in c.get("annotations") or [] if a.get("url")]
        elif item.get("type") == "search_results":
            cites += [x.get("url") for x in item.get("results") or [] if x.get("url")]
    if not texts and d.get("output_text"):
        texts.append(d["output_text"])
    return {"text": "\n".join(texts), "citations": list(dict.fromkeys(c for c in cites if c)), "status_code": r.status_code}


# ---------- Google sign-in shared by Search Console and GA4 ----------

def google_token(scopes: list[str]) -> str | None:
    """Short-lived Google access token from the keyless Workload Identity
    Federation sign-in (or a JSON key in GSC_SERVICE_ACCOUNT_JSON). None if
    neither is set up."""
    import json as _json
    sa = env("GSC_SERVICE_ACCOUNT_JSON")
    if not sa and not env("GOOGLE_APPLICATION_CREDENTIALS"):
        return None
    import google.auth
    import google.auth.transport.requests as gtr
    from google.oauth2 import service_account
    if sa:
        creds = service_account.Credentials.from_service_account_info(_json.loads(sa), scopes=scopes)
    else:
        creds, _ = google.auth.default(scopes=scopes)
    creds.refresh(gtr.Request())
    return creds.token


class GA4:
    """Minimal Google Analytics 4 Data API client (runReport)."""
    SCOPE = "https://www.googleapis.com/auth/analytics.readonly"

    def __init__(self, property_id: str, token: str):
        self.url = f"https://analyticsdata.googleapis.com/v1beta/properties/{property_id}:runReport"
        self.s = session()
        self.s.headers["Authorization"] = f"Bearer {token}"

    @classmethod
    def from_env(cls) -> "GA4 | None":
        pid = env("GA4_PROPERTY_ID")
        if not pid:
            return None
        tok = google_token([cls.SCOPE])
        return cls(pid.replace("properties/", ""), tok) if tok else None

    def report(self, dims: list[str], metrics: list[str], start: str = "28daysAgo", end: str = "yesterday",
               dim_filter: dict | None = None, limit: int = 10000) -> list[dict]:
        body = {"dimensions": [{"name": d} for d in dims], "metrics": [{"name": m} for m in metrics],
                "dateRanges": [{"startDate": start, "endDate": end}], "limit": limit}
        if dim_filter:
            body["dimensionFilter"] = dim_filter
        r = self.s.post(self.url, json=body, timeout=60)
        if r.status_code != 200:
            raise RuntimeError(f"GA4 API {r.status_code}: {r.text[:300]}")
        out = []
        for row in r.json().get("rows", []) or []:
            rec = {d: v["value"] for d, v in zip(dims, row.get("dimensionValues", []))}
            for m, v in zip(metrics, row.get("metricValues", [])):
                try:
                    rec[m] = float(v["value"])
                except (TypeError, ValueError):
                    rec[m] = None
            out.append(rec)
        return out


def ga4_filter(field: str, value: str, match: str = "EXACT") -> dict:
    return {"filter": {"fieldName": field, "stringFilter": {"matchType": match, "value": value}}}


def ga4_and(*filters: dict) -> dict:
    return {"andGroup": {"expressions": list(filters)}}


def ga4_in(field: str, values: list[str]) -> dict:
    return {"filter": {"fieldName": field, "inListFilter": {"values": values}}}


# ---------- Microsoft Clarity data export ----------

CLARITY_METRICS = {"DeadClickCount": "dead_clicks", "RageClickCount": "rage_clicks", "QuickbackClick": "quick_backs",
                   "ScrollDepth": "scroll_depth", "ExcessiveScroll": "excessive_scroll"}


def _clarity_value(info: dict):
    for k in ("sessionsWithMetricPercentage", "averageScrollDepth", "averageScroll"):
        if info.get(k) is not None:
            try:
                return round(float(info[k]), 1)
            except (TypeError, ValueError):
                pass
    return None


def clarity_insights(token: str, by_url: bool = True, days: int = 3) -> tuple[dict, dict]:
    """Clarity's live-insights export (last 1-3 days; 10 calls per project per day).
    Returns (per_url, overall): percentages of sessions with each frustration
    signal, plus average scroll depth. Never returns session counts."""
    from urllib.parse import urlparse
    url = "https://www.clarity.ms/export-data/api/v1/project-live-insights"
    hdr = {"Authorization": f"Bearer {token}"}
    per_url: dict = {}
    overall: dict = {}
    calls = [(True, {"numOfDays": days, "dimension1": "URL"})] if by_url else []
    calls.append((False, {"numOfDays": days}))
    for is_url, params in calls:
        r = session().get(url, params=params, headers=hdr, timeout=60)
        if r.status_code != 200:
            raise RuntimeError(f"Clarity {r.status_code}: {r.text[:150]}")
        for metric in r.json() or []:
            name = CLARITY_METRICS.get(metric.get("metricName"))
            if not name:
                continue
            for info in metric.get("information") or []:
                val = _clarity_value(info)
                if val is None:
                    continue
                if is_url:
                    u = next((v for k, v in info.items() if k.lower() == "url"), None)
                    if u:
                        p = urlparse(u)
                        per_url.setdefault((p.netloc, p.path.rstrip("/") or "/"), {})[name] = val
                else:
                    overall[name] = val
    return per_url, overall
