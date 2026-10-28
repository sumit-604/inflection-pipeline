# LEDGER: results | SONACOMS | q2fy27 (A2 enumerator)

=== A2 COUNT TEST ===
ids_in_structured: 1098 | ids_referenced_in_ledger: 1098 | orphan_ids: [] | match: yes
category: notes_numbered  grep_count: 13 (fulltext l.302-321 SA 7; l.635-653 CO 6)  sweep_count: 13  match: yes
category: notes_incl_4a_4b  grep_count: 15  sweep_count: 15  match: yes
category: footnotes_unnumbered  grep_count: 3  sweep_count: 3 (R1036,R1084,R1063)  match: yes
category: line_items  grep_count (distinct page+line, NUMBER rows): 249  sweep_count (distinct statement+label): 249  match: yes  [SA P&L 29, SA BS 39, SA CF 49, SA Note3 3, CO P&L 36, CO BS 41, CO CF 49, CO Note3 3]
category: line_item_cells  grep_count: 771  sweep_count: 771  match: yes
category: zero_standing_cells  grep_count: 47  sweep_count: 47  match: yes  (lines: 19)
category: agenda_items  grep_count: 1  sweep_count: 1  match: yes
category: auditor_paras  grep_count: 9 (fulltext l.83-113 SA, l.344-388 CO)  sweep_count: 9  match: yes
category: entities (Annexure 1)  grep_count: 17 (fulltext l.437-458)  sweep_count: 17  match: yes
category: signature_blocks  grep_count: 5  sweep_count: 5  match: yes
gate_a2: pass
=== END COUNT TEST ===

## 1. NOTES (numbered: standalone 1-7, consolidated 1-6; Note 4 has a and b)
| unit | note | structured IDs tagged | flags | materiality |
|---|---|---|---|---|
| Standalone | Note 1 | R366,R367,R861,R952,R953,R954,R1038,R1039 (8) | RESTATED | basis of preparation; Audit Committee 25-Oct, Board 26-Oct; unmodified report |
| Standalone | Note 2 | R368,R862,R955,R956,R957,R1040 (6) | RESTATED | Railway Business of Escorts Kubota acquired 01-Jun-2025, slump sale |
| Standalone | Note 3 | R369,R370,R371,R372,R373,R374,R375,R376,R377,R378,R379,R380,R381,R382,R383,R384,R385,R863,R958,R959,R960,R961,R962,R963,R1041,R1042,R1043,R1044,R1045,R1046,R1047 (31) | ZERO_STANDING BLANK_CELL RESTATED | Exceptional items table (acquisition-opportunity costs, New Labour Codes) |
| Standalone | Note 4a | R386,R387,R864,R964 (4) | RESTATED | ESOP Plan 2023: 1,00,000 options granted 16-Jun-2026 at Rs 596.35 |
| Standalone | Note 4b | R388,R865,R965,R966 (4) | RESTATED | Performance Share Plan 2025: 1,70,747 shares to MD, NRC 05-May-2026 |
| Standalone | Note 5 | R389,R390,R391,R392,R393,R866,R867,R868,R918,R919,R920,R921,R922,R923,R967,R1048,R1049,R1050 (18) | FORWARD RESTATED | DENSO JV agreements 22-Jul-2026; slump sale of EV motors business; 49% at EV Rs 17,500m |
| Standalone | Note 6 | R394,R869,R968 (3) |  | dividend Rs 594.63m from WOS 19-Jun-2026 (standalone) |
| Standalone | Note 7 | R870-R870 (1) |  | single reportable segment |
| Consolidated | Note 1 | R812,R813,R905,R987,R988,R989,R1086,R1087 (8) | RESTATED | basis of preparation; Audit Committee 25-Oct, Board 26-Oct; unmodified report |
| Consolidated | Note 2 | R814,R906,R990,R991,R992,R1088 (6) | RESTATED | Railway Business of Escorts Kubota acquired 01-Jun-2025, slump sale |
| Consolidated | Note 3 | R815,R816,R817,R818,R819,R820,R821,R822,R823,R824,R825,R826,R827,R828,R829,R830,R831,R832,R907,R993,R994,R995,R996,R997,R998,R1089,R1090,R1091,R1092,R1093,R1094,R1095 (32) | ZERO_STANDING RESTATED | Exceptional items table (acquisition-opportunity costs, New Labour Codes) |
| Consolidated | Note 4a | R833,R834,R908,R999 (4) | RESTATED | ESOP Plan 2023: 1,00,000 options granted 16-Jun-2026 at Rs 596.35 |
| Consolidated | Note 4b | R835,R909,R1000,R1001 (4) | RESTATED | Performance Share Plan 2025: 1,70,747 shares to MD, NRC 05-May-2026 |
| Consolidated | Note 5 | R836,R837,R838,R839,R840,R910,R911,R912,R924,R925,R926,R927,R928,R929,R1002,R1096,R1097,R1098 (18) | FORWARD RESTATED | DENSO JV agreements 22-Jul-2026; slump sale of EV motors business; 49% at EV Rs 17,500m |
| Consolidated | Note 6 | R913-R913 (1) |  | single reportable segment (no dividend note in consolidated) |

Unnumbered notes/footnotes: R1036 and R1084 (cash flow indirect method, Ind AS 7); R1063 (* Novelic India incorporated 28-Nov-2025, flag ENTITY_CHANGE); R1023/R1071 (Refer Note No. 3 marker); R1024/R1072 (EPS not annualised); R1025/R1029/R1073/R1077 (see accompanying notes). Counted: 3 footnotes (2 'Note:' + 1 asterisk).

