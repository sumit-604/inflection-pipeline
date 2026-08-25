# GATE 0 SCORECARD — MAN INDUSTRIES (INDIA) LTD (MANINDS)
Run date: 2026-08-21 | Model: claude-sonnet-5 | Stage: B01-gate0

Data available: 10 years (FY17 to FY26). Scoring adapted to 10-year history
(full-cycle confidence, per data-confidence table).

Sector note: the intake manifest labels MANINDS "Pharma/CDMO" — this is
WRONG. The company is a line-pipe (LSAW/HSAW steel pipe) manufacturer for
oil & gas transmission. Peers used throughout (Block F, M2/M5/M9) are Jindal
SAW, Ratnamani Metals & Tubes, and Welspun Corp, the three listed line-pipe
comparables supplied. This mislabel does not change any Gate 0 score; it is
carried to input_gaps for stage 3 correction.

All ₹ figures in Crores unless stated. Primary source: screener-Data_Sheet.csv
(screener-data). Cross-checks: AR = annual-report__Annual_Report.txt (FY24-25
Annual Report, page markers = source PDF page); results filing = FY26 audited
standalone financial statements (results__4da9bef6...txt).

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 6/20

Basis: ROCE computed (not provided by Data_Sheet) = EBIT ÷ (Net Worth +
Borrowings), i.e. Capital Employed = Total Assets − "Other Liabilities"
bucket (screener's aggregate liabilities-other-than-equity-and-borrowings
line; no current/non-current split is available to isolate Current
Liabilities directly — this is the stated basis, screener-data, computed).
EBIT = PBT + Interest (screener-data, computed).

| Year | EBIT | Capital Employed | ROCE | PAT | Avg Net Worth | ROE |
|---|---|---|---|---|---|---|
| FY17 | 80.63 | 1045.35 | 7.71% | 33.57 | 598.28 (closing only, no opening) | 5.61% |
| FY18 | 138.40 | 1019.92 | 13.57% | 63.69 | 625.24 | 10.19% |
| FY19 | 152.92 | 945.94 | 16.17% | 58.84 | 677.11 | 8.69% |
| FY20 | 129.68 | 1040.19 | 12.47% | 55.50 | 724.20 | 7.66% |
| FY21 | 189.49 | 1130.44 | 16.76% | 100.85 | 790.62 | 12.76% |
| FY22 | 172.27 | 999.13 | 17.24% | 101.58 | 888.53 | 11.43% |
| FY23 | 130.48 | 1432.93 | 9.11% | 67.04 | 1037.24 | 6.46% |
| FY24 | 232.13 | 1730.79 | 13.41% | 105.14 | 1268.58 | 8.29% |
| FY25 | 307.98 | 2083.49 | 14.78% | 153.17 | 1506.07 | 10.17% |
| FY26 | 388.97 | 2714.52 | 14.33% | 170.48 | 1846.91 | 9.23% |

(all rows: screener-data, computed)

- **A1 Median ROCE = 13.95%** (median of 10 yrs) → band 10-14.9% → **score 1**
- **A2 Minimum single-year ROCE = 7.71% (FY17)** → <8% → **score 0**
- **A3 Median ROE = 8.96%** (median of 10 yrs) → <12% → **score 0**
- **A4 ROCE trend, FY26 (14.33%) vs FY17 (7.71%)**: latest ≥ earliest → **score 5**

Block A total: 1+0+0+5 = **6/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 8/20

CFO and PAT: screener-data. FCF proxy = CFO + CFI (screener-data does not
break out a separate capex/PP&E-purchase line in the Cash Flow section — only
CFO/CFI/CFF/Net Cash Flow are given — so CFI, the full net investing cash
flow, is used as the capex proxy; this can include non-capex investing items
such as purchase/sale of investments, so FCF here is a proxy, stated as such
per data_notes).

