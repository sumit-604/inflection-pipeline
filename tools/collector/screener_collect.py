"""
screener_collect.py
Usage: py screener_collect.py https://www.screener.in/company/IVALUE/

Folder structure created automatically (main company mode):
    stock analysis-_output [Company Name]/
        SCREENING FOLDER/      <- Excel + Annual Reports
        PEER ANALYSIS/         <- empty, populated by collect_batch.py
        Concall files          <- root level (for deep dive pipeline)
        Investor Presentation  <- root level (for deep dive pipeline)

Peer mode (called by collect_batch.py with --output-dir):
    All files downloaded flat into the provided folder (no subfolders).
    Excel (Financials.xlsx) is downloaded here too.

Google Sheets conversion:
    After every run, any Financials.xlsx found on Google Drive that does not
    yet have a matching Google Sheet is automatically converted and the xlsx
    is deleted.  This conversion requires one-time credentials setup — see
    the SETUP section in convert_sheets.py for instructions.
    If credentials are not configured, the script skips conversion and
    prints a reminder to run convert_sheets.py manually.

Prerequisites (one-time):
    pip install playwright requests python-dotenv
    pip install google-api-python-client google-auth-oauthlib google-auth-httplib2
    playwright install chromium
"""

import os, sys, time, re, argparse, requests
from pathlib import Path
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

GDRIVE_BASE           = r"G:\My Drive\stock analysis"
OUTPUT_FOLDER_PREFIX  = "stock analysis-_output"
SCRIPT_DIR            = Path(__file__).parent

# ---------------------------------------------------------------------------
# credentials
# ---------------------------------------------------------------------------

def load_credentials():
    env_path = SCRIPT_DIR / ".env"
    if not env_path.exists():
        print("\n  .env file not found.")
        sys.exit(1)
    load_dotenv(env_path)
    email    = os.getenv("SCREENER_EMAIL")
    password = os.getenv("SCREENER_PASSWORD")
    if not email or not password:
        print("\n  SCREENER_EMAIL or SCREENER_PASSWORD missing in .env")
        sys.exit(1)
    return email, password

# ---------------------------------------------------------------------------
# folder helpers
# ---------------------------------------------------------------------------

def clean_name(name):
    name = re.sub(r'[<>:"/\\|?*\n\r\t]', '', name)
    name = re.sub(r'\s+', ' ', name)
    return name.strip('. ')[:80]

def create_folders(company_name):
    """Create main folder + SCREENING FOLDER + PEER ANALYSIS subfolders."""
    main      = Path(GDRIVE_BASE) / f"{OUTPUT_FOLDER_PREFIX} {clean_name(company_name)}"
    screening = main / "SCREENING FOLDER"
    peer      = main / "PEER ANALYSIS"
    main.mkdir(parents=True, exist_ok=True)
    screening.mkdir(exist_ok=True)
    peer.mkdir(exist_ok=True)
    print(f"\n  Main folder:     {main}")
    print(f"  |- SCREENING FOLDER  (Excel + Annual Reports)")
    print(f"  |- PEER ANALYSIS     (peer files via collect_batch.py)")
    print(f"  `- [root]            (Concalls + Presentation)")
    return main, screening, peer

# ---------------------------------------------------------------------------
# browser / download helpers
# ---------------------------------------------------------------------------

def download_excel_via_browser(email, password, url, dest_folder):
    """Login, go to company page, click Export to Excel, save to dest_folder."""
    print(f"\n  Downloading Excel (Financials.xlsx) -> {dest_folder} ...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        context = browser.new_context(
            accept_downloads=True,
            viewport={"width": 1280, "height": 900}
        )
        page = context.new_page()
        try:
            page.goto("https://www.screener.in/login/",
                      wait_until="domcontentloaded", timeout=60000)
            time.sleep(2)
            page.fill('input[name="username"]', email)
            page.fill('input[name="password"]', password)
            page.click('button[type="submit"]')
            time.sleep(4)

            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            time.sleep(3)

            excel_btn = page.locator(
                'a:has-text("Export to Excel"), '
                'button:has-text("Export to Excel"), '
                'a:has-text("EXPORT TO EXCEL")'
            )
            if excel_btn.count() > 0:
                with page.expect_download(timeout=30000) as dl_info:
                    excel_btn.first.click()
                dl   = dl_info.value
                dest = dest_folder / "Financials.xlsx"
                dl.save_as(str(dest))
                size_kb = dest.stat().st_size // 1024
                print(f"  OK  Financials.xlsx  ({size_kb} KB)  -> {dest}")
            else:
                print("  WARNING: Export to Excel button not found — download manually")

            html    = page.content()
            cookies = context.cookies()
            browser.close()
            return html, cookies

        except Exception as e:
            print(f"  WARNING: Excel download error: {str(e)[:80]}")
            try:
                html    = page.content()
                cookies = context.cookies()
                browser.close()
                return html, cookies
            except Exception:
                browser.close()
                return "", []

