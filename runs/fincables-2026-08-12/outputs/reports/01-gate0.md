# STAGE 1: GATE 0 QUANTITATIVE SCORECARD — v2 AUDITED RE-RUN

**THIS IS THE v2 AUDITED RE-RUN, SUPERSEDING THE v1 SCREENER-PROXY VERSION.**
v1 (classification AVOID, core 37/100) was run on screener-proxy data alone, with
Blocks B (cash generation) and D (balance sheet strength) partly unscored (D4
Current Ratio = N/A) because current-liability and trade-payables detail was
absent from the screener export. The operator has since supplied the audited
FY2026 + FY2025 standalone and consolidated financial statements (Q4 FY26 results,
28 May 2026) plus the Q1 FY27 results (11 Aug 2026, context only). This re-run
de-proxies Blocks B and D using those audited statements and resolves the cash-flag
question explicitly. **Net effect: classification moves from AVOID to AVERAGE**,
driven almost entirely by Block D's Current Ratio going from N/A (0) to a
computed 5/5 now that audited current-asset/current-liability detail exists — see
Classification Box and Decision Line below for the full mechanics, including why
this is not a "quality improvement," just a data-completeness fix.

Company: Finolex Cables Ltd (FINCABLES) | Run date: 2026-08-12 | Model: claude-sonnet-5

Data available: 10 years (FY2017 to FY2026). Scoring adapted to 10-year history.

Source files:
1. screener-Data_Sheet.csv (10-yr P&L/BS/CF history, FY2017-FY2026; the only
   populated screener export — Profit_Loss/Balance_Sheet/Cash_Flow/Quarters/
   Customization CSVs are header-only, no data cells).
2. Q4_FY26_Audited_Results_28May2026.pdf — scanned image PDF, read visually by
   page. Confirmed pages used: p3 (standalone+consolidated summary), p4
   (standalone P&L detail, FY26+FY25), p5 (standalone balance sheet), p6
   (standalone segment), p8 (standalone cash flow, FY26 vs FY25), p9
   (consolidated P&L), p10 (consolidated balance sheet), p11 (consolidated
   segment). AUDITED for FY26 and FY25 (both standalone and consolidated).
3. Q1_FY27_Results_11Aug2026.pdf — scanned image, UNAUDITED (limited review by
   Deloitte Haskins & Sells LLP), quarter ended 30-Jun-26. Context/momentum only,
   not scored (no comparable full-year figures, no cash flow statement in a
   quarterly filing).
4. FY2019-20 Annual_Report.pdf (STALE, 5+ years old) — used only for actual
   capex figures FY2019 (44.32) and FY2020 (32.33), carried forward from v1.

---

## FORMULA NOTES AND BASIS RECONCILIATION (stated once, applied throughout)

- **Screener basis mismatch, confirmed this run**: screener-Data_Sheet.csv's P&L
  and Balance Sheet sections are on a **CONSOLIDATED** basis (screener PAT
  FY26=713.72 matches audited consolidated PAT-owners 713.72 exactly, p9;
  screener Total Assets FY26=6,989.96 matches audited consolidated Total Assets
  6,989.96 exactly, p10; screener Reserves FY26=6,055.29 matches audited
  consolidated Other Equity 6,055.29, p10). But screener's Cash Flow section is
  **STANDALONE** (screener CFO FY26=49.08 and FY25=207.25 match the audited
  STANDALONE cash flow statement exactly, p8 — no consolidated cash flow
  statement is presented anywhere in this filing; Finolex Industries is
  equity-accounted, not line-item consolidated, so the standalone CF is the only
  one company discloses at the quarterly-results level). This means the 10-year
  cumulative CFO÷PAT ratio (B1) blends standalone CFO against consolidated PAT —
  flagged explicitly below, and cross-checked against a clean standalone-only
  FY25/FY26 ratio in the cash-flag resolution section.
- ROCE = EBIT ÷ (Total Assets − Current Liabilities). Screener has no separate
  ROCE/ROE row in this export, so both are **computed**. EBIT = PBT + Interest
  (consolidated basis, matching the consolidated capital-employed base, which
  includes the associate/JV investment — keeps numerator and denominator
  consistent: associate profit share is included in PBT, and the associate
  investment is included in capital employed).
- **Capital Employed, v1 vs v2**: v1 used a proxy (Equity Capital + Reserves +
  Borrowings = Total Assets − "Other Liabilities," since screener's own BS
  section does not split current vs non-current liabilities for any year). v2
  **replaces this proxy for FY2025 and FY2026 only** with the exact audited
  figure: Capital Employed = Total Assets − Total Current Liabilities
  (consolidated, p10). FY2017-FY2024 remain on the v1 proxy (no audited data for
  those years). Both bases are shown in the Block A table below.
