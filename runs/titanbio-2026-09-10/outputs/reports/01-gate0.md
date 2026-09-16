# STAGE 1 — GATE 0 SCORECARD: Titan Biotech Ltd (TITANBIO)
## CORRECTION RUN (supersedes the 2026-09-16 original in place)

Run date: 2026-09-16 (correction pass)

---

## CORRECTION LOG

An audit re-derived this scorecard against its own rubric. Each finding was
independently recomputed from the sources before acceptance. Results:

**1. CRITICAL — Block B, test B4, and the WC-days table. CONFIRMED, corrected.**
Payable Days was computed with revenue converted lakh-to-crore by a factor
of 10, not 100. Proof: FY25 Payable Days (121.68) implies Trade Payables of
Payable Days x Revenue / 365 = 121.68 x 156.45 / 365 = Rs 52.15 cr, but the
FY25 Trade Payables actually used elsewhere in this same report is Rs
521.65 lakh = Rs 5.2165 cr, and FY25 Total Current Liabilities is Rs
1,773.64 lakh = Rs 17.74 cr. Rs 52.15 cr payables cannot fit inside Rs
17.74 cr of total current liabilities — the original figure is impossible.
Recomputing Payable Days on the correct lakh basis (Trade Payables lakh /
Revenue lakh x 365, e.g. FY25 = 521.65 / 15,645 x 365 = 12.17, exactly
1/10th of the original 121.68) and rebuilding WC Days = Recv + Inv − Pay
with the unchanged Recv/Inv day figures gives FY23 130.85, FY24 135.39,
FY25 150.05, FY26 (adjusted) 127.67 — all four independently reproduced
here and matching the audit's figures exactly. Change FY26 vs FY23 =
127.67 − 130.85 = −3.18 days, a decrease of 3.18 days, inside the ±5-day
band. **B4 corrected 5 → 3. Block B corrected 17 → 15. Core score
corrected 81 → 79.**

