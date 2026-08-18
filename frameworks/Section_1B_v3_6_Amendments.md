# SECTION 1B v3.6 AMENDMENTS — DAMODARAN INTEGRATION

*Version 3.6 | 13 August 2026 | Damodaran integration, operator directive 13-Aug-2026. This document layers on top of Section 1B v3.3 (Four-Pillar Framework), the v3.3 Amendments (1-8, 4.1-4.5), and the v3.5.1 Reconciliation (consolidated Amendment 9, Routes A and B). It does not modify any prior file in place. Where it supersedes an earlier amendment, it says so and the earlier text stays in its file for history, banner-marked. Stage 11 reads this alongside the earlier Section 1B files; where they overlap, v3.6 governs the items named here.*

*Five of these amendments implement operator decision-gate outcomes confirmed on 13-Aug-2026 (Gates A, B, C, D, and the Module B2 default that lives in FTTCP v2.0). The rest implement the Damodaran exit-multiple integration directed for Role 1. Every change carries its tag inline.*

---

## AMENDMENT 11 — PILLAR 1 CEILING RESOLVED AT 30x (Gate D)

`[v3.6: Pillar 1 continuous formula capped at 30x with the elite extension; supersedes Amendment 5's 24x cap — Damodaran integration, operator directive 13-Aug-2026]`

**The conflict.** Amendment 5 (v3.3) capped the continuous Pillar 1 formula at 24x. The Master Project Prompt v3.3 Pillar 1 text and the v3.2 base spec carry an elite extension that raises the ceiling to 30x for capital-light names with ROCE above 33 percent. A run anchoring on Amendment 5 caps a 50 percent ROCE name at 24x; a run anchoring on Master v3.3 caps it at 30x. The same business earns two different quality bases.

**Resolution (Gate D confirmed).** Keep the continuous formula. Cap it at 30x. The Pillar 1 ROCE Base Multiple is:

- **For ROCE ≤ 33%: Base PE = 0.5 × ROCE(%) + 7.5, floored at 9x.**
- **For ROCE > 33%: Base PE = 24 + 0.3 × (ROCE(%) − 33), capped at 30x.**

Reference points: 12% → 13.5x | 17% → 16x | 22% → 18.5x | 27% → 21x | 32% → 23.5x | 40% → 26x | 50% → 29x | 55%+ → 30x.

Amendment 5's "capped at 24x" is SUPERSEDED. The 24x figure remains in the v3.3 Amendments file for history and must not be applied. Everything else in Amendment 5 (the continuous formula itself, one-decimal rounding of the base, no rounding of intermediate ROCE, the midpoint-ROCE feed) stands unchanged. The elite extension is reserved for genuinely capital-light names crossing 33 percent ROCE; it does not relax any sector cap, which remains absolute.

---

## AMENDMENT 12 — RRM r-TABLE SINGLE-CREDIT FIXES (Gates A, B, C)

`[v3.6: three single-credit corrections to the RRM required-return (r) adjustment table — Damodaran integration, operator directive 13-Aug-2026]`

The Required-Return Multiplier drives the discount rate through r (Master v3.3 RRM Dual-Track Derivation: RRM = 1 + (13.5% − r) × 0.12, bounded ×0.70 to ×1.60; base r small/micro 14%, mid 13%, large-quality 12%; adjust for durability and governance; bound r in [9%, 18%]). The granular r-adjustment items were pricing three risks twice. These fixes single-home each one. They change the adjustment table only; the RRM formula, its bounds, and the base r levels are unchanged.

**12A — Structural poor cash conversion (Gate A confirmed).** DELETE the +0.5 r-UP for structural poor cash conversion. Pillar 2 already prices structural poor cash conversion through the 0.65x Cash Multiplier. Charging r as well double-counts the same defect. **Pillar 2 owns cash quality; the r table no longer touches it.** The 0.65x multiplier and its structural-versus-growth-induced test (Master v3.3 Pillar 2) are unchanged.

**12B — Cyclicality (Gate B confirmed).** Where the Durability band is Moderate or Unproven BECAUSE of cyclicality, CAP the cyclical r-surcharge at +0.75 (the surcharge otherwise ranges +0.75 to +1.5). A docked durability band and a full cyclical surcharge both price the same cyclicality; capping the surcharge stops the double dock. Where the durability band is Moderate or Unproven for a reason other than cyclicality, the full surcharge range still applies. State in the worksheet why the durability band is docked, so the cap is auditable.

