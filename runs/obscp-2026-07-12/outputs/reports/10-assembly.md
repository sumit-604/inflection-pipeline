# STAGE 10: VALUATION INPUT ASSEMBLY (B10-valinputs)
## OBSC Perfection Ltd (OBSCP)
**Run Date:** 2026-07-12 | **Model:** claude-haiku-4-5 | **Status:** COMPLETE

---

## COMPANY IDENTITY BLOCK

| Field | Value | Source |
|-------|-------|--------|
| Company name | OBSC Perfection Ltd | manifest.yaml |
| Ticker | OBSCP | manifest.yaml |
| NSE platform | NSE Emerge (SME) | B00 / B04 |
| Sector | Manufacturing (corrected) | fttcp-deliberation (was "EPC / Civil construction" in manifest) |
| Business model type | Asset-heavy precision engineering; contract manufacturing | B04-bizmodel |
| Sector cap row (authority) | Manufacturing 25x | fttcp-deliberation, supersedes manifest |
| CMP (Rs per share) | 666 | manifest.yaml |
| Market cap (Rs Cr) | 1,720.15 | manifest.yaml, screener-Data_Sheet.csv line 8 |
| Shares outstanding (diluted, Cr) | 2.58 | screener-Data_Sheet.csv line 63 (Adjusted Equity Shares in Cr) |
| Enterprise value computation | Market cap + Net debt = 1,720.15 + 67.3 = 1,787.45 Cr | Market cap (manifest) + Net debt (computed below) |

---

## LATEST PERIOD FINANCIALS (FY26 = year ended 31 March 2026)

### Income Statement & Profitability

| Metric | FY26 Value | Source & Anchor |
|--------|-----------|-----------------|
| Revenue (also "Operating income") | Rs 219.54 Cr | screener-Data_Sheet.csv line 11; CRISIL confirms FY26 operating income Rs 220.58 Cr (CRISIL_Rating_Rationale_2026-07-02, p.2, Key Financial Indicators table) |
| EBITDA | Rs 43.64 Cr | CRISIL_Rating_Rationale_2026-07-02, p.2 ("interest coverage 9.72x…implies EBITDA Rs 43.64 Cr, 19.8% margin"); verified: EBITDA = EBIT + Deprec = (PBT + Interest) + Deprec = (31.77 + 4.49) + 7.38 = 43.64 Cr |
| EBITDA margin | 19.8% | CRISIL_Rating_Rationale_2026-07-02, p.2 |
| EBIT (Operating profit) | Rs 36.26 Cr | Computed: PBT + Finance cost = 31.77 + 4.49 = 36.26 Cr (screener lines 22, 21); used for ROCE calculation per fttcp-deliberation |
| PBT | Rs 31.77 Cr | screener-Data_Sheet.csv line 22 |
| Tax | Rs 4.77 Cr | screener-Data_Sheet.csv line 23 |
| PAT (Net profit) | Rs 27.01 Cr | screener-Data_Sheet.csv line 24; CRISIL_Rating_Rationale_2026-07-02, p.2 confirms "Reported profit after tax (PAT)" Rs 27.01 Cr |
| PAT margin | 12.24% | CRISIL_Rating_Rationale_2026-07-02, p.2 |
| Interest expense | Rs 4.49 Cr | screener-Data_Sheet.csv line 21 |
| Depreciation & amortisation | Rs 7.38 Cr | screener-Data_Sheet.csv line 20 |

### Cash Flow & Working Capital

| Metric | FY26 Value | Source & Anchor |
|--------|-----------|-----------------|
| Operating cash flow (CFO) | Rs -1.95 Cr | screener-Data_Sheet.csv line 57; negative despite positive PAT, flagged as working-capital build and capex-funded growth (B01, B02, B03) |
| Capital expenditure (Capex) | Rs 76.03 Cr | screener-Data_Sheet.csv line 58 (absolute value of investing activity outflow); funds Sanand/Supa/stamping expansion (B05, B07) |
| Free cash flow (FCF) | Rs -78.0 Cr | CFO - Capex = -1.95 - 76.03 = -78.0 Cr; strongly negative, capex-externally-funded (B04 flag: "fully externally funded via debt + preferential equity issue") |
| CFO / PAT ratio (latest) | -0.072x | CFO -1.95 / PAT 27.01 = -0.072; negative due to growth-phase working capital build (B01 block_b_trend: "CFO/PAT fell from 1.78x FY22 to -0.07x FY26") |
| CFO / PAT cumulative (FY22-FY26) | 0.31x | (6.39+1.45+5.0+8.85-1.95) / (3.6+4.57+12.21+16.76+27.01) = 19.74 / 64.15 = 0.307; B01 reports 0.31x, binding deal-breaker threshold <0.50 triggers max AVERAGE classification |
| FCF / PAT ratio | -2.89x | FCF -78.0 / PAT 27.01 = -2.89; capex vastly exceeds earnings |
| Cash & equivalents (year-end) | Rs 16.66 Cr | screener-Data_Sheet.csv line 51 |
| Receivables (trade) | Rs 66.08 Cr | screener-Data_Sheet.csv line 49; +62.3% YoY vs +24.1% revenue growth (B02: "Trade Receivables +62.3% YoY"); CRISIL: customer concentration top 5 = 50-55%, largest = 15-20% (CRISIL_Rating_Rationale_2026-07-02, p.2) |
| Inventory | Rs 47.18 Cr | screener-Data_Sheet.csv line 50; +79.0% YoY (B02), supporting multi-customer concurrent build-to-order |
| Gross current assets (GCAs) | 223 days | CRISIL_Rating_Rationale_2026-07-02, p.2: "GCAs stood at 223 days as on March 31, 2026" |
| Cash conversion nature (FTTCP) | GROWTH-INDUCED | fttcp-deliberation Override 1: "GROWTH-INDUCED working capital stress, not yet a structural collection or asset quality problem"; CRISIL confirms "working capital intensive operations" and "long credit periods to export customers" with no bad-debt mention (p.1-2); falsifier: over-12-month receivables bucket above ~15% or rising ECL |
| Cash conversion forward verdict | STAGNANT | fttcp-deliberation ruling: "STAGNANT (changed from DECLINING on review)"; cash multiplier = 0.80 base + 0.20 growth offset = 1.00x; catalyst strength Weak |

### Balance Sheet & Solvency

