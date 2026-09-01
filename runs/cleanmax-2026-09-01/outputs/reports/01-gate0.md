# STAGE 1: GATE 0 SCORECARD — Clean Max Enviro Energy Solutions Ltd (CLEANMAX)
Run date: 2026-09-01 | Model: claude-sonnet-5 | Mode: pipeline (no confirmation stops)

Basis: CONSOLIDATED figures throughout. Standalone accounts are NOT used anywhere in
this scorecard (standalone Sales Rs 6,003 Cr FY26 vs consolidated Rs 1,912.87 Cr —
the gap is the parent selling projects to its own SPVs; flagged, not scored).

Data available: 6 years (FY21 to FY26) for revenue/PAT/cash flow lines (screener
Data_Sheet, cross-checked to consolidated audited results and the RHP restated
financials). Full balance-sheet detail (current liabilities split, needed for ROCE
capital employed and for Payable Days) is available for only 4 years (FY23 to FY26),
sourced from the RHP restated consolidated Statement of Assets and Liabilities
(FY23-FY25) and the Q4 FY26 audited consolidated balance sheet (FY25-FY26). FY21-FY22
current-liability and payables detail is NOT FOUND in the provided corpus (pre-RHP,
pre-listing years, no restated BS granularity available). Scoring adapted: 6-year
history for Blocks A4 (partial)/C, 4-year history for Blocks A (ROCE), B (FCF, WC
days), D (latest year only).

Company listed 2 March 2026 (NSE/BSE, formerly Clean Max Enviro Energy Solutions
Private Limited). FY21-FY22 figures are pre-listing/pre-restatement; FY23-FY26 are
RHP-restated / audited-consolidated. Cross-checks below show revenue and CFO lines
tie out across Data_Sheet, RHP, and the Q4 FY26 results to within rounding — treated
as reliable.

---

## SOURCE ANCHOR KEY
- (Data_Sheet) = BASE/inputs/screening/screener-Data_Sheet.csv (consolidated, per
  cross-check against RHP and results — see notes)
- (RHP p.N) = BASE/inputs/prospectus/RHP_Prospectus_2026-02-25.txt, PDF page N
- (AR p.N) = BASE/inputs/annual-report/...0da3293c....txt, PDF page N
- (Q4FY26 results p.N) = BASE/inputs/results/abfeff84-...txt, PDF page N
- (Q1FY27 results p.N) = BASE/inputs/results/666b6d73-...txt, PDF page N

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

EBIT computed as PBT + Interest (screener/Data_Sheet does not populate its own ROCE
row — Balance_Sheet.csv was exported blank — so this is COMPUTED, not sourced).
Capital Employed = Total Assets − Total Current Liabilities, available FY23-FY26 only.

| FY | PBT (Data_Sheet) | Interest (Data_Sheet) | EBIT | Total Assets | Current Liab. | Cap. Employed | ROCE |
|----|----|----|----|----|----|----|----|
| FY23 | -18.11 | 217.22 | 199.11 | 7,000.14 (RHP p.107) | 1,629.26 (RHP p.108) | 5,370.88 | 3.71% |
| FY24 | 4.89 | 504.38 | 509.27 | 9,076.55 (RHP p.107) | 1,285.44 (RHP p.108) | 7,791.11 | 6.54% |
| FY25 | 52.20 | 662.89 | 715.09 | 13,279.25 (Q4FY26 results p.16) | 2,450.57 (Q4FY26 results p.16) | 10,828.68 | 6.60% |
| FY26 | 134.98 | 785.92 | 920.90 | 23,098.28 (Q4FY26 results p.16) | 5,129.21 (Q4FY26 results p.16) | 17,969.07 | 5.13% |

(PBT and Interest lines: screener-Data_Sheet, Rs Cr, all years)

**A1 Median ROCE (4 yrs) = 5.83%** → <10% → **score 0**
**A2 Minimum single-year ROCE = 3.71% (FY23)** → <8% → **score 0**
**A3 Median ROE = 1.94%** → <12% → **score 0**
(ROE = PAT ÷ average Net Worth; Net Worth = Reserves + Equity Share Capital,
Data_Sheet, ties to RHP/results "Total equity attributable to owners" every year
checked)
| FY | PAT (owners, Data_Sheet) | NW opening | NW closing | Avg NW | ROE |
|----|----|----|----|----|----|
| FY21 | 25.32 | N/A (opening unavailable — used closing) | 50.36 | 50.36 | 50.28% |
| FY22 | 30.36 | 50.36 | 1,260.64 | 655.50 | 4.63% |
| FY23 | -65.27 | 1,260.64 | 1,210.75 | 1,235.70 | -5.28% |
| FY24 | -30.99 | 1,210.75 | 1,833.47 | 1,522.11 | -2.04% |
| FY25 | 27.84 | 1,833.47 | 2,563.48 | 2,198.48 | 1.27% |
| FY26 | 94.13 | 2,563.48 | 4,638.27 | 3,600.88 | 2.61% |
Note: FY22 NW jumps 25x (Rs 50.36 Cr → Rs 1,260.64 Cr) on a large pre-IPO equity
infusion, mechanically depressing FY22 ROE via the averaging denominator. Data note,
not an estimate — both endpoints are sourced.

