# GATE 0 SCORECARD — Trident Lifeline Ltd (TLL), BSE SME 543616
Run date: 2026-09-26 | Basis: Consolidated (five subsidiaries) | Model: claude-sonnet-5

Data available: 5 years (FY22 to FY26), annual P&L and balance sheet
(screener-Data_Sheet.csv). Balance-sheet current-liability / trade-payable
detail needed for ROCE (A1/A2/A4) and Working Capital Days (B4) is only
available for FY24-FY26 (3 years) — the FY26 and FY25 Annual Reports carry
the consolidated current-liabilities split; no FY23/FY22 results filing or
AR is held in this corpus to split current liabilities that far back.
Scoring adapted: Blocks A/B rows that need the split run on the 3-year
FY24-FY26 window; Blocks C, and the P&L-only rows of D/E, run on the full
5-year window. This is stated per row below.

## LOAD-BEARING FACTS CHECK (first priority, per companies/TLL.md SPEAR)

**LBF1 (cash conversion).** Confirmed against the AR consolidated balance
sheet and cash flow statement:
- Trade Receivables Rs 27.68 Cr (FY25) to Rs 73.65 Cr (FY26) (Annual_Report_2026.pdf
  p.[Consolidated Balance Sheet], Note 17: 2,768.25 -> 7,365.39 lakh; matches
  screener-Data_Sheet.csv Receivables row exactly).
- Debtor days: 116.2 (FY25) to 208.4 (FY26), computed as Receivables/Sales x 365
  (screener-Data_Sheet.csv Sales and Receivables rows) — matches the "116 to 208"
  figure in companies/TLL.md exactly.
- CFO Rs +4.69 Cr FY26 on PAT Rs 19.04 Cr FY26 (screener-Data_Sheet.csv; AR
  consolidated cash flow "Net Cash Flow from Operating Activities" 469.07 lakh,
  Annual_Report_2026.pdf p.[Consolidated CF Statement]) — confirmed.
- CFO negative in FY23 (-19.00 Cr) and FY25 (-10.24 Cr) per screener-Data_Sheet.csv
  — also negative in FY22 (-0.21 Cr), so 3 of 5 years, not 2 of 4 as the company
  memory shorthand says; the two named years (FY23, FY25) are confirmed negative.
- GROWTH-INDUCED vs STRUCTURAL classification is a qualitative call outside Gate 0's
  no-judgment mandate; deferred to the stage that reads receivables ageing and
  customer-concentration notes. Gate 0 surfaces the number: Working Capital Days
  rose from 151.1 (FY24) to 202.8 (FY26), a swing that easily explains the CFO/PAT
  gap on its own, independent of a structural-vs-growth read.

**LBF2 (refiled results / accounting quality).** Two findings from Gate 0's own
extraction (not a full refiling comparison, which is a later-stage task):
1. **Other income share of PBT confirmed and traced.** Other Income Rs 8.23 Cr
   FY25 / Rs 9.27 Cr FY26 against PBT Rs 13.62 / 27.19 Cr (screener-Data_Sheet.csv)
   = 60.4% and 34.1% of PBT respectively. Traced to AR consolidated Note 22
   (Annual_Report_2026.pdf, Note 22 "OTHER INCOME"): the single largest FY26
   line is **"Claim Income" Rs 5.41 Cr**, 58% of the Rs 9.27 Cr other-income total
   and 20% of FY26 PBT on its own; the rest is FX gain (Rs 1.37 Cr), interest income
   on advances/FDs (Rs 2.63 Cr), duty drawback (Rs 0.57 Cr) and small items. "Claim
   Income" is not defined in the note text extracted; its nature (insurance claim,
   export-incentive claim, other) is NOT FOUND in the provided data. FLAGGED for a
   note-level dive at the qualitative stage — a swing item this size, unexplained,
   is exactly the kind of number a destination-PE case cannot rest on.
