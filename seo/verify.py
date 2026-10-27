"""Read a page the way a visitor does, and check AI claims against it.

Two jobs:

1. main_text(): the full text of a page's main content in reading order, with
   headings marked "# ". It includes text in divs, spans, tables, accordions and
   tabs (Drupal Layout Builder puts a lot there), and it never cuts a section
   in half: if a page is too long, it stops at a heading boundary and says so.

   Why: the AI checks used to read only <p>/<li> text, cut at 8-9,000
   characters. On /visit/hours the hours sit in <span>s, so the AI was told
   there were no hours. On /visit/lodging the cut landed mid-sentence, so it
   reported a truncated sentence. On /visit/directions the cut landed right after
   the "Getting Around Town" heading, so the section looked empty.

2. check_claim(): a few kinds of AI claim are easy to test mechanically
   ("this section is empty", "the page has no hours", "add the visit length",
   "the sentence is cut off", "duplicate H1"...). Each claim is tested against
   the live page; claims the page contradicts are dropped and listed, so the
   dashboard shows only what holds up.
"""
from __future__ import annotations

import re

from bs4 import BeautifulSoup, NavigableString

HEADINGS = ("h1", "h2", "h3", "h4", "h5", "h6")
BLOCKS = HEADINGS + ("p", "li", "div", "section", "article", "td", "th", "tr", "dt", "dd", "summary",
                     "details", "figcaption", "blockquote", "br", "ul", "ol", "table", "button", "label")
DROP = ("script", "style", "noscript", "nav", "header", "footer", "form", "svg", "template", "iframe")
ICONS = re.compile(r"^(keyboard_arrow_\w+|expand_(more|less)|chevron_\w+|play_circle|arrow_\w+)\s*")

TIME_RE = re.compile(r"\b\d{1,2}(:\d{2})?\s*(a\.?m\.?|p\.?m\.?)\b|\b\d{1,2}:\d{2}\b", re.I)
LENGTH_RE = re.compile(r"three and a half hours|3\s*(1/2|½|\.5)[\s-]*hours?|three-and-a-half", re.I)
PRICE_RE = re.compile(r"\$\s?\d+|\bfree admission\b|\badmission is free\b", re.I)
TERMINAL = re.compile(r"[.!?…:\"”’)\]]\s*$")


def _soup_main(html: str):
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main") or soup.body or soup
    for t in main.find_all(DROP):
        t.decompose()
    for t in main.select(".visually-hidden, .breadcrumb, [aria-label=breadcrumb]"):
        t.decompose()
    return soup, main


def main_lines(html: str) -> list[str]:
    """Main-content text, one block per line, headings prefixed with '# '."""
    _, main = _soup_main(html)
    for h in main.find_all(HEADINGS):
        h.insert(0, NavigableString("\n␞"))   # marker, replaced with "# "
        h.append(NavigableString("\n"))
    for b in main.find_all(BLOCKS):
        if b.name not in HEADINGS:
            b.insert_before(NavigableString("\n"))
            b.append(NavigableString("\n"))
    raw = main.get_text(" ")
    out, seen = [], set()
    for line in raw.split("\n"):
        line = re.sub(r"\s+", " ", line).strip()
        line = re.sub(r"\s+([,.;:!?])", r"\1", line)
        is_h = line.startswith("␞")
        line = ICONS.sub("", line.lstrip("␞ ").strip())
        if not line:
            continue
        line = ("# " if is_h else "") + line
        # repeated long blocks (mobile/desktop copies of the same text) once only;
        # short lines like "10am - 4pm" legitimately repeat under different headings
        if (out and out[-1] == line) or (len(line) > 60 and line in seen):
            continue
        seen.add(line)
        out.append(line)
    return out


def main_text(html: str, limit: int = 30000) -> str:
    """Full text; if over the limit, cut at the last heading before it and say so."""
    lines = main_lines(html)
    text = "\n".join(lines)
    if len(text) <= limit:
        return text
    kept, size = [], 0
    for ln in lines:
        if size + len(ln) + 1 > limit:
            break
        kept.append(ln)
        size += len(ln) + 1
    # drop a trailing partial section so nothing looks empty or cut off
    for i in range(len(kept) - 1, 0, -1):
        if kept[i].startswith("# "):
            kept = kept[:i]
            break
    return "\n".join(kept) + "\n[Page continues; the rest was left out for length. Do not treat later sections as missing.]"


