# A2 ENUMERATION LEDGER: Tejas Networks (TEJASNET), Q2 FY27, Results filing
Source: A1 structured extraction (R001-R851). Prior ledger: Q1 FY27 (diffs in section 9). Claim text lives at the row ID in the structured file; not re-copied here.

ids_in_structured: 851 | ids_referenced_in_ledger: 864 (851 structured + 13 MISSING_FROM_STRUCTURED R852-R864) | orphan_ids: [] | match: yes

```
=== A2 COUNT TEST ===
category: notes             grep_count: 12   sweep_count: 12   match: yes   (+2 footnotes R842,R834 and 7 xref/marker rows; see section 1)
category: line_items        grep_count: 242  sweep_count: 242  match: yes   (238 structured + R852-R855; grep = distinct page+line, sweep = label-run groups)
category: zero_standing     grep_count: 40   sweep_count: 40   match: yes   (rows; 37 structured + R852, R853, R855)
category: agenda_items      grep_count: 1    sweep_count: 1    match: yes   (results only; board times R698-R699)
category: auditor_paras     grep_count: 19   sweep_count: 19   match: yes   (11 structured + R856-R863; R864 is an identifier block, counted separately; section 5 and 10)
category: entities          grep_count: 4    sweep_count: 4    match: yes   (holding + 3 subs; 29 ENTITY rows)
fulltext_vs_structured: fulltext sweep found 864 units vs 851 structured rows; 13 MISSING_FROM_STRUCTURED rows named: R852 R853 R854 R855 R856 R857 R858 R859 R860 R861 R862 R863 R864 (fulltext lines 159, 170, 338, 715, 488-494, 76-84, 86-91, 105-109, 423-435, 437-442, 444-455, 480, 463-475)
category: signature_blocks  grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Reconciliation: line_items counted by page+line key (238) and by consecutive label-run (238); balance-sheet rows merge their two date columns into one item. Notes grep on context tag 'standalone/consolidated note N' returned R816-R820, R838-R841, R843-R845 = 12; manual sweep adds unnumbered footnotes R842, R834 and xref markers. Zero grep on the flag token and the sweep of dash cells agree. Entities: 29 raw ENTITY rows, 4 unique consolidation entities. No FORWARD rows exist in the structured file (A1 states none).

## 1. Notes, footnotes and cross-references
ROW_ID | category | flags | cross-ref / materiality
---|---|---|---
R816 | numbered note |  | standalone note 1 basis of preparation
R817 | numbered note |  | standalone note 2 segment
R818 | numbered note |  | standalone note 3 Q2 FY26 Rs 145.43cr CoM charge; xref R706,R787; restated as cons note 5 R843,R729,R799
R819 | numbered note |  | standalone note 4 warranty provision; xref R707-R709,R788; restated cons note 6 R844,R730-R732,R800
R820 | numbered note |  | standalone note 5 audit committee/board approval; xref R789,R758; restated cons note 7 R845,R767,R801
R838 | numbered note |  | consolidated note 1 group entities; xref R764-R766
R839 | numbered note |  | consolidated note 2 basis of preparation
R840 | numbered note |  | consolidated note 3 segment
R841 | numbered note |  | consolidated note 4 standalone summary table; table R677-R694
R843 | numbered note | RESTATED | consolidated note 5 Rs 145.43cr charge, restated of std note 3
R844 | numbered note | RESTATED | consolidated note 6 warranty, restated of std note 4
R845 | numbered note | RESTATED | consolidated note 7 approval, restated of std note 5
R842 | footnote |  | unnumbered Note under cons note 4 table (standalone results availability)
R834 | footnote |  | asterisk footnote "amount below rounding norm", for R833 Investments*; 0.00 values
R833 | footnote |  | asterisk marker on cons non-current Investments
R810 | xref |  | cross-reference "Refer note-3" on std P&L CoM line (R031-R036)
R811 | xref |  | cross-reference "Refer note-4" std other expenses
R830 | xref | FOOTNOTE_UNRESOLVED | cross-reference "Refer note-5" cons CoM line (but cons note 3 = segment; xref numbering to be reconciled by A3)
R831 | xref |  | cross-reference "Refer note-6" cons other expenses
R812 | footnote |  | reserves definition footnote std P&L
R832 | footnote |  | reserves definition footnote cons P&L

## 2. Line items (every financial table row, incl. nil)

### 2.1 standalone P&L (26 line items)

ROW_IDS | page/line | line item | A2 flags | note
---|---|---|---|---
R001-R006 | p3 l142 | (a) Revenue from sale of goods and rendering of service |  | 
R007-R012 | p3 l143 | (6) Other operating revenue | ZERO_STANDING(R007) | 
R013-R018 | p3 l144 | Total Revenue from operations |  | 
R019-R024 | p3 l145 | I Other income |  | 
R025-R030 | p3 l146 | ML Total income (1 +11) |  | 
R031-R036 | p3 l148 | (0) Cost of materials consumed (Refer note- 3) |  | 
R037-R042 | p3 l149 | (b) Purchases of stock-in-trade |  | 
R043-R048 | p3 l150 | (c) Changes in inventories of stock-in-trade and finish |  | 
R049-R054 | p3 l151 | {d) Employee benefit expense |  | 
R055-R060 | p3 l152 | (e) Finance costs |  | 
R061-R066 | p3 l153 | ff) Depreciation and amortization expense |  | 
R067-R072 | p3 l154 | (g) Allowance for expected credit loss |  | 
R073-R078 | p3 l155 | {h) Other expenses (Refer note- 4) |  | 
R079-R084 | p3 l156 | Total expenses (IV) |  | 
R085-R090 | p3 l157 | V__Profit/{Loss) before tax (Ill - IV) |  | 
R091-R096 | p3 l160 | (2) Deferred tax expense/{benefit) |  | 
R097-R102 | p3 l161 | Total tax expense/(benefit) |  | 
R103-R108 | p3 l162 | Vil Profit/(Loss) after tax (V- VI) |  | 
R109 | p3 l165 | Remeasurements of the post-employment benefit obligatio | COLS_PARTIAL(R109) | 
R110-R113 | p3 l167 | Income tax relating to above ° Ps | ZERO_STANDING(R110-R113) COLS_PARTIAL(R110-R113) | 
R114-R119 | p3 l169 | Gains/(losses) in cash flow hedges |  | 
R120-R125 | p3 l171 | 1X Total comprehensive income for the period (VIl + VII |  | 
R126-R131 | p3 l172 | X — Equity share capital (Face value of Rs. 10/- each} |  | 
R132-R134 | p3 l174 | z ‘ | ZERO_STANDING(R132-R133) COLS_PARTIAL(R132-R134) | 
R135-R140 | p3 l178 | (1) Basic |  | 
R141-R146 | p3 l179 | (2) Diluted |  | 

### 2.2 standalone balance sheet (38 line items)

ROW_IDS | page/line | line item | A2 flags | note
---|---|---|---|---
R147-R148 | p4 l211 | Property, plant and equipment |  | 
R149-R150 | p4 l212 | Right-of-use assets |  | 
R151-R152 | p4 l213 | Goodwill |  | 
R153-R154 | p4 l214 | Other intangible assets |  | 
R155-R156 | p4 l215 | Intangible assets under development |  | 
R157-R158 | p4 l217 | (i) Investments |  | 
R159-R160 | p4 l218 | (ii) Trade receivables |  | 
R161-R162 | p4 l219 | (iil) Other financial assets |  | 
R163-R164 | p4 l220 | Current tax assets (net) |  | 
R165-R166 | p4 l221 | Deferred tax assets (net) |  | 
R167-R168 | p4 l222 | Other non-current assets |  | 
R169-R170 | p4 l223 | Total non-current assets |  | 
R171-R172 | p4 l225 | Inventories |  | 
R173-R174 | p4 l227 | (i) Investments |  | 
R175-R176 | p4 l228 | (ii) Trade receivables |  | 
R177-R178 | p4 l229 | (iii) Cash and cash equivalents |  | 
R179-R180 | p4 l230 | (iv) Bank balances other than (iii) above |  | 
R181-R182 | p4 l231 | (v) Other financial assets |  | 
R183-R184 | p4 l232 | Other current assets |  | 
R185-R186 | p4 l233 | Total current assets |  | 
R187-R188 | p4 l234 | Total assets | OCR_MISREAD_PAIR(R187/R221) | 
R189-R190 | p4 l237 | Equity share capital |  | 
R191-R192 | p4 l238 | Other equity |  | 
R193-R194 | p4 l239 | Total equity |  | 
R195-R196 | p4 l243 | (i) Borrowings |  | 
R197-R198 | p4 l244 | (ii) Lease liabilities |  | 
R199-R200 | p4 l245 | Provisions |  | 
R201-R202 | p4 l246 | Total non-current liabilities |  | 
R203-R204 | p4 l249 | () Borrowings . |  | 
R205-R206 | p4 l250 | (ii) Lease liabilities |  | 
R207-R208 | p4 l252 | {a) Total outstanding dues of micro enterprises and sma |  | 
R209-R210 | p4 l253 | (b) Total outstanding dues of creditors other than micr |  | 
R211-R212 | p4 l254 | {iv} Other financial liabilities |  | 
R213-R214 | p4 l255 | Provisions |  | 
R215-R216 | p4 l256 | Other current liabilities |  | 
R217-R218 | p4 l257 | Total current liabilities |  | 
R219-R220 | p4 l258 | Total liabilities |  | 
R221-R222 | p4 l259 | Total equity and liabilities | OCR_MISREAD_PAIR(R187/R221) | 

### 2.3 standalone cash flow (52 line items)

ROW_IDS | page/line | line item | A2 flags | note
---|---|---|---|---
R223-R224 | p5 l288 | Profit/(Loss) before tax |  | 
R225-R226 | p5 l290 | Depreciation and amortization expense |  | 
R227-R228 | p5 l291 | Allowance for expected credit loss |  | 
R229-R230 | p5 l292 | Interest income |  | 
R231-R232 | p5 l293 | Unwinding of discount on fair valuation of financials a |  | 
R233-R234 | p5 l294 | Gain/(loss) on current investments carried at FYTPL |  | 
R235-R236 | p5 l295 | Gain on sale of current investments carried at FVTPL |  | 
R237-R238 | p5 l296 | Finance costs |  | 
R239-R240 | p5 l297 | Unrealized (gain)/ loss on exchange difference on cash  |  | 
R241-R242 | p5 l298 | Unrealised (gain}/ loss on exchange differance (net) |  | 
R243-R244 | p5 l299 | Profit/{Loss) on disposal of property, plant and equipm | ZERO_STANDING(R243) | 
R245-R246 | p5 l300 | Expense recognized in respect of equity-settled share-b |  | 
R247-R248 | p5 l301 | (label on prior line) |  | 
R249-R250 | p5 l303 | (Increase)/decrease in inventories |  | 
R251-R252 | p5 l304 | {Increase)/decrease in trade receivables |  | 
R253-R254 | p5 l305 | {Increase]/decrease in other financial assets |  | 
R255-R256 | p5 l306 | (Increase)/decrease in other assets |  | 
R257-R258 | p5 l307 | Increase/(decrease) in trade and other payables |  | 
R259-R260 | p5 l308 | Increase/{decrease) in provisions |  | 
R261-R262 | p5 l309 | Increase/{decrease) in other financial liabilities |  | 
R263-R264 | p5 l310 | Increase/{decrease) in other liabilities |  | 
R265-R266 | p5 l311 | Cash used in operations |  | 
R267-R268 | p5 l312 | Income taxes paid |  | 
R269-R270 | p5 l313 | Net cash used in operating activities (A) |  | 
R271-R272 | p5 l315 | Payment for purchase of property, plant and equipment |  | 
R273-R274 | p5 l316 | Payment for intangible assets (including under developm |  | 
R275-R276 | p5 l317 | Proceeds from disposal of property, plant and equipment | ZERO_STANDING(R275) | 
R277-R278 | p5 l318 | Investments in deposits with banks |  | 
R279-R280 | p5 l319 | Withdrawals of deposits from banks | ZERO_STANDING(R279) | 
R281-R282 | p5 l320 | Payments for purchase of investments in liquid mutual f |  | 
R283-R284 | p5 l321 | Proceeds from redemption of investments in liquid mutua |  | 
R285-R286 | p5 l322 | Interest received |  | 
R287-R288 | p5 l323 | Net cash used in investing activities (B) |  | 
R289-R290 | p5 l325 | Proceeds from exercise of restricted stock units/employ |  | 
R291-R292 | p5 l326 | Dividend paid | ZERO_STANDING(R291) | 
R293-R294 | p5 l327 | Proceeds from borrowings - non- current |  | 
R295-R296 | p5 l328 | Repayment of borrowings -non- current | ZERO_STANDING(R296) | 
R297-R298 | p5 l329 | Proceeds from borrowings - current (excluding supplier  |  | 
R299-R300 | p5 l330 | Repayment of borrowings - current (excluding supplier f |  | 
R301-R302 | p5 l331 | Proceeds received under supplier finance arrangement |  | 
R303-R304 | p5 l332 | Repayments under supplier finance arrangement |  | 
R305-R306 | p5 l333 | Principal payment on lease liabilities |  | 
R307-R308 | p5 l334 | Interest payment on lease liabilities |  | 
R309-R310 | p5 l335 | Interest on non-current borrowings |  | 
R311-R312 | p5 l336 | Interest on current borrowings (excluding supplier fina |  | 
R313-R314 | p5 l337 | Interest under supplier finance arrangement |  | 
R315-R316 | p5 l339 | Net cash generated from financing activities (C) |  | 
R317-R318 | p5 l340 | Net increase/(decrease) in cash and cash equivalents (A |  | 
R319-R320 | p5 l341 | Cash and cash equivalents at the beginning of the perio |  | 
R321-R322 | p5 l342 | Effects of exchange rate changes on the balance of cash |  | 
R323-R324 | p5 l343 | Cash and cash equivalents at the end of the period |  | 
R325-R326 | p5 l345 | Acquisition of right-of-use assets | ZERO_STANDING(R325) | 

### 2.4 consolidated P&L (29 line items)

ROW_IDS | page/line | line item | A2 flags | note
---|---|---|---|---
R327-R332 | p9 l533 | (a) Revenue from sale of goods and rendering of service | OCR_MISREAD_PAIR(R327/R339) | 
R333-R338 | p9 l534 | (b) Other operating revenue | ZERO_STANDING(R333) | 
R339-R344 | p9 l535 | Total Revenue from operations | OCR_MISREAD_PAIR(R327/R339) | 
R345-R350 | p9 l536 | I Other income |  | 
R351-R356 | p9 l537 | I Total income (i+ II) |  | 
R357-R362 | p9 l539 | (a) Cost of materials consumed (Refer note- 5} |  | 
R363-R368 | p9 l540 | {b) Purchases of stock-in-trade |  | 
R369-R374 | p9 l541 | (c) Changes in inventories of stock-in-trade and finish |  | 
R375-R380 | p9 l542 | (d) Employee benefit expense |  | 
R381-R386 | p9 l543 | (e) Finance costs |  | 
R387-R392 | p9 l544 | (f) Depreciation and amortization expense |  | 
R393-R398 | p9 l545 | (g) Allowance for expected credit loss |  | 
R399-R404 | p9 l546 | (h) Other expenses (Refer note- 6) |  | 
R405-R410 | p9 l547 | Total expenses (IV) |  | 
R411-R416 | p9 l548 | V_ Profit/{Loss) before tax {Ill - IV} |  | 
R417-R422 | p9 l550 | {1) Current tax expense/(benefit) | ZERO_STANDING(R417-R420) | 
R423-R428 | p9 l551 | (2) Deferred tax expense/(benefit} | OCR_MISREAD_PAIR(R428/R434) | 
R429-R434 | p9 l552 | Total tax expense/{benefit) | OCR_MISREAD_PAIR(R428/R434) | 
R435-R440 | p9 l553 | VII Profit/(Loss) after tax (V- Vi) |  | 
R441-R445 | p9 l556 | en the post-employment benefit obligation nee | COLS_PARTIAL(R441-R445) | 
R446-R449 | p9 l557 | Income tax relating to above 2 * | ZERO_STANDING(R446-R449) COLS_PARTIAL(R446-R449) | 
R450-R455 | p9 l559 | Gains/(losses) in cash flow hedges |  | 
R456-R461 | p9 l560 | Exchange differences on translation of foreign operatio |  | 
R462-R467 | p9 l561 | Income tax relating to above | ZERO_STANDING(R462-R467) | 
R468-R473 | p9 l562 | 1X Total comprehensive income for the period (Vil + VII |  | 
R474-R479 | p9 l563 | X Equity share capital (Face value of Rs. 10/- each) |  | 
R480-R485 | p9 l565 | (label on prior line) | ZERO_STANDING(R480-R484) | 
R486-R491 | p9 l569 | (1) Basic |  | 
R492-R497 | p9 l570 | (2) Diluted |  | 

### 2.5 consolidated balance sheet (38 line items)

ROW_IDS | page/line | line item | A2 flags | note
---|---|---|---|---
R498-R499 | p10 l597 | Property, plant and equipment |  | 
R500-R501 | p10 l598 | Right-of-use assets |  | 
R502-R503 | p10 l599 | Goodwill |  | 
R504-R505 | p10 l600 | ther Intangible assets |  | 
R506-R507 | p10 l601 | Intangible assets under development |  | 
R508-R509 | p10 l603 | (i) Investments* |  | 
R510-R511 | p10 l604 | (ii) Trade receivables |  | 
R512-R513 | p10 l605 | (iii) Other financial assets |  | 
R514-R515 | p10 l606 | Current tax assets (net) |  | 
R516-R517 | p10 l607 | Deferred tax assets (net) |  | 
R518-R519 | p10 l608 | Other non-current assets |  | 
R520-R521 | p10 l609 | Total non-current assets |  | 
R522-R523 | p10 l611 | Inventories |  | 
R524-R525 | p10 l613 | (i) Investments |  | 
R526-R527 | p10 l614 | (ii) Trade receivables |  | 
R528-R529 | p10 l615 | (iii) Cash and cash equivalents |  | 
R530-R531 | p10 l616 | (iv) Bank balances other than (iii) above |  | 
R532-R533 | p10 l617 | (v) Other financial assets |  | 
R534-R535 | p10 l618 | Other current assets |  | 
R536-R537 | p10 l619 | Total current assets |  | 
R538-R539 | p10 l620 | Total assets |  | 
R540-R541 | p10 l623 | Equity share capital |  | 
R542-R543 | p10 l624 | Other equity |  | 
R544-R545 | p10 l625 | Total equity |  | 
R546-R547 | p10 l629 | (i) Borrowings |  | 
R548-R549 | p10 l630 | (ii) Lease liabilities |  | 
R550-R551 | p10 l631 | Provisions |  | 
R552-R553 | p10 l632 | Total non-current liabilities |  | 
R554-R555 | p10 l635 | (i) Borrowings |  | 
R556-R557 | p10 l636 | (ii) Lease liabilities |  | 
R558-R559 | p10 l638 | (a) Total outstanding dues of micro enterprises and sma |  | 
R560-R561 | p10 l639 | (b) Total outstanding dues of creditors other than micr |  | 
R562-R563 | p10 l640 | (iv) Other financial liabilities |  | 
R564-R565 | p10 l641 | Provisions |  | 
R566-R567 | p10 l642 | Other current liabilities |  | 
R568-R569 | p10 l643 | Total current liabilities |  | 
R570-R571 | p10 l644 | Total llabilities |  | 
R572-R573 | p10 l645 | Total equity and liabilities |  | 

### 2.6 consolidated cash flow (52 line items)

ROW_IDS | page/line | line item | A2 flags | note
---|---|---|---|---
R574-R575 | p11 l675 | Profit/(Loss) before tax |  | 
R576-R577 | p11 l677 | Depreciation and amortization expense |  | 
R578-R579 | p11 l678 | Allowance for expected credit loss |  | 
R580-R581 | p11 l679 | Interest income |  | 
R582-R583 | p11 l680 | Unwinding of discount on fair valuation of financials a |  | 
R584-R585 | p11 l681 | Gain/{loss) on current investments carried at FVTPL |  | 
R586-R587 | p11 l682 | Gain on sale of current investments carried at FVTPL |  | 
R588-R589 | p11 l683 | Finance costs |  | 
R590-R591 | p11 l684 | Unrealised (gain)/ loss on exchange difference on cash  |  | 
R592-R593 | p11 l685 | Unrealised (gain)/ loss on exchange difference (net) |  | 
R594 | p11 l686 | Profit/(Loss) on disposal of property, plant and equipm | COLS_PARTIAL(R594) | 
R595-R596 | p11 l687 | Expense recognized in respect of equity-settled share-b |  | 
R597-R598 | p11 l688 | (label on prior line) |  | 
R599-R600 | p11 l690 | {increase}/decrease in inventories |  | 
R601-R602 | p11 l691 | (Increase}/decrease in trade receivables |  | 
R603-R604 | p11 l692 | (Increase)/decrease in other financial assets |  | 
R605-R606 | p11 l693 | (Increase)/decrease in other assets |  | 
R607-R608 | p11 l694 | Increase/(decrease) in trade and other payables |  | 
R609-R610 | p11 l695 | Increase/(decrease) in provisions |  | 
R611-R612 | p11 l696 | Increase/(decrease) in other financial liabilities |  | 
R613-R614 | p11 l697 | Increase/(decrease) in other liabilities |  | 
R615-R616 | p11 l698 | Cash used in operations |  | 
R617-R618 | p11 l699 | Income taxes paid |  | 
R619-R620 | p11 l700 | Net cash used in operating activities (A) |  | 
R621-R622 | p11 l702 | Payment for purchase of property, plant and equipment |  | 
R623-R624 | p11 l703 | Payment for intangible assets (including under developm |  | 
R625-R626 | p11 l704 | Proceeds from disposal of property, plant and equipment | ZERO_STANDING(R625) | 
R627-R628 | p11 l705 | Investments in deposits with banks |  | 
R629-R630 | p11 l706 | Withdrawals of deposits from banks | ZERO_STANDING(R629) | 
R631-R632 | p11 l707 | Payments for purchase of investments in liquid mutual f |  | 
R633-R634 | p11 l708 | Proceeds from redemption of investments in liquid mutua |  | 
R635-R636 | p11 l709 | Interest received |  | 
R637-R638 | p11 l710 | Net cash used in investing activities (B) |  | 
R639-R640 | p11 l712 | Proceeds from exercise of restricted stock units/employ |  | 
R641-R642 | p11 l713 | Dividend paid | ZERO_STANDING(R641) | 
R643-R644 | p11 l714 | Proceeds from borrowings - non- current |  | 
R645-R646 | p11 l716 | Proceeds from borrowings - current (excluding supplier  |  | 
R647-R648 | p11 l717 | Repayment of borrowings - current (excluding supplier f |  | 
R649-R650 | p11 l718 | Proceeds received under supplier finance arrangement |  | 
R651-R652 | p11 l719 | Repayments under supplier finance arrangement |  | 
R653-R654 | p11 l720 | Principal payment of lease liabilities |  | 
R655-R656 | p11 l721 | Interest payment of lease liabilities |  | 
R657-R658 | p11 l722 | Interest on non-current borrowings |  | 
R659-R660 | p11 l723 | Interest on current borrowings (excluding supplier fina |  | 
R661-R662 | p11 l724 | Interest under supplier finance arrangement |  | 
R663-R664 | p11 l725 | Other finance cost |  | 
R665-R666 | p11 l726 | Net cash generated from financing activities (C} |  | 
R667-R668 | p11 l727 | Net increase/(decrease) in cash and cash equivalents (A |  | 
R669-R670 | p11 l728 | Cash and cash equivalents at the beginning of the perio |  | 
R671-R672 | p11 l729 | Effects of exchange rate changes on the balance of cash |  | 
R673-R674 | p11 l730 | Cash and cash equivalents at the end of the period |  | 
R675-R676 | p11 l732 | Acquisition of right-of-use assets | ZERO_STANDING(R675) | 

### 2.7 standalone summary in consolidated note 4 (3 line items)

ROW_IDS | page/line | line item | A2 flags | note
---|---|---|---|---
R677-R682 | p12 l790 | Revenue from operations |  | 
R683-R688 | p12 l792 | Profit/(Loss} before tax |  | 
R689-R694 | p12 l794 | Profit/{Loss) after tax |  | 

## 3. ZERO_STANDING rows (dash/nil standing items)
ROW_IDS | line item | flags | note
---|---|---|---
R007 | p3 l143 (6) Other operating revenue | ZERO_STANDING | template signal
R110-R113 | p3 l167 Income tax relating to above ° Ps | ZERO_STANDING | template signal
R132-R133 | p3 l174 z ‘ | ZERO_STANDING | template signal
R243 | p5 l299 Profit/{Loss) on disposal of property, plant and equipm | ZERO_STANDING | template signal
R275 | p5 l317 Proceeds from disposal of property, plant and equipment | ZERO_STANDING | template signal
R279 | p5 l319 Withdrawals of deposits from banks | ZERO_STANDING | template signal
R291 | p5 l326 Dividend paid | ZERO_STANDING | template signal
R296 | p5 l328 Repayment of borrowings -non- current | ZERO_STANDING | template signal
R325 | p5 l345 Acquisition of right-of-use assets | ZERO_STANDING | template signal
R333 | p9 l534 (b) Other operating revenue | ZERO_STANDING | template signal
R417-R420 | p9 l550 {1) Current tax expense/(benefit) | ZERO_STANDING | template signal
R446-R449 | p9 l557 Income tax relating to above 2 * | ZERO_STANDING | template signal
R462-R467 | p9 l561 Income tax relating to above | ZERO_STANDING | template signal
R480-R484 | p9 l565 (label on prior line) | ZERO_STANDING | template signal
R625 | p11 l704 Proceeds from disposal of property, plant and equipment | ZERO_STANDING | template signal
R629 | p11 l706 Withdrawals of deposits from banks | ZERO_STANDING | template signal
R641 | p11 l713 Dividend paid | ZERO_STANDING | template signal
R675 | p11 l732 Acquisition of right-of-use assets | ZERO_STANDING | template signal
Material: Other operating revenue Q2 FY27 dash (R007, R333); consolidated income tax on OCI all periods dash (R462-R467); dividend paid dash (R291, R641).

## 4. Agenda items and board meeting
ROW_ID | category | flags | note
---|---|---|---
R776 | agenda item 1: approval of Q2 FY27 results (sole agenda item) | | no AGM, dividend, director, auditor, ESOP or capital item
R698,R699 | board meeting start 2.00 PM / end 4:15 PM IST | | 2h15m vs 3h10m in Q1 FY27; informational
R775,R777 | letter date, results period | | 
R778 | signature timestamp 17:48:05 | | after R699 end 16:15: no early-signature flag

## 5. Auditor report paragraphs and identifiers
ROW_ID | category | flags | note
---|---|---|---
R804 | auditor para |  | std: assurance level
R805 | auditor para |  | std: scope limitation, no audit opinion
R822 | auditor para |  | std: para 3 no audit opinion
R823 | auditor para |  | std: unmodified conclusion
R824 | auditor para |  | cons: group definition
R825 | auditor para |  | cons: SEBI additional procedures
R826 | auditor para | UNREVIEWED_SUBS | cons: 3 subsidiaries not reviewed by their auditors (Other Matter)
R827 | auditor para | UNREVIEWED_SUBS | cons: management representation not material
R828 | auditor para | UNREVIEWED_SUBS | cons: conclusion not modified for above matter
R850 | auditor para |  | cons: assurance level
R851 | auditor para |  | cons: scope limitation
R702,R701,R703 | std UDIN, membership, firm reg | | 
R721,R722,R723 | cons UDIN, membership, firm reg | | 
R711-R720,R792,R793 | unreviewed subsidiaries totals and counts | UNREVIEWED_SUBS | not reviewed by their auditors. No Going Concern or Emphasis of Matter row exists in structured file

## 6. Consolidation entities
ROW_ID | entity | flags | note
---|---|---|---
R760 | Tejas Networks Limited (holding) | | same as Q1
R761,R764 | Tejas Communication Pte. Limited, Singapore | | unchanged vs Q1 list; spelling variant between sections
R762,R765 | Tejas Communications (Nigeria) Limited | | unchanged
R763,R766 | Saankhya Labs Inc(.), USA | | unchanged; punctuation variant. No ENTITY_CHANGE
Other ENTITY rows (non-consolidation): R746-R759,R767-R774

## 7. Signature blocks
ROW_ID | signatory | flags | note
---|---|---|---
R749,R778 | Company Secretary (Anantha Murthy N), digital 2026.10.16 17:48:05 | | 
R751,R701,R702 | PW partner, standalone report | | 
R773,R722,R721 | PW partner, consolidated report | | 
R759,R710,R790 | MD and CEO Arnob Roy, standalone notes | | 
R768,R733,R801 | MD and CEO Arnob Roy, consolidated notes | | 

## 8. Dates, other numbers and qualifiers (remaining IDs)
DATE rows: R775-R801 | period labels; review/approval date 16-Oct-2026
Misc NUMBER rows (codes, pincodes, subsidiary totals, standards, warranty/charge values): R695-R745
Other QUALIFIER rows (stamps, unit labels, status): R802-R809,R813-R815,R821-R829,R835-R837,R846-R851

## 9. Flags and diffs vs Q1 FY27 ledger
- OCR_MISREAD_PAIR: R187/R221 (std total assets 8,440.67 vs equity+liabilities 3,440.67, p4); R327/R339 (cons Q2 revenue 405.68 vs total 205.68, p9); R428/R434 (cons FY26 tax (445.10) vs (945.12), p9). Values not corrected.
- COLS_PARTIAL rows: R109-R113,R132-R134,R441-R449,R594 (OCR columns unassignable).
- Notes: Q1 FY27 had 6 std + 7 cons numbered notes; Q2 has 5 + 7. Q1 inventory-obsolescence reversal note (Rs 3.10 cr) and balancing-figure note are absent in Q2; Q2 carries the Q2 FY26 Rs 145.43 cr CoM charge note (R818/R843). Silence signal for A3, not interpreted.
- Warranty provision Rs 7.24 cr Q2 vs 35.11 Q1 vs 44.44 Q2 FY26 (R707-R709, R730-R732).
- No FORWARD rows, no Going Concern, no EoM. Board meeting 2h15m (Q1 3h10m). No ENTITY_CHANGE.

## 10. MISSING_FROM_STRUCTURED (correction loop 1; found in A1 fulltext, no structured row; fulltext line cited)
ROW | fulltext line | category | A2 flags | unit
---|---|---|---|---
R852 | 159 | line item (std P&L p3) | MISSING_FROM_STRUCTURED, ZERO_STANDING | "(1) Current tax expense/(benefit)" standalone: all period cells dash/OCR noise (label row)
R853 | 170 | line item (std P&L p3) | MISSING_FROM_STRUCTURED, ZERO_STANDING | "Income tax relating to above" under cash flow hedges, standalone: all cells dash
R854 | 338 | line item (std cash flow p5) | MISSING_FROM_STRUCTURED, COLS_PARTIAL | "Other finance cost" (OCR "Ather finance cast"), values read "10.99) {NR": two columns, OCR-garbled, not corrected
R855 | 715 | line item (cons cash flow p11) | MISSING_FROM_STRUCTURED, ZERO_STANDING (comparative dash) | "Repayment of borrowings - non- current" (161.22) H1 FY27, comparative dash. MATERIAL: cash repayment of term debt
R856 | 488-494 | auditor para (cons p8) | MISSING_FROM_STRUCTURED | Cons review para 5: unmodified conclusion, no material misstatement
Further units found by fulltext count test (same flag, no structured row):
R857 | 76-84 | auditor para (std p2) | MISSING_FROM_STRUCTURED | std review para 1: scope of statements reviewed
R858 | 86-91 | auditor para (std p2) | MISSING_FROM_STRUCTURED | std para 2: management responsibility
R859 | 105-109 | auditor para (std p2) | MISSING_FROM_STRUCTURED | std para 4: conclusion text (R823 abbreviates it)
R860 | 423-435 | auditor para (cons p7) | MISSING_FROM_STRUCTURED | cons para 1: scope
R861 | 437-442 | auditor para (cons p7) | MISSING_FROM_STRUCTURED | cons para 2: management responsibility
R862 | 444-455 | auditor para (cons p7) | MISSING_FROM_STRUCTURED | cons para 3: review standard SRE 2410 (R850/R851 abbreviate)
R863 | 480 | auditor para (cons p8) | MISSING_FROM_STRUCTURED | cons para 4 intro: entity list lead-in (entities at R760-R763)
R864 | 463-475 | identifier block (p7) | MISSING_FROM_STRUCTURED | PW address, head office, LLP conversion 25-Jul-2014 text (R782, R727-R728 partial)
Not enumerated (boilerplate, no content): page markers, CIN/telephone/registered-office repeats, column header lines (138-139, 284-285, 529-530, 671-672, 784-786), stamp/signature OCR noise. Auditor paras restated: 19 auditor-paragraph rows (11 structured + R856-R863) plus 1 identifier block (R864); R864 is not an auditor paragraph.
Updated tally: line_items 238 + 4 = 242; zero_standing rows 37 + 3 = 40; missing_from_structured 13. Gate A2: pass (structured orphan_ids empty; all fulltext units now ledgered).
