# GATE 0 SCORECARD — OBSC Perfection Ltd (OBSCP)

Run date: 2026-07-12 | Model: claude-sonnet-5 | Stage: B01-gate0 | run_type: full

Data sources: screener.in CSV exports (screener-Data_Sheet.csv — primary
and ONLY populated screener file; screener-Profit_Loss.csv,
screener-Balance_Sheet.csv, screener-Cash_Flow.csv, screener-Quarters.csv,
screener-Customization.csv are blank export templates, no data rows) +
OBSC Perfection Ltd Annual Report FY25 (Annual_Report_2025.pdf),
standalone financial statements (Balance Sheet, Statement of P&L, Cash
Flow Statement, Notes 1-5) at pp.74-77 of the extracted range. results/
and rating/ folders are absent this run.

**Data available: 5 years (FY22 to FY26). Scoring adapted to 5-year
history.** All P&L and headline Balance Sheet figures are from
screener-Data_Sheet.csv (Report Dates 2022-03-31 through 2026-03-31, all
in Rs Cr). Certain balance-sheet-derived metrics (ROCE, Working Capital
Days, capex/FCF, Current Ratio) require a Current Liabilities / Trade
Payables split that screener's blank CSVs do not carry; this split is
anchored to the AR standalone Balance Sheet and Cash Flow Statement for
FY25 and FY24 only (the only two years the AR document covers). FY22,
FY23 and FY26 are marked NOT FOUND for those specific sub-metrics and
noted individually below.

**Critical source-integrity finding:** pages ~3-59 of the AR PDF (Notice
of AGM, Directors'/Board's Report, MGT-9 extract / shareholding pattern,
Corporate Governance Report, CSR Report) render with a corrupted font
encoding — every character is scrambled/unreadable in both text and
image extraction. Only the cover letter (pp.1-2) and the Independent
Auditor's Report + standalone financial statements + Notes 1-5 (pp.60-77)
are legible. This is in addition to the pre-flagged loss of AR pages
78-101. Consequence: promoter shareholding %, promoter pledge %, and
contingent liabilities (referenced as Note 29, beyond the legible range)
are NOT FOUND anywhere in the provided inputs. Block E is scored 0/20
entirely on this basis, not on adverse promoter conduct.

---

## BLOCK A: RETURN ON CAPITAL (15/20)

ROCE computed (screener provides no ROCE row; screener-Balance_Sheet.csv
"Return on Capital Emp" line is blank). ROCE = EBIT ÷ (Total Assets −
Current Liabilities); EBIT computed as PBT + Interest. Current
Liabilities are anchored only for FY24 and FY25 (AR Balance Sheet, p.[AR
BS p.1 of financial-statements section]); FY22, FY23, FY26 Current
Liabilities are NOT FOUND (screener-Balance_Sheet.csv blank; AR covers
only FY25 with FY24 comparative).

- FY24: EBIT = PBT 16.43 + Interest 2.69 = 19.12 Cr (screener-Data_Sheet,
  FY24 col). Capital Employed = Total Assets 86.50 − Current Liabilities
  29.22 (AR Balance Sheet as at 31.3.2024, comparative column) = 57.28 Cr.
  ROCE FY24 = 19.12 / 57.28 = **33.38%** (computed).
- FY25: EBIT = PBT 20.63 + Interest 3.12 = 23.75 Cr (screener-Data_Sheet,
  FY25 col). Capital Employed = Total Assets 158.55 − Current Liabilities
  33.61 (AR Balance Sheet as at 31.3.2025) = 124.94 Cr. ROCE FY25 = 23.75
  / 124.94 = **19.01%** (computed).
- FY22, FY23, FY26 ROCE: NOT FOUND (Current Liabilities split
  unavailable in provided data).

**A1 Median ROCE** (median of the only 2 anchored years = average =
26.20%): ≥25% band → **Score 5**. Caveat: based on 2 of 5 years only.

**A2 Minimum single-year ROCE** (min of 2 anchored years = 19.01%): ≥15%
band → **Score 5**.

**A3 Median ROE**: ROE = PAT ÷ average Net Worth (opening+closing)/2;
Net Worth = Equity Share Capital + Reserves (screener-Data_Sheet, all 5
years).
- FY22 Net Worth = 11.90+1.38 = 13.28 Cr. Opening (FY21) net worth NOT
  FOUND (data starts FY22) — closing NW used per rule. ROE FY22 =
  3.60/13.28 = 27.11% (closing-NW basis, stated).
