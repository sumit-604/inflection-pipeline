# STAGE 10 VALUATION INPUT ASSEMBLY — B10-valinputs
## K.C.P. Sugar and Industries Corporation Ltd (KCPSUGIND)
## Run date: 2026-07-21 | Model: claude-haiku-4-5-20251001

---

## COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|-------|-------|--------|
| Company | KCPSUGIND | (screener-Data_Sheet.csv row 2, BSE Scrip 533192) |
| Sector (corrected) | Agri processing | (fttcp-deliberation.md, corrected from manifest "Pharma / CDMO") |
| Business model type | Hybrid (revenue mix: Sugar 56.7%, Urad Dal 20.2%, Engineering 6.1%, others 16.7%) | (B04-bizmodel.yaml; FY26 consolidated breakdown per FY26_Audited_Results.txt p.4) |
| Sector cap row | Agri processing, 20x | (fttcp-deliberation.md override 3; operator-approved) |
| Current Market Price (CMP) | Rs 21.71 per share | (screener-Data_Sheet.csv row 7) |
| Market Capitalization | Rs 246.16 Cr | (screener-Data_Sheet.csv row 8, calculated as 11.34 Cr shares × Rs 21.71) |
| Shares outstanding (diluted) | 11.34 Cr | (screener-Data_Sheet.csv row 39, 63; no diluted instruments noted in filings) |
| Enterprise Value | Rs 334.52 Cr (calculation: Mcap Rs 246.16 Cr + Net Debt Rs 88.36 Cr) | (screener: Borrowings Rs 127.71 Cr FY26 minus Cash Rs 39.35 Cr = net debt Rs 88.36 Cr; FY26_Audited_Results.txt consolidated balance sheet) |
| Net Debt (mechanical) | Rs 88.36 Cr | (Borrowings Rs 127.71 Cr - Cash Rs 39.35 Cr; screener FY2026-03-31 columns) |
| Alternative view (CARE) | Net cash negative by ~Rs 204 Cr (investments Rs ~269 Cr + cash Rs ~47 Cr less debt Rs ~109 Cr per FY25 close) | (CARE_Rating_2025-10-07.txt p.2-3; note: FY26 data updates this; per deliberation, investment book directly valued in SOTP) |

---

## LATEST FINANCIAL METRICS (FY26 YEAR ENDED 31.03.2026)

### Income Statement (Consolidated)

| Metric | Value | Anchor |
|--------|-------|--------|
| Revenue from Operations (TTM) | Rs 259.95 Cr | (screener-Data_Sheet.csv row 11, FY2026-03-31; = FY26 consolidated Revenue Rs 25,994.68 lakhs per FY26_Audited_Results.txt p.3) |
| EBITDA (computed) | Rs 29.43 Cr | (FY26 consolidated: PAT Rs 11.13 Cr + Interest Rs 7.75 Cr + Tax Rs 4.6 Cr + Depreciation Rs 5.95 Cr per screener rows 21, 22, 23, 24) |
| Profit Before Tax (PBT) | Rs 15.73 Cr | (screener row 22, FY2026-03-31) |
| Net Profit After Tax (PAT) | Rs 11.13 Cr | (screener row 24, FY2026-03-31; = consolidated Rs 11.13 Cr per FY26_Audited_Results.txt) |
| Earnings Per Share (diluted) | Rs 0.98 | (FY26_Audited_Results.txt p.3, consolidated Basic and Diluted EPS for year ended 31.03.2026) |
| EBITDA Margin | 11.32% | (Rs 29.43 Cr / Rs 259.95 Cr) |
| PAT Margin | 4.28% | (Rs 11.13 Cr / Rs 259.95 Cr) |

### Cash Flow (TTM, consolidated per screener)

