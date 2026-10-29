# A2 COMPLETENESS LEDGER: Sky Gold & Diamonds Ltd (SKYGOLD) results q2fy27
Source: A1 structured extraction R001-R963 (16 pages). No prior-quarter ledger (first run), so ENTITY_CHANGE is judged against filing text only. Rows reference A1 IDs; verbatim values stay in the structured file.

ids_in_structured: 963 | ids_referenced_in_ledger: 963 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes (numbered)   grep_count: 15 (standalone 6 + consolidated 9)  sweep_count: 15   match: yes   (sub-items 5(i),5(ii) and note 6 split rows: 3 extra IDs, R955 R956 R958)
category: line_items         grep_count: 245 (render-read data rows with pipes: 239 in p7-p15 and p16 table body, plus 6 in p16 note 5 tables counted separately)  sweep_count: 245 distinct labels   match: yes
category: line_item_cells    structured number rows R001-R780 = 780 cells   sweep: 780   match: yes
category: zero_standing      line items with nil cells: 33 (53 cells, all flagged ZERO_STANDING in A1)  sweep: 33 (53 cells)  match: yes; plus 5 Annexure A nil items (R911-R915)
category: agenda_items       grep_count: 5 numbered letter items  sweep_count: 7 (5 numbered + QIP Committee authorisation + e-voting cut-off)  match: yes (2 unnumbered rows explained)
category: annexure_items     grep_count: 8 (Annexure A items 1-8)  sweep_count: 8   match: yes (Annexure B = results, enumerated in sections 1,4,5)
category: auditor_paras      grep_count: 12 (standalone 5 + consolidated 7)  sweep_count: 12   match: yes
category: entities           consolidation list 6 (holding + 5 subsidiaries incl step-down) + 2 unnamed other-auditor subs + Purvi (post quarter)  sweep: same  match: yes
category: signature_blocks   grep_count: 5 (letter e-sign, standalone notes, standalone review, consolidated review, consolidated notes)  sweep_count: 5   match: yes
category: board_times        start 12:15 PM, end 12:43 PM IST (R784,R785,R880); signature 12:55:29 IST (R786,R881) after end: no flag
category: id_accountability  structured 963 | ledger 963 | orphans 0 | duplicates 0   match: yes
category: missing_from_structured  0
gate_a2: pass
=== END COUNT TEST ===

## SPECIAL FLAG SUMMARY
- ZERO_STANDING (line items, 33 rows / 53 cells): standalone CF Dividend income (R252-253), Proceeds from sale of investments (R292-293), Investment in subsidiary company (R298-299), Dividend received (R300-301), Proceeds from share warrants (R306-307); consolidated exceptional item (R394-399, 4 nil cells), tax adjustment earlier year (R418-423, 5 nil), OCI items, NCI rows (R496-501, R514-519, R532-537), balance sheet nil cells (R573, R578, R596, R619), consolidated CF acquisition of subsidiary (R705-706), gain on disposal of subsidiary (R659-660), gain on derecognition of lease (R657-658), repayment of loan (R727-728), share capital proceeds (R719-720), warrants (R721-722), cash on acquisition/derecognition of subsidiaries (R737-738, R741-742), security deposits (R715-716). Template signals: subsidiary acquisition and disposal lines exist in the consolidated CF while the quarter shows Purvi Gems acquired after quarter end.
- ZERO_STANDING (annexure): R911-R915 Annexure A items 4-8 Not Applicable.
- ENTITY_CHANGE: R820 issuer rename; R831 MSKA rename; R835 predecessor auditor; R839/R853 Purvi Gems acquired Oct 7 2026; R847/R852/R902 Shri Rishab Gold partnership to Pvt Ltd Aug 22 2026.
- RESTATED: Purvi acquisition (R794,R808,R839,R853,R868,R869,R891,R903,R931,R959); Rs 1,800 Cr ceiling (R783,R789,R856,R867,R905); fraud (R805-R807,R870,R957,R958); DIN (R788,R809,R840); predecessor auditor dates (R884-885,R895-896).
- FOOTNOTE_UNRESOLVED: R815,R816,R963 UDIN legibility; R893,R962 review period OCR date; R949 cash flow footer says "standalone" on consolidated page.
- Not applicable to a results filing: MGMT_ABSENCE, REPEAT_QUESTION, DROPPED_SLIDE. No director profiles, no AR approval, no dividend, no record date, no ESOP, no auditor appointment items in the Board letter (absence enumerated, not filled).

## 1. LINE ITEMS (every financial-table row label; one ledger row per label, ID range covers all period cells)

### STANDALONE P&L (p7) (28 line items)

