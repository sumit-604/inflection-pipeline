# STAGE 1: GATE 0 SCORECARD — Vinyas Innovative Technologies Ltd (VINYAS)
Run date: 2026-09-01 | Model: claude-sonnet-5 | run_type: full

Data available: 7 years (FY2020 to FY2026), from screener-Data_Sheet.csv (P&L,
Balance Sheet, Cash Flow) cross-checked against the FY26 audited standalone
and consolidated results (VINYAS_28052026155354_OutcomeBM280526final.pdf) and
the FY2025-26 Annual Report (SME_AR_30897_VINYAS_2025_2026...pdf). Scoring is
adapted to this 7-year history for growth, ROE and shareholding metrics.
ROCE (A1/A2/A4), full Working Capital Days including payables (B4), and FCF
(B2/B3) are limited to 2 years (FY2025-FY2026) because the screener export
does not split current vs non-current liabilities or disclose trade
payables for FY2020-FY2024, and no annual report earlier than FY2025-26 was
provided in this run's inputs. This is a material data limitation, flagged
below and in the YAML block.

Screener sub-sheets (Profit_Loss.csv, Balance_Sheet.csv, Cash_Flow.csv,
Quarters.csv, Customization.csv) are unpopulated exports; all screener
figures below are anchored to screener-Data_Sheet.csv only.

## SPEAR LOAD-BEARING FACTS — VERIFICATION STATUS
1. Customer concentration: NOT DISCLOSED numerically FY23-FY26. AR MD&A
   (p.44, "Enterprise Risk Management") lists "customer concentration" only
   as a monitored risk category, no percentage given anywhere in the
   provided sources.
2. Material cost as % of revenue: FOUND. RM/Sales (screener-Data_Sheet.csv)
   FY20 99.96%, FY21 70.03%, FY22 69.79%, FY23 73.93%, FY24 74.65%,
   FY25 71.14%, FY26 78.90%. FY25/FY26 cross-checked against AR Note 20
   "Cost of Materials Consumed": FY26 Rs40,576.99L/Revenue Rs51,432.37L =
   78.90% (exact match); FY25 Rs28,948.38L/Rs39,663.56L = 72.98% (screener
   figure 71.14% is ~1.8pp lower, likely a stores/consumables
   classification difference between the screener's simplified P&L and the
   statutory note; both anchored, difference noted).
3. Repeat vs new revenue: NOT DISCLOSED. AR Business Overview (p.41,
   "Customer Relationships") states the company "secure[s] repeat business
   from several marquee customers" qualitatively, no % split given.
4. Root cause of 161-day receivables: PARTIALLY ADDRESSED, not verified.
   AR Note 35(f) "Analytical Ratios" explanation column: trade receivables
   turnover declined "mainly due to higher year-end receivables from
   increased business volumes and customer-specific project timelines."
   This is the company's own stated explanation, not independently
   evidenced in the provided sources. Flagged for downstream verification.
5. MARGIN PUZZLE: CONFIRMED, unresolved. Material cost/revenue rose from
   71.14% (FY25, screener basis) to 78.90% (FY26) — a 7.76pp increase — in
   the same year OPM rose from 11.09% to 12.50% (AR "Key Financial Ratios,"
   p.43; +142bps). The offsetting cost-line movement is not traceable from
   this run's sources (screener's "Other Expenses" line jumps from
   Rs0.51Cr FY25 to Rs11.65Cr FY26 in a way that does not reconcile cleanly
   to AR Note 25 "Other expenses" Rs978.94L/Rs1,165.63L). Flagged for
   downstream cost-line reconciliation.

---
## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 14/20

ROCE = EBIT / (Total Assets - Current Liabilities), computed per year.
Computable only for FY2025 and FY2026 (current/non-current liability split
available only from the FY26 AR standalone balance sheet, which carries the
FY25 comparative; FY20-FY24 screener data lumps Borrowings + Other
Liabilities with no current/non-current split — marked NOT FOUND).

- FY2025: EBIT (Profit before Interest & Exceptional Items) = Rs3,869.53L
  (AR standalone results, year ended 31-Mar-2025); Capital Employed =
  Total Assets Rs33,002.76L - Current Liabilities Rs17,106.46L =
  Rs15,896.30L. ROCE = 24.34% (AR p.68-69, computed).
