# GATE 0 QUANTITATIVE SCORECARD — Forbes Precision Tools & Machine Parts Ltd (TOTEM)

Run: runs/totem-2026-09-09/ | Stage 1 (B01-gate0) | Model: claude-sonnet-5 | 2026-09-09

Data available: 3 years (FY2023-24 to FY2025-26). Scoring adapted to 3-year
history. The company was incorporated in 2022; the Scheme of Arrangement
demerging it out of Forbes & Company Ltd took effect 01-Mar-2024; shares
listed on BSE 11-Jun-2024. FY23 is a pre-demerger shell stub (Total assets
Rs 0.05 cr, PBT Rs -0.01 lakh per screener-Data_Sheet.csv) and is NOT used
as a data year. Longer restated history exists only inside the Information
Memorandum (pre-demerger, different entity structure) and is not used here
per the prompt's basis-hierarchy rule. FY2023-24, FY2024-25 and FY2025-26
are the three audited standalone years used throughout.

Primary sources cross-verified against each other in every case: screener
CSV export (runs/totem-2026-09-09/inputs/screening/screener-Data_Sheet.csv)
against the audited FY26 results (results__FY26_Audited_Results_31Mar2026.txt)
and the FY24/FY25/FY26 Annual Reports. Every figure below matched on
cross-check unless noted.

---

## LOAD-BEARING FACTS — VERIFICATION FIRST

**LBF-1, Q1 FY27 margin bridge — CONFIRMED, all four legs exact.**
Source: inputs/results/FY27-Q1_Unaudited_Results_30Jun2026.pdf, Statement
of P&L, rendered page-03.png (Q1 FY27 results, p.3), cross-checked against
screener-Data_Sheet.csv Quarters block.
- Revenue: Q1 FY27 Rs 67.55 cr vs Q1 FY26 Rs 52.41 cr, +28.9%.
- OPM (Revenue minus materials, purchases, inventory change, employee cost,
  other expenses; excludes finance cost and D&A): Q1 FY27 = (6755-2348-0-92
  -1245-1522)/6755 = 22.9%. Q1 FY26 = (5241-1782-0-(-116)-1131-1603)/5241 =
  16.05% ≈ 16.1%. Both match the claim exactly.
- Combined material cost (cost of materials consumed + purchases of
  stock-in-trade + change in inventories, i.e. net material cost absorbed):
  Q1 FY27 = 2440/6755 = 36.12% of revenue. Q1 FY26 = 1666/5241 = 31.79%.
  Delta = +4.33pp, matching the claimed "+4.3pp worsening" exactly. This is
  the true reading of "raw-material cost worsened": net material cost as a
  share of revenue rose, even though the reported "Cost of materials
  consumed" line alone (34.8% vs 34.0%) looks nearly flat — the swing sits
  in the inventory-change line, not the purchase price line.
  [INFERENCE: the margin gain is not a raw-material story; it is an
  employee-cost and other-expense compression story riding on volume, with
  material cost (net of inventory absorption) actually a modest drag.]
- Employee cost: Q1 FY27 = 1245/6755 = 18.43% ≈ 18.4%. Q1 FY26 = 1131/5241
  = 21.58% ≈ 21.6%. Matches exactly.
- Other expenses: Q1 FY27 = 1522/6755 = 22.53% ≈ 22.5%. Q1 FY26 = 1603/5241
  = 30.59% ≈ 30.6%. Matches exactly.
- Exceptional items (Net) = NIL in both quarters (line item present, value
  blank/nil in the filing). PBT before and after exceptional items are
  identical for both periods.