| ROW_ID range | cells | category | A2 flags | note |
|---|---|---|---|---|
| R001-R006 | 6 | line_item |  | 7 1056 standalone 1 Revenue from operations |
| R007-R012 | 6 | line_item |  | 7 1057 standalone 1 Other income |
| R013-R018 | 6 | line_item |  | 7 1058 standalone 1 Total income |
| R019-R024 | 6 | line_item |  | 7 1059 standalone 2 Cost of raw materials consumed |
| R025-R030 | 6 | line_item |  | 7 1060 standalone 2 Change in inventories of finished goods and work-in-progress |
| R031-R036 | 6 | line_item |  | 7 1061 standalone 2 Employee benefits expense |
| R037-R042 | 6 | line_item |  | 7 1062 standalone 2 Finance costs |
| R043-R048 | 6 | line_item |  | 7 1063 standalone 2 Depreciation and amortization expense |
| R049-R054 | 6 | line_item |  | 7 1064 standalone 2 Other expenses |
| R055-R060 | 6 | line_item |  | 7 1065 standalone 2 Total expenses |
| R061-R066 | 6 | line_item |  | 7 1066 standalone 3 Profit before tax for the period/year (1-2) |
| R067-R072 | 6 | line_item |  | 7 1067 standalone 4 Current tax |
| R073-R078 | 6 | line_item |  | 7 1068 standalone 4 Deferred tax (credit)/charge |
| R079-R084 | 6 | line_item | ZERO_STANDING | 7 1069 standalone 4 Adjustment of tax relating to earlier year | nil cells: R079, R080, R081, R082, R083 |
| R085-R090 | 6 | line_item |  | 7 1070 standalone 4 Total tax expenses |
| R091-R096 | 6 | line_item |  | 7 1071 standalone 5 Profit after tax for the period/year (3-4) |
| R097-R102 | 6 | line_item |  | 7 1072 standalone 6 OCI i. Re-measurement of employee defined benefit plans |
| R103-R108 | 6 | line_item |  | 7 1073 standalone 6 OCI ii. Income tax on (i) above |
| R109-R114 | 6 | line_item |  | 7 1074 standalone 6 OCI (A) not reclassified to profit or loss |
| R115-R120 | 6 | line_item | ZERO_STANDING | 7 1075 standalone 6 OCI i. Fair value of non-trade investments | nil cells: R115 |
| R121-R126 | 6 | line_item | ZERO_STANDING | 7 1076 standalone 6 OCI ii. Income tax on (i) above (reclassifiable) | nil cells: R121 |
| R127-R132 | 6 | line_item | ZERO_STANDING | 7 1077 standalone 6 OCI (B) reclassified to profit or loss | nil cells: R127 |
| R133-R138 | 6 | line_item |  | 7 1078 standalone 6 Other comprehensive income/(loss) net of tax (A)+(B) |
| R139-R144 | 6 | line_item |  | 7 1079 standalone 7 Total comprehensive income for the period/year (5+6) |
| R145-R150 | 6 | line_item |  | 7 1080 standalone 8 Paid up equity share capital (face value of Rs. 10/- each) |
| R151-R151 | 1 | line_item |  | 7 1081 standalone 9 Other equity |
| R152-R157 | 6 | line_item |  | 7 1082 standalone 10 EPS Basic (Rs.) (not annualised for the periods) |
| R158-R163 | 6 | line_item |  | 7 1083 standalone 10 EPS Diluted (Rs.) (not annualised for the periods) |

### STANDALONE BALANCE SHEET (p8) (37 line items)

| ROW_ID range | cells | category | A2 flags | note |
|---|---|---|---|---|
| R164-R165 | 2 | line_item |  | 8 1087 standalone A1 Property, plant and equipment |
| R166-R167 | 2 | line_item |  | 8 1088 standalone A1 Right-of-use asset |
| R168-R169 | 2 | line_item |  | 8 1089 standalone A1 Investment property |
| R170-R171 | 2 | line_item |  | 8 1090 standalone A1 Other intangible assets |
| R172-R173 | 2 | line_item |  | 8 1091 standalone A1 Financial assets i) Investments |
| R174-R175 | 2 | line_item |  | 8 1092 standalone A1 Financial assets ii) Other financial assets |
| R176-R177 | 2 | line_item |  | 8 1093 standalone A1 Deferred tax assets (net) |
| R178-R179 | 2 | line_item |  | 8 1094 standalone A1 Other non-current assets |
| R180-R181 | 2 | line_item |  | 8 1095 standalone A1 Total non-current assets |
| R182-R183 | 2 | line_item |  | 8 1096 standalone A2 Inventories |
| R184-R185 | 2 | line_item |  | 8 1097 standalone A2 Financial assets i) Trade receivables |
| R186-R187 | 2 | line_item |  | 8 1098 standalone A2 Financial assets ii) Cash and cash equivalent |
| R188-R189 | 2 | line_item |  | 8 1099 standalone A2 Financial assets iii) Bank balance other than (ii) above |
| R190-R191 | 2 | line_item |  | 8 1100 standalone A2 Financial assets iv) Loans |
| R192-R193 | 2 | line_item |  | 8 1101 standalone A2 Financial assets v) Other financial assets |
| R194-R195 | 2 | line_item |  | 8 1102 standalone A2 Other current assets |
| R196-R197 | 2 | line_item |  | 8 1103 standalone A2 Total current assets |
| R198-R199 | 2 | line_item |  | 8 1104 standalone A3 Assets classified as held for sale |
| R200-R201 | 2 | line_item |  | 8 1105 standalone A Total assets |
| R202-R203 | 2 | line_item |  | 8 1106 standalone B1 Equity share capital |
| R204-R205 | 2 | line_item |  | 8 1107 standalone B1 Other equity |
| R206-R207 | 2 | line_item |  | 8 1108 standalone B1 Total equity |
| R208-R209 | 2 | line_item |  | 8 1109 standalone B2 Financial liabilities (i) Borrowings |
| R210-R211 | 2 | line_item |  | 8 1110 standalone B2 Financial liabilities (ii) Lease liabilities |
| R212-R213 | 2 | line_item |  | 8 1111 standalone B2 Provisions |
| R214-R215 | 2 | line_item |  | 8 1112 standalone B2 Total non-current liabilities |
| R216-R217 | 2 | line_item |  | 8 1113 standalone B3 Financial liabilities (i) Borrowings |
| R218-R219 | 2 | line_item |  | 8 1114 standalone B3 Financial liabilities (ii) Lease liabilities |
| R220-R221 | 2 | line_item |  | 8 1115 standalone B3 (iii) Trade payables (a) micro enterprises and small enterprises |
| R222-R223 | 2 | line_item |  | 8 1116 standalone B3 (iii) Trade payables (b) creditors other than micro enterprises and small enterprises |
| R224-R225 | 2 | line_item |  | 8 1117 standalone B3 (iv) Other financial liabilities |
| R226-R227 | 2 | line_item |  | 8 1118 standalone B3 Provisions |
| R228-R229 | 2 | line_item |  | 8 1119 standalone B3 Other current liabilities |
| R230-R231 | 2 | line_item |  | 8 1120 standalone B3 Current tax liabilities (net) |
| R232-R233 | 2 | line_item |  | 8 1121 standalone B3 Total current liabilities |
| R234-R235 | 2 | line_item |  | 8 1122 standalone B Total liabilities |
| R236-R237 | 2 | line_item |  | 8 1123 standalone B Total equity and liabilities |