| Year | CFO | CFI | FCF (=CFO+CFI) | PAT |
|---|---|---|---|---|
| FY17 | -74.78 | 20.59 | -54.19 | 33.57 |
| FY18 | 131.99 | -104.92 | 27.07 | 63.69 |
| FY19 | 137.35 | 0.16 | 137.51 | 58.84 |
| FY20 | 214.31 | -46.34 | 167.97 | 55.50 |
| FY21 | -59.89 | 4.26 | -55.63 | 100.85 |
| FY22 | 450.94 | -119.06 | 331.88 | 101.58 |
| FY23 | -120.30 | -135.49 | -255.79 | 67.04 |
| FY24 | 344.91 | -279.31 | 65.60 | 105.14 |
| FY25 | 67.99 | -41.33 | 26.66 | 153.17 |
| FY26 | 514.91 | -593.92 | -79.01 | 170.48 |

(all: screener-data, computed)

Cumulative CFO = 1607.43 | Cumulative PAT = 909.86 | Cumulative FCF = 312.07

- **B1 Cumulative CFO ÷ Cumulative PAT = 1607.43 ÷ 909.86 = 1.767** → ≥1.00 → **score 5**
- **B2 FCF-positive years = 6 of 10 (FY18,19,20,22,24,25) = 60%** → band 50-74% → **score 2**
- **B3 Cumulative FCF ÷ Cumulative PAT = 312.07 ÷ 909.86 = 0.343** → band 0.20-0.39 → **score 1**
- **B4 WC Days change, latest vs earliest**: see below → increase >15 days → **score 0**

Block B total: 5+2+1+0 = **8/20**

### WC Days detail (B4) — CONTEXT FLAG: FY25-26 balloon confirmed
Payable Days could NOT be computed: screener Data_Sheet does not disclose
Trade Payables separately (only an aggregate "Other Liabilities" bucket that
mixes payables, provisions, deferred tax and other current/non-current
items). WC Days below = Receivable Days + Inventory Days ONLY (payables
excluded); basis stated per formula rules. (screener-data, computed)

| Year | Receivable Days | Inventory Days | WC Days (ex-payables) |
|---|---|---|---|
| FY17 | 117.28 | 37.50 | 154.78 |
| FY18 | 86.90 | 94.98 | 181.88 |
| FY19 | 91.24 | 35.60 | 126.84 |
| FY20 | 93.35 | 78.75 | 172.10 |
| FY21 | 115.10 | 58.19 | 173.29 |
| FY22 | 92.90 | 54.33 | 147.23 |
| FY23 | 80.83 | 66.57 | 147.40 |
| FY24 | 41.25 | 74.99 | 116.24 |
| FY25 | 93.29 | 132.09 | 225.38 |
| FY26 | 103.42 | 157.24 | 260.66 |

FY26 (260.66) vs FY17 (154.78) = +105.88 days → B4 **score 0**.

**block_b_trend anchor number**: WC days (ex-payables) rose from **116.2 days
(FY24) to 260.7 days (FY26), a +144.4 day increase in two years**
(screener-data, computed) — this is the single number carrying the
FY25-FY26 balloon flagged in context, driven by both receivables (+62 days)
and inventory (+82 days) FY24→FY26.

---

## BLOCK C: GROWTH (Max 20) — Score: 15/20

Revenue and PAT: screener-data.

- **C1 Revenue CAGR, FY17 (₹1060.49cr) → FY26 (₹3563.90cr), 9yr = 14.41%**
  (screener-data, computed) → band 10-14.9% → **score 3**
- **C2 PAT CAGR, FY17 (₹33.57cr) → FY26 (₹170.48cr), 9yr = 19.79%**
  (screener-data, computed) → band 15-19.9% → **score 4**
- **C3 Positive YoY revenue years = 8 of 9 (only FY20 declined, -20.8% vs
  FY19)** = 88.9% (screener-data, computed) → band 75-99% → **score 3**
- **C4 PAT CAGR − Revenue CAGR = 19.79% − 14.41% = +5.38pp** → ≥+3pp →
  **score 5**

Block C total: 3+4+3+5 = **15/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 12/20

Latest = FY26. Borrowings/Cash&Bank/Net Worth: screener-data. D4 sourced
separately (see note) because screener-data has no current/non-current
split.

- **D1 Net Debt ÷ EBITDA, FY26**: Net Debt = Borrowings 627.98 − Cash&Bank
  657.21 = **−29.23 (net cash)** (screener-data, computed) → **score 5**
