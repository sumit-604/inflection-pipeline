# B10-valinputs: Valuation Input Assembly
**Stage 10 Output | GNG Electronics Ltd (EBGNG) | Run: 2026-07-12**

---

## COMPANY IDENTITY BLOCK

| Field | Value | Source |
|---|---|---|
| Company | GNG Electronics Ltd (formerly GNG Electronics Private Limited) | manifest.yaml |
| Ticker | EBGNG | manifest.yaml |
| CMP (Rs) | 634.0 | manifest.yaml |
| Market Cap (Rs Cr) | 7,227.0 | manifest.yaml |
| Business Model Type | Asset-light, working-capital-intensive refurbishment and trading (hybrid: product sale + ancillary income, nascent leasing) | B04-bizmodel |
| Sector Cap Row | Recycling / Manufacturing, 25x | fttcp-deliberation.md (operator-confirmed, supersedes manifest "Pharma/CDMO" tag) |

### Share Count & Enterprise Value

| Field | Value | Source | Calculation |
|---|---|---|---|
| Equity Share Capital (Rs Cr) | 228.02 | Results Q4 FY26 p.10 (Standalone Balance Sheet, as at March 31, 2026) | Standalone |
| Face Value per Share (Rs) | 2 | CLAUDE.md instruction; verified in Notes to Q4 FY26 results |
| Diluted Shares Outstanding (Cr) | 11.401 | Equity share capital 228.02 M / Rs 2 face value = 114.01 million shares = 11.401 Cr shares; CMP check: 7,227 Cr / 11.401 Cr = Rs 634 | Equity share capital / face value |
| **Net Debt/(Cash)** | | |
| Cash and Cash Equivalents (Consolidated, Rs Cr) | 118.24 | Results Q4 FY26 p.18 (Consolidated Cash Flow Statement, "Cash and cash equivalents at the end of the year," Mar 31 2026) (Rs Cr; source figure Rs 1,182.38 M ÷ 10) | Consolidated FY26 |
| Total Borrowings (Consolidated, Rs Cr) | 405.75 | 19.37 (non-current) + 1,252.04 + 30.53 (current lease) + 4,038.09 (current borrowings) = 5,340.03 gross; less lease 30.53 + 217.74 = 248.27, net borrowings component. Source figure Rs 4,057.46 M ÷ 10 = Rs 405.75 Cr | Consolidated FY26 Balance Sheet p.17 |
| Surplus Cash per FTTCP (Rs Cr) | 118.24 | fttcp-deliberation.md (Pillar 1 ROCE anchor, FY26 operational ROCE calc) |
| Net Debt (Gross Debt − Cash, Rs Cr) | 287.51 | (405.75 − 118.24) | Standard calculation |
| **Enterprise Value (Rs Cr)** | **7,514.51** | 7,227.0 + 287.51 | Market cap + Net debt |

---

## LATEST PERIOD CONSOLIDATED FINANCIALS (FY26 FULL YEAR, AUDITED)

All figures below sourced from **Q4 FY26 audited annual results (May-05-2026)** unless noted. Latest period is FY26 ending March 31, 2026. Consolidated basis (parent + subsidiaries: Electronics Bazaar FZC, Bright World Technologies Inc, Kay Kay Overseas Corporation, Sun Electronics Corporation, Electronics Bazaar B.V., Electronics Bazaar Inc).

