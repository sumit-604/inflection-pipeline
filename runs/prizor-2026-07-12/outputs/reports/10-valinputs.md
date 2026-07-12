# STAGE 10: VALUATION INPUT ASSEMBLY
# Prizor Viztech Ltd (PRIZOR)
Run date: 2026-07-12 | Model: claude-haiku-4-5 | Emits: B10-valinputs

---

## COMPLETE ROLE 1 VALUATION INPUT TABLE

### Company Identity Block

| Field | Value | Source Anchor |
|---|---|---|
| Company | Prizor Viztech Ltd | (manifest) |
| Ticker | PRIZOR | (manifest) |
| Sector (corrected) | Video Surveillance / Security Electronics | (B04, B01; manifest tag "Pharma/CDMO" rejected per FTTCP deliberation) |
| Business Model Type | Hybrid (trading + manufacturing) | (B04) |
| Sector Cap Row (authoritative) | Manufacturing / Industrial products, 25x | (FTTCP deliberation; manifest "Pharma/CDMO 38x" rejected as collection defect) |
| CMP (Rs) | 825 | (manifest) |
| Market Cap (Rs Cr) | 891 | (manifest) |
| Shares Outstanding (Cr, diluted) | 1.069 | (task message) |
| Net Debt (Rs Cr, FY25 basis) | 7.389 | (computed: Total borrowings 7.52 Cr - Cash 0.131 Cr, AR p.71, B01) |
| Enterprise Value (Rs Cr) | 898.389 | (computed: Market cap 891 + Net debt 7.389) |

---

### Latest Audited Financials (FY25: Year ended 31-Mar-2025)

