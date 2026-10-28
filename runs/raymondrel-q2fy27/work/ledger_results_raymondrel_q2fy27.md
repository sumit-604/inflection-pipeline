# LEDGER: results RAYMONDREL Q2 FY27 (A2 ENUMERATOR)
# Source: A1 structured extraction, runs/raymondrel-q2fy27/extracted/raymondrel-results-q2fy27-structured.md. Row IDs reference A1 rows; verbatim values stay there.

=== A2 COUNT TEST ===
category: structured_rows   grep_count: 874 (header says 874)   sweep_count: 874   match: yes (NUMBER 698 / ENTITY 50 / FORWARD 12 / DATE 39 / QUALIFIER 75 equal header counts: True)
category: notes             grep_count: 13 (10 numbered p6+p12, 2 indirect-method CF notes, 1 asterisk footnote)   sweep_count: 13 (N01-N13)   match: yes
category: line_items        grep_count: 184 (distinct page+line, NUMBER rows, statement pages 3,4,5,9,10,11)   sweep_count: 184   match: yes
category: zero_standing     grep_count: 48 ZERO_STANDING rows in structured   sweep_count: 48 cells on 23 line items (1 zero in every period)   match: yes
category: agenda_items      grep_count: 3 (numbered enclosures in Board Outcome letter)   sweep_count: 3 (B-A1..B-A3)   match: yes
category: auditor_paras     grep_count: 11 (4 standalone + 5 numbered consolidated + Further + conclusion-not-modified)   sweep_count: 11   match: yes
category: entities          grep_count: 7 (Annexure 1 numbered subsidiaries)   sweep_count: 7 subsidiaries + 1 holding = 8 in scope   match: yes
category: turns / questions / mgmt_numbers / slides: not applicable (results filing)
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 874 | ids_referenced_in_ledger: 874 | orphan_ids: [] | match: yes

Flag key: ZERO_STANDING | ENTITY_CHANGE | RESTATED | OCR_UNCERTAIN | OCR_UNREADABLE | MISSING_FROM_STRUCTURED | FWD | PR (press release, Rs Cr) | NO_TIMESTAMP
Units: statements Rs Lakhs; press release Rs Cr. IDs are A1 row IDs; L = fulltext line anchor.

## 1. NOTES LEDGER (13)
| # | ROW IDs | category | A2 flags | cross-ref / materiality |
|---|---|---|---|---|
| N01 | R821 | standalone Note 1 (basis of preparation, p6) |  |  |
| N02 | R712,R773,R822 | standalone Note 2 (Audit Committee review, Board approval, limited review, p6) |  | board date also R763 |
| N03 | R305,R713,R823 | standalone Note 3 (single segment Real Estate, Ind AS 108, p6) | RESTATED | same as N08 |
| N04 | R306-R308,R774-R775,R824 | standalone Note 4 (final dividend Rs 2/share, AGM 14 Jul 2026, paid same day, p6) | RESTATED | same as N09; dividend paid also in CF R287-R288 and R586-R587 |
| N05 | R825 | standalone Note 5 (regrouping of prior periods, p6) |  | no demerger or restatement note in document (A1 header) |
| N06 | R850 | consolidated Note 1 (basis, p12) |  |  |
| N07 | R726,R783,R851 | consolidated Note 2 (review/approval, p12) |  |  |
| N08 | R604,R852 | consolidated Note 3 (single segment, p12) | RESTATED | same as N03 |
| N09 | R605-R606,R784,R853 | consolidated Note 4 (dividend, p12) | RESTATED | same as N04 |
| N10 | R854 | consolidated Note 5 (regrouping, p12) |  |  |
| N11 | R820 | standalone CF indirect-method note (Ind AS 7, p5 L304) | | none |
| N12 | R849 | consolidated CF indirect-method note (Ind AS 7, p11 L596) | | none |
| N13 | R818,R819 | standalone CF asterisk footnote "amount below rounding convention" (marker on Loss on disposal of PPE, R245-R246, p5 L268/L303) | | RESOLVED (R819 pairs R818); no FOOTNOTE_UNRESOLVED |
No demerger, exceptional-item, contingent-liability, related-party or EPS-adjustment note exists in this document (A1 header).

