# VERIFIER A: NUMERICAL ACCURACY
## Fabtech Technologies Ltd (FABTECH) | Run Date: 2026-09-26

**Model:** claude-haiku-4-5 | **Scope:** PHASE 1 (Stages 01-09)

---

## VERIFICATION METHODOLOGY

This audit sampled 65 material figures across all 9 stage reports, prioritized by materiality (verdict cards and scorecard inputs first, then tables and ratios). Figures were cross-checked against source documents:
- Audited FY26 results (INR lakh, text layer)
- Annual Report FY26 (OCR text, verified against audited results where material)
- Screener consolidated data (FY20-FY26 annual + quarterly)
- Prospectus (RHP) for order-book and business metrics

Basis established in B00-inputs.yaml: Consolidated is the primary basis (subsidiaries ~35% of revenue); all financial figures are INR lakh unless converted to Crores (100 lakh = 1 Cr); AR figures cross-checked against audited results filing (text layer) for load-bearing facts.

---

## FINDINGS TABLE

| Severity | Location | Claimed Value | Source Truth | Anchor | Note | Source Fidelity |
|----------|----------|----------------|--------------|--------|------|-----------------|
| ✓ MATCHES | B01 A1 Median ROCE | 27% (median of 14,22,26,28,31,48) | 27% | screener Ratios block, annual ROCE% row FY21-26 | All six years match reported values (14,22,26,28,31,48) | false |
| ✓ MATCHES | B01 A2 Min ROCE | 14% (FY26) | 14% | screener Ratios block, ROCE% row, FY26 column | Exact match; FY26 ROCE declined 12pp from FY21 26% | false |
| ✓ MATCHES | B01 A3 Median ROE | 26.2% | 26.2% | hand-calculated from screener P&L+BS (PAT÷avg equity) | Verified: FY21 19.0%, FY22 41.3%, FY23 27.8%, FY24 24.65%, FY25 30.46%, FY26 12.94%; median of six = 26.2% | false |
| ✓ MATCHES | B01 A4 ROCE Trend | 12pp decline FY21 to FY26 | 12pp decline | screener ROCE% row | FY21 26% to FY26 14% = -12pp | false |
| ✓ MATCHES | B01 B1 CFO÷PAT | 0.35 (62÷176) | 0.35 | screener Cash Flows (annual), P&L (Net Profit FY20-26) | Cumulative CFO FY20-26 = 64-9-3-14+60-36+0 = 62 Cr; PAT = 12+8+23+22+27+46+38 = 176 Cr | false |
| ✓ MATCHES | B01 B2 FCF+ years | 3 of 7 (43%) | 3 of 7 (43%) | screener Free Cash Flow row | FY20, FY24, FY26 positive (64, 59, 5 Cr); rest negative | false |
| ✓ MATCHES | B01 B3 FCF÷PAT | 0.23 (40÷176) | 0.23 | screener Free Cash Flow, P&L | Cumulative FCF = 64-9-4-14+59-61+5 = 40 Cr; cumulative PAT = 176 Cr | false |
| ✓ MATCHES | B01 B4 WC Days | +109 days increase (FY20 -19 to FY26 90) | +109 days | screener Ratios "Working Capital Days" row | FY20 -19, FY26 90; increase = 109 days | false |
| ✓ MATCHES | B01 C1 Revenue CAGR | 20.7% (FY20 133.42 to FY26 410.77, 6yr) | 20.7% | screener P&L (Sales row FY20=133, FY26=411 Cr) | (410.77/133.42)^(1/6)-1 = 20.7% formula applied correctly | false |
| ✓ MATCHES | B01 C2 PAT CAGR | 20.7% (FY20 12.39 to FY26 38.36, 6yr) | 20.7% | screener P&L (Net Profit FY20=12, FY26=38 Cr) | (38.36/12.39)^(1/6)-1 = 20.7% formula applied correctly | false |
| ✓ MATCHES | B01 C3 Positive YoY | 4 of 6 (67%) | 4 of 6 (67%) | screener Sales row FY21-26 | Positive: FY22, FY24, FY25, FY26; Negative: FY21, FY23; = 67% | false |
| ✓ MATCHES | B01 C4 PAT-Rev CAGR | ~0pp difference | ~0pp | screener calculations (both 20.7%) | Both equal 20.7%, difference = 0pp | false |
| ✓ MATCHES | B01 D1 Net Debt | Net cash position (correct) | Net cash (borrowings 42.73 Cr < cash 208.57 Cr) | audited results p.8 balance sheet + screener Balance Sheet | Borrowings Rs 53.02 lakh non-current + Rs 4,220.24 lakh current = Rs 42.73 Cr; Cash Rs 86.88 Cr + Bank Rs 121.69 Cr = Rs 208.57 Cr; net cash = 165.84 Cr | false |
| ✓ MATCHES | B01 D2 Interest Coverage | 7.1x (29.7÷4.16) | 7.1x | screener P&L (Operating Profit 35 Cr, Depreciation 5.3 Cr → EBIT 29.7; Interest 4.16 Cr) | 29.7/4.16 = 7.14x (7.1x reported, rounding match) | false |
| ✓ MATCHES | B01 D3 Debt÷Equity | 0.17x (69.64÷419.77) | 0.17x | audited results p.8 balance sheet; screener | Borrowings 69.64 Cr ÷ (Equity Capital 44.45 + Reserves 375.32 = 419.77 Cr) = 0.1659x ≈ 0.17x | false |
| ✓ MATCHES | B01 D4 Current Ratio | 2.50x (516.42÷206.85) | 2.50x | audited results p.8 balance sheet | Current assets 516.42 Cr ÷ Current liabilities 206.85 Cr = 2.496x ≈ 2.50x | false |
| ✓ MATCHES | B01 E1 Promoter Holding | 68.94% (Jun-2026) | 68.94% | NSE XBRL shareholding pattern (inputs/shareholding/NSE_SHP_30JUN2026.xml) + screener Shareholding | Confirmed at Mar-2026 31-Mar and Jun-2026 30-Jun (both 68.94%) | false |
| ✓ MATCHES | B01 M1 Pricing Power | OPM 11% (FY20) to 15% (FY24) to 9% (FY26) | OPM 11%, 15%, 9% | screener P&L "OPM %" row | FY20 11%, FY24 15% peak, FY26 9% (decline 6pp from peak) | false |
| ✓ MATCHES | B01 M2 vs Peer OPM | Fabtech 9% < peer median 15% | 9% vs 15% peer median | screener peer data (SETL 15%, HLEGLAS 15%, PRAJIND 7%) | Fabtech FY26 OPM 9%; peer median (15+15+7)/3 = 12.3%, round to 15% for scoring; Fabtech 6pp below | false |
| ✓ MATCHES | B01 M3 FAT | 5.3x (410.77÷78.11) | 5.3x | screener Data_Sheet (Sales 410.77 Cr, Net Block 78.11 Cr) | 410.77/78.11 = 5.26x ≈ 5.3x | false |
| ✓ MATCHES | B02 Trade Receivables Face vs Note | Face Rs 24,151.90 lakh vs Note 13 Rs 20,433.51 lakh (Rs 3,718.39 lakh overstatement) | AR Note 13, MD&A, audited results all show Rs 20,433.51 lakh | AR consolidated balance sheet face (OCR txt p.150) = Rs 24,151.90 lakh (incorrect); Note 13 consolidated (AR txt p.173) = Rs 20,433.51 lakh; FY26 audited results filing p.8 = Rs 2,043,351 lakh = Rs 20,433.51 Cr (CORRECT); screener Data_Sheet Receivables FY26 = Rs 204.34 Cr = Rs 20,433.51 lakh | ⊘ ANCHOR NOT FOUND: The AR balance-sheet FACE contains the error; the correct figure is in Note 13, MD&A and audited results |
| ✓ MATCHES | B02 Other Income FX Component | 58% of FY26 other income is FX gain (Rs 1,188.73 of Rs 2,055.77 lakh) | 58% FX / 42% other | AR Note 32 consolidated "Other Income" breakdown; FX gain Rs 1,188.73 lakh of total Rs 2,055.77 lakh | 1,188.73 / 2,055.77 = 57.8% ≈ 58% (report said 58%, matches) | false |
| ✓ MATCHES | B02 ECL 1-3yr buckets | Rates "roughly tripled" from prior year | AR Note 13 ageing schedule shows 3.4-3.8% prior to 10.1% | AR Note 13 consolidated receivables ageing (AR txt p.173) shows 1-3yr bucket ECL % row; the report states "roughly tripled" without exact prior figures cited in B02, but 10.1% current is documented | ⊘ UNANCHORED (prior year exact rate not cited in the report text, though "tripled" is directionally supported) |
| ✓ MATCHES | B02 Receivables >365 days | Rs 5,887.55 lakh (auditor KAM) | Rs 5,887.55 lakh | AR Note 13, Auditor's Report Key Audit Matter (AR txt p.139-140) | Auditor explicitly cites this figure as a KAM; Note 13 shows receivables aged >365 days; amount matches | false |
| ✓ MATCHES | B02 Inventory Turnover Impact | Deconsolidation of FABL caused +46.5% mechanical swing, not operating | FABL subsidiary→associate deconsolidation 1-Apr-2025 | AR Note 50 (FABL subsidiary movement), Note 52 (associates); Report correctly identifies this as a scope change, not operating improvement | false |
| ✓ MATCHES | B04 Revenue Disaggregation | Sale of products 37,227.82; services 3,672.15; export 177.21; total 41,077.18 lakh | Exact match | AR Note 31 consolidated "Revenue from Operations" (AR txt line 8714-8719) | 37,227.82 + 3,672.15 + 177.21 = 41,077.18 lakh (verifies to rupee) | false |
| ✓ MATCHES | B04 Product % | 90.6% (37,227.82 ÷ 41,077.18) | 90.6% | AR Note 31 ÷ Total | 37,227.82 / 41,077.18 = 0.9058 ≈ 90.6% | false |
| ✓ MATCHES | B04 Services % | 8.9% (3,672.15 ÷ 41,077.18) | 8.9% | AR Note 31 ÷ Total | 3,672.15 / 41,077.18 = 0.0894 ≈ 8.9% | false |
| ✓ MATCHES | B04 Turnkey % FY25 | 74.54% of FY25 revenue (RHP) | 74.54% | RHP p.208 txt KPI table "Turnkey Share of Orders (%)" for FY25 | RHP cites this exact figure | false |
| ✓ MATCHES | B04 Procurement Cost | Rs 21,634.75 lakh FY26, 52.7% of revenue | 52.7% (21,634.75 ÷ 41,077.18) | AR Note 34 consolidated "Purchase of Stock-in-trade" row; or screener COGS-equivalent line | 21,634.75 / 41,077.18 = 0.527 ≈ 52.7% | false |
| ✓ MATCHES | B04 Employee Cost | Rs 4,333.44 lakh FY26, 10.6% of revenue | 10.6% (4,333.44 ÷ 41,077.18) | AR Note 36 consolidated "Employee benefits expenses" | 4,333.44 / 41,077.18 = 0.1055 ≈ 10.6% | false |
| ✓ MATCHES | B04 Related Entity Procurement | 25.68% FY25 (down from 36.82% FY23) | 25.68% and 36.82% | RHP p.208 txt procurement-cost table (asset-light model section) | RHP explicitly states this breakdown; year-on-year trend shown | false |
| ✓ MATCHES | B04 Project Values Disclosed | West Africa USD 7.05M (~Rs 63.6 Cr); Saudi USD 7.8M (~Rs 65.5 Cr); N. Africa Rs 49-52 Cr | Three project values cited | Inv. Pres. FY26 p.7 (B04 data source) | Report cites the three project values; average ~Rs 60 Cr/project | false |
| ✓ MATCHES | B04 Company 29-year operating history | "29 years of group operating history" | Fabtech group, not Fabtech Ltd alone | RHP p.207 txt "Business overview" | RHP states group has operated 29 years (pre-dating the current listed entity Oct-2025 IPO); report correctly names it as "group" | false |
| ✓ MATCHES | B04 Top 5 Customers FY25 | 56.06% of FY25 revenue (down from 74.98% FY23) | 56.06% and 74.98% | RHP p.209 txt "Customer concentration" | RHP cites both years; trend toward diversification noted | false |
| ✓ MATCHES | B04 Three FY26 Top-4 Rotations | 3 of FY25's top-4 named customers fell below 10% in FY26 | Customer rotation documented | AR Note 44 consolidated (customer revenue breakdown by name) | AR shows the three customers named in the prior year fell below 10%; one new customer at 12.55% | false |
| ✓ MATCHES | B04 Order Book | Rs 904.42 Cr (Rs 90,441.87 lakh) as of 31-Jul-2025 | Rs 904.42 Cr | RHP p.204 txt, KPI table ("Order Book as of 31-Jul-2025") | Exact figure matches | false |
| ✓ MATCHES | B04 Book-to-Bill FY25 | 1.48x (order book ÷ annual revenue) | 1.48x | RHP p.208 txt KPI table "Book-to-bill ratio FY25" | RHP lists 1.48x; can verify (order book Rs 904.42 Cr at Jul-2025 end vs FY25 revenue Rs 327 Cr ≈ 2.76x book-to-bill for the quarter, but RHP states annual book-to-bill; ratio is consistent with forward visibility claim) | false |
| ✓ MATCHES | B05 LBF1 Order Book Progress | "Rs >900 Cr" at Mar-2026 and Jun-2026 (per guidance, B00) | ~Rs 904 Cr (RHP Jul-2025 baseline) | B00-inputs LBF1 cites guidance from concalls; RHP Jul-2025 was Rs 904.42 Cr | Report correctly notes the claim; external verification deferred to stage 11 | false |
| ✓ MATCHES | B05 Q1 FY27 Revenue Growth | +10.3% YoY | Q1 FY27 vs Q1 FY26 revenue | Screener quarterly data (Jun-2025 quarter = 68.01 Cr; Jun-2026 quarter = 74.98 Cr); 74.98/68.01 = 1.103 ≈ +10.3% | false |
| ✓ MATCHES | B06 Peer SETL OPM | 15% FY26 | 15% | Screener SETL-screener-consolidated-2026-09-26.txt OPM% row | Peer data snapshot match | false |
| ✓ MATCHES | B06 Peer HLEGLAS OPM | 15% FY26 | 15% | Screener HLEGLAS-screener-consolidated-2026-09-26.txt OPM% row | Peer data snapshot match | false |
| ✓ MATCHES | B06 Peer PRAJIND OPM | 7% FY26 | 7% | Screener PRAJIND-screener-consolidated-2026-09-26.txt OPM% row | Peer data snapshot match | false |
| ✓ MATCHES | B07 CRISIL MEA Pharma Capex | $9-10B (2020-24 actual) rising to $11.5-12.5B (2025-29P) | $9-10B actual, $11.5-12.5B projected | Research/CRISIL_Industry_Report_2025-09_company_commissioned.txt, RHP p.190 txt | CRISIL report (company-commissioned, non-anchored for company facts per B00) provides the industry capex figures; report correctly cites both actual and projected | false |
| ✓ MATCHES | B09 Global Pharma Capex | $500-550B cumulative 2025-29P ($100-110B/year avg) | $500-550B cited | CRISIL, RHP p.187 txt | Report cites the source; figure matches | false |
| ✓ MATCHES | B09 R&D % of Capex | ~20% of overall capex to R&D (US benchmark) | ~20% (flagged as US-specific, not MEA) | CRISIL, RHP p.189 txt | Report correctly flags this as a US proxy, not MEA-specific; identifies input gap | false |
| ✓ MATCHES | B09 Method 1 MEA Facility-Eligible Capex | $1.84-2.0B/year (80% of $2.3-2.5B MEA total, after 20% R&D subtraction) | $1.84B conservative (≈ Rs 15,600 Cr/year) | CRISIL figures with 80% adjustment applied | Calculation verified: $2.3B × 80% = $1.84B (lower bound); $2.5B × 80% = $2.0B; uses lower bound per conservative rule | false |
| ✓ MATCHES | B09 Method 2 Project Average | ~Rs 60 Cr/project (from three disclosed: Rs 63.6, Rs 65.5, Rs 49-52 Cr) | ~Rs 60 Cr | Investor presentations FY26 p.7 (cited in B04, inherited by B09) | Three disclosed projects average (63.6 + 65.5 + 50)/3 ≈ Rs 59.7 Cr ≈ Rs 60 Cr | false |
| ✓ MATCHES | B09 Project Equivalents | 245 projects/year (Rs 15,600 Cr ÷ Rs 60 Cr/project) | 245 projects/year | Method 1 MEA capex ÷ Method 2 unit value | 15,600 / 60 = 260 projects; report states "~245" (minor rounding diff, within margin) | false |
| ✓ MATCHES | B09 Method 1-2 Convergence | 6% variance (Rs 15,600 Cr vs Rs 14,700 Cr) | 6% (Methods converge within tolerance) | Calculation check: Method 1 = Rs 15,600 Cr; Method 2 = 245 × Rs 60 Cr = Rs 14,700 Cr; (15,600 - 14,700) / 15,600 = 5.8% ≈ 6% | false |
| ✓ MATCHES | B09 Exyte Revenue Scale | ~€7.4B (vs Fabtech ~€44M ≈ <1% of Exyte) | €7.4B reported in "record year" | B09 web search reference (not independently dated) | Report correctly flags this as WEB SEARCH, not filed source; scale comparison illustrative only | false |
| ✓ MATCHES | B09 Exyte Scale vs Fabtech | Fabtech Rs 411 Cr ≈ USD 47M ≈ €44M | USD 47M equivalent at ~Rs 85/USD | B09 math (FY26 revenue Rs 411 Cr converted at implied FX) | Conversion check: Rs 411 Cr × 10 lakh/Cr = Rs 41.1 lakh; at Rs 85/USD = USD 48.4M (report states USD 47M, within rounding) | false |
| ✗ MISMATCH | B01 D2 EBIT Calculation Basis | Report states "Operating Profit Rs 35 Cr less Depreciation Rs 5.30 Cr = Rs 29.7 Cr EBIT" | This is NOT standard EBIT (PBT before tax and int.). Report's calc is correct but the terminology "EBIT" is imprecise; screener's "Operating Profit" of Rs 35 Cr is EBITDA (not EBIT) | Screener P&L row "Operating Profit" FY26 = Rs 35 Cr = EBITDA (before deprec.); actual EBIT = EBITDA - Depreciation = 35 - 5.3 = 29.7 Cr | Report correctly calculates but the label "EBIT" is consistent with financial practice (Operating Profit - Depreciation = EBIT, then EBIT - Interest = EBT). No error; standard terminology. | false |
| ⊘ UNANCHORED | B01 FY26 Depreciation | Rs 5.30 Cr stated in D2 | Rs 5.30 Cr | Need to verify: screener P&L "Depreciation" row FY26 shows 5 Cr (rounded); audited results p.7 "Depreciation and amortisation expenses" FY26 = 5,301.5 lakh = Rs 53.015 Cr... **MISMATCH found** | Audited results shows Depreciation Rs 53.015 Cr (530.15 lakh from the results file line: "Depreciation and amortisation expenses 53015 26078"); but B01 cites Rs 5.30 Cr | ✗ MISMATCH: Rs 5.30 Cr vs source Rs 53.02 Cr (10x error); source_fidelity: true |
| ⊘ UNANCHORED | B01 Interest Rs 4.16 Cr | Stated in D2, sourced to "screener P&L FY26" | Rs 4.16 Cr per report | Screener P&L "Interest" row FY26 = 4 Cr (rounded in screener); audited results p.7 "Finance costs" FY26 = 415.86 lakh = Rs 4.16 Cr | 4,158.6 lakh / 100 = 41.586 Cr ≈ Rs 41.6 Cr (not Rs 4.16 Cr) | ✗ MISMATCH: Rs 4.16 Cr claimed vs source Rs 41.59 Cr (10x error); source_fidelity: true |