- ROE = PAT ÷ average Net Worth (Equity Share Capital + Reserves, consolidated).
  FY2017 uses closing Net Worth only (no FY2016 opening balance). Unchanged from
  v1 — fully computable across all 10 years without any proxy.
- **FCF/Capex, v1 vs v2**: v1 used AR actuals for FY2019/FY2020 and a computed
  proxy (ΔNet Block+CWIP + Depreciation) for all other years including FY2025 and
  FY2026. v2 **replaces the FY2025 and FY2026 proxy with audited actuals**:
  capex (Purchase of PPE, incl. CWIP and intangibles, standalone cash flow) =
  154.28 (FY26, p8) and 236.43 (FY25, p8). FY2017-FY2024 unchanged from v1.
- **Working Capital Days / B4, v1 vs v2**: v1 could not compute this at all —
  Trade Payables were absent from every provided file. v2 now has audited Trade
  Payables for FY2025 and FY2026 only (standalone = consolidated, no MSME/other
  split affects the total): FY26 = 41.20+180.70 = 221.90 (p5); FY25 =
  35.66+206.06 = 241.72 (p5, "As at 31 March 2025" column). This still does not
  reach back to FY2017, so B4 is scored on a **2-year window (FY25→FY26), not
  the intended full-history latest-vs-earliest window** — stated as a limitation,
  not silently treated as the full 10-year trend.
- **Current Ratio / D4, v1 vs v2**: v1 could not compute this — no current
  asset/liability split existed anywhere in the provided data. v2 now has the
  full audited consolidated balance sheet (p10): Total Current Assets 3,531.97,
  Total Current Liabilities 419.61 (FY26). This is the single largest scoring
  change this run — see Block D.
- Basis used for WC-days components: **Revenue basis** throughout (Receivable
  Days = Receivables÷Revenue×365; Inventory Days = Inventory÷Revenue×365;
  Payable Days = Payables÷Revenue×365), per formula default; COGS basis not used.
- No PAT loss-to-profit swing in the window: PAT positive all 10 years
  (FY2017-FY2026), consolidated and standalone alike, so no synthetic-CAGR issue
  for C2.
- Block E (Shareholder Alignment) is scored 0/20 in full, per explicit operator
  instruction this run: no shareholding FILING was supplied (only a
  non-anchored screener.in screenshot showing promoters 35.86% stable, FII
  9.65%, DII 16.71% as of Jun 2026 — treated as non-anchored context, not scored,
  per instruction).

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

| FY | PBT | Interest | EBIT=PBT+Int | Cap. Employed | Basis | ROCE |
|---|---|---|---|---|---|---|
| 2017 | 503.68 | 4.29 | 507.97 | 2,142.12 | proxy (Eq.Cap+Res+Borrow) | 23.71% |
| 2018 | 549.14 | 1.44 | 550.58 | 2,429.80 | proxy | 22.66% |
| 2019 | 610.22 | 0.92 | 611.14 | 2,737.63 | proxy | 22.33% |
| 2020 | 512.05 | 1.55 | 513.60 | 3,011.65 | proxy | 17.06% |
| 2021 | 630.87 | 0.76 | 631.63 | 3,421.21 | proxy | 18.46% |
| 2022 | 786.63 | 1.52 | 788.15 | 3,930.85 | proxy | 20.05% |
| 2023 | 649.45 | 1.24 | 650.69 | 4,383.97 | proxy | 14.84% |
| 2024 | 863.79 | 2.03 | 865.82 | 4,963.92 | proxy | 17.44% |
| **2025** | **922.45** | **1.67** | **924.12** | **5,925.53** | **AUDITED: Total Assets 6,286.54 − Curr.Liab 361.01 (Q4 FY26 PDF p10, p5)** | **15.60%** |
| **2026** | **928.52** | **1.75** | **930.27** | **6,570.35** | **AUDITED: Total Assets 6,989.96 − Curr.Liab 419.61 (Q4 FY26 PDF p10)** | **14.16%** |

(FY2017-24: screener-Data_Sheet.csv L21-22, L39-41, proxy capital employed per
formula note, unchanged from v1. FY2025-26: audited consolidated PBT/Interest,
Q4 FY26 PDF p9; audited consolidated Total Assets and Current Liabilities, p10.)

v1 comparison: FY25/26 proxy ROCE were 16.76%/15.24%; audited actuals are
15.60%/14.16% — the proxy modestly overstated ROCE in both years because it
excluded some non-current liabilities (deferred tax 454.12, lease liabilities
13.29) from the capital-employed base that the exact formula includes.

- **A1 Median ROCE**: sorted {14.16, 14.84, 15.60, 17.06, 17.44, 18.46, 20.05,
  22.33, 22.66, 23.71}, median = (17.44+18.46)/2 = **17.95%** → band 15-19.9% →
  **Score 3** (unchanged from v1 — the two audited-corrected years were not the
  median-determining pair)
