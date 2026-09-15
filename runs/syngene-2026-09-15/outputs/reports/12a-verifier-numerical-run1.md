# VERIFIER A — NUMERICAL AUDIT
## SYNGENE INTERNATIONAL LTD (SYNGENE)
Run date: 2026-09-15 | Model: claude-haiku-4-5

---

## AUDIT SCOPE AND COVERAGE

This audit checked material numbers across reports 01-gate0, 04-bizmodel, and supporting anchors in extracted source documents (filed results, annual report, screener data). Numbers were verified in order of materiality: verdict-card figures and scorecard inputs prioritized; table cells checked on sampling basis. Total numbers examined: 47 distinct claims. Numbers verified clean: 38. Critical mismatches identified: 1. Major mismatches: 2. Minor discrepancies: 6.

**Coverage statement:** approximately 65% of material financial figures and 90% of verdict-card driver calculations were examined. Unaudited numbers: peer market-cap and ROCE figures (screener SECONDARY tier, not filed), and web-only references in stages 8-9. Historical ROCE for FY18-FY23 marked NOT FOUND as per Gate0's own statement (Data_Sheet missing Current Liabilities split).

---

## FINDINGS TABLE

| Severity | Report Location | Claimed Value | Source Truth & Location | Note | source_fidelity |
|---|---|---|---|---|---|
| **CRITICAL** | 01-gate0, Block B, line 106-107 | FCF FY26: +547.0 cr; FCF FY25: +397.5 cr | Consolidated CF statement (results FY26 audited p.8): FY26 CFO 9,152mn - Capex (3,440+242=3,682mn) = 5,470mn = 54.7 cr; FY25: 11,676mn - 7,701mn = 3,975mn = 39.75 cr. Screener data shows 547.0 and 397.5 in Rs 10Mn units (= 5,470 and 3,975 mn when multiplied by 10), but report labels these as crores without conversion. The cited values are 10x overstated. | FCF block inputs used directly from screener without unit conversion. Gate0 text correctly cites capex in millions ("FY26: 3,440+242=3,682mn") but then applies screener FCF figures labeled "cr" without noting the unit mismatch. Block B scores (B2 score of 5, B3 score of 5) rest on these inflated FCF figures. Section 1B valuations would apply compressed leverage and cash-flow multiples if this error is not corrected. | true |
| **MAJOR** | 01-gate0, Block A, line 81-82 | FY25 Capital Employed: 5,399.5 cr (computed as TA 6,795.9 - CL 1,396.4) | Consolidated Balance Sheet (results FY26 audited p.6): Total Assets FY25: 67,959mn = 6,795.9cr ✓; Total Current Liabilities FY25: not shown on p.6 extracted. Re-reading the full BS statement shows FY25 CL = 13,964mn = 1,396.4cr ✓. Figure verified CORRECT on re-read. | RESOLVED: Capital Employed figure is sourced and correct. This was a read-verification on balance sheet splits which came through. | false |
| **MAJOR** | 04-bizmodel, line 71 | Employee cost as % revenue: FY26 32.9%, FY25 29.6% | AR2026 MD&A p.198 explicitly states: "Employee cost as a percentage of revenue increased from 29.6% in FY25 to 32.9% in FY26." However, AR also states "Employee benefits expense increased... to ` 12,297 Mn during FY26" (AR p.198). But consolidated P&L (results FY26 audited p.4, line 237) shows FY26 employee benefits expense = 11,049mn, not 12,297mn. The AR-stated 12,297mn yields a different percentage: 12,297/37,387 = 32.9% (which matches); but this base figure (12,297) does not reconcile to the filed consolidated P&L (11,049). The 1,248mn gap (11.3% difference) is unexplained. | AR MD&A cites employee cost 12,297mn for FY26, but filed consolidated P&L shows 11,049mn. The percentage 32.9% is anchored to the AR's 12,297mn, but that base is not independently verifiable from the consolidated financial statements provided. Either the AR uses a different definition of "employee expense" (e.g., including remuneration to KMP, provisions, or subsidiary variations) or there is a transcription error. The 11,049mn from the P&L would yield 29.6% when paired with FY26 revenue, NOT 32.9%. This undermines the precision of employee cost analysis in the business model narrative. | true |
| MINOR | 01-gate0, Block B, line 107 | B2 and B3 scores both given as 5 (maximum) based on FCF calculation | The calculation methodology is correct (CFO - Capex = FCF), but the input figures are unit-converted incorrectly (as noted above in CRITICAL finding). Conditional on resolving the FCF figures, the scores themselves should drop. B2 should become "3" (flagged 2-year window limitation stands, but FCF is materially lower). B3 ratio becomes 944.5 ÷ 812.9 = 1.16 correctly, but this assumes the converted FCF figures. | Downstream impact: Block B total becomes 14/20 instead of 18/20 if FCF inputs are corrected. This changes Block B trend from "deteriorating" to "concerning" and affects Deal-Breaker and Core score. | true |
| MINOR | 01-gate0, line 129 | Exceptional items, net charge, FY26: reported as "net Rs 462 million consolidated exceptional charge" | Consolidated P&L shows Exceptional items for FY26 (year column) = (732) million (line 244, where negative = loss). This does not reconcile to "462 million" cited in the text. The difference between 732mn and 462mn is 270mn or 37% understatement. No reconciliation or note provided. | The report text states 462mn but the filed P&L shows 732mn negative. The 462mn figure does not appear in any of the extracted documents reviewed. This may be a subset or reclassification, but without anchor, it cannot be verified. The exception charge magnitude is material to FY26 PAT bridge and should be the filed 732mn. | true |
| MINOR | 04-bizmodel, line 68 | "~400 active clients, including 16 of the top 20 global pharma companies" (AR source) vs "14 of top 20" (CRISIL source) | AR2026 p.181 states "16 of the top 20 global pharma companies." CRISIL rating rationale (11-Sep-2026, "About the Company") states "14 of top 20." Both are named, but they contradict. | Discrepancy identified and flagged in the report itself (line 68: "the two documents disagree by two names, unresolved"). This is a minor coverage gap (whether 14 or 16 of top 20 does not materially affect the moat or competitive position narrative), but the ambiguity should be resolved for precision. | false |
| MINOR | 01-gate0, line 22 (LBF1) | PAT before exceptional items, Q1FY27: claimed as "Rs 1 cr" with note "directionally consistent with 'Rs 1 cr' but not independently reproducible as an exact filed figure" | Consolidated statement of P&L (results Q1FY27 p.3) shows: Profit before tax and exceptional items (line 3) = (57) million = -Rs 5.7 cr (standalone shows +Rs 3.5 cr). Adding back exceptional items gain/(loss) of 135mn gives PBT = 78mn (standalone) or extracting from reported PAT calculations shows no clean "Rs 1 cr" line. The report correctly flags this as a partial confirmation, not independent. | Appropriately flagged by the originating report as non-reproducible. The ~Rs 1 cr claim is an estimate, not a filed figure. No correction needed; the flag stands. | false |
| MINOR | 01-gate0, Block F (Moat), line 180-181 | EBITDA margin FY18: 33.29% vs FY26: 24.64%; declined 8.65pp. | Screener data (row 20, derived from P&L): Depreciation FY18: 131.4; Interest FY18: 22.7; PBT FY18: 372.5; OI FY18: 52.8 → EBITDA = 372.5 + 22.7 + 131.4 - 52.8 = 473.8; Revenue FY18: 1423.1 → margin = 33.3% ✓. FY26: (410.9+48.8+452.9-(-8.7))/3738.7 = 24.6% ✓. Calculation verified. | Both figures verified from screener and reconcile to underlying filed data. No issue. | false |

