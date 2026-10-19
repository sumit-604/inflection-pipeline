# A2 COMPLETENESS LEDGER: Tatva Chintan Pharma Chem Limited (TATVA), Q2 FY27, results

MISSING_FROM_STRUCTURED loop closed: A1 supplement R1049-R1090 now holds the 16 omitted Other lines (section 10 maps each). Source: runs/tatva-q2fy27/extracted/tatva-results-q2fy27-structured.md (A1). Fulltext used only for count-test fallback and MISSING_FROM_STRUCTURED confirmation. Units Rs million as printed. Prior-quarter ledger: none, so ENTITY_CHANGE and DROPPED checks are not run.

=== A2 COUNT TEST ===
category: notes          grep_count: 13  sweep_count: 13  match: yes   (consolidated 7 + standalone 6; grep on fulltext notes sections lines 345-371 and 633-643 returns 13; structured Note rows R1008-R1012,R1017,R1018,R1043-R1048 = 13)
category: line_items     grep_count: 241  sweep_count: 241  match: yes   (first sweep of structured file found 241 line items; fulltext grep found 241; first pass found 225, 16 "Other ..." lines were missing; A1 supplement R1049-R1090 (42 cells) now closes them)
category: zero_standing  grep_count: 69  sweep_count: 69  match: yes   (cells with ZERO_STANDING flag; grep on structured rows vs sweep by line item)
category: agenda_items   grep_count: 1  sweep_count: 1  match: yes   (cover letter carries one item, results approval; no AR, AGM, dividend, director or auditor agenda items present)
category: auditor_paras  grep_count: 10  sweep_count: 10  match: yes   (consolidated report paras 1-6, standalone report paras 1-4)
category: entities      grep_count: 3  sweep_count: 3  match: yes   (consolidation list a-c; 44 ENTITY rows in all are accounted for below)
category: structured_rows grep_count: 1090  sweep_count: 1090  match: yes   (NUMBER 914, ENTITY 44, FORWARD 3, DATE 57, QUALIFIER 72; header counts agree)
gate_a2: pass   (16 MISSING_FROM_STRUCTURED lines now carry A1 supplement IDs R1049-R1090; no orphan IDs)
=== END COUNT TEST ===
ids_in_structured: 1090 | ids_referenced_in_ledger: 1090 | orphan_ids: [] | match: yes

## 0. FOOTING AND TRANSCRIPTION CHECKS (requested by caller; A1 did not spot-check cells)
Method: every total re-added from its printed components, both entities, all columns. The 16 omitted "Other ..." lines (section MFS) were read from A1 fulltext to complete the sums.

Result: ZERO failing cells in A1 structured rows. Details:
- P&L (cons p4, std p10): Total income = Revenue + Other income; Total expenses = nine lines incl. Other expenses (foots only with the Other expenses line, supplement); PBT pre-exceptional = TI - TE; PBT = pre - exceptional; Tax = current + deferred; PAT = PBT - tax; OCI = components; TCI = PAT + OCI; H1 FY27 = Q2 + Q1 for every line; basic EPS = PAT / 23.392 mn shares. All pass, 6 columns each.
- Balance sheet (cons p5, std p11): non-current assets, current assets, total assets, non-current liabilities, current liabilities, total equity and liabilities all foot, and Total assets = Total equity and liabilities, in both columns, only once the omitted Other intangible / Other non-current assets / Other current assets / Other non-current liabilities / Other current liabilities lines are added. Other equity (omitted) also reconciles: cons 7,912.59 + 233.92 = 8,146.51; std 7,560.83 + 233.92 = 7,794.75.
- Cash flow (cons p6-7, std p12-13): adjustments, operating profit before WC, WC total, cash generated, CFO (A), CFI (B), CFF (C), D = A+B+C, closing = D + opening + FX, and cash components = Balance per statement of cash flows all foot (omitted Other non-cash items needed). Closing cash vs balance sheet: cons 106.79 (30.09.2026) and 57.64 (31.03.2026) match R264,R265; std 53.48 and 14.70 match the std balance sheet cash line.
- Equity roll: cons equity change 328.92 = H1 TCI 375.70 minus dividend paid 46.78 (R-ids in CFF). Std equity change 212.46 = H1 TCI 259.25 minus 46.79; std CFF shows dividend paid 8.55 against 46.78 on the consolidated CFF. The std cash flow foots as printed, so this is not a transcription defect. It is a standalone vs consolidated difference of 38.23 in dividend paid, left for A3/A4 (possible dividend payable or intra-group item). Flag DIVIDEND_PAID_DIFF.
- Note 5 table (cons p8) vs standalone P&L (p10): all 5 rows x 6 columns identical, flagged RESTATED with partner IDs below.
- H1 FY26 and FY26 columns cannot be footed against Q1 FY26 (Q1 FY26 not shown); they foot internally.
- Mechanical check issues remaining after completing the omitted rows: 0 (the "row missing" and CFF items in the raw log are label-matching misses in the checker; re-run by hand and all foot).

