# GATE 0 SCORECARD — Birla Cable Ltd (BIRLACABLE)
Run date: 2026-08-20 | Stage: B01-gate0 | Model: claude-sonnet-5

Data available: 4 years (FY2023 to FY2026). Scoring adapted to 4-year history.
Note: full P&L/PAT/revenue history spans FY23-FY26 (screener-data, Data_Sheet.csv).
Two metric-level sub-gaps inside this window are called out explicitly where they
occur: (a) Current Liabilities are only broken out in the AR's two-year comparative
(FY25, FY26), so formula-accurate ROCE could be computed for only those two years;
(b) capex (Purchase of PPE + intangibles) and Trade Payables are likewise only
disclosed in the AR's FY25/FY26 comparative columns, so FCF and full Working
Capital Days (with a payables leg) could be computed for only those two years.
FY23/FY24 values for these specific sub-metrics are marked N/A (not in provided
data); no substitute or estimate was used. ROE, revenue, PAT, and CFO/PAT are
computed on the full FY23-FY26 window since their inputs are complete.

Screener P&L/Balance Sheet/Cash Flow/Quarters CSVs were label-only (collector
defect, confirmed empty on inspection) and were not used as a data source; all
figures below come from screener-Data_Sheet.csv, the FY25-26 Annual Report, and
the CARE rating rationale (2026-04-01).

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 5/20

Capital Employed = Total Assets − Current Liabilities. Current Liabilities are
disclosed only for FY25/FY26 in the AR's two-year comparative balance sheet
(consolidated). FY23/FY24 Capital Employed is N/A (not in provided data); no
approximation was substituted.

| Year | EBIT (cr) | Capital Employed (cr) | ROCE |
|---|---|---|---|
| FY23 | 52.53 (computed: EBITDA 63.16 − Dep 10.63, screener-data) | N/A (not in provided data) | N/A |
| FY24 | 29.67 (computed: EBITDA 40.46 − Dep 10.79, screener-data) | N/A (not in provided data) | N/A |
| FY25 | 16.93 (computed: EBITDA 32.69 − Dep 15.76, screener-data) | 304.23 (computed: Total Assets 416.06 − Current Liab. 111.83, AR consolidated BS p.125) | 5.56% (computed) |
| FY26 | 31.18 (computed: EBITDA 46.97 − Dep 15.79, screener-data) | 326.86 (computed: Total Assets 464.45 − Current Liab. 137.59, AR consolidated BS p.125) | 9.54% (computed) |

EBITDA was derived as Sales − (Raw Material + Power&Fuel + Other Mfr. Exp +
Employee Cost + Selling&Admin + Other Expenses) + Change in Inventory
(screener-data); cross-checked against reported PBT for all four years — exact
match in each year, confirming the sign convention used.

A1 Median ROCE (2-yr subset, FY25/FY26): (5.56+9.54)/2 = **7.55%** → <10% = **0**
A2 Minimum single-year ROCE: **5.56%** (FY25) → <8% = **0**
A3 Median ROE (full 4-yr): see table below → **7.78%** → <12% = **0**
A4 ROCE trend, latest (FY26 9.54%) vs earliest available (FY25 5.56%): latest ≥
   earliest → **5** (flag: this is a 1-year window, not FY23→FY26, because
   FY23/FY24 ROCE is not computable from provided data)

ROE table (PAT ÷ average Net Worth; FY23 uses closing Net Worth only, no FY22
opening figure in provided data, stated per formula rule):
| Year | PAT (cr) | Avg Net Worth (cr) | ROE |
|---|---|---|---|
| FY23 | 32.94 (screener-data) | 229.42 (closing only, screener-data) | 14.36% |
| FY24 | 22.14 (screener-data) | 240.21 = (229.42+251.00)/2 (screener-data) | 9.22% |
| FY25 | 4.89 (screener-data) | 252.13 = (251.00+253.25)/2 (screener-data) | 1.94% |
| FY26 | 16.90 (screener-data) | 267.08 = (253.25+280.90)/2 (screener-data) | 6.33% |
Median of {1.94, 6.33, 9.22, 14.36} = **7.78%**

**Block A = A1(0)+A2(0)+A3(0)+A4(5) = 5/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 13/20

CFO and PAT are available for all 4 years (screener-data). Capex (Purchase of
PPE + Intangibles) is disclosed only in the AR's FY25/FY26 comparative cash
flow statement (consolidated); FY23/FY24 capex is N/A (not in provided data;
the screener CF CSV is the known label-only defect and does not fill this).