- **A2 Minimum single-year ROCE**: **14.16%** (FY2026, audited; was 14.84%/FY2023
  proxy in v1) → band 12-14.9% → **Score 3** (unchanged band)
- **A3 Median ROE**: PAT ÷ average Net Worth, consolidated, all 10 years fully
  computable (no proxy needed). FY2017 closing-only: 400.24/2,140.88=18.70%.
  FY2018-26: 14.45%, 15.77%, 13.62%, 14.38%, 16.33%, 12.16%, 13.99%, 13.42%,
  12.33%. Sorted: {12.16,12.33,13.42,13.62,13.99,14.38,14.45,15.77,16.33,18.70},
  median=(13.99+14.38)/2=**14.19%** → band 12-14.9% → **Score 2** (unchanged)
- **A4 ROCE trend, latest vs earliest**: FY2026 **14.16%** (audited) vs FY2017
  23.71% (proxy) = decline of **9.55pp** (was 8.47pp in v1, using the proxy FY26
  figure) → band >5pp decline → **Score 0** (unchanged band, magnitude worsened
  slightly on the more precise audited endpoint)

**Block A total = 3+3+2+0 = 8/20 (unchanged from v1; audited data sharpened the
FY25/26 anchors but did not move any band)**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — NOW AUDITED FOR FY25/FY26

| FY | CFO | PAT (consol.) | Capex | FCF | Capex basis |
|---|---|---|---|---|---|
| 2017 | 212.76 | 400.24 | N/A (no FY16 base) | N/A | — |
| 2018 | 235.68 | 330.11 | 34.97 | 200.71 | proxy |
| 2019 | 154.06 | 407.47 | 44.32 | 109.74 | AR p.103, actual |
| 2020 | 308.80 | 391.00 | 32.33 | 276.47 | AR p.103, actual |
| 2021 | 114.37 | 461.46 | 45.28 | 69.09 | proxy |
| 2022 | 473.05 | 599.14 | 85.66 | 387.39 | proxy |
| 2023 | 356.31 | 504.28 | 35.44 | 320.87 | proxy |
| 2024 | 576.90 | 651.69 | 199.87 | 377.03 | proxy |
| **2025** | **207.25** | **700.77** | **236.43** | **-29.18** | **AUDITED actual (Q4 FY26 PDF p8)** |
| **2026** | **49.08** | **713.72** | **154.28** | **-105.20** | **AUDITED actual (Q4 FY26 PDF p8)** |

(CFO: screener-Data_Sheet.csv L57, standalone basis, cross-checked exactly
against audited standalone CFO p8. PAT: consolidated, L24, cross-checked exactly
against audited consolidated PAT p9. Capex FY25/26: audited standalone cash flow,
"Purchase of PPE incl. CWIP and intangibles," p8.)

- **B1 Cumulative CFO ÷ Cumulative PAT (10yr)**: ΣCFO=2,688.26, ΣPAT=5,159.88,
  ratio=**0.521** → band 0.50-0.69 → **Score 1** (unchanged from v1; both
  components were already screener-sourced and now cross-checked exact against
  audited FY25/26 — see basis-mismatch note above: this ratio blends standalone
  CFO against consolidated PAT, understating true standalone cash conversion in
  years with material associate profit share)
- **B2 FCF-positive years**: 7 of 9 computable years positive (FY2018-24
  positive; FY2025, FY2026 now confirmed negative on **audited actual** capex,
  not proxy) = **77.8%** → band 75-99% → **Score 4** (unchanged from v1; FY26
  FCF is less negative on audited actual capex, -105.20 vs v1's proxy-based
  -171.40, but still negative, same band)
- **B3 Cumulative FCF ÷ Cumulative PAT** (matched FY2018-2026 window):
  ΣFCF=1,606.92, ΣPAT=4,759.64, ratio=**0.338** → band 0.20-0.39 → **Score 1**
  (unchanged band; ratio moved from 0.325 to 0.338 on audited FY25/26 capex)
- **B4 Change in WC Days, FY25→FY26 (2-year window only, not full history)**:
  Revenue basis. FY26: Receivable days 21.37 (370.08÷6,321.01×365) + Inventory
  days 59.08 (1,023.17÷6,321.01×365) − Payable days 12.81 (221.90÷6,321.01×365)
  = **67.64 days**. FY25: Receivable days 16.65 (242.56÷5,318.89×365) +
  Inventory days 49.19 (717.03÷5,318.89×365) − Payable days 16.58
  (241.72÷5,318.89×365) = **49.26 days**. Change = **+18.38 days increase** →
  band increased >15 days → **Score 0** (was N/A/0 in v1 for lack of any Trade
  Payables data; now scored on real audited evidence, same score, much higher
  confidence — and directionally consistent with the CFO collapse below)

