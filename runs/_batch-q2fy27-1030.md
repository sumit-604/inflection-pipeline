# Q2 FY27 results batch, 30-Oct-2026 (new machine; collection only, review ran outside the repo)

STATUS 30-Oct 02:00 IST: the operator ran the 20 reviews through the Claude API outside this repo and cancelled the /run-quarterly batch here before any company session started. No `runs/<ticker>-q2fy27/` folder exists for these names. This record keeps the collection on file: documents, transcripts, prices and the machine setup. The batch plan and standing instructions below stand for the next run on this machine.

Request (operator, 29-Oct evening IST): run the quarterly review for the 20 watchlist names that reported on 28-Oct-2026 (list from the screener feed window 28-Oct 05:55 to 29-Oct 05:00). Nothing from the 17-Oct, 19-Oct, 23-24-Oct or 28-29-Oct batches is repeated; the dedupe was checked against `yesterday_list.csv` and HANDOVER.md Part 2 on 30-Oct. ROUTE stays parked.

Machine: new Windows 11 laptop, 24 GB RAM, 12 logical CPUs, no GPU. Sessions run up to eight at a time (operator instruction: batch of 8). Company sessions run on Opus 5.5 at medium effort; subagents A1-A5 run at the model and effort pinned in `.claude/agents/` (operator ruling pending at the time of writing; see coordinator log).

Coordinator: the Fable 5.1 session that prepared the machine. Company sessions: one per name, each in its own worktree on branch `claude/qr-<ticker>-q2fy27-<hash>`, merged into `run/quarterly-q2fy27-2026-10-30` on commit.

