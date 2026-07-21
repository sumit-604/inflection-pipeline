# STAGE 1 — GATE 0 SCORECARD
**Company:** K.C.P. Sugar and Industries Corporation Ltd (KCPSUGIND)
**Run date:** 2026-07-21
**Sector note:** Sugar producer (cyclical commodity agri-processor: sugar, cogeneration power, industrial alcohol/ethanol, bio-fertilizers, calcium lactate, CO2) — NOT Pharma/CDMO as the manifest auto-picked. This correction carries forward to all downstream stages.

Data available: 10 years (FY2017 to FY2026). Scoring adapted to 10-year history.

**Primary source:** screener.in Data_Sheet CSV (`runs/kcpsugind-2026-07-21/inputs/screening/screener-Data_Sheet.csv`) — P&L, balance sheet and cash-flow line items, FY2017–FY2026, plus quarterly Q3FY24–Q4FY26 (quarterly data not used for annual scoring; no promoter-holding or peer fields present in any provided file).
**Supplementary source:** Annual Report FY2020-21 (`runs/kcpsugind-2026-07-21/inputs/annual-report/Annual_Report.pdf`) — used ONLY for contextual notes (contingent liabilities, R&D spend, industry structure). This AR is 5 years stale relative to the FY2026 data in the CSV and is never used to fill "latest" scoring fields.
**Balance_Sheet.csv and Cash_Flow.csv supplementary exports are empty templates** (no data rows) — confirmed by direct read; all balance-sheet and cash-flow figures below come from the Data_Sheet CSV only.

**NO-CONCALL MODE.** run_type: full, no results PDFs, no rating, no shareholding, no announcements, no research, no presentation. This scorecard is built entirely from the screener Data_Sheet CSV per the documented degradation path.

---

## RAW DATA EXTRACTED (screener Data_Sheet CSV, all Rs. Crore unless noted)

| FY | Sales | RM Cost | Other Income | Depreciation | Interest | PBT | Tax | PAT |
|----|------:|------:|------:|------:|------:|------:|------:|------:|
|2017|442.17|242.86|35.61|9.71|11.53|73.67|16.51|57.17|
|2018|351.41|295.63|61.85|9.40|14.79|-3.00|-14.50|11.50|
|2019|359.44|362.04|15.55|8.70|19.76|33.93|17.63|16.31|
|2020|392.62|264.27|13.85|8.04|21.86|-10.76|-4.50|-6.26|
|2021|328.55|168.74|47.67|6.36|24.36|17.12|-6.19|23.30|
|2022|319.40|174.02|16.04|5.18|19.70|5.16|1.58|3.58|
|2023|289.52|204.18|84.62|5.50|14.29|70.21|12.03|58.17|
|2024|345.68|190.83|76.63|5.88|11.19|78.87|12.70|66.16|
|2025|310.46|178.03|31.36|6.07|9.11|28.02|13.63|14.39|
|2026|259.95|192.46|28.56|5.95|7.75|15.73|4.60|11.13|
(screener Data_Sheet CSV, P&L rows, FY2017–FY2026)

| FY | Equity Cap. | Reserves | Borrowings | Other Liab. | Net Block | Receivables | Inventory | Cash&Bank |
|----|------:|------:|------:|------:|------:|------:|------:|------:|
|2017|11.34|270.62|139.87|125.85|107.56|32.96|225.15|16.00|
|2018|11.34|270.45|208.65|99.12|100.39|28.75|219.84|21.83|
|2019|11.34|285.76|220.50|179.79|98.82|28.43|378.69|17.70|
|2020|11.34|277.88|265.24|121.46|91.84|37.12|344.67|19.29|
|2021|11.34|301.96|270.35|59.54|91.13|46.30|261.58|13.54|
|2022|11.34|303.94|189.56|72.91|91.54|29.31|215.48|26.11|
|2023|11.34|361.51|183.60|71.42|99.49|22.11|230.29|49.19|
|2024|11.34|427.34|146.67|80.42|100.50|29.20|204.75|46.91|
|2025|11.34|438.94|99.33|69.08|98.91|48.62|133.38|47.93|
|2026|11.34|448.17|127.71|72.54|99.22|57.40|155.78|39.35|
(screener Data_Sheet CSV, balance sheet rows, FY2017–FY2026)

