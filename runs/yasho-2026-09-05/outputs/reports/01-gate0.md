# GATE 0 SCORECARD — Yasho Industries Ltd (YASHO)
Run date: 2026-09-05 | Model: Sonnet 5 | Stage: B01-gate0

Data available: 6 years (FY2021 to FY2026) for revenue/PAT/cash-flow lines
(screener-data Data_Sheet.csv). Company-reported ROCE/ROE cover 5 years
(FY2022 to FY2026, AR p.10 financial-highlights infographic). Working-capital
days (needs trade payables) and free cash flow (needs capex breakdown) are
computable only for FY2024-FY2026, the only years with annual-report cash
flow / balance sheet detail in the provided corpus (AR FY2026 + AR FY2025).
Promoter shareholding data spans only FY2025-FY2026 plus Q1FY27, not a full
3-year window. Scoring is adapted to these narrower sub-windows where noted;
each metric states exactly which years it uses.

DATA GAP (per orchestrator note): screener Profit_Loss/Balance_Sheet/
Cash_Flow/Quarters CSVs are header-only (collector defect). All financials
below are extracted from screener-Data_Sheet.csv (populated) and the two
Annual Report text extracts, cross-checked against each other and against
the AR's own financial-highlights infographic (AR p.10 / printed pp.12-15)
for internal consistency. No results/ or rating/ PDF exists in the corpus;
the only source for anything after FY2026 (Mar-2026) is the Q1FY27 Investor
Presentation, used only where explicitly marked "Q1FY27" below and never
substituted into a deal-breaker test in place of the FY2026 audited figure.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 6/20

Source: company-reported ROCE/ROE, consolidated basis (AR p.10 financial
highlights infographic, cross-checked: PAT/EPS in this infographic match
screener-data and the AR's consolidated P&L exactly, confirming these are
consolidated, not standalone, figures). 5-year window FY2022-FY2026.

| FY | ROCE % | ROE % |
|----|--------|-------|
| FY2022 | 34.16 | 30.21 |
| FY2023 | 24.63 | 28.52 |
| FY2024 | 12.87 | 19.66 |
| FY2025 | 8.98 | 1.46 |
| FY2026 | 11.34 | 5.69 |
(AR p.10 infographic; all 5-yr figures on one page)

A1 Median ROCE = 12.87% (sorted: 8.98, 11.34, 12.87, 24.63, 34.16) →
band 10-14.9% = **1**
A2 Minimum single-year ROCE = 8.98% (FY2025) → band 8-11.9% = **1**
A3 Median ROE = 19.66% (sorted: 1.46, 5.69, 19.66, 28.52, 30.21) →
band 15-19.9% = **4**
A4 ROCE trend, latest (FY2026, 11.34%) vs earliest (FY2022, 34.16%) =
decline of 22.82pp → band >5pp decline = **0**

Block A = 1+1+4+0 = **6/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 5/20

CFO and PAT, all 6 years (screener-data Cash Flow and P&L sections):

| FY | CFO (Rs cr) | PAT (Rs cr) |
|----|------|------|
| FY21 | 34.63 | 21.48 |
| FY22 | 16.16 | 52.29 |
| FY23 | 12.52 | 67.87 |
| FY24 | 90.19 | 57.94 |
| FY25 | -40.85 | 6.11 |
| FY26 | 151.29 | 25.26 |
(screener-data)

Cumulative CFO (FY21-26) = Rs 263.94 cr. Cumulative PAT = Rs 230.95 cr.

B1 Cumulative CFO / Cumulative PAT = 263.94/230.95 = 1.14x → band ≥1.00 = **5**

FCF (CFO - capex, capex = PPE + intangible purchases from consolidated cash
flow statement) is computable only for FY2024-FY2026, the only years the
corpus carries a capex breakdown:
- FY2024 capex = Rs 336.99 cr (PP&E incl. CWIP Rs 334.18 cr + intangibles
  Rs 2.81 cr; AR FY2025 p. consolidated CF statement, FY2024 comparative
  column, line "Purchase of property, plant and equipment... 33,418.45" +
  "Payment for intangible assets... 280.86", both in Rs Lakhs)
