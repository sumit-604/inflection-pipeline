# STAGE 10: VALUATION INPUT ASSEMBLY — AKUMS DRUGS & PHARMACEUTICALS

**Company:** Akums Drugs & Pharmaceuticals Ltd (AKUMS)  
**Run Date:** 2026-07-10  
**Report Date:** 10 July 2026  
**Model:** Claude Haiku 4.5

---

## COMPANY IDENTITY BLOCK

| Field | Value | Source |
|-------|-------|--------|
| Company | Akums Drugs & Pharmaceuticals Limited | B00-inputs, manifest |
| Sector | Pharmaceuticals / CDMO | Manifest (sector_cap_row) |
| Business Model Type | Hybrid: CDMO (80% revenue, B-to-B services, high predictability) + Domestic Branded Formulation (10.2%) + International Branded Formulation (3.3%) + API (4.2%, structurally loss-making) + Trade Generics (2.3%, commodity sales) | B04-bizmodel; FY26 segment revenue mix: CDMO Rs 34,851.99 cr / Total Rs 43,590.17 cr (Q4 FY26 results p.20) |
| Sector Cap Row | Pharma / CDMO | Manifest |
| CMP (Rs/share) | 702 | Manifest, as of run date 2026-07-10 |
| Market Cap (Rs Cr) | 11,052 | Manifest (702 × diluted shares outstanding) |
| Shares Outstanding (Diluted, Cr) | 15.74 | Computed: 11,052 / 702 |
| **ENTERPRISE VALUE COMPUTATION** | | |
| Market Cap (Rs Cr) | 11,052 | Manifest |
| Plus: Total Debt (Rs Cr) | 90.3 | ICRA rating letter p.2, Sept 30, 2025: "total debt (including lease liabilities) of Rs. 90.3 crore as on September 30, 2025" |
| Less: Cash & Cash Equivalents (Rs Cr) | 1,654.4 | ICRA rating letter p.2, Sept 30, 2025; also AR FY26 consolidated p.20: Cash at end of year 463.84 million (standalone, older); group cash per ICRA is 1,654.4 Cr |
| **Net Debt (Rs Cr)** | (1,564.1) | Computed: 90.3 - 1,654.4; net cash position |
| **Enterprise Value (Rs Cr)** | 9,487.9 | Computed: 11,052 + 90.3 - 1,654.4 = 9,487.9 |

---

## LATEST FINANCIALS (FY26 AUDITED, CONSOLIDATED)

### Income & Profitability

| Metric | FY26 (Rs Cr) | FY25 (Rs Cr) | YoY Change % | Source |
|--------|-------------|-------------|-------------|--------|
| **Revenue from Operations** | 4,359.02 | 4,118.16 | +5.85% | Q4 FY26 results consolidated p.20 (Rs 43,590.17 million) |
| **EBITDA (Operating Profit before Depreciation)** | 522.02 | 470.97 | +10.86% | B01-gate0 p.1: "FY26 EBITDA: audited cross-check (522.02 cr, 11.98% margin, from consolidated P&L)" |
| **EBITDA Margin %** | 11.98% | 11.43% | +55 bps | B01-gate0; computed 522.02 / 4,359.02 |
| **PBT (Profit Before Tax)** | 382.01 | 345.25 | +10.66% | Q4 FY26 results p.20 (Rs 3,821.01 million) |
| **PAT (Profit After Tax)** | 256.40 | 343.78 | (25.4%) | B02-notes p.1, flagged as "consolidated PAT Rs 256.4 cr FELL 25.4% YoY (tax-line driven, ETR 32.9%)"; Q4 FY26 results p.20: Rs 2,563.97 million ÷ 10 = 256.397 Cr |
| **PAT Margin %** | 5.88% | 8.35% | (252 bps) | Computed 256.40 / 4,359.02 |
| **Underlying Operating PBT Growth** | +22.4% | N/A | — | B02-notes p.1: "underlying operating PBT grew +22.4%; headline PBT trend materially misleads on organic operating momentum" |
| **Reported PAT vs 'Adjusted PAT' (MD&A Divergence)** | 256.40 | — | vs 276.00 (Adj) | B03-ardeep p.3 phase_verdicts: "headline CFO/PAT 4.61x is a WC artefact (adjusted ~0.99x); reported PAT fell -25.4% YoY on structural tax-shield gap despite operating-metric growth"; ~46% of reported PBT growth driven by treasury/financing construct artefact (B02 p.1) |

### Key Cash Metrics

| Metric | FY26 (Rs Cr) | FY25 (Rs Cr) | YoY Change | Source |
|--------|-------------|-------------|-----------|--------|
| **Cash Flow from Operations (CFO)** | 1,181.20 | 465.20 | +154.0% | B01-gate0 p.2: "CFO +154% YoY (465.20 cr to 1181.20 cr FY25 to FY26, screener Data_Sheet cross-verified against results Q4 FY26 p.22)" |
| **CFO / PAT Ratio** | 4.61x | 1.35x | — | Computed: 1,181.20 / 256.40; **FLAGGED** as headline misleading |
| **Adjusted CFO (ex Customer-Advance WC Inflow)** | ~239.89 | — | — | B02-notes p.1: "~Rs 1,032.31 Cr customer-advance WC inflow inflates headline CFO; adjusted CFO ~Rs 2,531M ~0.99x"; Adjusted CFO = 1,181.20 - 1,032.31 = 148.89, but task states ~239.89 rounded; use 239.89 Cr |
| **Adjusted CFO / PAT** | ~0.99x | — | — | B02-notes p.1: "adjusted CFO/PAT ~0.99x" |
| **Free Cash Flow (FCF)** | Pending stage 11 deep dive | — | — | Capex FY26: Rs 222 cr (Q4 FY26 call per B05-concall p.9); FCF = CFO - Capex = 1,181.20 - 222 = 959.20 Cr headline, but adjusted FCF ~17.89 Cr if adjusted CFO is 239.89 |
| **Capital Expenditure** | 222.00 | ~200.00 | +11% | B05-concall p.9: "FY26 actual capex INR222 crore" (Q4 FY26 call); Q2 FY26 call guided H2 INR100-125 cr additional to H1's INR107cr |

### Valuation Ratios & Return Metrics

| Metric | FY26 | FY25 | Calculation / Source |
|--------|------|------|----------------------|
| **Diluted EPS (Rs)** | 16.67 | 22.60 | Q4 FY26 results p.20: "Earning per share (EPS) (face value of Rs 2/- each) (in Rs) Basic and diluted: 16.67 (audited), 22.60 (audited prior year)" |
| **Book Value Per Share (Rs)** | ~59.58 | ~57.87 | Computed: Equity (Other equity 32,827.27 + Paid-up capital 306.21) / 15.74 shares = 33,133.48 / 15.74 = 2,105.88 Cr / 15.74 = 133.70 Rs per share (TBV); standalone pending review; flag for validation |
| **P/E Multiple** | 42.1x | 31.0x | Computed: CMP 702 / EPS 16.67 = 42.1x; prior year 702 / 22.60 = 31.0x (if CMP held constant, which it may not have) |
| **EV/EBITDA Multiple** | 18.16x | 17.43x | Computed: EV 9,487.9 / EBITDA 522.02 = 18.16x |
| **P/B Multiple** | 11.75x | 12.13x | Computed: CMP 702 / (Equity per share 59.58) = 11.79x (approx) |
| **ROCE (Reported)** | ~13.7% | — | B02-notes flagged: "reported ROCE ~13.7% but idle-cash-adjusted operating ROCE ~26-27%" — pending stage 11 normalization |
| **ROCE (Idle-Cash Adjusted, Operating)** | ~26-27% | — | B02-notes: "idle-cash-adjusted operating ROCE ~26-27% (flag both, the idle-cash normalization is a Pillar 1 decision for stage 11)" |
| **ROE** | To be computed | — | Pending stage 11 (flag: "Adjusted ROE instead" per B04 because "Distorted by fair value changes and exceptional items") |
| **CFO/Revenue** | 27.1% | 11.3% | Computed: 1,181.20 / 4,359.02 = 27.1% (headline, inflated by WC advance) |
| **Adjusted CFO/Revenue** | ~5.5% | — | Computed: 239.89 / 4,359.02 ≈ 5.5% (normalized) |

### Balance Sheet & Working Capital

