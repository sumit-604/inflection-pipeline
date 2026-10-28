# A2 LEDGER | LT | q2fy27 | presentation
REVISION 2026-10-28: updated after A1 CORRECTION_LOG (rows R1491-R1498 added; Domestic/International labels swapped on R244-R251 and R264-R271, values unchanged; page-1 and other line anchors moved). Counts below: structured 1498 = NUMBER 1352 + ENTITY 35 + FORWARD 16 + DATE 18 + QUALIFIER 77.
Source: runs/lt-q2fy27/extracted/lt-presentation-q2fy27-structured.md (R001-R1490). Method 2: sweep of fulltext numeric tokens per page, incl. appendix lines 951-977.
Row format: ROW_ID | category | A2 flags | cross-ref / materiality. Verbatim values stay in the structured file at the ID.
Prior ledger: none (first LT run). DROPPED_SLIDE cannot be assessed; none raised.

ids_in_structured: 1498 | ids_referenced_in_ledger: 1498 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: slides               grep_count: 36 (fulltext [page N] markers; formfeed_count 36)   sweep_count: 36   match: yes
category: structured_ids       grep_count: 1498 (grep ^R### rows)   sweep_count: 1498 (NUMBER 1352 + ENTITY 35 + FORWARD 16 + DATE 18 + QUALIFIER 77)   match: yes
category: slide_numbers        grep_count: 1352 (NUMBER rows)   sweep_count: 1352 after reconciliation (fulltext token sweep 1456 raw; excess explained below)   match: yes
category: zero_standing        grep_count: 39 ([ZERO_STANDING] tags)   sweep_count: 39 (nil/dash cells by slide, section 3)   match: yes
category: footnotes_qualifiers grep_count: 77 (R1422-R1498; R1491-R1498 are slide 12 index labels)   sweep_count: 77   match: yes
category: forward_stmts        grep_count: 16   sweep_count: 16   match: yes
category: dates                grep_count: 18   sweep_count: 18   match: yes
category: entities             grep_count: 35 (R1353-R1387, 4 are ENTITY-SUMMARY)   sweep_count: 35   match: yes
gate_a2: pass
=== END COUNT TEST ===

## RECONCILIATION: fulltext sweep vs structured NUMBER rows (independent second method)
Sweep = numeric tokens plus dash cells per page of fulltext, then a value-multiset diff against NUMBER-row values. Raw token total 1456 (incl. dash cells and footers) vs 1352 rows. Value-level diff is clean on every numeric slide except the items below.
- Printed slide-number footer: one token per slide on pages 5-6, 9-10, 13-24, 27-36 (page 28 shows footer 27). Not a disclosure unit. Explains the +1 per page.
- Page 8: values 54 and 10 (R1388-R1390 commentary, body lines 172-174) sit outside the appendix lines the sweep used for this slide. Covered.
- Page 21: 70, 2.60, 18.67 (PCR, RoA, CRAR; body line 502) sit outside the appendix. Covered by structured rows.
- Page 12: segment index digits 1-8. R1352 holds the PPM definition; M1 now resolved by R1491-R1498. Token "1111" at line 271 is a layout artefact (M2).
- Page 1: letter address digits. PINs and CIN are in R1384; tel/fax digits are not. See M3. Dates, ISO and IDs covered by R1404-R1405, R1386.
- Pages 35-36: "FY22-25" tokens are the qualifier text of R1483-R1484. Covered.
- Dash cells: fulltext dashes on pages 31, 32, 34, 36 reconcile to the 39 ZERO_STANDING rows; dash tokens on pages 7, 12, 25 are punctuation.
- Line anchors: A1 correction made page-1 rows absolute fulltext lines (e.g. R1404 line 29) and moved R1352 to line 266. Page-1 line cells in the register reflect the corrected structured file; read line at the ID.

## 1. SLIDE REGISTER (36 slides)
SLIDE | title | content type | NUMBER ids (count) | other ids (count) | fulltext start line | flags
S01 | Reg 30 cover letter to BSE/NSE | text | R1348-R1351 (4) | R1353-R1359,R1384,R1386,R1398,R1404-R1406 (13) | line 17 | UNIT=Rs bn
S02 | Earnings Call Presentation cover | photo/text | - (0) | R1407-R1408 (2) | line 69 | SECTION_DIVIDER_NO_NUMBERS
S03 | Disclaimer | text | - (0) | R1385,R1487 (2) | line 75 | DISCLAIMER
S04 | 01 Key Highlights divider | photo | - (0) | R1360 (1) | line 91 | SECTION_DIVIDER_NO_NUMBERS
S05 | A Record Quarter amidst Volatility | chart/KPI | R001-R012 (12) | R1409,R1422-R1423,R1428,R1490 (5) | line 96 | UNIT=Rs bn
S06 | Key Financial Indicators | table | R013-R048 (36) | R1410,R1424-R1427 (5) | line 115 | UNIT=Rs bn
S07 | 02 Group divider (PMCH photo) | photo | - (0) | R1361,R1399 (2) | line 146 | SECTION_DIVIDER_NO_NUMBERS
S08 | Q2/H1 FY27 Order Inflow / Order Book | chart+table | R049-R071 (23) | R1388-R1390,R1411,R1421,R1429-R1430 (7) | line 153 | UNIT=Rs bn
S09 | Group P&L Construct: Revenue to EBITDA | table+remarks | R072-R121 (50) | R1371-R1372,R1431-R1438 (10) | line 178 | UNIT=Rs bn
S10 | Group P&L Construct: EBITDA to PAT | table+remarks | R122-R167 (46) | R1373-R1374,R1439-R1442 (6) | line 213 | UNIT=Rs bn
S11 | 03 Segment Performance Analysis divider | photo | - (0) | R1362 (1) | line 242 | SECTION_DIVIDER_NO_NUMBERS
S12 | Current Segment Composition | diagram/text | R1352 (1) | R1363-R1370,R1397,R1412,R1443-R1445,R1491-R1498 (21) | line 247 | UNIT=Rs bn
S13 | Order Inflow Composition | chart | R168-R187 (20) | - (0) | line 274 | UNIT=Rs bn
S14 | Order Book as on 30-Sep-2026 | chart | R188-R197 (10) | R1413 (1) | line 297 | UNIT=Rs bn
S15 | Revenue Composition | chart | R198-R217 (20) | - (0) | line 318 | UNIT=Rs bn
S16 | Infrastructure & Utilities | chart+remarks | R218-R237 (20) | R1375,R1400,R1446-R1447 (4) | line 338 | UNIT=Rs bn
S17 | Energy - Conventional | chart+remarks | R238-R257 (20) | R1376,R1448-R1451 (5) | line 366 | UNIT=Rs bn
S18 | Energy - Green | chart+remarks | R258-R277 (20) | R1377,R1401,R1452-R1453 (4) | line 393 | UNIT=Rs bn
S19 | Manufacturing & Products | chart+remarks | R278-R297 (20) | R1378,R1454-R1457 (5) | line 421 | UNIT=Rs bn
S20 | Technology, Platforms & Services | chart+remarks | R298-R321 (24) | R1379,R1458-R1461 (5) | line 453 | UNIT=Rs bn
S21 | Financial Services | table+chart+remarks | R322-R350 (29) | R1383,R1403,R1420,R1462-R1463 (5) | line 483 | UNIT=Rs bn
S22 | Realty | chart+remarks | R351-R362 (12) | R1402,R1464 (2) | line 507 | UNIT=Rs bn
S23 | Return Ratios - PP&M portfolio | table | R363-R410 (48) | R1414,R1465-R1468,R1488 (6) | line 528 | UNIT=Rs crore
S24 | Return Ratios - Group | table | R411-R473 (63) | R1415,R1469-R1471,R1489 (5) | line 552 | ZERO_STANDING x1; UNIT=Rs crore
S25 | Resilient Portfolio; Disciplined Growth | text | - (0) | R1391-R1396,R1472 (7) | line 583 | -
S26 | Thank You / IR contacts | text | - (0) | R1380-R1381,R1387 (3) | line 610 | -
S27 | Balance Sheet | table | R474-R516 (43) | R1416 (1) | line 619 | UNIT=Rs bn
S28 | Cash & Cash Equivalents and Current Investments Breakup | table | R517-R526 (10) | R1382 (1) | line 642 | UNIT=Rs bn
S29 | Cash Flow - As Reported | table | R527-R611 (85) | R1417,R1473 (2) | line 654 | UNIT=Rs bn
S30 | Memorandum Cash Flow - Excl Financial Services | table | R612-R691 (80) | R1474 (1) | line 687 | ZERO_STANDING x2; UNIT=Rs bn
S31 | Segment Details - Q2 FY27 | table | R692-R805 (114) | R1475-R1476,R1479 (3) | line 716 | ZERO_STANDING x8; UNIT=Rs crore
S32 | Segment Details - H1 FY27 | table | R806-R920 (115) | R1477-R1478 (2) | line 770 | ZERO_STANDING x7; UNIT=Rs crore
S33 | Segment Breakup (EC, M&P) | table | R921-R1064 (144) | R1480-R1481 (2) | line 815 | UNIT=Rs bn
S34 | Order Inflow and Order Book Details | table | R1065-R1192 (128) | R1482 (1) | line 863 | ZERO_STANDING x19; UNIT=Rs crore
S35 | Order Inflow Trend, new segment composition | table | R1193-R1247 (55) | R1418,R1483,R1485 (3) | line 896 | UNIT=Rs crore
S36 | Revenue Trend, new segment composition | table | R1248-R1347 (100) | R1419,R1484,R1486 (3) | line 926 | ZERO_STANDING x2; UNIT=Rs crore

## 2. SLIDE NUMBERS (R001-R1352) by slide with unit
slide: count | unit | ID range
S01: 4 | Rs bn | R1348-R1351
S05: 12 | Rs bn | R001-R012
S06: 36 | Rs bn | R013-R048
S08: 23 | Rs bn | R049-R071
S09: 50 | Rs bn | R072-R121
S10: 46 | Rs bn | R122-R167
S12: 1 | Rs bn | R1352
S13: 20 | Rs bn | R168-R187
S14: 10 | Rs bn | R188-R197
S15: 20 | Rs bn | R198-R217
S16: 20 | Rs bn | R218-R237
S17: 20 | Rs bn | R238-R257
S18: 20 | Rs bn | R258-R277
S19: 20 | Rs bn | R278-R297
S20: 24 | Rs bn | R298-R321
S21: 29 | Rs bn | R322-R350
S22: 12 | Rs bn | R351-R362
S23: 48 | Rs crore | R363-R410
S24: 63 | Rs crore | R411-R473
S27: 43 | Rs bn | R474-R516
S28: 10 | Rs bn | R517-R526
S29: 85 | Rs bn | R527-R611
S30: 80 | Rs bn | R612-R691
S31: 114 | Rs crore | R692-R805
S32: 115 | Rs crore | R806-R920
S33: 144 | Rs bn | R921-R1064
S34: 128 | Rs crore | R1065-R1192
S35: 55 | Rs crore | R1193-R1247
S36: 100 | Rs crore | R1248-R1347
TOTAL: 1352

## 3. ZERO_STANDING rows
ROW_ID | category | flags | slide / line | note
R0416 | slide_number | ZERO_STANDING | S24 line 966 | Gross Revenue (H1 FY27 TTM), Corporate
R0629 | slide_number | ZERO_STANDING | S30 line 969 | Excl Financial Services: Loan towards financing activities, Q2 FY27
R0667 | slide_number | ZERO_STANDING | S30 line 969 | Excl Financial Services: Issue of Share Capital/Payment of Dividend to NCI, Q2 FY26
R0743 | slide_number | ZERO_STANDING | S31 line 970 | Development Projects, Q2 FY27 Net Revenue
R0787 | slide_number | ZERO_STANDING | S31 line 970 | Non-controlling interest (Q2 FY27), Realty
R0788 | slide_number | ZERO_STANDING | S31 line 970 | Non-controlling interest (Q2 FY27), DP
R0790 | slide_number | ZERO_STANDING | S31 line 970 | Non-controlling interest (Q2 FY27), Corporate
R0793 | slide_number | ZERO_STANDING | S31 line 970 | Share in profit/(loss) of JV and associate (Q2 FY27), FS
R0794 | slide_number | ZERO_STANDING | S31 line 970 | Share in profit/(loss) of JV and associate (Q2 FY27), Realty
R0795 | slide_number | ZERO_STANDING | S31 line 970 | Share in profit/(loss) of JV and associate (Q2 FY27), DP
R0797 | slide_number | ZERO_STANDING | S31 line 970 | Share in profit/(loss) of JV and associate (Q2 FY27), Corporate
R0902 | slide_number | ZERO_STANDING | S32 line 971 | Non-controlling interest (H1 FY27), Realty
R0903 | slide_number | ZERO_STANDING | S32 line 971 | Non-controlling interest (H1 FY27), DP
R0905 | slide_number | ZERO_STANDING | S32 line 971 | Non-controlling interest (H1 FY27), Corporate
R0908 | slide_number | ZERO_STANDING | S32 line 971 | Share in profit/(loss) of JV and associate (H1 FY27), FS
R0909 | slide_number | ZERO_STANDING | S32 line 971 | Share in profit/(loss) of JV and associate (H1 FY27), Realty
R0910 | slide_number | ZERO_STANDING | S32 line 971 | Share in profit/(loss) of JV and associate (H1 FY27), DP
R0912 | slide_number | ZERO_STANDING | S32 line 971 | Share in profit/(loss) of JV and associate (H1 FY27), Corporate
R1134 | slide_number | ZERO_STANDING | S34 line 974 | Technology, Platforms & Services, % Int 30-Sep-25
R1136 | slide_number | ZERO_STANDING | S34 line 974 | Technology, Platforms & Services, % Int 30-Sep-26
R1138 | slide_number | ZERO_STANDING | S34 line 974 | Financial Services, % Int Q2 FY26
R1140 | slide_number | ZERO_STANDING | S34 line 974 | Financial Services, % Int Q2 FY27
R1142 | slide_number | ZERO_STANDING | S34 line 974 | Financial Services, % Int H1 FY26
R1144 | slide_number | ZERO_STANDING | S34 line 974 | Financial Services, % Int H1 FY27
R1145 | slide_number | ZERO_STANDING | S34 line 974 | Financial Services, Order Book 30-Sep-25
R1146 | slide_number | ZERO_STANDING | S34 line 974 | Financial Services, % Int 30-Sep-25
R1147 | slide_number | ZERO_STANDING | S34 line 974 | Financial Services, Order Book 30-Sep-26
R1148 | slide_number | ZERO_STANDING | S34 line 974 | Financial Services, % Int 30-Sep-26
R1154 | slide_number | ZERO_STANDING | S34 line 974 | Realty, % Int 30-Sep-25
R1156 | slide_number | ZERO_STANDING | S34 line 974 | Realty, % Int 30-Sep-26
R1158 | slide_number | ZERO_STANDING | S34 line 974 | Development Projects, % Int Q2 FY26
R1159 | slide_number | ZERO_STANDING | S34 line 974 | Development Projects, Order Inflow Q2 FY27
R1160 | slide_number | ZERO_STANDING | S34 line 974 | Development Projects, % Int Q2 FY27
R1162 | slide_number | ZERO_STANDING | S34 line 974 | Development Projects, % Int H1 FY26
R1164 | slide_number | ZERO_STANDING | S34 line 974 | Development Projects, % Int H1 FY27
R1167 | slide_number | ZERO_STANDING | S34 line 974 | Development Projects, Order Book 30-Sep-26
R1168 | slide_number | ZERO_STANDING | S34 line 974 | Development Projects, % Int 30-Sep-26
R1258 | slide_number | ZERO_STANDING | S36 line 976 | Revenue: Energy - Green, FY22
R1308 | slide_number | ZERO_STANDING | S36 line 976 | EBITDA %: Energy - Green, FY22
ZERO_STANDING total: 39
Cluster note: slides 31-32 NCI and JV/associate lines nil for Realty, DP, Corporate, FS; slide 34 Financial Services and Development Projects nil order book and nil international share, Realty and TPS nil % Int on some dates; slide 36 Energy-Green FY22 revenue and margin nil; slide 30 two nil financing lines; slide 24 Corporate gross revenue 0.

## 3b. LABEL_SWAP rows
R244-R251 (S17) and R264-R271 (S18) | slide_number | LABEL_SWAP (A1 correction 2026-10-28: Domestic/International labels swapped, values unchanged; read labels from structured)

## 4. RESTATED cross-references
ROW_ID | category | flags | cross-ref
R001 | restated | RESTATED | with R014: Order inflow Q2 FY27 1477 (slides 5,6)
R003 | restated | RESTATED | with R023: Revenue Q2 787 (5,6)
R005 | restated | RESTATED | with R033: PAT Q2 52 (5,6)
R007 | restated | RESTATED | with R020: Order book 8535 (5,6)
R009 | restated | RESTATED | with R039: NWC 1.7% (5,6)
R011 | restated | RESTATED | with R041: ROE 16.7% (5,6)
R012 | restated | RESTATED | with R048: Labour Code 100 bps (5,6)
R1422 | restated | RESTATED | with R1424: ROE footnote (5,6)
R1423 | restated | RESTATED | with R1425: ROE marker (5,6)
R1387 | restated | RESTATED | footer tagline repeated on slides

## 5. FOOTNOTES, FINE PRINT AND MANAGEMENT REMARKS (QUALIFIER, 77)
ROW_ID | category | flags | slide / line | note
R1422 | qualifier | FOOTNOTE; FOOTNOTE_QUALIFIES_ROE; RESTATED | S05 line 110 | see structured row
R1423 | qualifier | - | S05 line 108 | see structured row
R1424 | qualifier | FOOTNOTE; FOOTNOTE_QUALIFIES_ROE; RESTATED | S06 line 142 | see structured row
R1425 | qualifier | - | S06 line 135 | see structured row
R1426 | qualifier | - | S06 line 140 | see structured row
R1427 | qualifier | - | S06 line 125 | see structured row
R1428 | qualifier | HEADLINE_QUALIFIER | S05 line 106 | see structured row
R1429 | qualifier | - | S08 line 156 | see structured row
R1430 | qualifier | - | S08 line 169 | see structured row
R1431 | qualifier | FOOTNOTE | S09 line 201 | see structured row
R1432 | qualifier | FOOTNOTE | S09 line 202 | see structured row
R1433 | qualifier | - | S09 line 185 | see structured row
R1434 | qualifier | MGMT_REMARK | S09 line 187 | see structured row
R1435 | qualifier | MGMT_REMARK | S09 line 191 | see structured row
R1436 | qualifier | MGMT_REMARK | S09 line 197 | see structured row
R1437 | qualifier | MGMT_REMARK | S09 line 202 | see structured row
R1438 | qualifier | MGMT_REMARK | S09 line 207 | see structured row
R1439 | qualifier | MGMT_REMARK | S10 line 220 | see structured row
R1440 | qualifier | MGMT_REMARK | S10 line 221 | see structured row
R1441 | qualifier | MGMT_REMARK | S10 line 231 | see structured row
R1442 | qualifier | MGMT_REMARK | S10 line 237 | see structured row
R1443 | qualifier | FOOTNOTE; PORTFOLIO_STATUS | S12 line 267 | see structured row
R1444 | qualifier | FOOTNOTE; PORTFOLIO_STATUS | S12 line 268 | see structured row
R1445 | qualifier | - | S12 line 265 | see structured row
R1446 | qualifier | MGMT_REMARK | S16 line 362 | see structured row
R1447 | qualifier | MGMT_REMARK | S16 line 361 | see structured row
R1448 | qualifier | FOOTNOTE; RECLASSIFICATION | S17 line 389 | see structured row
R1449 | qualifier | MGMT_REMARK | S17 line 387 | see structured row
R1450 | qualifier | MGMT_REMARK | S17 line 386 | see structured row
R1451 | qualifier | MGMT_REMARK | S17 line 385 | see structured row
R1452 | qualifier | MGMT_REMARK | S18 line 416 | see structured row
R1453 | qualifier | MGMT_REMARK | S18 line 417 | see structured row
R1454 | qualifier | MGMT_REMARK | S19 line 444 | see structured row
R1455 | qualifier | MGMT_REMARK | S19 line 445 | see structured row
R1456 | qualifier | MGMT_REMARK | S19 line 446 | see structured row
R1457 | qualifier | DEFENCE_DISCLAIMER | S19 line 448 | see structured row
R1458 | qualifier | MGMT_REMARK | S20 line 473 | see structured row
R1459 | qualifier | MGMT_REMARK | S20 line 474 | see structured row
R1460 | qualifier | MGMT_REMARK | S20 line 475 | see structured row
R1461 | qualifier | FOOTNOTE | S20 line 479 | see structured row
R1462 | qualifier | MGMT_REMARK | S21 line 502 | see structured row
R1463 | qualifier | - | S21 line 490 | see structured row
R1464 | qualifier | MGMT_REMARK | S22 line 524 | see structured row
R1465 | qualifier | FOOTNOTE | S23 line 546 | see structured row
R1466 | qualifier | FOOTNOTE | S23 line 548 | see structured row
R1467 | qualifier | FOOTNOTE | S23 line 548 | see structured row
R1468 | qualifier | RENDER_OBSERVATION | S23 line 965 | see structured row
R1469 | qualifier | FOOTNOTE | S24 line 577 | see structured row
R1470 | qualifier | FOOTNOTE | S24 line 577 | see structured row
R1471 | qualifier | FOOTNOTE; REGROUPED_HISTORY | S24 line 579 | see structured row
R1472 | qualifier | FOOTNOTE | S25 line 606 | see structured row
R1473 | qualifier | - | S29 line 655 | see structured row
R1474 | qualifier | - | S30 line 688 | see structured row
R1475 | qualifier | FOOTNOTE | S31 line 766 | see structured row
R1476 | qualifier | FOOTNOTE | S31 line 766 | see structured row
R1477 | qualifier | FOOTNOTE; RESTATED (slide 31 twin) | S32 line 811 | see structured row
R1478 | qualifier | FOOTNOTE; RESTATED (slide 31 twin) | S32 line 811 | see structured row
R1479 | qualifier | - | S31 line 719 | see structured row
R1480 | qualifier | FOOTNOTE; RECLASSIFICATION | S33 line 839 | see structured row
R1481 | qualifier | FOOTNOTE; RECLASSIFICATION | S33 line 859 | see structured row
R1482 | qualifier | - | S34 line 866 | see structured row
R1483 | qualifier | FOOTNOTE; INDICATIVE_HISTORY | S35 line 922 | see structured row
R1484 | qualifier | FOOTNOTE; INDICATIVE_HISTORY | S36 line 946 | see structured row
R1485 | qualifier | - | S35 line 899 | see structured row
R1486 | qualifier | - | S36 line 929 | see structured row
R1487 | qualifier | - | S03 line 76 | see structured row
R1488 | qualifier | - | S23 line 533 | see structured row
R1489 | qualifier | - | S24 line 555 | see structured row
R1490 | qualifier | HEADLINE_QUALIFIER | S05 line 99 | see structured row
R1491 | qualifier | SEGMENT_INDEX_LABEL | S12 line 250 | slide 12 index label (closes M1)
R1492 | qualifier | SEGMENT_INDEX_LABEL | S12 line 250 | slide 12 index label (closes M1)
R1493 | qualifier | SEGMENT_INDEX_LABEL | S12 line 259 | slide 12 index label (closes M1)
R1494 | qualifier | SEGMENT_INDEX_LABEL | S12 line 250 | slide 12 index label (closes M1)
R1495 | qualifier | SEGMENT_INDEX_LABEL | S12 line 250 | slide 12 index label (closes M1)
R1496 | qualifier | SEGMENT_INDEX_LABEL | S12 line 268 | slide 12 index label (closes M1)
R1497 | qualifier | SEGMENT_INDEX_LABEL | S12 line 268 | slide 12 index label (closes M1)
R1498 | qualifier | SEGMENT_INDEX_LABEL | S12 line 261 | slide 12 index label (closes M1)

Flag notes: R1457 defence disclaimer; R1448 and R1480-R1481 segment reclassifications; R1471 and R1483-R1484 history regrouped or indicative, so FY22-25 trends are not like for like; R1422/R1424 ROE 16.7% includes 100 bps Labour Code hit.

## 6. FORWARD-LOOKING STATEMENTS (16)
ROW_ID | category | flags | slide / line | note
R1388 | forward | - | S08 line 174 | forward or claim statement
R1389 | forward | - | S08 line 172 | forward or claim statement
R1390 | forward | - | S08 line 173 | forward or claim statement
R1391 | forward | - | S25 line 597 | forward or claim statement
R1392 | forward | - | S25 line 598 | forward or claim statement
R1393 | forward | - | S25 line 598 | forward or claim statement
R1394 | forward | - | S25 line 587 | forward or claim statement
R1395 | forward | - | S25 line 603 | forward or claim statement
R1396 | forward | - | S25 line 594 | forward or claim statement
R1397 | forward | - | S12 line 267 | forward or claim statement
R1398 | forward | - | S01 line 28 | forward or claim statement
R1399 | forward | - | S07 line 147 | forward or claim statement
R1400 | forward | - | S16 line 360 | forward or claim statement
R1401 | forward | - | S18 line 415 | forward or claim statement
R1402 | forward | - | S22 line 523 | forward or claim statement
R1403 | forward | - | S21 line 501 | forward or claim statement

## 7. DATES (18)
ROW_ID | category | flags | slide / line | note
R1404 | date | - | S01 line 13 | period or date reference
R1405 | date | - | S01 line 55 | period or date reference
R1406 | date | - | S01 line 24 | period or date reference
R1407 | date | - | S02 line 73 | period or date reference
R1408 | date | - | S02 line 71 | period or date reference
R1409 | date | - | S05 line 110 | period or date reference
R1410 | date | - | S06 line 131 | period or date reference
R1411 | date | - | S08 line 167 | period or date reference
R1412 | date | - | S12 line 267 | period or date reference
R1413 | date | - | S14 line 298 | period or date reference
R1414 | date | - | S23 line 533 | period or date reference
R1415 | date | - | S24 line 557 | period or date reference
R1416 | date | - | S27 line 620 | period or date reference
R1417 | date | - | S29 line 657 | period or date reference
R1418 | date | - | S35 line 903 | period or date reference
R1419 | date | - | S36 line 931 | period or date reference
R1420 | date | - | S21 line 503 | period or date reference
R1421 | date | - | S08 line 163 | period or date reference

## 8. ENTITIES (35, R1353-R1387)
ROW_ID | category | flags | slide / line | note
R1353 | entity | - | S01 line 2 | ENTITY
R1354 | entity | - | S01 line 15 | ENTITY
R1355 | entity | - | S01 line 15 | ENTITY
R1356 | entity | - | S01 line 26 | ENTITY
R1357 | entity | - | S01 line 29 | ENTITY
R1358 | entity | - | S01 line 60 | ENTITY
R1359 | entity | - | S01 line 55 | ENTITY
R1360 | entity | - | S04 line 92 | ENTITY
R1361 | entity | - | S07 line 147 | ENTITY
R1362 | entity | - | S11 line 243 | ENTITY
R1363 | entity | - | S12 line 254 | ENTITY
R1364 | entity | - | S12 line 254 | ENTITY
R1365 | entity | - | S12 line 254 | ENTITY
R1366 | entity | - | S12 line 254 | ENTITY
R1367 | entity | - | S12 line 254 | ENTITY
R1368 | entity | PORTFOLIO_STATUS (Nabha divested 25-Jun-2026; Hyderabad Metro held for sale) | S12 line 266 | ENTITY
R1369 | entity | - | S12 line 270 | ENTITY
R1370 | entity | - | S12 line 270 | ENTITY
R1371 | entity | - | S09 line 203 | ENTITY
R1372 | entity | - | S09 line 203 | ENTITY
R1373 | entity | NON_CONSOLIDATION (Hyderabad Metro) | S10 line 221 | ENTITY
R1374 | entity | - | S10 line 233 | ENTITY
R1375 | entity | - | S16 line 362 | ENTITY
R1376 | entity | - | S17 line 385 | ENTITY
R1377 | entity | - | S18 line 416 | ENTITY
R1378 | entity | - | S19 line 444 | ENTITY
R1379 | entity | - | S20 line 474 | ENTITY
R1380 | entity | - | S26 line 614 | ENTITY
R1381 | entity | - | S26 line 615 | ENTITY
R1382 | entity | - | S28 line 649 | ENTITY
R1383 | entity | - | S21 line 501 | ENTITY
R1384 | entity | - | S01 line 17 | ENTITY-SUMMARY
R1385 | entity | - | S03 line 76 | ENTITY-SUMMARY
R1386 | entity | - | S01 line 67 | ENTITY-SUMMARY
R1387 | entity | - | S26 line 613 | ENTITY-SUMMARY
ENTITY_CHANGE: no prior list to diff. In-deck status changes: Nabha Power divested, Hyderabad Metro held for sale and not consolidated, MRU business reclassified into Energy - Conventional (R1448).

## 9. MISSING_FROM_STRUCTURED (fulltext sweep; loop back to A1)
ROW_ID | category | flags | fulltext line | claim text
M1 | RESOLVED | segment index labels now in structured as R1491-R1498 (A1 correction 2026-10-28).
M2 | CLOSED_NO_DATA | stray "1111" at S12 line 271 is a layout artefact; A1 skipped it.
M3 | CLOSED_NO_DATA | S01 tel/fax digits; A1 skipped them as no analytic data.
No open MISSING_FROM_STRUCTURED rows remain.

## 10. TEXT-ONLY SLIDES (no NUMBER rows): S02 R1407-R1408; S03 R1385,R1487; S04 R1360; S07 R1361,R1399; S11 R1362; S25 R1391-R1396,R1472; S26 R1380-R1381,R1387.

## 11. OBSERVATIONS FOR A3/A4 (no interpretation)
Slides 23-24 gross segment revenue YoY blank for TTM Sep-25 (R1468). Slide 5 values are displayed rounded (R1490). Slide 25 tailwinds and headwinds are illustrative (R1472).
