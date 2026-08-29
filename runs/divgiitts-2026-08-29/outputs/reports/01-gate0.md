# STAGE 1: GATE 0 SCORECARD — Divgi TorqTransfer Systems Ltd (DIVGIITTS)
Run date: 2026-08-29 | Model: claude-sonnet-5

Data available: 9 years (FY2018 to FY2026), from screener.in Data Sheet export
(screener-Data_Sheet.csv), cross-checked against the FY26 audited annual
results filing and the Q1 FY27 unaudited results filing. Scoring adapted to
9-year history for revenue/PAT/margin metrics. Four sub-metrics (ROCE,
Working Capital Days, FCF, cumulative-CFO-basis checks needing Trade
Payables/Capex/Current-Liability splits) are computable only for FY2025 and
FY2026, because the screener export does not split current vs non-current
liabilities, does not carry a Trade Payables line, and does not carry a
capex line, for FY2018-FY2024. Those two years were reconstructed from the
detailed audited/unaudited balance sheets in the results filings. This is
stated per metric below.

Sector note: the run manifest's sector_cap_row read "Agri processing." That
is wrong. Divgi TorqTransfer is an auto driveline / transmission components
maker (transfer cases, AWD/NexTrac systems, EV transmissions). Treated as
auto ancillary throughout this scorecard; sector-cap fields not otherwise
used at Gate 0.

## SPEAR LOAD-BEARING FACT CHECK (first verification priority, per task)

1. Q1 FY27 run rate vs Indonesia launch batch: Q1 FY27 (Jun-26) revenue =
   Rs 137.14 Cr (screener-Quarters via Data_Sheet; matches results Q1 FY27
   p.5, Revenue from operations Rs 1,371.42 million). This is +91.3% YoY
   vs Q1 FY26 (Jun-25) Rs 71.68 Cr, and +27.4% QoQ vs Q4 FY26 (Mar-26)
   Rs 107.62 Cr. Magnitude is confirmed from filings; the "Indonesia" driver
   itself is not verifiable from financial statements alone (no segment/geo
   revenue disclosure in provided data) — flagged for downstream stages.
2. ~Rs 275 Cr net cash decline in FY26: NOT CORROBORATED by provided data.
   Computed net cash (Cash & Bank − Borrowings incl. lease liabilities,
   screener-data + results Q4 FY26 p.6) = Rs 283.76 Cr at FY25-end
   (284.83 − 1.07) and Rs 292.75 Cr at FY26-end (294.52 − 1.77) — an
   INCREASE of ~Rs 9 Cr, not a decline. No line item in the provided
   screener export or the two results filings reconciles to a ~Rs 275 Cr
   cash outflow in FY26. Flagged for downstream verification of the
   original source of this claim.
3. June 2026 FY25 results resubmission: cannot be verified from provided
   data. The only FY25 comparative figures available are the audited
   column in the FY26 annual results (results Q4 FY26 p.4-7), dated
   May 25, 2026 — which predates the stated June 2026 resubmission. A
   discrepancy was found: screener FY25 Interest = Rs 0.60 Cr
   (screener-data) vs the FY26 filing's audited FY25 comparative Finance
   Cost = Rs 0.382 Cr (results Q4 FY26 p.4, p.7: 3.82 million). All other
   FY25 P&L lines reconcile exactly between the two sources. This may be
   the resubmission's fingerprint, or an unrelated screener data glitch;
   the resubmitted filing itself was not provided. PDF audited figure used
   as authoritative for FY25 Interest in this scorecard.
4. Sigma EV SOP in Q2 FY27 after an April 2026 slip: forward-looking,
   post-dates the Q1 FY27 filing (Jun-26) provided. Not checkable from
   historical financials; N/A for this stage.

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 7/20

Formula: ROCE = EBIT ÷ (Total Assets − Current Liabilities). EBIT computed
as PBT + Interest (screener/results do not supply their own ROCE — both the
Balance_Sheet.csv and Data_Sheet.csv exports have no populated ROCE/ROE
ratio rows), stated "computed."

