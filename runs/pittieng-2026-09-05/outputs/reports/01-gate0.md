# GATE 0 SCORECARD — Pitti Engineering Ltd (PITTIENG)
Run: runs/pittieng-2026-09-05 | BSE 513519 / NSE PITTIENG | CMP Rs 1,085 | Mkt cap Rs 4,085 Cr | Run date 2026-09-05

Data available: P&L 7 years (FY20 to FY26, screener-data). Balance Sheet and Cash
Flow 6 years (FY21 to FY26, screener-data; FY20 opening balance sheet not
provided, so FY21 return ratios use closing net worth only, stated below).
Trade payables (needed for Working Capital Days) are available for only 2
years, FY25 and FY26, from the AR consolidated notes (AR FY26, PDF p.96),
because no earlier annual report is in this corpus. Scoring is adapted to
these three overlapping windows: growth metrics (Block C) use the full
7-year P&L window; return and balance-sheet metrics (Blocks A, D) use the
6-year window; the WC-days metric (B4) uses the 2-year window only, stated
as a proxy basis. Corpus verdict per orchestrator: CORPUS GAPPED (no results
filings, no rating, no shareholding-pattern filing, no research; see
input_gaps).

Source convention: screener.in consolidated export = (screener-data, row,
FY). Annual Report FY2025-26 = (AR FY26, PDF p.N). Screener consolidated
P&L/BS/CF figures were cross-checked line-by-line against the AR's own
consolidated financial statements (PDF p.96-98) and matched exactly or to
within rounding; the AR's page 16-17 "Financial Performance" infographic
was used only where its figures independently matched a primary-statement
number or the AR's own Note 25.21 Key Ratios (standalone) — its raw
chart-title-to-data pairing is not reliably sequential in the extracted
text and was NOT used as a primary source for any scored figure without
that cross-check.

---

## OPENING NOTE ON COMPANY MEMORY LOAD-BEARING FACTS
(memory to weigh, never anchored evidence; checked against this run's own
inputs per instruction)

1. FY28 turnover >Rs 2,500 Cr / FY27 EBITDA ~Rs 370 Cr guidance: NOT FOUND
   in this run's corpus (no guidance table in AR or Q1 FY27 presentation
   sidecar; likely lives in a concall transcript not provided here).
   Carries forward as an open verification item.
2. FY26 adjusted EBITDA up ~20% yet PAT fell: CONFIRMED. Adjusted EBITDA
   Rs 325.8 Cr (FY26) vs Rs 271.7 Cr (FY25), +19.9% (Investor_Presentation_1,
   sidecar p.25, "Historical Profit & Loss Statement"). Reported PAT fell
   Rs 122.3 Cr (FY25) to Rs 117.8 Cr (FY26), -3.7% (screener-data, Net
   profit, FY25/FY26). Gap traced below (Block A/analyst note).
3. Railway/traction ~40% of revenue via Wabtec and Alstom: PARTIALLY
   CONFIRMED, PARTIALLY CORRECTED. AR states Railways is the largest
   END-MARKET at 33% of FY26 revenue (AR FY26, PDF p.5), not "traction"
   specifically and not 40%. Separately, Note 25.6(c) (AR FY26, PDF p.115,
   consolidated) discloses 2 unnamed customers each above 10% of revenue,
   aggregating Rs 481.74 Cr = 25.19% of FY26 revenue from operations, DOWN
   from Rs 687.93 Cr = 40.36% in FY25 — the ~40% figure matches FY25, not
   FY26, and customer names are not disclosed. "Alstom" does not appear
   anywhere in this Annual Report; "Wabtec Corporation" appears once, as a
   past supplier-award citation (2019, 2022; AR FY26, PDF p.53), not as a
   quantified revenue-concentration disclosure.
4. Rs 290 Cr machined-components capex, castings to 36,000 MT "by Q1 FY29":
   AR states commissioning "by Q1 2029-30" (AR FY26, PDF p.14), i.e. Q1 of
   Indian FY 2029-30 = Q1 FY30, one year later than memory's "Q1 FY29".
   Flag for operator correction.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

ROCE (consolidated, EBIT/Average Capital Employed): FY22-FY26 anchored to
AR FY26 "Financial Performance" infographic (AR FY26, PDF p.16), which is
identical to the AR's own Note 25.21 Key Ratios standalone figures for
FY26/FY25 (14.72%/16.24%, AR FY26, PDF p.89) after allowing for the
standalone/consolidated split, and independently cross-validated (see ROE
below). FY21 is NOT in that AR summary (which starts FY22); computed here
via proxy: Capital Employed = Net Worth + Total Borrowings (screener-data,
since the FY21 current/non-current liability split is not in this corpus).

