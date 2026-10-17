# LEDGER: results HERITGFOOD q2fy27 (A2 enumerator)
Source: runs/heritgfood-q2fy27/extracted/heritgfood-results-q2fy27-structured.md (IDs reference A1 rows; verbatim values stay there)

ids_in_structured: 1242 | ids_referenced_in_ledger: 1242 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes (numbered, incl cash flow note 1)   grep_count: 12   sweep_count: 12   match: yes
category: line_items (distinct table+item)   grep_count: 299   sweep_count: 299 (distinct table+page+line)   match: yes
category: statement NUMBER rows   grep_count: 1114   sweep_count: 1114   match: yes
category: zero_standing rows   grep_count: 60   sweep_count: 60   match: yes
category: entities   grep_count: 28   sweep_count: 28   match: yes
category: dates   grep_count: 23   sweep_count: 23   match: yes
category: qualifiers (notes + footnotes)   grep_count: 50   sweep_count: 50   match: yes
category: agenda_items   grep_count: 0   sweep_count: 0   match: yes
gate_a2: pass
=== END COUNT TEST ===

## LINE ITEMS (financial tables; one row per item, IDs grouped)
ITEM# | table | page | line | line item (label from A1) | ROW IDs | n | A2 flags | note
L001 | standalone P&L | 2 | 75 | a. Revenue from operations | R001-R006 | 6 |  |
L002 | standalone P&L | 2 | 76 | b. Other income | R007-R012 | 6 |  |
L003 | standalone P&L | 2 | 77 | Total income | R013-R018 | 6 |  |
L004 | standalone P&L | 2 | 79 | a. Cost of materials consumed | R019-R024 | 6 |  |
L005 | standalone P&L | 2 | 80 | b. Purchases of stock-in-trade | R025-R030 | 6 |  |
L006 | standalone P&L | 2 | 81 | c. Changes in inventories of finished goods, semi finished goods, stoc | R031-R036 | 6 |  |
L007 | standalone P&L | 2 | 82 | d. Employee benefit expenses | R037-R042 | 6 |  |
L008 | standalone P&L | 2 | 83 | e. Finance costs | R043-R048 | 6 |  |
L009 | standalone P&L | 2 | 84 | f. Depreciation and amortization expense | R049-R054 | 6 |  |
L010 | standalone P&L | 2 | 85 | g. Impairment losses | R055-R060 | 6 | ZERO_STANDING(5 of 6 periods) |
L011 | standalone P&L | 2 | 86 | h. Other expenses | R061-R066 | 6 |  |
L012 | standalone P&L | 2 | 87 | Total expenses | R067-R072 | 6 |  |
L013 | standalone P&L | 2 | 88 | 3 Profit before exceptional items and tax | R073-R078 | 6 |  |
L014 | standalone P&L | 2 | 89 | 4 Exceptional items [refer note 4] | R079-R084 | 6 | ZERO_STANDING(3 of 6 periods) |
L015 | standalone P&L | 2 | 90 | 5 Profit before tax | R085-R090 | 6 |  |
L016 | standalone P&L | 2 | 92 | a. Current tax expense | R091-R096 | 6 |  |
L017 | standalone P&L | 2 | 93 | b. Deferred tax expense | R097-R102 | 6 |  |
L018 | standalone P&L | 2 | 94 | 7 Profit for the period/year | R103-R108 | 6 |  |
L019 | standalone P&L | 2 | 97 | (i) Re-measurement loss on defined benefit plan, net of tax | R109-R114 | 6 |  |
L020 | standalone P&L | 2 | 98 | (ii) Net loss / (gain) on fair value through OCI equity securities | R115-R120 | 6 |  |
L021 | standalone P&L | 2 | 99 | (b) Items that will be reclassified to profit or loss | R121-R126 | 6 | ZERO_STANDING(all periods) |
L022 | standalone P&L | 2 | 100 | 9 Total comprehensive income for the period/year | R127-R132 | 6 |  |
L023 | standalone P&L | 2 | 101 | 10 Paid up Equity Share Capital (face value of Rs 5 each) | R133-R138 | 6 |  |
L024 | standalone P&L | 2 | 102 | 11 Other equity | R139-R139 | 1 |  |
L025 | standalone P&L | 2 | 104 | *Basic and Diluted EPES (in absolute Rs terms) | R140-R145 | 6 |  |
L026 | standalone segment | 3 | 119 | a. Dairy | R146-R151 | 6 |  |
L027 | standalone segment | 3 | 120 | b. Renewable energy | R152-R157 | 6 |  |
L028 | standalone segment | 3 | 121 | Total | R158-R163 | 6 |  |
L029 | standalone segment | 3 | 122 | Less: Inter segment revenue | R164-R169 | 6 |  |
L030 | standalone segment | 3 | 123 | (net segment revenue) | R170-R175 | 6 |  |
L031 | standalone segment | 3 | 125 | a. Dairy | R176-R181 | 6 |  |
L032 | standalone segment | 3 | 126 | b. Renewable energy | R182-R187 | 6 |  |
L033 | standalone segment | 3 | 127 | Total | R188-R193 | 6 |  |
L034 | standalone segment | 3 | 128 | Less: i. Finance costs | R194-R199 | 6 |  |
L035 | standalone segment | 3 | 129 | ii. Other un-allocable expenses | R200-R205 | 6 |  |
L036 | standalone segment | 3 | 130 | Add: i. Interest income | R206-R211 | 6 |  |
L037 | standalone segment | 3 | 131 | ii. Other un-allocable income | R212-R217 | 6 |  |
L038 | standalone segment | 3 | 132 | Profit before tax | R218-R223 | 6 |  |
L039 | standalone segment | 3 | 134 | a. Dairy | R224-R229 | 6 |  |
L040 | standalone segment | 3 | 135 | b. Renewable energy | R230-R235 | 6 |  |
L041 | standalone segment | 3 | 136 | c. Unallocated | R236-R241 | 6 |  |
L042 | standalone segment | 3 | 137 | Total | R242-R247 | 6 |  |
L043 | standalone segment | 3 | 139 | a. Dairy | R248-R253 | 6 |  |
L044 | standalone segment | 3 | 140 | b. Renewable energy | R254-R259 | 6 |  |
L045 | standalone segment | 3 | 141 | c. Unallocated | R260-R265 | 6 |  |
L046 | standalone segment | 3 | 142 | Total | R266-R271 | 6 |  |
L047 | standalone balance sheet | 4 | 156 | (a) Property, plant and equipment | R272-R273 | 2 |  |
L048 | standalone balance sheet | 4 | 157 | (b) Right of use assets | R274-R275 | 2 |  |
L049 | standalone balance sheet | 4 | 158 | (c) Capital work-in-progress | R276-R277 | 2 |  |
L050 | standalone balance sheet | 4 | 159 | (d) Investment property | R278-R279 | 2 |  |
L051 | standalone balance sheet | 4 | 160 | (e) Other intangible assets | R280-R281 | 2 |  |
L052 | standalone balance sheet | 4 | 161 | (f) Intangible assets under development | R282-R283 | 2 |  |
L053 | standalone balance sheet | 4 | 163 | (i) Investment in subsidiary, joint venture and associate | R284-R285 | 2 |  |
L054 | standalone balance sheet | 4 | 164 | (ii) Loans | R286-R287 | 2 |  |
L055 | standalone balance sheet | 4 | 165 | (iii) Other investments | R288-R289 | 2 |  |
L056 | standalone balance sheet | 4 | 166 | (iv) Other financial assets | R290-R291 | 2 |  |
L057 | standalone balance sheet | 4 | 167 | (h) Other non-current assets | R292-R293 | 2 |  |
L058 | standalone balance sheet | 4 | 168 | Total non-current assets | R294-R295 | 2 |  |
L059 | standalone balance sheet | 4 | 170 | (a) Inventories | R296-R297 | 2 |  |
L060 | standalone balance sheet | 4 | 172 | (i) Investments | R298-R299 | 2 |  |
L061 | standalone balance sheet | 4 | 173 | (ii) Trade receivables | R300-R301 | 2 |  |
L062 | standalone balance sheet | 4 | 174 | (iii) Cash and cash equivalents | R302-R303 | 2 |  |
L063 | standalone balance sheet | 4 | 175 | (iv) Bank balances other than (iii) above | R304-R305 | 2 |  |
L064 | standalone balance sheet | 4 | 176 | (v) Loans | R306-R307 | 2 |  |
L065 | standalone balance sheet | 4 | 177 | (vi) Other financial assets | R308-R309 | 2 |  |
L066 | standalone balance sheet | 4 | 178 | (c) Current tax assets (net) | R310-R311 | 2 |  |
L067 | standalone balance sheet | 4 | 179 | (d) Other current assets | R312-R313 | 2 |  |
L068 | standalone balance sheet | 4 | 180 | Total current assets | R314-R315 | 2 |  |
L069 | standalone balance sheet | 4 | 181 | Total assets | R316-R317 | 2 |  |
L070 | standalone balance sheet | 4 | 183 | (a) Equity share capital | R318-R319 | 2 |  |
L071 | standalone balance sheet | 4 | 184 | (b) Other equity | R320-R321 | 2 |  |
L072 | standalone balance sheet | 4 | 185 | Total equity | R322-R323 | 2 |  |
L073 | standalone balance sheet | 4 | 188 | (i) Borrowings | R324-R325 | 2 |  |
L074 | standalone balance sheet | 4 | 189 | (ia) Lease liabilities | R326-R327 | 2 |  |
L075 | standalone balance sheet | 4 | 190 | (ii) Other financial liabilities | R328-R329 | 2 |  |
L076 | standalone balance sheet | 4 | 191 | (b) Government grant | R330-R331 | 2 |  |
L077 | standalone balance sheet | 4 | 192 | (c) Provisions | R332-R333 | 2 |  |
L078 | standalone balance sheet | 4 | 193 | (d) Deferred tax liabilities (net) | R334-R335 | 2 |  |
L079 | standalone balance sheet | 4 | 194 | (e) Other non-current liabilities | R336-R337 | 2 |  |
L080 | standalone balance sheet | 4 | 195 | Total non-current liabilities | R338-R339 | 2 |  |
L081 | standalone balance sheet | 4 | 197 | (i) Borrowings | R340-R341 | 2 |  |
L082 | standalone balance sheet | 4 | 198 | (ia) Lease liabilities | R342-R343 | 2 |  |
L083 | standalone balance sheet | 4 | 200 | - total outstanding dues of micro and small enterprises; | R344-R345 | 2 |  |
L084 | standalone balance sheet | 4 | 201 | - total outstanding dues of creditors other than micro and small enter | R346-R347 | 2 |  |
L085 | standalone balance sheet | 4 | 202 | (iii) Other financial liabilities | R348-R349 | 2 |  |
L086 | standalone balance sheet | 4 | 203 | (b) Other current liabilities | R350-R351 | 2 |  |
L087 | standalone balance sheet | 4 | 204 | (c) Government grant | R352-R353 | 2 |  |
L088 | standalone balance sheet | 4 | 205 | (d) Provisions | R354-R355 | 2 |  |
L089 | standalone balance sheet | 4 | 206 | Total current liabilities | R356-R357 | 2 |  |
L090 | standalone balance sheet | 4 | 207 | Total equity and liabilities | R358-R359 | 2 |  |
L091 | standalone cash flow | 5 | 221 | Profit before tax | R360-R362 | 3 |  |
L092 | standalone cash flow | 5 | 223 | Depreciation and amortization expense | R363-R365 | 3 |  |
L093 | standalone cash flow | 5 | 224 | Impairment losses on assets | R366-R368 | 3 | ZERO_STANDING(2 of 3 periods) |
L094 | standalone cash flow | 5 | 225 | Impairment losses on investments | R369-R371 | 3 | ZERO_STANDING(2 of 3 periods) |
L095 | standalone cash flow | 5 | 226 | Provision for doubtful debts and bad debts written off | R372-R374 | 3 |  |
L096 | standalone cash flow | 5 | 227 | Advances written off | R375-R377 | 3 |  |
L097 | standalone cash flow | 5 | 228 | Profit on sale of Property, plant and equipment ("PPE") | R378-R380 | 3 |  |
L098 | standalone cash flow | 5 | 229 | Gain on investments | R381-R383 | 3 |  |
L099 | standalone cash flow | 5 | 230 | Provisions no longer required/ credit balances written back | R384-R386 | 3 |  |
L100 | standalone cash flow | 5 | 231 | Interest income | R387-R389 | 3 |  |
L101 | standalone cash flow | 5 | 232 | Interest expenses | R390-R392 | 3 |  |
L102 | standalone cash flow | 5 | 233 | Guarantee Income | R393-R395 | 3 |  |
L103 | standalone cash flow | 5 | 234 | Property, plant and equipment written off | R396-R398 | 3 |  |
L104 | standalone cash flow | 5 | 235 | Amortisation of government grants | R399-R401 | 3 |  |
L105 | standalone cash flow | 5 | 236 | Lease rental income | R402-R404 | 3 |  |
L106 | standalone cash flow | 5 | 237 | Dividend income on long term investments | R405-R407 | 3 |  |
L107 | standalone cash flow | 5 | 238 | Operating profits before working capital changes | R408-R410 | 3 |  |
L108 | standalone cash flow | 5 | 240 | Changes in inventories | R411-R413 | 3 |  |
L109 | standalone cash flow | 5 | 241 | Changes in trade receivables | R414-R416 | 3 |  |
L110 | standalone cash flow | 5 | 242 | Changes in other assets | R417-R419 | 3 |  |
L111 | standalone cash flow | 5 | 243 | Changes in other financial assets | R420-R422 | 3 |  |
L112 | standalone cash flow | 5 | 244 | Changes in trade payables | R423-R425 | 3 |  |
L113 | standalone cash flow | 5 | 245 | Changes in provisions | R426-R428 | 3 |  |
L114 | standalone cash flow | 5 | 246 | Changes in other financial liabilities | R429-R431 | 3 |  |
L115 | standalone cash flow | 5 | 247 | Changes in other liabilities | R432-R434 | 3 |  |
L116 | standalone cash flow | 5 | 248 | Cash generated from operating activities | R435-R437 | 3 |  |
L117 | standalone cash flow | 5 | 249 | Income tax paid, net | R438-R440 | 3 |  |
L118 | standalone cash flow | 5 | 250 | Net cash generated from operating activities (A) | R441-R443 | 3 |  |
L119 | standalone cash flow | 5 | 252 | Purchase of PPE and other intangible assets, including CWIP | R444-R446 | 3 |  |
L120 | standalone cash flow | 5 | 253 | Proceeds from sale of PPE | R447-R449 | 3 |  |
L121 | standalone cash flow | 5 | 254 | Loans to subsidiaries | R450-R452 | 3 |  |
L122 | standalone cash flow | 5 | 255 | Investment in a subsidiaries | R453-R455 | 3 |  |
L123 | standalone cash flow | 5 | 256 | Receipts of government grants | R456-R458 | 3 | ZERO_STANDING(1 of 3 periods) |
L124 | standalone cash flow | 5 | 257 | Purchase of investments | R459-R461 | 3 |  |
L125 | standalone cash flow | 5 | 258 | Proceeds from sale of investments | R462-R464 | 3 |  |
L126 | standalone cash flow | 5 | 259 | Interest received | R465-R467 | 3 |  |
L127 | standalone cash flow | 5 | 260 | Movement in other bank balances, net | R468-R470 | 3 |  |
L128 | standalone cash flow | 5 | 261 | Rent received | R471-R473 | 3 |  |
L129 | standalone cash flow | 5 | 262 | Dividend income received | R474-R476 | 3 |  |
L130 | standalone cash flow | 5 | 263 | Net cash used in investing activities (B) | R477-R479 | 3 |  |
L131 | standalone cash flow | 5 | 265 | Proceeds from long term borrowings | R480-R482 | 3 |  |
L132 | standalone cash flow | 5 | 266 | Repayments of long term borrowings | R483-R485 | 3 |  |
L133 | standalone cash flow | 5 | 267 | Proceeds from/(Repayment of) short term borrowings, net | R486-R488 | 3 | ZERO_STANDING(1 of 3 periods) |
L134 | standalone cash flow | 5 | 268 | Interest paid | R489-R491 | 3 |  |
L135 | standalone cash flow | 5 | 269 | Lease rentals paid | R492-R494 | 3 |  |
L136 | standalone cash flow | 5 | 270 | Dividend paid | R495-R497 | 3 |  |
L137 | standalone cash flow | 5 | 271 | Net cash generated from / (used in) financing activities (C) | R498-R500 | 3 |  |
L138 | standalone cash flow | 5 | 272 | Net Change in cash and cash equivalents during the period/ year (A + B | R501-R503 | 3 |  |
L139 | standalone cash flow | 5 | 273 | Cash and cash equivalents at the beginning of the year | R504-R506 | 3 |  |
L140 | standalone cash flow | 5 | 274 | Cash and cash equivalents at the end of the year (Note 1) | R507-R509 | 3 |  |
L141 | standalone cash flow | 5 | 276 | Cash on hand | R510-R512 | 3 |  |
L142 | standalone cash flow | 5 | 277 | Balances with banks in current accounts | R513-R515 | 3 |  |
L143 | standalone cash flow | 5 | 278 | (total) | R516-R518 | 3 |  |
L144 | consolidated P&L | 9 | 407 | a. Revenue from operations | R519-R524 | 6 |  |
L145 | consolidated P&L | 9 | 408 | b. Other income | R525-R530 | 6 |  |
L146 | consolidated P&L | 9 | 409 | Total income | R531-R536 | 6 |  |
L147 | consolidated P&L | 9 | 411 | a. Cost of materials consumed | R537-R542 | 6 |  |
L148 | consolidated P&L | 9 | 412 | b. Purchases of stock-in-trade | R543-R548 | 6 |  |
L149 | consolidated P&L | 9 | 413 | c. Changes in inventories of finished goods, semi finished goods, stoc | R549-R554 | 6 |  |
L150 | consolidated P&L | 9 | 414 | d. Employee benefits expenses | R555-R560 | 6 |  |
L151 | consolidated P&L | 9 | 415 | e. Finance costs | R561-R566 | 6 |  |
L152 | consolidated P&L | 9 | 416 | f. Depreciation and amortization expense | R567-R572 | 6 |  |
L153 | consolidated P&L | 9 | 417 | g. Impairment losses | R573-R578 | 6 | ZERO_STANDING(5 of 6 periods) |
L154 | consolidated P&L | 9 | 418 | h. Other expenses | R579-R584 | 6 |  |
L155 | consolidated P&L | 9 | 419 | Total expenses | R585-R590 | 6 |  |
L156 | consolidated P&L | 9 | 420 | 3 Profit before share of loss of an associate and a joint venture | R591-R596 | 6 |  |
L157 | consolidated P&L | 9 | 421 | 4 Share of loss of an associate and a joint venture | R597-R602 | 6 | ZERO_STANDING(4 of 6 periods) |
L158 | consolidated P&L | 9 | 422 | 5 Profit before tax | R603-R608 | 6 |  |
L159 | consolidated P&L | 9 | 423 | 6 Exceptional items (refer note 4) | R609-R614 | 6 | ZERO_STANDING(3 of 6 periods) |
L160 | consolidated P&L | 9 | 424 | 7 Profit before tax | R615-R620 | 6 |  |
L161 | consolidated P&L | 9 | 426 | a. Current tax expense | R621-R626 | 6 |  |
L162 | consolidated P&L | 9 | 427 | b. Deferred tax expense | R627-R632 | 6 |  |
L163 | consolidated P&L | 9 | 428 | 9 Profit for the period/year | R633-R638 | 6 |  |
L164 | consolidated P&L | 9 | 431 | (i) Re-measurement loss on defined benefit plan, net of tax | R639-R644 | 6 |  |
L165 | consolidated P&L | 9 | 432 | (ii) Net loss /(gain) on fair value through OCI equity securities | R645-R650 | 6 |  |
L166 | consolidated P&L | 9 | 433 | (b) Items that will be reclassified to profit or loss | R651-R656 | 6 | ZERO_STANDING(all periods) |
L167 | consolidated P&L | 9 | 434 | 11 Total comprehensive income for the period/year | R657-R662 | 6 |  |
L168 | consolidated P&L | 9 | 436 | - Profit for the period / year | R663-R668 | 6 |  |
L169 | consolidated P&L | 9 | 437 | - Other comprehensive loss | R669-R674 | 6 |  |
L170 | consolidated P&L | 9 | 438 | - Total comprehensive income | R675-R680 | 6 |  |
L171 | consolidated P&L | 9 | 440 | - Loss for the period / year | R681-R686 | 6 |  |
L172 | consolidated P&L | 9 | 441 | - Other comprehensive loss | R687-R692 | 6 | ZERO_STANDING(all periods) |
L173 | consolidated P&L | 9 | 442 | - Total comprehensive loss | R693-R698 | 6 |  |
L174 | consolidated P&L | 9 | 443 | 14 Paid up Equity share capital (face value of Rs 5 each) | R699-R704 | 6 |  |
L175 | consolidated P&L | 9 | 444 | 15 Other equity (attributable to the Owners of the Company) | R705-R705 | 1 |  |
L176 | consolidated P&L | 9 | 446 | *Basic and Diluted EPES (in absolute Rs terms) | R706-R711 | 6 |  |
L177 | consolidated segment | 10 | 461 | a. Dairy | R712-R717 | 6 |  |
L178 | consolidated segment | 10 | 462 | b. Renewable energy | R718-R723 | 6 |  |
L179 | consolidated segment | 10 | 463 | c. Feed | R724-R729 | 6 |  |
L180 | consolidated segment | 10 | 464 | Total | R730-R735 | 6 |  |
L181 | consolidated segment | 10 | 465 | Less: Inter segment revenue | R736-R741 | 6 |  |
L182 | consolidated segment | 10 | 466 | Income from operations | R742-R747 | 6 |  |
L183 | consolidated segment | 10 | 468 | a. Dairy | R748-R753 | 6 |  |
L184 | consolidated segment | 10 | 469 | b. Renewable energy | R754-R759 | 6 |  |
L185 | consolidated segment | 10 | 470 | c. Feed | R760-R765 | 6 |  |
L186 | consolidated segment | 10 | 471 | Total | R766-R771 | 6 |  |
L187 | consolidated segment | 10 | 472 | Less: i. Share of loss of an associate and a joint venture | R772-R777 | 6 | ZERO_STANDING(4 of 6 periods) |
L188 | consolidated segment | 10 | 473 | ii. Finance costs | R778-R783 | 6 |  |
L189 | consolidated segment | 10 | 474 | iii. Other un-allocable expenses | R784-R789 | 6 |  |
L190 | consolidated segment | 10 | 475 | Add: i. Interest income | R790-R795 | 6 |  |
L191 | consolidated segment | 10 | 476 | ii. Other un-allocable income | R796-R801 | 6 |  |
L192 | consolidated segment | 10 | 477 | Profit before tax | R802-R807 | 6 |  |
L193 | consolidated segment | 10 | 479 | a. Dairy | R808-R813 | 6 |  |
L194 | consolidated segment | 10 | 480 | b. Renewable energy | R814-R819 | 6 |  |
L195 | consolidated segment | 10 | 481 | c. Feed | R820-R825 | 6 |  |
L196 | consolidated segment | 10 | 482 | d. Unallocated | R826-R831 | 6 |  |
L197 | consolidated segment | 10 | 483 | Total | R832-R837 | 6 |  |
L198 | consolidated segment | 10 | 485 | a. Dairy | R838-R843 | 6 |  |
L199 | consolidated segment | 10 | 486 | b. Renewable energy | R844-R849 | 6 |  |
L200 | consolidated segment | 10 | 487 | c. Feed | R850-R855 | 6 |  |
L201 | consolidated segment | 10 | 488 | d. Unallocated | R856-R861 | 6 |  |
L202 | consolidated segment | 10 | 489 | Total | R862-R867 | 6 |  |
L203 | consolidated balance sheet | 11 | 503 | (a) Property, plant and equipment | R868-R869 | 2 |  |
L204 | consolidated balance sheet | 11 | 504 | (b) Right of use assets | R870-R871 | 2 |  |
L205 | consolidated balance sheet | 11 | 505 | (c) Capital work-in-progress | R872-R873 | 2 |  |
L206 | consolidated balance sheet | 11 | 506 | (d) Investment property | R874-R875 | 2 |  |
L207 | consolidated balance sheet | 11 | 507 | (e) Goodwill | R876-R877 | 2 |  |
L208 | consolidated balance sheet | 11 | 508 | (f) Other intangible assets | R878-R879 | 2 |  |
L209 | consolidated balance sheet | 11 | 509 | (g) Intangible assets under development | R880-R881 | 2 |  |
L210 | consolidated balance sheet | 11 | 511 | (i) Other investments | R882-R883 | 2 |  |
L211 | consolidated balance sheet | 11 | 512 | (ii) Other financial assets | R884-R885 | 2 |  |
L212 | consolidated balance sheet | 11 | 513 | (i) Other non-current assets | R886-R887 | 2 |  |
L213 | consolidated balance sheet | 11 | 514 | Total non-current assets | R888-R889 | 2 |  |
L214 | consolidated balance sheet | 11 | 516 | (a) Inventories | R890-R891 | 2 |  |
L215 | consolidated balance sheet | 11 | 518 | (i) Investments | R892-R893 | 2 |  |
L216 | consolidated balance sheet | 11 | 519 | (ii) Trade receivables | R894-R895 | 2 |  |
L217 | consolidated balance sheet | 11 | 520 | (iii) Cash and cash equivalents | R896-R897 | 2 |  |
L218 | consolidated balance sheet | 11 | 521 | (iv) Bank balances other than (iii) above | R898-R899 | 2 |  |
L219 | consolidated balance sheet | 11 | 522 | (v) Loans | R900-R901 | 2 | ZERO_STANDING(1 of 2 periods) |
L220 | consolidated balance sheet | 11 | 523 | (vi) Other financial assets | R902-R903 | 2 |  |
L221 | consolidated balance sheet | 11 | 524 | (c) Current tax assets (net) | R904-R905 | 2 |  |
L222 | consolidated balance sheet | 11 | 525 | (d) Other current assets | R906-R907 | 2 |  |
L223 | consolidated balance sheet | 11 | 526 | Total current assets | R908-R909 | 2 |  |
L224 | consolidated balance sheet | 11 | 527 | Total assets | R910-R911 | 2 |  |
L225 | consolidated balance sheet | 11 | 529 | (a) Equity share capital | R912-R913 | 2 |  |
L226 | consolidated balance sheet | 11 | 530 | (b) Other equity | R914-R915 | 2 |  |
L227 | consolidated balance sheet | 11 | 531 | Equity attributable to the owners of the company | R916-R917 | 2 |  |
L228 | consolidated balance sheet | 11 | 532 | Non-controlling interest | R918-R919 | 2 |  |
L229 | consolidated balance sheet | 11 | 533 | Total equity | R920-R921 | 2 |  |
L230 | consolidated balance sheet | 11 | 536 | (i) Borrowings | R922-R923 | 2 |  |
L231 | consolidated balance sheet | 11 | 537 | (ia) Lease liabilities | R924-R925 | 2 |  |
L232 | consolidated balance sheet | 11 | 538 | (b) Government grant | R926-R927 | 2 |  |
L233 | consolidated balance sheet | 11 | 539 | (c) Provisions | R928-R929 | 2 |  |
L234 | consolidated balance sheet | 11 | 540 | (d) Deferred tax liabilities (net) | R930-R931 | 2 |  |
L235 | consolidated balance sheet | 11 | 541 | (e) Other liabilities | R932-R933 | 2 |  |
L236 | consolidated balance sheet | 11 | 542 | Total non-current liabilities | R934-R935 | 2 |  |
L237 | consolidated balance sheet | 11 | 544 | (i) Borrowings | R936-R937 | 2 |  |
L238 | consolidated balance sheet | 11 | 545 | (ia) Lease liabilities | R938-R939 | 2 |  |
L239 | consolidated balance sheet | 11 | 547 | - total outstanding dues of micro and small enterprises; | R940-R941 | 2 |  |
L240 | consolidated balance sheet | 11 | 548 | - total outstanding dues of creditors other than micro and small enter | R942-R943 | 2 |  |
L241 | consolidated balance sheet | 11 | 549 | (iii) Other financial liabilities | R944-R945 | 2 |  |
L242 | consolidated balance sheet | 11 | 550 | (b) Other current liabilities | R946-R947 | 2 |  |
L243 | consolidated balance sheet | 11 | 551 | (c) Government grant | R948-R949 | 2 |  |
L244 | consolidated balance sheet | 11 | 552 | (d) Provisions | R950-R951 | 2 |  |
L245 | consolidated balance sheet | 11 | 553 | Total current liabilities | R952-R953 | 2 |  |
L246 | consolidated balance sheet | 11 | 554 | Total equity and liabilities | R954-R955 | 2 |  |
L247 | consolidated cash flow | 12 | 568 | Profit before tax | R956-R958 | 3 |  |
L248 | consolidated cash flow | 12 | 570 | Depreciation and amortization expense | R959-R961 | 3 |  |
L249 | consolidated cash flow | 12 | 571 | Impairment losses on assets | R962-R964 | 3 | ZERO_STANDING(2 of 3 periods) |
L250 | consolidated cash flow | 12 | 572 | Provision for doubtful advances | R965-R967 | 3 | ZERO_STANDING(2 of 3 periods) |
L251 | consolidated cash flow | 12 | 573 | Share of loss of an associate and a joint venture | R968-R970 | 3 | ZERO_STANDING(1 of 3 periods) |
L252 | consolidated cash flow | 12 | 574 | Provision for doubtful debts and bad debts written off | R971-R973 | 3 |  |
L253 | consolidated cash flow | 12 | 575 | Amortisation of government grants | R974-R976 | 3 |  |
L254 | consolidated cash flow | 12 | 576 | Property, plant and equipment written off | R977-R979 | 3 |  |
L255 | consolidated cash flow | 12 | 577 | Profit on sale of Property, plant and equipment ("PPE") | R980-R982 | 3 |  |
L256 | consolidated cash flow | 12 | 578 | Provisions no longer required/ credit balances written back | R983-R985 | 3 |  |
L257 | consolidated cash flow | 12 | 579 | Gain on investments | R986-R988 | 3 |  |
L258 | consolidated cash flow | 12 | 580 | Interest income | R989-R991 | 3 |  |
L259 | consolidated cash flow | 12 | 581 | Interest expenses | R992-R994 | 3 |  |
L260 | consolidated cash flow | 12 | 582 | Advances written off | R995-R997 | 3 |  |
L261 | consolidated cash flow | 12 | 583 | Dividend income | R998-R1000 | 3 |  |
L262 | consolidated cash flow | 12 | 584 | Lease rental income | R1001-R1003 | 3 |  |
L263 | consolidated cash flow | 12 | 585 | Operating profits before working capital changes | R1004-R1006 | 3 |  |
L264 | consolidated cash flow | 12 | 586 | Changes in inventories | R1007-R1009 | 3 |  |
L265 | consolidated cash flow | 12 | 587 | Changes in trade receivables | R1010-R1012 | 3 |  |
L266 | consolidated cash flow | 12 | 588 | Changes in other assets | R1013-R1015 | 3 |  |
L267 | consolidated cash flow | 12 | 589 | Changes in other financial assets | R1016-R1018 | 3 |  |
L268 | consolidated cash flow | 12 | 590 | Changes in trade payables | R1019-R1021 | 3 |  |
L269 | consolidated cash flow | 12 | 591 | Changes in provisions | R1022-R1024 | 3 |  |
L270 | consolidated cash flow | 12 | 592 | Changes in other financial liabilities | R1025-R1027 | 3 |  |
L271 | consolidated cash flow | 12 | 593 | Changes in other liabilities | R1028-R1030 | 3 |  |
L272 | consolidated cash flow | 12 | 594 | Cash generated from operating activities | R1031-R1033 | 3 |  |
L273 | consolidated cash flow | 12 | 595 | Income-taxes paid, net | R1034-R1036 | 3 |  |
L274 | consolidated cash flow | 12 | 596 | Net cash generated from operating activities (A) | R1037-R1039 | 3 |  |
L275 | consolidated cash flow | 12 | 598 | Purchase of PPE and other intangible assets, including CWIP | R1040-R1042 | 3 |  |
L276 | consolidated cash flow | 12 | 599 | Proceeds from sale of PPE | R1043-R1045 | 3 |  |
L277 | consolidated cash flow | 12 | 600 | Investment in a Subsidiaries | R1046-R1048 | 3 | ZERO_STANDING(1 of 3 periods) |
L278 | consolidated cash flow | 12 | 601 | Receipts of government grants | R1049-R1051 | 3 | ZERO_STANDING(1 of 3 periods) |
L279 | consolidated cash flow | 12 | 602 | Purchase of investments | R1052-R1054 | 3 |  |
L280 | consolidated cash flow | 12 | 603 | Proceeds from sale of investments | R1055-R1057 | 3 |  |
L281 | consolidated cash flow | 12 | 604 | Interest received | R1058-R1060 | 3 |  |
L282 | consolidated cash flow | 12 | 605 | Movement in other bank balances, net | R1061-R1063 | 3 |  |
L283 | consolidated cash flow | 12 | 606 | Rent received | R1064-R1066 | 3 |  |
L284 | consolidated cash flow | 12 | 607 | Dividend received | R1067-R1069 | 3 |  |
L285 | consolidated cash flow | 12 | 608 | Net cash used in investing activities (B) | R1070-R1072 | 3 |  |
L286 | consolidated cash flow | 12 | 610 | Proceeds from long term borrowings | R1073-R1075 | 3 |  |
L287 | consolidated cash flow | 12 | 611 | Repayment of long term borrowings | R1076-R1078 | 3 |  |
L288 | consolidated cash flow | 12 | 612 | Proceeds from/(Repayment of) short term borrowings, net | R1079-R1081 | 3 | ZERO_STANDING(1 of 3 periods) |
L289 | consolidated cash flow | 12 | 613 | Interest paid | R1082-R1084 | 3 |  |
L290 | consolidated cash flow | 12 | 614 | Lease rentals paid | R1085-R1087 | 3 |  |
L291 | consolidated cash flow | 12 | 615 | Dividend paid, net | R1088-R1090 | 3 |  |
L292 | consolidated cash flow | 12 | 616 | Net cash generated from / (used in) financing activities (C) | R1091-R1093 | 3 |  |
L293 | consolidated cash flow | 12 | 617 | Net Change in cash and cash equivalents during the period/ year (A + B | R1094-R1096 | 3 |  |
L294 | consolidated cash flow | 12 | 618 | Cash and cash equivalents at the beginning of the year | R1097-R1099 | 3 |  |
L295 | consolidated cash flow | 12 | 619 | Cash and cash equivalents at the end of the year (Note 1) | R1100-R1102 | 3 |  |
L296 | consolidated cash flow | 12 | 621 | Cash on hand | R1103-R1105 | 3 |  |
L297 | consolidated cash flow | 12 | 622 | Balances with banks in current accounts | R1106-R1108 | 3 |  |
L298 | consolidated cash flow | 12 | 623 | Deposits with original maturity up to 3 months | R1109-R1111 | 3 | ZERO_STANDING(all periods) |
L299 | consolidated cash flow | 12 | 624 | (total) | R1112-R1114 | 3 |  |

## STANDING ZERO / DASH ROWS (itemised)
ROW ID | page | line | A2 flags | item
R055 | 2 | 85 | ZERO_STANDING | standalone P&L: g. Impairment losses, Q 30.09.2026
R056 | 2 | 85 | ZERO_STANDING | standalone P&L: g. Impairment losses, Q 30.06.2026
R057 | 2 | 85 | ZERO_STANDING | standalone P&L: g. Impairment losses, Q 30.09.2025
R058 | 2 | 85 | ZERO_STANDING | standalone P&L: g. Impairment losses, 6M 30.09.2026
R059 | 2 | 85 | ZERO_STANDING | standalone P&L: g. Impairment losses, 6M 30.09.2025
R079 | 2 | 89 | ZERO_STANDING | standalone P&L: 4 Exceptional items [refer note 4], Q 30.09.2026
R080 | 2 | 89 | ZERO_STANDING | standalone P&L: 4 Exceptional items [refer note 4], Q 30.06.2026
R082 | 2 | 89 | ZERO_STANDING | standalone P&L: 4 Exceptional items [refer note 4], 6M 30.09.2026
R121 | 2 | 99 | ZERO_STANDING | standalone P&L: (b) Items that will be reclassified to profit or loss, Q 30.09.2026
R122 | 2 | 99 | ZERO_STANDING | standalone P&L: (b) Items that will be reclassified to profit or loss, Q 30.06.2026
R123 | 2 | 99 | ZERO_STANDING | standalone P&L: (b) Items that will be reclassified to profit or loss, Q 30.09.2025
R124 | 2 | 99 | ZERO_STANDING | standalone P&L: (b) Items that will be reclassified to profit or loss, 6M 30.09.2026
R125 | 2 | 99 | ZERO_STANDING | standalone P&L: (b) Items that will be reclassified to profit or loss, 6M 30.09.2025
R126 | 2 | 99 | ZERO_STANDING | standalone P&L: (b) Items that will be reclassified to profit or loss, FY 31.03.2026
R366 | 5 | 224 | ZERO_STANDING | standalone cash flow: Impairment losses on assets, 6M 30.09.2026
R367 | 5 | 224 | ZERO_STANDING | standalone cash flow: Impairment losses on assets, 6M 30.09.2025
R369 | 5 | 225 | ZERO_STANDING | standalone cash flow: Impairment losses on investments, 6M 30.09.2026
R370 | 5 | 225 | ZERO_STANDING | standalone cash flow: Impairment losses on investments, 6M 30.09.2025
R457 | 5 | 256 | ZERO_STANDING | standalone cash flow: Receipts of government grants, 6M 30.09.2025
R487 | 5 | 267 | ZERO_STANDING | standalone cash flow: Proceeds from/(Repayment of) short term borrowings, net, 6M 30.09.2025
R573 | 9 | 417 | ZERO_STANDING | consolidated P&L: g. Impairment losses, Q 30.09.2026
R574 | 9 | 417 | ZERO_STANDING | consolidated P&L: g. Impairment losses, Q 30.06.2026
R575 | 9 | 417 | ZERO_STANDING | consolidated P&L: g. Impairment losses, Q 30.09.2025
R576 | 9 | 417 | ZERO_STANDING | consolidated P&L: g. Impairment losses, 6M 30.09.2026
R577 | 9 | 417 | ZERO_STANDING | consolidated P&L: g. Impairment losses, 6M 30.09.2025
R597 | 9 | 421 | ZERO_STANDING | consolidated P&L: 4 Share of loss of an associate and a joint venture, Q 30.09.2026
R598 | 9 | 421 | ZERO_STANDING | consolidated P&L: 4 Share of loss of an associate and a joint venture, Q 30.06.2026
R599 | 9 | 421 | ZERO_STANDING | consolidated P&L: 4 Share of loss of an associate and a joint venture, Q 30.09.2025
R600 | 9 | 421 | ZERO_STANDING | consolidated P&L: 4 Share of loss of an associate and a joint venture, 6M 30.09.2026
R609 | 9 | 423 | ZERO_STANDING | consolidated P&L: 6 Exceptional items (refer note 4), Q 30.09.2026
R610 | 9 | 423 | ZERO_STANDING | consolidated P&L: 6 Exceptional items (refer note 4), Q 30.06.2026
R612 | 9 | 423 | ZERO_STANDING | consolidated P&L: 6 Exceptional items (refer note 4), 6M 30.09.2026
R651 | 9 | 433 | ZERO_STANDING | consolidated P&L: (b) Items that will be reclassified to profit or loss, Q 30.09.2026
R652 | 9 | 433 | ZERO_STANDING | consolidated P&L: (b) Items that will be reclassified to profit or loss, Q 30.06.2026
R653 | 9 | 433 | ZERO_STANDING | consolidated P&L: (b) Items that will be reclassified to profit or loss, Q 30.09.2025
R654 | 9 | 433 | ZERO_STANDING | consolidated P&L: (b) Items that will be reclassified to profit or loss, 6M 30.09.2026
R655 | 9 | 433 | ZERO_STANDING | consolidated P&L: (b) Items that will be reclassified to profit or loss, 6M 30.09.2025
R656 | 9 | 433 | ZERO_STANDING | consolidated P&L: (b) Items that will be reclassified to profit or loss, FY 31.03.2026
R687 | 9 | 441 | ZERO_STANDING | consolidated P&L: - Other comprehensive loss, Q 30.09.2026
R688 | 9 | 441 | ZERO_STANDING | consolidated P&L: - Other comprehensive loss, Q 30.06.2026
R689 | 9 | 441 | ZERO_STANDING | consolidated P&L: - Other comprehensive loss, Q 30.09.2025
R690 | 9 | 441 | ZERO_STANDING | consolidated P&L: - Other comprehensive loss, 6M 30.09.2026
R691 | 9 | 441 | ZERO_STANDING | consolidated P&L: - Other comprehensive loss, 6M 30.09.2025
R692 | 9 | 441 | ZERO_STANDING | consolidated P&L: - Other comprehensive loss, FY 31.03.2026
R772 | 10 | 472 | ZERO_STANDING | consolidated segment: Less: i. Share of loss of an associate and a joint venture, Q 30.09.2026
R773 | 10 | 472 | ZERO_STANDING | consolidated segment: Less: i. Share of loss of an associate and a joint venture, Q 30.06.2026
R774 | 10 | 472 | ZERO_STANDING | consolidated segment: Less: i. Share of loss of an associate and a joint venture, Q 30.09.2025
R775 | 10 | 472 | ZERO_STANDING | consolidated segment: Less: i. Share of loss of an associate and a joint venture, 6M 30.09.2026
R901 | 11 | 522 | ZERO_STANDING | consolidated balance sheet: (v) Loans, 31.03.2026
R962 | 12 | 571 | ZERO_STANDING | consolidated cash flow: Impairment losses on assets, 6M 30.09.2026
R963 | 12 | 571 | ZERO_STANDING | consolidated cash flow: Impairment losses on assets, 6M 30.09.2025
R965 | 12 | 572 | ZERO_STANDING | consolidated cash flow: Provision for doubtful advances, 6M 30.09.2026
R966 | 12 | 572 | ZERO_STANDING | consolidated cash flow: Provision for doubtful advances, 6M 30.09.2025
R968 | 12 | 573 | ZERO_STANDING | consolidated cash flow: Share of loss of an associate and a joint venture, 6M 30.09.2026
R1046 | 12 | 600 | ZERO_STANDING | consolidated cash flow: Investment in a Subsidiaries, 6M 30.09.2026
R1050 | 12 | 601 | ZERO_STANDING | consolidated cash flow: Receipts of government grants, 6M 30.09.2025
R1080 | 12 | 612 | ZERO_STANDING | consolidated cash flow: Proceeds from/(Repayment of) short term borrowings, net, 6M 30.09.2025
R1109 | 12 | 623 | ZERO_STANDING | consolidated cash flow: Deposits with original maturity up to 3 months, 6M 30.09.2026
R1110 | 12 | 623 | ZERO_STANDING | consolidated cash flow: Deposits with original maturity up to 3 months, 6M 30.09.2025
R1111 | 12 | 623 | ZERO_STANDING | consolidated cash flow: Deposits with original maturity up to 3 months, FY 31.03.2026

## OTHER NUMBER ROWS (non-table: reference numbers, times, note amounts, UDIN, subsidiary figures)
ROW ID | page | line | category | A2 flags | note
R1115 | 1 | 20 | letter identifiers |  |
R1116 | 1 | 29 | letter identifiers |  |
R1117 | 1 | 45 | agenda/board time | BOARD_DURATION (11:30-14:50 = 3h20m) |
R1118 | 1 | 46 | agenda/board time | BOARD_DURATION (11:30-14:50 = 3h20m) |
R1119 | 1 | 61 | auditor/signature identifiers |  |
R1120 | 6 | 296 | note 4 amounts |  |
R1121 | 6 | 296 | note 4 amounts |  |
R1122 | 6 | 297 | note 4 amounts |  |
R1123 | 6 | 299 | note 4 amounts |  |
R1124 | 6 | 304 | letter identifiers |  |
R1125 | 8 | 376 | auditor/signature identifiers |  |
R1126 | 8 | 386 | auditor/signature identifiers |  |
R1127 | 8 | 385 | auditor/signature identifiers |  |
R1128 | 13 | 642 | note 4 amounts |  |
R1129 | 13 | 642 | note 4 amounts |  |
R1130 | 13 | 644 | note 4 amounts |  |
R1131 | 15 | 722 | auditor para / unreviewed subsidiary | MGMT_FURNISHED |
R1132 | 15 | 723 | auditor para / unreviewed subsidiary | MGMT_FURNISHED |
R1133 | 15 | 723 | auditor para / unreviewed subsidiary | MGMT_FURNISHED |
R1134 | 15 | 723 | auditor para / unreviewed subsidiary | MGMT_FURNISHED |
R1135 | 15 | 724 | auditor para / unreviewed subsidiary | MGMT_FURNISHED |
R1136 | 15 | 724 | auditor para / unreviewed subsidiary | MGMT_FURNISHED |
R1137 | 15 | 724 | auditor para / unreviewed subsidiary | MGMT_FURNISHED |
R1138 | 15 | 725 | auditor para / unreviewed subsidiary | MGMT_FURNISHED |
R1139 | 15 | 748 | auditor/signature identifiers |  |
R1140 | 2 | 101 | P&L footnote |  |
R1141 | 9 | 443 | P&L footnote |  |

## NOTES (numbered notes and footnotes)
ROW ID | page | line | A2 flags | cross-ref
R1205 | 5 | 275 |  | 
R1206 | 6 | 287 |  | 
R1207 | 6 | 289 |  | 
R1208 | 6 | 293 |  | 
R1209 | 6 | 296 | RESTATED | amounts R1120,R1121,R1122; restated consolidated at R1228 (RESTATED)
R1210 | 6 | 299 |  | amount R1123; consolidated Note 4 R1228 does not carry 4b impairment text in A1 row (note for A3)
R1224 | 12 | 620 |  | 
R1225 | 13 | 633 |  | 
R1226 | 13 | 635 |  | 
R1227 | 13 | 639 |  | 
R1228 | 13 | 642 | RESTATED | amounts R1128-R1130; RESTATED of R1209
R1229 | 13 | 645 |  | effective date R1188; ENTITY R1162

## FOOTNOTES, QUALIFIERS, UNIT/STATUS LABELS, FIDELITY ROWS (unnumbered)
ROW ID | page | line | A2 flags | cross-ref
R1193 | 1 | 38 |  |
R1194 | 2 | 71 |  |
R1195 | 2 | 72 |  |
R1196 | 2 | 105 | EPS_NOT_ANNUALISED |
R1197 | 2 | 104 |  |
R1198 | 2 | 89 | POINTER_TO_NOTE4 |
R1199 | 3 | 115 |  |
R1200 | 3 | 116 |  |
R1201 | 4 | 152 |  |
R1202 | 4 | 153 |  |
R1203 | 5 | 217 |  |
R1204 | 5 | 218 |  |
R1211 | 7 | 348 | AUDITOR_PARA |
R1212 | 8 | 364 | AUDITOR_PARA |
R1213 | 9 | 403 |  |
R1214 | 9 | 404 |  |
R1215 | 9 | 447 | EPS_NOT_ANNUALISED |
R1216 | 9 | 446 |  |
R1217 | 9 | 423 | POINTER_TO_NOTE4 |
R1218 | 10 | 457 |  |
R1219 | 10 | 458 |  |
R1220 | 11 | 499 |  |
R1221 | 11 | 500 |  |
R1222 | 12 | 564 |  |
R1223 | 12 | 565 |  |
R1230 | 14 | 695 | AUDITOR_PARA |
R1231 | 14 | 702 | AUDITOR_PARA |
R1232 | 15 | 713 | AUDITOR_PARA |
R1233 | 15 | 721 | AUDITOR_PARA |
R1234 | 15 | 729 | AUDITOR_PARA |
R1235 | 15 | 732 | AUDITOR_PARA |
R1236 | 16 | 764 |  |
R1237 | 2 | 66 |  |
R1238 | 12 | 561 | FOOTNOTE_UNRESOLVED; IMAGE_PARTIAL |
R1239 | 12 | 561 | FOOTNOTE_UNRESOLVED; IMAGE_PARTIAL |
R1240 | 12 | 561 | FOOTNOTE_UNRESOLVED; IMAGE_PARTIAL |
R1241 | 5 | 214 | FOOTNOTE_UNRESOLVED; IMAGE_PARTIAL |
R1242 | 10 | 454 | SIGN_CONVENTION |

## AGENDA ITEMS / BOARD OUTCOME LETTER
A1 holds only the results item and timings; no other agenda items (AR approval, AGM, dividend, directors, auditors, ESOP) exist in the structured file. Rows: R1117 start, R1118 end, R1170 meeting date, R1171 earlier letter date, R1172 results period, R1176/R1181 board approval, R1206/R1225 note 1 approval statements, R1146 CS, R1185 CS signature, R1115 letter ref, R1116/R1144 scrip codes.
SIGNATURE CHECK: CS digital signature R1185 at 14:59:25 is after board conclusion R1118 at 14:50 (ok). Auditor signature R1184 at 13:04:00 and R1191 at 13:05:27 are BEFORE board conclusion 14:50 and before 15 Oct board meeting start? Meeting began 11:30, so review reports were signed mid-meeting; flag AUDITOR_SIGNED_BEFORE_BOARD_CONCLUSION (information, not breach).

## AUDITOR REPORT PARAGRAPHS
ROW ID | para | flags
R1148 | limited review engagement (entity) | 
R1158 | Walker Chandiok & Co LLP | 
R1159 | audit partner Sumesh E S | 
R1125 | FRN | 
R1127 | membership no | 
R1126 | UDIN standalone | 
R1139 | UDIN consolidated | 
R1183 | standalone report date | 
R1192 | consolidated report date | 
R1184 | standalone signature timestamp | 
R1191 | consolidated signature timestamp | 
R1182 | standalone review period | 
R1190 | consolidated review period | 
R1211 | standalone scope limitation (SRE 2410) | 
R1212 | standalone conclusion unmodified | 
R1230 | consolidated scope limitation | 
R1231 | consolidated Reg 33(8) procedures | 
R1232 | consolidated conclusion unmodified | 
R1233 | Other Matter: unreviewed subsidiary | UNREVIEWED_SUBSIDIARY
R1234 | materiality statement by management | 
R1235 | non-modification | 
R1131 | sub total assets | 
R1132 | sub revenue Q | 
R1133 | sub revenue 6M | 
R1134 | sub NLAT Q | 
R1135 | sub NLAT 6M | 
R1136 | sub TCI Q | 
R1137 | sub TCI 6M | 
R1138 | sub net cash outflow | 
R1168 | unreviewed subsidiary entity | UNREVIEWED_SUBSIDIARY
Going Concern / Emphasis of Matter: none in A1 rows (conclusions unmodified; unreviewed subsidiary is an Other Matter).

## ENTITIES
ROW ID | page | line | relationship | A2 flags
R1142 | 1 | 24 | stock exchange addressee | 
R1143 | 1 | 25 | stock exchange addressee | 
R1144 | 1 | 29 | NSE scrip code | 
R1145 | 1 | 51 | issuer / registrant | 
R1146 | 1 | 53 | company secretary and compliance officer | 
R1147 | 1 | 39 | reviewed and recommended results | 
R1148 | 1 | 41 | limited review of results | 
R1149 | 2 | 69 | company CIN | 
R1150 | 3 | 114 | reportable segment standalone | 
R1151 | 3 | 120 | reportable segment | 
R1152 | 6 | 293 | segment evaluator, note 3 | 
R1153 | 6 | 294 | reportable segment, note 3 | 
R1154 | 6 | 294 | reportable segment, note 3 | 
R1155 | 6 | 299 | investee, impairment provision (formerly Heritage Novandie Foods Private Limited) | NAME_CHANGE (formerly Private Limited)
R1156 | 6 | 297 | product in GST refund | 
R1157 | 6 | 302 | Vice Chairperson and Managing Director | 
R1158 | 7 | 312 | statutory auditor | 
R1159 | 8 | 383 | audit partner | 
R1160 | 10 | 463 | reportable segment consolidated | 
R1161 | 13 | 640 | reportable segment, note 3 consolidated | 
R1162 | 13 | 645 | controlling interest acquired, previously a joint venture | ENTITY_CHANGE? Novandie JV to subsidiary 16 Jun 2025 (R1188,R1229); prior ledger ND
R1163 | 14 | 679 | consolidating parent | 
R1164 | 16 | 767 | subsidiary | 
R1165 | 16 | 768 | subsidiary | ENTITY_CHANGE? Novandie JV to subsidiary 16 Jun 2025 (R1188,R1229); prior ledger ND
R1166 | 16 | 769 | subsidiary | 
R1167 | 16 | 772 | associate | 
R1168 | 15 | 721 | subsidiary results not reviewed by its auditors | UNREVIEWED_SUBSIDIARY unnamed
R1169 | 2 | 109 | certification line in page footer (repeats pages 3-6, 9-13) | 
Consolidation list (Annexure 1): R1164,R1165,R1166 subsidiaries; R1167 associate; R1163 holding.

## DATES
ROW ID | page | line | note
R1170 | 1 | 20 | letter / board meeting date
R1171 | 1 | 35 | earlier continuation letter date
R1172 | 1 | 38 | results period
R1173 | 2 | 72 | standalone P&L column period ends
R1174 | 4 | 151 | standalone balance sheet dates
R1175 | 5 | 216 | cash flow periods
R1176 | 6 | 287 | board approval date
R1177 | 6 | 296 | note 4 period
R1178 | 6 | 287 | note 4 period
R1179 | 6 | 298 | interest reversal quarter
R1180 | 6 | 299 | impairment provision period
R1181 | 6 | 288 | signing date
R1182 | 7 | 333 | year to date review period
R1183 | 8 | 388 | auditor report date
R1184 | 8 | 380 | auditor digital signature timestamp
R1185 | 1 | 55 | CS digital signature timestamp
R1186 | 10 | 458 | consolidated segment column period ends
R1187 | 11 | 498 | consolidated balance sheet dates
R1188 | 13 | 645 | effective date of control of Heritage Novandie Foods Limited
R1189 | 13 | 634 | board approval date, consolidated
R1190 | 14 | 680 | consolidated YTD review period
R1191 | 15 | 742 | auditor digital signature timestamp
R1192 | 15 | 751 | consolidated auditor report date

## FORWARD STATEMENTS: none (0 rows in A1).

## MISSING_FROM_STRUCTURED: none found. Observation: no Board Outcome agenda items beyond results, no director profiles, in A1.
