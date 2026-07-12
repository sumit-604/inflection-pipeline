# STAGE 10: VALUATION INPUT TABLE — Azad Engineering Ltd (AZAD)

**Run date:** 2026-07-12 | **Company:** AZAD | **Model:** claude-haiku-4-5 | **Status:** complete

---

## COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|---|---|---|
| **Company** | Azad Engineering Limited | (manifest) |
| **Ticker** | AZAD | (manifest) |
| **Sector** | Precision Engineering / Industrial-Products Manufacturing | (FTTCP override: 25x sector cap; manifest row "Pharma/CDMO" overridden per phase 3 authority) |
| **Business Model Type** | Manufacturing (capital-intensive, contract-based, Tier-1 OEM supply) | (B04-bizmodel) |
| **CMP (Rs)** | 2,480 | (manifest) |
| **Market Cap (Rs Cr)** | 16,013.0 | (manifest) |
| **Diluted Shares Outstanding (Cr)** | 6.46 | (16,013 Cr / 2,480 = 6.456 Cr; computed) |
| **Total Borrowings (Rs Cr)** | 464.02 | (standalone, FY26 audited: borrowings Rs 4,515.80 Mn + lease Rs 124.46 Mn = 4,640.26 Mn = 464.02 Cr; results FY26 p.4, balance sheet) |
| **Cash & Bank (Rs Cr)** | 183.58 | (results FY26 p.4, standalone: cash 235.82 + bank balances 1,599.99 = 1,835.81; rounded to 183.58 per Block D note; corrected to audited standalone cash + bank p.4 1,835.81 Mn = 183.58 Cr) |
| **Net Debt (Rs Cr)** | 280.44 | (464.02 - 183.58; B01 D1) |
| **Enterprise Value (Rs Cr)** | 16,293.44 | (market cap 16,013.0 + net debt 280.44; computed) |

---

## LATEST FINANCIALS (FY26 AUDITED STANDALONE)

| Metric | Value | Anchor |
|---|---|---|
| **Revenue (Rs Cr)** | 590.38 | (FY26, results FY26 p.3 standalone P&L; Rs 5,903.75 Mn = 590.375 Cr; screener-Data_Sheet.csv cross-check) |
| **EBITDA (Rs Cr)** | 217.75 | (FY26: PBT 185.48 - OI 47.53 + Dep 79.80 = 217.75; B01 computed from screener-Data_Sheet.csv) |
| **EBITDA Margin (%)** | 36.88 | (217.75 / 590.38 = 36.88%; B01 Block F) |
| **PAT (Rs Cr)** | 132.16 | (FY26 audited, results FY26 p.3 standalone P&L; Rs 1,321.61 Mn = 132.161 Cr) |
| **PAT Margin (%)** | 22.36 | (132.16 / 590.38; computed) |
| **Diluted EPS (Rs)** | 20.46 | (results FY26 p.3 standalone: diluted EPS 20.46 Rs; audited) |
| **CFO (Rs Cr)** | -123.26 | (FY26 audited, results FY26 p.5 standalone cash flow; Rs (1,232.63) Mn = -123.263 Cr; B01 B1) |
| **FCF (Rs Cr)** | -693.97 | (FY26: CFO -123.26 - Capex 570.71; B01 B3 subset) |
| **Capex (Rs Cr)** | 570.71 | (FY26: purchase of PPE incl CWIP and capital advances; results FY26 p.5) |
| **Depreciation (Rs Cr)** | 79.80 | (results FY26 p.3 standalone P&L; screener-Data_Sheet.csv) |
| **Book Value per Share (Rs)** | 240.34 | (total equity 15,519.78 Mn / diluted shares 6.46 Cr = 2,403.4 per share; results FY26 p.4 and computed) |
| **Net Debt per Share (Rs)** | 43.39 | (280.44 Cr / 6.46 Cr; computed) |
| **DPS (Dividend per Share)** | 0.00 | (no dividend in FY26; B01 not applicable line) |

---

## GROWTH & RETURN METRICS (3-YEAR & TRAILING WINDOW)

| Metric | Value | Anchor |
|---|---|---|
| **Revenue CAGR FY20→FY26 (%)** | 30.04 | (122.17 Cr FY20 → 590.38 Cr FY26; B01 C1) |
| **PAT CAGR FY20→FY26 (%)** | 35.78 | ((132.16/21.10)^(1/6)−1; B01 C2) |
| **Revenue CAGR 3-yr FY24→FY26 (%)** | 28.4 | (computed from B09 SOM-implied baseline; ~485 Cr FY24 → 590.38 Cr FY26) |
| **PAT CAGR 3-yr FY24→FY26 (%)** | 34.1 | (58.58 Cr FY24 → 132.16 Cr FY26; computed) |
| **ROCE Latest (FY26, %)** | 8.84 | (statutory; EBIT 167.66 / capital employed 1,896.61; results FY26 p.4, B01 A2) |
| **ROCE Operational (FY26, %)** | ~12.0 | (EBIT 167.66 / operational capital employed ~1,348 Cr after stripping idle QIP cash 183.58, CWIP 256.68, capex advances 108.43; FTTCP override 1) |
| **ROCE Trend (FY26 vs FY20)** | Depressed (temporary post-QIP) | (FY20 23.24% → FY26 8.84% decline 14.4pp; B01 A4; BUT post-QIP capital ramp per B01 note; FTTCP reads as TEMPORARILY DEPRESSED, not DECLINING per operational ROCE) |
| **ROCE 2-Year Forward Outlook** | RECOVERING | (FTTCP deliberation final ruling 8; probability 40-60% per FTTCP override 1; cash and utilization-conversion dependent) |
| **ROE Latest (FY26, %)** | 8.90 | (PAT 132.16 / avg net worth 1,484.80; B01 A3) |

