# B00 — Input Validation (Stage 0)

**Company:** Millworks Technologies Limited (MILLWORKS)
**Run date:** 2026-08-22 | **Run type:** full | **CMP:** ₹828 | **Mkt cap:** ₹1,458 cr
**CIN:** U29200KA2021PLC153863 (incorporated Karnataka 2021)
**Listing:** SME IPO, RHP dated 07-Jul-2026 (fresh issue up to 48,44,000 shares, Chapter IX SEBI ICDR). Recently listed — RECENTLY-LISTED PRIORITY applies.

## Manifest
Parsed OK. `concalls_available: false` → NO-CONCALL MODE. `sector_cap_row: "Pharma / CDMO"` is WRONG (collect_to_repo v3 defect): business is high-precision / critical components for Defence, Railways, Semiconductors, Aerospace. Peers are Sika Interplant, Airfloa Rail, Apsis Aero, Unimech Aerospace. Sector row treated UNRESOLVED, flagged for phase-3 confirmation.

## Inventory (by subfolder)
| Folder | Count | Note |
|---|---|---|
| prospectus | 0 | EMPTY — but RHP is misfiled in annual-report/ (see below). Prospectus treated PRESENT via that file. |
| annual-report | 1 | RHP_Millworks-07.07.2026.pdf (365pp). This is the IPO prospectus, NOT an annual report. No standalone AR exists. |
| results | 0 | EMPTY. Gate 0 runs from screener CSVs + RHP restated audited financials FY22–FY26. |
| rating | 0 | EMPTY. Phase-3 Pillar-2 defaults conservative; rating_wc_quote unresolved. |
| concalls | 0 | Declared absent (concalls_available:false). NO-CONCALL MODE. Not a gap. |
| peer-concalls | 7 | Unimech ×4, Airfloa(544516) ×2, Apsis Aero ×1. Stage 6 runs. |
| announcements | 0 | EMPTY. Intent-and-action cross-check runs on RHP evidence only; stage 8 uses web + RHP governance. |
| shareholding | 0 | EMPTY. Post-IPO pattern not yet filed. UA institutional qualifier cannot be affirmed → UA withheld. Pre-IPO holding from RHP. |
| research | 0 | EMPTY. No effect on anchored evidence. |
| screening | 30 | MILLWORKS (`screener-*`) + 4 peers (523606 Sika, 544516 Airfloa, APSISAERO, UNIMECH). Main P&L/BS/CF/Quarters CSVs empty; only Data_Sheet populated (known defect). Restated financials taken from RHP. |
| presentation | 1 | 4-page deck. |
| other | 0 | — |

## HALT check
manifest parses; inputs/ tree not empty → PROCEED.

## Degradation posture (per DEGRADATION MAP + NO-CONCALL MODE)
- RHP substitutes for the annual report across stages 2, 3, 4, 7 (evidence-maximizing: it carries 5-yr restated audited financials, business model, promoter/group map, related-party trajectory). Stages 2/3 are NOT skipped.
- Stage 5 runs degraded (no transcripts): reads RHP business overview / MD&A-equivalent / risk factors + presentation; extracts stated intent; credibility_grade defaults C, ceiling B (just-listed, no prior guidance-vs-delivery record).
- Stage 6 runs (peer concalls present).
- Stage 7 F2 uses capex-completion / timeline evidence in place of promise-delivery.
- Stage 8 sources promoter/group background from web + RHP governance; group-company map flagged web/RHP-derived.
- Stage 9 web-search heavy, unaffected.

## Operator ruling
2026-08-22: operator answered "Proceed now" to the empty-folder confirmation. No further pause this run.

## input_gaps (carried on every downstream block)
prospectus-misfiled-in-annual-report (RHP), no-standalone-annual-report, no-results-pdf, no-rating, no-announcements, no-shareholding-pattern, no-research, main-screener-csv-empty-except-datasheet, sector_cap_row-wrong-Pharma/CDMO-UNRESOLVED, no-concall-mode.
