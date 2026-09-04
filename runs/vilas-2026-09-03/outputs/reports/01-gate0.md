# STAGE 1: GATE 0 SCORECARD — Vilas Transcore Ltd (VILAS)

Run date: 2026-09-03
Classification (archetype): CONVERTER, Section 1B v3.7 Amendment 17 (CRGO
electrical-steel lamination converter; sector row "Pharma/CDMO" in the
manifest is a collector error, ignored).
Data sources: screener-Data_Sheet.csv (7-yr P&L/BS/CF, FY20-FY26),
_sidecar_FY26_audited_results.txt (audited FY26 results, filed
2026-05-11: standalone balance sheet at 31-Mar-2026 / 31-Mar-2025 /
1-Apr-2024, FY25/FY26 P&L, FY25/FY26 cash flow — amounts in Rs Lacs in
source, converted /100 to Rs Cr here), shareholding-pattern-operator-ferried.md
(screener-tier, operator-ferried).

RE-RUN NOTE: first attempt could not open the 16.7 MB FY26 results PDF and
scored a DATA-GAP AVOID. That access failure is fixed; this is a clean
full scorecard on the readable inputs listed above.

Data available: 7 years (FY20 to FY26). Scoring adapted to 7-year history.

---

## BASIS NOTE (read before the blocks)

Two capital-employed bases are used across the 7-year window because the
current-liability split is available on an exact basis for only 3 of the
7 years:

- FY24, FY25, FY26: EXACT basis. Capital Employed = Total Assets − Total
  Current Liabilities, both lines taken from the audited standalone
  balance sheet in the sidecar, which gives all three dates (31-Mar-2026,
  31-Mar-2025, 1-Apr-2024 = FY24 close) (results FY26 audited, p.6).
  Trade Payables on this basis = MSME dues + non-MSME creditor dues, both
  lines in the sidecar (results FY26 audited, p.6).
- FY20-FY23: screener bundles the current/non-current split into a single
  "Other Liabilities" line, so the exact split is not in corpus. Capital
  Employed = Net Worth (Equity Share Capital + Reserves) + Borrowings
  (screener-data), stated per year as "capital-employed = NW + borrowings
  basis, CL split unavailable."

EBIT = Profit before tax + Interest, per year, per the fixed formula. For
FY24 (screener P&L only; sidecar has no FY24 P&L) and FY20-23, EBIT uses
screener-data. For FY25 and FY26, EBIT uses the sidecar's own audited
P&L line items (PBT, Finance Costs) so the ROCE numerator sits on the
same restated basis as the exact-basis denominator (results FY26
audited, p.7).

Screener's own ROCE field is blank; all ROCE figures below are computed.

---

## BLOCK A: RETURN ON CAPITAL (Max 20)

| Year | Basis | EBIT (Cr) | Capital Employed (Cr) | ROCE |
|---|---|---|---|---|
| FY20 | NW+Borrowings | 6.06 (screener-data: PBT 3.64+Int 2.42) | 103.46 (screener-data: NW 95.76+Borrow 7.70) | 5.86% |
| FY21 | NW+Borrowings | 8.68 (screener-data: PBT 7.05+Int 1.63) | 107.87 (screener-data: NW 100.29+Borrow 7.58) | 8.05% |
| FY22 | NW+Borrowings | 26.61 (screener-data: PBT 24.05+Int 2.56) | 120.98 (screener-data: NW 117.51+Borrow 3.47) | 22.00% |
| FY23 | NW+Borrowings | 29.22 (screener-data: PBT 27.26+Int 1.96) | 141.87 (screener-data: NW 136.98+Borrow 4.89) | 20.60% |
| FY24 | EXACT (TA−CL) | 32.32 (screener-data: PBT 30.76+Int 1.56) | 162.93 (results FY26 audited, p.6: TA 195.68−CL 32.75, as at 1-Apr-2024) | 19.84% |
| FY25 | EXACT (TA−CL) | 51.01 (results FY26 audited, p.7: PBT 49.51+FinCost 1.50) | 292.00 (results FY26 audited, p.6: TA 350.28−CL 58.27) | 17.47% |
| FY26 | EXACT (TA−CL) | 53.78 (results FY26 audited, p.7: PBT 51.66+FinCost 2.12) | 331.43 (results FY26 audited, p.6: TA 406.47−CL 75.05) | 16.23% |

