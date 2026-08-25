# GATE 0 SCORECARD — Millworks Technologies Limited (MILLWORKS)
Run date: 2026-08-22 | Model: claude-sonnet-5 | Stage: B01-gate0

Data available: 3 years (FY2024 to FY2026, restated). Scoring adapted to
3-year history.

## SOURCE NOTE (mandatory disclosure)

Per orchestrator instruction, this scorecard is built ENTIRELY from the RHP
restated financial statements:
`RHP_Millworks-07.07.2026 (1).pdf` (Red Herring Prospectus, dated July 07,
2026; company incorporated Nov 01, 2021 as Millworks Technologies Private
Limited, converted to public/listed on BSE SME ~July 2026).

Screener CSVs were checked and NOT used for financials, as instructed.
Contrary to the brief's description that all screener CSVs are "empty
shells," `screener-Data_Sheet.csv` actually carries populated FY2022-FY2026
P&L/BS/CF figures (only price and market cap are populated in
`screener-Profit_Loss.csv`, `screener-Balance_Sheet.csv`,
`screener-Cash_Flow.csv`, `screener-Quarters.csv`, which ARE blank). The
Data_Sheet figures appear mislabeled by one fiscal year against the RHP
restated figures (e.g. screener "FY25" Sales 148.77 = RHP FY26 Revenue
148.77 Cr) and are not used as an anchor source; all numbers below carry
RHP page anchors only.

Business per RHP: precision engineering company manufacturing machined
components, sheet-metal parts, and integrated assemblies for
mission-critical applications across railways, aerospace, defence, and
semiconductor sectors; Build-to-Print (BTP) and Build-to-Spec (BTS) models
(RHP, Annexure IV Note 1, p.F9). This confirms the operator's correction of
the manifest's "Pharma/CDMO" auto-tag.

---

## BLOCK A: RETURN ON CAPITAL (Max 20) — Score: 20/20

ROCE and ROE are RHP-reported figures (source's own figures used per the
formula-definition rule), from the "Basis for Issue Price — Key
Performance Indicators" table (RHP, p.96). RHP's RoCE = EBIT ÷ (tangible
net worth + total debt + deferred tax liabilities, at year-end), not the
Total-Assets-minus-Current-Liabilities formula in these instructions; see
data_notes for an independent cross-check.

| Metric | FY2024 | FY2025 | FY2026 | Source |
|---|---|---|---|---|
| ROCE | 38.61% | 23.02% | 56.44% | RHP p.96 |
| ROE | 144.46% | 40.94% | 69.94% | RHP p.95-96 |

- A1 Median ROCE = 38.61% (median of 23.02/38.61/56.44) → ≥25% = **5**
- A2 Minimum single-year ROCE = 23.02% (FY2025) → ≥15% = **5**
- A3 Median ROE = 69.94% (median of 40.94/69.94/144.46) → ≥20% = **5**
- A4 ROCE trend, latest (56.44%) vs earliest (38.61%): latest ≥ earliest = **5**

Block A total: **20/20**

---

## BLOCK B: CASH GENERATION QUALITY (Max 20) — Score: 0/20

| Metric (₹ Lakhs) | FY2024 | FY2025 | FY2026 | Source |
|---|---|---|---|---|
| CFO | 65.28 | (291.89) | (1,076.29) | RHP Restated Cash Flow, p.S3 / Annexure III p.F8 |
| PAT | 195.41 | 524.90 | 3,706.39 | RHP Restated P&L, p.S2 / Annexure II p.F7 |
| Capex (purchase of PP&E + intangibles, incl. capital advances) | 268.81 | 930.57 | 779.36 | RHP p.S3 / F8 |
| FCF = CFO − Capex | (203.53) | (1,222.46) | (1,855.65) | computed |

- B1 Cumulative CFO ÷ Cumulative PAT = (65.28 − 291.89 − 1,076.29) ÷
  (195.41 + 524.90 + 3,706.39) = −1,302.90 ÷ 4,426.70 = **−0.29x** → <0.50 = **0**
