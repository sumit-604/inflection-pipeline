# VERIFIER SUMMARY: DDev Plastiks Industries Ltd (DDEVPLSTIK)

Run: runs/ddevplstik-2026-07-23 | Date: 2026-07-23 | Phase 3 (valuation-inclusive)

## CONFIDENCE DELTA AND ACCEPTANCE RATES

| Component | Score | Verifier | Acceptance rate |
|---|---|---|---|
| Numerical acceptance | 98.6 | A (B12a, haiku) | 98.6% |
| Red-flag coverage | 64 | B (B12b, opus) | 64% |
| Framework adherence | 97.5 | C phase 1 (B12c, opus) 98% + C phase 3 (B12c-valuation, opus) 97% | 98% / 97% |
| Peer utilisation | 80 | D (B12d, sonnet) | 80% |
| **Overall** | **64** | min of four (red-flag-bound) | 60-74 band; downgrades a clean PROCEED one level |

REWORK triggers: none fired. Verifier A 0 CRITICAL; no acceptance below 60; no source-fidelity MISMATCH on a verdict-card or pillar input. Valuation-framework adherence complete at 97% (0 CRITICAL, 0 MAJOR, 3 MINOR cosmetic).

## FINDINGS, SORTED BY SEVERITY

### CRITICAL

None across all verifiers (A 0, B 0, C phase 1 0, C phase 3 0, D 0).

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| A (B12a) | B02 Note 52 lease-liability roll-forward | ANCHOR NOT FOUND: the internal-note reconciliation break was verified by B02's prior-stage auditor (source text p.185-186) but not independently re-verified this run due to text-cache limits; prior auditor confirmed it a genuine disclosure-control failure. Marked source_fidelity: true. A confirmed disclosure-quality weakness already flagged by B02/B03, not a financial-statement error and not a verdict-card figure. |
| B (B12b) | B05 Section 2A / promise_delivery (132 kV row) | 132 kV XLPE trial graded "delivered (implied)" and counted in the 5-delivered tally though no call confirms a successful trial or commercial supply; honest tally is 4 delivered / 4 partial / 4 missed. Decision and B-grade survive. |
| D (B12d) | B06.md lines 88, 119 (BEPL row) | BEPL characterization ("synthetic rubber/latex/emulsion polymer producer") attributed to sources that do not contain the text (grep-confirmed zero occurrences across all 12 screening CSVs and B05); a fabricated anchor inflating the BEPL blind-spot framing. Peripheral to the DDev verdict. |
| D (B12d) | B06.md lines 18-19 and Q4 answer (lines 61-69) | "Apcotex never once uses the words battery across all four transcripts" is false; "battery" appears in the Q1 FY26 call (31-Jul-2025) in a claim-relevant context never surfaced despite that transcript marked SUBSTANTIVE. Peripheral to the DDev verdict. |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| B (B12b) | B05 Section 3B / tone table (EBITDA/ton) | EBITDA-per-ton, presented as a clean transparency positive, includes non-operating other income per management's own words (Q1 p.11); quality caveat not raised. The single missed independent flag. |
| B (B12b) | B05 Section 3D / red_flags | BESS customer pipeline entirely pre-order/pre-MOU; noted as pre-revenue but absence of any binding order not elevated to a red flag despite BESS weighting. |
| B (B12b) | B05 Section 2C over-promotion | BESS ROCE 25-30% claim sits against initial EBITDA margins management pegs 5-8% below the ~11% core; internal ROCE-versus-margin tension not surfaced. |
| C phase 1 (B12c) | B01 Block E, E2 | E2 scored 3 using a 1-year holding-change window as proxy for the required 3-year window; deviates from the score-0-if-unavailable rule. Immaterial: core stays in the 60-79 GOOD band. |
| C phase 1 (B12c) | B01 Block F, M8 | M8 Distribution scored 1 via "mentioned unquantified" though reach is quantified (55 countries); higher bands genuinely fail. Defensible edge call, moat class unchanged. |
| C phase 1 (B12c) | B07 Section 3 / scorecard | 7 active Strong/Moderate categories sits one above the stated 3-6 realistic base rate; completionist recount performed and disclosed, no category mis-tiered. Observation, not a scoring error. |
| C phase 3 (B12c-valuation) | B11 4H Hurdle Ratio | HR uses capped 25.0x as "mid" versus range-mid 24.0x; 24.0x gives HR 2.35, still PASS; verdict unchanged. |
| C phase 3 (B12c-valuation) | B11 4E versus B14 Sec 5/7 | Entry-range low labelled Rs 303 (30% CAGR) in B11 versus Rs 273 (MoS) in B14; same numbers, cosmetic. |
| C phase 3 (B12c-valuation) | B11 RRM track | RRM applied to quality-adjusted base ex-Pillar-3; operator-approved derivation, non-material, both tracks clamp to the 25x cap. |
| D (B12d) | inputs/screening/BEPL-Data_Sheet.csv | BEPL quantitative screening data (CWIP trend, Q1 FY27 sales/margin spike) left unexamined as a coarse cross-check; outside stage 6's injected-input scope, an input-assembly gap rather than a B06 fault. |

## PHASE 3 VALUATION-ADHERENCE AUDIT (B12c-valuation, opus)

34 valuation rules checked, 0 fails, 3 MINOR cosmetic findings above. All pillar mechanics PASS: Pillar 1 formula and ROCE selection and v3.5.1 route (none; STAGNANT/DECLINING bars both routes) and single-credit; Pillar 2 multiplier (1.00x = INDETERMINATE neutral) and offset (none); Pillar 3 (3a +2x conservative, 3b +0x EM 23<25, 3c +0x no order book, shared catalyst flagged not double-credited, strategic +0x); UA qualifiers and ordering (min(Raw x1.25, Cap), Amendment 3); sector cap (Cables/Industrial 25x absolute); dual-track (both present, RRM 1.06 percentage-point, both cap 25x); Hurdle Ratio 2.45 versus threshold 1.953 PASS (recomputed, concur); Role 2 tier A, all four buy-now conditions hold, entry conjunction, position size Small (documented downgrade from mechanical Medium, defensible).