def get_session(cookies):
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer":    "https://www.screener.in/",
    })
    for cookie in cookies:
        session.cookies.set(cookie["name"], cookie["value"],
                            domain=cookie.get("domain", "screener.in"))
    return session

def get_company_name_from_html(html):
    for pattern in [r'<h1[^>]*>\s*([^<\n]{5,80})', r'<title>\s*([^|<\n]{5,80})']:
        m = re.search(pattern, html, re.IGNORECASE)
        if m:
            return clean_name(m.group(1).strip())
    return "Company"

def download_file(session, href, dest_path, label):
    if not href:
        return False
    if not href.startswith("http"):
        href = "https://www.screener.in" + href
    try:
        resp = session.get(href, timeout=60, stream=True, allow_redirects=True)
        if resp.status_code != 200:
            return False
        if "text/html" in resp.headers.get("content-type", ""):
            return False
        total = 0
        with open(dest_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
                total += len(chunk)
        size_kb = total // 1024
        if size_kb < 5:
            dest_path.unlink(missing_ok=True)
            return False
        print(f"  OK  {label}  ({size_kb} KB)")
        return True
    except Exception as e:
        print(f"  WARNING  {label}: {str(e)[:60]}")
        return False

# ---------------------------------------------------------------------------
# extraction helpers
# ---------------------------------------------------------------------------

def extract_concalls_with_dates(html):
    results = []
    all_links   = list(re.finditer(
        r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>\s*(?:Transcript|transcript)\s*</a>',
        html, re.IGNORECASE
    ))
    date_pattern = re.compile(
        r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{4})\b'
    )
    for i, m in enumerate(all_links):
        href           = m.group(1)
        preceding_html = html[:m.start()]
        dates          = list(date_pattern.finditer(preceding_html))
        if dates:
            last_date = dates[-1]
            filename  = f"Concall_{last_date.group(1)}_{last_date.group(2)}_Transcript"
        else:
            filename  = f"Concall_{i+1}_Transcript"
        results.append((href, filename))
    return results

def extract_annual_reports(html):
    results      = []
    year_pattern = re.compile(r'(20\d\d)')
    for pattern in [
        # anchor whose visible text says "Annual Report", allowing nested tags
        # (screener wraps the source as e.g. "Annual Report 2026 <span>from bse</span>")
        # and any host in the href (BSE-hosted AnnPdfOpen/AttachHis links etc.)
        r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(?:(?!</a>).)*?annual\s*report(?:(?!</a>).)*?</a>',
        # fallback: the href itself mentions an annual report
        r'<a[^>]+href=["\']([^"\']+annual[^"\']*)["\']',
    ]:
        for m in re.finditer(pattern, html, re.IGNORECASE | re.DOTALL):
            href = m.group(1)
            if not href.startswith("#"):
                # take the year from the matched anchor itself (not a ±100 window,
                # which can bleed into an adjacent year's link)
                years  = year_pattern.findall(m.group(0))
                year   = years[-1] if years else ""
                fname  = f"Annual_Report_{year}" if year else "Annual_Report"
                results.append((href, fname))
    return results

def extract_presentations(html):
    results = []
    for m in re.finditer(
        r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>[^<]*(?:[Pp]resentation|PPT)[^<]*</a>',
        html, re.IGNORECASE
    ):
        href = m.group(1)
        if not href.startswith("#"):
            results.append((href, "Investor_Presentation"))
    return results

# ---------------------------------------------------------------------------
# download functions
# ---------------------------------------------------------------------------

