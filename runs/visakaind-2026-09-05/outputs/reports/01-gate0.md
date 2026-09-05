# STAGE 1: GATE 0 SCORECARD — Visaka Industries Ltd (VISAKAIND)
Run date: 2026-09-05 | Model: claude-sonnet-5 | Mode: PIPELINE (no human in loop)

Data available: 10 years (FY2017 to FY2026) for P&L, cash-flow headline, and
balance-sheet aggregates (screener-Data_Sheet.csv). Full balance-sheet
granularity (current/non-current liability split, Trade Payables, Capex
break-out) is available only for **FY2024-FY2026**, from the two provided
Annual Reports (AR FY26 = year ended 31-Mar-2026 with FY25 comparative; AR
FY25 = year ended 31-Mar-2025 with FY24 comparative). No results filings, no
shareholding-pattern filing, no rating, no announcements are in this run's
corpus (carried from B00). Scoring below therefore runs on **two nested
windows, stated per metric**: the full 10-year screener window for
P&L-driven metrics (Blocks C, ROE, cumulative CFO/PAT), and a narrower
2-3-year AR-audited window for metrics that need balance-sheet granularity
the screener export does not carry (Block A ROCE for FY24-26, Block B
FCF/WC-days, moat test M12). Scoring adapted to 10-year history per the
confidence table (10+ years = full confidence band; **history_downgrade =
false** — the narrower per-metric windows are flagged individually below,
not treated as an overall short-history penalty).

## BASIS NOTE (declared up front)

screener-Data_Sheet.csv figures match **STANDALONE** audited financials
exactly at every checkpoint tested: FY26 Sales 1,675.59 Cr = standalone
Revenue from operations 1,67,558.66 lakh (AR FY26 p.156); FY26 Depreciation
64.97 Cr = standalone 6,496.94 lakh (AR FY26 p.156); FY26 Interest 32.96 Cr =
standalone Finance costs 3,296.41 lakh (AR FY26 p.156); FY26 CFO 182.64 Cr =
standalone Net cash inflow from operating activities 18,263.75 lakh (AR FY26
p.158); FY24 PBT 4.49 Cr = standalone 449.31 lakh (AR FY25 p.142,
comparative column); FY24 CFO 4.91 Cr = standalone 491.20 lakh (AR FY25
p.142). **Consolidated figures differ materially** — FY26 consolidated PAT
is Rs 85.36 Cr vs standalone/screener Rs 87.83 Cr, and FY25 consolidated PBT
is a **loss** of Rs 2.00 Cr vs standalone profit of Rs 1.32 Cr (AR FY26
p.224, consolidated P&L) — implying a loss-making subsidiary/JV drag not
visible in the screener series used for this scorecard. The AR's own Note 44
"Return on investment (ROI) of investee" is negative both years (-16.03%
FY26, -18.74% FY25, AR FY26 p.209) confirming subsidiary losses. All figures
below are standalone unless stated otherwise.

## FORMULA NOTES

- **EBIT** = PBT + Interest (screener convention, all years), per the
  standard used across this pipeline's prior Gate 0 runs. Not stripped of
  Other Income/exceptional items for the headline score (see the dedicated
  flag below for the ex-exceptional alternate, which changes D2's score
  band).
- **Capital Employed (ROCE) for FY2017-FY2023**: screener-Data_Sheet has no
  current/non-current liability split (only aggregate "Other Liabilities"),
  so CE is a **computed proxy: Equity Share Capital + Reserves + Borrowings**
  (closing-year), applied consistently, matching this pipeline's precedent
  (shyammetl-2026-07-19, northarc-2026-07-12 runs use the identical proxy).
- **Capital Employed (ROCE) for FY2024-FY2026**: the company's own audited
  standalone **Note 44/45 "Financial Ratios"** disclosure is used directly
  (source-provided, not recomputed) — FY26/FY25 at AR FY26 p.208-209, Note
  44; FY24 at AR FY25 p.190, Note 45. This basis is Schedule-III capital
  employed (average tangible net worth + total debt + deferred tax
  liability) and, per the AR's own stated variance reason, **includes the
  FY26 exceptional gain (Note 59) in the EBIT numerator** — flagged
  separately below.
- **Trade Payables**: NOT FOUND in screener-Data_Sheet for any year (no
  payables line in its Balance Sheet section). Only available FY2024-FY2026
  from the two provided ARs. WC Days (B4) and moat test M12 therefore use
  the FY2024-FY2026 window only, not the full 10-year span.
- **Capex** (Payments for PP&E): NOT FOUND in screener-Data_Sheet as a clean
  line (only aggregate Cash from Investing Activity, which for FY26 also
  bundles ~Rs 69.64 Cr of land/building sale proceeds — see the cash-quality
  flag below, this makes CFI unusable as a capex proxy). Capex known only
  for FY2024-FY2026 from the AR cash-flow statements (AR FY26 p.158; AR FY25
  p.142). B2/B3 (FCF metrics) therefore assessed on 3 of 10 years.
