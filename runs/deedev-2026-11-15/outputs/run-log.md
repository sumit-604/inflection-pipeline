## Step F corpus collection (2026-11-15)

Collector: tools/collector/collect_to_repo.py --dry-run via the scratchpad wrapper (REPO_ROOT overridden to this worktree, Playwright forced headless by a session-local sitecustomize hook). No file under tools/ was edited.

Mechanical problems and fixes
- First collector pass: screener returned the login/landing page ("Keep track of companies you like"), so the Excel export timed out and zero files were staged. A diagnostic login showed the login worked; the failure was transient (screener rate-limiting). Second pass succeeded for DEEDEV and ANUP. ISGEC and RATNAMANI Excel exports timed out again in that pass, but their ARs, concalls and presentations were still pulled (collector re-read the page); the data sheets for all four are present in inputs/screening.
- The first (aborted) pass left a stray background process that raced the second pass; the second pass logged a FileNotFoundError on _download/ (already moved by the first classifier). Staging completed, but ANUP peer concalls were not staged. Fix: re-ran screener_collect.py for ANUP into the scratchpad (--no-drive) and copied the 4 concalls as peer-concalls/ANUP-*.
- Collector announcements fetch took only the first 25 rows (newest), so it covered 22 Sep to 14 Nov 2026 only and included routine items. Fix: re-listed the BSE announcements API (AnnSubCategoryGetData, 2 windows of 6 months, scrip 544198; the short "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" User-Agent with Origin/Referer works, a full Chrome UA gets 403) and fetched 18 more material filings. Nothing from the collector was deleted.
- Collector sector guess "Pharma / CDMO" is wrong; manifest sector_cap_row set to "Cables / Industrial products" (Step D). sector_cap_row_guess kept as written.
- Results, rating and shareholding are not collected by the tool; fetched by direct HTTP (below).
- Tesseract OCR run on results/Results_Q4FY26_20260521.pdf (22 of 25 pages had no text layer). All 22 pages re-read, 0 still corrupt.

