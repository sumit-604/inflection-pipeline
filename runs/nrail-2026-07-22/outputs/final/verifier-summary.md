# VERIFIER SUMMARY (PHASE 1) — NRAIL, 2026-07-22

## Confidence delta and acceptance rates

| Component | Score | Verifier | Acceptance rate |
|---|---|---|---|
| Numerical acceptance | 93.9 | A (B12a, Haiku) | 93.9% (77/82 numbers clean) |
| Redflag coverage | 90 | B (B12b, Opus) | 70% raw (7 of 10 independent flags cleanly caught; component score 90 counts 7 full + 2 partial) |
| Framework adherence, Gate 0 + Emerging Moat only | 95 | C (B12c, Opus) | 95% (55/58 rules passed; valuation portion pending phase 3) |
| Peer utilisation | 88 | D (B12d, Sonnet) | 88% (7 of 8 peer transcripts correctly handled) |
| Overall (min of available) | 88 | — | band: normal (75 to 89) |

No CRITICAL from any verifier. No source fidelity MISMATCH survived to a verdict input. REWORK not triggered.

---

## Findings, sorted by severity

### CRITICAL
None.

### MAJOR

| Verifier | Location | Finding |
|---|---|---|
| A | AR Chairman's letter p.7 vs P&L p.99 vs infographic p.4/8 | Chairman's letter states PAT "decreased to Rs 15.96 cr". Audited P&L shows PAT Rs 17.65 Cr; Rs 15.96 Cr is PBT. AR infographic p.4/8 correctly shows PAT Rs 17.65 Cr. AR internal mislabel, correctly caught by Stage 3 (B03). Reclassified CRITICAL to MAJOR on source re-read; source_fidelity finding, gate held. |
| A | AR Chairman's letter p.7 vs p.9 | Plant investment stated as Rs 850 Cr on p.7 and Rs 1,000 Cr on p.9 for the same project, unreconciled. Implied 17.65% overrun. Disclosure gap in the source, both pages cited by B03. |
| A | AR Chairman's letter p.8, MD&A | FY26 guidance framed as 36% growth using the FY24 base of Rs 1,617 Cr. Against FY25 actual Rs 1,659.03 Cr the implied growth is 32.6%. Selective base year choice, not an arithmetic error. |
| A | AR Key Numbers p.17 vs Note 57 p.162 | ROCE FY24 shown as 11.06% (p.17) and 11.28% (Note 57). AR internal inconsistency, 0.22pp, immaterial to scoring, flagged by B03. |
| B | 05-concall Section 2A row 3 / 4C / 4D | FY26 profit recovery earnings quality not interrogated. March quarter NPAT Rs 1,419.84 L was 32.5% of full year NPAT Rs 4,369.91 L against a prior year Q4 loss, with no pre versus post exceptional bridge despite an unexplained Rs 444.29 L discard loss. Underpins the upper B credibility grade. The one fully missed independent flag. |
| C | 01-gate0 L214/L324; B01 YAML blocks{} L433 | Block E (Shareholder Alignment, 8/20) computed in body but dropped from Core Score, Grand Total and the emitted blocks map. Recompute: core 28 not 20, grand total 33 not 25. Decision unchanged AVOID, since core below 40 and deal breaker 6 both mandate AVOID. |
| D | Part 3 Peer Coverage Map / peer_coverage_map[0] | JK Paper Q4 FY22 call (filed May 2022) marked SUBSTANTIVE with no page anchored citation in Part 1/2; coverage map also overstates a company specific capex remark as an industry wide observation. |
| D | Part 1, Q1 evidence row | EBITDA margin 33.1% (FY23) attributed to the Q4 FY24 call (21 May 2024) p.2. The figure appears verbatim in the Q4 FY23 call (19 May 2023) p.2. Genuine number, wrong call and date. |

### MINOR

| Verifier | Location | Finding |
|---|---|---|
| A | AR Key Numbers p.17 vs Schedule V p.39 | EBITDA margin FY25 shown as 8.59% and 8.70% under two revenue base definitions, both correct, 0.11pp, immaterial. |
| B | 05-concall Section 4D flag 3 | Base year mislabel weighted Low; true FY25 to FY26 growth is +29.3%; warrants low to medium. |
| B | 05-concall Section 2B / 4C | excuse_pattern "honest" in mild tension with the base year mislabel plus two peer contradicted narrative claims; grade B survives. |
| B | 05-concall Section 2D / 4D | Debt funded capex noted but no cash conversion or CFO quality red flag raised at this stage; leverage trajectory handed on untagged (partly a Stage 11 lane). |
| B | environment / whole audit | Primary source PDFs un-renderable (pdftoppm absent, no shell); B05/B06 page anchors not independently re-verified; source fidelity defers to Verifier A. |
| C | 01-gate0 L356 / B01 YAML L441 | history_downgrade set true on a 5 year history that belongs in the 5 to 6 year flag only tier; immaterial at the AVOID floor. |
| C | 07-emoat L204 vs L170-174 | R1 regulatory tailwind impact scored Moderate though the Gujarat subsidy is shared eligibility, about Rs 9.1 Cr, undisclosed duration; a Low impact is defensible; EM would fall to about 18, still MODEST. |
| C | 01-gate0 Block A | Observation, not counted: A1/A4 blend company disclosed ROCE (FY22-25) with pipeline computed FY26; basis mix not flagged the way ROE/D-E/ICR were; framework sanctioned, moves no band. |
| D | Part 2E / risks_peers_raise | MIP and antidumping "1.5 to 2 years" timeline cited to Kuantum Q4 FY26 p.9-10; the exact quote is on p.8. Quote accurate, page imprecise. |
| D | Stage flags / YAML flags | Notebook segment exit 22% to 7-8% cited to Kuantum Q4 FY26 p.13, 17; first statement is on p.11. Figures accurate, page imprecise. |
| D | Part 3 Peer Coverage Map, Kuantum Q1 FY26 row | Row lists "wheat straw/wood cost baseline"; the 11 Aug 2025 call does not mention wheat straw, which first appears in the Q2/H1 FY26 call and is correctly cited elsewhere. Content exists, misattributed in this row. |

---

## Verifier disagreement note

Verifier A initially raised the Chairman's letter PBT/PAT item as CRITICAL, then reclassified it to MAJOR on source re-read.

Disposition: the figure is correct at source. Audited P&L (AR p.99) shows FY25 PAT Rs 17.65 Cr and PBT Rs 15.96 Cr, and the AR infographic p.4/8 correctly shows PAT Rs 17.65 Cr. The error is an AR internal mislabel in the Chairman's narrative, and it was caught by Stage 3 (B03) source reading, not introduced by the pipeline. The orchestrator independently confirmed the figures at source. GATE HELD, no REWORK. The mislabeled Rs 15.96 Cr was not carried into any verdict input as PAT.

Verifier B's raw acceptance rate reads 70% because it counts cleanly caught flags (7) over its own independent flags found (10). Its contributed confidence component is 90, which credits the 2 partially caught flags alongside the 7. The single fully missed flag, FY26 earnings quality and Q4 concentration, is carried as a MAJOR above and feeds the cash INDETERMINATE call and the falsification line.