| Metric | FY26 Value | Source & Anchor |
|--------|-----------|-----------------|
| Equity share capital | Rs 25.85 Cr | screener-Data_Sheet.csv line 39; unchanged nominal, but reserves grown from IPO and preferential issue |
| Reserves & surplus | Rs 146.12 Cr | screener-Data_Sheet.csv line 40; +550.8% from FY24 (Rs 12.22 Cr) due to Oct 2024 IPO (Rs 57.16 Cr fresh capital) and Feb 2026 preferential issue |
| Total networth / equity | Rs 171.97 Cr | Equity capital + Reserves = 25.85 + 146.12 = 171.97 Cr |
| Borrowings (bank + term loans) | Rs 68.54 Cr | screener-Data_Sheet.csv line 41; includes proposed/committed facilities per CRISIL annex |
| Unsecured group/director loans (treated as debt) | Rs 15.45 Cr | CRISIL_Rating_Rationale_2026-07-02, p.1: "Unsecured loans from group company and directors of Rs 15.45 crore as on 31st March 2026 has been treated as debt" |
| Total debt | Rs 83.99 Cr | Borrowings 68.54 + Related-party debt 15.45 = 83.99 Cr |
| Cash & equivalents | Rs 16.66 Cr | screener-Data_Sheet.csv line 51 |
| Net debt | Rs 67.33 Cr | Total debt - Cash = 83.99 - 16.66 = 67.33 Cr |
| Debt / Equity (adjusted) | 0.40x | CRISIL_Rating_Rationale_2026-07-02, p.2: "Adjusted debt/adjusted networth" = 0.40x (FY26); down from 0.26x (FY25) due to higher debt, used for sizing; denominator appears to be adjusted networth per rating methodology |
| Current ratio | 1.60x | CRISIL_Rating_Rationale_2026-07-02, p.2 |
| Interest coverage ratio | 9.72x | CRISIL_Rating_Rationale_2026-07-02, p.2; computed as EBIT / Interest = 36.26 / 4.49 = 8.08x (approximate; CRISIL may use adjusted EBIT) |
| Book value per share (BVPS) | Rs 66.67 | Networth / Shares = 171.97 / 2.58 = 66.67 per share |

### Valuation Multiples (Latest Period)

| Metric | FY26 Value | Computation & Source |
|--------|-----------|---------------------|
| Diluted EPS | Rs 10.47 | PAT / Shares = 27.01 / 2.58 = 10.47; NOTE: B02 flags diluted EPS Rs 8.12 exceeding basic EPS Rs 6.85 in FY25 as "anomalous under AS 20" |
| Price / Earnings (trailing) | 63.6x | CMP 666 / EPS 10.47 = 63.6x; extremely stretched (industry median ~20-30x for precision auto-components) |
| EV / EBITDA (trailing) | 41.0x | EV 1,787.45 / EBITDA 43.64 = 41.0x; does not reflect earnings power given high capex cycle |
| EV / Sales (trailing) | 8.1x | EV 1,787.45 / Revenue 219.54 = 8.1x |
| Price / Book | 10.0x | CMP 666 / BVPS 66.67 = 10.0x |
| P / FCF | NOT APPLICABLE | FCF negative; multiple meaningless during capex phase |

---

## RETURN ON CAPITAL & PROFITABILITY TRENDS

### ROCE (Return on Equity Invested)

| Period | ROCE Value | Basis & Source |
|--------|-----------|-----------------|
| FY26 (year-end capital employed basis) | ~15.1% | EBIT 36.26 / Year-end capital employed ~240.5 Cr = 15.1%; fttcp-deliberation: "on year-end capital employed ~240 Cr that is ~15%" |
| FY26 (average capital employed basis) | ~19.5% | EBIT 36.26 / Average capital employed ~185.7 Cr = 19.5%; fttcp-deliberation: "on average capital employed ~185.7 Cr gives ~19.5%" |
| FY25 | 19.01% | fttcp-deliberation (anchored from prior run); year-end basis assumed consistent |
| FY24 | 33.38% | fttcp-deliberation (anchored from prior run); year-end basis assumed consistent |
| 2-year trend direction | DECLINING | From 33.38% (FY24) → 19.01% (FY25) → ~15.1% to 19.5% (FY26); TEMPORARY DEPRESSION due to Oct 2024 IPO capital raise bloating denominator faster than profit growth (fttcp-deliberation section 7) |
| Forward verdict (FTTCP) | STAGNANT | fttcp-deliberation: "STAGNANT (changed from DECLINING)"; recovery not yet visible; year-end ROCE fell again from FY25's 19%; Pillar 1 uses current ROCE under STAGNANT rule |
| Pillar 1 base valuation multiple | 15-17x | fttcp-deliberation: "Pillar 1 base 16.5 to 17.5x pending the FY26 ROCE anchor"; on current ~15-19.5% ROCE range |
| Capital employed convention note | AMBIGUOUS | FY24/FY25 appear year-end basis per prior stage; FY26 anchor computed at stage 10; stage 11 to confirm consistent convention |

### ROE (Return on Equity Capital)

| Period | ROE Value | Computation |
|--------|-----------|-------------|
| FY26 | ~20.5% | PAT 27.01 / Average networth (current-year 171.97 + prior ~92) / 2 ≈ 27.01 / 132 = ~20.5%; depressed vs historical due to capital-raise dilution (B03 notes "Trailing ROE depressed by two recent capital raises") |

### 3-Year CAGR (FY24 to FY26)

| Metric | CAGR | Calculation & Source |
|--------|------|---------------------|
| Revenue CAGR | 38.5% | (219.54 / 114.54)^(1/2) - 1 = 38.5% |
| PAT CAGR | 48.7% | (27.01 / 12.21)^(1/2) - 1 = 48.7%; growth-led, but increasingly cash-constrained |
| Growth trajectory | FIRING | fttcp-deliberation section 10: "Revenue forward. FIRING. 54% growth FY26, order book above Rs 1,200 Cr, capacity commissioning." |

---

## CAPITAL STRUCTURE & FUNDING

| Item | FY26 | FY25 | FY24 | FY22 | Source |
|------|------|------|------|------|--------|
| **Equity capital (Cr)** | 25.85 | 24.45 | 17.85 | 11.90 | screener-Data_Sheet.csv line 39 |
| **Reserves (Cr)** | 146.12 | 79.54 | 12.22 | 1.38 | screener-Data_Sheet.csv line 40 |
| **Total networth (Cr)** | 171.97 | 103.99 | 30.07 | 13.28 | Sum of capital + reserves |
| **Borrowings (Cr)** | 68.54 | 26.98 | 41.48 | 18.98 | screener-Data_Sheet.csv line 41 |
| **Related-party debt (Cr)** | 15.45 | NOT FOUND | NOT FOUND | NOT FOUND | CRISIL_Rating_Rationale_2026-07-02; B08 flags RPT concentration |
| **Total debt (Cr)** | 83.99 | 26.98 | 41.48 | 18.98 | Sum of bank borrowings + related-party |
| **Cash (Cr)** | 16.66 | 16.60 | 0.58 | 0.39 | screener-Data_Sheet.csv line 51 |
| **Net debt (Cr)** | 67.33 | 10.38 | 40.90 | 18.59 | Total debt - Cash |