## 2. LINE-ITEM LEDGER (every statement line, incl. zero/nil/dash)
| ID# | table | L | ROW IDs | line item | A2 flags | note |
|---|---|---|---|---|---|---|
| L001 | Standalone P&L p3 | 167 | R028-R033 | a) Revenue from operations |  |  |
| L002 | Standalone P&L p3 | 168 | R034-R039 | b) Other income |  |  |
| L003 | Standalone P&L p3 | 169 | R040-R045 | Total income |  |  |
| L004 | Standalone P&L p3 | 172 | R046-R051 | a) Cost of land, development of properties, construction and |  |  |
| L005 | Standalone P&L p3 | 174 | R052-R057 | b) Changes in inventories of properties under development an |  |  |
| L006 | Standalone P&L p3 | 175 | R058-R063 | c) Employee benefits expense |  |  |
| L007 | Standalone P&L p3 | 176 | R064-R069 | d) Finance costs |  |  |
| L008 | Standalone P&L p3 | 177 | R070-R075 | e) Depreciation and amortisation expenses |  |  |
| L009 | Standalone P&L p3 | 178 | R076-R081 | f) Other expenses |  |  |
| L010 | Standalone P&L p3 | 179 | R082-R087 | Total expenses |  |  |
| L011 | Standalone P&L p3 | 180 | R088-R093 | 3 Profit before tax for the period / year (1-2) |  |  |
| L012 | Standalone P&L p3 | 182 | R094-R099 | Current tax |  |  |
| L013 | Standalone P&L p3 | 183 | R100-R105 | Deferred tax |  |  |
| L014 | Standalone P&L p3 | 184 | R106-R111 | Total tax expense |  |  |
| L015 | Standalone P&L p3 | 185 | R112-R117 | 5 Profit for the period / year (3-4) |  |  |
| L016 | Standalone P&L p3 | 188 | R118-R123 | Remeasurement of defined benefit plan | ZERO_STANDING (5 of 6 cells) |  |
| L017 | Standalone P&L p3 | 189 | R124-R129 | Income tax relating to above item | ZERO_STANDING (5 of 6 cells) |  |
| L018 | Standalone P&L p3 | 190 | R130-R135 | Total other comprehensive income (net of tax) | ZERO_STANDING (5 of 6 cells) |  |
| L019 | Standalone P&L p3 | 192 | R136-R141 | 7 Total comprehensive income for the period / year (5-6) |  |  |
| L020 | Standalone P&L p3 | 194 | R142-R147 | 8 Paid-up equity share capital (Face value of Rs 10 per shar |  |  |
| L021 | Standalone P&L p3 | 195 | R148 | Other equity, FY26 (year 31.03.2026) only |  | year-end only (FY26) |
| L022 | Standalone P&L p3 | 197 | R149-R154 | Basic |  |  |
| L023 | Standalone P&L p3 | 198 | R155-R160 | Diluted |  |  |
| L024 | Standalone Balance Sheet p4 | 207 | R161-R162 | (a) Property, plant and equipment |  |  |
| L025 | Standalone Balance Sheet p4 | 208 | R163-R164 | (b) Capital work-in-progress |  |  |
| L026 | Standalone Balance Sheet p4 | 209 | R165-R166 | (c) Intangible assets |  |  |
| L027 | Standalone Balance Sheet p4 | 211 | R167-R168 | (i) Investments |  |  |
| L028 | Standalone Balance Sheet p4 | 212 | R169-R170 | (ii) Loans |  |  |
| L029 | Standalone Balance Sheet p4 | 213 | R171-R172 | (iii) Other financial assets |  |  |
| L030 | Standalone Balance Sheet p4 | 214 | R173-R174 | (e) Deferred tax assets (net) |  |  |
| L031 | Standalone Balance Sheet p4 | 215 | R175-R176 | (f) Non-current tax assets (net) | ZERO_STANDING (1 of 2 cells) |  |
| L032 | Standalone Balance Sheet p4 | 216 | R177-R178 | (g) Other non-current assets (net) |  |  |
| L033 | Standalone Balance Sheet p4 | 217 | R179-R180 | Total non-current assets |  |  |
| L034 | Standalone Balance Sheet p4 | 219 | R181-R182 | (a) Inventories |  |  |
| L035 | Standalone Balance Sheet p4 | 221 | R183-R184 | (i) Investments | ZERO_STANDING (1 of 2 cells) |  |
| L036 | Standalone Balance Sheet p4 | 222 | R185-R186 | (ii) Trade receivables |  |  |
| L037 | Standalone Balance Sheet p4 | 223 | R187-R188 | (iii) Cash and cash equivalents |  |  |
| L038 | Standalone Balance Sheet p4 | 224 | R189-R190 | (iv) Bank balances other than cash and cash equivalents |  |  |
| L039 | Standalone Balance Sheet p4 | 225 | R191-R192 | (v) Loans |  |  |
| L040 | Standalone Balance Sheet p4 | 226 | R193-R194 | (vi) Others financial assets |  |  |
| L041 | Standalone Balance Sheet p4 | 227 | R195-R196 | (c) Other current assets |  |  |
| L042 | Standalone Balance Sheet p4 | 228 | R197-R198 | Total current assets |  |  |
| L043 | Standalone Balance Sheet p4 | 229 | R199-R200 | TOTAL ASSETS |  |  |
| L044 | Standalone Balance Sheet p4 | 232 | R201-R202 | a) Equity share capital |  |  |
| L045 | Standalone Balance Sheet p4 | 233 | R203-R204 | b) Other equity |  |  |
| L046 | Standalone Balance Sheet p4 | 234 | R205-R206 | Total equity |  |  |
| L047 | Standalone Balance Sheet p4 | 238 | R207-R208 | (i) Borrowings |  |  |
| L048 | Standalone Balance Sheet p4 | 239 | R209-R210 | (b) Provisions |  |  |
| L049 | Standalone Balance Sheet p4 | 240 | R211-R212 | Total non-current liabilities |  |  |
| L050 | Standalone Balance Sheet p4 | 243 | R213-R214 | (i) Borrowings |  |  |
| L051 | Standalone Balance Sheet p4 | 245 | R215-R216 | Total outstanding dues of micro enterprises and small enterp |  |  |
| L052 | Standalone Balance Sheet p4 | 246 | R217-R218 | Total outstanding dues of creditors other than micro enterpr |  |  |
| L053 | Standalone Balance Sheet p4 | 247 | R219-R220 | (iii) Other financial liabilities |  |  |
| L054 | Standalone Balance Sheet p4 | 248 | R221-R222 | (b) Other current liabilities |  |  |
| L055 | Standalone Balance Sheet p4 | 249 | R223-R224 | (c) Provisions |  |  |
| L056 | Standalone Balance Sheet p4 | 250 | R225-R226 | (d) Current tax liabilities | ZERO_STANDING (1 of 2 cells) |  |
| L057 | Standalone Balance Sheet p4 | 251 | R227-R228 | Total current liabilities |  |  |
| L058 | Standalone Balance Sheet p4 | 252 | R229-R230 | Total liabilities |  |  |
| L059 | Standalone Balance Sheet p4 | 253 | R231-R232 | TOTAL EQUITY AND LIABILITIES |  |  |
| L060 | Standalone Cash Flow p5 | 261 | R233-R234 | Profit before tax |  |  |
| L061 | Standalone Cash Flow p5 | 263 | R235-R236 | Depreciation and amortisation expenses |  |  |
| L062 | Standalone Cash Flow p5 | 264 | R237-R238 | Finance costs |  |  |
| L063 | Standalone Cash Flow p5 | 265 | R239-R240 | Interest income |  |  |
| L064 | Standalone Cash Flow p5 | 266 | R241-R242 | Gain on sale of investments (net) | ZERO_STANDING (1 of 2 cells) |  |
| L065 | Standalone Cash Flow p5 | 267 | R243-R244 | Fair value gain on financial assets measured at fair value t |  |  |
| L066 | Standalone Cash Flow p5 | 268 | R245-R246 | Loss on disposal of property, plant and equipment (net)* | ZERO_STANDING (all periods) |  |
| L067 | Standalone Cash Flow p5 | 269 | R247-R248 | Share based payment expense |  |  |
| L068 | Standalone Cash Flow p5 | 270 | R249-R250 | Cash generated from operations before working capital change |  |  |
| L069 | Standalone Cash Flow p5 | 272 | R251-R252 | (Decrease)/ increase in trade and other receivables |  |  |
| L070 | Standalone Cash Flow p5 | 273 | R253-R254 | Increase in inventories |  |  |
| L071 | Standalone Cash Flow p5 | 274 | R255-R256 | (Decrease)/ increase in trade, other payables and provisions |  |  |
| L072 | Standalone Cash Flow p5 | 275 | R257-R258 | Cash generated from operations before tax |  |  |
| L073 | Standalone Cash Flow p5 | 276 | R259-R260 | Less: Income-taxes paid (net of refunds) |  |  |
| L074 | Standalone Cash Flow p5 | 277 | R261-R262 | Net cash generated from operating activities |  |  |
| L075 | Standalone Cash Flow p5 | 279 | R263-R264 | Purchase of property, plant and equipment/ intangible assets |  |  |
| L076 | Standalone Cash Flow p5 | 280 | R265-R266 | Interest received |  |  |
| L077 | Standalone Cash Flow p5 | 281 | R267-R268 | (Investment in) /sale proceeds from mutual funds (net) |  |  |
| L078 | Standalone Cash Flow p5 | 282 | R269-R270 | Purchase of non-current investments | ZERO_STANDING (1 of 2 cells) |  |
| L079 | Standalone Cash Flow p5 | 283 | R271-R272 | Proceeds from deposits matured (net) |  |  |
| L080 | Standalone Cash Flow p5 | 284 | R273-R274 | Investment in preference shares of subsidiaries | ZERO_STANDING (1 of 2 cells) |  |
| L081 | Standalone Cash Flow p5 | 285 | R275-R276 | ICD (given)/repaid (net) | ZERO_STANDING (1 of 2 cells) |  |
| L082 | Standalone Cash Flow p5 | 286 | R277-R278 | Loans given to subsidiaries (net) | ZERO_STANDING (1 of 2 cells) |  |
| L083 | Standalone Cash Flow p5 | 287 | R279-R280 | Net cash used in investing activities |  |  |
| L084 | Standalone Cash Flow p5 | 289 | R281-R282 | Proceeds from short-term borrowings (net) | ZERO_STANDING (1 of 2 cells) |  |
| L085 | Standalone Cash Flow p5 | 290 | R283-R284 | Repayment of term loans |  |  |
| L086 | Standalone Cash Flow p5 | 291 | R285-R286 | Proceeds from term loans | ZERO_STANDING (1 of 2 cells) |  |
| L087 | Standalone Cash Flow p5 | 292 | R287-R288 | Dividend paid | ZERO_STANDING (1 of 2 cells) |  |
| L088 | Standalone Cash Flow p5 | 293 | R289-R290 | Payment of finance costs |  |  |
| L089 | Standalone Cash Flow p5 | 294 | R291-R292 | Net cash (used in) /generated from financing activities |  |  |
| L090 | Standalone Cash Flow p5 | 295 | R293-R294 | NET (DECREASE) / INCREASE IN CASH AND CASH EQUIVALENTS |  |  |
| L091 | Standalone Cash Flow p5 | 296 | R295-R296 | Add: Cash and cash equivalents at beginning of the year |  |  |
| L092 | Standalone Cash Flow p5 | 297 | R297-R298 | Cash and cash equivalents at end of the period |  |  |
| L093 | Standalone Cash Flow p5 | 299 | R299-R300 | Balances with banks |  |  |
| L094 | Standalone Cash Flow p5 | 300 | R301-R302 | Deposits with maturity up to three months | ZERO_STANDING (1 of 2 cells) |  |
| L095 | Standalone Cash Flow p5 | 301 | R303-R304 | Deposits with maturity up to three months |  |  |
| L096 | Consolidated P&L p9 | 466 | R339-R344 | a) Revenue from operations |  |  |
| L097 | Consolidated P&L p9 | 467 | R345-R350 | b) Other income |  |  |
| L098 | Consolidated P&L p9 | 468 | R351-R356 | Total income |  |  |
| L099 | Consolidated P&L p9 | 471 | R357-R362 | a) Cost of land, development of properties, construction and |  |  |
| L100 | Consolidated P&L p9 | 473 | R363-R368 | b) Changes in inventories of properties under development an |  |  |
| L101 | Consolidated P&L p9 | 474 | R369-R374 | c) Employee benefits expense |  |  |
| L102 | Consolidated P&L p9 | 475 | R375-R380 | d) Finance costs |  |  |
| L103 | Consolidated P&L p9 | 476 | R381-R386 | e) Depreciation and amortisation expenses |  |  |
| L104 | Consolidated P&L p9 | 477 | R387-R392 | f) Other expenses |  |  |
| L105 | Consolidated P&L p9 | 478 | R393-R398 | Total expenses |  |  |
| L106 | Consolidated P&L p9 | 479 | R399-R404 | 3 Profit before tax for the period / year (1-2) |  |  |
| L107 | Consolidated P&L p9 | 481 | R405-R410 | Current tax |  |  |
| L108 | Consolidated P&L p9 | 482 | R411-R416 | Deferred tax |  |  |
| L109 | Consolidated P&L p9 | 483 | R417-R422 | Total tax expense |  |  |
| L110 | Consolidated P&L p9 | 484 | R423-R428 | 5 Profit for the period / year (3-4) |  |  |
| L111 | Consolidated P&L p9 | 487 | R429-R434 | Remeasurement of defined benefit plan | ZERO_STANDING (5 of 6 cells) |  |
| L112 | Consolidated P&L p9 | 488 | R435-R440 | Income tax relating to above item | ZERO_STANDING (5 of 6 cells) |  |
| L113 | Consolidated P&L p9 | 489 | R441-R446 | Total other comprehensive income | ZERO_STANDING (5 of 6 cells) |  |
| L114 | Consolidated P&L p9 | 491 | R447-R452 | 7 Total comprehensive income for the period/ year (5-6) |  |  |
| L115 | Consolidated P&L p9 | 493 | R453-R458 | 8 Paid-up equity share capital (Face value of Rs 10 per shar |  |  |
| L116 | Consolidated P&L p9 | 494 | R459 | Other equity, FY26 (year 31.03.2026) only |  | year-end only (FY26) |
| L117 | Consolidated P&L p9 | 496 | R460-R465 | Basic |  |  |
| L118 | Consolidated P&L p9 | 497 | R466-R471 | Diluted |  |  |
| L119 | Consolidated Balance Sheet p10 | 506 | R472-R473 | (a) Property, plant and equipment |  |  |
| L120 | Consolidated Balance Sheet p10 | 507 | R474-R475 | (b) Capital work - in - progress |  |  |
| L121 | Consolidated Balance Sheet p10 | 508 | R476-R477 | (c) Intangible assets |  |  |
| L122 | Consolidated Balance Sheet p10 | 510 | R478-R479 | (i) Investments |  |  |
| L123 | Consolidated Balance Sheet p10 | 511 | R480-R481 | (ii) Other financial assets |  |  |
| L124 | Consolidated Balance Sheet p10 | 512 | R482-R483 | (e) Deferred tax assets (net) |  |  |
| L125 | Consolidated Balance Sheet p10 | 513 | R484-R485 | (f) Non-current tax assets (net) |  |  |
| L126 | Consolidated Balance Sheet p10 | 514 | R486-R487 | (g) Other non-current assets |  |  |
| L127 | Consolidated Balance Sheet p10 | 515 | R488-R489 | Total non-current assets |  |  |
| L128 | Consolidated Balance Sheet p10 | 517 | R490-R491 | (a) Inventories |  |  |
| L129 | Consolidated Balance Sheet p10 | 519 | R492-R493 | (i) Investments |  |  |
| L130 | Consolidated Balance Sheet p10 | 520 | R494-R495 | (ii) Trade receivables |  |  |
| L131 | Consolidated Balance Sheet p10 | 521 | R496-R497 | (iii) Cash and cash equivalents |  |  |
| L132 | Consolidated Balance Sheet p10 | 522 | R498-R499 | (iv) Bank balances other than cash and cash equivalents |  |  |
| L133 | Consolidated Balance Sheet p10 | 523 | R500-R501 | (v) Other financial assets |  |  |
| L134 | Consolidated Balance Sheet p10 | 524 | R502-R503 | (c) Other current assets |  |  |
| L135 | Consolidated Balance Sheet p10 | 525 | R504-R505 | Total current assets |  |  |
| L136 | Consolidated Balance Sheet p10 | 526 | R506-R507 | TOTAL ASSETS |  |  |
| L137 | Consolidated Balance Sheet p10 | 529 | R508-R509 | a) Equity share capital |  |  |
| L138 | Consolidated Balance Sheet p10 | 530 | R510-R511 | b) Other equity |  |  |
| L139 | Consolidated Balance Sheet p10 | 531 | R512-R513 | Total equity |  |  |
| L140 | Consolidated Balance Sheet p10 | 535 | R514-R515 | (i) Borrowings |  |  |
| L141 | Consolidated Balance Sheet p10 | 536 | R516-R517 | (b) Provisions |  |  |
| L142 | Consolidated Balance Sheet p10 | 537 | R518-R519 | (c) Deferred tax liabilities (Net) |  |  |
| L143 | Consolidated Balance Sheet p10 | 538 | R520-R521 | Total non-current liabilities |  |  |
| L144 | Consolidated Balance Sheet p10 | 541 | R522-R523 | (i) Borrowings |  |  |
| L145 | Consolidated Balance Sheet p10 | 543 | R524-R525 | Total outstanding dues of micro enterprises and small enterp |  |  |
| L146 | Consolidated Balance Sheet p10 | 544 | R526-R527 | Total outstanding dues of creditors other than micro enterpr |  |  |
| L147 | Consolidated Balance Sheet p10 | 545 | R528-R529 | (iii) Other financial liabilities |  |  |
| L148 | Consolidated Balance Sheet p10 | 546 | R530-R531 | (b) Other current liabilities |  |  |
| L149 | Consolidated Balance Sheet p10 | 547 | R532-R533 | (c) Provisions |  |  |
| L150 | Consolidated Balance Sheet p10 | 548 | R534-R535 | (d) Current tax liabilities (net) | ZERO_STANDING (1 of 2 cells) |  |
| L151 | Consolidated Balance Sheet p10 | 549 | R536-R537 | Total current liabilities |  |  |
| L152 | Consolidated Balance Sheet p10 | 550 | R538-R539 | Total liabilities |  |  |
| L153 | Consolidated Balance Sheet p10 | 551 | R540-R541 | TOTAL EQUITY AND LIABILITIES |  |  |
| L154 | Consolidated Cash Flow p11 | 559 | R542-R543 | Profit before tax |  |  |
| L155 | Consolidated Cash Flow p11 | 561 | R544-R545 | Depreciation and amortisation expenses |  |  |
| L156 | Consolidated Cash Flow p11 | 562 | R546-R547 | Finance costs |  |  |
| L157 | Consolidated Cash Flow p11 | 563 | R548-R549 | Interest income |  |  |
| L158 | Consolidated Cash Flow p11 | 564 | R550-R551 | Gain on sale of investments (net) | ZERO_STANDING (1 of 2 cells) |  |
| L159 | Consolidated Cash Flow p11 | 565 | R552-R553 | Fair value gain on financial assets at fair value through pr |  |  |
| L160 | Consolidated Cash Flow p11 | 566 | R554-R555 | Share based payment expense |  |  |
| L161 | Consolidated Cash Flow p11 | 567 | R556-R557 | Cash flow from operations before working capital changes |  |  |
| L162 | Consolidated Cash Flow p11 | 569 | R558-R559 | (Increase) in trade and other receivables |  |  |
| L163 | Consolidated Cash Flow p11 | 570 | R560-R561 | (Increase) in Inventories |  |  |
| L164 | Consolidated Cash Flow p11 | 571 | R562-R563 | Increase in trade, other payables and provisions |  |  |
| L165 | Consolidated Cash Flow p11 | 572 | R564-R565 | Cash used in operations before tax |  |  |
| L166 | Consolidated Cash Flow p11 | 573 | R566-R567 | Less: Income taxes paid (net of refunds) |  |  |
| L167 | Consolidated Cash Flow p11 | 574 | R568-R569 | Net cash used in operating activities |  |  |
| L168 | Consolidated Cash Flow p11 | 576 | R570-R571 | Purchase of property, plant and equipment/ intangible assets |  |  |
| L169 | Consolidated Cash Flow p11 | 577 | R572-R573 | Interest received |  |  |
| L170 | Consolidated Cash Flow p11 | 578 | R574-R575 | Proceeds from deposits matured (net) |  |  |
| L171 | Consolidated Cash Flow p11 | 579 | R576-R577 | (investment in)/ sale proceeds from mutual fund |  |  |
| L172 | Consolidated Cash Flow p11 | 580 | R578-R579 | Net cash (used in)/ generated from investing activities |  |  |
| L173 | Consolidated Cash Flow p11 | 582 | R580-R581 | Proceeds from short-term borrowings (net) | ZERO_STANDING (1 of 2 cells) |  |
| L174 | Consolidated Cash Flow p11 | 583 | R582-R583 | Repayment of term loans |  |  |
| L175 | Consolidated Cash Flow p11 | 584 | R584-R585 | Proceeds from term loans |  |  |
| L176 | Consolidated Cash Flow p11 | 585 | R586-R587 | Dividend paid | ZERO_STANDING (1 of 2 cells) |  |
| L177 | Consolidated Cash Flow p11 | 586 | R588-R589 | Payment of finance costs |  |  |
| L178 | Consolidated Cash Flow p11 | 587 | R590-R591 | Net cash generated from financing activities |  |  |
| L179 | Consolidated Cash Flow p11 | 588 | R592-R593 | NET (DECREASE) / INCREASE IN CASH AND CASH EQUIVALENTS |  |  |
| L180 | Consolidated Cash Flow p11 | 589 | R594-R595 | Add: Cash and cash equivalents at beginning of the year |  |  |
| L181 | Consolidated Cash Flow p11 | 590 | R596-R597 | Cash and cash equivalents at end of the period |  |  |
| L182 | Consolidated Cash Flow p11 | 592 | R598-R599 | Balances with banks |  |  |
| L183 | Consolidated Cash Flow p11 | 593 | R600-R601 | Deposits with maturity up to three months |  |  |
| L184 | Consolidated Cash Flow p11 | 594 | R602-R603 | Deposits with maturity up to three months |  |  |

