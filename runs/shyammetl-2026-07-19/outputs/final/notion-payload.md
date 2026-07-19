Execute via the claude.ai project; never overwrite Decision Status.

# Notion save payload — SHYAMMETL

Save instructions (for the executing session, not an action here):
- Fetch the live company page first if it exists.
- NEVER overwrite Decision Status from a pipeline run. Append, do not replace.
- This file is a payload only. Do not write to Notion from this pipeline stage.

## Page title
Shyam Metalics & Energy Ltd (SHYAMMETL) — Run 2026-07-19

## Run summary
- Headline: Transition real but price already exceeds value
- Evidence gate verdict: PROCEED WITH FLAGS (rule 3; FLAG-PROMOTER + FLAG-CASH active)
- Investment decision: AVOID (valuation and governance driven)
- Entry range: Rs 416 to 468 | MoS price: Rs 374 | CMP: Rs 1,022
- Tier A, 25% hurdle | Position size if actionable: Small
- Overall confidence: 69 (band 60 to 74, normal minus)

## Verdict
Evidence gate: PROCEED WITH FLAGS. The analysis record is trustworthy (source fidelity gate HELD, zero fabrications, all Gate 0 and Section 1B pillar inputs clean). Three active flags carry: FLAG-PROMOTER CONCERN, FLAG-CASH GROWTH-INDUCED, FLAG-GATE0 AVOID, plus a SHARED CATALYST flag. Investment decision AVOID is a separate call.

## Valuation decision
AVOID at Rs 1,022. Applied 20x flat on forward FY27E EPS ~45.67 (operator sector-cap ceiling; manifest Pharma/CDMO 38x overridden). Fair values bear 867 / base 913 / bull 1,006, all below CMP. Self-derived tracks: RRM mid 15.7x, additive mid 18.5x, both below the applied 20x. Hurdle Ratio STOP (base 1.24, bull 1.66 vs 1.953). Expected prob-weighted CAGR -3.3%.

## Entry zones
- Actionable entry: Rs 416 to 468 (Tier A, 25% hurdle)
- Margin of safety: Rs 374
- Zone top sits 54% below CMP; reaches entry only via a thesis-relevant shock or broad steel de-rating. Tier B barred (promoter CONCERN fails the Tier B quality gate). 52-week low / lowest tested price: price history unavailable this run.

## Thesis-broken triggers
- FY27 ROCE fails to turn up toward the pre-depression band (stays below ~14% while commissioned lines run) for two consecutive prints.
- Consolidated finished-goods inventory growth exceeds 2x revenue growth for two straight quarters.
- The ED-PMLA Rs 159.51 cr attachment on SSPL crystallizes as a cash outflow or extends to the parent.

## Monitoring checklist
1. FY27 annualized ROCE rising toward 15 to 16% (red: below 14% or falling two consecutive prints).
2. Consolidated FG inventory growth below 2x revenue growth (red: above 2x for two straight quarters) — primary cash-flag falsifier.
3. Standalone CFO/PAT at or above 0.7x after capex taper (red: below 0.7x).
4. SSPL profit contribution to consol P&L (red: further decline below ~45% or continued absolute decline).
5. SHARED CATALYST commissioning on schedule: Aluminium FRP 60kTPA Sep-2026, Wagon Phase-I Sep-2026, DRI 0.5 MTPA by Mar-2027 (red: any slip).
6. ED-PMLA Rs 159.51 cr attachment resolved with no cash cost and no extension to parent (red: cash outflow or spreads to parent).
7. CPCB Rengali/Sambalpur closure lifted within the 3-month window (red: unresolved or production loss).
8. Consolidated EBITDA margin sustained at or above 14% (red: reverts below 13%).

## Falsification line
Q1 FY27 consolidated PAT falls year on year again despite higher revenue, confirming the SSPL-led core decline is structural not a capex-cycle trough.

## Publish
No publish candidate this analysis.

## Links
- Drive folder: N/A (local git run)
- Run folder: runs/shyammetl-2026-07-19/
- Deliverables: runs/shyammetl-2026-07-19/outputs/final/ (business-narrative.md, fttcp-recommendation.md, verifier-summary.md, verifier-disagreement-log.md, fttcp-handoff.md, notion-payload.md)

## Operational note (not for the company page body)
manifest.sector_cap_row still reads "Pharma / CDMO" (38x). It was overridden to 20x for this run per the deliberation. The manifest FILE must be corrected to the steel Section 1B row before any future run.
