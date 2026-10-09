# Verifier A (numerical accuracy), scoped re-audit, run 2: MMP, 2026-10-05

Scope: B01 Gate 0 run 2 (mandatory tier, OR-32) and B07 Emerging Moat run 2 (sample tier, sections named in its RUN 2 CHANGES note). Fresh read of the source files. Units checked on the face of each document: AR and results in Rs Lakh, screener in Rs Cr, press releases in Rs Mn, decks and call in Rs Cr.

Result: 0 CRITICAL, 1 MAJOR, 4 MINOR. Mandatory tier 187 of 187 checked. One source-fidelity MISMATCH (E4 context, Note 52).

## Findings table

| # | Severity | Report location | Claimed (anchor) | Source truth (location) | Note | source_fidelity |
|---|---|---|---|---|---|---|
| 1 | MAJOR | B01 Block E, E4 line; B01 YAML data_notes E4 | "Capital commitments 7,621.61 L and other commitments 1,979.34 L (AR26 p.241, Note 52)" | AR26 p.241 Note 52, consolidated: Capital Commitments (A) 5,642.27 L; Other Commitments (B) 1,979.34 L; Total (A+B) 7,621.61 L | MISMATCH. 7,621.61 is the A+B total and contains the 1,979.34. The report presents it as capital commitments alone and lists 1,979.34 beside it, a double count. Not an E4 score input, so no score or class effect. Standalone Note 48 (AR26 p.157) total is 5,257.66 L, which matches neither. | true |
| 2 | MINOR | B07 H2 table row 3; B07 I2 table H2 row | "Toyo Aluminium 74%, MMP 26%" (AR26 p.31, p.54) | AR26 p.54: "MMP Industries Limited holds 26% equity". AR26 p.31: Toyal FY26 PAT Rs 30 Mn, no holding. 74.0% is at Q1 FY27 deck PDF p.11, p.22 and the Mar-26 deck | ANCHOR NOT FOUND for the 74% in the AR26. Number exists in the corpus. Non-material (100% minus 26%). | true |
| 3 | MINOR | B07 B1 note | Wire rod standalone EBITDA Rs 10,000-12,000 per tonne (May-26 call p.20) | May-26 call [page 13] (CFO). [page 20] has 37,000-42,000, 12,000-15,000 and 15,000-18,000 per ton and no wire rod figure | ANCHOR NOT FOUND at p.20; exists at p.13. Management claim, not scored. | true |
| 4 | MINOR | B07 report and B07 YAML | Q1 FY27 PR: lidding foil p.3, polymer vendor approvals and Q3/Q4 FY27 ramp p.4, solar Rs 30 Cr p.5. May-26 call: one-third exports p.22. AR26: 7.00% preference share p.119. Deck: cash flow cash 2.0 p.29 | PR at PDF p.4, p.5, p.6. Call at [page 23]. AR26 7.00% at p.118. Deck cash flow table at p.30 (p.29 balance sheet also shows 2.0) | Weak anchors, one page off. Every figure found in place. The PR mixes PDF-marker and printed-footer numbering. | true |
| 5 | MINOR | B01 LBF1, LBF4, Alt reading; B07 G1 | 135 bps; 12.53 Cr; 12.85%; 18,452.46 L | 134 bps (9.2252 - 7.8806 pp); 12.52 Cr (5,678.74 - 4,426.41 L); 12.83% (median 12.7794, 12.8903); 18,452.45 L (4,317.62 + 14,134.83) | Rounding of derived values. Inputs all match. No decision effect. | false |

## Rows struck by the rule 5b self-check (3)

- Q1 FY27 deck conductor capacity "doubles from 7,200 to 14,400 MTPA": 7,200 is the Mar-26 base (Mar-26 deck, May-26 call p.5), 8,400 is the Q1 FY27 base including the 1,200 pilot, 14,400 is post expansion. The report uses each base consistently in 2A. Basis labelled; struck (class 5a basis difference).
- AR26 FY25 comparatives (receivables 8,951.34; current liabilities 17,310.01; payables 833.86 + 1,878.78) differ from AR25 as filed (8,951.40; 17,310.08; 832.28 + 1,880.42). The reports cite AR26 for FY25 and the figures match AR26 p.171. Restatement, correctly labelled; struck.
- "RDSS" attributed to AR26 p.26. The term appears only in the May-26 call p.21. It is a name, not a number (rule 6); struck.

