# Verifier A: Numerical Accuracy. GVPIL, run 2026-11-15

Model: claude-sonnet-5-5. Inputs read: stage reports 01 to 09 (with 02 pass 1, 2, 3) and the source text files. Page anchors are the "[page N]" markers. AR figures are INR million; screener Data Sheets are INR crore.

## Result in short

- Mandatory tier (Gate 0 scorecard): 139 of 139 figures checked. 0 mismatches.
- Sample tier: about 290 of 431 material numbers checked. 8 findings: 0 CRITICAL, 4 MAJOR, 4 MINOR.
- 3 of the 4 MAJOR rows are source-fidelity findings (`source_fidelity: true`). They stand until the source PDF itself clears them.
- No verdict-card input and no Section 1B pillar input exists in these reports (stages 11 to 13 have not run). No CRITICAL is possible on this input set.

## Findings table

| # | Severity | Report location | Claimed (anchor) | Source truth (location) | Note |
|---|---|---|---|---|---|
| 1 | MAJOR, source_fidelity | 08-promoter.md Section 3A, materials purchased from group | INR M 697.6 (Note 36 p.181) | INR M 699.1 = 71.1 + 182.6 + 106.1 + 68.7 + 41.6 + 96.5 + 55.2 + 53.9 + 23.4 (AR26 Note 36 p.181, L 12421-12441). 02-notes-pass1 and 03-ardeep print 699.1 | Copy error. Context figure, not a pillar input |
| 2 | MAJOR, source_fidelity | 03-ardeep.md Phase 3B balance sheet table, "Other financial and other assets", FY26 | 1,432.7 (58.5 + 268.9 + 1,007.1 + 155.6 + 111.3 + 31.3) | 1,601.4 = 58.5 + 268.9 + 1,007.1 + 155.6 + 111.3 (AR26 standalone p.131). The listed parts as printed sum to 1,632.7 | The note under the table already gives 1,601.4 and drops the 31.3. The cell was not fixed. Rule 5 sets MAJOR |
| 3 | MAJOR, source_fidelity | 04-bizmodel.md Section 3B, material cost % row | Q2 FY27 67.6% against 60.2% healthy and a 67% red-flag line | 67.6% = 2,103.8 / 3,112.3 (Results Q2 FY27 p.3), gross of the (100.6) WIP change. The 60.2% and 67.3% bases are net of WIP change (AR26 p.132). Net Q2 FY27 is 64.4%, which 05, 06 and 07 use | Unlabelled basis difference (UNANCHORED, rule 5a). The red flag reads as tripped when the like-for-like figure is 64.4% |
| 4 | MAJOR | 09-tam.md Section 2 Method 2 | "about Rs 1.1 Cr per MW a year" (2,500 Cr over 224 GW) | Rs 2,500 Cr / 224,150 MW = Rs 0.0112 Cr = about Rs 1.1 lakh per MW | Cr versus lakh unit trap, 100x. Derived figure. The report says not to read it as a unit rate |
| 5 | MINOR | 02-notes.md (Section 3.6, rank 2, FLAG-EARNINGS, top_findings rank 2) | 55.3% of the 3,174.4 step-up | (1,320.0 + 433.5) / 3,174.4 = 55.24% = 55.2% | Rounding of rounded parts (41.6 + 13.7). 03-ardeep.md already flags and uses 55.2% |
| 6 | MINOR | 09-tam.md Section 3B second reading | CAGR 7.8% | (918/734)^(1/3) - 1 = 7.74% = 7.7% | Rounding |
| 7 | MINOR | 08-promoter.md Section 0 row 1 and flags; 02-notes.md 3.0.1, rank 7 | FY25 gap 382.4 next to "FY25 re-presented 121.5" | 382.4 = 514.5 less 132.1 (AR25 original). Against 121.5 the gap is 393.0 (02-notes-pass1 prints 393.0) | Unlabelled basis. Number is right on the AR25-original basis |
| 8 | MINOR | 09-tam.md Section 4A Utilisation row | PLF 65.2%, 66-68%, demand growth 0.8%, "(ICRA)" | None of the three is in inputs/rating/ICRA_Rationale_2026-03-03.txt. No ICRA URL in the Sources list | UNANCHORED. Reads as the corpus ICRA document. Not material to the 4% proxy |

## Mandatory tier: what was checked and how

