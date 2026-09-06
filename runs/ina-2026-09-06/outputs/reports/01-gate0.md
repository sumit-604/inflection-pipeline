# STAGE 1: GATE 0 SCORECARD — Insolation Energy Ltd (INA / 543620)
Run date: 2026-09-06 | Model: claude-sonnet-5 | Mode: pipeline

Data available: 5 years (FY2022 to FY2026), P&L and headline balance sheet /
cash flow from screener-Data_Sheet.csv. Scoring adapted to 5-year history.
Balance-sheet-split ratios (ROCE, Working Capital Days, contingent
liabilities, share count) are corroborated against the FY2026 Annual Report,
which itself carries only THREE balance sheet dates (31-Mar-2026,
31-Mar-2025, and a RESTATED 1-Apr-2024 opening balance sheet — see Basis
Note below). No FY2022/FY2023 Annual Report is in the corpus, so BS-split
metrics (ROCE denominator, Trade Payables, Working Capital Days) are
computed for FY2024–FY2026 only (3 years); P&L-only metrics (Revenue, PAT,
CFO, margins) use the full 5-year screener series.

## CORPUS CONSTRAINTS (carried from Stage 0 / B00)
- No results PDFs (inputs/results/ empty); Gate 0 runs off screening data
  and the FY2026 AR financial statements only.
- screener-Profit_Loss.csv, -Balance_Sheet.csv, -Cash_Flow.csv,
  -Quarters.csv are empty shells (collector defect); NOT read as findings.
  screener-Data_Sheet.csv is the populated primary source.
- No shareholding-pattern filing; promoter holding/pledge sourced from AR
  Note 15 (Equity Share Capital) only — pledge specifically is NOT
  disclosed anywhere in the AR financial statements (that disclosure lives
  in the SEBI shareholding-pattern filing, which is absent this run).
- FY2026 share count taken from AR Note 15 (22,03,94,625 shares, Re 1 FV),
  not from the blank screener cell.

## BASIS NOTE — screener vs AR, and a restatement flag (read before the numbers)
1. screener-Data_Sheet.csv is CONSOLIDATED, not standalone, for FY2025 and
   FY2026 — verified: Total Assets FY2026 screener Rs 2,155.13 cr = AR
   consolidated Total Equity & Liabilities Rs 2,15,512.71 lakh exactly (AR
   p.116). The company's standalone Total Assets FY2026 is only Rs 544.04
   cr (AR p.160) — nearly all revenue and assets sit in the wholly-owned
   subsidiary Insolation Green Energy Pvt Ltd (FY2026 total income Rs
   2,164.50 cr, net profit Rs 191.17 cr, AR p.2/Board's Report).
2. The FY2026 AR's comparative balance sheet carries a RESTATED "1 April
   2024" column (not just 31-Mar-2025), which Ind AS only requires when
   there has been a retrospective restatement (typically a common-control
   business combination). Insolation incorporated/added six new
   subsidiaries (Insolation Green Infra, five "MGVI Green Infra" entities)
   between Jul-2024 and Aug-2025 (AR p.2, Details of Subsidiaries). The
   restated FY2024 Total Assets (Rs 274.69 cr, AR p.116) does not match
   screener's own FY2024 figure (Rs 262.78 cr, screener-data), and restated
   FY2025 CWIP (Rs 52.88 cr, AR p.116) does not match screener's FY2025
   CWIP (Rs 46.10 cr, screener-data). Both are consistent with screener
   holding the AS-ORIGINALLY-REPORTED FY2022–FY2025 series while the AR's
   comparatives are retrospectively restated for the newly-consolidated
   step-down subsidiaries.
   PIPELINE IMPLICATION: Block C's revenue/PAT CAGR (computed on the
   un-restated screener series) is not on a fully consistent group-
   composition basis across FY2024–FY2026; part of the growth may be
   consolidation-scope expansion, not organic growth. Flagged, not
   adjusted (no instruction to re-derive a restated series without an
   AR for FY2022–FY2024).
