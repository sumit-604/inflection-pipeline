# STAGE 10: VALUATION INPUT ASSEMBLY
# Company: MACPOWER | Run Date: 2026-07-30 | Model: Claude Haiku 4.5

---

## COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|-------|-------|--------|
| Company Name | Macpower CNC Machines Limited | (manifest) |
| Ticker | MACPOWER | (manifest) |
| Sector | Capital goods / CNC machine tools | (B04, deliberation) |
| Sector Cap Row (Corrected) | Cables / Industrial products | (deliberation, Note: manifest erroneously states Pharma/CDMO 38x; corrected to Cables/Industrial products 25x per deliberation p.15-16) |
| Business Model Type | Manufacturing (capital goods, CNC/VMC/HMC-DCM/VTL machines) | (B04) |
| CMP (Current Market Price) | Rs 1,481 per share | (manifest) |
| Market Cap (incl. other equity) | Rs 1,482.0 cr | (manifest) |
| Shares Outstanding (diluted) | 100.042 million = 1.00042 crore | (FY25 AR Balance Sheet, Note 13, Equity Share Capital Rs 1,000.42 lakh / face value Rs 10) |
| Enterprise Value | Rs 1,481.58 cr | [Calculation: Market Cap Rs 1,482.0 cr + Net Debt / Cash] |
| EV Arithmetic | Market Cap (1,482.00) + Borrowings & Lease (309.66 lakh) - Cash & Equiv. (593.83 lakh) = Net Cash -284.17 lakh = Rs 1,481.58 cr | (FY26 results balance sheet p.6; FY25 AR Note 36(f) capital risk management; FY26 results Note 2 cash flow statement) |

---

## LATEST FINANCIALS TABLE (FY26 audited, year ended 31-Mar-2026; supplemented Q1 FY27 unaudited)

### Income & Profitability
| Metric | Value | Anchor |
|--------|-------|--------|
| **Revenue (Latest FY)** | Rs 333.18 cr | (FY26 results Q4/FY26, P&L Statement, p.3; year-ended column) |
| **EBITDA (Latest FY)** | Rs 53.90 cr | (B09-tam.yaml, cross-verified from 16.2% margin x 333.18 cr revenue) |
| **EBITDA Margin** | 16.2% | (B05 concall, B09 tam; Q4 FY26 shows flat 16.2% vs Q1 FY27; deliberation confirms stagnant margin at 16.2%) |
| **PAT (Latest FY)** | Rs 33.87 cr | (FY26 results P&L, "Profit for the period" row, year-ended 31-Mar-2026 column, p.3) |
| **PAT (TTM including Q1 FY27)** | Rs 43.45 cr approx. | (FY26 PAT 33.87 cr + Q1 FY27 PAT 9.58 cr, less Q1 FY25 PAT 4.55 cr ≈ 38.9 cr; operator-supplied screener trailing PAT from "Stock P/E 38.1" interpretation) |
| **PAT Margin (FY26)** | 9.72% | (FY26 results P&L, 33.87 / 333.18 calculation; consistent with B03 note of 9.72% vs disclosed 12.00% margin discrepancy) |
| **Diluted EPS (FY26)** | Rs 33.86 (uannualised Q4); Rs 33.86 (FY26 full year) | (FY26 results P&L, row 14, year-ended column; matches 3,387.08 lakh / 100.042 million shares) |
| **Forward EPS (FY27 basis)** | NOT FOUND in full-year committed targets; Q1 FY27 annualised proxy | (Q1 FY27 results show PAT Rs 9.58 cr for quarter; guidance from B05 states FY27 revenue 28-30% growth but EPS not explicitly guided; operator-approved earnings basis ONE-YEAR-FORWARD per deliberation) |

### Cash Flow & Conversion
| Metric | Value | Anchor |
|--------|-------|--------|
| **Operating Cash Flow (CFO, FY26)** | Rs 14.03 cr | (FY26 results cash flow statement p.6, "NET CASH FROM OPERATING ACTIVITIES" row, year-ended 31-Mar-2026) |
| **Free Cash Flow (FY26)** | Rs 3.06 cr | (Operating CF 14.03 cr - Capex 10.97 cr; capex from "Purchase of fixed assets" 1,096.95 lakh) |
| **Capex (FY26)** | Rs 10.97 cr | (FY26 results cash flow, "Purchase of fixed assets" line, 1,096.95 lakh = 10.97 cr) |
| **Depreciation (FY26)** | Rs 7.40 cr | (FY26 results P&L, row 4f, 739.55 lakh) |
| **CFO / PAT Ratio (FY26)** | 0.41x | (14.03 / 33.87; per B01 deal-breaker flag; per deliberation p.20, range 0.70x FY24 → 0.27x FY25 → 0.41x FY26, INDETERMINATE) |
| **CFO / PAT Cumulative (3-year FY24-26)** | 0.4538x | (B01 cumulative figure; below 0.50x threshold, drives max AVERAGE classification) |
| **FCF / PAT** | 0.090x | (3.06 / 33.87) |
| **Cash Conversion Determination** | INDETERMINATE (operator-confirmed) | (deliberation p.20-21; provisional 1.00x on FY26 CFO/PAT 0.41x, downside 0.80x if next period confirms structural deterioration) |