| Metric | Value | Anchor |
|--------|-------|--------|
| Operating Cash Flow (CFO) | Rs (30.89) Cr | (screener row 57, FY2026-03-31; first cash loss per CARO Annexure A clause xvii, noted in B03/deliberation) |
| Investing Cash Flow | Rs 6.09 Cr | (screener row 58, FY2026-03-31) |
| Free Cash Flow | Rs (24.80) Cr | (CFO Rs (30.89) Cr + Investing Activity Rs 6.09 Cr) |
| Cash from Financing | Rs 19.51 Cr | (screener row 59, FY2026-03-31) |
| CFO / PAT ratio (latest) | -2.77x | (CFO Rs (30.89) Cr / PAT Rs 11.13 Cr; structural cash conversion deterioration per deliberation) |
| CFO / PAT cumulative (3yr) | 64.7% | (3yr cumulative: CFO FY24 Rs 42.46 Cr + FY25 Rs 47.79 Cr + FY26 Rs (30.89) Cr = Rs 59.36 Cr / PAT FY24 Rs 66.16 Cr + FY25 Rs 14.39 Cr + FY26 Rs 11.13 Cr = Rs 91.68 Cr) |
| FCF / PAT | -2.23x | (Free Cash Flow Rs (24.80) Cr / PAT Rs 11.13 Cr; negative cash generation from earnings) |
| Price to FCF | NOT APPLICABLE | (negative FCF makes multiple undefined; market cap Rs 246.16 Cr / FCF Rs (24.80) Cr = negative multiple) |

### Balance Sheet (FY26 end 31.03.2026)

| Metric | Value | Anchor |
|--------|-------|--------|
| Equity Share Capital | Rs 11.34 Cr | (screener row 39, FY2026-03-31) |
| Reserves | Rs 448.17 Cr | (screener row 40, FY2026-03-31) |
| Net Worth | Rs 459.51 Cr | (Equity Rs 11.34 Cr + Reserves Rs 448.17 Cr; deliberation SOTP component a) |
| Total Borrowings | Rs 127.71 Cr | (screener row 41, FY2026-03-31; includes all debt instruments per B01) |
| Cash and Bank Balances | Rs 39.35 Cr | (screener row 51, FY2026-03-31) |
| Investments | Rs 292.76 Cr | (screener row 46, FY2026-03-31; deliberation notes investment book valued directly at holding-company discount in SOTP) |
| Net Block (PPE) | Rs 99.22 Cr | (screener row 44, FY2026-03-31) |
| Capital Work in Progress | Rs 0 (CWIP not separately shown for FY26 in screener) | (screener row 45 blank; B04 notes capex fell 36.1% YoY, below depreciation) |
| Book Value Per Share | Rs 40.52 | (Net Worth Rs 459.51 Cr / Shares 11.34 Cr) |
| Total Assets | Rs 659.76 Cr | (screener row 43, FY2026-03-31) |

### Returns and Efficiency

| Metric | Value | Anchor |
|--------|-------|--------|
| Return on Capital Employed (ROCE) | ~4% (reported); 0-2% (operating basis) | (fttcp-deliberation.md; per FTTCP DECLINING verdict, FY+1 lower bound ~4% reported); B01 median ROCE 6.93%, screener data FY26 shows reported ROCE degradation) |
| ROCE 2-year trend | DECLINING | (fttcp-deliberation.md Pillar 1: structurally low, no unwind catalyst) |
| Return on Equity (ROE) | 2.42% | (PAT Rs 11.13 Cr / Net Worth Rs 459.51 Cr; depressed due to high reserve base carrying inactive investment book) |
| Debt to Equity Ratio | 0.278x | (Borrowings Rs 127.71 Cr / Net Worth Rs 459.51 Cr; improved from prior year 0.30x per CARE p.3) |

### Growth Metrics (3-year trends)

| Metric | Value | Anchor |
|--------|-------|--------|
| 3-Year Revenue CAGR (FY24-FY26) | -10.5% | (FY24 Rs 345.68 Cr → FY26 Rs 259.95 Cr; screener rows 11, historical period) |
| 3-Year PAT CAGR (FY24-FY26) | -59.2% | (FY24 Rs 66.16 Cr → FY26 Rs 11.13 Cr; screener rows 24, historical period; collapsing consolidated profit) |
| Capex (FY26) | ~Rs 3.34 Cr (standalone); proxy ~Rs 6.26 Cr | (B04 notes capex fell 36.1% YoY, below FY26 depreciation of Rs 5.95 Cr; standalone capex Rs 3.34 Cr per B03/B04) |
| Depreciation (FY26) | Rs 5.95 Cr | (screener row 20, FY2026-03-31) |

### Dividend Policy

| Metric | Value | Anchor |
|--------|-------|--------|
| Dividend Per Share (FY26) | Rs 0 (no dividend) | (B05 notes dividend cut from Re 0.10 in FY25 to zero in FY26, loss-consistent; screener row 25 blank for FY26) |
| Dividend Per Share (FY25) | Re 0.10 | (screener row 25, FY2025-03-31) |

---

## SEGMENT PERFORMANCE (FY26 CONSOLIDATED)

