# VERIFIER A (SHADOW), SOUTHWEST, run 2026-11-09

Model: claude-haiku-5-5 (effort high). Shadow run per operator ruling 2026-10-11. These findings bind nothing: they do not enter B12a, the confidence delta, REWORK, the verdict or the synthesis.

Inputs: outputs/reports/01-gate0.md through 09-tam.md (02-notes, 02-notes-pass1 and 02-notes-pass2 read where cited), outputs/blocks/B01-gate0.yaml and B08-promoter.yaml, and the source corpus under inputs/. I did not read any other verifier output.

Anchor convention: "[page N]" marker in each .txt (marker N precedes printed page N content). AR26 = Annual_Report_2026.txt. AR25 = Annual_Report_2025.txt. Reg 29(2) filings are read from inputs/announcements/.

## 1. Scope and tiering

- Mandatory tier (OR-32): every Gate 0 scorecard input and load-bearing figure in 01-gate0.md. Phase 1 has no verdict card and no Section 1B pillar input, so no other mandatory figure exists. Result: 109 mandatory occurrences, 109 checked (100%). Derived ratios count once per occurrence. Derived figures were re-computed from anchored source values.
- Sample tier: 65 figures checked, drawn in materiality order from stage 3 (15 figures: standalone CFO, capex, receivables), stage 8 (33 figures: holdings, disposals, value, pledge, pay, cash) and stage 9 (17 figures: TAM base, peer revenue, CAGR cross-checks). Stages 2, 4, 5, 6 and 7 were not enumerated. The sample universe is therefore a lower bound, and I do not state it as a percentage of the full stage set.

## 2. Findings

| ID | Sev | Tier | SF | Location | Claimed | Source truth | Note |
|---|---|---|---|---|---|---|---|
| V-01 | MAJOR | mandatory | yes | 01-gate0 Block E, E1; B01 data_notes | E1 promoter holding 68.85% at 31 Mar 2026; "Jun to Sep 2026 promoter disposals ... not netted (outside inputs)" | The disposals are inside inputs/announcements. Reg 29(2) filings dated 24 Jun 2026 (20260625-9BA85695 p.2-3), 10 Jul 2026 (20260710-36543982 and 20260710-E0531F7E), 12-13 Aug 2026 (20260813-9C8BA238 p.2-3) and 11 Sep 2026 (6219323E_43E3 p.2-3) show 2,01,44,762 shares held after the sales = 61.70% of 3,26,51,422 shares. The 68.85% figure uses the pre-warrant base of 2,98,30,011 shares (AR26 Note 41, line 11472 of the .txt; Note 19(e), p.133). The same 31 Mar holding on the current base is 62.90% (2,05,38,783 / 3,26,51,422, derived). | The 68.85% figure is correct as of 31 Mar 2026. The "outside inputs" statement is contradicted by the corpus. E1 scores on a stale holding and a pre-conversion base. Verifier A does not judge the score. Verifier C and the analyst stages own that. |
| V-02 | MAJOR | mandatory | yes | 01-gate0 Block E, E3; B01 analyst_note | E3 pledge "NOT FOUND (no pledge or encumbrance disclosure in AR FY26 text)", scored 0 | Reg 29(2) forms show the "Shares in the nature of encumbrance" line as a dash (nil) before and after the sales: 20260625-9BA85695 p.2 and p.3; 6219323E_43E3 p.2 and p.3 (lines 93 and 134 of the .txt). Stage 8 reports the same nil reading for the 10 Jul and 12 Aug forms. Verifier A did not re-read those two forms. | NOT FOUND is a claim about absence. The corpus holds a nil reading in filings the stage says are outside its inputs. The Block E score depends on this item. Verifier A flags the source fact only. |
| V-03 | MAJOR | mandatory | yes | 01-gate0 Load-bearing fact 1; data_notes | "Guidance of about 20% growth is NOT FOUND in this stage's inputs (concall text is not an input)" | AR26 CMD message: "confident of achieving around 20 % growth year on year in short to medium term" (Annual_Report_2026.txt line 256; stage 9 anchors it at AR p.6). Also Concall_May_2026_Transcript.txt line 194: "around 20% growth year-on-year". The AR is cited throughout Gate 0 as an input. | Guidance is in the corpus. The "NOT FOUND" label is wrong on the AR and on the concall. |
| V-04 | MAJOR | sample | yes | 09-tam, "Cross-check on delivery" | FY23 to FY26 revenue CAGR = (243.02 / 117.73)^(1/3) - 1 = 27.3% | screener-Data_Sheet.csv Sales row: FY22 = 117.73, FY23 = 124.26, FY26 = 243.02. The FY23 to FY26 base is 124.26. Correct CAGR = (243.02 / 124.26)^(1/3) - 1 = 25.1%. Gate 0 Block F (M11) uses 124.26 and gets 25.1% as well. | MISMATCH on the base year. The label says FY23 and the number uses FY22. The delivery cross-check moves from 27.3% to 25.1%. |
| V-05 | (struck) | sample | no | 09-tam line 19 | "AR p.56 states INR 2,430 Mn" | Value 2,430 Mn (= 243.02 Cr) is printed at Annual_Report_2026.txt line 680, in [page 13]. Page 56 does not contain it. | Matched figure under rule 5a. Only the page citation is wrong. Struck from the findings. Anchor correction noted for stage 9. |
| V-06 | MINOR | mandatory | no | 01-gate0 Block F, M11 | "prior 13.2% (FY20-23)" | Screener Sales FY20 = 85.8, FY23 = 124.26. (124.26 / 85.8)^(1/3) - 1 = 13.1%. | Imprecision of 0.06 pp. No score threshold is near. |
| V-07 | MINOR | mandatory | no | 01-gate0 load-bearing fact 1; data_notes | "The 14.38% in company memory is not reproduced on either basis" | The 14.38% margin is printed in inputs/presentation/Investor_Presentation_1.txt, [page 32] headline and [page 35] table: EBITDA 83 Mn on revenue 577 Mn. The filing basis gives 14.42% (consolidated: 832.55 / 5,773.04 lakh). The gap is rounding in the presentation's rounded inputs. | The Gate 0 wording names company memory and omits the presentation anchor. The figure is in the corpus. Rewrite the reference, not the score. |
| V-08 | MINOR | sample | no | 08-promoter sections 3C, 6B and 6E; 03-ardeep line 216 (labelled S) | Cash 88.81 lakh; CFO/PAT 0.40; FCF (3,520.26) lakh, cited to B02/B03 with no basis label in the body | These are standalone values. Standalone CFO 1,233.87 (AR26 line 6269), standalone PAT 3,080.05 (results Q2 FY27 p.5). Consolidated FY26 values are: cash and cash equivalents 129.40 lakh (AR26 p.166), CFO/PAT 0.38 (1,244.88 / 3,302.70), FCF -35.09 Cr (B01). | Unlabelled basis difference, reported as UNANCHORED under rule 5a. The chain of anchors does carry the S label in B03, so this is MINOR and not material. Gate 0 and stage 8 disagree on FY26 CFO/PAT (0.38 against 0.40) because they use different bases. Both values are correct on their own basis. |
| V-09 | MINOR | sample | no | 08-promoter, Section 6A/6E and analyst_note | "14.38% EBITDA margin (B00)" for the Q2 FY27 print | The 14.38% figure is the rounded presentation figure at Investor_Presentation_1 [page 35] (see V-07). B00 is an intake block and does not hold it. The filing basis is 14.42%. | Anchor points to the wrong source. The value exists in the corpus. |

