# GATE 0 SCORECARD — Prizor Viztech Ltd (PRIZOR)
Run date: 2026-07-12 | Stage: B01-gate0 | Model: claude-sonnet-5

**Sector correction**: The manifest tags this company "Pharma / CDMO." This is
a known collect_to_repo defect and is disregarded per operator instruction.
Prizor Viztech is a video surveillance / security electronics manufacturer
(CCTV cameras, AI-enabled video systems). Peer set for moat tests: CP Plus,
D-Link India, OSEL Devices, Sahasra.

Data available: 2 years (FY2023-24 to FY2024-25). Scoring adapted to
2-year history — this is a recently-listed SME/micro-cap (IPO completed
during FY2024-25); no FY2023 or earlier balance sheet exists. All CAGR
labels below are effectively single-period (n=1) growth rates, not true
compound rates, and the median/trend tests in Blocks A and E collapse to
2-point comparisons. Treated honestly throughout; classification is
capped by the data-confidence rule for this reason (see below).

**Data sources**: No results/ PDFs and no rating/ PDF were provided
(DEGRADATION MAP applies). Gate 0 runs from screener Data_Sheet.csv
(2 years, FY24–FY25 only; the screener's P&L/BS/CF/Quarters CSVs are
empty templates) cross-checked against the FY2024-25 Annual Report
(standalone financial statements, notes, CARO report, shareholding
pattern). AR figures are in Rs thousands in-source; converted to Rs Cr
(÷10,000) for this scorecard and cross-checked against Data_Sheet values
(differences <0.2cr, immaterial, attributable to rounding/regrouping).

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 15/20

Capital Employed = Total Assets − Current Liabilities (AR balance sheet
breakdown; Data_Sheet does not split current liabilities from
non-current, so AR is used for CE / ROCE).
- FY24: Total Assets 24.624cr, Current Liabilities 12.878cr (AR p.71) →
  CE = 11.747cr
- FY25: Total Assets 56.798cr, Current Liabilities 9.151cr (AR p.71) →
  CE = 47.647cr
- EBIT (PBT + Finance Costs): FY24 = 7.55 + 0.65 = 8.201cr (screener-data;
  AR p.72 PBT 75,543.37 + Finance Cost 6,465.45 = 82,008.82 th = 8.201cr).
  FY25 = 13.66 + 1.42 = 14.910cr (screener-data; AR p.72: 136,702.85 +
  12,401.64 = 149,104.49 th = 14.910cr). "computed" per formula.

- **ROCE FY24 = 8.201 / 11.747 = 69.82%** (computed, AR p.71/72)
- **ROCE FY25 = 14.910 / 47.647 = 31.29%** (computed, AR p.71/72)

A1 Median ROCE (2yr, = average) = (69.82+31.29)/2 = **50.56%** → ≥25% → **5**
A2 Minimum single-year ROCE = 31.29% (FY25) → ≥15% → **5**
A3 Median ROE:
  - ROE FY24 = PAT 5.521cr (AR p.72) / closing Net Worth 6.668cr (AR p.71,
    opening NW unavailable — earliest year, closing basis used per rule)
    = **82.79%**
  - ROE FY25 = PAT 10.153cr (AR p.72) / avg NW [(6.668+42.829)/2 =
    24.749cr] = **41.02%**
  - Median (avg) = 61.90% → ≥20% → **5**
A4 ROCE trend, latest vs earliest: 31.29% vs 69.82% = decline of 38.5pp →
   decline >5pp → **0**. Note: this "decline" is a base effect — FY24 sat
   on a razor-thin pre-IPO equity/asset base (Net worth 6.67cr); FY25's
   47.6cr capital-employed base (post-IPO proceeds + bonus issue) is the
   structurally more meaningful figure. Flagged in data_notes, not
   overridden — formula applied as specified.

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 0/20

- CFO FY24 = −1.82cr (screener-data; AR p.73 standalone CF stmt:
  −18,202.34 th = −1.820cr) | CFO FY25 = −14.10cr (screener-data; AR p.73:
  −140,952.33 th = −14.095cr)
- Capex (Purchase of PPE + CWIP, from CF stmt, AR p.73): FY24 = 1.862cr |
  FY25 = 8.276cr
- FCF FY24 = −1.820 − 1.862 = **−3.682cr** | FCF FY25 = −14.095 − 8.276 =
  **−22.371cr**
- Cumulative CFO = −15.915cr | Cumulative PAT = 5.521 + 10.153 = 15.673cr
  (AR p.72)
