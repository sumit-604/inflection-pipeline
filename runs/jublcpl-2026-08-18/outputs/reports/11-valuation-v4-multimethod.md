# JUBLCPL Valuation v4: Multi-Method, Per Business, Triangulated

Role 1 complete multi-method run. 21-Aug-2026. Master v3.6 Sections 1A, 2,
3, 4. SOTP wrapper for the demerger. FTTCP v2.1 Part B outputs consumed.

WHY THIS VERSION. v3 ran only the Four-Pillar exit multiple (the P/E
method). The framework Role 1 is multi-method: select methods (1A), apply
each (3), triangulate weighted (4). This version does that per business.
Weights below are PROPOSED, pending operator sign-off. v3, v2, v3.3
preserved as audit record.

INPUT HONESTY. No standalone accounts exist (demerger not effective).
Per-entity figures are illustrative allocations. Segment EBITDA, agri book
value, and the DCF path are ESTIMATES, flagged [EST] at each use. The
DIRECTION of the result is robust across reasonable inputs; the second
decimal is not.

---

## SECTION 1A: METHOD SELECTION (PROPOSED WEIGHTS FOR SIGN-OFF)

Top-level method: SOTP. The pre-demerger entity is two businesses
(Section 1A lists SOTP for conglomerates and holding companies). Inside
each leg, the business-appropriate methods below.

### Business A: Performance Polymers & Chemicals
Specialty chemicals. Clean earnings. Low leverage (D/E 0.06). High ROCE.
Earnings near cash.

| Method | Role | Proposed weight | Justification |
|---|---|---|---|
| P/E (Four-Pillar exit multiple) | Primary | 45% | Clean earnings, low leverage, asset-light-ish; earnings approximate cash |
| EV/EBITDA | Secondary | 30% | Manufacturing base; direct peer set (Apcotex, specialty chem) |
| DCF (FCFF) | Tertiary | 15% | High ROCE and low debt make it informative; terminal-sensitive, so capped weight |
| PEG | Cross-check | 10% | Tests whether we overpay for the faded 10.5% growth |

Not run: EV/Capacity (EV/tonne latex) needs volume data, NOT FOUND. P/B and
NAV skipped (book value misses the VP-latex market position).

### Business B: Agri Division
P&K fertilizer plus agri nutrients. Cyclical. Subsidy-linked. FY26 is a
peak.

| Method | Role | Proposed weight | Justification |
|---|---|---|---|
| EV/EBITDA at mid-cycle | Primary | 40% | Cyclical; must value off the full cycle, not the FY26 peak |
| P/E on normalized earnings | Secondary | 30% | Works only on the normalized base (PAT 17 Cr), never the peak |
| P/B | Cross-check | 20% | Cyclical anchor; weaker because best at trough and this is a peak [EST book] |
| EV/Sales | Cross-check | 10% | Subsidy pass-through distorts revenue; low weight |

Not run: DCF (cyclical plus subsidy timing make cash flows unpredictable;
Damodaran fails it here).

---

## SECTION 2: PROJECTIONS (brief; full path in B11-valuation-v3)

Business A FY27: revenue 1,367 Cr, PAT 125 Cr, EBIT ~189 Cr [EST from
165.46 x growth], EBITDA ~209 Cr [EST, segment D&A ~20 Cr], net cash
~30 Cr (B7). Faded FY30 EPS base 112, 3yr CAGR 10.5%.

Business B normalized (full-cycle): revenue ~700 Cr, EBIT ~24.5 Cr (3.5%
full-cycle margin), PAT ~17 Cr, EBITDA ~30 Cr [EST D&A ~5 Cr], agri WC debt
~30 Cr [EST, subsidy-receivable-funded].

---

## SECTION 3: APPLY EACH METHOD

### Business A

**Method 1: P/E (Four-Pillar exit multiple).** Destination 32.5x base
(B8 NONE hardened), 35x bull cap. Framework path: FY30 EPS 112 x 32.5 =
Rs 3,640/sh target, discounted to today. Fair value today ~Rs 4,080 Cr.
Range bear ~3,400, bull ~4,700 Cr. This is the exit-multiple approach.

**Method 2: EV/EBITDA.** Peer multiple 15x (band 14-16x; Apcotex and
specialty-chem small caps). FY27 EBITDA ~209 Cr [EST] x 15 = EV 3,135 Cr,
plus net cash 30 = equity ~Rs 3,165 Cr. Range 2,955 to 3,375 Cr. Implied
PE equivalent ~22.4x, well below the Four-Pillar 32.5x.

**Method 3: DCF (FCFF).** Base NOPAT ~125 Cr, growth faded 13.5% to 6%,
ROIC held 30% [EST, below the 67.5% segment figure]. Enterprise value:
- at 14.75% (framework required return): ~Rs 1,400 Cr
- at 11.5% (market cost of equity): ~Rs 2,400 Cr
Central at ~13%: ~Rs 2,000 Cr equity. The DCF is the low anchor and is
highly discount-rate-sensitive.

