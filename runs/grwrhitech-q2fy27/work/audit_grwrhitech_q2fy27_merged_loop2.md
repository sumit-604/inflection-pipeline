# A5 ADVERSARY RE-AUDIT (MERGED REVIEW, LOOP 2): GRWRHITECH | q2fy27

Agent: A5 adversary / completeness auditor | Model: claude-opus-5-5 | Date: 2026-10-23
Review under audit: runs/grwrhitech-q2fy27/work/review_grwrhitech_q2fy27.md (1,296 lines; A4 merged_loop_iteration 2)
Prior merged audits: audit_grwrhitech_q2fy27_merged.md (non-STYLE F1, F2, M1, M2, M3, M4, C1; STYLE S1-S9) and audit_grwrhitech_q2fy27_merged_loop1.md (non-STYLE NF1, NM1; STYLE NS1-NS4). Both were read for their finding lists only.
Inputs read: the A4 review (all 1,296 lines). Results fulltext l.1-1169 in full, plus targeted greps beyond. Concall fulltext: the inventory, refund and mix answers (L0110-L0122, L0290-L0322, L0384-L0392), plus a digit-line sweep of all 842 lines (209 lines). A1 structured files: concall rows by type and line anchor; results rows by type and targeted ID. Both A2 ledgers in full. No source PDF, no audio, nothing under inputs/ opened. No A3 file opened.
Anchors: "rev l.N" = line N of the review as it stands now. "l.N" = line N of grwrhitech-results-q2fy27-fulltext.md. "L0nnn" = the 4-digit source prefix in grwrhitech-concall-q2fy27-fulltext.md. "R###" = A1 structured row. [DERIVED] = my arithmetic on the cited lines.

---

## PRIOR FINDINGS: RESOLUTION CHECK