| FY | ROCE % | Source |
|---|---|---|
| FY21 | 12.32 | computed: EBIT(PBT+Interest)=68.15 / CE(Equity+Borrowings)=553.37 (screener-data) |
| FY22 | 17.28 | AR FY26, PDF p.16 (consolidated) |
| FY23 | 17.19 | AR FY26, PDF p.16 (consolidated) |
| FY24 | 18.39 | AR FY26, PDF p.16 (consolidated) |
| FY25 | 16.07 | AR FY26, PDF p.16 (consolidated) |
| FY26 | 13.75 | AR FY26, PDF p.16 (consolidated); Note 25.21 standalone shows 14.72% (AR FY26, PDF p.89) |

A1 Median ROCE (6 yrs, sorted 12.32/13.75/16.07/17.19/17.28/18.39) = 16.63% → **3** (15-19.9 band)
A2 Minimum single-year ROCE = 12.32% (FY21, proxy-computed) → **3** (12-14.9 band)
A3 Median ROE (below) = 18.44% → **4** (15-19.9 band)
A4 ROCE trend, latest (FY26 13.75%) vs earliest (FY21 12.32%): latest ≥ earliest → **5**
  (Note: ROCE actually PEAKED at FY24 18.39% and has declined 3 straight
  years to FY26 13.75%, a real deceleration the endpoint-only formula does
  not show; see analyst_note.)

ROE (consolidated, PAT/Average Net Worth): FY22-FY26 anchored to AR FY26
PDF p.16 (independently reproduced by this run's own computation from
screener-data PAT and Net Worth to the basis point, confirming both the
AR figure and the computation method). FY21 uses CLOSING net worth only
(FY20 opening not in corpus), per formula instruction.

| FY | ROE % | Source |
|---|---|---|
| FY21 | 12.20 | computed: PAT 28.76 / closing Net Worth 235.79 (screener-data; closing-only, FY20 opening N/A) |
| FY22 | 19.96 | AR FY26, PDF p.16; matches computed PAT/avg-NetWorth |
| FY23 | 19.04 | AR FY26, PDF p.16; matches computed |
| FY24 | 22.23 | AR FY26, PDF p.16; matches computed |
| FY25 | 17.83 | AR FY26, PDF p.16; matches computed |
| FY26 | 12.50 | AR FY26, PDF p.16; matches computed |

**Block A total = 3+3+4+5 = 15/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

B1 Cumulative CFO ÷ Cumulative PAT, FY21-FY26 (6 yrs, screener-data CFO row
and Net profit row): CFO sum = 31.71+87.91+222.16+80.02+288.54+204.91 =
915.25 Cr. PAT sum = 28.76+51.87+58.83+89.70+122.29+117.81 = 469.26 Cr.
Ratio = 1.95 → **5** (≥1.00 band)

B2/B3 need capex. Capex is disclosed directly in the AR cash flow statement
only for FY25 (Rs 310.00 Cr, "Purchase of Property, Plant & equipment and
intangibles", AR FY26 PDF p.97) and FY26 (Rs 173.09 Cr, AR FY26 PDF p.96-97
carry-forward, same line). For FY22-FY24 (organic, pre-subsidiary-
acquisition years) capex is proxied: Capex = Δ(Net Block+CWIP) + Depreciation
for the year (screener-data). This proxy is NOT used for FY25 because FY25
Net Block jumped from Rs 586.76 Cr to Rs 1,090.05 Cr on the 2024 acquisition
of Tumakuru/Hoskote/Macharam as wholly-owned subsidiaries (AR FY26, PDF
p.14, "Acquired (in 2024 as a WoS)"), which the prompt's capex formula
explicitly excludes ("exclude acquisitions") — the AR's actual cash capex
line is used instead for FY25/FY26.

| FY | CFO | Capex | Basis | FCF |
|---|---|---|---|---|
| FY22 | 87.91 | 80.03 | proxy: Δ(327.32-286.17)+38.88 dep | 7.88 |
| FY23 | 222.16 | 105.66 | proxy: Δ(388.33-327.32)+44.65 dep | 116.50 |
| FY24 | 80.02 | 257.16 | proxy: Δ(586.76-388.33)+58.73 dep | -177.14 |
| FY25 | 288.54 | 310.00 | AR FY26 PDF p.97, actual | -21.46 |
| FY26 | 204.91 | 173.09 | AR FY26 PDF p.96-97, actual | 31.82 |

