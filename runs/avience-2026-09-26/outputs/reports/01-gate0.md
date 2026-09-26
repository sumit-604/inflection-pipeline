# STAGE 1 — GATE 0 SCORECARD (160 points)
Avience Biomedicals Ltd (AVIENCE) | Run date 2026-09-26 | Model: claude-sonnet-5

Data available: 3 years (FY24 to FY26). Scoring adapted to 3-year history.
Basis: CONSOLIDATED (screener main URL is consolidated, FY24-FY26; standalone
carries FY22-FY26 but the scorecard follows the consolidated basis to match
the framework's preferred all-entity view). Consolidation began with the
DR Meditech subsidiary acquisition 08-Aug-2023, so FY24 already carries a
part-year consolidated base.

UNITS: filings are in Rs lakh; screener and this report use Rs Cr. Every
number below states its source; where a filing figure in lakh is converted
to Cr for consistency with screener, the conversion is shown once (100 lakh
= 1 Cr, per B00 reporting_units).

LOAD-BEARING FACTS CHECKED AGAINST THIS SCORECARD (from B00):
- LBF2 (FY26 revised results, FY25 revenue on three bases): the REVISED
  25-Aug-2026 consolidated results (note 8) corrected an inter-company
  elimination error (Other Current Liabilities and Short-Term Loans and
  Advances each overstated by Rs 337.55 lakh). NO impact on profit or
  equity (results p.10, note 8; results p.11, board outcome). This
  scorecard's D-block ratios use the REVISED consolidated balance sheet
  (results p.12), which is the correct post-fix version. FY25 revenue is
  used at the SCREENER figure (Rs 44.92 Cr) throughout this scorecard for
  internal consistency with the 3-year screener P&L/BS/CF series; the
  REVISED RESULTS FILE shows FY25 consolidated revenue as Rs 45.24 Cr
  (results p.11) and the RHP restated shows Rs 45.97 Cr (RHP p.132) — a
  spread of about Rs 1 Cr across three bases. Named as a data_note; not
  resolved here (Gate 0 is mechanical, not a reconciliation exercise).
- LBF4 (cash conversion): screener's own CFO/OP 58% FY26 and debtor days
  146 are independently reproduced below from the raw P&L/BS lines
  (receivable days computed at 146.2, matching), which cross-validates the
  screener basis used throughout.

## DATA SOURCE MAP
- screener-Data_Sheet.csv (AVIENCE, CONSOLIDATED, FY24-FY26 annual; no
  quarterly block, half-yearly SME filer)
- Revised consolidated results, 25-Aug-2026 filing (AVIENBIO_25082026...txt),
  pages 11-13: full FY26 and FY25 consolidated P&L, balance sheet, cash flow
  with current/non-current liability and asset splits (used to compute ROCE,
  Current Ratio precisely for FY25-FY26)
- FY26 Annual Report (Annual_Report_FY2026_Avience.txt): contingent
  liabilities notes (standalone note 41, p.106; consolidated note 39, p.143)
- RHP (RHP_Avience_Biomedicals_Jun2026.txt): KPI table p.131-132 (own ROCE/
  D-E/Current Ratio definitions, used only as a cross-check, not substituted
  for the framework formula) and business-chapter distribution/R&D text
- B00-inputs.yaml: promoter holding and pledge (SHP as on 24-Jun-2026),
  sector row, input gaps
- Peer screener sheets: QLINE-Data_Sheet.csv, MOLBIO-Data_Sheet.csv,
  TARSONS-Data_Sheet.csv (FY26 rows used for moat peer comparisons)

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 20/20

Formula: ROCE = EBIT ÷ (Total Assets − Current Liabilities). Screener does
not carry its own ROCE figure in this Data_Sheet export (raw P&L/BS/CF
rows only), so ROCE is COMPUTED per the fixed formula.

FY26: EBIT = PBT 12.47 + Interest 1.70 = 14.17 Cr (screener-Data_Sheet).
Capital employed = Total Assets 7,456.82 lakh − Current Liabilities
2,958.09 lakh = 4,498.73 lakh = 44.99 Cr (revised consolidated results
p.12, balance sheet as at 31-Mar-2026). ROCE FY26 = 14.17 ÷ 44.99 = 31.5%
(computed).

FY25: EBIT = PBT 9.77 + Interest 1.45 = 11.22 Cr (screener-Data_Sheet).
Capital employed = Total Assets 5,648.84 lakh − Current Liabilities
2,359.18 lakh (computed as the identity Equity 2,265.98 + Non-current
liabilities 1,023.68, since the printed subtotal in the OCR'd text read
2,159.18, an evident scan error; the component sum and the balance-sheet
identity both give 2,359.18 lakh) = 3,289.66 lakh = 32.90 Cr (revised
consolidated results p.12). ROCE FY25 = 11.22 ÷ 32.90 = 34.1% (computed).

FY24: EBIT = PBT 3.03 + Interest 0.94 = 3.97 Cr (screener-Data_Sheet). The
FY24 consolidated balance sheet's current/non-current liability split is
NOT available in text form (RHP restated consolidated statements, pdf
pp.279-362, are image-only; not rendered for this stage). APPROXIMATION:
by the identity Capital Employed = Equity + Non-current liabilities, and
using RHP's own FY24 consolidated Debt-Equity ratio of 2.44x (=Long-term
debt ÷ Net worth, RHP p.132) applied to screener's FY24 net worth (Equity
Share Capital 3.28 + Reserves 2.94 = 6.22 Cr), implied FY24 long-term debt
≈ 2.44 × 6.22 = 15.18 Cr, which is close to screener's FY24 TOTAL
borrowings of 15.13 Cr — implying FY24 short-term borrowings were near
zero, i.e. non-current liabilities ≈ total borrowings for that year.
Capital employed (FY24, approximated) ≈ Equity 6.22 + Non-current liab
≈15.13 = 21.35 Cr. ROCE FY24 ≈ 3.97 ÷ 21.35 = 18.6% (computed,
APPROXIMATED; flagged in data_notes — do not treat as precise as the
FY25/FY26 figures).