Capital Employed computable only for FY25 and FY26 (detailed balance sheets
available from results filings; earlier years' screener export lumps
current + non-current liabilities into one "Other Liabilities" line with
no split).
- FY25: Total Assets Rs 660.453 Cr − Current Liabilities Rs 56.511 Cr =
  Rs 603.942 Cr (results Q4 FY26 p.6, audited FY25 column)
- FY26: Total Assets Rs 731.419 Cr − Current Liabilities Rs 89.291 Cr =
  Rs 642.128 Cr (results Q4 FY26 p.6, audited FY26 column)

EBIT:
- FY25: PBT Rs 33.004 Cr + Interest Rs 0.382 Cr = Rs 33.386 Cr (results Q4
  FY26 p.4)
- FY26: PBT Rs 62.749 Cr + Interest Rs 0.310 Cr = Rs 63.059 Cr (results Q4
  FY26 p.4)

ROCE FY25 = 33.386 / 603.942 = 5.53% (computed)
ROCE FY26 = 63.059 / 642.128 = 9.82% (computed)

- A1 Median ROCE (n=2, only computable years): (5.53+9.82)/2 = 7.68% →
  <10% → **Score 0**
- A2 Minimum single-year ROCE: 5.53% (FY25) → <8% → **Score 0**
- A3 Median ROE: ROE = PAT ÷ avg Net Worth (opening+closing/2; FY18 uses
  closing only, no FY17 opening available). Net Worth = Equity Share
  Capital + Reserves (screener-data).
  FY18: 25.28/96.37 (closing only) = 26.23%
  FY19: 40.28/164.19 = 24.54%
  FY20: 28.04/220.77 = 12.70%
  FY21: 38.04/252.70 = 15.05%
  FY22: 46.15/317.945 = 14.51%
  FY23: 51.16/445.65 = 11.48%
  FY24: 39.74/565.81 = 7.02%
  FY25: 24.39/588.555 = 4.15%
  FY26: 46.93/616.115 = 7.62%
  (all screener-data, PAT and Net Worth rows)
  Median (5th of 9, sorted) = 12.70% → 12-14.9% band → **Score 2**
- A4 ROCE trend, latest vs earliest computable year: FY26 (9.82%) ≥ FY25
  (5.53%) → increase → **Score 5** (Note: this trend spans only 2 years,
  FY25→FY26, not the full 9-year window, due to the Capital Employed data
  gap above.)

**Block A = 0+0+2+5 = 7/20.** Deal-breaker #1 fires (Block A<8 → max GOOD).
Deal-breaker #3 fires (median ROCE<10% → max AVERAGE).

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 11/20

CFO available FY2020-FY2026 only (screener-data Cash Flow section; FY18-19
blank/not exported).

- B1 Cumulative CFO ÷ Cumulative PAT, FY20-FY26 (matched window):
  Cumulative CFO = 38.33+26.97+51.08+40.82+32.46+35.21+41.08 = Rs 265.95 Cr
  (screener-data)
  Cumulative PAT (same window) = 28.04+38.04+46.15+51.16+39.74+24.39+46.93
  = Rs 274.45 Cr (screener-data)
  Ratio = 265.95/274.45 = 96.90% → 0.85-0.99 band → **Score 4**
- FCF = CFO − Capex (purchase of PPE + intangibles, excl. acquisitions).
  Capex only available from results filings (FY25, FY26); screener-data
  gives only a combined "Cash from Investing Activity" line for FY20-24
  with no capex breakout.
  FY25: CFO 35.21 − Capex 26.503 (results Q4 FY26 p.7) = +8.71 Cr
  FY26: CFO 41.08 − Capex 44.316 (results Q4 FY26 p.7) = −3.24 Cr
- B2 FCF-positive years as proportion (n=2, only computable years): 1/2 =
  50% → 50-74% band → **Score 2**
- B3 Cumulative FCF ÷ Cumulative PAT (FY25+FY26 only):
  Cumulative FCF = 8.71 + (−3.24) = Rs 5.47 Cr
  Cumulative PAT = 24.39+46.93 = Rs 71.32 Cr (screener-data)
  Ratio = 5.47/71.32 = 7.67% → <0.20 → **Score 0**
