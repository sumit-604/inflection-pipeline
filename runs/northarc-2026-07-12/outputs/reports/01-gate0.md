# GATE 0 SCORECARD — Northern Arc Capital Ltd (NORTHARC)
Run date: 2026-07-12 | Stage: B01-gate0 | Model: claude-sonnet-5

## METHODOLOGY NOTE — NBFC ADAPTATION (read first)

Northern Arc Capital Ltd (NACL) is a diversified retail-focused NBFC-Middle
Layer (RBI-registered lender), rated [ICRA]AA- (Stable)/[ICRA]A1+
(29-Dec-2025). The manifest's sector_cap_row "Pharma / CDMO" is a known
auto-collector error and is ignored here. Per operator instruction, Gate 0
blocks are scored on financial-services line items (AUM growth, NIM/spread,
GNPA/NNPA, credit cost, CRAR, managed gearing, RoA, RoE), and metrics with
no NBFC analogue (inventory turns, fixed-asset turnover, working-capital
days built on trade receivables/payables/inventory, current ratio) are
marked **NOT APPLICABLE (NBFC)** rather than scored as missing data. Where
a metric is computable but only via a structural proxy (ROCE, given
Ind AS NBFC balance sheets carry no current/non-current liabilities split),
that proxy is stated explicitly and flagged.

Data available: **9 annual data points (FY2017, FY2019–FY2026; FY2018 is
absent from the screener source — a gap in the data, not a company event)**.
Scoring adapted to this history. Public listed history is short (IPO
24-Sep-2024, ~1.75 years to this run date) even though pre-IPO financial
statements extend back to FY2017; this is flagged separately
(`history_downgrade: true`) from the financial-statement-years data
confidence tier.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 3/20

ROCE computed via NBFC-adapted proxy (screener's own Balance_Sheet ROCE
row was blank): **Capital Employed = Total Assets − "Other Liabilities"**
(screener line item; Other Liabilities ≈ trade payables + provisions +
other non-financial liabilities, i.e. non-debt operating liabilities — the
closest available analogue to "current liabilities" since Ind AS NBFC
balance sheets are presented in order of liquidity with no current/
non-current classification). **EBIT = PBT + Interest expense**
(screener-Data_Sheet.csv).

| FY | EBIT (PBT+Int, ₹Cr) | Capital Employed (₹Cr) | ROCE |
|---|---|---|---|
| 2017 | 273.13 | 2,838.49 | 9.62% |
| 2019 | 477.36 | 4,092.58 | 11.66% |
| 2020 | 454.03 | 4,427.93 | 10.25% |
| 2021 | 423.83 | 5,514.36 | 7.69% |
| 2022 | 659.53 | 7,722.04 | 8.54% |
| 2023 | 880.29 | 8,990.00 | 9.79% |
| 2024 | 1,150.33 | 11,362.16 | 10.12% |
| 2025 | 1,217.92 | 13,294.25 | 9.16% |
| 2026 | 1,430.38 | 16,153.90 | 8.86% |
(all screener-Data_Sheet, computed)

- **A1 Median ROCE = 9.62%** (screener-Data_Sheet, computed) → <10% → **0 pts**
- **A2 Minimum single-year ROCE = 7.69% (FY2021)** (screener-Data_Sheet, computed) → <8% → **0 pts**
- **A3 Median ROE = 10.93%** (screener-Data_Sheet, computed; see table below) → <12% → **0 pts**
- **A4 ROCE trend, FY2026 (8.86%) vs FY2017 (9.62%) = 0.76pp decline** (screener-Data_Sheet, computed) → below the explicit 1-3pp band, latest is nonetheless < earliest so the top "≥earliest" band does not apply; scored under nearest lower band as an edge case → **3 pts**

ROE detail (PAT ÷ average Net Worth; FY2017 and FY2019 use closing net
worth only per formula rule — FY2017 is the earliest year with no prior
data, and FY2019 follows the FY2018 gap):