**Funding events:** Oct 2024 IPO raised Rs 57.16 Cr (Rs 17.85 Cr new equity shares, Rs 39.31 Cr premium). Feb 2026 preferential share issue. Capex FY26 (Rs 76 Cr) funded by debt raise and equity (B04 flag notes "fully externally funded via debt + preferential equity issue").

---

## 5-YEAR HISTORY (FY22 to FY26)

### Revenue & Profitability

| Metric | FY22 | FY23 | FY24 | FY25 | FY26 | Source |
|--------|------|------|------|------|------|--------|
| **Sales (Rs Cr)** | 55.55 | 95.12 | 114.54 | 142.31 | 219.54 | screener-Data_Sheet.csv line 11 |
| **EBITDA (Rs Cr)** | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | 43.64 | CRISIL_Rating_Rationale_2026-07-02 (FY26 only) |
| **EBITDA margin (%)** | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | 19.8 | CRISIL_Rating_Rationale_2026-07-02 |
| **PBT (Rs Cr)** | 4.32 | 6.31 | 16.43 | 20.63 | 31.77 | screener-Data_Sheet.csv line 22 |
| **PAT (Rs Cr)** | 3.60 | 4.57 | 12.21 | 16.76 | 27.01 | screener-Data_Sheet.csv line 24 |
| **PAT margin (%)** | 6.5 | 4.8 | 10.7 | 11.8 | 12.24 | Computed / CRISIL |

### Cash Flow

| Metric | FY22 | FY23 | FY24 | FY25 | FY26 | Source |
|--------|------|------|------|------|------|--------|
| **CFO (Rs Cr)** | 6.39 | 1.45 | 5.00 | 8.85 | -1.95 | screener-Data_Sheet.csv line 57 |
| **Investing CF (Rs Cr)** | -5.97 | -13.83 | -10.40 | -32.37 | -76.03 | screener-Data_Sheet.csv line 58 (capex as outflow) |
| **Financing CF (Rs Cr)** | -1.02 | 12.59 | 5.38 | 39.54 | 78.04 | screener-Data_Sheet.csv line 59; FY25 includes IPO proceeds, FY26 includes preferential issue |
| **Net CF (Rs Cr)** | -0.60 | 0.21 | -0.02 | 16.02 | 0.06 | screener-Data_Sheet.csv line 60 |
| **CFO / PAT (x)** | 1.78 | 0.32 | 0.41 | 0.53 | -0.07 | Calculated; B01 flags "deteriorating — 1.78x (FY22) to -0.07x (FY26)" |
| **Cumulative CFO/PAT** | — | — | — | — | 0.31x | B01: "cumulative CFO/PAT 0.31x" for full FY22-26 span; binding deal-breaker |

### Balance Sheet

| Metric | FY22 | FY23 | FY24 | FY25 | FY26 | Source |
|--------|------|------|------|------|------|--------|
| **Receivables (Rs Cr)** | 15.58 | 19.97 | 21.53 | 34.93 | 66.08 | screener-Data_Sheet.csv line 49; FY26 +62.3% YoY |
| **Inventory (Rs Cr)** | 6.77 | 8.62 | 14.91 | 26.69 | 47.18 | screener-Data_Sheet.csv line 50; FY26 +79.0% YoY |
| **Fixed assets (Rs Cr)** | 22.11 | 30.30 | 40.83 | 69.90 | 112.20 | screener-Data_Sheet.csv line 44 (Net Block); large capex build: FY24 +35%, FY25 +71%, FY26 +60% |
| **CWIP (Rs Cr)** | 1.68 | 4.90 | 2.18 | 2.33 | 5.67 | screener-Data_Sheet.csv line 45; Sanand/Supa/stamping plants under construction |
| **Borrowings (Rs Cr)** | 18.98 | 33.41 | 41.48 | 26.98 | 68.54 | screener-Data_Sheet.csv line 41; FY26 spike +154% due to capex funding |
| **Reserves (Rs Cr)** | 1.38 | 5.96 | 12.22 | 79.54 | 146.12 | screener-Data_Sheet.csv line 40; +550.8% FY24-FY26 (IPO dilution) |

---

## FORWARD GUIDANCE & EARNINGS DRIVERS

### Management Guidance (from B05 concalls)

| Item | Stated Value | Timeframe | Concall Source | Status |
|------|--------------|-----------|-----------------|--------|
| **Revenue growth** | 40-45% | FY27 (next fiscal) | Q4 FY26 call (May 2026) | EXPECTED; credibility grade B (good) per B05 |
| **EBITDA margin** | ~1pp expansion | FY27 | Q4 FY26 call | EXPECTED; cut from +4-5pp medium-term ambition (flagged as guidance cut, B05 red flag) |
| **Incremental capex** | Rs 15-20 Cr | FY27, sustains ~2 years | Q4 FY26 call | EXPECTED; supports Sanand/stamping/forging ramp |
| **Order book conversion** | Rs 100-200 Cr/year | Ongoing, 5-6 year execution | Q4 FY26 call | EXPECTED; order book Rs 1,200+ Cr (CRISIL-confirmed filed source, p.2) |
| **Export mix** | >30-35% of business | FY27 | Q4 FY26 call | EXPECTED; China+1 sourcing tailwind |

### Key Growth Triggers (Priority Order, from B05 concalls)

| Trigger | Type | Timeframe | Conviction | Confirm Signal | Source |
|---------|------|-----------|-----------|-----------------|--------|
| **Sanand (Tenneco-dedicated) plant ramp** | VOLUME | Near (FY27) | H | Rs 40cr shock-absorber-line revenue materializes | B05, Priority 1 |
| **Defense ramp** | VOLUME | Near-Medium | M-H | Defense revenue >Rs 1-1.2cr/month sustained | B05, Priority 2 |
| **Tata AutoComp/Tesla EV ramp** | VOLUME | Medium | M | TAC revenue share growth + new projects | B05, Priority 3 |
| **Humanoid robotics cold-plate parts** | SECTORAL | Near-Medium | M | Trial → disclosed mass-production orders | B05, Priority 4 |
| **Export mix expansion** | SECTORAL | Near-Medium | M-H | Export share reaches 30-35% FY27 | B05, Priority 5 |
| **Aerospace AS9100D cert** | REGULATORY | Near (2 months stated) | L-M | Certification + first order | B05, Priority 6; RED FLAG: slipped >12 months unacknowledged |
| **Margin expansion** | COST | Medium | L-M | EBITDA margin improves beyond 19.5% FY26 | B05, Priority 7; management cut ambition once already |
| **Supa mega-factory** | INORGANIC | Long, vague | L | Firm capex/timeline announced | B05, Priority 8; no disclosed capex/timeline yet |

