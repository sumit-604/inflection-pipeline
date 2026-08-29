# STAGE 1 — GATE 0 SCORECARD: CMS Info Systems Ltd (CMSINFO)
Run date: 2026-08-29 | run_type: full | Model: claude-sonnet-5

Data available: 9 years (FY2018 to FY2026), consolidated basis, from
screener-Data_Sheet.csv. Scoring adapted to 9-year history for revenue,
PAT, cash flow and net-worth-based metrics. ROCE specifically is anchored
to only 3 years (FY2024-FY2026) because Data_Sheet does not carry a
precomputed ROCE row and the Annual Report's clean, page-anchored "Key
Ratios" table covers only FY24-FY26 (see Block A notes). Full working
capital days and free cash flow are anchored to only 2 years (FY25-FY26)
because Data_Sheet's cash-flow block has no capex split and no trade
payables line for FY18-FY24 (see Block B notes).

Cross-check note: screener-Profit_Loss.csv, screener-Balance_Sheet.csv,
screener-Cash_Flow.csv and screener-Quarters.csv are confirmed EMPTY
(collector defect) and were not used. All figures below trace to
screener-Data_Sheet.csv, the FY26 audited results filing, or the FY26
Annual Report (mislabelled Annual_Report_2023.pdf, verified as FY2025-26
report by content).

---

## LOAD-BEARING FACT CHECK (LBF-1): CASH CONVERSION

CFO/PAT, last 3 years (screener-Data_Sheet.csv, Cash Flow + P&L rows):
- FY24: CFO 439.89 / PAT 347.14 = 1.267x (Data_Sheet)
- FY25: CFO 482.53 / PAT 372.46 = 1.296x (Data_Sheet)
- FY26: CFO 389.59 / PAT 303.39 = 1.284x (Data_Sheet)