| FY | PAT (₹Cr) | Net Worth close (₹Cr) | Avg NW basis | ROE |
|---|---|---|---|---|
| 2017 | 63.77 | 475.76 | closing only | 13.40% |
| 2019 | 99.17 | 1,091.96 | closing only (FY18 gap) | 9.08% |
| 2020 | 92.84 | 1,423.78 | (1,091.96+1,423.78)/2 | 7.38% |
| 2021 | 67.52 | 1,499.67 | (1,423.78+1,499.67)/2 | 4.62% |
| 2022 | 172.50 | 1,656.43 | (1,499.67+1,656.43)/2 | 10.93% |
| 2023 | 230.01 | 1,872.78 | (1,656.43+1,872.78)/2 | 13.04% |
| 2024 | 308.33 | 2,231.75 | (1,872.78+2,231.75)/2 | 15.02% |
| 2025 | 304.55 | 3,434.25 | (2,231.75+3,434.25)/2 | 10.75% |
| 2026 | 406.02 | 3,895.56 | (3,434.25+3,895.56)/2 | 11.08% |
(all screener-Data_Sheet, computed)

FY2026 computed ROE (11.08%) reconciles closely to the company's disclosed
"Return on Equity increased by 110 bps YoY to 11.1% for FY26" (press
release, in results PDF p.25) — validates the methodology. FY2025's
computed ROE is compressed by the Sep-2024 IPO equity infusion (net worth
+54% at FY2025 close vs FY2024 close), a capital-base effect, not a
profitability decline — RoA and RoE both *improved* YoY in FY26 per the
company (see Block D commentary).

Deal-breakers triggered: **#1 Block A <8 → max GOOD** (driven by the
FY2021 COVID-trough minimum ROCE and structurally low NBFC ROCE proxy
across all years, see Methodology Note); **#3 median ROCE <10% → max
AVERAGE**.

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 0/20 (structural — see FLAG-CASH)

CFO is negative in every year with data (FY2019–FY2026). This is a known,
structural feature of a growing NBFC: loan disbursements are classified as
operating cash outflows under Ind AS, so a lender expanding AUM 20-22%
p.a. mechanically shows negative CFO. This is **not** the same signal as a
manufacturer burning cash against reported profit.

| FY | CFO (₹Cr) | PAT (₹Cr) | CFO/PAT |
|---|---|---|---|
| 2019 | -335.84 | 99.17 | -3.39x |
| 2020 | -54.21 | 92.84 | -0.58x |
| 2021 | -711.40 | 67.52 | -10.54x |
| 2022 | -1,325.50 | 172.50 | -7.68x |
| 2023 | -1,295.65 | 230.01 | -5.63x |
| 2024 | -2,134.44 | 308.33 | -6.92x |
| 2025 | -1,046.68 | 304.55 | -3.44x |
| 2026 | -1,540.60 | 406.02 | -3.79x |
(screener-Data_Sheet, cash flow section)

- **B1 Cumulative CFO ÷ Cumulative PAT = -8,444.32 ÷ 1,680.94 = -5.02x** (screener-Data_Sheet, computed) → negative → **0 pts**
- **B2 FCF-positive years = 0 of 8 (0%)** (CFO negative every year; capex is immaterial — FY26 consol capex ₹15.09 Cr, FY25 ₹18.08 Cr, results PDF p.24/p.36 — so FCF≈CFO, still negative) → **0 pts**
- **B3 Cumulative FCF ÷ Cumulative PAT ≈ -5.0x** (same basis) → negative → **0 pts**
- **B4 Change in WC Days** → **NOT APPLICABLE (NBFC)**. The company's core asset is "Loans" (₹12,492.77 Cr standalone, FY2026, results PDF p.7), not trade receivables; the screener "Receivables" line (₹20.6 Cr FY2026, ≈2.8 receivable-days-equivalent on Sales) is immaterial and non-representative of the operating cycle. Inventory is nil/blank throughout.

**block_b_trend: improving.** CFO/PAT ratio moved from -6.92x (FY2024) to
-3.44x (FY2025) to -3.79x (FY2026) — deeply negative throughout, but the
multi-year trough was FY2024 and the ratio has roughly halved in magnitude
since, consistent with the deceleration in loan-growth-driven cash use as
the book matures. Still structurally negative and worth monitoring if AUM
growth (guided 22-25% p.a. through FY2029 per MD&CEO commentary, press
release p.25) continues at pace.

Deal-breakers triggered: **#2 Block B <8 → max GOOD**; **#4 cumulative
CFO/PAT <0.50 → max AVERAGE** (both structural, see above — not a genuine
earnings-quality failure).

---

## BLOCK C: GROWTH (Max 20) — Score: 18/20 (strongest block)

Revenue = Total Income (interest income + fee income + other operating
income); this is the correct top-line measure for a lender.

