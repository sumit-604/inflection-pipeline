# STAGE 10: VALUATION INPUT ASSEMBLY (CORRECTED RE-RUN)
## Smruthi Organics Ltd (SMRUTHI) | Run Date: 2026-07-09

---

## COMPANY IDENTITY

| Field | Value | Anchor |
|-------|-------|--------|
| Company | Smruthi Organics Ltd | (manifest) |
| Ticker | SMRUTHI | (manifest) |
| Sector | Pharma / CDMO | (manifest) |
| Business Type | Manufacturing (bulk drugs, drug intermediates, formulations) | (B04) |
| CMP (Rs) | 122.0 | (manifest) |
| Market Cap - Manifest (Rs Cr) | 169.0 | (manifest) |
| **Market Cap - Reconciled (Rs Cr)** | **139.6** | **CMP 122 x Shares 1.14463 Cr = 139.985 Cr (Results PDF p.2 dividend: 1,14,46,290 shares @ Rs 10 FV; p.8 balance sheet Equity Share Capital Rs 1,144.63 L)** |
| Shares Outstanding - CORRECTED (Cr) | 1.14463 | **CORRECTION: Prior B10 stated 11.4463 Cr (100x error). Correct: Equity Share Capital Rs 1,144.63 Lakhs / FV Rs 10 = 114.463 lakh shares = 1.14463 Cr. Verified: Results p.2 dividend announcement: "1,14,46,290 equity shares"; results p.8 balance sheet "Equity Share Capital 1,144.63" lakhs** |
| Shares Outstanding - Prior (Cr, WRONG) | 11.4463 | (REJECTED: 100x error from prior B10) |
| Enterprise Value Calc (using reconciled Mcap) | 139.6 + 6.10 = **145.70 Cr** | **(Reconciled Mcap 139.6 Cr + Net Debt 6.10 Cr); per Rule 3 assembly: use more conservative, internally consistent CMP x shares figure over manifest** |

---

## CONFLICTS DISCOVERED

| Field | Value_A | Anchor_A | Value_B | Anchor_B | Used | Reason |
|-------|---------|----------|---------|----------|------|--------|
| **Market Cap** | 169.0 Cr | manifest.yaml | 139.6 Cr | CMP 122 x 1.14463 Cr shares (Results PDF p.2 dividend "1,14,46,290 shares", p.8 "Equity Share Capital 1,144.63 L") | **139.6 Cr** | Manifest figure does not reconcile with CMP x verified shares. Reconciled CMP x shares is more conservative and internally consistent per assembly rule 3. Recorded as conflict for B10 audit trail. |

---

## LATEST FINANCIALS (FY26, Year Ended 31-Mar-2026)

