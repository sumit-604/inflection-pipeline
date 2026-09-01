# CLEANMAX verifier summary (phase 1)

## Confidence delta and acceptance rates

| Verifier | Component | Score | Acceptance rate |
| --- | --- | --- | --- |
| A (numerical, B12a) | Numerical fidelity | 97 | 97% (34 of 35 numbers clean) |
| B (red-flags, B12b) | Red-flag coverage | 67 | 67% (8 of 12 independent flags caught upstream) |
| C (framework, B12c) | Framework adherence (Gate 0 + Emerging Moat) | 98 | 98% (49 of 50 rule checks) |
| D (peers, B12d) | Peer utilisation | 68 | 79% (13 substantive of 19 transcripts) |
| Overall | min of the four | 67 | band 60-74 (normal-minus) |

Verifier A found 0 source-fidelity findings. No REWORK was triggered: zero CRITICAL findings, no verifier acceptance below 60%, overall 67 (above 60). No Verifier-A-versus-downstream disagreement to log.

## CRITICAL findings

None.

## MAJOR findings

| Verifier | Location | Note |
| --- | --- | --- |
| B (B12b) | B05, Bikaner analysis 2A/3C/4D | Missed the disclosed TGNA status and no-revenue-protection mechanism; explains why 70% curtailment yields the ~Rs 170 Cr hit and resolves B06's most consequential open question. Anchor: Concall Mar 2026 p.18, May 2026 p.11. |
| B (B12b) | B05, 2E / 2A | Missed the repeated (2-quarter) deferral of quarterly generation/PLF disclosure and the unkept Q3 promise to provide it. Anchor: Concall Mar 2026 p.11, p.17; Aug 2026 p.14. |
| C (B12c) | B01 report file (whole) | Prompt 01 requires a closing fenced YAML block; the report file had none. Decision AVOID survives via prose; machine-readable payload was missing. Remediated: block written to outputs/blocks/B01-gate0.yaml and appended to the report. |
| D (B12d) | B06 Part 3, ACMESOLAR Q2 FY26 (Nov 2025) row | Wrong-transcript citation: the Sikar Rs 17.5 Cr curtailment loss appears in the ACMESOLAR Feb 2026 (Q3 FY26) transcript line 159, not the Nov 2025 call. Underlying fact true, call misattributed. |
| D (B12d) | B06 Part 3, JSWENERGY Q4 FY26 (May 2026) row | Marked CITED-ONLY, but the transcript also carries a 160 MU curtailment / Rs 16-50 Cr revenue-loss GNA-protection disclosure directly relevant to Claim 6, left unused. Anchor: JSWENERGY Concall May 2026, lines 232-240. |

## MINOR findings

| Verifier | Location | Note |
| --- | --- | --- |
| A (B12a) | B01, Block A | Median ROE (FY23-26) reported 1.94% does not reproduce from a direct median of the reported series (-0.385%); methodology likely uses a Data_Sheet averaging convention. Decision-neutral, ROE scores 0 regardless. Not a source-fidelity finding. |
| B (B12b) | B05 2A | Credit-rating "full notch within one quarter" overstated; the A+ to AA span is about a year, not one quarter. Anchor: May p.9; Aug p.3, p.9. |
| B (B12b) | B05 2A promise table | Counts 500 MW (incl. 100 MW RE services) as ~33% of the 1.5 GW floor; the floor is opex/power-sales capacity, so ~400 MW is ~27%. Anchor: May p.6; Aug p.4, p.13. |
| B (B12b) | B05, net debt handling | Under-weighted: net debt rose Rs 9,684 to Rs 11,809 Cr in one quarter, 38% (Rs 4,483 Cr) against non-earning under-construction assets. Anchor: Aug p.8. |
| B (B12b) | B05, curtailment/uptime framing | Under-weighted: the blended 99%+ grid-uptime headline masks the 70% Bikaner CTU curtailment. Anchor: May p.7; Aug p.6. |
| C (B12c) | B01, Block C, C2/C4 | PAT CAGR marked N/M gives C2=0, C4=0; a strict first-edge reading of positive endpoints would compute ~30% (C2=5, C4=5). Loss-to-profit-swing clause invoked, defensible; still under 40 and DB#6 fires, AVOID unchanged. |
| C (B12c) | B01, data-confidence / history downgrade | Core Blocks A/B/D rest on 4-year balance-sheet detail; the 3-4 year rule allows a one-tier downgrade not taken. Decision-neutral. |
| C (B12c) | B07 Section 5, H2 | Mixed documented/voice partnership treated documented at 1.0x; documented core (Osaka Gas Rs 176 Cr, Apple JV Rs 100+ Cr) with the voice target parked in optionality. Defensible, no score impact. |
| D (B12d) | B06 Part 3, JSWENERGY Q3 FY26 (Jan 2026) row | Marked CITED-ONLY, but the transcript also carries a GNA/TGNA curtailment exchange, redundant with citations already used. Industry-context miss, not decisive. |
| D (B12d) | B06 Part 3, ADANIGREEN Q3 FY26 (Jan 2026) row | Marked CITED-ONLY, but the transcript also carries curtailment Q&A, redundant with citations already used. Industry-context miss, not decisive. |
| D (B12d) | B06 Part 1, Claim 4 (KPIGREEN Feb 2026) | CPP EBITDA margin cited 18-22%; transcript gives 18-20% (management, line 571) and 20-22% (analyst-framed, line 564). Reasonable rounding, not a single verbatim figure. |

## Gate 0 and Emerging Moat framework audit (Verifier C, B12c)

- Gate 0: 38 rules checked, 1 MAJOR fail (missing closing YAML block, remediated), no valuation rules run (deferred to phase 3). Verifier C concurs with the AVOID classification.
- Emerging Moat: 12 rules checked, 0 fails.
- Business Understanding Narrative: not in phase-1 scope, not audited.
