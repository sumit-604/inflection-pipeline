# STAGE 1: GATE 0 SCORECARD — Entero Healthcare Solutions Ltd (ENTERO)
Run date: 2026-07-27 | Model: claude-sonnet-5 | Mode: pipeline

Data available: 7 years (FY20 to FY26, years ended 31-Mar). Scoring adapted
to 7-year history for P&L-based metrics. Balance-sheet sub-line detail
(current liabilities, trade payables) is available only for FY25 and FY26,
sourced from the FY26 audited results filing, which is the sole document in
this run's inputs that discloses a full current/non-current liability split.
Screener's own CSV balance sheet export carries only aggregate Total
Assets/Borrowings/Reserves rows, no current-liability or payables
breakdown, and its "Return on Capital Emp" / "Return on Equity" ratio rows
were blank in the provided export — so ROCE/ROE are computed here, not
sourced pre-built.

All figures in Rs crore unless stated. Consolidated basis throughout
(screener Data_Sheet annual P&L/BS/CF figures cross-checked and confirmed
consolidated: FY26 Sales 6,591.21 cr = consolidated revenue from operations
Rs 65,912.12 million on results p.11; FY26 PAT 115.04 cr = consolidated
profit attributable to owners Rs 1,150.42 million, same page; FY26 Total
Assets 3,600.26 cr = consolidated Rs 36,002.63 million, results p.14).

## SOURCE MAP
- (screener-data) = runs/entero-2026-07-27/inputs/screening/screener-Data_Sheet.csv
- (results FY26 audited, consol. P&L p.11) = .../results/5d6adb02-...pdf, page 11
- (results FY26 audited, consol. BS p.14) = .../results/5d6adb02-...pdf, page 14
- (results Q1 FY27, consol. P&L p.6) = .../results/80e84d9b-...pdf, page 6 (context/cross-check only, not a full FY, excluded from annual scoring)
- Balance_Sheet.csv, Cash_Flow.csv, Profit_Loss.csv, Quarters.csv, Customization.csv (screener secondary exports) = ratio rows blank / templates empty, no usable data beyond Data_Sheet.csv

## RAW EXTRACTS USED (all screener-data unless noted)
Sales (cr): FY20 1349.62, FY21 1773.10, FY22 2522.07, FY23 3300.21,
FY24 3922.31, FY25 5095.78, FY26 6591.21
PAT owners (cr): FY20 0.94, FY21 -15.54, FY22 -29.92, FY23 -11.56,
FY24 39.11, FY25 94.82, FY26 115.04
PBT (cr): FY20 3.87, FY21 -10.84, FY22 -19.81, FY23 -3.69, FY24 35.55,
FY25 138.74, FY26 179.34
Interest (cr): FY20 12.77, FY21 20.04, FY22 28.98, FY23 48.97, FY24 65.68,
FY25 41.62, FY26 54.39
Depreciation (cr): FY20 11.50, FY21 16.28, FY22 19.75, FY23 24.24,
FY24 25.02, FY25 30.69, FY26 43.29
EBIT = PBT + Interest, computed: FY20 16.64, FY21 9.20, FY22 9.17,
FY23 45.28, FY24 101.23, FY25 180.36, FY26 233.73
Total Assets (cr): FY20 748.97, FY21 835.64, FY22 1125.30, FY23 1308.05,
FY24 2344.95, FY25 2702.52, FY26 3600.26
Reserves+Capital, owners equity (cr): FY20 -16.03, FY21 -31.75,
FY22 -57.95, FY23 -68.59, FY24 1638.06, FY25 1724.15, FY26 1688.61
Borrowings (cr): FY20 602.80, FY21 720.05, FY22 973.62, FY23 1101.37,
FY24 337.98, FY25 385.23, FY26 677.15
Cash & Bank (cr): FY20 70.82, FY21 82.82, FY22 105.40, FY23 106.84,
FY24 893.18, FY25 260.42, FY26 161.79
Receivables (cr): FY20 231.80, FY21 242.59, FY22 374.60, FY23 514.88,
FY24 615.40, FY25 830.36, FY26 1212.44
Inventory (cr): FY20 194.55, FY21 243.93, FY22 310.16, FY23 341.63,
FY24 421.16, FY25 659.78, FY26 841.68
Raw Material Cost / COGS proxy (cr): FY20 1277.54, FY21 1686.57,
FY22 2342.47, FY23 3051.26, FY24 3627.81, FY25 4756.49, FY26 5914.84
CFO (cr): FY20 -36.52, FY21 -68.68, FY22 -35.27, FY23 -45.32, FY24 -36.61,
FY25 -76.87, FY26 96.20
Current Liabilities, consolidated (results FY26 audited, consol. BS p.14):
FY25 845.82 cr, FY26 1587.67 cr (no equivalent breakdown available for
FY20-FY24 in provided data)
Trade Payables, consolidated (results FY26 audited, consol. BS p.14):
FY25 397.30 cr, FY26 725.33 cr (no equivalent for FY20-FY24)

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