| FY | CFO | CFI | CFF |
|----|------:|------:|------:|
|2017|49.66|-92.72|35.90|
|2018|-70.18|7.40|68.60|
|2019|-52.09|29.12|17.39|
|2020|26.96|-1.10|-23.33|
|2021|17.44|-10.91|-11.15|
|2022|114.31|0.84|-101.62|
|2023|7.17|26.75|-15.20|
|2024|42.46|-7.07|-50.38|
|2025|47.79|3.33|-53.94|
|2026|-30.89|6.09|19.51|
(screener Data_Sheet CSV, cash flow rows, FY2017–FY2026)

**Data-granularity gap disclosed up front:** the CSV does not itemize (a) capex / purchase-of-PPE within Cash from Investing Activity, (b) Trade Payables separately from "Other Liabilities," or (c) Current Assets/Current Liabilities separately from the aggregate "Other Assets"/"Other Liabilities" lines. These gaps make FCF (B2, B3), Working Capital Days (B4), Current Ratio (D4) and Negative-WC float (M12) **NOT FOUND** — not estimated — and scored 0 per the "never estimate" rule. Each is flagged below at point of use.

---

## FORMULA CONVENTIONS USED (stated per instructions)

- **EBIT** = PBT + Interest (screener Data_Sheet CSV, standard add-back; Depreciation and Other Income are already embedded in the given PBT line).
- **EBITDA** = EBIT + Depreciation (screener Data_Sheet CSV, Depreciation row).
- **Capital Employed** (for ROCE) = Equity Share Capital + Reserves + Borrowings (screener Data_Sheet CSV convention: "Other Liabilities" treated as current liabilities and excluded, consistent with screener.in's own simplified Data Sheet methodology). Stated as "computed," not sourced from a screener-published ROCE figure (none was provided in this export).
- **Net Worth** (for ROE) = Equity Share Capital + Reserves (screener Data_Sheet CSV).
- **ROE FY2017**: opening Net Worth (FY2016) unavailable — closing Net Worth used only, stated so per instructions.
- **Net Debt** = Borrowings − Cash & Bank (screener Data_Sheet CSV, both explicit line items).

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: **0/20**

Capital Employed (Rs Cr) by year = Equity Cap + Reserves + Borrowings:
FY17 421.83 | FY18 490.44 | FY19 517.60 | FY20 554.46 | FY21 583.65 | FY22 504.84 | FY23 556.45 | FY24 585.35 | FY25 549.61 | FY26 587.22 (computed, screener Data_Sheet CSV)

EBIT (Rs Cr) = PBT+Interest: FY17 85.20 | FY18 11.79 | FY19 53.69 | FY20 11.10 | FY21 41.48 | FY22 24.86 | FY23 84.50 | FY24 90.06 | FY25 37.13 | FY26 23.48 (computed, screener Data_Sheet CSV)

**ROCE by year** (computed): FY17 20.20% | FY18 2.40% | FY19 10.37% | FY20 2.00% | FY21 7.11% | FY22 4.92% | FY23 15.19% | FY24 15.39% | FY25 6.75% | FY26 4.00%

- **A1 Median ROCE = 6.93%** (median of 10-year series, computed) → <10% → **Score 0**
- **A2 Minimum single-year ROCE = 2.00%** (FY20, computed) → <8% → **Score 0**
- **A3 Median ROE = 4.86%** (computed; ROE series below) → <12% → **Score 0**
- **A4 ROCE trend, latest (FY26 4.00%) vs earliest (FY17 20.20%) = decline of 16.20pp** (computed) → decline >5pp → **Score 0**

Net Worth (Rs Cr) = Equity Cap+Reserves: FY17 281.96 | FY18 281.79 | FY19 297.10 | FY20 289.22 | FY21 313.30 | FY22 315.28 | FY23 372.85 | FY24 438.68 | FY25 450.28 | FY26 459.51 (computed, screener Data_Sheet CSV)

**ROE by year** (computed; FY17 uses closing NW only, opening unavailable): FY17 20.28% | FY18 4.08% | FY19 5.63% | FY20 -2.14% | FY21 7.73% | FY22 1.14% | FY23 16.91% | FY24 16.31% | FY25 3.24% | FY26 2.45%

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: **1/20**

- **B1 Cumulative CFO ÷ Cumulative PAT**: Cumulative CFO (FY17–FY26) = Rs 152.63 Cr (computed, sum of screener Data_Sheet CSV CFO rows). Cumulative PAT = Rs 255.45 Cr (computed, sum of screener Data_Sheet CSV PAT rows). Ratio = **0.598** → band 0.50–0.69 → **Score 1**
- **B2 FCF-positive years as proportion**: **NOT FOUND**. Screener Data_Sheet CSV gives only aggregate "Cash from Investing Activity," with no capex/purchase-of-PPE breakout, so FCF = CFO − Capex cannot be computed without estimating capex, which is prohibited. **Score 0**, data gap noted.
- **B3 Cumulative FCF ÷ Cumulative PAT**: **NOT FOUND** for the same reason as B2. **Score 0**.
- **B4 Change in WC Days, latest vs earliest**: **NOT FOUND**. Receivable Days and Inventory Days are computable (Receivables and Inventory are explicit line items) but Trade Payables is not a separate line item in the Data_Sheet CSV (bundled inside "Other Liabilities" along with provisions and other current items), so Payable Days — and therefore total WC Days — cannot be computed without estimating the payables split. **Score 0**, data gap noted.

**block_b_trend: deteriorating** — the one number that shows it: **FY26 CFO = −Rs 30.89 Cr vs FY25 CFO = +Rs 47.79 Cr** (screener Data_Sheet CSV), a swing of −Rs 78.68 Cr in a single year, the only negative CFO print in the most recent four years. Cumulative 10-year CFO/PAT of 0.598 also sits below 1.0, i.e. cash realization has lagged reported profit over the full window.

---

## BLOCK C: GROWTH (Max 20) — Score: **0/20**

- **C1 Revenue CAGR (FY17→FY26, 9-year)**: (259.95/442.17)^(1/9)−1 = **−5.73%** (computed) → negative → **Score 0**
- **C2 PAT CAGR (FY17→FY26)**: both endpoints positive (FY17 57.17, FY26 11.13) so CAGR is computed, not N/M: (11.13/57.17)^(1/9)−1 = **−16.6%** (computed) → negative → **Score 0**. *Data note: FY20 PAT was −Rs 6.26 Cr (a loss year) inside this window; endpoints themselves are both positive so this is a valid CAGR, not a loss-to-profit swing calculation, but the FY20 loss year is flagged for context.*
- **C3 Positive YoY revenue years proportion**: of 9 YoY comparisons (FY18–FY26), only 3 were positive (FY19, FY20, FY24) = **33.3%** (computed) → <50% → **Score 0**
- **C4 PAT CAGR minus Revenue CAGR**: −16.6% − (−5.73%) = **−10.87pp** (computed) → <−8pp → **Score 0**

YoY revenue detail (screener Data_Sheet CSV, computed): FY18 ↓20.5% | FY19 ↑2.3% | FY20 ↑9.2% | FY21 ↓16.3% | FY22 ↓2.8% | FY23 ↓9.4% | FY24 ↑19.4% | FY25 ↓10.2% | FY26 ↓16.3%

**Deal-breaker #7 triggered: revenue declined in 6 of 9 years (FY18, FY21, FY22, FY23, FY25, FY26) — a majority.**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: **6/20**

- **D1 Net Debt ÷ EBITDA (latest, FY26)**: Net Debt = Borrowings(127.71) − Cash&Bank(39.35) = **Rs 88.36 Cr** (computed, screener Data_Sheet CSV). EBITDA FY26 = EBIT(23.48)+Dep(5.95) = **Rs 29.43 Cr** (computed). Ratio = **3.00x** → >3x → **Score 0**
- **D2 Interest Coverage EBIT÷Interest (latest, FY26)**: 23.48/7.75 = **3.03x** (computed) → band 3–4.9x → **Score 2**
- **D3 Debt÷Equity (latest, FY26)**: Borrowings(127.71)/NetWorth(459.51) = **0.278x** (computed) → band 0.1–0.5 → **Score 4**
- **D4 Current Ratio (latest)**: **NOT FOUND**. Data_Sheet CSV has no Current Assets/Current Liabilities split (Receivables, Inventory, Cash and Investments are given individually but not classified current vs. non-current; "Other Liabilities" and "Other Assets" are undifferentiated aggregates). **Score 0**, data gap noted.

**Near-miss flag on deal-breaker #6**: ND/EBITDA = 3.00x (just over the >3x threshold) and Interest Coverage = 3.03x (just over 3x). Deal-breaker #6 (ND/EBITDA>3x AND IC<3x → AVOID) requires IC<3x, and 3.03x narrowly fails that condition, so #6 is **not** triggered — but the company sits directly on this edge and should be treated as fragile on leverage regardless of the technical non-trigger.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: **0/20**

- **E1 Promoter holding (latest quarter)**: **NOT FOUND** — no shareholding-pattern file provided in this run (confirmed absent per run manifest). **Score 0**
- **E2 Promoter holding change over 3 years**: **NOT FOUND** — same reason. **Score 0**
- **E3 Promoter pledge (latest)**: **NOT FOUND** — same reason. **Score 0**
- **E4 Contingent liabilities ÷ Net Worth (latest)**: **NOT FOUND** for the current period — no contingent-liability disclosure in the screener CSV. *Context only, not scored*: AR FY20-21 Note 44 discloses contingent liabilities of Rs 7.76 Cr (demands: share transmission, labour cases, non-enrolment of contract labour for PF, captive power duty case, VAT case) (AR FY21 p.106, Note 44b) plus outstanding bank guarantees of Rs 2.50 Cr (AR FY21 p.106, Note 44a), against FY21 Net Worth of Rs 313.30 Cr (computed) ≈ 3.3% — but this is 5 years stale and cannot stand in for "latest." **Score 0**

Per CLAUDE.md: low institutional ownership is never itself treated as a risk; this is moot here since no ownership data exists at all to classify as low or high.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: **0/60**

| Test | Result | Score | Basis |
|---|---|---|---|
| M1 Pricing Power | EBITDA margin fell from 21.46% (FY17) to 11.32% (FY26), a decline of >5pp (computed), with negative revenue CAGR (no growth) | **0** | screener Data_Sheet CSV, computed |
| M2 Cost Advantage vs peer margin | No peer margin data provided | **0 — PEER DATA NEEDED** |  |
| M3 Capital Efficiency | FAT (Sales/Net Block) FY26 = 259.95/99.22 = 2.62x (computed); ROCE FY26 = 4.00%. Neither FAT>2x&ROCE>15% nor FAT>1x&ROCE>12% bands met | **0** | computed |
| M4 Customer Stickiness | 6 of 9 YoY periods were revenue-decline years (≥3 decline years band) | **0** | computed |
| M5 Scale & Dominance | No segment market-cap/peer data provided | **0 — PEER DATA NEEDED** |  |
| M6 Technology/R&D | No R&D spend disclosed in screener CSV for current years (AR FY21 shows Rs 0.49 Cr R&D spend (AR FY21 p.59) but is 5 years stale and not usable for "consistently" test) | **0 — PEER DATA NEEDED / NOT FOUND** |  |
| M7 Regulatory/License | Listed-player count in the regulated sugar segment not sourced from any provided document | **0 — PEER DATA NEEDED** |  |
| M8 Distribution | No distribution-reach data disclosed; sugar sold as bulk commodity | **0** |  |
| M9 Brand | GM proxy (Revenue−Raw Material Cost)/Revenue FY26 = (259.95−192.46)/259.95 = 25.96% (computed, proxy stated), but no peer median GM to compare against | **0 — PEER DATA NEEDED** | proxy computed but unscoreable without peer data |
| M10 Switching Costs | Revenue did not grow overall across the window (negative CAGR); "else 0" band applies | **0** | computed |
| M11 Network Effects | ≥6-year two-window test available. Latest-3yr CAGR (FY23→FY26) = −3.53% vs prior-3yr CAGR (FY20→FY23) = −9.65% (both computed) — technically "latest > prior" but both windows are contractions, not growth; FY26 selling-expense figure is blank in the CSV so the selling-% trend cannot be verified either | **0** | computed; scored conservatively given both windows are revenue contractions, not the growth pattern this test is designed to detect |
| M12 Negative WC/Float | **NOT FOUND** — Payable Days not computable (see B4), so WC Days cannot be tested | **0** | data gap |

**Moats confirmed (score ≥3): 0. Moat classification: NONE.**

---

## CLASSIFICATION

**Data confidence: 10 years (FY2017–FY2026) → "full" tier, no history-based downgrade.** (Note: this reflects P&L year-count only; several balance-sheet/cash-flow sub-line-items needed for full scoring were structurally absent from the export, as documented above — this is a *disclosure-granularity* gap, not a *history-length* gap, and does not change the data-confidence tier per the stated rule.)

| Block | Score | /Max |
|---|---:|---:|
| A — Return on Capital | 0 | 20 |
| B — Cash Generation Quality | 1 | 20 |
| C — Growth | 0 | 20 |
| D — Balance Sheet Strength | 6 | 20 |
| E — Shareholder Alignment | 0 | 20 |
| **Core Score** | **7** | **100** |
| F — Moat Score | 0 | 60 |
| **Grand Total** | **7** | **160** |

**Classification matrix**: Core score 7 falls in the "Core <40" band → base classification **AVOID**.

**Deal-breakers triggered:**
1. Block A <8 (=0) → caps at max GOOD
2. Block B <8 (=1) → caps at max GOOD
3. Median ROCE <10% (=6.93%) → caps at max AVERAGE
7. Revenue declined in majority of years (6 of 9) → caps at max AVERAGE

Deal-breakers not triggered: #4 (cumulative CFO/PAT = 0.598, ≥0.50), #5 (pledge NOT FOUND, cannot be assessed as triggered), #6 (ND/EBITDA>3x but IC = 3.03x fails the <3x condition — narrow non-trigger, flagged above), #8 (PAT positive in each of the last 3 years: FY24 66.16, FY25 14.39, FY26 11.13), #9 (10 years of history, well above the 3-year floor).

Because the base classification (AVOID) is already the floor of the classification set, the deal-breaker "caps" (which only restrict classification from going *above* GOOD or AVERAGE) do not change the outcome — **AVOID stands**.

### Strongest / weakest block
**Weakest (three-way tie at 0/20):** Blocks A (Return on Capital), C (Growth), E (Shareholder Alignment). Block E is the weakest in an evidentiary sense — every field is NOT FOUND rather than a substantively bad number, reflecting a missing-data gap rather than a demonstrated governance problem, and should not be read as an alignment red flag on its own.
**Least-weak block:** D (Balance Sheet Strength) at 6/20 — driven by low leverage (D/E 0.28x) and moderate interest coverage (3.03x), but undercut by a Net Debt/EBITDA ratio sitting right at the 3x ceiling.

### Decision line
**Gate 0 verdict: AVOID.** Core score 7/100 and moat score 0/60 reflect a structurally weak return-on-capital and growth profile (median ROCE 6.93%, median ROE 4.86%, revenue CAGR −5.73% over 9 years, PAT CAGR −16.6%) sitting on top of a fragile-but-not-yet-critical balance sheet (Net Debt/EBITDA 3.00x, Interest Coverage 3.03x — both essentially at the AVOID-deal-breaker edge) and a cash-conversion profile that turned negative in the most recent year (FY26 CFO −Rs 30.89 Cr). Per CLAUDE.md, this AVOID/quality signal propagates as a flag; it does not itself halt the pipeline, since only mechanical failures halt runs. Several scoring inputs (promoter holding/pledge, FCF, WC days, current ratio, all peer-dependent moat tests) are NOT FOUND rather than estimated, per the "never estimate" rule, and are listed as input gaps below for downstream stages to weigh explicitly.

---