- B2 FCF-positive years: 0 of 3 (all three years negative FCF) → <50% = **0**
- B3 Cumulative FCF ÷ Cumulative PAT = −3,281.64 ÷ 4,426.70 = **−0.74x** →
  negative = **0**
- B4 Change in WC Days, latest vs earliest: FY2024 = 136.11 days, FY2026 =
  191.15 days (computation below) → increase of +55.0 days → increased >15 = **0**

Working Capital Days (Revenue basis; Cost of Material Consumed is
disclosed but is not full COGS — excludes direct/employee/other
manufacturing costs — so Revenue basis is retained per the default rule):

| (days) | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Receivable Days (TR÷Rev×365) | 73.20 | 112.42 | 340.26 |
| Inventory Days (Inv÷Rev×365) | 140.40 | 124.10 | 28.14 |
| Payable Days (TP÷Rev×365) | 77.49 | 72.22 | 177.25 |
| **WC Days** | **136.11** | **164.30** | **191.15** |

Sources: Trade Receivables, Inventory, Trade Payables — RHP Restated
Assets & Liabilities, p.S1 / Annexure I, XI, XIX, XX (p.F19-F21); Revenue
— RHP p.S2.

Block B total: **0/20**

**block_b_trend: deteriorating.** Cumulative CFO/PAT = −0.29x across
FY2024-FY2026. CFO went from +65.28L (FY2024, profitable and cash
generative) to −1,076.29L (FY2026), even as PAT grew to 3,706.39L. Driver:
trade receivables jumped from 13.69% of revenue (FY2024) to 19.66%
(FY2025) to 48.90% (FY2026) (RHP p.90). RHP text explains the FY2026 spike
is partly tied to an arrangement with Quik Pay Private Limited, where
collection depends on Quik Pay's own receipt of funds (RHP p.90). Millworks
separately holds a ₹575.06L non-current equity investment in Quik Pay
Private Limited, acquired in FY2026 (RHP Annexure XV, p.F20) — a related
counterparty-concentration overlap with the receivables stress.

---

## BLOCK C: GROWTH (Max 20) — Score: 20/20

| (₹ Lakhs) | FY2024 | FY2025 | FY2026 | Source |
|---|---|---|---|---|
| Revenue from Operations | 938.60 | 2,210.01 | 14,876.70 | RHP p.S2 / p.95 |
| YoY Revenue Growth | — | +135.46% | +573.15% | RHP p.95 (KPI table) |
| PAT | 195.41 | 524.90 | 3,706.39 | RHP p.S2 |

- C1 Revenue CAGR (FY2024→FY2026, 2 years) = (14,876.70÷938.60)^(1/2) − 1
  = **298.1%** → ≥20% = **5**
- C2 PAT CAGR (same window) = (3,706.39÷195.41)^(1/2) − 1 = **335.5%** →
  ≥20% = **5**
- C3 Positive YoY revenue years: 2 of 2 (FY2025 +135.46%, FY2026 +573.15%,
  RHP p.95) → 100% = **5**
- C4 PAT CAGR − Revenue CAGR = 335.5% − 298.1% = **+37.4pp** → ≥+3pp = **5**

Block C total: **20/20**

Caveat (data_note): company was incorporated Nov 01, 2021; the restated
window opens at a near-nil FY2024 base (Rev 938.60L). These CAGRs measure
extreme base-effect expansion off IPO-scale-up, not steady-state growth.

---

## BLOCK D: BALANCE SHEET STRENGTH (Max 20) — Score: 15/20