## 2b. STATEMENT TABLE META (period headers, unit, audit status, footnotes)
| ROW IDs | table | note |
|---|---|---|
| R769-R770,R805-R811 | Standalone P&L p3 |  |
| R771,R812-R814 | Standalone Balance Sheet p4 |  |
| R772,R815-R820 | Standalone Cash Flow p5 | R818/R819 asterisk pair; R820 indirect-method note |
| R779-R780,R836-R842 | Consolidated P&L p9 |  |
| R781,R843-R845 | Consolidated Balance Sheet p10 |  |
| R782,R846-R849 | Consolidated Cash Flow p11 | R849 indirect-method note |

## 3. ZERO_STANDING REGISTER (23 line items, 48 cells)
| ID# | table | ROW IDs (zero cells) | line item | scope |
|---|---|---|---|---|
| L016 | Standalone P&L p3 L188 | R118-R122 | Remeasurement of defined benefit plan | some periods |
| L017 | Standalone P&L p3 L189 | R124-R128 | Income tax relating to above item | some periods |
| L018 | Standalone P&L p3 L190 | R130-R134 | Total other comprehensive income (net of tax) | some periods |
| L031 | Standalone Balance Sheet p4 L215 | R176 | (f) Non-current tax assets (net) | some periods |
| L035 | Standalone Balance Sheet p4 L221 | R184 | (i) Investments | some periods |
| L056 | Standalone Balance Sheet p4 L250 | R225 | (d) Current tax liabilities | some periods |
| L064 | Standalone Cash Flow p5 L266 | R241 | Gain on sale of investments (net) | some periods |
| L066 | Standalone Cash Flow p5 L268 | R245-R246 | Loss on disposal of property, plant and equipment (net)* | all periods |
| L078 | Standalone Cash Flow p5 L282 | R270 | Purchase of non-current investments | some periods |
| L080 | Standalone Cash Flow p5 L284 | R273 | Investment in preference shares of subsidiaries | some periods |
| L081 | Standalone Cash Flow p5 L285 | R276 | ICD (given)/repaid (net) | some periods |
| L082 | Standalone Cash Flow p5 L286 | R277 | Loans given to subsidiaries (net) | some periods |
| L084 | Standalone Cash Flow p5 L289 | R282 | Proceeds from short-term borrowings (net) | some periods |
| L086 | Standalone Cash Flow p5 L291 | R285 | Proceeds from term loans | some periods |
| L087 | Standalone Cash Flow p5 L292 | R288 | Dividend paid | some periods |
| L094 | Standalone Cash Flow p5 L300 | R302 | Deposits with maturity up to three months | some periods |
| L111 | Consolidated P&L p9 L487 | R429-R433 | Remeasurement of defined benefit plan | some periods |
| L112 | Consolidated P&L p9 L488 | R435-R439 | Income tax relating to above item | some periods |
| L113 | Consolidated P&L p9 L489 | R441-R445 | Total other comprehensive income | some periods |
| L150 | Consolidated Balance Sheet p10 L548 | R534 | (d) Current tax liabilities (net) | some periods |
| L158 | Consolidated Cash Flow p11 L564 | R550 | Gain on sale of investments (net) | some periods |
| L173 | Consolidated Cash Flow p11 L582 | R581 | Proceeds from short-term borrowings (net) | some periods |
| L176 | Consolidated Cash Flow p11 L585 | R587 | Dividend paid | some periods |
Template-signal note: standalone CF zero current-period cells where the comparative carries values (Gain on sale of investments, Investment in preference shares of subsidiaries, Loans given to subsidiaries, Proceeds from term loans) mark transaction types that occurred in the comparative period.