**Block B total = 1+4+1+0 = 6/20 (same total as v1; B4 moved from a data-absence
0 to an evidence-based 0 — see cash-flag resolution below for the full read on
what's driving this)**

---

## CASH-FLAG RESOLUTION (explicit, per operator instruction)

**Verdict: this is a working-capital-timing event to monitor, not a genuine
cash-quality leak, and not INDETERMINATE — but the FY27 reversal is unconfirmed
on the data provided, so it should not be treated as fully resolved either.**

Evidence, all from the audited standalone cash flow statement (Q4 FY26 PDF p8):

- **Operating profitability before working capital improved**, not
  deteriorated: Operating profit before WC changes = 640.21 (FY26) vs 527.91
  (FY25), +21.3%. The earnings engine is intact.
- **The entire CFO collapse is traceable to two identified balance-sheet lines**:
  Inventories absorbed cash of 306.14 (FY26) vs 140.70 (FY25) — more than double;
  Trade receivables absorbed cash of 127.61 (FY26) vs 60.09 (FY25) — roughly
  double. Combined incremental absorption vs FY25 run-rate ≈ Rs233cr, which
  alone would have taken FY26 CFO from 49.08 back up into the 280-300cr range,
  in line with FY24's 576.90 order of magnitude being the outlier on the high
  side and FY25's 207.25 being closer to a normal run-rate.
- This is **consistent with, but not independently confirmed beyond,
  management's stated Middle East raw-material pre-buying explanation** (per
  operator brief) — the audited statements show the balance-sheet effect
  precisely (inventory +306cr) but do not, on their own, prove management's
  causal narrative; that requires the concall/MD&A commentary, not provided in
  this data set.
- **Standalone-only cash conversion (cleanest comparison, avoids the
  consolidated-PAT/standalone-CFO basis mismatch flagged above)**: CFO÷PAT
  FY26 = 49.08÷622.87 = **7.9%**; FY25 = 207.25÷544.40 = **38.1%**. CFO÷EBITDA
  (EBITDA = PBT+Interest+Depreciation, standalone) FY26 = 49.08÷868.08 =
  **5.7%**; FY25 = 207.25÷761.83 = **27.2%**. Both ratios corroborate a real,
  material, single-year cash-conversion air pocket in FY26 — this is not a
  benign rounding effect.
- **Revenue growth alone does not fully explain it**: standalone revenue grew
  18.8% YoY (6,321.01 vs 5,318.89) — that alone would mechanically require more
  working capital in absolute Rupee terms even at stable WC-day ratios, but WC
  days themselves rose 18.38 days (B4 above), so there is a genuine efficiency
  deterioration layered on top of the volume-driven effect, not purely a
  scaling artifact.
- **What is NOT FOUND, and therefore not resolved**: whether the inventory and
  receivables build unwinds in FY27. Q1 FY27 (30-Jun-26) results show revenue
  +44.3% YoY (2,013.15 vs 1,395.52) and PAT +59.4% YoY (221.28 vs 138.82) —
  strong momentum continuing — but the Q1 FY27 filing is a P&L-only limited
  review disclosure with **no cash flow statement**, so the working-capital
  unwind (or further build) cannot be confirmed from any document in this run.

Given CLAUDE.md's rule that cash-conversion ambiguity must not silently resolve
to a clean read, this is recorded as: **not INDETERMINATE (drivers are
evidenced), not a genuine leak (operating profit intact and growing), but an
unconfirmed-reversal working-capital-timing event** — flagged for the next
quarter's cash flow statement to close out. See `cash_flag_resolution` in the
YAML block.

---

## BLOCK C: GROWTH (Max 20) — unchanged from v1

Revenue (screener-Data_Sheet.csv L11, consolidated, cross-checked exact against
audited FY26 6,321.01 and FY25 5,318.89): FY2017=2,444.84 → FY2026=6,321.01.
PAT (L24, consolidated, cross-checked exact against audited FY26 713.72 and FY25
700.77): FY2017=400.24 → FY2026=713.72.

- **C1 Revenue CAGR** (9-year, FY2017-FY2026): (6,321.01/2,444.84)^(1/9)-1 =
  **11.13%** → band 10-14.9% → **Score 3**
- **C2 PAT CAGR** (9-year): (713.72/400.24)^(1/9)-1 = **6.64%** → band 5-9.9% →
  **Score 1**
- **C3 Positive YoY revenue years**: 2 declines of 9 transitions (FY2020:
  2,877.30 < FY2019's 3,077.79; FY2021: 2,768.11 < FY2020's 2,877.30 —
  pandemic-era years), 7 positive = **77.8%** → band 75-99% → **Score 3**