**2. MAJOR — Block F, test M12. CONFIRMED, corrected.**
M12 uses the same WC-days series. Corrected values (130.85 / 135.39 /
150.05 / 127.67) exceed 45 days in all four years — none negative, none
in 0-15, none in 15-45. Band ">45 = 0" applies in every year, so the test
resolves cleanly to 0 with no ambiguity. **M12 corrected 1 → 0. Moat score
corrected 15 → 14. Moat class recomputed: moats present (score ≥3) are
still only M1 and M3 (M12's move from 1 to 0 crosses no ≥3 threshold), so
moat class stays MODERATE (2 present), unchanged. Grand total corrected
96 → 93.**

Downstream effect on classification: Core score 79 falls out of the
"≥80" row into the "60-79" row. Core 60-79 + MODERATE (not
STRONG/FORTRESS) → **GOOD** (matrix's "else" branch), not GOOD+.
**Classification corrected GOOD+ → GOOD.**

**3. MAJOR — `block_b_trend` and `analyst_note`. CONFIRMED, rewritten.**
Both asserted a WC-days swing from +4.26 to −12.40 and a "working-capital
release." The corrected series shows WC days rose from 130.85 (FY23) to a
peak of 150.05 (FY25) then eased to 127.67 (FY26 adjusted) — a net
decrease of only 3.18 days over the full window, not a swing to negative
and not a release. Rewritten below to state this; the FCF series
observation and the FY26 treasury-investment observation, which the
correction does not touch, are kept.

**4. MINOR — Block F, tests M5 and M7. Marker added, no score change,
one factual correction to the audit's own premise.**
M7 (Regulatory/License) scored 0 on data genuinely absent from the corpus
(segment player count, licensing barrier) — this is peer/segment data the
Block F instruction requires marking "PEER DATA NEEDED" when absent, and
the marker was omitted. Added below; score unchanged at 0.
M5 (Scale & Dominance): the audit's premise that "M5 scored 0" does not
match this report, which scored M5 = 1 (the "top 5 mcap" band), not 0 —
verified by re-reading the M5 line as originally written. The substantive
point still holds: M5's full "largest mcap in segment" / "top 3 mcap"
bands cannot be tested because segment-wide mcap and margin ranking beyond
the 3 auto-selected peers is NOT FOUND, so the same "PEER DATA NEEDED"
marker is warranted and added for transparency. No score change (M5
stays 1, per the audit's own instruction that this finding carries no
score effect).

**5. MINOR — `data_years` field. CONFIRMED, clarified (no score effect).**
`data_years: 10` is accurate only for the metrics that use the full
screener-data window (B1, C1-C4). Block A (A1-A4, ROCE/ROE) and Block B's
B2-B4 (capex, FCF, WC-days) rest on the FY23-FY26 AR-anchored window only,
because the corpus holds three annual reports (FY24, FY25, FY26), each
carrying a two-year comparative, and no FY17-FY22 balance-sheet or capex
granularity exists anywhere in the corpus. The effect of a longer window
on A1 (median ROCE) or A2 (minimum single-year ROCE) was NOT tested and
is NOT FOUND — it is not estimated. Clarified in the opening paragraph and
in `data_notes` below; `data_years`/`fy_range` left at 10 / FY17-FY26
because that is the true window for the metrics that do use it (B1,
C1-C4), with the per-block window stated explicitly at every line, as in
the original report.

**Unchanged, carried forward exactly as before (not questioned by the
audit and not contradicted by this recomputation):** the FLAG-REVENUE-BASIS
finding (freight gross-up), the FLAG-ASSOCIATE-RECON finding, the TM
Media / Titan Media resolution, the FY26 investing-outflow split finding,
all of Blocks A, C, D, E, and moat tests M1-M4, M6, M8-M11.

---

Data sources: screener.in Data_Sheet CSV (FY2017-FY2026, consolidated basis —
verified below), BSE results filings (Q1FY27, FY26 audited, Q3FY26), three
annual reports (AR FY2024, AR FY2025, AR FY2026). BSE scrip 524717. CMP Rs 437,
market cap Rs 1,805.66 cr (screener-data, as of 2026-09-10).

Data available: 10 years (FY2017 to FY2026) for revenue/PAT/CFO series
(screener-data). Balance-sheet-granularity metrics (precise ROCE, ROE,
Trade Payables, WC days) draw on AR-disclosed figures, available for 4 years
(FY2023-FY2026) because only three annual reports (FY24, FY25, FY26) are in
the corpus and each shows a two-year comparative. Scoring adapted
accordingly: growth/cash-flow blocks (B1, C1-C4) use the full 10-year
window; return and working-capital-day metrics (A1-A4, B2-B4) use the
4-year AR-anchored window, stated at each line. The `data_years: 10` /
`fy_range: FY17-FY26` fields describe the window used by the growth/cash
metrics only; Block A and B2-B4 are 4-year (FY23-FY26) reads. No
FY17-FY22 balance-sheet or capex detail exists in the corpus, so the
effect of a longer window on A1 (median ROCE) or A2 (minimum ROCE) was
not tested and is not estimated — NOT FOUND, left as such.

The screener Data_Sheet CSV is CONSOLIDATED (verified: FY26 Net Profit
30-day: 29.89 cr = consol "Profit for the period" Rs 2,988.52 lakh, AR FY26
p.161, not the standalone Rs 2,744.72 lakh, AR FY26 p.161).

---

## RUN'S FIRST VERIFICATION PRIORITY — findings before scoring

### 1. Freight gross-up in revenue — CONFIRMED, NOT like-for-like

Every FY26 and Q1FY27 filing carries the identical note: "Freight amount has
been added in revenue from operations for the purpose of calculation of
sales including GST in current year. Freight also added in total in other
expenses to neutralise the impact of its addition in revenue in current
year." (Q3FY26 results p.4 line ref; FY26 audited results p.4-5; Q1FY27
results p.4 — all texts, standalone and consolidated notes).

Cartage & Freight Outward: Rs 584.41 lakh FY26 vs Rs 426.95 lakh FY25 (AR
FY26 p.138, Note on Selling & Distribution Expenses, both standalone and
consolidated).

Cross-check: AR FY2025 (the FY25 annual report, filed before this policy
note existed) reports Cartage & Freight Outward FY25 = Rs 426.95 lakh and
FY24 = Rs 376.59 lakh (AR FY25 p.135/p.171) — IDENTICAL to the FY25
comparator shown in the FY26 AR. No search hit for "freight...added to
revenue" or "neutralise" anywhere in AR FY2025.txt. This confirms the FY25
comparator was NOT restated: FY26 revenue (Rs 20,619.03 lakh domestic +
overseas, AR FY26 p.142) carries the freight gross-up; FY25 (Rs 15,645.08
lakh, AR FY26 p.142 and AR FY25 p.105, identical both times) does not.

Like-for-like basis established: FY26 revenue ex-gross-up = Rs 20,619.03
lakh − Rs 584.41 lakh = Rs 20,034.62 lakh = Rs 200.35 cr (assumes the entire
Cartage & Freight Outward line is the amount added to revenue; freight
INWARD, Rs 65.99 lakh, is a manufacturing-overhead item unrelated to
customer billing and is not part of the gross-up per the note's wording).

- Reported FY26 revenue growth: 206.19 / 156.45 − 1 = 31.79%
- Like-for-like FY26 revenue growth: 200.35 / 156.45 − 1 = 28.06%

This like-for-like adjusted revenue (Rs 200.35 cr) is used as the FY26
anchor for every growth and margin score below (C1, C4, M1, M9, M11); the
reported figure (Rs 206.19 cr) is shown alongside for reference. Because
the gross-up nets to zero at the PBT/PAT line (equal add to revenue and to
"other expenses"), it does not distort EBITDA in rupee terms, only revenue
growth % and margin %.

Note for context, not scored: Q1FY27 vs Q1FY26 (screener-data quarterly,
59.17 cr vs 46.50 cr, +27.25%) is likely already like-for-like, since the
freight note also appears embedded in FY26's full-year filing (implying the
practice ran through all of FY26, including Q1FY26); both quarters being
compared would then sit on the same (gross-up) basis. Not independently
confirmed for Q1FY26 specifically (no Q1FY26 filing in corpus) — flagged as
a residual gap, not scored.

### 2. Peptech Biosciences associate reconciliation — FOUND

AOC-1 Form B (AR FY26 p.80): Peptech Biosciences Ltd, 36.87% held, cost Rs
1,230.01 lakh, net worth attributable Rs 7,432.90 lakh, "Profit/Loss for
the year — considered in Consolidation" = Rs 651.12 lakh. Titan Media Ltd,
48.44% held, cost Rs 406.89 lakh, net worth attributable Rs 830.39 lakh,
profit considered = Rs 7.71 lakh. Combined AOC-1 "profit considered" =
Rs 658.83 lakh.

The Consolidated Statement of Profit and Loss (AR FY26 p.161) shows the
actual bridge explicitly:
- IX. "Profit for the period (VII-VIII)" [pre-associate] FY26 = Rs 2,744.72
  lakh, FY25 = Rs 1,827.11 lakh — this FY26 figure is IDENTICAL to
  standalone PAT (Rs 2,744.72 lakh), confirming standalone and
  pre-associate-consolidated profit are the same line.
- "Share in profit of associate" FY26 = Rs 243.80 lakh, FY25 = Rs 326.05
  lakh (AR FY26 p.161).
- "Profit for the period" [post-associate, final] FY26 = Rs 2,988.52 lakh,
  FY25 = Rs 2,153.16 lakh.

2,744.72 + 243.80 = 2,988.52. Exact match. The Rs 2.44 cr gap the task
flagged is fully explained: it is the "Share in profit of associate" line,
not the full AOC-1 profit-considered figure.

Unresolved sub-question (named, not guessed): the AOC-1 "profit considered"
of Rs 658.83 lakh is Rs 415.03 lakh larger than the Rs 243.80 lakh actually
picked up in the P&L. The notes do not itemise this gap. A plausible
mechanism is Ind AS 28 unrealised-profit elimination on the Rs 389.38 lakh
of FY26 related-party revenue from Titan Biotech to Peptech (AR FY26 p.144,
Related Party Disclosures — Revenue from Operations, Peptech Biosciences
Ltd Associate, Rs 389.38 lakh FY26 vs Rs 493.93 lakh FY25), proportional to
Titan's 36.87% stake, until Peptech resells the input downstream — but this
specific elimination is NOT FOUND stated in the notes. Flagged, not scored
as a defect.

Consolidated basis is confirmed as the more complete earnings base (it
includes the associate pickup); the gap between standalone and consolidated
PAT is small (Rs 2.44 cr on a base of ~Rs 27-30 cr) and does not change
which basis this scorecard should use — consolidated, per the CSV.

### 3. TM Media vs Titan Media Ltd — RESOLVED, no overlap

"TM Media" (AR FY26 p.100, MD&A: "Titan Biotech (TM Media) leading the way
in manufacturing and supplying...") is Titan Biotech's OWN in-house brand
name for its culture-media product line. It is not a separate legal entity
and its revenue sits inside the reported consolidated P&L.

"Titan Media Limited" is a separate 48.44%-held ASSOCIATE (AR FY26 p.75,
Related Party list; p.164, Note 1.1: "The principal activities of the
associate company 'Titan Media Limited' is in the business of laboratory
chemicals"). Its business (laboratory chemicals) is unrelated to Titan
Biotech's own culture-media (TM Media) line. Peptech Biosciences' principal
activity, for contrast, is "manufacturing of Bio-Fertilizers, Bio-pesticides,
Bio-insecticides" (AR FY26 p.164).

Finding: coincidental name overlap only. No part of the culture-media
engine sits outside the consolidated P&L because of this naming; Titan
Media Ltd is a different business entirely, captured only via the (small,
Rs 7.71 lakh) associate-profit pickup.

### 4. FY26 investing outflow split — FOUND, dominated by portfolio investments

AR FY26 Consolidated Cash Flow Statement (p.162): Net cash used in
investing activities FY26 = Rs 3,254.59 lakh (Rs 32.55 cr); FY25 = Rs 985.33
lakh (Rs 9.85 cr). The standalone CFS (p.116) shows the same Rs 3,254.59
lakh / Rs 985.34 lakh. This is close to, but does not exactly match, the
screener-data aggregate of Rs 34.41 cr FY26 / Rs 9.87 cr FY25 — a residual
variance of about Rs 1.86 cr FY26 whose source is NOT FOUND in the provided
extracts (possibly a different treatment of bank-deposit movements between
screener's aggregation and the AR line items).

Split of the AR FY26 Rs 3,254.59 lakh outflow:
- "Investments in debt instruments and equity instruments": Rs 2,515.67
  lakh (Rs 25.16 cr, ~77% of the outflow) — financial-asset purchases.
- "Purchase of PP&E including CWIP" Rs 742.83 lakh, less "Proceeds from
  sale of PP&E" Rs 0.43 lakh, plus "Purchase of other intangible assets"
  Rs 0 = net capex Rs 742.40 lakh (Rs 7.42 cr, ~23%).

Cross-check via the Investments note (AR FY26 p.174, consolidated):
Aggregate quoted investments rose from Rs 813.10 lakh (FY25) to Rs 3,328.78
lakh (FY26), a rise of Rs 2,515.68 lakh — matching the CFS financial-asset
outflow almost to the rupee. Aggregate unquoted investments (the two
associate stakes) rose only Rs 243.64 lakh (Rs 2,463.85 lakh to Rs 2,707.49
lakh), which is explained by equity-method profit accretion (Rs 243.80 lakh
share in profit of associate, see finding 2 above), not a fresh cash stake
purchase — the AOC-1 cost basis for both associates is unchanged year on
year (Rs 1,230.01 lakh Peptech, Rs 406.89 lakh Titan Media).

Finding: the FY26 investing spike is a treasury/portfolio deployment (Rs
25.16 cr into quoted instruments), not a capacity expansion. Net Block
(screener-data) rose Rs 57.27 cr (FY25) to Rs 61.61 cr (FY26), a modest Rs
4.34 cr, consistent with the ~Rs 7.42 cr net capex figure above (small gap
plausibly CWIP timing). No stated capacity or commissioning date was found
in the corpus for this Rs 4-7 cr of capex.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Source-provided ROCE (AR MD&A "Significant Key Financial Ratios" and Note
45 Analytical Ratios tables, consolidated) used in place of a computed
figure, per formula-definition rule 1. Window: FY23-FY26 (the years both
AR-disclosed and cross-checked against two consecutive annual reports where
available).

| FY | ROCE (consol, source) | Anchor |
|---|---|---|
| FY23 | 24.37% | AR FY24 Note 45 (consolidated), p.197, comparative column |
| FY24 | 23.07% | AR FY24 Note 45 (consolidated), p.197, own-year column (also appears as 23.07% comparative in AR FY25 Note 45 p.187 — consistent) |
| FY25 | 16.11% | AR FY25 Note 45 (consolidated), p.187, own-year column |
| FY26 | 22.76% | AR FY26 Note 45 (consolidated), p.198, own-year column |

Data quality note: AR FY26's comparative for FY25 shows 17.18% (p.198),
about 1.07pp above FY25's own-report figure of 16.11%. Own-year figures
used throughout for internal consistency (each year scored on its own
audited number).

A1 Median ROCE (n=4): sorted 16.11, 22.76, 23.07, 24.37 → median 22.92% →
band 20-24.9% → **Score 4**

A2 Minimum single-year ROCE: 16.11% (FY25) → band ≥15% → **Score 5**

A3 Median ROE (n=4, consol, source-disclosed, same window/method as ROCE
for internal consistency):
| FY | ROE (consol, source) | Anchor |
|---|---|---|
| FY23 | 19.13% | AR FY24 Note 45 (consol), p.197, comparative |
| FY24 | 17.73% | AR FY24 Note 45 (consol), p.197, own-year |
| FY25 | 11.91% | AR FY25 Note 45 (consol), p.187, own-year |
| FY26 | 17.84% | AR FY26 Note 45 (consol), p.198, own-year |

Data quality note: AR FY26's comparative for FY25 ROE shows 15.28%
(p.198), a large 3.37pp gap from FY25's own-report 11.91% — larger than the
ROCE gap; mechanism NOT FOUND in the extracts (possibly average-equity base
differences pre/post the FY26 stock split). Own-year figures used.

Sorted: 11.91, 17.73, 17.84, 19.13 → median 17.79% → band 15-19.9% →
**Score 4**

Cross-check (not scored): a full 10-year computed ROE series using
screener-data PAT ÷ average(opening, closing) Net Worth (FY17 uses closing
only, no FY16 opening available) gives a median of 18.83%, landing in the
same 15-19.9% band — consistent.

A4 ROCE trend, latest (FY26 = 22.76%) vs earliest (FY23 = 24.37%): decline
of 1.61pp → band "decline 1-3pp" → **Score 3**

**Block A total: 4 + 5 + 4 + 3 = 16 / 20** (unchanged by this correction)

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

B1 Cumulative CFO ÷ Cumulative PAT, full 10-year window (screener-data,
consolidated):
CFO FY17-FY26: 0.13+1.90+5.47+6.12+19.08+22.04+21.18+21.15+20.12+30.42 =
Rs 147.61 cr.
PAT FY17-FY26: 2.18+2.54+3.52+7.07+30.34+21.68+24.84+24.85+21.53+29.89 =
Rs 168.44 cr.
Ratio = 147.61 / 168.44 = 0.876 → band 0.85-0.99 → **Score 4** (unchanged)

B2/B3/B4 require Capex and Trade Payables, which are not in the screener
CSV cash-flow/balance-sheet export (screener-data Cash Flow section shows
only aggregate "Cash from Investing Activity", which the formula
definition explicitly excludes as a capex proxy since it mixes in
investment purchases; screener-data Balance Sheet section has no Payables
row). AR-sourced figures used instead, restricting these three metrics to
the 4-year window FY23-FY26 where AR detail exists.

Capex = "Purchase of Property, Plant and Equipment" CFS line (each year's
own presentation; CWIP treatment varies by year's own filing format, noted):
| FY | Capex (Rs cr) | Anchor |
|---|---|---|
| FY23 | 3.07 | AR FY24 p.132 (CFS, comparative column, Rs 307.37 lakh) |
| FY24 | 19.48 | AR FY24 p.132 (CFS, own-year, Rs 1,948.49 lakh) |
| FY25 | 9.37 | AR FY25 p.112 (CFS, own-year, "Purchase of PP&E" Rs 936.88 lakh; excludes the separate "Addition of CWIP (net)" Rs 84.83 lakh line, kept out for cross-year consistency of definition) |
| FY26 | 7.42 | AR FY26 p.116/162 (CFS, "Purchase of PP&E incl. CWIP" Rs 742.83 lakh, net of Rs 0.43 lakh disposal proceeds) |

FCF = CFO (screener-data) − Capex (AR-sourced, above):
| FY | CFO (cr) | Capex (cr) | FCF (cr) |
|---|---|---|---|
| FY23 | 21.18 | 3.07 | 18.11 |
| FY24 | 21.15 | 19.48 | 1.67 |
| FY25 | 20.12 | 9.37 | 10.75 |
| FY26 | 30.42 | 7.42 | 22.99 |

B2 FCF-positive years: 4 of 4 (100%) → band 100% → **Score 5** (unchanged)

B3 Cumulative FCF ÷ Cumulative PAT (same FY23-FY26 window):
Cumulative FCF = 18.11+1.67+10.75+22.99 = Rs 53.51 cr.
Cumulative PAT (FY23-FY26) = 24.84+24.85+21.53+29.89 = Rs 101.11 cr.
Ratio = 53.51 / 101.11 = 0.529 → band 0.40-0.59 → **Score 3** (unchanged)

### B4 Change in WC Days, latest vs earliest — CORRECTED

Trade Payables (AR-sourced, each year's own-report figure preferred over a
later restated comparative — see note below):
| FY | Trade Payables (Rs lakh) | Anchor |
|---|---|---|
| FY23 | 554.97 | AR FY24 p.152, comparative column (micro: nil, other: 554.97) |
| FY24 | 336.82 | AR FY24 p.152, own-year (micro 55.65 + other 281.17); consistent with AR FY25 p.89/136 comparative |
| FY25 | 521.65 | AR FY25 p.89/136, own-year (micro 55.03 + other 466.62) |
| FY26 | 854.10 | AR FY26 p.160, own-year (micro 215.11 + other 638.99) |

Data quality note: AR FY26's comparative for FY25 Trade Payables shows Rs
765.52 lakh (micro 55.03 + other 710.49), Rs 243.87 lakh above FY25's own
Rs 521.65 lakh — a reclassification between "Trade Payables — other
creditors" and "Other financial liabilities" between the two reports
(the FY25 Total Current Liabilities figure, Rs 1,773.64 lakh, is IDENTICAL
in both AR FY25 and AR FY26, confirming this is a sub-line reclass, not a
restatement of the total). Own-year figures used.

Revenue basis: reported Sales (screener-data) for FY23-FY25; FY26 shown
both reported (206.19) and like-for-like adjusted (200.35, see finding 1).
FY23 = Rs 144.00 cr, FY24 = Rs 164.07 cr, FY25 = Rs 156.45 cr (all
screener-data, reported).

**Unit-error correction:** Payable Days = Trade Payables ÷ Revenue × 365
requires both figures in the same unit. The prior pass divided Trade
Payables (lakh) by Revenue expressed in crore x 10 (i.e. effectively lakh
÷ 100) — wait, precisely: it converted revenue to lakh by multiplying by
10 instead of 100 (Rs 156.45 cr treated as Rs 1,564.5 lakh instead of the
correct Rs 15,645 lakh), overstating every Payable Days figure by exactly
10x. Recomputed on the correct basis (Trade Payables lakh ÷ Revenue lakh x
365, Revenue lakh = Revenue cr x 100):

| FY | Trade Payables (lakh) | Revenue (lakh) | Payable Days (corrected) |
|---|---|---|---|
| FY23 | 554.97 | 14,400.00 | 554.97/14400 x 365 = **14.07** |
| FY24 | 336.82 | 16,407.00 | 336.82/16407 x 365 = **7.49** |
| FY25 | 521.65 | 15,645.00 | 521.65/15645 x 365 = **12.17** |
| FY26 (reported rev) | 854.10 | 20,619.00 | 854.10/20619 x 365 = **15.12** |
| FY26 (adjusted rev) | 854.10 | 20,034.62 | 854.10/20034.62 x 365 = **15.56** |

Proof of the error, worked from the original FY25 figure: Payable Days
121.68 implied Trade Payables of 121.68 x 15,645 lakh / 365 / 10 (the
error's own arithmetic) — more simply, 121.68 is exactly 12.17 x 10.
Cross-check against FY25 Total Current Liabilities (Rs 1,773.64 lakh =
Rs 17.74 cr): the erroneous reading, if taken at face value as implying
Trade Payables ≈ Rs 52.15 cr (121.68 x 156.45 / 365), exceeds Total
Current Liabilities of Rs 17.74 cr — an impossibility, since payables are
a subset of current liabilities. The corrected Rs 5.22 cr (521.65 lakh)
fits comfortably inside Rs 17.74 cr.

Receivable Days and Inventory Days used the correct revenue basis
throughout and are unaffected; carried forward unchanged.

| FY | Recv Days | Inv Days | Pay Days (corrected) | WC Days (corrected) |
|---|---|---|---|---|
| FY23 | 53.24 | 91.68 | 14.07 | 53.24+91.68−14.07 = **130.85** |
| FY24 | 41.52 | 101.36 | 7.49 | 41.52+101.36−7.49 = **135.39** |
| FY25 | 43.90 | 118.32 | 12.17 | 43.90+118.32−12.17 = **150.05** |
| FY26 (reported rev) | 40.41 | 98.72 | 15.12 | 40.41+98.72−15.12 = **124.01** |
| FY26 (adjusted rev) | 41.60 | 101.63 | 15.56 | 41.60+101.63−15.56 = **127.67** |

Change, FY26 (adjusted, 127.67) vs FY23 (130.85): 127.67 − 130.85 = **−3.18
days**, a decrease of 3.18 days → band "±5 days" → **Score 3** (was
incorrectly scored 5 on the erroneous −12.40-to-4.26 reading)

**Block B total: 4 + 5 + 3 + 3 = 15 / 20** (was 17/20)

### block_b_trend (corrected)

**stable** — FCF grew from Rs 18.11 cr (FY23) to Rs 22.99 cr (FY26),
despite a FY24 dip to Rs 1.67 cr on a capex spike (AR FY24 capex Rs 19.48
cr); on the corrected basis, WC days ran high throughout the window and
did not swing negative — they rose from 130.85 (FY23) to a peak of 150.05
(FY25), then eased to 127.67 (FY26, adjusted), a net decrease of only
3.18 days over the full period, inside the flat/no-material-change band.
No working-capital release occurred; the FY23-earlier figure and the
apparent negative FY26 figure in the prior pass were both artefacts of a
10x unit error in the Payable Days calculation, now corrected above.

---

## BLOCK C: GROWTH (Max 20)

Revenue basis: like-for-like adjusted per finding 1 (FY26 = Rs 200.35 cr;
all other years reported, no gross-up found in their own filings).

C1 Revenue CAGR, FY17 (Rs 52.74 cr, screener-data) to FY26 (Rs 200.35 cr,
adjusted), 9 years:
CAGR = (200.35/52.74)^(1/9) − 1 = 15.99% → band 15-19.9% → **Score 4**
(Reported-basis cross-check: (206.19/52.74)^(1/9)−1 = 16.35%, same band.)

C2 PAT CAGR, FY17 (Rs 2.18 cr) to FY26 (Rs 29.89 cr, consol, screener-data),
9 years: CAGR = (29.89/2.18)^(1/9) − 1 = 33.77% → band ≥20% → **Score 5**

Data note: PAT is non-monotonic across the window — it jumped to Rs 30.34
cr in FY21 (from Rs 7.07 cr FY20, on a revenue jump to Rs 142.24 cr from Rs
79.44 cr, screener-data), then declined to Rs 21.68 cr FY22 and Rs 24.84 cr
FY23, before climbing back to Rs 29.89 cr by FY26. No loss-to-profit swing
(all 10 years positive), so the CAGR calculation is valid per the edge
rules, but the FY21 spike-and-fade pattern means the 33.77% headline CAGR
overstates the smoothness of the trajectory.

C3 Positive YoY revenue years (screener-data, reported basis; FY26 vs FY25
positive under both reported and adjusted bases so the choice does not
change this count): 9 year-on-year comparisons FY18-FY26; declines in FY22
(123.55 vs 142.24) and FY25 (156.45 vs 164.07); 7 of 9 positive = 77.8% →
band 75-99% → **Score 3**

C4 PAT CAGR − Revenue CAGR (adjusted basis) = 33.77% − 15.99% = +17.78pp →
band ≥+3pp → **Score 5**

**Block C total: 4 + 5 + 3 + 5 = 17 / 20** (unchanged)

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20), latest = FY26

EBITDA FY26 (operating, pre-other-income) computed via EBITDA = PBT −
Other Income + Depreciation + Interest (cross-checked against the full
expense build and matches PBT exactly, screener-data): 38.17 − 5.41 + 4.93
+ 0.91 = **Rs 38.60 cr**. This is unaffected by the freight gross-up
(equal add to revenue and "other expenses").

D1 Net Debt ÷ EBITDA: Borrowings (screener-data, incl. lease liabilities
per screener convention, cross-checked against AR FY26 p.160: standalone
non-current borrowings Rs 32.67 lakh + current borrowings Rs 334.40 lakh +
non-current lease Rs 144.33 lakh + current lease Rs 59.32 lakh = Rs 570.72
lakh ≈ Rs 5.71 cr, matching screener-data exactly) = Rs 5.71 cr; Cash & Bank
(screener-data) = Rs 1.87 cr. Net Debt = Rs 3.84 cr (positive, small — not
net cash). Net Debt/EBITDA = 3.84/38.60 = 0.0995x → band 0-1.0x →
**Score 4**

D2 Interest Coverage: EBIT = PBT + Interest = 38.17 + 0.91 = Rs 39.08 cr
(screener-data); Interest = Rs 0.91 cr. Coverage = 42.9x → band ≥10x →
**Score 5**

D3 Debt ÷ Equity: Rs 5.71 cr / Rs 181.54 cr (Net Worth = Equity Share
Capital Rs 8.26 cr + Reserves Rs 173.28 cr, screener-data; cross-checked
against AR FY26 p.160 Total Equity Rs 18,154.75 lakh = Rs 181.5475 cr,
exact match) = 0.0314 → band <0.1 → **Score 5** (AR MD&A also discloses
Debt-equity Ratio 0.03, consolidated, AR FY26 p.105 — consistent)

D4 Current Ratio: AR FY26 MD&A "Significant Key Financial Ratios" table,
p.105, discloses Current Ratio = 3.28x (both standalone and consolidated,
FY26) → band ≥2.0 → **Score 5**

**Block D total: 4 + 5 + 5 + 5 = 19 / 20** (unchanged)

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20), latest = FY26

E1 Promoter holding (latest, 31-Mar-2026): 55.78% (AR FY26 p.61, and p.132
Disclosure of Shareholding of Promoters, total 2,30,47,520 shares of
4,13,18,500 = 55.78%) → band 50-59.9% → **Score 4**

E2 Promoter holding change over 3 years: FY23 = 55.88%, FY24 = 55.88%
(both AR FY24 p.132: "Total 4617515 55.88%" for both 31-Mar-2024 and
31-Mar-2023, "% Change during the year: -" for every promoter line), FY25 =
55.88% (implied flat, and shown as 55.88% comparative in AR FY26 p.132),
FY26 = 55.78% (AR FY26 p.132). Change FY23→FY26 = 55.78 − 55.88 = -0.10pp →
band ±1% → **Score 3**

E3 Promoter pledge: NOT FOUND (not in provided data) — no pledge or
encumbrance disclosure located in AR FY2024, AR FY2025, or AR FY2026 texts
(searched "pledge", "encumbered"; only generic pledge-of-securities audit
boilerplate and unrelated advertising-copy matches found, no promoter
pledge table). **Score 0**, per rule "never estimate a missing number."

E4 Contingent Liabilities ÷ Net Worth (latest FY26): Contingent Liabilities
= Rs 93.06 lakh (guarantees to bank against credit facilities/performance
guarantees; AR FY26 p.142 standalone and p.188 consolidated, identical both
statements; the Rs 406.86 lakh "Uncalled liability on partly paid-up
shares" is disclosed separately as a Commitment, not a Contingent
Liability, and is excluded per the note's own classification). Net Worth =
Rs 181.54 cr (18,154 lakh). Ratio = 93.06/18,154 = 0.51% → band <5% →
**Score 5**

**Block E total: 4 + 3 + 0 + 5 = 12 / 20** (unchanged)

---

## CORE SCORE (corrected)

A(16) + B(15) + C(17) + D(19) + E(12) = **79 / 100** (was 81/100)

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Peer set (auto-selected, per companies/TITANBIO.md operator ruling
2026-09-10): ADVANCED ENZYME TECHNOLOGIES LTD (ADVENZYMES), FERMENTA
BIOTECH LTD (FERMENTA), VIDHI SPECIALTY FOOD INGREDIENTS LTD (VIDHIING).
This is a limited, auto-selected 3-name comparator set, not an exhaustive
segment census — flagged wherever a moat test depends on segment breadth.

EBITDA margin (operating, = PBT − Other Income + Dep + Interest, all
screener-data FY26):
- Titan (adjusted revenue basis): 38.60 / 200.35 = 19.27% (reported basis:
  38.60/206.19 = 18.72%)
- ADVENZYMES: (232.54−46.04+40.09+3.73)/745.76 = 230.32/745.76 = 30.89%
- FERMENTA: (95.86−29.26+21.70+12.66)/523.20 = 100.96/523.20 = 19.30%
- VIDHIING: (65.79−1.79+9.23+4.77)/380.03 = 78.00/380.03 = 20.52%
Peer median = 20.52%

Gross margin proxy = (Revenue − Material Cost) / Revenue, FY26,
screener-data (Titan on adjusted revenue basis):
- Titan: (200.35−99.16)/200.35 = 50.51%
- ADVENZYMES: (745.76−194.31)/745.76 = 73.94%
- FERMENTA: (523.20−192.40)/523.20 = 63.22%
- VIDHIING: (380.03−223.79)/380.03 = 41.11%
Peer median = 63.22%

**M1 Pricing Power**: EBITDA margin FY17 (10.16%, computed as
(3.34−0.28+0.82+1.48)/52.74) vs FY26 adjusted (19.27%): expansion of
+9.11pp (≥2pp) AND revenue CAGR 15.99% (≥10%) → **Score 5**

**M2 Cost Advantage** vs peer median EBITDA margin: Titan 19.27% vs peer
median 20.52% = 1.25pp below, within the ±2pp band → **Score 1**

**M3 Capital Efficiency**: FAT = Sales/Net Block = 200.35/61.61 = 3.25x
(>3x); ROCE FY26 = 22.76% (>20%, source-disclosed, see Block A) →
**Score 5**

**M4 Customer Stickiness**: 2 revenue-decline years (FY22, FY25) over the
9-year window, overall CAGR positive → band "2 decline years, CAGR
positive" → **Score 1**

**M5 Scale & Dominance** — PEER DATA NEEDED (segment-wide ranking beyond
the 3 auto-selected comparators is NOT FOUND): mcap (screener-data):
ADVENZYMES Rs 3,405.77 cr > Titan Rs 1,805.66 cr > VIDHIING Rs 1,703.47 cr
> FERMENTA Rs 1,422.82 cr. Titan ranks 2nd of 4 by mcap (top 3) but 4th of
4 (last) by EBITDA margin — does not meet "top3 mcap AND margin top2."
Falls to "top5 mcap" band → **Score 1** on the 3-peer set available. True
segment ranking beyond this set is NOT FOUND; PEER DATA NEEDED for a
conclusive read. No score change from the original pass (this correction
only adds the marker).

**M6 Technology/R&D**: R&D recurring expenditure FY26 = Rs 27,47,023.70 =
Rs 27.47 lakh (AR FY26 p.83, "Expenditure incurred on Research and
Development"); FY25 = Rs 17.63 lakh. R&D/Revenue FY26 = 0.27/200.35 =
0.14%, far below the 1% floor for even the lowest scoring band →
**Score 0**

**M7 Regulatory/License** — PEER DATA NEEDED: count of listed players in
the biological ingredients / fermentation-inputs segment is NOT FOUND
beyond the 3 auto-selected peers; no explicit statement of segment player
count or licensing barrier in the corpus → **Score 0**

**M8 Distribution**: no quantified distribution reach, outlet count, or
revenue-per-outlet metric found in the corpus (only aggregate export value
Rs 8,033.20 lakh and import value Rs 862.78 lakh, AR FY26 p.142/188, which
is not a distribution-reach metric) → **Score 0**

**M9 Brand**: gross margin proxy 50.51% is 12.71pp BELOW peer median
(63.22%), not above → band "at/below" → **Score 0**

**M10 Switching Costs**: 2 decline years over the period (not "all but 1"),
overall growth positive → band "overall growth, 2+ decline years" →
**Score 1**

**M11 Network Effects** (9 years available, ≥6 required): prior 3yr CAGR
FY20→FY23 = (144.00/79.44)^(1/3)−1 = 21.92%; latest 3yr CAGR FY23→FY26
(adjusted) = (200.35/144.00)^(1/3)−1 = 11.65%. Latest is LOWER than prior,
and latest is also below the 20% and 15% thresholds in the lower bands →
**Score 0**

### M12 Negative WC/Float — CORRECTED

Corrected WC days over the 4 available years: FY23 = 130.85, FY24 =
135.39, FY25 = 150.05, FY26 (adjusted) = 127.67. All four years exceed 45
days — none negative, none in 0-15, none in 15-45 — band ">45" applies in
every year → **Score 0** (was incorrectly scored 1, on the erroneous
15-45-day median read that itself depended on the 10x Payable Days error).

**Block F (moat) total: 5+1+5+1+1+0+0+0+0+1+0+0 = 14 / 60** (was 15/60)

Moat profile:
```
M1  Pricing Power        [#####] 5  PRESENT
M2  Cost Advantage       [#    ] 1
M3  Capital Efficiency   [#####] 5  PRESENT
M4  Customer Stickiness  [#    ] 1
M5  Scale & Dominance    [#    ] 1
M6  Technology/R&D       [     ] 0
M7  Regulatory/License   [     ] 0
M8  Distribution         [     ] 0
M9  Brand                [     ] 0
M10 Switching Costs      [#    ] 1
M11 Network Effects      [     ] 0
M12 Negative WC/Float    [     ] 0
```

Moats present (score ≥3): M1, M3 = **2 moats confirmed** (unchanged — M12's
move from 1 to 0 does not cross the ≥3 "present" threshold)

Moat classification: 2 present → **MODERATE** (unchanged)

---

## CLASSIFICATION (corrected)

Core score: 79 / 100 (was 81/100)
Moat score: 14 / 60 (was 15/60)
Grand total: 93 / 160 (was 96/160)

Data confidence: 10 years (FY17-FY26) for revenue/PAT/CFO → "10+ yrs full"
tier for those metrics; 4 years (FY23-FY26) for AR-anchored ROCE/ROE/WC-day
metrics, noted throughout, not separately downgraded since each metric's
own available history meets or exceeds the 3-year floor. The effect of the
missing FY17-FY22 balance-sheet window on A1/A2 (median/minimum ROCE) is
NOT tested and NOT FOUND — no estimate is substituted.

Deal-breaker check (none triggered):
1. Block A (16) not <8 — no trigger
2. Block B (15, corrected from 17) not <8 — no trigger
3. Median ROCE (22.92%) not <10% — no trigger
4. Cumulative CFO/PAT (0.876) not <0.50 — no trigger
5. Pledge: NOT FOUND, cannot confirm >15% — no trigger (not estimated)
6. ND/EBITDA (0.0995x) not >3x — no trigger
7. Revenue declined in 2 of 9 years, not a majority — no trigger
8. PAT positive in all of last 3 years (FY24 24.85, FY25 21.53, FY26 29.89)
   — no trigger
9. History = 10 years, not <3 — no trigger

Classification matrix: Core 79 falls in the "60-79" row (not "≥80" — the
B4 correction pulled Core from 81 to 79). Core 60-79 + MODERATE moat
(not STRONG/FORTRESS) → matrix's "else" branch → **GOOD** (was GOOD+).

---

## STRONGEST / WEAKEST BLOCK

Strongest: Block D (Balance Sheet Strength), 19/20 — near-zero leverage
(Net Debt/EBITDA 0.10x, D/E 0.03x), high interest cover (42.9x), strong
current ratio (3.28x, AR-disclosed).

Weakest: Block E (Shareholder Alignment), 12/20 — driven entirely by the
E3 pledge data gap (NOT FOUND, scored 0) rather than a promoter-quality
finding; promoter holding itself is stable and moderately high (55.78%,
flat over 3 years).

Moat block is the other clear drag: 14/60, MODERATE (2 of 12 tests
present). Six of twelve tests scored 0 (M6, M7, M8, M9, M11, M12 —
M12 newly corrected to 0 this pass), several because the corpus lacks the
underlying disclosure (R&D detail exists but is negligible; distribution
reach, segment player count, and a wider peer set are simply not in the
provided data) rather than because a test was actively failed; M12 is now
a clean data-based 0 (WC days run 127.67-150.05 across all four years,
uniformly above the 45-day ceiling), not a disclosure gap.

---

## DECISION LINE (corrected)

GOOD (Core 79/100, Moat MODERATE 14/60, Grand total 93/160). No
deal-breaker triggered. This is a downgrade from the prior pass's GOOD+
read: a unit error in the Payable Days calculation (revenue converted
lakh-to-crore by 10x instead of 100x) had overstated every Payable Days
figure tenfold, manufacturing an apparent working-capital "release" to
negative WC days by FY26. Corrected, WC days run high and roughly flat
throughout FY23-FY26 (130.85 / 135.39 / 150.05 / 127.67), a net decrease
of only 3.18 days — inside the ±5-day flat band, not the >5-day
improvement originally scored. This pulls B4 from 5 to 3, Block B from
17 to 15, and Core score from 81 to 79 — below the 80 threshold the
matrix needs for GOOD+/EXCELLENT. The same corrected WC-days series also
takes M12 (Negative WC/Float) from 1 to 0, since every year now sits
above the 45-day ceiling; moat score falls from 15 to 14, moat class
unchanged at MODERATE. Two real data gaps remain in Block E (promoter
pledge NOT FOUND) and Block F (segment structure, distribution reach, and
a wider peer set NOT FOUND — M5 and M7 now explicitly marked PEER DATA
NEEDED) that should be closed before Halt 1.

The freight gross-up (verification priority 1) does not change the
classification band on any scored metric (C1 lands in the same band
reported or adjusted), but it does inflate the FY26 headline growth
narrative by about 3.7pp (31.8% reported vs 28.1% like-for-like) and this
adjusted figure is the one carried forward. The Peptech reconciliation
(priority 2) and the TM Media naming question (priority 3) are both
resolved with clean anchors; the investing-outflow split (priority 4)
shows the FY26 cash deployment was overwhelmingly a portfolio/treasury
allocation (Rs 25.16 cr into quoted instruments), not a capacity
investment, which is a distinct fact from the growth story and should be
carried into the business-understanding narrative at Halt 1.

---

```yaml
stage: B01-gate0
company: "TITANBIO"
run_date: "2026-09-16"
model: claude-sonnet-5
status: complete
input_gaps:
  - "Promoter pledge disclosure not found in any of the three annual reports (E3 scored 0)"
  - "R&D expenditure disclosed but immaterial (Rs 27.47 lakh FY26); no product-wise or segment revenue split available (single reportable segment)"
  - "Distribution reach, segment player count, and a wider peer set beyond the 3 auto-selected comparables not found (M5, M7 marked PEER DATA NEEDED; M8 also 0 on absent company-level distribution disclosure)"
  - "Residual Rs 1.86 cr variance between AR-CFS investing outflow (Rs 32.55 cr) and screener-data aggregate (Rs 34.41 cr) for FY26, source not found"
  - "Rs 415.03 lakh gap between AOC-1 associate profit-considered (Rs 658.83 lakh) and actual consolidated P&L pickup (Rs 243.80 lakh) not itemized in notes"
  - "FY17-FY22 balance-sheet/capex granularity not in corpus; effect of a longer window on A1/A2 (median/minimum ROCE) not tested, not estimated"
flags:
  - {type: FLAG-REVENUE-BASIS, reason: "FY26 revenue includes an estimated Rs 5.84 cr freight gross-up absent from the FY25 comparator (AR FY26 p.138, cross-checked against AR FY25); reported FY26 growth 31.79% vs like-for-like 28.06%. All growth/margin scores in this scorecard use the like-for-like Rs 200.35 cr FY26 revenue figure."}
  - {type: FLAG-ASSOCIATE-RECON, reason: "AOC-1 profit-considered for Peptech + Titan Media (Rs 658.83 lakh, AR FY26 p.80) exceeds the actual 'Share in profit of associate' P&L pickup (Rs 243.80 lakh, AR FY26 p.161) by Rs 415.03 lakh; plausible Ind AS 28 unrealised-profit elimination on Rs 389.38 lakh of FY26 related-party sales to Peptech, mechanism not disclosed."}
data_years: 10
fy_range: "FY17 to FY26"
blocks: {A: 16, B: 15, C: 17, D: 19, E: 12}
core_score: 79
moat_score: 14
grand_total: 93
moats_confirmed: 2
moat_class: "MODERATE"
classification: "GOOD"
deal_breakers: []
history_downgrade: false
data_notes:
  - "CORRECTION (2026-09-16, this pass): Payable Days originally divided Trade Payables by Revenue converted lakh-to-crore at a factor of 10 instead of 100, overstating every Payable Days figure 10x (e.g. FY25: 121.68 vs corrected 12.17). Proof: the erroneous FY25 reading implies Trade Payables of ~Rs 52.15 cr, which exceeds FY25 Total Current Liabilities of Rs 17.74 cr, an impossibility. Corrected WC Days: FY23 130.85, FY24 135.39, FY25 150.05, FY26 (adjusted) 127.67 -- a net decrease of only 3.18 days FY23-to-FY26, not the prior +4.26-to--12.40 swing. Effect: B4 5->3, Block B 17->15, Core 81->79, M12 1->0, moat 15->14, grand total 96->93, classification GOOD+->GOOD. Recv/Inv days and all other blocks/tests unaffected and unchanged."
  - "Screener Data_Sheet CSV confirmed CONSOLIDATED basis (FY26 PAT 29.89 cr matches consol Rs 2,988.52 lakh, AR FY26 p.161, not standalone Rs 2,744.72 lakh)"
  - "data_years=10 / fy_range=FY17-FY26 describes the window used by B1 and C1-C4 (growth/cash-flow) only. Block A (A1-A4, ROCE/ROE) and Block B's B2-B4 (capex, FCF, WC-days) use the FY23-FY26 AR-anchored 4-year window because no FY17-FY22 balance-sheet or capex detail exists in the corpus (only 3 annual reports on file, each a 2-year comparative). The effect of the longer window on A1/A2 was not tested and is NOT FOUND -- not estimated."
  - "PAT non-monotonic FY17-FY26: spiked to Rs 30.34 cr in FY21 (revenue jump to Rs 142.24 cr), dipped FY22-23, recovered by FY26; no loss-to-profit swing (all years positive)"
  - "ROCE/ROE restatement discrepancies found between consecutive ARs for FY25 (ROCE 16.11% own-report vs 17.18% restated in AR FY26; ROE 11.91% own-report vs 15.28% restated) — own-year figures used throughout for consistency"
  - "Trade Payables FY25 sub-line reclassified between AR FY25 (Rs 521.65 lakh) and AR FY26 comparative (Rs 765.52 lakh) though the Total Current Liabilities figure (Rs 1,773.64 lakh) is identical in both — a presentational reclass, not a restatement of the total; own-year figure used"
  - "Gross margin proxy used for M9 per rubric fallback: (Revenue - Material Cost)/Revenue, stated as proxy"
  - "1:5 stock split (effective 20-Feb-2026) and pending 1:4 bonus (recommended 03-Sep-2026, not yet approved) do not affect any metric in this scorecard, which works in absolute Rs crore terms (revenue, PAT, net worth, debt), not per-share figures; EPS/CAGR-per-share was out of scope for this framework"
block_b_trend: "stable — FCF grew from Rs 18.11 cr (FY23) to Rs 22.99 cr (FY26) despite a FY24 dip to Rs 1.67 cr on a capex spike; corrected WC days ran high throughout (130.85 FY23 -> 135.39 FY24 -> 150.05 FY25 -> 127.67 FY26 adjusted), a net decrease of only 3.18 days, not the swing to negative reported before correction — no working-capital release occurred"
analyst_note: "Classification (GOOD, corrected from GOOD+) is carried mainly by Blocks A, C and D. A unit error in Payable Days (revenue converted lakh-to-crore at 10x instead of 100x) had overstated a >5-day WC improvement that was actually a 3.18-day, inside-band change; corrected, Block B falls to 15/20 and Core to 79/100, below the 80 threshold for GOOD+. The moat score (14/60, MODERATE) is thin largely because disclosure is thin, not because tests were decisively failed — six of twelve moat tests scored 0, five on missing data (R&D immaterial, no distribution/segment/wider-peer data; M5 and M7 now marked PEER DATA NEEDED) and one (M12) now a clean data-based 0 since corrected WC days sit above 45 days in all four years. The two clean adverse moat findings are M9 (gross margin 12.7pp below peer median) and M11 (deceleration: latest 3yr revenue CAGR 11.65% vs prior 3yr 21.92%), both suggesting Titan is a margin-taker, not a margin-setter, in a segment where three-times-larger ADVENZYMES sits at nearly 2x its EBITDA margin. The FY26 investing spike (Rs 25.16 cr into quoted investments) is funded by strong operating FCF (Rs 22.99 cr), not a working-capital release as previously read; it should be tested at Halt 1 for whether it signals a lack of organic reinvestment opportunity."
```
