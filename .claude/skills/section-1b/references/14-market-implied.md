# Chunk 14. Market-Implied Assumptions v1.0

Loaded by: consumed by Role 1 Section 1 and the Section 4H-pre value-versus-price statement. Runs in claude.ai immediately after FTTCP and before Role 1. No pipeline stage loads it today; stage 11 resolves the recognition gap (below) from its own destination-PE work.
Sources in force: Market_Implied_Assumptions_v1_0.md; Master v3.7 Role 1 consumption clause and §4H-pre; FTTCP v2.3 Module B4; stage 11 override 13 and CLAUDE.md Transition Decision Matrix (recognition gap).

## Purpose

Before valuing the business, state what the current price already assumes about it. The discipline runs one way: take CMP as given and read it backward. It reads the price; it does not judge the business. Keeping the two apart stops the valuation from anchoring on the current price.

## Step 1: reverse-engineered growth

Price CAGR identity over a three-year hold:

**Price CAGR = EPS CAGR × (Exit PE ÷ Entry PE) ^ (1/3)**

Show both readings with the algebra:

- **Reading 1, flat multiple.** Exit PE = current PE. Price CAGR then equals EPS CAGR. State the EPS CAGR the operator's required return needs at the current price.
- **Reading 2, reasonable exit multiple.** Use a reasonable exit PE for the sector and quality, and state which and why. Never a round-number default. Solve for the EPS CAGR at which buying today returns exactly the cost of capital, not the 25% hurdle. That is the growth the price embeds.

Show every input: CMP, operating EPS (FTTCP Module B4), current PE, the exit PE used with its justification, and the solved EPS CAGR per reading. Where a reasonable exit multiple cannot be set without Section 1B, say so, use the flat-multiple reading as the primary figure, and flag that Role 1 refines it.

## Step 2: the market's implied story

Four to six plain sentences, numbers first, no adjectives, each checkable against the evidence. Form: **"At ₹___, the market is assuming ___."** Cover at minimum:

- the revenue growth the price embeds, as a rate and in words;
- the margin level it embeds (hold, expand, compress);
- the terminal quality it embeds (stays this good, fades to industry, keeps improving);
- whether it embeds a re-rating, a flat multiple or a de-rating.

## Step 3: the spread statement

**"Price assumes ___% growth; FTTCP evidence supports ___%. The spread is the trade."**

The evidence figure comes from FTTCP Part A (forward transition verdicts) and Part B (ROCE crossover and funded growth path, Modules B1, B2). The price figure comes from Step 1.

- Evidence above price → the market under-assumes the transition. The spread is the opportunity, subject to Role 1 confirming fair value and the entry zone.
- Evidence at price → fairly priced. There may be no trade even on a good business.
- Evidence below price, or price already at the bull case → **"The transition is priced, we are late."** This flag carries into the Role 1 value-versus-price statement.

## Step 4: output block (reproduce verbatim in the run folder)

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

The flag never halts a run and never sets the verdict on its own. It is one input to the value-versus-price statement and the final decision, weighed against fair value, the margin-of-safety schedule and the Hurdle Ratio.

## How Role 1 uses it

- Section 1 reads the block. Role 1 does not rebuild it.
- Section 4H-pre element 1, line two: what the price already assumes (the flag), what closes the gap, and when (chunk 06).

## Recognition gap (resolved at stage 11)

The signed mental model's recognition gap (Halt 1 dossier Part B4) resolves in Role 1 as the PE-gap check: does the current PE already sit at the TO rung's neighbourhood on the CLAUDE.md quality ladder? The destination-PE delta over the current PE is the re-rating engine. If the current PE already sits at the TO neighbourhood, the engine is spent and the return rides EPS CAGR alone; state this on the verdict card and in the Hurdle read. Resolve it inside the destination-PE and market-implied work; do not restructure the valuation math around it.

Illustration from the source file (numbers invented for shape only): CMP ₹500, operating EPS ₹20, current PE 25x. At a flat 25x exit, clearing a 25% price hurdle needs 25% EPS CAGR. At a reasonable 20x exit, the EPS CAGR that makes ₹500 fair at a 13.5% cost of capital is roughly 18%. FTTCP evidence of 22% funded growth → a live but not generous opportunity. Evidence of 12% → PRICED-WE-ARE-LATE.
