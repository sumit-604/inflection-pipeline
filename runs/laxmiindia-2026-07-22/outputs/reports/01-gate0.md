# STAGE 1: GATE 0 QUANTITATIVE SCORECARD — Laxmi India Finance Ltd (LAXMIINDIA)
Run date: 2026-07-22 | Model: claude-sonnet-5 | Mode: pipeline

**Company type: NON-BANK FINANCE COMPANY (NBFC)** — MSME/vehicle/construction-loan lender,
Rajasthan-based, Baid family promoters, RBI Middle-Layer NBFC. Listed 2025-07-31 (IPO). Per
CLAUDE.md/task instructions, NBFC treatment applied throughout: NIM/ROA/ROE/CRAR/GNPA/NNPA/
credit cost score in place of asset-turns, inventory days, and conventional working-capital
metrics, which are marked IRRELEVANT rather than scored against operating-company norms.

Data available: **4 years (FY23 to FY26)**. Scoring adapted to 4-year history — see Data
Confidence section (this triggers the framework's "3-4 years = LIMITED, downgrade one tier"
rule).

## SOURCES READ (all anchors below cite these)
- **DRHP** = inputs/annual-report/drhp.pdf — Prospectus dated 2025-07-31, 525pp. Restated
  Financial Statements (FY23/FY24/FY25, audited-restated) at printed pp.75-77, 279-288(KPI/ratio
  tables), 340-354 (notes 30-51), 381-391 (ratio disclosures/EBITDA/KPIs), 91-100 (shareholding).
- **AR26** = inputs/results/Annual_Report_2024.pdf (misnamed; actually FY26 AUDITED full-year
  results filed 2026-05-13) — P&L/BS/CF statements + Reg.52(4) ratio table.
- **Q3FY26** = inputs/results/41b31cc6-d660-47af-b768-daaf6d68163d.pdf — unaudited 9M/Q3 FY26
  (Dec 2025), limited-review, filed 2026-02-10. Used only as a cross-check for FY26 trend
  continuity, not as the primary FY26 anchor (AR26 audited full-year wins).
- **IP** = inputs/presentation/Investor_Presentation_1.pdf — Q4/FY26 investor deck, pp.5-16,
  contains the only available FY23-FY26 4-year trend charts and FY26 P&L/BS statements.
- **operator-context.md** — NON-ANCHORED. Used only as lead/cross-check per task instructions;
  every scored number below is anchored to one of the four PDFs above. Where operator figures
  agreed with an anchored source this is noted as a positive cross-check; the anchored figure is
  always the one scored.

## input_gaps carried forward from B00 (unchanged)
announcements, shareholding, research, laxmiindia_screening all absent — operator supplied
non-anchored summaries only for shareholding/announcements. No LAXMIINDIA screening CSV exists;
this stage extracted all financials directly from the four PDFs above.

---

## KEY NBFC-ADAPTATION NOTES (read before the blocks below)
1. **Block B (cash-generation quality) is structurally near-zero for any growing NBFC.** Loan
   disbursements net of collections are classified as an *operating* cash outflow under Ind AS
   (loans are the lender's core operating asset), while the funding for that growth shows up as
   a large *financing* cash inflow. This is textbook for a scaling secured lender, not a
   going-concern or earnings-quality problem. It is scored literally per the fixed formula
   (CLAUDE.md: "formula definitions fixed, do not substitute alternatives") and flagged heavily
   below rather than silently overridden.
2. **ROCE (Block A) does not have a clean current/non-current split on an NBFC balance sheet.**
   DRHP Note 34 (Maturity Analysis) discloses "liabilities due within 12 months" for FY23-25;
   the FY26 equivalent is taken from the investor-presentation ALM table ("Cumulative
   Liabilities, upto 1 year"). EBIT = PBT + Finance Costs (this exactly reproduces the company's
   own "Interest Coverage Ratio" in IP p.10, cross-checked below), consistent with treating
   interest expense as a financing, not operating, cost. This is an adaptation, not a DRHP-stated
   ratio — flagged.
3. **D1/D2 use CRAR/PCR per the framework's explicit financial-company override.** D3
   (Debt/Equity) uses the framework's explicit "Financials: default 3." D4 (Current Ratio) is
   marked **IRRELEVANT** — the company's own regulatory filings (DRHP Note 100 and both AR26/
   Q3FY26 Reg.52(4) tables) state "Current Ratio: Not Applicable" for an NBFC — and excluded from
   Block D's denominator rather than scored against an operating-company band.
