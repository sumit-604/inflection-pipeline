# STAGE 1 — GATE 0 QUANTITATIVE SCORECARD
## Fratelli Vineyards Ltd (FRATELLI) | Run date 2026-09-07

Data available: 8 years, non-contiguous (FY2017 to FY2021, then FY2024 to
FY2026; FY2022 and FY2023 are absent from every provided source —
screener-Data_Sheet.csv, the two annual reports, and the six results
filings). Scoring adapted to this 8-year, gapped history, with a further,
more important break inside it: **the business itself changed** between
FY2021 and FY2024. Everything below is scored mechanically per the
formulas, but the Block C growth math and the Block A/B interpretation
must be read through that break — see LOAD-BEARING FACT 1 below before
reading any score.

---

## LOAD-BEARING FACT 1 — THE REVENUE BASIS (verified)

- FY2017–FY2021 (screener-data): Rs 416.28 cr, 464.07, 487.59, 294.67,
  244.91 cr. This is **Tinna Trade Ltd, an agri-commodity trading
  business**. It has no relationship to wine. (AR FY25, p.42/Note 3
  "Change in nature of business": "Historically, the company was engaged
  in the domain of Trading Agriculture Commodities... Consequently, the
  Company has formally exited the agri-commodity trading business and
  transitioned its core focus to the wine industry.")
- The wine subsidiary, Fratelli Wines Private Limited, became a
  wholly-owned subsidiary on 22-Apr-2024 via share swap (AR FY25, Note 43,
  p.192-193; AR FY26, Note 39 equivalent). Because this was a
  **common-control combination**, Ind AS 103 Appendix C required the
  Company to **restate FY2024 comparatives as if the combination had
  occurred from 1-Apr-2023** (AR FY25, Note 43(v), p.193: "management has
  prepared the consolidated financial statements with effect from April 1,
  2023, to ensure comparability"). So the screener's FY2024 Rs 421.35 cr
  is **not** pure legacy agri-trading — it is restated-consolidated
  (wine, full year, pooled + legacy agri-trading, full year, before exit).
- FY2025 (Rs 276.25 cr, screener-data) is a genuine transition year: wine
  for the full year plus a shrinking agri-trading tail as the exit
  completed.
- FY2026 (Rs 181.29 cr, screener-data) is confirmed **wine-only**: the
  AOC-1 subsidiary return for Fratelli Wines Pvt Ltd shows Turnover Rs
  18,120.04 lakh = Rs 181.20 cr (AR FY26, p.50, Annexure-I Form AOC-1,
  item 9) against Rs 181.29 cr consolidated — the parent's own standalone
  "Revenue from operations" collapsed to Rs 67.83 lakh = Rs 0.68 cr (AR
  FY26, p.90, Standalone P&L line 20). The wine subsidiary is now
  essentially the whole company.
- The task brief's cited "wine business Rs 215.6 cr" FY24 figure could
  **not** be independently located in the provided corpus text. The
  nearest verified analogs are the AOC-1 standalone turnover figures for
  Fratelli Wines Pvt Ltd itself: Rs 178.44 cr for FY25 (AR FY25, p.49,
  Annexure-I item 9) and Rs 181.20 cr for FY26 (AR FY26, p.50, item 9). No
  equivalent FY24 AOC-1 return for the subsidiary appears in either AR
  extract (AOC-1 only reports the current year). Flagged, not assumed.

**Conclusion used for scoring below:** FY2017–FY2021 is a different
company (agri trading) and is excluded from Block C growth scoring.
FY2024–FY2026 (3 data points, 2 year-on-year transitions) is the only
internally comparable window for the current (wine) business, and even
that window carries transition-year contamination in FY2024–FY2025.
`history_downgrade: true`.

---

## LOAD-BEARING FACT 2 — GROSS MARGIN AND THE A&P LINE (verified)

- FY2026: Raw Material Cost Rs 54.98 cr on Sales Rs 181.29 cr
  (screener-data) → material-cost-only gross margin = (181.29-54.98) /
  181.29 = **69.7%** — this is the "70%" base the 77-80% management claim
  likely anchors to, and it is **before** the Rs 15.26 cr "Change in
  Inventory" adjustment (screener-data) is folded in. Adding that in
  (54.98+15.26=70.24 cr effective material cost) drops the ratio to
  61.3%.
- FY2025: Raw Material Cost Rs 126.39 cr on Sales Rs 276.25 cr
  (screener-data) → material-cost-only gross margin = **54.2%**, matching
  the task brief's "54%" figure exactly, before any inventory adjustment.
- The 77-80% claim does not reconcile to either year's P&L on a
  materials-only basis, and reconciles even less once inventory movement
  is included. NOT FOUND: a management bridge from reported material cost
  to the claimed 77-80% figure, in any of the four results filings or two
  ARs reviewed.
- The expense-line reclassification is confirmed directly in
  screener-data: "Selling and admin" carries Rs 74.10 cr (FY24), Rs 77.12
  cr (FY25), **blank** (FY26); "Other Expenses" carries Rs 4.67 cr (FY24),
  Rs 7.53 cr (FY25), **Rs 114.14 cr (FY26)**. The FY26 "Other Expenses"
  jump of Rs 106.6 cr against FY25 is arithmetically close to the FY25
  "Selling and admin" line disappearing (Rs 77.12 cr) plus other cost
  growth — consistent with a line-item reclassification, not a like-for-
  like cost explosion. NOT FOUND: a named FY26 advertising & promotion
  rupee figure in any provided filing; "Other Expenses" is not broken out
  further in the extracted text.

---

## LOAD-BEARING FACT 4 — RECEIVABLES (verified, computed)

Receivable Days = Trade Receivables ÷ Sales × 365 (Sales basis; COGS not
used — see B4 methodology note).
- FY2024: Receivables Rs 134.64 cr (screener-data) ÷ Sales Rs 421.35 cr ×
  365 = **116.6 days**
- FY2025: Rs 109.93 cr ÷ Rs 276.25 cr × 365 = **145.3 days**
- FY2026: Rs 105.11 cr ÷ Rs 181.29 cr × 365 = **211.6 days** — matches the
  task brief's "~212 days" almost exactly.
Receivable days nearly doubled across the only comparable window
available, even before inventory and payables are folded into the WC-days
metric (see B4).

---

# BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 0/20

Formula: ROCE = EBIT ÷ (Total Assets − Current Liabilities); EBIT =
PBT − Other Income + Interest (computed, screener does not carry its own
ROCE/ROE in this Data Sheet). Current Liabilities used exact figures from
the AR consolidated balance sheets for FY2024–FY2026 (Notes to Financials);
for FY2017–FY2021, "Other Liabilities" (screener-data) is used as the only
available proxy for Current Liabilities — the condensed screener sheet
does not split current/non-current for those years. Flagged as an
approximation.

| Year | EBIT (cr) | Capital Employed (cr) | ROCE | Source |
|---|---|---|---|---|
| FY17 | 8.45 | 97.27 | 8.7% | screener-data, computed |
| FY18 | 3.39 | 101.83 | 3.3% | screener-data, computed |
| FY19 | 6.52 | 55.50 | 11.8% | screener-data, computed |
| FY20 | -1.50 | 64.45 | -2.3% | screener-data, computed |
| FY21 | -1.07 | 52.54 | -2.0% | screener-data, computed |
| FY24 | 22.80 | 157.55 | 14.5% | screener-data + AR FY25 p.145 (Note, Total current liab Rs 190.11 cr), computed |
| FY25 | -13.12 | 207.36 | -6.3% | screener-data + AR FY26 p.145 (Total current liab Rs 126.58 cr), computed |
| FY26 | -16.63 | 185.90 | -9.0% | screener-data + AR FY26 p.145 (Total current liab Rs 160.64 cr), computed |

**A1 Median ROCE:** median of all 8 years = 0.6% (sorted midpoint of
-2.04% and 3.33%). Wine-era-only median (FY24-26, 3 pts) = -6.3%. Both
<10%. **Score: 0**

**A2 Minimum single-year ROCE:** -9.0% (FY26). <8%. **Score: 0**

**A3 Median ROE:** ROE = PAT ÷ avg Net Worth (opening+closing)/2; FY17 and
FY24 use closing NW only (no valid opening figure — FY24's predecessor
year, FY23, is not in any provided source). PAT and Net Worth from
screener-data.
FY17: 14.5% | FY18: -1.1% | FY19: 5.7% | FY20: -10.5% | FY21: -6.0% |
FY24: -0.7% | FY25: -15.7% | FY26: -17.1%.
Median (all 8) = -3.5%. Wine-era-only median (FY24-26) = -15.7%. Both
<12%. **Score: 0**

**A4 ROCE trend, latest (FY26, -9.0%) vs earliest (FY17, 8.7%):** decline
of 17.6pp, >5pp band. (Using FY24 as the nearer, less basis-broken anchor
instead: 14.5% → -9.0% = 23.4pp decline — same outcome either way.)
**Score: 0**

---

# BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 0/20

CFO and PAT from screener-data (cumulative, all 8 years, unless noted).
Capex (purchase of PP&E + intangibles, ex-acquisitions) is only available
in the corpus for FY2024–FY2026, from the AR consolidated cash flow
statements; FY2017–FY2021 capex breakdown is **NOT FOUND** in any provided
source (only net investing cash flow is in screener-data), so FCF metrics
(B2, B3) are scored on the FY2024–FY2026 window only.

| Year | CFO (cr) | Capex (cr) | FCF (cr) | Source |
|---|---|---|---|---|
| FY24 | 7.18 | 18.84 | -11.66 | screener-data; AR FY25 p.147, Consolidated CF stmt, "Payments for purchase of PP&E" Rs 1,883.70 lakh |
| FY25 | -7.00 | 40.74 | -47.74 | screener-data; AR FY26 p.145 comparative col, "Payments for purchase of PP&E" Rs 4,073.82 lakh |
| FY26 | 5.00 | 12.34 | -7.34 | screener-data; AR FY26 p.145, PP&E Rs 1,231.00 lakh + intangibles Rs 2.81 lakh |

Note: the FY25 AR's own extracted text shows several cash-flow signs
without parentheses in the FY25 column (an OCR/extraction artifact);
FY25 CFO sign was cross-checked against both screener-data (-7.0 cr) and
the FY26 AR's comparative column (Rs (700.08) lakh, negative,
p.145) — both agree; used as the anchor.

**B1 Cumulative CFO ÷ Cumulative PAT (all 8 years):** Cumulative CFO =
Rs 54.41 cr (screener-data, sum). Cumulative PAT = Rs -38.18 cr
(screener-data, sum) — **negative**. The ratio (54.41/-38.18 = -1.43) is
not meaningful in the intended direction (positive cash vs negative
profit is not "cash exceeding profit" in any useful sense); scored per the
worst band since the profit base itself is negative across the period.
**Score: 0**

**B2 FCF-positive years as proportion (FY24-26 window, the only years
with capex data):** 0 of 3 years FCF-positive. <50%. **Score: 0**

**B3 Cumulative FCF ÷ Cumulative PAT (FY24-26 window):** Cumulative FCF =
Rs -66.74 cr. Cumulative PAT (same window) = Rs -39.04 cr. Mechanically
the ratio is +1.71 (two negatives), which would map to the top band under
a literal reading of the formula — **flagged as a scoring artifact, not
applied.** Substance: FCF burn (Rs -66.74 cr) is *larger* than the
accounting loss (Rs -39.04 cr), i.e. cash quality is worse than earnings
quality, the opposite of what this metric is meant to reward. Scored 0,
consistent with the B1 treatment of a negative PAT base. **Score: 0**

**B4 Change in WC Days, latest vs earliest available (FY24 → FY26 — the
only years with a Trade Payables figure in the corpus):**
WC Days = Receivable Days + Inventory Days − Payable Days (Sales basis
throughout; COGS not used as a single clean line exists only as Raw
Material Cost, which excludes several other manufacturing cost lines, so
Sales basis was used for internal consistency across all three
components, per the formula's own basis rule).

| Year | Receivable Days | Inventory Days | Payable Days | WC Days | Source |
|---|---|---|---|---|---|
| FY24 | 116.6 | 80.2 | 47.7 | 149.1 | screener-data (receivables/inventory); AR FY25 p.146 Note 19 comparative, Trade Payables Rs 5,510.45 lakh |
| FY25 | 145.3 | 109.0 | 29.6 | 224.7 | screener-data; AR FY26 p.144 Note 19 comparative, Trade Payables Rs 2,241.37 lakh |
| FY26 | 211.6 | 191.5 | 54.5 | 348.6 | screener-data; AR FY26 p.144 Note 19, Trade Payables Rs 2,707.59 lakh |

WC Days rose from 149.1 to 348.6, +199.5 days. >15-day increase band.
**Score: 0**

**Block B total: 0/20.** `block_b_trend: "deteriorating — cumulative FCF
(Rs -66.7 cr, FY24-26) burns faster than the cumulative accounting loss
(Rs -39.0 cr) over the same window, and WC days rose from 149 to 349"`

---

# BLOCK C: GROWTH (Max 20) — Score: 0/20

Scored on the FY2024–FY2026 window only (the only internally comparable
window for the current wine business — see LOAD-BEARING FACT 1). A
CAGR spanning the FY2021→FY2024 basis break would be meaningless and is
not used for scoring; it is shown once below for transparency only, then
discarded.

Memo only, NOT scored: FY2017 (Rs 416.28 cr, agri trading) to FY2026
(Rs 181.29 cr, wine) CAGR = -8.8% over 9 years. **N/M for scoring — basis
break, per LOAD-BEARING FACT 1.**

**C1 Revenue CAGR (FY24 Rs 421.35 cr → FY26 Rs 181.29 cr, 2 years):**
(181.29/421.35)^(1/2) − 1 = **-34.4%**. Negative, both endpoints positive
(not a N/M case), falls in "<5%" band. Note: this decline is driven
substantially by the deliberate exit of the legacy agri-trading revenue
embedded in the FY24 restated base, not solely by wine-business
contraction — see LOAD-BEARING FACT 1. **Score: 0**

**C2 PAT CAGR (FY24 Rs -0.15 cr → FY26 Rs -24.91 cr):** both endpoints
negative. **N/M (negative endpoint). Score: 0**

**C3 Positive YoY revenue years proportion (FY24-26 window, 2
transitions):** FY25/FY24 negative, FY26/FY25 negative. 0 of 2 positive.
<50%. **Score: 0**

**C4 PAT CAGR minus Revenue CAGR:** PAT CAGR is N/M. Per the CAGR edge
rule, **C4 = 0** automatically.

**Block C total: 0/20.**

---

# BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 5/20

All FY26 (latest), consolidated, sourced to the AR's own Note 39/33
Capital Management disclosure where available (preferred over a derived
figure since the company states its own "Total debts" and "Net Debt"
directly).

**D1 Net Debt ÷ EBITDA:** Net Debt FY26 = Rs 119.66 cr (AR FY26, p.145,
Capital Management note, "Net Debt (A) 11,965.79" lakh). EBITDA FY26 =
EBIT (Rs -16.63 cr, computed) + Depreciation (Rs 8.84 cr, screener-data)
= **Rs -7.79 cr — negative.** Cross-checked via quarterly Operating
Profit sum (screener-data, Q1-Q4 FY26: -2.97+0.79-0.59-5.0 = -7.77 cr,
consistent). Ratio undefined/worse than any finite multiple with positive
net debt against negative operating earnings. **Score: 0**

**D2 Interest Coverage (EBIT ÷ Interest):** -16.63 / 13.26 (screener-data)
= **-1.25x**. <1.5x band. **Score: 0**

**D3 Debt ÷ Equity:** Total debts (borrowings only, ex-lease, per the
company's own Capital Management definition) Rs 119.74 cr (AR FY26,
p.145) ÷ Total Equity Rs 135.96 cr (screener-data: Rs 43.47 cr + Rs 92.49
cr) = **0.88x**. 0.5-1.0x band. **Score: 3**

**D4 Current Ratio:** Total Current Assets Rs 219.36 cr ÷ Total Current
Liabilities Rs 160.64 cr (AR FY26, p.144, Consolidated Balance Sheet) =
**1.37x**. 1.2-1.49x band. **Score: 2**

**Block D total: 5/20.**

---

# BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 5/20

**E1 Promoter holding (latest available, 31-Mar-2026):** 57.19% (AR FY26,
p.68, Category-wise shareholding table, "Total Promoter & Promoter Group
(A) 24,860,106 shares, 57.19%"). Note: two inter-se gift transfers among
promoters on 14-Aug-2026 and 21-Aug-2026 (per COMPANY MEMORY, not an
anchored source in this run's corpus) postdate the AR and are not
reflected here; they redistribute holdings within the promoter group and
are not evidenced in this run to change the aggregate promoter %.
50-59.9% band. **Score: 4**

**E2 Promoter holding change over 3 years:** **NOT FOUND.** Only two
data points exist in the corpus: 56.90% (31-Mar-2025, AR FY25 p.68) and
57.19% (31-Mar-2026, AR FY26 p.68) — a 1-year, +0.29pp change, not the
specified 3-year window. FY2023 (or any pre-2025 promoter %) is not in
any provided source. **Score: 0**

**E3 Promoter pledge (latest):** **NOT FOUND.** No promoter-share pledge
or encumbrance disclosure located in either AR's shareholding tables
(only fixed-deposit pledges against bank borrowings were found, AR FY25
p.116/p.164 — not a promoter share pledge). inputs/shareholding/ is empty
per the carried-forward gap; the granular SEBI pledge-column table
typically lives in the quarterly SHP filing, not in the AR text extracted
here. **Score: 0**

**E4 Contingent Liabilities ÷ Net Worth (latest, consolidated):**
Contingent Liabilities Rs 37.88 cr (AR FY26, p.150, Note 39 "Contingencies
and Commitments," Group total Rs 3,787.90 lakh) ÷ Total Equity Rs 135.96
cr (screener-data) = **27.9%**. 15-30% band. **Score: 1**

**Block E total: 5/20.**

---

# BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 0/60

| Test | Score | Basis |
|---|---|---|
| M1 Pricing Power | 0 | EBITDA margin FY24 6.98% → FY26 -4.30%, -11.3pp decline, alongside revenue decline (not growth). Fails all non-zero bands. |
| M2 Cost Advantage vs peer | 0 | PEER DATA NEEDED — no peer (SULA/other) financials in this run's corpus. |
| M3 Capital Efficiency | 0 | FAT (FY26) = Rev 181.29 / Net Block 96.41 = 1.88x, but ROCE -9.0% fails even the lowest (>12%) band. |
| M4 Customer Stickiness | 0 | 2 of 2 comparable years declined; CAGR negative, not positive — fails the "2 decline years, CAGR positive=1" band. |
| M5 Scale & Dominance | 0 | PEER DATA NEEDED — no peer market-cap/margin ranking data in this run's corpus. |
| M6 Technology/R&D | 0 | No R&D disclosure found in any provided filing. |
| M7 Regulatory/License | 0 | PEER DATA NEEDED — a defensible count of listed players in the regulated Indian wine/alco-bev segment is not sourced from any document in this run's corpus; not guessed. |
| M8 Distribution | 0 | Reach IS quantified and expanding: "available across more than 31,000 touch points" and Shotgun "approx. 18 States and around 9,000 outlets... including approximately 2,000 outlets added during FY 2025-26" (AR FY26, p.11-12). But the test's growth conditions (rev CAGR ≥15%, or stable/growing revenue-per-outlet) fail given the -34% FY26 revenue decline; scored per strict rule, flagged as likely understating a real, quantified network. |
| M9 Brand | 0 | PEER DATA NEEDED for the peer-median gross-margin comparison the test requires. Own GM proxy (Revenue − Material Cost)/Revenue = 69.7% (FY26) is computable but has no peer benchmark in this corpus. |
| M10 Switching Costs | 0 | Revenue declined both comparable years; receivable days rose 95 days (116.6→211.6) over the window, not "stable." |
| M11 Network Effects | 0 | Fewer than 6 years available for the two-window test; scored conservatively on the overall trend as instructed. Revenue CAGR negative; S&A/Other-Expenses-to-revenue ratio rose sharply (17.6%→27.9%→62.96%, though FY26 includes the reclassification noted in LOAD-BEARING FACT 2) — fails the "growth>15%" precondition regardless. |
| M12 Negative WC/Float | 0 | WC Days 149→225→349, all far above the 45-day ceiling for any non-zero band. |

**Moats present (score ≥3): 0. Moat classification: NONE.**

---

# CLASSIFICATION

**Core score = A(0) + B(0) + C(0) + D(5) + E(5) = 10/100**
**Moat score = 0/60. Moat class: NONE.**
**Grand total (core + moat) = 10/160**

Data confidence: 8 raw years present falls in the "7-9, moderate" band by
count alone, but the internally comparable history for the CURRENT (wine)
business is only 3 years (FY24-26), which is the "3-4, LIMITED" band —
downgrade one tier. `history_downgrade: true`. Since Core (10) is already
below the 40-point AVOID threshold, the one-tier downgrade does not change
the outcome — the floor is already reached on the raw numbers.

**Classification matrix: Core <40 → AVOID.**

**Deal-breakers fired:**
1. Block A (0) < 8 → cap max GOOD
2. Block B (0) < 8 → cap max GOOD
3. Median ROCE (0.6% all-years / -6.3% wine-era) < 10% → cap max AVERAGE
4. Cumulative CFO/PAT ratio negative (PAT base negative) → cap max AVERAGE
6. Interest Coverage -1.25x < 3x, and Net Debt Rs 119.66 cr against
   negative EBITDA (undefined, economically worse than any finite
   multiple) → cap AVOID
7. Revenue declined in the majority of computable year-on-year
   transitions (4 of 6 across the full 8-year set; both of the 2
   comparable wine-era transitions) → cap max AVERAGE
8. PAT negative in all 3 of the last 3 available years (FY24, FY25,
   FY26) → cap max AVERAGE

Deal-breaker 5 (pledge >15%) could not be evaluated — **NOT FOUND** (see
E3). Deal-breaker 9 (history <3 years) does not fire — exactly 3
comparable years exist.

None of the caps can lift a Core-driven AVOID; the final classification is
**AVOID**, with deal-breaker 6 independently corroborating the floor.

---

# STRONGEST / WEAKEST BLOCK

**Weakest:** Blocks A, B and C are tied at 0/20 each — return on capital,
cash generation, and growth are all scored at the floor for the current
business.

**Strongest:** Block E (5/20) — driven entirely by a still-majority
(57.19%) promoter holding; two of its four sub-tests (E2, E3) are
NOT FOUND rather than genuinely scored, so even this "strongest" block is
weak and partly unverifiable in this run's corpus.

---

# DECISION LINE

Gate 0 classification: **AVOID**, on numbers that mechanically span a
business that exited agri-commodity trading and pivoted to wine between
FY2024 and FY2026. Every growth, return, and cash metric for the
comparable (wine-era) window is negative or at the scoring floor: revenue
fell 34% two years running, ROCE and ROE are negative in FY25 and FY26,
free cash flow is negative and worsening in all three comparable years,
and receivable days nearly doubled to 212. This is a documented,
in-flight business-model transition, not necessarily a like-for-like
"AVOID" business — the pipeline's own deal-breaker note allows downstream
position sizing to reconsider a mechanical AVOID for "documented post-IPO
rebase / legacy cleanup" cases. FRATELLI is such a case on its face (see
LOAD-BEARING FACT 1), but Gate 0's job is to report the number, not
adjust it: **AVOID stands as computed, flagged for Halt 1 review of
whether the transition thesis (Vision 2030, PAT breakeven guided for
FY27) can be evaluated on its own terms downstream.**
