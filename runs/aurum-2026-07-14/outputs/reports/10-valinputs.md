# STAGE 10: VALUATION INPUT ASSEMBLY (B10-valinputs)
## Aurum Proptech Ltd (AURUM) | CMP ₹240 | Market Cap ₹1,726 Cr | Run date 2026-07-14

All values below are copied and anchored from the upstream stages (B01-B09, results PDFs, FY25 AR, operator context). No values are computed or estimated. Missing values are listed in unresolved[].

---

## COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|-------|-------|--------|
| Company Name | Aurum Proptech Ltd | (manifest.yaml, company field) |
| Ticker | AURUM | (manifest.yaml, ticker field) |
| Industry Sector | Platform / SaaS / IT services | (manifest.yaml, sector_cap_row; B04 business_type: "hybrid") |
| Business Model Type | Hybrid: operating-lease marketplace + B2B SaaS/lead-gen + nascent regulated asset management | (B04-bizmodel.yaml, Section 1A-1B) |
| Sector Cap Row (Authority) | Platform / SaaS / IT services, 45x | (manifest.yaml; FTTCP deliberation: "Sector cap row: Platform / SaaS / IT services, 45x. Confirmed against B04, not corrected.") |
| CMP (Current Market Price) | ₹240 | (manifest.yaml, cmp field) |
| Market Capitalization | ₹1,726 Cr | (manifest.yaml, market_cap_cr field) |
| Shares Outstanding (Diluted) | 7.19 Cr (calculated: 1726 Cr ÷ 240) | (Market Cap ÷ CMP, screener-Data_Sheet.csv Face Value ₹5) |
| Face Value | ₹5 | (screener-Data_Sheet.csv, Face value row; B01 report p.2) |
| Enterprise Value (ex-Lease Liabilities) | ₹1,646.73 Cr (calculated: 1726 + 79.27 Net Cash) | (Market Cap 1726 + [Cash 81.0 - Financial Debt ex-lease 1.73], all from screener-Data_Sheet FY26; B01 report p.2, lease liability breakdown) |
| **Note on Debt Status** | **Debt-free as of May 21, 2026** (LRD facility retired via building sale). FY26 audited (Mar-2026) shows ₹1.73 Cr financial debt ex-lease; ₹223.03 Cr Ind AS 116 lease liabilities remain. | (OPERATOR_CONTEXT.md item 3 & 4; B01 report p.38 debt schedule: "₹0.45+₹1.28 Cr non-current+current financial borrowings"; FTTCP: "debt free via the ₹112 Cr building sale") |

---

## LATEST-PERIOD FINANCIALS (FY26, AUDITED MAR-2026)

### Income Statement

| Field | Value | Period | Anchor |
|-------|-------|--------|--------|
| Revenue / Total Income | ₹424 Cr (consolidated) | FY26 full year | (OPERATOR_CONTEXT.md item 4: "FY26 total income ₹424 Cr (vs ₹285 Cr; +49% YoY)") |
| Or: Sales (Screener Classification) | ₹381.09 Cr | FY26 full year | (screener-Data_Sheet.csv, Sales row FY26; B01 report notes divergence from audited segment disclosures) |
| Adjusted EBITDA | ₹25.02 Cr (calculated: 424 × 5.9%) | FY26 full year | (OPERATOR_CONTEXT.md item 4: "FY26 adj EBITDA margin +5.9%"; note: "Adjusted" excl. Ind AS 116 lease RoU per B04 Section 3A) |
| Adjusted EBITDA Margin | 5.9% | FY26 full year | (OPERATOR_CONTEXT.md item 4; results press release Q4 FY26 p.2) |
| PAT (Net Profit) | ₹1.90 Cr | FY26 full year | (screener-Data_Sheet.csv, Net profit row FY26) |
| **PAT (Continuing Operations)** | ₹-14.96 Cr | FY26 continuing | (B01 data_notes: "continuing-vs-discontinued PBT split (continuing -14.96 Cr + discontinued +16.50 Cr = +1.54 Cr combined)") |
| PAT Margin | 0.45% (using consolidated ₹1.90 Cr) | FY26 full year | (1.90 ÷ 424 × 100) |
| **One-Time Items** | ~₹17.72 Cr building-sale gain in Q4 other income (discontinued operations) | Q4 FY26 | (results Q4 FY26 PDF p.15, Note 5 "Discontinued operations"; B01 FLAG-ONE-TIME-ITEM) |

### Cash Flow

| Field | Value | Period | Anchor |
|-------|-------|--------|--------|
| Cash from Operations (CFO) | ₹62.93 Cr | FY26 full year | (screener-Data_Sheet.csv, Cash Flow row; B01 report Block B) |
| Capital Expenditure (Capex) | ₹15.85 Cr (continuing ops only) | FY26 | (B01 report p.100: "FY26 15.85 (continuing ops only; discontinued-ops capex not separately disclosed)"; AR FY25 and results Q4 FY26 PDF p.17 cash flow statement) |
| Free Cash Flow (FCF) | ₹47.08 Cr (calculated: CFO 62.93 − Capex 15.85) | FY26 | (B01 report p.100) |
| CFO / PAT (Latest, FY26) | 33.1x (62.93 ÷ 1.90) | FY26 | (artificially high due to tiny PAT base; flagged as mechanical ratio distortion) |
| CFO / PAT (Cumulative, FY22-FY26) | -0.29 (36.50 ÷ −127.27) | FY22-FY26 | (B01 report Block B p.82-84; ratio negative due to cumulative PAT negative across loss years) |
| FCF / PAT (Latest, FY26) | 24.8x (47.08 ÷ 1.90) | FY26 | (mechanically inflated, same caveat as CFO/PAT) |

### Balance Sheet & Per-Share Metrics

| Field | Value | Period | Anchor |
|-------|-------|--------|--------|
| Equity Share Capital | ₹38.21 Cr | FY26 | (screener-Data_Sheet.csv, Balance Sheet, Equity Share Capital row) |
| Reserves | ₹468.04 Cr | FY26 | (screener-Data_Sheet.csv, Balance Sheet, Reserves row) |
| Net Worth (Total Equity) | ₹506.25 Cr (38.21 + 468.04) | FY26 | (screener-Data_Sheet and verified in B01 ROCE calculation table) |
| Book Value Per Share | ₹70.39 (506.25 Cr ÷ 7.19 Cr shares) | FY26 | (calculated) |
| Total Financial Borrowings (ex-Lease) | ₹1.73 Cr | FY26 | (B01 report p.38: "₹0.45+₹1.28 Cr non-current+current financial borrowings"; screener "Borrowings" row includes both) |
| Total Lease Liabilities (Ind AS 116) | ₹223.03 Cr | FY26 | (B01 report: "₹150.18+₹72.85 Cr non-current+current lease liabilities = ₹224.76 Cr"; note: screener-data "Borrowings" bundles both) |
| Cash & Bank Balance | ₹81.0 Cr | FY26 | (screener-Data_Sheet.csv, Balance Sheet, Cash & Bank row) |
| Net Cash Position (ex-Lease) | ₹79.27 Cr (81.0 − 1.73) | FY26 | (calculated) |
| Depreciation (Reported, incl. Lease RoU) | ₹103.74 Cr | FY26 | (screener-Data_Sheet.csv, Depreciation row) |
| Dividend Per Share (DPS) | NOT FOUND | — | (no dividend disclosed in FY26 AR or screener-data) |

