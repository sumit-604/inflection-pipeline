# A2 LEDGER: WeWork India Management Ltd (WEWORK) | q2fy27 | doctype presentation (Shareholders Letter, file tag letter)
Source: runs/wework-q2fy27/extracted/wework-letter-q2fy27-structured.md (R001-R1570). Fulltext used for count method 2 only. No interpretation.

ids_in_structured: 1570 | ids_referenced_in_ledger: 1570 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
METHOD 1 (structured header counts vs grep of row IDs by type)
category: number     header_count: 1399   grep_count: 1399   match: yes
category: entity     header_count: 47   grep_count: 47   match: yes
category: forward    header_count: 20   grep_count: 20   match: yes
category: date       header_count: 40   grep_count: 40   match: yes
category: qualifier  header_count: 64   grep_count: 64   match: yes
category: total      header_count: 1570   grep_count: 1570   unique_ids: 1570   gaps in R001-R1570: 0   match: yes
category: slides     page markers in fulltext body: 31   ledger slide rows: 31   match: yes
category: zero_standing   grep_count: 121   sweep_count: 121   match: yes
category: notes      grep_count (QUALIFIER rows reading Note N): 19   sweep_count: 19 (p25 Notes 3-10 = 8; p31 Notes 3-11 = 9; plus 2 other QUALIFIER rows that cite Note N)   match: yes

METHOD 2 (independent sweep of FULLTEXT numeric tokens per page vs structured NUMBER rows per page)
Pages 22-24 and 28-30 were swept from the IMAGE-VERIFIED appendix blocks, not the misaligned body (body duplicate token counts shown for reference only; not a value source). Pages 2 and 11 swept body plus appendix block.
The token regex counts every digit-bearing token: dates, addresses, phone numbers, statutory refs, list ordinals, axis ticks. A1 correctly leaves these out of NUMBER rows. Dash cells are not tokens but are ZERO_STANDING rows, so the filed-statement diffs go negative by the dash count. A second check looked for each token value inside the structured rows of the same page.