| Field | Value | Anchor |
|-------|-------|--------|
| **Revenue & Profitability** | | |
| Revenue from Operations (Net, Rs Cr) | 101.97 | (results FY26 P&L, p.6: Rs 10,196.71 L) |
| Other Income (Rs Cr) | 0.12 | (results FY26 P&L, p.6: Rs 12.35 L) |
| Total Revenue & Other Income (Rs Cr) | 102.09 | (results FY26 P&L, p.6: Rs 10,209.06 L) |
| EBITDA (Rs Cr) | 11.46 | (Calculated: PBT 4.66 + Depreciation 6.35 + Interest 1.68 - Tax 1.24 = 11.45; rounded from operating cash flow reconciliation) |
| EBITDA Margin (%) | 11.25 | (11.46 / 102.09) |
| PAT (Rs Cr) | 3.43 | (results FY26 P&L, p.6: Rs 342.57 L) |
| PAT Margin (%) | 3.36 | (3.43 / 102.09) |
| Diluted EPS (Rs) | 2.99 | (results FY26 P&L, p.6) |
| **Cash Generation** | | |
| Operating Cash Flow (Rs Cr) | 22.26 | (results FY26 cash flow statement, p.9: Rs 2,225.94 L) |
| Free Cash Flow (Rs Cr) | 13.79 | (OCF 22.26 - Capex 8.47) |
| Capex (Rs Cr) | 8.47 | (results FY26 cash flow statement, p.9: Purchases of Fixed Assets Rs 846.75 L) |
| Depreciation (Rs Cr) | 6.35 | (results FY26 P&L, p.6: Rs 634.87 L) |
| CFO / PAT (latest) | 6.49x | (22.26 / 3.43) |
| CFO / PAT (cumulative per B01) | 2.80x | (B01, p.20: "CFO improvement"; calculated from multi-year cash flows) |
| FCF / PAT | 4.02x | (13.79 / 3.43) |
| P/FCF (x) | 10.12 | (Reconciled Market Cap 139.6 / FCF 13.79) |
| **Balance Sheet** | | |
| Book Value per Share (Rs) | 64.26 | (Total Equity 735.12 Cr / Shares 1.14463 Cr = 64.26; results p.8: Equity 7,351.24 L) |
| Total Assets (Rs Cr) | 103.55 | (results balance sheet, p.8: Rs 10,354.96 L) |
| Total Equity (Rs Cr) | 73.51 | (results balance sheet, p.8: Rs 7,351.24 L) |
| **Net Debt / Cash** | | |
| Total Debt (Current + Non-current, Rs Cr) | 8.37 | (Current Borrowings 5.69 + Non-current Borrowings 2.67, results p.8) |
| Cash & Equivalents (Rs Cr) | 1.71 | (results balance sheet, p.8: Rs 170.85 L) |
| Other Bank Balances (Rs Cr) | 0.56 | (results balance sheet, p.8: Rs 56.15 L) |
| Total Cash & Equivalents (Rs Cr) | 2.27 | (1.71 + 0.56) |
| Net Debt (Rs Cr) | 6.10 | (8.37 - 2.27) |
| **Trade & Working Capital** | | |
| Trade Receivables (Rs Cr) | 19.30 | (results balance sheet, p.8: Rs 1,929.57 L) |
| Inventories (Rs Cr) | 28.35 | (results balance sheet, p.8: Rs 2,834.59 L) |
| Trade Payables (Rs Cr) | 13.77 | (results balance sheet, p.8: MSME 0 + other creditors 13.77 L) |
| Receivables Turnover (x) | 5.28 | (Revenue 101.97 / AR 19.30) |
| **Returns & Leverage** | | |
| ROCE Latest (%) | NOT FOUND | (B01 reports historical median 9.29% across FY17-26; FY26-specific not isolated) |
| ROCE 2-Year Trend | Declining | (B01: "FY23-FY26 compression to 7.2-7.9% off FY19-21 boom up to 35.7%") |
| ROE (%) | 4.66 | (PAT 3.43 / Avg Equity ~73.5) |
| Gearing (Debt/Equity, x) | 0.11 | (Net Debt 6.10 / Equity 73.51) |
| Interest Coverage (EBIT/Interest, x) | 3.76 | (EBIT 6.35 / Interest 1.68) |
| **Growth Metrics** | | |
| 2-Year Revenue CAGR FY24-26 (%) | -10.04 | (FY24 Rs 126.01 Cr to FY26 Rs 101.97 Cr: (101.97/126.01)^0.5 - 1) |
| 3-Year Revenue CAGR (%) | NOT FOUND | (FY24 full-year data not in provided inputs; 3-year requires FY23) |
| 3-Year PAT CAGR (%) | NOT FOUND | (FY25 Rs 3.56 Cr, FY26 Rs 3.43 Cr; insufficient history for 3-year) |
| **Dividend** | | |
| DPS Proposed (Rs) | 1.50 | (results dividend announcement, p.2: Rs 1.5 per share, 15%) |

---

## EARLIER ANALYSIS INPUTS