| Metric | FY26 Consolidated (Audited) | Source | Notes |
|---|---|---|---|
| **Revenue** | Rs 1,891.08 Cr | Results Q4 FY26 p.20 (Consolidated P&L, "Total income" line) (Rs Cr; source figure Rs 18,910.75 M ÷ 10) | Consolidated, year ended Mar 31 2026 |
| **EBITDA** | NOT FOUND | — | CARE rating provides PBILDT proxies (119.99 Cr FY25, 132.80 Cr 9MFY26) but full-year EBITDA not explicitly stated in results; must be estimated from CARE or reconstructed from P&L |
| **PAT (Profit After Tax)** | Rs 132.02 Cr | Results Q4 FY26 p.20 (Consolidated P&L, "Profit for the period/year") (Rs Cr; source figure Rs 1,320.16 M ÷ 10; PBT 1,477.42 M − tax 157.26 M = PAT 1,320.16 M) | Consolidated FY26 audited |
| **Diluted EPS (Rs)** | 11.58 (basic); per note, adjusted for 1:5 stock split and 500:1 bonus (Dec 2024) | Results Q4 FY26 p.20, Note 5 (EPS reclassification) | Basic and diluted shown; Note states retrospective adjustment for capital events post-period |
| **CFO (Operating Cash Flow, Rs Cr)** | (215.30) — **NEGATIVE** | Results Q4 FY26 p.19 (Consolidated Cash Flow Statement, "Net Cash flow generated from/(used in) operating activities") (Rs Cr; source figure Rs -2,153.02 M ÷ 10) | FY26 consolidated CFO negative, consistent with FLAG-CASH in B02/B03 |
| **FCF (Free Cash Flow, Rs Cr)** | (238.15) — **NEGATIVE** | CFO (215.30) + Capex (22.85) = (238.15) | Consolidated FY26 |
| **Book Value per Share (Rs)** | 66.5 | Total equity 759.33 Cr / diluted shares 11.401 Cr | Consolidated FY26 balance sheet; equity attributable to owners 757.79 Cr |
| **Net Debt (Rs Cr)** | 287.51 | 405.75 Cr (gross debt) − 118.24 Cr (cash) | Calculated as above |
| **EBITDA Margin (%)** | NOT FOUND | — | Revenue 1,891.08 Cr is known; EBITDA not stated in results PDF |
| **PAT Margin (%)** | 6.98% | 132.02 / 1,891.08 × 100 | Calculated from audited figures |
| **ROCE (Latest, FY26)** | 24.06% (cash-diluted, reported); 28.3% (operational ex-surplus-cash, deliberation override) | Reported per B01-gate0; operational per fttcp-deliberation.md, derived from EBIT 190.15 Cr, capital employed 790.40 Cr, surplus cash 118.24 Cr, yielding (190.15 / (790.40 − 118.24)) = 28.3% | FY26 consolidated; FTTCP confirms operational ROCE 28.3% is the Pillar 1 input, superseding cash-diluted 24.06% |
| **ROCE 2-Year Trend** | DEPRESSED → RECOVERING; fell from 42.0% (FY25 operational) to 28.3% (FY26 operational) | fttcp-deliberation.md; B01-gate0 discusses FY26 post-IPO equity dilution (net worth ~226 Cr to ~758 Cr) | Direction: downward FY25→FY26 due to IPO capital deployment into WC base; forward probability of recovery 40-60% per FTTCP |
| **ROE (Return on Equity)** | NOT FOUND | — | PAT 132.02 Cr / avg equity (~543.2 Cr, FY25→FY26) estimates ~24% but not verified in source docs |
| **3-Year Revenue CAGR** | 40.6% | B01-gate0 (FY2020–FY2026 consolidated) | Computed from Gate 0 data; note IPO July 2025 mid-cycle |
| **3-Year PAT CAGR** | 107.8% | B01-gate0 (FY2020–FY2026 consolidated) | Driven by margin expansion and scale |
| **CFO/PAT (Latest, FY26)** | (1.63) | (215.30) / 132.02 | Consolidated; negative CFO makes this negative |
| **CFO/PAT (Cumulative, FY2020–FY2026)** | (0.93) | B01-gate0 (cumulative CFO / cumulative PAT across 7-year track record) | Gate 0 Block B score 0/20 triggered by this figure; impacts deal-breaker verdict |
| **FCF/PAT (Latest, FY26)** | (1.80) | (238.15) / 132.02 | Calculated; negative FCF |
| **P/FCF** | NOT FOUND | — | FCF negative; ratio undefined / not meaningful |
| **Capex (Rs Cr)** | (22.85) | Results Q4 FY26 p.19 (Consolidated Cash Flow Statement, "Purchase of property, plant and equipment, intangible assets including Capital work in progress") (Rs Cr; source figure Rs -228.50 M ÷ 10) | FY26 consolidated |
| **Depreciation & Amortization (Rs Cr)** | 10.35 | Results Q4 FY26 p.18 (Consolidated Cash Flow Statement, "Depreciation and amortisation" under Operating Activities adjustments) (Rs Cr; source figure Rs 103.52 M ÷ 10) | FY26 consolidated |
| **DPS (Dividend per Share)** | NOT FOUND | — | No dividend policy or history disclosed to date (post-IPO Jul 2025); not yet relevant |

---

## EARLIER COMPARABLE PERIOD (FY25 FULL YEAR, AUDITED)

| Metric | FY25 Consolidated (Audited) | Source |
|---|---|---|
| Revenue | Rs 141.11 Cr | Results Q4 FY26 p.20, 9M comparative column (extracted from FY25 audited annual) (Rs Cr; source figure Rs 1,411.10 M ÷ 10) |
| PAT | Rs 69.03 Cr | Results Q4 FY26 p.20, 9M comparative (Rs Cr; source figure Rs 690.33 M ÷ 10) |
| CFO | (133.84) Cr | Results Q4 FY26 p.19, Cash Flow Statement comparative (Rs Cr; source figure Rs -1,338.41 M ÷ 10) |
| Net Debt | NOT FOUND | — |

---

## FROM BLOCKS B01–B09

### Guidance, Delivery Track Record & Management Credibility (B05)

| Item | Guided | Actual/Outcome | Grade | Source |
|---|---|---|---|---|
| FY26 Revenue Growth | 20–25% (Q2), revised 28–30% (Q3) | 34% YoY | **Beat** | B05-concall |
| FY26 EBITDA Margin Expansion | +75bps (Q2), revised +150–200bps (Q3) | +166–209bps (EBITDA margin, PAT margin) | **Beat** | B05-concall |
| H2 FY26 Interest Cost Savings | ~Rs 10–12 Cr | Missed; Q3 finance cost ~4–4.5 Cr higher than estimated; Q4 run-rate ~14.5 Cr/quarter | **Missed** | B05-concall, promise_delivery row 3 |
| Debtor Days Stability | 30–35 days foreseeable future (Q2) | Risen to ~40–45 days by Q4 FY26 | **Slipped** | B05-concall, promise_delivery row 4 |
| Capacity Build-out | ≥120k units/month (Q2); scale guidance asset-light | Delivered: 150k units/month (Q4); UAE 3→8 facilities, headcount 1,194→2,148 | **Delivered** | B05-concall |
| FY27 Guidance | 25% revenue, +50bps PAT margin | Issued Q4 FY26; notably conservative vs FY26 sandbagging pattern | **Issued, conservative** | B05-concall |
| **Credibility Grade** | — | **B (Good)** | Management beat both original and revised FY26 guidance; missed two quantified promises (interest savings, debtor days) with transparent explanation; FY27 guidance reset conservatively (sandbagging pattern). | B05-concall (credibility_grade: B, credibility_basis) |