| Field | Value | Source Anchor |
|---|---|---|
| Revenue (Rs Cr) | 70.98 | (Data_Sheet.csv; AR p.72) |
| EBITDA (Rs Cr) | 15.077 | (computed: EBIT 14.910 + Depreciation 0.166, AR p.72; B01) |
| PAT (Rs Cr) | 10.15 | (Data_Sheet.csv; AR p.72) |
| EBITDA Margin (%) | 21.42 | (computed: 15.077 / 70.98; B01) |
| PAT Margin (%) | 14.29 | (computed: 10.15 / 70.98) |
| Diluted EPS (Rs) | 9.495 | (computed: PAT 10.15 Cr / Shares 1.069 Cr; B01) |
| CFO (Rs Cr) | -14.10 | (Data_Sheet.csv; AR p.73, Cash Flow Statement) |
| Capex (Rs Cr) | 8.276 | (AR p.73, CF Statement; B01) |
| FCF (Rs Cr) | -22.371 | (computed: CFO -14.095 - Capex 8.276; B01) |
| Depreciation (Rs Cr) | 0.166 | (AR p.72; B01) |
| Book Value Per Share (Rs) | 40.07 | (computed: Shareholders' Funds 42.829 Cr / Shares 1.069 Cr; AR p.71, B01) |
| Net Debt or Net Cash (Rs Cr) | Net Debt 7.389 | (Total borrowings 7.52 Cr - Cash & equivalents 0.131 Cr; AR p.71; B01) |
| ROCE (Latest, FY25 %) | 31.29 | (AR Note 32; FTTCP deliberation: STAGNANT forward verdict; FY26 ROCE unaudited and internally inconsistent, must not be used) |
| ROCE 2-Year Trend Direction | Declining (69.82% FY24 → 31.29% FY25) | (B01, AR p.71/72; note: decline is base-effect, FY24 pre-IPO thin-equity base per B01 data_notes; FY25 more structurally meaningful) |
| ROE (Latest, FY25 %) | 41.02 | (computed: PAT 10.15 Cr / avg NW 24.749 Cr; B01) |
| CFO / PAT (Latest, FY25 ratio) | -1.39x | (computed: CFO -14.10 / PAT 10.15; B01, B02) |
| CFO / PAT (Cumulative, FY24-FY25 ratio) | -1.02x | (computed: Cumulative CFO -15.915 / Cumulative PAT 15.673; B01, FTTCP deliberation: INDETERMINATE cash conversion, leaning structural) |
| FCF / PAT (Latest, FY25 ratio) | -2.20x | (computed: FCF -22.371 / PAT 10.15; B01) |
| P / FCF | NOT FOUND | (Cannot compute with negative FCF; noted in B09) |
| DPS (Rs) | 0 (nil) | (B05: dividend policy is nil, profits retained for business) |

---

### 3-Year Growth Metrics (Limited Dataset)

| Field | Value | Source Anchor |
|---|---|---|
| 3-Year Revenue CAGR (%) | NOT FOUND | (Only 2 years of audited data available, FY24-FY25; SME IPO with no FY23 or earlier balance sheet; B01 input_gaps notes "history <3 years") |
| 3-Year PAT CAGR (%) | NOT FOUND | (Same data limitation; only 2 years available) |
| 1-Year (FY24-FY25) Revenue Growth (%) | 99.07 | (computed: (70.98 / 35.65) - 1; B01) |
| 1-Year (FY24-FY25) PAT Growth (%) | 83.88 | (computed: (10.15 / 5.52) - 1; B01) |

---

### Management Credibility & Guidance

| Field | Value | Source Anchor |
|---|---|---|
| Credibility Grade (A/B/C/D) | C | (B05: NO-CONCALL MODE rule — AR FY24-25 gave no quantified guidance to test against FY26 delivery, so no positive delivery evidence exists; strong reported growth offset by unexplained FY25 CFO shortfall, generic MD&A, internal ROCE/ROE inconsistency in company's own FY26 presentation) |
| Guidance: Revenue (FY26, Rs Cr) | NOT FOUND | (AR MD&A Outlook p.53-58 contains no quantified guidance; B05) |
| Guidance: EBITDA Margin (%) | NOT FOUND | (Same, no guidance in AR; B05) |
| Guidance: Timeline/Quarter Stated | NOT FOUND | (No guidance provided in document) |
| Top Trigger #1 (name, type, timeframe) | STQC/BIS-ER policy tailwind vs non-certified imports / Regulatory-Policy / near-term, ongoing | (B05, B09: April 2024 mandate enforced April 2026; domestic organised brands now >80% share, up from ~two-thirds; import-substitution event already substantially realised) |
| Top Trigger #2 (name, type, timeframe) | Dealer network scale-up (11,000+ dealers, 21 states, 3,000+ tehsils) / Volume / near-medium term | (B05, B07: dealer count 5,200 (FY24) → 11,000+ (FY26); self-reported, unaudited operational metric) |
| Top Trigger #3 (name, type, timeframe) | Backward integration (SMT/PCB in-house, margin durability) / Cost / near-medium term | (B05: conviction Low-Medium; B07, B04: 50 lakh PCB units/annum, 16 lakh camera assembly capacity installed FY26; capex-embedded growth 116% of FY26 revenue, debt-funded) |

---

### Emerging Moat Assessment

| Field | Value | Source Anchor |
|---|---|---|
| EM Score (0-80) | 13.6 | (B07: MODEST classification; only 2 categories at Strong level [B1 backward integration, R1 regulatory tailwind], insufficient breadth for HIGH POTENTIAL) |
| EM Classification | MODEST | (B07) |
| Combined Backward + Forward Assessment | AVERAGE | (B07: Gate 0 AVERAGE + EM MODEST = AVERAGE combined; "two genuinely strong verified categories not backed by broad enough or audited enough base to elevate to HIGH POTENTIAL") |
| Primary Evidence Mix (summary) | Mostly documented (18 documented, 7 claim, 4 inference) | (B07) |
| Strategic Moats Present (yes-with-description or no) | YES — Distribution network (11,000+ dealers, 21 states, 9 years built), Regulatory/licensing (BIS-ER/STQC, policy-dependent, category-wide), Cost advantage from backward integration (Gandhinagar SMT/assembly, unproven at scale), Brand (Prizor, low-medium durability) | (B04, B07) |
| Primary Catalyst (12-month window) | FY26 statutory Annual Report with audited capex/segment/utilisation detail; CFO turning positive (tests cash-conversion flag); IndieSemic MoU progression to signed agreement | (B07) |
| Catalyst Proximity Window (months) | 12 months | (B07) |

---

### Cash Conversion & Working Capital Assessment

| Field | Value | Source Anchor |
|---|---|---|
| Structural vs Growth-Induced Cash Determination | INDETERMINATE, leaning structural | (FTTCP deliberation, B01, B02: three years broken [CFO/PAT -33%, -139%, +0.01% FY24-26 unaudited], FY26 did not recover despite PAT tripling, audited FY26 cash flow and receivables ageing do not exist) |
| Evidence for Cash Determination | Cumulative CFO/PAT -1.02x both years, revenue growth +99% vs CFO +0%, finished-goods inventory +281.7% YoY vs revenue +99.4% YoY, inventory turnover fell 4.19x to 3.32x, trade payables squeezed (payable days 59.96 → 13.57), cash burn funded entirely by IPO proceeds (CFO negative both years; Financing Activities +Rs 22.64 Cr FY25) | (B01, B02, AR Note 16 p.83, Note 32 p.89, Cash Flow Statement p.73) |
| Rating Agency WC / Cash Commentary (quote + page) | NOT FOUND | (Rating PDF not available; B00 input gap notes "rating/ folder ABSENT"; FTTCP deliberation: "Named missing evidence: the credit rating working capital rationale and the full FY26 audited cash flow plus receivables ageing") |
| Working Capital Days (Latest, FY25) | 213.93 | (computed: Receivable Days 80.93 + Inventory Days 146.57 - Payable Days 13.57; B01, AR p.71-72, Note 9 p.76) |
| WC Days Trend (FY24 → FY25) | Deteriorating, +46.3 days (167.67 → 213.93) | (B01, B02) |
| Receivables Ageing (quality/trend) | Improving composition (95% <6mo FY25 vs 99% in 6mo-1yr bucket FY24), but days roughly flat at ~81 days FY25 vs 81.5 FY24 | (B02, AR Note 17 p.82) |
| Inventory Ageing / FIFO turnover (if disclosed) | Inventory turnover fell 4.19x (FY24) to 3.32x (FY25); finished-goods build +281.7% YoY against revenue +99.4% YoY | (B02, B01, AR Note 16 p.83, Note 32 p.89) |
| Payables Quality / Payment Stretch | Trade payables fell sharply (Rs 5.855 Cr → Rs 2.638 Cr, -54.9%) despite revenue doubling; payable days compressed 59.96 → 13.57 days (supplier-relationship squeeze) | (B01, B02, AR Note 9 p.76) |
| Cash Multiplier Flag & Disposition Impact | INDETERMINATE caps disposition at PROCEED WITH CAVEATS (per CLAUDE.md never-halt rule and FTTCP verdict); no SOTP carve-out (not a BOO/annuity model) | (FTTCP deliberation, CLAUDE.md) |

---

### Unresolved Authoritative Valuations (FTTCP)

| Field | Value | Source Anchor |
|---|---|---|
| ROCE Forward Verdict (authoritative for Pillar 1) | STAGNANT. Pillar 1 uses current audited ROCE = FY25 31.29% (AR Note 32). FY26 ROCE is unaudited and internally inconsistent (deck 37.2% vs 47.4%) and MUST NOT be used until audited. ROCE recovery credited via: NOT credited. | (FTTCP deliberation, AR Note 32, B04) |
| Sector Cap (authoritative for multiples) | Manufacturing / Industrial products, 25x | (FTTCP deliberation; manifest Pharma/CDMO 38x is REJECTED as collection defect) |
| Confidence Overlay | NO-CONCALL MODE and phase 1 confidence delta 62, forward confidence materially reduced | (FTTCP deliberation) |

---

### Valuation Methodology & Comparable Metrics

| Field | Value | Source Anchor |
|---|---|---|
| Primary Valuation Method | EV/EBITDA | (B04: "Normalizes across the large FY24-FY25 leverage/equity swing and the trading-to-manufacturing cost-structure transition") |
| Secondary Valuation Method | EV/Sales | (B04: "Cross-check for a still-scaling, still-transitioning hardware business where EBITDA margin mix is unsettled") |
| Tertiary Valuation Method | P/E | (B04: "Sanity-check only; earnings base not comparable across the transition and only ~2 years of listed history") |
| Peer Median P/E (if available) | NOT FOUND | (B06: Only CP Plus available as direct CCTV peer; no consistent P/E table disclosed; B06 flagged CP Plus comparability across all quarters; D-Link India has screening CSVs but no concall) |
| Peer Median EV/EBITDA (if available) | NOT FOUND | (B06: CP Plus Q4 FY26 EBITDA 18.0% best quarter (one-off), FY26 full year 13.7%, FY27 guidance 14-15%; Prizor claims 21-23% EBITDA, contradicted as "exceeds category-leading peer in every quarter examined" per B06 Q5 finding) |
| Peer Median P/B (if available) | NOT FOUND | (Not provided in B06 peer coverage) |
| Peer Median Revenue Growth (if available) | NOT FOUND | (B06 flagged demand as "strong but decelerating," CP Plus cut FY27 volume growth from >20% to 15-20%) |
| Peer Median ROCE (if available) | NOT FOUND | (B06 does not break out peer ROCE separately; focus on margins and cash-flow quality) |

---

### TAM / SAM / SOM & Market Assessment

| Field | Value | Source Anchor |
|---|---|---|
| TAM (conservative, Rs Cr, FY26 basis) | 12,370 | (B09 Method 1: Frost & Sullivan ₹10,620 Cr FY25 × 1.1646 CAGR = 12,368 Cr, corroborated by Prizor's own domestic chart at ~14.4% CAGR; confidence HIGH) |
| TAM (realistic, Rs Cr, FY26 basis) | 17,425 | (B09 Method 3: CP Plus-implied market = ₹14,962 Cr FY25 × 1.1646 = 17,425 Cr; confidence MEDIUM; note: 41% higher than Method 1 reflects vintage/scope difference, not silently averaged) |
| SAM (Rs Cr, FY26 basis) | 3,580 | (B09: conservative TAM 12,370 × SAM filters [product 90% × geography 72% × channel 70% × customer 75% × capability 85% = 28.9%] = 3,577 Cr ≈ 3,580 Cr) |
| SAM as % of TAM | 28.9% | (B09) |
| Current SAM Share (%) | 4.13 | (B09: FY26 revenue 148 Cr [unaudited, investor presentation] / SAM 3,580 Cr) |
| SOM 3-Year (Rs Cr) | 237 | (B09: current share 4.13% + share gain 2.5pp = 6.63% → SOM = 3,580 × 6.63%) |
| SOM 5-Year (Rs Cr) | 309 | (B09: current share 4.13% + share gain 4.5pp cumulative = 8.63% → SOM = 3,580 × 8.63%) |
| SOM-Implied Revenue CAGR (3-year) | 17.0% | (B09: computed (237 / 148)^(1/3) - 1) |
| SOM-Implied Revenue CAGR (5-year) | 15.9% | (B09: computed (309 / 148)^(1/5) - 1) |
| Revenue Headroom (SAM / Current Revenue, x) | 24.2 | (B09: 3,580 Cr / 148 Cr unaudited FY26) |
| Runway Classification | MASSIVE | (B09: 20+ years to saturate SAM at 17% CAGR; capacity surplus — installed 16 lakh unit capacity ceiling ~₹4,320 Cr vs SOM_5yr CCTV requirement ~₹238 Cr, ~5.5% utilisation; capex plan is optimistic side, not SOM) |
| TAM Growth % (CAGR to FY30) | 16.46 | (B09, B06: Frost & Sullivan via CP Plus; corroborated by Prizor's own chart ~14.4%; midpoint 15-16%) |

---

### UA (Undervalued Ancillary) Qualifiers (per CLAUDE.md Amendment 3)

| Qualifier | Result | Evidence | Source Anchor |
|---|---|---|---|
| Listed ≥12 months | ✓ YES | IPO completed July 2024; run date 2026-07-12 = ~21 months | (manifest, B08, B00) |
| Gate 0 ≥60 OR EM ≥25 | ✓ YES (on Gate0) | Gate 0 core score 63/100 (≥60); EM score 13.6 (<25) → qualified via Gate0 | (B01, B07) |
| FII + DII shareholding <3% | ✗ NOT FOUND | Shareholding pattern aggregator sites returned HTTP 403; only Promoter/Public two-line split available in AR | (B03 input gap, B08: "shareholding-pattern/pledge filings not retrieved (403)"; AR p.93) |
| **All three qualifiers met** | **Qualified (2 of 3 confirmed)** | Listed ≥12 months confirmed; Gate0 ≥60 confirmed; FII/DII unresolved | (as above) |
| **UA Multiplier Application** | min(Raw × 1.25, Sector Cap 25x) | All three must be evidenced for UA multiplier; FII/DII unresolved means conservative application or exclusion per stage 11 discretion | (CLAUDE.md Amendment 3) |

---

## CONFLICTS[]

No conflicts detected. All upstream stage determinations are consistent and internally reconciled via FTTCP deliberation (operator-accepted draft, no changes).

---

## UNRESOLVED[] (Fields No Source Could Fill)

| Field | Why Unresolved | Where It Might Be |
|---|---|---|
| FY26 Revenue (audited) | FY26 Annual Report not yet published (as of 2026-07-12); only unaudited investor presentation figures exist (₹148 Cr disclosed) | FY26 AR P&L, expected disclosure Jul-Aug 2026 |
| FY26 PAT (audited) | Same; only investor presentation figure (₹20.76 Cr unaudited) available | FY26 AR P&L |
| FY26 ROCE (audited) | FY26 ROCE unaudited and internally inconsistent (deck 37.2% vs 47.4%); MUST NOT be used per FTTCP deliberation until audited | FY26 AR Note 32 (expected) |
| FY26 CFO (audited) | Only unaudited investor presentation figure (₹0.29 Cr) available | FY26 AR Cash Flow Statement |
| FY26 Receivables Ageing (detail) | Only investor presentation aggregate (₹38.63 Cr) given; no age-bucket breakdown | FY26 AR Note 17 (expected) |
| Rating Agency (name, rating, outlook, date) | Credit rating PDF not provided; B00 input gap notes "rating/ folder ABSENT" | Separate rating/ PDF folder (if available post-run) |
| Rating WC / Cash Flow Commentary (quote) | No rating exists in provided documents | Credit rating document working-capital section (if published) |
| 3-Year Revenue CAGR | Only 2 years of audited history available (FY24-FY25); SME IPO with no FY23 or earlier balance sheet | FY26 AR (and any subsequent audited filings) |
| 3-Year PAT CAGR | Same data constraint | FY26 AR (and any subsequent audited filings) |
| Capex: FY26 detail (itemised by project) | FY26 capex shown as aggregate investing outflow (₹40.86 Cr); break-up by project (SMT line, assembly, IndieSemic, etc.) not itemised | FY26 AR Note 12 (PPE), Note 19 (Capital commitments, currently absent) |
| IndieSemic SoC: capex quantum and timeline | MoU stage, "In Pipeline" with no binding agreement date or capex commitment | FY26 AR MD&A or subsequent exchange filings (if deal progresses) |
| Facility Utilisation % (SMT line, assembly lines) | 16 lakh camera assembly capacity disclosed; current utilisation NOT FOUND | FY26 AR capacity/segment notes or subsequent investor calls (if concalls resume) |
| Peer P/E, EV/EBITDA, P/B, ROCE medians | Only CP Plus available as direct peer; other peers (OSEL, Sahasra) are diversified, not pure CCTV | B06 peer reports; additional peer concalls if available post-run |
| Current EPS (FY26, TTM, adjusted) | Only unaudited investor presentation PAT (₹20.76 Cr) available; no TTM EPS calculated | FY26 AR P&L; Q4 FY26 results PDF (not provided) |
| P/FCF (current) | Cannot compute with negative FCF (FY25 FCF -₹22.371 Cr); likely to remain negative until CFO structure resolves | FY26 AR Cash Flow Statement (when audited) |
| FII + DII shareholding % | Blocked access to aggregator sites and exchange filings; only Promoter/Public split in AR | SEBI shareholding-pattern portal, exchange PVL filings (HTTP 403 access denied this session) |
| Promoter Pledge % (current) | AR contains no SEBI-format shareholding table with encumbrance column; no zero-pledge confirmation independently fetched | SEBI shareholding-pattern portal, NSE letters PVL/038/2025-26, PVL/022/2026-27 (HTTP 403 blocked) |

---

## INPUT_GAPS[] (Carried Forward from B00, B01)

1. **Results/ PDFs (quarterly & annual)**: ABSENT. Gate 0 and stage 10 run from screener Data_Sheet (FY24-FY25 only) + AR + investor presentation. No quarterly results extracts available; latest-period audited fields marked unresolved.

2. **Rating/ PDF**: ABSENT. No credit rating available; rating_wc_quote unresolved; stage 11 Pillar 2 defaults conservative; FLAG-CASH rating rationale quote will be NOT FOUND.

3. **Screener CSVs (P&L, BS, CF, Quarters)**: EMPTY TEMPLATES (collect_to_repo v3 defect, also seen in TATVA, KARNIKA). Only Data_Sheet.csv carries values (2 years, FY24-FY25).

4. **Manifest sector tag defect**: "Pharma / CDMO" is WRONG for a video-surveillance / security-electronics maker. Correct Section 1B row is Manufacturing / Industrial products, 25x (per FTTCP deliberation). Recurring collect_to_repo defect.

5. **Data history constraint**: Only 2 years available (FY24-FY25); SME IPO with no pre-listing balance sheets. 3-year CAGRs, trend tests, and forward-confidence metrics mechanically capped.

6. **Concall transcripts**: ABSENT (no-concall mode triggered). Management credibility grade defaults to C; guidance completeness and delivery track record unscoreable on transcripts.

7. **FII/DII shareholding**: NOT FOUND (access to aggregator sites and NSE filing portals blocked via HTTP 403).

---

## FLAGS[]

1. **FLAG-CASH (from B02, FTTCP deliberation)**: Operating cash flow negative both FY24 (-₹1.82 Cr) and FY25 (-₹14.10 Cr) despite PAT growth (₹5.52 Cr → ₹10.15 Cr); cash conversion -139% (FY25), -33% (FY24). Driven by finished-goods inventory +281.7% YoY vs revenue +99.4% YoY and trade-payables squeeze. Entirely IPO-funded, not organic. **Disposition capped at PROCEED WITH CAVEATS.**

2. **FLAG-INVENTORY (from B02)**: Finished-goods inventory +281.7% YoY (₹14.27 Cr → ₹54.42 Cr) vs revenue +99.4% YoY under delivery-triggered revenue-recognition policy; inventory turnover fell 4.19x to 3.32x. Raises sell-in vs sell-through question; risk of future write-down if build does not convert.

3. **FLAG-RPT-UNRECONCILED (from B02, B03)**: ₹3.00 Cr loan-to-equity conversion (Note 3, 07-May-2024, 4,00,000 shares at ₹75) cannot be traced to any director, KMP, or named related party across three independent cross-checks. Highest-priority open governance item.

4. **FLAG-RELATED-PARTY-REVENUE (from B02, B03)**: Related-party revenue (Om Security Solutions) was 9.95% of FY24 revenue (₹3.55 Cr) and fell to zero in FY25 (the IPO year), unexplained. Pre-IPO related-party revenue reliance vanishing exactly at listing.

5. **FLAG-DISCLOSURE-QUALITY (from B03)**: MD&A risk/industry sections generic and business-irrelevant (AI, cross-border data flows for a CCTV-hardware trading company); CSR self-contradiction (Board's Report 'not applicable' vs Note 51 ₹5.50L spent); inverted Section 197(12) remuneration-to-median ratio (0.12x disclosed vs 8.63x correct).

6. **FLAG-FORWARD-ROCE-DILUTION (from B07, B09)**: Capacity ceiling (installed 16 lakh units → ₹4,320 Cr revenue at Method 2 ASP) vastly exceeds SOM_5yr requirement (₹238 Cr CCTV segment, ~5.5% utilisation). Capex plan debt-funded against negative cumulative CFO; ROCE (currently 47.4%) likely to compress mechanically as fixed-asset base grows into under-utilised plant.

7. **FLAG-MARGIN-PEER-CONTRADICTED (from B06)**: Prizor's claimed 21-23% EBITDA / 14% PAT for CCTV hardware assembly exceeds the category-leading, most-scaled direct peer (CP Plus) in every quarter examined (CP Plus: 8.7%-18.0% EBITDA, 4.4%-11.9% PAT, with FY26 full year 13.7% / 8.72% and FY27 guidance 14-15% called "the new normal"). Priority item for synthesis stage 11 to reconcile claimed vs peer-verified margins.

8. **FLAG-INTERNAL-ROCE-INCONSISTENCY (from B04, B05)**: Internal ROCE/ROE inconsistency within the same Apr-2026 investor presentation (cover slide vs detailed ratio chart): slide 5 states 47.4% ROCE / 38.0% ROE for FY26, while slide 29 chart shows 37.2% ROCE / 35.5% ROE for FY26. FY26 figures are unaudited; FTTCP verdict: must not be used until audited.

---

```yaml
stage: B10-valinputs
company: "PRIZOR"
run_date: "2026-07-12"
model: claude-haiku-4-5
status: complete
input_gaps:
  - "Results/ PDFs (quarterly & annual) ABSENT — no latest-period results beyond investor presentation"
  - "Rating/ PDF ABSENT — credit rating, rating agency WC/cash commentary unresolved"
  - "Screener P&L/BS/CF/Quarters CSVs EMPTY (collect_to_repo defect) — only Data_Sheet.csv populated"
  - "FY26 (audited) revenue, PAT, ROCE, CFO, receivables ageing — all unaudited (investor presentation) or NOT FOUND"
  - "3-year revenue/PAT CAGRs NOT FOUND — only 2 years history (SME IPO, no pre-FY24 balance sheet)"
  - "Concall transcripts ABSENT — no-concall mode; credibility grade defaults to C; guidance completeness unscoreable"
  - "FII/DII shareholding NOT FOUND — access to aggregator sites blocked (HTTP 403)"
  - "Peer P/E, EV/EBITDA, P/B, ROCE medians — only CP Plus available as direct CCTV peer; others diversified"
  - "Capex: FY26 itemised by project NOT FOUND; IndieSemic SoC capex and timeline NOT FOUND"
  - "Facility utilisation % (SMT, assembly lines) NOT FOUND"
flags:
  - {type: FLAG-CASH, severity: HIGH, reason: "Operating cash flow negative both years and deteriorating (FY25 CFO -₹14.10 Cr vs PAT +₹10.15 Cr, conversion -139%; FY24 CFO -₹1.82 Cr vs PAT +₹5.52 Cr, -33%), driven by inventory +281.7% YoY vs revenue +99.4% YoY and trade-payables squeeze; entirely IPO-funded. INDETERMINATE determination caps disposition at PROCEED WITH CAVEATS."}
  - {type: FLAG-INVENTORY, severity: MEDIUM-HIGH, reason: "Finished-goods inventory +281.7% YoY vs revenue +99.4% YoY; inventory turnover fell 4.19x to 3.32x under delivery-triggered revenue policy; raises sell-in vs sell-through concern and write-down risk if build does not convert."}
  - {type: FLAG-RPT-UNRECONCILED, severity: HIGH, reason: "₹3.00 Cr loan-to-equity conversion (07-May-2024, 4,00,000 shares at ₹75) unreconciled to any named lender; identity, relationship, original loan terms entirely undisclosed — governance and disclosure gap."}
  - {type: FLAG-RELATED-PARTY-REVENUE, severity: MEDIUM, reason: "Related-party revenue (Om Security Solutions) was 9.95% of FY24 revenue (₹3.55 Cr) and fell to zero in FY25 (IPO year), unexplained; pre-IPO revenue reliance vanished exactly at listing."}
  - {type: FLAG-DISCLOSURE-QUALITY, severity: MEDIUM, reason: "MD&A generic and business-irrelevant; CSR self-contradiction; inverted remuneration ratio; undisclosed post-balance-sheet promoter remuneration hike (~150%, approved 01-Jul-2025)."}
  - {type: FLAG-FORWARD-ROCE-DILUTION, severity: MEDIUM, reason: "Installed capacity (16 lakh units, scalable to 40 lakh) vastly exceeds SOM_5yr requirement (~₹238 Cr, ~5.5% utilisation); capex debt-funded against negative cumulative CFO; ROCE (47.4% FY26 unaudited) likely to compress mechanically as fixed-asset base grows into under-utilised plant."}
  - {type: FLAG-MARGIN-PEER-CONTRADICTED, severity: MEDIUM, reason: "Prizor's claimed 21-23% EBITDA / 14% PAT for CCTV hardware assembly exceeds category-leading direct peer CP Plus in every quarter examined (CP Plus: 13.7% EBITDA / 8.72% PAT FY26 full year, FY27 guidance 14-15% 'new normal'). Priority item for stage 11 reconciliation."}
  - {type: FLAG-INTERNAL-ROCE-INCONSISTENCY, severity: MEDIUM, reason: "ROCE/ROE inconsistency within same Apr-2026 investor presentation (47.4% / 38.0% cover slide vs 37.2% / 35.5% chart for FY26); FY26 unaudited, must not be used until audited."}
  - {type: FLAG-GATE0-DEAL-BREAKER, severity: MEDIUM, reason: "Classification AVERAGE (cumulative CFO/PAT -1.02x, history <3 years, Block B score 0/20); flags propagate forward for scrutiny rather than halting pipeline."}
table:
  company_identity:
    company: "Prizor Viztech Ltd"
    ticker: "PRIZOR"
    sector_corrected: "Video Surveillance / Security Electronics"
    business_model: "Hybrid (trading + manufacturing)"
    sector_cap_row: "Manufacturing / Industrial products, 25x"
    cmp_rs: 825
    market_cap_cr: 891
    shares_outstanding_cr: 1.069
    net_debt_cr: 7.389
    enterprise_value_cr: 898.389
  latest_audited_financials_fy25:
    revenue_cr: 70.98
    ebitda_cr: 15.077
    pat_cr: 10.15
    ebitda_margin_pct: 21.42
    pat_margin_pct: 14.29
    diluted_eps_rs: 9.495
    cfo_cr: -14.10
    capex_cr: 8.276
    fcf_cr: -22.371
    depreciation_cr: 0.166
    book_value_per_share_rs: 40.07
    net_debt_or_net_cash: "Net Debt 7.389 Cr"
    roce_latest_pct: 31.29
    roce_2yr_trend: "Declining (69.82% FY24 → 31.29% FY25, base-effect)"
    roe_latest_pct: 41.02
    cfo_pat_latest_ratio: -1.39x
    cfo_pat_cumulative_ratio: -1.02x
    fcf_pat_ratio: -2.20x
    p_fcf: "NOT FOUND (negative FCF)"
    dps_rs: 0
  growth_metrics_limited:
    revenue_3yr_cagr_pct: "NOT FOUND (2 years history only)"
    pat_3yr_cagr_pct: "NOT FOUND (2 years history only)"
    revenue_1yr_growth_pct: 99.07
    pat_1yr_growth_pct: 83.88
  management_credibility_guidance:
    credibility_grade: "C"
    guidance_revenue_fy26_cr: "NOT FOUND"
    guidance_ebitda_margin_pct: "NOT FOUND"
    guidance_timeline: "NOT FOUND"
    top_trigger_1: "STQC/BIS-ER policy tailwind, Regulatory-Policy, near-term ongoing"
    top_trigger_2: "Dealer network scale-up (11,000+), Volume, near-medium term"
    top_trigger_3: "Backward integration (SMT/PCB margin durability), Cost, near-medium term"
  emerging_moat:
    em_score: 13.6
    em_classification: "MODEST"
    combined_backward_forward: "AVERAGE"
    evidence_mix: "Mostly documented (18 documented, 7 claim, 4 inference)"
    moats_present: "YES — Distribution (11,000+ dealers, 21 states, 9 years), Regulatory/licensing (BIS-ER/STQC, policy-dependent, category-wide), Cost advantage (backward integration, unproven at scale), Brand (Prizor, low-medium durability)"
    primary_catalyst: "FY26 statutory AR with audited capex/segment/utilisation; CFO positive test; IndieSemic MoU progression"
    catalyst_proximity_months: 12
  cash_conversion_wc:
    determination: "INDETERMINATE, leaning structural"
    evidence: "Cumulative CFO/PAT -1.02x, inventory +281.7% vs revenue +99.4%, payables squeezed (59.96 → 13.57 days), entire cash burn IPO-funded"
    rating_wc_quote: "NOT FOUND"
    wc_days_latest_fy25: 213.93
    wc_days_trend: "Deteriorating +46.3 days (167.67 → 213.93)"
    receivables_aging: "Improving composition (95% <6mo), days flat at ~81"
    inventory_turnover: "Fell 4.19x → 3.32x, FG build +281.7% YoY"
    payables_quality: "Squeezed sharply, payable days 59.96 → 13.57"
    cash_multiplier_disposition: "INDETERMINATE caps at PROCEED WITH CAVEATS; no SOTP carve-out"
  fttcp_authoritative:
    roce_forward_verdict: "STAGNANT — use FY25 audited 31.29%; FY26 unaudited internally inconsistent, must not use until audited; ROCE recovery NOT credited"
    sector_cap_authoritative: "Manufacturing / Industrial products, 25x (manifest Pharma/CDMO 38x REJECTED)"
    confidence_overlay: "NO-CONCALL MODE, phase 1 confidence delta 62, forward confidence materially reduced"
  valuation_methodology:
    primary_method: "EV/EBITDA"
    secondary_method: "EV/Sales"
    tertiary_method: "P/E (sanity-check only)"
    peer_median_pe: "NOT FOUND"
    peer_median_ev_ebitda: "NOT FOUND"
    peer_median_pb: "NOT FOUND"
    peer_median_growth_pct: "NOT FOUND"
    peer_median_roce_pct: "NOT FOUND"
  tam_sam_som:
    tam_conservative_cr: 12370
    tam_realistic_cr: 17425
    sam_cr: 3580
    sam_pct_of_tam: 28.9
    current_sam_share_pct: 4.13
    som_3yr_cr: 237
    som_5yr_cr: 309
    som_implied_revenue_cagr_3yr: 17.0
    som_implied_revenue_cagr_5yr: 15.9
    revenue_headroom_x: 24.2
    runway_classification: "MASSIVE"
    tam_growth_cagr_pct: 16.46
  ua_qualifiers:
    listed_12m: "YES (IPO July 2024, ~21 months at run date)"
    gate0_or_em: "YES on Gate0 (core 63 ≥60); EM 13.6 <25"
    fii_dii_lt3: "NOT FOUND (aggregator access blocked)"
    all_met: "Qualified (2 of 3 confirmed; FII/DII unresolved)"
  credibility_grade: "C"

conflicts: []

unresolved:
  - {field: "FY26 Revenue (audited)", why: "FY26 AR not yet published; only unaudited investor presentation (₹148 Cr)", where_it_might_be: "FY26 AR P&L (expected Jul-Aug 2026)"}
  - {field: "FY26 PAT (audited)", why: "Same; investor presentation shows ₹20.76 Cr unaudited", where_it_might_be: "FY26 AR P&L"}
  - {field: "FY26 ROCE (audited)", why: "Unaudited and internally inconsistent (37.2% vs 47.4%); MUST NOT be used until audited per FTTCP", where_it_might_be: "FY26 AR Note 32"}
  - {field: "FY26 CFO (audited)", why: "Only unaudited investor presentation (₹0.29 Cr)", where_it_might_be: "FY26 AR Cash Flow Statement"}
  - {field: "FY26 Receivables Ageing", why: "Only investor presentation aggregate (₹38.63 Cr); no age-bucket breakdown", where_it_might_be: "FY26 AR Note 17"}
  - {field: "Rating Agency (name, rating, outlook, date)", why: "Credit rating PDF not provided; B00 input gap 'rating/ folder ABSENT'", where_it_might_be: "Separate rating/ PDF folder"}
  - {field: "Rating WC / Cash Flow Commentary (quote)", why: "No rating document exists in provided set", where_it_might_be: "Credit rating working-capital section (if published)"}
  - {field: "3-Year Revenue CAGR", why: "Only 2 years history; SME IPO with no FY23 or earlier balance sheet", where_it_might_be: "FY26 AR and any subsequent audited filings"}
  - {field: "3-Year PAT CAGR", why: "Same data constraint", where_it_might_be: "FY26 AR and any subsequent audited filings"}
  - {field: "FY26 Capex (itemised by project)", why: "Aggregate investing outflow ₹40.86 Cr given; project break-up not disclosed", where_it_might_be: "FY26 AR Note 12, Note 19 (currently absent)"}
  - {field: "IndieSemic SoC capex and timeline", why: "MoU stage, 'In Pipeline,' no binding agreement or capex commitment", where_it_might_be: "FY26 AR MD&A or subsequent exchange filings"}
  - {field: "Facility Utilisation % (SMT, assembly lines)", why: "Capacity disclosed but NOT FOUND utilisation % for current or forward", where_it_might_be: "FY26 AR capacity/segment notes or subsequent investor calls"}
  - {field: "Peer P/E, EV/EBITDA, P/B, ROCE medians", why: "Only CP Plus available as direct CCTV peer; others (OSEL, Sahasra) are diversified", where_it_might_be: "B06 peer concall reports; additional peer transcripts if available"}
  - {field: "Current EPS (FY26, TTM, adjusted)", why: "Only unaudited investor presentation PAT (₹20.76 Cr); no TTM EPS or adjustment", where_it_might_be: "FY26 AR P&L; Q4 FY26 results PDF (not provided)"}
  - {field: "P/FCF (current)", why: "Cannot compute with negative FCF (FY25 -₹22.371 Cr)", where_it_might_be: "FY26 AR Cash Flow Statement (when audited)"}
  - {field: "FII + DII shareholding %", why: "Aggregator access blocked (HTTP 403); only Promoter/Public split in AR", where_it_might_be: "SEBI shareholding-pattern portal, NSE PVL letters"}
  - {field: "Promoter Pledge %", why: "AR lacks SEBI-format shareholding table with encumbrance column", where_it_might_be: "SEBI portal, NSE letters (access blocked)"}

rating_wc_quote: "NOT FOUND (credit rating PDF not available; B00 input gap 'rating/ folder ABSENT'; FTTCP deliberation notes 'Named missing evidence: the credit rating working capital rationale')"

ua_qualifiers:
  listed_12m: "YES"
  gate0_or_em: "YES (Gate0 63)"
  fii_dii_lt3: null
  all_met: false
```

---

End of report. Full table, conflicts, and unresolved sections above. YAML handoff block ready for stage 11.