### STANDALONE CASH FLOW (p9) (42 line items)

| ROW_ID range | cells | category | A2 flags | note |
|---|---|---|---|---|
| R238-R239 | 2 | line_item |  | 9 1127 standalone A Profit before tax |
| R240-R241 | 2 | line_item |  | 9 1128 standalone A Depreciation and Amortisation |
| R242-R243 | 2 | line_item |  | 9 1129 standalone A Expense on employee stock option scheme |
| R244-R245 | 2 | line_item |  | 9 1130 standalone A Loss on sale of property, plant and equipment (net) |
| R246-R247 | 2 | line_item |  | 9 1131 standalone A Provision for doubtful debts / Advances |
| R248-R249 | 2 | line_item |  | 9 1132 standalone A Finance costs |
| R250-R251 | 2 | line_item |  | 9 1133 standalone A Interest Income |
| R252-R253 | 2 | line_item | ZERO_STANDING | 9 1134 standalone A Dividend Income | nil cells: R252 |
| R254-R255 | 2 | line_item |  | 9 1135 standalone A Operating profit before working capital changes |
| R256-R257 | 2 | line_item |  | 9 1136 standalone A Increase in trade payables |
| R258-R259 | 2 | line_item |  | 9 1137 standalone A Increase in other current assets |
| R260-R261 | 2 | line_item |  | 9 1138 standalone A (Increase)/decrease in other non current assets |
| R262-R263 | 2 | line_item |  | 9 1139 standalone A Increase in other non-current financial assets |
| R264-R265 | 2 | line_item |  | 9 1140 standalone A Decrease/(increase) in other current financial assets |
| R266-R267 | 2 | line_item |  | 9 1141 standalone A (Decrease)/increase in other current liabilities |
| R268-R269 | 2 | line_item |  | 9 1142 standalone A (Decrease)/increase in other current financial liabilities |
| R270-R271 | 2 | line_item |  | 9 1143 standalone A Increase in long term provisions |
| R272-R273 | 2 | line_item |  | 9 1144 standalone A Increase/(decrease) in short term provisions |
| R274-R275 | 2 | line_item |  | 9 1145 standalone A Increase in loans |
| R276-R277 | 2 | line_item |  | 9 1146 standalone A Increase in inventories |
| R278-R279 | 2 | line_item |  | 9 1147 standalone A Increase in trade receivables |
| R280-R281 | 2 | line_item |  | 9 1148 standalone A Cash generated/(used) from operations |
| R282-R283 | 2 | line_item |  | 9 1149 standalone A Income tax paid (net) |
| R284-R285 | 2 | line_item |  | 9 1150 standalone A Net cash generated/(used) in operating activities (A) |
| R286-R287 | 2 | line_item |  | 9 1151 standalone B Acquisition of property, plant and equipment (including capital advances) |
| R288-R289 | 2 | line_item |  | 9 1152 standalone B Proceeds from sale of property, plant and equipment |
| R290-R291 | 2 | line_item |  | 9 1153 standalone B Acquisition of intangible assets |
| R292-R293 | 2 | line_item | ZERO_STANDING | 9 1154 standalone B Proceeds from sale of investments | nil cells: R293 |
| R294-R295 | 2 | line_item |  | 9 1155 standalone B Investment in fixed deposits including margin money |
| R296-R297 | 2 | line_item |  | 9 1156 standalone B Redemption of fixed deposits including margin money |
| R298-R299 | 2 | line_item | ZERO_STANDING | 9 1157 standalone B Investment in subsidiary company | nil cells: R298 |
| R300-R301 | 2 | line_item | ZERO_STANDING | 9 1158 standalone B Dividend received on investments | nil cells: R300 |
| R302-R303 | 2 | line_item |  | 9 1159 standalone B Interest received on fixed deposits |
| R304-R305 | 2 | line_item |  | 9 1160 standalone B Net cash used in investing activities (B) |
| R306-R307 | 2 | line_item | ZERO_STANDING | 9 1161 standalone C Proceeds from issue of share warrants | nil cells: R306 |
| R308-R309 | 2 | line_item |  | 9 1162 standalone C Proceeds from borrowings received (net) |
| R310-R311 | 2 | line_item |  | 9 1163 standalone C Repayment of principal portion of lease liabilities |
| R312-R313 | 2 | line_item |  | 9 1164 standalone C Interest paid |
| R314-R315 | 2 | line_item |  | 9 1165 standalone C Net cash generated from financing activities (C) |
| R316-R317 | 2 | line_item |  | 9 1166 standalone Net increase in cash and cash equivalents (A+B+C) |
| R318-R319 | 2 | line_item |  | 9 1167 standalone Cash and cash equivalent at the beginning of the period/year |
| R320-R321 | 2 | line_item |  | 9 1168 standalone Cash and cash equivalent at the end of the period/year |