| Prior finding | Type | Where A4 fixed it | My check | Status |
|---|---|---|---|---|
| NF1 8C guide check mixed refund bases | FACTUAL | rev l.487 rebuilt. The bear bullet (rev l.484) and the forward-map Q3 bear fork (rev l.1157) now say a bear print "puts the 27% guide midpoint at risk". Prior F1 fix text amended (rev l.1179). NF1 fix logged (rev l.1175). YAML flag (rev l.1290) and analyst_note (rev l.1292) aligned. The wrong sentence "a bear-zone print fits the guide" is gone: grep finds it only in the YAML fix log (rev l.1175) | 16 inside the guide: 278.28 / 1,171.39 = 23.757%. Less 4.16 = 19.60%; less 1.03 = 22.73%. 16 outside: 25.122 - 4.16 = 20.96%; 25.122 - 1.03 = 24.09% [DERIVED; l.1010, l.1021-1024, l.1118]. Q4 needed on the 573 illustration: Q3 EBITDA 573 x 18.95% = 108.58. (278.28 - 108.58) / 598.39 = 28.36%; (294.28 - 108.58) / 598.39 = 31.03%. The chart Q4 labels are Q4 FY24 20.1% (90 / 447), Q4 FY25 22.2% (121 / 548) and Q4 FY26 26.2% (157 / 597). The l.1010 / l.1021 series runs Q4 FY24 to Q2 FY27, eleven labels, so the Q4 FY24 attribution at rev l.487 is correct. Robustness: on the FY26 Q3 revenue share of H2 (459 / 1,056 = 43.5%), Q3 is 509.6 and Q4 is 661.8. The Q4 need is then 27.5% (16 inside) or 29.9% (16 outside), still above every chart Q4 [DERIVED]. So the "midpoint at risk" reading holds on either revenue split | RESOLVED |
| NM1 export-stock timing test not grafted | MISSING | Q19 (rev l.514), 6B row 11 (rev l.409), 5A row (rev l.815), Flag 18 (rev l.1066), Step 5 inventory note (rev l.344), YAML Q19 text (rev l.1240) and flag (rev l.1288), analyst_note | Group FG/WIP/SIT change: Q2 +20.40 (a drawdown), Q1 (46.85), H1 (26.45), FY26 (73.00) (l.518). Parent: Q2 (0.82), Q1 (43.55), H1 (44.37), FY26 (25.98) (l.179). Outside the parent: Q2 -21.22, H1 -17.92, FY26 +47.02 [DERIVED]. Twenty days of Q2 exports: 695.53 x 80% / 92 x 20 = 120.96. At the material share, 315.14 / 695.53 = 45.31%, that is 54.8 [DERIVED; L0115, l.516-518]. Both readings and the Q19 date test are present | RESOLVED (wording note NS5) |
| F1 8C Q3 test rebuilt Q3-to-Q3 | FACTUAL | rev l.480-487 and the cells aligned to it | Bull 18.95 + 3.760 = 22.71%. The Q2 alternative is 18.95 + 2.193 = 21.14% (l.509, l.523-532, l.1024). No stale 22.3% or 19.5% line remains in the body (grep: hits only in the YAML fix log, rev l.1179) | STILL HOLDS |
| F2 pricing "parity or better" | FACTUAL | rev l.455, l.819, l.928, l.986, l.1038, l.1137, l.1147 | Matches L0498-L0508 and L0515. The phrase "parity or better" now appears only in the YAML fix log (rev l.1180) | STILL HOLDS |
| M1 Q3 FY26 ex-OI ceiling | MISSING | rev l.257, l.268, l.416, l.976, l.1068 | 87 - 0.18 x 459 = 4.38. Q4 need 37.60 - 4.38 = 33.22. Even split 68.20 / 459 = 14.86%. Q4 floor 119.40 / 597 = 20.0% | STILL HOLDS |
| M2 refund-stripped two-year gain | MISSING | rev l.232, l.1061, l.1283 | 369.72 / 1,328.61 = 27.83% vs 25.55% = +228 bps. 178.00 / 695.53 = 25.59% vs 24.2% = +139 bps. 369.72 / 280 = +32.0%; 178 / 150 = +18.7% | STILL HOLDS |
| M3 inventory split | MISSING | rev l.316, l.335, l.344, l.350, l.907 | 71.74 - 26.45 = 45.29 (63.1%). 89.99 - 44.37 = 45.62. The subsidiary stock change of -18.25 (100.26 to 82.01) ties to -17.92 within FX | STILL HOLDS |
| M4 top three on the filed 34% | MISSING | rev l.496, l.786, l.1056, l.1278 | 34 + 2 x 11.33 = 56.7; 34 + 2 x 17 = 68 | STILL HOLDS |
| C1 "Waluj plant" | CONTRADICTION | rev l.371, l.503 | Waluj appears in the extract only as the registered office (l.60, l.79, l.153, l.497). "Waluj plant" now appears only in the YAML fix log (rev l.1185) | STILL HOLDS |
| S1-S9, NS1-NS4 | STYLE | Logged by A4, not applied (rev l.13, l.14) | Allowed: STYLE never loops. All still stand. Examples: NS1 at rev l.819 and l.1147; NS3 at rev l.316 vs l.344; NS4 at rev l.391 | LOGGED, carried |

---

## AUDIT 0. DELIVERABLE-COMPLETENESS (hard gate)

| Brief part | Location | Status |
|---|---|---|
| (1) Summary narrative | rev l.1105-1122 (17 lines, inside the 10-20 band) | PRESENT |
| (2) Sector intelligence | rev l.1124-1131 (7 bullets) | PRESENT |
| (3) Business-model intelligence | rev l.1133-1142 (9 bullets) | PRESENT |
| (4) Competition intelligence | rev l.1144-1148 (4 bullets) | PRESENT |
| (5) Forward map | rev l.1150-1161 (make-or-break line plus 10 dated catalysts, each with a Bull and a Bear fork) | PRESENT |

Gate: PASS.

---

## AUDIT 1. COVERAGE (fresh enumeration vs A2 ledgers)