Files fetched by direct HTTP (curl/requests, BSE Referer)
- annual-report/Annual_Report_2026.pdf: collector copy is byte-identical in size to https://www.bseindia.com/xml-data/corpfiling/AttachHis/85a88d1b-9155-4961-86dd-7824cdd1556a.pdf (10,657,976 bytes), cover reads "Annual Report 2025-26".
- results/Results_Q2FY27_20261114.pdf: https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=0f6763ea-da21-4c04-b688-3620cdc11cb2.pdf
- results/Results_Q1FY27_20260804.pdf: BSE attachment 073e70e0-4393-417d-9297-34d017e3efdd.pdf (AttachHis)
- results/Results_Q4FY26_20260521.pdf: BSE attachment 4a06e666-a3cf-4743-817f-2a0f85e947d5.pdf (AttachHis)
- other/Results_Q3FY26_20260203.pdf: BSE attachment e812115c-fab1-4b9f-9081-ae1c975ed00a.pdf (spare)
- rating/CARE_Rationale_20261109.pdf: https://www.careratings.com/upload/CompanyFiles/PR/202611131156_DEE_Development_Engineers_Limited.pdf
- prospectus/DEE_Prospectus_June2024.pdf: SEBI page embeds https://www.sebi.gov.in/sebi_data/attachdocs/jun-2024/1719219270308.pdf (final prospectus dated 22 Jun 2024, 510 pages)
- shareholding/shareholding-30Sep2026.txt: NSE API corporate-share-holdings-master (symbol DEEDEV) gave the XBRL https://nsearchives.nseindia.in/corporate/xbrl/SHP_1739490_16102026103415_WEB.xml (quarter 30-SEP-2026, submitted 16-OCT-2026); flattened to text, source URL on line 1. No PDF was fetched.
- announcements/: 18 added by BSE attachment id: 8049f76e, 265df74e, 62648ed9, 2ba4db67, cc8a35b1, 692306e6, a1f30b26, 1beee715, 0f25c10a, 26299ab0, 01ee8562, ed295f93, bf391072, 47e7d5d0, 2c11dce8, 8bc396f6, 846a9c7a, 0c972c21 (all under https://www.bseindia.com/xml-data/corpfiling/AttachHis/<id>.pdf).
- Presentation and concalls from the collector match the BSE ids named in the brief by size (Q1 FY27 presentation 58826f6f, Q1 FY27 call d14e2ad4).

Chrome browser fallback: not used.

Moved
- annual-report/Annual_Report_2025.pdf -> other/Annual_Report_2025.pdf (older AR, FY2024-25)
- concalls/Concall_Nov_2025_Transcript.pdf -> other/ (4th transcript; only 3 most recent kept)

Gaps
- Q2 FY27 investor presentation: none on BSE as of 14 Nov 2026 (latest is Q1 FY27, filed 5 Aug 2026). Q2 FY27 call (17 Nov) transcript does not exist yet.
- screener export sheets Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization are EMPTY (formulas, no cached values) for DEEDEV, ANUP, ISGEC and RATNAMANI. Only the Data_Sheet CSV carries figures. Not repaired (needs Excel recalculation).
- other/Annual_Report_2025.pdf has a custom-font text layer (GARBLED per check_extraction); not OCR-repaired because it is outside the contract.
- announcements 20260924-45f61375 (AGM) and 87246f76 (scrutinizer report) have mostly image pages; low value, not OCR-repaired.
- Results_Q4FY26 .txt: ocr_repair writes '===== PAGE N =====' markers; rewritten to '[page N]' so check_extraction accepts it (now clean).

## Phase 1 run log (2026-11-15)

- Checkout guard: git fetch origin main OK; diff against origin/main (b4ec38ce) over .claude/ prompts/ frameworks/ CLAUDE.md LESSONS.md is empty.
- Step A: screener returned 429 on the first check (nine parallel sessions); the consolidated URL returned OK on retry.
- Steps B, C, D ran on an Opus 5.5 subagent (174,664 tokens, 481 s). Step F ran on a Sonnet 5.5 subagent (179,931 tokens, 1,392 s). These are intake rows, outside the Phase 1 stage ledger.
- Verifier A shadow: NOT run here. Nine /step1 sessions run in parallel today; the single shadow run belongs to the TD Power session (operator batch instruction). .claude/shadow.yaml not touched.
- Tooling gate: pypdf test-read of inputs/results/Results_Q2FY27_20261114.pdf page 4 OK. Text route is the default: every PDF has a page-marked .txt.
- Freshness: RESULTS to CONCALL fails (Q2 FY27 call is on 17 Nov 2026). B00.freshness_verdict CORPUS GAPPED-FRESHNESS; gate caps at PROCEED WITH CAVEATS.
- Stage 2 pass 1: report did not end with its YAML block; block file present and valid. Orchestrator appended the block to the report as an erratum (file governs). Pass 1 declared partial coverage (standalone policy text, consolidated Notes 2, 17-26, 32-37); pass 2 was told to cover those first.
- Stage 2 pass 2: same report-tail defect as pass 1; block appended as an erratum. Pass 2 corrected pass 1 on the exceptional item (Labour Codes), first-time standards and Thailand interest.
- Stage 3: report errata appended by the orchestrator (five items the stage reported but could not edit). Stray outputs/blocks/_fix_marker.txt removed. Stage 3 found no SEBI order; freshness pair 3 stays PASS.
- Stage 8: status partial, six searches skipped (sebi.gov.in entity search, MCA21, Trendlyne 405, proxy advisers, Glassdoor, tax appeal status). Verdict CAUTION. No SEBI order found; freshness pair 3 stays PASS, provisional on the skipped sebi.gov.in lookup.
- Stage 6: one report erratum appended by the orchestrator (order book is point-in-time, not H1 intake).
- Stage 7: the agent stalled (stream watchdog, no progress for 600 s) AFTER writing its full report (480 lines, closed YAML block) and BEFORE writing the block file. The orchestrator wrote outputs/blocks/B07-emoat.yaml from the report with tools/extract_block.py (run-pipeline step 3: block absent, written from the stage output). No re-invoke was needed. The failed notification carried no usage figure, so the ledger row is n/a.
- Stage 9: status partial, five searches skipped (powerpeakdigest 403, CEA Apr-Jun 2026 report, USD/INR rate, peer piping-only revenue, HRSG market size).
- Verifiers A, B, C (phase 1 scope), D dispatched once each; manifest verifier_runs set to 1 each before dispatch.
- Verifiers: all four returned complete; each report and block passed the completion check separately. Verifier A identity check: no CRITICAL rows, nothing struck. No REWORK trigger. Confidence delta overall 83.3, set by peer_utilisation.
- Source fidelity: three Verifier A MAJOR rows (source_fidelity true) corrected at source by orchestrator errata in 03-ardeep.md, 05-concall.md and 09-tam.md. Gate held, no disagreement to log.
- Verifier B acceptance: block field 88.9% used as written; the fully-caught-only reading is 44.4%. Sent to Halt 1 as an operator open item.
