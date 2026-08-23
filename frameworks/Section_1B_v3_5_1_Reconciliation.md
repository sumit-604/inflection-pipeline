# SECTION 1B v3.5.1 — RECONCILIATION OF AMENDMENT 9 AND AMENDMENT 4.5

> **ACTIVE — not a superseded draft.** This file is the Pillar 1 normalization layer of Section 1B, the sole exit-multiple authority. It lives in frameworks/ as a runtime input to stage 11 and governs capital-cycle ROCE route selection (Routes A and B). The version number tags this amendment layer, not a competing copy of the Master Prompt. Do not archive or delete it. Read it together with the other Section_1B_* files (v3.3 Amendments, v3.6 Amendments, v3.7 Amendments, v3.8 Amendments); where they overlap, the later layer governs.

*Reconciliation session 12-Jul-2026 (Fable 5). Two amendments were adopted independently on the same day, both labelled v3.5, both modifying Pillar 1 for capital-cycle names: Amendment 9 (mid-cycle OPERATIONAL ROCE — capital-base normalization, adopted in the operator session) and Amendment 4.5 (normalized pre-depression ROCE anchor, promoted to law during the TATVA run). Left unreconciled, a run could apply both and double-credit the same recovery — the exact failure class Amendment 4 (single-credit rule) exists to prevent. This document supersedes both texts and replaces them with a single consolidated Amendment 9. Amendment 4.5 is RETIRED as a number; its mechanism survives as Route B below.*

---

## CONSOLIDATED AMENDMENT 9 — PILLAR 1 NORMALIZATION FOR CAPITAL-CYCLE NAMES

**The two distortions.** Point-in-time ROCE misprices a capital-cycle business through two distinct channels:

1. **Denominator bloat** — CWIP, idle raised capital, and capex advances sit in capital employed but are not yet earning (AZAD: statutory 8.8% vs operational 12%).
2. **Numerator trough** — current EBIT is cyclically depressed relative to the evidenced pre-capex earning power (TATVA: trough-anchored model entry Rs 121 vs a four-year market floor of Rs 590; pre-depression ROCE 15-20% repriced fair value to Rs 350-600).

Both channels understate true capital efficiency, drive the destination PE below any price the market has paid, and systematically screen out transition setups — the operation's own strategy.

**The single-credit principle extended.** A run may normalize through ONE route only. Applying both routes credits the recovery twice (once by shrinking the denominator, once by lifting the numerator). The worksheet must declare the route.

### ROUTE SELECTION RULE

| Condition | Route |
|---|---|
| (CWIP + idle raised capital + capex advances) > 20% of capital employed | **Route A — Operational ROCE** (denominator fix) |
| Denominator clean (test above fails) BUT FTTCP verdict TEMPORARILY DEPRESSED or RECOVERING with 📄-evidenced pre-depression ROCE history | **Route B — Pre-Cycle Normalized ROCE** (numerator fix) |
| Both conditions hold | **Route A governs.** Route A already prices the commissioning; layering pre-cycle normalization on top double-credits. Note in worksheet: "Route B condition also present — suppressed per single-credit rule." |
| Neither holds | No normalization. Statutory ROCE feeds Pillar 1 directly. |

### ROUTE A — OPERATIONAL ROCE (from Amendment 9 as adopted)

- **Operational capital employed** = capital employed minus non-operating cash and investments, minus CWIP, minus capex advances. EBIT adjusted to exclude income those stripped assets generate (e.g. interest on idle cash) — numerator and denominator stay consistent.
- **Mid-cycle ROCE** = normalized EBIT on that operational base at target/steady-state utilization, taken from the FTTCP RECOVERING blend where a recovery verdict applies, else trailing operational ROCE.
- **9.1 Blend Consistency Rule.** When operational ROCE is used, either BOTH blend endpoints are computed on the same operational basis, or the blend is skipped and operational ROCE feeds the formula alone. Worksheet states: "Blend basis: [operational-consistent / blend skipped]."
- **9.2 Staleness Rule.** Capital qualifies for stripping only with 📄-tier evidence of a deployment plan and commissioning timeline within 24 months. Idle beyond that stays in the denominator and is flagged to Role 3 as a capital-allocation concern.
- **Mandatory disclosure line:** statutory ROCE, each stripped item with amount, resulting operational ROCE. Never management's "adjusted ROCE."
- **EV/EBITDA cross-check** where that is the primary method; divergence >25% requires a stated governing choice.

### ROUTE B — PRE-CYCLE NORMALIZED ROCE (from Amendment 4.5, TATVA)

- **Third ROCE anchor** = median ROCE of the evidenced pre-depression cycle, 📄-gated (audited filings only), CAPPED at the evidenced historical level — never extrapolated above what the company has actually printed.
- **Named unwind catalyst required.** The depression must have a specific, dated, documented unwind mechanism (capacity commissioning, contract restart, regulatory clearance). "Cycle will turn" is not a catalyst.
- **Probability-weighted blend.** The pre-cycle anchor blends with current ROCE per the FTTCP recovery probability — it does not replace current ROCE outright. RECOVERING (40-60%) blends 60/40 current/anchor; higher-confidence verdicts may weight the anchor more, per the FTTCP verdict band.
- **Self-withdrawal clause.** If the recovery does not print by the named catalyst date (+1 quarter grace), the anchor is withdrawn at the next refresh and Pillar 1 reverts to statutory ROCE. The withdrawal is logged in Key Notes.
- **Decision discipline unchanged.** Route B lifts fair value toward evidenced reality; it does not manufacture entry zones. TATVA under Route B remains AVOID-on-valuation at Rs 1,326 — the market prices it at fair value, not at a 25% discount. That is the correct outcome, not a defect.

### INTERACTION WITH THE REST OF THE FRAMEWORK

- Amendment 4 (single-credit for ROCE recovery across Pillar 1 / Strategic Premium) applies on top of this: whichever route is used, ROCE recovery credited in Pillar 1 bars the Strategic Premium route, as before.
- Amendment 10 (intrinsic cross-check) triggers and mechanics are unaffected; where triggered, the DCF uses the same route-declared ROCE basis for its capital-efficiency assumptions.
- FTTCP remains the sole source of the recovery verdict and probability. Neither route may be invoked on a STAGNANT or DECLINING ROCE verdict.

### WORKSHEET LINE (replaces the Amendment 9 worksheet line 1)

"Pillar 1 normalization route: [NONE / A-Operational / B-Pre-Cycle / A-governs-B-suppressed]. If A: statutory ___%, stripped items [list+amounts], operational ___%, blend basis ___. If B: pre-cycle median ___% (source: [filing, years]), unwind catalyst [named, dated, 📄], blend weight ___/___, self-withdrawal date ___."

---

## VERSION HISTORY ADDITION

| Version | Date | Changes |
|---|---|---|
| 3.5.1 | 12-Jul-2026 | Amendment 9 and Amendment 4.5 reconciled into consolidated Amendment 9 with Route A (operational ROCE, denominator fix) and Route B (pre-cycle normalized ROCE, numerator fix), mutually exclusive per run under the route selection rule; Route A governs where both conditions hold. Amendment 4.5 retired as a number. 9.1 blend consistency and 9.2 staleness carried into Route A; 📄 gate, named catalyst, probability blend, and self-withdrawal carried into Route B. |
