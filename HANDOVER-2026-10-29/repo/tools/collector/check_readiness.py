"""
check_readiness.py
------------------
Checks that a company's Google Drive folder has all required documents
before you start the Gemini pipeline.

Usage:
    py check_readiness.py

It reads companies.txt to find the main company label, then searches
Google Drive for the matching folder and runs all checks.

You can also pass a company name directly:
    py check_readiness.py "PNGS Gargi"

Run this BEFORE starting the Gemini pipeline to avoid wasting tokens.
"""

import sys
import re
import os
from pathlib import Path
from dotenv import load_dotenv

SCRIPT_DIR   = Path(__file__).parent
GDRIVE_BASE  = r"G:\My Drive\stock analysis"
OUTPUT_PREFIX = "stock analysis-_output"

# ── File type detection ───────────────────────────────────────────────────────

def is_annual_report(name):
    n = name.lower()
    return ("annual" in n or "ar_" in n or "annual_report" in n)

def is_latest_annual_report(name):
    """Annual report AND contains FY25 or FY26 year marker."""
    if not is_annual_report(name):
        return False
    n = name.lower()
    return any(y in n for y in ["2025", "2026", "fy25", "fy26", "_25", "_26", "25.", "26."])

def is_concall(name):
    n = name.lower()
    return any(w in n for w in ["concall", "transcript", "con_call", "earning", "conference"])

def is_presentation(name):
    n = name.lower()
    return any(w in n for w in ["investor", "presentation", "pres_", "ppt", "investor_pres"])

def is_google_sheet(path):
    """A Google Sheet shows up as a folder-less file with no extension, or
    we detect it by checking if a .xlsx sibling does NOT exist."""
    return path.suffix == "" and "financials" in path.name.lower()

def is_xlsx(name):
    return name.lower().endswith(".xlsx")

def get_files(folder):
    """Return list of file Paths directly in a folder (non-recursive)."""
    if not folder.exists():
        return []
    return [f for f in folder.iterdir() if f.is_file()]

def get_subfolders(folder):
    """Return list of subfolder Paths directly inside folder."""
    if not folder.exists():
        return []
    return [f for f in folder.iterdir() if f.is_dir()]

# ── Checklist helpers ─────────────────────────────────────────────────────────

PASS = "  OK  "
FAIL = " FAIL "
WARN = " WARN "

class Report:
    def __init__(self, company_name):
        self.company_name = company_name
        self.lines = []
        self.failures = 0
        self.warnings = 0

    def ok(self, msg):
        self.lines.append(f"  [  OK  ]  {msg}")

    def fail(self, msg):
        self.lines.append(f"  [ FAIL ]  {msg}")
        self.failures += 1

    def warn(self, msg):
        self.lines.append(f"  [ WARN ]  {msg}")
        self.warnings += 1

    def section(self, title):
        self.lines.append("")
        self.lines.append(f"  {'─'*56}")
        self.lines.append(f"  {title}")
        self.lines.append(f"  {'─'*56}")

    def print(self):
        width = 62
        print(f"\n{'='*width}")
        print(f"  PIPELINE READINESS CHECK")
        print(f"  Company: {self.company_name}")
        print(f"{'='*width}")
        for line in self.lines:
            print(line)
        print(f"\n{'='*width}")
        if self.failures == 0 and self.warnings == 0:
            print(f"  RESULT:  READY TO RUN  -  all checks passed")
        elif self.failures == 0:
            print(f"  RESULT:  READY (with {self.warnings} warning(s))")
            print(f"  Warnings are advisory — pipeline can still run.")
        else:
            print(f"  RESULT:  NOT READY  -  {self.failures} item(s) missing")
            print(f"  Fix the FAIL items above before starting the pipeline.")
        print(f"{'='*width}\n")

# ── Individual section checks ─────────────────────────────────────────────────

def check_screening_folder(r, screening_folder):
    r.section("SCREENING FOLDER")

    files = get_files(screening_folder)
    names = [f.name for f in files]

    if not screening_folder.exists():
        r.fail("SCREENING FOLDER does not exist")
        return

    # Financials Google Sheet
    has_gsheet  = any(is_google_sheet(f) for f in files)
    has_xlsx    = any(is_xlsx(f.name) for f in files)

    if has_gsheet:
        r.ok("Financials — Google Sheet present")
    elif has_xlsx:
        r.fail("Financials.xlsx found but NOT converted to Google Sheet — run: py convert_sheets.py")
    else:
        r.fail("Financials — no Google Sheet and no xlsx found")

    # Latest Annual Report
    latest_ars = [f for f in files if is_latest_annual_report(f.name)]
    any_ars    = [f for f in files if is_annual_report(f.name)]

    if latest_ars:
        r.ok(f"Latest Annual Report (FY25/FY26) found: {latest_ars[0].name}")
    elif any_ars:
        r.warn(f"Annual Report found but may not be latest (no FY25/FY26 marker): {any_ars[0].name}")
    else:
        r.fail("No Annual Report found in SCREENING FOLDER")


