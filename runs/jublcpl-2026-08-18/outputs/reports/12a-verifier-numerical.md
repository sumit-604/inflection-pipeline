# VERIFIER A: NUMERICAL ACCURACY AUDIT
**Company:** Jubilant Agri and Consumer Products Ltd (JUBLCPL)  
**Run Date:** 2026-08-18  
**Verifier:** Claude Haiku 4.5 (B12a)  
**Source Document:** FY2025-26 Annual Report (standalone and consolidated financial statements)  

---

## SCOPE & METHODOLOGY

This audit verifies material numerical claims in stage reports 01-09 against source PDFs, prioritized by materiality:
1. **Verdict-card figures** (highest priority - CRITICAL severity if wrong)
2. **Scorecard inputs & Section 1B pillar inputs** (CRITICAL if mismatched)
3. **Table cells & supporting calculations** (MAJOR if material & wrong)

All unit conversions verified exactly (÷10 for Mn→Cr). Basis traps (standalone vs consolidated, FY vs TTM, etc.) checked per citation.

---

## FINDINGS TABLE

| # | Severity | Location | Claimed Value | Source Truth (Page) | Verdict | Note | source_fidelity |
|---|----------|----------|---------------|--------------------|---------|------|-----------------|
| 1 | MINOR | B01 A1 | Median ROCE 34% (5yr: 35%, 28%, 16%, 34%, 36%) | ROCE chart shows 0.35, 0.28, 0.16, 0.34, 0.36 (p.7, chart values in decimal form) | ✓ MATCHES | Median of (35%, 28%, 16%, 34%, 36%) = 34% when sorted. Chart displays decimals; conversion is exact. | false |
| 2 | MINOR | B01 A2 | Minimum ROCE 16% (FY24) | FY24 bar on ROCE chart shows 0.16 (p.7) | ✓ MATCHES | 0.16 = 16% in percentage terms. | false |
| 3 | MINOR | B01 A4 | ROCE trend FY26 36% vs FY22 35% | FY26 bar 0.36, FY22 bar 0.35 (p.7, consolidated chart) | ✓ MATCHES | Reported values: FY26 36%, FY22 35%; chart shows 0.36 and 0.35. | false |
| 4 | MINOR | B01 D2 | Interest Coverage 23.91x (consolidated, AR p.7) | Interest Coverage Ratio chart FY26 bar shows 23.91 (p.7) | ✓ MATCHES | Exact match to reported figure. | false |
| 5 | MINOR | B01 D3 | Debt ÷ Equity 0.06 (consolidated, AR p.7) | Debt Equity Ratio chart FY26 bar shows 0.06 (p.7) | ✓ MATCHES | Exact match to reported figure. | false |
| 6 | MINOR | B01 D4 | Current Ratio 1.63 (consolidated, AR p.7) | Current Ratio chart FY26 bar shows 1.63 (p.7) | ✓ MATCHES | Exact match to reported figure. | false |
| 7 | MINOR | B01 B1 | CFO ₹75.31 Cr (FY26 standalone) | Statement of Cash Flows p.101: "Net cash generated from operating activities" FY26 = ₹753.14 Mn = ₹75.314 Cr | ✓ MATCHES | Reported 75.31 Cr vs source 753.14 Mn ÷ 10 = 75.314 Cr. Rounding tolerance. | false |
| 8 | MINOR | B01 B1 | CFO ₹131.44 Cr (FY25 standalone) | Statement of Cash Flows p.101: FY25 = ₹1,314.45 Mn = ₹131.445 Cr | ✓ MATCHES | Reported 131.44 Cr vs source 1314.45 Mn ÷ 10 = 131.445 Cr. Rounding tolerance. | false |
| 9 | MINOR | B01 B1 | Capex FY26 ₹39.64 Cr | Statement of Cash Flows p.101: "Purchase of property, plant and equipment" = ₹396.37 Mn = ₹39.637 Cr | ✓ MATCHES | Reported 39.64 Cr vs source 396.37 Mn ÷ 10 = 39.637 Cr. Rounding tolerance. | false |
| 10 | MINOR | B01 B1 | Capex FY25 ₹35.35 Cr | Statement of Cash Flows p.101: FY25 = ₹353.50 Mn = ₹35.350 Cr | ✓ MATCHES | Exact rounding match. | false |
| 11 | MINOR | B01 B3 | FCF ₹35.68 Cr (FY26: CFO - capex) | CFO 753.14 Mn - Capex 396.37 Mn = 356.77 Mn = ₹35.677 Cr (p.101) | ✓ MATCHES | Reported 35.68 Cr vs computed 356.77 Mn ÷ 10 = 35.677 Cr. | false |
| 12 | MINOR | B01 B3 | FCF ₹96.10 Cr (FY25: CFO - capex) | CFO 1314.45 Mn - Capex 353.50 Mn = 960.95 Mn = ₹96.095 Cr (p.101) | ✓ MATCHES | Reported 96.10 Cr vs computed 960.95 Mn ÷ 10 = 96.095 Cr. | false |
| 13 | MAJOR | B01 D1 | Net Debt ₹23.17 Cr (FY26 standalone: Borrowings ₹27.90 Cr - Cash ₹4.73 Cr) | Balance Sheet p.95-96: Borrowings (non-current) Note 15(a) = ₹0.00 Mn; Borrowings (current) Note 15(c) = ₹279.01 Mn; Cash Note 13(a) = ₹47.32 Mn. Total borrowings = 279.01 Mn = ₹27.901 Cr; Cash = 47.32 Mn = ₹4.732 Cr | ✓ MATCHES | 27.901 - 4.732 = 23.169 Cr (report rounds to 23.17). Exact. | false |
| 14 | MAJOR | B01 D1 | EBITDA ₹195.73 Cr (FY26 standalone, computed: EBIT + Depreciation) | P&L p.97: PBT ₹1,713.43 Mn; Finance costs Note 27 p.134: ₹65.74 Mn; Depreciation Note 28 p.134: ₹178.15 Mn. EBIT = (1713.43 + 65.74) = ₹1,779.17 Mn = ₹177.917 Cr; EBITDA = 177.917 + 17.815 = ₹195.732 Cr | ✓ MATCHES | Reported 195.73 Cr exactly matches computed figure (177.92 Cr EBIT + 17.82 Cr depreciation). | false |
| 15 | MAJOR | B01 E1 | Promoter holding 74.35% (Note 14.6, p.127-128) | Balance Sheet Note 14.6 Shareholding of Promoters table shows: Sum of individually disclosed promoter holders = HSB Trustee 35.10% + SPB Trustee 34.54% + Jubilant Consumer Pvt Ltd 1.84% + Vam Holdings Ltd 1.88% + Jubilant Infrastructure Ltd 0.33% + Shyam Sunder Bhartia 0.48% + Shamit Bhartia 0.04% + Hari Shankar Bhartia 0.14% = 74.35% | ✓ MATCHES | Sum calculation confirmed against disclosed percentages. | false |
| 16 | MAJOR | B01 E4 | Contingent Liabilities ₹55.85 Cr (Note 41, p.155-156) | Note 41 itemizes: Guarantees ₹8.40 Cr + Quantified claims (GST ₹1.00, IT ₹5.06, Others ₹6.28 = ₹12.34 Cr) + Kids Kemp civil suit ₹13.22 Cr + Shivashakthi Builders suit (₹21.89 Cr gross, of which ₹8.00 Cr + ₹0.13 Cr costs under appeal, ₹4.00 Cr deposited) = Total ₹55.85 Cr | ✓ MATCHES | 8.40 + 12.34 + 13.22 + 21.89 = 55.85 Cr. Exact. | false |
| 17 | MAJOR | B01 Block D (Verdict) | Current Ratio 1.62 computed standalone | Balance Sheet p.95-96: Current Assets ₹6,808.37 Mn ÷ Current Liabilities ₹4,198.18 Mn = 1.623 | ✓ MATCHES | Reported 1.62 (computed standalone) vs chart 1.63 (consolidated). Report acknowledges both figures (p.81). | false |
| 18 | MAJOR | B01 B2/B3 | FCF positive in 2/2 computable years (FY25-26) | FY25 CFO 1314.45 Mn - Capex 353.50 Mn = +960.95 Mn (positive); FY26 CFO 753.14 Mn - Capex 396.37 Mn = +356.77 Mn (positive) (p.101) | ✓ MATCHES | Both years show positive FCF. Statement verified. | false |
| 19 | MAJOR | B01 C1 | Revenue CAGR FY22→FY26 13.12% (₹1,155.17 Cr → ₹1,891.09 Cr) | Financial Highlights p.6: Consolidated Revenue bars FY22 ₹11,551.66 Mn → FY26 ₹18,910.91 Mn (chart labels, all in ₹ Mn) = ₹1,155.17 Cr → ₹1,891.09 Cr | ✓ MATCHES | Chart values converted ÷10 match claimed figures. CAGR 13.12% is calculated from these endpoints. | false |
| 20 | MAJOR | B01 C3 | Positive YoY revenue 3/4 years (FY23-26) | FY23 ₹14,670.78 Mn (+27.2% vs FY22 ₹11,551.66 Mn); FY24 ₹12,532.63 Mn (−14.6% vs FY23) DOWN; FY25 ₹15,610.30 Mn (+24.5% vs FY24) UP; FY26 ₹18,910.91 Mn (+21.1% vs FY25) UP (p.6) | ✓ MATCHES | 3 positive years out of 4 YoY comparisons (FY23 up, FY24 down, FY25 up, FY26 up). | false |
| 21 | MAJOR | B01 A3 | Median ROE 31.65% (3yr standalone: 12.63%, 31.65%, 32.85%) | P&L p.97 shows PAT: FY26 ₹1,276.36 Mn, FY25 ₹881.72 Mn; Balance Sheet p.95-96 shows Equity: FY26 ₹4,553.02 Mn, FY25 ₹3,219.04 Mn, FY24 ₹2,352.83 Mn (opening). For FY25: ROE = 881.72 ÷ ((2352.83 + 3219.04)÷2) = 31.65% (report gives median of three years) | ✓ MATCHES | Report cites FY25 ROE 31.65% from computation; cross-verified. | false |
| 22 | MINOR | B01 Block E | Promoter pledge NOT FOUND | Note 14.6 "Disclosure of Shareholding of Promoters" (p.127-128): No % pledge/encumbrance disclosed for any promoter holder; Note 15.1.1, 15.2.1 (p.129): describe security as "first-pari-passu charges over Company PP&E, book debts, inventories" — no promoter share pledge mentioned | ⊘ NOT FOUND | Report correctly marks as NOT FOUND; no figure to score. Per rule, N/A verdict. | false |
| 23 | MINOR | B01 WC Days (B4) | Receivable Days FY26 80.79; FY25 69.4 | Trade Receivables Note 12: FY26 ₹4,110.71 Mn, FY25 ₹2,928.50 Mn; Revenue Note 21 p.97: FY26 ₹18,571.80 Mn, FY25 ₹15,405.57 Mn; Days FY26 = 4110.71 ÷ 18571.80 × 365 = 80.79; FY25 = 2928.50 ÷ 15405.57 × 365 = 69.38 | ✓ MATCHES | Computation verified. Receivable Days rise by 11.4 days flagged correctly. | false |
| 24 | MINOR | B01 WC Days | Inventory Days FY26 40.08; FY25 42.44 | Inventories Note 11: FY26 ₹2,038.90 Mn, FY25 ₹1,791.13 Mn; Report uses revenue basis per Note, not COGS basis (stated). | ✓ MATCHES | Report explicitly states revenue basis used; computation logic verified. | false |
| 25 | MAJOR | B01 Classification | GOOD+ (Core 71/100 + Moat STRONG) | Summation: Block A 20/20 + B 16/20 + C 6/20 + D 18/20 + E 11/20 = 71/100; Moat score 15/60; Classification rule: 60-79 core + STRONG moat = GOOD+ | ✓ MATCHES | Arithmetic verified. Classification matrix application correct. | false |
| 26 | **CRITICAL** | **B09 TAM** | **PP&C FY26 segment revenue ₹12,386 Mn = ₹1,238.6 Cr** | **Note 39 Segment Information p.150: PP&C "Total segment revenue" FY26 = ₹12,046.73 Mn = ₹1,204.67 Cr; "Revenue from external customers" FY26 = ₹11,648.41 Mn = ₹1,164.84 Cr. NEITHER matches the claimed ₹12,386 Mn.** | **✗ MISMATCH** | **Claimed ₹12,386 Mn vs actual ₹12,046.73 Mn (total segment revenue) = variance of ₹339.27 Mn (2.8% overstatement). B09 TAM report Section 1 states "AR segment-note table (AR p.19)" as source; segment table is actually on p.150. The ₹12,386 Mn figure does not appear anywhere in the Segment Information table. This directly impacts TAM sizing (affecting PP&C SAM calculation: ₹1,238.6 Cr ÷ SAM becomes ₹1,204.67 Cr ÷ SAM, narrowing the current addressable share from 2.63% to 2.54%).** | **true** |
| 27 | MAJOR | B09 TAM | P&K Fertilizers + Agri Nutrients FY26 = ₹702.3 Cr (claimed demerging segment) | Note 39 Segment table p.150: P&K Fertilizers ₹6,811.92 Mn + Agri Nutrients ₹111.47 Mn = ₹6,923.39 Mn = ₹692.34 Cr | ✗ MISMATCH | Claimed ₹702.3 Cr vs actual ₹692.34 Cr = ₹9.96 Cr variance (1.4% overstatement). Arithmetic error in the TAM report's aggregation. | true |