### CONSOLIDATED P&L (p13) (41 line items)

| ROW_ID range | cells | category | A2 flags | note |
|---|---|---|---|---|
| R322-R327 | 6 | line_item |  | 13 1172 consolidated 1 Revenue from operations |
| R328-R333 | 6 | line_item |  | 13 1173 consolidated 1 Other income |
| R334-R339 | 6 | line_item |  | 13 1174 consolidated 1 Total income |
| R340-R345 | 6 | line_item |  | 13 1175 consolidated 2 Cost of raw materials consumed |
| R346-R351 | 6 | line_item |  | 13 1176 consolidated 2 Purchases of stock-in-trade |
| R352-R357 | 6 | line_item |  | 13 1177 consolidated 2 Change in inventories of finished goods, work-in-progress and stock-in-trade |
| R358-R363 | 6 | line_item |  | 13 1178 consolidated 2 Employee benefits expense |
| R364-R369 | 6 | line_item |  | 13 1179 consolidated 2 Finance costs |
| R370-R375 | 6 | line_item |  | 13 1180 consolidated 2 Depreciation and amortization expense |
| R376-R381 | 6 | line_item |  | 13 1181 consolidated 2 Other expenses |
| R382-R387 | 6 | line_item |  | 13 1182 consolidated 2 Total expenses |
| R388-R393 | 6 | line_item |  | 13 1183 consolidated 3 Profit before tax and exceptional item for the period/year (1-2) |
| R394-R399 | 6 | line_item | ZERO_STANDING | 13 1184 consolidated 4 Exceptional income/(expense) (Refer note 6) | nil cells: R395, R396, R398, R399 |
| R400-R405 | 6 | line_item |  | 13 1185 consolidated 5 Profit before tax for the period/year (3+4) |
| R406-R411 | 6 | line_item |  | 13 1186 consolidated 6 Current tax |
| R412-R417 | 6 | line_item |  | 13 1187 consolidated 6 Deferred tax (credit)/charge |
| R418-R423 | 6 | line_item | ZERO_STANDING | 13 1188 consolidated 6 Adjustment of tax relating to earlier year | nil cells: R418, R419, R420, R421, R422 |
| R424-R429 | 6 | line_item |  | 13 1189 consolidated 6 Total tax expenses |
| R430-R435 | 6 | line_item |  | 13 1190 consolidated 7 Profit after tax for the period/year (5-6) |
| R436-R441 | 6 | line_item |  | 13 1191 consolidated 8 OCI i. Re-measurement of employee defined benefit plans |
| R442-R447 | 6 | line_item |  | 13 1192 consolidated 8 OCI ii. Income tax on (i) above |
| R448-R453 | 6 | line_item |  | 13 1193 consolidated 8 OCI (A) not reclassified to profit or loss |
| R454-R459 | 6 | line_item | ZERO_STANDING | 13 1194 consolidated 8 OCI i. Fair value of non-trade investments | nil cells: R454 |
| R460-R465 | 6 | line_item | ZERO_STANDING | 13 1195 consolidated 8 OCI ii. Foreign currency translation difference of foreign operations | nil cells: R462, R464, R465 |
| R466-R471 | 6 | line_item | ZERO_STANDING | 13 1196 consolidated 8 OCI iii. Income tax on (i) above | nil cells: R466 |
| R472-R477 | 6 | line_item |  | 13 1197 consolidated 8 OCI (B) reclassified to profit or loss |
| R478-R483 | 6 | line_item |  | 13 1198 consolidated 8 Other comprehensive income/(loss) net of tax (A)+(B) |
| R484-R489 | 6 | line_item |  | 13 1199 consolidated 9 Total comprehensive income for the period/year (7+8) |
| R490-R495 | 6 | line_item |  | 13 1200 consolidated Profit attributable to: Owners of the Holding Company |
| R496-R501 | 6 | line_item | ZERO_STANDING | 13 1201 consolidated Profit attributable to: Non-controlling interest | nil cells: R498, R500 |
| R502-R507 | 6 | line_item |  | 13 1202 consolidated Profit attributable to: Total |
| R508-R513 | 6 | line_item |  | 13 1203 consolidated OCI attributable to: Owners of the Holding Company |
| R514-R519 | 6 | line_item | ZERO_STANDING | 13 1204 consolidated OCI attributable to: Non-controlling interest | nil cells: R514, R515, R516, R517, R518, R519 |
| R520-R525 | 6 | line_item |  | 13 1205 consolidated OCI attributable to: Total |
| R526-R531 | 6 | line_item |  | 13 1206 consolidated Total comprehensive income attributable to: Owners of the Holding Company |
| R532-R537 | 6 | line_item | ZERO_STANDING | 13 1207 consolidated Total comprehensive income attributable to: Non-controlling interest | nil cells: R534, R536 |
| R538-R543 | 6 | line_item |  | 13 1208 consolidated Total comprehensive income attributable to: Total |
| R544-R549 | 6 | line_item |  | 13 1209 consolidated 10 Paid up equity share capital (face value of Rs. 10/- each) |
| R550-R550 | 1 | line_item |  | 13 1210 consolidated 11 Other equity |
| R551-R556 | 6 | line_item |  | 13 1211 consolidated 12 EPS Basic (Rs.) (not annualised for the periods) |
| R557-R562 | 6 | line_item |  | 13 1212 consolidated 12 EPS Diluted (Rs.) (not annualised for the periods) |

