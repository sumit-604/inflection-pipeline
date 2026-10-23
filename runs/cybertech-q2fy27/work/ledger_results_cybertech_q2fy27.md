=== A2 COUNT TEST ===
category: notes            grep_count: 7    sweep_count: 7    match: yes   (Notes 1-6 plus Note 5 second paragraph R738; R732 header)
category: line_items       grep_count: 191  sweep_count: 191  match: yes   (financial table line items R001-R551; grep by distinct page/line, sweep by label group)
category: embedded_numbers grep_count: 42   sweep_count: 42   match: yes   (non-table numbers R552-R593)
category: zero_standing    grep_count: 45   sweep_count: 45   match: yes   (45 dash cells across 27 line items)
category: agenda_items     grep_count: 1    sweep_count: 1    match: yes   (results only; letter says inter-alia, see flag)
category: auditor_paras    grep_count: 7    sweep_count: 7    match: yes   (R698-R701 consol, R716-R718 standalone; no EoM, no Going Concern)
category: entities         grep_count: 46   sweep_count: 46   match: yes
category: forward          grep_count: 3    sweep_count: 3    match: yes
category: dates            grep_count: 51   sweep_count: 51   match: yes
category: qualifiers       grep_count: 46   sweep_count: 46   match: yes
category: signature_blocks grep_count: 10   sweep_count: 10   match: yes   (R663-R671 auditor x9, R675 CS)
gate_a2: pass
=== END COUNT TEST ===

ids_in_structured: 739 | ids_referenced_in_ledger: 739 | orphan_ids: [] | match: yes
(NUMBER R001-R593 via sections 2-3; ENTITY R594-R639; FORWARD R640-R642; DATE R643-R693; QUALIFIER R694-R739.)

Row format: ROW_ID | category | location | A2 flags | cross-ref / materiality note

## 1 NOTES

R732 | notes | p10 |  | Notes header
R733 | notes | p10 |  | Note 1 board/AC approval
R734 | notes | p10 | ENTITY_WORDING_DIFF | Note 2 consolidation; Canada described as subsidiary of USA entity, compare R609-R611 auditor list
R735 | notes | p10 | RESTATED | Note 3 ESOP 1,00,000 shares; cross R579-R582
R736 | notes | p10 |  | Note 4 single segment, cross R629/R586
R737 | notes | p10 | RESTATED | Note 5 Labour Codes; cross R640,R642,R583,R584,R686-R688
R738 | notes | p10 |  | Note 5 para 2; cross R641
R739 | notes | p10 |  | Note 6 regrouping; regrouped figures not itemised

## 2 LINE ITEMS, financial tables (191 items; 45 zero cells in 27 items flagged ZERO_STANDING)