### Growth Triggers & Catalyst Window (B05, B07)

| Priority | Trigger | Type | Timeframe | Conviction | Confirm Signal | Kill Signal | Source |
|---|---|---|---|---|---|---|---|
| 1 | Memory/component price supercycle sustaining refurb-PC demand + ASP/margin expansion | Sectoral/Price-Mix | Near-medium term (~2028 per mgmt) | **High** | Continued ASP growth, IDC declines holding, gross margin ≥19% | Memory/component price normalization faster than guided; margin reversion to 15–17% | B05-triggers |
| 2 | Distributor channel expansion (Ingram, Supertron, Europe/US advanced stage) | Volume | Medium term | **Medium** | Named-distributor revenue becomes material % of sales (currently minuscule) | Contribution stays negligible 2+ qtrs or partnerships lapse | B05-triggers |
| 3 | Capacity/geographic expansion (150k units/month, 46 countries) | Volume | Near term | **High** | Continued country/touchpoint growth, utilization rising toward stated ceiling | Expansion stalls, utilization falls, headcount growth reverses | B05-triggers |
| 4 | FY27 guidance beat potential | Volume/Price-Mix | Near term (FY27) | **Medium-High** | Q1 FY27 beats guided 25%, consistent with FY26 sandbagging | Growth decelerates toward/below 25% guided | B05-triggers |
| 5 | Consumer financing/EMI retail push + India domestic consumption growth (80% YoY FY26) | Volume | Near-medium term | **Low-Medium** | EMI-channel volume becomes disclosed and material | Negligible EMI uptake or credit-quality issues emerge | B05-triggers |
| 6 | Working-capital/inventory strategy payoff (elevated Rs 743 Cr inventory position) | Cost | Near term | **Medium** | Margin expansion continues while debt/finance cost stabilizes/declines | Memory prices reverse suddenly, triggering write-down or forced destocking | B05-triggers |

**12-Month Catalysts (B07):**
- FY27 guidance delivery (25% revenue growth, +50bps PAT margin) — management claim, 12m window
- Ingram Micro / Supertron distributor revenue becoming quantifiable (currently minuscule) — 12–18m
- Debtor days reverting toward 30–35 day guided range from current 40–45 — documented, 6–12m
- US and Europe distributor discussions (advanced stage) converting to signed agreements — 6–12m

**Shared Macro Catalyst Flag:** Memory and component price supercycle underlies revenue, margin and the Rs 743 Cr inventory bet at once; single macro point of failure for Role 3. (fttcp-deliberation.md, final section)

### Emerging Moat Analysis (B07)

| Metric | Value | Source | Notes |
|---|---|---|---|
| EM Score | 23.0 / 100 | B07-emoat | Modest classification |
| EM Classification | **MODEST** | B07-emoat | Qualified depth; active categories below |
| Active Moat Categories (6 documented) | B2 (Qualification lock-in, strong), C2 (Customer concentration improving, strong), H3 (ESG moat, strong), R1 (Regulatory/policy tailwinds, strong), F2 (Execution moat, moderate), H1 (Industry consolidation beneficiary, moderate) | B07-emoat (completionist_recount) | Excludes Ingram/Supertron partnerships (pre-revenue, routed to optionality register) |
| Evidence Mix | Documented: 15; Claim: 9; Inference: 5 | B07-emoat (evidence_mix) | Mixed-quality evidence base |
| **Combined Assessment** | **AVERAGE** | B07-emoat (combined_assessment) | Gate 0 AVERAGE backward score meets MODEST forward emerging-moat score; certification/customer/procurement diversification real but largely shared with compliant competitors; cash conversion deteriorating exactly where transition thesis needs improvement |
| **Top Moat Risks** | (1) WC deterioration narrows balance-sheet capacity for distributor/EU pushes; (2) Ingram/Supertron pre-revenue-scale, no committed contracts; (3) Certifications attainable by any compliant competitor; (4) Capacity build running ahead of demand (utilization slack); (5) Component/memory price supercycle is macro tailwind, not company-specific, could normalize | B07-emoat | Listed as threats to moat durability |

### Cash Conversion & Working Capital Determination (B01, B02, FTTCP)

