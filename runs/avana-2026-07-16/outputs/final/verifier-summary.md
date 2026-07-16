# Phase-1 verifier summary

## Confidence delta and acceptance rates

| Component | Score | Acceptance / basis |
|---|---|---|
| Numerical acceptance (verifier A, B12a) | 88 | 28 of 32 numbers clean; 0 CRITICAL, 0 MAJOR, 4 MINOR |
| Framework adherence (verifier C, B12c) | 100 | 47 Gate 0 rules + 14 Emerging Moat rules; 0 CRITICAL, 0 MAJOR, 2 MINOR presentational |
| Red flag coverage (verifier B) | N/A | not run; no subject concall/AR/results narrative to audit |
| Peer utilisation (verifier D) | N/A | not run; no B06 exists |
| Overall | 88 | min of available components; band 75-89 normal. Measures fidelity to sources, not evidence sufficiency |

Verifier A acceptance rate: 88%. Verifier C acceptance rate: 100%. No REWORK trigger fired (0 CRITICAL, no acceptance below 60%).

## Findings, sorted by severity

CRITICAL: none.

MAJOR: none.

MINOR:

| Verifier | Location | Note |
|---|---|---|
| A (numerical) | B09 Section 1B | Order book Rs 52.24 Cr (30-Nov-2025) not in screener; sourced from RHP/IPO aggregator. Anchor NOT FOUND in local sources; no contradiction found elsewhere. |
| A (numerical) | B09 TAM section | TAM Rs 1,100-1,700 Cr rests on third-party reports (Mordor, Markets & Data, ICRA) behind HTTP 403 paywalls, recovered via search snippets. Web-sourced tier, not local-PDF verified; report acknowledges the limit; no contradiction in peer concalls. |
| A (numerical) | B07 Section 2C | Implied incremental revenue 4.67 x 15.76 = 73.60 Cr; exact 73.6352 Cr. Rounding within tolerance (<0.1%). |
| A (numerical) | B07 Section 2C | Capex-embedded growth stated 87.8%; exact 87.75%. Rounding within tolerance (<0.05pp). |
| C (framework) | B01 M9 gross-margin proxy | Used (Rev - RawMaterial - ChangeInInventory)/Rev vs framework's (Rev - MaterialCost)/Rev. Disclosed in data_notes; +6.45pp vs peer median keeps M9 in the same 3/5 band under either formula. No score or classification impact. |
| C (framework) | B07 evidence_mix (inference:8) | inference:8 counts narrative touchpoints, not the 2 nonzero-scored inference categories (G1, R1); unreconciled and potentially misleading downstream. Scorecard, active_categories (1), and completionist_recount are internally correct. No score impact. |

## Verifier coverage notes

Verifier A confirmed 100% of verdict-card figures (Gate 0 classification, core/moat/grand scores, deal-breaker application) clean against the screener data sheet, plus all Block A-E and Moat M1-M11 inputs, all AVANA revenue/EPS/P/E figures in B09, and peer moat metrics. No fabrications, no mechanical errors, no material misstatements of sources; all limitations stated in upstream reports.

Verifier C recomputed core score 49, classification AVERAGE, moat FORTRESS, grand total 76, em_score 2.5, em_classification NONE, and combined AVERAGE, all matching B01 and B07. All 9 Gate 0 deal-breakers correctly evaluated, including Block B<8 triggered-but-non-binding and pledge correctly not-triggered-by-absence. History downgrade verified. Valuation half deferred to phase 3 (B10/B11 do not exist).