R001-R006 | line_item | p3 L100 |  | consolidated 1 Revenue from operations (6 cells)
R007-R012 | line_item | p3 L101 |  | consolidated 2 Other income (6 cells)
R013-R018 | line_item | p3 L102 |  | consolidated 3 Total Income (1+2) (6 cells)
R019-R024 | line_item | p3 L104 |  | consolidated a) Outsourced service costs (6 cells)
R025-R030 | line_item | p3 L105 |  | consolidated b) Employee benefits expense (6 cells)
R031-R036 | line_item | p3 L106 |  | consolidated c) Finance costs (6 cells)
R037-R042 | line_item | p3 L107 |  | consolidated d) Depreciation and amortization expense (6 cells)
R043-R048 | line_item | p3 L108 |  | consolidated e) Other expenses (6 cells)
R049-R054 | line_item | p3 L109 |  | consolidated Total Expenses (6 cells)
R055-R060 | line_item | p3 L110 |  | consolidated 5 Profit before Tax (3-4) (6 cells)
R061-R066 | line_item | p3 L112 |  | consolidated a) Current Tax (6 cells)
R067-R072 | line_item | p3 L113 |  | consolidated b) Deferred Tax (6 cells)
R073-R078 | line_item | p3 L114 | ZERO_STANDING (2 of 6 cells: R075,R077) | consolidated c) Tax adjustments for earlier years (6 cells)
R079-R084 | line_item | p3 L115 |  | consolidated 7 Profit for the period (5-6) (6 cells)
R085-R090 | line_item | p3 L118 | ZERO_STANDING (3 of 6 cells: R085,R086,R088) | consolidated a Remeasurement of the net defined benefit liabilities (6 cells)
R091-R096 | line_item | p3 L119 | ZERO_STANDING (3 of 6 cells: R091,R092,R094) | consolidated b Income tax relating to items that will not be reclassified to profit (6 cells)
R097-R102 | line_item | p3 L121 |  | consolidated a Foreign currency translation reserve (6 cells)
R103-R108 | line_item | p3 L122 | ZERO_STANDING (all periods) | consolidated b Income tax relating to items that will not be reclassified to profit (6 cells)
R109-R114 | line_item | p3 L123 |  | consolidated 9 Total Comprehensive Income for the period (7+8) (6 cells)
R115-R120 | line_item | p3 L124 |  | consolidated 10 Paid up equity share capital (Face value: Rs.10 per share) (6 cells)
R121-R123 | line_item | p3 L125 |  | consolidated 11 Other equity (3 cells)
R124-R129 | line_item | p3 L127 |  | consolidated Basic (Not annualised) (6 cells)
R130-R135 | line_item | p3 L128 |  | consolidated Diluted (Not annualised) (6 cells)
R136-R137 | line_item | p4 L142 |  | consolidated (a) Property, plant and equipment (2 cells)
R138-R139 | line_item | p4 L143 |  | consolidated (b) Right of use (Assets) (2 cells)
R140-R141 | line_item | p4 L144 |  | consolidated (c) Investment Property (2 cells)
R142-R143 | line_item | p4 L145 | ZERO_STANDING (1 of 2 cells: R142) | consolidated (d) Intangible assets (2 cells)
R144-R145 | line_item | p4 L147 | ZERO_STANDING (1 of 2 cells: R144) | consolidated (i) Investments [non-current] (2 cells)
R146-R147 | line_item | p4 L148 |  | consolidated (ii) Loans [non-current] (2 cells)
R148-R149 | line_item | p4 L149 |  | consolidated (iii) Other financial assets [non-current] (2 cells)
R150-R151 | line_item | p4 L150 |  | consolidated (f) Other non-current assets (2 cells)
R152-R153 | line_item | p4 L151 |  | consolidated Subtotal-Non-Current Assets (2 cells)
R154-R155 | line_item | p4 L154 |  | consolidated (i) Investments [current] (2 cells)
R156-R157 | line_item | p4 L155 |  | consolidated (ii) Trade receivables (2 cells)
R158-R159 | line_item | p4 L156 |  | consolidated (iii) Cash and cash equivalents (2 cells)
R160-R161 | line_item | p4 L157 |  | consolidated (iv) Bank balances other than (iii) above (2 cells)
R162-R163 | line_item | p4 L158 |  | consolidated (v) Loans [current] (2 cells)
R164-R165 | line_item | p4 L159 |  | consolidated (vi) Other Financial Assets [current] (2 cells)
R166-R167 | line_item | p4 L160 | ZERO_STANDING (1 of 2 cells: R166) | consolidated (b) Current Tax Assets (Net) (2 cells)
R168-R169 | line_item | p4 L161 |  | consolidated (c) Other current assets (2 cells)
R170-R171 | line_item | p4 L162 |  | consolidated Subtotal-Current Assets (2 cells)
R172-R173 | line_item | p4 L163 |  | consolidated TOTAL ASSETS (2 cells)
R174-R175 | line_item | p4 L166 |  | consolidated (a) Equity share capital (2 cells)
R176-R177 | line_item | p4 L167 |  | consolidated (b) Other equity (2 cells)
R178-R179 | line_item | p4 L168 |  | consolidated Subtotal-Equity (2 cells)
R180-R181 | line_item | p4 L172 |  | consolidated (i) Lease Liabilities [non-current] (2 cells)
R182-R183 | line_item | p4 L173 |  | consolidated (ii) Other financial liabilities [non-current] (2 cells)
R184-R185 | line_item | p4 L174 |  | consolidated (b) Deferred tax liabilities (net) (2 cells)
R186-R187 | line_item | p4 L175 |  | consolidated Sub total-Non-Current liabilities (2 cells)
R188-R189 | line_item | p4 L178 | ZERO_STANDING (1 of 2 cells: R188) | consolidated (i) Borrowings (2 cells)
R190-R191 | line_item | p4 L179 |  | consolidated (ii) Lease Liabilities [current] (2 cells)
R192-R193 | line_item | p4 L181 |  | consolidated -Total outstanding of Micro and Small Enterprises (2 cells)
R194-R195 | line_item | p4 L182 |  | consolidated -Total outstanding of Creditors other than Micro and Small Enterprises (2 cells)
R196-R197 | line_item | p4 L183 |  | consolidated (iv) Other financial liabilities [current] (2 cells)
R198-R199 | line_item | p4 L184 |  | consolidated (b) Other current liabilities (2 cells)
R200-R201 | line_item | p4 L185 |  | consolidated (c) Provisions (2 cells)
R202-R203 | line_item | p4 L186 |  | consolidated (d) Current tax liabilities (Net) (2 cells)
R204-R205 | line_item | p4 L187 |  | consolidated Subtotal-Current Liabilities (2 cells)
R206-R207 | line_item | p4 L188 |  | consolidated Total Liabilities (2 cells)
R208-R209 | line_item | p4 L189 |  | consolidated TOTAL EQUITY AND LIABILITIES (2 cells)
R210-R211 | line_item | p5 L201 |  | consolidated Profit before tax (2 cells)
R212-R213 | line_item | p5 L203 |  | consolidated Depreciation and amortisation expense (2 cells)
R214-R215 | line_item | p5 L204 |  | consolidated Unrealised foreign exchange gain (2 cells)
R216-R217 | line_item | p5 L205 | ZERO_STANDING (1 of 2 cells: R216) | consolidated Loss on assets disposed / discarded (net) (2 cells)
R218-R219 | line_item | p5 L206 |  | consolidated Interest and dividend income (2 cells)
R220-R221 | line_item | p5 L207 |  | consolidated Finance costs (2 cells)
R222-R223 | line_item | p5 L208 | ZERO_STANDING (1 of 2 cells: R222) | consolidated Provision for doubtful receivables, advances and expected credit losse (2 cells)
R224-R225 | line_item | p5 L209 | ZERO_STANDING (1 of 2 cells: R224) | consolidated Sundry credit balances written back (net) (2 cells)
R226-R227 | line_item | p5 L210 | ZERO_STANDING (1 of 2 cells: R227) | consolidated Reversal of expected credit losses (2 cells)
R228-R229 | line_item | p5 L211 |  | consolidated Profit on sale of investments in mutual funds (2 cells)
R230-R231 | line_item | p5 L212 |  | consolidated Gain on fair valuation of investments in mutual funds and Treasury bil (2 cells)
R232-R233 | line_item | p5 L213 |  | consolidated Adjustments subtotal [unlabelled] (2 cells)
R234-R235 | line_item | p5 L214 |  | consolidated Operating profit before working capital changes (2 cells)
R236-R237 | line_item | p5 L216 |  | consolidated Decrease in trade receivables (2 cells)
R238-R239 | line_item | p5 L217 |  | consolidated (Increase) / Decrease in loans, other financial assets and other asset (2 cells)
R240-R241 | line_item | p5 L218 |  | consolidated Increase in trade payables, other financial liabilities and other liab (2 cells)
R242-R243 | line_item | p5 L219 |  | consolidated Working capital changes subtotal [unlabelled] (2 cells)
R244-R245 | line_item | p5 L220 |  | consolidated Cash generated from operations (2 cells)
R246-R247 | line_item | p5 L221 |  | consolidated Direct taxes paid (net) (2 cells)
R248-R249 | line_item | p5 L222 |  | consolidated Net cash flow generated from operating activities (A) (2 cells)
R250-R251 | line_item | p5 L224 |  | consolidated Purchase of property, plant & equipment (Including capital work-in-pro (2 cells)
R252-R253 | line_item | p5 L225 | ZERO_STANDING (1 of 2 cells: R252) | consolidated Proceeds from sale of property, plant & equipment (2 cells)
R254-R255 | line_item | p5 L226 |  | consolidated Purchase of investments (2 cells)
R256-R257 | line_item | p5 L227 |  | consolidated Proceeds from sale of investments (2 cells)
R258-R259 | line_item | p5 L228 |  | consolidated Fixed deposits placed with banks (2 cells)
R260-R261 | line_item | p5 L229 |  | consolidated Proceeds from fixed deposits matured (2 cells)
R262-R263 | line_item | p5 L230 |  | consolidated Interest and Dividend received (2 cells)
R264-R265 | line_item | p5 L231 |  | consolidated Net cash flow generated from /(used in) investing activities (B) (2 cells)
R266-R267 | line_item | p5 L233 |  | consolidated Repayment of short-term borrowings (net) (2 cells)
R268-R269 | line_item | p5 L234 | ZERO_STANDING (1 of 2 cells: R269) | consolidated Proceeds from issue of equity shares under ESOP (including securities  (2 cells)
R270-R271 | line_item | p5 L235 | ZERO_STANDING (1 of 2 cells: R271) | consolidated Buyback of equity shares (including transaction costs) (2 cells)
R272-R273 | line_item | p5 L236 |  | consolidated Finance cost paid (2 cells)
R274-R275 | line_item | p5 L237 |  | consolidated Payment of lease liabilities (2 cells)
R276-R277 | line_item | p5 L238 |  | consolidated Net cash used in financing activities (C) (2 cells)
R278-R279 | line_item | p5 L239 |  | consolidated Net Increase/(decrease) in cash & cash equivalents (A + B + C) (2 cells)
R280-R281 | line_item | p5 L240 |  | consolidated Cash & cash equivalents - Opening (2 cells)
R282-R283 | line_item | p5 L241 |  | consolidated Effect of exchange rate changes on Cash & Cash Equivalents (2 cells)
R284-R285 | line_item | p5 L242 |  | consolidated Cash & cash equivalents - Closing (2 cells)
R286-R291 | line_item | p7 L286 |  | standalone 1 Revenue from operations (6 cells)
R292-R297 | line_item | p7 L287 |  | standalone 2 Other income (6 cells)
R298-R303 | line_item | p7 L288 |  | standalone 3 Total Income (1+2) (6 cells)
R304-R309 | line_item | p7 L290 |  | standalone a) Outsourced service costs (6 cells)
R310-R315 | line_item | p7 L291 |  | standalone b) Employee benefits expense (6 cells)
R316-R321 | line_item | p7 L292 |  | standalone c) Finance costs (6 cells)
R322-R327 | line_item | p7 L293 |  | standalone d) Depreciation and amortization expense (6 cells)
R328-R333 | line_item | p7 L294 |  | standalone e) Other expenses (6 cells)
R334-R339 | line_item | p7 L295 |  | standalone Total Expenses (6 cells)
R340-R345 | line_item | p7 L296 |  | standalone 5 Profit before Tax (3-4) (6 cells)
R346-R351 | line_item | p7 L298 |  | standalone a) Current Tax (6 cells)
R352-R357 | line_item | p7 L299 |  | standalone b) Deferred Tax (6 cells)
R358-R363 | line_item | p7 L300 | ZERO_STANDING (5 of 6 cells: R358,R359,R360,R361,R362) | standalone c) Tax adjustments for earlier years (6 cells)
R364-R369 | line_item | p7 L301 |  | standalone 7 Profit for the period (5-6) (6 cells)
R370-R375 | line_item | p7 L304 | ZERO_STANDING (3 of 6 cells: R370,R371,R373) | standalone a Remeasurement of the net defined benefit liabilities (6 cells)
R376-R381 | line_item | p7 L305 | ZERO_STANDING (3 of 6 cells: R376,R377,R379) | standalone b Income tax relating to items that will not be reclassified to profit (6 cells)
R382-R387 | line_item | p7 L306 |  | standalone 9 Total Comprehensive Income for the period (7+8) (6 cells)
R388-R393 | line_item | p7 L307 |  | standalone 10 Paid up equity share capital (Face value: Rs.10 per share) (6 cells)
R394-R396 | line_item | p7 L308 |  | standalone 11 Other equity (3 cells)
R397-R402 | line_item | p7 L310 |  | standalone Basic (Not annualised) (6 cells)
R403-R408 | line_item | p7 L311 |  | standalone Diluted (Not annualised) (6 cells)
R409-R410 | line_item | p8 L324 |  | standalone (a) Property, plant and equipment (2 cells)
R411-R412 | line_item | p8 L325 |  | standalone (b) Right of use (Assets) (2 cells)
R413-R414 | line_item | p8 L326 |  | standalone (c) Investment Property (2 cells)
R415-R416 | line_item | p8 L327 | ZERO_STANDING (1 of 2 cells: R415) | standalone (d) Intangible assets (2 cells)
R417-R418 | line_item | p8 L329 |  | standalone (i) Investments [non-current] (2 cells)
R419-R420 | line_item | p8 L330 |  | standalone (ii) Loans [non-current] (2 cells)
R421-R422 | line_item | p8 L331 |  | standalone (iii) Other financial assets [non-current] (2 cells)
R423-R424 | line_item | p8 L332 |  | standalone (f) Other non-current assets (2 cells)
R425-R426 | line_item | p8 L333 |  | standalone Subtotal-Non-Current Assets (2 cells)
R427-R428 | line_item | p8 L336 |  | standalone (i) Investments [current] (2 cells)
R429-R430 | line_item | p8 L337 |  | standalone (ii) Trade receivables (2 cells)
R431-R432 | line_item | p8 L338 |  | standalone (iii) Cash and cash equivalents (2 cells)
R433-R434 | line_item | p8 L339 |  | standalone (iv) Bank balances other than (iii) above (2 cells)
R435-R436 | line_item | p8 L340 |  | standalone (v) Loans [current] (2 cells)
R437-R438 | line_item | p8 L341 |  | standalone (vi) Other Financial Assets [current] (2 cells)
R439-R440 | line_item | p8 L342 |  | standalone (b) Other current assets (2 cells)
R441-R442 | line_item | p8 L343 |  | standalone Subtotal-Current Assets (2 cells)
R443-R444 | line_item | p8 L344 |  | standalone TOTAL ASSETS (2 cells)
R445-R446 | line_item | p8 L347 |  | standalone (a) Equity share capital (2 cells)
R447-R448 | line_item | p8 L348 |  | standalone (b) Other equity (2 cells)
R449-R450 | line_item | p8 L349 |  | standalone Subtotal-Equity (2 cells)
R451-R452 | line_item | p8 L353 |  | standalone (i) Lease Liabilities [non-current] (2 cells)
R453-R454 | line_item | p8 L354 |  | standalone (ii) Other financial liabilities [non-current] (2 cells)
R455-R456 | line_item | p8 L355 |  | standalone (b) Deferred tax liabilities (net) (2 cells)
R457-R458 | line_item | p8 L356 |  | standalone Sub total-Non-Current liabilities (2 cells)
R459-R460 | line_item | p8 L359 | ZERO_STANDING (1 of 2 cells: R459) | standalone (i) Borrowings (2 cells)
R461-R462 | line_item | p8 L360 |  | standalone (ii) Lease liabilities [current] (2 cells)
R463-R464 | line_item | p8 L362 |  | standalone -Total outstanding of Micro and Small Enterprises (2 cells)
R465-R466 | line_item | p8 L363 |  | standalone -Total outstanding of Creditors other than Micro and Small Enterprises (2 cells)
R467-R468 | line_item | p8 L364 |  | standalone (iv) Other financial liabilities [current] (2 cells)
R469-R470 | line_item | p8 L365 |  | standalone (b) Other current liabilities (2 cells)
R471-R472 | line_item | p8 L366 |  | standalone (c) Provisions (2 cells)
R473-R474 | line_item | p8 L367 |  | standalone (d) Current tax liabilities (Net) (2 cells)
R475-R476 | line_item | p8 L368 |  | standalone Subtotal-Current Liabilities (2 cells)
R477-R478 | line_item | p8 L369 |  | standalone Total Liabilities (2 cells)
R479-R480 | line_item | p8 L370 |  | standalone TOTAL EQUITY AND LIABILITIES (2 cells)
R481-R482 | line_item | p9 L382 |  | standalone Profit before tax (2 cells)
R483-R484 | line_item | p9 L384 |  | standalone Depreciation and amortisation expense (2 cells)
R485-R486 | line_item | p9 L385 |  | standalone Unrealised foreign exchange gain (2 cells)
R487-R488 | line_item | p9 L386 | ZERO_STANDING (1 of 2 cells: R487) | standalone Loss on assets disposed / discarded (net) (2 cells)
R489-R490 | line_item | p9 L387 |  | standalone Interest income (2 cells)
R491-R492 | line_item | p9 L388 |  | standalone Finance costs (2 cells)
R493-R494 | line_item | p9 L389 | ZERO_STANDING (1 of 2 cells: R494) | standalone Reversal of expected credit losses (2 cells)
R495-R496 | line_item | p9 L390 |  | standalone Profit on sale of investments in mutual funds (2 cells)
R497-R498 | line_item | p9 L391 |  | standalone Gain on fair valuation of investments in mutual funds (2 cells)
R499-R500 | line_item | p9 L392 |  | standalone Adjustments subtotal [unlabelled] (2 cells)
R501-R502 | line_item | p9 L393 |  | standalone Operating profit before working capital changes (2 cells)
R503-R504 | line_item | p9 L395 |  | standalone Decrease in trade receivables (2 cells)
R505-R506 | line_item | p9 L396 |  | standalone Decrease in loans, other financial assets and other assets (2 cells)
R507-R508 | line_item | p9 L397 |  | standalone Increase in trade payables, other financial liabilities and other liab (2 cells)
R509-R510 | line_item | p9 L398 |  | standalone Working capital changes subtotal [unlabelled] (2 cells)
R511-R512 | line_item | p9 L399 |  | standalone Cash generated from operations (2 cells)
R513-R514 | line_item | p9 L400 |  | standalone Direct taxes paid (net) (2 cells)
R515-R516 | line_item | p9 L401 |  | standalone Net cash flow generated from operating activities (A) (2 cells)
R517-R518 | line_item | p9 L403 |  | standalone Purchase of property, plant & equipment (Including capital work-in-pro (2 cells)
R519-R520 | line_item | p9 L404 | ZERO_STANDING (1 of 2 cells: R519) | standalone Proceeds from sale of property, plant & equipment (2 cells)
R521-R522 | line_item | p9 L405 | ZERO_STANDING (1 of 2 cells: R522) | standalone Investment in a wholly owned subsidiary (2 cells)
R523-R524 | line_item | p9 L406 | ZERO_STANDING (1 of 2 cells: R524) | standalone Purchase of investments (2 cells)
R525-R526 | line_item | p9 L407 | ZERO_STANDING (1 of 2 cells: R526) | standalone Proceeds from sale of Investments (2 cells)
R527-R528 | line_item | p9 L408 |  | standalone Fixed deposits placed with banks (2 cells)
R529-R530 | line_item | p9 L409 |  | standalone Proceeds from fixed deposits matured (2 cells)
R531-R532 | line_item | p9 L410 |  | standalone Interest received (2 cells)
R533-R534 | line_item | p9 L411 |  | standalone Net cash flow generated from / (used in) investing activities (B) (2 cells)
R535-R536 | line_item | p9 L413 |  | standalone Repayments of short-term borrowings (net) (2 cells)
R537-R538 | line_item | p9 L414 | ZERO_STANDING (1 of 2 cells: R538) | standalone Proceeds from issue of equity shares under ESOP (including securities  (2 cells)
R539-R539 | line_item | p9 L415 |  | standalone Buyback of equity shares (including transaction costs) (1 cells)
R540-R541 | line_item | p9 L416 |  | standalone Finance cost paid (2 cells)
R542-R543 | line_item | p9 L417 |  | standalone Payment of lease liabilities (2 cells)
R544-R545 | line_item | p9 L418 |  | standalone Net cash flow used in financing activities (C) (2 cells)
R546-R547 | line_item | p9 L419 |  | standalone Net Increase/(decrease) in cash & cash equivalents (A + B + C) (2 cells)
R548-R549 | line_item | p9 L420 |  | standalone Cash & cash equivalents - Opening (2 cells)
R550-R551 | line_item | p9 L421 |  | standalone Cash & cash equivalents - Closing (2 cells)

Materiality notes: p9 L405 Investment in wholly owned subsidiary R521 = (4,113.13) H1 FY27 vs ZERO_STANDING R522 prior year; standalone-only, absent from consolidated, no subsidiary named (R624, R731). Buyback (1,498.00) H1 FY27 (R270, R539) vs nil prior year R271; standalone buyback row has one cell only (R539), second period cell absent in A1 fulltext L415. Standalone tax adjustments L300 nil in five periods, (2.26) FY26 (R363). Other equity rows (R121-R123, R394-R396) carry 3 cells only (blank quarter/half columns, per A1). Header date 31-09-2025 invalid (R652, R711). Consolidated and standalone same-named lines are separate IDs.

## 3 EMBEDDED NUMBERS (non-table, 42)

R552-R552 | line_item | p1 L29 |  | BSE scrip code (1 cells)
R553-R553 | line_item | p1 L46 |  | board meeting commencement time (1 cells)
R554-R554 | line_item | p1 L46 |  | board meeting conclusion time (1 cells)
R555-R555 | line_item | p1 L36 |  | board meeting serial number (1 cells)
R556-R556 | line_item | p1 L39 |  | SEBI LODR regulation cited (1 cells)
R557-R557 | line_item | p1 L40 |  | year of SEBI LODR Regulations (1 cells)
R558-R558 | line_item | p1 L55 |  | company secretary membership number (1 cells)
R559-R559 | line_item | p1 L20 |  | company telephone, page 1 (1 cells)
R560-R560 | line_item | p1 L19 |  | registered office pin code, page 1 (1 cells)
R561-R561 | line_item | p1 L19 |  | registered office plot, page 1 (1 cells)
R562-R562 | line_item | p1 L19 |  | registered office road number (1 cells)
R563-R563 | line_item | p2 L71 |  | SRE standard cited by auditor, consolidated review (1 cells)
R564-R564 | line_item | p2 L69 |  | Companies Act section cited, consolidated review (1 cells)
R565-R565 | line_item | p2 L68 |  | SEBI LODR regulation, consolidated review (1 cells)
R566-R566 | line_item | p2 L69 |  | Companies Act year, consolidated review (1 cells)
R567-R567 | line_item | p2 L86 |  | auditor partner membership number (1 cells)
R568-R568 | line_item | p2 L82 |  | auditor firm registration numbers (1 cells)
R569-R569 | line_item | p2 L87 |  | UDIN, consolidated review report (1 cells)
R570-R570 | line_item | p2 L90 |  | Lodha LLP conversion effective date (1 cells)
R571-R571 | line_item | p3 L124 |  | face value per share, consolidated P&L (1 cells)
R572-R572 | line_item | p3 L95 |  | registered office pin code, page 3 (1 cells)
R573-R573 | line_item | p6 L262 |  | SRE standard cited by auditor, standalone review (1 cells)
R574-R574 | line_item | p6 L260 |  | Companies Act section cited, standalone review (1 cells)
R575-R575 | line_item | p6 L258 |  | SEBI LODR regulation, standalone review (1 cells)
R576-R576 | line_item | p6 L272 |  | auditor partner membership number, standalone review (1 cells)
R577-R577 | line_item | p6 L273 |  | UDIN, standalone review report (1 cells)
R578-R578 | line_item | p7 L307 |  | face value per share, standalone P&L (1 cells)
R579-R579 | line_item | p10 L432 |  | equity shares allotted on ESOP exercise, quarter ended 30-Sep-2026 (1 cells)
R580-R580 | line_item | p10 L432 |  | face value per share, Note 3 allotment (1 cells)
R581-R581 | line_item | p10 L432 |  | equity share capital as stated in Note 3 (1 cells)
R582-R582 | line_item | p10 L432 |  | number of shares comprising capital as stated in Note 3 (1 cells)
R583-R583 | line_item | p10 L434 |  | labour laws consolidated by the four Labour Codes (1 cells)
R584-R584 | line_item | p10 L434 |  | Labour Codes notified (1 cells)
R585-R585 | line_item | p10 L431 |  | accounting standard for consolidation, Note 2 (1 cells)
R586-R586 | line_item | p10 L433 |  | accounting standard for segments, Note 4 (1 cells)
R587-R587 | line_item | p10 L440 |  | executive director DIN, page 10 (1 cells)
R588-R588 | line_item | p3 L132 |  | executive director DIN, page 3 (1 cells)
R589-R589 | line_item | p4 L193 |  | executive director DIN, page 4 (1 cells)
R590-R590 | line_item | p5 L246 |  | executive director DIN, page 5 (1 cells)
R591-R591 | line_item | p7 L315 |  | executive director DIN, page 7 (1 cells)
R592-R592 | line_item | p8 L374 |  | executive director DIN, page 8 (1 cells)
R593-R593 | line_item | p9 L425 |  | executive director DIN, page 9 (1 cells)

Note: R553-R554 meeting 07:20 PM to 08:30 PM = 70 minutes. R587-R593 repeat DIN 05350841 on seven pages (RESTATED).

## 4 AGENDA ITEMS (Board Outcome letter)

R694 | agenda_item 1 | p1 L37 | | Un-audited standalone and consolidated results with Limited Review Report (cross R695, R672-R673, R601, R602)
R553-R555 | meeting times/serial | p1 | | commenced 07:20 PM, concluded 08:30 PM, BM 03/2026-27
FLAG AGENDA_NOT_LISTED | letter says "inter-alia considered and approved" but names one item; no dividend, AR/AGM, appointment, ESOP or capital item. Absence, not an A1 miss.

## 5 AUDITOR REPORT PARAGRAPHS (limited review, Lodha & Co LLP; R607-R608, R612-R617)

R698 | auditor_para | | | Consol scope, moderate assurance
R699 | auditor_para | | | Consol review not audit
R700 | auditor_para | | | Consol perimeter: three wholly owned subs reviewed (R609-R611)
R701 | auditor_para | | | Consol conclusion unmodified
R716 | auditor_para | | | Standalone scope
R717 | auditor_para | | | Standalone review not audit
R718 | auditor_para | | | Standalone conclusion unmodified
Emphasis of Matter: none. Other Matter: none. Going Concern language: none. Opinion: unmodified limited review. UDINs R569 (consol), R577 (standalone). Unaudited/management-furnished entities: none stated. Report dates R677, R681.

## 6 ENTITIES (46; first run, no prior list, no ENTITY_CHANGE possible)

R594-R639 | entity | p1-p10 | | 46 rows incl. subs R609-R611 (auditor list), R625-R627 (Note 2). R626 step-down wording vs R611 direct wholly owned: ENTITY_WORDING_DIFF. R624 unnamed subsidiary in standalone cash flow: ENTITY_UNNAMED. R604 signature text garbled vs R603 name. Auditor R607/R620 and partner R608/R621 repeated (RESTATED).

## 7 FORWARD STATEMENTS (3)

R640-R642 | forward | p10 L434-435 | | Note 5 Labour Code restructure from 1-Apr-2026, rules in draft, accounting effect later; no quantified impact (cross R737, R738, R687)

## 8 DATES (51)

R643-R662 | dates | period headers | FOOTNOTE_UNRESOLVED | R652 prints invalid 31-09-2025
R663-R671 | dates | auditor digital signature timestamps 20:04:40 to 20:23:06 on 22-Oct-2026 | SIGNATURE_BEFORE_MEETING_CLOSE | meeting concluded 20:30 (R554); all nine precede it. R667 (20:04:40) earliest.
R675 | dates | CS signature 20:45:14, after close
R672-R674, R676-R693 | dates | cover/report/note dates and statute years; R678 and R682 Lodha LLP conversion 27-Dec-2023 (RESTATED)

## 9 SIGNATURE BLOCKS

R618, R636 | Ramasubramanian Sankaran (S. Ramasubramanian), Executive Director, DIN 05350841 | results p3, notes p10; DIN repeated R587-R593
R663-R671 | auditor R P Baradiya, nine digital stamps | SIGNATURE_BEFORE_MEETING_CLOSE
R675, R603, R604, R697 | CS Sarita Leelaramani, cover letter 20:45:14
No CMD/MD signatory; Executive Director signs results.

## 10 QUALIFIERS (46)

R694-R739 | qualifier | p1-p10 | | audit status, units, EPS not annualised, capex/ESOP/buyback definitions, Notes 1-6. R711 header-typo qualifier; R731 standalone-only subsidiary investment (pairs with R522 ZERO_STANDING). R705/R722 audit status RESTATED across consolidated and standalone.

## MISSING_FROM_STRUCTURED

none

```yaml
stage: A2-enumerator
company: "CYBERTECH"
quarter: "q2fy27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/cybertech-q2fy27/work/ledger_results_cybertech_q2fy27.md"
counts:
  notes: 7
  line_items: 191
  zero_standing: 45
  agenda_items: 1
  auditor_paras: 7
  entities: 46
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
  embedded_numbers: 42
  forward: 3
  dates: 51
  qualifiers: 46
flags_raised: [ZERO_STANDING, SIGNATURE_BEFORE_MEETING_CLOSE, AGENDA_NOT_LISTED, ENTITY_WORDING_DIFF, ENTITY_UNNAMED, RESTATED, FOOTNOTE_UNRESOLVED]
ids_in_structured: 739
ids_referenced: 739
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "45 dash cells across 27 line items. Largest: standalone Investment in a wholly owned subsidiary (4,113.13) H1 FY27 vs nil prior year (R521/R522), no subsidiary named and absent from consolidated; buyback (1,498.00) H1 FY27 vs nil (R270/R271, R539); standalone buyback row has a single cell. All nine auditor signature timestamps (20:04 to 20:23) precede the stated board close 20:30. Letter says inter-alia but lists one agenda item. Note 2 calls Canada a subsidiary of the USA entity; auditor list calls it wholly owned. Cash-flow prior-year header prints 31-09-2025. No prior ledger, so no ENTITY_CHANGE diff."
```