Method. Concall: I grep-counted A1 rows by type and the turn table. I swept all 209 digit-bearing fulltext lines (digits after the timestamp) and checked the high-risk lines against row line anchors. That covers L0153-L0378, L0270-L0274, L0286-L0289, L0348-L0355, L0397-L0450, L0477-L0483, L0515-L0519, L0611-L0651, L0696-L0700, L0747-L0761 and L0782-L0786, with A2's documented 1-3 line drift allowed (ledger_concall l.21). Results: I grep-counted all row IDs, FORWARD rows and the footnote block R1766-R1779. I re-counted numbered notes (l.357-367, l.735-749), entities (l.424-427, l.744-746), agenda items (l.40-49) and auditor paragraphs (l.100-135, l.390-480) from the fulltext.

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Results: numbered notes | 7 | 7 (SA 1-3; C 1-4) | none | PASS |
| Results: unnumbered footnotes | 14 | 14 (R1766-R1779 by grep; p29 4, p31 2, p32 1, p35 4, p42 3) | none | PASS |
| Results: line items | 205 | 205 (statement labels re-walked; each SA and C statement re-tied, audit 2) | none | PASS |
| Results: zero-standing | 11 | 11 | none | PASS |
| Results: agenda items | 3 | 3 (item 1 l.40; release l.45; presentation l.48) | none | PASS |
| Results: auditor paragraphs | 13 | 13 | none | PASS |
| Results: entities | 4 distinct / 6 rows | 4 / 6 | none | PASS |
| Results: forward statements | 37 | 37 (grep FORWARD) | none | PASS |
| Results: slides | 24 | 24 (pp20-43) | none (category-level "all reviewed", rev l.20; S9 carried) | PASS |
| Results: structured IDs | 1,782 | 1,782 (grep of row lines) | none | PASS |
| Results: MISSING_FROM_STRUCTURED | 4 | 4 (CIN l.77, l.495, l.1478; signature l.751) | none | PASS |
| Concall: participants | 11 | 11 | none | PASS |
| Concall: turns | 97 | 97 (grep of the turn table) | none | PASS |
| Concall: analyst-side turns | 39 | 39 on A2's definition. My pattern also catches three thanks-only turns, T27, T75 and T83. A2 excludes those and includes T67 as a comment. All 39 map to the 36 Step 4A exchanges | none | PASS |
| Concall: NUMBER / FORWARD / QUALIFIER / ENTITY / DATE rows | 222 / 67 / 47 / 53 / 30 | 222 / 67 / 47 / 53 / 30 (grep by type; sum 419) | none | PASS |
| Concall: fresh numeric sweep | 1 unit (MFS01, L0520) | 1. Every other digit line has a row within drift. Examples: L0272 R173; L0288 R177-R178; L0399-L0417 R217-R230; L0445-L0449 R238-R241; L0481 to R249 (l.480); L0613-L0624 R276-R282; L0749-L0761 R351-R362; L0784 R377 | none | PASS |

Ledger-row accounting in A4: "Unreviewed ledger rows: none" (rev l.25). All notes, turns and slides are reviewed (rev l.20-22). Each named A2 flag is taken up, as in the prior audits. orphan_rows: none. missing_from_ledger: none. Coverage: PASS.

---

## AUDIT 2. ARITHMETIC (recomputed from raw extracted numbers)