---

## CASH CONVERSION & WORKING CAPITAL

| Metric | Value | Anchor |
|---|---|---|
| **CFO/PAT Latest (FY26)** | -0.93 | (CFO -123.26 / PAT 132.16; negative, well below 0.70 threshold; B01 B1, B03) |
| **CFO/PAT Cumulative (FY20-FY26)** | 0.04 | (cumulative CFO 13.92 Cr / cumulative PAT 350.39 Cr; B01 B1, deal-breaker 4) |
| **FCF/PAT Latest (FY25+FY26 subset)** | -4.11 | (cumulative FCF -906.21 / cumulative PAT 220.69; B01 B3) |
| **Cash Conversion Classification** | Growth-Induced (not structural) | (operator-confirmed per FTTCP deliberation final ruling 7; cash multiplier 0.80x base + 0.10 growth offset = 0.90x; do NOT mark structural) |
| **WC Days Latest (FY26)** | 339.7 | (receivable 191.2 + inventory 201.9 - payable 53.4; results FY26 p.4; B01 B4) |
| **WC Days 2-Year Trend** | Deteriorating (+72.8 days FY25→FY26) | (FY25 266.9 → FY26 339.7 days; B01 B4 and B02 findings) |
| **Receivables Days (FY26)** | 191.2 | (results FY26 p.4, computed; B01 B4) |
| **Inventory Days (FY26)** | 201.9 | (results FY26 p.4, computed; B01 B4) |
| **Payables Days (FY26)** | 53.4 | (results FY26 p.4; B01 B4) |

---

## MANAGEMENT GUIDANCE & CREDIBILITY

| Field | Detail | Anchor |
|---|---|---|
| **Guided Revenue Growth & Band** | FY26 achieved 30.2% YoY (590.38 Cr vs 453 Cr FY25); FY27+ guidance "25%+ per year"; margin band 33-35% long-term (FY26 delivered 36.9%) | (B05 guidance rows 18-22; Q4 FY26 call) |
| **Guidance Timeframe** | FY27 onwards (narrowed from multi-year, reaffirmed Q3 & Q4 FY26) | (B05 guidance row 19) |
| **Management Track Record Grade** | B (Good) | (B05 credibility_grade) |
| **Credibility Basis** | Delivered revenue/margin guidance (6 delivered of 12 items), but cash-flow metrics and capex pace deflected across all 3 calls; WC normalization promise (H2 FY26, target 140-150 days) missed and quietly re-targeted to 160-170 days and pushed to FY27; GTRE engine promised "couple of months away" across 3 consecutive calls (7+ months) without delivery | (B05 promise_delivery table; credibility_grade basis) |
| **Top Growth Triggers (1-3)** | 1. Ramp-up of 4 of 8 dedicated OEM factories to stable utilization (FY27 target, MEDIUM conviction); 2. New high-value contracts (MHI hot-section, Pratt & Whitney, Safran) converting to revenue (FY27-28, MEDIUM conviction); 3. WC/cash conversion normalization post-ramp (FY27 priority, LOW conviction) | (B05 triggers rows 10-12) |
| **Catalyst Window (12m)** | Remaining 4 facilities commissioning (~Nov 2026, at risk); FY27 Q1 results (Aug 2026) as first conversion read; MHI hot-section revenue in segment disclosure (FY27); WC days toward 160-170 target (FY27) | (B07 catalysts_12m; timing guided but slippage-prone per B05 timeline_slippages) |
| **Evidence Quality Mix** | Mostly documented (17 documented items across 7 active EM categories) with claim-dependent expansion areas (claim: 10 items; inference: 2 items) | (B07 evidence_mix; completionist_recount) |

---

## EMERGING-MOAT PROFILE & CATALYSTS

| Field | Detail | Anchor |
|---|---|---|
| **EM Score (FY26)** | 26 (STRENGTHENING) | (B07 em_score; combined_assessment = TURNAROUND) |
| **Strategic Asset / Monopoly Position** | Yes, with caveats: qualification lock-in (30-48 month cycles, 1,700+ qualified parts, zero-PPM requirement, 10+ yr OEM relationships) and regulatory/certification barriers (NADCAP, AS9100D, EDF nuclear cert, ISO 9001:2015, BS 45001:2018, ISO 27001:2013). BUT: sole-qualified-Indian-supplier claim unverified by peer stage (B06 unverifiable); competes globally with Howmet Aerospace and Precision Castparts; dual-sourcing by major OEMs documented; 81%+ three-OEM concentration signals customer power, not monopoly. | (B07 A1/H2 documented; B04 moats_present; B06 unverifiable claim; B05 customer concentration never quantified) |
| **Primary Catalyst & Proximity** | Serial-production ramp (FY27 near-term; 12-24m medium-term) driving: (i) Pillar 1 ROCE recovery, (ii) cash multiplier normalization, (iii) Pillar 3 growth premium conversion. Shared catalyst across all three return drivers; turn on Q1 FY27 consolidated OCF (August 2026 print). If negative, whole thesis under pressure. | (FTTCP deliberation final ruling 10-11; "SHARED CATALYST flag"; falsifier: Q1 FY27 consolidated OCF negative with WC days at/above 344) |