A1 Median ROCE (7 values, sorted 5.86/8.05/16.23/17.47/19.84/20.60/22.00) =
**17.47%** → band 15-19.9% → **score 3**

A2 Minimum single-year ROCE = **5.86%** (FY20, NW+borrowings basis) →
<8% → **score 0**

A3 Median ROE (PAT ÷ avg NW; FY20 earliest year uses closing NW only,
screener-data throughout): FY20 3.76%, FY21 5.34%, FY22 16.45%, FY23
15.88%, FY24 15.58%, FY25 15.27%, FY26 12.83%. Median = **15.27%** →
band 15-19.9% → **score 4**

A4 ROCE trend, latest (FY26 16.23%) vs earliest (FY20 5.86%): latest ≥
earliest → **score 5**

**Block A total = 3+0+4+5 = 12/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20)

Cumulative CFO (FY20-26, screener-data): 21.69+19.76+12.91+13.19+49.16
+(-35.46)+(-1.70) = **79.55 Cr**
Cumulative PAT (FY20-26, screener-data): 3.60+5.23+17.91+20.21+23.08
+34.17+39.56 = **143.76 Cr**

B1 Cumulative CFO ÷ Cumulative PAT = 79.55/143.76 = **0.553** → band
0.50-0.69 → **score 1**

Capex: FY25/FY26 exact from sidecar cash flow statement, "Purchase of
Property, Plant and Equipments": FY26 = 39.15 Cr, FY25 = 38.47 Cr
(results FY26 audited, p.8). FY20-24: screener does not break out capex
from other investing items, so total Cash from Investing Activity is
used as a proxy (data_notes: proxy, not a breakdown).

FCF = CFO − Capex: FY20 21.16, FY21 19.27, FY22 11.09, FY23 2.55, FY24
39.17, FY25 −73.93, FY26 −40.85 (all Cr).

B2 FCF-positive years = 5 of 7 (FY20-24 positive, FY25-26 negative) =
**71.4%** → band 50-74% → **score 2**

Cumulative FCF = 21.16+19.27+11.09+2.55+39.17−73.93−40.85 = **−21.55 Cr**

B3 Cumulative FCF ÷ Cumulative PAT = −21.55/143.76 = **−0.15** →
negative → **score 0**

B4 Change in WC Days: full 3-component WC days (Receivable + Inventory −
Payable, revenue basis) is computable exactly only for FY24-26, since
Trade Payables is not broken out in screener for FY20-23 (see basis
note). Comparison uses FY24 (earliest exact-basis year) vs FY26 (latest):
- FY24: Receivable days 45.88 + Inventory days 30.38 − Payable days 34.88
  = **41.38 days** (payable days from results FY26 audited p.6, 1-Apr-2024
  column)
- FY26: Receivable days 61.41 + Inventory days 57.31 − Payable days 22.25
  = **96.47 days** (payable days from results FY26 audited p.6,
  31-Mar-2026 column)

Change = +55.1 days → increased >15 → **score 0**

**Block B total = 1+2+0+0 = 3/20**

block_b_trend: **DETERIORATING**. Cumulative CFO/PAT of 0.55x is dragged
down entirely by CFO turning negative: −35.46 Cr FY25 and −1.70 Cr FY26
(screener-data), even as PAT rose from 23.08 Cr (FY24) to 39.56 Cr
(FY26) (screener-data). Note: the sidecar's own audited (Ind AS 101
restated, transition date 1-Apr-2024) cash flow statement shows FY25
Net Cash from Operating Activities as −41.53 Cr (results FY26 audited,
p.8), a restatement gap of ~6 Cr against the screener figure; screener
is used as the 7-year trend anchor, sidecar flagged as the freshly
restated audited version.