B2 FCF-positive years: FY22(+), FY23(+), FY26(+) = 3 of 5 = 60% → **2** (50-74 band)
B3 Cumulative FCF ÷ Cumulative PAT (FY22-26): FCF sum = -42.40 Cr; PAT sum
(FY22-26) = 51.87+58.83+89.70+122.29+117.81 = 440.50 Cr. Ratio = -0.096 →
**0** (negative band)

B4 Change in WC Days, latest vs earliest AVAILABLE (only 2 years have Trade
Payables in this corpus: FY25 and FY26; Receivables/Inventory basis =
Revenue, since COGS is not explicitly broken out consistently — Revenue
basis stated per formula rule):
- Trade Payables FY25 = Rs 327.52 Cr (598.01+32,153.83 lakh, AR FY26 PDF
  p.96, comparative column); FY26 = Rs 243.27 Cr (717.79+23,609.24 lakh,
  AR FY26 PDF p.96).
- FY25: Receivable Days 254.55/1704.57×365=54.51; Inventory Days
  329.11/1704.57×365=70.47; Payable Days 327.52/1704.57×365=70.13.
  WC Days = 54.85.
- FY26: Receivable Days 206.25/1912.81×365=39.36; Inventory Days
  394.91/1912.81×365=75.37; Payable Days 243.27/1912.81×365=46.42.
  WC Days = 68.31.
- Change = +13.46 days (increase) → **1** (increased 5-15 band)

**Block B total = 5+2+0+1 = 8/20** (at the deal-breaker-2 threshold of <8;
does not trigger since 8 is not less than 8)

---

## BLOCK C: GROWTH (Max 20)

Using the full 7-year P&L window (screener-data, Sales and Net profit
rows, FY20-FY26).

C1 Revenue CAGR: (1,912.81/525.06)^(1/6)-1 = 24.06% → **5** (≥20 band)
C2 PAT CAGR: (117.81/17.10)^(1/6)-1 = 37.95%. Both endpoints positive, no
loss-to-profit swing → **5** (≥20 band)
C3 Positive YoY revenue years: FY21 declined -1.31% vs FY20 (518.17 vs
525.06); FY22 through FY26 all grew. 5 of 6 YoY comparisons positive =
83.3% → **3** (75-99 band)
C4 PAT CAGR minus Revenue CAGR = 37.95% - 24.06% = +13.89pp → **5** (≥+3pp band)

**Block C total = 5+5+3+5 = 18/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

Latest year = FY26, consolidated (AR FY26, PDF p.96, cross-checked to
screener-data BS row). Debt is presented on TWO bases because they land in
different scoring bands for D1: EXCLUDING lease liabilities (matching the
AR's own Note 25.21 footnote, "Debt excludes lease liabilities", AR FY26
PDF p.89) is used as PRIMARY; INCLUDING lease liabilities (screener-data's
single "Borrowings" row, which nets to the AR's borrowings+lease total
exactly) is shown as a cross-check.

- Debt excl. lease (primary) = Non-current borrowings 380.81 + Current
  borrowings 318.03 = Rs 698.84 Cr (AR FY26, PDF p.96, Notes 10A/13A)
- Debt incl. lease (cross-check) = Rs 810.58 Cr (screener-data, Borrowings,
  FY26; reconciles to AR: 380.81+77.22 lease NC+318.03+34.52 lease-C = 810.58)
- Cash & Bank = Rs 146.72 Cr (screener-data; = AR Cash equiv. 119.45 +
  other bank balances 27.27)
- EBITDA FY26 (excl. other income) = Rs 315.75 Cr, computed as PBT+Dep+
  Interest-OtherIncome = 167.58+104.66+83.41-39.90 (screener-data); AR/
  presentation "Reported EBITDA" = Rs 315.5 Cr (Investor_Presentation_1,
  sidecar p.25) — near-exact cross-check.
- Equity FY26 = Rs 986.90 Cr (18.83+968.07, screener-data)

