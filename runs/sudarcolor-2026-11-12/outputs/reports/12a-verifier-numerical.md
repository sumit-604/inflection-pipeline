# Verifier A: Numerical accuracy. SUDARCOLOR, run 2026-11-12

Inputs read: stage reports 01 to 09 (with 02 pass 1 and pass 2), B01 block, and the source files named in the task. Method: every claim located in the page-marked .txt beside its PDF. Results_Q2FY27 page 3 was opened as an image because the text layer carries an OCR error.

Overall read: the stage reports are accurate. All filing-sourced figures I tested tie, with seven mismatches and four weaker anchors listed below. Four of the seven mismatches come from a single sign error in the Gate 0 margin derivation (inventory line), which reaches stage 4.

## Findings table

| # | Severity | Report location | Claimed (anchor) | Source truth (location) | Note | SF |
|---|---|---|---|---|---|---|
| 1 | MAJOR | 01-gate0 Block F M2; 04-bizmodel 2B, FLAG-MOAT, must-track; B01 and B04 yaml | FY26 EBITDA margin SUDARSCHEM 9.63%, MOL 11.88%, ASAHISONG 9.31%, peer median 9.63% (screener peer sheets) | SUDARSCHEM 6.16%, MOL 8.17%, ASAHISONG 9.31%, median 8.17%. Ties to sheet PBT (SUDARSCHEM 603.3 + 74.8 - 347.2 - 174.3 = 156.6; MOL 177.56 + 95.29 - 118.95 - 91.86 = 62.04). Sheets: SUDARSCHEM-Data_Sheet.csv, MOL-Data_Sheet.csv, FY26 column | The reported 9.63 and 11.88 need the Change in Inventory line added with the wrong sign; that version does not tie to PBT. Company 7.42 vs 8.17 is 0.75pp, inside the +/-2pp band, so M2 scores 1 not 0 (prompts/01 M2) | yes |
| 2 | MAJOR | 01-gate0 Block F M9; 04-bizmodel lines 45, 139, 253, 287, 321 | Peer gross margin proxy median 42.71% vs company 39.26%, M9 = 0 | Peers: SUDARSCHEM 49.20%, MOL 39.00%, ASAHISONG 33.94%; median 39.00%. 42.71 is MOL with the inventory sign reversed. Company 39.26% correct | Company is 0.26pp above the corrected median; M9 rule "above peers but growth below = 1". Stage 4 "peers 42.7%" repeats the error | yes |
| 3 | MAJOR | 01-gate0 Block F line 48 | EBITDA margin FY17 7.06% | 6.84% (67.13 / 980.98); ties to FY17 PBT 36.29 (screener-Data_Sheet.csv FY17) | Same sign error. FY26 7.42% is right. M1 = 0 either way | yes |
| 4 | MAJOR | 08-promoter line 146 (and B08 yaml); 04-bizmodel line 175; 05-concall line 43 | H1 FY27 PBT 59.87; operating EBITDA 60.27 (12.2%) | PBT 59.67 on the PDF image (Results_Q2FY27 p.3); 502.98 - 443.31 = 59.67; cash flow p.5 starts at 59.67. Operating EBITDA 60.07, still 12.2% | The .txt layer misreads 59.67 as 59.87; the report copied it. No conclusion moves | yes |
| 5 | MAJOR | 02-notes rank 4; B02 yaml FLAG-CASH, top_findings, red_flags | 24.76 "release of government balances" in OCF; OCF ex-release 9.48 | 24.76 = 28.96 + 2.52 - 6.72 (three cash flow lines, AR FY26 p.76). Government balances alone net 20.53 (Notes 8, 14 pp.83, 85). OCF ex 20.53 = 13.71 | B03 caught this in its own report; stage 2 still carries it. The sum is right, the label is wrong | yes |
| 6 | MAJOR | 08-promoter 1B and 3B | 2,30,81,978 shares | 2,30,81,798 (AR FY26 p.66, Note 15 p.86, Note 36 p.90) | Transposed digits twice. Derived Rs 272.95 per share unaffected | yes |
| 7 | MAJOR | 08-promoter 6D | Institutional holding 0.70% (0.51 + 0.20, Dec-2025) | 0.71% (screener shareholding, Dec 2025 column) | Sum off by 0.01 against its own components | yes |
| 8 | MINOR | 08-promoter reconciliation row 2, analyst_note | Brief says CMP about Rs 386 | Brief line 11 says Rs 381; data sheet says 385.5 | Wrong artefact cited; 455.25 media figure not testable | yes |
| 9 | MINOR | 06-peers line 15, Claim 8 | SUDARSCHEM Q1 FY27, Mukhopadhyay, p.10 | Printed Page 9 of 14 (file p.10), lines 372-378 of the transcript | Quote exact; report uses printed pages elsewhere and those tie | yes |
| 10 | MINOR | 01-gate0 Block B line 24 | Payables FY24 175.18, FY25 159.03 "AR FY25 p.65 area" | AR FY25 p.64 balance sheet and p.74 Note 19; p.65 is cash flow | Values right, anchor weak | yes |
| 11 | MINOR | 08-promoter 1C | Roy appointment date "UNVERIFIED" (25-Nov-2024 vs 22-Jan-2025) | AR FY26 p.29 Annexure C note b: effective November 25, 2024 | A filed document answers it; not a numeric mismatch | no |

