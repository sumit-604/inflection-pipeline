# VERIFIER A: NUMERICAL ACCURACY. ASTRAMICRO, run 2026-11-15

Verdict: no CRITICAL. One MAJOR (an arithmetic slip in a derived figure). Six MINOR anchor slips. Every source figure I checked exists in the PDF at or next to the cited anchor. Errata appended to the reports were applied first, and I audited the corrected value.

Route: each number was compared to the page-marked .txt twin of the PDF named in its anchor. Page of a line was set by the nearest preceding `[page N]` marker. Derived figures were recomputed from the source inputs.

## 1. Findings table

| # | Severity | Report location | Claimed (value and anchor) | Source truth (value and location) | Note | source_fidelity |
|---|---|---|---|---|---|---|
| 1 | MAJOR | 04-bizmodel.md, Findings item 3 (HAL order value) | Deck Rs 1,878.8 Cr x 1.18 = Rs 2,216.98 Cr; "the two differ by about 1.2%" from AR Rs 2,205.23 Cr incl. taxes | AR p.28 prints Rs 2,205.23 Cr (lines 1868-1872, 1925). Gap 2,216.98 vs 2,205.23 = 0.53%. Also 2,205.23 / 1.18 = 1,868.8 vs 1,878.8 = 0.54% | Both inputs correct. The stated 1.2% is more than double the true gap. The true gap is near rounding, so "not reconciled" is overstated in FLAG-CONC and the analyst note. A calc slip, not a source-existence finding | false |
| 2 | MINOR | 05-concall.md, call anchors (priority table, 1A, 2A, YAML) | SGR Rs 1,350 Cr at p.3; MVR Rs 182 Cr, ARC Rs 836 Cr, Rs 360 Cr at p.3; Uttam Phase 1 at p.11; Atim Rs 1,870 Cr ex-GST at p.6; "delay from our side" at p.17; Rs 1,057 Cr at p.18; Q4 call Rs 1,157 / 530 / 2,141 / 490 at p.4; Q3 call advances at p.11, "offensive" at p.10 | Same values one page later on the PDF marker: 1,350 at PDF p.4; 182 / 836 / 360 at PDF p.4; Phase 1 at PDF p.10; 1,870 at PDF p.7; "delay" at PDF p.18; 1,057 at PDF p.19; Q4 call figures at PDF p.5; Q3 advances at PDF p.12, "offensive" at PDF p.11 | Header says PDF page; about nine anchors use the printed footer page; Phase 1 "p.11" matches neither (PDF p.10, printed p.9). Values are right. Other B05 anchors are on PDF pages (Atim 1,350 at p.7, Atim 1,600 at p.8, Q4 CFO at p.4) | true |
| 3 | MINOR | 04-bizmodel.md (Findings item 3), 07-emoat.md (P1, 1C, 2D, E2-2) "PR p.1" | Q2 orders received Rs 2,036 Cr; H1 exports 5.7%, at press release p.1 | Both on PDF p.2 of the press release (lines 56-59). PDF p.1 is the cover letter; printed folio "1" sits on PDF p.2 | Printed-page anchor. Values right. B05 cites the release as p.2 | true |
| 4 | MINOR | 07-emoat.md, 1A row 9 and D1-1 | "first satellite targeting 2027-28", AR p.22 | Single occurrence at line 1678 = PDF p.25. B03 cites p.25. AR p.22 holds the 40 GHz MMIC text | Wrong page, correct text | true |
| 5 | MINOR | 09-tam.md, Method 2 | Uttam Rs 1,878.8 Cr, deck PDF p.7 | Deck PDF p.6 (line 187). PDF p.7 is the revenue break-up | Page slip | true |
| 6 | MINOR | 03-ardeep.md (triple-pass row 14, B02 corrections 2, YAML) and 02-notes.md (P3-2) | Janyu 77,837 / 28,486 at Note 46 p.265; rates 7.15% to 9.80% at Note 14 p.236 | Note 46 is on PDF p.264 (lines 17273-17282); p.265 holds Note 47. The rate sentence (line 15701) is on PDF p.237 | Values right; derived 49,351 remaining shares is right | true |
| 7 | MINOR | 03-ardeep.md, Phase 3C ("pp.31, 35") | EBITDA Rs 343 Cr vs Rs 266 Cr; 29.70% vs 25.47% | Rs 343 Cr at PDF p.34 (line 2407); table at PDF p.35 (lines 2423, 2460). PDF p.31 holds the segment order book table; "31" is the printed folio of PDF p.34 | Mixed printed and PDF page. The mixed-basis EBITDA finding recomputes exactly | true |