### Balance Sheet & Returns
| Metric | Value | Anchor |
|--------|-------|--------|
| **Book Value per Share (FY25)** | Rs 142.77 | (FY25 AR Balance Sheet p.128-129, Total Equity 14,282.42 lakh / 100.042 million shares; used as proxy pending FY26 audited balance sheet) |
| **Net Cash / (Debt)** | Rs (28.42) lakhs = (Rs 0.28) cr (net cash position) | (FY26 results balance sheet p.6, net cash = cash 593.83 - borrowings 21.58 - lease 288.08 - other payables; per capital risk Note 36 FY25 -284.17 lakh) |
| **Book Value (FY25 Total Equity)** | Rs 142.82 cr | (FY25 AR, Equity Share Capital 1,000.42 + Other Equity 13,282.00 = 14,282.42 lakh) |
| **ROCE (Latest, FY25)** | 23.75% | (FY25 AR Note 38(vi) "Return on Capital employed" row, 2024-25 column, p.185; per deliberation p.20: "screener shows 29.1% on a different capital-employed basis, to be anchored at stage 10"; reconciliation required) |
| **ROCE (Screener Basis, per deliberation input)** | 29.1% | (operator-supplied screener card; deliberation p.36-38 flags two ROCE bases: AR Note 38 23.75% vs screener 29.1%; stage 10 to reconcile; deliberation confirms 23.75% is operative for Pillar 1) |
| **ROCE 2-Year Trend Direction** | Declining | (FY24 26.70% per AR Note 38 → FY25 23.75% = -295 bps softening; deliberation p.21 "softening from 26.70% under growth capex, not TEMPORARILY DEPRESSED (fall ~295 bps, short of 500 bps trigger)"; forward STAGNANT) |
| **ROE (FY25)** | 17.65% | (FY25 AR Note 38(vi), 2024-25 column) |
| **ROE (FY24 comparator)** | 20.15% | (FY25 AR Note 38(vi), 2023-24 column; downtrend evident) |

### Valuation Multiples & Margins
| Metric | Value | Anchor |
|--------|-------|--------|
| **P/E (Trailing, CMP basis)** | 38.1x | (Deliberation p.29-32, operator override confirmed; trailing TTM profit ~39 cr yields 38.1x; operator-supplied screener card Stock P/E 38.1) |
| **P/B** | 10.4x | (CMP 1,481 / BVPS 142.77) |
| **EV/EBITDA (FY26)** | 27.5x | (EV 1,481.58 cr / EBITDA 53.90 cr) |
| **P/FCF** | NOT FOUND; FCF-based valuation not standard for capital-goods cyclicals | (B04 states primary method EV/EBITDA; secondary P/E; FCF volatile due to capex cycle) |

### Growth & CAGR
| Metric | Value | Anchor |
|--------|-------|--------|
| **Revenue (FY26 vs FY25)** | +27.3% YoY | (FY26 333.18 cr vs FY25 261.82 cr per AR p.130; FY27 guidance 28-30% per B05 concall) |
| **3-Year Revenue CAGR (FY24-26)** | 17.5% | (FY24 241.17 cr → FY26 333.18 cr: (333.18/241.17)^(1/2) - 1 = 17.5%) |
| **PAT (FY26 vs FY25)** | +32.9% YoY | (FY26 33.87 cr vs FY25 25.44 cr) |
| **3-Year PAT CAGR (FY24-26)** | 18.1% | (FY24 24.10 cr → FY26 33.87 cr: CAGR calculation) |
| **EBITDA (FY26 vs FY25)** | +29.8% YoY | (FY26 53.90 cr vs FY25 41.54 cr per AR operating highlights) |

---

## UPSTREAM ANALYSIS EXTRACTION (from B01-B09)

### From B04 (Business Model)
| Field | Value | Anchor |
|--------|-------|--------|
| Business Type | Manufacturing: capital-equipment, capital-goods manufacturer of CNC machine tools | (B04, standard operating business) |
| Asset Intensity | Medium | (B04) |
| Working Capital Intensity | High | (B04; confirmed by inventory days 223 FY25, receivables 39 days; capex-cycle financing model) |
| Pricing Power | Moderate | (B04) |
| Cyclicality | Cyclical (customer capex-cycle dependent, bank-financed machine purchases per SWOT threats) | (B04) |
| Moats Present | 1. Backward integration (sheet metal, spindle assembly, powder coating, Macrotrol controller in-house) - moderate durability; 2. Regulatory/qualification (DRDO/HAL/ISRO/ordnance factory pre-qualification) - moderate-high durability; 3. Brand/switching cost via NEXA premium range + 39-city service network - low-moderate durability | (B04, B07 emerging moat confirmation; B07 flags 99% imported controllers cap the backward-integration lever) |

### From B05 (Concall & Guidance)
| Field | Value | Anchor |
|--------|-------|--------|
| **Guided Revenue Growth** | 25-30% (stated FY26 & FY27) | (B05, Q2 FY26 call guidance; actual FY26 +27.3%, Q1 FY27 +56.1%) |
| **Guided Margin Band** | 15-17% EBITDA (operating margin printed 16.2% flat FY25-FY26) | (B05, Q3 FY26 call; aspiration 25% marginal future, gated on 60-acre land per deliberation) |
| **Guidance Reference Quarter** | Q2-Q4 FY26 calls covering FY26 and FY27 | (B05) |
| **Management Credibility Grade** | B (Good) | (B05 p.60-61: "FY26 revenue/EBITDA/PAT growth all delivered, Q1 FY27 ran ahead of guidance; 60-acre land slipped 3+ quarters (external blame); market-share figure 4.5% vs 1-2% unreconciled; machine volumes deflected every quarter") |
| **Top 2-3 Growth Triggers (Priority)** | 1. Capacity utilization ramp to ~90% on 2,500-machine base (FY27, HIGH conviction); 2. NEXA/high-end mix rising past 40% of order book (near-medium, HIGH); 3. 13-acre Metoda land execution (medium FY27, MEDIUM conviction) | (B05 triggers table) |
| **Primary Catalyst (12-month window)** | 13-acre plant construction/utilization ramp + 60-acre land signing decision | (B07 catalysts; B05 three timeline slippages on 60-acre (Dec-2025 → Mar-2026 → undated)) |