I re-tied every statement subtotal I used. SA P&L, SA CF (operating profit 325.16, CGO 154.58, CFO 94.70, investing (70.08), financing (33.78), net (9.16)), C P&L, C CF (operating profit 358.61, CGO 261.38, CFO 195.34) and both balance sheets by position all tie. Every A4 number below ties within rounding. Row NF2 fails as a reconciliation, not as arithmetic.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| C Op EBITDA Q2 FY27 / Q1 FY27 / Q2 FY26 / H1 FY27 / H1 FY26 / FY26 | 169.47 / 172.00 / 119.44 / 341.47 / 229.01 / 434.71 | PBT + D + Fin - OI on each column | l.510-532 | PASS |
| Op margins | 24.37 / 27.17 / 20.97 / 25.70 / 21.51 / 20.50% | 24.366 / 27.169 / 20.966 / 25.701 / 21.510 / 20.504% | l.509 | PASS |
| Reported EBITDA and margin, Q2 / Q1 / H1 FY27 / H1 FY26 / FY26 | 189.00 27.17%; 191.72 30.28%; 380.72 28.66%; 256.25 24.07%; 499.55 23.56% | same | l.509-532 | PASS |
| SA Op EBITDA Q2 / Q1; QoQ | 144.16 / 166.16; -571 bps | 176.51 + 12.72 + 1.57 - 46.64; 168.15 + 12.50 + 1.51 - 16.00; 22.735 - 28.445 | l.170-193 | PASS |
| YoY revenue / PAT / H1 revenue | +22.09% / +41.88% / +24.79% | 695.53 / 569.69; 129.44 / 91.23; 1,328.61 / 1,064.68 | l.509, l.541 | PASS |
| PAT bridge and tax split | +38.21; 12.76 + 1.70 | 26.38 + 23.65 - 2.24 - 0.79 + 5.67 - 12.76 - 1.70; 52.67 x 24.221%; 173.06 x 0.984 pp | l.532-541 | PASS |
| OI-stripped PAT cases | 125.20 / 114.83 / 106.60; EPS 215.56 / 197.71 / 183.54 | 167.39, 153.53, 142.53 x (1 - 25.205%); x 4 / 2.3232 | l.532, l.539 | PASS |
| Intra-group revenue; PAT-level deduction | 225.19 / 218.53 / 443.72; 50.88 / 3.71 / 54.59 | 634.09 + 286.63 - 695.53 etc.; 139.87 + 40.55 - 0.10 - 129.44 etc. | l.170, l.202, l.443-457, l.509, l.541 | PASS |
| Step 2 refund strip Q2 / Q1 | 22.78% (+182 bps) / 25.43% | 158.47 / 695.53; 161.00 / 633.08 | l.509; L0388 | PASS |
| Two-year Q2 / H1 (chart) and M2 strip | +12.0% / +21.2%; +297 / +311 bps; +228 / +139 bps | 695.53 / 621; 1,328.61 / 1,096; 27.17 - 24.2; 28.655 - 25.547; 27.828 - 25.547; 25.592 - 24.2 | l.1010, l.1021-1022 | PASS |
| H2 FY26 filed; Q3 gap to own half | 1,055.43 / 243.30 / 23.05%; 103 bps / 410-416 bps | 2,120.11 - 1,064.68; 499.55 - 256.25; 21.20 - 20.17; 23.05 / 23.11 - 18.95 | l.509-532, l.1010, l.1021-1024 | PASS |
| Guide-implied H2; 16 inside | 25.12%; 23.76%; about 20.9% ex-OI | 294.28 / 1,171.39; 278.28 / 1,171.39; 23.757 - 2.808 | l.1118; L0390 | PASS |
| NF1 rebuilt guide bands | 19.6-22.7% / 21.0-24.1% | as in the resolution table | l.1010, l.1021-1024, l.1118 | PASS |
| NF1 Q4 need on 573 | about 28.4% / 31.0% | 169.70 / 598.39; 185.70 / 598.39 | as above | PASS |
| 8C bull / Q2 alternative / refund share | 22.7% / 21.1% / 2.79 pts | 18.95 + 3.760; 18.95 + 2.193; 16 / 573 | l.509, l.523-532, l.1024; L0390 | PASS |
| M1 bound | 4.38; 33.22; 14.86%; 20.0% | as in the resolution table | l.510-511, l.1010, l.1024 | PASS |
| NM1 outside-parent stock Q2 / H1 / FY26 | -21.22 / -17.92 / +47.02 | -20.40 - 0.82; 26.45 - 44.37; 73.00 - 25.98 | l.179, l.518 | PASS |
| NM1 20 days of Q2 exports; material share | about 121 / about 55; 45.31% | 695.53 x 0.8 / 92 x 20 = 120.96; x 0.4531 = 54.8; 315.14 / 695.53 | l.509, l.516-518; L0115 | PASS |
| C CFO/PAT; FCF; WC change | 0.75x; 168.27; (95.87) | 195.34 / 262.09; 195.34 - 27.07; sum of nine C CF lines | l.692-711 | PASS |
| SA CFO/PAT; FCF; WC change | 0.36x; 67.64; (170.58) | 94.70 / 266.45; 94.70 - 27.06; sum of nine SA CF lines | l.316-336 | PASS |
| C days and CCC | 9.83 / 63.32 / 25.44; 47.71 (prior 45.02) | 71.56, 460.99, 185.21 on 2,657.22 x 365; 53.08, 389.25, 180.83 on 2,120.11 | l.609-645 (by position) | PASS |
| Net cash; ex MF gain | 920.21 / 757.93; 898.93 | 191.62 + 29.45 + 711.75 - 12.61; 126.53 + 28.87 + 618.19 - 15.66; less 21.28 | l.611-642, l.716 | PASS |
| ROCE FY26 / H1 ann. / avg CE / Q2 ann. / TTM | 17.01 / 24.31 / 25.39 / 24.11 / 19.68 (20.55)% | 454.42 / 2,671.82; 709.72 / 2,919.46; / 2,795.64; 703.80 / 2,919.46; 574.41 / 2,919.46 (/ 2,795.64) | l.523, l.532, l.629-642 | PASS |
| EPS bases; PE at 7,037.90 | 222.84 / 225.62 / 183.40 / 228.40; 31.2x / 38.4x | 55.71 x 4; 112.81 x 2; 70.59 + 112.81; 57.10 x 4; 31.19 / 38.37 | l.571-577 | PASS |
| 8A-W price gaps | +104.8% / +23.5%; +93.8% / +16.8% | 7,037.90 / 3,437; / 5,700; 6,660 / 3,437; / 5,700 | rev l.469 | PASS |
| Cash profit | 293.22, +46.2% | 262.09 + 25.86 + 5.27; / 200.63 | l.537-541 | PASS |
| Role 5 Step 2 checks | 25.27%; 840-855; 3,482-3,532; about 473; 26.25-35.00 | (702 - 380.72) / 1,271.39; 3,000 x 28-28.5%; 2,782 + 450-500 + 250; 0.51 x 2,782 / 0.75 x 0.25; 75-100 x 35% | L0613, L0646, L0693-L0695, L0369, L0578-L0608 | PASS |
| **7A row, H1 margin "+464 bps to 26.30%" (L0049)** | **Filing evidence 28.66% incl OI (+459 bps), 25.70% ex-OI (+419 bps). Verdict "CONTRADICTED as spoken (ASR mishear or misstatement; FN01)" (rev l.903). Elsewhere: "except the spoken 26.30%" (rev l.921, l.1039) and "(likely ASR)" (rev l.996)** | **The A4 arithmetic is right. But the spoken figure is the filed H1 PBT margin: 349.52 / 1,328.61 = 26.31%, against 230.72 / 1,064.68 = 21.67% in H1 FY26, +464 bps [DERIVED]. The release prints the same row: "PBT Margin % ... 26.3% 21.7% 464 bps" (l.780; R839 = 26.3%, R841 = 464). The deck prints the H1 PBT margins 21.7% to 26.3% (l.994; R931, R932). The call line L0049 is the PBT sentence ("Profit before tax increased 51% to Rs 350 crore with EBITDA margin expanding by 464 basis points to 26.30%"). So the number and the bps match the filing exactly; only the label is wrong** | l.780, l.994; l.532, l.509; L0049 | **FAIL (reconciliation; NF2)** |