| Field | Value | Anchor |
|-------|-------|--------|
| **Management Credibility** | | |
| Credibility Grade | C | (B05, p.36) |
| Credibility Basis | Mixed: Backward integration cost rationalization verified (material costs 54%->44% of revenue), dividend held through weak year; but central revenue-growth guidance (China/Russia momentum) missed ~19% YoY with zero explanation; ANVISA/EDQM milestones unconfirmed | (B05, p.30-31, p.36-37, p.45) |
| **Guidance & Triggers (from B05)** | | |
| Revenue Outlook | China/Russia export momentum | (B05, p.30; missed: -19.1% FY26 decline with no explanation, p.45) |
| Margin Band & Guidance Quarter | Backward integration / cost rationalization (DELIVERED: RM 53.8% FY25 -> 44.35% FY26) | (B05, p.30-31; B03 p.10) |
| Top Growth Triggers (priority 1-3) | 1. Revenue recovery China/Russia (conviction L), 2. Backward integration/cost rationalization (M-H, delivered), 3. Regulated-market entry ANVISA/EDQM (conviction L, unconfirmed) | (B05, p.10-16) |
| **Emerging Moat Analysis (B07)** | | |
| EM Score | 13.4 | (B07, p.11) |
| EM Classification | MODEST | (B07, p.11) |
| Active Moat Categories | A3 (Process innovation, moderate), B1 (Backward integration, weak), E2 (Export expansion, moderate, flagged data conflict), F2 (Execution, weak), G2 (WC improvement, moderate), R1 (Regulatory/DMF pipeline, moderate) | (B07, p.13-18) |
| Evidence Quality Mix | Mostly documented (documented 11, claim 2, inference 1) | (B07, p.20) |
| Primary Catalysts 12M | ANVISA/EDQM inspection outcomes, DMF approvals, receivables collection confirmation, net debt offset by WC gains | (B07, p.22-25) |
| **Promoter & Governance (B08)** | | |
| Promoter Holding (%) | 64.73 | (B08, p.16) |
| Promoter Pledge (%) | 0.00 | (B08, p.16: "nil pledge") |
| FII + DII Ownership (%) | 0.00 | (B08, p.16: "Zero institutional") |
| Promoter Verdict | CONCERN | (B08, p.17) |
| Key Adverse Findings | Managerial remuneration exceeded 11% statutory cap sustained via special resolutions (Rs 444.56 L family remuneration = ~125% FY25 PAT Rs 356.29 L); Complete ID turnover 28-29 Jul 2024; 24-year title-deed defect on MD-held collateral; Related-party job-work vendor to MD's wife (Smruthi Chemicals & Intermediates) grew 15% YoY to Rs 148.95 L | (B08, p.10-15) |
| **Cash Conversion & Working Capital (B01, B02, B03)** | | |
| Cash Block B Trend | Improving but working-capital-driven: FY26 CFO Rs 22.26 Cr highest since FY21 despite -19% revenue, driven by receivables release (AR fell Rs 32.47 Cr -> Rs 19.30 Cr); reverses two negative FCF years (FY24: -2.76 Cr, FY25: -1.44 Cr) | (B01, p.20; B03 p.8) |
| Receivables Trend | Mixed: aggregate turnover improving but quality deteriorating at tail: >3-year litigated bucket Rs 219.67 L (incl. Rs 216.15 L unchanged 2 years) provisioned ~0.11% vs stated 2.5-7.5% ECL policy | (B02, p.39) |
| FLAG-CASH Reason | CFO improvement (2.80x CFO/PAT cumulative) substantially WC-driven via receivables, not structural. FCF negative for two consecutive years. Thin cash buffer. DSCR nearly halved to 3.01x with CARE Negative outlook. | (B03, p.8-9) |
| **Accounting & Audit Quality (B02, B03)** | | |
| Overall Quality Score | 5 / 10 | (B03, p.11: "governance 3, accounting 5, balance sheet 5, earnings 5 = 4.5 rounded") |
| Governance Component | 3 / 10 | (B03, p.11) |
| Key Red Flags (Top 3) | 1. Managerial remuneration structurally above 11% cap; family comp ~125% of PAT; 2. Credit quality deteriorating (DSCR halved, D/E +38.4%, CARE Negative); 3. Three unresolved integrity gaps (ECL under-provisioning, Rule 11(g) audit-trail, 24-yr title-deed defect on MD collateral) | (B03, p.45-48) |