| Metric (FY2026, latest) | Value | Source |
|---|---|---|
| Total Borrowings (LT 787.14 + ST 914.68) | 1,701.82 | RHP p.S1 / Annexure VII, X (p.F19) |
| Cash & Bank | 135.16 | RHP p.S1 / Annexure XXI (p.F21) |
| Net Debt | 1,566.66 | computed |
| EBITDA | 5,630.43 | RHP p.95-96 (KPI table) |
| Net Debt ÷ EBITDA | 0.278x | computed |
| EBIT (PBT 5,022.97 + Finance cost 340.06) | 5,363.03 | RHP p.S2 |
| Interest (Finance costs) | 340.06 | RHP p.S2 |
| Interest Coverage (EBIT÷Interest) | 15.77x | computed |
| Debt ÷ Equity | 0.21 | RHP p.96 (source-reported, KPI table) |
| Current Assets | 15,396.91 | computed from RHP p.S1 |
| Current Liabilities | 10,737.52 | computed from RHP p.S1 |
| Current Ratio | 1.434 | computed |

- D1 Net Debt÷EBITDA = 0.278x → 0-1.0x = **4**
- D2 Interest Coverage = 15.77x → ≥10x = **5**
- D3 Debt÷Equity = 0.21 → 0.1-0.5 = **4**
- D4 Current Ratio = 1.434 → 1.2-1.49 = **2**

Block D total: **15/20**

---

## BLOCK E: SHAREHOLDER ALIGNMENT (Max 20) — Score: 15/20

| Metric | Value | Source |
|---|---|---|
| Promoter + Promoter Group holding (latest, RHP date) | 65.08% | RHP p.74 (Shareholding Pattern) |
| Promoters only (4 named individuals) | 59.22% | RHP p.76 |
| Promoter pledge (latest) | 0% | RHP p.78 ("none of the Equity Shares held by our Promoters are pledged") |
| Contingent Liabilities (FY2026) | 8.45 | RHP p.55 (Summary of Contingent Liabilities) |
| Net Worth (FY2026) | 8,266.99 | RHP p.95-96 |
| Contingent Liabilities ÷ Net Worth | 0.10% | computed |

- E1 Promoter holding (latest) = 65.08% (Promoters + Promoter Group, RHP
  p.74) → ≥60% = **5**
- E2 Promoter holding change: only a ~2-year comparable window exists (not
  3), because the company was a 4-founder, 50,000-share private entity at
  incorporation (Nov 2021) and the RHP's earliest 1%-holder table dated
  "two years prior to filing" (RHP p.75) shows the 4 promoters holding
  ~75.26% combined (Sridhar Acharya 18.28% + H K Madhu 18.28% + Rashmi
  Sridhar Acharya 19.35% + Sowmya Madhu 19.35%). Against the latest 65.08%
  (or 59.22% promoters-only), this is a decrease of 10.2-16.0pp. Per rule,
  decreased >3% = **0**. Data note: this is pre-IPO preferential-allotment
  and 200:1 bonus-issue dilution (RHP p.69-72), not open-market promoter
  selling.
- E3 Promoter pledge = 0% → **5**
- E4 Contingent Liabilities ÷ Net Worth = 8.45 ÷ 8,266.99 = 0.10% → <5% = **5**

Block E total: **15/20**

---

## BLOCK F: QUANTITATIVE MOAT SCORING (Max 60) — Score: 13/60

Peer data used where available: Unimech Aerospace and Manufacturing Ltd
and Azad Engineering Ltd, both sourced from RHP "Basis for Issue Price —
Comparison of KPIs with Listed Industry Peers" (RHP p.96-98) and the
Trade Receivables comparison table (RHP p.90).

