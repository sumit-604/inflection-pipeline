# VERIFIER A: NUMERICAL ACCURACY, SOUTHWEST, run 2026-11-09

Model claude-sonnet-5-5. Sources read: the .txt twins of Annual_Report_2026 and Annual_Report_2025, Results_Q2FY27 / Q1FY27 / FY26, Investor_Presentation_1 (Nov 2026) and the filed May 2026 deck, the three SOUTHWEST concalls, the 12 peer transcripts (targeted greps), the announcements folder (Reg 29(2), AGM results, Alara filings, Q3 FY26 results, 8 Nov press release), and screener Data_Sheet for SOUTHWEST and the three peers. Text twins were readable at every page checked. No PDF was opened.

Units and basis traps checked first: INR Lakh vs Cr (all Gate 0 conversions use /100 and hold), standalone vs consolidated (Gate 0 uses consolidated; B03 and B05 label S and C), FY vs quarter vs TTM (B09 TTM PAT 35.59 and revenue 259.78 tie to screener quarters), CFO classification (finance cost sits in financing in the AR, as B03 states).

## Findings table

| # | Severity | Report location | Claimed (anchor) | Source truth (location) | Note |
|---|---|---|---|---|---|
| 1 | MAJOR, source_fidelity | 09-tam.md Section 3B cross-check and Section 5B | FY23 to FY26 revenue CAGR 27.3% = (243.02 / 117.73)^(1/3) - 1, "DS Sales row" | Data_Sheet Sales row: FY22 117.73, FY23 124.26, FY26 243.02. Correct FY23-26 CAGR 25.1% (Gate 0 M11 also says 25.1%) | Wrong base-year cell (FY22 value used as FY23). Saturation years move from 9.6 to about 10.9. No pillar input touched |
| 2 | MAJOR, source_fidelity | 04-bizmodel.md Section 4D, question 4 | "revenue growth of INR 6,263 L (standalone)" | Standalone 24,292.95 - 17,919.32 = 6,373.63 L (Results Q2 FY27 p.5; AR S p.114). Consolidated 6,272.67 L (AR C p.167). Neither gives 6,263 | Arithmetic slip. The 4,456.25 L receivable figure beside it ties (AR S p.115) |
| 3 | MAJOR, source_fidelity | 03-ardeep.md Phase 2-V rank 10; B03 yaml discrepancies rank 10 | B02's 855.35 "not reproducible"; visible parts sum to 697.52 | 668.20 (loans; AR S Note 48/49 table, [page 148-149]) + 56.91 (Other Receivables, Note 16 S, [page 132]) + 130.24 (debtors, Note 48 S, [page 148]) = 855.35, 4.22% of 20,251.42 | Stage 3 raised a discrepancy against a figure the AR supports. B02 pass 2 P2-2 shows the build |
| 4 | MAJOR, source_fidelity | 03-ardeep.md Phase 2-V rank 11; B03 yaml discrepancies rank 11 | B02's "depreciation rose 150.50" not reproduced; AR shows +184.48 | Plant depreciation 780.24 to 930.74 = +150.50 (AR S Note 2, depreciation lines near [page 127]). Total +184.48 is also correct but a different basis | Stage 3 tested a plant-block figure against total depreciation. With ranks 10 and 11 cleared, B03 verified count is 14 of 15, not 12 |
| 5 | MINOR | 01-gate0.md E2 | FY25 change -4.34pp (Vikash -2.74, Piyush -1.60) | The two printed lines sum to -4.34. Promoter group 73.61% to 68.85% = -4.76pp (AR25 line 6936) | Components named; headline omits group total. E2 score unchanged (0) |
| 6 | MINOR | 01-gate0.md load-bearing fact 1 | standalone Q2 FY27 margin 13.92% | 800.71 / 5,750.03 = 13.925%, rounds to 13.93% | Truncation |
| 7 | MINOR | 01-gate0.md M11 | prior 3-yr CAGR 13.2% (FY20-23) | (124.26 / 85.80)^(1/3) - 1 = 13.14%, rounds to 13.1% | Rounding. Tier unchanged |
| 8 | MINOR | 02-notes.md rank 9; pass 2 P2-7; B02 rank 9 | margin-money cover "of guarantees" 61.2% | 61.2% = 1,390.57 / 2,273.57 non-fund limits. On guarantees 2,250.07 it is 61.8% | Basis label wrong, arithmetic right. B03 listed it as a discrepancy; it is a label issue |