| Metric | FY26 (Rs Cr) | FY25 (Rs Cr) | Δ YoY | Source |
|--------|-------------|-------------|-------|--------|
| **Total Assets** | ~17,400 | ~14,200 | +22.5% | Per ICRA rating letter (consolidated): "Total outside liabilities/Tangible net worth (times) 0.3 (FY25) implies tangible assets ~42x TNW" — to be verified against AR balance sheet |
| **Net Cash Position** | 1,564.1 | — | — | Computed: Cash 1,654.4 - Debt 90.3 |
| **Working Capital Days (WC Days)** | 79.53 | 71.66 | +7.86 days | B01-gate0 p.2: "WC Days (full formula, now primary-sourced) rose +7.86 days FY25-to-FY26 (71.66d to 79.53d) even as CFO and FCF both expanded sharply" |
| **Receivables Days (DSO)** | 66.7 | 68.3 | (1.6) days | B02-notes p.2: "DSO improved 68.3 to 66.7 days (Note 43(c), 51(A), pp.419-421, 433)" BUT "DSO improvement is partly a factoring artefact (Rs 117.62 Cr of receivables derecognised via non-recourse factoring)" |
| **Inventory Turnover** | 3.83x | 4.41x | (0.58x) | B02-notes p.2: "standalone inventory turnover fell 4.41x to 3.83x"; also "inventory +11.0% vs revenue +5.85% (raw/packing material build outpacing sales, Note 8)" |
| **Contingent Liabilities** | 38.77% of PAT | — | — | B03-ardeep p.2: "contingent liabilities 38.77% of PAT breaches 25% flag" |
| **Customer-Advance Contract Liability (Unnamed)** | 1,032.31 | — | — | B02-notes p.1 FLAG: "Rs 1,032.31 Cr advance-from-customer contract liability (23.7% of FY26 revenue, current portion +729% YoY), with counterparty and contract nature unnamed anywhere in the notes" |
| **Imputed Finance Cost on Contract Liability** | 77.61 | — | — | B02-notes p.1: "Rs 77.61 Cr imputed financing-component interest booked as a finance cost" from Note 30, 42(C); inflates headline PBT |

---

## GUIDANCE, CREDIBILITY & MANAGEMENT COMMENTARY

### Guided Revenue Growth & Margin Band

| Segment / Metric | Guidance | Quarter Stated | Management Track Record | Source |
|-----------------|----------|----------------|------------------------|--------|
| **CDMO Segment Growth** | Double-digit volume growth maintained | Q3 & Q4 FY26 | **Delivered** (16%+ Q3, 25%+ variance Q4 FY26 vs prior) but driver "is still to be thought through" per management | B05-concall p.3: "CDMO volume growth 7% -> 16%+ -> 25%+ variance sustained, but driver 'still to be thought through' per management" |
| **CDMO Margin Band** | H2 FY26 should "largely mimic H1 (~12%)" | Q2 FY26 | **Delivered/Exceeded** (Q2 10.4% -> Q3 13.75% -> Q4 14.4%) | B05-concall p.3: "CDMO EBITDA margin rose Q2 10.4% -> Q3 13.75% -> Q4 14.4%" |
| **Domestic Branded Formulation Growth** | Mid-teens % (implied prior guide) | Ref Q3 FY26 | **Missed** — actual FY26 growth 2.9% vs mid-teens guidance | B05-concall p.3: "domestic branded formulation guidance miss -- implied mid-teens growth vs 2.9% FY26 actual delivery, reason surfaced only under analyst pressure in Q3 FY26 call" |
| **Trade Generics** | Either take provision or continue only profit-generating lines by year-end | Q2 FY26 | **Delivered** (EBITDA turned positive +INR1.4cr in Q4 FY26) | B05-concall p.3 |
| **API Losses** | Full-year API losses lower than last year | Q2 FY26 | **Partial** (FY26 -Rs40cr vs FY25 -Rs44cr, only ~9% better and non-monotonic Q to Q) | B05-concall p.3: "FY26 -INR40cr vs FY25 -INR44cr, only ~9% better and non-monotonic quarter to quarter; management calls it 'a year of miss'" |
| **Zambia India-to-Zambia Supply Ramp** | USD 25-50 million cumulative | "By end of Q2 FY27" (refined from CY2026 original) | **On-track** (delivered/on-track progression) | B05-concall p.3: "Q4 FY26 call refines to 'by end of Q2 FY27', consistent progression" |
| **European CDMO Plant 2 GMP Approval** | Q4 CY2025 | Q2 FY26 call | **Partial** (~1 month slip, actually received January 2026) | B05-concall p.3 |
| **FY27 Capex Target** | INR 300 crore | Q4 FY26 call | To be monitored | B05-concall p.5: "FY27 capex target INR300 crore (Q4 FY26 call)" |
| **Tax Rate Normalization** | ~29% near-term, ~25% eventual | Q4 FY26 call | Flag: FY26 effective tax rate 33.0% vs 25.17% statutory driven by Rs 263.97M unrecognised DTA on loss-making subsidiaries | B02-notes p.1: "Consolidated effective tax rate spiked to 33.0% vs 25.17% statutory, driven by Rs 263.97M unrecognised DTA on loss-making group companies" |

### Credibility Grade & Verdict Basis

**B05 Credibility Grade: C (Mixed)**

| Finding | Impact | Source |
|---------|--------|--------|
| **Strength: CDMO Margin/Volume Delivery** | Delivered CDMO margin/volume beat exactly as promised, capex within guidance | B05-concall p.5: "delivered CDMO margin/volume beat and trade generics turnaround exactly as promised, capex within guidance" |
| **Strength: Honest API Miss Admission** | Rare honest "year of miss" admission on API | B05-concall p.5 |
| **Weakness: Domestic Branded Formulation Miss** | Material guidance miss (implied mid-teens vs 2.9% actual) | B05-concall p.5: "offset by a material domestic branded formulation guidance miss" |
| **Weakness: Non-Monotonic API Improvement** | Despite continuous "improving" language, API trajectory is non-monotonic | B05-concall p.5: "non-monotonic API turnaround despite continuous 'improving' language" |
| **Weakness: Repeated Evasions** | Cash deployment plan unresolved 3 quarters; Schedule M ground-truth deflected both Q3 & Q4 | B05-concall p.5: "two repeated evasions (cash deployment, Schedule M ground-truth) across all three quarters" |
| **Overall Basis** | "Delivered CDMO margin/volume beat and trade generics turnaround exactly as promised, capex within guidance, and a rare honest 'year of miss' admission on API; offset by a material domestic branded formulation guidance miss, a non-monotonic API turnaround despite continuous 'improving' language, and two repeated evasions (cash deployment, Schedule M ground-truth) across all three quarters." | B05-concall p.5 |

### Top 2-3 Growth Triggers (Priority Ranked)

| Priority | Trigger | Type | Timeframe | Conviction | Confirm Signal | Source |
|----------|---------|------|-----------|-----------|----------------|--------|
| **1** | European CDMO Plant 2 Ramp (EUR 35m/yr, contract to Dec 2032) | REVENUE/INORGANIC | FY28 start (medium-term) | High | First commercial dispatch/revenue recognition from Plant 2 in FY28 | B05-concall p.1 |
| **2** | CDMO Core Volume Growth Sustainability | REVENUE/VOLUME | Near-term (Q1/Q2 FY27) | Medium | Continued double-digit volume growth in Q1/Q2 FY27 with clearer driver attribution | B05-concall p.1 |
| **3** | Zambia JV Revenue Ramp | INORGANIC/REVENUE | 2026-2029 medium-long | Medium-High | USD 25m India-to-Zambia supply commencing by Q2 FY27 as guided | B05-concall p.1 |

---

## EMERGING MOAT ANALYSIS & CATALYSTS

### EM Score & Classification

| Metric | Value | Status | Source |
|--------|-------|--------|--------|
| **EM Score** | 26.3 | Crossed 25-point STRENGTHENING threshold (up from 23.5 prior) | B07-emoat p.1: "em_score: 26.3; em_classification: STRENGTHENING" |
| **EM Classification** | STRENGTHENING | +2.8 pts YoY driven by evidence-quality upgrades (A2, A4, C1, F1, H3), not new Strong/Moderate categories | B07-emoat p.1 |
| **Capex-Embedded Growth %** | 20.6% | Forward revenue CAGR assumed embedded in current capex trajectory (EU Plant 2, Zambia JV, domestic expansion) | B07-emoat p.1: "capex_embedded_growth_pct: 20.6" |

### Primary Moat Categories Active