def sections(lines: list[str]) -> list[tuple[str, list[str]]]:
    """[(heading, [lines under it])] in order. Text before the first heading has heading ''."""
    out: list[tuple[str, list[str]]] = [("", [])]
    for ln in lines:
        if ln.startswith("# "):
            out.append((ln[2:], []))
        else:
            out[-1][1].append(ln)
    return out


def page_facts(html: str, ticket_re: re.Pattern | None = None) -> dict:
    soup, main = _soup_main(html)
    h1s = [h.get_text(" ", strip=True) for h in soup.find_all("h1") if h.get_text(strip=True)]
    lines = main_lines(html)
    text = "\n".join(lines)
    ticket_re = ticket_re or re.compile(r"access\.trlibrary\.com|/tickets\b")
    links = [a["href"] for a in main.find_all("a", href=True)]
    return {
        "lines": lines,
        "sections": sections(lines),
        "text": text,
        "has_times": bool(TIME_RE.search(text)),
        # opening hours specifically (times near "open"/"hours"/a weekday), not e.g. a show time
        "has_open_hours": bool(re.search(r"(open|hours|closed|daily|monday|tuesday|wednesday|thursday|friday|saturday|sunday)"
                                         r"[\s\S]{0,60}?\b\d{1,2}(:\d{2})?\s*(a\.?m\.?|p\.?m\.?)", text, re.I)),
        "has_visit_length": bool(LENGTH_RE.search(text)),
        "has_price": bool(PRICE_RE.search(text)),
        "has_ticket_link": any(ticket_re.search(h) for h in links),
        "h1_count": len(h1s),
    }


# ---------- claim checks ----------

QUOTED = re.compile(r"[\"'“‘]([^\"'”’]{3,80})[\"'”’]")


def _named_section(claim: str, facts: dict):
    """The section a claim names in quotes (e.g. 'Getting Around Town'), if it exists on the page."""
    for name in QUOTED.findall(claim):
        n = name.strip(" #").lower()
        for h, body in facts["sections"]:
            if h and (h.lower() == n or n in h.lower()):
                return h, body
    m = re.search(r"\b(?:under|in|below) (?:the )?([A-Z][\w’']*(?: [A-Za-z][\w’']*){0,5}) (?:heading|section)", claim)
    if m:
        n = m.group(1).lower()
        for h, body in facts["sections"]:
            if h and n in h.lower():
                return h, body
    return None


def _ends_cleanly(s: str) -> bool:
    return bool(TERMINAL.search(s.strip()))


def check_claim(claim: str, facts: dict) -> tuple[bool | None, str]:
    """(True = page confirms it, False = page contradicts it, None = can't check), reason."""
    c = (claim or "").lower()
    if not c:
        return None, ""

    # "empty 'X' heading/section", "heading with no content"
    if re.search(r"\bempty\b|no content (under|below|after)|nothing (under|below)|blank (heading|section)", c):
        sec = _named_section(claim, facts)
        if sec:
            words = sum(len(ln.split()) for ln in sec[1])
            return (False, f"“{sec[0]}” has {words} words under it") if words >= 8 else (True, f"“{sec[0]}” has no text under it")
        empties = [h for h, body in facts["sections"] if h and not body]
        return (True, f"empty heading: “{empties[0]}”") if empties else (None, "")

    # "ends abruptly", "truncated sentence", "cuts off mid-sentence", "unfinished sentence"
    if re.search(r"truncat|cuts? off|cut-off|mid-sentence|unfinished|incomplete sentence|ends abruptly|trailing sentence", c):
        sec = _named_section(claim, facts)
        if sec:
            body = [ln for ln in sec[1] if len(ln) > 20]
            if not body:
                return True, f"“{sec[0]}” has no text under it"
            return (False, f"“{sec[0]}” ends with a complete sentence") if _ends_cleanly(body[-1]) \
                else (True, f"“{sec[0]}” ends without punctuation")
        # a real mid-sentence cut ends on a word; citations end on an ISBN, year or page number
        long_lines = [ln for ln in facts["lines"] if not ln.startswith("# ") and len(ln) > 120 and "ISBN" not in ln]
        cut = [ln for ln in long_lines if not _ends_cleanly(ln) and re.search(r"[a-z,;]\s*$", ln)]
        return (True, f"a paragraph ends without punctuation: “…{cut[0][-60:]}”") if cut \
            else (False, "every paragraph on the page ends with a complete sentence")

    # duplicate / multiple H1
    if re.search(r"(duplicate|multiple|two|second|extra|more than one) h1|h1 (tags|headings) .*(duplicate|twice)", c):
        n = facts["h1_count"]
        return (True, f"page has {n} H1 headings") if n > 1 else (False, f"page has {n} H1 heading")

    # "add a callout box near the top with the hours" is about placement, not absence: leave it alone
    if re.search(r"\b(callout|box|banner|summary|section|faq|block|table|near the top|at the top|above the fold|"
                 r"prominent|scannable|first screen|upfront|up front|higher|move|repeat)\b", c) \
            and not re.search(r"\b(missing|lacks?|lacking|no (mention|hours|price|times)|not (state|list|mention)|leaving (it|them) out|absent)\b", c):
        return None, ""
    missing_words = (r"(add|missing|lacks?|lacking|no |not (state|list|show|include|mention)|without|omits?|include|state|"
                     r"clarify|list|tell|note|mention|establish|surface|put|show)")
    # hours
    if re.search(r"\b(opening|daily|operating)? ?(hours|opening and closing times|closing times)\b", c) and re.search(missing_words, c) \
            and not re.search(r"visit length|3 ?1/2|three and a half|hours? (to|for) (explore|visit)", c):
        has = facts.get("has_open_hours", facts["has_times"])
        return (False, "the page lists opening times") if has else (True, "no opening times found on the page")
    # visit length
    if re.search(r"3 ?1/2|3½|three and a half|visit length|visit duration|how long (to|visitors)|recommended visit|duration", c) and re.search(missing_words, c):
        return (False, "the page already gives the 3½-hour visit length") if facts["has_visit_length"] else (True, "no visit length on the page")
    # prices
    if re.search(r"ticket prices?|admission prices?|\bprices?\b|\bcost\b", c) and re.search(missing_words, c):
        return (False, "the page lists a price") if facts["has_price"] else (True, "no price on the page")
    # ticket / booking link
    if re.search(r"(ticket|booking|buy|purchase|reservation)[\w ]{0,12}(link|button)|link to (buy|book|tickets)", c) and re.search(missing_words, c):
        return (False, "the page already links to tickets") if facts["has_ticket_link"] else (True, "no ticket link on the page")
    return None, ""