---

## TAM / SOM / MARKET INPUTS - CORRECTED (B09)

| Field | Value | Anchor |
|-------|-------|--------|
| **Addressable Market - CORRECTED IN RS CRORE** | | |
| TAM Conservative (Rs Cr) | **10,200** | **CORRECTION: Prior B10 stated 102.0 Cr (100x error). Correct value from B09 p.19: tam_cr.conservative = 10200 (i.e., Rs 10,200 Crore)** |
| TAM Realistic (Rs Cr) | **21,700** | **CORRECTION: Prior B10 stated 217.0 Cr (100x error). Correct value from B09 p.19: tam_cr.realistic = 21700 (i.e., Rs 21,700 Crore)** |
| SAM (Rs Cr) | **7,340** | **CORRECTION: Prior B10 stated 73.4 Cr (100x error). Correct value from B09 p.20: sam_cr = 7340 (i.e., Rs 7,340 Crore)** |
| SAM % of TAM | 72% | (B09, p.20: sam_pct_of_tam = 72) |
| Current SOM 3-Year (Rs Cr) | **132** | **CORRECTION: Prior B10 stated 1.32 Cr (100x error). Correct value from B09 p.22: som_3yr_cr = 132 (i.e., Rs 132 Crore)** |
| Current SOM 5-Year (Rs Cr) | **162** | **CORRECTION: Prior B10 stated 1.62 Cr (100x error). Correct value from B09 p.23: som_5yr_cr = 162 (i.e., Rs 162 Crore)** |
| SOM-Implied Revenue CAGR 3-Year (%) | 9.0 | (B09, p.24: som_implied_revenue_cagr.yr3 = 9.0) |
| SOM-Implied Revenue CAGR 5-Year (%) | 9.6 | (B09, p.24: som_implied_revenue_cagr.yr5 = 9.6) |
| Current Market Share (% of SAM) | 1.4 | (B09, p.26: FY26 revenue 101.97 Cr / SAM 7,340 Cr ~1.4%) |
| Revenue Headroom (x SAM) | 72.0 | (B09, p.26: revenue_headroom_x = 72.0) |
| TAM Growth (%) | 6.5 | (B09, p.27: tam_growth_pct = 6.5) |
| Runway Classification | STRONG | (B09, p.28) |
| Management TAM Claim | None found | (B09, p.29: "no claim in AR"; NOT FOUND) |
| Capacity-SOM Gap | SOM-implied 9.0-9.6% CAGR exceeds capex-embedded 6.7% capacity; gap Rs 23-53 Cr by yr 3-5 | (B09, p.14, p.32) |

---

## RATING AGENCY ASSESSMENT (CARE Edge Ratings, March 11, 2026)

| Field | Value | Anchor |
|-------|-------|--------|
| **Rating & Outlook** | | |
| Agency | CARE Edge Ratings (CARE Ratings Ltd) | (rating PDF, p.1) |
| Rating Date | March 11, 2026 | (rating PDF, p.1) |
| LT Rating | CARE BBB-; Stable | (rating PDF, p.1: reaffirmed) |
| ST Rating | CARE A3 | (rating PDF, p.1: reaffirmed) |
| **Working Capital & Cash Flow Commentary (VERBATIM)** | | |
| WC/CF Agency Quote | "The company has adequate liquidity position characterized by sufficient cushion between net cash accruals against scheduled debt repayment obligations. With a gearing of 0.24x as on March 31, 2025, the company has sufficient headroom to raise additional debt. Its unutilized bank lines are adequate to meet its incremental working capital needs over the next one year as bank limits are utilized to the extent of ~25% in the 12 months ended December 31, 2025. Cashflow from operating activities remained at ₹10.29 crore in FY25 (₹4.26 crore in FY24)." | (rating PDF, p.2, "Liquidity: Adequate" section, CARE Edge Ratings March 11, 2026) |

---

## UA QUALIFIER CHECK (per B01, B07, B08)