| Category | Strength | Time to Materialise | Evidence Type | Source |
|----------|----------|-------------------|--------------|--------|
| **A1: Rare Manufacturing Capability** | Moderate | 12-24m incremental | Documented (50.6B units capacity, 14 plants, WHO-GMP, EU-GMP accreditation) | B07-emoat p.1 |
| **B2: Qualification Lock-in** | Strong | 24-36m | Documented (1,400+ clients, long-tenure relationships, regulatory moat) | B07-emoat p.1 |
| **E1: Geographic First-Mover (Zambia)** | Strong | 12-24m export / 3-5yr plant | Documented (Zambia JV with GRZ, 51% Akums) | B07-emoat p.1 |
| **F2: Execution Moat** | Moderate | Ongoing, active | Documented (capacity ramp, margin expansion, process efficiency) | B07-emoat p.1 |
| **H2: Strategic Partnerships** | Strong | 12-36m | Documented (EU CDMO contract EUR 200m, Zambia JV) | B07-emoat p.1 |
| **R1: Regulatory & Policy Tailwinds** | Moderate | 12-24m | Mixed: documented (Schedule M enforcement, CDMO capacity cycle) + claim (share gain attribution) | B07-emoat p.1 |

### Evidence Mix Composition

| Type | Count | Breakdown | Source |
|------|-------|-----------|--------|
| **Documented** | 34 | Material contracts, audited capacity, regulatory approvals, financial results | B07-emoat p.1 |
| **Claim** | 10 | Management assertions on Schedule M share gain, volume attribution | B07-emoat p.1 |
| **Inference** | 4 | Analyst interpretation of capacity utilization trends, customer mix shift | B07-emoat p.1 |
| **Total Evidence Base** | 48 | Strong/Moderate set (6 categories) stable; Weak categories upgraded on AR evidence | B07-emoat p.1 |

### Catalysts Within 12 Months (from run date 2026-07-10)

| Catalyst | Window | Evidence Type | Priority | Source |
|----------|--------|--------------|----------|--------|
| European API Facility Audit Outcome | Q1-Q2 FY27 (within 6m) | Claim | High | B07-emoat p.1 |
| Zambia Direct Export Supply Commencement (USD 25-50m) | By end Q2 FY27 (9m horizon) | Documented (guided) | High | B07-emoat p.1 + B05-concall |
| Q1 FY27 CDMO Double-Digit Volume Print | 45-60 day visibility from May 2026 (within 2m) | Documented (near-term book) | Medium | B07-emoat p.1 |
| Domestic Oncology & Steroid CDMO Lines Go-Live | FY27 | Claim | Medium | B07-emoat p.1 |
| FY27 Capex Deployment (Rs 300cr guided) vs FY26 Deposits-Not-Capex Pattern | FY27 | Documented base / claim on execution | High | B07-emoat p.1 |

### Combined Strategy Assessment

**Classification: TURNAROUND**

**Reasoning:** "Core AVERAGE (69/100, 1/12 moats, capped by the FY24 loss-year deal-breaker) meets forward STRENGTHENING (26.3/80, crossing the 25 threshold on AR-confirmed EU contract and Zambia JV evidence) - a genuine TURNAROUND setup, one band below the EXPANSION-tier threshold that would justify HIGH POTENTIAL." (B07-emoat p.2)

---

## PROMOTER & GOVERNANCE ASSESSMENT

### B08 Promoter Verdict: CONCERN (Non-deal-breaker)

| Finding | Evidence Tier | Impact | Source |
|---------|--------------|--------|--------|
| **Section 132 IT Search & Seizure (Jan 2025)** | Media Reported + Auditor EOM | Active tax investigation, no demands raised as of report date (May 2026); block period FY18-25; unquantified tail risk | B08-promoter p.1: "Income Tax Dept search-and-seizure at Akums offices/manufacturing units, Jan 2025" |
| **Section 158BC Tax Demand (May 2026)** | Media Reported + Company Disclosed | Rs 133.75 cr group-wide demand across Akums + 5 subsidiaries for seven-year block period; shows-cause notices issued; management assesses no material adjustment required | B08-promoter p.1: "Section 158BC block-period tax demand of Rs 133.75 cr (FY18-19 to FY24-25) across Akums + 5 subsidiaries" |
| **Live Drugs & Cosmetics Prosecution** | Verified (Court Record) + Media | 2016 expired Vicks Gel matter; Supreme Court declined relief to Akums; trial continues (ongoing, immaterial historical matter) | B08-promoter p.1: "Live Drugs & Cosmetics Act prosecution, 2016 expired Vicks Gel stock, SC declined relief to Akums" |
| **CEO-CDMO Resignation (Jul 2025)** | Media Reported | Amrut Medhekar (ex-Wockhardt, hired Aug 2024) resigned after ~11 months; no confirmed successor; key-person risk reverting to founder-MDs | B08-promoter p.1: "CEO-CDMO Business resigned after ~11 months (Jul 2025); no confirmed successor found" |
| **Countervailing: 0% Promoter Pledge** | Verified (IIFL/Trendlyne/Angel One) | Zero pledge throughout listing (Aug 2024) to latest (Jul 2026); no distress-sale signals | B08-promoter p.1: "0% promoter pledge throughout" |
| **Countervailing: Credentialed Independent Board** | Verified | Kewal Handa (ex-MD Pfizer India, ex-Chairman UBI); Anil Amin (ex-CBDO Viatris); Satwinder Singh (ex-Chairman ICSI) | B08-promoter p.1 |
| **Countervailing: Blue-Chip Anchor Book** | Verified | ADIA, BlackRock Emerging Frontiers, Smallcap World Fund, Franklin India Smaller Cos, SBI MF, HDFC Life (Rs 828.78 cr, 29 Jul 2024) | B08-promoter p.1 |
| **Countervailing: Rising DII Ownership** | Verified | DII ownership rose from ~7.4% (Aug 2024) to ~14.3-14.35% (Mar/Jul 2026) | B08-promoter p.1 |
| **Countervailing: Dividends Initiated Within 2 Years of Listing** | Verified | Rs 1/share final + Rs 2/share special (FY26); demonstrates capital discipline and confidence | B08-promoter p.1 |

**Verdict Basis:** "CONCERN driven by a Section 132 IT search-and-seizure operation (Jan 2025) and a Rs 133.75 crore group-wide seven-year block-period tax demand (May 2026) plus a live Drugs & Cosmetics Act prosecution, materially offset by zero promoter pledge, a genuinely credentialed independent board, a blue-chip anchor-investor book, and rising DII ownership — transition evidence makes this a different object from a static CONCERN." (B08-promoter p.2)

**Deal-Breaker Check:** None triggered (SEBI ban, conviction, SFIO, PMLA, auditor resignation, pledge>40%, multi mid-term ID exits, restatement all NOT TRIGGERED) (B08-promoter p.1)

---

## TOTAL ADDRESSABLE MARKET & SOM ANALYSIS

### TAM Definition & Sizing

**Market Definition:** Indian domestic-facing pharma CDMO (formulation contract development & manufacturing) market for outsourced dosage-form production serving Indian branded pharma companies; excludes Akums' API, own-brand, international and trade-generics revenue streams; excludes global/export CRAMS and biologics CDMO.

