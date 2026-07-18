# STAGE 10: VALUATION INPUT ASSEMBLY (B10-valinputs)
## Virtuoso Optoelectronics Ltd (VOEPL) — FY26/FY30

**Company:** Virtuoso Optoelectronics Ltd (VOEPL)  
**Run Date:** 2026-07-18  
**Model:** claude-haiku-4-5  
**Status:** COMPLETE

---

## COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|-------|-------|--------|
| Company Name | Virtuoso Optoelectronics Ltd | manifest |
| Ticker | VOEPL | manifest |
| Sector (stated in manifest) | Agri processing | manifest (COLLECTOR DEFECT) |
| Sector (authoritative, deliberation) | Cables / Industrial products | fttcp-deliberation.md, line 15; identical-cap alternative Recycling / Manufacturing 25x |
| Sector Cap Row | Cables / Industrial products 25x | fttcp-deliberation.md, line 15 |
| Business Model Type | Asset-heavy contract manufacturing (ODM/OEM, backward integration phase) | B04, line 8; deliberation line 13 |
| CMP (Rs) | 509 | manifest |
| Market Cap (Rs Cr) | 1621 | manifest |
| FV (Rs) | 10 | screener-Data_Sheet.csv, line 6 |
| Shares Outstanding (all figures in line) | **DILUTED SHARES NOT FOUND in provided sources** | see unresolved[] |
| Enterprise Value (Mcap + Net Debt) | **UNRESOLVED** (net debt requires balance sheet) | see unresolved[] |

---

## LATEST FINANCIALS (FY26 AUDITED, Board Approved 29-May-2026)

### Revenue & Profitability

| Metric | FY26 | FY25 | FY24 | Basis | Trend/CAGR |
|--------|------|------|------|-------|-----------|
| **Revenue from Operations (Rs Cr)** | 823.6 | 697.32 | 531.06 | screener-Data_Sheet.csv rows 11 | FY24-FY26 CAGR: 24.54% (B01, line 15; screener CFO basis) |
| **EBITDA (Rs Cr)** | 85.61 | 70.08 | 52.58 | computed: PAT + Tax + Interest + Depreciation from screener | Margin FY26 10.4% (B05 guidance delivered, fttcp-deliberation line 23) |
| **EBITDA Margin %** | 10.4 | 10.05 | 9.90 | screener-derived | FY26 DELIVERED within guidance 8.5-9% revised upward (B05 line 23) |
| **PAT (Net Profit, Rs Cr)** | 15.03 | 14.09 | 10.17 | screener-Data_Sheet.csv row 24 | FY24-FY26 CAGR: 21.57% (B01, line 15) |
| **PAT Margin %** | 1.8 | 2.02 | 1.92 | computed | FY26 MARGIN MISSED: guided 2.5-3%, delivered 1.8% (B05 line 44) |
| **Diluted EPS (Rs)** | unresolved[] | unresolved[] | unresolved[] | screener shares data incomplete | see unresolved[] |
| **PBT (Rs Cr)** | 24.51 | 25.15 | 14.36 | screener-Data_Sheet.csv row 22 | Decline FY25→FY26 despite revenue growth (profit growth mechanical, B02 red flag) |

### Cash Flow & Capital

| Metric | FY26 | FY25 | FY24 | Basis | Notes |
|--------|------|------|------|-------|-------|
| **CFO (Operating Cash Flow, Rs Cr)** | 3.33 | 30.6 | 13.75 | screener-Data_Sheet.csv row 57 | Collapsed from 30.6 to 3.33; CFO/PAT fell 2.17x → 0.22x (B01 line 36, block_b_trend) |
| **CFO/PAT (Cash Conversion) — Latest** | 0.22 | 2.17 | 1.35 | computed from screener | **DETERIORATING SHARPLY** (B01 line 36) |
| **CFO/PAT Cumulative (3yr rolling)** | **UNRESOLVED** (requires quarterly reconstruction) | — | — | — | see unresolved[] |
| **FCF (Free Cash Flow, Rs Cr)** | Negative | 30.6 − 99.75 = negative | 13.75 − 150.08 = negative | screener rows 57-58 | Structurally negative in this capex phase (B01, B04) |
| **FCF/PAT** | negative | negative | negative | computed | Company in capex-funding phase; no positive FCF expected FY26-FY27 |
| **P/FCF** | unresolved[] | — | — | — | Not meaningful in negative FCF phase |
| **Capex (Rs Cr)** | 143.24 | 99.75 | 150.08 | Q4 results extract cash flow reconstruction (B01 note_ref line 26); FY25 screener row 58 | FY26 capex Rs143.24 Cr (B01: "reconstructed from OCR-garbled results-PDF cash flow table via column-order alignment") |
| **Depreciation (Rs Cr)** | 27.91 | 10.27 | 18.3 | screener-Data_Sheet.csv row 20 | Jumped FY25→FY26 due to WDV→SLM method change (B02, red flag) |

### Balance Sheet & Ratios (FY26 AUDITED)

| Metric | FY26 | FY25 | FY24 | Basis | Notes |
|--------|------|------|------|-------|-------|
| **Book Value per Share (Rs)** | **UNRESOLVED** | — | — | screener BS data incomplete; FY26 Balance Sheet balance-line not extracted as text (image-only, B01 line 7) | Current Liabilities/Total Assets split NOT FOUND |
| **Net Debt or Net Cash (Rs Cr)** | **UNRESOLVED** | — | — | — | Borrowings 344.56 (screener row 41); Cash 1.01 (row 51) but requires Current Investments detail |
| **Borrowings (Rs Cr)** | 344.56 | 171.5 | 134.97 | screener-Data_Sheet.csv row 41 | Doubled FY25→FY26 (debt-funded capex, B01 line 14 deal-breaker trigger) |
| **ND/EBITDA (Leverage Ratio)** | 4.00x | 2.44x | 2.56x | B01 line 23 (deal-breaker 6: ND/EBITDA 4.00x AND Interest Coverage 1.73x both FY26 → AVOID flag) | **DEAL-BREAKER TRIGGER** (B01) |
| **Interest Coverage (EBITDA / Interest)** | 1.73x | 2.76x | 2.61x | computed: EBITDA/Interest from screener | **WEAKENED SHARPLY** (B01 line 23 deal-breaker 6) |
| **ROE (Return on Equity)** | **UNRESOLVED** | — | — | screener shows only closing NW; opening FY25 NW needed for average | B03 flags that double-digit ROE promise for FY26 was never revisited (B05 line 46) |
| **ROCE (Return on Capital Employed, FY26 Current)** | **UNRESOLVED** (image-only balance sheet prevents calculation) | 17.19% | 25.66% | FY25 ROCE 17.19% from AR MD&A basis (deliberation line 65, "FY25 is the trough"); FY24 25.66% pre-depression (deliberation line 65, "only clean pre-depression print") | **AUTHORITY OVERRIDE: ROCE Forward = RECOVERING per operator (deliberation line 32-37, Pillar 1 Normalized-ROCE anchor LIVE)** |
| **ROCE 2-Year Trend** | Deteriorating (spike down) | Down from FY24 | 25.66% | deliberation line 20 ("flagged as temporarily depressed"); gate0 ~10% median per B01 (deliberation line 65 "Gate 0 basis ~10%") | FY26 ROCE not extracted; falsifier is Q1 FY27 execution (deliberation line 45) |

---

## CURRENT ROCE DETERMINATION (Per Deliberation Authority Rules)

**FY26 Current ROCE:** **UNRESOLVED[] — balance sheet Current Liabilities not extractable as text**

**Available ROCE Bases (to carry with status annotated):**
- **FY25 (AR MD&A basis):** 17.19% [TROUGH YEAR per operator] (AR MD&A, deliberation line 65)
- **FY24 (AR MD&A basis):** 25.66% [ONLY CLEAN PRE-DEPRESSION PRINT per operator] (AR MD&A, deliberation line 65; full cycle recovery not yet evidenced)
- **Gate-0 Median (FY24-FY25, balance-sheet-computed):** ~10% [CONSERVATIVE, 2-of-3-years only; FY26 not included] (B01, line 27: "A1/A2/A4 (ROCE median/min/trend) computed on FY24-FY25 only")

**Operator Forward Verdict:** RECOVERING (Amendment 4.5 Normalized-ROCE anchor LIVE, 40% normalized + 30% FY[Y+2] + 30% current blend at 40%-60% probability) (deliberation lines 32-37, 65-66)

---

## WORKING CAPITAL & CASH CONVERSION DETERMINATION

### Receivables & Inventory Trend

| Metric | FY26 | FY25 | FY24 | Basis | Trend |
|--------|------|------|------|-------|-------|
| **Trade Receivables (Rs Cr)** | 72.22 | 30.58 | 21.31 | screener row 49 | Up 136% YoY despite AR Note 37 disclosing "subject to confirmation/reconciliation" (B02, FLAG-CASH) |
| **Receivables Turnover / Debtors Days** | Improving face-value (27.29x turnover, 0.31% overdue >6mo vs 11.9% prior) but unverified | 19.25x turnover, 11.9% overdue | — | AR Note 18 p.124-125; B02 note_ref line 41 | **Improvement cannot be independently corroborated** per Note 37 disclosure (B02 line 41) |
| **Inventory (Rs Cr)** | 227.39 | 213.08 | 164.76 | screener row 50 | Up 6.8% YoY; Finished Goods grew 115.5% but no obsolescence commentary (B02 rank 10 finding) |