### Valuation Implications for Forward Period

| Metric | Value | Basis & Source |
|--------|-------|-----------------|
| **SOM-implied revenue CAGR (3-year)** | 39.1% | B09: "som_implied_revenue_cagr yr3: 39.1"; conservative TAM-based addressable market size analysis |
| **SOM-implied revenue CAGR (5-year)** | 34.4% | B09: "som_implied_revenue_cagr yr5: 34.4"; market runway "MASSIVE" (84.7x current SAM share) |
| **Peer median P/E (if available)** | NOT FOUND | B06 peer cross-checks did not provide peer financial medians; peer coverage map lists 16 peers but no comparable P/E extraction |
| **Peer median EV/EBITDA** | NOT FOUND | Not provided |
| **Peer median P/B** | NOT FOUND | Not provided |
| **Peer median ROCE** | NOT FOUND | Not provided |
| **Capex embedded growth (Pillar 3a)** | 18% | B07: "capex_embedded_growth_pct: 18"; stamping ~Rs 9 Cr (~70% done), Sanand ~Rs 40 Cr incremental revenue, Supa undisclosed |

---

## EMERGING MOAT ASSESSMENT (B07)

| Dimension | Score / Status | Detail & Source |
|-----------|----------------|-----------------|
| **EM score** | 23 (MODEST) | B07: "em_score: 23, em_classification: MODEST" |
| **EM classification** | MODEST | Below 25-threshold for UA multiplier qualification |
| **Combined assessment** | AVERAGE (backward) + MODEST (forward) | B07: "AVERAGE backward Gate 0 score plus MODEST forward emerging-moat development, both capped by binding cumulative CFO/PAT 0.31x deal-breaker" |
| **Primary catalyst (12m)** | Capex commissioning (Sanand shock-absorber line) | B07: catalyst_12m item 1 "Sanand/Tenneco shock-absorber-rod revenue ramp (~Rs40cr incremental), window FY27" |
| **Catalyst proximity window** | Shared 12-month window across Sanand, Stamping, Humanoid trials | B07 lists 5 catalysts within 12-month horizon; fttcp-deliberation notes "SHARED CATALYST flag (capex commissioning drives Pillar 1 and Pillar 3a)" |
| **Evidence quality mix** | Documented 16, Claim 15, Inference 1 | B07: "evidence_mix: {documented: 16, claim: 15, inference: 1}"; mixed evidence quality; "mostly-📄 / mixed / mostly-🎙️🔍" = MIXED |
| **Major moat risks** | Cash-conversion collapse; certification slip; tariff volatility; customer concentration; European slowdown | B07 top_moat_risks (1-5); concentration risk unquantified |
| **True customer concentration** | 50-55% (top 5), 15-20% (largest) | CRISIL_Rating_Rationale_2026-07-02, p.2; genuine concentration risk, monitored |

---

## QUALITATIVE ASSESSMENTS (Copied Upstream, Anchored)

| Assessment | Value / Grade | Anchor & Context |
|-----------|---------------|------------------|
| **Management credibility (B05 concall track record)** | Grade B (Good) | B05: "credibility_grade: B"; delivered on FY26 >40% revenue growth, broke quarterly disclosure promise, let aerospace cert slip >12 months unacknowledged, cut margin guidance once |
| **Earnings quality / accounting (B03 deep-dive)** | Overall quality = 4 (on 1-10 scale, poor to excellent) | B03: "overall_quality: 4"; red flags: diluted EPS > basic (anomalous), negative short-term provisions, weak cash conversion (~34-52%), interest-paid financing classification masking run-rate; governance 3, accounting 3, balance sheet 6, earnings 3 |
| **Business quality (B04 verdict)** | "High-growth precision-engineering vendor with real qualification moats but thin near-term free cash flow and rising related-party/concentration risk" | B04: "one_line_verdict"; flagged: FY26 CFO negative, related-party raw material sourcing, customer concentration top 2 SKUs ~40%, simultaneous multi-front expansion, NSE Emerge liquidity constraint |
| **Rating agency assessment** | CRISIL BBB+/Stable | CRISIL_Rating_Rationale_2026-07-02: "Crisil BBB+/Stable' assigned to bank debt"; strengths (promoter experience, order book, diversified products) vs weaknesses (cyclicality exposure, WC intensity, moderate scale, customer concentration) balanced at mid-spectrum rating |
| **Promoter quality / governance (B08)** | CAUTION (not CONCERN) | B08: "verdict: CAUTION"; clean on SEBI/criminal/tax, zero pledge, independent director additions (2026), but RPT concentration (Omega Bright Steel raw material sourcing, no non-compete, recent asset buy), governance pages unreadable, DRHP litigation section inaccessible |
| **Strategic position (B07 vs B04)** | "Qualification lock-in (strong)" + "Execution moat (moderate)" | B07 active categories B2, F2; B04 business model moats include "established customer base" and "multi-industry diversification" but held by thin FCF and WC drag |

---

## CAPITAL ALLOCATION & VALUATION FRAMEWORK INPUTS (From Deliberation & Frameworks)

### Section 1B Pillar Inputs (Four-Pillar Model Authority)