### CONSOLIDATED BALANCE SHEET (p14) (41 line items)

| ROW_ID range | cells | category | A2 flags | note |
|---|---|---|---|---|
| R563-R564 | 2 | line_item |  | 14 1216 consolidated A1 Property, plant and equipment |
| R565-R566 | 2 | line_item |  | 14 1217 consolidated A1 Right-of-use asset |
| R567-R568 | 2 | line_item |  | 14 1218 consolidated A1 Investment property |
| R569-R570 | 2 | line_item |  | 14 1219 consolidated A1 Goodwill |
| R571-R572 | 2 | line_item |  | 14 1220 consolidated A1 Other intangible assets |
| R573-R574 | 2 | line_item | ZERO_STANDING | 14 1221 consolidated A1 Financial assets i) Investments | nil cells: R573 |
| R575-R576 | 2 | line_item |  | 14 1222 consolidated A1 Financial assets ii) Other financial assets |
| R577-R578 | 2 | line_item | ZERO_STANDING | 14 1223 consolidated A1 Deferred tax assets (net) | nil cells: R578 |
| R579-R580 | 2 | line_item |  | 14 1224 consolidated A1 Other non-current assets |
| R581-R582 | 2 | line_item |  | 14 1225 consolidated A1 Total non-current assets |
| R583-R584 | 2 | line_item |  | 14 1226 consolidated A2 Inventories |
| R585-R586 | 2 | line_item |  | 14 1227 consolidated A2 Financial assets i) Trade receivables |
| R587-R588 | 2 | line_item |  | 14 1228 consolidated A2 Financial assets ii) Cash and cash equivalent |
| R589-R590 | 2 | line_item |  | 14 1229 consolidated A2 Financial assets iii) Bank balance other than (ii) above |
| R591-R592 | 2 | line_item |  | 14 1230 consolidated A2 Financial assets iv) Loans |
| R593-R594 | 2 | line_item |  | 14 1231 consolidated A2 Financial assets v) Other financial assets |
| R595-R596 | 2 | line_item | ZERO_STANDING | 14 1232 consolidated A2 Current tax assets (net) | nil cells: R596 |
| R597-R598 | 2 | line_item |  | 14 1233 consolidated A2 Other current assets |
| R599-R600 | 2 | line_item |  | 14 1234 consolidated A2 Total current assets |
| R601-R602 | 2 | line_item |  | 14 1235 consolidated A3 Assets classified as held for sale |
| R603-R604 | 2 | line_item |  | 14 1236 consolidated A Total assets |
| R605-R606 | 2 | line_item |  | 14 1237 consolidated B1 Equity share capital |
| R607-R608 | 2 | line_item |  | 14 1238 consolidated B1 Other equity |
| R609-R610 | 2 | line_item |  | 14 1239 consolidated B1 Non controlling interest |
| R611-R612 | 2 | line_item |  | 14 1240 consolidated B1 Total equity |
| R613-R614 | 2 | line_item |  | 14 1241 consolidated B2 Financial liabilities (i) Borrowings |
| R615-R616 | 2 | line_item |  | 14 1242 consolidated B2 Financial liabilities (ii) Lease liabilities |
| R617-R618 | 2 | line_item |  | 14 1243 consolidated B2 Provisions |
| R619-R620 | 2 | line_item | ZERO_STANDING | 14 1244 consolidated B2 Deferred tax liability (net) | nil cells: R619 |
| R621-R622 | 2 | line_item |  | 14 1245 consolidated B2 Total non-current liabilities |
| R623-R624 | 2 | line_item |  | 14 1246 consolidated B3 Financial liabilities (i) Borrowings |
| R625-R626 | 2 | line_item |  | 14 1247 consolidated B3 Financial liabilities (ii) Lease liabilities |
| R627-R628 | 2 | line_item |  | 14 1248 consolidated B3 (iii) Trade payables (a) micro enterprises and small enterprises |
| R629-R630 | 2 | line_item |  | 14 1249 consolidated B3 (iii) Trade payables (b) creditors other than micro enterprises and small enterprises |
| R631-R632 | 2 | line_item |  | 14 1250 consolidated B3 (iv) Other financial liabilities |
| R633-R634 | 2 | line_item |  | 14 1251 consolidated B3 Provisions |
| R635-R636 | 2 | line_item |  | 14 1252 consolidated B3 Other current liabilities |
| R637-R638 | 2 | line_item |  | 14 1253 consolidated B3 Current tax liabilities (net) |
| R639-R640 | 2 | line_item |  | 14 1254 consolidated B3 Total current liabilities |
| R641-R642 | 2 | line_item |  | 14 1255 consolidated B Total liabilities |
| R643-R644 | 2 | line_item |  | 14 1256 consolidated B Total equity and liabilities |