Location clarification for row 3: the phrase "PR p.1" appears in 07-emoat.md at P1, 1C, 2D and E2-2. The block row writes "4D exports"; it should read "2D".

Severity count: CRITICAL 0, MAJOR 1, MINOR 6.

## 2. Self-check (rule 5b)

Rows struck before emit: 5 (`false_positives_struck: 5`).

1. Gate 0 D1 "borrowings 287.66 (equals Q4 p.17 28,705.35 + leases 61.38)": the sum is 287.67 Cr. The screener row prints 287.66. A 0.01 Cr rounding difference; matched figure. Struck.
2. Promoter holding 6.53% (AR, Mar-26) against 6.54% (BSE, Sep-26): 6,205,827 / 94,945,008 = 6.536%. Both printed. Matched figure, basis labelled. Struck.
3. 04-bizmodel body: "2,036 opening + 2,156 received - 256 executed". The orchestrator errata item 5 settles it at source (Q1 results text line 247: Rs 2,156.44 Cr at 30 Jun 2026). The deck waterfall reads 2,156 opening, 2,036 received, 256 executed, 3,937 closing. The corrected value is right. Struck as superseded.
4. 03-ardeep "4 of 9" claims fail (errata: 5 of 9) and "lines leaving grew 40.3%" (errata: 67.6%; 15,559 / 9,285 = 1.6757). Corrected values recompute. Struck.
5. 09-tam analyst_note "yr3 19.6, yr5 15.9" (errata: 17.9, 15.8). Recomputed: share 18.79% + 4pp on the 4-year SAM gives SOM FY29 1,637, CAGR 17.9%; FY31 2,086, CAGR 15.8%. Corrected values hold. Struck.

Every remaining row was tested for the three 5a classes. Row 1 has genuinely different values (1.2% against 0.53%). Rows 2 to 7 are anchor slips: the claimed anchor and the true anchor are different pages, not the same value. None is a faithfully copied anomaly or a labelled basis difference. Severity follows rule 5: no verdict-card or Section 1B pillar input is a MISMATCH, so none is CRITICAL.

## 3. Coverage

### 3.1 Mandatory tier (OR-32)

Mandatory figures checked: 234 of 234. None left unchecked.

Rule used. No B10, B11 or verdict card exists in Phase 1, so there are no verdict-card inputs. The tier is (a) every sourced input of the Gate 0 scorecard, (b) the Section 1B sector-cap row inputs in 04-bizmodel, (c) pillar or priority inputs the reports feed forward. A ten-year series counts once per year.

| Group | Figures | Result |
|---|---|---|
| Gate 0 Block A: ROCE 18.52 / 19.34 / 22.78 / 22.94 (AR p.11); cross-check inputs and results; ROE by year and median 12.09 | 27 | all match; ROE chain recomputed |
| Gate 0 series: Sales, derived EBITDA, EBITDA %, PAT, net worth, CFO FY17-FY26 (screener Data Sheet); cumulative CFO 367.07, PAT 776.57, ratio 0.47 | 58 | all match; EBITDA recomputed for all ten years from the seven expense rows and ties to PBT |
| Gate 0 Block B: capex FY26 / FY25 (Q4 p.18), FCF, WC days FY25 / FY26 (Q4 p.17), H1 FY27 CFO -14,784.83 and inventory -19,050.35 (Q2 p.12), Sep-26 and Mar-26 inventory and current borrowings (Q2 p.11) | 28 | all match |
| Gate 0 Block C: revenue CAGR 12.9%, PAT CAGR 14.4%, positive years 7 of 9, spread +1.5pp | 4 | all match |
| Gate 0 Block D: FY26 borrowings, cash and bank, EBIT, interest, D/E, current assets 162,051.47, current liabilities 51,828.93; Sep-26 and TTM check (borrowings 48,722.07, cash 206.87, TTM EBITDA 364.96, PBT 290.82, interest 51.07, equity 135,642.36, current assets 179,288.67, current liabilities 70,255.10) | 30 | all match |
| Gate 0 Block E: promoter 6.54% and 6,205,827; institutions 16.52% and 10.48%; Note 12(d) 3.41% and 3.12%; pledge, NDU, encumbrance "No"; contingent 8,000.00 / 91.66 / 93.20; commitments 4,445.74; ratio 6.23% | 16 | all match (BSE Table I, III; AR Note 35 p.326) |
| Gate 0 Block F: net block 267.04, FAT 4.35, selling cost %, R&D 5,573.92 / 4,009.92 and incl. capex, 3-year CAGR endpoints | 14 | all match (AR Note 37 p.252) |
| Stage 4 sector-cap row: five segment Rs Lakhs (AR p.191), five Rs Cr (AR p.31), company-stated %, computed % | 20 | all match |
| Priority and pillar inputs across reports: FY27 guide Rs 1,350 Cr plus or minus 25 and FY28 Rs 1,600 Cr plus or minus 50 (Q1 call); standalone book 3,937.00, consolidated 4,707.59, Mar-26 2,141.21; HAL 2,205.23 / 1,878.8 / 122 / 121; warrants 173.99 / 43.50 / 20,13,885 / Rs 864 / 29 Dec 2026 / 130.50; FY26 standalone revenue 115,566.75, PAT 17,783.73, CFO 37,595.92 and -9,893.82; ARC 50% and Rs 622 / 361 Cr; H1 FY27 standalone revenue and CFO; EBITDA 34,318.04 and 28.07%; gross margin 49.18 / 43.87; capex 72.66 / 75; H1 margins 27.4 / 33.2 | 37 | all match except the anchor slips in rows 2 and 3 |

