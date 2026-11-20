# VERIFIER A: NUMERICAL ACCURACY, TD Power Systems Ltd (TDPOWERSYS), run 2026-11-15

Model: claude-sonnet-5-5. One pass, fresh context. Inputs read: stage reports 01 to 09 (02 with its two working passes read through the final 02-notes.md only), the page-marked .txt beside each PDF, and the Data_Sheet CSV. Where a .txt layout was unclear I opened the PDF page (presentation slide 5). Units checked first: Rs lakh (AR, results) against Rs crore (Data_Sheet) against Rs Mn (deck). Basis checked first: consolidated against standalone, FY against TTM against quarter.

## Result in one line

No CRITICAL finding. One MAJOR MISMATCH (a year, not a pillar input). Seven MINOR findings: six page anchors one page off, one unlabelled basis. All Gate 0 scorecard inputs tie to source.

## Findings table

| # | Severity | Report location | Claimed value and anchor | Source truth and location | Note | source_fidelity |
|---|---|---|---|---|---|---|
| 1 | MAJOR | 04-bizmodel.md section 1B row 5 and section 2B Alstom row; 05-concall.md section 3D "Customers" bullet | Alstom long-term agreement for traction stators and rotors dated "2020" (Pres. slide 5) | Slide 5 prints the Alstom agreement under 2017 ("Local production of Generators in Turkey / Signs Long Term Agreement with Alstom ..."). 2020 on the slide reads "Increases footprint in the European and Turkish Market". Confirmed on the rendered PDF page. The AR has no Alstom text. 07-emoat.md prints 2017 correctly | Wrong year on a non-pillar fact. No score or valuation input uses it. Not a basis difference and not a transcribed anomaly | true |
| 2 | MINOR | 05-concall.md section 1B (rows "FY28 capacity", "Debottlenecking capex", "FY29-FY30 capacity", "Large-generator agreement announcement") and the 2A row 23 | "INR22 billion", "INR500 million", "INR40 billion and above", "probably in the month of August" anchored to Q1C p.3 | The four statements sit on Q1C p.4 (txt lines 154 to 164, page 4 starts line 144). Page 3 holds order book 22.08 bn, inflow 7.34 bn, consolidated sales (lines 118 to 137). 04 and 09 anchor the same text at p.4 correctly | Figures exist in the source, one page later. 05 states its anchor key is the [page N] marker | true |
| 3 | MINOR | 05-concall.md section 0A item 1 and section 1B ("Capacity" row) | NK Q4C p.13: "I said that we have a capacity to address INR32 billion for FY '28" | The quote is on Q4C p.14 (txt line 597; page 14 starts line 570). Page 13 (lines 530 to 569) has no INR32 billion text | One page off | true |
| 4 | MINOR | 05-concall.md section 3A first row; section 3D "Customers" bullet | Siemens 2012 licence and Alstom agreement "in the Q2 presentation (p.4)" | The timeline is on slide 5. Slide 4 is the "Journey and Evolution" divider page. 04 and 07 cite slide 5 | One page off | true |
| 5 | MINOR | 07-emoat.md section 0 item 1 | Q1C p.5: "it is not written in stone" (FY28 Rs 3,200 cr is capacity, not guidance) | Text is on Q1C p.6 (txt line 245; page 5 is lines 186 to 226). 09 anchors it at p.6 correctly | One page off | true |
| 6 | MINOR | 09-tam.md section 1B | "p.6: no market-share number (B04 cites Q1 call p.9)" | The "we don't have that number" market-share answer is on Q1C p.9 (txt lines 377 to 381). Page 6 has no market-share statement. 09 itself names p.9 through B04 | Self-contradicting anchor, the p.9 half is right | true |
| 7 | MINOR | 04-bizmodel.md section 2A competition row and section 2B BRUSH row | "BRUSH Group, CG Newage, Kirloskar Electric (Pres. slide 15, 17)" | CG Newage is on slide 15 (line 286), Kirloskar Electric on slide 17 (line 323), BRUSH Group on slide 18 (line 362, Olsson biography) | BRUSH is one slide beyond the cited pair | true |
| 8 | MINOR | 04-bizmodel.md section 0 item 4, section 4A and 4C; 05-concall.md section 0A item 4; 07-emoat.md section 0 item 4 | "Promoter holding 26.5% at 30 Sep 2026" (Pres. slide 36), paired in 05 with the "shareholding pattern 30 Sep 2026" | Slide 36 prints 26.5% under the title "as on 30th September 2026". The filed Reg 31 for 30 Sep 2026 (p.3) prints 27.16% (85,207,322 of 313,706,860). 26.51% appears only in the 12 Oct 2026 post-QIP pattern (321,448,795 shares). The deck figure is on the post-QIP denominator | The deck number is copied correctly. The basis is not labelled in 04, 05 or 07. 01-gate0.md and 08-promoter.md use 27.16% and explain the 26.51% correctly, so no score input is wrong | false |

