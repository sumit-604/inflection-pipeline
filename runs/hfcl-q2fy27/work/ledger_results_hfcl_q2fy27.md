# LEDGER: results HFCL Q2 FY27 (A2)

ids_in_structured: 1507 | ids_referenced_in_ledger: 1507 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes          grep_count: 10   sweep_count: 10   match: yes   (grep -o distinct note labels: Note 1,2,3(i),3(ii),4,4(o),5,6, CF note 1, CF note 2)
category: line_items(FS)  grep_count: 153 sweep_count: 153   match: yes   (distinct labels 152 + one label repeated across current and non-current lease liabilities blocks = 153; cells 1076 = 32x12+26x12+45x4+50x4)
category: line_items(PR)  grep_count: 14  sweep_count: 14   match: yes
category: zero_standing  grep_count: 103 sweep_count: 103 cells in 24 line items + R051,R052   match: yes (101 A1-tagged + 2 untagged 0.00 R1268, R1270; sweep cells include those 2, so grep 101 + 2 = 103)
category: agenda_items   grep_count: 1   sweep_count: 1   match: yes   (letter names only results; "inter-alia" flag raised)
category: auditor_paras  grep_count: 10 (numbered lines in fulltext L88-L270)  sweep_count: 11 (SA p1-3 + CA p1-8)   match: yes after resolution (fulltext L99 prints "I." = standalone para 1)
category: entities       grep_count: 15 (Note 4 rows)  sweep_count: 15 (11 review-list + parent, Canada, UK, Pty)   match: yes
category: forward        grep_count: 21  sweep_count: 21   match: yes
category: superseded_ids grep_count: 124  sweep_count: 124  match: yes
category: type_totals    A1 header NUMBER 1325 ENTITY 77 FORWARD 21 DATE 35 QUALIFIER 49 = 1507; grep identical  match: yes
gate_a2: pass
=== END COUNT TEST ===

## 1. BOARD LETTER / AGENDA (page 1)
| ROW_ID | category | A2 flags | cross-ref / materiality |
|---|---|---|---|
| R002-R005 | addressees / security codes | | BSE 500183, NSE HFCL |
| R008-R010 | board meeting date / earlier intimation | | meeting 19 Oct 2026; intimation 13 Oct 2026 |
| R006 | meeting start 11:00 | | |
| R007 | meeting end 11:40 | | 40-minute meeting |
| R001, R011-R012, R016, R018-R019 | AGENDA ITEM 1: approve Q2/H1 FY27 unaudited standalone+consolidated results with limited review reports; Audit Committee recommended | INTER_ALIA_OTHER_ITEMS_UNLISTED | Only one item named; letter says "inter-alia" so other items, if any, are not disclosed. No AR, AGM, dividend, director, auditor, ESOP, fund-raise item present |
| R013-R014 | statutory auditors named | | S. Bhandari & Co LLP; Oswal Sunil & Company (joint auditors) |
| R015, R020 | signature block: Manoj Baid, President & Company Secretary, signed 2026.10.19 11:41:38 +05:30 | | signed 1 min 38 s after stated conclusion 11:40; no pre-meeting timestamp flag |
| R017 | registered office / CIN | | |
| M01 | Reg 47 newspaper publication arranged | MISSING_FROM_STRUCTURED | fulltext L58 |
| M02 | results also on www.hfcl.com | MISSING_FROM_STRUCTURED | fulltext L60 |
| M03 | enclosures listed: Results+LRR; Statement of Assets and Liabilities; Statement of Cash Flow; Press Release | MISSING_FROM_STRUCTURED | fulltext L80-83 |
| M04 | disclosure basis: Reg 30 read with Para A Part A Schedule III | MISSING_FROM_STRUCTURED | fulltext L42 |

## 2. AUDITOR REPORT PARAGRAPHS (pages 2-4)
| ROW_ID | category | A2 flags | cross-ref / materiality |
|---|---|---|---|
| R021-R022, R028, R033 | Standalone para 1: scope, Reg 33, Ind AS 34 |  | |
| R029-R030, R032 | Standalone para 2: SRE 2410, moderate assurance, no audit opinion |  | |
| R031 | Standalone para 3: conclusion, nothing came to attention (unmodified) |  | |
| R023-R027 | Standalone signature block: J.S.P. Bansal (S Bhandari) Memb 070980; Oswal partner; 2 UDINs; place/date 19 Oct 2026 | UDIN_OCR_UNCERTAIN | |
| R048 | Consolidated para 1: scope |  | |
| (no structured row of its own) | Consolidated para 2: mgmt responsibility | | para exists in fulltext |
| R045-R046, R049 | Consolidated para 3: SRE 2410, no audit opinion |  | |
| R034-R044 | Consolidated para 4: entity list reviewed (9 subs + 2 JCE) | ENTITY_CHANGE_CHECK (see sec 3) | |
| R047 | Consolidated para 5: conclusion unmodified |  | |
| R050-R057, R075 | Consolidated para 6: 3 subs + 2 JCE not reviewed by signing auditors; reviewed by other respective auditors whose reports were furnished by Management (fulltext L227-228) | ZERO_STANDING; UNREVIEWED_ENTITIES | |
| R058-R065, R076 | Consolidated para 7: 4 subs reviewed by one joint auditor | RELIANCE_ON_OTHER_AUDITOR | |
| R066-R074, R077 | Consolidated para 8: 2 foreign subs, converted to Indian GAAP by mgmt | MGMT_FURNISHED_CONVERSION | |
| R078-R081 | Consolidated signature block: 2 UDINs, place/date 19 Oct 2026 | UDIN_OCR_UNCERTAIN | |
| (none) | Emphasis of Matter / Other Matter / Going Concern / modified opinion | ABSENT | no such paragraph in A1 rows or fulltext; opinion type = unmodified limited review conclusion on both reports |
| M06 | Para 6: total comprehensive income of 3 unreviewed subs Rs (0.17) Cr Q2 and Rs (0.18) Cr H1 FY27 | MISSING_FROM_STRUCTURED | fulltext L221-222 |
| M07 | Para 7: net cash flows of four subs Rs (0.29) Cr, Apr-Sep 2026 | MISSING_FROM_STRUCTURED | fulltext L238 |
| M08 | Press release outlook: "Our advanced optical fiber cable portfolio and data centre connectivity solutions continue to strengthen." | MISSING_FROM_STRUCTURED; FORWARD | fulltext L749-750 |
| M05 | Oswal Sunil & Co signing partner Membership No. 056931 (name illegible) on consolidated report; "05693 I" on standalone | MISSING_FROM_STRUCTURED | fulltext L262, ~L135 |

