# STAGE 1: GATE 0 SCORECARD — QMS Medical Allied Services Ltd (QMSMEDI)
Run date: 2026-09-26

Data available: 8 years (FY19 to FY26) on the STANDALONE screener series (FY18
excluded as a pre-operational stub year, sales Rs 0.08 Cr) (screener-standalone-Profit_Loss.csv).
Scoring adapted to 8-year history (confidence tier "7-9 moderate", no downgrade).

BASIS NOTE (binding on every number below): consolidated statements exist
only for FY24-FY26 (Saarathi Healthcare subsidiary acquired Jul-2024)
(B00-inputs.yaml). Blocks A, B and C (return, cash, growth) are computed on
the STANDALONE series (screener-standalone-*.csv) because it gives 8 years
against the consolidated 3, per the run's BASIS NOTE instruction to use
standalone for backward history. Block D (balance-sheet strength) uses the
CONSOLIDATED FY26 balance sheet (screener-Balance_Sheet.csv; Annual_Report_2026.txt
pp.125-127) because that is the audited state of the group as it exists
today, including Saarathi's debt. Block E (shareholder alignment) is
basis-neutral (shareholding XBRL, entity-level). Each number below states
its basis.

---

## BLOCK A: RETURN ON CAPITAL (STANDALONE, FY19-FY26) — Max 20

Source ROCE and ROE are the screener's own figures (screener-standalone-Data_Sheet.csv,
rows "Return on Capital Emp" / "Return on Equity"), used directly per the
formula rule that a provided ROCE/ROE need not be recomputed.

| FY | ROCE | ROE |
|----|------|-----|
| FY19 | 120.52% | 99.68% |
| FY20 | 64.80% | 67.16% |
| FY21 | 53.54% | 53.74% |
| FY22 | 32.84% | 34.45% |
| FY23 | 13.84% | 9.06% |
| FY24 | 17.39% | 11.46% |
| FY25 | 16.56% | 11.84% |
| FY26 | 9.62% | 6.42% |

(screener-standalone-Data_Sheet.csv, "Return on Capital Emp" / "Return on Equity" rows)

**A1 Median ROCE = 25.12%** (average of the 4th/5th sorted values, 17.39%
and 32.84%) (screener-standalone-Data_Sheet.csv) → band ≥25% → **score 5**.
FLAG: this median is carried entirely by FY19-FY22, when the standalone
entity had a net worth under Rs 35 Cr (screener-standalone-Balance_Sheet.csv,
"Total" row); it does not reflect the business the company runs today.

**A2 Minimum single-year ROCE = 9.62% (FY26)** (screener-standalone-Data_Sheet.csv)
→ band 8-11.9% → **score 1**.

**A3 Median ROE = 23.15%** (average of 11.84% and 34.45%) (screener-standalone-Data_Sheet.csv)
→ band ≥20% → **score 5**. Same FLAG as A1: FY19-FY22 pre-scale years
dominate the median; FY26 ROE is 6.42%.

**A4 ROCE trend, FY26 vs FY19: 9.62% vs 120.52%, decline of 110.9pp**
(screener-standalone-Data_Sheet.csv) → band decline >5pp → **score 0**.

**Block A total: 11/20.** A1 and A3 are inflated by inception-scale years;
A2 and A4 capture the current, much weaker, run rate. Downstream stages
should read A1/A3 as an artefact, not evidence of a 25%+ ROCE business.

---

## BLOCK B: CASH GENERATION QUALITY — Max 20 (STANDALONE)

CFO and PAT, FY19-FY26 (screener-standalone-Cash_Flow.csv, screener-standalone-Profit_Loss.csv):

| FY | CFO (Cr) | PAT (Cr) |
|----|----------|----------|
| FY19 | 0.26 | 3.07 |
| FY20 | 4.18 | 6.32 |
| FY21 | 1.88 | 10.92 |
| FY22 | -1.72 | 10.69 |
| FY23 | -7.54 | 6.38 |
| FY24 | 1.36 | 9.00 |
| FY25 | 26.09 | 10.42 |
| FY26 | 18.77 | 6.69 |

Cumulative CFO = 43.28 Cr; Cumulative PAT = 63.49 Cr (screener-standalone-Cash_Flow.csv,
screener-standalone-Profit_Loss.csv, summed FY19-FY26).

**B1 Cumulative CFO / Cumulative PAT = 43.28 / 63.49 = 0.68** → band
0.50-0.69 → **score 1**.