critical_count 0, major_count 4, minor_count 4.

Rows 5 to 8 are derived-value rounding, scope or label issues. None asserts that a number sits in the source that does not, so they are not marked source_fidelity. Rows 1 to 4 are marked source_fidelity: true and stand until the PDF disproves them.

## Rule 5b self-check (struck rows)

Eight candidate rows were struck before emit:
1. 14.38% (deck p.32 and p.35, B03/B04/B05/B07/B08/B09) vs 14.42% (Gate 0, results p.8). Both exist. The deck prints 14.38% (83 / 577 on rounded Mn); the lakh-level build gives 14.42%. Gate 0 says "not reproduced" from the filing, which is true. Basis difference, labelled.
2. Contingent liabilities 2,250.08 (bank guarantee line, Gate 0) vs 2,250.07 (printed total, B03); 2,812.70 vs 2,812.69. Both printed in Note 42 [page 185].
3. Revenue 24,302.17 (C) vs 24,292.95 (S): labelled bases.
4. EBITDA 24.00% (derived from lakh) vs 23.99% (company, Mn): rounding.
5. Receivables +57.0% gross vs +56.6% net (B03): labelled.
6. Gate 0 FY25 WC days 210.4 vs sum of rounded parts 210.3: parts are unrounded.
7. Rig count 45 / 47 / 43 / 40 across documents: faithfully transcribed anomaly, each count exists at its anchor.
8. B05 employee cost 13.7% Q2 FY26 (13.75%): rounding.

No severity was lifted for importance. No row is CRITICAL because none is a verdict-card or Section 1B pillar input (stage 11 and 13 have not run).

## Mandatory tier, Gate 0 (OR-32): 170 of 170 checked

Rule used: every numeric input stated in 01-gate0.md / B01 for Blocks A to F, the five block scores and totals, and the four load-bearing Gate 0 facts. Count by enumeration: A 36 (PBT, interest, total assets, current liabilities, EBIT, capital employed, ROCE for FY24-26; ROE for 10 years plus medians; A1, A2, A4 outputs), B 34 (cumulative CFO and PAT, capex components and totals, FCF, CFO/PAT trend, payables, WC days), C 8, D 20, E 14, F 20, load-bearing facts 30, scores and totals 8.

All 170 were traced to the Data_Sheet, AR26/AR25 (S and C), or the Q2 FY27 results, and recomputed. Three carry only a rounding or scope note (rows 5 to 7). Highlights: ROCE 12.44 / 15.84 / 23.11 recompute from screener PBT and interest and AR total assets less current liabilities (AR26 [page 166], AR25 consolidated balance sheet lines 9148-9215); CFO 12.45 = AR 1,244.88; capex 4,254.31 + 499.77 (AR26 [page 168]); Q2 FY27 consolidated expenses 4,940.49 = 1,522.64 + 1,916.09 + 1,317.76 + 184.00 (results p.8); H1 FCF -235.13 = 1,610.76 - 1,477.95 - 367.94 (results p.10); E4 contingent liabilities 2,250.08 / 562.62 (FY26 column confirmed by the detail table: 115.85 + 446.77 = 562.62, Note 42 [page 185]).

No verdict-card or Section 1B pillar block exists among these inputs. Those parts of the OR-32 tier are empty by construction, not skipped.

## Sample tier

Material numbers in stages 2 to 9: about 500 by my count. I counted a figure as material when it feeds a flag, a guidance or promise-delivery row, a ratio, a threshold, or a table cell that a judgment reads. Checked: 205, in order of materiality:
- B03: balance sheet, P&L, cash flow, receivable ageing, ratio table, guidance table, CARO figures, FX line, promoter table.
- B04: deck stream split (May deck [page 5], pairing confirmed on the page), order book table, incremental margin, PPE share, derived days.
- B05: quarterly record (Q3 FY26, Q4 FY26, Q1 FY27, Q2 FY27 margins recomputed), promise tests, H1 FY27 cash flow, call quotes (412, 581, 24.25%, 77%, 15 crore, 225 crore, 23.24%, 26.25%, 24.15%, 128%).
- B06: peer margins, order books, receivable figures, JINDRILL day rates, DEEPINDS write-offs, screener peer sales and receivables.
- B07: score sum 12.8, capital commitment arithmetic, net debt at FY25 / FY26 / H1 FY27 (219 / 669 / 551 Mn).
- B08: share ledger (26,63,309; per-brother totals), holding path 68.85 / 64.94 / 65.94 / 61.70, AGM votes, Alara counts and rights-issue arithmetic.
- B09: all TAM, SAM, SOM, CAGR and capacity arithmetic; TTM PAT, P/E.