Notes on V-01 and V-02. Both are Gate 0 scorecard inputs. Rule 5 sets CRITICAL only for a verdict-card or Section 1B pillar MISMATCH. These two items therefore carry MAJOR as the rule is written. The orchestrator should read section 5 before it reads the severity.

## 3. Rows struck and items not counted as findings

Struck under rule 5a (screener basis or rounding, labelled, not findings):
1. 01-gate0 Block D total assets FY26 332.13 (screener) against AR26 33,211.72 lakh (332.12 Cr). Screener basis, 0.01 Cr rounding.
2. 01-gate0 Block A PBT FY26 43.54 (screener) against AR26 4,353.45 lakh (43.53 Cr). Screener basis, labelled.
3. 01-gate0 Block A interest FY26 8.79 (screener) against AR26 finance costs 842.34 lakh (8.42 Cr). Screener basis, labelled. The ROCE line mixes screener PBT and interest with AR capital employed, and the report labels each input.
4. 01-gate0 Block B4 FY24 payables days 17.9 against 17.85 recomputed. Rounding.
5. Employee cost FY26 35.74 (screener) against 35.71 (AR26 3,570.88 lakh). Screener basis, used only in the M1 margin derivation.
6. V-05 (above): matched figure, page citation only.

Observation, not a finding: the H1 FY27 CFO of 1,610.76 lakh (results Q2 FY27 p.10) matches the consolidated basis. The p.10 table PBT of 1,691.60 ties to the consolidated p.8 figure. The table footnote at line 476 says "Standalone". The Gate 0 line gives no basis. The value is correct.

