# STAGE 1 — GATE 0 SCORECARD: MODISON LTD (MODISONLTD)
Run date: 2026-09-03 | Model: Sonnet 5 | Mode: pipeline (no human in loop)

Data available: 10 years (FY2016 to FY2026, FY2019 missing) for the P&L
series, Cash Flow series, Receivables, Inventory and Net Worth
(screener-data Data_Sheet.csv). Scoring adapted to a 10-year P&L/cash
history. IMPORTANT LIMITATION: the Data_Sheet balance sheet does NOT carry
a separate Current Liabilities or Trade Payables line for any year — it
only gives Borrowings (all maturities blended) and a residual "Other
Liabilities" line that itself blends current and non-current non-debt
items. Precise Current Liabilities and Trade Payables were recovered ONLY
for FY2024-FY2026 from the two Annual Report extracts (audited standalone
and consolidated financial statements). Consequently: ROCE (Block A1/A2/A4)
and Payable-Days-dependent metrics (Block B2/B3/B4) are computed on a
3-year window (FY24-FY26), precisely anchored, while ROE (Block A3),
Receivable/Inventory Days, and cumulative CFO/PAT (Block B1) use the full
10-year window. This is stated per metric below, never estimated across
the gap.

No shareholding-pattern PDF was provided among this stage's designated
input files (Data_Sheet.csv, 3 results extracts, 2 AR extracts) and no
category-wise (promoter/FII/DII) shareholding table was found inside
either AR extract's Corporate Governance section (only a shareholding-SIZE
distribution table is present, AR p.103-104, which does not break out
promoter %). Block E1/E2/E3 (promoter holding, its 3-yr change, pledge)
are therefore N/A (not in provided data) = scored 0 each, per rule 5. (An
operator-supplied, explicitly NON-ANCHORED screener image exists elsewhere
in the run's corpus — runs/modisonltd-2026-09-03/inputs/research/
operator-supplied-shareholding-pattern.md, promoter ~52.1-52.2% flat,
0% pledge mentioned as "not in this image, check AR/rating" — but it falls
outside this stage's designated source list and is NOT used for scoring,
consistent with GROUNDED CLAIMS. It is reported here for downstream
awareness only, not anchored.)

---

## SPEAR LOAD-BEARING FACT VERIFICATION

**F1 — MARGIN PATH.** VERIFIED, direction and magnitude both hold.
Computed EBITDA = Sales − Raw Material Cost + Change in Inventory − Power
& Fuel − Other Mfr. Exp − Employee Cost − Selling & Admin − Other Expenses
(screener-data Data_Sheet.csv, P&L rows 11-19; cross-checked against the
Quarters block's own "Operating Profit" row, which sums to within ~1% of
the annual figure for both years, confirming the formula and sign
convention on "Change in Inventory"):
- FY2025: EBITDA Rs 45.35 cr / Sales Rs 490.24 cr = **9.25%** (spear cited
  ~9.6%; quarterly-summed cross-check gives 9.14%, screener-data Quarters
  rows 27-36). Small variance vs the spear brief's 9.6% is within normal
  definitional noise (other income treatment); direction and rough level
  both confirmed.
- FY2026: EBITDA Rs 118.36 cr / Sales Rs 710.33 cr = **16.66%** (spear
  cited ~16.1%; quarterly-summed cross-check gives 16.52%). Confirmed.
- Trend: margin roughly **doubled** FY25 to FY26 (9.25% → 16.66%),
  matching the spear's directional claim.
- Q1 FY27 (30-Jun-2026, screener-data Quarters row, unaudited): Operating
  Profit Rs 50.10 cr / Sales Rs 270.47 cr = 18.53% — margin momentum
  continued into the following quarter, above the guided range.
- Management's forward guidance of "at least 10-12%" next year: NOT FOUND
  in this stage's designated sources. The three results extracts provided
  (Q3 FY26, Q4/FY26 annual, Q1 FY27) are SEBI Reg. 33/30 filings only —
  board outcome letters and financial statements, no MD commentary or
  concall transcript. This guidance figure could not be independently
  verified from the corpus given to this stage; it likely originates from
  the 43rd AGM webcast (Jul-2026), which is outside this stage's reading
  list. Flag for stage 4/5 verification as B00 already directs.