**B2 and B3 (FCF-based): capex is NOT FOUND as a clean standalone line item
for FY19-FY24** (screener cash-flow exports carry only aggregate "Cash
from Investing Activity", which mixes fixed-deposit and subsidiary-investment
movements; the underlying capex sub-line is not broken out for those years
in the provided screener data). Capex IS available for FY25 and FY26 from
the standalone cash-flow statement's "Payment made to creditors towards
purchase of assets" line (Annual_Report_2026.txt p.97: Rs 308.16 lakh
FY25, Rs 554.29 lakh FY26 = Rs 3.08 Cr / Rs 5.54 Cr). Computed for those
two years only (NOT the full 8-year window used elsewhere in this block):
- FCF FY25 = CFO 26.09 - Capex 3.08 = 23.01 Cr
- FCF FY26 = CFO 18.77 - Capex 5.54 = 13.23 Cr

**B2 FCF-positive years, FY25-FY26 window = 2/2 = 100%** → **score 5**
(2-year sample; FY19-FY24 marked N/A, not in provided data).

**B3 Cumulative FCF / Cumulative PAT, FY25-FY26 window = 36.24 / 17.11 =
2.12** → band ≥0.60 → **score 5** (same 2-year-sample caveat).

**B4 Working-capital days:** Payable Days needs Trade Payables, not in the
screener exports; pulled from the AR note (Annual_Report_2026.txt p.95
standalone, p.125 consolidated). Only FY25 and FY26 are available (older
ARs not in this corpus), so this is a 1-year change, not the 8-year
window:
- FY25 standalone: Receivable Days 135.83 (Debtors 53.82 / Sales 144.64 x
  365), Inventory Days 99.13 (Inventory 39.28 / Sales 144.64 x 365, revenue
  basis), Payable Days 41.82 (Trade Payables 16.57 Cr / Sales 144.64 x
  365). WC Days = 193.14.
- FY26 standalone: Receivable Days 141.96, Inventory Days 110.15, Payable
  Days 43.18 (Trade Payables 18.00 Cr). WC Days = 208.93.
(screener-standalone-Balance_Sheet.csv for Debtors/Inventory/Sales;
Annual_Report_2026.txt p.95 for Trade Payables FY26/FY25 standalone,
Rs 208.64 lakh + Rs 1,591.75 lakh = Rs 1,800.39 lakh FY26; Rs 132.76 lakh +
Rs 1,524.64 lakh = Rs 1,657.40 lakh FY25.)

**B4 Change = +15.79 days (FY25→FY26 only)** → band increase >15 →
**score 0**.

**Block B total: 11/20.** block_b_trend = **deteriorating**: standalone
CFO fell from Rs 26.09 Cr (FY25) to Rs 18.77 Cr (FY26), -28% YoY
(screener-standalone-Cash_Flow.csv), while PAT fell from Rs 10.42 Cr to
Rs 6.69 Cr, -36% YoY, and WC days rose 15.8 days in the same year.

---

## BLOCK C: GROWTH (STANDALONE, FY19-FY26, 7-year CAGR span) — Max 20

Revenue: FY19 Rs 51.89 Cr → FY26 Rs 152.13 Cr (screener-standalone-Profit_Loss.csv).
PAT: FY19 Rs 3.07 Cr → FY26 Rs 6.69 Cr (screener-standalone-Profit_Loss.csv).

**C1 Revenue CAGR = (152.13/51.89)^(1/7) - 1 = 16.61%** → band 15-19.9% →
**score 4**.

**C2 PAT CAGR = (6.69/3.07)^(1/7) - 1 = 11.77%** → band 10-14.9% →
**score 3**.

**C3 Positive YoY revenue years: 6 of 7 (FY23 declined, Rs 146.32 Cr →
Rs 103.94 Cr; all other years grew)** (screener-standalone-Profit_Loss.csv)
= 85.7% → band 75-99% → **score 3**.

**C4 PAT CAGR minus Revenue CAGR = 11.77% - 16.61% = -4.84pp** → band -3
to -8pp → **score 1**.

**Block C total: 11/20.** Deal-breaker 7 (revenue declined majority of
years) NOT triggered: 1 of 7 years, not a majority.

---

## BLOCK D: BALANCE SHEET STRENGTH (CONSOLIDATED, FY26 latest) — Max 20

FY26 consolidated figures (screener-Balance_Sheet.csv, screener-Profit_Loss.csv,
cross-checked to Annual_Report_2026.txt pp.125-127):
- Total borrowings Rs 74.48 Cr (Long-term Rs 6.97 Cr + Short-term Rs 67.51
  Cr, AR p.125) (screener-Balance_Sheet.csv, "Borrowings" FY26)
- Cash and cash equivalents Rs 1.20 Cr (AR p.126, Note 16, Rs 119.54 lakh)
- EBITDA (Operating Profit) Rs 25.88 Cr (screener-Profit_Loss.csv, FY26)
- PBT Rs 16.44 Cr, Interest Rs 6.55 Cr (screener-Profit_Loss.csv, FY26);
  EBIT = PBT + Interest = Rs 22.99 Cr
