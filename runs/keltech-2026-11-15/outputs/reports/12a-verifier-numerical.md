# VERIFIER A: NUMERICAL ACCURACY. KELTECH, run 2026-11-15

Model claude-sonnet-5-5. Fresh context. Inputs read: stage reports 01 to 09 (with 02 pass 1 and pass 2) and the source files under runs/keltech-2026-11-15/inputs. Page numbers below are the [page N] markers of the text twins. Where a twin was garbled I opened the PDF page image and read the digits there. Units: AR and results in Rs lakh, screener and CRISIL in Rs crore.

## Result in brief

- Critical findings: 0. Major: 5. Minor: 2. Rows struck by the rule 5b self-check: 5.
- Three MISMATCH findings are digit errors copied from garbled text twins of the Q2 FY27 and Q4 FY26 results filings. The PDF page images carry the correct digits. They sit in stages 4, 5, 6 and 7 and feed three downstream trigger thresholds.
- One ANCHOR NOT FOUND sits on a Gate 0 mandatory input (D2 interest, cited "AR p.4"). The figure is right and sits at AR p.99.
- One UNANCHORED basis label sits in stage 2 (bank-return gaps). Stage 3 already disclosed the correction, stage 2 text still carries the wrong label.
- No verdict-card input and no Section 1B pillar input exists in the reports in front of me (no stage 10, 11 or 13 output). So no finding can be CRITICAL.
- All findings below are source-fidelity findings. Only the PDF can clear them.

## Findings table

