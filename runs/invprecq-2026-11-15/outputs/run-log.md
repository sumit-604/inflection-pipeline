# Run log: invprecq-2026-11-15

## Step F corpus collection 2026-11-15

### Collector (collect_to_repo.py via scratch wrapper, --dry-run)
- Wrapper set REPO_ROOT to this worktree; sitecustomize.py forced Playwright headless (headed launch fails with spawn UNKNOWN). No 429 seen on the main company.
- Delivered for INVPRECQ: Financials.xlsx (only Data_Sheet CSV written; P&L, Quarters, Balance Sheet, Cash Flow, Customization sheets came out empty), Annual Report FY26 and FY25 (BSE links), Investor_Presentation_1 (which is the Q4 FY26 deck), 8 BSE announcements (collector cap).
- Peers in the collector run: STEELCAS delivered 4 concalls. AZAD returned nothing (Excel timeout, no ARs or concalls) and ALICON was empty, probably screener throttling from sibling sessions.
- Manifest edits: sector_cap_row set to "Cables / Industrial products" (guess left as "Pharma / CDMO"); concalls_available false; remediation_cycles 0; verifier_runs {A:0,B:0,C:0,D:0}; cmp 1322.0 and market_cap_cr 1322.0 as the collector wrote them (non-zero); repair_note added.

### Repairs
- Peer retry: screener_collect.py rerun for AZAD and ALICON alone with 40 s gap; both delivered 4 concalls each (Nov 2025, Feb, May, Aug 2026). Files copied into peer-concalls/ with a ticker prefix. Peer ARs and presentations not staged (pipeline needs only concalls).
- Annual reports: the collector staged FY25 and FY26 as Annual_Report_2025/2026. Page-1 and period text checked: 2026 = year ended 31 Mar 2026. FY26 AR kept in annual-report/ as Annual_Report_FY2025-26.pdf; FY25 AR moved to other/.
- Exact duplicates removed: Investor_Presentation_1.pdf (identical to the Q4 FY26 deck), the Q2 results copy in announcements (moved to results/ and presentation/), the FY26 AR copy in announcements.

### Direct HTTP downloads (python requests / curl, BSE headers; BSE announcement API worked with python requests, AttachLive then AttachHis)
BSE base: https://www.bseindia.com/xml-data/corpfiling/AttachLive/ or AttachHis/ + guid.pdf. The listing came from api.bseindia.com AnnSubCategoryGetData (scrip 504786, 12 months).
- results/20261114-Q2FY27-results.pdf: edb7271a-0840-4eb4-8660-354b9ee1562e (AttachLive)
- results/20260813-Q1FY27-results.pdf: 897903e6-b4ae-4ce8-844e-d12b84c98f59 (AttachHis)
- results/20260519-Q4FY26-results.pdf: 38f8e104-2360-4eb7-a05b-fdd5ff56bceb; 20260525 resubmission: ec7dae3e-0fb3-41f7-becd-3204738f4f55; Q3 FY26: e761c1a4-8d20-49bc-be2f-135642537485
- presentation/20261114-Q2FY27: a55429ce-ebb2-4aed-818c-6b301676754a; 20260519 Q4 FY26: ab84027c-1ac0-49ac-9681-3e27c9d7402f; other/: a75cdd22-b722-4ea8-b60b-bc70055b247d (Q2 FY26), 9dd1d11c-49c5-486f-9f49-ac8c8e2a2f25 (older)
- rating/20260709-CARE-rationale.pdf: https://www.careratings.com/upload/CompanyFiles/PR/202607130735_Investment_&_Precision_Castings_Limited.pdf (7 pp full rationale); rating/20260710-credit-rating-intimation.pdf is the BSE Reg 30 filing (4f4eec05-2841-4b17-ae18-a9819e684672), carrying the same text.
- announcements: 16 further guids (awards and orders, Reg 30 updates, solar commissioning, board outcomes Q3 FY26, Q4 FY26, Q1 FY27, price-movement clarification).

### Chrome browser fallback
- Shareholding Sep 2026: no PDF exists and the BSE API/pages were blocked or JS-only for scripts. Opened BSE shareholding pattern pages in a new Chrome tab (summary, promoter, public) and saved the page text to shareholding/20260930-shareholding-pattern-Sep2026-BSE-page.txt. Tabs closed afterwards. No downloads, no sign-in.

### Extraction and OCR
- tools/extract_pdfs.py run on the whole folder. check_extraction.py flagged 8 files as mostly blank (scanned): Q2 FY27, Q1 FY27, Q4 FY26 (both), Q3 FY26 results, and three board-outcome announcements.
- tools/ocr_repair.py (Tesseract 5.4, 200 dpi) repaired all 8 (still_corrupt = 0 each). Repaired files use "===== PAGE N =====" headers, so check_extraction reports "no [page N] markers" for them; that is a format mismatch in the tools, not a defect. The ocrcache dirs were removed. Log: outputs/ocr_run.log.

