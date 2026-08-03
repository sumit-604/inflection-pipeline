# Verifier summary, phase 1

## Confidence delta and acceptance rates

| Component | Score | Verifier | Acceptance rate |
|---|---|---|---|
| Numerical acceptance | 100 | A (B12a) | 100 |
| Red flag coverage | 79 | B (B12b) | 65 (any-form 94, full-catch 65) |
| Framework adherence | 90 | C (B12c, Gate 0 + Emerging Moat only) | 90 |
| Peer utilisation | 100 | D (B12d) | 80 |
| Overall | 79 | min of four | band 75-89 normal, no downgrade, no REWORK |

REWORK gate: 0 Verifier A CRITICAL, source fidelity PASS; no acceptance rate below 60 (A 100, B 65, C 90, D 80); forced_rework false.

## Findings, sorted CRITICAL then MAJOR then MINOR

No CRITICAL findings from any verifier.

### MAJOR

| Verifier | Location | Note |
|---|---|---|
| B | B05 4D / 1C vs Oct meet p.6, Q2 p.12, Q3 p.7 | MISSED: BioPharm consolidated at GROSS revenue (gross ~$38.1m vs net ~$29.2m) inflates INR headline growth, dilutes blended margin; never framed as a revenue-quality issue. The one fully missed flag. |
| B | B05 guidance log / 1C vs Oct meet p.8 | UNDER-WEIGHTED: BioPharm 3-year revenue stagnation around $40m gross against 15-20% earnout growth assumption; integration/turnaround execution risk. |
| B | B05 2C / 2B vs Q4 p.8 | UNDER-WEIGHTED: reported -1.4% to adjusted +12.7% FY26 PAT bridge leans on retroactive Ind AS 109 hedge reclassification plus TCPA add-back; B05 logged the hedge change only as a positive. |
| C | B01 Block F, M4 Customer Stickiness | M4 scored 3 while M10 scored 1 on identical evidence (0 decline years, receivable days +42.5). Consistent conservative read = 1, which moves moat_class MODERATE to THIN and classification GOOD+ to GOOD. Operator-resolvable, evidence gate invariant. |
| D | B06 Part 3, IKS Health row Q2 FY26 (Nov 2025) | Table row credits Nov 2025 with the 24% rev vs 1.5% headcount data point that is actually in Feb 2026; Nov 2025's real analog is 17% rev vs ~3% headcount. Part 1 body text attributes correctly; only the table row is wrong. |
| D | B06 Part 3, IKS Health row Q3 FY26 (Feb 2026) | Table row credits Feb 2026 with the RPE non-disclosure exchange that is actually in Nov 2025. Matched swap with the row above. Body text correct; only the table row wrong. |
| D | B06 Part 3, Sagility row Q1 FY27 (Jul 2026) | Table row credits Jul 2026 with long-sales-cycle confirmation not located in that transcript; the real Q7 evidence is correctly anchored to the Feb 2026 call in Part 1. Payer-cost-pressure contribution on the same row is genuinely supported. |

### MINOR

| Verifier | Location | Note |
|---|---|---|
| B | B05 3C vs Q3 p.8, Q4 p.8 | UNDER-WEIGHTED: OCF/PAT 154%/162% headline mechanically inflated by rising non-cash amortization; verdict called it genuine strength (DSO 72->63 is real). |
| B | B05 3D vs Q3 p.5/p.9 | UNDER-WEIGHTED: renewal price concessions as first AI-driven price give-back in Indegene's own book, framed only as net positive. |
| B | B05 2B vs Q3 p.15, Q4 p.10 | UNDER-WEIGHTED: Q3 "150bps behind us, will not enhance" assurance versus continued non-recovery pushed to H2 FY27 plus fresh go-live costs. |
| C | B01 Block F, M10 Switching Costs | M10 = 1; strict band read gives 0. Immaterial, below 3 either way. |
| C | B01 Block A, ROCE derivation | ROCE computed with proxy capital-employed basis FY19-24 instead of screener's own ROCE; band outcome not obviously changed; number match owned by Verifier A. |
| C | B07 Section 5, rows A4 and G1 | Raw = 2 on ML-labelled rows; per stated matrix ML = 1. Recomputed em_score 30 vs 31; classification STRENGTHENING unchanged. |
| C | B07 Section 3 prose count | Prose grouping of Strong rows loose; count of 9 correct; cosmetic. |
| D | B06 Part 2A | eClerx Jul 2025 quote attributed to Vasa's Q&A is actually spoken by Kapil Jain answering Vasa; low-materiality labelling ambiguity, not a location error. |

### CLEAN

Verifier A (B12a) checked 38 numbers: 37 exact matches plus 1 legitimate basis difference (EBITDA Rs 619.0 Cr computed excluding ESOP vs Rs 624.7 Cr stated including it, 0.9% variance). Zero mismatches, zero ANCHOR NOT FOUND, zero UNANCHORED material figures. Source fidelity gate PASS across all six source categories.

## Logged verifier disagreement

| Field | Detail |
|---|---|
| Number/claim | FY26 Other Income |
| Verifier A first pass | CRITICAL MISMATCH, B01 Rs 51.7 Cr vs AR "Other income (net)" Rs 72.0 Cr (720 mn); source_fidelity flagged |
| Orchestrator check and re-run | Screener-vs-AR BASIS DIFFERENCE. B01 explicitly cited the screener Data_Sheet (Rs 51.7 Cr); the AR consolidated "Other income (net)" is Rs 72.0 Cr. Both correct at their own anchors. The FLAG-GATE0 "fall in other income" narrative holds on either basis (drag ~Rs 35-42 Cr FY25 to FY26). Decision neutral. |
| Disposition | FLAG CLEARED. Source re-check confirmed the number exists at a correct anchor (screener basis, correctly transcribed); AR basis differs by reclassification. Re-run acceptance 100%. |
| Re-checked by | orchestrator (direct AR grep) + Verifier A re-run |