| Aspect | Finding | Source | Impact |
|---|---|---|---|
| **Cash Conversion Verdict** | **INDETERMINATE** (not overridden) | fttcp-deliberation.md | Caps disposition at PROCEED WITH CAVEATS; resolving evidence is the first post-IPO statutory cash flow statement; live monitorable, not a multiple reducer |
| **CFO Status** | Negative FY26 (Rs -215.30 Cr consolidated), negative FY25 (Rs -133.84 Cr), CARE states negative since FY20 | B02-notes, FLAG-CASH; Results Q4 FY26 Cash Flow Statement | Structural working-capital dependency on short-term loan rollover, not organic cash generation |
| **WC Days (Block B Trend)** | Deteriorating: 136.4 days (FY25) → 178.1 days (FY26), +41.7 days | B01-gate0 (block_b_trend); Results Q4 FY26 p.17 Consolidated Balance Sheet | CARE operating cycle 93 days (FY24) → 122 days (FY25), expected to stay >150 days medium-term |
| **Working Capital Loan Classification** | **RED FLAG**: WCL draws classified as operating working-capital adjustment in Cash Flow Statement, not financing activity | B02-notes, B03-ardeep (FLAG-CASH, Rank 1 finding); Results Q4 FY26 p.19 Cash Flow Statement raw p.249 | FY24 WCL inflow Rs 207.06 Cr exceeds reported cash generated from operations Rs 102.48 Cr itself; FY22 net CFO negative Rs -3.83 Cr |
| **DSCR (Debt Service Coverage Ratio)** | Never exceeded 1.0x in any of 4 periods (0.43→0.40→0.25→0.12 FY22→H1FY25) | B03-ardeep; Note 46 results (raw p.300) | Deteriorating trajectory; negative forward indicator for WC stability |
| **Receivables Trend** | Deteriorating: gross receivables Rs 42.18 Cr (FY22) → Rs 180.18 Cr (H1FY25); 100% <6-month bucket, zero ECL allowance despite lifetime-ECL policy | B02-notes (receivables_trend); Note 10 pp.262–263, Note 46 p.296 | Debtor days worsened FY22→FY23 (~28.7→36.9 days), partially recovered FY24 (~33.4 days), lengthened into H1FY25 (~44.7 days half-year) |
| **Accounting Quality Score** | 3 / 10 | B02-notes (accounting_quality) | Flags: WCL classification as operating CF, zero ECL despite policy, no warranty provision, note-drafting arithmetic errors, tax-reconciliation inconsistencies, unaudited UAE subsidiary (~78% of PAT), related-party entanglement |
| **CARE Rating WC Commentary (Verbatim, Agency + Page)** | "Working capital intensive nature of business: GEL's business remains working capital intensive owing to requirements of sizeable stocking of both old and refurbished laptops, which leads to high inventory holding. The company primarily sources used laptops in bulk from corporates and other distributors with quick payment requirements, which is then refurbished and stocked as finished goods before being sold through its distribution partnerships. While the payment terms with suppliers and customers are short, the sizeable inventory holding requirements translated into increase in average operating cycle to 122 days in FY25 (PY: 93 days)...Working capital intensity is also reflected in negative cash flow from operations since FY20 and GEL's improved yet moderate average utilisation of fund-based working capital (cash credit) lines in the last 12 months ended February 2026. GEL's ability to maintain liquidity cushion and acceptable level of inventory and receivables remain key monitorable." | Rating PDF (202604130446_GNG_Electronics_Limited.pdf, p.2, Key Weaknesses section) | WC monitorables: operating cycle trend, cash flow from operations, WCL utilization |

### Promoter Assessment & Governance (B08)

| Finding | Status | Source |
|---|---|---|
| **Promoter Verdict** | **CAUTION** | B08-promoter, fttcp-deliberation.md |
| **Credibility Grade** | **B (Good)** — see B05 above | B05-concall |
| **Pledge Status** | 0% current, stable at 0% per DRHP (as of 2025-03-25); no post-listing pledge creation found | B08-promoter (pledge_pct_latest, pledge_trend) |
| **KKOC (Promoter Firm) Multi-Role RPT** | Registered-office landlord + trading counterparty + Cholamandalam facility security provider; no arm's-length benchmark disclosed | B08-promoter (adverse_findings rank 4) |
| **KKOC Pending Tax Demand** | Rs 305.32 M aggregate (Rs 255.31 M direct tax AY23–24 + Rs 27.39 M GST, balance ~Rs 41.8 M unitemised) | B08-promoter, DRHP raw p.334 |
| **Board/Finance KMP Tenure** | Entire board and both finance KMPs (CFO, CS) appointed within 6 weeks pre-DRHP; stable through one full post-listing fiscal year (FY26) | B08-promoter (adverse_findings rank 8) |
| **UAE Subsidiary Audit Scope** | Electronics Bazaar FZC generates ~78% of FY24 consolidated PAT; never audited by principal Indian auditor in any period; 3 different local auditors used across 4 periods | B08-promoter (adverse_findings rank 7); B02-notes (red_flags rank 7) |
| **Institutional Entry & Credit Upgrade** | Goldman Sachs, Motilal Oswal, Mirae Asset, ITI, Edelweiss, Trust, MCP Emerging Markets, Mobius investment entered ~3.94% block (~Rs 175 Cr, Jun 2026); CARE upgraded BBB-/Positive (pre-IPO) to BBB/Stable (Apr 2026) | B08-promoter (transition_evidence) |

### EM Score and Classification (B07)

- **Score:** 23.0 (MODEST classification; AVERAGE combined with AVERAGE Gate 0 backward score)
- **Active Moat Categories:** 6 categories at Strong/Moderate strength (B2, C2, H3, R1, F2, H1)
- **Evidence Quality:** Mostly documented, with claim and inference components
- **Forward Catalysts:** FY27 guidance delivery, distributor tie-ups, debtor days reversion, US/Europe expansion

### Sector Multiples & Peer Comparables (B06, B09)