- B4 Change in WC Days, latest vs earliest computable year. WC Days =
  Receivable Days + Inventory Days − Payable Days, revenue basis (COGS not
  separately isolated in provided data — proxy basis stated). Trade
  Payables only available for FY25/FY26 from results filings; screener
  Data Sheet carries no Payables row for FY18-24.
  FY25: Receivables 55.46/218.92*365=92.47d; Inventory 41.79/218.92*365=
  69.68d; Payables 40.271/218.92*365=67.15d (payables from results Q4
  FY26 p.6: 13.22+389.49 million). WC Days FY25 = 92.47+69.68−67.15 =
  95.00 days.
  FY26: Receivables 79.29/352.89*365=82.02d; Inventory 58.78/352.89*365=
  60.80d; Payables 60.128/352.89*365=62.19d (results Q4 FY26 p.6:
  81.67+519.61 million). WC Days FY26 = 82.02+60.80−62.19 = 80.63 days.
  Change = 80.63 − 95.00 = −14.37 days (decrease) → >5 days decrease →
  **Score 5**

**Block B = 4+2+0+5 = 11/20.** No deal-breaker (Block B≥8).

block_b_trend: **deteriorating** — FCF swung from +Rs 8.71 Cr (FY25) to
−Rs 3.24 Cr (FY26) as FY26 capex (Rs 44.32 Cr) outpaced CFO growth
(Rs 41.08 Cr), even as CFO/PAT conversion stayed strong (96.9% cumulative)
and WC days improved by 14.4 days.

## BLOCK C: GROWTH (Max 20) — Score: 8/20

Revenue (Rs Cr, screener-data): FY18 159.48, FY19 186.89, FY20 159.07,
FY21 186.58, FY22 233.78, FY23 271.04, FY24 253.42, FY25 218.92,
FY26 352.89.
PAT (Rs Cr, screener-data): FY18 25.28, FY19 40.28, FY20 28.04, FY21 38.04,
FY22 46.15, FY23 51.16, FY24 39.74, FY25 24.39, FY26 46.93.

- C1 Revenue CAGR FY18-FY26 (8 years): (352.89/159.48)^(1/8)−1 = 10.44% →
  10-14.9% band → **Score 3**
- C2 PAT CAGR FY18-FY26 (8 years): (46.93/25.28)^(1/8)−1 = 8.04% → 5-9.9%
  band → **Score 1**
- C3 Positive YoY revenue years / total (8 YoY comparisons, FY19-FY26):
  FY19 up, FY20 down, FY21 up, FY22 up, FY23 up, FY24 down, FY25 down,
  FY26 up → 5/8 = 62.5% → 50-74% band → **Score 1**
- C4 PAT CAGR − Revenue CAGR = 8.04% − 10.44% = −2.40pp → within ±3pp →
  **Score 3**

**Block C = 3+1+1+3 = 8/20.** Deal-breaker #7 (revenue declined majority of
years) NOT triggered: 3/8 = 37.5%, not a majority. Deal-breaker #8 (PAT
negative in any of last 3 years) NOT triggered: FY24/25/26 PAT all
positive (39.74/24.39/46.93).

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 20/20

All at FY26 (latest), Rs Cr:
- Borrowings (incl. lease liabilities, screener-data convention;
  reconciles to results Q4 FY26 p.6: non-current borrowings 0.46m +
  current borrowings 0.95m + non-current lease 8.67m + current lease
  7.62m = 17.70m = Rs 1.77 Cr) = 1.77
- Cash & Bank (screener-data; reconciles to results Q4 FY26 p.6: cash
  equivalents 315.20m + other bank balances 2,630.03m = Rs 294.52 Cr) =
  294.52
- Net cash position (not net debt): 292.75 Cr net cash

- D1 Net Debt ÷ EBITDA: net cash → **Score 5**
- D2 Interest Coverage = EBIT 63.059 / Interest 0.310 = 203.4x → ≥10x →
  **Score 5**
- D3 Debt ÷ Equity = 1.77 / 635.46 (screener-data Equity Share Capital
  15.29 + Reserves 620.17) = 0.003 → <0.1 → **Score 5**
