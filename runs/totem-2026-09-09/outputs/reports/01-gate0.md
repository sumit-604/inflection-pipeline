# GATE 0 QUANTITATIVE SCORECARD — Forbes Precision Tools & Machine Parts Ltd (TOTEM)

Run: runs/totem-2026-09-09/ | Stage 1 (B01-gate0) | Model: claude-sonnet-5 | 2026-09-09 | **RUN 3**

## WHY THIS IS RUN 3

Two independent verifiers audited run 2 and returned three MAJOR findings
and four MINOR findings. Each is fixed at source below, not patched over.

**MAJOR 1 (numerical verifier, source-fidelity, non-overridable).** Run 2's
LBF-4 said the Rs 5.9 cr Labour Codes charge was NOT FOUND in any filed
source. Wrong. It is disclosed three times: AR FY26 Note 39 (p.126), the
FY26 Audited Results filing Note 5 (p.8 of 10), and the AR FY26 Board's
Report / MD&A (p.24-25). Corrected below (LBF-4). A related fact the
red-flag verifier surfaced and this run independently re-verified: the
same disclosure showed Rs 387 lakh in the Q3 FY26 filing and Rs 590 lakh
in the FY26 audited filing, a 52% upward revision in the same paragraph
with no change-in-estimate note. Reported below.

**MAJOR 2 (framework verifier, Block F test M5).** Run 2 scored M5 = 3
against a 4-company set (subject + Kennametal + Wendt + Birla Precision)
while conceding that set is not the segment: the Indian round-cutting-tool
market runs mostly on unlisted and imported supply (Sandvik, Guhring,
Walter, Ceratizit, Kyocera, Chinese imports), so 3 listed peers cannot
establish a segment rank. M5 is re-scored 0, PEER DATA NEEDED, below.

**MAJOR 3 (framework verifier, Block B test B4).** Run 2 displayed "+5.0
days" and scored it 1 under "increased 5-15", without stating that "+5.0"
sits on the same displayed value as the "±5 days" = 3 band boundary. This
run recomputes B4 to two decimal places from primary balance-sheet
figures (not the earlier rounded intermediates): delta = +5.01 days. The
boundary and the call are stated explicitly below. Score unchanged at 1,
but now defended rather than asserted.

**MINOR fixes applied:**
1. Two FY26 EBITDA bases existed (Rs 52.62 cr filed-results basis vs
   Rs 52.94 cr Data_Sheet.csv-consistent basis). Governance rule stated
   and applied consistently below (D1, D2, M1 use the filed basis; M2, M9
   use the Data_Sheet-consistent basis because peer figures only exist in
   that format). This also caught and fixed a mislabeling bug: run 2's M1
   line cited "AR-sourced basis" for numbers that were actually the
   Data_Sheet-consistent basis. M1 is recomputed on the correct (filed)
   basis below; the score does not change.
2. D1 mutual-fund exclusion: kept excluded, one-line rationale below.
3. M8 Distribution: the 2024 Information Memorandum (p.58 of 182) records
   "200+ distributors supported through 12 divisional sales offices & 60+
   sales & application Engineers" — mentioned, unquantified trend. Ruled
   in scope (it is a filed corpus document); M8 re-scored 1 (was 0).
4. Kennametal's June-2026 Data_Sheet.csv column carries a Rs 225.0 cr
   Change in Inventory (vs Rs 21.5 cr prior year) alongside blank Power &
   Fuel / Other Mfr. Exp / Selling & Admin cells and a Rs 226.8 cr Other
   Expenses figure (vs Rs 7.8 cr prior year) — a re-bucketing artifact in
   the source export, named below beside the year-end alignment note.

Everything else in run 2 stood up to audit and is carried unchanged:
Blocks A, C, D (except the two lines above), E, the pledge deal-breaker,
the three-year history reality, and LBF-1/LBF-2/LBF-3.

Data available: 3 years (FY2023-24 to FY2025-26). Scoring adapted to
3-year history. The company was incorporated in 2022; the Scheme of
Arrangement demerging it out of Forbes & Company Ltd took effect
01-Mar-2024; shares listed on BSE 11-Jun-2024. FY23 is a pre-demerger shell
stub (Total assets Rs 0.05 cr, PBT Rs -0.01 lakh per screener-Data_Sheet.csv)
and is NOT used as a data year. Longer restated history exists only inside
the Information Memorandum (pre-demerger, different entity structure) and
is not used here per the basis-hierarchy rule. FY2023-24, FY2024-25 and
FY2025-26 are the three audited standalone years used throughout.

---

## LOAD-BEARING FACTS — VERIFICATION FIRST