Per FY26_Audited_Results.txt segment table (p.4-5, segment wise revenue and results):

| Segment | Revenue (Rs Cr) | Segment Result PBIT (Rs Cr) | Anchor |
|---------|-----------------|---------------------------|--------|
| Sugar (core) | Rs 141.55 | Rs (17.31) loss | (FY26_Audited_Results.txt p.4 segment table: Sugar revenue 14,155.02 lakhs, result (1,730.80) lakhs; widening loss per B03/B04/deliberation) |
| Engineering (Eimco-KCP consolidated) | Rs 78.64 | Rs 24.63 | (FY26_Audited_Results.txt p.4: Engineering revenue 7,863.55 lakhs, result 2,463.32 lakhs; order book growth but revenue fell 18.8% YoY per B04/B07) |
| Others (incl. Urad Dal) | Rs 45.16 | Rs 4.21 | (FY26_Audited_Results.txt p.4: Others revenue 4,515.56 lakhs, result 421.20 lakhs; Urad Dal scaled but segment turned loss-making per B04) |
| Chemicals | Rs 13.84 | Rs (2.86) loss | (FY26_Audited_Results.txt p.4: Chemicals revenue 1,383.71 lakhs, result (285.67) lakhs) |
| Power & Fuel | Rs 19.70 | Rs 1.27 | (FY26_Audited_Results.txt p.4: Power & Fuel revenue 1,969.90 lakhs, result 126.73 lakhs) |
| **Consolidated Total** | **Rs 259.95** | Segment PBIT before unallocable Rs 9.94 Cr | (FY26_Audited_Results.txt p.4; consolidated revenue 25,994.68 lakhs after inter-segment elimination) |

---

## FTTCP FORWARD TRANSITIONS & AUTHORITATIVE DELIBERATION OVERRIDES

Per fttcp-deliberation.md, carried verbatim as authoritative:

| Transition | Verdict | Anchor | Evidence |
|-----------|---------|--------|----------|
| **Revenue** | STARTING (+1) | fttcp-deliberation.md override 2 | Eimco-KCP Rs 257 Cr Hyundai order (operator-confirmed, released 20-21 Jul 2026, pending exchange filing) |
| **Margin** | DECLINING (-1) | fttcp-deliberation.md final rulings | Operating margin near zero in FY26; sugar segment loss widening three years (FY24: +Rs 6.51 Cr → FY26: -Rs 17.31 Cr); sector price tailwind not captured |
| **Cash Conversion** | DECLINING (-1), STRUCTURAL | fttcp-deliberation.md final rulings | First actual cash loss FY26 (Rs 11.36 Cr per CARO), CFO negative, DSCR 0.25x, receivable days 31 → 81, not growth-induced |
| **ROCE** | DECLINING (-1) | fttcp-deliberation.md final rulings | Reported ~4%, operating basis 0-2%, FY23-24 highs were investment income, no unwind catalyst; v3.5.1 normalized-ROCE anchor DOES NOT APPLY |
| **Composite Score** | -2 / -4 to +8 range | fttcp-deliberation.md composite and position | Revenue +1, Margin -1, Cash -1, ROCE -1 |
| **Operating Verdict** | DEEP WATCH leaning AVOID | fttcp-deliberation.md final FTTCP verdict | Kernex cash cap (DECLINING cash, catalyst NONE) binds at DEEP WATCH regardless of revenue upgrade; Eimco order lifts revenue but not cash, margin, or ROCE |

---

## OPERATOR-APPROVED VALUATION PILLARS (AUTHORITATIVE FOR PHASE 3)

Per fttcp-deliberation.md section "OPERATOR-APPROVED VALUATION PILLARS (AUTHORITATIVE FOR PHASE 3)":