- D4 Current Ratio = Current Assets Rs 450.229 Cr / Current Liabilities
  Rs 89.291 Cr (results Q4 FY26 p.6) = 5.04 → ≥2.0 → **Score 5**

**Block D = 5+5+5+5 = 20/20.** Strongest block. Deal-breaker #6 (ND/EBITDA
>3x AND IC<3x) NOT triggered — net cash, not net debt.

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 0/20

Shareholding pattern, promoter pledge disclosures, and contingent
liabilities notes are all absent from the provided data set (carried from
B00 input_gaps: shareholding ABSENT; no notes-to-accounts section in either
results filing covers contingent liabilities).

- E1 Promoter holding: N/A (not in provided data) → **Score 0**
- E2 Promoter holding change, 3yr: N/A (not in provided data) → **Score 0**
- E3 Promoter pledge: N/A (not in provided data) → **Score 0**
- E4 Contingent liabilities ÷ Net Worth: N/A (not in provided data) →
  **Score 0**

**Block E = 0/20.** This is a data-availability gap, not a demonstrated
governance weakness — flagged for the next stage that has access to
shareholding filings.

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 1/60

OPM by year (Operating Profit = PBT − Other Income + Depreciation +
Interest, screener-data; cross-checked against screener-Quarters "Operating
Profit" row, which sums to the same FY26 figure — Sales less Expenses,
before Dep/Interest/Other Income):
FY18 27.75%, FY19 28.72%, FY20 23.33%, FY21 27.90%, FY22 28.16%,
FY23 27.53%, FY24 21.01%, FY25 17.06-17.17% (see Interest discrepancy
note), FY26 19.84%.

- M1 Pricing Power: OPM FY18 27.75% → FY26 19.84% = −7.91pp (declined
  >5pp) despite revenue CAGR 10.44% (≥10%). Decline exceeds the "declined
  2-5pp" band. → **Score 0**
- M2 Cost Advantage vs peer: PEER DATA NEEDED → **Score 0**
- M3 Capital Efficiency: FAT (FY26) = Sales 352.89 / Net Block 259.82 =
  1.36x; ROCE FY26 = 9.82%. Fails even the lowest band (FAT>1x AND
  ROCE>12%) since ROCE<12%. → **Score 0**
- M4 Customer Stickiness: 3 revenue-decline years (FY20, FY24, FY25) →
  3+ decline years band → **Score 0**
- M5 Scale & Dominance: PEER DATA NEEDED (no mcap/segment ranking data
  provided) → **Score 0**
- M6 Technology/R&D: R&D spend not disclosed as a separate line in any
  provided source → N/A (not in provided data) → **Score 0**
- M7 Regulatory/License: unregulated industry (auto ancillary component
  manufacturer); no licence/quota dependency evidenced in provided data →
  **Score 0**
- M8 Distribution: B2B OEM supply model; no distribution-network metric
  applicable or quantified in provided data → **Score 0**
- M9 Brand: PEER DATA NEEDED (no peer gross-margin median available) →
  **Score 0**
- M10 Switching Costs: overall revenue growth FY18→FY26 positive, but with
  3 decline years (2+ decline-year band) → **Score 1**
- M11 Network Effects (9 years available, qualifies for two-window test):
  Latest 3yr revenue CAGR (FY23→FY26) = (352.89/271.04)^(1/3)−1 = 9.19%.
  Prior 3yr revenue CAGR (FY20→FY23) = (271.04/159.07)^(1/3)−1 = 19.44%.
  Latest CAGR is lower than prior CAGR, and latest CAGR <15% and <20% →
  fails all positive bands → **Score 0**
- M12 Negative WC/Float: WC Days computable only FY25 (95.00d) and FY26
  (80.63d), both >45 days → **Score 0**

**Moat score = 0+0+0+0+0+0+0+0+0+1+0+0 = 1/60.**
Moats "present" (score≥3): **0**. Moat classification: **NONE**.

Note: 4 of the 12 tests (M2, M5, M7, M9) are constrained by "PEER DATA
NEEDED" rather than a demonstrated absence of moat; this is a data gap for
downstream stages (peer/segment benchmarking), not a finding that no moat
exists on those dimensions.