**F2 — CASH CONVERSION (critical). VERIFIED, exactly as briefed, and it
is the dominant finding of this scorecard.** All figures screener-data
Data_Sheet.csv, Cash Flow and Balance Sheet rows 41, 49-51, 57:
- Cash from Operating Activity: FY2024 = **−3.89** cr, FY2025 = **−16.10**
  cr, FY2026 = **−64.19** cr — three consecutive negative years, and
  worsening each year.
- Over the same window PAT ROSE: FY24 Rs 21.36 cr → FY25 Rs 24.68 cr →
  FY26 Rs 72.54 cr.
- Borrowings: FY2025 Rs 72.76 cr → FY2026 Rs 174.47 cr (+Rs 101.71 cr,
  +139.8%). Growth and working capital are being funded by debt, not by
  the business's own cash generation.
- Receivables: FY2025 Rs 86.13 cr → FY2026 Rs 159.97 cr (+85.7%).
  Inventory: FY2025 Rs 127.48 cr → FY2026 Rs 219.80 cr (+72.4%), both far
  outrunning the 44.9% revenue growth (Sales FY25 Rs 490.24 cr → FY26
  Rs 710.33 cr) over the same year.
- Cumulative CFO ÷ Cumulative PAT, full 10-year window (FY16-FY26):
  Rs 53.06 cr ÷ Rs 223.49 cr = **0.24x**. This is the single number Block
  B is built on; it triggers deal-breaker #4 (cumulative CFO/PAT <0.50 →
  max classification AVERAGE) on its own.
This is scored honestly below, not smoothed: Block B = 0/20, the lowest
possible score, and every one of its four sub-metrics independently lands
in the bottom band.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 13/20

Formula: ROCE = EBIT ÷ (Total Assets − Current Liabilities); computed
(source lacks its own ROCE line). EBIT = PBT + Interest.
Precise Current Liabilities are available only for FY24-FY26 (Annual
Report extracts). ROCE for FY16-FY18, FY20-FY23 is **NOT FOUND** — the
Data_Sheet's "Other Liabilities" row blends current and non-current
non-debt items and cannot be split; no estimate was made.

| FY | EBIT (PBT+Int) | Total Assets | Current Liab. | Capital Employed | ROCE |
|----|------|------|------|------|------|
| FY24 | 32.06 (screener-data, PBT 29.14+Int 2.92) | 271.23 (screener-data) | 62.35 (AR-FY25 p.117, Note "Total Current Liabilities", consol comparative col) | 208.87 | **15.35%** |
| FY25 | 39.52 (screener-data, PBT 33.55+Int 5.97) | 319.26 (screener-data) | 94.44 (AR-FY26 p.141, Note "Total Current Liabilities", consol) | 224.80 | **17.58%** |
| FY26 | 106.10 (screener-data, PBT 96.95+Int 9.15) | 502.78 (screener-data) | 219.77 (AR-FY26 p.141, Note "Total Current Liabilities", consol) | 282.98 | **37.51%** |

Cross-check: company's own AR-disclosed "Return on Capital Employed" ratio
(AR-FY26 p.183, Note 50 Financial Ratios, definition = PBT+Finance Costs ÷
[Net Worth + Lease Liab. + Deferred Tax Liab. + Borrowings], a DIFFERENT,
wider capital-employed base than the framework's Total Assets − Current
Liabilities formula) reads FY26 23.31%, FY25 13.39%. Both series move the
same direction and both show the same sharp FY26 jump; absolute levels
differ because of the different Capital Employed definition. The
framework's stricter formula is used for scoring per instructions.

