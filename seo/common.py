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
