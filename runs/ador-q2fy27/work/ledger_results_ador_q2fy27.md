# A2 LEDGER: ADOR Q2 FY27 results filing
Source: runs/ador-q2fy27/extracted/ador-results-q2fy27-structured.md (R001-R900). Units INR lakhs. No prior ledger.

=== A2 COUNT TEST ===
category: notes        grep_count: 22   sweep_count: 22   match: yes   (grep: 19 numbered note lines [9 standalone + 10 consol] + 3 lettered sub-notes 3a,3b,4a)
category: line_items   grep_count: 243   sweep_count: 243   match: yes   (238 statement lines + 5 exceptional-table lines: 3 standalone note 3, 2 consol note 4)
category: zero_standing grep_count: 91 cells   sweep_count: 91 cells over 34 line items   match: yes
category: agenda_items grep_count: 3   sweep_count: 3   match: yes   (a results, b LRR, c dividend)
category: auditor_paras grep_count: 12   sweep_count: 12   match: yes   (10 paras/blocks carry A1 rows; consol LRR para 2 mgmt responsibility and para 5 conclusion carry no discrete number/date so no A1 ID; both confirmed present in fulltext lines 373 and 392)
category: entities     grep_count: 26   sweep_count: 26   match: yes
turns/questions/mgmt_numbers/slides/slide_numbers: not applicable (results filing)
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 926 | ids_referenced_in_ledger: 926 | orphan_ids: [] | match: yes

## 1. NOTES (numbered notes and sub-notes; ID carries page/line)

IDs | category | A2 flags | cross-ref / materiality
--- | --- | --- | ---
R393 | note-adjunct | - | Standalone notes heading
R394, R395 | note | - | Standalone note 1
R396 | note | - | Standalone note 2
R397, R398, R399 | note | FY26_COLUMN_ONLY | Standalone note 3 (exceptional items table); values sit only in FY26 column; quarter and half columns dash (ZERO_STANDING, R901-R926) (A1 note p3)
R400, R401, R402 | note | - | Standalone note 3a
R403, R404, R405, R406, R407, R408, R409 | note | RESTATED | Standalone note 3b (Labour Codes); mirrors C4a
R410, R411, R412, R413, R414, R415, R416, R417, R418, R419 | note | FORWARD_LAPSED_TARGET,RESTATED | Standalone note 4 (turnkey project provisions); turnkey target June 2025 is past; commitment language carried forward; mirrors C5
R420, R421, R422, R423, R424, R425 | note | RESTATED | Standalone note 5 (BIS compounding); mirrors C6
R426, R427, R428, R429 | note | RESTATED | Standalone note 6 (Kuwait recovery); mirrors C7
R430, R431 | note | - | Standalone note 7 (segment)
R432, R433, R434, R435, R436, R437, R438 | note | RESTATED | Standalone note 8 (special interim dividend); 7.50 per share; mirrors R015 and C10
R439 | note | - | Standalone note 9 (policies)
R440, R441, R442 | note-adjunct | - | Standalone signature block (MD A. T. Malkani, DIN, date)
R857, R858 | note | - | Consol note 1
R859 | note | - | Consol note 2
R860, R861 | note | - | Consol note 3 (entities)
R862, R863, R864 | note | FY26_COLUMN_ONLY | Consol note 4 (exceptional items table)
R865, R866, R867, R868, R869, R870 | note | RESTATED | Consol note 4a (Labour Codes); mirrors S3b
R871, R872, R873, R874, R875, R876, R877, R878, R879, R880 | note | FORWARD_LAPSED_TARGET,RESTATED | Consol note 5 (turnkey); mirrors S4
R881, R882, R883, R884, R885, R886 | note | RESTATED | Consol note 6 (BIS); mirrors S5
R887, R888, R889, R890 | note | RESTATED | Consol note 7 (Kuwait); mirrors S6
R891 | note | - | Consol note 8 (segment)
R892 | note | - | Consol note 9 (policies)
R893, R894, R895, R896, R897 | note | RESTATED,OCR_CONFLICT | Consol note 10 (special interim dividend); R893 reads 27.50 and R895 reads 210 (OCR glyph); page 1 R015 states 7.50; FV 10 x 75% = 7.50 (R434)
R898, R899, R900 | note-adjunct | - | Consol signature block (MD A. T. Malkani, DIN, date)

## 2. LINE ITEMS (every financial-table line, one row per line; dash cells flagged)