| Pillar / Input | Approved Value | Note | Anchor |
|---|---|---|---|
| **Primary valuation method** | SUM-OF-THE-PARTS (lead) | Investment book valued directly at holding-company discount; Eimco-KCP as going concern with Rs 257 Cr order as revenue visibility; sugar core at asset/replacement or token operating value | fttcp-deliberation.md override 3 |
| **Pillar 1 ROCE** | ~4% reported (FTTCP DECLINING → FY+1 lower bound); operating basis 0-2% | Normalized-ROCE anchor (v3.5.1) DOES NOT APPLY | fttcp-deliberation.md, Section 1B Amendment 5 (0.5×ROCE+7.5, floor 9x) |
| **Pillar 1 base PE** | 9.5x at the 9x floor | On an operating basis (floor binding) | Section 1B Amendment 5; fttcp-deliberation.md approved table |
| **Pillar 2 cash multiplier** | 0.65x STRUCTURAL | Seasonal agri procurement; no growth offset | fttcp-deliberation.md |
| **Pillar 3 (growth + moat + duration)** | +0x | EM NONE (score 5); SOM CAGR <20% (9.7% to 7.5%, B09); order unfiled at run date | fttcp-deliberation.md, B07, B09 |
| **Strategic premium** | +0x | Nothing to credit | fttcp-deliberation.md |
| **Undiscovered Alpha (UA)** | NOT APPLIED | Fails Gate 0 ≥60 OR EM ≥25 qualifier (Gate 0 = 26, EM = 5); shareholding (FII+DII) absent so all-three-qualifier rule prevents application | fttcp-deliberation.md, B01 classification table; B03 input gaps; deliberation.md UA section |
| **Destination (exit) PE - additive track** | ~6x on normalized operating earnings | 9.5 × 0.65 + 0 + 0; far below the 20x cap | fttcp-deliberation.md approved table |
| **Destination (exit) PE - RRM track** | ~7x on normalized operating earnings | 9.5 × RRM(0.70-0.82); far below the 20x cap | fttcp-deliberation.md approved table |
| **Earnings basis** | TRAILING P/E | Applies to operating cross-check only; investment book valued directly in SOTP so base does not apply there | fttcp-deliberation.md override 4 |
| **Sector cap (corrected)** | Agri processing, 20x | Corrected from manifest "Pharma / CDMO"; operator-approved for phase 3 use | fttcp-deliberation.md override 3 |

---

## SOTP COMPONENTS (ASSEMBLED FOR STAGE 11 PRIMARY VALUATION)

Per fttcp-deliberation.md override 3 and task instructions, stage 11 receives these explicit pieces for SOTP calculation:

| Component | Value | Unit | Anchor |
|-----------|-------|------|--------|
| **(a) Investment Book** | | | |
| Investments (FV, primarily FVTPL) | Rs 292.76 | Cr (FY26) | screener row 46, FY2026-03-31; deliberation notes Rs 292.76 Cr in task preamble |
| Cash and Bank | Rs 39.35 | Cr (FY26) | screener row 51, FY2026-03-31 |
| **Investment Book Total** | **Rs 332.11** | Cr | (Inv Rs 292.76 Cr + Cash Rs 39.35 Cr) |
| **(b) Equity Value** | | | |
| Equity Share Capital | Rs 11.34 | Cr | screener row 39 |
| Reserves | Rs 448.17 | Cr | screener row 40 |
| **Net Worth** | **Rs 459.51** | Cr | (summed above) |
| **(c) Eimco Engineering Subsidiary (going concern)** | | | |
| Revenue (FY26 consolidated Engineering) | Rs 78.64 | Cr | FY26_Audited_Results.txt p.4 segment table |
| PBIT segment result (FY26) | Rs 24.63 | Cr | FY26_Audited_Results.txt p.4 segment table (2,463.32 lakhs) |
| PAT (Eimco standalone, FY25) | Rs 16.56 | Cr | B03-ardeep.yaml; B08-promoter.yaml carry this as proxy for subsidiary PAT; Eimco FY25 audited per AR consolidated data |
| Forward trigger (operator-confirmed) | Rs 257 Cr order | Hyundai Eimco-KCP | fttcp-deliberation.md override 1; order released 20-21 Jul 2026; pending exchange filing (Reg 30) |
| **(d) Sugar Core (operating)** | | | |
| Segment Revenue (FY26) | Rs 141.55 | Cr | FY26_Audited_Results.txt p.4 (14,155.02 lakhs) |
| Segment Result (FY26, PBIT) | Rs (17.31) | Cr loss | FY26_Audited_Results.txt p.4 (negative 1,730.80 lakhs) |
| Trend | Three consecutive years of losses / widening loss | FY24: +6.51 Cr → FY25: -8.21 Cr → FY26: -17.31 Cr | B03-ardeep.yaml; B04-bizmodel.yaml; FY26_Audited_Results.txt |
| **(e) Borrowings (debt base for net debt calc)** | | | |
| Total Borrowings | Rs 127.71 | Cr (FY26) | screener row 41, FY2026-03-31 |
| **(f) Shares Outstanding** | | | |
| Shares (diluted) | Rs 11.34 | Cr (count, not value) | screener rows 39, 63 |
| Current Market Price | Rs 21.7 | per share | screener row 7 |
| **Market Capitalization** | **Rs 246** | Cr | (11.34 Cr × Rs 21.7) |

