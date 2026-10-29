# RUNBOOK: bare Windows machine to one successful /run-quarterly

Written 2026-10-29 from the machine that ran the 17-Oct, 19-Oct, 23-24-Oct and 28-29-Oct Q2 FY27 batches. Every command below was taken from what that machine has installed. Nothing here was tested on a fresh machine. Where a step depends on an account only the operator holds, the step says so.

Target: `C:\Users\<you>\repos\inflection-pipeline` holds the repo. `C:\ConcallPipeline\Daily Concall Intelligence` holds the download and daily-review scripts (not a git repo; restore it from this handover's `concall-pipeline/` and `untracked/` folders).

## 0. What the pipeline is, in four lines

`/run-quarterly TICKER --docs results.pdf [concall.pdf] [presentation.pdf]` is a Claude Code slash command (`.claude/commands/run-quarterly.md`). It reads `prompts/quarterly-00-orchestrator.md` and runs five subagents defined in `.claude/agents/quarterly-a1..a5-*.md`: A1 extract, A2 enumerate, A3 forensics, A4 analyst, A5 adversary. The agents call `pdftotext`, `pdfinfo`, `pdffonts`, `pdftoppm` and `tesseract` from Bash. Documents are not fetched by the command; you place the PDFs first and pass their paths. Notion is read live at setup and written only after the operator approves the printed payload.

## 1. Install the tool chain (PowerShell, as the user; admin where winget asks)

```powershell
winget install -e --id Git.Git
winget install -e --id GitHub.cli
winget install -e --id Python.Python.3.14
winget install -e --id oschwartz10612.Poppler
winget install -e --id UB-Mannheim.TesseractOCR
winget install -e --id Gyan.FFmpeg
```

Notes.
- Python 3.14 is the interpreter that holds the ASR and OCR packages on the old machine (`py -3.14`). Python 3.15 is also present there as the `python` default with a small package set. One interpreter is enough on the new machine; use 3.14 so the pinned wheels (torch, ctranslate2, pymupdf) resolve.
- Poppler installs under `%LOCALAPPDATA%\Microsoft\WinGet\Packages\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe\poppler-25.07.0\Library\bin`. Add that folder to PATH. The orchestrator checks `pdftotext`, `pdfinfo`, `pdffonts`, `pdftoppm` on PATH and stops if any is missing.
- Tesseract installs to `C:\Program Files\Tesseract-OCR\tesseract.exe` and is NOT on PATH on the old machine. The batch standing instruction tells agents to call it by full path. Either add it to PATH or keep the full-path habit.
- ffmpeg installs under `%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg_...\ffmpeg-9.0.2-full_build\bin`; the winget package adds it to PATH. Needed only for concall audio (decode to 16 kHz PCM for faster-whisper; pull audio out of an mp4).
- Node is not installed on the old machine and nothing in the pipeline needs it. Claude Code runs from the desktop app.

Python packages (one shot, the core set):

```powershell
py -3.14 -m pip install -q pypdf pdfplumber pymupdf pymupdf4llm pillow requests beautifulsoup4 lxml python-dotenv playwright pyyaml pandas openpyxl faster-whisper ctranslate2 numpy av yt-dlp
py -3.14 -m playwright install chromium
```

Full pins from the old machine: `env/requirements-python314-asr-ocr.txt` (the 3.14 environment, 190 packages including torch 2.12.1, docling, rapidocr) and `env/requirements-python315-main.txt` (the 3.15 default). `pip install -r` of the 3.14 file pulls about 3 GB (torch). Torch is not needed by any pipeline script; skip it unless docling is wanted.

Whisper model. The ASR step uses `Systran/faster-whisper-small.en` (464 MB) from the Hugging Face hub, cached under `%USERPROFILE%\.cache\huggingface\hub\models--Systran--faster-whisper-small.en`. It downloads on first use; no login needed. `medium.en` (1.5 GB) is also cached on the old machine and does NOT finish on 6 GB RAM; do not use it there. To pre-download:

```powershell
py -3.14 -c "from faster_whisper import WhisperModel; WhisperModel('small.en', device='cpu', compute_type='int8')"
```

GPU. Nothing requires one. faster-whisper runs CPU int8 (one hour of call audio in about 15 to 60 minutes depending on RAM and the model). Tesseract and poppler are CPU. With no GPU, keep one transcription at a time and run it before the review batch, not beside it.

## 2. Clone the repo (sparse; the full tree is 4.9 GB under runs/ plus 3.8 GB of .git)

```powershell
gh auth login
cd $HOME\repos
git clone --filter=blob:none --no-checkout git@github.com:sumit-604/inflection-pipeline.git
cd inflection-pipeline
git sparse-checkout init
git sparse-checkout set --no-cone '/*' '!/runs/*/*' '/runs/_template/**' '/runs/*/session-cost.md' '/runs/*/manifest.yaml'
git checkout main
```

If `gh auth login` uses HTTPS, change the remote to `https://github.com/sumit-604/inflection-pipeline.git` or add the SSH key. The old machine's gh is logged in as `sumit-604` via a `GITHUB_TOKEN` fine-grained PAT (the token itself lives in the old machine's environment, not in any file here).