| Test | Score | Basis |
|---|---|---|
| M1 Pricing Power | **5** | EBITDA margin expanded 29.55%→36.71% (+7.16pp, RHP p.95-96) AND revenue CAGR 298.1% (≥10%) |
| M2 Cost Advantage vs peer median | **0** | Millworks FY2026 EBITDA margin 36.71% vs peer median (Unimech 42.47% + Azad 41.78%)÷2 = 42.13% (RHP p.97-98) — below peers |
| M3 Capital Efficiency | **5** | FAT = Rev 14,876.70 ÷ Net Block (PP&E 1,991.91 + Intangibles 516.57 = 2,508.48) = 5.93x (>3x) AND ROCE 56.44% (>20%) |
| M4 Customer Stickiness | **3** | Zero revenue-decline years, but receivable days NOT stable ±10 (73→112→340 days); scored at the "max 1 decline year / effectively no decline" tier, not the top tier, because the stability leg of the AND condition fails — see data_notes |
| M5 Scale & Dominance | **0 — PEER DATA NEEDED** | Millworks FY2026 revenue (148.77 Cr) and EBITDA margin (36.71%) are both the smallest/lowest of the 3 named peers; full segment-mcap universe beyond Unimech/Azad not available |
| M6 Technology/R&D | **0 — N/A (not in provided data)** | R&D/Revenue not disclosed in RHP restated financials |
| M7 Regulatory/License | **0 — N/A (not in provided data)** | Not a licence-scarcity model per RHP business description; count of comparable regulated players not disclosed |
| M8 Distribution | **0** | B2B mission-critical component manufacturer; no distribution-network disclosure in provided data |
| M9 Brand | **0 — PEER DATA NEEDED** | Peer gross-margin/material-cost breakdown not extracted; Millworks GM proxy = (14,876.70−7,595.53)÷14,876.70 = 48.94% but no peer comparator available |
| M10 Switching Costs | **0** | Revenue grew every year, but receivable days rose +267 days over the period (far beyond the ≤10-day top-tier threshold); no tier fits cleanly, "else = 0" applied |
| M11 Network Effects | **0** | <6-year history triggers conservative scoring per rule; selling/distribution expense not separately disclosed in restated P&L (bundled in "Other expenses"), so even the overall-trend tier could not be confirmed |
| M12 Negative WC/Float | **0** | WC Days 136.11/164.30/191.15, all >45 days in every year |

Moat score: **13/60**. Moats "present" (score ≥3): M1, M3, M4 = **3 confirmed**.

Moat classification: 2-3 present = **MODERATE**

---

## DATA CONFIDENCE

3 restated fiscal years (FY2024-FY2026) available → **3-4 yrs = LIMITED**.
Per rule: downgrade classification one tier. **history_downgrade: true.**

---

## SCORECARD SUMMARY

| Block | Score | Max | % |
|---|---|---|---|
| A — Return on Capital | 20 | 20 | 100% |
| B — Cash Generation Quality | 0 | 20 | 0% |
| C — Growth | 20 | 20 | 100% |
| D — Balance Sheet Strength | 15 | 20 | 75% |
| E — Shareholder Alignment | 15 | 20 | 75% |
| **Core (A+B+C+D+E)** | **70** | **100** | **70%** |
| F — Moat Score | 13 | 60 | 21.7% |
| **Grand Total** | **83** | **160** | — |

Strongest blocks: A (Return on Capital) and C (Growth), both 20/20.
Weakest block: B (Cash Generation Quality), 0/20 — a complete cash-
conversion failure sitting directly beneath the strongest P&L numbers.

---

## DEAL-BREAKER OVERRIDES

- **DB2**: Block B score = 0 (<8) → caps classification at max GOOD.
- **DB4**: Cumulative CFO ÷ Cumulative PAT = −0.29x (<0.50) → caps
  classification at max AVERAGE. **This is the binding constraint** (more
  restrictive than DB2).
- DB1 (Block A<8), DB3 (median ROCE<10%), DB5 (pledge>15%), DB6
  (ND/EBITDA>3x AND IC<3x), DB7 (revenue declined majority of years), DB8
  (PAT negative in last 3 years), DB9 (history<3 years): **not triggered**
  (history is exactly 3 years, not fewer).

---

## CLASSIFICATION

Matrix result before overrides: Core 70 (60-79 band) + Moat MODERATE
(not STRONG/FORTRESS) → **GOOD**.

Deal-breaker DB4 caps this at **AVERAGE**.

Data-confidence downgrade (3-yr LIMITED history) then drops one further
tier: **AVERAGE → AVOID**.

## FINAL CLASSIFICATION: AVOID

## DECISION LINE

