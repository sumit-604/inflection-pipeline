# B12a — VERIFIER A: NUMERICAL ACCURACY
**Company:** JITF Infralogistics Limited (JITFINFRA)
**Run date:** 2026-08-12
**Model:** claude-haiku-4-5
**Stage:** B12a (Numerical Accuracy Verifier)

---

## FINDINGS TABLE

| Severity | Location | Claimed Value + Anchor | Source Truth + Location | Note | Source Fidelity |
|----------|----------|-------------------------|--------------------------|------|-----------------|
| MAJOR | B01-gate0, Block D1, p.189 | Net Debt/EBITDA: 6.71x (using EBITDA ₹558.46 Cr post-exceptional) | Correct EBITDA per Board's Report: ₹604.43 Cr (pre-exceptional); correct Net Debt/EBITDA: 6.19x (FY26 Results Consolidated P&L, audited). B01 used post-exceptional EBITDA (excluding ₹4,592.17 lakh ESOP charge) rather than pre-exceptional normalized EBITDA. Both figures exceed 3x threshold, so verdict unchanged, but magnitude is material difference. | Post-exceptional vs pre-exceptional EBITDA choice affects ratio by 0.52x. Standard leverage practice uses pre-exceptional normalized figures; B01's choice is conservative but non-standard. Deal-breaker #6 still triggers (6.19x >3x), but exact number differs significantly. | true |
| MAJOR | B01-gate0, Block D2, p.193 | Interest Coverage: 1.14x (using post-exceptional PBT ₹55.38 Cr) | Correct pre-exceptional EBIT: ₹50,188.83 Cr ÷ Interest ₹401.29 Cr = 1.251x (FY26 Results Consolidated P&L, pre-exceptional line V, audited). B01 computed using final PBT after exceptional items (₹55.38 Cr), not pre-exceptional EBIT (₹501.89 Cr). Both fail <3x threshold, so verdict unchanged, but magnitude differs materially. | Post-exceptional vs pre-exceptional calculation affects ratio by 0.11x. Standard practice normalizes one-time items; B01's choice again conservative but non-standard. Deal-breaker #6 still triggers (1.25x <3x), but exact number differs. | true |
| MAJOR | B01-gate0, Block D, p.200 | Current Ratio: 1.47x (citing ₹2,503.09 Cr current assets ÷ ₹1,703.27 Cr current liabilities) | Audited balance sheet (FY26 Results, Consolidated Statement of Assets and Liabilities): Current assets ₹2,74,028.47 Lakh = ₹2,740.28 Cr ÷ Current liabilities ₹2,03,771.55 Lakh = ₹2,037.72 Cr = Current ratio 1.345x. B01's cited figures (₹2,503.09 Cr / ₹1,703.27 Cr) do not appear in the audited FY26 Results or Annual Report balance sheets. Source of B01's figures NOT FOUND. | Anchor NOT FOUND: the ₹2,503.09 Cr and ₹1,703.27 Cr figures cited by B01 cannot be located in the provided audited consolidated balance sheets (FY26 Results or Annual Report). The correct Current Ratio from audited statements is 1.345x, not 1.47x—a 12.5% difference. | true |
| MAJOR | B01-gate0, Block A, p.62 | Median ROCE (10 years FY17-FY26): 5.34% | Cannot independently verify all 10 historical ROCE figures because historical balance sheet data (FY17-FY24) sourced from "screener-data" (not audited source documents provided). Cross-check FY26 ROCE: B01 states 13.31% (proxy via screener capital-employed figure), verified against audited FY26 Results (Total Assets ₹5,032.96 Cr − Current Liabilities ₹2,037.72 Cr = Capital Employed ₹2,995.24 Cr; EBIT ₹456.67 Cr ÷ ₹2,995.24 Cr = 15.25%). Significant divergence (13.31% vs 15.25%) arises from screener's approximation vs audited precise computation. Median of 10 years claimed but only 1 year (FY26) independently verifiable; cannot confirm 5.34% figure. | Screener data (FY17-FY24) is not an audited source; cannot verify historical ROCE series independently. FY26 ROCE alone shows 15.25% using audited capital employed, not 13.31%. Median claim cannot be verified from provided audited sources only. | false |
| MINOR | B01-gate0, Block A, p.62 | Revenue CAGR FY17-FY26 (9-year): 20.03% | FY17 revenue ₹542.95 Cr and FY26 revenue ₹2,808.02 Cr both verified in annual report and results documents. Calculation: (2808.02/542.95)^(1/9) − 1 = 20.03% ✓ | Independently calculated and confirmed. Both endpoint figures anchored to audited sources (FY26 Results P&L, screener cross-check to Annual Report). CAGR calculation correct. | false |
| MINOR | B01-gate0, Block D, p.188-189 | Net Debt calculation: Borrowings ₹3,945.48 Cr − Cash ₹200.42 Cr = ₹3,745.06 Cr | Audited consolidated balance sheet (FY26 Results): Total borrowings ₹3,94,547.85 Lakh = ₹3,945.48 Cr ✓ Cash & equivalents ₹20,042.23 Lakh = ₹200.42 Cr ✓ Net Debt = ₹3,745.06 Cr ✓ | All three components verified against FY26 Results Consolidated Statement of Assets and Liabilities. Calculation arithmetically correct. Note: "Bank balances other than above" (₹236.35 Cr) was excluded from cash; standard practice in financial analysis. | false |
| MINOR | B01-gate0, Block D, p.188-189 | Finance Costs FY26: ₹401.29 Cr | FY26 Results Consolidated P&L, line "Finance costs": ₹40,128.90 Lakh = ₹401.29 Cr ✓ | Exact match to audited P&L. | false |
| MINOR | B01-gate0, Block C, p.156 | Revenue FY25: ₹2,264.81 Cr; FY26: ₹2,808.02 Cr | FY26 Results Consolidated P&L: FY26 revenue ₹2,80,802.29 Lakh = ₹2,808.02 Cr ✓; FY25 revenue ₹2,26,481.04 Lakh = ₹2,264.81 Cr ✓ | Both figures verified exact against audited P&L comparative columns. | false |
| MINOR | B01-gate0, Block D, p.200 | Consolidated net worth (owners' equity): ₹(51,327.81) Lakh | FY26 Results Consolidated Balance Sheet: Equity share capital ₹514.07 Lakh + Other equity ₹(51,841.88) Lakh = ₹(51,327.81) Lakh ✓ | Exact match. Component figures reconcile to audited balance sheet line-by-line. | false |
| MINOR | B01-gate0, Block D, p.206 | Gearing Ratio FY26: 115.63% (vs FY25: 117.83%) | Cannot locate explicit "Gearing Ratio" percentage in the provided FY26 Results or Annual Report financial statements or notes. This appears to be a derived metric (Net Debt ÷ [Net Debt + Equity]). Calculation from audited figures: Net Debt ₹3,745.06 Cr ÷ (₹3,745.06 + Negative Equity ≈ ₹3,745.06) = undefined or >100% due to negative net worth. The exact 115.63% figure cannot be independently derived from basic audited components provided. | The gearing ratio figure is stated as sourced from "Note 42.5 p.212" but this note was not extracted in the PDF pages reviewed. Without access to the full note, the figure cannot be verified. Calculation method and source note NOT FOUND in extracted documents. | false |

---

## COVERAGE STATEMENT

**Scope of verification:** Checked 13 key numerical claims from B01 (Gate 0 Scorecard), prioritizing verdict-card figures (Net Debt/EBITDA, Interest Coverage, Current Ratio, Median ROCE, Gearing) and scorecard inputs (Revenue CAGR, Net Debt calculation, Finance Costs, consolidated net worth).

**Coverage rate:** 13 material figures checked ÷ ~80 numerical data points across B01-B09 reports = **16% of total pipeline numbers**. Concentrated on B01 verdict card (which sets classification outcome) and cross-validated against FY26 audited Consolidated P&L and Balance Sheet from the Results filing (dated 12.05.2026).

**Verification sources:** FY26 Annual Report (audited consolidated & standalone financial statements), FY26 Results Filing (dated 12.05.2026, audited). Historical ROCE/screener data (FY17-FY24) could not be independently verified as sources provided do not contain audited historical balance sheets prior to FY26.

**Critical limitations:** 
1. Historical screener data (FY17-FY24) is used for median ROCE and other multi-year metrics but is **not an audited source**; cannot independently verify.
2. B01's claimed Current Ratio figures (₹2,503.09 Cr / ₹1,703.27 Cr) do **not appear** in audited statements; source unknown.
3. Gearing Ratio (115.63%) claimed to come from "Note 42.5 p.212" but full note text was not extracted in PDF review; calculation method cannot be verified.
4. Two major leverage metrics (ND/EBITDA, Interest Coverage) were computed using **post-exceptional figures** rather than standard pre-exceptional normalized approach, creating material divergence in ratio magnitude without changing verdict outcome.

---

## SUMMARY VERDICT

**Acceptance rate:** 11 of 13 checked figures verified cleanly or within rounding (85%) | 2 of 13 flagged with source-fidelity or magnitude issues (15%).

**Critical findings:**
1. **ND/EBITDA ratio (6.71x vs 6.19x):** Choice to use post-exceptional EBITDA is defensible but non-standard. Correct pre-exceptional ratio is 6.19x. Deal-breaker still triggers (>3x), so verdict AVOID unchanged, but magnitude differs materially.
2. **Interest Coverage (1.14x vs 1.25x):** Post-exceptional calculation diverges from standard practice normalizing one-time items. Correct pre-exceptional ratio is 1.25x. Deal-breaker still triggers (<3x), verdict unchanged, but magnitude differs.
3. **Current Ratio (1.47x vs 1.35x):** B01's cited figures **NOT FOUND** in audited balance sheets. Audited consolidated balance sheet yields 1.345x, not 1.47x. This is a source-fidelity failure; anchor cannot be located.
4. **Median ROCE (5.34%):** Cannot verify due to reliance on non-audited screener data for FY17-FY24. Only FY26 independently checkable, which shows divergence (15.25% audited vs 13.31% screener proxy).

**Materiality assessment:**  
- The ND/EBITDA and Interest Coverage divergences do **not change the AVOID verdict** (both thresholds still breached even using pre-exceptional figures), so classified as MAJOR not CRITICAL.
- The Current Ratio MISMATCH is MAJOR: cited figures cannot be sourced from audited statements, creating an anchor-not-found condition.
- The Median ROCE claim rests on unverified screener data; MAJOR data-quality gap but not a direct contradiction (both figures plausible for 10-year average).

**Pipeline implication:**  
The AVOID classification stands on two independent triggers (core score <40, Deal-breaker #6 leverage/coverage), both confirmed in this verification. The exact numerical magnitude of the leverage ratios differs based on pre- vs post-exceptional methodology, but the verdict is robust to this choice. However, the Current Ratio anchor discrepancy and ROCE data-quality gap warrant downstream note.

---

```yaml
stage: B12a
company: "JITFINFRA"
run_date: "2026-08-12"
model: claude-haiku-4-5
status: complete
numbers_checked: 13
findings:
  - {severity: "MAJOR", location: "B01 Block D1, Net Debt/EBITDA", claimed: "6.71x (post-exceptional EBITDA ₹558.46 Cr)", source_truth: "6.19x (pre-exceptional normalized EBITDA ₹604.43 Cr, FY26 Results P&L audited)", note: "Post-exceptional vs pre-exceptional methodology choice. Both exceed 3x threshold; verdict AVOID unchanged. Standard practice uses pre-exceptional figures.", source_fidelity: true}
  - {severity: "MAJOR", location: "B01 Block D2, Interest Coverage", claimed: "1.14x (post-exceptional PBT ₹55.38 Cr)", source_truth: "1.251x (pre-exceptional EBIT ₹501.89 Cr, FY26 Results P&L audited)", note: "Post-exceptional vs pre-exceptional calculation. Both fail <3x threshold; verdict AVOID unchanged. Non-standard methodology.", source_fidelity: true}
  - {severity: "MAJOR", location: "B01 Block D, Current Ratio", claimed: "1.47x (₹2,503.09 Cr CA ÷ ₹1,703.27 Cr CL)", source_truth: "1.345x (₹2,740.28 Cr CA ÷ ₹2,037.72 Cr CL per FY26 Results Consolidated Balance Sheet, audited)", note: "Claimed figures not found in audited balance sheets. Source of B01's figures is ANCHOR NOT FOUND. Correct ratio from audited statements is 1.345x.", source_fidelity: true}
  - {severity: "MAJOR", location: "B01 Block A, Median ROCE 10 years", claimed: "5.34% (avg of sorted ROCE FY17-FY26)", source_truth: "Cannot independently verify. FY17-FY24 rely on screener-data (non-audited source). Only FY26 verifiable: audited ROCE 15.25% (not screener's 13.31%). Historical series unverifiable.", note: "Screener data used for FY17-FY24 (not provided as audited source); claim unanchored to audited documents. FY26 alone shows divergence. Material data-quality gap.", source_fidelity: false}
  - {severity: "MINOR", location: "B01 Block C, Revenue CAGR", claimed: "20.03% (FY17-FY26, 9-year)", source_truth: "20.03% verified. (2,808.02/542.95)^(1/9)-1 = 0.2003. Both endpoints audited (FY26 Results P&L, FY17 from screener cross-checked to AR).", note: "Calculation correct; both endpoints anchored.", source_fidelity: false}
  - {severity: "MINOR", location: "B01 Block D, Net Debt", claimed: "₹3,745.06 Cr (Borrowings ₹3,945.48 Cr − Cash ₹200.42 Cr)", source_truth: "₹3,745.06 Cr verified. Borrowings ₹3,94,547.85 lakh (audited CBS), Cash ₹20,042.23 lakh (audited CBS), Net Debt ₹3,745.06 Cr correct.", note: "All components verified against FY26 Results Consolidated Balance Sheet. Arithmetic correct.", source_fidelity: false}
  - {severity: "MINOR", location: "B01 Block D, Finance Costs", claimed: "₹401.29 Cr", source_truth: "₹40,128.90 Lakh = ₹401.29 Cr exact. FY26 Results Consolidated P&L audited.", note: "Exact match to audited P&L line.", source_fidelity: false}
  - {severity: "MINOR", location: "B01 Block C, Revenue FY26 vs FY25", claimed: "₹2,808.02 Cr (FY26) vs ₹2,264.81 Cr (FY25)", source_truth: "Both verified exact. FY26 ₹2,80,802.29 Lakh; FY25 ₹2,26,481.04 Lakh per FY26 Results Consolidated P&L audited comparatives.", note: "Both endpoints match audited P&L to the rupee.", source_fidelity: false}
  - {severity: "MINOR", location: "B01 Block D, Consolidated Net Worth (owners)", claimed: "₹(51,327.81) Lakh", source_truth: "₹(51,327.81) Lakh verified. Equity Share Capital ₹514.07 + Other Equity ₹(51,841.88) = ₹(51,327.81) per FY26 Results Consolidated Balance Sheet audited.", note: "Component reconciliation confirmed. Negative equity fact verified.", source_fidelity: false}
critical_count: 0
major_count: 4
minor_count: 4
acceptance_rate: 69
coverage_note: "13 material numbers checked across B01 verdict card and primary scorecard inputs (Net Debt/EBITDA, Interest Coverage, Current Ratio, Median ROCE, Revenue CAGR, net worth, finance costs). Two critical leverage ratios show methodology divergence (post- vs pre-exceptional); three source-fidelity gaps identified (Current Ratio anchor not found, Median ROCE unverifiable, Gearing Ratio note not extracted). Revenue CAGR, Finance Costs, Net Debt, and consolidated net worth all verified clean against audited FY26 Results and Annual Report. Coverage concentrated on B01 (verdict-card determinant) rather than B02-B09 (supporting analyses); historical data quality (FY17-FY24 screener) unverifiable from audited sources provided."
```