**A4 ROCE trend, latest (FY26, 5.13%) vs earliest available (FY23, 3.71%)**: latest ≥
earliest → **score 5**

**BLOCK A TOTAL = 0+0+0+5 = 5 / 20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

CFO from Data_Sheet, cross-checked exactly to RHP restated cash flow (FY23-25) and
Q4FY26 results (FY26). Capex = "Capital expenditure on PPE, CWIP, intangible assets
and capital advances" line from the consolidated cash flow statement (excludes
acquisitions, per formula) — available FY23-FY26 only (RHP p.111-112 restated CF;
Q4FY26 results p.17-18 audited CF). FY21-FY22 capex breakdown NOT FOUND (only the
netted "Cash from Investing Activity" total is in Data_Sheet, which is not usable
for a formula-compliant FCF).

| FY | CFO | Capex | FCF | PAT (owners) |
|----|----|----|----|----|
| FY23 | 927.65 (Data_Sheet; ties RHP p.111 Rs 9,276.49 mn) | 2,845.59 (RHP p.111) | -1,917.94 | -65.27 |
| FY24 | 86.28 (Data_Sheet; ties RHP p.111 Rs 862.76 mn) | 1,866.13 (RHP p.111) | -1,779.86 | -30.99 |
| FY25 | 1,404.20 (Data_Sheet; ties RHP p.111 Rs 14,041.96 mn) | 2,910.62 (RHP p.111) | -1,506.42 | 27.84 |
| FY26 | 1,731.24 (Data_Sheet; ties Q4FY26 results p.17 Rs 17,312.37 mn) | 5,754.32 (Q4FY26 results p.17, PPE/CWIP/advances Rs 56,871.87 mn + intangibles Rs 671.31 mn) | -4,023.08 | 94.13 |

**B1 Cumulative CFO ÷ Cumulative PAT**: ΣCFO = 4,149.37; ΣPAT = 25.71 → ratio = 161.4x
→ mechanically ≥1.00 → **score 5, but flagged as a DISTORTED ratio** — the PAT base
is near-zero (FY23+FY24 losses almost exactly offset FY25+FY26 profits), so any small
CFO number divided by it inflates the ratio. Not treated as evidence of high cash
conversion quality; see analyst_note.

**B2 FCF-positive years**: 0 of 4 years (FY23-26) positive → 0% → **score 0**

**B3 Cumulative FCF ÷ Cumulative PAT**: ΣFCF = -9,227.30; ΣPAT = 25.71 → deeply
negative → **score 0**

**B4 Change in WC Days, latest (FY26) vs earliest available (FY23)**:
WC Days = Receivable Days + Inventory Days − Payable Days (Trade Receivables/Sales
basis; Trade Payables from RHP p.108 FY23-24, Q4FY26 results p.16 FY25-26 — not in
Data_Sheet, which does not carry a payables line)

| FY | Rec Days | Inv Days | Pay Days | WC Days |
|----|----|----|----|----|
| FY23 | 66.51 | 30.13 | 439.53 | -342.89 |
| FY24 | 66.12 | 10.49 | 207.00 | -130.39 |
| FY25 | 45.89 | 12.71 | 212.89 | -154.29 |
| FY26 | 53.03 | 7.62 | 334.00 | -273.35 |

WC days are deeply negative throughout (trade payables, largely equipment/EPC
creditors for projects under construction, dwarf receivables + inventory) — a
float-like feature, not a red flag by itself. But latest (-273.35) vs earliest
(-342.89) = **increase of 69.5 days** (WC days moved toward zero, i.e. worse) → >15
days increase → **score 0**

**BLOCK B TOTAL = 5+0+0+0 = 5 / 20**