- FY23 NW = 11.90+5.96 = 17.86. ROE = 4.57 / avg(13.28,17.86)=15.57 =
  29.35%.
- FY24 NW = 17.85+12.22 = 30.07. ROE = 12.21 / avg(17.86,30.07)=23.965 =
  50.95%.
- FY25 NW = 24.45+79.54 = 103.99. ROE = 16.76 / avg(30.07,103.99)=67.03 =
  25.01%.
- FY26 NW = 25.85+146.12 = 171.97. ROE = 27.01 / avg(103.99,171.97)=137.98
  = 19.58%.
  (all: screener-Data_Sheet, respective FY columns)
- Median (sorted 19.58, 25.01, 27.11, 29.35, 50.95) = **27.11%**. ≥20%
  band → **Score 5**.

**A4 ROCE trend, latest vs earliest**: only two ROCE data points exist
(FY24, FY25); used as the "latest vs earliest" pair since FY22/FY26 ROCE
is NOT FOUND. FY25 (19.01%) vs FY24 (33.38%) = decline of 14.37pp.
Decline >5pp → **Score 0**. (Note: FY25's capital base was inflated by a
57.16 Cr share-premium raise — screener-Data_Sheet FY25 Reserves jump
12.22→79.54 Cr — consistent with a post-listing capital-employed
step-up not yet earning a full return; see deal-breaker discussion
below.)

**Block A subtotal = 5+5+5+0 = 15/20**

---

## BLOCK B: CASH GENERATION QUALITY (1/20) — WEAKEST EVIDENCED BLOCK

**B1 Cumulative CFO ÷ Cumulative PAT** (all 5 years, both fully available
from screener-Data_Sheet):
- Cumulative CFO = 6.39+1.45+5.00+8.85+(−1.95) = 19.74 Cr.
- Cumulative PAT = 3.60+4.57+12.21+16.76+27.01 = 64.15 Cr.
- Ratio = 19.74/64.15 = **0.31**. <0.50 band → **Score 0**.

**B2 FCF-positive years as proportion**: FCF = CFO − Capex (purchase of
PPE+intangibles, ex-acquisitions). Capex only anchored for FY24 (Rs
1,052.69 lakh = 10.53 Cr, AR Cash Flow Statement 2023-24 column) and FY25
(Rs 3,326.99 lakh = 33.27 Cr, AR Cash Flow Statement 2024-25 column,
"Purchase of Fixed Assets" line). FY22/FY23/FY26 capex NOT FOUND
(screener-Cash_Flow.csv blank; not in AR range).
- FCF FY24 = 5.00 − 10.53 = **−5.53 Cr**.
- FCF FY25 = 8.85 − 33.27 = **−24.42 Cr**.
- Both of the 2 measurable years are negative → 0% positive. <50% band →
  **Score 0**.

**B3 Cumulative FCF ÷ Cumulative PAT** (matched FY24-FY25 window, the
only years with capex data): Cumulative FCF = −5.53+(−24.42) = −29.95 Cr.
Cumulative PAT (same window) = 12.21+16.76 = 28.97 Cr. Ratio = −1.03.
Negative → **Score 0**.

**B4 Change in WC Days, latest vs earliest** (measurable window FY24→
FY25 only; Trade Payables NOT FOUND for FY22/23/26):
- Receivable Days = Trade Receivables÷Revenue×365 (revenue basis).
  FY24 = 21.53/114.54×365 = 68.60 days; FY25 = 34.93/142.31×365 = 89.59
  days (screener-Data_Sheet Receivables & Sales rows).
- Inventory Days (revenue basis) FY24 = 14.91/114.54×365 = 47.51 days;
  FY25 = 26.69/142.31×365 = 68.46 days.
- Payable Days (revenue basis) FY24 = 11.59/114.54×365 = 36.93 days (AR
  BS Trade Payables FY24 comparative = Rs 1,159.21 lakh); FY25 =
  25.31/142.31×365 = 64.93 days (AR BS Trade Payables FY25 = Rs 2,530.87
  lakh).