- **A1 Median ROCE** (n=3, FY24-26): median = 17.58% → band 15-19.9% = **3**
- **A2 Minimum single-year ROCE** (n=3): min = 15.35% (FY24) → band ≥15% = **5**
- **A3 Median ROE** (n=10, full history; ROE = PAT ÷ avg Net Worth,
  Net Worth = Equity Share Capital + Reserves, screener-data rows 39-40):
  FY16 10.43% (closing NW only, opening unavailable, stated), FY17 13.03%,
  FY18 13.59%, FY20 11.05% (opening NW is FY18 closing due to the FY19
  gap — flagged, not a clean 1-year average), FY21 14.41%, FY22 8.60%,
  FY23 6.16%, FY24 10.94%, FY25 11.75% (cross-checks to the AR's own
  disclosed 11.76%, AR-FY26 p.182, Note 50), FY26 29.53% (cross-checks to
  AR's disclosed 29.55%). Median (5th/6th of 10 sorted) = (11.05+11.75)/2
  = **11.40%** → band <12% = **0**
- **A4 ROCE trend, latest vs earliest** (within the only precise window,
  FY24 vs FY26): 37.51% vs 15.35%, latest ≥ earliest → **5**

data_notes: A1/A2/A4 rest on a 3-year window only; A3 uses the full
10-year window and both computed ROE figures for FY25/FY26 independently
cross-validate against the company's own disclosed ROE, which materially
raises confidence in the underlying PAT/Net Worth series used across this
whole scorecard.

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 0/20

**This is the block the spear gate flagged, and it fails on every leg.**

- **B1 Cumulative CFO ÷ Cumulative PAT** (n=10, full window): Cumulative
  CFO = 26.41+12.28+18.81+19.23+23.83+14.19+22.49−3.89−16.10−64.19 =
  **Rs 53.06 cr** (screener-data Data_Sheet row 57). Cumulative PAT =
  10.88+14.26+16.40+15.12+22.44+14.63+11.18+21.36+24.68+72.54 =
  **Rs 223.49 cr** (row 24). Ratio = **0.24x** → band <0.50 = **0**
  (also fires deal-breaker #4: max classification AVERAGE)
- **B2 FCF-positive years as proportion.** FCF = CFO − Capex (purchase of
  PP&E + intangibles, ex-acquisitions). Precise capex (AR Cash Flow
  Statement "Purchase of Property Plant and Equipment... including
  Capital WIP & Capital Advances" line) is available FY24-FY26 only:
  FY24 Rs 15.85 cr (AR-FY25 p.120, comparative col), FY25 Rs 15.47 cr
  (AR-FY26 p.144, comparative col; AR-FY25 primary col agrees at Rs 15.47
  cr), FY26 Rs 15.10 cr (AR-FY26 p.144). FCF FY24 = −3.89−15.85 = **−19.74**
  cr; FY25 = −16.10−15.47 = **−31.57** cr; FY26 = −64.19−15.10 = **−79.29**
  cr. All three of the only precisely-computable years are FCF-negative.
  (FY16-FY23 capex cannot be isolated from the Data_Sheet's single
  aggregate "Cash from Investing Activity" line, which the AR shows also
  contains ICD placements/redemptions, investment purchases/sales and
  interest received — e.g. in FY25 alone these non-capex items are
  worth ~Rs 6.85 cr, enough to materially distort a CFI-as-capex proxy.
  FY16-FY23 FCF is therefore marked NOT FOUND rather than approximated.)
  0 of 3 precisely-known years FCF-positive → band <50% = **0**
- **B3 Cumulative FCF ÷ Cumulative PAT** (same 3-year precise window):
  Cumulative FCF = −19.74−31.57−79.29 = **−130.60 cr**; Cumulative PAT
  (FY24-26) = 21.36+24.68+72.54 = **118.58 cr**. Ratio = **−1.10x** →
  negative → **0**
- **B4 Change in WC Days, latest vs earliest** (precise window FY24 vs
  FY26; WC Days = Receivable Days + Inventory Days − Payable Days,
  revenue basis; Trade Payables from AR only, FY16-23 not available):
  FY24: Receivable Days 59.72 (Rs 66.20cr/Rs404.56cr×365) + Inventory
  Days 86.71 (Rs96.11cr/Rs404.56cr×365) − Payable Days 8.92 (Rs9.89cr
  [AR-FY25 p.117]/Rs404.56cr×365) = **137.51 days**.
  FY26: Receivable Days 82.19 + Inventory Days 112.94 − Payable Days 8.00
  (Rs15.58cr [AR-FY26 p.141]/Rs710.33cr×365) = **187.13 days**.
  Change = +49.62 days → band increased >15 days = **0**

**block_b_trend: deteriorating.** The one number that shows it: cumulative
CFO/PAT collapsed to 0.24x over 10 years while the most recent 3 years
alone ran CFO of −3.89, −16.10, −64.19 cr against rising PAT, funded by a
Rs 101.71 cr one-year jump in borrowings (FY25→FY26).

---

## BLOCK C: GROWTH (Max 20) — Score: 17/20

(n=10, FY16-FY26, screener-data Data_Sheet.csv rows 10-24; CAGR spans the
elapsed 10 fiscal years FY16→FY26 even though FY19 has no reported data
point.)

- **C1 Revenue CAGR:** (710.33/168.18)^(1/10)−1 = **15.50%** → band
  15-19.9% = **4**
- **C2 PAT CAGR:** both endpoints positive, no loss year anywhere in the
  series (min FY23 Rs 11.18 cr). (72.54/10.88)^(1/10)−1 = **20.88%** →
  band ≥20% = **5**
- **C3 Positive YoY revenue years, proportion.** Of 8 valid single-year
  comparisons (FY18→FY20 excluded, it spans 2 years across the FY19 gap):
  FY16→17 up, FY17→18 up, FY20→21 up, FY21→22 up, **FY22→23 DOWN**
  (339.53→334.71), FY23→24 up, FY24→25 up, FY25→26 up. 7/8 = 87.5% →
  band 75-99% = **3**
- **C4 PAT CAGR − Revenue CAGR:** 20.88% − 15.50% = **+5.38pp** → band
  ≥+3pp = **5**

data_notes: one revenue-decline year exists (FY23, −1.4% YoY), fully
recovered the following year (FY24 revenue exceeded the prior peak). This
matters for M4/M10 moat scoring below (caps the top band on both).

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 15/20
(latest year, FY2026; not a bank/NBFC — standard bands apply)

- **D1 Net Debt ÷ EBITDA:** Net Debt = Borrowings 174.47 − Cash & Bank
  1.49 (screener-data row 41, 51) = **Rs 172.98 cr**. EBITDA (computed
  above) = **Rs 118.36 cr**. Ratio = **1.46x** → band 1-2x = **3**
- **D2 Interest Coverage (EBIT ÷ Interest):** EBIT Rs 106.10 cr ÷
  Interest Rs 9.15 cr (screener-data row 21) = **11.59x** → band ≥10x = **5**
- **D3 Debt ÷ Equity:** Debt Rs 174.47 cr ÷ Equity (Share Capital 3.25 +
  Reserves 271.41 = Rs 274.66 cr) = **0.64x** → band 0.5-1.0x = **3**
- **D4 Current Ratio:** Total Current Assets Rs 398.10 cr ÷ Total Current
  Liabilities Rs 219.77 cr (both AR-FY26 p.141, consol) = **1.81x** —
  cross-checks exactly to the company's own disclosed Current Ratio of
  1.81 (AR-FY26 p.182, Note 50 Financial Ratios) → band 1.5-1.99x = **4**

data_notes: Debt-Equity per the company's own Note 50 disclosure is 0.64x
(matches this calc exactly, AR-FY26 p.182). The balance sheet is not yet
stressed on a debt/coverage basis despite the borrowings jump — the
problem sits in Block B (cash quality), not yet in Block D (solvency).

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 5/20

- **E1 Promoter holding (latest quarter):** N/A (not in provided data) —
  no shareholding-pattern PDF among this stage's sources; no category
  breakdown found inside either AR extract → **0**
- **E2 Promoter holding change over 3 years:** N/A (not in provided
  data), same reason → **0**
- **E3 Promoter pledge (latest):** N/A (not in provided data). No
  "encumbrance"/pledge disclosure found in either AR extract's notes or
  directors' report sections searched → **0**
- **E4 Contingent Liabilities ÷ Net Worth (latest, FY26):** Contingent
  Liabilities Rs 6.31 cr (AR-FY26 p.165, Note 30a "Total Current
  Liabilities"... "Total" contingent-liability line, consol, Rs 630.93
  lakh) ÷ Net Worth Rs 274.66 cr (screener-data) = **2.30%** → band <5% = **5**

data_notes: this 5/20 reflects a missing-data gap in this stage's source
set, not a demonstrated alignment problem. An operator-supplied,
non-anchored lead elsewhere in the corpus (outside this stage's reading
list) shows promoter holding flat at ~52.1-52.2% for 3+ years with a tiny
uptick to 52.23% by Jun-2026 and no visible pledge line — consistent with,
but not a substitute for, a filed shareholding pattern. Flag for the next
stage that reads the shareholding-pattern/rating documents to confirm E1-E3
on a filed anchor.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 16/60

| # | Test | Score | Basis |
|---|------|-------|-------|
| M1 | Pricing Power | 3 | Margin change FY16 (15.53%) → FY26 (16.66%) = +1.13pp, within ±2pp = "stable"; Revenue CAGR 15.50% ≥10%. Note: full-period comparison masks a collapse to 7.3-9.3% margin FY22-FY25 and a sharp FY26 recovery — see Block C/spear F1. |
| M2 | Cost Advantage vs peers | 0 | PEER DATA NEEDED — no peer EBITDA margin data in this stage's sources |
| M3 | Capital Efficiency | 5 | FAT (Sales/Net Block, FY26) = 710.33/94.44 = 7.52x >3x; ROCE FY26 = 37.51% >20% (single-year, see Block A caveat on ROCE window) |
| M4 | Customer Stickiness | 3 | 1 revenue-decline year (FY23), fully recovered FY24 → "max 1 decline year, fully recovered" band |
| M5 | Scale & Dominance | 0 | PEER DATA NEEDED — no segment mcap/margin ranking data provided |
| M6 | Technology/R&D | 0 | R&D spend FY26 Rs 1.59 cr / FY25 Rs 2.11 cr (AR-FY26 p.70) ÷ Revenue = 0.22% FY26, 0.43% FY25 — below the 1% floor of even the bottom scoring band |
| M7 | Regulatory/License | 0 | Unregulated: electrical contacts manufacturing carries no licence/quota regime evidenced in the corpus |
| M8 | Distribution | 0 | No quantified Modison distribution-network figures in either AR extract (AR mentions industry-wide "transmission and distribution networks," not the company's own reach) — direct industrial B2B supply model |
| M9 | Brand | 0 | PEER DATA NEEDED for the ≥5-10pp-above-peer-median gross-margin test. Proxy GM = (Revenue−Raw Material Cost)/Revenue computed for reference only: FY25 16.13%, FY26 12.85% (declining) — not scored, no peer benchmark available |
| M10 | Switching Costs | 0 | Growth all-but-1-year holds, but receivable days rose from 62.56 (FY16) to 82.19 (FY26), +19.6 days — not "stable"; falls through both defined bands to else=0 |
| M11 | Network Effects | 5 | Latest-3yr revenue CAGR (FY23→FY26) 28.53% > prior-3yr CAGR (FY20→FY23) 15.14%; Selling & Admin/Sales declined 1.53% (FY20) → 1.09% (FY23) → 0.91% (FY26). MECHANICAL PASS ONLY — flagged: this is a component manufacturer with no economic network effect; the pass is an artifact of accelerating revenue growth and a shrinking selling-cost ratio, not evidence of a genuine network moat. Downstream stages should discount this line. |
| M12 | Negative WC/Float | 0 | WC Days (precise years only) 137.51 (FY24) to 187.13 (FY26), all >45 → bottom band |

**Moats confirmed (score ≥3): 4** — M1 (Pricing Power, 3), M3 (Capital
Efficiency, 5), M4 (Customer Stickiness, 3), M11 (Network Effects, 5;
flagged as a mechanical artifact, not a real moat — see note above).
**Moat classification: 4-5 confirmed → STRONG.** Read this with the M11
caveat: on a qualitative basis, the confirmed count would more honestly
read 3 (MODERATE), since M11's economic rationale doesn't apply to this
business.

Moat profile:
```
M1  Pricing Power       [███░░] 3/5  CONFIRMED
M2  Cost Advantage      [░░░░░] 0/5  PEER DATA NEEDED
M3  Capital Efficiency  [█████] 5/5  CONFIRMED
M4  Customer Stickiness [███░░] 3/5  CONFIRMED
M5  Scale & Dominance   [░░░░░] 0/5  PEER DATA NEEDED
M6  Technology/R&D      [░░░░░] 0/5
M7  Regulatory/License  [░░░░░] 0/5
M8  Distribution        [░░░░░] 0/5
M9  Brand               [░░░░░] 0/5  PEER DATA NEEDED
M10 Switching Costs     [░░░░░] 0/5
M11 Network Effects     [█████] 5/5  CONFIRMED (mechanical artifact — flagged)
M12 Neg. WC / Float     [░░░░░] 0/5
```

---

## CLASSIFICATION

| Block | Score | Max |
|-------|-------|-----|
| A — Return on Capital | 13 | 20 |
| B — Cash Generation Quality | 0 | 20 |
| C — Growth | 17 | 20 |
| D — Balance Sheet Strength | 15 | 20 |
| E — Shareholder Alignment | 5 | 20 |
| **CORE TOTAL** | **50** | **100** |
| F — Moat Score | 16 | 60 |
| **GRAND TOTAL** | **66** | **160** |

Data confidence: 10 years available for the P&L/cash/receivables/
inventory/net-worth series (full/moderate tier) BUT Block A's ROCE
sub-metrics and Block B's capex/payable-dependent sub-metrics rest on a
precisely-anchored 3-year window (FY24-FY26) only, flagged throughout
rather than triggering a blanket LIMITED-tier downgrade (history_downgrade
= false; the constraint is metric-specific, not a shallow overall
history).

Classification matrix: Core 50 falls in the 40-59 band → **AVERAGE**
(this band is Core-score-determined regardless of moat class).

Deal-breaker overrides checked:
1. Block A (13) <8? No.
2. **Block B (0) <8? YES → caps classification at max GOOD.**
3. Median ROCE (17.58%, 3-yr window) <10%? No.
4. **Cumulative CFO/PAT (0.24x) <0.50? YES → caps classification at max AVERAGE.**
5. Pledge >15%? NOT FOUND — cannot confirm or rule out; not triggered on available evidence.
6. ND/EBITDA (1.46x) >3x AND IC (11.59x) <3x? No (neither leg true).
7. Revenue declined in majority of years? No (1 of 8 comparisons).
8. PAT negative in any of last 3 years? No (all positive: 21.36, 24.68, 72.54).
9. History <3 years? No.

Most restrictive applicable cap: **max AVERAGE** (deal-breaker #4). The
Core-score-driven classification (AVERAGE) already sits at that ceiling,
so the deal-breakers confirm rather than further lower the outcome.

## FINAL CLASSIFICATION: AVERAGE

Strongest block: **C — Growth (17/20)**. Weakest block: **B — Cash
Generation Quality (0/20)**, by a wide margin the defining fact of this
scorecard.

Decision line: Modison shows strong, accelerating top-line and margin
growth (Revenue CAGR 15.5%, PAT CAGR 20.9%, EBITDA margin 9.25%→16.66%
FY25→FY26) sitting directly on top of a cash-conversion collapse (CFO
negative three straight years, cumulative CFO/PAT 0.24x, working capital
days up ~50 in two years, borrowings up 139.8% in one year). Growth and
cash quality are pulling in opposite directions; deal-breaker #4 caps this
scorecard at AVERAGE regardless of the growth and balance-sheet numbers
elsewhere. This is a flag for growth-induced-vs-structural determination
downstream (per B00's own analyst_note), not a verdict — Gate 0 does not
halt on company quality, and this scorecard's role is to surface the
tension prominently, which it does via Block B's 0/20 and the FLAG-GATE0
entry below.

---

## YAML BLOCK

```yaml
stage: B01-gate0
company: "MODISONLTD"
run_date: "2026-09-03"
model: claude-sonnet-5
status: complete
input_gaps:
  - "no filed shareholding-pattern PDF in this stage's source set: Block E1/E2/E3 (promoter holding, 3yr change, pledge) scored 0, N/A (not in provided data)"
  - "no announcements/ folder: not scored by Gate 0 but carried forward per B00"
  - "Data_Sheet.csv balance sheet lacks a Current Liabilities / Trade Payables line for FY16-FY23: ROCE (A1/A2/A4) and Payable-Days-dependent metrics (B2/B3/B4) computed on a precise FY24-FY26 window only, not estimated for earlier years"
flags:
  - {type: FLAG-GATE0, reason: "Classification AVERAGE (Core 50/100) driven by Block B = 0/20: cumulative CFO/PAT 0.24x over FY16-26, three straight negative-CFO years FY24-26 (-3.89, -16.10, -64.19 cr) against rising PAT (21.36 to 72.54 cr), funded by a Rs 101.71 cr one-year borrowings jump FY25-FY26 and a working-capital-days rise of ~50 days FY24-FY26. Deal-breaker #4 (cumulative CFO/PAT <0.50) caps classification at max AVERAGE."}
  - {type: FLAG-CASH, reason: "Three consecutive negative operating cash flow years despite rising PAT; growth (revenue +44.9% FY25-26) funded by debt (+139.8%) and a receivables/inventory build that outran revenue growth. Growth-induced-vs-structural determination needed downstream with receivables ageing and the full 3-year CFO trend."}
  - {type: FLAG-DATA-GAP, reason: "Shareholding pattern not filed in corpus provided to this stage; Block E1-E3 unscored (0) pending a filed anchor at a later stage."}
data_years: 10
fy_range: "FY16 to FY26 (FY19 missing)"
blocks: {A: 13, B: 0, C: 17, D: 15, E: 5}
core_score: 50
moat_score: 16
grand_total: 66
moats_confirmed: 4
moat_class: "STRONG"
classification: "AVERAGE"
deal_breakers: ["Block B <8 (max GOOD)", "cumulative CFO/PAT <0.50 (max AVERAGE)"]
history_downgrade: false
data_notes:
  - "EBITDA computed as Sales - Raw Material Cost + Change in Inventory - Power&Fuel - Other Mfr Exp - Employee Cost - Selling&Admin - Other Expenses (sign convention on Change in Inventory verified against the Quarters block's own Operating Profit row, which the annual figure reconciles to within ~1%)"
  - "ROCE (A1/A2/A4): precise 3-year window (FY24-FY26) only; company's own AR-disclosed ROCE (different capital-employed definition: Net Worth+Lease Liab+DTL+Borrowings) reads 23.31% FY26 / 13.39% FY25, directionally consistent"
  - "ROE (A3) cross-validated: computed FY25 11.75% and FY26 29.53% match the AR's own disclosed Return on Equity Ratio of 11.76% and 29.55% almost exactly (AR-FY26 p.182, Note 50)"
  - "FCF (B2/B3) precise for FY24-FY26 only; FY16-FY23 capex cannot be isolated from Data_Sheet's aggregate Cash from Investing Activity line, which the AR shows contains non-capex items (ICD movements, investment purchases/sales, interest received) material enough (~Rs 6.85 cr in FY25 alone) to distort a CFI-as-capex proxy - marked NOT FOUND rather than approximated"
  - "M9 Brand gross-margin proxy computed for reference only, not scored: (Revenue-Raw Material Cost)/Revenue = 16.13% FY25, 12.85% FY26 (PEER DATA NEEDED to score)"
  - "M11 Network Effects passes the mechanical test (accelerating 3yr revenue CAGR, declining selling-expense ratio) but the underlying business (electrical contacts component manufacturer) has no genuine network-effect economics; flagged as a mechanical artifact, downstream stages should discount this moat"
  - "One data reconciliation gap left unresolved: Data_Sheet's FY24 Cash from Investing Activity (-15.40 cr) does not match the AR-disclosed FY24 investing cash flow (-20.54 cr consol / -20.28 cr standalone, per the FY25 AR's comparative column); Data_Sheet used as primary per instructions, AR capex figure substituted only for the FCF capex component, discrepancy not otherwise resolved"
block_b_trend: "deteriorating - cumulative CFO/PAT 0.24x over 10 years (FY16-26); most recent 3 years alone: CFO -3.89, -16.10, -64.19 cr against rising PAT (21.36 to 72.54 cr), funded by a Rs 101.71 cr one-year borrowings jump FY25-FY26"
analyst_note: "Block B (0/20) is the whole story of this scorecard: every one of its four sub-metrics independently lands in the bottom scoring band, and it is corroborated across three independent evidence lines (Data_Sheet CFO series, AR-precise capex/payables for FY24-26, and the borrowings jump). Growth (Block C, 17/20) and near-term balance-sheet ratios (Block D, 15/20) both look strong in isolation, which is exactly the pattern a growth-funded-by-debt story produces before it shows up in interest coverage or gearing. ROCE and WC-days precision is confined to a 3-year window because Data_Sheet.csv never carries a Current Liabilities or Trade Payables line; this is a genuine source-granularity gap, not a shortcut, and it does not change Block B's verdict since B1 (the softest-data sub-metric) already uses the full 10-year window and lands at 0.24x on its own. Promoter alignment (Block E) is unscored on filed evidence, not adverse; treat E's 5/20 as a data gap flag for the next stage, not a governance finding."
```
