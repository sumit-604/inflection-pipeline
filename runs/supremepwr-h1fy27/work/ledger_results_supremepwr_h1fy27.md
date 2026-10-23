# A2 COMPLETENESS LEDGER: SUPREMEPWR results H1 FY27

Source: runs/supremepwr-h1fy27/extracted/supremepwr-results-h1fy27-structured.md (R001-R609). Rows reference A1 IDs only; verbatim values stay in the structured file. No prior ledger (first quarterly run), so ENTITY_CHANGE and DROPPED_SLIDE are not testable.

ids_in_structured: 609 | ids_referenced_in_ledger: 609 | orphan_ids: [] | match: yes

```
=== A2 COUNT TEST ===
category: notes         grep_count: 24   sweep_count: 24   match: yes   (17 numbered + 4 cash flow notes + 2 balance sheet footnotes + 1 certificate note)
category: line_items    grep_count: 168  sweep_count: 168  match: yes   (SA P&L 25, SA BS 23, SA CF 40, CON P&L 27, CON BS 23, CON CF 30)
category: zero_standing grep_count: 44   sweep_count: 44   match: yes   (44 dash NUMBER rows across 23 line items; plus 1 Nil remark R605)
category: agenda_items  grep_count: 2    sweep_count: 2    match: yes
category: auditor_paras grep_count: 9    sweep_count: 9    match: yes   (SA LRR 4 + CON LRR 5; certificate rows ledgered under annexure)
category: entities      grep_count: 28   sweep_count: 28   match: yes
category: dates         grep_count: 33   sweep_count: 33   match: yes
category: forward       grep_count: 9    sweep_count: 9    match: yes
category: signatures    grep_count: 3    sweep_count: 3    match: yes
category: id_accountability  structured 609  ledger 609  orphans 0  match: yes
turns / questions / mgmt_numbers / slides / slide_numbers: not applicable (results filing)
gate_a2: pass
=== END COUNT TEST ===
```

## 1. NOTES (24)
ROW ID | category | A2 flags | cross-ref / note
---|---|---|---
R566 | note: standalone note 1 (p6 l428) |  | ties R535
R567 | note: standalone note 2 (p6 l433) |  | ties R532
R568 | note: standalone note 3 (p6 l435) | RESTATED | RESTATED with R156-R163, R472-R478, R608-R609 (warrant terms)
R569 | note: standalone note 4 (p6 l445) | RESTATED | RESTATED as R594 (payables/loans/liabilities subject to confirmation); R514 forward
R570 | note: standalone note 5 (p6 l447) | RESTATED | single segment; RESTATED R596
R571 | note: standalone note 6 (p6 l449) | RESTATED | EPS caveat; RESTATED R595
R572 | note: standalone note 7 (p6 l452) |  | 
R573 | note: standalone note 8 (p6 l453) |  | no exceptional items; ties zero rows R058-R061
R590 | note: consolidated note 1 (p12 l995) |  | ties R543
R591 | note: consolidated note 2 (p12 l1004) |  | ties R541
R592 | note: consolidated note 3 (p12 l1007) |  | ties R402-R404, R501-R503
R593 | note: consolidated note 4 (p12 l1019) | FOOTNOTE_UNRESOLVED | FOOTNOTE_UNRESOLVED: bracketed alternatives left in filed text; consolidated LRR relies on this subsidiary result (R581)
R594 | note: consolidated note 5 (p12 l1023) | RESTATED | RESTATED of R569; R515 forward
R595 | note: consolidated note 6 (p12 l1026) | RESTATED | RESTATED of R571
R596 | note: consolidated note 7 (p12 l1030) | RESTATED | RESTATED of R570
R597 | note: consolidated note 8 (p12 l1033) |  | 
R598 | note: consolidated note 9 (p12 l1035) |  | ties zero rows R297-R300
R577 | note: standalone cash flow note (i) (p7 l585) |  | 
R578 | note: standalone cash flow note (ii) (p7 l586) |  | 
R601 | note: consolidated cash flow note (i) (p13 l1169) |  | 
R602 | note: consolidated cash flow note (ii) (p13 l1170) |  | 
R564 | note: balance sheet footnote (standalone) (p5 l362) |  | 
R588 | note: balance sheet footnote (consolidated) (p11 l915) |  | 
R607 | note: certificate note 1 (heading) (p15 l1233) |  | content R608-R609
R565 | note heading, standalone notes 1-8 | | grouped with notes
R589 | note heading, consolidated notes 1-9 | | grouped with notes
R608-R609 | certificate note 1 content | RESTATED | grouped under R607; ties R156-R163
Note: standalone has 8 numbered notes, consolidated has 9 (extra note is the subsidiary-results note, R593). Consolidated note 3 (AS 21 basis) has no standalone equivalent.

