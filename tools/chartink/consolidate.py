#!/usr/bin/env python3
"""Fold the per-tile Chartink CSVs into a few analysis files.

The collector writes one CSV per dashboard tile, which is faithful but awkward
to read. This script merges them by what a row actually represents:

    market_breadth_daily.csv   one row per date, every market-wide metric
    sector_daily.csv           one row per date and sector
    industry_daily.csv         one row per date and industry
    marketcap_daily.csv        one row per date and market cap band
    indices_daily.csv          one row per date and index
    screeners/<name>.csv       the per-stock screener lists, left alone

Column names are prefixed with a short tile name, because tiles reuse labels
like '%' and 'High'. Two dashboards measuring the same thing therefore stay in
separate columns and can be compared rather than silently overwriting.

Run it after fetch_chartink.py:

    python tools/chartink/consolidate.py
"""

from __future__ import annotations

import csv
import json
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = REPO_ROOT / "data" / "chartink"
MANIFEST = DATA_ROOT / "_manifest.json"
OUT_DIR = DATA_ROOT / "analysis"

# Which manifest kind lands in which consolidated file.
TARGETS = {
    "market": ("market_breadth_daily.csv", None),
    "sector": ("sector_daily.csv", "sector"),
    "industry": ("industry_daily.csv", "industry"),
    "marketcap": ("marketcap_daily.csv", "marketcap"),
    "index": ("indices_daily.csv", "index"),
}

# Tile names are long. Shorten them for use as a column prefix.
DROP_WORDS = {
    "the", "of", "in", "a", "an", "and", "vs", "by", "at", "to", "with",
    "stocks", "stock", "count", "number", "indicates", "terms", "where",
    "is", "are", "every", "wise", "level", "market",
}


def short_name(name, words_kept=4):
    words = re.split(r"[^a-zA-Z0-9]+", str(name or "").lower())
    keep = [w for w in words if w and w not in DROP_WORDS]
    if not keep:
        keep = [w for w in words if w]
    return "_".join(keep[:words_kept]) or "tile"


def build_prefixes(tiles):
    """One unique column prefix per tile.

    Two tiles can shorten to the same prefix ('MBM 2.0 (velocity) - basic' and
    '... - advanced' both give mbm_2_0_velocity). Widen the name until the
    clash is gone, then fall back to the widget id so a prefix is never shared.
    """
    prefixes = {}
    for width in (4, 6, 9):
        prefixes = {}
        counts = {}
        for t in tiles:
            p = short_name(t["name"], width)
            counts[p] = counts.get(p, 0) + 1
            prefixes[t["widget_id"]] = p
        if all(v == 1 for v in counts.values()):
            return prefixes
    # Still clashing: disambiguate with the widget id.
    seen = {}
    for t in tiles:
        p = prefixes[t["widget_id"]]
        seen[p] = seen.get(p, 0) + 1
    for t in tiles:
        p = prefixes[t["widget_id"]]
        if seen[p] > 1:
            prefixes[t["widget_id"]] = p + "_" + str(t["widget_id"])
    return prefixes


def col_name(prefix, col):
    """Prefixed, file-safe column name. '%' slugifies to nothing, so name it."""
    suffix = re.sub(r"[^a-zA-Z0-9]+", "_", col).strip("_").lower()
    if not suffix:
        suffix = "pct" if "%" in col else "value"
    return prefix + "__" + suffix


def read_csv(path):
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        return list(reader.fieldnames or []), [dict(r) for r in reader]


def load_manifest():
    if not MANIFEST.exists():
        print("No _manifest.json. Run fetch_chartink.py first.", file=sys.stderr)
        sys.exit(2)
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    entries = []
    for dash_entries in data.values():
        entries.extend(dash_entries)
    return entries


def build(entries, kind, out_name, group_label):
    """Merge every CSV of one kind into a single wide file."""
    rows = {}          # key -> merged row
    columns = []       # output column order after the keys
    used = 0

    tiles = sorted((e for e in entries if e["kind"] == kind),
                   key=lambda x: (x["dashboard"], x["name"]))
    prefixes = build_prefixes(tiles)

    for e in tiles:
        path = DATA_ROOT / e["file"]
        if not path.exists():
            continue
        _, file_rows = read_csv(path)
        if not file_rows:
            continue
        used += 1
        prefix = prefixes[e["widget_id"]]

        for r in file_rows:
            date = r.get("date", "")
            group = r.get("group", "")
            key = (date, group)
            if key not in rows:
                base = {"date": date}
                if group_label:
                    base[group_label] = group
                rows[key] = base
            for col, val in r.items():
                if col in ("date", "time", "group"):
                    continue
                out_col = col_name(prefix, col)
                if out_col not in columns:
                    columns.append(out_col)
                rows[key][out_col] = val

    if not rows:
        return None, 0, 0

    header = ["date"] + ([group_label] if group_label else []) + columns
    out_path = OUT_DIR / out_name
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=header, extrasaction="ignore")
        writer.writeheader()
        for key in sorted(rows):
            writer.writerow({c: rows[key].get(c, "") for c in header})

    return out_path, len(rows), used


RECENT_ROWS = 90


def write_recent():
    """A small tail of the master history for the web project's knowledge.

    The full market_breadth_daily.csv is too large to sit in a claude.ai
    project. The last 90 dated rows are enough for a brainstorm and small
    enough to sync every night.
    """
    src = OUT_DIR / "market_breadth_daily.csv"
    if not src.exists():
        return 0
    cols, rows = read_csv(src)
    tail = rows[-RECENT_ROWS:]
    with (OUT_DIR / "market_breadth_recent.csv").open("w", encoding="utf-8",
                                                        newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(tail)
    return len(tail)


def copy_screeners(entries):
    """Copy the per-stock screener lists across unchanged."""
    dest = OUT_DIR / "screeners"
    dest.mkdir(parents=True, exist_ok=True)
    n = 0
    for e in entries:
        if e["kind"] != "stock":
            continue
        src = DATA_ROOT / e["file"]
        if not src.exists():
            continue
        shutil.copyfile(src, dest / (short_name(e["name"]) + ".csv"))
        n += 1
    return n


def main():
    entries = load_manifest()
    print("manifest: " + str(len(entries)) + " tiles")

    made = []
    for kind, (out_name, group_label) in TARGETS.items():
        path, n_rows, n_files = build(entries, kind, out_name, group_label)
        if path:
            made.append((out_name, n_rows, n_files))
            print("  " + out_name + ": " + str(n_rows) + " rows from "
                  + str(n_files) + " tiles")

    n_screeners = copy_screeners(entries)
    print("  screeners/: " + str(n_screeners) + " stock lists copied")

    n_recent = write_recent()
    print("  market_breadth_recent.csv: last " + str(n_recent) + " dated rows")

    print("\nWrote to " + str(OUT_DIR))
    return 0


if __name__ == "__main__":
    sys.exit(main())
