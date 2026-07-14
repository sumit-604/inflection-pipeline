# STAGE 1 — GATE 0 QUANTITATIVE SCORECARD
## Aurum Proptech Ltd (AURUM) | CMP ₹240 | Market Cap ₹1,726 Cr | Run date 2026-07-14

Data available: 10 years of raw feed (FY17-FY26) in screener-Data_Sheet.csv, but
**FY17-FY21 belong to a divested, unrelated business** — Aurum Proptech was
Majesco Ltd until FY19 (US enterprise insurance-software business, FY19 Sales
₹988.10 Cr (screener-data)), which was sold; FY20 Sales collapsed to ₹10.24 Cr
(screener-data) as the shell was rebuilt into the current proptech/SaaS platform
(NestAway, HelloWorld, Sell.do, Aurum Analytica, PropTiger). FY17-FY21 are
excluded from every block below as a different enterprise.

**Usable post-transformation history: 5 years, FY22 to FY26 (screener-data).
Scoring adapted to a 5-year history.** Data confidence band = 5-6 years =
"lower, flag — may not have seen a full cycle" (per Data confidence table);
this does not fall in the 3-4 year auto-downgrade band, but given the business
itself is only 5 years old (not merely a data-window artefact), `history_downgrade`
is set **true** below as a qualitative caveat carried forward (see YAML notes).

FY26 (audited, year ended Mar-2026) is the first full profit year: Net Profit
+₹1.90 Cr, after FY24 -₹55.75 Cr and FY25 -₹33.37 Cr (screener-data). Quarterly
PAT turned positive in Q3 FY26 (+₹3.26 Cr) and Q4 FY26 (+₹16.64 Cr)
(screener-data, Quarters). **FY26 profit includes a ~₹17.72 Cr (₹1,772 lakh)
one-time gain** from the partial sale of the Q5/Q6 buildings (Navi Mumbai),
recognised as "Other Income from Discontinued Operations" on transfer of
possession of one floor (results Q4 FY26 PDF p.15, Note 5 — Discontinued
operations). This is flagged wherever it materially distorts an FY26 ratio.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 5/20

Basis: ROCE not carried in screener-Data_Sheet (Ratios sheet is an empty
template) — **computed**. EBIT = PBT + Interest (screener/Ind-AS convention,
other income remains inside PBT). Capital Employed = Net Worth (Equity Share
Capital + Reserves) + Total Borrowings (screener-data "Borrowings" row, which
bundles financial borrowings AND Ind AS 116 lease liabilities — confirmed
against the audited FY26 balance sheet: ₹0.45+₹1.28 Cr non-current+current
financial borrowings + ₹150.18+₹72.85 Cr non-current+current lease liabilities
= ₹224.76 Cr, matching screener-data Borrowings FY26 exactly (results Q4 FY26
PDF p.16, audited consolidated balance sheet)). This proxy for Capital
Employed is not identical to "Total Assets − Current Liabilities" (which would
require a current/non-current split unavailable for FY22-FY24); cross-checked
against FY26 audited data it is within 0.2% of the strict figure (₹731.01 Cr
proxy vs ₹732.39 Cr strict), but diverges by up to ~10% in FY25 owing to
short-term borrowings sitting inside the proxy. Used consistently FY22-FY26,
flagged as a computation-basis limitation.

| FY | PBT (screener-data) | Interest (screener-data) | EBIT=PBT+Int | Net Worth (screener-data) | Borrowings (screener-data) | Capital Employed | ROCE |
|----|------|------|------|------|------|------|------|
| FY22 | -16.79 | 0.25 | -16.54 | 168.08 | 7.55 | 175.63 | -9.42% |
| FY23 | -51.07 | 8.52 | -42.55 | 222.54 | 98.57 | 321.11 | -13.25% |
| FY24 | -77.80 | 25.97 | -51.83 | 180.38 | 323.24 | 503.62 | -10.29% |
| FY25 | -44.47 | 29.23 | -15.24 | 274.35 | 273.34 | 547.69 | -2.78% |
| FY26 | -2.61 | 26.86 | 24.25 | 506.25 | 224.76 | 731.01 | +3.32% |

