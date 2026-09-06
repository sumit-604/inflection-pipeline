# STAGE 1: GATE 0 QUANTITATIVE SCORECARD
Cyient DLM Ltd (CYIENTDLM) | Run date: 2026-09-06 | Model: claude-sonnet-5

Data available: 4 years (FY2023 to FY2026), consolidated, from screener-Data_Sheet.csv.
Scoring adapted to 4-year history. No prospectus in corpus (company listed
FY2023-24; no restated pre-IPO financials). Supplementary company-disclosed
KPI series (revenue, EBITDA, PAT, ROCE%, NWC days, order book) reach back to
FY2022 in AR FY2025-26 p.27 and AR FY2024-25 p.69; these are used only where
explicitly noted, never to replace the declared 4-year scoring window.

Screener Data Sheet figures cross-checked and confirmed CONSOLIDATED
(total assets, CFO, capex, PAT all tie to the AR FY2025-26 consolidated
financial statements, e.g. Total assets FY2026 = Rs 16,421.86 mn = Rs
1,642.19 cr matches screener-Data_Sheet.csv exactly).

CMP = Rs 856.95, Market Cap = Rs 6,802.76 cr, Face Value = Rs 10
(screener-Data_Sheet.csv, header rows).

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

ROCE is company-disclosed (source provides its own figure; used per rule,
not independently computed). Source: AR FY2025-26 p.27, five-year KPI
chart "ROCE (%)" (consolidated): FY2022 18%, FY2023 13%, FY2024 11%,
FY2025 11%, FY2026 11.4%. Cross-checked against AR FY2024-25 p.69 (same
chart, FY2021-25 window: FY2021 11%, FY2022 18%, FY2023 13%, FY2024 11%,
FY2025 11%) and AR FY2024-25 p.73 MD&A "Key financial ratios" table
(FY2025 ROCE% = 11.4%, FY2024 ROCE% = 10.6%) — consistent.

ROE computed per fixed formula (PAT / average Net Worth; FY2023 uses
closing Net Worth, opening not available):
- Net Worth (screener-Data_Sheet.csv, Equity Share Capital + Reserves):
  FY2023 = 197.88 cr, FY2024 = 908.98 cr, FY2025 = 949.44 cr,
  FY2026 = 1,012.10 cr
- PAT (screener-Data_Sheet.csv): FY2023 = 31.73 cr, FY2024 = 61.20 cr,
  FY2025 = 68.08 cr, FY2026 = 73.28 cr
- ROE FY2023 = 31.73/197.88 = 16.04% (closing NW basis, stated)
- ROE FY2024 = 61.20/553.43 = 11.06% (cf. AR FY2024-25 p.73 MD&A: 11.1%)
- ROE FY2025 = 68.08/929.21 = 7.33% (cf. AR FY2024-25 p.73 MD&A: 7.3%)
- ROE FY2026 = 73.28/980.77 = 7.47% (AR FY2025-26 standalone Note 35,
  p.136, shows ROE 6% on a Tangible-Net-Worth-plus-debt/standalone basis;
  our figure is consolidated per the fixed formula, computed)

**A1 Median ROCE**: values 13, 11, 11, 11.4 (FY23-26) -> median = 11.2%.
Band 10-14.9% = **1** (screener/AR-derived, AR FY2025-26 p.27)

**A2 Minimum single-year ROCE**: min = 11% (FY2024 and FY2025). Band
8-11.9% = **1** (AR FY2025-26 p.27)

**A3 Median ROE**: values 16.04, 11.06, 7.33, 7.47 -> median = 9.27%.
Band <12% = **0** (computed, screener-Data_Sheet.csv)

**A4 ROCE trend, latest (FY26=11.4%) vs earliest (FY23=13%)**: decline
1.6pp. Band decline 1-3pp = **3** (AR FY2025-26 p.27)

**BLOCK A SUBTOTAL: 5 / 20**

Flag for context (not scored, outside declared 4-yr window): on the fuller
5-year company-disclosed series (FY2022=18% to FY2026=11.4%), ROCE
declined 6.6pp, which would score A4 = 0 under the ">5pp decline" band.
The 4-year window used for scoring (FY23-26) understates the peak-to-now
decline because FY2022 (pre-large-capex, pre-IPO) is excluded from the
declared data window. AR FY2025-26 p.27 narrative: "ROCE remained subdued
during FY 2023-26, primarily due to investments in net working capital
and capital expenditure to support future growth."

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