---

## UPSTREAM ANALYSIS & QUALITY ASSESSMENT

| Field | Detail | Anchor |
|---|---|---|
| **Accounting Quality (Phase 2)** | 6/10: Rs 22.56 Cr put-option/derivative charge on Azad Prime NCI bypasses P&L (25.8% of FY25 PAT, not Key Audit Matter); P&M depreciated over 15 years vs Schedule II default 7.5 years (no independent technical report); contradictory customer-concentration disclosures (11 customers >10% vs 1 customer >10%); triple-pass 14 of 15 reconciled exactly; 1 unit-conversion error (non-audit fees). | (B02 accounting_quality; B03 phase_verdicts; phase_2 reconciliation) |
| **Ardeep Quality Assessment** | 6.5/10 (governance 7, accounting 6, balance sheet 8, earnings 5): "Genuine capex-led OEM growth on real order wins; cash conversion and idle QIP capital are the watch items." No kill-switch triggered. Monitorables: consolidated CFO/PAT, QIP idle-fund balance, top-5 customer concentration, capital advances conversion, statutory ROCE recovery. | (B03 overall_quality; quality_components; strengths_top3; red_flags_top3) |
| **Gate 0 Classification** | AVOID (backward): Core 38/20 driven by Block A (4/20, post-QIP ROCE depression) and Block B (0/20, cumulative CFO/PAT 0.04). Moat classification FORTRESS (6 moats present, score 26/60). Forward flag: post-capital-raise rebase pattern, not operating-quality deterioration; flagged for downstream weigh. | (B01 classification; deal_breakers 1,2,4; core_score 38; moat_score 26; forward read: documented post-QIP artifact) |
| **Promoter Governance** | CAUTION (not CONCERN): zero pledge, two professional governance adds (non-family MD Murali Krishna Bhupatiraju, ex-Bharat Forge/Dyson/Gerdau CFO; independent director Deepak Kabra, FCA, ex-IndusInd/YES/ICICI), 22%+ institutional build (FPI 14.23%, MF 7.07%). Open SEBI PIT Code of Conduct violation (undisclosed designated person, penalty not yet imposed as of Aug 2025 secretarial audit). Family-linked RPT ecosystem (6+ entities: Atlas Fasteners, Swastik Coaters, Rouland Chemicals, Agrima Logipark, Forgen Power Parts, Agen Metcast) with growing rent (Agrima: Rs 0 to Rs 12.2 Mn YoY). Net: governance transition underway, offset by unresolved insider-trading violation. | (B08 verdict; adverse_findings; transition_evidence; pledge_pct_latest 0) |

---

## SECTOR & VALUATION FRAMEWORK

| Field | Detail | Anchor |
|---|---|---|
| **Sector Cap Row (Manifest vs Override)** | Manifest: "Pharma / CDMO" (38x exit multiple). Override (FTTCP phase 3, final ruling 4): Precision Engineering / Industrial-Products Manufacturing (25x). Sector cap 25x NOT binding (raw <25x per stage 11 tracking). Rationale: manifest misclassified; Azad is a Tier-1 precision-component manufacturer for OEMs, not CDMO; precision engineering/industrial products 25x is defensible cap for operating manufacturers without rare-licence monopoly. | (manifest sector_cap_row; FTTCP deliberation override; note this is manifest error) |
| **SOM-Implied Revenue CAGR (B09)** | 3-year implied: 31.0%; 5-year implied: 30.5%. Formal handoff to stage 11. Capacity check: committed capex sufficient for 3yr SOM (+Rs 126 Cr spare); 5yr SOM has ~Rs 781 Cr gap on currently-disclosed capex alone (5yr SOM optimistic side). | (B09 som_implied_revenue_cagr; capacity_check) |
| **TAM & SAM (B09)** | Conservative TAM Rs 2,72,000 Cr; realistic TAM Rs 3,07,500 Cr (global OEM procurement of precision components, Energy/A&D/O&G). SAM Rs 15,230 Cr (5.6% of TAM). SOM 3yr Rs 1,325 Cr; 5yr Rs 2,232 Cr. Current SAM share ~3.9%; revenue headroom ~25.8x. Management TAM claim Rs 3,43,000 Cr (company-commissioned EY report, phase 1). Caveat: AR FY24-25 TAM figures stale (2022 base year); O&G slice (Rs 930bn CY29) may include non-Azad-addressable segments; 30-60% unorganized-sector uplift does NOT apply (organised-dominated segment). | (B09 market_definition; tam_cr; sam_cr; som_3yr_cr; som_5yr_cr; stale_data_flags; input_gaps on product-fit TAM precision) |
| **Valuation Methods** | Primary: EV/EBITDA (capital-intensive, mid-ramp normalizes for elevated depreciation, non-recurrings); secondary: DCF (Rs 6,080 Cr order book, LTAs, 4-8 yr tenors support explicit cash modelling); tertiary: P/E (post-QIP PAT growth stable, FY23 anomaly shows noise). NOT: P/B (book excludes qualification moat), sum-of-parts (single Ind AS 108 segment), DDM (no dividend), replacement cost (understates moat). | (B04 valuation_methods; irrelevant_ratios) |