arithmetic_mismatches: none in A4's numbers. The NF2 reconciliation error is listed under FACTUAL findings.

---

## AUDIT 3. ADVERSARIAL READ (three most positive claims)

### AR1. "At or above Base on H1 pro-rata for revenue, margin, PAT, EPS, net cash and ROCE, also after an 11 refund strip"; revenue "Above Bull" (rev l.386-391, l.468)
Bear counter tested: H1 is the strong half, and an H1 net-cash figure is compared with a year-end base.
- Seasonality. On the heaviest seasonal shares in the extract the claim holds. FY25 H1 was 52.0% of revenue and 56.6% of EBITDA (1,096 / 2,109; 280 / 495). FY26 H1 was 50.2% of revenue, 51.3% of EBITDA and 51.5% of PAT (l.509-541, l.1010, l.1022, l.1116, l.1120) [DERIVED].
- Revenue implied 2,555-2,646, above Bull 2,502.
- EBITDA incl OI implied 673-742, a 26.3-28.0% margin. After the 11 strip it is 653, or 25.6%, against the 24% base.
- PAT implied about 509, or about 493 after a post-tax strip of 8.25, against the 397 base.
- ROCE: TTM 19.68%, or 19.30% after the 11 strip ((574.41 - 11) / 2,919.46), against the 19% base. Above, but thinly (NS4 carried).
- Net cash. 920.21 at 30-Sep against the 820 FY27 year-end base. If the deck's ~170 capex is the FY27 figure (l.1128), H2 capex is about 143. Net cash then stays at or above 820 if H2 CFO is at least about 43, or about 64 excluding the 21.28 MF gain. H1 CFO was 195.34 (l.709) [DERIVED]. The review already writes "before H2 capex" (rev l.352).
Survives: NO.

