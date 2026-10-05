# VERIFIER A, NUMERICAL AUDIT, RUN 2 (re-audit): ESCONET, run 2026-10-05

Model: Sonnet 5.5. Phase 1. Page checks used the .txt [page N] markers of the corpus extracts. No PDF page was rendered.

## Scope

- Fresh audit, mandatory tier (OR-32): every Gate 0 input in 01-gate0.md and B01-gate0.yaml (run 2, FY2021 to FY2026), including the new FY21 and FY22 figures.
- Fresh check of the changed figures in 07-emoat.md Sections 6C to 6E, evidence_mix and the completionist recount.
- Carried from run 1 without re-audit: findings and sample checks for stages 2, 3, 4, 5, 6, 8 and 9 (B12a-run1.yaml). Six run 1 rows carry into B12a.yaml.
- Superseded: the run 1 findings on B01. Each one is resolved in the re-issue (see table below).

## Run 1 B01 findings: resolved in the re-issue

| Run 1 row | Run 2 state | Verified at |
|---|---|---|
| Results filing balance sheet cited p.15, CFO p.16 | Now results [page 14] (balance sheet) and [page 15] (cash flow) | Outcome_BM_28052026 [page 14], [page 15] |
| AR FY25 balance sheet cited by folio p.110 | Now AR FY25 [page 112], folio 110 in brackets | Annual_Report_2025 [page 112] |
| FY23 revenue 94.59 and receivables 12.59 basis unlabelled | Basis table added. Screener FY23 column rejected, with the neither-set tie-out stated | PROSP [page 50], [page 190], [page 192]; screener Data_Sheet |
| M3 net block 18.40 includes goodwill, unlabelled | Labelled: 18.40 Cr = 989.00 + 851.11 Lakhs | AR FY26 [page 132] |
| M6 Annexure III | Now Annexure IV [page 72] | AR FY26 [page 72] |

## Findings table (new in run 2)

No new CRITICAL or MAJOR. Four new MINOR rows.

| Severity | Report location | Claimed | Source truth | Note |
|---|---|---|---|---|
| MINOR | 01-gate0.md WC-days lines; B01 data_notes | FY21 "71.6 + 48.5 - 72.4 = 47.6"; FY24 58.5 | The three printed FY21 terms sum to 47.7. Unrounded FY21 is 47.64 (47.6, correct). Unrounded FY24 is 58.44 (58.4, not 58.5). | Derived arithmetic, mixed rounding. Every input behind it matches. B4 stays 5 (change -5.32). M12 median 44.98 reproduces on unrounded values. source_fidelity false. |
| MINOR | 01-gate0.md Section 10 item 1; B01 data_notes | Standalone Q1 purchases 4,845.14 and standalone inventory change -518.50, no anchor | Results Q1 [page 4] prints "48,45.14" and "-5,18.50". Values match. Consolidated 10,217.64 and (518.50) on [page 7] match. | UNANCHORED, present in source, not scored. source_fidelity false (not material). |
| MINOR | 01-gate0.md Section 10 item 4 | FY27 guidance Rs 370-400 Cr, no anchor | CRISIL rationale 2026-07-02 text line 26: "increase in revenue to Rs 370-400 crore". 116.33/400 = 29.1%, /370 = 31.4%. | UNANCHORED, present in source, not scored. source_fidelity false. |
| MINOR | 01-gate0.md Block B trend; B01 block_b_trend and FLAG-CASH | PAT 6.16 Cr cited to AR FY26 [page 134] | [page 134] holds CFO -882.50 (correct). PAT 615.50 is on [page 133]. Cumulative PAT pages omitted from the FLAG-CASH cite. | Page-level imprecision. Values correct and correctly anchored in the Section 1 table. source_fidelity false. |

Six carried rows (3 MAJOR, 3 MINOR) are in the YAML marked "(carried run 1)". Four of them keep source_fidelity true and still stand: 03-ardeep promoter basis, 04-bizmodel 52.35% vs 53.15%, 09-tam ZeaCloud turnover 568.79 vs 534.43, and the Netweb 2,058 mn page cite. Two run 1 rows I re-saw while checking (17.65 vs 18.59 interest on statutory dues; promoter 64.94% on PROSP [page 35]) were confirmed on the page.