- FY2025 capex = Rs 12.83 cr (Rs 344.40 lakhs PP&E + Rs 938.80 lakhs
  intangibles; AR FY2026 consolidated CF statement, FY2025 comparative
  column, matches AR FY2025's own FY2025 primary column exactly)
- FY2026 capex = Rs 73.84 cr (Rs 6,679.07 lakhs PP&E/CWIP + Rs 704.51 lakhs
  intangibles; AR FY2026 consolidated CF statement, FY2026 column)

FCF FY2024 = 90.19 - 336.99 = **-246.80 cr**
FCF FY2025 = -40.85 - 12.83 = **-53.68 cr**
FCF FY2026 = 151.29 - 73.84 = **+77.45 cr**

B2 FCF-positive years = 1 of 3 measurable years (33%) → band <50% = **0**
B3 Cumulative FCF (FY24-26) / Cumulative PAT (FY24-26) =
(-246.80-53.68+77.45) / (57.94+6.11+25.26) = -223.03/89.31 = -2.50x →
negative → **0**

B4 Working capital days, computable for FY2024-FY2026 only (trade payables
not available pre-FY2024 in the corpus). All days on revenue basis
(COGS not separately disclosed as a single line):
- Receivable Days = Trade Receivables / Revenue x 365 (screener-data)
- Inventory Days = Inventory / Revenue x 365 (screener-data)
- Payable Days = Trade Payables / Revenue x 365 (Trade Payables: FY2024
  Rs 47.95 cr, FY2025 Rs 64.94 cr, FY2026 Rs 89.46 cr — AR FY2026
  consolidated balance sheet Note 22, current-year and comparative
  columns, plus AR FY2025 consolidated balance sheet for the FY2024
  comparative column)

| FY | Recv Days | Inv Days | Pay Days | WC Days |
|----|-----------|----------|----------|---------|
| FY24 | 73.77 | 83.07 | 29.49 | 127.35 |
| FY25 | 72.40 | 142.65 | 35.09 | 179.96 |
| FY26 | 79.67 | 112.64 | 39.34 | 152.97 |

Latest (FY26, 152.97 days) vs earliest available (FY24, 127.35 days) =
increase of 25.6 days → band increased >15 = **0**

Block B = 5+0+0+0 = **5/20**

Note: company's own Investor Presentation (p.12) states working-capital
cycle improved from 190 to 143 days recently, endeavouring to hold there.
This does not match the FY24→FY26 revenue-basis WC-days trend computed
above (worsened, +25.6 days); the two likely use different bases/windows
(company figure appears to be a recent-quarter/trailing measure, not a
year-end-to-year-end audited comparison). B4 is scored on the audited
year-end figures only, per the "never estimate" rule; the divergence is
noted for the operator, and lines up with company memory's load-bearing
verification item #3 (cash conversion structural vs growth-induced).

---

## BLOCK C: GROWTH (Max 20) — Score: 7/20

Revenue and PAT, FY2021-FY2026 (screener-data):
Revenue: 359.44 / 612.66 / 671.55 / 593.57 / 675.64 / 830.03 (Rs cr)
PAT: 21.48 / 52.29 / 67.87 / 57.94 / 6.11 / 25.26 (Rs cr)

C1 Revenue CAGR (FY21→FY26, 5 yrs) = (830.03/359.44)^(1/5)-1 = **18.22%**
→ band 15-19.9% = **4**
C2 PAT CAGR (FY21→FY26, 5 yrs) = (25.26/21.48)^(1/5)-1 = **3.30%**
→ band <5% = **0**
C3 Positive YoY revenue years: FY22(+), FY23(+), FY24(-, 593.57 vs 671.55),
FY25(+), FY26(+) = 4 of 5 = 80% → band 75-99% = **3**
C4 PAT CAGR minus Revenue CAGR = 3.30 - 18.22 = **-14.92pp** →
band <-8pp = **0**

Block C = 4+0+3+0 = **7/20**

No deal-breaker 7 (revenue declined in only 1 of 5 years, not a majority).
No deal-breaker 8 (annual PAT positive in all of FY24/25/26; note PAT was
negative in two individual quarters within FY25 — Q1FY25 -Rs 2.46 cr and
Q3FY25 -Rs 0.82 cr per screener-data Quarters — but the full fiscal years
themselves stayed positive).

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 4/20

All figures FY2026 audited, consolidated (last full balance sheet in the
corpus). Borrowings figure used throughout (screener-data Borrowings row,
Rs 557.93 cr) is lease-inclusive; cross-checked against AR FY2026
consolidated balance sheet Notes 15/16/20/21 (non-current borrowings
28,913.37 + non-current lease 673.69 + current borrowings 25,180.70 +
current lease 1,025.48 = 55,793.24 lakhs = Rs 557.93 cr, exact match) and
against the company's own reported Net Debt/Equity of 1.22x (AR p.10
infographic) which implies the same net-debt base.

