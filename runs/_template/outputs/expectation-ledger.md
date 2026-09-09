# EXPECTATION LEDGER — <TICKER> <run-date>

*Section 1B v3.9 Appendix A schema. Written by Stage 11 (Role 1 valuation) from
the FTTCP Section C.2 catalyst credit. Refreshed by the quarterly review (Role 4,
Quarterly_Results_Review_Protocol) and by Role 6 (AR). Saved to Notion with every
Role 1 / Role 4 / Role 6 output (Amendment 22). An expectation not on this ledger
may not be credited in the price.*

CMP basis: Rs <cmp> on <date> | Amendment 21 run-rate PAT base: Rs <x> Cr |
Forward target year: FY<nn> | Destination PE (governing): <n>x

| # | Catalyst / expectation | ₹ Cr PAT increment | Probability | Evidence basis (📄/🎙️/🔍) | Confirming metric and threshold | Confirm-by | Status |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | OPEN |
| D1 | Downside term (MANDATORY, negative) | (negative) | | | | | OPEN |

## RULES (Section 1B v3.9 Amendments 21-24)

- At least ONE downside row (negative increment, its own probability). A ledger
  with only positive entries is REJECTED; Stage 11 does not credit it.
- Every row carries a confirming metric-and-threshold AND a confirm-by date. A
  row missing either cannot be credited.
- Tiering: probability ≥ 0.50 is T2 (high-probability); < 0.50 is T3 (speculative).
- Decay: if the confirming evidence does not appear by the confirm-by date, the
  credit decays by a fixed step of 25% of the original credit per missed review,
  and the position is trimmed in proportion (Amendment 25). Status moves
  OPEN → DECAYED-1 → DECAYED-2.
- Two consecutive missed confirm-by dates RETIRE the item to zero (Status RETIRED)
  and register a DROPPED commitment in the Role 5 promise-vs-delivery tracker.
- A CONFIRMED item moves out of the ledger into the confirmed run-rate base at the
  next Amendment 21 refresh (Status CONFIRMED, then folded into T1).

Status values: OPEN | CONFIRMED | DECAYED-1 | DECAYED-2 | RETIRED.

## DECISION FEED (how this ledger reaches the verdict)

- T2 net = Σ(increment × probability) for p ≥ 0.50, net of the downside term(s).
- T3 = Σ(increment × probability) for p < 0.50.
- These feed the Amendment 24 price decomposition (T1 confirmed + T2 + T3 +
  residual) and the Amendment 25 sizing ladder (starter / add / trim) for
  fast-growth names.

## CHANGE LOG

| Date | Role | Change (row, field, from → to) | Reason |
|---|---|---|---|
| | | | |