page | fulltext_tokens | structured_NUMBER | diff | explanation / disposition
1 | 22 | 2 | +20 | Address blocks, pin codes, phone, registration identifiers. Not metrics. BSE code and CS membership are rows R001-R002.
2 | 2 | 0 | +2 | Cover date tokens (26th October 2026, H1 & Q2 FY27); captured as DATE R1471-R1472.
3 | 0 | 0 | +0 | Disclaimer text, no numbers.
4 | 13 | 14 | -1 | A1 holds "Six years ago" (R016) as a word-number row; tokens otherwise match 1:1.
5 | 67 | 64 | +3 | A1 splits compound tokens differently (8.5% CoB, 1.5x EBITDA). Value check: every token value present in rows of the page.
6 | 39 | 37 | +2 | Same compound-token effect; value check clean.
7 | 22 | 22 | +0 | Match.
8 | 0 | 0 | +0 | Divider, no data (appendix block confirms).
9 | 8 | 2 | +6 | Numbered values list 01-06 (Member first ... Get it done): ordinals, not metrics. One ENTITY-SUMMARY row covers the values list.
10 | 33 | 19 | +14 | Year and period labels (FY26, 2030, H2 FY27) and running-text repeats. Value check: only a comma fragment unmatched. No value missing.
11 | 57 | 21 | +36 | Body chart text layer and appendix image-check block both swept (double count of FY21-FY26 revenue and occupancy labels), axis ticks 90% and 50%, period labels. All 10 chart data labels are rows R172-R181. Axis ticks are not data points.
12 | 4 | 4 | +0 | Match.
13 | 22 | 13 | +9 | Section ordinals 04 and 05 (PRODUCT SUITE, ASSET QUALITY) and period labels. Value check clean.
14 | 37 | 21 | +16 | Year and period labels (2030, FY26, H2 FY27, 2026). Value check clean.
15 | 15 | 7 | +8 | Period labels and ordinals. Value check clean.
16 | 0 | 0 | +0 | Divider text.
17 | 152 | 189 | -37 | Diff equals 37 ZERO_STANDING dash rows. Net 0.
18 | 157 | 189 | -32 | Diff equals 32 ZERO_STANDING dash rows. Net 0.
19 | 42 | 42 | +0 | Match.
20 | 3 | 0 | +3 | Phone and email digits in contact block. Not metrics.
21 | 44 | 3 | +41 | Auditor letter text: Section 133, Companies Act 2013, SRE 2410, Listing Regulations 2015, Reg 33/34 refs, firm address, pin codes, phone, registration numbers. UDIN illegible in OCR (ENTITY R1429). Not metrics. 3 NUMBER rows kept.
22 | 125 | 150 | -25 | 28 ZERO_STANDING dash rows. Net diff +3: row-label note refs inside the transcription (for example Refer Note 5). Value check: 0 values absent from rows of the page. No MISSING. Body duplicate 164 tokens.
23 | 71 | 72 | -1 | 1 ZERO_STANDING dash row. Net 0. Body duplicate 83 tokens.
24 | 79 | 86 | -7 | 7 ZERO_STANDING dash rows. Net 0. Body duplicate 100 tokens.
25 | 73 | 13 | +60 | Ind AS note text: dates, Regulation and Section refs, Act years, note ordinals. Note numeric content sits in NUMBER rows and QUALIFIERs R1545-R1552. Value check: no metric absent.
26 | 38 | 0 | +38 | Auditor letter refs, dates, address, phone, registration. Not metrics. 0 NUMBER rows is correct.
27 | 47 | 14 | +33 | Auditor text. The Rs 31.51 / 18.58 / 9.55 million subsidiary figures are NUMBER rows (14 rows); remainder dates and statutory refs.
28 | 205 | 210 | -5 | 8 ZERO_STANDING dash rows. Net diff +3: same row-label note-ref effect as page 22. Value check clean. Body duplicate 262 tokens.
29 | 85 | 86 | -1 | 1 ZERO_STANDING dash row. Net 0. Body duplicate 97 tokens.
30 | 83 | 90 | -7 | 7 ZERO_STANDING dash rows. Net 0. Body duplicate 100 tokens.
31 | 108 | 29 | +79 | Consolidated note text: dates, statutory refs, note ordinals. Metric tokens present as NUMBER R1371-R1399 or QUALIFIER text. One gap: Note 8 consolidated paid-up capital figures (Rs 1,385.90 / 1,388.70 / 1,353.78 million, lines 1584-1585) are not split into NUMBER rows on page 31 (same values are R965/R966 and R1177-R1182). Raised as MFS-1, low materiality.
TOTAL | 1653 | 1399 | +254 | Every per-page difference explained above. Dash-count check: ZERO_STANDING by page p17=37, p18=32, p22=28, p23=1, p24=7, p28=8, p29=1, p30=7 (sum 121) equals the 121 ZERO_STANDING rows. One value gap found (MFS-1).
gate_a2: pass
=== END COUNT TEST ===

