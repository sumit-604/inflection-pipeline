# tools/collector

The screener.in corpus collector, now inside the repo so `/step1` and manual
runs are self-contained. No external Desktop folder is needed.

## What is here (versioned)

- `collect_to_repo.py` — companies.txt -> screener.in -> repo. Downloads the main
  company and its peers, classifies the PDFs into
  `runs/<ticker>-<date>/inputs/...`, writes `manifest.yaml`. Runs with
  `--no-drive`: it does NOT touch Google Drive. Flags: `--dry-run` (stage, no
  push), `--push-again` (re-push the latest run folder).
- `screener_collect.py` — the single-company downloader `collect_to_repo` calls.
  Accepts `--no-drive` to skip the Google Drive check and the Google Sheet
  conversion.
- `collect_batch.py` — LEGACY. Downloads to Google Drive and converts to Google
  Sheets. This is the only path that still needs Google credentials.
- `convert_sheets.py`, `check_readiness.py`, `prepare_run.py` — legacy Drive helpers.
- `companies.txt.example` — the input format. `/step1` writes the live
  `companies.txt` (gitignored) each run.

## Secrets — you place these on disk, they are gitignored (never committed)

**REQUIRED for `/step1` and `collect_to_repo.py`: `.env` only.**

One file, `tools/collector/.env`, with two lines:

```
SCREENER_EMAIL=your_screener_email
SCREENER_PASSWORD=your_screener_password
```

That is the whole requirement now. Because the repo path runs `--no-drive`, it
never signs into Google, so it needs no Google files.

**OPTIONAL — `credentials.json` and `token.json` (Google OAuth).** Needed ONLY by
the legacy `collect_batch.py` Google-Drive workflow. Leave them out unless you
use that path.

`.gitignore` in this folder excludes `.env`, `credentials.json`, `token.json`,
and the per-run `companies.txt`. After you create `.env`, run `git status` — it
must NOT list `.env`. If it does, stop and fix `.gitignore` before committing.

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
