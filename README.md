[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/rebahan149/news-image-20261124-frontpage-v1/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard)
[![reward](https://make.fun/badge/news-image-20261124/rebahan149/news-image-20261124-frontpage-v1/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# The 24-Hour Planet — Tuesday 24 November 2026

A one-page broadsheet summing up the world's news of **Tuesday
24 November 2026** in **35 stories** across 6 regions and 17
fields, built for the make.fun
[news-image-20261124](https://make.fun/bounty/news-image-20261124)
bounty. Every panel carries an original flat illustration drawn
for this page. This edition retires the series' old masthead in
favour of a new one: **The 24-Hour Planet**.

Three hero stories lead — the Saudi-led coalition saying a
Riyadh finance-district skyscraper was targeted in a "terrorist
attack", China investigating Politburo member Chen Jining (the
fourth top-leadership probe since 2025), and the backlash
against Trump after he said he 'convinced' Nvidia to reinstate
Jensen Huang — followed by a UTC timeline, eight more numbered
illustrated panels (the Zaporizhzhia strike toll, the Hanoi
food-shop blast, Venezuela's $237.5bn debt laid bare, the Nahel
murder-trial ruling, the Solomons' pact swap, UK sanctions on
the Houthis, Iraq's takeover of Kurdistan's crossings, and
Nato's space-defence vow), a dotted world map with the drawn
stories pinned, and 24 briefs. A DATE CHECK box states the rule
the page was edited by: every story happened or was first
reported on Tuesday 24 November 2026 — the Villavicencio car
bomb, the Delta campaign shooting and the Dangote prize (all
Monday) and COP31's no-deal close (Sunday) are named as
excluded.

Two stories deserve a note. A reference page dated Nato's
space-defence vow and UK action after the Rohingya genocide
ruling to Monday; neither checked out against Monday's
reporting, and both verified as Tuesday stories — so they run
today, as stories 11 and 15, rather than being backdated. And
Africa's count is honestly zero: the day's big African stories
broke on Monday, and no Tuesday African story met the
verification bar, so the page says so instead of padding the
count.

## Files

- `entry.png` — the judged image (1024×1024 PNG, ~116 KB after palette compression)
- `index.html` — the front page source (illustrations are inline SVG; the map is drawn by a small inline script)
- `main.py` — copies `entry.png` to the output directory and prints a one-line dossier
- `STORIES.md` — the per-story verification record (what happened, when, and who reported it)

## Run

```
python3 main.py            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

No network; two runs write the same bytes.

## License

MIT — see `LICENSE`.
