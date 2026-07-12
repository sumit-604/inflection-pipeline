# STAGE 0: INPUT VALIDATION — NORTHARC (Northern Arc Capital Ltd)

Run date: 2026-07-12 | run_type: full | concalls_available: true

## Manifest
- company: Northern Arc Capital Ltd
- ticker: NORTHARC (NSE: NORTHARC, BSE: 544260, CIN L65910TN1989PLC017021)
- cmp: 325.0 | market_cap_cr: 5257.0
- sector_cap_row (as collected): "Pharma / CDMO" — **WRONG**. Northern Arc
  Capital is a diversified retail-focused NBFC (lending / financial
  services), rated [ICRA]AA- (Stable) per inputs/rating/139993.pdf. The
  auto-collector (collect_to_repo v3) mis-picked the sector row, the same
  defect logged for KARNIKA on 2026-07-11. Recorded in input_gaps and
  surfaced to phase 3: the exit-multiple authority (Section 1B v3.3) must
  select the correct NBFC / financial-services cap row, and NBFC valuation
  is book-value / P-ABV driven, not an earnings exit PE on a manufacturer.

## Inventory (by subfolder)
- **annual-report/** — 1 PDF (8180eb1f...). PRESENT.
- **results/** — 2 PDFs. PRESENT.
  - 5f083c0b... = Q4 & FY26 audited results, quarter/year ended 31-Mar-2026
    (board meeting 08-May-2026).
  - ec38f56d... = Q3 FY26 unaudited results, quarter ended 31-Dec-2025
    (board meeting 30-Jan-2026). 26.7MB.
- **rating/** — 1 PDF (139993.pdf). PRESENT. ICRA, dated 29-Dec-2025:
  [ICRA]AA- (Stable) reaffirmed on NCDs / bank facilities; [ICRA]A1+ on CP.
- **concalls/** — 4 PDFs. PRESENT. concalls_available: true → NORMAL mode.
  Contract uses the 3 most recent; Jul-2025 (Q1 FY26) is dropped.
  Quarter map (Mar FY end):
  - Concall_Jul_2025 → Q1 FY26 (qtr ended Jun-2025) — NOT USED (oldest of 4)
  - Concall_Oct_2025 → Q2 FY26 (qtr ended Sep-2025) — USED (transcript 1)
  - Concall_Jan_2026 → Q3 FY26 (qtr ended Dec-2025) — USED (transcript 2)
  - Concall_May_2026 → Q4 FY26 (qtr ended Mar-2026) — USED (transcript 3)
- **peer-concalls/** — 14 PDFs across 4 peers. PRESENT. Contract cap is 12;
  all 14 passed to stage 6 (more peer evidence favoured), count noted.
  - CGCL (Capri Global): Aug-2025, Nov-2025, Feb-2026, May-2026 (4)
  - FEDFINA (Fedbank Financial): Aug-2025, Oct-2025, Jan-2026 (3)
  - MASFIN (MAS Financial): Nov-2025, Feb-2026, Feb-2026_2 (3; two Feb-2026
    files — stage 6 to treat _2 as continuation/duplicate)
  - UGROCAP (UGRO Capital): Aug-2025, Nov-2025, Feb-2026, Apr-2026 (4)
- **screening/** — 24 CSVs. PRESENT. Company set = screener-*.csv (6 files:
  Balance_Sheet, Cash_Flow, Customization, Data_Sheet, Profit_Loss,
  Quarters). Peer sets = CGCL-*, MASFIN-*, UGROCAP-* (6 each). Note: no
  FEDFINA screening CSVs despite FEDFINA peer concalls present.
- **presentation/** — 1 PDF (Investor_Presentation_1.pdf). PRESENT.
- **other/** — ABSENT (nothing to preserve).

## Halt check
manifest.yaml parses; inputs/ tree is non-empty. No mechanical halt.
No input folder is empty or absent among the tracked types (annual-report,
results, rating, concalls, peer-concalls, screening, presentation), so the
single stage-0 empty-folder operator pause is NOT triggered.

## Company memory
companies/NORTHARC.md does not exist (no prior /finalize run). No COMPANY
MEMORY to carry. run_type is full, not refresh; no PRIOR RUN CONTEXT.

## Notes to downstream
- NBFC accounting: Gate 0 (stage 1) and the AR stages read financial-
  services line items (AUM, NIM, GNPA/NNPA, credit cost, CRAR, managed
  gearing, cost-to-income), not manufacturer ratios. B04 must flag the
  irrelevant_ratios (inventory days, gross block turns, etc.).
- Stage 11 (phase 3): correct the sector_cap_row to the financial-services
  / NBFC row before selecting any exit multiple.