3. A cash reconciliation gap: screener's own FY2026 cash-flow lines
   (CFO -73.13 + CFI -185.57 + CFF +697.80 = Net Change +439.10, screener-
   data, arithmetic checks) imply closing cash of Rs 313.93 cr (FY25
   closing) + 439.10 = Rs 753.03 cr, but screener's own FY2026 "Cash &
   Bank" balance-sheet line shows Rs 520.94 cr. This Rs 232 cr gap is
   internal to the screener file, not a screener-vs-AR mismatch, and could
   not be resolved from the extracted AR cash flow statement (line-item
   labels and values became separated during PDF-to-text extraction; see
   Note below). It affects D1 (Net Debt/EBITDA): using Rs 520.94 cr cash,
   ND/EBITDA = 1.28x (score 3); using the CF-implied Rs 753.03 cr, it would
   be 0.47x (score 4). Reported using the screener balance-sheet figure,
   flagged as scoring-sensitive.
4. AR extraction quality: the AR's cash-flow-statement tables (both
   consolidated and standalone, pages 117 and 160-161) extracted with
   labels and their numeric columns separated into non-adjacent blocks of
   text. Figures that could be identified with high confidence by matching
   a unique value against the screener series (PBT, Revenue, Other Income,
   Depreciation, Interest, CFO, Total Assets, Net Block, Borrowings,
   Receivables, Inventory — all FY2026) are anchored below with page and
   line evidence. Granular cash-flow sub-line items (individual working
   capital movements) could not be reliably isolated and are not relied on;
   the Fixed Asset movement schedule (Note 4, a cleaner table) is used
   instead as the capex anchor for FCF.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score 14

ROCE = EBIT ÷ (Total Assets − Current Liabilities), computed (screener does
not carry a ROCE row in this data set). EBIT = PBT + Interest − Other
Income (screener P&L structure has Other Income and Interest as separate
post-EBIT lines).

| Year | PBT | Interest | Other Inc | EBIT | Total Assets | Curr. Liab. | Capital Employed | ROCE |
|---|---|---|---|---|---|---|---|---|
| FY2024 | 67.53 (screener-data) | 10.49 (screener-data) | 4.15 (screener-data) | 73.87 (computed) | 274.69 (AR p.116, "1-Apr-2024" col) | 135.08 (AR p.116) | 139.61 (computed) | 52.91% |
| FY2025 | 153.62 (screener-data) | 7.57 (screener-data) | 9.05 (screener-data) | 152.14 (computed) | 851.00 (AR p.116, "31-Mar-2025" col) | 209.63 (AR p.116) | 641.37 (computed) | 23.72% |
| FY2026 | 245.28 (screener-data; = AR p.117 Rs 24,528.53 lakh) | 23.54 (screener-data; = AR p.117 Rs 2,354.09 lakh) | 17.50 (screener-data; = AR p.117 Rs 1,750.25 lakh) | 251.32 (computed) | 2,155.13 (screener-data; = AR p.116 exactly) | 758.29 (AR p.116) | 1,396.84 (computed) | 17.99% |

FY2022/FY2023 ROCE: N/A (not in provided data) — no Current Liabilities
split exists for these years in either screener-Data_Sheet.csv (only a
combined "Other Liabilities" line) or the corpus (no FY2022/2023 AR).

- **A1 Median ROCE** (3 yrs: 52.91/23.72/17.99): median 23.72% → band
  20-24.9% = **4**
- **A2 Minimum single-year ROCE**: 17.99% (FY2026) → ≥15% = **5**
- **A4 ROCE trend, latest vs earliest** (FY2026 17.99% vs FY2024 52.91%):
  decline of 34.9pp → >5pp decline = **0**

ROE = PAT ÷ average Net Worth (opening+closing ÷ 2); FY2022 uses closing
only (no FY2021 opening net worth in corpus), stated per formula rule.
Net Worth = Equity Share Capital + Reserves (screener-data for FY2022/23;
AR p.116 ex-NCI for FY2024-26, which is within 1.3% of screener's own
FY2025/26 figures).

| Year | PAT | Avg Net Worth | ROE |
|---|---|---|---|
| FY2022 | 6.95 | 22.14 (closing only) | 31.40% |
| FY2023 | 10.68 | 37.51 | 28.47% |
| FY2024 | 55.47 | 80.51 | 68.90% |
| FY2025 | 126.20 | 358.25 | 35.23% |
| FY2026 | 200.22 | 707.75 | 28.29% |

- **A3 Median ROE** (5 yrs, sorted 28.29/28.47/31.40/35.23/68.90): median
  31.40% → ≥20% = **5**

**Block A total: 4 + 5 + 5 + 0 = 14/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score 2