Not checked, stated honestly:
- 02-notes-pass1.md detail cells (about 258 lines, largely repeated in B03 tables).
- Page anchors of most peer quotes in B06 (about 25 quoted figures checked; quote page numbers not re-walked).
- Web-sourced inputs absent from inputs/: B08 Trendlyne and bulk-deal prices, B09 figures 596, 712, 792, 5,925, CMPDI 6.70 / 11.00 lakh m. They carry source tags and tier labels. They cannot be tested against the corpus here. Coverage shortfall, not a finding.
- Deck slide numbers in B07 beyond those confirmed against [page N] markers (deck printed page = marker minus 1; B04 and B07 cite markers consistently where checked).

acceptance_rate 98 = (375 checked - 8 numbers with findings) / 375.

## Notes for the orchestrator

- Rows 3 and 4 sit in the B03 yaml `triple_pass_verification` block. B03 says "verified 12" and lists three discrepancies. Two of the three (ranks 10, 11) are not discrepancies in B02. This changes no rating, but downstream readers of B03 should not carry "B02 numbers did not reproduce" for ranks 10 and 11.
- B09's 27.3% historical CAGR feeds only the saturation-years line and the "SWPE is gaining share" sentence. The central SOM (14.3% / 14.1%) does not use it.
- Cross-stage consistency (informational, not a finding): Gate 0 reports Q2 FY27 margin 14.42% and says the 14.38% memory figure is not reproduced. Stages 3, 4, 5, 7, 8, 9 use 14.38% or 14.4%. The deck prints 14.38%, so both exist in the source.

