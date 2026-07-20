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
- [x] Stage 1 Gate 0 (B01): AVOID, core 24, moat THIN, FLAG-GATE0. Redeemable pref ₹8.89cr possible debt-like.
- [x] Stage 2 notes triple-pass (B02): acct quality 4/10, FLAG-CASH, 15 findings, 9 red flags.
- [x] Stage 3 AR deep dive (B03): quality 3/10, turnaround_watchlist. Flags: FLAG-CASH, FLAG-RPT-INTEGRITY, FLAG-GOVERNANCE-CHURN, FLAG-KAM-EMPTY. 15/15 stage-2 findings verified. Positives credited (promoter injection, no pledge, IC improving, clean audit).
- [x] Stage 4 bizmodel (B04): manufacturing, price-taker, cyclical, high WC. Primary val EV/EBITDA; DCF/PE/DDM/SOTP N/A. FY26 margin 4.03% down from 4.81% despite +42% rev.
- [x] Stage 5 concall (B05): credibility C; promise 3d/4p/2m; excuse external-blame-heavy; margin flat ~4%; util unreconciled; direct-charging slipped. 6 peer questions.
- [x] Stage 8 promoter (B08): FLAG-PROMOTER CONCERN. 2016 CBI coal-block conviction (Pradeep & Udit Rathi), appeal unresolved (deal-breaker). RPT-gap corroborated. Transition: family off board, lender OTS, ED complaint declined Mar26. STATUS PARTIAL (6 WebFetch 403s).
- [x] Stage 6 peers (B06): 2 docs, neither a true concall (VRAJ=CARE rationale, Scan=IP deck). Scan contradicts 'India's first hot-charging'. Peers cleaner util, bigger equity-funded capex. net effect: complicates.
- [x] Stage 7 emoat (B07): em 9.9/~80 NONE; combined AVOID. Flags: EMOAT-SPARSE, CAPEX-NIL-COMMITMENT (AR Note1 NIL vs verbal capex), F2-NEGATIVE-EXECUTION, STALE-CLAIM.
- [x] Stage 9 TAM (B09): runway GOOD, mgmt claim inflated (ratio 2.4, capacity-unsupported vs NIL committed capex). STATUS PARTIAL (paywalled).
- [x] Verifiers: A 88.2% (2 CRITICAL source-fidelity), B 85% (11/13), C 97% (gate0+EM; 2 MINOR), D 100% (2/2, 1 MAJOR VRAJ capex). All committed.
- [x] Confidence delta overall 85 (normal band). Source-fidelity gate HELD.
- [x] Synthesis-lite (B13): PROCEED WITH FLAGS. 3 files written. FLAG-CASH INDETERMINATE. All corrections applied.
- Phase 1 COMPLETE. Handoff to /fttcp.

## Additional flags surfaced (for gate recommendation)
- FLAG-RPT-INTEGRITY (B03/B08): promoter-group entities excluded from RPT note; clean CARO sign-off.
- FLAG-GOVERNANCE-CHURN (B03/B08): 5 leadership exits in ~9 months; disputed/waived BSE NRC fine.
- FLAG-KAM-EMPTY (B03): empty Key Audit Matters.
- FLAG-CASH (B02/B03): neg OCF vs +PAT; determination for gate-rec (STRUCTURAL/GROWTH-INDUCED/INDETERMINATE) to be set by synthesis-lite.