- **D2 Interest Coverage, FY26**: EBIT 388.97 ÷ Interest 152.03 =
  **2.56x** (screener-data, computed) → band 1.5-2.9x → **score 1**
- **D3 Debt ÷ Equity, FY26**: Borrowings 627.98 ÷ Net Worth 2086.54 =
  **0.301** (screener-data, computed) → band 0.1-0.5 → **score 4**
- **D4 Current Ratio, FY26**: Total Current Assets ₹3037.93cr ÷ Total
  Current Liabilities ₹2287.96cr = **1.328** (results FY26 standalone
  BS, p.24) → band 1.2-1.49 → **score 2**

Block D total: 5+1+4+2 = **12/20**

**Cross-check flag (not scored, for stage 8)**: the FY26 standalone BS
(results filing p.24) shows non-current + current borrowings (ex-lease) of
₹433.38cr, and ₹534.93cr including lease liabilities — both below
screener-data's FY26 Borrowings figure of ₹627.98cr. Difference ≈
₹93-195cr, unreconciled. D1/D2/D3 above use screener-data (primary
source per DATA_SOURCES); if the lower results-filing figure governs
instead, D1 stays net-cash (still score 5) and D3 improves, so this does
not currently move the classification, but stage 8 should reconcile it.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 8/20

- **E1 Promoter holding, latest (Jun 2026) = 43.21%** (screener
  shareholding, operator-ferried 2026-08-24) → band 40-49.9% → **score 3**
- **E2 Promoter holding change, Sep 2023 (49.61%, earliest point in the
  supplied series, ≈2.75yr window) → Jun 2026 (43.21%) = −6.40pp**
  (screener shareholding, operator-ferried 2026-08-24) → decreased >3% →
  **score 0**
- **E3 Promoter pledge = N/A (not in provided data)** → **score 0**.
  The shareholding source has no pledge column. The AR does NOT carry the
  standard disclosed "% of promoter holding pledged" either; it carries a
  different disclosure — Note 15(a) (AR p.153): "Pledge of 65,00,000 shares
  of the Company by the promoters ... " as loan security for an SBI foreign
  currency term loan, as at March 31, 2025. Converting this raw share count
  to a "% of promoter holding" figure would require assuming (a) total
  shares outstanding basis and (b) that this is the ONLY promoter pledge —
  neither is confirmed, so per the "never estimate" rule this is NOT
  converted into a score. Flagged in data_notes and input_gaps for stage 8
  to source the formal disclosure; a rough unscored back-of-envelope
  (65,00,000 ÷ [46.20% × 6,47,35,188 shares, FY25 basis] ≈ 20%) would, if
  confirmed, cross the >15% deal-breaker threshold — surfaced as a risk
  signal only, not applied here.
- **E4 Contingent Liabilities ÷ Net Worth**: AR Note 33a (AR p.162, FY2024-25
  Annual Report — the latest AR in the provided corpus; FY26 AR notes were
  not supplied) = Entry Tax/VAT ₹366.77L + Excise/Customs/GST ₹2292.09L +
  Income tax ₹3712.10L + SEBI ₹25.00L = **₹6395.96 lakh = ₹63.96cr**.
  Net Worth, same period (FY25, screener-data) = ₹1607.27cr.
  Ratio = 63.96 ÷ 1607.27 = **3.98%** → <5% → **score 5**.
  (Arbitration/legal cases of ₹10,936.07L, Note 33b, are amounts the company
  expects to RECOVER, not a liability, and are excluded from this ratio.)

Block E total: 3+0+0+5 = **8/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 11/60

Peers used for M2/M5/M9: Jindal SAW (JINDALSAW), Ratnamani Metals & Tubes
(RATNAMANI), Welspun Corp (WELCORP) — all peer-Data_Sheet, computed, FY26.

