# STAGE 1: GATE 0 SCORECARD — K.C.P. Sugar and Industries Corporation Ltd (KCPSUGIND)
Run date: 2026-07-21 | Model: Sonnet 5 | Mode: PIPELINE (RE-RUN, text-cache sources)

Data available: 10 years (FY2017 to FY2026). Scoring adapted to 10-year history.

**RE-RUN NOTE:** the prior run of this stage flagged FLAG-DATA-GAP because the
source PDFs could not be opened. That is resolved in this run: every source is
now read from a pre-extracted text cache (screener-Data_Sheet.csv, FY26 Audited
Results, Q3 FY26 Results, CARE rating, and AR FY24-25 pp.1-150). No tooling
failure is re-raised here; only genuine data gaps are marked NOT FOUND (see
Block E and the notes at the end).

**Basis note (read before the numbers):** the screener Data_Sheet CSV figures
reconcile exactly to the CONSOLIDATED FY26 audited results (Revenue, Other
Income, Depreciation, Interest, PBT, PAT for both FY26 and FY25 all tie out —
cross-checks shown inline). KCP has material subsidiaries (EIMCO-K.C.P Ltd —
Engineering, KCP Sugars Agricultural Farms, Quality Engineering) that are
profitable and materially inflate consolidated results relative to the
loss-making standalone sugar entity. CARE's rating (CARE_Rating_2025-10-07.txt)
is explicitly **standalone** ("Analytical approach: Standalone", p.1). Wherever
CARE and the consolidated CSV diverge, both are shown and the anchor used is
stated. Company is sugar + distillery + cogeneration + chemicals (pharma-grade
calcium lactate/CO2) + engineering + black-gram (urad dal) processing +
bio-fertiliser — NOT pharma/CDMO.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Formula note: screener Data_Sheet CSV has no ROCE/ROE row, so both are
**computed**. Capital Employed = Equity Share Capital + Reserves + Total
Borrowings (screener's simplified 3-line balance sheet does not disaggregate
current vs non-current "Other Liabilities" for historical years; only the
FY26 audited note breaks this out in full). Where FY26 full detail is
available (FY26_Audited_Results.txt, consolidated balance sheet), true
"Total Assets − Current Liabilities" is ~6% higher than this proxy (₹624.07cr
vs ₹587.22cr proxy), so the ROCE figures below are mildly *overstated* versus
the strict formula — noted, does not change any band.

EBIT = PBT + Interest (screener-data, all years); EBITDA = EBIT + Depreciation.

| FY | PBT | Interest | EBIT | Cap. Employed (proxy) | ROCE |
|---|---|---|---|---|---|
| 2017 | 73.67 | 11.53 | 85.20 | 421.83 | 20.20% |
| 2018 | -3.00 | 14.79 | 11.79 | 490.44 | 2.40% |
| 2019 | 33.93 | 19.76 | 53.69 | 517.60 | 10.37% |
| 2020 | -10.76 | 21.86 | 11.10 | 554.46 | 2.00% |
| 2021 | 17.12 | 24.36 | 41.48 | 583.65 | 7.11% |
| 2022 | 5.16 | 19.70 | 24.86 | 504.84 | 4.92% |
| 2023 | 70.21 | 14.29 | 84.50 | 556.45 | 15.19% |
| 2024 | 78.87 | 11.19 | 90.06 | 585.35 | 15.39% |
| 2025 | 28.02 | 9.11 | 37.13 | 549.61 | 6.75% |
| 2026 | 15.73 | 7.75 | 23.48 | 587.22 | 4.00% |

(all inputs: screener-data, screener-Data_Sheet.csv rows Sales/PBT/Interest/
Equity Share Capital/Reserves/Borrowings, FY2017-FY2026; FY2026 PBT/Interest
cross-checked and confirmed to tie to FY26_Audited_Results.txt consolidated
P&L, p.3: PBT 1572.51 lakhs = 15.73cr, Interest 774.63 lakhs = 7.75cr)

**A1 Median ROCE = 6.93%** (median of the 10 values above, computed) → **<10% = 0**

**A2 Minimum single-year ROCE = 2.00%** (FY2020, computed) → **<8% = 0**