### CONSOLIDATED CASH FLOW (p15) (50 line items)

| ROW_ID range | cells | category | A2 flags | note |
|---|---|---|---|---|
| R645-R646 | 2 | line_item |  | 15 1260 consolidated A Profit before tax |
| R647-R648 | 2 | line_item |  | 15 1261 consolidated A Depreciation and Amortisation |
| R649-R650 | 2 | line_item |  | 15 1262 consolidated A Expense on employee stock option scheme |
| R651-R652 | 2 | line_item |  | 15 1263 consolidated A Provision for doubtful debts / advances |
| R653-R654 | 2 | line_item |  | 15 1264 consolidated A Loss on sale of property, plant and equipment (net) |
| R655-R656 | 2 | line_item |  | 15 1265 consolidated A Finance costs |
| R657-R658 | 2 | line_item | ZERO_STANDING | 15 1266 consolidated A Gain on derecognition of lease (net) | nil cells: R657 |
| R659-R660 | 2 | line_item | ZERO_STANDING | 15 1267 consolidated A Gain on disposal of subsidiary | nil cells: R659 |
| R661-R662 | 2 | line_item |  | 15 1268 consolidated A Interest income |
| R663-R664 | 2 | line_item | ZERO_STANDING | 15 1269 consolidated A Dividend income | nil cells: R663 |
| R665-R666 | 2 | line_item |  | 15 1270 consolidated A Operating profit before working capital changes |
| R667-R668 | 2 | line_item |  | 15 1271 consolidated A Increase in trade payables |
| R669-R670 | 2 | line_item |  | 15 1272 consolidated A Increase in other current assets |
| R671-R672 | 2 | line_item |  | 15 1273 consolidated A Decrease in other non current assets |
| R673-R674 | 2 | line_item |  | 15 1274 consolidated A Increase in other non current financial assets |
| R675-R676 | 2 | line_item |  | 15 1275 consolidated A Decrease/(increase) in other current financial assets |
| R677-R678 | 2 | line_item |  | 15 1276 consolidated A (Decrease)/increase in other current liabilities |
| R679-R680 | 2 | line_item |  | 15 1277 consolidated A (Decrease)/increase in other current financial liabilities |
| R681-R682 | 2 | line_item |  | 15 1278 consolidated A Increase in long term provisions |
| R683-R684 | 2 | line_item |  | 15 1279 consolidated A Increase in short term provisions |
| R685-R686 | 2 | line_item |  | 15 1280 consolidated A Increase in loans |
| R687-R688 | 2 | line_item |  | 15 1281 consolidated A Increase in inventories |
| R689-R690 | 2 | line_item |  | 15 1282 consolidated A Increase in trade receivables |
| R691-R692 | 2 | line_item |  | 15 1283 consolidated A Cash generated/(used) from operations |
| R693-R694 | 2 | line_item |  | 15 1284 consolidated A Income tax paid (net) |
| R695-R696 | 2 | line_item |  | 15 1285 consolidated A Net cash generated/(used) in operating activities (A) |
| R697-R698 | 2 | line_item |  | 15 1286 consolidated B Acquisition of property, plant and equipment (including capital advances) |
| R699-R700 | 2 | line_item |  | 15 1287 consolidated B Proceeds from sale of property, plant and equipment |
| R701-R702 | 2 | line_item | ZERO_STANDING | 15 1288 consolidated B Proceeds from sale of investments | nil cells: R702 |
| R703-R704 | 2 | line_item |  | 15 1289 consolidated B Acquisition of intangible assets |
| R705-R706 | 2 | line_item | ZERO_STANDING | 15 1290 consolidated B Acquisition of Subsidiary | nil cells: R705 |
| R707-R708 | 2 | line_item |  | 15 1291 consolidated B Investment in fixed deposits including margin money |
| R709-R710 | 2 | line_item |  | 15 1292 consolidated B Redemption of fixed deposits including margin money |
| R711-R712 | 2 | line_item | ZERO_STANDING | 15 1293 consolidated B Dividend received on investments | nil cells: R711 |
| R713-R714 | 2 | line_item |  | 15 1294 consolidated B Interest received on fixed deposits |
| R715-R716 | 2 | line_item | ZERO_STANDING | 15 1295 consolidated B Security Deposits given during the year | nil cells: R715 |
| R717-R718 | 2 | line_item |  | 15 1296 consolidated B Net cash used in investing activities (B) |
| R719-R720 | 2 | line_item | ZERO_STANDING | 15 1297 consolidated C Proceeds from increase in share capital | nil cells: R719 |
| R721-R722 | 2 | line_item | ZERO_STANDING | 15 1298 consolidated C Proceeds from issue of share warrants | nil cells: R721 |
| R723-R724 | 2 | line_item |  | 15 1299 consolidated C Proceeds from borrowings received (Net) |
| R725-R726 | 2 | line_item |  | 15 1300 consolidated C Repayment of principal portion of lease liabilities |
| R727-R728 | 2 | line_item | ZERO_STANDING | 15 1301 consolidated C Repayment of loan | nil cells: R728 |
| R729-R730 | 2 | line_item |  | 15 1302 consolidated C Interest paid |
| R731-R732 | 2 | line_item |  | 15 1303 consolidated C Net cash generated from financing activities (C) |
| R733-R734 | 2 | line_item |  | 15 1304 consolidated Net increase in cash and cash equivalents (A+B+C) |
| R735-R736 | 2 | line_item |  | 15 1305 consolidated Cash and cash equivalent at the beginning of the period/year |
| R737-R738 | 2 | line_item | ZERO_STANDING | 15 1306 consolidated Cash and cash equivalent on acquisition of subsidiaries | nil cells: R737 |
| R739-R740 | 2 | line_item |  | 15 1307 consolidated Exchange difference of foreign currency cash & cash equivalent |
| R741-R742 | 2 | line_item | ZERO_STANDING | 15 1308 consolidated Cash and cash equivalent on derecognition of subsidiary | nil cells: R741 |
| R743-R744 | 2 | line_item |  | 15 1309 consolidated Cash and cash equivalent at the end of the period/year |