- FY2026: EBIT = Rs5,773.39L (AR standalone results / Board's Report p.47,
  "Profit before Interest & Exceptional Items"); Capital Employed =
  Total Assets Rs46,837.44L - Current Liabilities Rs21,603.33L =
  Rs25,234.11L. ROCE = 22.88% (AR p.85/p.110, computed).
- FY2020-FY2024: NOT FOUND (current liabilities breakdown unavailable).
- Cross-check: AR's own "Return on Capital Employed" (Note 35j, different
  denominator = Tangible Net Worth + non-current debt only) reports
  25% (FY25) and 24% (FY26) — anchored but not used for scoring since it
  is not the pipeline's fixed formula.

A1 Median ROCE (2 data points, median = average) = 23.61% → 20-24.9% band
   → **Score 4**
A2 Minimum single-year ROCE = 22.88% (FY26) → ≥15% band → **Score 5**
A3 Median ROE (7 years, average net worth basis; opening NW unavailable
   for FY20 so closing-only used per formula rule):
   FY20 4.38% | FY21 4.04% | FY22 3.25% | FY23 19.07% | FY24 17.67% |
   FY25 14.12% | FY26 16.14% (all: screener-Data_Sheet.csv Equity Share
   Capital + Reserves, computed). Cross-check: AR Note 35(d) "Return on
   Equity Ratio" reports 14% (FY25) / 16% (FY26) — exact match to this
   computation. Median (4th of 7 sorted) = 14.12% → 12-14.9% band →
   **Score 2**
A4 ROCE trend, latest (FY26 22.88%) vs earliest available (FY25 24.34%) =
   decline of 1.46pp → decline 1-3pp band → **Score 3**

Block A total: 4+5+2+3 = **14/20**

---
## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 3/20

B1 Cumulative CFO / Cumulative PAT (7-year window, screener-Data_Sheet.csv
   Cash from Operating Activity and Net profit rows):
   CFO: 15.36 -24.65 +11.82 +11.59 -28.87 +8.78 -32.30 = **-38.27 Cr**
   PAT: 1.32+1.23+1.01+7.34+15.35+19.42+30.87 = **76.54 Cr**
   Ratio = -0.50 → negative, <0.50 band → **Score 0**
   (Recent 3-year window, FY24-FY26, matching company memory: CFO
   -28.87+8.78-32.30 = -52.39 Cr vs PAT 65.64 Cr, ratio -0.80 — same
   conclusion under either window.)
B2 FCF-positive years as proportion (only 2 years computable — see B3):
   1 of 2 years positive = 50% → 50-74% band → **Score 2**
