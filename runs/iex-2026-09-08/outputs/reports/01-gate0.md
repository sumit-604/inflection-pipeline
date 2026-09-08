# STAGE 1 — GATE 0 QUANTITATIVE SCORECARD
## Indian Energy Exchange Ltd (IEX) — RUN 2 — run 2026-09-08

This is a full re-run, not a patch. Run 1's two source gaps are now closed:
the annual report (previously unreadable as a PDF) is supplied as
page-marked plain text, and peer screener files (MCX, BSE, CDSL) are now
supplied. Every block below is scored fresh from source.

Data available: 8 years (FY19 to FY26) for P&L, balance sheet and cash flow
(screener-Data_Sheet.csv — the only populated screener CSV; the other four
screener CSVs in inputs/screening/ hold row labels only, a recorded
collector defect, not a missing-data gap). A 10-quarter series runs
Q4FY24-Q1FY27. Three full balance-sheet years (FY24, FY25, FY26) are now
cross-verified against the audited annual reports (Annual_Report_2026.txt
carries FY26 primary/FY25 comparative; Annual_Report_2025.txt carries FY25
primary/FY24 comparative), which extends the ROCE/FCF/WC-days sub-window
from 2 years (run 1) to 3 years this run. Scoring adapted to 8-year history
for P&L/CF growth and cash-conversion metrics; ROCE, FCF and WC-days trend
metrics are constrained to the FY24-FY26 window where the underlying
current/non-current liability split and a separated capex line are only
available for those three years — flagged at each metric below. Peer data
(MCX, BSE, CDSL Data_Sheet.csv) is used for M2, M5, M9.

Currency: all figures Rs crore unless stated. Source PDFs (and their
extracted text) are in lakhs; converted 1 lakh = Rs0.01cr throughout.

---

## LOAD-BEARING FACTS — RE-VERIFIED AGAINST THE ANNUAL REPORT AND RESULTS

### 1. Market coupling exposure — DAM vs RTM/TAM/green/certificates

**Revenue-basis split.** Correction to run 1's finding: a revenue-basis
split DOES exist, but only two-way. AR Note 28 "Revenue from operations"
disaggregates transaction-fee revenue into "Electricity (comprising RTM,
DAM, TAM, Green Segments)" = Rs558.51cr and "Certificates (comprising REC,
Escerts Segments)" = Rs25.45cr for FY26, vs Rs478.34cr and Rs35.21cr FY25
(AR p.211, Note 28). **No further revenue-basis breakdown within the
Electricity bundle (DAM vs RTM vs TAM vs Green) exists anywhere in this
corpus** — the four electricity products are reported as one revenue
number. Ind AS 108 still reports ONE operating segment overall
(FY26_Q4_Audited_Results p.9; Q1FY27_Results p.5/p.10).

**Volume-basis split — now a THREE-WAY inconsistency, not two-way.** Run 1
found the Apr-2026 call said RTM = 39% of FY26 volume and the Jul-2026
Analyst Meet said RTM = 34%. The annual report itself, read in full, adds a
third data point and does not simply side with one call:

- AR p.17 (narrative box): "the RTM segment has recorded a five-year CAGR
  of 42% and in FY'26 accounted for **34%** of the total electricity traded
  volume on IEX."
- AR p.25 (FY26 Product Mix infographic): **DAM 39% | RTM 34% | Certificates
  12% | TAM 6% | Green Market 7% | DAC 2%.** These six figures sum to
  exactly 100%, an internal consistency check the chart passes.
- AR p.62 (Risk Management, market coupling mitigation): "The Day-Ahead
  Market (DAM) contributed **39%** of IEX's total traded volumes in FY'26,
  compared with 44% in FY'25." Consistent with the p.25 chart's DAM=39%.
- AR p.33 (Business Performance narrative): "RTM volumes grew 41%
  year-on-year to 55 billion units, now accounting for **nearly 40%** of
  total electricity volumes on IEX."
- AR p.36-37 (MD&A): "DAM accounted for approximately **44%** of total
  electricity volumes on IEX" for FY26, immediately followed by "[RTM]...
  accounting for approximately **39%** of total electricity volumes traded
  on IEX" for FY26.