## Mandatory tier: B01 Gate 0 (187 figures, 187 checked)

Counting rule: each distinct figure in a scored row (A1-A4, B1-B4, C1-C4, D1-D4, E1-E4, M1-M12) or in LBF1-LBF4, once, whether source-read or derived from source figures. Count by block: A 33, B 45, C 12, D 14, E 15, F 33, LBF 35.

| Block | Verified against | Result |
|---|---|---|
| A ROCE table | screener rows PBT, Interest, Total (CSV rows 22, 21, 43/48); AR25 p.154 CL 11,738.68 L; AR26 p.171 CL 21,130.77 and 17,310.01 L | All match. EBIT 46.81/61.30/53.40, capital employed 317.61/375.94/413.63, ROCE 14.74/16.31/12.91 recomputed. |
| A ROE 10 years | screener PAT and equity plus reserves | All ten recomputed (31.6, 24.4, 16.4, 10.2, 8.7, 13.0, 8.6, 11.6, 12.7, 9.26). Median 12.15. FY26 9.26% matches AR26 p.224. |
| B1-B3 | screener CFO, PAT; AR25 p.156; AR26 p.173 | CFO 297.83, PAT 246.72, ratio 1.21. PPE 3,078.11, 4,974.53, 3,923.03 L. FCF 11.97, 7.04, 14.06. Alt-capex FCF 0.43, 4.76, -2.50 recomputed from CWIP and capital advances lines. |
| B4 | AR25 p.154-155; AR26 p.171-172 | Receivables 5,706.17, 8,884.99; inventory 11,099.96, 15,809.91; payables 2,324.44, 4,622.21; revenue 57,854.35, 82,400.49. Days 36.0/70.0/14.7/91.4 and 39.4/70.0/20.5/88.9; FY25 104.1. All match. |
| C | screener Sales, Net profit | CAGR 16.8% and 6.8%, 7 of 9 growth years, -10.1 pp. All match. |
| D | screener rows 41, 51, 39, 40; AR26 p.171, p.224 | 184.52, 2.01, 182.51, 2.81x, 4.01x, 0.53, 1.26 match. |
| E | SHP 2026-06-30; AR25 p.112; AR26 p.241, p.157 | 74.49%, 74.48% (Mar-24, Sep-24), no pledge, 25,402,613 shares, 445.72 L, 517.57 L, 7,133.72 L (3,400 + 3,288 L) match. 7,621.61 L mislabelled (finding 1). |
| F | four screener Data_Sheets | MMP 65.27 / 824.00 = 7.92%; Apar 1,921.79 / 22,902.12 = 8.39%; Arfin 46.16 / 617.99 = 7.47%; Maan 20.12 / 808.71 = 2.49%. GM proxy 21.28, 17.92, 12.16, 10.97. Market caps, FAT 3.29x, M11 15.3% and 30.6%, SG&A 1.73 and 1.94% match. AR26 p.44 no R&D confirmed. |
| LBF | AR26 p.172-173; AR25 p.155-156 | Revenue +19.1%, EBITDA 6,493.54 / 6,382.68 L, 973.69 L exceptional, associates 820.78 / 613.67 / 721.66 L and shares of PBT 20.49 / 12.01 / 18.05%, CFO items match. Rounding notes in finding 5. |

## Sample tier: B07 run 2 (224 of about 260 checked)

