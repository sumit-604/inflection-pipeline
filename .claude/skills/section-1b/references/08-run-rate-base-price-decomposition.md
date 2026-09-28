# Chunk 08. Forward run-rate earnings base and three-tier price decomposition (A21, A24, with A25 sizing)

Loaded by: Role 1 earnings base for every multiple, and the Section 4 verdict. Pipeline: stage 11 (emits `run_rate_base` and `price_decomposition` in the B11 YAML); stage 14 (Role 2 applies A25 sizing); quarterly review (refreshes the A21 base each quarter).
Sources in force: Section 1B v3.9 Amendments 21, 24, 25; v3.10 Amendment 26 interaction; Master v3.7 §3 operating-earnings rule; FTTCP v2.3 Module B4.

Design principle: the market pays for the probability-weighted future, not the audited past.

## Amendment 21: forward run-rate earnings base

- The earnings base for every Section 1B and Role 1 calculation is **the latest reported quarter's run-rate, annualised, adjusted for known one-offs**. State and adjust treasury income on a depleting cash pile, exceptional items and seasonal distortions.
- The base is refreshed every quarter at the Role 4 results review. It is never frozen at the annual model.
- The annual (AR / Role 6) model is retained as a cross-check and floor, not the anchor. Where run-rate and annual model diverge by more than 25%, the worksheet states which is used and why.
- Seasonal or lumpy businesses (project cargo, agri, capital goods) use a trailing-4-quarter base instead of a single-quarter annualisation. The worksheet declares the basis.
- Operating earnings only: the EPS entering every multiple is FTTCP Module B4 operating EPS (treasury, rental and investment income stripped). Non-operating assets enter through the equity bridge, never inside the multiple.
- Confirmed Expectation Ledger items move into this base at the next refresh (chunk 09).
- Amendment 26.1 RUN-RATE revenue uses the same run-rate definition.
- Entry-exit basis symmetry still binds (Amendment 18.1, chunk 10).

## Amendment 24: price decomposition

At any CMP, decompose market capitalisation into three supported tiers plus a residual. Show each tier in ₹ Cr, ₹/share and % of CMP.

| Tier | Earnings basis | Multiple |
|---|---|---|
| T1 Confirmed | Amendment 21 run-rate base | Destination PE (Section 1B) |
| T2 High-probability expectation | Σ(increment × p) for p ≥ 0.50, net of downside terms | Destination PE |
| T3 Speculative expectation | Σ(increment × p) for p < 0.50 | Destination PE |
| Residual | CMP minus (T1 + T2 + T3) | Unsupported premium |

- The verdict is stated as the four percentages, never as a single over/under-valued line.
- The destination PE in each tier is the governing Section 1B destination (the operator-approved base where one exists), capped by the sector cap. Where a live Step 1C peer table exists, print the cross-check (chunk 15); without one, the tier multiple is the pillar destination and the cross-check reads PENDING LIVE PEER TABLE.
- **Position size is set to T1 + T2.** T3 is the explicit bet and is disclosed as such.
- A residual above 25% of CMP caps the verdict at starter size regardless of conviction.
- The Hurdle Ratio is recomputed on the Amendment 21 base with the probability-weighted EPS CAGR (chunk 06).

## Amendment 25: margin of safety as position size (fast-growth carve-out)

- Fast-growth = Amendment 21 run-rate growth ≥ 40% YoY, OR FTTCP Revenue Transition = ACCELERATING. For these names the margin of safety is position size, not a price haircut below fair value.
- **Starter:** 2-3% of portfolio (Small) when T1 + T2 ≥ 75% of CMP and the residual ≤ 25%.
- **Add ladder:** +1 to +2% on each ledger item that confirms (moves from T2/T3 to T1), up to Medium (4-6%) when T1 alone ≥ 60% of CMP, and Large (7-10%) only when T1 ≥ 80% of CMP AND Gate 0 EXCELLENT AND Promoter TRUSTWORTHY or better.
- **Trim ladder:** trim 25% of the position for each ledger item that decays (Amendment 23); trim 50% if the residual exceeds 40% of CMP after a decay.
- **Exit:** thesis-broken triggers are unchanged and remain absolute.
- Non-fast-growth names keep the price-based, evidence-scaled margin of safety (chunk 06).
- The dispersion cap and the Role 2 / Promoter caps still bind; the tightest cap wins.
- Accepted cost, recorded by the operator: this method will sometimes open starter positions in names whose expectations fail. The starter size and the ledger expiry are the two controls that bound that cost.

## Amendment 26: where caution lives

Amendment 25 is the sole home of caution about a projection. Doubt is expressed as a starter size and a confirm-by date, never by lowering a projection number.

## Worksheet and YAML fields

- "Earnings base: [single-quarter-annualised / trailing-4q] | PAT run-rate ₹___ Cr | one-offs adjusted: ___ | annual model divergence ___% (governing: ___ because ___)"
- "Decomposition at ₹___: T1 ___% | T2 ___% | T3 ___% | residual ___% | governing multiple: [pillar / relative] ___x"
- "Fast-growth: Y/N (basis ___) | size: starter / Medium / Large | next add trigger: ledger item ___"
