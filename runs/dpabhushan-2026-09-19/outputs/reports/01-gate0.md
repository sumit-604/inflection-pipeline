# STAGE 1 — GATE 0 SCORECARD: D. P. Abhushan Ltd (DPABHUSHAN)
Run date: 2026-09-19 | Model: claude-sonnet-5 | RUN 2 (corrected text extraction; supersedes RUN 1 output)

Data available: P&L, cash flow and balance-sheet totals: 10 years (FY2017
to FY2026, screener-Data_Sheet.csv). Balance-sheet GRANULARITY needed by
the fixed formulas (Current Liabilities split, Trade Payables, precise
capex) is available only 3 years (FY2024 to FY2026), from the FY26 AR
(FY26 audited + FY25 comparative, standalone) and the FY25 AR (FY25
audited + FY24 comparative, standalone); the screener Data_Sheet has no
Current Liabilities or Trade Payables line, so ROCE, D/E-style leverage
and Working-Capital-Days cannot be computed per formula outside this
3-year window. Scoring is adapted per block: Blocks A, D and the WC-based
moat tests (M4, M10, M11, M12) use the FY24-FY26 AR-detail window; Block C
(growth) uses the full FY17-FY26 P&L window; Block B1 uses the full
10-year CFO/PAT series (screener), B2-B4 use the FY24-FY26 AR-detail
window (capex only available there). Data confidence held at "10+ yrs
full" for the overall review (the company has traded through a full cycle
including the FY20 COVID dip); the narrower 3-year BS-detail window is
flagged per-metric below, not applied as a blanket history downgrade.