Read on growth-induced vs structural: the evidence points to
GROWTH-INDUCED, not structural. CWIP was 37.94 Cr in FY25 (screener-data;
37.67 Cr per sidecar p.6) as Unit-3 capacity build was underway; Net
Block jumped from 32.28 Cr (FY25) to 81.79 Cr (FY26, screener-data) as
Unit-3 capitalised. Receivables rose from 38.93 Cr (FY24) to 77.50 Cr
(FY26) and inventory from 25.78 Cr to 72.33 Cr over the same two years
(screener-data), both scaling with the volume ramp (FY26 CRGO output
19,856 MT vs 36,000 MTPA target = 55% utilisation, operator anchor,
still ramping). The ramp was funded externally, not from operations: FY25
Cash from Financing Activities was +105.12 Cr (screener-data), including
IPO proceeds of Rs 95.26 Cr (results FY26 audited, p.11); FY26 CFF was
+26.09 Cr on incremental short-term borrowings of 38.96 Cr (screener-data,
sidecar p.6). A secondary, separable concern: trade payables fell from
38.12 Cr (FY25) to 28.08 Cr (FY26, results FY26 audited p.6) even as
receivables and inventory kept rising, which is a WC-efficiency
deterioration, not merely a scale effect. This is not yet confirmed
structural; it needs a post-ramp (FY27) check on whether WC days
normalise as Unit-3 utilisation climbs toward the 36,000 MTPA target.

---

## BLOCK C: GROWTH (Max 20)

Revenue CAGR FY20→FY26 (6-yr): (460.67/161.91)^(1/6)−1 = **19.03%**
(screener-data) → band 15-19.9% → **C1 score 4**

PAT CAGR FY20→FY26 (6-yr): (39.56/3.60)^(1/6)−1 = **49.12%**
(screener-data) → ≥20% → **C2 score 5**

C3 Positive YoY revenue years: 5 of 6 transitions positive (FY21 vs FY20
declined 161.91→132.65, screener-data; FY22-26 all grew) = **83.3%** →
band 75-99% → **score 3**

C4 PAT CAGR − Revenue CAGR = 49.12% − 19.03% = **+30.09pp** → ≥+3pp →
**score 5**

**Block C total = 4+5+3+5 = 17/20**

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20, latest = FY26)

D1 Net Debt ÷ EBITDA: Borrowings 38.96 Cr − Cash & Bank 94.36 Cr =
**Net Cash of 55.40 Cr** (screener-data) → net cash → **score 5**

EBITDA FY26 = PBT + Interest + Depreciation − Other Income (computed,
screener-data) = 51.65+2.12+4.29−6.60 = **51.46 Cr**, margin 11.17% of
Sales 460.67 Cr — matches the operator anchor of Rs 51.5 Cr / 11.17%
exactly.

D2 Interest Coverage EBIT ÷ Interest = 53.77 ÷ 2.12 = **25.4x**
(screener-data) → ≥10x → **score 5**

D3 Debt ÷ Equity = Borrowings 38.96 ÷ Net Worth 328.53 = **0.119**
(screener-data) → band 0.1-0.5 → **score 4**

D4 Current Ratio = Current Assets 287.51 Cr ÷ Current Liabilities 75.05
Cr = **3.83x** (results FY26 audited, p.6, exact basis) → ≥2.0 →
**score 5**

**Block D total = 5+5+4+5 = 19/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20)

E1 Promoter holding (latest, Mar-2026) = **73.14%**
(shareholding-pattern-operator-ferried.md) → ≥60% → **score 5**

E2 Promoter holding change: 73.17% (May-2024, IPO-listing quarter) →
73.14% (Mar-2026) = **−0.03pp**. Note: company listed May-2024, so only
~2 years of post-listing holding history exist, short of the full 3-year
window the metric assumes; this is stated, not papered over. → within
±1% → **score 3**

E3 Promoter pledge (latest) = **N/A (not in provided data)**. The
aggregator shareholding table carries no pledge column
(shareholding-pattern-operator-ferried.md); the primary SHP filing was
not pushed to inputs/shareholding/. → **score 0**

E4 Contingent Liabilities ÷ Net Worth (latest) = **N/A (not in provided
data)**. Neither screener-Data_Sheet.csv nor the FY26 results sidecar
(a results extract, not full AR notes) carries a contingent-liabilities
note. → **score 0**

**Block E total = 5+3+0+0 = 8/20**

---

## CORE SCORE

Block A 12 + Block B 3 + Block C 17 + Block D 19 + Block E 8 =
**Core score = 59/100**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60)

EBITDA margin series (computed, screener-data, PBT+Interest+Dep−Other
Income basis): FY20 4.42%, FY21 6.65%, FY22 11.47%, FY23 10.37%, FY24
9.81%, FY25 12.62%, FY26 11.17%.

**M1 Pricing Power**: margin expanded FY20→FY26 by +6.75pp (≥2pp) AND
revenue CAGR 19.03% (≥10%) → **score 5**

