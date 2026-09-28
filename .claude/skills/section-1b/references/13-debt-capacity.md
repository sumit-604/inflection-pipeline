# Chunk 13. Debt Capacity Assessment v1.0

Loaded by: consumed by Role 1 (consumption clause; Section 3 EV bridge via FTTCP Module B7) and by FTTCP Part B Modules B1 and B7. Runs in claude.ai immediately before FTTCP and after Role 5.5. No pipeline stage loads it today; when absent, Role 1 names the gap and never estimates capacity.
Sources in force: Debt_Capacity_Assessment_v1_0.md; Master v3.7 Role 1 consumption clause; FTTCP v2.3 Modules B1, B7.

## Purpose and limits

The judgment is backward only. It asks what coverage the company has sustained through a normal year, computes the debt that coverage supports on mid-cycle operating income, and compares that ceiling with debt on the books today. It produces one number, one trend and one verdict.

It does not forecast EBIT or debt (forward paydown lives in Module B7), assign a synthetic credit rating (parked item 3.3), estimate a probability of default (parked item 3.4), or apply a liquidity haircut (parked item 3.7, awaiting operator sign-off).

## Placement

Role 5 → Role 5.5 → **Debt Capacity Assessment** → FTTCP → Market-Implied Assumptions → Role 1 → Role 2 → Role 3.

## Step 1: mid-cycle debt capacity

- **Normalized (mid-cycle) EBIT.** Never a trough year, never a peak year. Take the average EBIT across a complete cycle from audited filings. For a sector flagged cyclical, use the full-cycle average consistent with the FTTCP cyclical margin rule. For a non-cyclical business, use a representative normal year or a multi-year average that excludes one-off distortion. State the years used and the ₹ Cr figure. Strip non-operating income so the coverage measured is what operations earn.
- **Sustained interest coverage.** The EBIT ÷ interest the company has actually held, read from the Step 2 trend line. Evidence, not a target.
- **Coverage threshold.** Default 3x (serviceable investment-grade coverage for a small or mid-cap operating business). Where the record shows a different level sustained through a normal year, use the historical level and say so.
- **Formula:** Maximum debt at [threshold] coverage on mid-cycle EBIT = **Mid-cycle EBIT ÷ (coverage threshold × cost of debt)**. Cost of debt = the actual blended borrowing rate from the filings, in percent. Round to the nearest ₹ Crore and show every input.

State three numbers:

- Maximum debt at [3x] coverage on mid-cycle EBIT = ₹___ Cr
- Current debt (latest audited net debt, or gross debt where cash is restricted or non-operating) = ₹___ Cr
- Headroom (capacity − current) = ₹___ Cr, and as % of capacity. A negative number is a breach, flagged and never averaged into comfort by a growth story.

## Step 2: coverage trend line

| Fiscal year | EBIT (₹ Cr) | Interest (₹ Cr) | EBIT / Interest | Notes |
|---|---|---|---|---|
| FY[Y-4] | | | | |
| FY[Y-3] | | | | |
| FY[Y-2] | | | | |
| FY[Y-1] | | | | |
| FY[Y-0] (latest) | | | | |

- IMPROVING: coverage rising across the series, the most recent two years above the five-year average.
- STABLE: coverage within a narrow band with no clear direction.
- DETERIORATING: coverage falling, the most recent two years below the five-year average. A flag even when current coverage still clears the threshold.

## Step 3: output block (reproduce verbatim in the run folder)

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

Verdict rule:

- **COMFORTABLE:** current debt at or below capacity with headroom of 20% or more, AND trend IMPROVING or STABLE.
- **STRETCHED:** at or below capacity but headroom under 20%, OR headroom positive but trend DETERIORATING.
- **BREACH:** current debt exceeds mid-cycle capacity.

The verdict never halts a run. It propagates. A BREACH name still goes through FTTCP and valuation, with the breach named at every stage and priced through the required return and the deleveraging path.

## How downstream uses it

- Role 1 reads the verdict; it does not re-derive capacity.
- Module B1: a STRETCHED or BREACH business cannot fund new-reinvestment growth with new debt; growth must come from utilization ramp or internal cash, or it fails.
- Module B7: models the paydown schedule, the interest saving to PAT, and Year 3 equity = exit EV − projected Year 3 net debt. Where the verdict was BREACH, the schedule must show the business returning inside mid-cycle capacity, or the deleveraging thesis fails and is flagged to Role 3.
- Role 1 Section 3 EV/EBITDA bridge subtracts the B7 Year 3 net debt.

Illustration from the source file (numbers invented for shape only): mid-cycle EBIT ₹120 Cr, cost of debt 9%, threshold 3x → capacity ₹120 ÷ (3 × 0.09) = ₹444 Cr; net debt ₹300 Cr → headroom ₹144 Cr (32%); coverage 2.1x, 2.4x, 2.8x, 3.3x, 3.9x → IMPROVING → COMFORTABLE.