**block_b_trend = deteriorating.** FCF widened from -Rs 1,780 Cr (FY24) to -Rs 4,023
Cr (FY26). This is GROWTH-CAPEX driven, not an operating breakdown: CFO itself grew
20x over the same window (Rs 86 Cr → Rs 1,731 Cr, Data_Sheet/results), while capex
grew 3.1x (Rs 1,866 Cr → Rs 5,754 Cr, RHP p.111 / Q4FY26 results p.17). Operating
cash generation is scaling; capex on new capacity is scaling faster. Borrowings rose
Rs 5,570 Cr (FY24) → Rs 12,684 Cr (FY26) (Data_Sheet) to fund this gap.

---

## BLOCK C: GROWTH (Max 20)

Revenue (Data_Sheet, Rs Cr, consolidated — ties to RHP p.109 and Q4FY26 results p.15
for every year checked): FY21 621.27, FY22 701.73, FY23 929.58, FY24 1,389.84, FY25
1,495.70, FY26 1,912.87

**C1 Revenue CAGR (FY21→FY26, 5 yrs) = (1,912.87/621.27)^(1/5)-1 = 25.21%** → ≥20% →
**score 5**

**C2 PAT CAGR**: PAT (owners, Data_Sheet) went 25.32 (FY21) → 30.36 (FY22) → -65.27
(FY23) → -30.99 (FY24) → 27.84 (FY25) → 94.13 (FY26). Both endpoints are positive,
but the series contains a **profit-to-loss swing (FY22→FY23) and a loss-to-profit
swing (FY24→FY25)** inside the window. Per the CAGR edge rule, no synthetic CAGR is
computed. **PAT CAGR = N/M (loss-to-profit swing, FY24 to FY25; also profit-to-loss,
FY22 to FY23)** → **score 0**

**C3 Positive YoY revenue years**: 5 of 5 YoY comparisons (FY22 through FY26) are
positive → 100% → **score 5**

**C4 PAT CAGR minus Revenue CAGR**: PAT CAGR is N/M → **score 0, per rule**

**BLOCK C TOTAL = 5+0+5+0 = 10 / 20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — latest = FY26

All figures FY26, consolidated (Q4FY26 results p.15-16, cross-checked to Data_Sheet).

- Borrowings (incl. lease liabilities): Rs 12,684.32 Cr (Data_Sheet; ties to Q4FY26
  results p.16: non-current borrowings 1,13,124.22 mn + current borrowings 10,983.42
  mn + lease liabilities 2,497.43+238.04 mn = 12,684.31 Cr)
- Cash & Bank: Rs 2,287.96 Cr (Data_Sheet; ties to Q4FY26 results p.16: cash &
  equivalents 12,019.60 mn + other bank balances 10,859.97 mn = 2,287.96 Cr)
- Net Debt = 12,684.32 − 2,287.96 = **Rs 10,396.36 Cr**
- EBITDA (company-reported, Q4FY26 results p.15, Line III "EBITDA (I-II)", FY26) =
  **Rs 1,294.56 Cr**. Note: this reported EBITDA line includes Other Income (Rs
  168.59 Cr, Data_Sheet) inside Total Income; the narrower operating-only figure
  (Sales − operating expenses, excl. Other Income) is Rs 1,132.22 Cr. Either basis
  gives the same scoring outcome below.
- Owners' equity: Rs 4,638.27 Cr (Data_Sheet Reserves+ESC; ties Q4FY26 results p.16
  "Total equity attributable to owners of the Company")
- Total Current Assets: Rs 3,405.12 Cr; Total Current Liabilities: Rs 5,129.21 Cr
  (Q4FY26 results p.16)
- Interest (Finance costs), FY26: Rs 785.92 Cr (Data_Sheet; ties Q4FY26 results p.15)
- EBIT (PBT+Interest), FY26: Rs 920.90 Cr (as computed in Block A)

**D1 Net Debt ÷ EBITDA = 10,396.36 / 1,294.56 = 8.03x** → >3x → **score 0**

**D2 Interest Coverage = EBIT ÷ Interest = 920.90 / 785.92 = 1.17x** → <1.5x →
**score 0**

**D3 Debt ÷ Equity = 12,684.32 / 4,638.27 = 2.73x** → >1.5 → **score 0**

**D4 Current Ratio = 3,405.12 / 5,129.21 = 0.66x** → <1.0 → **score 0**

**BLOCK D TOTAL = 0+0+0+0 = 0 / 20**

**DEAL-BREAKER #6 FIRES: ND/EBITDA (8.03x) > 3x AND Interest Coverage (1.17x) < 3x →
AVOID.** This is the dominant, mechanical override for this run (see
Classification below).

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

