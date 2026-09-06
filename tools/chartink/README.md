# Chartink daily collector and breadth brief

Downloads the 34 table CSVs from the operator's two public Chartink
dashboards every weekday, computes a facts sheet from them, and has a
scheduled Claude session write a full market breadth brief. No browser, no
login.

## What you open

Bookmark this. It is the front door:

    data/chartink/analysis/index.html

It links to two folders, each with an index of every date and a `latest.html`:

| Folder | What it is |
|---|---|
| `analysis/briefs/` | The full nightly brief. Regime, indices, sectors, screeners, flow, threshold scan, confluence, 30 action points, 3 theses. 2,000 to 3,500 words. |
| `analysis/digest/` | The computed digest with percentiles, headed by the brief's top actions and flag. |

## The 34 files

Every weekday the collector writes the same 34 CSVs a manual download of
both dashboards produces, under the same names:

    data/chartink/csv/<trade date>/<Chartink tile name>.csv

For example `data/chartink/csv/2026-09-04/Minervini Screener.csv`. The
header follows Chartink's export: `Date`, then `Symbol` or `Sector`, then the
tile's columns. Dates are ISO so they sort.

Row counts match or exceed the manual download. The dashboard export pages
screener lists at 100 rows; the collector asks for up to 1,000 and gets
whatever the server has. Minervini returned 222 names on 2026-09-04 where the
export gave 100.

The two dashboards also carry 32 chart tiles with no CSV button. The
collector pulls those too, into the history layer below, because they carry
the same breadth series with 375 days of history.

## The chain

`run_daily.bat`, run by Windows Task Scheduler at 21:00 on weekdays:

| Step | Script | Writes |
|---|---|---|
| 1 | `fetch_chartink.py` | `csv/<date>/` the 34 files, plus the per-tile history under `data/chartink/<dashboard>/` |
| 2 | `consolidate.py` | `analysis/*.csv` a few wide history files |
| 3 | `digest.py` | `analysis/digest/<date>.md` percentiles and movers |
| 4 | `facts.py` | `analysis/facts/<date>.md` the sheet the brief is written from |
| 5 | `render_html.py` | the browser pages |

Then the scheduled Claude task `chartink-market-read` at 21:30 on weekdays:

| Step | Reads | Writes |
|---|---|---|
| 6 | `BREADTH_BRIEF_FRAMEWORK.md`, `facts/latest.md`, prior brief | `analysis/briefs/<date>.md` and `<date>-appendix.md` |
| 7 | the brief | the digest's market-read section |
| 8 | | re-renders the browser pages |

Then `push_data.bat`, run by Windows Task Scheduler at 22:15 on weekdays:

| Step | Does |
|---|---|
| 9 | `git add data/chartink`, one data-only commit named `chartink data: <trade date>`, push to `main`. Rebases and retries once if the remote moved. Nothing else is ever staged. |

## The claude.ai project

The brainstorming happens in a claude.ai project whose knowledge is synced
from this repo on GitHub. Add from GitHub, and select:

- `data/chartink/analysis/briefs/` (the briefs and their appendices)
- `data/chartink/analysis/market_breadth_recent.csv` (last 90 trade dates)

Do not add `data/chartink/csv/`. The raw files are in the repo for on-demand
fetching, not for standing knowledge; one day's shareholding lists alone are
thousands of rows.

Paste `PROJECT_INSTRUCTIONS.md` into the project's instructions. Keep the repo
copy and the project copy in sync by hand.

## The facts sheet

`facts.py` reads the 34 files and writes one dense markdown sheet of
numbers: every regime metric with 1-day, 5-day and 20-day change and a
percentile against its own 375-day history; the index and sector tables;
each screener's size, sector mix, cap mix and leading names; the return
leaders by horizon and which names persist; the four shareholding lists with
the zero-prior caveat applied; and a confluence table of names that appear on
three or more screens, with their flow flags.

It is arithmetic. It ranks, counts and intersects. It draws no conclusion.
The brief writer reads this sheet, not the 34 raw files, so every number in
the brief traces to one place.

Three guards keep it honest. A metric with fewer than 20 readings shows
`n=<count>` instead of a percentile. A Chartink division-by-zero sentinel
(about 1.7e308) is discarded as NOT FOUND. Grouped tiles that carry several
dates per symbol are deduplicated to the latest date before counting.

## The brief

`BREADTH_BRIEF_FRAMEWORK.md` is the specification. The nightly task follows it
section by section. In short: a TOP 3 ACTIONS box, a TOP FLAG box, data
freshness, regime with a label, what changed since the prior brief, indices,
sectors, screeners, flow, a fixed 13-condition threshold scan, confluence
names, 15 investor points and 15 trader points each carrying a number and a
condition, three theses with base case, positioning, invalidation and risk of
ruin, and a meta-observation.

Tags in the text, coloured by the renderer: `[BULL]` `[BEAR]` `[FLAG]`
`[ACTION]` `[WATCH]` `[HIT]` `[OK]` `[NEW]` `[STALE]`.

The brief describes conditions and names what a setup favours or penalises at
sector and screen level. It gives no buy, sell, hold, target or stop
instruction on any named stock. Naming a stock from a screener or the
confluence table reports the data.

The task prompt is at `~/.claude/scheduled-tasks/chartink-market-read/SKILL.md`.
Edit the framework, not the prompt, to change what the brief contains.

## How the download works

A Chartink dashboard page embeds every tile definition in its HTML: the tile
name, its scan query, and its history size. The page POSTs each query to
`/widget/process` and renders the JSON. The collector does the same two steps
with `requests`, adding `limit=1000` so grouped lists return in full. Both
dashboards are public.

The config is read from the live page on every run. Add, remove or edit a
tile on chartink.com and the next run picks it up. `dashboards.txt` lists the
dashboards, one per line.

## Scheduling

    powershell -ExecutionPolicy Bypass -File tools\chartink\schedule_task.ps1 -Time 21:00
    powershell -ExecutionPolicy Bypass -File tools\chartink\schedule_task.ps1 -Remove
    Start-ScheduledTask -TaskName 'Chartink Daily Collector'

The Windows task runs whether or not the Claude app is open, and catches up
on next boot if the machine was off. The Claude task runs only while the app
is open; if it is shut at 21:22, the brief is written on next launch. Manage
it under Scheduled in the sidebar.

## Usage by hand

    python tools/chartink/fetch_chartink.py            # download
    python tools/chartink/fetch_chartink.py --dry-run  # list tiles
    python tools/chartink/consolidate.py
    python tools/chartink/digest.py
    python tools/chartink/facts.py [YYYY-MM-DD]
    python tools/chartink/render_html.py

Log: `data/chartink/_collector.log`.

## Load and etiquette

66 tiles is 66 POSTs per run, once a day after close, with a 2-second sleep
plus jitter, three retries with backoff, and a 20-second back-off on HTTP 429.
Do not loop it intraday.

## When it breaks

Two download failures are loud and mean Chartink changed its page:
`csrf-token not found` and `widget definitions not found`. Fix the regex in
`load_dashboard()`. A dashboard made private fails the same way; there is no
login path by design.