**B1 Cumulative CFO ÷ Cumulative PAT** (5 yrs, screener-data):
CFO: 8.79 + (-1.40) + 30.27 + 113.10 + (-73.13) = 77.63
PAT: 6.95 + 10.68 + 55.47 + 126.20 + 200.22 = 399.52
Ratio = 0.194 → <0.50 = **0**

FY2026 CFO of -Rs 73.13 cr against PAT of +Rs 200.22 cr is confirmed
against the AR: AR consolidated cash flow statement shows Net Cash From
Operating Activities of Rs (7,312.82) lakh = -Rs 73.13 cr (AR p.117),
against PBT of Rs 24,528.53 lakh = Rs 245.28 cr on the same statement —
matches screener exactly. Receivables (Rs 110.09 cr → Rs 281.59 cr) and
Inventory (Rs 76.98 cr → Rs 379.05 cr) both verified against AR Note 13/
consolidated balance sheet (AR p.116): FY2026 Trade Receivables Rs 28,158.52
lakh = Rs 281.59 cr; FY2026 Inventories Rs 37,905.21 lakh = Rs 379.05 cr —
both match screener exactly.

**FCF = CFO − Capex.** Capex could not be reliably isolated from the
garbled AR cash-flow investing section; used the Fixed Asset Note 4 gross
block "Additions" (tangible assets) as the capex anchor, plus the year's
net increase in Capital Work-in-Progress (capex spend not yet capitalised).
For FY2023/FY2024 (no Note 4 comparative that far back), capex is proxied
as Δ Net Block + Depreciation + Δ CWIP. FY2022 capex: N/A (no FY2021
opening Net Block in corpus).

| Year | CFO | Capex (proxy) | FCF |
|---|---|---|---|
| FY2023 | -1.40 | 31.17 (ΔNetBlock 28.82 + Dep 2.35, screener-data) | -32.57 |
| FY2024 | 30.27 | 16.85 (ΔNetBlock 8.36 + Dep 7.09 + ΔCWIP 1.40) | 13.42 |
| FY2025 | 113.10 | 91.98 (Note 4 additions 40.50, AR p.119 + ΔCWIP 51.48) | 21.12 |
| FY2026 | -73.13 | 450.68 (Note 4 additions 430.63, AR p.119, Rs 43,063.31 lakh + ΔCWIP 20.05) | -523.81 |

**B2 FCF-positive years as proportion** (4 yrs with data: FY2023-26; 2 of 4
positive = 50%) → band 50-74% = **2**

**B3 Cumulative FCF ÷ Cumulative PAT** (same 4-yr window):
Cumulative FCF = -32.57+13.42+21.12-523.81 = -521.84
Cumulative PAT (FY23-26) = 10.68+55.47+126.20+200.22 = 392.57
Ratio = -1.33 → negative = **0**

**B4 Change in WC Days, latest vs earliest** (3 yrs with a Trade Payables
split available, FY2024-2026; Payables sourced only from AR — screener
does not carry a payables line — AR p.116):

| Year | Receivables | Inventory | Payables | RecDays | InvDays | PayDays | WC Days |
|---|---|---|---|---|---|---|---|
| FY2024 | 51.96 | 73.79 | 37.42 (AR: micro 12.13+non-micro 25.29 lakh, Rs cr) | 25.72 | 36.53 | 18.53 | 43.72 |
| FY2025 | 110.09 | 76.98 | 72.04 (AR: micro 12.78+non-micro 59.26 lakh, Rs cr) | 30.12 | 21.07 | 19.71 | 31.48 |
| FY2026 | 281.59 | 379.05 | 292.73 (AR: micro 44.96+non-micro 247.77 lakh, Rs cr) | 47.90 | 64.47 | 49.79 | 62.58 |

(Basis: Sales, per formula default — COGS not separately available.)

Change, FY2026 vs FY2024: +18.86 days → increased >15 days = **0**

**Block B total: 0 + 2 + 0 + 0 = 2/20**

**Block B trend: DETERIORATING.** CFO swung from +Rs 113.10 cr (FY2025) to
-Rs 73.13 cr (FY2026) while PAT rose from Rs 126.20 cr to Rs 200.22 cr —
the P&L and the cash statement are moving in opposite directions. WC days
rose from 31.48 to 62.58 over the same year, driven by both inventory
build (Rs 76.98 cr → Rs 379.05 cr) and receivables build (Rs 110.09 cr →
Rs 281.59 cr) outrunning the payables increase.