**LBF-2, FY26 inventory build — CONFIRMED on absolute rupee figures;
inventory-days and CCC figures NOT reproducible from the prescribed
formula on this run's own data.**
Source: annual-report__Annual_Report_2026.txt, Note 8 Inventories
(AR FY26, p.92): Total inventory Rs 5,642.15 lakh (Rs 56.42 cr) at
31-Mar-2026 vs Rs 3,193.07 lakh (Rs 31.93 cr) at 31-Mar-2025 — matches the
claim (Rs 31.9 cr to Rs 56.4 cr) exactly. Breakdown: raw materials Rs
1,993.71 lakh (up from Rs 738.71 lakh), WIP Rs 1,277.50 lakh (up from
693.91), finished goods Rs 2,210.52 lakh (up from 1,541.74), stores/spares
Rs 160.42 lakh (down from 218.71). CFO: Rs 2,755.29 lakh (Rs 27.55 cr) FY26
vs Rs 5,131.62 lakh (Rs 51.32 cr) FY25 (AR FY26, Cash Flow Statement, p.71)
— matches the claim (Rs 51 cr to Rs 28 cr) exactly.
Using this stage's fixed formula (Inventory Days = Inventory ÷ Revenue ×
365, revenue basis; COGS is not a single explicit P&L line in the filing so
revenue basis is used and stated per the prompt's rule), inventory days
computed here are FY24 61.5, FY25 50.1, FY26 82.0 — a real and material
increase in FY26 but far below the claimed 146 → 255 days. The company's
own AR-disclosed inventory turnover ratio (COGS ÷ average inventory; AR
FY26 p.118) is 1.83x FY26 vs 2.27x FY25, i.e. days-equivalent of ~199.5
vs ~160.8 — also directionally consistent with deterioration but still not
matching 146/255. [DATA NOTE: the LBF-2 "146 to 255 days" and "91 to 152
day CCC" figures cannot be reconstructed from this run's own filed data on
any basis tried (revenue, COGS, average-inventory turnover). Direction is
confirmed (WC days did increase in FY26); the specific magnitude claimed by
the third-party read is not verified and is flagged as unresolved, not
used in scoring.] This stage's own formula-compliant WC Days: FY24 73.8,
FY25 65.2, FY26 78.9 (component days below).

**LBF-3, promoter pledge — CONFIRMED exactly, all three quarters checked.**
Source: shareholding__SHP_30Jun2026.txt (SHP 30-Jun-2026, p.4-5),
shareholding__SHP_31Mar2026.txt (p.4-5), shareholding__SHP_30Jun2025.txt
(p.4-5). Promoter and promoter group hold 38,102,764 shares = 73.85% of
51,594,464 total shares, unchanged across all three filings. Shares
pledged = 35,967,172, all held by Shapoorji Pallonji And Company Private
Limited (the ultimate promoter entity; 35,967,172 of its 35,967,172 shares
= 100% of ITS holding pledged). Pledged shares as % of total promoter
group holding = 35,967,172 / 38,102,764 = 94.4%, identical at Jun-2025,
Mar-2026 and Jun-2026. No shares are subject to Non-Disposal Undertaking or
other encumbrance. No related-party guarantee from the operating company
to the promoter group is disclosed in the FY26 AR related-party note or the
contingent-liabilities note (AR FY26, p.124: only contingency is Rs 16.81
lakh of labour-matter claims, unchanged FY25→FY26; no corporate guarantees
given). This is a promoter (Shapoorji Pallonji & Co.) financing-structure
pledge, not evidence of an operating-company guarantee or exposure, but it
is a stable, near-total pledge of the controlling stake and is treated as
a governance deal-breaker per the scoring rules below.