CFO (screener-Data_Sheet.csv, "Cash from Operating Activity", confirmed
against AR FY2025-26 consolidated cash flow statement p.145-146 and AR
FY2024-25 consolidated cash flow statement p.235):
FY2023 = 53.96 cr, FY2024 = -70.54 cr, FY2025 = -62.39 cr,
FY2026 = 53.90 cr.

Capex (Purchase of PPE + intangibles, consolidated cash flow statement;
excludes the FY2025 acquisition-of-business outflow of Rs 1,158.80 mn per
instruction): FY2024 = 33.771 cr (AR FY2024-25 p.235, comparative col),
FY2025 = 50.01 cr (AR FY2024-25 p.235 and AR FY2025-26 p.145, comparative
col), FY2026 = 44.663 cr (AR FY2025-26 p.145). **FY2023 capex is NOT
FOUND** — no AR2024 in corpus (prospectus/AR FY2023-24 both ABSENT per
B00 gaps) and screener-Data_Sheet.csv gives only aggregate "Cash from
Investing Activity" (-141.84 cr), which is not capex alone and was not
used per the never-estimate rule.

FCF = CFO - Capex: FY2024 = -70.54 - 33.771 = -104.31 cr,
FY2025 = -62.39 - 50.01 = -112.40 cr, FY2026 = 53.90 - 44.663 = +9.24 cr.
FY2023 FCF = NOT FOUND (capex missing).

**B1 Cumulative CFO / Cumulative PAT** (4 years, all data available):
Cumulative CFO = 53.96 - 70.54 - 62.39 + 53.90 = -25.07 cr.
Cumulative PAT = 31.73+61.20+68.08+73.28 = 234.29 cr.
Ratio = -0.11 (negative). Band <0.50 = **0**
(screener-Data_Sheet.csv; AR FY2025-26 p.145-146)

**B2 FCF-positive years as proportion** (3 years usable: FY24-26, FY23
excluded, capex NOT FOUND): 1 of 3 positive (FY2026) = 33%. Band <50% =
**0** (AR FY2024-25 p.235; AR FY2025-26 p.145)

**B3 Cumulative FCF / Cumulative PAT** (matched 3-year window FY24-26 for
both numerator and denominator, since FY23 FCF is not computable):
Cumulative FCF = -104.31-112.40+9.24 = -207.47 cr.
Cumulative PAT (FY24-26 only) = 61.20+68.08+73.28 = 202.56 cr.
Ratio = -1.02 (negative). Band <0.20 or negative = **0**

**B4 Change in WC Days, latest vs earliest**: used the company's own
disclosed "Net Working Capital (Days)" KPI (AR FY2025-26 p.27,
consolidated) rather than a formula rebuild, because Trade Payables were
not available in screener-Data_Sheet.csv for all four years (needed for
the Receivable+Inventory-Payable formula). FY2023 = 48 days, FY2026 = 145
days. Change = +97 days. Band increased >15 = **0**
(AR FY2025-26 p.27; cross-checked partially against AR FY2024-25 p.73
MD&A DSO/DIO/DPO table: FY2024 DSO 57 + DIO 117 - DPO 70 = 104 days,
FY2025 DSO 69 + DIO 171 - DPO 92 = 148 days — same direction, magnitude
differs from the KPI-chart NWC-days metric, likely a different netting
convention; both confirm a large working-capital deterioration FY24-25.)

**BLOCK B SUBTOTAL: 0 / 20**

Driver years for the Block B collapse: FY2024 (CFO -70.54 cr) and FY2025
(CFO -62.39 cr), both explained in AR FY2024-25 p.69/p.73 as
receivables-and-inventory buildup tied to large-deal execution and
post-IPO capacity investment, not to core margin deterioration. FY2026
CFO recovered to +53.90 cr. This is the kind of "documented post-IPO
rebase" pattern the operating rules flag as a candidate for downstream
position-sizing override of a mechanical AVERAGE/AVOID score — recorded
here, not resolved here.

**block_b_trend: improving** — CFO swung from -Rs 62.39 cr (FY2025) to
+Rs 53.90 cr (FY2026), a Rs 116.29 cr YoY swing, though cumulative
FY2023-26 CFO remains negative (-Rs 25.07 cr) against cumulative PAT of
+Rs 234.29 cr (screener-Data_Sheet.csv).

---

## BLOCK C: GROWTH (Max 20)