---

## BLOCK C: GROWTH (Max 20) — Score 20

Revenue and PAT series (screener-data, 5 years, un-restated basis — see
Basis Note above):
Revenue: 215.37 → 279.36 → 737.17 → 1,333.76 → 2,146.02
PAT: 6.95 → 10.68 → 55.47 → 126.20 → 200.22

- **C1 Revenue CAGR** (FY2022-26, 4-yr): (2,146.02/215.37)^(1/4)-1 = 77.67%
  → ≥20% = **5**
- **C2 PAT CAGR** (FY2022-26, 4-yr): (200.22/6.95)^(1/4)-1 = 131.7% → ≥20%
  = **5**
- **C3 Positive YoY revenue years**: 4 of 4 transitions positive (100%) =
  **5**
- **C4 PAT CAGR − Revenue CAGR**: 131.7% − 77.67% = +54.0pp → ≥+3pp = **5**

**Block C total: 5+5+5+5 = 20/20**

Caveat (see Basis Note #2): this growth spans a period in which the group
added six subsidiaries; the CAGR is not proven to be on a fully consistent
consolidation basis across the window, so part of the growth rate may be
scope expansion rather than organic volume/price growth. No adjustment
made — flagged only, no restated FY2022-24 series exists in the corpus.

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest year FY2026 only) — Score 13

- **D1 Net Debt ÷ EBITDA**: Borrowings Rs 887.91 cr (screener-data;
  reconciles to AR: non-current + current borrowings Rs 834.80 cr + lease
  liabilities Rs 53.12 cr = Rs 887.92 cr, AR p.116) − Cash & Bank Rs 520.94
  cr (screener-data) = Net Debt Rs 366.97 cr. EBITDA = EBIT + Depreciation
  = 251.32 + 35.80 = Rs 287.12 cr. ND/EBITDA = 1.28x → band 1-2x = **3**
  (Flagged: an internal screener cash-flow-vs-balance-sheet gap of ~Rs 232
  cr, Basis Note #3, means this could be as low as 0.47x/score 4 if the
  cash-flow-implied cash balance is used instead — not resolved from the
  corpus.)
- **D2 Interest Coverage** = EBIT ÷ Interest = 251.32 / 23.54 = 10.68x →
  ≥10x = **5**
- **D3 Debt ÷ Equity** = Borrowings Rs 887.91 cr ÷ Net Worth Rs 807.14 cr
  (screener-data = share capital 22.04 + reserves 785.10; matches AR p.116
  ex-NCI exactly) = 1.10x → band 1.0-1.5x = **1**
- **D4 Current Ratio** = Total Current Assets Rs 1,409.71 cr ÷ Total
  Current Liabilities Rs 758.29 cr (both AR p.116) = 1.86x → band 1.5-1.99x
  = **4**

**Block D total: 3+5+1+4 = 13/20**

Deal-breaker #6 check (ND/EBITDA >3x AND IC <3x → AVOID): not triggered
(1.28x and 10.68x).

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score 5

Source: AR Note 15, Equity Share Capital and promoter-shareholding
reconciliation (AR p.123) — no separate shareholding-pattern filing exists
in the corpus (Stage 0 gap, staleness noted).

Promoter holding (Manish Gupta + Vikas Jain + 2 minor holders):
FY2024 (as at 31-Mar-2024, pre-split, AR p.123): 34.98% + 34.92% = ~69.90%
FY2025 (as at 31-Mar-2025, post-split, AR p.123): 33.03% + 32.91% = 65.94%
FY2026 (as at 31-Mar-2026, AR p.123): 33.02% + 32.90% = 65.92%

Individual promoter shareholdings were numerically UNCHANGED between
31-Mar-2025 and 31-Mar-2026 (7,27,70,800 and 7,25,07,300 shares each year,
AR p.123) — the small % drop is dilution from the 51,625-share ESOP
issuance (AR Note 15), not promoter selling.

- **E1 Promoter holding (latest)**: 65.92% → ≥60% = **5**
- **E2 Promoter holding change over 3 years** (FY2024 69.90% → FY2026
  65.92%): decreased 3.98pp → decreased >3% = **0**
