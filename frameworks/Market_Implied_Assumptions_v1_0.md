# MARKET-IMPLIED ASSUMPTIONS v1.0

*Version 1.0 | 13 August 2026 | Damodaran integration, operator directive 13-Aug-2026. New standalone section. Runs immediately AFTER FTTCP v2.0 and immediately BEFORE Role 1. Its output block is consumed by Role 1 Section 1 and by the valuation conclusion. Before we value the business, we state what the current price already assumes about it.*

## WHY THIS SECTION EXISTS

A valuation built in isolation tells you what a business is worth. It does not tell you whether the market already agrees. The gap between the two is the entire trade. A business worth ₹800 a share is a buy at ₹400 and a sell at ₹1,200, and the number ₹800 says nothing about which one you are looking at. This section fixes that by reading the price backward before Role 1 reads the business forward.

The discipline is simple and it runs in one direction only. Take the current market price as given. Ask what growth, what margin, and what terminal quality that price already embeds at a reasonable exit multiple. Then, when Role 1 produces its own forward view, the operator can see at a glance whether the price is asking for more than the evidence supports, the same as the evidence, or less. When the price already assumes the bull case, the transition is priced and we are late. When the price assumes stagnation and the evidence shows a firing transition, the spread is the opportunity.

## THE PLACEMENT

```
FTTCP v2.0 → MARKET-IMPLIED ASSUMPTIONS (this section) → Role 1 → Role 2 → Role 3
```

This section runs after FTTCP so it can use FTTCP's operating EPS (Module B4) as the base earnings figure, and before Role 1 so its output is on the table when the valuation begins. It reads the price; it does not judge the business. The judging is Role 1's job, and keeping the two separate is what stops the valuation from quietly anchoring on the current price.

## STEP 1 — REVERSE-ENGINEERED GROWTH

State the EPS CAGR the current market price (CMP) implies at a reasonable exit multiple, and show the algebra.

The price CAGR identity over a three-year hold is:

**Price CAGR = EPS CAGR × (Exit PE ÷ Entry PE) ^ (1/3)**

Rearranged to solve for the growth the price is paying for, hold the exit multiple at a reasonable level and set the target price CAGR to the operator's hurdle. Two readings are useful and both should be shown.

- **Reading 1 — growth implied at a flat multiple.** Assume the exit PE equals the current PE (no re-rating, no de-rating). Then price CAGR equals EPS CAGR, and the market is paying the current price for whatever EPS CAGR would deliver the operator's required return. State that required EPS CAGR.
- **Reading 2 — growth implied at a reasonable exit multiple.** Use a reasonable exit PE for the sector and quality (state which, and why it is reasonable; do not use a round-number default). Solve for the EPS CAGR that makes the current price fair, meaning the EPS CAGR at which buying today returns exactly the cost of capital rather than the 25 percent hurdle. That is the growth the price embeds.

Show every input: CMP, operating EPS (from FTTCP Module B4), current PE, the exit PE used and its justification, and the solved EPS CAGR for each reading. Where a reasonable exit multiple cannot be set without Section 1B, say so and use the current PE reading as the primary figure, flagging that Role 1 will refine it.

## STEP 2 — THE MARKET'S IMPLIED STORY

Translate the implied growth into a plain-language story of what the price embeds. Write four to six plain sentences, each stating one embedded assumption in words a reader can check against the evidence. Use the form:

**"At ₹___, the market is assuming ___."**

Cover, at minimum:

- The revenue growth the price embeds, as a rate and in plain words.
- The margin level the price embeds (does it assume margins hold, expand, or compress).
- The terminal quality the price embeds (does the price assume the business stays this good forever, fades to industry, or keeps improving).
- Whether the price embeds any re-rating, or a flat multiple, or a de-rating.

Keep the sentences numbers-first and free of adjectives. The point is a reader can hold each sentence against the FTTCP evidence and the Role 1 projection and see whether it holds.

## STEP 3 — THE SPREAD STATEMENT

State the spread between what the price assumes and what the evidence supports, in one block:

**"Price assumes ___% growth; FTTCP evidence supports ___%. The spread is the trade."**

The evidence figure comes from FTTCP Part A (the forward transition verdicts) and Part B (the ROCE crossover and the funded growth path from Modules B1 and B2). The price figure comes from Step 1. Then read the spread:

- **Evidence above price:** the market is under-assuming the transition. The spread is the opportunity, subject to Role 1 confirming the fair value and the entry zone.
- **Evidence at price:** the transition is fairly priced. There may be no trade even on a good business.
- **Evidence below price, or price already at the bull case:** flag it plainly. **"The transition is priced, we are late."** A good business fully priced is not a buy, and this flag carries into the Role 1 conclusion so the value-versus-price statement there is honest.

## STEP 4 — OUTPUT BLOCK

Reproduce this block verbatim in the run folder. Role 1 Section 1 and the valuation conclusion consume it.

```
MARKET-IMPLIED ASSUMPTIONS OUTPUT
CMP: ₹___    Operating EPS (FTTCP B4): ₹___    Current PE: ___x
Reasonable exit PE used: ___x (basis: ___)
Implied EPS CAGR at flat multiple: ___%
Implied EPS CAGR at reasonable exit PE: ___%
Market's implied story (4-6 sentences): [reproduced from Step 2]
FTTCP evidence-supported growth: ___%
SPREAD: price ___% vs evidence ___%
Flag: OPPORTUNITY / FAIRLY PRICED / PRICED-WE-ARE-LATE
```

The flag never halts a run and never sets the verdict on its own. It is one input to the Role 1 value-versus-price statement and to the final decision, weighed against fair value, the margin of safety schedule, and the hurdle ratio.

## WORKED-EXAMPLE PLACEHOLDER

Illustrative arithmetic, numbers invented for shape only. CMP ₹500, operating EPS ₹20, current PE 25x. At a flat 25x exit, delivering the operator's 25 percent price hurdle needs 25 percent EPS CAGR, so the price at 25x is already asking for 25 percent compounding just to clear the hurdle. At a reasonable exit PE of 20x (a mild de-rating a maturing name should expect), the EPS CAGR that merely makes ₹500 fair at a 13.5 percent cost of capital is roughly 18 percent. If FTTCP evidence supports 22 percent funded growth with ROCE crossing the cost of capital in FY2, evidence sits above the fair-value growth and near the hurdle growth: a live but not generous opportunity, for Role 1 to size. If FTTCP evidence supported only 12 percent, the flag reads PRICED-WE-ARE-LATE.

## VERSION HISTORY

| Version | Date | Changes |
|---|---|---|
| 1.0 | 13-Aug-2026 | `[v1.0: new standalone Market-Implied Assumptions section, runs after FTTCP and before Role 1 — Damodaran integration, operator directive 13-Aug-2026]` Initial version. Reverse-engineered growth (flat-multiple and reasonable-exit-PE readings, algebra shown), the market's implied story (4-6 plain sentences in the "At ₹___, the market is assuming ___" form), the spread statement ("price assumes __% ; evidence supports __% ; the spread is the trade", with the priced-we-are-late flag), and an output block consumed by Role 1 Section 1 and the valuation conclusion. Uses FTTCP Module B4 operating EPS as the base earnings figure. |