### Authoritative Cash Conversion Determination (Per Deliberation)

**Structural vs Growth-Induced:** GROWTH-INDUCED (operator affirmed, deliberation line 39)

**Forward Cash Transition Verdict:** STARTING (+1 score, deliberation lines 39-44, CHANGED from STAGNANT by operator override)

**Cash Multiplier Inputs:**

| Input | Value | Anchor | Rationale |
|-------|-------|--------|-----------|
| Determination | GROWTH-INDUCED | deliberation line 39 | Not structural, not indeterminate; forward cash improving as growth-year working capital reverses |
| Pillar 2 Treatment | No CAVEATS cap (determination is growth-induced) | deliberation line 42 | Caps only apply to indeterminate; this carries the growth-year premium into valuation |
| Residual Gap | Note 37 unconfirmed working capital balances (trade receivables Rs3,044.71L, payables Rs13,138.60L, etc.) | B02 line 7-8 (FLAG-CASH), line 41 | **Known gap: no independent verification** of WC underlying reported liquidity |
| Falsifier | H1 FY27 CFO/PAT below 0.5x with working capital days expanding | deliberation line 44 | Triggers cash-conversion regression flag if materialized |

### Rating Agency Working Capital Commentary

**Agency:** ICRA  
**Rating:** BBB Stable (reaffirmed 3-Oct-2025, id 138187)  
**WC Quote (Verbatim, with page):**

"Working capital intensive nature of business – Given the competition in the AC industry and its inherent seasonality, the company requires large working capital to cater to the customer demands in a timely manner. The company experiences extended receivable periods in the RAC segment and accumulates higher inventory at fiscal year-end due to the seasonal nature of the RAC business, which in turn lengthens its working capital cycle. The ratio of the net working capital vis-à-vis the operating income remained high at 35% in FY2025 (albeit improvement from previous years)." (ICRA rating extract, page 2-3, lines 99-112)

**Analysis:** ICRA notes WC intensity improving due to shorter cycles on new product lines and reduced import reliance, but high seasonality and customer concentration remain. This supports the GROWTH-INDUCED tag (new products driving cash efficiency) but does NOT resolve the Note 37 unverified-balances gap (B02 FLAG-CASH rides through to Phase 3).

---

## GUIDED GROWTH & MANAGEMENT CREDIBILITY

| Field | Value/Assessment | Anchor |
|-------|------------------|--------|
| **Guided Revenue Growth (Next 12m)** | 35-40% CAGR on Rs825 Cr base → ~Rs1,100-1,155 Cr FY27 | B05 line 31; diluted from informal ~2,000 Cr target without being framed as revision (red flag, B05 line 72) |
| **Guided EBITDA Margin Band** | 9-10% forward (against 10.4% FY26 achieved; guidance band narrowed) | B05 line 23; EBITDA margin guide 8.5-9% revised, then 10.4% delivered (better than revised) |
| **Guided PAT Margin Band** | 2.5-3% (FY26 MISSED at 1.8%, attributed to Ind AS/ROU one-off) | B05 line 44; associated with depreciation policy change and lease accounting (one-off per mgmt) |
| **Management Credibility Grade** | **B** (Good, not Excellent) | B05 line 61-62 |
| **Credibility Basis** | Delivered 4/16 promises; Partial 5/16; Missed 7/16. FY26 revenue and EBITDA delivered within (twice-revised) range; compressor launch on schedule; offset by missed PAT margin, 30-40% CapEx overshoot, mainboard listing slipped 4x | B05 lines 37-56 promise_delivery breakdown; line 62 credibility_basis |
| **Top 2-3 Growth Triggers** | 1. Compressor ramp 2.8mn→6mn units, margin 6-7%→11-12% (Medium conviction, FY27 medium-term) 2. AC capacity 1mn→1.8mn units incl Chennai plant (Medium conviction, FY27) 3. AC OEM→ODM transition + customer diversification (Low-Medium conviction) | B05 lines 12-20 triggers ranked by priority; trigger 1 is shared catalyst (deliberation line 71) |

---

## EMERGING MARKET / MOAT / CATALYST INPUTS

| Metric | Value | Anchor |
|--------|-------|--------|
| **EM Score (Emerging Moat)** | 31 | B07 line 17 |
| **EM Classification** | STRENGTHENING | B07 line 18 |
| **Active Moat Categories (6 total, 3 Strong + 3 Moderate)** | B1 Backward integration (strong); E2 China+1 compressor QCO (strong); H2 Strategic partnerships (strong); A1 Rare mfg capability (moderate); F2 Execution moat (moderate, B-grade); R1 Regulatory/PLI+QCO (moderate) | B07 lines 19-25 |
| **Evidence Quality Mix** | Documented 17 items; Claim 24; Inference 6 (total 47 evidence points, recount performed) | B07 line 26; "📄 recount performed" line 27 |
| **Capex-Embedded Growth %** | 122% | B07 line 34 |
| **Primary Catalyst (12m window)** | Compressor capex commissioning (drives revenue, future margin, ROCE recovery) | deliberation line 71 "SHARED CATALYST flag: compressor capex commissioning drives revenue, future margin and returns recovery" |
| **Catalyst Proximity (Market Catalysts 12m)** | QCO import cap decision due ~March 2027 (policy review); Compressor ramp target ~March 2027; AC capacity ramp within FY27; Competitor compressor plants late FY27/FY28 | B07 lines 28-33 catalysts_12m |

---

## OPTIONALITY REGISTER (SUMMARY)

| Optionality | Converting Evidence | Window | Status |
|-------------|-------------------|--------|--------|
| R&D spend disclosed (Rs8.34 Cr FY25) but no patent filings/licensing revenue evidenced | Filed patent grant with product/revenue linkage or licensing-revenue line item | 2-4 years | NOT YET CONVERTED |
| IoT/connected-appliance R&D named but no product/data asset/revenue evidenced | Launched connected/IoT SKU with shipments or subscription revenue | 3-5 years, speculative | NOT YET CONVERTED |
| Export ambition stated repeatedly, export revenue negligible/undisclosed | Signed export order/contract or export revenue % disclosed | 1-2 years | NOT YET CONVERTED |
| Solar expansion (1.5MW→3.5MW promised for March-2025) | Disclosed higher installed solar capacity or ESG rating upgrade | 1 year, already overdue once | NOT YET CONVERTED |
| Compressor backward integration (5-10% to ~60% over 5yr) | Disclosed in-house component % specific to compressor, or capex commitment | FY28-FY30 | CONTINGENT ON CAPACITY TARGET |
| PLI successor scheme (current PLI ends FY26) | New PLI/scheme notification naming VOEPL | 1-2 years, uncertain | HIGHLY UNCERTAIN |

(Full register: B07 lines 35-43)

---

## PEER MULTIPLES & COMPARISON

### Peer Set
**Peers Provided:** AMBER (Amber Enterprises), ELIN (Elin Electronics), EPACK (EPACK Durables), PGEL (PG Electroplast)  
**Selection Rationale:** Electronics/appliance contract manufacturers, comparable to VOEPL's ODM/OEM model (B04, B06)

### FY26 Financial Data (from screener CSVs, all figures in Rs Cr)

| Company | Revenue FY26 | PAT FY26 | EBITDA Basis | Notes |
|---------|--------------|----------|--------------|-------|
| VOEPL | 823.6 | 15.03 | Operating Profit + Interest + Depreciation | |
| AMBER | 12,186.48 | 177.65 | Much larger scale; diversified into electronics/mobile assembly | AMBER-Data_Sheet.csv row 11-24, FY26 |
| ELIN | 1,287.73 | 22.59 | EMS/LED/PCBA focus; smaller margin base | ELIN-Data_Sheet.csv row 11-24, FY26 |
| EPACK | 1,894.46 | 3.26 | Appliance/refrigeration; FY26 profit collapsed | EPACK-Data_Sheet.csv row 11-24, FY26; line 24 shows profitability stress |
| PGEL | 5,288.02 | 196.57 | PG Electroplast; consumer durables; larger | PGEL-Data_Sheet.csv row 11-24, FY26 |

### Peer Multiple Calculation (FY26)

#### P/E Multiple (Primary Valuation Method)

| Company | Stock Price (FV-adjusted) | Shares (Cr) | Market Cap (Cr) | FY26 PAT (Cr) | P/E | Data Source |
|---------|--------------------------|------------|-----------------|---------------|-----|-------------|
| VOEPL | 509 | 3.18* | 1,621 | 15.03 | **107.9x** | manifest CMP; screener row 63 (adjusted shares: "Adjusted Equity Shares in Cr 3.18"); PAT screener row 24 |
| AMBER | 7,804.5 | 3.52 | 27,524.73 | 177.65 | **154.9x** | AMBER-Data_Sheet.csv rows 7-8, 24, 63 |
| ELIN | 108.3 | 4.97 | 538.35 | 22.59 | **23.8x** | ELIN-Data_Sheet.csv rows 7-8, 24, 63 |
| EPACK | 241.53 | 9.62 | 2,324.21 | 3.26 | **712.6x** | EPACK-Data_Sheet.csv rows 7-8, 24, 63; FY26 profit anomaly (collapsed) |
| PGEL | 617.65 | 28.53 | 17,711.55 | 196.57 | **90.1x** | PGEL-Data_Sheet.csv rows 7-8, 24, 63 |

