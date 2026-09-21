# Chunk 09. Probabilistic catalyst credit and the Expectation Ledger (A22, A23)

Loaded by: FTTCP Step 2 Section C.2; Role 1 Section 4 decomposition. Pipeline: stage 11 (writes `outputs/expectation-ledger.md` from `runs/_template/outputs/expectation-ledger.md`); /fttcp; stage 09b (ledger seeds); Verifier C (off-ledger and residual gates); quarterly review (reads and refreshes the ledger).
Sources in force: Section 1B v3.9 Amendments 22, 23, Appendix A; FTTCP v2.3 Section C.2 and Step 4.5; v3.10 Amendments 26.1, 26.2 feeds.

## Amendment 22: probabilistic catalyst credit

- Each catalyst in the FTTCP catalyst table carries an explicit **probability (0.00-1.00)** assigned by the operator, with the evidence basis stated.
- The earnings increment attributable to that catalyst is credited at **increment × probability**.
- Probabilities are **updated each quarter** on new evidence: state the prior, the evidence, the posterior.
- Tiering for Amendment 24: probability ≥ 0.50 is high-probability expectation (T2); below 0.50 is speculative (T3).
- The evidence symbols (📄 documented / 🎙️ management verbal / 🔍 inferred) are inputs to the probability, not gates on the credit. Documented evidence raises the probability; it does not unlock a premium tier by itself.
- **Downside terms are mandatory.** At least one negative increment (base erosion: cost growth outpacing revenue, margin compression on new capacity, catalyst slippage, treasury-income fade on a depleting cash pile) carries its own probability, so the distribution is two-sided.

## FTTCP Section C.2: the valuation-facing table

Section C bands still drive the transition verdict (chunk 16). Section C.2 converts the same catalysts into the credit Role 1 consumes. Build it for the run's forward target year on the Amendment 21 base.

| # | Catalyst | ₹ Cr PAT increment if fires | Probability (0.00-1.00) | Evidence basis (📄/🎙️/🔍) | Prob-weighted increment (₹ Cr) | Confirming metric + threshold | Confirm-by | Tier |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | T2 / T3 |
| D1 | Downside term (MANDATORY, negative) | (negative) | | | (negative) | | | (netted) |

Rules:

- The Section C band maps to a starting range: HIGH ~0.60-0.90, MODERATE ~0.30-0.60, LOW ~0.10-0.30, VERY LOW <0.10. The number is the operator's call with the evidence basis stated.
- 📄 raises the probability; 🎙️ and 🔍 lower it; the Section B promise-vs-delivery discount still applies.
- **Rejection rule.** A catalyst table with no downside row is REJECTED. FTTCP emits no Step 3 scorecard and hands no credit to Role 1 until a downside row exists. This is a mechanical incompleteness that halts like a missing input, not a judgment call.
- The downside row's negative prob-weighted increment nets against the T2 sum before it reaches Role 1.
- A confirming metric with threshold AND a confirm-by date are mandatory on every row. A row without both cannot be credited.

## Amendment 23: the Expectation Ledger with expiry

- Every expectation credited in the price sits on the ledger with: the catalyst, the ₹ Cr earnings increment, the probability, the confirming evidence (a specific metric and threshold), and a confirm-by date.
- **An expectation not on the ledger may not be credited in the price.**
- If the confirming evidence does not appear by the confirm-by date, the credit **decays by a fixed step of 25% of the original credit per missed review**, and the position is trimmed in proportion (Amendment 25 trim ladder, chunk 08).
- Two consecutive missed confirm-by dates on the same item **retire it to zero** and register a DROPPED commitment in the Role 5 promise-vs-delivery tracker (governance flag).
- Confirmed items move from the ledger into the confirmed run-rate base at the next Amendment 21 refresh.
- The ledger is saved to Notion with every Role 1, Role 4 and Role 6 output.

### Ledger template (Appendix A)

| # | Catalyst / expectation | ₹ Cr PAT increment | Probability | Evidence basis (📄/🎙️/🔍) | Confirming metric and threshold | Confirm-by | Status |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | OPEN / CONFIRMED / DECAYED-1 / DECAYED-2 / RETIRED |
| D1 | Downside term (mandatory) | (negative) | | | | | |

Rules: at least one downside row; every row has a confirm-by date; p ≥ 0.50 = T2, p < 0.50 = T3; decay 25% per missed review; two misses = RETIRED plus a DROPPED flag.

## What feeds the ledger

- Amendment 26.1: a revenue basis diverging from historical CAGR by more than 10 pp (chunk 07).
- Amendment 26.2: every margin-bridge confirm-by date (chunk 07).
- Rule F Second-Order chains (Role 2 §3.5, FTTCP Step 4.5): every "observation that confirms or breaks this chain, and confirm-by date" line. A chain uses the Amendment 22 probability where one exists and never restates it as certainty.
- Option Resolution Calendar events (chunk 10) where the tracker row exists.

## Worksheet line

"Ledger: ___ items (T2 ___, T3 ___, downside ___) | prob-weighted T2 net ₹___ Cr | T3 ₹___ Cr | items past confirm-by: ___ (status ___)"
