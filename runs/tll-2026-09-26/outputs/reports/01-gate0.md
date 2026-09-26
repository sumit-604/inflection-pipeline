# GATE 0 SCORECARD — Trident Lifeline Ltd (TLL), BSE SME 543616
Run date: 2026-09-26 | Basis: Consolidated (five subsidiaries) | Model: claude-sonnet-5
REWORK ROUND (run 2). This run corrects run 1 against the framework audit
(outputs/final/gate-recommendation.md, rework items 12-16; detail in
outputs/superseded/12c-verifier-framework-run1-superseded.md). Superseded
run-1 report and block are at outputs/superseded/01-gate0-run1-superseded.md
and B01-gate0-run1-superseded.yaml. Every item below was re-checked against
the rule text and the primary source myself, not accepted on the auditor's
word alone; two items (15, 16) turned up anchors the auditor itself did not
cite.

Data available: 5 years (FY22 to FY26), annual P&L and balance sheet
(screener-Data_Sheet.csv). Balance-sheet current-liability / trade-payable
detail needed for ROCE (A1/A2/A4) and Working Capital Days (B4) is only
available for FY24-FY26 (3 years) — the FY26 and FY25 Annual Reports carry
the consolidated current-liabilities split; no FY23/FY22 results filing or
AR is held in this corpus to split current liabilities that far back.
Scoring adapted: Blocks A/B rows that need the split run on the 3-year
FY24-FY26 window; Blocks C, and the P&L-only rows of D/E, run on the full
5-year window. This is stated per row below.

## REWORK RESOLUTION (items 12-16 of the gate-recommendation)

**12. EBIT basis (ACCEPTED).** The formula block (prompts/01-gate-0-pipeline.md,
line 27-31) gives one fixed ROCE formula and rule 2 bars qualitative
judgment: no substituted alternatives. EBIT without a stated qualifier is
the conventional PBT + Interest; there is no "operating EBIT" variant
defined anywhere in the prompt file. Run 1 substituted PBT + Interest −
Other Income without authority to do so. Corrected: EBIT = PBT + Interest
(all-in) is now the SCORED basis for A1, A2, A4, D2 and M3. The
operating-EBIT figure (excluding Other Income) is kept as a disclosed
sensitivity only, given Other Income is 34-60% of PBT in FY25-26 — that
observation has analytical merit but the rule does not permit it to
replace the scored figure. D1 is unaffected: its EBITDA is a distinct
metric from "EBIT" and its operating basis (excluding Other Income)
independently matches screener's own published "Operating Profit"
convention (screener-Data_Sheet.csv quarterly rows: 5.17+6.86+5.09+10.99 =
28.11 Cr FY26, same figure D1 already used), so D1's basis is not a
substitution and stays as run 1 scored it.

**13. M4 literal tier (ACCEPTED).** M4 tier 3 reads "max 1 decline year,
fully recovered = 3" (prompts/01-gate-0-pipeline.md, M4 rule text) — no
receivable-days leg. TLL has zero revenue-decline years FY23-26
(screener-Data_Sheet.csv Sales row: 21.77→31.69→44.63→86.92→129.02, all
positive YoY). Zero decline years satisfies "max 1 decline year" literally
(0 ≤ 1); with nothing to recover from, "fully recovered" is vacuously true.
Run 1's "no literal tier fits" was wrong; the top tier's compound test
(decline years AND receivable-days stability) is what run 1 was actually
scoring against, and that reasoning belongs to a different row (M10), not
M4. Corrected: M4 = 3 (present).

**14. Recomputed card — subsumed into this run's own scorecard below.** Not
a separate action; the corrected Block A, Block F and classification
numbers below are the answer to item 14.