**A3 Median ROE = 4.86%** (computed; ROE = PAT ÷ average Net Worth, opening+
closing/2; FY2017 uses closing net worth only, opening unavailable, stated
per rule). Yearly ROE: FY17 20.28% (closing basis) / FY18 4.08% / FY19 5.63% /
FY20 −2.14% / FY21 7.73% / FY22 1.14% / FY23 16.91% / FY24 16.30% / FY25 3.24%
/ FY26 2.45% → **<12% = 0**

**A4 ROCE trend, FY2026 (4.00%) vs FY2017 (20.20%) = decline of 16.20pp** →
**>5pp decline = 0**

**BLOCK A TOTAL = 0/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

**B1 Cumulative CFO ÷ Cumulative PAT**
Cumulative CFO (FY17–FY26, screener-data "Cash from Operating Activity") = ₹152.63cr
Cumulative PAT (FY17–FY26, screener-data "Net profit") = ₹255.45cr
Ratio = 0.5977 → **0.50–0.69 = 1**

**B2 / B3 — Capex proxy note:** screener CSV has no discrete "purchase of PPE"
cash-flow line (only an aggregate "Cash from Investing Activity", which
bundles investment purchases/sales in a company that carries a ₹270-290cr
investments book). Capex is therefore **proxied** as ΔNet Block + Depreciation
(standard proxy, stated). FY2017 excluded (no FY2016 Net Block to difference
against). Cross-check: the actual audited standalone FY2026 cash-flow
statement (FY26_Audited_Results.txt p.7) gives "Purchase of Property, Plant
and Equipment" = ₹3.34cr vs the ₹6.26cr proxy for the same year — proxy
overstates capex here but does not flip that year's FCF sign (both negative).

| FY | CFO | Capex (proxy) | FCF |
|---|---|---|---|
| 2018 | -70.18 | 2.23 | -72.41 |
| 2019 | -52.09 | 7.13 | -59.22 |
| 2020 | 26.96 | 1.06 | 25.90 |
| 2021 | 17.44 | 5.65 | 11.79 |
| 2022 | 114.31 | 5.59 | 108.72 |
| 2023 | 7.17 | 13.45 | -6.28 |
| 2024 | 42.46 | 6.89 | 35.57 |
| 2025 | 47.79 | 4.48 | 43.31 |
| 2026 | -30.89 | 6.26 | -37.15 |

**B2 FCF-positive years = 5 of 9 computable years (55.6%)** (FY20, 21, 22, 24,
25 positive; FY18, 19, 23, 26 negative) → **50–74% = 2**

**B3 Cumulative FCF ÷ Cumulative PAT** = ₹50.23cr ÷ ₹198.28cr (PAT for the same
9-yr window, FY18–FY26) = 0.2534 → **0.20–0.39 = 1**

**B4 Change in WC Days, latest vs earliest: NOT FOUND / scored 0.** screener's
simplified balance sheet has no Trade Payables line for historical years
(only the FY26 audited note breaks out Trade Payables), and FY2017 has no
prior-year figure at all against which to base a ΔNetBlock-style estimate.
Payable Days cannot be computed for FY2017, so WC Days (which needs all three
legs: Receivable + Inventory − Payable) cannot be validly compared latest vs
earliest. Per "never estimate," scored 0 rather than substituting a
2-leg-only proxy for the earliest year. → **NOT FOUND, score 0**

**BLOCK B TOTAL = 1+2+1+0 = 4/20**

**block_b_trend: deteriorating** — CFO swung from +₹47.79cr (FY2025) to
**−₹30.89cr (FY2026)** (screener-data), a ₹78.68cr reversal in the latest
audited year, the first negative annual CFO print since FY2019.

---

## BLOCK C: GROWTH (Max 20)

Revenue (screener-data): FY17 442.17 → FY26 259.95 (9-year window)
PAT (screener-data): FY17 57.17 → FY26 11.13

**C1 Revenue CAGR = (259.95/442.17)^(1/9)−1 = −5.74%** (both endpoints
positive, so a valid negative CAGR, not N/M) → **<5% = 0**

**C2 PAT CAGR = (11.13/57.17)^(1/9)−1 = −16.62%** (both endpoints positive;
PAT dipped negative in FY2020, −₹6.26cr, a mid-window loss year that is
masked by the CAGR math since both endpoints are positive — noted, not
scored as a swing per the CAGR edge rule) → **negative = 0**