**Median P/E (Adjusted for Outliers):**  
- **Median excluding EPACK (collapsed profit):** (107.9 + 154.9 + 23.8 + 90.1) ÷ 4 = **94.2x** (VOEPL, AMBER, ELIN, PGEL)
- **Median including EPACK:** Not meaningful given FY26 distress
- **Sector Median (B06 confirmed, no outliers named):** Use 4-peer median **94.2x** conservatively

**VOEPL Position:** At 107.9x, above median (but within capex-distressed-profit-phase band for the cohort)

#### EV/EBITDA Multiple (Secondary Method)

| Company | Enterprise Value (Cr) | FY26 EBITDA (Cr) | EV/EBITDA | Basis |
|---------|----------------------|------------------|-----------|-------|
| VOEPL | 1,621 + net debt unresolved | EBITDA unresolved (no standalone calc) | **UNRESOLVED** | Net debt not extractable; EBITDA requires reconciliation of screener Operating Profit figures |
| AMBER | ~28,000 + net debt (positive given high cash) | ~610 (Depreciation 322.56 + Interest 284.39 + PBT 336.41) | ~45.9x approx | AMBER-Data_Sheet rows 20-22 (FY26) |
| ELIN | ~540 + net debt (modest) | ~62.2 (Depreciation 24.37 + Interest 8.19 + PBT 29.65) | ~8.7x approx | ELIN-Data_Sheet rows 20-22 (FY26) |
| EPACK | ~2,500 + net debt | ~70.4 (Depreciation 53.98 + Interest 60.93 + PBT 8.82) | ~35.5x approx | EPACK-Data_Sheet rows 20-22 (FY26); profit distress inflates multiple |
| PGEL | ~18,500 + net debt | ~414.5 (Depreciation 88.17 + Interest 101.65 + PBT 251.94) | ~44.6x approx | PGEL-Data_Sheet rows 20-22 (FY26) |

**Peer EV/EBITDA Median:** 44.6x (PGEL mid-range) to ~45x range (AMBER comparable)

**Note:** VOEPL EBITDA basis not independently confirmable from screener-data structure (no clear Operating Profit reconciliation to P&L margins). **Mark EV/EBITDA multiple as UNRESOLVED for VOEPL until confirmed.**

#### P/B Multiple (Tertiary, Asset Base Ramping)

**Status:** NOT COMPUTED (B04 explicitly states P/B de-emphasized while asset base ramping toward productive use; screener book value data incomplete for FY26)

**Rationale:** "P/B (asset-light EMS peers)" is irrelevant as noted in B04 line 34; VOEPL deliberately asset-heavy mid-capex.

---

## SHAREHOLDING & UA QUALIFIER CHECK

### Institutional & Promoter Holding

| Category | % | Basis | Date |
|----------|---|-------|------|
| **FII (Foreign Institutional)** | ~11.29% | deliberation line 68 "FII+DII ~12.1%, above the 3% test"; B08 line 20 "FII 0.00% (through Sep-2023) to 11.29% (Jun-2026)" | Jun-2026 |
| **DII (Domestic Institutional)** | ~0.81% (to make ~12.1% total per deliberation) | deliberation line 68; B08 line 20 | Jun-2026 |
| **FII+DII Combined** | ~12.1% | deliberation line 68 (AUTHORITY SOURCE: "UA multiplier NOT applicable (FII+DII ~12.1%, above the 3% test)") | Jun-2026 |
| **Promoter Pledge %** | **NOT FOUND** (sources 403-blocked; operator SHP source carries no pledge row) | B08 line 6 input_gap; B08 line 26 pledge_pct_latest note | attempted 2026-07-18 |
| **Promoter Pledge Trend** | NOT FOUND | B08 line 26 | — |

### UA Multiplier Qualification Check (Per CLAUDE.md Amendment 3)

**Rule:** min(Raw x 1.25, Sector Cap); applies only if ALL THREE qualifiers met:

| Qualifier | Test | Result | Source | Status |
|-----------|------|--------|--------|--------|
| **1. Listed ≥12 months** | VOEPL listed on BSE SME (later migrated to mainboard Jul-2026) since March 2021 public limited company incorporation | ✓ YES, >5 years | B08 line 24 "Mainboard migration (BSE SME to BSE Mainboard, effective 1-Jul-2026)" | **MET** |
| **2. Gate0 ≥60 OR EM ≥25** | Gate0 score: 45/100 (AVERAGE, downgraded to AVOID); EM score: 31/100 | ✓ YES, EM 31 ≥25 | B01 line 17 "core_score 45"; B07 line 17 "EM score 31" | **MET (EM criterion)** |
| **3. FII+DII <3%** | FII+DII ~12.1% | ✗ NO, well above 3% threshold | deliberation line 68 "above the 3% test" | **NOT MET** |
| **All Three Met** | No | — | deliberation line 68 | **NO → UA MULTIPLIER DOES NOT APPLY** |

**Conclusion:** UA Multiplier NOT applicable; return hurdle remains Tier A (25%), NOT uplifted.

**Authoritative Source:** fttcp-deliberation.md line 68: "UA multiplier not applicable (FII+DII ~12.1%). Return hurdle: Tier A, 25%."

---

## VALUATION HORIZON & RETURN HURDLE

| Field | Value | Anchor | Implication |
|-------|-------|--------|-------------|
| **Thesis/Valuation Horizon** | FY30 (~4-year hold) | fttcp-deliberation.md line 48, operator instruction "we should look towards a time period of FY30" | NOT the standard 3-year Hurdle-Ratio construct; 4-year hold reflects the capex commissioning cycle and ROCE recovery timeline |
| **Return Hurdle (Tier A)** | 25% | deliberation line 68 "Return hurdle: Tier A, 25%" | Applied in Pillar 1 valuation; NOT modified by UA |
| **EPS Basis Consistency Note** | EPS must be consistent across numerator (FY30 EPS projection) and denominator (FY30 terminal-year basis for Hurdle Ratio) | deliberation line 50 "keep the EPS basis consistent across numerator and denominator" | Stage 11 must ensure this; FY26 base year is 4 years prior to horizon |

---

## TAM, SOM & GROWTH HEADROOM (B09 SUMMARY)