## 2. LINE ITEMS (168), every financial-table line, ZERO_STANDING kept
Table | ROW IDs | page | line | cols | line item label (A1) | A2 flags
---|---|---|---|---|---|---
standalone P&L | R010-R013 | 4 | 204 | 4 | I Revenue From Operations | 
standalone P&L | R014-R017 | 4 | 205 | 4 | II Other Income | 
standalone P&L | R018-R021 | 4 | 206 | 4 | III Total Income (I+II) | 
standalone P&L | R022-R025 | 4 | 208 | 4 | Purchases of Stock in Trade | 
standalone P&L | R026-R029 | 4 | 209 | 4 | Changes in Inventories | 
standalone P&L | R030-R033 | 4 | 210 | 4 | Other Direct Expenses | 
standalone P&L | R034-R037 | 4 | 211 | 4 | Employee Benefits Expenses | 
standalone P&L | R038-R041 | 4 | 212 | 4 | Finance Costs | 
standalone P&L | R042-R045 | 4 | 213 | 4 | Depreciation & Amortisation Expenses | 
standalone P&L | R046-R049 | 4 | 214 | 4 | Other Expenses | 
standalone P&L | R050-R053 | 4 | 215 | 4 | Total Expenses (IV) | 
standalone P&L | R054-R057 | 4 | 217 | 4 | V Profit Before Exceptional and Extraordinary Items and Tax (III-IV) | 
standalone P&L | R058-R061 | 4 | 218 | 4 | VI Exceptional Items | ZERO_STANDING(all periods)
standalone P&L | R062-R065 | 4 | 220 | 4 | VII Profit Before Extraordinary Items and Tax (V-VI) | 
standalone P&L | R066-R069 | 4 | 221 | 4 | VIII Extraordinary Items | ZERO_STANDING(all periods)
standalone P&L | R070-R073 | 4 | 222 | 4 | IX Profit Before Tax (VII-VIII) | 
standalone P&L | R074-R077 | 4 | 224 | 4 | (1) Current Tax | 
standalone P&L | R078-R081 | 4 | 225 | 4 | (2) Deferred Tax | NEGATIVE_AS_MINUS
standalone P&L | R082-R085 | 4 | 226 | 4 | (3) Tax Adjustments for Earlier Years | ZERO_STANDING(all periods)
standalone P&L | R086-R089 | 4 | 227 | 4 | XI Profit/(Loss) For The Period (IX-X) | 
standalone P&L | R090-R093 | 4 | 229 | 4 | (1) Basic | 
standalone P&L | R094-R097 | 4 | 230 | 4 | (2) Diluted | 
standalone P&L | R098-R101 | 4 | 231 | 4 | Total no of Shares (Weighted Average) | 
standalone P&L | R102-R105 | 4 | 232 | 4 | Diluted no of Shares (Weighted Average) | 
standalone P&L | R106-R109 | 4 | 233 | 4 | Face Value Per Share | 
standalone balance sheet | R110-R111 | 5 | 330 | 2 | (a) Share Capital | 
standalone balance sheet | R112-R113 | 5 | 331 | 2 | (b) Reserves and Surplus | 
standalone balance sheet | R114-R115 | 5 | 332 | 2 | (c) Money received against share warrants | 
standalone balance sheet | R116-R117 | 5 | 334 | 2 | (a) Long-Term Borrowings | 
standalone balance sheet | R118-R119 | 5 | 335 | 2 | (b) Deferred Tax Liabilities (Net) | 
standalone balance sheet | R120-R121 | 5 | 336 | 2 | (c) Long-Term Provisions | 
standalone balance sheet | R122-R123 | 5 | 338 | 2 | (a) Short-Term Borrowings | 
standalone balance sheet | R124-R125 | 5 | 341 | 2 | (A) Total outstanding dues of Micro Enterprises and Small Enterprises | 
standalone balance sheet | R126-R127 | 5 | 343 | 2 | (B) Total outstanding dues of Creditors other than Micro Enterprises a | 
standalone balance sheet | R128-R129 | 5 | 344 | 2 | (c) Other Current Liabilities | 
standalone balance sheet | R130-R131 | 5 | 345 | 2 | (d) Short-Term Provisions | 
standalone balance sheet | R132-R133 | 5 | 346 | 2 | TOTAL EQUITY AND LIABILITIES | 
standalone balance sheet | R134-R135 | 5 | 350 | 2 | (i) Property, Plant & Equipment | 
standalone balance sheet | R136-R137 | 5 | 351 | 2 | (ii) Intangible Assets | 
standalone balance sheet | R138-R139 | 5 | 352 | 2 | (iii) Capital Work in Progress | 
standalone balance sheet | R140-R141 | 5 | 353 | 2 | (iv) Intangible assets under development | 
standalone balance sheet | R142-R143 | 5 | 354 | 2 | (b) Non-Current Investments | 
standalone balance sheet | R144-R145 | 5 | 355 | 2 | (c) Other Non Current Assets | 
standalone balance sheet | R146-R147 | 5 | 357 | 2 | (a) Inventories | 
standalone balance sheet | R148-R149 | 5 | 358 | 2 | (b) Trade Receivables | 
standalone balance sheet | R150-R151 | 5 | 359 | 2 | (c) Cash & Cash Equivalents | 
standalone balance sheet | R152-R153 | 5 | 360 | 2 | (d) Other Current Assets | 
standalone balance sheet | R154-R155 | 5 | 361 | 2 | TOTAL ASSETS | 
standalone cash flow | R164-R165 | 7 | 543 | 2 | Profit Before Extraordinary items and tax | 
standalone cash flow | R166-R167 | 7 | 544 | 2 | Adjustments for depreciation and amortisation expense | 
standalone cash flow | R168-R169 | 7 | 545 | 2 | Adjustments for Provision of Gratuity | ZERO_STANDING(partial: 1 of 2 periods)
standalone cash flow | R170-R171 | 7 | 546 | 2 | Interest Expense | 
standalone cash flow | R172-R173 | 7 | 547 | 2 | Interest Income | 
standalone cash flow | R174-R175 | 7 | 548 | 2 | Profit On Sale of Fixed Asset | ZERO_STANDING(partial: 1 of 2 periods)
standalone cash flow | R176-R177 | 7 | 549 | 2 | Share of profit and loss from partnership firm or AOP or LLP | ZERO_STANDING(partial: 1 of 2 periods)
standalone cash flow | R178-R179 | 7 | 550 | 2 | Operating Profit before working capital changes: | 
standalone cash flow | R180-R181 | 7 | 551 | 2 | Adjustments for Decrease/(Increase) in Inventories | 
standalone cash flow | R182-R183 | 7 | 552 | 2 | Adjustments for Decrease/(Increase) in Trade Receivables | 
standalone cash flow | R184-R185 | 7 | 553 | 2 | Adjustments for Decrease/(Increase) in Other Non-Current Assets | 
standalone cash flow | R186-R187 | 7 | 554 | 2 | Adjustments for Decrease/(Increase) in Other Current Assets | 
standalone cash flow | R188-R189 | 7 | 555 | 2 | Adjustments for Increase/(Decrease) in Trade Payables | 
standalone cash flow | R190-R191 | 7 | 556 | 2 | Adjustments for Increase/(Decrease) in Other Current Liabilities | 
standalone cash flow | R192-R193 | 7 | 557 | 2 | Adjustments for Increase/(Decrease) in Provisions | ZERO_STANDING(partial: 1 of 2 periods)
standalone cash flow | R194-R195 | 7 | 558 | 2 | Cash generated from operations | 
standalone cash flow | R196-R197 | 7 | 559 | 2 | Dividends received | ZERO_STANDING(all periods)
standalone cash flow | R198-R199 | 7 | 560 | 2 | Interest paid | ZERO_STANDING(all periods)
standalone cash flow | R200-R201 | 7 | 561 | 2 | Interest received | ZERO_STANDING(all periods)
standalone cash flow | R202-R203 | 7 | 562 | 2 | Less: Income taxes paid | 
standalone cash flow | R204-R205 | 7 | 563 | 2 | Net cash flows from (used in) operating activities before extraordinar | 
standalone cash flow | R206-R207 | 7 | 564 | 2 | Proceeds from extraordinary items | ZERO_STANDING(all periods)
standalone cash flow | R208-R209 | 7 | 565 | 2 | Payment for extraordinary items | ZERO_STANDING(all periods)
standalone cash flow | R210-R211 | 7 | 566 | 2 | NET CASH FLOWS FROM (USED IN) OPERATING ACTIVITIES (A) | 
standalone cash flow | R212-R213 | 7 | 568 | 2 | Purchase of tangible assets & intangible assets | ZERO_STANDING(partial: 1 of 2 periods)
standalone cash flow | R214-R215 | 7 | 569 | 2 | Interest received | 
standalone cash flow | R216-R217 | 7 | 570 | 2 | Proceeds from Sale of Fixed Assets | ZERO_STANDING(partial: 1 of 2 periods)
standalone cash flow | R218-R219 | 7 | 571 | 2 | Fixed assets purchased including CWIP | ZERO_STANDING(partial: 1 of 2 periods)
standalone cash flow | R220-R221 | 7 | 572 | 2 | (Increase)/Decrease in Non-Current Investments | 
standalone cash flow | R222-R223 | 7 | 573 | 2 | NET CASH FLOWS FROM (USED IN) INVESTING ACTIVITIES (B) | 
standalone cash flow | R224-R225 | 7 | 575 | 2 | Interest paid | 
standalone cash flow | R226-R227 | 7 | 576 | 2 | Increase/(Decrease) in Long-Term Borrowings | 
standalone cash flow | R228-R229 | 7 | 577 | 2 | Increase/(Decrease) in Short-Term Borrowings | 
standalone cash flow | R230-R231 | 7 | 578 | 2 | Proceeds from issue of share warrants | ZERO_STANDING(partial: 1 of 2 periods)
standalone cash flow | R232-R233 | 7 | 579 | 2 | NET CASH FLOWS FROM (USED IN) FINANCING ACTIVITIES (C) | 
standalone cash flow | R234-R235 | 7 | 580 | 2 | D NET INCREASE IN CASH AND CASH EQUIVALENT (A+B+C) | 
standalone cash flow | R236-R237 | 7 | 581 | 2 | Opening Cash and Cash Equivalents | 
standalone cash flow | R238-R239 | 7 | 582 | 2 | CLOSING CASH AND CASH EQUIVALENT | 
standalone cash flow | R240-R241 | 7 | 583 | 2 | Reconciliation: Cash & Cash Equivalent as per Balance Sheet | 
standalone cash flow | R242-R243 | 7 | 584 | 2 | Cash & Cash Equivalent at the End of the Period | 
consolidated P&L | R249-R252 | 10 | 766 | 4 | I Revenue From Operations | 
consolidated P&L | R253-R256 | 10 | 767 | 4 | II Other Income | 
consolidated P&L | R257-R260 | 10 | 768 | 4 | III Total Income (I+II) | 
consolidated P&L | R261-R264 | 10 | 770 | 4 | Purchases of Stock in Trade | 
consolidated P&L | R265-R268 | 10 | 771 | 4 | Changes in inventories | 
consolidated P&L | R269-R272 | 10 | 772 | 4 | Other Direct Expenses | 
consolidated P&L | R273-R276 | 10 | 773 | 4 | Employee Benefits Expenses | 
consolidated P&L | R277-R280 | 10 | 774 | 4 | Finance Costs | 
consolidated P&L | R281-R284 | 10 | 775 | 4 | Depreciation & Amortisation Expenses | 
consolidated P&L | R285-R288 | 10 | 776 | 4 | Other Expenses | 
consolidated P&L | R289-R292 | 10 | 777 | 4 | Total Expenses (IV) | 
consolidated P&L | R293-R296 | 10 | 779 | 4 | V Profit Before Exceptional and Extraordinary Items and Tax (III-IV) | 
consolidated P&L | R297-R300 | 10 | 780 | 4 | VI Exceptional Items | ZERO_STANDING(all periods)
consolidated P&L | R301-R304 | 10 | 782 | 4 | VII Profit Before Extraordinary Items and Tax (V-VI) | 
consolidated P&L | R305-R307 | 10 | 783 | 3 | VIII Extraordinary Items | ZERO_STANDING(all periods); COLUMN_SHORT(3 of 4; see R586)
consolidated P&L | R308-R311 | 10 | 784 | 4 | IX Profit Before Tax (VII-VIII) | 
consolidated P&L | R312-R315 | 10 | 786 | 4 | (1) Current Tax | 
consolidated P&L | R316-R319 | 10 | 787 | 4 | (2) Deferred Tax | NEGATIVE_AS_MINUS
consolidated P&L | R320-R323 | 10 | 788 | 4 | (3) Tax Adjustments for Earlier Years | ZERO_STANDING(partial: 2 of 4 periods)
consolidated P&L | R324-R327 | 10 | 789 | 4 | XI Profit/(Loss) For The Period (IX-X) | 
consolidated P&L | R328-R331 | 10 | 790 | 4 | XII Less: Share of Minority Interest | 
consolidated P&L | R332-R335 | 10 | 792 | 4 | XIII Net Profit transferred to Reserves & Surplus (XI-XII) | 
consolidated P&L | R336-R339 | 10 | 794 | 4 | (1) Basic | 
consolidated P&L | R340-R343 | 10 | 795 | 4 | (2) Diluted | 
consolidated P&L | R344-R347 | 10 | 796 | 4 | Total no.of Shares (Weighted Average) | 
consolidated P&L | R348-R351 | 10 | 797 | 4 | Diluted no.of Shares (Weighted Average) | 
consolidated P&L | R352-R355 | 10 | 798 | 4 | Face Value Per Share | 
consolidated balance sheet | R356-R357 | 11 | 884 | 2 | (a) Share Capital | 
consolidated balance sheet | R358-R359 | 11 | 885 | 2 | (b) Reserves and Surplus | 
consolidated balance sheet | R360-R361 | 11 | 886 | 2 | (c) Money Received against Share Warrants | 
consolidated balance sheet | R362-R363 | 11 | 887 | 2 | 2 MINORITY INTEREST | 
consolidated balance sheet | R364-R365 | 11 | 889 | 2 | (a) Long-Term Borrowings | 
consolidated balance sheet | R366-R367 | 11 | 890 | 2 | (b) Deferred Tax Liabilities (Net) | 
consolidated balance sheet | R368-R369 | 11 | 891 | 2 | (c) Long-Term Provisions | 
consolidated balance sheet | R370-R371 | 11 | 893 | 2 | (a) Short-Term Borrowings | 
consolidated balance sheet | R372-R373 | 11 | 896 | 2 | (A) Total outstanding dues of Micro and small enterprises; and | 
consolidated balance sheet | R374-R375 | 11 | 897 | 2 | (B) Total outstanding dues of other creditors | 
consolidated balance sheet | R376-R377 | 11 | 898 | 2 | (c) Other Current Liabilities | 
consolidated balance sheet | R378-R379 | 11 | 899 | 2 | (d) Short-Term Provisions | 
consolidated balance sheet | R380-R381 | 11 | 900 | 2 | TOTAL | 
consolidated balance sheet | R382-R383 | 11 | 904 | 2 | (i) Property, Plant & Equipment | 
consolidated balance sheet | R384-R385 | 11 | 905 | 2 | (ii) Intangible Assets | 
consolidated balance sheet | R386-R387 | 11 | 906 | 2 | (iii) Capital Work in Progress | 
consolidated balance sheet | R388-R389 | 11 | 907 | 2 | (iv) Intangible Assets under Development | 
consolidated balance sheet | R390-R391 | 11 | 908 | 2 | (b) Other Non-Current Assets | 
consolidated balance sheet | R392-R393 | 11 | 910 | 2 | (a) Inventories | 
consolidated balance sheet | R394-R395 | 11 | 911 | 2 | (b) Trade Receivables | 
consolidated balance sheet | R396-R397 | 11 | 912 | 2 | (c) Cash & Cash Equivalents | 
consolidated balance sheet | R398-R399 | 11 | 913 | 2 | (d) Other Current Assets | 
consolidated balance sheet | R400-R401 | 11 | 914 | 2 | TOTAL | 
consolidated cash flow | R405-R406 | 13 | 1137 | 2 | Profit before extraordinary items and tax | 
consolidated cash flow | R407-R408 | 13 | 1138 | 2 | Adjustments for depreciation and amortisation expense | 
consolidated cash flow | R409-R410 | 13 | 1139 | 2 | Adjustments for Provision of Gratuity | 
consolidated cash flow | R411-R412 | 13 | 1140 | 2 | Interest Expenses | 
consolidated cash flow | R413-R414 | 13 | 1141 | 2 | Interest Income | 
consolidated cash flow | R415-R416 | 13 | 1142 | 2 | Exchange difference on Forex (Gain)/Loss | ZERO_STANDING(all periods)
consolidated cash flow | R417-R418 | 13 | 1143 | 2 | Profit on Sale of Fixed Assets | ZERO_STANDING(partial: 1 of 2 periods)
consolidated cash flow | R419-R420 | 13 | 1144 | 2 | Operating Profit before working capital changes: | 
consolidated cash flow | R421-R422 | 13 | 1145 | 2 | Adjustments for decrease/(increase) in trade receivables | 
consolidated cash flow | R423-R424 | 13 | 1146 | 2 | Adjustments for decrease/(increase) in inventories | 
consolidated cash flow | R425-R426 | 13 | 1147 | 2 | Adjustments for decrease/(increase) in other current assets | 
consolidated cash flow | R427-R428 | 13 | 1148 | 2 | Adjustments for decrease/(increase) in other non-current assets | 
consolidated cash flow | R429-R430 | 13 | 1149 | 2 | Adjustments for increase/(decrease) in trade payables | 
consolidated cash flow | R431-R432 | 13 | 1150 | 2 | Adjustments for increase/(decrease) in other current liabilities | 
consolidated cash flow | R433-R434 | 13 | 1151 | 2 | Net cash flows from (used in) operations | 
consolidated cash flow | R435-R436 | 13 | 1152 | 2 | Income taxes paid | 
consolidated cash flow | R437-R438 | 13 | 1153 | 2 | NET CASH FLOWS FROM (USED IN) OPERATING ACTIVITIES (A) | 
consolidated cash flow | R439-R440 | 13 | 1155 | 2 | Purchase of intangible assets & tangible assets | 
consolidated cash flow | R441-R442 | 13 | 1156 | 2 | Proceeds from sale of fixed assets | ZERO_STANDING(partial: 1 of 2 periods)
consolidated cash flow | R443-R444 | 13 | 1157 | 2 | Interest received | 
consolidated cash flow | R445-R446 | 13 | 1158 | 2 | NET CASH FLOWS FROM (USED IN) INVESTING ACTIVITIES (B) | 
consolidated cash flow | R447-R448 | 13 | 1160 | 2 | Interest paid | 
consolidated cash flow | R449-R450 | 13 | 1161 | 2 | Increase/(Decrease) in Long-Term Borrowings | 
consolidated cash flow | R451-R452 | 13 | 1162 | 2 | Increase/(Decrease) in Short-Term Borrowings | 
consolidated cash flow | R453-R454 | 13 | 1163 | 2 | Moneys raised through share warrants | ZERO_STANDING(partial: 1 of 2 periods)
consolidated cash flow | R455-R456 | 13 | 1164 | 2 | Net Additional / (Withdrawn) by Other Partners in Subsidiary Firm | 
consolidated cash flow | R457-R458 | 13 | 1165 | 2 | NET CASH FLOWS FROM (USED IN) FINANCING ACTIVITIES (C) | 
consolidated cash flow | R459-R460 | 13 | 1166 | 2 | D NET INCREASE IN CASH AND CASH EQUIVALENT (A+B+C) | 
consolidated cash flow | R461-R462 | 13 | 1167 | 2 | Opening Cash and Cash Equivalents | 
consolidated cash flow | R463-R464 | 13 | 1168 | 2 | CLOSING CASH AND CASH EQUIVALENT | 