**C3 Positive YoY revenue years: 3 of 9 (33.3%)** — growth in FY19, FY20, FY24
only; decline in FY18, FY21, FY22, FY23, FY25, FY26 (screener-data) → **<50% = 0**

**C4 PAT CAGR minus Revenue CAGR = −16.62% − (−5.74%) = −10.88pp** → **<−8pp = 0**

**BLOCK C TOTAL = 0/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

"Latest" = FY2026 audited. Reliable FY26 detail exists at both standalone
(clean, from FY26_Audited_Results.txt balance sheet, pp.5-6) and consolidated
(screener-data, reconciled to FY26_Audited_Results.txt pp.3-4) levels. CARE's
rating figures (CARE_Rating_2025-10-07.txt) are standalone, dated FY2025 (its
most recent audited base) — one year older than the FY26 audited cache. Per
task instruction, CARE is used as primary anchor for gearing/coverage/
current-ratio/deal-breaker 6; FY26 self-computed figures are shown as the
current cross-check.

**D1 Net Debt ÷ EBITDA (latest)**
- CARE anchor (standalone, FY2025, CARE_Rating_2025-10-07.txt p.2): "the
  company is net debt negative as on March 31, 2025" — total debt ₹109.82cr
  vs free cash + investments ₹204.08cr → **net cash = 5**
- Mechanical cross-check, strict formula (Net Debt = Borrowings − Cash & Bank
  only, no investment netting), consolidated FY2026 (screener-data):
  Borrowings 127.71 − Cash&Bank 39.35 = ND 88.36cr; EBITDA = EBIT(23.48) +
  Dep(5.95) = 29.43cr → **ND/EBITDA ≈ 3.00x** (right at the >3x boundary)
- Mechanical cross-check, standalone FY2026 (FY26_Audited_Results.txt BS/P&L):
  Total Borrowings 138.21cr − Cash&Bank 30.74cr = ND 107.47cr; EBITDA =
  EBIT(5.55) + Dep(4.71) = 10.26cr → **ND/EBITDA ≈ 10.48x**
- **This is the single largest judgment call in this scorecard.** The gap
  between "net cash" (CARE, netting ~₹250cr of standalone liquid investments/
  mutual funds/equities against debt) and "~10.5x levered" (strict
  Borrowings-minus-Cash-only, standalone) is entirely about whether the
  investment book counts as debt-offsetting quasi-cash. Per task instruction,
  **CARE anchor used: D1 = 5**, flagged here for downstream review. If the
  strict mechanical figure were used instead, D1 = 0 and Block D total =
  9/20 (used only for a classification sensitivity check below — does not
  change the final AVOID classification, see Overrides).

**D2 Interest Coverage EBIT ÷ Interest (latest)**
- CARE anchor (standalone, FY2025, CARE_Rating_2025-10-07.txt p.3, Brief
  Financials table): **Interest coverage = −0.46x** → **<1.5x = 0**
- Cross-check, standalone FY2026 (FY26_Audited_Results.txt): EBIT = PBT(−2.73)
  + Interest(8.28) = 5.55cr; IC = 5.55/8.28 = **0.67x** → also **<1.5x = 0**
- Cross-check, consolidated FY2026 (screener-data): EBIT=23.48, Interest=7.75,
  IC=3.03x (would score 2) — the consolidated figure is flattered by the
  profitable Engineering subsidiary and ₹28.56cr of non-operating other
  income (dividends, FVTPL gains on the investment book); both standalone
  bases (CARE FY25 and self-computed FY26) agree the core sugar entity's
  coverage is weak-to-negative.
- **D2 = 0** (both standalone bases agree; used as anchor over the flattered
  consolidated figure)

**D3 Debt ÷ Equity (latest)**
- CARE anchor (standalone, FY2025): **overall gearing = 0.30x**
  (CARE_Rating_2025-10-07.txt p.2) → **0.1–0.5x = 4**
- Cross-check, standalone FY2026 (computed): Borrowings 138.21 / Net Worth
  361.94 = **0.382x** → same band, **4**
- **D3 = 4**

**D4 Current Ratio (latest)**
- CARE anchor (standalone, FY2025): **2.73x** (up from 1.89x FY2024)
  (CARE_Rating_2025-10-07.txt p.3) → **≥2.0x = 5**
- Cross-check, standalone FY2026 (computed from FY26_Audited_Results.txt BS):
  Current Assets 240.08cr ÷ Current Liabilities 109.49cr = **2.19x** → same
  band, **5**