**15. FCF false input gap (ACCEPTED, extended).** Run 1 claimed the AR's
"Purchase of Fixed Assets" line could not be separated from acquisition
outflows. That claim is false. Checked directly: the FY26 AR consolidated
cash flow statement carries "Purchase of Fixed Assets" ₹3,647.24L (FY26)
and ₹1,109.95L (FY25) on its own line, separate from "Purchase of Equity
Shares" ₹794.67L / ₹565.80L (per 03-ardeep.md Phase 3A, sourced to
Annual_Report_2026.txt Consolidated Cash Flow Statement). Going further
than the audit asked: the FY25 AR's own consolidated cash flow statement
carries the SAME line with a THIRD data point — a FY24 comparative column
— "Purchase of Fixed Assets" ₹1,644.68L (Annual_Report_2025.txt,
Consolidated Cash Flow Statement, lines 9007-9011; reconciles exactly: Net
Investing CF FY25 ₹(1,382.47)L = Interest Received 262.21 + Increase in LT
Loans&Advances 330.91 − Investment in FD 299.85 − Purchase of Equity
Shares 565.80 − Purchase of Fixed Assets 1,109.95). This gives a genuine
defined-FCF figure for THREE years (FY24-26), not the two the audit
flagged. FY22-FY23 remain on the CFO + net Investing CF proxy: that is a
REAL gap (no AR or results filing that far back carries the capex
breakdown, per B00 input_gaps), distinct from the false gap run 1 claimed
for FY24-26. See Block B below for the recomputed figures; B2/B3 scores are
unchanged (both were, and remain, at the floor).

**16. One net worth basis (ACCEPTED); M5 (ACCEPTED, scored).** Run 1 used
three different net-worth denominators in one scorecard: A3 used screener
Share Capital + Reserves 100.40 Cr (which folds in ₹3.73 Cr of share
application money pending allotment, per Annual_Report_2026.txt line 9949,
372.67 lakh); D3 added Minority Interest to get 107.89 Cr; E4 used the AR's
own face-value Shareholders' Funds excluding Minority Interest, 96.68 Cr
(Share Capital ₹1,193.30L + Reserves ₹8,474.26L, Annual_Report_2026.txt
lines 9933-9938). Corrected: ONE basis used throughout — AR-face
Shareholders' Funds excluding Minority Interest (Share Capital + Reserves,
excluding both minority interest, which is not the parent's equity, and
share application money pending allotment, which is not yet issued
equity), for every year it is available (FY25-26 from the AR; FY22-24 use
screener Share Capital + Reserves, since no minority interest or pending
allotment existed in those years to create the same discrepancy). See
Block A (A3) and Block D (D3) and Block E (E4) below — none of the three
scores changes band, but the basis is now internally consistent and
stated once. M5 (Scale & Dominance): run 1 marked this "PEER DATA NEEDED,"
but the same three peer Data_Sheet.csv files used for M2 and M9 carry
Market Capitalization on row 8: TLL ₹487.49 Cr, SENORES ₹6,241.18 Cr,
INNOVACAP ₹7,330.51 Cr, CAPLIPOINT ₹21,550.08 Cr. On this four-name set TLL
ranks last (4th of 4), which literally meets "top 5 mcap = 1" (M5 rule
text). Corrected: M5 = 1 (not a present moat; present needs ≥3).

---

## LOAD-BEARING FACTS CHECK (first priority, per companies/TLL.md SPEAR)

**LBF1 (cash conversion).** Unchanged from run 1, confirmed against the AR
consolidated balance sheet and cash flow statement: Trade Receivables
Rs 27.68 Cr (FY25) to Rs 73.65 Cr (FY26) (Annual_Report_2026.pdf, Note 17:
2,768.25 -> 7,365.39 lakh; matches screener-Data_Sheet.csv exactly); debtor
days 116.2 to 208.4 (Receivables/Sales x 365); CFO Rs +4.69 Cr FY26 on PAT
Rs 19.04 Cr FY26 (screener-Data_Sheet.csv; AR Consolidated CF Statement,
469.07 lakh). CFO negative in FY22 (-0.21 Cr), FY23 (-19.00 Cr), FY25
(-10.24 Cr) — 3 of 5 years. Working Capital Days rose from 151.1 (FY24) to
202.8 (FY26), +51.7 days in two years.

