# STAGE 1 — GATE 0 SCORECARD: Aimtron Electronics Ltd (AIMTRON)
Run date: 2026-07-12 | Model: Sonnet 5 | Mode: Pipeline (full run, first for this ticker)

Data available: 3 years (FY2024 to FY2026). Scoring adapted to 3-year history.

## DATA BASIS NOTE (read first)

Two conflicting data sets exist for FY26: screener.in's `screener-Data_Sheet.csv`
(Sales Rs 301.16 Cr, PAT Rs 45.97 Cr) and the company's own **audited** standalone
results filed 28-Apr-2026 (Revenue from Operations Rs 257.13 Cr, PAT Rs 39.16 Cr).
Cross-checking the screener FY26 expense lines (Raw Material Rs 281.29 Cr + Change
in Inventory Rs 67.66 Cr + Employee Cost Rs 12 Cr + Other Expenses Rs 9.76 Cr =
Rs 370.71 Cr) against Sales of Rs 301.16 Cr shows an internal inconsistency — the
implied expense total exceeds sales by ~Rs 70 Cr, incompatible with the stated
positive PBT of Rs 60.91 Cr. The screener FY26 P&L breakdown is therefore
unreliable. **This scorecard uses the audited standalone figures (AR2025 for
FY2024/FY2025, and the 28-Apr-2026 results filing for FY2025/FY2026) throughout**,
cross-checked internally (Total Income − Total Expenses = PBT ties out in every
year on this basis). Screener consolidated figures are cited only where they
independently corroborate a standalone number (e.g. FY25 borrowings, FY25 PAT).
Flagged as FLAG-DATA-QUALITY below.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 14/20

Basis: standalone audited (AR2025 pp.88-89 for FY24/FY25; results 28-Apr-2026 pp.2-3
for FY25/FY26). ROCE and ROE are **computed** (screener's own ROCE/ROE rows in
`screener-Balance_Sheet.csv` are blank for this company).

| Metric | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| EBIT (PBT + Finance Costs) | Rs 20.27 Cr (AR2025 p.89) | Rs 32.37 Cr (results 28-Apr-2026 p.2) | Rs 54.70 Cr (results 28-Apr-2026 p.2) |
| Capital Employed (Total Assets − Current Liabilities) | Rs 64.39 Cr (AR2025 p.88) | Rs 155.68 Cr (results 28-Apr-2026 p.3) | Rs 227.95 Cr (results 28-Apr-2026 p.3) |
| ROCE (computed) | 31.48% | 20.79% | 24.00% |
| PAT | Rs 13.60 Cr (AR2025 p.89) | Rs 25.74 Cr (results 28-Apr-2026 p.2) | Rs 39.16 Cr (results 28-Apr-2026 p.2) |
| Net Worth (closing) | Rs 51.70 Cr (AR2025 p.88) | Rs 155.09 Cr (results 28-Apr-2026 p.3) | Rs 227.86 Cr incl. Rs 20.32 Cr share-warrant money (results 28-Apr-2026 p.3) |
| ROE (computed; FY24 uses closing NW only, opening NW not available pre-FY24) | 26.30% | 24.89% | 20.46% |

- **A1 Median ROCE = 24.00%** (band 20-24.9%) → **4/5**
- **A2 Minimum single-year ROCE = 20.79%** (≥15%) → **5/5**
- **A3 Median ROE = 24.89%** (≥20%) → **5/5**
- **A4 ROCE trend, latest (FY26=24.00%) vs earliest (FY24=31.48%) = −7.48pp** (decline >5pp) → **0/5**

Note: FY24's unusually high 31.48% ROCE reflects a capital-light, pre-IPO base
(low asset denominator before the June-2024 IPO and Sept-2025 warrant capital
were deployed into plant, receivables and inventory). The A4 decline captures
real capital dilution as growth capital was put to work, not deteriorating unit
economics — ROCE is still comfortably in the 20-25% zone in both post-IPO years.

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 0/20 ⚠ WEAKEST BLOCK