def download_annual_reports(session, html, dest_folder, max_count=2):
    print(f"\n  Downloading Annual Reports -> {dest_folder.name} (up to {max_count}) ...")
    links  = extract_annual_reports(html)
    seen   = set()
    unique = [(h, n) for h, n in links if h not in seen and not seen.add(h)]
    if not unique:
        print("  WARNING: No annual reports found on screener.in for this company.")
        return
    downloaded = 0
    used_names = set()
    for href, name in unique[:max_count]:
        final_name = name
        counter    = 2
        while final_name in used_names:
            final_name = f"{name}_{counter}"
            counter   += 1
        used_names.add(final_name)
        dest = dest_folder / f"{final_name}.pdf"
        if download_file(session, href, dest, f"Annual Report {final_name}"):
            downloaded += 1
    if downloaded == 0:
        print("  WARNING: Could not download annual reports.")

def download_concalls(session, html, dest_folder, max_count=4):
    print(f"\n  Downloading Concall Transcripts -> {dest_folder.name} (up to {max_count}) ...")
    links  = extract_concalls_with_dates(html)
    seen   = set()
    unique = [(h, n) for h, n in links if h not in seen and not seen.add(h)]
    if not unique:
        print("  WARNING: No concall transcripts found.")
        return
    used_names = set()
    for href, name in unique[:max_count]:
        final_name = name
        counter    = 2
        while final_name in used_names:
            final_name = f"{name}_{counter}"
            counter   += 1
        used_names.add(final_name)
        dest = dest_folder / f"{final_name}.pdf"
        download_file(session, href, dest, final_name)

def download_presentations(session, html, dest_folder, max_count=1):
    print(f"\n  Downloading Investor Presentation -> {dest_folder.name} ...")
    links  = extract_presentations(html)
    seen   = set()
    unique = [(h, n) for h, n in links if h not in seen and not seen.add(h)]
    if not unique:
        print("  WARNING: No investor presentations found.")
        return
    for i, (href, name) in enumerate(unique[:max_count]):
        dest = dest_folder / f"{name}_{i+1}.pdf"
        if download_file(session, href, dest, f"Presentation {i+1}"):
            return

# ---------------------------------------------------------------------------
# Google Sheets conversion
# ---------------------------------------------------------------------------

def get_drive_service():
    """
    Build and return an authenticated Google Drive API service object.
    Returns None if credentials are not configured (conversion will be skipped).

    One-time setup:
        1. Go to console.cloud.google.com
        2. Select your GCP project (the same one used for Apps Script)
        3. APIs & Services -> Enable APIs -> enable "Google Drive API"
        4. APIs & Services -> Credentials -> Create Credentials -> OAuth client ID
           Application type: Desktop app   Name: screener-collector (or anything)
        5. Download the JSON file and save it as  credentials.json
           in the same folder as this script.
        6. Run the script once — a browser window will open asking you to
           authorise. After authorising, token.json is created automatically.
           All future runs are silent (no browser needed).
    """
    try:
        from googleapiclient.discovery import build
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
    except ImportError:
        return None

    SCOPES     = ["https://www.googleapis.com/auth/drive"]
    token_path = SCRIPT_DIR / "token.json"
    creds_path = SCRIPT_DIR / "credentials.json"
    creds      = None

    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        elif creds_path.exists():
            flow  = InstalledAppFlow.from_client_secrets_file(str(creds_path), SCOPES)
            creds = flow.run_local_server(port=0)
            token_path.write_text(creds.to_json(), encoding="utf-8")
        else:
            return None   # credentials.json not set up yet

    return build("drive", "v3", credentials=creds)