**M2 Cost Advantage vs peer median**: PEER DATA NEEDED (no peer set in
corpus) → **score 0**

**M3 Capital Efficiency**: FAT = Revenue 460.67 ÷ (Net Block 81.79 +
CWIP 23.35) = 460.67/105.14 = **4.38x** (screener-data); ROCE FY26 =
16.23% (exact basis, computed above). FAT>3x AND ROCE>20% fails (ROCE
not >20%); FAT>2x AND ROCE>15% holds → **score 3**

**M4 Customer Stickiness**: 1 revenue-decline year (FY21, COVID),
recovered strongly FY22 onward (screener-data); receivable days NOT
stable ±10 across the period (range 34.66-117.35 days) → "1 decline
year, fully recovered" tier → **score 3**

**M5 Scale & Dominance**: PEER DATA NEEDED (no mcap/segment peer set) →
**score 0**

**M6 Technology/R&D**: R&D spend not disclosed/not broken out in
screener-data or the sidecar → **score 0**

**M7 Regulatory/License**: number of listed players in the CRGO
lamination-converter segment not quantified in provided data → PEER DATA
NEEDED → **score 0**

**M8 Distribution**: dealer/distributor network reach not quantified in
provided data → **score 0**

**M9 Brand**: gross-margin-vs-peer-median comparison needs peer data,
not provided → PEER DATA NEEDED → **score 0**

**M10 Switching Costs**: revenue grew all years but 1 (FY21 decline);
receivable days moved from 106.72 (FY20) to 61.41 (FY26, screener-data),
a net decrease, though with high intra-period volatility (34.66-117.35
days) → "growth all but 1 year AND stable" tier → **score 3**

**M11 Network Effects** (7 years available, ≥6-year test applies):
latest-3yr revenue CAGR (FY23→FY26) = (460.67/282.61)^(1/3)−1 = 17.69%;
prior-3yr CAGR (FY20→FY23) = (282.61/161.91)^(1/3)−1 = 20.41%. Latest is
NOT greater than prior → tier 1 fails. Overall CAGR 19.03% is just under
the ≥20% tier-2 threshold, and Selling & Admin expense as % of revenue
rose from 1.06% (FY20) to 1.35% (FY25, screener-data; FY26 not disclosed
in screener) → tier-2 fails (selling% rising, not stable/declining) →
"growth >15% but selling% rising" tier → **score 1**

**M12 Negative WC/Float**: WC days are positive and rising, not
negative, in every exact-basis year (41.38 FY24, 94.30 FY25, 96.47 FY26,
computed above) → >45 days → **score 0**

**Moat score = 5+0+3+3+0+0+0+0+0+3+1+0 = 15/60**

Moats present (score ≥3): M1, M3, M4, M10 = **4 moats confirmed**

**Moat classification: 4-5 present = STRONG**

Moat profile:
```
M1  Pricing Power        [#####] 5  PRESENT
M2  Cost Advantage       [.....] 0  PEER DATA NEEDED
M3  Capital Efficiency   [###..] 3  PRESENT
M4  Customer Stickiness  [###..] 3  PRESENT
M5  Scale & Dominance    [.....] 0  PEER DATA NEEDED
M6  Technology/R&D       [.....] 0  not disclosed
M7  Regulatory/License   [.....] 0  PEER DATA NEEDED
M8  Distribution         [.....] 0  not disclosed
M9  Brand                [.....] 0  PEER DATA NEEDED
M10 Switching Costs      [###..] 3  PRESENT
M11 Network Effects      [#....] 1  below threshold
M12 Negative WC/Float    [.....] 0  WC days rising, positive
```

---

## DATA CONFIDENCE

7 years of data (FY20-FY26) → **7-9 years = moderate confidence**. One
clear trough year in the window (FY21, COVID-linked revenue decline)
gives partial, not full, cycle visibility. No history-based downgrade
triggered (that applies only below 5 years). `history_downgrade: false`.

---

## GRAND TOTAL AND CLASSIFICATION

Core score = 59/100
Moat score = 15/60
**Grand total = 74** (59 + 15)
Moat class = STRONG (4 moats confirmed)

Classification matrix: Core 59 falls in the "Core 40-59" band, which maps
to **AVERAGE** regardless of moat class (the moat-class overlay only
applies at Core ≥60).

