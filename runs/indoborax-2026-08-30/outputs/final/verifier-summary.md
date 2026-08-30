# Verifier summary (phase 1)

Confidence delta and acceptance rates.

| Component | Score | Verifier | Acceptance rate |
|---|---|---|---|
| Numerical acceptance | 94 | A (B12a) | 94 |
| Red flag coverage | 64 | B (B12b) | 64 |
| Framework adherence | 94 | C (B12c), Gate 0 + Emerging Moat only | 94 |
| Peer utilisation | 75 | D (B12d) | 86 |
| Overall (min of four) | 64 | | |

Verifier C's valuation adherence audit is deferred to phase 3; only its Gate 0 and Emerging Moat checks ran this phase. No CRITICAL findings from any verifier. No forced REWORK.

## Findings, sorted by severity

### CRITICAL

None.

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| A (numerical) | 01-gate0.md Block B, line B4 | FY26 inventory days 53.94 and payable days 5.25 do not reconcile to the AR Note 27 COGS basis (101.68 and 9.89); denominator basis not disclosed. Source fidelity flag. Affects the Block B4 score and the WC days swing narrative. |
| B (red flags) | B05 excuse_pattern | "balanced-with-one-deflection" understates a repeated within call deflection to prior management: margin history (Kalra p.7), DOT under utilisation (Kalra p.20), debt and pledge deferred to IR email (p.20). Decision survives; single call caps grade at C. |
| D (peers) | B06 Part 5, Part 3 coverage map | Two excluded but available DMCC transcripts (Nov-2024, May-2025) hold claim relevant material: DMCC's boron business was already large and growing for 4 to 5 quarters, and its capex caution predates the Nov-2025 Turkey ore disruption by a full year, qualifying Part 5's causal framing. |
| D (peers) | B06 Part 2C, Part 5 | The Rs 495 cr figure attributed to "the R-32 project" is a combined plan of Rs 405 cr HFC-32 plus about Rs 90 cr other products; the R-32 project alone is Rs 395/390 cr. Overstates the R-32 specific commitment by about 20 to 25 percent. |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| B (red flags) | B05 red_flags[5] / analyst_note | PAT exceeds EBITDA in Q4 (14.53 vs 12.82) and FY26 (50.27 vs 44.16); the growth quality implication that the 41.9 percent PAT jump is largely non operating is not surfaced as a flag. |
| B (red flags) | B05 red_flags[4] | Investor concern that the Rs 30 special dividend services promoter acquisition covenants (Bajaj p.11) is not drawn out; the dividend to leverage linkage is not flagged. |
| B (red flags) | B05 trigger 2 | Boric Acid at peak capacity (Kalra p.5, p.9) with only 1,000 to 1,500 t debottlenecking headroom (p.26) versus a 20 to 35 percent revenue guide is not itemised as a capacity versus guidance tension. |
| B (red flags) | B05 (absent) | Guidance anchored to a cherry picked best quarter (Q3 set aside, Q4 made the run rate base, Kalra p.9) is not noted. |
| C (framework) | B01 Block A, 01-gate0.md lines 30-73 | FY17 to FY24 ROCE computed via Net Worth + Borrowings rather than a screener ROCE figure. Transparently justified by the missing capital employed split; band invariant. |
| C (framework) | B01 M7, 01-gate0.md lines 282-287 | Regulatory / licence test scored 0 PEER DATA NEEDED though the sole India manufacturer FDA/BIS position is documented. Conservative and rule defensible; classification unchanged (deal breaker 5 caps to AVERAGE). |
| C (framework) | B07 G1 scorecard, 07-emoat.md lines 287, 423 | War chest scored with a 1.0x documented multiplier, while the emerging moat value (capex deployment) rests on management claim and the documented leg is static cash. Does not cross a band. |
| C (framework) | B07 active_categories, B07-emoat.yaml lines 14-17 | G1 labelled strength "Moderate" in YAML while the Section 3 band table places it in Weak-Moderate. Presentational inconsistency. |
| D (peers) | B06 Part 1 Claim 3, Part 2E | DMCC page citation convention inconsistent across the two cited calls (PDF page order vs printed footer). Quote content verified accurate. |
| D (peers) | B06 Part 1 Claim 4 | Tanfac "16.3% prior year" EBITDA margin is not verbatim; computed from disclosed figures the ratio is about 16.48 percent. |
| D (peers) | B06 Part 1 Claim 4 | Tanfac 30 to 45 day pass through lag detail is on transcript footer p.6, not p.4 as cited alongside the margin compression quote. |

## Verifier disagreement log

Points where a downstream step's conclusion conflicted with a Verifier A source fidelity finding, or where a source re check cleared a flag.

| Date | Run | Number / claim | Verifier A verdict + anchor | Downstream step + position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-08-30 | indoborax-2026-08-30 | Gate 0 Block B4 WC days: inventory 53.94, payable 5.25 | MAJOR source fidelity, unreconciled to AR Note 27 COGS basis (about 101.68 / 9.89), 01-gate0.md Block B line B4 | B04 bizmodel independently computed about 99 to 101 inventory days | GATE HELD, figure to be corrected at source; the 53.94 / 5.25 pair is removed from any verdict input and B04's about 99 to 101 day computation is carried forward as closer to the AR basis | No valuation verdict card exists in phase 1; correction stands for phase 3 assembly. |
| 2026-08-30 | indoborax-2026-08-30 | B02 finding #3: "about 66 percent (Rs 2,805 lakh) of FY26 investment property monetisation to an unnamed counterparty" | Not a Verifier A finding; B03 vs B02 source discrepancy | B03 AR deep dive re checked AOC-2 Annexure III, AR p.42 | FLAG CLEARED, source re check found AOC-2 names the FULL Rs 4,250 lakh residential property disposal as a Jain family RPT (Sajal / Saumya / Sreelekha Jain jointly), not a 34 percent named plus 66 percent unnamed split; re checked by stage 3 (B03) | The disposal is fully related party, which strengthens, not weakens, the promoter RPT flag. |

No other disagreements this run.