- **C1 Revenue CAGR, FY2017 (₹370.14 Cr) → FY2026 (₹2,690.24 Cr), 9 yrs elapsed = 24.65%** (screener-Data_Sheet, computed) → ≥20% → **5 pts**
- **C2 PAT CAGR, FY2017 (₹63.77 Cr) → FY2026 (₹406.02 Cr), 9 yrs = 22.83%** (screener-Data_Sheet, computed) → ≥20% → **5 pts**
- **C3 Positive YoY revenue years = 7 of 7 valid consecutive transitions (100%)** (FY19→20→21→22→23→24→25→26 all positive; the FY2017→FY2019 transition is excluded as non-consecutive due to the FY2018 gap) (screener-Data_Sheet, computed) → 100% → **5 pts**
- **C4 PAT CAGR − Revenue CAGR = 22.83% − 24.65% = -1.81pp** (computed) → within ±3pp → **3 pts**

No loss-to-profit swing; PAT positive every measured year.

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, NBFC alternates per framework) — Score: 8/20

- **D1 CRAR (latest) = 22.56%** (standalone, audited, results PDF p.18, Annexure 1: "Capital adequacy ratio (CRAR) 22.56%"; consolidated managed CRAR 22.6% per press release p.25, and 24.6% per ICRA H1 FY2026 table on a broader "managed assets" basis, rating PDF p.6) → ≥18% → **5 pts**
- **D2 PCR (Provision Coverage Ratio) = (Gross Stage 3 − Net Stage 3) ÷ Gross Stage 3 = (1.34% − 0.70%) ÷ 1.34% = 47.8%** (standalone, results PDF p.18, Annexure 1: "Gross stage 3 assets ratio 1.34%", "Net stage 3 assets ratio 0.70%"; consolidated press-release GNPA/NNPA of 1.2%/0.6% gives an equivalent ≈50%, results PDF p.25) → <60% → **0 pts**
- **D3 Debt/Equity = 3.13x disclosed** (standalone, results PDF p.18, Annexure 1) — **"Financials: default 3" applied per framework rule** → **3 pts**
- **D4 Current Ratio** → **NOT APPLICABLE (NBFC)** — the company's own filing states this explicitly: "current ratio... are not applicable / relevant to the Company and hence not disclosed" (results PDF p.18, Annexure 1 notes).

Context (not separately scored): Gross Stage 3 (NPA) ratio rose 0.5%
(FY2024) → 1.0% (FY2025) → 1.2% (FY2026) (ICRA table, rating PDF p.6;
press release, results PDF p.25). ICRA notes "a few of NACL's exposures
in the NBFC segment went under stress in recent quarters" and flags
increased stress in the microfinance and secured business loan portfolios
as monitorable (rating PDF p.3). Consolidated managed gearing improved
4.3x (Mar-2024) → 3.1x (Mar-2025) → 3.0x (Sep-2025) on IPO/equity infusion
(rating PDF p.3). Absolute NPA levels remain low by NBFC standards; the
shortfall is specifically on the coverage-ratio calculation (D2), not
absolute asset quality.