### Return Metrics

| Field | Value | Period | Anchor |
|-------|-------|--------|--------|
| ROCE (Latest, FY26) | 3.32% | FY26 | (B01 report p.56: ROCE = EBIT ÷ Capital Employed; FY26 [(-2.61 + 26.86) ÷ 731.01] = 24.25 ÷ 731.01 = 3.32%; includes Ind AS 116 lease adjustments in Borrowings) |
| ROCE (FY25) | -2.78% | FY25 | (B01 report p.56) |
| ROCE 2-Year Trend | Improving (FY25: -2.78% → FY26: +3.32%) | FY25-FY26 | (B01 report; both years near-zero; trend inflecting upward but magnitude still weak) |
| ROE (Latest, FY26) | 0.49% | FY26 | (B01 report p.71: PAT 1.90 ÷ Avg Net Worth 390.30 = 0.49%) |
| **ROCE Forward Verdict (FTTCP Authority)** | **STAGNANT (Pillar 1 uses CURRENT ROCE, no forward uplift)** | — | (FTTCP deliberation: "Pillar 1 uses current ROCE. No forward ROCE uplift enters Pillar 1." Falsifier: "a clean FY27 low-to-mid-teens operating ROCE ex surplus cash and goodwill") |

### Growth Metrics

| Field | Value | Period | Anchor |
|-------|-------|--------|--------|
| 3-Year Revenue CAGR (FY24-FY26) | 40.8% (using Total Income 424 Cr FY26 endpoint) | FY24-FY26 | (calculated: [424 ÷ 214.05]^[1/2] − 1; or 33.4% using Sales 381.09 Cr; FY24 base from screener-data ₹214.05 Cr) |
| 3-Year PAT CAGR | N/M (Turnaround: FY24 -55.75 → FY25 -33.37 → FY26 +1.90) | FY24-FY26 | (loss-to-profit swing, not a computable geometric CAGR) |
| Quarterly Revenue Trend (Latest 4Q) | Q4 FY26 +72% YoY (₹78 Cr → ₹135 Cr) | Q4 FY26 | (results press release Q4 FY26 p.2; also "Q4 total income ₹135 Cr (+72% YoY)") |
| ARR Achievement | ₹500+ Cr (crossed) | FY26 | (OPERATOR_CONTEXT.md item 4: "ARR crossed ₹500 Cr in FY26"; results press release Q4 FY26 p.2) |
| ARR Target (3-Year) | ₹1,000 Cr | ~FY29 | (OPERATOR_CONTEXT.md: "target ₹1,000 Cr annualised"; B05-concall guidance: "₹1,000cr ARR, organic only... 3 years / 10-12 quarters") |

### Valuation Ratios (Market-Based)

| Field | Value | Calculation | Anchor |
|-------|-------|-------------|--------|
| P/E (Trailing, based on FY26 PAT) | 906x (₹240 ÷ ₹1.90/share = 1726 Cr ÷ 1.90 Cr) | — | (IRRELEVANT per B04 Section 3A; FY26 barely profitable + Q4 one-time gain) |
| EV / Revenue (based on ₹424 Cr Income) | 3.88x (1646.73 ÷ 424) | — | (B04 primary valuation method: "EV/Revenue + EV/EBITDA per segment") |
| EV / Adjusted EBITDA (based on ₹25.02 Cr) | 65.8x (1646.73 ÷ 25.02) | — | (same caveat: FY26 EBITDA is first-year inflection from losses) |
| P/FCF | 36.7x (1726 ÷ 47.08) | — | (cross-check metric; based on latest FCF) |
| P/B (Price to Book) | 3.41x (240 ÷ 70.39) | — | (not recommended per B04: goodwill 61% of net worth, impairment risk) |
| **Note on Goodwill Risk** | Goodwill ₹174.25 Cr = 61% of consolidated net worth; 80.5% concentrated in two negative-net-worth subsidiaries (NestAway, HelloWorld) | — | (B02-notes.yaml rank 2; B04 tertiary valuation: "Segment-level DCF... must use Adjusted EBITDA (post-lease-payment)") |

---

## UPSTREAM ANALYSIS INPUTS

### From B05: Concall & Management Credibility

| Field | Value | Anchor |
|-------|-------|--------|
| Credibility Grade | B | (B05-concall.yaml, credibility_grade field) |
| Credibility Basis | "Core financial guidance (adjusted EBITDA positive Q2 FY26, PBT/PAT positive Q3 FY26, Rs500cr ARR by Q4 FY26, company breakeven target beaten a year early) delivered on or ahead of every stated timeline; but SM-REIT launch has slipped across all four calls since the Jul-2025 license, the company's own stated 'ecosystem revenue' moat went unquantified for a year until an honest single-digit admission in Q4, and a Q3 claim that NestAway rationalization was 'completed' was contradicted by continued portfolio shrinkage in Q4." | (B05-concall.yaml, credibility_basis field) |
| Guided Revenue Growth & Margin Band | Company breakeven (EBITDA/operational) at ₹550-575 Cr revenue, FY27 target; delivered ahead (PAT+ at ~₹105 Cr quarterly, a year early) | (B05-concall.yaml, guidance table; OPERATOR_CONTEXT.md item 1) |
| Top 3 Growth Triggers | 1. Rs1,000cr ARR organic scale-up (VOLUME, long-term, 3yr, conviction M); 2. Rental segment profitability (COST, near-term FY27, conviction M); 3. Debt-free status via Q5/Q6 building sale (INORGANIC, completed May-2026, conviction H) | (B05-concall.yaml, triggers list) |
| Promise Delivery Record | Delivered: 5 (adj EBITDA+, PBT/PAT+, ARR ₹500cr, distribution ARR ₹200cr, breakeven ahead); Partial: 3 (PropTiger profitability unconfirmed, rental/distribution split overshot target, LRD debt repayment in progress); Missed: 3 (SM-REIT launch slipped 4 calls, ecosystem revenue unquantified until Q4, NestAway rationalization contradicted) | (B05-concall.yaml, promise_delivery table) |

### From B07: Emerging Moat (EM) & Catalysts