def convert_all_financials_to_gsheet(service):
    """
    Find every Financials.xlsx on Google Drive that does not yet have a
    matching Financials Google Sheet in the same folder.
    Convert each one and delete the xlsx.

    This function is idempotent — safe to run multiple times.
    Files that are already converted (GSheet exists, xlsx gone) are ignored.

    Drive sync delay: files saved via Google Drive File Stream can take
    10-30 seconds to appear in the Drive API.  We wait 15 seconds here.
    If a file is still not found, it will be converted on the next run
    (or by running convert_sheets.py manually).
    """
    if service is None:
        print(
            "\n  Google Sheets conversion: credentials not configured."
            "\n  To enable automatic conversion, follow the setup instructions"
            "\n  in convert_sheets.py, then re-run."
            "\n  OR: run  py convert_sheets.py  manually after Drive sync completes."
        )
        return

    print("\n  Waiting 15 seconds for Google Drive to sync before converting...")
    time.sleep(15)

    print("  Searching Drive for Financials.xlsx files to convert...")

    try:
        results = service.files().list(
            q="name='Financials.xlsx' and trashed=false",
            fields="files(id, name, parents)",
            pageSize=50
        ).execute()

        xlsx_files = results.get("files", [])

        if not xlsx_files:
            print("  No Financials.xlsx files found on Drive.")
            return

        print(f"  Found {len(xlsx_files)} Financials.xlsx file(s).")
        converted = 0
        skipped   = 0

        for f in xlsx_files:
            file_id   = f["id"]
            parent_id = f["parents"][0] if f.get("parents") else None

            # Check if a Google Sheet named 'Financials' already exists here
            if parent_id:
                existing = service.files().list(
                    q=(
                        f"name='Financials' and "
                        f"'{parent_id}' in parents and "
                        f"mimeType='application/vnd.google-apps.spreadsheet' and "
                        f"trashed=false"
                    ),
                    fields="files(id)"
                ).execute().get("files", [])

                if existing:
                    skipped += 1
                    continue   # already converted, skip

            # Convert: copy as Google Sheets, then delete xlsx
            service.files().copy(
                fileId=file_id,
                body={
                    "name":     "Financials",
                    "mimeType": "application/vnd.google-apps.spreadsheet"
                }
            ).execute()
            service.files().delete(fileId=file_id).execute()
            print(f"  OK  Converted Financials.xlsx -> Google Sheet  (id {file_id})")
            converted += 1

        print(f"  Conversion complete: {converted} converted, {skipped} already done.")

    except Exception as e:
        print(f"  WARNING: Conversion error: {str(e)[:120]}")
        print("  Run  py convert_sheets.py  manually to retry.")


# ---------------------------------------------------------------------------
# peer analysis self-copy
# ---------------------------------------------------------------------------

def is_concall_file(name):
    n = name.lower()
    return any(w in n for w in ["concall", "transcript", "con_call", "earning", "conference"])

def is_presentation_file(name):
    n = name.lower()
    return any(w in n for w in ["investor", "presentation", "pres_", "ppt"])