4. Deal-breaker #6 (ND/EBITDA>3x AND IC<3x → AVOID) duplicates D1's leverage test, which the
   framework already redirects to CRAR for financials. Applying it literally (ND/EBITDA≈6.3x,
   IC≈1.48x, both FY26) would force an AVOID purely from a formula mismatch against a company
   whose CRAR (26.12%) is comfortably above regulatory minimums. **Not applied** — flagged for
   verifier review rather than silently triggering AVOID.
5. Working-capital/receivable-day tests (B4, M4/M10's receivable-day leg, M12) are marked
   IRRELEVANT for a lender per CLAUDE.md; where a test has a secondary leg that still computes
   (e.g., M4's "zero revenue-decline years"), that leg is scored and the WC leg is noted as
   adapted/satisfied-by-substitute rather than blocked.

---

## [BLOCK A: RETURN ON CAPITAL] — adapted for NBFC, see note 2 above

EBIT = PBT + Finance Costs. Capital Employed = Total Assets − Liabilities due within 12 months
(DRHP Note 34, printed p.345, for FY23-25; IP p.13 ALM table "Cumulative Liabilities, upto 1
year" for FY26).

| FY | PBT (₹cr) | Finance Cost (₹cr) | EBIT (₹cr) | Total Assets (₹cr) | Curr. Liab (₹cr) | Cap. Employed | ROCE |
|----|---|---|---|---|---|---|---|
| FY23 | 22.019 (DRHP p.76) | 62.857 (DRHP p.76) | 84.876 | 778.708 (DRHP p.75) | 263.279 (DRHP p.345, Note 34) | 515.429 | **16.46%** |
| FY24 | 29.636 (DRHP p.76) | 83.420 (DRHP p.76) | 113.056 | 984.846 (DRHP p.75) | 257.831 (DRHP p.345) | 727.015 | **15.55%** |
| FY25 | 47.355 (DRHP p.76) | 114.627 (DRHP p.76) | 161.982 | 1,412.521 (DRHP p.75) | 423.207 (DRHP p.345) | 989.314 | **16.37%** |
| FY26 | 66.047 (AR26 CF stmt; matches IP p.15 PBT 66.05) | 137.340 (AR26/IP p.15) | 203.387 | 1,817.78 (AR26 BS/IP p.16) | 561.10 (IP p.13, ALM "upto 1 year" cumulative liabilities) | 1,256.68 | **16.19%** |

Cross-check: FY26 EBIT/Finance Cost = 203.387/137.340 = 1.48x, exactly matching IP p.10's own
"Interest Coverage Ratio" of 1.48 for FY26 — confirms the EBIT construction is internally
consistent with the company's own methodology.

- **A1 Median ROCE** = median(15.55, 16.37, 16.46, 16.19) = **16.28%** → band 15-19.9% = **3**
- **A2 Minimum single-year ROCE** = 15.55% (FY24) → band ≥15% = **5**
- **A4 ROCE trend (latest FY26 16.19% vs earliest FY23 16.46%)** = decline of 0.27pp. No band
  covers <1pp; scored under the smallest specified decline band (1-3pp) = **3** (flagged: this
  is a rounding-level move, not a real deterioration).

**A3 Median ROE** (PAT ÷ average Net Worth, opening+closing/2; PAT = Total Comprehensive Income
per DRHP's own Return-Ratio convention, DRHP p.281 "PAT to Average Net Worth"; FY22 opening net
worth ₹110.751cr from DRHP Note 104, p.382 restated-opening-balance reconciliation):

| FY | PAT incl-OCI (₹cr) | Avg Net Worth (₹cr) | ROE |
|----|---|---|---|
| FY23 | 16.028 (DRHP p.76, Total Comprehensive Income) | (110.751+152.546)/2=131.649 | 12.18% |
| FY24 | 22.620 (DRHP p.76) | (152.546+201.731)/2=177.139 | 12.77% |
| FY25 | 35.910 (DRHP p.76) | (201.731+257.894)/2=229.813 | 15.63% (DRHP's own calc: 15.66%, p.281 — matches) |
| FY26 | 49.676 (AR26 Reg.52(4) table: PAT incl OCI 4,967.58 lakh; IP p.5/9: 13.73% ROE, exact match) | (257.894+465.47)/2=361.682 | 13.73% |

- **A3 Median ROE** = median(12.18,12.77,13.73,15.63) = **13.25%** → band 12-14.9% = **2**

**Block A = A1(3) + A2(5) + A3(2) + A4(3) = 13/20**

---

## [BLOCK B: CASH GENERATION QUALITY] — structurally near-zero for a scaling NBFC, see note 1

CFO and Capex (₹cr; DRHP Restated Statement of Cash Flows p.77 for FY23-25; AR26 Statement of
Cashflows for FY26, cross-checked against DRHP's FY25 comparator column which reconciles
exactly after unit conversion — DRHP FY25 CFO −311.264cr = AR26 FY25 comparator −31,126.42 lakh):

| FY | CFO (₹cr) | Capex (₹cr) | FCF (₹cr) | PAT incl-OCI (₹cr) | CFO÷PAT |
|----|---|---|---|---|---|
| FY23 | −169.414 (DRHP p.77) | −5.133 (DRHP p.77, "Purchase/Sales of PPE and intangibles") | −174.547 | 16.028 | −10.57x |
| FY24 | −223.752 (DRHP p.77) | −2.434 (DRHP p.77) | −226.186 | 22.620 | −9.89x |
| FY25 | −311.264 (DRHP p.77) | −3.658 (DRHP p.77) | −314.922 | 35.910 | −8.67x |
| FY26 | −279.992 (AR26 CF stmt) | −6.495 (AR26 CF stmt) | −286.487 | 49.676 | −5.63x |

Cumulative CFO = −984.42cr; Cumulative PAT = 124.23cr; Cumulative FCF = −1,002.14cr.

- **B1 Cumulative CFO ÷ Cumulative PAT** = −984.42/124.23 = **−7.93x** → band <0.50 = **0**
- **B2 FCF-positive years** = 0/4 = 0% → band <50% = **0**
- **B3 Cumulative FCF ÷ Cumulative PAT** = −1,002.14/124.23 = **−8.07x** → band <0.20/negative = **0**
- **B4 (WC days)** — IRRELEVANT for a lender (no conventional receivable/inventory/payable cycle;
  the balance-sheet "Receivables" line is trivial, <₹0.4cr in every year, DRHP p.75). Excluded.

**Block B = B1(0) + B2(0) + B3(0) = 0/15** (B4 excluded from denominator)

**block_b_trend: IMPROVING** — the CFO/PAT ratio, while deeply negative every year, has narrowed
from −10.57x (FY23) to −5.63x (FY26) as PAT scales faster than the operating cash absorbed by
loan-book growth. This is the single most important flag in this scorecard: a mechanically
zero Block B score driven entirely by a lender's balance-sheet mechanics (loans classified as
operating assets), not by earnings-quality or distress. Financing activities were strongly
positive every year (₹212.7cr, ₹177.5cr, ₹389.8cr, ₹354.3cr — DRHP p.77 / AR26 CF stmt) funding
exactly this loan growth, which is the expected, healthy pattern for a scaling secured lender.

---

## [BLOCK C: GROWTH]

Total Income / Revenue (₹cr; DRHP Restated P&L p.76 for FY23-25; AR26/IP p.15 for FY26,
cross-checked: AR26 Total Income FY26 = 31,959.01 lakh = ₹319.59cr = Interest Earned
₹299.12cr + Fees/FV gains + Other Income, IP p.15 Interest Earned 299.12 + NII build 161.78
reconciles):

| FY | Total Income (₹cr) | YoY | PAT incl-OCI (₹cr) | YoY |
|----|---|---|---|---|
| FY23 | 130.668 (DRHP p.76) | — | 16.028 (DRHP p.76) | — |
| FY24 | 175.018 (DRHP p.76) | +33.9% | 22.620 (DRHP p.76) | +41.1% |
| FY25 | 248.038 (DRHP p.76) | +41.7% | 35.910 (DRHP p.76) | +58.7% |
| FY26 | 319.590 (AR26; IP p.15) | +28.9% | 49.676 (AR26 Reg.52(4); IP p.5/6: 49.68) | +38.3% |

- **C1 Revenue CAGR (FY23→FY26, 3yr)** = (319.590/130.668)^(1/3)−1 = **34.75%** → band ≥20% = **5**
- **C2 PAT CAGR (FY23→FY26, 3yr)** = (49.676/16.028)^(1/3)−1 = **45.81%** → band ≥20% = **5**
- **C3 Positive YoY revenue years** = 3/3 = 100% → **5**
- **C4 PAT CAGR − Revenue CAGR** = 45.81−34.75 = **+11.06pp** → band ≥+3pp = **5**

**Block C = 20/20** — Strongest block. AUM (₹686.8cr→961.4cr→1,277.0cr→1,626.3cr, IP p.7),
customer base (16,851→42,809, IP p.7) and branch network (119→176, IP p.7) all corroborate the
income-statement growth; no PEER DATA NEEDED gaps in this block.

---

## [BLOCK D: BALANCE SHEET STRENGTH] — NBFC overrides applied (D1=CRAR, D2=PCR, D3=default,
D4=irrelevant)

| FY | CRAR (D1) | PCR, Gross NPA basis (D2) |
|----|---|---|
| FY23 | 23.09% (DRHP p.284/391) | 45.60% (DRHP p.281/283) |
| FY24 | 21.81% (DRHP p.284/391) | 54.41% (DRHP p.281/283) |
| FY25 | 20.80% (DRHP p.284/391) | 55.18% (DRHP p.281/283) |
| FY26 | 26.12% (AR26 Reg.52(4) table; IP p.5/10 — matches) | 49.43% (IP p.5/11, "PCR" — cross-checked against operator-context, consistent) |

- **D1 CRAR (latest, FY26)** = 26.12% → band ≥18% = **5**
- **D2 PCR (latest, FY26)** = 49.43% → band <60% = **0**. Flagged: PCR sits below 60% in *all
  four* years (45.6/54.4/55.2/49.4%), which for this book looks low mainly because GNPA is small
  and >90% secured (real-estate/vehicle collateral) — high collateral coverage substitutes for
  heavy provisioning. This is a legitimate framework-vs-business-model tension, not necessarily
  an under-provisioning signal, but it is scored 0 as written.
- **D3 Debt/Equity** — "Financials: default 3" per framework = **3**. (For reference, actual
  D/E: FY23 4.04x, FY24 3.81x, FY25 4.41x, FY26 2.87-2.89x — DRHP p.284/391, AR26 Reg.52(4),
  IP p.10 — leverage fell sharply post-IPO equity infusion, a normal and positive capital-
  structure development for a lender, not scored here since D3 uses the fixed default.)
- **D4 Current Ratio** — **IRRELEVANT**, excluded. DRHP Note 100 (p.381) and both AR26/Q3FY26
  Reg.52(4) tables state "Current Ratio: Not Applicable" for this NBFC in the company's own
  regulatory disclosures.

**Block D = D1(5) + D2(0) + D3(3) = 8/15** (D4 excluded from denominator)

---

## [BLOCK E: SHAREHOLDER ALIGNMENT]

- **E1 Promoter holding (latest)**: Anchored figure = **70.22%** post-Offer (DRHP p.99, "Total
  (A+B+C+D+E+F+G)" build-up table, % of post-Offer equity share capital — this is the DRHP's own
  computed post-listing promoter position, "subject to finalisation of Basis of Allotment").
  Cross-check (NON-ANCHORED, operator-context.md, screener screenshot): 60.45% (Sep-25) →
  60.45% (Dec-25) → 60.31% (Mar-26) → 60.17% (Jun-26). Both the anchored figure and the
  non-anchored latest-quarter figure fall in the same scoring band. **≥60% = 5**. Flagged: the
  ~10pp gap between the DRHP's own post-Offer computation (70.22%, Aug-25) and the first
  post-listing screener print (60.45%, Sep-25) is unexplained by anchored evidence — no
  post-listing SHP filing is in inputs/ to reconcile it (input_gaps: shareholding absent).
- **E2 Promoter holding change (3yr proxy)**: closest anchored comparators are DRHP p.93 "2
  years prior to Prospectus" = 99.41% vs post-Offer 70.22% (DRHP p.93/99) — a **29.2pp decline**.
  Context: this decline is driven by (a) dilutive private-placement/rights-issue capital raises
  in FY22-24 as the company funded loan-book growth (DRHP p.94-99 build-up table) and (b) the
  planned IPO Offer-for-Sale (disclosed, not open-market selling). Scored per the literal rule:
  decrease >3% → **0**.
- **E3 Promoter pledge**: DRHP p.100, explicit: "none of the Equity Shares held by our Promoters
  are pledged" as of Prospectus date. No later anchored confirmation exists (operator-context.md
  notes "no promoter pledge figure supplied," non-anchored). **0% = 5**.
- **E4 Contingent liabilities ÷ Net Worth**: DRHP Note 46 (p.349, Ind AS 37 disclosure) —
  Contingent Liabilities (claims not acknowledged as debt) FY23 = nil, FY24 = nil, FY25 = ₹0.009cr
  (income-tax demand). Net worth FY25 = ₹257.894cr (DRHP p.75). Ratio = 0.09/2,578.94 ≈ **0.003%**
  → band <5% = **5**. FY26 contingent-liability note **NOT FOUND** (not disclosed in the
  abridged quarterly-format Reg.33/52 filing; full annual-report Ind AS 37 note not yet
  available) — FY25 used as latest anchored figure, FY26 gap flagged. Note: "Capital and other
  Commitments — partially disbursed loans" (₹24.45cr FY25, DRHP Note 46) is excluded from this
  ratio as it is an ordinary lending-business commitment, not a contingent liability in the
  guarantee/claim sense the metric targets.

**Block E = E1(5) + E2(0) + E3(5) + E4(5) = 15/20**

---

## [BLOCK F: QUANTITATIVE MOAT SCORING] — Max 60 nominal; M3 and M12 excluded as IRRELEVANT
for a lender (adjusted max 50 across 10 scorable tests)

| # | Test | Score | Basis / anchor |
|---|---|---|---|
| M1 | Pricing Power | **3** | EBITDA margin (DRHP p.385 "EBITDA to Total Income": FY23 65.78%, FY24 65.47%, FY25 66.07%; FY26 computed 205.68/319.59=64.36%) moved −1.42pp over the window — within ±2pp — while revenue CAGR 34.75%≥10% → "margin stable ±2pp AND rev CAGR≥10%" = 3. Flagged: EBITDA-margin is a poor fit for a lender (Finance Cost, the dominant expense, is added back); NIM — the natural pricing-power metric — actually *expanded* every year (DRHP p.282: 9.27%→9.23%→9.73%; IP p.8 alt-basis 10.25%→10.14%→10.47%→11.26%), arguing for a stronger true signal than this adapted test captures. |
| M2 | Cost Advantage vs peer median | **0** | PEER DATA NEEDED — no peer EBITDA-margin data in this stage's source set. |
| M3 | Capital Efficiency (FAT) | **EXCLUDED** | Fixed-asset turnover is not a meaningful concept for a lender (loan book, not PP&E, is the earning asset). Not scored, not counted in denominator. |
| M4 | Customer Stickiness | **5** | Zero revenue-decline years (Block C). Receivable-days leg N/A for a lender (trivial non-loan receivables line, DRHP p.75); substituted with GNPA/asset-quality stability (largely stable/improving ex the FY26 Up Money DA event) as the adapted second leg — satisfied. |
| M5 | Scale & Dominance | **0** | PEER DATA NEEDED — no mcap/margin peer ranking available. |
| M6 | Technology/R&D | **0** | R&D/Revenue not separately disclosed (tech spend embedded in operating expense; digital LOS/LMS/Synofin/CRM stack described qualitatively in IP pp.19, but unquantified against this test's specific metric). |
| M7 | Regulatory/License | **1** | NBFC lending is RBI-regulated (RBI Reg. No. B-10.00318, DRHP p.78), but the listed NBFC-MSME/vehicle-finance segment has well over 10 listed peers → "regulated but >10 players = 1". |
| M8 | Distribution | **5** | Reach quantified and growing (119→135→158→176 branches, DRHP p.284/IP p.7); AUM/branch growing every year (₹57.71mn→71.21mn→80.82mn, DRHP p.284; continuing to ~₹92.4mn FY26 per IP p.7 AUM÷branch); revenue CAGR 34.75%≥15% → all criteria met. |
| M9 | Brand | **0** | PEER DATA NEEDED — no peer gross-margin/spread comparison available; GM proxy not meaningful for a lender without peer NIM data. |
| M10 | Switching Costs | **5** | Revenue grew every year; adapted receivable-days leg (as M4) trivially stable. |
| M11 | Network Effects | **3** (conservative — only 4yrs, framework wants ≥6yrs for the two-window test) | Revenue CAGR 34.75%≥20%; "selling"-proxy expense (Business/Sales Promotion+Commission, DRHP Note 32 p.341) ≈0.21%→0.37%→0.33% of revenue — roughly stable → "rev CAGR≥20% AND selling% stable/declining=3", scored conservatively per the <6yr rule and stated. |
| M12 | Negative WC/Float | **EXCLUDED** | Non-deposit-taking NBFC; no conventional operating WC cycle or float concept. Not scored, not counted in denominator. |

**Moat tests scored ≥3 ("present"): M1, M4, M8, M10, M11 = 5 tests present.**
Sum of 10 scorable tests = 3+0+5+0+1+5+0+5+3 = **22** (M2/M5/M9 = 0 purely from PEER DATA
NEEDED, not weak-moat evidence — flagged for stage 6/7 peer work to revisit).

**Moat classification: 5 present → STRONG** (band: 6+=FORTRESS, 4-5=STRONG, 2-3=MODERATE,
1=THIN, 0=NONE).

---

## DASHBOARD SUMMARY

```
BLOCK A  Return on Capital          13/20   ███████░░░░░░░░░░░░░  (ROCE adapted; ROE weak)
BLOCK B  Cash Generation Quality     0/15   ░░░░░░░░░░░░░░░░░░░░  (structural NBFC zero — see note 1)
BLOCK C  Growth                     20/20   ████████████████████  STRONGEST BLOCK
BLOCK D  Balance Sheet Strength      8/15   ██████████░░░░░░░░░░  (CRAR strong; PCR low; D4 n/a)
BLOCK E  Shareholder Alignment      15/20   ███████████████░░░░░  (holding decline is IPO-related)
---------------------------------------------------------------------
CORE SCORE (A+B+C+D+E, raw /100)   56/100

MOAT PROFILE (12 tests, M3/M12 excluded, /50 adjusted, /60 nominal)
Present (≥3): M1 M4 M8 M10 M11  |  Absent/PEER-DATA-NEEDED: M2 M5 M6 M7 M9
Moat score (raw sum, 10 scorable tests): 22   Moat class: STRONG (5 present)

GRAND TOTAL (core + moat, raw): 56 + 22 = 78
```

## DATA CONFIDENCE
4 years of disclosed financials (FY23-FY26) — this is the *maximum* history obtainable: the
company IPO'd 2025-07-31, and DRHP restatement rules only mandate 3 years back (FY23-25); FY26
is the first post-listing full year. Per framework: **"3-4 years = LIMITED, downgrade
classification one tier."** This applies mechanically here even though 4 years is genuinely all
the audited history that exists for a company at this stage of its listed life — flagged
explicitly so downstream stages do not read the downgrade as a judgment on data quality.

## DEAL-BREAKER OVERRIDES
| # | Test | Triggered? | Effect |
|---|---|---|---|
| 1 | Block A <8 | No (13) | — |
| 2 | Block B <8 | **Yes (0)** | Caps classification at max GOOD (non-binding; base classification is already below GOOD) |
| 3 | Median ROCE <10% | No (16.28%) | — |
| 4 | Cumulative CFO/PAT <0.50 | **Yes (−7.93x)** | Caps classification at max AVERAGE. Driven by **all four years FY23-FY26** — this is the lender's structural loan-growth cash-flow pattern (note 1 above), not a specific bad year or a legacy-cleanup event. Downstream position sizing should weigh this as a formula-fit issue, not a quality signal. |
| 5 | Pledge >15% | No (0%) | — |
| 6 | ND/EBITDA>3x AND IC<3x → AVOID | **Not applied** — see NBFC-adaptation note 4. Literal calc (ND/EBITDA≈6.3x, IC≈1.48x) would trigger AVOID but duplicates D1's leverage test already redirected to CRAR (26.12%, well-capitalized) for financials. Flagged for verifier review rather than mechanically applied. | |
| 7 | Revenue declined majority of years | No (0/3 declines) | — |
| 8 | PAT negative in any of last 3 years | No (positive & growing every year) | — |
| 9 | History <3 years | No (4 years) | — (but see Data Confidence downgrade above) |

## CLASSIFICATION

Classification matrix: Core 56 falls in the **40-59 band → AVERAGE**, regardless of the STRONG
moat class (matrix requires Core≥60 for moat class to lift the tier).

Deal-breakers #2 and #4 both cap at or below AVERAGE — consistent with the base matrix result,
non-binding.

**Data-confidence downgrade (4yr history = LIMITED) then applies one further tier: AVERAGE →
AVOID.**

**Final Gate 0 classification: AVOID.**

### Why this AVOID should NOT be read as "the company is bad" — read this before acting on it
Per CLAUDE.md: flags propagate, they do not halt a run, and company quality never triggers a
STOP. This AVOID is the mechanical output of two specific, identified drivers:
1. Block B scoring zero *by construction* for any scaling secured NBFC (loan disbursements are
   classified as operating cash outflow under Ind AS) — not evidence of cash-quality problems.
   CFO/PAT is actually *improving* (−10.57x → −5.63x over 4 years) as the book scales.
2. A one-tier mechanical downgrade for having "only" 4 years of history, which is the maximum
   possible for a company that IPO'd 13 months ago.

Set against this: Block C (growth) is a perfect 20/20, AUM/PAT/NII have compounded at
33-46% over FY23-26, CRAR is strong and improved post-IPO (26.12%), leverage fell sharply
post-equity-raise (D/E 4.4x→2.9x), asset quality (ex the identified, quantified, one-off Up
Money DA pool) is clean (GNPA 0.80% / NNPA 0.53% FY26 excluding that pool vs 2.13%/1.08%
including it), and promoter alignment metrics (pledge 0%, holding still ≥60% by every measure)
are sound. The Block A adaptation (ROCE) and Block D PCR-below-60% result are both genuine,
if modest, watch items independent of the NBFC-formula issues.

**Strongest block: C (Growth), 20/20.**
**Weakest block: B (Cash Generation Quality), 0/15 — flagged as a framework-fit issue, not a
company-quality issue; downstream stages should weight NIM/ROA/AUM-growth trends over the raw
Block B score for this name.**

## DECISION LINE
Gate 0 mechanical classification = **AVOID**, driven by (i) a Block B cash-flow test that is
structurally incompatible with lender balance-sheet mechanics and (ii) a mechanical
short-history downgrade for a 13-month-old listing. Underlying fundamentals (growth, asset
quality ex-one-off, capitalisation, leverage trend) do not support treating this as a
fundamentally weak business at Gate 0; this flag should propagate to downstream stages
(especially stage 11 valuation and stage 13 synthesis) as a named, explained mechanical
artifact rather than a verdict on the company. No STOP is issued — none of PROCEED / PROCEED
WITH CAVEATS / PROCEED WITH FLAGS / REWORK / INSUFFICIENT EVIDENCE is determined at this stage;
that determination belongs to stage 13.

---

```yaml
stage: B01-gate0
company: "LAXMIINDIA"
run_date: "2026-07-22"
model: claude-sonnet-5
status: complete
input_gaps:
  - type: announcements
    severity: MEDIUM
    note: "inputs/announcements/ empty; operator-context.md non-anchored summary used as lead only, not scored."
  - type: shareholding
    severity: MEDIUM
    note: "inputs/shareholding/ empty; no post-listing SHP filing available. E1/E2 anchored to DRHP's own post-Offer computation (70.22%, Aug-25) and DRHP historical build-up tables; operator screener figures (60.17-60.45%, Sep25-Jun26) used as non-anchored cross-check only, landing in the same E1 scoring band."
  - type: research
    severity: LOW
    note: "inputs/research/ empty. No effect on anchored evidence."
  - type: laxmiindia_screening
    severity: LOW
    note: "No LAXMIINDIA screening CSV existed; this stage extracted all financials directly from drhp.pdf, Annual_Report_2024.pdf (FY26 audited results), the Q3 FY26 unaudited filing, and Investor_Presentation_1.pdf."
flags:
  - type: FLAG-GATE0
    reason: "Classification AVOID driven mechanically by (1) Block B scoring 0/15 because loan-book growth is classified as operating cash outflow under Ind AS for any scaling NBFC (CFO/PAT actually improving -10.57x to -5.63x FY23-FY26, not deteriorating), and (2) a mechanical one-tier downgrade for 4-year history, the maximum available for a company that IPO'd 2025-07-31. Growth (Block C 20/20), capitalisation (CRAR 26.12% FY26), leverage trend (D/E 4.4x to 2.9x post-IPO), and asset quality ex the identified one-off Up Money DA pool (GNPA 0.80%/NNPA 0.53% FY26 ex-pool) do not support a fundamentally weak read. Downstream stages should weight NIM/ROA/AUM growth over raw Block B/history-tier mechanics for this name."
  - type: FLAG-CASH
    reason: "Block B = 0/15, cumulative CFO/PAT = -7.93x, all four years FY23-FY26. Structural NBFC pattern (financing activities fund loan-book growth every year: +Rs212.7cr/177.5cr/389.8cr/354.3cr FY23-FY26), not a cash-quality red flag; see block_b_trend."
  - type: FLAG-DATA-GAP
    reason: "D2 (PCR) uses FY26=49.43%, below the 60% band in all 4 years (45.6/54.4/55.2/49.4%); likely reflects high secured-collateral coverage rather than under-provisioning but not confirmable without peer PCR data (PEER DATA NEEDED, same gap affects M2/M5/M9 moat tests)."
  - type: FLAG-SHAREHOLDING-GAP
    reason: "~10pp unexplained gap between DRHP's own post-Offer promoter computation (70.22%, Aug-25, anchored) and first post-listing operator/screener figure (60.45%, Sep-25, non-anchored). No SHP filing in inputs/ to reconcile. Does not change E1 scoring band (both >=60%) but flagged for stage 8/finalize."
data_years: 4
fy_range: "FY23 to FY26"
blocks: {A: 13, B: 0, C: 20, D: 8, E: 15}
core_score: 56
moat_score: 22
grand_total: 78
moats_confirmed: 5
moat_class: "STRONG"
classification: "AVOID"
deal_breakers:
  - "Block B <8 (actual 0) -> max GOOD (non-binding, base classification already below GOOD)"
  - "Cumulative CFO/PAT <0.50 (actual -7.93x) -> max AVERAGE, driven by all 4 years FY23-FY26, structural NBFC loan-growth cash-flow classification, not a specific bad year or distress signal"
  - "ND/EBITDA>3x AND IC<3x -> AVOID: NOT APPLIED, duplicates D1 leverage test already redirected to CRAR (26.12%) for financials per framework; literal calc would show ND/EBITDA~6.3x and IC~1.48x FY26 but this is a formula-fit mismatch, flagged for verifier review not mechanically triggered"
history_downgrade: true
data_notes:
  - "PAT series uses Total Comprehensive Income (incl. OCI) per DRHP's own Return-on-Net-Worth convention (DRHP p.281) and matching the investor presentation/Reg.52(4) figures; pre-OCI 'Profit for the year' alternate series (FY23 15.971cr, FY24 22.468cr, FY25 36.005cr, FY26 49.757cr) produces materially identical CAGR/band outcomes."
  - "Investor presentation FY23/FY24 PAT bars (15.46cr/22.47cr) use AS-PREVIOUSLY-REPORTED (pre-restatement) figures, not DRHP's restated figures (16.03cr/22.62cr) -- traced to DRHP Note 104's restatement reconciliation table (p.382); DRHP-restated figures used as the authoritative series since restatement corrected identified accounting errors."
  - "ROCE (Block A) is an adapted metric for this NBFC: capital employed = Total Assets - liabilities-due-within-12-months (DRHP Note 34 maturity analysis for FY23-25; investor-presentation ALM table for FY26, a different disclosure basis) -- flagged as an adaptation, not a DRHP-stated ratio, cross-checked via EBIT/Finance-Cost reproducing the company's own Interest Coverage Ratio (1.48x FY26, IP p.10) exactly."
  - "D4 (Current Ratio) and B4/M3/M12 (working-capital/inventory/fixed-asset-turnover-based tests) marked IRRELEVANT for a lender per CLAUDE.md NBFC treatment and excluded from their blocks' denominators rather than scored against operating-company norms; company's own filings independently confirm 'Current Ratio: Not Applicable' (DRHP p.381; AR26 and Q3FY26 Reg.52(4) tables)."
  - "M2, M5, M9 scored 0 as PEER DATA NEEDED (peer mcap/EBITDA-margin/gross-margin data not in this stage's source set) -- flagged as a data gap for stage 6 (peers) and stage 7 (emerging moat), not evidence of moat absence."
  - "FY26 contingent-liabilities note (Ind AS 37) NOT FOUND -- not disclosed in the abridged SEBI Reg.33/52 quarterly-format filing; E4 uses FY25 (latest anchored: 0.09cr/257.89cr = 0.003%) with the FY26 gap flagged."
  - "Q3 FY26 unaudited filing (41b31cc6-...pdf) read and cross-checked (9M PAT incl-OCI Rs29.10cr, GNPA 2.40%, NNPA 1.24%, CRAR 28.40%, D/E 2.69x, all matching operator-context.md's non-anchored summary) -- used only as an interim-trend cross-check; FY26 audited full-year (AR26) is the primary anchor for all FY26 scored figures."
  - "Up Money Ltd DA pool (~Rs19cr, Jalandhar NBFC counterparty default) is the single identified driver of the FY26 GNPA/NNPA/PCR deterioration (2.13%/1.08%/49.43% including it vs 0.80%/0.53% excluding it); provisioned ~60% per rating action (operator-context.md, non-anchored cross-check only) and under legal recovery action per management commentary reviewed in concalls (out of scope for this stage)."
block_b_trend: "improving -- CFO/PAT ratio narrowed from -10.57x (FY23) to -5.63x (FY26) as PAT compounded faster than the operating cash absorbed by loan-book growth; still deeply negative every year (structural NBFC pattern, financing activities fund the growth: +Rs212.7cr/177.5cr/389.8cr/354.3cr FY23-FY26), not a deteriorating cash-quality signal."
```