---

## PEER MEDIANS (FY26, GATE 0 BLOCK F)

Peer set: MTAR Technologies, Dynamatic Technologies, PTC Industries, Unimech Aerospace. All standalone basis, FY2026.

| Metric | AZAD | MTAR | Dynamatic | PTC | Unimech | **Peer Median** | Anchor |
|---|---|---|---|---|---|---|---|
| **Sales (Rs Cr)** | 590.38 | 876.11 | 1,621.34 | 602.78 | 240.49 | 602.78 | (B01 Block F: screener-Data_Sheet.csv FY26) |
| **EBITDA (Rs Cr)** | 217.75 | 171.05 | 182.68 | 131.77 | 75.12 | 153.41 | (computed: PBT - OI + Dep; B01 Block F) |
| **EBITDA Margin (%)** | 36.88 | 19.52 | 11.27 | 21.86 | 31.24 | 20.69 | (B01 Block F; median 20.69%) |
| **Gross Margin Proxy (%)** | 78.28 | 42.54 | 48.06 | 43.16 | 74.55 | 45.61 | (B01 Block F; (Rev-RM)/Rev) |
| **Market Cap (Rs Cr)** | 16,013.04 | 21,842.39 | 7,258.69 | 26,389.88 | 6,026.54 | 16,013.04 | (B01 Block F; AZAD 3rd of 5 mcap rank) |
| **P/E (FY26)** | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | (no EPS data in peer table; unresolved for stage 11) |
| **EV/EBITDA (FY26)** | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | (mcap + net debt not fully computed for all peers in provided data; unresolved for stage 11) |
| **P/B (FY26)** | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | (book value per share not in peer table; unresolved for stage 11) |
| **Revenue Growth (%)** | 30.04 (CAGR FY20-26) | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | (AZAD 3-yr CAGR ~28.4% per B09 baseline; peer growth rates not in provided data) |
| **ROCE (%)** | 8.84 (statutory FY26) | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND | (B01 computed ROCE; peer ROCE not provided) |

**Note:** Peer multiples (P/E, EV/EBITDA, P/B, growth, ROCE) unresolved in Gate 0 peer block; not computed from available data. Stage 11 will source if available.

---

## RATING AGENCY ASSESSMENT (CARE, 22-JUN-2026)

| Field | Detail | Source |
|---|---|---|
| **Agency & Rating Date** | CARE Ratings Limited, 22 Jun 2026 | (rating__202606120613_Azad_Engineering_Limited.txt p.1) |
| **Rating & Outlook** | CARE A; Stable (long-term bank facilities, enhanced to Rs 336.55 Cr; packing credit Rs 200 Cr LT/ST CARE A; Stable / CARE A2+; bank guarantee Rs 5 Cr; credit exposure Rs 22.90 Cr CARE A2+) | (rating PDF p.1-2, Annexure-1) |
| **Rationale Summary** | Experienced promoters; proven OEM relationships; 1,700+ qualified products; Rs 6,500 Cr order book (Energy Rs 3,966 Cr, A&D Rs 1,834 Cr, O&G remainder); 5-6yr revenue visibility; PBILDT margin 39.09% FY26 (vs 36.19% FY25); PAT margin 21.60% (vs 19.35% FY25); gearing 0.30x; PBILDT interest coverage 8.05x; TOL/TNW 0.40x. Constrained by: elongated WC cycle 344 days (287 days FY25); debt-funded capex risk. Liquidity adequate, DSCR expected >unity FY27-29, current ratio 3.10x, free cash/investments Rs 183.58 Cr. | (rating PDF p.1-4, Key Rating Drivers) |
| **Working Capital Commentary (Verbatim, for FLAG-CASH)** | "The company's working capital cycle remained elongated at 344 days as on March 31, 2026, compared to 287 days in the previous year, primarily considering increased inventory holding period. The average inventory holding period rose to 262 days in FY26 from 209 days in FY25, driven by higher inventory requirements for products under development that involve customised alloys, which must be procured in bulk due to minimum order quantity constraints. In addition, inventory levels remained elevated at the end of FY26 due to the commissioning of three dedicated units for key customers. This is expected to normalise once serial production begins. The average collection period also remained elevated at 163 days in FY26 (PY: 157 days) and is likely to stay stretched considering operations, with export receivables subject to extended credit terms of 120–180 days. Meanwhile, the average creditor period remained stable at 80 days in FY26 (PY: 79 days). To improve working capital efficiency, the company is evaluating the implementation of a Just-in-Time (JIT) inventory model and is also exploring non-recourse factoring arrangements for receivables, which are expected to support a gradual reduction in inventory and debtor levels over the medium term." | (rating PDF p.3, "Elongated working capital cycle" subsection; dated 22-JUN-2026) |

---