(all rows: screener-data, computed)

- **A1 Median ROCE** = -9.42% (median of the 5 values above) → <10% band → **A1 = 0**
- **A2 Minimum single-year ROCE** = -13.25% (FY23) → <8% band → **A2 = 0**
- **A3 Median ROE**: ROE = PAT ÷ average Net Worth (opening+closing÷2). Opening Net
  Worth FY22 = FY21 Equity Share Capital ₹14.31 Cr + Reserves ₹161.03 Cr =
  ₹175.34 Cr (screener-data).

| FY | PAT (screener-data) | Avg Net Worth | ROE |
|----|------|------|------|
| FY22 | -11.16 | 171.71 | -6.50% |
| FY23 | -28.89 | 195.31 | -14.79% |
| FY24 | -55.75 | 201.46 | -27.68% |
| FY25 | -33.37 | 227.37 | -14.68% |
| FY26 | +1.90 | 390.30 | +0.49% |

  Median ROE = -14.68% (FY25) → <12% band → **A3 = 0**
- **A4 ROCE trend, latest vs earliest**: FY26 (+3.32%) ≥ FY22 (-9.42%) →
  **A4 = 5**

**Block A = 0+0+0+5 = 5/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 3/20

CFO (screener-data, Cash Flow): FY22 -24.26, FY23 -50.06, FY24 20.21, FY25
27.68, FY26 62.93. Cumulative CFO (FY22-FY26) = **36.50 Cr**.
PAT cumulative (FY22-FY26, screener-data) = **-127.27 Cr**.

- **B1 Cumulative CFO ÷ Cumulative PAT** = 36.50 ÷ -127.27 = **-0.29** →
  <0.50 band → **B1 = 0** (ratio is mechanically negative because cumulative
  PAT is negative; flagged as a loss-period artefact, not a cash-quality
  signal in the conventional sense — cumulative CFO is itself positive)

FCF = CFO − Capex (purchase of PPE + intangibles, cash-flow basis, excl.
acquisitions). Capex only obtainable for FY24-FY26 from the two annual
reports/results in-run (FY22/FY23 cash-flow statements not provided —
**N/A (not in provided data)**, excluded from B2/B3 rather than estimated):

| FY | CFO (screener-data) | Capex (AR FY25 p.215 / results Q4 FY26 PDF p.17, cash flow stmt) | FCF |
|----|------|------|------|
| FY24 | 20.21 | 104.45 | -84.24 |
| FY25 | 27.68 | 19.38 | +8.30 |
| FY26 | 62.93 | 15.85 (continuing ops only; discontinued-ops capex not separately disclosed) | +47.08 |

- **B2 FCF-positive years as proportion** (of 3 years with capex data) = 2/3
  = 66.7% → 50-74% band → **B2 = 2**
- **B3 Cumulative FCF ÷ Cumulative PAT** (same 3-year window, FY24-FY26):
  Cumulative FCF = -84.24+8.30+47.08 = **-28.86**; Cumulative PAT (FY24-FY26)
  = -55.75-33.37+1.90 = **-87.22**. Ratio = -28.86 ÷ -87.22 = **0.33** →
  0.20-0.39 band → **B3 = 1** (both cumulative figures negative; ratio is
  positive as an arithmetic artefact, flagged)
- **B4 Change in WC Days, latest vs earliest**: Trade Payables not carried in
  screener-Data_Sheet at all; sourced from AR/results, available only FY24-FY26
  (AR FY25 p.211, Note 10.c / results Q4 FY26 PDF p.16). Inventory = NIL all
  years (screener-Data_Sheet Inventory row blank; platform/rental business, no
  inventory).