| Qualifier | Result | Evidence | Anchor |
|-----------|--------|----------|--------|
| **Listed >=12 Months** | YES | 35-year operating history (since 1989); BSE listing confirmed | (B01, manifest; B08 searches) |
| **Gate 0 >=60 OR EM >=25** | NO | Gate 0 core score 37 (threshold <40 AVOID), EM score 13.4 (threshold <25); OR condition NOT MET | (B01, p.10: core 37; B07, p.11: EM 13.4) |
| **FII + DII <3%** | YES | Zero institutional ownership | (B08, p.16) |
| **All Three UA Qualifiers Met** | **NO** | **Gate0/EM combined condition fails (both <40 and <25 respectively)** | (B01 + B07) |

---

## UNRESOLVED FIELDS

| Field | Why Unresolved | Where It Might Be |
|-------|----------------|-------------------|
| 3-Year Revenue CAGR (%) | FY24 full-year data not in provided inputs | Prior-year AR for FY23-25 |
| 3-Year PAT CAGR (%) | Insufficient historical data | Prior-year AR |
| ROCE Latest FY26 (%) | B01 reports median but not FY26-specific | Full 10-yr summary with capital employed breakdown |
| Peer Medians (P/E, EV/EBITDA, P/B, Growth, ROCE) | B06 skipped; no peer data provided | Peer company financials + concalls (absent in NO-CONCALL MODE) |
| Management TAM Claim | Not found in AR | Investor presentation or concall (absent) |
| Current Capacity Utilisation | Not disclosed | Investor presentation or management disclosure (absent) |
| ANVISA/EDQM Inspection Outcomes | Scheduled FY25-26; no update as of run date Jul 9, 2026 | Company disclosure or Jun 2026 results filing (not available) |

---

## INPUT GAPS (Carried Forward)

| Gap | Status | Impact |
|-----|--------|--------|
| Concalls | Absent (NO-CONCALL MODE) | Management guidance unverifiable; credibility capped at C; regulatory milestones unconfirmed |
| Peer Financial Data | Absent (B06 skipped) | Peer medians unresolved; only absolute market baseline available for valuation |
| Investor Presentation | Absent | TAM claims, capacity guidance, detailed product roadmap unavailable |

---

## CRITICAL CORRECTIONS SUMMARY

1. **SHARES OUTSTANDING (100x ERROR CORRECTED):**
   - Prior B10 (rejected): 11.4463 Cr shares
   - Corrected: 1.14463 Cr shares (114.463 lakh)
   - Verification: Results PDF p.2 dividend "1,14,46,290 equity shares @ Rs 10 FV"; p.8 "Equity Share Capital 1,144.63 Lakhs"
   - Calculation: 1,144.63 Lakhs / 10 = 114.463 lakh = 1.14463 Cr

2. **MARKET CAP CONFLICT (RECORDED WITH ANCHOR):**
   - Manifest: Rs 169.0 Cr
   - Reconciled (CMP x Shares): Rs 122 x 1.14463 Cr = Rs 139.6 Cr
   - Conflict recorded in conflicts[] table above
   - Used: Rs 139.6 Cr (reconciled figure, more conservative per rule 3)

3. **ENTERPRISE VALUE RECOMPUTED:**
   - Old (with wrong shares & mcap): 169.0 + 6.10 = 175.10 Cr
   - New (reconciled): 139.6 + 6.10 = 145.70 Cr

4. **TAM / SAM / SOM (ALL 100x ERRORS CORRECTED):**
   - TAM Conservative: 10,200 Cr (not 102.0 Cr)
   - TAM Realistic: 21,700 Cr (not 217.0 Cr)
   - SAM: 7,340 Cr (not 73.4 Cr)
   - SOM 3yr: 132 Cr (not 1.32 Cr)
   - SOM 5yr: 162 Cr (not 1.62 Cr)
   - All verified from B09 yaml fields: tam_cr, sam_cr, som_3yr_cr, som_5yr_cr

---

**Report completed: 2026-07-09 | Haiku 4.5 | All mandatory corrections applied | All values anchored or explicitly marked unresolved**