- **C4 PAT CAGR minus Revenue CAGR**: 6.64% − 11.13% = **-4.49pp** → band -3 to
  -8pp → **Score 1**

**Block C total = 3+1+3+1 = 8/20 (unchanged)**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — NOW FULLY AUDITED, LARGEST CHANGE THIS RUN

Latest year FY2026, consolidated (Q4 FY26 PDF p10):
Total Borrowings = 0.79 (non-current) + 0.07 (current) = 0.86; Cash & Cash
Equivalents = 163.13; Total Equity = 6,085.88; Total Current Assets = 3,531.97;
Total Current Liabilities = 419.61; EBIT (per Block A) = 930.27; Interest = 1.75.

- **D1 Net Debt ÷ EBITDA**: Net Debt = 0.86 − 163.13 = **-162.27 (net cash)** →
  **Score 5** (unchanged from v1; confirmed on audited consolidated figures
  rather than the screener proxy)
- **D2 Interest Coverage** (EBIT ÷ Interest): 930.27 ÷ 1.75 = **531.6x** → band
  ≥10x → **Score 5** (unchanged, audited-confirmed)
- **D3 Debt ÷ Equity**: 0.86 ÷ 6,085.88 = **0.0001x** → band <0.1 → **Score 5**
  (unchanged, audited-confirmed)
- **D4 Current Ratio (latest)**: 3,531.97 ÷ 419.61 = **8.42x** → band ≥2.0 →
  **Score 5** — **NEW THIS RUN**: v1 scored this N/A/0 because no current
  asset/liability split existed in any provided file. The audited consolidated
  balance sheet (p10) now provides it directly.

**Block D total = 5+5+5+5 = 20/20 (up from 15/20 in v1 — entirely a
data-completeness fix, not a change in the underlying business; the company was
always this liquid, it just wasn't provable from screener data alone)**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — 0/20, unscored per operator instruction

- **E1-E4**: all **N/A (not in provided data)** — no shareholding pattern
  FILING was supplied this run. The operator provided only a non-anchored
  screener.in screenshot (promoters 35.86% stable, FII 9.65%, DII 16.71%, as of
  Jun 2026) — this is context, not an anchorable filing, and is not scored per
  explicit instruction. → **Score 0/20**

**Block E total = 0/20 — a data-absence outcome, not a scored weakness.**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Only M3 (Capital Efficiency) changes this run, as a direct cascade from Block A's
audited FY26 ROCE correction (15.24% proxy → 14.16% audited). All other moat
tests are unchanged from v1 (screener-sourced, no audited-data dependency).

| # | Test | v1 Score | v2 Score | Basis |
|---|---|---|---|---|
| M1 | Pricing Power | 0 | 0 | EBITDA margin (computed, screener-basis = PBT−OI+Dep+Int, ÷Sales) fell from 16.20% (FY2017) to 9.80% (FY2026), a 6.4pp decline despite revenue CAGR 11.1% → "else 0". **Data note**: screener's FY26 Other Income (370.17) does not match either audited standalone (237.98, p4) or consolidated (165.63, p9) Other Income — an unresolved screener-source discrepancy, flagged but not recomputed (outside this run's Block B/D scope); does not change the 0 score given the size of the margin decline either way |
| M2 | Cost Advantage vs peer | 0 | 0 | **PEER DATA NEEDED** — no peer EBITDA margin data provided |
| M3 | Capital Efficiency | 3 | **1** | FAT (Sales÷Net Block, FY2026) = 6,321.01÷849.78 = 7.44x (>3x, also >2x, >1x). **ROCE now 14.16% audited** (was 15.24% proxy) — no longer >15%, still >12% → band "FAT>1x AND ROCE>12% = 1" (was band "FAT>2x AND ROCE>15% = 3" on the proxy figure) — **CHANGED** |
| M4 | Customer Stickiness | 1 | 1 | 2 revenue-decline years (FY2020, FY2021), overall CAGR positive → band 1, unchanged |
| M5 | Scale & Dominance | 0 | 0 | **PEER DATA NEEDED** |
| M6 | Technology/R&D | 0 | 0 | N/A — no R&D line disclosed |
| M7 | Regulatory/License | 0 | 0 | Unregulated segment |
| M8 | Distribution | 1 | 1 | Stale FY2019-20 AR narrative (5,000+ distributors; retailers 30,000→50,000) — unchanged, still stale |
| M9 | Brand | 0 | 0 | **PEER DATA NEEDED** (informational GM proxy only, not scored: 19.69% FY2017 vs 10.94% FY2026, declining) |
| M10 | Switching Costs | 1 | 1 | Overall growth, 2 decline years → band 1, unchanged |
| M11 | Network Effects | 0 | 0 | Latest 3yr revenue CAGR (12.14%) not greater than prior 3yr (15.93%), neither ≥20% → 0, unchanged |
| M12 | Negative WC/Float | 0 | 0 | Still N/A for the full-history test — FY17-24 Trade Payables absent; the 2-year FY25/26 window (49.26/67.64 days) is well above the 0-15 day band regardless → 0, unchanged conclusion |