| Metric | GNG FY26 | Peer 1 (Redington) | Peer 2 (RPTECH) | Peer 3 (CNL) | Source | Notes |
|---|---|---|---|---|---|---|
| Revenue Growth (YoY) | 34% | ~2–5% | ~8–15% | ~5% | B06-peers, B05-concall, peer concalls | GNG significantly outpacing peers; driven by memory/component supercycle + distributor expansion |
| Gross Margin (%) | 12.31% (FY24) | 32–47% (estimated across segments) | 30–38% | 27–30% | B04-bizmodel, peer commentary | GNG trails all peers despite superior scale/growth; FLAG-MARGIN in B04 |
| Debtor Days | 40–45 (Q4 FY26, drifted from 30–35 promised) | ~35–45 range (estimated) | 46–47 (improved from 61 in earlier period) | ~51–58 days | B05-concall, B06-peers | RPTECH improved; GNG deteriorated; CNL stable-elevated |
| Memory/Component Price Corroboration | DDR5 8GB $23.35→~$120, 1TB SSD $70→$249 (Oct 2025–Apr 2026) | Confirmed component shortage, 20% ESG price hike | Confirmed RAM 2–3x increase, notebook +20–30% | Confirmed cost inflation | B06-peers (peer_coverage_map, verified claim rank 1) | Substantive peer corroboration for GNG's primary growth driver |
| IDC PC Shipment Decline 2026 | Cites 55–60mn unit demand gap, -11% forecast | Cited -5–10% CY26 dip | Cited 5–10% dip | Referenced | B05-concall, B06-peers | Peer support for GNG's refurb-demand thesis |
| **Peer Medians if Provided** | NOT FOUND in stage 1 inputs | — | — | — | — | Peer financial CSVs exist for stage 6; not provided to B10 assembly stage |

### SOM-Implied Growth & TAM (B09)

| Metric | Value | Source | Notes |
|---|---|---|---|
| **TAM (Conservative)** | Rs 1,252,452 Cr | B09-tam (tam_cr.conservative) | Refurbished/certified ICT devices (laptops, desktops, tablets, servers, smartphones) in India + USA/UAE/Europe export organized channels |
| **TAM (Realistic)** | Rs 1,320,660 Cr | B09-tam (tam_cr.realistic) | Higher estimate accounting for channel mix uncertainty |
| **SAM (Serviceable Addressable Market)** | Rs 149,900 Cr | B09-tam (sam_cr) | GNG's addressable market within TAM |
| **SAM % of TAM** | 12.0% | B09-tam (sam_pct_of_tam) | Penetration available to GNG |
| **SOM 3-Year (Rs Cr)** | Rs 4,734 Cr | B09-tam (som_3yr_cr) | GNG projected 3-year serviceable obtainable market |
| **SOM 5-Year (Rs Cr)** | Rs 11,154 Cr | B09-tam (som_5yr_cr) | 5-year SOM |
| **SOM-Implied Revenue CAGR (3-Year)** | 35.7% | B09-tam (som_implied_revenue_cagr.yr3) | Mechanical extrapolation of SOM |
| **SOM-Implied Revenue CAGR (5-Year)** | 42.5% | B09-tam (som_implied_revenue_cagr.yr5) | 5-year equivalent CAGR |
| **Current SAM Share (%)** | 1.26% | B09-tam (current_sam_share_pct) | GNG's FY26 revenue (~Rs 1.9 Cr) as % of SAM |
| **Revenue Headroom (x)** | 79.1x | B09-tam (revenue_headroom_x) | Multiple of addressable market available to GNG |
| **Runway Classification** | **MASSIVE** | B09-tam (runway_class) | SOM extends well beyond committed capex capacity |
| **Management TAM Claim** | Rs 1,804,380 Cr | B09-tam (mgmt_claim_cr) | Company's stated TAM (IPO presentation) |
| **Claim Reasonableness Ratio** | 1.44x realistic | B09-tam (mgmt_claim_ratio) | Management claim 1.44x the conservative/realistic estimate; read as "reasonable" |
| **Data Stale Flags** | Global refurb+used PC ($34.06B/$57.4B, CY23/28), premium smartphone ($109.9B/$193.7B, CY23/28), India refurb-PC (11%/32%, FY24/29 organized), USA/Europe PC/smartphone (CY23/28), India PC penetration (75–95/1,000, filing-vintage) | B09-tam (stale_data_flags) | Primary research from 1Lattice, DRHP; no post-run-date refresh performed |

---

## CASH FLOW QUALITY & STRUCTURAL ASSESSMENT

### Operating Cycle Trajectory

- **FY25 Consolidated:** 93 days (per CARE rating FY24 baseline)
- **FY25 to FY26 Trajectory:** 122 days (CARE FY25), expected to stay >150 days medium-term
- **WC Days Gate 0 Computed (Consolidated):** 136.4 days (FY25) → 178.1 days (FY26)
- **Trend:** Deteriorating; FLAG-CASH in B02/B03

### Structural vs. Growth-Induced Cash Determination

Per B01 (block_b_trend), B02 (FLAG-CASH, rank 1 finding), CARE rating commentary (p.2, Key Weaknesses), and fttcp-deliberation.md: **INDETERMINATE**. 

Evidence summary:
- **Structural indicators:** WCL classification in operating CF statement, not financing (masks true CFO); 81.9% of group debt current/short-tenor across 20+ fragmented lenders (Note 19.1, results Q4 FY26 p.274 raw); DSCR never >1.0x in any period
- **Growth-induced indicators:** Receivable/inventory days lengthened with revenue expansion; distributor credit terms extended (debtor days 30–35 → 40–45)
- **Both elements present:** Cannot isolate dominant driver without post-IPO full statutory cash flow statement (resolving evidence per FTTCP)
- **Outcome:** INDETERMINATE caps disposition at PROCEED WITH CAVEATS

---

## RATING EXTRACT