Verified in place: 1A (insulator Rs 23 Mn FY26 and 231.94 L, Rs 5 Mn Q1, 35-40 Cr, 18-20 / 45-50 / 130-140 Cr, 1,200 and 6,000 MTPA, 85-90 Cr, Kotak 3,188.00 L sanctioned and 512.70 L drawn at AR26 p.205, conductor Rs 171 Mn and -42%); 1B (subsidiary dates AR26 p.29, US$100,000 Venezuela order); 1C (all five FY26 mix lines on AR26 p.226, 66.1/26.0/7.3/0.2/0.4 Q1 mix, segment margins 11.88, 12.37, 2.00, 4.86, 8.27, 89.6%); 2A (CWIP 3,832.49 and 2,840.66 L, cash capex 5,560.50 L, guarantees 66.88 Cr, wire rod 13-15 to 20-25 Cr, +54 to +67%); 2C (FAT 3.05/3.37/3.17/3.11/3.29, mean 3.196, marginal 2.73, case A and B tables, 20.4%, 1,696.07 L, 3.0x to 3.2x); 2D (FOB 3,836.87 and 2,300.88 L at AR26 p.44, +66.8%, 4.7% of 82,168.59 L at AR26 p.94); G1 and G2 (76.6%, 2.75x and 2.81x, WC days 104.1 and 88.9, payable days 14.3 and 20.5, 97.5 and 109.4); H3 (2,358.51 L at Rs 8.57 and Rs 7.98, 1.5 MW, 5.5 MW and 20%); F2 (565 and 523 employees, 145.4 / 132.3 / +9.9%); 6B (141.3 Cr, 793.05 L); 6C-6E (all Gate 0 inputs match B01); register (5,372-5,755 L). Call anchors p.5, p.14, p.15, p.16, p.17, p.18, p.19, p.21 confirmed by [page] marker.

Not checked (named): run 1 B03 purchase-basis days (121.5 to 102.5; 17.8 to 24.8), stage 5 record and guidance cut, most Jul 2022 call and chart-reading F2 items, the "run 1 reading" of solar date changes, the stage 2 EBITDA basis label.

## Coverage statement

Mandatory tier: 187 of 187 checked; none unchecked. Rule: every distinct figure in a Gate 0 scored row or load-bearing fact.
Sample tier: about 260 material figures in the B07 changed sections (material = feeds a table cell, derived ratio or stated judgment); 224 checked (86%). numbers_checked 411 = 187 + 224. material_universe 447 = 187 + 260.
Acceptance rate: 14 figures flagged of 411 checked; 397 clean; 96.6%.