**LBF-1, Q1 FY27 margin bridge — CONFIRMED, all four legs exact.**
(unchanged from run 2) Source: inputs/results/FY27-Q1_Unaudited_Results_30Jun2026.pdf,
Statement of P&L, rendered page-03.png (Q1 FY27 results, p.3), cross-checked
against screener-Data_Sheet.csv Quarters block.
- Revenue: Q1 FY27 Rs 67.55 cr vs Q1 FY26 Rs 52.41 cr, +28.9%.
- OPM (Revenue minus materials, purchases, inventory change, employee cost,
  other expenses; excludes finance cost and D&A): Q1 FY27 = (6755-2348-0-92
  -1245-1522)/6755 = 22.9%. Q1 FY26 = (5241-1782-0-(-116)-1131-1603)/5241 =
  16.05% ≈ 16.1%. Both match the claim exactly.
- Combined material cost (net of inventory absorption): Q1 FY27 =
  2440/6755 = 36.12% of revenue. Q1 FY26 = 1666/5241 = 31.79%. Delta =
  +4.33pp, matching the claimed "+4.3pp worsening" exactly. [INFERENCE:
  the margin gain is not a raw-material story; it is an employee-cost and
  other-expense compression story riding on volume, with material cost
  (net of inventory absorption) actually a modest drag.]
- Employee cost: Q1 FY27 = 1245/6755 = 18.43% ≈ 18.4%. Q1 FY26 = 1131/5241
  = 21.58% ≈ 21.6%. Matches exactly.
- Other expenses: Q1 FY27 = 1522/6755 = 22.53% ≈ 22.5%. Q1 FY26 = 1603/5241
  = 30.59% ≈ 30.6%. Matches exactly.
- Exceptional items (Net) = NIL in both quarters.

**LBF-2, FY26 inventory build — CONFIRMED on absolute rupee figures;
inventory-days and CCC figures NOT reproducible from the prescribed
formula on this run's own data.** (unchanged from run 2)
Source: annual-report__Annual_Report_2026.txt, Note 8 Inventories (AR FY26,
p.92): Total inventory Rs 5,642.15 lakh (Rs 56.42 cr) at 31-Mar-2026 vs
Rs 3,193.07 lakh (Rs 31.93 cr) at 31-Mar-2025 — matches the claim exactly.
CFO: Rs 2,755.29 lakh (Rs 27.55 cr) FY26 vs Rs 5,131.62 lakh (Rs 51.32 cr)
FY25 (AR FY26, Cash Flow Statement, p.71) — matches the claim exactly.
Using this stage's fixed formula (Inventory Days = Inventory ÷ Revenue ×
365, revenue basis; COGS is not a single explicit P&L line so revenue
basis is used and stated), inventory days computed here are FY24 61.45,
FY25 50.1, FY26 82.04 — real deterioration but far below the claimed
146 → 255 days. The AR-disclosed inventory turnover ratio (AR FY26, p.118)
is 1.83x FY26 vs 2.27x FY25, days-equivalent ~199.5 vs ~160.8 — also
directionally consistent but still not matching 146/255. [DATA NOTE: the
LBF-2 "146 to 255 days" and "91 to 152 day CCC" figures cannot be
reconstructed from this run's own filed data on any basis tried. Direction
confirmed; specific magnitude unverified, not used in scoring.]

**LBF-3, promoter pledge — CONFIRMED exactly, all three quarters checked.**
(unchanged from run 2) Source: shareholding__SHP_30Jun2026.txt (p.4-5),
shareholding__SHP_31Mar2026.txt (p.4-5), shareholding__SHP_30Jun2025.txt
(p.4-5). Promoter and promoter group hold 38,102,764 shares = 73.85% of
51,594,464 total shares, unchanged across all three filings. Shares
pledged = 35,967,172, all held by Shapoorji Pallonji And Company Private
Limited (100% of ITS holding pledged). Pledged shares as % of total
promoter group holding = 35,967,172 / 38,102,764 = 94.4%, identical at
Jun-2025, Mar-2026 and Jun-2026. No corporate guarantees given (AR FY26
contingent-liabilities note, p.124: only Rs 16.81 lakh labour-matter
claims). Promoter (Shapoorji Pallonji & Co.) financing-structure pledge,
not evidence of an operating-company guarantee, but a stable, near-total
pledge of the controlling stake and a governance deal-breaker per the
scoring rules.