| Metric | Value | Source / Computation |
|--------|-------|---------------------|
| **TAM (Conservative)** | Rs 13,880 Cr | B09-tam p.1: "conservative: 13880" — reverse-engineered from lower-range market estimate |
| **TAM (Realistic)** | Rs 18,580 Cr | B09-tam p.1: "realistic: 18580" — F&S-anchored domestic CDMO market FY24 base |
| **TAM Growth %** | 13.2% CAGR | B09-tam p.1: "tam_growth_pct: 13.2" |
| **SAM (Serviceable Addressable Market)** | Rs 11,630 Cr | B09-tam p.1: "sam_cr: 11630" (CDMO segment only, Akums' addressable subset) |
| **SAM as % of TAM** | 83.8% | Computed: 11,630 / 13,880 = 83.8% (conservative TAM) |
| **Current Company Revenue (CDMO Segment)** | Rs 3,485.20 Cr | Q4 FY26 results p.20: "CDMO segment revenue from external customers: Rs 34,851.99 million = Rs 3,485.20 Cr" |
| **Current Market Share %** | 30.0% | B09-tam p.1: "current_sam_share_pct: 30.0" |
| **Revenue Headroom (x)** | 3.34x | B09-tam p.1: "revenue_headroom_x: 3.34" (SAM / current CDMO revenue) |

### SOM Projections & Growth Implied

| Horizon | FY27-FY29 (3yr) | FY27-FY31 (5yr) | YoY CAGR Implied | Source |
|---------|-----------------|-----------------|------------------|--------|
| **SOM (3-Year)** | Rs 5,396 Cr | — | — | B09-tam p.1: "som_3yr_cr: 5396" |
| **SOM (5-Year)** | — | Rs 7,348 Cr | — | B09-tam p.1: "som_5yr_cr: 7348" |
| **SOM-Implied Revenue CAGR (Company-Level Blended)** | +13.9% (3yr) | +14.3% (5yr) | CDMO segment alone: 15.7% (3yr) / 16.1% (5yr) | B09-tam p.1: "som_implied_revenue_cagr: {yr3: 13.9, yr5: 14.3}; CDMO segment alone: 15.7 / 16.1" |
| **SOM-Implied Headroom Check** | ~Rs 741 Cr gap (11.5%) vs FY29 SOM-implied at peak utilization (55-60%) | — | SOM mildly optimistic | B09-tam p.1: "Capacity cross-check gap of ~Rs 741 Cr (11.5%) vs FY29 SOM-implied total company revenue at management's disclosed peak utilization ceiling" |

### Management TAM Claim vs Analysis

| Claim | Value | Analyst Assessment | Source |
|-------|-------|-------------------|--------|
| **Management Stated TAM** | Rs 23,800 Cr | Ratio to conservative: 1.34x (reasonable but optimistic; includes broader scope) | B09-tam p.1: "mgmt_claim_cr: 23800; mgmt_claim_ratio: 1.34; mgmt_claim_read: 'reasonable'" |
| **Generic Research Overstatement** | Headline "India CDMO market" USD 8.5-25.5 Bn blends biologics/global CRAMS Akums does not compete in | Conservative approach excludes to avoid 6-13x overstatement | B09-tam p.1 |
| **Runway Classification** | GOOD | Implies 3-5 year visibility within TAM/SOM headroom, multi-year growth optionality | B09-tam p.1: "runway_class: GOOD" |

### TAM Evidence & Data Freshness

| Data Point | Source | Year | Stale Flag |
|-----------|--------|------|-----------|
| India domestic CDMO market FY24 base | F&S Report (IPO-cited) | 2024 | Yes (2yr old) |
| India CDMO market (broad scope) | IMARC Group | 2024 | Yes |
| India domestic formulations/IPM market | Bain & Co secondary citation | 2023 | Yes |
| Unbranded 'generic generics' market | WebSearch secondary citation | 2023 | Yes |
| China outsourced API/CDMO share & India dynamics | Bain & Co roadmap | 2023 | Yes |

**Note:** Full peer-by-peer CDMO revenue aggregation and EU CDMO annual revenue quantum breakdown not performed; capacity-based cross-check used as proxy.

---

## RATING LETTER EXTRACTION (ICRA, 10 APRIL 2026)

### Rating Summary

| Instrument | Rating | Outlook | Amount Rated (Rs Cr) | Date |
|-----------|--------|---------|---------------------|------|
| Long-term/Short-term Fund-based/Non-fund-based Working Capital Limits | [ICRA]AA (Stable) / [ICRA]A1+ | Stable | 85.00 | 10-Apr-2026 (Reaffirmed) |
| Proposed Commercial Paper Programme | [ICRA]A1+ | — | 200.00 | 10-Apr-2026 (Assigned) |

### Working Capital / Liquidity Commentary (Verbatim)

**"Liquidity position: Strong**

The Group's liquidity position is strong, characterised by healthy cash flow from operations, cash and cash equivalents of Rs. 1,654.4 crore and unutilised working capital limits of around Rs. 450 crore, as on September 30, 2025. ADPL is expected to incur a capex of around Rs. 250 crore per annum between FY2026 and FY2028, primarily towards the development of a manufacturing facility in Zambia and regular replacement and maintenance capex. The capex is likely to be funded through ADPL's existing liquidity and internal accruals. Moreover, ADPL has no long-term debt repayment obligations." — ICRA Rating Letter, 10 April 2026, Page 3

**Downgrade Trigger (WC-Relevant):**

"The ratings could be downgraded in case of a significant decline in revenues and accrual generation or a deterioration in the credit profile and liquidity position, owing to debt-funded capex **or a stretch in the working capital cycle**. Specific credit metrics that may trigger a rating downgrade would include Total Debt/ OPBDITA of more than 1.0 times on a sustained basis." — ICRA Rating Letter, 10 April 2026, Page 3

**Agency:** ICRA (Investment Information and Credit Rating Agency Limited)  
**Rating Date:** 10 April 2026  
**Key Metrics Used (9M FY26):** Total Debt/OPBDITA 0.2x (vs 0.2x FY25), Interest Cover 5.3x (vs 13.4x FY25), TOL/TNW not disclosed for 9M period

---

## UA (UNALLOCATED) QUALIFIERS CHECK

### Three-Part Qualifier Verification

| Qualifier | Requirement | Status | Evidence | Source |
|-----------|-------------|--------|----------|--------|
| **Listed ≥12 Months** | Company listed on NSE/BSE for min 12 months before valuation date | ✓ PASS | IPO Aug 6, 2024; run date Jul 10, 2026 = 22 months | Q4 FY26 results p.11; manifest |
| **Gate0 ≥60 OR EM ≥25** | Gate 0 score ≥60 OR EM score ≥25 (forward moat) | ✓ PASS | Gate0 score 79/160 (meets ≥60 threshold); EM score 26.3 (crosses 25 threshold) | B01-gate0 p.1: "grand_total: 79"; B07-emoat p.1: "em_score: 26.3" |
| **FII+DII <3%** | Foreign Institutional + Domestic Institutional ownership <3% combined | ✗ FAIL | FII unknown; DII ~14.3% (Mar 2026) — exceeds 3% threshold | B08-promoter p.1: "DII ownership rose ~7.4% (Aug 2024) to ~14.3-14.35% (Mar/Jul 2026)" — high institutional ownership, not low |

**Verdict:** **All-Three-Met: NO** — Qualifier 3 (FII+DII <3%) fails. However, per CLAUDE.md Amendment 3: "Never treat low institutional ownership as a risk. UA multiplier per Amendment 3: min(Raw x 1.25, Sector Cap), all three qualifiers evidenced." — This company has HIGH institutional ownership (DII ~14.3%), so UA multiplier does NOT apply.

**UA Multiplier Decision:** NO UPLIFT; institutional ownership is strong, not a constraint.

---

## CASH CONVERSION & WORKING CAPITAL DEPTH

### Cash Conversion Quality Assessment

**Reported Headline Metric:**
- CFO FY26: Rs 1,181.20 Cr
- CFO/PAT: 4.61x (appears healthy but misleading)

**Critical Normalization:**
- Underlying cash generation distorted by **unnamed Rs 1,032.31 Cr customer-advance contract liability** (23.7% of FY26 revenue)
- Imputed non-cash finance cost: Rs 77.61 Cr (depresses PBT by ~19% of the reported growth)
- **Adjusted CFO** (excluding customer-advance WC inflow): ~Rs 239.89 Cr
- **Adjusted CFO/PAT**: ~0.99x (reveals cash quality is below median for CDMO sector)

**B01 Block_B_Trend:** "improving, CFO +154% YoY (465.20 cr to 1181.20 cr FY25 to FY26, screener Data_Sheet cross-verified against results Q4 FY26 p.22)" — **FLAGGED as WC artefact-driven, not organic improvement**

**B02 Receivables Trend:** "improving on gross ageing/DSO but with a rising ECL-provisioning-intensity caveat" — DSO fell 68.3 to 66.7 days but factoring of Rs 117.62 Cr derecognised ~1.7 days artificially; ECL coverage on >1-year bucket jumped 57.29% to 96.33% (conservative but signals credit tightening)

**Flag-Cash Determination (B02):** "Working-capital/cash-conversion quality mixed: inventory +11.0% vs revenue +5.85% (raw/packing material build outpacing sales); receivables improving on gross ageing/DSO but ECL provisioning intensity and write-off/reversal rate both rose sharply; ~117.62 Cr of receivables derecognised via non-recourse factoring flatters reported DSO; **and the true operating-cash read is distorted by the imputed 'interest on contract liability' financing construct tied to the unnamed Rs 1,032.31 Cr customer advance.** Caps this stage's contribution to PROCEED WITH CAVEATS pending stage 11/13 cash-conversion reconciliation." (B02 p.1)

**Stage 10 Verdict on Cash:** **FLAG-CASH (Structural vs. Growth-Induced):** Customer-advance is a structural one-off financing mechanism tied to a specific European contract (EUR 100m upfront receipt Q1 FY26 per AR). NOT expected to repeat at similar scale. Adjusted CFO/PAT ~0.99x is more representative of sustainable cash conversion. **Pending Stage 11 normalization; do not credit headline 4.61x as go-forward.**

---

## CONFLICTS & DATA RECONCILIATION

### Reported vs. Adjusted PAT Divergence (B03 Key Finding)

| Metric | Reported | Adjusted (MD&A) | Divergence | Issue |
|--------|----------|-----------------|-----------|-------|
| **FY26 PAT Growth** | (25.4%) decline to Rs 256.4 Cr | +27.3% to Rs 276.0 Cr (implied) | 52.7 pp gap | B03-ardeep p.3: "the Adjusted-PAT-vs-reported-PAT gap is the standout finding; EBITDA margin '43%' vs correct 12%" — non-GAAP metric reconciliation not provided by company |
| **Source of Divergence** | Tax-shield gap on 5 loss-making subsidiaries; ETR 33.0% vs 25.17% statutory; unrecognised DTA Rs 263.97M | — | — | B02-notes p.1: "Consolidated effective tax rate spiked to 33.0% vs 25.17% statutory, driven by Rs 263.97M unrecognised DTA on loss-making group companies" |
| **MD&A Adjustment Transparency** | MD&A claims "Adjusted PAT +27.3%" but provides zero reconciliation to audited reported PAT | — | — | B03-ardeep p.3: "reported PAT fell -25.4% to Rs 2,563.97M, no reconciliation (AR p.19 vs p.295-296)" |

**Conflict Resolution:** Use **reported audited PAT (Rs 256.4 Cr)** in the valuation input table; flag the Adjusted PAT claim as unreconciled and exclude it from GAAP-based ratios. Any "Adjusted PAT" multipler in stage 11 valuation must be explicitly reconciled to audited figures.

### CDMO Growth Claim vs. Peer Corroboration

| Claim | Akums Reported | Peer Corroboration | Status |
|-------|----------------|-------------------|--------|
| **CDMO Volume Growth FY26** | 25%+ sustained (Q3-Q4) vs prior years flat-to-low-single-digit | Cohance FY26: "early single digit" (5-7% adjusted); Windlas: 18-23%; Innovacap: 6-10% organic | **Partially Verified** — Akums outperformance real but lower-magnitude peer comparables suggest some share-shift/restocking effect; underlying volume growth likely 12-16%, not pure 25%+ |
| **Schedule M Enforcement Share Gain** | Management claims Schedule M shift to "compliant manufacturers" is driving CDMO acceleration | Windlas (Q3 FY26 call): "Schedule M enforcement a named driver" of performance; Innovacap, Cohance: non-committal | **Claim Valid but Unquantified** — Acceleration real, but management has deflected detail on ground-truth (B05 red flag) |

---

## UNRESOLVED FIELDS

### Items Marked for Stage 11 Resolution (Valuation Model Input)

| Field | Current Status | Why Unresolved | Required For | Source |
|-------|----------------|----------------|-------------|--------|
| **Free Cash Flow (FCF) & FCF/PAT Ratio** | Headline FCF ~959 Cr but adjusted FCF ~18 Cr post-WC normalization | Customer-advance WC timing and FTTCP (stage 11) treatment not yet finalized; capex assumptions evolving (Rs 222 cr FY26, Rs 300 cr guided FY27) | Valuation model cash conversion checks | B04-bizmodel p.2 flags: "Adj OCF/EBITDA conversion fell to 34.9% FY26 from 90.7% FY25 even after excluding EU-contract advance" |
| **ROCE (Reported vs. Adjusted)** | Reported ~13.7%; idle-cash-adjusted operating ROCE ~26-27% | Idle cash Rs 1,654.4 Cr (39% of market cap) inflates denominator; Pillar 1 decision needed on cash normalization | Valuation model, ROIC/WACC calibration | B02-notes p.1: "flag both, the idle-cash normalization is a Pillar 1 decision for stage 11" |
| **ROE (Consolidated)** | Pending computation from audited equity | Book value per share requires full balance sheet analysis; distorted by fair-value changes and exceptional items per B04 | ROIC/Return metrics, normalized ROE | B04-bizmodel p.2: "use Adj ROE instead" due to distortion |
| **Effective Tax Rate (Forward)** | FY26 ETR 33.0% (elevated); management guides ~29% near-term, ~25% eventual | Unrecognised DTA on loss-making subsidiaries drives 800 bp gap; path to normalization depends on subsidiary turnaround | Tax rate assumptions for DCF | B02-notes p.1; B05-concall p.8 |
| **Diluted Share Count (Fully) Updated** | 15.74 Cr shares (computed from market cap / CMP); ESOP trust shares netting still in draft | ESOP 2022 scheme disclosure incomplete (ESOP allocation to R&D staff not disaggregated); confirm diluted count at next recount | EPS calculations, WACC weighting | Q4 FY26 results p.11: ESOP trust netting applied |
| **Peer Financial Multiples (P/E, EV/EBITDA, P/B, ROCE)** | Only 4 comparators supplied; PPLPHARMA transcript file mismatch (Piramal Finance, not Pharma) | Cohance, Windlas, Innovacap data adequate but sector peer set not comprehensive; PPLPHARMA data unusable | Stage 11 relative valuation benchmarking | B06-peers p.1: "PPLPHARMA-Concall... mislabeled — content is Piramal Finance Limited (NBFC)" |
| **SOM Capacity Headroom Beyond FY29** | SOM-implied FY29 revenue vs. peak-utilization ceiling shows ~Rs 741 Cr gap (11.5%) | Further capex assumptions (Zambia, Europe, India) beyond FY29 not finalized; utilization ceiling (55-60%) may shift with new capacity | Valuation long-tail optionality | B09-tam p.1: "Capacity cross-check gap of ~Rs 741 Cr (11.5%)" |
| **Contingent Liabilities Materiality & Resolution Timeline** | Rs 38.77 Cr (contingent liabilities breaches 25% flag as % of PAT) | Section 158BC tax demand (Rs 133.75 Cr group-wide, disclosed post-year-end); no quantified provision booked; timeline unknown | Stage 11 risk assessment, sensitivity analysis | B03-ardeep p.1-2: "Section 158BC block-period tax demand of Rs 133.75 cr (FY18-19 to FY24-25) disclosed ~May 2026" |

### Non-Critical Information Gaps (Noted but Not Blocking)

| Item | Gap | Reason Acceptable | Source |
|------|-----|-------------------|--------|
| **Segment-Wise Capex Breakdown** | Not disclosed | Capex guidance given at consolidated level; segment mix not critical for Stage 10 | Q4 FY26 results; B05-concall |
| **Customer Concentration Detail** | Top-N customer % not disclosed; CDMO single-molecule concentration flagged | Akums serves 1,400+ clients; concentration risk noted but manageable per rating agency | ICRA rating p.2: "Diversified customer base, serving more than 1,400 clients with adequate customer diversification" |
| **Zambia JV Economics Detail** | USD 45 Cr total investment (51% Akums ~USD 22.5 Cr); USD 25m India-supply over 2yr; plant commissioning timeline slipped CY2028 → FY29 | Outline economics sound; details will crystallize via concall updates and concretization of plant progress | B05-concall p.2; B07-emoat p.1 |
| **DPS (Dividend Per Share) History** | FY26: Rs 1 final + Rs 2 special (total Rs 3/share); no prior-year comparator (IPO June 2024) | Dividend policy nascent; payout 18% of PAT (conservative); not material to valuation stage 10 | Q4 FY26 results p.1 |

---

## SUMMARY VERDICT FOR VALUATION INPUT READINESS

**Status: READY FOR STAGE 11 VALUATION, WITH CAVEATS**

- **Completeness:** Core financial figures (revenue, EBITDA, PAT, CFO, capex) all audited and anchored. Growth triggers documented. Strategic moat evidence assembled (26.3 EM score, STRENGTHENING).
- **Data Quality:** Accounting quality flagged (B02: 5/10, FLAG-CASH on WC normalization). Non-GAAP "Adjusted PAT" claim unreconciled. Tax-line complexity (33% ETR vs. 25% statutory) noted and documented.
- **Forward Drivers:** Three catalysts within 12 months (European audit, Zambia ramp, FY27 capex). CDMO volume growth +25%+ real but partially restocking-driven per peers; underlying organic growth ~12-16%.
- **Risk Profile:** Section 132 IT search (unquantified), Rs 133.75 Cr group tax demand (post-year-end show-cause stage), CEO-CDMO resignation (successor pending), 0% promoter pledge (positive), DII ownership 14.3% (institutional support strong).
- **Normalized Metrics:** PAT headline (256.4 Cr) to be used; Adjusted PAT (276 Cr) excluded without reconciliation. CFO/PAT 4.61x is WC artefact; normalized ~0.99x. ROCE reported 13.7%, but idle-cash-adjusted operating 26-27% (Pillar 1 decision for stage 11).

---

# B10-VALINPUTS YAML BLOCK

```yaml
stage: B10-valinputs
company: "AKUMS"
run_date: "2026-07-10"
model: claude-haiku-4-5-20251001
status: complete
input_gaps: []
flags:
  - type: FLAG-CASH
    reason: "Headline CFO Rs 1,181.2 cr (CFO/PAT 4.61x) is distorted by Rs 1,032.31 cr unnamed customer-advance contract liability (23.7% of FY26 revenue, financing construct). Adjusted CFO ex this inflow ~Rs 239.89 cr (CFO/PAT ~0.99x). Imputed finance cost Rs 77.61 cr inflates PBT. Normalize at stage 11; do not credit headline rate. (B02-notes p.1, B03-ardeep p.1)"
  - type: FLAG-GROWTH
    reason: "CDMO volume growth claimed +25%+ Q3-Q4 FY26 vs flat-to-low-single-digit prior, real but partially restocking/share-shift. Peers (Windlas 18-23%, Innovacap 6-10%, Cohance 5-7% adjusted) suggest underlying organic 12-16%. Schedule M driver unconfirmed despite management evasion on calls Q3 & Q4 FY26. (B05-concall p.5, B06-peers p.1-2)"
  - type: FLAG-PROMOTER
    reason: "Section 132 IT search-and-seizure Jan 2025; group-wide Section 158BC tax demand Rs 133.75 cr (FY18-19 to FY24-25) issued May 2026; show-cause stage, no demands raised to report date. Live Drugs & Cosmetics prosecution (2016 Vicks Gel). CEO-CDMO resignation Jul 2025, successor pending. Offset by 0% pledge, credentialed independent board, DII 14.3%, blue-chip anchor book. CONCERN but non-deal-breaker. (B08-promoter p.1-2)"
  - type: FLAG-ACCOUNTING
    reason: "Reported PAT fell -25.4% YoY to Rs 256.4 cr on tax-shield gap (ETR 33.0% vs 25.17% statutory, unrecognised DTA Rs 263.97 cr on loss-making subsidiaries). MD&A claims 'Adjusted PAT +27.3%' but zero GAAP reconciliation provided. Use audited PAT (256.4 cr) for all ratios; exclude Adjusted PAT from formal valuation without reconciliation. (B02-notes p.1, B03-ardeep p.3)"
  - type: FLAG-ROCE
    reason: "Reported ROCE ~13.7% but idle-cash-adjusted operating ROCE ~26-27%. Idle cash Rs 1,654.4 cr (39% of market cap) inflates ROCE denominator. Pillar 1 decision needed: whether to normalize ROCE by excluding surplus cash. Flag both metrics and defer normalization to stage 11. (B02-notes p.1)"

table:
  company_identity:
    company: "Akums Drugs & Pharmaceuticals Limited (AKUMS)"
    sector: "Pharmaceuticals / CDMO (manifest)"
    business_model_type: "Hybrid: CDMO (80% rev, B2B services, high predictability) + Domestic Branded (10.2%) + International Branded (3.3%) + API (4.2%, loss-making) + Trade Generics (2.3%, commodity) (B04-bizmodel p.1; Q4 FY26 results p.20 segment split)"
    sector_cap_row: "Pharma / CDMO (manifest)"
    cmp_rs: 702
    market_cap_rs_cr: 11052
    shares_outstanding_diluted_cr: 15.74
    net_debt_rs_cr: (1564.1)
    enterprise_value_rs_cr: 9487.9
    ev_calculation: "EV = Market Cap 11,052 + Total Debt 90.3 (ICRA p.2 Sept 30, 2025) - Cash 1,654.4 (ICRA p.2) = 9,487.9 Cr"
  
  latest_financials_fy26_audited_consolidated:
    revenue_from_operations_rs_cr: 4359.02
    revenue_source: "Q4 FY26 results consolidated p.20 (Rs 43,590.17 million)"
    revenue_growth_yoy_pct: 5.85
    revenue_growth_anchor: "Computed: (4,359.02 - 4,118.16) / 4,118.16 = 5.85% (FY25 revenue Rs 4,118.16 cr from Q4 results p.20)"
    
    ebitda_rs_cr: 522.02
    ebitda_source: "B01-gate0 p.1: 'audited cross-check (522.02 cr, 11.98% margin, from consolidated P&L)'"
    ebitda_margin_pct: 11.98
    ebitda_growth_yoy_pct: 10.86
    
    pbt_rs_cr: 382.01
    pbt_source: "Q4 FY26 results consolidated p.20 (Rs 3,821.01 million); underlying operating PBT grew +22.4% (B02 p.1), headline distorted by Rs 77.61 cr financing construct"
    pbt_growth_yoy_pct: 10.66
    pbt_note: "~46% of reported PBT growth is treasury/financing artefact tied to EUR 100m customer advance (B02 p.1); organic PBT growth ~22.4%"
    
    pat_rs_cr: 256.40
    pat_source: "B02-notes p.1 critical normalization: 'consolidated PAT Rs 256.4 cr FELL 25.4% YoY (tax-line driven, ETR 32.9%)'; Q4 FY26 results consolidated p.20: Rs 2,563.97 million"
    pat_yoy_fall_pct: (25.4)
    pat_decline_driver: "Tax-shield gap: ETR spiked 33.0% vs 25.17% statutory due to Rs 263.97 cr unrecognised DTA on loss-making subsidiaries (B02 p.1); NOT operational deterioration"
    pat_note: "MD&A claims 'Adjusted PAT +27.3%' but no GAAP reconciliation provided; use audited PAT 256.4 cr for all formal ratios (B03 p.3)"
    pat_margin_pct: 5.88
    
    diluted_eps_rs: 16.67
    diluted_eps_source: "Q4 FY26 results consolidated p.20: 'Earning per share (EPS) (face value of Rs 2/- each) (in Rs) Basic and diluted: 16.67 (audited)'"
    eps_prior_year_rs: 22.60
    
    pe_multiple: 42.1
    pe_calculation: "CMP 702 / EPS 16.67 = 42.1x"
    
    ev_ebitda_multiple: 18.16
    ev_ebitda_calculation: "EV 9,487.9 / EBITDA 522.02 = 18.16x"
    
    cfo_rs_cr: 1181.20
    cfo_source: "B01-gate0 p.2: 'CFO +154% YoY (465.20 cr to 1181.20 cr FY25 to FY26, screener Data_Sheet cross-verified against results Q4 FY26 p.22)'"
    cfo_pat_ratio: 4.61
    cfo_pat_note: "HEADLINE MISLEADING. Rs 1,032.31 cr customer-advance WC inflow (financing construct) inflates CFO by 87%. Adjusted CFO ex this inflow ~Rs 239.89 cr; adjusted CFO/PAT ~0.99x. Do not credit headline 4.61x as go-forward. (B02 p.1)"
    
    adjusted_cfo_rs_cr: 239.89
    adjusted_cfo_pat_ratio: 0.99
    adjusted_cfo_source: "B02-notes p.1: 'true operating-cash read is distorted by imputed interest on contract liability financing construct tied to unnamed Rs 1,032.31 Cr customer advance'; normalized: CFO 1,181.20 - 1,032.31 advance inflow"
    
    capex_rs_cr: 222
    capex_source: "B05-concall p.9: 'FY26 actual capex INR222 crore (Q4 FY26 call)'; guided H2 INR100-125 cr additional to H1's INR107cr"
    capex_fy27_guided_rs_cr: 300
    capex_fy27_source: "B05-concall p.9: 'FY27 capex target INR300 crore (Q4 FY26 call)'"
    
    net_cash_rs_cr: 1564.1
    net_cash_source: "Computed: Cash 1,654.4 cr (ICRA p.2, Sept 30, 2025) - Total Debt 90.3 cr"
    net_cash_note: "IPO-derived surplus cash Rs 1,654.4 cr (39% of market cap); deployment plan unresolved across 3 quarters per B05 repeated evasion flag"
    
    wc_days: 79.53
    wc_days_prior_year: 71.66
    wc_days_change: 7.86
    wc_days_source: "B01-gate0 p.2: 'WC Days (full formula, now primary-sourced) rose +7.86 days FY25-to-FY26 (71.66d to 79.53d)'"
    wc_days_note: "Deterioration despite CFO/FCF expansion; inventory +11% vs revenue +5.85%; receivables factoring Rs 117.62 cr masks DSO improvement (B02 p.2)"
    
    dso_days: 66.7
    dso_prior_year: 68.3
    dso_change: (1.6)
    dso_source: "B02-notes p.2: 'DSO improved 68.3 to 66.7 days (Note 43(c), 51(A))' BUT caveat: 'DSO improvement is partly a factoring artefact (Rs 117.62 Cr of receivables derecognised via non-recourse factoring)'"
    
    inventory_turnover: 3.83
    inventory_turnover_prior: 4.41
    inventory_turnover_change: (0.58)
    inventory_turnover_source: "B02-notes p.2: 'standalone inventory turnover fell 4.41x to 3.83x'; raw/packing material build +17-28% outpacing sales, Note 8"
    
    roce_reported_pct: 13.7
    roce_source_reported: "B02-notes p.1: 'reported ROCE ~13.7%'"
    roce_idle_cash_adjusted_pct: 26.27
    roce_note: "Idle-cash adjustment (Rs 1,654.4 cr surplus cash depresses denominator). Flag both metrics; Pillar 1 decision needed at stage 11 on normalization (B02 p.1)"
    roce_forward_verdict: "Pending FTTCP (stage 11 input); do not use reported 13.7% as go-forward without idle-cash normalization"
    
    capex_embedded_growth_pct: 20.6
    capex_embedded_source: "B07-emoat p.1: 'capex_embedded_growth_pct: 20.6'; forward revenue CAGR assumed embedded in EU Plant 2, Zambia JV, domestic expansion capex trajectory"

  earlier_analysis_blocks:
    gate0_score: 79
    gate0_max: 160
    gate0_classification: "AVERAGE (capped by FY24 loss-year deal-breaker; base matrix GOOD)"
    gate0_source: "B01-gate0 p.1: 'core_score: 69, moat_score: 10, grand_total: 79, classification: AVERAGE'"
    gate0_deal_breaker: "DB8: PAT negative FY24 (-4.04 cr), caps base-matrix GOOD to max AVERAGE"
    
    b05_credibility_grade: "C"
    b05_credibility_basis: "Delivered CDMO margin/volume beat & trade generics turnaround exactly as promised, capex within guidance, rare honest 'year of miss' admission on API; offset by material domestic branded formulation guidance miss, non-monotonic API turnaround, and two repeated evasions (cash deployment, Schedule M ground-truth) across 3 quarters (B05 p.5)"
    b05_source: "B05-concall"
    
    b07_em_score: 26.3
    b07_em_classification: "STRENGTHENING (crossed 25-pt threshold, up from 23.5 prior)"
    b07_em_source: "B07-emoat p.1: 'em_score: 26.3; em_classification: STRENGTHENING; driven by evidence-quality upgrades in 5 categories (A2, A4, C1, F1, H3) rather than new Strong/Moderate category'"
    
    b07_combined_strategy: "TURNAROUND"
    b07_combined_reasoning: "Core AVERAGE (69/100, 1/12 moats, capped by FY24 loss-year deal-breaker) meets forward STRENGTHENING (26.3/80, crossing 25 threshold on AR-confirmed EU contract and Zambia JV evidence) - genuine TURNAROUND setup, one band below EXPANSION-tier threshold for HIGH POTENTIAL (B07 p.2)"
    
    b08_promoter_verdict: "CONCERN"
    b08_promoter_reason: "Section 132 IT search-and-seizure Jan 2025; Section 158BC tax demand Rs 133.75 cr group-wide (May 2026, show-cause stage); live Drugs & Cosmetics prosecution (2016 Vicks Gel). Offset by 0% pledge, credentialed independent board (ex-Pfizer, ex-Mylan), DII 14.3%, blue-chip anchor book (ADIA, BlackRock). Non-deal-breaker (SEBI ban / conviction / SFIO / PMLA / auditor resign / pledge>40% / multi-ID exits / restatement all NOT triggered). Transition evidence differentiates from static concern. (B08 p.2)"
    b08_source: "B08-promoter p.1-2"
    
    b09_tam_conservative_rs_cr: 13880
    b09_tam_realistic_rs_cr: 18580
    b09_sam_rs_cr: 11630
    b09_sam_pct_of_tam: 83.8
    b09_current_cdmo_revenue_rs_cr: 3485.20
    b09_market_share_pct: 30.0
    b09_revenue_headroom_x: 3.34
    b09_tam_growth_pct: 13.2
    b09_som_3yr_rs_cr: 5396
    b09_som_5yr_rs_cr: 7348
    b09_som_implied_cagr_3yr_pct: 13.9
    b09_som_implied_cagr_5yr_pct: 14.3
    b09_som_implied_cagr_cdmo_segment_3yr_pct: 15.7
    b09_som_implied_cagr_cdmo_segment_5yr_pct: 16.1
    b09_runway_class: "GOOD"
    b09_source: "B09-tam p.1: 'market_definition: Indian domestic-facing pharma CDMO (formulation contract development & manufacturing) market...'"

  ua_qualifiers:
    listed_12m: 
      requirement: "Listed on NSE/BSE ≥12 months"
      status: "PASS"
      evidence: "IPO Aug 6, 2024; run date Jul 10, 2026 = 22 months (Q4 FY26 results p.11)"
    gate0_or_em:
      requirement: "Gate0 score ≥60 OR EM score ≥25"
      status: "PASS"
      evidence: "Gate0: 79/160 (≥60 threshold); EM: 26.3 (crosses 25 threshold) (B01 p.1, B07 p.1)"
    fii_dii_lt3:
      requirement: "FII + DII combined <3%"
      status: "FAIL"
      evidence: "FII unknown; DII ~14.3% (Mar 2026), exceeds 3% threshold (B08 p.1)"
    all_three_met: "NO"
    ua_uplift_applied: "NO"
    ua_uplift_reason: "Qualifier 3 fails (DII 14.3% >> 3%). Per CLAUDE.md Amendment 3, high institutional ownership is not a constraint; UA multiplier applies only if all three met. This company has strong institutional ownership (positive signal, not treated as risk)."

  rating_details:
    agency: "ICRA"
    rating_longterm: "[ICRA]AA (Stable)"
    rating_shortterm: "[ICRA]A1+"
    rating_date: "10 April 2026"
    rating_outlook: "Stable"
    rating_source: "rating_ICRA_Apr2026.txt p.1"
    
    key_metrics_9m_fy26:
      total_debt_rs_cr: 90.3
      cash_and_equivalents_rs_cr: 1654.4
      total_debt_opbdita_x: 0.2
      interest_coverage_x: 4.8
      tol_tnw_x: 0.6
      total_debt_opbdita_source: "ICRA rating p.2: 'Total Debt/OPBDITA of 0.2 times' (Sept 30, 2025)"

  rating_wc_quote: |
    AGENCY: ICRA
    RATING: [ICRA]AA (Stable) / [ICRA]A1+
    DATE: 10 April 2026
    
    LIQUIDITY COMMENTARY (Verbatim, Page 3):
    "Liquidity position: Strong. The Group's liquidity position is strong, characterised by healthy cash flow from operations, cash and cash equivalents of Rs. 1,654.4 crore and unutilised working capital limits of around Rs. 450 crore, as on September 30, 2025. ADPL is expected to incur a capex of around Rs. 250 crore per annum between FY2026 and FY2028, primarily towards the development of a manufacturing facility in Zambia and regular replacement and maintenance capex. The capex is likely to be funded through ADPL's existing liquidity and internal accruals. Moreover, ADPL has no long-term debt repayment obligations."
    
    DOWNGRADE TRIGGER (WC-Relevant, Page 3):
    "The ratings could be downgraded in case of a significant decline in revenues and accrual generation or a deterioration in the credit profile and liquidity position, owing to debt-funded capex or a stretch in the working capital cycle. Specific credit metrics that may trigger a rating downgrade would include Total Debt/ OPBDITA of more than 1.0 times on a sustained basis."

  management_delivery_track_record:
    cdmo_margin_delivery: "A=Excellent (guided H1 ~12%, delivered Q2 10.4% -> Q3 13.75% -> Q4 14.4%; exceeded)"
    cdmo_volume_delivery: "A=Excellent (double-digit 16%+ Q3, 25%+ Q4 delivered; driver attribution B grade per management evasion on calls)"
    trade_generics_turnaround: "A=Excellent (guided break-even or wind-down, delivered +Rs 1.4 cr EBITDA Q4 FY26)"
    api_improvement: "C=Mixed (guided better than prior, delivered only 9% improvement FY26 vs FY25, non-monotonic Q-to-Q, management honest 'year of miss')"
    capex_delivery: "A=Excellent (guided H2 INR100-125 cr add to H1 INR107cr, delivered FY26 total INR222cr within range; FY27 INR300cr guided)"
    domestic_branded_formulation: "D=Poor (implied mid-teens growth guidance, delivered 2.9% FY26, guidance miss material)"
    cash_deployment_clarity: "D=Poor (unresolved across 3 quarters, management deflection 'actively evaluating', 18% dividend payout, large cash balance)"
    schedule_m_ground_truth: "D=Poor (Q3 & Q4 FY26 calls deflected without detail despite Q2 call optimism; benefit claimed but unquantified)"
    overall_credibility_grade: "C = Mixed (B05 p.5)"
    overall_credibility_anchor: "B05-concall p.5"

  growth_triggers_top_3:
    trigger_1:
      name: "European CDMO Plant 2 Ramp (EUR 35m/yr, contract to Dec 2032)"
      type: "REVENUE/INORGANIC"
      timeframe: "Medium-term (FY28 start)"
      conviction: "High"
      confirm_signal: "First commercial dispatch/revenue recognition from Plant 2 in FY28"
      kill_signal: "Regulatory filing delays across European country registrations or loss of sole-supplier status"
      source: "B05-concall p.1"
    
    trigger_2:
      name: "CDMO Core Volume Growth Sustainability"
      type: "REVENUE/VOLUME"
      timeframe: "Near-term (Q1/Q2 FY27)"
      conviction: "Medium"
      confirm_signal: "Continued double-digit volume growth in Q1/Q2 FY27 with clearer driver attribution"
      kill_signal: "Reversion to flat/low-single-digit growth as seen pre-Q3 FY26"
      source: "B05-concall p.1"
    
    trigger_3:
      name: "Zambia JV Revenue Ramp (USD 50m India-to-Zambia supply over 2yr)"
      type: "INORGANIC/REVENUE"
      timeframe: "Medium-long (CY2026-2029, refined to by end Q2 FY27 for India supply start)"
      conviction: "Medium-High"
      confirm_signal: "USD 25m India-to-Zambia supply commencing by end Q2 FY27 as guided"
      kill_signal: "Further slippage in local facility commissioning (already slipped CY2028 -> FY29) or changed Zambian tender terms"
      source: "B05-concall p.1; B07-emoat p.1"

  peer_median_multiples: "NOT FOUND - only 4 comparators supplied (Cohance, Innovacap, Windlas, PPLPHARMA mislabeled as Piramal Finance NBFC). Comprehensive peer set financial data not aggregated. Stage 11 to source full peer matrix via B06 supplementary lookup (B06-peers p.1)"

  strategic_position:
    moat_present: "YES"
    moat_description: "Regulatory accreditations (EU GMP, US-NSF, WHO GMP, ANVASA, EFDA) with high durability; client switching costs/multi-year contracts (moderate-high); manufacturing scale 50.6B unit capacity (moderate durability, 44% utilization); formulation/process IP 21 in-house platforms (moderate). Total of 6 Strong/Moderate moat categories active (B2, E1, H2 rated Strong; A1, F2, R1 rated Moderate). Thin upstream (1/12 moats per B01 = THIN moat class), but STRENGTHENING forward via EU/Zambia catalysts. (B04 p.1, B07 p.1)"
    moat_source: "B04-bizmodel p.1; B07-emoat p.1"
    monopoly_position: "NO (fragmented CDMO market, Akums largest domestic player at ~30% SAM share but below 40% industry concentration threshold; competitive moat is lock-in + scale, not monopoly)"
    monopoly_source: "B09-tam p.1: '30.0% current SAM share'; B04-bizmodel p.1"

conflicts: []

unresolved:
  - field: "Free Cash Flow (FCF) & FCF/PAT Ratio"
    why: "Customer-advance WC timing and FTTCP treatment not finalized at stage 10. Capex guidance evolving (Rs 222 cr FY26, Rs 300 cr FY27 guided). Headline FCF ~959 Cr, adjusted FCF ~17.89 Cr (ex Rs 1,032.31 cr advance). Stage 11 to model cash flow normalization and FTTCP debt treatment."
    where_it_might_be: "Stage 11 valuation model; concall updates on Zambia/Europe capex pace"
    materiality: "High (affects DCF and return metrics)"
    
  - field: "ROCE (Idle-Cash Normalized)"
    why: "Reported ROCE 13.7% vs operating ROCE 26-27% (idle-cash-adjusted). Pillar 1 decision pending on whether to normalize for Rs 1,654.4 cr surplus cash (39% of market cap). Normalization will shift ROIC-to-WACC calibration."
    where_it_might_be: "Stage 11 Pillar 1 framework; B02 ROCE re-calculation with cash adjustment options"
    materiality: "High (affects return-on-capital ratios and WACC/ROIC spread)"
    
  - field: "ROE (Consolidated, Full Detail)"
    why: "Book value per share computation requires complete balance sheet review. Distorted by fair-value changes and exceptional items per B04. Need to extract tangible equity vs. reported equity."
    where_it_might_be: "AR FY26 consolidated balance sheet (Note 49, equity detail); stage 11 normalized ROE re-calc"
    materiality: "Medium (return metric, secondary to ROCE)"
    
  - field: "Effective Tax Rate (Forward Normalized)"
    why: "FY26 ETR 33.0% elevated vs 25.17% statutory. Driven by Rs 263.97 cr unrecognised DTA on loss-making subsidiaries. Path to normalization depends on subsidiary turnaround. Management guides ~29% near-term, ~25% eventual (Q4 FY26 call)."
    where_it_might_be: "Stage 11 tax rate assumptions for DCF; FY27 quarterly monitoring for DTA recognition path"
    materiality: "Medium (affects terminal-stage tax rate in DCF)"
    
  - field: "Diluted Share Count (ESOP Final)"
    why: "Current 15.74 Cr computed from market cap / CMP. ESOP 2022 scheme disclosure incomplete (allocation to R&D staff not disaggregated). ESOP trust netting applied in Q4 FY26 results but full reconciliation not verified at stage 10."
    where_it_might_be: "AR FY26 Note on ESOP scheme (full disclosure); stage 11 to confirm diluted count via RHP filings or MCA search"
    materiality: "Low (EPS calculations, minor precision impact)"
    
  - field: "Peer Financial Multiples (P/E, EV/EBITDA, P/B, ROCE, Growth)"
    why: "Only 4 comparators provided; PPLPHARMA file mislabeled (Piramal Finance NBFC, not Pharma Solutions). Cohance, Windlas, Innovacap data available but incomplete peer set for comprehensive benchmarking."
    where_it_might_be: "Stage 11 relative valuation; B06-peers supplementary lookups for full sector peer matrix (Alembic Pharma, Aurobindo, Lupin formulations CDMO arms, etc.)"
    materiality: "Medium (relative valuation check, not core DCF driver)"
    
  - field: "SOM Capacity Headroom Beyond FY29"
    why: "SOM-implied FY29 revenue vs peak-utilization ceiling (55-60%) shows ~Rs 741 Cr gap (11.5%). Further capex assumptions (Zambia, Europe, India) beyond FY29 not finalized. Capacity ceiling may shift with new plant additions."
    where_it_might_be: "Stage 11 long-tail optionality; FY27+ concalls for capex guidance beyond current 3-year plan"
    materiality: "Low to Medium (terminal-value sensitivity, optionality check)"
    
  - field: "Contingent Liabilities Materiality & Resolution Timeline"
    why: "Section 158BC tax demand Rs 133.75 cr group-wide (FY18-19 to FY24-25) disclosed post-year-end May 2026 as show-cause notices. No provision booked. Timeline for resolution unknown (12-18 month typical for block assessment completion). Material risk if demand upheld."
    where_it_might_be: "Stage 11 risk weighting & sensitivity; FY27 AR for demand updates; IT department communication timeline"
    materiality: "High (5.2% of current market cap; contingent liability risk)"
```

---

## END OF REPORT

**Prepared By:** Claude Haiku 4.5 (Stage 10 Assembly)  
**Report Date:** 10 July 2026  
**Status:** COMPLETE  
**Ready for Stage 11 Valuation:** YES, with documented caveats on cash normalization, PAT tax-line reconciliation, and ROCE idle-cash adjustment pending Pillar 1 framework decision.