**Block F (moat) total = 0+0+1+1+0+0+0+1+0+1+0+0 = 4/60 (down from 6/60 in v1,
driven entirely by the M3 audited-ROCE correction)**

Moat profile bars (score/5):
```
M1  Pricing Power        [          ] 0
M2  Cost Advantage       [PEER DATA NEEDED]
M3  Capital Efficiency   [=         ] 1  <- was 3 (CONFIRMED) in v1, now below the "present" threshold
M4  Customer Stickiness  [=         ] 1
M5  Scale & Dominance    [PEER DATA NEEDED]
M6  Technology/R&D       [          ] 0 (N/A)
M7  Regulatory/License   [          ] 0 (unregulated)
M8  Distribution         [=         ] 1
M9  Brand                [PEER DATA NEEDED]
M10 Switching Costs      [=         ] 1
M11 Network Effects      [          ] 0
M12 Negative WC/Float    [          ] 0 (N/A / evidenced weak)
```

**Moats confirmed (score ≥3): 0 (was 1 — Capital Efficiency — in v1)**
**Moat classification: 0 present = NONE (was THIN in v1)**

---

## CLASSIFICATION BOX

```
Core score        = A(8) + B(6) + C(8) + D(20) + E(0) = 42 / 100
Moat score         = 4 / 60
Moat classification = NONE (0 of 12 tests confirmed)
Data confidence     = 10 years (FY2017-FY2026) = "10+ yrs full" -- no downgrade
Classification matrix: Core 40-59 -> AVERAGE (moat class does not change this tier)

CLASSIFICATION: AVERAGE (was AVOID in v1)
Grand total (core + moat) = 42 + 4 = 46 / 160 (was 43/160 in v1)
```

**Why the classification moved (mechanics, not a quality judgment)**: v1 landed
in Core<40 -> AVOID because D4 (Current Ratio) scored 0 for lack of data,
holding core at 37. v2 supplies the audited current asset/liability split,
scoring D4 at 5/5 (Current Ratio 8.42x), lifting core to 42 -- one point above
the Core<40 threshold and squarely into the 40-59 AVERAGE band. This is a
**data-completeness correction, not an improvement in the underlying business**:
the company's liquidity was always this strong, it simply wasn't provable from
screener data alone. Working against this, Block F moat score fell from 6 to 4
(M3 Capital Efficiency no longer scores as "present") purely because the
audited FY26 ROCE (14.16%) is more precise than the FY26 proxy (15.24%) and
falls just under the 15% moat threshold -- a genuine, evidenced result, not a
data artifact.

**Deal-breaker check** (all 9 rules tested):
1. Block A <8 -> A=8, exactly at threshold, not triggered
2. Block B <8 -> **B=6, TRIGGERED** (cap: max GOOD -- non-binding, AVERAGE is
   already below GOOD)
3. Median ROCE <10% -> 17.95%, not triggered
4. Cumulative CFO/PAT <0.50 -> 0.521, not triggered (still a near-miss, 2pp
   above threshold, and this ratio blends standalone CFO with consolidated PAT
   -- see basis note; the cleaner standalone-only FY26 ratio is 7.9%, well
   below 0.50, but that is a single-year not cumulative figure so the rule as
   written is not triggered)
5. Pledge >15% -> data absent, cannot confirm, not triggered
6. ND/EBITDA >3x AND IC <3x -> net cash position, not triggered
7. Revenue declined majority of years -> 2 of 9 years, not majority, not
   triggered
8. PAT negative in any of last 3 years -> PAT positive FY2024-2026, not
   triggered
9. History <3 years -> 10 years available, not triggered

---

## STRONGEST / WEAKEST BLOCK

- **Strongest block: D (Balance Sheet Strength), 20/20 (100%)** — net-cash,
  negligible debt (D/E 0.0001x), interest coverage 531.6x, current ratio 8.42x.
  Fully audited-confirmed this run, no remaining gaps.
- **Weakest scored block: B (Cash Generation Quality), 6/20 (30%)** —
  cumulative cash conversion of 52% (10yr, basis-mismatched) and a confirmed
  FY2026 audited collapse to 7.9% standalone CFO/PAT are genuine, evidenced
  depressors — see Cash-Flag Resolution above for why this is a
  working-capital-timing event to monitor rather than a clean pass.
- **Lowest raw block: E (Shareholder Alignment), 0/20** — pure data-absence
  outcome (no shareholding filing provided this run), not a confirmed
  governance weakness.