- Cumulative FCF = −26.053cr

B1 Cumulative CFO ÷ Cumulative PAT = −15.915 / 15.673 = **−1.02** → <0.50
   → **0**
B2 FCF-positive years = 0 of 2 = 0% → **0**
B3 Cumulative FCF ÷ Cumulative PAT = −26.053 / 15.673 = **−1.66** →
   <0.20/negative → **0**
B4 Change in WC Days, latest vs earliest (see Block C/WC calc below):
   167.67 days (FY24) → 213.93 days (FY25) = **+46.3 days** → increased
   >15 → **0**

**This is the block that determines the classification.** Both years show
deeply negative operating cash flow despite strong reported profit —
receivables, and especially inventory, are consuming cash far faster than
profit is being generated. This is a material Block B signal per the
task brief and is carried into deal-breakers below.

## BLOCK C: GROWTH (Max 20) — Score: 15/20

- Revenue: FY24 = 35.65cr (screener-data; AR p.72: 35.654cr) → FY25 =
  70.98cr (screener-data; AR p.72: 71.094cr)
- PAT: FY24 = 5.52cr → FY25 = 10.15cr (screener-data)
- Working Capital Days (revenue basis — COGS not cleanly isolable from
  screener data; Payable Days uses AR trade payables since Data_Sheet
  does not break payables out from "Other Liabilities"):
  - FY24: Receivable Days = 7.96/35.65×365 = 81.50 | Inventory Days =
    14.27/35.65×365 = 146.13 | Payable Days = 5.855/35.65×365 = 59.96
    (Trade Payables 5.855cr, AR p.71 Note 9) → **WC Days = 167.67**
  - FY25: Receivable Days = 15.74/70.98×365 = 80.93 | Inventory Days =
    28.50/70.98×365 = 146.57 | Payable Days = 2.638/70.98×365 = 13.57
    (Trade Payables 2.638cr, AR p.71 Note 9) → **WC Days = 213.93**

C1 Revenue CAGR (n=1 window, FY24→FY25) = 70.98/35.65 − 1 = **99.07%** →
   ≥20% → **5** (single-period growth, not a true multi-year CAGR — noted)
C2 PAT CAGR (n=1) = 10.15/5.52 − 1 = **83.88%** → both endpoints positive,
   no loss-to-profit swing → ≥20% → **5**
C3 Positive YoY revenue years = 1 of 1 available comparison = 100% → **5**
   (only one YoY comparison exists given 2-year history)
C4 PAT CAGR − Revenue CAGR = 83.88% − 99.07% = **−15.19pp** → <−8pp → **0**
   (margin/profit growth lagged revenue growth materially despite the
   PAT increase — consistent with the EBITDA margin compression noted
   in M1 below and the cash-conversion weakness in Block B)

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 18/20

Latest year = FY25.
- Total borrowings FY25 = 7.52cr (screener-data; AR p.71: LT 4.764cr + ST
  2.756cr = 7.521cr) | Cash FY25 = 0.23cr (screener-data; AR p.71:
  0.131cr — screener's 0.23cr includes wider "cash & bank" definition;
  AR-narrow cash-and-equivalents used below for Net Debt, more
  conservative)
- EBITDA FY25 = EBIT 14.910cr + Depreciation 0.166cr (AR p.72) =
  **15.077cr**

D1 Net Debt ÷ EBITDA = (7.521 − 0.131) / 15.077 = 7.390/15.077 = **0.49x**
   → 0–1.0x → **4**
D2 Interest Coverage = EBIT ÷ Interest = 14.910 / 1.240 (AR p.72 Finance
   Costs) = **12.02x** → ≥10x → **5**
