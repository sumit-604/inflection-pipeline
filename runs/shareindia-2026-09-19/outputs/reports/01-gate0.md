# STAGE 1: GATE 0 SCORECARD — SHARE INDIA SECURITIES LTD (SHAREINDIA)
Run date: 2026-09-19. Consolidated financials primary (screener CSVs, INR Cr,
rounded). Standalone not used except where noted.

Data available: 11 years (FY16 to FY26), FY16-FY26 P&L/balance sheet/cash
flow; ROCE series FY17-FY26 (10 years, screener does not report a Mar-2016
ROCE). Scoring adapted to 11-year history (10+ years = full confidence, no
downgrade).

Business note carried into this scorecard: Share India is a diversified
capital-market intermediary (proprietary trading, client broking, MTF
lending, an NBFC subsidiary with AUM Rs 265.3 Cr, merchant banking). It has
no listed peer row in the Section 1B sector cap table; B00 assigned
"Banks / NBFCs / MFIs" as the closest row (flagged for Phase 3 operator
confirmation). Several Block D and Block F tests are built for a
manufacturing/trading company or for a pure lender and do not fit this
business cleanly. Every such mismatch is named below, scored per the
instruction file's literal rule (never invented), and flagged.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Source: screener-data, consol ratios CSV, "ROCE %" row (screener's own
figure, used per formula-definitions rule; not recomputed).

| Year | FY17 | FY18 | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|---|---|---|---|
| ROCE % | 28 | 32 | 26 | 24 | 36 | 57 | 52 | 38 | 21 | 18 |

(screener-data, consol ratios CSV, ROCE % row, Mar2017..Mar2026 columns)

- **A1 Median ROCE** = 30% (median of 10 values, sorted 18/21/24/26/28/32/
  36/38/52/57, median of (28,32)) (screener-data, consol ratios CSV). Band
  ≥25% = **5**
- **A2 Minimum single-year ROCE** = 18% (FY26, the low of the series)
  (screener-data, consol ratios CSV, Mar2026). Band ≥15% = **5**
- **A3 Median ROE** = 26.67% (computed: PAT ÷ average Net Worth, screener-
  data consol P&L "Net Profit" row and consol balance sheet "Equity
  Capital" + "Reserves" rows; FY16 uses closing net worth only, opening
  (FY15) not in provided data, stated). 11-year series: FY16 23.08%, FY17
  26.67%, FY18 28.04%, FY19 21.65%, FY20 23.36%, FY21 34.25%, FY22 55.57%,
  FY23 45.56%, FY24 30.96%, FY25 16.08%, FY26 13.04%; median = FY17 value
  26.67%. Band ≥20% = **5**
- **A4 ROCE trend, latest vs earliest** = FY26 18% vs FY17 28% = decline of
  10pp (screener-data, consol ratios CSV). Band decline >5pp = **0**

**Block A = 15/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

Source: screener-data, consol cash-flow CSV ("Cash from Operating Activity",
"Free Cash Flow" rows) and consol P&L CSV ("Net Profit" row), FY16-FY26.

| Year | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CFO (Cr) | 10 | 14 | 22 | 49 | 68 | 236 | 409 | -170 | -310 | 6 | -182 |
| PAT (Cr) | 6 | 8 | 15 | 25 | 41 | 81 | 202 | 331 | 426 | 328 | 324 |
| FCF (Cr) | 8 | 12 | 22 | 47 | 65 | 227 | 391 | -181 | -328 | 4 | -186 |

(screener-data, consol cash-flow CSV rows "Cash from Operating Activity" and
"Free Cash Flow"; consol P&L CSV row "Net Profit")

- **B1 Cumulative CFO ÷ Cumulative PAT** = 152 Cr ÷ 1,787 Cr = **0.085**
  (screener-data, consol cash-flow + P&L CSVs, FY16-FY26 sums). Band <0.50
  = **0**
- **B2 FCF-positive years** = 8 of 11 (FY16,17,18,19,20,21,22,25 positive;
  FY23,24,26 negative) = 72.7% (screener-data, consol cash-flow CSV, FCF
  row). Band 50-74% = **2**
- **B3 Cumulative FCF ÷ Cumulative PAT** = 81 Cr ÷ 1,787 Cr = **0.045**
  (screener-data, consol cash-flow + P&L CSVs, FY16-FY26 sums). Band
  <0.20 or negative = **0**