Files on disk: `C:\ConcallPipeline\Daily Concall Intelligence\Q2 FY27 Results\` folders 36 to 55. Document tables: `_DOCS_2026-10-30_partA.md` (36-45) and `_DOCS_2026-10-30_partB.md` (46-55). Price snapshot for every name: `_CMP_snapshot_2026-10-30.md` (screener.in, read 30-Oct 00:30 IST). ASR queue status: `_ASR_STATUS.md`.

## Names, documents held, call status (as of 30-Oct 00:45 IST)

| # | Name | Ticker | Folder | Results | Deck | Press release | Call | Recording / transcript |
|---|---|---|---|---|---|---|---|---|
| 1 | Aarti Pharmalabs | AARTIPHARM | 36 Aarti Pharmalabs | 16p text (Results_2 is the 4.4 MB clear version) | 30p | none | 29-Oct 15:30 | company page https://www.aartipharmalabs.com/q2-fy-27/ ; ASR queued if audio found |
| 2 | Aeroflex Industries | AEROFLEX | 37 Aeroflex Industries | 17p text, 5 pages image-only | 33p | none | 29-Oct 11:00 | mp3 held; ASR queued |
| 3 | Bandhan Bank | BANDHANBNK | 38 Bandhan Bank | 12p text (board outcome carries results and press release) | 45p | inside results | 28-Oct 17:15 | company page, no direct audio URL; ASR queued if audio found |
| 4 | Fabtech Technologies | FABTECH | 39 Fabtech Technologies | 21p text | none | yes | 30-Oct 14:00 (today) | none yet |
| 5 | Forbes Precision Tools | 544186 | 40 Forbes Precision Tools and Machine Parts | 8p SCAN (pages 3-8 no text; OCR) | none | none | none found | none |
| 6 | Goodluck India | GOODLUCK | 41 Goodluck India | 15p SCAN (8 pages no text; OCR); results = board outcome = press release, same bytes | none | same file | 31-Oct 11:30 (future) | none |
| 7 | Hexaware Technologies | HEXT | 42 Hexaware Technologies | 40p text, 7 pages image-only (company calls it Q3 CY2026) | 27p | none | 29-Oct 08:00 | company page https://hexaware.com/investors/quarterly-results/ ; ASR queued if audio found |
| 8 | Kotyark Industries | KOTYARK | 43 Kotyark Industries | 15p text | none | yes | none found | none |
| 9 | Macfos | 543787 | 44 Macfos | 15p SCAN (14 pages no text; OCR) | 26p | none | 3-Nov 16:00 (future) | none |
| 10 | Onemi Technology Solutions (Kissht) | KISSHT | 45 Onemi Technology Solutions | 20p SCAN (15 pages no text; OCR) | 43p | yes | 29-Oct 12:00 | mp3 held; ASR queued |
| 11 | PNGS Gargi Fashion Jewellery | 543709 | 46 PNGS Gargi | 7p text | 29p | none | no call filing | none |
| 12 | PVR Inox | PVRINOX | 47 PVR Inox | 13p text | 38p | 4p | 28-Oct, time not stated | mp3 held; ASR queued |
| 13 | Raymond Lifestyle | RAYMONDLSL | 48 Raymond Lifestyle | 25p text (press release and board outcome are the same file) | 32p | inside results | 29-Oct 17:00 | mp3 held; ASR queued |
| 14 | Refex Industries | REFEX | 49 Refex Industries | 16p text | 51p | 3p | 29-Oct 11:30 | company page; ASR queued if audio found |
| 15 | Sasken Technologies | SASKEN | 50 Sasken Technologies | 65p text (audited; seven BSE rows carry the same file) | none in window | none in window | 29-Oct 15:00 | company page; ASR queued if audio found |
| 16 | Satin Creditcare Network | SATIN | 51 Satin Creditcare | 16p text | 36p | 6p | 29-Oct, time not stated | mp3 held; ASR queued |
| 17 | Shilchar Technologies | SHILCTECH | 52 Shilchar Technologies | 5p text | 33p | none | 29-Oct, time not stated | mp3 held; ASR queued |
| 18 | Vaibhav Global | VAIBHAVGBL | 53 Vaibhav Global | 16p text | 41p | 5p | 29-Oct, time not stated | mp3 held; ASR queued |
| 19 | Womancart | WOMANCART | 54 Womancart | NSE only; connector-rebuilt text PDF (see folder SOURCES.md) or none | per rebuild | per rebuild | unknown | none |
| 20 | Zota Health Care | ZOTA | 55 Zota Health Care | NSE only; connector-rebuilt text PDF (see folder SOURCES.md) or none | per rebuild | per rebuild | unknown | none |

No company filed a concall transcript in the window. Machine transcripts, when they land, are `<Short>_Q2FY27_Concall_Transcript_ASR.txt` in each `concall_audio\` folder.

## Batches (by readiness, eight at a time)

- Batch 1 (filed documents only, no transcript dependency): 544186 Forbes, KOTYARK, 543709 PNGS, FABTECH, GOODLUCK, 543787 Macfos, WOMANCART, ZOTA. If a rebuilt PDF for WOMANCART or ZOTA is not on disk when the batch starts, that name moves to batch 3 and the batch runs with six or seven.
- Batch 2 (direct mp3 held, ASR first in the queue): AEROFLEX, KISSHT, PVRINOX, RAYMONDLSL, SATIN, SHILCTECH, VAIBHAVGBL, AARTIPHARM.
- Batch 3 (recording from company pages): BANDHANBNK, HEXT, REFEX, SASKEN, plus any carry-over.

Start the next session only when one finishes. Restart a failed start in place, never as a second session.

## Standing instructions for every company session (read before `/run-quarterly`)

1. Work only in your worktree. Run folder `runs/<ticker lowercase>-q2fy27/` (BSE-code names use the code, e.g. `runs/544186-q2fy27/`). Copy the input PDFs from the company's folder under `C:\ConcallPipeline\Daily Concall Intelligence\Q2 FY27 Results\` into `runs/<ticker>-q2fy27/inputs/` and write `inputs/SOURCES.md` naming each file's origin (copy the lines from the folder's SOURCES.md; BSE attachment URL, company website URL, or connector). Never touch another name's run folder.
2. Transcripts: a machine transcript, when present, is `<Short>_Q2FY27_Concall_Transcript_ASR.txt` in the company's `concall_audio/` folder (faster-whisper small.en, chunked, beam 3). Treat it as ASR: management-tier, unverified, numbers may be misheard. Check for it once before A4 starts; if it has appeared since the run began, run A1-A3 on it as `concall` before A4. If it is absent, run on the filed documents only and say so in the review header and the brief.
3. Toolchain: poppler is on PATH. Tesseract is at `C:\Program Files\Tesseract-OCR\tesseract.exe` (also on the user PATH; call by full path if the shell does not find it). Four results filings are scans (Forbes, Goodluck, Macfos, Onemi): render with `pdftoppm -r 200 -png` and OCR with tesseract `--psm 6`, and check `pdftotext` output against page images before trusting any statement page. Refresh PATH at the start of each PowerShell call if a tool is missing: `$env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User')`.
4. One correction loop by default. A second loop only for an A5 item tagged FACTUAL or CONTRADICTION that moves a verdict-card number. Wording and label items stay logged.
5. Subagents run in the foreground. If an agent step writes nothing for 30 minutes (check the newest file timestamp in `work/`), restart that step once.
6. Do not write to Notion. Write `notion-payload.md` in the run folder for the operator's approval. If the company has no COMPANIES MASTER page, say so in the payload and leave the create-row payload for the operator.
7. Close-out, in this order: `session-cost.md` (per-agent token ledger), then `operator-brief.md` in the run folder in the format of `_Operator_Briefs_Q2FY27_2026-10-28.md` in the files folder (10-12 plain narrative points, FY27E and FY28E revenue and PAT with basis and evidence tier per number, two readings and the separating observation, forward PE at the CMP from `_CMP_snapshot_2026-10-30.md`; indicative only, not a Role 1 valuation, no Section 1B exit multiple). Then `git add runs/<ticker>-q2fy27` and `git commit -q -m "quarterly review: <TICKER> q2fy27"`. If the commit fails on `index.lock`, wait 30 seconds and retry; never run `git stash` or `git reset`. Report the commit hash and `git log -1 --stat`.
8. Stuck rule: stop after three unchanged repeats or five turns with nothing new; report what you tried; mark the run blocked.
9. Prose to the operator in STE (one idea per sentence, 20 words or fewer, active voice, no dashes as punctuation).
10. Connector-rebuilt filings (Womancart, Zota): say in the review header, the brief and the payload that the filing is a connector rebuild, not the exchange original, and mark every number pending verification against the NSE original.