## 3. CONSOLIDATION ENTITIES
Sources: review-report para 4 list (R034-R044, 11 entities) and Note 4 list (R1491-R1505, 15 entities). No prior ledger, so cross-quarter diff not possible.
| ROW_ID | entity | relationship | A2 flags | cross-ref |
|---|---|---|---|---|
| R1491 | HFCL Limited | Holding Company |  | in Note 4 only, not in review-report para 4 list |
| R034, R1492 | HTL Limited | Subsidiary |  | in both lists |
| R038, R1493 | Raddef Private Limited | Subsidiary |  | in both lists |
| R036, R1494 | Moneta Finance Private Limited | WOS |  | in both lists |
| R035, R1495 | Polixel Security Systems Private Limited | WOS |  | in both lists |
| R037, R1496 | HFCL Advance Systems Private Limited | WOS |  | in both lists |
| R039, R1497 | DragonWave HFCL India Private Limited | WOS |  | in both lists |
| R040, R1498 | HFCL Technologies Private Limited | WOS |  | in both lists |
| R041, R1499 | HFCL Inc. (USA) | WOS |  | in both lists |
| R042, R1500 | HFCL B.V. (Netherlands) | WOS |  | in both lists |
| R043, R1501 | Nimpaa Telecommunications Private Limited | JCE |  | in both lists |
| R044, R1502 | BigCat Wireless Private Limited | JCE |  | in both lists |
| R1503 | HFCL Canada Inc. | WOS of HFCL B.V. (step-down) |  | in Note 4 only, not in review-report para 4 list |
| R1504 | HFCL UK Limited | WOS of HFCL B.V. (step-down) |  | in Note 4 only, not in review-report para 4 list |
| R1505 | HFCL Pty Limited (Australia) | WOS of HFCL B.V. (step-down), LIQUIDATED 19 Aug 2026 | ENTITY_CHANGE (liquidated/deregistered w.e.f. 19 Aug 2026; Note 4(o) R1455, R1485) | in Note 4 only, not in review-report para 4 list |

## 4. NOTES
| ROW_ID | note | A2 flags | cross-ref |
|---|---|---|---|
| R121, R1447 | Note 1: Audit Committee review / Board approval 19 Oct 2026 |  | text-layer rows restate image rows where both present: RESTATED |
| R122, R1448 | Note 2: Ind AS compliance |  | text-layer rows restate image rows where both present: RESTATED |
| R1449, R1459-R1469, R1507 | Note 3(i): QIP: shares, price, utilisation, FD, monitoring account |  | text-layer rows restate image rows where both present: RESTATED |
| R131, R136-R137, R1450, R1470-R1480, R1482-R1484, R1490 | Note 3(ii): Warrants to promoter/promoter group | FORWARD (R1490 balance 75% within 18 months) | text-layer rows restate image rows where both present: RESTATED |
| R1491-R1504 | Note 4: Consolidation entity list (15 entities incl parent, see entities table) |  | text-layer rows restate image rows where both present: RESTATED |
| R1455, R1485, R1505 | Note 4(o): HFCL Pty step-down subsidiary liquidated 19 Aug 2026 | ENTITY_CHANGE | text-layer rows restate image rows where both present: RESTATED |
| R159, R1451 | Note 5: EPS not annualised |  | text-layer rows restate image rows where both present: RESTATED |
| R160, R1452 | Note 6: Regrouping of previous period figures |  | text-layer rows restate image rows where both present: RESTATED |
| R200, R1453 | Cash flow note 1: Indirect method Ind AS 7 |  | text-layer rows restate image rows where both present: RESTATED |
| R201, R1454 | Cash flow note 2: Brackets = outflow |  | text-layer rows restate image rows where both present: RESTATED |
| R173-R175, R199, R202, R1456-R1458, R1481, R1486-R1489, R1506 | statement metadata: unit statements, column status, periods, place/date, MD DIN 00052898 and signatory Mahendra Nahata, segment-structure descriptor | | |