- Net worth (parent) Rs 104.20 Cr (Equity Cap 19.34 + Reserves 84.86)
  (screener-Balance_Sheet.csv, FY26)
- Current assets Rs 142.01 Cr, current liabilities Rs 92.28 Cr (AR p.125-126,
  Notes 5-8 and 13-18, summed)

**D1 Net Debt / EBITDA = (74.48 - 1.20) / 25.88 = 2.83x** → band 2-3x →
**score 1**.

**D2 Interest Coverage = EBIT / Interest = 22.99 / 6.55 = 3.51x** → band
3-4.9x → **score 2**.

**D3 Debt / Equity = 74.48 / 104.20 = 0.71x** → band 0.5-1.0x → **score 3**.

**D4 Current Ratio = 142.01 / 92.28 = 1.54x** → band 1.5-1.99x →
**score 4**.

**Block D total: 10/20.** Deal-breaker 6 (ND/EBITDA >3x AND IC <3x) NOT
triggered (2.83x and 3.51x), but both ratios sit one notch from the
threshold; this matches the run's LBF2 load-bearing fact (interest cover
3.5x vs 5.0x prior year) (B00-inputs.yaml).

---

## BLOCK E: SHAREHOLDER ALIGNMENT — Max 20

**E1 Promoter holding, latest quarter (30-Jun-2026) = 68.11%**
(QMSMEDI-SHP-2026-06-30-NSE.xml, ShareholdingOfPromoterAndPromoterGroup)
→ band ≥60% → **score 5**.

**E2 Promoter holding change: 73.67% (30-Jun-2025) → 68.11% (30-Jun-2026),
change = -5.56pp** (QMSMEDI-SHP-2025-06-30-NSE.xml,
QMSMEDI-SHP-2026-06-30-NSE.xml) → band decreased >3% → **score 0**. Note:
this is a ONE-YEAR change, not 3 years (company's listed history is short);
the decline is attributable to the Sep-2025 rights issue diluting the base
(B00-inputs.yaml LBF3/BASIS), not a promoter sale — the rights-issue
mechanic should be checked before reading this as a stewardship flag.

**E3 Promoter pledge, latest = 0%** (QMSMEDI-SHP-2026-06-30-NSE.xml,
WhetherAnySharesHeldByPromotersAreEncumberedUnderPledged = false; same
false at 30-Jun-2025) → **score 5**.

**E4 Contingent liabilities / Net worth: N/A (not in provided data).**
No "Contingent Liabilities" note found in either Annual_Report_2026.txt or
Annual_Report_2025.txt (full-text search, no match) → **score 0**.

**Block E total: 10/20.** Deal-breaker 5 (pledge >15%) NOT triggered.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (STANDALONE, FY19-FY26) — Max 60

| Test | Score | Basis |
|------|-------|-------|
| M1 Pricing Power | 5 | OPM 8.98% (FY19) → 13.48% (FY26), +4.5pp, rev CAGR 16.6% ≥10% (screener-standalone-Data_Sheet.csv, "OPM" row). FLAG: OPM fell FY25→FY26 (16.12%→13.48%, -2.64pp), the mechanical test uses the full-period endpoints and misses this reversal. |
| M2 Cost Advantage vs peer | 0 | PEER DATA NEEDED — no peer EBITDA-margin data in this stage's input set |
| M3 Capital Efficiency | 0 | FAT (FY26) = Sales 152.13 / Net Block 24.66 = 6.17x (>3x), but ROCE FY26 = 9.62% (<12%), so no threshold clears (screener-standalone-Balance_Sheet.csv, Data_Sheet.csv) |
| M4 Customer Stickiness | 3 | 1 revenue-decline year (FY23), fully recovered by FY26 (Rs 152.13 Cr > FY22 peak Rs 146.32 Cr) (screener-standalone-Profit_Loss.csv) |
| M5 Scale & Dominance | 0 | PEER DATA NEEDED — no peer market-cap/margin ranking in this stage's input set |
| M6 Technology / R&D | 0 | No R&D line disclosed in the P&L; NOT FOUND |
| M7 Regulatory / License | 0 | No listed-player-count data for the segment provided; NOT FOUND |
| M8 Distribution | 0 | No quantified distribution-reach metric in the provided data; NOT FOUND |
| M9 Brand | 0 | PEER DATA NEEDED for gross-margin comparison. GM proxy (Revenue - Material Cost)/Revenue computed for reference only: FY26 = (152.13 - 103.09)/152.13 = 32.2% (Raw Material Cost Rs 95.53 Cr + Change in Inventory Rs 7.56 Cr, screener-standalone-Data_Sheet.csv); no peer median to compare against |
| M10 Switching Costs | 0 | 1 decline year but receivable days rose from 56 to 142 (not stable); does not clear the "growth all but 1 year AND stable" tier nor the "2+ decline years" tier |
| M11 Network Effects | 0 | Latest-3yr rev CAGR (FY23→FY26) 13.54% vs prior-3yr (FY20→FY23) 12.62% is higher, but selling-expense % of sales rose (4.85% FY23 → 6.83% FY26, screener-standalone-Data_Sheet.csv), failing the "selling % declining/stable" condition on every tier that would otherwise score |
| M12 Negative WC / Float | 0 | WC Days 193 (FY25) and 209 (FY26), far above the 45-day ceiling (see Block B4) |

**Moat score: 8/60. Moats present (score ≥3): M1, M4 = 2. Moat
classification: 2-3 present = MODERATE.**

Four tests (M2, M5, M9 partially, and the peer leg of M6/M7) are capped by
"PEER DATA NEEDED": this stage's input set carries no peer (INDGN/ENTERO/
POLYMED) financial data, though such files exist elsewhere in the run's
corpus per B00-inputs.yaml; they were not part of this stage's injected
inputs and are not used here.