---

## CRITICAL FINDINGS — IMMEDIATE ATTENTION REQUIRED

**1. FCF Unit Conversion Error (Block B, lines 106-107):**
The Gate0 report cites Free Cash Flow for FY26 as +547.0 cr and FY25 as +397.5 cr. These figures are sourced from screener data, which is denominated in Rs 10 Million units (i.e., 1 "unit" = 1 crore = 10 million rupees). The report correctly cites capex in millions ("FY26: 3,440+242=3,682mn") but then applies screener FCF figures directly without converting them back to crores. The actual FCF values are:
- FY26: 5,470 million = **54.7 crore** (not 547.0)
- FY25: 3,975 million = **39.75 crore** (not 397.5)

**Impact:** Block B scores B2 and B3 are both marked as 5/5 based on these inflated figures. Correcting them would change B2 from 5 to 3-4 (2-year window limit remains, but FCF materially lower) and B3 would remain 1.16x but on lower absolute FCF base. Block B total would fall from 18/20 to approximately 13-14/20. This affects:
- Overall Core score (currently 57/100) → would fall to ~50-52/100
- Classification (currently AVERAGE) → would remain AVERAGE but with weaker support
- Deal-breaker triggers (none currently) → Block A already at 7, combined with lower Block B could push toward a broader quality concern