Rows struck at the rule 5b self-check: 5 (see section "Struck rows").

## What was checked and found clean (no finding)

Mandatory tier, 01-gate0.md. Every Data_Sheet figure matches the CSV. Every derived figure recomputes to the printed value.
- Block A. PBT, interest, share capital, reserves, borrowings and PAT for FY17 to FY26. Capital employed, EBIT and ROCE for all 10 years (for example FY26: 31.24 + 1,040.52 + 18.11 = 1,089.87; EBIT 326.12 + 7.60 = 333.72; 30.6%). ROE on average net worth for all 10 years (FY26 238.77 / 966.04 = 24.7%). Medians 14.6% and 12.1%, minimum -0.1%. The AR cross-check (total assets 187,659.91 less current liabilities 79,322.55 = 108,337.36 lakh) ties to AR p.194, and the FY25 871.94 ties to p.194.
- Block B. CFO series and sum 430.62; PAT sum 758.50; ratio 0.57. Capex lines 10,418.02, 433.76, 5,219.15 and 378.03 lakh and CFO 12,906.76 lakh tie to AR p.198. Trade payables 4,871.60, 36,301.08, 2,380.30 and 20,705.56 lakh tie to AR p.194. All day counts recompute.
- Block C. Revenue CAGR 19.3% and PAT CAGR FY20 to FY26 41.3% recompute from the Data_Sheet. M11's 28.6% and 19.2% recompute.
- Block D. All 30 Sep 2026 balance sheet lines tie to results Q2 FY27 p.8 (current assets 214,475.18 and current liabilities 114,723.79 re-add; equity 3,137.07 + 130,823.35 = 133,960.42). FY26 154,818.78 and 79,322.55 tie to AR p.194.
- Block E. 27.16% and the 85,207,322 and 313,706,860 share counts and the pledge "No" items tie to Reg 31 p.2 and p.3. The six contingent-liability lines (12,246.21, 1,400.45, 0, 120.85, 1,986.03, 13.12) tie to AR p.230 Note 39 and sum to 15,766.66. The promoter percentages 15.41, 12.34, 6.46, 0.16, 0.05 (sum 34.42) and the FY26 holdings tie to the standalone Note 15 VI table (AR p.152). Customer shares tie to AR p.238 (consolidated) and to the standalone note (print p.182, pdf p.170).
- Block F. EBITDA margin and receivable day series, R&D 872.50 lakh and 0.51% (AR Directors' Report Annexure 3), FAT 6.3x.
- Section 0. H1 FY27 revenue 148,137.27 lakh (results p.7), receivables and other current liabilities (p.8), H1 CFO 21,174.13, H1 capex 4,610.09, other payables +29,764.52 (p.9), Europe GmbH 25,628.33 and USA Inc 16,707.65 lakh (AOC-2, AR Directors' Report).

Sample tier, spot results by report.
- 02 and 03: order book, inflow, MD&A (AR p.50), the p.12 highlights in Rs Mn, BRSR 24% and 28.23%, advances 17,205.21 and 18,717.26, MSME 122.03, 284.52, 648.33, lien 5,475.41, FY26 CFO S 11,479.64, FG in transit 4,461.43, sales to subsidiaries 24,368.53 + 16,707.65 + 266.14 = 41,342.32, promoter share counts and the 99,00,000 and 62,28,000 sale arithmetic, shareholder table values. All tie.
- 04 and 05: presentation slides 26 to 38 (order book 23,187 Mn and its six parts, inflow 8,224 / 8,244 and 15,585 Mn, P&L, balance sheet, historical table), the incremental margin arithmetic (17.3%, 21.3%, 22.8%), working capital Rs 833.4 and 1,095.7 cr, TTM revenue 2,513.2 cr, Q3 to Q2 quarterly revenue, gross margin and EBITDA margin recomputed from Q4 FY26 results p.14 (30.7%, 35.1%, 16.6%, 19.0%, 20.6%), the three call order-book and inflow statements, Q1 FY27 quotes on p.4, p.7, p.8, p.10, p.13, p.16 and Q3C p.4 to p.12, the Axis SAST filing (4.85%, 8,58,803, 5.12%), the Rs 192 cr order.
- 06: Triveni FY26 Rs 21.81 bn (+9%), receivable days 84 against 49, Q1 FY27 EBITDA 18% against 25.8%, domestic orders -35.4% and exports +53.4%, orders -26% in Q3 FY26, 56-odd percent tariff; CG backlog Rs 17,333 cr (+45%); Azad Rs 6,500 cr book, Rs 700 cr QIP, 37.6% EBITDA. All tie.
- 07: score arithmetic (18.7), employee cost ratios, FAT 6.59x, CRISIL AA-/A1+, Rs 140 cr Unit 3, Rs 60 to 80 cr capex, interest cover 47x, 5% utilisation, AR employees 991, ESAR 24,000 at Rs 882. All tie.
- 08: Reg 31 holders (Nippon 6.91%, Axis Focused 4.15%, HSBC 3.42%, MF 25.67%, FPI 21.10%), lock-in 27,180,640, 26.51% = 21.57% + 4.94% on 321,448,795 shares, EGM floor Rs 576.17 and 10-day VWAP Rs 556.10, QIP allottee shares, AGM votes (99.15%, 96.16%, 3.84%, 41,04,072, 98.21%), 25 Aug 2026 Reg 29(2) holdings. The price-gap and block-sale arithmetic recomputes. All tie.
- 09: AR chart values (USD 52.8 bn, 107.6 bn, 5.43 to 8.92, 8.64%, 6.18%, 20.25, 21.11, 30.24, 32.51, 61.13 and the hydro 166.84), CRISIL 111 countries, about 70% overseas, 1 to 50 MW, 60 to 70% top 10. All unit conversions (Rs 95.25 per USD), CAGR, EBITDA-growth and share arithmetic recompute.

Basis traps examined and cleared.
- AR p.194 and p.198 are consolidated; AR p.126 and p.130 are standalone. Reports 02 and 03 label S and C on every figure checked. Report 01 uses consolidated throughout and says so.
- AR cited page numbers: "p.N" in 01 to 08 is the PDF page marker. 09 cites printed AR pages for the market charts and says so in its first line (printed p.55 to p.58 on PDF p.42 to p.46). Not a finding.
- The Data_Sheet's FY23 borrowings cell is blank. 01 treats it as nil in the FY23 capital-employed sum (604.52). The AR FY23 balance sheet was not in my inputs. Treated as a coverage note, not a finding.

## Struck rows (rule 5b)

1. 01-gate0 34.42% promoter holding at 31 Mar 2024 against 02-notes 34.27%. Both are labelled arithmetic on the same AR table (sum of printed percentages against shares over total shares). 03 reconciles the two in its section 5D. A labelled basis difference is not a finding (5a).
2. Share count 15,62,14,830 (Directors' Report, CG Annexure B) against 156,214,831 (Data_Sheet, AR notes). The AR prints both. 03 cites the first at its printed anchors. Faithful transcription (5a).
3. 09-tam AR chart anchors "AR p.55 to p.58". Labelled as printed pages in the report's first line (5a).
4. 01-gate0 "around p.182 of the AR print" for the standalone customer note. Print page 182 equals PDF page 170. Labelled (5a).
5. 04-bizmodel and 05-concall Q2 inflow Rs 822.4 cr against Rs 824.4 cr. The deck itself prints 8,224 Mn (slide 26) and 8,244 Mn (slide 28). Both reports copy both and flag the conflict (5a: transcribed anomaly).

## Treatment of web-sourced figures (08-promoter.md and 09-tam.md)

I have no PDF for web content, so none of the following was verified and none is a finding. Each was read only to see whether the report marks it as web-sourced.
- 08: press items (block deals 22 May 2025, Rs 456 cr proceeds, glassdoor and AmbitionBox ratings, marketscreener biographies, MD reappointment 17 Jan 2026, Trilegal QIP counsel). All carry a MEDIA or UNVERIFIED tag in the report. Arithmetic built on them (99,00,000 x Rs 461 = Rs 456.4 cr; 16.4%) recomputes.
- 09: USD/INR 95.25, backlog GW figures (GE Vernova, Siemens Energy, MHI, WoodMac), INNIO capacity, Bloom, Enverus, CEA, motor market sizes. The report calls them secondary web sources and states status partial. Arithmetic built on them recomputes.
Treatment: arithmetic checked, inputs left unverified. No downstream score input in 01 to 07 rests on a web figure.

## Coverage statement

Mandatory tier (OR-32). 277 of 277 checked. Counting rule: each distinct input figure that feeds a Gate 0 block score or a Section 0 first-priority line in 01-gate0.md, with a 10-year series counted as 10 values, derived inputs (EBIT, capital employed, ROCE, ROE, day counts) counted once each, and the YAML block treated as a restatement (not counted again). By block: A 108, B 44, C 13, D 22, E 28, F 28, Section 0 priority lines 34. The count is my own enumeration and is approximate to a few figures at the margin; every figure I enumerated was checked. There is no verdict card and no Section 1B pillar input in the reports in front of me (stages 10, 11 and 13 have not run), so the Gate 0 scorecard is the whole mandatory tier. No mandatory figure was left unchecked. One brief-sourced figure, the 1,481.5 cr "brief" number in 01, is not among my inputs; I checked it against the deck's 14,815.21 Mn total income instead and it ties.

Sample tier. Material numbers in 02 to 09: I counted about 680. Rule for material: a number that feeds a flag, guidance or capacity statement, a promise-delivery row, a moat score, a TAM or SOM step, a promoter-conduct finding, or a first-verification-priority line. I checked about 305 of them (roughly 45%), taking the highest-materiality first: all first-priority lines, all YAML-block figures I could trace, the guidance and order-book ladder, working-capital and cash-conversion lines, the moat-score and TAM arithmetic, and promoter share and price arithmetic. Not checked: most standalone Notes 1 to 57 line items below the top-15 in 02 (taken from the notes without a second read), BRSR detail tables, the Part 2 narrative quotes in 06 beyond the dozen listed above, peer figures in 09 that came from the web, and the Q2 FY26 transcript in other/. Percentages here carry the denominators above.

numbers_checked in the block is 277 + 305 = 582.

## Block

```yaml
stage: B12a
company: "TDPOWERSYS"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
numbers_checked: 582
mandatory_checked: 277
mandatory_total: 277
findings:
  - {severity: "MAJOR", location: "04-bizmodel.md s1B row 5 and s2B Alstom row; 05-concall.md s3D Customers bullet", claimed: "Alstom long-term agreement dated 2020 (Pres. slide 5)", source_truth: "Pres. slide 5 prints the Alstom agreement under 2017; 2020 is 'Increases footprint in the European and Turkish Market' (PDF page 5 rendered)", note: "Wrong year on a non-pillar fact; 07-emoat.md has 2017 correctly", source_fidelity: true}
  - {severity: "MINOR", location: "05-concall.md s1B rows FY28 capacity, Debottlenecking capex, FY29-FY30 capacity, Large-generator announcement; s2A row 23", claimed: "INR22 billion, INR500 million, INR40 billion and above, 'month of August' at Q1C p.3", source_truth: "All four are on Q1C p.4 (txt lines 154-164); p.3 holds order book, inflow and sales", note: "Figures exist one page later; 04 and 09 anchor p.4", source_fidelity: true}
  - {severity: "MINOR", location: "05-concall.md s0A item 1 and s1B Capacity row", claimed: "NK Q4C p.13: capacity to address INR32 billion for FY28", source_truth: "Quote is on Q4C p.14 (txt line 597); p.13 has no INR32 billion text", note: "One page off", source_fidelity: true}
  - {severity: "MINOR", location: "05-concall.md s3A first row and s3D Customers bullet", claimed: "Siemens 2012 licence and Alstom agreement in presentation p.4", source_truth: "Timeline is on slide 5; slide 4 is the divider page", note: "One page off; 04 and 07 cite slide 5", source_fidelity: true}
  - {severity: "MINOR", location: "07-emoat.md s0 item 1", claimed: "Q1C p.5: 'it is not written in stone'", source_truth: "Text is on Q1C p.6 (txt line 245)", note: "One page off; 09 anchors p.6", source_fidelity: true}
  - {severity: "MINOR", location: "09-tam.md s1B", claimed: "p.6: no market-share number (B04 cites p.9)", source_truth: "Market-share answer is on Q1C p.9 (txt lines 377-381); p.6 has none", note: "Self-contradicting anchor; p.9 half is right", source_fidelity: true}
  - {severity: "MINOR", location: "04-bizmodel.md s2A competition row and s2B BRUSH row", claimed: "BRUSH Group, CG Newage, Kirloskar Electric at Pres. slide 15, 17", source_truth: "CG Newage slide 15, Kirloskar slide 17, BRUSH Group slide 18", note: "BRUSH one slide beyond the cited pair", source_fidelity: true}
  - {severity: "MINOR", location: "04-bizmodel.md s0 item 4, s4A, s4C; 05-concall.md s0A item 4; 07-emoat.md s0 item 4", claimed: "Promoter holding 26.5% at 30 Sep 2026 (Pres. slide 36), paired in 05 with the 30 Sep 2026 shareholding pattern", source_truth: "Slide 36 prints 26.5% on a post-QIP denominator; Reg 31 for 30 Sep 2026 p.3 prints 27.16% (85,207,322 of 313,706,860); 26.51% is in the 12 Oct 2026 pattern", note: "Unlabelled basis; 01 and 08 use 27.16% and explain 26.51% correctly; no score input wrong", source_fidelity: false}
critical_count: 0
major_count: 1
minor_count: 7
false_positives_struck: 5
material_universe: 680
acceptance_rate: 98.6
coverage_note: "Mandatory tier 277 of 277 checked: the whole Gate 0 scorecard (01-gate0.md), counted as distinct input figures with 10-year series as 10 values; no verdict card or Section 1B pillar input exists in the reports yet (stages 10, 11, 13 not run). Sample tier: about 680 material numbers in 02-09, about 305 checked (roughly 45%), highest materiality first. Not checked: most standalone Note 1-57 lines below the 02 top-15, BRSR detail tables, most 06 Part 2 quotes beyond those spot-checked, web-sourced figures in 08 and 09 (no PDF exists; arithmetic on them recomputed, inputs left unverified and not a finding), the Q2 FY26 transcript in other/. Data_Sheet FY23 borrowings is blank and 01 treats it as nil; the AR FY23 balance sheet was not in the inputs. Acceptance rate is (582 checked - 8 findings) / 582."
```