ROCE = EBIT ÷ (Total Assets − Current Liabilities), computed (screener
ratio row blank). Computable only for FY25-FY26 since Current Liabilities
is not disclosed for FY20-FY24 in any provided source.
- FY25: Capital Employed = 2702.52 − 845.82 = 1856.70; ROCE = 180.36 ÷
  1856.70 = 9.71% (results FY26 audited, consol. BS p.14 for CL; screener-data for EBIT inputs)
- FY26: Capital Employed = 3600.26 − 1587.67 = 2012.59; ROCE = 233.73 ÷
  2012.59 = 11.62% (same sourcing)

A1 Median ROCE (2 usable years: 9.71%, 11.62%) = 10.67% → band 10-14.9% = **1**
A2 Minimum single-year ROCE = 9.71% (FY25) → band 8-11.9% = **1**
A3 Median ROE: ROE = PAT ÷ avg Net Worth. FY20-FY23 net worth negative
(pre-IPO accumulated losses); ROE for those years is N/M (negative
denominator), not scored. FY24 average net worth spans a mid-year IPO
equity infusion (opening -68.59 cr to closing 1638.06 cr), which mechanically
distorts the average — flagged, not excluded, per formula.
  - FY24: avg NW = (-68.59+1638.06)/2 = 784.74; ROE = 39.11/784.74 = 4.98%
    (distorted by IPO infusion, see data_notes)
  - FY25: avg NW = (1638.06+1724.15)/2 = 1681.11; ROE = 94.82/1681.11 = 5.64%
  - FY26: avg NW = (1724.15+1688.61)/2 = 1706.38; ROE = 115.04/1706.38 = 6.74%
  Median (FY24-26) = 5.64% → band <12% = **0**
A4 ROCE trend, latest (FY26 11.62%) vs earliest usable (FY25 9.71%):
  latest ≥ earliest → **5**

**Block A = 1+1+0+5 = 7/20**

## BLOCK B: CASH GENERATION QUALITY (Max 20)

Cumulative CFO (FY20-FY26, screener-data) = -36.52-68.68-35.27-45.32-36.61
-76.87+96.20 = **-203.07 cr**
Cumulative PAT (same window) = 0.94-15.54-29.92-11.56+39.11+94.82+115.04
= **192.89 cr**

B1 Cumulative CFO ÷ Cumulative PAT = -203.07 ÷ 192.89 = **-1.05** (negative
ratio: six of seven years show CFO burn even while cumulative PAT is
positive) → band <0.50 = **0**
B2 FCF-positive years proportion: FCF = CFO − Capex (PPE+intangibles
purchases, ex-acquisitions). NOT computable — screener's Cash_Flow.csv
export gives only net CFO/CFI/CFF totals, no capex line; the only capex
line item in the provided PDFs is in the FY26 filing's STANDALONE cash
flow statement (Rs 155.34mn FY26, Rs 19.79mn FY25), a different
consolidation basis than the consolidated CFO used above, and not
disclosed for FY20-24 at all. Marked N/A (not in provided data) → **0**
B3 Cumulative FCF ÷ Cumulative PAT: same gap as B2 → N/A → **0**
B4 Change in WC Days, latest vs earliest **computable** year:
  WC Days = Receivable Days + Inventory Days − Payable Days. Inventory
  and Payable Days computed on COGS (Raw Material Cost) basis, stated —
  Raw Material Cost is Entero's cost of goods purchased for resale, the
  applicable COGS proxy for a pure distributor.
  - FY25: Recv Days 830.36/5095.78*365=59.46; Inv Days 659.78/4756.49*365
    =50.63; Pay Days 397.30/4756.49*365=30.49; WC Days = 79.60
  - FY26: Recv Days 1212.44/6591.21*365=67.16; Inv Days 841.68/5914.84*365
    =51.94; Pay Days 725.33/5914.84*365=44.76; WC Days = 74.34
  Change = -5.26 days (decrease). LOW CONFIDENCE flag: this is a 2-year
  window only (payables not disclosed pre-FY25), and the result sits right
  at the 5-day scoring threshold — a small revision to the OCR-read payables
  figures could move this to the ±5-day band. Scored as computed:
  decrease >5 days → **5**