| FY | Receivable Days (Receivables÷Sales×365, screener-data) | Payable Days (AR/results, screener-data Sales denominator) | WC Days |
|----|------|------|------|
| FY24 | 39.61 | 59.14 (AR FY25 p.211: ₹34.69 Cr) | -19.53 |
| FY25 | 40.11 | 44.70 (results Q4 FY26 PDF p.16, restated: ₹32.31 Cr) | -4.59 |
| FY26 | 50.03 | 30.79 (results Q4 FY26 PDF p.16: ₹32.15 Cr) | +19.24 |

  Latest (FY26, +19.24) vs earliest-available (FY24, -19.53): change =
  +38.77 days → increased >15 days → **B4 = 0**

**Block B = 0+2+1+0 = 3/20**

**block_b_trend: improving** — CFO went from -₹24.26 Cr (FY22) to +₹62.93 Cr
(FY26); FCF swung from -₹84.24 Cr (FY24) to +₹47.08 Cr (FY26). The trend
line is positive even though every banded sub-score is weak, because the
bands are calibrated on cumulative figures dominated by the FY22-FY25 loss
years.

---

## BLOCK C: GROWTH (Max 20) — Score: 10/20

Revenue (screener-data): FY22 15.79, FY23 126.87, FY24 214.05, FY25 263.84,
FY26 381.09.

- **C1 Revenue CAGR (FY22→FY26, 4 years)** = (381.09÷15.79)^(1/4)-1 =
  **+121.6%** → ≥20% band → **C1 = 5**. Flagged: this is inflated by the
  FY22 base being the first, near-zero year of the rebuilt business (₹15.79
  Cr). Supplementary, less base-distorted figure: 3-year CAGR FY23→FY26 =
  (381.09÷126.87)^(1/3)-1 = **+44.3%** — still comfortably ≥20%, so the score
  is robust to the choice of window.
- **C2 PAT CAGR**: PAT is negative at the start (FY22 -11.16) →
  **N/M (negative endpoint)** → **C2 = 0**. `data_notes`: loss-to-profit
  swing, FY25 to FY26 (FY22-FY25 all net losses; FY26 first profit year).
- **C3 Positive YoY revenue years proportion**: FY23 +703.6%, FY24 +68.7%,
  FY25 +23.3%, FY26 +44.4% (all screener-data) — 4 of 4 years positive =
  100% → **C3 = 5**
- **C4 PAT CAGR − Revenue CAGR**: PAT CAGR is N/M → **C4 = 0** (per rule)

**Block C = 5+0+5+0 = 10/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 9/20

All figures latest = FY26 (audited, Mar-2026).

- **D1 Net Debt ÷ EBITDA**: Net Debt = Borrowings ₹224.76 Cr (screener-data;
  cross-verified above) − Cash & Bank ₹81.00 Cr (screener-data; matches
  audited BS Cash & cash equivalents ₹17.54 Cr + other bank balances ₹63.46
  Cr = ₹81.00 Cr, results Q4 FY26 PDF p.16) = **₹143.76 Cr**. EBITDA = PBT +
  Interest + Depreciation (screener-data) = -2.61+26.86+103.74 = **₹127.99
  Cr**. Net Debt÷EBITDA = **1.12x** → 1-2x band → **D1 = 3**. Flagged: this
  EBITDA is materially inflated by Ind AS 116 right-of-use depreciation
  (₹103.74 Cr, screener-data) typical of the lease-heavy coliving/rental
  model, and by the ~₹17.72 Cr one-time building-sale gain sitting inside
  FY26 PBT (results Q4 FY26 PDF p.15, Note 5). Ex-one-time EBITDA ≈ ₹110.27
  Cr, giving Net Debt÷EBITDA ≈ 1.30x — same scoring band, so the score is
  unaffected, but the underlying ratio quality is weaker than it looks.
- **D2 Interest Coverage (EBIT÷Interest)**: EBIT = PBT+Interest = **₹24.25
  Cr**; Interest = **₹26.86 Cr** (screener-data). IC = **0.90x** → <1.5x
  band → **D2 = 0**. Ex-one-time-gain EBIT ≈ ₹6.53 Cr → IC ≈ 0.24x — still
  <1.5x, so the weak coverage is not an artefact of the one-time item; it is
  understated by leaving it in, not overstated.