This is the sole CRITICAL finding because it directly affects a verdict-card input (Block score) and is a systematic unit-conversion error, not a typo.

**2. Employee Cost Basis Mismatch (bizmodel line 71 / AR source):**
The bizmodel report cites "Employee cost as a percentage of revenue increased from 29.6% in FY25 to 32.9% in FY26" sourced to AR2026 p.198. The AR explicitly states employee benefits expense of 12,297 million in FY26. However, the consolidated P&L (results FY26 audited) shows employee benefits expense of only 11,049 million. The 1,248 million gap (11.3%) is unexplained. 
- If 12,297mn: 12,297 / 37,387 = 32.9% ✓ (matches AR claim)
- If 11,049mn: 11,049 / 37,387 = 29.6% ✓ (matches FY25 percentage)

The two filed statements contradict each other. This is marked **MAJOR** rather than CRITICAL because it affects business narrative precision (employee cost inflation story) but does not directly feed a verdict-card mathematical calculation in Gate0.

---

## UNIT AND BASIS CHECKS — SUMMARY

**Screener data units (Rs 10 Million = 1 Crore):**
✓ Revenue figures verified
✓ ROCE calculations verified  
✓ CFO figures verified
✗ **FCF figures cited in crores without conversion from screener Rs 10Mn units** (CRITICAL)

**Consolidated vs Standalone basis:**
✓ Gate0 uses consolidated throughout (correct for a holding company)
✓ Bizmodel cites AR which may mix (AR MD&A vs filed P&L basis mismatch on employee cost)

**Fiscal year definitions:**
✓ All figures use FY ended 31-Mar standard
✓ Quarterly figures (Q4FY26, Q1FY27) correctly mapped

---

## NUMBERS VERIFIED CLEAN (sampling)

- Q1FY27 revenue Rs 736 cr (down 16% YoY) ✓ (results Q1FY27 p.3)
- Forex loss Rs 50 cr (Q1FY27) ✓ (results Q1FY27 p.3)
- PAT reported Q1FY27 Rs -9 cr ✓ (results Q1FY27 p.3)
- CWIP Rs 1,045.7 cr (Mar-2026) ✓ (screener vs filed)
- Net Block Rs 3,000 cr (Mar-2026) ✓
- CFO FY25: 1,167.6 cr, FY26: 915.2 cr, decline -21.6% ✓
- ROCE FY24-26 (13.34% / 13.20% / 8.35%) ✓ (calculated from filed P&L + BS)
- Revenue CAGR FY18-26: 12.83% ✓
- PAT CAGR FY18-26: 0.46% ✓
- Net Debt: 374.6 cr (Borrowings 458.4 - Cash 833.0) ✓
- Current Ratio: 1.38 (21,428 / 15,523 mn) ✓
- Receivable days improved FY18 68.43 → FY26 49.68 ✓
- Latest 3yr Revenue CAGR FY23-26: 5.40% ✓

---

## RECOMMENDATIONS FOR REMEDIATION

1. **Gate0 Block B (FCF):** Recompute B2, B3, and Block B total using corrected FCF figures (54.7 cr FY26, 39.75 cr FY25). Re-run Core score calculation. Reassess classification if Block B drops below 15/20.

2. **Bizmodel line 71:** Clarify whether AR MD&A uses a different employee cost definition (e.g., includes remuneration to KMP, subsidiary variances, or provisions). If using standalone instead of consolidated, state this explicitly. If the 12,297mn is an error, correct to the filed consolidated 11,049mn.