2. **A cash-flow restatement was found, not looked for.** The FY25 Annual Report
   (audited then) reports FY25 consolidated CFO as **-Rs 10.24 Cr** (-1,024.17 lakh,
   Annual_Report_2025.txt, Consolidated Cash Flow Statement, line "Net Cash Flow
   from Operating Activities"). The FY26 Annual Report's FY25 comparative column
   for the same line reads **-Rs 3.99 Cr** (-398.50 lakh, Annual_Report_2026.txt,
   Consolidated Cash Flow Statement). That is a Rs 6.26 Cr swing in a previously
   audited number, with no restatement note located in the text searched. Gate 0
   scored Block B on the screener figure, which equals the originally-filed FY25
   AR figure (-10.24 Cr), per this stage's instruction to use the provided
   Data_Sheet consistently. FLAGGED (FLAG-DATA-QUALITY) for the accounting-quality
   read at the qualitative stage — whichever figure is correct, a Rs 6+ Cr
   unexplained CFO restatement is load-bearing.
   Refiling of the H1 FY25 and H1 FY26 RESULTS themselves (trade-payable
   bifurcation per the BSE query) was not re-compared line-by-line here; that
   remains open per companies/TLL.md LBF2 and is not resolved by this stage.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — computed, FY24-FY26 window

EBIT computed as PBT + Interest - Other Income (operating basis). Other Income
is 34-60% of PBT in the two latest years (LBF2 above); an EBIT that folds it in
would materially inflate every ROCE figure below, so the operating basis is
used as the primary score, with the all-in alternative shown for the record.

Capital Employed = Total Assets - Current Liabilities. Current Liabilities from
AR consolidated balance sheet (screener Data_Sheet's "Other Liabilities" row
does not split current from non-current, so this stage went to the AR for the
split):
- FY24: CL Rs 20.26 Cr (Annual_Report_2025.txt, Consolidated Balance Sheet, "(4)
  Current Liabilities Total" 2,025.62 lakh); TA Rs 87.08 Cr (screener-Data_Sheet.csv,
  matches AR 8,707.62 lakh)
- FY25: CL Rs 53.55 Cr (Annual_Report_2026.txt, Consolidated Balance Sheet FY25
  comparative, 5,355.46 lakh); TA Rs 156.01 Cr (AR) / 155.54 Cr (screener, used TA
  from AR for consistency with the AR-sourced CL)
- FY26: CL Rs 87.89 Cr (Annual_Report_2026.txt, Consolidated Balance Sheet,
  8,789.27 lakh); TA Rs 236.83 Cr (screener-Data_Sheet.csv, matches AR exactly)

| Year | EBIT (op.) | Capital Employed | ROCE (op.) | ROCE (all-in, PBT+Int) |
|---|---|---|---|---|
| FY24 | 7.26 Cr | 66.82 Cr | 10.87% | 13.98% |
| FY25 | 9.53 Cr | 102.46 Cr | 9.30% | 17.33% |
| FY26 | 22.04 Cr | 148.94 Cr | 14.80% | 21.02% |

(All figures: screener-Data_Sheet.csv P&L rows, computed; AR sources for CL/TA
as cited above.)

- **A1 Median ROCE (op.) = 10.87%** -> band 10-14.9% = **1**
  (all-in basis would give median 17.33% -> band 15-19.9% = 3; footnoted, not used)
- **A2 Minimum single-year ROCE (op.) = 9.30%** (FY25) -> band 8-11.9% = **1**
- **A3 Median ROE = 23.10%** (FY26; PAT/avg Net Worth, screener-Data_Sheet.csv
  PAT and Equity Share Capital+Reserves rows; FY22 uses closing NW only, no
  opening NW available pre-IPO, stated) -> band ≥20% = **5**
  (5-year series: FY22 82.6%* FY23 23.9% FY24 12.9% FY25 20.0% FY26 23.1%;
  *FY22 distorted by a near-zero pre-IPO equity base, kept per no-estimate rule)
- **A4 ROCE trend, FY26 (14.80%) vs FY24 (10.87%)**: latest ≥ earliest -> **5**

**Block A = 12/20**

## BLOCK B: CASH GENERATION QUALITY (Max 20) — computed, 5-year window (B1-B3), 3-year window (B4)

- **B1 Cumulative CFO / Cumulative PAT**: CFO sum FY22-26 = -0.21-19.00+2.23-10.24+4.69
  = **-22.53 Cr**; PAT sum = 3.95+6.02+6.34+11.75+19.04 = **47.10 Cr** (screener-Data_Sheet.csv).
  Ratio = -0.478 -> band <0.50 = **0** [DEAL-BREAKER #4]
- **B2 FCF-positive years proportion**: FCF proxied as CFO + net Investing CF
  (screener-Data_Sheet.csv "Cash from Investing Activity" row), because the AR's
  own "Purchase of Fixed Assets" cash-flow line could not be cleanly separated
  from acquisition-of-subsidiary outflows in the extracted text (see data_notes).
  This proxy is punitive: it folds the TNS/Mediquip/Parenterals acquisition cash
  (LBF3) into "capex". All 5 years negative: FY22 -0.66, FY23 -28.69, FY24 -18.13,
  FY25 -23.95, FY26 -31.92 -> 0% positive -> band <50% = **0**
- **B3 Cumulative FCF / Cumulative PAT**: cumulative FCF (proxy) = -103.35 Cr;
  PAT = 47.10 Cr -> ratio negative -> **0**
- **B4 Change in WC Days, FY26 vs FY24** (3-year window; see Block A note on
  why FY22-23 are excluded): Receivable Days + Inventory Days - Payable Days,
  Trade Payables from AR consolidated balance sheet (FY24 Rs 7.54 Cr, FY25
  Rs 14.79 Cr, FY26 Rs 38.43 Cr; Annual_Report_2025/2026.txt Consolidated BS
  Note 7). WC Days: FY24 = 151.1, FY25 = 172.7, FY26 = 202.8. Change = +51.7
  days -> band increased >15 days = **0**

**Block B = 0/20** [DEAL-BREAKER #2: Block B <8 -> max GOOD]

**block_b_trend: DETERIORATING** — cumulative CFO is negative (-Rs 22.5 Cr)
against cumulative PAT of Rs 47.1 Cr FY22-26; Working Capital Days rose from
151 (FY24) to 203 (FY26), +52 days in two years (screener-Data_Sheet.csv,
AR trade payables notes).

## BLOCK C: GROWTH (Max 20) — computed, 5-year window

All from screener-Data_Sheet.csv Sales / Net profit rows, FY22-FY26.

- **C1 Revenue CAGR** = (129.02/21.77)^(1/4)-1 = **56.05%** -> band ≥20% = **5**
- **C2 PAT CAGR** = (19.04/3.95)^(1/4)-1 = **48.16%** -> band ≥20% = **5**
- **C3 Positive YoY revenue years**: FY23 +45.6%, FY24 +40.9%, FY25 +94.7%,
  FY26 +48.4% -> 4/4 = 100% -> **5**
- **C4 PAT CAGR - Revenue CAGR** = 48.16% - 56.05% = **-7.89pp** -> band
  -3 to -8pp = **1**

**Block C = 16/20**

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — latest = FY26, computed

- **D1 Net Debt / EBITDA**: Net Debt = Borrowings 72.99 Cr - Cash 4.22 Cr =
  68.77 Cr (screener-Data_Sheet.csv). EBITDA (operating) = PBT+Interest+Dep-
  OtherIncome = 27.19+4.12+6.07-9.27 = 28.11 Cr. Ratio = **2.45x** -> band
  2-3x = **1**
- **D2 Interest Coverage, EBIT(op.)/Interest** = 22.04/4.12 = **5.35x** ->
  band 5-9.9x = **4**
- **D3 Debt/Equity** = Borrowings 72.99 Cr / (Share Capital+Reserves+Minority
  Interest 100.40+7.49=107.89 Cr) = **0.68x** -> band 0.5-1.0x = **3**
  (excluding minority interest: 72.99/100.40 = 0.73x, same band)
- **D4 Current Ratio**: Current Assets Rs 139.51 Cr / Current Liabilities
  Rs 87.89 Cr (Annual_Report_2026.txt, Consolidated Balance Sheet, Current
  Assets Total 13,951.49 lakh, Current Liabilities Total 8,789.27 lakh) =
  **1.59x** -> band 1.5-1.99x = **4**

**Block D = 12/20**

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — latest = Jun-2026 where noted

- **E1 Promoter holding, latest quarter (Jun-2026) = 62.59%** (inputs/shareholding/
  screener-shareholding-pattern.csv — a screener aggregation, NOT a filing; the
  filed FY26 AR shareholding table (Annual_Report_2026.txt, note 1.6) lists
  individual promoters but the text extraction did not cleanly capture a summed
  "Total promoter %" row, so the screener aggregate is used and flagged as
  non-filing per B00) -> band ≥60% = **5**
- **E2 Promoter holding change over ~3 years** (Sep-2023 70.04% to Jun-2026
  62.59%, same source) = **-7.45pp** -> band decreased >3% = **0**
- **E3 Promoter pledge (latest) = NOT FOUND in provided data.** shareholding/
  folder holds only the non-filing screener table (no pledge column); the AR's
  simplified promoter table (note 1.6) carries no pledge column either; the
  formal SEBI SHP-I filing that would carry it is not in this corpus (B00 gap).
  Scored **0** per the no-estimate rule, not assumed 0% or >15%.
- **E4 Contingent Liabilities / Net Worth**: Consolidated contingent liabilities
  (corporate guarantees to Talon Healthcare LLP & Tench Life Sciences LLP)
  Rs 5.00 Cr FY26 (Annual_Report_2026.txt, Note 32 "CONTINGENT LIABILITIES AND
  COMMITMENTS", consolidated, Total 500.00 lakh). Net Worth (Share Capital +
  Reserves, excl. minority interest) Rs 96.68 Cr. Ratio = **5.17%** -> band
  5-15% = **3** (boundary-sensitive: including minority interest in net worth
  gives 4.80%, band <5% = 5; the stricter, excl.-minority basis is used and
  scored)

**Block E = 8/20**

---

## CORE SCORE

| Block | Score | /20 |
|---|---|---|
| A — Return on Capital | 12 | 20 |
| B — Cash Generation | 0 | 20 |
| C — Growth | 16 | 20 |
| D — Balance Sheet | 12 | 20 |
| E — Shareholder Alignment | 8 | 20 |
| **CORE TOTAL** | **48** | **100** |

Strongest block: C (Growth), 16/20. Weakest block: B (Cash Generation), 0/20 —
the widest possible spread on this scorecard.

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Peer set: CAPLIPOINT, SENORES, INNOVACAP Data_Sheet.csv (FY26 column), per
runs/tll-2026-09-26/inputs/screening/.

- **M1 Pricing Power**: EBITDA margin (op.) FY22 = 12.5% (2.72/21.77), FY26 =
  21.8% (28.11/129.02) -> expanded +9.3pp AND revenue CAGR 56% ≥10% -> **5**
- **M2 Cost Advantage vs peer median EBITDA margin**: TLL FY26 21.8% vs peer
  median 26.6% (CAPLIPOINT 35.0%, SENORES 26.6%, INNOVACAP 14.9%; computed
  same operating-EBITDA basis from each peer Data_Sheet.csv) -> BELOW peer
  median -> **0**
- **M3 Capital Efficiency**: FAT = Sales/Net Block = 129.02/60.73 = 2.12x;
  ROCE (op.) FY26 = 14.80% -> FAT>1x AND ROCE>12% (next tier down; FAT>2x AND
  ROCE>15% narrowly missed on ROCE) -> **1**
- **M4 Customer Stickiness**: zero revenue-decline years (true) but receivable
  days rose 109.9 -> 208.4 over FY24-26, far outside "±10 stable" -> top tier
  fails on the stability leg. No literal tier fits a zero-decline-year company
  with blown-out receivables; scored conservatively -> **1** (judgment call,
  stated; not a literal match to any listed tier)
- **M5 Scale & Dominance**: segment mcap/margin ranking not in provided data ->
  **0**, PEER DATA NEEDED
- **M6 Technology/R&D**: no R&D spend line in screener-Data_Sheet.csv or AR
  extract located -> **0**, NOT FOUND
- **M7 Regulatory/License**: pharma export manufacturing is regulated (WHO-GMP,
  drug licences) but with far more than 10 listed players in the segment ->
  band "regulated but >10 players" -> **1**
- **M8 Distribution**: export reach via distributors mentioned in decks/AR but
  not quantified with outlet/distributor counts and growth trend in the data
  provided -> "mentioned unquantified" -> **1**
- **M9 Brand**: Gross margin proxy (Revenue - Raw Material Cost)/Revenue: TLL
  FY26 = 46.4% vs peer median 57.5% (CAPLIPOINT 57.5%, SENORES 60.2%, INNOVACAP
  48.6%) -> TLL below peer median -> **0**
- **M10 Switching Costs**: revenue grew every year (top condition met) but
  receivable days rose ~98 days over the FY24-26 window, far above the ≤10-day
  cap -> fails; no tier matches a zero-decline-year, blown-out-receivables
  profile -> scored **0** (deteriorating collections read as the opposite of a
  switching-cost moat, judgment call stated)
- **M11 Network Effects**: only 5 years of history, below the 6-year two-window
  test minimum -> scored on overall trend per the rule's fallback: revenue CAGR
  56% ≥20% but Selling & Admin cost as % of sales rose from 3.9% (FY22) to 6.3%
  (FY25) (screener-Data_Sheet.csv; FY26 Selling and admin cell is blank in the
  source, so FY26 % not computable) -> "growth ≥20% but selling% rising" -> **1**
- **M12 Negative WC/Float**: WC days FY24-26 = 151.1 / 172.7 / 202.8, none
  negative and all far above the 45-day ceiling -> **0**

| Test | Score |
|---|---|
| M1 Pricing Power | 5 |
| M2 Cost Advantage | 0 |
| M3 Capital Efficiency | 1 |
| M4 Customer Stickiness | 1 |
| M5 Scale & Dominance | 0 (PEER DATA NEEDED) |
| M6 Technology/R&D | 0 (NOT FOUND) |
| M7 Regulatory/License | 1 |
| M8 Distribution | 1 |
| M9 Brand | 0 |
| M10 Switching Costs | 0 |
| M11 Network Effects | 1 |
| M12 Negative WC/Float | 0 |
| **MOAT TOTAL** | **10 / 60** |

Moats "present" (score ≥3): only **M1 Pricing Power** clears the bar (score 5).
Every other test scores 0 or 1, below the present threshold.

**Moats confirmed = 1. Moat classification: 1 present -> THIN**

```
Moat profile:
M1  [#####] 5  present
M2  [     ] 0
M3  [#    ] 1
M4  [#    ] 1
M5  [     ] 0  PEER DATA NEEDED
M6  [     ] 0  NOT FOUND
M7  [#    ] 1
M8  [#    ] 1
M9  [     ] 0
M10 [     ] 0
M11 [#    ] 1
M12 [     ] 0
```

---

## CLASSIFICATION

Grand Total = Core 48 + Moat 10 = **58 / 160**

Data confidence: 5 years of P&L history (FY22-FY26) -> band "5-6 lower, flag
'may not have seen full cycle'". Sub-metrics needing the balance-sheet current-
liability split (ROCE, WC Days) run on a 3-year sub-window (FY24-26) only, a
separate limitation stated per-row above, not the trigger for the "3-4 LIMITED"
history-downgrade rule (which is about overall corpus history, not one metric's
availability). **history_downgrade: false** on that basis, but the 5-6 year
flag applies to the whole scorecard: **FLAG — may not have seen a full cycle.**

Classification matrix: Core 48 falls in the 40-59 band -> **AVERAGE**
(independent of moat tier, since bands below Core 60 do not branch on moat class).

Deal-breaker check:
1. Block A <8: A=12, not triggered
2. **Block B <8: B=0, TRIGGERED -> max GOOD**
3. Median ROCE <10%: 10.87% (op. basis), not triggered (borderline — 0.87pp above the line)
4. **Cumulative CFO/PAT <0.50: -0.478, TRIGGERED -> max AVERAGE**
5. Pledge >15%: NOT FOUND, not triggered (no evidence to trigger on)
6. ND/EBITDA >3x AND IC <3x: ND/EBITDA=2.45x, not triggered
7. Revenue declined majority of years: never declined, not triggered
8. PAT negative any of last 3 years: FY24/25/26 all positive, not triggered
9. History <3 years: 5 years of P&L held, not triggered

Binding cap: deal-breaker #4 (max AVERAGE) is the stricter of the two triggered
caps and matches the score-band outcome. **No conflict.**

## CLASSIFICATION: AVERAGE

Strongest block: **C — Growth (16/20)**, driven by a 56% revenue CAGR and a
48% PAT CAGR with zero revenue-decline years across five audited years.

Weakest block: **B — Cash Generation (0/20)** — every one of the four rows
scored zero. Cumulative operating cash flow is negative across FY22-26 despite
positive cumulative profit, working capital days widened by 52 in two years,
and the FCF proxy is negative in every year (though that proxy is inflated by
acquisition-related investing outflows, see data_notes).

## DECISION LINE

AVERAGE, with the classification held there by two independent deal-breakers
(Block B cash generation, cumulative CFO/PAT). The growth is real and fast
by every P&L measure available; the cash behind it has not shown up yet, and
receivable days more than doubled in the year the growth accelerated most.
Nothing here halts the pipeline — no mechanical failure occurred — but this
run carries that finding into every later stage as the load-bearing question
LBF1 already named.