Columns: P&L = H1 FY27, H2 FY26, H1 FY26, FY26 (4). Balance sheet = 30-Sep-2026, 31-Mar-2026 (2 rows per line). Cash flow = H1 FY27, FY26 (2).
Cross-statement ties for A3 (enumerated only): SA vs CON share capital R110/R356, reserves R112/R358 (identical); net profit SA R086-R089 vs CON transferred R332-R335 (1,365.09 vs 1,365.10); closing cash SA R238 vs BS R150; CON R463 vs BS R396. Standalone cash flow rows R212-R219 are flagged ROW_SKEW by A1 (R576).

## 3. ZERO_STANDING (44 dash rows in 23 line items; plus 1 Nil)
ROW IDs | table | line item | pattern
---|---|---|---
R058-R061 | standalone P&L | VI Exceptional Items | ZERO_STANDING(all periods)
R066-R069 | standalone P&L | VIII Extraordinary Items | ZERO_STANDING(all periods)
R082-R085 | standalone P&L | (3) Tax Adjustments for Earlier Years | ZERO_STANDING(all periods)
R168-R169 | standalone cash flow | Adjustments for Provision of Gratuity | ZERO_STANDING(partial: 1 of 2 periods)
R174-R175 | standalone cash flow | Profit On Sale of Fixed Asset | ZERO_STANDING(partial: 1 of 2 periods)
R176-R177 | standalone cash flow | Share of profit and loss from partnership firm or AOP or LLP | ZERO_STANDING(partial: 1 of 2 periods)
R192-R193 | standalone cash flow | Adjustments for Increase/(Decrease) in Provisions | ZERO_STANDING(partial: 1 of 2 periods)
R196-R197 | standalone cash flow | Dividends received | ZERO_STANDING(all periods)
R198-R199 | standalone cash flow | Interest paid | ZERO_STANDING(all periods)
R200-R201 | standalone cash flow | Interest received | ZERO_STANDING(all periods)
R206-R207 | standalone cash flow | Proceeds from extraordinary items | ZERO_STANDING(all periods)
R208-R209 | standalone cash flow | Payment for extraordinary items | ZERO_STANDING(all periods)
R212-R213 | standalone cash flow | Purchase of tangible assets & intangible assets | ZERO_STANDING(partial: 1 of 2 periods)
R216-R217 | standalone cash flow | Proceeds from Sale of Fixed Assets | ZERO_STANDING(partial: 1 of 2 periods)
R218-R219 | standalone cash flow | Fixed assets purchased including CWIP | ZERO_STANDING(partial: 1 of 2 periods)
R230-R231 | standalone cash flow | Proceeds from issue of share warrants | ZERO_STANDING(partial: 1 of 2 periods)
R297-R300 | consolidated P&L | VI Exceptional Items | ZERO_STANDING(all periods)
R305-R307 | consolidated P&L | VIII Extraordinary Items | ZERO_STANDING(all periods)
R320-R323 | consolidated P&L | (3) Tax Adjustments for Earlier Years | ZERO_STANDING(partial: 2 of 4 periods)
R415-R416 | consolidated cash flow | Exchange difference on Forex (Gain)/Loss | ZERO_STANDING(all periods)
R417-R418 | consolidated cash flow | Profit on Sale of Fixed Assets | ZERO_STANDING(partial: 1 of 2 periods)
R441-R442 | consolidated cash flow | Proceeds from sale of fixed assets | ZERO_STANDING(partial: 1 of 2 periods)
R453-R454 | consolidated cash flow | Moneys raised through share warrants | ZERO_STANDING(partial: 1 of 2 periods)
R605 | certificate | Remarks column Nil | ZERO_STANDING (token read from OCR, see R605)
Template signals: Exceptional Items and Extraordinary Items lines stand at nil in all periods; Tax Adjustments for Earlier Years nil except R320-R323 (0.37 in H2 FY26); cash flow dividends, interest paid/received in the operating block nil (SA R196-R201).