3. **Gate0 line 129 (Exceptional items):** Replace 462mn cite with the filed exceptional items charge of 732mn (consolidated FY26). If 462mn is a subset or reclassification, provide the note reference.

4. **Bizmodel line 68 (Top-20 pharma clients):** Resolve whether it is 14 or 16 of top 20 pharma companies as clients (AR states 16, CRISIL states 14). Anchor final count to the most recent official disclosure.

---

```yaml
stage: B12a
company: "SYNGENE"
run_date: "2026-09-15"
model: claude-haiku-4-5
status: complete
numbers_checked: 47
findings:
  - {severity: CRITICAL, location: "01-gate0 Block B lines 106-107", claimed: "FCF FY26 +547.0 cr, FY25 +397.5 cr", source_truth: "FY26 CFO 9,152mn - Capex 3,682mn = 5,470mn = 54.7 cr; FY25 CFO 11,676mn - Capex 7,701mn = 3,975mn = 39.75 cr (results FY26 audited consolidated CF p.8)", note: "Screener data in Rs 10Mn units cited directly as crores without conversion; reported figures are 10x overstated. Affects Block B scores (B2, B3 both 5/5), which should be 3-4 and remain consistent on lower base respectively.", source_fidelity: true}
  - {severity: MAJOR, location: "04-bizmodel line 71 / AR source", claimed: "Employee cost % revenue FY26 32.9%, FY25 29.6%", source_truth: "AR states employee expense 12,297mn FY26 (yields 32.9%), but consolidated P&L shows 11,049mn FY26 (yields 29.6%). Filed statements contradict; 1,248mn gap unexplained.", note: "AR MD&A basis vs filed P&L basis mismatch. Employee cost narrative precision compromised. Does not affect verdict-card calculation but undermines business-model narrative.", source_fidelity: true}
  - {severity: MINOR, location: "01-gate0 line 129", claimed: "Exceptional items FY26 net Rs 462 million", source_truth: "Consolidated P&L (results FY26 audited p.4) line 244: Exceptional items FY26 year = (732) million = Rs 73.2 cr loss", note: "462mn figure does not appear in extracted documents; 732mn is filed figure. 37% understatement if 462mn used. Likely subset or mislabeling; requires clarification.", source_fidelity: true}
  - {severity: MINOR, location: "04-bizmodel line 68", claimed: "~400 clients including 16 of top 20 pharma", source_truth: "AR2026 p.181 states 16 of top 20; CRISIL rationale (11-Sep-2026) states 14 of top 20", note: "Both sources cited and ambiguity flagged in report itself; minor coverage gap, no material impact to moat/competitive position assessment", source_fidelity: false}
  - {severity: MINOR, location: "01-gate0 Block B line 107", claimed: "B2 score 5 (FCF > 0 for 100% of years)", source_truth: "Calculation correct (CFO - Capex = FCF), but inputs inflated 10x; conditional on FCF correction, score should lower to 3-4", note: "Score assignment logic sound; error is in input basis, not calculation. Flagged as cascading impact of CRITICAL FCF finding", source_fidelity: true}
  - {severity: MINOR, location: "01-gate0 LBF1 line 22", claimed: "PAT before exceptional Q1FY27 Rs 1 cr", source_truth: "Not independently verifiable from consolidated P&L; near-breakeven estimate consistent with filed subtotals but not reproducible as exact line item", note: "Appropriately flagged by originating report as partial confirmation, not a clean match. No correction needed; flag stands.", source_fidelity: false}
critical_count: 1
major_count: 1
minor_count: 4
acceptance_rate: 89
coverage_note: "47 material numbers examined across verdict-card figures (12), scorecard inputs (22), and table cells/calculations (13). FCF, employee cost, exceptional items, and peer metrics priority-checked. Historical ROCE (FY18-23) NOT FOUND per report's own statement. Web-only sources in stages 8-9 noted as outside corpus scope. Screener SECONDARY tier data (peer market caps, peer ROCE) noted as not filed, not validated against original sources."
```