- **B4 Change in WC Days, latest vs earliest** = FY26 -139 days vs FY16 +29
  days = decreased 168 days (screener-data, consol ratios CSV, "Working
  Capital Days" row, used directly per source; Receivable/Inventory/
  Payable-day components are blank in the source for FY16-FY24, so the
  source's own WC-days figure is used rather than rebuilt from parts).
  Band decreased >5 days = **5**

**Block B = 7/20**

data_note: block_b_trend = **deteriorating**. CFO was negative in 3 of the
last 4 years (FY23 -170 Cr, FY24 -310 Cr, FY26 -182 Cr), with only FY25's
+6 Cr as a brief positive between two large negative years. Cumulative
CFO/PAT of 0.085 over 11 years means the P&L profit has barely converted to
cash at all across the period, driven by the FY23-24-26 pattern, not offset
by the earlier (FY16-22) strongly cash-generative years. This is LBF3 from
company memory (CFO negative FY23/FY24/FY26); the filings confirm the
negative-CFO years exactly as flagged, and this scorecard finds no year
since FY22 where CFO exceeded FCF's small positive FY25 print. Growth-
induced (MTF book funding, exchange margin placement) vs structural
(trading inventory) is not resolvable from screener CSVs alone; this is a
Halt-1 verification item, not a Gate-0 finding.

---

## BLOCK C: GROWTH (Max 20)

Source: screener-data, consol P&L CSV, "Sales" and "Net Profit" rows,
FY16-FY26.

| Year | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Sales (Cr) | 74 | 110 | 138 | 206 | 228 | 453 | 862 | 1,088 | 1,483 | 1,449 | 1,470 |
| PAT (Cr) | 6 | 8 | 15 | 25 | 41 | 81 | 202 | 331 | 426 | 328 | 324 |

(screener-data, consol P&L CSV)

- **C1 Revenue CAGR** (FY16→FY26, 10-year) = (1,470÷74)^(1/10)-1 = **34.8%**
  (screener-data, consol P&L CSV). Band ≥20% = **5**
- **C2 PAT CAGR** (FY16→FY26, 10-year) = (324÷6)^(1/10)-1 = **49.0%**
  (screener-data, consol P&L CSV). Band ≥20% = **5**
- **C3 Positive YoY revenue years** = 9 of 10 (only FY25 declined, 1,449 <
  1,483) = 90% (screener-data, consol P&L CSV). Band 75-99% = **3**
- **C4 PAT CAGR − Revenue CAGR** = 49.0% − 34.8% = **+14.2pp**
  (computed from C1/C2). Band ≥+3pp = **5**

**Block C = 18/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

Share India is classified under the "Banks / NBFC / Insurance" alternate
rule (B00 sector-cap-row assignment, flagged for Phase 3 confirmation),
but it is a diversified capital-markets group whose NBFC subsidiary (AUM
Rs 265.3 Cr, AR p.74/printed 71) is a small slice of the Rs 4,590 Cr
consolidated balance sheet (screener-data, consol BS CSV, Mar2026 Total
Assets). The alternate metrics below (CAR, PCR) are disclosed, if at all,
only at the NBFC-subsidiary level, not group-wide. This mismatch is named
per stage instructions ("where a metric does not fit a financial
intermediary, say so"), scored as the rule requires, and flagged.

- **D1 Net Debt ÷ EBITDA / CAR** — Capital Adequacy Ratio is **N/A (not in
  provided data)**. No CAR % is disclosed anywhere in the screener CSVs,
  results text, or AR text searched. Score = **0**. (Data note: gross
  Borrowings FY26 = Rs 695 Cr, EBITDA-proxy Operating Profit FY26 = Rs 570
  Cr [screener-data, consol BS and P&L CSVs] would give a gross-debt
  multiple of ~1.2x, but cash is not broken out from "Other Assets" in the
  screener balance sheet, so a true Net Debt figure cannot be built either;
  this is shown for context only, not scored.)
- **D2 Interest Coverage / PCR** — Provision Coverage Ratio computed as a
  **proxy** from AR-disclosed asset-quality figures for the NBFC subsidiary
  only: GNPA 4.30%, NNPA 2.66% (AR p.74/printed 71, "Asset quality remained
  healthy, with GNPA of 4.30% and NNPA of 2.66%"). PCR proxy = (GNPA−NNPA)
  ÷ GNPA = (4.30−2.66)÷4.30 = **38.1%**. Band <60% = **0**. Flagged as a
  proxy, not a source-reported PCR, and as subsidiary-level not group-
  level. (Data note: a general-corporate Interest Coverage is computable
  from the same P&L — EBIT (PBT+Interest) FY26 = 440+131 = 571 Cr ÷
  Interest 131 Cr = 4.36x [screener-data, consol P&L CSV], which would
  score 2 under the non-financial band — shown for cross-check only.)
- **D3 Debt ÷ Equity** — Financials default = **3** per instruction file
  ("Financials: default 3"). (Data note: computed D/E FY26 = Borrowings
  695 Cr ÷ Net Worth 2,635 Cr [44+2,591] = 0.26x, screener-data, consol BS
  CSV, Mar2026 — would score 4 under the general-corporate band, shown for
  context only; the financials default of 3 is what is scored.)
- **D4 Current Ratio** — **N/A (not in provided data)**. The screener
  consolidated balance sheet has no Current Assets/Current Liabilities
  split (only Total Liabilities, Borrowings, Other Liabilities, Fixed
  Assets, CWIP, Investments, Other Assets). Ind AS financial-services
  balance sheets are presented in order of liquidity, not current/non-
  current classification, so this line structurally does not exist for
  this business. Score = **0**.

**Block D = 3/20**

data_note: Block D's low score is a data-fit and data-availability
artifact for a diversified capital-markets intermediary, not a confirmed
finding of balance-sheet distress. The general-corporate cross-checks shown
above (gross debt/EBITDA ~1.2x, interest coverage 4.36x, D/E 0.26x) do not
suggest an overleveraged group; they cannot be scored under the file's
Banks/NBFC substitution rule because CAR and a group-wide PCR are not
disclosed in the provided corpus. FLAG for Phase 3: confirm the correct
sector-cap-row treatment for Block D (echoes the same open flag in B00 for
the Section 1B sector cap).

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

- **E1 Promoter holding (latest quarter)** = 48.62% (screener-data, consol
  shareholding CSV, Jun 2026 column). Band 40-49.9% = **3**
- **E2 Promoter holding change over ~3 years** = Sep 2023 52.81% → Jun 2026
  48.62% = **decreased 4.19pp** (screener-data, consol shareholding CSV,
  Sep2023 and Jun2026 columns; the provided quarterly series starts Sep
  2023, so the window is ~2.75 years, not a clean FY-anchored 3 years —
  nearest available endpoints used, stated). Band decreased >3% = **0**
- **E3 Promoter pledge (latest)** = **57.80%** of promoter holding, 28.10%
  of total share capital, 6,14,92,594 shares (BSE SHP summary, quarter
  ending Jun 2026, promoter row "No. of Shares pledged or otherwise
  encumbered"). Band >15% = **0**. Confirms LBF2: pledge rose from 52.16%
  of promoter holding (Sep 2025, BSE SHP summary) to 57.80% (Jun 2026),
  i.e. the filings show the pledge climb load-bearing fact is real and
  current at scorecard date.
- **E4 Contingent liabilities ÷ Net Worth (latest)** = Rs 3,233.44 Cr ÷
  Rs 2,635 Cr = **122.7%**. Contingent liabilities FY26 = guarantees given
  Rs 3,23,271.75 lakh + income-tax demand Rs 68.15 lakh + indirect-tax
  demand Rs 3.79 lakh = Rs 3,23,343.69 lakh = Rs 3,233.44 Cr (AR p.287/
  printed 284, Note 44, "Contingent liabilities and commitment", column
  "As at March 31, 2026"). Net Worth = Equity Capital 44 + Reserves 2,591
  = Rs 2,635 Cr (screener-data, consol BS CSV, Mar2026). Band >30% = **0**.
  Confirms and updates LBF2 (screener's cited Rs 2,182 Cr is the FY25
  figure, Rs 2,18,197.82 lakh, AR p.287 comparative column — the FY26
  figure is 48% higher). Guarantees are almost entirely NSE Clearing /
  MCX Clearing bank guarantees for exchange margin requirements (AR
  p.287-288, Note 44(a) breakdown).

**Block E = 3/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Peer set used where peer data is scored: Angel One (ANGELONE), Choice
International (CHOICEIN), SMC Global Securities (SMCGLOBAL) — consolidated
screener CSVs, FY26 column, the only peer data provided in this run's
inputs/screening folder.

- **M1 Pricing Power** = EBITDA margin (OPM%) FY16 19% → FY26 39%, expanded
  20pp (screener-data, consol P&L CSV, OPM % row); revenue CAGR 34.8%
  (from C1). Both conditions of the top band met. = **5**
- **M2 Cost Advantage vs peer median EBITDA margin** = SHAREINDIA OPM FY26
  39% vs peer median 35% (peers FY26 OPM: Angel One 35%, Choice
  International 36%, SMC Global 20%, screener-data consol P&L CSVs;
  median of the three = 35%). Diff = **+4pp**. Band 2-5pp above = **3**
- **M3 Capital Efficiency** = Fixed Asset Turnover FY26 = Sales 1,470 Cr ÷
  Fixed Assets 65 Cr (screener-data, consol P&L and BS CSVs) = **22.6x**;
  ROCE FY26 = 18% (from Block A). FAT>3x AND ROCE>20% fails (ROCE 18%<20%);
  FAT>2x AND ROCE>15% holds. = **3**. Note: the very high FAT is a
  structural feature of a people/technology-led intermediary with most of
  the balance sheet in "Other Assets" (client funds, margin, trade
  receivables), not evidence of manufacturing-style capital efficiency;
  named, not treated as a red flag.
- **M4 Customer Stickiness** = 1 revenue-decline year (FY25, 1,449 < 1,483)
  (screener-data, consol P&L CSV). FY26 revenue 1,470 Cr is 99.1% of the
  FY24 pre-decline peak of 1,483 Cr — growth resumed but the prior peak is
  not yet fully re-taken. Scored against the closest defined band ("max 1
  decline year, fully recovered = 3"); the 0.9% shortfall to the prior peak
  is a near-miss, flagged rather than silently rounded. = **3 (judgment
  call flagged)**
- **M5 Scale & Dominance** = **PEER DATA NEEDED**. Market capitalisation is
  not present in any provided screener CSV (financial-statement rows only;
  no valuation/mcap line). Cannot rank vs peers. = **0**
- **M6 Technology / R&D** = **N/A (not in provided data)**. No R&D spend
  is disclosed by this broking/NBFC group in the provided corpus. = **0**
- **M7 Regulatory / License** = SEBI-regulated capital-market intermediary,
  but the segment has far more than 10 listed players (Angel One, Choice
  International, SMC Global, Motilal Oswal, IIFL, 5paisa, Geojit, Anand
  Rathi, Nuvama, JM Financial and others; company identity from B00/AR,
  count is general market knowledge of listed brokers, not a filed
  number). Band "regulated but >10 players" = **1**
- **M8 Distribution** = Broking network "95 branches across 13 states"
  (AR-FY26, "investors through a network of 95 branches across 13
  states"); NBFC network "73 branches" FY26 vs "80 branches and
  franchises" FY25 (AR-FY26 vs AR-FY25 texts) — a **decline**, not growth,
  on the one comparable NBFC-branch count available. The broking-network
  FY25 comparator ("280 branches and franchises", AR-FY25) uses a
  different, non-comparable category to FY26's "95 branches" figure, so
  no clean growth comparison is possible from provided data. Reach is
  quantified but growth is not confirmed (one comparable series shows
  decline). = **0**
- **M9 Brand** = Same OPM comparison as M2: SHAREINDIA 39% is only 4pp
  above the 3-peer median of 35% (screener-data, consol P&L CSVs, FY26),
  below the ≥5pp threshold needed for any scoring band above 0 despite
  strong revenue CAGR (34.8%, well past the growth thresholds in every
  band). None of the defined bands cleanly fit a "narrowly above peers,
  growth strong" case; scored at the most conservative literal reading.
  Gross-margin proxy not used (no material cost line for a broking/NBFC
  business; OPM used in its place, stated). = **0**
- **M10 Switching Costs** = Revenue grew all years but FY25 (from C3, 9 of
  10 years); Debtor Days fell from 91 (FY16) to 9 (FY26) (screener-data,
  consol ratios CSV) — a large decrease, which satisfies "rose ≤10 days"
  (a decrease is included). Band "growth all but 1 year AND stable" = **3**
- **M11 Network Effects** (11 years available, ≥6-year test qualifies) =
  Latest 3-year revenue CAGR (FY23→FY26) = (1,470÷1,088)^(1/3)-1 = **10.6%**;
  prior 3-year CAGR (FY20→FY23) = (1,088÷228)^(1/3)-1 = **68.4%**
  (screener-data, consol P&L CSV). Latest CAGR is well below prior CAGR —
  growth is decelerating, not accelerating. Selling-expense % is **N/A (not
  in provided data)**: the screener P&L gives one combined "Expenses" line,
  no separate selling-expense row. Neither top band (accelerating growth)
  nor the ≥20%-CAGR band (10.6%<20%) is met. = **0**
- **M12 Negative WC / Float** = WC Days negative in 10 of 11 years (all
  except FY16, +29 days) (screener-data, consol ratios CSV, "Working
  Capital Days" row). Majority-negative = **5**

**Block F = 23/60. Moats present (score ≥3): M1, M2, M3, M4, M10, M12 = 6.**

**Moat classification: 6+ present = FORTRESS.**

data_note: this FORTRESS reading rests on several borderline or
data-limited calls — M2/M3 sit at the bottom of their scoring band, M4 is a
99.1%-of-peak near-miss flagged above, M5/M6/M9/M11 score 0 on missing or
insufficient data rather than confirmed absence of a moat, and M8 shows an
outright branch-count decline on the one comparable series available. The
mechanical FORTRESS label should not be read as an unqualified "wide moat"
finding; it is the literal output of the 12-test formula given the
evidence in hand, most of it thin. Downstream stages should treat the
individual test results, not the aggregate label, as the load-bearing
output.

---

## CLASSIFICATION

- Core score (Blocks A-E) = 15 + 7 + 18 + 3 + 3 = **46 / 100**
- Moat score (Block F) = **23 / 60**
- **Grand total = 69 / 160**
- Data confidence: 11 years available → **10+ yrs, full confidence** (no
  history downgrade)

Classification matrix: Core 40-59 = **AVERAGE** (flat rule, independent of
moat classification at this core band).

**Deal-breaker overrides triggered** (recorded per instruction file; cap
classification, do not change the core-band result here since it is
already AVERAGE):
1. **#2 Block A/B <8** — Block B = 7 < 8 → max GOOD (superseded by #4 below)
2. **#4 Cumulative CFO ÷ PAT <0.50** — 0.085 < 0.50 → max AVERAGE
3. **#5 Pledge >15%** — 57.80% of promoter holding (Jun 2026) → max AVERAGE

Not triggered: #3 median ROCE<10% (30%, not triggered); #6 ND/EBITDA>3x
AND IC<3x (both inputs N/A under the financial-sector substitution rule,
not evaluable, not confirmed triggered); #7 revenue declined majority of
years (1 of 10, not triggered); #8 PAT negative in last 3 years (FY24/25/26
all positive, not triggered); #9 history <3 years (11 years available, not
triggered).

Which years drive the deal-breakers, named per pipeline instruction: Block
B's collapse is driven by FY23 (CFO -170 Cr), FY24 (CFO -310 Cr) and FY26
(CFO -182 Cr) against FY16-22's strongly cash-generative years; the pledge
deal-breaker is a live, worsening, current-quarter fact (Jun 2026), not a
legacy or post-IPO rebase artefact, so the pipeline note's carve-out for
"documented post-IPO rebase / legacy cleanup cases" does not apply here.

## FINAL CLASSIFICATION: AVERAGE

## Strongest block: Block C (Growth), 18/20
## Weakest block: Block D (Balance Sheet Strength), 3/20 — but flagged as
largely a data-fit artifact for this sector, not confirmed weakness; the
more informative weak reading is Block B (Cash Generation Quality), 7/20,
and Block E (Shareholder Alignment), 3/20, both of which are confirmed by
filed evidence (CFO history, pledge %, contingent liabilities), not by data
gaps.

## Decision line
Gate 0 mechanical output is AVERAGE, capped there independently by the
core-score band and by two deal-breakers (cash conversion, pledge). The
FORTRESS moat label is real per the formula but rests on thin/borderline
evidence in six of twelve tests. This is a flag-forward, not a halt: no
Gate 0 finding here stops the pipeline (company-quality never halts a run
per house rule); it hands Halt 1 four things to weigh together with the
load-bearing facts already carried from B00 — LBF2 (pledge, confirmed and
worsening), LBF3 (cash conversion, confirmed and deteriorating), the FY26
contingent-liability jump (new finding, not in B00's LBFs), and the
sector-cap-row mismatch that weakens Block D's and part of Block F's
evidentiary weight.