### Remaining gaps
- No FY26 AR gap. No Q1 FY27 investor presentation was filed on BSE in the 12-month listing (none found).
- Screening: only Data_Sheet populated (P&L and Balance Sheet, FY17 to FY26). Quarters, Cash Flow, Customization empty (formulas without cached values). Not attempted via Chrome download.
- Shareholding is a text capture, not the XBRL filing PDF. Historical shareholding trend not collected.
- Concalls: none by design (company holds none).
- PTC Industries peer not collected (not in companies.txt).

## Phase 1 run log 2026-11-15
- Checkout guard: PASS (origin/main b4ec38ce). Spear gate: PASS (OVERRIDE line).
- Verifier A shadow: NOT RUN here. Nine /step1 sessions run in parallel today; the single shadow run belongs to the TD Power session. .claude/shadow.yaml not touched.
- Stage 0: intake check complete (40 files). Three folder_match false rows verified at the page: two older decks moved from other/ to presentation/; FY2024-25 AR kept in other/ (one-AR contract).
- Tooling: whole run on pre-extracted .txt. Stages run as harness subagents; completion is proven on disk (report + block) before any dependent stage starts.
- Ledger: the harness gives total tokens and wall time only; split columns are n/a.
- OCR repair 2 (orchestrator): stage 1 reported Q2 FY27 results pages 3, 4, 7 illegible. Cause: results tables are rotated 90 degrees in the scans. A scratch script (PyMuPDF render at 300 dpi, Tesseract psm 6, rotations 0/90/270, best score kept) re-read the low-score pages of all five results filings and the Q3 FY26, Q4 FY26 and Q2 FY27 board outcomes. Rotated pages now read as rows; column headers are lost and the rupee sign reads as 2. task-common.md tells every later stage. No tools/ file edited.
- ERRATUM, stage 1 (01-gate0.md): the report says Q2 FY27 results pages 3, 4 and 7 are OCR-illegible and takes no figure from them. Those pages were repaired after stage 1 ran. Stage 1 was not re-run (not a mechanical failure; its scores rest on screener and AR data). Later stages read the repaired pages.
- ERRATUM, stage 2 (02-notes-pass1.md, 02-notes-pass2.md, 02-notes.md, B02-notes.yaml): AR page anchors are one page too high (marker read as page end; the marker precedes the page). Note numbers and values verified 15 of 15 by stage 3. Correction table: 03-ardeep.md Phase 2. Stage 2 not re-run; task-common.md carries the convention to later stages.
- Stages 4 and 5 run 1: both subagents stalled (harness: no progress for 600s, stream watchdog did not recover). No report or block on disk. Mechanical failure; re-invoked once each (run 2).
- Stage 5 (run 2): the analyst_note inside the report embedded YAML is an older wording than the block file. The block file B05-concall.yaml governs.
- Verifiers A, B, C (Gate 0 + EM scope), D: all four reports and blocks on disk; completion check passed for each. verifier_runs set to 1 each in manifest.yaml before dispatch. Shadow not run.
- Confidence delta: numerical 98, redflag 71, framework 89.5 (phase-1 scope), peers 100; overall 71, set by redflag_coverage. No REWORK trigger. No remediation cycle run (remediation_cycles stays 0).
- OPEN ITEM for Halt 1: B12b gives 71% (partial catches counted) and 29% (full catches only) for its own rate. The block field (71) is used. On the strict count REWORK would fire.
- Figure check (orchestrator, at source): CMD pay rise appears as +51.2% (Note 38: 347.11 against 229.54 lakh; B03, B08) and +41.10% (Board report Annexure 5 percentage; B12b). Both are printed in the AR on different bases (AR text lines 4160 and 7797). Not a FLAG-DISAGREEMENT; both carried with their basis.
- Framework note for a later PR (from B12c observations): prompts/12-verifiers-pipeline.md line 379 holds placeholder text where the rule 9 key set should be; prompts/07 Section 6D names a standard matrix it never defines; prompts/07 does not say how offset evidence scores.
- Stage 13 (phase 1 lite) complete: three outputs/final files; verdict line PROCEED WITH CAVEATS. Stage 09b complete.
- MECHANICAL DOSSIER CHECK: PASS. Six section headers in order (lines 7, 52, 112, 120, 223, 254). One corpus verdict line (line 30, CORPUS GAPPED; line 48 is an explanatory sentence that names both terms). DRAFT - PENDING OPERATOR SIGN-OFF marker present once. Section 6 answers questions 1 to 10 in order and ends with the corpus commit hash line 8574d70aa0e6b7ebaf9d7a8c5e6f292f1006da08.
- Stage 09b report does not end with its YAML block (the stage could not append without a rewrite). The block is in outputs/blocks/B09b-dossier.yaml, which governs. The orchestrator did not append it, because Section 6 must end with the hash line.
- Hash note: the dossier hash 8574d70a is HEAD before stage 09b ran and contains the corpus. The corpus commit itself is df88990a; the OCR repair of scanned tables is c353f91e.