## 2. LINE ITEMS (one row per line; IDs = one per period cell)
| statement | page | line | line item | IDs | cells | A2 flags | note |
|---|---|---|---|---|---|---|---|
| Standalone P&L | 4 | 146 | Revenue from operations | R020-R025 | 6 |  |  |
| Standalone P&L | 4 | 147 | Foreign exchange gain (net) | R026-R031 | 6 |  |  |
| Standalone P&L | 4 | 148 | Other income | R032-R037 | 6 |  |  |
| Standalone P&L | 4 | 149 | Total income | R038-R043 | 6 |  |  |
| Standalone P&L | 4 | 150 | Cost of materials consumed | R044-R049 | 6 |  |  |
| Standalone P&L | 4 | 151 | Changes in inventories of finished goods and work-in-progress | R050-R055 | 6 |  |  |
| Standalone P&L | 4 | 152 | Employee benefits expense | R056-R061 | 6 |  |  |
| Standalone P&L | 4 | 153 | Finance costs | R062-R067 | 6 |  |  |
| Standalone P&L | 4 | 154 | Depreciation and amortisation expense | R068-R073 | 6 |  |  |
| Standalone P&L | 4 | 155 | Other expenses | R074-R079 | 6 |  |  |
| Standalone P&L | 4 | 156 | Total expenses | R080-R085 | 6 |  |  |
| Standalone P&L | 4 | 157 | Profit before exceptional items and tax | R086-R091 | 6 |  |  |
| Standalone P&L | 4 | 158 | Exceptional items (Refer Note No. 3) | R092-R097 | 6 | ZERO_STANDING | nil in 3 of 6 cells (R092,R093,R095) ties to Note 3 |
| Standalone P&L | 4 | 159 | Profit before tax | R098-R103 | 6 |  |  |
| Standalone P&L | 4 | 160 | Tax expense - Current tax | R104-R109 | 6 |  |  |
| Standalone P&L | 4 | 161 | Tax expense - Tax related to previous years | R110-R115 | 6 | ZERO_STANDING | nil in 5 of 6 cells (R110-R114) |
| Standalone P&L | 4 | 162 | Tax expense - Deferred tax (credit)/ charge | R116-R121 | 6 |  |  |
| Standalone P&L | 4 | 163 | Total tax expense | R122-R127 | 6 |  |  |
| Standalone P&L | 4 | 164 | Profit for the period/year | R128-R133 | 6 |  |  |
| Standalone P&L | 4 | 165 | OCI not reclassified - Remeasurements gains/(losses) on defined benefit plans | R134-R139 | 6 |  |  |
| Standalone P&L | 4 | 166 | OCI not reclassified - Income tax relating to above mentioned item | R140-R145 | 6 | ZERO_STANDING | nil in 1 of 6 cells (R141-R141) |
| Standalone P&L | 4 | 167 | OCI reclassified - Effective portion of gain on designated portion of hedging instruments in a cash flow hedge | R146-R151 | 6 |  |  |
| Standalone P&L | 4 | 168 | OCI reclassified - Income tax relating to above mentioned items | R152-R157 | 6 |  |  |
| Standalone P&L | 4 | 169 | Other comprehensive (loss)/ income for the period/ year | R158-R163 | 6 |  |  |
| Standalone P&L | 4 | 170 | Total comprehensive income for the period/ year | R164-R169 | 6 |  |  |
| Standalone P&L | 4 | 171 | Paid up equity share capital (Face value: Rs. 10/- per share) | R170-R175 | 6 |  |  |
| Standalone P&L | 4 | 172 | Total reserves | R177-R177 | 1 |  |  |
| Standalone P&L | 4 | 173 | Earnings per share (Basic) (in Rs) | R178-R183 | 6 |  |  |
| Standalone P&L | 4 | 174 | Earnings per share (Diluted) (in Rs) | R184-R189 | 6 |  |  |
| Standalone Balance Sheet | 5 | 185 | Property, plant and equipment | R190-R191 | 2 |  |  |
| Standalone Balance Sheet | 5 | 186 | Right-of-use assets | R192-R193 | 2 |  |  |
| Standalone Balance Sheet | 5 | 187 | Capital work-in-progress | R194-R195 | 2 |  |  |
| Standalone Balance Sheet | 5 | 188 | Goodwill | R196-R197 | 2 |  |  |
| Standalone Balance Sheet | 5 | 189 | Other intangible assets | R198-R199 | 2 |  |  |
| Standalone Balance Sheet | 5 | 190 | Intangible assets under development | R200-R201 | 2 |  |  |
| Standalone Balance Sheet | 5 | 191 | Non-current financial assets (i) Investments | R202-R203 | 2 |  |  |
| Standalone Balance Sheet | 5 | 192 | Non-current financial assets (ii) Other financial assets | R204-R205 | 2 |  |  |
| Standalone Balance Sheet | 5 | 193 | Income tax assets (net) | R206-R207 | 2 |  |  |
| Standalone Balance Sheet | 5 | 194 | Other non-current assets | R208-R209 | 2 |  |  |
| Standalone Balance Sheet | 5 | 195 | Total non-current assets | R210-R211 | 2 |  |  |
| Standalone Balance Sheet | 5 | 196 | Inventories | R212-R213 | 2 |  |  |
| Standalone Balance Sheet | 5 | 197 | Current financial assets (i) Investments | R214-R215 | 2 |  |  |
| Standalone Balance Sheet | 5 | 198 | Current financial assets (ii) Trade receivables | R216-R217 | 2 |  |  |
| Standalone Balance Sheet | 5 | 199 | Current financial assets (iii) Cash and cash equivalents | R218-R219 | 2 |  |  |
| Standalone Balance Sheet | 5 | 200 | Current financial assets (iv) Bank balances other than (iii) above | R220-R221 | 2 |  |  |
| Standalone Balance Sheet | 5 | 201 | Current financial assets (v) Other financial assets | R222-R223 | 2 |  |  |
| Standalone Balance Sheet | 5 | 202 | Other current assets | R224-R225 | 2 |  |  |
| Standalone Balance Sheet | 5 | 203 | Total current assets | R226-R227 | 2 |  |  |
| Standalone Balance Sheet | 5 | 204 | Total assets | R228-R229 | 2 |  |  |
| Standalone Balance Sheet | 5 | 205 | Equity share capital | R230-R231 | 2 |  |  |
| Standalone Balance Sheet | 5 | 206 | Other equity | R232-R233 | 2 |  |  |
| Standalone Balance Sheet | 5 | 207 | Total equity | R234-R235 | 2 |  |  |
| Standalone Balance Sheet | 5 | 208 | Non-current financial liabilities (i) Lease liabilities | R236-R237 | 2 |  |  |
| Standalone Balance Sheet | 5 | 209 | Non-current financial liabilities (ii) Other financial liabilities | R238-R239 | 2 |  |  |
| Standalone Balance Sheet | 5 | 210 | Non-current provisions | R240-R241 | 2 |  |  |
| Standalone Balance Sheet | 5 | 211 | Deferred tax liabilities (net) | R242-R243 | 2 |  |  |
| Standalone Balance Sheet | 5 | 212 | Total non-current liabilities | R244-R245 | 2 |  |  |
| Standalone Balance Sheet | 5 | 213 | Current financial liabilities (i) Borrowings | R246-R247 | 2 |  |  |
| Standalone Balance Sheet | 5 | 214 | Current financial liabilities (ii) Lease liabilities | R248-R249 | 2 |  |  |
| Standalone Balance Sheet | 5 | 215 | Trade payables - dues of micro enterprises and small enterprises | R250-R251 | 2 |  |  |
| Standalone Balance Sheet | 5 | 216 | Trade payables - dues of creditors other than micro and small enterprises | R252-R253 | 2 |  |  |
| Standalone Balance Sheet | 5 | 217 | Current financial liabilities (iv) Other financial liabilities | R254-R255 | 2 |  |  |
| Standalone Balance Sheet | 5 | 218 | Other current liabilities | R256-R257 | 2 |  |  |
| Standalone Balance Sheet | 5 | 219 | Current provisions | R258-R259 | 2 |  |  |
| Standalone Balance Sheet | 5 | 220 | Current tax liabilities (net) | R260-R261 | 2 |  |  |
| Standalone Balance Sheet | 5 | 221 | Total current liabilities | R262-R263 | 2 |  |  |
| Standalone Balance Sheet | 5 | 222 | Total liabilities | R264-R265 | 2 |  |  |
| Standalone Balance Sheet | 5 | 223 | Total equity and liabilities | R266-R267 | 2 |  |  |
| Standalone Cash Flow | 6 | 234 | A. Profit before income tax | R268-R269 | 2 |  |  |
| Standalone Cash Flow | 6 | 235 | Depreciation and amortisation expense | R270-R271 | 2 |  |  |
| Standalone Cash Flow | 6 | 236 | (Gain)/Loss on sale of property plant and equipment (net) | R272-R273 | 2 |  |  |
| Standalone Cash Flow | 6 | 237 | Allowance for doubtful receivables | R274-R275 | 2 | ZERO_STANDING | nil in 1 of 2 cells (R274-R274) |
| Standalone Cash Flow | 6 | 238 | Share based payments | R276-R277 | 2 |  |  |
| Standalone Cash Flow | 6 | 239 | Unwinding of discount on fair valuation of security deposits and deferred payment liabilities | R278-R279 | 2 |  |  |
| Standalone Cash Flow | 6 | 240 | Provision for slow moving inventory | R280-R281 | 2 |  |  |
| Standalone Cash Flow | 6 | 241 | Fair value (gain)/loss on derivatives | R282-R283 | 2 |  |  |
| Standalone Cash Flow | 6 | 242 | Profit on sale of investments | R284-R285 | 2 |  |  |
| Standalone Cash Flow | 6 | 243 | Dividend income | R286-R287 | 2 | ZERO_STANDING | nil in 1 of 2 cells (R287-R287) |
| Standalone Cash Flow | 6 | 244 | Provision for warranty | R288-R289 | 2 |  |  |
| Standalone Cash Flow | 6 | 245 | Finance costs | R290-R291 | 2 |  |  |
| Standalone Cash Flow | 6 | 246 | Interest income | R292-R293 | 2 |  |  |
| Standalone Cash Flow | 6 | 247 | Unrealised foreign exchange (gain)/loss (net) | R294-R295 | 2 |  |  |
| Standalone Cash Flow | 6 | 248 | Operating profit before working capital changes | R296-R297 | 2 |  |  |
| Standalone Cash Flow | 6 | 249 | Movement in inventories | R298-R299 | 2 |  |  |
| Standalone Cash Flow | 6 | 250 | Movement in trade receivables | R300-R301 | 2 |  |  |
| Standalone Cash Flow | 6 | 251 | Movement in financial assets | R302-R303 | 2 |  |  |
| Standalone Cash Flow | 6 | 252 | Movement in other assets | R304-R305 | 2 |  |  |
| Standalone Cash Flow | 6 | 253 | Movement in trade payables | R306-R307 | 2 |  |  |
| Standalone Cash Flow | 6 | 254 | Movement in financial liabilities | R308-R309 | 2 |  |  |
| Standalone Cash Flow | 6 | 255 | Movement in provisions | R310-R311 | 2 |  |  |
| Standalone Cash Flow | 6 | 256 | Movement in other liabilities | R312-R313 | 2 |  |  |
| Standalone Cash Flow | 6 | 257 | Cash generated from operations | R314-R315 | 2 |  |  |
| Standalone Cash Flow | 6 | 258 | Direct taxes paid | R316-R317 | 2 |  |  |
| Standalone Cash Flow | 6 | 259 | Net cash flow generated from operating activities - Total (A) | R318-R319 | 2 |  |  |
| Standalone Cash Flow | 6 | 260 | B. Payments for acquisition of PPE, intangibles and CWIP incl capital advances/payables | R320-R321 | 2 |  |  |
| Standalone Cash Flow | 6 | 261 | Proceeds from sale of property, plant and equipment | R322-R323 | 2 |  |  |
| Standalone Cash Flow | 6 | 262 | Fixed deposits created during the year | R324-R325 | 2 |  |  |
| Standalone Cash Flow | 6 | 263 | Fixed deposits matured during the year | R326-R327 | 2 |  |  |
| Standalone Cash Flow | 6 | 264 | Sale/(Purchase) of current investment (net) | R328-R329 | 2 |  |  |
| Standalone Cash Flow | 6 | 265 | Purchase of non-current investments | R330-R331 | 2 |  |  |
| Standalone Cash Flow | 6 | 266 | Dividend received | R332-R333 | 2 | ZERO_STANDING | nil in 1 of 2 cells (R333-R333) |
| Standalone Cash Flow | 6 | 267 | Interest received | R334-R335 | 2 |  |  |
| Standalone Cash Flow | 6 | 268 | Net cash (used) in investment activities - Total (B) | R336-R337 | 2 |  |  |
| Standalone Cash Flow (cont) | 7 | 278 | C. Proceeds/(Repayment) from short term borrowings (net) | R338-R339 | 2 |  |  |
| Standalone Cash Flow (cont) | 7 | 279 | Repayment of deferred payment liabilities | R340-R341 | 2 | ZERO_STANDING | nil in 1 of 2 cells (R340-R340) |
| Standalone Cash Flow (cont) | 7 | 280 | Repayment of principal amount of lease liabilities | R342-R343 | 2 |  |  |
| Standalone Cash Flow (cont) | 7 | 281 | Interest paid on lease liabilities | R344-R345 | 2 |  |  |
| Standalone Cash Flow (cont) | 7 | 282 | Dividend paid | R346-R347 | 2 |  |  |
| Standalone Cash Flow (cont) | 7 | 283 | Proceeds from issue of equity shares [including securities premium, (net)] | R348-R349 | 2 |  |  |
| Standalone Cash Flow (cont) | 7 | 284 | Interest paid | R350-R351 | 2 |  |  |
| Standalone Cash Flow (cont) | 7 | 285 | Net cash flow (used in)/generated from financing activities - Total (C) | R352-R353 | 2 |  |  |
| Standalone Cash Flow (cont) | 7 | 286 | D. Net (decrease)/increase in cash and cash equivalents (A)+(B)+(C) | R354-R355 | 2 |  |  |
| Standalone Cash Flow (cont) | 7 | 287 | E. Cash and cash equivalents at the beginning of the year | R356-R357 | 2 |  |  |
| Standalone Cash Flow (cont) | 7 | 288 | F. Cash and cash equivalents at the end of the period (D)+(E) | R358-R359 | 2 |  |  |
| Standalone Cash Flow (cont) | 7 | 289 | Cash comprises - Balances in current accounts | R360-R361 | 2 |  |  |
| Standalone Cash Flow (cont) | 7 | 290 | Cash comprises - Cash on hand | R362-R363 | 2 |  |  |
| Standalone Cash Flow (cont) | 7 | 291 | Balances per statement of cash flows | R364-R365 | 2 |  |  |
| Standalone Note 3 Exceptional Items | 8 | 309 | Costs incurred in relation to various acquisition opportunities | R369-R374 | 6 | ZERO_STANDING | nil in 3 of 6 cells (R369,R370,R372) |
| Standalone Note 3 Exceptional Items | 8 | 310 | Statutory impact of New Labour Codes | R375-R380 | 6 | ZERO_STANDING | nil in 5 of 6 cells (R375-R379) |
| Standalone Note 3 Exceptional Items | 8 | 311 | Total | R381-R385 | 5 | ZERO_STANDING BLANK_CELL | nil in 3 of 5 cells (R381,R382,R384) standalone Note 3 Total has 5 of 6 cells; H1 FY26 total cell blank in source (fulltext l.311), components sum 108.42 (R373) |
| Consolidated P&L | 12 | 470 | Revenue from operations | R420-R425 | 6 |  |  |
| Consolidated P&L | 12 | 471 | Foreign exchange (loss)/gain (net) | R426-R431 | 6 |  |  |
| Consolidated P&L | 12 | 472 | Other income | R432-R437 | 6 |  |  |
| Consolidated P&L | 12 | 473 | Total income | R438-R443 | 6 |  |  |
| Consolidated P&L | 12 | 474 | Cost of materials consumed | R444-R449 | 6 |  |  |
| Consolidated P&L | 12 | 475 | Changes in inventories of finished goods and work-in-progress | R450-R455 | 6 |  |  |
| Consolidated P&L | 12 | 476 | Employee benefits expense | R456-R461 | 6 |  |  |
| Consolidated P&L | 12 | 477 | Finance costs | R462-R467 | 6 |  |  |
| Consolidated P&L | 12 | 478 | Depreciation and amortisation expense | R468-R473 | 6 |  |  |
| Consolidated P&L | 12 | 479 | Other expenses | R474-R479 | 6 |  |  |
| Consolidated P&L | 12 | 480 | Total expenses | R480-R485 | 6 |  |  |
| Consolidated P&L | 12 | 481 | Profit before exceptional items and tax | R486-R491 | 6 |  |  |
| Consolidated P&L | 12 | 482 | Exceptional items (Refer Note No. 3) | R492-R497 | 6 | ZERO_STANDING | nil in 3 of 6 cells (R492,R493,R495) ties to Note 3 |
| Consolidated P&L | 12 | 483 | Profit before tax | R498-R503 | 6 |  |  |
| Consolidated P&L | 12 | 484 | Tax expense - Current tax | R504-R509 | 6 |  |  |
| Consolidated P&L | 12 | 485 | Tax expense - Tax related to previous years | R510-R515 | 6 | ZERO_STANDING | nil in 5 of 6 cells (R510-R514) |
| Consolidated P&L | 12 | 486 | Tax expense - Deferred tax (credit)/ charge | R516-R521 | 6 |  |  |
| Consolidated P&L | 12 | 487 | Total tax expense | R522-R527 | 6 |  |  |
| Consolidated P&L | 12 | 488 | Profit for the period/year | R528-R533 | 6 |  |  |
| Consolidated P&L | 12 | 489 | OCI not reclassified - Remeasurements gains/(losses) on defined benefit plans | R534-R539 | 6 | LOW_LEGIBILITY | H1FY27 cell R537 read 7.05 from blurred cell |
| Consolidated P&L | 12 | 490 | OCI not reclassified - Income tax relating to above mentioned items | R540-R545 | 6 | ZERO_STANDING | nil in 1 of 6 cells (R541-R541) |
| Consolidated P&L | 12 | 491 | OCI reclassified - Exchange differences on translation of foreign operations | R546-R551 | 6 |  |  |
| Consolidated P&L | 12 | 492 | OCI reclassified - Effective portion of gain/(loss) on designated portion of hedging instruments in a cash flow hedge | R552-R557 | 6 |  |  |
| Consolidated P&L | 12 | 493 | OCI reclassified - Income tax relating to above mentioned items | R558-R563 | 6 |  |  |
| Consolidated P&L | 12 | 494 | Other comprehensive income for the period/ year | R564-R569 | 6 |  |  |
| Consolidated P&L | 12 | 495 | Total comprehensive income for the period/ year | R570-R575 | 6 |  |  |
| Consolidated P&L | 12 | 496 | Profit attributable to: a) Owners of the parent | R576-R581 | 6 |  |  |
| Consolidated P&L | 12 | 497 | Profit attributable to: b) Non-controlling interests | R582-R587 | 6 |  |  |
| Consolidated P&L | 12 | 498 | OCI attributable to: a) Owners of the parent | R588-R593 | 6 |  |  |
| Consolidated P&L | 12 | 499 | OCI attributable to: b) Non-controlling interests | R594-R599 | 6 |  |  |
| Consolidated P&L | 12 | 500 | Total comprehensive income attributable to: a) Owners of the parent | R600-R605 | 6 |  |  |
| Consolidated P&L | 12 | 501 | Total comprehensive income attributable to: b) Non-controlling interests | R606-R611 | 6 |  |  |
| Consolidated P&L | 12 | 502 | Paid up equity share capital (Face value: Rs. 10/- per share) | R612-R617 | 6 |  |  |
| Consolidated P&L | 12 | 503 | Total reserves | R619-R619 | 1 |  |  |
| Consolidated P&L | 12 | 504 | Earnings per share (Basic) (in Rs) | R620-R625 | 6 |  |  |
| Consolidated P&L | 12 | 505 | Earnings per share (Diluted) (in Rs) | R626-R631 | 6 |  |  |
| Consolidated Balance Sheet | 13 | 516 | Property, plant and equipment | R632-R633 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 517 | Right-of-use assets | R634-R635 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 518 | Capital work-in-progress | R636-R637 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 519 | Goodwill | R638-R639 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 520 | Other intangible assets | R640-R641 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 521 | Intangible assets under development | R642-R643 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 522 | Non-current financial assets (i) Investments | R644-R645 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 523 | Non-current financial assets (ii) Other financial assets | R646-R647 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 524 | Income tax assets (net) | R648-R649 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 525 | Other non-current assets | R650-R651 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 526 | Total non-current assets | R652-R653 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 527 | Inventories | R654-R655 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 528 | Current financial assets (i) Investments | R656-R657 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 529 | Current financial assets (ii) Trade receivables | R658-R659 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 530 | Current financial assets (iii) Cash and cash equivalents | R660-R661 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 531 | Current financial assets (iv) Bank balances other than (iii) above | R662-R663 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 532 | Current financial assets (v) Other financial assets | R664-R665 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 533 | Other current assets | R666-R667 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 534 | Total current assets | R668-R669 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 535 | Total assets | R670-R671 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 536 | Equity share capital | R672-R673 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 537 | Other equity | R674-R675 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 538 | Non-controlling interest | R676-R677 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 539 | Total equity | R678-R679 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 540 | Non-current financial liabilities (i) Borrowings | R680-R681 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 541 | Non-current financial liabilities (ii) Lease liabilities | R682-R683 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 542 | Non-current financial liabilities (iii) Other financial liabilities | R684-R685 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 543 | Non-current provisions | R686-R687 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 544 | Deferred tax liabilities (net) | R688-R689 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 545 | Total non-current liabilities | R690-R691 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 546 | Current financial liabilities (i) Borrowings | R692-R693 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 547 | Current financial liabilities (ii) Lease liabilities | R694-R695 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 548 | Trade payables - dues of micro enterprises and small enterprises | R696-R697 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 549 | Trade payables - dues of creditors other than micro and small enterprises | R698-R699 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 550 | Current financial liabilities (iv) Other financial liabilities | R700-R701 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 551 | Other current liabilities | R702-R703 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 552 | Current provisions | R704-R705 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 553 | Current tax liabilities (net) | R706-R707 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 554 | Total current liabilities | R708-R709 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 555 | Total liabilities | R710-R711 | 2 |  |  |
| Consolidated Balance Sheet | 13 | 556 | Total equity and liabilities | R712-R713 | 2 |  |  |
| Consolidated Cash Flow | 14 | 567 | A. Profit before income tax | R714-R715 | 2 |  |  |
| Consolidated Cash Flow | 14 | 568 | Depreciation and amortisation expense | R716-R717 | 2 |  |  |
| Consolidated Cash Flow | 14 | 569 | Loss on sale of property plant and equipment (net) | R718-R719 | 2 |  |  |
| Consolidated Cash Flow | 14 | 570 | Allowance for doubtful receivables | R720-R721 | 2 | ZERO_STANDING | nil in 1 of 2 cells (R720-R720) |
| Consolidated Cash Flow | 14 | 571 | Share based payments | R722-R723 | 2 |  |  |
| Consolidated Cash Flow | 14 | 572 | Unwinding of discount on fair valuation of security deposits and deferred payment liabilities | R724-R725 | 2 |  |  |
| Consolidated Cash Flow | 14 | 573 | Provision for slow moving inventory | R726-R727 | 2 |  |  |
| Consolidated Cash Flow | 14 | 574 | Fair value (gain)/loss on derivatives | R728-R729 | 2 |  |  |
| Consolidated Cash Flow | 14 | 575 | Profit on sale of investments | R730-R731 | 2 |  |  |
| Consolidated Cash Flow | 14 | 576 | Provision for warranty | R732-R733 | 2 |  |  |
| Consolidated Cash Flow | 14 | 577 | Finance costs | R734-R735 | 2 |  |  |
| Consolidated Cash Flow | 14 | 578 | Interest income | R736-R737 | 2 |  |  |
| Consolidated Cash Flow | 14 | 579 | Unrealised foreign exchange loss/(gain) (net) | R738-R739 | 2 |  |  |
| Consolidated Cash Flow | 14 | 580 | Operating profit before working capital changes | R740-R741 | 2 |  |  |
| Consolidated Cash Flow | 14 | 581 | Movement in inventories | R742-R743 | 2 |  |  |
| Consolidated Cash Flow | 14 | 582 | Movement in trade receivables | R744-R745 | 2 |  |  |
| Consolidated Cash Flow | 14 | 583 | Movement in financial assets | R746-R747 | 2 |  |  |
| Consolidated Cash Flow | 14 | 584 | Movement in other assets | R748-R749 | 2 |  |  |
| Consolidated Cash Flow | 14 | 585 | Movement in trade payables | R750-R751 | 2 |  |  |
| Consolidated Cash Flow | 14 | 586 | Movement in financial liabilities | R752-R753 | 2 |  |  |
| Consolidated Cash Flow | 14 | 587 | Movement in provisions | R754-R755 | 2 |  |  |
| Consolidated Cash Flow | 14 | 588 | Movement in other liabilities | R756-R757 | 2 |  |  |
| Consolidated Cash Flow | 14 | 589 | Cash generated from operations | R758-R759 | 2 |  |  |
| Consolidated Cash Flow | 14 | 590 | Direct taxes paid | R760-R761 | 2 |  |  |
| Consolidated Cash Flow | 14 | 591 | Net cash flow generated from operating activities - Total (A) | R762-R763 | 2 |  |  |
| Consolidated Cash Flow | 14 | 592 | B. Payments for acquisition of PPE, intangibles and CWIP incl capital advances/payables | R764-R765 | 2 |  |  |
| Consolidated Cash Flow | 14 | 593 | Proceeds from sale of property, plant and equipment | R766-R767 | 2 |  |  |
| Consolidated Cash Flow | 14 | 594 | Fixed deposits created during the year | R768-R769 | 2 |  |  |
| Consolidated Cash Flow | 14 | 595 | Fixed deposits matured during the year | R770-R771 | 2 |  |  |
| Consolidated Cash Flow | 14 | 596 | Sale/(Purchase) of current investment (net) | R772-R773 | 2 |  |  |
| Consolidated Cash Flow | 14 | 597 | Purchase of non-current investments | R774-R775 | 2 | ZERO_STANDING | nil in 1 of 2 cells (R774-R774) |
| Consolidated Cash Flow | 14 | 598 | Interest received | R776-R777 | 2 |  |  |
| Consolidated Cash Flow | 14 | 599 | Net cash (used) in investment activities - Total (B) | R778-R779 | 2 |  |  |
| Consolidated Cash Flow (cont) | 15 | 609 | C. Proceeds/(Repayment) from short term borrowings (net) | R780-R781 | 2 |  |  |
| Consolidated Cash Flow (cont) | 15 | 610 | Repayment of deferred payment liabilities | R782-R783 | 2 | ZERO_STANDING | nil in 1 of 2 cells (R782-R782) |
| Consolidated Cash Flow (cont) | 15 | 611 | Repayment of principal amount of lease liabilities | R784-R785 | 2 |  |  |
| Consolidated Cash Flow (cont) | 15 | 612 | Interest paid on lease liabilities | R786-R787 | 2 |  |  |
| Consolidated Cash Flow (cont) | 15 | 613 | Dividend paid | R788-R789 | 2 |  |  |
| Consolidated Cash Flow (cont) | 15 | 614 | Net proceeds from issue of equity shares [including securities premium (net)] | R790-R791 | 2 |  |  |
| Consolidated Cash Flow (cont) | 15 | 615 | Interest paid | R792-R793 | 2 |  |  |
| Consolidated Cash Flow (cont) | 15 | 616 | Net cash flow generated from/(used in) financing activities - Total (C) | R794-R795 | 2 |  |  |
| Consolidated Cash Flow (cont) | 15 | 617 | D. Net (decrease)/increase in cash and cash equivalents (A)+(B)+(C) | R796-R797 | 2 |  |  |
| Consolidated Cash Flow (cont) | 15 | 618 | E. Cash and cash equivalents at the beginning of the year | R798-R799 | 2 |  |  |
| Consolidated Cash Flow (cont) | 15 | 619 | F. Effect of exchange differences on cash and cash equivalents | R800-R801 | 2 |  |  |
| Consolidated Cash Flow (cont) | 15 | 620 | G. Cash and cash equivalents at the end of the period (D)+(E)+(F) | R802-R803 | 2 |  |  |
| Consolidated Cash Flow (cont) | 15 | 621 | Cash comprises - Balances in current accounts | R804-R805 | 2 |  |  |
| Consolidated Cash Flow (cont) | 15 | 622 | Cash comprises - Cash on hand | R806-R807 | 2 |  |  |
| Consolidated Cash Flow (cont) | 15 | 623 | Cash comprises - Bank deposits with original maturity of less than three months | R808-R809 | 2 |  |  |
| Consolidated Cash Flow (cont) | 15 | 624 | Balances per statement of cash flows | R810-R811 | 2 |  |  |
| Consolidated Note 3 Exceptional Items | 16 | 642 | Costs incurred in relation to various acquisition opportunities | R815-R820 | 6 | ZERO_STANDING | nil in 3 of 6 cells (R815,R816,R818) |
| Consolidated Note 3 Exceptional Items | 16 | 643 | Statutory impact of New Labour Codes | R821-R826 | 6 | ZERO_STANDING | nil in 5 of 6 cells (R821-R825) |
| Consolidated Note 3 Exceptional Items | 16 | 644 | Total | R827-R832 | 6 | ZERO_STANDING | nil in 3 of 6 cells (R827,R828,R830) |