### From B07 (Emerging Moat & Catalysts)
| Field | Value | Anchor |
|--------|-------|--------|
| **Emerging Moat Score** | 15.0 (MODEST) | (B07, "4 Moderate categories, 0 Strong; claims-heavy (15 claim, 4 documented, 4 inference)") |
| **Emerging Moat Classification** | MODEST (not sufficient to override B01 AVOID gate) | (B07) |
| **EM Categories Active (Moderate strength)** | A4 (Product platform/modular architecture, 12-24m); F2 (Execution moat, 12-36m); G1 (War chest/low-leverage self-funded capex, ongoing); R1 (Regulatory/policy tailwind, 12-24m) | (B07) |
| **Evidence Mix** | Documented 6, Claim 15, Inference 4 | (B07 p.26) |
| **Optionality Register Summary** | 1. 60-acre greenfield land (10K machines, undated, slipped 3x); 2. JV/technology-transfer (NDA stage, unconfirmed); 3. Defence/aero bid-book (Rs 304-376 cr under evaluation, 6-12m, unconfirmed); 4. NEXA/premium mix progression (~39-40%, ongoing); 5. 25% EBITDA margin aspiration (gated on 60-acre land, multi-year journey); 6. Backward integration to ~34% of COGS (FY27-28 AR target) | (B07 optionality_register) |
| **Capex-Embedded Growth %** | 70% | (B07, FY26 capex Rs 15.36 cr on revenue growth 333.18 cr; 13-acre Phase 1 Rs 30-35 cr FY27 per Q4 call; deliberation flags capex will not resolve margin/ROCE aspiration without the land delay resolving) |

### From B01 (Gate 0 & Cash Flow Flag)
| Field | Value | Anchor |
|--------|-------|--------|
| **Block B Trend (CFO/PAT Cumulative)** | Deteriorating: 0.70x (FY24) → 0.27x (FY25) → 0.41x (FY26); 3-year cumulative 0.4538x | (B01 block_b_trend, deal-breaker, caps at max AVERAGE; threshold <0.50x) |
| **FLAG-GATE0** | Classification AVOID despite strong A/C/D blocks (18/16/20) + STRONG moat class (4/12) driven by Block B <8 + 3-year LIMITED history one-tier downgrade | (B01 p.7-9) |
| **FLAG-CASH** | CFO/PAT deteriorating 0.70→0.27→0.41x; cumulative FCF/PAT only 0.0043x across 3-year window | (B01 p.9; B02 receivables >6mo ageing up to 15.4% from 12.2%, turnover down 33%; B03 confirms) |
| **Core Score (Gate 0)** | 67 (meets ≥60 threshold) | (B01) |
| **Historical Downgrade Applied** | Yes, one-tier downgrade due to FY25 capex ramp (FCF -Rs 899.87 lakh) + FY26 inventory build (WC days +27.19 vs FY24); growth-capex pattern, not weakness | (B01 p.8-9, interpreted as non-halting per framework) |

