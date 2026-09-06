#!/usr/bin/env python3
"""Daily Chartink dashboard collector.

Pulls every widget on the configured public Chartink dashboards and merges the
results into one CSV per widget under data/chartink/<dashboard>/.

How it works. A Chartink dashboard page embeds its widget definitions in the
HTML as a :widgets="..." attribute. Each definition carries the widget name,
its scan query, and its history size. The page then POSTs each query to
/widget/process and renders the JSON. This script does the same two steps with
plain HTTP. No login and no browser are needed for public dashboards.

Because the config is read from the live page on every run, editing a dashboard
on chartink.com changes what this script collects. Nothing here to update.

Usage:
    python fetch_chartink.py                 # collect every dashboard
    python fetch_chartink.py --dry-run       # list widgets, fetch nothing
    python fetch_chartink.py --only 133280   # one dashboard
    python fetch_chartink.py --delay 3.0     # slower, politer

Exit code is 0 only when every widget succeeded.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import random
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE = "https://chartink.com"
IST = timezone(timedelta(hours=5, minutes=30))

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_FILE = Path(__file__).resolve().parent / "dashboards.txt"
OUT_ROOT = REPO_ROOT / "data" / "chartink"
LOG_FILE = OUT_ROOT / "_collector.log"

# Chartink is a free service. Keep the load light.
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0 Safari/537.36"
)
DEFAULT_DELAY = 2.0
REQUEST_TIMEOUT = 60
MAX_RETRIES = 3

# Key columns written first in every CSV.
KEY_COLS = ["date", "time", "group"]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def log(msg):
    stamp = datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S")
    line = "[" + stamp + "] " + msg
    print(line, flush=True)
    try:
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with LOG_FILE.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except OSError:
        pass


def slugify(text):
    s = re.sub(r"[^a-zA-Z0-9]+", "-", str(text or "")).strip("-").lower()
    return s or "widget"


# Index universe segment used by Chartink for the indices watchlist.
INDEX_SEGMENT = "{45603}"


def classify(query, grouped=None):
    """Say what one row of this widget's output represents.

    Returned values:
      market    one row per date, whole market
      sector    one row per date and sector
      industry  one row per date and industry
      marketcap one row per date and market cap band
      index     one row per date and index
      stock     one row per date and symbol, an ordinary screener list

    The GROUP BY clause is the first signal, but it is not sufficient: several
    screener tiles carry no GROUP BY and still come back per symbol. So when the
    response is available, its shape decides whether the tile is grouped at all.
    """
    q = query or ""
    m = re.search(r"\bGROUP\s+BY\s+([a-zA-Z_]+)", q, re.I)
    by = m.group(1).lower() if m else None

    if by == "sector":
        return "sector"
    if by == "industry":
        return "industry"
    if by == "marketcapname":
        return "marketcap"

    # Grouped by symbol, or not grouped in the query at all. Trust the response
    # when we have it: a tile that returns groups is per symbol, not market-wide.
    if grouped is None:
        grouped = by == "symbol"
    if not grouped:
        return "market"
    return "index" if INDEX_SEGMENT in q else "stock"


def read_config():
    """Read dashboards.txt. Lines are: <dashboard_id> [name]. # starts a comment."""
    if not CONFIG_FILE.exists():
        log("FATAL config not found: " + str(CONFIG_FILE))
        sys.exit(2)
    out = []
    for raw in CONFIG_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        parts = line.split(None, 1)
        dash_id = parts[0]
        slug = slugify(parts[1]) if len(parts) > 1 else dash_id
        out.append({"id": dash_id, "slug": slug})
    return out


# ---------------------------------------------------------------------------
# Chartink access
# ---------------------------------------------------------------------------

def new_session():
    s = requests.Session()
    s.headers.update({
        "User-Agent": USER_AGENT,
        "Accept-Language": "en-GB,en;q=0.9",
    })
    return s