Revenue (screener-Data_Sheet.csv): FY2023 = 832.03 cr, FY2024 = 1,191.87
cr, FY2025 = 1,519.63 cr, FY2026 = 1,261.49 cr.
PAT (screener-Data_Sheet.csv): FY2023 = 31.73 cr, FY2024 = 61.20 cr,
FY2025 = 68.08 cr, FY2026 = 73.28 cr.

**C1 Revenue CAGR** (FY23->FY26, 3-year period): (1,261.49/832.03)^(1/3)-1
= 14.9%. Band 10-14.9% = **3**

**C2 PAT CAGR** (FY23->FY26): (73.28/31.73)^(1/3)-1 = 32.2%. Both
endpoints positive, no swing. Band >=20% = **5**

**C3 Positive YoY revenue years / total YoY periods**: FY24 vs FY23
+43.2% (positive), FY25 vs FY24 +27.5% (positive), FY26 vs FY25 -17.0%
(negative). 2 of 3 = 66.7%. Band 50-74% = **1**

**C4 PAT CAGR minus Revenue CAGR**: 32.2 - 14.9 = +17.3pp. Band >=+3pp =
**5**

**BLOCK C SUBTOTAL: 14 / 20**

Data quality flag on C2/C4: AR FY2025-26 p.27 states reported PAT
FY2026 grew 7.6% YoY "driven by the reversal of one-off earn-out
provisions recognized during the year," while normalized PAT declined
24% YoY on a lower revenue base. The PAT CAGR feeding C2 and C4 therefore
includes a material non-operating tailwind in the terminal year; on a
normalized basis the growth picture (C2/C4) would be materially weaker.
This is not re-scored (screener PAT is the fixed-formula input) but is
flagged as a distortion the downstream stages must weigh.

Deal-breaker #7 check: revenue declined in 1 of 3 periods (FY26), not a
majority — does not trigger.

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY2026)