---

## EARLIER ANALYSIS: MANAGEMENT CREDIBILITY & FORWARD VIEW

### Guidance & Delivery Track Record

Per B05-concall.yaml section "guidance" and "promise_delivery":

| Item | Stated Guidance | Timeframe | Outcome | Credibility Impact |
|------|-----------------|-----------|---------|-------------------|
| Sugar recovery | "Should stay firm; product prices expected to stay supportive" (AR Future Outlook) | FY25-26 (implicit) | MISSED (proxy): FY26 Sugar segment revenue -17.4%, loss +71% wider YoY; CARE (Oct 2025, independent) already flagged lower cane availability/recovery as active constraint | Negative |
| Ethanol opportunities | "Foresee opportunities in Ethanol production" (AR Future Outlook) | Not specified | PARTIAL/MISSED: Same AR reports 82% YoY collapse in alcohol production (FY25), sales value down 74%; FY26 data not separately disclosed | Negative |
| Dividend (FY25) | Re 0.10/share (10% of face value) | FY24-25, paid post-AGM | DELIVERED (standard declared dividend) | Neutral (not a claim about forward performance) |
| Diversification hedges | Value-added diversification (power, alcohol, Urad Dal) insulates against sugar price risk (Risk Mgmt Sec 5(iii)) | Ongoing | PARTIAL: Standalone Engineering revenue +5.7% FY26 but segment result -44.6%; consolidated Engineering (incl. Eimco-KCP) revenue -18.8% and result -19.4% YoY | Negative |
| **Credibility Grade** | **C** | | | |
| **Basis** | Default C per NO-CONCALL MODE, confirmed rather than upgraded: AR's only forward claims (recovery/price 'stay firm', ethanol opportunity) lack verifiable FY26 metrics or are contradicted by same-AR/FY26 delivery evidence; no company-specific accountability language; guidance unquantified | | | (B05-concall.yaml) |

### Management Execution Delivery

| Delivery Category | Status | Evidence | Anchor |
|-------------------|--------|----------|--------|
| Promise delivered | 1 of 4 claims | FY25 dividend delivered (but is a past-year item, not forward forecast) | B05 promise_delivery rows |
| Promise partial | 2 of 4 claims | Diversification logic and ethanol outlook both partially undercut by segment-level execution | B05 promise_delivery rows |
| Promise missed | 1 of 4 claims | Sugar recovery/margin improvement not delivered | B05 promise_delivery rows |

### Growth Triggers & Catalysts (12-month horizon)

Per B05-concall.yaml "triggers" and B07-emoat.yaml "catalysts_12m":

| Priority | Trigger / Catalyst | Type | Timeframe | Conviction | Confirm Signal | Kill Signal | Anchor |
|----------|-------------------|------|-----------|-----------|-----------------|-----------|--------|
| **Primary (Catalyst 0-6m)** | Reg 30 filing confirming (or not) Eimco-Hyundai Rs 257 Cr order | INORGANIC/VOLUME | 0-6m | L (unconfirmed) | Exchange filing + Reg 30 disclosure | No filing confirmation surfaces | B05 priority 4; B07 catalysts_12m item 1; fttcp-deliberation.md override 1 |
| **Secondary (Catalyst 6-12m)** | Consolidated Engineering segment revenue resuming YoY growth | VOLUME | 6-12m | L | Consolidated Engineering segment revenue recovery after FY26 dip (Rs 7,863 Cr vs Rs 9,687 Cr FY25) | Continued segment shrinkage | B07 catalysts_12m item 2 |
| **Tertiary (Catalyst 6-12m)** | Urad Dal / Others segment result turning positive | VOLUME | 6-12m | L | Segment result positive after FY25/FY26 losses; disclosed unit economics | Losses continue to widen | B07 catalysts_12m item 3 |
| **Quaternary (Catalyst 6-12m)** | Distillery utilisation recovery under E20 national mandate | REGULATORY/VOLUME | 6-12m | L | Disclosed recovery in distillery production/utilisation volumes | Continued collapse (as in FY25: -82% YoY) | B05 priority 1; B07 catalysts_12m item 4; CARE p.2 policy reference |
| **Cost Risk (Priority 5)** | Cane-price/FRP cost pressure | COST RISK | Near | M (as risk, not opportunity) | Next AR shows cane price rising with FRP without margin compression | Sugar segment loss widens despite firm prices | B05 priority 5; CARE p.2 (FRP expected to rise to Rs 355/quintal 2025-26) |

