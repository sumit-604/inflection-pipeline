# Chunk 17. The Section 2 worksheet line and Rule E track-record weighting

Loaded by: Role 1 Section 2C-w and Section 4D. Pipeline: stage 11 (emits the 2C-w line in full); stage 10 (assembles `B10.credibility_grade`); stage 05 (produces the Role 5 grade in pipeline runs); stage 15 (Rule H precondition 1); Verifier C (12c).
Sources in force: Section 1B v3.10 Amendment 26 worksheet line and Amendment 26.4; Master v3.7 §2C-w, §4D, pipeline position; Master Role 3 Rule H; quarterly-review skill (grade source).

## The 2C-w worksheet line (state in full, every run)

"Base-case basis: [RUN-RATE / ORDER-BOOK / CAPACITY / GUIDANCE-DISCOUNTED / HISTORICAL]. Evidence: [filing, section, date]. Historical CAGR cross-check: ___% (divergence ___ pp, confirm-by observation: ___, date: ___). Margin bridge: current ___% -> Year 3 ___% via [lever: bps, evidence] x N. Track-record period for weighting: trailing ___ quarters, Role 5 grade ___. Catalyst credit split: revenue ___% / Pillar 3 ___%."

| Field | Where it comes from |
|---|---|
| Base-case basis and evidence | Rule B hierarchy (chunk 07) |
| Historical CAGR cross-check, divergence, confirm-by | Rule B; a divergence above 10 pp feeds the Expectation Ledger (chunk 09) |
| Margin bridge | Rule C bridge, or the cyclical override where flagged (chunk 07) |
| Track-record period and grade | Rule E, below |
| Catalyst credit split | single credit between revenue and Pillar 3 (chunks 03, 04) |

Rule H: Role 3 does not run unless this line declares a forward basis and the margin bridge is stated.

## Rule E: relevant-period track record (Amendment 26.4)

- Probability weights in 4D, and the guidance discount in the GUIDANCE-DISCOUNTED basis, are keyed to the **trailing four quarters of delivery** (the Role 5 credibility ratio).
- Mixed older history plus four quarters of delivery = Good weighting.
- Where Role 5 history is shorter than four quarters, use what exists and state the period.
- A transition name has a thin record for the reason it is interesting. It is not penalised for the years before the transition.

### Where the grade comes from

This skill carries no grading logic.

- Once a quarterly history exists, the credibility grade comes from the `quarterly-review` skill's Role 5 trailing-four-quarter credibility grade.
- In pipeline runs the grade arrives as `B10.credibility_grade` (produced by stage 05, assembled by stage 10). Role 1 reads it; it never re-grades.
- Mapping: A = Excellent, B = Good, C = Mixed, D = Poor.
- If no grade exists, the weighting input is NOT FOUND: state it, and do not infer a grade.

## 4D probability weights

| Grade | Bear | Base | Bull |
|---|---|---|---|
| A (Excellent) | 20% | 50% | 30% |
| B (Good) | 25% | 50% | 25% |
| C (Mixed) | 35% | 45% | 20% |
| D (Poor) | 45% | 40% | 15% |

| Scenario | Probability | 3-year CAGR | Weighted return |
|---|---|---|---|
| Bear | ___% | ___% | ___% |
| Base | ___% | ___% | ___% |
| Bull | ___% | ___% | ___% |
| **Expected CAGR** | 100% | | ___% |

**Re-weighting rule (from Role 4 v1.2), unchanged:** if actuals landed below bear on 2+ key metrics for 2 consecutive quarters, shift one notch toward the Poor weights regardless of the grade. This cuts against the name exactly as Rule E cuts for it.

## Every rule gated on the same grade

| Rule | Gate | Chunk |
|---|---|---|
| 4D weights | grade → weights table | 17 |
| Hurdle Ratio bull row | A or B to use Bull EPS CAGR; else Base + 5 pp maximum | 06 |
| Bull revenue | guidance at face value only if A or B | 07 |
| Bull margin | guided margin at face value where A or B | 07 |
| ORDER-BOOK basis | concall evidence counts only with grade A or B | 07 |
| GUIDANCE-DISCOUNTED basis | guidance discounted by the trailing-4-quarter credibility ratio | 07 |
| Pillar 3a delivery criterion | A or B qualifies; C caps 3a at +2x; D pays +0x | 03 |

All of these read the same trailing-four-quarter grade, stated once in the 2C-w line.