A1 Median ROCE (18.6%, 34.1%, 31.5%) = 31.5% → ≥25% → **Score 5**
A2 Minimum single-year ROCE = 18.6% (FY24, approximated) → ≥15% → **Score 5**
A3 Median ROE: ROE = PAT ÷ average Net Worth.
  FY24: opening net worth unavailable (screener has no FY23 row); closing
  net worth used per rule, stated so. NW(FY24 closing) = 3.28+2.94 =
  6.22 Cr (screener-Data_Sheet). PAT FY24 = 2.16 Cr. ROE = 2.16÷6.22 = 34.7%.
  FY25: avg NW = (6.22 + [4.03+18.63=22.66]) ÷ 2 = 14.44 Cr. PAT FY25 =
  7.10 Cr. ROE = 7.10÷14.44 = 49.2%.
  FY26: avg NW = (22.66 + [4.03+27.38=31.41]) ÷ 2 = 27.04 Cr. PAT FY26 =
  8.75 Cr. ROE = 8.75÷27.04 = 32.4%.
  Median = 34.7% → ≥20% → **Score 5**
A4 ROCE trend, latest (31.5%) vs earliest (18.6%): latest ≥ earliest →
  **Score 5**

BLOCK A TOTAL: 20/20

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 2/20

CFO (screener-Data_Sheet): FY24 = 1.02 Cr, FY25 = 3.39 Cr, FY26 = 5.91 Cr.
Cumulative CFO = 10.32 Cr. Cumulative PAT (2.16+7.10+8.75) = 18.01 Cr.

B1 Cumulative CFO ÷ Cumulative PAT = 10.32 ÷ 18.01 = 0.573 → falls in
  0.50-0.69 → **Score 1**