## 1. SLIDES (31). Columns: page | title | content type | ID ranges by type | A2 flags
page | title | content type | NUMBER | ENTITY | FORWARD | DATE | QUALIFIER | flags
1 | Cover and corporate details | text | R001-R002 | R1400-R1406 | - | R1467-R1470 | R1507 | -
2 | Cover title page (image) | image | - | R1407 | - | R1471-R1472 | - | IMAGE_PAGE
3 | Important notice / disclaimer | text | - | R1408 | - | - | R1508-R1511 | -
4 | Note to shareholders from the CEO | text | R003-R016 | R1409-R1410 | R1447-R1450 | - | - | -
5 | Q2 FY27 at a glance | table/KPI | R017-R080 | R1411 | R1451-R1453 | R1473-R1474 | R1512-R1514 | -
6 | Q2 commentary (numbered points) | text | R081-R117 | R1412 | - | - | R1515-R1516 | -
7 | H1 FY27 at a glance | table/KPI | R118-R139 | - | - | - | R1517 | -
8 | Section divider (image, no data) | image | - | R1413 | - | - | - | IMAGE_PAGE
9 | Spotlight: vision and values | text | R140-R141 | R1414-R1415 | - | - | - | -
10 | Spotlight: flex has gone mainstream | text+chart | R142-R160 | R1416 | R1454-R1455 | R1475 | R1518-R1521 | -
11 | Spotlight: resilient through every cycle | chart+text | R161-R181 | R1417 | R1456 | R1476-R1479 | R1522-R1523 | CHART_LABELS
12 | Spotlight: how companies use space | text | R182-R185 | R1418 | - | - | R1524-R1525 | -
13 | Spotlight: why members choose WeWork and stay | text | R186-R198 | R1419-R1422 | - | - | R1526-R1527 | -
14 | Spotlight: India adding companies and talent | text | R199-R219 | R1423 | R1457-R1460 | R1480-R1484 | R1528 | -
15 | Conclusion: why branded workspaces | text | R220-R226 | - | R1461-R1462 | R1485 | - | -
16 | Annexure divider | text | - | R1424 | - | - | - | -
17 | Annexure: quarterly IndAS to IGAAP reconciliation | table | R227-R415 | - | - | R1486 | R1529-R1532 | ZERO_STANDING
18 | Annexure: half-yearly IndAS to IGAAP reconciliation | table | R416-R604 | - | - | R1487 | R1533-R1535 | ZERO_STANDING
19 | Annexure: rent costs and cash flows | table | R605-R646 | - | - | R1488-R1489 | R1536-R1538 | -
20 | Investor relations contacts | text | - | R1425-R1426 | - | - | - | -
21 | Auditor limited review report, standalone | text (auditor) | R647-R649 | R1427-R1429 | - | R1490-R1491 | R1539-R1541 | -
22 | Standalone statement of P&L (filed) | table | R650-R799 | R1430 | - | R1492-R1493 | R1542 | APPENDIX_ANCHORED, ZERO_STANDING
23 | Standalone assets and liabilities (filed) | table | R800-R871 | - | - | - | R1543 | APPENDIX_ANCHORED, ZERO_STANDING
24 | Standalone cash flows (filed) | table | R872-R957 | - | - | - | R1544 | APPENDIX_ANCHORED, ZERO_STANDING
25 | Standalone results notes | text (notes) | R958-R970 | R1431-R1436 | R1463-R1464 | R1494-R1498 | R1545-R1552 | -
26 | Auditor limited review report, consolidated (part 1) | text (auditor) | - | R1437-R1441 | - | R1499-R1500 | R1553-R1554 | -
27 | Auditor limited review report, consolidated (part 2) | text (auditor) | R971-R984 | - | - | R1501 | R1555-R1558 | -
28 | Consolidated statement of P&L (filed) | table | R985-R1194 | R1442 | - | R1502 | R1559 | APPENDIX_ANCHORED, ZERO_STANDING
29 | Consolidated assets and liabilities (filed) | table | R1195-R1280 | - | - | - | R1560 | APPENDIX_ANCHORED, ZERO_STANDING
30 | Consolidated cash flows (filed) | table | R1281-R1370 | - | - | - | R1561 | APPENDIX_ANCHORED, ZERO_STANDING
31 | Consolidated results notes and signature | text (notes) | R1371-R1399 | R1443-R1446 | R1465-R1466 | R1503-R1506 | R1562-R1570 | -

Dropped slides: not assessable (no prior-quarter ledger). DROPPED_SLIDE not raised.
Pages 22-24 and 28-30: every row anchors to the appendix after page 31 (fulltext lines 1620-1871). Body text on those pages is a misaligned duplicate and is not referenced.

## 2. SLIDE NUMBERS (every NUMBER row by page; value stays in structured file)
page | NUMBER ID range(s) | n | ZERO_STANDING ids | note
1 | R001-R002 | 2 | - | 
4 | R003-R016 | 14 | - | 
5 | R017-R080 | 64 | - | 
6 | R081-R117 | 37 | - | 
7 | R118-R139 | 22 | - | 
9 | R140-R141 | 2 | - | 
10 | R142-R160 | 19 | - | 
11 | R161-R181 | 21 | - | chart data labels R172-R181 (revenue FY21-FY26; occupancy May21, Mar23, Mar25, Mar26)
12 | R182-R185 | 4 | - | 
13 | R186-R198 | 13 | - | 
14 | R199-R219 | 21 | - | 
15 | R220-R226 | 7 | - | 
17 | R227-R415 | 189 | R283, R286, R289, R309, R312, R315, R319, R322, R325, R336, R339, R342, R353-R361, R371-R373, R375, R390, R393, R396, R398-R399, R401-R402, R404-R405, R408, R411, R414 | IndAS to IGAAP reconciliation, quarterly, Rs Cr
18 | R416-R604 | 189 | R472, R475, R478, R498, R501, R504, R508, R511, R514, R525, R528, R531, R542-R548, R561, R579, R582, R585, R587-R588, R590-R591, R593-R594, R597, R600, R603 | IndAS to IGAAP reconciliation, half-yearly, Rs Cr
19 | R605-R646 | 42 | - | rent paid to landlords, cash flow tracing
21 | R647-R649 | 3 | - | 
22 | R650-R799 | 150 | R675-R676, R722-R726, R734-R744, R746-R750, R764-R765, R767-R769 | standalone P&L, Rs Million, six period columns
23 | R800-R871 | 72 | R809 | standalone balance sheet, Rs Million, two date columns
24 | R872-R957 | 86 | R881, R883, R891, R893, R927, R937, R954 | standalone cash flows, Rs Million, two columns
25 | R958-R970 | 13 | - | note-text figures (Labour Codes, IPO, ESOP, capital)
27 | R971-R984 | 14 | - | subsidiary figures in auditor report (unaudited, management-furnished): MGMT_FURNISHED
28 | R985-R1194 | 210 | R1010-R1011, R1075-R1079, R1121 | consolidated P&L, Rs Million, six period columns
29 | R1195-R1280 | 86 | R1206 | consolidated balance sheet, Rs Million
30 | R1281-R1370 | 90 | R1290, R1292, R1300, R1302, R1338-R1339, R1350 | consolidated cash flows, Rs Million
31 | R1371-R1399 | 29 | - | R1381-R1398 restate page 22 standalone values (RESTATED)
TOTAL NUMBER rows: 1399  (filed-statement cells, pages 22-24 and 28-30: 694)