## What was checked and matched (mandatory tier)

1. Section 1 table, 96 cells (16 rows x 6 years), against the source for each year.
   - FY21 and FY22: restated standalone, PROSP [page 48], [page 50], [page 51]. All 32 cells exact. Current liabilities rebuild: FY21 321.49 + 875.67 + 24.42 + 4.94 = 1,226.52; FY22 378.40 + 1,455.22 + 71.74 + 5.41 = 1,910.77. Net worth: 76.71 + 101.38 = 178.09; 76.71 + 173.74 = 250.45. Borrowings: 313.36 + 321.49; 396.43 + 378.40.
   - FY23: restated consolidated, PROSP [page 190], [page 192], [page 194]. All exact. PAT 304.00 after minority interest 14.42 (before 318.42). Net worth 76.71 + 477.48 = 554.19, minority interest 34.42 excluded.
   - FY24, FY25: AR FY25 [page 112], [page 113], [page 114]. All exact.
   - FY26: AR FY26 [page 132], [page 133], [page 134]. All exact.
2. Source conflict (Section 0). Results filing [page 14]: receivables 1,963.93, payables 3,004.26, total 13,102.08. AR [page 132]: 4,426.93, 5,467.26, 15,565.08. Gap 2,463.00 on each. CFO -882.50 in both ([page 15], [page 134]). Working-capital lines: results +3,291.13 and (1,129.32); AR +828.13 and +1,333.68. Both gaps equal 2,463.00. Debtor days 20.2 on 1,963.93, 45.6 on 4,426.93.
3. D4 components and both ratios (13,647.86 / 7,372.96 = 1.85; 11,184.86 / 4,909.96 = 2.28). Capital employed 8,192.12 on both bases.
4. Block E. SHP XBRL Jun-2026: 7,942,196 shares, 0.6019, pledge, NDU and other encumbrance flags false. 64.94% on PROSP [page 35] (and 60.09 + 4.85 on the p.67 table). Contingent liabilities nil and 500.00 ZeaCloud commitment on AR FY26 [page 145]. -4.75pp reproduces.
5. Block F. Netweb, Rashi, Orient and Esconet screener inputs all exact. Margins reproduce: 13.05%, 2.93%, 4.99% (median 4.99%), Esconet 2.49%. Gross margins reproduce: 21.4%, 2.0%, 21.0% (median 21.0%), Esconet 10.9%. Market caps 325.68, 26,872.08, 6,329.46, 1,050.10. FAT 35.8x on 989.00 and 19.3x on 18.40 (= 989.00 + 851.11 = 1,840.11 Lakhs).
6. Selling proxy, all six years, each line item and total. FY21 47.71 + 52.22 + 10.13 = 110.06; FY22 71.98 + 117.51 + 16.90 = 206.39 (PROSP [page 254]). FY23 102.88 + 124.69 + 21.67 = 249.24 (PROSP [page 215], consolidated). FY24 10.99 + 49.03 + 40.80 + 32.85 + 149.08 = 282.75 (AR FY25 [page 124]). FY25 477.67 and FY26 703.00 (AR FY26 [page 144]). Percentages 2.49, 3.01, 2.58, 2.01, 2.07, 1.98 reproduce.
7. Screener cross-check. FY23 column: sales 94.59, total 28.91, cash 0.72, CFO -1.86, PBT 4.45, receivables 12.59 are as printed, and the report's claim that they tie to neither restated set is true. Consolidated 96.59 and 27.98, standalone 94.66 and 27.62 are exact. FY24 to FY26 tie to the AR.
8. Q1 FY27. Revenue 11,632.69, other income 193.21, EBITDA 1,011.16, margin 8.55% (on total income 11,825.90), purchases 10,217.64. Ex other income margin 817.95 / 11,632.69 = 7.03%. Revenue 116.33 Cr, 29.1% to 31.4% of 370-400.
9. Dates and drivers. ZeaCloud incorporated 11 May 2022 (PROSP [page 199]). Listing 23 Feb 2024 (AR FY25 [page 115]; AR FY26 [page 105]). Prospectus dated 20 Feb 2024. FY24 receivables build 2,439.02 (AR FY25 [page 114]). FY26 inventory build 3,255.66 (AR FY26 [page 134]).
10. Recomputed from checked inputs and reproduced: EBIT, capital employed, EBITDA and margin, ROCE (-6.23, 20.29, 60.56, 23.30, 16.12, 11.96), ROE (-56.4, 33.8, 75.6, 25.6, 15.0, 8.2; median 20.27), receivable, inventory and payable days, cumulative CFO -798.86, cumulative PAT 2,234.14, ratio -0.36, ex-FY26 ratio 0.05, FCF by year and cumulative -2,499.72, revenue CAGR 51.7%, FY23 to FY26 54.2%, FY21 to FY23 48.0%, D1 -1,413.37, D2 8.3x, D3 0.17. Standalone FY23 ROCE 60.7% and growth 38.1% reproduce.