### Emerging Moat Score & Classification

| Category | Score / Status | Anchor |
|----------|---|---|
| **EM Score (total adjusted)** | 5 (on ~0-80 scale) | B07-emoat.yaml |
| **EM Classification** | NONE | B07-emoat.yaml |
| **Evidence mix** | Documented: 13 items; Claim: 0; Inference: 4 | B07-emoat.yaml |
| **Active categories** | Regulatory & Policy Tailwinds (Ethanol/E20 blending mandate) - Moderate strength, company-specific capture contingent on distillery recovery | B07-emoat.yaml |
| **17 of 20 categories** | NO EVIDENCE FOUND | B07-emoat.yaml completionist_recount |
| **Combined assessment** | AVOID (Backward AVOID [core 26, moat 1, deteriorating CFO] + forward NO MEANINGFUL EMERGING MOAT [em_score ~5, 17 of 20 categories NO EVIDENCE]) | B07-emoat.yaml |

---

## RATING AGENCY ASSESSMENT (CARE RATINGS)

### Rating Summary

| Attribute | Value | Anchor |
|-----------|-------|--------|
| **Agency** | CARE Ratings Limited (CareEdge Ratings) | CARE_Rating_2025-10-07.txt |
| **Rating** | CARE A-; Stable | CARE_Rating_2025-10-07.txt p.1 |
| **Outlook** | Stable | CARE_Rating_2025-10-07.txt p.1 (Outlook section, p.2) |
| **Rating Date** | 07 October 2025 | CARE_Rating_2025-10-07.txt p.1 cover date |
| **Rating Action** | Reaffirmed | CARE_Rating_2025-10-07.txt p.1 |

### Rating Commentary — Working Capital & Cash Flow

**Verbatim quote from CARE rating (p.3, "Liquidity: Strong" section):**

> "Liquidity remains strong, marked by free cash and investments of ₹204.08 crore as on March 31, 2025. Average working capital utilisation stood at 37.65% for 12 months ended June 2025, providing headroom for additional working capital requirements in non-sugar segments. Current ratio improved to 2.73x as on March 31, 2025, compared to 1.89x as on March 31, 2024. The company has nil term debt and fixed deposit current maturity of ₹20.72 crore due in FY26 (PY: ₹22.69 crore). However, most of the fixed deposit is expected to be renewed upon maturity. As on March 31, 2025, fixed deposits stood at ₹65.84 crore compared to ₹62.82 crore as on March 31, 2024."

**Rating agency constraint language (p.2, "Key weaknesses" section):**

> "Ratings are constrained by lower cane availability and lower recovery rate of sugarcane in its command area, affecting profitability margins. Ratings also factor in susceptibility of revenues and profitability to demand-supply dynamics and the cyclical and regulated nature of the sugar industry in terms of command area and plant location."

**Negative factors for rating action (p.2, "Rating sensitivities"):**

> "Negative factors: Factors that could individually or collectively lead to negative rating action/downgrade: Debt funded capex, resulting in net term debt/net worth >0.3x on a sustained basis. Continued decline in cane crushed/cane availability on a sustained basis, leading to lower capacity utilisation"

---

## UNDISCOVERED ALPHA (UA) QUALIFIERS CHECK

Per instruction rule on UA: "Never treat low institutional ownership as a risk. UA multiplier per Amendment 3: min(Raw x 1.25, Sector Cap), all three qualifiers evidenced."

| Qualifier | Status | Value | Anchor | Met? |
|-----------|--------|-------|--------|------|
| **Listed ≥12 months** | CONFIRMED YES | Long-listed on BSE Scrip 533192 | B00-inputs.yaml; B01-gate0.yaml "listed_status: long-listed" | ✓ YES |
| **Gate 0 ≥60 OR EM ≥25** | CONFIRMED NO | Gate 0 = 26 (classification AVOID); EM = 5 (classification NONE) | B01-gate0.yaml (core_score 26, moat_score 1); B07-emoat.yaml (em_score 5) | ✗ NO (fails both) |
| **FII+DII <3%** | UNRESOLVED | Data not found in available AR text or filings | B00-inputs.yaml input_gaps (shareholding absent); B03-ardeep.yaml (SEBI shareholding-pattern not embedded in AR); B08-promoter.yaml (no primary SEBI/NSDL shareholding-pattern found) | ? UNRESOLVED |
| **All three qualifiers met** | NO | Fails on Gate 0/EM; FII+DII unresolved means all-three-qualifier rule prevents application even if FII+DII were below 3% | fttcp-deliberation.md UA section; deliberation.md Pillar table row "Undiscovered Alpha: NOT APPLIED" | **✗ NO** |