Millworks screens with textbook Return-on-Capital and Growth numbers
(20/20 each) built on a near-zero FY2024 base and a single explosive
FY2026 scale-up year, but the cash-generation block is a complete zero:
every one of FY2024-FY2026 posted negative free cash flow, and FY2026
alone burned ₹10.76 Cr of operating cash against ₹37.06 Cr of reported
PAT, driven by a receivables spike tied in part to a Quik Pay Private
Limited counterparty in which Millworks also holds a ₹5.75 Cr equity
stake. The cash-conversion deal-breaker caps the classification at
AVERAGE; the company's 3-year restated history (LIMITED data confidence)
downgrades it one more tier to AVOID. Per pipeline rules this does not
halt the run — company quality never halts a run — but it is the leading
flag for every downstream stage: verify the Quik Pay receivables and
equity-investment relationship before any valuation work proceeds.

---

## ANALYST NOTE

Millworks screens as a paradox: near-perfect Return on Capital and Growth
blocks (20/20 each) sit beside a zero-score Cash Generation block. Revenue
and PAT CAGRs near 300-335% are real numbers but measure expansion off a
near-nil FY2024 base (incorporated Nov 2021), not steady-state economics.
All three restated years show negative CFO after FY2024, and FY2026 alone
burned Rs 10.76 Cr of operating cash while reporting Rs 37.06 Cr of PAT,
driven by trade receivables jumping to 48.9% of revenue. RHP explicitly
ties part of this to a Quik Pay Private Limited arrangement, where
collections wait on Quik Pay's own cash receipt; Millworks also holds a
Rs 5.75 Cr equity stake in Quik Pay, an unusual related-counterparty
overlap. Deal-breaker DB4 (cumulative CFO/PAT <0.50) caps classification
at AVERAGE regardless of the strong P&L blocks; the 3-year restated
window (LIMITED data confidence) then downgrades one more tier to AVOID.
Moat score is thin (13/60, MODERATE) because 5 of 12 tests lack peer or
R&D/distribution data and were scored 0 rather than guessed. Downstream
stages should treat the Quik Pay receivables/investment link as the
single highest-priority verification item.

---

## INPUT GAPS (carried from B00)

- No results PDF (recently listed; RHP is the sole financial source).
- No credit rating disclosed in provided documents.
- No standalone Annual Report (RHP restated financial statements used as
  the source of record instead).
- Shareholding pattern was NOT actually missing — it was located inside
  the RHP Capital Structure section (p.68-79) and used for Block E above.
  Flagging the resolution here since B00 listed it as a gap.