## 4. BOARD OUTCOME AGENDA ITEMS (p1)
| # | ROW IDs | item | A2 flags | note |
|---|---|---|---|---|
| B-A1 | R010,R008,R009,R763 | Enclosure 1: Unaudited Financial Results (Standalone and Consolidated) Q2 and H1 ended 30 Sep 2026 | | only decision item; Reg 30 and 33 |
| B-A2 | R010 | Enclosure 2: Limited Review Report of Statutory Auditors | | |
| B-A3 | R010 | Enclosure 3: Press Release on results | | enumerated in section 8 |
| B-T1 | R006,R007,R764 | Board meeting 03:40 P.M. to 05:00 P.M. (80 minutes) | | duration only; signature dates carry no time |
| B-X | R800 | "inter alia considered and approved" qualifier | | no AR, AGM, dividend, director, auditor, ESOP or capital-raising item disclosed |
Letter rows: header R001-R005,R699-R701,R761-R762; approval and meeting R006-R007,R763-R764,R800; enclosures R008-R010,R702; website/Reg 46 R011,R749 (R749 FWD); signature and footer R012-R014,R703-R704,R801.

## 5. AUDITOR REPORT PARAGRAPHS (11 paragraphs + 2 letterheads)
| # | ROW IDs | paragraph | A2 flags | note |
|---|---|---|---|---|
| A01 | R015-R018,R705-R706,R765 | Standalone report: letterhead, title, addressee (joint auditors Walker Chandiok & Co LLP, Chaturvedi & Shah LLP) |  |  |
| A02 | R019,R766-R767 | Standalone para 1: scope, quarter and YTD, Reg 33, SEBI Master Circular |  | limited review, no audit opinion |
| A03 | R020-R021 | Standalone para 2: management responsibility, Ind AS 34, s.133 |  |  |
| A04 | R022-R023,R707,R802-R803 | Standalone para 3: SRE 2410 review; "do not express an audit opinion" |  |  |
| A05 | R804 | Standalone para 4: conclusion, nothing has come to attention (unmodified) |  | no Emphasis of Matter, Other Matters or Going Concern paragraph |
| A06 |  | Consolidated report: letterhead, title, addressee |  |  |
| A07 | R715,R776 | Consolidated para 1: scope, Holding Company and subsidiaries |  |  |
| A08 |  | Consolidated para 2: management responsibility |  |  |
| A09 | R310,R826-R828 | Consolidated para 3: SRE 2410, Reg 33(8) procedures, no audit opinion |  |  |
| A10 | R829 | Consolidated para 4: conclusion (unmodified) after considering other auditors reports |  |  |
| A11 | R311-R319,R716,R777,R830-R831 | Consolidated para 5: 5 subsidiaries not reviewed by group auditors, reviewed by other auditors (assets, revenue, PAT, cash flow in lakhs) | OCR_UNCERTAIN | R831: loss digit uncertain, R315-R318; auditor-only data |
| A12 | R320-R328,R717,R832 | Consolidated Further para: 2 subsidiaries reviewed solely by Chaturvedi & Shah LLP |  | R320-R328 |
| A13 | R833 | Consolidated: "Our conclusion is not modified in respect of these matters" (R833) |  | reliance language, not an EoM |
Count observation: unreviewed-by-group subsidiaries 5 (R311,R716) + 2 (R320,R717) = 7, equal to the 7 subsidiaries in Annexure 1.