EBITDA FY2026 = Rs 144.46 cr (= PBT 33.96 + Interest 55.72 + Depreciation
54.77, screener-data; independently matches AR p.10 infographic EBITDA of
Rs 14,446 lakhs exactly, confirming methodology).

Cash & Bank FY2026 = Rs 18.02 cr (screener-data). Net Debt = 557.93-18.02 =
**Rs 539.91 cr**.

D1 Net Debt / EBITDA = 539.91/144.46 = **3.74x** → band >3x = **0**
D2 Interest Coverage = EBIT/Interest = (33.96+55.72)/55.72 = 89.68/55.72 =
**1.61x** → band 1.5-2.9x = **1**
D3 Debt / Equity = 557.93 / 443.92 (Total Equity FY2026 consolidated,
AR p.86 balance sheet: Equity Share Capital 1,205.71 + Other Equity
43,186.08 lakhs = Rs 443.92 cr) = **1.257x** → band 1.0-1.5x = **1**
D4 Current Ratio = Total Current Assets 49,856.59 / Total Current
Liabilities 36,396.95 (AR FY2026 consolidated balance sheet, p.86) =
**1.370x** → band 1.2-1.49x = **2**

Block D = 0+1+1+2 = **4/20**

**DEAL-BREAKER 6 TRIGGERED**: ND/EBITDA (3.74x) >3x AND Interest Coverage
(1.61x) <3x → caps classification at AVOID.

**Flagged divergence (not used to override the deal-breaker):** the
Investor Presentation (p.17-18, "Financial Leverage" chart) shows company-
disclosed Debt/EBITDA falling from 5.12x (FY24) to 4.72x (FY25) to 3.74x
(FY26, matches the audited figure above) to **1.86x (Q1FY27)**, with Total
Debt only easing marginally (Rs 552.3 cr → Rs 540.9 cr) over that last
quarter. The scale of the ratio improvement is therefore driven mostly by
the EBITDA denominator, and the presentation does not disclose whether this
is a trailing-twelve-month EBITDA or another basis; attempting to
reconstruct it from screener quarterly Operating Profit (TTM Q2FY26-Q1FY27
= Rs 183.95-194 cr, depending on assumptions) does not cleanly reproduce
1.86x. This basis could not be independently reconciled from the provided
corpus, so D1/D2 are scored on the fully-reconciled FY2026 audited figures,
not the Q1FY27 presentation figure. This is precisely company memory's
load-bearing verification item #2/#3 (margin step-up and leverage
improvement: structural or one quarter) and should be first-priority in
downstream verification.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 13/20