## 1. NOTES (numbered notes, footnotes, cross-reference lines)
ROW_ID | category | A2 flags | cross-ref / materiality note
R1008 | note: Cons Note 1 | - | FORWARD:no. Board and Audit Committee 19 Oct 2026; matches cover letter R922.
R1009 | note: Cons Note 2 | - | Unmodified opinion language on a limited review (review, not audit).
R1010 | note: Cons Note 3 | - | 
R1011 | note: Cons Note 4 | RESTATED | Single segment, specialty chemicals; mirrors Std Note 4 (R1046), RESTATED.
R1012-R1016 | note: Cons Note 5 (standalone key numbers table, see section 2D) | RESTATED | Table rows R-ids in section 2D; values equal std P&L. RESTATED.
R1017 | note: Cons Note 6 | - | Website availability commitment, FORWARD R918.
R1018 | note: Cons Note 7 | RESTATED, RECLASS_UNQUANTIFIED | Reclassification of prior-period figures; no quantification given. Mirrors Std Note 6 (R1048). Flag RECLASS_UNQUANTIFIED.
R1043 | note: Std Note 1 | - | 
R1044 | note: Std Note 2 | - | 
R1045 | note: Std Note 3 | - | 
R1046 | note: Std Note 4 | RESTATED | 
R1047 | note: Std Note 5 | - | FORWARD R919.
R1048 | note: Std Note 6 | RESTATED | Reclassification, no quantification. RESTATED with Cons Note 7.
Unnumbered footnotes / qualifier lines (no asterisk or dagger footnotes exist; these are inline qualifiers):
R983-R1007,R1019-R1042 | qualifier groups (unit statement, audit status of columns, EPS not annualised, face value, MSME definitions, tax paid, capex scope, notes cross-ref, review scope) | - | R1005 and R1040 carry label anomaly: caption reads "Net decrease in cash" while cons H1 FY27 value 49.52 and std 38.79 are positive. Flag LABEL_ANOMALY. R1035 heading difference (cons vs std operating activities caption). R1000: 31.03.2026 column is full-year.

## 2. LINE ITEMS (every line in every financial table, incl. zero / nil / dash)
ROW_ID range | category | A2 flags | cross-ref / materiality note. One ledger row = one line item across its period columns. LINE = fulltext line number.