## 3. ZERO_STANDING (every nil/dash cell, grouped by line)
| statement | page | line item | nil cell IDs | nil/total cells | note |
|---|---|---|---|---|---|
| Standalone P&L | 4 | Exceptional items (Refer Note No. 3) | R092,R093,R095 | 3/6 | nil in some periods, nonzero in others |
| Standalone P&L | 4 | Tax expense - Tax related to previous years | R110,R111,R112,R113,R114 | 5/6 | nil in some periods, nonzero in others |
| Standalone P&L | 4 | OCI not reclassified - Income tax relating to above mentioned item | R141 | 1/6 | nil in some periods, nonzero in others |
| Standalone Cash Flow | 6 | Allowance for doubtful receivables | R274 | 1/2 | nil in some periods, nonzero in others |
| Standalone Cash Flow | 6 | Dividend income | R287 | 1/2 | nil in some periods, nonzero in others |
| Standalone Cash Flow | 6 | Dividend received | R333 | 1/2 | nil in some periods, nonzero in others |
| Standalone Cash Flow (cont) | 7 | Repayment of deferred payment liabilities | R340 | 1/2 | nil in some periods, nonzero in others |
| Standalone Note 3 Exceptional Items | 8 | Costs incurred in relation to various acquisition opportunities | R369,R370,R372 | 3/6 | nil in some periods, nonzero in others |
| Standalone Note 3 Exceptional Items | 8 | Statutory impact of New Labour Codes | R375,R376,R377,R378,R379 | 5/6 | nil in some periods, nonzero in others |
| Standalone Note 3 Exceptional Items | 8 | Total | R381,R382,R384 | 3/5 | nil in some periods, nonzero in others |
| Consolidated P&L | 12 | Exceptional items (Refer Note No. 3) | R492,R493,R495 | 3/6 | nil in some periods, nonzero in others |
| Consolidated P&L | 12 | Tax expense - Tax related to previous years | R510,R511,R512,R513,R514 | 5/6 | nil in some periods, nonzero in others |
| Consolidated P&L | 12 | OCI not reclassified - Income tax relating to above mentioned items | R541 | 1/6 | nil in some periods, nonzero in others |
| Consolidated Cash Flow | 14 | Allowance for doubtful receivables | R720 | 1/2 | nil in some periods, nonzero in others |
| Consolidated Cash Flow | 14 | Purchase of non-current investments | R774 | 1/2 | nil in some periods, nonzero in others |
| Consolidated Cash Flow (cont) | 15 | Repayment of deferred payment liabilities | R782 | 1/2 | nil in some periods, nonzero in others |
| Consolidated Note 3 Exceptional Items | 16 | Costs incurred in relation to various acquisition opportunities | R815,R816,R818 | 3/6 | nil in some periods, nonzero in others |
| Consolidated Note 3 Exceptional Items | 16 | Statutory impact of New Labour Codes | R821,R822,R823,R824,R825 | 5/6 | nil in some periods, nonzero in others |
| Consolidated Note 3 Exceptional Items | 16 | Total | R827,R828,R830 | 3/6 | nil in some periods, nonzero in others |
Total nil cells: 47; lines: 19