## Stage 7 changed figures (Sections 6C to 6E, evidence_mix, recount)

- 6C table: core 60, blocks 13/5/10/17/15, moat 18, 4 moats, grand 78 match B01 run 2. Run 1 values (4 years, core 59, moat 12, 2 moats, MODERATE, history downgrade) match B01-gate0-run1.yaml.
- 6D and 6E: Q1 FY27 standalone gross margin 29.16% = (6,107.71 - 4,845.14 + 518.50) / 6,107.71. FY26 standalone 13.72% = 4,086.15 / 29,782.95. Reversion gap 943.10 vs PBT 935.67. Finance cost 7.32 (Q1 BM [page 4]). ROCE 60.6% to 11.96%, CFO -798.86 vs PAT 2,234.14.
- Emerging Moat total: 1.0 + 1.0 + 0.7 + 0.7 + 1.4 + 0.7 = 5.5.
- Recount: documented A4 2, B2 4, C1 2, C2 2, H2 2 = 12; claims 1 + 2 + 3 + 3 = 9; inference 1. Mix 12/9/1. The 6 Weak rows and "6 of 23 rows" match the Section 3 summary table.
- Supporting figures: 41.35% top-5 (PROSP [page 28]); service charges 847.30 / 35,440.48 = 2.39% and 150.38 / 23,029.80 = 0.65% (AR FY26 [page 143]); Info Edge Rs 20.06 Cr and C-DAC Rs 25.74 Cr (Reg 30 filings); 25.74 / 354.4 = 7.3%.
- No stage 7 finding.

## Self-check (rule 5b)

- No CRITICAL or MAJOR row was written this run, so no severity test failed.
- Three candidate rows struck: screener PBT 4.45 vs standalone 445.60 (rounding of 4.456); prospectus cash-flow interest 72.34 vs P&L finance cost 72.35 for FY21 (both printed, report uses P&L); screener FY26 PAT 6.16 vs 615.50 / 100 (rounding of 6.155). `false_positives_struck` is 7 (3 here, 4 carried from run 1).
- The WC-days row is kept. The two printed figures differ from the recomputed ones by 0.1 day, and it is not a matched figure, a transcribed anomaly or a labelled basis difference. It is MINOR and not source_fidelity.

## Coverage

Mandatory tier: 215 of 215 checked. No figure unchecked. No verdict-card or Section 1B pillar input exists yet (no stage 10 or 11 output); empty by construction.

Sample tier: material universe 1,035 (about 820 in stages 2 to 9 as counted in run 1, plus the 215 Gate 0 mandatory figures). Checked 466 (251 carried from run 1 plus the 215 mandatory). The ~40 stage 7 re-checks are not added because most overlap the run 1 sample. The run 1 NOT CHECKED list stands: the scanned SAST disclosure, web and media claims in B08 and B09, note-level B02 figures beyond the sample, and Reg 30 filings beyond the sampled items.

Acceptance: 452 clean of 466 checked = 97.0%.

Source-fidelity status after this audit: 0 CRITICAL, 3 MAJOR (all carried, source_fidelity true), 7 MINOR. Four standing rows (three MAJOR, one MINOR Netweb page) are non-overridable until the PDF clears them.

Full YAML block with findings and coverage_note: runs/esconet-2026-10-05/outputs/blocks/B12a.yaml