`tools/sparse_session.sh runs/<folder>` adds one run folder to the sparse set when a session needs it. Quarterly runs live on run branches, not on main:

| Batch | Branch | Worktree on the old machine |
|---|---|---|
| 17-Oct (10 names) | run/quarterly-q2fy27-2026-10-17 | .claude/worktrees/q2fy27 |
| 19-Oct (6 names) | run/quarterly-q2fy27-2026-10-19 | .claude/worktrees/q2fy27-1019 |
| 23-24-Oct (14 names) | claude/quarterly-<name>-q2fy27-<hash>, one per name, never merged into a run branch | .claude/worktrees/quarterly-* |
| 28-29-Oct (16 names) | run/quarterly-q2fy27-2026-10-28 (15 merged) plus claude/qr-<name>-q2fy27-<hash> | .claude/worktrees/q2fy27-1028 and qr-* |

For today's run, branch off main (`git checkout -b run/quarterly-q2fy27-2026-10-30 origin/main`), or continue `run/quarterly-q2fy27-2026-10-28` if the operator wants one branch for the week. The command's checkout guard compares `.claude/ prompts/ frameworks/ CLAUDE.md LESSONS.md` against `origin/main` and stops on any difference, so the branch must carry no framework edits.

## 3. Restore the ConcallPipeline folder and credentials

