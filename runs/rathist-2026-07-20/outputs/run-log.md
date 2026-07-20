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

## Stage progress
- [x] B00 inputs — written, committed.