- **E3 Promoter pledge (latest)**: N/A (not in provided data) — no pledge/
  encumbrance disclosure found anywhere in the AR; this data lives only in
  the SEBI shareholding-pattern filing, absent this run (Stage 0 gap
  "shareholding", MEDIUM). Scored **0** per grounding rule; not confirmed
  as a >15% deal-breaker, simply unverifiable this run.
- **E4 Contingent Liabilities ÷ Net Worth (latest)**: AR Note 42
  (consolidated, p.137) discloses Corporate Guarantees given by Insolation
  Energy Ltd / Insolation Green Energy Pvt Ltd to banks (SBI Rs 215 cr,
  HDFC Rs 130 cr, Bajaj Finance Rs 50 cr, IREDA Rs 1,134 cr, AU Bank Rs
  48.72 cr, plus co-borrower/cross-guarantee items) totalling Rs 1,654.01
  cr as at 31-Mar-2026 (sum of the eight itemised guarantees, AR p.137;
  cross-checked against the standalone Note 41 total of Rs 1,577.72 cr, AR
  p.178, which covers the parent-only subset of the same guarantees).
  Against Net Worth of Rs 807.14 cr: ratio ≈ 205% → >30% = **0**.
  IMPORTANT CAVEAT: these guarantees mostly secure debt of the wholly-owned
  subsidiary that is ITSELF already consolidated (its Rs 887.91 cr group
  borrowings are already on the Block D balance sheet) — in a fully
  eliminated consolidation this would not normally count as incremental
  contingent risk. The AR discloses it in the consolidated notes as filed;
  scored mechanically as disclosed per pipeline rules (no qualitative
  override), flagged here so the number is not read as fresh off-balance-
  sheet risk on top of Block D's leverage picture.

**Block E total: 5+0+0+0 = 5/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score 15

Peer EBITDA margin, gross margin and market cap comparisons drawn from the
three peer Data_Sheet CSVs provided (WAAREEENER = Waaree Energies,
PREMIERENE = Premier Energies, WEBELSOLAR = Websol Energy Systems), all
FY2026. EBITDA computed uniformly as PBT + Interest + Depreciation − Other
Income for INA and all three peers (screener-data, each company's own
sheet).

| Metric | INA | Waaree | Premier | Websol | Peer median |
|---|---|---|---|---|---|
| EBITDA margin FY26 | 13.38% | 22.27% | 30.38% | 43.99% | 30.38% |
| Gross margin proxy FY26 ((Rev-RM)/Rev) | 9.87% | 24.50% | 36.06% | 51.72% | 36.06% |
| Market cap (Rs cr) | 1,989.36 | 75,796.13 | 45,485.94 | 3,235.82 | — |

- **M1 Pricing Power**: EBITDA margin expanded from 6.45% (FY22) to
  13.38% (FY26), +6.93pp, AND revenue CAGR 77.67% ≥10% = **5**
- **M2 Cost Advantage vs peer median EBITDA margin**: 13.38% vs 30.38% =
  -17.0pp, below peer = **0**
- **M3 Capital Efficiency**: FAT = Sales/Net Block = 2,146.02/524.89 =
  4.09x (>3x); ROCE FY26 17.99% (>15% but not >20%) → FAT>2x AND ROCE>15%
  = **3**
- **M4 Customer Stickiness**: zero revenue-decline years, BUT receivable
  days ranged 25.72-47.90 across FY2024-26 (not stable ±10) → does not
  meet the top tier; scored on the "no decline year" condition = **3**
- **M5 Scale & Dominance**: INA is the smallest by market cap of the four
  companies compared (Rs 1,989 cr vs Rs 3,236-75,796 cr for the three named
  peers). PEER DATA NEEDED for the full listed-peer set (only 3 comparators
  provided; broader solar-module-maker universe, e.g. Vikram Solar, Adani
  Solar, not in corpus) — scored conservatively on available data = **0**
- **M6 Technology/R&D**: no R&D expenditure line disclosed in
  screener-data or found as a separate AR note = N/A (not in provided
  data) = **0**
- **M7 Regulatory/License**: solar module manufacturing carries ALMM
  (Approved List of Models and Manufacturers) listing requirements but is
  not a scarce-license business; more than 10 listed module makers exist
  in India (the 3 peers here plus others not in corpus) = **0**
- **M8 Distribution**: B2B/project-sales model; no distribution-network or
  outlet data disclosed = **0**