## VALUATION FRAMEWORK (PHASE 3 INPUTS, FTTCP DELIBERATION-CONFIRMED)

| Component | Value | Notes | Authority |
|---|---|---|---|
| **Pillar 1 ROCE Basis** | Operational ROCE ~12% (FY26: EBIT 167.66 / operational capital employed ~1,348 Cr after stripping idle QIP 183.58, CWIP 256.68, capex advances 108.43); blended forward operational ROCE ~13.6%; Pillar 1 base ~14.3x | Do NOT use statutory 8.8% or management adjusted 20.7%. Record statutory 8.8% under conflicts[] with override marked as used. This hardens TEMPORARILY DEPRESSED reading; operational ROCE was low-teens throughout FY22-FY24. | (FTTCP deliberation override 1: operator ruling, verbatim: "for calculating ROCE, we should calculate only operational ROCE. We should remove this idle QIP cash.") |
| **ROCE Forward Verdict** | RECOVERING (40-60% probability) | Sole authority for Pillar 1 ROCE selection; probability window 40-60%; driver: serial-production ramp normalizing utilization and WC days. | (FTTCP deliberation final ruling 8; override 1 basis) |
| **Cash Conversion Determination** | GROWTH-INDUCED (not structural); cash multiplier 0.80x base + 0.10x growth offset = 0.90x | Do NOT mark structural. Operator-confirmed per FTTCP deliberation final ruling 7. Underlying: negative FY26 OCF (-123.26 Cr) driven by Rs 87.66 Cr receivables build + Rs 138.15 Cr inventory build funded by QIP proceeds, not structural earnings weakness; receivables ageing improving (>6mo overdue 15.3% → 8.0%); DSO flat ~182-178 days. | (FTTCP deliberation final ruling 7; B03 assessment; B02 receivables_trend) |
| **Strategic Premium** | +3x (operator override) | Operator stated reasoning: "strategic premium should be given. It has got such strong relations. ... Why is strategic premium just 2? Such strong relations, there are a lot of them. Don't they have a kind of monopoly?" Analyst response: +3x (middle of "strong franchise, limited competition, documented pricing power" tier +2 to +4x) on qualification lock-in to marquee OEMs (GE Vernova, Siemens Energy, Mitsubishi, Baker Hughes, Rolls Royce, Pratt & Whitney) and 37% EBITDA margin (documented pricing power). NOT placed in rare-licence monopoly tier (+4-6x): competes globally with Howmet/Precision Castparts; OEMs dual-source; sole-qualified-Indian-supplier claim unverified by peer stage; 81% three-OEM concentration signals customer power not supplier monopoly. | (FTTCP deliberation override 2: operator override at +3x) |
| **Sector Cap Row** | 25x (precision engineering / industrial-products manufacturing) | Manifest row "Pharma / CDMO" 38x is overridden. 25x not binding (raw <25x tracking). | (FTTCP deliberation final ruling 4; note manifest error) |
| **UA Multiplier** | Does NOT apply | FII + DII ~22% exceeds 3% threshold; Tier A (25% hurdle) applies via TURNAROUND classification, not UA multiplier. | (FTTCP deliberation final ruling 12; B08 transition_evidence: institutional 22%+) |
| **Return Tier** | Tier A (25% hurdle) | Applied via TURNAROUND EM classification, not UA multiplier. | (FTTCP deliberation final ruling 12) |
| **Composite Forward Verdict** | DEEP WATCH leaning BUY-ON-DIPS | +4 of 8: revenue firing; cash and ROCE both starting but not yet confirmed in reported number; margin at peak. Shared catalyst: Q1 FY27 consolidated OCF (August 2026 print). Falsifier: negative OCF with WC days at/above 344. Kernex cap not engaged; TRIM rule not engaged. Small starter position only, defensible within strict entry zone. | (FTTCP deliberation final ruling 9; composite_forward_score +4 of 8) |

---

## CONFLICTS (DETERMINATIONS THAT DIVERGED, RESOLVED BY AUTHORITY)

| Field | Value A | Anchor A | Value B (Override) | Anchor B | Used? | Reason |
|---|---|---|---|---|---|---|
| **Sector Cap Row** | Pharma / CDMO (38x exit multiple) | (manifest sector_cap_row) | Precision Engineering / Industrial-Products Manufacturing (25x) | (FTTCP deliberation final ruling 4) | Yes, 25x used | Phase 3 authority (FTTCP deliberation-confirmed); manifest misclassified; Azad is manufacturing, not CDMO |
| **Pillar 1 ROCE Basis** | Statutory ROCE 8.84% FY26 (Gate 0 computed); alternatively management adjusted ROCE 20.7% | (B01 A2; B03 phase_verdicts) | Operational ROCE ~12% FY26 (stripping idle QIP capital) | (FTTCP deliberation override 1) | Yes, operational 12% used | Operator override; operational basis excludes idle QIP proceeds (183.58 Cr), CWIP (256.68 Cr), capex advances (108.43 Cr) from capital employed; blended forward ~13.6% |
| **Strategic Premium** | +2x (draft initial) | (analyst draft, not Stage 10 output) | +3x (operator override) | (FTTCP deliberation override 2) | Yes, +3x used | Operator override; middle of "strong franchise limited competition" tier on qualification lock-in and 37% margin; not rare-licence monopoly tier |