### AR2. "The YoY expansion is real on either split" and the two-year margin "direction holds" (rev l.232-233)
Bear counter tested: the chart series includes other income, and FY25 other income is ND.
- H1. Refund-stripped, the ex-OI H1 FY27 margin is 27.83 - 2.95 = 24.87%. The direction reverses only if H1 FY25 other income was below 0.68% of revenue, about 7.4 on 1,096. Every filed half carried 27.24 or more (l.510-511) [DERIVED].
- Q2. If all 11 fell in Q2, the ex-OI Q2 margin is 22.78%. The direction reverses only if Q2 FY25 other income was below 1.42% of revenue, about 8.8 on 621. Every filed quarter carried 13.38-19.72 [DERIVED].
- YoY. Q2 ex-OI before the refund is +182 bps on the worst split (Step 2).
Survives: NO. The review already says the ex-OI gain "could be smaller still" and is ND.

### AR3. Working capital "leans growth-induced"; the derived split "partly verifies" the raw-material build; the NM1 graft says "an FY27 own-book build is excluded" (rev l.344, l.350, l.409)
Bear counter tested: does a residual bear reading on working capital survive the loop-1 graft?
- The export-stock bear reading (customer channel fill) is now in Q19, 6B row 11, 5A and Flag 18.
- The standalone CCC +11.78 days, receivables +35.2% with at least 191.03 intra-group, and the 22.70 undisclosed non-current build are already gaps (a)-(c) (rev l.350).
- No further bear counter in the extract survives.
- The residual point cuts the other way, toward the company:
  - Management's range is "15 to 25" days (L0310-L0311). The cause is "number of days have gone by", which reads as longer transit.
  - At the 15-day low end on material cost, the build is about 41.1 [DERIVED 695.53 x 0.8 / 92 x 15 x 0.4531].
  - The parent's FG/WIP rose 43.55 in Q1 FY27 and held in Q2 (+0.82; l.179). So parent-held in-transit stock built in Q1 can be fitted at that edge, with the subsidiaries destocking 17.92.
  - The analyst also framed the inventory-day rise as running "over the last few years" (L0292-L0294).
  - The review's quantified test ("No own-book build of that size", rev l.409; "of that size", rev l.1066) holds at the stated 20 days. Its categorical form ("excluded", rev l.409; "did not land on group books", rev l.344, l.514, l.1292) overreaches at the edge.
  - Logged as NS5 (STYLE). The edge case needs the 15-day low end, a material-only valuation, and the whole parent Q1 FG/WIP build being export stock.
Survives: NO (as a bear counter).

### Mandatory acquisition-economics probe
No acquisition, business purchase or third-party stake buy appears in either document.
- The only entity investment is 0.52 into a wholly owned subsidiary (SA CF l.335 by position, label l.339).
- That subsidiary has nil revenue and an H1 loss of 0.38 (l.457). Consideration / target PAT = 0.52 / (-0.38), which is not meaningful. There is no seller and no earnings multiple.
- The Lubrizol MoU (l.830-833) and the resin "understanding" (L0820-L0821) are a partnership and a supply term, not a stake purchase. The review tests the possible take-or-pay at Q20.
Probe: NOT APPLICABLE, with the reason stated.

---

## FINDINGS (tagged)