def copy_main_company_to_peer_folder(main_folder, company_name):
    """
    Copy all concall transcripts and investor presentations from main_folder
    into PEER ANALYSIS/[company_name]/ so the peer pipeline can compare
    the main company against its peers.
    Runs every time — always overwrites with the latest files.
    """
    import shutil
    peer_self_folder = main_folder / "PEER ANALYSIS" / company_name
    peer_self_folder.mkdir(parents=True, exist_ok=True)

    print(f"\n  Copying main company files -> PEER ANALYSIS/{company_name}/ ...")

    files_to_copy = [
        f for f in main_folder.iterdir()
        if f.is_file() and (is_concall_file(f.name) or is_presentation_file(f.name))
    ]

    if not files_to_copy:
        print(f"  WARNING: No concalls or presentations in main folder to copy.")
        return

    copied = 0
    for src in files_to_copy:
        dest = peer_self_folder / src.name
        shutil.copy2(src, dest)
        print(f"    Copied: {src.name}")
        copied += 1

    print(f"  {copied} file(s) copied into PEER ANALYSIS/{company_name}/")


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Download company documents from screener.in"
    )
    parser.add_argument(
        "url",
        help="screener.in company URL e.g. https://www.screener.in/company/IVALUE/"
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help=(
            "Override output folder. Used by collect_batch.py for peer companies — "
            "routes files into the parent company's PEER ANALYSIS subfolder instead "
            "of creating a new top-level folder."
        )
    )
    parser.add_argument(
        "--no-drive", action="store_true",
        help="Skip all Google Drive access (the G: existence check and the "
             "xlsx->Google Sheet conversion). collect_to_repo.py passes this.")
    args = parser.parse_args()

    url       = args.url.rstrip("/") + "/"
    peer_mode = args.output_dir is not None

    if "screener.in/company/" not in url:
        print("  URL must be a screener.in company page.")
        sys.exit(1)

    if not args.no_drive and not Path(GDRIVE_BASE).exists():
        print(f"  Google Drive path not found: {GDRIVE_BASE}")
        sys.exit(1)

    email, password = load_credentials()

    print(f"\n{'='*60}")
    if peer_mode:
        print(f"  SCREENER.IN COLLECTOR  (peer mode)")
    else:
        print(f"  SCREENER.IN COLLECTOR")
    print(f"{'='*60}")
    print(f"  {url}")

    # ------------------------------------------------------------------
    # Step 1: Excel download via browser + capture HTML + cookies
    #
    # Main mode:  Excel -> temp folder, moved to SCREENING FOLDER after
    #             create_folders() tells us the real folder name.
    # Peer mode:  Excel -> directly into args.output_dir (the peer subfolder).
    #             No move needed.
    # ------------------------------------------------------------------
    if peer_mode:
        excel_dest = Path(args.output_dir)
        excel_dest.mkdir(parents=True, exist_ok=True)
    else:
        excel_dest = Path(GDRIVE_BASE) / "temp_screening"
        excel_dest.mkdir(parents=True, exist_ok=True)

    html, cookies = download_excel_via_browser(email, password, url, excel_dest)

    # ------------------------------------------------------------------
    # Step 2: Company name from HTML
    # ------------------------------------------------------------------
    company_name = get_company_name_from_html(html) if html else "Company"
    print(f"\n  Company: {company_name}")

    # ------------------------------------------------------------------
    # Step 3: Set up folder routing
    # ------------------------------------------------------------------
    if peer_mode:
        # Flat layout — everything goes into the provided peer subfolder.
        # Excel is already there (saved in Step 1).
        main_folder      = Path(args.output_dir)
        screening_folder = main_folder   # annual reports alongside everything else
        print(f"  Peer output folder: {main_folder}")

    else:
        # Create proper folder hierarchy.
        main_folder, screening_folder, _ = create_folders(company_name)

        # Move Excel from temp location to SCREENING FOLDER.
        temp_excel = excel_dest / "Financials.xlsx"
        if temp_excel.exists():
            temp_excel.replace(screening_folder / "Financials.xlsx")
            try:
                excel_dest.rmdir()   # clean up if empty
            except Exception:
                pass

        # Write folder path so collect_batch.py can map label -> folder.
        last_folder_file = SCRIPT_DIR / "_last_folder.txt"
        try:
            last_folder_file.write_text(str(main_folder), encoding="utf-8")
        except Exception:
            pass

    # ------------------------------------------------------------------
    # Step 4: PDF downloads via requests session
    # ------------------------------------------------------------------
    if cookies:
        session = get_session(cookies)
        download_annual_reports(session, html, screening_folder, max_count=2)
        download_concalls(session, html, main_folder, max_count=4)
        download_presentations(session, html, main_folder, max_count=1)

    # ------------------------------------------------------------------
    # Step 5: Summary
    # ------------------------------------------------------------------
    print(f"\n{'='*60}")
    print(f"  DOWNLOAD COMPLETE")

    if peer_mode:
        all_files = [f for f in main_folder.iterdir() if f.is_file()]
        print(f"\n  {main_folder.name}/  ({len(all_files)} files)")
        for f in sorted(all_files):
            print(f"    {f.name}  ({f.stat().st_size // 1024} KB)")
    else:
        print(f"\n  {main_folder.name}/")
        s_files = list(screening_folder.iterdir())
        print(f"  |- SCREENING FOLDER/  ({len(s_files)} files)")
        for f in sorted(s_files):
            print(f"  |    {f.name}  ({f.stat().st_size // 1024} KB)")
        print(f"  |- PEER ANALYSIS/  (populate with collect_batch.py PEER: lines)")
        r_files = [f for f in main_folder.iterdir() if f.is_file()]
        print(f"  `- [root]  ({len(r_files)} files)")
        for f in sorted(r_files):
            print(f"       {f.name}  ({f.stat().st_size // 1024} KB)")

    print(f"{'='*60}")

    # ------------------------------------------------------------------
    # Step 6: Copy main company concalls + presentations into
    #         PEER ANALYSIS/[company_name]/  (main mode only)
    # ------------------------------------------------------------------
    if not peer_mode:
        copy_main_company_to_peer_folder(main_folder, company_name)

    # ------------------------------------------------------------------
    # Step 7: Convert Financials.xlsx -> Google Sheet on Drive
    # ------------------------------------------------------------------
    if not args.no_drive:
        print(f"\n  Converting Excel files to Google Sheets...")
        drive_service = get_drive_service()
        convert_all_financials_to_gsheet(drive_service)

    print(f"\n  All done.\n")


if __name__ == "__main__":
    main()