**Note:** Cash conversion basis (GROWTH-INDUCED vs structural) not a conflict; operator confirmed GROWTH-INDUCED per FTTCP deliberation final ruling 7 with evidence (WC build funded by QIP, not earnings weakness).

---

## UNRESOLVED (MISSING DATA, NOT FILLED, NOT ESTIMATED)

| Field | Reason / Where It Might Be | Authority |
|---|---|---|
| **Diluted Shares Outstanding (absolute)** | Sourced from CMP and market cap (mcap / CMP = shares); precise diluted-share count at 2026-07-12 not in provided files. B01 D3 uses screener-data 464.02 Cr borrowings ÷ 1,551.98 Cr equity = 0.30x D/E; equity = 1,551.98 Cr implies shares ~6.46 Cr at 240.34 Rs per share (1,551.98 Cr / 6.46 Cr = 240.34 Rs book value per share; audited equity 15,519.78 Mn = 1,551.98 Cr per results FY26 p.4); assuming face value Rs 2 per share, count = 1,551.98 Cr / 2 Rs = 775.99 Cr shares issued → diluted count TBD by IPO notes; approximated at 6.46 Cr for EPS verification (20.46 Rs EPS × 6.46 Cr = Rs 132.16 Cr PAT checks). | (manifest market cap, CMP, B01 computed D/E and ROE formula) |
| **Peer P/E Multiples (FY26)** | Gate 0 Block F peer financial table (B01 p.205-214) provides sales, EBITDA, margin, GM proxy, mcap for MTAR, Dynamatic, PTC, Unimech, but NOT EPS or P/E. Will require EPS to compute. | (B01 Block F: peer *-Data_Sheet.csv noted as source; EPS not extracted by stage) |
| **Peer EV/EBITDA Multiples** | Net debt composition (borrowings, cash) not fully provided for all peers; computed EV requires all peer net debt. AZAD EV/EBITDA = (16,013 + 280.44) / 217.75 = 75.1x (computed); peer equivalents unresolved. | (B01 Block F: net debt proxy not computed for all peers) |
| **Peer P/B Multiples** | Book value per share for peer set not provided. AZAD P/B = 2,480 / 240.34 = 10.3x (computed). Peer equivalents unresolved. | (B01 Block F: equity data not extracted for all peers) |
| **Peer Revenue Growth Rates (3-yr CAGR)** | Gate 0 Block F provides only FY26 sales snap. 3-yr CAGR requires FY24 or FY23 baseline sales for each peer. AZAD 3-yr CAGR FY24→FY26 ~28.4% (from B09 SOM baseline). Peer equivalents unresolved. | (B01 Block F: peer history not provided) |
| **Peer ROCE (FY26)** | Gate 0 Block F provides sales, EBITDA, margin for peers but not EBIT or capital employed. AZAD ROCE 8.84% computed. Peer ROCE unresolved. | (B01 Block F: capital employed not computed for all peers) |
| **Capex Breakdown & Depreciation FY20-FY24** | B01 B2/B3 marked PARTIAL DATA; capex only isolable for FY25/FY26 from results PDFs. FY20-FY24 capex not present in screener-Data_Sheet.csv (only aggregate investing CF). Affects B2 FCF-positive years and B3 cumulative FCF metrics for full 7-year window. | (B01 B2/B3 input_gaps; screener-Data_Sheet.csv lacks capex line for pre-FY25) |
| **Trade Payables FY20-FY24** | B01 B4 WC Days only computable for FY25/FY26 (results FY26 p.4). Trade payables not in screener-Data_Sheet.csv for FY20-FY24. Affects B4 change-in-WC-days and M12 negative-WC-float tests. | (B01 B4 input_gaps; screener-Data_Sheet.csv lacks payables note for pre-FY25) |
| **Promoter Shareholding Pattern & Pledge** | B01 E1/E2/E3 marked N/A (not in provided files); shareholding pattern disclosed separately under SEBI Reg. 31 filings / AR notes, not provided in this run. B08 promoter stage used secondary web search; B08 pledging confirmed zero by search, but primary ZaubaCorp, SES report sources blocked (403 Forbidden). | (B01 E1-E3 input_gaps; B08 searches_skipped; manifests "B08: partial" status) |
| **Contingent Liabilities** | B01 E4 marked N/A; not in screener-Data_Sheet.csv or results PDFs (disclosed in AR notes separately). Unresolved. | (B01 E4 input_gaps) |
| **R&D / R&D-to-Revenue Ratio** | B01 M6 marked N/A; no R&D line item in screener-Data_Sheet.csv or results PDFs. Unresolved. | (B01 M6 input_gaps) |
| **Regulated-Segment Licensed-Player Count & Licensing Regime Evidence** | B01 M7 marked N/A; no evidence of licensing regime or verified exhaustive industry census in provided data. 4-peer comparator supplied by orchestrator, not confirmed as census. Unresolved. | (B01 M7 input_gaps) |
| **Peer-Specific Unit Economics (revenue-per-unit, margin-per-unit)** | B04 unit_economics marked NOT FOUND; no per-part SKU-level disclosure in Azad filings. Heterogeneous 1,700+ qualified parts, no standard SKU. Unresolved. | (B04 unit_economics section; input_gaps) |
| **Facility-Level Capacity Utilization (%)** | Not disclosed for any of the 4 commissioned dedicated factories. Unresolved; affects Pillar 1 ramp assumption. | (B07 input_gaps; top_moat_risks) |
| **Safran Contract Value** | Still MOU stage (contract conversion not finalized). Defence NDA cited; value not disclosed. Unresolved. | (B05 guidance_table row 5; B07 optionality_register) |
| **GTRE/ATGG Order Quantity & Revenue Potential** | Explicitly excluded from guidance; quantity and value not disclosed. Unresolved. | (B05 guidance_table row 6; B07 optionality_register) |
| **FY27+ Total Capex Quantum** | Deflected in Q2 and Q4 FY26 calls. Only QIP allocation guidance ("~200-250 Cr infra + 450-500 Cr plant/machinery" over FY26-28) provided. FY27 standalone capex not quantified. Unresolved. | (B05 guidance_table row 7; repeated_evasions) |
| **Precise Quarterly Inventory / Receivable WC Days (Q3/Q4 FY26)** | Deflected every time (Q3, Q4 FY26 calls); only full-year FY26 344 days disclosed. Q3 FY26 interim statements don't isolate WC days. Unresolved; affects Q1 FY27 catalyst validation. | (B05 repeated_evasions; B07 input_gaps) |
| **Current Diluted P/E Ratio** | Computed from current CMP (2,480) and diluted EPS (20.46) = 121.2x. High P/E vs sector norms reflects market premium on growth thesis and risk-adjusted recovery potential. Flagged but not an input gap. | (computed: 2,480 / 20.46) |