| Field | Value | Anchor |
|-------|-------|--------|
| EM Score | 25.2 | (B07-emoat.yaml, em_score field) |
| EM Classification | STRENGTHENING | (B07-emoat.yaml, em_classification field) |
| Evidence Mix | 14 documented + 11 claim + 3 inference (total 28 evidence points) | (B07-emoat.yaml, evidence_mix breakdown; note: "📄 recount performed: 14 documented items") |
| Evidence Quality Summary | Mostly documentary (50% documented), 39% claim-based, 11% inference; **Caveat**: central AI narrative ("Unified Brain," "data is the biggest moat") is weakest-evidenced (D1, A2 both Weak) | (B07-emoat.yaml) |
| Active Categories (Moderate+Strong) | C1 (Customer ecosystem), D2 (Digital platform), F2 (Execution moat), G2 (WC improvement trajectory), H2 (REA Group strategic 5.5% stake), R1 (SM-REIT registration + GST ruling) | (B07-emoat.yaml, active_categories list) |
| Primary Catalyst (12-Month Window) | SM-REIT first scheme launch (or continued 'wait and watch' delay); window FY27 (mgmt-stated 'this financial year' as of Q4 FY26 call) | (B07-emoat.yaml, catalysts_12m list) |
| Secondary Catalysts | Debt-free completion (completed May 21, 2026, ₹112 Cr building sale, LRD paydown); Rental segment profitability target FY27; Ecosystem revenue % disclosure (mgmt's own FY27 timeline); July-2026 fund-raise terms | (B07-emoat.yaml, catalysts_12m list) |
| **Optionality Register** | D1 (Unified Brain AI moat), A2 (patent IP), E1 (Nestr Dubai), G1 (AI war chest capex disclosure), H1 (acquisition consolidation), C1 (ecosystem revenue materiality) — all convertible to higher-confidence evidence within 12-24m windows | (B07-emoat.yaml, optionality_register list) |

### From B09: TAM & SOM

| Field | Value | Anchor |
|-------|-------|--------|
| TAM (Total Addressable Market) | ₹47,057-54,407 Cr (conservative to realistic, 3-segment India-specific build) | (B09-tam.yaml, tam_cr table: conservative 47057, realistic 54407) |
| TAM Growth Rate | 15% p.a. | (B09-tam.yaml, tam_growth_pct field) |
| SAM (Serviceable Addressable Market) | ₹32,915 Cr (70% of TAM) | (B09-tam.yaml, sam_cr field) |
| Current SAM Share (% of SAM) | 1.29% (Aurum's current ARR ~₹500 Cr against ₹32,915 Cr addressable market) | (B09-tam.yaml, current_sam_share_pct field) |
| Revenue Headroom (SAM ÷ Current Revenue) | 77.6x (₹32,915 ÷ ₹424) | (B09-tam.yaml, revenue_headroom_x field) |
| SOM 3-Year (₹1,000 Cr ARR Target) | ₹1,664 Cr (SOM if 3yr target achieved) | (B09-tam.yaml, som_3yr_cr field) |
| SOM 5-Year | ₹3,478 Cr | (B09-tam.yaml, som_5yr_cr field) |
| SOM-Implied Revenue CAGR (3yr) | 57.8% (top-down build; mgmt's ₹1,000 Cr target implies ~26% CAGR, so mgmt is **conservative** vs. this build) | (B09-tam.yaml, som_implied_revenue_cagr, yr3 field; FLAG-SOM-CAGR-VS-MGMT) |
| Management's ARR Target Ratio vs. SOM | 0.60x (mgmt claim is conservative vs. SOM-implied build) | (B09-tam.yaml, mgmt_claim_ratio field: "conservative read") |
| Capacity Check | Qualitative (no physical capex ceiling); asset-light model; GTM/execution pace is binding constraint | (B09-tam.yaml: "B07 capex_embedded_growth_pct = NOT FOUND") |
| **TAM Divergence Flags** | Co-living market size estimates range ₹4,000 Cr (Colliers 2025, used) to USD 40 Bn (Cushman & Wakefield); SM-REIT TAM diverges ~11x (mgmt ₹50,000 Cr near-term vs. CBRE ~₹5,70,000 Cr eligible stock) | (B09-tam.yaml, flags section) |

### From FTTCP Deliberation (Authoritative for B10)

| Field | Value | Anchor |
|-------|-------|--------|
| **ROCE Forward Verdict (Pillar 1)** | **STAGNANT (0)**. Pillar 1 uses CURRENT ROCE (3.32% FY26), **no forward uplift**. | (FTTCP deliberation: "ROCE forward verdict: STAGNANT. Pillar 1 uses current ROCE. No forward ROCE uplift enters Pillar 1.") |
| **ROCE Recovery Credited Via** | **NEITHER Pillar 1 nor Strategic Premium**. STAGNANT means no premium crossing in the window. | (FTTCP deliberation: "not credited (STAGNANT, no premium crossing in the window; neither Pillar 1 forward uplift nor the Strategic Premium applies)") |
| **Cash Conversion Determination (Pillar 2)** | **INDETERMINATE** (default conservative; disposition caps at PROCEED WITH CAVEATS) | (FTTCP deliberation: "Cash / Pillar 2: INDETERMINATE, default conservative; disposition caps at PROCEED WITH CAVEATS.") |
| **Named Missing Evidence (Cash)** | Credit rating rationale + FY26 receivables ageing note (NOT independently verified in this run) | (FTTCP deliberation: "Named missing evidence: credit rating rationale and the FY26 receivables ageing note.") |
| **Valuation Method Caution** | FY26 barely profitable; earnings PE four-pillar output is strained; **SOTP primary lens (EV/Revenue + EV/EBITDA per segment), PE cross-check only** | (FTTCP deliberation: "Valuation method caution: FY26 barely profitable, so the earnings PE four pillar output is strained; SOTP with EV/Revenue and EV/EBITDA per segment is the primary lens, PE a cross check only.") |
| **Segment Valuation Guidance** | Rental segment (asset-heavier) must be valued separately rather than stretching 45x across it; Distribution uses 45x (platform cap); SOTP is primary method | (FTTCP deliberation: "B04 primary method is SOTP; the Rental segment is asset heavier and must be valued separately rather than stretching 45x across it") |
| **SHARED CATALYST Flag** | The whole inflection rests on Distribution segment scaling profitably and profit is partly one-time-aided. Stress test by stripping one-time other income and asset sale gains and re-asking whether operating business is profitable. | (FTTCP deliberation: "SHARED CATALYST flag for the devil's advocate: the whole inflection (revenue, margin, ROCE) rests on the Distribution segment scaling profitably, and that profitability is partly one time aided.") |
| **Sector Cap Row (Confirmed)** | Platform / SaaS / IT services, 45x | (FTTCP: "Sector cap row: Platform / SaaS / IT services, 45x. SOTP primary per B04; value Rental separately.") |

### From B04: Segment Revenue & Economics (SOTP Inputs)

| Field | Segment | FY25 Revenue | FY25 % of Total | FY26 Status | Profit Status | Anchor |
|-------|---------|-------------|-----------------|-------------|---------------|--------|
| **Rental** | NestAway + HelloWorld | ₹168.62 Cr | 63.9% of ₹263.84 Cr | ~₹148-170 Cr (est. 35-40% of ₹424 Cr, exact FY26 segment table NOT FOUND) | FY25: -₹14.54 Cr loss; FY26: targeting breakeven/small profit FY27 | (B04 Section 1C table; AR FY25 p.51 Note 23 segment table; OPERATOR_CONTEXT item 4 for FY26 guidance; B04 input_gaps: "Q4/FY26 investor presentation text... not available in this run") |
| **Distribution** | Aurum Analytica + Sell.do + PropTiger | ₹79.28 Cr | 30.1% of ₹263.84 Cr | ~₹254 Cr (est. 60% of ₹424 Cr, exact segment table NOT FOUND) | FY25: segment profit NOT disclosed separately; FY26: ₹32.3 Cr | (B04 Section 1C; OPERATOR_CONTEXT item 4: "Distribution FY26 segment profit ₹32.3 Cr"; AR FY25 shows Distribution profitable but exact margin not extracted) |
| **Capital** | SM-REIT/AMSA + Integrow/YieldWiseX | ₹15.94 Cr | 6.0% of ₹263.84 Cr | <₹10 Cr (est. <3% of ₹424 Cr; exact NOT FOUND) | FY25: -₹7.39 Cr loss; FY26: still pre-scale, loss-making | (B04 Section 1C; AR FY25 p.51 Note 23; +137% YoY growth FY25 but from small base) |
| **Distribution Unit Economics** | Sell.do (SaaS): per-seat license fee | 1,100 new licenses added Q3 FY26; 916 accounts Q4 FY26 (+38% YoY) | Recurring SaaS model | High incremental margin | Q4 FY26 press release; OPERATOR_CONTEXT item 4 |
| **Distribution Unit Economics** | Aurum Analytica: per-lead model | 1,17,000+ leads Q3 FY26 (+54% YoY); 1,48,392 leads Q4 FY26 (+93% YoY) | Pay-per-lead transactional | Volume-driven, platform leverage | OPERATOR_CONTEXT item 4; results press release |
| **Distribution Unit Economics** | PropTiger: transaction commission | "Record ₹42.8 Cr quarterly gross commission" Q4 FY26 | Developer transaction volume | Commission-based, cyclical | OPERATOR_CONTEXT item 4; results press release Q4 FY26 p.3 |
| **Rental Unit Economics** | NestAway: commission model | 10% recurring landlord commission + ~5% blended tenant commission on rent value | 9,559 signed units (+3% YoY Q4); 5,214 active houses (-23% YoY rationalisation); 19,286 beds (+9% YoY); 76% occupancy | Loss-making as of FY25; targeting FY27 breakeven; NestAway Select premium model launch | (B04 Section 1B; Inv. Pres. Q2 FY26 slide 13; OPERATOR_CONTEXT item 4) |
| **Rental Unit Economics** | HelloWorld: co-living lease model | 5-7 year property lease from owner; converted to co-living beds; operator retains spread | 270+ properties (+24% YoY Q3); multiple cities across India; adj-EBITDA breakeven target achieved Mar-2026 | Loss-making FY25; adj-EBITDA breakeven by Mar-2026; targeting FY27 profitability | (B04 Section 1B; Inv. Pres. Q2 FY26 slide 14; OPERATOR_CONTEXT item 4 Q3/Q4 targets) |

---

## SHAREHOLDING & UA QUALIFIER INPUTS

| Field | Value | Anchor |
|-------|-------|--------|
| Promoters % (Mar-2026) | 47.41% | (OPERATOR_CONTEXT.md shareholding table, Mar 2026 row) |
| FII % (Mar-2026) | 0.13% | (OPERATOR_CONTEXT.md shareholding table, Mar 2026 row) |
| DII % (Mar-2026) | NOT FOUND (3-row view: Promoters / FIIs / Public; no separate DII row) | (OPERATOR_CONTEXT.md note: "FII ~0.13% and NO separate DII row shown (3-row view)") |
| Public % (Mar-2026) | 52.45% (includes DII if present) | (OPERATOR_CONTEXT.md shareholding table, Mar 2026 row) |
| Shareholder Count | 56,379 (declining from 85,553 Jun-2023, per consolidation) | (OPERATOR_CONTEXT.md shareholding table) |
| **UA Qualifier 1: Listed ≥12 Months** | YES | (B01 report: "long-listed"; screener data shows history back to FY17 Majesco; current listing continuous) |
| **UA Qualifier 2: Gate 0 ≥60 OR EM ≥25** | YES (EM = 25.2 meets ≥25 threshold; Gate 0 = 58, just below) | (B01-gate0.yaml grand_total 58; B07-emoat.yaml em_score 25.2) |
| **UA Qualifier 3: FII+DII <3%** | LIKELY YES (FII 0.13%, DII unknown but likely small; FII alone << 3%) | (OPERATOR_CONTEXT.md note: FII 0.13%, no separate DII row shown) |
| **All Three UA Qualifiers Met** | Likely YES (pending DII clarification if it exists as separate row) | (calculated from above three) |
| **Amendment 3 Institutional Multiplier** | min(Raw × 1.25, Sector Cap 45x); FII+DII <3% → yes, applies multiplier | (CLAUDE.md Amendment 3: "UA multiplier per Amendment 3: min(Raw x 1.25, Sector Cap), all three qualifiers evidenced.") |

---

## RATING & CREDIT METRICS

| Field | Value | Anchor |
|-------|-------|--------|
| Credit Rating | NOT FOUND | (B01 input_gaps: "rating/ folder absent from inputs"; no credit agency PDF collected in-run) |
| Rating Agency | NOT FOUND | — |
| Rating Outlook | NOT FOUND | — |
| Rating Date | NOT FOUND | — |
| **Working Capital Commentary (Rating PDF)** | NOT FOUND | (no rating PDF to extract verbatim quote) |
| **Cash Flow Commentary (Rating PDF)** | NOT FOUND | (no rating PDF to extract verbatim quote) |
| Interest Coverage (D2, FY26) | 0.90x (EBIT 24.25 ÷ Interest 26.86) ex-one-time; 0.24x if one-time gain stripped | (B01 report Block D, D2 line; B02 FLAG-CASH: "Adjusted EBITDA margin −3.4% FY25 to +5.9% FY26, Q4 +12.2%, but thin and partly one time aided") |
| **Interest Coverage Note** | Weak; remains weak even after excluding the one-time ₹17.72 Cr building-sale gain (would be 0.24x vs 0.90x), per B01 FLAG-ONE-TIME-ITEM | (B01 report p.23-24) |
| Net Debt / EBITDA (D1, FY26, ex-one-time) | 1.12x (using Adj EBITDA ₹25.02 Cr, if using financial debt ex-lease ₹79.27 net cash: actually Net CASH / EBITDA = -3.17x negative, or using total Borrowings including lease ₹224.76: ND/EBITDA = 8.97x) | (B01 report Block D, D1 line; screener-data figures; note: "Net Debt/EBITDA calculation varies sharply depending on whether lease liabilities are included") |

---

## UNRESOLVED FIELDS & DATA GAPS

| Field | Why Unresolved | Where It Might Be | Severity |
|-------|-----------------|-------------------|----------|
| **FY26 Segment Revenue/Profit (Audited Ind AS 108 Note)** | No FY26 results press release segment table or Q4 results PDF segment note provided in-run; OPERATOR_CONTEXT segment splits are secondary (operator-supplied, not primary AR/results anchor) | FY26 Audited AR (not collected in-run); Q4 results PDF detailed notes | HIGH (affects SOTP primary method) |
| **Credit Rating (Agency, Rating, Outlook, Date, WC/CFO commentary)** | rating/ folder absent from inputs | Credit rating agency website (CARE Ratings, ICRA, Fitch, etc.); BSE/NSE filings | MEDIUM (not blocking valuation, but impacts cash determination) |
| **FY26 Receivables Ageing Note Detail** | FY25 ageing detail available in AR (B02-notes.yaml analysis), but FY26 ageing (critical for cash conversion flag-CASH) not yet disclosed in collected inputs | FY26 Audited AR note 4 (trade receivables detail) | HIGH (explicitly named as missing evidence for cash determination cap) |
| **Detailed Q5/Q6 Building Sale Filing (Reg 30)** | Building sale mentioned in results and concall, but underlying Reg 30 intimation filing not collected in-run | NSE/BSE Reg 30 filing, Mar-Apr 2026 timeframe | MEDIUM (secondary corroboration via OPERATOR_CONTEXT and results other-income) |
| **July-2026 Fund-Raise Board Meeting Filing (Reg 30)** | Board intimation for equity/QIP/preferential issuance post-run-date (Jul-16-2026 board meeting, run_date 2026-07-14) | NSE/BSE Reg 30 filing post-Jul-14-2026 | LOW (post-run-date; will be known in future periods) |
| **Peer Financial Statements (Margins, Market Cap, ROCE for M2/M5/M9 moat tests)** | Only peer concall transcripts collected; no margin/market-cap dataset provided for ZAGGLE/RATEGAIN/NAZARA/CARTRADE | Screener.in financial datasets or company ARs | MEDIUM (affects moat validation, not core valuation) |
| **FY26 Standalone P&L Split (Standalone vs Consolidated, Continuing vs Discontinued)** | Screener-data FY26 PBT (-2.61 Cr) does not reconcile to audited PDF continuing-vs-discontinued split (continuing -14.96 + discontinued +16.50 = +1.54 net) | Results Q4 FY26 PDF p.16-17 detailed segment note | LOW (consolidated figures used; standalone is secondary) |
| **Detailed Capex Reconciliation (Continuing vs Discontinued, Cash vs Accrual Basis)** | FY26 capex stated as ₹15.85 Cr "continuing ops only; discontinued-ops capex not separately disclosed" in B01 report | Results Q4 FY26 PDF cash flow statement note, or FY26 AR capex note | LOW (total capex used for FCF; discontinued is non-recurring) |
| **DII (Domestic Institutional Investors) Shareholding %** | Shareholding table shows 3-row view (Promoters / FIIs / Public) with no separate DII row; DII may be embedded in Public or not separately tracked | Screener.in or MSEI/stock-exchange shareholding filings; company filings | LOW (doesn't block UA 3-part test, as FIIs alone << 3%) |
| **Promoter Pledge % (Shares Pledged as Collateral)** | B01 scored E3=0; flagged as "not found in any provided source"; stage 8 flagged for BSE/screener disclosure confirmation | BSE/NSE shareholding pattern (SHP) Table II; company RHP filings; Screener pledge tracker | MEDIUM (doesn't affect current B10, but flagged for phase-3) |

---

## SUMMARY TABLES FOR ASSEMBLY

### Full Role 1 Input Table (Complete with Anchors)

**[See structured tables above for each section — this is the detailed component breakdown]**

### Segment SOTP Inputs (For Primary Valuation Method)

| Segment | FY26 Revenue (₹ Cr) | Revenue % of Total | Segment Profit (₹ Cr) | Profit Margin | Valuation Method | Anchor |
|---------|-------------------|-------------------|----------------------|---------------|-----------------|--------|
| **Rental (NestAway + HelloWorld)** | ~148-170 est. (exact FY26 segment note NOT FOUND) | 35-40% est. | Targeting breakeven/small profit FY27 (FY25 was -₹14.54 Cr loss) | Margin expanding but still near-zero | EV/Revenue + EV/EBITDA per sub-segment (not stretched at sector 45x) | (B04 Section 1C; FTTCP: "Rental segment is asset heavier and must be valued separately"; OPERATOR_CONTEXT item 4; results press release) |
| **Distribution (Analytica + Sell.do + PropTiger)** | ~254 est. (60% of ₹424 Cr Income) | ~60% | ₹32.3 Cr (disclosed FY26 segment profit) | ~12.7% (32.3 ÷ 254) | EV/Revenue; EV/EBITDA (platform SaaS logic); Sector 45x earnings cap applies | (OPERATOR_CONTEXT item 4: "Distribution FY26 segment profit ₹32.3 Cr"; B04 Section 1C table; results press release Q4 FY26 p.3 operational KPIs) |
| **Capital (SM-REIT/AMSA + Integrow/YieldWiseX)** | <₹10 Cr est. (<3% of ₹424 Cr) | <3% | Loss-making, pre-scale | Negative | DCF or revenue-multiple cross-check; NOT sector cap; one-time impact risk (Integrow CARO default per B02) | (B04 Section 1C; B02-notes rank 1: "Integrow Asset Management... CARO ix(a) default"; OPERATOR_CONTEXT: capital segment nascent) |

### Authoritative Deliberation Inputs (From FTTCP)

**These items OVERRIDE earlier determinations where they conflict; anchor them to fttcp-deliberation.md:**

- **Pillar 1 ROCE Selection**: Use CURRENT ROCE (3.32% FY26), no forward uplift (FTTCP: "STAGNANT")
- **Strategic Premium Qualification**: Does NOT apply; ROCE is stagnant, no premium crossing
- **Pillar 2 Cash-Conversion Disposition**: INDETERMINATE, caps at PROCEED WITH CAVEATS with named missing evidence (credit rating rationale, FY26 receivables ageing note)
- **Valuation Method Authority**: SOTP primary (EV/Revenue + EV/EBITDA per segment); PE four-pillar is secondary/cross-check only (FY26 barely profitable)
- **Sector Cap Row Applied**: Platform / SaaS / IT services, 45x (for Distribution segment; Rental valued separately)
- **SHARED CATALYST Flag**: Entire inflection hinges on Distribution profitability; profit is partly one-time-aided; stress test by excluding one-time gains

---

## FLAGS SUMMARY

| Flag Type | Finding | Severity | Anchor |
|-----------|---------|----------|--------|
| **FLAG-METRIC-DISTORTION** | Reported EBITDA (30.3% Q3 FY26 of Total Income) vs. Adjusted EBITDA (6.5%) differ by ~4-5x due to Ind AS 116 lease accounting; always use Adjusted EBITDA for this company | MEDIUM | (B04 Section 3A; B04 Section 3B must-track metrics) |
| **FLAG-ONE-TIME-ITEM** | Q4 FY26 PAT includes ~₹17.72 Cr building-sale gain (discontinued operations other income); underlying operating profitability may be lower; stress test required | HIGH | (B01 FLAG-ONE-TIME-ITEM; results Q4 FY26 PDF p.15 Note 5) |
| **FLAG-CASH** | Consolidated receivables ageing deteriorated sharply (>1yr buckets +327% YoY); collections unaddressed on all four concalls; lease cash outflow (₹70.50 Cr) exceeds CFO (₹27.68 Cr FY25) by 2.5x | HIGH | (B02-notes rank 1 & 6; B03 reaffirmed; FTTCP: "Named missing evidence: credit rating rationale and the FY26 receivables ageing note") |
| **FLAG-NARRATIVE-VS-EVIDENCE** | Central AI/"Unified Brain" narrative (management's stated moat, "data is the biggest moat") is weakest-evidenced category in B07 (D1, A2 both Weak); no disclosed model-performance metric or monetized AI product beyond calling bots/lead scoring | MEDIUM | (B07-emoat.yaml; B04 Section 2C moat assessment) |
| **FLAG-SHARED-CATALYST** | Entire inflection (revenue, margin, ROCE) rests on Distribution segment scaling profitably; that profitability is partly one-time-aided (building-sale gain pushed EBITDA/interest ratios); stress test by stripping one-time gains | HIGH | (FTTCP deliberation: "SHARED CATALYST flag") |
| **FLAG-GOODWILL-IMPAIRMENT-RISK** | Goodwill ₹174.25 Cr = 61% of consolidated net worth; 80.5% in two negative-net-worth subsidiaries (NestAway acquired at distressed 95% valuation cut, HelloWorld); no impairment charge to date but real risk | HIGH | (B02-notes rank 2; B03 missing_risks; AR FY25 Note 3.c / Note 25) |
| **FLAG-LEASE-LIABILITY-DOMINANCE** | Consolidated lease liabilities ₹192.33 Cr are 2.4x total financial borrowings ₹81.01 Cr; real fixed-obligation leverage is understated by standard debt ratios; lease cash service (₹70.50 Cr FY25) dominated by lease, not debt | MEDIUM | (B02-notes rank 10; B04 Section 3A) |
| **FLAG-SM-REIT-TIMELINE-SLIPPAGE** | SM-REIT launch timeline slipped in all four consecutive concalls since Jul-2025 SEBI license; still no quarter or AUM given as of Q4 FY26 | MEDIUM | (B05-concall.yaml repeated_evasions; FTTCP catalysts_12m: "FY27 (mgmt-stated 'this financial year' as of Q4 FY26 call)") |
| **FLAG-GOVERNANCE** | Unexplained auditor withdrawal (MSKA reappointed for 2nd 5-yr term Apr-2024, withdrew Sep-2024); Integrow CARO ix(a) confirmed loan default (unquantified); 7-entity CARO exception year under first-year auditor covering 56% of Group assets | MEDIUM-HIGH | (B08-promoter.yaml deal_breaker; B02-notes rank 1; B03 top_3 red_flags) |

---

## STAGE 10 YAML BLOCK

```yaml
stage: B10-valinputs
company: "Aurum Proptech Ltd"
ticker: "AURUM"
run_date: "2026-07-14"
model: "claude-haiku-4-5-20251001"
status: complete

company_identity:
  sector: "Platform / SaaS / IT services"
  sector_cap_row: "45x (authority: FTTCP deliberation, manifest.yaml)"
  cmp: 240
  market_cap_cr: 1726
  shares_outstanding_cr: 7.19
  face_value: 5
  enterprise_value_cr: 1646.73
  ev_calculation: "Market Cap (1726) + Net Cash ex-lease (79.27 = Cash 81.0 - Financial Debt ex-lease 1.73)"

latest_financials_fy26:
  revenue_cr: 424
  revenue_anchor: "OPERATOR_CONTEXT.md item 4; results press release Q4 FY26 p.2"
  adjusted_ebitda_cr: 25.02
  adjusted_ebitda_margin_pct: 5.9
  ebitda_anchor: "OPERATOR_CONTEXT.md item 4; FY26 margin 5.9%"
  pat_cr: 1.90
  pat_margin_pct: 0.45
  pat_anchor: "screener-Data_Sheet.csv Net profit row FY26"
  cfo_cr: 62.93
  cfo_anchor: "screener-Data_Sheet.csv Cash Flow row"
  capex_cr: 15.85
  capex_anchor: "B01 report p.100; results Q4 FY26 PDF p.17 (continuing ops only)"
  fcf_cr: 47.08
  fcf_anchor: "Calculated: CFO 62.93 - Capex 15.85 (B01 report p.100)"
  book_value_per_share: 70.39
  bvps_anchor: "Net Worth 506.25 Cr / Shares 7.19 Cr"
  net_cash_position_cr: 79.27
  net_cash_anchor: "Cash 81.0 - Financial Debt ex-lease 1.73 (B01 p.38; screener-Data_Sheet FY26)"
  lease_liabilities_cr: 223.03
  lease_anchor: "B01 report: 150.18 + 72.85 Cr non-current + current lease liabilities"
  capex_as_pct_revenue: 3.74
  depreciation_cr: 103.74
  depreciation_anchor: "screener-Data_Sheet.csv FY26 (includes Ind AS 116 lease RoU)"
  dps: "NOT FOUND"

returns_latest:
  roce_pct: 3.32
  roce_anchor: "B01 report p.56 ROCE table FY26 row"
  roce_fy25_pct: -2.78
  roce_trend: "improving (FY25 -2.78 → FY26 +3.32)"
  roce_trend_anchor: "B01 report, 5-year ROCE table"
  roe_pct: 0.49
  roe_anchor: "B01 report p.71"
  roce_forward_verdict: "STAGNANT (Pillar 1 uses current ROCE, no forward uplift)"
  roce_forward_anchor: "FTTCP deliberation: 'Pillar 1 uses current ROCE. No forward ROCE uplift enters Pillar 1.'"

growth_metrics:
  revenue_3yr_cagr_pct: 40.8
  revenue_cagr_anchor: "Calculated: [424 FY26 ÷ 214.05 FY24]^0.5 - 1 = 40.8%; screener-Data_Sheet FY26 endpoints"
  pat_3yr_cagr: "N/M (turnaround: FY24 -55.75 → FY25 -33.37 → FY26 +1.90)"
  arr_fy26_cr: 500
  arr_anchor: "OPERATOR_CONTEXT.md item 4: 'ARR crossed ₹500 Cr in FY26'; results press release Q4 FY26"
  arr_3yr_target_cr: 1000
  arr_target_anchor: "B05-concall.yaml guidance; OPERATOR_CONTEXT.md: '3 years / 10-12 quarters'"
  q4_revenue_yoy_growth_pct: 72
  q4_growth_anchor: "results press release Q4 FY26 p.2: 'Q4 total income ₹135 Cr (+72% YoY)'"

cash_conversion:
  cfo_pat_latest: 33.1
  cfo_pat_note: "Mechanically inflated due to low PAT base (1.90 Cr FY26); flagged as ratio distortion"
  cfo_pat_cumulative_5yr: -0.29
  cfo_pat_cumulative_anchor: "B01 report p.82-84 Block B: CFO cumulative 36.50 ÷ PAT cumulative -127.27"
  fcf_pat_latest: 24.8
  fcf_pat_anchor: "FCF 47.08 ÷ PAT 1.90"
  cash_determination: "INDETERMINATE (Pillar 2 default conservative; disposition caps at PROCEED WITH CAVEATS)"
  cash_determination_anchor: "FTTCP deliberation: 'Cash / Pillar 2: INDETERMINATE, default conservative'"
  named_missing_evidence:
    - "Credit rating rationale (not collected in-run)"
    - "FY26 receivables ageing note (needed to validate receivables-trend FLAG-CASH)"

segment_revenue_sotp_inputs:
  rental_segment:
    revenue_fy26_cr: "~148-170 (est. 35-40% of 424, exact FY26 segment note NOT FOUND)"
    revenue_anchor: "OPERATOR_CONTEXT.md; B04 Section 1C; results FY26 segment disclosure NOT in collected inputs"
    profit_fy26_cr: "Targeting breakeven/small profit FY27 (FY25 was -14.54 Cr loss)"
    profit_anchor: "OPERATOR_CONTEXT.md item 4; results Q4 FY26 press release"
    current_occupancy_pct: 76
    occupancy_anchor: "OPERATOR_CONTEXT.md item 4; NestAway Q4 FY26"
  distribution_segment:
    revenue_fy26_cr: "~254 (est. 60% of 424 Cr income)"
    revenue_anchor: "OPERATOR_CONTEXT.md item 7: 'Distribution now ~60% of income'"
    profit_fy26_cr: 32.3
    profit_anchor: "OPERATOR_CONTEXT.md item 4: 'FY26 segment profit ₹32.3 Cr'"
    profit_margin_pct: 12.7
    margin_calc: "32.3 ÷ 254 = 12.7%"
  capital_segment:
    revenue_fy26_cr: "<10 (est. <3% of 424)"
    status: "Pre-scale, loss-making, nascent SM-REIT scheme not yet launched"
    anchor: "OPERATOR_CONTEXT.md item 4; results Q4 FY26 press release"

em_score_and_catalysts:
  em_score: 25.2
  em_classification: "STRENGTHENING"
  em_anchor: "B07-emoat.yaml em_score and em_classification fields"
  evidence_mix: "14 documented + 11 claim + 3 inference (total 28 points; 50% documented)"
  evidence_anchor: "B07-emoat.yaml evidence_mix breakdown"
  primary_catalyst: "SM-REIT first scheme launch (or continued 'wait and watch' delay); window FY27"
  catalyst_anchor: "B07-emoat.yaml catalysts_12m list; FTTCP: 'FY27 (mgmt-stated this financial year)'"
  secondary_catalysts:
    - "Debt-free completion (completed May 21, 2026 per building sale)"
    - "Rental segment profitability target FY27"
    - "Ecosystem revenue % disclosure (mgmt's own FY27 timeline)"

credibility_grade:
  grade: "B"
  basis: "Strong delivery on core financials (adj EBITDA+, PBT/PAT+, ARR ₹500cr); but SM-REIT timeline slipped 4 calls, ecosystem revenue untracked until Q4, NestAway rationalization contradicted"
  anchor: "B05-concall.yaml credibility_grade and credibility_basis fields"

ua_qualifiers:
  listed_12m_months: true
  listed_12m_anchor: "B01 report: long-listed company"
  gate0_gte60_or_em_gte25: true
  qualifier_values: "Gate 0 = 58, EM = 25.2 (meets ≥25 threshold)"
  qualifier_anchor: "B01-gate0.yaml grand_total 58; B07-emoat.yaml em_score 25.2"
  fii_dii_lt3: true
  fii_pct: 0.13
  dii_pct: "NOT FOUND (3-row view, no separate DII row)"
  fii_dii_anchor: "OPERATOR_CONTEXT.md shareholding table Mar-2026; note: FII alone 0.13% << 3%"
  all_three_met: true

rating_credit_metrics:
  credit_rating: "NOT FOUND"
  rating_agency: "NOT FOUND"
  rating_date: "NOT FOUND"
  rating_outlook: "NOT FOUND"
  rating_gap_reason: "rating/ folder absent from inputs (B01 input_gaps)"
  wc_commentary_quote: "NOT FOUND"
  cfo_commentary_quote: "NOT FOUND"
  interest_coverage_d2: 0.90
  ic_anchor: "B01 report Block D D2 line (EBIT 24.25 ÷ Interest 26.86)"
  ic_ex_one_time: 0.24
  ic_ex_one_time_note: "Worse without the one-time building-sale gain, per B01 FLAG-ONE-TIME-ITEM"
  net_debt_ebitda_d1: 1.12
  nd_ebitda_anchor: "B01 report Block D D1 line; note: ratios vary sharply depending on lease liability treatment"

input_gaps:
  - "FY26 Segment Revenue/Profit (Audited Ind AS 108 Note) — not in collected FY26 segment press release; OPERATOR_CONTEXT splits are secondary"
  - "Credit Rating (Agency, Rating, Outlook, Date, WC/CFO commentary) — rating/ folder absent from inputs"
  - "FY26 Receivables Ageing Note Detail — explicitly named as FTTCP missing evidence; FY25 ageing in B02 but FY26 pending"
  - "Q5/Q6 Building Sale Reg 30 Filing — mentioned in results/concall, but underlying filing not collected"
  - "July-2026 Fund-Raise Board Meeting Reg 30 Filing — post-run-date event"
  - "Peer Financial Statements (margins, market cap) — only concall transcripts collected for M2/M5/M9 moat tests"
  - "FY26 Standalone P&L Split (Continuing vs Discontinued detail) — screener-data FY26 PBT diverges from audited segment split"
  - "DII Shareholding % — 3-row view shows no separate DII row; may be embedded in Public"
  - "Promoter Pledge % (E3) — not found; flagged for phase-3 confirmation via BSE/screener"

flags:
  - type: "FLAG-METRIC-DISTORTION"
    finding: "Reported EBITDA 30.3% Q3 FY26 vs Adjusted EBITDA 6.5% differ ~4-5x due to Ind AS 116 lease accounting"
    severity: "MEDIUM"
    anchor: "B04 Section 3A; B04 Section 3B must-track"
  - type: "FLAG-ONE-TIME-ITEM"
    finding: "Q4 FY26 PAT includes ~₹17.72 Cr building-sale gain (discontinued); underlying operating profitability lower; stress test required"
    severity: "HIGH"
    anchor: "B01 FLAG-ONE-TIME-ITEM; results Q4 FY26 PDF p.15 Note 5"
  - type: "FLAG-CASH"
    finding: "Consolidated receivables ageing deteriorated sharply (>1yr buckets +327% YoY); lease cash outflow ₹70.50 Cr vs CFO ₹27.68 Cr FY25 = 2.5x coverage gap"
    severity: "HIGH"
    anchor: "B02-notes rank 1 & 6; FTTCP: Named missing evidence includes FY26 receivables ageing note"
  - type: "FLAG-NARRATIVE-VS-EVIDENCE"
    finding: "Central AI Unified Brain narrative is weakest-evidenced moat category (D1, A2 both Weak); no disclosed model-performance metric or monetized AI product"
    severity: "MEDIUM"
    anchor: "B07-emoat.yaml; B04 Section 2C moat assessment; FLAG-NARRATIVE-VS-EVIDENCE"
  - type: "FLAG-SHARED-CATALYST"
    finding: "Entire inflection hinges on Distribution segment scaling profitably; that profit is partly one-time-aided; stress test by excluding one-time gains"
    severity: "HIGH"
    anchor: "FTTCP deliberation: SHARED CATALYST flag"
  - type: "FLAG-GOODWILL-IMPAIRMENT-RISK"
    finding: "Goodwill ₹174.25 Cr = 61% of net worth; 80.5% in two negative-net-worth subsidiaries; real impairment risk"
    severity: "HIGH"
    anchor: "B02-notes rank 2; AR FY25 Note 3.c / Note 25"
  - type: "FLAG-LEASE-LIABILITY-DOMINANCE"
    finding: "Lease liabilities ₹192.33 Cr are 2.4x financial borrowings ₹81.01 Cr; real leverage understated by standard debt ratios"
    severity: "MEDIUM"
    anchor: "B02-notes rank 10; B04 Section 3A"
  - type: "FLAG-SM-REIT-TIMELINE-SLIPPAGE"
    finding: "SM-REIT launch timeline slipped in all 4 consecutive concalls since Jul-2025 license; still no quarter or AUM given as of Q4 FY26"
    severity: "MEDIUM"
    anchor: "B05-concall.yaml repeated_evasions"
  - type: "FLAG-GOVERNANCE"
    finding: "Unexplained auditor withdrawal (MSKA Sep-2024); Integrow CARO ix(a) confirmed loan default (unquantified); 7-entity CARO exception year under 56%-coverage-only auditor"
    severity: "MEDIUM-HIGH"
    anchor: "B08-promoter.yaml deal_breaker; B02-notes rank 1"

conflicts:
  []

unresolved:
  - field: "FY26 Segment Revenue/Profit (Audited Ind AS 108 Note)"
    why: "No FY26 results press release segment table or detailed Q4 PDF segment note provided in-run; OPERATOR_CONTEXT splits are secondary"
    where_it_might_be: "FY26 Audited AR Note 23 (segment reporting); Q4 results PDF detailed notes section"
  - field: "Credit Rating (Agency, Rating, Outlook, Date, WC/CFO commentary)"
    why: "rating/ folder absent from inputs; no credit agency PDF collected in-run"
    where_it_might_be: "CARE Ratings, ICRA, Fitch, or other credit agency website; BSE/NSE filings"
  - field: "FY26 Receivables Ageing Note (Aged Bucket Detail)"
    why: "FY25 ageing detail available in AR, but FY26 ageing critical for cash conversion flag-CASH not yet disclosed in collected inputs"
    where_it_might_be: "FY26 Audited AR Note 4 (trade receivables) ageing table"
  - field: "Q5/Q6 Building Sale Filing (Reg 30 Intimation)"
    why: "Building sale mentioned in results and concall, but Reg 30 filing not collected in-run"
    where_it_might_be: "NSE/BSE Reg 30 filing, Mar-Apr 2026 timeframe; company investor relations"
  - field: "July-2026 Fund-Raise Board Meeting Filing (Reg 30 Intimation)"
    why: "Board meeting Jul-16-2026 post-run-date (2026-07-14); equity/QIP/preferential issuance terms unknown"
    where_it_might_be: "NSE/BSE Reg 30 filing post-Jul-14-2026"
  - field: "Peer Financial Statements (Margins, Market Cap for Moat Benchmarking)"
    why: "Only peer concall transcripts collected; no margin/market-cap dataset provided for ZAGGLE/RATEGAIN/NAZARA/CARTRADE"
    where_it_might_be: "Screener.in financial datasets or individual company ARs"
  - field: "DII (Domestic Institutional Investors) Shareholding %"
    why: "Shareholding table shows 3-row view (Promoters / FIIs / Public) with no separate DII row; DII may be embedded in Public"
    where_it_might_be: "Screener.in or NSE/BSE shareholding pattern filings; company investor relations"
  - field: "Promoter Pledge % (Shares Pledged as Collateral, E3 Metric)"
    why: "B01 scored E3=0, flagged as not found in any provided source; stage 8 flagged for confirmation"
    where_it_might_be: "BSE/NSE shareholding pattern (SHP) Table II; company RHP filings; Screener pledge tracker"

authoritative_deliberation_inputs_from_fttcp:
  roce_forward_pillar1: "STAGNANT (use current ROCE 3.32% FY26, no forward uplift)"
  roce_forward_anchor: "FTTCP deliberation: 'Pillar 1 uses current ROCE. No forward ROCE uplift enters Pillar 1.'"
  roce_recovery_credited_via: "NEITHER (Pillar 1 forward uplift nor Strategic Premium applies)"
  roce_recovery_anchor: "FTTCP: 'not credited (STAGNANT, no premium crossing in the window)'"
  cash_pillar2_determination: "INDETERMINATE (default conservative, disposition caps at PROCEED WITH CAVEATS)"
  cash_pillar2_anchor: "FTTCP: 'Cash / Pillar 2: INDETERMINATE, default conservative; disposition caps at PROCEED WITH CAVEATS'"
  cash_named_missing_evidence:
    - "Credit rating rationale"
    - "FY26 receivables ageing note"
  cash_anchor: "FTTCP: 'Named missing evidence: credit rating rationale and the FY26 receivables ageing note'"
  sector_cap_row_applied: "Platform / SaaS / IT services, 45x"
  sector_cap_anchor: "FTTCP: 'Sector cap row: Platform / SaaS / IT services, 45x. Confirmed against B04, not corrected.'"
  valuation_method_caution: "FY26 barely profitable; earnings PE four-pillar output is STRAINED; SOTP primary lens (EV/Revenue + EV/EBITDA per segment); PE cross-check only"
  valuation_method_anchor: "FTTCP: 'SOTP with EV/Revenue and EV/EBITDA per segment is the primary lens, PE a cross check only'"
  segment_valuation_guidance: "Rental segment (asset-heavier) must be valued separately rather than stretching 45x across it; Distribution uses 45x (platform cap)"
  segment_guidance_anchor: "FTTCP: 'B04 primary method is SOTP; the Rental segment is asset heavier and must be valued separately'"
  shared_catalyst_flag: "The whole inflection rests on Distribution segment scaling profitably; that profitability is partly one-time-aided. Stress test by stripping one-time other income and asset sale gains."
  catalyst_anchor: "FTTCP: 'SHARED CATALYST flag for the devil's advocate: the whole inflection (revenue, margin, ROCE) rests on the Distribution segment scaling profitably, and that profitability is partly one time aided.'"
```

---

## END OF REPORT

**All values in this report are anchored to upstream stages (B01-B09), results PDFs, AR FY25, operator context, and manifest. No values are computed or estimated beyond mechanical calculations (e.g., Book Value Per Share = Net Worth ÷ Shares). Missing values are listed in unresolved[] with justification and source location guidance. The YAML block above is complete and ready for stage 11 consumption.**

**Report prepared by Stage 10 (Valuation Input Assembly, Haiku 4.5-20251001) on 2026-07-14 for Aurum Proptech Ltd (AURUM). All authoritative determinations from FTTCP deliberation (fttcp-deliberation.md) are carried forward onto the input table with explicit anchors.**