```yaml
stage: B12a
company: "MMP"
run_date: "2026-10-05"
model: claude-sonnet-5-5
status: complete
numbers_checked: 411
mandatory_checked: 187
mandatory_total: 187
findings:
  - {severity: "MAJOR", location: "B01 report Block E, E4 line (and B01 YAML data_notes E4 line): 'Capital commitments 7,621.61 L and other commitments 1,979.34 L (AR26 p.241, Note 52)'", claimed: "Capital commitments 7,621.61 L (AR26 p.241, Note 52)", source_truth: "AR26 p.241 Note 52 (consolidated): Total Capital Commitments (A) 5,642.27 L; Total Other Commitments (B) 1,979.34 L; Total (A + B) 7,621.61 L. 7,621.61 is the A+B total, not capital commitments; it contains the 1,979.34 L. Not an E4 score input (E4 excludes commitments), so no score effect.", note: "MISMATCH on label and value. The report states capital commitments 7,621.61 and other commitments 1,979.34 as two separate items, which double counts the 1,979.34 L. Correct pair: 5,642.27 L capital, 1,979.34 L other, 7,621.61 L total. Standalone Note 48 (AR26 p.157) has its own total 5,257.66 L; neither matches the claim. Only the PDF clears it.", source_fidelity: true}
  - {severity: "MINOR", location: "B07 report Family H, H2 table row 3 ('Toyal MMP (Toyo Aluminium 74%, MMP 26%) ... AR26 p.31, p.54') and I2 table H2 row ('Toyo Aluminium holds 74% of the JV (AR26 p.31, p.54)')", claimed: "Toyo Aluminium holds 74% (AR26 p.31, p.54)", source_truth: "AR26 p.54 states only 'MMP Industries Limited holds 26% equity in the Joint Venture'; AR26 p.31 gives Toyal FY26 PAT Rs 30 Mn and no holding. 74.0% appears at Q1 FY27 deck PDF p.11 and p.22 ('Toyo Holding - 74.0%') and in the Mar-26 deck, not in the AR26.", note: "ANCHOR NOT FOUND for the 74% at the cited AR26 pages. The figure is in the corpus at the Q1 FY27 deck. Non-material (100% minus the documented 26%), so MINOR. The 26% and the Rs 30 Mn and Rs 7.8 Mn figures match (AR26 p.37 AOC-1: 30,033,576 and 7,808,730 Rs).", source_fidelity: true}
  - {severity: "MINOR", location: "B07 report Family B, B1 note ('Wire rod standalone EBITDA claim Rs 10,000-12,000 per tonne (May-26 call p.20)')", claimed: "Rs 10,000-12,000 per tonne, May-26 call p.20", source_truth: "The figure is at May-26 call [page 13] (CFO, 'wire rod standalone segment ... around INR10,000 to INR12,000 per ton'). [page 20] holds 37,000-42,000 powder, 12,000-15,000 foil and 15,000-18,000 conductor per ton, and no wire rod figure.", note: "ANCHOR NOT FOUND at p.20; number exists at p.13. Management claim, not scored, so MINOR. The same sentence's 14-15% LT cable margin cite (p.14) is correct.", source_fidelity: true}
  - {severity: "MINOR", location: "B07 report and B07 YAML, page anchors off by one page. Q1 FY27 PR (PDF page markers): lidding foil and named customers cited p.3 (found p.4); polymer vendor approvals MSEDCL/PGVCL/CSPDCL and 'Q3/Q4FY27' ramp cited p.4 (found p.5); solar Rs 30 Cr and Q3 FY27 cited p.5 (found p.6). May-26 call: 'one third exports' cited p.22 (found [page 23]). AR26: '7.00% preference share' cited p.119 (found p.118; the 500.00 L amount is on p.119). Q1 FY27 deck: cash 2.0 'cash flow table' cited p.29 (cash flow table is p.30; the p.29 balance sheet also shows 2.0).", claimed: "Cited pages as listed", source_truth: "Each figure exists in the same document one page away (PDF page markers). The Q1 FY27 PR carries printed 'PAGE n OF 8' footers one lower than the PDF marker; the report mixes the two conventions (segment table p.2, exports p.3, BIS p.4 and wire rod p.5 follow PDF markers; the three above follow neither).", note: "Weak anchors. All figures verified in place: Rs 30 Cr and Q3 FY27, lidding named prospects, vendor approvals, 'one third exports', 7.00%. No number is absent from the source. Logged as ANCHOR NOT FOUND at the cited page, MINOR (non-material).", source_fidelity: true}
  - {severity: "MINOR", location: "Rounding of derived figures: B01 report LBF1 'Fall 135 bps'; B01 report LBF4 'CFO ex short-term borrowing FY25 12.53 Cr'; B01 report Alternative reading 'ROCE proxy 10-year median 12.85%'; B07 report G1 'Gross borrowings 18,452.46 Lakh (non-current 4,317.62 + current 14,134.83)'", claimed: "135 bps; 12.53 Cr; 12.85%; 18,452.46 L", source_truth: "134 bps (9.2252% - 7.8806% = 1.3446 pp from AR26 p.172); 12.52 Cr (5,678.74 - 4,426.41 = 1,252.33 L, AR26 p.173); 12.83% (median of 12.7794% FY25 and 12.8903% FY20 from screener-data; the report value equals the median of the rounded 12.8 and 12.9); 18,452.45 L (4,317.62 + 14,134.83, AR26 p.171)", note: "Derived values off by one unit in the last place or by 0.02 pp, from rounded intermediates. All cited inputs match. No score, band or classification changes. Not a source-fidelity matter: the derived figure is not printed in the source.", source_fidelity: false}
critical_count: 0
major_count: 1
minor_count: 4
false_positives_struck: 3
material_universe: 447
acceptance_rate: 96.6
coverage_note: "Mandatory tier (OR-32) = every figure in the Gate 0 report B01 that feeds a scored row or a load-bearing fact (A1-A4, B1-B4, C1-C4, D1-D4, E1-E4, M1-M12, LBF1-LBF4), counting each distinct figure once: 187 of 187 checked, none skipped. Sample tier = stage 7 sections named in its RUN 2 CHANGES note. My count is about 260 material figures; 224 checked (86%). Not checked: run 1 B03 purchase-basis days, stage 5 items, most Jul 2022 call and chart-reading F2 items, the run 1 reading of solar date revisions, the stage 2 EBITDA basis label. Full text in outputs/blocks/B12a-run2.yaml."
```