---

## DECISION LINE

Classification: **AVERAGE** (core 42/100, moat NONE, 0 of 12 moat tests
confirmed) — up from v1's AVOID, driven entirely by resolving Block D's Current
Ratio gap with audited data (D: 15/20 -> 20/20), partly offset by a genuine,
evidenced downgrade in Block F's Capital Efficiency test (M3: 3 -> 1) once the
audited (rather than proxy) FY26 ROCE is used. Per pipeline rules this flags but
does not halt — flags propagate downstream, no STOP verdict exists.

The cash-conversion question (Block B, weakest scored block) is now resolved
with audited evidence rather than left as a screener-proxy inference: FY2026's
CFO collapse is a working-capital-timing event (inventory +306cr, receivables
+128cr, against an *improving* operating-profit-before-WC base of 640.21) most
plausibly tied to raw-material pre-buying, but its FY2027 reversal is
unconfirmed on any document in this run (Q1 FY27 filing has no cash flow
statement). This should be treated as an open item for the next quarterly cash
flow statement, not as resolved-clean.

Remaining unscored areas, unchanged from v1 and not addressed by this run's new
inputs: Block E (shareholding filing still absent — only a non-anchored
screenshot was supplied), M2/M5/M9 (peer data absent), and the full-history
B4/M12 working-capital-days tests (Trade Payables still absent for FY2017-2024,
only the 2-year FY25/26 window is now evidenced).