B3 FCF = CFO - Capex. Capex basis: PPE Note 2 gross additions (FY25:
   Rs220.97L; FY26: Rs3,089.06L) plus FY26 Capital Work in Progress
   movement (Rs450.34L, Consolidated CF Statement, AR p.113). FY20-FY24
   capex NOT FOUND (screener gives only net "Cash from Investing
   Activity," not split into capex vs other investing items).
   FY25 FCF = CFO Rs8.78Cr - Capex Rs2.21Cr = **+Rs6.57Cr**
   FY26 FCF = CFO -Rs32.30Cr - Capex Rs35.39Cr = **-Rs67.69Cr**
   Cumulative FCF (2yr) = -Rs61.12Cr; Cumulative PAT (2yr) = Rs50.29Cr
   Ratio = -1.22 → negative → **Score 0**
B4 Change in WC Days, latest vs earliest computable year. Full formula
   (Receivable Days + Inventory Days - Payable Days) needs Trade Payables,
   disclosed only for FY25/FY26 (AR Note 14.2).
   FY25: Receivable Days 162.97 + Inventory Days 70.34 - Payable Days
   28.35 = **204.96 days**
   FY26: Receivable Days 161.15 + Inventory Days 91.29 - Payable Days
   34.82 = **217.62 days**
   Change = +12.66 days → increased 5-15 band → **Score 1**
   (Receivable-days-only proxy across all 7 years, screener basis:
   FY20 64.96, FY21 51.76, FY22 100.25, FY23 32.60, FY24 101.33,
   FY25 162.97, FY26 161.15 — closely matches company memory's cited
   "33/101/163/161" for FY23-FY26.)

Block B total: 0+2+0+1 = **3/20** — weakest block by a wide margin.

---
## BLOCK C: GROWTH (Max 20) — Score: 20/20

C1 Revenue CAGR FY20 (Rs149.67Cr) to FY26 (Rs514.32Cr), 6-year window
   (screener-Data_Sheet.csv) = (514.32/149.67)^(1/6)-1 = **22.84%** →
   ≥20% band → **Score 5**
C2 PAT CAGR FY20 (Rs1.32Cr) to FY26 (Rs30.87Cr) = (30.87/1.32)^(1/6)-1 =
   **69.1%**. Both endpoints positive, no loss-to-profit swing.
   ≥20% band → **Score 5** (flag: driven by an unusually thin FY20 base;
   recent 3-year PAT CAGR FY23-FY26 = 61.4%, still very strong.)
C3 Positive YoY revenue years: all 6 YoY periods FY20-FY26 positive
   (100%) → **Score 5**
C4 PAT CAGR (69.1%) minus Revenue CAGR (22.84%) = +46.3pp → ≥+3pp band →
   **Score 5**

Block C total: 5+5+5+5 = **20/20** — strongest block.

---
## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 12/20
(Latest year = FY2026; all figures from AR Note 28 "Financial Instruments,"
Note 8.2 "Cash and bank balance," Board's Report p.47, and AR Note 35
"Analytical Ratios," cross-validated against screener-Data_Sheet.csv)

D1 Net Debt/EBITDA: Total Borrowings Rs130.06Cr (Note 28, carrying value)
   - Cash & Bank Rs18.45Cr (Note 8.2) = Net Debt Rs111.61Cr. EBITDA
   Rs64.77Cr (Board's Report p.47). Ratio = 1.72x → 1-2x band →
   **Score 3**
D2 Interest Coverage: EBIT Rs57.73Cr / Interest Rs15.59Cr = 3.70x
   (matches AR's own "Interest Coverage Ratio" 3.70, Note 35/p.43 exactly)
   → 3-4.9x band → **Score 2**
D3 Debt/Equity: Rs130.06Cr / Rs235.72Cr = 0.55 (matches AR's own
   Debt-Equity Ratio 0.55, Note 35b exactly) → 0.5-1.0 band → **Score 3**
D4 Current Ratio: 1.82 (AR's own ratio, Note 35a, exactly reproduced by
   Current Assets Rs394.27Cr / Current Liabilities Rs216.03Cr) →
   1.5-1.99 band → **Score 4**

Block D total: 3+2+3+4 = **12/20**

---
## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 9/20

E1 Promoter holding, latest quarter (31-Mar-2026): **29.40%** (AR Note 10c
   "Shareholding by Promoters," and Corporate Governance p.53 "Pattern of
   Shareholding," 36,99,402 shares / 1,25,84,726). FII/DII combined per
   the same pattern table = FII 0.49% + Bodies Corporate 11.68% (not a
   clean FII+DII split; company memory's "7.02%" not independently
   reconciled from this table). Not "professionally managed" (promoter
   family holds 3 of 6 board seats, MD + 2 WTDs). <30% band →
   **Score 0**
E2 Promoter holding change, available window: 29.38% (30-Sep-2024, H1
   FY26 results PDF) to 29.40% (31-Mar-2026, AR Note 10c) = +0.02pp.
   Full 3-year window NOT FOUND — company listed on NSE Emerge in 2023
   (AR corporate timeline p.12) and no pre-listing or FY23/FY24
   shareholding disclosure was in this run's sources; only ~18 months of
   quarterly data available. Within the available window: ±1% band →
   **Score 3** (data-limited, flagged).
E3 Promoter pledge, latest: 0% (results PDF pledge/encumbrance table
   shows nil for both promoter categories, FY26) → **Score 5**
E4 Contingent Liabilities / Net Worth, latest (AR Note 36): Income Tax
   demand Rs24.04L + VAT demand Rs2.40L + labour litigation Rs650.00L +
   GST demand Rs372.94L + Bank Guarantees Rs3,568.30L = **Rs4,617.68L
   (Rs46.18Cr)**. Net Worth FY26 = Rs235.72Cr. Ratio = 19.59% → 15-30%
   band → **Score 1** (dominated by Rs35.68Cr of outstanding bank
   guarantees, standard for a defence-EMS order book, not a distress
   signal by itself; labour litigation of Rs6.50Cr unchanged FY25-FY26).

Block E total: 0+3+5+1 = **9/20**

---
## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 18/60, 4 moats present

M1 Pricing Power: EBITDA margin FY20 8.25% (computed: PBT+Interest+Dep /
   Sales) to FY26 12.59% (computed) / 12.50% (AR, total-income basis) =
   +4.3pp expansion; Revenue CAGR 22.84% ≥10%. Both conditions met →
   **Score 5**
M2 Cost Advantage vs peer median: PEER DATA NEEDED (no peer EBITDA margin
   data in provided sources) → **Score 0**
M3 Capital Efficiency: FAT (Sales/Net Block) FY26 = 514.32/64.73 = 7.95x
   (>3x); ROCE FY26 22.88% (>20%). Both met → **Score 5**
M4 Customer Stickiness: zero revenue-decline years (fits "max 1 decline
   year" tier) but receivable days NOT stable ±10 (rose 33→161 days,
   disqualifying the top band) → **Score 3**
M5 Scale & Dominance: PEER DATA NEEDED (no peer mcap/margin ranking data)
   → **Score 0**
M6 Technology/R&D: R&D spend not separately disclosed as a % of revenue
   in the provided sources → NOT FOUND → **Score 0**
M7 Regulatory/License: number of listed peers in the defence-EMS segment
   NOT FOUND in provided sources (PEER DATA NEEDED) → **Score 0**
M8 Distribution: not applicable — B2B contract manufacturer to OEMs, no
   distribution/outlet network metric in the business model (AR p.34,
   "one geographical segment," direct OEM relationships) → **Score 0**
M9 Brand: GM proxy (Revenue - Material Cost)/Revenue = 21.11% FY26,
   28.86%(screener basis) FY25, but no peer GM median available to
   complete the comparison → PEER DATA NEEDED → **Score 0**
M10 Switching Costs: revenue grew every year (better than "growth all but
   1 year"), but receivable days rose 128 days over FY23-FY26, far
   exceeding the "≤10 days" and "stable" conditions in both the 5- and
   3-point bands; the residual "2+ decline years" band does not apply
   (0 decline years) → **Score 0** (flagged: this is a genuine red flag —
   growth financed partly by extending customer payment terms, consistent
   with spear fact #4).
M11 Network Effects (7 years available, ≥6 required): latest-3yr revenue
   CAGR (FY23-FY26) 30.0% > prior-3yr CAGR (FY20-FY23) 16.16%. Selling &
   admin expense as % of sales: FY20 3.20% declining to FY25 1.69%
   (screener-Data_Sheet.csv); FY26 selling & admin not separately
   disclosed in the screener export (merged into "Other Expenses") —
   data gap flagged. Directional trend (declining) plus the CAGR
   acceleration condition → **Score 5**
M12 Negative WC/Float: WC days computable only FY25 (204.96) and FY26
   (217.62), both far above 45 → >45 band → **Score 0**

Moats present (score ≥3): M1, M3, M4, M11 = **4 moats**
Moat classification (4-5 present = STRONG): **STRONG**
Block F total: 5+0+5+3+0+0+0+0+0+0+5+0 = **18/60**

---
## CLASSIFICATION AND OVERRIDES

Data confidence: 7 years of P&L/growth/ROE data → "7-9 moderate" band, no
automatic history downgrade triggered. Separately (not covered by this
band rule): ROCE, full WC Days and FCF rest on only 2 usable years
(FY25-FY26) — flagged as a material sub-metric limitation, not a general
history-depth downgrade.

Core score (A+B+C+D+E) = 14+3+20+12+9 = **58/100**
Moat score = **18/60**
Grand total = **76** (58 core + 18 moat)
Moats confirmed = **4** | Moat class = **STRONG**

Deal-breaker check:
1. Block A <8? No (14). Not triggered.
2. Block B <8? **Yes (3)** → caps at max GOOD.
3. Median ROCE <10%? No (23.61%). Not triggered.
4. Cumulative CFO/PAT <0.50? **Yes (-0.50)** → caps at max AVERAGE.
5. Pledge >15%? No (0%). Not triggered.
6. ND/EBITDA >3x AND IC <3x? No (1.72x / 3.70x). Not triggered.
7. Revenue declined in majority of years? No. Not triggered.
8. PAT negative in any of last 3 years? No (FY24 15.35, FY25 19.42,
   FY26 30.87, all positive). Not triggered.
9. History <3 years? No (7 years). Not triggered.

Base matrix position: Core 58 (60-79 band, just below) — Core is actually
58, which falls in the "Core 40-59 = AVERAGE" band on its own; even before
deal-breakers, the base classification from the matrix is **AVERAGE**
(Core 58 sits in the 40-59 bucket, one point under the 60-79/STRONG "GOOD+"
threshold). Deal-breaker 4 (cumulative CFO/PAT <0.50, cap max AVERAGE)
would in any case cap classification at AVERAGE even had Core cleared 60.

**FINAL CLASSIFICATION: AVERAGE**

Strongest block: Block C, Growth (20/20) — perfect score, but flagged as
partly a low-FY20-base artifact; recent 3-year growth remains strong on
its own terms.
Weakest block: Block B, Cash Generation Quality (3/20) — cumulative
CFO/PAT negative across every window tested, FY26 recorded the worst
operating cash flow of the 7-year period (-Rs32.30Cr) against the highest
-ever PAT (Rs30.87Cr).

Decision line: PROCEED is not this stage's call (Gate 0 has no STOP/PROCEED
verdict per pipeline rules) — classification AVERAGE, driven by a genuine
and severe cash-conversion deal-breaker sitting underneath strong reported
growth, margin and ROE trends. This is the exact pattern the Section 1B
CONVERTER-classification and Amendment 17 guardrails exist to catch;
downstream stages should treat cash-conversion quality, receivable-days
root cause, and the FY26 margin puzzle as first-priority verification
items alongside the spear load-bearing facts.

---
## DATA NOTES
- ROE computed on average-net-worth basis per the pipeline's fixed formula;
  this exactly matches AR Note 35(d) "Return on Equity Ratio" (14%/16% for
  FY25/FY26). AR's separately reported "Return on Net Worth" (13.10%/13.22%,
  Financial Performance p.43) uses a closing-net-worth-only basis and is
  NOT used for scoring here, cited only as a cross-check.
- AR's own "Return on Capital Employed" (Note 35j: 24%/25% FY26/FY25) uses
  Capital Employed = Tangible Net Worth + non-current debt only, a
  narrower base than this scorecard's fixed formula (Total Assets -
  Current Liabilities). Both are anchored; this scorecard uses the fixed
  formula per pipeline rules (22.88%/24.34%).
- No loss-to-profit swing: PAT positive in all 7 years (FY20 Rs1.32Cr to
  FY26 Rs30.87Cr).
- PEER DATA NEEDED: M2, M5, M7, M9 all scored 0 for lack of peer data in
  provided sources — not evidence of moat absence, evidence of missing
  inputs.
- Capex basis note: FY25/FY26 use PPE Note 2 gross additions (+ FY26 CWIP
  movement); FY20-FY24 capex NOT FOUND because screener-Data_Sheet.csv
  gives only net "Cash from Investing Activity," not split into capex vs
  other investing items.
- Promoter holding 29.40% (just under the E1 30% threshold) reflects
  NSE-Emerge public-float dilution since the 2023 listing, not promoter
  selling; the % has been essentially flat (29.38%-29.40%) across every
  quarter available in this run's sources (Sep-2024 to Mar-2026).
- Screener sub-sheets (Profit_Loss.csv, Balance_Sheet.csv, Cash_Flow.csv,
  Quarters.csv) are unpopulated in the provided export; all
  screener-sourced figures in this report are anchored to
  screener-Data_Sheet.csv specifically.

## INPUT GAPS CARRIED FORWARD
- Prospectus absent (company long-listed on NSE Emerge since 2023, not a
  high-priority gap per orchestrator note).
- Announcements folder absent; operator ferried a 6-month event timeline
  separately (downstream tier, not used in this scorecard).
- Shareholding folder absent; operator ferried the quarterly pattern
  separately. This run's shareholding figures are sourced instead from
  the FY26 AR and the H1 FY26 results PDF, which together cover only
  Sep-2024 through Mar-2026 (see E2 note above).
- Research and "other" folders absent.
- Balance sheet current/non-current liability split and trade payables
  unavailable for FY2020-FY2024 (no annual report earlier than FY2025-26
  provided) — this is the single largest data gap in this run, driving
  the A1/A2/A4/B3/B4/M12 limitations noted throughout.