Consolidated balance sheet, AR FY2025-26 p.142-143 (confirmed to tie to
screener-Data_Sheet.csv Total Assets exactly):
Total current assets = Rs 12,223.01 mn, Total current liabilities =
Rs 4,915.73 mn.
Borrowings (screener-Data_Sheet.csv; confirmed = interest-bearing debt +
lease liabilities, i.e. Rs 1,061.25 mn borrowings + Rs 661.49 mn lease
liabilities = Rs 1,722.74 mn, ties to screener's Rs 172.27 cr) =
172.27 cr. Cash & Bank (screener-Data_Sheet.csv) = 125.80 cr.
EBITDA FY2026 (AR FY2025-26 p.27, company-disclosed, consolidated,
reported) = Rs 1,268 mn = 126.80 cr (ties to sum of the four FY2026
quarterly "Operating Profit" rows in screener-Data_Sheet.csv: 25.06 +
31.19 + 27.50 + 43.08 = 126.83 cr).
EBIT FY2026 = PBT + Interest (screener-Data_Sheet.csv) = 93.16 + 27.17 =
120.33 cr. Interest FY2026 = 27.17 cr (ties to AR FY2025-26 consolidated
cash flow statement "Finance costs" Rs 271.69 mn, p.145).
Net Worth FY2026 (screener-Data_Sheet.csv) = 1,012.10 cr.

**D1 Net Debt / EBITDA**: Net Debt = 172.27 - 125.80 = 46.47 cr.
46.47 / 126.80 = 0.37x. Band 0-1.0x = **4**

**D2 Interest Coverage (EBIT / Interest)**: 120.33 / 27.17 = 4.43x.
Band 3-4.9x = **2**

**D3 Debt / Equity**: 172.27 / 1,012.10 = 0.17x. Band 0.1-0.5x = **4**

**D4 Current Ratio**: 12,223.01 / 4,915.73 = 2.49x. Band >=2.0x = **5**
(cf. AR FY2025-26 standalone Note 35, p.136: Current Ratio 2.63,
standalone basis — consolidated figure used here for consistency with
the rest of Block D)

**BLOCK D SUBTOTAL: 15 / 20**

Deal-breaker #6 check: ND/EBITDA (0.37x) is not >3x — does not trigger.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

**E1 Promoter holding (latest, FY2026)**: Cyient Limited holds
4,13,66,502 shares = 52.1222% (AR FY2025-26 p.100-101, "Distribution of
Shareholding on the basis of ownership as on March 31, 2026" and ">1%
shareholders" table). Band 50-59.9% = **4**

**E2 Promoter holding change over 3 years**: only two data points exist
in the provided corpus — FY2025 = 52.16% (AR FY2024-25 p.150) and
FY2026 = 52.12% (AR FY2025-26 p.100-101), a 1-year change of -0.04pp.
No FY2023 or FY2024 promoter-holding disclosure is present (shareholding
pattern filings and AR FY2023-24 are both ABSENT per B00 gaps; AR
FY2024-25 does not carry a prior-year comparative in its shareholding
note). **N/A (not in provided data) for the 3-year test, score 0.**

**E3 Promoter pledge (latest)**: no pledge or encumbrance disclosure
found in either annual report's shareholding sections. AR FY2025-26
CARO report, p.100 area (Auditor's clause 3(ix)(f)), states "The Company
has not raised loans during the year on the pledge of securities held in
its subsidiaries" — this confirms no loan was raised BY THE COMPANY
against ITS SUBSIDIARIES' pledged shares, which is not the same
disclosure as promoter (Cyient Limited) pledge of ITS CYIENTDLM shares.
No SEBI-format pledge/encumbrance table was found in the corpus (
"shareholding ABSENT" and "announcements ABSENT" per B00 gaps cover the
BSE/NSE filings that would carry this). **N/A (not in provided data),
score 0.**

**E4 Contingent liabilities / Net Worth**: AR FY2025-26 consolidated
Note 28, p.164: "Claims against the Company not acknowledged as debt:
- -" (nil, both FY2026 and FY2025). Nil / 1,012.10 cr = 0%. Band <5% =
**5**

**BLOCK E SUBTOTAL: 9 / 20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

EBITDA margin (AR-disclosed consolidated EBITDA / screener revenue):
FY2023 = 87.8/832.03 = 10.55%, FY2024 = 111.0/1,191.87 = 9.31%,
FY2025 = 137.2/1,519.63 = 9.03%, FY2026 = 126.8/1,261.49 = 10.05%
(AR FY2025-26 p.27).

**M1 Pricing Power**: margin change FY23->FY26 = 10.05-10.55 = -0.50pp
(stable, within +-2pp). Revenue CAGR (FY23-26) = 14.9% (>=10%). Band
"margin stable +-2pp AND rev CAGR >=10%" = **3**

**M2 Cost Advantage vs peer median EBITDA margin**: no peer data in
corpus (screening PARTIAL, no comparator file). **PEER DATA NEEDED,
score 0**

**M3 Capital Efficiency**: FAT (Revenue/Net Block, screener-Data_Sheet.csv)
FY2026 = 1,261.49/354.81 = 3.56x (>3x). ROCE FY2026 = 11.4% (AR p.27),
not >20%, not >15%, and not >12% (falls short of the >1x-and->12% band by
0.6pp). No band satisfied. **Score 0**
(AR FY2024-25 p.73 MD&A discloses its own "Fixed Assets T/O" of 8.5x
FY2025 / 8.6x FY2024, on a different — likely standalone, possibly
average/gross-block — denominator; not used here to keep the metric
formula-consistent across years; noted as a data point, not scored.)

**M4 Customer Stickiness**: 1 revenue-decline year (FY2026, -17.0%), not
zero, and not "recovered" (FY2026 is the most recent year, no
subsequent recovery year exists in the data). Receivable Days (computed:
Trade Receivables/Revenue x365, screener-Data_Sheet.csv): FY2023 = 70.9
days, FY2024 = 69.2 days, FY2025 = 83.4 days, FY2026 = 88.9 days; change
+18.0 days (not stable +-10). Neither the 5-tier nor the 3-tier band is
met; closest to the "2 decline years, CAGR positive" description in
spirit (1 decline year, overall CAGR still positive) is used
conservatively. **Score 1** (judgment flagged; see analyst_note)

**M5 Scale & Dominance**: requires peer market-cap and margin ranking;
not in corpus. **PEER DATA NEEDED, score 0**

**M6 Technology / R&D**: no "Research and Development" disclosure found
in either annual report (grepped both, no match). Design-led
manufacturing/EMS contract model; no separate R&D expense line
identified. **Score 0** (not "PEER DATA NEEDED" — this is a disclosure
absence, not a peer-comparison gap)

**M7 Regulatory / License**: requires count of listed peers in the
ESDM/aerospace-EMS segment; not in corpus. **PEER DATA NEEDED, score 0**

**M8 Distribution**: business model is B2B contract manufacturing
(design-led manufacturing for OEM customers), not a distribution/outlet
network business; no distribution-reach disclosure applies. **Score 0**
("none" band — not a peer-data gap, a business-model non-applicability)

**M9 Brand**: Gross margin proxy (Revenue - Material Cost)/Revenue,
Material Cost = Raw Material Cost + Change in Inventory
(screener-Data_Sheet.csv): FY2023 = 25.1%, FY2024 = 18.0%, FY2025 =
29.9%, FY2026 = 35.2% (proxy basis stated). No peer median available to
compare. **PEER DATA NEEDED, score 0**

**M10 Switching Costs**: revenue grew in 2 of 3 periods ("all but 1
year" — satisfied) but receivable days rose 18.0 days over the period
(fails the "stable" leg required for the 3-tier band). Falls to
**score 0**

**M11 Network Effects**: fewer than 6 years available (4 declared, 5
with the AR KPI supplement) — scored conservatively per instruction.
Overall Revenue CAGR (FY23-26) = 14.9%, below the 20% threshold for the
middle band, and the terminal year (FY26) shows a revenue decline, not
acceleration. **Score 0** (insufficient years for the two-window test,
stated)

**M12 Negative WC / Float**: company-disclosed NWC days (AR FY2025-26
p.27): FY2023 = 48, FY2024 = 79, FY2025 = 127, FY2026 = 145 — all well
above 45 days in every year. **Score 0**

**BLOCK F SUBTOTAL: 4 / 60** (M1=3, M2=0, M3=0, M4=1, M5=0, M6=0, M7=0,
M8=0, M9=0, M10=0, M11=0, M12=0)

Moats "present" (score >=3): M1 only. **Moats confirmed: 1**
Moat classification (1 present) = **THIN**

---

## MOAT PROFILE

```
M1  Pricing Power        [###......] 3/5  PRESENT
M2  Cost Advantage       [.........] 0/5  PEER DATA NEEDED
M3  Capital Efficiency   [.........] 0/5
M4  Customer Stickiness  [#........] 1/5
M5  Scale & Dominance    [.........] 0/5  PEER DATA NEEDED
M6  Technology / R&D     [.........] 0/5
M7  Regulatory / License [.........] 0/5  PEER DATA NEEDED
M8  Distribution         [.........] 0/5
M9  Brand                [.........] 0/5  PEER DATA NEEDED
M10 Switching Costs      [.........] 0/5
M11 Network Effects      [.........] 0/5  (<6yr, conservative)
M12 Negative WC / Float  [.........] 0/5
```

---

## SCORE SUMMARY

| Block | Score | Max |
|---|---|---|
| A - Return on Capital | 5 | 20 |
| B - Cash Generation Quality | 0 | 20 |
| C - Growth | 14 | 20 |
| D - Balance Sheet Strength | 15 | 20 |
| E - Shareholder Alignment | 9 | 20 |
| **Core Score (A+B+C+D+E)** | **43** | **100** |
| F - Quantitative Moat | 4 | 60 |
| **GRAND TOTAL** | **47** | **160** |

Strongest block: **D - Balance Sheet Strength (15/20)** — light debt
load (D/E 0.17x, ND/EBITDA 0.37x), strong current ratio (2.49x
consolidated).

Weakest block: **B - Cash Generation Quality (0/20)** — every one of
the four tests scored zero; cumulative CFO is negative across FY23-26
despite cumulative PAT of +Rs 234.29 cr, and net working capital days
nearly tripled (48 -> 145) over the period.

---

## DEAL-BREAKER CHECK

1. Block A <8 -> max GOOD: **triggered** (A=5) — no effect, classification
   already below GOOD.
2. Block B <8 -> max GOOD: **triggered** (B=0) — no effect, classification
   already below GOOD.
3. Median ROCE <10% -> max AVERAGE: not triggered (median ROCE = 11.2%).
4. Cumulative CFO/PAT <0.50 -> max AVERAGE: **triggered** (ratio = -0.11).
   Driver years: FY2024 (CFO -70.54 cr) and FY2025 (CFO -62.39 cr), both
   attributed by AR FY2024-25 p.69/p.73 to receivables and inventory
   buildup for large-deal execution and post-IPO capacity investment;
   FY2026 CFO recovered to +53.90 cr.
5. Pledge >15% -> max AVERAGE: not evaluable (pledge data N/A, not in
   provided corpus) — not triggered on available evidence, but unresolved.
6. ND/EBITDA >3x AND IC <3x -> AVOID: not triggered (ND/EBITDA = 0.37x).
7. Revenue declined in majority of years -> max AVERAGE: not triggered
   (1 of 3 YoY periods declined).
8. PAT negative in any of last 3 years -> max AVERAGE: not triggered
   (PAT positive all 4 years, though FY2026 growth includes a one-off
   earn-out reversal per AR FY2025-26 p.27).
9. History <3 years -> AVERAGE: not triggered (4 years available).

---

## CLASSIFICATION

Data confidence: 4 years = LIMITED (band "3-4 LIMITED, downgrade
classification one tier").

Classification matrix: Core Score 43 falls in the 40-59 band ->
**AVERAGE** (pre-downgrade; moat tier does not affect this band).
Deal-breaker #4 independently caps at max AVERAGE — consistent, no
additional effect.

Data-confidence downgrade (LIMITED, one tier down from AVERAGE):
**AVOID**

**FINAL CLASSIFICATION: AVOID**

This is a mechanical score. Per the operating rules, classification is
not a halt: flags propagate, they do not stop the pipeline. Note also
the CLAUDE.md instruction that "downstream position sizing may override
AVERAGE for documented post-IPO rebase / legacy cleanup cases" — the
Block B collapse here is substantially explained by two years (FY24,
FY25) of AR-documented working-capital investment tied to large-deal
execution and post-IPO capacity build, not by margin or demand collapse.
This is recorded for downstream weighing, not resolved at this stage.

---

## DECISION LINE

CYIENTDLM scores AVOID on Gate 0 mechanics (Core 43/100, Grand Total
47/160, moat THIN, 1 confirmed moat test of 12). The scorecard is driven
down by a Block B cash-generation collapse (0/20) concentrated in two
specific years (FY24-25) that the company's own AR attributes to
working-capital investment behind large-deal execution, and a Block A
return-on-capital profile stuck near 11% for three straight years
(FY24-26) after an 18% pre-IPO peak (FY22, outside the scored window).
Growth (14/20) and balance sheet strength (15/20) are the offsetting
positives. Four significant evidence gaps remain open for Phase 3:
promoter pledge status (E3), promoter holding history beyond one year
(E2), any peer comparator set (blocks M2/M5/M7/M9), and FY2023 capex
(B2/B3 window). Company quality flags propagate; this scorecard does not
halt the pipeline.

---

## DATA NOTES

- No loss-to-profit PAT swing in the window (PAT positive all 4 years).
- Proxy basis used: M9 gross margin proxy = (Revenue - Material Cost) /
  Revenue, Material Cost = Raw Material Cost + Change in Inventory
  (screener-Data_Sheet.csv). Not scored (no peer median).
- PEER DATA NEEDED: M2, M5, M7, M9 (score 0 each, not a company-level
  finding).
- FY2023 capex NOT FOUND (no AR FY2023-24 in corpus); B2 and B3 computed
  on a 3-year window (FY24-26) instead of 4, both numerator and
  denominator matched to the same window.
- ROCE used as company-disclosed (AR FY2025-26 p.27 consolidated KPI
  chart), not independently computed, per the rule preferring a
  source-provided figure. A4 was scored on the declared FY23-26 window
  (decline 1.6pp, score 3); the fuller 5-year company series (FY22-26)
  shows a 6.6pp decline (would score 0) because FY2022, the pre-large-
  capex peak, sits outside the declared scoring window.
- WC Days (B4, M12) used the company's own disclosed "Net Working
  Capital (Days)" KPI (AR FY2025-26 p.27) rather than a formula rebuild,
  because Trade Payables were not available in screener-Data_Sheet.csv
  for all 4 years. Receivable Days (used independently for M4 and M10)
  was computed per the fixed formula from screener-Data_Sheet.csv and is
  not fully reconcilable to the KPI-chart NWC-days metric (different
  netting convention); both point the same direction (deterioration).
- FY2026 reported PAT growth (+7.6% YoY) is flagged by AR FY2025-26 p.27
  itself as driven by "the reversal of one-off earn-out provisions,"
  with normalized PAT down 24% YoY. This materially affects the
  credibility of C2 (PAT CAGR = 32.2%, scored 5) and C4 (scored 5) as
  clean growth signals.
- E2 (promoter holding 3-year change) and E3 (promoter pledge): both
  N/A, not in provided corpus. Shareholding-pattern filings and
  announcements are ABSENT per B00 gaps; only two annual reports' own
  shareholding notes were available (FY2025, FY2026 promoter % only).
- Screener aggregate line items ("Borrowings", "Other Liabilities",
  "Cash & Bank") were cross-checked against the AR FY2025-26 and AR
  FY2024-25 consolidated balance sheets and reconcile exactly once lease
  liabilities are included in "Borrowings" — noted so downstream stages
  do not re-flag this as a discrepancy.