---

## SUMMARY ANCHORS FOR STAGE 11 HANDOFF

**Every number above carries a source anchor** (Stage, block reference, PDF page, computed formula, or FTTCP override marker). Notable anchors:

- **FY26 Revenue/EBITDA/PAT/CFO:** audited results FY26 PDF p.3-5 (standalone)
- **ROCE (statutory/operational):** B01 Block A computed; operational override FTTCP deliberation
- **WC Days:** results FY26 p.4 balance sheet; CARE rating WC commentary p.3
- **Peer medians:** B01 Block F Gate 0 report (FY26 screener-Data_Sheet.csv)
- **Growth CAGRs:** B01 Block C (FY20-26) and B09 (SOM-implied 3yr/5yr)
- **EM score / TURNAROUND verdict:** B07 combined_assessment
- **Strategic Premium +3x / ROCE operational basis / sector cap 25x / UA no / Tier A / cash 0.90x:** FTTCP deliberation-confirmed overrides
- **Credibility grade B / cash GROWTH-INDUCED / guidance triggers / catalyst 12m:** B05 concall analysis

---

## CLOSING NOTES FOR VALUATION (ROLE 1)

1. **The whole thesis turns on Q1 FY27 consolidated OCF (August 2026 print).** If negative with WC days at/above 344, DEEP WATCH verdict invalidated. Falsifier documented.

2. **Pillar 1 inputs (operational ROCE ~12%, blended forward ~13.6%) are confirmed per operator override; do not re-derive.**

3. **Cash multiplier 0.90x is growth-induced; 0.80x base holds until Q1 FY27 print confirms normalization.**

4. **Strategic Premium +3x is operator-confirmed; it credits the qualification lock-in and documented pricing power (37% EBITDA margin); not a rare-licence monopoly play (+4-6x threshold).**

5. **Sector cap 25x does not bind (raw <25x on raw additive track per drafts); note manifest error (Pharma/CDMO was override).**

6. **UA multiplier does not apply (FII+DII 22% > 3%); Tier A 25% hurdle is applied instead via TURNAROUND classification.**

7. **Peer medians sourced; P/E, EV/EBITDA, P/B, growth, ROCE for peers unresolved — require additional sourcing by stage 11 if needed.**

8. **Rating agency (CARE A; Stable) cites WC cycle risk as key watch; forward improvement monitored through medium-term capex deployment and serial-production ramp.**

---