- **M9 Brand**: gross margin proxy 9.87% vs peer median 36.06%, at/below
  peers = **0**
- **M10 Switching Costs**: revenue grew every year, BUT receivable days
  rose from 27.98 (FY22) to 47.90 (FY26), +19.92 days (>10-day threshold)
  = **0**
- **M11 Network Effects**: only 5 years available (test needs ≥6 for the
  two-window comparison) — scored conservatively on the overall trend per
  the instruction. Revenue CAGR 77.67% (≥20%). Selling & admin expense as
  % of sales: 2.60% (FY22) → 2.18% → 2.16% → 2.14% (FY25); FY2026 Selling
  and admin is blank in screener-data (not disclosed) so the most recent
  point cannot be confirmed. On the FY22-25 trend (stable/declining %) and
  revenue CAGR ≥20% = **3**
- **M12 Negative WC/Float**: WC Days (3 yrs with data) = 43.72 (FY24),
  31.48 (FY25), 62.58 (FY26) — 2 of 3 years fall in the 15-45 day band,
  but FY2026 has moved to 62.58 (>45 band), consistent with the Block B
  deterioration. Scored on the majority-of-available-years basis, flagged
  as worsening = **1**

**Block F total: 5+0+3+3+0+0+0+0+0+0+3+1 = 15/60**

Moats present (score ≥3): M1, M3, M4, M11 = **4 moats confirmed**
Moat classification (4-5 present = STRONG): **STRONG**

---

## CLASSIFICATION

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 14 | 20 |
| B — Cash Generation Quality | 2 | 20 |
| C — Growth | 20 | 20 |
| D — Balance Sheet Strength | 13 | 20 |
| E — Shareholder Alignment | 5 | 20 |
| **Core Score** | **54** | **100** |
| F — Moat Score | 15 | 60 |
| **Grand Total** | **69** | **120** |

Moat class: STRONG (4 moats confirmed: M1 Pricing Power, M3 Capital
Efficiency, M4 Customer Stickiness, M11 Network Effects-conservative)

Data confidence: 5 years of P&L history → "5-6 lower" band → flag: may not
have seen a full capacity/demand cycle for the post-fundraise, post-capex
group structure. This does NOT auto-downgrade the classification (that
only triggers at 3-4 years); no `history_downgrade`.

**Classification matrix**: Core Score 54 falls in the 40-59 band →
**AVERAGE**, independent of the STRONG moat class (the matrix only lets
moat class upgrade a Core ≥60 band).

**Deal-breaker overrides checked:**
1. Block A <8 → max GOOD: not triggered (A=14)
2. Block B <8 → max GOOD: **TRIGGERED** (B=2). Ceiling only; current
   classification (AVERAGE) is already below this cap, so no net effect,
   but recorded per instructions. Driven entirely by FY2026: CFO collapse
   to -Rs 73.13 cr and WC days blowing out to 62.58.
3. Median ROCE <10% → max AVERAGE: not triggered (23.72%)
4. Cumulative CFO/PAT <0.50 → max AVERAGE: **TRIGGERED** (ratio 0.194).
   Same FY2026 cash-conversion driver as #2.
5. Pledge >15% → max AVERAGE: cannot confirm (E3 = N/A, no data); not
   triggered on available evidence, but this is an unverified gap, not a
   clean pass.
6. ND/EBITDA >3x AND IC <3x → AVOID: not triggered (1.28x / 10.68x)
7. Revenue declined in majority of years → max AVERAGE: not triggered
   (zero decline years)
8. PAT negative in any of last 3 years → max AVERAGE: not triggered (PAT
   positive FY2024-26: 55.47/126.20/200.22)
9. History <3 years → AVERAGE: not triggered (5 years)

**FINAL CLASSIFICATION: AVERAGE**

Which years drive the deal-breakers (per pipeline note): FY2026 alone.
FY2022-FY2025 show a business scaling revenue and PAT with generally
improving margins and (through FY2025) POSITIVE cash conversion (FY2025
CFO Rs 113.10 cr against PAT Rs 126.20 cr, a healthy 0.90 ratio for that
single year). The AVERAGE classification and both triggered deal-breakers
are concentrated entirely in the FY2026 cash-conversion collapse and
balance-sheet step-up, which coincides with the Main Board migration
(09-Mar-2026) and a large capex/working-capital build. This is a
mechanical scoring artifact worth naming explicitly for the downstream
verifiers and Halt 1 dossier — not a judgment on whether it is a temporary
funding-cycle feature or a structural deterioration.