## 3. ZERO_STANDING (nil or dash items, 121; none dropped)
page | IDs | n
17 | R283, R286, R289, R309, R312, R315, R319, R322, R325, R336, R339, R342, R353-R361, R371-R373, R375, R390, R393, R396, R398-R399, R401-R402, R404-R405, R408, R411, R414 | 37
18 | R472, R475, R478, R498, R501, R504, R508, R511, R514, R525, R528, R531, R542-R548, R561, R579, R582, R585, R587-R588, R590-R591, R593-R594, R597, R600, R603 | 32
22 | R675-R676, R722-R726, R734-R744, R746-R750, R764-R765, R767-R769 | 28
23 | R809 | 1
24 | R881, R883, R891, R893, R927, R937, R954 | 7
28 | R1010-R1011, R1075-R1079, R1121 | 8
29 | R1206 | 1
30 | R1290, R1292, R1300, R1302, R1338-R1339, R1350 | 7
Pages 17-18 nil items are in the reconciliation schedule; pages 22/28 nil items are in the filed P&L (includes the exceptional item line). The line exists in the template though nil in the period.
Total ZERO_STANDING: 121

## 4. RESTATED cross-references (pages 4-15: same value and same metric on 2 or more rows)
value | metric | IDs | flag
768.7 Cr | revenue | R006, R072 | RESTATED
162.9 Cr | EBITDA | R011, R033, R083 | RESTATED
21.2% | EBITDA margin | R012, R034, R085 | RESTATED
65.8 Cr | PAT | R015, R035, R094 | RESTATED
83.7% | portfolio occupancy | R017, R064, R125 | RESTATED
237.7 Cr | FCFO | R036, R107 | RESTATED
8.6% | PAT margin | R037, R096 | RESTATED
85 centres | centres | R052, R140 | RESTATED
8 cities | cities | R053, R141 | RESTATED
119.0 Cr | PAT | R097, R124 | RESTATED
379.8 Cr | FCFO | R101, R133 | RESTATED
16.0 Cr | FCFF | R104, R134 | RESTATED
31.1% | ROCE | R114, R132 | RESTATED
16k+ accounts | accounts | R194, R225 | RESTATED
Further RESTATED groups: (a) R1381-R1398 restate page 22 standalone values (Note 11); (b) page 25 Note 8 values R965, R966 restated by R782-R787, R836-R837, R1177-R1182, R1239.
RESTATED value groups listed in table: 14

## 5. ENTITIES (47). ENTITY_CHANGE not assessable (no prior list).
page | ENTITY IDs | n | note
1 | R1400-R1406 | 7 | 
2 | R1407 | 1 | 
3 | R1408 | 1 | 
4 | R1409-R1410 | 2 | 
5 | R1411 | 1 | 
6 | R1412 | 1 | 
8 | R1413 | 1 | 
9 | R1414-R1415 | 2 | 
10 | R1416 | 1 | 
11 | R1417 | 1 | 
12 | R1418 | 1 | 
13 | R1419-R1422 | 4 | 
14 | R1423 | 1 | 
16 | R1424 | 1 | 
20 | R1425-R1426 | 2 | 
21 | R1427-R1429 | 3 | standalone review: auditor R1427; engagement partner name OCR-only R1428; UDIN illegible R1429 (UDIN_UNREADABLE)
22 | R1430 | 1 | 
25 | R1431-R1436 | 6 | 
26 | R1437-R1441 | 5 | consolidation list: Holding Co R1438; subsidiaries WW Tech Solutions India Pvt Ltd R1439, Zoapi Innovations Pvt Ltd R1440; associate MyHQ Anarock Pvt Ltd R1441
28 | R1442 | 1 | 
31 | R1443-R1446 | 4 | signature R1446: Karan Virwani, MD and CEO
Consolidation entities: 4 (1 holding, 2 subsidiaries, 1 associate).