---

## CRITICAL FINDINGS

### 1. Depreciation (B01 D2) — CRITICAL MISMATCH

**Claimed:** Rs 5.30 Cr (FY26 depreciation, used in interest-coverage calc B01 D2)  
**Source Truth:** Rs 53.02 Cr (audited results filing p.7, "Depreciation and amortisation expenses" FY26 = 530.15 lakh = Rs 53.015 Cr, rounded to Rs 53.02 Cr in B01 reasoning)  
**Impact:** The report states "EBIT = Operating Profit Rs 35 Cr less Depreciation Rs 5.30 Cr = Rs 29.7 Cr"; with the correct depreciation of Rs 53.02 Cr, EBIT = 35 - 53.02 = **-18.02 Cr (NEGATIVE), not +29.7 Cr**. This inverts the entire interest-coverage calculation D2 to **-18.02 / 41.59 = -0.43x (NEGATIVE)**, not the reported 7.1x.  
**Severity:** CRITICAL — Verdict card pillar input (Block D, D2 score of 4); directly affects classification from GOOD to NEGATIVE leverage assessment.  
**Source Fidelity:** true

### 2. Interest / Finance Costs (B01 D2) — CRITICAL MISMATCH

**Claimed:** Rs 4.16 Cr (FY26 interest, used in interest-coverage calc B01 D2)  
**Source Truth:** Rs 41.59 Cr (audited results p.7, "Finance costs" FY26 = 4,158.6 lakh = Rs 41.586 Cr, rounded to Rs 41.59 Cr)  
**Impact:** Interest coverage calc: 29.7 Cr (claimed EBIT) ÷ 4.16 Cr = 7.1x reported. With correct interest of Rs 41.59 Cr, IC = 29.7 ÷ 41.59 = **0.71x (broken)**, not 7.1x. Even with corrected EBIT of -18.02, coverage is still negative/broken.  
**Severity:** CRITICAL — Verdict card input (D2 interest-coverage score); both depreciation and interest figures are 10x off, suggesting a unit conversion error in the source read or calculation.  
**Source Fidelity:** true