No Block D deal-breaker triggers (CRAR is strong; the ND/EBITDA>3x AND
IC<3x combo (#6) is a manufacturing-metric test not used here, and its
NBFC analogue — weak CRAR and weak PCR together — does not apply since
CRAR is comfortably above threshold).

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 3/20

NACL has **no promoter group** — it is a professionally managed,
PE/DFI-backed NBFC that listed via IPO on 24-Sep-2024.

- **E1 Promoter holding** → "Professionally managed: 3 if FII+DII >50%" rule applied. Per ICRA (29-Dec-2025, rating PDF p.5): on a fully-diluted basis as of Sep-2025, LeapFrog Financial Inclusion India II Ltd (16.2%), Augusta Investments II Pte Ltd (16.0%), Eight Roads Investments (Mauritius) II Ltd (7.3%), IFC (6.1%), Accion (4.0%), SMBC (3.8%) and Dvara Trust (3.1%) — all institutional/FPI investors — together hold **56.5%**, exceeding 50% ("others" 40.0% unspecified by holder type) → **3 pts**
- **E2 Promoter holding change, 3yr** → **NOT APPLICABLE** (no promoter/promoter group exists)
- **E3 Promoter pledge** → **NOT APPLICABLE** (no promoter/promoter group exists)
- **E4 Contingent liabilities ÷ Net Worth** → **N/A (not in provided data)** — the provided results filings do not include the notes-to-accounts contingent-liability schedule (would require the Annual Report) → **0 pts**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Raw score: 10 (2 of 12 tests N/A)

| Test | Score | Basis / anchor |
|---|---|---|
| M1 Pricing Power | 0 | PBT margin (proxy for EBITDA margin — annual "Operating Profit" line not in screener) fell from 26.15% (FY2017) to 19.91% (FY2026), a 6.24pp decline despite revenue CAGR ≥10%; exceeds the "declined 2-5pp" partial-credit band (screener-Data_Sheet, computed). Note: FY26 RoA/RoE/credit-cost trends are improving YoY (press release, results PDF p.25) even though the full 9-year PBT-margin window shows compression (COVID-era FY2021 trough, then elevated credit costs). |
| M2 Cost Advantage vs peers | 0 | PEER DATA NEEDED — no peer financials provided |
| M3 Capital Efficiency (FAT) | **NOT APPLICABLE (NBFC)** | Net Block is 0.49% of Total Assets (₹81.43 Cr / ₹16,744.6 Cr, FY2026); fixed-asset turnover has no meaningful analogue for a balance-sheet lender |
| M4 Customer Stickiness | 3 (partial) | Zero revenue-decline years across all 7 valid transitions FY2019-FY2026 (verified); "receivable days stable ±10" sub-condition **NOT APPLICABLE (NBFC)** — trade receivables trivial/non-core. Scored on the verified component; treat as lower-confidence than M8 |
| M5 Scale & Dominance | 0 | PEER DATA NEEDED |
| M6 Technology/R&D | 0 | R&D/Revenue NOT FOUND (not in provided data); qualitative reference to proprietary "Nimbus" tech platform (rating PDF p.5) is unquantified |
| M7 Regulatory/License | 0 | PEER DATA NEEDED — count of listed NBFC-ML peers not in provided data set |
| M8 Distribution | 3 | Network growing and quantified: 432 branches, +72 added in FY2026, 57 digital partnerships, 368 origination partners (press release, results PDF p.25); revenue CAGR 24.65% ≥15%. "Revenue per outlet stable/growing" for the top band not computable from provided data |
| M9 Brand | 0 | PEER DATA NEEDED |
| M10 Switching Costs | 3 (partial) | Revenue grew every year FY2019-FY2026 (verified, exceeds the "growth all but 1 year" threshold); "receivable days rose ≤10 days" sub-condition **NOT APPLICABLE (NBFC)**, same basis as M4 |
| M11 Network Effects | 1 | Latest 3yr revenue CAGR (FY2024→FY2026) = 19.28% < prior 3yr CAGR (FY2021→FY2024) = 40.49% (screener-Data_Sheet, computed), so top band fails; ≥20% band also fails (19.28%<20%); FY2026 "Selling and admin" expense line is blank in source (NOT FOUND), so the selling-expense-% trend is unverified. Scored on the growth>15% criterion alone |
| M12 Negative WC / Float | **NOT APPLICABLE (NBFC)** | No trade-payables/inventory cycle for a balance-sheet lender |

**Moat score = 10** (raw sum, 10 tests scored, 2 marked N/A and excluded).
**Moats "present" (score ≥3): M4, M8, M10 → moats_confirmed = 3.**
M4 and M10 rest on a partially-inapplicable NBFC test (verified on the
revenue-stability component only); M8 is fully evidenced. Treat
moats_confirmed with that caveat.

**Moat classification: 2-3 present = MODERATE.**

---

## CLASSIFICATION

**Raw core_score (literal sum of Blocks A-E, 0-20 each) = 3+0+18+8+3 = 32/100.**

This raw figure mechanically implies "Core <40 → AVOID," but 20 of the 80
nominal points behind it (B4, D4, E2, E3) are scored 0 by convention
purely because the metric is **NOT APPLICABLE** to an NBFC — not because
data is missing or performance is weak. Per operator instruction ("do not
let inapplicable manufacturing ratios drag the score as if data were
missing"), the adjusted-basis calculation is:

**32 achieved ÷ 80 applicable nominal points = 40%** — the AVERAGE
threshold.

Independently, the deal-breaker overrides already cap classification at
**max AVERAGE** (triggers #3 median ROCE <10%, #4 cumulative CFO/PAT
<0.50 — both traced above to NBFC-structural causes, not company-specific
deterioration), which converges with the adjusted-basis reading. No
deal-breaker forces a classification below AVERAGE (revenue never
declined; PAT never negative; no pledge exists; history exceeds the
<3-year threshold).

**grand_total (raw) = core_score(32) + moat_score(10) = 42.**

**Classification: AVERAGE.**

Data confidence: 9 annual data points (7-9 bracket) = "moderate" — no
forced tier downgrade under the numeric-years rule. However, per operator
instruction, **history_downgrade = true** is set separately to flag that
the company's *public listed* history is short (IPO 24-Sep-2024, ~1.75
years to this run date), which materially limits confidence in
market-based continuity (price history, post-listing shareholder
behavior) even though the financial-statement history is longer.

### Strongest block: C (Growth) — 18/20 (90%)
### Weakest block: B (Cash Generation Quality) — 0/20 (structural NBFC feature, not a genuine red flag — see FLAG-CASH)

### Decision line
AVERAGE (adjusted-basis). A structurally strong, growing (24.65% revenue
CAGR, 22.83% PAT CAGR), well-capitalized (CRAR 22.56%, comfortably above
the 18% threshold), professionally managed (no promoter, FII/DII 56.5%)
NBFC whose Gate 0 return-on-capital and cash-conversion blocks score
mechanically low only because this scorecard's manufacturer-oriented ROCE
and cash-conversion metrics have no clean analogue for a loan-book-growth
business under Ind AS. Genuine, non-structural watch items: PCR (~47.8%)
sits below the 60% adequacy band despite low absolute NPAs (Gross
1.2%/Net 0.6%, FY2026); Gross Stage 3 rose from 0.5% to 1.2% over
FY2024-FY2026, flagged by ICRA (29-Dec-2025) as monitorable in
microfinance and secured business loans; and public listed history is
short. This is a Gate 0 mechanical screen only — flags propagate,
decision stays human.

---

## INPUT GAPS / DATA NOTES SUMMARY

- Sector_cap_row mislabeled "Pharma / CDMO" for an NBFC; corrected downstream (ignored here).
- Short public listed history (IPO 24-Sep-2024); flagged via history_downgrade.
- FY2018 annual data point absent from screener source (Data_Sheet.csv jumps FY2017→FY2019).
- E4 (contingent liabilities/net worth): not in provided data; would require Annual Report notes.
- M2, M5, M7, M9: PEER DATA NEEDED — no peer/competitor financials provided.
- M6: R&D/Revenue NOT FOUND.
- M11: FY2026 selling & admin expense line blank in source (NOT FOUND).
- ROCE (A1/A2/A4) is a computed NBFC proxy (Other Liabilities as Current Liabilities analogue), not a screener-native figure — stated explicitly throughout.

```yaml
stage: B01-gate0
company: "NORTHARC"
run_date: "2026-07-12"
model: claude-sonnet-5
status: complete
input_gaps: ["sector_cap_row mislabeled 'Pharma / CDMO' for an NBFC; corrected downstream", "short public history (IPO Sep-2024)", "FY2018 annual data point absent from screener source (gap between FY2017 and FY2019 columns)", "E4 contingent liabilities / net worth not in provided data (requires Annual Report notes)", "M2/M5/M7/M9 PEER DATA NEEDED - no peer financials provided", "M6 R&D/Revenue NOT FOUND", "M11 FY2026 selling and admin expense line blank in source"]
flags:
  - {type: FLAG-GATE0, reason: "Classification AVERAGE (adjusted-basis) driven by deal-breakers #1-4 (Block A<8, Block B<8, median ROCE<10%, cumulative CFO/PAT<0.50); all four depressors trace to NBFC-structural features (Ind AS liquidity-based balance sheet with no current-liabilities line distorting the ROCE proxy; loan-book-growth-driven negative CFO under Ind AS operating-activity classification of loan disbursements) rather than genuine earnings-quality deterioration. Raw literal core_score of 32/100 understates position because 20 of 80 nominal points (B4 WC-days, D4 current ratio, E2/E3 promoter change/pledge) are NOT APPLICABLE for this NBFC and scored 0 by convention; adjusted-basis score is 32/80 applicable points = 40%, the AVERAGE threshold."}
  - {type: FLAG-CASH, reason: "CFO negative in all 8 years with comparable data (FY2019-FY2026), cumulative CFO/PAT = -5.02x. Structural to a growing NBFC (loan disbursements classified as operating cash outflow under Ind AS as AUM grows 22% YoY), not a cash-conversion failure. Trend improving: CFO/PAT ratio moved from -6.92x (FY2024) to -3.44x (FY2025) to -3.79x (FY2026)."}
  - {type: FLAG-ASSET-QUALITY, reason: "PCR (computed from standalone Gross/Net stage 3 ratios) is ~47.8%, below the 60% adequacy threshold, despite low absolute NPAs (Gross 1.2%/Net 0.6%, FY2026). Gross Stage 3 rose from 0.5% (FY2024) to 1.2% (FY2026). ICRA (29-Dec-2025) flags increased stress in microfinance and secured business loan segments as monitorable."}
data_years: 9
fy_range: "FY2017 to FY2026"
blocks: {A: 3, B: 0, C: 18, D: 8, E: 3}
core_score: 32
moat_score: 10
grand_total: 42
moats_confirmed: 3
moat_class: "MODERATE"
classification: "AVERAGE"
deal_breakers:
  - "Block A <8 (raw=3) -> max GOOD [driven by FY2021 COVID-trough min ROCE 7.69% and structurally low NBFC ROCE proxy across FY2017-FY2026]"
  - "Block B <8 (raw=0) -> max GOOD [driven by CFO negative every year FY2019-FY2026, an Ind AS/loan-growth structural effect]"
  - "median ROCE <10% (9.62%, FY2017-FY2026) -> max AVERAGE [NBFC-structural, see Block A]"
  - "cumulative CFO/PAT <0.50 (-5.02x, FY2019-FY2026) -> max AVERAGE [NBFC-structural, see Block B]"
history_downgrade: true
data_notes: ["FY2018 data point absent from source; CAGR endpoints use elapsed time (2017-2026=9yr), unaffected", "ROCE (A1/A2/A4) computed via NBFC proxy: Capital Employed = Total Assets - 'Other Liabilities' (screener line), EBIT = PBT + Interest; not a screener-native ROCE figure", "ROE FY2017 and FY2019 use closing net worth only (no prior-year opening available / FY2018 gap), stated per formula rule; FY2026 computed ROE 11.08% reconciles closely to company-disclosed 11.1%, validating method", "FY2025 net worth base inflated ~54% by Sep-2024 IPO equity infusion, compressing computed FY2025 ROE relative to underlying profitability", "B4 WC Days marked NOT APPLICABLE (NBFC): core asset is Loans not trade receivables; screener Receivables line is trivial (~2.8 days-equivalent)", "D4 Current Ratio marked NOT APPLICABLE (NBFC) per company's own filing note that it is not applicable/relevant and hence not disclosed", "D3 Debt/Equity scored at framework's fixed 'Financials: default 3' regardless of the disclosed 3.13x ratio", "D2 PCR computed as (Gross Stage3-Net Stage3)/Gross Stage3 = 47.8% standalone (consol GNPA/NNPA basis gives ~50%); below 60% band despite low absolute NPAs", "E1 scored 3 under 'professionally managed, FII+DII>50%' rule: no promoter group; named institutional/FPI holders (LeapFrog, Augusta, Eight Roads, IFC, Accion, SMBC, Dvara Trust) sum to 56.5% as of Sep-2025 per ICRA", "E2/E3 marked NOT APPLICABLE: no promoter/promoter group exists for this professionally managed, PE/DFI-backed, Sep-2024 IPO-listed NBFC", "M2/M5/M7/M9 PEER DATA NEEDED, not a company deficiency", "M3 and M12 marked NOT APPLICABLE (NBFC): fixed-asset turnover and WC-days/float concepts have no analogue for a balance-sheet lender", "M4 and M10 scored 3 on a PARTIAL basis (revenue-growth component verified; receivable-days sub-condition NOT APPLICABLE and unverifiable) - lower confidence than M8", "M11 scored 1 on the growth criterion alone; FY2026 selling-expense-% trend unverifiable (source line blank)", "No loss-to-profit swings; PAT positive in all measured years", "core_score (32) is the literal raw sum of Blocks A-E with NOT APPLICABLE sub-items scored 0 by convention (20 of 80 nominal points); adjusted-basis score excluding those points is 32/80=40%, which supports the AVERAGE classification applied rather than a literal sub-40 AVOID reading, per operator instruction not to let NBFC-inapplicable ratios drag the score"]
block_b_trend: "improving - CFO/PAT ratio moved from -6.92x (FY2024) to -3.44x (FY2025) to -3.79x (FY2026), though structurally negative throughout due to 22% YoY AUM growth (loan disbursements booked as operating outflows under Ind AS)"
```