## DASHBOARD SUMMARY

| Block | Score | Max |
|---|---|---|
| A. Return on Capital | 7 | 20 |
| B. Cash Generation Quality | 11 | 20 |
| C. Growth | 8 | 20 |
| D. Balance Sheet Strength | 20 | 20 |
| E. Shareholder Alignment | 0 | 20 |
| **Core total (A-E)** | **46** | **100** |
| F. Quantitative Moat | 1 | 60 |
| **Grand total** | **47** | **160** |

Moat profile: [M1 0][M2 0*][M3 0][M4 0][M5 0*][M6 0][M7 0][M8 0][M9 0*]
[M10 1][M11 0][M12 0]  (* = PEER DATA NEEDED)

Strongest block: **D — Balance Sheet Strength (20/20)**. Net cash of
Rs 292.75 Cr, near-zero leverage, current ratio 5.04x.

Weakest block: **A — Return on Capital (7/20)**, a genuine depressor (not
a data gap): the post-IPO treasury cash pile inflates capital employed
faster than operating EBIT grows, pulling computed ROCE to 5.5-9.8%.
Block E (0/20) is separately weak but purely on data availability, not a
demonstrated finding.

## DATA CONFIDENCE

9 years of annual P&L/PAT history (FY2018-FY2026) → 7-9 band → **moderate**
confidence for revenue/PAT/margin trend metrics. No history-based
downgrade applies (moderate tier does not trigger the "may not have seen
full cycle" flag or a tier downgrade). However, the balance-sheet-dependent
sub-metrics (ROCE, WC Days, FCF) carry materially lower confidence,
computable for only 2 of the 9 years (FY25-FY26), because the screener
export does not carry the current/non-current liability split, Trade
Payables, or capex lines for FY2018-FY2024.

## CLASSIFICATION AND DEAL-BREAKERS

Baseline from matrix: Core score 46 falls in the 40-59 band → **AVERAGE**
(moat tier is not consulted at this Core band).

Deal-breaker overrides checked:
1. Block A (7) < 8 → max GOOD. **FIRES.**
2. Block B (11) ≥ 8 → not triggered.
3. Median ROCE (7.68%) < 10% → max AVERAGE. **FIRES.**
4. Cumulative CFO/PAT (96.9% cumulative FY20-26) ≥ 0.50 → not triggered.
5. Pledge > 15% → unknown (N/A, not in provided data); cannot fire on
   unverified data.
6. ND/EBITDA > 3x AND IC < 3x → not triggered (net cash, IC 203.4x).
7. Revenue declined in majority of years → not triggered (3/8 = 37.5%).
8. PAT negative in any of last 3 years → not triggered (all positive).
9. History < 3 years → not triggered (9 years available).

The tightest applicable cap (deal-breaker #3, AVERAGE) matches the
matrix-baseline result. **Final classification: AVERAGE.**

## DECISION LINE

Classification: **AVERAGE**. Depressors are (a) ROCE diluted by a large
post-IPO cash balance not yet deployed into proportionate operating
earnings, (b) EBITDA margin compression of ~7.9pp FY18-FY26 despite
double-digit revenue CAGR, (c) an uneven growth path with 3 of the last 8
years showing revenue decline, and (d) a moat profile that scores near-zero
largely because peer/segment benchmarking data was not provided (4 of 12
tests are PEER DATA NEEDED, not demonstrated absence). Balance sheet
strength is excellent (20/20, net cash). Gate 0 does not halt on company
quality; this classification and its depressors carry forward as flags,
not a stop. The unresolved SPEAR net-cash-decline discrepancy (found
INCREASE, not decline) is the single highest-priority item for the next
verification pass, since it is an explicit load-bearing fact for this run.

---
```yaml
stage: B01-gate0
company: "DIVGIITTS"
run_date: "2026-08-29"
model: claude-sonnet-5
status: complete
input_gaps:
  - "prospectus (ABSENT, carried from B00)"
  - "credit rating (ABSENT, carried from B00)"
  - "announcements corpus (ABSENT, carried from B00)"
  - "shareholding pattern (ABSENT, carried from B00) - drives Block E to 0"
  - "research reports (ABSENT, carried from B00)"
  - "screener export lacks current/non-current liability split for FY2018-FY2024 - limits ROCE to FY25-FY26 only"
  - "screener export lacks Trade Payables line for FY2018-FY2024 - limits WC Days trend to FY25-FY26 only"
  - "screener export lacks capex breakout for FY2018-FY2024 - limits FCF calc to FY25-FY26 only (PDF-sourced)"
  - "R&D expenditure not disclosed as a separate line in any provided source"
  - "no peer/segment benchmarking data provided - affects M2, M5, M7, M9"
  - "contingent liabilities not disclosed in provided results filings (no notes section)"
  - "FY25 Interest/Finance Cost discrepancy: screener 0.60 Cr vs FY26 filing's audited FY25 comparative 0.382 Cr - unresolved, used PDF audited figure"
flags:
  - type: FLAG-GATE0
    reason: "Classification AVERAGE. Median ROCE 7.68% (FY25-26, only computable years) driven by outsized post-IPO cash pile (~Rs 283-295 Cr) inflating capital employed relative to operating EBIT; EBITDA margin compressed ~7.9pp FY18-FY26 despite 10.4% revenue CAGR; 3 of last 8 years show revenue decline."
data_years: 9
fy_range: "FY2018 to FY2026"
blocks: {A: 7, B: 11, C: 8, D: 20, E: 0}
core_score: 46
moat_score: 1
grand_total: 47
moats_confirmed: 0
moat_class: "NONE"
classification: "AVERAGE"
deal_breakers:
  - "rule 1: Block A total 7 < 8 -> caps at max GOOD"
  - "rule 3: median ROCE 7.68% < 10% -> caps at max AVERAGE (binding cap)"
history_downgrade: false
data_notes:
  - "ROCE computable only for FY25 and FY26 (screener export lacks current/non-current liability split for FY18-FY24); Capital Employed sourced from audited results-filing balance sheets."
  - "FCF computable only for FY25 and FY26 (capex breakout only in results filings; screener gives combined investing cash flow only for FY18-FY24)."
  - "WC Days computable only for FY25 and FY26 (Trade Payables absent from screener export for FY18-FY24)."
  - "WC Days computed on revenue basis; COGS not explicitly isolated in provided data."
  - "PEER DATA NEEDED: M2, M5, M7(partial), M9 - no peer/segment data provided; scored 0."
  - "No loss-to-profit swing in the 9-year window; PAT positive all years FY2018-FY2026."
  - "SPEAR load-bearing fact 'approximately Rs 275 Cr net cash decline in FY26' NOT corroborated: computed net cash rose from Rs 283.76 Cr (FY25) to Rs 292.75 Cr (FY26), an increase of ~Rs 9 Cr. Flagged for downstream verification of the original source."
  - "SPEAR load-bearing fact 'June 2026 FY25 results resubmission' not verifiable from provided data; only FY25 comparative available (dated 25-May-2026) predates the stated resubmission date."
block_b_trend: "deteriorating - FCF swung from +Rs 8.71 Cr (FY25) to -Rs 3.24 Cr (FY26) as FY26 capex (Rs 44.32 Cr) outpaced CFO (Rs 41.08 Cr), despite WC days improving by 14.4 days and 96.9% cumulative CFO/PAT conversion (FY20-26)."
analyst_note: "AVERAGE is driven by real numbers, not gaps. Cash-heavy post-IPO balance sheet (Rs 292.75 Cr net cash) mechanically depresses ROCE to single digits even though ROE and absolute profit hold up better. Margin compressed 7.9pp over 8 years despite growth, and growth itself is lumpy (3 of 8 years down). Moat score of 1/60 is misleading in isolation: 4 of 12 tests are blocked purely by missing peer data, not evidence of no moat, so downstream stages should not read NONE as a settled verdict on competitive position. Highest-priority open item: the SPEAR fact of a ~Rs 275 Cr FY26 net cash decline could not be reproduced from any provided document; the computed direction is an increase. This needs resolution before it is used as a load-bearing fact in later stages."
```