```yaml
stage: B01-gate0
company: "MILLWORKS"
run_date: "2026-08-22"
model: claude-sonnet-5
status: complete
input_gaps: ["no results PDF", "no rating", "no standalone AR (RHP is the source)", "no shareholding pattern"]
flags:
  - type: FLAG-GATE0
    reason: "Classification AVOID. DB4 (cumulative CFO/PAT = -0.29x, <0.50) caps at AVERAGE; 3-year LIMITED history downgrades one tier to AVOID. Block A and C both 20/20 (ROCE, ROE, revenue/PAT CAGR) but Block B is 0/20 -- all 3 restated years FCF-negative, FY2026 CFO -1,076.29L against PAT +3,706.39L. Driver: trade receivables 48.90% of FY2026 revenue (RHP p.90), tied partly to a Quik Pay Private Limited arrangement; Millworks also holds a 575.06L equity investment in Quik Pay (RHP Annexure XV) -- related counterparty-concentration flag for downstream verification."
data_years: 3
fy_range: "FY2024 to FY2026"
blocks: {A: 20, B: 0, C: 20, D: 15, E: 15}
core_score: 70
moat_score: 13
grand_total: 83
moats_confirmed: 3
moat_class: "MODERATE"
classification: "AVOID"
deal_breakers:
  - "DB2: Block B score 0 (<8) -> caps at max GOOD"
  - "DB4: Cumulative CFO/PAT = -0.29x (<0.50) -> caps at max AVERAGE (binding constraint)"
history_downgrade: true
data_notes:
  - "No loss-to-profit swing; all 3 restated years (FY24-FY26) PAT-positive."
  - "ROCE/ROE used RHP-reported figures (p.96) per source-figure rule; RHP RoCE basis (tangible net worth+total debt+DTL) differs from the Total Assets-CL formula in these instructions. Independent cross-check using the strict formula gives ~58.9% FY26 ROCE, directionally consistent, no scoring impact."
  - "WC Days computed on Revenue basis (Cost of Material Consumed disclosed but is not full COGS, so COGS basis not used per default rule)."
  - "E2 measured over ~2 years, not 3, because the company was a 4-founder 50,000-share entity at Nov-2021 incorporation; decline from ~75.3% (2yr prior, RHP p.75) to 65.08% (RHP p.74) is pre-IPO preferential-allotment and 200:1 bonus-issue dilution, not open-market promoter selling."
  - "screener-Data_Sheet.csv is NOT actually empty (contradicts orchestrator brief) but its FY labels appear misaligned vs RHP restated figures and it was not used as an anchor source per instruction; screener-Profit_Loss/Balance_Sheet/Cash_Flow/Quarters.csv ARE genuinely blank."
  - "RHP Annexure IV Note 3 (p.F15-F16) discloses extensive self-identified restatement adjustments across all 3 years (insurance, electricity, ICD interest, MSME interest, rent, salary, sales, inventory, gratuity, FX, D&A, prior-period items, tax) -- not scored in Gate 0 but relevant to downstream data-quality review."
  - "M5/M6/M7/M8/M9 scored 0 as PEER DATA NEEDED or N/A (not in provided data): no R&D%, no full segment mcap universe beyond Unimech/Azad, no distribution disclosure, no peer gross-margin breakdown."
  - "M11 scored 0: <6yr history plus selling-expense line not separately disclosed (bundled in 'Other expenses'), so even the conservative overall-trend tier could not be confirmed."
  - "M4 scored 3 not 5: zero revenue-decline years but receivable days rose from 73 to 340 over the window, failing the stability leg of the AND condition."
  - "Significant related-party transactions with V3 Technologies (partnership firm, 5.86% shareholder, promoter-family controlled): rent 155.76L (FY26)/91.85L (FY25), PP&E purchase 707.74L (FY25), material purchases, advances (RHP p.56-57) -- not scored in Gate 0 but relevant to downstream governance review."
  - "Company incorporated Nov 01, 2021; restated window opens at a near-nil FY2024 base (Rev 938.60L), so Block C CAGRs reflect extreme base-effect expansion, not steady-state growth."
block_b_trend: "deteriorating -- cumulative CFO/PAT = -0.29x FY24-FY26; CFO went from +65.28L (FY24) to -1,076.29L (FY26) despite PAT growing to 3,706.39L; WC days rose from 136 to 191 over the same window (RHP p.S3/Annexure III, p.F8)."
analyst_note: "Millworks screens as a paradox: near-perfect Return on Capital and Growth blocks (20/20 each) sit beside a zero-score Cash Generation block. Revenue and PAT CAGRs near 300-335% are real numbers but measure expansion off a near-nil FY2024 base (incorporated Nov 2021), not steady-state economics. All three restated years show negative CFO after FY2024, and FY2026 alone burned Rs 10.76 Cr of operating cash while reporting Rs 37.06 Cr of PAT, driven by trade receivables jumping to 48.9% of revenue. RHP explicitly ties part of this to a Quik Pay Private Limited arrangement, where collections wait on Quik Pay's own cash receipt; Millworks also holds a Rs 5.75 Cr equity stake in Quik Pay, an unusual related-counterparty overlap. Deal-breaker DB4 caps classification at AVERAGE regardless of the strong P&L blocks; the 3-year restated window (LIMITED data confidence) then downgrades one more tier to AVOID. Moat score is thin (13/60, MODERATE) because 5 of 12 tests lack peer or R&D/distribution data and were scored 0 rather than guessed. Downstream stages should treat the Quik Pay receivables/investment link as the single highest-priority verification item."
```