- **D3 Debt ÷ Equity**: Borrowings ₹224.76 Cr ÷ Net Worth (Equity Share
  Capital + Reserves) ₹506.25 Cr (screener-data) = **0.44x** → 0.1-0.5 band
  → **D3 = 4**
- **D4 Current Ratio**: Total current assets ₹298.68 Cr ÷ Total current
  liabilities ₹215.64 Cr (results Q4 FY26 PDF p.16, audited consolidated
  balance sheet; excludes the separately-disclosed ₹40.98 Cr assets / ₹64.13
  Cr liabilities of the disposal group held for sale, per the company's own
  balance-sheet presentation) = **1.39x** → 1.2-1.49 band → **D4 = 2**.
  (If held-for-sale items are included as current: ₹339.66÷₹279.77 = 1.21x —
  same band, score unchanged.)

**Block D = 3+0+4+2 = 9/20**

Note: Net Debt÷EBITDA (1.12x, not >3x) means **deal-breaker #6 (AVOID
override) does NOT trigger** — the leverage itself is not the risk here;
interest coverage is.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 9/20

- **E1 Promoter holding (latest quarter, Mar-2026)** = 47.41% (screener
  shareholding screenshot, operator-supplied 2026-07-14) → 40-49.9% band →
  **E1 = 3**
- **E2 Promoter holding change over ~3 years**: Jun-2023 (50.34%) → Mar-2026
  (47.41%) = -2.93pp (operator-supplied screenshot) → decreased 1-3% band →
  **E2 = 1**. Note: the step-down is concentrated Jun-2025 (49.81%) →
  Sep-2025 (47.04%), coincident with the FY23 Rights Issue call-money window;
  stage 8 to determine dilution vs open-market sale (per OPERATOR_CONTEXT.md).
- **E3 Promoter pledge (latest)**: **N/A (not in provided data)** — not
  disclosed in the operator shareholding screenshot (3-row Promoters/FII/
  Public view, no pledge column), and not found anywhere in AR_FY25.txt
  despite a targeted search (no "pledge/encumbered" disclosure in the
  Corporate Governance shareholding-pattern section, AR FY25 p.100-101).
  Per rule 5, scored **0**; carried to `input_gaps` for phase-3 confirmation
  via BSE/screener pledge disclosure (not a confirmed breach — genuinely
  absent from all sources in-run, not scored as if pledge >15%).