**Method 4: PEG.** Growth 10.5%. Fair PE at PEG 1.5 to 2.0 = 15.75x to
21x. On FY27 PAT 125 Cr → Rs 1,970 to 2,625 Cr, central ~Rs 2,300 Cr. At
the current 32.5x the PEG is 3.1, which reads expensive.

### Business B

**Method 1: EV/EBITDA mid-cycle.** 7x (band 6-8x, cyclical). Normalized
EBITDA ~30 Cr [EST] x 7 = EV 210, less WC debt 30 = equity ~Rs 180 Cr.
Range 150 to 210 Cr.

**Method 2: P/E normalized.** 14x (band 12-17.5x) on PAT 17 Cr =
Rs 238 Cr. Range 204 to 298 Cr.

**Method 3: P/B.** ~1.2x on estimated agri net worth ~Rs 165 Cr [EST, no
standalone book] = ~Rs 200 Cr. Range 150 to 270 Cr. Soft anchor.

**Method 4: EV/Sales.** 0.30x (band 0.25-0.35x) on revenue 700 Cr = EV
210, less debt 30 = equity ~Rs 180 Cr. Range 145 to 215 Cr.

---

## SECTION 4: TRIANGULATION

### Business A (proposed 45/30/15/10)

| Method | Base value (Rs Cr) | Weight | Contribution |
|---|---|---|---|
| P/E exit multiple | 4,080 | 45% | 1,836 |
| EV/EBITDA | 3,165 | 30% | 950 |
| DCF | 2,000 | 15% | 300 |
| PEG | 2,300 | 10% | 230 |
| **Triangulated** | | 100% | **~3,315 Cr** |

### Business B (proposed 40/30/20/10)

| Method | Base value (Rs Cr) | Weight | Contribution |
|---|---|---|---|
| EV/EBITDA mid-cycle | 180 | 40% | 72 |
| P/E normalized | 238 | 30% | 71 |
| P/B | 200 | 20% | 40 |
| EV/Sales | 180 | 10% | 18 |
| **Triangulated** | | 100% | **~201 Cr** |

### 4B. Methods-agreement check

**Business A: FAIL (wide dispersion).** The methods span Rs 2,000 Cr (DCF)
to Rs 4,080 Cr (P/E exit multiple), a 2.0x ratio. The P/E exit multiple is
the HIGH OUTLIER. Three of four methods (EV/EBITDA, DCF, PEG) cluster
Rs 2,000 to 3,165 Cr. The disagreement is the finding: the 32.5x
destination is ~45% above the ~22x that peers and cash flows support.

**Business B: PASS (tight).** Methods span Rs 180 to 238 Cr. They agree.
AVOID on every one.

### Combined SOTP

| Line | Value |
|---|---|
| Business A (triangulated) | ~Rs 3,315 Cr |
| Business B (triangulated) | ~Rs 201 Cr |
| Combined fair value | ~Rs 3,516 Cr |
| Per share | ~Rs 2,321 |
| Market cap / CMP | Rs 3,549 Cr / Rs 2,342 |
| Premium to CMP | ~ -0.9% (fairly valued) |

---

## WHAT MULTI-METHOD CHANGES

The single-method v3 said fair value Rs 4,320 Cr, +22% above the market.
The multi-method triangulation says fair value ~Rs 3,516 Cr, roughly LEVEL
with the market. The gap is entirely Business A, and entirely the P/E exit
multiple standing above the other three methods.

Read plainly: **on one method JACPL looked 22% cheap; across four methods it
is fairly valued at today's price.** The Four-Pillar 32.5x is richer than
peers (EV/EBITDA), cash flows (DCF), and growth (PEG) support. Triangulation
is the correction the single method could not make.

## DECISION

WATCHLIST holds and hardens. At CMP there is now **essentially no margin of
safety** on the triangulated fair value, not the 22% cushion the single
method implied. The wide Business A dispersion (2.0x) lowers confidence and
argues for the conservative end of the range and a wider margin of safety.

Proposed entry: ~30% below triangulated fair value given the dispersion =
~Rs 1,625/sh. Margin-of-safety price ~Rs 1,460. Buy trigger a ~30% dip, or
the first standalone polymer accounts that (a) confirm the segment cash
conversion and (b) justify a multiple above the ~22x peer level.

Business B AVOID unchanged (methods agree, ~Rs 200 Cr).

---

## FOR OPERATOR SIGN-OFF

1. Business A weights: **P/E 45 / EV-EBITDA 30 / DCF 15 / PEG 10.**
2. Business B weights: **EV-EBITDA 40 / P/E 30 / P/B 20 / EV-Sales 10.**
3. The DCF discount rate: I ran a range (11.5% to 14.75%). Your call on the
   central rate moves Business A by ~Rs 1,000 Cr at the method level.
4. Confirm the estimated inputs are acceptable as illustrative until
   standalone accounts print: segment EBITDA, agri book value, DCF path.

Change any weight and I re-triangulate. The Business A method dispersion,
not the point estimate, is the real message: the exit multiple is the
optimistic outlier.