**12C — Short public record (Gate C: single-home).** A record under five years listed currently both DEFINES the Unproven durability band (zero durability discount) and earns a +0.75 r-UP. DROP the +0.75 short-record r-UP. **The Unproven durability band owns short-record risk.** A young listing is priced once, through the durability band, not twice. Any other genuine risk a young company carries (thin history on cash conversion, unproven margins) is priced through its own channel on its own evidence, not through a blanket short-record r-UP.

**Worksheet line (r-adjustment audit):** "r base ___%; durability adj ___ (band: ___, reason: ___); governance adj ___; cyclical surcharge ___ (capped at +0.75 per 12B? Y/N); complexity adj ___ (Amendment 13); cash-conversion r-UP: none per 12A; short-record r-UP: none per 12C; final r ___% (bounded [9%,18%])."

---

## AMENDMENT 13 — COMPLEXITY DISCOUNT (lives in r, and nowhere else)

`[v3.6: complexity discount adds +0.5 to r for structural opacity — Damodaran integration, operator directive 13-Aug-2026]`

Where the annual report shows structural complexity that makes the accounts harder to trust, the required return rises. Complexity is a real cost of capital: a reader who cannot fully see through the numbers demands a higher return to hold them. The triggers, any one of which qualifies:

- high subsidiary count (a sprawling group structure that obscures where profit and cash actually sit),
- dense related-party transactions (material RPT that could move margin between the listed entity and promoter vehicles),
- audit qualifications (a qualified or adverse opinion, or an emphasis of matter that goes to the numbers).

Where one or more triggers is present, **r rises by +0.5**. Complexity lives in r and nowhere else. It does not dock a pillar, does not scale a premium, and does not touch the sector cap. Pricing it once, in r, keeps it from leaking into the quality base or the growth premium where it would compound. State the trigger and the +0.5 in the r-adjustment worksheet line. This +0.5 is separate from and additive to the durability and governance adjustments; it is a distinct opacity charge.

---

## AMENDMENT 14 — DURABILITY-OF-GROWTH FADE HORIZON FROM THE EMERGING MOAT SCORE

`[v3.6: Emerging Moat classification sets the growth fade horizon for projections and DCF, replacing flat CAGR lines — Damodaran integration, operator directive 13-Aug-2026]`

Flat CAGR lines through the projection assume a business grows at one rate and then stops, which no business does. Growth fades, and how fast it fades depends on how durable the moat is. The Emerging Moat classification (already produced in stage 7) sets the fade horizon. This horizon governs the Role 1 projections and any DCF, replacing flat CAGR lines.

| Emerging Moat Classification | Durability of Growth (fade horizon) |
|---|---|
| Moat Expansion | Holds high growth through Year 5 |
| Strengthening | Fades by Year 4 |
| Modest | Fades to industry growth by Year 3 |
| None | Fades immediately (industry growth from Year 1) |

"Fades" means the growth rate steps down toward industry growth across the stated horizon, not that growth stops. The projection must show the step-down explicitly, year by year. This interacts with the projection-horizon rule in Master v3.4 Role 1: the model runs to Year 5 even on a three-year hold, because the Year 3 buyer pays for Years 4 and 5, and the fade horizon is what makes the Year 4 and Year 5 numbers honest. A name classified None with no credible Year 4 to Year 5 story takes the exit-multiple haircut named in Master v3.4.

---

## AMENDMENT 15 — RELATIVE PE PRIMACY IN THE DESTINATION PE

`[v3.6: destination PE also expressed as a relative PE against the name's and sector's historical relative band, citing FTTCP Module B8 — Damodaran integration, operator directive 13-Aug-2026]`

India prices growth relatively. A destination PE stated only in absolute terms ignores that the market re-rates a name against its own history and against its sector, not against a textbook. The destination PE from the Four-Pillar Summary is therefore ALSO expressed as a relative PE:

**Relative destination PE = absolute destination PE ÷ market PE**, compared against the name's own historical relative band and its sector's historical relative band.