Basis: standalone audited, all 3 years (AR2025 p.90 CF for FY24/FY25; results
28-Apr-2026 pp.4-5 CF for FY25/FY26).

| Metric | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| CFO | Rs 6.69 Cr (AR2025 p.90) | Rs (17.69) Cr (results 28-Apr-2026 p.4) | Rs 0.47 Cr (results 28-Apr-2026 p.4) |
| Capex (Purchase of PPE, CF basis) | Rs 3.97 Cr (AR2025 p.90) | Rs 12.96 Cr (results 28-Apr-2026 p.4) | Rs 4.36 Cr (results 28-Apr-2026 p.4) |
| FCF (CFO − Capex) | Rs 2.72 Cr | Rs (30.65) Cr | Rs (3.89) Cr |
| PAT | Rs 13.60 Cr | Rs 25.74 Cr | Rs 39.16 Cr |
| WC Days (RD+ID−PD, revenue basis) | 183.5 days (AR2025 pp.88-89) | 171.7 days | 220.0 days (results 28-Apr-2026 pp.2-3) |

- **B1 Cumulative CFO ÷ Cumulative PAT** = (6.69−17.69+0.47) ÷ (13.60+25.74+39.16)
  = **−10.53 ÷ 78.50 = −0.13x** (negative, <0.50) → **0/5**
- **B2 FCF-positive years** = 1 of 3 (FY24 only) = 33.3% (<50%) → **0/5**
- **B3 Cumulative FCF ÷ Cumulative PAT** = −31.82 ÷ 78.50 = **−0.41** (negative) → **0/5**
- **B4 Change in WC Days, latest vs earliest** = 220.0 − 183.5 = **+36.6 days** (increased >15) → **0/5**

**Deal-breaker #4 triggers here: cumulative CFO/PAT (−0.13x) is deeply below the
0.50 floor.** Driven by FY25 (CFO −Rs 17.69 Cr against PAT +Rs 25.74 Cr, on a
+Rs 70 Cr trade-receivables build) and a still-weak FY26 (CFO barely positive
against PAT +Rs 39.16 Cr, on a further receivables/inventory build funded by IPO
and Sept-2025 warrant proceeds, not by operations). See FLAG-CASH.

## BLOCK C: GROWTH (Max 20) — Score: 20/20 ✓ STRONGEST BLOCK (tied)

Basis: standalone audited, FY24→FY26 (AR2025 p.89; results 28-Apr-2026 p.2).

| Metric | Value |
|---|---|
| Revenue: FY24 Rs 92.98 Cr → FY25 Rs 158.31 Cr → FY26 Rs 257.13 Cr | all anchored above |
| PAT: FY24 Rs 13.60 Cr → FY25 Rs 25.74 Cr → FY26 Rs 39.16 Cr | all anchored above |

- **C1 Revenue CAGR (2yr)** = (257.13/92.98)^(1/2) − 1 = **66.3%** (≥20%) → **5/5**
- **C2 PAT CAGR (2yr)** = (39.16/13.60)^(1/2) − 1 = **69.7%** (≥20%) → **5/5**
- **C3 Positive YoY revenue years** = 2 of 2 periods = 100% → **5/5**
- **C4 PAT CAGR − Revenue CAGR** = 69.7% − 66.3% = **+3.4pp** (≥+3pp) → **5/5**

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 20/20 ✓ STRONGEST BLOCK (tied)

Basis: latest = FY2026 standalone audited (results 28-Apr-2026 p.3).

| Metric | FY2026 |
|---|---|
| Total borrowings (ST Rs 0.49 Cr + LT Rs 0) | Rs 0.49 Cr |
| Cash & cash equivalents | Rs 8.65 Cr |
| Net Debt | **Rs (8.16) Cr — net cash** |
| EBITDA (EBIT + Dep&Amort, P&L basis) | Rs 61.83 Cr |
| Interest (Finance Costs) | Rs 0.68 Cr |
| Total Equity (incl. Rs 20.32 Cr money received against share warrants) | Rs 227.86 Cr |
| Current Assets / Current Liabilities | Rs 307.09 Cr / Rs 117.63 Cr |