## 6. SIGNATURE BLOCKS (ink signatures; no digital timestamps present)
| # | ROW IDs | signatory | A2 flags | note |
|---|---|---|---|---|
| G01 | R024-R027,R708-R711,R768 | Standalone review report: Mayank Jain (Walker Chandiok, M.No. 512495) and Lalit R. Mhalsekar (Chaturvedi & Shah, M.No. 103418), dated 27 Oct 2026 (R768) | OCR_UNREADABLE (UDINs R710,R711), NO_TIMESTAMP | |
| G02 | R329-R331,R778 | Consolidated review report: same partners, dated 27 Oct 2026 (R778) | MISSING_FROM_STRUCTURED (UDINs, M1-M2), NO_TIMESTAMP | |
| G03 | R309,R714 | Standalone results: Managing Director Harmohan Sahni, DIN 00046068 (R309,R714), Mumbai, 27 Oct 2026 | NO_TIMESTAMP | name OCR-garbled on p6 |
| G04 | R607,R727,R785 | Consolidated results: Harmohan Sahni, DIN 00046068 (R607,R727), 27 Oct 2026 (R785) | RESTATED vs G03, NO_TIMESTAMP | |
| G05 | R704 | Board Outcome letter: Hiren Sonawala, Company Secretary, letter date 27 Oct 2026 (R761) | NO_TIMESTAMP | meeting concluded 05:00 P.M.; no signing time to compare |

