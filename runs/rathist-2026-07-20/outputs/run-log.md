# Run Log — RATHIST (Rathi Steel & Power Ltd) — 2026-07-20 — PHASE 1

## Session setup
- Resolved folder: runs/rathist-2026-07-20 from arg "RATHIST".
- PDF extraction: pypdf broken (missing _cffi_backend); fixed via `pip install --force-reinstall cffi`. poppler-utils installed via apt (needed by the Read tool for PDF rendering). Both paths verified working.
- Empty-folder confirmation: AskUserQuestion tool aborted (permission stream closed). Operator then pushed documents (peer-concalls added to main, commit 1645a88), which the pipeline fast-forwarded in. Single permitted pause treated as consumed. Proceeding with remaining gaps recorded.

## Findings recorded at stage 0 (carry into all stages)
1. MANIFEST SECTOR WRONG: sector_cap_row "Pharma / CDMO" on a steel company. Correct before stage 11 (phase 3).
2. BSE CODE WRONG: manifest/collection code 513456 = KANISHK STEEL, not Rathi. Rathi's real scrip = 504903 (both results filings). Screening file 513456-* is a PEER (Kanishk); RATHIST self-data is screener-*.csv.
3. AR STALE: only FY2023 annual report present. Stages 2/3 run on FY23 AR; FY26 financials from results + screener CSVs; transition evidence from concalls + results + presentation.
4. Shareholding filing absent; operator screener snapshot saved as NON-ANCHORED lead.
5. Rating, announcements, research absent — degrade per map.
6. Concalls: 4 present; stage 5 uses 3 most recent (Nov'25 Q2FY26, Feb'26 Q3FY26, Jun'26 Q4FY26). Jun'25 (Q4FY25) excluded by cap.

## CORRECTION (stage 2 pass 1)
- The file inputs/annual-report/Annual_Report_2023.pdf is MISNAMED. Its actual content is the 54th Annual Report for FY2024-25 (year ended 31 Mar 2025), with FY24 and FY23 comparatives. So the AR is NOT stale FY23 — it is FY25. Backward baseline = FY23..FY25 (AR) + FY26 (results). Downstream AR-consuming stages (3,4,7) told the AR is FY24-25.

## Stage progress
- [x] B00 inputs — written, committed.
- [x] Stage 1 Gate 0 — running.
- [x] Stage 2 pass 1 — done (02-notes-pass1.md). Flagged: neg OCF vs +PAT, FG inv +145.9%, profit exceptional-item-driven, ₹72.91cr DTA vs stated policy, contingent liab ~21% of net worth.
- [ ] Stage 2 pass 2 — dispatched.