## 4. BOARD OUTCOME / COVER LETTER (page 1). Agenda items: ONE (approval of unaudited standalone and consolidated results Q2/H1 FY27, Reg 33). No AR, AGM, dividend, director, auditor change, ESOP or fund-raise item. Meeting 2:00 to 4:05 pm (R005,R006,R933,R934).
| ID | type | page | line | A2 flags | cross-ref / note |
|---|---|---|---|---|---|
| R001 | NUMBER | 1 | 27 |  |  |
| R002 | NUMBER | 1 | 29 |  |  |
| R003 | NUMBER | 1 | 30 |  |  |
| R004 | NUMBER | 1 | 40 |  |  |
| R005 | NUMBER | 1 | 49 |  | meeting 2:00 to 4:05 pm = 125 min |
| R006 | NUMBER | 1 | 50 |  | meeting 2:00 to 4:05 pm = 125 min |
| R842 | ENTITY | 1 | 24 |  |  |
| R843 | ENTITY | 1 | 26 |  |  |
| R844 | ENTITY | 1 | 28 |  |  |
| R845 | ENTITY | 1 | 32 |  |  |
| R846 | ENTITY | 1 | 40 |  |  |
| R847 | ENTITY | 1 | 56 |  |  |
| R848 | ENTITY | 1 | 63 | SIGNATURE |  |
| R930 | DATE | 1 | 24 |  |  |
| R931 | DATE | 1 | 36 |  |  |
| R932 | DATE | 1 | 38 |  |  |
| R933 | DATE | 1 | 49 |  |  |
| R934 | DATE | 1 | 50 |  |  |
| R935 | DATE | 1 | 60 | SIGNATURE | cover letter signed 16:58:28 after board end 16:05 (R006) - ok |
| R1004 | QUALIFIER | 1 | 37 |  |  |
| R1005 | QUALIFIER | 1 | 41 |  |  |
| R1006 | QUALIFIER | 1 | 43 |  |  |
| R1007 | QUALIFIER | 1 | 46 |  |  |
| R1008 | QUALIFIER | 1 | 58 | SIGNATURE |  |