**UA Determination:** NOT APPLIED (deliberation.md: "fails Gate 0 >=60 or EM >=25 qualifier (Gate 0 = 26, EM = 5)") — Shareholding data (FII+DII) is absent per B00/B03/B08, so the all-three-qualifier rule is already satisfied to WITHHOLD UA in Phase 3.

---

## SOM-IMPLIED REVENUE CAGR

Per B09-tam.yaml market definitions and calculated SOM:

| Metric | 3-Year | 5-Year | Anchor |
|--------|--------|---------|--------|
| **SOM (Rs Cr)** | Rs 343.0 | Rs 372.6 | B09-tam.yaml (som_3yr_cr, som_5yr_cr) |
| **Implied Revenue CAGR** | 9.7% | 7.5% | B09-tam.yaml (som_implied_revenue_cagr: yr3=9.7, yr5=7.5) |
| **Current Revenue** | Rs 259.95 Cr (FY26) | | screener; B09 baseline |
| **Runway Class** | MODERATE (overridden down from mechanical MASSIVE) | | B09: "revenue_headroom_x (614.7x) is a mechanical SAM artifact; runway_class overridden down from MASSIVE to MODERATE given zero capex-embedded growth and slow blended TAM growth (3.7%)" |
| **SOM CAGR Drivers** | Urad Dal running at ~21-26% of installed 22,000 MTPA capacity; strip this out and blended CAGR falls to mid-single digits | | B09-tam.yaml flags section |
| **Note on Eimco order** | Rs 257 Cr Hyundai order EXCLUDED from anchored TAM/SAM/SOM figures; if confirmed, ~3.3x FY26 Engineering segment revenue | | B09-tam.yaml flags section |

---

## CONFLICTS & UNRESOLVED DATA

### Conflicts (data disagreement between blocks)

**No conflicts identified in data-assembly stage.** The deliberation record and operator rulings supersede earlier draft positions per task instructions. Pillar 1 base PE (9.5x), Pillar 2 cash (0.65x), and SOTP as primary method are authoritative per fttcp-deliberation.md and require no conflicting-data flagging.

### Unresolved Data

| Field | Why Unresolved | Where It Might Be | Anchor |
|-------|---|---|---|
| **FII+DII institutional shareholding (latest %)** | Standard SEBI shareholding-pattern export not provided; AR FY25 does not embed SEBI SHP table; aggregator data partial (~3.31% FII across 62 funds per B08, media-reported, non-authoritative) | SEBI NSDL portal; company's latest shareholding disclosure filing (Reg 31) | B00-inputs.yaml input_gaps; B03-ardeep.yaml; B08-promoter.yaml |
| **Promoter shareholding % (latest FY26)** | SEBI shareholding-pattern table not embedded in AR; B08 media-reported state is ~42% (net buyer through loss year, 0% pledge) but not filing-anchored | SEBI shareholding-pattern filing (Reg 31); company BSE/NSE announcement (Reg 30/29(2)) | B08-promoter.yaml; B00-inputs.yaml input_gaps |
| **Promoter pledge status (latest %)** | Not embedded in available AR; B08 reports 0% pledge across all periods found (via media/aggregator search) but not primary-filing-anchored | SEBI shareholding-pattern PDF; company's latest pledge disclosure | B08-promoter.yaml searches_skipped |
| **Eimco-KCP standalone audit-trail status (ITGC) for FY26** | AR pp.151-275 (Eimco consolidated FY26 auditor notes) are scanned/not extractable; noted as weakness in FY25 per B02 | Next AR (FY26-27) Eimco Directors'/Auditor's Report; FY26-27 Q1 disclosure if separately filed | B03-ardeep.yaml; B02-notes.yaml monitorables |
| **Single-customer revenue concentration (Eimco-KCP order pipeline detail)** | Eimco order book disclosed as growing +30.4% YoY FY25 (B03: Rs 91.86 Cr) but customer concentration/top-customer share within the order book NOT DISCLOSED; Rs 257 Cr Hyundai order is sole large order referenced | Eimco-KCP Directors' Report / MD&A (next AR or Reg 30 EPC project disclosure) | B04-bizmodel.yaml mgmt_questions; B07-emoat.yaml optionality_register |
| **FY26 Ethanol/Alcohol segment revenue separately disclosed** | FY26 Results filing abandoned the FY25 AR practice of breaking Ethanol/Alcohol as a distinct line; consolidated Alcohol output data not separately given for FY26; FY25 figure (Rs 10.20 Cr sold value) carried as proxy | FY26-27 quarterly segment notes (Reg 33); next AR product-wise Note 44 equivalent | B09-tam.yaml input_gaps; B05-concall.yaml input_gaps |
| **Eimco-KCP engineering subsidiary standalone margin/PBIT (FY26)** | Consolidated Eimco-KCP (part of consolidated Engineering segment) FY26 segment result available (Rs 24.63 Cr PBIT per FY26 results p.4); standalone Eimco PAT carried from FY25 (Rs 16.56 Cr, per AR & B03) for illustration | Eimco-KCP Limited's own FY26 Annual Report (due to be published) | B03-ardeep.yaml; deliberation SOTP component (c) |