**E1 Promoter holding (latest available)**: Promoter and Promoter Group = **49.48%**
of total equity as at 31 March 2026 (AR p.351, Shareholding Pattern by Category —
this is the most recent disclosure in the provided corpus; no post-listing quarterly
SHP beyond FY26 year-end was in the corpus). 40-49.9% band → **score 3**

**E2 Promoter holding change over 3 years**: **NOT FOUND — score 0.** CLEANMAX listed
2 March 2026; three years ago the company was a private, PE-backed entity (RHP p.150
pre-Offer cap table shows Promoters+Group at 64.99% pre-Offer, 49.15% post-Offer on a
fully diluted IPO basis — but that drop is primary-issuance dilution from the IPO
itself, not a comparable "3-year public float trend" and not usable per the
never-estimate rule for a genuine like-for-like comparison).

**E3 Promoter pledge (latest)**: As at 31 March 2026, Kuldeep Jain + KEMPINC LLP had
pledged 11,597,866 equity shares in favour of 360 One Prime Limited (AR p.420, Note
19(g), pledge agreement dated 22 July 2025). Total Promoter+Group holding at that
date = 57,930,860 shares (AR p.351). **Pledge = 11,597,866 / 57,930,860 = 20.02% of
promoter holding.** Note: the RHP (p.150, filed 25 Feb 2026) stated these same shares
"had been released prior to filing of the Red Herring Prospectus" — but the AR (FY26
year-end, later and more authoritative) shows the pledge back in place as at 31 March
2026, i.e. re-pledged after the RHP was filed. >15% → **score 0**

**E4 Contingent Liabilities ÷ Net Worth**: AR Note 38, FY26 (AR p.441): Income tax
claims Rs 974.46 mn + GST claims Rs 984.58 mn + Bank guarantees Rs 10,369.51 mn =
Rs 12,328.55 mn = **Rs 1,232.86 Cr**. Net Worth (owners) = Rs 4,638.27 Cr. Ratio =
**26.58%**. 15-30% band → **score 1**

**BLOCK E TOTAL = 3+0+0+1 = 4 / 20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

OPM (= Operating Profit ÷ Sales, excl. Other Income, Data_Sheet-derived): FY21 38.6%,
FY22 42.1%, FY23 40.3%, FY24 50.8%, FY25 60.2%, FY26 59.2%

**M1 Pricing Power**: EBITDA/OPM margin expanded +20.6pp (38.6%→59.2%, FY21→FY26)
AND revenue CAGR 25.21% ≥10% → **score 5**

**M2 Cost Advantage vs peer median**: no peer EBITDA margin data in the provided
corpus → **score 0, PEER DATA NEEDED**

**M3 Capital Efficiency**: FAT (Sales ÷ Net Block) FY26 = 1,912.87/11,953.85 = 0.16x
(Data_Sheet); ROCE FY26 = 5.13%. FAT <1x and ROCE <12% → **score 0**. (Large CWIP —
Rs 5,342.77 Cr at FY26, ~31% of gross PP&E — not yet earning is the structural
reason; see analyst_note.)

**M4 Customer Stickiness**: 0 revenue-decline years (all 6) BUT receivable days
range 28.1-66.5 (>±10 band from a ~47-day midpoint) → does not clear the top tier;
0 decline years is strictly better than "max 1 decline, fully recovered" → **score
3**

**M5 Scale & Dominance**: no peer mcap/segment-share data in the provided corpus →
**score 0, PEER DATA NEEDED**

**M6 Technology/R&D**: no R&D line item disclosed in the provided corpus → **score
0, PEER DATA NEEDED**

**M7 Regulatory/License**: no sourced count of listed players in the C&I
open-access/rooftop renewable segment in the provided corpus → **score 0, PEER DATA
NEEDED**

**M8 Distribution**: no quantified reach/client-count series in the provided corpus
→ **score 0** (not scoreable from evidence provided)

**M9 Brand**: no peer gross-margin benchmark in the provided corpus → **score 0,
PEER DATA NEEDED**

**M10 Switching Costs**: revenue grew every year (0 declines) BUT receivable days
rose 24.96 days (FY21 28.07 → FY26 53.03), exceeding the ≤10-day threshold for either
qualifying tier → **score 0**

**M11 Network Effects** (6-year minimum met, two overlapping 3-yr windows used):
prior 3yr CAGR (FY21→FY24) = 30.81%; latest 3yr CAGR (FY23→FY26) = 27.21%. Latest is
NOT > prior → top tier fails. Latest 3yr CAGR ≥20% but Selling & Admin expense as %
of Sales rose FY21→FY26 (2.16%→3.85%, Data_Sheet) → "growth >15% but selling % rising"
→ **score 1**