1. Copy `concall-pipeline/` from this handover to `C:\ConcallPipeline\Daily Concall Intelligence\` (scripts, `review_spec\`, the `Q2 FY27 Results\_*.md` ledgers).
2. Copy `untracked\ConcallPipeline\Daily Concall Intelligence\.env` (zip only; it holds the screener.in login, the Gmail app password for the newsletter and the Discord webhook) to the same folder. Copy `untracked\inflection-pipeline\tools\collector\.env` to `repos\inflection-pipeline\tools\collector\.env`. Both files are gitignored on the repo side; never commit them.
3. If the zip is not to hand, create `.env` from `env/ConcallPipeline.env.example` and `env/collector.env.example` and fill the values from the operator's password manager (KeePassXC is installed on the old machine at `C:\Program Files\KeePassXC`; the screener.in entry is the operator's).
4. Trendlyne MCP: the old machine registers it in `%USERPROFILE%\.claude.json` as a global `mcpServers` entry of type `http` with the token in the URL. The redacted shape is in `claude-config/claude.json.mcpServers.REDACTED.json`. Get the token from the Trendlyne account page (or copy the entry from the old machine) and add it with `claude mcp add --transport http trendlyne "<url with token>"` or by editing `~/.claude.json`. Nothing in /run-quarterly needs Trendlyne; the daily review uses screener.in for prices.
5. Notion, Bull AI, Google Drive, Gmail, Calendar: these are claude.ai connectors enabled in the desktop app account, not local MCP servers. They need no file. Confirm in the app that Notion and Bull AI show as connected before starting. The Notion write tool needs an allow rule; see section 6 failure mode 7.

## 4. Restore Claude Code config and memory

Copy from `claude-config/`:

| From | To |
|---|---|
| `.claude/settings.json` | `%USERPROFILE%\.claude\settings.json` (auto mode default; allow rules for notion-search, notion-fetch, trendlyne, python; the additional directory `C:\ConcallPipeline\Daily Concall Intelligence`) |
| `.claude/projects/C--Users-SUMIT-SHARMA-repos-inflection-pipeline/memory/*` | `%USERPROFILE%\.claude\projects\<slug of the new repo path>\memory\` where the slug is the absolute repo path with `:\` and `\` replaced by `-` (on the old machine: `C--Users-SUMIT-SHARMA-repos-inflection-pipeline`) |
| `.claude/scheduled-tasks/*` | `%USERPROFILE%\.claude\scheduled-tasks\` (the daily-watchlist-deep-review and chartink tasks; optional for /run-quarterly) |
| `skills/notion-save/` | the claude.ai account skill; it is already attached to the account and needs no copy. Kept here as the reference text. |
| `scripts/transcribe_faster_whisper.py` | anywhere on disk; the ASR runner used for the batch |

Project-level config travels with the repo: `.claude/settings.json` (subagent cache TTL 1h, session-start hook), `.claude/settings.local.json` (allow rules), `.claude/agents/*.md` (models), `.claude/commands/*.md`, `.claude/hooks/*`. There is no `.mcp.json` and no user-level `CLAUDE.md`.

## 5. Running one company

1. Get the documents into one folder, named like the batch did: `C:\ConcallPipeline\Daily Concall Intelligence\Q2 FY27 Results\NN <Company>\<Company>_Q2FY27_Results.pdf`, `..._Investor_Presentation.pdf`, `..._Press_Release.pdf`, plus `concall_audio\<Company>_Q2FY27_Concall.mp3` when a recording exists. Sources, in the order the batch used them: the daily screener feed download (`fetch_announcements.py`, needs the screener login), the BSE announcements API and attachment URLs (`claude-config/scripts/bse_list.py` and `bse_get.py` show the exact endpoints), the company investor page, the NSE archive (often refuses with a bot check), and last the Bull AI connector (page text only, no file; label anything rebuilt from it, as the Neochem run did).
2. Transcribe the call if there is a recording and no filed transcript:

```powershell
py -3.14 "C:\path\to\transcribe_faster_whisper.py" "<folder>\concall_audio\X_Q2FY27_Concall.mp3" "<folder>\concall_audio\X_Q2FY27_Concall_Transcript_ASR.txt" small.en
```

The script chunks the audio into 600 s pieces through ffmpeg, writes one part file per chunk under `<out>.parts\`, and resumes if killed. Edit the `prompt` string at the top to the company's own vocabulary (it still carries the Fedbank list from its first use). On 6 GB RAM use `small.en`, `beam_size` 2, `cpu_threads` 6 to 8; expect 9 to 10 minutes per 10-minute chunk. Run one at a time. Mark the result ASR in `inputs/SOURCES.md`: management tier, unverified, numbers may be misheard.
3. Start a Claude Code session in the repo on the run branch. Model and effort for the session itself are fixed at start (the batch coordinator ran on Fable 5.1; company sessions ran on the default session model). Subagent models come from `.claude/agents` frontmatter and are not chosen at run time:

| Agent | Model | Effort |
|---|---|---|
| quarterly-a1-extractor | claude-sonnet-5-5 | low |
| quarterly-a2-enumerator | claude-sonnet-5-5 | medium |
| quarterly-a3-forensics | claude-opus-5-5 | high |
| quarterly-a4-analyst | claude-opus-5-5 | high |
| quarterly-a5-adversary | claude-opus-5-5 | xhigh |

The brief for this handover says "Opus 5.5 medium". No agent file says medium. CLAUDE.md DISPATCH says quarterly A5 runs Opus 5.5 xhigh, A3-A4 Opus 5.5 high, A2 Sonnet medium, A1 Sonnet low. Changing effort means editing the agent file on a framework branch and opening a PR; a session never overrides it.
4. Run:

```
/run-quarterly NETWEB --docs "C:\...\Netweb_Q2FY27_Results.pdf" "C:\...\Netweb_Q2FY27_Investor_Presentation.pdf" "C:\...\Netweb_Q2FY27_Press_Release.pdf" "C:\...\concall_audio\Netweb_Q2FY27_Concall_Transcript_ASR.txt"
```

Before it, paste the standing instructions block from `runs/_batch-q2fy27-1028.md` (section "Standing instructions for every company session") into the session. They set the run folder name `runs/<ticker lowercase>-q2fy27/`, SOURCES.md, the one-loop cap, the 30-minute stall check, the Notion write gate, and the close-out order (session-cost.md, operator-brief.md, notion-payload.md, commit).
5. Batches. The 28-Oct coordinator started at most four company sessions at a time with `start_session` and `use_worktree: true`, each on its own `claude/qr-<ticker>-q2fy27-<hash>` branch, and merged each into the run branch when it committed. On a 6 GB machine four is the ceiling and three is safer when a transcription is also running. Start the next session only when one finishes; restart a failed start in place, never as a second session.
6. Time and token budget per company (28-Oct batch, measured): about 1 h 45 min wall clock; 1.7M to 3.8M subagent tokens for a full run with results, deck, press release and call (A1 50k-160k per document, A2 45k-110k, A3 75k-210k, A4 300k-440k, A5 270k-330k, one correction loop 0.1M-1.1M); about 0.8M for a results-only light name (Puretrop 827k). A day of 16 names cost about 40M subagent tokens.
7. Close-out per company: `session-cost.md`, `operator-brief.md` (10-12 plain points, FY27E and FY28E revenue and PAT with basis and tier, forward PE at the CMP from `_CMP_snapshot_<date>.md`), `notion-payload.md`, then `git add runs/<ticker>-q2fy27 && git commit -q -m "quarterly review: <TICKER> q2fy27"`, report the hash and `git log -1 --stat`.
8. Notion save: only after the operator approves the printed payload in that session. Two calls per page: `notion-update-page` with `update_properties` (Key Notes prepended with ` \| `, Analysis Date, optionally Current Market Price; never Decision Status), then `notion-update-page` with `insert_content` at `end`, split into sequential complete-section chunks (the batch used 9 to 15 inserts per page; never split a table). If the company has no COMPANIES MASTER page, create none; leave the create-row payload for the operator.

## 6. Known failure modes and fixes (all seen in October 2026)

1. Scan with no text layer (Netweb results, Tatva results). A1's text-layer gate fails; render with `pdftoppm -r 200 -png` and OCR with `"C:\Program Files\Tesseract-OCR\tesseract.exe" page.png out --psm 6`, or run `tools/ocr_repair.py <pdf> <out.txt>`. Check `pdftotext` output against the page image before trusting a statement page; several filings had garbled hidden text layers (Unimech pages 4-16 were transcribed from 130 dpi renders).
2. Coordinator wake latency. Completion notes reached the coordinator up to two hours after the company session committed (batch 1 on 28-Oct; DYCL and ROUTE on 29-Oct never woke when a subagent returned until nudged). Fix: judge progress by the newest file time under `runs/<ticker>/work/`, not by session notes; send the session a one-line check message after 30 minutes of no new file.
3. Machine clock zone flip. The old machine's clock jumped zones mid-batch (16:08 read as 02:46), so file ages across sessions were not comparable. Compare a session's newest file against sibling sessions, not against wall clock.
4. Background subagents die silently on a network drop (23-Oct, four sessions waited for hours). Run subagents in the foreground.
5. faster-whisper medium.en stalls on 6 GB RAM; stale runner shells re-spawn jobs after the python child is killed. Use small.en; kill the runner's shell process tree, not just python.
6. Too many sessions at once (14 on 23-Oct): eight never started, retries created duplicate sessions and duplicate work. Four at a time; restart a failed start in place.
7. Notion write denied. On 29-Oct the PARACABLES session's first `insert_content` was refused by the permission classifier (External System Writes) and nothing was written. Fix: add `mcp__622a4e63-d69a-4dec-90da-0c58637236c0__notion-update-page` to the allow list in `.claude/settings.local.json` (the server id prefix is the Notion connector's id on the old machine; check `claude mcp list` for the id on the new one), or run the save in claude.ai from `notion-payload.md`.
8. No Notion page for the company (WeWork, L&T, Sky Gold, Knack, Dynamic Cables, Puretrop, Neochem). The sessions correctly wrote nothing. The operator decides whether to open coverage; `notion-payload.md` holds the create-row payload.
9. NSE archive bot check refuses the PDF (Neochem). Read the filing through the Bull AI connector, rebuild a text PDF, label it rebuilt on page 1 and in SOURCES.md, and mark every number "pending NSE original".
10. Recording link garbled by text extraction (Paramount, Sona: a hyphen dropped). Read the link from the PDF annotation (`pymupdf` `page.get_links()`), not from the extracted text.
11. Late filings after the evening fetch (Cybertech deck at 17:18 IST on 23-Oct). Check the BSE announcements page for the company once more before A4 starts.
12. `index.lock` on commit when sessions share a worktree. Wait 30 s and retry. Never `git stash` or `git reset --hard` (the stash stack is shared across worktrees).
13. A5 INCOMPLETE on a wording item that moves no number (Paramount C1, L&T N1, DYCL N-01). One loop only; a second loop is allowed only for a FACTUAL or CONTRADICTION item that moves a verdict-card number. Carry the item as open for the operator.
14. Session run out of context mid A4/A5 (orchestrator exited before the completion notice: ROUTE, DYCL). Token counts for that step are NOT RECORDED in session-cost.md; the files on disk are the record. Resume with a fresh agent given only the gap lines (Knack lesson: resumes re-read the whole context).

## 7. Order of operations for today, in one list

1. Install (section 1), clone (section 2), restore ConcallPipeline and `.env` files (section 3), restore `~/.claude/settings.json` and memory (section 4).
2. Confirm Notion and Bull AI connectors are connected in the desktop app. `gh auth status`. `pdftotext -v`, `pdfinfo -v`, `tesseract --version` (full path), `ffmpeg -version`, `py -3.14 -c "import faster_whisper, fitz"`.
3. Read `HANDOVER.md` Part 2 so no name from 17-Oct to 29-Oct is run again. ROUTE is the only open one.
4. Download today's documents into `Q2 FY27 Results\NN <Company>\`. Refresh CMPs into a new `_CMP_snapshot_<date>.md` (screener.in company pages; `refresh_prices.py --names "A,B,C"` does it for a list).
5. Transcribe calls one at a time.
6. Branch, paste the standing instructions, run `/run-quarterly` per name, four sessions at most.
7. Collect operator briefs into one `_Operator_Briefs_Q2FY27_<date>.md`; print payloads; write to Notion only on the operator's approval.
8. Commit each run folder, merge into the run branch, push, and end the day with the batch record (`runs/_batch-q2fy27-<date>.md`) and `LESSONS_ARCHIVE.md` entry.