## 5. AUDITOR REPORTS (pp 2-3 standalone; 9-10 consolidated). Numbered paras SA 1-4, CO 1-5 (CO para 5 = other-auditor reliance, 5 foreign subs). Both unmodified, no Going Concern, no EoM. UDIN R019 (SA), R418 (CO).
| ID | type | page | line | A2 flags | cross-ref / note |
|---|---|---|---|---|---|
| R007 | NUMBER | 2 | 70 |  |  |
| R008 | NUMBER | 2 | 72 |  |  |
| R009 | NUMBER | 2 | 74 |  |  |
| R010 | NUMBER | 2 | 75 |  |  |
| R011 | NUMBER | 2 | 78 |  |  |
| R012 | NUMBER | 2 | 92 |  |  |
| R013 | NUMBER | 2 | 93 |  |  |
| R014 | NUMBER | 2 | 98 |  |  |
| R015 | NUMBER | 2 | 104 |  |  |
| R016 | NUMBER | 3 | 113 |  |  |
| R017 | NUMBER | 3 | 123 |  |  |
| R018 | NUMBER | 3 | 132 |  |  |
| R019 | NUMBER | 3 | 133 |  |  |
| R396 | NUMBER | 9 | 331 |  |  |
| R397 | NUMBER | 9 | 335 |  |  |
| R398 | NUMBER | 9 | 336 |  |  |
| R399 | NUMBER | 9 | 339 |  |  |
| R400 | NUMBER | 9 | 347 |  |  |
| R401 | NUMBER | 9 | 355 |  |  |
| R402 | NUMBER | 9 | 362 |  |  |
| R403 | NUMBER | 9 | 368 |  |  |
| R404 | NUMBER | 9 | 373 |  |  |
| R405 | NUMBER | 10 | 380 |  |  |
| R406 | NUMBER | 10 | 388 |  |  |
| R407 | NUMBER | 10 | 390 |  |  |
| R408 | NUMBER | 10 | 390 |  |  |
| R409 | NUMBER | 10 | 391 |  |  |
| R410 | NUMBER | 10 | 391 |  |  |
| R411 | NUMBER | 10 | 391 |  |  |
| R412 | NUMBER | 10 | 392 |  |  |
| R413 | NUMBER | 10 | 392 |  |  |
| R414 | NUMBER | 10 | 394 |  |  |
| R415 | NUMBER | 10 | 402 |  |  |
| R416 | NUMBER | 10 | 413 |  |  |
| R417 | NUMBER | 10 | 422 |  |  |
| R418 | NUMBER | 10 | 423 |  |  |
| R849 | ENTITY | 2 | 69 |  |  |
| R850 | ENTITY | 2 | 81 |  |  |
| R851 | ENTITY | 2 | 98 |  |  |
| R852 | ENTITY | 3 | 121 | SIGNATURE |  |
| R853 | ENTITY | 3 | 126 | SIGNATURE |  |
| R854 | ENTITY | 3 | 135 |  |  |
| R875 | ENTITY | 9 | 330 |  |  |
| R876 | ENTITY | 9 | 342 |  |  |
| R877 | ENTITY | 9 | 346 |  |  |
| R878 | ENTITY | 10 | 380 | UNNAMED_ENTITY | which five foreign subs unnamed; total assets R407 |
| R879 | ENTITY | 10 | 411 | SIGNATURE |  |
| R880 | ENTITY | 10 | 416 | SIGNATURE |  |
| R881 | ENTITY | 10 | 425 |  |  |
| R936 | DATE | 2 | 84 |  |  |
| R937 | DATE | 2 | 85 |  |  |
| R938 | DATE | 3 | 128 | SIGNATURE SIGNATURE_BEFORE_BOARD | auditor report signed 13:2x IST before board start 14:00 (R005); Audit Committee met 25 Oct (R953) |
| R939 | DATE | 3 | 136 | SIGNATURE |  |
| R970 | DATE | 9 | 348 |  |  |
| R971 | DATE | 10 | 393 |  |  |
| R972 | DATE | 10 | 418 | SIGNATURE SIGNATURE_BEFORE_BOARD | auditor report signed 13:2x IST before board start 14:00 (R005); Audit Committee met 25 Oct (R953) |
| R973 | DATE | 10 | 426 | SIGNATURE |  |
| R1009 | QUALIFIER | 2 | 77 |  |  |
| R1010 | QUALIFIER | 2 | 90 |  |  |
| R1011 | QUALIFIER | 2 | 96 |  |  |
| R1012 | QUALIFIER | 2 | 103 |  |  |
| R1013 | QUALIFIER | 2 | 106 |  |  |
| R1014 | QUALIFIER | 3 | 113 |  |  |
| R1015 | QUALIFIER | 3 | 125 | SIGNATURE |  |
| R1051 | QUALIFIER | 9 | 338 |  |  |
| R1052 | QUALIFIER | 9 | 367 |  |  |
| R1053 | QUALIFIER | 9 | 372 |  |  |
| R1054 | QUALIFIER | 10 | 381 |  |  |
| R1055 | QUALIFIER | 10 | 388 |  |  |
| R1056 | QUALIFIER | 10 | 389 |  |  |
| R1057 | QUALIFIER | 10 | 390 |  |  |
| R1058 | QUALIFIER | 10 | 400 |  |  |
| R1059 | QUALIFIER | 10 | 408 |  | no modification; no Going Concern or EoM language anywhere in either report |
| R1060 | QUALIFIER | 10 | 415 | SIGNATURE |  |

