# PERMAGNET — Core-Operating ROCE Recompute (FTTCP v2, Reading 2)

Company: Permanent Magnets Ltd | Ticker: PERMAGNET | CMP Rs 882 (screener.in, 20-Aug-2026)
Run: runs/permagnet-2026-08-19 | First workup | NO-CONCALL MODE
Purpose: anchor the core-operating ROCE ex-QMPL for FY26 and set the Reading 2 Pillar 1 base.
Scope: FTTCP layer only. No Phase 3 SOTP or fair value. Role 1 runs those at /finalize.
Source: AR-FY26 only (285e7c4a...pdf, extracted work/txt/AR-FY26.txt). Every number anchored. NOT FOUND is the only fill.

---

## 1. The question

The block set Pillar 1 off CONSOLIDATED ROCE 12.54% (Reading 1). The SOTP then quarantines the
loss-making QMPL subsidiary in a separate slice and puts its debt in the equity bridge. That
double-counts the QMPL drag. B15 flagged it. This file recomputes the CORE-operating ROCE ex-QMPL
(Reading 2), fully anchored, and reads the Pillar 1 consequence.

Rule of adoption (operator, this session): adopt Reading 2 if the anchored core ROCE lands at or
above 13.5% cost of capital. The methodology is right; only the number was missing.

---

## 2. QMPL on its own (Form AOC-1, AR-FY26 p.57)

| QMPL item | Value (Rs Cr) | Anchor |
|---|---|---|
| Share capital | 0.05 | AOC-1 row 5 |
| Reserves & surplus | (7.58) | AOC-1 row 6 |
| Net worth | (7.53) | derived |
| Total assets | 46.58 | AOC-1 row 7 |
| Turnover | 1.23 | AOC-1 row 10 |
| Profit before tax | (5.31) | AOC-1 row 11 |
| Profit after tax | (5.62) | AOC-1 row 13 |

QMPL capital employed ≈ net worth (7.53) + ECB borrowing 47.81 ≈ Rs 40.3 Cr. ECB is non-current
(Consol Note 16; Consol Balance Sheet non-current borrowings 66.84 = parent 19.03 + QMPL 47.81).

QMPL operating EBIT: **NOT FOUND**. PBT is (5.31). Finance cost accrued Rs 1.72 Cr is disclosed,
but the split between the P&L charge and interest capitalised into CWIP is not disclosed, so QMPL's
own EBIT cannot be anchored to one figure. The core computation does not use it. QMPL is stripped
whole.

---

## 3. Core capital employed (parent standalone, ex-QMPL)

| Component | Value (Rs Cr) | Anchor |
|---|---|---|
| Standalone total assets | 238.35 | Std Balance Sheet p.91 |
| Less current liabilities | (40.79) | Std Balance Sheet, block E |
| = Standalone capital employed | 197.56 | derived |
| Less investment in QMPL (Note 3) | (0.05) | Std Balance Sheet, non-current investments |
| Less loans to QMPL, closing 31.03.26 | (2.73) | Reg-30 / RPT note, "Loans to Subsidiary Co." |
| **= Core capital employed** | **194.78** | derived |

Capital employed uses closing Total Assets minus Current Liabilities. This matches the AR's own
consolidated ROCE definition, so the core number is directly comparable to the disclosed 12.54%.

---

## 4. Core operating EBIT (QMPL income treatment stated)

| Component | Value (Rs Cr) | Anchor |
|---|---|---|
| PBT before exceptional items | 29.45 | Std P&L (V) p.92 |
| Add finance costs (Note 30) | 3.12 | Std P&L, finance costs line |
| = Standalone EBIT, operating, pre-exceptional | 32.57 | derived |
| Less QMPL-related income (loan interest, net of TDS) | (0.52) | RPT note, "Interest received (net of TDS)" |
| **= Core operating EBIT** | **32.05** | derived |

Only one QMPL income line sits in the standalone P&L: Rs 0.52 Cr of intercompany loan interest,
inside Other Income (Rs 6.20 Cr, Note 26). It is stripped. QMPL pays no dividend (AOC-1 row 14), so
nothing else flows up.

The Rs 1.74 Cr exceptional item (Note 33) is a one-off charge. The operating figure above excludes
it. Including it lowers EBIT to Rs 30.30 Cr.

---

## 5. Core ROCE

| Basis | Core EBIT (Rs Cr) | Core CE (Rs Cr) | Core ROCE |
|---|---|---|---|
| Operating, ex the Rs 1.74 one-off | 32.05 | 194.78 | **16.5%** |
| Including the Rs 1.74 one-off | 30.30 | 194.78 | 15.6% |

**Anchored core ROCE band: 15.6% to 16.5%.** Both readings clear the ~13.5% cost of capital.

By the operator's stated adoption rule (>= 13.5%), Reading 2 stands unless overruled.

---

## 6. The triangle — why disclosed standalone 11.20% is below consolidated 12.54%