**LBF-4, FY26 Labour Codes charge — CORRECTED THIS RUN. The charge exists,
it is Rs 5.90 cr, and it sits inside ordinary Employee Benefits Expense,
not as an exceptional item.**
Sources: annual-report__Annual_Report_2026.txt, Note 39 (AR FY26, p.126,
"NOTES TO FINANCIAL STATEMENTS ... (Contd.)"): "On November 21, 2025, the
Government of India notified four Labour Codes... In accordance with IND
AS 19, these changes constitute a plan amendment requiring immediate
recognition of past service cost, resulting in an incremental impact of
₹590 Lakhs (comprising gratuity and compensated absences) which has been
recognized as an employee benefit expense in the current reporting
period." Also disclosed verbatim in the AR FY26 Board's Report / MD&A
(p.24-25: "...notwithstanding the estimated impact of ₹590 Lakhs recognized
during the year in relation to employee benefit obligations pursuant to
the notified Labour Codes") and in results__FY26_Audited_Results_31Mar2026.txt,
Note 5 (FY26 Audited Results, p.8 of 10), same wording, same Rs 590 lakh
figure.
- Statement of P&L (FY26 Audited Results, p.5 of 10): Employee benefits
  expense FY26 Rs 5,044 lakh vs FY25 Rs 4,403 lakh — the Rs 590 lakh
  charge is embedded in this line, confirmed by Note 39/Note 5's own text
  ("recognized as an employee benefit expense"), not carried as a
  separate line.
- Exceptional items (Net): NIL for both FY26 and FY25 (Statement of P&L,
  line 4, FY26 Audited Results p.5 of 10) — this half of run 2's LBF-4
  was correct and stands.
- Revenue from operations: Rs 25,101.13 lakh FY26 vs Rs 23,266.17 lakh
  FY25 (AR FY26 Note 21, p.70), matching screener-Data_Sheet.csv exactly.
  Growth 7.9%.
- **Restatement check (Q3 FY26 vs FY26 audited), independently
  re-verified this run:** results__FY26-Q3_Unaudited_Results_31Dec2025.txt,
  Note 5 (Q3 FY26 results, p.5 of 5), same paragraph, nearly identical
  wording, discloses "an incremental impact of ₹387 lakhs (comprising
  gratuity and compensated absences)". The FY26 Audited Results (12-month)
  discloses ₹590 lakhs for the same estimate. Increase = (590-387)/387 =
  52.5% ≈ 52%, same paragraph structure and wording, no change-in-estimate
  note in either filing. [DATA NOTE: an actuarial/legal estimate that
  rose 52% between the nine/quarter-to-date disclosure and the full-year
  disclosure, unexplained in the filed text. Flagged, not scored — Gate 0
  has no formula slot for a one-off employee-benefit past-service-cost
  estimate revision.]
- Run 2's original claim that the charge "is NOT FOUND in any filed
  source" is withdrawn as an error of source-reading, not of interpretation.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — unchanged from run 2, not peer-dependent

Source: AR FY25 ratio note (AR FY25, p.100) for FY24/FY25; AR FY26 ratio
note (AR FY26, p.118) for FY26.

| Year | ROCE (AR-disclosed) | ROE (AR-disclosed) |
|---|---|---|
| FY24 | 28% | 43% |
| FY25 | 22% | 19% |
| FY26 | 22% | 17% |

FY24's 43% ROE is a base-effect artifact of the demerger (average equity
blends a near-zero FY23 pre-demerger base with the post-demerger closing
equity). Flagged, not excluded — the AR discloses it as the actual ratio.

- **A1 Median ROCE** = median(28, 22, 22) = 22% → 20-24.9% band → **4**
- **A2 Minimum single-year ROCE** = 22% → ≥15% → **5**
- **A3 Median ROE** = median(43, 19, 17) = 19% → 15-19.9% band → **4**
- **A4 ROCE trend, latest (22%) vs earliest (28%)** = decline of 6pp →
  decline >5pp → **0**

**Block A total = 13/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — B4 recomputed to two decimals this run (MAJOR finding 3)

Source: Cash Flow Statements, AR FY25 (p.58) for FY24/FY25, AR FY26 (p.71)
for FY26.

| Year | CFO (cr) | Capex (cr) | FCF (cr) | PAT (cr) |
|---|---|---|---|---|
| FY24 | 9.46 | 97.26 | -87.80 | 29.71 |
| FY25 | 51.32 | 28.26 | 23.06 | 28.75 |
| FY26 | 27.55 | 18.39 | 9.16 | 28.77 |

FY24's huge capex is the post-demerger capacity build.