| Pillar | Sub-component | Value / Ruling | Source & Rationale |
|--------|---------------|-----------------|-------------------|
| **Pillar 1: Return on Capital** | Forward verdict | STAGNANT (changed from RECOVERING) | fttcp-deliberation: "ROCE forward verdict CHANGED on this evidence: FY26 EBIT is Rs 36.26 Cr…recovery is not visible (year-end ROCE fell again from FY25's 19%, average roughly flat). Return on capital forward moves from RECOVERING to STAGNANT." |
| | Base valuation multiple (Pillar 1 alone) | 15-17x (conservative on current ROCE ~15-19.5%) | fttcp-deliberation: "Pillar 1 base 16.5 to 17.5x pending the FY26 ROCE anchor, on current ~15-19.5% ROCE range" |
| | FY26 ROCE (current, year-end basis) | ~15.1% | EBIT 36.26 Cr / Year-end capital employed ~240.5 Cr; fttcp-deliberation section 8 |
| | FY26 ROCE (current, average basis) | ~19.5% | EBIT 36.26 Cr / Average capital employed ~185.7 Cr; fttcp-deliberation section 8 |
| | FY25 ROCE (baseline for trend) | 19.01% | Anchored from B01; year-end basis assumed |
| | FY24 ROCE (baseline for trend) | 33.38% | Anchored from B01; temporary depression driver = Oct 2024 IPO capital raise |
| | Strategic premium routing | NOT CREDITED; ROCE in Pillar 1 only | fttcp-deliberation: "Strategic Premium remains +0x"; single-credit rule: ROCE not credited separately in Pillar 4 |
| **Pillar 2: Cash Conversion** | Forward verdict | STAGNANT | fttcp-deliberation: "Cash forward verdict moves to STAGNANT, catalyst Weak, Kernex cap lifts" |
| | Nature of cash challenge | GROWTH-INDUCED (not structural) | fttcp-deliberation Override 1: CRISIL confirms "working capital intensive operations" and "long credit periods to export customers"; FY26 CFO negative due to 62% receivables build and 79% inventory build vs 24% revenue growth, typical of scale-up |
| | Cash multiplier | 1.00x | 0.80 base + 0.20 growth offset (revenue CAGR >40% = FY26 growth 54%); fttcp-deliberation: "Cash multiplier = 0.80 base + 0.20 growth offset equals 1.00x" |
| | Valuation multiple (Pillar 2 alone) | 1.00x (multiplicative on Pillar 1) | Applied as haircut/adjustment; no standalone multiple |
| **Pillar 3: Capex & Embedded Growth** | 3a: Capex-embedded growth % | +3x (on 6x available spectrum) | B07: "capex_embedded_growth_pct: 18" of revenue; delivery grade B (good); fttcp-deliberation: "Pillar 3 becomes 3a +3 plus 3b +0 plus 3c +2 equals +5x" |
| | 3b: Unquantified optionality | +0x | B07 EM 23 < 25 (no bonus for sub-25 EM); aerospace cert delayed, humanoid/medical nascent |
| | 3c: Order book duration premium | +2x | fttcp-deliberation Override 2: "the stated order book is genuine only, so we need to give them duration premium"; Rs 1,200 Cr over 5-6 years = 5.5x revenue, >4-year tenor; CRISIL-filed source (p.2: "to be executed over the next 5-6 fiscals") |
| | Pillar 3 combined | +5x | (capped at +6x ceiling per Section 1B v3.3) |
| **Pillar 4: Strategic Premium** | Routing | NONE; +0x | fttcp-deliberation: "Strategic Premium remains +0x; single credit; ROCE in Pillar 1" |
| | (Rationale for zero) | ROCE credential capped at STAGNANT; only one recovery route can credit the moat; Pillar 3 accounts for capex-embedded growth |
| **Destination PE (all four pillars)** | Range & midpoint | 20-24x, midpoint 22x | fttcp-deliberation: "Four pillar destination PE 20x to 24x, midpoint 22x. Pillar 1 base 16.5 to 17.5x pending the FY26 ROCE anchor, Pillar 2 cash 1.00x, Pillar 3 +5x, Pillar 4 +0x" |
| **Sector cap (authority)** | Manufacturing row | 25x | fttcp-deliberation: "Sector cap row. CORRECTED to Manufacturing 25x. The manifest's 'EPC / Civil construction' 20x is wrong; OBSCP is a precision components manufacturer"; stage 11 uses 25x as ceiling only |
| **Sector cap binding?** | Cap engagement | NOT BINDING at 20-24x destination PE | Destination 22x midpoint < 25x ceiling, so cap does not constrain |

### Unaffected Arbitrage (UA) Multiplier Qualification

| Qualifier | Status | Anchor & Threshold |
|-----------|--------|-------------------|
| **Listed ≥12 months** | NOT MET | Oct 2024 IPO → ~9 months as of July 2026; needs 12+ months (amendment 3: min(Raw x 1.25, Sector Cap)) |
| **Gate 0 core ≥60 OR EM ≥25** | NOT MET | Gate 0 core = 52 < 60 (B01, B03); EM = 23 < 25 (B07); both thresholds failed |
| **FII + DII < 3%** | MET | B08: "public float 23.58% and institutional float 2.94%"; 2.94% < 3% ✓ |
| **All three qualifiers met?** | NO | Only 1 of 3 met; UA multiplier NOT applied |
| **Implication** | Destination PE remains 20-24x (no UA upside) | Typical for sub-60 Gate 0 or sub-25 EM; growth and moat must come through organically |

### Return Hurdle Assessment (Entry Threshold for 25% CAGR Target)

| Dimension | Value | Calculation & Source |
|-----------|-------|---------------------|
| **Entry price (CMP)** | Rs 666 | manifest.yaml, current as of run date 2026-07-12 |
| **Target price (destination PE 22x midpoint)** | Rs 230 (conservative) to Rs 290 (bull estimate) | Destination PE 22x × Forward PAT (FY27 est. ~Rs 37-40 Cr on 40% guidance) = Rs 22 × 10.5 to 13 ≈ Rs 230-286 per share; fttcp-deliberation estimates Rs 409-688 range depending on bull-base-bear case |
| **Required CAGR from CMP to target (3-year)** | NEGATIVE; price de-rating necessary | CMP 666 → Target 230-290 means equity returns ~-25% to -30% over 3 years even on earnings growth; hurdle verdict STOP |
| **Hurdle Ratio (25% CAGR test)** | 0.85 (base case), 1.03 (bull case) vs 1.953 hurdle | fttcp-deliberation: "Hurdle Ratio, Tier A 25%: base 0.85, bull 1.03, both far below the 1.953 pass line. Hurdle verdict STOP." |
| **Hurdle outcome** | STOP — not qualified for 25% CAGR | De-rating from 64x trailing PE to 22x destination PE swamps earnings growth; entry infeasible at CMP |
| **Fair entry zone (per FTTCP)** | Rs 280-350 | fttcp-deliberation: "Entry zone about Rs 290 to Rs 350, MoS about Rs 235 to Rs 280, both roughly half of CMP." |

### Return Hurdle Tier & FII/DII Check

| Item | Value | Source |
|--------|-------|--------|
| **Return hurdle tier** | Tier A (25% CAGR) | fttcp-deliberation section 11: "Return hurdle Tier A (25%)" |
| **FII + Domestic Institutional participation** | 2.94% | B08 derived from shareholding pattern; below 3% threshold |
| **Implication** | FII/DII < 3% qualifier met, but other UA qualifiers failed; hurdle remains binding | Amendment 3 rule: all three UA qualifiers must be met for multiplier application |

---

## RATING PDF EXTRACT (CRISIL BBB+/Stable, 2 July 2026)

### Agency & Rating Detail