- **WC Days basis**: Revenue basis throughout (Inventory Days and Payable
  Days on Revenue, not COGS — no single clean COGS line in screener).
- **Receivable/Inventory data**: available all 10 years from
  screener-Data_Sheet (Balance Sheet section carries Receivables and
  Inventory every year).
- **Peer set**: 3 Data_Sheets provided by the orchestrator — BirlaNu Ltd
  (509675, formerly HIL), Everest Industries (EVERESTIND), Ramco Industries
  (RAMCOIND). "Segment"/"peer median" for M2/M5/M9 below is defined over
  this 4-company set (including Visaka), not the full BSE building-materials
  universe.

---

## KEY FINDING (load-bearing for every block below): the FY26 exceptional item

Standalone FY26 PBT of Rs 110.25 Cr (screener-data; AR FY26 p.156) splits as
**Profit before exceptional items and tax Rs 50.55 Cr + Exceptional items Rs
59.70 Cr** (AR FY26 p.156, lines V-VI). Note 59 (AR FY26 p.211): "The
Company has sold land in Ahmedabad, Gujarat, during the June 2025 quarter
and also land and building sold in Kanchipuram, Tamil Nadu, during the March
2026 quarter. The profits from sale of these assets, amounting to Rs
3,674.30 lakhs and Rs 2,296.03 lakhs respectively, have been presented as
exceptional items." Screener's FY26 "Other Income" row of Rs 66.81 Cr =
standalone Other Income Rs 7.10 Cr (AR FY26 p.156) + this Rs 59.70 Cr
exceptional gain (screener has no separate exceptional-items line and folds
it into Other Income) — this is company-memory verification item #1,
resolved: **the jump is a one-off land/building sale, not recurring other
income.** This single item is the primary driver of company-memory item #2
(the FY24 Rs 2.53 Cr / FY25 Rs 0.14 Cr / FY26 Rs 87.83 Cr PAT shape) and is
addressed again under company-memory item #3 (borrowings/CFI) below. It is
threaded through Blocks A and D and Block F below wherever it changes a
score band.

---

## BLOCK A: RETURN ON CAPITAL — Score: 4 / 20

| FY | EBIT (PBT+Int) | CE basis | ROCE | Source |
|---|---|---|---|---|
| FY17 | 88.82 | 605.69 (proxy) | 14.67% | computed, screener-data |
| FY18 | 119.89 | 686.79 (proxy) | 17.45% | computed, screener-data |
| FY19 | 120.30 | 745.89 (proxy) | 16.13% | computed, screener-data |
| FY20 | 74.52 | 767.87 (proxy) | 9.71% | computed, screener-data |
| FY21 | 162.07 | 742.40 (proxy) | 21.83% | computed, screener-data |
| FY22 | 172.33 | 899.49 (proxy) | 19.16% | computed, screener-data |
| FY23 | 96.79 | 1,161.12 (proxy) | 8.34% | computed, screener-data |
| FY24 | — | AR Schedule-III basis | **3.01%** | source: AR FY25 p.190, Note 45 |
| FY25 | — | AR Schedule-III basis | **3.46%** | source: AR FY26 p.208, Note 44 |
| FY26 | — | AR Schedule-III basis, incl. exceptional item | **11.87%** | source: AR FY26 p.209, Note 44 |

Proxy CE = Equity Share Capital + Reserves + Borrowings, closing-year
(screener-Data_Sheet.csv). Cross-check: applying the same proxy to FY26
gives EBIT 143.21 / CE 1,139.01 = 12.57% ROCE — close to the AR-reported
11.87%, validating the proxy for the years it is used (FY17-FY23).

- **A1 Median ROCE**: sorted [3.01, 3.46, 8.34, 9.71, 11.87, 14.67, 16.13,
  17.45, 19.16, 21.83] → median = (11.87+14.67)/2 = **13.27%**. Band
  10-14.9% = **1**
- **A2 Minimum single-year ROCE** = **3.01%** (FY24, AR-audited). <8% =
  **0**
- **A3 Median ROE**: see table below, median = **10.99%**. <12% = **0**
- **A4 ROCE trend, latest (FY26 11.87%) vs earliest (FY17 14.67%)**:
  decline = 2.80pp. Band decline 1-3pp = **3**

**Block A = 1+0+0+3 = 4/20.** Deal-breaker #1 triggered (Block A <8 → max
GOOD).

### ROE (10-year, fully computed and AR-validated)

| FY | Avg Net Worth (Cr) | PAT (Cr) | ROE |
|---|---|---|---|
| FY17 | 392.57 (closing only, no FY16) | 42.78 | 10.90% |
| FY18 | 419.12 | 66.56 | 15.88% |
| FY19 | 472.58 | 67.41 | 14.27% |
| FY20 | 502.26 | 49.30 | 9.82% |
| FY21 | 565.97 | 110.64 | 19.55% |
| FY22 | 679.62 | 118.53 | 17.44% |
| FY23 | 752.61 | 54.79 | 7.28% |
| FY24 | 764.29 | 2.53 | 0.33% |
| FY25 | 753.21 | 0.14 | 0.02% |
| FY26 | 793.16 | 87.83 | 11.07% |

