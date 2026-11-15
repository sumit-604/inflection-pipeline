# TASK MESSAGE, COMMON PART (orchestrator to every evidence stage; not for verifiers)

This file is part of your task message. It carries the run constants. It is
not a source: nothing in it is anchored evidence.

- COMPANY: Investment & Precision Castings Ltd. TICKER: INVPRECQ. BSE code
  504786. RUN_DATE: 2026-11-15. Run type: full.
- Repo root (your working directory):
  C:\Users\sumit\repos\inflection-pipeline\.claude\worktrees\step1-invprecq-1b0ec6
- Run folder: runs/invprecq-2026-11-15 . All input paths below are relative
  to the repo root.
- UNITS: All figures in ₹ Cr unless the source says otherwise; the source unit
  is on the face of the document, not in the filename. In this corpus the
  results filings, the annual report and the presentation P&L slides report in
  ₹ lakh ("Rs in Lacs"); CARE and screener report in ₹ Cr. Carry every figure
  in its source unit with the unit in the anchor. Do not convert silently.
- READING THE CORPUS: every PDF has a page-marked text copy beside it (same
  name, .txt). Read the .txt, not the PDF. Page markers are "[page N]"; the
  scanned files (all results filings, the board-outcome announcements) were
  OCR-repaired and use "===== PAGE N =====". Anchor every number as
  (file, page N). OCR can misread a digit: where a figure looks wrong, does
  not foot, or matters to a verdict, Read that page of the PDF itself and say
  so. Use Grep to find sections in the 181-page annual report before reading;
  do not read it end to end unless your prompt requires it.
- NO-CONCALL MODE: manifest concalls_available is false. The company holds no
  earnings calls. inputs/concalls/ is empty by declaration.
- INPUT GAPS (carry into your block's input_gaps): see
  runs/invprecq-2026-11-15/outputs/blocks/B00-inputs.yaml (read it; it is
  small). It also holds reporting_units and the sector cap row
  ("Cables / Industrial products").
- Q4 FY26 results exist as two filings (20260519 and a 20260525 re-filing).
  Use inputs/results/20260525-Q4FY26-results-resubmission.txt as the Q4 FY26
  filing and name any difference you notice.
- COMPANY MEMORY (memory to weigh, never anchored evidence; every number you
  report comes from this run's inputs): companies/INVPRECQ.md and
  runs/invprecq-2026-11-15/step1-business-brief.md. Read both. The four
  LOAD-BEARING FACTS in them are this run's FIRST verification priority:
  check each one that your stage's sources can reach, against the filings,
  before your own work, and report what you found for each (confirmed,
  contradicted with the filed figure, or not reachable from your inputs).
- Corpus paths:
  - inputs/annual-report/Annual_Report_FY2025-26.txt (FY2025-26 AR, 181 pages)
  - inputs/results/20261114-Q2FY27-results.txt
  - inputs/results/20260813-Q1FY27-results.txt
  - inputs/results/20260525-Q4FY26-results-resubmission.txt
  - inputs/results/20260204-Q3FY26-results.txt (older; context only)
  - inputs/rating/20260709-CARE-rationale.txt
  - inputs/presentation/20261114-Q2FY27-investor-presentation.txt (H1 FY27)
  - inputs/presentation/20260519-Q4FY26-investor-presentation.txt
  - inputs/presentation/20251100-Q2FY26-quarterly-performance-report.txt
  - inputs/presentation/20250500-Q4FY25-investor-presentation.txt
  - inputs/screening/screener-Data_Sheet.csv (screener raw data FY17-FY26:
    P&L, quarters, balance sheet, cash flow; ₹ Cr; third-party export)
  - inputs/shareholding/20260930-shareholding-pattern-Sep2026-BSE-page.txt
  - inputs/announcements/*.txt (15 Reg 30 filings, Dec 2025 to Nov 2026)
  - inputs/peer-concalls/*.txt (AZAD, STEELCAS, ALICON; 4 transcripts each)
  - inputs/other/Annual_Report_FY2024-25.txt is preserved, not a run input.
- Paths are under runs/invprecq-2026-11-15/ . Write your report and your
  block to the exact paths your task message names. Write the block file
  before you reply.