## 4. OTHER NUMBERS (non-table, 43 rows)
ROW IDs | description | A2 flags
---|---|---
R001 | outcome letter date (also DATE R520) | RESTATED
R002 | NSE address pin | 
R003-R004 | LRR standards references (standalone) | 
R005 | SEBI circular ref (standalone LRR); restated R244 | RESTATED
R006-R009 | auditor identifiers standalone LRR: FRN, peer review, membership, UDIN | OCR_VARIANT: FRN R006 vs R245 vs R479 differ in read
R156-R163 | warrant terms in standalone note 3 (issue price, split, balance, window) | RESTATED across R472-R478, R568, R608-R609
R244 | SEBI circular ref (consolidated LRR) | RESTATED of R005
R245-R248 | auditor identifiers consolidated LRR | OCR_VARIANT on FRN (R245 vs R006 vs R479)
R402-R404 | partner profit shares in subsidiary (90 / 7.5 / 2.5) | ties to R592, R501-R503
R465 | NSE circular ref in certificate | ties to R508
R466-R467 | certificate utilised and unutilised amounts | materiality: Rs 520.31 + 6.55 = 526.86 Lakhs, ties to R114
R468-R470 | certificate allocation and subscription share | RESTATED R604
R471-R478 | certificate note 1 warrant terms | RESTATED of R156-R163
R479-R482 | auditor identifiers certificate | OCR_VARIANT on FRN