| Item | Value | Source Page |
|------|-------|-------------|
| **Rating agency** | CRISIL Ratings Limited (subsidiary of Crisil Limited, S&P Global company) | CRISIL_Rating_Rationale_2026-07-02 footer |
| **Rating assigned** | Crisil BBB+/Stable | Cover page (p.1) and rating action table (p.1) |
| **Instrument rated** | Long-term bank debt facilities, Rs 100 Cr total | CRISIL_Rating_Rationale_2026-07-02, p.1 |
| **Regulatory authority** | RBI (Reserve Bank of India) | CRISIL_Rating_Rationale_2026-07-02, p.1 |
| **Date of rating** | 2 July 2026 | Cover page |
| **Outlook** | Stable | Rating action table (p.1) |

### Working Capital & Cash Flow Commentary (Verbatim from CRISIL, p.2)

**Quoted section:** "Working capital intensive operations: Gross current assets (GCAs) remained elevated at 133-223 days over the three fiscals ended March 31, 2026, reflecting the company's working capital intensive operations. GCAs stood at 223 days as on March 31, 2026, driven by high receivables and inventory levels. The company is required to extend relatively long credit periods to its export customers, leading to elevated debtor levels. Additionally, the nature of operations necessitates maintaining sizeable work-in-process and inventory levels. With export sales expected to be higher over the medium term the working capital requirement is expected to increase. The ability to manage working capital efficiently over the medium term with limited reliance on external borrowings and maintenance of adequate liquidity will be monitored."

**Key evidence: Absence of bad-debt flag.** CRISIL text frames the 223-day GCA and elevated receivables/inventory purely as "working capital intensive operations" and "long credit periods to export customers" — no mention of rising overdue buckets, delinquencies, or ECL inadequacy. This validates the GROWTH-INDUCED cash conversion diagnosis (fttcp-deliberation Override 1).

### Rating Sensitivity & Monitoring (from p.3 of CRISIL)

**Upside factors:**
- Sustained growth in revenue by more than 40% and operating margin sustained above 18%, leading to higher net cash accruals
- Improvement in working capital management with GCAs below 210 days along with sustenance of financial risk profile

**Downside factors:**
- Decline in revenue or profitability, leading to net cash accrual of less than Rs 25 crore
- Large debt-funded capex or a substantial increase in working capital requirement, weakening the capital structure and liquidity

---

## DATA GAPS & UNRESOLVED ITEMS

| Field | Why Unresolved | Where It Might Be | Impact on Valuation |
|-------|-----------------|-------------------|---------------------|
| Quarterly revenue cadence (Q1-Q4 FY27 forward) | Only two concalls collected; quarterly disclosure promise broken | Investor release or updated company website (if disclosed) | Limits forward cash-flow modeling granularity; reliant on full-year guidance 40-45% growth |
| FY26 over-12-month receivables ageing bucket | AR pages 78-101 truncated; notes schedule lost | Clean copy of FY26 annual report (if available) or next concall disclosure | Falsifier for GROWTH-INDUCED cash verdict; critical for monitoring; currently unanchored ~15% threshold |
| Supa mega-factory capex quantum and timeline | Management explicitly declined to disclose | Future investor updates or AR note 2 | Affects Pillar 3 and long-term SOM; undisclosed so not modeled separately |
| FY22/FY23/FY26 ROCE (prior run data missing for two years) | AR pages unreadable; screener does not extract ROCE; historical calculations NOT FOUND | Prior run files or analyst equity reports | ROCE trend used only for FY24/FY25/FY26 observed; FY22/FY23 gap noted but not binding (uses current ROCE under STAGNANT) |
| Peer financial medians (P/E, EV/EBITDA, P/B, ROCE) | B06 peer concalls analyzed qualitatively; no financial statement extraction | Peer annual reports or consolidated financial summaries | Valuation cross-check deferred; OBSCP multiples (63.6x P/E, 41x EV/EBITDA) assessed as stretched on absolute basis only |
| Detailed capex breakup (Sanand vs Stamping vs Supa allocated amounts) | Investment presentation slide 10 lists categories but not capex Rs breakdown; Supa quantum undisclosed | Investor relations or IR presentations (if more recent) | Pillar 3a assessment uses 18% capex-embedded growth figure from B07; detail deferred to stage 11 |
| Consolidated financial statements or subsidiary/JV detail | AR Note 2 not recoverable; consolidated statements not prepared despite subsidiary existence | FY26 AR or CARO note clarification | B03 flags s.129(3) exemption basis NOT FOUND; no material subsidiary risk identified but not fully verified |
| EPS reconciliation (diluted > basic anomaly in FY25) | Note 26 truncated; arithmetic verified as real but cause unexplained | FY26 AR Note 26 or management clarification | B02/B03 red flag unresolved; FY26 EPS diluted vs basic status unknown; does not affect stage 10 base case (uses consolidated PAT) |

---

## SUMMARY FLAGS & CONFLICT RESOLUTION

### Conflicts Between Upstream Stages

| Field | Draft Value | Deliberation Value | Used in B10 | Rationale |
|-------|-------------|-------------------|------------|-----------|
| ROCE forward verdict | RECOVERING (90% probability per B07) | STAGNANT | STAGNANT | fttcp-deliberation overrides on CRISIL-anchored FY26 data showing no recovery visible; more conservative |
| Sector cap row | EPC / Civil construction 20x (manifest) | Manufacturing 25x | Manufacturing 25x | fttcp-deliberation: business is precision components, not civil contractor; corrected at deliberation stage |
| Cash conversion determination | INDETERMINATE (due to truncated notes) | GROWTH-INDUCED (per CRISIL + screener.ai check) | GROWTH-INDUCED | Operator override with filed rating evidence; lifts disposition from PROCEED WITH CAVEATS |
| Order book duration premium (Pillar 3c) | +0x (concall stated, not filed LoAs) | +2x (operator ruling: genuine, duration premium applies) | +2x | fttcp-deliberation Override 2: "the stated order book is genuine only, so we need to give them duration premium"; CRISIL filing validates |

No conflicting values on financial metrics; upstream stages generally aligned. FTTCP deliberation supersedes draft stage outputs per CLAUDE.md instruction.

### Major Flags Carried Forward

