# STAGE 1: GATE 0 SCORECARD — Yash Highvoltage Ltd (YASHHV) — RUN 2 (CORRECTED)

## CORRECTION LOG (run 2, against verifier B12c findings on B01)

1. **A4 ROCE trend computed on a PROXY capital-employed series for FY20-23, against the "fixed, do
   not substitute" formula rule (verifier MJ-2).** ACCEPTED. The formula is ROCE = EBIT ÷ (Total
   Assets − Current Liabilities). FY20-23 Total Current Liabilities is not in the corpus in exact
   form, so the correct treatment per rule 5 ("if a data point is not available, mark N/A... score
   it 0") is to mark FY20-23 ROCE not computable on the fixed formula, not to substitute a
   Net-Worth-plus-Debt proxy. A1 (median) and A2 (minimum) are recomputed on the 3 years where the
   fixed formula is exactly computable (FY24-26); both scores are unchanged (median 27.5%, min
   20.2%, both still top band). A4 (trend) is recomputed as FY26 27.5% vs FY24 42.3% = −14.8pp,
   "decline >5pp" → **Score 0** (was 3). Block A: 18 → **15**. Core: 70 → **67**. Grand total:
   91 → **88**. Classification unaffected (GOOD; deal-breaker #2 still governs, Core still in the
   60-79 band). The FY20-23 proxy figures are retained below as unscored supplementary context,
   clearly labelled.

2. **E2 data note "dilution, not sell-down" contradicted by the report's own share counts
   (1,76,03,595 → 1,65,43,595) and cited an Aug-2026 allotment for a 31-Mar-2026 figure (verifier
   MJ-3).** ACCEPTED, and now grounded further. Re-reading the RHP: the Dec-2024 IPO itself
   included a Promoter Offer for Sale of up to 11,30,000 shares by Mr. Keyur Girishchandra Shah
   (RHP p.15, "B. Offer for Sale by Promoter Selling Shareholder"). The actual FY-end promoter
   share-count fall (10,60,000 shares, close to the 11,30,000 OFS ceiling) is consistent with that
   disclosed OFS, not an unexplained post-IPO sell-down and not the Aug-2026 allotment (which
   post-dates the 31-Mar-2026 measurement date and cannot explain it). The corrected note below
   splits the 21.5pp decline into ~17.8pp from issuance-driven dilution (denominator growth: Fresh
   Issue + post-IPO preferential allotments) and ~3.7pp from the promoter's own OFS at the IPO. The
   E2 score (0) is unchanged; the note is corrected so downstream stages read this as a disclosed,
   bounded, one-time IPO-stage promoter exit, not a stealth sell-down and not unexplained.

3. **FY20-21 capex proxy (verifier MN-1).** POSITION KEPT. FY20-21 capex is still proxied by
   screener's aggregate "Cash from Investing Activity" because no RHP/AR cash-flow breakdown exists
   for those years (RHP's restated cash flow statement covers FY22-24 + stub only). The verifier
   confirms this produces no score change (B2 and B3 both keep their bands whether FY20-21 are
   included via proxy or excluded: B2 5/7=71.4% vs 3/5=60%, both land in the 50-74% band = Score 2;
   B3 −67.15/97.96=−0.686 vs −72.57 FY22-26-only, both negative = Score 0). No fix required to the
   score; the PROXY label and exclusion-window arithmetic are both stated explicitly below and in
   data_notes so no downstream stage treats FY20-21 capex as exact.

4. **Narrow M6 R&D search; the AR documents DSIR-recognised R&D (verifier MN-2).** ACCEPTED. Run 1
   searched only "Research and Development" / "R&D expenditure" as literal strings and reported no
   match, which was a search-scope failure, not an absence of disclosure. A wider search finds the
   AR FY26 standalone Note 43 ("Expenditure on Formulation and Development (R&D)") and the AR FY25
   Note 34 / Board's Report technology-absorption annexure, both of which disclose the Company as a
   DSIR-recognised in-house R&D centre (Scientific & Industrial Research Organisation, SIRO) with a
   quantified rupee spend. M6 is rescored below on the actual figures. The score remains 0 (the
   ratio is below even the lowest ≥1% band), but it is now grounded on found data instead of a
   false "not disclosed."

5. **Moat M11 Network Effects — stage 7 overrode it to no evidence.** POSITION KEPT for Gate 0's own
   score, with the flag strengthened. B01 runs before stage 7 in the pipeline sequence and has no
   stage 7 output to consult; the Gate 0 M11 test is explicitly mechanical ("apply the tests exactly
   as specified... 0-5 each"), and the verifier confirms the mechanical application is correct
   ("PASS (mechanical, as the rubric demands)"). Run 1 already flagged this exact risk in-line and
   in data_notes ("no disclosed network-effect mechanism... flagged for stage 7 qualitative moat
   scan to confirm or override") and named the likely outcome. That flag is kept and sharpened below
   so stage 7's override is expected, not a surprise; Gate 0's own moat_score (21/60) and
   moats_confirmed (5) are left as the mechanical rubric computes them, per the rule that Gate 0 is a
   quantitative, non-judgmental screen (rule 2, "No qualitative judgments"). Downstream stages must
   read the flag and use stage 7's own moat count once it is available, not Gate 0's.

---

Data available: 7 years (FY20 to FY26), standalone. Scoring adapted to 7-year history.
Consolidated data covers FY25-FY26 only (subsidiary/JV consolidation began FY25); FY20-FY26
standalone series (screener-standalone-Data_Sheet.csv) used as the primary series per orchestrator
instruction. Company listed 19-Dec-2024 (BSE SME); it is a half-yearly reporter, no quarterly
results exist. FY25 and H1FY26 comparatives in the FY26 audited results are labelled RESTATED.
All screener figures are ₹ Cr (source: screener-standalone-Data_Sheet.csv); AR/RHP/results figures
are ₹ Lakh on the face of the document, converted to ₹ Cr at 1 Cr = 100 Lakh, shown as "computed."

Screener's own ratio sheets (Profit & Loss, Balance Sheet, Cash Flow, Quarters, Customization tabs)
came out EMPTY per the collector (B00 input_gaps) — no pre-computed ROCE/ROE/ratio rows exist.
Every ratio below is COMPUTED from the raw Data_Sheet P&L/BS/CF lines plus AR/RHP notes, per the
Formula Definitions. No screener-native ratio was available to cite directly.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

Formula (fixed): Capital Employed (CE) = Total Assets − Total Current Liabilities. EXACT Total
Current Liabilities is available in the corpus only for FY24-26 (AR FY26 audited standalone balance
sheet, comparative columns FY26/FY25/1-Apr-2024). FY20-23 Total Current Liabilities is NOT in the
corpus in exact form: the screener Data_Sheet has no current/non-current split (only an aggregate
"Other Liabilities" line), and the RHP restated balance-sheet totals were not found under that exact
line label in the extracted text. Per rule 5, this run scores ROCE only for the years where the fixed
formula is exactly computable (FY24-26). FY20-23 figures are shown below as unscored supplementary
context (PROXY, Equity+Reserves+Borrowings), never fed into A1/A2/A4.

EBIT = PBT + Interest (screener-standalone-Data_Sheet.csv, PROFIT & LOSS block).

| FY | EBIT (Cr) | CE (Cr) | ROCE | Method | Used for scoring? |
|----|-----------|---------|------|--------|--------------------|
| 20 | 4.70 | 16.58 | 28.3% | PROXY (NW+Debt) | No — unscored context |
| 21 | 6.18 | 19.39 | 31.9% | PROXY | No — unscored context |
| 22 | 13.46 | 31.95 | 42.1% | PROXY | No — unscored context |
| 23 | 17.37 | 39.87 | 43.6% | PROXY | No — unscored context |
| 24 | 19.92 | 47.13 | 42.3% | EXACT (AR FY26 p.99: Total Assets 7,117.73L − Total Current Liab 2,346.98L) | **Yes** |
| 25 | 31.44 | 155.70 | 20.2% | EXACT (AR FY26 p.99: TA 20,405.19L − TCL 4,835.73L) | **Yes** |
| 26 | 54.05 | 196.72 | 27.5% | EXACT (AR FY26 p.99: TA 26,443.15L − TCL 6,770.80L) | **Yes** |

**A1 Median ROCE** (FY24-26 only, 3 exact years): sorted 20.2, 27.5, 42.3 → median = 27.5% → ≥25%
→ **Score 5** (computed, AR FY26 p.99)

**A2 Minimum single-year ROCE** (FY24-26 only) = 20.2% (FY25) → ≥15% → **Score 5**

**A3 Median ROE**: unaffected by the CE issue — Net Worth = Equity Capital + Reserves
(screener-standalone-Data_Sheet.csv), no current-liabilities split needed.
FY20 opening NW unavailable (no FY19 data in corpus) → FY20 ROE uses closing NW only, stated.
| FY | PAT | Avg NW | ROE |
|----|-----|--------|-----|
| 20 | 2.81 | 13.09 (closing only) | 21.5% |
| 21 | 3.90 | 15.04 | 25.9% |
| 22 | 8.71 | 20.75 | 42.0% |
| 23 | 11.42 | 28.30 | 40.4% |
| 24 | 12.33 | 36.95 | 33.4% |
| 25 | 21.45 | 94.61 | 22.7% |
| 26 | 37.34 | 165.71 | 22.5% |

Median (sorted 21.5,22.5,22.7,25.9,33.4,40.4,42.0) = 25.9% → ≥20% → **Score 5**

**A4 ROCE trend, latest vs earliest** — recomputed on the formula-compliant (exact) series only:
FY26 27.5% vs FY24 42.3% (earliest exact year) = decline of 14.8pp → "decline >5pp" → **Score 0**
(was 3 in run 1, which had compared a PROXY FY20 figure to an EXACT FY26 figure; that comparison is
withdrawn — see Correction Log item 1).

**Block A = 5+5+5+0 = 15/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

CFO (screener-standalone-Data_Sheet.csv, CASH FLOW block) cross-checked against AR/RHP cash flow
statements: FY22 CFO 7.28Cr = RHP restated 727.90L (RHP p.75/rendered offset). FY23 9.12Cr = RHP
912.22L. FY24 14.41Cr = AR FY25 comparative 1,441.02L (AR FY25 p.39/[page 39]). FY25 9.53Cr = AR FY26
comparative 953.13L (AR FY26 p.103/[page 103]) — NOTE: AR FY25's own FY25 column originally showed
918.68L; the FY26 AR restates it to 953.13L, consistent with the FY25/H1FY26 RESTATED labelling
flagged in B00/LBF3. FY26 8.83Cr = AR FY26 882.53L (AR FY26 p.103). All screener CFO figures
reconcile to the audited AR figures; treated as anchored.

Capex (Purchase of PPE incl. CWIP and capital advances, excludes investments/acquisitions):
- FY20, FY21: not disclosed in RHP (restated cash flow statement in corpus covers FY22-FY24 + stub
  period only) or in any AR. PROXIED by screener's "Cash from Investing Activity" (−1.27Cr, −2.64Cr)
  since these years predate any acquisition activity — marked PROXY, N/A precise breakdown. See
  Correction Log item 3: confirmed no score change either way.
- FY22: 666.63L (RHP p.75, restated cash flow statement) = 6.67Cr
- FY23: 407.34L (RHP p.75) = 4.07Cr
- FY24: 1,334.95L (AR FY25 p.39, FY24 comparative column, "Purchase of PPE incl. CWIP & Capital
  Advances") = 13.35Cr
- FY25: 3,845.00L (AR FY26 p.103, FY25 comparative column) = 38.45Cr (matches AR FY25's own FY25
  figure of 3,845.00L exactly — capex unrestated even though CFO was)
- FY26: 5,920.15L (AR FY26 p.103) = 59.20Cr

| FY | CFO (Cr) | Capex (Cr) | FCF (Cr) |
|----|----------|------------|----------|
| 20 | 2.77 | 1.27 (proxy) | 1.50 |
| 21 | 6.56 | 2.64 (proxy) | 3.92 |
| 22 | 7.28 | 6.67 | 0.61 |
| 23 | 9.12 | 4.07 | 5.05 |
| 24 | 14.41 | 13.35 | 1.06 |
| 25 | 9.53 | 38.45 | −28.92 |
| 26 | 8.83 | 59.20 | −50.37 |

FY26 FCF of −50.37Cr confirms the LBF2 first-verification-priority number (screener flagged FCF
≈ −Rs 50Cr FY26). Verified: driven by capex 59.20Cr for the Vadodara plant build-out (AR FY26 p.103,
CWIP jumped to 4,303.46L from 239.24L, AR FY26 p.99/[page 99]) against CFO of only 8.83Cr, itself
suppressed by inventory build (+3,698.11L working-capital drag, AR FY26 p.[103], cash flow statement
line "(Increase)/Decrease in inventories").

**B1 Cumulative CFO ÷ Cumulative PAT**: ΣCFO = 58.50Cr, ΣPAT = 97.96Cr → 0.597 → 0.50-0.69 band →
**Score 1**

**B2 FCF-positive years as proportion**: 5 of 7 years positive (FY20-24 positive, FY25-26 negative)
= 71.4% → 50-74% band → **Score 2**. (Excluding the proxied FY20-21: 3 of 5 years positive = 60%,
same band, same score — confirms Correction Log item 3.)

**B3 Cumulative FCF ÷ Cumulative PAT**: ΣFCF = −67.15Cr, ΣPAT = 97.96Cr → −0.686 → negative →
**Score 0**. (Excluding proxied FY20-21: ΣFCF FY22-26 = −72.57Cr, still negative, same score —
confirms Correction Log item 3.)

**B4 Change in WC Days, latest vs earliest**: Trade Payables are not in the screener Data_Sheet at
all (only Receivables, Inventory, Cash & Bank are broken out); sourced from RHP (FY22, FY23) and AR
FY26 (FY24 opening balance, FY25, FY26) financial-liability maturity notes. This limits the WC-days
comparison window to FY22-FY26 (5 years); FY20-21 payables are NOT FOUND anywhere in the corpus.

Trade Payables: FY22 772.51L (RHP p.[273], restated trade payables note) = 7.73Cr; FY23 1,432.27L
(RHP) = 14.32Cr; FY24 1,564.60L (AR FY26 p.[145], "As at 1 April 2024" maturity table) = 15.65Cr;
FY25 2,001.70L (AR FY26 p.[145]) = 20.02Cr; FY26 2,054.08L (AR FY26 p.[145]) = 20.54Cr.

Basis: revenue (no separate COGS line disclosed; Receivable/Inventory/Payable Days all on revenue
basis, stated per formula rule).

| FY | Recv Days | Inv Days | Pay Days | WC Days |
|----|-----------|----------|----------|---------|
| 22 | 53.0 | 69.5 | 43.4 | 79.1 |
| 23 | 66.4 | 66.3 | 57.8 | 74.9 |
| 24 | 42.1 | 72.8 | 52.7 | 62.2 |
| 25 | 67.7 | 72.4 | 48.9 | 91.2 |
| 26 | 47.4 | 103.4 | 31.9 | 118.9 |

Latest (FY26, 118.9 days) vs earliest available (FY22, 79.1 days) = increase of 39.8 days →
increased >15 → **Score 0**

**Block B = 1+2+0+0 = 3/20** — the weakest block. Deal-breaker #2 fires (Block B < 8).

**block_b_trend: deteriorating.** The one number: cumulative FCF/PAT = −0.69 (FY20-26); FY26 alone
carries FCF of −50.37Cr against a WC-days climb from 79.1 (FY22) to 118.9 (FY26), driven by the FY26
inventory jump (Inventory 66.65Cr vs 29.67Cr FY25, +125% YoY vs revenue +57% YoY — screener-
standalone-Data_Sheet.csv, BALANCE SHEET block) ahead of the Vadodara plant ramp.

---

## BLOCK C: GROWTH (Max 20)

Revenue (screener-standalone-Data_Sheet.csv): FY20 37.85Cr → FY26 235.16Cr, 6 years.
PAT: FY20 2.81Cr → FY26 37.34Cr, 6 years.

**C1 Revenue CAGR** = (235.16/37.85)^(1/6) − 1 = 35.6% → ≥20% → **Score 5**

**C2 PAT CAGR** = (37.34/2.81)^(1/6) − 1 = 53.9% → ≥20% → **Score 5**. No loss-to-profit swing;
PAT positive every year FY20-26.

**C3 Positive YoY revenue years**: FY21 declined (37.39 vs 37.85, screener), the only decline year
in 6 YoY transitions. 5/6 = 83.3% → 75-99% → **Score 3**

**C4 PAT CAGR minus Revenue CAGR** = 53.9% − 35.6% = +18.3pp → ≥+3pp → **Score 5**

**Block C = 5+5+3+5 = 18/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20), latest = FY26

EBITDA (computed) = PBT + Interest + Depreciation − Other Income = 50.07+3.98+6.33−3.67 = 56.71Cr
(screener-standalone-Data_Sheet.csv, PROFIT & LOSS block, FY26 column).

**D1 Net Debt ÷ EBITDA**: Net Debt = Borrowings 37.55Cr − Cash & Bank 20.06Cr = 17.49Cr (screener
FY26). 17.49/56.71 = 0.31x → 0-1.0x → **Score 4**

**D2 Interest Coverage** = EBIT ÷ Interest = 54.05/3.98 = 13.58x → ≥10x → **Score 5**

**D3 Debt ÷ Equity** = 37.55/184.00 (Equity Share Capital 14.28 + Reserves 169.72, screener FY26) =
0.204 → 0.1-0.5 → **Score 4**

**D4 Current Ratio** = Total Current Assets ÷ Total Current Liabilities = 13,243.43L / 6,770.80L
(AR FY26 p.99, standalone balance sheet, FY26 column) = 1.96x → 1.5-1.99 → **Score 4**

**Block D = 4+5+4+4 = 17/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20), latest = 31-Mar-2026 shareholding pattern

**E1 Promoter holding (latest)** = 57.94% (inputs/shareholding/2026-03-31_shareholding-pattern.pdf,
Table II, "Total Shareholding of Promoter and Promoter Group," 1,65,43,595 shares of 2,85,51,249) →
50-59.9% → **Score 4**

**E2 Promoter holding change over 3 years** — CORRECTED (see Correction Log item 2): no 3-year
shareholding history exists (listed 19-Dec-2024). Pre-offer promoter + group holding was 79.48% of
pre-offer capital (1,76,03,595 shares of 2,21,49,900 shares implied; RHP p.30, "Pre-Offer and Post
Offer Shareholding of Promoter"). Latest (31-Mar-2026) is 57.94% (1,65,43,595 of 2,85,51,249).
Mechanical change = −21.5pp → decreased >3% → **Score 0** (unchanged).

Decomposition of the −21.5pp: if promoter share count had NOT fallen (still 1,76,03,595) but the
denominator had grown to 2,85,51,249 (Fresh Issue + post-IPO issuance), promoter % would be
1,76,03,595 / 2,85,51,249 = 61.66%. So ~17.8pp of the decline (79.48% → 61.66%) is denominator
dilution from primary issuance. The remaining ~3.7pp (61.66% → 57.94%) comes from the promoter
share count itself falling by 10,60,000 shares (1,76,03,595 → 1,65,43,595).

CAUSE FOUND: the Dec-2024 RHP discloses a Promoter Offer for Sale of up to 11,30,000 Equity Shares
by Mr. Keyur Girishchandra Shah, the Promoter Selling Shareholder (RHP p.15, "B. Offer for Sale by
Promoter Selling Shareholder"). The actual fall (10,60,000 shares) sits just under that disclosed
ceiling of 11,30,000, consistent with the OFS executing near its full size at the IPO itself. This
is a one-time, disclosed, bounded promoter exit concentrated at the IPO, not an unexplained or
ongoing post-listing sell-down. It is also NOT explained by the Aug-2026 preferential allotment
(that allotment post-dates the 31-Mar-2026 measurement date and cannot be its cause — run 1's note
wrongly cited it; withdrawn).

Evidence that no further sell-down has occurred since listing: the promoter's absolute share count
(1,65,43,595) and % (57.94%) are IDENTICAL in both the 30-Sep-2025 and 31-Mar-2026 shareholding
patterns (inputs/shareholding/2025-09-30_shareholding-pattern.pdf and 2026-03-31_shareholding-
pattern.pdf).

Scored per the mechanical rule as instructed (Score 0). FLAG for downstream: read this as ~17.8pp
issuance dilution + ~3.7pp promoter OFS at the Dec-2024 IPO (RHP-disclosed, one-time), not as an
ongoing or unexplained promoter exit.

**E3 Promoter pledge (latest)**: 0%. Both shareholding patterns state "Whether any shares held by
promoters are encumbered under Pledged? No" (2026-03-31_shareholding-pattern.pdf, line 26/28; also
2025-09-30 pattern) → **Score 5**

**E4 Contingent Liabilities ÷ Net Worth**: Contingent liabilities (Tax Disputes only, excludes
Capital Commitments which are not contingent liabilities) = 80.51L (AR FY26 Note 37, [page in
extracted text], "Contingent Liabilities & Capital Commitments," FY26 column, total of Sales Tax/CST/
GST litigation lines). Net Worth FY26 = 184.00Cr. 80.51L = 0.805Cr. 0.805/184.00 = 0.44% → <5% →
**Score 5**. Note: Capital Commitments of 3,534.25L (same note) are excluded per the formula
definition (not a contingent liability); if erroneously included, the ratio would be 19.6% (15-30
band). Flagged so no downstream stage double-counts this.

**Block E = 4+0+5+5 = 14/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Peer Data_Sheets (QPOWER, POWERINDIA, VILAS) came out with EMPTY P&L/Balance Sheet/Cash Flow/
Quarters sheets per the collector (B00 input_gaps) — no peer numeric series exists in the corpus.
Every test requiring a peer figure is scored 0, marked PEER DATA NEEDED, never guessed.

**M1 Pricing Power**: EBITDA margin FY20 = (3.90+0.80+1.37−0.06)/37.85 = 15.9%. FY26 =
(50.07+3.98+6.33−3.67)/235.16 = 24.1%. Expansion = +8.2pp, Revenue CAGR 35.6% ≥10% →
condition "expanded ≥2pp AND CAGR≥10%" met → **Score 5**

**M2 Cost Advantage vs peer median EBITDA margin**: PEER DATA NEEDED → **Score 0**

**M3 Capital Efficiency**: FAT = Revenue ÷ Net Block = 235.16/51.80 = 4.54x (>3x); ROCE FY26 = 27.5%
(>20%, exact-method figure per Correction Log item 1) → **Score 5**

**M4 Customer Stickiness**: 1 revenue-decline year (FY21), fully recovered (FY22 +74% YoY) →
"max 1 decline year, fully recovered" → **Score 3**

**M5 Scale & Dominance**: PEER DATA NEEDED (mcap/margin ranking vs peers not in corpus) →
**Score 0**

**M6 Technology/R&D** — CORRECTED (see Correction Log item 4): the AR discloses a DSIR-recognised
in-house R&D centre (Scientific & Industrial Research Organisation status) with quantified spend.
AR FY26 standalone Note 43 ("Expenditure on Formulation and Development (R&D)") gives R&D expenditure
of ₹100.78 Lakh (FY26) and ₹109.94 Lakh (FY25); the AR FY25 Board's Report technology-absorption
annexure independently states FY25 R&D expenditure of ₹109.94 Lacs (AR FY25, "3. Expenditure incurred
on Research and Development"). Revenue: FY26 235.16Cr = 23,516L, FY25 149.57Cr = 14,957L
(screener-standalone-Data_Sheet.csv). R&D/Revenue: FY26 = 100.78/23,516 = 0.43%; FY25 = 109.94/14,957
= 0.74%. Both years sit below the lowest test band (≥1%) → **Score 0** (unchanged from run 1's
result, now grounded on found figures instead of a "no disclosure" claim).

**M7 Regulatory/License**: No license/quota/regulated-player-count evidence in the provided data;
transformer bushings is not disclosed as a licensed segment → unregulated per available evidence →
**Score 0**

**M8 Distribution**: No quantified distribution-reach or per-outlet revenue data in the corpus →
N/A (not in provided data) → **Score 0**

**M9 Brand**: Gross margin proxy = (Revenue − Material Cost)/Revenue, proxy stated. FY26 =
(235.16−124.48)/235.16 = 47.1%. No peer gross margin available to compare against → PEER DATA
NEEDED → **Score 0**

**M10 Switching Costs**: Revenue grew all years but 1 (FY21 decline); Receivable Days FY20 = 7.01/
37.85×365 = 67.6 days, FY26 = 47.4 days — days FELL 20.2, which satisfies "stable" (no rise) under
the growth-all-but-1-year band → **Score 3**

**M11 Network Effects** (7 years available, ≥6yr test qualifies; see Correction Log item 5): Latest
3yr revenue CAGR (FY23→FY26, 90.36→235.16) = 37.6%; prior 3yr CAGR (FY20→FY23, 37.85→90.36) = 33.7%.
Latest > prior. Selling & admin expense as % of sales: FY20 9.3%, FY26 7.5%, declining. Both
conditions met → **Score 5** (mechanical rubric application; verifier B12c confirms this is the
correct mechanical result). FLAG, unchanged and sharpened from run 1: this is a mechanical pass on a
two-window revenue-growth/opex-ratio test only. YASHHV is a build-to-spec transformer-bushing
component maker with no disclosed network-effect mechanism anywhere in the corpus (no platform, no
user base, no multi-sided market). Gate 0 has no discretion to override its own numeric rubric (rule
2, "No qualitative judgments"); the score stands as computed. Stage 7's qualitative moat scan is
expected to override this to NO EVIDENCE, and downstream stages (Halt 1 dossier, Role 1/2) should use
stage 7's moat count once available, not Gate 0's mechanical 5-moat count, for any qualitative
argument about moat durability.

**M12 Negative WC / Float**: WC Days FY22-26 = 79.1, 74.9, 62.2, 91.2, 118.9 — all >45 in every year
with data → **Score 0**

**Moat score = 5+0+5+3+0+0+0+0+0+3+5+0 = 21/60**

Moats present (score ≥3): M1, M3, M4, M10, M11 = **5 moats confirmed** (Gate 0's own mechanical
count; expected to become 4 once stage 7 overrides M11 — see flag above).

Moat classification: 5 present → 4-5 band → **STRONG**

---

## CLASSIFICATION

| Block | Score | /Max |
|-------|-------|------|
| A — Return on Capital | 15 | 20 |
| B — Cash Generation Quality | 3 | 20 |
| C — Growth | 18 | 20 |
| D — Balance Sheet Strength | 17 | 20 |
| E — Shareholder Alignment | 14 | 20 |
| **Core Score** | **67** | **100** |
| F — Moat Score | 21 | 60 |
| **Grand Total** | **88** | **160** |

Data confidence: 7 years of P&L/BS/CF history (FY20-26) → 7-9 band → **moderate**. The ROCE-scored
window (FY24-26 exact, per Correction Log item 1) is shorter, 3 years; Trade Payables/WC-days history
is shorter (FY22-26, 5 years); shareholding/pledge history is shorter still (company listed
19-Dec-2024, under 2 years). No automatic downgrade tier applies to the 7-year primary window; the
shorter sub-windows are flagged inline above and in data_notes, not scored as a separate confidence
downgrade.

Moat classification: STRONG (5 of 12 tests present, ≥3 each, on Gate 0's own mechanical count)

Classification matrix: Core 67 (60-79 band) + STRONG → matrix says GOOD+.

**Deal-breaker overrides checked:**
1. Block A <8? No (15). Not triggered.
2. **Block B <8? YES (3). TRIGGERED → caps classification at max GOOD.**
3. Median ROCE <10%? No (27.5% on the exact-method series). Not triggered.
4. Cumulative CFO/PAT <0.50? No (0.597, close to the 0.50 line but above it). Not triggered.
5. Pledge >15%? No (0%). Not triggered.
6. ND/EBITDA >3x AND IC <3x? No (0.31x and 13.58x). Not triggered.
7. Revenue declined in majority of years? No (1 of 6 YoY transitions). Not triggered.
8. PAT negative in any of last 3 years? No (positive FY24, FY25, FY26). Not triggered.
9. History <3 years? No (7 years). Not triggered.

**Final classification: GOOD** (matrix would say GOOD+ on Core 67 + STRONG moat, but deal-breaker #2
— Block B, cash generation quality, at 3/20 — caps it at GOOD. The years driving this deal-breaker
are FY25 and FY26: capex for the Vadodara plant (38.45Cr FY25, 59.20Cr FY26) outran operating cash
flow (9.53Cr, 8.83Cr), and inventory build (+125% YoY in FY26) added to the working-capital drag.
FY20-24 cash conversion was not the problem — 5 of those 5 years were FCF-positive. This
classification is unchanged from run 1; only the Core Score and its A4 component changed, per
Correction Log item 1.)

Strongest block: A (Return on Capital, 15/20) and C (Growth, 18/20). C is now the single strongest
block after the A4 correction (was tied A/C at 18 each in run 1).
Weakest block: B (Cash Generation Quality, 3/20).

**Decision line: GOOD, with the classification capped by a single, dated, capex-driven cash
deal-breaker (Block B <8, FY25-26) rather than a durable earnings-quality problem. Returns on
capital are strong on the formula-exact FY24-26 window (27.5-42.3%) but the exact-method trend is
declining (−14.8pp FY24 to FY26), a genuine finding this run surfaces that run 1's proxy-blended
trend understated. Growth is at or near the top band. The cash story needs verification against the
Vadodara plant's completion timeline and the resulting inventory unwind, per LBF1/LBF2/LBF4.**

---

## DATA NOTES

- No loss-to-profit swing: PAT positive in all 7 years (FY20-26).
- ROCE (Block A) is fixed-formula (Total Assets − Total Current Liabilities), scored only on the
  3 years where the exact formula is computable (FY24-26): median 27.5%, minimum 20.2% (both A1/A2
  Score 5), trend FY24 42.3% → FY26 27.5% = −14.8pp (A4 Score 0). FY20-23 ROCE (Equity+Reserves+
  Borrowings proxy: 28.3%, 31.9%, 42.1%, 43.6%) is NOT scored; shown as unscored supplementary
  context only, per the "fixed, do not substitute" rule (verifier B12c MJ-2, corrected this run).
- Capex FY20-21 PROXIED by screener's aggregate "Cash from Investing Activity" line (no RHP/AR
  breakdown exists for these pre-restatement-window years); FY22-26 capex is EXACT from RHP/AR
  cash flow statements. Confirmed no score change to B2/B3 whether these two years are included or
  excluded (verifier B12c MN-1).
- Trade Payables (needed for WC Days / B4) are NOT FOUND in the screener Data_Sheet at all and NOT
  FOUND in the corpus for FY20-21; sourced from RHP (FY22-23) and AR FY26 (FY24-26). B4 is computed
  on the FY22→FY26 window (5 years), not the full FY20→FY26 window.
- FY25 CFO is RESTATED between AR FY25 (918.68L, its own FY25 column) and AR FY26 (953.13L, FY25
  comparative column) — a 34.45L (₹0.34Cr) upward restatement. Capex for FY25 is unchanged
  (3,845.00L in both). No restatement reason found in the AR FY26 text searched; per LBF3, the
  reason should come from the auditor's report or AR FY26 notes not yet located — carried forward
  as an open item for later stages.
- PEER DATA NEEDED: M2 (Cost Advantage), M5 (Scale & Dominance), M9 (Brand) all require peer
  numeric series; QPOWER/POWERINDIA/VILAS Data_Sheets came out empty per B00 input_gaps. Scored 0,
  not guessed.
- M6 (Technology/R&D) — CORRECTED this run: R&D expenditure IS disclosed (AR FY26 Note 43, AR FY25
  Board's Report annexure), DSIR-recognised in-house SIRO status confirmed. R&D/Revenue FY26 0.43%,
  FY25 0.74%, both below the ≥1% lowest test band → Score 0 stands, now grounded (run 1's search for
  "Research and Development"/"R&D expenditure" literal strings missed the Note 43/Note 34 headings
  and Board's Report annexure; corrected search found them).
- M7 (Regulatory/License), M8 (Distribution): N/A, not in provided data.
- M9 gross-margin proxy stated: (Revenue − Material Cost) ÷ Revenue = 47.1% FY26. Proxy used because
  no separate COGS line is disclosed; still 0-scored for lack of a peer comparator.
- M10 (Switching Costs) passes the mechanical numeric test; M11 (Network Effects) also passes the
  mechanical numeric test but the business (build-to-spec transformer-bushing component maker) has
  no disclosed network-effect mechanism in the corpus read for this stage — flagged for the stage 7
  qualitative moat scan to confirm or override (verifier B12c confirms Gate 0's mechanical
  application of M11 is correct; the override, if any, belongs to stage 7, not this stage).
- E2 (promoter holding change), CORRECTED this run: scored 0 mechanically (−21.5pp vs pre-offer).
  Decomposed: ~17.8pp is issuance/denominator dilution (Fresh Issue + post-IPO issuance); ~3.7pp is
  the promoter's own share count falling by 10,60,000 shares. CAUSE FOUND: RHP-disclosed Promoter
  Offer for Sale of up to 11,30,000 shares by Mr. Keyur Girishchandra Shah at the Dec-2024 IPO
  (RHP p.15). This is a one-time, bounded, disclosed promoter exit at the IPO, not an ongoing or
  unexplained sell-down; promoter % and absolute share count are unchanged between the 30-Sep-2025
  and 31-Mar-2026 shareholding patterns, confirming no further sell-down since listing. Run 1's note
  ("dilution, not sell-down," citing the Aug-2026 allotment) is withdrawn as ungrounded per verifier
  B12c MJ-3; this note replaces it.
- E4: Contingent liabilities figure (80.51L, FY26) excludes Capital Commitments (3,534.25L) per the
  formula definition. If Capital Commitments were wrongly included, the ratio would be 19.6%
  (15-30% band, Score 1 instead of 5) — flagged to prevent downstream double-counting.
- Reporting units: screener in ₹ Cr; AR/RHP/results in ₹ Lakh on the face of the document. Every
  Lakh-sourced figure above is shown with its Lakh anchor plus the Cr conversion, per instruction.
