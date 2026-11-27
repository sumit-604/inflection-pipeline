# TASK CONTEXT (orchestrator, common to every stage) — runs/rkforge-2026-11-12

COMPANY: Ramkrishna Forgings Ltd. TICKER: RKFORGE (NSE RKFORGE, BSE 532527). RUN_DATE: 2026-11-12.
Run folder (absolute): C:\Users\sumit\repos\inflection-pipeline\.claude\worktrees\step1-rkforge-ea6cc5\runs\rkforge-2026-11-12
Repo root (absolute): C:\Users\sumit\repos\inflection-pipeline\.claude\worktrees\step1-rkforge-ea6cc5

UNITS: All figures in ₹ Cr unless the source says otherwise; the source unit is on the face of the document, not in the filename.
B00.reporting_units: results filings INR lakh; annual reports INR lakh; rating rationale INR million; screener Data_Sheet INR Cr. No stage converts silently; carry the unit in every anchor.

READING THE CORPUS: every PDF under inputs/ has a page-marked .txt beside it (same name, "[page N]" markers). Read the .txt (Grep it first, then Read the page ranges you need); cite the PDF filename and page. Open the PDF page itself only where the text is garbled.
OCR CAVEAT: inputs/results/Results_Q4_FY26_Mar_2026_BoardOutcome_01May2026.pdf is a scan with an OCR text layer that misreads digits (example "3,75492.46"). For any figure taken from it, read the PDF page image, or take the audited FY26 figure from inputs/annual-report/Annual_Report_2026.pdf.

INPUT GAPS (B00.input_gaps, carry on your block):
- screening: only screener-Data_Sheet.csv is populated (INR Cr, 10 years). Profit & Loss, Quarters, Balance Sheet, Cash Flow sheets exported EMPTY and are absent.
- announcements: collector BSE fetch failed; 23 exchange filings fetched by hand from ramkrishnaforgings.com (Nov 2025 to Oct 2026, plus the 30 May 2025 board outcome). A selection, not the complete BSE feed.
- shareholding: NSE API summary and two XBRL filings saved as .txt (19 Sep 2026 and 30 Sep 2026); no PDF pattern.
- rating: India Ratings rationale of 22 Jun 2026 printed from the agency web page to PDF. CRISIL rationale not collected (only the 20 Dec 2025 intimation, in announcements/).
- research: empty. prospectus: empty, not expected (listed 2004).
- Q4 FY26 results: scan with OCR text layer, see caveat.
- annual-report/ holds two reports: Annual_Report_2026.pdf (FY2025-26, the primary) and Annual_Report_2025.pdf (FY2024-25, prior year).

COMPANY MEMORY (memory to weigh, NEVER anchored evidence; every number you report comes from this run's inputs):
- companies/RKFORGE.md and runs/rkforge-2026-11-12/step1-business-brief.md (read them if useful).
- Spear: OVERRIDE 2026-11-12 (Step-1 intake). LOAD-BEARING FACTS, check these against the filings before your own work where your stage touches them:
  1. Inventory restatement and controls: the Rs 220.5 Cr inventory overstatement found in the FY25 count, the restated FY24 and FY25 figures, the auditor's opinion and internal-control report in the FY26 annual report, any further adjustment in FY26.
  2. Guidance against delivery: net debt Rs 1,500 Cr and ROCE 12-15% by end FY27, 20% in FY28, against H1 FY27 actuals; FY27 capex guide moved from Rs 350 Cr to about Rs 550 Cr.
  3. Promoter capital and holding: the Rs 204.75 Cr warrant money (receipts, dates, the 24 Sep 2026 conversion of 34,00,000 warrants) and the cause of the fall in promoter holding from 43.39% (Jun 2026) to about 40.9% (Sep 2026).
  4. Cash conversion and concentration: inventory days, the working capital cycle, bill discounting and LC acceptances outside reported borrowings, Tata Motors share of revenue.

Write your full report to the output path and your YAML block to the block path given in your task message BEFORE you reply.