**Block B = 0+0+0+5 = 5/20**

block_b_trend: **improving** — FY26 CFO turned positive at Rs 96.2 cr,
the first positive year after six straight years of negative CFO
(FY20 -36.5, FY21 -68.7, FY22 -35.3, FY23 -45.3, FY24 -36.6, FY25 -76.9,
all screener-data). Cumulative CFO over the 7-year window is still -203.07
cr against cumulative PAT of +192.89 cr. This matches the qualitative
context (India Ratings rationale, per B00 propagation, not itself a
DATA_SOURCE for this stage): negative free cash flow since inception,
management guiding FCF-positive from end-FY26. One year of positive CFO
does not resolve six years of cash burn; FLAG-CASH raised below.

## BLOCK C: GROWTH (Max 20)

C1 Revenue CAGR, FY20→FY26 (6 years): (6591.21/1349.62)^(1/6)-1 = 30.27%
→ band ≥20% = **5**
C2 PAT CAGR: PAT swung from profit (FY20 +0.94) to losses (FY21-FY23) and
back to profit (FY24 onward) within the window — loss-to-profit swing,
FY21 to FY24. Per CAGR edge rule, no synthetic CAGR attempted → **N/M, 0**
C3 Positive YoY revenue years: 6 of 6 YoY comparisons positive (FY20→FY26,
screener-data) = 100% → **5**
C4 PAT CAGR minus Revenue CAGR: PAT CAGR is N/M → **0** (per rule)

**Block C = 5+0+5+0 = 10/20**

data_notes: loss-to-profit swing, FY21 to FY24 (net losses FY21 -15.54,
FY22 -29.92, FY23 -11.56; return to profit FY24 +39.11), screener-data.

## BLOCK D: BALANCE SHEET STRENGTH (Max 20)

D1 Net Debt ÷ EBITDA (FY26, latest): Net Debt = Borrowings 677.15 − Cash
161.79 = 515.36 cr (screener-data). EBITDA = EBIT 233.73 + Depreciation
43.29 = 277.02 cr. Ratio = 1.86x → band 1-2x = **3**
D2 Interest Coverage, EBIT ÷ Interest (FY26): 233.73 ÷ 54.39 = 4.30x →
band 3-4.9x = **2**
D3 Debt ÷ Equity (FY26): Borrowings 677.15 ÷ owners equity 1688.61 = 0.401
→ band 0.1-0.5 = **4**
D4 Current Ratio (FY26): Current Assets 2508.44 cr (results FY26 audited,
consol. BS p.14, Rs 25,084.36mn) ÷ Current Liabilities 1587.67 cr = 1.58x
→ band 1.5-1.99 = **4**

**Block D = 3+2+4+4 = 13/20**

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

No shareholding-pattern data (promoter holding, pledge) is present in any
provided source (screener CSVs and results PDFs do not carry shareholding
disclosures; this matches the propagated B00 input_gap: shareholding,
MEDIUM). No contingent-liability note was present in the results extracts
reviewed (notes sections cover ESOP, OCDs, acquisitions, and Ind AS 108
segment reporting only — no contingent liability disclosure).

E1 Promoter holding (latest quarter): **N/A (not in provided data) → 0**
E2 Promoter holding change, 3 years: **N/A (not in provided data) → 0**
E3 Promoter pledge (latest): **N/A (not in provided data) → 0**
E4 Contingent Liabilities ÷ Net Worth (latest): **N/A (not in provided data) → 0**

**Block E = 0/20** — entirely a data-absence result, not an evidenced
shareholder-alignment failure. Flagged for Halt 1 corpus-gap resolution.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

Operating EBITDA (excl. Other Income) computed for margin trend, using
Sales − (Raw Material Cost − Change in Inventory + Power&Fuel + Other
Mfr Exp + Employee Cost + Selling&Admin + Other Expenses), screener-data.
FY26 sub-lines for Power/OtherMfr/Selling were blank in the export;
algebraic cross-check against PBT+Interest+Depreciation confirms these
were folded into the FY26 "Other Expenses" line (168.92 cr), noted below.
EBITDA margin (excl other income): FY20 1.74%, FY21 0.84%, FY22 0.97%,
FY23 1.94%, FY24 2.85%, FY25 3.37%, FY26 4.04%.