## 6. CONSOLIDATION LIST (page 11 Annexure 1): 17 entries = holding R882 + 10 WOS R883-R892 + 6 at 54% R893-R898
| ID | type | page | line | A2 flags | cross-ref / note |
|---|---|---|---|---|---|
| R419 | NUMBER | 11 | 451 |  |  |
| R882 | ENTITY | 11 | 437 | NAME_VARIANT | holding co spelt Precisions vs Precision elsewhere (R847) |
| R883 | ENTITY | 11 | 440 |  |  |
| R884 | ENTITY | 11 | 441 |  |  |
| R885 | ENTITY | 11 | 442 |  |  |
| R886 | ENTITY | 11 | 443 |  |  |
| R887 | ENTITY | 11 | 444 |  |  |
| R888 | ENTITY | 11 | 445 |  |  |
| R889 | ENTITY | 11 | 446 |  |  |
| R890 | ENTITY | 11 | 447 |  |  |
| R891 | ENTITY | 11 | 448 |  |  |
| R892 | ENTITY | 11 | 449 |  |  |
| R893 | ENTITY | 11 | 453 |  |  |
| R894 | ENTITY | 11 | 454 |  |  |
| R895 | ENTITY | 11 | 455 |  |  |
| R896 | ENTITY | 11 | 456 |  |  |
| R897 | ENTITY | 11 | 457 |  |  |
| R898 | ENTITY | 11 | 458 | ENTITY_CHANGE | Novelic India incorporated 28-Nov-2025; no prior ledger to diff; confirm new vs Q2 FY26 perimeter |
| R974 | DATE | 11 | 460 | ENTITY_CHANGE | Novelic India incorporated 28-Nov-2025; no prior ledger to diff; confirm new vs Q2 FY26 perimeter |
| R1061 | QUALIFIER | 11 | 432 |  |  |
| R1062 | QUALIFIER | 11 | 451 |  |  |
| R1063 | QUALIFIER | 11 | 460 | ENTITY_CHANGE | Novelic India incorporated 28-Nov-2025; no prior ledger to diff; confirm new vs Q2 FY26 perimeter |

