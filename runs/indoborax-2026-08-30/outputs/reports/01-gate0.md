# STAGE 1: GATE 0 SCORECARD — Indo Borax & Chemicals Ltd (INDOBORAX)
Run date: 2026-08-30 | Model: claude-sonnet-5 | Re-run (poppler now installed; Block E and spear facts closed from AR)

Data available: 10 years (FY2017 to FY2026). Scoring adapted to 10-year history.

Data sources used:
- screener-Data_Sheet.csv (primary numeric, P&L/BS/CF FY17-FY26 + quarterly)
- Q4 FY26 audited standalone + consolidated results filing (c98b4ce9…pdf), 22 pages, all read
- Q1 FY27 unaudited results filing (c59ebc11…pdf)
- Annual Report FY2025-26 (Annual_Report_2023.pdf — filename legacy, content confirmed 45th AGM, year ended 31-Mar-2026), pages 1-50 and 81-120 read directly this run
- India Ratings credit rating report, 23-Jul-2026 (rating.pdf)
- screener-shareholding-pattern.txt (SECONDARY tier, quarterly trend)
- companies/INDOBORAX.md (COMPANY MEMORY, weighed not anchored)

---

## GATE 0 CORRECTION LOG (this re-run vs prior impaired run)

The prior run scored Block E as 0/20 because pdftoppm was missing and the AR could not be
rendered. poppler-utils is now installed. This run read the AR directly (pages 1-50, 81-120)
and the Q4 FY26 results filing pages in full. Block E is now populated with real anchors.
Two spear facts (#1 imported-ore/export-NIL, #4 sponsor/affiliate-debt structure) are lifted
from SECONDARY to FILED. A drafting inconsistency in the AR's own ratio note (Note 45) was
found and is flagged rather than used.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Formula: ROCE = EBIT ÷ (Total Assets − Current Liabilities). For FY2025 and FY2026, the
company's own filed ROCE (AR p.113, Note 45, "Return on Capital Employed") is used per the
"use the source's own figure" rule. For FY2017-FY2024, screener's balance sheet does not
split "Other Liabilities" into current/non-current, so Capital Employed is computed as
Net Worth + Borrowings (screener convention), noted as an approximation — non-current
liabilities are immaterial (~15-16% of non-equity liabilities in the FY25/FY26 AR split, the
only years the split is disclosed), so the approximation is not expected to move any band.

| FY | EBIT/PBT+Int (₹cr) | Capital Employed (₹cr) | ROCE | Source |
|----|---|---|---|---|
| FY17 | 11.76 | 95.98 | 12.25% | computed, screener-data (Sales/PBT/Interest/Equity/Reserves/Borrowings rows) |
| FY18 | 20.52 | 104.59 | 19.62% | computed, screener-data |
| FY19 | 24.27 | 121.47 | 19.98% | computed, screener-data |
| FY20 | 22.41 | 138.34 | 16.20% | computed, screener-data |
| FY21 | 46.64 | 172.92 | 26.98% | computed, screener-data |
| FY22 | 50.04 | 207.18 | 24.15% | computed, screener-data |
| FY23 | 69.09 | 255.08 | 27.09% | computed, screener-data |
| FY24 | 52.27 | 293.44 | 17.81% | computed, screener-data |
| FY25 | — | — | **17.28%** | AR FY26 p.113, Note 45 (company's own filed ratio, previous-period column) |
| FY26 | — | — | **17.13%** | AR FY26 p.113, Note 45 (company's own filed ratio, current-period column) |

Independent cross-check for FY26: EBIT (PBT ₹6,580.96 lakh + Finance Cost ₹6.61 lakh) ÷
Capital Employed (Total Assets ₹40,283.91 lakh − Current Liabilities ₹1,556.13 lakh =
₹38,727.78 lakh) = 17.01%, close to the filed 17.13% (results filing p.9 & p.11, standalone).

**A1 Median ROCE**: sorted {12.25, 16.20, 17.13, 17.28, 17.81, 19.62, 19.98, 24.15, 26.98,
27.09}; median = (17.81+19.62)/2 = 18.72% → band 15-19.9% → **Score 3**

**A2 Minimum single-year ROCE**: 12.25% (FY17) → band 12-14.9% → **Score 3**

**A3 Median ROE**: ROE = PAT ÷ average Net Worth. Opening Net Worth unavailable for FY17;
FY17 uses closing Net Worth (stated). PAT and Net Worth per screener-data.
FY17 8.45% | FY18 13.46% | FY19 15.53% | FY20 13.05% | FY21 22.02% | FY22 19.15% |
FY23 21.94% | FY24 14.22% | FY25 13.52% | FY26 13.93%
Sorted median = (13.93+14.22)/2 = 14.08% → band 12-14.9% → **Score 2**

DATA QUALITY FLAG: AR p.113 Note 45 discloses the company's own "Return on Equity Ratio" as
15.50% (FY26) / 13.05% (FY25). These are numerically identical to the AR's own EPS figures
(₹15.50 and ₹13.05, Note 36 / results filing) — this looks like a copy-paste error in the AR's
ratio note, not an independent ROE calculation. It is NOT used as the A3 anchor; the
independently computed figures above (13.93% FY26 / 13.52% FY25, close to the AR error's
13.05% FY25 by coincidence only) are used instead.

**A4 ROCE trend, latest vs earliest**: FY26 17.13% ≥ FY17 12.25% → **Score 5**

**BLOCK A TOTAL: 13/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

Data-basis note: screener's CFO/PAT for FY25 and FY26 are CONSOLIDATED (cross-checked
exactly against the AR's consolidated P&L and cash flow statement — PAT ₹50.27cr / ₹42.51cr,
CFO ₹87.15cr / −₹104.47cr, all match to the rupee). FY17-FY24 predate the subsidiary
(IndoBorax Infrastructure Pvt Ltd, incorporated later) so standalone = consolidated for those
years. Basis is continuous.

Cumulative CFO (FY17-FY26, ₹cr): 20.58+1.2+14.75+13.18+15.75+11.48+60.25+69.49−104.47+87.15
= **189.36cr** (screener-data)
Cumulative PAT (FY17-FY26, ₹cr): 7.99+13.4+17.54+16.95+34.26+36.37+50.69+38.98+42.51+50.27
= **308.96cr** (screener-data)

**B1 Cumulative CFO ÷ Cumulative PAT** = 189.36/308.96 = 0.613 → band 0.50-0.69 → **Score 1**

Context (not score-changing, mechanical rule applied as-is): the single largest driver of the
low ratio is FY25's CFO of −₹104.47cr (consolidated) / −₹93.03cr (standalone, AR p.86,
Q4FY26 filing). The cash flow statement shows this is dominated by "(increase) in non-current
financial assets" −₹8,217.80 lakh and "(increase) in current financial assets" −₹3,109.87
lakh (Q4FY26 filing, standalone CF statement) — i.e., the company's large mutual-fund/bond
treasury portfolio churns through the operating section under Ind AS classification, not a
core-business collection failure. FY26 CFO recovered to +₹87.15cr.

**Capex** (purchase of PP&E + intangibles from cash flow statement, excl. acquisitions):
only available for FY25 and FY26 in the provided corpus (screener does not itemise capex;
AR FY24/FY25 not in corpus — input_gap: annual_report_fy24_fy25). FY17-FY24 capex is
N/A (not in provided data); FCF for those years cannot be computed and is not scored.

FY25: Capex ₹6.73cr (₹672.94 lakh, Q4FY26 filing p.9/p.11, standalone CF, comparative column)
FY26: Capex ₹0.29cr (₹29.11 lakh, Q4FY26 filing p.9/p.11, standalone CF, current column)

FCF (screener CFO basis) FY25 = −104.47 − 6.73 = **−111.20cr**
FCF (screener CFO basis) FY26 = 87.15 − 0.29 = **+86.86cr**

**B2 FCF-positive years as proportion** (of the 2 computable years): 1/2 = 50% → band
50-74% → **Score 2**. LOW CONFIDENCE — n=2 only, flagged, not treated as a 10-year trend.

**B3 Cumulative FCF ÷ Cumulative PAT** (matched period, FY25+FY26 only, since capex is only
known for these two years): FCF −24.34cr ÷ PAT 92.78cr = −0.262 → negative → **Score 0**

**B4 Change in WC Days, latest vs earliest available**: Trade Payables not in screener-data
for FY17-FY24 (input_gap), so WC Days is only computable for FY25 and FY26 (Q4FY26 filing,
standalone balance sheet notes and P&L revenue line).

FY25: Receivable Days 32.88 + Inventory Days 98.03 − Payable Days 11.30 = **119.61 days**
(Trade Receivables ₹1,578.73 lakh, Inventory ₹4,706.75 lakh, Trade Payables ₹542.42 lakh,
Revenue ₹17,526.11 lakh — all Q4FY26 filing p.9-p.11, revenue basis, comparative column)

FY26: Receivable Days 17.58 + Inventory Days 53.94 − Payable Days 5.25 = **66.27 days**
(Trade Receivables ₹1,037.92 lakh, Inventory ₹3,182.75 lakh, Trade Payables ₹309.66 lakh,
Revenue ₹21,545.11 lakh — Q4FY26 filing p.9-p.11, revenue basis, current column)

Note: this cross-confirms company-memory spear fact #2 (receivable days 33 FY25 / 18 FY26)
almost exactly (32.88 / 17.58) — SECONDARY figure now FILED via the results filing.

Change = 66.27 − 119.61 = **−53.34 days** (decreased) → band >5 days decrease → **Score 5**.
Only a 2-year comparison (input_gap limits the window); flagged.

**BLOCK B TOTAL: 8/20**

---

## BLOCK C: GROWTH (Max 20)

Revenue (screener-data, ₹cr): FY17 66.59 → FY26 215.38 (9-year window)
PAT (screener-data, ₹cr): FY17 7.99 → FY26 50.27

**C1 Revenue CAGR** = (215.38/66.59)^(1/9) − 1 = **13.93%** → band 10-14.9% → **Score 3**

**C2 PAT CAGR** = (50.27/7.99)^(1/9) − 1 = **22.67%** → band ≥20% → **Score 5**
(Sensitivity check: using core FY26 PAT ~₹42.07cr, computed by stripping the ₹10.15cr
exceptional at the standalone effective tax rate 24.42%, PAT CAGR is 20.27% — still ≥20%
band. The FY26 exceptional does not move this score. See data_notes.)

**C3 Positive YoY revenue years, proportion** (9 year-over-year comparisons, FY18-FY26):
Positive: FY18, FY19, FY21, FY22, FY23, FY26 (6). Negative: FY20 (−10.2%), FY24 (−15.0%),
FY25 (−8.4%) (3). Proportion = 6/9 = 66.7% → band 50-74% → **Score 1**

**C4 PAT CAGR − Revenue CAGR** = 22.67% − 13.93% = **+8.74pp** → band ≥+3pp → **Score 5**

**BLOCK C TOTAL: 14/20**

Deal-breaker 7 check: revenue declined in 3/9 years (33%), not a majority → not triggered.

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

All figures anchored to the Q4FY26 filing standalone Statement of Assets & Liabilities
(31-Mar-2026, p.9) and Statement of Cash Flow (p.11); cross-checked against the company's own
filed ratios at AR p.113, Note 45.

Total Assets FY26 ₹40,283.91 lakh; Current Liabilities FY26 ₹1,556.13 lakh; Current Assets
₹31,202.60 lakh; Total Equity ₹38,455.18 lakh; Borrowings: NIL (only lease liabilities,
₹142.99 lakh combined non-current + current, an IndAS 116 non-cash item, not bank/NCD debt).
Cash & equivalents ₹1,353.42 lakh + Current investments ₹18,535.82 lakh + other financial
assets → total liquid resources far exceed the ₹142.99 lakh lease liability.

**D1 Net Debt ÷ EBITDA (latest)**: net cash position (cash + investments ≈ ₹210cr vs debt
≈ ₹1.43cr) → **Score 5** (Q4FY26 filing p.9; rating.pdf p.2 "IBCL had no debt outstanding on
its books at FYE26")

**D2 Interest Coverage** = EBIT (PBT ₹6,580.96 + Finance Cost ₹6.61 = ₹6,587.57 lakh) ÷
Finance Cost ₹6.61 lakh = **997x** → band ≥10x → **Score 5** (Q4FY26 filing p.9)

**D3 Debt ÷ Equity** = ₹142.99 lakh ÷ ₹38,455.18 lakh = **0.0037** → band <0.1 → **Score 5**
(Cross-check: AR p.113 Note 45 shows the company's own Debt-Equity Ratio disclosure as nil/
blank both years, consistent.)

**D4 Current Ratio** = ₹31,202.60 lakh ÷ ₹1,556.13 lakh = **20.05x** → band ≥2.0 → **Score 5**
(Exact match to the company's own filed ratio, AR p.113 Note 45: Current Ratio 20.05
current / 8.64 previous period.)

**BLOCK D TOTAL: 20/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

**E1 Promoter holding, latest quarter (Jun-2026)** = **38.41%** (screener-shareholding-
pattern.txt, Jun-2026 row) → band 30-39.9% → **Score 1**

Cross-check: AR p.23 (Annexure A, Director Sunil Malhotra's shareholding table) states
Zenrock Chemicals Private Limited held 98,82,230 shares (30.80%) as at 31-Mar-2026 and
1,23,26,764 shares "as on date of this Notice" (post-notice date, post open-offer
completion). 1,23,26,764 ÷ 3,20,90,000 = 38.41% — exact match to the screener Jun-2026
figure and to company-memory spear item #6/#8 (24,44,534 shares acquired via open offer
04-May-2026: 98,82,230 + 24,44,534 = 1,23,26,764). This lifts the promoter build-up chain to
FILED tier.

**E2 Promoter holding change over ~3 years**: earliest available point in the corpus is
Sep-2023 (52.07%, screener-shareholding-pattern.txt), 2.75 years before Jun-2026, used as the
best available proxy for "3 years" (stated per formula rule: use available history). Change
= 38.41% − 52.07% = **−13.66pp** → band decreased >3% → **Score 0**

IMPORTANT CONTEXT (does not change the mechanical score): this decline is NOT organic
promoter selling. It is a control transaction. AR p.32 ("Material Changes/Events") discloses
a Share Purchase Agreement dated 15-Dec-2025 in which Zenrock Chemicals Pvt Ltd + India
Special Assets Fund III + ISAF III Onshore Fund + Special Situation India Fund acquired
1,63,00,230 shares (50.80% of equity) from the erstwhile Jain-family promoter group, followed
by an open offer for up to 83,43,400 shares (26.00%) of which 24,44,534 were actually
tendered and acquired (04-May-2026). The reclassification (Zenrock as new promoter at 30.80%
→ 38.41%; the three AIFs remaining at ~20.00% combined as non-promoter institutional holders,
per AR p.101 Note 16(c)/(d) shareholders->5% table) explains the shareholding-pattern
discontinuity seen at Mar-2026/Jun-2026 in the screener trend.

**E3 Promoter pledge (latest)**: **100%** of the promoter (Zenrock) shareholding is pledged
to secure Zenrock's acquisition-level debt (rating.pdf p.1: "100% pledge of Zenrock's
shareholding"; p.3: "The rating is constrained by the 100% pledge of the promoter
shareholding held by Zenrock Chemicals Private Limited (ZCPL) in IBCL. The pledge was
created to secure promoter-level acquisition financing... does not form part of the
company's standalone borrowings.") → band >15% → **Score 0**

**E4 Contingent Liabilities ÷ Net Worth (latest)**: Contingent liability (Note 46, AR p.113)
= ₹1.65 lakh bank guarantee (STC of India Ltd claim, both current and previous year). Net
Worth FY26 = ₹38,455.18 lakh (Q4FY26 filing p.9). Ratio = 0.0165cr ÷ 384.55cr = **0.0043%**
→ band <5% → **Score 5**

Related note (not a contingent liability, excluded from this ratio, flagged separately):
Note 47, AR p.113 — an Inter Corporate Deposit of ₹509.04 lakh (₹5.09cr) to Radius Estate
Projects Pvt Ltd (formerly Vishwaroop Realtors) is under IBC insolvency proceedings and
doubtful of recovery; no interest accrued FY26; also flagged as an Emphasis of Matter in the
statutory auditor's report (Q4FY26 filing p.2/p.14). Small relative to net worth (~1.3%) but
an asset-quality item worth carrying forward.

**BLOCK E TOTAL: 6/20**

Deal-breaker 5 check: pledge 100% > 15% → **TRIGGERED, caps classification at max AVERAGE.**
Driving fact: current-state (as at 23-Jul-2026 rating report; pledge share count 1,23,26,764
matches company-memory spear item #7 exactly) — this is a post-acquisition financing
structure, not a distressed legacy promoter pledge. The scorecard applies the rule
mechanically regardless of context; the context is carried forward for the operator.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Clean operating EBITDA margin series used where available (company memory, cross-checked
against rating.pdf: FY24 21.6% / FY25 26.18% (rating.pdf p.4) / FY26 20.50% (rating.pdf p.4)).

**M1 Pricing Power**: margin FY24→FY26 21.6%→20.5% (declined ~1.1pp, not ≥2pp); revenue
CAGR over same window (FY24 ₹191.29cr → FY26 ₹215.38/215.45cr) = 6.11%, <10% →
**Score 0**

**M2 Cost Advantage vs peer median EBITDA margin**: no peer data in provided corpus →
**Score 0 — PEER DATA NEEDED**

**M3 Capital Efficiency**: FAT (Revenue ÷ Net Block) FY26 = 215.38/47.61 = 4.52x; ROCE FY26
17.13%. FAT>2x AND ROCE>15% → **Score 3**. Caveat: FY26 Net Block fell from ₹100.92cr to
₹47.61cr mainly because of the RPT asset sale to exiting promoters (AR p.42, Annexure III),
not organic fixed-asset efficiency improvement — flagged, not treated as a durable moat
signal.

**M4 Customer Stickiness**: 3 revenue-decline years in the 9-year YoY series (FY20, FY24,
FY25) → band "3+ decline years" → **Score 0**

**M5 Scale & Dominance**: rating.pdf states ~50% market share in the steel/refractory boric
acid segment (qualitative), but no quantified peer mcap/margin comparison in corpus →
**Score 0 — PEER DATA NEEDED**

**M6 Technology/R&D**: AR p.29/p.32 and rating.pdf both state the company has no dedicated
R&D department → R&D/Revenue effectively 0% → **Score 0**

**M7 Regulatory/License**: company is the sole India manufacturer of IP-grade boric acid with
an FDA licence and BIS certification for technical-grade boric acid (rating.pdf p.2) — a
genuine niche-license position, but the number of listed players in the segment is not
quantified in corpus → **Score 0 — PEER DATA NEEDED** (flagged as likely under-scored
given the qualitative strength of the disclosure; the framework requires a counted figure,
not an inference, so 0 stands per rule "never guess peer figures")

**M8 Distribution**: no quantified dealer/distribution network disclosed in corpus →
**Score 0**

**M9 Brand**: Gross margin proxy (Revenue − Raw Material Cost) ÷ Revenue: FY26 45.63%,
FY25 53.22% (screener-data). No peer GM median in corpus → **Score 0 — PEER DATA NEEDED**

**M10 Switching Costs**: overall revenue growth (FY17→FY26 positive) with 3 decline years
(≥2) → band "overall growth, 2+ decline years" → **Score 1**

**M11 Network Effects** (10-year history, ≥6yr test applies): latest 3yr revenue CAGR
(FY23→FY26: ₹225.04cr→₹215.38cr) = −1.45%; prior 3yr CAGR (FY20→FY23: ₹115.25cr→₹225.04cr)
= 25.02%. Latest is NOT greater than prior, and latest is negative (not ≥20% or >15%) →
**Score 0**

**M12 Negative WC/Float**: WC Days computable only FY25 (119.61) and FY26 (66.27), both >45
→ **Score 0**

**MOAT TESTS SUMMARY**: M1=0, M2=0(PDN), M3=3, M4=0, M5=0(PDN), M6=0, M7=0(PDN), M8=0,
M9=0(PDN), M10=1, M11=0, M12=0
**BLOCK F TOTAL: 4/60**
Moats "present" (score ≥3): M3 only → **moats_confirmed = 1**
Classification: 1 present → **THIN**

---

## SCORECARD DASHBOARD

```
BLOCK                          SCORE     BAR
A. Return on Capital           13/20     [########------------]
B. Cash Generation Quality      8/20     [#####---------------]
C. Growth                      14/20     [#########-----------]
D. Balance Sheet Strength      20/20     [####################]
E. Shareholder Alignment        6/20     [######---------------] (deal-breaker triggered)
                                ----
CORE SCORE                     61/100

F. Quantitative Moat            4/60     [##------------------]
MOAT CLASS: THIN (1/12 tests present, ≥3 threshold: M3 Capital Efficiency only)

GRAND TOTAL (Core + Moat)      65/160
```

**Strongest block: D — Balance Sheet Strength (20/20).** Debt-free, net cash of roughly
₹210cr against a ₹1.43cr lease liability, current ratio 20x, interest coverage ~1,000x — all
independently cross-checked against the company's own filed Note 45 ratios, which match to
within rounding.

**Weakest block: E — Shareholder Alignment (6/20).** Driven entirely by the 100% pledge
(deal-breaker 5) and the promoter-holding discontinuity from the control transaction, not by
weak contingent-liability discipline (E4 scored a clean 5/5).

---

## DATA CONFIDENCE AND CLASSIFICATION

Data confidence: 10 years available → **10+ yrs full**, no history-based downgrade.

Classification matrix: Core 61 (band 60-79) + Moat THIN → matrix result = **GOOD**.

**Deal-breaker overrides checked:**
1. Block A<8 → not triggered (A=13)
2. Block B<8 → not triggered (B=8, exactly at threshold, not below it)
3. Median ROCE<10% → not triggered (18.72%)
4. Cumulative CFO/PAT<0.50 → not triggered (0.613)
5. **Pledge>15% → TRIGGERED (100% pledge, rating.pdf).** Caps classification at max AVERAGE.
6. ND/EBITDA>3x AND IC<3x → not triggered (net cash, IC ~997x)
7. Revenue declined majority of years → not triggered (3/9)
8. PAT negative in any of last 3 years → not triggered (all positive)
9. History<3 years → not triggered (10 years)

**FINAL CLASSIFICATION: AVERAGE** (matrix result GOOD, capped by deal-breaker 5)

---

## SPEAR FACT VERIFICATION (lifted from SECONDARY to FILED this run)

**Spear fact #1** — "Imported ore Rs 96.26 cr vs revenue Rs 175.26 cr FY25 (55%); export
earnings NIL FY24 and FY25": **CONFIRMED FILED for FY25/FY26** via AR FY26 p.33, Board's
Report "C. Foreign Exchange Earnings and Outgo" table: Inflow — NIL both FY25 and FY26
(dash, no exports); Outflow ₹9,626.55 lakh (₹96.27cr) FY25, ₹6,625.52 lakh (₹66.26cr) FY26.
₹96.27cr / ₹175.26cr revenue = 54.9% ≈ 55%, matching the spear claim closely (the ₹0.01cr gap
to the quoted ₹96.26cr is immaterial, likely a sourcing/rounding difference from the prior
pass's AR FY25 read). FY24 itself is not independently confirmable — the FY24 AR is not in
this corpus (input_gap: annual_report_fy24_fy25) — but the FY25 comparative in this AR
supports the pattern.

**Spear fact #4** — "Sponsor is EAAA/Edelweiss; acquisition debt is affiliate debt (Rs 390cr
NCD + Rs 75cr CCPS in Zenrock), NOT on Indo Borax's own balance sheet; Indo Borax remains
debt-free": **CONFIRMED FILED**. rating.pdf p.3: "The acquisition was funded through the
issuance of secured NCDs worth INR3,900 million and compulsorily convertible preference
shares worth INR750 million at the promoter level [ZCPL]." p.4: "At the promoter level, ZCPL
had raised NCDs for acquisition financing, which do not form part of IBCL's standalone
borrowings... ZCPL has repaid around INR1,350 million of NCD principal, reducing the
outstanding amount to around INR2,550 million, with a bullet repayment due in FY31." Indo
Borax's own balance sheet (Q4FY26 filing, AR Note 45) shows zero bank/NCD borrowings at
FY26 close, and rating.pdf p.2 explicitly states "IBCL had no debt outstanding on its books
at FYE26." Q1 FY27 (30-Jun-2026): the quarterly results filing does not disclose a balance
sheet (not mandatory under Reg 33 for non-half-year quarters), so a direct Q1FY27 balance
sheet confirmation is NOT FOUND in corpus; the rating report (23-Jul-2026, three weeks after
Q1 close) reaffirms "no scheduled debt repayment obligations at the standalone level,"
supporting continuity of the debt-free position through the rating date.

**Bonus finding (beyond the two requested spear facts), material to the mental model**: the
AR (p.32, p.113 Note 49) discloses the actual SPA terms for Indo Borax itself: 1,63,00,230
shares (50.80%) acquired at ₹256.30/share on 15-Dec-2025 by Zenrock + the three AIFs
collectively, followed by an open offer for up to 83,43,400 shares (26.00%), of which
24,44,534 were tendered (04-May-2026, ~29% take-up). This confirms company-memory spear
items #6 and #8 are FILED-tier consistent, and clarifies that company-memory's FIRST
VERIFICATION PRIORITY items #1-#2 (2,38,44,000 shares / 64.26% at ₹103.22; 95,70,000 shares
open offer at ₹157.27) do NOT belong to Indo Borax — those share counts do not reconcile to
Indo Borax's 3,20,90,000 total shares outstanding, but do reconcile to a target with roughly
3.71cr total shares. They almost certainly describe the Kronox Lab Sciences acquisition
referenced elsewhere in the mental model, a different listed entity in the same sponsor's
roll-up. This should be corrected in company memory to avoid conflating the two deals.

**Spear items #5 (ESOP 16,88,950 options) and Rs700cr Section 186 envelope**: ESOP figure
CONFIRMED FILED (AR p.34: "On May 8, 2026... approved ESOP 2026 for issuance of 16,88,950
Employee Stock Options"). The ₹700cr Section 186 limit itself was not located in the notes
read this run and remains reliant on the postal ballot notice (input_gap:
postal_ballot_notices, not in corpus).

**Item #9 (Q4 FY26 split of the ₹10.15cr exceptional)**: CONFIRMED FILED. Q4FY26 filing p.7:
"Exceptional Item" = ₹80.03 lakh for the three months ended 31-Mar-2026, vs ₹1,014.75 lakh
(₹10.15cr) for the full year. So ~₹9.35cr of the ₹10.15cr exceptional occurred in Q1-Q3
FY26, not Q4 — the bulk of the RPT asset-sale gain was booked earlier in the year (AOC-2
dates of execution: property 22-Jan-2026, office 29-Sep-2025, vehicles 10-Jan-2026 — Q3/Q4
weighted, consistent).

**Item #10 (FY26 closing cash + investments after the ₹128cr dividend)**: PARTIALLY
VERIFIED. AR p.112 Note 44 "Dividends not recognised at the end of the reporting period" =
₹12,836.00 lakh (₹128.36cr), which is exactly ₹40/share × 3,20,90,000 shares — confirming the
dividend size and that it was NOT YET paid/recognised as a liability at the 31-Mar-2026
balance date (still sitting inside the FY26 closing cash+investments of ~₹210cr, standalone).
The actual post-payment cash position is NOT FOUND in the provided corpus: Q1 FY27 quarterly
results do not disclose a balance sheet (structural gap under Reg 33), and rating.pdf
(23-Jul-2026) indicates the payout was still pending/being planned for FY27 rather than
already executed.

---

## INPUT GAPS CARRIED FORWARD

- annual_report_fy24_fy25 (only the FY26 AR is in corpus; limits capex/FCF/WC-days history
  to 2 years and blocks independent FY24 confirmation of spear fact #1)
- postal_ballot_notices (blocks confirmation of the ₹700cr Section 186 envelope)
- shareholding_reg31_filing (screener aggregate and AR point-in-time snapshots are used;
  exact current promoter sub-classification as of Jun-2026 — Zenrock vs the three AIFs
  individually — is inferred by arithmetic reconciliation, not read directly from a Reg 31
  filing for that quarter)
- Q1 FY27 balance sheet (not disclosed in the quarterly filing under Reg 33; blocks item #10)

freshness_verdict: CORPUS GAPPED-FRESHNESS

---

## ANALYST NOTE

Classification computed as GOOD (Core 61/100, THIN moat) but capped to AVERAGE by
deal-breaker 5: promoter shareholding is 100% pledged (rating.pdf, 23-Jul-2026), securing
Zenrock's acquisition-level NCD/CCPS debt, not operating distress. E1/E2 promoter-holding
decline reflects the Dec-2025 SPA and 2026 open offer control transaction, not entrenched-
promoter selling — a different risk signature than the scorecard's design intent, worth
weighing qualitatively downstream. Block D is a clean 20/20: debt-free, net cash ~₹210cr,
current ratio 20x, matches the company's own filed ratios (AR Note 45) almost exactly.
Block B's weak 8/20 stems mostly from one distorted year: FY25 CFO of −₹104.47cr is a
treasury/investment-portfolio classification effect, not a core cash-conversion failure;
FCF is only computable for FY25-26 since capex history pre-FY25 is not in corpus. FY26 PAT
includes a disclosed ₹10.15cr exceptional (property/vehicle sale to exiting promoters, AR
p.24/p.42); core PAT is ~₹42cr, but this does not change any score band. Moat is THIN
(4/60): only capital efficiency scores present, and it is inflated by the same asset sale
that shrank net block. Four moat tests are marked PEER DATA NEEDED, including the licence
test (M7), which is likely under-scored given the qualitative strength of the FDA/BIS
disclosure but cannot be scored without a counted peer figure.

---

```yaml
stage: B01-gate0
company: "INDOBORAX"
run_date: "2026-08-30"
model: claude-sonnet-5
status: complete
input_gaps: [annual_report_fy24_fy25, postal_ballot_notices, shareholding_reg31_filing]
flags:
  - {type: FLAG-GATE0, reason: "Classification capped at AVERAGE by deal-breaker 5 (promoter pledge 100%, rating.pdf p.1/p.3-4); the matrix-computed classification before override was GOOD (Core 61/100 + THIN moat). Pledge secures Zenrock's acquisition-level NCD/CCPS debt, not Indo Borax operating distress."}
  - {type: FLAG-CASH, reason: "Cumulative CFO/PAT 0.61x (10yr, screener/AR-consolidated basis) driven almost entirely by FY25 CFO of -Rs104.47cr, a treasury/investment-portfolio cash-flow classification effect (AR/Q4FY26 CF statement), not core operating distress. FCF-based B2/B3 rest on only 2 years of disclosed capex (FY25-FY26); pre-FY25 capex not in corpus."}
data_years: 10
fy_range: "FY17 to FY26"
blocks: {A: 13, B: 8, C: 14, D: 20, E: 6}
core_score: 61
moat_score: 4
grand_total: 65
moats_confirmed: 1
moat_class: "THIN"
classification: "AVERAGE"
deal_breakers: ["5: pledge>15% (100% of promoter Zenrock shareholding pledged, rating.pdf 23-Jul-2026) -> capped matrix result GOOD down to max AVERAGE"]
history_downgrade: false
data_notes:
  - "Screener CFO/PAT for FY25-FY26 are consolidated (verified exact match to AR consolidated P&L/CF); FY17-FY24 predate the subsidiary and are effectively standalone=consolidated."
  - "FY26 reported PAT (Rs50.27cr consol / Rs49.74cr standalone) includes a Rs10.15cr exceptional (AOC-2 sale of residential property Rs42.50cr + office Rs14.00cr + 3 vehicles Rs5.52cr to the exiting Sajal Jain promoter family, AR p.24 and p.42). Core FY26 PAT computed as ~Rs42.1cr (PBT before exceptional Rs55.66cr standalone x (1-24.42% effective tax rate)). PAT CAGR score (C2) unaffected: raw 22.67% and core-adjusted 20.27% both fall in the >=20% band."
  - "ROCE for FY25/FY26 anchored to the company's own filed disclosure (AR p.113 Note 45); ROCE for FY17-FY24 computed via screener capital-employed convention (Net Worth + Borrowings) since the current/non-current liability split is not in screener-data for those years."
  - "AR p.113 Note 45's own 'Return on Equity Ratio' (15.50% FY26 / 13.05% FY25) is numerically identical to the AR's own EPS figures -- an apparent drafting error in the filed ratio note. Not used as the A3 anchor; independently computed ROE used instead (13.93% FY26 / 13.52% FY25)."
  - "WC Days (B4) computable only for FY25 vs FY26 (Trade Payables not in screener-data pre-FY25); the -53.34 day swing is a genuine 1-year change, not a multi-year trend."
  - "Company-memory spear items #1-#2 (Kronox share counts/prices) do not reconcile to Indo Borax's own 3,20,90,000 shares outstanding; they belong to the Kronox Lab Sciences acquisition by the same sponsor group, a separate entity. Recommend correcting company memory to avoid conflation."
block_b_trend: "improving - CFO swung from -Rs104.47cr (FY25, consolidated) to +Rs87.15cr (FY26, consolidated), a +Rs191.62cr change, driven by reversal of investment-portfolio/treasury cash-flow timing effects rather than core operating improvement"
analyst_note: "Classification computed as GOOD (Core 61/100, THIN moat) but capped to AVERAGE by deal-breaker 5: promoter shareholding is 100% pledged (rating.pdf, 23-Jul-2026), securing Zenrock's acquisition-level NCD/CCPS debt, not operating distress. E1/E2 promoter-holding decline reflects the Dec-2025 SPA and 2026 open offer control transaction, not entrenched-promoter selling, a different risk signature worth weighing qualitatively downstream. Block D is a clean 20/20, matching the company's own filed Note 45 ratios almost exactly. Block B's weak 8/20 stems mostly from one distorted year: FY25 CFO of -Rs104.47cr is a treasury/investment-portfolio classification effect, not core cash-conversion failure; FCF is only computable for FY25-26. FY26 PAT includes a disclosed Rs10.15cr exceptional (property/vehicle sale to exiting promoters); core PAT is ~Rs42cr, but this does not change any score band. Moat is THIN (4/60): only capital efficiency scores, inflated by the same asset sale that shrank net block. Four moat tests are PEER DATA NEEDED, including the licence test (M7), likely under-scored given the FDA/BIS disclosure but not scorable without a counted peer figure."
```