IDs | category | A2 flags | cross-ref / materiality
--- | --- | --- | ---
R043, R044, R045, R046, R047, R048 | line_item Standalone P&L p3 l125: Revenue from operations | - | 6 period cells
R049, R050, R051, R052, R053, R054 | line_item Standalone P&L p3 l126: Other income | - | 6 period cells
R055, R056, R057, R058, R059, R060 | line_item Standalone P&L p3 l127: Total income | - | 6 period cells
R061, R062, R063, R064, R065, R066 | line_item Standalone P&L p3 l129: Cost of materials consumed | - | 6 period cells
R067, R068, R069, R070, R071, R072 | line_item Standalone P&L p3 l130: Purchases of stock-in-trade | - | 6 period cells
R073, R074, R075, R076, R077, R078 | line_item Standalone P&L p3 l131: Changes in inventories of finished goods, work-in-progress,  | - | 6 period cells
R079, R080, R081, R082, R083, R084 | line_item Standalone P&L p3 l133: Employee benefits expense | - | 6 period cells
R085, R086, R087, R088, R089, R090 | line_item Standalone P&L p3 l134: Finance costs | - | 6 period cells
R091, R092, R093, R094, R095, R096 | line_item Standalone P&L p3 l135: Depreciation and amortisation expense | - | 6 period cells
R097, R098, R099, R100, R101, R102, R103 | line_item Standalone P&L p3 l136: Onerous cost and Liquidated Damages (refer note 4) | ZERO_STANDING | 6 period cells, 4 dash cells; carries refer-note qualifier
R104, R105, R106, R107, R108, R109, R110 | line_item Standalone P&L p3 l137: Impairment reversal on trade receivables (refer note 6) | ZERO_STANDING | 6 period cells, 5 dash cells; carries refer-note qualifier
R111, R112, R113, R114, R115, R116 | line_item Standalone P&L p3 l138: Other expenses | - | 6 period cells
R117, R118, R119, R120, R121, R122 | line_item Standalone P&L p3 l139: Total expenses | - | 6 period cells
R123, R124, R125, R126, R127, R128 | line_item Standalone P&L p3 l140: Profit / (Loss) before exceptional items and tax (1-2) | - | 6 period cells
R129, R130, R131, R132, R133, R134, R135 | line_item Standalone P&L p3 l141: Exceptional items (refer note 3) | ZERO_STANDING | 6 period cells, 5 dash cells; carries refer-note qualifier
R136, R137, R138, R139, R140, R141 | line_item Standalone P&L p3 l142: Profit / (Loss) before tax (3-4) | - | 6 period cells
R142, R143, R144, R145, R146, R147 | line_item Standalone P&L p3 l144: Current tax | - | 6 period cells
R148, R149, R150, R151, R152, R153 | line_item Standalone P&L p3 l145: Deferred tax | ZERO_STANDING | 6 period cells, 1 dash cells
R154, R155, R156, R157, R158, R159 | line_item Standalone P&L p3 l146: Total tax expenses (net) | - | 6 period cells
R160, R161, R162, R163, R164, R165 | line_item Standalone P&L p3 l147: Profit / (Loss) for the period /year (5-6) | - | 6 period cells
R166, R167, R168, R169, R170, R171 | line_item Standalone P&L p3 l150: - Re-measurement of net defined benefit liability | ZERO_STANDING | 6 period cells, 1 dash cells
R172, R173, R174, R175, R176, R177 | line_item Standalone P&L p3 l151: - Income tax relating to above item | ZERO_STANDING | 6 period cells, 1 dash cells
R178, R179, R180, R181, R182, R183 | line_item Standalone P&L p3 l152: Total comprehensive income for the period / year (after tax) | - | 6 period cells
R184, R185, R186, R187, R188, R189 | line_item Standalone P&L p3 l153: Paid-up equity share capital (Face value of INR. 10 per shar | - | 6 period cells
R190, R191 | line_item Standalone P&L p3 l154: Other equity (excluding revaluation reserve INR. Nil) | - | 1 period cells; carries refer-note qualifier
R192, R193, R194, R195, R196, R197, R198 | line_item Standalone P&L p3 l156: Basic Earnings Per Share (not annualized except for year end | - | 6 period cells; carries refer-note qualifier
R199, R200, R201, R202, R203, R204, R205 | line_item Standalone P&L p3 l157: Diluted Earnings Per Share (not annualized except for year e | - | 6 period cells; carries refer-note qualifier
R210, R211 | line_item Standalone BS p4 l186: (a) Property, plant and equipment | - | 2 period cells
R212, R213 | line_item Standalone BS p4 l187: (b) Right-of-use assets | - | 2 period cells
R214, R215 | line_item Standalone BS p4 l188: (c) Capital work-in-progress | - | 2 period cells
R216, R217 | line_item Standalone BS p4 l189: (d) Investment properties | - | 2 period cells
R218, R219 | line_item Standalone BS p4 l190: (©) Intangible assets i | - | 2 period cells
R220, R221 | line_item Standalone BS p4 l192: (}) Investments | - | 2 period cells
R222, R223 | line_item Standalone BS p4 l193: (it) Other financial assets | - | 2 period cells
R224, R225 | line_item Standalone BS p4 l194: (g) Income tax assets (net) | - | 2 period cells
R226, R227 | line_item Standalone BS p4 l195: (h) Deferred tax assets (net) | - | 2 period cells
R228, R229 | line_item Standalone BS p4 l196: (i) Other non-current assets | - | 2 period cells
R230, R231 | line_item Standalone BS p4 l197: Total Non-current assets | - | 2 period cells
R232, R233 | line_item Standalone BS p4 l199: (a) Inventories | - | 2 period cells
R234, R235 | line_item Standalone BS p4 l201: (i) Investments | - | 2 period cells
R236, R237 | line_item Standalone BS p4 l202: (ii) Trade receivables | - | 2 period cells
R238, R239 | line_item Standalone BS p4 l203: (iit) Cash and cash equivalents | - | 2 period cells
R240, R241 | line_item Standalone BS p4 l204: (iv) Bank balances other than (iit) above | - | 2 period cells
R242, R243 | line_item Standalone BS p4 l205: (v) Loans | - | 2 period cells
R244, R245 | line_item Standalone BS p4 l206: (vi) Other financial assets | - | 2 period cells
R246, R247 | line_item Standalone BS p4 l207: (c) Other current assets | - | 2 period cells
R248, R249 | line_item Standalone BS p4 l208: Total Current assets | - | 2 period cells
R250, R251 | line_item Standalone BS p4 l209: Total Assets | - | 2 period cells
R252, R253 | line_item Standalone BS p4 l212: (a) Equity share capital | - | 2 period cells
R254, R255 | line_item Standalone BS p4 l213: (b) Other equity | - | 2 period cells
R256, R257 | line_item Standalone BS p4 l214: Total equity | - | 2 period cells
R258, R259 | line_item Standalone BS p4 l218: () Borrowings | ZERO_STANDING | 2 period cells, 1 dash cells
R260, R261 | line_item Standalone BS p4 l219: (it) Lease liabilities | - | 2 period cells
R262, R263 | line_item Standalone BS p4 l220: (ii) Other financial liabilities | - | 2 period cells
R264, R265 | line_item Standalone BS p4 l221: (b) Provisions | - | 2 period cells
R266, R267 | line_item Standalone BS p4 l222: (c) Other non-current liabilities | ZERO_STANDING | 2 period cells, 1 dash cells
R268, R269 | line_item Standalone BS p4 l223: Total Non- current liabilities | - | 2 period cells
R270, R271 | line_item Standalone BS p4 l226: () Borrowings | - | 2 period cells
R272, R273 | line_item Standalone BS p4 l227: (it) Lease liabilities | - | 2 period cells
R274, R275 | line_item Standalone BS p4 l229: ‘Total outstanding dues to micro and small enterprises | - | 2 period cells
R276, R277 | line_item Standalone BS p4 l230: Total outstanding dues to creditors other than micro and sma | - | 2 period cells
R278, R279 | line_item Standalone BS p4 l231: (iv) Other financial liabilities | - | 2 period cells
R280, R281 | line_item Standalone BS p4 l232: (b) Other current liabilities | - | 2 period cells
R282, R283 | line_item Standalone BS p4 l233: (c) Provisions | - | 2 period cells
R284, R285 | line_item Standalone BS p4 l234: (d) Current tax liabilities (net) | - | 2 period cells
R286, R287 | line_item Standalone BS p4 l235: Total Current liabilities | - | 2 period cells
R288, R289 | line_item Standalone BS p4 l236: Total Equity and Liabilities | - | 2 period cells
R293, R294 | line_item Standalone CF p5 l249: Profit before tax | - | 2 period cells
R295, R296 | line_item Standalone CF p5 l251: Provision / liabilities no longer required now written back | - | 2 period cells
R297, R298 | line_item Standalone CF p5 l252: Depreciation and amortisation expense | - | 2 period cells
R299, R300 | line_item Standalone CF p5 l253: Impairment Loss on trade receivables at | - | 2 period cells
R301, R302 | line_item Standalone CF p5 l254: Loss allowances on trade receivables | - | 2 period cells
R303, R304 | line_item Standalone CF p5 l255: Impairment of Intercorporate deposit (ICD) | ZERO_STANDING | 2 period cells, 1 dash cells
R305, R306 | line_item Standalone CF p5 l256: Impairment loss on Inventories | - | 2 period cells
R307, R308 | line_item Standalone CF p5 l257: Equity settled shared based payments | - | 2 period cells
R309, R310 | line_item Standalone CF p5 l258: Inventory written off | ZERO_STANDING | 2 period cells, 1 dash cells
R311, R312 | line_item Standalone CF p5 l259: Finance costs | - | 2 period cells
R313, R314 | line_item Standalone CF p5 l260: Gain on sale of investments (net) | - | 2 period cells
R315, R316 | line_item Standalone CF p5 l261: Interest expense on lease liabilities | - | 2 period cells
R317, R318 | line_item Standalone CF p5 l262: Net loss/(gain) on sale of property, plant & equipment (net) | - | 2 period cells
R319, R320 | line_item Standalone CF p5 l263: Fair value change of financial asset measured at FVTPL | - | 2 period cells
R321, R322 | line_item Standalone CF p5 l264: Interest income | - | 2 period cells
R323, R324 | line_item Standalone CF p5 l265: Rental income from investment properties | - | 2 period cells
R325, R326 | line_item Standalone CF p5 l266: Exchange gain on revaluation of foreign currency monetary it | ZERO_STANDING | 2 period cells, 1 dash cells
R327, R328 | line_item Standalone CF p5 l267: Operating cash flow before working capital changes | - | 2 period cells
R329, R330 | line_item Standalone CF p5 l269: (Increase) / Decrease in inventories | - | 2 period cells
R331, R332 | line_item Standalone CF p5 l270: (Increase) / Decrease in trade receivables | - | 2 period cells
R333, R334 | line_item Standalone CF p5 l271: (Increase) / Decrease in other assets, including financial a | - | 2 period cells
R335, R336 | line_item Standalone CF p5 l272: Increase/ (Decrease) in Trade payables | - | 2 period cells
R337, R338 | line_item Standalone CF p5 l273: Increase/ (Decrease) in other liabilities, including financi | - | 2 period cells
R339, R340 | line_item Standalone CF p5 l274: Cash generated from operating activities | - | 2 period cells
R341, R342 | line_item Standalone CF p5 l275: Income taxes paid | - | 2 period cells
R343, R344 | line_item Standalone CF p5 l276: Net cash generated /(used) in operating activities (A) | - | 2 period cells
R345, R346 | line_item Standalone CF p5 l278: Acquisition of property, plant and equipment (including capi | - | 2 period cells
R347, R348 | line_item Standalone CF p5 l280: Purchase of investments | - | 2 period cells
R349, R350 | line_item Standalone CF p5 l281: Proceeds from sale of property, plant and equipment | - | 2 period cells
R351, R352 | line_item Standalone CF p5 l282: Proceeds from sale of investments | - | 2 period cells
R353, R354 | line_item Standalone CF p5 l283: Interest income received | - | 2 period cells
R355, R356 | line_item Standalone CF p5 l284: Rental income from investment properties | - | 2 period cells
R357, R358 | line_item Standalone CF p5 l285: Inter Corporate Deposit given to wholly owned subsidary | - | 2 period cells
R359, R360 | line_item Standalone CF p5 l286: Fixed deposits matured | - | 2 period cells
R361, R362 | line_item Standalone CF p5 l287: Fixed deposits placed | ZERO_STANDING | 2 period cells, 1 dash cells
R363, R364 | line_item Standalone CF p5 l288: Net cash from/(used in) investing activities (B) | - | 2 period cells
R365, R366 | line_item Standalone CF p5 l290: Finance costs paid other than lease liabilities | - | 2 period cells
R367, R368 | line_item Standalone CF p5 l291: Finance cost paid on lease liabilities | - | 2 period cells
R369, R370 | line_item Standalone CF p5 l292: Repayment of principal portion of lease liabilities | - | 2 period cells
R371, R372 | line_item Standalone CF p5 l293: Repayment of vehicle loans | - | 2 period cells
R373, R374 | line_item Standalone CF p5 l294: Dividend paid | - | 2 period cells
R375, R376 | line_item Standalone CF p5 l295: Proceeds from borrowings | ZERO_STANDING | 2 period cells, 1 dash cells
R377, R378 | line_item Standalone CF p5 l296: Net cash used in financing activities (C) | - | 2 period cells
R379, R380 | line_item Standalone CF p5 l297: Net increase / (decrease) in cash and cash equivalents (A+B+ | - | 2 period cells
R381, R382 | line_item Standalone CF p5 l298: Cash and cash equivalents at the beginning of the year | - | 2 period cells
R383, R384 | line_item Standalone CF p5 l299: Cash and cash equivalents at the end of the period | - | 2 period cells
R385, R386 | line_item Standalone CF p5 l301: Cash on hand | - | 2 period cells
R387, R388 | line_item Standalone CF p5 l302: Mixed Deposit with banks (original maturity of less than 3 m | ZERO_STANDING | 2 period cells, 1 dash cells
R389, R390 | line_item Standalone CF p5 l303: Balances with banks in current accounts | - | 2 period cells
R391, R392 | line_item Standalone CF p5 l304: Total cash and cash equivalents | - | 2 period cells
R474, R475, R476, R477, R478, R479 | line_item Consol P&L p9 l440: Revenue from operations | - | 6 period cells
R480, R481, R482, R483, R484, R485 | line_item Consol P&L p9 l441: Other income | - | 6 period cells
R486, R487, R488, R489, R490, R491 | line_item Consol P&L p9 l442: Total income | - | 6 period cells
R492, R493, R494, R495, R496, R497 | line_item Consol P&L p9 l444: Cost of raw materials consumed | - | 6 period cells
R498, R499, R500, R501, R502, R503 | line_item Consol P&L p9 l445: Purchases of stock-in-trade | - | 6 period cells
R504, R505, R506, R507, R508, R509 | line_item Consol P&L p9 l446: Changes in inventories of finished goods, work-in-progress,  | - | 6 period cells
R510, R511, R512, R513, R514, R515 | line_item Consol P&L p9 l448: Employee benefits expenses | - | 6 period cells
R516, R517, R518, R519, R520, R521 | line_item Consol P&L p9 l449: Finance costs | - | 6 period cells
R522, R523, R524, R525, R526, R527 | line_item Consol P&L p9 l450: Depreciation and amortisation expense | - | 6 period cells
R528, R529, R530, R531, R532, R533, R534 | line_item Consol P&L p9 l451: Onerous cost and Liquidated Damages (refer note 5) | ZERO_STANDING | 6 period cells, 4 dash cells; carries refer-note qualifier
R535, R536, R537, R538, R539, R540, R541 | line_item Consol P&L p9 l452: Impairment reversal on trade receivables (refer note 7) | ZERO_STANDING | 6 period cells, 5 dash cells; carries refer-note qualifier
R542, R543, R544, R545, R546, R547 | line_item Consol P&L p9 l453: Other expenses | - | 6 period cells
R548, R549, R550, R551, R552, R553 | line_item Consol P&L p9 l454: Total expenses | - | 6 period cells
R554, R555, R556, R557, R558, R559 | line_item Consol P&L p9 l455: Profit/(loss) before exceptional items and tax (1-2) | - | 6 period cells
R560, R561, R562, R563, R564, R565, R566 | line_item Consol P&L p9 l456: Exceptional items (refer note 4) | ZERO_STANDING | 6 period cells, 5 dash cells; carries refer-note qualifier
R567, R568, R569, R570, R571, R572 | line_item Consol P&L p9 l457: Profit / (loss) before tax (3-4) | - | 6 period cells
R573, R574, R575, R576, R577, R578 | line_item Consol P&L p9 l459: Current tax | - | 6 period cells
R579, R580, R581, R582, R583, R584 | line_item Consol P&L p9 l460: Deferred tax | - | 6 period cells
R585, R586, R587, R588, R589, R590 | line_item Consol P&L p9 l461: Total tax expenses (net) | - | 6 period cells
R591, R592, R593, R594, R595, R596 | line_item Consol P&L p9 l462: Profit / (loss) for the period / year (5-6) | - | 6 period cells
R597, R598, R599, R600, R601, R602 | line_item Consol P&L p9 l465: - Re-measurement of net defined benefit liability | ZERO_STANDING | 6 period cells, 1 dash cells
R603, R604, R605, R606, R607, R608 | line_item Consol P&L p9 l466: - Income tax relating to above item | ZERO_STANDING | 6 period cells, 1 dash cells
R609, R610, R611, R612, R613, R614 | line_item Consol P&L p9 l467: Total comprehensive income for the period / year (after tax) | - | 6 period cells
R615, R616, R617, R618, R619, R620, R621 | line_item Consol P&L p9 l469: Owners of the Parent Company | - | 6 period cells; carries refer-note qualifier
R622, R623, R624, R625, R626, R627 | line_item Consol P&L p9 l470: Non-controlling interest | ZERO_STANDING | 6 period cells, 6 dash cells; NCI line all-dash for a wholly owned subsidiary (template signal)
R628, R629, R630, R631, R632, R633 | line_item Consol P&L p9 l472: Owners of the Parent Company | ZERO_STANDING | 6 period cells, 1 dash cells
R634, R635, R636, R637, R638, R639 | line_item Consol P&L p9 l473: Non-controlling interest | ZERO_STANDING | 6 period cells, 6 dash cells; NCI line all-dash for a wholly owned subsidiary (template signal)
R640, R641, R642, R643, R644, R645 | line_item Consol P&L p9 l475: Owners of the Parent Company | - | 6 period cells
R646, R647, R648, R649, R650, R651 | line_item Consol P&L p9 l476: Non-controlling interest | ZERO_STANDING | 6 period cells, 6 dash cells; NCI line all-dash for a wholly owned subsidiary (template signal)
R652, R653, R654, R655, R656, R657 | line_item Consol P&L p9 l477: Paid-up equity share capital (Face value of INR 10 per share | - | 6 period cells
R658, R659 | line_item Consol P&L p9 l478: Other equity (excluding revaluation reserve INR Nil) | - | 1 period cells; carries refer-note qualifier
R660, R661, R662, R663, R664, R665, R666 | line_item Consol P&L p9 l480: Basic Earnings Per Share (not annualized except for year end | - | 6 period cells; carries refer-note qualifier
R667, R668, R669, R670, R671, R672, R673 | line_item Consol P&L p9 l481: Diluted Earnings Per Share (not annualized except for year e | - | 6 period cells; carries refer-note qualifier
R678, R679 | line_item Consol BS p10 l506: (a) Property, plant and equipment | - | 2 period cells
R680, R681 | line_item Consol BS p10 l507: (b) Right-of-use assets | - | 2 period cells
R682, R683 | line_item Consol BS p10 l508: (c) Capital work-in-progress | - | 2 period cells
R684, R685 | line_item Consol BS p10 l509: (d) Investment properties | - | 2 period cells
R686, R687 | line_item Consol BS p10 l510: (e) Intangible assets | - | 2 period cells
R688, R689 | line_item Consol BS p10 l512: (i) Investment | - | 2 period cells
R690, R691 | line_item Consol BS p10 l513: (ii) Other financial assets | - | 2 period cells
R692, R693 | line_item Consol BS p10 l514: (g) Income tax assets (net) | - | 2 period cells
R694, R695 | line_item Consol BS p10 l515: (h) Deferred tax assets (net) | - | 2 period cells
R696, R697 | line_item Consol BS p10 l516: (i) Other non-current assets | - | 2 period cells
R698, R699 | line_item Consol BS p10 l517: Total Non-current assets | - | 2 period cells
R700, R701 | line_item Consol BS p10 l519: (a) Inventories | - | 2 period cells
R702, R703 | line_item Consol BS p10 l521: (i) Investments | - | 2 period cells
R704, R705 | line_item Consol BS p10 l522: (ii) Trade receivables | - | 2 period cells
R706, R707 | line_item Consol BS p10 l523: (iii) Cash and cash equivalents | - | 2 period cells
R708, R709 | line_item Consol BS p10 l524: (iv) Bank balances other than (iii) above | - | 2 period cells
R710, R711 | line_item Consol BS p10 l525: (vy) Loans | - | 2 period cells
R712, R713 | line_item Consol BS p10 l526: (vi) Other financial assets | - | 2 period cells
R714, R715 | line_item Consol BS p10 l527: (c) Other current assets | - | 2 period cells
R716, R717 | line_item Consol BS p10 l528: Total Current assets | - | 2 period cells
R718, R719 | line_item Consol BS p10 l529: Total Assets | - | 2 period cells
R720, R721 | line_item Consol BS p10 l532: (a) Equity share capital | - | 2 period cells
R722, R723 | line_item Consol BS p10 l533: (b) Other equity | - | 2 period cells
R724, R725 | line_item Consol BS p10 l534: Total equity | - | 2 period cells
R726, R727 | line_item Consol BS p10 l538: (!) Borrowings | ZERO_STANDING | 2 period cells, 1 dash cells
R728, R729 | line_item Consol BS p10 l539: (ii) Lease liabilities | - | 2 period cells
R730, R731 | line_item Consol BS p10 l540: (iii) Other financial liabilities | - | 2 period cells
R732, R733 | line_item Consol BS p10 l541: (b) Provisions | - | 2 period cells
R734, R735 | line_item Consol BS p10 l542: (c) Other non-current liabilities | - | 2 period cells
R736, R737 | line_item Consol BS p10 l543: Total Non- current liabilities | - | 2 period cells
R738, R739 | line_item Consol BS p10 l546: (i) Borrowings B71. | - | 2 period cells
R740, R741 | line_item Consol BS p10 l547: (ii) Lease liabilities | - | 2 period cells
R742, R743 | line_item Consol BS p10 l549: Total outstanding dues to micro and small enterprises | - | 2 period cells
R744, R745 | line_item Consol BS p10 l550: Total outstanding dues to creditors other than micro and sma | - | 2 period cells; R744 now 11,119 (A1 corrected, image-verified); stale check closed
R746, R747 | line_item Consol BS p10 l551: (iv) Other financial liabilities | - | 2 period cells
R748, R749 | line_item Consol BS p10 l552: (b) Other current liabilities | - | 2 period cells
R750, R751 | line_item Consol BS p10 l553: (c) Provisions | - | 2 period cells
R752, R753 | line_item Consol BS p10 l554: (d) Current tax liabilities (net) | - | 2 period cells
R754, R755 | line_item Consol BS p10 l555: Total Current liabilities | - | 2 period cells
R756, R757 | line_item Consol BS p10 l556: Total Equity and Liabilities | - | 2 period cells
R761, R762 | line_item Consol CF p11 l573: Profit before tax | - | 2 period cells
R763, R764 | line_item Consol CF p11 l575: Provision / liabilities no longer required now written back | - | 2 period cells
R765, R766 | line_item Consol CF p11 l576: Depreciation and amortisation expense | - | 2 period cells
R767, R768 | line_item Consol CF p11 l577: Impairment Loss on trade receivables | - | 2 period cells
R769, R770 | line_item Consol CF p11 l578: Loss allowances on trade receivables | - | 2 period cells
R771, R772 | line_item Consol CF p11 l579: Impairment loss on Inventories | - | 2 period cells
R773, R774 | line_item Consol CF p11 l580: Equity settled shared based payments | - | 2 period cells
R775, R776 | line_item Consol CF p11 l581: Inventory written off | ZERO_STANDING | 2 period cells, 1 dash cells
R777, R778 | line_item Consol CF p11 l582: Finance costs | - | 2 period cells
R779, R780 | line_item Consol CF p11 l583: Gain on sale of investments (net) | - | 2 period cells
R781, R782 | line_item Consol CF p11 l584: Interest expense on lease liability | - | 2 period cells
R783, R784 | line_item Consol CF p11 l585: Net loss/(gain) on sale of property, plant & equipment | - | 2 period cells
R785, R786 | line_item Consol CF p11 l586: Fair value change of financial asset measured at FVITPL | - | 2 period cells
R787, R788 | line_item Consol CF p11 l587: Interest income | - | 2 period cells
R789, R790 | line_item Consol CF p11 l588: Rental income from investment properties | - | 2 period cells
R791, R792 | line_item Consol CF p11 l589: Unrealised (Gain) /Loss on foreign exchange (net) | ZERO_STANDING | 2 period cells, 1 dash cells
R793, R794 | line_item Consol CF p11 l590: Operating profit before working capital changes | - | 2 period cells
R795, R796 | line_item Consol CF p11 l592: (Increase) /Decrease in inventories | - | 2 period cells
R797, R798 | line_item Consol CF p11 l593: (Increase) /Decrease in trade receivables | - | 2 period cells
R799, R800 | line_item Consol CF p11 l594: (Increase) /Decrease in other assets, including financial as | - | 2 period cells
R801, R802 | line_item Consol CF p11 l595: Increase/ (Decrease) in Trade payables | - | 2 period cells
R803, R804 | line_item Consol CF p11 l596: Increase/ (Decrease) in other liabilities, including financi | - | 2 period cells
R805, R806 | line_item Consol CF p11 l597: Cash generated from operating activities | - | 2 period cells
R807, R808 | line_item Consol CF p11 l598: Income tax paid | - | 2 period cells
R809, R810 | line_item Consol CF p11 l599: Net cash generated/used from/in operating activities (A) | - | 2 period cells
R811, R812 | line_item Consol CF p11 l601: Acquisition of property, plant and equipment (including capi | - | 2 period cells
R813, R814 | line_item Consol CF p11 l603: Purchase of investments | - | 2 period cells
R815, R816 | line_item Consol CF p11 l604: Proceeds from sale of property, plant and equipment | - | 2 period cells
R817, R818 | line_item Consol CF p11 l605: Proceeds from sale of investments | - | 2 period cells
R819, R820 | line_item Consol CF p11 l606: Interest income received | - | 2 period cells
R821, R822 | line_item Consol CF p11 l607: Rental income from investment properties | - | 2 period cells
R823, R824 | line_item Consol CF p11 l608: Fixed deposits matured | ZERO_STANDING | 2 period cells, 1 dash cells
R825, R826 | line_item Consol CF p11 l609: Fixed deposits placed | - | 2 period cells
R827, R828 | line_item Consol CF p11 l610: Net cash from/used in investing activities (B) | - | 2 period cells
R829, R830 | line_item Consol CF p11 l614: Finance costs paid other than lease liabilities | - | 2 period cells
R831, R832 | line_item Consol CF p11 l615: Finance cost paid on lease liabilities | - | 2 period cells
R833, R834 | line_item Consol CF p11 l616: Repayment of principal portion of lease liabilities | - | 2 period cells
R835, R836 | line_item Consol CF p11 l617: Repayment of Vehicle Loans | - | 2 period cells
R837, R838 | line_item Consol CF p11 l618: Dividend paid | - | 2 period cells
R839, R840 | line_item Consol CF p11 l619: Proceeds from borrowings | ZERO_STANDING | 2 period cells, 1 dash cells
R841, R842 | line_item Consol CF p11 l620: Net cash used in financing activities (C) | - | 2 period cells
R843, R844 | line_item Consol CF p11 l621: Net increase / (decrease) in‘cash and cash equivalents (A+B+ | - | 2 period cells
R845, R846 | line_item Consol CF p11 l622: Cash and cash equivalents at the beginning of the year | - | 2 period cells
R847, R848 | line_item Consol CF p11 l623: Cash and cash equivalents at the end of the period | - | 2 period cells
R849, R850 | line_item Consol CF p11 l625: Cash on hand | - | 2 period cells
R851, R852 | line_item Consol CF p11 l626: Fixed Deposit with banks (original maturity of less than 3 m | ZERO_STANDING | 2 period cells, 1 dash cells
R853, R854 | line_item Consol CF p11 l627: Balances with banks in current accounts | - | 2 period cells
R855, R856 | line_item Consol CF p11 l628: Total cash and cash equivalents | - | 2 period cells
R398, R901, R902, R903, R904, R905 | line_item Standalone note 3 table: provision/diminution investment+ICD 3DFT (FY26 col 556; other 5 cells dash) | ZERO_STANDING | exceptional-items table line; 5 dash cells
R399, R906, R907, R908, R909, R910 | line_item Standalone note 3 table: Labour Codes (FY26 col 275; other 5 cells dash) | ZERO_STANDING | exceptional-items table line; 5 dash cells
R911, R912, R913, R914, R915, R916 | line_item Standalone note 3 table: Total exceptional items (FY26 col 831 = 556 + 275; other 5 cells dash) | ZERO_STANDING | exceptional-items table line; 5 dash cells; ties to R398+R399
R863, R917, R918, R919, R920, R921 | line_item Consol note 4 table: Labour Codes (FY26 col 275; other 5 cells dash) | ZERO_STANDING | exceptional-items table line; 5 dash cells
R864, R922, R923, R924, R925, R926 | line_item Consol note 4 table: exceptional total (FY26 col 275; other 5 cells dash) | ZERO_STANDING | exceptional-items table line; 5 dash cells

## 2b. TABLE METADATA (period/unit/audit-status headers not attached to a line)

IDs | category | A2 flags | cross-ref / materiality
--- | --- | --- | ---
R039 | table_meta | - | Standalone P&L p3 l119 QUALIFIER
R040 | table_meta | - | Standalone P&L p3 l120 QUALIFIER
R041 | table_meta | - | Standalone P&L p3 l122 DATE
R042 | table_meta | - | Standalone P&L p3 l123 QUALIFIER
R206 | table_meta | - | Standalone P&L p3 l159 QUALIFIER
R207 | table_meta | - | Standalone BS p4 l180 QUALIFIER
R208 | table_meta | - | Standalone BS p4 l182 DATE
R209 | table_meta | - | Standalone BS p4 l183 QUALIFIER
R290 | table_meta | - | Standalone CF p5 l244 QUALIFIER
R291 | table_meta | - | Standalone CF p5 l245 DATE
R292 | table_meta | - | Standalone CF p5 l247 QUALIFIER
R471 | table_meta | - | Consol P&L p9 l435 QUALIFIER
R472 | table_meta | - | Consol P&L p9 l437 DATE
R473 | table_meta | - | Consol P&L p9 l438 QUALIFIER
R674 | table_meta | - | Consol P&L p9 l482 QUALIFIER
R675 | table_meta | - | Consol BS p10 l500 QUALIFIER
R676 | table_meta | - | Consol BS p10 l502 DATE
R677 | table_meta | - | Consol BS p10 l503 QUALIFIER
R758 | table_meta | - | Consol CF p11 l567 DATE
R759 | table_meta | - | Consol CF p11 l568 QUALIFIER
R760 | table_meta | - | Consol CF p11 l571 QUALIFIER

## 3. AGENDA ITEMS (Board Outcome letter)

IDs | category | A2 flags | cross-ref / materiality
--- | --- | --- | ---
R001, R002, R003, R004, R005 | agenda_item letter header (reference, scrip code, exchanges, letter date) | - | 
R006, R007, R008 | agenda_item meeting date and times: start 12:00 Noon, end 03:15 (3h15m) | A1_OCR | end time OCR_PARTIAL (R008)
R009, R010, R011 | agenda_item agenda a: Unaudited Financial Results standalone and consolidated | - | 
R012, R013, R014 | agenda_item agenda b: Limited Review Report, BSR & Co. LLP, plus website/newspaper publication | - | 
R015, R016, R017, R018, R019 | agenda_item agenda c: interim dividend Rs 7.50, record date 30-Oct-2026, payment by 20-Nov-2026 | RESTATED | restated in notes S8/C10; no AR, AGM, director, auditor, ESOP or capital-raise items on the letter (absence)
R020, R021, R022, R023 | agenda_item letter signature: Company Secretary Vinayak M. Bhide, registered office, CIN | - | wet-seal signature; no digital timestamp in text

## 4. AUDITOR PARAGRAPHS (standalone LRR p2; consolidated LRR p7-8)

IDs | category | A2 flags | cross-ref / materiality
--- | --- | --- | ---
R024, R025, R026 | auditor_para | - | Standalone LRR para 1 (review scope, periods)
R027 | auditor_para | - | Standalone LRR para 2 (mgmt responsibility, framework)
R028, R029, R030 | auditor_para | - | Standalone LRR para 3 (SRE 2410, scope)
R031 | auditor_para | - | Standalone LRR para 4 (conclusion, unmodified); no Emphasis of Matter, no Going Concern language in either LRR (grep of fulltext)
R032, R033, R034, R035, R036, R037, R038 | auditor_para | A1_OCR | Standalone LRR signature block (firm, partner membership, UDIN, date); UDIN OCR uncertain (R034); partner name not captured
R443, R444 | auditor_para | - | Consol LRR para 1
R445, R446 | auditor_para | - | Consol LRR para 3 (procedures, Reg 33(8))
R447, R448 | auditor_para | - | Consol LRR para 4 (entity list: 3DFT subsidiary); sole consolidation entity listed; see entity table
R449, R450, R451 | auditor_para | - | Consol LRR p7 footer (BSR LLP conversion, page 1 of 2)
R452, R453, R454, R455, R456, R457, R458, R459, R460, R461, R462, R463, R464, R465, R466 | auditor_para | UNREVIEWED_ENTITY | Consol LRR para 6 OTHER MATTER (one subsidiary not reviewed by BSR; other auditor; figures before consolidation adjustments); 3DFT figures: assets 299, Q2 revenue 56, H1 revenue 137, Q2 loss (49), H1 loss (64), net cash flow (0.02), INR lakhs; conclusion not modified; other auditor unnamed
R467, R468, R469, R470 | auditor_para | - | Consol LRR signature block (partner Amar Sunder, UDIN, date)
(no ID) | auditor_para | - | Consol LRR para 2 (mgmt responsibility) and para 5 (conclusion, unmodified): no discrete units in A1 rows; fulltext lines 373, 392

## 5. ENTITIES (all 26 ENTITY rows; consolidation list = Parent + 3DFT)

IDs | category | A2 flags | cross-ref / materiality
--- | --- | --- | ---
R003 | entity | - | p1 l20 exchange; no prior ledger, ENTITY_CHANGE not testable
R004 | entity | - | p1 l20 exchange
R010 | entity | - | p1 l31 regulation
R013 | entity | - | p1 l35 statutory auditor
R020 | entity | - | p1 l49 company
R021 | entity | - | p1 l56 Company Secretary
R022 | entity | - | p1 l60 registered office
R024 | entity | - | p2 l65 auditor
R027 | entity | - | p2 l82 framework
R029 | entity | - | p2 l88 professional body
R401 | entity | - | p6 l319 subsidiary
R406 | entity | - | p6 l321 regulator
R412 | entity | - | p6 l326 division with turnkey project
R423 | entity | - | p6 l331 regulator
R428 | entity | - | p6 l333 project
R430 | entity | - | p6 l335 segment
R441 | entity | - | p6 l345 director
R447 | entity | UNREVIEWED_ENTITY | p7 l391 subsidiary in LRR
R464 | entity | - | p8 l414 sub auditor
R467 | entity | - | p8 l422 audit partner
R621 | entity | - | p9 l469 attribution
R860 | entity | - | p12 l636 consolidated entity
R873 | entity | - | p12 l649 division
R883 | entity | - | p12 l654 regulator
R889 | entity | - | p12 l656 project
R899 | entity | - | p12 l665 director

## 6. CROSS-REFERENCES (RESTATED sets; IDs already counted above)

IDs | category | A2 flags | cross-ref / materiality
--- | --- | --- | ---
Interim dividend Rs 7.50 | R015,R432,R893 | RESTATED | R893 OCR 27.50 and R895 OCR 210 conflict with page 1
Labour Codes INR 275 lakhs | R399,R407,R408,R863,R864,R867,R869 | RESTATED | standalone and consol identical
Turnkey provisions 1,293 + 1,499 + VO 310 | R415,R416,R418,R876,R877,R878 | RESTATED | prior-year amounts; target June 2025 lapsed (R410,R413,R871,R875)
BIS compounding 3,643 / fine 34 | R420,R425,R885,R886 | RESTATED | 
Kuwait recovery 1,412 | R426,R887 | RESTATED | 
MD DIN 01585637 | R440,R898 | RESTATED | 
Board approval/LRR date 21-Oct-2026 | R035,R394,R469,R857,R442,R900 | RESTATED | LRR date equals board date; meeting ended 03:15 PM

## 7. MISSING_FROM_STRUCTURED

IDs | category | A2 flags | cross-ref / materiality
--- | --- | --- | ---
M01 | page 1 | line 24 | Company Symbol: ADOR (NSE trading symbol, beside scrip code 517041) | MISSING_FROM_STRUCTURED | low materiality, loop to A1 (line 317 item closed: R911-R916 added by A1)