| Year | CFO (cr) | Capex (cr) | FCF (cr) |
|---|---|---|---|
| FY23 | -7.84 (screener-data) | N/A (not in provided data) | N/A |
| FY24 | 15.82 (screener-data) | N/A (not in provided data) | N/A |
| FY25 | 112.26 (screener-data) | 27.60 = 27.5495 PPE + 0.049 Intangibles (AR consolidated CF p.127) | 84.66 |
| FY26 | -20.71 (screener-data) | 2.71 = 2.7092 PPE + 0 Intangibles (AR consolidated CF p.127) | -23.42 |

B1 Cumulative CFO ÷ Cumulative PAT (full 4-yr): CFO sum = -7.84+15.82+112.26-20.71
   = 99.53; PAT sum = 32.94+22.14+4.89+16.90 = 76.87; ratio = **1.295** → ≥1.00 = **5**
B2 FCF-positive years as proportion (2-yr subset only, FY23/FY24 not
   assessable): FY25 positive, FY26 negative = 1 of 2 = **50%** → 50-74% = **2**
   (flag: computed on half the available history)
B3 Cumulative FCF ÷ Cumulative PAT (2-yr subset): FCF sum = 84.66-23.42=61.24;
   PAT sum (FY25+FY26) = 21.79; ratio = **2.81** → ≥0.60 = **5** (flag: excludes
   FY23/FY24, whose CFO was weak/negative — this ratio likely overstates true
   4-year cash conversion)
B4 Change in WC Days, latest vs earliest available (FY25→FY26 only; FY23/FY24
   Trade Payables not in provided data): FY25 = 104.20 days, FY26 = 118.90 days,
   increase of **14.70 days** → increased 5-15 = **1**

WC Days detail (Receivable Days + Inventory Days − Payable Days, revenue basis;
no explicit single COGS line was available, so revenue basis used throughout,
per formula rule):
| Year | Receivables (cr) | Inventory (cr) | Payables (cr) | Revenue (cr) | Rec.Days | Inv.Days | Pay.Days | WC Days |
|---|---|---|---|---|---|---|---|---|
| FY25 | 167.22 (screener-data) | 51.19 (screener-data) | 29.51=2950.63 lakh (AR consol. Note 22, p.140) | 661.65 (screener-data) | 92.24 | 28.24 | 16.28 | 104.20 |
| FY26 | 202.97 (screener-data) | 78.97 (screener-data) | 30.73=3073.16 lakh (AR consol. Note 22, p.140) | 771.11 (screener-data) | 96.07 | 37.38 | 14.55 | 118.90 |

Cross-reference (not used for scoring, different basis/entity level): CARE
rating rationale states BCL (standalone) operating cycle 134 days FY24 → 125
days FY25, with receivable/inventory/payable days of 113/51/30 (FY24) and
104/37/16 (FY25) (rating p.5-6). Directionally consistent with FY25 figure
computed here; FY24 standalone figure not mixed into the consolidated
FY25/FY26 WC Days series above to avoid basis inconsistency.

**Block B = B1(5)+B2(2)+B3(5)+B4(1) = 13/20**

block_b_trend: **deteriorating** — FCF swung from +₹84.66cr (FY25) to
-₹23.42cr (FY26); WC days rose 104.2 → 118.9 (+14.7 days) over the same period.

---

## BLOCK C: GROWTH (Max 20) — Score: 0/20

Revenue (cr, screener-data): FY23 792.20 | FY24 685.50 | FY25 661.65 | FY26 771.11
PAT (cr, screener-data): FY23 32.94 | FY24 22.14 | FY25 4.89 | FY26 16.90

C1 Revenue CAGR (FY23→FY26, 3yr): (771.11/792.20)^(1/3)-1 = **-0.89%** (computed)
   → <5% = **0**
C2 PAT CAGR (FY23→FY26, 3yr): (16.90/32.94)^(1/3)-1 = **-19.94%** (computed) →
   negative = **0**
C3 Positive YoY revenue years: FY24 vs FY23 decline (-13.47%), FY25 vs FY24
   decline (-3.48%), FY26 vs FY25 increase (+16.55%) → 1 of 3 = **33.3%** →
   <50% = **0**
C4 PAT CAGR minus Revenue CAGR: -19.94 - (-0.89) = **-19.05pp** → <-8pp = **0**