- **E4 Contingent Liabilities ÷ Net Worth (latest available)**: Latest formal
  disclosure is FY25 (AR FY25 p.266, Note 22 — Commitments and contingent
  liabilities; FY26 AR not yet issued/available in this run's inputs).
  Contingent Liabilities = Income tax matters ₹0.41 Cr + GST matters ₹3.62 Cr
  = **₹4.03 Cr** (quantified items only; a separate furniture-lease
  arbitration matter, ₹6.54 Cr claim with ₹3.06 Cr already provisioned and
  ₹0.77 Cr deposited on appeal, is not included as an unquantified residual
  contingent exposure — AR FY25 p.266). Net Worth FY25 (total equity, AR FY25
  p.210) = **₹284.47 Cr**. Ratio = 4.03÷284.47 = **1.42%** → <5% band →
  **E4 = 5**

**Block E = 3+1+0+5 = 9/20**

---

## CORE SCORE

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 5 | 20 |
| B — Cash Generation Quality | 3 | 20 |
| C — Growth | 10 | 20 |
| D — Balance Sheet Strength | 9 | 20 |
| E — Shareholder Alignment | 9 | 20 |
| **CORE TOTAL** | **36** | **100** |

Strongest block: **C — Growth (10/20)**. Weakest block: **B — Cash
Generation Quality (3/20)**.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

| # | Test | Score | Basis |
|---|---|---|---|
| M1 | Pricing Power | **5** | Operating EBITDA margin (Sales − Employee − Other opex, screener-data, excl. other income) moved from -120.2% (FY22) to -12.8% (FY23), +1.5% (FY24), +17.6% (FY25), +22.1% (FY26); expansion far exceeds 2pp and revenue CAGR ≥10% on any sub-window (e.g. FY23→FY26 margin +34.9pp, CAGR +44.3%) |
| M2 | Cost Advantage vs peer median EBITDA margin | **0** | **PEER DATA NEEDED** — no peer financial statements provided in-run (only peer concall transcripts for ZAGGLE/RATEGAIN/NAZARA/CARTRADE, no margin data extracted at this stage) |
| M3 | Capital Efficiency | **0** | FAT (Sales÷Net Block) FY26 = 381.09÷518.47 (screener-data) = 0.74x, <1x; ROCE FY26 = 3.32% (computed above), <12% → below the lowest band |
| M4 | Customer Stickiness | **3** | Zero revenue-decline years FY23-FY26 (screener-data), but receivable days are not stable within ±10 across the full available window (39.6-53.4 days, FY23-FY26) — scored at the "max 1 decline year, fully recovered" tier as the closest fit given zero decline years but receivables volatility above the ±10-day threshold for the top band |
| M5 | Scale & Dominance | **0** | **PEER DATA NEEDED** — no peer market-cap/segment-margin ranking data provided in-run |
| M6 | Technology / R&D | **0** | AR FY25 explicitly discloses "expenditure incurred on Research and Development: Nil" (AR FY25, Form MBP/Annexure on Conservation of Energy). Product development cost is capitalised as intangibles rather than expensed as R&D, but the formal R&D/Revenue metric required by the test is 0%, below the ≥1% floor |
| M7 | Regulatory / License | **0** | Core proptech/SaaS/rental-marketplace business is unregulated; the new SM REIT license (secured 2025, first product targeted FY27, results Q4 FY26 PDF p.4) is a nascent sub-vertical, not yet the core business — scored as unregulated overall |
| M8 | Distribution | **1** | Reach is quantified (rental: 5,214 houses -23% YoY rationalisation, 9,559 signed units +3%, 19,286 beds +9%, occupancy 76%, results Q4 FY26 PDF p.4 / OPERATOR_CONTEXT item 4) but mixed — the primary footprint metric (houses) is shrinking as the model premiumises, so "network growing" is not clearly satisfied; scored at the "mentioned/quantified but not clearly growing" tier |
| M9 | Brand | **0** | **PEER DATA NEEDED** — no peer gross-margin data provided in-run to benchmark the GM proxy |
| M10 | Switching Costs | **5** | Revenue grew every year FY23-FY26 (screener-data); receivable days over the same window fell from 53.44 (FY23) to 50.03 (FY26), i.e. did not rise — well within the ≤10-day-rise threshold |
| M11 | Network Effects | **3** | Only 3-4 comparable years available, below the ≥6-year two-window test threshold — scored conservatively on overall trend as instructed: Selling & admin expense ÷ Sales declined FY23→FY25 (47.0%→37.6%→33.0%, screener-data; FY26 not separately disclosed, bundled into Other Expenses) while 3-year revenue CAGR (FY23-FY26) = +44.3%, ≥20% → matches the "rev CAGR ≥20% AND selling% stable/declining" tier |
| M12 | Negative WC / Float | **5** | WC Days negative in 2 of the 3 years for which payables data exists (FY24 -19.53, FY25 -4.59, FY26 +19.24) — majority negative on the available sample. Flagged: sample is only 3 years (payables not available FY22-FY23) and the trend reversed to positive in the latest year, driven by receivable days rising to 50.0 while payable days fell to 30.8 (screener-data / AR / results) — a caveat on data breadth and directional worsening, not a rule override |

**Moat score = 5+0+0+3+0+0+0+1+0+5+3+5 = 22/60**

Moats "present" (score ≥3): M1, M4, M10, M11, M12 = **5 confirmed**

```
M1  Pricing Power        [#####] 5  PRESENT
M2  Cost Advantage       [     ] 0  PEER DATA NEEDED
M3  Capital Efficiency   [     ] 0
M4  Customer Stickiness  [###  ] 3  PRESENT
M5  Scale & Dominance    [     ] 0  PEER DATA NEEDED
M6  Technology / R&D     [     ] 0
M7  Regulatory / License [     ] 0
M8  Distribution         [#    ] 1
M9  Brand                [     ] 0  PEER DATA NEEDED
M10 Switching Costs      [#####] 5  PRESENT
M11 Network Effects      [###  ] 3  PRESENT
M12 Negative WC / Float  [#####] 5  PRESENT
```

Moat classification: 5 present → **STRONG** (band: 4-5 = STRONG)

---

## CLASSIFICATION

Core Score = 36 (<40) → matrix rule "Core <40 = AVOID" applies before any
deal-breaker cap is even relevant.

Data confidence: 5-year usable history → "5-6 lower, flag: may not have seen
full cycle" band (not the 3-4-year automatic one-tier downgrade band).
Because the underlying business itself is only 5 years old (not a data
artefact), `history_downgrade` is recorded **true** as a qualitative caveat.

**Deal-breaker checks (recorded per pipeline rule; caps only bind if they are
BELOW the matrix result — here the matrix result, AVOID, is already the
floor, so no cap changes the outcome, but all are recorded with driving
years as instructed):**

1. Block A (5) < 8 → cap max GOOD — **triggered**, driven by FY22-FY26 median/min ROCE
2. Block B (3) < 8 → cap max GOOD — **triggered**, driven by FY22-FY23 negative CFO years dominating the cumulative ratios
3. Median ROCE (-9.42%) < 10% → cap max AVERAGE — **triggered**
4. Cumulative CFO÷PAT (-0.29) < 0.50 → cap max AVERAGE — **triggered**
5. Pledge > 15% → cap max AVERAGE — **not triggered** (pledge data unavailable, not confirmed as a breach)
6. Net Debt÷EBITDA >3x AND IC <3x → AVOID — **not triggered** (ND/EBITDA = 1.12x, not >3x)
7. Revenue declined in majority of years → cap max AVERAGE — **not triggered** (0 decline years, FY23-FY26)
8. PAT negative in any of last 3 years → cap max AVERAGE — **triggered**, driven by FY24 (-55.75) and FY25 (-33.37); FY26 (+1.90) is the exception
9. History < 3 years → AVERAGE — **not triggered** (5 usable years, FY22-FY26)

**CLASSIFICATION: AVOID** (mechanical, driven by Core Score 36/100 <40)

---

## FLAG-GATE0

Classification (AVOID) is ≤ AVERAGE with clearly identified historical
depressors: **the entire Core score is dominated by FY22-FY25, the loss-making
rebuild years of a business relaunched after the Majesco divestment.** FY26 is
the first profit year (two consecutive profitable quarters, Q3 and Q4 FY26),
Revenue CAGR is strong on any window (C1/C3 both scored 5/5), and the
quantitative moat scan independently finds a STRONG moat class (5 of 12 tests
present) built on pricing power, switching costs, negative-WC float and early
network-effect signals — none of which depend on the historical loss years.
This is analogous in spirit to the deal-breaker note's "documented post-IPO
rebase / legacy cleanup" carve-out (here: post-divestment rebuild, not
post-IPO), and is flagged for downstream (stage 11/13) weighing rather than
treated as a clean AVOID. Grand total (Core 36 + Moat 22 = **58**) sits well
above what the Core-alone classification implies, reflecting the split
between a weak historical mechanical record and a materially stronger
forward-emerging quality signal.

