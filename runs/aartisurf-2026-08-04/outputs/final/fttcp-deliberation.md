# FTTCP DELIBERATION RECORD: AARTI SURFACTANTS LTD (AARTISURF)

Run: runs/aartisurf-2026-08-04 | CMP Rs 523.0 | Market cap Rs 443 Cr | Run date 2026-08-04
Phase 2 (operator deliberation). First workup. NO-CONCALL MODE. Operator: Keerti Kaushik.

---

## FINAL VERDICT

**FTTCP composite +1 out of 8 → DEEP WATCH leaning AVOID.** Revenue STARTING +1, Margin STAGNANT 0, Cash STAGNANT 0, ROCE STAGNANT 0 (ROCE moved from DECLINING to STAGNANT on operator override, see below). Kernex cap not engaged, TRIM rule not engaged. Backward composite 1 positive of 4, BACKWARD FAIL.

The whole call turns on one print: Q2 FY27 operating margin. At or above 7.5% moves margin to STARTING and the composite to +2; back below 6% confirms the Q1 FY27 recovery as noise and the case weakens back toward AVOID.

**Operator verdict in own words:** not dictated as a verbatim line. The operator ruled the individual calls (ROCE to STAGNANT), approved the valuation base (12.2x additive, forward basis), and signed off ("I am signing off from here"). Recorded from the explicit rulings and sign-off; the verbatim-one-line gap is noted, consistent with the MAPMYINDIA / SFL / AURUM / VOEPL precedent.

---

## FINAL RULINGS (draft rulings as amended in review)

| # | Call | Final ruling | Confidence | Changed in review? |
|---|---|---|---|---|
| Window | Forward window | 3m / 6m / 12m (ROCE) | sure | no |
| Business type | Standard operating business, four standard transitions | sure | no |
| Workup | First workup | sure | no |
| Sector cap | Specialty chemicals 35x (corrected from manifest Pharma/CDMO 38x); non-binding | fairly sure | no |
| Rev backward | STAGNANT (3yr CAGR 12.6%) | fairly sure | no |
| Margin backward | COMPRESSING (about -507 bps over 2yr) | sure | no |
| Cash backward | FIRING on the letter of the rule; flatters the business | fairly sure | no |
| Cash nature | Not structural, not growth-induced: one-time working-capital release, non-repeatable | fairly sure | no |
| ROCE backward | DECLINING, not TEMPORARILY DEPRESSED | fairly sure | no |
| Rev forward | STARTING (+1) | fairly sure | no |
| Margin forward | STAGNANT (0), genuinely uncertain, swing call | genuinely uncertain | no |
| Cash forward | STAGNANT (0), catalyst NONE FOUND | fairly sure | no |
| **ROCE forward** | **STAGNANT (0)** | fairly sure | **YES, operator override (was DECLINING -1)** |
| Kernex cap | Not engaged | fairly sure | no |
| Composite | **+1 / 8, DEEP WATCH leaning AVOID** | fairly sure | changed via the ROCE override (was 0, AVOID) |
| Position | No starter at this price on transition evidence; price call belongs to Role 1 | fairly sure | no |
| UA | Not applied (Gate 0 core 55 < 60, EM 13.5 < 25) | sure | no |
| Tier | Tier A, hurdle 25% (FII+DII 0.08%) | sure | no |

---

## OPERATOR OVERRIDES

**Override 1. ROCE forward verdict: DECLINING to STAGNANT.**
- Draft determination: ROCE forward DECLINING (-1), composite 0, AVOID band. Basis: ROCE at 9.3% far below any premium threshold, fresh debt-funded capex dilutes the denominator near term, and the framework biases to DECLINING when torn.
- Operator ruling: "please keep ROCE stagnant, not declined." (The operator first ruled "keep ROCE at decline," then on reflection reversed to STAGNANT.)
- Operator reasoning, as developed in the exchange: the ROCE decline decomposes entirely into the margin. EBIT margin fell 7.81% FY24 to 3.40% FY26 while capital turnover ROSE from 1.86x to 2.46x (revenue up 45.6% on capital employed up 10%). ROCE is the margin's arithmetic shadow, not an independent capital-efficiency failure, so it should not be scored more negatively than margin, which is STAGNANT.
- Effect: composite 0 to +1; band AVOID to DEEP WATCH leaning AVOID; and Pillar 1 now draws current ROCE (the STAGNANT mapping), which is consistent with the approved 12.2x base computed off current ROCE.
- Analyst note carried to Role 3: the near-term capex denominator drag is real and unaddressed by this override; the devil's advocate should test whether ROCE prints flat or down over the next 12 months as the Rs 60 Cr debt-funded capex lands before it earns.

**Override 2. Destination PE base: additive track over the RRM governing default.**
- Draft determination: RRM track 8.5x is the more conservative track and, on the framework's own rule, governs the entry zone; additive track 12.2x presented alongside.
- Operator ruling: "so let's take a price-to-earnings of 12.2." The operator approved the additive-track 12.2x as the destination base, overriding the RRM-governs default.
- Effect: destination PE 12.2x (range 11.5x to 13.0x), about 44% above the RRM floor of 8.5x. Phase 3 fair values land higher than the conservative track would give, but still a de-rating from the current ~24x trailing-four-quarter / ~35x FY26-basic multiple.

