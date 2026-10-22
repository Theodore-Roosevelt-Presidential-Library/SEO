"""Ticket checkout completion rates from GA4.

ACME's ticket store (access.trlibrary.com) reports to the same GA4 property as
trlibrary.com. This job measures how many store visitors reach each checkout
step and how many who start checkout finish.

PUBLIC DASHBOARD RULE: only rates are written. No user, order or revenue counts
ever leave this function, and rates based on fewer than `min_users_for_rate`
users are replaced with "low volume".

Needs the repo variable GA4_PROPERTY_ID and the Google sign-in (the same
service account as Search Console, added in GA4 as a Viewer).

Writes checkout/latest.json and checkout/history.json.
"""
from __future__ import annotations


from . import common as C

LABELS = {"store_visit": "Visited the ticket store", "view_item": "Viewed a ticket or date",
          "add_to_cart": "Added tickets to cart", "begin_checkout": "Started checkout",
          "add_payment_info": "Entered payment", "purchase": "Completed purchase"}


def users_by_event(ga, start: str, end: str, store: str, steps: list[str], extra_dim: str | None = None) -> dict:
    dims = ["eventName"] + ([extra_dim] if extra_dim else [])
    rows = ga.report(dims, ["totalUsers"], start, end,
                     dim_filter=C.ga4_and(C.ga4_filter("hostName", store), C.ga4_in("eventName", ["page_view"] + steps)))
    out: dict = {}
    for r in rows:
        key = r.get(extra_dim) if extra_dim else "all"
        ev = "store_visit" if r["eventName"] == "page_view" else r["eventName"]
        out.setdefault(key, {})[ev] = int(r.get("totalUsers") or 0)
    return out


def rates(counts: dict, steps: list[str], min_users: int) -> dict:
    """Turn private counts into public rates. Counts are never returned."""
    base = counts.get("store_visit", 0)

    def rate(n, d):
        if not d or d < min_users:
            return "low volume" if d else None
        return round(min(n, d) / d, 3)
    seq = ["store_visit"] + steps
    seen = [s for s in seq if counts.get(s)]
    out = {
        "tracked_steps": [s for s in steps if counts.get(s)],
        "missing_steps": [s for s in steps if not counts.get(s)],
        "of_store_visitors": {s: rate(counts.get(s, 0), base) for s in steps if counts.get(s)},
        "step_to_step": {},
        "checkout_completion": rate(counts.get("purchase", 0), counts.get("begin_checkout", 0))
        if counts.get("begin_checkout") else None,
        "store_conversion": rate(counts.get("purchase", 0), base) if counts.get("purchase") else None,
    }
    for a, b in zip(seen, seen[1:]):
        out["step_to_step"][f"{a}->{b}"] = rate(counts.get(b, 0), counts.get(a, 0))
    return out


def run() -> None:
    cfg = C.config().get("checkout", {})
    if not C.env("GA4_PROPERTY_ID"):
        C.set_status("checkout", "skipped", "Add the repo variable GA4_PROPERTY_ID (and give the service account Viewer access in GA4) to measure ticket checkout completion.")
        return
    try:
        ga = C.GA4.from_env()
        if not ga:
            C.set_status("checkout", "skipped", "GA4_PROPERTY_ID is set but Google sign-in isn't configured.")
            return
        store, steps, mn = cfg.get("store_host", "access.trlibrary.com"), cfg.get("steps", []), cfg.get("min_users_for_rate", 30)

        cur = users_by_event(ga, "28daysAgo", "yesterday", store, steps).get("all", {})
        prev = users_by_event(ga, "56daysAgo", "29daysAgo", store, steps).get("all", {})
        by_dev = users_by_event(ga, "28daysAgo", "yesterday", store, steps, "deviceCategory")

        # website ticket page -> store hand-off (approximate: needs cross-domain linking in GA4 to be exact)
        site_rows = ga.report(["hostName"], ["totalUsers"], "28daysAgo", "yesterday",
                              dim_filter=C.ga4_and(C.ga4_filter("hostName", cfg.get("site_host", "www.trlibrary.com")),
                                                   C.ga4_filter("pagePath", cfg.get("ticket_page_prefix", "/tickets"), "BEGINS_WITH")))
        ticket_page_users = int(sum(r.get("totalUsers") or 0 for r in site_rows))
        handoff = None
        if ticket_page_users >= mn and cur.get("store_visit"):
            handoff = round(min(cur["store_visit"], ticket_page_users) / ticket_page_users, 3)

        # weekly trend of the headline rate, last 12 weeks
        weekly = users_by_event(ga, "84daysAgo", "yesterday", store, steps, "isoYearIsoWeek")
        trend = []
        for wk in sorted(weekly):
            r = rates(weekly[wk], steps, mn)
            trend.append({"week": wk, "checkout_completion": r["checkout_completion"], "store_conversion": r["store_conversion"]})

        out = {
            "updated": C.now_iso(),
            "store": store,
            "period": "last 28 days",
            "note": "Rates only; counts are never published. Users who triggered each step on the ticket store, from GA4.",
            "labels": LABELS,
            "current": rates(cur, steps, mn),
            "previous": rates(prev, steps, mn),
            "by_device": {d: rates(c, steps, mn) for d, c in by_dev.items()},
            "ticket_page_to_store": handoff,
            "weekly": trend,
        }
        C.write_json("checkout/latest.json", out)
        cc = out["current"]["checkout_completion"]
        C.upsert_history("checkout/history.json", {"date": C.today().isoformat(),
                                                   "checkout_completion": cc,
                                                   "store_conversion": out["current"]["store_conversion"]})
        if not out["current"]["tracked_steps"]:
            C.set_status("checkout", "error", f"No checkout events seen on {store} in GA4. The ACME store may need GA4 ecommerce tracking turned on.")
            return
        miss = out["current"]["missing_steps"]
        C.set_status("checkout", "ok", f"Checkout completion {cc if isinstance(cc, str) else f'{cc:.0%}' if cc is not None else 'n/a'}"
                     + (f"; steps not tracked: {', '.join(miss)}" if miss else ""))
    except Exception as e:  # noqa: BLE001
        C.set_status("checkout", "error", str(e)[:400])
        raise C.JobError(str(e)) from e


if __name__ == "__main__":
    run()