**Classification = AVERAGE**

### Deal-breaker override check
1. Block A <8 → max GOOD: Block A = 12, not triggered.
2. Block B <8 → max GOOD: Block B = 3, **TRIGGERED**. Non-binding here
   since AVERAGE already sits below the GOOD cap.
3. Median ROCE <10% → max AVERAGE: median 17.47%, not triggered.
4. Cumulative CFO/PAT <0.50 → max AVERAGE: 0.553, not triggered (close
   to the line).
5. Pledge >15% → max AVERAGE: pledge is N/A/not disclosed, cannot
   confirm a breach; not triggered on available evidence, but this is an
   open item, not a clean pass.
6. ND/EBITDA >3x AND IC <3x → AVOID: net cash position, IC 25.4x, not
   triggered.
7. Revenue declined in majority of years → max AVERAGE: 1 of 6 years,
   not triggered.
8. PAT negative in any of last 3 years → max AVERAGE: FY24/25/26 all
   positive, not triggered.
9. History <3 years → AVERAGE: 7 years, not triggered.

Deal-breaker 2 (Block B <8) is recorded and named which years drive it:
FY25 and FY26, where CFO went negative against rising PAT, both years
tied to the Unit-3 capex/WC ramp described above.

---

## STRONGEST / WEAKEST BLOCK

- Strongest: **Block D (Balance Sheet Strength), 19/20** — net cash
  position, 25.4x interest coverage, 3.83x current ratio, D/E 0.12x.
- Weakest: **Block B (Cash Generation Quality), 3/20** — cumulative
  CFO/PAT of 0.55x, CFO negative in FY25 and FY26, WC days up 55 days
  FY24→FY26. This is the single largest depressor on the classification
  and is read as growth-induced (Unit-3 ramp) rather than structural, per
  the block_b_trend analysis above, but it is unresolved evidence, not a
  clean pass.

---

## DECISION LINE

Gate 0 classification: **AVERAGE** (Core 59/100, Moat STRONG/15/60,
Grand total 74). No mechanical deal-breaker forces AVOID or a hard cap
below AVERAGE; Block B's cash-conversion weakness is the primary
depressor and is flagged forward as FLAG-CASH, with the growth-induced
read stated and the open item (does WC normalise post-ramp) named for
later-stage verification. Per pipeline rules this Gate 0 outcome does
not halt the run; it carries forward as evidence for stage 11 and the
verdict.

---