**Override 3. Earnings basis: one-year-forward.**
- Operator ruling: "we will use the one-year forward multiples method."
- Reason (operator, implied by the selection): forward basis fits a mid-capex business whose current earnings sit in a margin trough.
- Analyst caution carried to Role 3 (not a change to the ruling): forward basis credits the same margin recovery the transition score marks STAGNANT and genuinely uncertain, so the devil's advocate MUST rebuild the return hurdle on a no-margin-recovery bear EPS. If the call clears only when the unproven recovery is fed into both the earnings and the multiple, it is a bet on the Q2 and Q3 FY27 margin prints and must be labelled that way (the INDGN 2026-08-03 double-credit lesson).

---

## CROSS-FAMILY GRADE

**Did not run.** The cross-family FTTCP grader (verifiers/fttcp_crossgrade.py) SKIPPED with exit 3: no GEMINI_API_KEY or GOOGLE_API_KEY configured in this environment. There is no independent third-family read on this FTTCP verdict, so FTTCP confidence is treated one notch below the phase-1 overall of 86. No CRITICAL rubric violation was raised because the check did not execute. Same environment limitation as SHYAMMETL and KCPSUGIND.

---

## OPERATOR-APPROVED VALUATION PILLARS (authoritative for Phase 3)

Phase 3 (stage 10 assembly, stage 11 valuation) MUST use this approved base and basis. It may not silently derive a different exit PE.

| Pillar / input | Approved value | Note |
|---|---|---|
| Pillar 1 ROCE | Current ROCE, statutory FY26 **9.30%** (year-end denominator; 9.72% on average) | ROCE forward verdict STAGNANT → FTTCP table maps to current ROCE |
| Pillar 1 normalization route (v3.5.1) | **NONE** | Route A fails (CWIP 12.8% of capital employed, under 20%); Route B barred (no invocation on a STAGNANT/DECLINING verdict). Statutory ROCE feeds Pillar 1 directly. |
| A. ROCE base PE | **12.2x** | 0.5 × 9.30 + 7.5 (Amendment 5), floor 9x cap 24x |
| Pillar 2 cash multiplier | **1.00x** | Volatile band (CFO/PAT ran 0.77x to 6.21x); not structural, so 0.65x does not apply; no growth offset (that applies only to the 0.80x band) |
| C. Quality-adjusted base | **12.2x** | A × B |
| Pillar 3 (3a+3b+3c) | **+0x** | 3a: only 1 of 4 criteria qualifies and grade C caps it; 3b: EM 13.5 below the 25 floor; 3c: no documented order book / contracted tenor |
| Strategic premium | **+0x** | No scarcity, weak pricing power; ROCE re-rating route barred (single-credit, and no recovery to credit) |
| ROCE recovery credited via | **Not credited** | No recovery; Strategic Premium route stays barred |
| F. Raw destination PE | **12.2x** | C + D + E |
| Undiscovered Alpha (F2) | **Not applied** | Quality qualifier fails (Gate 0 core 55 needs 60; EM 13.5 needs 25) |
| Sector cap (G) | **Specialty chemicals 35x** | Corrected from manifest Pharma/CDMO 38x; NON-BINDING at this destination |
| **H. Destination PE, APPROVED** | **12.2x (additive track)** | Range 11.5x to 13.0x at +/- 7.5%. Operator override of the RRM-governs default. |
| Destination PE, RRM track | 8.5x | Computed (12.2 × RRM 0.70, r=16%); NOT the chosen base |
| **Earnings basis, APPROVED** | **ONE-YEAR-FORWARD** | Multiple applied to year-forward EPS at exit; phase 3 builds the EPS ladder to the year after the exit year |
| Return tier | **Tier A, hurdle 25%**, divisor 1.953 | FII+DII 0.08%, under 3% |
| SHARED CATALYST flag | **YES** | Pithampur Dec-2026 commissioning is the single point of failure behind the revenue path, any margin operating leverage, and any ROCE recovery. Role 3 stress-tests it as one risk. |
| Concall gate | NOT CLEARED | No transcript; confidence materially reduced |

**Phase-3 authority note.** The ROCE forward verdict STAGNANT (operator override), the cash determination (one-time working-capital release, not repeatable; catalyst NONE), the destination base 12.2x additive, and the one-year-forward earnings basis are authoritative inputs at stage 10 and flow through valuation, thesis and devil's advocate. Where any earlier phase-1 determination conflicts, this record supersedes it.

---

## ACTIVE TRIPWIRES (into Phase 3 and monitoring)

1. Q2 FY27 operating margin at or above 7.5% (Reg 52(4) basis) moves margin to STARTING and composite to +2. Below 6% hardens the AVOID. **The decisive one.**
2. H1 FY27 CFO below zero, or falling with payables falling, moves cash to DECLINING and engages the Kernex cap.
3. Rs 18.50 Cr preference-share redemption due 19-Aug-2026 completed without new short-term borrowing.
4. Pithampur commissioning announced complete by 31-Dec-2026; slippage moves the ROCE catalyst to NONE and engages the cap.
5. Total debt to PBILDT toward CARE's below-2.5x expectation; above 3.5x triggers CARE's negative sensitivity.
6. Two-customer concentration above 71%, or any disclosed customer loss.
7. Pollution Control Committee matter beyond the Rs 17.4 lakh compensation order.

Falsification line for the whole forward case: Q2 FY27 operating margin printing back below about 6%, reverting toward the Q4 FY26 5.22% level.