**LBF-4, FY26 revenue basis and exceptional item — RESOLVED: screener
figure is the audited figure; the alleged exceptional item is not found.**
Source: results__FY26_Audited_Results_31Mar2026.txt (FY26 Audited Results,
p.5), audited Statement of P&L, "Year ended 31.03.2026 (Audited)": Revenue
from operations Rs 25,101 lakh = Rs 251.01 cr, FY25 Rs 23,266 lakh =
Rs 232.66 cr. This is the audited "Revenue from operations" figure and
matches screener-Data_Sheet.csv exactly (251.01, 232.66). Growth =
251.01/232.66 - 1 = 7.89% ≈ 7.9% — the growth rate in the third-party read
is correct even though its Rs 241 cr absolute figure is not traceable to
any audited line in this corpus. "Exceptional items (Net)" is a labelled
line in the audited P&L and is NIL for both FY26 and FY25 (Profit before
exceptional items and tax = Profit before tax for the period in both
years, Rs 3,950 lakh FY26 / Rs 4,088 lakh FY25). A corpus-wide search for
"Labour Code" / "Code on Wages" / "Code on Social Security" across all
three Annual Reports and the FY26 results returns only the standard,
identical boilerplate disclosure in each year ("effective date... yet to
be notified... impact will be assessed... post notification") — no rupee
figure, no exceptional charge, in any year. [DATA NOTE: the claimed
"Rs 5.9 cr pre-tax Labour Codes charge inside FY26 profit" is NOT found in
this run's own filed sources and is treated as unverified / likely
erroneous. Audited FY26 revenue from operations is Rs 251.01 cr, up 7.9%,
with NIL exceptional items.]

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

ROCE and ROE are taken from the company's own AR-disclosed ratio note
(Numerator/Denominator per Ind AS 113 ratio disclosure), not from
screener's live-site figures (the provided screener CSV export contains no
ROCE/ROE columns; only the AR ratio note qualifies as "the source's own
figure" present in this run's data). Source: AR FY25 Financial Risk
Management ratio note (AR FY25, p.100) gives FY24 and FY25; AR FY26 ratio
note (AR FY26, p.118) gives FY25 (cross-check, matches) and FY26.

| Year | ROCE (AR-disclosed) | ROE (AR-disclosed) |
|---|---|---|
| FY24 | 28% | 43% |
| FY25 | 22% | 19% |
| FY26 | 22% | 17% |

FY24's 43% ROE is a base-effect artifact: average shareholders' equity for
FY24 blends the near-zero pre-demerger equity base (FY23 total equity
Rs 0.04 cr) with the post-demerger closing equity of Rs 137.75 cr, so the
denominator is artificially depressed. Flagged, not excluded — the AR
discloses it as the actual ratio and the formula rules require using the
source's own figure.

- **A1 Median ROCE** = median(28, 22, 22) = 22% → 20-24.9% band → **4**
- **A2 Minimum single-year ROCE** = 22% → ≥15% → **5**
- **A3 Median ROE** = median(43, 19, 17) = 19% → 15-19.9% band → **4**
  (flag: FY24's 43% is a demerger base-effect distortion, not organic)
- **A4 ROCE trend, latest (22%) vs earliest (28%)** = decline of 6pp →
  decline >5pp → **0**

**Block A total = 13/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

CFO and capex (Payments for property, plant and equipment, including
investment properties/intangibles/advances — excludes acquisitions) taken
from the audited Cash Flow Statements: AR FY25 (p.58) for FY24 and FY25,
AR FY26 (p.71) for FY25 (cross-check, matches) and FY26.

| Year | CFO (cr) | Capex (cr) | FCF (cr) | PAT (cr) |
|---|---|---|---|---|
| FY24 | 9.46 | 97.26 | -87.80 | 29.71 |
| FY25 | 51.32 | 28.26 | 23.06 | 28.75 |
| FY26 | 27.55 | 18.39 | 9.16 | 28.77 |

FY24's huge capex (Rs 97.26 cr) is the post-demerger capacity build: fixed
assets (Net Block + CWIP) rose from a low post-demerger base; the FY26 AR
narrative and screener figures both describe CNC lines, robotic flute
grinding capacity and a spring-washer furnace commissioned across FY24-FY26
(company memory, not re-anchored here as evidence).

- **B1 Cumulative CFO ÷ Cumulative PAT** = 88.33 / 87.23 = 1.013 → ≥1.00 →
  **5**
- **B2 FCF-positive years** = 2 of 3 (FY25, FY26 positive; FY24 negative)
  = 66.7% → 50-74% band → **2**
- **B3 Cumulative FCF ÷ Cumulative PAT** = -55.58 / 87.23 = -0.637 →
  negative → **0**
- **B4 Change in WC Days, latest vs earliest** = 78.9 - 73.8 = +5.0 days →
  increased 5-15 → **1**

**Block B total = 8/20**

block_b_trend: **deteriorating** — CFO fell from Rs 51.32 cr (FY25) to
Rs 27.55 cr (FY26), a 46% decline, on the inventory build (LBF-2); WC days
rose from 65.2 (FY25) to 78.9 (FY26), +13.7 days within the year even
though the 3-year trend (FY24→FY26) is a smaller +5.0 day net change
because FY24's WC days (73.8) were already elevated by the pre-listing
capex ramp.

---

## BLOCK C: GROWTH (Max 20)

Revenue and PAT from the audited P&L (screener-Data_Sheet.csv, cross-
verified against AR FY25 p.57 and FY26 results p.5).

| Year | Revenue (cr) | PAT (cr) |
|---|---|---|
| FY24 | 228.50 | 29.71 |
| FY25 | 232.66 | 28.75 |
| FY26 | 251.01 | 28.77 |

- **C1 Revenue CAGR** (FY24→FY26, 2 years) = (251.01/228.50)^(1/2) - 1 =
  4.81% → <5% → **0**
- **C2 PAT CAGR** = (28.77/29.71)^(1/2) - 1 = -1.60% → negative → **0**
  (PAT effectively flat-to-down across the 3 audited years: Rs 29.71 cr →
  28.75 cr → 28.77 cr, not a loss-to-profit swing, no data_notes entry
  needed on that account)
- **C3 Positive YoY revenue years** = 2 of 2 transitions (FY24→FY25,
  FY25→FY26 both positive) = 100% → **5**
- **C4 PAT CAGR minus Revenue CAGR** = -1.60 - 4.81 = -6.41pp → -3 to -8pp
  band → **1**

**Block C total = 6/20**

This is the weakest block. Three years of essentially flat revenue
(4.8% CAGR) and flat-to-declining PAT (-1.6% CAGR) sit directly underneath
the Q1 FY27 print (+28.9% revenue, OPM 16.1%→22.9%, PAT +137% per LBF-1).
The scorecard captures the pre-inflection base the thesis has to prove a
break from; it does not and cannot capture Q1 FY27 itself (single quarter,
not a scoring year).

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

FY26 figures (latest). Borrowings and cash from screener-Data_Sheet.csv,
cross-verified: FY26 total borrowings Rs 16.64 cr = non-current borrowings
Rs 10.72 cr + current borrowings Rs 4.15 cr + lease liabilities Rs 1.77 cr
(AR FY26 Balance Sheet, p.69), all summing exactly to the screener figure.
Cash & bank balances Rs 6.28 cr (AR FY26, cash and other bank balances
notes). Net worth FY26 = Equity Share Capital Rs 51.59 cr + Reserves
Rs 116.99 cr = Rs 168.58 cr.

- **D1 Net Debt ÷ EBITDA** = (16.64 - 6.28) / 52.62 = 10.36 / 52.62 =
  0.197x → 0-1.0x band → **4**. [Note: this excludes Rs 23.23 cr of
  mutual-fund investments (AR FY26 Balance Sheet); including them as
  quasi-cash would flip the company to net cash. EBITDA (Operating
  Profit, excludes other income) FY26 = Revenue 251.01 - (Cost of
  materials 93.32 + purchases 0.32 + change in inventories -12.52 +
  employee cost 50.44 + other expenses 66.83) = Rs 52.62 cr, computed
  from FY26 Audited Results p.5.]
- **D2 Interest Coverage, EBIT ÷ Interest** = EBIT (PBT + Finance cost =
  39.50 + 1.66 = 41.16) ÷ Interest 1.66 = 24.8x → ≥10x → **5**
- **D3 Debt ÷ Equity** = 16.64 / 168.58 = 0.099 → <0.1 → **5** [boundary
  note: the AR's own disclosed Debt-Equity Ratio (narrower "total debt"
  definition, excludes lease) is 10% for FY26 (AR FY26, p.118), which sits
  exactly at the 0.1 threshold; this stage's computed figure using
  screener's total-borrowings-incl-lease basis is 9.9%, just under the
  threshold, and is used for scoring]
- **D4 Current Ratio** = 1.84 (AR-disclosed, AR FY26 p.118) → 1.5-1.99
  band → **4**

**Block D total = 18/20** — strongest block. Company is near net cash on
a comprehensive basis, has ample interest cover, and carries almost no
leverage.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

Source: shareholding__SHP_30Jun2026.txt (p.4-5), shareholding__SHP_31Mar2026.txt
(p.4-5), shareholding__SHP_30Jun2025.txt (p.4-5) — the three shareholding
filings provided in this run (no earlier SHP filing was provided; the
company listed 11-Jun-2024, so a true 3-year promoter-holding-change window
does not yet exist in the listed company's own life, let alone in this
run's inputs).

- **E1 Promoter holding (latest, Jun-2026)** = 73.85% → ≥60% → **5**
- **E2 Promoter holding change** — unchanged at 73.85% across all three
  filings available (Jun-2025, Mar-2026, Jun-2026; ~12 months of data, not
  3 years — see note above) → within ±1% → **3** [data_note: window is
  ~12 months not 3 years, due to short listed history; treat this score as
  provisional]
- **E3 Promoter pledge (latest, Jun-2026)** = 94.4% of the 73.85% promoter
  holding (35,967,172 of 38,102,764 shares) → >15% → **0**
- **E4 Contingent liabilities ÷ Net Worth** = Rs 16.81 lakh / Rs 168.58 cr
  = Rs 0.1681 cr / Rs 168.58 cr = 0.0997% → <5% → **5**

**Block E total = 13/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Peer screening CSVs provided for this run (KENNAMET-, WENDT-, BIRLAPREC-
prefixed files in inputs/screening/) are empty templates — headers only,
no populated financial data (identical empty structure to the subject's own
Profit_Loss.csv/Balance_Sheet.csv/Cash_Flow.csv/Quarters.csv files, which
were superseded by a populated Data_Sheet.csv that has NO peer-side
equivalent in this run's inputs). Every moat test requiring peer figures
is therefore scored 0 and marked PEER DATA NEEDED per the prompt's rule;
the peer figures quoted in company memory (step1-business-brief.md) are
NOT used as they are not this run's own verified inputs.

- **M1 Pricing Power**: OPM FY24 22.5% → FY26 21.0%, change -1.5pp (not
  expansion); revenue CAGR 4.8% (<10%). Fits no scoring tier. **0**
- **M2 Cost Advantage vs peer median EBITDA margin**: PEER DATA NEEDED.
  **0**
- **M3 Capital Efficiency**: FAT (Revenue ÷ [Net Block + CWIP]) FY26 =
  251.01 / 113.40 = 2.21x; ROCE FY26 = 22%. FAT>2x AND ROCE>15% → **3**
- **M4 Customer Stickiness**: zero revenue-decline years (FY24→25→26 both
  positive); receivable days FY24 47.0 → FY26 43.9, within ±10 days →
  **5**
- **M5 Scale & Dominance**: PEER DATA NEEDED. **0**
- **M6 Technology/R&D**: R&D spend not disclosed as a separate line in any
  provided filing (NOT FOUND). **0**
- **M7 Regulatory/License**: unregulated, no licence/quota regime governs
  this business. **0**
- **M8 Distribution**: not disclosed in any filed source in this run (the
  "200+ distributors / 12 divisional offices" figure exists only on the
  company website, cited in company memory, not in the AR/results filings
  actually read this run — NOT FOUND in provided data). **0**
- **M9 Brand**: PEER DATA NEEDED (gross-margin-vs-peer-median test). **0**
- **M10 Switching Costs**: revenue grew every year AND receivable days
  fell (43.9 vs 47.0, i.e. rose ≤10 days trivially satisfied) → **5**
- **M11 Network Effects**: only 3 years available, below the 6-year
  two-window test threshold; scored conservatively on overall trend. 2-year
  CAGR is weak (4.8%) and well under the ≥15-20% thresholds in any tier;
  business model (industrial consumable tooling) shows no structural
  network-effect mechanism. **0** [fewer than 6 years available, scored
  conservatively per the rule]
- **M12 Negative WC/Float**: WC days positive and >45 in all three years
  (73.8, 65.2, 78.9). **0**

**Moats present (score ≥3): M3, M4, M10 = 3 moats**
**Moat score = 3+5+0+5+0+0+0+0+0+5+0+0 = 13/60**
**Moat classification: 2-3 present = MODERATE**

---

## SCORECARD DASHBOARD

```
BLOCK A  Return on Capital        [======......] 13/20
BLOCK B  Cash Generation Quality  [========......] 8/20
BLOCK C  Growth                   [======........] 6/20
BLOCK D  Balance Sheet Strength   [==================] 18/20
BLOCK E  Shareholder Alignment    [=============.] 13/20
--------------------------------------------------------
CORE SCORE (A+B+C+D+E)                              58/100

BLOCK F  Quantitative Moat (12 tests, max 60)        13/60
Moats present: M3 Capital Efficiency, M4 Customer Stickiness,
               M10 Switching Costs
Moat classification: MODERATE (3 of 12 present)

GRAND TOTAL (core + moat)                            71/160
```

**Strongest block: D (Balance Sheet Strength), 18/20.** Near net cash,
24.8x interest coverage, D/E 0.10x, current ratio 1.84x.

**Weakest block: C (Growth), 6/20.** Flat revenue (4.8% 3-year CAGR),
flat-to-declining PAT (-1.6% CAGR) across the three audited years — a
structurally quiet base sitting directly beneath the Q1 FY27 inflection
claim, which this scorecard's fixed 3-year annual window cannot capture.

---

## CLASSIFICATION

**Data confidence**: 3 years (FY24-FY26) → 3-4 band → **LIMITED,
downgrade classification one tier**.

**Classification matrix**: Core score 58 falls in the 40-59 band →
baseline **AVERAGE** (this band is flat in the matrix; it does not branch
on moat tier).

**Deal-breaker overrides checked**:
1. Block A <8? No (13). Not triggered.
2. Block B <8? No (8, exactly at the line). Not triggered.
3. Median ROCE <10%? No (22%). Not triggered.
4. Cumulative CFO/PAT <0.50? No (1.01). Not triggered.
5. **Pledge >15%? YES (94.4% of the 73.85% promoter stake pledged,
   Shapoorji Pallonji & Co., stable across three consecutive quarters
   Jun-2025 to Jun-2026) → caps classification at max AVERAGE.**
6. ND/EBITDA >3x AND IC <3x? No (0.2x and 24.8x). Not triggered.
7. Revenue declined in majority of years? No (grew both years). Not
   triggered.
8. PAT negative in any of last 3 years? No (positive all three, ~Rs 29 cr
   flat). Not triggered.
9. History <3 years? No (exactly 3 audited years). Not triggered (this is
   distinct from the data-confidence downgrade above, which uses a 3-4
   year LIMITED band rather than a strict <3 threshold).

**Sequencing**: baseline AVERAGE (Core 40-59) → apply the 3-year LIMITED
history-confidence downgrade, one tier: AVERAGE → **AVOID**. The pledge
deal-breaker independently caps the classification at "max AVERAGE" — a
ceiling, not a floor — so it does not itself force AVOID, but it does
confirm the classification cannot rise above AVERAGE even before the
history downgrade is applied.

**FINAL CLASSIFICATION: AVOID** (mechanical, per the fixed scoring rules)

This is a compounding-mechanism outcome, not a company-quality verdict on
its own terms, and CLAUDE.md is explicit that quality does not halt a run
and that "downstream position sizing may override AVERAGE for documented
post-IPO rebase / legacy cleanup cases." Two distinct things drive AVOID
here and both should be weighed on their own facts by the operator, not
collapsed into one:
- The pledge (94.4% of promoter stake, stable, no operating-company
  guarantee found) is a real governance flag on its own facts, not a
  rebase artifact — the promoter has pledged nearly all of its holding
  for reasons outside this filing set.
- The 3-year LIMITED-history downgrade is a structural artifact of the
  Mar-2024 demerger and Jun-2024 listing, not a company-quality signal.
  Absent that downgrade, the mechanical floor here is AVERAGE (from the
  pledge deal-breaker alone), not AVOID.
Underlying fundamentals in the three audited years are unremarkable-to-
solid: near-net-cash balance sheet, 22% ROCE, positive cumulative
CFO/PAT — sitting under flat growth and a cash-conversion wobble in FY26
that LBF-1's Q1 FY27 print (if it holds up) would be the first data point
against.

---

## DECISION LINE

Gate 0 mechanical classification: **AVOID** (pledge deal-breaker caps at
AVERAGE; 3-year LIMITED-history downgrade pulls one tier further to
AVOID). Flags propagate; this does not halt the run. Historical
depressors are named above (flat 3-year growth, FY26 cash-conversion
deterioration, near-total promoter pledge, short listed history) for the
operator to weigh against the Q1 FY27 inflection claim this run exists to
test.