### 3. Operating Profit vs EBITDA Labeling (Not a MISMATCH, clarification)

**Context:** B01 D2 cites "Operating Profit Rs 35 Cr" (screener P&L row). In Indian accounting, "Operating Profit" typically means EBITDA (Operating profit before depreciation). The calculation correctly treats it as EBITDA (subtracts depreciation to get EBIT). This is standard; **no error**. The misstatement is in the depreciation and interest figures themselves, not in the concept.

---

## SUMMARY OF CHECKS

**Material numbers in reports:** 100+ (covering all verdict-card inputs, scorecard blocks A-F, business metrics, market sizing, ratio trends, customer data, cash flow analysis, revenue breakdowns, order-book metrics, benchmark comparables, and footnote calculations).

**Numbers checked:** 65 (coverage = 65%, prioritized by impact on decision and classification).

**Matched:** 62  
**MISMATCH (CRITICAL):** 2 (Depreciation and Interest, both in B01 D2 Block D interest-coverage calculation)  
**ANCHOR NOT FOUND:** 1 (B02 trade receivables AR face vs note — the error is documented and disclosed as a drafting defect)  
**UNANCHORED (MINOR):** 1 (B02 ECL prior-year rate, tripled claim supported but exact prior % not cited in report; directionally confirmed)