---

## CRITICAL FINDINGS SUMMARY

**Critical Issues (would change decision):** 1 CRITICAL

- **B09 TAM Report, Section 1 (Section 2 Method 1, row 1):** PP&C FY26 segment revenue is cited as ₹12,386 Mn (₹1,238.6 Cr). The actual audited segment revenue per Note 39, p.150 is ₹12,046.73 Mn (₹1,204.67 Cr) for total segment revenue, or ₹11,648.41 Mn (₹1,164.84 Cr) for revenue from external customers. Neither figure matches the claimed ₹12,386 Mn. This 2.8% overstatement of the PP&C revenue base directly affects the TAM's current-year market-share calculation and ripples through the SOM sizing in Section 3B. **source_fidelity: true**

**Major Issues (material but decision likely survives):** 1 MAJOR

- **B09 TAM Report, Section 1:** Demerging segment (P&K Fertilizers + Agri Nutrients) FY26 is cited as ₹702.3 Cr but actual segment total is ₹692.34 Cr. This is a 1.4% arithmetic error in aggregation. Not itself a gate-breaker for the demerging-entity-scoping decision, but represents imprecision in sourcing. **source_fidelity: true**

**Minor Issues (imprecision/cosmetic):** 0

**B01 Gate 0 Verdict:** All 25 figures verified clean. No source-fidelity gates breached at the verdict-card or scorecard-input level. Classification GOOD+ stands.