Scorecard in 01-gate0.md. Every input was traced to the source column and recomputed.

- Screener Data Sheet (INR Cr): all ten years of Sales, PBT, Interest, Net profit, Equity capital, Reserves, Borrowings, CFO, Receivables, Cash, Net block, Market cap. Rebuilt EBIT, capital employed proxy and ROCE for FY17 to FY26 (10.3, 9.0, 22.7, 23.0, 12.7, -18.2, -43.0, -43.2, 71.6, 48.4). Rebuilt ROE on average net worth for FY18 to FY26. Medians 11.5 and 5.4 reproduce. FY26 EBITDA 269.14 reproduces from the expense lines with change in inventory as a credit.
- Cumulative CFO 365.60, cumulative PAT -190.51, FY24 to FY26 CFO 1,030.80 and PAT 284.28 (3.63x), FCF 180.08, 376.01, 467.23 and 1,023.32 (3.60x). All reproduce. Capex 21.3, 30.3 (AR26 p.215) and 23.2 (AR25 p.249) found.
- Revenue CAGR -4.9% (9 years) and -10.9% (3 years) reproduce. Up-years 5 of 9 reproduce.
- AR26 consolidated: revenue 12,693.9, cost lines, finance cost 219.0, PBT 3,285.8, PAT 2,526.1 (p.214); CFO 4,693.6, receivables +5,136.5, other current liabilities (2,158.3), loan 4,500.0 (p.215); current assets 19,200.1, current liabilities 14,363.0 and 16,172.4, equity 5,825.4, payables 494.8 + 5,035.2 and 540.0 + 4,692.8, lease 63.9 and 112.0 (p.213). Loss allowance (1,016.6) and royalty 125.7 and 121.5 (p.252). Contingent 2,036.7 + 132.6 + 1,105.8 + 1,300.8 = 4,575.9 (p.268). R&D "Nil" (p.58).
- Derived: EBITDA 2,595.2 = 20.4%; 26.8% of PBT before exceptional; 12.4% ex credit; other income 34.9% of PBT; WC days 219.2, 43.0, 159.0, 103.2 and 408.9, 30.7, 182.4, 257.2; current ratio 1.34; TA less CL ROCE 41.4% and 62.6%; FAT 31.6x; contingent over net worth 78.6%. All reproduce.
- Results Q2 FY27 p.3: Q1 margin 447.2 = 14.5%; Q2 306.3 = 9.8%; Q2 FY26 279.5 = 10.0%; other income 312.8 / 529.8 = 59.0%; H1 631.6 / 1,218.0 = 51.9%.
- Peers: EBITDA 2,571.79 / 583.04 / 702.20; margins 7.6%, 8.6%, 11.6%; median 8.6%; gross margin proxy 59.7%, 50.9%, 45.4%, 85.7%; market caps. All reproduce.
- Shareholding CSV: promoter 68.58% in Dec 2023 and Sep 2026.
- Score sums: Block A 6, B 2, C 1, D 16, E 8, core 33, moat 11, total 44. All add.

Correctly labelled basis differences were not scored as findings: Gate 0 uses AR26 consolidated (CFO 4,693.6, equity 5,825.4) and stages 2 to 9 use standalone (CFO 4,692.5, equity 5,437.7). Both are labelled.

## Sample tier: what was checked