- **D1 Net Debt/EBITDA**: net cash position → **5/5**
- **D2 Interest Coverage** = 54.70/0.68 = **80.6x** (≥10x) → **5/5**
- **D3 Debt/Equity** = 0.49/227.86 = **0.002x** (<0.1) → **5/5**
- **D4 Current Ratio** = 307.09/117.63 = **2.61x** (≥2.0) → **5/5**

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 8/20

| Metric | Value | Source |
|---|---|---|
| Promoter holding, 31-Mar-2025 (10 named promoter-group entities) | 60.33+5.84+4.96+0.00+0.03+0.00+0.01+0.01+0.17+0.00 = **71.35%** | AR2025 p.131 (consol Note 1(iv)) / p.97 (standalone) |
| Promoter holding, 31-Mar-2024 (2 names only, pre-IPO) | 81.99+7.95 = **89.94%** | AR2025 p.98 |
| Promoter pledge | **NOT FOUND (not in provided data)** | — |
| Contingent liabilities, 31-Mar-2025 | Rs 20.91 Cr (TDS 0.13 + Income Tax 790.81 + GST 1,300.00 lakh) | AR2025 p.96 Note 30 |
| Net worth, 31-Mar-2025 | Rs 155.09 Cr | AR2025 p.88 |

- **E1 Promoter holding (latest available = 31-Mar-2025)** = 71.35% (≥60%) → **5/5**.
  Caveat: no FY26 shareholding pattern was provided; a Sept-2025 preferential
  warrant issue (13,89,388 warrants) partially converted (1,95,352 shares) by
  31-Mar-2026, so current promoter % is **NOT FOUND** and may differ.
- **E2 Promoter holding change** = 71.35% − 89.94% = **−18.59pp** (decreased >3%) → **0/5**.
  This is the IPO-driven creation of public float (June-2024 IPO issued 54,04,800
  new shares) plus first-time formal disclosure of 8 additional promoter-group
  members in FY25 — not promoter divestment in the secondary market. Only a
  1-year change is available; a true 3-year like-for-like trend is NOT FOUND
  (company listed 4-Jun-2024, less than 2 years old).
- **E3 Promoter pledge**: data not in any provided document → **0/5 (NOT FOUND)**.
- **E4 Contingent liabilities ÷ Net Worth** = 20.91/155.09 = **13.48%** (band 5-15%) → **3/5**.

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 10/60

| Test | Score | Basis |
|---|---|---|
| M1 Pricing Power | **1** | EBITDA margin FY24 26.22% → FY25 23.38% → FY26 24.05%; declined 2.17pp despite 66.3% revenue CAGR → "declined 2-5pp despite growth" tier (computed from standalone P&L, AR2025/results 28-Apr-2026) |
| M2 Cost Advantage vs peers | **0** | PEER DATA NEEDED |
| M3 Capital Efficiency | **5** | FAT (Revenue/Net PPE) FY26 = 257.13/29.13 = 8.83x (>3x) AND ROCE FY26 24.0% (>20%) |
| M4 Customer Stickiness | **3** | Zero revenue-decline years, but receivable days swung 65→199→167 days (not stable ±10) — scored at the "≤1 decline year" tier given unbroken growth |
| M5 Scale & Dominance | **0** | PEER DATA NEEDED (no segment mcap/margin ranking available) |
| M6 Technology/R&D | **0** | R&D/Revenue not disclosed as a line item — NOT FOUND / PEER DATA NEEDED |
| M7 Regulatory/License | **0** | EMS/PCB contract manufacturing is unregulated (no license barrier) |
| M8 Distribution | **1** | "500+ Customers Satisfied Globally" mentioned (AR2025 p.4) but unquantified reach growth / no revenue-per-customer trend |
| M9 Brand | **0** | GM proxy [(Revenue−(Material Cost+Change in Inventories))/Revenue] = FY24 38.2%, FY25 27.2%, FY26 28.3% (computed, AR2025/results 28-Apr-2026) — no peer median available → PEER DATA NEEDED |
| M10 Switching Costs | **0** | Revenue grew every year, but receivable days rose 65→167 days (+101 days), far beyond the ≤10-day tolerance for full credit |
| M11 Network Effects | **0** | Only 3 years available vs 6 required for the two-window test; scored conservatively — selling-expense trend for FY26 not disclosed at required granularity |
| M12 Negative WC/Float | **0** | WC days 183/172/220 — always >45 days, never negative |