M1 Pricing Power: margin expanded +2.30pp (FY20 1.74% → FY26 4.04%) AND
revenue CAGR 30.27% ≥10% → **5**
M2 Cost Advantage vs peer median EBITDA margin: no peer data provided →
**PEER DATA NEEDED, 0**
M3 Capital Efficiency: FAT (FY26) = Sales 6591.21 ÷ Net Block 960.49 =
6.86x (>3x) but ROCE FY26 = 11.62% (<12%, fails even the lowest band) →
**0**
M4 Customer Stickiness: zero revenue-decline years (FY20-26) AND
receivable days FY20 62.68 → FY26 67.16, change +4.48 days, within ±10 →
**5**
M5 Scale & Dominance: needs peer mcap/margin ranking, not provided →
**PEER DATA NEEDED, 0**
M6 Technology/R&D: no R&D line disclosed; distribution business, not an
R&D-driven archetype → **0**
M7 Regulatory/License: pharma distribution is a licensed activity, but
count of listed peers in the segment is not in provided data →
**PEER DATA NEEDED, 0**
M8 Distribution: reach (depot/town count) not quantified in any provided
source → **N/A (not in provided data), 0**
M9 Brand: GM proxy needs peer median, not provided → **PEER DATA NEEDED, 0**
M10 Switching Costs: revenue grew every year AND receivable days rose only
4.48 days over the period (≤10) → **5**
M11 Network Effects (7 years available, meets the ≥6yr threshold):
latest 3yr revenue CAGR (FY23→FY26) = 25.94%, prior 3yr CAGR (FY20→FY23)
= 34.74% — latest is LOWER than prior (decelerating, not the top tier).
Latest 3yr CAGR ≥20%; selling-expense % of revenue FY23 1.67%, FY24 1.71%,
FY25 1.72% — roughly stable (FY26 not separable, sub-line folded into
Other Expenses, see note). Scored on the ≥20% + stable tier → **3**
M12 Negative WC / Float: WC Days FY25 79.60, FY26 74.34, both >45 in the
only two years computable → **0**

**Moat score = 5+0+0+5+0+0+0+0+0+5+3+0 = 18/60**

Moats present (score ≥3): M1, M4, M10, M11 = **4 moats confirmed**
Moat classification: 4-5 present = **STRONG**

Moat profile bar:
```
M1  [#####] 5  Pricing Power        (present)
M2  [     ] 0  Cost Advantage       PEER DATA NEEDED
M3  [     ] 0  Capital Efficiency
M4  [#####] 5  Customer Stickiness  (present)
M5  [     ] 0  Scale & Dominance    PEER DATA NEEDED
M6  [     ] 0  Technology/R&D
M7  [     ] 0  Regulatory/License   PEER DATA NEEDED
M8  [     ] 0  Distribution         N/A (not in provided data)
M9  [     ] 0  Brand                PEER DATA NEEDED
M10 [#####] 5  Switching Costs      (present)
M11 [###  ] 3  Network Effects      (present)
M12 [     ] 0  Negative WC/Float
```

---

## CLASSIFICATION AND OVERRIDES

Data confidence: 7 years of P&L history (FY20-FY26) → **moderate**
confidence band (7-9 years), no automatic downgrade from the years-count
rule. Note, separately, that several sub-metrics (ROCE, WC Days, all of
Block E, 4 of 12 moat tests) have far thinner effective coverage (2 years
or zero years) due to source gaps, not a full-cycle data limitation — this
is called out per-metric above rather than folded into the global
data-confidence tier.

Core score (Blocks A+B+C+D+E) = 7+5+10+13+0 = **35/100**
Moat score = **18/60**
Grand total = 35+18 = **53/100**

Classification matrix: Core <40 = **AVOID** (Core 35 falls in this band,
overriding all other combinations regardless of moat class).

Deal-breaker overrides triggered (recorded; already consistent with, and
non-binding relative to, the Core<40 AVOID floor):
1. Block A (7) <8 → max GOOD (Block A driven by thin ROCE/ROE, computable
   only FY25-FY26)
2. Block B (5) <8 → max GOOD (cash-conversion driven, see B1/B4 above)
4. Cumulative CFO ÷ PAT (-1.05) <0.50 → max AVERAGE (six of seven years
   of negative CFO despite cumulative positive PAT)