Note: neither CAGR endpoint is negative or zero in either case, so both are
valid CAGRs (not N/M); the business genuinely contracted over FY23-FY26.

**Block C = C1(0)+C2(0)+C3(0)+C4(0) = 0/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 11/20

Latest year = FY26 throughout.

D1 Net Debt ÷ EBITDA: Net Debt = Borrowings 132.57 − Cash&Bank 3.63 = 128.94
   (screener-data); EBITDA = 46.97 (computed, see Block A note); ratio =
   **2.74x** → 2-3x = **1**
D2 Interest Coverage (EBIT ÷ Interest): EBIT 31.18 ÷ Interest 12.34
   (screener-data) = **2.53x** → 1.5-2.9x = **1**
D3 Debt ÷ Equity: Borrowings 132.57 ÷ Net Worth 280.90 (screener-data) =
   **0.47x** → 0.1-0.5x = **4**
D4 Current Ratio: Total Current Assets 301.53 (30153.44 lakh, AR consolidated
   BS p.125) ÷ Total Current Liabilities 137.59 (13758.93 lakh, AR consolidated
   BS p.125) = **2.19x** → ≥2.0 = **5**

Cross-reference (not used for scoring, standalone basis): CARE reports BCL
TD/PBILDT 3.19x FY25 (PY 3.78x FY24) and interest coverage 2.62x FY25 (PY
2.94x FY24) — standalone, PBILDT-basis, broadly consistent direction with the
consolidated EBITDA-basis figures computed here (rating p.6).

**Block D = D1(1)+D2(1)+D3(4)+D4(5) = 11/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 10/20

Input gap carried from B00: a dedicated shareholding-pattern filing was not
provided. The only promoter-holding figure available is in the AR's
"Category of Shareholders" table.

E1 Promoter holding (latest available): **66.35%** (19,905,743 of 30,000,000
   shares; AR p.61, "Category of Shareholders" table). Note: this table is
   labelled "as on March 31, 2025" in the source text but appears immediately
   after the FY26 (31 Mar 2026) distribution-of-shareholding table and uses
   the FY26 total share count; date label is ambiguous / possibly a drafting
   carryover in the source document. Treated as the latest available figure.
   → ≥60% = **5**
E2 Promoter holding change over 3 years: **N/A (not in provided data)**. The
   AR's individual promoter-holding table (p.96, Note (d)) shows "% Change
   During the year" = Nil for each listed promoter entity, but this is a
   1-year (FY26) figure, not the required 3-year window → **0**
E3 Promoter pledge (latest): **N/A (not in provided data)**. No promoter
   share-pledge disclosure was found anywhere in the AR text (searched
   case-insensitive for "pledg*" — only hits were inventory/receivables
   pledged as loan security and a subsidiary-securities pledge note, both
   unrelated to promoter shareholding). Not assumed zero → **0**
E4 Contingent Liabilities ÷ Net Worth: Contingent Liabilities (consolidated,
   Note 36) = ₹20.85 lakh = 0.2085 cr, "claims against the Holding Company not
   acknowledged as debts" (AR p.144) ÷ Net Worth 280.90 (screener-data) =
   **0.07%** → <5% = **5**

**Block E = E1(5)+E2(0)+E3(0)+E4(5) = 10/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 0/60