### FACTUAL
NF2. The review reads the spoken H1 "EBITDA margin ... 464 basis points to 26.30%" (L0049) as a number conflict, "likely ASR". The filing carries that exact figure as the H1 PBT margin. Agent: A4.
- Filed: release "PBT Margin %" row, H1 FY27 26.3% vs H1 FY26 21.7%, 464 bps (l.780; R839, R840, R841). Deck p25 H1 margins: PBT 21.7% to 26.3% (l.994; R931, R932). Recomputed: 349.52 / 1,328.61 = 26.31%; 230.72 / 1,064.68 = 21.67%; +464 bps [DERIVED; l.509, l.532].
- L0049 is the PBT sentence of the prepared remarks: "Profit before tax increased 51% to Rs 350 crore with EBITDA margin expanding by 464 basis points to 26.30%".
- The ASR heard the number and the bps correctly. The slip is the label, by the speaker or the ASR, which cannot be told apart.
- Cells that state a contradiction the extract does not support:
  - preamble item (4) (rev l.24);
  - Step 1 claim #12 (rev l.600);
  - Step 1 internal contradiction (a) (rev l.630);
  - 7A row verdict "CONTRADICTED as spoken (ASR mishear or misstatement)" (rev l.903);
  - 7A Read "no material contradiction ... except the spoken 26.30%" (rev l.921);
  - 8E "the spoken 26.30% (likely ASR)" (rev l.996);
  - Section C Reconciliation "match the filing, except the spoken 26.30%" (rev l.1039).
- Corrected reading:
  - Every backward number on the call matches the filing.
  - One label slip remains: the H1 PBT margin was called the EBITDA margin.
  - This is a small point in favour of the ASR text's fidelity.
  - It is also a minor basis slip on a call with no finance officer. That fits FN14 and the call's silence on the other-income basis.
- Fix:
  - Restate the 7A row as "CONFIRMED as the H1 PBT margin (l.780); labelled EBITDA on the call".
  - Align the six other cells listed above.
  - No number elsewhere changes. No verdict changes.
- Provenance: the misreading starts at A3 FN01 and has stood since the merge. Both prior merged audits passed it. It is new to this audit, not caused by loop 2.

### MISSING
None new. NM1 resolved.

### CONTRADICTION
None new.

### STYLE (logged; no loop)
- S1-S9 (merged audit) and NS1-NS4 (merged loop 1): still unapplied; carried as logged.
- NS5. NM1 wording. "An FY27 own-book build is excluded" (rev l.409) and "did not land on group books in FY27" (rev l.344, l.514, l.1292) are categorical. The quantified test supports "no own-book build of 20 days' size", as rev l.409 and l.1066 say elsewhere.
  - At management's 15-day low end (L0310-L0311) on material cost, about 41.1, the parent's Q1 FY27 FG/WIP build of 43.55, held in Q2 (l.179), could hold part of it as in-transit stock.
  - The analyst framed the rise as "over the last few years" (L0292-L0294). That leans to an earlier rise, consistent with reading (a).
  - Suggest: "excluded at 20 days and at the subsidiaries; not ruled out for parent-held transit stock at the 15-day low end".
  - This is STYLE because the stated figure is "roughly 20 days", and the edge case needs the low end, a material-only valuation and the whole parent build being export stock.
- NS6. IPD at peer level. The brief's competition "Margin gap" bullet (rev l.1146) compares the group margin with Uflex 11.25% and Cosmo First 9.94% [SECONDARY]. Management puts its own IPD margin at 10-12% (L0792) [ASR], which is the peer level. So the gap is the CPD specialty mix, not a cost edge across the book. Optional cross-reference to rev l.1136. The claim as written stands.
- NS7. Header metadata. Rev l.14 records the loop-2 approval as "operator-approved 2026-10-24". This audit runs on 2026-10-23. Confirm the date (time zone or typo).

---

## VERDICT
INCOMPLETE. Loop back to A4.
- Gap (NF2, FACTUAL): the review treats the spoken H1 "EBITDA margin ... 464 bps to 26.30%" (L0049) as its one backward-number conflict and says "likely ASR". The filed release prints the H1 PBT margin as 26.3% vs 21.7%, +464 bps (l.780; R839, R841), and the deck prints the same (l.994; R931, R932). So the number matches the filing exactly and only the label is wrong.
- Restate the 7A row as CONFIRMED (PBT margin, mislabelled EBITDA). Align preamble item (4) (rev l.24), Step 1 #12 (rev l.600), Step 1 contradiction (a) (rev l.630), the 7A Read (rev l.921), 8E (rev l.996) and Section C (rev l.1039).
- Text only. No number or verdict changes. Thesis-neutral.
- Both loop-1 findings (NF1, NM1) are RESOLVED. All seven earlier merged fixes (F1, F2, M1, M2, M3, M4, C1) still hold.
- Coverage: PASS (no orphan rows, nothing missing from either ledger). Arithmetic: every A4 number ties within rounding. No A2 or A3 loop is needed.