---

## CLASSIFICATION

Data confidence: 8 years (FY19-FY26 standalone) → "7-9 moderate" tier, no
downgrade (history_downgrade = false).

| Block | Score | Max |
|-------|-------|-----|
| A Return on Capital | 11 | 20 |
| B Cash Generation | 11 | 20 |
| C Growth | 11 | 20 |
| D Balance Sheet | 10 | 20 |
| E Shareholder Alignment | 10 | 20 |
| **Core total** | **53** | **100** |
| F Moat | 8 | 60 |
| **Grand total** | **61** | **160** |

Moat classification: MODERATE (2 of 12 tests present, M1 and M4).

Deal-breaker check (all 9 tested, none triggered):
1. Block A (11) not <8. 2. Block B (11) not <8. 3. Median ROCE (25.12%,
mechanically computed, see FLAG above) not <10%. 4. Cumulative CFO/PAT
(0.68) not <0.50. 5. Pledge (0%) not >15%. 6. ND/EBITDA (2.83x) not >3x
AND IC (3.51x) not <3x — both close to the line. 7. Revenue declined in 1
of 7 years, not a majority. 8. PAT positive in all of FY24/FY25/FY26
standalone (Rs 9.00 / Rs 10.42 / Rs 6.69 Cr). 9. History is 8 years, not
<3.

**Classification matrix: Core 40-59 → AVERAGE** (this band is AVERAGE
regardless of moat tier per the matrix).

**Strongest block:** Block A and Block C, tied at 11/20 — but Block A's
strength is an artefact of pre-scale years (see FLAG); Block C (growth) is
the more genuine strength, with 16.6% revenue CAGR and only one down year
in eight.

**Weakest block:** Block D (Balance Sheet Strength), 10/20 — interest
cover 3.51x and Net Debt/EBITDA 2.83x both sit one band above the
deal-breaker line, and this is on the FY26 CONSOLIDATED figures that
already include the Saarathi acquisition debt.

**DECISION LINE: CLASSIFICATION = AVERAGE.** Core score 53/100 sits inside
the flat AVERAGE band. The scorecard shows a business that grew revenue at
16.6% CAGR over 8 years with only one down year, but whose current-year
(FY26) returns (ROCE 9.62%, ROE 6.42%), cash trend (CFO -28% YoY, PAT -36%
YoY, WC days +15.8), and leverage (interest cover 3.51x) are all weaker
than the multi-year averages suggest. The A-block median scores (A1, A3)
are inflated by tiny-base years and should not be read as evidence of a
strong-ROCE business; the FY26 run rate is what should govern downstream
position sizing. No deal-breaker fired. This is a mechanical read only;
company-quality judgment happens downstream, never here.

---

## DATA GAPS (marked N/A / PEER DATA NEEDED per rule 5, never estimated)
- Capex, FY19-FY24 standalone: not broken out in screener cash-flow
  exports; B2/B3 computed on FY25-FY26 only.
- Trade Payables, FY19-FY24: not in screener exports; B4 computed on
  FY25-FY26 only (1-year change, not 8-year).
- Contingent Liabilities: no note found in Annual_Report_2026.txt or
  Annual_Report_2025.txt; E4 = N/A, scored 0.
- Peer (INDGN/ENTERO/POLYMED) financial data: not part of this stage's
  injected input set; M2, M5, and the peer leg of M9 = PEER DATA NEEDED,
  scored 0.
- R&D disclosure, distribution-reach metrics, segment player-count: not
  disclosed anywhere in the provided data; M6, M7, M8 = NOT FOUND, scored 0.
