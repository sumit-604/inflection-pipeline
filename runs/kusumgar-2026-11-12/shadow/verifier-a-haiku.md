# Verifier A (shadow, Haiku 5.5): Numerical accuracy, KUSUMGAR, run 2026-11-12

SHADOW RUN. Operator ruling 2026-10-11. These findings bind nothing: they never enter B12a, the confidence delta, a REWORK decision, the verdict or the synthesis. The check ran as if it counted.

Inputs: outputs/reports/01 to 09 (ALL_STAGE_REPORTS) and the source twins in inputs/ (prospectus .txt with [page N] markers, screener CSV and shareholding print, Q1 and Q2 FY27 results, Q2 investor deck, concall transcript). Anchors read as PDF page N from the twin markers. Results files are OCR-degraded in places (for example "1,855,30" for 1,855.30); those values were read by line context and recomputed.

Not read: outputs/reports/12d-verifier-peers.md (another verifier's output, not in ALL_STAGE_REPORTS).

## 1. Findings

Mandatory tier = Gate 0 scorecard values in 01-gate0.md (OR-32). Sample tier = everything else.

| # | Sev | Tier | Location | Claimed | Source truth (anchor) | Note | SF |
|---|---|---|---|---|---|---|---|
| 1 | MINOR | mandatory | 01 Block F, M3 | Closing-PPE sensitivity 2.94x, no page anchor | 2,356.68 = PPE at 31 Mar 2026, prospectus p.75 line 4872; 2.94x reproduces | Unanchored, not material; M3 stays 5 | no |
| 2 | MINOR | mandatory | 01 Block F, M5 | "Kusumgar ranks 7th of 7 by market cap" (screener p.2) | Screener p.2 peer table has eight rows; Kusumgar 5,772.39 Cr is 7th of 8. The seven named rows support 7th | Denominator not reconciled; score unaffected | no |
| 3 | MINOR | mandatory | 01 Block E, E4 | 1,089.70 cited to prospectus p.80 | p.80 prints 1,038.77 + 10.14 + 40.79 = 1,089.70 (58.33 commitment excluded, as labelled). p.80 total is 1,148.03 incl. commitment. 1,089.70 total printed p.44 (lines 3086, 3101) | Figure present as a sum on the cited page; cite p.44 | no |
| 4 | MAJOR | sample | 04 Section 0 rows 1, 4; 04 Section 1D; 05 FLAG-CASH; 07 Section 0 row 1 | H1 FY27 CFO 248.85 (tax 372.02); Sep 2026 receivables 2,203.67; inventories 2,688.41; borrowings 701.32 + 1,855.31 | All consolidated (Q2 results p.11 BS lines 961-1010; p.12 CF lines 1111-1112). Standalone basis used in 01 (labelled): CFO 340.73, tax 365.06 (p.6); TR 1,915.61, inventories 2,555.82, borrowings 700.42 + 1,855.30, cash 451.61 (p.5) | Same H1 period on two bases in one run; consolidated basis unlabelled. Material to the cash-conversion read. UNANCHORED (basis) | yes |
| 5 | MAJOR | sample | 07 Section 0 row 3, Section 2C; 09 Section 3C | CWIP 101.04 at Sep 2026, cited Q2 results p.11 | 101.04 occurs once in the Q2 results twin (line 327, page 5, standalone BS). Page 11 does not contain it. Mar 2026 CWIP 262.64 is consolidated (prospectus p.75) | ANCHOR NOT FOUND on a material growth input (capex_embedded_growth_pct 5.0); mixes standalone and consolidated | yes |
| 6 | MAJOR | sample | 07 Section 0 row 1; 05 FLAG-CASH | H1 FY27 EBITDA 1,480 (cited Q2 results p.12) | 1,480 is the H1 FY27 EBITDA cell of the Q2 investor deck (line 98). Absent from the Q2 results file including p.12. Deck figure includes other income (04 Section 2B note) | ANCHOR NOT FOUND in 07 on a material ratio (16.8%); 05 uses deck basis unlabelled | yes |
| 7 | MINOR | sample | 07 Section 0 row 4 | Promoters 89.79% pre-offer | Prospectus p.103 (lines 7045-7051) shows 89.79% basic. Fully diluted 89.44% at p.59 (line 4063) and p.108 (line 7165). 01 uses 89.44%. 07 also uses 15,521,698 OFS shares where 01 uses 15,521,350 (Q2 results p.7) | Unlabelled basis; E2 score same either way | no |
| 8 | MINOR | sample | 08 Section 1B, Kusumgar Holdings LLP | Trademarks assigned "for 0.05" (no unit) | Prospectus line 14598 (p.239): consideration Rs 51,000 = 0.051 INR million | Unit omitted, rounded; reproduces | no |

Severity count: 0 CRITICAL, 3 MAJOR, 5 MINOR.

Rows struck under rule 5b (3): (a) the 07/09 capex line "7.83% with the 58.33 mn commitment" first read as an arithmetic error; it reproduces as (101.04 + 58.33) x 3.40 / 6,920.03 = 7.83%, the 07 method, so it is a matched figure. (b) The EBITDA margin 22.50% (67.86 / 301.65 = 22.50%) reproduces. (c) 15,521,350 vs 15,521,698 shares: the 01 figure matches the cited Q2 results p.7 and the BM outcome; the difference is between two corpus documents, not a report error.

## 2. Coverage

MANDATORY TIER (OR-32): 234 of 234 checked. Scope is every Gate 0 scorecard value in 01-gate0.md, grouped below. Each value was checked against its anchor (prospectus page markers, screener CSV, screener print, Q2 results and deck) or recomputed from checked inputs.

| Group | Values | Result |
|---|---|---|
| Load-bearing table (screener, segments, capacity, concentration, exports) | 69 | 69 clean |
| Block A (ROCE, ROE, equity, A1-A4) | 28 | clean |
| Block B (CFO, capex, FCF, WC days and inputs, cash-flow context) | 62 | clean |
| Block C (CAGRs, positive-year count) | 6 | clean |
| Block D (debt, cash, EBITDA, cover, D/E, current ratio, leases, Sep 2026 standalone) | 23 | clean |
| Block E (holdings, pledge, contingent liabilities, IPO, selling amounts) | 19 | 1 non-clean (row 3, 1,089.70 anchor) |
| Block F (margins, FAT, PPE, R&D, own proxy, S&A shares, M5 rank) | 19 | 2 non-clean (rows 1 and 2) |
| Block totals (A 15, B 0, C 16, D 17, E 11, core 59, moat 13, total 72) | 8 | clean |
| **Total** | **234** | **231 clean, 3 non-clean** |

SAMPLE TIER (rule 2): the material universe in reports 02 to 09 was not enumerated (about 2,000 lines). Sample count is approximate: about 110 values, selected by materiality. Checked: 04 Section 0 and 2B, 09 Sections 2 and 3 (TAM, SAM, SOM, capacity, derived paths), 07 Section 0, 08 Sections 1A and 1B holdings, 05 H1 cash-flow lines. About 101 of 110 clean. Overall acceptance: 332 of 344 = 96.5%; mandatory 231 of 234 = 98.7%.

Not checked:
- 02-notes (three files), 06-peers, 03-ardeep (except PBT growth, which reproduces).
- 07 category scores and multipliers (the Pillar 3 emerging-moat feed). This is the largest gap. Pillar 3 numbers are not verified in this run.
- 05 transcript quotes; Q1 FY27 results and deck; rating PDFs (no rating figure appears in the checked set); peer concalls.
- Web-sourced figures in 09 (Section 4A duty and budget items, Section 2 search snippets). These are not in the inputs and cannot be checked from them.

## 3. Observations for the orchestrator (not findings)

- 12d-verifier-peers.md sits in outputs/reports before Phase 1 verifiers run. It is outside ALL_STAGE_REPORTS. Check whether it should be there under the no-cross-verifier rule.
- 07 tags CWIP and H1 EBITDA as stage inputs without a basis label. The same Sep 2026 standalone and consolidated mix recurs in 04, 05 and 07. Operator may want one basis rule for Q2 figures.
- Two OFS share counts are in the corpus (15,521,350 in filings; 15,521,698 in the prospectus, with a footnote). Reports should name which they use.
- Tier judgment for operator: row 5 (capex_embedded_growth_pct) is tiered sample here. If it feeds a 1B growth basis, it is mandatory and would be re-tiered.

```yaml
stage: B12a
company: "KUSUMGAR"
run_date: "2026-11-12"
model: claude-haiku-5-5
status: complete
shadow_run: true
shadow_note: "Operator ruling 2026-10-11. Findings bind nothing: not in B12a, confidence delta, REWORK, verdict or synthesis."
numbers_checked: 344            # approx: mandatory 234 exact; sample about 110 counted by row during the run
mandatory_checked: 234
mandatory_total: 234
findings:
  - {severity: "MINOR", location: "01-gate0.md, Block F, M3 (data_notes and sensitivity)", claimed: "closing-PPE sensitivity 6,920.03 / 2,356.68 = 2.94x, no page anchor given", source_truth: "2,356.68 is PPE at 31 Mar 2026, prospectus p.75 (line 4872); 2.94x reproduces", note: "UNANCHORED, not material: M3 stays 5 on the average-PPE basis", source_fidelity: false, tier: mandatory}
  - {severity: "MINOR", location: "01-gate0.md, Block F, M5 (note)", claimed: "Kusumgar ranks 7th of 7 by market cap (screener print p.2)", source_truth: "screener print p.2 peer table has eight rows; Kusumgar (Mar Cap 5,772.39 Cr) is 7th of 8; the seven named rows support 7th", note: "denominator not reconciled to the print; M5 score unaffected", source_fidelity: false, tier: mandatory}
  - {severity: "MINOR", location: "01-gate0.md, Block E, E4", claimed: "contingent liabilities 1,089.70 cited to prospectus p.80", source_truth: "p.80 prints bank guarantee 1,038.77, tax demand 10.14, letter of credit 40.79 (sum 1,089.70 correct; 58.33 commitment excluded as labelled); p.80 total is 1,148.03 including the commitment. The 1,089.70 total is printed at p.44 (lines 3086, 3101)", note: "figure present at the cited page as a sum; cite p.44 or show the sum", source_fidelity: false, tier: mandatory}
  - {severity: "MAJOR", location: "04-bizmodel.md Section 0 rows 1 and 4, Section 1D WC row; 05-concall.md FLAG-CASH; 07-emoat.md Section 0 row 1", claimed: "H1 FY27 CFO 248.85 (tax 372.02); Sep 2026 receivables 2,203.67; inventories 2,688.41; borrowings 701.32 + 1,855.31", source_truth: "all consolidated: Q2 FY27 results p.11 balance sheet (lines 961-1010) and p.12 cash flow (lines 1111-1112). The standalone basis used in 01 (labelled) is CFO 340.73 and tax 365.06 (p.6); trade receivables 1,915.61, inventories 2,555.82, borrowings 700.42 + 1,855.30 (p.5)", note: "same H1 period carried on two bases in one run; consolidated basis unlabelled in 04, 05 and 07. Material to the cash-conversion read. UNANCHORED (basis)", source_fidelity: true, tier: sample}
  - {severity: "MAJOR", location: "07-emoat.md Section 0 row 3 and Section 2C (CWIP lines); 09-tam.md Section 3C", claimed: "CWIP 101.04 at Sep 2026, cited to Q2 results p.11", source_truth: "101.04 appears once in the Q2 results twin, line 327, on page 5 (standalone balance sheet). Page 11 (consolidated balance sheet) does not contain it. Mar 2026 CWIP 262.64 is consolidated (prospectus p.75)", note: "ANCHOR NOT FOUND on a material growth input (capex_embedded_growth_pct 5.0). Mixes standalone Sep 2026 with consolidated Mar 2026. Tier sample: flagged for operator to confirm whether this feeds a 1B pillar", source_fidelity: true, tier: sample}
  - {severity: "MAJOR", location: "07-emoat.md Section 0 row 1 (anchor: Q2 results p.12); 05-concall.md FLAG-CASH", claimed: "H1 FY27 EBITDA 1,480 used for the 16.8% CFO ratio", source_truth: "1,480 is the H1 FY27 EBITDA cell of the Q2 investor presentation (Investor_Presentation_Q2FY27_2026-11-05.txt, line 98). It is absent from the Q2 results file, including p.12. The deck figure includes other income (04-bizmodel.md Section 2B note)", note: "ANCHOR NOT FOUND in 07 on a material ratio. 05 uses the deck basis without a label", source_fidelity: true, tier: sample}
  - {severity: "MINOR", location: "07-emoat.md Section 0 row 4", claimed: "promoters 89.79% pre-offer, falling to about 75.01%", source_truth: "prospectus shareholding pattern p.103 (lines 7045-7051) shows 89.79% on a basic basis. Fully diluted 89.44% at p.59 (line 4063) and p.108 (line 7165). 01 uses 89.44%. The offer share count in 07 (15,521,698, prospectus) differs from 01 (15,521,350, Q2 results p.7); both appear in the corpus", note: "unlabelled basis. Same E2 score either way (-14.43pp or -14.78pp)", source_fidelity: false, tier: sample}
  - {severity: "MINOR", location: "08-promoter.md Section 1B, Kusumgar Holdings LLP row", claimed: "trademarks assigned to the company for 0.05 (no unit)", source_truth: "prospectus line 14598 (p.239): one-time consideration aggregating to Rs 51,000, which is 0.051 INR million", note: "unit omitted and value rounded; figure reproduces", source_fidelity: false, tier: sample}
critical_count: 0
major_count: 3
minor_count: 5
false_positives_struck: 3       # 7.83% capex line (reproduces as (101.04+58.33) x 3.40 / 6,920.03, 07 method); 22.50% EBITDA margin (reproduces); 15,521,350 vs 15,521,698 (report matches cited filing; source-to-source difference, not a report error)
material_universe: null         # not enumerated across reports 02-12; see coverage_note
acceptance_rate: 96.5           # clean 332 of 344 checked (mandatory 231 of 234 = 98.7; sample about 101 of about 110)
coverage_note: "MANDATORY TIER (OR-32): 234 of 234 checked. Scope = every Gate 0 scorecard value in 01-gate0.md: load-bearing table, Blocks A-F, and the block, core, moat and grand totals, plus recomputation of derived values. No mandatory figure unchecked. Source: prospectus .txt twin (page markers), screener CSV and shareholding print, Q2 FY27 results and investor deck. Non-clean mandatory values: 3 (rows 1-3). SAMPLE TIER (rule 2): material universe not enumerated; about 110 values checked by materiality across 04 Section 0 and 2B, 09 Sections 2-3, 07 Section 0, 08 Sections 1A-1B, 05 cash-flow lines. NOT checked: 02-notes (3 files), 03-ardeep (PBT growth only), 06-peers, 07 category scores (Pillar 3 EM feed: not verified in this run), 05 transcript quotes, Q1 FY27 results and presentation, rating PDFs, web-sourced figures (09 Section 4A and search snippets; not in the inputs, so not checkable). outputs/reports/12d-verifier-peers.md is present in the reports folder; it is not in ALL_STAGE_REPORTS and was NOT read (another verifier's output)."
```
