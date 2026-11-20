# VERIFIER A (NUMERICAL), PHASE 1: INVPRECQ, run 2026-11-15

Model: Sonnet 5.5 (high). Inputs: reports 01 to 09 and the source corpus under runs/invprecq-2026-11-15/inputs. Result: 0 CRITICAL, 1 MAJOR, 6 MINOR. Three of the six MINOR rows (rows 2 to 4) are source-fidelity anchor findings with correct values, flagged true. The MAJOR row is a derived-arithmetic error, not a source-existence finding.

## Findings table

| # | Severity | Report location | Claimed (value + anchor) | Source truth (location) | Note | source_fidelity |
|---|---|---|---|---|---|---|
| 1 | MAJOR | 05-concall.md 3B, India defence production bullet | Required growth "about 14.8% a year over four years (derived)" from Rs 1,50,590 cr (FY25) to Rs 3 lakh cr (2029) | Q2 FY27 presentation p.16 gives both inputs. Four years: (300,000/150,590)^(1/4) - 1 = 18.8%. 14.8% is the five-year rate | Inputs match the source. The derived rate is wrong on the stated period. Context figure, no decision input | false |
| 2 | MINOR | 07-emoat.md A1 table (CARE p.1, p.4) and 2B plant table (CARE p.1) | Vacuum capacity up to 100 MTPA at CARE p.1; vacuum casting since FY18 at CARE p.4 | CARE rationale p.2 holds the 100 MTPA sentence; p.3 holds the FY18 sentence. p.1 is the rating table, p.4 annexures | Values exist, cited pages do not hold them. ANCHOR NOT FOUND | true |
| 3 | MINOR | 02-notes-pass1, pass2, 02-notes and B02 block, all AR anchors | AR anchors read one page above PDF page (CF p.111, P&L p.109, BS p.108, Note 23 p.127, Cons Note 38 p.174, Notice pp.46 and 53, Board report p.76) | PDF pages 110, 108, 107, 126, 173, 45 and 52, 75. Marker precedes content | Systematic. Values and note numbers match. Logged in run-log erratum and in the 03-ardeep Phase 2 table. Counted once. ANCHOR NOT FOUND | true |
| 4 | MINOR | 03-ardeep.md 0, fact 2 | "KPI p.21 and p.24 show 5.86%" | 5.86% printed on AR p.22. p.21 prints 7.90 and 2.97 Cr. p.24 prints 1.60% and 4.26%, which sum to 5.86 | Value exists. Cited pages do not print it | true |
| 5 | MINOR | 01-gate0.md D1 | Net debt Rs 67.70 Cr (71.59 - 3.88) | 71.59 - 3.88 = 67.71 (AR p.107: 7,158.75 - 387.51 = 6,771.24 lakh) | 0.01 Cr rounding slip. 2.19x and score unchanged | false |
| 6 | MINOR | 01-gate0.md M12, data_notes | WC days FY25 139.2 | AR p.107 and p.108: 6,292.80 / 16,507.37 x 365 = 139.14 | 0.1 day. FY26 121.6 matches. M12 score 0 unchanged | false |
| 7 | MINOR | 01-gate0.md D2 | EBIT 2,308.95 / finance cost 617.97 = 3.74x (AR p.108) | 2,308.95 is PBT after the 52.51 exceptional item plus 617.97. Pre-exceptional EBIT 2,361.46 gives 3.82x (used in 03-ardeep) | Basis unlabelled in Gate 0 (UNANCHORED, not material). Band 3-4.9, score 2, unchanged | false |

Self-check (rule 5b) on the MAJOR row: claimed 14.8 and truth 18.8 are different numbers; not a matched figure, not a faithfully copied anomaly, not a labelled basis difference; severity follows rule 5 (MISMATCH outside the verdict card or pillar tier is MAJOR). No row is CRITICAL.