- WC Days FY24 = 68.60+47.51−36.93 = 79.18. WC Days FY25 = 89.59+68.46−
  64.93 = 93.12. Change = **+13.94 days** (increase). 5-15 day increase
  band → **Score 1**.

**Block B subtotal = 0+0+0+1 = 1/20**

**block_b_trend = deteriorating.** Year-by-year CFO÷PAT (all
screener-Data_Sheet, computed): FY22 1.78x → FY23 0.32x → FY24 0.41x →
FY25 0.53x → FY26 **−0.07x**. The one number that shows it: FY26 CFO =
−1.95 Cr against FY26 PAT of +27.01 Cr (screener-Data_Sheet, FY26
column) — operating cash flow turned negative in the latest year despite
61% YoY PAT growth, driven by working-capital build (receivables 34.93→
66.08 Cr, inventory 26.69→47.18 Cr) and a capex-heavy investing program
(CFI −76.03 Cr in FY26).

---

## BLOCK C: GROWTH (20/20) — STRONGEST BLOCK

**C1 Revenue CAGR** (FY22 55.55 Cr → FY26 219.54 Cr, 4-year window,
screener-Data_Sheet): CAGR = (219.54/55.55)^(1/4) − 1 = **41.0%**. ≥20%
band → **Score 5**.

**C2 PAT CAGR** (FY22 3.60 Cr → FY26 27.01 Cr, screener-Data_Sheet): CAGR
= (27.01/3.60)^(1/4) − 1 = **65.4%**. ≥20% band → **Score 5**.

**C3 Positive YoY revenue years proportion**: FY22→23 (+), FY23→24 (+),
FY24→25 (+), FY25→26 (+) — all 4 transitions positive (screener-Data_
Sheet). 100% → **Score 5**.

**C4 PAT CAGR minus Revenue CAGR** = 65.4% − 41.0% = **+24.4pp**. ≥+3pp
band → **Score 5**.

**Block C subtotal = 5+5+5+5 = 20/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (16/20)

All "latest" figures use FY26 (screener-Data_Sheet) except D4, where
FY26 Current Liabilities is NOT FOUND, so D4 uses FY25 (the latest year
with an anchored Current Liabilities figure, AR Balance Sheet) — flagged
explicitly.

**D1 Net Debt ÷ EBITDA (latest, FY26)**: Net Debt = Borrowings 68.54 −
Cash & Bank 16.66 = 51.88 Cr. EBITDA = EBIT (PBT 31.77+Interest 4.49=
36.26) + Depreciation 7.38 = 43.64 Cr (all screener-Data_Sheet FY26).
Ratio = 51.88/43.64 = **1.19x**. 1-2x band → **Score 3**.

**D2 Interest Coverage, EBIT ÷ Interest (latest, FY26)**: 36.26/4.49 =
**8.08x**. 5-9.9x band → **Score 4**.

**D3 Debt ÷ Equity (latest, FY26)**: Borrowings 68.54 ÷ Net Worth 171.97
= **0.40**. 0.1-0.5x band → **Score 4**.

**D4 Current Ratio (latest anchored year, FY25 — not FY26, NOT FOUND for
FY26)**: Current Assets FY25 = Inventories 26.69 + Trade Receivables
34.93 + Cash & Cash Equivalents 16.60 + Short-term Loans & Advances 6.57
= 84.79 Cr (AR Balance Sheet as at 31.3.2025). Current Liabilities FY25 =
33.61 Cr (AR Balance Sheet, computed above). Ratio = 84.79/33.61 =
**2.52x**. ≥2.0x band → **Score 5**.

**Block D subtotal = 3+4+4+5 = 16/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (0/20) — DATA GAP, NOT ADVERSE FINDING

**E1 Promoter holding (latest quarter)**: N/A (not in provided data) —
not in screener CSVs (no shareholding rows populated); AR shareholding
tables sit in the corrupted-font page range (~pp.3-59). **Score 0**.

**E2 Promoter holding change over 3 years**: N/A (not in provided data).
**Score 0**.

**E3 Promoter pledge (latest)**: N/A (not in provided data). **Score 0**.

