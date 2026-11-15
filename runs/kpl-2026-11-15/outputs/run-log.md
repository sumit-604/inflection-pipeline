# Run log: kpl-2026-11-15

## Step F corpus collection

Collector: collect_to_repo.py --dry-run (headless Playwright shim, REPO_ROOT pointed at this worktree). Exit 0, no 429s hit.
It staged into runs/kpl-2026-11-16 (calendar date); moved to runs/kpl-2026-11-15, 11-16 folder deleted, run_date set to 2026-11-15.

### What the collector did / where it failed
- Downloaded: Financials.xlsx (Data_Sheet CSV only; P&L, Quarters, Balance Sheet, Cash Flow, Customization sheets are EMPTY formula sheets, no CSV written, for KPL and all 3 peers), AR FY25 + FY26, 2 KPL transcripts (Aug 2026 duplicate deduped), 1 presentation (Q2 FY27), peer transcripts (9), 16 BSE announcements.
- Failed: CAPLIPOINT May 2026 transcript (connection reset). No results, rating or shareholding source in the collector. BSE announcement fetch capped at 25 rows (only Aug-Nov 2026 covered).
- Collector set concalls_available false (only 2 transcripts); repaired to true per instruction.

### Repairs to manifest.yaml
- run_date 2026-11-15; sector_cap_row "Pharma / CDMO"; concalls_available true.
- Added remediation_cycles: 0 and verifier_runs {A:0,B:0,C:0,D:0}.
- manifest parses (yaml.safe_load). cmp 3823.0, market_cap_cr 3966.0 (non-zero; Data_Sheet price 3822.6, mcap 3966.41 agree). Main URL was the consolidated variant.
- collector_warnings still in the manifest are the collector's original text and are partly stale: shareholding/ now has the BSE summary; results/ and rating/ now filled; concall warning superseded.

### Files obtained by direct HTTP (BSE API + AttachLive/AttachHis, browser UA, Referer bseindia.com)
- Own BSE announcement listing (12 months, two 6-month windows, 77 rows) to find filings.
- results/: Q1 FY27 (20260810-a801ea43), Q4 FY26 audited (20260519-3ba529f9). Q2 FY27 came from the collector's announcements (board outcome + financial results with limited review report, 24 pp), moved to results/.
- rating/: ICRA rationale dated 7 May 2026 (BBB+ Stable / A2), taken from the 9-page BSE rating intimation 20260508-1ab08dfa (cover letter + full rationale).
- presentation/: Q4 FY26 (20260519-2dd8e61b), Q1 FY27 (copy of 20260810-28ad8c7c); Q2 FY27 already from collector.
- announcements/ added: 20260508 credit rating, 20260310 BE programme phase 1, 20260602 director resignation (and CoM), 20260724 Reg 30 disclosure, 20260202 and 20260204 change in management/cessation of directors.
- shareholding/: BSE API shpSecSummery_New, Sep 2026 summary (txt + raw html). Promoter 54.86%, public 45.14%, no pledge, 17,880 holders. Public sub-breakdown (FII/DII) NOT in this file.
- peer-concalls/: CAPLIPOINT Q4 FY26 (14 May 2026) from the company website link (caplinpoint.net) named in the BSE cover letter.

### Files via Chrome browser
- None. Not needed: every file found came by direct HTTP. Chrome screener Documents fallback not used because the only missing KPL file (Q2 FY27 transcript) is confirmed unpublished (see gaps).

### Removed / moved
- Duplicates (identical md5) removed from announcements/: 20261112-7e5f2326 (auditor appointment, same PDF as outcome), 20261112-efb35788 (financial results, same PDF), 20261112-c41a6b24 (Q2 presentation, same as presentation/Investor_Presentation_1.pdf), 20261114-a1050258 (duplicate recording intimation), 20260602-5bfccb8f (duplicate director resignation), 20260810-28ad8c7c (moved copy to presentation/).
- 20261112-49e6260f moved from announcements/ to results/ as the Q2 FY27 results. 20261112-4a20fb35 (identical file, filed as auditor resignation) stays in announcements/.
- A one-page CAPLIPOINT cover letter was overwritten by the real linked transcript.
- No files from other companies found. Peer files checked by first page.