### CONSOLIDATED NOTE 5(i) GEOGRAPHIC REVENUE (p16) (3 line items)

| ROW_ID range | cells | category | A2 flags | note |
|---|---|---|---|---|
| R745-R750 | 6 | line_item |  | 16 1313 consolidated Within India |
| R751-R756 | 6 | line_item |  | 16 1314 consolidated Outside India |
| R757-R762 | 6 | line_item |  | 16 1315 consolidated Total |

### CONSOLIDATED NOTE 5(ii) NON-CURRENT OPERATING ASSETS (p16) (3 line items)

| ROW_ID range | cells | category | A2 flags | note |
|---|---|---|---|---|
| R763-R768 | 6 | line_item |  | 16 1319 consolidated non-current operating assets Within India |
| R769-R774 | 6 | line_item |  | 16 1320 consolidated non-current operating assets Outside India |
| R775-R780 | 6 | line_item |  | 16 1321 consolidated non-current operating assets Total |

## 2. BOARD OUTCOME AGENDA ITEMS AND MEETING FACTS

| ROW_ID range | category | A2 flags | note |
|---|---|---|---|
| R823 | agenda_items |  | QIP Committee mandate, tied to agenda item 1 |
| R826-R827 | agenda_items |  | MCA VC circulars; scrutinizer (agenda item 5) |
| R856-R863 | agenda_items |  | Board outcome letter: item 1 fund raise QIP up to Rs 1,800 Cr (R856,R857,R859); QIP Committee (R858); item 3 EOGM (R860); item 4 notice (R861); cut-off (R862); item 5 scrutinizer (R863) |
| R871-R876 | agenda_items |  | letter dates, meeting day, prior intimation, circular date |
| R878-R879 | agenda_items |  | EOGM 18 Nov 2026 11:00 AM; e-voting cut-off 11 Nov 2026 |
| R880 | agenda_items |  | Board meeting 12:15-12:43 PM IST, 28 minutes; see R784-785 |
| R905 | agenda_items | RESTATED | qualifier on item 1 (conditions of fund raise); restates R856,R857 |
| R906-R907 | agenda_items |  | item 2 results unaudited; limited review report in Annexure B |
| R908 | agenda_items |  | e-voting entitlement basis |

## 3. ANNEXURE A TABLE (items 1-8) AND RELATED

| ROW_ID range | category | A2 flags | note |
|---|---|---|---|
| R789 | annexure | RESTATED | Annexure A item 3 max amount; also R783, R856, R867 |
| R829-R830 | annexure |  | QIP mode; ICDR 2018 |
| R864-R867 | annexure |  | Annexure A items 1-3 (securities, issuance mode, max amount) |
| R882 | annexure |  | circular date, Annexure A heading |
| R909-R910 | annexure |  | approx amount; premium inclusive |
| R911-R915 | annexure | ZERO_STANDING | Annexure A items 4-8 Not Applicable (nil disclosures) |

## 4. NOTES (standalone 1-6, consolidated 1-9 incl 5(i),5(ii)) AND TABLE FOOTNOTES

| ROW_ID range | category | A2 flags | note |
|---|---|---|---|
| R794 | notes | RESTATED | Purvi Gems share capital (standalone note 4); also R808 |
| R805-R807 | notes | RESTATED | consolidated note 6 fraud amounts 1,070.00 / recovered 334.51 / exceptional 735.49 lakhs; see R957,R958,R870 |
| R808 | notes | RESTATED | Purvi Gems acquisition (cons note 7); see R794 |
| R810 | notes |  | standalone note 3 standard reference (Ind AS 108) |
| R868-R869 | notes | RESTATED | Purvi acquisition completed event; see R794,R808,R931,R959 |
| R870 | notes |  | fraud recovery pending on balance; see R957,R958 |
| R921-R926 | notes |  | table unit and status footnotes (standalone P&L, BS, CF) |
| R927 | notes |  | cash flow method footnote, standalone |
| R928-R933 | notes |  | standalone notes 1-6 |
| R943-R948 | notes |  | table unit and status footnotes (consolidated P&L, BS, CF) |
| R949 | notes | FOOTNOTE_UNRESOLVED | cons CF footer reads 'standalone' |
| R950-R961 | notes |  | consolidated notes 1-9 incl 5(i), 5(ii); note 6 split R957/R958 |

## 5. AUDITOR REPORT PARAGRAPHS

