# Run log: GVPIL 2026-11-15

## Step F corpus collection

### Collector (screener.in, dry-run, via wrapper with headless hook)
- Attempt 1: screener served a non-company page for GVPIL and BHEL ("Keep track of companies you like"; Excel timeout, no ARs, no concalls). Peers POWERMECH and ISGEC worked. Cause unknown (rate limit or session). Attempt 2 (full rerun, same day) worked for all four names.
- Delivered: annual-report 2 (FY25, FY26), concalls 4, presentation 1, screening 4 Data_Sheet CSVs, peer-concalls 12 (BHEL 4, ISGEC 4, POWERMECH 4), announcements 11 (BSE API, collector).
- Not delivered by collector: results, rating, shareholding. BSE announcement hits also incomplete.

### Repairs
- manifest.yaml: company "Gvpil" -> "GE Power India Limited"; sector_cap_row set to "EPC / Civil construction" (exact row exists in .claude/skills/section-1b/references/05-sector-cap.md, 20x); removed the sector_cap_row_guess line. collector_warnings left as written (now partly stale: results, rating, shareholding are filled). The `notes` line still says sector_cap_row is empty; stale.
- Collector concalls folder held 2 July 2026 files. They are investor meets (6 and 10 Jul 2026), not earnings calls; moved to other/.

### Fetched by direct HTTP (BSE, browser User-Agent, Referer bseindia.com)
- BSE announcements API (python requests, 12-month window 2025-11-16 to 2026-11-15, scrip 532309): 86 filings listed.
- PDFs from https://www.bseindia.com/xml-data/corpfiling/AttachLive|AttachHis/<id>.pdf:
  - annual-report/Annual_Report_2026.pdf = 64bd32ae-7855-46fe-8bf5-11460ebf1228 (same bytes as the collector copy)
  - results/Results_Q2FY27_30Sep2026.pdf = 1390fa26-4fac-47ad-9441-c6f7e9bcabdd
  - results/Results_Q1FY27_30Jun2026.pdf = 2eb9438f-b761-43ed-ab53-f4a26c224326
  - results/Results_Q4FY26_31Mar2026_audited.pdf = c1a5bbba-ea8e-46f9-8ed4-4ca90765311d
  - concalls/Concall_Nov_2025_Q2FY26_Transcript.pdf = ab7f2b22-dbb0-4f7d-bbd2-64aa44525288 (Q2 FY26 call, 14 Nov 2025)
  - presentation/Investor_Presentation_Q4FY26_2026-05-11.pdf = 5a7930a2-57b6-45cd-bdba-9bca56ce7f35
  - presentation/Investor_Presentation_1.pdf (collector) = d3409c0f-548a-4f54-8f5f-42ad910ce28f (investor meet deck, 3 Jul 2026)
  - 39 further Reg 30 filings added to announcements/ (date-prefixed, BSE attachment id): Durgapur scheme / NCLT meeting notices (Apr-Jul 2026, 1 Oct 2026 order), order receipt 12 Aug and 8 Sep 2026, CFO/CS/director/management changes, ICRA intimation, Q3 FY26 results.
- rating/ICRA_Rationale_2026-03-03.pdf: https://www.icra.in/Rating/ShowRationalReportFilePdfViewer/141387 (ICRA upgrade to [ICRA]BBB+ Stable / A2, 3 Mar 2026; full rationale, 7 pages).

### Fetched through Chrome
- shareholding/Shareholding_Pattern_screener_Sep2026.csv: transcribed from the screener.in shareholding table (Dec 2023 to Sep 2026). It is NOT the filed BSE pattern PDF.
- BHEL announcement list read in Chrome on bseindia.com (the Python API was returning 403) to look for transcripts. None found.
- No file downloaded through the Chrome download mechanism.

### Removed duplicates (identical bytes of files kept elsewhere)
Removed from announcements/: Nov 2025 and Feb/May 2026 transcripts, Q4/Q1/Q2 results copies, Q4 board outcome copy (32bb6f74), two 3 Jul presentation copies, two Jul transcript copies, two AR copies, 3661c5f2 (same bytes as Q2 FY27 results), and 3 duplicate-in-folder notices (d637c05d, 83cf2cf2, f4c1b6f8 kept once under their twin). No junk or wrong-company files were found.

### Remaining gaps
- No Q2 FY27 earnings call transcript (call scheduled 16 Nov 2026; Nov 6 BSE intimation). Expected.
- No Q1 FY27 (Aug 2026) earnings call: BSE shows none for GVPIL; only investor meets 6 and 10 Jul 2026 (in other/).
- No Q2 FY27 investor presentation on BSE yet (latest decks: 3 Jul 2026 meet, 11 May 2026 Q4).
- BHEL peer transcripts are stale (latest May 2024, Q4 FY24); BHEL has posted no transcripts on BSE in the last 12 months.
- Filed BSE shareholding pattern PDF (Sep 2026) not obtained; screener-derived table only. No pledge detail.
- Screener export: only Data_Sheet CSV per company is populated; the 5 other sheets (P&L, Quarters, BS, CF, Customization) are empty in every export. The Data_Sheet itself holds annual P&L, quarters to Sep 2026, balance sheet and cash flow.
- FGD contract terminations (Jaypee Bina / Nigrie): no matching BSE filing found in the 12-month list.

## Phase 1 orchestration (2026-11-15)

- Checkout guard: `git fetch origin main` ok; framework diff against origin/main empty.
- Identity: screener symbol GVPIL (GEPIL returns 404), URL https://www.screener.in/company/GVPIL/consolidated/ OK on tools/check_url.py after 429 retries. Legal name GE Power India Limited, BSE 532309.
- Steps B, C, D ran on an Opus 5.5 subagent with live web (operator batch instruction). Step F ran on a Sonnet 5.5 subagent.
- Sector cap row: "EPC / Civil construction" (20x), section-1b chunk 05 line 48. The brief names "Cables / Industrial products" (25x) as the other reading.
- Tooling gate: all PDFs pre-extracted to page-marked .txt (tools/extract_pdfs.py). tools/check_extraction.py flags one file GARBLED: inputs/announcements/20261115-f68052f4-...pdf. Its page 1 is a readable company cover letter; the garbled pages are a vernacular newspaper notice of the results. Not OCR-repaired; named as unreadable beyond page 1.
- Stages and verifiers receive .txt paths.
- Reporting units: results and AR in INR million; screener Data Sheet in INR crore.
- Verifier A shadow: NOT RUN here. Nine /step1 sessions run in parallel today; the single shadow run belongs to the TD Power session (operator batch instruction). .claude/shadow.yaml is left untouched in this worktree.
- Empty-folder confirmation: suppressed per /step1 autonomy contract; standing answer "proceed with the gaps".
- Agent dispatch: this harness launches subagents asynchronously. Each stage is treated as done only after its report and block files pass the completion check.
- Stages 4, 5 and 8 (first dispatch, 2026-11-15 evening): all three subagents failed with "Agent stalled: no progress for 600s (stream watchdog did not recover)". No report or block file was on disk. Mechanical failure (API error / timeout class, orchestrator Section 7). Re-invoked once each on 2026-11-16 01:57 IST with the same task messages. Not counted against any cap. Token use of the stalled runs is not exposed.