---

## DECISION LINE

Gate 0 mechanical score: **AVOID** (Core 36/100, STRONG moat class 5/12,
Grand Total 58/160). Driven entirely by four years of losses (FY22-FY25) in a
business that was rebuilt from scratch after the FY19-20 Majesco divestment;
FY26 is the first profit year. Cash generation (Block B, weakest at 3/20) and
return on capital (Block A, 5/20) are the two blocks doing the damage — both
are backward-looking and both are inflecting per the FY26 audited numbers and
the two consecutive profitable quarters. Interest coverage (D2 = 0, IC 0.90x)
is the one balance-sheet metric that stays weak even after stripping the
one-time building-sale gain, and is the genuine ongoing risk to carry forward,
not an artefact of the loss-year history. Human review required; flagged
FLAG-GATE0 for stage 11/13 to weigh the historical-depressor context against
the mechanical AVOID.

---

## INPUT GAPS CARRIED FORWARD

- rating/ folder absent from inputs (no credit rating data collected in-run)
- announcements/ folder absent; operator-supplied summary only (OPERATOR_CONTEXT.md), corroborated where possible against the two results PDFs and four concall transcripts in-run; items with no anchored corroboration (rights-issue CARE deviation, Q5/Q6 building sale filing, Jul-2026 fund-raise board intimation) carried as directional operator context, not anchored figures
- Shareholding % filled from an operator-supplied screener screenshot (treated as anchored per provenance rules in OPERATOR_CONTEXT.md), not a freshly pulled CSV
- Prospectus not expected/not collected (long-listed company, not a recent IPO)
- sector_cap_row "Platform / SaaS / IT services" appears correct on the business description but is carried as unconfirmed — flagged for phase-3 confirmation
- Promoter pledge % (E3) not found in any provided source (operator screenshot, AR_FY25.txt, results PDFs) — scored 0 per rule 5, flagged for phase-3 confirmation via BSE/screener pledge disclosure, NOT treated as a confirmed >15% breach
- FY22/FY23 capex (cash flow statement) not available in-run (no AR predating FY24-25 collected) — B2/B3 computed on the FY24-FY26 subset only, disclosed explicitly above
- FY22/FY23 trade payables not available in-run — B4 (WC Days trend) computed on the FY24-FY26 subset only, disclosed explicitly above
- Peer financial statements (margins, market cap) not provided in-run (only peer concall transcripts for ZAGGLE/RATEGAIN/NAZARA/CARTRADE) — M2, M5, M9 scored 0 and marked PEER DATA NEEDED
- Latest formal contingent-liability disclosure available is FY25 (AR), not FY26 (FY26 AR not yet issued/collected in-run) — E4 uses the FY25 figure with this lag disclosed