- **B1 Cumulative CFO ÷ Cumulative PAT** = 88.33 / 87.23 = 1.013 → **5**
- **B2 FCF-positive years** = 2 of 3 = 66.7% → 50-74% band → **2**
- **B3 Cumulative FCF ÷ Cumulative PAT** = -55.58 / 87.23 = -0.637 → **0**
- **B4 Change in WC Days, latest vs earliest — recomputed to two decimal
  places from primary balance-sheet figures:**

  Formula (stage-fixed): WC Days = Receivable Days + Inventory Days −
  Payable Days, each = balance ÷ Revenue from operations × 365 (revenue
  basis; COGS is not a single explicit P&L line, so revenue basis is used
  throughout, as in LBF-2).

  FY24 (year end 31-Mar-2024) inputs — AR FY25, Balance Sheet (p.55
  assets / p.56 liabilities) and Note 21 (p.57):
  Trade receivables Rs 2,944.40 lakh; Inventory Rs 3,846.87 lakh; Trade
  payables Rs 782.35 + Rs 1,387.07 = Rs 2,169.42 lakh (micro/small +
  other creditors, Note 19); Revenue from operations Rs 22,849.66 lakh.
  - Receivable Days = 2,944.40 / 22,849.66 × 365 = 47.03
  - Inventory Days = 3,846.87 / 22,849.66 × 365 = 61.45
  - Payable Days = 2,169.42 / 22,849.66 × 365 = 34.65
  - WC Days FY24 = 47.03 + 61.45 − 34.65 = **73.83** (73.8291 unrounded)

  FY26 (year end 31-Mar-2026) inputs — AR FY26, Balance Sheet (p.68 assets
  / p.69 liabilities) and Note 21 (p.70):
  Trade receivables Rs 3,019.59 lakh; Inventory Rs 5,642.15 lakh; Trade
  payables Rs 1,431.62 + Rs 1,808.53 = Rs 3,240.15 lakh; Revenue from
  operations Rs 25,101.13 lakh.
  - Receivable Days = 3,019.59 / 25,101.13 × 365 = 43.91
  - Inventory Days = 5,642.15 / 25,101.13 × 365 = 82.04
  - Payable Days = 3,240.15 / 25,101.13 × 365 = 47.12
  - WC Days FY26 = 43.91 + 82.04 − 47.12 = **78.84** (78.8363 unrounded)

  **Delta, latest vs earliest = 78.8363 − 73.8291 = +5.0072 ≈ +5.01 days.**

  Band boundary, stated explicitly: the "±5 days" band spans −5.00 to
  +5.00 inclusive; "increased 5-15" begins strictly above +5.00. The
  full-precision delta (+5.0072) sits 0.01 day past the upper edge of the
  ±5 band, not inside it. This is not a rounding artifact of the earlier
  "+5.0" display — the true delta is +5.01, unambiguously in the
  "increased 5-15" band.
  - **B4 = 1** (increased 5-15 days). Call defended: score stands, but on
    a stated, not assumed, boundary reading.

**Block B total = 5+2+0+1 = 8/20** — unchanged from run 2.

block_b_trend: **deteriorating** — CFO fell from Rs 51.32 cr (FY25) to
Rs 27.55 cr (FY26), a 46% decline, on the inventory build (LBF-2); WC days
rose from 65.2 (FY25, prior-run figure, unchanged this run) to 78.84
(FY26, recomputed), +13.6 days within the year even though the 3-year
trend is a smaller +5.01 day net change because FY24's WC days (73.83)
were already elevated by the pre-listing capex ramp. FY26's Employee
Benefits Expense also carries the Rs 590 lakh Labour Codes one-off
(LBF-4), which this stage's fixed formulas do not strip out of PAT or
CFO — a further reason the FY26 print reads softer than the underlying
run rate.

---

## BLOCK C: GROWTH (Max 20) — unchanged from run 2, not peer-dependent

| Year | Revenue (cr) | PAT (cr) |
|---|---|---|
| FY24 | 228.50 | 29.71 |
| FY25 | 232.66 | 28.75 |
| FY26 | 251.01 | 28.77 |

- **C1 Revenue CAGR** (FY24→FY26, 2 years) = (251.01/228.50)^(1/2) - 1 =
  4.81% → <5% → **0**
- **C2 PAT CAGR** = (28.77/29.71)^(1/2) - 1 = -1.60% → negative → **0**
- **C3 Positive YoY revenue years** = 2 of 2 = 100% → **5**
- **C4 PAT CAGR minus Revenue CAGR** = -1.60 - 4.81 = -6.41pp → -3 to -8pp
  band → **1**

**Block C total = 6/20**

Three years of flat revenue (4.8% CAGR) and flat-to-declining PAT
(-1.6% CAGR) sit directly underneath the Q1 FY27 print (+28.9% revenue,
OPM 16.1%→22.9%, PAT +137% per LBF-1). This scorecard's fixed 3-year
annual window cannot capture Q1 FY27 (single quarter, not a scoring year).
FY26 PAT is additionally held down by the Rs 590 lakh Labour Codes charge
(LBF-4) that this stage's fixed formula does not adjust for.

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — EBITDA basis governance stated this run (MINOR 1, 2)

FY26 figures. Total borrowings Rs 16.64 cr = non-current Rs 10.72 cr +
current Rs 4.15 cr + lease liabilities Rs 1.77 cr (AR FY26 Balance Sheet,
p.69). Cash & bank Rs 6.28 cr. Net worth FY26 = Rs 51.59 cr + Rs 116.99 cr
= Rs 168.58 cr.