Rows struck on the self-check (6, `false_positives_struck: 6`):
1. "185.79 not found in presentation": the Q2 FY27 deck p.21 prints 18,579.07 lakh = 185.79 Cr. A unit conversion of a printed figure.
2. Stage 5 Q2 FY26 revenue gap 93.33 against power and fuel gap 87.85: both faithfully copied from the Q2 FY26 report p.10. The anomaly belongs to the company.
3. Gate 0 ROE basis: closing basis stated for FY17, average equity otherwise, as the Gate 0 formula rule requires. Labelled.
4. Stage 4 incremental margin "37.0%" (514 lakh / 1,391.26): EBITDA 5.14 Cr is a rounded deck figure, so 36.9% and 37.0% cannot be separated.
5. Stage 7 plant 1/2/3 capacity mapping from the Q4 deck p.4: the text layout is ambiguous, the sum 3,060 t ties. Not a number error.
6. 02-notes "forecast 61.62" in the gratuity item: the FY25-column estimate for the next 12 months (AR line 7724). Correct reading.

## Mandatory tier (OR-32): 111 of 111 checked

No verdict-card, Section 1B pillar or B10/B11 input exists in Phase 1. The tier is every Gate 0 scorecard input in 01-gate0.md. Counted 111, checked 111.

| Group | Count | Source and result |
|---|---|---|
| ROCE series FY17-FY26 | 10 | Recomputed from screener-Data_Sheet.csv (PBT + interest over equity + reserves + borrowings): 11.20, 15.15, 11.14, 4.15, 4.65, 4.86, 10.28, 11.73, 9.77, 13.32. All MATCH |
| A1 median, A2 min, A4 compare | 3 | 10.71, 4.15 (FY20), FY26 13.32 vs FY17 11.20. MATCH |
| ROE series, A3 median | 11 | Average-equity basis recomputed: 7.02 (closing, FY17), 12.61, 14.03, -0.97, 0.57, 0.23, 7.35, 9.50, 6.85, 12.13; median 7.19. MATCH |
| Block B inputs | 20 | CFO sum 138.98, PAT sum 53.08, ratio 2.62; 10 FCF values; 7 of 10; cumulative 26.36 and 0.50; payables absent from the Data Sheet (NOT FOUND stands); days 138.4, 176.3, +37.9. MATCH |
| Block C inputs | 9 | Sales 92.04 and 188.45, CAGR 8.29%; PAT 4.17 and 11.76, CAGR 12.21%; FY20 loss -0.72; 7 of 9 up years; +3.92pp. MATCH |
| Block D inputs | 15 | EBITDA 3,089.77 lakh (derived from AR p.108 lines; equals quarter sum 30.90); debt 7,009.87; lease 148.88; 71.59; cash and bank 3.88 (219.57 + 167.94, AR p.107); net debt 67.70 (row 5); 2.19x; EBIT 2,308.95 and 617.97 (row 7); D/E 0.68 (AR p.132); CA 10,420.71; CL 8,703.22; 1.197. MATCH except rows 5 and 7 |
| Block E inputs | 6 | 51.97% and pledge No (shareholding page); 51.91% and 51.97% (AR p.68); contingent 11.94 (AR p.132); equity 10,278.09; 0.12%. MATCH |
| Block F inputs | 16 | 10 EBITDA margins recomputed from the Data Sheet lines (16.17, 19.39, 16.85, 12.05, 12.19, 9.91, 12.73, 14.89, 13.70, 16.46); FAT 1.87; +0.29pp; CAGRs 3.5% and 21.4%; WC days 121.6 (match) and 139.2 (row 6) |
| Load-bearing figures | 13 | H1 FY27 CFO 348.50, PAT 1,079.22, inventories (1,145.75), capex 768.26: PDF page 6 of the Q2 FY27 results read, all MATCH. 80.18 Cr (p.2), CARE 150 to 133 days and 189.20 (CARE p.3), presentation 185.79 (= 18,579.07 lakh, p.21) and 189.7 (p.10), FY26 revenue 18,844.62 (AR p.108), screener Q2 58.00, "245 days not in Data Sheet" (true). MATCH |
| Scorecard sums | 8 | Blocks 6/10/12/7/14, core 49, moat 3, total 52, each re-scored against prompts/01-gate-0-pipeline.md bands. MATCH |

Orchestrator errata on file (stage 1 written before OCR repair) are read as artifacts. Stage 1 took no number from the unreadable pages; its figures stand on the AR, screener and the readable p.6 page.

## Sample tier

Rule used: material = a number that sits in a table, a load-bearing fact, a flag, a register or a block field and feeds a judgment. Distinct value-and-anchor pairs counted by hand, repeats across reports once.