Re-computed and matched (no finding): all ten yearly ROE values and the 10-year median 11.37%; FY24 to FY26 ROCE (12.44%, 15.84%, 23.11%); cumulative CFO 119.06 and PAT 116.02; FY24 to FY26 capex 37.79, 5.70, 47.54; the FCF series; WC days 258.1, 210.4, 216.7; receivable days 73 and 175; FY26 margin 24.00% (AR26 p.167); Q2 FY27 revenue 5,773.04 against 6,244.47 (-7.55%); H1 FY27 11,941.25 against 10,266.09 (+16.3%); the coal segment assets 2,298.52 and 1,930.58 (results Q2 FY27 p.11); the coal block note 5 (p.12); promoter holding 68.85% and the FY25 change of -4.34 pp (AR26 p.133); contingent liabilities 2,250.08 and 562.62 (AR26 Note 42, p.185; column order garbled, both readings present); the stage 8 promoter share arithmetic (26,63,309 sold; 14,47,062 Vikas; 12,16,247 Piyush; 28.95 Cr first tranche; 62.8 Cr total); peer FY26 sales 791.05, 890.71 and 996.57 (Asian Energy, Deep Industries, Jindal Drilling data sheets); the 45 rigs (AR26 p.58).

## 4. Coverage statement (two counts, rule applied)

- Mandatory tier: 109 of 109 checked. The rule is "every Gate 0 scorecard input and load-bearing figure in 01-gate0.md", counted by occurrence. No verdict-card or Section 1B pillar input exists in Phase 1. No unchecked mandatory figure.
- Sample tier: 65 checked. Material universe enumerated: 65 (stage 3: 15, stage 8: 33, stage 9: 17). Stages 2, 4, 5, 6 and 7 were not enumerated, so the sample universe is at least 65 and unknown above that.
- Acceptance: 164 of 174 checked figures are clean (94.3%). Mandatory 104 of 109 (95.4%). Sample 60 of 65 (92.3%). Denominators are above 4, so the rate applies to the shadow comparison.
- Not checkable against the corpus: stage 8 web-sourced MEDIA figures (Trendlyne sale prices, bulk-deal print of Rs 162.56 on 9 Nov 2026, the Rs 450 crore coal headline, the Rs 200-220 crore CRISIL capex figure if not in the rating PDF). The RHP and SEBI pages are PENDING LIVE VERIFICATION in stage 8. The Q2 FY27 concall is not in the corpus. The Annexure-A prices may sit inside the Reg 29(2) PDFs; I did not check them.

## 5. Observations for the orchestrator (not findings)

- Gate 0 (stage 1) and stage 8 disagree on the promoter position. Stage 8 read the Reg 29(2) filings and the Gate 0 report did not. Stage 8 states the pledge reading as nil (four forms) and the holding as 61.70%. Gate 0 still says NOT FOUND and 68.85%. This is a sequencing gap, not a single-number error.
- Severity question for the operator. Rule 5 names only verdict-card and Section 1B pillar inputs as CRITICAL. V-01 and V-02 would move the Gate 0 scorecard (Block E is 8 of 20). If the operator wants Gate 0 scorecard MISMATCHES at CRITICAL, the rule text needs a change. This shadow run applies the text as written.
- No CRITICAL finding in this shadow run. No REWORK trigger from this run's acceptance rate.

## 6. Method limits

I checked numbers against the page-marked .txt twins. I did not open the PDFs. Where a number appears in both the AR and a stage report, I checked the AR .txt page marker. The Gate 0 score effects belong to Verifier C and the analyst stages. I did not judge classifications, premiums or determinations (rule 6).