**These last two passages (p.33 and p.36-37) contradict the chart (p.25)
and the risk section (p.62) within the SAME annual report.** The p.25
chart and p.62 risk section agree with each other and sum to a clean 100%;
the p.33/p.36-37 narrative passages do not reconcile with them or with each
other (p.33 says RTM~40%, p.36-37 says RTM~39% paired with DAM~44%, which
itself contradicts p.62's DAM=39%/44%-prior-year framing). **Read as a
whole, the numerically self-consistent figures (p.25 chart summing to
100%, corroborated by p.62) support DAM = 39%, RTM = 34% for FY26 — this
matches the Jul-2026 Analyst Meet's RTM figure, not the Apr-2026 call's.**
The Apr-2026 call's "39% RTM" claim and the AR's own p.33/p.36-37 passages
share the same apparent error: reporting DAM's 39% share as RTM's. This
is flagged, not silently resolved by this stage — a downstream verifier
should treat DAM=39%/RTM=34% as the better-evidenced figure but note the
AR itself has NOT internally reconciled this.

Market coupling scope (AR p.61-62, cross-checked against
Concall_Jul_2026_Transcript p.18-19): CERC's July-2025 order targets DAM
only. IEX challenged before APTEL (28-Aug-2025); APTEL held 13-Feb-2026
that IEX was not an aggrieved party until final regulations issue; IEX
appealed to the Supreme Court 10-Apr-2026, hearing scheduled 3-Aug-2026
(AR p.62). CERC issued Draft Market Coupling Regulations 17-Apr-2026,
final regulations not yet issued as of the AR's date. RTM coupling remains
explicitly deferred per management (Concall_Jul_2026_Transcript p.18-19).

### 2. Operating vs treasury earnings

Re-verified against the full annual report, not just the abbreviated
results filings. Consolidated P&L (AR p.237/241, Note 27-28):

| FY26 consolidated (Rs cr) | Amount | % of PBT |
|---|---|---|
| Revenue from operations | 615.6470 | — |
| Total expenses (opex+D&A+finance cost) | 121.1838 | — |
| **Operating EBIT (Rev − Expenses)** | **494.4632** | **76.60%** |
| Other income (pure/treasury), Note 29 (AR p.230, standalone basis; consol other income AR p.241) | 131.3047 | 20.34% |
| Share of profit of associate (IGX, equity method) | 19.7953 | 3.07% |
| **Profit before tax** | **645.5632** | **100%** |

Matches Data_Sheet's composite "Other Income" = 131.3047 + 19.7953 =
**151.10cr** to the cent (AR p.241, Note 27/28).

Q1FY27 consolidated (Q1FY27_Results_Unaudited p.9, re-verified this run):
Revenue 157.8767cr, total expenses 33.7268cr, **operating EBIT 124.1499cr
(70.22% of PBT)**; other income (pure) 44.9327cr (25.41% of PBT); IGX
associate share 7.7188cr (4.37% of PBT); PBT 176.8014cr. Combined
non-operating share of PBT = 52.6515/176.8014 = **29.78%** (task states
29.75%; the 0.03pp gap is rounding on the inputs, not a data conflict).

**Trend: non-operating share of PBT rose from 23.41% (FY26 full year) to
29.78% (Q1FY27), +6.37pp in one quarter.** Kept separate from operating
earnings in every metric below per the run's instruction.

### 3. Guidance against delivery — Q4FY26 call (24-Apr-2026) vs Q1FY27 print (23-Jul-2026)

Unchanged from run 1 (same source documents, re-confirmed): FY27 volume
growth guided "15-20% every year" (Concall_Apr_2026 p.13); Q1FY27 delivered
+15.9% YoY (Q1FY27_Press_Release p.1) — low end of the range. Revenue growth
decelerating (FY26 +13.6% to Q1FY27 +10.1% YoY). PAT growth decelerating
(FY26 +14.9% to Q1FY27 +11.7% YoY). REC volumes down sharply YoY/QoQ per an
analyst's own figure at the Jul call, thinly addressed by management. IGX
IPO process delivered ahead of the vague April framing (DRHP filed
14-Jul-2026). Coal Exchange delivered faster than typical regulatory pace
(Rules notified 4-Jun-2026, Indian Coal Exchange Ltd incorporated
1-Jun-2026). Full detail in run 1's table, re-confirmed against the same
source pages this run.

### 4. IGX carrying value, shareholding, accounting treatment, OFS

- **IGX is EQUITY-ACCOUNTED as an associate**, not consolidated (AR p.241,
  "Share in profit of associate (net of tax)"; AR p.4577-4583, Board's
  Report, "As on March 31, 2026, IGX stands as the associate of IEX").
- **Carrying value Rs90.25cr as at 31-Mar-2026** (9,025.09 lakh, AR p.16 of
  consolidated balance sheet section, "Investments accounted for using the
  equity method"), up from **Rs75.75cr as at 31-Mar-2025** (7,574.70 lakh,
  same line, comparative column) — re-verified against the full AR, exact
  match to run 1's figures sourced from the abbreviated results filing.
- IEX holds **47.28%** of IGX (AR p.34, p.4583; consistent with the
  concalls' "47.3%"). PNGRB ceiling 25%.
- IGX filed its DRHP with SEBI 14-Jul-2026, a pure Offer For Sale of **up to
  22.28%** equity by IEX (AR p.34: "The Offer comprises an offer for sale of
  up to 22.28% equity shares by IEX"). **Cash proceeds from the sell-down
  remain NOT FOUND** in this run's data sources — no price band or
  valuation is quoted in the AR, the concalls, or the results filings; the
  IGX draft abridged prospectus was not among the files listed for this
  stage.
- **IGX FY26 PAT growth — the annual report resolves this in favour of the
  35% figure, not 28%.** Three separate AR passages state PAT growth at
  35% or 35.29%, all consistent with each other and with the Apr-2026 call:
  - AR p.24 (Board's Report business highlights): "IGX recorded a profit
    after tax of Rs418.68 million, registering a growth in profit after tax
    of **35.29%** over the previous year."
  - AR p.34 (Diversification section): "IGX achieved a Profit After Tax of
    Rs41.9 Crore, **35% higher** than the previous year."
  These corroborate the Apr-2026 call's "35%" (Concall_Apr_2026_Transcript
  p.6) and are unreconciled with the Jul-2026 Analyst Meet's separately
  stated "28%" (Concall_Jul_2026_Transcript p.7) — a Jul-call-only outlier,
  not an AR-vs-call split down the middle. **Downstream stages should use
  35% (35.29%), not 28%, for IGX FY26 PAT growth**, on the strength of two
  independent, mutually consistent AR passages against one concall
  statement.
- IGX volumes: FY26 76.79 million MMBtu (AR p.24, cumulative-volume table),
  consistent across AR and both concalls' "76.8 million MMBtu, +28% YoY".
  Q1FY27 IGX PAT Rs16.3cr, +15.5% YoY (Q1FY27_Press_Release p.1) — outside
  the AR's FY26 coverage, unchanged from run 1.

---

## FORMULA NOTES AND DATA-COVERAGE CAVEATS (read before the scorecard)

- **ROCE / FCF / WC-days window extended to 3 years this run (FY24-FY26)**,
  up from run 1's 2-year window (FY25-FY26), because Annual_Report_2025.txt
  (new this run) carries the FY24 comparative balance sheet and cash flow
  with the same current/non-current liability split and separated capex
  line that only the FY26 AR and the abridged results filings provided in
  run 1. Pre-FY24 annual reports remain outside this run's corpus, so the
  P&L/cash-flow growth metrics (Block C, cumulative CFO/PAT) still use the
  full 8-year Data_Sheet window while ROCE/FCF/WC-days use FY24-FY26 only —
  flagged at each affected line.
- **ROCE.** EBIT = PBT + Interest (Data_Sheet), which necessarily includes
  the ~20-30% of PBT that is treasury/associate income per Load-Bearing
  Fact 2 — the formula is fixed and not substitutable. Capital employed
  (Total Assets − Current Liabilities), consolidated, re-verified against
  the audited AR balance sheets: FY24 Rs1,022.2953cr, FY25 Rs1,190.0902cr,
  FY26 Rs1,417.2182cr (AR p.16/p.241 area of Annual_Report_2026.txt;
  FY24 comparative from Annual_Report_2025.txt).
- A supplementary **operating-only ROCE** (excluding other income and the
  IGX associate share) is materially lower (FY26 ~35.05% vs the formula's
  45.71%) but both figures still clear every Block A score band; the
  distinction does not change any score.
- **"Borrowings" in Data_Sheet (Rs11.16cr FY26) is IEX's total lease
  liability (Ind AS 116), not conventional debt.** Confirmed: non-current
  lease liabilities Rs652.74 lakh + current lease liabilities Rs462.85 lakh
  = Rs1,115.59 lakh = Rs11.16cr, exact match (AR p.179, consolidated
  balance sheet section). No separate "borrowings" line exists at all — IEX
  has zero interest-bearing bank/NBFC debt.
- **Working capital is structurally near-zero for IEX** (net block
  Rs96.68cr vs total assets Rs2,435.74cr); the ~Rs975-1,000cr "Other
  financial liabilities" block on both sides of the balance sheet is
  member/trading-deposit settlement float, a pass-through, not company
  capital. WC-day metrics are computed per the fixed formula but remain,
  per the operator's own framing, "largely meaningless" for this business —
  flagged at each relevant line, not read as a genuine liquidity or
  float-moat signal except where explicitly caveated.
- **Peer data (MCX, BSE, CDSL Data_Sheet.csv) is used this run** for M2,
  M5, M9. All three peers, like IEX, carry a blank "Raw Material Cost" row
  — none of the four companies (asset-light exchange/registry/depository
  platforms) discloses a COGS line. This is a structural feature of the
  business model, not a missing-data gap, and is flagged at M9.

---

## BLOCK A: RETURN ON CAPITAL (20/20)

EBIT (PBT + Interest, Data_Sheet, consolidated): FY24 = 466.15 + 2.83 =
**Rs468.98cr**; FY25 = 564.54 + 2.62 = **Rs567.16cr**; FY26 = 645.56 + 2.28
= **Rs647.84cr**.

Capital employed (Total Assets − Current Liabilities, consolidated,
audited AR): FY24 = 1,773.6599 − 751.3646 = **Rs1,022.2953cr**
(Annual_Report_2025.txt, FY24 comparative column); FY25 = 2,196.6591 −
1,006.5689 = **Rs1,190.0902cr**; FY26 = 2,435.7480 − 1,018.5298 =
**Rs1,417.2182cr** (Annual_Report_2026.txt).

- **A1 Median ROCE** (3-year window FY24-FY26, extended this run from run
  1's 2-year window): FY24 = 468.98/1,022.2953 = **45.88%**; FY25 =
  567.16/1,190.0902 = **47.66%**; FY26 = 647.84/1,417.2182 = **45.71%**.
  Median = **45.88%**. ≥25% → **A1 = 5**
- **A2 Minimum single-year ROCE** (same window): min = 45.71% (FY26). ≥15%
  → **A2 = 5**
- **A3 Median ROE** (full 8-year history, PAT ÷ average Net Worth,
  Data_Sheet, unchanged from run 1): FY19 44.58% (closing NW only, opening
  unavailable), FY20 46.35%, FY21 45.09%, FY22 50.31%, FY23 40.72%, FY24
  39.61%, FY25 40.71%, FY26 39.42%. Median = (40.72+44.58)/2 = **42.65%**.
  ≥20% → **A3 = 5**
- **A4 ROCE trend, latest vs earliest** (now FY26 vs FY24, extended window):
  FY26 45.71% vs FY24 45.88% = a decline of **0.16pp** — smaller than the
  rubric's finest band (1-3pp decline). Read literally, 45.71 < 45.88 fails
  the "latest ≥ earliest" test for the top band; but a 0.16pp gap is an
  order of magnitude below the smallest defined decline band (1-3pp), and
  scoring it at the same level as a genuine 1-3pp decline would overstate
  the finding. **Scored A4 = 5, flagged**: the raw 0.16pp figure is shown
  so a downstream verifier can re-score conservatively (band 3) if a
  stricter literal reading is preferred.

## BLOCK B: CASH GENERATION QUALITY (18/20)

Cumulative CFO (FY19-FY26, Data_Sheet, unchanged) = 138.27+126.02+306.36
+762.32−22.62+298.46+427.25+432.77 = **Rs2,468.83cr**. Cumulative PAT (same
window) = 165.04+175.72+206.09+309.26+305.89+350.78+429.17+492.92 =
**Rs2,434.87cr**. FY23 CFO was −Rs22.62cr against PAT of Rs305.89cr — a
working-capital/settlement-float swing, not an earnings-quality failure.

- **B1 Cumulative CFO ÷ Cumulative PAT** = 2,468.83/2,434.87 = **1.014**.
  ≥1.00 → **B1 = 5**
- **B2 FCF-positive years** (3-year window FY24-FY26, extended this run):
  capex now sourced from the audited AR cash flow statements. FY24 capex
  (purchase of PP&E + intangibles) = Rs15.30cr (Annual_Report_2025.txt,
  consolidated cash flow, FY24 comparative column: 1,529.91 lakh); FY24
  CFO 298.46cr (Data_Sheet) → **FY24 FCF = Rs283.16cr** (positive). FY25
  FCF = CFO 427.25 − capex 7.85 = **Rs419.40cr** (positive,
  Annual_Report_2026.txt FY25 comparative). FY26 FCF = CFO 432.77 − capex
  14.78 = **Rs417.99cr** (positive). 3/3 years positive = 100% → **B2 = 5**
- **B3 Cumulative FCF ÷ Cumulative PAT** (same 3-year window): FCF
  283.16+419.40+417.99 = Rs1,120.55cr; PAT 350.78+429.17+492.92 =
  Rs1,272.87cr. Ratio = 1,120.55/1,272.87 = **0.8804**. ≥0.60 → **B3 = 5**
- **B4 Change in WC Days, latest vs earliest** — now computable as a
  genuine trend for the first time (run 1 scored this N/A). Consolidated
  trade receivables/payables sourced from the audited AR balance sheets:
  FY24 receivables Rs0.7906cr, payables Rs2.5856cr, revenue Rs449.15cr →
  WC days = (0.7906/449.15×365) + 0 − (2.5856/449.15×365) = 0.64 − 2.10 =
  **−1.46 days**. FY26 receivables Rs1.975cr, payables Rs4.6877cr, revenue
  Rs615.65cr → WC days = 1.17 − 2.78 = **−1.61 days**. Change latest vs
  earliest = a further decrease of 0.15 days (more negative). Within ±5
  days → **B4 = 3**

**block_b_trend: stable.** CFO/PAT and FCF/PAT conversion are strong and
consistent across all three audited years now available; WC days sit at a
consistent, near-zero, slightly-negative level across the extended window,
not deteriorating. The one historical wrinkle (FY23 negative CFO) is a
float-timing effect outside the scored window.

## BLOCK C: GROWTH (15/20)

Revenue: FY19 254.08 → FY26 615.65cr (Data_Sheet). PAT: FY19 165.04 → FY26
492.92cr (Data_Sheet). Both 7-period (8-year) CAGRs, unchanged from run 1
(no new P&L history this run).

- **C1 Revenue CAGR** = (615.65/254.08)^(1/7) − 1 = **13.48%**. 10-14.9% →
  **C1 = 3**
- **C2 PAT CAGR** = (492.92/165.04)^(1/7) − 1 = **16.92%**. 15-19.9% →
  **C2 = 4**
- **C3 Positive YoY revenue years**: 6 of 7 positive; FY23 declined
  (400.85cr vs FY22's 431.04cr, Data_Sheet). 85.7% → 75-99% → **C3 = 3**
- **C4 PAT CAGR minus Revenue CAGR** = 16.92 − 13.48 = **+3.44pp**. ≥+3pp →
  **C4 = 5**

## BLOCK D: BALANCE SHEET STRENGTH (19/20)

FY26 consolidated, audited, re-verified against Annual_Report_2026.txt
p.16/p.179-area. "Debt" = total lease liabilities only, Rs11.16cr (IEX has
zero conventional borrowings — confirmed above). Cash + Investments =
105.18 + 1,993.10 = Rs2,098.28cr (Data_Sheet). Net Debt = 11.16 − 2,098.28
= **−Rs2,087.12cr (net cash)**.

Operating EBITDA FY26 = Revenue − opex (excl. D&A/interest/other income) =
615.65 − 95.59 = **Rs520.06cr** (Data_Sheet: Power&Fuel 0.18 + Other Mfr
15.4 + Employee 49.74 + S&A 20.04 + Other Exp 10.23 = 95.59).

- **D1 Net Debt ÷ EBITDA**: net cash → **D1 = 5**
- **D2 Interest Coverage (EBIT ÷ Interest)** = 647.84/2.28 = **284x**. ≥10x
  → **D2 = 5** (mechanically enormous — near-zero interest-bearing debt —
  flagged for context, not a scoring change)
- **D3 Debt ÷ Equity** = 11.16/1,364.56 = **0.008x** (consolidated Total
  equity, AR p.16 area: 1,36,456.28 lakh). <0.1 → **D3 = 5**
- **D4 Current Ratio** = 2,03,222.96/1,01,852.98 (lakh, AR consolidated
  balance sheet) = **1.995x**. Just short of ≥2.0 → **D4 = 4**. ~Rs975cr of
  both current Investments and current "Other financial liabilities" is
  member/trading-deposit float that roughly nets out — not a conventional
  liquidity signal for this business.

## BLOCK E: SHAREHOLDER ALIGNMENT (13/20)

Promoter holding = **0.00%** (no promoter category exists for IEX; listed
2017 with none). Public = 99.73%, Employee Benefit Trusts = 0.27%
(Shareholding_Pattern_30_JUN_2026.xml, XBRL tags PublicShareholding_ContextI
= 0.9973, EmployeeBenefitsTrusts_ContextI = 0.0027). FII = 112,590,860
shares = **12.63%**; DII = 280,532,823 shares = **31.47%**; combined
**44.10%** of the ~891.7cr share base.

- **E1 Promoter holding**: no promoter. Professionally-managed carve-out
  needs FII+DII >50%; IEX's 44.10% falls short. **E1 = 0** — a mechanical/
  structural outcome of having no promoter at all, not a governance red
  flag, flagged explicitly.
- **E2 Promoter holding change**: flat at 0.00% across all 5 shareholding
  filings in this corpus (30-Jun-2025 to 30-Jun-2026 — confirmed the pledge
  tag and the public/EBT split are consistent across all 5 files, re-checked
  this run). This is a **1-year window, not the 3-year window the metric
  calls for**; the full 3-year comparison is NOT FOUND in this run's
  corpus. Because IEX has had no promoter since its 2017 listing (a
  structural fact, not something evidenced by 3 years of filed data in this
  corpus), a 3-year comparison would almost certainly also read flat at
  0.00% — noted as context, not substituted as evidence. Within ±1% →
  **E2 = 3** (1-year basis only, flagged)
- **E3 Promoter pledge**: XBRL tag
  "WhetherAnySharesHeldByPromotersAreEncumberedUnderPledged" = false in all
  5 filings re-checked this run. 0% → **E3 = 5**
- **E4 Contingent liabilities ÷ Net Worth**: **NOW FOUND — the gap closed
  this run.** Standalone Note 39 (AR p.217) and consolidated Note 38 (AR
  p.279) both disclose the SAME single matter: a GST demand from the Sales
  Tax Officer (Adjudicating Authority, Delhi), order dated 28-Aug-2024 —
  Tax Rs260.71 lakh + Interest Rs216.97 lakh + Penalty Rs26.08 lakh =
  **Rs503.76 lakh = Rs5.0376cr total**, under appeal, management believes
  "not tenable and highly unlikely to be retained." No other contingent
  liability is disclosed in either note. Against consolidated Net Worth FY26
  = Rs1,364.56cr (AR balance sheet), ratio = 5.0376/1,364.56 = **0.369%**.
  This confirms the prior-stage pointer (02-notes-pass1.md's "Rs5.04cr,
  ~0.37%") exactly. <5% → **E4 = 5**

## BLOCK F: QUANTITATIVE MOAT SCORING (30/60)

- **M1 Pricing Power**: EBITDA margin FY19 79.85% (202.89/254.08) → FY26
  84.47% (520.06/615.65), +4.62pp, revenue CAGR 13.48% (≥10%). Margin
  expanded ≥2pp AND CAGR ≥10% → **M1 = 5**
- **M2 Cost Advantage vs peer median EBITDA margin** — NOW SCORED, peer
  data supplied this run. Peer FY26 EBITDA margins (Sales − Power&Fuel −
  Other Mfr Exp − Employee Cost − S&A − Other Exp, ÷ Sales, from each
  Data_Sheet.csv): MCX = (2,302.00−5.00−109.26−186.40−212.24−147.42)/
  2,302.00 = **71.32%**; BSE = (5,124.25−29.43−303.78−301.07−936.01−73.68)/
  5,124.25 = **67.92%**; CDSL = (1,144.92−2.24−188.60−160.45−95.80−115.76)/
  1,144.92 = **50.84%**. Peer median = **67.92%** (BSE). IEX FY26 = 84.47%,
  **+16.55pp above peer median**. ≥5pp above → **M2 = 5**
- **M3 Capital Efficiency**: FAT = Revenue/Net Block = 615.65/96.68 =
  **6.37x**; ROCE 45.71-45.88% (all bases clear the bar). FAT>3x AND
  ROCE>20% → **M3 = 5**
- **M4 Customer Stickiness**: one revenue-decline year (FY23), fully
  recovered by FY24. Receivable days swing widely (FY19 65.9 days → FY26
  1.17 days, spikes to ~74-87 days in FY22/FY24 in between) — not "stable
  ±10." Max-1-decline-year band → **M4 = 3**
- **M5 Scale & Dominance** — NOW SCORED. Market caps: BSE Rs138,435.86cr >
  MCX Rs85,223.39cr > CDSL Rs29,260.00cr > **IEX Rs10,396.21cr (smallest of
  the four, last of four by mcap)**. IEX is NOT top-3 mcap in this
  four-company comparison set, despite having the HIGHEST EBITDA margin of
  all four (84.47% vs BSE 67.92%, MCX 71.32%, CDSL 50.84%) — a genuine,
  non-mechanical finding: IEX is the smallest-by-market-cap but
  highest-margin name in its own comparison set. Because the rule's "top 5
  mcap" band is trivially satisfied by any 4th-of-4 ranking in a 4-name
  set, this literal "1" score is a small-n artifact, flagged rather than
  presented as a real "top 5" finding. **M5 = 1**, PEER DATA NEEDED caveat
  removed (peer data now present), replaced with a small-comparison-set
  caveat. For context (not scored): management states IEX has "always been
  maintaining 80-85% market share" within power exchanges specifically
  (Concall_Jul_2026_Transcript p.10) — a different, narrower "segment" than
  the four-company multi-asset-class exchange/depository comparison set
  used here.
- **M6 Technology/R&D**: R&D/Revenue not disclosed as a separate line for
  IEX anywhere in this corpus (folded into employee/technology cost).
  **M6 = 0, N/A (not in provided data)**
- **M7 Regulatory/License**: corpus references only 3 named power exchanges
  (IEX, HPX, PXIL — Concall_Apr_2026_Transcript p.13), so ≤5 players.
  EBITDA margin moved +4.62pp over the 8-year period (within the ±5pp band)
  → ≤10 players AND ±5pp → **M7 = 3**
- **M8 Distribution**: purely digital platform (9,100+ registered
  participants, AR p.20/p.25), no physical outlet network. Rule scores
  "none or purely digital" as 0 → **M8 = 0**
- **M9 Brand** — NOW ATTEMPTED with peer data, but structurally
  unscoreable. The fixed GM proxy formula, (Revenue − Material Cost) ÷
  Revenue, requires a Material Cost line. **None of the four companies —
  IEX or any of MCX/BSE/CDSL — discloses a Raw Material Cost line**; all
  four Data_Sheet.csv files carry it blank. This is a structural feature of
  asset-light exchange/registry/depository platforms (no COGS concept
  applies), not a peer-data-availability gap — peer data IS present, the
  underlying cost category simply does not exist for this business model.
  **M9 = 0, N/A (structural — no Material/COGS line for IEX or any peer)**
- **M10 Switching Costs**: revenue grew all years but FY23 (growth-all-but-
  one-year band); receivable days FELL sharply over the period (not rose)
  → "growth all but 1 year AND stable" band → **M10 = 3**
- **M11 Network Effects** (8 years available, ≥6-year test valid): latest
  3yr revenue CAGR (FY23→FY26) = (615.65/400.85)^(1/3)−1 = **15.38%**;
  prior 3yr CAGR (FY20→FY23) = (400.85/257.13)^(1/3)−1 = **15.96%**. Latest
  is NOT greater than prior. Selling & admin expense fell from 7.41% of
  revenue (FY19) to 3.26% (FY26) — declining, not rising. Neither the
  5-band, the 3-band (needs ≥20% latest CAGR), nor the literal 1-band
  condition (growth>15% but selling% RISING) is met → **M11 = 0** (the
  near-miss is favourable-direction, not a real weakness, but the literal
  band test fails)
- **M12 Negative WC/Float**: WC days negative in all 3 computable years
  (FY24 −1.46, FY25 −0.59, FY26 −1.61 — 3-year window now, up from run 1's
  2-year window). Negative in majority (3/3) → **M12 = 5**, heavily
  caveated: this reflects near-zero, not meaningfully negative, working
  capital — a structural artifact of a fee-only platform with de minimis
  receivables/payables and pass-through member-deposit float, not a
  retailer-style float moat.

**Moats present (score ≥3): M1, M2, M3, M4, M7, M10, M12 = 7 of 12** (up
from run 1's 6, driven by M2 now scoring 5 with peer data present).
**Moat classification: 6+ present = FORTRESS.**

---

## DASHBOARD SUMMARY

| Block | Score | Max | Run 1 | Change |
|---|---|---|---|---|
| A — Return on Capital | 20 | 20 | 18 | +2 (A4, extended window) |
| B — Cash Generation Quality | 18 | 20 | 15 | +3 (B4 now scored) |
| C — Growth | 15 | 20 | 15 | 0 |
| D — Balance Sheet Strength | 19 | 20 | 19 | 0 |
| E — Shareholder Alignment | 13 | 20 | 8 | +5 (E4 now scored) |
| **Core total** | **85** | **100** | **75** | **+10** |
| F — Quantitative Moat | 30 | 60 | 24 | +6 (M2 now scored) |
| **Grand total** | **115** | **160** | **99** | **+16** |

Moat profile: `M1=5 M2=5 M3=5 M4=3 M5=1 M6=0 M7=3 M8=0 M9=0 M10=3 M11=0 M12=5`
→ FORTRESS (7/12 present).

**Deal-breaker check** (none triggered): Block A (20) not <8; Block B (18)
not <8; median ROCE (45.88%) not <10%; cumulative CFO/PAT (1.014) not
<0.50; pledge (0%) not >15%; Net Debt/EBITDA is net cash, no AND-condition
with IC<3x to trigger; revenue declined in only 1 of 7 years, not a
majority; PAT positive in every one of the last 3 years (FY24 350.78, FY25
429.17, FY26 492.92); 8 years of history, not <3.

**Data confidence**: 8 years (7-9 band) = moderate. No downgrade triggered.
The ROCE/FCF/WC-days sub-window is now 3 years (FY24-FY26), improved from
run 1's 2 years but still short of the 8-year P&L window — flagged at each
affected line, not a whole-run confidence downgrade.

**Classification matrix**: Core 85 sits in the ≥80 band; moat class is
FORTRESS. Core ≥80 + FORTRESS/STRONG → **EXCELLENT**.

This is a tier change from run 1's GOOD+ (Core 75, 60-79 band). The change
is driven entirely by closing the two source gaps this run was built to
close: (1) the FY24 annual-report comparative data extended the ROCE/FCF/
WC-days window from 2 to 3 years, fixing A4 (18→20 in Block A) and enabling
B4 for the first time (15→18 in Block B); (2) the full annual report
resolved E4 from NOT FOUND to a verified 0.37% ratio (8→13 in Block E);
(3) peer data resolved M2 to a clearly-scored 5 (24→30 in Block F). None of
these are re-interpretations of the same evidence — each is new evidence
this run's inputs supplied that run 1's did not have.

**Strongest block**: A (Return on Capital, 20/20) — median ROCE 45.88%
across all three audited years now available, with a genuinely flat trend
(0.16pp) rather than the 1.95pp apparent decline run 1 measured off a
2-year window.

**Weakest block**: C (Growth, 15/20) — 13.48% revenue CAGR and one
down-year (FY23) hold C1 and C3 below full marks; this is the one block
unaffected by this run's new inputs, since no additional P&L history became
available.

**Decision line**: PROCEED to the next stage on the Gate 0 numbers alone.
IEX clears every deal-breaker with room, carries a FORTRESS-tier moat count
now partly corroborated by peer data (not just IEX's own numbers), and
shows strong, now 3-year-confirmed capital-return and cash-conversion
metrics. The Block E score, still the weakest core block after Block C, is
driven by the same structural E1 mechanical zero (no promoter) as run 1,
not by any new governance concern — both pledge and the newly-scored E4 are
clean. The open items that carry forward as real substance, not scoring
noise:
(1) the annual report itself contains an unreconciled three-way
inconsistency on RTM's FY26 volume share (34% at the internally-consistent
p.25 product-mix chart and p.62 risk section vs "nearly 40%"/"approximately
39%" at p.33 and p.36-37 MD&A) — the better-evidenced figure is DAM=39%/
RTM=34%, but this stage flags rather than fully resolves it, since the AR's
own drafting has not reconciled it either;
(2) IGX's FY26 PAT growth is now resolved in the annual report's favour at
35% (35.29%), two independent AR passages against the Jul-2026 Analyst
Meet's outlier 28% figure — downstream stages should use 35%;
(3) treasury and IGX-associate income's share of PBT rose from 23.41% to
29.78% quarter-on-quarter into Q1FY27, a trend worth watching;
(4) IGX's OFS cash proceeds remain entirely absent from this run's data;
(5) a genuine, if two-way-only, revenue segment split exists (Electricity
bundle vs Certificates, AR Note 28) that run 1 did not find — still no
split within the Electricity bundle by DAM/RTM/TAM/Green on a revenue
basis.

---

## DATA NOTES

- Data_Sheet's "Other Income" row (Rs151.10cr FY26, Rs52.65cr Q1FY27) is a
  composite of pure treasury other income plus IEX's equity-method share of
  IGX's profit — see Load-Bearing Fact 2, re-verified this run against the
  full annual report (not just the abbreviated results filings) to the
  cent.
- Data_Sheet's "Borrowings" row is IEX's total lease liability under Ind AS
  116, not conventional debt — re-verified against the AR this run. IEX
  carries zero interest-bearing bank/NBFC borrowings.
- ROCE (A1/A2/A4), FCF (B2/B3) and WC-days (B4) now computed on a 3-year
  window (FY24-FY26), extended this run from run 1's 2-year window, using
  the FY24 comparative balance sheet and cash flow statement newly
  available in Annual_Report_2025.txt. Pre-FY24 data remains outside this
  run's corpus.
- Revenue-basis segment disclosure: a two-way split (Electricity bundle vs
  Certificates) exists in AR Note 28 — a correction to run 1's finding of
  "no revenue-basis segment split anywhere." No further split within the
  Electricity bundle (DAM/RTM/TAM/Green) exists on a revenue basis anywhere
  in this corpus.
- RTM FY26 volume share: the annual report itself carries two mutually
  inconsistent figures (34% at p.17/p.25/p.62-consistent cluster vs
  ~39-40% at p.33/p.36-37) — see Load-Bearing Fact 1. Flagged, not resolved,
  by this stage; the better-evidenced figure is 34% (DAM=39%).
- IGX FY26 PAT growth: resolved this run at 35% (35.29%), on two
  independent AR passages, against the Jul-2026 Analyst Meet's isolated 28%
  claim — see Load-Bearing Fact 4.
- IGX OFS cash proceeds: still NOT FOUND in this run's data sources.
- Contingent liabilities (E4): NOW FOUND — Rs5.0376cr, 0.369% of net worth,
  one GST matter, AR standalone Note 39 (p.217) and consolidated Note 38
  (p.279), verifying the prior-stage pointer (02-notes-pass1.md) exactly.
- M2, M5 now scored with peer data (MCX, BSE, CDSL Data_Sheet.csv) supplied
  this run; PEER DATA NEEDED no longer applies to either.
- M9 remains unscored (0) but for a different, structural reason this run:
  no Material/COGS line exists for IEX or any of the three peers (all four
  are asset-light platforms with no such disclosed cost category), so the
  fixed GM proxy formula is not computable for anyone in the comparison
  set — not a case of missing peer data.
- M6 (R&D/Revenue) remains N/A — not a disclosed line item for IEX in any
  source this run.