### 3.2 Sample tier

Material numbers outside the mandatory tier in the reports (my count): about 950. Rule for "material": a number that feeds a scorecard, a table cell, a flag, a calculation or a triangulation. Dates, page references and names are excluded. Total with the mandatory tier: about 1,184.

Checked: 458 (about 48 percent). Order of work was materiality first.

| Report | Checked | What was checked |
|---|---|---|
| 02-notes (consolidated) | 95 | ARC chain (16,009.91 / 7,418.75 / 19,579.28 / 26,267.79 / 74.5%), customer concentration 61,052.05 = 52.84%, ageing and ECL table (8,158.33 / 4,591.91 / 1,219.10 / 900.84 / 14.9% / 19.6%, 5,229.57, 7,083.37, 144.14), deposit and net debt (12,309.93 / 28,309.93 / 21.9%), pledge 1,73,753.02 = 88.6%, undrawn lines 58,014.50 / 56,514.50, ARC intangibles 9,427.48 and net assets 8,220.63, Navictronics 912.00 / 1,824.00 / 285.70, warrants, margin lines |
| 03-ardeep | 125 | audit and CARO anchors and UDINs, P&L, balance sheet, cash flow walks, DuPont, EBITDA basis table, ratio recomputes, MD&A segment table and inflows, FY25 AR guidance quotes, shareholding table, RPT map, contingent table, compensation, Notice items, BRSR payable days |
| 04-bizmodel | 45 | deck pp.4-12, 17, 20, 22-25, 38-41, press release, unit economics, incremental margin, H2 gap |
| 05-concall | 40 | all three transcripts for guidance, ARC, order book, advances, CFO claim, base-year contradiction, quarter filings |
| 06-peers | 18 | DP and Apollo quotes: FY26 revenue 925 / 31%, Q4 share 37% / 55%, CCC 365 / 428, order book 2,654, capex 150-200, Apollo CFO +22 Cr, 353 days, FY29, 12x capacity |
| 07-emoat | 55 | Reg 30 order values, NSE letter, deck order tables, capex and fixed asset turnover recomputes, scale arithmetic, score sum 16.5 and four sensitivities, HR and BRSR figures |
| 08-promoter | 35 | BSE Table II-IV counts, warrant split by category, insider 71.3%, voting results, MD cash 1,35,68,889, monitoring agency 43.49 / 40.00 / 3.49, Reg 30 filings |
| 09-tam | 45 | recomputed every TAM, SAM, SOM, CAGR, capacity and PEG step from its stated inputs; all hold |
| Total | 458 | |

Not checked against a PDF (coverage shortfall, not UNANCHORED, because each carries a URL): web figures in 08-promoter (SEBI orders, Trendlyne, AmbitionBox, Bajaj Broking, Business Today) and in 09-tam (IDSA, Credence, MarketsandMarkets, MoD, BEL, newsonair rupee rate). The 09-tam arithmetic on them was recomputed. Pass-level files 02-notes-pass1 and 02-notes-pass2 were not audited. Cons Notes 40, 41, 43, 44 in 02-notes were sampled.

Unit and basis traps checked and clean: Rs Lakh to Rs Cr conversion in Gate 0; standalone against consolidated labels (CFO 37,595.92 vs 38,673.39; current borrowings 411 Cr deck standalone vs 412.09 Cr filing consolidated); Indian digit grouping in the AR text; FY against TTM in Block D; printed against PDF page in anchors (the cause of rows 2 to 7).

## 4. Acceptance rate