## 7. ENTITY LEDGER (all 50 A1 ENTITY rows; prior ledger none, ENTITY_CHANGE judged on in-document evidence)
| ROW ID | page L | entity | category | A2 flags | note |
|---|---|---|---|---|---|
| R699 | p1 L19 | Raymond Realty Limited | filer / regulator / other |  |  |
| R700 | p1 L30 | National Stock Exchange of India Limited (NSE) | filer / regulator / other |  |  |
| R701 | p1 L32 | BSE Limited | filer / regulator / other |  |  |
| R702 | p1 L57 | SEBI | filer / regulator / other |  |  |
| R703 | p1 L77 | Raymond Lifestyle Limited | filer / regulator / other | ENTITY_CHANGE | company formerly Raymond Lifestyle Limited |
| R704 | p1 L79 | Hiren Sonawala | filer / regulator / other |  |  |
| R705 | p2 L89 | Walker Chandiok & Co LLP | auditor / signatory |  |  |
| R706 | p2 L89 | Chaturvedi & Shah LLP | auditor / signatory |  |  |
| R707 | p2 L122 | Institute of Chartered Accountants of India (ICAI) | filer / regulator / other |  |  |
| R708 | p2 L143 | Mayank Jain | auditor / signatory |  |  |
| R709 | p2 L144 | Lalit R. Mhalsekar | auditor / signatory |  |  |
| R710 | p2 L146 | UDIN (Walker Chandiok, standalone) | auditor / signatory | OCR_UNREADABLE |  |
| R711 | p2 L148 | UDIN (Chaturvedi & Shah, standalone) | auditor / signatory | OCR_UNREADABLE |  |
| R712 | p6 L316 | Audit Committee | filer / regulator / other |  |  |
| R713 | p6 L320 | Chief Operating Decision Maker (CODM) | filer / regulator / other |  |  |
| R714 | p6 L333 | Managing Director, DIN 00046068 (Harmohan Sahni per page 12) | filer / regulator / other |  |  |
| R715 | p7 L354 | Raymond Realty Limited (Holding Company) | consolidation holding company |  |  |
| R716 | p7 L394 | 5 subsidiaries reviewed by other auditors (unnamed) | unnamed subsidiary group (auditor reliance) |  | 5+2 unnamed subs; Annexure lists 7 named |
| R717 | p8 L409 | 2 subsidiaries reviewed solely by Chaturvedi & Shah LLP | unnamed subsidiary group (auditor reliance) |  | 5+2 unnamed subs; Annexure lists 7 named |
| R718 | p8 L444 | Ten X Realty Limited | consolidation subsidiary (Annexure 1) |  |  |
| R719 | p8 L445 | Ten X Realty East Limited | consolidation subsidiary (Annexure 1) |  |  |
| R720 | p8 L446 | Ten X Realty West Limited | consolidation subsidiary (Annexure 1) |  |  |
| R721 | p8 L447 | Ten X Realty North Limited (formerly known as Chembur Realty Limited) | consolidation subsidiary (Annexure 1) | ENTITY_CHANGE | rename: Chembur Realty Limited -> Ten X Realty North Limited; date of change not stated |
| R722 | p8 L447 | Chembur Realty Limited | filer / regulator / other | ENTITY_CHANGE | rename: Chembur Realty Limited -> Ten X Realty North Limited; date of change not stated |
| R723 | p8 L448 | Ten X Realty South Limited | consolidation subsidiary (Annexure 1) |  |  |
| R724 | p8 L449 | Rayzone Property Services Limited | consolidation subsidiary (Annexure 1) |  |  |
| R725 | p8 L450 | Ten X Mahalaxmi Limited | consolidation subsidiary (Annexure 1) |  |  |
| R726 | p12 L609 | Audit Committee | filer / regulator / other |  |  |
| R727 | p12 L622 | Harmohan Sahni | filer / regulator / other |  |  |
| R728 | p13 L631 | Raymond Realty Limited | press release entity |  |  |
| R729 | p13 L637 | Mumbai JDAs | press release entity |  |  |
| R730 | p13 L637 | Owned Thane Land Parcel | press release entity |  |  |
| R731 | p13 L662 | Address by GS | press release entity |  |  |
| R732 | p13 L667 | Mumbai Metropolitan Region (MMR) | press release entity |  |  |
| R733 | p13 L673 | 100 Acre Thane Land Parcel | press release entity |  |  |
| R734 | p14 L687 | Address by GS Season 1 Tower B, Thane | press release entity |  |  |
| R735 | p14 L688 | RERA | press release entity |  |  |
| R736 | p14 L691 | JDA Portfolio (eight projects) | press release entity |  |  |
| R737 | p14 L694 | JDA projects Bandra, BKC, Wadala, Sion | press release entity |  |  |
| R738 | p14 L707 | Mahim 1 | press release entity |  |  |
| R739 | p14 L708 | Mahim 2 | press release entity |  |  |
| R740 | p14 L719 | BMC / TMC / MHADA | press release entity |  |  |
| R741 | p14 L720 | CARE (rating agency) | press release entity |  |  |
| R742 | p14 L726 | Harmohan Sahni | press release entity |  |  |
| R743 | p15 L745 | Raymond Group | press release entity |  |  |
| R744 | p15 L750 | TenX | press release entity |  |  |
| R745 | p15 L750 | The Address by GS | press release entity |  |  |
| R746 | p15 L751 | Invictus by GS | press release entity |  |  |
| R747 | p15 L766 | Shalini Singh | press release entity |  |  |
| R748 | p15 L768 | Raymond Limited | press release entity |  |  |
Consolidation scope: Holding Company (R715) + 7 subsidiaries (R718,R719,R720,R721,R723,R724,R725); Annexure serials R332-R338.