**Moats present (score ≥3): 2 (M3, M4) → Moat classification: MODERATE**

Moat profile: `[M1:█░░░░][M2:░░░░░][M3:█████][M4:███░░][M5:░░░░░][M6:░░░░░][M7:░░░░░][M8:█░░░░][M9:░░░░░][M10:░░░░░][M11:░░░░░][M12:░░░░░]`

---

## SCORE SUMMARY

| Block | Score | /Max |
|---|---|---|
| A — Return on Capital | 14 | 20 |
| B — Cash Generation Quality | 0 | 20 |
| C — Growth | 20 | 20 |
| D — Balance Sheet Strength | 20 | 20 |
| E — Shareholder Alignment | 8 | 20 |
| **Core Score** | **62** | **100** |
| F — Moat Scoring | 10 | 60 |
| **Grand Total** | **72** | **160** |

**Strongest blocks:** C (Growth) and D (Balance Sheet Strength), both 20/20.
**Weakest block:** B (Cash Generation Quality), 0/20.

---

## CLASSIFICATION

**Data confidence:** 3 years exactly → **LIMITED band → downgrade classification one tier.**

**Baseline (matrix):** Core 62 (60-79 band) + Moat MODERATE (not STRONG/FORTRESS)
→ **GOOD**.

**Deal-breaker overrides applied:**
- #2 Block A/B check: Block B = 0 (<8) → caps at max GOOD (non-binding, already GOOD)
- **#4 Cumulative CFO/PAT = −0.13x (<0.50) → caps at max AVERAGE (binding).**
  Driven by FY25 and FY26 (both standalone; see Block B). No other deal-breaker
  triggers (median ROCE 24.0% ≫10%; revenue grew every year; PAT positive all 3
  years; pledge unconfirmed rather than confirmed >15%; ND/EBITDA is net cash).

Post deal-breaker: **AVERAGE.**

**History downgrade applied:** 3-year LIMITED band → one tier down from AVERAGE
→ **AVOID.**

## ┌─────────────────────────────────┐
## │  GATE 0 CLASSIFICATION: AVOID    │
## └─────────────────────────────────┘

**Decision line:** Mechanical Gate-0 output is AVOID, driven entirely by two
compounding structural factors rather than an operating problem: (1) deal-breaker
#4 — cumulative operating cash conversion is negative (−0.13x CFO/PAT) because
FY25-FY26 receivables and inventory grew faster than revenue during post-IPO
capacity scale-up, funded by IPO (Jun-2024, Rs 87 Cr) and preferential-warrant
(Sep-2025, Rs 94.6 Cr) proceeds rather than by operations; and (2) the 3-year
LIMITED-history downgrade, mechanical for any company listed under 2 years
(IPO 4-Jun-2024). Set against this: revenue and PAT both compounded above 65%
FY24-FY26, ROCE stayed in the 20-31% zone every year, the balance sheet is
net-cash with 2.6x current ratio and near-zero leverage, and promoter holding
(71.35% as of the last verified date) is well above the alignment floor. This is
the CLAUDE.md-anticipated "documented post-IPO rebase" scenario flagged for
downstream position-sizing review — Gate 0 does not itself override the
mechanical classification. No STOP verdict applies; this classification and its
flags propagate to downstream stages.

