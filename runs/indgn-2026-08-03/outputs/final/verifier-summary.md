# Verifier summary, phase 1 + phase 3 valuation

## Confidence delta and acceptance rates

| Component | Score | Verifier | Acceptance rate |
|---|---|---|---|
| Numerical acceptance | 100 | A (B12a) | 100 |
| Red flag coverage | 79 | B (B12b) | 65 (any-form 94, full-catch 65) |
| Framework adherence | 93 | C (B12c: Gate 0 + Emerging Moat 90, valuation 97) | 90 / 97 |
| Peer utilisation | 100 | D (B12d) | 80 |
| Overall | 79 | min of four | band 75-89 normal, no downgrade, no REWORK |

Framework adherence is rule-weighted across both halves of Verifier C: phase-1 Gate 0 + Emerging Moat 47/52 (90) plus phase-3 valuation adherence 35/36 (97), giving (47+35)/(52+36) = 82/88 = 93.

REWORK gate: 0 Verifier A CRITICAL, source fidelity PASS; no acceptance rate below 60 (A 100, B 65, C gate0+EM 90, C valuation 97, D 80); forced_rework false.

## Findings, sorted CRITICAL then MAJOR then MINOR

No CRITICAL findings from any verifier.

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| B | B05 4D / 1C vs Oct meet p.6, Q2 p.12, Q3 p.7 | MISSED: BioPharm consolidated at GROSS revenue (gross ~$38.1m vs net ~$29.2m) inflates INR headline growth, dilutes blended margin; never framed as a revenue-quality issue. The one fully missed flag; carried as contradicted claim + monitorable. |
| B | B05 guidance log / 1C vs Oct meet p.8 | UNDER-WEIGHTED: BioPharm 3-year revenue stagnation around $40m gross against a 15-20% earnout growth assumption; integration/turnaround execution risk. |
| B | B05 2C / 2B vs Q4 p.8 | UNDER-WEIGHTED: reported -1.4% to adjusted +12.7% FY26 PAT bridge leans on retroactive Ind AS 109 hedge reclassification plus TCPA add-back; B05 logged the hedge change only as a positive. |
| C (gate0) | B01 Block F, M4 Customer Stickiness | M4 scored 3 while M10 scored 1 on identical evidence (0 decline years, receivable days +42.5). Consistent conservative read = 1, which moves moat_class MODERATE to THIN and classification GOOD+ to GOOD. Operator-resolvable, evidence gate invariant. |
| D | B06 Part 3, IKS Health row Q2 FY26 (Nov 2025) | Table row credits Nov 2025 with the 24% rev vs 1.5% headcount data point actually in Feb 2026; Nov 2025's real analog is 17% rev vs ~3% headcount. Part 1 body text attributes correctly; only the table row is wrong. |
| D | B06 Part 3, IKS Health row Q3 FY26 (Feb 2026) | Table row credits Feb 2026 with the RPE non-disclosure exchange actually in Nov 2025. Matched swap with the row above. Body text correct; only the table row wrong. |
| D | B06 Part 3, Sagility row Q1 FY27 (Jul 2026) | Table row credits Jul 2026 with long-sales-cycle confirmation not located in that transcript; the real Q7 evidence is correctly anchored to the Feb 2026 call in Part 1. Payer-cost-pressure contribution on the same row is genuinely supported. |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| C (valuation) | B10 line 224/222; B11 YAML line 399 | Units label: combined contingent liability written "Rs 1,531 cr"; correct is Rs 1,531 mn = Rs 153 cr (TP 1,114 mn + TCPA 417 mn). 38.2% of PAT and 21.2% of PBT confirm the mn/cr magnitude. Decision-neutral, never enters pillars/destination PE/Hurdle/entry. B14 caught and corrected it. |
| B | B05 3C vs Q3 p.8, Q4 p.8 | UNDER-WEIGHTED: OCF/PAT 154%/162% headline mechanically inflated by rising non-cash amortization; verdict called it genuine strength (DSO 72->63 is real). |
| B | B05 3D vs Q3 p.5/p.9 | UNDER-WEIGHTED: renewal price concessions as first AI-driven price give-back in Indegene's own book, framed only as net positive. |
| B | B05 2B vs Q3 p.15, Q4 p.10 | UNDER-WEIGHTED: Q3 "150bps behind us, will not enhance" assurance versus continued non-recovery pushed to H2 FY27 plus fresh go-live costs. |
| C (gate0) | B01 Block F, M10 Switching Costs | M10 = 1; strict band read gives 0. Immaterial, below 3 either way. |
| C (gate0) | B01 Block A, ROCE derivation | ROCE computed with proxy capital-employed basis FY19-24 instead of screener's own ROCE; band outcome not obviously changed; number match owned by Verifier A. |
| C (emoat) | B07 Section 5, rows A4 and G1 | Raw = 2 on ML-labelled rows; per stated matrix ML = 1. Recomputed em_score 30 vs 31; classification STRENGTHENING unchanged. |
| C (emoat) | B07 Section 3 prose count | Prose grouping of Strong rows loose; count of 9 correct; cosmetic. |
| D | B06 Part 2A | eClerx Jul 2025 quote attributed to Vasa's Q&A is actually spoken by Kapil Jain answering Vasa; low-materiality labelling ambiguity, not a location error. |

## Phase-3 valuation adherence audit (B12c-valuation)

Framework adherence on the valuation half scored 97 (35 of 36 rule-checks clean plus 1 decision-neutral MINOR). All pillar, RRM, Hurdle, entry-divisor, decision-mapping and carry-discipline checks PASS. Key confirmations: Pillar 1 formula 0.5x25.8+7.5=20.4x within [9,24]; Route A governs, B suppressed per single-credit; Pillar 2 1.30x consistent with GROWTH INDUCED; Pillar 3 +5x within +6x cap; UA correctly NOT applied (institutions 18.66% fails <3%); sector cap 45x Platform/SaaS/IT, 31.5x non-binding; RRM 1.06 reading correct at 28.1x; divergence 12.1% under 15%; Hurdle 2.12 >= Tier B 1.728; SFL EPS basis consistent FORWARD on numerator and denominator; forward-PE-at-exit convention held (FY29 exit, destination on FY30 EPS). Destination PE 31.5x additive / 28.1x RRM and decision BUY (on-dips) Medium staged reproduced exactly. The only finding is the units-label MINOR above.

### CLEAN

Verifier A (B12a) checked 38 numbers: 37 exact matches plus 1 legitimate basis difference (EBITDA Rs 619.0 Cr computed excluding ESOP vs Rs 624.7 Cr stated including it, 0.9% variance). Zero mismatches, zero ANCHOR NOT FOUND, zero UNANCHORED material figures. Source fidelity gate PASS across all six source categories (Annual Report FY26, FY26 Results, Q1 FY27 Investor Presentation, Shareholding Jun 2024-Jun 2026, concalls Q2-Q4 FY26 + Q1 FY27, peer concalls x4 companies / 12 transcripts).
