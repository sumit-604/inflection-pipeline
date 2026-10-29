# HANDOVER 2026-10-29: /run-quarterly daily results review

Prepared 2026-10-29 on the old machine (Windows 11 Home, user `SUMIT SHARMA`, 6 GB RAM, no GPU) for a fresh Claude Code session on a new Windows machine. No review was run while packaging. Secrets are named, never pasted; the real `.env` files travel only inside the zip under `untracked/` and are gitignored on the branch.

Folder map of this handover:

| Folder | Holds |
|---|---|
| `HANDOVER.md` | this file: answers to the 13 questions |
| `RUNBOOK.md` | bare machine to one successful run, installs, failure modes |
| `yesterday_list.csv` | the 16 names of the 28-29-Oct batch with branch, commit, A5 verdict, Notion state |
| `repo/` | verbatim copies of the pipeline definition from the repo (frameworks, prompts, commands, agents, hooks, skills, settings, CLAUDE.md, tools, companies/) |
| `concall-pipeline/` | the download and daily-review scripts from `C:\ConcallPipeline\Daily Concall Intelligence` plus the season ledgers and a file listing of the source-document tree |
| `runs/` | the 16 run folders of the 28-29-Oct batch (15 closed plus ROUTE paused), the batch record, and the earlier batch records (17-Oct, 19-Oct) |
| `review/` | the daily watchlist deep review (REVIEW.md, INDEX.md, companies.json) for the two windows 26-Oct 20:17 to 28-Oct 05:55 and 28-Oct 05:55 to 29-Oct 05:00 |
| `claude-config/` | user-level Claude Code settings, project memory, scheduled tasks, the notion-save skill text, the redacted MCP registration, the ASR and BSE helper scripts |
| `untracked/` | gitignored files the pipeline needs: the two `.env` files and `companies.txt` (zip only) |
| `env/` | redacted `.env.example` files, pip freezes for both interpreters, tool versions |

## PART 1. THE ANALYSIS REPOSITORY

### 1. Repo identity

- Local path (old machine): `C:\Users\SUMIT SHARMA\repos\inflection-pipeline`
- Remote: `origin  git@github.com:sumit-604/inflection-pipeline.git` (fetch and push). GitHub: https://github.com/sumit-604/inflection-pipeline (private)
- Default branch: `main`. `origin/main` = `2bf99f1c` ("chartink data: 2026-10-28").
- Checked-out branch in the main working copy at packaging time: `screens/shallow-2026-10-27`, HEAD `70ac3240` ("screens: shallow cards for eight names (2026-10-29); TIPSMUSIC rewrite; run record"). Pushed; equal to `origin/screens/shallow-2026-10-27`.
- `git status --short` in the main working copy: 159 lines, all under `data/chartink/` (the nightly Chartink breadth job regenerates and pushes these from its own worktree `C:\Users\SUMIT SHARMA\AppData\Local\Temp\ip-main` on branch `tools/chartink-push-main`; they are not part of this handover) plus three unrelated personal PDFs at the repo root (`Ayush_*.pdf`, not committed, not part of the pipeline).
- The working copy is a sparse checkout (`tools/sparse_session.sh`): everything outside `runs/` plus `runs/_template`, every run's `session-cost.md` and `manifest.yaml`. Quarterly runs live in git worktrees under `.claude/worktrees/` on their own branches (see item 6).

### 2. Push state

Done during packaging (2026-10-29):

| Branch | Commit | On GitHub |
|---|---|---|
| `screens/shallow-2026-10-27` | 70ac3240 | yes |
| `run/quarterly-q2fy27-2026-10-28` (the 28-29-Oct batch, 15 names merged plus the 11 "notion write recorded" commits merged in now) | 7b4f4162 | yes, new branch |
| `claude/qr-route-q2fy27-fb3514` (ROUTE, paused; its untracked `runs/route-q2fy27/` committed now) | bc9c448b | yes |
| the other 15 `claude/qr-<ticker>-q2fy27-<hash>` branches | see `yesterday_list.csv` | yes |
| `run/quarterly-q2fy27-2026-10-17`, `run/quarterly-q2fy27-2026-10-19`, and the 32 `claude/quarterly-<name>-q2fy27-<hash>` branches of the 17-24-Oct batches | various | pushed in the same session (verify with `git ls-remote --heads origin 'claude/quarterly-*'`) |
| `handover/2026-10-29` (this folder, minus `.env` files) | 3d4c4ec0 (first commit; this hash line added in the commit that follows it) | yes |

`companies/*.md`: no uncommitted change; no quarterly run of 27-29 Oct wrote one (none of the 16 names has a `companies/<TICKER>.md` except AEQUS and SYNGENE, which were not touched). `REVIEW.md` is not in the repo at all: it lives in `C:\ConcallPipeline\Daily Concall Intelligence\announcements\<window>\REVIEW.md` (not a git repo) and is copied under `review/`.