| Attribute | Value | Source |
|---|---|---|
| Agency | CARE Ratings Limited (CAREEdge Ratings) | Rating PDF header (202604130446_GNG_Electronics_Limited.pdf) |
| Rating (Long-term) | **CARE BBB; Stable** | Rating PDF p.1 (Facilities table) |
| Previous Rating (Long-term) | CARE BBB-; Positive (pre-IPO) | Rating PDF p.1 (Rating Action: Upgraded from CARE BBB-; Positive) |
| Rating (Short-term) | **CARE A3+** | Rating PDF p.1; upgraded from CARE A3 (Jan 2025) |
| Outlook | **Stable** | Rating PDF p.2 (Outlook section) |
| Rating Date | April 08, 2026 | Rating PDF header |
| **Rating WC Quote (Verbatim)** | "Working capital intensive nature of business: GEL's business remains working capital intensive owing to requirements of sizeable stocking of both old and refurbished laptops, which leads to high inventory holding. The company primarily sources used laptops in bulk from corporates and other distributors with quick payment requirements, which is then refurbished and stocked as finished goods before being sold through its distribution partnerships. While the payment terms with suppliers and customers are short, the sizeable inventory holding requirements translated into increase in average operating cycle to 122 days in FY25 (PY: 93 days)...Working capital intensity is also reflected in negative cash flow from operations since FY20 and GEL's improved yet moderate average utilisation of fund-based working capital (cash credit) lines in the last 12 months ended February 2026. GEL's ability to maintain liquidity cushion and acceptable level of inventory and receivables remain key monitorable." | Rating PDF p.2, Key Weaknesses section |

---

## FTTCP-AFFIRMED INPUTS (PHASE 3 HANDOFF, AUTHORITATIVE FOR B10)

The following inputs are sourced from fttcp-deliberation.md (authoritative Phase 3 handoff to Stage 11 valuation):

| Input | Value | Basis | Override? |
|---|---|---|---|
| **ROCE Forward Verdict** | **RECOVERING**, 40–60% probability (12m) | Operator refinement of FTTCP analysis; draft "Temporarily Depressed" refined given IPO dilution explanation | Yes (Override 1: Pillar 1 operational ROCE anchor) |
| **Pillar 1 ROCE Input** | **Operational ex-surplus-cash ROCE ~28.3% (FY26)**; base ~21.5x; recovery credited via Pillar 1; Strategic Premium ROCE re-rating barred | FY26 EBIT 190.15 Cr / (capital employed 790.40 Cr − surplus cash 118.24 Cr) = 28.3%; reported ROCE (cash-diluted) 24.06% used for Gate 0 but superseded for valuation | Yes (Override 1) |
| **Cash Conversion Determination** | **INDETERMINATE**; caps disposition at PROCEED WITH CAVEATS; resolving evidence is the first statutory cash flow statement; live monitorable, not a multiple reducer | Cumulative CFO/PAT -0.93, CFO negative FY25/FY26, CARE records CFO negative since FY20, WCL draws in operating activities; no post-IPO audit separation of structural vs growth-induced | Not overridden; stands as INDETERMINATE |
| **Destination / Exit PE** | **20x** (operator override, growth-duration rationale); below the 25x sector cap | Operator ruling: "take the destination price-to-earnings as 20 because the growth duration is large...penetration is not a scope, so more duration for the growth can be given." | Yes (Override 2: supersedes mechanical additive stack ~16x) |
| **Exit PE Basis** | **Forward basis: 20x on FY30 EPS at FY29 exit** (recorded at finalize, 2026-07-13) | Operator ruling: "for EXIT in FY29, take the EPS earnings of FY30" — raises exit value relative to trailing-at-exit convention, consistent with forward-PE preference | Yes (Override 4) |
| **Sector Cap Row** | **Recycling / Manufacturing, 25x** (operator-confirmed) | Operator ruling: "sector will be Recycling and Manufacturing only"; manifest tag "Pharma/CDMO" 38x is a collector error, discarded | Yes (Override 3; supersedes manifest) |
| **Business Type** | Standard operating business, asset-light, working-capital-intensive refurbisher and trader, not a lender; four standard transitions | Standard business classification | Not overridden |
| **Promoter Verdict** | **CAUTION** | KKOC multi-role RPT entanglement + Rs 305.32 M pending tax demand; offset by institutional entry, CARE upgrade, zero pledge | From fttcp-deliberation.md handoff table |
| **Shared Catalyst Flag** | Memory and component price supercycle underlies revenue, margin, and Rs 743 Cr inventory bet; single macro point of failure for Role 3 | Macro risk requiring downstream sensitivity | Flagged for monitoring; does not reduce exit multiple per FTTCP |

---

## UA QUALIFIER CHECK (12-MONTH LISTING ELIGIBILITY)

Per CLAUDE.md Amendment 3: Listed ≥12 months? Gate 0 ≥60 OR EM ≥25? FII+DII <3%?

| Qualifier | Requirement | GNG Status | Source | Met? |
|---|---|---|---|---|
| **Listed ≥12 months** | Must be listed ≥12 months as of run date | IPO July 30, 2025; run date 2026-07-12 = 347 days, <12 months | Manifest, DRHP, listing exchange filings | **NO** (347 days) |
| **Gate 0 ≥60 OR EM ≥25** | Core score ≥60 (GOOD) OR EM score ≥25 (STRONG) | Gate 0 core 48 (AVERAGE, <60); EM 23 (MODEST, <25) | B01-gate0 (core_score: 48); B07-emoat (em_score: 23.0) | **NO** (both fail) |
| **FII + DII <3%** | Institutional ownership <3% | FII + DII ~3.94% (as of Jun 2026, post-IPO entry Goldman Sachs, Motilal Oswal, etc.; ~Rs 175 Cr / ~Rs 7,227 Cr mcap = ~2.4% but aggregated reporting shows 3.94%) | B08-promoter (transition_evidence, institutional investor entry ~3.94% block) | **NO** (3.94% >3%) |
| **All Three Met** | All three must be true | 0 of 3 met | — | **NO** |