## 5. AGENDA ITEMS (Board Outcome letter, page 1)
ROW ID | item | flags | note
---|---|---|---
R553 | agenda 1: approval of unaudited standalone and consolidated results with LRR | | ties R520-R524
R554 | agenda 2: Reg 32 statement of deviation for warrant proceeds with auditor certificate | | ties R606
Meeting: R521 (date), R524 (start and end times; 120 minutes), R522 (period). No AR approval, AGM notice, record date, dividend, director appointment, auditor change, ESOP or fund-raising resolution appears in the structured file: absence noted for A3.

## 6. AUDITOR PARAGRAPHS (9) and UDINs
ROW ID | para | flags | note
---|---|---|---
R556 | SA LRR basis of preparation (p2 l93) |  | 
R557 | SA LRR scope, moderate assurance (p2 l102) |  | 
R558 | SA LRR no audit opinion (p3 l113) |  | 
R559 | SA LRR conclusion, unmodified (p3 l121) |  | 
R579 | CON LRR scope (p8 l631) |  | 
R580 | CON LRR no audit opinion (p8 l642) |  | 
R581 | CON LRR subsidiary results unaudited, relied on (p9 l660) | FOOTNOTE_UNRESOLVED | ties R593
R582 | CON LRR basis: management statement (p9 l665) |  | 
R583 | CON LRR conclusion, unmodified (p9 l667) |  | 
Identifiers: SA LRR R006-R009 (UDIN R009), CON LRR R245-R248 (UDIN R248), certificate R479-R482 (UDIN R482); three different UDINs, FRN read three ways (OCR_VARIANT). Auditor entities R486, R489, R491, R499, R504, R509, R510. No Emphasis of Matter, Other Matter or Going Concern paragraph appears in the structured file (absence for A3).