(Net Worth = Equity Share Capital + Reserves, screener-Data_Sheet.csv;
PAT = Net profit row, same source.) FY24/FY25/FY26 independently
cross-checked to the exact AR-disclosed figures: 0.33% (AR FY25 p.190),
0.02% (AR FY26 p.208), 11.07% (AR FY26 p.208) — all match to two decimal
places, validating the formula and the screener data for the whole 10-year
series.

Median sorted [0.02, 0.33, 7.28, 9.82, 10.90, 11.07, 14.27, 15.88, 17.44,
19.55] = (10.90+11.07)/2 = **10.99%**.

---

## BLOCK B: CASH GENERATION QUALITY — Score: 17 / 20

CFO (screener-Data_Sheet.csv, Cash from Operating Activity, all 10 years):
152.72, 87.99, 70.91, 74.03, 294.01, 55.46, 30.10, 4.91, 119.11, 182.64.
Cumulative = **1,071.88 Cr**.
PAT (same source): 42.78, 66.56, 67.41, 49.30, 110.64, 118.53, 54.79, 2.53,
0.14, 87.83. Cumulative = **600.51 Cr**.

- **B1 Cumulative CFO ÷ Cumulative PAT** = 1,071.88 / 600.51 = **1.785**.
  ≥1.00 = **5**
- **B2 FCF-positive years as proportion** (assessable FY2024-FY2026 only —
  Capex not disclosed before FY24, see Formula Notes):

  | FY | CFO (Cr) | Capex (Cr) | FCF (Cr) |
  |---|---|---|---|
  | FY24 | 4.91 | 117.85 | **-112.94** |
  | FY25 | 119.11 | 28.31 | **+90.80** |
  | FY26 | 182.64 | 36.75 | **+145.89** |

  (CFO: screener-Data_Sheet.csv, matches AR exactly. Capex "Payments for
  property plant and equipment": FY26 3,674.76 lakh, AR FY26 p.158; FY25
  2,830.91 lakh and FY24 11,785.05 lakh, AR FY25 p.142 comparative column.)

  2 of 3 years positive = 66.7%. Band 50-74% = **2**
- **B3 Cumulative FCF ÷ Cumulative PAT** (same 3-year window, partial-period
  not full 10-year): Cumulative FCF = -112.94+90.80+145.89 = **123.75 Cr**.
  Cumulative PAT (FY24-26) = 2.53+0.14+87.83 = **90.50 Cr**. Ratio =
  **1.367**. ≥0.60 = **5**
- **B4 Change in WC Days, latest (FY26) vs earliest available with full
  Trade-Payables data (FY24)** — not the full FY17-FY26 span, flagged:

  | FY | Receivables | Inventory | Payables | Revenue | Rec. Days | Inv. Days | Pay. Days | WC Days |
  |---|---|---|---|---|---|---|---|---|
  | FY24 | 138.59 | 425.32 | 88.99 | 1,520.51 | 33.28 | 102.10 | 21.36 | **114.02** |
  | FY25 | 185.74 | 364.83 | 84.14 | 1,540.81 | 44.00 | 86.44 | 19.93 | **110.51** |
  | FY26 | 160.96 | 351.66 | 88.33 | 1,675.59 | 35.06 | 76.60 | 19.24 | **92.42** |

  (Receivables/Inventory/Revenue: screener-Data_Sheet.csv, all 10 years
  available but only FY24-26 shown here for the Payables-matched window.
  Payables: FY26 445.06+8,387.98 lakh = AR FY26 p.155; FY25 418.62+7,995.08
  lakh = AR FY26 p.155 comparative; FY24 400.51+8,498.67 lakh = AR FY25
  p.139 comparative.)

  Change = 92.42 - 114.02 = **-21.60 days** (decreased). Decreased >5 days =
  **5**

**Block B = 5+2+5+5 = 17/20.**

`block_b_trend`: **improving** — the one number: FCF swung from **-Rs
112.94 Cr (FY24)** to **+Rs 145.89 Cr (FY26)**. Caveat: FY24's collapse was
a capex-heavy year (Rs 117.85 Cr) and FY26's strength is boosted by the
one-off land-sale proceeds inside CFI, not by FCF itself, which is a clean
CFO-minus-capex measure and genuinely improved — but see the cash-quality
flag below on what funded the debt paydown.

---

## BLOCK C: GROWTH — Score: 8 / 20

Revenue (screener-Data_Sheet.csv): FY17 = 960.57 Cr → FY26 = 1,675.59 Cr (9
years). PAT: FY17 = 42.78 Cr → FY26 = 87.83 Cr.

- **C1 Revenue CAGR** = (1,675.59/960.57)^(1/9) - 1 = **6.38%**. Band
  5-9.9% = **1**
- **C2 PAT CAGR** = (87.83/42.78)^(1/9) - 1 = **8.32%**. Both endpoints
  positive (no N/M trigger — min PAT over the window is FY25's Rs 0.14 Cr,
  positive not zero/negative). Band 5-9.9% = **1**
