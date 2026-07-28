# STAGE 1 — GATE 0 SCORECARD: Dynacons Systems & Solutions Ltd (DSSL)
Run date: 2026-07-27 | Model: claude-sonnet-5 | Mode: pipeline (no human-in-loop)

Data available: 10 years (FY2017 to FY2026). Scoring adapted to 10-year history.
Company: IT systems integration & Technology Workforce Augmentation Services provider, incorporated 1995 (CIN L72200MH1995PLC093130), listed BSE (532365) / NSE (DSSL). Promoters: Shirish M. Anjaria, Dharmesh S. Anjaria, Parag J. Dalal (Acuité PR 31-Dec-2025, p.1). Long operating history — history_downgrade rule (reserved for 3-4yr LIMITED tier) does NOT apply.

Data sources used: screener.in Data_Sheet.csv (P&L/BS/CF FY2017-FY2025 + FY2026 P&L/BS, price, quarters block) = (screener-data); FY26 audited standalone+consolidated results (results FY26 audited, p.2-9); Q3/9M FY26 unaudited results (results Q3FY26, p.6-8); Acuité Ratings PR dated 31-Dec-2025 (Acuité PR 31-Dec-2025, p.N); FY25 Annual Report (AR FY25, p.N) for Block E contingent liabilities (FY26 AR not yet published); operator-supplied screener.in quarterly Shareholding Pattern, treated as ANCHORED-EQUIVALENT (screener SHP, <quarter>), for Block E promoter-holding level and trend (received mid-run as a gap-fill for the empty inputs/shareholding/ folder).

