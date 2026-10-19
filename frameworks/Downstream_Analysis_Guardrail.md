# Downstream Analysis Guardrail

Ruling: OR-33 (operator, 19-Oct-2026). Read this before starting any downstream analysis.

## What downstream analysis is

Downstream analysis checks a company's demand from the outside. It uses customers, regulators, trade data and sector data. It never uses the company's own numbers to verify anything.

Its output is signals for the DOWNSTREAM SIGNAL TRACKER. Each signal is something outside the company that will confirm or break the thesis.

## The five rules

1. **One vertical per revenue stream.** Never one per dominant variable. A stream counts if it is 10% or more of revenue, or the thesis depends on it.
2. **List the streams first.** Before Vertical 1, write the revenue streams, each with its share of revenue. Map every dominant variable to the stream where its outside signal lives.
3. **Start each vertical with the Demand Chain Map.** Fill the seven fields: product, who makes it, scope, direct customer, demand driver, chain dependencies, verification points.
4. **Verify only from outside sources.** Customers, counterparties, regulators, trade data and sector series count. The company's own filings can frame the question. They cannot answer it.
5. **End each vertical with at least one signal row.** Give the signal name, primary source URL, update cadence, the observation that confirms it, the observation that falsifies it, and the thesis line it tests.

## The drift test

Ask this at the start and end of every vertical:

> Is my main evidence the company's own P&L, balance sheet, cash flow, capex or disclosures?

If yes, it is not downstream work. It is an **internal check**.

Margin bridges, working capital, funding, project delays and restatements are internal checks. They are useful. Put them in a separate block called **"Internal checks: inputs to the /fttcp gate"**. Never number them as downstream verticals. Never write them to the tracker.

## The example that caused this rule

Kross, October 2026: six verticals were run by dominant variable. Vertical 3 (margin) and Vertical 4 (working capital and funding) were internal. Vertical 5 (capex) was half internal.

The correct structure is one vertical per stream:

- trailer axles
- truck components
- tractor parts
- exports
- tipping jacks
- seamless tube (merchant sales, from FY28)