Not triggered: #3 (median ROCE 10.67% ≥10%, narrowly clears); #7 (no
revenue decline years); #8 (PAT positive in all of last 3 years);
#9 (7 years of history, not <3).

history_downgrade: **false** (top-line data-years count does not trigger
the downgrade rule; per-metric gaps are flagged individually instead).

**Strongest block: D — Balance Sheet Strength, 13/20 (65%).**
**Weakest block (data-driven): E — Shareholder Alignment, 0/20, entirely
due to absent shareholding-pattern data, not an evidenced failure.**
**Weakest block (evidence-driven): B — Cash Generation Quality, 5/20,
a genuine deal-breaker on cumulative CFO/PAT.**

### DECISION LINE
Classification: **AVOID**. Core score 35/100 sits below the 40 threshold,
driven jointly by thin return metrics (Block A 7/20), a real cumulative
cash-conversion deal-breaker (Block B 5/20, cumulative CFO/PAT = -1.05),
and a complete data absence in Block E (0/20, no shareholding data
provided). Moat profile is STRONG (4 of 12 tests present: pricing power,
customer stickiness, switching costs, network effects), which the
classification matrix does not let outweigh a sub-40 Core score. Growth
(Block C, revenue CAGR 30.27%, 100% positive YoY years) is the strongest
top-line signal but is not scored highly here because PAT CAGR is
N/M (loss-to-profit swing) under the formula's edge rule.

---

## FLAGS

- **FLAG-GATE0**: Classification AVOID (≤AVERAGE threshold). Historical
  depressors identified: (a) genuine — cumulative CFO/PAT of -1.05 across
  FY20-FY26, six of seven years cash-burn negative CFO despite cumulative
  positive PAT; ROCE computable only FY25-FY26 (9.71%, 11.62%), both
  sub-15%; (b) data-absence driven — Block E scored 0/20 for total lack of
  shareholding data; 4 of 12 moat tests scored 0 for lack of peer data
  (M2, M5, M7, M9); ROCE/WC-Days trend limited to a 2-year window because
  current-liability and trade-payables detail is disclosed only in the
  FY26 annual results filing, not for FY20-FY24. Downstream stages should
  treat AVOID as provisional pending Halt-1 corpus-gap resolution
  (shareholding pattern, consolidated cash flow statement with capex
  detail, pre-FY25 balance sheet current-liability breakdown), not as a
  final verdict on company quality.
