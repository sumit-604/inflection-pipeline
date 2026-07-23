# Verifier summary (phase 1)

Confidence delta: numerical 98.6 / red-flag 64 / framework 98 / peer 80 / overall 64 (min, redflag-bound). Band 60 to 74: a clean PROCEED downgrades one level. No REWORK: 0 CRITICAL, all acceptance at or above 60, no source-fidelity MISMATCH on a verdict-card input.

Acceptance rates: Verifier A 98.6 (numbers) | Verifier B 64 (red flags) | Verifier C 98 (framework, Gate 0 + Emerging Moat portion; valuation adherence pending phase 3) | Verifier D 80 (peers).

Totals across the four (phase-1 scope): 0 CRITICAL, 4 MAJOR, 7 MINOR.

## CRITICAL

None.

## MAJOR

| Verifier | Location | Finding |
|---|---|---|
| A (B12a) | B02 Note 52 lease-liability roll-forward | Note 52 closing balance claim could not be independently re-verified in this run (note text unavailable in cache); the roll-forward break is a genuine disclosure-control weakness confirmed by the prior-stage auditor (source p.185-186). Marked source_fidelity true. Not a financial-statement error; carried forward as a known disclosure gap, not a verdict-card MISMATCH. |
| B (B12b) | B05 Section 2A / promise_delivery, 132 kV row | 132 kV XLPE trial graded "delivered (implied)" and counted in the 5-delivered tally though no call confirms a successful trial, approval or commercial supply (Q4 p.19 only says "reached up to the capacity of 132 kV"). Honest tally is 4 delivered / 4 partial / 4 missed. Credibility grade B and the evidence base survive. |
| D (B12d) | B06.md lines 88, 119 (BEPL row) | BEPL business characterization ("synthetic rubber/latex/emulsion polymer producer") is attributed to its screening CSV and to Stage 5, but neither source contains that text (grep-confirmed zero occurrences across all 12 screening CSVs and B05). A fabricated anchor inflating the BEPL blind-spot framing. Peripheral to DDev's evidence base; BEPL is UNUSED (no transcript). |
| D (B12d) | B06.md lines 18-19 and Q4 answer (lines 61-69) | "Apcotex never once uses the words battery across all four transcripts" is false; "battery" appears in the Q1 FY26 call (31-Jul-2025, textcache lines 413-421) in a claim-relevant context never surfaced, despite that transcript being marked SUBSTANTIVE and claimed read in full. Peripheral point; does not change DDev's evidence base. |

## MINOR

| Verifier | Location | Finding |
|---|---|---|
| B (B12b) | B05 Section 3B / tone table (EBITDA/ton) | EBITDA-per-ton, presented as a clean transparency positive, includes non-operating other income per management's own words (Q1 p.11); quality caveat not raised. Source partly in the 3-cap-excluded Q1 call. |
| B (B12b) | B05 Section 3D / red_flags | BESS customer pipeline is entirely pre-order and pre-MOU (Q3 p.7-8, Q4 p.9-10); noted as pre-revenue but the absence of any binding order not elevated to a red flag despite BESS revenue weighting. |
| B (B12b) | B05 Section 2C over-promotion | BESS ROCE 25-30% (Q3 p.11-12) sits against initial EBITDA margins management pegs 5-8% below the ~11% core (Q4 p.10-11); the internal ROCE-versus-margin tension not surfaced. |
| C (B12c) | B01 Block E, E2 | E2 scored 3 using a 1-year holding-change window as proxy for the required 3-year window; deviates from the score-0-if-unavailable rule. Immaterial: does not move core out of the 60-79 GOOD band. |
| C (B12c) | B01 Block F, M8 | M8 Distribution scored 1 via "mentioned unquantified" though reach is quantified (55 countries); higher bands genuinely fail. Defensible edge call, immaterial, moat class unchanged. |
| C (B12c) | B07 Section 3 / scorecard | 7 active Strong/Moderate categories sits one above the stated 3-6 realistic base rate. Completionist recount was performed and disclosed; marginal rows carry 0.7x multipliers; no category mis-tiered. Observation, not a scoring error. |
| D (B12d) | inputs/screening/BEPL-Data_Sheet.csv | BEPL quantitative screening data (CWIP trend, Q1 FY27 sales/margin spike) was available in this run's inputs and left unexamined as a coarse cross-check. Outside stage 6's transcript-only scope, so an input-assembly gap rather than a B06 execution fault. |

Scope note: Verifier C's valuation-framework portion (B10/B11) is deferred to phase 3 and not audited here; only the Gate 0 and Emerging Moat rules were checked (61 of 62 audited rules pass, E2 the sole minor fail).