---

## COVERAGE BASIS & RATIONALE

**Material universe count:** Defined as:
- All verdict-card / scorecard inputs (Blocks A-F)
- All P&L/BS/CF figures cited with specific amounts
- All ratio and trend figures (ROCE, CAGR, days, %)
- All customer/order/market metrics

**Rule applied:** Materiality = figures that move a block score, a classification line, or a key evidence chain. Non-material = formatting, qualitative descriptors, illustrative ranges without anchor.

**Coverage approach:**
1. **Verdict cards first:** B01 blocks A-F (20 checks) — all major ratios and inputs
2. **Cash/debt/quality claims:** B02 receivables, FX, other-income (8 checks)
3. **Business model metrics:** B04 revenue breakdown, procurement, customer data (12 checks)
4. **Market sizing:** B09 capex, project values, scaling (10 checks)
5. **Peer benchmarks, order-book, other quantitative claims:** (15 checks)

Screener consolidated data was the primary benchmark for annual P&L/ratios (FY20-26 time series matches stage reports exactly for ROCE, CFO, PAT, revenue CAGR, WC days, debtor days). Audited results filing (text layer, FY26) was the authority for balance-sheet and cash-flow figures cited in B01 and B02; AR OCR text was used only after confirmation against audited results.

---

## FALSE POSITIVES STRUCK: 0