D1 Net Debt/EBITDA: excl-lease (primary) = (698.84-146.72)/315.75 = 1.75x
→ **3** (1-2x band). Incl-lease cross-check = (810.58-146.72)/315.75 =
2.10x → would score **1** (2-3x band). PRIMARY SCORE USED: 3. This choice
moves Block D by 2 points (10 vs 8) but does not change the final
classification either way (see below).
D2 Interest Coverage EBIT/Interest: EBIT = PBT+Interest = 167.58+83.41 =
250.99 (matches presentation's EBIT 251.0, sidecar p.25). Interest = 83.41
(screener-data). IC = 3.01x → **2** (3-4.9 band)
D3 Debt/Equity: excl-lease 698.84/986.90 = 0.708x; incl-lease 810.58/986.90
= 0.821x — BOTH fall in the same band → **3** (0.5-1.0 band, either basis)
D4 Current Ratio: Total Current Assets 90,531.52 / Total Current
Liabilities 64,542.36 (AR FY26, PDF p.96, lakh) = 1.403x → **2** (1.2-1.49
band). Standalone Note 25.21 shows 1.33x (AR FY26, PDF p.89) — same band.

**Block D total (primary) = 3+2+3+2 = 10/20** (alternate, incl-lease D1: 8/20)

Deal-breaker 6 check (ND/EBITDA>3x AND IC<3x → AVOID): neither threshold
breached on either debt basis. Not triggered.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

E1 Promoter holding (latest, 31-Mar-2026) = 54.18% (Promoters & Promoter
group, 2,03,99,999 shares of 3,76,53,588; AR FY26, PDF p.56, Corporate
Governance shareholding distribution) → **4** (50-59.9 band)

E2 Promoter holding change over 3 years: **N/A (not in provided data)** —
score 0. This AR (FY26) discloses promoter shareholding for FY26 and FY25
only (both 54.18%, 2,03,99,999 shares unchanged; AR FY26, PDF p.107, "(d)
Shares held by Promoters"), a 1-year flat comparison, not the required
3-year window. No earlier annual report or shareholding-pattern filing is
in this corpus (per B00 input gaps) to reach FY23. The 1-year data point
(0% change) is noted here as context, not scored.

E3 Promoter pledge (latest): **N/A (not in provided data)** — score 0. No
pledge/encumbrance disclosure was located anywhere in this Annual Report
(searched "pledge", "encumbrance", Regulation 31 disclosures). The only
"pledge" hit in the document is an unrelated CARO auditor statement that
the Company itself has not raised loans against securities pledged in its
subsidiary (AR FY26, PDF p.63) — not a promoter share-pledge disclosure.
The shareholding-pattern filing that ordinarily carries this is absent
from this run's corpus (per B00 input gaps).

E4 Contingent Liabilities ÷ Net Worth (latest, consolidated): Contingent
liabilities FY26 = Rs 74.99 Cr (claims 9.72+RoDTEP 3.97+EPCG 25.15+advance
licence 3.03+bank guarantees 33.12 = 74.99 Cr; Note 25.2, AR FY26, PDF
p.112, consolidated). Net Worth FY26 = Rs 986.90 Cr. Ratio = 7.60% → **3**
(5-15 band)

**Block E total = 4+0+0+3 = 7/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Peer set available this run: RKFORGE (Ramkrishna Forgings, screener-data)
and SANSERA (Sansera Engineering, screener-data). VILAS (Vilas Transcore)
has no CSV in this run — every peer-dependent test below is scored on a
MEDIAN OF 2, and VILAS's absence is flagged as PEER DATA NEEDED where it
would materially change the read (M5).

FY26 EBITDA margins (own formula, PBT+Dep+Interest-OtherIncome, applied
identically to all three companies from their own screener-data):
PITTIENG 315.75/1912.81 = 16.51%; RKFORGE (84.01+332.89+212.5-2.4)/4238.08
= 14.79%; SANSERA (432.12+205.86+37.74-43.62)/3497.92 = 18.07%. Peer
median (of 2) = 16.43%.

Gross-margin proxy, M9 ((Revenue-Material Cost)/Revenue, screener-data,
stated as proxy per instruction): PITTIENG (1912.81-1203.24)/1912.81 =
37.10%; RKFORGE (4238.08-2055.55)/4238.08 = 51.50%; SANSERA
(3497.92-1503.62)/3497.92 = 57.02%. Peer median = 54.26%.

| # | Test | Score | Basis |
|---|---|---|---|
| M1 | Pricing Power | **3** | EBITDA margin FY20 14.80% → FY26 16.51%, +1.71pp (within ±2pp, just under the +2pp expansion threshold); Revenue CAGR 24.06% ≥10% → "stable ±2pp AND rev CAGR≥10%" band |
| M2 | Cost Advantage vs peers | **1** | 16.51% vs peer median 16.43%, +0.08pp → within ±2pp band |
| M3 | Capital Efficiency | **1** | FAT = Revenue/Net Block = 1912.81/1152.84 = 1.66x (>1x); ROCE FY26 13.75% (>12%, not >15%) → lowest present band |
| M4 | Customer Stickiness | **3** | 1 revenue-decline year (FY21), fully recovered FY22 (+84%); receivable days moved -82 days over the period (not "stable", so the top band fails on stability, not decline count) |
| M5 | Scale & Dominance | **0 — PEER DATA NEEDED** | Only 2 of 3 named peers have data in this run and no segment-wide (electrical steel lamination) market-cap/margin ranking is available; PITTIENG mcap Rs 4,085 Cr is smallest of the 2 available comparators (RKFORGE Rs 12,767 Cr, SANSERA Rs 23,605 Cr, screener-data) but this is not the relevant segment |
| M6 | Technology/R&D | **0** | R&D/Revenue disclosed as "Nil" both FY26 and FY25 (BRSR Principle 2, AR FY26, PDF p.42) |
| M7 | Regulatory/License | **0** | Unregulated manufacturing segment (electrical steel laminations/castings/machining); no licence-cap disclosed |
| M8 | Distribution | **0** | BRSR discloses "Sales to dealers/distributors as % of total sales: Nil" (AR FY26, PDF p.41) — direct B2B OEM model, no distribution network to score |
| M9 | Brand | **0** | GM proxy 37.10% is BELOW peer median 54.26% by -17.16pp → "at/below" band despite Revenue CAGR 24.06% |
| M10 | Switching Costs | **0** | Revenue grew all but 1 year (5/6), but receivable days fell ~82 days (not "stable" as the tier requires) and only 1 decline year (not the 2+ required for the score-1 band) — falls between tiers, scored 0 by elimination |
| M11 | Network Effects | **3** | Latest 3yr CAGR (FY23→FY26) 20.26% vs prior 3yr CAGR (FY20→FY23) 27.97% — DECELERATING, fails the top band; Revenue CAGR (latest 3yr) 20.26% ≥20% AND Selling+admin/Revenue roughly stable-to-declining (FY23 5.18% → FY26 5.11%) → score-3 band |
| M12 | Negative WC/Float | **0** | WC Days 54.85 (FY25) and 68.31 (FY26), both >45 days → lowest band |

Moats present (score ≥3): M1, M4, M11 = **3 of 12**

**Block F total = 3+1+1+3+0+0+0+0+0+0+3+0 = 11/60**

Moat profile:
```
M1  Pricing Power      [###..] 3/5  PRESENT
M2  Cost Advantage     [#....] 1/5
M3  Capital Efficiency [#....] 1/5
M4  Customer Sticky    [###..] 3/5  PRESENT
M5  Scale/Dominance    [.....] 0/5  PEER DATA NEEDED
M6  Tech/R&D           [.....] 0/5
M7  Regulatory         [.....] 0/5
M8  Distribution       [.....] 0/5
M9  Brand              [.....] 0/5
M10 Switching Costs    [.....] 0/5
M11 Network Effects    [###..] 3/5  PRESENT
M12 Negative WC/Float  [.....] 0/5
```

Moat classification: 3 present → **MODERATE** (2-3 band)

---

## SCORE SUMMARY

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 15 | 20 |
| B — Cash Generation Quality | 8 | 20 |
| C — Growth | 18 | 20 |
| D — Balance Sheet Strength (primary) | 10 | 20 |
| E — Shareholder Alignment | 7 | 20 |
| **Core (A+B+C+D+E)** | **58** | **100** |
| F — Moat Score | 11 | 60 |
| **Grand Total** | **69** | **160** |

Strongest block: **C — Growth (18/20)**, driven by a clean multi-year
revenue and PAT compounding record (24.06% / 37.95% CAGR) with only one
soft year (FY21).

Weakest block by raw score: **E — Shareholder Alignment (7/20)**, but 2 of
its 4 sub-metrics (E2, E3) are NOT FOUND rather than confirmed adverse
findings — this is a corpus gap (no shareholding-pattern filing, no prior
AR), not evidence of misalignment. Reading past the gap, the weakest block
with FULL data coverage is **B — Cash Generation Quality (8/20)**, which
IS a genuine finding: cumulative FCF is negative across FY22-FY26 (-Rs
42.40 Cr against Rs 440.50 Cr of cumulative PAT) because two of the five
years (FY24 organic brownfield capex, FY25 subsidiary-consolidation capex)
consumed cash faster than operations generated it, and working capital
days rose 13.46 days into FY26 even as FY26 capex moderated and FY26 FCF
turned positive again (+Rs 31.82 Cr).

---

## DATA CONFIDENCE

The binding balance-sheet-dependent window is 6 years (FY21-FY26), which
falls in the "5-6, lower, flag" band per the framework: **flag — may not
have seen a full cycle.** This is a flag only; it does NOT trigger the
one-tier classification downgrade (that requires a 3-4 year window). The
growth-only window (7 years, FY20-FY26) would sit in the "7-9, moderate"
band on its own, but the binding constraint across most blocks is 6 years.

---

## DEAL-BREAKER CHECK

1. Block A <8 → max GOOD: A=15, not triggered.
2. Block B <8 → max GOOD: B=8, exactly at the threshold, NOT triggered
   (8 is not less than 8) — flagged as a near-miss.
3. Median ROCE <10% → max AVERAGE: 16.63%, not triggered.
4. Cumulative CFO/PAT <0.50 → max AVERAGE: 1.95x, not triggered.
5. Pledge >15% → max AVERAGE: pledge data NOT FOUND; cannot confirm
   breach; cannot confirm clearance either. Flagged as an open item, not
   scored as a breach.
6. ND/EBITDA >3x AND IC <3x → AVOID: ND/EBITDA 1.75x-2.10x (both bases),
   IC 3.01x — neither leg breached on either debt basis. Not triggered.
7. Revenue declined in majority of years → max AVERAGE: 1 of 6 years
   declined, not triggered.
8. PAT negative in any of last 3 years → max AVERAGE: FY24/25/26 all
   positive, not triggered.
9. History <3 years → AVERAGE: 6-7 years available, not triggered.

**No deal-breaker fires.**

---

## CLASSIFICATION

Classification matrix: Core 40-59 → **AVERAGE** (independent of moat
class). Core = 58 falls in this band regardless of the D1 debt-basis
choice (primary 58, alternate incl-lease 56 — both land in 40-59).

**CLASSIFICATION: AVERAGE**

This is driven by Block B (cash conversion strain across the
capex-heavy FY24-25 window) and Block E (data-gap driven, not a confirmed
finding) more than by any single collapsed metric. Growth (C) and returns
(A) are both comfortably above AVERAGE-band thresholds on their own; the
moat profile is genuinely thin (MODERATE, 3/12) and consistent with the
company's own archetype description — a vertically-integrated, B2B
component/casting/machining supplier with no brand, licence, R&D, or
distribution moat, whose edge (where present) is customer-qualification
stickiness (M4) and a currently-decelerating growth compounding pattern
(M11) rather than pricing power or scale.

---

## DECISION LINE

Gate 0 = AVERAGE (Core 58/100, Moat 11/60 MODERATE, Grand Total 69/160).
No deal-breaker fires. This is a mechanical screen only; it does not halt
the run (company-quality flags propagate, per pipeline rule). Flag
FLAG-GATE0 raised for downstream stages given the AVERAGE classification,
naming Block B (cash-conversion strain, capex-driven) and Block E (data
gaps, not adverse findings) as the depressors, for the operator's
attention at Halt 1.

---

## INPUT GAPS CARRIED FORWARD

- Results filings absent; rating rationale absent; exchange announcements
  absent; shareholding pattern filing absent (AR FY26 tables as of
  31-Mar-2026 stand in, only 2 years deep); research absent; screener
  P&L/BS/CF/Quarters CSVs header-only (Data_Sheet populated); AR weblink
  letter misfiled as AR (ignored per instruction).
- Trade Payables available for FY25-FY26 only (AR notes); no multi-year
  Trade Payables series in this corpus, so B4 (WC Days trend) is a 2-year
  read, not the full 6-year window used elsewhere in Block A/D.
- Capex line-item available for FY25-FY26 only (AR cash flow statement);
  FY22-FY24 capex is a Net-Block-delta-plus-depreciation proxy (stated
  above), which would be unreliable in an acquisition year — none of
  FY22-FY24 had one, so the proxy is used with moderate confidence there.
- Promoter holding 3-year trend (E2) and promoter pledge (E3): NOT FOUND
  in this corpus; both require the absent shareholding-pattern filing or
  an earlier annual report.
- FY27/FY28 management guidance (turnover, EBITDA margin, EBITDA Rs
  crore) named in company memory load-bearing fact #1: NOT FOUND in the
  AR or the Q1 FY27 investor presentation sidecars provided this run.
- Segment/customer identity behind the Note 25.6(c) 2-customer
  concentration disclosure (25.19% FY26, 40.36% FY25 of revenue) is not
  named in the AR; cannot confirm this is Wabtec/Alstom specifically.

---

## DATA NOTES

1. Proxy basis, Block A: FY21 ROCE and ROCE Capital Employed use Net
   Worth + Total Borrowings (screener-data) since neither the AR's own
   summary (which starts FY22) nor a current/non-current liability split
   is available for FY21 in this corpus. FY22-FY26 ROCE/ROE are anchored
   to the AR's own Financial Performance summary (AR FY26, PDF p.16),
   independently cross-validated by this run's own PAT/Average-Net-Worth
   computation (exact match) and by the AR's separate Note 25.21 Key
   Ratios, standalone basis (AR FY26, PDF p.89).
2. Proxy basis, Block B: capex for FY22-FY24 is Δ(Net Block+CWIP)+
   Depreciation (screener-data); FY25/FY26 capex is the AR's actual cash
   flow statement line (AR FY26, PDF p.96-97). The proxy would be
   unreliable in an acquisition year (FY25's Net Block jump includes the
   2024 subsidiary acquisitions, not cash capex) — this is precisely why
   FY25/FY26 use the actual AR figure instead of the proxy.
3. Proxy basis, Block B: Working Capital Days use REVENUE as the
   denominator for Receivable/Inventory/Payable Days (COGS not
   consistently broken out across all years in this corpus), stated per
   the formula's own basis rule.
4. PEER DATA NEEDED: M5 (Scale & Dominance) needs a full segment-wide
   market-cap/margin ranking; only 2 of 3 named peers (RKFORGE, SANSERA)
   have screener data in this run, and neither is a true electrical-steel-
   lamination peer (both are auto/forging component makers) — scored 0,
   PEER DATA NEEDED, rather than guessed.
5. M2 and M9 use a median-of-2 peer set (RKFORGE, SANSERA); VILAS (Vilas
   Transcore) has no CSV in this run and is excluded rather than
   estimated.
6. Management's own "Adjusted EBITDA" (adds back ESOP cost, excludes
   other income) is HIGHER than the "Reported EBITDA" used throughout
   this scorecard: FY26 Adjusted Rs 325.8 Cr vs Reported Rs 315.5 Cr,
   FY25 Adjusted Rs 271.7 Cr vs Reported Rs 271.1 Cr (Investor_
   Presentation_1, sidecar p.25). Gate 0 scores REPORTED figures
   throughout, per instruction; Adjusted figures are noted here only.
7. Loss-to-profit swing check: none. PAT was positive in every year FY20-
   FY26 (screener-data); no synthetic CAGR was needed.
8. D1 (Net Debt/EBITDA) is presented on two debt bases (excl. and incl.
   lease liabilities) because they land in different scoring bands (3 vs
   1). The AR's own Note 25.21 explicitly excludes lease liabilities from
   "Debt" for its standalone ratios; that convention is used as PRIMARY
   here. This choice moves Block D from 10 to 8 under the alternate basis
   but does not change the Core-score classification band (40-59 either
   way).


## B01 HANDOFF BLOCK (emitted by the stage in its final response; appended verbatim by the orchestrator)

```yaml
stage: B01-gate0
company: "PITTIENG"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
input_gaps:
  - "results filings absent"
  - "rating rationale absent"
  - "exchange announcements absent"
  - "shareholding pattern filing absent (AR FY26 tables as of 31-Mar-2026 stand in, only 2 years deep)"
  - "research absent"
  - "screener P&L/BS/CF/Quarters CSVs header-only (Data_Sheet populated)"
  - "AR weblink letter misfiled as AR (ignored)"
  - "Trade Payables available FY25-FY26 only; no multi-year series for WC-days trend"
  - "Capex line-item available FY25-FY26 only; FY22-FY24 capex is a Net-Block-delta proxy"
  - "promoter holding 3-year trend (E2) NOT FOUND"
  - "promoter pledge (E3) NOT FOUND"
  - "FY27/FY28 management guidance NOT FOUND in AR or Q1 FY27 presentation sidecars"
  - "customer identity behind Note 25.6(c) 2-customer concentration NOT named"
flags:
  - type: FLAG-GATE0
    reason: "Classification AVERAGE (Core 58/100). Depressors: Block B cash-conversion strain (cumulative FCF FY22-26 negative, -Rs42.40cr vs Rs440.50cr cumulative PAT, driven by FY24 brownfield capex and FY25 subsidiary-consolidation capex) and Block E (7/20, but half data-gap-driven: E2/E3 NOT FOUND, not confirmed adverse findings). Moat MODERATE (3/12: M1 pricing power, M4 customer stickiness, M11 network-effect-adjacent growth), consistent with commodity-adjacent B2B component-maker archetype, no brand/R&D/licence/distribution edge."
data_years: 7
fy_range: "FY20 to FY26"
blocks: {A: 15, B: 8, C: 18, D: 10, E: 7}
core_score: 58
moat_score: 11
grand_total: 69
moats_confirmed: 3
moat_class: "MODERATE"
classification: "AVERAGE"
deal_breakers: []
history_downgrade: false
data_notes:
  - "Block A: FY21 ROCE/ROE proxy-computed (Equity+Total Borrowings; closing-only net worth); FY22-FY26 anchored to AR FY26 PDF p.16, cross-validated exactly against own PAT/avg-equity computation and Note 25.21 standalone (PDF p.89)."
  - "Block B: capex FY22-FY24 proxied as Δ(NetBlock+CWIP)+Depreciation (screener-data); FY25/FY26 capex from AR cash flow statement actuals (PDF p.96-97), since FY25 Net Block jump reflects 2024 subsidiary acquisitions, not cash capex."
  - "Block B: WC Days use Revenue basis (COGS not consistently available); Trade Payables only available FY25-FY26 (AR PDF p.96), so B4 is a 2-year read."
  - "Block D: D1 shown on two debt bases (excl./incl. lease liabilities); primary uses excl.-lease per AR Note 25.21's own convention (1.75x, score 3); incl.-lease cross-check gives 2.10x (score 1). Moves Block D 10 vs 8, does not change classification band."
  - "Block F: M5 scored 0, PEER DATA NEEDED (no full segment-wide mcap/margin ranking; only RKFORGE+SANSERA available, neither a true lamination peer)."
  - "Block F: M2/M9 use median-of-2 peer set (RKFORGE, SANSERA); VILAS has no CSV this run, excluded not estimated."
  - "Management's Adjusted EBITDA (FY26 Rs325.8cr, +19.9% YoY) exceeds Reported EBITDA (Rs315.5cr) used for scoring; source Investor_Presentation_1 sidecar p.25."
  - "No loss-to-profit swing: PAT positive every year FY20-FY26."
  - "Company memory load-bearing fact #3 (~40% railway/traction via Wabtec+Alstom): AR shows Railways=33% of revenue (not traction-specific, not 40%); Note 25.6(c) shows 2 unnamed customers >10% each aggregating 40.36% FY25 / 25.19% FY26; Alstom not mentioned anywhere in AR; Wabtec appears only as a past supplier award (2019/2022)."
  - "Company memory load-bearing fact #4: AR states capex/casting-capacity commissioning 'by Q1 2029-30' (Q1 FY30), one year later than memory's 'Q1 FY29'."
block_b_trend: "deteriorating - WC Days rose from 54.85 (FY25) to 68.31 (FY26), +13.46 days, even as FCF turned positive again in FY26 (+Rs31.82cr) after two negative years (FY24 -Rs177.14cr, FY25 -Rs21.46cr); cumulative FCF/PAT FY22-26 is negative (-0.10x)"
analyst_note: "PAT fell (Rs122.3cr to Rs117.8cr) FY25 to FY26 despite Adjusted EBITDA +19.9%, because Depreciation (+Rs24.2cr), Finance cost (+Rs15.6cr) and Tax (+Rs10.5cr) together outran EBITDA growth (+Rs44-54cr): a scale-up cost story (new capacity depreciating, more debt funding it), not a margin problem. A4 scores 5 on endpoint comparison (FY26 ROCE 13.75% above FY21's 12.32%) but this masks 3 straight years of ROCE decline from an FY24 peak of 18.39%, coincident with FY25 subsidiary acquisitions and brownfield capex. The moat profile (3/12) fits a plain B2B component-maker: no brand, R&D, licence or distribution edge; present tests are customer-qualification stickiness (M4) and scale-compounding (M11), both diluted by a decelerating 3yr revenue CAGR (28% prior window to 20% latest). Customer concentration (2 unnamed customers, 25-40% of revenue depending on year) is a real, unnamed tripwire; verify identity and durability before treating railway/traction exposure as diversified."
```