## 7b. NON-STATEMENT ROWS BY SECTION (letter, review reports, notes, annexure; each ID once)
| section | ROW IDs by type | page |
|---|---|---|
| B1: Letter header, addressees, ref, ISIN | NUMBER: R001-R005; ENTITY: R699-R701; DATE: R761-R762 | [1] |
| B2: Board approval paragraph and meeting times | NUMBER: R006-R007; DATE: R763-R764; QUALIFIER: R800 | [1] |
| B3: Enclosure list (agenda items) | NUMBER: R008-R010; ENTITY: R702 | [1] |
| B4: Website intimation (Reg 30/46) | NUMBER: R011; FORWARD: R749 | [1] |
| B5: Signature block, registered office footer | NUMBER: R012-R014; ENTITY: R703-R704; QUALIFIER: R801 | [1] |
| S0: Standalone review report: letterhead, title, addressee | NUMBER: R015-R018; ENTITY: R705-R706; DATE: R765 | [2] |
| S1: Standalone review report para 1 | NUMBER: R019; DATE: R766-R767 | [2] |
| S2: Standalone review report para 2 | NUMBER: R020-R021 | [2] |
| S3: Standalone review report para 3 | NUMBER: R022-R023; ENTITY: R707; QUALIFIER: R802-R803 | [2] |
| SS: Standalone review report signature block | NUMBER: R024-R027; ENTITY: R708-R711; DATE: R768 | [2] |
| N3s: Standalone Note 3 | NUMBER: R305; ENTITY: R713; QUALIFIER: R823 | [6] |
| N4s: Standalone Note 4 | NUMBER: R306-R308; DATE: R774-R775; QUALIFIER: R824 | [6] |
| MDs: Standalone results signature (Managing Director) | NUMBER: R309; ENTITY: R714 | [6] |
| C3: Consolidated review report para 3 | NUMBER: R310; QUALIFIER: R826-R828 | [7] |
| C5: Consolidated review report para 5 (5 subsidiaries, other auditors) | NUMBER: R311-R319; ENTITY: R716; DATE: R777; QUALIFIER: R830-R831 | [7, 8] |
| C6: Consolidated review report Further para (2 subsidiaries, joint-auditor reliance) | NUMBER: R320-R328; ENTITY: R717; QUALIFIER: R832 | [8] |
| CS: Consolidated review report signature block | NUMBER: R329-R331; DATE: R778 | [8] |
| AX: Annexure 1: list of entities included in the Statement | NUMBER: R332-R338; ENTITY: R718-R725; QUALIFIER: R834-R835 | [8] |
| N3c: Consolidated Note 3 | NUMBER: R604; QUALIFIER: R852 | [12] |
| N4c: Consolidated Note 4 | NUMBER: R605-R606; DATE: R784; QUALIFIER: R853 | [12] |
| MDc: Consolidated results signature (Managing Director) | NUMBER: R607; ENTITY: R727; DATE: R785 | [12] |
| N2s: Standalone Note 2 | ENTITY: R712; DATE: R773; QUALIFIER: R822 | [6] |
| C1: Consolidated review report para 1 | ENTITY: R715; DATE: R776 | [7] |
| N2c: Consolidated Note 2 | ENTITY: R726; DATE: R783; QUALIFIER: R851 | [12] |
| S4: Standalone review report para 4 | QUALIFIER: R804 | [2] |
| N1s: Standalone Note 1 | QUALIFIER: R821 | [6] |
| N5s: Standalone Note 5 | QUALIFIER: R825 | [6] |
| C4: Consolidated review report para 4 | QUALIFIER: R829 | [7] |
| C7: Consolidated review report conclusion-not-modified para | QUALIFIER: R833 | [8] |
| N1c: Consolidated Note 1 | QUALIFIER: R850 | [12] |
| N5c: Consolidated Note 5 | QUALIFIER: R854 | [12] |