**E4 Contingent liabilities ÷ Net Worth (latest)**: N/A (not in provided
data) — Auditor's Report (p.4 of the audit report, "Report on other
legal and regulatory requirements") references "Note No. 29 to the
financial statements" for contingent liabilities / pending litigation
disclosure, but Notes only extend to Note 1-5 (accounting policies) in
the legible page range (AR pp.74-77, "Page 1 of 6" to "Page 4 of 6" of
the Notes section); Note 29 falls in the lost/unreadable range. **Score
0**.

**Block E subtotal = 0/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (14/60)

**M1 Pricing Power — Score 5.** EBITDA margin: FY22 7.27/55.55=13.09% →
FY26 43.64/219.54=19.88% (screener-Data_Sheet, computed), expansion of
+6.79pp (≥2pp) with revenue CAGR 41.0% (≥10%). Full-marks tier.

**M2 Cost Advantage vs peer median EBITDA margin — Score 0.** PEER DATA
NEEDED (no peer set provided this run).

**M3 Capital Efficiency — Score 3.** FAT (Sales÷Net Block) FY25 =
142.31/69.90 = 2.04x; ROCE FY25 = 19.01% (computed above). FAT>2x AND
ROCE>15% tier → Score 3 (falls short of FAT>3x AND ROCE>20% top tier).

**M4 Customer Stickiness — Score 3.** Zero revenue-decline years
(screener-Data_Sheet, all 4 YoY transitions positive), but receivable
days rose 21 days FY24→FY25 (68.60→89.59, computed above), failing the
"stable ±10" condition required for the top tier. Scored at the "max 1
decline year, fully recovered" tier (0 decline years trivially satisfies
"max 1").

**M5 Scale & Dominance — Score 0.** PEER DATA NEEDED.

**M6 Technology / R&D — Score 0.** R&D/Revenue disclosure NOT FOUND in
legible AR range or screener data; PEER DATA NEEDED for full test.

**M7 Regulatory / License — Score 0.** Business is unregulated precision
metal-component manufacturing for automotive (AR Note 1, "Corporate
Information," p.[AR Notes p.1 of 6]) — not a licensed/regulated segment
under this test's definition.

**M8 Distribution — Score 0.** Reach not quantified in provided data
(business description sections are in the corrupted-font page range).

**M9 Brand — Score 0.** Proxy used: GM = (Revenue − Raw Material Cost) ÷
Revenue (screener-Data_Sheet), stated proxy. FY22 34.11%, FY23 31.22%,
FY24 41.24%, FY25 45.42%, FY26 23.71% — FY26 shows an anomalous drop,
possibly a reclassification of "Purchases-Finished/Traded goods" into
the Raw Material Cost line (flagged in data_notes). No peer median
available to benchmark against → PEER DATA NEEDED, Score 0.

**M10 Switching Costs — Score 0.** Revenue grew every year (screener-
Data_Sheet), but receivable days rose 21 days over the FY24-FY25 window
(computed above), exceeding the ≤10-day threshold required at any
scoring tier; scored 0 per the "else" fallback.

**M11 Network Effects — Score 3 (scored conservatively, <6yr history, as
instructed).** Only 5 years of data available versus the 6 required for
the two-window CAGR test. Overall revenue CAGR 41.0% (≥20%) with Selling
& admin expense as % of revenue declining across the years with data:
FY22 4.45%, FY23 4.08%, FY24 3.84%, FY25 3.79% (screener-Data_Sheet;
FY26 Selling and admin is blank/NOT FOUND in the source). Scored at the
"rev CAGR≥20% AND selling% stable/declining" tier.

**M12 Negative WC / Float — Score 0.** WC Days FY24=79.18, FY25=93.12
(computed above, only measurable years) — both >45 days. Score 0.

**Block F subtotal = 5+0+3+3+0+0+0+0+0+0+3+0 = 14/60**

**Moats "present" (score ≥3): M1, M3, M4, M11 = 4 tests.**
**Moat classification: 4-5 present = STRONG.**

```
Moat profile (0-5 each):
M1  [#####] 5  Pricing Power
M2  [.....] 0  Cost Advantage        (PEER DATA NEEDED)
M3  [###..] 3  Capital Efficiency
M4  [###..] 3  Customer Stickiness
M5  [.....] 0  Scale & Dominance     (PEER DATA NEEDED)
M6  [.....] 0  Technology / R&D      (NOT FOUND / PEER DATA NEEDED)
M7  [.....] 0  Regulatory / License
M8  [.....] 0  Distribution          (NOT FOUND)
M9  [.....] 0  Brand                 (PEER DATA NEEDED)
M10 [.....] 0  Switching Costs
M11 [###..] 3  Network Effects       (conservative, <6yr history)
M12 [.....] 0  Negative WC / Float
```

---

## CLASSIFICATION

Core Score = A(15) + B(1) + C(20) + D(16) + E(0) = **52/100**
Moat Score = **14/60**
Grand Total = 52 + 14 = **66/100**
Moats confirmed = 4 → **STRONG**

Data confidence: 5 years (FY22-FY26) → "5-6 lower" tier → flag "may not
have seen full cycle" (no automatic classification downgrade at this
tier). history_downgrade = false.

