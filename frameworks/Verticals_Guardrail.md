# Verticals Guardrail: Internal and Downstream

Ruling: OR-34 (operator, 20-Oct-2026). Replaces the Downstream Analysis Guardrail of 19-Oct-2026. Read this before starting the verticals for any company.

## Two kinds of vertical

Phase 2 has two kinds of vertical. They answer different questions. Never mix them, and never give them the same name.

| | Internal Verticals | Downstream Verticals |
|---|---|---|
| Question | Is the company's own engine sound? | Is outside demand real, and how will we know? |
| One per | Dominant variable from the mental model | Revenue stream |
| Evidence | The company's filings, rating, concalls | Customers, rivals, regulators, industry data |
| Ends with | A ruling recommendation for the /fttcp gate | Signal rows for the tracker |
| Goes to | The handover dossier | The DOWNSTREAM SIGNAL TRACKER |
| Runs | Once per cycle | Ongoing, refreshed monthly |

## Order

1. Run the Internal Verticals first.
2. Then run the Downstream Verticals.

The internal work shows which streams matter and what to test. Example: Kross's Internal Vertical on capex found that over 90% of the tube plant's output must be sold outside. That is why the tube plant got its own downstream stream map.

## Internal Verticals: the rules

1. **One vertical per dominant variable.** Minimum four.
2. **Use the company's own evidence:** filings, notes, the rating rationale, concalls, extraction prompts to Claude Code. Typical topics are the margin bridge, working capital, funding and leverage, capex delivery, restatements and disclosure quality.
3. **End each one with a verdict, open questions, and the ruling it feeds.** Examples: the cash multiplier, the base margin, the entity map, the converter test, a promoter tripwire.
4. **They never go to the tracker.**

## Downstream Verticals: the rules

1. **One vertical per revenue stream.** A stream counts if it is 10% or more of revenue, or if the thesis depends on it.
2. **List the streams first.** Before Downstream Vertical 1, write each revenue stream with its share of revenue. Map every dominant variable to the stream where its outside signal lives.
3. **Start each vertical with the Demand Chain Map.** Fill the seven fields: product, who makes it, scope, direct customer, demand driver, chain dependencies, verification points.
4. **Verify only from outside sources.** Customers, counterparties, regulators, trade data and sector series count. The company's own filings can frame the question. They cannot answer it.
5. **End each vertical with at least one signal row.** Give the signal name, primary source URL, update cadence, the observation that confirms it, the observation that falsifies it, and the thesis line it tests.
6. **Flag shared dependencies.** If one signal drives two streams, it is one tracker row and one catalyst, never two.

## The drift test

Ask this at the start and end of every Downstream Vertical:

> Is my main evidence the company's own P&L, balance sheet, cash flow, capex or disclosures?

If yes, the work is an Internal Vertical. Move it there.

## The example that caused this rule

Kross, October 2026: the first six verticals were all called "downstream", but most were internal. Under this guardrail they split like this:

**Internal Verticals:** margin bridge, working capital and funding, capex bets (project delivery, cost per tonne, captive versus merchant).

The first-round work on the trailer cycle, competition and anti-dumping, and new markets used outside evidence. It was folded into the Downstream Verticals below.

**Downstream Verticals:**
- trailer axles
- truck components
- tractor parts
- exports
- tipping jacks
- seamless tube (merchant sales, from FY28)