METHODOLOGY NOTES (read before scores):
1. EBIT = PBT + Interest − Other Income (excludes non-operating other income; validated against Acuité's independently stated FY25 metrics — see cross-checks below).
2. EBITDA = Sales − Raw Material Cost − Employee Cost − Other Expenses − Power&Fuel − Other Mfr. Exp − Selling&Admin + Change in Inventory (screener's "Change in Inventory" carries the opposite sign convention to the raw P&L filing's "Changes in Inventories" line — verified by reconciling FY24 (7.62%) and FY25 (8.31%) computed margins against Acuité's independently stated EBITDA margins of 7.63% and 8.31% (Acuité PR 31-Dec-2025, p.2) — exact match confirms formula and sign convention).
3. Capital Employed (CE) for ROCE: screener's Data_Sheet does not split Current vs Non-Current liabilities for FY2017-FY2024, so CE for those years = Net Worth + Total Borrowings (screener "Borrowings" line, which itself bundles interest-bearing debt AND lease liabilities under Ind AS 116 — confirmed by reconciling FY25 screener Borrowings of Rs138.84cr against Acuité's stated FY25 gearing of 0.60x on Net Worth Rs230.92cr = Rs138.55cr, and against AR Note 32.7 capital-management figures once lease liabilities are added back). For FY2025 and FY2026, the audited results give full Current Liabilities, so CE = Total Assets − Current Liabilities (precise formula) is used for those two years. Stated explicitly as "computed, hybrid CE basis" per every ROCE figure below.
4. Capex = "Purchase of Property, Plant and Equipment" line only (excludes CWIP reclass/timing adjustments). Granular PPE-only breakdown is available only for FY25-FY26 (from the FY26 audited CF statement, which carries FY25 comparatives); for FY2017-FY2024 the only capex proxy available in provided data is the aggregate "Cash from Investing Activity" line (screener-data) — stated as proxy.
5. Trade Payables are NOT broken out in the screener Data_Sheet (folded into "Other Liabilities") for FY2017-FY2024. Only FY2025/FY2026 payables are available (from the audited BS breakdown in the FY26 results filing). This limits Working-Capital-Days trend analysis (B4, M12) to the 2 years where all three components (receivables, inventory, payables) are available — stated as a data gap, not estimated.
6. Block E gap-fill: the operator supplied a screener.in quarterly Shareholding Pattern mid-run (runs/dssl-2026-07-27/inputs/shareholding/OPERATOR_screener_shp.md, Sep-2023 through Jun-2026, quarterly promoter/FII/DII/public % and shareholder count), treated as ANCHORED-EQUIVALENT (screener class). This resolves the promoter-holding staleness that would otherwise have applied (E1/E2 now current to Jun-2026, not the FY25 AR's Mar-2025 cut). The SHP table does NOT carry a pledge/encumbrance column, so E3 (promoter pledge) remains NOT FOUND — not estimated as 0% or otherwise. Contingent liabilities (E4) still rely on the FY25 Annual Report since the FY26 AR (with notes to accounts) is not yet published as of run date — that piece of Block E remains on a Mar-2025 basis, flagged.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Per-year EBIT (screener-data, PBT+Interest−Other Income) and Capital Employed (hybrid, see note 3):

| FY | EBIT (Cr) | CE (Cr) | ROCE |
|----|-----------|---------|------|
| 2017 | 4.11 | 40.53 (proxy: NW20.43+Borrow20.10) | 10.14% |
| 2018 | 6.13 | 58.78 (proxy) | 10.43% |
| 2019 | 12.24 | 67.33 (proxy) | 18.18% |
| 2020 | 13.60 | 74.21 (proxy) | 18.33% |
| 2021 | 17.33 | 93.10 (proxy) | 18.61% |
| 2022 | 29.26 | 132.11 (proxy) | 22.15% |
| 2023 | 53.32 | 173.39 (proxy) | 30.75% |
| 2024 | 76.56 | 193.39 (proxy) | 39.59% |
| 2025 | 103.71 | 302.60 (precise: TotalAssets777.19−CurrLiab474.59) | 34.28% |
| 2026 | 131.39 | 435.47 (precise: TotalAssets1012.99−CurrLiab577.52) | 30.17% |

All figures (screener-data for FY17-25 P&L/BS; results FY26 audited consol p.2/4 for FY26 EBIT and CE inputs; results FY26 audited consol p.4 for FY25 Current Liabilities comparative).

**A1 Median ROCE = 20.38%** (sorted median of 10 values, midpoint of 18.61% and 22.15%) → band 20-24.9% → **Score 4**
**A2 Minimum single-year ROCE = 10.14% (FY2017)** → band 8-11.9% → **Score 1**
**A3 Median ROE = 23.84%** (see table below) → band ≥20% → **Score 5**
**A4 ROCE trend, FY2026 (30.17%) vs FY2017 (10.14%)**: latest ≥ earliest (+20.0pp) → **Score 5**

ROE table (PAT ÷ average Net Worth; opening NW unavailable for FY2017, closing NW used and stated):
FY17 PAT1.21/NW20.43(closing, opening unavail.)=5.92%; FY18 2.10/avg21.87=9.60%; FY19 5.17/avg27.61=18.73%; FY20 5.71/avg34.46=16.57%; FY21 8.54/avg43.31=19.72%; FY22 16.43/avg58.78=27.96%; FY23 33.45/avg86.37=38.73%; FY24 53.83/avg131.20=41.02%; FY25 72.39/avg194.31=37.26%; FY26 84.74/avg273.03=31.03% (screener-data, PAT and NW as tabulated).
Median = avg(19.72, 27.96) = 23.84%.

**BLOCK A TOTAL = 4+1+5+5 = 15/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

CFO by year (Rs Cr): FY17 4.42, FY18 −12.92, FY19 4.04, FY20 4.29, FY21 9.07, FY22 −13.36, FY23 13.13, FY24 29.25, FY25 66.04 (screener-data, all); FY26 46.13 (results FY26 audited, consol CF statement p.8 — "Net Cash Flow from operating activities" Rs4,613.45 lakh; screener Data_Sheet FY26 CFO cell is blank).

**B1 Cumulative CFO ÷ Cumulative PAT** = Rs150.09cr ÷ Rs283.57cr = **0.529** → band 0.50-0.69 → **Score 1** (note: 0.529 is within 3% of the 0.50 deal-breaker-4 threshold — a near miss, not triggered).

Capex by year (Rs Cr, see methodology note 4): FY17 0.30, FY18 0.58, FY19 0.37, FY20 0.05, FY21 2.82, FY22 1.17, FY23 0.30, FY24 0.54 (screener-data, "Cash from Investing Activity" proxy); FY25 5.36 (results FY26 audited, consol CF statement p.8, comparative col, "Purchase of PP&E" Rs535.51 lakh); FY26 65.00 (results FY26 audited, consol CF statement p.8, "Purchase of PP&E" Rs6,500.43 lakh — the FY26 spike reflects a new leased corporate premises fit-out, coincident with the Rs89.95cr Right-of-Use asset addition under Ind AS 116, results FY26 audited p.4).

FCF (CFO−Capex) by year: FY17 +4.12, FY18 −13.50, FY19 +3.67, FY20 +4.24, FY21 +6.25, FY22 −14.53, FY23 +12.83, FY24 +28.71, FY25 +60.68, FY26 −18.87.

**B2 FCF-positive years** = 7 of 10 (FY18, FY22, FY26 negative) = 70% → band 50-74% → **Score 2**
**B3 Cumulative FCF ÷ Cumulative PAT** = Rs73.60cr ÷ Rs283.57cr = **0.260** → band 0.20-0.39 → **Score 1**

**B4 Change in WC Days, latest vs earliest**: NOT COMPUTABLE on the full FY17→FY26 window — Trade Payables are not disaggregated in screener Data_Sheet for FY2017-FY2024 (see methodology note 5). Marked N/A (not in provided data) → **Score 0**.
For transparency, WC Days ARE computable for the two years where payables are available: FY25 = Receivable Days 125.8 + Inventory Days 16.8 − Payable Days 114.0 = **28.6 days** (results FY26 audited consol BS p.4 comparative, and screener-data revenue); FY26 = Receivable Days 154.3 + Inventory Days 4.1 − Payable Days 114.3 = **44.1 days** (results FY26 audited consol BS p.4). This 1-year move (+15.5 days) is directional information only, not the scored B4 metric.
Cross-check: Receivable Days computed here (125.8 FY25, 143.1 FY24) match Acuité's independently stated debtor days of 126 and 143 (Acuité PR 31-Dec-2025, p.2) — confirms formula basis (revenue-basis, consistent with Acuité).

**BLOCK B TOTAL = 1+2+1+0 = 4/20** — below the deal-breaker-2 threshold of 8 (see Deal-Breakers section).

**block_b_trend: "deteriorating"** — CFO fell from Rs66.04cr (FY25) to Rs46.13cr (FY26), a 30.1% YoY decline (screener-data FY25; results FY26 audited consol p.8 FY26), and FCF swung from +Rs60.68cr (FY25) to −Rs18.87cr (FY26) on the Rs65.00cr FY26 capex spike for the new leased premises.

---

## BLOCK C: GROWTH (Max 20)

Revenue (Rs Cr): FY17 158.29 → FY26 1424.28 (screener-data / results FY26 audited consol p.2, "Net Sales/Income from operations").
**C1 Revenue CAGR (9yr, FY17→FY26)** = (1424.28/158.29)^(1/9)−1 = **27.65%** → band ≥20% → **Score 5**

PAT (Rs Cr, consol attributable to owners): FY17 1.21 → FY26 84.74 (screener-data / results FY26 audited consol p.3).
**C2 PAT CAGR (9yr)** = (84.74/1.21)^(1/9)−1 = **60.34%** → band ≥20% (positive, not N/M) → **Score 5**

**C3 Positive YoY revenue years** = 9 of 9 transitions positive (FY17→FY26, no decline year) = 100% → **Score 5**

**C4 PAT CAGR − Revenue CAGR** = 60.34% − 27.65% = **+32.69pp** → band ≥+3pp → **Score 5**

**BLOCK C TOTAL = 5+5+5+5 = 20/20** — strongest block.

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY2026)

FY2026 consolidated (results FY26 audited, p.2-4): Sales 1424.28cr, EBITDA 145.92cr (methodology note 2), EBIT 131.39cr, Interest 23.20cr, Borrowings 236.54cr (screener-data; per audited BS p.4, this = financial debt Rs81.23cr [non-current 1.51cr + current 79.72cr] + lease liabilities Rs155.32cr [non-current 113.60cr + current 41.71cr] under Ind AS 116 — a large FY26 jump vs FY25's Rs138.84cr driven by the new office lease), Cash&Bank 111.51cr, Equity(NW) 315.08cr, Current Assets 777.87cr, Current Liabilities 577.52cr.

**D1 Net Debt ÷ EBITDA** = (236.54−111.51)/145.92 = 125.03/145.92 = **0.857x** → band 0-1.0x → **Score 4**
**D2 Interest Coverage (EBIT÷Interest)** = 131.39/23.20 = **5.66x** → band 5-9.9x → **Score 4**
**D3 Debt ÷ Equity** = 236.54/315.08 = **0.75x** → band 0.5-1.0x → **Score 3** (context: excluding lease liabilities, pure financial-debt/equity = 81.23/315.08 = 0.26x — the D3 score used here follows the "Borrowings" line as reported, consistent with Acuité's own gearing convention which also folds lease liabilities into debt — see cross-check below)
**D4 Current Ratio** = 777.87/577.52 = **1.35x** → band 1.2-1.49x → **Score 2**

Cross-check vs Acuité (FY25, most recent rated data, Acuité PR 31-Dec-2025 p.2/4): Gearing (D/E) 0.60x, ICR (PBDIT basis) 8.43x, TOL/TNW 2.35x, Debt/EBITDA 1.24x, GCA 155 days, debtor days 126, DSCR 4.58x. Independently computed FY25 screener-basis figures: D/E = 138.84/230.98 = 0.601x (matches Acuité's 0.60x almost exactly — validates the "Borrowings-includes-lease-liabilities" convention); EBITDA margin 8.31% (matches Acuité's 8.31% exactly). FY26 (latest, audited but post-dates the Dec-2025 rating) shows a marked leverage step-up from the new office lease, not yet reflected in any published rating action as of run date.

**BLOCK D TOTAL = 4+4+3+2 = 13/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

Block E was gap-filled mid-run with an operator-supplied screener.in quarterly Shareholding Pattern (screener SHP, Sep-2023 to Jun-2026), which supersedes the FY25-AR-only promoter-holding figures used for E1/E2 in an earlier draft of this block (both approaches agree closely; the SHP is current and preferred). E3 and E4 still rely on the FY25 Annual Report, as neither pledge data nor FY26 notes-to-accounts are available anywhere in provided data.

**E1 Promoter holding (latest quarter: Jun 2026)** = **60.89%** (screener SHP, Jun 2026) — consistent with the FY25 AR's Mar-2025 cut of 60.95% (AR FY25, Note 15.2, p.120) and the intervening quarters (60.95% held flat Mar-2025 through Dec-2025, screener SHP) → band ≥60% → **Score 5**

**E2 Promoter holding change**: screener SHP gives Sep-2023 (61.10%) → Jun-2026 (60.89%), a **−0.21pp** move over the ~2.75-year window available (Sep-2023 is the earliest quarter in the supplied table; no Jun-2023 data point exists to make this an exact 3-year window, but this is the closest available and materially represents the 3-year trend: essentially flat, no sell-down) (screener SHP, Sep 2023 and Jun 2026) → band ±1% → **Score 3**

**E3 Promoter pledge**: NOT FOUND (not in provided data) — confirmed by both the FY25 AR promoter shareholding table (Note 15.2/15.3, no encumbrance column) and the operator-supplied screener SHP (which explicitly carries no pledge column). No pledge amount can be confirmed or ruled out from provided data. → **Score 0** per grounded-claims rule (N/A scores 0; NOT estimated as 0% or >15%).

**E4 Contingent Liabilities ÷ Net Worth (latest available: FY2025, standalone — FY26 AR with notes-to-accounts not yet published as of run date)**: Contingent liabilities = GST claim (FY2018-19, under appeal) Rs9.64 lakh + Bank guarantees given by company's bankers Rs14,645.70 lakh = **Rs14,655.34 lakh (Rs146.55cr)** (AR FY25, standalone Note 32.7, p.135). Net Worth FY25 (standalone) = Rs23,091.97 lakh (Rs230.92cr) (AR FY25, standalone Note 32.7.A, p.135). Ratio = 146.55/230.92 = **63.47%** → band >30% → **Score 0**.
Data note: Rs14,645.70 lakh of the Rs14,655.34 lakh total (99.9%) is bank guarantees issued in the ordinary course of DSSL's government/enterprise systems-integration tendering business (consistent with Acuité's noted Rs2,700cr unexecuted order book, Acuité PR p.2), not litigation exposure — the GST dispute itself is immaterial (Rs9.64 lakh). This composition is noted per the "no qualitative override" rule; the mechanical score stands at 0.

Additional context (not scored, for stage-11 UA institutional-absence qualifier per Amendment 3): FII+DII combined ownership was 0.00% in Sep-2023, rising to ~1.36% by Jun-2026 (FII 1.08% + DII 0.28%) (screener SHP). Institutional ownership remains near-absent throughout. Shareholder count rose from 21,973 (Sep-2023) to 41,418 (Jun-2026) (screener SHP) — a broadening retail base, informational only.

**BLOCK E TOTAL = 5+3+0+0 = 8/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

**M1 Pricing Power** — EBITDA margin FY17 2.98% → FY26 10.24% (+7.26pp expansion; screener-data computed, cross-validated against Acuité FY24/FY25 exact matches) AND Revenue CAGR 27.65% ≥10% → **Score 5**

**M2 Cost Advantage vs peer median** — PEER DATA NEEDED, none provided → **Score 0**

**M3 Capital Efficiency** — FAT (Sales÷Net Block) FY26 = 1424.28/157.97 = **9.02x** (>3x) AND ROCE FY26 30.17% (>20%) → **Score 5**

**M4 Customer Stickiness** — Zero revenue-decline years (10/10) but Receivable Days far from stable (67.9d FY17 → 154.3d FY26, a +86.4-day secular rise; screener-data/results computed) — fails the "stable ±10 days" condition for the top tier. Scored at the "max 1 decline year, fully recovered" tier (0 actual decline years trivially satisfies "max 1") → **Score 3**, with the receivable-day deterioration flagged as a working-capital-quality caveat.

**M5 Scale & Dominance** — PEER DATA NEEDED (no mcap/margin peer ranking provided) → **Score 0**

**M6 Technology/R&D** — No R&D line disclosed anywhere in provided P&L; not applicable to the IT systems-integration/services model → **Score 0**

**M7 Regulatory/License** — Acuité explicitly characterises the industry as "highly competitive and fragmented" (Acuité PR 31-Dec-2025, p.1) — unregulated/fragmented, not a licensed oligopoly → **Score 0**

**M8 Distribution** — Reach is quantified (11 branch offices/warehouses, presence in 250+ locations across India, plus a Singapore subsidiary for APAC — Acuité PR p.1) but no time-series is provided to confirm network growth or revenue-per-outlet trend. Scored conservatively → **Score 1**

**M9 Brand** — Gross-margin proxy (Revenue−Material Cost)/Revenue computed for own trend (FY17 10.63% → FY26 18.40%, rising) but PEER DATA NEEDED for the required peer-median comparison → **Score 0** (GM proxy stated per M9's own proxy-basis instruction)

**M10 Switching Costs** — Revenue grew every year (10/10) but Receivable Days rose 86.4 days over the period, far outside any reasonable "stable" reading, and the "2+ decline years" condition for the partial-credit tier does not apply (0 decline years) — none of the defined tiers is literally satisfied → **Score 0**

**M11 Network Effects** (10yr history, ≥6yr test applies) — Latest 3yr revenue CAGR (FY23→FY26 base) = (1424.28/804.47)^(1/3)−1 = 20.98%; prior 3yr CAGR (FY20→FY23 base) = (804.47/328.85)^(1/3)−1 = 34.75%. Latest is LOWER than prior (decelerating, not accelerating) — fails top tier. Latest 3yr CAGR ≥20% AND Selling & Admin expense as % of revenue declining (FY23 1.35% → FY24 1.03% → FY25 0.86%; screener-data, FY26 not disclosed separately — folded into "Other Expenses") → **Score 3**

**M12 Negative WC/Float** — Only 2 of 10 years have full WC-Days data (payables gap, see B4): FY25 = 28.6 days, FY26 = 44.1 days, both in the 15-45-day band → **Score 1** (based on 2/10 years of available data; not a full 10-year read)

**BLOCK F TOTAL = 5+0+5+3+0+0+0+1+0+0+3+1 = 18/60**
**Moats present (score ≥3): M1, M3, M4, M11 = 4 moats**

Moat profile bar (0-5 each):
```
M1  Pricing Power        [#####] 5
M2  Cost Advantage       [     ] 0  (peer data needed)
M3  Capital Efficiency   [#####] 5
M4  Customer Stickiness  [###  ] 3
M5  Scale & Dominance    [     ] 0  (peer data needed)
M6  Technology/R&D       [     ] 0  (n/a)
M7  Regulatory/License   [     ] 0  (unregulated)
M8  Distribution         [#    ] 1
M9  Brand                [     ] 0  (peer data needed)
M10 Switching Costs      [     ] 0
M11 Network Effects      [###  ] 3
M12 Negative WC/Float    [#    ] 1  (2/10 years only)
```
**Moat classification: 4 present → STRONG**

---

## CLASSIFICATION

Data confidence: **10 years — "10+ yrs full"** (no confidence downgrade, no history_downgrade tier applies).

| Block | Score | Max |
|-------|-------|-----|
| A — Return on Capital | 15 | 20 |
| B — Cash Generation Quality | 4 | 20 |
| C — Growth | 20 | 20 |
| D — Balance Sheet Strength | 13 | 20 |
| E — Shareholder Alignment | 8 | 20 |
| **Core Score** | **60** | **100** |
| F — Moat Score | 18 | 60 |
| **Grand Total** | **78** | **160** |

Moat class: STRONG (4 moats confirmed: M1, M3, M4, M11)

Classification matrix lookup: Core 60-79 + STRONG/FORTRESS → **GOOD+**

### Deal-breaker check
1. Block A < 8? No (15). Not triggered.
2. **Block B < 8? YES (4/20). Deal-breaker triggered → caps classification at max GOOD.**
   Driving years: FY2018 and FY2022 CFO-negative (screener-data); FY2018, FY2022 AND FY2026 (latest year) FCF-negative — the FY2026 negative FCF (−Rs18.87cr) is driven by the Rs65.00cr capex for the new leased corporate premises (results FY26 audited, consol CF p.8), not an operating deterioration; cumulative CFO/PAT of 0.529x sits just above (i.e., 3% away from) the separate 0.50 AVERAGE-cap deal-breaker.
3. Median ROCE < 10%? No (20.38%). Not triggered.
4. Cumulative CFO/PAT < 0.50? No (0.529 — near miss, not triggered).
5. Pledge > 15%? UNKNOWN — not confirmable from provided data (E3 = NOT FOUND, confirmed by both FY25 AR and the operator-supplied screener SHP, neither of which carries a pledge column). Not triggered (absence of evidence is not evidence of a breach), but flagged as an open item.
6. ND/EBITDA > 3x AND IC < 3x? No (0.857x and 5.66x). Not triggered.
7. Revenue declined in majority of years? No (0/9 decline years). Not triggered.
8. PAT negative in any of last 3 years (FY24/25/26)? No (all positive, growing). Not triggered.
9. History < 3 years? No (10 years). Not triggered.

**Final classification: GOOD** (capped down from GOOD+ solely by deal-breaker 2, Block B < 8).

### Strongest / weakest block
- **Strongest: Block C (Growth) — 20/20**, a clean top-decile growth profile: 27.65% revenue CAGR, 60.34% PAT CAGR, zero revenue-decline years across 9 years of transitions.
- **Weakest: Block B (Cash Generation Quality) — 4/20**, the deal-breaker block: cumulative CFO/PAT of 0.529x, two CFO-negative years (FY18, FY22) plus a third FCF-negative year in FY26 driven by the new-office capex, and a WC-Days trend that cannot be scored on the full 10-year window because Trade Payables are not disaggregated pre-FY2025.

### Decision line
GATE 0 → **GOOD** (Core 60/100, moat STRONG, grand total 78/160; capped from GOOD+ by the Block B < 8 cash-quality deal-breaker). No STOP verdict issued — flags propagate downstream: (i) cash-conversion quality and the FY26 capex-driven FCF dip carry forward as a cash-quality watch item for stages 5-6; (ii) promoter pledge status is unresolved (NOT FOUND, not "0%") even after the shareholding-pattern gap-fill — the SHP confirms current holding level and a flat 3-year trend but carries no pledge column, so a direct pledge-disclosure check (exchange filing or AR footnote) is still needed before any position-sizing decision; (iii) five of twelve moat tests (M2, M5, M6, M9, plus partially M8) are peer-data-limited or disclosure-limited, not zero-moat findings — flagged for stage 7/11 to revisit if peer data becomes available.

---

## INPUT GAPS CARRIED FORWARD
- announcements/ folder empty.
- shareholding/ folder gap-filled mid-run by the operator with a screener.in quarterly Shareholding Pattern (screener SHP) — promoter holding level and 3-year trend are now current (Jun-2026), but promoter PLEDGE % remains NOT FOUND (no pledge/encumbrance column in either the SHP or the FY25 AR).
- Trade Payables not disaggregated in screener Data_Sheet for FY2017-FY2024 — limits B4 and M12 to the 2 years (FY25, FY26) where the full BS breakdown is available from the FY26 audited results filing.
- Peer/industry comparison data absent entirely — M2, M5, M9 scored 0 as "PEER DATA NEEDED", not as zero-moat findings.
- FY2026 Annual Report (with notes to accounts, contingent liabilities, promoter pledge) not yet published as of run date (2026-07-27) — E4 necessarily uses the FY2025 AR as the latest available source for contingent liabilities.

```yaml
stage: B01-gate0
company: "DSSL"
run_date: "2026-07-27"
model: claude-sonnet-5
status: complete
input_gaps: ["announcements/ empty", "shareholding/ gap-filled mid-run via operator-supplied screener SHP (promoter holding/trend now current to Jun-2026; pledge % still NOT FOUND, no pledge column in SHP or FY25 AR)", "Trade Payables not disaggregated pre-FY2025 in screener Data_Sheet (limits B4/M12 to FY25-FY26)", "peer/industry comparison data absent (M2, M5, M9 scored 0 as PEER DATA NEEDED)", "FY2026 Annual Report not yet published as of run date (E4 contingent-liabilities uses FY2025 AR)"]
flags:
  - {type: FLAG-CASH, reason: "Block B (cash generation) scored 4/20, triggering deal-breaker 2 (cap to max GOOD); cumulative CFO/PAT 0.529x (near the separate 0.50 AVERAGE-cap threshold); CFO fell Rs66.04cr (FY25) to Rs46.13cr (FY26), -30.1% YoY; FCF turned negative in FY26 (-Rs18.87cr) on Rs65.00cr capex for new leased premises (Ind AS 116 ROU addition)"}
  - {type: FLAG-DATA-GAP, reason: "Promoter pledge % (E3) not disclosed anywhere in provided data, including the operator-supplied screener SHP (Sep2023-Jun2026, no pledge column) and the FY25 AR promoter table; scored 0 as NOT FOUND, not confirmed 0% or >15%"}
  - {type: FLAG-STALE, reason: "E4 (contingent liabilities / net worth) sourced from FY25 Annual Report (31-Mar-2025), ~16 months stale vs run_date 2026-07-27, since the FY26 AR is not yet published; E1/E2 promoter-holding staleness has been resolved via the operator-supplied screener SHP (current to Jun-2026)"}
data_years: 10
fy_range: "FY2017 to FY2026"
blocks: {A: 15, B: 4, C: 20, D: 13, E: 8}
core_score: 60
moat_score: 18
grand_total: 78
moats_confirmed: 4
moat_class: "STRONG"
classification: "GOOD"
deal_breakers: ["Block B < 8 (scored 4/20) -> caps classification at max GOOD; driven by FY2018 and FY2022 CFO-negative years, FY2026 FCF-negative on new-office capex (Rs65.00cr), and cumulative CFO/PAT of 0.529x (screener-data FY17-25; results FY26 audited consol p.8)"]
history_downgrade: false
data_notes: ["EBITDA formula validated exactly against Acuité's independently stated FY24 (7.63%) and FY25 (8.31%) margins (Acuité PR 31-Dec-2025, p.2)", "screener 'Change in Inventory' sign is opposite to the raw P&L filing's 'Changes in Inventories' line; reconciled and used consistently", "ROCE Capital Employed basis: FY17-24 = Net Worth + Total Borrowings (proxy, screener does not split current/non-current liabilities pre-FY25); FY25-26 = Total Assets - Current Liabilities (precise, from audited BS breakdown)", "screener 'Borrowings' line bundles interest-bearing debt with Ind AS 116 lease liabilities from FY24 onward; validated against Acuité's FY25 gearing of 0.60x (exact match) and used consistently for D1/D3", "Capex = Purchase of PP&E line only; FY17-24 uses aggregate 'Cash from Investing Activity' as the only available proxy (granular PPE-only breakdown not provided for those years)", "Trade Payables not disaggregated pre-FY2025 in screener Data_Sheet; WC Days computable only for FY25 (28.6d) and FY26 (44.1d), a +15.5 day one-year move noted as directional color, not the scored B4 metric", "GM proxy used for M9 per its own instruction: (Revenue-Material Cost)/Revenue, own-trend only (10.63% FY17 to 18.40% FY26), no peer benchmark available", "Receivable Days computed here (125.8d FY25, 143.1d FY24) match Acuité's independently stated debtor days of 126 and 143 exactly, cross-validating the revenue basis used", "E4 contingent liabilities of Rs146.55cr is 99.9% bank guarantees issued in ordinary-course government/enterprise tendering (consistent with Acuité's stated Rs2,700cr order book), not litigation exposure; GST dispute itself is only Rs9.64 lakh -- noted for context, mechanical score of 0 unchanged", "Block E gap-filled mid-run: operator-supplied screener SHP (Sep2023-Jun2026) confirms promoter holding essentially flat (61.10% to 60.89%, -0.21pp) and resolves E1/E2 staleness; pledge % still NOT FOUND in any source; FII+DII rose 0.00% (2023) to ~1.36% (Jun2026), still near-absent institutional ownership (informational, feeds stage-11 UA qualifier, not scored here)"]
block_b_trend: "deteriorating - CFO fell from Rs66.04cr (FY25) to Rs46.13cr (FY26), -30.1% YoY, and FCF swung from +Rs60.68cr (FY25) to -Rs18.87cr (FY26) on the Rs65.00cr new-premises capex (screener-data FY25; results FY26 audited consol p.8)"
```