| ROW_ID range | category | A2 flags | note |
|---|---|---|---|
| R795-R802 | auditor_paras |  | consolidated para 6: two unreviewed subsidiaries financials (other auditors); entities unnamed |
| R811-R814 | auditor_paras |  | standards/section cited in review paras |
| R884-R885 | auditor_paras |  | standalone para 5: predecessor auditor comparatives and report dates |
| R894 | auditor_paras |  | para 6 subsidiaries total assets date |
| R895-R896 | auditor_paras | RESTATED | consolidated para 7 predecessor dates; same as R884-885 |
| R916-R920 | auditor_paras |  | standalone review report paras 1-5; unmodified limited review conclusion; no EoM; no going concern language; para 5 predecessor reliance (not modified) |
| R934-R942 | auditor_paras |  | consolidated review report paras 1-7; para 6 other auditors reliance; para 7 predecessor; conclusion unmodified |
| R962-R963 | auditor_paras | FOOTNOTE_UNRESOLVED | A1 discrepancy / UDIN legibility notes |

## 5b. AUDITOR IDENTITY, REGISTRATION, UDIN

| ROW_ID range | category | A2 flags | note |
|---|---|---|---|
| R790-R793 | auditor |  | MSKA LLPIN, phone, ICAI FRN, membership no. |
| R803-R804 | auditor |  | MSKA FRN, membership no. (consolidated report) |
| R815-R816 | auditor | FOOTNOTE_UNRESOLVED | UDINs handwritten, legibility uncertain; see R963 |
| R831-R834 | auditor | ENTITY_CHANGE | MSKA & Associates LLP (renamed); address; FRN; signing partner |
| R835 | auditor | ENTITY_CHANGE | predecessor auditor unnamed; auditor transition, comparatives reviewed by predecessor |
| R841 | auditor |  | MSKA address, consolidated report |

## 6. CONSOLIDATION ENTITIES AND ENTITY EVENTS

| ROW_ID range | category | A2 flags | note |
|---|---|---|---|
| R839 | entities | ENTITY_CHANGE | Purvi Gems acquired Oct 7 2026, post-quarter, not consolidated this quarter; see R853 |
| R842 | entities |  | consolidation group (holding + subsidiaries) |
| R843-R846 | entities |  | wholly owned subsidiary (consolidation list) |
| R847 | entities | ENTITY_CHANGE | step-down sub; formerly Shri Rishab Gold partnership firm, now Pvt Ltd w.e.f. Aug 22 2026; see R852,R953 |
| R848 | entities |  | two subsidiaries reviewed by other auditors; unnamed |
| R850-R851 | entities |  | fraud-hit subsidiary; Cyber Police |
| R852 | entities | ENTITY_CHANGE | Shri Rishab Gold conversion |
| R853 | entities | ENTITY_CHANGE | Purvi Gems acquired 100%, post quarter-end; restates R839 |

## 6b. OTHER ENTITIES (addressees, regulators, issuer details)

| ROW_ID range | category | A2 flags | note |
|---|---|---|---|
| R817-R818 | entities_other |  | exchange addressees |
| R819 | entities_other |  | NSE trading symbol |
| R820 | entities_other | ENTITY_CHANGE | issuer renamed Sky Gold Limited to Sky Gold and Diamonds Limited; see R831 (MSKA renamed too) |
| R822 | entities_other |  | SEBI |
| R824-R825 | entities_other |  | Statutory Auditor; Audit Committee |
| R828 | entities_other |  | place of signing |
| R836-R838 | entities_other |  | issuer CIN, office, contact |
| R854-R855 | entities_other |  | geography; websites |

## 7. SIGNATURE BLOCKS, DINs, SIGNING DATES

| ROW_ID range | category | A2 flags | note |
|---|---|---|---|
| R788 | signatures | RESTATED | Mangesh Chauhan DIN; also R809, R840 |
| R809 | signatures | RESTATED | DIN, consolidated notes signature |
| R821 | signatures |  | Board outcome letter signatory, MD |
| R840 | signatures | RESTATED | standalone results signatory |
| R849 | signatures |  | consolidated review signing partner |
| R881 | signatures |  | letter digital signature 2026.10.27, timestamp 12:55:29 IST after meeting end 12:43: no flag; see R786 |
| R886 | signatures |  | standalone review report date |
| R892 | signatures |  | standalone notes signing date |
| R897 | signatures |  | consolidated review report date |
| R904 | signatures |  | consolidated notes signing date |

## 8. PERIOD / DATE REFERENCES

| ROW_ID range | category | A2 flags | note |
|---|---|---|---|
| R877 | dates |  | results period |
| R883 | dates |  | standalone review period |
| R887-R889 | dates |  | standalone column periods |
| R890 | dates |  | Board approval of standalone results |
| R891 | dates | RESTATED | Purvi completion; also R903 |
| R893 | dates | FOOTNOTE_UNRESOLVED | consolidated review period; OCR text layer said Sept 20, render says Sept 30; see R962 |
| R898-R900 | dates |  | consolidated column periods |
| R901 | dates |  | Board approval date, consolidated |
| R902 | dates | ENTITY_CHANGE | Shri Rishab Gold conversion date |
| R903 | dates | RESTATED | Purvi acquisition completed |

## 9. LETTER NUMERICS (scrip code, circular no, ceiling, times)

| ROW_ID range | category | A2 flags | note |
|---|---|---|---|
| R781-R787 | meta_numerics |  | BSE scrip code, SEBI circular no., QIP ceiling, board start/end time, letter signature timestamp, EOGM start |