---

```yaml
stage: B01-gate0
company: "Aurum Proptech Ltd"
run_date: "2026-07-14"
model: claude-sonnet-5
status: complete
input_gaps:
  - "rating/ folder absent from inputs"
  - "announcements/ folder absent; operator-supplied summary only, partially corroborated"
  - "shareholding % filled from operator-supplied screener screenshot, not fresh CSV"
  - "prospectus not expected (long-listed, not recent IPO)"
  - "sector_cap_row 'Platform / SaaS / IT services' unconfirmed, flag for phase-3"
  - "promoter pledge % (E3) not found in any provided source; scored 0, not a confirmed breach"
  - "FY22/FY23 capex not available; B2/B3 computed on FY24-FY26 subset only"
  - "FY22/FY23 trade payables not available; B4 computed on FY24-FY26 subset only"
  - "peer financial statements not provided; M2/M5/M9 marked PEER DATA NEEDED"
  - "latest contingent-liability disclosure available is FY25 AR, not FY26 (one-year lag)"
flags:
  - type: FLAG-GATE0
    reason: "Classification AVOID (<=AVERAGE) driven by FY22-FY25 loss years of a post-Majesco-divestment business rebuild; FY26 is the first profit year with two consecutive profitable quarters (Q3, Q4 FY26) and a STRONG moat class (5/12) built on non-historical signals (pricing power, switching costs, negative WC, growth). Flagged for stage 11/13 to weigh the inflection against the mechanical score, analogous to the deal-breaker override note for documented legacy-cleanup cases."
  - type: FLAG-DATA-GAP
    reason: "Promoter pledge % (E3) not found in any provided source (operator screenshot, AR_FY25.txt, results PDFs); scored 0 per rule 5. Needs phase-3 confirmation via BSE/screener pledge disclosure before being treated as clean."
  - type: FLAG-ONE-TIME-ITEM
    reason: "FY26 PBT/PAT and EBIT/EBITDA-based ratios (D1, D2) include a ~INR 17.72 Cr one-time gain from the partial Q5/Q6 building sale (results Q4 FY26 PDF p.15, Note 5). D1 (Net Debt/EBITDA) score is unaffected by stripping it (1.12x vs 1.30x, same band); D2 (Interest Coverage) is actually WORSE ex-gain (0.24x vs 0.90x), so this is not inflating the weak score."
  - type: FLAG-DATA-GAP
    reason: "Moat tests M2 (Cost Advantage), M5 (Scale and Dominance), M9 (Brand) all require peer financial data not provided in this run (only peer concall transcripts available, no margin/market-cap datasets); scored 0 and marked PEER DATA NEEDED, not guessed."
data_years: 5
fy_range: "FY22 to FY26"
blocks: {A: 5, B: 3, C: 10, D: 9, E: 9}
core_score: 36
moat_score: 22
grand_total: 58
moats_confirmed: 5
moat_class: "STRONG"
classification: "AVOID"
deal_breakers:
  - "1: Block A (5) <8 -> max GOOD [triggered, moot vs matrix result]"
  - "2: Block B (3) <8 -> max GOOD [triggered, moot vs matrix result]"
  - "3: median ROCE (-9.42%) <10% -> max AVERAGE [triggered, driven by FY22-FY26 ROCE all near-zero or negative except FY26]"
  - "4: cumulative CFO/PAT (-0.29) <0.50 -> max AVERAGE [triggered, driven by FY22-FY23 negative CFO]"
  - "8: PAT negative in any of last 3 years -> max AVERAGE [triggered, driven by FY24 (-55.75) and FY25 (-33.37); FY26 (+1.90) is the exception]"
history_downgrade: true
data_notes:
  - "Pre-FY22 (FY17-FY21) figures belong to the divested Majesco US software business; excluded from all scoring as a different enterprise."
  - "C2/C4: PAT CAGR marked N/M (negative endpoint); loss-to-profit swing, FY25 to FY26."
  - "FY26 profit includes ~INR 17.72 Cr one-time building-sale gain (results Q4 FY26 PDF p.15, Note 5); flagged wherever it affects an FY26 ratio (see D1/D2)."
  - "screener-Data_Sheet FY26 PBT (-2.61 Cr) does not cleanly reconcile to the audited PDF's continuing-vs-discontinued PBT split (continuing -14.96 Cr + discontinued +16.50 Cr = +1.54 Cr combined); Data_Sheet's own P&L rows are internally self-consistent (Sales+OI-Expenses-Dep-Interest=PBT exactly) and used as primary per task instructions, but the divergence vs the audited segment disclosure is disclosed as a data-quality caveat, not resolved by estimation."
  - "Capital Employed for ROCE (Block A) uses Net Worth + Total Borrowings as a proxy (current/non-current liability split unavailable FY22-FY24); validated within 0.2% of the strict Total Assets - Current Liabilities figure for FY26, diverges up to ~10% for FY25."
  - "M2, M5, M9 (moat block) scored 0 and marked PEER DATA NEEDED; no peer financial statements provided in-run."
block_b_trend: "improving — CFO went from -24.26 Cr (FY22) to +62.93 Cr (FY26); FCF swung from -84.24 Cr (FY24) to +47.08 Cr (FY26), even though every banded B1-B4 sub-score is weak because the bands are calibrated on cumulative figures dominated by the FY22-FY25 loss years."
```