Capex (purchase of PPE, from cash flow statement, excl. acquisitions):
FY26 = 13.4486 Cr (revised results p.13, "Purchase of property, plant and
equipments (including capital advances)" 1,344.86 lakh); FY25 = 9.2985 Cr
(929.85 lakh, same source, comparative column). FY24 capex is NOT broken
out anywhere in the provided corpus in this granularity; screener's total
"Cash from Investing Activity" for FY24 (−3.90 Cr) is used as a capex
PROXY (the company had negligible other investing lines pre-YEIDA ramp;
flagged as a proxy in data_notes).

FCF = CFO − Capex:
  FY24 ≈ 1.02 − 3.90 = −2.88 Cr (proxy capex)
  FY25 = 3.39 − 9.2985 = −5.91 Cr
  FY26 = 5.91 − 13.4486 = −7.54 Cr
All three years negative — consistent with B00/LBF4 ("FCF negative
FY24-FY26").

B2 FCF-positive years as proportion = 0 of 3 = 0% → <50% → **Score 0**
B3 Cumulative FCF ÷ Cumulative PAT = (−2.88−5.91−7.54) ÷ 18.01 = −16.33 ÷
  18.01 = −0.906 → negative → **Score 0**
B4 Change in WC Days, latest vs earliest available:
  Receivable Days = Receivables ÷ Revenue × 365 (Revenue basis; COGS is
  not explicitly stated as a single line in the source, so Revenue basis
  applies throughout, per the formula rule).
    FY24: 8.09÷23.83×365 = 123.9 days
    FY25: 17.21÷44.92×365 = 139.8 days
    FY26: 21.02÷52.46×365 = 146.2 days (matches B00/LBF4's screener-quoted
    146 debtor days almost exactly — cross-validated)
  Inventory Days (Revenue basis, per the same rule):
    FY24: 12.40÷23.83×365 = 189.9 days
    FY25: 13.07÷44.92×365 = 106.1 days
    FY26: 17.18÷52.46×365 = 119.5 days
    (Note: B00/LBF4 cites screener's own "inventory days" of 218, which
    screener computes on a COGS basis, not the Revenue basis this
    scorecard's formula mandates; the two are not comparable. Flagged in
    data_notes, not reconciled.)
  Payable Days (Revenue basis): NOT AVAILABLE for FY24 — screener's
  simplified balance sheet has no separate Trade Payables line (bundled
  into "Other Liabilities"), and the FY24 consolidated balance sheet note
  detail is not in text form (see A2 note above). Available for FY25-FY26
  from the revised results balance sheet (p.12):
    FY25: Payables (186.83→ FY26 col; FY25 col = 101.86+624.97=726.83
    lakh = 7.2683 Cr) ÷ 44.92 × 365 = 59.1 days
    FY26: Payables (186.83+760.63=947.46 lakh = 9.4746 Cr) ÷ 52.46 × 365 =
    65.9 days
  WC Days = RD + InvD − PD:
    FY25 = 139.8 + 106.1 − 59.1 = 186.8 days
    FY26 = 146.2 + 119.5 − 65.9 = 199.8 days
  FY24 WC Days cannot be computed (payables missing) — "latest vs
  earliest" uses FY25 as the earliest AVAILABLE full-basis year, not FY24
  (flagged; FY24-to-FY26 change may differ). Change FY26 vs FY25 = +13.0
  days → increased 5-15 days → **Score 1**

BLOCK B TOTAL: 2/20 (data_notes: cash generation is genuinely weak on the
provided numbers, not an artifact of a missing metric — CFO/PAT, FCF and
the payable-days gap all point the same direction)

---

## BLOCK C: GROWTH (Max 20) — Score: 20/20

Revenue (screener-Data_Sheet): FY24 = 23.83 Cr, FY25 = 44.92 Cr, FY26 =
52.46 Cr.
PAT: FY24 = 2.16 Cr, FY25 = 7.10 Cr, FY26 = 8.75 Cr.

C1 Revenue CAGR (FY24→FY26, 2-year): (52.46÷23.83)^(1/2) − 1 = 48.4% →
  ≥20% → **Score 5**
C2 PAT CAGR (FY24→FY26, 2-year): (8.75÷2.16)^(1/2) − 1 = 101.3% → ≥20% →
  **Score 5**
C3 Positive YoY revenue years: FY25 vs FY24 (+), FY26 vs FY25 (+) = 2 of 2
  = 100% → **Score 5**
C4 PAT CAGR minus Revenue CAGR = 101.3% − 48.4% = +52.9pp → ≥+3pp →
  **Score 5**

BLOCK C TOTAL: 20/20

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY26) — Score: 12/20

D1 Net Debt ÷ EBITDA: Net debt = Borrowings 28.93 − Cash 2.93 = 26.00 Cr
  (screener-Data_Sheet, FY26). EBITDA FY26 = EBIT 14.17 + Depreciation
  1.22 = 15.39 Cr (screener-Data_Sheet). ND/EBITDA = 26.00 ÷ 15.39 = 1.69x
  → falls 1-2x → **Score 3**
D2 Interest Coverage = EBIT ÷ Interest = 14.17 ÷ 1.70 = 8.34x → falls
  5-9.9x → **Score 4**
D3 Debt ÷ Equity = Borrowings 28.93 ÷ Equity (4.03+27.38=31.41) = 0.921 →
  falls 0.5-1.0 → **Score 3**
D4 Current Ratio (latest, FY26) = Current Assets 4,316.35 lakh ÷ Current
  Liabilities 2,958.09 lakh (revised consolidated results p.12) = 1.459 →
  falls 1.2-1.49 → **Score 2**

BLOCK D TOTAL: 12/20

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 15/20

E1 Promoter holding (latest): 64.59% (B00-inputs.yaml, citing NSE SHP XBRL
  as on 24-Jun-2026, revised 16-Jul-2026) → ≥60% → **Score 5**
E2 Promoter holding change over 3 years: pre-IPO 87.89% → post-IPO 64.59%
  (B00-inputs.yaml / companies/AVIENCE.md), a decrease of 23.3pp → per
  formula, decreased >3% → **Score 0**. FLAGGED: this decline is IPO
  primary-issue dilution (14,53,800 fresh shares issued 18-22 Jun 2026),
  not promoter selling, and only ONE shareholding pattern exists since
  listing (B00 input_gaps) — there is no true 3-year trend to measure for
  a company listed 25-Jun-2026. Scored mechanically per the formula; the
  0 should not be read as evidence of promoter exit.
E3 Promoter pledge (latest): 0% ("no pledge or encumbrance", B00-inputs.yaml
  citing the SHP filing) → **Score 5**
E4 Contingent Liabilities ÷ Net Worth (latest, CONSOLIDATED basis):
  Contingent liabilities FY26 = Rs 37.16 lakh, a GST demand at the
  subsidiary for FY2017-18 under appeal (FY26 AR, consolidated note 39,
  p.143). The standalone note 41 (p.106) additionally shows a Rs 500 lakh
  corporate guarantee to the subsidiary's bank facility at FY25, but this
  does not appear in the CONSOLIDATED note (intra-group, eliminated) and
  is not double counted here. Net worth FY26 (consolidated) = 3,141.30
  lakh (revised results p.12). Ratio = 37.16 ÷ 3,141.30 = 1.18% → <5% →
  **Score 5**

BLOCK E TOTAL: 15/20

---

## CORE SCORE (A+B+C+D+E): 20+2+20+12+15 = 69/100

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 18/60

Peer set for moat comparisons (screener-Data_Sheet, FY26 row): QLINE
(Q-Line Biotech), MOLBIO (Molbio Diagnostics), TARSONS (Tarsons Products).
Peer EBITDA margins and gross-margin proxies computed the same way as
AVIENCE's own (EBIT=PBT+Interest; EBITDA=EBIT+Depreciation).
  QLINE FY26: EBIT=72.55+19.42=91.97, EBITDA=91.97+10.79=102.76, margin
  102.76÷341.74=30.1%. GM proxy (Rev−RM cost)÷Rev = (341.74−137.48)÷341.74
  =59.8%.
  MOLBIO FY26: EBIT=197.56+23.15=220.71, EBITDA=220.71+35.73=256.44,
  margin 256.44÷1313.4=19.5%. GM proxy=(1313.4−489.92)÷1313.4=62.7%.
  TARSONS FY26: EBIT=21.9+22.75=44.65, EBITDA=44.65+96.53=141.18, margin
  141.18÷422.51=33.4%. GM proxy=(422.51−122.79)÷422.51=70.9%.
  Peer median EBITDA margin = 30.1%. Peer median GM proxy = 62.7%.

M1 Pricing Power: EBITDA margin FY24=19.3% (4.59÷23.83), FY25=26.9%
  (12.10÷44.92), FY26=29.3% (15.39÷52.46) — expanded +10.1pp over the
  window, AND revenue CAGR 48.4% ≥10% → **Score 5**
M2 Cost Advantage vs peer median EBITDA margin: AVIENCE FY26 29.3% vs
  peer median 30.1% = −0.8pp → within ±2pp → **Score 1**
M3 Capital Efficiency: FAT = Revenue ÷ Net Block = 52.46÷16.06 = 3.27x
  (>3x) AND ROCE 31.5% (>20%) → **Score 5**
M4 Customer Stickiness: zero revenue-decline years (both YoY periods
  positive), BUT receivable days rose from 123.9 to 146.2 (not stable
  ±10) → top band (5) not met on the stability leg; nearest applicable
  band is "max 1 decline year, fully recovered" (0 decline years
  trivially satisfies "max 1") → **Score 3**
M5 Scale & Dominance: PEER DATA NEEDED — the 3 named peers (QLINE, MOLBIO,
  TARSONS) are not a validated ranking of "the segment"; no broader
  listed-player mcap ranking for Indian IVD/diagnostics manufacturers is
  in the provided corpus → **Score 0, PEER DATA NEEDED**
M6 Technology/R&D: no R&D-to-revenue figure is disclosed anywhere in the
  provided corpus. RHP (p.61-62, "risk factor 45") states the company
  currently has four employees in R&D and plans to build an R&D centre,
  with no quantified spend → **Score 0**
M7 Regulatory/License: the segment is regulated (CDSCO licences), but no
  count of listed players in the specific IVD-reagent/analyser segment is
  in the provided corpus (peers named are hand-picked, not a full listed
  universe) → **Score 0, PEER DATA NEEDED**
M8 Distribution: RHP text (pp.29-30, risk factor 48; business chapter)
  describes a distributor/dealer network qualitatively ("network of
  distributors and dealers... continuously seek to increase the
  penetration...") but gives no count of distributors, outlets, or
  revenue-per-outlet figure → mentioned, unquantified → **Score 1**
M9 Brand: GM proxy (Revenue − Raw Material Cost) ÷ Revenue, proxy basis
  stated. AVIENCE FY26 = (52.46−32.60)÷52.46 = 37.9%, versus peer median
  62.7% — AVIENCE sits BELOW peer median by 24.8pp → at/below → **Score 0**
M10 Switching Costs: revenue grew every year (2 of 2 periods), BUT
  receivable days rose 22.3 days over the period (FY24→FY26), exceeding
  the ≤10-day threshold for any positive band, and there are no decline
  years to fit the "2+ decline years" band either → falls to else →
  **Score 0**
M11 Network Effects: the test needs ≥6 years for the two-window
  comparison; only 3 years are available (2 YoY periods). Scored
  CONSERVATIVELY on the overall trend, as instructed: revenue CAGR 48.4%
  (≥20%) AND selling & admin expense as % of revenue declining (FY24
  8.2%, FY25 6.75%, FY26 6.39%, screener-Data_Sheet) → **Score 3** (stated
  as based on partial history, not the full 2-window test)
M12 Negative WC/Float: WC Days FY25=186.8, FY26=199.8 (from Block B4) —
  both far above the 45-day ceiling → **Score 0**

MOAT SCORE TOTAL: 5+1+5+3+0+0+0+1+0+0+3+0 = 18/60

Moats present (score ≥3): M1 (5), M3 (5), M4 (3), M11 (3) = 4 moats present
→ **Moat classification: STRONG** (4-5 present)

---

## DATA CONFIDENCE AND CLASSIFICATION

Data confidence: 3 years (FY24-FY26) → per the ladder, "3-4 LIMITED,
downgrade classification one tier."

Classification matrix: Core score 69 (falls in 60-79) + moat STRONG →
matrix gives GOOD+. Applying the 3-4-year LIMITED downgrade (one tier):
GOOD+ → **GOOD**.

Deal-breaker overrides checked:
1. Block A <8 → max GOOD: Block A = 20, NOT triggered.
2. Block B <8 → max GOOD: Block B = 2 → **TRIGGERED**, caps at GOOD
   (drivers: B2=0 zero FCF-positive years, B3=0 negative cumulative
   FCF/PAT — both driven by FY24-FY26 capex ramp for the YEIDA plant,
   which the company itself frames as growth capex, not distress; the
   scorecard records the mechanical trigger, not a judgment on cause).
3. Median ROCE <10% → max AVERAGE: 31.5%, NOT triggered.
4. Cumulative CFO/PAT <0.50 → max AVERAGE: 0.573, NOT triggered.
5. Pledge >15% → max AVERAGE: 0%, NOT triggered.
6. ND/EBITDA >3x AND IC <3x → AVOID: ND/EBITDA 1.69x, NOT triggered.
7. Revenue declined in majority of years → max AVERAGE: 0 decline years,
   NOT triggered.
8. PAT negative in any of last 3 years → max AVERAGE: PAT positive all 3
   years, NOT triggered.
9. History <3 years → AVERAGE: exactly 3 years, NOT triggered.

Both paths (matrix + history downgrade, and deal-breaker #2) independently
land on **GOOD**.

---

## GRAND TOTAL: Core 69 + Moat 18 = 87/160

## STRONGEST / WEAKEST BLOCK
Strongest: Block A (Return on Capital), 20/20, and Block C (Growth), 20/20
— tied. High, fast-compounding returns and PAT growing faster than
revenue on a small base.
Weakest: Block B (Cash Generation Quality), 2/20 — cumulative CFO covers
only 57% of cumulative PAT, FCF has been negative all three years, and
working-capital days have widened (debtor days 124→146, WC days 187→200
FY25→FY26). This is the single number set that should carry into every
downstream stage's cash-conversion check (per LBF4).

## DECISION LINE
Classification: **GOOD** (Core 69/100 GOOD+-range + STRONG moat, downgraded
one tier for 3-year LIMITED history; independently capped at GOOD by the
Block B <8 deal-breaker). This is a mechanical Gate 0 score only — it does
not resolve LBF1 (guidance delivery), LBF2 (revenue-basis reconciliation),
or LBF3 (concentration/related-party exposure), all of which are named as
first verification priorities for later stages.

---

## DATA NOTES
1. FY25 revenue used at the SCREENER figure (44.92 Cr) throughout for
   internal consistency with the screener 3-year series; the revised
   consolidated results file shows 45.24 Cr and the RHP restated shows
   45.97 Cr for the same year (LBF2). Not reconciled at this stage.
2. FY24 ROCE (18.6%) is an APPROXIMATION: the FY24 consolidated balance
   sheet's current/non-current liability split is not available in text
   form (RHP restated consolidated statements are image-only, pdf
   pp.279-362). Capital employed was derived from the accounting identity
   Capital Employed = Equity + Non-current liabilities, using RHP's own
   FY24 consolidated Debt-Equity ratio (2.44x) to infer that FY24
   long-term debt approximated total borrowings (i.e., near-zero
   short-term debt that year). FY25 and FY26 ROCE are computed directly
   from the revised consolidated results' full balance sheet detail and
   are not subject to this approximation.
3. FY24 capex used the screener's total "Cash from Investing Activity"
   (−3.90 Cr) as a PROXY for capex (purchase of PPE), since the detailed
   FY24 cash flow breakdown by investing line is not in the provided
   corpus in text form. FY25/FY26 capex are exact figures from the
   revised consolidated results cash flow statement.
4. Inventory Days in this scorecard are computed on a REVENUE basis per
   the fixed formula (COGS is not cleanly a single disclosed line here).
   B00/LBF4 quotes screener's own "inventory days" of 218, which screener
   computes on a COGS basis internally — the two figures (119.5 here vs
   218 at LBF4) are NOT comparable and are not an error.
5. Payable Days, and therefore full WC Days, could not be computed for
   FY24 (no Trade Payables line on screener's simplified balance sheet,
   and FY24 consolidated note detail is image-only in the RHP). Block B4's
   "latest vs earliest" therefore compares FY26 to FY25, not FY24.
6. E2 (promoter holding change) reflects IPO primary-issue dilution
   (87.89% pre-IPO to 64.59% post-IPO), not promoter selling, and only one
   shareholding pattern exists since listing — there is no genuine 3-year
   trend for a company listed 25-Jun-2026. Scored mechanically at 0 per
   the formula; flagged so the number is not misread downstream.
7. M5 and M7 scored 0 with PEER DATA NEEDED: the three concall-selected
   peers (QLINE, MOLBIO, TARSONS) are not a validated count of "listed
   players in the segment"; no broader ranking is in the provided corpus.
8. Loss-to-profit swings: none. PAT was positive in all three years
   (FY24 2.16 Cr, FY25 7.10 Cr, FY26 8.75 Cr).

## ANALYST NOTE
Growth and returns are exceptional on the numbers (48% revenue CAGR, 101%
PAT CAGR, ROCE rising to 31%+), but Block B's near-zero score is the real
story: every rupee of that growth has been funded by working capital
build and YEIDA capex, not internally generated cash, and FCF has been
negative in all three years on record. The GOOD classification (not
GOOD+) reflects that gap directly — a deal-breaker override, not a
history-length artifact alone. FY24's ROCE and WC figures rest on
approximations (data_notes 2-3, 5) because the RHP's FY24 consolidated
statements are image-only; a downstream stage should render those pages
if FY24 precision matters to a specific test. The IPO-driven promoter
dilution (E2=0) should not be read as an alignment red flag on its own.