- Stage 2 (pass 1, 2, 3 and consolidation): Notes 26, 27, 28, 29, 33, 35, 36, 39, 47, 52 to 54 values; related-party sums (435.7, 514.5, 851.9, 318.4, 699.1, 241.0); provision roll-forwards and the 299.2 and 322.7 bounds; Durgapur block 280.3 and expense lines 548.0; RPO 16,278 / 26,623 / 15,870 and derived 2,347.7; net cash 8,473.1 / 3,973.1; profit bridge to 3,174.4; core margin 16.1% and 4.5%; receivable ageing and AR25 FY24 comparatives; AR25 to AR26 re-presentation 604.8 and its four parts; contingent growth 5.6% and 7.1% (reproduces from 4,046.4, 4,274.2, 4,575.9).
- Stage 3: CARO table sums (8,022.1, 7,658.3, gap 3,446.2); cash flow table including AR25 comparatives; margin waterfall; ROE, ROCE, DuPont, dividend and CFO ratios; MD&A ratios p.93; Notice figures for LM Wind (turnover 25,488.7, PAT 2,917.1, net worth 9,366.2) and guarantee peak 20,432; NGSL book and inflow; BHEL 3,430.6 and 1,050.5; BRSR turnover 71.11%.
- Stage 4: Q4 deck slide values (1,218, 1,124, 3,615 / 3,309 / 2,662 / 1,631, 877, 734, 1,364, 162 to 320); Q4 call quotes (85-90%, 11%, 18%, 1,628, 116 / 22 / 18 Cr, 3,500-4,000, 18%); 7,749 termination (Results Q1 FY27); order bridge 10,097 vs 8,770; Q1 and Q2 margin rebuilds; Note 35 split and geography.
- Stage 5: Q2 and Q3 call quotes (1,825, 162 vs 112, 25 and 27 Cr, 1,671 with 450, 14.5% and 10%, plus or minus 5%, 5-8%, 300-320, 30% plus, 60% to 80%, 216 and 125 Cr); backlog 15,273 and 15,454; BHEL reversal 235 + 371.8 + 443.7 = 1,050.5; Shoaiba 550 Cr.
- Stage 6: Power Mech, ISGEC and BHEL quotes (15-16%, 12.3%, 4,260, 17,000, 936, 18%, 10-11%, 800 Cr, 13.7%, 5.7%, 10,273, 502, 1,563, 7,210, 176 Cr at 10.8%, 750 Cr, 1,093).
- Stage 7: scorecard sum 11.6; QPPL 18 / 25 / 10 Cr, 7% and 53 weeks; GST order 2,109,252; Durgapur PPE 65.0 and 17.4; outside-India revenue 349.5 and 361.7; derived 43.6%, 7.3%, 51.5x.
- Stage 8: Notice 4,156.4, 13,000, 6.71%; GST penalty 319,483,311 (BRSR p.56); CS resignation date; shareholding CSV values.
- Stage 9: funnel arithmetic (29.4%, 18.4%, 2,812, 3,042, 883, 986, 6.4%, 6.1%, 918, 12.8%, 3.4x, 5.4x, 59%).

## Rule 5b self-check

Rows drafted and then struck (4):
1. "Contingent liabilities grew 5.6%" (02-notes top finding 9): reproduces. 4,274.2 / 4,046.4 = 5.63% is the FY25 growth (AR25 p.168 note, lines 13464-13467).
2. CFO 4,693.6 (Gate 0) against 4,692.5 (stages 2 and 3), and equity 5,825.4 against 5,437.7: consolidated and standalone, each labelled. Basis difference correctly labelled (rule 5a).
3. ICRA upgrade dated 2 Mar 2026 (03-ardeep, AR26 p.115) against 3 Mar 2026 (other stages, ICRA document): each date is in its own source. Matched.
4. BHEL ECL reversal "about Rs 116 Cr" (04, 05) against 105.05 Cr: the report quotes the CFO's spoken figure faithfully (Q4 call p.6) and 05 flags the gap itself. Faithfully transcribed (rule 5a).

Each remaining row has a claimed value that differs from the source value (rows 1 to 4 and 7 by a different number; rows 5 and 6 by rounding; row 8 is a missing anchor). Only rows 1, 2 and 3 carry `source_fidelity: true`. Row 4 is a derived-figure error, not a question of what the source contains, so it stays false.

## Clearance path for the source-fidelity rows

- Row 1: clears only if AR26 Note 36 p.181 shows 697.6 as the sum of the materials lines. It does not.
- Row 2: clears only if AR26 p.131 shows the FY26 other-asset lines summing to 1,432.7. They sum to 1,601.4.
- Row 3: clears when 04-bizmodel.md labels 67.6% as gross of WIP change or restates it as 64.4% net. The PDF figures (2,103.8, 100.6, 3,112.3) are not in dispute.

## Coverage statement

Mandatory tier: 139 of 139 figures checked (rule: every Gate 0 scorecard input and load-bearing fact rebuild; no verdict-card or Section 1B figure exists in Phase 1). Sample tier: 431 material numbers counted (a number that feeds a scorecard, table, flag, guidance row or trigger), about 290 checked.