def filter_items(items: list, facts: dict, key: str, where: str, dropped: list) -> list:
    """Keep items whose claim isn't contradicted by the page; record the rest in dropped."""
    kept = []
    for it in items or []:
        text = it.get(key, "") if isinstance(it, dict) else str(it)
        if isinstance(it, dict):
            text = " ".join(str(it.get(k, "")) for k in (key, "why", "note") if it.get(k))
        ok, why = check_claim(text, facts)
        if ok is False:
            dropped.append({"where": where, "claim": (it.get(key) if isinstance(it, dict) else it), "reason": why})
            continue
        if ok and isinstance(it, dict):
            it["confirmed"] = why
        kept.append(it)
    return kept


def check_tips(t: dict, facts: dict) -> dict:
    """Drop page-tip items the live page contradicts. Adds t['dropped_claims']."""
    dropped: list = []
    for field in ("content_additions", "ai_readiness", "technical", "needs_verification"):
        if t.get(field):
            t[field] = filter_items(t[field], facts, "suggestion", field, dropped)
    ok, why = check_claim(t.get("summary") or "", facts)
    if ok is False:
        dropped.append({"where": "summary", "claim": t.get("summary"), "reason": why})
        t["summary_note"] = f"The summary's claim isn't borne out by the live page ({why})."
    t["dropped_claims"] = dropped
    return t


def check_task_result(res: dict, facts: dict) -> dict:
    """Fix task statuses the page contradicts and drop a contradicted 'biggest fix'."""
    dropped: list = []
    tasks = res.get("tasks") or {}
    # (hours aren't auto-corrected here: a page can list restaurant or event times
    #  and still not give the Library's opening hours)
    present = {"visit_length": facts["has_visit_length"],
               "price": facts["has_price"], "buy": facts["has_ticket_link"]}
    for tid, has in present.items():
        t = tasks.get(tid)
        if t and t.get("status") == "missing" and has:
            dropped.append({"where": f"task {tid}", "claim": f"{tid} missing", "reason": "found on the page"})
            t["status"], t["note"] = "buried", ((t.get("note") or "") + " [auto-check: found on the page]").strip()
    fix = res.get("biggest_fix")
    ok, why = check_claim(fix or "", facts)
    if ok is False:
        dropped.append({"where": "biggest fix", "claim": fix, "reason": why})
        res["biggest_fix"] = None
    res["dropped_claims"] = dropped
    return res