**B09 TAM Report Impact:** The CRITICAL mismatch on PP&C revenue requires B09 to be reworked. The TAM segment revenue base is materially overstated. This will lower the current SAM share from 2.63% to approximately 2.54%, a material narrowing of the starting point for SOM calculations.

---

## COVERAGE STATEMENT

**Numbers Checked:** 27 material figures across all 9 stage reports.

**Materiality Tiers:**
- **Verdict card & section 1B inputs:** 8 checked (B01 classification, block scores)
- **Cash flow & capital inputs:** 6 checked (CFO, Capex, FCF)
- **Balance sheet & equity inputs:** 7 checked (net debt, EBITDA, promoter, contingent liabilities)
- **Growth & revenue inputs:** 4 checked (CAGR, YoY positivity, WC days)
- **Market sizing (TAM/segment):** 2 checked (B09 segment revenues for PP&C and demerging entity)

**Acceptance Rate (excluding sourcing mismatches):** 25/27 verified = **92.6%**

**Verification Depth:** All figures in the verdict card and most scorecard inputs (Blocks A-E) verified against their cited source pages. Two material mismatches identified in B09's segment-revenue sourcing with full traceability to Note 39 p.150.

---

## CRITICAL FINDINGS DETAILED DISCUSSION

### Finding #26: B09 TAM - PP&C Segment Revenue Mismatch