- **D4 = 5**

**BLOCK D TOTAL = 5+0+4+5 = 14/20** (9/20 under the strict-mechanical D1
alternative; see D1 note — final classification unaffected either way, see
Overrides)

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

**Genuine data gap (not a tooling failure):** no shareholding-pattern (SEBI
SHP) export was supplied and none of the injected sources contain a quarterly
SHP. The Annual_Report.txt cache (standalone notes, pp.1-150) does contain a
promoter-holding note (Note 17.3/17.4, "as at 31.03.2025") which is used as
the best-available substitute for E1, but it is an annual AR snapshot, not
the "latest quarter" the formula calls for, and it has no pledge/encumbrance
column and only one year of prior-year comparison (not three years) — so E2
and E3 remain genuinely NOT FOUND.

**E1 Promoter holding (latest available, AR FY25 Note 17.4, cache p.109,
"as at March 31, 2025"):** Durgamba Investment Pvt Ltd 38.58% + Ms. Irmgard
Velagapudi 1.59% + Ms. Kiran Velagapudi 0.26% + Mr. Vinod R Sethi 0.16% =
**40.59%** (Annual_Report.txt p.109, Note 17.4 — basis: AR annual snapshot,
not quarterly SHP, stated) → **40–49.9% = 3**

**E2 Promoter holding change over 3 years: NOT FOUND.** Only two years are
visible in the supplied AR note (FY2024 and FY2025, both 40.59%, "Nil"
change) — no 3-year lookback is available in the provided sources.
→ **NOT FOUND, score 0**

**E3 Promoter pledge (latest): NOT FOUND.** Note 17.3/17.4 in the AR carries
no encumbrance/pledge column (unlike a full SEBI SHP filing). No pledge
percentage is disclosed anywhere in the supplied text caches.
→ **NOT FOUND, score 0**