**LBF1 SENSITIVITY (new, carried from Stage 3's independent re-derivation,
03-ardeep.md).** Stage 3 re-summed the cash flow statement's own line items
with the undisclosed "Changes in Working Capital Facilities" addback
removed: FY26 CFO would be ₹469.07L − ₹945.65L = **₹(476.58)L** (≈ −Rs 4.77
Cr), NEGATIVE against the ₹469.07L printed; FY25 CFO would be ₹(398.50)L −
₹625.67L = **₹(1,024.17)L**, which is exactly the FY25 AR's own audited
FY25 figure (the number run 1 flagged as restated). This stage scores
Block B on the AS-FILED / screener basis (per the pipeline instruction to
use the provided Data_Sheet consistently, and because Gate 0 is a
no-judgment mechanical scorer, not the stage that adjudicates undisclosed
reclassifications). The true-CFO basis is shown here as the sensitivity:
on it, B1's cumulative CFO/PAT and B2/B3's FCF ratios would all be MORE
negative than scored below, not less — the correction does not flatter
TLL on either basis, and no B-row score changes as a result (all four
rows are already at the floor).

**LBF2 (refiled results / accounting quality).** Unchanged from run 1: (1)
Other Income is 60.4% of PBT (FY25) / 34.1% of PBT (FY26); FY26's largest
component is an unexplained "Claim Income" line, Rs 5.41 Cr (58% of Other
Income), AR Note 22, nature NOT FOUND. (2) FY25 CFO restated between the
FY25 AR (audited then, −Rs 10.24 Cr) and the FY26 AR's FY25 comparative
column (−Rs 3.99 Cr as originally reported) — Stage 3's true-CFO
sensitivity above now explains the mechanism: the undisclosed "Changes in
Working Capital Facilities" addback of ₹625.67L in the FY26 AR's
presentation of FY25 is exactly what produces the ₹1,024.17L vs ₹398.50L
gap. Both findings forwarded, not resolved, per Gate 0's
no-qualitative-judgment mandate; Stage 3 has since substantially resolved
(2).

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — computed, FY24-FY26 window, EBIT = PBT + Interest (rule-literal; corrected per item 12)

