# Verifier Summary — HCP Plastene Bulkpack Ltd (526717)

Run date 2026-07-15. All four verifiers plus the phase-3 valuation-adherence audit. Phase 1 covered A (numerical), B (concall red flags, no-concall mode), D (peer coverage), and the Gate 0 + Emerging Moat portion of C. Phase 3 added C's deferred valuation-adherence and Role 2 decision-rule audit (B12c-valuation). Findings sorted CRITICAL first, then MAJOR, then MINOR. Notes are the verifiers' own; no added commentary.

## CONFIDENCE DELTA AND ACCEPTANCE RATES

| Component | Verifier | Score | Acceptance rate | CRITICAL / MAJOR / MINOR |
|---|---|---|---|---|
| Numerical | A (B12a) | 98.7 | 98.7% | 0 / 0 / 1 |
| Red flag coverage | B (B12b) | 63 | 63% (5 of 8 flags caught) | 0 / 2 / 5 |
| Framework adherence | C combined (B12c + B12c-valuation) | 94.5 | phase-1 96%, phase-3 93% | 0 / 1 / 5 |
| Peer utilisation | D (B12d) | 75 | 75% (6 of 8 substantive) | 0 / 4 / 0 |
| **Overall** | min of four | **63** | red flag bound | **0 CRITICAL total** |

No CRITICAL finding anywhere. No verifier acceptance rate below 60%. REWORK not triggered. Overall 63 sits in the 60 to 74 band; the binding constraint is red flag coverage.

## CRITICAL

None across all verifiers.

## MAJOR