## STYLE NOTES
S1-S9 and NS1-NS4 (carried), and NS5-NS7 (new), recorded. No re-run on their account.

```yaml
stage: A5-adversary
company: "GRWRHITECH"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
findings_by_type:
  factual:
    - "NF2 (A4): spoken H1 'EBITDA margin expanding by 464 basis points to 26.30%' (L0049) is read as a number conflict, 'likely ASR' (rev l.903, l.921, l.996, l.1039; also l.24, l.600, l.630). The filing carries it as the H1 PBT margin: release 'PBT Margin %' H1 FY27 26.3% vs H1 FY26 21.7%, 464 bps (l.780; R839, R841); deck H1 PBT 21.7% to 26.3% (l.994; R931, R932); 349.52/1,328.61 = 26.31% vs 230.72/1,064.68 = 21.67% [DERIVED]. Number and bps match the filing; only the label is wrong. Restate the 7A verdict as CONFIRMED (PBT margin, mislabelled EBITDA) and align the six other cells. Origin A3 FN01; missed by both prior merged audits; text only, no number or verdict change"
  missing: []
  contradiction: []
  style:
    - "S1-S9 (merged audit) and NS1-NS4 (merged loop 1): still unapplied; carried as logged"
    - "NS5: NM1 wording 'an FY27 own-book build is excluded' / 'did not land on group books in FY27' (rev l.344, l.409, l.514, l.1292) is categorical; the quantified test holds at the stated 20 days, but at the 15-day low end (L0310-L0311) on material cost (~41.1) the parent's Q1 FG/WIP build of 43.55, held in Q2 (l.179), could hold transit stock; the analyst framed the rise as 'over the last few years' (L0292-L0294); suggest 'excluded at 20 days and at the subsidiaries'"
    - "NS6: competition 'Margin gap' vs Uflex 11.25% / Cosmo 9.94% (rev l.1146): management's own IPD margin is 10-12% (L0792), at peer level; the gap is CPD mix, not a book-wide cost edge; optional cross-reference"
    - "NS7: header records loop-2 approval as 2026-10-24 (rev l.14), after this audit date 2026-10-23; confirm (time zone or typo)"
loop_back_to: "A4"
gap: "NF2 (FACTUAL): the spoken H1 'EBITDA margin ... 464 bps to 26.30%' (L0049) is the filed H1 PBT margin (release l.780: 26.3% vs 21.7%, 464 bps, R839/R841; deck l.994, R931/R932), not a number conflict or ASR mishear. Restate 7A (rev l.903) as CONFIRMED (PBT margin, mislabelled EBITDA). Align preamble (4) rev l.24, Step 1 #12 rev l.600, Step 1 contradiction (a) rev l.630, 7A Read rev l.921, 8E rev l.996, Section C rev l.1039. Text only; no number or verdict changes"
style_notes:
  - "S1-S9, NS1-NS4 carried, unapplied"
  - "NS5 NM1 'excluded' wording: say 'excluded at 20 days and at the subsidiaries'; 15-day low end (~41.1) fits the parent's Q1 FG/WIP +43.55"
  - "NS6 IPD 10-12% (L0792) sits at peer level; competition margin gap is a mix effect"
  - "NS7 header approval date 2026-10-24 vs audit date 2026-10-23"
analyst_note: "Both loop-1 findings are fixed. The rebuilt guide check ties: a bear Q3 print sits below the 19.6-24.1% guide path, and the midpoint then needs a Q4 above every chart Q4 on either revenue split. The export-stock timing test is grafted in all four cells. The seven earlier merged fixes still hold. Coverage and arithmetic are clean. One new item loops to A4, and it is old. The review treats the spoken '464 bps to 26.30%' as the call's one backward-number conflict, 'likely ASR'. That figure is the filed H1 PBT margin, printed in the release (l.780) and the deck (l.994). So every backward number on the call matches the filing, and the ASR heard it right. Only the label slipped, on a call with no finance officer. The fix is text in seven cells, with no number or verdict change. It came from A3 FN01, and both prior merged audits missed it. The loop-2 header calls that loop final, so the operator decides whether to spend a loop or carry NF2 as an open item."
```