def load_dashboard(session, dash_id):
    """GET the dashboard page. Return (csrf token, widget list, page title)."""
    url = BASE + "/dashboard/" + str(dash_id)
    resp = session.get(url, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    page = resp.text

    m = re.search(r'name="csrf-token"\s+content="([^"]+)"', page)
    if not m:
        raise RuntimeError("csrf-token not found; page layout changed")
    csrf = m.group(1)

    title_m = re.search(r"<title>(.*?)</title>", page, re.S)
    title = html.unescape(title_m.group(1)).strip() if title_m else str(dash_id)

    wm = re.search(r':widgets="(.*?)"\s*\n', page, re.S)
    if not wm:
        raise RuntimeError("widget definitions not found; page layout changed")
    widgets = json.loads(html.unescape(wm.group(1)))

    parsed = []
    for w in widgets:
        jd = w.get("jsondetails") or {}
        groups = jd.get("groups") or {}
        size = groups.get("size") or 1
        try:
            size = int(size)
        except (TypeError, ValueError):
            size = 1
        query = w.get("query")
        if not query:
            log("  SKIP widget " + str(w.get("id")) + ": no query")
            continue
        parsed.append({
            "id": w.get("id"),
            "name": w.get("name") or str(w.get("id")),
            "query": query,
            "size": size,
            "result_type": jd.get("resultType"),
        })
    return csrf, parsed, title


# Grouped queries (one row per symbol, sector, index) page at 75 rows unless
# told otherwise. The dashboard's own CSV export goes to 999. Ask for more than
# any tile currently returns; the server caps at what is available.
GROUP_LIMIT = 1000

# The Chartink export writes the group column under these names.
GROUP_HEADER = {
    "stock": "Symbol",
    "index": "Symbol",
    "sector": "Sector",
    "industry": "Industry",
    "marketcap": "Market cap",
}


def run_widget(session, csrf, dash_id, widget):
    """POST one widget query to /widget/process and return the parsed JSON."""
    body = {"query": widget["query"], "size": str(widget["size"]),
            "limit": str(GROUP_LIMIT)}
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRF-TOKEN": csrf,
        "Referer": BASE + "/dashboard/" + str(dash_id),
        "Origin": BASE,
    }
    last_err = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = session.post(BASE + "/widget/process", data=body,
                             headers=headers, timeout=REQUEST_TIMEOUT)
            if r.status_code == 429:
                wait = 20 * attempt
                log("    rate limited, waiting " + str(wait) + "s")
                time.sleep(wait)
                last_err = "HTTP 429"
                continue
            r.raise_for_status()
            data = r.json()
            if isinstance(data, str):
                data = json.loads(data)
            if isinstance(data, dict) and data.get("error"):
                raise RuntimeError(str(data["error"])[:200])
            return data
        except Exception as exc:
            last_err = str(exc)[:200]
            if attempt < MAX_RETRIES:
                time.sleep(3 * attempt)
    raise RuntimeError(last_err or "unknown error")


# ---------------------------------------------------------------------------
# JSON to rows
# ---------------------------------------------------------------------------

def to_rows(data):
    """Flatten one /widget/process response into (column names, rows).

    The response is column-major. metaData[0].tradeTimes holds the timestamps.
    Each groupData entry holds {name, results: [{alias: [v0, v1, ...]}]}, and
    values line up with tradeTimes by index.
    """
    meta = (data.get("metaData") or [{}])[0]
    trade_times = meta.get("tradeTimes") or []
    aliases = list(meta.get("columnAliases") or [])
    group_data = data.get("groupData") or []

    grouped = not (len(group_data) == 1
                   and group_data[0].get("name") == "*no-groups*")

    rows = []
    seen_cols = []

    for gd in group_data:
        gname = gd.get("name") or ""
        if gname == "*no-groups*":
            gname = ""
        series = {}
        for result in gd.get("results") or []:
            if isinstance(result, dict):
                for alias, values in result.items():
                    series[alias] = values if isinstance(values, list) else [values]

        for alias in series:
            if alias not in seen_cols:
                seen_cols.append(alias)

        n = max([len(v) for v in series.values()] or [0])
        for i in range(n):
            if i >= len(trade_times):
                continue
            dt = datetime.fromtimestamp(trade_times[i] / 1000, tz=IST)
            row = {
                "date": dt.strftime("%Y-%m-%d"),
                "time": dt.strftime("%H:%M"),
                "group": gname,
            }
            for alias, values in series.items():
                val = values[i] if i < len(values) else None
                row[alias] = "" if val is None else val
            rows.append(row)

    ordered = [a for a in aliases if a in seen_cols]
    for c in seen_cols:
        if c not in ordered:
            ordered.append(c)

    cols = ["date", "time"] + (["group"] if grouped else []) + ordered
    if not grouped:
        for r in rows:
            r.pop("group", None)
    return cols, rows