**EBITDA basis governance (stated once, applied consistently):** two
EBITDA figures exist in this run's working. The filed-audited-results
basis (Total Income excl. other income, minus Total Expenses excl.
finance cost and D&A, per the Statement of P&L in the primary filed
sources) gives FY26 = Rs 52.62 cr (20.96% margin) and FY24 = Rs 51.38 cr
(22.48% margin). The Data_Sheet.csv-consistent basis (used in Block F
below because it is the only formula computable identically across the
subject and all three peers from the one common data source) gives FY26
= Rs 52.94 cr (21.09% margin). **The filed-audited-results basis governs
every single-entity test (D1, D2, M1); the Data_Sheet-consistent basis is
used only in the two cross-peer tests that need it (M2, M9), and is never
substituted into a single-entity test.** This also corrects a run 2
labelling bug: M1 was tagged "AR-sourced basis" while actually using the
Data_Sheet-consistent numbers; M1 below is recomputed on the correct
(filed) basis. The score does not change (see M1).

- **D1 Net Debt ÷ EBITDA** = (16.64 - 6.28) / 52.62 = 0.197x → **4**.
  [Excludes Rs 23.23 cr mutual-fund investments (Note 4B, Financial
  Assets - Investments, current) from cash. Judgment kept unchanged this
  run: these sit under a separate balance-sheet line from Note 9 Cash and
  cash equivalents, and the stage's fixed formula does not instruct
  treating investments as a cash-equivalent. If included as quasi-cash,
  the company flips to net cash and D1 scores 5 — an operator override,
  not applied here.]
- **D2 Interest Coverage** = (39.50 + 1.66) / 1.66 = 24.8x → **5**
- **D3 Debt ÷ Equity** = 16.64 / 168.58 = 0.099 → <0.1 → **5** [AR's own
  narrower "total debt" D/E is 10% (AR FY26, p.118), exactly at the
  threshold; this stage's screener-total-borrowings-incl-lease basis is
  9.9%, used for scoring]
- **D4 Current Ratio** = 1.84 (AR-disclosed, AR FY26 p.118) → **4**

**Block D total = 18/20** — strongest block. Near net cash, ample
interest cover, minimal leverage.

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — unchanged from run 2, not peer-dependent

Source: shareholding__SHP_30Jun2026.txt, shareholding__SHP_31Mar2026.txt,
shareholding__SHP_30Jun2025.txt (all p.4-5). No earlier SHP filing was
provided; the company listed 11-Jun-2024, so a true 3-year
promoter-holding-change window does not yet exist in this run's inputs.

- **E1 Promoter holding (latest, Jun-2026)** = 73.85% → **5**
- **E2 Promoter holding change** — unchanged at 73.85% across all three
  filings (~12 months, not 3 years) → within ±1% → **3** [data_note: window
  is provisional]
- **E3 Promoter pledge (latest, Jun-2026)** = 94.4% of the 73.85% promoter
  holding → >15% → **0**
- **E4 Contingent liabilities ÷ Net Worth** = Rs 0.1681 cr / Rs 168.58 cr =
  0.0997% → <5% → **5**

**Block E total = 13/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — RE-SCORED THIS RUN (MAJOR finding 2, MINOR findings 3 and 4)

### Peer year-end alignment (stated honestly, unchanged from run 2)

Kennametal India (KENNAMET) reports to a **June** year end: its "FY24",
"FY25", "FY26" columns in KENNAMET-Data_Sheet.csv end 2024-06-30,
2025-06-30, 2026-06-30. The subject and Birla Precision Technologies
(BIRLAPREC) both report to **March**: FY24/FY25/FY26 end 2024-03-31,
2025-03-31, 2026-03-31. Wendt India (WENDT) also reports to March, same
calendar as the subject.

For latest-year peer comparisons (M2, M9 below) I compared subject FY26
(year ended 31-Mar-2026) against BIRLAPREC FY26 and WENDT FY26 (same
31-Mar-2026 year end, exact match) and against KENNAMETAL's FY26 column
(year ended 30-Jun-2026, a 3-month lag). Sensitivity checks (substituting
Kennametal FY25 instead) did not change the peer median or ranking used
for scoring in either surviving test, because Birla's and Wendt's own
exact-match FY26 figures already determine the tier.

