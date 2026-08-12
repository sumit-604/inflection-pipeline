# Verifier summary — JITFINFRA phase 1

## Confidence delta and acceptance rates

| Component | Verifier | Score / acceptance | CRITICAL | MAJOR | MINOR |
|---|---|---|---|---|---|
| numerical_acceptance | A (B12a) | 69 | 0 | 4 | 4 |
| redflag_coverage | B (B12b) | 83 | 0 | 1 | 3 |
| framework_adherence (Gate0 + Emerging Moat only) | C (B12c) | 99 | 0 | 0 | 3 |
| peer_utilisation | D (B12d) | 100 | 0 | 0 | 3 |
| overall (min) | | 69 | | | |

Band 60 to 74. Framework adherence is the phase-1 portion only (Gate 0 plus Emerging Moat, 80 of 81 rules clean); the valuation half is deferred to phase 3. Zero CRITICAL across all four verifiers. The REWORK gate did not trigger.

Verifier D note: the first B12d run raised a CRITICAL "fabrication" finding on the false premise that the peer transcripts were absent from inputs. The orchestrator confirmed all 16 peer concall PDFs are present and readable, and Verifier B independently read them, so the first run was a tooling failure. It is superseded by the valid re-run below, which accepts at 100 percent.

## Findings sorted by severity

No CRITICAL findings.

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| A | B01 Block D1, Net Debt/EBITDA | Claimed 6.71x post-exceptional; standard pre-exceptional value 6.19x (EBITDA Rs 604.43 Cr, FY26 Results P&L audited). Both breach 3x; AVOID unchanged. Source-fidelity. |
| A | B01 Block D2, Interest Coverage | Claimed 1.14x post-exceptional; pre-exceptional 1.251x (EBIT Rs 501.89 Cr). Both fail; AVOID unchanged. Source-fidelity. |
| A | B01 Block D, Current Ratio | Claimed 1.47x is ANCHOR NOT FOUND; correct audited 1.345x (Rs 2,740.28 Cr CA / Rs 2,037.72 Cr CL, FY26 Results CBS). Source-fidelity. |
| A | B01 Block A, Median ROCE | 5.34 percent unverifiable; FY17-FY24 rests on non audited screener data. FY26 audited 15.25 percent versus screener 13.31 percent. Data-quality gap. |
| B | B05 Section 2D / 4D | Trade-receivables surge and cash-conversion risk absent from B05 "what they are not saying"; consol receivables up 52 percent to Rs 1,271 Cr vs 24 percent revenue, Rs 434 Cr CF drain. Captured instead by B02 receivables_trend and B03 FLAG-CASH. |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| A | B01 Block C, Revenue CAGR | 20.03 percent FY17-FY26 verified; both endpoints anchored. Clean. |
| A | B01 Block D, Net Debt | Rs 3,745.06 Cr verified against audited CBS. Clean. |
| A | B01 Block D, Finance Costs | Rs 401.29 Cr = Rs 40,128.90 lakh, exact match to audited P&L. Clean. |
| A | B01 Block D, Consolidated Net Worth (owners) | Rs (51,327.81) lakh verified; negative equity fact confirmed. Clean. |
| B | B05 Section 4D (ESOP row) | Q4 loss Rs 783.80 lakh stated "larger than" full-year loss Rs 993.47 lakh; comparative inverted (783.80 < 993.47). ESOP point stands. |
| B | B05 Sections 2C/4D/1C | "Going-concern qualification" label imprecise; opinion unmodified, para 3 material uncertainty, para 4 emphasis of matter. Flag validity intact. |
| B | B05 Section 2D/4D vs FY26 P&L | Interest-coverage burden under-weighted; group finance costs about 66 percent of EBITDA. Partially caught. |
| C | B01 Block A / ROCE formula | Proxy capital-employed denominator used in place of rulebook formula; validated within 0.4pp on FY26 audited data. No band or classification impact. |
| C | B01 M5 Scale & Dominance | Scored 0; literal band could give 1 (JITF 5th of 5 named comps). Conservative direction; cannot change "not present" status or classification. |
| C | B07 G1 War chest | LL=1 retained though "net cash growing" definition unmet; rests on documented rating upgrade and cost-of-debt fall. Zeroing yields em_score 16.7, still MODEST. |
| D | B06 Part 1 Q7 (WABAG Nov 2025) | CBG-from-sludge quote over-attributed to both Nov 2025 and Feb 2026 calls; exact phrase only in Feb 2026. Underlying live CBG project corroborated in both quarters. |
| D | B06 Part 1 Q5 (AWHCL Feb 2026) | 22-23 percent margin correctly sourced but mislabeled segment-specific; it is AWHCL's company-wide blended EBITDA guidance. |
| D | B06 Part 1 Q7 (AWHCL Q4 FY26) | Call labeled May 2026; transcript dated June 1, 2026. Quarter and figures correct; only calendar-month label off. |

## Source-fidelity disagreement note

Three Verifier A findings carry source_fidelity: true (Net Debt/EBITDA, Interest Coverage, Current Ratio). All three are MAJOR, none flips the verdict. Synthesis carries the corrected or audited figures with anchors per the gate; Verifier C's clean re-derivation of AVOID is subordinate to Verifier A on the existence-of-a-number question and does not clear these. GATE HELD, figures corrected in the gate recommendation.