**M12 Negative WC/Float**: WC Days negative in all 4 years with data (FY23-26; FY21-22
NOT FOUND, payables unavailable) → majority negative → **score 5**

**BLOCK F TOTAL = 5+0+0+3+0+0+0+0+0+0+1+5 = 14 / 60**

**Moats confirmed (score ≥3): M1 (Pricing Power), M4 (Customer Stickiness), M12
(Negative WC/Float) = 3** → **Moat classification: MODERATE (2-3 present)**

---

## SCOREBOARD

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 5 | 20 |
| B — Cash Generation Quality | 5 | 20 |
| C — Growth | 10 | 20 |
| D — Balance Sheet Strength | 0 | 20 |
| E — Shareholder Alignment | 4 | 20 |
| **Core Total (A-E)** | **24** | **100** |
| F — Moat Score (raw) | 14 | 60 |
| **Grand Total** | **38** | **160** |

Moat profile bars (present ≥3):
```
M1  [#####] 5  Pricing Power        PRESENT
M2  [     ] 0  Cost Advantage       PEER DATA NEEDED
M3  [     ] 0  Capital Efficiency
M4  [###  ] 3  Customer Stickiness  PRESENT
M5  [     ] 0  Scale & Dominance    PEER DATA NEEDED
M6  [     ] 0  Technology/R&D       PEER DATA NEEDED
M7  [     ] 0  Regulatory/License   PEER DATA NEEDED
M8  [     ] 0  Distribution
M9  [     ] 0  Brand                PEER DATA NEEDED
M10 [     ] 0  Switching Costs
M11 [#    ] 1  Network Effects
M12 [#####] 5  Negative WC/Float    PRESENT
```

Strongest block: **C — Growth (10/20)** — unbroken revenue growth, 25.2% 5-yr CAGR.
Weakest block: **D — Balance Sheet Strength (0/20)** — every single D-metric scores
zero at FY26 (ND/EBITDA 8.03x, IC 1.17x, D/E 2.73x, Current Ratio 0.66x).

---

## CLASSIFICATION AND OVERRIDES

Data confidence: 6 years overall (FY21-FY26), but only 4 years for balance-sheet-
anchored metrics → **"5-6 lower, flag: may not have seen a full cycle."** No tier
downgrade applied (downgrade only triggers at 3-4 years).

**Deal-breakers triggered:**
1. Block A (5) < 8 → max GOOD
2. Block B (5) < 8 → max GOOD
3. Median ROCE (5.83%) < 10% → max AVERAGE
5. Promoter pledge (20.02% of promoter holding) > 15% → max AVERAGE
6. **ND/EBITDA (8.03x) > 3x AND Interest Coverage (1.17x) < 3x → AVOID** (dominant)
8. PAT negative in FY24 (one of the last 3 years, FY24-FY26) → max AVERAGE

**Classification matrix (independent of deal-breakers)**: Core score 24 < 40 →
**AVOID** on the matrix alone, before any override is applied.

**FINAL CLASSIFICATION: AVOID**

Both the deal-breaker override (#6) and the base classification matrix (Core <40)
independently land on AVOID — this is not a single fragile trigger.

**Which years drive this, for downstream position-sizing consideration**: the D-block
failure and the FY24 PAT loss are FY24-FY26 phenomena, concurrent with the company's
IPO-cycle capacity build-out (CWIP roughly doubled FY24→FY26; borrowings roughly
2.3x'd FY24→FY26). This is a leverage-and-ROCE story driven by a young, capital-
intensive IPP scaling capacity ahead of full earnings recognition, not by declining
unit economics (OPM expanded every year since FY23; revenue never declined). Whether
that distinction changes the downstream verdict is an operator/FTTCP call — this
stage reports the mechanical AVOID and names the driver, per instructions; it does
not soften the classification.

---

## DECISION LINE

CLEANMAX scores **AVOID (Grand Total 38/160, Core 24/100, Moat MODERATE 14/60)**.
Deal-breaker #6 (Net Debt/EBITDA 8.03x with Interest Coverage 1.17x) and a Core score
under 40 both independently force AVOID. Growth is genuine and undisputed (25.2%
5-yr revenue CAGR, zero decline years) but is currently unsupported by returns on
capital (median ROCE 5.83%, ROE 1.94%) or by balance-sheet cushion (every D-block
metric scores zero). A governance flag (promoter pledge re-established at 20.02% of
promoter holding as at 31 Mar 2026, after having been reported released in the Feb
2026 RHP) compounds the picture. This is a mechanical Gate 0 finding; it does not
determine the pipeline's final verdict but is the load-bearing quantitative input to
it.