```yaml
stage: B01-gate0
company: "FINCABLES"
run_date: "2026-08-12"
model: claude-sonnet-5
status: complete
input_gaps:
  - "shareholding: ABSENT (filing) -- only a non-anchored screener.in screenshot supplied (promoters 35.86%, FII 9.65%, DII 16.71%, Jun 2026); Block E (E1-E4) scores 0/20 entirely, per explicit operator instruction not to score on the screenshot"
  - "rating: ABSENT"
  - "announcements: ABSENT"
  - "research: ABSENT"
  - "annual report provided is FY2019-20 vintage, 5+ years stale vs FY2026 audited results; used only for FY2019/FY2020 capex actuals and the (stale) M8 distribution narrative"
  - "Trade Payables absent for FY2017-FY2024 in all provided files (only FY25/FY26 now available from the audited balance sheet) -- B4 and M12 scored on a 2-year window only, not the intended full-history latest-vs-earliest window"
  - "Q1 FY27 filing (11 Aug 2026) is P&L-only, unaudited/limited-review, no cash flow statement -- cannot confirm whether the FY26 working-capital build unwinds in FY27"
  - "peer/industry comparator data absent -- caused M2, M5, M9 to score 0/PEER DATA NEEDED"
flags:
  - type: FLAG-GATE0
    reason: "Classification AVERAGE (core 42/100, moat NONE), up from v1's AVOID -- driven by resolving Block D's Current Ratio gap with audited data (D 15->20/20), partly offset by Block F's Capital Efficiency test dropping out of 'present' status (M3 3->1) once audited FY26 ROCE (14.16%, vs 15.24% proxy) is used. Genuine, evidenced depressors independent of data gaps: ROCE decline 23.71%->14.16% FY17-FY26 audited (A4=0), EBITDA margin compression 16.2%->9.8% (M1=0), PAT CAGR trailing revenue CAGR by 4.5pp (C4=1), and the FY26 cash-conversion air pocket (see FLAG-CASH below). Remaining unscored areas: Block E (shareholding filing absent), M2/M5/M9 (peer data absent), full-history B4/M12 (Trade Payables absent pre-FY25)."
  - type: FLAG-CASH
    reason: "FY2026 standalone CFO/PAT collapsed to 7.9% (49.08/622.87) from 38.1% (207.25/544.40) in FY2025, fully traceable in the audited standalone cash flow statement to inventory (+306.14cr) and trade receivables (+127.61cr) build against an IMPROVING operating-profit-before-WC-changes base (640.21 vs 527.91, +21.3%) -- classified as a working-capital-timing event to monitor, not a genuine cash-quality leak and not INDETERMINATE (drivers are evidenced), consistent with but not independently confirmed beyond management's stated Middle East raw-material pre-buying explanation. FY2027 reversal is UNCONFIRMED -- the Q1 FY27 filing has no cash flow statement. Caps confidence at PROCEED WITH CAVEATS-equivalent for any downstream stage relying on cash quality until a subsequent quarter's cash flow statement confirms the unwind."
data_years: 10
fy_range: "FY2017 to FY2026"
blocks: {A: 8, B: 6, C: 8, D: 20, E: 0}
core_score: 42
moat_score: 4
grand_total: 46
moats_confirmed: 0
moat_class: "NONE"
classification: "AVERAGE"
deal_breakers:
  - "Block B <8 (scored 6/20) -> cap max GOOD (non-binding, AVERAGE already below GOOD)"
history_downgrade: false
data_notes:
  - "No PAT loss-to-profit swing FY2017-FY2026; PAT positive all 10 years, consolidated and standalone"
  - "Screener basis mismatch confirmed this run: P&L and Balance Sheet sections of screener-Data_Sheet.csv are CONSOLIDATED (cross-checked exact vs audited FY26/FY25); Cash Flow section is STANDALONE (cross-checked exact vs audited standalone CF, no consolidated CF statement exists in this filing) -- affects B1's cumulative CFO/PAT ratio, which blends standalone CFO against consolidated PAT"
  - "ROCE computed (screener has no ROCE/ROE rows); EBIT=PBT+Interest, consolidated. Capital Employed FY2017-2024 = proxy (Eq.Cap+Reserves+Borrowings, current-liability split absent for those years); FY2025-2026 = exact audited (Total Assets - Total Current Liabilities, consolidated)"
  - "FY2017 ROE uses closing Net Worth only, no FY2016 opening balance available"
  - "Capex: AR actuals FY2019 (44.32) and FY2020 (32.33); AUDITED actuals FY2025 (236.43) and FY2026 (154.28) this run, replacing v1's proxy for those two years; FY2018/2021-2024 remain computed proxy (Delta Net Block+CWIP + Depreciation); FY2017 capex not computable"
  - "Trade Payables now available FY2025 (241.72) and FY2026 (221.90) from the audited balance sheet; still absent FY2017-2024 -- B4 and M12 scored on the 2-year window only, stated as a limitation"
  - "M1 data note: screener's FY26 Other Income (370.17) does not reconcile to either audited standalone (237.98) or consolidated (165.63) Other Income -- unresolved screener-source discrepancy, flagged, not recomputed (outside this run's Block B/D scope, does not change M1's score)"
  - "M3 changed this run: 3->1, direct cascade of the audited FY26 ROCE correction (14.16% vs 15.24% proxy), crossing below the 15% moat threshold"
  - "M8 Distribution still scored from stale FY2019-20 AR narrative, not FY2026 reality"
  - "M9 Brand: informational GM proxy computed (19.69% FY2017 vs 10.94% FY2026, declining) but not scored -- no peer data"
  - "PEER DATA NEEDED: M2, M5, M9"
  - "Q1 FY27 context only, not scored: standalone revenue +44.3% YoY (2,013.15 vs 1,395.52), PAT +59.4% YoY (221.28 vs 138.82) -- strong momentum continuing but no cash flow statement in this unaudited quarterly filing, so cannot confirm FY26 working-capital unwind"
block_b_trend: "deteriorating, now audited-confirmed -- standalone CFO/PAT cash conversion fell from 38.1% in FY2025 (CFO 207.25/PAT 544.40) to 7.9% in FY2026 (CFO 49.08/PAT 622.87), fully traceable to inventory (+306.14cr) and receivables (+127.61cr) build against an improving operating-profit-before-WC base (640.21 vs 527.91); FCF negative both years (-29.18 FY25, -105.20 FY26 on audited actual capex); classified as working-capital-timing to monitor, not a genuine leak, per FLAG-CASH -- FY2027 reversal unconfirmed"
data_basis: "Blocks B and D are scored from AUDITED FY2026/FY2025 standalone and consolidated financial statements (Q4_FY26_Audited_Results_28May2026.pdf) this run, replacing v1's screener-proxy figures for those two years; Blocks A and C retain the v1 screener-proxy basis for FY2017-2024 (no audited data available for those years) with FY2025/2026 endpoints now audited-confirmed; Block E remains entirely unscored per explicit operator instruction (no shareholding filing supplied)."
cash_flag_resolution: "NOT INDETERMINATE and NOT a genuine cash-quality leak -- classified as a working-capital-timing event to monitor. Audited evidence: FY2026 standalone CFO/PAT fell to 7.9% (49.08/622.87) from 38.1% (207.25/544.40) in FY2025, entirely traceable to inventory (+306.14cr) and trade receivables (+127.61cr) absorption in the audited standalone cash flow statement, against an IMPROVING operating-profit-before-working-capital-changes base (640.21 vs 527.91, +21.3%). Consistent with, but not independently confirmed beyond, management's stated Middle East raw-material pre-buying explanation. Missing evidence that prevents full resolution: no cash flow statement exists in the Q1 FY27 filing, so the FY2027 unwind (or further build) of this working capital cannot be confirmed from any document in this run. Per CLAUDE.md, this caps at a caveated read (see FLAG-CASH) rather than resolving silently to clean; downstream stages relying on cash-conversion quality should treat FY2026 as an open, evidenced-but-unconfirmed-reversal item pending the next quarterly cash flow statement."
```