The FTTCP Module B8 re-rating potential rating (HIGH / MODERATE / NONE, with its convergence target and binary gate) is cited in the destination PE discussion. Where B8 reads HIGH, the relative-PE convergence target supports a destination PE toward the upper end of the range, subject always to the absolute sector cap. Where B8 reads NONE, the relative expression is a check that the absolute destination PE is not assuming a re-rating the peer set does not support. The absolute sector cap remains the binding ceiling; the relative expression informs where inside the range the destination PE sits, it never breaches the cap.

---

## AMENDMENT 16 — GROWTH PREMIUM ELIGIBILITY GATE (from FTTCP Module B2)

`[v3.6: no Pillar 3 growth premium until projected ROCE crosses the minimum ROCE requirement — Damodaran integration, operator directive 13-Aug-2026]`

Pillar 3 pays a premium for visible growth. Growth below the cost of capital is not worth paying for; it destroys value as it compounds. The FTTCP Module B2 crossover is the gate. **No Pillar 3 growth premium (3a growth visibility, 3b moat formation, 3c duration) is awarded for any year before projected ROCE crosses the minimum ROCE requirement.** The crossover is a monitorable binary gate: Module B2 states "growth premium eligible: YES from FY__ / NO," and Role 1 reads that flag directly.

Where B2 reads NO (ROCE does not cross the minimum requirement within the projection), Pillar 3 pays +0x regardless of order book, moat score, or duration. Where B2 reads YES from a future fiscal year, the growth premium is eligible only from that year forward, and the projection must reflect the pre-crossover years earning no premium. This gate sits on top of the existing Pillar 3 evidence gates (📄 tiers, EM thresholds, catalyst proximity); it does not replace them, it precedes them.

---

## INTERACTION WITH THE REST OF THE FRAMEWORK

- **Single-credit stays supreme.** Amendment 4 (ROCE recovery credited in Pillar 1 or the Strategic Premium, never both) and the v3.5.1 route selection (Route A operational or Route B pre-cycle, never both) are unchanged. Amendment 12's fixes are the same discipline applied to the r table. Amendment 13's complexity charge lives in r alone for the same reason.
- **The sector cap is still absolute.** Amendments 11, 14, 15, and 16 all defer to it. Nothing here raises a cap.
- **FTTCP v2.0 is the sole source of the forward verdicts and the Part B outputs** that Amendments 14 (via the EM classification path into projections) and 16 (via Module B2) rely on. Role 1 consumes them and does not recompute them.
- **The RRM formula, bounds, and base r are unchanged.** Amendments 12 and 13 change only which adjustments enter r, not how RRM maps r to a multiplier.

## VERSION HISTORY

| Version | Date | Changes |
|---|---|---|
| 3.5.1 | 12-Jul-2026 | (prior) Amendment 9 and 4.5 reconciled into consolidated Amendment 9, Routes A and B. See `Section_1B_v3_5_1_Reconciliation.md`. |
| 3.6 | 13-Aug-2026 | Amendments 11-16, Damodaran integration and operator decision-gate outcomes of 13-Aug-2026. Amendment 11 (Gate D): Pillar 1 continuous formula capped at 30x with the elite extension, superseding Amendment 5's 24x cap. Amendment 12 (Gates A, B, C): three RRM r-table single-credit fixes, namely delete the +0.5 cash-conversion r-UP (Pillar 2 owns it), cap the cyclical surcharge at +0.75 where the durability band is docked for cyclicality, and drop the +0.75 short-record r-UP (the Unproven durability band owns it). Amendment 13: complexity discount, +0.5 to r for high subsidiary count, dense RPT, or audit qualifications, living in r and nowhere else. Amendment 14: Emerging Moat classification sets the growth fade horizon (Expansion holds to Year 5, Strengthening fades by Year 4, Modest fades to industry by Year 3, None fades immediately), replacing flat CAGR lines in projections and DCF. Amendment 15: destination PE also expressed as a relative PE (absolute ÷ market PE) against the name's and sector's historical relative band, citing FTTCP Module B8. Amendment 16: no Pillar 3 growth premium until projected ROCE crosses the minimum ROCE requirement, read from FTTCP Module B2's binary gate. |