Capital Employed = Total Assets - Current Liabilities. Current Liabilities
from AR consolidated balance sheet (screener Data_Sheet's "Other
Liabilities" row does not split current from non-current):
- FY24: CL Rs 20.26 Cr (Annual_Report_2025.txt, Consolidated Balance
  Sheet, "(4) Current Liabilities Total" 2,025.62 lakh); TA Rs 87.08 Cr
- FY25: CL Rs 53.55 Cr (Annual_Report_2026.txt, Consolidated Balance
  Sheet FY25 comparative, 5,355.46 lakh); TA Rs 156.01 Cr (AR)
- FY26: CL Rs 87.89 Cr (Annual_Report_2026.txt, Consolidated Balance
  Sheet, 8,789.27 lakh); TA Rs 236.83 Cr

| Year | EBIT (all-in, scored) | EBIT (op., sensitivity) | Capital Employed | ROCE (all-in) | ROCE (op., sensitivity) |
|---|---|---|---|---|---|
| FY24 | 9.34 Cr (8.69+0.65) | 7.26 Cr | 66.82 Cr | 13.98% | 10.87% |
| FY25 | 17.76 Cr (13.62+4.14) | 9.53 Cr | 102.46 Cr | 17.33% | 9.30% |
| FY26 | 31.31 Cr (27.19+4.12) | 22.04 Cr | 148.94 Cr | 21.02% | 14.80% |

(All figures: screener-Data_Sheet.csv P&L rows, computed; AR sources for
CL/TA as cited above.)

- **A1 Median ROCE = 17.33%** (FY25) -> band 15-19.9% = **3**
  (operating-basis sensitivity: median 10.87% -> band 10-14.9% = 1; shown,
  not scored, per item 12)
- **A2 Minimum single-year ROCE = 13.98%** (FY24) -> band 12-14.9% = **3**
  (operating-basis sensitivity: 9.30% -> band 8-11.9% = 1; shown, not scored)
- **A3 Median ROE = 23.6%** (recomputed on the single net-worth basis, item
  16: AR Shareholders' Funds excl. Minority Interest for FY25-26, screener
  Share Capital+Reserves for FY22-24, since no minority interest or
  pending allotment existed pre-FY25 to create the discrepancy). Net worth
  used: FY22 4.78 Cr (closing only, no opening pre-IPO) / FY23 45.64 Cr /
  FY24 52.90 Cr / FY25 64.46 Cr / FY26 96.68 Cr (Annual_Report_2026.txt
  lines 9933-9938: Share Capital 1,193.30L + Reserves 8,474.26L, excl.
  Minority Interest 749.02L and excl. the 372.67L share application
  money folded into screener's reserves figure). ROE series: FY22 82.6%*
  FY23 23.9% FY24 12.9% FY25 20.0% FY26 23.6% -> median (sorted 12.9, 20.0,
  23.6, 23.9, 82.6) = **23.6%** -> band ≥20% = **5**
  (*FY22 distorted by a near-zero pre-IPO equity base, kept per no-estimate
  rule; unchanged from run 1)
- **A4 ROCE trend, FY26 (21.02%) vs FY24 (13.98%)**: latest ≥ earliest ->
  **5**

**Block A = 16/20** (up from run 1's 12/20; the rule-literal EBIT basis
raises A1 and A2 by two bands each, matching the framework audit's
recompute exactly)

## BLOCK B: CASH GENERATION QUALITY (Max 20) — computed, 5-year window (B1-B3), 3-year window (B4)

- **B1 Cumulative CFO / Cumulative PAT** (unchanged from run 1; not a
  formula the EBIT/FCF corrections touch): CFO sum FY22-26 =
  -0.21-19.00+2.23-10.24+4.69 = **-22.53 Cr**; PAT sum =
  3.95+6.02+6.34+11.75+19.04 = **47.10 Cr** (screener-Data_Sheet.csv).
  Ratio = -0.478 -> band <0.50 = **0** [DEAL-BREAKER #4]. Sensitivity: on
  Stage 3's true-CFO basis (LBF1 sensitivity above), FY26 CFO is
  approximately -Rs 4.77 Cr rather than +Rs 4.69 Cr — cumulative CFO would
  be more negative still, ratio further below the floor; no change to the
  score, which is already 0.
- **B2 FCF-positive years proportion**: FCF now computed on the rule's own
  formula (CFO − capex, capex = Purchase of Fixed Assets, item 15
  correction) for the three years the AR carries the line, and on the CFO
  + net Investing CF proxy for the two years it does not (a real, not
  false, gap — no AR or results filing back to FY22/FY23 is in this
  corpus):
  - FY22 (proxy): -0.21 + (-0.45) = -0.66 Cr
  - FY23 (proxy): -19.00 + (-9.69) = -28.69 Cr
  - FY24 (defined): CFO 2.23 - Purchase of Fixed Assets 16.4468 Cr
    (Annual_Report_2025.txt, Consolidated Cash Flow Statement, FY24
    comparative column, 1,644.68 lakh) = **-14.22 Cr**
  - FY25 (defined): CFO -10.24 - Purchase of Fixed Assets 11.0995 Cr
    (Annual_Report_2025.txt / Annual_Report_2026.txt, both show 1,109.95
    lakh) = **-21.34 Cr**
  - FY26 (defined): CFO 4.69 - Purchase of Fixed Assets 36.4724 Cr
    (Annual_Report_2026.txt, 3,647.24 lakh, per 03-ardeep.md Phase 3A) =
    **-31.78 Cr**
  All 5 years negative -> 0% positive -> band <50% = **0** (score
  unchanged from run 1; the corrected figures are individually different
  from run 1's proxy-for-all-years numbers, most visibly FY24 -14.22 Cr
  here vs -18.13 Cr in run 1, but the proportion-positive answer is
  identical: zero either way)
- **B3 Cumulative FCF / Cumulative PAT**: cumulative defined/proxy FCF =
  -0.66-28.69-14.22-21.34-31.78 = **-96.69 Cr**; PAT = 47.10 Cr -> ratio
  -2.05, negative -> band <0.20 or negative = **0** (unchanged score;
  run 1's proxy-only cumulative was -103.35 Cr, similarly negative)
- **B4 Change in WC Days, FY26 vs FY24** (unchanged from run 1, not
  touched by any of the five audit items): Receivable Days + Inventory
  Days - Payable Days, Trade Payables from AR consolidated balance sheet.
  WC Days: FY24 = 151.1, FY25 = 172.7, FY26 = 202.8. Change = +51.7 days ->
  band increased >15 days = **0**

**Block B = 0/20** [DEAL-BREAKER #2: Block B <8 -> max GOOD]

**block_b_trend: DETERIORATING** — cumulative CFO is negative (-Rs 22.5 Cr,
as-filed basis) against cumulative PAT of Rs 47.1 Cr FY22-26; on Stage 3's
true-CFO sensitivity it is more negative still; Working Capital Days rose
from 151 (FY24) to 203 (FY26), +52 days in two years.

## BLOCK C: GROWTH (Max 20) — computed, 5-year window (unchanged from run 1; not touched by any audit item)

All from screener-Data_Sheet.csv Sales / Net profit rows, FY22-FY26.

- **C1 Revenue CAGR** = (129.02/21.77)^(1/4)-1 = **56.05%** -> band ≥20% = **5**
- **C2 PAT CAGR** = (19.04/3.95)^(1/4)-1 = **48.16%** -> band ≥20% = **5**
- **C3 Positive YoY revenue years**: FY23 +45.6%, FY24 +40.9%, FY25 +94.7%,
  FY26 +48.4% -> 4/4 = 100% -> **5**
- **C4 PAT CAGR - Revenue CAGR** = 48.16% - 56.05% = **-7.89pp** -> band
  -3 to -8pp = **1**

**Block C = 16/20**

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — latest = FY26, computed

- **D1 Net Debt / EBITDA** (unchanged from run 1; the operating-EBITDA
  basis independently matches screener's own Operating Profit convention,
  see item 12 resolution above — not a substitution): Net Debt =
  Borrowings 72.99 Cr - Cash 4.22 Cr = 68.77 Cr. EBITDA (operating) =
  PBT+Interest+Dep-OtherIncome = 27.19+4.12+6.07-9.27 = 28.11 Cr. Ratio =
  **2.45x** -> band 2-3x = **1**
- **D2 Interest Coverage, EBIT(all-in, per item 12)/Interest** =
  31.31/4.12 = **7.60x** -> band 5-9.9x = **4** (unchanged band; the
  operating-basis sensitivity, 22.04/4.12 = 5.35x, sits in the same band)
- **D3 Debt/Equity** = Borrowings 72.99 Cr / Net Worth 96.68 Cr (single
  basis per item 16: Share Capital + Reserves, excl. Minority Interest and
  excl. share application money) = **0.76x** -> band 0.5-1.0x = **3**
  (unchanged band from run 1's 0.68x on the screener-inclusive basis)
- **D4 Current Ratio** (unchanged from run 1): Current Assets Rs 139.51 Cr
  / Current Liabilities Rs 87.89 Cr = **1.59x** -> band 1.5-1.99x = **4**

**Block D = 12/20**

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — latest = Jun-2026 where noted

- **E1 Promoter holding, latest quarter (Jun-2026) = 62.59%** (unchanged
  from run 1; inputs/shareholding/screener-shareholding-pattern.csv — a
  screener aggregation, NOT a filing, per B00) -> band ≥60% = **5**
- **E2 Promoter holding change over ~3 years** (Sep-2023 70.04% to
  Jun-2026 62.59%) = **-7.45pp** (unchanged) -> band decreased >3% = **0**
- **E3 Promoter pledge (latest) = NOT FOUND in provided data.** (unchanged)
  Scored **0** per the no-estimate rule.
- **E4 Contingent Liabilities / Net Worth**: Consolidated contingent
  liabilities (guarantees to Talon Healthcare LLP & Tench Life Sciences
  LLP) Rs 5.00 Cr FY26 (Annual_Report_2026.txt, Note 32) / Net Worth
  Rs 96.68 Cr (single basis per item 16, same figure now used in A3 and
  D3). Ratio = **5.17%** -> band 5-15% = **3** (unchanged score;
  previously derived on its own basis, now the SAME basis as A3/D3
  rather than a third, separately-chosen one)

**Block E = 8/20**

---

## CORE SCORE

| Block | Score | /20 |
|---|---|---|
| A — Return on Capital | 16 | 20 |
| B — Cash Generation | 0 | 20 |
| C — Growth | 16 | 20 |
| D — Balance Sheet | 12 | 20 |
| E — Shareholder Alignment | 8 | 20 |
| **CORE TOTAL** | **52** | **100** |

Strongest block: A and C tied (16/20 each) — Return on Capital (corrected
basis) and Growth. Weakest block: B (Cash Generation), 0/20, unchanged and
still the widest possible spread on this scorecard.

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Peer set: CAPLIPOINT, SENORES, INNOVACAP Data_Sheet.csv (FY26 column), per
runs/tll-2026-09-26/inputs/screening/.

- **M1 Pricing Power** (unchanged from run 1): EBITDA margin (op.) FY22 =
  12.5% (2.72/21.77), FY26 = 21.8% (28.11/129.02) -> expanded +9.3pp AND
  revenue CAGR 56% ≥10% -> **5**
- **M2 Cost Advantage vs peer median EBITDA margin** (unchanged): TLL FY26
  21.8% vs peer median 26.6% (CAPLIPOINT 34.98%, SENORES 26.61%, INNOVACAP
  14.90%) -> BELOW peer median -> **0**
- **M3 Capital Efficiency** (CORRECTED per item 12): FAT = Sales/Net Block
  = 129.02/60.73 = 2.12x; ROCE (all-in, per item 12) FY26 = 21.02% ->
  FAT>2x AND ROCE>15% -> **3** (present; was 1 in run 1 on the operating
  ROCE basis)
- **M4 Customer Stickiness** (CORRECTED per item 13): zero revenue-decline
  years FY23-26 -> literal tier 3 ("max 1 decline year, fully recovered")
  is met -> **3** (present; was 1 in run 1's judgment call, which the
  audit correctly identified as not matching the rule's literal wording)
- **M5 Scale & Dominance** (CORRECTED per item 16): peer market caps ARE
  in the corpus (row 8 of each Data_Sheet.csv): TLL Rs 487.49 Cr, SENORES
  Rs 6,241.18 Cr, INNOVACAP Rs 7,330.51 Cr, CAPLIPOINT Rs 21,550.08 Cr. TLL
  ranks 4th of 4 -> literal "top 5 mcap" -> **1** (not present; run 1's
  "PEER DATA NEEDED" was incorrect — the data was in the same sheets M2
  and M9 already used)
- **M6 Technology/R&D** (unchanged): no R&D spend line located -> **0**,
  NOT FOUND
- **M7 Regulatory/License** (unchanged): regulated but >10 listed players
  -> **1**
- **M8 Distribution** (unchanged): mentioned, unquantified -> **1**
- **M9 Brand** (unchanged): GM proxy TLL 46.4% vs peer median 57.5% ->
  below peer median -> **0**
- **M10 Switching Costs** (unchanged, confirmed correct by the audit):
  revenue grew every year but receivable days rose ~98 days over
  FY24-26, far above the ≤10-day cap for the tier requiring "AND stable"
  -> **0**
- **M11 Network Effects** (unchanged): <6-year fallback; revenue CAGR
  56% ≥20% but Selling & Admin % of sales rose 3.9% (FY22) to 6.3% (FY25)
  -> **1**
- **M12 Negative WC/Float** (unchanged): WC days 151.1/172.7/202.8, none
  negative, all far above 45-day ceiling -> **0**

| Test | Score |
|---|---|
| M1 Pricing Power | 5 |
| M2 Cost Advantage | 0 |
| M3 Capital Efficiency | 3 (was 1) |
| M4 Customer Stickiness | 3 (was 1) |
| M5 Scale & Dominance | 1 (was 0, PEER DATA NEEDED) |
| M6 Technology/R&D | 0 (NOT FOUND) |
| M7 Regulatory/License | 1 |
| M8 Distribution | 1 |
| M9 Brand | 0 |
| M10 Switching Costs | 0 |
| M11 Network Effects | 1 |
| M12 Negative WC/Float | 0 |
| **MOAT TOTAL** | **15 / 60** (was 10) |

Moats "present" (score ≥3): **M1 Pricing Power (5), M3 Capital Efficiency
(3), M4 Customer Stickiness (3)** — three moats now clear the bar, up from
one in run 1.

**Moats confirmed = 3. Moat classification: 3 present -> MODERATE** (was
THIN in run 1)

```
Moat profile:
M1  [#####] 5  present
M2  [     ] 0
M3  [###  ] 3  present
M4  [###  ] 3  present
M5  [#    ] 1
M6  [     ] 0  NOT FOUND
M7  [#    ] 1
M8  [#    ] 1
M9  [     ] 0
M10 [     ] 0
M11 [#    ] 1
M12 [     ] 0
```

---

## CLASSIFICATION

Grand Total = Core 52 + Moat 15 = **67 / 160** (was 58 in run 1)

Data confidence: 5 years of P&L history (FY22-FY26) -> band "5-6 lower,
flag 'may not have seen full cycle'". Sub-metrics needing the balance-sheet
current-liability split (ROCE, WC Days) run on a 3-year sub-window
(FY24-26) only, a separate limitation stated per-row above, not the
trigger for the "3-4 LIMITED" history-downgrade rule. **history_downgrade:
false** on that basis; the 5-6 year flag applies to the whole scorecard:
**FLAG — may not have seen a full cycle.**

Classification matrix: Core 52 falls in the 40-59 band -> **AVERAGE**
(independent of moat tier — the Core 40-59 band does not branch on moat
class in the matrix; moving from THIN to MODERATE this run does not change
the classification for that reason).

Deal-breaker check:
1. Block A <8: A=16, not triggered (was not triggered in run 1 either,
   at 12)
2. **Block B <8: B=0, TRIGGERED -> max GOOD**
3. Median ROCE <10%: 17.33% (all-in basis, now the scored figure), not
   triggered — this line moves further from the boundary than run 1's
   10.87%, which had been within 0.87pp of triggering
4. **Cumulative CFO/PAT <0.50: -0.478, TRIGGERED -> max AVERAGE**
5. Pledge >15%: NOT FOUND, not triggered
6. ND/EBITDA >3x AND IC <3x: ND/EBITDA=2.45x, IC=7.60x (all-in), not
   triggered
7. Revenue declined majority of years: never declined, not triggered
8. PAT negative any of last 3 years: FY24/25/26 all positive, not
   triggered
9. History <3 years: 5 years of P&L held, not triggered

Binding cap: deal-breaker #4 (max AVERAGE) is the stricter of the two
triggered caps and matches the score-band outcome. **No conflict.**

## CLASSIFICATION: AVERAGE

Strongest block: **A and C (16/20 each)** — Return on Capital, corrected
to the rule-literal EBIT basis (median ROCE 17.33%, up two bands from run
1's operating-EBIT median of 10.87%), and Growth, driven by a 56% revenue
CAGR and a 48% PAT CAGR with zero revenue-decline years across five
audited years.

Weakest block: **B — Cash Generation (0/20)** — every one of the four rows
scored zero, on both the as-filed and the true-CFO sensitivity basis.
Cumulative operating cash flow is negative across FY22-26 despite positive
cumulative profit, working capital days widened by 52 in two years, and
defined free cash flow (now correctly computed for FY24-26 using the AR's
own "Purchase of Fixed Assets" line, per item 15) is negative in every
year with data.

## DECISION LINE

AVERAGE, unchanged from run 1's classification, but on a corrected and now
internally consistent scorecard: Core 52 (was 48), Moat 15 (was 10), Grand
Total 67 (was 58), moat class MODERATE (was THIN). The classification is
held at AVERAGE by two independent, still-binding deal-breakers (Block B
cash generation at 0/20; cumulative CFO/PAT at -0.478). Correcting the
EBIT basis (item 12) and the M4 tier read (item 13) materially strengthens
the return-on-capital and moat pictures — TLL clears more of this
scorecard on the rules as written than run 1 credited it for — but neither
correction touches the cash-generation floor, which is the finding that
actually caps the classification. The growth is real and fast by every P&L
measure available; the cash behind it has not shown up yet on the as-filed
basis, and on Stage 3's independent re-derivation (removing an undisclosed
cash-flow addback) it is worse than as-filed, not better. Nothing here
halts the pipeline — no mechanical failure occurred — but this run carries
that finding into every later stage as the load-bearing question LBF1
already named.