**Kennametal FY26 (30-Jun-2026) column anomaly, named beside the year-end
note:** KENNAMET-Data_Sheet.csv shows Power & Fuel, Other Mfr. Exp, and
Selling & Admin as BLANK for the 2026-06-30 column, while Change in
Inventory jumps to Rs 225.0 cr (vs Rs 21.5 cr FY25) and Other Expenses
jumps to Rs 226.8 cr (vs Rs 7.8 cr FY25). This is a re-bucketing artifact
in the source export (those three blanked cost lines appear to have been
folded into "Other Expenses" and/or "Change in Inventory" for this one
column), not an operating event. It does not corrupt the EBITDA-margin
figure used in scoring below: EBITDA computed by this run's formula from
the raw column (20.10%) reconciles to within rounding against Kennametal's
own Quarters-block "Operating Profit" line summed over the four quarters
(20.09%, the figure used), so the aggregate nets out correctly even though
the individual expense-line buckets are corrupted. Any test that read
Change in Inventory or Other Expenses as standalone lines for Kennametal
FY26 (this run's tests do not) would be unreliable.

Every EBITDA-margin and gross-margin figure below is computed from the
Data_Sheet.csv P&L component rows using one formula, applied identically
to all four companies (screener's own sign convention: "Change in
Inventory" is additive back):

`EBITDA = Sales − Raw Material Cost − Power & Fuel − Other Mfr. Exp −
Employee Cost − Selling & Admin − Other Expenses + Change in Inventory`

This formula was verified against each company's own Quarters-block
"Operating Profit" line (Sales − Expenses, given directly) by summing the
four quarters making up each fiscal year and cross-checking against the
annual computation. All four companies' FY25 and FY26 figures below
reconciled to within rounding; only FY24 could not be cross-checked
(quarterly data in this export starts at the quarter ending 2024-03-31,
before FY24 begins for a March filer and mid-FY24 for a June filer). This
Data_Sheet-consistent basis is used ONLY in M2 and M9 below (the two
cross-peer tests), per the EBITDA basis governance stated in Block D; it
is not used for M1 or any single-entity test.

**EBITDA margin (Data_Sheet-consistent basis, cross-peer tests only):**

| Company | Basis | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| Subject (TOTEM) | Mar FYE | 22.49% | 22.01% | 21.09% |
| Kennametal India | Jun FYE (offset +3mo) | 15.58% | 14.71% | 20.09% |
| Birla Precision | Mar FYE | 11.11% | 8.57% | 6.95% |
| Wendt India | Mar FYE | 24.71% | 22.73% | 13.72% |

(Anchors: KENNAMET-Data_Sheet.csv PROFIT & LOSS rows 11-18, columns
2024-06-30/2025-06-30/2026-06-30; BIRLAPREC-Data_Sheet.csv PROFIT & LOSS
rows 11-18, columns 2024-03-31/2025-03-31/2026-03-31; WENDT-Data_Sheet.csv
PROFIT & LOSS rows 11-18, columns 2024-03-31/2025-03-31/2026-03-31;
screener-Data_Sheet.csv PROFIT & LOSS rows 11-18. Quarterly cross-check:
each file's Quarters block rows 27-36, "Operating Profit" row, summed over
the four quarters composing the relevant fiscal year.)

- **M1 Pricing Power** (not peer-dependent; recomputed this run on the
  correct filed-audited-results basis — run 2 had mislabeled the
  Data_Sheet-consistent figures as "AR-sourced"): FY24 EBITDA (filed
  basis) = Revenue 22,849.66 − (Materials 8,050.05 + Purchases 128.72 +
  Δinv -220.04) − Employee 4,106.51 − Other Expenses 5,646.88 = Rs
  5,137.54 lakh = Rs 51.38 cr → margin 22.48% (AR FY25, Statement of
  P&L, p.57). FY26 EBITDA (filed basis) = Rs 52.62 cr → margin 20.96%
  (computed above, D1). Change FY24→FY26 = -1.52pp (not expansion, not a
  ≥2pp decline either); revenue CAGR 4.8% (<10%). Fits no scoring tier
  (needs revenue CAGR ≥10% for either the expansion or stable tier). **0**
  [Score unchanged from run 2's mislabeled version; basis correction did
  not change the tier because both bases give a decline under 2pp.]
- **M2 Cost Advantage vs peer median EBITDA margin** (Data_Sheet-consistent
  basis, per governance above): subject FY26 21.09%. Peer FY26 figures:
  Kennametal (Jun-26) 20.09%, Birla (Mar-26) 6.95%, Wendt (Mar-26) 13.72%.
  Peer median = 13.72%. Subject − peer median = **+7.37pp**, ≥5pp above
  → **5**. [Sensitivity: substituting Kennametal FY25 (14.71%) for FY26
  gives the same peer median, 13.72% — score unchanged.]
- **M3 Capital Efficiency** (not peer-dependent, unchanged): FAT (Revenue
  ÷ [Net Block + CWIP]) FY26 = 251.01 / 113.40 = 2.21x; ROCE FY26 = 22%.
  FAT>2x AND ROCE>15% → **3**
- **M4 Customer Stickiness** (not peer-dependent, unchanged): zero
  revenue-decline years; receivable days FY24 47.03 → FY26 43.91, within
  ±10 days → **5**
- **M5 Scale & Dominance — RE-SCORED THIS RUN (MAJOR finding 2).** The
  test's own language ("largest mcap in segment", "top 3 mcap ... in
  segment") requires a true segment-wide rank, not a rank within
  whichever peers this run's inputs happen to hold. This run holds market
  cap and margin data for exactly 3 listed peers (Kennametal, Wendt,
  Birla Precision). The actual Indian round-cutting-tool / precision
  cutting-tool segment is dominated by unlisted and imported supply
  (Sandvik Coromant, Guhring, Walter, Ceratizit, Kyocera, plus Chinese
  imports) that this run has no market-cap or margin data for at all. A
  3-listed-peer comparison set cannot establish where the subject ranks
  in that segment — it can only rank the subject against 3 named
  companies, which is a different, narrower claim than the test asks for.
  Per the rule ("if a test needs peer data that is not provided, score 0
  and mark PEER DATA NEEDED — never guess peer figures"), scoring a
  within-4-company rank as a proxy for segment rank is exactly the
  guess the rule forbids. **M5 = 0, PEER DATA NEEDED** (full segment
  market-cap and margin data for the unlisted/import competitive set is
  the missing input).
- **M6 Technology/R&D** (unchanged): no R&D line exists in any of the four
  Data_Sheet.csv exports and none is disclosed as a separate line in the
  subject's filed ARs. NOT FOUND across the board, not a peer-data gap.
  **0**
- **M7 Regulatory/License** (not peer-dependent, unchanged): unregulated,
  no licence/quota regime governs this business (cutting tools / precision
  machine parts is not a licensed segment). **0**
- **M8 Distribution — RE-SCORED THIS RUN (MINOR finding 3).** The 2024
  Information Memorandum (prospectus__Information_Memorandum_2024.txt,
  p.58 of 182): "Totem cover domestic market with 200+ distributors
  supported through 12 divisional sales offices & 60+ sales & application
  Engineers." Ruling: the Information Memorandum is a filed corpus
  document in this run's source list and is treated as in scope for M8,
  consistent with how it is used elsewhere in this run (e.g., it is
  listed among {{DATA_SOURCES}}). The figure is a reach disclosure with
  no growth trend or revenue-per-outlet metric attached — "mentioned
  unquantified" → **1** (was 0 in run 2).
- **M9 Brand** (Data_Sheet-consistent basis, per governance above): gross
  margin proxy = (Revenue − Raw Material Cost) ÷ Revenue, stated basis
  (raw material cost only, not netted for inventory change, applied
  identically to subject and all three peers). Subject FY26 GM =
  (251.01−93.32)/251.01 = 62.83%. Peer FY26 GM: Kennametal
  (1510.7−1018.0)/1510.7 = 32.61%; Birla (247.13−96.87)/247.13 = 60.81%;
  Wendt (236.32−103.38)/236.32 = 56.25%. Peer median = 56.25%. Subject −
  peer median = **+6.58pp** (≥5pp above tier) but revenue CAGR is 4.81%
  (<8% required for the ≥5pp/≥8% tier). Falls to "above peers but growth
  below" → **1**. [Sensitivity: substituting Kennametal FY25 GM (44.61%)
  for FY26 gives the same peer median, 56.25% — score unchanged. Note M9
  is a gross-margin (single-line) test, not read against the M5 segment
  concern: it compares against the same 3 held peers only, which the
  test's own wording ("peer median") does not require to be
  segment-exhaustive the way M5's "largest ... in segment" language does.]
- **M10 Switching Costs** (not peer-dependent, unchanged): revenue grew
  every year; receivable days fell (43.91 vs 47.03) → **5**
- **M11 Network Effects** (not peer-dependent, unchanged): only 3 years
  available, below the 6-year two-window test threshold; scored
  conservatively. 2-year CAGR 4.8%, well under thresholds; no structural
  network-effect mechanism in this business model. **0**
- **M12 Negative WC/Float** (not peer-dependent, unchanged): WC days
  positive and >45 in all three years (73.83, 65.2, 78.84 recomputed). **0**

**Moats present (score ≥3): M2, M3, M4, M10 = 4 moats**
**Moat score = 0(M1)+5(M2)+3(M3)+5(M4)+0(M5)+0(M6)+0(M7)+1(M8)+1(M9)+5(M10)+0(M11)+0(M12) = 20/60**
**Moat classification: 4-5 present = STRONG**

This is a step down from run 2's overstated 5-moats/22-60/STRONG (M5 was
wrongly credited on a 4-company set that is not the segment) but a step
up from run 1's MODERATE/13-60 (which wrongly zeroed the genuinely
peer-evidenced M2 and M9 tests). The moat picture that survives correct
scoring: a real, evidenced margin edge over the 3 named listed peers
(M2 +7.37pp EBITDA margin, M9 +6.58pp gross margin), plus capital
efficiency, customer stickiness and switching-cost tests that are not
peer-dependent at all — four confirmed moats, STRONG classification,
with the segment-dominance claim (M5) honestly marked unprovable from
this run's inputs rather than guessed from an incomplete comparison set.

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

BLOCK F  Quantitative Moat (12 tests, max 60)        20/60
Moats present: M2 Cost Advantage, M3 Capital Efficiency,
               M4 Customer Stickiness, M10 Switching Costs
Moat classification: STRONG (4 of 12 present)
M5 Scale & Dominance: PEER DATA NEEDED (0) — full segment (unlisted/
               import competitive set) data not held this run

GRAND TOTAL (core + moat)                            78/160
```

**Strongest block: D (Balance Sheet Strength), 18/20.** Near net cash,
24.8x interest coverage, D/E 0.10x, current ratio 1.84x.

**Weakest block: C (Growth), 6/20.** Flat revenue (4.8% 3-year CAGR),
flat-to-declining PAT (-1.6% CAGR) across the three audited years — a
structurally quiet base, additionally held down in FY26 by the Rs 590
lakh Labour Codes charge (LBF-4), sitting directly beneath the Q1 FY27
inflection claim, which this scorecard's fixed 3-year annual window
cannot capture.

---

## CLASSIFICATION

**Data confidence**: 3 years (FY24-FY26) → 3-4 band → **LIMITED,
downgrade classification one tier**.

**Classification matrix**: Core score 58 falls in the 40-59 band → this
band is flat in the matrix (does not branch on moat tier) → baseline
**AVERAGE**. (Block F's STRONG classification does not change the
baseline at Core 40-59; it would matter at Core 60-79 or Core ≥80.)

**Deal-breaker overrides checked** (unchanged from run 2; none are
peer-dependent):
1. Block A <8? No (13). Not triggered.
2. Block B <8? No (8, at the line). Not triggered.
3. Median ROCE <10%? No (22%). Not triggered.
4. Cumulative CFO/PAT <0.50? No (1.01). Not triggered.
5. **Pledge >15%? YES (94.4% of the 73.85% promoter stake pledged,
   Shapoorji Pallonji & Co., stable across three consecutive quarters
   Jun-2025 to Jun-2026) → caps classification at max AVERAGE.**
6. ND/EBITDA >3x AND IC <3x? No. Not triggered.
7. Revenue declined in majority of years? No. Not triggered.
8. PAT negative in any of last 3 years? No. Not triggered.
9. History <3 years? No (exactly 3 audited years). Not triggered (distinct
   from the data-confidence downgrade below).

**Sequencing**: baseline AVERAGE (Core 40-59) → apply the 3-year LIMITED
history-confidence downgrade, one tier: AVERAGE → **AVOID**. The pledge
deal-breaker independently confirms the classification cannot rise above
AVERAGE even before the history downgrade.

**FINAL CLASSIFICATION: AVOID** (mechanical, per the fixed scoring rules —
unchanged outcome from run 1 and run 2, now on a corrected Block F: 4
moats / 20/60 / STRONG, grand total 78/160, not run 2's overstated
22/60 / 5 moats / 80/160)

This is a compounding-mechanism outcome, not a company-quality verdict on
its own terms. CLAUDE.md is explicit that quality does not halt a run and
that "downstream position sizing may override AVERAGE for documented
post-IPO rebase / legacy cleanup cases." Three distinct things should be
weighed on their own facts by the operator, not collapsed into one:
- The pledge (94.4% of promoter stake, stable, no operating-company
  guarantee found) is a real governance flag on its own facts.
- The 3-year LIMITED-history downgrade is a structural artifact of the
  Mar-2024 demerger and Jun-2024 listing, not a company-quality signal.
  Absent that downgrade, the mechanical floor here is AVERAGE (from the
  pledge deal-breaker alone), not AVOID.
- With the corrected peer data, the moat picture underneath this AVOID is
  STRONG (4 of 12): a genuine, evidenced margin edge over the three named
  listed peers on M2 and M9, on top of capital efficiency, customer
  stickiness and switching-cost tests that clear the bar on their own —
  but the segment-dominance claim (M5) is honestly unprovable from this
  run's inputs, not credited on an incomplete 4-company set. Underlying
  fundamentals in the three audited years are solid: near-net-cash
  balance sheet, 22% ROCE, positive cumulative CFO/PAT, and a
  demonstrated cost/margin advantage versus the closest listed
  comparators — sitting under flat growth, an FY26 cash-conversion
  wobble, and a confirmed one-off Labour Codes charge (LBF-4) that
  LBF-1's Q1 FY27 print (if it holds up) would be the first data point
  against.

---

## DECISION LINE

Gate 0 mechanical classification: **AVOID** (pledge deal-breaker caps at
AVERAGE; 3-year LIMITED-history downgrade pulls one tier further to
AVOID). Flags propagate; this does not halt the run. Historical
depressors are named above (flat 3-year growth, a confirmed Rs 590 lakh
FY26 one-off Labour Codes charge that restated 52% higher between Q3 and
full-year filings, FY26 cash-conversion deterioration with WC days
recomputed to +5.01 days over the 3-year window, near-total promoter
pledge, short listed history) for the operator to weigh against a moat
block that, once correctly scored, reads STRONG on 4 of 12 tests (20/60)
— with the segment-dominance test (M5) honestly marked PEER DATA NEEDED
rather than guessed — and against the Q1 FY27 inflection claim this run
exists to test.
