"""
collect_batch.py
----------------
Downloads documents for multiple companies in one go.

Usage:
    py collect_batch.py

Reads companies.txt from the same folder as this script.

companies.txt format
---------------------

# Lines starting with # are comments. Blank lines are ignored.

# MAIN COMPANY (creates its own top-level folder as normal):
WELLSPUN:https://www.screener.in/company/WELLSPUNCORP/

# Or without a label (ticker is extracted from the URL automatically):
https://www.screener.in/company/VENUSPIPES/

# PEER COMPANY (files go into the parent company's PEER ANALYSIS subfolder):
# Format:  PEER:[PARENT_LABEL]:[URL]
# PARENT_LABEL must exactly match the label on the main company line above.
PEER:WELLSPUN:https://www.screener.in/company/VENUSPIPES/
PEER:WELLSPUN:https://www.screener.in/company/AEROFLEX/
PEER:WELLSPUN:https://www.screener.in/company/KRNETWORK/

NOTES
------
- Main companies are always processed BEFORE peer companies, regardless of
  the order they appear in companies.txt.
- After downloading each main company, screener_collect.py writes the created
  folder path to _last_folder.txt. This script reads that file to map the
  label to the real folder on Google Drive.
- Peer files land in:
      [Parent Folder]/PEER ANALYSIS/[PEER_TICKER]/
  where PEER_TICKER is extracted from the peer's screener.in URL.
"""

import sys
import re
import time
import subprocess
from pathlib import Path


SCRIPT_DIR       = Path(__file__).parent
COLLECT_SCRIPT   = SCRIPT_DIR / "screener_collect.py"
LAST_FOLDER_FILE = SCRIPT_DIR / "_last_folder.txt"
COMPANIES_FILE   = SCRIPT_DIR / "companies.txt"


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def ticker_from_url(url):
    """Extract ticker from a screener.in URL.
    e.g. https://www.screener.in/company/VENUSPIPES/ -> VENUSPIPES
    """
    m = re.search(r"/company/([^/]+)/?", url)
    return m.group(1).upper() if m else "UNKNOWN"