- **FLAG-CASH**: Cumulative CFO ÷ Cumulative PAT = -1.05 (deal-breaker
  #4). FY26 is the first positive-CFO year (Rs 96.2 cr) after six
  consecutive years of negative CFO. Matches the propagated B00 context
  (India Ratings rationale: negative FCF since inception, management
  guiding FCF-positive from end-FY26). FCF itself (B2/B3) could not be
  computed — no per-year capex line available at the consolidated level
  in any provided source. Per CLAUDE.md, cash-conversion evidence here is
  INDETERMINATE for the FCF metrics specifically (not merely low); this
  caps any downstream verdict at PROCEED WITH CAVEATS with the missing
  capex/consolidated-cash-flow evidence named, independent of what this
  stage's mechanical classification says.

---

## ANALYST NOTE

AVOID here is roughly half data-gap, half genuine weakness. Genuine:
cumulative operating cash flow is negative across FY20-FY26 (-203 cr) even
though cumulative PAT is positive (+193 cr); FY26 is the first cash-flow
positive year. ROCE, computable only for FY25-FY26, sits at 9.7% and
11.6%, both below a durable-quality bar. Growth is real: 30% revenue CAGR,
100% positive YoY years, and margin has expanded 2.3pp since FY20,
consistent with a scaling distribution roll-up. Data-gap driven: Block E
(shareholder alignment) is 0/20 purely because no shareholding pattern was
in any provided file; 4 of 12 moat tests need peer data not supplied;
ROCE/working-capital trend rests on only 2 usable years because
current-liability and payables detail exists only in the FY26 annual
filing. Treat the AVOID score as provisional. The near-term evidence
priority for Halt 1 is shareholding pattern, the consolidated cash flow
statement (for capex/FCF), and FY20-24 balance sheet current-liability
detail — resolving these could move Blocks A, B, and E materially, in
either direction.

```yaml
stage: B01-gate0
company: "ENTERO"
run_date: "2026-07-27"
model: claude-sonnet-5
status: complete
input_gaps: ["prospectus (HIGH)", "announcements (MEDIUM)", "shareholding (MEDIUM)", "research (LOW)"]
flags:
  - {type: FLAG-GATE0, reason: "Classification AVOID, Core 35/100 <40. Mixed genuine (cumulative CFO/PAT -1.05, ROCE 9.7-11.6% FY25-26) and data-absence depressors (Block E 0/20 no shareholding data, 4/12 moat tests PEER DATA NEEDED, ROCE/WC-Days limited to 2-year window). Treat as provisional pending Halt 1 corpus-gap resolution."}
  - {type: FLAG-CASH, reason: "Cumulative CFO/PAT = -1.05 across FY20-FY26; six of seven years CFO-negative; FY26 first positive CFO year (Rs 96.2cr). FCF itself not computable, no per-year consolidated capex data in any provided source. Cash conversion is INDETERMINATE for FCF specifically; caps downstream verdict at PROCEED WITH CAVEATS per CLAUDE.md until capex/consolidated CF statement evidence is supplied."}
data_years: 7
fy_range: "FY20 to FY26"
blocks: {A: 7, B: 5, C: 10, D: 13, E: 0}
core_score: 35
moat_score: 18
grand_total: 53
moats_confirmed: 4
moat_class: "STRONG"
classification: "AVOID"
deal_breakers:
  - "1: Block A (7) <8 -> max GOOD"
  - "2: Block B (5) <8 -> max GOOD"
  - "4: cumulative CFO/PAT (-1.05) <0.50 -> max AVERAGE"
history_downgrade: false
data_notes:
  - "loss-to-profit swing, FY21 to FY24 (losses FY21-FY23, return to profit FY24); no synthetic PAT CAGR attempted (C2, C4 = N/M, scored 0)"
  - "ROE FY24 uses average net worth spanning a mid-year IPO equity infusion (opening -68.59cr to closing 1638.06cr); mechanically computed per formula but flagged as distorted"
  - "Inventory Days and Payable Days computed on COGS basis (Raw Material Cost used as COGS proxy for a distributor); Receivable Days on Revenue basis per formula"
  - "PEER DATA NEEDED: M2 (cost advantage), M5 (scale & dominance), M7 (regulatory/license player count), M9 (brand) - no peer figures in provided sources"
  - "ROCE and full Working Capital Days computable only for FY25-FY26; current liabilities and trade payables not disclosed for FY20-FY24 in any provided source (screener CSV lacks the breakdown; only the FY26 annual audited results PDF shows both years' current-liability/payables detail)"
  - "FCF (B2, B3) not computable: screener Cash_Flow.csv gives only net CFO/CFI/CFF with no capex line; PDFs disclose only STANDALONE capex (FY25-FY26), a different consolidation basis than the consolidated CFO figures used, so not substituted"
  - "FY26 P&L sub-lines Power and Fuel, Other Mfr Exp, and Selling and admin are blank in screener-data; algebraic cross-check against PBT+Interest+Depreciation confirms they are folded into the FY26 Other Expenses line (168.92cr); limits M11 selling-expense-ratio trend to FY23-FY25"
  - "B4 WC-Days change (-5.26 days) sits right at the 5-day scoring threshold on a 2-year window only; low confidence, small revision to OCR-read payables figures could shift the band"
block_b_trend: "improving - FY26 CFO turned positive at Rs 96.2cr, first positive year after six consecutive negative-CFO years (FY20 -36.5cr through FY25 -76.9cr); cumulative CFO still -203.07cr vs cumulative PAT +192.89cr over FY20-FY26"
analyst_note: "AVOID is roughly half data-gap, half genuine weakness. Genuine: cumulative CFO negative across FY20-26 (-203cr) despite positive cumulative PAT (+193cr); ROCE 9.7-11.6% (FY25-26 only, sub-15%). Growth is real: 30% revenue CAGR, 100% positive YoY years, margin +2.3pp since FY20. Data-gap driven: Block E is 0/20 purely from no shareholding data anywhere in provided files; 4 of 12 moat tests need unsupplied peer data; ROCE/WC-Days trend rests on 2 usable years since current-liability/payables detail exists only in the FY26 annual filing. Treat AVOID as provisional. Priority for Halt 1: shareholding pattern, consolidated cash flow statement with capex detail, FY20-24 balance-sheet current-liability breakdown."
```