def check_main_folder(r, main_folder):
    r.section("MAIN FOLDER  (deep-dive documents)")

    files = get_files(main_folder)

    # Latest Annual Report
    latest_ars = [f for f in files if is_latest_annual_report(f.name)]
    any_ars    = [f for f in files if is_annual_report(f.name)]

    if latest_ars:
        r.ok(f"Latest Annual Report (FY25/FY26) found: {latest_ars[0].name}")
    elif any_ars:
        r.warn(f"Annual Report found but may not be latest (no FY25/FY26 marker): {any_ars[0].name}")
    else:
        r.fail("No Annual Report found in main folder")

    # Concall transcripts
    concalls = [f for f in files if is_concall(f.name)]
    if len(concalls) == 0:
        r.fail("No concall transcripts found (need min 1, ideally 4)")
    elif len(concalls) < 4:
        r.warn(f"Only {len(concalls)} concall transcript(s) found (ideally 4) — pipeline can run")
    else:
        r.ok(f"Concall transcripts: {len(concalls)} found (good)")

    # Investor Presentations
    pres = [f for f in files if is_presentation(f.name)]
    if len(pres) == 0:
        r.fail("No Investor Presentation found (need min 1)")
    elif len(pres) < 4:
        r.warn(f"Only {len(pres)} Investor Presentation(s) found (ideally up to 4) — pipeline can run")
    else:
        r.ok(f"Investor Presentations: {len(pres)} found (good)")

    # No xlsx remaining
    xlsx_files = [f for f in files if is_xlsx(f.name)]
    if xlsx_files:
        r.fail(f"Unconverted .xlsx file(s) still present: {[f.name for f in xlsx_files]} — run: py convert_sheets.py")
    else:
        r.ok("No .xlsx files remaining in main folder")


def check_peer_main_company_folder(r, peer_analysis_folder, company_name):
    r.section(f"PEER ANALYSIS / {company_name}  (main company copy)")

    company_peer_folder = peer_analysis_folder / company_name

    if not company_peer_folder.exists():
        r.fail(f"Folder '{company_name}' missing inside PEER ANALYSIS — run screener_collect.py again to auto-create it")
        return

    files = get_files(company_peer_folder)

    # Concalls
    concalls = [f for f in files if is_concall(f.name)]
    if len(concalls) == 0:
        r.fail("No concall transcripts copied into main company peer folder (need min 1)")
    elif len(concalls) < 4:
        r.warn(f"Only {len(concalls)} concall transcript(s) in main company peer folder (ideally 4)")
    else:
        r.ok(f"Concall transcripts: {len(concalls)} found")

    # Investor Presentations
    pres = [f for f in files if is_presentation(f.name)]
    if len(pres) == 0:
        r.fail("No Investor Presentation copied into main company peer folder (need min 1)")
    elif len(pres) < 4:
        r.warn(f"Only {len(pres)} Investor Presentation(s) in main company peer folder (ideally up to 4)")
    else:
        r.ok(f"Investor Presentations: {len(pres)} found")


def check_peer_subfolders(r, peer_analysis_folder, company_name):
    r.section("PEER ANALYSIS / [EACH PEER COMPANY]")

    subfolders = get_subfolders(peer_analysis_folder)

    # Filter out the main company folder — that is checked separately above
    peer_folders = [f for f in subfolders if f.name.upper() != company_name.upper()]

    if not peer_folders:
        r.warn("No peer company subfolders found inside PEER ANALYSIS")
        r.warn("Download peers using collect_batch.py with PEER: lines in companies.txt")
        return

    for peer_folder in sorted(peer_folders):
        files = get_files(peer_folder)
        peer_name = peer_folder.name

        # Financials Google Sheet
        has_gsheet = any(is_google_sheet(f) for f in files)
        has_xlsx   = any(is_xlsx(f.name) for f in files)

        if has_gsheet:
            r.ok(f"{peer_name}: Financials Google Sheet present")
        elif has_xlsx:
            r.fail(f"{peer_name}: Financials.xlsx not converted — run: py convert_sheets.py")
        else:
            r.fail(f"{peer_name}: No Financials (no Google Sheet, no xlsx)")

        # Concalls
        concalls = [f for f in files if is_concall(f.name)]
        if len(concalls) == 0:
            r.fail(f"{peer_name}: No concall transcripts (need min 1)")
        elif len(concalls) < 4:
            r.warn(f"{peer_name}: Only {len(concalls)} concall transcript(s) (ideally 4)")
        else:
            r.ok(f"{peer_name}: Concall transcripts — {len(concalls)} found")

        # Investor Presentations
        pres = [f for f in files if is_presentation(f.name)]
        if len(pres) == 0:
            r.fail(f"{peer_name}: No Investor Presentation (need min 1)")
        elif len(pres) < 4:
            r.warn(f"{peer_name}: Only {len(pres)} Investor Presentation(s) (ideally up to 4)")
        else:
            r.ok(f"{peer_name}: Investor Presentations — {len(pres)} found")

        # No xlsx remaining
        xlsx_files = [f for f in files if is_xlsx(f.name)]
        if xlsx_files:
            r.fail(f"{peer_name}: Unconverted .xlsx still present — run: py convert_sheets.py")