### From B02 (Accounting Quality & Receivables)
| Field | Value | Anchor |
|--------|-------|--------|
| **Accounting Quality Score** | 6/10 | (B02) |
| **Receivables Trend** | Deteriorating: gross >6mo ageing rose to 15.4% (FY25) from 12.2% (FY24); net receivables +57.5% YoY against revenue +8.6%; turnover down 33% (9.32x vs 13.97x), implied days ~26 to ~39 | (B02 Finding #1, Note 9 p.149/174, Note 38vi p.185) |
| **Red Flag Summary** | Trade receivables deterioration (rank 1); margin improvement mechanical from inventory build, not operational (rank 3); fire incident Rs 439 lakh inventory loss (rank 4); Note 12/35 CFO loan contradiction (rank 5) | (B02 p.28-33) |
| **Rating PDF** | NOT PROVIDED | (per task input; no rating agency WC commentary available) |

### From B08 (Promoter & Governance)
| Field | Value | Anchor |
|--------|-------|--------|
| **Promoter Verdict** | TRUSTWORTHY | (B08 p.8) |
| **Promoter Holding %** | 73.2% | (B08) |
| **Pledge %** | 0% (stable across 12 quarters Sep-2023 to Jun-2026) | (B08 p.25-26) |
| **FII/DII Ownership (Latest)** | FII 0.57% + DII 0.39% = 0.96% (as of Jun-2026) | (B08 transition_evidence; rose from 0.00% Sep-2023 to peak 1.32% Mar-2025) |

### From B09 (TAM & SOM)
| Field | Value | Anchor |
|--------|-------|--------|
| **SOM-Implied Revenue CAGR (5-year)** | 24.3% | (B09, som_implied_revenue_cagr yr5; conservative TAM 20,000 cr, realistic 24,000 cr) |
| **TAM (Domestic CNC)** | Rs 20,000 cr (conservative) to Rs 24,000 cr (realistic) | (B09, based on IMTMA Goa Summit data >2x scrutiny per B09 flags) |
| **SAM (Serviceable Addressable Market)** | Rs 14,900 cr (62% of realistic TAM) | (B09) |
| **SOM 3-Year Revenue Target** | Rs 660 cr (27.3% CAGR from FY26 base 333.18) | (B09, capacity-check flagged ~Rs 190-290 cr gap at flat realisation for SOM 5yr; closes only if ASP/mix uplift + 13-acre capacity deliver) |
| **Management Market-Share Claim** | 4.5% (Q2/Q3 FY26) vs 1-2% (Q4 FY26, corrected under analyst pressure, per B05/B09 reconciliation flag) | (B09 p.11 flag; unreconciled 2-4x self-correction) |
| **Runway Class** | MASSIVE (44.7x revenue headroom on realistic TAM) | (B09, though capacity-gated on 13-acre + 60-acre execution per deliberation) |

---

## DELIBERATION RECORD AUTHORITATIVE CARRIES (Phase 3 Dependencies)

### FTTCP Verdict and Pillar Foundations
| Item | Approved Value | Anchor |
|-------|-----------------|--------|
| **FTTCP ROCE Forward Verdict** | STAGNANT | (deliberation p.23, "forward verdict STAGNANT (0)"; Pillar 1 uses CURRENT ROCE; normalization route NONE) |
| **Pillar 1 Normalization Route** | NONE (Route A fails 20% idle-capital test; Route B barred on STAGNANT verdict) | (deliberation p.23) |
| **ROCE Recovery Credit** | NOT CREDITED | (deliberation p.23, p.70-71) |
| **Pillar 2 (Cash Multiplier)** | INDETERMINATE; Provisional 1.00x on FY26 CFO/PAT 0.41x; Downside 0.80x | (deliberation p.23, p.71; operator-confirmed per p.20-21) |
| **Pillar 3 (Growth)** | +2x total: 3a +2x (order book 1.37x revenue, capex-embedded 70%, delivery grade B), 3b +0x (EM 15 <25), 3c +0x (order book <2.5x tenor) | (deliberation p.72) |
| **Strategic Premium** | +0x (no rare license, no documented pricing power, ROCE re-rating barred as STAGNANT) | (deliberation p.73) |
| **Undiscovered Alpha (UA) Applies?** | YES, times 1.25 on raw destination PE before cap | (deliberation p.74; all three qualifiers hold: listed 2018, Gate 0 67 ≥60, FII+DII 0.96% <3%) |
| **UA Qualifier 1: Listed ≥12 months** | YES (listed 2018, NSE main board 2020) | (B08 p.8; deliberation p.74) |
| **UA Qualifier 2: Gate 0 ≥60 OR EM ≥25** | YES (Gate 0 core score 67, EM 15) | (B01 core_score 67; B07 em_score 15; deliberation p.74) |
| **UA Qualifier 3: FII+DII <3%** | YES (0.96% Jun-2026) | (B08 p.23; deliberation p.74) |
| **UA Qualifiers All-Met** | YES | (deliberation p.74) |
| **Sector Cap (Corrected)** | 25x (Cables / Industrial products) | (deliberation p.15, p.75; manifest error Pharma/CDMO 38x superseded) |
| **Destination (Exit) PE, Operator-Approved** | 25.0x | (deliberation p.36-38; additive raw 26.75x = 21.4x x 1.25 UA, capped to 25x sector cap; RRM track 16-17x noted as lower reality track) |
| **Earnings Basis, Operator-Chosen** | ONE-YEAR-FORWARD | (deliberation p.40-43; apply exit PE to FY27 forward EPS, fits order-book-backed 28-30% grower) |
| **Tier** | A (25% hurdle, FII+DII <3%) | (deliberation p.76) |
| **SHARED CATALYST Flag** | 13-acre plant backward-integration capex + 60-acre land = single point of failure behind revenue-fulfilment AND margin/ROCE aspiration narratives | (deliberation p.81) |
| **Phase 3 Dependencies Remain** | Anchor FY26 ROCE and reconcile 23.75% (AR Note 38) vs 29.1% (screener) capital-employed basis; obtain credit rating rationale and receivables ageing schedule to close INDETERMINATE cash; confirm forward FY27 EPS used for exit multiple | (deliberation p.83-84) |

---

## UA QUALIFIER CHECK (per CLAUDE.md Amendment 3)

| Qualifier | Met? | Evidence & Anchor |
|-----------|------|-------------------|
| **Listed ≥12 months (as of run date 2026-07-30)** | YES | Listed on NSE SME Emerge 2018; migrated main board Aug-2020 (B08 p.12-13, board's report notes; >6 years as of run date) |
| **Gate 0 ≥60 OR Emerging Moat ≥25** | YES (Gate 0 ≥60) | Core Score 67 (B01, p.12; meets ≥60 threshold); EM Score 15 (B07, below 25 but Gate 0 qualifies) |
| **FII+DII <3%** | YES | FII 0.57% + DII 0.39% = 0.96% as of Jun-2026 (B08, p.23) |
| **All Three Qualifiers Met (per Amendment 3 per CLAUDE.md)** | YES | All three conditions satisfied; UA multiplier applies min(Raw x 1.25, Sector Cap 25x) = 25x (deliberation p.74) |

---

## UNRESOLVED[] & CONFLICTS[]

### Unresolved Fields

| Field | Why Unresolved | Where It Might Be |
|-------|-----------------|-------------------|
| **Forward FY27 EPS (exact full-year committed figure)** | Q1 FY27 PAT Rs 9.58 cr Q annualised is ~38.3 cr, but management has not published full-year FY27 EPS guidance (only revenue 28-30% growth), and Q1 results show PAT +110% YoY which is not sustainable run-rate | B05 concall transcripts (Q4 FY26 May call); Q1 FY27 results p.3 show annualised proxy Rs 9.58 cr quarter; operator-approved earnings basis ONE-YEAR-FORWARD per deliberation, but exact forward EPS figure remains in forecast domain outside stage 10's copy-only mandate |
| **FY26 ROCE (reconciliation of two bases: 23.75% AR Note 38 vs 29.1% screener)** | AR Note 38 states 23.75% on capital-employed basis per independent audit; screener shows 29.1% on a different capital-employed definition (likely excluding lease liabilities or other adjustments); deliberation confirms 23.75% feeds Pillar 1 but stage 10 instructed to "reconcile" the basis difference | FY26 results balance sheet (has lease liabilities 288.08 lakh which may be excluded in screener's capital-employed calculation); Note 38 of FY26 results equivalent (not yet extracted; FY25 AR Note 38(vi) only available) |
| **Credit Rating & WC Commentary (Rating PDF)** | Rating PDF NOT PROVIDED in inputs; no rating agency verbal working capital or cash-conversion language available | Not in inputs/ directory; task states "NOT PROVIDED (no rating PDF in inputs) → mark rating_wc_quote and any rating-derived field unresolved" |
| **Book Value per Share (FY26 basis)** | FY25 AR Balance Sheet available (Rs 142.77), but FY26 audited balance sheet embedded in Q4/FY26 results filing does not separately itemize total equity in detail comparable to FY25 AR's breakdown; FY26 results p.6 shows balance sheet but equity composition less detailed | FY26 results audited balance sheet p.6, columns for 31.03.2026 and 31.03.2025; would need Q4 FY26 full standalone statements restatement |
| **Depreciation (FY24 for CAGR computation)** | FY24 depreciation shown in FY25 AR comparative column as Rs 413.56 lakh (FY24-25 P&L statement p.130), but balance-sheet-based depreciation calculations for forward projection require full asset schedule (not extracted) | FY25 AR P&L p.130 shows FY24 depreciation; Asset schedule in Note 3 of FY25 AR (not yet extracted) |

### Conflicts

| Field | Value A | Anchor A | Value B | Anchor B | Used (Conservative) | Note |
|-------|---------|----------|---------|----------|----------------------|------|
| **ROCE (FY25)** | 23.75% | AR Note 38(vi), audited capital-employed basis | 29.1% | Screener card (operator-supplied, capital-employed basis unspecified) | 23.75% | Deliberation p.36-38 acknowledges both bases; confirms 23.75% (AR Note 38) for Pillar 1 use; screener uplift is capped by sector ceiling anyway (25x); reconciliation of capital-employed definition deferred to stage 10 detailed work |
| **PAT Margin (FY25)** | 12.00% | AR Note 38(vi) and MD&A p.85 disclosed figure (labeled "Net Profit Margin") | 9.72% | Direct computation from P&L (25.44 cr PAT / 261.82 cr revenue) + confirmed AR front-matter KPI chart p.4 | 9.72% (direct computation) | B03 triple_pass verification (p.26-27) flags ~2.3pp unreconciled gap; direct P&L and front-matter KPI chart both show 9.72% decline FY24 10.00% → FY25 9.72%, opposite direction from MD&A/Note 38(vi) disclosure of "improved 12.00%"; used conservative direct P&L computation per B03 kill-switch reasoning |
| **Revenue (FY25) Comparative** | 26,181.50 lakh (per FY25 AR P&L) | FY25 AR Statement of P&L p.130 audited | 261.82 cr (per operating highlights chart p.4 AR) | AR front-matter KPI chart | No material conflict (26,181.50 lakh = 261.815 cr rounding matches) | Confirmed consistent; used AR P&L 26,181.50 lakh |

---

## RATING PDF EXTRACTION

| Field | Value |
|-------|-------|
| **Agency** | NOT PROVIDED |
| **Rating** | NOT PROVIDED |
| **Outlook** | NOT PROVIDED |
| **Date** | NOT PROVIDED |
| **Working Capital / Cash Flow Commentary (Verbatim)** | NOT PROVIDED (no rating PDF in inputs) |
| **Rating WC Quote** | UNRESOLVED |

---

## PEER FINANCIAL DATA (B06 Summary)

| Metric | Macpower | JYOTICNC Comparable? | ADOR Comparable? | KLBRENG Comparable? |
|--------|----------|---------------------|------------------|---------------------|
| **P/E (Trading)** | 38.1x | Unquoted; disclosure-light peer data in B06 | Unquoted; Q4 FY26 call discussions only | Unquoted; Q4 FY26 call discussions only |
| **EV/EBITDA** | 27.5x | Unquoted in peer data available | NOT PROVIDED in B06 extracts | NOT PROVIDED in B06 extracts |
| **P/B** | 10.4x | NOT PROVIDED | NOT PROVIDED | NOT PROVIDED |
| **Growth (3-yr)** | 17.5% | >20% cited for JYOTICNC CNC consumption per B06; detailed peer multiples NOT PROVIDED | ~3-5% per B06 industry_cross_read | Capacity-race growth evident; detailed CAGR NOT PROVIDED |
| **ROCE** | 23.75% (FY25 AR) | NOT PROVIDED (peer ROCE unquoted) | NOT PROVIDED | NOT PROVIDED |

**Note:** B06 concludes "net_narrative_effect: complicates" due to defence bid conversion rate disparity (JYOTICNC far larger defence/aero order book and faster conversion than Macpower's described ~10-13% tender-bid ratio), suggesting Macpower's defence narrative may be running ahead of peer norms. Peer financial data complete extraction deferred to specialist comparative stage.

---

## SUMMARY METRICS FOR VALUATION MODEL HANDOFF

| Metric | Value | Tier | Note |
|--------|-------|------|------|
| **CMP Entry** | Rs 1,481 | Input | Manifest |
| **Exit PE (Approved)** | 25.0x | Authoritative | Deliberation, capped sector 25x, delivers fair value ~Rs 1,100 at one-year-forward earnings basis |
| **Earnings Basis** | ONE-YEAR-FORWARD (FY27) | Authoritative | Operator-chosen; deliberation p.40-43 |
| **Forward Revenue Base (FY27 est.)** | Rs 426-429 cr (28-30% guided growth on FY26 333.18 cr) | Guidance-based | B05 guidance; not yet delivered |
| **Forward EPS (FY27, for exit multiple)** | ~Rs 44 (illustrative from deliberation fair value calculation: Rs 1,100 / 25x) | Derived (not independently anchored) | Deliberation p.42 states "fair value Rs 1,100 (25x times forward EPS about Rs 44)"; actual FY27 EPS forecast NOT PROVIDED by management, only revenue guidance 28-30% |
| **ROCE (Pillar 1 input)** | 23.75% | Authoritative | AR Note 38(vi) FY25; use current ROCE per STAGNANT verdict (no normalization) |
| **Cash Multiplier (Pillar 2)** | INDETERMINATE; 1.00x provisional, 0.80x downside | Authoritative | Deliberation p.71; no clean pass on INDETERMINATE determination |
| **Growth Pillar (Pillar 3)** | +2x | Authoritative | Order book 1.37x FY26 revenue (Rs 456 cr), capex 70%-embedded, grade B delivery |
| **Strategic Premium** | +0x | Authoritative | No re-rating on STAGNANT ROCE verdict |
| **UA Multiplier** | 1.25x (capped at sector 25x) | Authoritative | All three qualifiers met (listed 12m, Gate0≥60, FII+DII<3%) |
| **Verdict (Operator-Approved)** | PROCEED WITH CAVEATS (FTTCP disposition); AVOID on valuation at CMP (fair value Rs 1,100 vs CMP Rs 1,481) | Authoritative | Deliberation p.54-56; Hurdle STOPS on base (1.45) and bull (1.83); entry zone Rs 563, MoS Rs 451 |

---

## GUIDANCE DELIVERY TRACK RECORD & CREDIBILITY GRADE CARRIER

| Guidance Item | Promised | Promised In | Outcome | Credibility Impact |
|----------------|----------|------------|---------|-------------------|
| **FY26 Revenue Growth** | 25-30% | Q2 FY26 | Delivered (+27.3%) | ✓ Hit |
| **FY26 EBITDA Target** | Rs 50 cr | Q2 FY26 | Delivered (Rs 53.90 cr) | ✓ Exceeded |
| **FY26 Order Book** | Rs 300-330 cr by year-end | Q2 FY26 | Delivered (Rs 456 cr actual, Rs 406 cr stated) | ✓ Exceeded |
| **60-acre Govt Land Signing** | End Dec-2025 | Q2 FY26 | **MISSED** (still undated as of Jun-2026 call, slipped 3x total) | ✗ External blame (policy) |
| **25% EBITDA Margin Aspiration** | 2-3 years via new plant | Q3 FY26 | **Narrowed** (re-anchored in Q4 to specifically require 60-acre land, not 13-acre nearer facility) | ~ Goalpost-shift under pressure |
| **Q1 FY27 Results** | Revenue guidance 28-30% for FY27 | Q4 FY26 | Q1 FY27 actual +56.1% YoY | ✓ Well ahead (one-quarter sample) |

**Grade Assigned (B05):** B (Good) — *5 delivered / 2 partial / 2 missed across 9 tracked items; execution track record strong on financial targets, weak on land/JV optionality; deflection on unit volume disclosure; credibility capped one tier by goalpost-narrowing pressure and external-blame-heavy excuse pattern on the land.*

---

## OUTPUT YAML BLOCK

```yaml
stage: B10-valinputs
company: "MACPOWER"
run_date: "2026-07-30"
model: "claude-haiku-4-5-20251001"
status: complete
input_gaps:
  - "Forward FY27 EPS (full-year committed figure not published; Q1 FY27 +110% YoY is not sustainable run-rate; management guides only revenue 28-30% growth)"
  - "FY26 ROCE reconciliation (AR Note 38 23.75% vs screener 29.1% on different capital-employed bases; stage 10 instructed to reconcile)"
  - "Credit rating PDF (NOT PROVIDED in inputs; no rating agency WC commentary available)"
  - "Book Value per Share FY26 (FY25 available at Rs 142.77; FY26 audited balance-sheet detail in Q4 results less granular than AR format)"
  - "Peer financial data complete (P/E, EV/EBITDA, P/B, growth multiples from named peers JYOTICNC, ADOR, KLBRENG largely unquoted or discussed only via concalls; detailed financial comparables NOT PROVIDED)"
flags:
  - "Deliberation record supersedes manifest sector_cap_row: Pharma/CDMO 38x CORRECTED to Cables/Industrial products 25x (deliberation p.15, p.75)"
  - "Cash conversion INDETERMINATE (operator-confirmed) per deliberation p.71: provisional 1.00x on FY26 CFO/PAT 0.41x, downside 0.80x; CFO/PAT deteriorated 0.70→0.27→0.41x over FY24-26, cumulative 0.4538x <0.50x threshold"
  - "ROCE forward verdict STAGNANT per deliberation p.23: current ROCE 23.75% (AR Note 38 FY25) feeds Pillar 1; normalization route NONE; ROCE recovery NOT credited"
  - "Shared catalyst (60-acre land) has slipped 3x (Dec-2025 → Mar-2026 → undated); gates both revenue-fulfillment AND margin/ROCE aspiration narratives per deliberation p.81"
  - "FTTCP disposition PROCEED WITH CAVEATS (capped by INDETERMINATE cash determination); valuation verdict AVOID at CMP per deliberation p.52-56"
  - "PAT margin disclosure conflict (AR Note 38/MD&A 12.00% vs direct P&L 9.72% FY25); used conservative direct P&L per B03 triple-pass verification (p.26-27)"
  - "Receivables trend deteriorating: >6mo ageing +15.4% from 12.2%, net receivables +57.5% YoY vs revenue +8.6%, turnover down 33% (per B02 Finding #1, FLAG-CASH)"

table:
  company_identity:
    company_name: "Macpower CNC Machines Limited"
    ticker: "MACPOWER"
    sector: "Capital goods / CNC machine tools"
    sector_cap_row_corrected: "Cables / Industrial products | 25x"
    business_model_type: "Manufacturing (capital-goods, CNC/VMC/HMC-DCM/VTL machines)"
    cmp_rs: 1481.0
    market_cap_cr: 1482.0
    shares_outstanding_million: 100.042
    enterprise_value_cr: "1481.58 | Calc: MCap 1482.00 + Borrowings/Lease 309.66 - Cash 593.83 = Net Cash (28.42 lakh) ≈ 1481.58 cr"
  
  latest_financials_fy26_audited_31mar2026:
    revenue_cr: "333.18 (FY26 results P&L, year-ended 31-Mar-2026)"
    ebitda_cr: "53.90 (B09-tam, cross-verified 16.2% margin; deliberation confirms flat 16.2% FY25-FY26)"
    ebitda_margin_pct: "16.2 (B05 concall, B09)"
    pat_cr: "33.87 (FY26 results P&L, 'Profit for the period')"
    pat_margin_pct: "9.72 (direct P&L calculation, preferred over Note 38 12.00% per B03 triple-pass, p.26-27)"
    diluted_eps_rs: "33.86 (FY26 full-year; 3387.08 lakh / 100.042 million shares)"
    operating_cash_flow_cr: "14.03 (FY26 cash flow statement, 'NET CASH FROM OPERATING ACTIVITIES')"
    free_cash_flow_cr: "3.06 (OCF 14.03 - Capex 10.97)"
    capex_cr: "10.97 (FY26 'Purchase of fixed assets', 1096.95 lakh)"
    depreciation_cr: "7.40 (FY26 P&L, 739.55 lakh)"
    cfo_pat_ratio: "0.41 (per B01, deliberation p.20)"
    cfo_pat_cumulative_3yr: "0.4538 (B01, FY24-26 window, below 0.50 threshold)"
    fcf_pat_ratio: "0.090"
    cash_conversion_determination: "INDETERMINATE (operator-confirmed, deliberation p.71; provisional 1.00x on 0.41x, downside 0.80x)"
    book_value_per_share_fy25_rs: "142.77 (FY25 AR Balance Sheet, Total Equity 14282.42 / 100.042m shares; pending FY26 detailed BS)"
    net_cash_cr: "0.28 (net cash position, FY26 results balance sheet, cash 593.83 - borrowings 21.58 - lease 288.08; per FY25 AR Note 36 -284.17 lakh)"
    roce_latest_fy25_pct: "23.75 (AR Note 38vi, capital-employed basis; deliberation p.36 confirms this feeds Pillar 1 despite screener 29.1% on different basis)"
    roce_2yr_trend: "Declining (FY24 26.70% → FY25 23.75% = -295 bps softening; deliberation p.21 'STAGNANT forward')"
    roe_latest_fy25_pct: "17.65 (AR Note 38vi)"
    pe_trailing_cmp: "38.1 (deliberation p.29-32, operator override; TTM profit ~39 cr implied)"
    pb_ratio: "10.4 (CMP 1481 / BVPS 142.77)"
    ev_ebitda_fy26: "27.5 (1481.58 / 53.90)"
  
  growth_and_cagr:
    revenue_fy26_vs_fy25_yoy_pct: "27.3 (333.18 vs 261.82)"
    revenue_3yr_cagr_fy24_26_pct: "17.5 ((333.18/241.17)^0.5 - 1)"
    pat_fy26_vs_fy25_yoy_pct: "32.9 (33.87 vs 25.44)"
    pat_3yr_cagr_fy24_26_pct: "18.1 (24.10 → 33.87)"
    ebitda_fy26_vs_fy25_yoy_pct: "29.8 (53.90 vs 41.54 per AR operating highlights)"
    guidance_revenue_growth_fy27_pct: "28-30 (B05 Q2-Q4 FY26 concalls)"
    som_implied_5yr_revenue_cagr_pct: "24.3 (B09, conservative TAM 20000 cr, realistic 24000 cr)"
  
  upstream_analysis_extraction:
    business_type_b04: "Manufacturing, capital-goods (CNC/VMC/HMC-DCM/VTL machines); asset intensity medium, WC intensity high, pricing moderate, cyclicality cyclical"
    moats_present_b04_b07: "1. Backward integration (sheet metal, spindle, coating, Macrotrol in-house) moderate durability; 2. Regulatory (DRDO/HAL/ISRO pre-qual) mod-high; 3. Brand/switching (NEXA premium, 39-city network) low-mod; B07 flags 99% imported controllers cap backward-integration lever"
    guidance_revenue_band_b05: "25-30% (stated FY26 & FY27); actual FY26 +27.3%, Q1 FY27 +56.1%"
    guidance_ebitda_margin_band_b05: "15-17% operating margin (printed 16.2% flat FY25-FY26); aspiration 25% gated on 60-acre land"
    management_credibility_grade_b05: "B (Good) | 5 delivered / 2 partial / 2 missed; FY26 revenue/EBITDA/PAT targets hit, Q1 FY27 ahead of guidance; 60-acre land slipped 3+ quarters, market-share unreconciled 4.5% vs 1-2%, machine volumes deflected every quarter"
    top_2_3_growth_triggers_b05: "1. Capacity 2500-machine utilization ramp to 90% FY27 (HIGH, near); 2. NEXA/premium mix past 40% order book (HIGH, near-medium); 3. 13-acre Metoda land execution (MEDIUM, medium-term)"
    em_score_b07: "15.0 (MODEST classification, 4 Moderate categories, 0 Strong, evidence mix documented 6 + claim 15 + inference 4)"
    evidence_mix_b07: "Claims-heavy (15 claim vs 6 documented); 4 documented items (E2 export growth, G1 net-cash self-funded, F2 Q1 FY27 +56.1%, PP&E +11.3% YoY)"
    primary_catalyst_12m_b07: "13-acre plant construction/utilization ramp + 60-acre land signing decision (undated, slipped Dec-2025 → Mar-2026 → pending)"
    capex_embedded_growth_pct_b07: "70 (FY26 capex 15.36 cr on revenue growth; 13-acre Phase 1 Rs 30-35 cr FY27 per concall)"
    block_b_trend_b01: "Deteriorating: 0.70x (FY24) → 0.27x (FY25) → 0.41x (FY26), cumulative 0.4538x; deal-breaker <0.50 threshold"
    receivables_trend_b02: "Deteriorating | gross >6mo ageing 15.4% from 12.2%, net +57.5% YoY vs revenue +8.6%, turnover down 33% (9.32x vs 13.97x), implied days 26→39"
    promoter_verdict_b08: "TRUSTWORTHY | 73.2% holding, 0% pledge stable 12 quarters, clean audit history, zero promoter red flags"
    fii_dii_ownership_latest_b08: "0.96% (FII 0.57% + DII 0.39% Jun-2026, up from 0% Sep-2023)"
  
  deliberation_authoritative_carries:
    fttcp_roce_forward_verdict: "STAGNANT (deliberation p.23 & p.70; Pillar 1 uses CURRENT ROCE 23.75%, normalization route NONE, recovery NOT credited)"
    pillar_1_base_roce_pct: "23.75 (AR Note 38vi FY25, capital-employed per deliberation; reconcile screener 29.1% basis difference at stage 10/11)"
    pillar_2_cash_multiplier: "INDETERMINATE | provisional 1.00x on FY26 CFO/PAT 0.41x, downside 0.80x (deliberation p.71)"
    pillar_3_growth: "+2x (3a +2x order book 1.37x revenue capex 70% grade B, 3b +0x EM 15<25, 3c +0x tenor <2.5x)"
    strategic_premium_x: "+0x (no pricing power, ROCE re-rating barred STAGNANT)"
    ua_applies: "YES | all three qualifiers met: listed 2018, Gate0 67≥60, FII+DII 0.96%<3%; multiplier 1.25x capped sector 25x"
    sector_cap_corrected_x: "25x (Cables/Industrial products; manifest Pharma/CDMO 38x superseded deliberation p.15)"
    destination_exit_pe_x: "25.0 (additive raw 26.75x = 21.4x × 1.25 UA capped sector 25x; RRM track 16-17x noted lower reality)"
    earnings_basis_chosen: "ONE-YEAR-FORWARD (operator-chosen p.40-43; apply 25x to FY27 EPS)"
    shared_catalyst_flag: "13-acre capex + 60-acre land single point of failure revenue AND margin/ROCE narratives (deliberation p.81)"
    disposition_gate_fttcp: "PROCEED WITH CAVEATS (capped INDETERMINATE cash determination, deliberation p.52)"
    valuation_verdict_at_cmp: "AVOID (fair value ~Rs 1,100 at 25x one-year-forward, CMP Rs 1,481; Hurdle STOPS base 1.45 bull 1.83; entry Rs 563 MoS Rs 451)"
  
  ua_qualifiers_all_checked:
    listed_12m_plus: "YES (listed 2018, NSE main 2020, >6 years as of 2026-07-30)"
    gate0_or_em_meets: "YES (Gate0 67≥60 per B01)"
    fii_dii_lt3pct: "YES (0.96% Jun-2026 per B08)"
    all_three_met: "YES"
  
  credibility_grade_carrier: "B (Good) | per B05: 5 delivered FY26 targets, 2 partial (25% margin, JV stuck NDA), 2 missed (60-acre land slip, market-share deflection) across 9 tracked; strong financial delivery, weak on optionality execution"

conflicts:
  - field: "ROCE FY25"
    value_a: "23.75%"
    anchor_a: "AR Note 38(vi) audited capital-employed basis"
    value_b: "29.1%"
    anchor_b: "Screener card operator-supplied (capital-employed basis unspecified)"
    used: "23.75% (deliberation p.36-38 confirms for Pillar 1 use; sector cap ceiling applies both)"
    note: "Reconciliation of capital-employed definition deferred stage 10/11 per phase-3 dependencies (deliberation p.83)"
  - field: "PAT Margin FY25"
    value_a: "12.00%"
    anchor_a: "AR Note 38(vi) and MD&A p.85"
    value_b: "9.72%"
    anchor_b: "Direct P&L computation 25.44/261.82 + AR front-matter KPI p.4"
    used: "9.72% (conservative direct P&L per B03 triple-pass kill-switch p.26-27)"
    note: "~2.3pp unreconciled gap; P&L and KPI both show decline FY24 10%→FY25 9.72%, opposite MD&A disclosure"

unresolved:
  - field: "Forward FY27 EPS (full-year committed)"
    why: "Management guidance states revenue 28-30% growth for FY27 but does NOT publish full-year EPS guidance; Q1 FY27 PAT Rs 9.58 cr (+110% YoY) when annualised ~38.3 cr is not sustainable run-rate; operator-approved earnings basis ONE-YEAR-FORWARD per deliberation but exact figure remains in forecast domain outside stage 10 copy-only mandate"
    where_it_might_be: "B05 Q4 FY26 concall transcript (May 2026); Q1 FY27 results show quarter annualised; operator fair-value illustration in deliberation p.42 implies Rs 44/share but this is derived illustration not independently anchored"
  - field: "FY26 ROCE reconciliation (23.75% AR vs 29.1% screener capital-employed basis difference)"
    why: "AR Note 38 capital-employed definition clear per audit; screener basis definition not specified; may exclude lease liabilities or use alternative working capital adjustments; deliberation confirms 23.75% for Pillar 1 but stage 10 instructed to reconcile"
    where_it_might_be: "FY26 results audited balance sheet (extracted p.6 but not detailed equivalent to FY25 AR Note 38(vi) full disclosure); potential FY26 Q4 standalone audit file restatement; deliberation p.36 & p.83 phase-3 dependency"
  - field: "Credit Rating & Working Capital Commentary"
    why: "Rating PDF NOT PROVIDED in inputs per task specification"
    where_it_might_be: "Not in inputs/ directory"
  - field: "Book Value per Share FY26 (post-audited balance-sheet basis)"
    why: "FY25 AR provides detailed equity breakdown (share capital 1000.42 + other equity 13282.00 = 14282.42); FY26 results balance sheet p.6 audited but less granular in equity presentation; full FY26 audited statement may not have been filed as comprehensive as FY25 AR"
    where_it_might_be: "FY26 Q4 results standalone statements; potential full FY26-27 AR when filed (expected Aug-2025 for FY24-25 precedent)"
  - field: "Peer financial data complete (P/E, EV/EBITDA, P/B, detailed growth multiples)"
    why: "B06 peer section does not provide quantified financial multiples for JYOTICNC, ADOR, KLBRENG; only narrative concall discussions and industry trends cited; complete peer ROCE, P/B, detailed EV/EBITDA NOT PROVIDED"
    where_it_might_be: "B06 notes "peer financial data was provided" but direct multiples extraction incomplete; peer concall transcripts (cited but exact pages not extracted); JYOTICNC/ADOR/KLBRENG respective annual reports (not in inputs/)"

rating_wc_quote: "NOT PROVIDED (no rating PDF in inputs)"

ua_qualifiers:
  listed_12m: true
  gate0_or_em: true
  fii_dii_lt3: true
  all_met: true

credibility_grade: "B"
```

---

## END OF REPORT

**Report Status:** COMPLETE  
**Assembly Model:** Claude Haiku 4.5 20251001  
**Report Date:** 2026-07-30  
**Data Freshness:** FY26 Audited (31-Mar-2026); Q1 FY27 Unaudited (30-Jun-2026); FY25 AR Audited (29-May-2025)

**Handoff to Stage 11 Valuation (Role 1, Opus):**  
All inputs anchored and conflicts documented. Deliberation record OPERATOR-APPROVED VALUATION PILLARS block carried verbatim. Phase-3 dependencies flagged (FY26 ROCE reconciliation, cash determination closure, forward EPS confirmation). Ready for final valuation assembly and dual-track (additive + RRM) assessment per framework.