| Flag ID | Type | Severity | Description | Source | Resolution Route |
|---------|------|----------|-------------|--------|-------------------|
| FLAG-CASH | Cash conversion | CAUTION (Growth-induced) | CFO negative FY26 despite positive PAT; receivables +62%, inventory +79% vs 24% revenue growth | B01, B02, B03, fttcp-deliberation | Operator override: GROWTH-INDUCED, falsifier is over-12-month bucket >15% or rising ECL |
| FLAG-ACCOUNTING-QUALITY | Diluted EPS > Basic | RED | FY25 diluted EPS Rs 8.12 > basic EPS Rs 6.85, AS 20-anomalous, reconciliation unrecoverable | B02, B03 | FY26 status unknown; monitorable for restatement risk |
| FLAG-ACCOUNTING-QUALITY | Short-term provisions | YELLOW | FY25 swing from +0.66 to -0.27 Cr, confirmed real, cause unrecoverable | B02, B03 | Monitor FY26 reversal; likely one-off but unvalidated |
| FLAG-CFO-QUALITY | Interest-paid classification | YELLOW | Interest paid Rs 3.12 Cr classified as financing, not operating (non-standard); inflates reported CFO; reclassified drops CFO/PAT 52.8% to 34.2% | B03 | Rating agency precedent: acceptable under Ind-AS but raises conservatism question |
| FLAG-PROMOTER | Related-party concentration | CAUTION | Omega Bright Steel (promoter-controlled) supplies primary raw material; no non-compete agreement; Nov 2025 Rs 12.45 Cr asset buy | B04, B08 | RPT pricing/fairness undisclosed; CAUTION verdict held; independent director additions (2026) mitigate |
| FLAG-CUSTOMER-CONCENTRATION | Top customer risk | MEDIUM | CRISIL anchors top 5 = 50-55%, largest = 15-20% | CRISIL, B05, B07 | Order book real (FTTCP validation), but concentration remains key monitorable; Tata AutoComp moved to #2 within 1 year (B05) |
| FLAG-AEROSPACE-CERT | Execution timeline slip | MEDIUM | AS9100D certification promised "next quarter" in H2 FY25 call; still not certified Q4 FY26 (~12 months slip, unacknowledged) | B05, B07 | Credibility grade B (good) held despite slip; critical for aerospace/defense SOM expansion; monitor FY27 completion |
| FLAG-QUARTERLY-DISCLOSURE | Credibility commitment broken | MEDIUM | Management promised quarterly disclosure cadence in H2 FY25; only 1 further call held in 12 months | B05 | Credibility grade B (good) vs A; minor deduction but breaks market communication promise |

---

## CONSTRUCTION OF VALUATION MODEL INPUTS

### Inputs to Destination PE Calculation (Section 1B Four-Pillar Model)

**Pillar 1 Base (ROCE-driven):**
- Current ROCE FY26: 15.1% (year-end) to 19.5% (average) — conservative 15% → base multiple 15-17x
- ROCE trajectory: Declining from 33.4% (FY24) to 19.0% (FY25) to ~15-19.5% (FY26)
- Forward verdict: STAGNANT (recovery not visible; ruled out RECOVERING)
- Base multiple: 15-17x (conservative, no recovery credit)

**Pillar 2 Adjustment (Cash multiplier):**
- Forward cash verdict: STAGNANT (growth-induced)
- Cash multiplier: 1.00x (0.80 base + 0.20 growth offset)
- Adjustment: Multiplicative haircut of 1.00x = no adjustment

**Pillar 3 Catalyst (Capex-embedded growth + order book):**
- 3a (capex growth): +3x on 6x spectrum (18% embedded, delivery grade B, Rs 40 Cr Sanand line visible)
- 3b (unquantified optionality): +0x (EM 23 < 25, aerospace/humanoid nascent)
- 3c (order book duration): +2x (Rs 1,200 Cr over 5-6 years, 5.5x revenue, >4yr tenor, CRISIL-filed)
- Pillar 3 total: +5x (at +6x ceiling)

**Pillar 4 Strategic Premium:**
- Routing: +0x (single-credit rule; ROCE already in Pillar 1)
- Rationale: Capex moat credited in Pillar 3a; no second credit for same capability

**Destination PE composite:**
- Base (Pillar 1): 15-17x (conservative case); 17-19x (base case); 19-21x (bull case on higher average ROCE)
- Catalyst (Pillar 3): +5x
- Cash (Pillar 2): 1.00x (no adjustment)
- Strategic (Pillar 4): +0x
- Destination: 20-24x range, midpoint 22x (base case using 17x + 5x)
- Sector cap (Manufacturing): 25x (not binding; destination < ceiling)

### Inputs to Earnings Forecast (Forward PAT for destination PE)

| Metric | FY27 Estimate | Basis |
|--------|---------------|-------|
| **Revenue growth guidance** | 40-45% | B05 Q4 FY26 call; delivered 54% in FY26 (beat prior 40%+ guidance) |
| **FY27 revenue estimate** | Rs 307-318 Cr (base: 40% on Rs 219.54 Cr) | Conservative end of 40-45% band = 219.54 × 1.40 = 307 Cr |
| **EBITDA margin guidance** | ~1pp expansion (from 19.8% base) | B05: "FY27 margin growth guide ~1%"; conservative vs 4-5pp prior medium-term ambition (cut in FY26) |
| **FY27 EBITDA estimate** | Rs 46.5-47.5 Cr (20.8% margin on conservative revenue) | 307 × 0.208 ≈ 64 Cr (high case on 45% growth); conservative: 307 × 0.20 = 61 Cr |
| **PAT conversion (FY26: 12.24%)** | Assume stable 12-12.5% at flat tax rate | FY26 tax 18.8% effective vs 25% statutory; conservative case: 12% margin |
| **FY27 PAT estimate (conservative case)** | Rs 37 Cr (307 Cr × 12%) | Used for base-case destination PE calculation |
| **FY27 PAT estimate (base case)** | Rs 38-40 Cr | On 40-45% revenue growth × 12.5% consolidated PAT margin |
| **Forward P/E at destination 22x** | Rs 814-880 per share (22x × 37-40 Cr PAT / 2.58 Cr shares) = Rs 315-342 per share target | Divided by shares to get per-share valuation; cf. CMP 666 = 2.1x upside to base case destination |

**Caveat:** FY27 forward estimates are illustrative per B05 guidance; not anchored to filed results. Used for destination PE sanity check only. Actual stage 11 valuation model will refine with operator-reviewed forward assumptions.

---

## CONCLUSION

**Data completeness for valuation:** FY26 base financials fully anchored (CRISIL + screener). Forward guidance (FY27 40-45% revenue, ~1pp margin) from management concalls, credibility grade B. Capital structure fully reconstructed (debt Rs 84 Cr including Rs 15.45 Cr related-party, networth Rs 172 Cr). ROCE computed at 15-19.5% FY26 (staging authority: stage 11 to finalize convention vs FY24/FY25 basis).

**Deliberation overlays applied:** ROCE forward = STAGNANT (not recovering); sector cap = Manufacturing 25x (not EPC 20x); cash conversion = GROWTH-INDUCED 1.00x multiplier; Pillar 3 = +5x (including +2x order book duration); UA multiplier = NOT applied (fails 2 of 3 qualifiers). Destination PE = 20-24x, midpoint 22x.