Cross-checked against audited consolidated results: FY26 CFO Rs 3,895.93
million = Rs 389.59 Cr (results p.13, cash flow statement, line "Net cash
flow generated from operating activities (A)"); FY26 PAT Rs 3,033.92
million = Rs 303.39 Cr (results p.10, consolidated P&L, "Profit for the
period/year attributable to equity share holders"). Both match Data_Sheet
exactly. LBF-1 CONFIRMED: cash conversion above 1.2x, three years running.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Data_Sheet has no ROCE row. Screener's own precomputed ROCE is absent from
this export, so per the formula rules this stage uses the AR's own
reported figure (source provides it) rather than compute from
Total Assets minus Current Liabilities, because Current Liabilities (split
from Non-Current Liabilities) is available in the corpus for only FY25 and
FY26 (audited results balance sheet, p.11), not for FY18-FY24.

**AR "Key Ratios" table (AR p.52, printed pages 96-97, "Post-Tax ROCE (%)"
row), consolidated basis:**
- FY24: 25.4% (AR p.52)
- FY25: 25.2% (AR p.52)
- FY26: 16.6% (AR p.52)

Cross-check: FY26 figure is corroborated by a separate 5-year ROCE bar
chart on AR p.21-22 ("RETURN ON CAPITAL EMPLOYED (ROCE)", FY22-FY26,
average 23.0%), which shows the values {23.4%, 24.4%, 25.2%, 25.4%,
16.59%}. Three of the five chart values (25.4, 25.2, 16.59) match the
table exactly, confirming the chart and table describe the same metric.
The remaining two chart values (23.4%, 24.4%) are almost certainly FY22
and FY23 ROCE but the OCR/text-extraction of the bar chart does not
preserve which value belongs to which year, so they are NOT used for
scoring (data_notes carries them as context only).

- A1 Median ROCE (FY24-26: 16.6, 25.2, 25.4; median = 25.2%): >= 25% = **5**
- A2 Minimum single-year ROCE (16.6%, FY26): >= 15% = **5**
- A3 Median ROE (computed, PAT / average Net Worth, Data_Sheet
  share-capital + reserves rows, 9 years FY18-26; FY18 uses closing net
  worth only, opening unavailable):
  FY18 11.89% | FY19 13.54% | FY20 16.88% | FY21 18.37% | FY22 19.996% |
  FY23 21.09% | FY24 19.79% | FY25 17.68% | FY26 12.91%
  Median (5th of 9, sorted) = 17.68% (FY25): 15-19.9% = **4**
- A4 ROCE trend, latest (FY26 16.6%) vs earliest anchored (FY24 25.4%):
  decline of 8.8pp, > 5pp decline = **0**

**Block A subtotal: 14/20**

Note: the only clean anchored ROCE window is 3 years (FY24-26), so A4
reads as a one-year dip rather than a longer erosion. The AR chart's
unordered FY22-23 values (23.4-24.4% range) suggest ROCE was already
easing from a higher base before FY26's sharper fall; this softens but
does not reverse the A4 read. Flagged in analyst_note.

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

- B1 Cumulative CFO / Cumulative PAT (9 years, Data_Sheet):
  Cumulative CFO = 149.02+101.78+214.16+185.44+256.51+406.76+439.89+482.53+389.59
  = Rs 2,625.68 Cr (Data_Sheet, Cash Flow row, FY18-26)
  Cumulative PAT = 80.17+96.14+134.71+168.52+224.04+297.24+347.14+372.46+303.39
  = Rs 2,023.81 Cr (Data_Sheet, P&L row, FY18-26)
  Ratio = 1.298x: >= 1.00 = **5**
- B2 FCF-positive years as proportion. FCF = CFO - Capex. Data_Sheet's
  cash-flow block gives only net "Cash from Investing Activity" (no capex
  split) and this is not usable alone (it nets acquisitions, investments
  in mutual funds/deposits, etc). Capex ("Purchase of property, plant and
  equipment, Intangible assets") is available only for FY25 and FY26 from
  the audited results investing-activities note (results p.13):
  FY26 capex Rs 4,092.68 million = Rs 409.27 Cr; FY25 capex Rs 1,543.37
  million = Rs 154.34 Cr.
  FY26 FCF = 389.59 - 409.27 = **-19.68 Cr** (negative)
  FY25 FCF = 482.53 - 154.34 = **+328.19 Cr** (positive)
  1 of 2 years positive = 50%: 50-74% = **2**
  NOT FOUND for FY18-24 (no capex breakdown in provided corpus).
- B3 Cumulative FCF / Cumulative PAT (same 2-year window, FY25-26 only):
  Cumulative FCF = 328.19 - 19.68 = Rs 308.51 Cr
  Cumulative PAT (FY25-26) = 372.46 + 303.39 = Rs 675.85 Cr
  Ratio = 0.4565: 0.40-0.59 = **3**
- B4 Change in WC Days, latest vs earliest available (FY26 vs FY25 only;
  trade payables not available pre-FY25):
  Basis: Receivable Days = Receivables/Sales x 365; Inventory Days =
  Inventory/Sales x 365 (COGS not separately disclosed); Payable Days =
  Trade Payables/Sales x 365. Receivables/Inventory from Data_Sheet;
  Trade Payables from audited results balance sheet (results p.11):
  FY25 payables = Rs 102.38m (MSME) + Rs 3,398.56m (other) = Rs 350.09 Cr
  FY26 payables = Rs 93.47m (MSME) + Rs 3,027.02m (other) = Rs 312.05 Cr
  FY25: Receivable Days 122.64 + Inventory Days 11.98 - Payable Days 52.71
  = **81.91 days**
  FY26: Receivable Days 130.93 + Inventory Days 10.15 - Payable Days 45.79
  = **95.29 days**
  Change = +13.38 days (increase): increased 5-15 days = **1**

**Block B subtotal: 11/20**

**block_b_trend: deteriorating.** Single clearest number: FY26 FCF turned
negative (-Rs 19.7 Cr) from FY25's +Rs 328.2 Cr, as capex nearly tripled
YoY (Rs 409.3 Cr vs Rs 154.3 Cr, results p.13) for major contract
build-out (SBI 4,000-ATM mandate, AR p.52). WC days rose 13.4 days over
the same one-year window. Cash conversion (B1, LBF-1) itself stayed above
1.2x, so this is a capex-and-working-capital story, not a P&L-to-cash
leakage story, but it caps Block B below the top band regardless.

---

## BLOCK C: GROWTH (Max 20)

- C1 Revenue CAGR (FY18 Rs 977.66 Cr -> FY26 Rs 2,487.18 Cr, 8 years,
  Data_Sheet): CAGR = (2487.18/977.66)^(1/8) - 1 = 12.38%: 10-14.9% = **3**
- C2 PAT CAGR (FY18 Rs 80.17 Cr -> FY26 Rs 303.39 Cr, 8 years,
  Data_Sheet): CAGR = (303.39/80.17)^(1/8) - 1 = 18.11%: 15-19.9% = **4**
- C3 Positive YoY revenue years (8 YoY comparisons FY19-FY26,
  Data_Sheet): 7 of 8 positive (FY21 vs FY20 was the sole decline,
  1306.09 vs 1383.24, COVID-year cash-logistics volume hit) = 87.5%:
  75-99% = **3**
- C4 PAT CAGR minus Revenue CAGR = 18.11 - 12.38 = +5.73pp: >= +3pp = **5**

**Block C subtotal: 15/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

- D1 Net Debt / EBITDA (FY26). Data_Sheet's "Borrowings" row (Rs 221.38
  Cr, FY26) reconciles exactly to Ind AS 116 lease liabilities (non-current
  Rs 1,553.71m + current Rs 660.11m = Rs 2,213.82m = Rs 221.38 Cr,
  results p.11) — CMS carries no conventional financial debt. Company
  states "maintained its zero-net-debt position throughout FY26" (AR
  p.52). Cash & Bank Rs 154.59 Cr + Investments Rs 373.85 Cr (Data_Sheet)
  against Rs 221.38 Cr lease liabilities = net cash of ~Rs 307 Cr.
  EBITDA FY26 = Rs 600 Cr, margin 24.1% (results p.4, media release,
  matches AR Key Ratios EBITDA/Revenue 24.1%, AR p.52).
  Net cash position = **5**
- D2 Interest Coverage, EBIT/Interest (FY26). EBIT = PBT + Interest =
  405.40 + 19.48 = Rs 424.88 Cr (Data_Sheet; Interest row matches audited
  Finance costs Rs 194.79m = Rs 19.48 Cr, results p.10). Interest = Rs
  19.48 Cr (Data_Sheet). IC = 424.88/19.48 = 21.81x: >= 10x = **5**
- D3 Debt/Equity (FY26). AR reports "Debt-Equity Ratio 0.0" for FY24-26
  (AR p.52, Key Ratios table). Cross-check using Data_Sheet's
  lease-liability-labelled "Borrowings" as debt: 221.38/2432.34 = 0.091,
  same band either way: <0.1 = **5**
- D4 Current Ratio (FY26). AR-reported 2.6 (AR p.52). Cross-check from
  audited consolidated balance sheet: Current Assets Rs 15,664.87m /
  Current Liabilities Rs 6,119.07m = 2.56x (results p.11). >= 2.0 = **5**

**Block D subtotal: 20/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

Structural note: CMS has NO PROMOTER. Sion Investment Holdings
(Advent/Baring affiliate) sold its residual stake Feb-2024 and was
declassified promoter -> public wef 2-Apr-2025. Promoter category has
read 0.00% since Mar-2024 (shareholding-pattern-screener-quarterly.txt).
This is a completed, disclosed structural exit, not a disclosure gap.

- E1 Promoter holding (latest quarter, Jun 2026): Promoter = 0.00%
  (shareholding file). Professionally managed alt-path applies: FII+DII =
  22.70% + 36.00% = 58.70% (Jun 2026, shareholding file), > 50% = **3**
- E2 Promoter holding change over 3 years: literal formula reads Sep-2023
  (26.69%, earliest quarter in the provided window) to Jun-2026 (0.00%),
  a decline of 26.69pp, which is "decreased >3% = 0" on a literal read.
  Scored **3 (neutral)** instead: this decline is the disclosed, orderly
  completion of a PE-sponsor exit (Advent/Baring's Sion vehicle), not
  insider distress selling, and there is no promoter register left to
  test alignment against. Scoring it 0 would misclassify a
  governance-neutral-to-positive structural event (removal of a PE
  overhang, replaced by rising DII ownership) as an alignment red flag.
  See data_notes.
- E3 Promoter pledge (latest): 0% pledge, trivially true — there is no
  promoter to pledge shares. 0% = **5**
- E4 Contingent Liabilities / Net Worth (FY26, consolidated basis to
  match Data_Sheet net worth). Consolidated contingent liabilities Rs
  554.60 million = Rs 55.46 Cr (AR Note 31a, consolidated financial
  statements, AR p.128). Net Worth FY26 = Rs 2,432.34 Cr (Data_Sheet,
  Equity Share Capital + Reserves). Ratio = 2.28%: < 5% = **5**
  (Note: standalone contingent liabilities are higher, Rs 959.82 million
  = Rs 95.98 Cr, AR Note 31a standalone financial statements, AR p.96 —
  not used here to keep numerator/denominator on the same consolidation
  basis.)

**Block E subtotal: 16/20**

---

## CORE SCORE

A 14 + B 11 + C 15 + D 20 + E 16 = **76/100**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

EBITDA margin series used for M1/M11 (computed as PBT + Depreciation +
Interest - Other Income, all Data_Sheet rows; cross-checked within ~1pp
of AR-reported figures for FY24-26 where both exist):
FY18 15.07% | FY19 17.27% | FY20 18.36% | FY21 22.48% | FY22 25.15% |
FY23 28.09% | FY24 26.47% (AR: 26.7%) | FY25 25.85% (AR: 26.1%) | FY26
23.97% (AR/media release: 24.1%)
Caveat: Ind AS 116 lease-accounting adoption (effective FY20) moved
operating-lease payments out of opex into D&A + interest, inflating
apparent EBITDA margin from FY20 onward on a like-for-like basis versus
FY18-19. FY18-19 are pre-adoption and not strictly comparable to later
years.

- **M1 Pricing Power [#####] 5/5 PRESENT.** Margin expanded FY18 15.07%
  -> FY26 23.97%/24.1% (+8.9pp) AND revenue CAGR 12.38% (C1) >= 10% = 5.
  Caveat: expansion is partly an Ind AS 116 accounting artefact, and the
  most recent 2 years show compression (FY24 26.47%/26.7% -> FY26
  23.97%/24.1%, roughly -2.6pp), which the full-period test does not
  capture. See analyst_note.
- **M2 Cost Advantage vs peer median [ ] 0/5.** PEER DATA NEEDED — no
  peer EBITDA margin data supplied to this stage.
- **M3 Capital Efficiency [###] 3/5 PRESENT.** FAT (Revenue/Net Block,
  Data_Sheet, FY26) = 2487.18/1154.71 = 2.15x > 2x AND ROCE FY26 16.6%
  (AR p.52) > 15% = 3. (Sensitivity: including CWIP in the fixed-asset
  base, FAT = 2487.18/1268.18 = 1.96x, which would drop the band to
  "FAT>1x AND ROCE>12%" = 1; Net Block only used as the more standard
  convention.)
- **M4 Customer Stickiness [###] 3/5 PRESENT.** 1 revenue-decline year
  (FY21, Data_Sheet) fully recovered by FY22 (1589.67 > prior peak
  1383.24, FY20) = 3. Receivable days were NOT stable (72.75 days FY18 to
  130.93 days FY26, computed from Data_Sheet), so the top band (0 decline
  years AND receivable days stable +/-10) does not apply.
- **M5 Scale & Dominance [ ] 0/5.** PEER DATA NEEDED — no peer mcap or
  margin-ranking data supplied. Qualitative context only (not scored):
  AR describes CMS as market leader in cash management/ATM services and
  states Managed Services moved from #5 to #3 position in FY26 (AR p.52,
  media release).
- **M6 Technology/R&D [ ] 0/5.** No R&D/Revenue disclosure found in
  provided AR or results text. Scored 0, not "PEER DATA NEEDED" — this is
  an absence of the underlying disclosure, not a missing peer comparison.
- **M7 Regulatory/License [ ] 0/5.** PEER DATA NEEDED — cash logistics is
  a licensed/security-regulated business (qualitative, AR risk section)
  but no sourced count of listed players in the segment was supplied to
  test the "<=5" / "<=10" bands.
- **M8 Distribution [#] 1/5.** AR states "pan-India network spanning 97%
  of districts" (media release, results p.5) — reach is quantified, but
  this is a single current-year data point; no multi-year outlet-count
  trend or revenue-per-outlet series was found in the provided corpus to
  test "growing" and "stable/growing revenue per outlet." Scored
  conservatively at the "mentioned" band despite the reach being
  numeric, because growth cannot be verified.
- **M9 Brand [ ] 0/5.** PEER DATA NEEDED — no peer gross-margin data
  supplied. CMS is a B2B services platform, not a classic branded
  consumer business; low relevance expected regardless of data.
- **M10 Switching Costs [ ] 0/5.** 1 revenue-decline year (not 0), AND
  receivable days rose +58.18 days over the full period (FY18-26,
  computed from Data_Sheet) — well past the "<=10 days" band needed to
  pair with 1 decline year for a score of 3. Falls into "else" = 0. This
  echoes the B4 finding: receivable/WC days are extending, not stable.
- **M11 Network Effects [ ] 0/5.** 9 years available (>=6 required).
  Latest 3-year revenue CAGR (FY23->FY26) = (2487.18/1914.73)^(1/3)-1 =
  9.12% (Data_Sheet). Prior 3-year CAGR (FY20->FY23) =
  (1914.73/1383.24)^(1/3)-1 = 11.46% (Data_Sheet). Latest < prior, so the
  "accelerating" condition fails; neither the >=20% nor the >15% growth
  bands are met either = 0.
- **M12 Negative WC/Float [ ] 0/5.** Only 2 years of full WC-days data
  available (FY25 81.91 days, FY26 95.29 days, both from B4 above), both
  well above the 45-day ceiling for any positive band = 0. Directionally
  robust to the missing years given the magnitude.

**Moat score: 5+0+3+3+0+0+0+1+0+0+0+0 = 12/60**
**Moats present (score >=3): 3 (M1, M3, M4)**
**Moat classification: 2-3 present = MODERATE**

---

## GRAND TOTAL

Core 76 + Moat 12 = **88** (of 160 max)

---

## DEAL-BREAKER CHECK

1. Block A < 8? A=14. No.
2. Block B < 8? B=11. No.
3. Median ROCE < 10%? 25.2%. No.
4. Cumulative CFO/PAT < 0.50? 1.298x. No.
5. Pledge > 15%? 0%. No.
6. ND/EBITDA > 3x AND IC < 3x? Net cash position, IC 21.81x. No.
7. Revenue declined in majority of years? 1 of 8 YoY periods (12.5%). No.
8. PAT negative in any of last 3 years? Positive FY24/25/26 throughout
   (Data_Sheet). No.
9. History < 3 years? 9 years available. No.

**No deal-breakers triggered.**

---

## DATA CONFIDENCE

9 years of core financial history (FY18-FY26) falls in the 7-9 "moderate"
confidence band. No downgrade applies (downgrade is reserved for 3-4
years, LIMITED). Sub-metrics with shorter anchored windows (ROCE: 3
years; FCF/WC days/M10/M12: 2 years) are individually flagged above and
in data_notes but do not trigger the overall history-based downgrade,
which governs total years of financial history, not per-metric coverage.

---

## CLASSIFICATION

Core score 76 falls in the 60-79 band. Moat classification MODERATE
(not STRONG/FORTRESS). Matrix: "Core 60-79 + else = GOOD".

**CLASSIFICATION: GOOD**

---

## STRONGEST / WEAKEST BLOCK

**Strongest: Block D, Balance Sheet Strength, 20/20.** Net cash position,
21.8x interest coverage, near-zero leverage, 2.6x current ratio — all
four sub-metrics hit top band on both AR-reported and Data_Sheet-derived
figures.

**Weakest: Block B, Cash Generation Quality, 11/20 (55%).** Not a cash
conversion failure (B1 = 1.30x cumulative CFO/PAT, LBF-1 confirmed clean)
but a working-capital-and-capex story: FCF flipped negative in FY26 on a
capex surge, and WC days extended 13.4 days in the one year the data
allows testing. Block A (14/20, 70%) is the second-weakest, dragged
entirely by A4's 8.8pp ROCE decline over the only clean 3-year window
available.

---

## DECISION LINE

GATE 0: **GOOD** (Core 76/100, Moat MODERATE 12/60 with 3 moats present,
Grand Total 88/160). No deal-breaker triggered; no mechanical halt.
Watch items for downstream stages: FY26 ROCE nearly halved year on year
(25.2% to 16.6%, AR p.52), FCF turned negative on a capex surge, and both
receivable days and full working-capital days are extending — none of
these are disqualifying on the evidence available, but all three point
the same direction (FY26 was a genuine step-down year, not noise) and
should be checked against Q1 FY27 and management's FY27 guidance
(revenue Rs 2,800-2,900 Cr, EBITDA margin ~27% target, results p.4) in
later stages.

---

## DATA NOTES (full list)

1. ROCE not provided by screener Data_Sheet; scored using AR-reported
   consolidated Post-Tax ROCE, FY24-26 only (AR p.52, Key Ratios table).
   A 5-year AR chart (FY22-26, AR p.21-22) shows two further values
   (23.4%, 24.4%) that are almost certainly FY22/FY23 ROCE (3 of 5 chart
   values match the table exactly) but the year-to-value order cannot be
   confirmed from the OCR-extracted bar chart, so they are excluded from
   Block A scoring.
2. EBITDA margin series (FY18-26) computed as PBT + Depreciation +
   Interest - Other Income from Data_Sheet; cross-checked within ~1pp of
   AR-reported figures for FY24-26. Pre/post-FY20 comparison is confounded
   by Ind AS 116 lease-accounting adoption; flagged wherever the margin
   trend is used (M1, M11).
3. FCF (B2/B3) and full Working Capital Days (B4) are computable only for
   FY25-FY26. Data_Sheet's cash-flow block gives only net investing cash
   flow (no capex split) and the balance sheet block has no trade
   payables line for any year. Capex and trade payables for FY25-26
   sourced from the FY26 audited results (2-year comparative only,
   results p.11 and p.13). FY18-24 marked NOT FOUND for these specific
   sub-metrics.
4. Loss-to-profit swing: none. PAT positive every year FY18-26
   (Data_Sheet).
5. M2, M5, M7, M9 scored 0 = PEER DATA NEEDED (no peer mcap/margin/
   listed-player-count data supplied to this stage).
6. M6 (R&D) scored 0: no R&D/Revenue disclosure found in provided AR or
   results text; treated as absent disclosure, not a peer-data gap.
7. Contingent liabilities (E4) sourced from AR consolidated Note 31a
   (Rs 554.60 million FY26, AR p.128); a separate standalone Note 31a
   shows Rs 959.82 million FY26 (AR p.96). Consolidated figure used to
   match the consolidated net worth denominator.
8. Promoter block (E1-E3): CMS has had NO promoter since Mar-2024 (Sion
   Investment Holdings/Advent-Baring fully exited, declassified promoter
   -> public wef 2-Apr-2025, shareholding file). E1 scored via the
   "professionally managed, FII+DII > 50%" alt-path (58.70%, Jun-2026).
   E3 scored 5 (0% pledge, trivially true, no promoter exists to pledge).
   E2 scored 3 (neutral) rather than the formula-literal 0, because the
   26.69pp "decline" is the disclosed, orderly completion of a PE-sponsor
   exit, not insider distress selling, and there is no promoter register
   left to test ongoing alignment against.
9. Prospectus absent (long-listed since Dec-2021, expected). Announcement
   feed has no filed Reg-30 PDFs in this run's inputs. screener split-CSVs
   (Profit_Loss/Balance_Sheet/Cash_Flow/Quarters) are confirmed empty,
   Data_Sheet is the sole screener source. Shareholding pattern is
   screener-tier, not a filed SHP PDF.