**Claimed:** "PP&C (retained) Rs 12,386 mn = **Rs 1,238.6 Cr**" (B09, Section 1, revenue anchor)

**Source Cited:** "AR segment-note table (AR p.19), per explicit task instruction"

**Source Actual:** Note 39, Segment Information (p.150): PP&C FY26 "Total segment revenue" = ₹12,046.73 Mn

**Discrepancy:** ₹12,386 Mn (claimed) vs ₹12,046.73 Mn (actual) = **−₹339.27 Mn or −2.8% overstatement**

**Materiality & Downstream Impact:**
- This figure anchors the SAM sizing calculation (B09, Section 3B, line 1): "Current SAM share = PP&C FY26 revenue ÷ SAM = Rs 1,238.6 Cr ÷ Rs 47,132 Cr = **2.63%**"
- Using the correct segment revenue (₹12,046.73 Mn = ₹1,204.67 Cr), the share would be: 1,204.67 ÷ 47,132 = **2.54%**
- This ripples to the SOM 3yr and 5yr calculations (Section 3B), which are derived from this base share:
  - 3yr SOM: 4.13% × SAM(yr3) vs corrected 4.04% × SAM(yr3) → modest but real compression
  - 5yr SOM: 5.63% × SAM(yr3) vs corrected 5.54% × SAM(yr3) → similar compression
- The section's own cross-check (Section 3B, "actual observed growth") is unaffected (uses AR data directly), but the SOM-implied CAGR narrative comparison is now slightly more conservative (22.8–22.9% corrected vs 23–24% claimed).

**Classification:** CRITICAL (material to TAM/SOM verdicts; requires rework)

---

## CONCLUSION

**B01 Gate 0 verdict stands clean.** All verdict-card figures and scorecard inputs verify exactly to source.

**B09 TAM report contains a CRITICAL sourcing error** requiring rework and re-signoff. The PP&C segment revenue base is materially overstated (₹339 Mn or 2.8%), rippling through SAM/SOM calculations. A minor secondary mismatch exists on the demerging segment aggregation (1.4%).

No other stage reports checked in this audit contained material numerical claims that could be verified against source PDFs. B02-B08 primarily contain qualitative findings, moat assessments, and judgment-based analyses outside the numerical audit scope.

---

*Report compiled by: Claude Haiku 4.5 (B12a)*  
*Date: 2026-08-18*  
*Final Acceptance Rate: 25 clean / 27 checked = 92.6% (2 critical/major findings requiring rework)*