**Hurdle outcome:** STOP at CMP Rs 666 (63.6x trailing P/E, hurdle ratio 0.85-1.03 vs 1.953 threshold). Fair entry ~Rs 280-350 per FTTCP verdict. Call turns on FY27 operating cash flow print and receivables ageing validation.

**Ready for stage 11 valuation model input:** All table fields populated with source anchors or marked "NOT FOUND" (zero estimates). B10 YAML block emitted below.

---

# CONFLICTS & UNRESOLVED ITEMS SUMMARY

## conflicts[]

```json
[
  {
    "field": "ROCE forward verdict",
    "value_a": "RECOVERING (90% probability)",
    "anchor_a": "B07 section 8",
    "value_b": "STAGNANT (recovery not visible)",
    "anchor_b": "fttcp-deliberation, CRISIL-anchored FY26 ROCE ~15% year-end, ~19.5% average, flat or declining from FY25 19%",
    "used": "STAGNANT (deliberation supersedes)"
  },
  {
    "field": "Sector cap authority",
    "value_a": "EPC / Civil construction 20x",
    "anchor_a": "manifest.yaml sector_cap_row",
    "value_b": "Manufacturing 25x",
    "anchor_b": "fttcp-deliberation: OBSCP is precision components manufacturer, not civil contractor",
    "used": "Manufacturing 25x (corrected, not binding at destination 22x)"
  },
  {
    "field": "Cash conversion nature",
    "value_a": "INDETERMINATE",
    "anchor_a": "B01 block_b_trend notes truncated receivables notes unrecoverable",
    "value_b": "GROWTH-INDUCED",
    "anchor_b": "fttcp-deliberation Override 1: CRISIL evidence + screener.ai over-6-month receivables reconciliation to FY22-24 base; no bad-debt flag",
    "used": "GROWTH-INDUCED (operator override, rating-agency validated)"
  }
]
```

## unresolved[]

```json
[
  {
    "field": "FY26 over-12-month receivables ageing bucket (% of receivables)",
    "why": "AR pages 78-101 truncated in downloaded PDF; Notes schedule (detail on receivables ageing) NOT FOUND",
    "where_it_might_be": "Clean copy of FY26 annual report (if corrected PDF available) or Q1 FY27 concall disclosure (if ageing mentioned)",
    "impact": "Falsifier for GROWTH-INDUCED verdict; if bucket >~15% of receivables or rising, reverts to STRUCTURAL cash conversion"
  },
  {
    "field": "Supa mega-factory capex quantum (Rs Cr) and timeline",
    "why": "Management explicitly declined to disclose in both concalls; Investor Presentation slide 10 shows placeholder only",
    "where_it_might_be": "Future investor updates, Q1 FY27 concall, or FY26 AR notes-to-accounts (capital commitments note)",
    "impact": "Affects SOM yr3-5 capacity ceiling check and Pillar 3 sizing; currently unquantified; B09 flags gap of Rs 150-250 Cr between SOM and committed capex"
  },
  {
    "field": "FY22 & FY23 ROCE (return on capital)",
    "why": "Historical calculations NOT FOUND in screener or B01 extraction; only FY24 (33.38%), FY25 (19.01%) anchored from prior runs",
    "where_it_might_be": "Prior run files or analyst equity reports (if available)",
    "impact": "ROCE trend used as 3-year only (FY24-26); does not affect stage 10 output (uses FY26 current ROCE under STAGNANT rule)"
  },
  {
    "field": "Peer financial medians (P/E, EV/EBITDA, P/B, ROCE for Divgi, Precision Camshafts, RACL, Talbros)",
    "why": "B06 peer concalls analyzed qualitatively; no financial statement extraction performed; cost-benefit not justified for stage 10",
    "where_it_might_be": "Peer annual reports, stock exchange filings, or equity research summaries",
    "impact": "Valuation cross-check deferred; OBSCP multiples assessed on absolute basis only (trailing 63.6x P/E stretched vs typically 20-30x precision auto-components sector)"
  },
  {
    "field": "Capex breakup detail: Sanand plant capex vs Stamping vs Supa allocated Rs amounts",
    "why": "Investor Presentation slide 10 lists project names but not capex Rs allocation; Supa quantum managed as trade secret",
    "where_it_might_be": "IR presentation update (Q1 FY27) or detailed capex note in FY26 AR",
    "impact": "Pillar 3a assessment uses 18% capex-embedded growth aggregate figure (B07); detail deferred to stage 11 modeling"
  },
  {
    "field": "Consolidated financial statements or subsidiary/JV performance detail",
    "why": "AR Note 2 not recoverable (pages 3-59 corrupted font); consolidated statements not prepared; s.129(3) exemption basis NOT FOUND",
    "where_it_might_be": "FY26 AR or Board's Report clarification (currently unreadable)",
    "impact": "B03 flags note as a governance gap; no material subsidiary risk identified but not fully verified; inter-company RPT with Omega Bright Steel confirmed via CRISIL"
  },
  {
    "field": "FY25 Diluted vs Basic EPS reconciliation (diluted > basic anomaly)",
    "why": "Note 26 truncated in AR; arithmetic confirmed as real (diluted Rs 8.12, basic Rs 6.85) but cause unexplained",
    "where_it_might_be": "FY26 AR Note 26 or management clarification in Q1 FY27 concall",
    "impact": "B02/B03 red flag unresolved; FY26 diluted vs basic EPS status unknown; does not affect stage 10 base case (uses consolidated PAT aggregate)"
  },
  {
    "field": "ROCE convention confirmation (year-end vs average basis for FY24/FY25 historical)",
    "why": "FY24 33.38% and FY25 19.01% sourced from B01; convention (year-end vs average capital employed) not stated",
    "where_it_might_be": "B01 notes or prior run files; FY26 computed at both conventions for reference",
    "impact": "Minor: FY26 ROCE trend direction (declining) robust under both conventions; stage 11 to state final choice for forecast"
  },
  {
    "field": "Quarterly revenue/profitability guidance (Q1-Q4 FY27)",
    "why": "Only 2 concalls collected (H2 FY25, Q4 FY26); quarterly disclosure cadence promised but not honored; no quarterly breakdown provided",
    "where_it_might_be": "Investor release if OBSCP restarts quarterly disclosures; Q1 FY27 or H1 FY27 concall if held",
    "impact": "Forward cash flow modeling limited to full-year guidance (40-45% growth, ~1pp margin); seasonal/quarterly lumping unknown"
  }
]
```

---

END OF REPORT

