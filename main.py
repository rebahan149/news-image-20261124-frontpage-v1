# Entrypoint for the news-image-20261124 entry (v1 page).
# The judged artifact is entry.png (1024x1024 PNG, <= 1 MiB): one front
# page — masthead "The 24-Hour Planet" — summing up Tuesday
# 24 November 2026 in 35 stories across 6 regions and 17 fields —
# 3 illustrated hero panels, 8 more numbered illustrated panels, a
# UTC timeline, a dotted world map with the drawn stories pinned,
# 24 briefs and a date-check box.
# The page source is index.html; the per-story verification record is
# STORIES.md. This program copies entry.png into $MAKEFUN_OUTPUT_DIR
# (default /output) and prints a one-line dossier describing the page.
# It runs with no network, and two runs write the same bytes: the copy
# is the whole program's output.
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

COMPETITION = "news-image-20261124"
DATE = "2026-11-24"
WEEKDAY = "Tuesday"
TITLE = "The 24-Hour Planet"
STORIES = 35
ILLUSTRATED = 11
REGIONS = 6
FIELDS = 17

HEROES = [
    "Saudi-led coalition says a Riyadh finance-district skyscraper was targeted in a 'terrorist attack'",
    "China investigates Politburo member Chen Jining, the fourth top-leadership probe since 2025",
    "Trump faces backlash after saying he 'convinced' Nvidia to reinstate CEO Jensen Huang; Germany's foreign minister 'shocked'",
]

REGIONS_COUNT = {
    "Europe": 14,
    "Asia-Pacific": 10,
    "North America": 4,
    "Middle East": 3,
    "World & Sport": 3,
    "Latin America": 1,
}

NUMBERS = {
    "venezuela_debt_usd_bn": 237.5,
    "zaporizhzhia_killed": 2,
    "zaporizhzhia_wounded": 22,
    "hanoi_killed": 6,
    "hanoi_injured": 10,
    "sooryavanshi_runs": 204,
    "sooryavanshi_balls": 53,
    "best_buy_comparable_sales_growth_pct": 6.1,
    "politburo_probes_since_2025": 4,
}


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(src, dst)
    dossier = {
        "competition": COMPETITION,
        "date": DATE,
        "weekday": WEEKDAY,
        "title": TITLE,
        "stories": STORIES,
        "illustrated": ILLUSTRATED,
        "regions": REGIONS_COUNT,
        "fields": FIELDS,
        "heroes": HEROES,
        "numbers": NUMBERS,
        "output": dst,
        "bytes": os.path.getsize(dst),
    }
    print(json.dumps(dossier, ensure_ascii=False))


if __name__ == "__main__":
    main()