| Test | Score | Bar | Basis |
|---|---|---|---|
| M1 Pricing Power | 3 | [███░░] | 3yr-avg EBITDA margin FY17-19 (10.46%) vs FY24-26 (10.85%) = +0.39pp (stable ±2pp); revenue CAGR 14.41% ≥10% → score 3 (screener-data, computed) |
| M2 Cost Advantage | 0 | [░░░░░] | MANINDS FY26 EBITDA margin 13.13% vs peer median 16.18% (Jindal SAW 13.00%, Ratnamani 19.34%, Welspun Corp 16.18%) = −3.05pp, below median → score 0 (screener-data + peer-Data_Sheet, computed) |
| M3 Capital Efficiency | 1 | [█░░░░] | FAT = Sales 3563.9 ÷ Net Block 864.08 = 4.13x (>3x); ROCE FY26 14.33% (not >20%, not >15%, but >12%) → FAT>1x AND ROCE>12% → score 1 (screener-data, computed) |
| M4 Customer Stickiness | 3 | [███░░] | 1 revenue-decline year (FY20, -20.8%), fully recovered by FY23 (2231.34 > FY19's 2221.71) → score 3 (screener-data, computed) |
| M5 Scale & Dominance | 0 | [░░░░░] | Mcap: MANINDS ₹5354.93cr, smallest of the 4 compared (Jindal SAW ₹18,615.99cr, Ratnamani ₹16,473.36cr, Welspun Corp ₹60,831.43cr); FY26 EBITDA margin 13.13% ranks 3rd of 4 (only above Jindal SAW) → not top-3 mcap, not top-2 margin → score 0. PEER DATA is limited to these 3; full segment universe not supplied (screener-data + peer-Data_Sheet, computed) |
| M6 Technology/R&D | 0 | [░░░░░] | R&D/Revenue **N/A (not in provided data)** → score 0 |
| M7 Regulatory/License | 0 | [░░░░░] | Line-pipe (LSAW/HSAW) manufacturing is a competitive industrial segment, not a licence/quota business; more than 10 listed+unlisted players in India → unregulated → score 0 |
| M8 Distribution | 0 | [░░░░░] | No dealer/distribution-reach metric disclosed in provided sources (business is EPC/project-tender, not a distribution-network model) → score 0 |
| M9 Brand (GM proxy) | 0 | [░░░░░] | GM proxy = (Revenue − Raw Material Cost) ÷ Revenue, FY26: MANINDS 29.58% vs peer median 40.54% (Jindal SAW 40.54%, Ratnamani 41.39%, Welspun Corp 35.22%) = −10.96pp, at/below peers → score 0 (screener-data + peer-Data_Sheet, computed, GM proxy stated) |
| M10 Switching Costs | 3 | [███░░] | Growth in 8 of 9 YoY years (all but FY20); Receivable Days FY17 117.28 → FY26 103.42, a decline (stable/improved, not a rise) → score 3 (screener-data, computed) |
| M11 Network Effects | 1 | [█░░░░] | Latest-3yr revenue CAGR (FY23→FY26) 16.91% > prior-3yr (FY20→FY23) 8.24% — condition 1 met. Selling & admin % of sales roughly flat (prior-window avg 7.29% vs latest-window avg 7.30%, FY24-25 only — **FY26 Selling and admin expense not disclosed in screener Data_Sheet**, so the latest window is incomplete); not clearly declining → does not qualify for top band; latest-3yr CAGR 16.91% <20% so mid band also fails; falls to "growth >15% but selling% rising/flat" → score 1, scored conservatively per data-limitation instruction (screener-data, computed) |
| M12 Negative WC/Float | 0 | [░░░░░] | WC Days (ex-payables) never below 116 days in any of the 10 years (min FY24 116.24, max FY26 260.66), all >45 → score 0 (screener-data, computed) |

**Moat score total: 3+0+1+3+0+0+0+0+0+3+1+0 = 11/60**

**Moats present (score ≥3): 3** — M1 Pricing Power, M4 Customer Stickiness,
M10 Switching Costs.

Moat classification: 3 present → band "2-3 = MODERATE" → **MOAT CLASS: MODERATE**

---

## CLASSIFICATION

Data confidence: 10 years (FY17-FY26) → **10+ yrs = full** confidence, no
downgrade tier applied. `history_downgrade: false`

| Block | Score | Max | % |
|---|---|---|---|
| A — Return on Capital | 6 | 20 | 30% |
| B — Cash Generation | 8 | 20 | 40% |
| C — Growth | 15 | 20 | 75% |
| D — Balance Sheet | 12 | 20 | 60% |
| E — Shareholder Alignment | 8 | 20 | 40% |
| **Core score** | **49** | **100** | **49%** |
| F — Moat (informational, not in core) | 11 | 60 | 18% |
| **Grand total** | **60** | **160** | — |

**Strongest block: C — Growth (15/20, 75%)** — a 9-year revenue CAGR of
14.41% and PAT CAGR of 19.79%, with growth outpacing revenue by 5.38pp
(margin-accretive growth), and only one down-revenue year in the window
(FY20, COVID-period).

**Weakest block: A — Return on Capital (6/20, 30%)** — median ROCE (13.95%)
and median ROE (8.96%) sit below the top bands across the full 10-year
cycle; the minimum single-year ROCE (7.71%, FY17) and the sub-12% ROE
median are what drag this block down, not a single bad year.

### Deal-breaker overrides triggered
1. **Block A < 8 (actual 6) → caps classification at max GOOD.** Driver
   years: FY17 (ROCE 7.71%, the single-year minimum) and the sub-12%
   full-cycle ROE median (8.96%) — this is a structural, cycle-wide
   under-return pattern, not one bad year, per Block A detail above.

No other deal-breakers triggered (median ROCE 13.95% is not <10%; cumulative
CFO/PAT 1.767 is not <0.50; ND/EBITDA is net-cash so the >3x-AND-IC<3x
combination cannot trigger; revenue declined in only 1 of 9 years, not a
majority; PAT was positive in all of the last 3 years; pledge is N/A/unscored
so the >15% pledge deal-breaker is not formally applied, see E3 note above;
history is 10 years, not <3).

### Classification matrix application
Core score = 49 → falls in the **Core 40-59 band = AVERAGE**, independent
of moat class (the 40-59 band does not branch on moat tier). The Block A
deal-breaker cap (max GOOD) is non-binding here since AVERAGE already sits
below GOOD.

```
┌─────────────────────────────────────────┐
│  CLASSIFICATION: AVERAGE                 │
│  Core score:  49 / 100                   │
│  Moat class:  MODERATE (3 tests present) │
│  Grand total: 60 / 160                   │
│  Deal-breaker: Block A<8 (non-binding,   │
│    core score already caps at AVERAGE)   │
└─────────────────────────────────────────┘
```

**DECISION: AVERAGE.** Growth is real and margin-accretive (Block C
75%), and the balance sheet carries net cash on a screener-data basis
(Block D 60%, but interest coverage is thin at 2.56x). The name is capped
by a structurally sub-par capital-return record across the full cycle
(Block A 30%), weak cash-to-FCF conversion in more than a third of the
FCF-negative years (Block B 40%), a promoter stake that both fell 6.4pp in
under 3 years and carries an unresolved pledge question (Block E 40%), and
a MODERATE (not STRONG/FORTRESS) quantitative moat where the company reads
weaker than its three listed line-pipe peers on cost (M2), scale (M5) and
gross margin (M9). The FY25-FY26 working-capital balloon (+144 days in two
years, receivables and inventory both) is the single sharpest recent-period
flag and should be a specific focus of the corpus read in stage 3 onward.

---

## FLAG-GATE0
Classification landed at AVERAGE (≤AVERAGE threshold) with identified
depressors:
- Block A (Return on Capital): full-cycle median ROCE 13.95% and median
  ROE 8.96% below top bands; minimum single-year ROCE 7.71% (FY17).
- Block B4 / block_b_trend: WC days (ex-payables) rose from 116.2 (FY24)
  to 260.7 (FY26), +144.4 days in two years — receivables and inventory
  both drove it.
- Block E: promoter holding down 6.40pp in <3 years; pledge status
  unresolved (AR carries a partial, non-standard pledge disclosure that
  a rough unscored compute puts near ~20% of promoter holding).
- Moat: MODERATE only — peer-relative weakness on cost advantage (M2),
  scale (M5) and gross margin (M9) against the three listed line-pipe
  comparables.