## 7. NOTES PAGES, per-ID (pages 8 and 16)
| ID | type | page | line | A2 flags | cross-ref / note |
|---|---|---|---|---|---|
| R366 | NUMBER | 8 | 303 | RESTATED | restated R812 |
| R367 | NUMBER | 8 | 303 | RESTATED | restated R813 |
| R368 | NUMBER | 8 | 305 | RESTATED | restated R814 |
| R386 | NUMBER | 8 | 313 | RESTATED | restated R833 |
| R387 | NUMBER | 8 | 313 | RESTATED | restated R834 |
| R388 | NUMBER | 8 | 314 | RESTATED | restated R835 |
| R389 | NUMBER | 8 | 316 | RESTATED | restated R836 |
| R390 | NUMBER | 8 | 317 | RESTATED | restated R837 |
| R391 | NUMBER | 8 | 318 | RESTATED | restated R838 |
| R392 | NUMBER | 8 | 319 | RESTATED | restated R839 |
| R393 | NUMBER | 8 | 319 | RESTATED | restated R840; DENSO 49% at EV Rs 17,500m; pending customary conditions (R1048) |
| R394 | NUMBER | 8 | 320 |  | Rs 594.63m dividend from WOS 19-Jun-2026; standalone only (intra-group); relates to Q1 other income R033 817.83 |
| R395 | NUMBER | 8 | 327 | RESTATED | restated R841 |
| R812 | NUMBER | 16 | 636 | RESTATED | restated R366 |
| R813 | NUMBER | 16 | 636 | RESTATED | restated R367 |
| R814 | NUMBER | 16 | 638 | RESTATED | restated R368 |
| R833 | NUMBER | 16 | 646 | RESTATED | restated R386 |
| R834 | NUMBER | 16 | 646 | RESTATED | restated R387 |
| R835 | NUMBER | 16 | 647 | RESTATED | restated R388 |
| R836 | NUMBER | 16 | 649 | RESTATED | restated R389 |
| R837 | NUMBER | 16 | 650 | RESTATED | restated R390 |
| R838 | NUMBER | 16 | 651 | RESTATED | restated R391 |
| R839 | NUMBER | 16 | 652 | RESTATED | restated R392 |
| R840 | NUMBER | 16 | 652 | RESTATED | restated R393 |
| R841 | NUMBER | 16 | 659 | RESTATED | restated R395 |
| R861 | ENTITY | 8 | 303 | RESTATED | restated R905 |
| R862 | ENTITY | 8 | 305 | RESTATED | restated R906 |
| R863 | ENTITY | 8 | 310 | RESTATED | restated R907 |
| R864 | ENTITY | 8 | 313 | RESTATED | restated R908 |
| R865 | ENTITY | 8 | 314 | RESTATED | restated R909 |
| R866 | ENTITY | 8 | 315 | RESTATED | restated R910 |
| R867 | ENTITY | 8 | 316 | RESTATED | restated R911 |
| R868 | ENTITY | 8 | 317 | RESTATED | restated R912 |
| R869 | ENTITY | 8 | 320 | UNNAMED_ENTITY | Rs 594.63m dividend from WOS 19-Jun-2026; standalone only (intra-group); relates to Q1 other income R033 817.83 |
| R870 | ENTITY | 8 | 321 | RESTATED | restated R913 |
| R871 | ENTITY | 8 | 322 | RESTATED | restated R914 |
| R872 | ENTITY | 8 | 323 | RESTATED SIGNATURE | restated R915 |
| R873 | ENTITY | 8 | 325 | RESTATED SIGNATURE | restated R916 |
| R874 | ENTITY | 8 | 328 | RESTATED | restated R917 |
| R905 | ENTITY | 16 | 636 | RESTATED | restated R861 |
| R906 | ENTITY | 16 | 638 | RESTATED | restated R862 |
| R907 | ENTITY | 16 | 643 | RESTATED | restated R863 |
| R908 | ENTITY | 16 | 646 | RESTATED | restated R864 |
| R909 | ENTITY | 16 | 647 | RESTATED | restated R865 |
| R910 | ENTITY | 16 | 648 | RESTATED | restated R866 |
| R911 | ENTITY | 16 | 649 | RESTATED | restated R867 |
| R912 | ENTITY | 16 | 650 | RESTATED | restated R868 |
| R913 | ENTITY | 16 | 653 | RESTATED | restated R870 |
| R914 | ENTITY | 16 | 654 | RESTATED | restated R871 |
| R915 | ENTITY | 16 | 655 | RESTATED SIGNATURE | restated R872 |
| R916 | ENTITY | 16 | 657 | RESTATED SIGNATURE | restated R873 |
| R917 | ENTITY | 16 | 660 | RESTATED | restated R874 |
| R918 | FORWARD | 8 | 315 | RESTATED FORWARD | restated R924 |
| R919 | FORWARD | 8 | 316 | RESTATED FORWARD | restated R925 |
| R920 | FORWARD | 8 | 317 | RESTATED FORWARD | restated R926 |
| R921 | FORWARD | 8 | 318 | RESTATED UNNAMED_ENTITY FORWARD | restated R927 |
| R922 | FORWARD | 8 | 319 | RESTATED FORWARD | restated R928; DENSO 49% at EV Rs 17,500m; pending customary conditions (R1048) |
| R923 | FORWARD | 8 | 319 | RESTATED FORWARD | restated R929 |
| R924 | FORWARD | 16 | 648 | RESTATED FORWARD | restated R918 |
| R925 | FORWARD | 16 | 649 | RESTATED FORWARD | restated R919 |
| R926 | FORWARD | 16 | 650 | RESTATED FORWARD | restated R920 |
| R927 | FORWARD | 16 | 651 | RESTATED UNNAMED_ENTITY FORWARD | restated R921 |
| R928 | FORWARD | 16 | 652 | RESTATED FORWARD | restated R922 |
| R929 | FORWARD | 16 | 652 | RESTATED FORWARD | restated R923 |
| R952 | DATE | 8 | 302 | RESTATED | restated R987 |
| R953 | DATE | 8 | 303 | RESTATED | restated R988 |
| R954 | DATE | 8 | 303 | RESTATED | restated R989 |
| R955 | DATE | 8 | 305 | RESTATED | restated R990 |
| R956 | DATE | 8 | 305 | RESTATED | restated R991 |
| R957 | DATE | 8 | 306 | RESTATED | restated R992 |
| R958 | DATE | 8 | 308 |  |  |
| R959 | DATE | 8 | 308 |  |  |
| R960 | DATE | 8 | 308 |  |  |
| R961 | DATE | 8 | 308 |  |  |
| R962 | DATE | 8 | 308 |  |  |
| R963 | DATE | 8 | 308 |  |  |
| R964 | DATE | 8 | 313 | RESTATED | restated R999 |
| R965 | DATE | 8 | 314 | RESTATED | restated R1000 |
| R966 | DATE | 8 | 314 | RESTATED | restated R1001 |
| R967 | DATE | 8 | 315 | RESTATED | restated R1002 |
| R968 | DATE | 8 | 320 |  | Rs 594.63m dividend from WOS 19-Jun-2026; standalone only (intra-group); relates to Q1 other income R033 817.83 |
| R969 | DATE | 8 | 324 | RESTATED SIGNATURE | restated R1003 |
| R987 | DATE | 16 | 635 | RESTATED | restated R952 |
| R988 | DATE | 16 | 636 | RESTATED | restated R953 |
| R989 | DATE | 16 | 636 | RESTATED | restated R954 |
| R990 | DATE | 16 | 638 | RESTATED | restated R955 |
| R991 | DATE | 16 | 638 | RESTATED | restated R956 |
| R992 | DATE | 16 | 639 | RESTATED | restated R957 |
| R993 | DATE | 16 | 641 |  |  |
| R994 | DATE | 16 | 641 |  |  |
| R995 | DATE | 16 | 641 |  |  |
| R996 | DATE | 16 | 641 |  |  |
| R997 | DATE | 16 | 641 |  |  |
| R998 | DATE | 16 | 641 |  |  |
| R999 | DATE | 16 | 646 | RESTATED | restated R964 |
| R1000 | DATE | 16 | 647 | RESTATED | restated R965 |
| R1001 | DATE | 16 | 647 | RESTATED | restated R966 |
| R1002 | DATE | 16 | 648 | RESTATED | restated R967 |
| R1003 | DATE | 16 | 656 | RESTATED SIGNATURE | restated R969 |
| R1037 | QUALIFIER | 8 | 300 | RESTATED | restated R1085 |
| R1038 | QUALIFIER | 8 | 302 |  |  |
| R1039 | QUALIFIER | 8 | 304 | RESTATED | restated R1087 |
| R1040 | QUALIFIER | 8 | 305 | RESTATED | restated R1088; slump sale basis |
| R1041 | QUALIFIER | 8 | 307 | RESTATED | restated R1089 |
| R1042 | QUALIFIER | 8 | 308 |  |  |
| R1043 | QUALIFIER | 8 | 308 |  |  |
| R1044 | QUALIFIER | 8 | 308 |  |  |
| R1045 | QUALIFIER | 8 | 308 |  |  |
| R1046 | QUALIFIER | 8 | 308 |  |  |
| R1047 | QUALIFIER | 8 | 308 |  |  |
| R1048 | QUALIFIER | 8 | 318 | RESTATED | restated R1096 |
| R1049 | QUALIFIER | 8 | 318 | RESTATED | restated R1097 |
| R1050 | QUALIFIER | 8 | 319 | RESTATED | restated R1098; DENSO 49% at EV Rs 17,500m; pending customary conditions (R1048) |
| R1085 | QUALIFIER | 16 | 633 | RESTATED | restated R1037 |
| R1086 | QUALIFIER | 16 | 635 |  |  |
| R1087 | QUALIFIER | 16 | 637 | RESTATED | restated R1039 |
| R1088 | QUALIFIER | 16 | 638 | RESTATED | restated R1040; slump sale basis |
| R1089 | QUALIFIER | 16 | 640 | RESTATED | restated R1041 |
| R1090 | QUALIFIER | 16 | 641 |  |  |
| R1091 | QUALIFIER | 16 | 641 |  |  |
| R1092 | QUALIFIER | 16 | 641 |  |  |
| R1093 | QUALIFIER | 16 | 641 |  |  |
| R1094 | QUALIFIER | 16 | 641 |  |  |
| R1095 | QUALIFIER | 16 | 641 |  |  |
| R1096 | QUALIFIER | 16 | 651 | RESTATED | restated R1048 |
| R1097 | QUALIFIER | 16 | 651 | RESTATED | restated R1049 |
| R1098 | QUALIFIER | 16 | 652 | RESTATED | restated R1050 |

