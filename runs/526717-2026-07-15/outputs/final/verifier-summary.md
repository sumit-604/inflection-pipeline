# Verifier Summary (Phase 1) — HCP Plastene Bulkpack Ltd (526717)

Run date 2026-07-15. Phase-1 verifiers: A (numerical), B (concall red flags, no-concall mode), D (peer coverage), and the Gate 0 + Emerging Moat portion of C. Verifier C's valuation-adherence audit is deferred to phase 3.

## Confidence delta and acceptance rates

| Verifier | Component | Score | Acceptance rate | Findings (C/M/Mi) |
|---|---|---|---|---|
| A | Numerical acceptance | 98.7 | 98.7 | 0 / 0 / 1 |
| B | Red-flag coverage | 63 | 63 | 0 / 2 / 5 |
| C (phase-1) | Framework adherence | 96 | 96 | 0 / 1 / 2 |
| D | Peer utilisation | 75 | 75 | 0 / 4 / 0 |
| Overall | min of the four | 63 | — | Band 60-74, one-level downgrade |

No CRITICAL finding from any verifier. No acceptance rate below 60. REWORK not triggered. Framework-valuation adherence pending phase 3 (B12c scope).

Verifier caveats (from confidence.yaml):
- Verifier B could not open the 8 peer-concall PDFs via its tools; peer-side coverage is carried by Verifier D, which read all 8 transcripts in full.
- Verifier A notes one peer (COMSYN) FY26 expense detail missing from screener; MINOR, no verdict impact.
- Operator-supplied shareholding and 6m-update files are transcriptions, not original filing PDFs; verifiers A/B could not cross-check them against a source PDF (provenance-limited, noted, not treated as fabrication).

## Findings, sorted by severity

### MAJOR

| # | Verifier | Location | Finding |
|---|---|---|---|
| 1 | B | B05 Section 2A/4D vs Annual_Report.pdf p.8 | MISSED: Saudi Arabia JV MOU (Saeed Ghodran Group, 2 Jul 2024) disclosed in the same FY25 AR is untracked by B05; second abandoned international-expansion commitment, same failure mode B05 flagged for Malaysia. |
| 2 | B | B05 (whole) vs RESULTS_1.txt p.18 / p.9 | MISSED: standalone short-term loans & advances surged Rs 211.66 lakh (FY25) to Rs 4,790.00 lakh (FY26); consolidated Rs 1,482.20 to Rs 6,284.55 lakh, about Rs 45 cr out of a cash-negative, highly levered parent with heavy RPT concentration, unexplained in any filing. |
| 3 | C | 01.md Block F, M11 (Network Effects) | Conservative-fallback misapplied with 6 years present; mechanical score 3 not 1, and assigned 1 also mismatches band-1 definition. Would move moat_score 21 to 23, moat_class STRONG to FORTRESS. Conservative direction; classification (AVOID) unchanged (Core<40 and binding DB#6). |
| 4 | D | B06 Part 1, Q5 narrative (Emmbi capex quote) | Rs 7-10cr "low capex cycle" / 3,000-tonne-addition quote cited as Aug 12 2021 call p.12; actual location Nov 8 2021 call p.10. Part 3 coverage map cites it correctly, so Part 1 and Part 3 are internally inconsistent. Content genuine and correctly classified SUBSTANTIVE; only the Part 1 pointer is wrong. |
| 5 | D | B06 Part 1, Q1 net read and Q4 verdict (Bangladesh EU-import-share / EU-FTA quote) | "Bangladesh at about 12% of the EU imports" and "0% EU duty" cited as Aug 19 2025 call p.16-17; not present there. Actual source Feb 20 2026 call p.16. Also conflates UK-India FTA (Aug 2025 call p.12) with the separate EU-India FTA/duty content (only Feb 2026), presenting both as one Aug-2025 citation. |
| 6 | D | B06 Part 2 (2E), risks_peers_raise, and May 2026 coverage_map (forex hedging quote) | "Formal, weekly-reviewed forex hedging policy" cited as Kanpur Q4/FY26 (May 4 2026) call p.13 in three places; not present there. Actual source Feb 20 2026 (Q3 FY26) call p.13. Repetition across three sections indicates a systematic quarter mislabel, not an isolated slip. |
| 7 | D | B06 Part 1, Q4 verdict and Part 4 "strongest independent confirmation" (Aug 2025 margin-split quote) | "Standard product ~12% EBITDA, food-grade ~7% EBITDA" presented as settled fact, but Aug 19 2025 call p.8 ("One could be around 12%... the other could be around 7%") never states which category maps to which. Direction runs counter to the usual specialised-premium expectation; if inverted it would undercut rather than support the report's stated single strongest confirmation of HPBL's margin durability. Ambiguity resolved silently, should have been flagged. |

### MINOR

| # | Verifier | Location | Finding |
|---|---|---|---|
| 8 | B | B05 Section 2A/4D vs Annual_Report.pdf p.22 | PARTIALLY CAUGHT: B05 states one Reg 30 board-outcome delay; Secretarial Audit lists five FY25 lapses including two board-outcome delays (14 Nov 2024, 14 Feb 2025) plus delayed ROC e-forms. Instance count understated; conclusion unchanged/reinforced. |
| 9 | B | B05 05.md guidance table vs RESULTS_2.txt p.4 | MISSED (partial): maiden Rs 1/share interim dividend (paid 3 Dec 2025, about Rs 106.75 lakh) declared while standalone CFO was minus Rs 759.44 lakh and consolidated gearing 3.63x; capital-allocation tension not flagged by B05. |
| 10 | B | B05 05.md YAML excuse_pattern vs its own Section 2B | OVERSTATED: YAML tags "external-blame-heavy" while the prose finds no macro/competitor scapegoating and describes technical-minimisation/silence; label inconsistent with evidence. |
| 11 | B | Annual_Report.pdf p.5 (Chairman's Message) | Disclosure-quality error uncaught by B05: total revenue labelled "standalone basis" for both Rs 11,808.53 lakh and Rs 46,343.54 lakh; the second is the consolidated figure mislabelled. |
| 12 | B | Annual_Report.pdf p.22 (MR-3) | Disclosure-quality error uncaught by B05: Secretarial Audit Report titled FY ended 31 March 2024 while its body/audit period is FY ended 31 March 2025. |
| 13 | C | 07.md Section 5, E2 vs C2 | C2 (4.0) and E2 (1.5) both rest on the same direct-export-growth fact; em_score 12.0 sits exactly on the MODEST/NONE boundary, so any overlap discount drops the band to NONE. Decision unchanged (forward far below EXPANSION>=40; Gate 0 floors at AVOID). |
| 14 | C | 01.md Block F, M5 | Top-3/top-5 mcap thresholds applied against a 4-company peer universe; mechanically satisfied and flagged indicative-only by the maker. Data-adequacy caveat. |
| 15 | A | Stage 01, Block F (M2 peer EBITDA margin) | COMSYN FY26 EBITDA margin 12.41% cannot be independently re-derived (screener FY26 expense detail blank), but is internally consistent with the peer median used (9.51%) and produces the correct M2 score. Data limitation, not fabrication; does not affect the Gate 0 AVOID ruling (driven by deal-breaker #6). |

Verifier B additional context: all B05 red flags were independently reproducible from source (pipeline_flags_not_supported empty); promise-delivery spot-checks 5 of 5 confirmed; credibility grade C concurred, with the uncaught flags all cutting toward less credibility. Verifier D: all B06 claims addressed, no verdict-discipline fails, the four MAJORs are quote-location/attribution errors that leave the substantive conclusions intact.