E1 Promoter holding, latest = 67.91% (FY2026, AR p.30 pdf/"Shareholding
Pattern as on March 31, 2026", Sub-total [A] 81,88,115 shares, 67.91%) →
band ≥60% = **5** (Q1FY27 presentation, p.19, shows 67.94% as of 30-Jun-2026,
consistent)

E2 Promoter holding change over 3 years: **N/A (data not available)**.
Corpus carries only FY2025 (67.99%, AR FY2025 p. shareholding pattern,
Sub-total [A] 81,98,165 shares) and FY2026 (67.91%), a 1-year window
(-0.08pp), plus Q1FY27 (67.94%). No FY2023 baseline exists in the provided
corpus (no AR FY2023/FY2024 text extract). Per rule 5, not filled with an
estimate. → **0**

E3 Promoter pledge, latest: no promoter-share pledge or encumbrance
disclosure found anywhere in AR FY2026 (searched "pledge"/"encumb" across
the full text; the only pledge references found are the company's own
assets/receivables pledged as loan security against borrowings, Note 15/20
and Directors' Report, unrelated to promoter shareholding). SEBI Reg 31
mandates disclosure of any promoter pledge in the shareholding pattern; its
absence is read as 0% pledge. → band 0% = **5** (flagged as an
absence-of-disclosure inference, not an explicit "0%" statement, for
verifier awareness)

E4 Contingent Liabilities / Net Worth, latest: Contingent Liabilities
FY2026 = LC/Bills under LC Rs 1,588.33 lakhs + Bank guarantees Rs 232.23
lakhs + GST dispute Rs 3,853.72 lakhs + Customs duty dispute Rs 175.36
lakhs = Rs 5,849.64 lakhs = **Rs 58.50 cr** (AR p.74/Note 37 "Contingent
Liabilities & Commitments"; Capital Commitments of Rs 2,751.42 lakhs
excluded as a commitment, not a contingent liability). Net Worth FY2026 =
Rs 443.92 cr (consolidated, as above). E4 = 58.50/443.92 = **13.18%** →
band 5-15% = **3**

Block E = 5+0+5+3 = **13/20**

---

## CORE SCORE

| Block | Score | Max |
|-------|-------|-----|
| A - Return on Capital | 6 | 20 |
| B - Cash Generation Quality | 5 | 20 |
| C - Growth | 7 | 20 |
| D - Balance Sheet Strength | 4 | 20 |
| E - Shareholder Alignment | 13 | 20 |
| **Core Total** | **35** | **100** |

Strongest block: **E (Shareholder Alignment, 13/20, 65%)** — high promoter
holding, no pledge signal, contingent liabilities modest relative to net
worth.
Weakest block: **D (Balance Sheet Strength, 4/20, 20%)** — FY2024 Pakhajan
capex cycle (Rs 336.99 cr in one year) pushed leverage and coverage past
deal-breaker thresholds on the FY2026 audited base; B (5/20) is a close
second, same root cause (capex swamped operating cash flow FY24-FY25).

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 10/60

| Test | Score | Basis |
|------|-------|-------|
| M1 Pricing Power | 3 | EBITDA margin FY21 16.44% → FY26 17.40% (screener-data PBT+Interest+Depreciation; cross-matches AR infographic EBITDA exactly for FY22-26) = +0.96pp, stable within ±2pp; revenue CAGR 18.22% ≥10% → tier 2 |
| M2 Cost Advantage vs peer | 0 | PEER DATA NEEDED — no peer set in corpus |
| M3 Capital Efficiency | 0 | FAT (FY26) = Revenue 830.03 / Net Fixed Assets 644.22 cr (AR infographic, Net Block+CWIP) = 1.29x (>1x) but ROCE FY26 = 11.34% (not >12%, near-miss) → fails AND condition, else = 0 |
| M4 Customer Stickiness | 3 | 1 revenue-decline year (FY24); FY25 (675.64) exceeded prior peak FY23 (671.55), fully recovered → tier 2 |
| M5 Scale & Dominance | 0 | PEER DATA NEEDED — no peer mcap/margin data in corpus |
| M6 Technology/R&D | 0 | R&D/Revenue FY26 = Rs 5.73 cr / Rs 830.03 cr = 0.69% (AR p. Secretarial Audit annexure, Total R&D Expenditure Rs 573.04 lakhs vs Rs 288.39 lakhs FY25); below the ≥1% floor tier |
| M7 Regulatory/License | 0 | Unregulated, non-licence specialty-chemicals segment |
| M8 Distribution | 1 | "2,000+ Customers" stated (AR p.6 infographic) but no multi-year reach trend disclosed in corpus; archetype is B2B export chemicals, "outlet" concept has limited applicability → mentioned, unquantified trend |
| M9 Brand | 0 | PEER DATA NEEDED for peer gross-margin comparison; GM proxy (Revenue-Material Cost)/Revenue FY26 = 40.13%, stated as proxy but no peer benchmark available |
| M10 Switching Costs | 3 | Revenue grew all years but 1 (FY24); receivable days FY21 (72.61) vs FY26 (79.67) = +7.06 days, within the ±10-day "stable" threshold used elsewhere in this framework → tier 2 |
| M11 Network Effects | 0 | 6 years available (minimum for the two-window test), but the "prior 3yr" window has only 2 intervals (FY21-FY23, no FY20 baseline in corpus): 2-yr CAGR 36.69% vs latest 3-yr CAGR (FY23→FY26) 7.32% — sharp deceleration either way; scored conservatively per the "score conservatively, state so" instruction for a boundary case = 0 |
| M12 Negative WC/Float | 0 | WC days (FY24-26 only, per Block B) = 127-180 days, consistently >45 days |

Moats present (score ≥3): M1, M4, M10 = **3**
Moat classification: 2-3 present = **MODERATE**

Moat score = 3+0+0+3+0+0+0+1+0+3+0+0 = **10/60**

---

## CLASSIFICATION

Grand Total = Core (35) + Moat (10) = **45/160**

Data confidence: 6 years of revenue/PAT history → "5-6 lower confidence,
flag may not have seen full cycle" band. Several Block B/D/E sub-metrics
rest on a narrower 3-year (FY24-26) or 1-year (E2) window due to corpus
gaps, noted throughout above. No downgrade tier applies (that triggers only
at 3-4 years); classification stands as computed.

Classification matrix: Core 35 <40 → **AVOID** (independent of moat tier).

Deal-breaker overrides triggered:
1. Block A (6) <8 → max GOOD (non-binding, AVOID is lower)
2. Block B (5) <8 → max GOOD (non-binding, AVOID is lower)
6. ND/EBITDA (3.74x) >3x AND Interest Coverage (1.61x) <3x → **AVOID**
   (binding, drives FY2024 Pakhajan capex cycle)

Not triggered: #3 (median ROCE 12.87%, not <10%), #4 (cumulative CFO/PAT
1.14x, not <0.50), #5 (no pledge found), #7 (only 1 of 5 years declined),
#8 (all 3 latest annual PATs positive), #9 (6 years of history, not <3).

**CLASSIFICATION: AVOID**

Decision line: Gate 0 mechanically scores AVOID on FY2026 audited
financials, driven by the FY2024 Pakhajan-expansion capex cycle (Rs 336.99
cr in one year) that pushed net debt/EBITDA to 3.74x and interest coverage
down to 1.61x, and by growth quality that has decoupled (revenue CAGR
18.22% vs PAT CAGR 3.30% over FY21-26). This is a mechanical score, not a
verdict — per pipeline rules there is no STOP and company quality never
halts a run; the AVOID classification and its named depressors travel
forward as evidence for Halt 1. The Q1FY27 company-disclosed reversal
(leverage 3.74x→1.86x, EBITDA margin 17.4%→23.8% per company memory) is
exactly the kind of post-period data this scorecard is structurally unable
to verify or credit, and is flagged as the top downstream verification
priority, consistent with the operator's stated spear load-bearing facts.

```yaml
stage: B01-gate0
company: "YASHO"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
input_gaps:
  - "screener Profit_Loss/Balance_Sheet/Cash_Flow/Quarters CSVs are header-only (collector defect); all financials extracted from screener-Data_Sheet.csv and AR FY2026/FY2025 text instead"
  - "no results/ or rating/ PDFs in corpus; Q1FY27 latest-period figures sourced only from Investor Presentation (unaudited), used for context, never substituted into a deal-breaker or Block D/E score in place of FY2026 audited figures"
  - "promoter holding 3-year change (E2): only FY2025-FY2026 + Q1FY27 available in corpus, no FY2023 baseline"
  - "capex breakdown and trade payables unavailable for FY2021-FY2023 (no AR corpus for those years); FCF (Block B2/B3) and WC days (Block B4) computed only for FY2024-FY2026"
  - "peer/sector comparison data absent in corpus for moat tests M2, M5, M9"
flags:
  - {type: FLAG-GATE0, reason: "Classification AVOID; Core 35/100 driven by growth-quality decoupling (revenue CAGR 18.22% vs PAT CAGR 3.30%, FY21-26) and a triggered leverage/coverage deal-breaker (ND/EBITDA 3.74x, EBIT/Interest 1.61x, FY2026 audited), both traced to the FY2024 Pakhajan capex cycle (Rs 336.99 cr in one year)."}
  - {type: FLAG-CASH, reason: "Block B 5/20; cumulative FCF/PAT FY2024-FY2026 = -2.50x, only 1 of 3 measurable years FCF-positive, driven by FY2024 capex exceeding CFO; FY2026 shows a sharp reversal (CFO Rs 151.29 cr vs Rs -40.85 cr FY2025) not yet reflected in the cumulative ratio."}
  - {type: FLAG-LEVERAGE-DIVERGENCE, reason: "FY2026 audited ND/EBITDA (3.74x, triggers deal-breaker 6) vs Q1FY27 company-disclosed ND/EBITDA (1.86x, Investor Presentation p.17-18); TTM EBITDA basis behind the Q1FY27 figure could not be reconciled from provided data. Matches company memory load-bearing verification items #2 and #3 (margin step-up and leverage improvement, structural or one quarter) — top downstream verification priority."}
data_years: 6
fy_range: "FY2021 to FY2026"
blocks: {A: 6, B: 5, C: 7, D: 4, E: 13}
core_score: 35
moat_score: 10
grand_total: 45
moats_confirmed: 3
moat_class: "MODERATE"
classification: "AVOID"
deal_breakers:
  - "1: Block A 6 <8 -> max GOOD (non-binding)"
  - "2: Block B 5 <8 -> max GOOD (non-binding)"
  - "6: ND/EBITDA 3.74x >3x AND Interest Coverage 1.61x <3x (FY2026 audited) -> AVOID (binding)"
history_downgrade: false
data_notes:
  - "PEER DATA NEEDED for M2 (cost advantage), M5 (scale/dominance), M9 (brand) — no peer/sector comparison set in corpus"
  - "WC days (Block B4) and FCF (Block B2/B3) computed only for FY2024-FY2026; wider FY21-23 window unavailable due to missing capex/payables detail"
  - "M9 gross-margin proxy used: (Revenue - Material Cost) / Revenue = 40.13% FY2026, no peer benchmark available to score against"
  - "E3 (0% pledge) is an absence-of-disclosure inference (no pledge/encumbrance mention found in AR FY2026 full text), not an explicit stated percentage"
  - "D1/D2 scored on FY2026 audited annual basis; Q1FY27 company-disclosed leverage improvement (3.74x -> 1.86x ND/EBITDA) noted but not used to score or override deal-breaker 6, methodology unreconciled from provided data"
block_b_trend: "improving, but from a weak base: CFO swung from -Rs 40.85 cr (FY2025) to +Rs 151.29 cr (FY2026); cumulative FY24-26 FCF/PAT still -2.50x"
analyst_note: "AVOID is mechanical, not a company-quality verdict: Block D failure and much of Block B weakness trace to one event, the FY2024 Pakhajan capex cycle (Rs 336.99 cr in a single year), which pushed FY2026 audited ND/EBITDA to 3.74x and interest coverage to 1.61x, triggering deal-breaker 6. Growth quality is separately weak on its own terms: revenue CAGR 18.22% has not converted to PAT CAGR (3.30%) over FY21-26, with FY2025 a near-trough year (PAT Rs 6.11 cr, ROE 1.46%). The scorecard cannot see past FY2026 (Mar-2026): the only later data point, Q1FY27, shows large moves in the same metrics that drove the AVOID (leverage 3.74x->1.86x, margin 17.4%->23.8% per company memory) but its EBITDA/leverage methodology is not reconcilable from the provided corpus, so none of it is scored here. Whether that Q1FY27 move is structural (supports a transition thesis) or a single strong quarter is the single highest-value fact for downstream verification, and is already named as such in company memory's spear load-bearing facts."
```
