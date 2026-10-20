"""Run one or more jobs, keep going if one fails, exit non-zero at the end.

  python -m seo.run daily
  python -m seo.run weekly
  python -m seo.run audit tips      # any job names
"""
from __future__ import annotations

import sys
import traceback

from . import ai_visibility, audit, common as C, digest, gsc, opportunities, ranks, tips

JOBS = {
    "gsc": gsc.run,
    "audit": audit.run,
    "ranks": ranks.run,
    "ai_visibility": ai_visibility.run,
    "opportunities": opportunities.run,
    "tips": tips.run,
    "digest": digest.run,
}
PLANS = {
    "daily": ["gsc", "opportunities", "digest"],
    "weekly": ["gsc", "audit", "ranks", "ai_visibility", "opportunities", "tips", "digest"],
}


def main(argv: list[str]) -> int:
    names: list[str] = []
    for a in argv or ["daily"]:
        names += PLANS.get(a, [a])
    failed = []
    for n in names:
        if n not in JOBS:
            C.log(f"Unknown job: {n}")
            failed.append(n)
            continue
        try:
            JOBS[n]()
        except C.JobError:
            failed.append(n)
        except Exception as e:  # noqa: BLE001
            traceback.print_exc()
            C.set_status(n, "error", str(e)[:400])
            failed.append(n)
    C.write_json("meta.json", {"updated": C.now_iso(), "last_run": names, "failed": failed})
    if failed:
        C.log(f"Failed: {', '.join(failed)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