**UA Verdict: all_met = false**

---

## CONFLICTS & UNRESOLVED FIELDS

### Conflicts Between Upstream Sources

| Field | Value_A | Anchor_A | Value_B | Anchor_B | Used | Reason |
|---|---|---|---|---|---|---|
| Sector Cap Row | "Pharma / CDMO" 38x | manifest.yaml | "Recycling / Manufacturing" 25x | fttcp-deliberation.md (operator override) | Recycling / Mfg 25x | FTTCP deliberation is authoritative Phase 3 handoff; manifest tag flagged as collector defect in task instructions |
| FY26 ROCE (Pillar 1 Input) | 24.06% (cash-diluted, reported) | B01-gate0, results Q4 FY26 | 28.3% (operational ex-surplus-cash) | fttcp-deliberation.md (Override 1) | 28.3% (operational) | Deliberation confirms operational ROCE is Pillar 1 anchor; cash-diluted superseded for valuation |

### Unresolved Fields (Not Found; For Stage 11 & Downstream Stages)

| Field | Why Unresolved | Where It Might Be | Source/Notes |
|---|---|---|---|
| **EBITDA (FY26)** | Results PDF provides revenue, PAT, CFO; EBITDA not explicitly stated. CARE rating provides PBILDT proxies (119.99 Cr FY25, 132.80 Cr 9MFY26) but full-year EBITDA not in source PDFs | Stage 11 to reconstruct from P&L or use CARE PBILDT as proxy | Results Q4 FY26 P&L does not separate EBITDA line |
| **FY27–FY30 EPS Projections** | Not available in sources; stage 10 is assembly only, not forecasting | Stage 11 DCF model to project forward earnings | B05 guidance gives FY27 (25% revenue, +50bps PAT margin) but no EPS $ figure |
| **Peer Financial Data (P/E, EV/EBITDA, P/B, Growth, ROCE medians)** | Stage 6 peer analysis used concall/secondary data; financial CSV data not provided to B10 | Stage 6 detailed peer financials (RedSeer, RPTECH, CNL balance sheets) | B06-peers notes "Peer financial data provided to stage 6/verifier D" but not to B10 assembly |
| **Current-Status ROE** | PAT 132.02 Cr / avg equity (~543.2 Cr FY25→FY26) estimates ~24% but not verified in source docs | Compute from latest balance sheet or ask for management guidance | Results Q4 FY26 standalone ROE can be computed but consolidated ROE requires audited equity track record |
| **Detailed Capex Pipeline (Committed, Multi-Year)** | FY26 capex (22.85 Cr) stated; no forward capex guidance disclosed in concalls or results | Stage 11 to cross-check capacity utilization trend against capex needs | B05-concall (Capacity/geographic expansion trigger) gives ≥120k→150k units/month achieved but no forward capex schedule |
| **Foreign Exchange Exposure & Hedge Ratio** | No formal FX hedging policy despite 75.65% of H1FY25 revenue from outside India | Materialized FX loss/gain typically <0.3% of revenue (B04-bizmodel note) but no quantified current hedge position | B04-bizmodel flags "no formal FX hedge policy despite 75pct export revenue" as risk |
| **Debt Schedule & Tenor Mix (Post-IPO Current)** | Note 19.1 shows 81.9% current/short-tenor (Rs 408.62 Cr of Rs 498.97 Cr at H1FY25); post-IPO deleveraging via ~Rs 3,200 M equity proceeds (July 2025), but current debt tenor mix post-deleveraging not available | Stage 11 or investor relations for updated debt schedule as of Jun 2026 | Results Q4 FY26 (May 2026) show only stand-alone/consolidated totals; detailed tenor schedule (H1FY25) in Note 19.1 raw p.274 but post-IPO restatement unclear |
| **Optionality Register (Conversion Timelines for Ingram/Supertron, EU Hub, Device-as-a-Service, Right to Repair)** | B07-emoat routes 4 optionality items; none yet converted to scored moat (pre-revenue or uncertain gate timing) | B07-emoat optionality_register; stage 11 to weight as upside/downside scenarios | B07 explicitly excludes these from active moat count; scenarios for downstream sensitivity |

---

## INPUT GAPS CARRIED FORWARD

From B01-B09 input_gaps arrays, consolidated:
1. **presentation_absent** — No Q4 FY26 earnings call presentation deck in provided inputs (transcript used, slides unavailable)
2. **annual_report_is_drhp** — Company's "annual report" is the DRHP (IPO document, March 2025); no post-IPO statutory annual report issued yet (FY26 full annual report due Aug/Sep 2026)
3. **sector_cap_mismatch** — Manifest tag "Pharma/CDMO" inconsistent with actual business (refurbishment/trading); RESOLVED to Recycling/Manufacturing per operator deliberation
4. **concalls_4_available_3_used** — Q2, Q3, Q4 FY26 concalls reviewed; Q1 FY26 (Jul 2025, post-IPO listing) not located in provided inputs
5. **quarterly_product_geo_mix_not_disclosed_post_drhp** — Segment data (product/geography breakdown) in DRHP but not refreshed in post-IPO quarterly disclosures (B04-bizmodel input gap)
6. **tablets_servers_submarket_not_sized** — B09 TAM sizing focuses on laptops + smartphones; desktops, tablets, servers, workstations unsized (likely understates TAM)
7. **uae_organized_share_not_found** — UAM organized refurb market share proxied, not sourced (B09 input gap)