```yaml
stage: B12a
company: "SOUTHWEST"
run_date: "2026-11-09"
model: claude-sonnet-5-5
status: complete
numbers_checked: 375
mandatory_checked: 170
mandatory_total: 170
findings:
  - {severity: "MAJOR", location: "09-tam.md Section 3B cross-check line and Section 5B runway (FY23-26 revenue CAGR 27.3%; growth ratio 1.273; 9.6 years to saturate SAM)", claimed: "FY23 to FY26 revenue CAGR 27.3% = (243.02 / 117.73)^(1/3) - 1, base cell cited as screener Data_Sheet Sales row", source_truth: "screener-Data_Sheet.csv Sales row: FY22 = 117.73, FY23 = 124.26, FY26 = 243.02. FY23 to FY26 CAGR = (243.02 / 124.26)^(1/3) - 1 = 25.1% (agrees with 01-gate0.md M11 25.1%). 117.73 is the FY22 cell.", note: "Wrong base-year cell. Saturation years recompute to about 10.9 on the 1.251 ratio. No verdict-card or Section 1B pillar input is touched.", source_fidelity: true}
  - {severity: "MAJOR", location: "04-bizmodel.md Section 4D question 4 (receivables vs revenue growth)", claimed: "revenue growth of INR 6,263 L (standalone)", source_truth: "Standalone revenue 24,292.95 less 17,919.32 = 6,373.63 L (Results_Q2FY27 p.5 col Mar-26; AR26 S p.114). Consolidated 24,302.17 less 18,029.50 = 6,272.67 L (AR26 C p.167). Neither basis gives 6,263.", note: "Arithmetic slip on a labelled basis. The receivable figure 4,456.25 L beside it ties (AR26 S p.115).", source_fidelity: true}
  - {severity: "MAJOR", location: "03-ardeep.md Phase 2-V rank 10 and B03 yaml triple_pass_verification.discrepancies rank 10", claimed: "B02 related-party exposure 855.35 'not reproducible'; visible components sum to 697.52", source_truth: "Reproduces exactly: loans 668.20 (257.86 + 410.34; AR26 S Note 48/49 table, [page 148-149]) + Other Receivables 56.91 (AR26 S Note 16, [page 132]) + debtors 130.24 (AR26 S Note 48, [page 148]) = 855.35; 855.35 / 20,251.42 = 4.22%. B02 pass 2 P2-2 shows this build.", note: "Stage 3 raised a discrepancy against a B02 figure that the AR supports. B03 'verified 12 of 15' should read 13 of 15 on this row.", source_fidelity: true}
  - {severity: "MAJOR", location: "03-ardeep.md Phase 2-V rank 11 and B03 yaml triple_pass_verification.discrepancies rank 11", claimed: "B02 'depreciation rose 150.50' not reproduced; AR shows +184.48 total", source_truth: "Plant depreciation for the year 780.24 (FY25) to 930.74 (FY26) = +150.50 (AR26 S Note 2, depreciation lines near [page 127]). Total depreciation +184.48 is also right (1,144.33 vs 959.85), but it is a different basis from the B02 plant figure (B02 pass 2 P2-6 labels it 'Plant depreciation').", note: "Stage 3 tested a plant-block figure against total depreciation and called the plant figure wrong. B03 'verified 12 of 15' should read 14 of 15 once ranks 10 and 11 are cleared.", source_fidelity: true}
  - {severity: "MINOR", location: "01-gate0.md Block E, E2 (and B01 data_notes)", claimed: "FY25 change -4.34pp (Vikash Jain -2.74, Piyush Jain -1.60; AR FY26 p.133)", source_truth: "The two printed lines sum to -4.34. Total promoter-group holding moved 73.61% to 68.85% = -4.76pp (AR25 promoter table, line 6936; AR26 [page 133] FY25 column).", note: "Components are named, so the basis is labelled; the headline omits the group-wide figure. E2 score (0) unchanged.", source_fidelity: false}
  - {severity: "MINOR", location: "01-gate0.md Load-bearing fact 1 (standalone Q2 FY27 margin)", claimed: "standalone 13.92% (results Q2 FY27 p.5)", source_truth: "(5,750.03 - (1,522.64 + 1,925.13 + 1,317.76 + 183.79 = 4,949.32)) / 5,750.03 = 13.925%, rounds to 13.93%", note: "Truncation, 0.01pp. Derived value.", source_fidelity: false}
  - {severity: "MINOR", location: "01-gate0.md Block F, M11 (prior 3-yr CAGR)", claimed: "prior 13.2% (FY20-23)", source_truth: "(124.26 / 85.80)^(1/3) - 1 = 13.14%, rounds to 13.1% (screener Sales row FY20 85.8, FY23 124.26)", note: "Rounding, 0.1pp. Latest 25.1% ties. Tier unchanged.", source_fidelity: false}
  - {severity: "MINOR", location: "02-notes.md rank 9; 02-notes-pass2.md P2-7; B02 yaml rank 9", claimed: "margin-money cover of guarantees 61.2% (FY26) vs 98.9% (FY25)", source_truth: "61.2% = 1,390.57 / 2,273.57 non-fund limits (pass 2 P2-7 build). On bank guarantees 2,250.07 the ratio is 61.8% (AR26 Note 14 S [page 131], Note 9 S [page 130], Note 42 C [page 185]).", note: "Figure is right on non-fund limits; the consolidated row labels the denominator 'guarantees'. Basis label wrong, not the arithmetic. B03 flagged this as a discrepancy; it is a label issue.", source_fidelity: false}
critical_count: 0
major_count: 4
minor_count: 4
false_positives_struck: 8
material_universe: 500
acceptance_rate: 98
coverage_note: "MANDATORY TIER 170 of 170 checked (rule used: every numeric input stated in 01-gate0.md/B01 for Blocks A-F, the classification scores, and the four load-bearing Gate 0 facts; counted by enumeration in the report). No verdict card (stage 13) and no Section 1B pillar block (stage 11) exist in these inputs, so those parts of the OR-32 tier are empty by construction, not skipped. SAMPLE TIER: about 500 material numbers in stages 2-9 by my count (material = any figure that feeds a flag, a guidance or promise-delivery row, a ratio, or a stated threshold); 205 checked, in order of materiality: B03 statements and ratios, B04 deck and stream figures, B05 quarterly record and promise tests, B06 peer figures, B07 scorecard and net-debt arithmetic, B08 share ledger and AGM votes, B09 TAM arithmetic. NOT CHECKED: 02-notes-pass1.md detail cells (about 258 lines, mostly repeated in B03 tables); most peer-transcript page anchors in B06 (about 25 quoted figures checked, the page numbers of quotes not re-walked); B08 Trendlyne/bulk-deal prices and tier-MEDIA web figures; B09 web-sourced inputs (596, 712, 792, 5,925, CMPDI 6.70/11.00 lakh m): none sits in inputs/, so they are unverifiable here (coverage shortfall, not a finding). Text twins were readable at every page checked; no PDF was opened."
```