## 5. LINE ITEMS (financial tables, page-image rows R371-R1446)
Cell grid: P&L and segment 12 cells/item (Q2FY27, Q1FY27, Q2FY26, H1FY27, H1FY26, FY26 x standalone, consolidated); BS and CF 4 cells/item (2 periods x 2 bases).
| ROW_ID range | table | line item | cells | A2 flags | note |
|---|---|---|---|---|---|
| R371-R382 | P&L | Revenue from Operations | 12 |  |  |
| R383-R394 | P&L | Other Income | 12 |  |  |
| R395-R406 | P&L | Total Income | 12 |  |  |
| R407-R418 | P&L | Cost of materials/services consumed | 12 |  |  |
| R419-R430 | P&L | Purchases of stock-in-trade | 12 |  |  |
| R431-R442 | P&L | Change in inventories of finished goods, WIP and stock-in-trade | 12 |  |  |
| R443-R454 | P&L | Employee benefits expense | 12 |  |  |
| R455-R466 | P&L | Finance costs | 12 |  |  |
| R467-R478 | P&L | Depreciation, Impairment and Amortisation expenses | 12 |  |  |
| R479-R490 | P&L | Other expenses | 12 |  |  |
| R491-R502 | P&L | Total Expenses | 12 |  |  |
| R503-R514 | P&L | III Profit/(Loss) before exceptional items and tax (I-II) | 12 |  |  |
| R515-R526 | P&L | IV Share of net profits/(loss) of jointly controlled entities (equity  | 12 | ZERO_STANDING (6 of 12 cells: R515-R520) |  |
| R527-R538 | P&L | V Profit/(Loss) before exceptional items and tax (III+IV) | 12 |  |  |
| R539-R550 | P&L | VI Exceptional items | 12 | ZERO_STANDING (all periods) |  |
| R551-R562 | P&L | VII Profit/(Loss) before tax (V-VI) | 12 |  |  |
| R563-R574 | P&L | VIII Tax expense - Current Tax | 12 | ZERO_STANDING (2 of 12 cells: R565, R567) |  |
| R575-R586 | P&L | VIII Tax expense - Deferred Tax/(Benefits) | 12 |  |  |
| R587-R598 | P&L | IX Profit/(Loss) after tax from continuing operations (VII-VIII) | 12 |  |  |
| R599-R610 | P&L | X OCI - Items that will not be reclassified to profit or loss | 12 |  |  |
| R611-R622 | P&L | X OCI - Income tax on above item | 12 |  |  |
| R623-R634 | P&L | X OCI - Items that will be reclassified to profit or loss | 12 |  |  |
| R635-R646 | P&L | X Other comprehensive income/(loss) for the period/year after tax | 12 |  |  |
| R647-R658 | P&L | XI Total comprehensive income/(loss) for the period/year (IX+X) | 12 |  |  |
| R659-R670 | P&L | XII Profit attributable to Owners of the Parent | 12 | ZERO_STANDING (6 of 12 cells: R659-R664) |  |
| R671-R682 | P&L | XII Profit attributable to Non-controlling interests | 12 | ZERO_STANDING (6 of 12 cells: R671-R676) |  |
| R683-R694 | P&L | XIII Total comprehensive income attributable to Owners of the Parent | 12 | ZERO_STANDING (6 of 12 cells: R683-R688) |  |
| R695-R706 | P&L | XIII Total comprehensive income attributable to Non-controlling intere | 12 | ZERO_STANDING (6 of 12 cells: R695-R700) |  |
| R707-R718 | P&L | XIV Paid-up Equity Share Capital (face value Re 1/- each) | 12 |  |  |
| R719-R730 | P&L | XV Other Equity | 12 | ZERO_STANDING (10 of 12 cells: R719-R723, R725-R729) |  |
| R731-R742 | P&L | XVI Earnings/(Loss) per Share Basic (Re/Rs) | 12 |  |  |
| R743-R754 | P&L | XVI Earnings/(Loss) per Share Diluted (Re/Rs) | 12 |  |  |
| R755-R766 | Segment | 1 Segment Revenue a. Telecom Products | 12 |  |  |
| R767-R778 | Segment | 1 Segment Revenue b. Defence Product & Services | 12 | ZERO_STANDING (1 of 12 cells: R769) |  |
| R779-R790 | Segment | 1 Segment Revenue c. Turnkey Contracts and Services | 12 |  |  |
| R791-R802 | Segment | 1 Segment Revenue d. Others | 12 | ZERO_STANDING (6 of 12 cells: R791-R796) |  |
| R803-R814 | Segment | 1 Revenue from Operations (segment total) | 12 |  |  |
| R815-R826 | Segment | 2 Segment Results Profit/(Loss) before tax and interest a. Telecom Pro | 12 |  |  |
| R827-R838 | Segment | 2 Segment Results b. Defence Product & Services | 12 |  |  |
| R839-R850 | Segment | 2 Segment Results c. Turnkey Contracts and Services | 12 |  |  |
| R851-R862 | Segment | 2 Segment Results d. Others | 12 | ZERO_STANDING (6 of 12 cells: R851-R856) |  |
| R863-R874 | Segment | 2 Segment Results Total | 12 |  |  |
| R875-R886 | Segment | Less: i. Interest | 12 |  |  |
| R887-R898 | Segment | Less: ii. Other un-allocable expenditure net off | 12 |  |  |
| R899-R910 | Segment | Less: iii. Un-allocable income | 12 |  |  |
| R911-R922 | Segment | Total Profit/(Loss) before Tax | 12 |  |  |
| R923-R934 | Segment | 3 Segment Assets a. Telecom Products | 12 |  |  |
| R935-R946 | Segment | 3 Segment Assets b. Defence Product & Services | 12 |  |  |
| R947-R958 | Segment | 3 Segment Assets c. Turnkey Contracts and Services | 12 |  |  |
| R959-R970 | Segment | 3 Segment Assets d. Others | 12 | ZERO_STANDING (6 of 12 cells: R959-R964) |  |
| R971-R982 | Segment | 3 Segment Assets e. Un-allocated | 12 |  |  |
| R983-R994 | Segment | 3 Segment Assets Total | 12 |  |  |
| R995-R1006 | Segment | 4 Segment Liabilities a. Telecom Products | 12 |  |  |
| R1007-R1018 | Segment | 4 Segment Liabilities b. Defence Product & Services | 12 |  |  |
| R1019-R1030 | Segment | 4 Segment Liabilities c. Turnkey Contracts and Services | 12 |  |  |
| R1031-R1042 | Segment | 4 Segment Liabilities d. Others | 12 | ZERO_STANDING (6 of 12 cells: R1031-R1036) |  |
| R1043-R1054 | Segment | 4 Segment Liabilities e. Un-allocated | 12 |  |  |
| R1055-R1066 | Segment | 4 Segment Liabilities Total | 12 |  |  |
| R1067-R1070 | Balance sheet | Non-current Assets (a) Property, Plant and Equipment | 4 |  |  |
| R1071-R1074 | Balance sheet | (b) Capital work-in-progress | 4 |  |  |
| R1075-R1078 | Balance sheet | (c) Right-of-use-assets | 4 |  |  |
| R1079-R1082 | Balance sheet | (d) Goodwill | 4 | ZERO_STANDING (2 of 4 cells: R1079-R1080) |  |
| R1083-R1086 | Balance sheet | (e) Other Intangible assets | 4 |  |  |
| R1087-R1090 | Balance sheet | (f) Intangible assets under development | 4 |  |  |
| R1091-R1094 | Balance sheet | (g) Investment in subsidiaries and joint controlled entities | 4 |  |  |
| R1095-R1098 | Balance sheet | (h)(i) Financial Assets - Investments | 4 |  |  |
| R1099-R1102 | Balance sheet | (h)(ii) Financial Assets - Trade receivables | 4 |  |  |
| R1103-R1106 | Balance sheet | (h)(iii) Financial Assets - Loans | 4 |  |  |
| R1107-R1110 | Balance sheet | (h)(iv) Financial Assets - Others | 4 |  |  |
| R1111-R1114 | Balance sheet | (i) Other non-current assets | 4 |  |  |
| R1115-R1118 | Balance sheet | Non-current assets Sub-total | 4 |  |  |
| R1119-R1122 | Balance sheet | Current Assets (a) Inventories | 4 |  |  |
| R1123-R1126 | Balance sheet | (b)(i) Financial Assets - Investments | 4 |  |  |
| R1127-R1130 | Balance sheet | (b)(ii) Financial Assets - Trade receivables | 4 |  |  |
| R1131-R1134 | Balance sheet | (b)(iii) Cash and cash equivalents | 4 |  |  |
| R1135-R1138 | Balance sheet | (b)(iv) Bank balances other than (iii) above | 4 |  |  |
| R1139-R1142 | Balance sheet | (b)(v) Loans | 4 |  |  |
| R1143-R1146 | Balance sheet | (b)(vi) Others | 4 |  |  |
| R1147-R1150 | Balance sheet | (c) Current Tax Assets (Net) | 4 |  |  |
| R1151-R1154 | Balance sheet | (d) Other current assets | 4 |  |  |
| R1155-R1158 | Balance sheet | Current assets Sub-total | 4 |  |  |
| R1159-R1162 | Balance sheet | Assets classified as held for sale | 4 | ZERO_STANDING (2 of 4 cells: R1161-R1162) |  |
| R1163-R1166 | Balance sheet | Total Assets | 4 |  |  |
| R1167-R1170 | Balance sheet | Equity (a) Equity Share capital | 4 |  |  |
| R1171-R1174 | Balance sheet | (b) Other Equity | 4 |  |  |
| R1175-R1178 | Balance sheet | (c) Non-Controlling interest | 4 | ZERO_STANDING (2 of 4 cells: R1175-R1176) |  |
| R1179-R1182 | Balance sheet | Equity Sub-total | 4 |  |  |
| R1183-R1186 | Balance sheet | Non-current Liabilities (a)(i) Borrowings | 4 |  |  |
| R1187-R1190 | Balance sheet | (a)(ii) Lease liabilities | 4 |  | block position distinguishes non-current from current |
| R1191-R1194 | Balance sheet | (b) Provisions | 4 |  |  |
| R1195-R1198 | Balance sheet | (c) Deferred tax liabilities (net) | 4 |  |  |
| R1199-R1202 | Balance sheet | Non-current liabilities Sub-total | 4 |  |  |
| R1203-R1206 | Balance sheet | Current Liabilities (a)(i) Borrowings | 4 |  |  |
| R1207-R1210 | Balance sheet | (a)(ii) Lease liabilities | 4 |  | block position distinguishes non-current from current |
| R1211-R1214 | Balance sheet | (a)(iii) Operational Buyers' Credit | 4 |  |  |
| R1215-R1218 | Balance sheet | (a)(iv) Trade Payable | 4 |  |  |
| R1219-R1222 | Balance sheet | (a)(v) Other financial liabilities | 4 |  |  |
| R1223-R1226 | Balance sheet | (b) Current Tax liabilities (Net) | 4 |  |  |
| R1227-R1230 | Balance sheet | (c) Other current liabilities | 4 |  |  |
| R1231-R1234 | Balance sheet | (d) Provisions | 4 |  |  |
| R1235-R1238 | Balance sheet | Current liabilities Sub-total | 4 |  |  |
| R1239-R1242 | Balance sheet | Liabilities directly associated with the assets held for sale | 4 | ZERO_STANDING (2 of 4 cells: R1241-R1242) |  |
| R1243-R1246 | Balance sheet | Total Equity and Liabilities | 4 |  |  |
| R1247-R1250 | Cash flow | I Net Profit before taxes and Exceptional items | 4 |  |  |
| R1251-R1254 | Cash flow | Adj: Depreciation, Impairment and Amortization expenses | 4 |  |  |
| R1255-R1258 | Cash flow | Adj: (Gain)/Loss on disposal of property, plant and equipment | 4 |  |  |
| R1259-R1262 | Cash flow | Adj: Financial Guarantee impairment | 4 |  |  |
| R1263-R1266 | Cash flow | Adj: Bad Debts, Warrants forfieted, advances and misc balances written | 4 |  |  |
| R1267-R1270 | Cash flow | Adj: Liquidated Damages recovered on Sales | 4 | ZERO_STANDING (2 of 4 cells: R1268, R1270); value 0.00 not tagged by A1 |  |
| R1271-R1274 | Cash flow | Adj: Unrealised Loss/(gain) on foreign exchange fluctuation | 4 |  |  |
| R1275-R1278 | Cash flow | Adj: (Gain)/Loss on Sale of Investments - Net | 4 |  |  |
| R1279-R1282 | Cash flow | Adj: Share of (profit)/loss of associates | 4 | ZERO_STANDING (2 of 4 cells: R1279-R1280) |  |
| R1283-R1286 | Cash flow | Adj: Dividend and interest income classified as investing cash flows | 4 |  |  |
| R1287-R1290 | Cash flow | Adj: Finance costs (net) | 4 |  |  |
| R1291-R1294 | Cash flow | Operating profit before working capital changes (unlabelled subtotal) | 4 |  | A1 unlabelled subtotal |
| R1295-R1298 | Cash flow | (Increase)/Decrease in Trade and other receivables | 4 |  |  |
| R1299-R1302 | Cash flow | (Increase)/Decrease in Inventories | 4 |  |  |
| R1303-R1306 | Cash flow | Increase/(Decrease) in Trade payables | 4 |  |  |
| R1307-R1310 | Cash flow | (Increase)/Decrease in other financial assets | 4 |  |  |
| R1311-R1314 | Cash flow | Increase/(Decrease) in other financial liabilities | 4 |  |  |
| R1315-R1318 | Cash flow | (Increase)/Decrease in other non-current assets | 4 |  |  |
| R1319-R1322 | Cash flow | (Increase)/Decrease in other current assets | 4 |  |  |
| R1323-R1326 | Cash flow | Increase/(Decrease) in provisions | 4 |  |  |
| R1327-R1330 | Cash flow | Increase/(Decrease) in other non-current liabilities | 4 |  |  |
| R1331-R1334 | Cash flow | Increase/(Decrease) in other current liabilities | 4 |  |  |
| R1335-R1338 | Cash flow | Change in operating assets and liabilities (unlabelled subtotal) | 4 |  | A1 unlabelled subtotal |
| R1339-R1342 | Cash flow | Cash generated from/(used in) operations | 4 |  |  |
| R1343-R1346 | Cash flow | Income taxes paid/refund (net) | 4 |  |  |
| R1347-R1350 | Cash flow | Net cash inflow from/(used in) operating activities | 4 |  |  |
| R1351-R1354 | Cash flow | II Payment for acquisition of subsidiaries & other investments | 4 | ZERO_STANDING (2 of 4 cells: R1351, R1353) |  |
| R1355-R1358 | Cash flow | II Proceeds from sale of Investment | 4 | ZERO_STANDING (2 of 4 cells: R1355, R1357) |  |
| R1359-R1362 | Cash flow | II Payments for property, plant and equipment including CWIP & Capital | 4 |  |  |
| R1363-R1366 | Cash flow | II Payments for Intangible Assets including CWIP | 4 |  |  |
| R1367-R1370 | Cash flow | II Payment for loan to bodies corporate/subsidiaries | 4 |  |  |
| R1371-R1374 | Cash flow | II Proceeds from sale of property, plant and equipment | 4 |  |  |
| R1375-R1378 | Cash flow | II Bank deposits (placed)/matured (net) | 4 |  |  |
| R1379-R1382 | Cash flow | II Dividends received | 4 | ZERO_STANDING (all periods) |  |
| R1383-R1386 | Cash flow | II Interest received | 4 |  |  |
| R1387-R1390 | Cash flow | Net Cash flow from/(used in) investing activities | 4 |  |  |
| R1391-R1394 | Cash flow | III Proceeds from Issue of convertible Warrants | 4 | ZERO_STANDING (2 of 4 cells: R1392, R1394) |  |
| R1395-R1398 | Cash flow | III Proceeds from issues of Share Capital (including security premium) | 4 |  |  |
| R1399-R1402 | Cash flow | III Proceeds from borrowings | 4 |  |  |
| R1403-R1406 | Cash flow | III (Repayment) of borrowings | 4 |  |  |
| R1407-R1410 | Cash flow | III Proceeds/(Repayment) under supplier finance arrangement | 4 |  |  |
| R1411-R1414 | Cash flow | III Repayment of lease liabilities | 4 |  |  |
| R1415-R1418 | Cash flow | Financing subtotal before Less items (unlabelled) | 4 |  | A1 unlabelled subtotal |
| R1419-R1422 | Cash flow | Less: Interest paid under supplier finance arrangement | 4 |  |  |
| R1423-R1426 | Cash flow | Less: Finance Costs paid on other than supplier finance arrangement | 4 |  |  |
| R1427-R1430 | Cash flow | Less: Dividend paid | 4 | ZERO_STANDING (2 of 4 cells: R1427, R1429) |  |
| R1431-R1434 | Cash flow | Net Cash flow from/(used in) financing activities | 4 |  |  |
| R1435-R1438 | Cash flow | IV Net increase/(decrease) in cash & cash equivalents (I+II+III) | 4 |  |  |
| R1439-R1442 | Cash flow | V Cash and cash equivalents at the beginning of the financial year | 4 |  |  |
| R1443-R1446 | Cash flow | VI Cash and cash equivalents at end of the period/year | 4 |  |  |

Press release tables (page 10): line items
| ROW_ID range | line item | cells | A2 flags | cross-ref |
|---|---|---|---|---|
| R274-R278 | PR Q2 table: Revenue | 5 | | RESTATED: filing R377 R378 R379; R225-R228 |
| R279-R283 | PR Q2 table: EBITDA | 5 | | R246-R248 text restate; EBITDA is not a filing line item |
| R284-R288 | PR Q2 table: EBITDA margin | 5 | |  |
| R289-R293 | PR Q2 table: PBT | 5 | | RESTATED: filing R557 (538.60); R229 R252 |
| R294-R298 | PR Q2 table: PBT margin | 5 | |  |
| R299-R303 | PR Q2 table: PAT | 5 | | RESTATED: filing R593 (394.22); R232 R255 |
| R304-R308 | PR Q2 table: PAT margin | 5 | |  |
| R309-R311 | PR H1 table: Revenue | 3 | | filing R380 R381 |
| R312-R314 | PR H1 table: EBITDA | 3 | |  |
| R315-R317 | PR H1 table: EBITDA margin | 3 | |  |
| R318-R320 | PR H1 table: PBT | 3 | | RESTATED: R236 R237 R267 |
| R321-R323 | PR H1 table: PBT margin | 3 | |  |
| R324-R326 | PR H1 table: PAT | 3 | | RESTATED: R239 R240 R268 |
| R327-R329 | PR H1 table: PAT margin | 3 | |  |

## 6. ZERO_STANDING (summary of section 5 plus auditor-report nil rows)
| ROW_ID | item | flag |
|---|---|---|
| R051, R052 | Revenue nil (Q2, H1 FY27) of 3 unreviewed subsidiaries (para 6) | ZERO_STANDING |
| R515-R520 | IV Share of net profits/(loss) of jointly controlled entities (equity  (P&L) | ZERO_STANDING |
| R539-R550 | VI Exceptional items (P&L) | ZERO_STANDING |
| R565, R567 | VIII Tax expense - Current Tax (P&L) | ZERO_STANDING |
| R659-R664 | XII Profit attributable to Owners of the Parent (P&L) | ZERO_STANDING |
| R671-R676 | XII Profit attributable to Non-controlling interests (P&L) | ZERO_STANDING |
| R683-R688 | XIII Total comprehensive income attributable to Owners of the Parent (P&L) | ZERO_STANDING |
| R695-R700 | XIII Total comprehensive income attributable to Non-controlling intere (P&L) | ZERO_STANDING |
| R719-R723, R725-R729 | XV Other Equity (P&L) | ZERO_STANDING |
| R769 | 1 Segment Revenue b. Defence Product & Services (Segment) | ZERO_STANDING |
| R791-R796 | 1 Segment Revenue d. Others (Segment) | ZERO_STANDING |
| R851-R856 | 2 Segment Results d. Others (Segment) | ZERO_STANDING |
| R959-R964 | 3 Segment Assets d. Others (Segment) | ZERO_STANDING |
| R1031-R1036 | 4 Segment Liabilities d. Others (Segment) | ZERO_STANDING |
| R1079-R1080 | (d) Goodwill (Balance sheet) | ZERO_STANDING |
| R1161-R1162 | Assets classified as held for sale (Balance sheet) | ZERO_STANDING |
| R1175-R1176 | (c) Non-Controlling interest (Balance sheet) | ZERO_STANDING |
| R1241-R1242 | Liabilities directly associated with the assets held for sale (Balance sheet) | ZERO_STANDING |
| R1268, R1270 | Adj: Liquidated Damages recovered on Sales (Cash flow) | ZERO_STANDING |
| R1279-R1280 | Adj: Share of (profit)/loss of associates (Cash flow) | ZERO_STANDING |
| R1351, R1353 | II Payment for acquisition of subsidiaries & other investments (Cash flow) | ZERO_STANDING |
| R1355, R1357 | II Proceeds from sale of Investment (Cash flow) | ZERO_STANDING |
| R1379-R1382 | II Dividends received (Cash flow) | ZERO_STANDING |
| R1392, R1394 | III Proceeds from Issue of convertible Warrants (Cash flow) | ZERO_STANDING |
| R1427, R1429 | Less: Dividend paid (Cash flow) | ZERO_STANDING |

## 7. PRESS RELEASE NARRATIVE ROWS (pp9-11, excluding section 5 tables)
| ROW_ID | category | A2 flags | cross-ref |
|---|---|---|---|
| R220-R224, R330-R332, R366-R370 | header / claims / contacts / boilerplate / table-period labels |  | company claims "best-ever", "Profits Rise Over 5x" (R222, R223) |
| R225-R241, R246-R260, R267-R268 | headline and bullet numbers | RESTATED | tie to section 5 PR tables and filing R377 R557 R593 |
| R242, R261-R263, R334 | order book 28,911 (R242) vs "exceeds 28,900" (R261, R334); visibility six to seven years | RESTATED; FORWARD | order book stated at two precisions |
| R264-R266, R337-R339 | FY27 revenue growth guidance at least 80% over FY26, with qualifier | FORWARD; RESTATED | R264 = R337 (body vs MD quote); qualifier R339 |
| R269-R270, R343-R344, R351-R352, R364-R365 | capex ~1,800 crore (OFC, cable, preform); ammunition AP facility; preform MP facility | FORWARD; RESTATED | R269/R270 vs R343/R344 |
| R271-R273, R347-R350 | Defence ~500 crore FY27; Defence and Aerospace growth engine; growth pillars | FORWARD; RESTATED | R271/R272 vs R347/R348 |
| R340-R342 | 10,000 crore revenue by FY29 | FORWARD |  |
| R345-R346 | aerospace business acquisition expected to complete current quarter | FORWARD | counterparty not named in structured rows |
| R243-R245, R333, R335-R336 | demand / conversion / visibility claims | FORWARD |  |
| R353-R363 | products, facilities and R&D centres named |  |  |

## 8. FORWARD-LOOKING ROWS (all A1 FORWARD)
R136, R243-R245, R262, R264, R269, R271, R333, R335-R337, R340, R343, R345, R347, R349-R352, R1490 ; count 21 ; each also referenced in sections 4 and 7. No turn numbers (not a transcript).

## 9. SUPERSEDED ROWS (R082-R219 OCR text-layer on pp5-8, 124 rows)
| ROW_ID | A2 flags | superseded by |
|---|---|---|
| R082 | SUPERSEDED | R371-R754 |
| R083 | SUPERSEDED | R371-R754 |
| R084 | SUPERSEDED | R371-R754 |
| R085 | SUPERSEDED | R371-R754 |
| R086 | SUPERSEDED | R371-R754 |
| R087 | SUPERSEDED | R371-R754 |
| R088 | SUPERSEDED | R371-R754 |
| R089 | SUPERSEDED | R377 |
| R090 | SUPERSEDED | R379 |
| R091 | SUPERSEDED | R380 |
| R092 | SUPERSEDED | R374 |
| R093 | SUPERSEDED | R372 |
| R094 | SUPERSEDED | R375 |
| R095 | SUPERSEDED | R376 |
| R096 | SUPERSEDED | R395 |
| R097 | SUPERSEDED | R396 |
| R098 | SUPERSEDED | R398 |
| R099 | SUPERSEDED | R400 |
| R100 | SUPERSEDED | R401 |
| R101 | SUPERSEDED | R402 |
| R102 | SUPERSEDED | R403 |
| R103 | SUPERSEDED | R404 |
| R104 | SUPERSEDED | R405 |
| R105 | SUPERSEDED | R406 |
| R106 | SUPERSEDED | R503 |
| R107 | SUPERSEDED | R506 |
| R108 | SUPERSEDED | R533 |
| R109 | SUPERSEDED | R536 |
| R110 | SUPERSEDED | R537 |
| R111 | SUPERSEDED | R593 |
| R112 | SUPERSEDED | R647 |
| R113 | SUPERSEDED | R648 |
| R114 | SUPERSEDED | R650 |
| R115 | SUPERSEDED | R653 |
| R116 | SUPERSEDED | R654 |
| R117 | SUPERSEDED | R665 |
| R118 | SUPERSEDED | R707 |
| R119 | SUPERSEDED | R730 |
| R120 | SUPERSEDED | R755-R1507 |
| R123 | SUPERSEDED | R1449 |
| R124 | SUPERSEDED | R1459 |
| R125 | SUPERSEDED | R755-R1507 |
| R126 | SUPERSEDED | R1465 |
| R127 | SUPERSEDED | R1466 |
| R128 | SUPERSEDED | R755-R1507 |
| R129 | SUPERSEDED | R1469 |
| R130 | SUPERSEDED | R755-R1507 |
| R132 | SUPERSEDED | R1470 |
| R133 | SUPERSEDED | R755-R1507 |
| R134 | SUPERSEDED | R755-R1507 |
| R135 | SUPERSEDED | R755-R1507 |
| R138 | SUPERSEDED | R755-R1507 |
| R139 | SUPERSEDED | R1477 |
| R140 | SUPERSEDED | R755-R1507 |
| R141 | SUPERSEDED | R1479 (corrected from R763) |
| R142 | SUPERSEDED | R1491 |
| R143 | SUPERSEDED | R1492 |
| R144 | SUPERSEDED | R1493 |
| R145 | SUPERSEDED | R1494 |
| R146 | SUPERSEDED | R1495 |
| R147 | SUPERSEDED | R1496 |
| R148 | SUPERSEDED | R1497 |
| R149 | SUPERSEDED | R1498 |
| R150 | SUPERSEDED | R755-R1507 |
| R151 | SUPERSEDED | R1500 |
| R152 | SUPERSEDED | R1501 |
| R153 | SUPERSEDED | R1502 |
| R154 | SUPERSEDED | R1503 |
| R155 | SUPERSEDED | R1504 |
| R156 | SUPERSEDED | R1505 |
| R157 | SUPERSEDED | R755-R1507 |
| R158 | SUPERSEDED | R1485 |
| R161 | SUPERSEDED | R1506 |
| R162 | SUPERSEDED | R1486 (corrected from R1485) |
| R163 | SUPERSEDED | R1458 |
| R164 | SUPERSEDED | R779 (holds Turnkey Contracts segment revenue; A1 label "Others" is wrong) |
| R165 | SUPERSEDED | R780 (Turnkey Contracts segment revenue; A1 label "Others" is wrong) |
| R166 | SUPERSEDED | R914 |
| R167 | SUPERSEDED | R920 |
| R168 | SUPERSEDED | R755-R1507 |
| R169 | SUPERSEDED | R1001 |
| R170 | SUPERSEDED | R878 |
| R171 | SUPERSEDED | R884 |
| R172 | SUPERSEDED | R755-R1507 |
| R176 | SUPERSEDED | R1163 |
| R177 | SUPERSEDED | R1164 |
| R178 | SUPERSEDED | R1165 |
| R179 | SUPERSEDED | R1166 |
| R180 | SUPERSEDED | R1167 |
| R181 | SUPERSEDED | R1168 |
| R182 | SUPERSEDED | R1171 |
| R183 | SUPERSEDED | R1172 |
| R184 | SUPERSEDED | R1173 |
| R185 | SUPERSEDED | R1174 |
| R186 | SUPERSEDED | R1179 |
| R187 | SUPERSEDED | R1180 |
| R188 | SUPERSEDED | R1181 |
| R189 | SUPERSEDED | R1182 |
| R190 | SUPERSEDED | R1177 |
| R191 | SUPERSEDED | R1178 |
| R192 | SUPERSEDED | R1067 |
| R193 | SUPERSEDED | R1069 |
| R194 | SUPERSEDED | R1131 |
| R195 | SUPERSEDED | R1133 |
| R196 | SUPERSEDED | R1183 |
| R197 | SUPERSEDED | R1185 |
| R198 | SUPERSEDED | R1205 |
| R203 | SUPERSEDED | R1247 |
| R204 | SUPERSEDED | R1248 |
| R205 | SUPERSEDED | R1249 |
| R206 | SUPERSEDED | R1250 |
| R207 | SUPERSEDED | R1435 |
| R208 | SUPERSEDED | R1436 |
| R209 | SUPERSEDED | R1437 |
| R210 | SUPERSEDED | R1438 |
| R211 | SUPERSEDED | R1439 |
| R212 | SUPERSEDED | R1440 |
| R213 | SUPERSEDED | R1441 |
| R214 | SUPERSEDED | R1442 |
| R215 | SUPERSEDED | R1443 |
| R216 | SUPERSEDED | R1444 |
| R217 | SUPERSEDED | R1445 |
| R218 | SUPERSEDED | R1446 |
| R219 | SUPERSEDED | R1247-R1488 |

Non-superseded rows within R082-R219 (14), covered in sections 4 and 5: R121 R122 R131 R136 R137 R159 R160 R173 R174 R175 R199 R200 R201 R202.

## 10. NOT APPLICABLE
Concall turns, questions, mgmt numbers, slides: 0 (results filing + press release).