# ---------------------------------------------------------------------------
# CSV merge
# ---------------------------------------------------------------------------

def export_name(name):
    """The filename Chartink's own CSV export uses for a tile.

    Chartink keeps the tile name and swaps characters Windows forbids for an
    underscore, so 'Market Breadth: Number above 500' becomes
    'Market Breadth_ Number above 500'. Match that exactly, so files here line
    up with anything downloaded by hand.
    """
    return re.sub(r'[\\/:*?"<>|]', "_", str(name or "").strip()) + ".csv"


def write_export(out_root, widget, kind, cols, rows):
    """Write the dated, Chartink-named CSV for one table tile.

    One folder per trade date, holding the same 34 files a manual download of
    both dashboards produces, under the same names. Header style follows the
    export too: 'Date', then the group column, then each label capitalised.
    Dates stay ISO so they sort and parse without a lookup table.
    """
    if not rows:
        return None
    trade_date = max(r["date"] for r in rows)
    folder = out_root / "csv" / trade_date
    folder.mkdir(parents=True, exist_ok=True)

    metric_cols = [c for c in cols if c not in KEY_COLS]
    header = ["Date"]
    if "group" in cols:
        header.append(GROUP_HEADER.get(kind, "Symbol"))
    header += [c[:1].upper() + c[1:] for c in metric_cols]

    path = folder / export_name(widget["name"])
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        # Newest first, as the export does; grouped tiles keep server order.
        ordered = sorted(rows, key=lambda r: (r["date"], r["time"]), reverse=True) \
            if "group" not in cols else rows
        for r in ordered:
            line = [r["date"] + (" " + r["time"] if r["time"] != "00:00" else "")]
            if "group" in cols:
                line.append(r.get("group", ""))
            line += [r.get(c, "") for c in metric_cols]
            w.writerow(line)
    return path


def row_key(row):
    return (row.get("date", ""), row.get("time", ""), row.get("group", ""))