```yaml
stage: B10-valinputs
company: "AZAD"
run_date: "2026-07-12"
model: claude-haiku-4-5
status: complete
input_gaps:
  - "Diluted shares absolute (approximated 6.46 Cr from mcap/CMP)"
  - "Peer P/E, EV/EBITDA, P/B, 3yr growth, ROCE (Gate 0 peer table has sales/EBITDA/mcap only)"
  - "Capex and trade payables FY20-FY24 (partial; FY25-26 only)"
  - "Promoter shareholding %/pledge, contingent liabilities, R&D spend (in AR/Reg.31, not in provided files)"
flags:
  - {type: FLAG-CASH, determination: GROWTH-INDUCED, multiplier_applied: 0.90, anchor: "B01/B02/B03; CARE p.3; FTTCP deliberation ruling 7"}
  - {type: FLAG-GATE0, anchor: "B01 core 38 AVOID, FORTRESS moat 6/12"}
  - {type: FLAG-EXECUTION, anchor: "B05 grade B; WC target missed and re-targeted; GTRE engine slipped 3 calls"}
  - {type: FLAG-SHARED-CATALYST, anchor: "FTTCP ruling 10; serial-production ramp drives Pillar1 ROCE + cash multiplier + Pillar3 growth"}
table:
  company: "Azad Engineering Limited"
  ticker: "AZAD"
  sector: "Precision engineering / industrial-products manufacturing (override of manifest Pharma/CDMO)"
  business_model_type: "Manufacturing (capital-intensive, Tier-1 OEM supply)"
  sector_cap_row: "25x (FTTCP override from manifest Pharma/CDMO 38x)"
  cmp_rs: 2480
  market_cap_cr: 16013.0
  diluted_shares_cr: 6.46
  net_debt_cr: 280.44
  enterprise_value_cr: 16293.44
  revenue_fy26_cr: 590.38
  ebitda_fy26_cr: 217.75
  ebitda_margin_pct: 36.88
  pat_fy26_cr: 132.16
  diluted_eps_rs: 20.46
  cfo_fy26_cr: -123.26
  fcf_fy26_cr: -693.97
  capex_fy26_cr: 570.71
  book_value_per_share_rs: 240.34
  dps_rs: 0.00
  revenue_cagr_20_26_pct: 30.04
  pat_cagr_20_26_pct: 35.78
  roce_latest_fy26_statutory_pct: 8.84
  roce_operational_fy26_pct: 12.0
  roce_forward_verdict: "RECOVERING (40-60%); Pillar 1 sole authority"
  roe_latest_fy26_pct: 8.90
  cfo_pat_latest_fy26: -0.93
  cfo_pat_cumulative_fy20_26: 0.04
  wc_days_latest_fy26: 339.7
  wc_days_2yr_trend: "deteriorating (+72.8d FY25->FY26); CARE 287->344"
  credibility_grade: "B (Good)"
  guided_revenue_growth: "FY27+ 25%+; long-term margin 33-35% (FY26 delivered 36.9%)"
  em_score: 26
  em_classification: "STRENGTHENING (combined TURNAROUND)"
  som_implied_revenue_cagr_3yr_pct: 31.0
  som_implied_revenue_cagr_5yr_pct: 30.5
  revenue_headroom_x: 25.8
  runway_class: MASSIVE
  peer_median_ebitda_margin_pct: 20.69
  rating_agency: "CARE Ratings Limited"
  rating_grade: "CARE A; Stable"
  rating_date: "22 Jun 2026"
  pillar_1_roce_basis: "OPERATIONAL ~12% FY26; blended forward ~13.6%; base ~14.3x; NOT statutory 8.84% nor mgmt 20.7%"
  cash_conversion_basis: "GROWTH-INDUCED; 0.80x base + 0.10x offset = 0.90x"
  strategic_premium_override: "+3x (operator override)"
  sector_cap_override: "25x (not binding; raw < 25x)"
  ua_multiplier: "does NOT apply (FII+DII ~22% > 3%)"
  return_tier: "Tier A (25% hurdle via TURNAROUND)"
conflicts:
  - {field: "Sector cap row", value_a: "Pharma/CDMO 38x (manifest)", value_b: "Precision engineering 25x (FTTCP deliberation ruling 4)", used: "25x"}
  - {field: "Pillar 1 ROCE basis", value_a: "statutory 8.84% (B01) / mgmt adj 20.7% (B03)", value_b: "operational ~12% (FTTCP override 1)", used: "operational 12%"}
  - {field: "Strategic Premium", value_a: "+2x (analyst draft)", value_b: "+3x (FTTCP override 2)", used: "+3x"}
unresolved:
  - {field: "Diluted shares absolute", why: "approximated from mcap/CMP", where: "DRHP / Reg.31 filing"}
  - {field: "Peer P/E, EV/EBITDA, P/B, growth, ROCE", why: "peer EPS/net debt/BVPS not extracted", where: "peer ARs / screener"}
  - {field: "Promoter holding/pledge, contingent liabilities", why: "in AR/Reg.31, not provided", where: "Reg.31 filing, AR FY26 notes"}
  - {field: "FY27+ total capex quantum", why: "deflected in concalls", where: "Q1 FY27 concall"}
ua_qualifiers: {listed_12m: true, gate0_or_em: true, fii_dii_lt3: false, all_met: false}
credibility_grade: "B"
rating_wc_quote: "The company's working capital cycle remained elongated at 344 days as on March 31, 2026, compared to 287 days in the previous year, primarily considering increased inventory holding period. The average inventory holding period rose to 262 days in FY26 from 209 days in FY25, driven by higher inventory requirements for products under development that involve customised alloys, which must be procured in bulk due to minimum order quantity constraints. In addition, inventory levels remained elevated at the end of FY26 due to the commissioning of three dedicated units for key customers. This is expected to normalise once serial production begins. The average collection period also remained elevated at 163 days in FY26 (PY: 157 days) and is likely to stay stretched considering operations, with export receivables subject to extended credit terms of 120-180 days. Meanwhile, the average creditor period remained stable at 80 days in FY26 (PY: 79 days). To improve working capital efficiency, the company is evaluating a Just-in-Time (JIT) inventory model and is also exploring non-recourse factoring arrangements for receivables, which are expected to support a gradual reduction in inventory and debtor levels over the medium term. (CARE Ratings Limited, 22 Jun 2026, rating PDF p.3, Elongated working capital cycle subsection)"
```
