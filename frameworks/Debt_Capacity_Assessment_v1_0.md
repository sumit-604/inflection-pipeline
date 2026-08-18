# DEBT CAPACITY ASSESSMENT v1.0

*Version 1.0 | 13 August 2026 | Damodaran integration, operator directive 13-Aug-2026. New standalone section. Runs immediately BEFORE FTTCP v2.0 and after Role 5.5 (Downstream Signal Identification). Its output block is consumed by FTTCP Part B Module B7 and by Role 1. It establishes the maximum debt the company is capable of carrying, judged from the PAST, before any transition analysis begins.*

## WHY THIS SECTION EXISTS

Every forward thesis on a levered business rests on an unstated assumption: that the company can carry the debt it already holds and any debt the growth plan will add. That assumption is usually left implicit and the analysis moves straight to growth. This section makes it explicit and it does so before FTTCP, so the transition work runs on a business whose balance sheet has already been judged solvent on its own history.

The judgment here is backward only. It asks what coverage this company has actually sustained through a normal year, computes the debt that coverage supports on mid-cycle operating income, and compares that ceiling to the debt on the books today. It does not forecast. It does not assign a credit rating. It does not estimate a probability of failure. Those belong to parked items 3.3 and 3.4 and stay parked. This section produces one number, one trend, and one verdict, and hands them forward.

## THE PLACEMENT

```
Role 5 (concall) → Role 5.5 (Downstream Signal Identification) →
DEBT CAPACITY ASSESSMENT (this section) →
FTTCP v2.0 → Market-Implied Assumptions → Role 1 → Role 2 → Role 3
```

Debt Capacity runs first because FTTCP Module B7 (Post-Deleveraging Earnings Picture) and Role 1 both consume its output. A business flagged BREACH here carries that flag into every downstream stage. A business flagged COMFORTABLE frees FTTCP to read a deleveraging path as a genuine transfer of value from lenders to shareholders rather than a rescue.

## STEP 1 — MID-CYCLE DEBT CAPACITY

Maximum sustainable debt is computed on normalized operating income, never on a trough year and never on a peak year. A trough understates capacity and screens out solvent businesses at the bottom of a cycle. A peak overstates it and waves through businesses that only cover their interest when everything is going right. Mid-cycle is the only honest base.

**Normalized (mid-cycle) EBIT.** Take the average EBIT across a complete cycle from audited filings. Where the sector is flagged cyclical, use the full-cycle average consistent with the FTTCP v2.0 cyclical margin rule. Where the business is not cyclical, use a representative normal year or a multi-year average that excludes any one-off distortion. State the years used and the figure in ₹ Crores. Strip non-operating income from EBIT so the coverage the company earns is the coverage its operations earn, not the coverage its treasury book earns.

**Sustained interest coverage.** State the interest coverage (EBIT ÷ interest) the company has actually held through its history, read off the coverage trend line in Step 2. This is evidence, not a target. A business that has run at 3x through a normal year is judged at 3x. A business that has never cleared 2x is judged there.

**The capacity number.** Maximum sustainable debt is the debt level at which mid-cycle EBIT still clears the chosen coverage threshold. The default threshold is 3x, which is a serviceable investment-grade coverage for a small or mid-cap operating business. Where the historical record shows the company has sustained a different level through a normal year, use the historical level and say so. The formula:

**Maximum debt at [3x] coverage on mid-cycle EBIT = Mid-cycle EBIT ÷ (coverage threshold × cost of debt).**

Cost of debt is the company's actual blended borrowing rate from the filings, in percent. The result is a rupee debt ceiling. Round to the nearest ₹ Crore and show every input.

State the three numbers plainly:

- Maximum debt at [3x] coverage on mid-cycle EBIT = ₹___ Cr
- Current debt (latest audited net debt, or gross debt where the cash is restricted or non-operating) = ₹___ Cr
- Headroom or breach = ₹___ Cr (capacity minus current), and the same as a percentage of capacity

Headroom is capacity minus current debt. A positive number is headroom. A negative number is a breach, and a breach is flagged, never averaged into comfort by a strong growth story.

## STEP 2 — COVERAGE TREND LINE

Capacity computed on one mid-cycle figure hides the direction of travel. A company at 2.5x coverage climbing toward 4x is a different balance sheet from a company at 2.5x sliding toward 1.5x, even when the point estimate matches. Build the five-year series and read the direction.