def check_no_xlsx_anywhere(r, main_folder):
    """Walk the entire company folder tree and flag any remaining xlsx."""
    r.section("GLOBAL CHECK  (no .xlsx files anywhere)")

    found_xlsx = []
    for root, dirs, files in os.walk(main_folder):
        for fname in files:
            if is_xlsx(fname):
                rel = Path(root).relative_to(main_folder)
                found_xlsx.append(str(rel / fname))

    if found_xlsx:
        r.fail(f"{len(found_xlsx)} unconverted .xlsx file(s) found — run: py convert_sheets.py")
        for f in found_xlsx:
            r.fail(f"  -> {f}")
    else:
        r.ok("No .xlsx files remaining anywhere in the folder tree")


# ── Folder finder ─────────────────────────────────────────────────────────────

def find_company_folder(search_name):
    """
    Find the company's output folder on Google Drive.
    Searches for 'stock analysis-_output' folders whose name contains
    the search_name (case-insensitive).
    """
    root = Path(GDRIVE_BASE)
    if not root.exists():
        print(f"\n  ERROR: Google Drive path not found: {GDRIVE_BASE}")
        sys.exit(1)

    search_lower = search_name.lower().replace(" ", "")
    matches = []

    for folder in root.iterdir():
        if folder.is_dir() and OUTPUT_PREFIX in folder.name:
            folder_key = folder.name.lower().replace(" ", "")
            if search_lower in folder_key:
                matches.append(folder)

    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        print(f"\n  Multiple folders matched '{search_name}':")
        for i, m in enumerate(matches):
            print(f"    {i+1}. {m.name}")
        print(f"\n  Please be more specific. Example:")
        print(f"    py check_readiness.py \"PNGS Gargi Fashion\"")
        sys.exit(1)
    else:
        return None


def get_company_name_from_folder(folder_path):
    """Extract company name from folder name like 'stock analysis-_output PNGS Gargi'"""
    name = folder_path.name.replace(OUTPUT_PREFIX, "").strip()
    return name


# ── companies.txt reader ──────────────────────────────────────────────────────

def get_main_company_from_companies_txt():
    """
    Read companies.txt and return the label of the first non-PEER entry.
    Used as default when no company name is passed on command line.
    """
    txt_path = SCRIPT_DIR / "companies.txt"
    if not txt_path.exists():
        return None

    with open(txt_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.upper().startswith("PEER:"):
                continue
            # First main entry
            if line.startswith("http"):
                # Plain URL — extract ticker
                m = re.search(r"/company/([^/]+)/?", line)
                return m.group(1) if m else None
            elif ":" in line:
                return line.split(":", 1)[0].strip()
    return None


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    load_dotenv(SCRIPT_DIR / ".env")

    # Determine which company to check
    if len(sys.argv) >= 2:
        search_name = " ".join(sys.argv[1:])
    else:
        search_name = get_main_company_from_companies_txt()
        if not search_name:
            print("\n  Usage: py check_readiness.py [company name or ticker]")
            print("  Example: py check_readiness.py PNGSGARGI")
            print("  Or: add a main company line to companies.txt and run without arguments.")
            sys.exit(1)
        print(f"\n  Using company from companies.txt: {search_name}")

    # Find the folder
    print(f"\n  Searching for folder matching: '{search_name}' ...")
    main_folder = find_company_folder(search_name)

    if not main_folder:
        print(f"\n  ERROR: No folder found matching '{search_name}'")
        print(f"  In: {GDRIVE_BASE}")
        print(f"\n  Make sure you have run screener_collect.py for this company first.")
        print(f"  Folder should be named like: stock analysis-_output [Company Name]")
        sys.exit(1)

    company_name = get_company_name_from_folder(main_folder)
    print(f"  Found: {main_folder.name}")

    # Sub-paths
    screening_folder  = main_folder / "SCREENING FOLDER"
    peer_analysis_folder = main_folder / "PEER ANALYSIS"

    # Run all checks
    r = Report(company_name)

    check_screening_folder(r, screening_folder)
    check_main_folder(r, main_folder)
    check_peer_main_company_folder(r, peer_analysis_folder, company_name)
    check_peer_subfolders(r, peer_analysis_folder, company_name)
    check_no_xlsx_anywhere(r, main_folder)

    r.print()


if __name__ == "__main__":
    main()