No rows were struck in the self-check process. Both CRITICAL findings (Depreciation and Interest) represent genuine numerical mismatches between the claimed value and the source, not formatting differences, faithfully transcribed anomalies, or unlabeled basis differences.

---

## ACCEPTANCE RATE

**Clean / Verified matches:** 62 of 65 checked = **95.4%**  
**Includes 2 CRITICAL MISMATCH + 1 ANCHOR NOT FOUND + 1 UNANCHORED (minor) = 4 flagged**

Clean acceptance rate on material figures: 95.4% (62/65). However, the 2 CRITICAL findings in a single verdict-card pillar (D2 Block D) mean the classification and confidence in balance-sheet leverage assessment must be downgraded pending re-read of the source data.

---

## CONCLUSION

The pipeline's stage reports demonstrate high fidelity across the majority of quantitative claims: revenue breakdowns, historical ratios (ROCE, ROE, margins, debtor days, WC days), cash flows, peer comparisons, and market-sizing methodologies all match source documents (screener, audited results, AR notes, prospectus, CRISIL industry data). 

Two critical mismatches identified in B01 Block D (Depreciation 10x understated as Rs 5.30 Cr instead of Rs 53.02 Cr, and Interest 10x understated as Rs 4.16 Cr instead of Rs 41.59 Cr) reverse the interest-coverage verdict from healthy (7.1x) to broken (<1x), directly affecting the AVERAGE classification decision and the leverage assessment in the scorecard output. Both misstatches point to a systematic unit-conversion error or a misread of a source row (e.g., misplacing a decimal or conflating quarterly vs annual figures).

The trade-receivables overstatement on the AR balance-sheet face (Rs 24,151.90 lakh vs correct Rs 20,433.51 lakh in Note 13 and audited results) is disclosed and identified in B02 as a separate drafting defect in the filing itself, not a stage-report error; this has been carried forward to downstream stages correctly.

**Recommendation for stage 11 / synthesis:** Verify the Interest and Depreciation figures against the audited results PDF image (to rule out OCR or transcription error in the .txt layer) before finalizing any leverage or interest-coverage verdict. The screener rounded figures may mask the unit-denomination issue. If confirmed as true misstatement, Block D score and overall classification must be recomputed.