- **C3 Positive YoY revenue years**: 9 YoY comparisons FY18-FY26. Declines
  in FY20 (1,050.38 vs FY19's 1,136.41) and FY24 (1,520.51 vs FY23's
  1,646.58); 7 of 9 up = 77.8%. Band 75-99% = **3**
- **C4 PAT CAGR - Revenue CAGR** = 8.32 - 6.38 = **+1.94pp**. Within ±3pp =
  **3**

No loss-to-profit swing (PAT positive every year, floor Rs 0.14 Cr FY25 —
see data_notes).

**Block C = 1+1+3+3 = 8/20.**

---

## BLOCK D: BALANCE SHEET STRENGTH — Score: 13 / 20 (latest = FY26)

- **D1 Net Debt ÷ EBITDA**: Borrowings 303.44 Cr - Cash & Bank 27.55 Cr
  (screener-Data_Sheet.csv; cross-checked to AR FY26 p.155: Cash and cash
  equivalents 2,418.98 lakh + Other bank balances 336.51 lakh = 27.55 Cr
  exactly) = Net Debt **275.89 Cr**. EBITDA = PBT+Interest+Depreciation =
  110.25+32.96+64.97 = **208.18 Cr**. Ratio = 275.89/208.18 = **1.325x**.
  Band 1-2x = **3**
- **D2 Interest Coverage (EBIT ÷ Interest)** = (110.25+32.96) / 32.96 =
  143.21/32.96 = **4.34x**. Band 3-4.9x = **2**. **Flagged**: ex-exceptional
  (EBIT = Rs 50.55 Cr pre-exceptional PBT + Rs 32.96 Cr Interest = Rs 83.51
  Cr) coverage = 83.51/32.96 = **2.53x**, which would score **1** (band
  1.5-2.9x), one band lower. Headline score used per this pipeline's
  standard EBIT=PBT+Interest convention (not stripped of exceptional items);
  the ex-exceptional number is the decision-relevant one.
- **D3 Debt ÷ Equity** = Borrowings 303.44 / (Equity Share Capital 17.32 +
  Reserves 818.25 = 835.57) = **0.363x**. Band 0.1-0.5 = **4**. Cross-check:
  AR FY26 p.208, Note 44 reports Debt Equity ratio 0.42x (broader "Total
  Debt" definition, includes lease liabilities) — same band, score
  unaffected.
- **D4 Current Ratio** = **1.60x** (AR FY26 p.208, Note 44, audited
  standalone; independently cross-checked: Current Assets 628.24 Cr /
  Current Liabilities 391.47 Cr = 1.605x, computed from AR FY26 p.155
  balance-sheet line items). Band 1.5-1.99 = **4**

**Block D = 3+2+4+4 = 13/20.**

---

## BLOCK E: SHAREHOLDER ALIGNMENT — Score: 14 / 20

- **E1 Promoter holding (latest available)**: **53.24%** as at 31-Mar-2026,
  "Promoters - Indian" category, 4,60,05,365 of 8,64,04,760 shares (AR FY26
  p.132, "Categories of Shareholders as on March 31, 2026"). Not a true
  "latest quarter" (Q1 FY27 shareholding pattern is ABSENT from this run's
  corpus, carried from B00) — this is the AR's year-end snapshot, 5 months
  stale vs the 5-Sep-2026 run date. Note: a narrower Companies-Act
  disclosure (Note 16(C), AR FY26 p.181) names only two individual
  promoters totalling 43.50% — the 53.24% SEBI-category figure is used here
  as the standard "promoter holding %" convention (see flag below on the
  gap between these two figures). ≥60% band fails; 50-59.9% = **4**
- **E2 Promoter holding change**: only a **1-year window** is available
  (31-Mar-2025 to 31-Mar-2026, not the full 3 years the formula wants — no
  earlier AR in the corpus). 48.42% (31-Mar-2025, AR FY25 p.117) → 53.24%
  (31-Mar-2026, AR FY26 p.132) = **+4.82pp**. Increased ≥1% = **5**.
  **Flagged**: this is a large one-year jump while the two named individual
  promoters' shareholdings were unchanged (Note 16(C) shows 0.00% change for
  both, AR FY26 p.181) — the increase is not explained in any provided
  document and appears linked to a matching decline in the "Private
  Corporate Bodies" category (10.33%→7.05% of shares) and Indian Public
  (38.31%→36.99%). Worth independent verification before relying on this
  score.
- **E3 Promoter pledge (latest)**: **NOT FOUND** in any provided document.
  Assets-pledged-as-security notes (AR FY26 p.180, 210, Notes 41/42) concern
  company borrowings collateral, not promoter share pledge; no SEBI (SAST)
  pledge disclosure is in this corpus (shareholding pattern ABSENT, carried
  from B00). Scored **0** on data-availability grounds, **not a confirmed
  pledge**.
- **E4 Contingent liabilities ÷ Net Worth**: Contingent liabilities FY26 =
  Rs 773.08 lakh = **Rs 7.73 Cr** (VAT/CST + Excise/Service tax + GST +
  Income tax; AR FY26 p.203, Note 38). Net Worth FY26 = 835.57 Cr. Ratio =
  0.925%. <5% = **5**

