"""
daily_pack.py — gather one day of watchlist feed PDFs into a single folder.

download_feed.py writes every 4 hours into
    results_downloads_feed/<YYYY-MM-DD>/<HHMM>/*.pdf
This script copies one "day" of those slot folders into
    daily_pack/<YYYY-MM-DD>/
and writes INDEX.md there with the file count and the file list.

A "day" runs from 05:30 on that date to 05:30 the next morning, so the
overnight slots (00:55, 04:55) land in the pack you read at 05:30.

Files are COPIED, not moved: the 4-hourly Claude task still reads the
slot folders.

Usage:
    python daily_pack.py                 # yesterday (for the 05:15 run)
    python daily_pack.py --date 2026-10-01
"""

from datetime import date, datetime, timedelta
import argparse
import os
import shutil
import sys

CUTOFF = "0530"

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
FEED_ROOT = os.path.join(PROJECT_ROOT, "results_downloads_feed")
PACK_ROOT = os.path.join(PROJECT_ROOT, "daily_pack")


def slot_dirs(day: date):
    """(label, path) for every slot folder in the window, oldest first."""
    nxt = day + timedelta(days=1)
    picks = []
    for d, keep in ((day, lambda s: s >= CUTOFF), (nxt, lambda s: s < CUTOFF)):
        day_dir = os.path.join(FEED_ROOT, d.isoformat())
        if not os.path.isdir(day_dir):
            continue
        for slot in sorted(os.listdir(day_dir)):
            path = os.path.join(day_dir, slot)
            if os.path.isdir(path) and keep(slot):
                picks.append((f"{d.isoformat()} {slot[:2]}:{slot[2:]}", path))
    return picks


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="YYYY-MM-DD (default: yesterday)")
    args = parser.parse_args()
    day = (date.fromisoformat(args.date) if args.date
           else date.today() - timedelta(days=1))

    out_dir = os.path.join(PACK_ROOT, day.isoformat())
    os.makedirs(out_dir, exist_ok=True)

    per_slot = []
    files = []
    for label, path in slot_dirs(day):
        names = sorted(n for n in os.listdir(path)
                       if os.path.isfile(os.path.join(path, n)))
        per_slot.append((label, len(names)))
        for n in names:
            shutil.copy2(os.path.join(path, n), os.path.join(out_dir, n))
            files.append((n, label))

    pdfs = sum(1 for n, _ in files if n.lower().endswith(".pdf"))
    others = len(files) - pdfs
    nxt = day + timedelta(days=1)

    lines = [
        f"# Watchlist feed pack: {day.isoformat()}",
        "",
        f"Window: {day.isoformat()} 05:30 to {nxt.isoformat()} 05:30",
        f"Built: {datetime.now().isoformat(timespec='seconds')}",
        "",
        f"**Files: {len(files)}** (PDF {pdfs}, other {others})",
        "",
        "## By download slot",
        "",
        "| Slot | Files |",
        "|---|---|",
    ]
    lines += [f"| {label} | {n} |" for label, n in per_slot] or ["| none | 0 |"]
    lines += ["", "## Files", ""]
    lines += [f"- {n}  ({label})" for n, label in sorted(files)] or ["- none"]

    with open(os.path.join(out_dir, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"PACK: day={day.isoformat()} files={len(files)} "
          f"pdf={pdfs} other={others} slots={len(per_slot)} -> {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
