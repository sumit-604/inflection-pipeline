# Run log: ASTRAMICRO 2026-11-15

## Step F corpus collection

### What the collector did
- Ran `collect_to_repo.py --dry-run` through a scratch wrapper (REPO_ROOT set to this worktree; the module hard-codes a path that does not exist). `screener_collect.py` is a child process and needed no path override: it takes `--output-dir` from the parent.
- Playwright headed launch fails ("spawn UNKNOWN"). A session-local `sitecustomize.py` on PYTHONPATH forced headless, which also reached the child processes.
- Screener facts: cmp 1704.0, market cap 16174.0 Cr, name scraped as "Astramicro".
- Main company: Financials.xlsx, Annual_Report_2026 and 2025, four concall transcripts (Aug 2026, Jun 2026, Feb 2026, Nov 2025), one investor presentation (Q2 FY27).
- Peers: only DATAPATTNS delivered (4 transcripts). APOLLO and PARAS delivered nothing to the staging folder.
- BSE announcements step in the collector filed 15 documents (mostly AGM papers, duplicates of corpus files); these were discarded and the folder rebuilt (below).
- Collector warnings kept in manifest.yaml as written (shareholding empty, five screener sheets empty, no results PDFs, no rating PDF). Repairs below close the shareholding, results and rating ones.

### Repairs
- manifest.yaml: `sector_cap_row` set to "Defence / strategic"; `sector_cap_row_guess` kept as "Pharma / CDMO". The `notes` line still says sector_cap_row is empty; left as collected.
- concalls/: Nov 2025 transcript removed (three most recent kept: Q1 FY27 held 11 Aug 2026, Q4 FY26 held 27 May 2026, Q3 FY26 held 13 Feb 2026).
- announcements/: cleared and rebuilt from the BSE announcements API (two 6-month windows, 109 filings Nov 2025 to Nov 2026); 22 material filings kept (order wins, BEL MoU, demerger approvals and exchange observation letters, MD stepping down, KMP change, CRISIL intimations, monitoring agency reports, scheme board approval, AGM voting results).
- results/, presentation/ press release, rating/, shareholding/ and APOLLO peer concalls were filled by direct HTTP (below).

### Files fetched by direct HTTP (browser User-Agent, bseindia.com Referer)
- results/2026-11-12_Q2FY27_results_70cb396f.pdf: https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=70cb396f-8367-4aad-9e03-c0ff201b43a7.pdf
- results/2026-08-10_Q1FY27_results_c4386b87.pdf and results/2026-05-26_Q4FY26_audited_results_f086a834.pdf: https://www.bseindia.com/xml-data/corpfiling/AttachLive/<id>.pdf (ids from the announcements API)
- presentation/2026-11-12_Q2FY27_press_release_4b8f4126.pdf: same pattern, id 4b8f4126-2abd-4ddc-8168-0f0a1c52fbbf
- rating/CRISIL_rationale_2026-08-28.txt: https://www.crisil.com/mnt/winshare/Ratings/RatingList/RatingDocs/AstraMicrowaveProductsLimited_August%2028_%202026_RR_404820.html (no PDF link found; HTML page text saved as .txt, not a PDF)
- shareholding/BSE_shareholding_pattern_2026-09-30.txt: BSE API shpQNewFormat (scrip 532493), XBRL viewer https://www.bseindia.com/XBRLFILES/SHPXBRLDataXML/532493_9102026145239_SP.html, text extracted (filing dated 2026-10-09; no PDF exposed by the API)
- announcements/ (22 PDFs): https://www.bseindia.com/xml-data/corpfiling/AttachLive/<attachment id>.pdf, ids in each filename
- peer-concalls/APOLLO-*: Oct 2026 from https://apollo-micro.in/api/files/reports/f1151a27-3dd7-403a-82c4-7874c20b9016-earnings-call-transcript---october-26,-2026.pdf; Aug 2026, May 2026, Feb 2026 from BSE AnnPdfOpen links on the screener APOLLO documents page (Pname 79339d93..., 626429de..., cdb31d7c...)
- Q1 FY27 transcript (a3759892) matches the collector's Concall_Aug_2026 file.

### Files that came through the Chrome browser
None. No Chrome fallback was needed.

### Remaining gaps
- Q2 FY27 concall transcript (call held 13 Nov 2026): BSE has only the audio recording filing (92bb686f, 13 Nov 2026); no transcript yet. Not transcribed.
- PARAS peer concalls: screener lists no transcript links for PARAS; 90 BSE filings (scrip 543367, Nov 2025 to Nov 2026) scanned, none a transcript. Peer-concalls hold 8 files (APOLLO 4, DATAPATTNS 4).
- Screener export sheets Profit & Loss, Quarters, Balance Sheet, Cash Flow and Customization are EMPTY (row labels, no figures: formulas with no cached values). Only screener-Data_Sheet.csv is populated and holds the P&L, quarterly, balance sheet and cash flow raw rows.
- Managing Director change: the April 2026 stepping-down filings are in; no filing on a successor appointment in Oct 2026 was found in the BSE list.
- Warrant allotment / preferential issue: no allotment filing in the 12-month BSE window; only monitoring agency and deviation reports (Q4 FY26, Q2 FY27) that reference prior issue proceeds. Warrants outstanding confirmed in the Sep 2026 shareholding declaration (Q3: Yes).
- Prospectus: not expected. research/: empty (.gitkeep).

### Mechanical issues
- Hard-coded REPO_ROOT; headed Playwright launch failure; BSE API returned 403 Access Denied intermittently (needed fresh session, Accept-Language header and retries); collector deleted `_download/` at the end.
- Extraction: tools/extract_pdfs.py and tools/check_extraction.py ran clean (no flagged files, no OCR needed).

## Phase 1 run log (orchestrator)

- 2026-11-15: checkout guard passed (origin/main diff empty). Spear gate passed on the OVERRIDE line in companies/ASTRAMICRO.md.
- LESSONS pre-read done. Archetype not yet declared; matched on sector only: no tagged lessons for "Defence / strategic".
- Tooling gate: all PDFs pre-extracted to page-marked .txt at Step F; check_extraction clean. Stages and verifiers get the .txt paths.
- Execution: the Agent tool in this desktop session dispatches every subagent asynchronously and notifies on completion. The orchestrator waits for each notification and applies the completion check (report file, block file, block parses) before any dependent stage starts.
- Stage 0: intake check (Haiku 5.5) returned 43 rows, 0 unreadable, 0 unidentified, 1 proposed move (Q2 FY27 press release, presentation/ to results/). Type confirmed at page 1; not moved (reason in B00.input_gaps).
- Freshness: pair 1 FAILS (Q2 FY27 results held, Q2 FY27 transcript not yet filed). B00.freshness_verdict = CORPUS GAPPED-FRESHNESS; the gate recommendation caps at PROCEED WITH CAVEATS.
- Empty-folder confirmation suppressed per the /step1 autonomy contract; standing answer "proceed with the gaps".
- Verifier A shadow: NOT run here. Nine /step1 sessions run in parallel today and the single shadow run belongs to the TD Power session. This run leaves .claude/shadow.yaml untouched.