### Extraction
- extract_pdfs.py: all PDFs have page-marked .txt. check_extraction.py: clean. No OCR needed, no unreadable PDF.

### Remaining gaps
- KPL Q2 FY27 transcript (call 13 Nov 2026): not published. Company site shows audio recording only (uploaded 14 Nov); no BSE transcript filing as of 16 Nov. Reg 30 allows 5 working days. Re-run later.
- KPL Q3 FY26 (Feb 2026) transcript: none exists (investor meet audio/video only). Concalls folder holds 2 transcripts (Q4 FY26, Q1 FY27).
- Rating: no newer rating than ICRA May 2026 found on BSE.
- Screening: P&L, Quarters, Balance Sheet, Cash Flow, Customization CSVs EMPTY for KPL and peers (Data_Sheet carries FY17-FY26 annuals and quarters to Sep 2026).
- Shareholding: no FII/DII public-category breakdown; no full pattern PDF.
- Company secretary resignation: not found. Nov 14 2026 filing is still signed by the Company Secretary (Gurpreet Kaur). Statutory auditor resignation (Vijay Mehra & Co, 12 Nov 2026) is in the Q2 outcome filing; new auditor appointment text is in the same 24-page PDF.
- Peers: no Q2 FY27 call for CAPLIPOINT (not yet published); LINCOLN has nothing after Feb 2026 on BSE (May 2024 file is stale); only 2 LINCOLN files. Peer total 10 of 12.
- prospectus, research: empty (not expected).

### collector_warnings (as in manifest)
See manifest.yaml; five entries (shareholding empty, screener sheets empty, no results, no rating, only 2 concalls). Superseded in part as noted above.

## Orchestrator notes (session)

- 2026-11-15: checkout guard passed against origin/main b4ec38ce. Identity: KPL, https://www.screener.in/company/KPL/consolidated/ (check_url OK 200). Steps B, C, D ran on an Opus 5.5 subagent with live web (134,250 tokens, 31 tool uses, 473 s).
- 2026-11-15: a task-list tool call (update_plan) was declined in this session with an instruction to stop and wait for the operator. The run paused before Step F. No corpus subagent had been dispatched. This was a pause, not a stream stall.
- 2026-11-16: the operator typed "Continue" in this session. The declined call was not retried in its old form; the task list was rewritten. Step F then ran on a Sonnet 5.5 subagent (147,234 tokens, 34 tool uses, 576 s).
- 2026-11-16: the collector named its folder kpl-2026-11-16 from the clock date. The contents were moved to runs/kpl-2026-11-15 and run_date kept at 2026-11-15, per the batch brief.
- manifest.yaml company corrected by hand from "Kpl" to "Kwality Pharmaceuticals Ltd" (collector name scrape defect).
- Q2 FY27 transcript check by the orchestrator: the screener concall row for Nov 2026 carries PPT and REC links only, no Transcript link. The gap is real. Chrome fallback not used: no file exists to download.
- Verifier A shadow: NOT run here. Nine /step1 sessions run in parallel and the single shadow run belongs to the TD Power session. .claude/shadow.yaml is left untouched by this run.
- LESSONS pre-read done (active LESSONS.md). Open actions noted; none blocks Phase 1. No tagged lessons for sector "Pharma / CDMO"; no archetype declared yet.
- Stage 0: B00-intake (Haiku 5.5) found no misfile and no UNIDENTIFIED row in 43 files; nothing to verify at the page, no moves. B00-inputs written inline. Units: results and AR in INR lakhs, screener in INR Cr.
- Freshness pair 1 FAILS (Q2 FY27 results present, Q2 FY27 transcript not published). B00.freshness_verdict = CORPUS GAPPED-FRESHNESS; the gate recommendation caps at PROCEED WITH CAVEATS.
- Empty-folder confirmation suppressed per /step1; proceeding with gaps.
- Harness note: the Agent tool dispatches every subagent in the background in this desktop session. The orchestrator waits for each completion notice and then applies the PROVE COMPLETION check (report and block on disk) before any dependent stage starts.
- annual-report/ holds two ARs. Stages use FY2025-26 as the AR; FY2024-25 is passed as a prior-year reference only.