Cross-checks: AR-sourced CFO (FY24 -0.28 Cr, FY25 -18.93 Cr, FY26 -97.31
Cr; AR FY26 p.84/PDF p.84, "Net Cash Flow from/(used in) Operating
Activities", and AR FY25 p.176/PDF p.180) match screener-Data_Sheet.csv
CFO exactly for all three years. AR-sourced PBT, PAT, Equity Capital and
Reserves also match screener for FY24-FY26. This corroborates the
screener Data_Sheet as reliable for the P&L/BS totals it does carry.

One material discrepancy found and flagged, not used: screener-Data_Sheet
"Interest" row shows FY25 = Rs 17.14 Cr and FY24 = Rs 14.12 Cr; the AR's
own "Finance Cost" line (Note 27, both ARs) shows FY25 = Rs 14.44 Cr and
FY24 = Rs 11.62 Cr for the same years (FY26's screener/AR interest figures
match exactly at Rs 16.22 Cr). All EBIT/EBITDA/interest calculations below
use the AR Finance Cost figures throughout, for internal consistency with
the AR PBT figures; the screener anomaly is not used anywhere in this
scorecard's arithmetic.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Formula: ROCE = EBIT / (Total Assets - Current Liabilities); EBIT = PBT +
Finance Cost (AR). ROE = PAT / average Net Worth. Computed for FY24-FY26,
the only years with a filed Current Liabilities split.

| FY | PBT (Cr) | Finance Cost (Cr) | EBIT (Cr) | Total Assets (Cr) | Current Liab. (Cr) | Capital Employed (Cr) | ROCE |
|---|---|---|---|---|---|---|---|
| FY24 | 83.39 | 11.62 | 95.00 | 537.37 | 283.09 | 254.28 | 37.36% |
| FY25 | 150.98 | 14.44 | 165.42 | 837.30 | 412.07 | 425.23 | 38.91% |
| FY26 | 282.70 | 16.22 | 298.92 | 1,142.62 | 490.79 | 651.83 | 45.86% |

(AR FY26 pp.83, PDF p.83, Standalone Balance Sheet & P&L, both halves;
AR FY25 pp.173-175, PDF pp.177,179, Standalone Balance Sheet & P&L, for
FY24 comparative)

Net Worth (screener-Data_Sheet, Equity Share Capital + Reserves, Cr):
FY23 = 181.07, FY24 = 238.75, FY25 = 404.13, FY26 = 632.61 (all cross-check
exactly against the AR Total Equity lines for FY24-FY26).

| FY | PAT (Cr) | Avg Net Worth (Cr) | ROE |
|---|---|---|---|
| FY24 | 61.86 | 209.91 | 29.47% |
| FY25 | 112.70 | 321.44 | 35.07% |
| FY26 | 211.84 | 518.37 | 40.86% |

**A1 Median ROCE** = 38.91% (FY25) -> **5/5** (>=25%)
**A2 Minimum single-year ROCE** = 37.36% (FY24) -> **5/5** (>=15%)
**A3 Median ROE** = 35.07% (FY25) -> **5/5** (>=20%)
**A4 ROCE trend, latest vs earliest** = 45.86% (FY26) vs 37.36% (FY24),
latest >= earliest -> **5/5**

**BLOCK A TOTAL: 20/20**

Flag: these are very high, and this is the same window LBF1 names for a
gold-price / inventory-holding-gain effect on margin (FY26 GM 10% vs
FY25 7.72%, EBITDA margin rising sharply into FY26). Stage 11 / the
operator, not this mechanical scorecard, must separate structural margin
gain from gold-price tailwind before trusting the ROCE trend as durable.

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

**B1 Cumulative CFO / Cumulative PAT** (full 10-year screener series,
FY17-FY26, Cr):

CFO by year: 8.46, -9.45, 37.22, 7.27, -29.29, 16.75, 60.97, -0.28,
-18.93, -97.31 (screener-Data_Sheet.csv, Cash Flow block; FY24-FY26
cross-checked against AR cash flow statements, exact match).
Cumulative CFO = **-24.59 Cr**.
PAT by year: 4.90, 8.15, 11.79, 16.68, 27.46, 40.44, 45.32, 61.86, 112.70,
211.84 (screener-Data_Sheet.csv, P&L block; FY24-FY26 cross-checked
against AR, exact match).
Cumulative PAT = **541.14 Cr**.
Ratio = -24.59 / 541.14 = **-4.5%** -> **0/5** (<0.50)

**B2/B3 FCF**: capex is only anchored for FY24-FY26 (AR cash flow
statements give the PPE/CWIP/intangible addition lines; screener's
"Cash from Investing Activity" lumps capex with investments and advances
and cannot be used per the formula's capex definition). Scored on this
3-year window.

Capex = Addition to PPE + Addition to CWIP + Intangible Assets Addition
(excludes Capital Advances and the FY26 liquid-fund investment, per the
formula's "exclude acquisitions" instruction):
- FY24: 279.14 + 49.46 + 38.44 = 367.04 Lakh = 3.67 Cr (AR FY25 p.176,
  PDF p.180)
- FY25: 1,467.95 + 1,050.70 + 10.36 = 2,529.01 Lakh = 25.29 Cr (AR FY25
  p.176, PDF p.180, FY25 own-year column)
- FY26: 614.79 + 45.87 + 57.69 = 718.35 Lakh = 7.18 Cr (AR FY26 p.84,
  PDF p.84)

FCF = CFO - Capex:
- FY24: -0.28 - 3.67 = **-3.95 Cr**
- FY25: -18.93 - 25.29 = **-44.22 Cr**
- FY26: -97.31 - 7.18 = **-104.49 Cr**

**B2 FCF-positive years as proportion** = 0/3 = 0% -> **0/5** (<50%)

**B3 Cumulative FCF / Cumulative PAT** (same 3-year window for
consistency): Cumulative FCF = -152.66 Cr; Cumulative PAT (FY24-26) =
386.40 Cr. Ratio = -152.66 / 386.40 = **-39.5%** -> **0/5** (negative)

**B4 Change in WC Days, latest (FY26) vs earliest available with a filed
Trade Payables line (FY24)** — see Working Capital Days table under Block
D/moat notes below. WC days: FY24 = 59.72, FY26 = 80.08, an increase of
**20.4 days** -> **0/5** (increased >15)

**BLOCK B TOTAL: 0/20**

block_b_trend: **deteriorating**. CFO went from -Rs 18.93 Cr (FY25) to
-Rs 97.31 Cr (FY26) (screener; AR FY26 p.84 confirms -Rs 9,730.52 Lakh),
while Inventory rose from Rs 722.10 Cr to Rs 1,003.94 Cr (+39%,
screener-Data_Sheet.csv Balance Sheet block; AR FY26 Note 7). This is the
LBF2 pattern the mental model must classify GROWTH-INDUCED (new-store
stock build for the ~6-store-a-year plan) vs STRUCTURAL before Halt 1.

---

## BLOCK C: GROWTH (Max 20)

Full available window, FY17 to FY26 (screener-Data_Sheet.csv, P&L block,
Sales and Net Profit rows), 9-year CAGR:

**C1 Revenue CAGR** = (4,065.13 / 451.02)^(1/9) - 1 = **27.67%** ->
**5/5** (>=20%)
Cross-check, latest 3-year window (FY23-FY26): (4,065.13/1,971.11)^(1/3)-1
= 27.29%. Consistent; no material deceleration on the full-period read.

**C2 PAT CAGR** = (211.84 / 4.90)^(1/9) - 1 = **51.99%** -> **5/5**
(>=20%; both endpoints positive, no loss-to-profit swing)

**C3 Positive YoY revenue years** = 8 of 9 year-on-year transitions
positive (FY17-18 through FY25-26); the one decline is FY19->FY20 (807.17
Cr vs 811.88 Cr, screener-Data_Sheet.csv). 8/9 = 88.9% -> **3/5** (75-99%)

**C4 PAT CAGR minus Revenue CAGR** = 51.99% - 27.67% = **+24.3pp** ->
**5/5** (>=+3pp)

**BLOCK C TOTAL: 18/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

Latest = FY26, AR-anchored (AR FY26 p.83, PDF p.83, Standalone Balance
Sheet; AR FY26 p.161, PDF p.83 right half, Standalone P&L; AR FY26 Note
27, p. ~166, "Finance Cost" break-up).

Total Borrowings FY26 = Non-Current Borrowings 336.90 Lakh + Current
Borrowings 28,401.25 Lakh = 28,738.15 Lakh = **287.38 Cr** (AR FY26 p.83).
[Cross-check: screener-Data_Sheet.csv Borrowings FY26 = 290.04 Cr, a ~2.7
Cr gap versus the AR sum; used the AR figure as primary, more granular
anchor. The gap does not change any band below.]
Cash & Bank FY26 = 25.75 Cr (AR FY26 p.83/PDF p.84 "Cash and Cash
Equivalents", matches screener exactly).
Net Debt FY26 = 287.38 - 25.75 = **261.63 Cr**.
EBITDA FY26 = EBIT (298.92 Cr, Block A) + Depreciation (10.76 Cr, AR Note
28 / screener) = **309.67 Cr**.

**D1 Net Debt / EBITDA** = 261.63 / 309.67 = **0.85x** -> **4/5** (0-1.0x)

**D2 Interest Coverage** = EBIT / Finance Cost = 298.92 / 16.22 =
**18.43x** -> **5/5** (>=10x)

**D3 Debt / Equity** = Total Borrowings / Total Equity = 287.38 / 632.61
= **0.454** -> **4/5** (0.1-0.5)

**D4 Current Ratio** = Total Current Assets / Total Current Liabilities =
1,05,124.21 / 49,078.82 (Lakh, AR FY26 p.83) = **2.14x** -> **5/5**
(>=2.0)

**BLOCK D TOTAL: 18/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

**E1 Promoter holding (latest filed)** = Promoters 41.52% + Promoters
Relative 32.07% = **73.59%** as at 31-Mar-2026 (AR FY26 p.81, PDF p.43,
"On the Category of Shareholders"; total shares 22,827,920 reconciles to
the 2,282.79 Lakh equity share capital on the FY26 balance sheet). ->
**5/5** (>=60%)
[Context, not anchored as a filing: screener-shareholding-pattern text
shows Promoters 74.89% at Mar-2026, ~1.3pp above the AR category-table
figure; the two AR tables in this corpus disaggregate "Promoters" and
"Promoters Relative" as separate rows and the sum is used here as the
filed, anchored figure.]

**E2 Promoter holding change**: only a 1-year filed comparison is
available in this corpus (2 ARs held, not 4). AR FY25 p.67 (PDF p.67),
"On the Category of Shareholders": Promoters 41.9140% + Promoters
Relative 31.9037% = **73.82%** as at 31-Mar-2025. Change 31-Mar-2025 to
31-Mar-2026 = 73.82% -> 73.59% = **-0.23pp**. Scored on this 1-year
window (data limitation: the corpus holds only FY26 and FY25 ARs, not a
filed Mar-2023 shareholding pattern) -> **3/5** (+-1%)
[Context, not anchored: screener-shareholding-pattern text shows a
3-year, non-filing trend of Promoters 75.00% (Mar-2023) -> 74.89%
(Mar-2026), -0.11pp, directionally consistent with the anchored 1-year
read.]

**E3 Promoter pledge**: searched both ARs (Annual_Report_2026.txt,
Annual_Report_2025.txt) for "pledge"/"encumbrance" in the shareholding
context; every hit is boilerplate insider-trading-code language or a
vehicle-loan security note (AR FY26 p. ~79, "Vehicles are pledged as
Security against Vehicle Loans" — not a promoter-shareholding pledge).
No SEBI-format "shares pledged or otherwise encumbered" table or
statement was found in either AR. The CARE rating rationale
(CARE-PR-2026-01-08-DPAbhushan.txt) makes no pledge reference either. The
three unreadable SAST scans (image-only, named in B00 input_gaps) concern
a Reg 29(2) acquisition, not pledge. -> **N/A (not in provided data)**,
score **0/5**

**E4 Contingent Liabilities / Net Worth**: Contingent Liabilities FY26 =
disputed income-tax demand Rs 12.57 Lakh (AR FY26 Note 33.10, p. ~166;
"Contingent Liabilities" line itself shows Nil, only the disputed-demand
claim line is populated). Net Worth FY26 = 632.61 Cr = 63,261 Lakh. Ratio
= 12.57 / 63,261 = **0.02%** -> **5/5** (<5%)

**BLOCK E TOTAL: 13/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Working Capital Days (Receivable + Inventory - Payable, Revenue basis;
AR FY26 p.83/161, AR FY25 p.173-175):

| FY | Trade Receivables (Lakh) | Inventory (Lakh) | Trade Payables (Lakh) | Revenue from Ops (Lakh) | Rec. days | Inv. days | Pay. days | WC days |
|---|---|---|---|---|---|---|---|---|
| FY24 | 57.55 | 45,454.96 | 7,219.14 | 2,33,995.99 | 0.09 | 70.90 | 11.27 | 59.72 |
| FY25 | 217.99 | 72,209.90 | 17,670.67 | 3,31,079.01 | 0.24 | 79.62 | 19.48 | 60.38 |
| FY26 | 164.37 | 1,00,394.33 | 11,360.74 | 4,06,512.83 | 0.15 | 90.14 | 10.20 | 80.08 |

(LBF1/LBF2 note: the ~100-inventory-days figure in the load-bearing facts
does not match this formula's result of ~70-90 days; likely a different
revenue or averaging basis on the operator's side. Flagged, not
reconciled here — this is a mechanical scorecard, not an interpretive
stage.)

Peer FY26 EBITDA margin (EBIT+Dep basis, screener-Data_Sheet.csv,
peer P&L blocks), for M2/M5:
- DPABHUSHAN: EBITDA 309.67 Cr / Sales 4,065.13 Cr = **7.62%**
- SENCO: EBITDA (762.74+219.21+81.96=1,063.91) / 8,430.03 = **12.62%**
- PNGJL: EBITDA (542.67+89.76+55.09=687.52) / 10,640.74 = **6.46%**
- MOTISONS: EBITDA (85.09+6.04+1.85=92.98) / 489.54 = **18.99%**
- Peer median (SENCO, PNGJL, MOTISONS) = **12.62%**

Peer FY26 market cap (screener META block): DPABHUSHAN Rs 3,306.17 Cr;
SENCO Rs 5,703.75 Cr; PNGJL Rs 8,902.08 Cr; MOTISONS Rs 2,081.64 Cr.

**M1 Pricing Power**: EBITDA margin FY17 = (7.59+11.67+1.20)/451.02 =
4.54%; FY26 = 7.62%. Expansion = +3.08pp, and revenue CAGR (9yr) =
27.67% >=10%. -> **5/5**
[Flag: LBF1 — part of this margin expansion may be a gold-price /
inventory-holding-gain effect, not structural (mix, making charges).
This mechanical score does not net that out; stage 11 / the operator
must.]

**M2 Cost Advantage vs peer median EBITDA margin**: 7.62% vs peer median
12.62% -> DPABHUSHAN is *below* the peer median. -> **0/5**

**M3 Capital Efficiency**: Fixed Asset Turnover = Sales / Net Block =
4,065.13 / 74.66 = **54.5x** (screener-Data_Sheet.csv), reflecting an
asset-light, rented-showroom model (AR FY26 p. ~9, "predominantly
asset-light, rented-store model"). FAT >3x AND ROCE (45.86%, Block A)
>20% -> **5/5**

**M4 Customer Stickiness**: one revenue-decline year (FY20, Block C3),
fully recovered by FY21 (Sales 1,215.23 Cr vs FY20's 807.17 Cr); Trade
Receivable days near-zero and stable across FY24-FY26 (0.09 to 0.24
days, well within +-10). -> **3/5** (max 1 decline year, fully recovered)

**M5 Scale & Dominance**: DPABHUSHAN is 3rd of 4 by market cap (behind
PNGJL and SENCO, ahead of MOTISONS) -> "top 3 mcap" true. EBITDA margin
rank among the 4 is also 3rd (MOTISONS > SENCO > DPABHUSHAN > PNGJL) ->
not top 2 on margin. Falls to the "top 5 mcap" tier. -> **1/5**

**M6 Technology / R&D**: no R&D disclosed; not an R&D-driven archetype
(jewellery retailer). -> **0/5**

**M7 Regulatory / License**: jewellery retail is not a licence-capped
segment (thousands of listed and unlisted players; BIS hallmarking is a
compliance requirement, not an entry-limiting licence). -> **0/5**

**M8 Distribution**: 12 showrooms as at FY26 year-end, explicitly
growing (AR FY26 p. ~5, "new showrooms in Ratlam and Dhar, taking the
network to 12 showrooms"; guidance of ~6 stores/year to 51 by FY30 per
LBF3). Network growing AND revenue CAGR (27.67%, 9yr) >=15%. Average
revenue per store is disclosed as a metric (AR FY26 p. ~9) but no
multi-year per-store trend is given in this corpus to confirm
stable/growing at store level. -> **3/5**

**M9 Brand**: gross margin (Revenue - Cost of Material Consumed -
Purchase of Stock-in-Trade + Changes in Inventories, Revenue basis) FY26
= 10.28% (AR FY26 P&L), FY25 = 8.03% (AR FY26 restated FY25 column) —
broadly consistent with LBF1's cited 10%/7.72%. Peer gross-margin proxy
using screener "Raw Material Cost" produced a negative and internally
inconsistent result for SENCO (Raw Material Cost > Sales, likely an
inventory-change sign/categorisation artefact in that peer's screener
export) and is not usable for a reliable peer-median comparison. Marked
**PEER DATA NEEDED** (screener export quality, not absence) -> **0/5**

**M10 Switching Costs**: revenue grew in 8 of 9 years (Block C3); Trade
Receivable days stable near-zero (FY24-FY26 range 0.09-0.24 days, well
under 10 days). -> **3/5** (growth all but 1 year AND stable)

**M11 Network Effects** (>=6 years available, full two-window test):
latest 3-year revenue CAGR (FY23-FY26) = 27.29% vs prior 3-year CAGR
(FY20-FY23) = (1,971.11/807.17)^(1/3)-1 = 34.67%. Latest is *below*
prior — deceleration, not acceleration, so the top band fails outright.
Latest 3yr CAGR 27.29% >=20%; Selling & Admin expense as % of sales
(screener-Data_Sheet.csv; FY26 cell blank/not populated) = FY23 0.94%,
FY24 0.88%, FY25 1.06% — roughly stable within the available series (no
FY26 figure to extend the trend; flagged as a data gap). -> **3/5**
(rev CAGR >=20% AND selling % stable/declining)

**M12 Negative WC / Float**: WC days FY24 = 59.72, FY25 = 60.38, FY26 =
80.08 — positive and >45 days in all three available years. -> **0/5**

**MOAT SCORE: 5+0+5+3+1+0+0+3+0+3+3+0 = 23/60**

Moats present (score >=3): M1, M3, M4, M8, M10, M11 = **6 present**

**Moat classification: 6+ present -> FORTRESS**

---

## SCORECARD DASHBOARD

```
BLOCK A  RETURN ON CAPITAL        [====================] 20/20
BLOCK B  CASH GENERATION QUALITY  [                    ]  0/20
BLOCK C  GROWTH                   [==================  ] 18/20
BLOCK D  BALANCE SHEET STRENGTH   [==================  ] 18/20
BLOCK E  SHAREHOLDER ALIGNMENT    [=============       ] 13/20
                                   CORE SCORE:            69/100

MOAT PROFILE (0-5 each, present at >=3)
M1  Pricing Power         [=====] 5  PRESENT
M2  Cost Advantage        [     ] 0
M3  Capital Efficiency    [=====] 5  PRESENT
M4  Customer Stickiness   [===  ] 3  PRESENT
M5  Scale & Dominance     [=    ] 1
M6  Technology/R&D        [     ] 0
M7  Regulatory/License    [     ] 0
M8  Distribution          [===  ] 3  PRESENT
M9  Brand                 [     ] 0  (PEER DATA NEEDED)
M10 Switching Costs       [===  ] 3  PRESENT
M11 Network Effects       [===  ] 3  PRESENT
M12 Negative WC/Float     [     ] 0
                            MOAT SCORE:  23/60  (6 present -> FORTRESS)

GRAND TOTAL: 69 + 23 = 92 / 160
```

## DEAL-BREAKER OVERRIDES

1. Block A <8? No (20). Not triggered.
2. Block B <8? **Yes (0)** -> max GOOD. Triggered, but superseded below.
3. Median ROCE <10%? No (38.91%). Not triggered.
4. Cumulative CFO/PAT <0.50? **Yes (-4.5%)** -> **max AVERAGE**.
   Triggered; this is the binding, most restrictive cap.
5. Pledge >15%? Unknown (E3 NOT FOUND); not triggered on present
   evidence, but the underlying fact is unverified, not confirmed-clean.
6. ND/EBITDA >3x AND IC <3x? No (0.85x / 18.43x). Not triggered.
7. Revenue declined in majority of years? No (1 of 9 years). Not
   triggered.
8. PAT negative in any of last 3 years? No. Not triggered.
9. History <3 years? No. Not triggered.

Binding deal-breaker: **#4, cumulative CFO/PAT -4.5%, driven by FY26
(-97.31 Cr) and FY25 (-18.93 Cr)** — the two years of the aggressive
store-expansion and inventory-build phase (LBF2, LBF3).

## CLASSIFICATION

Core score 69 (60-79 band) + FORTRESS moat class would map to **GOOD+**
by the classification matrix alone. Deal-breaker #4 caps this at
**AVERAGE**, and #4 is the binding, most restrictive override on the
table.

**FINAL CLASSIFICATION: AVERAGE** (capped from GOOD+ by deal-breaker #4)

Strongest block: **Block A (Return on Capital), 20/20** — ROCE
37.4-45.9% and ROE 29.5-40.9% across the three years with filed
granularity, both rising.
Weakest block: **Block B (Cash Generation Quality), 0/20** — every
sub-metric scored zero; cumulative CFO is negative against Rs 541 Cr of
cumulative PAT, and FCF is negative in all three anchored years.

## DECISION LINE

DPABHUSHAN screens **AVERAGE** on Gate 0 mechanics. A FORTRESS-level moat
profile (6 of 12 tests present, led by capital efficiency and pricing
power) and a maxed-out Block A sit against a maxed-out-in-the-wrong-
direction Block B: cumulative operating cash flow is negative across the
full 10-year window and free cash flow is negative in every one of the
three years this scorecard can anchor. The historical depressor is
named and dated: FY25-FY26, the two years of the showroom-expansion and
inventory-build phase. Per CLAUDE.md, this classification does not halt
the run; it flags. The named tension for stage 2 and Halt 1: is the
FY25-FY26 cash conversion collapse GROWTH-INDUCED (new-store stock,
self-correcting as showrooms mature) or STRUCTURAL (a permanent feature
of this business's working-capital intensity)? LBF2 exists precisely to
resolve this before any valuation work proceeds.

---

```yaml
stage: B01-gate0
company: "DPABHUSHAN"
run_date: "2026-09-19"
model: claude-sonnet-5
status: complete
input_gaps:
  - "COLLECTOR WARNING (verbatim): shareholding/ is empty: no source is automated yet. Push the latest quarterly shareholding pattern by hand; it closes the FII+DII UA qualifier and the promoter pledge trend."
  - "COLLECTOR WARNING (verbatim): screener export sheets came out EMPTY (formulas with no cached values), so no CSV was written for them: screener:Profit & Loss, screener:Quarters, screener:Balance Sheet, screener:Cash Flow, screener:Customization, THANGAMAYL:Profit & Loss, THANGAMAYL:Quarters, THANGAMAYL:Balance Sheet, THANGAMAYL:Cash Flow, THANGAMAYL:Customization, SENCO:Profit & Loss, SENCO:Quarters, SENCO:Balance Sheet, SENCO:Cash Flow, SENCO:Customization. Open Financials.xlsx once in Excel or LibreOffice, save it, then run --push-again."
  - "COLLECTOR WARNING (verbatim): no results PDFs yet (screener has none): add later on github or locally + --push-again"
  - "COLLECTOR WARNING (verbatim): no rating PDF yet: add later the same way"
  - "RESOLVED AT INTAKE: results/ filled from BSE (AttachHis): Q1 FY27 (board outcome 20-Jul-2026), Q4/FY26 audited (21-May-2026), Q3 FY26 (board outcome 23-Jan-2026, BSE-filed 29-Jan-2026). Q2 FY26 results (03-Nov-2025) held in inputs/other/ as an extra backward check; its text layer is poor OCR."
  - "RESOLVED AT INTAKE: rating/ holds the company's Reg 30 CARE intimation (09-Jan-2026) and the full CARE press release with rationale (08-Jan-2026, careratings.com): CARE A-; Stable / CARE A2+, reaffirmed; limits Rs 51.95 Cr LT + Rs 288 Cr LT/ST."
  - "RESOLVED AT INTAKE (PARTIAL): shareholding/ holds the screener shareholding table as text (Sep-2023 to Jun-2026; promoter 74.89%, FII 0.23%, DII 0.00% at Jun-2026). It is a SCREENER AGGREGATION, NOT A FILING: weigh, do not anchor. The filed pattern at 31-Mar-2026 is in the FY26 AR. The UA FII+DII qualifier may be read from the AR filed pattern; the Jun-2026 figure is unanchored."
  - "screening: EMPTY-CSV defect present. Profit & Loss, Balance Sheet, Cash Flow and Quarters sheets are absent for the subject and all peers. The four Data_Sheet CSVs (screener-Data_Sheet.csv for DPABHUSHAN; SENCO, PNGJL, MOTISONS) are populated with raw annual P&L, balance sheet, cash flow and quarterly rows. Stage 1 reads Data_Sheet only. THANGAMAYL-Data_Sheet.csv moved to inputs/other/ (rejected peer)."
  - "screener basis: main URL is STANDALONE (/company/DPABHUSHAN/). The /consolidated/ page stops at Mar-2022; the FY26 AR states the company has no subsidiary, JV or associate. Standalone is the only basis."
  - "annual-report/: TWO ARs held, FY26 (Reg 34 filing 03-Sep-2026, 106 PDF pages, each PDF page a two-page print spread, printed pages up to 205) and FY25 (Reg 34 filing 05-Sep-2025, 221 PDF pages). Contract is 0-1: FY26 is the primary AR; FY25 is the backward-check AR. The FY26 AR duplicate in announcements/ (9c3bc998) was removed."
  - "concalls: 4 transcripts held; quarter read from page 1: Concall_Dec_2025 = Q2 FY26 (call 06-Nov-2025, filed 12-Nov-2025; screener filename month is wrong); Concall_Jan_2026 = Q3 FY26 (call 24-Jan-2026); Concall_May_2026 = Q4 FY26 (call 22-May-2026); Concall_Jul_2026 = Q1 FY27 (call 22-Jul-2026). Stage 5 uses the three most recent (Q3 FY26, Q4 FY26, Q1 FY27); Q2 FY26 is an extra backward check."
  - "peer-concalls: 12 transcripts, 4 per peer. Peer set changed at intake: THANGAMAYL replaced by MOTISONS because Thangamayil files no earnings-call transcripts on BSE."
  - "announcements/SAST-*.pdf: four Reg 29(2) SAST disclosures by promoter Santosh Kataria; THREE are image-only scans with NO TEXT LAYER: UNREADABLE by the text route in this session (pdftoppm absent). Named here, never anchored."
  - "research: EMPTY. No broker notes. No effect on anchored evidence."
  - "presentation: 2 decks, Q4 FY26 (22-May-2026) and Q1 FY27 (21-Jul-2026). Earlier decks not held."
  - "prospectus: EMPTY, not expected (listed >3 years). Not a gap."
  - "STAGE 1 (this run): screener-Data_Sheet.csv has no Current Liabilities, Trade Payables or capex-split line for any year. ROCE, D/E-style leverage and WC-days are computable per formula only for FY24-FY26, using the AR standalone financials (FY26 AR gives FY26+FY25; FY25 AR gives FY25+FY24). Block C growth metrics use the full FY17-FY26 screener series; Block B1 uses the full 10-year CFO/PAT series; B2-B4 and Block A/D/most WC-moat tests use the FY24-FY26 AR-detail window only."
  - "STAGE 1 (this run): E3 promoter pledge searched in both ARs and the CARE rationale; no SEBI-format pledge/encumbrance table or statement found for promoter shareholding (only an unrelated vehicle-loan pledge note). Scored NOT FOUND / 0, not assumed clean."
  - "STAGE 1 (this run): M9 peer gross-margin proxy unusable — screener-Data_Sheet.csv Raw Material Cost for SENCO FY26 exceeds Sales, an apparent inventory-change categorisation artefact in that peer's export. Marked PEER DATA NEEDED rather than guessed."
  - "STAGE 1 (this run): screener-Data_Sheet.csv 'Interest' row for FY24 (14.12 Cr) and FY25 (17.14 Cr) does not match the AR's own 'Finance Cost' line (11.62 Cr and 14.44 Cr respectively) for the same years; FY26 matches exactly (16.22 Cr both sources). AR figures used throughout this scorecard; screener figure not used anywhere in the arithmetic."
flags:
  - {type: FLAG-GATE0, reason: "Classification capped at AVERAGE by deal-breaker #4 (cumulative CFO/PAT -4.5%). Historical depressor named: FY25-FY26 cash-conversion collapse (CFO -18.93 Cr then -97.31 Cr) during the showroom-expansion/inventory-build phase (LBF2/LBF3). FORTRESS moat profile (6/12) and maxed Block A (20/20 ROCE/ROE) sit against a zeroed Block B (0/20); stage 2 must classify GROWTH-INDUCED vs STRUCTURAL before Halt 1."
  - {type: FLAG-CASH, reason: "block_b_trend deteriorating: CFO -0.28 Cr (FY24) -> -18.93 Cr (FY25) -> -97.31 Cr (FY26), tracking Inventory Rs 454.55 Cr -> Rs 722.10 Cr -> Rs 1,003.94 Cr. FCF negative in all 3 anchored years (FY24 -3.95, FY25 -44.22, FY26 -104.49 Cr)."
data_years: 10
fy_range: "FY2017 to FY2026 (P&L/CF full window; balance-sheet-detail window FY2024 to FY2026 only, see data_notes)"
blocks: {A: 20, B: 0, C: 18, D: 18, E: 13}
core_score: 69
moat_score: 23
grand_total: 92
moats_confirmed: 6
moat_class: "FORTRESS"
classification: "AVERAGE"
deal_breakers:
  - "#2 Block B <8 (score 0) -> max GOOD (superseded by #4)"
  - "#4 Cumulative CFO/PAT <0.50 (-4.5%) -> max AVERAGE (BINDING)"
history_downgrade: false
data_notes:
  - "No loss-to-profit swing in any CAGR window (Revenue and PAT both positive at every endpoint used)."
  - "ROCE/ROE/D1-D4/WC-days computed only for FY24-FY26 (the only years with a filed Current Liabilities and Trade Payables split); Block C growth uses the full FY17-FY26 screener series; B1 uses the full 10-year CFO/PAT series; B2-B4 use the FY24-FY26 AR-detail window (capex only anchored there)."
  - "M9 (Brand) marked PEER DATA NEEDED: screener Raw Material Cost line for peer SENCO FY26 exceeds Sales, an apparent categorisation artefact; DPABHUSHAN's own AR-anchored gross margin (10.28% FY26 vs 8.03% FY25 restated) is directionally consistent with LBF1's cited 10%/7.72% but not independently peer-ranked here."
  - "E3 (pledge) marked NOT FOUND after searching both ARs and the CARE rationale; no SEBI-format pledge/encumbrance table for promoter shareholding was located in the corpus."
  - "screener-Data_Sheet.csv 'Interest' row for FY24/FY25 is inconsistent with the AR's own Finance Cost line for the same years (FY26 matches); AR figures used throughout, screener figure not used in any calculation."
  - "Inventory-days formula result (~70-90 days across FY24-FY26) does not match LBF2's cited ~100 days; likely a different revenue or averaging basis upstream. Flagged for stage 2, not reconciled here."
block_b_trend: "deteriorating - CFO -0.28 Cr (FY24) -> -18.93 Cr (FY25) -> -97.31 Cr (FY26), tracking a 39% YoY inventory build in FY26 (Rs 722.10 Cr -> Rs 1,003.94 Cr); FCF negative in all 3 anchored years."
analyst_note: "The scorecard's central tension: Block A maxes at 20/20 (ROCE 37-46%, ROE 29-41%, both rising) while Block B zeroes at 0/20 (cumulative CFO/PAT -4.5%, FCF negative all 3 anchored years). Both are real, from the same anchored numbers, in the same FY24-FY26 window. The deal-breaker rule correctly caps classification at AVERAGE rather than letting the FORTRESS moat profile and strong core score alone read as GOOD+. LBF1 (gold-price/inventory-holding-gain vs structural margin) and LBF2 (growth-induced vs structural cash burn) are the two questions that resolve which read is right; this stage cannot resolve them, only surface the numbers. E3 (pledge) is unverified, not confirmed-clean, despite a direct AR search."
```