| Fiscal Year | EBIT (₹ Cr) | Interest (₹ Cr) | EBIT / Interest | Notes |
|---|---|---|---|---|
| FY[Y-4] | | | | |
| FY[Y-3] | | | | |
| FY[Y-2] | | | | |
| FY[Y-1] | | | | |
| FY[Y-0] (latest) | | | | |

**Coverage trend verdict:** IMPROVING / STABLE / DETERIORATING.

- **IMPROVING**: coverage rising across the series, most recent two years above the five-year average.
- **STABLE**: coverage within a narrow band across the series with no clear direction.
- **DETERIORATING**: coverage falling across the series, most recent two years below the five-year average. A deteriorating trend is a flag even when current coverage still clears the threshold, because the direction is what matters for a forward hold.

## STEP 3 — OUTPUT BLOCK

This block is the deliverable. It is consumed by FTTCP Part B Module B7 and by Role 1. Reproduce it verbatim in the run folder.

```
DEBT CAPACITY OUTPUT
Mid-cycle EBIT (₹ Cr, years used): ___
Coverage threshold applied: ___x   (default 3x; state historical level if used)
Cost of debt (blended, %): ___
Maximum sustainable debt (₹ Cr): ___
Current debt (₹ Cr): ___
Headroom (₹ Cr): ___   Headroom (% of capacity): ___%
Coverage trend (5-yr): IMPROVING / STABLE / DETERIORATING
VERDICT: COMFORTABLE / STRETCHED / BREACH
```

**Verdict rule (one line):**

- **COMFORTABLE**: current debt is at or below capacity with headroom of 20 percent or more, and the coverage trend is IMPROVING or STABLE.
- **STRETCHED**: current debt is at or below capacity but headroom is under 20 percent, OR headroom is positive but the coverage trend is DETERIORATING.
- **BREACH**: current debt exceeds mid-cycle capacity. The business does not cover the chosen threshold on a normal year. This is flagged prominently and carried into FTTCP and Role 1.

The verdict never halts a run. It propagates. A BREACH company still goes through FTTCP and valuation, with the breach named at every stage and priced through the required return and the deleveraging path, not hidden.

## WORKED-EXAMPLE PLACEHOLDER

The table below is a shape, not a live company. Fill it from audited filings on the name under analysis.

| Line | Value |
|---|---|
| Mid-cycle EBIT (FY__ to FY__ average) | ₹___ Cr |
| Cost of debt (blended) | ___% |
| Coverage threshold applied | 3x |
| Maximum sustainable debt = EBIT ÷ (3 × cost of debt) | ₹___ Cr |
| Current net debt (latest audited) | ₹___ Cr |
| Headroom (capacity − current) | ₹___ Cr |
| Headroom as % of capacity | ___% |
| 5-yr coverage: FY-4 / FY-3 / FY-2 / FY-1 / FY-0 | __x / __x / __x / __x / __x |
| Coverage trend | IMPROVING / STABLE / DETERIORATING |
| **Verdict** | **COMFORTABLE / STRETCHED / BREACH** |

Illustrative arithmetic, numbers invented for shape only: mid-cycle EBIT ₹120 Cr, cost of debt 9 percent, threshold 3x gives maximum sustainable debt of ₹120 Cr ÷ (3 × 0.09) = ₹444 Cr. Current net debt ₹300 Cr gives headroom of ₹144 Cr, or 32 percent of capacity. If the five-year coverage series reads 2.1x, 2.4x, 2.8x, 3.3x, 3.9x, the trend is IMPROVING and the verdict is COMFORTABLE.

## WHAT THIS SECTION DELIBERATELY DOES NOT DO

- No synthetic credit rating. Parked item 3.3.
- No probability of default or truncation probability. Parked item 3.4.
- No forward projection of EBIT or debt. Forward paydown is modelled in FTTCP Module B7, which consumes this output; it is not re-derived here.
- No liquidity haircut. Parked item 3.7, awaiting operator sign-off.

## VERSION HISTORY

| Version | Date | Changes |
|---|---|---|
| 1.0 | 13-Aug-2026 | `[v1.0: new standalone Debt Capacity Assessment section, runs before FTTCP — Damodaran integration, operator directive 13-Aug-2026]` Initial version. Mid-cycle debt capacity on normalized EBIT at a default 3x coverage threshold; five-year coverage trend line; output block (current vs capacity, headroom %, coverage trend, one-line verdict COMFORTABLE / STRETCHED / BREACH) consumed by FTTCP Part B Module B7 and Role 1; worked-example placeholder table. Synthetic ratings and failure probabilities deliberately excluded (parked 3.3, 3.4). |