---

## FLAGS & MONITORABLES SUMMARY

**Flags Propagated to Disposition:**
- **FLAG-CASH (Critical):** Working capital deterioration, negative CFO FY25/FY26, WCL classification in operating CF, DSCR <1.0x all periods. Caps verdict at PROCEED WITH CAVEATS per FTTCP.
- **FLAG-PROMOTER (Medium):** KKOC multi-role RPT, Rs 305.32 M pending tax demand. Verdict CAUTION per B08; offset by institutional entry and credit upgrade.
- **FLAG-MARGIN (Medium):** Gross margin 12% trails all three named peers (27–47%). FLAG-MARGIN in B04.
- **FLAG-GATE0 (Medium):** Core score 48/100 (AVERAGE). Block B 0/20 (CFO/PAT cumulative -0.93, WC days deterioration). Blocks C/D strong but Block B deal-breaker.
- **Shared Macro Catalyst Flag:** Memory/component supercycle single point of failure for margin and inventory thesis.

**Monitorables (Stage 11 & Downstream):**
1. DSCR move toward/above 1.0x or below 0.12x (first post-listing statutory annual report)
2. WCL cash-flow classification reclassification to financing (full SA 700 audit)
3. Electronics Bazaar FZC audit assignment (principal Indian auditor assumes direct responsibility)
4. Note-drafting QC errors remediated (Note 45/36 corrections in FY27 annual)
5. Contingent liabilities growth beyond Rs 109.04 M (GST ITC disputes)
6. Undisclosed top customer (17.28% FY24 revenue) identity/continuity disclosed
7. Debtor days revert toward 30–35 day guided range
8. Ingram/Supertron revenue becomes quantifiable (currently "minuscule")
9. FY27 revenue growth achieves ≥25% guidance or decelerates toward/below

---

## SUMMARY TABLE: ALL ANCHORED VALUES

| Category | Field | Value | Anchor |
|---|---|---|---|
| **Identity** | Company | GNG Electronics Ltd | manifest.yaml |
| | Ticker | EBGNG | manifest.yaml |
| | Sector Cap | Recycling / Manufacturing, 25x | fttcp-deliberation.md |
| | CMP | Rs 634 | manifest.yaml |
| | Market Cap | Rs 7,227 Cr | manifest.yaml |
| **Capital Structure** | Diluted Shares (Cr) | 11.401 | Equity capital 228.02 M / Rs 2 face value = 114.01M shares = 11.401 Cr |
| | Enterprise Value | Rs 7,514.51 Cr | Market cap 7,227 + Net debt 287.51 |
| **FY26 Financials (Consolidated)** | Revenue | Rs 1,891.08 Cr | Results Q4 FY26 p.20 (Rs Cr; source Rs 18,910.75 M ÷ 10) |
| | PAT | Rs 132.02 Cr | Results Q4 FY26 p.20 (Rs Cr; source Rs 1,320.16 M ÷ 10) |
| | CFO | Rs (215.30) Cr | Results Q4 FY26 p.19 (Rs Cr; source Rs -2,153.02 M ÷ 10) |
| | Book Value/Share | Rs 66.5 | Total equity 759.33 Cr / 11.401 Cr shares |
| | PAT Margin | 6.98% | 132.02 / 1,891.08 |
| | ROCE (Operational, ex-surplus-cash) | 28.3% | fttcp-deliberation.md, operational ROCE calc |
| | Capex | Rs (22.85) Cr | Results Q4 FY26 p.19 (Rs Cr; source Rs -228.50 M ÷ 10) |
| **Governance** | Credibility Grade | B (Good) | B05-concall (credibility_grade) |
| | Promoter Verdict | CAUTION | fttcp-deliberation.md, B08-promoter |
| | Pledge % | 0% | B08-promoter |
| **Valuation Inputs (FTTCP)** | Pillar 1 ROCE | 28.3% (operational) | fttcp-deliberation.md (Override 1) |
| | Exit PE | 20x (forward basis: FY30 EPS at FY29 exit) | fttcp-deliberation.md (Overrides 2 & 4) |
| | Cash Conversion | INDETERMINATE | fttcp-deliberation.md |
| | ROCE Forward Verdict | RECOVERING (40–60% probability) | fttcp-deliberation.md |
| **Catalysts & Growth** | Primary Trigger (12m) | Memory/component supercycle + FY27 guidance delivery | B05-concall, B07-emoat |
| | EM Score | 23.0 (MODEST) | B07-emoat |
| | SOM 3yr | Rs 4,734 Cr | B09-tam |
| | Revenue CAGR Implied (3yr) | 35.7% | B09-tam |
| **Rating** | Agency | CARE Ratings | Rating PDF header |
| | Long-Term Rating | CARE BBB; Stable | Rating PDF p.1 |
| | Short-Term Rating | CARE A3+ | Rating PDF p.1 |

---

**Report Status:** Complete. All values carry explicit source anchors. Unresolved fields listed separately with justification. FTTCP deliberation-confirmed inputs carry "fttcp-deliberation.md" anchor throughout. Conflicts resolved per precedence rules (FTTCP Phase 3 > upstream blocks > manifest). Input gaps tracked and carried forward. Unit corrections applied: all financial figures in Rs Crore (Rs Million ÷ 10). Ready for Stage 11 (valuation model) ingestion.