**Strongest block**: C (Growth, 20/20) — caveated by the consolidation-
scope-change flag above.
**Weakest block**: B (Cash Generation Quality, 2/20) — the FY2026 CFO/WC
collapse.

---

## SOURCE ANCHOR INDEX
- screener-data = runs/ina-2026-09-06/inputs/screening/screener-Data_Sheet.csv
- AR p.116 = CONSOLIDATED BALANCE SHEET AS AT 31 MARCH 2026 (lines
  15203-15452 of the extracted text)
- AR p.117 = CONSOLIDATED STATEMENT OF PROFIT AND LOSS and CONSOLIDATED
  STATEMENT OF CASH FLOWS (lines 15483-15779)
- AR p.119 = Note No. 4, Property Plant and Equipment movement schedule
  (lines 16126-16505)
- AR p.123 = Note No. 15 (Equity Share Capital) and promoter shareholding
  reconciliation (lines 17775-17925)
- AR p.137 = Note No. 42, Contingent Liabilities (consolidated) (lines
  21357-21437)
- AR p.160/161 = STANDALONE STATEMENT OF CASH FLOWS (lines 27029-27298;
  read but NOT used for scoring — standalone entity is immaterial vs
  consolidated group)
- AR p.178 = Note No. 41, Contingent Liabilities (standalone) (lines
  32040-32135)
- Peer files: WAAREEENER-Data_Sheet.csv, PREMIERENE-Data_Sheet.csv,
  WEBELSOLAR-Data_Sheet.csv (all in inputs/screening/)

## INPUT GAPS CARRIED FROM STAGE 0
prospectus (HIGH), results (HIGH), rating (MEDIUM), shareholding (MEDIUM),
research (LOW), screening-csv-shells (MEDIUM), sector_cap_row-mismatch
(MEDIUM), announcements-thin (MEDIUM), peer-concalls-partial (LOW),
share-count-blank-FY26 (LOW, resolved this stage via AR Note 15).