Both ratios are AR-disclosed. They use the same EBIT-style numerator but **different denominators**.

| Ratio | Numerator | Denominator (as printed) | Result |
|---|---|---|---|
| Standalone (ratios note) | Earning before tax and finance cost | "Net worth + borrowings + lease liabilities" | 11.20% |
| Consolidated (ratios note) | Earning before tax and finance cost | "Total Assets − current liabilities other than interest-bearing" | 12.54% |

The driver, in one paragraph. Consolidation folds in QMPL's Rs 47.81 Cr ECB and its debt-funded
assets. The consolidated formula adds QMPL's ECB interest back into EBIT, because it is a
finance-cost add-back, so QMPL's pre-tax loss, which is mostly interest, barely dents the numerator.
Meanwhile a large slice of the undeployed ECB cash sits in treasury and CWIP inside the capital
base. Two different denominators plus the interest add-back make the consolidated 12.54% print above
the standalone 11.20%. It is a definitional artifact, not proof that the loss-making subsidiary earns
its keep. On one consistent definition, consolidation dilutes the parent's ~16.5% core down to
12.54%, which is the intuitive direction. This is the same front-matter-versus-back-matter
inconsistency B03 flagged.

---

## 7. Reading 2 Pillar 1 base (Section 1B v3.6 Amendment 11)

Amendment 11: for ROCE at or below 33%, **Base PE = 0.5 x ROCE(%) + 7.5**, floored 9x, capped 30x.
No normalization route applies. Route A needs ROCE >= 20% (16.5% fails). Route B is barred on
STAGNANT growth. So the statutory core ROCE feeds Pillar 1 directly.

| Reading | ROCE | Pillar 1 base PE |
|---|---|---|
| Reading 1 (consolidated, block) | 12.54% | 0.5 x 12.54 + 7.5 = **13.8x** |
| **Reading 2 (core ex-QMPL)** | **16.5%** | 0.5 x 16.45 + 7.5 = **15.7x** |
| Reading 2 lower bound | 15.6% | 0.5 x 15.56 + 7.5 = 15.3x |

---

## 8. Recomputed P/E BASE CARD (preview, provisional, for operator approval)

Same pillar mechanics as the block, Reading 2 base substituted. Additive = base x cash x UA. RRM =
additive x rrm(0.82). Nothing here is Phase 3; Role 1 runs the full SOTP.

| Pillar | Reading 1 (block) | Reading 2 (this file) | Note |
|---|---|---|---|
| Pillar 1 base (ROCE) | 13.8x (12.54%) | **15.7x (16.5%)** | Amendment 11; route NONE |
| Pillar 2 cash multiplier | 1.00x | 1.00x | growth-induced; 1.15x trigger on a third strong FY27 |
| Pillar 3 growth premium | +0x (gate shut) | **+0x, gate now OPEN** | see flag below |
| Strategic premium | +0x | +0x | ROCE-recovery route not used; single-credit |
| Undiscovered Alpha | x1.25 | x1.25 | all 3 qualifiers met, unchanged |
| Sector cap | 25x (non-binding) | 25x (non-binding) | 19.6x < 25x |
| **Destination PE, additive** | 17.3x | **19.6x** (band 19.1-19.6x) | 15.7 x 1.25 |
| **Destination PE, RRM** | 14.1x | **16.1x** (band 15.7-16.1x) | 19.6 x 0.82 |

Earnings basis: **ONE-YEAR-FORWARD**, applied to FY27 core operating EPS ~Rs 22.9 (grade-C
conservative build, operator-confirmed). Price-side context unchanged: CMP 882 / 22.9 = 38.5x forward
core.

**Pillar 3 flag for operator ruling.** Core ROCE 16.5% crosses the ~13.5% cost of capital, so the
Amendment 16 gate that held Pillar 3 at +0x is now open. My view: hold Pillar 3 at +0x anyway. The
core grows modestly and the Pillar 1 FTTCP verdict is STAGNANT, so there is no organic growth basis
for a premium. The transformation is already priced in the separate option slices, so crediting a
core Pillar-3 premium would double-count the same optionality and break single-credit. This is your
call, not mine to close. The single fact that would change it: audited FY27 core revenue growth
durably above the mid-teens, which would give the core its own growth basis.

---

## 9. What this does and does not change

- Pillar 1 base rises 13.8x to ~15.7x. Both destination tracks rise about 2x.
- The AVOID decision survives. RRM 16.1x on ~Rs 22.9 forward core EPS is far below the 38.5x forward
  price. The hurdle still fails.
- Open item for operator: the Amendment 16 Pillar-3 gate, now crossed. Recommendation +0x holds.

NOT FOUND, unchanged: QMPL's own operating EBIT (interest capitalisation split undisclosed);
segment-level core-versus-relay cost split (single IND AS 108 segment); FY27 forward
revenue/margin guidance (no-concall mode).
