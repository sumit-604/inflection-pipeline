# Verifier summary: VOEPL (2026-07-18), phase 3

## Confidence delta

| Component | Score |
|---|---|
| Numerical acceptance | 98.8 |
| Redflag coverage | 67 |
| Framework adherence | 96.3 |
| Peer utilisation | 94 |
| Valuation adherence | 95 |
| OVERALL | 67 (band 60-74, bound by redflag coverage) |

REWORK not forced: Verifier A 0 CRITICAL, minimum acceptance 67 clears 60, and the one framework MAJOR is non-decision-determinative (STOP/AVOID invariant).

## Acceptance rates

| Verifier | Scope | Acceptance | C / MAJ / MIN |
|---|---|---|---|
| A (B12a, haiku) | Numbers, 160 figures across B01-B09 | 98.8 | 0 / 0 / 2 |
| B (B12b, opus) | Red flags and credibility | 67 | 0 / 0 / 6 |
| C (B12c, opus) | Framework and valuation adherence | 99 gate0/em, 95 valuation | 0 / 1 / 3 |
| D (B12d, sonnet) | Peer triangulation, 16 peers | 100 | 0 / 0 / 1 |

Concurrences: Verifier C CONCURS AVOID (on valuation) and Hurdle STOP. Verifier B concurs credibility grade B. Verifier D reports clean verdict discipline. Verifier A confirms all three deal-breaker figures clean (ND/EBITDA 4.00x, interest coverage 1.73x, debt/equity 0.84) and zero fabrication.

## Findings, sorted by severity

### CRITICAL

None across all four verifiers.

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| C | B11 Pillar 1, Section 1B lines 53-70 | Worksheet selected Recon v3.5.1 Route B as governing but applied the retired Amendment 4.5 three-anchor blend (40% norm + 30% FY[Y+2] + 30% current = 21.72%). Governing Route B specifies 60/40 current/anchor = 20.58%. Overstates ROCE about 1.1pp, base 18.4x vs 17.8x, destination PE about 0.5x higher, less-conservative direction. Does not flip the Hurdle (STOP) or the decision (AVOID). Non-decision-determinative. |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| A | B01 Block C Revenue CAGR | Claimed 24.54% vs 24.52% computed; rounding precision below 0.02pp, functionally identical. |
| A | B01 Block C PAT CAGR | Claimed 21.57% vs 21.53% computed; rounding precision below 0.04pp, immaterial. |
| B | B05 4D vs Q3 FY26 (Siddhant K.) | EMS 6-crore-units prior metric unreconciled with the current 4 lakh CPH figure; management sidestepped. Missed transparency gap. |
| B | B05 1B vs Q2-Q3 FY26 | Compressor FY26 revenue expectation halved (about 30cr to 15cr 9M) on delayed mass production; noted but not flagged as a walkdown. |
| B | B05 1B/1C vs Q4 FY26 presentation | Compressor capacity target unstable within the Q4 call (6 / 7.5 / 8.5 / 9.5mn); only the 7.5 to 6 trim was captured. |
| B | B05 1B vs FY25 (Manan) + Q3 (Siddhant K.) | Compressor margin drift from FY25 7-8% to 5% understated; origin and step-down omitted. |
| B | B05 2D vs Q4 FY26 (Abhishek Hindocha) | Q4 employee-expense jump dismissal uncaptured; only the receivables dismissal was caught. |
| B | B06 Claim 4 vs Q4 FY26 (SS/SB) | QCO 40-vs-30 CONTRADICTED possibly overstated (reciprocating vs rotary categories not established as like for like); 40% is anyway the less self-flattering reading. |
| C | B11 Pillar 1 normalized anchor, line 59 | Normalized cycle median rests on a single pre-depression year (FY24 25.66%); FY22-FY23 NOT FOUND. Applied under explicit operator LIVE designation, capped conservatively; acceptable but thin. |
| C | B11 Hurdle Ratio, lines 141-154 | 4-year HR variant (threshold 1.25^4 = 2.4414) used vs the written 3-year form (1.953). Operator FY30 horizon authorizes it; outcome invariant, STOP under both. |
| C | B07 Section 5 scorecard, row H1 | Evidence type labeled documented (implies 1.0x) but the 0.7x multiplier was applied. If corrected, em_score 31 to 32, stays in the STRENGTHENING band; H1 is a non-active Weak category, so active categories unchanged. |
| D | B06 Claim 4, import-allowance section | The 30-vs-40 contradiction is genuinely double-sourced and correctly flagged; only the same-circular attribution to AMBER is an inference beyond AMBER's own transcript. Does not change the verdict. |