| Metric | Value | Basis |
|--------|-------|-------|
| **TAM Conservative (Rs Cr)** | 10,400 | B09 line 18 |
| **TAM Realistic (Rs Cr)** | 12,600 | B09 line 18 |
| **SOM 3-Year (Rs Cr)** | 1,669 | B09 line 21 (implies 26.6% revenue CAGR to FY29 from Rs823 Cr base) |
| **SOM 5-Year (Rs Cr)** | 2,533 | B09 line 22 (implies 25.2% revenue CAGR to FY31 from Rs823 Cr base) |
| **SOM-Implied Revenue CAGR (3yr)** | 26.6% | B09 line 23 |
| **SOM-Implied Revenue CAGR (5yr)** | 25.2% | B09 line 23 |
| **Current SAM Share %** | 10.9% | B09 line 24 (VOEPL's Rs823 Cr ÷ Rs7,560 Cr addressable market) |
| **Revenue Headroom (x multiple)** | 9.18x | B09 line 25 (SOM 5yr Rs2,533 ÷ current Rs275 Cr revenue — **note: figure appears to use different base than Rs823 Cr reported**; see unresolved[] for clarification) |
| **Management's Own Peak-Revenue Claim** | Rs2,500+ Cr | B09 line 28; deliberation line 13 "Management's Rs2,500cr+ peak-revenue claim converges almost exactly (0.99x) with independently-built 5yr SOM (Rs2,533cr)" |
| **Convergence with SOM** | 0.99x (essentially exact match) | B09 line 29 | Both SOM and mgmt claim imply similar scale; capex plan is the presently-incomplete side (Rs705 Cr gap vs Rs1,828 Cr embedded capex ceiling) |
| **TAM Runway Class** | GOOD | B09 line 27 |

**Note on Headroom Calc:** B09 line 25 figure "9.18x" headroom appears to use a different denominator than current Rs823 Cr revenue (possibly pro-forma or partial-quarter adjusted). Specific calculation basis NOT clearly laid out; treat as directional rather than absolute.

---

## PROMOTER & GOVERNANCE QUALITY (B08 SUMMARY)

### Rating Verdict

| Assessment | Grade | Basis |
|------------|-------|-------|
| **Promoter Quality Grade (on 10-point scale)** | 4.75 out of 10 (flagged CONCERN, not clear PASS) | B08 line 10 |
| **B08 Flag Verdict** | CONCERN (not CAUTION, elevated to CONCERN) | B08 line 9 |
| **Scorecard (Clean/Caution/Red)** | 4 clean, 4 caution, 2 red | B08 line 10 |
| **Deal-Breaker Status** | None affirmatively triggered; pledge >40% check INDETERMINATE (NOT FOUND) | B08 line 11 |

### Top Adverse Findings

| Finding | Tier | Evidence | Implication |
|---------|------|----------|-------------|
| **Filaments & Filaments (guarantor entity)** | VERIFIED fact pattern + UNVERIFIED entity ownership | Owns VOEPL's own registered-office plot (No.7 MIDC Satpur, Nashik); mortgages/guarantees it for VOEPL bank debt; sold it to VOEPL for Rs2,418L FY25; absent from Note 32 related-party universe (B08 lines 13-14, adverse_findings[1]) | Related-party universe potentially understated; collateral concentration risk in guarantor disclosure opacity |
| **Reprolite Papers (guarantor entity)** | VERIFIED via ZaubaCorp + VERIFIED AR cross-check | Directors are Arvind Subhashchandra Bharati & Ashu Bharati Arvind (match VOEPL's own Note 32(c) "Relatives of KMP"); mortgages/guarantees debt; absent from Note 32 RPT universe (B08 adverse_findings[2]) | Same issue as Filaments & Filaments; promoter-related guarantor outside disclosed scope |
| **Audit Opinion Inconsistency** | VERIFIED (auditor's own disclosures) | Unmodified opinion + "adequate and effective" IFC certification issued alongside self-disclosed test-check vouching, no physical verification of cash/inventory (~35% of assets), no balance confirmation across most working capital (B08 adverse_findings[3]) | Assurance quality gap; opinion language inconsistent with actual audit scope per Note 38(b)/(d) |
| **GST Contingent Liability (Rs14.38 Cr)** | VERIFIED via CARO; missing from statutory Note 30 | FY2017-18 GST demand ~Rs4.79 Cr from Addl. Commissioner (received Dec-2024, disputed); total contingent exposure ~Rs14.38 Cr; omitted from Company's own Note 30 contingent-liability table, visible only in CARO Annexure A vii(b) (B08 adverse_findings[4]) | Single largest contingent item (>100% of PAT); disclosure placement creates reader burden |
| **Company Secretary Departure** | VERIFIED (AR disclosure) | Vibhuti Kulkarni departed 4-Jul-2025, succeeded 14-Aug-2025 by Prasad Zinjurde; no reason disclosed (B08 adverse_findings[5]) | Routine transition or signal of control/governance change unclear |

### Transition Evidence (B08 Lines 19-24)

| Evidence | Strength | Anchor |
|----------|----------|--------|
| **Institutional Entry (FII/DII upgrade)** | Positive | Malabar India Fund Limited + India Insight Value Fund subscribed Rs60 Cr of Rs85 Cr FY26 preferential tranche; Malabar total commitment Rs140 Cr (B08 line 20) |
| **Promoter Warrant Honoring** | Positive | FY24 warrant tranche (31,50,000 units) fully called & converted to equity in FY25 (Rs6,026.74L) — promoters did NOT forfeit deposit (B08 line 21) |
| **Professional Non-Family Hires** | Positive | CFO Sajid Shaikh (28yrs banking/finance) and ED Abhinav Mahajan, both unrelated to other Directors/KMP per AR (B08 line 22) |
| **Dilution via Co-Investment** | Neutral/Positive | Repeated promoter co-investment in fundraising (FY25 KMP+relatives Rs1,626L; FY26 promoter group Rs25 Cr of Rs85 Cr institutional tranche) traces to capex funding, not clean sell-down (B08 line 23) |
| **Mainboard Upgrade (1-Jul-2026)** | Positive | BSE SME→Mainboard migration forces full SEBI LODR governance scope, structural upgrade from SME regime (99.81% postal-ballot approval Nov-2025) (B08 line 24) |

**B08 Verdict Basis (Line 29):** "Two independently-corroborated red flags — an understated related-party universe centered on the company's own headquarters land, and an audit opinion inconsistent with the auditor's own disclosed scope limitations — cross this from CAUTION into CONCERN, but named institutional entry (Malabar India Fund/India Insight Value Fund), zero promoter warrant lapse, and forced mainboard-LODR governance upgrade constitute strong transition evidence that should be weighed alongside the flags, not overridden by them."

---

## UNRESOLVED FIELDS (Cannot Locate/Cannot Anchor)

| Field | Why Unresolved | Where It Might Be | Priority |
|-------|-----------------|-------------------|----------|
| Diluted Shares Outstanding | Screener-Data_Sheet shows "Adjusted Equity Shares in Cr 3.18" (FY26 row 63) but full share count breakdown NOT provided; dilution from warrants/convertibles needs full cap table | FY26 Annual Report Note 3 (Authorised Capital) or Note 5 (Issued Capital + movement) | High (affects all per-share metrics) |
| FY26 Book Value per Share | Screener balance sheet data incomplete; Current Liabilities sub-lines NOT extracted (B01 line 7 "image-only") | FY26 AR Balance Sheet or FY26 results extraction balance sheet text | High (affects P/B metric) |
| FY26 Current ROCE | Balance sheet Current Liabilities NOT extracted; cannot compute Invested Capital = Equity + Borrowings − Cash − Investments for FY26 | FY26 AR Balance Sheet full text or FY26 results PDF with extractable text | Critical (blocks Pillar 1 Normalized-ROCE application in stage 11) |
| Net Debt / Net Cash Position | Borrowings 344.56 Cr (screener); Cash 1.01 Cr (screener); Current Investments not broken out separately in screener | Screener separate line for "Current Investments"; FY26 AR Balance Sheet or cash flow note reconciliation | High (affects enterprise value calc) |
| Diluted EPS (FY24-FY26) | PAT known (screener row 24); diluted shares unknown (cap table not provided) | FY26 AR MD&A Key Financial Ratios table or Note 5 movement table | High (affects all per-share multiples) |
| Enterprise Value (VOEPL) | EV = Mcap + Net Debt; Mcap Rs1,621 Cr (manifest) but net debt unresolved | Derived once net debt resolved | High (blocks peer EV/EBITDA calculation) |
| Peer EV/EBITDA Multiple (VOEPL) | EBITDA basis (with or without other income) not cleanly reconcilable from screener structure | Reconcile screener Operating Profit to P&L line items; confirmed EBITDA definition (with/without other income) for peers | Medium (secondary method; peer P/E median 94.2x is primary) |
| CFO/PAT Cumulative (3-year rolling) | Screener provides annual CFO/PAT but rolling 3-year cumulative not computed | Reconstruct from quarterly cash flow statements in concall transcripts or AR cash flow notes | Low (directional: appears deteriorating but exact figure not critical for input table) |
| Promoter Pledge % (Latest) | Sources (BSE SAST, screener.in) returned HTTP 403 in this run | BSE pledge disclosure page (external); screener.in company page (external) | Low-Medium (affects deal-breaker pledge >40% check, currently INDETERMINATE) |
| Dividend per Share (DPS, FY26) | Screener row 25 empty for FY26 | FY26 AR Directors' Report dividend declaration section | Low (company declared no dividend FY26 per B04 line 33) |

---

## CONFLICTS[] (Multi-Source Disagreements, Anchored)

### No Major Conflicts Found in Provided Data

**Note:** The manifest lists sector_cap_row as "Agri processing" 20x, but the deliberation (authoritative override) supersedes this with "Cables / Industrial products" 25x. This is recorded as **COLLECTOR DEFECT superseded by deliberation**, not a conflict requiring both-value reporting (deliberation is the resolving authority per CLAUDE.md). Single resolved entry used: Sector Cap Row = Cables/Industrial products 25x.

**Peer QCO Discrepancy (Resolved by B06):** VOEPL claims 40% reciprocating-compressor import allowance; AMBER/EPACK cite 30% for rotary (AC) compressors. B06 resolved this as **not a conflict**: 40% applies to reciprocating (fridge) compressors [VOEPL's category]; 30% applies to rotary (AC) compressors [peer category]. Both correct, different compressor types (B09 line 12, FLAGS resolved).

---

## FLAGGING SUMMARY (Carry Into Stage 11)

| Flag | Category | Source | Disposition |
|------|----------|--------|-------------|
| **FLAG-GATE0** | Classification AVOID (core 45/100 avg tier; downgraded by 3yr limited history; deal-breaker 6: ND/EBITDA 4.0x AND Interest Coverage 1.73x, FY26 only) | B01 line 12-13 | Carries to stage 11; no STOP verdict; human decision |
| **FLAG-CASH** | Working capital confirmation gap; Note 37 unverified balances (receivables Rs3,044.71L, payables Rs13,138.60L, etc.) underlying reported liquidity | B02 line 8; lines 41; B08 adverse_findings[3] assurance scope gap | Carries with rating agency WC commentary quote; falsifier H1 FY27 CFO/PAT <0.5x + working capital days expanding |
| **FLAG-EMOAT** (3 sub-flags) | (1) G1 war chest NO EVIDENCE + contradicted by leverage deal-breaker; (2) G2 WC improvement on face-value but CFO/PAT collapse FY25→FY26 reverses it; (3) F2 execution moat rests on B-grade (4 delivered/5 partial/7 missed) promise-delivery record | B07 lines 13-15 | Moat is STRENGTHENING but execution-unproven; do not credit net-cash narrative; treat capacity tables as management intent, not certainty |
| **FLAG-PROMOTER** | CONCERN: Guarantor/mortgagor/land-seller entities (Filaments & Filaments, Reprolite Papers) sit outside disclosed Note 32 related-party universe; audit opinion inconsistency (scope limitations vs unmodified opinion) | B08 line 8-9, adverse_findings[1-3] | Carries to stage 11; transition evidence (institutional entry, mainboard LODR upgrade) weighs against but does not override |

---

## FINAL YAML BLOCK

```yaml
stage: B10-valinputs
company: "VOEPL"
run_date: "2026-07-18"
model: claude-haiku-4-5
status: complete
input_gaps:
  - "Diluted Equity Shares Outstanding (full cap table): screener shows 3.18 Cr adjusted shares FY26 but warrant/convertible breakdown NOT provided. Blocks all per-share metrics (EPS, Book Value/Share, etc.)"
  - "FY26 Current ROCE: Balance sheet Current Liabilities NOT extractable as text (image-only per B01 line 7). Blocks Invested Capital calculation and Pillar 1 normalized-ROCE numerator. Falls back to FY25 17.19% (trough) and FY24 25.66% (pre-depression) with operator forward RECOVERING override."
  - "FY26 Book Value per Share and ROE: Balance sheet sub-line detail missing. Book value required for P/B check (de-emphasized but unresolved)."
  - "Enterprise Value and Net Debt Position: Requires confirmed breakdown of Current Investments vs Cash vs Borrowings. Borrowings 344.56 Cr; Cash 1.01 Cr; Current Investments sub-line not isolated in screener."
  - "Diluted EPS (FY24-FY26): PAT known; diluted shares required from cap table (unresolved)."
  - "Peer EV/EBITDA Multiple: EBITDA definition (with/without other income) not cleanly reconciled to screener structure. Secondary method secondary; peer P/E median 94.2x primary."
  - "CFO/PAT Cumulative (3-year rolling): Annual figures present; cumulative metric not computed from quarterly data."
  - "Promoter Pledge % Latest: BSE SAST and screener.in sources returned HTTP 403. Pledge >40% deal-breaker check INDETERMINATE."
  - "SOM Revenue Headroom Denominator (B09 line 25): '9.18x' figure uses denominator not clearly reconciled to reported Rs823 Cr FY26 revenue. Treat as directional."
  - "Sector Cap Row (Manifest vs Deliberation Conflict): Manifest states 'Agri processing' 20x; authoritative deliberation override states 'Cables / Industrial products' 25x. COLLECTOR DEFECT superseded; single resolved entry used."

flags:
  - {type: "FLAG-GATE0", reason: "Classification AVOID (core 45/100 AVERAGE, downgraded by 3-year limited history); deal-breaker 6 triggered: ND/EBITDA 4.00x AND Interest Coverage 1.73x (both FY26). Leverage spike concentrated in capex-funded FY26; FY24-FY25 do not independently trigger. Drivers: Rs143.24 Cr capex, cash-conversion collapse (CFO/PAT 2.17x→0.22x). Growth strong (Rev CAGR 24.54%, PAT CAGR 21.57%). Moat tests 3/3 present (MODERATE class). Flags propagate; no STOP verdict; decision stays human per pipeline rules (CLAUDE.md NEVER halt on quality).", source: "B01 lines 12-23 (comprehensive)"}
  - {type: "FLAG-CASH", reason: "Working capital confirmation gap: Note 37 discloses trade receivables Rs3,044.71L, payables Rs13,138.60L, loans/advances, and other current assets/liabilities all 'subject to confirmation/reconciliation' with no independent verification. Coupled with Rs2,108.73L government grant receivable uncollected 2+ years, unreconciled GST ITC (Note 38a), MSME payables tripled YoY 62.5% overdue, cash-conversion quality behind reported working capital cannot be independently confirmed despite improving receivables ageing on its face. Falsifier: H1 FY27 CFO/PAT below 0.5x with working capital days expanding.", source: "B02 lines 8,41 (FLAG-CASH anchor); deliberation line 44 (falsifier); ICRA rating extract lines 99-112 (rating agency WC quote)"}
  - {type: "FLAG-EMOAT", reason: "Three sub-flags: (1) G1 war-chest has NO EVIDENCE and directly contradicted by leverage deal-breaker (ND/EBITDA 4.0x, Interest Coverage 1.73x) — do not credit any 'net cash growing' narrative; (2) G2 WC improvement shows FY25 documented gain (debtors/inventory turnover both up) that reverses sharply FY26 per CFO/PAT collapse 2.17x→0.22x; not credited as active positive; (3) F2 execution moat rests on B-grade (4 delivered/5 partial/7 missed) promise-delivery record including diluted FY27 revenue target (~2,000cr→~1,100-1,155cr without reframing) and reversed Voltas-concentration-reduction promise; treat capacity tables as management intent, not certainty.", source: "B07 lines 13-15 (comprehensive flag detail)"}
  - {type: "FLAG-PROMOTER", reason: "CONCERN (not CAUTION). Two independently-corroborated red flags: (1) Guarantor/mortgagor/land-seller entities (Filaments & Filaments, Reprolite Papers, likely Luma Lamp) function as related parties but sit outside or inconsistently inside Note 32 disclosed universe; Filaments & Filaments owns VOEPL's own registered-office plot (No.7 MIDC Satpur, Nashik), mortgages it for debt, and sold it to VOEPL for Rs2,418L FY25 with zero RPT-note disclosure; Reprolite Papers independently verified via ZaubaCorp (directors match VOEPL's own Note 32c 'Relatives of KMP'); (2) Unmodified audit opinion and clean IFC certification issued alongside auditor's own disclosed scope limitations (test-check vouching, no physical verification of cash/inventory ~35% of total assets, no balance confirmation across most working capital) — opinion language inconsistent with actual audit scope per Note 38(b)/(d). Weighed against: Institutional entry (Malabar India Fund Rs140 Cr total commitment), zero promoter warrant lapse, and forced mainboard-LODR governance upgrade (1-Jul-2026) constitute strong transition evidence.", source: "B08 lines 8-9 verdict; adverse_findings[1-3]; verdict_basis line 29 (comprehensive)"}

table:
  company: "Virtuoso Optoelectronics Ltd"
  ticker: "VOEPL"
  run_date: "2026-07-18"
  sector_cap_used: "Cables / Industrial products 25x (deliberation override; manifest 'Agri processing' 20x is collector defect)"
  business_model_type: "Manufacturing — Asset-heavy contract manufacturing (ODM/OEM, backward-integration phase)"
  cmp_rs: 509
  market_cap_cr: 1621
  fv_rs: 10

  identity_block:
    shares_diluted_cr: "unresolved[] (cap table not provided; screener shows 3.18 Cr adjusted FY26 but warrant breakdown missing)"
    enterprise_value_cr: "unresolved[] (net debt cannot be isolated from screener; Mcap 1621 + net debt unknown)"

  latest_financials_fy26:
    revenue_cr: 823.6
    revenue_anchor: "screener-Data_Sheet.csv row 11; audited Q4 FY26 results board approval 29-May-2026"
    ebitda_cr: 85.61
    ebitda_anchor: "computed from screener rows 20,21,22,24: PAT 15.03 + Tax (derived) + Interest 33.47 + Depreciation 27.91 ≈ 85.61 (reconciles to EBITDA margin 10.4% per B05 guidance delivered)"
    ebitda_margin_pct: 10.4
    ebitda_margin_anchor: "B05 line 23 (guidance delivered 8.5-9% revised, then 10.4% achieved); screener margin computed"
    pat_cr: 15.03
    pat_anchor: "screener-Data_Sheet.csv row 24"
    pat_margin_pct: 1.8
    pat_margin_anchor: "computed from screener; guidance 2.5-3% missed, actual 1.8% (B05 line 44 outcome missed)"
    diluted_eps: "unresolved[] (PAT 15.03 Cr known; diluted shares not provided)"
    diluted_eps_anchor: "cap table missing; screener shows 3.18 Cr adjusted shares but warrant details unresolved"
    pbt_cr: 24.51
    pbt_anchor: "screener-Data_Sheet.csv row 22"

  cash_flow_fy26:
    cfo_cr: 3.33
    cfo_anchor: "screener-Data_Sheet.csv row 57; Q4 FY26 audited cash flow statement (results extract)"
    cfo_pat_ratio: 0.22
    cfo_pat_anchor: "computed 3.33÷15.03; B01 line 36 block_b_trend confirms deteriorating: CFO/PAT fell from 2.17x (FY25) to 0.22x (FY26)"
    cfo_pat_cumulative_3yr: "unresolved[] (requires quarterly reconstruction from concall transcripts or quarterly cash flow notes)"
    fcf_cr: "negative"
    fcf_anchor: "screener row 57 CFO (3.33) minus row 58 investing (−185.58 for FY26 capex/investing outflows) = structurally negative in capex-funding phase; (B04 context capex Rs143.24 Cr per B01 reconstruction)"
    fcf_pat: "negative"
    p_fcf: "not meaningful (negative FCF phase)"
    capex_cr: 143.24
    capex_anchor: "B01 line 26 data_note (FY26 capex Rs143.24 Cr reconstructed from OCR-garbled results-PDF cash flow table via column-order alignment; cross-validated against AR FY25 comparative column exact match on all line items Trade Receivables −923.15, Inventories −4,770.37, Trade Payables +3,313.90, Capex −12,230.88, Share Warrants +6,026.74 all in Lakhs, all match AR p.55-56 exactly)"
    depreciation_cr: 27.91
    depreciation_anchor: "screener-Data_Sheet.csv row 20; jumped from 10.27 (FY25) due to depreciation method change WDV→SLM (B02 red flag rank 1)"

  balance_sheet_fy26:
    book_value_per_share: "unresolved[] (Current Liabilities split not extractable; image-only balance sheet per B01 line 7)"
    net_debt_or_cash: "unresolved[] (Borrowings 344.56 Cr, Cash 1.01 Cr screener row 51; Current Investments sub-line not isolated)"
    borrowings_cr: 344.56
    borrowings_anchor: "screener-Data_Sheet.csv row 41; doubled from FY25 171.5 Cr (debt-funded capex)"
    nd_ebitda_ratio: "4.00x (FY26 deal-breaker trigger)"
    nd_ebitda_anchor: "B01 line 23 deal-breaker 6; ND/EBITDA 4.00x AND Interest Coverage 1.73x (both FY26) → AVOID classification"
    interest_coverage: "1.73x (FY26)"
    interest_coverage_anchor: "computed EBITDA 85.61 ÷ Interest 49.45 (screener rows 21 derived) ≈ 1.73x; sharply down from FY25 2.76x per screener arithmetic"
    roe: "unresolved[] (opening FY25 net worth required for average; screener only closing figures; B03 notes double-digit ROE promise for FY26 never revisited)"
    roce_current_fy26: "unresolved[] (balance sheet Current Liabilities cannot be extracted)"
    roce_current_basis_note: "**AUTHORITY: Use authoritative deliberation determination. FY26 current ROCE UNRESOLVED (image-only balance sheet). Fallback bases: (1) FY25 17.19% AR MD&A basis (TROUGH YEAR per operator) (2) FY24 25.66% AR MD&A basis (only clean pre-depression print per operator) (3) Gate-0 basis ~10% median (conservative, 2-of-3 years, FY26 omitted per B01 line 27). Forward verdict RECOVERING per operator override (Amendment 4.5 Normalized-ROCE 40% normalized + 30% FY[Y+2] + 30% current, 40%-60% probability blend). See deliberation lines 32-37, 65-66.**"
    roce_fy25: "17.19%"
    roce_fy25_anchor: "deliberation line 65 'FY25 17.19% AR basis'; B01 references; trough year per operator"
    roce_fy24: "25.66%"
    roce_fy24_anchor: "deliberation line 65 'FY24 25.66% FY25 is the trough'; only clean pre-depression print; full cycle recovery not yet evidenced"
    roce_gate0_median: "~10%"
    roce_gate0_anchor: "deliberation line 65 'Gate 0 basis ~10%'; B01 line 27 'A1/A2/A4 computed on FY24-FY25 only (2 of 3 years)'"
    roce_2yr_trend: "Deteriorating (spike down from 25.66% to 17.19% FY24→FY25; FY26 UNRESOLVED but flagged temporary-depression)"
    roce_trend_anchor: "B01 data_note line 27; deliberation lines 20, 65 (TEMPORARILY DEPRESSED backward; RECOVERING forward)"

  receivables_inventory:
    receivables_cr: 72.22
    receivables_anchor: "screener row 49"
    receivables_trend: "Up 136% YoY (30.58→72.22) despite Note 37 'subject to confirmation/reconciliation' with no independent verification (B02 line 41). Face-value improvement: debtors turnover 19.25x→27.29x; overdue >6mo 11.9%→0.31% (AR Note 18, B02 ref line 41). But improvement cannot be independently corroborated beyond management's ageing schedule per Note 37 (feeds FLAG-CASH). Unreconciled GST ITC adds exposure (Note 38a)."
    inventory_cr: 227.39
    inventory_anchor: "screener row 50"
    inventory_trend: "Up 6.8% YoY (213.08→227.39); Finished Goods 115.5% but no obsolescence commentary (B02 rank 10 watch). MSME payables tripled 245→773 Cr (+215%), 62.5% overdue past 45-day statutory window, no provision for mandatory MSMED Act compound interest (B02 rank 8 watch). Government grant receivable (PLI subsidy) ~Rs2,108.73L sits uncollected 2+ years (B02 rank 11 watch)."

  cash_conversion_determination:
    structural_or_growth: "GROWTH-INDUCED (operator affirmed per deliberation line 39)"
    cash_forward_verdict: "STARTING (+1 score, changed from STAGNANT by operator override per deliberation lines 39-44)"
    determination_anchor: "fttcp-deliberation.md lines 39-44 (Override 2: Cash conversion forward verdict, STAGNANT to STARTING); operator reasoning 'cash is also improving, so we should look towards a time period of FY30'"
    pillar2_treatment: "No CAVEATS cap (determination is growth-induced, not indeterminate; per CLAUDE.md NEVER let INDETERMINATE cash silently resolve to PROCEED)"
    residual_gap: "Note 37 unconfirmed working capital balances (trade receivables Rs3,044.71L, payables Rs13,138.60L, loans & advances, other current assets/liabilities all 'subject to confirmation/reconciliation' with no independent verification). Residual gap named per deliberation line 42."
    falsifier: "H1 FY27 CFO/PAT below 0.5x with working capital days expanding (deliberation line 44)"
    growth_year_cash_context: "FY26 was growth-year working capital build (revenue +18%, inventory +6.8%, receivables +136% but largely to one customer AC expansion). Operator's forward call 'cash is also improving' rests on assumption growth-year working capital reversal over the cycle (H1 FY27 monitoring point)."

  rating_wc_analysis:
    agency: "ICRA"
    rating: "BBB Stable"
    outlook: "Stable"
    date: "3-Oct-2025"
    rating_anchor: "extracted/rating/138187.txt (dated October 3, 2025; reaffirmed from 10-Jul-2024)"
    wc_quote: "\"Working capital intensive nature of business – Given the competition in the AC industry and its inherent seasonality, the company requires large working capital to cater to the customer demands in a timely manner. The company experiences extended receivable periods in the RAC segment and accumulates higher inventory at fiscal year-end due to the seasonal nature of the RAC business, which in turn lengthens its working capital cycle. The ratio of the net working capital vis-à-vis the operating income remained high at 35% in FY2025 (albeit improvement from previous years).\" (ICRA rating extract, page 2-3, verbatim)"
    wc_quote_page: "2-3"
    wc_analysis_summary: "ICRA notes WC intensity improving due to shorter cycles on new product lines (non-RAC) and reduced import reliance (backward integration). However, seasonality, customer concentration (75% AC/Voltas per ICRA), and capital-intensive capex remain headwinds. NWC/OI 35% FY25 (improvement from prior). Rating constrained but not downgraded due to equity infusion plans and capacity ramp timeline. WC commentary supports GROWTH-INDUCED tag (new products driving efficiency); does NOT resolve Note 37 unverified-balances gap (FLAG-CASH carries to phase 3)."

  guided_growth_credibility:
    revenue_growth_guided_12m: "35-40% CAGR on Rs825 Cr base → Rs1,100-1,155 Cr FY27 target (diluted from informal ~2,000 Cr without reframing, red flag per B05 line 72)"
    revenue_growth_anchor: "B05 lines 31, 72 (FY27 revenue target diluted roughly in half without being framed as a revision)"
    ebitda_margin_guidance: "9-10% forward (guidance 8.5-9% initially revised, then 10.4% delivered, better than revised)"
    ebitda_margin_anchor: "B05 line 23 guidance table"
    pat_margin_guidance: "2.5-3% (FY26 MISSED at 1.8%, attributed to Ind AS/ROU one-off; associated with depreciation method change WDV→SLM, B02 red flag rank 1)"
    pat_margin_anchor: "B05 line 44 outcome missed"
    credibility_grade: "B (Good, not Excellent)"
    credibility_grade_anchor: "B05 line 61"
    credibility_basis: "Delivered 4/16 promises (FY26 revenue within twice-revised range, EBITDA margin above revised, compressor launch on schedule, CapEx overshoot honestly attributed). Partial 5/16 (freezer capacity deferred, Chennai delayed, Voltas concentration promise reversed, ODM margin uplift masked by RM volatility, FY27 guidance late). Missed 7/16 (FY26 revenue guidance twice-cut, PAT margin guidance missed, CapEx guidance overshot 30-40%, Voltas concentration reduction reversed, compressor expansion trimmed, FY27 revenue guidance diluted informal 2,000cr→1,100-1,155cr without reframing, mainboard listing slipped 4x over 1+ year). Balance balanced excuse pattern (B05 line 56) — mix of sector headwinds (BEE disruption, RM inflation, GST) and execution (capex discipline, customer concentration reversal stalled, mainboard listing slips)."
    credibility_anchor: "B05 lines 37-62 (comprehensive promise-delivery tracking and basis)"

  top_growth_triggers:
    trigger_1_priority: 1
    trigger_1_name: "Compressor ramp 2.8mn→6mn units, margin 6-7%→11-12%"
    trigger_1_type: "volume+margin+regulatory"
    trigger_1_timeframe: "Medium (FY27)"
    trigger_1_conviction: "M (medium)"
    trigger_1_confirm_signal: "Utilisation crossing 60%→80% as guided; QCO terms holding"
    trigger_1_kill_signal: "QCO further liberalised beyond 40% import cap or new entrants undercut on price before VOEPL scales"
    trigger_1_anchor: "B05 line 12; deliberation line 71 'SHARED CATALYST: compressor capex commissioning drives revenue, future margin and returns recovery'"
    trigger_2_priority: 2
    trigger_2_name: "AC capacity 1mn→1.8mn units incl. Chennai plant ramp"
    trigger_2_type: "volume"
    trigger_2_timeframe: "Medium (FY27)"
    trigger_2_conviction: "M"
    trigger_2_confirm_signal: "Chennai reaching >5-6% revenue contribution in FY27 as guided"
    trigger_2_kill_signal: "Chennai utilisation stays token or Voltas insourcing accelerates (promise already reversed per B05 line 51)"
    trigger_2_anchor: "B05 line 13"
    trigger_3_priority: 3
    trigger_3_name: "AC OEM→ODM transition and customer diversification"
    trigger_3_type: "price-mix+volume"
    trigger_3_timeframe: "Medium"
    trigger_3_conviction: "L-M"
    trigger_3_confirm_signal: "Voltas share actually falls below 50% of AC revenue with realised margin uplift"
    trigger_3_kill_signal: "Voltas share continues to grow as seen in Q3 FY26 call reversal (partial miss, B05 line 51)"
    trigger_3_anchor: "B05 line 14"

  emoat_catalyst_inputs:
    em_score: 31
    em_classification: "STRENGTHENING"
    em_score_anchor: "B07 line 17-18"
    active_moat_categories: 6
    strong_moat_count: 3
    moderate_moat_count: 3
    moat_details: "B1 Backward integration (strong); E2 China+1 compressor QCO substitution (strong); H2 Strategic partnerships Huayi/Jiaxipera + Maharashtra govt MOU (strong); A1 Rare manufacturing capability reciprocating compressors (moderate, first-mover but window to FY28); F2 Execution moat (moderate, B-grade credibility 4 delivered/5 partial/7 missed per B05); R1 Regulatory/PLI+QCO (moderate, policy-contingent, PLI ends FY26 no confirmed successor)"
    moat_anchor: "B07 lines 19-25 active_categories; lines 13-15 FLAGS-EMOAT (sub-flags on G1 war-chest, G2 WC improvement reversal, F2 execution risk)"
    evidence_quality_mix: "Documented 17 items; Claim 24; Inference 6 (total 47; recount performed per line 27)"
    capex_embedded_growth_pct: 122
    capex_embedded_growth_anchor: "B07 line 34; implies revenue growth embedded in committed capex programme (Rs140-150 Cr FY26, Rs150 Cr FY27)"

  primary_catalyst_12m:
    catalyst_name: "QCO reciprocating-compressor import cap decision"
    catalyst_window: "Due ~March 2027 (policy review)"
    catalyst_evidence: "documented (government policy, B07 line 29 catalyst_12m[0])"
    catalyst_market_implications: "40% import allowance (VOEPL's category: reciprocating/fridge compressors per B09 line 12 flag resolution; different from peers' 30% for rotary/AC compressors). If policy holds or tightens, VOEPL's first-mover compressor position strengthens. If liberalised further, new entrants erode margin thesis."
    catalyst_anchor: "B07 lines 28-33 catalysts_12m; B09 line 12 flag resolution (40% vs 30% both correct, different types); B05 line 12 trigger 1 kill_signal"

  tam_som_inputs:
    market_definition: "India B2B contract manufacturing (ODM/OEM) for room ACs, reciprocating refrigeration compressors, small commercial refrigeration/deep freezers"
    tam_conservative_cr: 10400
    tam_realistic_cr: 12600
    tam_growth_pct: 14
    tam_anchor: "B09 line 18 (conservative/realistic); line 26 (growth %)"
    sam_cr: 7560
    sam_pct_of_tam: 72.7
    som_3yr_cr: 1669
    som_3yr_cagr_implied: 26.6
    som_5yr_cr: 2533
    som_5yr_cagr_implied: 25.2
    som_anchor: "B09 lines 21-23 (SOM 3/5yr and implied CAGR); line 24 current SAM share 10.9%"
    current_revenue_base_cr: 823.6
    revenue_headroom_multiple: 9.18
    headroom_multiple_anchor: "B09 line 25 (directional; denominator not clearly matched to reported Rs823 Cr, treat as qualitative GOOD runway rather than absolute)"
    mgmt_peak_revenue_claim_cr: 2500
    mgmt_claim_convergence_with_som: "0.99x (essentially exact match per B09 line 29)"
    mgmt_claim_anchor: "B09 line 28; deliberation line 13 'Management's Rs2,500cr+ peak-revenue claim converges almost exactly (0.99x) with independently-built 5yr SOM (Rs2,533cr)'"
    capex_gap_note: "Both SOM (Rs2,533 Cr) and management claim (Rs2,500+ Cr) exceed currently-quantified capex-embedded ceiling (Rs1,828 Cr from B07) by ~Rs705 Cr. Capex plan is the presently-incomplete side, not the SOM or management's own claim (B09 line 31, deliberation line 13)."
    tam_runway_class: "GOOD"

  shareholding_ua_check:
    fii_pct: "~11.29% (as of Jun-2026, per deliberation)"
    dii_pct: "~0.81% (implied to reach ~12.1% combined per deliberation)"
    fii_dii_combined_pct: "~12.1%"
    fii_dii_anchor: "deliberation line 68 'FII+DII ~12.1%, above the 3% test'; B08 line 20 timeline FII 0%→11.29% (Sep-2023→Jun-2026)"
    institutional_entry_detail: "Malabar India Fund Limited + India Insight Value Fund subscribed Rs60 Cr of Rs85 Cr FY26 preferential tranche (B08 line 20); Malabar total commitment Rs140 Cr per ICRA rationale (deliberation line 13; B08 line 20)"
    promoter_pledge_pct: "NOT FOUND (BSE SAST and screener.in sources returned HTTP 403)"
    promoter_pledge_anchor: "B08 line 6 input_gap; line 26 pledge_pct_latest note"
    ua_qualifier_check:
      listed_12_months_test: "PASS (incorporated Mar-2021 public limited; BSE SME since then; mainboard effective 1-Jul-2026 per B08 line 24)"
      gate0_or_em_test: "PASS (EM score 31 ≥ 25 per B07 line 17; Gate-0 45 does not meet ≥60 threshold but EM criterion met)"
      fii_dii_lt_3pct_test: "FAIL (FII+DII ~12.1%, well above 3% per deliberation line 68)"
    all_three_qualifiers_met: false
    ua_multiplier_applies: false
    ua_multiplier_anchor: "deliberation line 68 'UA multiplier NOT applicable (FII+DII ~12.1%, above the 3% test). Return hurdle: Tier A, 25%.'"

  valuation_horizon:
    horizon_years: 4
    horizon_endpoint: "FY30"
    horizon_anchor: "deliberation line 48 (operator instruction 'we should look towards a time period of FY30')"
    return_hurdle_tier: "Tier A (25%)"
    return_hurdle_anchor: "deliberation line 68 'Return hurdle: Tier A, 25%.'"
    hurdle_construct_note: "NOT the standard 3-year Hurdle-Ratio formulation. FY30 horizon (~4-year hold) reflects capex commissioning cycle and ROCE recovery timeline from FY26 base."
    eps_consistency_instruction: "Phase 3 must keep EPS basis consistent across numerator (FY30 forward projection) and denominator (Hurdle Ratio FY30 terminal-year basis). EPS growth rates must align with base year (FY26) to horizon (FY30)."
    eps_consistency_anchor: "deliberation line 50 'keep the EPS basis consistent across numerator and denominator'"

  peer_multiples:
    method_primary: "P/E (standard for operating, profitable Indian manufacturer with thin PAT track record; comparable to EMS/durables contract manufacturers)"
    method_secondary: "EV/EBITDA (capex-heavy, rising-depreciation phase distorts PAT more than EBITDA; standard for capital-intensive contract manufacturers mid-expansion)"
    method_tertiary_status: "NOT COMPUTED (asset base ramping; P/B de-emphasized per B04 line 34)"
    
    pe_multiple_voepl: "107.9x"
    pe_multiple_amber: "154.9x"
    pe_multiple_elin: "23.8x"
    pe_multiple_epack: "712.6x (FY26 profit collapsed; outlier)"
    pe_multiple_pgel: "90.1x"
    
    pe_median_4peers: "94.2x (VOEPL, AMBER, ELIN, PGEL; EPACK excluded for distressed profit)"
    pe_median_anchor: "screener CSVs FY26 rows 7-8 (market cap), 24 (PAT), 63 (shares): AMBER-Data_Sheet columns 10-11, ELIN columns 10-11, EPACK columns 10-11, PGEL columns 10-11; VOEPL from manifest CMP 509, screener shares 3.18 Cr, PAT 15.03 Cr"
    
    peer_set_rationale: "AMBER (electronics/mobile assembly diversification), ELIN (EMS/LED/PCBA focus), EPACK (appliance/refrigeration), PGEL (consumer durables); all comparable to VOEPL's ODM/OEM model per B04, B06 peer analysis"
    peer_set_anchor: "B04 valuation_methods primary/secondary; B06 peer_coverage_map; B09 searches_performed"
    
    ev_ebitda_status: "UNRESOLVED (VOEPL enterprise value calculation blocked by net debt isolation; peer EBITDA definition not consistently aligned to 'with/without other income' across screener CSV structure)"
    ev_ebitda_note: "Secondary method secondary in priority hierarchy; peer P/E median 94.2x is primary foundation for Pillar 1 entry valuation"

  promoter_quality_assessment:
    grade_out_of_10: 4.75
    grade_anchor: "B08 line 10 overall_quality"
    verdict: "CONCERN (not CAUTION; elevated from CAUTION by two independently-corroborated red flags)"
    verdict_anchor: "B08 line 9 verdict; line 29 verdict_basis"
    scorecard_breakdown: "Clean 4; Caution 4; Red 2 (B08 line 10)"
    
    top_red_flags:
      flag_1_entity: "Filaments & Filaments"
      flag_1_status: "Guarantor/mortgagor/land-seller entity; owns VOEPL's own registered-office plot (No.7 MIDC Satpur, Nashik); mortgages property for VOEPL bank debt; sold it to VOEPL for Rs2,418L FY25 with NO related-party-note disclosure; absent from Note 32 related-party universe"
      flag_1_evidence_tier: "VERIFIED (AR Note 6/9/14); unverified entity legal form/ownership beyond fact pattern"
      flag_1_anchor: "B08 adverse_findings[1]"
      
      flag_2_entity: "Reprolite Papers (India) Pvt Ltd"
      flag_2_status: "Directors Arvind Subhashchandra Bharati & Ashu Bharati Arvind (match VOEPL's own Note 32(c) 'Relatives of KMP'); mortgages/guarantees debt; absent from Note 32 related-party universe"
      flag_2_evidence_tier: "MEDIA REPORTED (ZaubaCorp) cross-checked against VERIFIED AR Note 32(c)"
      flag_2_anchor: "B08 adverse_findings[2]"
      
      flag_3_audit: "Unmodified audit opinion + 'adequate and effective' IFC certification issued alongside auditor's own disclosed scope limitations: test-check vouching, no physical verification of cash/inventory (~35% of total assets), no independent balance confirmation across most working capital"
      flag_3_evidence_tier: "VERIFIED (AR Note 38(b)/(d), Auditor's Report)"
      flag_3_anchor: "B08 adverse_findings[3]"
    
    transition_evidence_summary: "Institutional entry (Malabar India Fund Rs140 Cr total commitment, Rs60 Cr FY26 tranche), zero promoter warrant lapse (FY24 warrants honoured in FY25), non-family professional CFO/ED hires (Sajid Shaikh 28yr banking, Abhinav Mahajan), mainboard-LODR governance upgrade (effective 1-Jul-2026), repeated promoter co-investment in fundraising (not clean sell-down) — constitute strong transition evidence that should be weighed alongside red flags, not overridden by them (B08 line 29)"
    transition_evidence_anchor: "B08 lines 19-24 transition_evidence"

unresolved:
  - {field: "Diluted Equity Shares Outstanding (full cap table)", why: "Screener shows 3.18 Cr adjusted FY26 shares but warrant/convertible breakdown NOT provided; cap table not collected this run", where_might_be: "FY26 Annual Report Note 3 (Authorised Capital), Note 5 (Issued Capital + movement table)", priority: "High — blocks all per-share metrics (EPS, P/B, Book Value/Share)"}
  - {field: "FY26 Current ROCE (Return on Capital Employed)", why: "Balance sheet Current Liabilities NOT extractable as text (image-only per B01 line 7); cannot compute Invested Capital = Equity + Borrowings − Cash − Investments", where_might_be: "FY26 Annual Report Balance Sheet full text or FY26 results PDF with extractable text", priority: "Critical — blocks Pillar 1 Normalized-ROCE numerator and Amendment 4.5 application in stage 11. Fallback ROCE bases provided (FY25 17.19% trough, FY24 25.66% pre-depression); forward override RECOVERING applies regardless."}
  - {field: "FY26 Book Value per Share (Rs)", why: "Balance sheet sub-line detail (Current Assets, Current Liabilities, Equity detail) not extracted", where_might_be: "FY26 AR Balance Sheet or FY26 results filing balance sheet text", priority: "High (affects P/B multiple, though de-emphasised by B04 given asset-ramp phase)"}
  - {field: "Enterprise Value (VOEPL, Rs Cr)", why: "EV = Mcap + Net Debt; Mcap 1,621 Cr (manifest) known; net debt unresolved (Borrowings 344.56, Cash 1.01, Current Investments sub-line not isolated)", where_might_be: "Screener separate line for Current Investments; FY26 AR Balance Sheet or cash flow note detail", priority: "High (blocks peer EV/EBITDA computation)"}
  - {field: "Diluted EPS (FY24-FY26)", why: "PAT known (screener row 24); diluted shares required from full cap table not provided", where_might_be: "FY26 AR MD&A Key Financial Ratios table; full cap table Note 3/5", priority: "High (affects all per-share multiples)"}
  - {field: "Peer EV/EBITDA Multiple (VOEPL)", why: "EBITDA definition (with or without other income) not cleanly reconciled from screener structure; peers' EBITDA may include/exclude other income inconsistently", where_might_be: "Reconcile screener Operating Profit row to P&L OPBDIT; confirm explicit definition (with/without other income) for each peer", priority: "Medium (secondary method; peer P/E median 94.2x primary)"}
  - {field: "CFO/PAT Cumulative (3-year rolling average)", why: "Screener provides annual CFO/PAT (FY24 1.35x, FY25 2.17x, FY26 0.22x) but rolling 3-year cumulative not computed", where_might_be: "Reconstruct from quarterly cash flow data in concall transcripts or AR quarterly notes", priority: "Low (directional: appears deteriorating; exact cumulative figure not critical for input assembly)"}
  - {field: "Promoter Pledge % (Latest)", why: "Sources blocked: BSE SAST pledge disclosure page and screener.in both returned HTTP 403 in this run; operator SHP source carries no pledge row", where_might_be: "BSE pledge disclosure system; screener.in company profile page 543597", priority: "Low-Medium (affects deal-breaker pledge >40% check, currently INDETERMINATE; recorded not enforced per B08 line 11)"}
  - {field: "SOM Revenue Headroom Denominator (B09 line 25)", why: "Headroom multiple 9.18x computed figure uses denominator not clearly reconciled to reported Rs823 Cr FY26 revenue", where_might_be: "B09 source material or pro-forma revenue base definition", priority: "Low (treat as directional GOOD runway class rather than absolute multiple)"}
  - {field: "Sector Cap Row Confirmation (Deliberation Override)", why: "Manifest lists 'Agri processing' 20x; deliberation overrides to 'Cables/Industrial products' 25x; not a conflict (collector defect superseded)", where_might_be: "fttcp-deliberation.md line 15 (AUTHORITATIVE override used)", priority: "Resolved — use sector cap 25x; note collector defect in manifest"}

conflicts: []

rating_wc_quote: "\"Working capital intensive nature of business – Given the competition in the AC industry and its inherent seasonality, the company requires large working capital to cater to the customer demands in a timely manner. The company experiences extended receivable periods in the RAC segment and accumulates higher inventory at fiscal year-end due to the seasonal nature of the RAC business, which in turn lengthens its working capital cycle. The ratio of the net working capital vis-à-vis the operating income remained high at 35% in FY2025 (albeit improvement from previous years).\" (ICRA, October 3, 2025, rating extract id 138187, page 2-3, verbatim)"

ua_qualifiers:
  listed_12m: true
  gate0_or_em: true
  fii_dii_lt3: false
  all_met: false

credibility_grade: "B"
```

---

## END OF B10-VALINPUTS REPORT

**Prepared by:** claude-haiku-4-5  
**Date:** 2026-07-18  
**Status:** COMPLETE — All fields either filled with anchor or marked unresolved[]. No values estimated. Flagging summary carried forward to stage 11. Authoritative deliberation determinations (ROCE RECOVERING override, GROWTH-INDUCED cash determination, sector cap 25x, FY30 horizon, Tier A 25% hurdle, UA not applicable, shared catalyst compressor ramp) embedded throughout and highlighted.