### CONSOLIDATED P&L (page 4)
LINE | line item | ROW_IDs | A2 flags | note
145 | 1 Revenue from operations | R029-R034 | - | 
146 | 2 Other income | R035-R040 | - | 
147 | 3 Total income (1+2) | R041-R046 | - | 
149 | Cost of materials consumed | R047-R052 | - | 
150 | Purchases of stock-in-trade | R053-R058 | - | 
151 | Changes in inventories of finished goods, work-in-progress a | R059-R064 | - | 
152 | Employee benefits expense | R065-R070 | - | 
153 | Finance costs | R071-R076 | - | 
154 | Depreciation and amortisation expenses | R077-R082 | - | 
155 | Other expenses | R1049-R1054 | MISSING_FROM_STRUCTURED(resolved) | 
156 | 4 Total expenses | R083-R088 | - | 
157 | 5 Profit/(loss) before exceptional items and tax (3-4) | R089-R094 | - | 
158 | 6 Exceptional items | R095-R100 | ZERO_STANDING(4 of 6 cells: R095+R097+R099-R100) | Exceptional item 13.18 booked in Q1 FY27 (quarter ended 30.06.2026) only; nil in Q2 FY27, nil in all FY26 columns. Nature not disclosed in a note.
159 | 7 Profit/(loss) before tax (5-6) | R101-R106 | - | 
161 | Current tax | R107-R112 | - | 
162 | Deferred tax | R113-R118 | - | 
163 | 8 Total tax expenses/(benefits) | R119-R124 | - | 
164 | 9 Profit for the period/year (7-8) | R125-R130 | - | 
166 | Items that will not be reclassified to profit or loss | R131-R136 | - | 
167 | Income tax relating to items that will not be reclassified t | R137-R142 | - | 
168 | Items that will be reclassified to profit or loss | R143-R148 | - | 
169 | Income tax relating to items that will be reclassified to pr | R149-R154 | ZERO_STANDING(all periods) | 
170 | 10 Other comprehensive income/(expense) for the period/year, | R155-R160 | - | 
171 | 11 Total comprehensive income for the period/year (9+10) | R161-R166 | - | 
172 | 12 Profit for the period/year attributable to: - Owners of t | R167-R172 | - | 
173 | 12 Profit for the period/year attributable to: - Non control | R173-R178 | ZERO_STANDING(all periods) | 
174 | 12 Profit for the period/year attributable to: (sub-total) | R179-R184 | - | 
175 | 13 Other comprehensive income/(expense) attributable to: - O | R185-R190 | - | 
176 | 13 Other comprehensive income/(expense) attributable to: - N | R191-R196 | ZERO_STANDING(all periods) | 
177 | 13 Other comprehensive income/(expense) attributable to: (su | R197-R202 | - | 
178 | 14 Total comprehensive income attributable to: - Owners of t | R203-R208 | - | 
179 | 14 Total comprehensive income attributable to: - Non control | R209-R214 | ZERO_STANDING(all periods) | 
180 | 14 Total comprehensive income attributable to: (sub-total) | R215-R220 | - | 
181 | 15 Earnings per share (Face value of Rs 10/- each) (not annu | R221-R226 | - | 
182 | 15 Earnings per share (Face value of Rs 10/- each) (not annu | R228-R233 | - | 
183 | 16 Paid - up equity share capital (Face value of Rs 10/- eac | R234-R239 | - | 
(line items in this statement: 36)

### CONSOLIDATED BALANCE SHEET (page 5)
LINE | line item | ROW_IDs | A2 flags | note
201 | Property, plant and equipment | R244-R245 | - | 
202 | Right-of-use assets | R246-R247 | - | 
203 | Capital work-in-progress | R248-R249 | - | 
204 | Other intangible assets | R1055-R1056 | MISSING_FROM_STRUCTURED(resolved) | 
205 | Intangible assets under development | R250-R251 | - | 
207 | i) Investments | R252-R253 | - | 
208 | ii) Other financial assets | R254-R255 | - | 
209 | Deferred tax assets (net) | R256-R257 | - | 
210 | Other non-current assets | R1057-R1058 | MISSING_FROM_STRUCTURED(resolved) | 
211 | Total non-current assets | R258-R259 | - | 
213 | Inventories | R260-R261 | - | 
215 | i) Trade receivables | R262-R263 | - | 
216 | ii) Cash and cash equivalents | R264-R265 | - | 
217 | iii) Bank balances other than cash and cash equivalents | R266-R267 | - | 
218 | iv) Loans | R268-R269 | - | 
219 | v) Other financial assets | R270-R271 | - | 
220 | Current tax assets (net) | R272-R273 | - | 
221 | Other current assets | R1059-R1060 | MISSING_FROM_STRUCTURED(resolved) | 
222 | Total current assets | R274-R275 | - | 
223 | Total assets | R276-R277 | - | 
226 | Equity share capital | R278-R279 | - | 
227 | Other equity | R1061-R1062 | MISSING_FROM_STRUCTURED(resolved) | 
228 | Equity attributable to owners | R280-R281 | - | 
229 | Non-controlling interests | R282-R283 | ZERO_STANDING(all periods) | 
230 | Total equity | R284-R285 | - | 
234 | i) Borrowings | R286-R287 | - | 
235 | Employee benefit obligations | R288-R289 | - | 
236 | Other non-current liabilities | R1063-R1064 | MISSING_FROM_STRUCTURED(resolved) | 
237 | Total non-current liabilities | R290-R291 | - | 
240 | i) Borrowings | R292-R293 | - | 
241 | ii) Trade payables (a) total outstanding dues of micro enter | R294-R295 | - | 
242 | ii) Trade payables (b) total outstanding dues of creditors o | R296-R297 | - | 
243 | iii) Other financial liabilities | R298-R299 | - | 
244 | Other current liabilities | R1065-R1066 | MISSING_FROM_STRUCTURED(resolved) | 
245 | Provisions | R300-R301 | - | 
246 | Current tax liabilities (net) | R302-R303 | - | 
247 | Total current liabilities | R304-R305 | - | 
248 | Total equity and liabilities | R306-R307 | - | 
(line items in this statement: 38)