| Verifier | Location | Finding |
|---|---|---|
| B (B12b) | B05 Sec 2A/4D vs Annual_Report.pdf p.8 | MISSED: Saudi Arabia JV MOU (2 Jul 2024) disclosed in the same AR is untracked by B05; a second abandoned international-expansion commitment, same failure mode B05 flagged for Malaysia. Stage 7 caught it independently. |
| B (B12b) | B05 (whole) vs RESULTS_1.txt p.18/p.9 | MISSED: standalone short-term loans and advances surged Rs 211.66 lakh (FY25) to Rs 4,790.00 lakh (FY26); consolidated 1,482.20 to 6,284.55 lakh, ~Rs 45 cr out of a cash-negative, highly levered parent with heavy RPT concentration, unexplained in any filing. Financial-forensics item likely owned by stage 2/3, absent from B05. |
| C phase 1 (B12c) | 01.md Block F, M11 | M11 Network Effects used the <6-year conservative fallback despite 6 years available; mechanical two-window score is 3 not the assigned 1, and 1 mismatches the band-1 definition. Would move moat_score 21 to 23, moat_class STRONG to FORTRESS. Conservative direction; classification (AVOID via Core<40 and binding DB#6) unchanged. |
| D (B12d) | B06 Part 1, Q5 (Emmbi capex quote) | Rs 7-10 cr low-capex-cycle / 3,000-tonne-addition quote cited as 12 Aug 2021 call p.12; actual location is 8 Nov 2021 call p.10. Part 3 coverage map cites it correctly, so Part 1 and Part 3 are internally inconsistent. Content genuine, correctly SUBSTANTIVE; only the Part 1 pointer is wrong. |
| D (B12d) | B06 Part 1, Q1/Q4 (Bangladesh EU-import-share / EU-FTA quote) | "Bangladesh ~12% of EU imports" and "0% EU duty" cited as 19 Aug 2025 call p.16-17; not present there. Actual source is 20 Feb 2026 call p.16. Also conflates the UK-India FTA (Aug 2025 p.12) with the separate EU-India FTA/duty content (Feb 2026) as one Aug-2025 citation. |
| D (B12d) | B06 Part 2 (2E), YAML risks_peers_raise, May 2026 coverage map (forex hedging quote) | "Formal, weekly-reviewed forex hedging policy" cited as Kanpur Q4/FY26 (4 May 2026) p.13 in three separate report locations; not present there. Actual source is 20 Feb 2026 (Q3 FY26) call p.13. Repetition across three sections indicates a systematic quarter mislabel. |
| D (B12d) | B06 Part 1 Q4 / Part 4 (Aug 2025 margin-split quote) | "Standard product ~12% EBITDA, food-grade ~7%" presented as settled fact, but the 19 Aug 2025 p.8 source ("One could be around 12%... the other could be around 7%") never states which category maps to which. B06's direction runs counter to the conventional expectation that specialised product carries the premium; if inverted, this would undercut rather than support the report's "single strongest independent confirmation" of margin durability. Ambiguity resolved silently. |

## MINOR

| Verifier | Location | Finding |
|---|---|---|
| A (B12a) | Stage 01 Block F, M2 peer EBITDA comparison | COMSYN FY26 EBITDA margin 12.41% cannot be independently re-derived (screener FY26 expense detail blank for one peer); internally consistent with the peer median used, correct M2 score. Data limitation, not fabrication. Does not affect the Gate 0 AVOID ruling. |
| B (B12b) | B05 Sec 2A/4D vs Annual_Report.pdf p.22 | PARTIALLY CAUGHT: B05 states one Reg 30 board-outcome delay; Secretarial Audit lists five FY25 lapses including two board-outcome delays (14 Nov 2024, 14 Feb 2025) plus delayed ROC e-forms. Instance count understated; conclusion reinforced. |
| B (B12b) | B05 guidance table vs RESULTS_2.txt p.4 | MISSED (partial): maiden Rs 1/share interim dividend (paid 3 Dec 2025, ~Rs 106.75 lakh) declared while standalone CFO was -759.44 lakh and consolidated gearing 3.63x; capital-allocation tension not flagged. |
| B (B12b) | B05 YAML excuse_pattern vs its own Sec 2B | OVERSTATED: YAML tags "external-blame-heavy" while the prose finds no macro/competitor scapegoating and describes technical-minimisation/silence. Label inconsistent with evidence. |
| B (B12b) | Annual_Report.pdf p.5 (Chairman's Message), uncaught by B05 | Disclosure-quality error: total revenue labelled "standalone basis" for both Rs 11,808.53 lakh and Rs 46,343.54 lakh; the second is the consolidated figure mislabelled. |
| B (B12b) | Annual_Report.pdf p.22 (MR-3), uncaught by B05 | Disclosure-quality error: Secretarial Audit Report titled FY ended 31 Mar 2024 while its body/audit period is FY ended 31 Mar 2025. |
| C phase 1 (B12c) | 07.md Section 5, E2 vs C2 | C2 (4.0) and E2 (1.5) both rest on the same direct-export-growth fact; em_score 12.0 sits on the MODEST/NONE boundary, so any overlap discount drops the band to NONE. Decision unchanged (forward far below EXPANSION >=40; Gate 0 floors at AVOID). |
| C phase 1 (B12c) | 01.md Block F, M5 | top-3/top-5 mcap thresholds applied against a 4-company peer universe; mechanically satisfied and flagged indicative-only by the maker. Data-adequacy caveat. |
| C phase 3 (B12c-valuation) | B11 11.md l.54 / Pillar 2; B10 cash_conversion_and_wc | Cash multiplier 0.80x under INDETERMINATE; the band table also supports 0.65x (Infomerics confirms persistent WC; cumulative 6yr CFO/PAT -0.888x, 5/6 yrs negative), while naive latest-year 0.70x would map 1.00-1.15x. 0.80x is the conservative midpoint faithfully carried from the authoritative FTTCP deliberation; bear correctly uses 0.65x. Verdict-invariant. |
| C phase 3 (B12c-valuation) | B11 11.md l.117-119 / EBIT-basis reconciliation | ROCE-basis inconsistency: B10 EBITDA uses results-line EBIT 39.98 but Pillar 1 ROCE 28.62% derives from EBIT ex-other-income 48.33 (8.35 cr gap). B11 correctly used the authoritative FTTCP ROCE and disclosed the ~1.9-PE-point sensitivity; under the alternate basis Track-1 Hurdle recomputes to ~1.98 (still >1.953, narrow). Which EBIT basis is right is Verifier A's domain; not a framework misapplication. Decision unchanged. |
| C phase 3 (B12c-valuation) | B14 14.md l.17 / one-line thesis | One-line frames "two hard caps" with cash INDETERMINATE "on top", while B11 and the risk matrix carry three overlapping caps (Gate0 leverage, Promoter CONCERN, INDETERMINATE cash). Cosmetic count mismatch; all three surfaced and drive AVOID. Decision-invariant. |

## PHASE-3 VALUATION-ADHERENCE AUDIT (B12c-valuation, 0 CRITICAL / 0 MAJOR / 3 MINOR)

Valuation: 33 rules checked, 30 clean plus the 3 MINORs above. All pillars PASS: Pillar 1 formula (0.5x28.62+7.5=21.8x) and ROCE selection (FTTCP FIRING to current 28.62%); Amendment 9 route NONE; Pillar 2 0.80x under INDETERMINATE, growth offset barred; Pillar 3 +0x; strategic premium +0x; single-credit respected (ROCE via Pillar 1, Strategic ROCE route BARRED); UA ordering all-three-fail so not applied; sector cap Packaging 22x absolute, not binding, no exit PE from outside Section 1B; RRM Track 1 r=16.0%, RRM 0.70, 12.2x; dual-track divergence 30%>15% so conservative Track 1 governs; Hurdle PASS (2.23 T1 / 3.18 T2 vs 1.953); entry 222, MoS 177, U/D 3.27x, prob-weighted +17.4%; SOM cross-check consistent; unresolved inputs carried NOT FOUND with no silent fills.

Role 2: 8 rules checked, 8 clean. Promoter CONCERN default to AVOID (Master l.916); Gate0 AVOID + Promoter CONCERN each trigger AVOID independently; buy-now gate correctly excluded; CMP in zone but caps live so zone WITHDRAWN and value trap called; hardest-verdict-wins (FTTCP conditional DEEP WATCH overridden by AVOID caps); Tier B barred (Promoter CONCERN); position sizing None on AVOID.

Recomputed destination PE: concur, Track 1 12.2x / Track 2 17.4x. Recomputed decision: concur, AVOID.

## VERIFIER CAVEATS

- B12b (Verifier B) could not open the 8 peer-concall PDFs individually; peer-side coverage carried by B12d, which read all 8.
- Every B05 red flag was independently reproducible from source; all SUPPORTED. The B12b MAJORs are omissions (uncaught flags), not unsupported claims.
- Operator-supplied shareholding and 6-month-update files are transcriptions, not original filing PDFs; provenance-limited, noted. Verifier A could not cross-check the SHP against a source PDF.