```yaml
stage: B12a
company: "SOUTHWEST"
run_date: "2026-11-09"
model: claude-haiku-5-5
shadow_run: true
shadow_note: "Verifier A shadow run (operator ruling 2026-10-11). Findings bind nothing."
status: complete
numbers_checked: 174
mandatory_checked: 109
mandatory_total: 109
findings:
  - {severity: "MAJOR", location: "outputs/reports/01-gate0.md Block E E1; B01 data_notes", claimed: "E1 promoter holding 68.85% at 31 Mar 2026 on pre-warrant base 2,98,30,011; Jun-Sep 2026 disposals stated as not netted and outside inputs", source_truth: "Reg 29(2) filings in inputs/announcements: 20260625-9BA85695 p.2-3; 20260710-36543982; 20260813-9C8BA238 p.2-3; 6219323E_43E3 p.2-3 show 2,01,44,762 shares = 61.70% of 3,26,51,422 after sales; same 31 Mar holding on current base 62.90% (derived)", note: "68.85% correct as of 31 Mar 2026 on its base. The outside-inputs statement is contradicted by the corpus. E1 score rests on stale holding and pre-conversion base. Score effect is for Verifier C.", source_fidelity: true, tier: "mandatory"}
  - {severity: "MAJOR", location: "outputs/reports/01-gate0.md Block E E3; B01 analyst_note", claimed: "E3 pledge NOT FOUND (no pledge or encumbrance disclosure in AR FY26), scored 0", source_truth: "Reg 29(2) encumbrance line nil (dash) before and after: 20260625-9BA85695 p.2 and p.3; 6219323E_43E3 p.2 and p.3", note: "Absence claim contradicted by nil readings in corpus filings. Stage 8 reports nil in four forms; the 10 Jul and 12 Aug forms were not re-read by Verifier A.", source_fidelity: true, tier: "mandatory"}
  - {severity: "MAJOR", location: "outputs/reports/01-gate0.md load-bearing fact 1; data_notes", claimed: "Guidance of about 20% growth NOT FOUND in stage inputs (concall text not an input)", source_truth: "Annual_Report_2026.txt line 256 (CMD message, stage 9 anchors AR p.6): around 20 % growth year on year in short to medium term; Concall_May_2026_Transcript.txt line 194", note: "Guidance exists in an input the report cites. Label wrong.", source_fidelity: true, tier: "mandatory"}
  - {severity: "MAJOR", location: "outputs/reports/09-tam.md Cross-check on delivery", claimed: "FY23 to FY26 revenue CAGR 27.3% = (243.02 / 117.73)^(1/3) - 1", source_truth: "screener-Data_Sheet.csv Sales: FY22 117.73, FY23 124.26, FY26 243.02. FY23 to FY26 CAGR = 25.1%", note: "Base-year MISMATCH: uses FY22 value under an FY23 label. Delivery cross-check moves 27.3% to 25.1%.", source_fidelity: true, tier: "sample"}
  - {severity: "MINOR", location: "outputs/reports/01-gate0.md Block F M11", claimed: "prior 3-yr revenue CAGR 13.2% (FY20-23)", source_truth: "Screener Sales FY20 85.8, FY23 124.26 gives 13.1%", note: "Imprecision of 0.06 pp. No threshold affected.", source_fidelity: false, tier: "mandatory"}
  - {severity: "MINOR", location: "outputs/reports/01-gate0.md load-bearing fact 1; data_notes", claimed: "14.38% in company memory not reproduced on either basis", source_truth: "14.38% printed in inputs/presentation/Investor_Presentation_1.txt [page 32] and [page 35] (EBITDA 83 Mn / revenue 577 Mn); filing basis 14.42%", note: "Presentation anchor omitted. Rounding gap only.", source_fidelity: false, tier: "mandatory"}
  - {severity: "MINOR", location: "outputs/reports/08-promoter.md sections 3C, 6B, 6E; 03-ardeep.md line 216", claimed: "cash 88.81 lakh; CFO/PAT 0.40; FCF (3,520.26) lakh, no basis label in body", source_truth: "Standalone values (AR26 standalone CF line 6269: CFO 1,233.87; results Q2 FY27 p.5: PAT 3,080.05). Consolidated FY26: cash 129.40 lakh (AR26 p.166), CFO/PAT 0.38, FCF -35.09 Cr (B01)", note: "Unlabelled basis difference (rule 5a UNANCHORED). Label present upstream in B03 (S anchors). Not material.", source_fidelity: false, tier: "sample"}
  - {severity: "MINOR", location: "outputs/reports/08-promoter.md sections 6A and 6E; analyst_note", claimed: "14.38% EBITDA margin cited to B00 for Q2 FY27", source_truth: "Presentation [page 35] rounded figure 14.38%; filing consolidated basis 14.42%", note: "Anchor points to intake block, not to the source that holds the value.", source_fidelity: false, tier: "sample"}
critical_count: 0
major_count: 4
minor_count: 4
false_positives_struck: 6
material_universe: 174
acceptance_rate: 94.3
coverage_note: "Mandatory tier: 109 of 109 checked. Mandatory = every Gate 0 scorecard input and load-bearing figure in 01-gate0.md, counted by occurrence; derived ratios counted once. No verdict-card or Section 1B pillar input exists in Phase 1. Sample tier: 65 checked (stage 3: 15, stage 8: 33, stage 9: 17), drawn in materiality order. Stages 2, 4, 5, 6 and 7 not enumerated, so sample universe is a lower bound. Not checkable against corpus: stage 8 web-sourced MEDIA figures (Trendlyne prices, bulk-deal print, Rs 450 cr headline) and Q2 FY27 concall. Struck (6): five screener basis or rounding items under rule 5a (FY26 total assets 332.13 vs 332.12; FY26 PBT 43.54 vs 43.53; FY26 interest 8.79 vs AR 8.42 labelled screener; FY24 payables days 17.9 vs 17.85; employee cost 35.74 vs 35.71) plus one matched figure (2,430 Mn, page citation only). Acceptance: 164 clean of 174 checked (mandatory 104 of 109; sample 60 of 65)."
```