Struck at self-check (3): FY25 group sales 28.5% in 03 (derived 234.91 / 825.06; BRSR prints 28.4% on another basis, a correctly derived basis difference); ASAHISONG Blue "370-400" (an analyst's figure in the call, copied correctly; attribution is judgment); stage 7 R1 labelled documented in the recount and scored at the 0.7 claim multiplier (a classification matter, goes to Verifier C).

## What was checked and held (selection)

- Gate 0: all ten ROCE years recompute (FY17 4.11 ... FY26 6.46; median 7.98; sensitivity median 10.2, min 4.8); ROE series; cumulative CFO 556.49 and PAT 534.73; capex FY24 16.52 (1,652.46 lakh, AR FY25 p.65), FY25 11.89, FY26 28.72; FCF 77.99, 98.70, 5.52; revenue CAGR -2.50%, PAT CAGR 6.87%; D1 to D4 including current assets 588.08 and current liabilities 203.35 (Q2 FY27 p.4, Mar-26 column); contingent liabilities 14.61 + 34.63 + 1.52 = 50.76 (AR FY26 p.90); promoter 54.37 to 70.26; mcap 9392.11 / 1401.53 / 425.33; FAT 4.72x; selling cost 6.80% and 8.93%.
- Load-bearing: Q2 FY27 revenue 269.76 vs 183.14; H1 balances (255.22 / 156.15; 244.95 / 179.39; 276.89 / 166.33; CFO -24.11); note 10 (36,68,036 shares, 15.89%, Rs 150.76 Cr, Rs 411); 760.63 appears in no source file.
- Note 40: every group sales and purchases line sums to 191.40, 159.15, FY25 234.91 and 80.72; balances 56.56 and 43.87. Note 19 ageing 62.32 overdue; Note 10 ageing 164.34 not due, 4.60 over six months; Note 24 other income lines; Note 30 lines; Note 47 ratios; Annexure C pay; BRSR RPT shares.
- Stage 5 to 7 derived margins (Q1 11.5%, Q2 12.8%, gross margins 39.5 / 39.1 / 41.0 / 41.7), net trade WC 223.28, liquid assets 206.11, FAT-based capex-embedded growth 5.6%, EM total 9.9.
- Stage 9: FX 93.45 from AR p.89, chart 5.0 / 3.0 / 0.6 (p.17), every TAM, SAM, SOM, CAGR and capacity-gap figure recomputes.
- Stage 6: ten peer quotes and numbers verified against the transcripts (MOL 131 / 161 and 39% / 51%, 125-day receivables, hangover quote, SUDARSCHEM NWC 23.6%, 8.19% promoter holding, intercompany quote, Rs 411 reply text).

## Coverage statement

Mandatory tier (OR-32): 35 figures counted, 35 checked, none unchecked. Count rule: every Gate 0 scorecard input in 01 (A: 6, B: 4, C: 4, D: 4, E numeric: 3, F numeric: 6), the five load-bearing facts in 01, and three Section 1B-adjacent inputs handed on (EM score 9.9, capex-embedded growth 5.6, SOM CAGR 10.9). Three of the 35 carry findings (M2, M9, M1). No verdict card or Section 1B worksheet exists at stages 1 to 9.

Sample tier: about 480 material numbers counted (a number that feeds a flag, scorecard cell, table judgment or trigger; derived ratios counted once). About 215 checked, in order of materiality. Not checked: pass 1 per-note detail beyond the Top 15, most peer quotes beyond ten, BRSR energy lines, FY25 AR comparatives other than capex and payables. Web-sourced figures in stages 8 and 9 have no corpus PDF and are not audited here. The three scanned announcement PDFs were not read; no report figure depends on them alone.

Severity note. Rule 5 makes CRITICAL only a verdict-card or Section 1B pillar input. A Gate 0 scorecard input is mandatory-tier but is neither, so findings 1 to 3 are MAJOR. If the orchestrator rules Gate 0 scorecard inputs to be verdict-card inputs, findings 1 and 2 escalate and the OR-29 REWORK trigger fires. I have not made that call.

## Hand-off to Verifier C and the orchestrator

Findings 1 and 2 change two Gate 0 Block F rows: M2 from 0 to 1 and M9 from 0 to 1 on the prompt rubric, so Block F reads 2 and the grand total 62 instead of 60. The prompt matrix may leave the class at AVERAGE through deal-breaker 3; Verifier C owns that re-derivation. Only the source PDF can clear any finding above, and each clearance is a logged disagreement.

```yaml
stage: B12a
company: "SUDARCOLOR"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
numbers_checked: 250
mandatory_checked: 35
mandatory_total: 35
findings:
  - {severity: "MAJOR", location: "01-gate0.md Block F M2; 04-bizmodel.md and B04 yaml repeats", claimed: "peer EBITDA margins SUDARSCHEM 9.63, MOL 11.88, median 9.63; M2 = 0", source_truth: "SUDARSCHEM 6.16, MOL 8.17, median 8.17 (screener peer sheets FY26; ties to PBT)", note: "inventory sign error; M2 scores 1 on corrected median", source_fidelity: true}
  - {severity: "MAJOR", location: "01-gate0.md Block F M9; 04-bizmodel.md repeats", claimed: "peer gross margin proxy median 42.71; M9 = 0", source_truth: "median 39.00 (SUDARSCHEM 49.20, MOL 39.00, ASAHISONG 33.94); company 39.26 above median", note: "inventory sign error; M9 scores 1", source_fidelity: true}
  - {severity: "MAJOR", location: "01-gate0.md Block F line 48", claimed: "FY17 EBITDA margin 7.06", source_truth: "6.84 (67.13 / 980.98; ties to PBT 36.29)", note: "same sign error; M1 unchanged", source_fidelity: true}
  - {severity: "MAJOR", location: "08-promoter.md line 146; 04-bizmodel.md line 175; 05-concall.md line 43", claimed: "H1 FY27 PBT 59.87; operating EBITDA 60.27", source_truth: "PBT 59.67 on PDF image p.3; operating EBITDA 60.07", note: "text-layer OCR error copied; margin 12.2 unchanged", source_fidelity: true}
  - {severity: "MAJOR", location: "02-notes.md rank 4; B02 yaml", claimed: "24.76 release of government balances; OCF ex-release 9.48", source_truth: "24.76 is three cash flow lines (AR FY26 p.76); government balances alone 20.53; OCF ex 20.53 = 13.71", note: "label error, already caught in B03", source_fidelity: true}
  - {severity: "MAJOR", location: "08-promoter.md share count", claimed: "2,30,81,978 shares", source_truth: "2,30,81,798 (AR FY26 p.66, Note 15 p.86)", note: "transposition, derived per-share price unaffected", source_fidelity: true}
  - {severity: "MAJOR", location: "08-promoter.md 6D", claimed: "institutional holding 0.70% (0.51 + 0.20)", source_truth: "0.71% (screener shareholding Dec 2025)", note: "sum off by 0.01", source_fidelity: true}
  - {severity: "MINOR", location: "08-promoter.md reconciliation row 2", claimed: "brief says CMP about Rs 386", source_truth: "brief says Rs 381; data sheet 385.5", note: "wrong artefact cited", source_fidelity: true}
  - {severity: "MINOR", location: "06-peers.md Claim 8", claimed: "Mukhopadhyay reply at p.10", source_truth: "printed Page 9 of 14 (file p.10)", note: "quote exact, page off by one", source_fidelity: true}
  - {severity: "MINOR", location: "01-gate0.md Block B line 24", claimed: "payables from AR FY25 p.65 area", source_truth: "AR FY25 p.64 balance sheet and p.74 Note 19", note: "values right, weak anchor", source_fidelity: true}
  - {severity: "MINOR", location: "08-promoter.md 1C", claimed: "Roy appointment date UNVERIFIED", source_truth: "AR FY26 p.29 prints November 25, 2024", note: "NOT FOUND is wrong; no number mismatch", source_fidelity: false}
critical_count: 0
major_count: 7
minor_count: 4
false_positives_struck: 3
material_universe: 480
acceptance_rate: 95
coverage_note: "Mandatory 35 of 35 checked (Gate 0 scorecard inputs, five load-bearing facts, three 1B-adjacent inputs); three carry findings. No verdict card or Section 1B worksheet exists at stages 1-9, so rule 5 CRITICAL was not reachable; M2 and M9 are MAJOR by literal rule 5 and escalate to CRITICAL only if the orchestrator rules Gate 0 scorecard inputs to be verdict-card inputs. Sample: about 480 material numbers, about 215 checked. Web-sourced figures in stages 8 and 9 and three scanned announcement PDFs not audited."
```
