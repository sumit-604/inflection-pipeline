PROCEED WITH FLAGS

# Gate recommendation (phase 1, evidence only)

This is the FTTCP go/no-go on the evidence stages alone. No valuation ran this phase. No entry zone, no destination PE, no decision, no Hurdle verdict appears here. Verdict rule 3 fired: FLAG-CASH is active, which lands the verdict at PROCEED WITH FLAGS.

## Verdict derivation

Selection rules applied in order:

1. REWORK check: no verifier CRITICAL, no source-fidelity finding, no acceptance rate below 60, overall 62 is not below 60. REWORK does not fire.
2. INSUFFICIENT EVIDENCE check: the annual report ran (stages 2 and 3 both completed), Gate 0 ran on both screening data and results. No decision-relevant pillar gap forces this. Does not fire.
3. FLAG-CASH is active. Determination is GROWTH-INDUCED, which routes to PROCEED WITH FLAGS (not the INDETERMINATE cap of PROCEED WITH CAVEATS). FLAG-PROMOTER is not active. This rule fires.

Confidence band interaction: overall confidence 62 sits in the 60-74 band, which downgrades a PROCEED-family verdict one level. A clean-evidence PROCEED would fall to PROCEED WITH CAVEATS on the band alone. The active FLAG-CASH takes it one step further to PROCEED WITH FLAGS. REWORK is not reached because there is no CRITICAL finding and overall confidence holds at or above 60. Band and flag point the same way; the flag is the binding step.

## Confidence delta

| Component | Score | Source | Note |
|---|---|---|---|
| Numerical acceptance | 89 | B12a | 47 numbers audited, 0 CRITICAL, 0 source-fidelity findings after one permitted re-invoke |
| Red-flag coverage | 62 | B12b | binding floor: 5 concall red flags B05 missed, 1 MAJOR |
| Framework adherence | 96 | B12c | Gate 0 + Emerging Moat portion only; valuation adherence deferred to phase 3 |
| Peer utilisation | 100 | B12d | 13 of 13 peers used substantively |
| Overall | 62 | confidence.yaml | min of the four components |

Weakest component: red-flag coverage at 62. Verifier B found five concall red flags that stage 5 missed, the most material being the Rs 804 Cr in-quarter prepayment that nets to only about Rs 220 Cr of net-debt reduction. This is a management-communication caveat, not a numerical or framework failure, so it lowers confidence without forcing a rework.

## FLAG-CASH (active)

Determination: GROWTH-INDUCED.

