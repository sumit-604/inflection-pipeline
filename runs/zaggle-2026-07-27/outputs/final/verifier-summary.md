=== FILE: verifier-summary.md ===

Phase 1 verifier findings. Valuation adherence (Verifier C on B10/B11) is deferred to phase 3.

## Confidence delta and acceptance rates

| Verifier | Component | Score | Acceptance rate |
|---|---|---|---|
| A (B12a) | Numerical acceptance | 95.7 | 95.7 |
| B (B12b) | Red flag coverage | 82 | 82 |
| C (B12c) | Framework adherence (Gate 0 + Emerging Moat only) | 98 | 98 |
| D (B12d) | Peer utilisation | 86 | 86 |
| Overall | min of available | 82 | — |

REWORK check: Verifier A CRITICAL 0; no acceptance rate below 60; overall 82. Verdict: NO REWORK. Band 75 to 89 normal.

## Findings, sorted by severity

### CRITICAL

| Verifier | Location | Finding | source_fidelity |
|---|---|---|---|
| D (B12d) | B06 Part 1 Q6 / Part 3 coverage map, Tanla Q3 FY26 (Jan-2026) row | The AI and vibe coding productivity quote ("half of the code that we write is AI generated... what used to take us several months to build... now can be done in weeks") is cited to Tanla but is a RATEGAIN Q3 FY26 quote (Bhanu Chopra, Feb-2026), a second RateGain quote from a call already cited once in the same paragraph. Not present in any Tanla transcript. Converts Tanla's actual silence into fabricated corroboration and inflates Q6 from 2 genuine peers to a claimed 3. | true |

### MAJOR

| Verifier | Location | Finding | source_fidelity |
|---|---|---|---|
| A (B12a) | B01 Block B FCF, FY23 | FY23 FCF claimed at least as negative as -15.62; capex NOT FOUND in any provided source, FY23 cash flow detail unavailable. FY23 FCF bounded by CFO only, not quantified. Does not affect Gate 0 classification (deal breaker driven by FY24 and FY26 verified figures). | true |
| A (B12a) | B01 Block B WC Days, earliest year | FY23 trade payables NOT FOUND; earliest WC year moved to FY24. WC Days change computed FY26 65.28 vs FY24 81.42 = -16.14 days rather than a full 4 year trend. Does not change Block B4 score; reduces historical depth. | true |
| B (B12b) | B05 4D concall red flags / 1C | Astha Jain (Q4 FY26) explicitly raised capitalised dev costs doubling H1 Rs 30 cr to H2 Rs 56 cr (about Rs 107 cr FY26) as an earnings quality and FCF issue; B05 framed it only as an AI productivity plausibility question. Partially caught, under weighted; material to cash flow valuation. | — |
| B (B12b) | B05 2A / credibility section | Q4 FY26 standalone PAT +18% vs revenue +44% (D&A drag from capitalisation) not examined; headline PAT delivery credited without the earnings momentum signal. Missed. | — |

### MINOR

| Verifier | Location | Finding |
|---|---|---|
| B (B12b) | B05 red_flags | Rs 40 cr to 50 cr short term borrowing taken while holding about Rs 440 cr cash (Q4 FY26, Prakshal Jain). Missed; reinforces cash quality concern. |
| B (B12b) | B05 red_flags | Rs 10 cr pre close loan to loss making DICE, netted against the Rs 68 cr payout (Q4 FY26). Missed governance and funding note. |
| C (B12c) | B01 Block B / B4 | Earliest WC Days year anchored to FY24 (FY23 payables NOT FOUND); honest no estimate reading but score maximising (5 vs a possible 3). Correctly disclosed. No decision impact. |
| C (B12c) | B01 Block E / E2 | E2 rule specifies a 3 year window; only a 1 year change (FY24 to FY25 +0.29pp) available. Plus or minus 1% band applied on available history; disclosed. No decision impact. |
| C (B12c) | B07 Section 3 / active_categories | active_categories lists 7 but Section 3 prose and completionist recount say 9 Strong or Moderate (adds borderline B3, R1); counts do not reconcile. em_score 26, STRENGTHENING, TURNAROUND all unaffected. |
| C (B12c) | B07 Section 2C | capex_embedded_growth set to 0 / NOT MEANINGFUL after showing the 190% mechanical arithmetic; defensible for asset light model, flagged in handoff. |
| D (B12d) | B06 Part 3 coverage map, Tanla Q1 FY26 (Jul-2025) row | Row lists CPaaS TAM commentary as a Jul-2025 contribution; the quantified 8 to 12% CPaaS TAM figure in Part 1 Q1 is correctly cited there as coming from the Jan-2026 call (Anubhav Batra). Presentational internal inconsistency. |
| D (B12d) | B06 Part 2B pricing cross-read | RateGain VIVA below OTA take rate (15 to 20%) bundled under the Feb-2026 call; the quote is from the Nov-2025 call. Substance genuinely anchored; quarter attribution off by one call. |

## Logged verifier disagreement

Recorded so the correction is never resolved silently. Disposition: figure corrected at source, correct anchor shown.

| Field | Entry |
|---|---|
| Date | 2026-07-27 |
| Run | zaggle-2026-07-27 |
| Number / claim | B06 Q6 AI productivity dev cycle compression corroborated by "three peers" (Capillary, RateGain, Tanla) |
| Verifier finding + anchor | Verifier D (B12d) CRITICAL, source_fidelity true: quote attributed to Tanla is RATEGAIN Q3 FY26 (Bhanu Chopra, Feb-2026); Tanla silent on AI and dev cycle compression across all three transcripts. B06 Part 1 Q6 / Part 3 coverage map |
| Downstream step + position | B06 peer stage triangulation summary claimed three peer corroboration; carried into narrative and gate documents |
| Disposition | GATE HELD — corrected. Peer corroboration count set to TWO (Capillary, RateGain) at source; correct anchor shown (RATEGAIN Q3 FY26 call, Feb-2026, Bhanu Chopra). Re-checked by Verifier D (B12d). |
| Note | Does not touch any valuation number or the evidence gate decision. Corrected count used wherever peers are discussed in this synthesis. |