- Material numbers in stages 2 to 9: about 600.
- Checked: about 330, taken in order of materiality.
- Checked in full or near full: 03-ardeep (statement tables, Note 39 ratios, KPI pages, segment note, Notes 17 and 10, RPT map, rating, price table, Notice items, MD&A claims); 02-notes Top 15 and most of pass 2 (Notes 2, 7 to 13, 17 to 22, 25, 30, 35 to 39); 04 and 05 (every cross-document figure: presentation pp.8-11, 16-19, 21; results pp.3-6; CARE pp.1-3; announcements); 07 (gross block, FY25 gross block, export figures, CARE and deck anchors); 08 (shareholding page, RPT table, Notice and Annexure 5 anchors, announcements 20260630 and 20261102).
- Recomputed with correct result: DuPont, ND/EBITDA 2.15x, EBIT cover 3.82x, family take 507.91 (29.1% of PBT, 43.2% of PAT), RPT flows 884.92 and FY25 667.17, guarantee commission 1.26%, A&D increments, revenue per tonne, CAGRs; all stage 9 TAM, SOM, capacity and runway arithmetic.
- Peer transcripts: about 20 figures spot-checked (Steelcast 28.23%, 25-26%, Rs 120 cr, 8,500 t, Rs 114 cr, 63-64%; Azad 37.6%, Rs 6,500 cr, Rs 457 cr, Rs 700 cr QIP, 2.5 years; Alicon Rs 9,100 and 7,600 cr, EV 16%, hybrid 12%, 135 days, Rs 125 cr and Rs 500 cr, possession 1 September, SOP March 2027). All MATCH. Steelcast anchors page-checked against the [page N] markers: correct.
- Not checkable here (source not among inputs): stage 9 web figures (IMARC, MRFR, ACMA, IIF, PIB defence production, PTC, Grand View, Alvarez and Marsal) and stage 8 aggregator and AmbitionBox items. Their arithmetic is correct; their existence is unverified from this corpus.
- Not checked: remaining peer quotes in 06-peers; pass 1 and pass 2 items outside the Top 15 beyond spot checks.

## Basis and unit traps tested

Rs lakh vs Rs cr (all conversions correct); standalone vs consolidated (stage 3 labels Cons Note 38 and Note 39 correctly; screener and AR equity gap 0.17 cr stated and true); results sales 18,539.50 vs deck 18,579.07 vs AR 18,844.62 (three bases, each correctly labelled in 04, 05, 09); CFO and interest classification (99.86 other borrowing cost and 512.21 interest paid correct); FY vs quarter vs H1 (Q2 FY27 column order tied to the deck appendix and correct).

Acceptance: 434 of 441 checked numbers clean (7 flagged numbers across 7 rows), 98%.

