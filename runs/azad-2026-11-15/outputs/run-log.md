## Step F corpus collection (2026-11-15)

Collector (tools/collector/collect_to_repo.py --dry-run, headless Chromium via a scratch hook, REPO_ROOT overridden to this worktree; no tools/ file edited):
- Main AZAD: Financials.xlsx, Annual_Report_2026 and 2025, four concall transcripts (Nov 2025, Feb, May, Aug 2026), one investor presentation (Nov 2026). Staged into inputs/ and the manifest written.
- Peers PTCIL, MTARTECH, UNIMECH: all three came back with 0 files (Excel download timeout, no documents found; screener served a non-company page, rate limit). A later direct screener_collect run for PTCIL worked and returned only a Jun 2023 transcript.
- Screening: only screener-Data_Sheet.csv written (quarters to Sep 2026, P&L/BS/CF to FY26). Sheets Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization came out EMPTY (formulas, no cached values), so no CSV for them. The collector deleted _download/ itself (Financials.xlsx is not kept).
- Collector classified 13 announcement PDFs (hash-named); replaced by the descriptive set below.

Manifest: sector_cap_row set to "Cables / Industrial products"; sector_cap_row_guess kept ("Pharma / CDMO"); listed_date "2023-12-28" (confirmed in Annual Report FY25 text); collector_warnings kept as written. cmp 2456.0, market_cap_cr 15861.0.

Direct HTTP fetches (browser-like User-Agent, BSE session cookie from bseindia.com home page):
- BSE announcement list: api.bseindia.com/BseIndiaAPI/api/AnnSubCategoryGetData/w, scrip 544061, 2025-11-16 to 2026-11-15 (82 items). Attachments from www.bseindia.com/xml-data/corpfiling/AttachLive/<file>.pdf.
- results/: Q2FY27 (b503fcc5), Q1FY27 (adef773d), Q4FY26 audited (27fb26a6), all BSE.
- concalls/: Q2FY27 transcript filed 2026-11-14 (b9ebe2eb, BSE); Q1FY27 and Q4FY26 matched the collector files (same md5). Older Q3FY26 and Q2FY26 transcripts moved to other/ (contract max 3).
- presentation/: Q2FY27 (collector file, same as BSE 141ce341); Q1FY27 (BSE 999d22fd).
- announcements/: 25 material BSE filings (orders, change in management, AGM notice and outcome, BRSR, QIP monitoring agency reports, auditor change, CS change, regulatory order of 2026-03-25, ESOP allotment, press release, Q3FY26 results, analyst meet outcomes). Trading window, routine intimation, newspaper, Reg 74(5), scrutinizer, SAST and board-meeting-outcome duplicates of results skipped or removed.
- rating/: CARE Ratings press release dated 2026-06-22, https://www.careratings.com/upload/CompanyFiles/PR/202606120613_Azad_Engineering_Limited.pdf. The 2026-06-16 CARE rating letter (azad.in) kept in other/.
- prospectus/: RHP dated 2023-12-14 (https://www.angelone.in/wp-content/uploads/pdfs/Azad-Engineering-Limited-RHP.pdf, the SEBI-hosted RHP PDF was corrupt) and Prospectus dated 2023-12-23 (https://www.sebi.gov.in/sebi_data/attachdocs/dec-2023/1703848312741.pdf). DRHP 2023-09-29 (https://www.azad.in/wp-content/uploads/2023/10/DRHP.pdf) in other/. QIP placement document not collected (not pursued).
- shareholding/: Sep 2026 pattern from NSE API corporate-share-holdings-master (XBRL https://nsearchives.nseindia.in/corporate/xbrl/SHP_1737385_14102026110317_WEB.xml, broadcast 2026-10-14) plus a plain-text rendering of the same facts. Promoter 55.84%, no pledge.
- peer-concalls/: MTARTECH 4 (2026-02-05, 05-20, 08-06, 11-06) and UNIMECH 4 (2026-05-04, 06-03, 08-08, 10-31) from BSE (scrips 543270, 544322); PTCIL 1 (2023-06-09, from screener, stale).

Chrome browser fallback: none used.

Remaining gaps:
- PTCIL peer concalls: company does not file transcripts on BSE/NSE; ptcil.com holds only the Jun 2023 meet transcript; screener lists only that one. Tried BSE, NSE, ptcil.com, screener.
- Screening sheets P&L/Quarters/BS/CF/Customization empty (Data_Sheet carries the same data).
- QIP placement document not collected.
- research/: empty by design.

Verification: all 56 PDFs have %PDF header, open in pypdf with text; identity check on first pages passed; exact duplicates removed (board-outcome copies of results, one change-in-management copy).

OCR: tools/extract_pdfs.py wrote a page-marked .txt beside every PDF (56 OK); tools/check_extraction.py reported clean. No file needed OCR; none unreadable.

Units: Q2FY27 results and AR FY26 financial statements are printed in INR million.

## Orchestrator notes (2026-11-15)
- Checkout guard passed against origin/main b4ec38ce. Run branch run/azad-2026-11-15 cut from origin/main in the session worktree.
- Steps B, C, D ran on an Opus 5.5 subagent with live web; Step F on a Sonnet 5.5 subagent (operator batch instruction).
- manifest.company corrected from "Azad" to "Azad Engineering Ltd" (collector scraped a short name).
- Verifier A shadow: NOT RUN here. Nine /step1 sessions run in parallel today and the single shadow run belongs to the TD Power session. .claude/shadow.yaml is left untouched by this run.
- inputs/annual-report/ holds two ARs (FY2025-26 and FY2024-25; collector two-most-recent rule). Stages read FY2025-26 as the AR; FY2024-25 is passed as a prior-year reference only.