Gitignored but required to run (copied under `untracked/`, zip only):

| Relative path | Why |
|---|---|
| `tools/collector/.env` | `SCREENER_EMAIL`, `SCREENER_PASSWORD` for `collect_to_repo.py` / `screener_collect.py` (Phase 1 corpus collector; not used by /run-quarterly) |
| `tools/collector/companies.txt` | the collector's input list |
| `C:\ConcallPipeline\Daily Concall Intelligence\.env` | `SCREENER_EMAIL`, `SCREENER_PASSWORD` (feed download), `NEWSLETTER_SENDER_EMAIL`, `NEWSLETTER_GMAIL_APP_PASSWORD`, `NEWSLETTER_RECIPIENT_EMAIL`, `DISCORD_WEBHOOK_URL`, `DISCORD_BOT_NAME` |

Other gitignored paths (`runs/*/work/raster/`, `runs/*/work/*.txt`, `runs/*/extracted/images/`, `screens/corpus/**/*.pdf`, `data/chartink/**/*.html`) are derived artefacts; nothing in /run-quarterly needs them. There are no model files or caches inside the repo. The whisper model cache is outside the repo (item 4).

### 3. Pipeline definition files copied verbatim (under `repo/`)

- `frameworks/` (all 19 files): `Quarterly_Results_Review_Protocol_v1_4.md`, `Quarterly_Concall_Analysis_Protocol_v1_1.md`, `Document_Review_Protocol_v1_1.md`, `Master_Project_Prompt_v3_6.md` (banner v3.7), `Annual_Report_Analysis_Protocol_v1_3.md`, `FTTCP_v2_1_Consolidated.md`, `Debt_Capacity_Assessment_v1_0.md`, `Market_Implied_Assumptions_v1_0.md`, `Downstream_Source_Discovery_Protocol_v1_0.md`, `Section_1B_v3.3_Amendments.md` through `Section_1B_v3_10_Amendments.md`, `Section_1B_v3_5_1_Reconciliation.md`, `success_catalogue.md`, `README.txt`.
- The command: `.claude/commands/run-quarterly.md` (169 lines). It reads `prompts/quarterly-00-orchestrator.md` (339 lines) as the authority on sequence, gates, file names, dispatch and the Notion save. Agent prompts: `prompts/quarterly-a1-extractor.md`, `quarterly-a2-enumerator.md`, `quarterly-a3-forensics.md`, `quarterly-a4-analyst.md`, `quarterly-a5-adversary.md`. Agent definitions with model routing: `.claude/agents/quarterly-a1-extractor.md` .. `quarterly-a5-adversary.md`. The loop and re-audit are not separate files: the orchestrator prompt and the command's section 3 define them (one loop back to the named agent, A5 re-audit). The operator brief format is defined by the batch standing instruction 7 in `runs/_batch-q2fy27-1028.md` and the example file `concall-pipeline/Q2 FY27 Results/_Operator_Briefs_Q2FY27.md`. The Notion save is defined in `prompts/quarterly-00-orchestrator.md` section "NOTION SAVE", the command's section 4, and the claude.ai skill `claude-config/skills/notion-save/SKILL.md` with `references/schema.md`. The other commands (`run-pipeline`, `step1`, `fttcp`, `finalize`, `compost`) and all 14 Phase-1 prompts are included for completeness.
- `CLAUDE.md`: only one exists, at the repo root. There is no `~/.claude/CLAUDE.md` and no CLAUDE.md in `C:\ConcallPipeline`. Also copied: `HANDOFF.md`, `LESSONS.md`, `Narrative_Writing_Style_v1.md`, `anti-ai-writing-style.md`, `team_workflow_project_instructions.md`, `claude-web/PROJECT_INSTRUCTIONS.md`, `README.md`, `VERSIONING.md`, `.gitignore`. `LESSONS_ARCHIVE.md` is not copied (large; it is on `main`).
- `.claude/settings.json` (project: subagent prompt cache TTL 1h, SessionStart hook), `.claude/settings.local.json` (allow rules), `.claude/shadow.yaml`, `.claude/hooks/session-start.sh`, `.claude/hooks/lessons-phrase-check.py`, `.claude/skills/section-1b/` (17 chunks; the valuation authority, not read by /run-quarterly). There is NO `.mcp.json` in the repo or in the ConcallPipeline folder.
- Scripts the pipeline calls: `tools/extract_pdfs.py` (pypdf page-marked text), `tools/ocr_repair.py` (pdftoppm + tesseract, resumable), `tools/check_extraction.py`, `tools/extract_block.py`, `tools/check_url.py`, `tools/sparse_session.sh`, `tools/dry_check.sh`, `tools/collector/` (`collect_to_repo.py`, `collect_batch.py`, `screener_collect.py`, `fetch_ratings.py`, `prepare_run.py`, `check_readiness.py`, `convert_sheets.py`, README, SETUP_INSTRUCTIONS, COMMANDS). A1 extraction itself is done by the subagent with `pdftotext -layout`, `pdfinfo`, `pdffonts`, `pdftoppm` and tesseract through Bash; there is no standalone A1 script. ASR: `claude-config/scripts/transcribe_faster_whisper.py` (the runner the coordinator used; it lived in a session scratchpad, not in the repo). Notion save helpers: none in code; the save is made inline with the Notion MCP tools.
- `companies/` (all 43 per-company memory files) and `verifiers/`, `runs/_template/`.