---

## FLAGS

**FLAG-GATE0** — Classification AVOID is driven by deal-breaker #4 (cumulative
CFO/PAT −0.13x, standalone FY24-FY26) plus the mandatory LIMITED 3-year-history
downgrade; core+moat scoring alone (Core 62, Moat MODERATE) would read GOOD.
Underlying growth (Revenue/PAT CAGR both >65%) and balance sheet (net cash,
2.6x current ratio) are strong; the cash-conversion shortfall is working-capital
driven during a funded scale-up, not a profitability problem.

**FLAG-CASH** — Block B = 0/20. Cumulative CFO/PAT = −0.13x FY24-FY26 (standalone);
FCF negative in FY25 (−Rs 30.65 Cr) and FY26 (−Rs 3.89 Cr); WC days rose from
183.5 to 220.0 (+36.6 days) FY24→FY26, driven by trade receivables growing from
Rs 16.68 Cr to Rs 117.42 Cr and inventory from Rs 35.74 Cr to Rs 80.28 Cr
(standalone). block_b_trend = deteriorating.

**FLAG-DATA-QUALITY** — screener-Data_Sheet.csv FY26 P&L figures (Sales
Rs 301.16 Cr; implied Total Expenses Rs 370.71 Cr exceed Sales) are internally
inconsistent and conflict with the audited standalone FY26 filing (Revenue
Rs 257.13 Cr, results 28-Apr-2026 p.2). This scorecard uses the audited
standalone figures throughout for FY24-FY26; downstream stages should do the
same and not rely on screener-Data_Sheet FY26 P&L line items.

**FLAG-OWNERSHIP-GAP** — Promoter holding (E1/E2) is anchored to AR2025
(31-Mar-2025, 71.35%); no FY26-quarter shareholding pattern was provided.
Sept-2025 preferential warrants (13,89,388 units) partially converted
(1,95,352 shares) by 31-Mar-2026 (results 28-Apr-2026 p.2, Note 4); current
promoter % post-dilution is NOT FOUND. Promoter pledge % is NOT FOUND in any
provided document (E3 scored 0). No credit rating was provided (per
INPUT_GAPS); D-block used computed ratios only.

---

## SECTOR NOTE

The manifest's `sector_cap_row` of "Pharma / CDMO" is a collector mis-pick per
task instructions. Aimtron is an Electronics System Design and Manufacturing
(ESDM) / EMS-PCB contract manufacturer (AR2025 p.4-5: two ISO-certified
facilities, Bengaluru and Vadodara; Wholly Owned Subsidiary Aimtron Electronics
LLC, Texas, incorporated Aug-2024). This mislabel has not been used anywhere in
the scoring above; M2/M5/M6/M9 peer-dependent tests are scored 0/PEER DATA
NEEDED rather than borrowed from an unrelated sector.

---

