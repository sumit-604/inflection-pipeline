# tools/collector

The screener.in corpus collector, now inside the repo so `/step1` and manual
runs are self-contained. No external Desktop folder is needed.

## What is here (versioned)

- `collect_to_repo.py` — companies.txt -> screener.in -> repo. Downloads the main
  company and its peers, classifies the PDFs into
  `runs/<ticker>-<date>/inputs/...`, writes `manifest.yaml`. Flags: `--dry-run`
  (stage locally, no push), `--push-again` (re-push the latest run folder).
- `screener_collect.py` — the single-company downloader `collect_to_repo` calls.
- `collect_batch.py` — downloads to Google Drive only (no git). Legacy path.
- `convert_sheets.py`, `check_readiness.py`, `prepare_run.py` — helpers.
- `companies.txt.example` — the input format. `/step1` writes the live
  `companies.txt` (gitignored) each run.

## What is NOT here (secrets — you place these once, they are gitignored)

The collector needs three credential files in THIS folder. They are never
committed (see `.gitignore`). Copy them once from the old Desktop collector:

```bash
cp "/c/Users/SUMIT SHARMA/OneDrive/Desktop/screener_collector/.env" tools/collector/
cp "/c/Users/SUMIT SHARMA/OneDrive/Desktop/screener_collector/credentials.json" tools/collector/
cp "/c/Users/SUMIT SHARMA/OneDrive/Desktop/screener_collector/token.json" tools/collector/
```

- `.env` — `SCREENER_EMAIL` and `SCREENER_PASSWORD` for the screener login.
- `credentials.json`, `token.json` — Google OAuth for the xlsx -> Google Sheet
  conversion step.

Without these the download and conversion steps fail. `git status` must never
show any of the three; if it does, stop and fix `.gitignore` before committing.

## Running it

Always set `PYTHONUTF8=1` (the summary prints the rupee sign, which crashes
under Windows cp1252 when output is redirected):

```bash
cd tools/collector
PYTHONUTF8=1 py collect_to_repo.py --dry-run
```

`/step1 <company>` drives all of this automatically; run it by hand only to
debug. The old `C:\Users\SUMIT SHARMA\OneDrive\Desktop\screener_collector`
folder can stay as a backup but is no longer the source of truth.
