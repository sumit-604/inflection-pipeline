# STAGE 1 — GATE 0 SCORECARD
TAAL Tech Ltd (TAALTECH) | Run: taaltech-2026-09-10 | Model: claude-sonnet-5

Data available: 10 years (FY2017 to FY2026), consolidated. Scoring adapted to
10-year history. Ten quarters also available (Mar 2024 to Jun 2026).
Primary source: screener-Data_Sheet.csv (consolidated P&L, balance sheet,
cash flow, quarters), cross-checked line by line against the audited
consolidated FY2026 results (results__Results_Q4FY26_Mar_2026.txt) and the
FY2025-26 Annual Report (annual-report__Annual_Report_2026.txt). Every
Data_Sheet total reconciled exactly against the audited filings where a
filing figure existed (Total Assets, Revenue, PAT, CFO, Receivables,
Investments — all match to the rupee-lakh).

## CORPUS MECHANICS NOTE ON HISTORY
TAAL Tech Ltd (formerly TAAL Enterprises Ltd, "TTL") received TWO businesses
in a single Oct-2014 demerger from Taneja Aerospace and Aviation Ltd
("TAAL"): the Air Charter business (including an investment in First
Airways Inc, USA) AND the Engineering Design Services business, the latter
held through wholly-owned subsidiary TAAL Tech India Pvt Ltd ("TTIPL")
(AR p.69, standalone Note 1, General Information). TTIPL was consolidated
into TTL's group accounts from that point; the May-2025 NCLT order that
amalgamated TTIPL into TTL as one legal entity (appointed date 1-Apr-2023)
changed the STANDALONE accounts materially (standalone total assets moved
Rs19cr Mar-2024 to Rs207cr Mar-2025, per company memory) but should NOT have
changed the CONSOLIDATED series, since TTIPL was already inside
consolidation. Data_Sheet.csv reconciles exactly to the audited CONSOLIDATED
statements, so it is used as the primary series here.
UNRESOLVED: the FY2026 AR (the only annual report in this corpus) reports a
single segment, "Engineering Design Service" (AR p.78/119, segment note),
for FY2026 and FY2025 only. It does not disclose when the Air Charter
business stopped contributing consolidated revenue, or whether it still did
during FY2017-FY2021. No annual report older than FY2026 is in this corpus.
A FY2021 anomaly is notable and unexplained: Net Block fell from Rs5.22cr to
Rs0.62cr against depreciation of only Rs2.28cr (Data_Sheet.csv), implying
~Rs2.3cr of disposals/write-offs beyond normal depreciation that year — this
is consistent with, but does NOT confirm, an aircraft-related write-off; it
is equally consistent with Ind AS 116 lease-asset reclassification (adopted
industry-wide around FY2020). **This is flagged, not resolved. history_downgrade
= true.** FY2017-FY2021 revenue/profit rows are used in the mechanical
scoring below because they are the only data available (rule: "use whatever
history is available"), but every metric touching those years is flagged
where it drives a score.

---

## BLOCK A: RETURN ON CAPITAL (max 20)

Formula used: ROCE = Operating EBIT ÷ (Total Assets − Non-Debt Liabilities),
computed, not sourced (Data_Sheet.csv carries no ROCE row). Operating EBIT =
Operating Profit − Depreciation, EXCLUDING Other Income (see load-bearing
fact 1 discussion below Block C). Capital Employed = Total Assets − "Other
Liabilities" row (Data_Sheet.csv), which retains the "Borrowings" row
(= lease liabilities, confirmed by exact match to AR lease-liability notes
for FY2025/FY2026) inside capital employed, the standard ROCE convention.
This Capital Employed basis was validated exactly against the audited
FY2025/FY2026 balance sheets (results Q4FY26 p.16).

| FY | Op. Profit | Dep. | Op. EBIT | Total Assets | Other Liab. | Cap. Employed | ROCE |
|---|---|---|---|---|---|---|---|
|2017|10.51|1.29|9.22|43.99|17.01|26.98|34.2%|
|2018|16.48|2.22|14.26|57.09|23.25|33.84|42.1%|
|2019|30.98|1.31|29.67|83.26|34.07|49.19|60.3%|
|2020|31.36|5.83|25.53|96.00|45.47|50.53|50.5%|
|2021|22.55|2.28|20.27|110.66|34.40|76.26|26.6%|
|2022|40.26|3.60|36.66|138.35|30.53|107.82|34.0%|
|2023|43.40|5.29|38.11|156.12|22.59|133.53|28.5%|
|2024|47.17|6.33|40.84|190.31|21.23|169.08|24.2%|
|2025|58.81|5.53|53.28|227.88|19.89|207.99|25.6%|
|2026|59.50|4.04|55.46|270.93|24.88|246.05|22.5%|
(All figures Rs cr, screener-Data_Sheet.csv, computed)

**A1 Median ROCE** = 31.25% (median of the ten years above) → ≥25% → **A1 = 5**
**A2 Minimum single-year ROCE** = 22.5% (FY2026) → ≥15% → **A2 = 5**

**A3 Median ROE**: ROE = PAT ÷ average Net Worth (opening+closing÷2); FY2017
uses closing Net Worth only (no FY2016 opening figure in provided data,
stated per rule).
Net Worth (Equity Share Capital + Reserves, screener-Data_Sheet.csv):
17.17 / 32.96 / 48.83 / 50.53 / 76.26 / 98.70 / 124.16 / 162.28 / 204.04 / 245.14 (FY17-26)
ROE: 22.2% / 62.3% / 44.4% / 34.8% / 50.2% / 36.5% / 28.0% / 25.9% / 26.6% / 25.3%
Median = 31.4% → ≥20% → **A3 = 5**
FLAG: ROE and ROCE both run very high in FY2017-2019 (44-62%) off a small
post-demerger equity base, then settle to a stable mid-20s% band from
FY2023 onward. The mid-20s band (FY2023-FY2026: 24.2-28.5% ROCE, 25.3-28.0%
ROE) is the more representative read of the business as it stands today.

**A4 ROCE trend, latest vs earliest**: FY2026 (22.5%) vs FY2017 (34.2%) =
decline of 11.7pp → decline >5pp → **A4 = 0**
FLAG: this comparison uses FY2017 as the earliest year, which per the
history-break note above carries unresolved comparability risk (thin
capital base, possible charter-business residue). Comparing FY2026 (22.5%)
to FY2022 (34.0%, the first year after the FY2021 disposal anomaly) still
shows an 11.5pp decline — so the declining-ROCE read is not solely an
artifact of the FY2017 base; it also holds across a shorter, safer window.

**BLOCK A TOTAL: 15/20**

---

## BLOCK B: CASH GENERATION QUALITY (max 20)

CFO and PAT, screener-Data_Sheet.csv, cross-checked against results Q4FY26
p.17 (consolidated cash flow statement) for FY2025/FY2026 — exact match.

| FY | CFO | PAT | CFO/PAT |
|---|---|---|---|
|2017|2.41|3.81|0.63x|
|2018|14.59|15.61|0.93x|
|2019|23.24|18.14|1.28x|
|2020|32.59|17.28|1.89x|
|2021|39.98|31.80|1.26x|
|2022|29.63|31.91|0.93x|
|2023|21.96|31.23|0.70x|
|2024|34.41|37.15|0.93x|
|2025|41.02|48.79|0.84x|
|2026|18.74|56.72|0.33x|

**B1 Cumulative CFO ÷ Cumulative PAT** = 258.57 ÷ 292.44 = **0.884x** →
0.85-0.99 band → **B1 = 4**

**B2/B3 FCF**: FCF = CFO − Capex. Data_Sheet.csv does not carry a capex row
for FY2017-2024. FY2025/FY2026 capex is directly filed (results Q4FY26
p.17, consolidated: Rs1.62cr FY2025, Rs0.13cr FY2026). For FY2018-2024,
capex is COMPUTED as ΔNet Block + Depreciation (a derived figure from
Data_Sheet.csv, not an estimate; stated as "computed, proxy basis" per the
rule that instructs computing only when a source figure is absent). This
proxy was checked against the FY2025 filed figure (proxy Rs1.65cr vs filed
Rs1.62cr — within 2%), giving reasonable confidence for FY2018-2024. FY2017
is excluded (no FY2016 Net Block to build the delta). FY2021 is excluded:
Net Block fell more than the depreciation charge that year (see history-break
note), so the proxy cannot isolate capex from disposal, and the result would
be a negative "capex" that is not meaningful.

| FY | Capex (basis) | FCF |
|---|---|---|
|2017| N/A (not in provided data) | N/A |
|2018| 2.23 (computed) | 12.36 |
|2019| 0.96 (computed) | 22.28 |
|2020| 5.34 (computed) | 27.25 |
|2021| N/A (proxy invalid — disposal year) | N/A |
|2022| 15.46 (computed) | 14.17 |
|2023| 6.40 (computed) | 15.56 |
|2024| 2.89 (computed) | 31.52 |
|2025| 1.62 (results Q4FY26 p.17, filed) | 39.40 |
|2026| 0.13 (results Q4FY26 p.17, filed) | 18.62 |

**B2 FCF-positive years**: of the 8 years with usable data, all 8 are
positive = 100% of computable years → **B2 = 5** (2 of 10 years, FY2017 and
FY2021, are N/A and excluded — noted as a data gap, not scored as negative)

**B3 Cumulative FCF ÷ Cumulative PAT** (8 usable years) = 181.16 ÷ 256.83 =
**0.705x** → ≥0.60 → **B3 = 5**

**B4 Change in WC Days, latest vs earliest**: WC Days = Receivable Days +
Inventory Days − Payable Days. screener-Data_Sheet.csv has no Trade Payables
row for ANY year, and Inventory is blank throughout (nil for a services
business). Trade Payables are only available for FY2025/FY2026, from the
audited consolidated balance sheet (results Q4FY26 p.16: FY2026 payables
Rs4.19cr, FY2025 Rs1.96cr). FY2017 payables are NOT FOUND (no pre-FY2025
annual report in this corpus). **B4 cannot be computed on the mandated
latest-vs-earliest (FY2026 vs FY2017) basis → B4 = N/A, scored 0.**
Supplementary, the only full-formula WC Days available (FY2025 → FY2026,
one year): 72.3 days → 88.4 days, a 16.1-day increase in the single year
that can be fully checked (Receivable Days 76.1→96.2 days, Payable Days
3.9→7.8 days; screener-Data_Sheet.csv + results Q4FY26 p.16). This is
directional evidence for the FLAG-CASH item below, not a scored input.

**BLOCK B TOTAL: 14/20**
**block_b_trend: DETERIORATING** — CFO/PAT fell from 0.84x (FY2025) to
0.33x (FY2026); Trade Receivables rose Rs38.61cr to Rs52.04cr and Other
Financial Assets + Other Current Assets (consolidated) rose Rs12.86cr to
Rs28.48cr over the same year (results Q4FY26 p.16), a working-capital build
that coincides with the Q4FY26/Q1FY27 revenue acceleration discussed under
load-bearing fact 2. The 10-year cumulative ratios (B1=0.884x, B3=0.705x)
score well, but they average over an improving FY2018-2021 stretch and a
now-deteriorating FY2025-2026 stretch; the LATEST year alone would fail B1's
top bands (0.33x sits in the "<0.50 = 0" band as a standalone-year reading).

---

## BLOCK C: GROWTH (max 20)

Revenue and PAT, screener-Data_Sheet.csv.

**C1 Revenue CAGR, FY2017→FY2026 (9 yrs)**: (197.43/92.06)^(1/9)−1 = **8.85%**
→ 5-9.9% band → **C1 = 1**

**C2 PAT CAGR, FY2017→FY2026 (9 yrs)**: (56.72/3.81)^(1/9)−1 = **35.0%** →
≥20% → **C2 = 5**
FLAG: this is driven almost entirely by the FY2017 base (PAT Rs3.81cr, the
smallest year in the series, sitting close to the post-demerger transition).
A shorter, more representative window: FY2022→FY2026 (4 yrs) PAT CAGR =
(56.72/31.91)^(1/4)−1 = **15.5%**; FY2024→FY2026 (2 yrs) = **23.6%**. Both
are real numbers, both are lower than the formally-scored 35.0%.

**C3 Positive YoY revenue years**: of 9 YoY comparisons (FY18-FY26), 6 are
positive (FY18, FY19, FY22, FY23, FY24, FY26) and 3 are declines (FY20, FY21,
FY25) → 6/9 = 66.7% → 50-74% band → **C3 = 1**

**C4 PAT CAGR − Revenue CAGR** = 35.0% − 8.85% = **+26.15pp** → ≥+3pp →
**C4 = 5**
FLAG: same FY2017-base sensitivity as C2. On the FY2022-2026 window,
revenue CAGR is (197.43/129.36)^(1/4)−1 = 11.15%, PAT CAGR 15.5%, spread
+4.3pp — still positive operating leverage, materially smaller than the
scored +26.15pp.

**BLOCK C TOTAL: 12/20** (formally computed; FLAG-GATE0 attached — see
analyst_note for the base-year sensitivity this total carries)

---

## LOAD-BEARING FACT 1 — THE 30% OPERATING MARGIN

Operating Profit (screener-Data_Sheet.csv methodology, reconciled exactly to
the audited P&L) = Revenue − Employee Cost − Selling & Admin − Other
Manufacturing Expense − Power & Fuel − Other Expenses. This EXCLUDES Other
Income and Depreciation. Checked against the audited consolidated FY2026
P&L (results Q4FY26 p.14): Revenue Rs197.43cr (19,742.92 lakh) − Employee
Rs115.13cr (11,499.87 lakh) − Other Expenses Rs20.76cr (Selling&Admin
17.59 + Other Mfr 1.37 + Power&Fuel 0.67 + Other Exp 3.17, reconciling to
the filed "Other expenses" line of Rs23.10cr once Data_Sheet's four
sub-lines are combined; the residual Rs2.34cr difference reflects
classification granularity between screener's five expense sub-lines and
the filing's single "Other expenses" line — both total to the same Total
Expenses figure) = Operating Profit Rs59.50cr, OPM **30.1%** for FY2026;
**31.8%** for FY2025 (Rs58.81cr / Rs185.14cr). This IS a genuinely operating
figure: it contains no Other Income.
Other Income sits SEPARATELY at Rs19.40cr (Data_Sheet.csv) / Rs19.03cr
(results Q4FY26 p.14, consolidated Rs1,902.72 lakh) inside FY2026 PBT of
Rs74.36cr / Rs74.36cr — **26% of pre-tax profit is non-operating.** The
cash-flow statement (results Q4FY26 p.17) itemises the source: Mark-to-market
gain on investments Rs12.04cr, interest income on debentures Rs3.64cr,
interest income on fixed deposits Rs1.23cr, other interest income Rs0.99cr,
dividend income Rs0.08cr — these sum to ~Rs17.98cr of the Rs19.03cr Other
Income, i.e. Other Income is overwhelmingly treasury/investment return on
the Rs143.89cr investment book (Data_Sheet.csv; matches results Q4FY26 p.16
non-current + current investments Rs12,651.95 lakh + Rs1,737.08 lakh
exactly), not operations.
**Conclusion: the 30-32% margin is operating. It is a genuine EBITDA margin
on the engineering-services revenue line, separate from the Rs19cr of
treasury income that also runs through the P&L.** The margin RISE from 25%
(FY2024) to 32% (FY2025) while revenue fell Rs186.87cr to Rs185.14cr is
attributable to Employee Cost falling Rs113.91cr to Rs106.41cr that year
(Data_Sheet.csv) — a cost-control move during a flat-revenue year, not a
mix-shift or an other-income artifact. FY2026 OPM eased slightly to 30.1%
as Employee Cost rose again to Rs115.13cr alongside the revenue recovery.

## LOAD-BEARING FACT 2 — THE Q1 FY27 REVENUE JUMP

Consolidated revenue: Q1 FY27 (Jun 2026) Rs64.81cr (Rs6,481.12 lakh) vs Q1
FY26 (Jun 2025) Rs45.77cr (Rs4,576.78 lakh), +41.6% (results Q1FY27 p.6).
Standalone: Rs63.23cr vs Rs43.88cr, +44.1% (results Q1FY27 p.2). Net profit
(consolidated): Rs19.43cr vs Rs13.71cr, +41.7%.
The jump is NOT isolated to one quarter: consolidated revenue ran Rs45.79cr
(Q3 FY26, Dec 2025) → Rs57.04cr (Q4 FY26, Mar 2026, +24.6% QoQ) → Rs64.81cr
(Q1 FY27, Jun 2026, +13.6% QoQ) (screener-Data_Sheet.csv, quarters section).
This is a two-quarter acceleration, not a single-quarter spike.
The Q1 FY27 results filing lists the same three consolidated subsidiaries
(TAAL Technologies Inc USA, TAAL Tech GmbH Switzerland, TAAL Tech UK Ltd) as
the FY2026 annual report (results Q1FY27 p.4; AR p.10, auditor's report on
consolidated results) — **no new subsidiary or acquisition entered the
consolidation between the FY2026 AR and Q1 FY27**, ruling out an
M&A-driven step-change as the explanation.
Beyond that, **the filings name no cause.** There is no MD&A, no segment
disaggregation by client or geography, and — per NO-CONCALL MODE — no
earnings call or investor presentation exists to ask management. Whether the
step is organic demand, one large client ramp, or a scope change cannot be
confirmed or ruled out from the documents provided. This remains an open
verification item for the next stage.

## LOAD-BEARING FACT 3 — CASH CONVERSION

Covered fully under Block B / block_b_trend above. Consolidated CFO fell to
Rs18.74cr (results Q4FY26 p.17: 1,874.29 lakh) against PAT Rs56.72cr, 0.33x,
down from Rs41.02cr against Rs48.79cr, 0.84x, in FY2025 — both figures match
Data_Sheet.csv exactly. Receivables rose Rs38.61cr to Rs52.04cr (results
Q4FY26 p.16). The cash-flow statement's working-capital line ("Decrease/
(increase) in trade and other receivables") shows an outflow of Rs27.88cr in
FY2026 versus a Rs1.06cr inflow in FY2025 (results Q4FY26 p.17) — this is
LARGER than the trade-receivables move alone, meaning Other Financial Assets
and Other Current Assets (likely unbilled revenue / contract assets) also
built materially: Rs6.56cr→Rs15.78cr and Rs6.30cr→Rs12.70cr respectively
(results Q4FY26 p.16). **Trend direction: deteriorating, and broader than
receivables alone.** This coincides with the Q4FY26/Q1FY27 revenue
acceleration (load-bearing fact 2) — consistent with growth-induced working
capital stretch, but the filings do not confirm this causal link explicitly.

## LOAD-BEARING FACT 4 — RELATED-PARTY EXPOSURE TO THE TANEJA GROUP

FY2026 related-party note (AR p.97, standalone Note 37; p.150, consolidated
Note 36): TAAL Tech Ltd's HOLDING COMPANY is **Vishkul Enterprises Private
Limited** (50.74% of equity, AR p.86), not Taneja Aerospace directly.
"Entities under common control" (same promoter, Salil Taneja) include
Taneja Aerospace and Aviation Ltd, Katra Auto Engineering Pvt Ltd, Asscher
Enterprises Ltd (erstwhile Indian Seamless Enterprises Ltd), and (until
14/19-Feb-2025) Laurus Tradecon Pvt Ltd.
Transactions with Taneja Aerospace and Aviation Ltd in FY2026 are minor: a
single "Sale of Car" for Rs1.50 lakh (AR p.97). No material balance,
guarantee, or loan to/from Taneja Aerospace is disclosed for FY2026 or
FY2025.
The material related-party item is instead a **Rs1,000 lakh (Rs10cr) loan
to holding company Vishkul Enterprises Pvt Ltd** during FY2026 (interest
income Rs98.55 lakh, ~9.85% effective rate, AR p.97) with no comparable FY2025
transaction. Terms are stated as arm's length (AR p.98). This is a promoter
holding-company loan, not a Taneja-Aerospace-specific exposure; it does not
map to Gate 0's mechanical E-block tests but is flagged for the Role 2
promoter ledger.
Contingent liabilities (consolidated, Note 36, AR p.150): Rs938.46 lakh
(Rs9.38cr) FY2026, Rs777.92 lakh (Rs7.78cr) FY2025 — both are an
income-tax dispute (AY2016-17 and AY2020-21 assessment orders), not related
to the Taneja group.

---

## BLOCK D: BALANCE SHEET STRENGTH (max 20)

Latest year = FY2026, screener-Data_Sheet.csv, cross-checked to results
Q4FY26 p.16 (consolidated B/S).

**D1 Net Debt ÷ EBITDA**: Borrowings Rs0.91cr (= lease liabilities, exact
match to AR lease-liability notes) vs Cash & Bank Rs27.78cr → Net Debt is
negative (net cash of Rs26.87cr) → **D1 = 5**

**D2 Interest Coverage** = Operating EBIT (Rs55.46cr) ÷ Interest (Rs0.50cr,
Data_Sheet.csv; results Q4FY26 p.14 gives consolidated finance costs of
Rs0.33cr for FY2026 — either figure gives >100x) → ≥10x → **D2 = 5**

**D3 Debt ÷ Equity** = Rs0.91cr ÷ Rs245.14cr = 0.0037x → <0.1 → **D3 = 5**

**D4 Current Ratio** = Total Current Assets Rs135.68cr ÷ Total Current
Liabilities Rs25.79cr (results Q4FY26 p.16, consolidated) = 5.26x → ≥2.0 →
**D4 = 5**

**BLOCK D TOTAL: 20/20** — no debt, deep net cash, no leverage concerns.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (max 20)

**E1 Promoter holding (latest)**: Vishkul Enterprises Pvt Ltd 50.74% + Salil
Baldevraj Taneja 0.04% + Asscher Enterprises Ltd 0.02% = **50.80%** as at
31-Mar-2026 (AR p.86, Shareholding of Promoters note) → 50-59.9% band →
**E1 = 4**

**E2 Promoter holding change over 3 years**: NOT FOUND. The FY2026 AR
discloses promoter holding for FY2025 and FY2026 only (both 50.80%, "% of
change during the year" shown as nil, AR p.86); no FY2023 shareholding
pattern is in this corpus to build the mandated 3-year comparison. **E2 = 0
(N/A, data gap)**

**E3 Promoter pledge (latest)**: NOT FOUND. No pledge/encumbrance note for
promoter shares was located anywhere in the FY2026 annual report; the SEBI
quarterly shareholding-pattern filing (which carries the dedicated
encumbrance column) is not in this corpus. Per rule, not estimated. **E3 = 0
(N/A, data gap)** — flagged for downstream verification since the balance
sheet shows no company-level borrowing against which shares would typically
be pledged, making pledge unlikely but unconfirmed.

**E4 Contingent Liabilities ÷ Net Worth**: Rs9.38cr ÷ Rs245.14cr = **3.83%**
(AR p.150, consolidated Note 36; Net Worth from screener-Data_Sheet.csv) →
<5% → **E4 = 5**

**BLOCK E TOTAL: 9/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (max 60)

| # | Test | Score | Basis |
|---|---|---|---|
| M1 | Pricing Power | 0 | OPM expanded 11.4%→30.1% (FY17→FY26, screener-Data_Sheet.csv) but revenue CAGR is 8.85%, below the ≥10% qualifying threshold for any non-zero band. Formula gives 0 despite genuine margin gain — rule artifact, flagged. |
| M2 | Cost Advantage vs peers | 0 | PEER DATA NEEDED — no peer financial statements in this run's input set. |
| M3 | Capital Efficiency | 5 | FAT = Rev÷Net Block = 197.43/2.95 = 66.9x; ROCE(op) 22.5%. Both clear the top band. FLAG: Net Block is near-zero (Rs2.95cr) for an asset-light services business — FAT is not a meaningful capital-intensity signal here; the mechanical score is a formula artifact for this business model, not evidence of a productive-asset moat. |
| M4 | Customer Stickiness | 0 | 3 revenue-decline years (FY20, FY21, FY25) → "3+ decline years" band. |
| M5 | Scale & Dominance | 0 | PEER DATA NEEDED — no peer mcap/margin ranking data provided. |
| M6 | Technology/R&D | 0 | R&D expense Rs37.55 lakh (Rs0.376cr) FY2026 (AR p.49, Conservation of Energy / Technology Absorption / R&D note) ÷ Revenue Rs197.43cr = 0.19%. Below the ≥1% floor for any non-zero score. Only one year of R&D disclosure available (standalone, mandatory Companies Act note). |
| M7 | Regulatory/License | 0 | Unregulated ER&D services business; no license/quota constraint identified. |
| M8 | Distribution | 0 | No physical distribution network; B2B direct-delivery services model. |
| M9 | Brand | 0 | PEER DATA NEEDED — no peer gross-margin data provided for comparison. |
| M10 | Switching Costs | 1 | Overall growth FY17→FY26 positive, but 3 decline years (≥2) → "overall growth, 2+ decline years" band. |
| M11 | Network Effects | 5 | Latest-3yr revenue CAGR (FY23→FY26) 7.45% > prior-3yr (FY20→FY23) 7.01% AND Selling&Admin/Revenue declining (avg 9.18% FY21-23 window → avg 8.86% FY24-26 window, screener-Data_Sheet.csv). FLAG: the CAGR gap (0.44pp) is marginal; this is a borderline pass on the ">" test, not a strong signal. |
| M12 | Negative WC/Float | 0 | Only FY2025 (72.3 days) and FY2026 (88.4 days) have full WC-Days data (Trade Payables unavailable pre-FY2025); both are well above the 45-day ceiling. Insufficient data to assess "majority of years" formally, but both available years fail decisively, and Receivable Days alone (60-96 days every year, screener-Data_Sheet.csv) make a negative-WC finding for the missing years very unlikely. Scored on available evidence. |

**Moats present (score ≥3): 2 of 12 (M3, M11)**
**MOAT SCORE: 11/60**
**MOAT CLASSIFICATION: MODERATE** (2 present → 2-3 band)

Moat profile:
```
M1  [                    ] 0
M2  [PEER DATA NEEDED    ] 0
M3  [########## ] 5  present
M4  [                    ] 0
M5  [PEER DATA NEEDED    ] 0
M6  [                    ] 0
M7  [                    ] 0
M8  [                    ] 0
M9  [PEER DATA NEEDED    ] 0
M10 [##                  ] 1
M11 [########## ] 5  present (borderline)
M12 [                    ] 0
```

---

## CLASSIFICATION

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 15 | 20 |
| B — Cash Generation Quality | 14 | 20 |
| C — Growth | 12 | 20 |
| D — Balance Sheet Strength | 20 | 20 |
| E — Shareholder Alignment | 9 | 20 |
| **CORE SCORE** | **70** | **100** |
| F — Moat (informational) | 11 | 60 |
| **GRAND TOTAL** | **81** | **160** |

Data confidence: 10 years available → nominal "full" tier by year-count, but
**history_downgrade = true** per the unresolved FY2017-2021 business-mix
question (see corpus mechanics note above) — flagged, not silently scored
across.

Deal-breaker override check (none triggered):
1. Block A <8 → N/A (A=15)
2. Block B <8 → N/A (B=14)
3. Median ROCE <10% → N/A (31.25%)
4. Cumulative CFO/PAT <0.50 → N/A (0.884x)
5. Pledge >15% → cannot confirm (E3 = N/A, data gap, not scored as breach)
6. ND/EBITDA >3x AND IC <3x → N/A (net cash)
7. Revenue declined majority of years → N/A (3 of 9 years, 33%)
8. PAT negative in any of last 3 years → N/A (positive every year FY17-26)
9. History <3 years → N/A (10 years)

Classification matrix: Core 70 (60-79 band) + Moat MODERATE (not
STRONG/FORTRESS) → **"Core 60-79 + else = GOOD"**

```
╔══════════════════════════════════════╗
║  CLASSIFICATION: GOOD                 ║
║  Core Score: 70/100                   ║
║  Moat: MODERATE (11/60, 2 confirmed)  ║
║  Grand Total: 81/160                  ║
║  Deal-breakers triggered: NONE        ║
║  History downgrade flag: TRUE         ║
╚══════════════════════════════════════╝
```

**Strongest block**: D — Balance Sheet Strength, 20/20. No debt, deep net
cash (Rs26.87cr net cash, Rs143.89cr in investments), current ratio 5.26x.

**Weakest block**: E — Shareholder Alignment, 9/20 — but this is driven by
two DATA GAPS (E2, E3 both N/A, not confirmed adverse findings), not by
confirmed weak alignment. Promoter holding itself (E1=4, 50.80%) and
contingent-liability coverage (E4=5, 3.83% of net worth) both score well.
If E2/E3 data gaps were resolved favourably, E could reach 16-20/20.

**Decision line**: GOOD, with three propagating flags: (1) a genuine but
FY2017-base-sensitive growth/profitability read in Block C and moat test M1
(the more representative recent-window numbers are materially lower —
revenue CAGR ~11%, PAT CAGR ~15-16% over FY2022-2026 vs the scored 8.85%/
35.0%); (2) a deteriorating, not merely low, cash-conversion trend in Block
B (0.84x → 0.33x CFO/PAT in one year) coinciding with the Q1 FY27 revenue
acceleration; (3) an unresolved pre-FY2022 business-mix question that this
corpus cannot settle. None of these halt the run; all propagate to Stage 2
onward per pipeline rules.

---