692 numbers checked (234 + 458). About 19 distinct numbers sit inside the seven findings (1 in row 1, about 9 in row 2, 2 in row 3, 2 in row 4, 1 in row 5, 4 in row 6, 1 in row 7 with the value correct). Verified clean: 673 of 692 = 97.3 percent.

## 5. YAML block

```yaml
stage: B12a
company: "ASTRAMICRO"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
numbers_checked: 692
mandatory_checked: 234
mandatory_total: 234
findings:
  - {severity: "MAJOR", location: "04-bizmodel.md, 'Findings on the four first-verification priorities' item 3 (HAL order value reconciliation)", claimed: "Deck Rs 1,878.8 Cr x 1.18 = Rs 2,216.98 Cr; 'the two differ by about 1.2%' against the AR figure Rs 2,205.23 Cr incl. taxes", source_truth: "AR p.28 prints Rs 2,205.23 Cr (text lines 1868-1872 and 1925). Both inputs are right. Recomputed gap: 2,216.98 vs 2,205.23 = 11.75 = 0.53%; equivalently 2,205.23 / 1.18 = 1,868.8 vs deck 1,878.8 = 0.54%", note: "Arithmetic slip on two correctly anchored inputs. The stated 1.2% is more than double the true gap. The true gap is close to rounding, which weakens the 'not reconciled' framing carried into FLAG-CONC and the analyst note. Not a source-existence finding, so source_fidelity is false; no verdict-card or Section 1B input is affected.", source_fidelity: false}
  - {severity: "MINOR", location: "05-concall.md, anchors for the Q1 FY27 call (Concall_Aug_2026) and Q4 FY26 call (Concall_Jun_2026) in the priority table, 1A, 2A and the YAML (guidance, promise_delivery)", claimed: "SGR 'about Rs 1,350 Cr' at p.3; MVR Q1 revenue Rs 182 Cr, ARC order book Rs 836 Cr and ARC sales Rs 360 Cr at p.3; Uttam Phase 1 '12 units by Sep 2027' at p.11; Atim 'around INR1,870 crores without GST' at p.6; 'delay from our side' at p.17; Rs 1,057 Cr base at p.18; Q4 call MVR Rs 1,157 Cr, Rs 530 Cr, Rs 2,141 Cr and Q4 billing Rs 490 Cr at p.4; Q3 call advance rates at p.11 and 'quite offensive' at p.10", source_truth: "Each value is in the transcript, one page later on the PDF [page N] marker the report says it uses: 1,350 at PDF p.4 (line 128); 182, 836, 360 at PDF p.4 (lines 148-152); Phase 1 at PDF p.10 (lines 383-384); 1,870 at PDF p.7 (line 246); 'delay from our side' at PDF p.18 (line 702); 1,057 at PDF p.19 (line 745); Q4 call 1,157 / 530 / 2,141 / 490 at PDF p.5 (lines 189-209); Q3 call advances at PDF p.12 (lines 502-505), 'offensive' at PDF p.11 (line 471)", note: "B05 header says PDF page but about nine anchors use the printed footer page (PDF minus 1), and the Phase 1 anchor p.11 matches neither convention (PDF p.10, printed p.9). Every value itself is correct. Other B05 anchors are on PDF pages (Atim 1,350 plus or minus 25 at p.7, Atim 1,600 at p.8, Q4 call CFO at p.4, Q3 call order book at p.3). Reader following the cited page will not find the line.", source_fidelity: true}
  - {severity: "MINOR", location: "04-bizmodel.md (Findings item 3, 'PR p.1') and 07-emoat.md (P1 inflow line, 4D exports, E2-2, 1C, 'PR p.1')", claimed: "Press release p.1: 'Orders received during the quarter stood at Rs. 2,036 crores' and H1 FY27 exports 5.7%", source_truth: "Both lines are on PDF page 2 of 2026-11-12_Q2FY27_press_release (lines 56-59). PDF page 1 is the cover letter. The printed folio '1' sits on PDF p.2.", note: "Printed-page anchor used where the stated convention is PDF page. Values 2,036 and 5.7% are correct. B05 cites the same release correctly as p.2.", source_fidelity: true}
  - {severity: "MINOR", location: "07-emoat.md, 1A row 9 and D1-1 ('AR p.22')", claimed: "'first satellite targeting 2027-28' at AR p.22", source_truth: "The phrase occurs once in Annual_Report_2026.txt, at line 1678, which is PDF p.25 (p.25 spans lines 1539-1693). B03 cites it correctly as p.25. AR p.22 carries the 40 GHz MMIC text.", note: "Wrong page, correct text. Single occurrence, so the claim is supported at p.25.", source_fidelity: true}
  - {severity: "MINOR", location: "09-tam.md, Section 3 Method 2 bottom-up ('deck PDF p.7')", claimed: "Uttam AAAU Rs 1,878.8 Cr ex-tax at deck PDF p.7", source_truth: "Investor_Presentation_1 PDF p.6 ('Major Orders Received in Q2 FY27', HAL Production 1878.8, line 187). PDF p.7 is the revenue break-up. The same report cites p.6 for the Rs 3,937 Cr book.", note: "Page slip. Value correct.", source_fidelity: true}
  - {severity: "MINOR", location: "03-ardeep.md (triple-pass row 14, B02 CORRECTIONS item 2, YAML note_ref 'Note 46 p.265') and 02-notes.md (P3-2 'Note 14, p.236')", claimed: "Janyu CCPS 'up to 75% of CCPS (77,837 shares) ... sold 28,486 shares' at Note 46 p.265; floating rate range 7.15% to 9.80% at Note 14 p.236", source_truth: "Note 46 text (lines 17273-17282) is on PDF p.264; p.265 holds Note 47 only. The 7.15% to 9.80% sentence (line 15701) is on PDF p.237; p.236 holds the WCDL 15,109.45 and cash credit 4,883.82 lines.", note: "Adjacent-page slips. All four values (77,837; 28,486; 7.15%; 9.80%) are correct, and the derived 49,351 remaining shares is right.", source_fidelity: true}
  - {severity: "MINOR", location: "03-ardeep.md, Phase 3C EBITDA BASIS MISMATCH ('pp.31, 35')", claimed: "EBITDA Rs 343 Cr FY26 vs Rs 266 Cr FY25, margin 29.70% vs 25.47%, cited at pp.31, 35", source_truth: "Rs 343 Cr is at PDF p.34 (line 2407) and the table with 266 / 343 and 25.47 / 29.70 is at PDF p.35 (lines 2423, 2460). PDF p.31 holds the segment order book table. The folio '31' printed on PDF p.34 appears to have been used.", note: "Mixed printed and PDF page. Values correct and the basis finding itself (FY26 includes other income, FY25 does not) recomputes exactly.", source_fidelity: true}
critical_count: 0
major_count: 1
minor_count: 6
false_positives_struck: 5
material_universe: 1184
acceptance_rate: 97.3
coverage_note: "Mandatory tier: no B10, B11 or verdict card exists in Phase 1, so there are no verdict-card inputs. The tier was set as (a) every sourced input of the Gate 0 scorecard in 01-gate0 (177 figures, a ten-year series counted once per year), (b) the Section 1B sector-cap row inputs in 04-bizmodel (20), and (c) 37 other pillar or priority inputs the reports feed forward (FY27 and FY28 guidance, order books, HAL order, warrants, FY26 standalone revenue, PAT and CFO, ARC stake, promoter holding and pledge, ROCE, EBITDA and gross margin, capex). 234 of 234 checked; none left unchecked. Sample tier: about 950 material numbers outside the mandatory tier (counted as any number that feeds a scorecard, table cell, flag, calc or triangulation; dates, page refs and names excluded); 458 checked (about 48 percent), taken in order of materiality (stage 2 and 3 top findings and ratios, stage 4 deck inputs, stage 5 guidance and promise table, stage 7 and 9 recomputations, stage 8 voting and warrant counts, stage 6 peer quotes spot-checked at 18). Not checked against a PDF: web-sourced figures in 08-promoter (SEBI orders, Trendlyne, AmbitionBox, Bajaj Broking, Business Today) and 09-tam (IDSA, Credence, MarketsandMarkets, MoD, BEL, rupee rate); they carry URLs and are outside the corpus, so they are a coverage shortfall and not UNANCHORED. The 09-tam arithmetic on those inputs was recomputed and holds. Pass-level files 02-notes-pass1 and 02-notes-pass2 were not audited; only consolidated 02-notes was. 02-notes Cons Notes 40, 41, 43 and 44 were sampled, not exhausted. Errata appended to the reports were applied before checking (B03 5 of 9, 67.6 percent, 49,351 Janyu shares, 29 Dec 2026 warrant date; B04 2,156 opening and 2,036 received; B09 17.9 and 15.8 percent). Unit and basis traps checked and clean: Rs Lakh to Rs Cr conversions in Gate 0, standalone against consolidated labels (CFO 37,595.92 vs 38,673.39; borrowings 411 vs 412 Cr), Indian digit grouping in the AR text (for example 1,73,753.02), FY against TTM in Gate 0 Block D, printed page against PDF page in anchors."
```
