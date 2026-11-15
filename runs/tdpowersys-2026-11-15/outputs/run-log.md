# Run log: tdpowersys-2026-11-15

## Step F corpus collection (2026-11-15)

### What the collector delivered
- Ran `collect_to_repo.py --dry-run` through a scratch wrapper (REPO_ROOT set to this worktree) with a session-local `sitecustomize.py` forcing headless Chromium.
- Main company TDPOWERSYS (screener): Financials.xlsx, 2 annual reports (FY2025-26, FY2024-25), 4 concall transcripts (Nov 2025, Feb 2026, May 2026, Aug 2026), 1 investor presentation (it was the Q2 FY27 deck of 12 Nov 2026).
- BSE announcements (scrip 533553): 17 PDFs (first 25 rows of the 12-month window).
- Peers CGPOWER, TRITURBINE, AZAD: ZERO files. The Playwright pass on each peer page timed out on the Excel download and read the screener landing page ("Keep track of companies you like"), so no documents were found. Re-running one peer alone gave the same result.
- Screening: only `screener-Data_Sheet.csv` (populated, annual to FY26, quarters to Sep 2026). The Profit & Loss, Quarters, Balance Sheet, Cash Flow and Customization sheets of Financials.xlsx came out EMPTY (formulas without cached values), so no CSV exists for them. These are gaps for B00. Data_Sheet carries P&L, Quarters, Balance Sheet and Cash Flow blocks, so the figures exist; the per-sheet CSVs do not.
- manifest.yaml: cmp 638.0, market_cap_cr 20494.0, sector_cap_row empty, collector_warnings listed 4 items (shareholding empty, empty screener sheets, no results PDFs, no rating PDF).

### Repairs made
- `manifest.yaml`: `sector_cap_row` set to "Cables / Industrial products". The `sector_cap_row_guess: "Pharma / CDMO"` line (keyword guess) and `notes` line were left as the collector wrote them.
- `annual-report/`: FY2025-26 AR kept (renamed `TDPOWERSYS_Annual_Report_FY2025-26.pdf`, 267 pp). FY2024-25 AR moved to `other/Annual_Report_FY2024-25_older.pdf`.
- `concalls/`: kept the three newest (Q3 FY26 4 Feb 2026, Q4 FY26 19 May 2026, Q1 FY27 18 Aug 2026), renamed with order prefix 1_, 2_, 3_. The Nov 2025 transcript moved to `other/`.
- `results/`: built from BSE filings already staged in announcements/ (copies): Q2 FY27 (12 Nov 2026), Q1 FY27 (11 Aug 2026), Q4 FY26 (14 May 2026). These are the board-outcome filings with the financial results attached.
- `presentation/`: collector file verified byte-identical to the BSE Q2 FY27 deck (5a12caf6...), renamed.
- `peer-concalls/`: 12 transcripts downloaded (see below), renamed with ticker, date and quarter.
- `rating/`: CRISIL rationale (8 pp PDF) rendered from the HTML rationale by headless Chromium. The HTML source moved to `other/`.
- `shareholding/`: Sep 2026 (Reg 31(1)(b)) and the 12 Oct 2026 capital-restructuring (post-QIP) pattern from the company website. The Jun 2026 pattern (image-only PDF, 17 pp) moved to `other/`; it is not OCR'd.
- `announcements/`: 49 additional Reg 30 / SAST / corporate action PDFs added from the BSE feed. A duplicate undated SAST copy removed.
- `research/` and `prospectus/` have `.gitkeep`. Folders `outputs/blocks`, `outputs/reports`, `outputs/final` created.
- Extraction: `tools/extract_pdfs.py` ran on all PDFs. `tools/check_extraction.py` flagged two scanned or garbled announcement PDFs; both were OCR'd with `tools/ocr_repair.py` (Tesseract) and their page markers set to `[page N]`. The SAST Reg 29(1) of 14 Nov 2026 was an image-only scan. Remaining flag: `other/TDPOWERSYS_shareholding_pattern_2026-06_Q1_image.txt` (blank, not a pipeline input, not repaired).