## 8. PRESS RELEASE (pages 13-15, Rs Cr; enumerated as part of this results document)
| ROW IDs | type | page L | item | A2 flags | cross-ref |
|---|---|---|---|---|---|
| R608-R610 | NUMBER | p13 L634 | Q2 FY27 booking value YoY growth | PR |  |
| R611 | NUMBER | p13 L636 | H1 FY27 booking value | PR |  |
| R612-R613 | NUMBER | p13 L637 | booking value mix, Mumbai JDAs | PR |  |
| R614-R616 | NUMBER | p13 L638 | Q2 FY27 collections YoY growth | PR, RESTATED | R689 (collections growth 67%) |
| R617 | NUMBER | p13 L640 | H1 FY27 collections | PR |  |
| R618 | NUMBER | p13 L641 | total portfolio GDV | PR, RESTATED | R647, R697 (~520 bn) |
| R619-R621 | NUMBER | p13 L644 | Q2FY27 total income | PR |  |
| R622-R624 | NUMBER | p13 L645 | Q2FY27 EBITDA | PR |  |
| R625-R627 | NUMBER | p13 L646 | net debt | PR, RESTATED | R675 (net debt) |
| R628-R630 | NUMBER | p13 L653 | Total Income Q2FY27, table | PR |  |
| R631-R633 | NUMBER | p13 L654 | EBITDA Q2FY27, table | PR |  |
| R634-R635 | NUMBER | p13 L655 | EBITDA margin Q2FY27, table | PR |  |
| R636-R638 | NUMBER | p13 L656 | PBT Q2FY27, table | PR |  |
| R639-R640 | NUMBER | p13 L657 | PBT margin Q2FY27, table | PR |  |
| R641 | NUMBER | p13 L659 | Q2 FY27 total income, narrative | PR |  |
| R642 | NUMBER | p13 L660 | total income YoY, narrative | PR |  |
| R643-R645 | NUMBER | p13 L663 | EBITDA YoY, narrative | PR |  |
| R646 | NUMBER | p13 L666 | FY27 EBITDA margin guidance | PR |  |
| R647 | NUMBER | p13 L671 | total portfolio GDV, narrative | PR, RESTATED | R618 |
| R648-R649 | NUMBER | p13 L673 | Thane land parcel size | PR |  |
| R650 | NUMBER | p13 L675 | Thane acres under development | PR |  |
| R651-R652 | NUMBER | p13 L676 | RERA carpet area, Thane under development | PR |  |
| R653 | NUMBER | p13 L678 | corporate office postal code | PR |  |
| R654 | NUMBER | p14 L684 | Thane land sold to date | PR |  |
| R655 | NUMBER | p14 L685 | Thane collections to date | PR |  |
| R656-R657 | NUMBER | p14 L688 | Address by GS S1 Tower B units | PR |  |
| R658 | NUMBER | p14 L691 | JDA portfolio count | PR |  |
| R659 | NUMBER | p14 L692 | JDA portfolio revenue potential | PR |  |
| R660 | NUMBER | p14 L694 | JDA projects launched | PR |  |
| R661-R662 | NUMBER | p14 L695 | RERA carpet area, 4 launched JDAs | PR |  |
| R663 | NUMBER | p14 L699 | JDA sold to date | PR |  |
| R664 | NUMBER | p14 L700 | JDA collections to date | PR |  |
| R665 | NUMBER | p14 L702 | launch horizon | PR |  |
| R666 | NUMBER | p14 L703 | MMR launch pipeline cumulative GDV | PR, RESTATED | R672, R691, R752-R753, R758 |
| R667 | NUMBER | p14 L704 | JDA launches in current FY | PR |  |
| R668-R669 | NUMBER | p14 L707 | Mahim 1 GDV Rs Cr | PR |  |
| R670-R671 | NUMBER | p14 L708 | Mahim 2 GDV Rs Cr | PR |  |
| R672-R673 | NUMBER | p14 L709 | launch pipeline total GDV Rs Cr | PR |  |
| R674 | NUMBER | p14 L712 | gross debt | PR |  |
| R675-R676 | NUMBER | p14 L713 | net debt | PR, RESTATED | R625 |
| R677 | NUMBER | p14 L714 | debt to equity ceiling | PR |  |
| R678 | NUMBER | p14 L715 | liquidity buffer | PR |  |
| R679 | NUMBER | p14 L716 | cost of debt | PR |  |
| R680 | NUMBER | p14 L717 | total interest cost Q2 FY27 | PR |  |
| R681-R682 | NUMBER | p14 L718 | interest on bank borrowings Q2 FY27 | PR |  |
| R683 | NUMBER | p14 L720 | credit rating | PR |  |
| R684 | NUMBER | p14 L723 | FY27 pre-sales growth guidance | PR |  |
| R685-R687 | NUMBER | p14 L724 | FY27 ROCE guidance | PR |  |
| R688 | NUMBER | p14 L730 | CEO: quarterly pre-sales | PR |  |
| R689 | NUMBER | p14 L731 | CEO: collections surge | PR, RESTATED | R614 |
| R690 | NUMBER | p14 L732 | CEO: Thane tower ahead of RERA timeline | PR |  |
| R691 | NUMBER | p14 L733 | CEO: MMR launch pipeline | PR, RESTATED | R666 |
| R692 | NUMBER | p15 L747 | year of foray into real estate | PR |  |
| R693 | NUMBER | p15 L748 | rank claim among India real estate players | PR |  |
| R694 | NUMBER | p15 L750 | residential brands named | PR |  |
| R695-R696 | NUMBER | p15 L751 | owned land | PR |  |
| R697 | NUMBER | p15 L752 | estimated gross development value | PR, RESTATED | R618 |
| R698 | NUMBER | p15 L769 | contact telephone | PR |  |
| R728 | ENTITY | p13 L631 | press release issuer | PR |  |
| R729-R730 | ENTITY | p13 L637 | booking mix component | PR |  |
| R731 | ENTITY | p13 L662 | existing portfolio brand | PR |  |
| R732 | ENTITY | p13 L667 | launch geography | PR |  |
| R733 | ENTITY | p13 L673 | owned land asset | PR |  |
| R734 | ENTITY | p14 L687 | project receiving OC in Q2 FY27 | PR |  |
| R735 | ENTITY | p14 L688 | regulator, completion timelines | PR |  |
| R736 | ENTITY | p14 L691 | joint development agreements | PR |  |
| R737 | ENTITY | p14 L694 | four launched JDA projects | PR |  |
| R738 | ENTITY | p14 L707 | planned JDA launch | PR |  |
| R739 | ENTITY | p14 L708 | planned JDA launch | PR |  |
| R740 | ENTITY | p14 L719 | authorities receiving interest for additional FSI and approvals | PR |  |
| R741 | ENTITY | p14 L720 | reaffirmed CARE A+ Stable | PR |  |
| R742 | ENTITY | p14 L726 | Managing Director & CEO | PR |  |
| R743 | ENTITY | p15 L745 | parent group of Raymond Realty | PR |  |
| R744-R745 | ENTITY | p15 L750 | residential brand | PR |  |
| R746 | ENTITY | p15 L751 | residential brand | PR |  |
| R747 | ENTITY | p15 L766 | Corporate Communications contact | PR |  |
| R748 | ENTITY | p15 L768 | contact organisation | PR |  |
| R750 | FORWARD | p13 L665 | EBITDA margin trajectory | PR, FWD |  |
| R751-R752 | FORWARD | p13 L666 | FY27 EBITDA margin | PR, FWD |  |
| R753 | FORWARD | p14 L702 | launch pipeline | PR, FWD |  |
| R754 | FORWARD | p14 L704 | FY27 launches | PR, FWD |  |
| R755 | FORWARD | p14 L714 | leverage | PR, FWD |  |
| R756 | FORWARD | p14 L715 | liquidity | PR, FWD |  |
| R757 | FORWARD | p14 L723 | FY27 guidance | PR, FWD |  |
| R758 | FORWARD | p14 L733 | CEO statement | PR, FWD |  |
| R759 | FORWARD | p14 L734 | CEO statement | PR, FWD |  |
| R760 | FORWARD | p15 L756 | safe-harbour disclaimer | PR, FWD |  |
| R786 | DATE | p13 L629 | press release date | PR |  |
| R787 | DATE | p13 L631 | quarter | PR |  |
| R788 | DATE | p13 L634 | half year | PR |  |
| R789 | DATE | p13 L644 | comparative quarter | PR |  |
| R790 | DATE | p13 L648 | results quarter | PR |  |
| R791 | DATE | p13 L666 | guidance year | PR |  |
| R792 | DATE | p14 L687 | OC received quarter | PR |  |
| R793 | DATE | p14 L689 | proposed RERA completion date, Address by GS S1 Tower B | PR |  |
| R794 | DATE | p14 L702 | launch window | PR |  |
| R795 | DATE | p14 L723 | guidance year | PR |  |
| R796 | DATE | p14 L728 | CEO statement period | PR |  |
| R797 | DATE | p14 L732 | CEO: tower delivery | PR |  |
| R798 | DATE | p15 L745 | Raymond Group history | PR |  |
| R799 | DATE | p15 L747 | foray into real estate | PR |  |
| R855 | QUALIFIER | p13 L641 | approximation marker | PR |  |
| R856 | QUALIFIER | p13 L648 | press release unaudited status | PR |  |
| R857 | QUALIFIER | p13 L651 | extraction qualifier | PR |  |
| R858 | QUALIFIER | p13 L652 | PR table unit qualifier | PR |  |
| R859 | QUALIFIER | p13 L660 | context qualifier on total income growth | PR |  |
| R860 | QUALIFIER | p13 L664 | margin qualifier | PR |  |
| R861 | QUALIFIER | p13 L673 | metric qualifier | PR |  |
| R862 | QUALIFIER | p13 L676 | approximation marker | PR |  |
| R863 | QUALIFIER | p14 L684 | approximation and cumulative marker | PR |  |
| R864 | QUALIFIER | p14 L689 | date qualifier | PR |  |
| R865 | QUALIFIER | p14 L692 | approximation marker | PR |  |
| R866 | QUALIFIER | p14 L695 | approximation marker | PR |  |
| R867 | QUALIFIER | p14 L699 | approximation and cumulative marker | PR |  |
| R868 | QUALIFIER | p14 L707 | table unit qualifier | PR |  |
| R869 | QUALIFIER | p14 L712 | leverage metric | PR |  |
| R870-R871 | QUALIFIER | p14 L715 | approximation marker | PR |  |
| R872 | QUALIFIER | p14 L717 | composition qualifier | PR |  |
| R873 | QUALIFIER | p15 L752 | unit-variant marker | PR |  |
| R874 | QUALIFIER | p15 L754 | disclaimer | PR |  |
PR vs statements (flagged for A3, not reconciled here): PR Q2 total income 757 Cr (R619,R628,R641) vs consolidated Total income Q2 FY27 75,749 lakhs (R351); PR PBT 66 Cr (R636) vs consolidated PBT 6,632 lakhs (R399); EBITDA (R622,R631,R643) has no statement row; net debt 912 Cr at R625 and R675; collections growth 67% at R614 and R689; GDV ~52,000 Cr at R618,R647 and approx 520 billion at R697.

## 9. MISSING_FROM_STRUCTURED (loop back to A1)
| M# | fulltext line | unit | flag |
|---|---|---|---|
| M1 | L435 (p8) | Consolidated review report UDIN, Walker Chandiok (Mayank Jain); stamp text OCR-garbled in fulltext | MISSING_FROM_STRUCTURED, OCR_UNREADABLE |
| M2 | L435 (p8) | Consolidated review report UDIN, Chaturvedi & Shah (Lalit Mhalsekar); OCR-garbled | MISSING_FROM_STRUCTURED, OCR_UNREADABLE |
| M3 | L427 (p8) | Consolidated report firm reg nos: Walker Chandiok 001076N/N500013 (A1 holds only N500013, R329) and Chaturvedi & Shah 101720W/W100355 (no row) | MISSING_FROM_STRUCTURED |
| M4 | L147,L150 (p2); L437 (p8) | "Place: Mumbai" in the four auditor signature blocks (no row) | MISSING_FROM_STRUCTURED (minor) |