**E4 Contingent Liabilities ÷ Net Worth (latest, standalone FY2025,
Annual_Report.txt Note 45, cache pp.115-116):** Outstanding bank guarantees
₹150.49 lakhs + demands raised (share transmission 11.06 + labour cases
59.31 + PF non-enrolment 110.95 + captive power case 578.87 + VAT case 16.61
= ₹776.80 lakhs) = **Total ₹927.29 lakhs = ₹9.27cr** (Annual_Report.txt
pp.115-116, Note 45). Standalone Net Worth FY2025 = Equity 11.34 + Other
Equity 353.93 = ₹365.27cr (FY26_Audited_Results.txt, standalone BS, "previous
period" column). Ratio = 9.27/365.27 = **2.54%** → **<5% = 5**

**BLOCK E TOTAL = 3+0+0+5 = 8/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Peer set named in task (KMSUGAR, RAJSREESUG, UGARSUGAR) has **no data
supplied** beyond this company's own screening CSV — every test requiring
peer comparison is scored 0 and marked "PEER DATA NEEDED" per instructions
(never guess peer figures).

**M1 Pricing Power:** EBITDA margin FY17 21.46% (94.91/442.17, computed) →
FY26 11.32% (29.43/259.95, computed), a −10.1pp decline, against revenue
CAGR −5.74% (no growth). Neither growth-with-margin-expansion nor
growth-with-stable-margin condition is met. → **M1 = 0**

**M2 Cost Advantage vs peer median EBITDA margin: PEER DATA NEEDED.** → **M2 = 0**

**M3 Capital Efficiency:** FAT = Revenue/Net Block, FY2026 = 259.95/99.22 =
**2.62x** (screener-data, computed); ROCE FY2026 = 4.00% (Block A). FAT>2x but
ROCE not >15%; FAT>1x but ROCE not >12% either. → **M3 = 0**

**M4 Customer Stickiness:** 6 of 9 YoY periods were revenue declines
(Block C3) — well past the "3+ decline years" threshold. → **M4 = 0**

**M5 Scale & Dominance: PEER DATA NEEDED** (mcap/margin ranking vs peers
unavailable). → **M5 = 0**

**M6 Technology/R&D:** No R&D/Revenue percentage disclosed in any supplied
source (the Q3FY26 limited-review report notes a "Research & Development
unit" exists within the sugar division, qualitatively, Q3FY26_Results.txt
pp.4-5, but gives no quantified ratio). → **NOT FOUND, M6 = 0**

**M7 Regulatory/License:** Sugar is a licensed, government-price-regulated
industry (SAP/FRP mechanisms — CARE_Rating_2025-10-07.txt p.2) with far more
than 10 listed players nationally (Balrampur Chini, Dwarikesh, Triveni, EID
Parry, Dalmia Bharat Sugar, Bajaj Hindustan, Shree Renuka, KMSUGAR,
RAJSREESUG, UGARSUGAR and others — general industry knowledge, player count
itself not independently verified in the provided sources). Margin also not
stable (−10.1pp move, M1). → **regulated but >10 players = 1**

**M8 Distribution:** No distribution-reach, outlet-count, or revenue-per-
outlet data disclosed in any supplied source; sugar is sold largely via
monthly government release quota, not a distribution-network model.
→ **NOT FOUND, M8 = 0**

**M9 Brand:** GM proxy = (Revenue − Material Cost incl. inventory change) ÷
Revenue, FY2026 = (259.95 − 203.27)/259.95 = **21.81%** (screener-data,
proxy, stated) — but **PEER DATA NEEDED** to compare vs peer median, so
cannot be scored. → **M9 = 0**

**M10 Switching Costs:** Revenue did not grow overall (CAGR −5.74%, 6
decline years) — does not qualify for any "overall growth" band. → **M10 = 0**

**M11 Network Effects (10 years available, ≥6yr test applies):** Latest 3yr
revenue CAGR (FY23→FY26) = −3.53% vs prior 3yr CAGR (FY20→FY23) = −9.65%
(both computed, screener-data) — technically "less negative," but this is
deceleration-of-decline, not real acceleration. Selling & admin as % of
revenue **rose** FY24→FY25 (3.43%→4.54%, screener-data; FY26 selling & admin
cell is blank/NOT FOUND in the screener export, precluding a clean latest-
year check) — directly contradicts the "selling % declining" requirement in
every qualifying band. → **M11 = 0**

**M12 Negative WC / Float:** Cannot be computed across history — same Trade
Payables gap as B4 (screener's simplified balance sheet has no historical
Payables line). FY2026 snapshot only (both bases, for reference, NOT scored
on this alone): standalone WC days ≈ 279 (Receivable 22.3 + Inventory 263.4
− Payable 6.3); consolidated WC days ≈ 283 (Receivable 80.6 + Inventory
218.8 − Payable 16.7) — both strongly positive, nowhere near negative,
consistent with M12=0 even on the one year available. → **NOT FOUND for
trend, M12 = 0**

**BLOCK F TOTAL = 0+0+0+0+0+0+1+0+0+0+0+0 = 1/60**

Moat profile:
```
M1  Pricing Power       [          ] 0/5
M2  Cost Advantage      [          ] 0/5  PEER DATA NEEDED
M3  Capital Efficiency  [          ] 0/5
M4  Customer Stickiness [          ] 0/5
M5  Scale & Dominance   [          ] 0/5  PEER DATA NEEDED
M6  Technology / R&D    [          ] 0/5
M7  Regulatory/License  [==        ] 1/5
M8  Distribution        [          ] 0/5
M9  Brand               [          ] 0/5  PEER DATA NEEDED
M10 Switching Costs     [          ] 0/5
M11 Network Effects     [          ] 0/5
M12 Negative WC / Float [          ] 0/5
```

Moats "present" (score ≥3): **none**. **Moat classification: 0 present = NONE**

---

## SCORECARD SUMMARY

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 0 | 20 |
| B — Cash Generation Quality | 4 | 20 |
| C — Growth | 0 | 20 |
| D — Balance Sheet Strength | 14 | 20 |
| E — Shareholder Alignment | 8 | 20 |
| **CORE SCORE (A-E)** | **26** | **100** |
| F — Quantitative Moat | 1 | 60 |
| **GRAND TOTAL** | **27** | **160** |

**Strongest block: D (Balance Sheet Strength), 14/20** — driven by CARE's
"net-cash"/low-gearing standalone characterization; note this is
anchor-dependent (see D1 discussion — falls to 9/20 under a strict mechanical
Net Debt formula).

**Weakest blocks: A (Return on Capital) and C (Growth), both 0/20** — a
genuine, multi-year structural down-cycle (declining cane availability and
recovery rate in the Krishna belt, per CARE's own rating narrative), not a
data-availability or tooling artifact.

**Data confidence: 10 years = "full"** (no history-based classification
downgrade). `history_downgrade: false`

---

## DEAL-BREAKER OVERRIDES

1. Block A (0) < 8 → cap: max GOOD — **triggered**
2. Block B (4) < 8 → cap: max GOOD — **triggered**
3. Median ROCE (6.93%) < 10% → cap: max AVERAGE — **triggered**
4. Cumulative CFO/PAT (0.5977) < 0.50 → not triggered
5. Pledge > 15% → **cannot evaluate, E3 NOT FOUND** — not asserted as
   triggered (no evidence of breach; genuine data gap, not a pass)
6. ND/EBITDA >3x AND IC <3x → **basis-dependent.** Under the CARE anchor
   (net cash, D1=5) this does NOT trigger (ND/EBITDA condition fails).
   Under the strict mechanical standalone figures (ND/EBITDA≈10.5x AND
   IC≈0.67x) it WOULD trigger → AVOID. Flagged for downstream review; does
   not change the final tier either way (see below).
7. Revenue declined in majority of years (6 of 9 YoY) → cap: max AVERAGE
   — **triggered**
8. PAT negative in any of last 3 years (FY24 +66.16, FY25 +14.39, FY26
   +11.13, all positive) → not triggered
9. History < 3 years → not triggered (10 years available)

None of these caps are more permissive than the base classification below,
so they do not alter the outcome; all are recorded per instruction.

---

## CLASSIFICATION

Core score = 26 (< 40) → **Core <40 = AVOID**, per the classification
matrix, irrespective of moat class (moat class is NONE regardless). This
holds under both the CARE-anchored Block D (core 26) and the strict-
mechanical alternative (core 21) — the classification is AVOID either way.

## CLASSIFICATION: AVOID

---

## DECISION LINE

KCPSUGIND scores AVOID on Gate 0 mechanics: zero-scoring Return on Capital
and Growth blocks reflect a real, multi-year structural down-cycle in the
standalone sugar business (declining cane availability/recovery in the
Krishna delta command area, per CARE), only partially offset by a profitable
Engineering subsidiary (EIMCO-K.C.P) and a large non-operating investment
book that flatters consolidated numbers but does not change the core
operating picture. No moat signature (0 of 12 tests confirmed at score ≥3,
1/60 points total). Balance-sheet strength (14/20, driven by CARE's
standalone "net cash"/low-gearing view) is the only bright spot, and even
that is sensitive to whether the ₹250-270cr investment portfolio is treated
as debt-offsetting quasi-cash — a judgment call this stage flags for the
operator rather than resolving unilaterally. Historical depressors (cyclical
sugar down-cycle, FY2020 loss year, FY2026 CFO reversal to −₹30.89cr) are
named, not a data gap.

---
## DATA GAPS AND NOTES SUMMARY (for input_gaps / data_notes)

- Shareholding-pattern export not supplied; E1 uses AR FY25 annual note (not
  quarterly SHP) as best-available substitute; E2 (3yr promoter change) and
  E3 (pledge %) genuinely NOT FOUND.
- Peer data (KMSUGAR/RAJSREESUG/UGARSUGAR) not supplied beyond this
  company's own screening CSV; M2, M5, M9 scored 0 / PEER DATA NEEDED.
- screener Data_Sheet CSV's simplified 3-line balance sheet (Equity/
  Reserves/Borrowings/Other Liabilities) does not disaggregate current vs
  non-current liabilities, nor break out Trade Payables, for historical
  years. This affects: (a) ROCE proxy in Block A (mildly overstates ROCE vs
  strict formula, doesn't change bands), (b) B4 WC Days trend (NOT FOUND),
  (c) M12 WC Days trend (NOT FOUND, FY2026 snapshot only, both positive
  ~280 days).
- screener FY2026 P&L columns for Power & Fuel, Other Mfr. Exp, and Selling
  and admin are blank in the export (likely folded into the year's
  unusually large "Other Expenses" 43.63cr figure, or not yet tagged); did
  not affect EBIT/EBITDA computation (uses PBT+Interest+Depreciation, all
  of which are populated for FY26).
- AR pp.151-275 are scanned images and not in the text cache; any figure
  that would only live there is NOT AVAILABLE (AR pp.151-275 scanned).
- PAT dipped to a loss in FY2020 (−₹6.26cr) mid-window despite positive
  endpoints (FY2017, FY2026); this is not flagged by the CAGR edge rule
  (which only fires on negative/zero endpoints) but is noted as it obscures
  real volatility.
- CARE's rating base (FY2025, standalone) is one year older than the FY26
  audited cache used elsewhere; where both are available they are shown
  side by side.

---

```yaml
stage: B01-gate0
company: "KCPSUGIND"
run_date: "2026-07-21"
model: claude-sonnet-5
status: complete
input_gaps:
  - "shareholding-pattern (SEBI SHP) export not supplied; E1 uses AR FY25 annual promoter-holding note as substitute; E2 (3yr promoter change) and E3 (pledge %) NOT FOUND"
  - "peer data (KMSUGAR/RAJSREESUG/UGARSUGAR) not supplied beyond this company's own screening CSV; M2/M5/M9 PEER DATA NEEDED"
  - "screener Data_Sheet CSV simplified balance sheet lacks historical Trade Payables line and current/non-current split; B4 and M12 WC-days trend NOT FOUND (FY26 snapshot only)"
  - "AR pp.151-275 scanned/not in text cache; any figure only there is NOT AVAILABLE"
flags:
  - {type: FLAG-GATE0, reason: "Classification AVOID; Blocks A and C both 0/20 driven by a genuine multi-year sugar down-cycle (declining cane availability/recovery, CARE_Rating p.2), not a data or tooling gap. Zero confirmed moats (1/60)."}
  - {type: FLAG-DATA-JUDGMENT, reason: "D1 (Net Debt/EBITDA) is anchor-dependent: CARE (standalone, FY25) frames the company as net-debt-negative by netting ~250cr of liquid investments against debt (D1=5); the strict mechanical Borrowings-minus-Cash-only formula gives ~10.5x standalone / ~3.0x consolidated (D1=0). CARE anchor used per instruction; flagged for operator review since it swings Block D by 5 points (does not change final AVOID classification)."}
data_years: 10
fy_range: "FY2017 to FY2026"
blocks: {A: 0, B: 4, C: 0, D: 14, E: 8}
core_score: 26
moat_score: 1
grand_total: 27
moats_confirmed: 0
moat_class: "NONE"
classification: "AVOID"
deal_breakers:
  - "DB1: Block A 0/20 <8 (cap: max GOOD) - triggered, superseded by AVOID"
  - "DB2: Block B 4/20 <8 (cap: max GOOD) - triggered, superseded by AVOID"
  - "DB3: median ROCE 6.93% <10% (cap: max AVERAGE) - triggered, superseded by AVOID"
  - "DB6: ND/EBITDA vs IC<3x - basis-dependent (see FLAG-DATA-JUDGMENT); does not trigger under CARE anchor, would trigger under strict mechanical standalone figures"
  - "DB7: revenue declined 6 of 9 YoY years, majority (cap: max AVERAGE) - triggered, superseded by AVOID"
history_downgrade: false
data_notes:
  - "PAT dipped to loss in FY2020 (-6.26cr) mid-window despite positive endpoints FY2017/FY2026; CAGR edge rule does not fire (endpoints positive) but volatility is real"
  - "ROCE computed via Capital Employed proxy = Equity+Reserves+Borrowings (screener simplified BS lacks current/non-current liability split for history); ~6% understates true Capital Employed at FY26 where full detail exists, so reported ROCE is mildly overstated vs strict formula - does not change any score band"
  - "FCF capex proxied as delta-NetBlock+Depreciation (screener CSV lacks a discrete PPE-purchase cash-flow line); cross-checked against actual FY26 standalone capex (3.34cr) which is lower than the proxy (6.26cr) but does not flip any year's FCF sign"
  - "GM proxy for M9 = (Revenue-Material Cost incl. inventory change)/Revenue = 21.81% FY2026, computed but unscored - PEER DATA NEEDED"
  - "consolidated FY26 figures reconcile exactly to screener-data (Revenue, Other Income, Depreciation, Interest, PBT, PAT for FY25 and FY26 all tie out) confirming the CSV spine is CONSOLIDATED, not standalone"
block_b_trend: "deteriorating - CFO swung from +47.79cr (FY2025) to -30.89cr (FY2026), screener-data"
```