Classification matrix: Core 52 falls in the 40-59 band → **AVERAGE**,
irrespective of the STRONG moat class (moat only elevates classification
at Core ≥60).

**Deal-breaker overrides checked:**
1. Block A <8 → max GOOD: Block A=15, not triggered.
2. Block B <8 → max GOOD: **Block B=1, TRIGGERED** — non-binding (base
   classification AVERAGE is already below the GOOD cap).
3. Median ROCE <10% → max AVERAGE: median ROCE=26.2%, not triggered.
4. Cumulative CFO/PAT <0.50 → max AVERAGE: **0.31 <0.50, TRIGGERED** —
   binding, consistent with base classification. Years driving this:
   weak conversion is broad-based (FY23 0.32x, FY24 0.41x) and turns
   outright negative in FY26 (CFO −1.95 Cr) on the back of a working-
   capital build and a capex-heavy plant-expansion cycle (AR Note 1
   references a third Pune unit starting production in FY25; FY26 CFI
   = −76.03 Cr, screener-Data_Sheet).
5. Pledge >15% → max AVERAGE: pledge NOT FOUND, cannot evaluate.
6. ND/EBITDA >3x AND IC <3x → AVOID: 1.19x / 8.08x, not triggered.
7. Revenue declined majority of years → max AVERAGE: not triggered (all
   4 years grew).
8. PAT negative in any of last 3 years → max AVERAGE: not triggered (PAT
   positive and growing every year).
9. History <3 years → AVERAGE: 5 years available, not triggered.

**Final classification: AVERAGE**

Strongest block: **C — Growth (20/20)**, revenue CAGR 41.0% and PAT CAGR
65.4% over FY22-FY26, both fully anchored across 5 years.

Weakest evidenced block: **B — Cash Generation Quality (1/20)**,
cumulative CFO/PAT of 0.31x and a deteriorating CFO/PAT trend that turned
negative in FY26 despite strong reported profit growth. (Block E is
numerically lower at 0/20 but reflects a data-access gap, not adverse
evidence — see note above.)

**Decision line:** OBSCP screens AVERAGE on Gate 0, driven by a hard
cash-conversion deal-breaker (cumulative CFO/PAT 0.31x, block B=1/20)
against otherwise strong, fully-anchored top-line and bottom-line growth
(Block C=20/20) and a comfortable, low-leverage balance sheet (Block
D=16/20, Net Debt/EBITDA 1.19x). Block E (shareholder alignment) is
entirely unscored due to a source-document integrity failure (corrupted
AR page range ~3-59) rather than any evidenced governance concern — this
must be closed with an alternate source (exchange shareholding filing)
before this name proceeds past Gate 0 with confidence. Flags propagate;
no STOP verdict is issued at this stage.

---

## INPUT GAPS CARRIED FORWARD

- results/ absent — Gate 0 built from screener CSVs + AR statements.
- rating/ absent.
- AR pages 78-101 lost (truncated download); detailed notes schedules
  (including Note 29, contingent liabilities) unavailable.
- AR pages ~3-59 (Board's Report, MGT-9/shareholding pattern, Corporate
  Governance Report, CSR Report) render with corrupted font encoding —
  unreadable in both text and image form; promoter holding, promoter
  pledge, and business/segment qualitative detail NOT FOUND as a result.
- screener-Profit_Loss.csv, screener-Balance_Sheet.csv,
  screener-Cash_Flow.csv, screener-Quarters.csv are blank export
  templates (no data rows); all screener-sourced figures in this report
  come from screener-Data_Sheet.csv only.