```yaml
stage: B01-gate0
company: "VILAS"
run_date: "2026-09-03"
model: claude-sonnet-5
status: complete
input_gaps:
  - {item: "Prospectus (May-2024 IPO)", severity: HIGH, note: "not in corpus; FY20-22 restated figures visible only as screener aggregates, not primary source"}
  - {item: "FY26 Annual Report", severity: HIGH, note: "not filed yet (results-only corpus); freshness gap, FY26 sourced from audited results filing + screener only"}
  - {item: "H1 FY26 results PDF (VILAS_13112025)", severity: LOW, note: "image-only, no text layer, needs OCR; not required for annual Gate 0 scoring"}
  - {item: "Announcements primary PDFs", severity: MEDIUM, note: "partial coverage in corpus"}
  - {item: "Shareholding pattern primary exchange filing", severity: MEDIUM, note: "only aggregator (screener) table available; pledge column absent"}
  - {item: "Contingent liabilities note", severity: MEDIUM, note: "not present in results sidecar or screener; needed for E4"}
  - {item: "Peer set for moat tests M2/M5/M6/M7/M9", severity: MEDIUM, note: "PEER DATA NEEDED, none provided in corpus"}
flags:
  - {type: FLAG-GATE0, reason: "Core score 59/100 falls in the Core 40-59 band, giving AVERAGE regardless of the STRONG (4-moat) qualitative profile; primary depressor is Block B (3/20) cash generation quality."}
  - {type: FLAG-CASH, reason: "Cumulative CFO/PAT 0.55x (FY20-26); CFO -35.46 Cr FY25 and -1.70 Cr FY26 (screener-data) against rising PAT (+34.17 Cr, +39.56 Cr); WC days rose 41.4 to 96.5 FY24-FY26 (computed). Reads growth-induced (Unit-3 capex/WC ramp, IPO- and borrowing-funded) not yet confirmed structural; flag a post-ramp (FY27) recheck."}
data_years: 7
fy_range: "FY20 to FY26"
blocks: {A: 12, B: 3, C: 17, D: 19, E: 8}
core_score: 59
moat_score: 15
grand_total: 74
moats_confirmed: 4
moat_class: "STRONG"
classification: "AVERAGE"
deal_breakers:
  - "Rule 2: Block B = 3 (<8) -> caps classification at max GOOD; non-binding since AVERAGE already sits below GOOD. Driven by FY25 and FY26 negative CFO against rising PAT."
history_downgrade: false
data_notes:
  - "No loss-to-profit swing: PAT positive in all 7 years (FY20 3.60 Cr to FY26 39.56 Cr, screener-data)."
  - "ROCE FY20-23 computed on Net Worth + Borrowings capital-employed basis (current-liability split unavailable in screener); FY24-26 computed on exact Total Assets - Total Current Liabilities basis from the audited standalone balance sheet in the FY26 results sidecar, which gives all three dates (31-Mar-2026 / 31-Mar-2025 / 1-Apr-2024)."
  - "EBIT for FY25 and FY26 taken from the sidecar's own audited P&L (PBT + Finance Costs) to match the exact-basis denominator; FY20-24 EBIT taken from screener-data (PBT + Interest)."
  - "Capex for FY20-24 proxied by total Cash from Investing Activities (screener does not break out PPE/intangible purchases separately); FY25-26 capex is the exact 'Purchase of Property, Plant and Equipment' line from the sidecar cash flow statement."
  - "WC Days (3-component, Receivable+Inventory-Payable) computable on an exact basis only for FY24-26 (Trade Payables not broken out for FY20-23 in screener); B4 trend uses FY24 vs FY26, not FY20 vs FY26."
  - "FY25 CFO discrepancy: screener/operator anchor -35.46 Cr vs sidecar audited restated (Ind AS 101, transition date 1-Apr-2024) -41.53 Cr; screener used as the 7-year trend anchor, sidecar flagged as the freshly restated version filed with FY26 results."
  - "PEER DATA NEEDED: M2 (cost advantage), M5 (scale/dominance), M7 (regulatory/license player count), M9 (brand vs peer GM) all scored 0 for lack of a peer set in corpus."
  - "M6 (R&D) and M8 (distribution) scored 0 for lack of company-specific disclosure, not peer data."
  - "E3 (pledge) and E4 (contingent liabilities/net worth) scored 0, N/A (not in provided data): aggregator shareholding table has no pledge column; results sidecar carries no contingent-liabilities note."
  - "E2 promoter-holding-change window is ~2 years (IPO listing May-2024 to Mar-2026), short of the full 3-year window the metric assumes; stated, not papered over."
block_b_trend: "deteriorating: cumulative CFO/PAT 0.55x; CFO -35.46 Cr FY25 and -1.70 Cr FY26 (screener-data) vs rising PAT (+34.17 Cr, +39.56 Cr); WC days 41.4 (FY24) to 96.5 (FY26, computed). Reads growth-induced (Unit-3 capex/WC ramp, CWIP 37.94 Cr FY25, receivables 38.93->77.50 Cr and inventory 25.78->72.33 Cr FY24-FY26, IPO- and borrowing-funded per financing cash flows), with a secondary WC-efficiency deterioration (trade payables fell 38.12->28.08 Cr FY25-FY26 even as receivables/inventory grew) not yet confirmed structural."
analyst_note: "Classification AVERAGE is driven almost entirely by Block B (3/20), not by growth or balance-sheet quality, both of which score strongly (C 17/20, D 19/20). The moat profile is STRONG (4 confirmed: pricing power, capital efficiency, customer stickiness, switching costs) but sits below the Core>=60 threshold needed for the moat overlay to lift the classification. The cash-quality weakness coincides exactly with the Unit-3 capacity ramp (capex, receivables, inventory all stepping up FY25-26, externally funded via IPO proceeds and short-term borrowing) rather than with margin compression or revenue softness, which argues for growth-induced over structural, but this is unresolved evidence pending a post-ramp FY27 check, not a clean pass. Six of twelve moat tests (M2,M5,M6,M7,M8,M9) scored 0 purely for missing peer/disclosure data, not for a demonstrated absence of moat; treat the moat score as a floor, not a ceiling, until peer data is sourced downstream."
```