| # | Severity | Report location | Claimed value and anchor | Source truth and location | Note |
|---|---|---|---|---|---|
| F1 | MAJOR | 05-concall.md section 1C table (T2 row), section 2D row 4, section 3C item 3, YAML kill_signal | Q4 FY26 Explosives segment revenue 12,365.58 lakh (Q4 FY26 results p.10); growth +7.8% vs Q4 FY25 11,471.77 | 12,355.58 lakh. Q4 FY26 audited results PDF p.10, segment table, Q4 column (read on the page image). Cross-checks: Q1 FY27 results comparative column prints 12,355.58 (p.3 segment table); 45,766.61 - 12,187.13 - 10,155.04 - 11,068.86 = 12,355.58. Growth = 7.70%, not 7.8% | Transposed digit from the garbled twin ("1236558"). Q4 margin 575.89 / 12,355.58 = 4.66% still holds at two decimals. Source fidelity |
| F2 | MAJOR | 05-concall.md section 2A row 2 and YAML promise_delivery row 2; 04-bizmodel.md section 3B table and YAML must_track_metrics; 06-peers.md Q3 net read; 07-emoat.md section 1C | H1 FY27 Explosives segment result 1,963.31 lakh; margin 6.47% (05, 06, 07) and 6.48% (04, which also prints H1 Explosives revenue 30,320.32) | Segment result 1,953.31 lakh and revenue 30,323.32 lakh. Q2 FY27 results PDF p.6, segment table, H1 FY27 column (page image). Cross-check: 936.60 + 1,016.71 = 1,953.31; 13,900.64 + 16,422.68 = 30,323.32. Margin = 6.44% | Twin printed "1963.31" and "3032032". 05 uses the right revenue (30,323.32) with the wrong result; 04 has both wrong. B05 trigger 2 confirm signal ("at or above 6.5% on filing basis") was set against the wrong 6.47% base. Source fidelity |
| F3 | MAJOR | 05-concall.md section 1C margin table (Q2 FY27 and H1 FY27 columns), section 2A row 2, section 2D, section 4A trigger 3, YAML trigger 3; 06-peers.md section 2B | Q2 FY27 other income 200.80 lakh (Q2 p.5); EBITDA ex other income Q2 1,318.51, margin 8.21%; H1 2,698.11, margin 7.85% | Q2 FY27 other income 209.80 lakh (Q2 FY27 results PDF p.5, page image; total income 16,263.01 = 16,053.21 + 209.80; screener quarter other income 2.10 Cr agrees). EBITDA ex other income Q2 = 1,125.41 + 160.48 + 233.42 - 209.80 = 1,309.51; margin 8.16%. H1 = 2,689.11; 7.82% | Twin printed "200.80". Q1 FY27 and Q2 FY26 columns tie. The 8% confirm signal still holds on the right figure. Source fidelity |
| F4 | MAJOR | 01-gate0.md method note line "Exceptional items" and block D line D2 | "interest ties to AR p.4: 417.88 lakh"; "AR p.4 line items" for exceptional 317.76 | AR PDF p.4 is the board and KMP list. 417.88 and 317.76 sit at AR p.99 (P&L lines VII and finance costs), p.27 (Board's report, 317.76) and p.130 (Note 23, 417.88) | The value is right (scr interest 4.18 Cr ties). The anchor is wrong. D2 is a mandatory-tier Gate 0 input. ANCHOR NOT FOUND. Source fidelity |
| F5 | MAJOR | 02-notes.md top findings rank 1, key risks table, red_flags, questions_for_mgmt, YAML FLAG-BANK-RETURNS | "inventory 19-30% above books"; "receivables 20.4% above books at Dec-25" | AR p.118, Note 13 table: gaps are 976.66/3,218.39 = 30.3%, 758.66/3,958.97 = 19.2%, 1,047.64/3,759.06 = 27.9%, 1,201.61/4,203.59 = 28.6% of the amount REPORTED in the return (the note's own basis, "**Considered upto 10% of amount reported in Quarterly returns"). As a share of BOOKS: 43.6%, 23.7%, 38.6%, 40.0%; receivables Dec-25 25.6% | The two source amounts are copied correctly; the label "above books" names the wrong base. 03-ardeep.md section 2 and its YAML already correct this, so downstream text that quotes 03 is clean, but 02 stays unlabelled. UNANCHORED basis, material (the only RED finding). Source fidelity |
| F6 | MINOR | 03-ardeep.md Phase 2 Top-15 row 14 | Note 13(c) outstanding liabilities 2,695.09 at "p.120" | Found at AR p.119 (line "Outstanding liabilities 2,695.09 1,535.03", total 2,725.30). 02-notes.md cites p.119 | Number right, one page off. Source fidelity (anchor) |
| F7 | MINOR | 06-peers.md Q6, Q7, Q9, Q1 and coverage map | (a) SOLARINDS Q2FY26 international revenue Rs 960 Cr at p.3; (b) SOLARINDS Q2FY27 defence order book Rs 17,568 Cr at p.9; (c) APOLLO Q4FY26 IDL revenue "little less than INR380 crores" at p.10; (d) PREMEXPLN Q1FY27 "94% defense orders and 6% regular explosives" within pp.4, 10-11 | (a) [page 4]; the printed footer "Page 3 of 15" sits inside that PDF page. (b) [page 10]. (c) [page 9] ("loss making" is p.10). (d) [page 9] | All four numbers exist and are quoted right; each cited page does not hold them. Source fidelity (anchor) |

## Rows struck by the rule 5b self-check (5)

1. PREMEXPLN gross margin proxy: report 42.3%, my recompute 42.35% (164.48 / 388.34). Same value within rounding. Struck.
2. Vijay V Chowgule post-transfer holding: 05 prints 44.96%, 08 prints 44.97%; 449,662 / 1,000,000 = 44.9662%. Rounding only. Struck.
3. Value of transferred stake: 08 prints Rs 679.03 Cr; recompute 679.02 to 679.05 depending on CMP 16,564 or 16,564.5. Same value. Struck.
4. TTM P/E 54.1x (04, 09): recompute 54.1x to 54.2x on 1,656 / 30.58. Same value. Struck.
5. 05 quote "shall not, by itself, constitute completion" placed beside a Q2 p.2 anchor: the quote is in the LOI (announcement p.7); the Q2 p.2 phrase "yet to be effected" is correct. 08 anchors it to p.7. Faithful transcription. Struck.

## What was checked and found clean (examples; not exhaustive)

- Gate 0 (01): every derived series from the screener sheet reproduced (EBIT, capital employed, ROCE, ROE, capex proxy, FCF, EBITDA, margins, cumulative CFO 160.37 and PAT 117.60, FCF -5.59, CAGRs 11.4% and 19.3%, M11 -1.8% and 37.6%). AR figures in lakh: balance sheet p.97-98, P&L p.99, cash flow pp.102-103 (4,850.02; -1,757.03; 961.95; -1,101.46; 8,563.29; 35.87; 1,193.72), contingent liabilities p.140 (121.02; 3,956.89; FY25 1,647.95, 159.30, 4,063.59), commitments p.141, R&D p.29, shareholding CSV (54.33%, DII 0.16% to 1.26%), peer EBITDA and gross margin proxies and market caps from the peer CSVs, Q2 FY27 p.7-8 (CWIP 6,280.63, borrowings, equity 16,764.70, CFO 638.39, PAT 1,633.10).
- Stage 2: AR notes quoted (Note 13 returns table, Note 3 CWIP, Note 26 ageing, Note 30, Note 40 split 233.41 + 84.35 = 317.76, powder factor 394.40, outstanding liabilities 2,695.09 vs 1,535.03).
- Stage 3: Note 13(a) TNT loan 2,045.46 at 8.50% read on PDF p.117; term-loan lines on p.116; segment note 28 (45,766.62; 3,051.85; 3,129.40; capex 5,531.47); Note 34 (52,924.07; 814.35; 770.48); Note 41 ratios; liquid pool 5,715.82; P&L and margin walk arithmetic.
- Stage 4: CRISIL p.1-3 (190 crore; 135 crore; April 2027; 21%; GCA 114 days; 32-38 crore; 9%; eight states; 30-Sep-34), peer P&L ratios from the peer CSVs, TTM PAT 3,058.90, Note 19 and Note 22 lines.
- Stage 5: LOI facts (4,09,940 shares, p.4; Reg 10(1)(a)(ii), p.5), Q1 FY27 and Q4 FY26 quarterly revenue, PAT and PBT, Q2 FY27 balance sheet movements, H1 FY27 free cash flow arithmetic.
- Stage 6: peer quotes and pages for SOLARINDS Q4FY26 (28.5%, 2,700 and 2,050, 10-15% and 18-20%, Kalyani, 60%, 1,600, p.12 contraction), SOLARINDS Q2FY27 (29.02%, 3,519, 7,187, share percentages, 1,676, 10-15%), SOLARINDS Q3FY26, APOLLO Q1FY27 (41.33%, 1,550, 480), APOLLO Q2FY27 (353 and 359, 9,000 t, 15 types), PREMEXPLN Q1FY27 (4.7%, 40 players, 80 crore), PREMEXPLN Q3FY26 (150-200 crore, 60 crore); derived Solar segment values re-computed.
- Stage 7: capex turnover arithmetic, H1 FY27 mix, 292 staff, ISO line, AR p.39 laws.
- Stage 8: AGM vote 546,247 and 1,045, 99.81% and 0.19% (scrutinizer pp.6-9), Wataney terms (AR), CESTAT order penalty 13,75,43,257, change-in-management profile.
- Stage 9: screener TTM figures (615.11; 343.81 vs 260.75; operating profit 46.98; PAT 30.58), per-MT arithmetic, FY22-26 CAGR.

## Coverage statement

Mandatory tier (OR-32). No verdict-card input and no Section 1B pillar input exists in the reports in front of me; stages 10, 11 and 13 have not run. The mandatory tier is therefore the Gate 0 scorecard inputs: A1 to A4, B1 to B4, C1 to C4, D1 to D4, E1 to E4 and M1 to M12, which is 32 scored items. Mandatory figures checked: 32 of 32. Items needing a note: B4 earliest-year WC days and E3 pledge are reported NOT FOUND by the stage (verified: no payables history in the sheet, SH header says pledge is not in the capture); D2 has the F4 anchor defect.

Sample tier. Material numbers in the reports: about 560 by my count. I counted a number as material if it feeds a score, a flag, a trigger threshold, a load-bearing fact, a table input to a judgment, or a figure quoted from a peer or filing as evidence for a verdict. I checked about 300 of them, at the claim level (one claim with its derivation counts once). Not checked: web-sourced figures in stages 8 and 9 (Ken Research, Univest, ICRA rationales, media, ThePrint, RBI rate, MarketsandMarkets, aggregators), because they are outside the source PDFs; the ICRA CCPL rationale is not among my inputs; the Q1 FY27 OCR pages were compared only through the figures that the Q2 FY27 filing repeats; about 25 of roughly 150 peer-transcript quotes were located and checked for page and wording; stage 3 phases 5 and 6 (governance table cells and narrative marks) were sampled, not exhausted.

Rule used for the sample: scorecard and table inputs that feed a judgment first, then load-bearing facts, then trigger and threshold figures, then other table cells.

Acceptance rate: 95% (about 285 clean of about 300 checked; defective numbers counted per distinct figure and anchor, about 15).

```yaml
stage: B12a
company: "KELTECH"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
numbers_checked: 300
mandatory_checked: 32
mandatory_total: 32
findings:
  - {severity: "MAJOR", location: "05-concall.md s1C T2 row, s2D row 4, s3C item 3, YAML kill_signal (Q4 FY26 Explosives revenue and growth)", claimed: "12,365.58 lakh; +7.8% vs Q4 FY25 11,471.77 (Q4 FY26 results p.10)", source_truth: "12,355.58 lakh; +7.70% (Q4 FY26 audited results PDF p.10 page image; Q1 FY27 results comparative column 12,355.58; annual 45,766.61 less Q1-Q3 FY26 sum)", note: "MISMATCH from garbled text twin; margin 4.66% unchanged at 2 dp", source_fidelity: true}
  - {severity: "MAJOR", location: "05-concall.md s2A row 2 and YAML promise_delivery and trigger 2; 04-bizmodel.md s3B and YAML must_track; 06-peers.md Q3 net read; 07-emoat.md s1C (H1 FY27 Explosives segment result and margin; 04 also H1 revenue)", claimed: "result 1,963.31 lakh; margin 6.47% (05, 06, 07) or 6.48% (04); 04 revenue 30,320.32", source_truth: "result 1,953.31 lakh; revenue 30,323.32 lakh; margin 6.44% (Q2 FY27 results PDF p.6 page image; 936.60 + 1,016.71; 13,900.64 + 16,422.68)", note: "MISMATCH from garbled twin; B05 trigger 2 confirm signal of 6.5% was set against the wrong base", source_fidelity: true}
  - {severity: "MAJOR", location: "05-concall.md s1C margin table, s2A row 2, s2D, s4A trigger 3, YAML trigger 3; 06-peers.md s2B (Q2 FY27 EBITDA ex other income)", claimed: "other income 200.80; EBITDA 1,318.51, 8.21%; H1 2,698.11, 7.85%", source_truth: "other income 209.80; EBITDA 1,309.51, 8.16%; H1 2,689.11, 7.82% (Q2 FY27 results PDF p.5 page image; total income 16,263.01 = 16,053.21 + 209.80)", note: "MISMATCH from garbled twin; 8% confirm signal still holds", source_fidelity: true}
  - {severity: "MAJOR", location: "01-gate0.md method note (exceptional items) and block D line D2 (interest coverage)", claimed: "'AR p.4' for finance costs 417.88 lakh and for exceptional 317.76 lakh", source_truth: "AR p.4 is the board and KMP list; 417.88 and 317.76 sit at AR p.99 (P&L), p.27 (Board's report) and p.130 (Note 23)", note: "ANCHOR NOT FOUND on a mandatory Gate 0 input; value is correct (scr 4.18 Cr ties)", source_fidelity: true}
  - {severity: "MAJOR", location: "02-notes.md top findings rank 1, risks table, red_flags, questions, YAML FLAG-BANK-RETURNS (bank return gaps)", claimed: "inventory 19-30% above books; receivables 20.4% above books", source_truth: "AR p.118 Note 13: 19.2%-30.3% (receivables 20.4%) are shares of the amount reported in the return; as a share of books 23.7%-43.6% (receivables 25.6%)", note: "UNANCHORED basis label on the only RED finding; 03-ardeep.md already corrects it, 02 does not", source_fidelity: true}
  - {severity: "MINOR", location: "03-ardeep.md Phase 2 Top-15 row 14", claimed: "Note 13(c) outstanding liabilities 2,695.09 at p.120", source_truth: "AR p.119", note: "ANCHOR NOT FOUND (one page off); number correct", source_fidelity: true}
  - {severity: "MINOR", location: "06-peers.md Q6, Q7, Q9 and coverage map (four peer page anchors)", claimed: "SOLARINDS Q2FY26 Rs 960 Cr at p.3; SOLARINDS Q2FY27 Rs 17,568 Cr at p.9; APOLLO Q4FY26 IDL ~Rs 380 Cr at p.10; PREMEXPLN Q1FY27 6% regular explosives within pp.4, 10-11", source_truth: "[page 4]; [page 10]; [page 9]; [page 9]", note: "ANCHOR NOT FOUND (adjacent page); all four numbers exist and are quoted correctly", source_fidelity: true}
critical_count: 0
major_count: 5
minor_count: 2
false_positives_struck: 5
material_universe: 560
acceptance_rate: 95
coverage_note: "Mandatory tier = Gate 0 scored inputs (A1-A4, B1-B4, C1-C4, D1-D4, E1-E4, M1-M12), 32 of 32 checked; no verdict-card or Section 1B pillar input exists in stage 1-9 reports (stages 10, 11, 13 not run). B4 and E3 are stage-reported NOT FOUND and were confirmed absent from the sources; D2 anchor defect is F4. Sample tier: about 560 material numbers counted (feed a score, flag, trigger, load-bearing fact or verdict evidence), about 300 checked at claim level. Not checked: web-sourced figures in stages 8 and 9 (Ken Research, Univest, ICRA, media, aggregators, RBI rate) and the ICRA CCPL rationale, none of which is a source PDF in my inputs; Q1 FY27 OCR pages only through figures repeated in Q2 FY27; about 25 of about 150 peer-transcript quotes located; stage 3 phases 5-6 sampled. Q2 FY27 and Q4 FY26 text twins are garbled in places; F1-F3 digits were read from the PDF page images and every other Q2 and Q4 figure used by the stages that I checked tied."
```
