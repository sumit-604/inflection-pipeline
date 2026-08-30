# Verifier Summary — Entero Healthcare Solutions (ENTERO), run 2026-07-27

## Confidence delta and acceptance rates

| Component | Score |
|---|---|
| Numerical acceptance (Verifier A, B12a) | 89 |
| Red-flag coverage (Verifier B, B12b) | 85 |
| Framework adherence (Verifier C, B12c) | 94 |
| Peer utilisation (Verifier D, B12d component) | 92 |
| Overall | 85 |

Band: normal (75-89). No PROCEED downgrade, no forced REWORK. Zero CRITICAL across all verifiers in both phases. No acceptance rate below 60.

Acceptance rates by verifier: A (numerical) 89; B (red-flag) 85; C (framework: Gate 0 + Emerging Moat phase 1, valuation-adherence phase 3) 94; D (peer, own file) 83. Phase-3 valuation adherence COMPLETE: Verifier C concurs destination PE 19x both tracks and decision AVOID, HR STOP at CMP 1,806; zero CRITICAL or MAJOR, 2 MINOR presentational.

## Findings, sorted by severity

### CRITICAL
None.

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| A (B12a) | B02 Finding 6 | source_fidelity: "Adjusted net debt-to-equity 0.02x->0.23x" methodology not traced to a note; consolidated basis shows 0.09x->0.31x. Term may exclude certain instruments. |
| A (B12a) | B02 Finding 8 | source_fidelity: CEO remuneration Rs43.74M->Rs94.50M (+116%) build not re-verified in abbreviated read; Note 52 p.235 exists, full breakdown pending complete note review. |
| A (B12a) | B02 Finding 1 | source_fidelity: goodwill 43.8% of net worth; numerator Rs7,490.90M verified (Note 6), denominator Rs17,090.35M not a single BS line, appears computed from equity components. |
| A (B12a) | B02 Finding 12 | source_fidelity: CFO/CS changed within ~2y of IPO; current CFO verified, prior CFO name not in provided corpus (FY25 AR / IPO signing block absent). |
| B (B12b) | B05 2D/2E/red-flag table | MISSED: Q1 FY27 refusal to disclose quarterly gross debt, net debt and OCF (Q1 call 10-Aug-2026, Binoy Jariwala exchange, p.14); part of a three-quarter granularity-opacity pattern, two instances missed. |
| B (B12b) | B05 red flag 7 | PARTIALLY CAUGHT: minority-buyout call options are a committed forward cash claim on thin OCF (Q1 p.3,6-7,11); accounting caught, cash-claim implication under-weighted. |
| D (B12d) | B06 Part 1, Q5 evidence | "LIT is a better gross margin product" attributed to Rajesh Goenka (RPTECH May-2026) is actually analyst Madhur Rathi's question premise, not a management claim; weakens the independent-corroboration basis of the Q5 PARTIALLY VERIFIED grade. |
| D (B12d) | B06 Part 3 coverage map, RPTECH Nov-2025 row | Labelled CITED-ONLY "no new decisive evidence," but Part 1 Q1 net-read substantively cites this same call for the 10-12% false-friend finding; internal inconsistency, understates the evidence. |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| B (B12b) | B05 red flag 1 / 2D | Reach-metric label shifted "retail pharmacies" -> "retail customers" Q4->Q1; relabel deepens rather than explains the contraction. |
| B (B12b) | B05 1B item 7 / 4A#6 | Rising leverage framed only as an upside trigger, not a risk; ~Rs 200 Cr fresh acquisition debt, IPO funds exhausted (Q1 p.7). |
| C (B12c) | B07 Section 5 scoring (phase 1) | Documented rows B3/D1/D2 multiplied 0.7 not 1.0; conservative, no classification or UA impact (18.8 vs <=20.7, both MODEST). |
| C (B12c) | B11 fair_values labelling | Year-3 exit prices (base 929) unqualified while decision cites today's FV Rs 617; framework-math correct at every use (FV today 617 -> Y3 929, FV CAGR 14.6%; CMP 1806/617 = 2.9x). Presentational; rename fair_values_exit_y3, add fair_value_today: 617. |
| C (B12c) | B11 Hurdle Ratio basis | Y0->Y3 EPS CAGR used with a Year-1 forward Current PE; strict-forward g is Y1->Y4 CAGR (14.6%); overstates HR ~0.03; verdict-invariant, STOP holds. |
| D (B12d) | B06 Part 1, Q5 evidence | "close to 6% gross margins" is analyst premise; only the PAT clause is S.V. Krishnan's reply (REDINGTON Feb-2026); management confirms direction, presentation overstates what was volunteered. |
| D (B12d) | B06 Part 3 / Q1 cross-reference | MEDPLUS SSSG "10.5% (Feb-2026)" not found verbatim; only analyst paraphrase "10% plus"; directional finding confirmed verbatim elsewhere in the same call. |
| D (B12d) | B06 Part 2E | RPTECH "quantifies the expected revenue hit" from Micron end-of-life overstates; response is qualitative only ("crucial definitely will be a dent"), no number given. |

## Notes carried from the confidence record

- Verifier A's 4 MAJOR items are all source_fidelity source-confirm items; none sits on a verdict-card or Section 1B pillar input. The FY26 owners' PAT/EPS (Rs 115.04 Cr / Rs 26.40) and the net-worth denominator were settled from the filed consolidated results at stage 11. See verifier-disagreement-log.md.
- Verifier B credibility-grade concurs: B (Good) fits the strong guidance-delivery record; the balance-sheet-opacity pattern is broader than B05 credited but sits at the low edge of B, not below it.
- Rs 617 (intrinsic today) versus Rs 929 (Year-3 target at 19x forward) reconciled by Verifier C; labelling MINOR.
