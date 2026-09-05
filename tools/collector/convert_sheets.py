"""
convert_sheets.py
-----------------
Standalone script to convert ALL Financials.xlsx files on Google Drive
to Google Sheets format, then delete the xlsx.

Run this:
  - After a batch download where conversion was skipped (e.g. Drive had not
    synced yet by the time screener_collect.py tried to convert)
  - If you already have many xlsx files from earlier downloads
  - Any time you want to ensure everything is in Google Sheets format

Usage:
    py convert_sheets.py

This script is safe to run multiple times.  Files already converted (Google
Sheet exists, xlsx gone) are silently skipped.

============================================================
ONE-TIME SETUP (do this once, then never again)
============================================================

Step 1 — Enable Google Drive API:
    1. Go to https://console.cloud.google.com
    2. Select the same GCP project you use for your Apps Script pipeline
    3. Click "APIs & Services" -> "Enable APIs and Services"
    4. Search for "Google Drive API" and click Enable

Step 2 — Create OAuth credentials:
    1. Still in APIs & Services, click "Credentials"
    2. Click "Create Credentials" -> "OAuth client ID"
    3. Application type: Desktop app
    4. Name: screener-collector  (or any name you like)
    5. Click Create, then click "Download JSON"
    6. Rename the downloaded file to:  credentials.json
    7. Move it to:
       C:\\Users\\SUMIT SHARMA\\OneDrive\\Desktop\\screener_collector\\

Step 3 — Install required packages (run once in your terminal):
    pip install google-api-python-client google-auth-oauthlib google-auth-httplib2

Step 4 — First run (authorise):
    py convert_sheets.py
    A browser window will open. Sign in with your Google account and click Allow.
    This creates token.json in the same folder — all future runs are silent.

That's it. From now on, screener_collect.py also converts automatically after
every download (using the same credentials.json and token.json).
============================================================
"""

import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

# ---------------------------------------------------------------------------
# Drive API helpers
# ---------------------------------------------------------------------------

def get_drive_service():
    """Build authenticated Google Drive API service. Exits with instructions if not set up."""
    try:
        from googleapiclient.discovery import build
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
    except ImportError:
        print(
            "\n  Required packages not installed."
            "\n  Run this command first:"
            "\n"
            "\n      pip install google-api-python-client google-auth-oauthlib google-auth-httplib2"
            "\n"
            "\n  Then re-run:  py convert_sheets.py"
        )
        sys.exit(1)

    SCOPES     = ["https://www.googleapis.com/auth/drive"]
    token_path = SCRIPT_DIR / "token.json"
    creds_path = SCRIPT_DIR / "credentials.json"
    creds      = None

    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception:
                creds = None

        if not creds or not creds.valid:
            if not creds_path.exists():
                print(
                    "\n  credentials.json not found."
                    "\n  Please follow the ONE-TIME SETUP instructions at the top of this file."
                    "\n"
                    "\n  Short version:"
                    "\n    1. Go to console.cloud.google.com -> your GCP project"
                    "\n    2. APIs & Services -> Credentials -> Create Credentials"
                    "\n       -> OAuth client ID -> Desktop app -> Download JSON"
                    "\n    3. Rename to credentials.json and put it in:"
                    f"\n       {SCRIPT_DIR}"
                    "\n    4. Re-run:  py convert_sheets.py"
                )
                sys.exit(1)

            flow  = InstalledAppFlow.from_client_secrets_file(str(creds_path), SCOPES)
            creds = flow.run_local_server(port=0)
            token_path.write_text(creds.to_json(), encoding="utf-8")
            print("  Authorised successfully. token.json saved.")

    return build("drive", "v3", credentials=creds)


# ---------------------------------------------------------------------------
# Conversion logic
# ---------------------------------------------------------------------------

def get_all_xlsx(service):
    """Return list of all Financials.xlsx on Drive (not trashed)."""
    all_files = []
    page_token = None

    while True:
        params = dict(
            q          = "name='Financials.xlsx' and trashed=false",
            fields     = "nextPageToken, files(id, name, parents)",
            pageSize   = 100
        )
        if page_token:
            params["pageToken"] = page_token

        response   = service.files().list(**params).execute()
        all_files += response.get("files", [])
        page_token = response.get("nextPageToken")

        if not page_token:
            break

    return all_files


def gsheet_exists_in_same_folder(service, parent_id):
    """Return True if a Google Sheet named 'Financials' already exists in parent_id."""
    if not parent_id:
        return False
    existing = service.files().list(
        q=(
            f"name='Financials' and "
            f"'{parent_id}' in parents and "
            f"mimeType='application/vnd.google-apps.spreadsheet' and "
            f"trashed=false"
        ),
        fields="files(id)"
    ).execute().get("files", [])
    return len(existing) > 0


def convert_xlsx_list(service, xlsx_files, dry_run=False):
    """
    Convert each xlsx in xlsx_files to Google Sheets.
    Skips files that already have a matching GSheet.
    Deletes the xlsx after successful conversion.

    dry_run=True: print what would happen without actually converting.
    """
    converted = 0
    skipped   = 0
    failed    = 0

    for i, f in enumerate(xlsx_files, 1):
        file_id   = f["id"]
        parent_id = f["parents"][0] if f.get("parents") else None

        print(f"\n  [{i}/{len(xlsx_files)}]  id={file_id}", end="")

        # Skip if already converted
        if gsheet_exists_in_same_folder(service, parent_id):
            print("  ->  already converted, skipping")
            skipped += 1
            continue

        if dry_run:
            print("  ->  WOULD convert (dry run)")
            converted += 1
            continue

        try:
            # Create Google Sheet copy
            service.files().copy(
                fileId=file_id,
                body={
                    "name":     "Financials",
                    "mimeType": "application/vnd.google-apps.spreadsheet"
                }
            ).execute()

            # Delete the xlsx
            service.files().delete(fileId=file_id).execute()

            print("  ->  converted and xlsx deleted")
            converted += 1

        except Exception as e:
            print(f"  ->  FAILED: {str(e)[:100]}")
            failed += 1

    return converted, skipped, failed


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    dry_run = "--dry-run" in sys.argv

    print(f"\n{'='*60}")
    print(f"  GOOGLE SHEETS BULK CONVERTER")
    if dry_run:
        print(f"  DRY RUN MODE — no changes will be made")
    print(f"{'='*60}")

    print("\n  Connecting to Google Drive API...")
    service = get_drive_service()
    print("  Connected.")

    print("\n  Searching for Financials.xlsx files on Drive...")
    xlsx_files = get_all_xlsx(service)

    if not xlsx_files:
        print("  No Financials.xlsx files found on Drive.")
        print("  Either there are none, or Drive has not synced yet.")
        print("  If you just ran a download, wait 30 seconds and try again.")
        sys.exit(0)

    print(f"  Found {len(xlsx_files)} Financials.xlsx file(s).")

    converted, skipped, failed = convert_xlsx_list(service, xlsx_files, dry_run=dry_run)

    print(f"\n{'='*60}")
    print(f"  DONE")
    print(f"  Converted : {converted}")
    print(f"  Skipped   : {skipped}  (GSheet already existed)")
    print(f"  Failed    : {failed}")
    if failed:
        print(f"  Re-run this script to retry failed conversions.")
    if dry_run:
        print(f"\n  This was a dry run. Re-run without --dry-run to apply changes.")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