---

## RATING PDF WORKING CAPITAL QUOTE (FOR FLAG-CASH ANCHOR)

**Extracted verbatim from CARE Ratings (07 Oct 2025) for the downstream FLAG-CASH determination per instruction requirement:**

**Source:** CARE_Rating_2025-10-07.txt pages 2-3

**Agency:** CARE Ratings Limited (CareEdge Ratings)

**Rating:** CARE A-; Stable (Reaffirmed)

**Date:** 07 October 2025

**Working Capital Commentary (verbatim from p.3, "Liquidity: Strong" section):**

> "Liquidity remains strong, marked by free cash and investments of ₹204.08 crore as on March 31, 2025. Average working capital utilisation stood at 37.65% for 12 months ended June 2025, providing headroom for additional working capital requirements in non-sugar segments. Current ratio improved to 2.73x as on March 31, 2025, compared to 1.89x as on March 31, 2024."

**Operational/Cash Flow Risk Language (from p.2, "Key weaknesses"):**

> "Ratings are constrained by lower cane availability and lower recovery rate of sugarcane in its command area, affecting profitability margins."

**Liquidity Outlook Language (p.2, "Outlook: Stable"):**

> "CareEdge Ratings believes that the company will maintain its risk profile, considering its comfortable capital structure and liquidity."

---

## SUMMARY OF AUTHORITATIVE DETERMINATIONS FOR STAGE 11

| Decision | Authority | Anchor |
|----------|-----------|--------|
| **Primary Valuation Method** | SUM-OF-THE-PARTS (lead); investment book valued directly at holding-company discount; Eimco-KCP as going concern with Rs 257 Cr order; sugar core at asset/replacement or token value | fttcp-deliberation.md override 3 (operator-approved) |
| **Earnings Basis** | TRAILING P/E (applies to operating cross-check only; investment book valued directly in SOTP) | fttcp-deliberation.md override 4 (operator-approved) |
| **Pillar 1 base PE** | 9.5x at 9x floor (FTTCP DECLINING ROCE ~4% reported / 0-2% operating, no normalization adjustment) | fttcp-deliberation.md approved table; Section 1B Amendment 5 |
| **Pillar 2 cash multiplier** | 0.65x STRUCTURAL (seasonal agri, no growth offset) | fttcp-deliberation.md approved table |
| **Pillar 3 & Strategic** | +0x each (EM NONE, SOM CAGR <20%, order unfiled at run; nothing to credit) | fttcp-deliberation.md approved table |
| **Destination PE (cross-check)** | ~6x additive / ~7x RRM on normalized operating earnings (far below 20x sector cap) | fttcp-deliberation.md approved table |
| **Sector cap** | Agri processing 20x (corrected from manifest Pharma/CDMO) | fttcp-deliberation.md override 3 (operator-approved); Phase 3 must use this row |
| **UA Status** | NOT APPLIED (fails Gate 0 ≥60 or EM ≥25 qualifier; shareholding absent so all-three-qualifier withheld) | fttcp-deliberation.md; B01; B07 |

---

*Report compiled by pipeline stage 10-assembly, claude-haiku-4-5-20251001, 2026-07-21. Every value anchored to source block, results PDF, screening CSV, rating cache, or authoritative deliberation record. No values estimated. Unresolved data explicitly listed above.*