| Test | Score | Basis |
|---|---|---|
| M1 Pricing Power | 0 | EBITDA margin FY23 7.97% → FY26 6.09% (declined, not expanded); revenue CAGR negative. Neither qualifying condition met. (computed, screener-data) |
| M2 Cost Advantage vs peer | 0 | **PEER DATA NEEDED** — no peer/sector comparison data provided |
| M3 Capital Efficiency | 0 | FAT (FY26) = Revenue 771.11 ÷ Net Block 109.99 = 7.01x; ROCE FY26 9.54%. FAT>1x but ROCE not >12% — no band met (computed) |
| M4 Customer Stickiness | 0 | 2 revenue-decline years (FY24, FY25) but revenue CAGR negative, not positive, so does not meet the "2 decline years, CAGR positive = 1" band; scored 0 as closest fit |
| M5 Scale & Dominance | 0 | **PEER DATA NEEDED** — no peer mcap/margin ranking data provided |
| M6 Technology / R&D | 0 | No R&D expenditure line disclosed in any provided source; not applicable to this manufacturer's disclosed P&L |
| M7 Regulatory / License | 0 | Not a license-restricted segment; CARE explicitly describes the cable/EPC industry as "highly fragmented with numerous organised and unorganised players" (rating p.5) — treated as unregulated |
| M8 Distribution | 0 | No distribution-network reach/outlet data disclosed; sales model is direct/institutional (telecom operators, PSUs), not a quantified distribution network |
| M9 Brand | 0 | **PEER DATA NEEDED** — gross-margin proxy computable ((Revenue−Material Cost)/Revenue ≈ 17.7% FY26, 19.9% FY25) but no peer median to compare against |
| M10 Switching Costs | 0 | Revenue did not grow every year (declined FY24, FY25) and overall FY23-FY26 trajectory is a CAGR decline, not growth — below the lowest explicit positive band |
| M11 Network Effects | 0 | Only 4 years of history available; two-window test requires ≥6 years. Scored conservatively per instruction, given negative overall revenue trend |
| M12 Negative WC / Float | 0 | WC Days 104.2 (FY25) and 118.9 (FY26), both >45 days in the only years assessable |

**moats_confirmed (score ≥3) = 0. Moat classification = NONE**

Moat profile:
```
M1  [          ] 0/5
M2  [PEER DATA NEEDED]
M3  [          ] 0/5
M4  [          ] 0/5
M5  [PEER DATA NEEDED]
M6  [          ] 0/5
M7  [          ] 0/5
M8  [          ] 0/5
M9  [PEER DATA NEEDED]
M10 [          ] 0/5
M11 [          ] 0/5
M12 [          ] 0/5
```

---

## CLASSIFICATION

core_score = A(5) + B(13) + C(0) + D(11) + E(10) = **39/100**
moat_score = **0/60**
grand_total = **39**

Data confidence: 4 years of continuous P&L/BS/CF history → falls in the "3-4
LIMITED, downgrade classification one tier" band. **history_downgrade = true**

Base matrix: Core 39 (<40) → **AVOID**

Deal-breakers triggered (recorded; none can move the classification above the
matrix result since AVOID is already the floor of this scale):
1. **Block A < 8** (Block A = 5) → max GOOD. Driven by FY25/FY26 ROCE (only
   years computable) and full-history ROE, all sub-12% median.
2. **Median ROCE < 10%** (7.55%, FY25-FY26 subset) → max AVERAGE.
3. **Revenue declined in majority of years** (2 of 3 YoY transitions: FY24,
   FY25) → max AVERAGE.

Not triggered: Block B <8 (Block B=13); cumulative CFO/PAT <0.50 (1.295);
pledge >15% (not assessable, no data — not assumed); ND/EBITDA>3x AND IC<3x
(ND/EBITDA 2.74x, does not meet the >3x leg); PAT negative in any of last 3
years (FY24/FY25/FY26 all positive PAT); history <3 years (4 years available).

**Classification = AVOID** (matrix result, already at the floor; deal-breaker
caps are moot since none can improve on AVOID)

Strongest block: **Block B (Cash Generation), 13/20 (65%)** — driven by strong
cumulative CFO/PAT coverage (1.295x) across the full 4-year window.
Weakest block: **Block C (Growth), 0/20** — revenue and PAT both contracted
FY23-FY26, majority of years saw revenue decline.

**Decision line: AVOID. Core score 39/100 sits below the 40 floor on its own;
three deal-breakers (weak Block A, sub-10% median ROCE, majority-decline
revenue years) would each independently cap the name at GOOD or AVERAGE even
before the floor is applied. Zero of twelve moat tests scored ≥3 — no
quantitative moat evidence. Four-year data history is LIMITED and would
downgrade a stronger classification one tier if one had been reached.**

---

## MATERIAL CONTEXT (not scored, flagged for downstream stages)

The company's Board approved amalgamation of Birla Cable Ltd into its parent,
Vindhya Telelinks Limited (VTL), announced 21-March-2026. Shareholders of BCL
will receive 10 VTL shares for every 115 BCL shares held, no cash
consideration. Expected completion ~10-12 months from announcement, subject
to regulatory approval (CARE rating rationale, 2026-04-01, p.1-2). CARE has
placed BCL's ratings on "Rating Watch with Positive Implications" pending this
scheme. This is a structural event that may supersede standalone valuation
of BIRLACABLE before any entry decision is executed; downstream stages should
weigh this heavily.