## Token ledger (filled by the coordinator from each run's session-cost.md)

| Name | Run folder | total_run_tok | Loops | A5 verdict | Commit |
|---|---|---|---|---|---|

## Problems log (coordinator)

- 30-Oct 00:00-00:45 IST: machine prepared (git, gh, Python 3.12 and 3.14, poppler, tesseract, ffmpeg, faster-whisper small.en). Filings for 18 names pulled from the BSE API; Womancart and Zota are NSE-only and the NSE API returned 403, so their filings are being rebuilt from the Bull AI connector (Neochem precedent). Aeroflex BSE code is 543972, not 543916. Repo clone waited on the operator's `gh auth login`.
- 30-Oct 00:39-01:28 IST: nine call recordings transcribed (faster-whisper small.en, int8, beam 3, three jobs at once, 4 threads each): Hexaware, Aeroflex, Refex, Sasken, Aarti Pharmalabs, Raymond Lifestyle, Satin, Shilchar, Vaibhav Global. About nine hours of audio in 50 minutes on the 12-core machine. Transcripts sit in each company's `concall_audio/` as `<Short>_Q2FY27_Concall_Transcript_ASR.txt`. Status file `_ASR_STATUS.md`.
- Recordings not obtained: PVR Inox and Onemi (CDN returns 403 to scripts; no bypass attempted), Bandhan (page lists no audio). Future calls: Fabtech 30-Oct 14:00, Goodluck 31-Oct 11:30, Macfos 3-Nov 16:00. No call: Forbes, Kotyark, PNGS. Zota call 29-Oct 12:00, recording link relative only.
- 30-Oct 01:00 IST: Womancart (13p results outcome, incl. Rs 12 Cr rights issue) and Zota (10p results, 48p deck, call intimation, audio-link notice) rebuilt from Bull AI connector text into text-layer PDFs; hand-transcribed by the session, not machine-exported; every number pending verification against the NSE original. Bull AI calls used today: about 12 of the 631 remaining this cycle.
- 30-Oct 01:45 IST: operator cancelled the review (done via the Claude API). Machine stabilisation continued: repo sparse-cloned to `C:\Users\sumit\repos\inflection-pipeline` (main at 2bf99f1c), checkout guard CLEAN, protocol files present, toolchain precheck passed, OCR path proven on the Forbes scan (page 3: pdftotext 1 char, tesseract 465 words). Task Scheduler job `\ConcallPipeline\Watchlist Announcements 0500` re-registered (daily 05:00, `fetch_announcements.bat`, python path patched to this machine). Project allow list for the Notion write tool prepared as `settings.local.json.PROPOSED-for-repo-.claude` in the ConcallPipeline folder (the session may not write `.claude/` settings itself; operator copies it to `.claude/settings.local.json`).
- Open setup items for the operator: user-level `~/.claude/settings.json` and project memory restore (blocked as self-modification; one-line command given in chat), Trendlyne MCP token, agent effort ruling (medium vs pinned high/xhigh), KeePassXC and Google Drive for desktop if wanted.