Not checked: web-sourced figures in 09-tam.md (CEA GW figures, CREA 44 GW, IMARC USD 1,043.6M, BHEL Rs 75,000 Cr) and 08-promoter.md (SEC USD 200M, vote percentages, 10 Dec 2025 NSE filing); eight of twelve peer transcripts beyond the quoted passages; press-release page numbers (p.23) in Results Q4 FY26 (values found, page not re-opened). Pages that could not be read: none. Every cited .txt page opened.

```yaml
stage: B12a
company: "GVPIL"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
numbers_checked: 429
mandatory_checked: 139
mandatory_total: 139
findings:
  - {severity: "MAJOR", location: "08-promoter.md Section 3A, 'Purchases from group: materials INR M 697.6 FY26 across named suppliers'", claimed: "INR M 697.6 (Note 36 p.181)", source_truth: "INR M 699.1 = 71.1 + 182.6 + 106.1 + 68.7 + 41.6 + 96.5 + 55.2 + 53.9 + 23.4 (AR26 Note 36 'Purchase of materials and components', fellow subsidiaries, p.181, L 12421-12441). 02-notes-pass1.md and 03-ardeep.md both print 699.1", note: "Copy error in stage 8. The source column sums to 699.1, not 697.6. Context figure, not a pillar input. Clears only if the PDF shows 697.6", source_fidelity: true}
  - {severity: "MAJOR", location: "03-ardeep.md Phase 3B balance sheet table, row 'Other financial and other assets', FY26 cell", claimed: "1,432.7 (58.5 + 268.9 + 1,007.1 + 155.6 + 111.3 + 31.3)", source_truth: "1,601.4 = 58.5 + 268.9 + 1,007.1 + 155.6 + 111.3 (AR26 standalone balance sheet p.131, L 8908-8938). The listed components as printed also sum to 1,632.7, not 1,432.7", note: "The report's own note under the table gives 1,601.4 and calls the 31.3 an extra item, so the reader is told. The table cell itself still holds the wrong value. Severity follows rule 5 (MISMATCH outside the pillar set is MAJOR)", source_fidelity: true}
  - {severity: "MAJOR", location: "04-bizmodel.md Section 3B must-track table, row 'Material cost % of revenue' (healthy 60.2% FY26, red flag 'Back above 67% (Q2 FY27 67.6%, calc)')", claimed: "Q2 FY27 material cost 67.6% of revenue, shown against a 60.2% healthy level and a 67% red-flag line", source_truth: "67.6% = 2,103.8 / 3,112.3 (Results Q2 FY27 p.3), which is cost of material and erection WITHOUT the (100.6) WIP change. The 60.2% FY26 base and the 67.3% FY25 base are NET of WIP change (AR26 p.132). On the same net basis Q2 FY27 is (2,103.8 - 100.6) / 3,112.3 = 64.4%, the figure 05-concall.md, 06-peers.md and 07-emoat.md use", note: "Unlabelled basis difference, reported as UNANCHORED per rule 5a. It makes the 67% red flag read as tripped when the like-for-like figure is 64.4%. Clears when the row states the gross basis or uses 64.4%", source_fidelity: true}
  - {severity: "MAJOR", location: "09-tam.md Section 2 Method 2 (bottom-up)", claimed: "'management's 2,500 over 224 GW is about Rs 1.1 Cr per MW a year (calc)'", source_truth: "Rs 2,500 Cr / 224,150 MW = Rs 0.0112 Cr per MW = about Rs 1.1 lakh per MW per year. Inputs are right (2,500 Cr, Q3 FY26 call; 224.15 GW coal, web). The ratio is out by 100x (Cr versus lakh unit trap)", note: "Derived figure, not a source number. The report adds 'do not read it as a unit rate', so no decision rests on it. Severity follows rule 5", source_fidelity: false}
  - {severity: "MINOR", location: "02-notes.md Sections 3.6, A rank 2, FLAG-EARNINGS and top_findings rank 2 ('55.3% of the INR M 3,174.4 step-up'); also 03-ardeep.md rank-2 row shows the claimed 55.3%", claimed: "55.3%", source_truth: "(1,320.0 + 433.5) / 3,174.4 = 55.24% = 55.2%. 55.3 is the sum of the rounded parts 41.6 + 13.7 in 02-notes-pass2.md B5. Inputs tie to AR26 p.132-133, 167-168", note: "Rounding only. 03-ardeep.md already flags it and uses 55.2% from Phase 3 on; 02-notes.md was not updated", source_fidelity: false}
  - {severity: "MINOR", location: "09-tam.md Section 3B 'Second reading on 4,000'", claimed: "CAGR 7.8% (918 over 734, three years)", source_truth: "(918 / 734)^(1/3) - 1 = 7.74% = 7.7%", note: "Rounding. Neighbouring 6.4%, 6.1% and 12.8% all reproduce", source_fidelity: false}
  - {severity: "MINOR", location: "08-promoter.md Section 0 row 1 and flags ('Gap to P&L INR M 310.0 FY26, 382.4 FY25'); 02-notes.md 3.0.1 and Top-15 rank 7 (FY25 gap 382.4)", claimed: "FY25 gap 382.4 stated beside 'FY25 re-presented 121.5'", source_truth: "382.4 = 514.5 (Note 36 FY25, not re-presented) less 132.1 (AR25 original royalty line). Against the re-presented 121.5 the gap is 393.0, the figure 02-notes-pass1.md prints. Both inputs are in the sources", note: "Unlabelled basis difference. Number exists and is right on the AR25-original basis, but the surrounding text names 121.5 as the FY25 line", source_fidelity: false}
  - {severity: "MINOR", location: "09-tam.md Section 4A Drivers row 'Utilisation': 'PLF 65.2% FY26 (ICRA), 66-68% FY27 forecast (ICRA); FY26 demand growth 0.8% (ICRA)'", claimed: "PLF 65.2%, 66-68%, demand growth 0.8%, attributed to ICRA", source_truth: "None of the three figures is in inputs/rating/ICRA_Rationale_2026-03-03.txt. The Sources list names no ICRA URL. The report's own log says external figures carry the search tool's attribution", note: "UNANCHORED. Reads as the corpus ICRA document, which does not contain them. Not material to the 4% growth proxy. External web figures in stage 9 and stage 8 cannot be checked against corpus PDFs (see coverage_note)", source_fidelity: false}
critical_count: 0
major_count: 4
minor_count: 4
false_positives_struck: 4
material_universe: 570
acceptance_rate: 98
coverage_note: "MANDATORY TIER (OR-32): Phase 1 holds no verdict card and no Section 1B pillar input (stages 11 to 13 not run). The tier is the Gate 0 scorecard in 01-gate0.md: 139 figures counted (10-year ROCE and ROE rows 20; Block A tests 5; Block B 29; Block C 6; Block D 12; Block E 10; Block F 27; load-bearing fact rebuilds 30). 139 of 139 checked against screener-Data_Sheet.csv, BHEL, ISGEC and POWERMECH Data Sheets, the shareholding CSV, AR26 consolidated p.213-215, p.252, p.268, AR25 p.249, AR26 p.58 and Results Q2 FY27 p.3. No mismatch. SAMPLE TIER: material = a number that feeds a scorecard, table, flag, guidance row or trigger; my count is 570 in total including the 139 above, so 431 sample numbers. Checked about 290 of 431 (all stage 2 and 3 top-15 and Phase 1-3 figures, stage 4 and 5 guidance and quote anchors, stage 6 peer quotes, stage 7 scorecard sums and filing anchors, stage 8 RPT and Notice figures, stage 9 funnel arithmetic). NOT CHECKED: web-sourced figures in 09-tam.md (CEA 224.15 GW, 228,560 MW, 44 GW CREA, 9.4 vs 12.8 GW, IMARC USD 1,043.6M, BHEL Rs 75,000 Cr) and 08-promoter.md (SEC USD 200M, 99.99% and 99.9359% votes, 10 Dec 2025 NSE filing): no PDF in the corpus. 08 yaml searches and the companies/GVPIL.md memory leads (27.0%, 48%, Rs 13.21 cr) are not source documents and were not treated as claims. Eight of 12 peer transcripts and the Q2 FY26 and Q3 FY26 call pages beyond the quotes listed were sampled by keyword, not read in full. Q4 FY26 and Q1 FY27 results press-release page numbers (p.23) were not re-opened; the 27.0% and 22.5% figures were found in the files at the stated values. Page anchors: stage reports use '[page N]' markers (AR, deck) and, in 04-bizmodel.md, the printed 'Page N of 16' for the Q4 call; each lands within one page of the quote and was not scored as a finding."
```