### CONSOLIDATED CASH FLOW (pages 6-7)
LINE | line item | ROW_IDs | A2 flags | note
264 | Profit before tax (i) | R310-R312 | - | 
266 | Finance costs | R313-R315 | - | 
267 | Depreciation and amortisation expenses | R316-R318 | - | 
268 | Unrealised foreign exchange loss/(gain) (net) | R319-R321 | - | 
269 | Interest income | R322-R324 | - | 
270 | Net gain on sale of current investments | R325-R327 | ZERO_STANDING(1 of 3 cells: R325) | 
271 | Other non-cash items | R1067-R1069 | MISSING_FROM_STRUCTURED(resolved) | 
272 | Total adjustments to reconcile profit (ii) | R328-R330 | - | 
273 | Operating profit before working capital changes (iii) = (i)  | R331-R333 | - | 
275 | (Increase)/decrease in inventories | R334-R336 | - | 
276 | (Increase)/decrease in trade receivables | R337-R339 | - | 
277 | Decrease/(increase) in other non-current financial assets | R340-R342 | - | 
278 | Decrease/(increase) in other current financial assets | R343-R345 | - | 
279 | Decrease/(increase) in other non-current assets | R346-R348 | - | 
280 | Decrease/(increase) in other current assets | R349-R351 | - | 
281 | Increase/(decrease) in trade payables | R352-R354 | - | 
282 | (Decrease)/increase in other current financial liabilities | R355-R357 | - | 
283 | (Decrease)/increase in other current liabilities | R358-R360 | - | 
284 | (Decrease)/increase in non-current provisions | R361-R363 | ZERO_STANDING(1 of 3 cells: R362) | 
285 | (Decrease)/increase in current provisions | R364-R366 | - | 
286 | Total changes in working capital (iv) | R367-R369 | - | 
287 | Cash generated from/(used in) operating activities (v) = (ii | R370-R372 | - | 
288 | Less: Taxes paid (Net of refund) (vi) | R373-R375 | - | 
289 | Net cash generated from/(used in) operating activities (A) = | R376-R378 | - | 
291 | Purchase of property, plant and equipment (including right-o | R379-R381 | - | 
292 | Government grant received for capital asset | R382-R384 | ZERO_STANDING(2 of 3 cells: R382-R383) | 
293 | Proceeds from sale of property, plant and equipment | R385-R387 | - | 
294 | (Increase)/decrease in deposits with banks | R388-R390 | - | 
295 | Purchase of Investment (Non current) | R391-R393 | ZERO_STANDING(2 of 3 cells: R391-R392) | 
296 | Purchase of current investment | R394-R396 | ZERO_STANDING(1 of 3 cells: R394) | 
297 | Proceeds from sale of current investments | R397-R399 | ZERO_STANDING(1 of 3 cells: R397) | 
298 | Interest income | R400-R402 | - | 
299 | Cash (used in) investing activities (B) | R403-R405 | - | 
314 | Dividend paid | R407-R409 | ZERO_STANDING(1 of 3 cells: R408), CROSS_ENTITY_DIFF | cons 46.78 vs std 8.55 in H1 FY27 (see section 0) DIVIDEND_PAID_DIFF
315 | Proceeds from long-term borrowings | R410-R412 | ZERO_STANDING(2 of 3 cells: R410-R411) | 
316 | Repayment of long-term borrowings | R413-R415 | - | 
317 | Net proceeds from short-term borrowings | R416-R418 | - | 
318 | Decrease / (increase) in loans to employees | R419-R421 | - | 
319 | Interest paid | R422-R424 | - | 
320 | Cash generated from financing activities (C) | R425-R427 | - | 
321 | Net decrease in cash and cash equivalents D=(A+B+C) | R428-R430 | LABEL_ANOMALY | caption "Net decrease" but H1 FY27 value positive (LABEL_ANOMALY, R1005/R1040)
322 | Cash and cash equivalents at the beginning of the year (E) | R431-R433 | - | 
323 | Effect of exchange rate changes on cash and cash equivalents | R434-R436 | - | 
324 | Cash and cash equivalents at the end of the year (D+E+F) | R437-R439 | - | 
326 | Cash on hand | R440-R442 | - | 
327 | Balances with banks: - in current accounts | R443-R445 | - | 
328 | Balances with banks: - in current accounts (foreign currency | R446-R448 | - | 
329 | Balances with banks: - in cash credit accounts (surplus) | R449-R451 | ZERO_STANDING(2 of 3 cells: R449-R450) | 
330 | Balances with banks: - in EEFC current accounts | R452-R454 | - | 
331 | Balances with banks: - in deposits with original maturity of | R455-R457 | - | 
332 | Balance as per statement of cash flows | R458-R460 | - | 
(line items in this statement: 51)

### CONSOLIDATED NOTE 5 TABLE, standalone key numbers (page 8)
LINE | line item | ROW_IDs | A2 flags | note
362 | Total income from operations (Net) | R466-R471 | RESTATED | equals std P&L line 447 (R508-R513): identical
363 | Net profit/(loss) before tax (before exceptional items) | R472-R477 | RESTATED | equals std P&L line 459 (R568-R573): identical
364 | Net profit/(loss) before tax (after exceptional items) | R478-R483 | RESTATED | equals std P&L line 461 (R580-R585): identical
365 | Net profit/(loss) after tax | R484-R489 | RESTATED | equals std P&L line 466 (R604-R609): identical
366 | Total comprehensive income/(expense) | R490-R495 | RESTATED | equals std P&L line 471 (R628-R633): identical
(line items in this statement: 5)

### STANDALONE P&L (page 10)
LINE | line item | ROW_IDs | A2 flags | note
447 | 1 Revenue from operations | R508-R513 | - | 
448 | 2 Other income | R514-R519 | - | 
449 | 3 Total income (1+2) | R520-R525 | - | 
451 | Cost of materials consumed | R526-R531 | - | 
452 | Purchases of stock-in-trade | R532-R537 | ZERO_STANDING(all periods) | 
453 | Changes in inventories of finished goods and work-in-progres | R538-R543 | - | 
454 | Employee benefits expense | R544-R549 | - | 
455 | Finance costs | R550-R555 | - | 
456 | Depreciation and amortisation expense | R556-R561 | - | 
457 | Other expenses | R1070-R1075 | MISSING_FROM_STRUCTURED(resolved) | 
458 | 4 Total expenses | R562-R567 | - | 
459 | 5 Profit before exceptional items and tax (3-4) | R568-R573 | - | 
460 | 6 Exceptional items | R574-R579 | ZERO_STANDING(4 of 6 cells: R574+R576+R578-R579) | Exceptional item 13.18 booked in Q1 FY27 (quarter ended 30.06.2026) only; nil in Q2 FY27, nil in all FY26 columns. Nature not disclosed in a note.
461 | 7 Profit before tax (5-6) | R580-R585 | - | 
463 | Current tax | R586-R591 | ZERO_STANDING(1 of 6 cells: R587) | 
464 | Deferred tax | R592-R597 | - | 
465 | 8 Total tax expenses | R598-R603 | - | 
466 | 9 Profit for the period/year (7-8) | R604-R609 | - | 
468 | Items that will not be reclassified to profit or loss | R610-R615 | - | 
469 | Income tax relating to items that will not be reclassified t | R616-R621 | - | 
470 | 10 Other comprehensive income/(expenses) for the period/year | R622-R627 | - | 
471 | 11 Total comprehensive income for the period/year (9+10) | R628-R633 | - | 
472 | 12 Earnings per share (Face value of Rs 10/- each) (not annu | R634-R639 | - | 
473 | 12 Earnings per share (Face value of Rs 10/- each) (not annu | R641-R646 | - | 
474 | 13 Paid - up equity share capital (Face value of Rs 10/- eac | R647-R652 | - | 
(line items in this statement: 25)

### STANDALONE BALANCE SHEET (page 11)
LINE | line item | ROW_IDs | A2 flags | note
492 | Property, plant and equipment | R657-R658 | - | 
493 | Right-of-use assets | R659-R660 | - | 
494 | Capital work-in-progress | R661-R662 | - | 
495 | Other intangible assets | R1076-R1077 | MISSING_FROM_STRUCTURED(resolved) | 
496 | Intangible assets under development | R663-R664 | - | 
498 | i) Investments | R665-R666 | - | 
499 | ii) Other financial assets | R667-R668 | - | 
500 | Deferred tax assets (net) | R669-R670 | - | 
501 | Other non-current assets | R1078-R1079 | MISSING_FROM_STRUCTURED(resolved) | 
502 | Total non-current assets | R671-R672 | - | 
504 | Inventories | R673-R674 | - | 
506 | i) Trade receivables | R675-R676 | - | 
507 | ii) Cash and cash equivalents | R677-R678 | - | 
508 | iii) Bank balances other than cash and cash equivalents | R679-R680 | - | 
509 | iv) Loans | R681-R682 | - | 
510 | v) Other financial assets | R683-R684 | - | 
511 | Current tax assets (net) | R685-R686 | - | 
512 | Other current assets | R1080-R1081 | MISSING_FROM_STRUCTURED(resolved) | 
513 | Total current assets | R687-R688 | - | 
514 | Total assets | R689-R690 | - | 
517 | Equity share capital | R691-R692 | - | 
518 | Other equity | R1082-R1083 | MISSING_FROM_STRUCTURED(resolved) | 
519 | Total equity | R693-R694 | - | 
523 | i) Borrowings | R695-R696 | - | 
524 | Employee benefit obligations | R697-R698 | - | 
525 | Other non-current liabilities | R1084-R1085 | MISSING_FROM_STRUCTURED(resolved) | 
526 | Total non-current liabilities | R699-R700 | - | 
529 | i) Borrowings | R701-R702 | - | 
530 | ii) Trade payables (a) total outstanding dues of micro enter | R703-R704 | - | 
531 | ii) Trade payables (b) total outstanding dues of creditors o | R705-R706 | - | 
532 | iii) Other financial liabilities | R707-R708 | - | 
533 | Other current liabilities | R1086-R1087 | MISSING_FROM_STRUCTURED(resolved) | 
534 | Provisions | R709-R710 | - | 
535 | Current tax liabilities (net) | R711-R712 | ZERO_STANDING(1 of 2 cells: R711) | 
536 | Total current liabilities | R713-R714 | - | 
537 | Total equity and liabilities | R715-R716 | - | 
(line items in this statement: 36)