### Direct downloads (no Chrome needed; the screener-in-Chrome fallback was not used)
- BSE announcement list: `https://api.bseindia.com/BseIndiaAPI/api/AnnSubCategoryGetData/w` (Python requests, BSE headers, 12-month window 2025-11-16 to 2026-11-15, 103 rows). The `AnnGetData` endpoint and curl calls returned 403 Access Denied.
- BSE files: `https://www.bseindia.com/xml-data/corpfiling/AttachHis/<id>.pdf` (fallback AttachLive). Key ids: AR FY26 424c4c46-8b6d-4689-8ab9-68f43e6bdeaf, Q2 deck 5a12caf6-cf27-425c-8a63-9300311df871, Q2 results 8b36c4d5-a0ef-4932-970f-ad6a96b9f8ba, Q1 results 01bb706d-5ff6-4831-8682-0aaf4037fc45, Q4 results 9c37dcd3-9a21-48e9-b18c-aaa87ea3d138, Q1 FY27 transcript a93b0ca0-28ed-460d-bf0f-eab665db635c, credit rating letter c0aa1490-4509-41c3-a2f0-95c5fa78a730.
- CRISIL rationale: `https://www.crisil.com/mnt/winshare/Ratings/RatingList/RatingDocs/TDPowerSystemsLimited_June%2022_%202026_RR_392766.html` (the `.pdf` variant returns HTML).
- Shareholding: `https://www.tdps.co.in/_files/ugd/6c2f9d_bab809d3cebf4a89b6d1d128eb9b3130.pdf` (Sep 2026), `.../6c2f9d_8ca79c5c55a34d61923a75bbd9ad8cd8.pdf` (12 Oct 2026), `.../6c2f9d_8f87bf90dd474d419716b68b1219ff94.pdf` (Jun 2026, to other/).
- Peer transcripts: links read from the public screener company pages (documents section). CG Power: cgglobal.com uploads (IIFL-CGPower-Jul24-2026, May06-2026_v2, Jan27-2026, iiflcap-cgpower-oct29-2025). Triveni Turbine and Azad: BSE `AnnPdfOpen.aspx?Pname=` ids 06048a54, 7eb58552, c3ee1092, e284c057 (Triveni) and c595c5f6, 521d7519, 27924b98, fcb4082e (Azad). Each first page was read to confirm company and date.

### Remaining gaps
- **Q2 FY27 earnings call transcript (call held 13 Nov 2026): NOT AVAILABLE.** BSE announcements to 15 Nov 2026 hold the outcome (13 Nov) but no transcript. The screener documents list shows only the audio recording (wixstatic mp3). The company website shows no transcript. Last year's lag was 5-6 days (Q1 FY27 call 12 Aug, transcript filed 18 Aug), so the transcript is likely to be filed about 19 Nov 2026. The results-to-concall freshness pair fails today: Q2 FY27 results and deck against a Q1 FY27 transcript. Re-check BSE after 19 Nov and add as `concalls/4_...`.
- Peer Q2 FY27 transcripts for TRITURBINE and AZAD not yet filed (screener lists audio only); CGPOWER latest is Q1 FY27 (24 Jul 2026), Q2 call not yet held or listed.
- Screening: per-sheet CSVs for Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization are EMPTY (formulas with no cached values). Only Data_Sheet is populated. Peer Excel files were not collected (collector peer pass failed), so there are no peer screening CSVs.
- Peer annual reports and presentations were not collected (not required by the folder spec).
- BSE announcements API blocked curl and one endpoint (403); Python requests on AnnSubCategoryGetData worked.
- The CRISIL rationale is a Chromium print of the HTML page; the original CRISIL PDF could not be fetched.
- Newspaper-publication and trading-window announcements were skipped by design.