### 4. Tool chain for a fresh Windows machine

Captured versions are in `env/toolchain-versions.txt`; the exact install commands are in `RUNBOOK.md` section 1. Summary:

| Tool | Version on old machine | Install | Path |
|---|---|---|---|
| Python | 3.14.4 (holds ASR and OCR packages; `py -3.14`) and 3.15.0 (default `python`, small set) | `winget install -e --id Python.Python.3.14` | `%LOCALAPPDATA%\Python\pythoncore-3.14-64\python.exe` |
| pip packages | `env/requirements-python314-asr-ocr.txt` (190 pins: faster-whisper 1.2.1, ctranslate2 4.8.3, av 19.0.1, numpy 2.5.0, pymupdf 1.28.2, pypdf 6.14.2, pdfplumber 0.11.10, playwright 1.58.0, python-dotenv 1.2.2, beautifulsoup4 4.15.0, yt-dlp, pandas 3.0.3, torch 2.12.1 (not needed), rapidocr, docling (not needed)); `env/requirements-python315-main.txt` (35 pins) | `py -3.14 -m pip install -r env\requirements-python314-asr-ocr.txt` or the short list in the RUNBOOK | |
| Poppler (pdftotext, pdfinfo, pdffonts, pdftoppm) | 25.07.0 via winget; an msys xpdf 4.06 `pdftotext` also sits earlier on PATH | `winget install -e --id oschwartz10612.Poppler`; add `...\poppler-25.07.0\Library\bin` to PATH | `%LOCALAPPDATA%\Microsoft\WinGet\Packages\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe\poppler-25.07.0\Library\bin` |
| Tesseract OCR | 5.4.0.20240606 (leptonica 1.84.1), English only | `winget install -e --id UB-Mannheim.TesseractOCR` | `C:\Program Files\Tesseract-OCR\tesseract.exe` (NOT on PATH; call by full path) |
| OCR engine in code | tesseract via `tools/ocr_repair.py` and the A1 fallback; `rapidocr-onnxruntime` is installed but no pipeline script calls it; no PaddleOCR | | |
| ffmpeg / ffprobe | 9.0.2 full build (gyan.dev) | `winget install -e --id Gyan.FFmpeg` | `%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin` |
| faster-whisper models | `Systran/faster-whisper-small.en` (464 MB, the one used), `Systran/faster-whisper-medium.en` (1.5 GB, stalls on 6 GB RAM), `mobiuslabsgmbh/faster-whisper-large-v3-turbo` (incomplete, 3.7 MB) | downloads on first `WhisperModel('small.en')` | `%USERPROFILE%\.cache\huggingface\hub\models--Systran--faster-whisper-small.en` |
| git | 2.x (msys) | `winget install -e --id Git.Git` | |
| gh | logged in as `sumit-604` via `GITHUB_TOKEN` (fine-grained PAT in the old machine's environment) | `winget install -e --id GitHub.cli`; `gh auth login` | |
| node | not installed; not needed | | |
| Playwright Chromium | for `fetch_announcements.py`, `login.py`, `download*.py` | `py -3.14 -m playwright install chromium` | |
| KeePassXC | installed; the operator's password manager | | `C:\Program Files\KeePassXC` |

GPU: none on the old machine and none required. Without a GPU: faster-whisper runs CPU int8 at roughly real time with small.en (one hour of call in 15 to 60 minutes; one job at a time on 6 GB); tesseract OCR of a 20-page scan takes a few minutes; nothing else is compute bound. No step breaks without a GPU; `medium.en` breaks on low RAM regardless.

### 5. How source documents are fetched

/run-quarterly fetches nothing. It takes `--docs` paths. The documents were obtained by these routes, in the order used:

| Document | Route | Script and function |
|---|---|---|
| Results PDF, investor presentation, press release, intimations | Screener.in watchlist announcement feed, daily 05:00 download (logged in with Playwright) | `C:\ConcallPipeline\Daily Concall Intelligence\fetch_announcements.py` (`main()`; GET `https://www.screener.in/dash/85202/?timestamp=<data-last-timestamp>` with header `X-Requested-With: XMLHttpRequest`, pages until the cutoff in `announcements\last_run.txt`; writes `announcements\<since>_to_<now>\<Company>_<Title>_<hash>.pdf`, `INDEX.md`, `companies.json`). Task Scheduler "Watchlist Announcements 0500" runs `fetch_announcements.bat`. |
| The same, for a named company and date range | BSE announcements API and attachment store, no login | `claude-config/scripts/bse_list.py` (lists filings for a scrip code via `https://api.bseindia.com/BseIndiaAPI/api/AnnSubCategoryGetData/w` with the headers `BSE_ANN`/`BSE_HEADERS` imported from `tools/collector/collect_to_repo.py`) and `bse_get.py` (downloads `https://www.bseindia.com/xml-data/corpfiling/AttachLive/<attachment>.pdf`, falling back to `AttachHis/`). For the 28-Oct batch the coordinator session downloaded files by hand with these endpoints and the company investor pages, and recorded each origin in `runs/<ticker>-q2fy27/inputs/SOURCES.md`. |
| NSE filings | `https://nsearchives.nseindia.com/corporate/...pdf`; refuses automated fetches with a bot check (Neochem 28-Oct) | no script; browser download by the operator, or fall back to Bull AI |
| Filing text when no PDF can be fetched | Bull AI MCP (claude.ai connector): `search_company_documents`, `get_document_chunks`, `list_document_availability` | no script; the Neochem run rebuilt a labelled text PDF from the connector's page text (`runs/neochem-q2fy27/inputs/Neochem_H1FY27_Results_Board_Outcome_REBUILT_from_BullAI.pdf`). Per operator ruling, say plainly that no file was downloaded. |
| Concall audio | Link in the call-recording intimation PDF (read the PDF link annotation, not the extracted text) or the company investor page; mp3 direct, or mp4 with audio pulled by ffmpeg; yt-dlp is installed for hosted players | no fixed script; the coordinator fetched with WebFetch/curl into `Q2 FY27 Results\NN <Company>\concall_audio\<Company>_Q2FY27_Concall.mp3` |
| Concall transcript | Filed transcript when present (Screener feed or BSE); else machine transcript | `claude-config/scripts/transcribe_faster_whisper.py <audio> <out.txt> small.en` (faster-whisper, int8, 600 s chunks through ffmpeg, VAD on, resumable parts folder). `download.py` shows the older screener.in "View Transcript" route (`https://www.screener.in/concalls/`). |
| Prices and market cap (CMP snapshot, operator brief forward PE) | screener.in company page, plain GET with regex; NSE and BSE quote APIs as backup | `C:\ConcallPipeline\Daily Concall Intelligence\refresh_prices.py` (`screener_search`, `screener_page`); the batch snapshot is `concall-pipeline/Q2 FY27 Results/_CMP_snapshot_2026-10-28.md` |
| Trendlyne | MCP registered globally (`~/.claude.json`); used by shallow screens and earlier daily reviews, replaced by screener.in for prices; not used by /run-quarterly | tools `mcp__trendlyne__*` |
| Phase-1 corpus (annual reports, old concalls, presentations, Excel) | screener.in logged in, Playwright | `tools/collector/collect_to_repo.py` (runs on the operator's desktop, out of session) and `screener_collect.py`; `fetch_ratings.py` for credit ratings (no login) |
| Notion thesis, Decision Status, monitoring checklist (read at setup) | Notion MCP `notion-search`, `notion-fetch` against COMPANIES MASTER | inline in the orchestrator (command section 0f); saved as `work/notion_context_*.md` and `work/notion_checklist_*.md` |

## PART 2. YESTERDAY'S LIST

### 6. Companies reviewed in the 27-Oct and 28-Oct daily runs

There was no /run-quarterly run on 27-Oct-2026 (`git log --all --since=2026-10-26` shows only chartink data and shallow-screen commits that day). The 28-Oct batch started 28-Oct 09:10 IST and closed 29-Oct. The daily watchlist deep review (not /run-quarterly) ran for the windows 26-Oct 20:17 to 28-Oct 05:55 and 28-Oct 05:55 to 29-Oct 05:00; both REVIEW.md files are under `review/`.

Batch record: `runs/_batch-q2fy27-1028.md` (branch `run/quarterly-q2fy27-2026-10-28`, head `7b4f4162`). Source documents: `C:\ConcallPipeline\Daily Concall Intelligence\Q2 FY27 Results\` folders `20 Netweb Technologies` to `35 Route Mobile`. Operator briefs for the 15 closed names: `concall-pipeline/Q2 FY27 Results/_Operator_Briefs_Q2FY27_2026-10-28.md`. Notion page ids are COMPANIES MASTER pages (data source `345bb2b9-d3ab-8032-9b46-000ba16ab827`). The same table is `yesterday_list.csv`.

| # | Company | Ticker | Run folder | Branch | Commit | A5 verdict | Notion save |
|---|---|---|---|---|---|---|---|
| 1 | Netweb Technologies | NETWEB | runs/netweb-q2fy27 | claude/qr-netweb-q2fy27-a60c5c | 86dec775 | COMPLETE; PROCEED WITH FLAGS; cash INDETERMINATE (adverse) | WRITTEN 29-Oct, page 353bb2b9-d3ab-8114-8b87-c619f5507cb6 |
| 2 | Aequs | AEQUS | runs/aequs-q2fy27 | claude/qr-aequs-q2fy27-f2613d | 28fb68fe | COMPLETE; PROCEED WITH FLAGS; falsification line fired | WRITTEN 29-Oct, page 3d7bb2b9-d3ab-81df-ae18-d9af81e6e477 |
| 3 | Paramount Communications | PARACABLES | runs/paracables-q2fy27 | claude/qr-paracables-q2fy27-a220cd | 210c281e | INCOMPLETE on one ledger-index item (C1, no number moved); PROCEED WITH FLAGS | NOT WRITTEN, insert denied by permission classifier; page 345bb2b9-d3ab-808f-9f1d-e0960dc67726; payload ready |
| 4 | Sona BLW | SONACOMS | runs/sonacoms-q2fy27 | claude/qr-sonacoms-q2fy27-c7173c | c0295da5 | COMPLETE; PROCEED WITH FLAGS | WRITTEN 29-Oct, page 36dbb2b9-d3ab-81cf-879a-c0b005eaa4ae |
| 5 | WeWork India | WEWORK | runs/wework-q2fy27 | claude/qr-wework-q2fy27-97d635 | 2d470b12 | COMPLETE; PROCEED WITH FLAGS | NO PAGE; nothing written; create-row payload pending |
| 6 | IndiaMART | INDIAMART | runs/indiamart-q2fy27 | claude/qr-indiamart-q2fy27-acb6b5 | f2ada840 | COMPLETE; PROCEED WITH FLAGS; enquiry exit rule #6 fired | NOT WRITTEN (payload only); page 345bb2b9-d3ab-80fd-a1db-cd98e3968666 |
| 7 | Syngene | SYNGENE | runs/syngene-q2fy27 | claude/qr-syngene-q2fy27-f49780 | 65ba58de | COMPLETE; PROCEED WITH FLAGS; T3 and T4 fired; no call transcript | NOT WRITTEN (payload only); page 3e9bb2b9-d3ab-8168-afd5-ca86954e8113 |
| 8 | Raymond Realty | RAYMONDREL | runs/raymondrel-q2fy27 | claude/qr-raymondrel-q2fy27-f76d61 | 2dc7890c | COMPLETE; PROCEED WITH FLAGS; two operator rulings open | NOT WRITTEN (payload only); page 394bb2b9-d3ab-81ab-a206-e4fbc8b538a5 |
| 9 | Unimech Aerospace | UNIMECH | runs/unimech-q2fy27 | claude/qr-unimech-q2fy27-1b1895 | aeec7b5c | COMPLETE; PROCEED WITH FLAGS; no trigger fired | NOT WRITTEN (payload only); page 36fbb2b9-d3ab-814e-8a31-e6b1f305f9f9 |
| 10 | Larsen & Toubro | LT | runs/lt-q2fy27 | claude/qr-lt-q2fy27-6d55c1 | 166b5474 | INCOMPLETE on one text item (N1, no number moved); PROCEED WITH FLAGS | NO PAGE; nothing written |
| 11 | Sky Gold | SKYGOLD | runs/skygold-q2fy27 | claude/qr-skygold-q2fy27-7e1298 | 26e9a493 | COMPLETE; PROCEED WITH FLAGS; call 31-Oct not yet held | NO PAGE; nothing written |
| 12 | Knack Packaging | KNACK | runs/knack-q2fy27 | claude/qr-knack-q2fy27-0febb1 | 9d878a4d | COMPLETE; PROCEED WITH FLAGS | NO PAGE; nothing written |
| 13 | Dynamic Cables | DYCL | runs/dycl-q2fy27 | claude/qr-dycl-q2fy27-766ddd | cef66606 | INCOMPLETE on one wording item (N-01, no number moved); PROCEED WITH FLAGS | NO PAGE; nothing written |
| 14 | Puretrop Fruits | 530077 | runs/530077-q2fy27 | claude/qr-puretrop-q2fy27-888061 | 8a387599 | COMPLETE; PROCEED WITH FLAGS; results only | NO PAGE; nothing written |
| 15 | Neochem Bio Solutions | NEOCHEM | runs/neochem-q2fy27 | claude/qr-neochem-q2fy27-76041a | 44c575f8, dbcedb89 | COMPLETE; PROCEED WITH FLAGS; connector-rebuilt filing; H1 FY27 | NO PAGE; nothing written |
| 16 | Route Mobile | ROUTE | runs/route-q2fy27 (branch only) | claude/qr-route-q2fy27-fb3514 | bc9c448b (work files, PAUSED) | NOT CLOSED, see item 7 | NOT WRITTEN; page 345bb2b9-d3ab-8041-a078-fd2708a38fdf (HELD, 4% at Rs 509) |

Three names were written to Notion on 29-Oct after the operator's approval ("We can save all the reviews in Notion."): NETWEB, AEQUS, SONACOMS. Seven have no COMPANIES MASTER page and were correctly left unwritten. PARACABLES was denied by the permission classifier. INDIAMART, SYNGENE, RAYMONDREL, UNIMECH and ROUTE have pages and payloads but no write attempt on record. No Decision Status was written anywhere. No tracker rows were written.

Season to date, so nothing is repeated (all Q2 FY27, folder numbers from `Q2 FY27 Results\`):

- 17-Oct batch (branch `run/quarterly-q2fy27-2026-10-17`, record `runs/_batch-q2fy27-tokens.md` and `_batch-q2fy27-narratives.md`): Aurum Proptech, Cyient DLM, Fedbank Financial, Tata Communications, Heritage Foods, Indo Rama, Supreme Power (H1), Karnika Industries (H1), Eimco Elecon, Premier Polyfilm, G M Breweries, Poonawalla Fincorp; also Tejas Networks, Urban Company, E2E Networks and Paushak in that folder series (01-16).
- 19-Oct batch (branch `run/quarterly-q2fy27-2026-10-19`, record `runs/_batch-q2fy27-1019.md`): Kross, HFCL, Tatva Chintan, GOCL, Gallantt Ispat, Quality Power (EGM document review). All six A5 COMPLETE.
- 23-24-Oct batch (per-name branches `claude/quarterly-<name>-q2fy27-<hash>`, worktrees `.claude/worktrees/quarterly-*`, no run branch): Garware Hi-Tech, Pitti Engineering, Paisalo Digital, GHV Infra, Fairchem Organics, Tinna Rubber, Cybertech Systems, Aye Finance, Yash Highvoltage, Indosolar, Ador Welding, Tejas Networks, Supreme Power, Gallantt (call). The record for that batch is the memory file `claude-config/.claude/projects/.../memory/project-quarterly-batch-capacity.md` and the draft `concall-pipeline/Results_Season_Daily_Workflow_DRAFT.md`.
- 28-29-Oct batch: the 16 above.

### 7. Incomplete or stuck

"Bitwin" matches no company name in the repo, the ConcallPipeline folder, the Notion workspace (workspace search on 29-Oct returned nothing), or any run folder. The only name of the 28-Oct batch left open is **Route Mobile (ROUTE)**, and the two sessions that blocked the run for hours were **ROUTE and Dynamic Cables (DYCL)**. Most likely "Bitwin" is a mis-hearing of one of these; the record below covers both.

- **ROUTE (Route Mobile Ltd), NOT CLOSED.** Branch `claude/qr-route-q2fy27-fb3514`, commit `bc9c448b` (work files committed during packaging; nothing was committed by the run). Worktree `.claude/worktrees/qr-route-q2fy27-fb3514`. Documents: results (18 p), investor presentation (23 p), press release; call 28-Oct 16:30 IST, recording not posted, so filed documents only. Steps done: A1, A2, A3 on all three documents (gates passed), A4 merged review (PROCEED WITH FLAGS, cash INDETERMINATE-WITH-DIRECTION, branch 8A, 22 questions), A5 loop 0 returned INCOMPLETE (coverage FAIL: 12 signed blocks vs 6 in the ledger; 6 arithmetic mismatches, 4 FACTUAL, 3 bear counters; 8 STYLE), correction loop 1: A2 results resume done (M01-M11 rows), A4 resume done (853-line review at 08:11, 23 questions). Step it stalled at: the session did not wake when the A4 loop-1 subagent returned; after about two hours a coordinator nudge restarted it, and the operator then ruled "leave route" (29-Oct). Not run: A5 re-audit of the loop-1 review, close-out (`session-cost.md`, `operator-brief.md`, `notion-payload.md`), commit. There was no error message; the failure was coordinator and session wake latency (the orchestrator process exited before the subagent's completion notice, so A4 tokens are NOT RECORDED). Exact resume steps are in `runs/route-q2fy27/work/PAUSED.md`.
- **DYCL (Dynamic Cables Ltd), CLOSED after a stall.** The session restarted before the A5 loop-0 completion notice arrived (A5 tokens NOT RECORDED), waited about two hours, was nudged by the coordinator, then ran loop 1 with fresh agents and closed with A5 INCOMPLETE on one wording item (N-01, moves no number). Commit `cef66606`, merged. No Notion page exists.
- Batch-level stalls with no company at fault: batch-1 completion notes reached the coordinator two hours after the commits (11:24 to 13:43 on 28-Oct); the machine clock flipped zones during batch 3; faster-whisper medium.en could not finish a 10-minute chunk in 20 minutes on 756 MB free RAM (08:44 to 08:58 on 28-Oct) and was replaced by small.en.

### 8. Copies

`review/2026-10-26_2017_to_2026-10-28_0555/REVIEW.md` (591 KB) and `review/2026-10-28_0555_to_2026-10-29_0500/REVIEW.md` (686 KB), each with `INDEX.md` and `companies.json`. The full run folders of all 16 names plus `_batch-q2fy27-1028.md` are under `runs/` (229 MB; inputs, extracted text, work files, blocks, session-cost, operator brief, notion payload). The downloaded PDFs are inside each `runs/<ticker>-q2fy27/inputs/`. The call audio (mp3, 2.3 GB across the `Q2 FY27 Results` tree) is not copied; the ASR transcripts are in `inputs/`. `concall-pipeline/Q2 FY27 Results/_FILE_LISTING_2026-10-29.txt` lists every file in that tree.

## PART 3. CREDENTIALS, LOGINS AND MEMORY

### 9. screener.in

- How it is used: a Playwright Chromium browser launched by a Python script logs in with username and password at `https://www.screener.in/login/` on every run. No persistent browser profile, no cookies file, no Claude in Chrome. Scripts: `fetch_announcements.py` (the daily 05:00 watchlist feed download, dashboard `https://www.screener.in/dash/85202/`), `login.py`, `download.py`, `download_feed.py`, `download_today.py`, `download_many.py`, `download_backfill_win.py`, `tools/collector/collect_to_repo.py` and `screener_collect.py` (Phase-1 corpus, run on the operator's desktop). `refresh_prices.py` and the 28-Oct CMP snapshot read screener company pages with a plain GET, no login. Claude Code itself never logs in; when a session needed a screener page it used WebFetch on the public page or the built-in browser pane, where the operator may have been signed in (that sign-in is the operator's, not stored by the pipeline).
- Account: the email is the value of `SCREENER_EMAIL`. It is not written here. Read it from `untracked\ConcallPipeline\Daily Concall Intelligence\.env` in the zip, or from the operator's KeePassXC database. The repo copy of the same pair is `tools/collector/.env`.
- Password: `SCREENER_PASSWORD` in the same two `.env` files, loaded with `python-dotenv`. Not in any password manager export here; KeePassXC (`C:\Program Files\KeePassXC`) is the operator's manager. Not written in this document.

### 10. Other external sources

| Source | Needs | Where it lives |
|---|---|---|
| screener.in | login | `SCREENER_EMAIL`, `SCREENER_PASSWORD` in `C:\ConcallPipeline\Daily Concall Intelligence\.env` and `tools/collector/.env` |
| Trendlyne MCP | account token in the server URL | `%USERPROFILE%\.claude.json` → `mcpServers.trendlyne.url` (type http, `https://mcp.trendlyne.com/mcp/?token=...`). Redacted copy: `claude-config/claude.json.mcpServers.REDACTED.json`. Get the token from the Trendlyne account or copy the line from the old machine. |
| BSE API and attachments | none (browser-like headers only, `BSE_HEADERS` in `collect_to_repo.py`) | |
| NSE archive | none, but bot check blocks scripts | |
| Bull AI MCP | claude.ai connector, metered | enabled in the desktop app account; no local key |
| Notion MCP | claude.ai connector | enabled in the desktop app account; no local key. Allow rules for `notion-search` and `notion-fetch` are in `~/.claude/settings.json`; `notion-update-page` needs an allow rule or per-call approval |
| GitHub | `gh` login as `sumit-604` | `GITHUB_TOKEN` fine-grained PAT in the old machine's environment (not in a file); or `gh auth login` fresh. SSH remote `git@github.com:sumit-604/inflection-pipeline.git` needs an SSH key, or switch to HTTPS |
| Google Drive | Drive for desktop mounted as `G:\My Drive` on the old machine; a Google Drive claude.ai connector is also enabled | no file |
| Gmail (newsletter) | app password | `NEWSLETTER_SENDER_EMAIL`, `NEWSLETTER_GMAIL_APP_PASSWORD`, `NEWSLETTER_RECIPIENT_EMAIL` in the ConcallPipeline `.env`; used by `send_newsletter.py` only |
| Discord | webhook | `DISCORD_WEBHOOK_URL`, `DISCORD_BOT_NAME` in the ConcallPipeline `.env`; used by `post_to_discord.py` only |
| Anthropic API | not used by the pipeline (Claude Code session only); `anthropic` package installed, no key file found | |
| Google Sheets conversion in `convert_sheets.py` | optional OAuth credentials | not configured on the old machine (script skips) |

Redacted examples: `env/ConcallPipeline.env.example`, `env/collector.env.example`.

### 11. Claude Code memory and settings exported (`claude-config/`)

| Original | Copy |
|---|---|
| `~/.claude/CLAUDE.md` | does not exist on the old machine |
| `~/.claude/settings.json` | `claude-config/.claude/settings.json` |
| `~/.claude/.claude.json` | `claude-config/.claude/.claude.json` |
| `~/.claude.json` (MCP servers only, token redacted) | `claude-config/claude.json.mcpServers.REDACTED.json` |
| `~/.claude/projects/C--Users-SUMIT-SHARMA-repos-inflection-pipeline/memory/` (MEMORY.md and 10 memory files) | `claude-config/.claude/projects/C--Users-SUMIT-SHARMA-repos-inflection-pipeline/memory/` |
| `~/.claude/scheduled-tasks/{chartink-market-read,daily-watchlist-deep-review,shallow-selan-koltepatil-2026-10-26}/SKILL.md` | `claude-config/.claude/scheduled-tasks/` |
| `~/.claude/skills`, `~/.claude/commands`, `~/.claude/hooks`, `~/.claude/agents` | do not exist on the old machine; all project-level, under `repo/.claude/` |
| claude.ai account skill `notion-save` (served from the desktop app's data folder) | `claude-config/skills/notion-save/SKILL.md` and `references/schema.md` |
| ASR runner (session scratchpad) | `claude-config/scripts/transcribe_faster_whisper.py` |
| BSE helpers (session scratchpad) | `claude-config/scripts/bse_list.py`, `bse_get.py` |

`~/.claude/.credentials.json` (Claude Code login) is NOT copied; sign in on the new machine.

### 12. Operator identity and the Notion save procedure

Identity rule (from `claude-config/skills/notion-save/SKILL.md` and `CLAUDE.md`): the research is Keerti Kaushik's. The claude.ai account and this machine are shared with Sumit; Notion writes in this project are Keerti's only. Never write defence-side work. Keerti is the sole approver of every Notion write and the only person who sets or changes **Decision Status**; Claude never sets, changes or proposes it in a payload. A fired trigger is flagged in the Key Notes line and the report; the operator decides. Git commits carry the machine's git identity (`sumit-604`), which is a repo fact, not an authorship claim.

Save procedure used by /run-quarterly (command section 4; orchestrator "NOTION SAVE"; skill steps 1-7):

1. Data sources: COMPANIES MASTER `345bb2b9-d3ab-8032-9b46-000ba16ab827`; DOWNSTREAM SIGNAL TRACKER `926b65ce-ddd2-4d8b-8eae-05e66b6f6c9f`.
2. Fetch the COMPANIES MASTER schema by data_source_id first; search the company by name and ticker; use the existing page. If none exists, write nothing in a batch run (the 28-Oct instruction); a new row is an operator decision and is created inside COMPANIES MASTER only.
3. Print the exact payload (page, properties, content) and STOP for the operator's approval in that session. No approval: save `notion-payload.md` in the run folder instead.
4. Two calls per page, in order: `notion-update-page` with `update_properties`, then `notion-update-page` with `insert_content` at position `end`. The 28-Oct sessions ran them in the other order where recorded (inserts first, then the property update); the skill's order is properties first. Either way both run, nothing is overwritten.
5. Properties: Key Notes = PREPEND the new dated line to the existing pipe-delimited trail with the separator ` \| ` (read it first; verify the prior text is byte-identical after the write); Analysis Date = the save month; Current Market Price optional; Decision Status never; Position Size and Avg Cost only when Keerti states them.
6. Content: the full review (every table, the Questions-for-Management table, the PLAIN-LANGUAGE BRIEF, the forward map), the A3 findings tables and F1-F17 scorecards per document, the A5 verdict and re-audit, the operator brief. Dated heading `## Q2 FY27 quarterly review ... DD-Mon-YYYY`. Headings demoted one level inside the page body; `|` inside table cells escaped as `\|`; `~` as `\~`; `<` as `\<`.
7. Part-splitting: split large content across sequential `insert_content` calls in document order, each call one or more complete sections, never a table split across calls, confirm each call before the next (the batch used 9 to 15 inserts per page; a page body grew from 88k to 300k characters for Sona).
8. Tracker rows: proposed in section 3 of each `notion-payload.md`; none were written in the batch. Each row is one write linked to the company row with Tier, cadence, next check date, Signal Health, Falsifying Observation, verified Primary Source URL, thesis element and the operator ruling in Notes.
9. Confirm with the proof block (sections saved, properties updated, Key Notes line, tracker rows, page id, Decision Status unchanged) and record the write in `work/run-log.md` and `notion-payload.md`, then commit.

## PART 4. RUNBOOK

`RUNBOOK.md` in this folder: install commands (winget and pip), sparse clone, credential placement, config restore, how batches and subagent models are set, per-company time and token budget, the fourteen failure modes seen in October with their fixes, and the order of operations for today.