### STANDALONE CASH FLOW (pages 12-13)
LINE | line item | ROW_IDs | A2 flags | note
553 | Profit before tax (i) | R719-R721 | - | 
555 | Finance costs | R722-R724 | - | 
556 | Depreciation and amortisation expenses | R725-R727 | - | 
557 | Unrealised foreign exchange loss/(gain) (net) | R728-R730 | - | 
558 | Interest income | R731-R733 | - | 
559 | Net gain on sale of current investments | R734-R736 | ZERO_STANDING(1 of 3 cells: R734) | 
560 | Other non-cash items | R1088-R1090 | MISSING_FROM_STRUCTURED(resolved) | 
561 | Total adjustments to reconcile profit (ii) | R737-R739 | - | 
562 | Operating profit before working capital changes (iii) = (i)  | R740-R742 | - | 
564 | (Increase)/decrease in inventories | R743-R745 | - | 
565 | (Increase)/decrease in trade receivables | R746-R748 | - | 
566 | (Increase)/decrease in other non-current financial assets | R749-R751 | - | 
567 | (Increase)/decrease in other current financial assets | R752-R754 | - | 
568 | (Increase)/decrease in other non-current assets | R755-R757 | - | 
569 | (Increase)/decrease in other current assets | R758-R760 | - | 
570 | (Decrease)/increase in trade payables | R761-R763 | - | 
571 | (Decrease)/increase in other current financial liabilities | R764-R766 | - | 
572 | (Decrease)/increase in other current liabilities | R767-R769 | - | 
573 | (Decrease)/increase in non-current provisions | R770-R772 | ZERO_STANDING(1 of 3 cells: R771) | 
574 | (Decrease)/increase in current provisions | R773-R775 | - | 
575 | Total changes in working capital (iv) | R776-R778 | - | 
576 | Cash generated from/(used in) operating activities (v) = (ii | R779-R781 | - | 
577 | Less: Taxes paid (net of refund) (vi) | R782-R784 | - | 
578 | Net cash generated from/(used in) operating activities (A) = | R785-R787 | - | 
580 | Purchase of property, plant and equipment (including right-o | R788-R790 | - | 
581 | Government grant received for capital asset | R791-R793 | ZERO_STANDING(2 of 3 cells: R791-R792) | 
582 | Proceeds from sale of property, plant and equipment | R794-R796 | - | 
583 | (Increase)/decrease in deposits with banks | R797-R799 | - | 
584 | Purchase of Investment (Non current) | R800-R802 | ZERO_STANDING(2 of 3 cells: R800-R801) | 
585 | Purchase of Investment (Current) | R803-R805 | ZERO_STANDING(1 of 3 cells: R803) | 
586 | Proceeds from sale of current investments | R806-R808 | ZERO_STANDING(1 of 3 cells: R806) | 
587 | Interest income | R809-R811 | - | 
588 | Cash (used in) investing activities (B) | R812-R814 | - | 
603 | Dividend paid | R816-R818 | ZERO_STANDING(1 of 3 cells: R817), CROSS_ENTITY_DIFF | cons 46.78 vs std 8.55 in H1 FY27 (see section 0) DIVIDEND_PAID_DIFF
604 | Proceeds from Non-current borrowings | R819-R821 | ZERO_STANDING(2 of 3 cells: R819-R820) | 
605 | Repayment of long-term borrowings | R822-R824 | - | 
606 | Net proceeds from short-term borrowings | R825-R827 | - | 
607 | Decrease / (increase) in loans to employees | R828-R830 | - | 
608 | Interest paid | R831-R833 | - | 
609 | Cash generated from financing activities (C) | R834-R836 | - | 
610 | Net decrease in cash and cash equivalents D=(A+B+C) | R837-R839 | LABEL_ANOMALY | caption "Net decrease" but H1 FY27 value positive (LABEL_ANOMALY, R1005/R1040)
611 | Cash and cash equivalents at the beginning of the year (E) | R840-R842 | - | 
612 | Effect of exchange rate changes on cash and cash equivalents | R843-R845 | ZERO_STANDING(1 of 3 cells: R844) | 
613 | Cash and cash equivalents at the end of the year (D+E+F) | R846-R848 | - | 
615 | Cash on hand | R849-R851 | - | 
616 | Balances with banks: - in current accounts | R852-R854 | - | 
617 | Balances with banks: - in cash credit accounts (surplus) | R855-R857 | ZERO_STANDING(2 of 3 cells: R855-R856) | 
618 | Balances with banks: - in EEFC current accounts | R858-R860 | - | 
619 | Balances with banks: - in deposits with original maturity of | R861-R863 | - | 
620 | Balance as per statement of cash flows | R864-R866 | - | 
(line items in this statement: 50)

TOTAL line items: 241 (incl. 16 supplement lines). Check vs fulltext grep 241: match

### ZERO_STANDING register (all cells flagged nil / dash)
PAGE | LINE | line item | ROW_IDs
4 | 158 | 6 Exceptional items | R095,R097,R099-R100
4 | 169 | Income tax relating to items that will be reclassified to pr | R149-R154
4 | 173 | 12 Profit for the period/year attributable to: - Non control | R173-R178
4 | 176 | 13 Other comprehensive income/(expense) attributable to: - N | R191-R196
4 | 179 | 14 Total comprehensive income attributable to: - Non control | R209-R214
5 | 229 | Non-controlling interests | R282-R283
6 | 270 | Net gain on sale of current investments | R325
6 | 284 | (Decrease)/increase in non-current provisions | R362
6 | 292 | Government grant received for capital asset | R382-R383
6 | 295 | Purchase of Investment (Non current) | R391-R392
6 | 296 | Purchase of current investment | R394
6 | 297 | Proceeds from sale of current investments | R397
7 | 314 | Dividend paid | R408
7 | 315 | Proceeds from long-term borrowings | R410-R411
7 | 329 | Balances with banks: - in cash credit accounts (surplus) | R449-R450
10 | 452 | Purchases of stock-in-trade | R532-R537
10 | 460 | 6 Exceptional items | R574,R576,R578-R579
10 | 463 | Current tax | R587
11 | 535 | Current tax liabilities (net) | R711
12 | 559 | Net gain on sale of current investments | R734
12 | 573 | (Decrease)/increase in non-current provisions | R771
12 | 581 | Government grant received for capital asset | R791-R792
12 | 584 | Purchase of Investment (Non current) | R800-R801
12 | 585 | Purchase of Investment (Current) | R803
12 | 586 | Proceeds from sale of current investments | R806
13 | 603 | Dividend paid | R817
13 | 604 | Proceeds from Non-current borrowings | R819-R820
13 | 612 | Effect of exchange rate changes on cash and cash equivalents | R844
13 | 617 | Balances with banks: - in cash credit accounts (surplus) | R855-R856
ZERO_STANDING lines: 29; cells: 69. Standing lines nil in ALL periods: non-controlling interest rows (profit, OCI, TCI attribution, balance sheet) and tax on reclassifiable OCI (cons). These are template lines for a group with no NCI.

## 3. OTHER NUMBER ROWS (identifiers, addresses, regulation cites, times; not financial-table cells)
ROW_IDs | category | A2 flags | note
R001 | letter reference number | - | 
R002 | NSE address PIN | - | 
R003 | NSE scrip symbol | - | 
R004 | BSE address PIN | - | 
R005 | BSE scrip code | - | 
R006 | SEBI LODR regulations cited | - | 
R007 | auditor firm registration number | RESTATED | 
R008 | board meeting start time | MEETING_TIME | meeting 11:30 A.M. to 03:45 P.M. = 4 h 15 min
R009 | board meeting end time | MEETING_TIME | meeting 11:30 A.M. to 03:45 P.M. = 4 h 15 min
R010 | digital signature timestamp | SIGNATURE_TS | signed 15:48:12 +05:30, 3 minutes AFTER meeting end 03:45 P.M.; no early-signature flag
R011 | company secretary membership number | - | 
R012,R497 | accounting standard cited | - | 
R013,R016,R464,R498,R500,R870 | Companies Act section cited | - | 
R014,R021,R463,R869 | Listing Regulations cited | - | 
R015,R499 | review standard cited | - | 
R017 | SEBI circular regulation cited | - | 
R018,R504 | auditor registered office PIN | - | 
R019 | auditor office number | - | 
R020,R505 | auditor landline | - | 
R022,R501 | auditor FRN | RESTATED | 
R023,R502 | auditor partner membership number | - | 
R024 | UDIN consolidated review report | - | 
R025,R243,R309,R406,R462,R506,R656,R718,R815,R868 | company CIN | RESTATED | 
R026 | registered office plot number | - | 
R027 | registered office PIN | - | 
R028,R507 | company telephone | - | 
R227,R240,R640,R653 | face value per share | RESTATED | 
R241 | 17 Other equity excluding revaluation reserve; Year ended 31.03.2026 (Audited) | - | 
R242,R308,R461,R655,R717,R867 | notes page range | - | 
R465,R871 | segment standard cited | - | 
R496,R872 | director DIN | - | 
R503 | UDIN standalone review report | - | 
R654 | 14 Other equity excluding revaluation reserve; Year ended 31.03.2026 (Audited) | - | 
(non-table NUMBER rows: 67)

## 4. AGENDA ITEMS (Board outcome / cover letter, page 1)
ROW_IDs | item | A2 flags | note
R006-R007,R876-R878,R920-R922 | Item 1 (only item): approval of standalone and consolidated unaudited results, quarter and half year ended 30 Sep 2026; reviewed by Audit Committee, approved by Board, 19 Oct 2026; Reg 30 and 33 | - | cover letter ref R001 (TCPCL/SEC/2026-27/00054)
R008-R009 | Meeting times: start 11:30 A.M., end 03:45 P.M. (4 h 15 min, long for a results-only meeting) | MEETING_TIME | Letter lists no other agenda item, so A3 should note the duration with no explained driver. Flag LONG_MEETING_NO_AGENDA.
NONE FOUND | AR approval, AGM notice, record date, dividend, director appointment, auditor change, scrutinizer, ESOP grants, capital-raising enabling resolutions | NOT_DISCLOSED | no such item in the letter; A3 should not infer. (Dividend: cash flow shows dividend paid 46.78 cons / 8.55 std in H1 FY27, see section 0.)

## 5. ANNEXURES AND DIRECTOR PROFILES
NONE FOUND | no annexure tables other than the enclosed statements and review reports; no director profiles in this filing | NOT_DISCLOSED | -

## 6. AUDITOR REPORT PARAGRAPHS
PARA | ROW_IDs | A2 flags | note
Cons para 1: scope, Reg 33, quarter and half year to 30 Sep 2026 | R925,R980 | - | 
Cons para 2: management responsibility, Ind AS 34 | R981 | - | 
Cons para 3: SRE 2410, review not audit, no audit opinion | R012-R016,R882,R982-R983 | - | no audit opinion expressed (limited review)
Cons para 4: SEBI circular Reg 33(8) procedures | R017 | - | 
Cons para 5: entities included (a Holding, b USA Inc, c Europe B.V.), auditor office block | R018-R020,R883-R887,R984 | - | consolidation scope: holding + 2 wholly owned subsidiaries; all subsidiaries covered by the review (not carved out as unaudited / management-furnished)
Cons para 6: unmodified conclusion, UDIN, signature (page 3) | R021-R024,R888-R890,R926,R985 | - | conclusion unmodified; no Emphasis of Matter, no Other Matter, no Going Concern language in either report
Std para 1: scope | R954,R1019 | - | 
Std para 2: management responsibility | R497-R498 | - | 
Std para 3: SRE 2410, review not audit | R499-R500,R905,R1020 | - | no audit opinion expressed (limited review)
Std para 4: unmodified conclusion, UDIN, signature | R501-R504,R906-R907,R955,R1021 | - | Std report has 4 paras, cons has 6; no SEBI circular 33(8) para and no entity list in std (single entity)
R007,R022-R024,R503,R889,R906 | UDINs: cons 26434585QMVVAA6682 (R024), std 26434585DBUAOH1630 (R503); partner CA Basant Chandak M.No. 434585 (R023, R889, R906); report dates 19 Oct 2026 (R926, R955); place Vadodara | - | two distinct UDINs, same partner, same date as board meeting.

## 7. ENTITIES
ROW_IDs | entity | A2 flags | note
R883 | Tatva Chintan Pharma Chem Limited, Holding Company | - | consolidation list a
R884 | Tatva Chintan USA Inc., Wholly Owned Subsidiary | - | consolidation list b; no prior ledger, ENTITY_CHANGE not testable
R885 | Tatva Chintan Europe B.V., Wholly Owned Subsidiary | - | consolidation list c
R873-R882,R886-R916 | exchanges, regulator, committees, auditor NDJ & Co (FRN 136345W), signatories (Ishwar Nayi CS; Chintan N. Shah CMD DIN 00183618), ICAI, places of signing, stamps, EEFC accounts, segment (specialty chemicals), registered office | - | 41 supporting ENTITY rows; repeated company-name headers RESTATED

## 8. SIGNATURE BLOCKS
ROW_IDs | signatory | A2 flags | note
R010-R011,R880,R923-R924 | Ishwar Nayi, CS and Compliance Officer, M.No. A37444; digital signature 2026.10.19 15:48:12 +05:30 | SIGNATURE_TS | 3 minutes after stated meeting end (R009); not an early-signature flag
R023-R024,R889,R926 | CA Basant Chandak, Partner, NDJ & Co, cons review report, 19 Oct 2026, Vadodara | - | -
R503,R906,R955 | CA Basant Chandak, Partner, NDJ & Co, std review report, 19 Oct 2026, Vadodara | - | -
R902,R953 | Chintan N. Shah, Chairman and Managing Director, DIN 00183618, cons statement, 19 Oct 2026, Vadodara | - | -
R915,R976 | Chintan N. Shah, CMD, std statement, 19 Oct 2026, Vadodara | - | -

## 9. DATE, FORWARD AND REMAINING QUALIFIER ROWS
ROW_IDs | category | A2 flags | note
R920-R976 | DATE rows (57): letter, meeting, signature, review-period, report and note dates, and table column period headings for each statement | RESTATED (column headings repeat per statement) | all dates 19 Oct 2026; Q2 FY27 period end 30 Sep 2026
R917-R919 | FORWARD rows (3): website availability commitments only (cover letter, cons note 6, std note 5) | - | no forward-looking business statement in this filing
R977-R979 | remaining QUALIFIER rows (3) not already listed in sections 1 and 6 | - | -

## 10. MISSING_FROM_STRUCTURED (closed by A1 supplement R1049-R1090)
LINE | item | A2 flags | new ROW_IDs
155 | Other expenses | MISSING_FROM_STRUCTURED (resolved, was omitted in first pass) | R1049-R1054
204 | Other intangible assets | MISSING_FROM_STRUCTURED (resolved, was omitted in first pass) | R1055-R1056
210 | Other non-current assets | MISSING_FROM_STRUCTURED (resolved, was omitted in first pass) | R1057-R1058
221 | Other current assets | MISSING_FROM_STRUCTURED (resolved, was omitted in first pass) | R1059-R1060
227 | Other equity | MISSING_FROM_STRUCTURED (resolved, was omitted in first pass) | R1061-R1062
236 | Other non-current liabilities | MISSING_FROM_STRUCTURED (resolved, was omitted in first pass) | R1063-R1064
244 | Other current liabilities | MISSING_FROM_STRUCTURED (resolved, was omitted in first pass) | R1065-R1066
271 | Other non-cash items | MISSING_FROM_STRUCTURED (resolved, was omitted in first pass) | R1067-R1069
457 | Other expenses | MISSING_FROM_STRUCTURED (resolved, was omitted in first pass) | R1070-R1075
495 | Other intangible assets | MISSING_FROM_STRUCTURED (resolved, was omitted in first pass) | R1076-R1077
501 | Other non-current assets | MISSING_FROM_STRUCTURED (resolved, was omitted in first pass) | R1078-R1079
512 | Other current assets | MISSING_FROM_STRUCTURED (resolved, was omitted in first pass) | R1080-R1081
518 | Other equity | MISSING_FROM_STRUCTURED (resolved, was omitted in first pass) | R1082-R1083
525 | Other non-current liabilities | MISSING_FROM_STRUCTURED (resolved, was omitted in first pass) | R1084-R1085
533 | Other current liabilities | MISSING_FROM_STRUCTURED (resolved, was omitted in first pass) | R1086-R1087
560 | Other non-cash items | MISSING_FROM_STRUCTURED (resolved, was omitted in first pass) | R1088-R1090
supplement lines: 16; cells: 42


## ID ACCOUNTABILITY DETAIL
orphans after full sweep: []