```yaml
stage: B01-gate0
company: "INA"
run_date: "2026-09-06"
model: claude-sonnet-5
status: complete
input_gaps:
  - "prospectus (HIGH)"
  - "results (HIGH)"
  - "rating (MEDIUM)"
  - "shareholding (MEDIUM)"
  - "research (LOW)"
  - "screening-csv-shells (MEDIUM)"
  - "sector_cap_row-mismatch (MEDIUM)"
  - "announcements-thin (MEDIUM)"
  - "peer-concalls-partial (LOW)"
  - "share-count-blank-FY26 (LOW, resolved via AR Note 15, p.123)"
flags:
  - type: FLAG-GATE0
    reason: "Classification AVERAGE (Core 54/100) with historical depressors concentrated entirely in FY2026: cash-conversion collapse (CFO -Rs73.13cr vs PAT +Rs200.22cr, cumulative 5yr CFO/PAT 0.194) and Working Capital Days blowout (31.48 to 62.58 days) drive both Block B (2/20) and two deal-breaker triggers (Block B<8, cumulative CFO/PAT<0.50). FY2022-FY2025 standalone-of-that-period trend was healthy (FY2025 CFO/PAT ratio 0.90). Also flags an unresolved intra-group contingent guarantee overhang (~Rs1,654cr, 205% of net worth, AR Note 42) and a consolidation-scope restatement that makes the 5yr growth CAGR not fully like-for-like."
data_years: 5
fy_range: "FY2022 to FY2026"
blocks: {A: 14, B: 2, C: 20, D: 13, E: 5}
core_score: 54
moat_score: 15
grand_total: 69
moats_confirmed: 4
moat_class: "STRONG"
classification: "AVERAGE"
deal_breakers:
  - "Block B <8 (actual 2) -> caps classification at max GOOD (no net effect, already AVERAGE)"
  - "Cumulative CFO/PAT <0.50 (actual 0.194) -> caps classification at max AVERAGE"
history_downgrade: false
data_notes:
  - "screener-Data_Sheet.csv is CONSOLIDATED basis for FY2025-26 (verified vs AR exactly); standalone FY2026 Total Assets is only Rs544.04cr vs consolidated Rs2,155.13cr -- almost all business sits in subsidiary Insolation Green Energy Pvt Ltd."
  - "AR FY2026 restates the FY2024 opening balance sheet ('1 April 2024' column) for newly-added subsidiaries (6 entities incorporated Jul-2024 to Aug-2025); restated FY2024 Total Assets (Rs274.69cr, AR p.116) and FY2025 CWIP (Rs52.88cr, AR p.116) do not match screener's own un-restated FY2024/25 figures (Rs262.78cr / Rs46.10cr) -- Block C's 5yr CAGR is not on a fully consistent consolidation basis."
  - "ROCE, Current Ratio, Trade Payables and Working Capital Days computable only for FY2024-2026 (3yrs) -- no FY2022/2023 AR in corpus to obtain the Current Liabilities / Trade Payables split; screener-Data_Sheet.csv does not carry these splits for any year."
  - "FCF/Capex proxied via AR Note 4 PPE gross-block Additions (p.119) plus change in CWIP for FY2025-26; via Delta Net Block + Depreciation + Delta CWIP for FY2023-24 (no Note 4 comparative that far back); FY2022 capex N/A (no FY2021 opening balance in corpus). CFO statement's own investing-activity capex line could not be isolated due to PDF extraction label/value separation."
  - "Internal screener cash reconciliation gap: FY2026 CFO+CFI+CFF implies closing cash of Rs753.03cr but screener's own FY2026 Cash & Bank line shows Rs520.94cr (~Rs232cr gap), unresolved from corpus; affects D1 Net Debt/EBITDA sensitivity (1.28x as reported vs 0.47x if CF-implied cash is used)."
  - "E3 Promoter pledge: no encumbrance/pledge disclosure found anywhere in the AR; this data lives only in the SEBI shareholding-pattern filing, absent this run (Stage 0 gap). Scored 0 per grounding rule, not confirmed as a >15% deal-breaker trigger."
  - "E4 Contingent liability (AR Note 42, consolidated, p.137, ~Rs1,654cr, 205% of net worth) is substantially corporate guarantees for the already-consolidated subsidiary's own bank debt (which is already on the Block D balance sheet as Rs887.91cr group borrowings); scored mechanically as disclosed with no qualitative override, but flagged so it is not double-counted as fresh off-balance-sheet risk."
  - "M5/M2/M9 peer comparison used only the 3 peer CSVs provided (Waaree, Premier Energies, Websol); broader listed solar-module-maker universe not in corpus, so M5 scored conservatively (PEER DATA NEEDED for full segment ranking)."
  - "M6 (R&D) and M8 (Distribution): no R&D expenditure line or distribution-network data disclosed anywhere in screener-data or the AR; scored 0 as N/A (not in provided data), not as a negative qualitative judgment."
  - "M11 Network Effects: only 5 years available against the test's preferred >=6yr two-window design; scored conservatively on the overall FY22-25 trend (FY2026 Selling & admin expense is blank in screener-data, not disclosed, so the most recent data point could not be confirmed)."
block_b_trend: "deteriorating - CFO swung from +Rs113.10cr (FY2025) to -Rs73.13cr (FY2026) while PAT rose from Rs126.20cr to Rs200.22cr; Working Capital Days rose from 31.48 (FY2025) to 62.58 (FY2026), driven by inventory (Rs76.98cr to Rs379.05cr) and receivables (Rs110.09cr to Rs281.59cr) both outrunning payables growth."
analyst_note: "The scorecard is a study in two eras. FY2022-FY2025 shows genuine operating improvement: margins expanded, ROCE stayed high, and FY2025 alone converted cash at 0.90x PAT. FY2026 breaks that pattern completely: PAT still grew 59% but CFO went negative, working capital days nearly doubled, and the balance sheet gained Rs1,308cr of assets funded mostly by Rs780cr of new borrowings, on the same year the company migrated to the Main Board and drew a large IREDA term loan (Rs1,134cr guarantee, Note 42). This reads like a capacity-and-working-capital ramp funded ahead of collections, not an earnings-quality failure per se, but Gate 0 cannot distinguish those two stories from numbers alone -- that judgment needs the Q1FY27 filing (absent from this corpus) and the AR's own MD&A commentary on the ramp, which stage 2+ should pull specifically. The Rs1,654cr guarantee figure and the restated-vs-unrestated FY2024/25 gap are both large enough that a verifier should re-check them independently before Halt 1."
```