D3 Debt ÷ Equity = 7.521 / 42.829 (AR p.71 Shareholders' Funds) =
   **0.176** → 0.1–0.5 → **4**
D4 Current Ratio = Current Assets 46.508cr ÷ Current Liabilities 9.151cr
   (AR p.71) = **5.08x** → ≥2.0 → **5**

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 15/20

E1 Promoter holding, latest (31-Mar-2025) = **68.28%** (AR p.93,
   Corporate Governance shareholding disclosure — total Promoters and
   Promoter Group; cross-checked at AR p.79: Mitali Gauswami 45.18% +
   Dasharathbharthi Gauswami 23.10% = 68.28%) → ≥60% → **5**
E2 Promoter holding change: FY24 close = 90.00% + 9.99% = 99.99% (AR
   p.80, wholly pre-IPO promoter-held) → FY25 close = 68.28% (AR p.79) →
   change = **−31.71pp** → decreased >3% → **0**. Only a 2-year window
   is available (not the specified 3-year window); the entire decline is
   IPO-driven float creation (28,91,200 IPO shares issued + 66,00,003
   bonus shares, AR p.79 share reconciliation) plus bonus dilution, not
   open-market promoter selling — both promoters held their full
   pre-IPO share count unchanged at FY25 close. Scored literally per the
   formula; context flagged in data_notes.
E3 Promoter pledge, latest = **0%** (AR p.66, CARO report: "the company
   has not raised loans during the period on the pledge of securities
   held in its subsidiaries, joint ventures or associate companies"; no
   pledge disclosed against promoter/promoter-group holding anywhere in
   the shareholding pattern) → 0% → **5**
E4 Contingent Liabilities ÷ Net Worth, latest = **0 / 42.829cr = 0%** (AR
   p.91, Note 43: "Currently, there are no contingent liabilities that
   should be reported in the financial statements of the company") →
   <5% → **5**

---

## CORE SCORE

| Block | Score | Max |
|---|---|---|
| A — Return on Capital | 15 | 20 |
| B — Cash Generation Quality | 0 | 20 |
| C — Growth | 15 | 20 |
| D — Balance Sheet Strength | 18 | 20 |
| E — Shareholder Alignment | 15 | 20 |
| **Core Total** | **63** | **100** |

Strongest block: **D — Balance Sheet Strength (18/20, 90%)** — low
leverage, strong coverage, high liquidity, all funded off IPO proceeds.
Weakest block: **B — Cash Generation Quality (0/20)** — every sub-metric
scored zero; cash conversion is the defining weakness of this company.

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 19/60

EBITDA margin (screener-data basis, for M1): FY24 = 8.21/35.65 = 23.03% |
FY25 = 15.20/70.98 = 21.42% (cross-check, AR-derived basis: FY24 23.14%,
FY25 21.20% — consistent within rounding).

M1 Pricing Power: margin change = 21.42% − 23.03% = **−1.61pp** (within
   ±2pp) AND revenue CAGR ≥10% (99.07%) → "margin stable ±2pp AND rev
   CAGR ≥10%" → **3**
M2 Cost Advantage vs peer median EBITDA margin: no peer (CP Plus, D-Link
   India, OSEL Devices, Sahasra) financial data was provided to this
   stage → **0, PEER DATA NEEDED**
M3 Capital Efficiency: FAT = Revenue ÷ Net Block = 70.98 / 8.27 (screener-
   data FY25 Net Block; AR p.71 PPE net 8.271cr) = **8.58x** (>3x) AND
   ROCE FY25 = 31.29% (>20%) → **5**
M4 Customer Stickiness: 0 revenue-decline years (of 1 available
   comparison) AND receivable days change FY24→FY25 = 81.50→80.93 =
   **−0.57 days** (stable, well within ±10) → **5**
M5 Scale & Dominance: needs peer mcap/margin ranking; no peer data
   provided to this stage → **0, PEER DATA NEEDED**
M6 Technology / R&D: R&D expenditure = **NIL** (AR p.40, Directors'
   Report, "the expenditure incurred on Research and Development: NIL")
   → R&D/Revenue = 0%, below the 1% floor → **0**
M7 Regulatory / License: video surveillance / CCTV manufacturing is not a
   licensed/regulated segment (no licensing regime identified in AR) →
   unregulated → **0**
M8 Distribution: no quantified dealer/distributor/system-integrator
   network disclosed anywhere in the AR (searched for
   distributor/dealer/channel-partner/reseller/system-integrator/OEM
   terms — no matches) → **0**
M9 Brand: requires peer gross-margin comparison; no peer data provided to
   this stage → **0, PEER DATA NEEDED**
M10 Switching Costs: revenue grew (1 of 1 available years) AND
   receivable days change over the period = −0.57 days (≤10 days,
   in fact declined) → **5**
M11 Network Effects: test requires ≥6 years for the two-window
   comparison; only 2 years available — **scored conservatively on
   overall trend, stated per rule**. Revenue CAGR (99%) ≥20%, but
   Selling & Admin expense rose from 1.60% of revenue (FY24: 0.57/35.65)
   to 2.31% (FY25: 1.64/70.98) — selling % rising alongside growth →
   "growth >15% but selling % rising" → **1**
M12 Negative WC / Float: WC Days FY24 = 167.67, FY25 = 213.93 — both
   >45 in both years, no negative-WC years → **0**

| Test | Score | Note |
|---|---|---|
| M1 Pricing Power | 3 | margin stable, rev CAGR ≥10% |
| M2 Cost Advantage | 0 | PEER DATA NEEDED |
| M3 Capital Efficiency | 5 | FAT 8.58x, ROCE 31.3% |
| M4 Customer Stickiness | 5 | no decline yr, receivable days stable |
| M5 Scale & Dominance | 0 | PEER DATA NEEDED |
| M6 Technology / R&D | 0 | R&D = NIL |
| M7 Regulatory / License | 0 | unregulated segment |
| M8 Distribution | 0 | no quantified network disclosed |
| M9 Brand | 0 | PEER DATA NEEDED |
| M10 Switching Costs | 5 | growth + stable receivable days |
| M11 Network Effects | 1 | <6yr history, selling % rising |
| M12 Negative WC / Float | 0 | WC days 168→214, both >45 |
| **Total** | **19/60** | |

Moats present (score ≥3): M1, M3, M4, M10 = **4 moats present**.
Moat classification: 4-5 present = **STRONG**.

Three of twelve tests (M2, M5, M9) are unscoreable as PEER DATA NEEDED —
no financial data for CP Plus, D-Link India, OSEL Devices, or Sahasra was
injected into this stage. This depresses the moat score mechanically
versus what a full peer-benchmarked run would show; carry forward to
downstream stages that do have peer access.

---

## CLASSIFICATION

Grand total (core + moat) = 63 + 19 = **82**

**Data confidence: <3 years (2 years available) → auto AVERAGE.** This
overrides the raw classification-matrix lookup (Core 60-79 + STRONG
would otherwise map to GOOD+). Applied per rule.

Deal-breaker overrides checked:
1. Block A <8? No (15). Not triggered.
2. Block B <8? **Yes (0)** → max GOOD. Triggered.
3. Median ROCE <10%? No (50.56%). Not triggered.
4. Cumulative CFO/PAT <0.50? **Yes (−1.02)** → max AVERAGE. Triggered.
5. Pledge >15%? No (0%). Not triggered.
6. ND/EBITDA >3x AND IC <3x? No (0.49x / 12.02x). Not triggered.
7. Revenue declined in majority of years? No. Not triggered.
8. PAT negative in any of last 3 years? No (both years positive). Not
   triggered.
9. History <3 years? **Yes (2 years)** → AVERAGE. Triggered.

Most restrictive override = **AVERAGE** (from deal-breakers #4 and #9,
independently reinforced by the standalone data-confidence auto-AVERAGE
rule). Years driving the deal-breakers: **both FY24 and FY25** for the
cash-conversion breaker (#4) — negative CFO in every year of the
available history, not a one-off; and the entire dataset (post-IPO
listing, no pre-FY24 financials exist) for the history breaker (#9).

### FINAL CLASSIFICATION: AVERAGE

Core Score: 63/100 | Moat Score: 19/60 (STRONG, 4 moats present) |
Grand Total: 82 | Data confidence: LOW (<3yr, auto-AVERAGE)

Decision line: Prizor Viztech screens with strong reported growth (99%
revenue, 84% PAT, single-period), a genuinely strong balance sheet
(net cash-light, 12x interest cover, 5x current ratio, all IPO-funded),
and 4 of 12 quantitative moat tests present (pricing stability, capital
efficiency, customer stickiness, switching costs) — but Block B (cash
generation) scores zero across all four sub-tests, cumulative CFO/PAT is
−1.02x, and working capital days rose 46 days in the one year measured.
Combined with only 2 years of post-IPO history, the mechanical
classification caps at AVERAGE regardless of the otherwise-strong growth
and balance-sheet picture. This is not a company-quality judgment — it
is the mechanical output of the deal-breaker and data-confidence rules
as specified, and it flags forward for scrutiny in later stages rather
than halting the pipeline.

---

## FLAGS

- **FLAG-GATE0**: Classification AVERAGE with historical depressors
  identified. Drivers: (1) cumulative CFO/PAT = −1.02x across both years
  of available history (deal-breaker #4); (2) history <3 years, SME IPO
  with no pre-FY24 financials (deal-breaker #9); (3) Block B scores 0/20
  on every sub-metric. Downstream note: post-IPO working-capital build
  (inventory 14.27→28.50cr, receivables 7.96→15.74cr) is a plausible
  scale-up story but is not evidenced as transient in the data provided
  — treat as a live risk, not assumed to normalize.