**Block E = 4+5+0+5 = 14/20.**

---

## BLOCK F: QUANTITATIVE MOAT SCORING — Score: 12 / 60

### Peer snapshot used for M2/M5/M9 (FY26, all screener-Data_Sheet.csv)

| Company | Mkt Cap (Cr) | Sales FY26 | PBT FY26 | Op. EBITDA (ex-Other-Income) | Op. EBITDA margin | GM proxy (Rev-RawMat)/Rev |
|---|---|---|---|---|---|---|
| VISAKAIND | 806.76 | 1,675.59 | 110.25 | 141.37 | **8.44%** | **49.24%** |
| BirlaNu (509675/HIL) | 1,091.92 | 2,426.53 | -12.64 | 60.85 | 2.51% | 40.96% |
| Everest Industries | 672.13 | 1,354.24 | -111.05 | -34.31 | -2.53% | 43.66% |
| Ramco Industries | 2,807.15 | 1,443.50 | 145.84 | 139.53 | 9.67% | 47.14% |

Op. EBITDA = PBT + Interest + Depreciation - Other Income (strips other
income/exceptional items from the margin comparison so FY26's one-off gain
doesn't distort it). Peer median margin (3 peers) = **2.51%**. Peer median
GM proxy = **43.66%**.

- **M1 Pricing Power**: Op. EBITDA margin FY17 12.20% → FY26 8.44% = decline
  of **3.76pp**; revenue still grew over the period (CAGR 6.38%, not
  ≥10%). "Margin declined 2-5pp despite growth" band = **1**
- **M2 Cost Advantage vs peer median**: 8.44% vs peer median 2.51% =
  **+5.93pp above**. ≥5pp above = **5**. **Flagged**: all 3 peers show
  unusually weak FY26 profitability (2 of 3 with negative PBT), an
  apparent sector-wide weak year (possibly tied to asbestos raw-material
  import/anti-dumping pressure common to this peer set). 3-year-average
  (FY24-26) alternate basis: VISAKAIND 6.92% vs peer-median 3.94% = +2.98pp
  → would move this to the 2-5pp band, **Score 3**, not 5. Both bases
  reported; FY26-only used as primary per the "(latest)" convention applied
  elsewhere in this framework.
- **M3 Capital Efficiency**: FAT (Revenue/Net Block) = 1,675.59/676.89 =
  **2.48x** (>2x); ROCE FY26 = 11.87% (AR-audited, Block A) — **not** >15%
  and **not** >12% (fails both the FAT>2x/ROCE>15% and FAT>1x/ROCE>12%
  bands by a small margin). **Score 0**
- **M4 Customer Stickiness**: 2 revenue-decline years (FY20, FY24, from
  Block C). "2 decline years, CAGR positive" = **1**
- **M5 Scale & Dominance**: among the 4-company peer set, VISAKAIND ranks
  3rd by market cap (Ramco 2,807 > BirlaNu 1,092 > **VISAKAIND 807** >
  Everest 672) — inside "top 3 mcap". Op. EBITDA margin rank among that
  top-3-mcap group: Ramco 9.67% (1st) > **VISAKAIND 8.44% (2nd)** > BirlaNu
  2.51% (3rd). "Top 3 mcap AND margin top 2" = **3**. **Flagged**: this
  ranking is over the 4-name peer set provided for this run, not the full
  listed building-materials universe (see input_gaps).
- **M6 Technology/R&D**: AR FY26 p.95, Note iii(a): "No specific
  expenditure exclusively on R&D has been incurred." R&D/Revenue not a
  quantified, material line. **Score 0**
- **M7 Regulatory/License**: no license/quota regime evidenced in provided
  documents (fibre-cement roofing, not a licensed/quota segment).
  **Score 0**
- **M8 Distribution**: reach is quantified but **declining, not growing**:
  dealers/distributors fell from 5,246 (FY25) to 4,974 (FY26), and sales
  through the dealer channel fell from 62.91% to 59.91% of total sales (AR
  FY26 p.106, BRR "Openness of business" disclosure). Neither "growing"
  band is met, and it is not "unquantified" either. **Score 0**
  (declining reach, flagged as a genuine finding, not a data gap)
- **M9 Brand**: GM proxy 49.24% vs peer median 43.66% = **+5.58pp above**.
  Revenue CAGR 6.38%, not ≥8%. "Above peers but growth below" = **1**
- **M10 Switching Costs**: overall revenue growth over the period with 2
  decline years (FY20, FY24). "Overall growth, 2+ decline years" = **1**
- **M11 Network Effects** (10 years available, ≥6 required): latest 3yr
  revenue CAGR (FY23→FY26) = (1,675.59/1,646.58)^(1/3)-1 = **0.58%**; prior
  3yr CAGR (FY20→FY23) = (1,646.58/1,050.38)^(1/3)-1 = **16.16%**. Latest is
  far LOWER than prior (decelerating, not accelerating) — fails top band.
  Latest 3yr CAGR (0.58%) is nowhere near ≥20% — fails middle band. Not
  >15% either — fails third band. **Score 0**
- **M12 Negative WC/Float**: WC Days (Block B4 table, FY24-26 only, full
  history not available) = 114.02, 110.51, 92.42 — all well above 45 days.
  **Score 0**

**Block F = 1+5+0+1+3+0+0+0+1+1+0+0 = 12/60.**

Moats "present" (score ≥3): **M2, M5** = **2 moats confirmed**.

**Moat classification: 2-3 present = MODERATE**

---

## CLASSIFICATION AND OVERRIDES

**Core score** (A+B+C+D+E) = 4+17+8+13+14 = **56/100**
**Moat score** (Block F) = **12/60**
**Grand total** = 56+12 = **68/160**

### Deal-breaker check

1. Block A <8 → Block A = 4 → **TRIGGERED** → max GOOD. Driven by FY23-FY25
   (ROCE 8.34%, 3.01%, 3.46%; ROE 7.28%, 0.33%, 0.02%) — a genuine
   multi-year operating trough (raw-material cost pressure, peak borrowings
   ~Rs 535 Cr at FY24, rising interest cost), not a post-listing rebase or
   one-time accounting artifact. FY26's partial recovery (ROCE 11.87%) is
   itself substantially the one-off land-sale gain (see Key Finding above).
2. Block B <8 → Block B = 17 → not triggered
3. Median ROCE <10% → 13.27% → not triggered
4. Cumulative CFO/PAT <0.50 → 1.785 → not triggered
5. Pledge >15% → status unknown (NOT FOUND), not a confirmed breach → not
   triggered, flagged as a gap (E3)
6. ND/EBITDA >3x AND IC <3x → ND/EBITDA = 1.325x (not >3x) → not triggered
7. Revenue declined majority of years → 2 of 9 years (22%) → not triggered
8. PAT negative in any of last 3 years → FY24/25/26 all positive (min Rs
   0.14 Cr, FY25) → not triggered
9. History <3 years → 10-year primary window → not triggered

**deal_breakers: [1]**

### Data confidence / history downgrade

Primary data window = 10 years (FY2017-FY2026) → **10+ years = full
confidence band**, no automatic downgrade. **history_downgrade = false**.
Caveat (not a formal downgrade trigger, but load-bearing): several
individual metrics — Block A ROCE FY24-26, Block B FCF/WC-days, moat test
M12 — rely on a narrower 2-3-year AR-audited window because
screener-Data_Sheet lacks current-liability, Trade-Payables and Capex
granularity for FY17-FY23. Each instance is flagged at the metric.

### Classification matrix

Core = 56 → falls in the **Core 40-59 = AVERAGE** band directly (this band
is not further split by moat class in the matrix). Deal-breaker #1's "max
GOOD" cap does not change this outcome, since AVERAGE already sits below
GOOD on the classification ladder.

**Classification = AVERAGE**

---

## STRONGEST / WEAKEST BLOCK

**Strongest**: Block B (17/20) — cumulative cash conversion is strong
(CFO/PAT 1.785x over 10 years) and, in the 3-year window where full data
exists, FCF swung decisively positive and WC Days improved by 21.6 days.

**Weakest**: Block A (4/20) — the deal-breaker block. Median ROCE (13.27%)
and median ROE (10.99%) are both dragged down by a genuine 3-year trough
(FY23-FY25) that FY26 only partially and partly optically reverses (Key
Finding above). Block F (moat, 12/60) is comparably weak: only 2 of 12
tests clear the "present" bar (M2 cost advantage, itself sensitive to an
apparently unusual weak year across the whole peer set, and M5 scale, on a
narrow 4-name peer set), and three tests fail on genuine findings rather
than data gaps — declining dealer network (M8), decelerating growth (M11),
and WC Days consistently above 45 (M12).

---

## DECISION LINE

AVERAGE on a 10-year audited window, driven by a real earnings trough
(FY23-FY25 ROCE 3-8%, ROE near zero) that the FY26 numbers do not cleanly
resolve: roughly half of FY26's PBT recovery is a one-off land and building
sale (Rs 59.70 Cr pre-tax, Note 59), not an operating turnaround. Ex-
exceptional, FY26 interest coverage falls one full score band (4.34x to
2.53x) and ROCE would sit closer to 7% than the reported 11.87%. Cash
generation (Block B) and balance-sheet leverage (Block D) are the
comparative strengths, but even the debt paydown (borrowings Rs 534.98 Cr
FY24 to Rs 303.44 Cr FY26) leaned on the same asset-sale proceeds, not
solely on organic FCF. Moat scoring is thin (2 of 12 tests present,
MODERATE), with two genuine adverse findings (shrinking dealer network,
decelerating revenue) rather than data gaps. Four items are decision-
relevant beyond the numeric score and should carry into the Halt-1 dossier:
the exceptional-item earnings quality issue, the unexplained one-year
promoter-holding jump, ATUM solar-roofing's undisclosed real contribution,
and the consolidated-vs-standalone gap suggesting a loss-making subsidiary.

---

```yaml
stage: B01-gate0
company: "VISAKAIND"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
input_gaps:
  - "Screener Data_Sheet lacks a Ratios section (no source-provided ROCE/ROE) and lacks current/non-current liability split in the Balance Sheet section; FY2017-FY2023 ROCE computed via proxy (Equity+Reserves+Borrowings, closing-year), not the strict Total Assets-Current Liabilities formula. FY2024-FY2026 use the AR's own audited Note 44/45 ROCE instead."
  - "Trade Payables not disclosed in screener Balance Sheet section for any year; only available FY2024-FY2026 via the two provided Annual Reports. Block B4 (WC Days) and moat test M12 use FY2024-FY2026 only (3 of 10 years), not the full history."
  - "Capex (Payments for PP&E) not separately disclosed in screener Cash Flow section (only aggregate Cash from Investing Activity, which for FY26 also bundles ~Rs 69.64cr of land/building-sale proceeds). Capex known only for FY2024-FY2026 from AR cash-flow statements. Block B2/B3 (FCF metrics) assessed on 3 of 10 years only."
  - "Promoter shareholding pattern (SEBI quarterly filing) ABSENT from provided inputs (carried from B00); the two ARs give only two annual snapshots (31-Mar-2025 and 31-Mar-2026), so E2 (intended 3-year change) is computed over a 1-year window only."
  - "Promoter pledge %: NOT FOUND in any provided document. E3 scored 0 on data-availability grounds, not a confirmed pledge."
  - "ATUM solar-roofing revenue/profit contribution: NOT FOUND as a separately disclosed figure. AR's segment note (Note 37/36) reports only two segments (Building product; Synthetic yarn); ATUM is bundled inside Building product with no standalone break-out despite heavy MD&A narrative emphasis."
  - "Peer set limited to 3 names provided for this run (BirlaNu/HIL, Everest Industries, Ramco Industries); M2/M5/M9 'segment'/'peer median' are defined over this 4-company set (including Visaka), not the full listed building-materials universe."
  - "Results filings, credit rating, announcements, shareholding pattern, and current concalls/presentation all ABSENT/stale in this run's corpus (carried from B00)."
flags:
  - {type: FLAG-GATE0, reason: "Classification AVERAGE (Core 56/100) with historical depressors identified: Block A deal-breaker triggered by a genuine 3-year ROCE/ROE trough (FY23 8.34%/7.28%, FY24 3.01%/0.33%, FY25 3.46%/0.02%), not a post-listing rebase. FY26's partial recovery is substantially a one-off asset sale, not an operating turnaround (see FLAG-ACCOUNTING)."}
  - {type: FLAG-ACCOUNTING, reason: "FY26 standalone PBT of Rs110.25cr includes a one-off exceptional gain of Rs59.70cr (pre-tax) from sale of land in Ahmedabad (Jun-2025 qtr, Rs36.74cr) and land+building in Kanchipuram (Mar-2026 qtr, Rs22.96cr) (AR FY26 p.211, Note 59; p.156 P&L lines V-VI). Ex-exceptional standalone PBT is only Rs50.55cr. Interest coverage falls from a headline 4.34x to 2.53x ex-exceptional (one score band lower, D2). ROCE (AR-audited, includes the exceptional item per the AR's own variance note) would be materially lower ex-exceptional, roughly 6-7% vs the reported 11.87%."}
  - {type: FLAG-CASH, reason: "FY26 investing cash flow turned positive (+Rs36.21cr, screener-data) not from operating asset growth but from ~Rs69.64cr of land/building sale proceeds (AR FY26 p.158: Proceeds from sale of PP&E Rs3,055.46 lakh + Proceeds from sale of assets held for sale Rs3,908.77 lakh), partly offset by Rs36.75cr of ongoing capex. The FY24-to-FY26 borrowings reduction (Rs534.98cr to Rs303.44cr, screener-data) is partly funded by this one-off asset monetisation, not solely by organic FCF (FY24 FCF was -Rs112.94cr)."}
  - {type: FLAG-DATA-GAP, reason: "Promoter pledge unconfirmed (E3); E2's intended 3-year window is only 1 year (see input_gaps); ATUM solar-roofing's real revenue/profit contribution is not separately disclosed despite prominent MD&A narrative (see input_gaps)."}
  - {type: FLAG-GOVERNANCE, reason: "Promoter holding (SEBI 'Promoters - Indian' category) jumped +4.82pp in the only available 1-year window (48.42% at 31-Mar-2025, AR FY25 p.117, to 53.24% at 31-Mar-2026, AR FY26 p.132) while the two named individual promoters' holdings were unchanged (0.00% change each, Note 16(C), AR FY26 p.181). The increase is not explained in any provided document and appears linked to a matching decline in the 'Private Corporate Bodies' category (10.33% to 7.05%) and Indian Public (38.31% to 36.99%). Worth independent verification before crediting E1/E2 as an alignment strength."}
data_years: 10
fy_range: "FY2017 to FY2026"
blocks: {A: 4, B: 17, C: 8, D: 13, E: 14}
core_score: 56
moat_score: 12
grand_total: 68
moats_confirmed: 2
moat_class: "MODERATE"
classification: "AVERAGE"
deal_breakers: [1]
history_downgrade: false
data_notes:
  - "No technical loss-to-profit PAT swing: PAT positive (though near-zero) every year FY2017-FY2026, floor FY25 Rs0.14cr (screener-data). CAGR edge rule not triggered on the full-period calc, but the FY24-FY25 near-zero trough is qualitatively a near-loss condition (see FLAG-ACCOUNTING and FLAG-GATE0)."
  - "ROCE basis blend: FY2017-FY2023 computed as proxy EBIT(PBT+Interest)/CE(Equity+Reserves+Borrowings, closing-year, screener-data); FY2024-FY2026 use the company's own audited standalone Note 44/45 ROCE (Schedule-III average capital-employed basis, includes exceptional items in the FY26 EBIT numerator per the AR's own stated variance reason). Cross-check: applying the proxy formula to FY26 gives ~12.57% vs the AR-reported 11.87%, validating the proxy basis used for FY17-FY23."
  - "ROE fully computed FY2017-FY2026 from screener PAT and Net Worth (opening+closing average; FY17 uses closing-only, no FY16 data available). Cross-validated exactly against AR Note44/45 for FY24 (0.33%), FY25 (0.02%), FY26 (11.07%) -- all match to two decimal places."
  - "M9 gross-margin proxy used: (Revenue - Raw Material Cost) / Revenue, applied consistently to VISAKAIND and all 3 peers (screener-Data_Sheet.csv 'Raw Material Cost' row)."
  - "M2/M9 peer comparison uses FY26 only; all 3 provided peers show unusually weak FY26 profitability (BirlaNu PBT -Rs12.64cr, Everest PBT -Rs111.05cr), an apparent sector-wide weak year. 3-year-average (FY24-26) alternate basis: VISAKAIND op-EBITDA margin 6.92% vs peer-median 3.94% (+2.98pp) would move M2 to the 2-5pp-above band (Score 3, vs Score 5 on the FY26-only basis used as primary)."
  - "M6/M7/M8 scored 0 on substantive grounds, not data absence: no R&D spend disclosed (AR FY26 p.95, explicit statement); no license/quota regime evidenced; dealer network is quantified but declining, not growing (5,246 to 4,974 dealers YoY, dealer-channel sales mix 62.91% to 59.91%, AR FY26 p.106)."
  - "Basis note: screener-Data_Sheet.csv figures match STANDALONE audited financials exactly at every checkpoint tested for FY24-FY26; consolidated figures differ materially (FY26 consolidated PAT Rs85.36cr vs standalone/screener Rs87.83cr; FY25 consolidated PBT is a LOSS of Rs2.00cr vs standalone profit of Rs1.32cr, AR FY26 p.224), implying a loss-making subsidiary/JV drag not visible in the screener series used for this scorecard. AR's own Note44 'Return on investment (ROI) of investee' is negative both years (-16.03% FY26, -18.74% FY25, AR FY26 p.209)."
  - "Screener FY26 'Other Income' row (Rs66.81cr) = standalone Other Income (Rs7.10cr, AR FY26 p.156) + Exceptional items (Rs59.70cr, land/building sale gain, Note 59) folded together; screener has no separate exceptional-items line. This resolves company-memory verification item #1."
block_b_trend: "improving -- FCF swung from -Rs112.94cr (FY24, capex-heavy year) to +Rs145.89cr (FY26); WC Days improved 21.6 days over the same 3-year window (114.02 to 92.42 days). Caveat: FY26 debt paydown was partly funded by one-off asset-sale proceeds inside CFI, not solely by this FCF improvement (see FLAG-CASH)."
analyst_note: "Classification is AVERAGE (Core 56, moat MODERATE) on a genuine finding, not a data artifact: standalone ROCE and ROE both troughed near zero in FY24-FY25 (ROCE 3.0-3.5%, ROE 0.3-0.02%, AR-audited) before a sharp FY26 recovery. That recovery is materially optical: Rs59.70cr of the Rs110.25cr FY26 PBT is a one-off gain from selling land in Ahmedabad and land-plus-building in Kanchipuram (Note 59), not operating improvement. Strip it out and FY26 ROCE falls to roughly 6-7% and interest coverage to 2.53x, both still weak. The same asset sale, not organic cash generation alone, funded most of the FY26 debt paydown (borrowings Rs535cr to Rs303cr) and the positive investing cash flow. Block B (cash quality) scores well on cumulative history, but that history is dominated by FY21's exceptional Rs294cr CFO year, not a broad, even trend. Two items need independent verification before Halt 1: a one-year promoter-holding jump (+4.82pp) with no named-individual change, and ATUM solar-roofing's real revenue contribution, which the company does not break out from the Building Products segment despite heavy narrative emphasis. A third: consolidated PAT/PBT run below standalone in both FY25 and FY26, pointing to a loss-making subsidiary that the standalone-only screener series does not show."
```
