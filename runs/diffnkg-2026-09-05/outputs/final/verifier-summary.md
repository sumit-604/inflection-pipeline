# Diffusion Engineers (DIFFNKG) — Verifier Summary (Phase 1)

## Confidence delta and acceptance rates

| Verifier | Scope | Acceptance | Overall contribution |
|---|---|---|---|
| A (B12a, haiku) | Numerical fidelity, 21 numbers | 95.2% | numerical_acceptance 95.2 |
| B (B12b, opus) | Red flag coverage, 15 independent flags | 73% | redflag_coverage 73 |
| C (B12c, opus) | Framework adherence, Gate 0 + Emerging Moat | 89% | framework_adherence 89 |
| D (B12d, sonnet) | Peer utilisation, 6 transcripts | 100% | peer_utilisation 100 |

**Overall confidence delta: 73** (min of the four). Band 60 to 74. No verifier logged a CRITICAL. No acceptance rate fell below 60%. No forced REWORK. Binding component: red flag coverage at 73.

The valuation half of Verifier C is deferred to Phase 3 (B10/B11 did not run). The Business Understanding Narrative audit is out of scope this phase and is not a REWORK trigger.

## Findings, sorted by severity

### MAJOR

| Verifier | Location | Finding |
|---|---|---|
| B | B05 concall, earnings quality flag absent | Reported PAT flattered by non operating income: interest on about Rs 67 Cr unutilised IPO cash in deposits, a one time about Rs 5 Cr Singapore subsidiary dividend, and an associate profit spike. 9M FY26 consolidated PAT +49.55% versus EBITDA +12.60%. Thesis relevant to cash conversion and Role 1 FCF. Missed upstream. (Aug-2026 p7/p10-11/p17; Feb-2026 p5; May-2026 p4) |
| B | B05 concall, trigger framing; Aug-2026 PAGE 18 | Heavy engineering, the fastest growing segment and about 76% of the order book, is 70% new project build and 30% spares. Qualifies the repeat customer stickiness framing central to the transition and quality ladder thesis. Missed upstream. |
| C | B07 Section 5 scorecard (rows B1, B2, F1, F2, H2) | Invented a 0.85 evidence quality multiplier outside the defined 1.0 / 0.7 / 0.5 set, on 5 mixed evidence rows; no blending rule exists. Recompute at either governing tier leaves classification MODEST and below EM>=25. Outcome neutral, decision survives. |
| D | 06-peers.md Part 1, Q5 net read | Ador Fontech merger date "effective 25 September 2024" cited to Ador Nov 2024 call PAGE 8-9; no merger date appears anywhere in that transcript. Unanchored specific fact presented as source cited. |

### MINOR

| Verifier | Location | Finding |
|---|---|---|
| A | Gate 0 Section B1, Block A PAT row FY26 | Consolidated PAT FY26 stated 50.32 Cr (screener); AR p.191 shows 504.10 Mn = 50.41 Cr. 0.09 Cr variance (0.18%), likely rounding. Immaterial to ROCE/ROE verdicts and Gate 0 classification. source_fidelity: false. |
| B | B05 concall, Tejorup treatment; Feb-2026 PAGE 6 | Tejorup 10% stake priced on a soft basis (pre revenue, estimated PSO value / valuer reports). Captured as optionality and regulatory risk but not weighted as a capital allocation red flag. Partially caught, under weighted. |
| B | B05 concall, utilization narrative; Aug-2026 PAGE 20 | Units 2 and 3 at about 2 to 3% utilization, against the headline 85% utilization story used to justify expansion. Missed, minor. |
| C | B01 YAML history_downgrade | Set true, but the body states no history length tier downgrade applies at 8 years. Body and YAML contradict. Classification AVERAGE correct regardless. Fix: set history_downgrade false, keep IPO rebase point. |
| C | B07 Section 5 adjusted total / em_score | Stated adjusted column sums to 17.25 (rounds 17); report states 17.55, em_score 18. Both in the 12 to 24 MODEST band; classification unaffected. |
| D | 06-peers.md Part 2E, risk item 2 | Ador "65% of welding equipments are imported" quote cited PAGE 12; actual location PAGE 13. Quote text accurate. |
| D | 06-peers.md Part 1, Q3 row | GEE cobalt alloy business quote cited PAGE 13; actual location PAGE 14. Quote text accurate. |
| D | 06-peers.md Part 1, Q6 row | GEE RDSO / 10 year railway empanelment quote cited PAGE 3; actual location PAGE 4. Quote text accurate. |
| D | 06-peers.md Part 2A / Part 3 coverage map, Ador May 2026 | "Best order book" demand tone asserted without an inline page anchor in Part 1. |

## Verifier disagreement note

Verifier A run 1 raised a CRITICAL on the welding consumables TAM cited near Rs 1.6 bn. On re-check it was CLEARED (disposition FLAG CLEARED). The figure is a management cited number that the pipeline itself flagged (B05, "likely a units error") and contradicted about 100x through GEE Ltd (B06), and B09's actual TAM does not use it. It is not an analyst fabrication. Re-checked by a Verifier A re-invoke plus an orchestrator sanity check. Verifier A run 2 is the authoritative B12a at 95.2%.

Verifier D acceptance is 100% at the peer handling level: all 6 transcripts were correctly labelled and their citations are locatable. The merger date defect is a MAJOR finding on one sub claim, not a mislabelled peer.