## 7. ANNEXURE: UTILISATION CERTIFICATE (pages 14-15)
ROW IDs | item
---|---
R603 | certificate basis; period to 30-Sep-2026
R604 | allocation and subscription qualifier
R605 | remarks column Nil (ZERO_STANDING)
R606 | no-deviation conclusion
R516 | objects of issue (forward use of proceeds)
R465-R470 | numbers table (see section 4)
R504, R505, R507, R508 | certificate entities
R545-R552 | certificate dates
Utilised R466 plus unutilised R467 sums to the subscription in R470 and R114: flag for A3 only; where the unutilised amount sits is not stated in the structured file.

## 8. ENTITIES (28; consolidation list = 2)
ROW ID | flags | note
---|---|---
R483 |  |  (p1 l23)
R484 |  |  (p1 l27)
R485 |  |  (p1 l29)
R486 |  |  (p1 l42)
R487 | CONSOLIDATION_LIST | holding / sole subsidiary Danya Electric Company (partnership, 90%) (p1 l57)
R488 |  |  (p1 l62)
R489 |  |  (p2 l66)
R490 |  |  (p2 l88)
R491 |  |  (p3 l141)
R492 |  |  (p4 l150)
R493 |  |  (p4 l151)
R494 |  | MD signatory, DIN stated (p5 l363)
R495 |  |  (p6 l432)
R496 |  |  (p6 l435)
R497 |  |  (p6 l436)
R498 |  |  (p6 l443)
R499 |  |  (p8 l590)
R500 | CONSOLIDATION_LIST | holding / sole subsidiary Danya Electric Company (partnership, 90%) (p9 l654)
R501 | CONSOLIDATION_LIST | holding / sole subsidiary Danya Electric Company (partnership, 90%) (p12 l1008)
R502 | RELATED_PARTY | other partners in Danya; Vee Rajmohan is also MD (R494) (p12 l1010)
R503 | RELATED_PARTY | other partners in Danya; Vee Rajmohan is also MD (R494) (p12 l1010)
R504 |  |  (p14 l1176)
R505 |  |  (p14 l1184)
R506 |  |  (p14 l1186)
R507 |  |  (p14 l1188)
R508 |  |  (p14 l1196)
R509 |  |  (p15 l1255)
R510 |  |  (p15 l1260)
ENTITY_CHANGE: not testable, no prior ledger.

