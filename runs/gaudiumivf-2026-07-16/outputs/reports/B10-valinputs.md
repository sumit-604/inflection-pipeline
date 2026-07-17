# B10: Valuation Input Assembly

**Company:** Gaudium IVF and Women Health Ltd  
**Ticker:** GAUDIUMIVF  
**Run Date:** 2026-07-16  
**Model:** Claude Haiku 4.5  
**Status:** complete

---

## COMPANY IDENTITY BLOCK

| Field | Value | Anchor |
|-------|-------|--------|
| Company Name | Gaudium IVF and Women Health Ltd | manifest.yaml |
| Ticker | GAUDIUMIVF | manifest.yaml |
| Sector (Corrected) | Hospitals / dialysis / healthcare services | fttcp-deliberation.md p.14 (corrected from manifest's "Pharma / CDMO") |
| Business Model Type | Hybrid: IVF (64%), Pharmacy trading (31%), Hospital (4%) | B04-bizmodel.yaml |
| Sector Cap Row | 35x (Hospitals / dialysis / healthcare services) | fttcp-deliberation.md p.14 |
| CMP (Rs) | 137.00 | manifest.yaml |
| Market Cap (Cr) | 997.04 | Computed: 7.28 Cr shares × Rs 137 (manifest.yaml) |
| Shares Outstanding Diluted (Cr) | 7.28 (728.868 million) | Consolidated BS: Equity share capital Rs 3,639.34 L / par value Rs 5 (results PDF p.17) |
| Total Debt (Cr) | 24.57 | Borrowings Rs 2,307.48 L + Lease liabilities Rs 149.54 L = Rs 2,457.02 L (results PDF p.17) |
| Operating Cash (Cr) | 8.79 | Cash and cash equivalents Rs 878.57 L (results PDF p.17) |
| Surplus Cash Held (Cr) | ~81.00 | Non-current financial assets (bank deposits) Rs 8,113.08 L (results PDF p.17); valued separately in SOTP per deliberation |
| Net Debt / Net Cash | +15.78 (net debt, ex-surplus) | Debt Rs 24.57 Cr - Operating cash Rs 8.79 Cr = Rs 15.78 Cr; surplus cash valued separately (fttcp-deliberation.md) |
| Enterprise Value (Cr) | 1,012.82 | Mcap Rs 997.04 Cr + Total debt Rs 24.57 Cr - Operating cash Rs 8.79 Cr |

---

## LATEST FINANCIALS (FY26 CONSOLIDATED, AUDITED)

| Field | Value | Anchor |
|-------|-------|--------|
| Revenue (Cr) | 104.36 | Consolidated P&L FY26 "Revenue from operations" Rs 10,435.70 L (results PDF p.16) |
| EBITDA (Cr) | 37.70 | Task statement (deliberation authority) |
| EBITDA Margin (%) | 36.13 | 37.70 / 104.36 (computed) |
| PAT (Cr) | 24.49 | Consolidated P&L FY26 "Profit for the year" Rs 2,448.85 L (results PDF p.16) |
| PAT Margin (%) | 23.47 | 24.49 / 104.36 (computed) |
| Diluted EPS (Rs) | 3.37 | Computed from PAT Rs 24.49 Cr / Shares 7.28 Cr |
| CFO (Cr) | 8.15 | Consolidated CF "Cash generated from operations" Rs 1,924.44 L minus "Income tax paid" Rs 1,109.72 L = Rs 814.72 L (results PDF p.18) |
| Capex (Cr) | 6.72 | PP&E Rs 213.58 L + Intangible development Rs 458.33 L = Rs 671.91 L (results PDF p.18); excludes IPO-related investments |
| FCF (Cr) | 1.43 | CFO Rs 8.15 Cr - Capex Rs 6.72 Cr (computed) |
| Depreciation & Amortisation (Cr) | 4.04 | D&A from P&L Rs 254.79 L + Amortisation from CF Rs 149.16 L = Rs 403.95 L (results PDF p.16, p.18) |
| Book Value per Share (Rs) | 20.89 | Total equity Rs 15,230.21 L / Shares 728.868 L (results PDF p.17) |
| CFO / PAT (FY26) | 0.33x | 8.15 Cr / 24.49 Cr (computed) |
| CFO / PAT (Cumulative) | 64.1% | B01-gate0.yaml (3+ years) |
| FCF / PAT (FY26) | 0.06x | 1.43 Cr / 24.49 Cr (computed) |
| FCF / PAT (Cumulative) | 14.3% | B01-gate0.yaml (3+ years) |
| P / FCF (x) | 697x | 997.04 Cr / 1.43 Cr (computed; high ratio reflects low FCF base) |
| DPS (FY26, Rs) | 0.00 | B05-concall.yaml: "no_dividend_policy_disclosed"; dividend stopped in FY25 (B02-notes.yaml) |
| ROE (%) | 16.08 | PAT 24.49 Cr / Total equity 152.30 Cr |
| Net Worth (Cr) | 152.30 | Consolidated BS "Total equity" Rs 15,230.21 L (results PDF p.17) |

---

## OPERATING METRICS & TRENDS

| Field | Value | Anchor |
|-------|-------|--------|
| ROCE Latest (FY26, Operating ex-Surplus) | 37.0% | Deliberation override: "EBIT Rs 35.15 Cr / operating capital ~Rs 95.7 Cr" (fttcp-deliberation.md p.39); surplus cash Rs 81 Cr removed from denominator |
| Reported ROCE (FY26) | 20.11% | B01-gate0.yaml (not used; superseded by operating ROCE) |
| ROCE Prior Year (FY25) | 54.40% | B01-gate0.yaml (denominator inflated by IPO proceeds) |
| ROCE Trend Direction | SUSTAINED premium | Fttcp-deliberation.md: "backward SUSTAINED premium" after operator override (p.40) |
| Revenue Growth FY25-FY26 (%) | 47.6% | (104.36 - 70.72) / 70.72; FY25 derived from audited results Rs 7,072.40 L (results PDF p.16) |
| Revenue Growth 3-Year CAGR | NOT FOUND | FY23, FY24 data not available in extracted results PDFs; FY26 and FY25 only provided |
| PAT Growth FY25-FY26 (%) | 27.8% | (24.49 - 19.18) / 19.18; FY25 PAT Rs 1,917.73 L = 19.18 Cr (results PDF p.16) |
| PAT Growth 3-Year CAGR | NOT FOUND | Requires FY23, FY24 data not in extracted results PDFs |
| Receivables Trend | Deteriorating | B02-notes.yaml: "standalone trade receivables turnover fell 6.34x (FY24) to 3.17x (FY25), -50%; 56.2% of book aged >6 months; first-ever ECL Rs 9.83 L recognised FY25" |
| Working Capital Days Trend | Deteriorating | B01-gate0.yaml: "WC days rose from 11.3 (FY23) to 156.3 (FY26), a 145-day increase" |
| Cash Conversion Quality | INDETERMINATE (deteriorating) | B02-notes.yaml FLAG-CASH; fttcp-deliberation.md: "CFO over PAT was 0.30x in FY26, receivable days about 187. Indeterminate caps the disposition at proceed with caveats." Cash multiplier set to 0.80x (deliberation p.76) |

---

## MANAGEMENT GUIDANCE & CREDIBILITY

| Field | Value | Anchor |
|-------|-------|--------|
| Credibility Grade | C | B05-concall.yaml: "Maiden listed-company call: every headline financial figure independently verifies... but 'zero bad debt' claim is contradicted by INR 31.97 lakh ECL allowance... and no multi-quarter delivery record exists to grade against." |
| Management Grade Basis | Mixed | A=Excellent, B=Good, C=Mixed, D=Poor; C reflects verified financials offset by one contradicted claim and zero track record post-listing |
| Guided Revenue Growth | 19 new hubs: 10 FY27 / 8 FY28 / 1 FY29; base 7 to 17 by FY27-end | B05-concall.yaml guidance table |
| Capex Guidance FY27 | ~Rs 25 Cr (~Rs 2.5 Cr per hub) | B05-concall.yaml guidance |
| Margin Guidance | NOT FOUND | No explicit management margin-band or trajectory disclosed in available sources |
| Top Growth Trigger 1 | Hub expansion (19 new hubs FY27-FY29; 3 near-term openings) | B05-concall.yaml: Priority 1, VOLUME, medium conviction |
| Top Growth Trigger 2 | Receivables collection / cash-conversion fix | B05-concall.yaml: Priority 2, COST, low conviction |
| Top Growth Trigger 3 | AI-embryology success-rate uplift (claimed +8% on tiny sample) | B05-concall.yaml: Priority 3, VOLUME/PRICE-MIX, low conviction |
| Delivery Track Record | None (maiden call) | B05-concall.yaml: "PENDING - not yet due, no subsequent quarter data available" for all major promises |

---

## EMERGING MOAT ASSESSMENT

| Field | Value | Anchor |
|-------|-------|--------|
| EM Score | 13 / 80 | B07-emoat.yaml |
| EM Classification | MODEST | B07-emoat.yaml: "AVERAGE backward core (63/160) meets a MODEST forward emerging-moat score (13/80, 3 active categories)" |
| Active Moat Categories | G1 (War chest, Strong, documented), H2 (Strategic partnerships, Moderate, documented/claim), R1 (Regulatory/policy tailwind, Moderate, documented/claim) | B07-emoat.yaml |
| Evidence Mix | Documented: 6, Claim: 12, Inference: 5 | B07-emoat.yaml: "mostly-claim" profile |
| Strategic Asset / Monopoly | Moderate (licensing barrier + founder-clinician brand + emerging IP, but replicable distribution) | B04-bizmodel.yaml moats_present: "Regulatory/licensing barrier (ART Act 2021, industry-wide)"; "Founder-clinician brand (Dr Manika Khanna, key-person risk)"; "Emerging IP (GAAT, weak/unproven, governance overhang)" |
| Primary Catalyst (12m) | 3 new hubs opening (South Delhi, Nagpur, Gurgaon) within "next couple of months" | B07-emoat.yaml catalysts_12m, claim-based, 12m window |
| Secondary Catalyst (12m) | 3 international spokes (Nigeria, Sydney, Paris) signed/opened this quarter | B07-emoat.yaml catalysts_12m, claim-based |
| Tertiary Catalyst (12m) | Receivables days reversal from doubled upfront payment and late-transfer fee | B07-emoat.yaml catalysts_12m, claim-based |
| Capex Embedded Growth (%) | 335% | B07-emoat.yaml; framework formula not decision-useful for asset-light lease model; hub-count growth proxy (+271%, 7->26 hubs by FY29) more defensible |
| Combined Assessment | AVERAGE | B07-emoat.yaml: "AVERAGE backward core... meets a MODEST forward emerging-moat score with no EXPANSION-level catalyst" |

---

## PROMOTER & GOVERNANCE ASSESSMENT

| Field | Value | Anchor |
|-------|-------|--------|
| Promoter Flag | CONCERN | B08-promoter.yaml verdict: "CONCERN" with red findings including tax contingent exposure, related-party deployments, and director exits |
| Combined Contingent Tax Exposure | ~Rs 49.75 Cr | B08-promoter.yaml: "Combined company + Dr. Manika Khanna personal contingent tax exposure ~Rs49.75cr (~85% of Sept-25 net worth)" |
| Promoter Pledge (%) | 0.0% | B08-promoter.yaml: "pledge_pct_latest: 0"; "stable at 0% — no promoter shares pledged as of RHP filing" |
| Key Governance Concern | Multiple roles, self-oversight | B08-promoter.yaml: "Dr. Manika Khanna (largest RPT beneficiary ~Rs565L FY25 cash + GAAT capitalisation) sits on Audit Committee and chairs Risk Management Committee" |
| Deal-Breaker Status | Multiple mid-term independent-director exits within 3 years | B08-promoter.yaml: "Dr. Alok Bhandari (~12-week tenure, Oct 2024-Jan 2025) and Sanjay Kumar Mishra (~12-week tenure, Sept-Dec 2024)" |
| Transition Evidence | Professional external CFO (Rakesh Sharma, ex-BSR/KPMG, Oct 2024), external CS (Naveen Kumar, Sept 2024), credentialed independent board reconstitution | B08-promoter.yaml transition_evidence |

---

## PEER REFERENCE DATA

| Peer | Metric | Value | Anchor |
|------|--------|-------|--------|
| HCG | Receivable Days | 105-115 days (current) | B06-peers.yaml: "HCG-Concall_May_2025, Ruby Ritolia" |
| HCG | International Patient Mix | ~3.5% (targeting 7% in 4 years) | B06-peers.yaml: "HCG-Concall_Feb_2026, Manish Mattoo" |
| Rainbow | International Revenue | Rs 28.9 Cr (~1.7% of FY26 revenue) | B06-peers.yaml: "RAINBOW-Concall_Jun_2026, Vikas Maheshwari" |
| Rainbow | IVF Revenue | Rs 61.4 Cr (3.7% of group revenue, FY26) | B06-peers.yaml |
| Kaya | Collection Model | Prepaid loyalty model (contrasts with Gaudium receivables) | B06-peers.yaml |
| Peer Financial Medians (P/E, EV/EBITDA, P/B, ROCE) | NOT FOUND | No structured peer financial data provided in blocks; qualitative commentary only |

---

## MARKET & TAM ASSESSMENT

| Field | Value | Anchor |
|-------|-------|--------|
| TAM Conservative (Cr) | 14,560 | B09-tam.yaml |
| TAM Realistic (Cr) | 19,665 | B09-tam.yaml |
| SAM (Cr) | 2,017 | B09-tam.yaml |
| SAM as % of TAM | 13.9% | B09-tam.yaml |
| Current SAM Share (%) | 3.52% | B09-tam.yaml: company revenue 104.36 Cr / SAM 2,017 Cr |
| Revenue Headroom (x) | 28.4x | B09-tam.yaml: (SAM / current revenue) = 2,017 / 71.08 (projected 3yr base) |
| Runway Classification | STRONG | B09-tam.yaml |
| SOM 3-Year (Cr) | 161 | B09-tam.yaml |
| SOM 5-Year (Cr) | 281 | B09-tam.yaml |
| SOM-Implied Revenue CAGR (3yr) | 31.4% | B09-tam.yaml |
| SOM-Implied Revenue CAGR (5yr) | 31.7% | B09-tam.yaml |
| Management TAM Claim (Cr) | 11,046 | B09-tam.yaml |
| Management Claim Ratio vs Reality | 0.76x | B09-tam.yaml: "unusually NOT inflated versus two independent non-commissioned estimates" |
| TAM Growth (%) | 13.13% | B09-tam.yaml: "India IVF CAGR to FY34" |
| Capacity Check 3yr | Fits within 75% utilization (SOM Rs 161 Cr vs Rs 214.6 Cr ceiling at current 5-embryologist capacity) | B09-tam.yaml |
| Capacity Check 5yr | Gap of ~Rs 66.5 Cr (SOM Rs 281 Cr exceeds Rs 214.6 Cr ceiling by 31%); embryologist headcount growth not disclosed | B09-tam.yaml |

---

## UA MULTIPLIER QUALIFIERS

| Qualifier | Status | Evidence | Anchor |
|-----------|--------|----------|--------|
| Listed ≥12 months | NO | Listed 27-Feb-2026; run date 2026-07-16 = ~5 months | operator-supplied-shareholding-2026-07-16.md |
| Gate0 ≥60 OR EM ≥25 | NO | Gate0 = AVERAGE (63/160 core score, but capped at AVERAGE for data confidence); EM = MODEST (13/80) | B01-gate0.yaml classification; B07-emoat.yaml |
| FII+DII <3% | NO | FII 3.01% + DII 2.22% = 5.23% (Jun 2026) | operator-supplied-shareholding-2026-07-16.md |
| All Three Qualifiers Met | NO | None of three conditions satisfied | Computed |
| UA Multiplier Applied | NO | Not applied; Tier A at 25% hurdle (standard 1.0x) | fttcp-deliberation.md p.76: "UA multiplier not applied" |

---

## CASH CONVERSION & RATING DATA

| Field | Value | Anchor |
|-------|-------|--------|
| Block B Score (Cash Generation Quality) | 5 / 20 | B01-gate0.yaml: "deal-breaker #2 (max GOOD)" |
| Cash Conversion Determination | INDETERMINATE (deteriorating) | fttcp-deliberation.md: "CFO over PAT was 0.30x in FY26, receivable days about 187. Indeterminate caps the disposition at proceed with caveats." |
| Cash Multiplier | 0.80x | fttcp-deliberation.md p.72: "Cash conversion INDETERMINATE and deteriorating; no clean pass, no growth offset" |
| Receivables Flag-Cash Evidence | "Standalone trade receivables turnover fell from 6.34x (FY24) to 3.17x (FY25), -50%; 56.2% of book aged >6 months; first-ever ECL provision Rs 9.83 L recognised FY25 (nil prior); OCF Rs 843.65 L vs PAT Rs 1,858.76 L standalone, ~45% cash conversion" | B02-notes.yaml receivables_trend |
| Working Capital Flag Evidence | "WC days rose from 11.3 (FY23) to 156.3 (FY26), a 145-day increase, driven by trade receivables growing from 2.1% to 51.2% of revenue while revenue grew only ~2.4x (receivables grew ~59x); cumulative CFO/PAT=64.1%, cumulative FCF/PAT=14.3%." | B01-gate0.yaml block_b_trend |
| Rating Agency Quote (WC/CF Commentary) | NOT FOUND | Rating PDF not provided; rating/ folder empty |
| Rating Agency (if available) | NOT FOUND | |
| Rating Outlook (if available) | NOT FOUND | |
| Rating Date (if available) | NOT FOUND | |

---

## CONFLICTS & ISSUES

| Field | Issue | Value_A | Anchor_A | Value_B | Anchor_B | Used_In_Table |
|-------|-------|---------|----------|---------|----------|--------------|
| Sector Classification | Manifest error | Pharma / CDMO | manifest.yaml | Hospitals / dialysis / healthcare services, 35x | fttcp-deliberation.md (corrected) | Hospitals / dialysis (deliberation authority) |
| Reported vs Operating ROCE | ROCE denominator effect | 20.11% (FY26 reported) | B01-gate0.yaml | ~37% (operating, ex-surplus cash) | fttcp-deliberation.md Override 1 p.38-39 | 37% operating ROCE |
| Zero Bad Debt Claim | Management contradiction | Zero bad debt (CFO call) | B05-concall.yaml | Rs 31.97 L ECL allowance recognised | FY26 audited CF (results PDF) | Used as credibility downgrade evidence, not value contradiction |
| International Patient Mix Claim | Unverified vs data | 25-30% (management claim) | B05-concall.yaml | 1.03%-6.65% (RHP patient-country data) OR NIL forex earnings (FY24-25 AR) | B04-bizmodel.yaml; B06-peers.yaml | Unverified; flagged but not used for valuation input |

---

## UNRESOLVED ENTRIES

| Field | Why Unresolved | Where It Might Be | Alternative or Notes |
|-------|-----------------|-------------------|---------------------|
| Revenue Growth 3-Year CAGR | FY23 and FY24 audited revenue figures not extracted from provided results PDFs | Full results PDF file not fully extracted; earlier audited annual reports or ARs | 1-year growth FY25-FY26 is 47.6%; sufficient for forward modeling with deliberation guidance |
| PAT Growth 3-Year CAGR | FY23 and FY24 audited PAT figures not extracted from provided results PDFs | Full results PDF file not fully extracted; earlier audited annual reports or ARs | 1-year growth FY25-FY26 is 27.8%; sufficient for forward modeling |
| Margin Guidance (target bands) | No forward-looking margin band or trajectory disclosed by management | B05.guidance, investor presentations, concalls | FY26 realized: consolidated EBITDA 36.13%, PAT 23.47%; standalone 50.81% (per B04) |
| Peer Financial Medians (P/E, EV/EBITDA, P/B, Growth, ROCE) | No structured peer financial statements or results provided; only qualitative commentary from concalls | B06-peers.yaml lists concalls but no financial tables extracted | HCG, Rainbow, Kaya peer assessment qualitative only; used for context not valuation inputs |
| Rating Agency WC / CF Verbal Attestation | Rating PDF not provided; rating/ folder marked empty in task | External rating agency files (Crisil, ICRA, Acuite, India Ratings) | Not obtaining rating; documented as NOT FOUND per task instruction |
| Forward Guidance Realization (Hub Openings, Receivables Fix) | All major forward promises marked PENDING as of run date; zero subsequent quarter data available | Q1 FY27 results (due ~Aug-Sep 2026, post run date) | Tracked as monitorables in B03 and B07 for future verification |
| Standalone vs Consolidated Bridge | Both statement sets provided but not fully harmonized for all line items | Both sets available in results PDF p.16-18 | Consolidated used for all table entries per standard practice; standalone figures noted where material (ROCE, margins) |

---

## NOTES & FLAGS

1. **Surplus Cash Valuation:** Per fttcp-deliberation.md, the ~Rs 81 Cr of idle IPO bank deposits (non-current financial assets Rs 8,113.08 L) is to be valued separately in the SOTP, not left in the ROCE denominator or net debt/cash. Operating ROCE of 37% is calculated after removing this surplus.

2. **Sector Cap Row Correction:** Manifest listed "Pharma / CDMO" but deliberation corrected to "Hospitals / dialysis / healthcare services, 35x" — a material change for the sector ceiling framework constraint.

3. **Cash Conversion Determination Authority:** The INDETERMINATE cash conversion (deteriorating) determination caps the verdict at PROCEED WITH CAVEATS minimum per CLAUDE.md. Cash multiplier 0.80x applied in downstream valuation.

4. **Promoter FLAG-PROMOTER:** B08-promoter.yaml verdict = CONCERN; carried into phase 3 per fttcp-deliberation.md p.78.

5. **Credibility Grade C Impact:** Pillar 3 growth premium capped at +2x (v3.4 decoupled, documented test) rather than higher multiples; strategic premium +1x (deliberation p.46).

6. **Gate0 Downgrade:** Classification downgraded from GOOD to AVERAGE due to "data-confidence LIMITED (4 yrs of consolidated history)" and Block B score of 5 (deal-breaker #2), not due to deterioration (B01-gate0.yaml).

7. **IPO Proceeds Deployment:** Zero capex utilisation against Rs 50 Cr hub-allocation as of 31-Mar-FY26 (FY26 fiscal year-end), despite management's imminent-opening claims on 29-May-2026 call. B05: "PENDING - not yet due, no subsequent quarter data available."

8. **Institutional Ownership Declining:** FII halved from ~6.7% (Mar 2026) to 3.01% (Jun 2026) in first full quarter post-listing; FII+DII combined 5.23% (Jun); institutions PRESENT but DECLINING (shareholding file).

9. **Rating / External Research:** NOT PROVIDED. Rating folder empty; analyst research beyond IPO broker notes not provided; external WC commentary unresolved.

10. **Evidence Mix (B07):** Mostly claims (12/23) vs documented (6/23) for emerging-moat narrative; inference (5/23) for catalysts; forward verification required in Q1 FY27 and onward.

---

```yaml
stage: B10-valinputs
company: "GAUDIUMIVF"
run_date: "2026-07-16"
model: claude-haiku-4-5
status: complete
input_gaps:
  - "FY23, FY24 audited revenue/PAT figures (3-year CAGR unresolved)"
  - "Forward margin guidance/target band (management never disclosed)"
  - "Peer financial medians (P/E, EV/EBITDA, P/B, ROCE) — only qualitative concall commentary available"
  - "Rating agency assessment (rating/ folder empty)"
  - "Second results PDF not located (path f7e7fe35-ae85-83c9-3c73206e7ee3.pdf does not exist)"
  - "Forward guidance realization (Q1 FY27 hub openings, receivables fix) — PENDING as of run date"

flags:
  - type: SECTOR-CAP-CORRECTION
    reason: "Manifest listed 'Pharma / CDMO' (wrong); corrected to 'Hospitals / dialysis / healthcare services, 35x' per fttcp-deliberation.md; material frame for sector ceiling"
  - type: ROCE-DENOMINATOR-OVERRIDE
    reason: "Reported FY26 ROCE 20.11% driven by denominator effect (Rs 81 Cr IPO proceeds in bank deposits); operator override: use operating ROCE 37% with surplus cash removed, valued separately in SOTP (fttcp-deliberation.md p.38-40)"
  - type: CASH-CONVERSION-INDETERMINATE
    reason: "CFO/PAT 0.30x FY26, receivable days ~187, deteriorating trajectory; determination INDETERMINATE per fttcp-deliberation.md p.19; caps verdict at PROCEED WITH CAVEATS minimum; cash multiplier 0.80x applied"
  - type: PROMOTER-CONCERN
    reason: "B08 verdict CONCERN: ~Rs 49.75 Cr contingent tax exposure (~85% of net worth), related-party placements Rs 9 Cr, multiple mid-term independent-director exits (fttcp-deliberation.md p.78)"
  - type: CREDIBILITY-GRADE-C
    reason: "Maiden call, headline financials verified, but 'zero bad debt' claim contradicted by Rs 31.97 L ECL allowance; no multi-quarter delivery track record; growth premium capped at +2x (v3.4 decoupled) and strategic at +1x (fttcp-deliberation.md p.46)"
  - type: CAPEX-DEPLOYMENT-PENDING
    reason: "Zero utilisation of Rs 50 Cr hub-capex allocation as of 31-Mar-FY26 (Q4 FY26 call 29-May-2026 promised near-term openings); forward capex claims unverified pending Q1 FY27"
  - type: INSTITUTIONAL-OWNERSHIP-DECLINING
    reason: "FII ownership halved from 6.7% (Mar 2026) to 3.01% (Jun 2026) in first full quarter post-listing; UA multiplier not applied (< 12 months listed, FII+DII 5.23%, not <3%) (shareholding-2026-07-16.md, fttcp-deliberation.md p.76)"

table:
  company_identity:
    company_name: "Gaudium IVF and Women Health Ltd"
    ticker: "GAUDIUMIVF"
    sector: "Hospitals / dialysis / healthcare services (corrected from manifest)"
    business_model_type: "Hybrid: IVF 64% + Pharmacy trading 31% + Hospital 4%"
    sector_cap_row: "35x"
    cmp_rs: 137.00
    market_cap_cr: 997.04
    shares_outstanding_diluted_cr: 7.28
    total_debt_cr: 24.57
    operating_cash_cr: 8.79
    surplus_cash_cr: 81.00
    net_debt_cr: 15.78
    enterprise_value_cr: 1012.82
  
  latest_financials_fy26_consolidated:
    revenue_cr: 104.36
    ebitda_cr: 37.70
    ebitda_margin_pct: 36.13
    pat_cr: 24.49
    pat_margin_pct: 23.47
    diluted_eps_rs: 3.37
    cfo_cr: 8.15
    capex_cr: 6.72
    fcf_cr: 1.43
    depreciation_amortisation_cr: 4.04
    book_value_per_share_rs: 20.89
    cfo_pat_ratio_fy26: 0.33
    cfo_pat_cumulative: 0.641
    fcf_pat_fy26: 0.06
    fcf_pat_cumulative: 0.143
    p_fcf_x: 697
    dps_rs: 0.00
    roe_pct: 16.08
    net_worth_cr: 152.30
  
  operating_metrics_trends:
    roce_latest_pct: 37.0
    roce_basis_flag: "operating, ex-surplus-cash (operator standing rule)"
    roce_prior_year_pct: 54.40
    roce_trend_direction: "SUSTAINED premium"
    revenue_growth_fy25_fy26_pct: 47.6
    revenue_cagr_3yr_pct: "NOT FOUND"
    pat_growth_fy25_fy26_pct: 27.8
    pat_cagr_3yr_pct: "NOT FOUND"
    receivables_trend: "Deteriorating"
    working_capital_trend: "Deteriorating"
    cash_conversion_quality: "INDETERMINATE (deteriorating)"
    cash_multiplier: 0.80
  
  management_guidance_credibility:
    credibility_grade: "C"
    credibility_basis: "Maiden call; headline financials verified; 'zero bad debt' contradicted by ECL; no multi-quarter track record"
    guided_revenue_growth: "19 hubs: 10 FY27 / 8 FY28 / 1 FY29"
    capex_guidance_fy27_cr: 25
    margin_guidance: "NOT FOUND"
    top_growth_trigger_1: "Hub expansion (19 new hubs, 3 near-term)"
    top_growth_trigger_2: "Receivables collection fix"
    top_growth_trigger_3: "AI-embryology uplift (claimed +8%)"
    delivery_track_record: "None (maiden call, PENDING)"
  
  emerging_moat_assessment:
    em_score: 13
    em_classification: "MODEST"
    active_moat_categories: "G1 (War chest, Strong); H2 (Strategic partnerships, Moderate); R1 (Regulatory tailwind, Moderate)"
    evidence_mix: "documented 6, claim 12, inference 5 — mostly claim"
    strategic_asset_monopoly: "Moderate: ART licensing + founder brand + GAAT IP, but replicable distribution"
    primary_catalyst_12m: "3 new hubs opening (South Delhi, Nagpur, Gurgaon) in next 1-2 months"
    secondary_catalyst_12m: "3 international spokes (Nigeria, Sydney, Paris)"
    tertiary_catalyst_12m: "Receivables days reversal from pricing changes"
    capex_embedded_growth_pct: 335
    combined_assessment: "AVERAGE"
  
  promoter_governance:
    promoter_flag: "CONCERN"
    contingent_tax_exposure_cr: 49.75
    promoter_pledge_pct: 0.0
    key_governance_concern: "Promoter sits on Audit Committee, chairs Risk Committee; largest RPT beneficiary"
    deal_breaker_status: "Multiple mid-term independent-director exits within 3 years"
    transition_evidence: "External CFO (Oct 2024), external CS (Sept 2024), credentialed board reconstitution"
  
  peer_reference_data:
    hcg_receivable_days: "105-115 (vs Gaudium ~187)"
    hcg_international_patient_mix_pct: 3.5
    rainbow_international_revenue_cr: 28.9
    rainbow_ivf_revenue_cr: 61.4
    kaya_collection_model: "Prepaid loyalty (vs Gaudium receivables-heavy)"
    peer_financial_medians: "NOT FOUND"
  
  market_tam_assessment:
    tam_conservative_cr: 14560
    tam_realistic_cr: 19665
    sam_cr: 2017
    sam_pct_of_tam: 13.9
    current_sam_share_pct: 3.52
    revenue_headroom_x: 28.4
    runway_classification: "STRONG"
    som_3yr_cr: 161
    som_5yr_cr: 281
    som_implied_revenue_cagr_3yr_pct: 31.4
    som_implied_revenue_cagr_5yr_pct: 31.7
    management_tam_claim_cr: 11046
    tam_growth_pct: 13.13
    capacity_check_3yr: "Fits within 75% utilization"
    capacity_check_5yr: "Gap ~Rs 66.5 Cr; embryologist headcount not disclosed"
  
  ua_multiplier_qualifiers:
    listed_12m: false
    gate0_or_em: false
    fii_dii_lt3: false
    all_met: false
    ua_multiplier_applied: false
  
  cash_conversion_rating_data:
    block_b_score: 5
    block_b_trigger: "deal-breaker #2 (max GOOD)"
    cash_conversion_determination: "INDETERMINATE (deteriorating)"
    cash_multiplier_applied: 0.80
    receivables_flag_evidence: "Turnover 6.34x (FY24) to 3.17x (FY25), -50%; 56.2% aged >6mo; first ECL Rs 9.83L FY25"
    working_capital_flag_evidence: "WC days 11.3 (FY23) to 156.3 (FY26), +145dy; receivables grew 59x vs revenue 2.4x; cumulative CFO/PAT 64.1%, FCF/PAT 14.3%"
    rating_agency_wc_quote: "NOT FOUND"

conflicts:
  - field: "Sector Classification"
    value_a: "Pharma / CDMO"
    anchor_a: "manifest.yaml"
    value_b: "Hospitals / dialysis / healthcare services, 35x"
    anchor_b: "fttcp-deliberation.md p.14 (operator correction authority)"
    used: "Hospitals / dialysis (deliberation authority supersedes manifest)"
  
  - field: "Reported vs Operating ROCE (FY26)"
    value_a: "20.11% (reported)"
    anchor_a: "B01-gate0.yaml"
    value_b: "37% (operating, surplus cash removed)"
    anchor_b: "fttcp-deliberation.md Override 1 p.38-39"
    used: "37% operating ROCE (operator override authority; surplus cash valued separately)"
  
  - field: "Zero Bad Debt Claim"
    value_a: "Zero bad debt (management call)"
    anchor_a: "B05-concall.yaml"
    value_b: "Rs 31.97 L ECL allowance recognised FY26"
    anchor_b: "Consolidated CF audited results (results PDF p.18)"
    used: "Used as credibility downgrade evidence (C-grade), not as conflicting input value"
  
  - field: "International Patient Mix Claim"
    value_a: "25-30% (management claim)"
    anchor_a: "B05-concall.yaml guidance"
    value_b: "1.03%-6.65% RHP patient-country data OR NIL forex earnings FY24-25"
    anchor_b: "B04-bizmodel.yaml; B06-peers.yaml; AR foreign exchange"
    used: "Flagged as unverified; not used for valuation input"

unresolved:
  - field: "Revenue Growth 3-Year CAGR"
    why: "FY23 and FY24 audited revenue figures not in extracted results PDFs; only FY25, FY26 available"
    where_it_might_be: "Full results PDF file (not fully extracted); earlier audited annual reports or ARs"
    alternative: "1-year growth FY25-FY26 at 47.6% available; deliberation guidance covers forward modeling"
  
  - field: "PAT Growth 3-Year CAGR"
    why: "FY23 and FY24 audited PAT figures not in extracted results PDFs"
    where_it_might_be: "Full results PDF file; earlier audited annual reports or ARs"
    alternative: "1-year growth FY25-FY26 at 27.8% available"
  
  - field: "Forward Margin Guidance (Target Band)"
    why: "No explicit management margin band or trajectory disclosed in available sources"
    where_it_might_be: "Investor presentations, concall transcripts (not fully provided)"
    alternative: "FY26 realized: consolidated EBITDA 36.13%, PAT 23.47%; standalone 50.81%"
  
  - field: "Peer Financial Medians (P/E, EV/EBITDA, P/B, Growth, ROCE)"
    why: "No structured peer financial statements or results tables provided; only qualitative concall commentary"
    where_it_might_be: "Peer audited annual reports, equity research reports"
    alternative: "Qualitative peer assessment (HCG, Rainbow, Kaya concalls) available for context; not for valuation medians"
  
  - field: "Rating Agency WC / Cash Flow Verbal Attestation"
    why: "Rating PDF not provided; rating/ folder marked empty in task"
    where_it_might_be: "External rating agency files (Crisil, ICRA, Acuite, India Ratings)"
    alternative: "None; rating agency commentary unresolved per task instruction"
  
  - field: "Forward Guidance Realization (Hub Openings, Receivables Fix)"
    why: "All major forward promises marked PENDING; zero subsequent quarter data available as of run date"
    where_it_might_be: "Q1 FY27 results (due ~Aug-Sep 2026, post-run-date 2026-07-16)"
    alternative: "Tracked as monitorables (B03, B07) for future verification; not usable as current input"

rating_wc_quote: "NOT FOUND — rating PDF not provided; rating/ folder empty"
ua_qualifiers:
  listed_12m: false
  gate0_or_em: false
  fii_dii_lt3: false
  all_met: false
credibility_grade: "C"
```