def parse_companies_file(filepath):
    """
    Returns:
        main_entries  -- list of (label, url)
        peer_entries  -- list of (parent_label, peer_ticker, url)
    """
    main_entries = []
    peer_entries = []

    with open(filepath, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue

            upper = line.upper()

            if upper.startswith("PEER:"):
                # Format: PEER:PARENT_LABEL:https://...
                # URL itself contains ":" so split into max 3 parts.
                parts = line.split(":", 2)
                if len(parts) < 3:
                    print(f"  WARNING: Skipping malformed PEER line: {line}")
                    continue
                parent_label = parts[1].strip().upper()
                url = parts[2].strip()
                if not url.startswith("http"):
                    print(f"  WARNING: PEER line has no valid URL: {line}")
                    continue
                peer_ticker = ticker_from_url(url)
                peer_entries.append((parent_label, peer_ticker, url))

            elif line.startswith("http"):
                # Plain URL — derive label from URL
                label = ticker_from_url(line)
                main_entries.append((label, line))

            elif ":" in line:
                # LABEL:https://...
                colon_pos = line.index(":")
                label = line[:colon_pos].strip().upper()
                url   = line[colon_pos + 1:].strip()
                if not url.startswith("http"):
                    print(f"  WARNING: Skipping unrecognised line: {line}")
                    continue
                main_entries.append((label, url))

            else:
                print(f"  WARNING: Skipping unrecognised line: {line}")

    return main_entries, peer_entries


def read_last_folder():
    """Read folder path written by screener_collect.py. Returns string or None."""
    try:
        if LAST_FOLDER_FILE.exists():
            return LAST_FOLDER_FILE.read_text(encoding="utf-8").strip()
    except Exception:
        pass
    return None


def clear_last_folder():
    """Remove _last_folder.txt so a stale value is never used."""
    try:
        if LAST_FOLDER_FILE.exists():
            LAST_FOLDER_FILE.unlink()
    except Exception:
        pass


def run_main_company(url):
    """Call screener_collect.py for a main company. Returns True on success."""
    clear_last_folder()
    result = subprocess.run(
        [sys.executable, str(COLLECT_SCRIPT), url],
        check=False
    )
    return result.returncode == 0


def run_peer_company(url, output_dir):
    """Call screener_collect.py in peer mode with --output-dir. Returns True on success."""
    output_dir.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [sys.executable, str(COLLECT_SCRIPT), url, "--output-dir", str(output_dir)],
        check=False
    )
    return result.returncode == 0


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    if not COMPANIES_FILE.exists():
        print(f"\n  companies.txt not found in {SCRIPT_DIR}")
        print(f"\n  Create companies.txt with entries like:")
        print(f"  WELLSPUN:https://www.screener.in/company/WELLSPUNCORP/")
        print(f"  PEER:WELLSPUN:https://www.screener.in/company/VENUSPIPES/")
        sys.exit(1)

    main_entries, peer_entries = parse_companies_file(COMPANIES_FILE)

    if not main_entries and not peer_entries:
        print("\n  No valid entries found in companies.txt")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"  BATCH DOWNLOAD")
    print(f"  {len(main_entries)} main  |  {len(peer_entries)} peer")
    print(f"{'='*60}")

    # label -> Path of created folder (populated as main companies finish)
    label_to_folder = {}

    # ------------------------------------------------------------------
    # Step 1: Main companies
    # ------------------------------------------------------------------
    if main_entries:
        print(f"\n-- MAIN COMPANIES --")

    main_success = 0
    main_failed  = []

    for i, (label, url) in enumerate(main_entries, 1):
        print(f"\n[{i}/{len(main_entries)}]  {label}")
        print(f"  {url}")
        print("-" * 60)

        ok = run_main_company(url)

        if ok:
            main_success += 1
            folder_path = read_last_folder()
            if folder_path:
                label_to_folder[label] = Path(folder_path)
                print(f"  Mapped  {label}  ->  {folder_path}")
            else:
                print(f"  WARNING: _last_folder.txt not found after {label}.")
                print(f"           Peer downloads for {label} will be skipped.")
        else:
            main_failed.append((label, url))

        if i < len(main_entries):
            print(f"\n  Waiting 5 seconds...")
            time.sleep(5)

    # ------------------------------------------------------------------
    # Step 2: Peer companies
    # ------------------------------------------------------------------
    peer_success = 0
    peer_failed  = []
    peer_skipped = []

    if peer_entries:
        print(f"\n-- PEER COMPANIES --")

    for i, (parent_label, peer_ticker, url) in enumerate(peer_entries, 1):
        print(f"\n[{i}/{len(peer_entries)}]  {peer_ticker}  (peer of {parent_label})")
        print(f"  {url}")

        parent_folder = label_to_folder.get(parent_label)

        if not parent_folder:
            print(f"  WARNING: Parent folder for '{parent_label}' not found.")
            print(f"    Either '{parent_label}' is not in this batch's main entries,")
            print(f"    or the main company download failed.")
            print(f"    Fix: make sure '{parent_label}:https://...' is in companies.txt")
            print(f"    as a main entry, then re-run.")
            peer_skipped.append((parent_label, peer_ticker, url))
            continue

        # Files go into: [Parent Folder]/PEER ANALYSIS/[PEER_TICKER]/
        peer_dest = parent_folder / "PEER ANALYSIS" / peer_ticker
        print(f"  Destination: {peer_dest}")

        ok = run_peer_company(url, peer_dest)
        if ok:
            peer_success += 1
        else:
            peer_failed.append((parent_label, peer_ticker, url))

        if i < len(peer_entries):
            print(f"\n  Waiting 5 seconds...")
            time.sleep(5)

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print(f"\n{'='*60}")
    print(f"  BATCH COMPLETE")
    print(f"  Main :  {main_success}/{len(main_entries)} OK", end="")
    if main_failed:
        print(f"   |  {len(main_failed)} FAILED")
        for label, url in main_failed:
            print(f"     FAILED  {label}  {url}")
    else:
        print("   |  all OK")

    if peer_entries:
        issues = len(peer_failed) + len(peer_skipped)
        print(f"  Peers:  {peer_success}/{len(peer_entries)} OK", end="")
        if issues:
            print(f"   |  {issues} issues")
            for pl, pt, u in peer_failed:
                print(f"     FAILED   {pt} (peer of {pl})  {u}")
            for pl, pt, u in peer_skipped:
                print(f"     SKIPPED  {pt} (peer of {pl})  parent folder not found")
        else:
            print("   |  all OK")

    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