## 9. DATES (33) and FORWARD (9)
ROW ID | kind | page/line | flags
R520 | DATE | p1 l19 | 
R521 | DATE | p1 l31 | 
R522 | DATE | p1 l40 | 
R523 | DATE | p1 l47 | 
R524 | DATE | p1 l51 | 
R525 | DATE | p1 l60 | 
R526 | DATE | p2 l86 | 
R527 | DATE | p3 l117 | RESTATED
R528 | DATE | p3 l135 | RESTATED
R529 | DATE | p4 l201 | 
R530 | DATE | p5 l326 | 
R531 | DATE | p5 l363 | RESTATED
R532 | DATE | p6 l432 | RESTATED
R533 | DATE | p6 l435 | RESTATED
R534 | DATE | p6 l436 | RESTATED
R535 | DATE | p6 l461 | RESTATED
R536 | DATE | p7 l540 | 
R537 | DATE | p9 l647 | RESTATED
R538 | DATE | p9 l685 | RESTATED
R539 | DATE | p10 l763 | 
R540 | DATE | p11 l880 | 
R541 | DATE | p12 l1002 | RESTATED
R542 | DATE | p12 l1018 | 
R543 | DATE | p12 l1043 | RESTATED
R544 | DATE | p13 l1134 | 
R545 | DATE | p14 l1195 | 
R546 | DATE | p14 l1196 | 
R547 | DATE | p14 l1200 | 
R548 | DATE | p15 l1226 | 
R549 | DATE | p15 l1229 | 
R550 | DATE | p15 l1235 | RESTATED
R551 | DATE | p15 l1237 | RESTATED
R552 | DATE | p15 l1264 | RESTATED
R511 | FORWARD | p6 l439 | RESTATED R517
R512 | FORWARD | p6 l441 | RESTATED R518
R513 | FORWARD | p6 l443 | RESTATED R519
R514 | FORWARD | p6 l446 | RESTATED R515
R515 | FORWARD | p12 l1023 | RESTATED R514
R516 | FORWARD | p14 l1204 | use of proceeds
R517 | FORWARD | p15 l1242 | RESTATED R511
R518 | FORWARD | p15 l1247 | RESTATED R512
R519 | FORWARD | p15 l1249 | RESTATED R513

## 10. SIGNATURE BLOCKS (3)
ROW ID | signatory | note
---|---|---
R555 / R525 | Priyanka Bansal, CS (R488), digital signature 16:37:54 on 16-Oct-2026 | meeting concluded 16:30 (R524): signature after close, no flag
R494 / R531 | Vee Rajmohan, MD, for Board, dated 16-10-2026 (balance sheet) | 
R491 / R510 | R. Rajaram, Partner (auditor), LRRs and certificate | UDINs per section 6

## 11. TABLE QUALIFIERS AND A1 NOTES
R560, R561, R563, R574, R575, R584, R585, R587, R599, R600 | unit and audit-status qualifiers for the six financial tables (audit status: H1 FY27, H2 FY26, H1 FY26 unaudited; FY26 audited)
R562 | A1 note: standalone Paid up Equity Share Capital row has no value in image | FOOTNOTE_UNRESOLVED; possible line-item gap for A1 check
R576 | A1 note: standalone cash flow values assigned by row order, image skewed | ROW_SKEW
R586 | A1 note: consolidated Extraordinary Items row has 3 columns not 4 | COLUMN_SHORT

## 12. MISSING_FROM_STRUCTURED
None raised. Sweep was of the structured file only; source not opened.