## 8. TABLE METADATA, per-ID (column periods, status, units, seals, headers; pp 4-7, 12-15)
| ID | type | page | line | A2 flags | cross-ref / note |
|---|---|---|---|---|---|
| R176 | NUMBER | 4 | 171 |  |  |
| R618 | NUMBER | 12 | 502 |  |  |
| R855 | ENTITY | 4 | 141 |  |  |
| R856 | ENTITY | 4 | 176 |  |  |
| R857 | ENTITY | 5 | 225 |  |  |
| R858 | ENTITY | 6 | 269 |  |  |
| R859 | ENTITY | 7 | 292 |  |  |
| R860 | ENTITY | 7 | 293 |  |  |
| R899 | ENTITY | 12 | 465 |  |  |
| R900 | ENTITY | 12 | 507 |  |  |
| R901 | ENTITY | 13 | 558 |  |  |
| R902 | ENTITY | 14 | 600 |  |  |
| R903 | ENTITY | 15 | 625 |  |  |
| R904 | ENTITY | 15 | 626 |  |  |
| R940 | DATE | 4 | 145 |  |  |
| R941 | DATE | 4 | 145 |  |  |
| R942 | DATE | 4 | 145 |  |  |
| R943 | DATE | 4 | 145 |  |  |
| R944 | DATE | 4 | 145 |  |  |
| R945 | DATE | 4 | 145 |  |  |
| R946 | DATE | 5 | 184 |  |  |
| R947 | DATE | 5 | 184 |  |  |
| R948 | DATE | 6 | 233 |  |  |
| R949 | DATE | 6 | 233 |  |  |
| R950 | DATE | 7 | 277 |  |  |
| R951 | DATE | 7 | 277 |  |  |
| R975 | DATE | 12 | 469 |  |  |
| R976 | DATE | 12 | 469 |  |  |
| R977 | DATE | 12 | 469 |  |  |
| R978 | DATE | 12 | 469 |  |  |
| R979 | DATE | 12 | 469 |  |  |
| R980 | DATE | 12 | 469 |  |  |
| R981 | DATE | 13 | 515 |  |  |
| R982 | DATE | 13 | 515 |  |  |
| R983 | DATE | 14 | 566 |  |  |
| R984 | DATE | 14 | 566 |  |  |
| R985 | DATE | 15 | 608 |  |  |
| R986 | DATE | 15 | 608 |  |  |
| R1016 | QUALIFIER | 4 | 144 |  |  |
| R1017 | QUALIFIER | 4 | 145 |  |  |
| R1018 | QUALIFIER | 4 | 145 |  |  |
| R1019 | QUALIFIER | 4 | 145 |  |  |
| R1020 | QUALIFIER | 4 | 145 |  |  |
| R1021 | QUALIFIER | 4 | 145 |  |  |
| R1022 | QUALIFIER | 4 | 145 |  |  |
| R1023 | QUALIFIER | 4 | 158 |  |  |
| R1024 | QUALIFIER | 4 | 173 |  |  |
| R1025 | QUALIFIER | 4 | 175 |  |  |
| R1026 | QUALIFIER | 5 | 183 |  |  |
| R1027 | QUALIFIER | 5 | 184 |  |  |
| R1028 | QUALIFIER | 5 | 184 |  |  |
| R1029 | QUALIFIER | 5 | 224 |  |  |
| R1030 | QUALIFIER | 6 | 232 |  |  |
| R1031 | QUALIFIER | 6 | 233 |  |  |
| R1032 | QUALIFIER | 6 | 233 |  |  |
| R1033 | QUALIFIER | 7 | 276 |  |  |
| R1034 | QUALIFIER | 7 | 277 |  |  |
| R1035 | QUALIFIER | 7 | 277 |  |  |
| R1036 | QUALIFIER | 7 | 292 |  |  |
| R1064 | QUALIFIER | 12 | 468 |  |  |
| R1065 | QUALIFIER | 12 | 469 |  |  |
| R1066 | QUALIFIER | 12 | 469 |  |  |
| R1067 | QUALIFIER | 12 | 469 |  |  |
| R1068 | QUALIFIER | 12 | 469 |  |  |
| R1069 | QUALIFIER | 12 | 469 |  |  |
| R1070 | QUALIFIER | 12 | 469 |  |  |
| R1071 | QUALIFIER | 12 | 482 |  |  |
| R1072 | QUALIFIER | 12 | 504 |  |  |
| R1073 | QUALIFIER | 12 | 506 |  |  |
| R1074 | QUALIFIER | 13 | 514 |  |  |
| R1075 | QUALIFIER | 13 | 515 |  |  |
| R1076 | QUALIFIER | 13 | 515 |  |  |
| R1077 | QUALIFIER | 13 | 557 |  |  |
| R1078 | QUALIFIER | 14 | 565 |  |  |
| R1079 | QUALIFIER | 14 | 566 |  |  |
| R1080 | QUALIFIER | 14 | 566 |  |  |
| R1081 | QUALIFIER | 15 | 607 |  |  |
| R1082 | QUALIFIER | 15 | 608 |  |  |
| R1083 | QUALIFIER | 15 | 608 |  |  |
| R1084 | QUALIFIER | 15 | 625 |  |  |

```yaml
company: "SONACOMS"
quarter: "q2fy27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-sonacoms-q2fy27-c7173c/runs/sonacoms-q2fy27/work/ledger_results_sonacoms_q2fy27.md"
counts:
  notes: 15            # 13 numbered (SA 7, CO 6); 4a/4b split gives 15; plus 3 unnumbered footnotes
  line_items: 249      # SA 120 (P&L 29, BS 39, CF 49, Note3 3), CO 129 (P&L 36, BS 41, CF 49, Note3 3); 771 cells
  zero_standing: 47    # cells, in 19 lines
  agenda_items: 1
  auditor_paras: 9     # SA paras 1-4, CO paras 1-5
  entities: 17         # Annexure 1: holding + 10 WOS + 6 at 54%
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, ENTITY_CHANGE, BLANK_CELL, LOW_LEGIBILITY, SIGNATURE_BEFORE_BOARD, NAME_VARIANT, UNNAMED_ENTITY, RESTATED, FORWARD]
ids_in_structured: 1098
ids_referenced: 1098
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
```