Basis:
- Current ratio 0.85 in FY26, below 1.0 and down from 0.90 in FY25; 0.74 on the framework formula, 0.86 on the annual report's own consolidated figure (B02, Note 61 standalone / Note 56 consol).
- Free cash flow negative in both years, moving from minus Rs 398 Cr (FY25) to minus Rs 54 Cr (FY26); the strain is capex-driven, with gross fixed assets rising Rs 4,377 Cr to Rs 5,206 Cr on a Bio-MEG and ethylene-oxide buildout, capex 5.3 times depreciation (B01 block_b_trend; B03 flags).
- Operating cash flow held above twice reported profit across ten years (CFO/PAT 2.06x, B01); the FY26 reading of 2.72x is partly a one-time inventory drawdown of about Rs 281 Cr that will not repeat (B03 flags).
- Net capital turnover is structurally negative but driven by short-term borrowings inside current liabilities, not genuine negative trade working capital (B04 irrelevant_ratios).
- Receivables are stable: over-6-months bucket 4.93% versus 4.94% flat, no single-customer concentration (B02 receivables_trend).
- Rating agency verbatim (the only rating-agency quote in the corpus): "CARE Ratings Limited... kept the rating unchanged for the long-term/short-term bank facilities... However, Placed on Rating Watch with Developing Implications (RWD), owing to restructuring actions being taken by the Company." (B03, Board's Report [[page 21]]). A CARE working-capital-specific verbatim is NOT FOUND in the extracted corpus; the CARE report on file (6 Mar 2026) confirms only the preferential-issue use of proceeds.

Why GROWTH-INDUCED, not STRUCTURAL: the negative FCF traces to a now-completing capex programme, not to weak collections or margins; receivables are flat and cash conversion is strong on a multi-year basis. Why not INDETERMINATE: the drivers are named and evidenced, so the flag does not cap at PROCEED WITH CAVEATS.

Falsification metric (single quarterly print): FY27 CFO/PAT below 1.5x with the current ratio falling further below 0.85, in a quarter where capex has dropped below 2 times depreciation. If cash conversion stays weak after the capex programme winds down, the flag reclassifies STRUCTURAL. Watch the next balance sheet and cash-flow statement.

## FLAG-GATE0 (active)

Core score 40 out of 100, AVERAGE (corrected from 42 after the B12c A1 re-band; grand total 44 out of 160). Depressor detail (B01, B12c):
- A1 median ROCE 11.96% sits in the 10 to 14.9% band, scored 1 (was mis-scored 3); Block A corrected 9 to 7.
- Corrected Block A of 7 is below 8, which fires deal-breaker 1 (max grade GOOD). Outcome does not change because AVERAGE already sits below GOOD; the deal-breaker should be recorded.
- Sub-1.0 current ratio and capex-driven negative FCF in both data-covered years.
- Below-top-band revenue growth; PAT CAGR flattered by a depressed FY17 base and an FY22 other-income outlier.
- Block E tests E1 to E3 scored 0 on absent promoter and pledge filings, not a confirmed misalignment signal.
- The grade describes trailing consolidated history that ends 1 September 2026; three entities inherit pieces on different bases.

## FLAG-PROMOTER (not active)

B08 verdict is TRUSTWORTHY (scorecard 5 clean / 5 caution / 0 red, no deal-breakers, 0% pledge). The flag does not fire. Carry one open item: the Rs 20.4 Cr NSEL-related legacy receivable, carried as good 13 years after the 2013 default, with the FY26 notes internally inconsistent on whether the balance is still open (B08 adverse_findings; B02 finding 13).

## Contradicted claims (peer stage, priority monitoring)

- Uttar Pradesh market volume 15 lakh to 23 to 25 lakh cases per month: marked CONTRADICTED against Globus (near a crore cases a month), but RECONCILABLE. India Glycols' 23 to 25 lakh is an IMFL-only slice; its own ~90 lakh IMIL figure sums to ~1.1 crore, matching Globus's ~1 crore total. Segment-scope mismatch, not a factual conflict (B06 contradicted; B12b finding).
- OMC ethanol allocation decline ~22% YoY: direction corroborated by Globus and Triveni, magnitude unconfirmed by any peer. Treat the direction as verified, the number as unverified; check a primary OMC allocation source before use (B06 partially_verified).
- Bio-glycols/MEG realisation decline ~30%: structurally unverifiable, no peer in the set makes glycols; needs chemicals-sector peers not provided (B06 unverifiable).

## Monitorables and triggers

1. Ethanol Supply Year 2026-27 OMC allocation figure, due around November 2026: watch for further volume erosion below the FY26 15.43 crore litres. Source: PPAC / MoPNG tender results. Tests whether the 22% cut is the full extent of the bio-fuel headwind.
2. BSPC / bio-glycols realisation per MT, next quarterly segment disclosure: watch for a move up from the ~Rs 19,280 per MT FY26 run-rate. Tests whether the residual chemicals entity's 30% price decline is bottoming, which is the whole residual-entity thesis.
3. Current ratio and CFO/PAT, next balance sheet and cash-flow statement: watch for the current ratio falling below 0.85 with CFO/PAT under 1.5x once the inventory drawdown does not repeat. This is the FLAG-CASH falsifier.
4. FX hedge notional and open FX position, next quarterly sensitivity note: watch for re-hedging above USD 3.73 million or continued silence. Tests whether the 92% hedge collapse is being reversed or is an ongoing lapse.
5. NCLT effectiveness and the separate listings of IGL Spirits and Ennature Bio Pharma, September 2026 onward: watch for the effective-date notification and opening balance sheets. Governs whether the three-entity split completes on schedule.
6. Credit rating action off "Watch, Developing Implications" post-demerger, FY27: watch for a formal CARE action. Tests whether the standalone entities clear the restructuring overhang.
7. IGL Spirits FY27 EBITDA run-rate against the stated >Rs 500 Cr target (Q1 FY27 already ~Rs 120 Cr): watch quarterly. Tests the highest-conviction near-term growth trigger; kill signal is IMFL volume growth stalling below double digits.
8. NSU / Performance Chemicals revenue against the Rs 150 Cr FY27 guide: watch quarterly. A third straight period capped near 40% growth kills the scale-up trigger.

## Falsification line

The single most damaging next-quarter print: BSPC / bio-glycols realisation per MT falling again below the FY26 ~Rs 19,280 run-rate. That is the earnings base a continuing holder keeps after the demerger, and another leg down on price would confirm the residual entity is still losing a growing market on realisation, not volume.

## Publish check

No publish candidate this analysis.