```yaml
stage: B12a
company: "INVPRECQ"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
numbers_checked: 441
mandatory_checked: 111
mandatory_total: 111
findings:
  - {severity: "MAJOR", location: "05-concall.md section 3B (India defence production bullet)", claimed: "required growth about 14.8% a year over four years (derived), from Rs 1,50,590 crore FY25 to Rs 3 lakh crore by 2029", source_truth: "Same two inputs (Q2 FY27 presentation p.16) over the four years the report states give (300,000/150,590)^(1/4)-1 = 18.8%; 14.8% is the five-year rate", note: "Inputs match the source; the derived rate is wrong on the report's own stated period. Context statistic, not a decision input.", source_fidelity: false}
  - {severity: "MINOR", location: "07-emoat.md A1 evidence table (CARE p.1, p.4) and section 2B plant table (CARE p.1)", claimed: "vacuum casting capacity up to 100 MTPA at CARE p.1; vacuum casting since FY18 at CARE p.4", source_truth: "Capacity sentence is on CARE rationale p.2 (after the [page 2] marker); FY18 vacuum casting sentence is on p.3 (company description). p.1 holds the rating table and opening, p.4 holds annexures", note: "Values 100 MTPA and FY18 exist in the document; the cited pages do not contain them.", source_fidelity: true}
  - {severity: "MINOR", location: "02-notes-pass1.md, 02-notes-pass2.md, 02-notes.md and B02 block (all AR page anchors)", claimed: "AR anchors one page above the PDF page, e.g. CF p.111, P&L p.109, BS p.108, Note 23 p.127, Cons Note 38 p.174, Notice item 4 pp.46 and 53, Board report p.76", source_truth: "PDF pages are 110 (cash flow), 108 (P&L), 107 (BS), 126 (Note 23), 173 (Cons Note 38), 45 and 52 (Notice item 4), 75 (Board report). Values and note numbers all match.", note: "Systematic off-by-one anchor, already logged in the run-log erratum and corrected in the 03-ardeep Phase 2 table. Counted once. Note numbers let a reader find every item.", source_fidelity: true}
  - {severity: "MINOR", location: "03-ardeep.md section 0 fact 2", claimed: "KPI p.21 and p.24 show 5.86%", source_truth: "5.86% is printed on AR p.22 (Aerospace & Defence 10.87 Cr, 5.86% of revenue). p.21 prints defence 7.90 Cr and aerospace 2.97 Cr; p.24 prints segment percentages 1.60 and 4.26 that sum to 5.86", note: "Value exists in the AR; the cited pages do not print it as 5.86%.", source_fidelity: true}
  - {severity: "MINOR", location: "01-gate0.md D1 (net debt)", claimed: "net debt Rs 67.70 Cr from debt plus lease 71.59 less cash and bank 3.88", source_truth: "71.59 - 3.88 = 67.71 (AR p.107: 7,158.75 - 387.51 = 6,771.24 lakh). Ratio 2.19x and score 1 unchanged", note: "Rounding slip of 0.01 Cr in a Gate 0 input.", source_fidelity: false}
  - {severity: "MINOR", location: "01-gate0.md block F M12 and data_notes (WC days FY25)", claimed: "139.2 days FY25", source_truth: "AR p.107 and p.108: (4,158.33 + 4,872.15 - 2,737.68) / 16,507.37 x 365 = 139.14 days", note: "0.1 day rounding difference. FY26 121.6 matches. Score unchanged (M12 0).", source_fidelity: false}
  - {severity: "MINOR", location: "01-gate0.md D2", claimed: "EBIT 2,308.95 lakh / finance cost 617.97 = 3.74x (AR p.108)", source_truth: "2,308.95 = PBT after the 52.51 exceptional item (1,690.98) + 617.97. Pre-exceptional EBIT is 2,361.46 (3.82x, used in 03-ardeep). Basis not stated in Gate 0", note: "Unlabelled basis difference. Band 3-4.9 and score 2 unchanged on either basis.", source_fidelity: false}
critical_count: 0
major_count: 1
minor_count: 6
false_positives_struck: 6
material_universe: 600
acceptance_rate: 98
coverage_note: "Mandatory tier: no verdict-card, Section 1B pillar or B10/B11 input exists in Phase 1; the tier is every Gate 0 scorecard input in 01-gate0.md, 111 counted and 111 checked (ROCE and ROE series 20, CFO/FCF/PAT/sales/CAGR inputs, balance sheet and AR statement lines, shareholding and pledge, 10 EBITDA margins, moat inputs, 13 load-bearing figures, scorecard sums 6/10/12/7/14/49/3/52 recomputed against prompts/01-gate-0-pipeline.md). Q2 FY27 results p.6 cash-flow digits settled on the PDF page; p.2 and p.3 figures read from the OCR text and tied to the presentation appendix, those PDF pages not opened. Sample tier: about 600 material numbers (hand count of distinct value-and-anchor pairs in tables, load-bearing facts, flags and block YAML of stages 2 to 9, repeats across reports counted once); about 330 checked, in order of materiality (stage 3 and 4 tables and ratios, stage 2 note figures, stage 5 and 7 flags and registers, stage 8 RPT and shareholding, stage 9 arithmetic, about 20 peer-transcript figures). Not checkable, source not among inputs: stage 9 web figures (IMARC 579.1 M USD, MRFR 1.5 bn, ACMA, IIF, PIB defence production, PTC Industries revenue, Grand View, Alvarez and Marsal) and stage 8 web items (Tofler, AmbitionBox, aggregator tenure); the arithmetic on them was recomputed and is correct. Not checked: most peer quotes in 06-peers beyond about 20 figures, and pass 1 and pass 2 items outside the Top 15 beyond spot checks."
```