## 6. FORWARD-LOOKING (20) and DATES (40)
type | page | IDs
FORWARD | 4 | R1447-R1450
FORWARD | 5 | R1451-R1453
FORWARD | 10 | R1454-R1455
FORWARD | 11 | R1456
FORWARD | 14 | R1457-R1460
FORWARD | 15 | R1461-R1462
FORWARD | 25 | R1463-R1464
FORWARD | 31 | R1465-R1466
DATE | 1 | R1467-R1470
DATE | 2 | R1471-R1472
DATE | 5 | R1473-R1474
DATE | 10 | R1475
DATE | 11 | R1476-R1479
DATE | 14 | R1480-R1484
DATE | 15 | R1485
DATE | 17 | R1486
DATE | 18 | R1487
DATE | 19 | R1488-R1489
DATE | 21 | R1490-R1491
DATE | 22 | R1492-R1493
DATE | 25 | R1494-R1498
DATE | 26 | R1499-R1500
DATE | 27 | R1501
DATE | 28 | R1502
DATE | 31 | R1503-R1506
Board meeting date R1503 = 26 Oct 2026; signing date R1506 = 26 Oct 2026. Same day, no time of day in structured file. Flag SIGNATURE_TIME_NOT_FOUND.

## 7. FOOTNOTES, NOTES AND DISCLAIMERS (QUALIFIER, 64)
page | QUALIFIER IDs | n | note
1 | R1507 | 1 | 
3 | R1508-R1511 | 4 | safe harbor, rounding, performance, unverified-data disclaimers
5 | R1512-R1514 | 3 | 
6 | R1515-R1516 | 2 | 
7 | R1517 | 1 | 
10 | R1518-R1521 | 4 | 
11 | R1522-R1523 | 2 | 
12 | R1524-R1525 | 2 | 
13 | R1526-R1527 | 2 | 
14 | R1528 | 1 | 
17 | R1529-R1532 | 4 | basis notes
18 | R1533-R1535 | 3 | basis notes
19 | R1536-R1538 | 3 | basis notes
21 | R1539-R1541 | 3 | 
22 | R1542 | 1 | 
23 | R1543 | 1 | 
24 | R1544 | 1 | 
25 | R1545-R1552 | 8 | standalone Notes 3-10 (R1545-R1552); Note 7 prints 468,896
26 | R1553-R1554 | 2 | 
27 | R1555-R1558 | 4 | 
28 | R1559 | 1 | 
29 | R1560 | 1 | 
30 | R1561 | 1 | 
31 | R1562-R1570 | 9 | consolidated Notes 3-11 (R1562-R1570); Note 7 prints 4,68,896 (A1 noted; formatting difference vs page 25)
FOOTNOTE_UNRESOLVED: filed notes begin at Note 3 on pages 25 and 31. Notes 1 and 2 are absent from the text layer and from the appendix transcriptions (likely on the statement page footers). Not in the structured file; low materiality.
Auditor paragraphs (pages 21, 26, 27): carried as ENTITY and QUALIFIER rows. No Emphasis of Matter or Going Concern paragraph tagged by A1. Page 27 subsidiary figures are unaudited and management-furnished (MGMT_FURNISHED).

## 8. MISSING_FROM_STRUCTURED
MFS-1 | page 31 | fulltext lines 1584-1585 | MISSING_FROM_STRUCTURED | Note 8 consolidated: paid-up equity share capital of the Holding Company rose from Rs 1,385.90 million to Rs 1,388.70 million (quarter) and from Rs 1,353.78 million to Rs 1,388.70 million (six months). | Same values already on R965, R966, R1177-R1182. Low materiality.

## 9. ID ACCOUNTABILITY
Every ID R001-R1570 appears in section 1 by page and type range. Sections 2, 3, 5, 6, 7 repeat the ranges by type.
ids_in_structured: 1570 | ids_referenced_in_ledger: 1570 | orphan_ids: [] | match: yes