def merge_csv(path, cols, rows):
    """Merge rows into path, keyed on (date, time, group).

    Returns (added, updated). Existing history is never dropped, so a run that
    returns a short window still leaves older rows in place.
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    existing = {}
    old_cols = []
    if path.exists():
        with path.open("r", encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh)
            old_cols = list(reader.fieldnames or [])
            for r in reader:
                existing[row_key(r)] = dict(r)

    all_cols = [c for c in KEY_COLS if c in cols or c in old_cols]
    for c in old_cols + cols:
        if c not in all_cols:
            all_cols.append(c)

    added = 0
    updated = 0
    for r in rows:
        # Rows read back from CSV are strings. Normalise the fresh rows the same
        # way so the changed count reports real changes, not float-vs-string.
        r = {c: ("" if v is None else str(v)) for c, v in r.items()}
        k = row_key(r)
        if k in existing:
            before = dict(existing[k])
            merged = dict(existing[k])
            for c, v in r.items():
                merged[c] = v
            existing[k] = merged
            if merged != before:
                updated += 1
        else:
            existing[k] = r
            added += 1

    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=all_cols, extrasaction="ignore")
        writer.writeheader()
        for _, row in sorted(existing.items(), key=lambda kv: kv[0]):
            writer.writerow({c: row.get(c, "") for c in all_cols})

    return added, updated


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def collect(dash, delay, dry_run):
    """Collect one dashboard. Returns (ok count, fail count)."""
    session = new_session()
    log("dashboard " + dash["id"] + " (" + dash["slug"] + "): loading")
    try:
        csrf, widgets, title = load_dashboard(session, dash["id"])
    except Exception as exc:
        log("  FAIL dashboard " + dash["id"] + ": " + str(exc)[:200])
        return 0, 1

    log("  title: " + title)
    log("  " + str(len(widgets)) + " widgets")

    out_dir = OUT_ROOT / dash["slug"]
    ok = 0
    fail = 0
    manifest = []
    tables_written = []

    for idx, w in enumerate(widgets, 1):
        label = "[" + str(idx) + "/" + str(len(widgets)) + "] " + w["name"]
        if dry_run:
            log("  " + label + " (size=" + str(w["size"])
                + ", type=" + str(w["result_type"])
                + ", rows=" + classify(w["query"]) + "?)")
            ok += 1
            continue
        try:
            data = run_widget(session, csrf, dash["id"], w)
            cols, rows = to_rows(data)
            kind = classify(w["query"], grouped="group" in cols)
            if not rows:
                log("  " + label + ": no rows returned, nothing written")
                fail += 1
            else:
                fname = slugify(w["name"]) + "-" + str(w["id"]) + ".csv"
                added, updated = merge_csv(out_dir / fname, cols, rows)
                note = ""
                if w["result_type"] == "table":
                    exp = write_export(OUT_ROOT, w, kind, cols, rows)
                    if exp:
                        note = " | csv/" + exp.parent.name + "/" + exp.name
                        tables_written.append(exp)
                log("  " + label + ": " + str(len(rows)) + " rows -> " + fname
                    + " (+" + str(added) + " new, ~" + str(updated) + " changed)"
                    + note)
                manifest.append({
                    "dashboard": dash["slug"],
                    "dashboard_id": dash["id"],
                    "widget_id": w["id"],
                    "name": w["name"],
                    "file": dash["slug"] + "/" + fname,
                    "kind": kind,
                    "result_type": w["result_type"],
                    "columns": [c for c in cols if c not in KEY_COLS],
                })
                ok += 1
        except Exception as exc:
            log("  FAIL " + label + ": " + str(exc)[:200])
            fail += 1
        time.sleep(delay + random.uniform(0, 0.5))

    write_manifest(dash["slug"], manifest)
    if tables_written:
        log("  " + str(len(tables_written)) + " table CSVs written to "
            + str(tables_written[0].parent))
    return ok, fail


def write_manifest(dash_slug, entries):
    """Record what each CSV holds, so consolidate.py can group them correctly."""
    if not entries:
        return
    path = OUT_ROOT / "_manifest.json"
    data = {}
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            data = {}
    data[dash_slug] = entries
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(
        description="Collect Chartink dashboard data into CSVs.")
    ap.add_argument("--only", help="collect just this dashboard id")
    ap.add_argument("--delay", type=float, default=DEFAULT_DELAY,
                    help="seconds between widget requests (default 2.0)")
    ap.add_argument("--dry-run", action="store_true",
                    help="list widgets without fetching data")
    args = ap.parse_args()

    dashboards = read_config()
    if args.only:
        dashboards = [d for d in dashboards if d["id"] == args.only]
        if not dashboards:
            log("FATAL dashboard " + args.only + " not in " + CONFIG_FILE.name)
            return 2

    log("=" * 62)
    log("chartink collector starting (" + str(len(dashboards)) + " dashboard(s))")

    total_ok = 0
    total_fail = 0
    for d in dashboards:
        ok, fail = collect(d, args.delay, args.dry_run)
        total_ok += ok
        total_fail += fail

    log("done: " + str(total_ok) + " ok, " + str(total_fail) + " failed")
    return 0 if total_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