```yaml
stage: B01-gate0
company: "AIMTRON"
run_date: "2026-07-12"
model: claude-sonnet-5
status: complete
input_gaps:
  - "credit rating: NOT FOUND (no rating PDF provided)"
  - "promoter pledge %: NOT FOUND in any provided document"
  - "latest-quarter shareholding pattern: NOT FOUND; used AR2025 (31-Mar-2025) as latest verified anchor"
  - "R&D expense / revenue: NOT FOUND"
  - "peer data for M2, M5, M6, M9: NOT FOUND"
  - "sector_cap_row 'Pharma / CDMO' is a manifest mis-pick; company is EMS/ESDM electronics manufacturing, not used in scoring"
flags:
  - {type: FLAG-GATE0, reason: "Classification AVOID driven by deal-breaker #4 (cumulative CFO/PAT -0.13x, FY24-FY26 standalone) plus mandatory LIMITED 3-year-history downgrade; core+moat alone (Core 62, Moat MODERATE) reads GOOD. Growth (Rev/PAT CAGR both >65%) and balance sheet (net cash, current ratio 2.6x) are strong; shortfall is working-capital driven during funded post-IPO scale-up, not a profitability problem."}
  - {type: FLAG-CASH, reason: "Block B = 0/20. Cumulative CFO/PAT = -0.13x FY24-FY26. FCF negative FY25 (-Rs 30.65 Cr) and FY26 (-Rs 3.89 Cr). WC days rose 183.5 to 220.0 (+36.6 days) FY24-FY26 on receivables Rs16.68cr->Rs117.42cr and inventory Rs35.74cr->Rs80.28cr."}
  - {type: FLAG-DATA-QUALITY, reason: "screener-Data_Sheet FY26 P&L (Sales Rs301.16cr, implied expenses Rs370.71cr) is internally inconsistent and conflicts with audited standalone FY26 (Revenue Rs257.13cr, results 28-Apr-2026). Scorecard uses audited standalone figures throughout; downstream stages should do the same."}
  - {type: FLAG-OWNERSHIP-GAP, reason: "Promoter holding anchored to AR2025 (31-Mar-2025, 71.35%); no FY26 shareholding pattern provided. Sep-2025 warrants (13,89,388 units) partially converted (1,95,352 shares) by 31-Mar-2026; current promoter % NOT FOUND. Pledge % NOT FOUND, E3 scored 0."}
data_years: 3
fy_range: "FY2024 to FY2026"
blocks: {A: 14, B: 0, C: 20, D: 20, E: 8}
core_score: 62
moat_score: 10
grand_total: 72
moats_confirmed: 2
moat_class: "MODERATE"
classification: "AVOID"
deal_breakers:
  - "#2 Block B <8 -> max GOOD (Block B = 0/20, non-binding, already GOOD before #4)"
  - "#4 cumulative CFO/PAT <0.50 -> max AVERAGE (ratio = -0.13x, FY24-FY26 standalone; FY25 and FY26 drive it)"
history_downgrade: true
data_notes:
  - "screener-Data_Sheet FY26 P&L figures internally inconsistent (implied expenses exceed sales); audited standalone figures (AR2025 + results 28-Apr-2026) used throughout instead for FY24-FY26"
  - "EBIT = PBT + Finance Costs; EBITDA = EBIT + Depreciation&Amortisation (P&L basis, not CF-statement D&A, which differs slightly in FY26: P&L Rs712.36 lakh vs CF Rs616.29 lakh, unreconciled minor gap in the source filing)"
  - "ROCE and ROE computed (screener's own ROCE/ROE rows are blank for this company)"
  - "GM proxy for M9 = (Revenue - [Cost of Material Consumed + Change in Inventories]) / Revenue: FY24 38.2%, FY25 27.2%, FY26 28.3% (computed); no peer median available"
  - "FY24 promoter % (89.94%, 2 names) is pre-IPO (year-end 31-Mar-2024, IPO was 4-Jun-2024); FY25 (71.35%, 10 names) is first post-listing figure. E2 change reflects IPO float creation and first-time full promoter-group disclosure, not secondary-market divestment; true 3-year like-for-like trend NOT FOUND (company listed <2 years)"
  - "FY26 net worth of Rs227.86cr includes Rs20.32cr 'money received against share warrants' (25% upfront on Sep-2025 preferential issue, per company's own equity-section presentation); excluding it, FY26 net worth = Rs207.54cr and ROE = 21.6% (same scoring band, A3 unaffected)"
  - "M11 Network Effects scored conservatively at 0: only 3 years available vs the 6 years the test specifies"
  - "No prior-run comparison performed: first run for this ticker (COMPANY MEMORY = none)"
block_b_trend: "deteriorating - cumulative CFO/PAT = -0.13x (FY24-FY26 standalone); FY25 CFO -Rs17.69cr against PAT +Rs25.74cr is the single number that shows it"
```
