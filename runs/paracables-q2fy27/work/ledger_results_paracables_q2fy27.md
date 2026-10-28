# A2 COMPLETENESS LEDGER: results | PARACABLES | Q2 FY27 (quarter and half year ended 30-Sep-2026)
source of IDs: extracted/paracables-results-q2fy27-structured.md (R001-R989). Rows reference IDs; claim text stays in the structured file.
Prior-quarter ledger: none available. ENTITY_CHANGE and DROPPED diffs vs prior quarter cannot be run; only in-document entity changes are flagged.

ids_in_structured: 989 | ids_referenced_in_ledger: 989 | orphan_ids: [] | match: yes
missing_from_structured: 4 values on 2 line items (M001-M004), see section 2b

=== A2 COUNT TEST ===
category: notes           grep_count: 20  sweep_count: 20  match: yes  (raw grep gave 7 SA + 8 CO + 4 CF = 19; CO note 1 on fulltext line 625 starts "~ 4" (OCR of "1"); re-swept, 9 CO notes confirmed; sub-items 4a-c and 5a-c = 6 extra, listed in section 1)
category: footnotes       grep_count: 2   sweep_count: 2   match: yes  (asterisk footnote under use-of-proceeds table: R948 p6, R982 p12; unit and audit-status qualifiers in section 9)
category: line_items      grep_count: 235 sweep_count: 235  match: yes  (distinct page+line pairs vs stem groups in structured file); fulltext line sweep found 2 more lines missing from structured = 237 total
category: zero_standing   grep_count: 148 sweep_count: 148  match: yes  (grep -c ZERO_STANDING on structured: 143 table rows, 5 NIL values in auditor para 5 R852-R856); plus 2 nil cells in missing rows M002, M004 = 150
category: agenda_items    grep_count: 2   sweep_count: 2   match: yes  (Board Outcome items a) and b) only)
category: auditor_paras   grep_count: 11  sweep_count: 11  match: yes  (SA 4 paras; CO 6 numbered paras + 1 unnumbered SEBI circular paragraph)
category: entities        grep_count: 29  sweep_count: 29  match: yes  (ENTITY rows; consolidation list = 2 subsidiaries + 1 divested)
category: signature_blocks grep_count: 4 sweep_count: 4  match: yes
gate_a2: pass
=== END COUNT TEST ===

## 0. VERIFICATION STATUS BY PAGE (carry to A3/A4)
page | content | A1 status
---|---|---
1 | Board Outcome letter, signature | RAW OCR (not image-checked)
2 | Standalone limited review report, UDIN | RAW OCR; UDIN FOOTNOTE_UNRESOLVED (R941, R830)
3 | Standalone P&L | IMAGE-CHECKED
4 | Standalone balance sheet | IMAGE-CHECKED
5 | Standalone cash flow, CF notes | IMAGE-CHECKED (note text 1-2 raw OCR)
6 | Standalone notes 1-7 | RAW OCR for note text; use-of-proceeds table values IMAGE-CHECKED (C36)
7 | Consolidated review report p1 | RAW OCR
8 | Consolidated review report p2, UDIN | RAW OCR; UDIN labelled "DIN" in OCR (R861), treat as unresolved
9 | Consolidated P&L | IMAGE-CHECKED
10 | Consolidated balance sheet | IMAGE-CHECKED
11 | Consolidated cash flow | IMAGE-CHECKED (2 rows missed by A1, see 2b)
12 | Consolidated notes 1-9 | RAW OCR for note text; use-of-proceeds table values IMAGE-CHECKED (C37)
13 | Segment annexure A | IMAGE-CHECKED
Note: the 38 OCR corrections (C01-C38) are logged in the fulltext header; A2 does not re-test them.

## 1. NOTES (numbered notes, sub-items, footnotes)
ROW_IDs | note | A2 flags | cross-ref / materiality note
---|---|---|---
R944, R919 | SA note 1 (audit committee + board 26 Oct 2026) p6 | - | RAW_OCR; twin CO note 1
R945 | SA note 2 (limited review, unmodified opinion) p6 | - | RAW_OCR; twin R979
R946 | SA note 3 (Ind AS, s133) p6 | - | RAW_OCR; twin R980
R834-R838, R890, R920, R921 | SA note 4a (preferential equity to non-promoters, EGM 06.06.2026, allotted 01.07.2026, share count change) p6 | RESTATED | twin CO note 5a; allottees unnamed
R839, R840, R909, R922 | SA note 4b (72,00,000 promoter warrants, 25% application money, allotted 01.07.2026) p6 | RESTATED; FORWARD | 75% balance payable on conversion, timing not stated; twin CO note 5b
R841-R845, R947-R949 | SA note 4c (use-of-proceeds table, no-deviation statement) p6 | RESTATED | table IMAGE-CHECKED (C36); asterisk footnote R948: unutilised amount parked in mutual fund and utilisation account; unutilised Rs 26.66 Cr (R845) is the item to track against balance-sheet current investments (R219)
R846-R848, R891, R923 | SA note 5 (ESOP allotment 14.07.2026, share count change) p6 | RESTATED | twin CO note 6
R950 | SA note 6 (no separate reportable segments, Ind AS 108) p6 | - | contrasts with CO note 8 (two reportable segments, R985)
R951 | SA note 7 (regrouping of prior periods) p6 | - | twin CO note 9 R986
R964 | SA cash flow note 1 (indirect method, Ind AS 7) p5 | - | twin R967
R965 | SA cash flow note 2 (brackets = outflow) p5 | - | twin R968
R978, R933 | CO note 1 (audit committee + board 26 Oct 2026) p12 | - | RAW_OCR; OCR rendered "1" as "4" on line 625
R979 | CO note 2 (limited review, unmodified) p12 | - | RAW_OCR
R980 | CO note 3 (Ind AS, s133) p12 | - | RAW_OCR
R981, R862 | CO note 4 (consolidation per Ind AS 110) p12 | - | RAW_OCR
R863-R866, R934, R935 | CO note 5a (preferential equity) p12 | RESTATED | twin SA note 4a
R867, R868, R910 | CO note 5b (warrants) p12 | RESTATED; FORWARD | twin SA 4b
R869-R873, R982, R983 | CO note 5c (use of proceeds) p12 | RESTATED | table IMAGE-CHECKED (C37)
R874-R876, R901, R936 | CO note 6 (ESOP allotment) p12 | RESTATED | twin SA note 5
R984, R902, R937 | CO note 7 (Valens Technologies divested 6 Nov 2025; FY27 columns exclude it; Q2 FY26, H1 FY26, FY26 include it; not directly comparable) p12 | ENTITY_CHANGE | material: every YoY comparison in the consolidated P&L spans the divestment
R985, R903, R904 | CO note 8 (two reportable segments Wires & Cables, Pipes; Annexure A) p12 | - | Pipes nil in FY27 columns (section 2, segment annexure)
R986 | CO note 9 (regrouping) p12 | - | twin SA note 7
R967, R968 | CO cash flow notes 1-2 p11 | - | twin R964, R965

Note count: SA 7 + CO 9 + CF 4 = 20 numbered notes; sub-items SA 4a/4b/4c and CO 5a/5b/5c = 6. No dagger or "Note:" items beyond the two cash-flow note blocks.

## 2. LINE ITEMS (every financial-table line; labels only, values stay in the structured file)
Twin = same line in the standalone vs consolidated statement. "FY27 current columns equal twin" = quarter 30.09.2026, quarter 30.06.2026 and half-year 30.09.2026 columns (P&L), or the 30.09.2026 column (BS/CF), equal in the structured file. A2 does not test arithmetic.

### Standalone P&L (p3)  | verification: IMAGE-CHECKED (page image)

ROW_IDs | line item (label only) | n_vals | A2 flags | cross-ref / materiality note
---|---|---|---|---
R001-R006 | I Revenue from operations | 6 | - | consolidated twin R345-R350; FY27 current columns equal twin
R007-R012 | II Other income | 6 | - | consolidated twin R351-R356; FY27 current columns equal twin
R013-R018 | III Total Income (I+II) | 6 | - | consolidated twin R357-R362; FY27 current columns equal twin
R019-R024 | (a) Cost of materials consumed | 6 | - | consolidated twin R363-R368; FY27 current columns equal twin
R025-R030 | (b) Changes in inventories of finished goods, | 6 | - | consolidated twin R369-R374; FY27 current columns equal twin
R031-R036 | (c) Employee benefits expense | 6 | - | consolidated twin R375-R380; FY27 current columns equal twin
R037-R042 | (d) Finance costs | 6 | - | consolidated twin R381-R386; FY27 current columns equal twin
R043-R048 | (e) Depreciation and amortization expense | 6 | - | consolidated twin R387-R392; FY27 current columns equal twin
R049-R054 | (f}) Other expenses | 6 | - | consolidated twin R393-R398; FY27 current columns equal twin
R055-R060 | Total Expenses (IV) | 6 | - | consolidated twin R399-R404; FY27 current columns equal twin
R061-R066 | V Profit before exceptional items and tax (ill -IV) | 6 | - | consolidated twin R405-R410; FY27 current columns equal twin
R067-R072 | VI Exceptional items | 6 | ZERO_STANDING(all 6) | consolidated twin R411-R416; FY27 current columns equal twin
R073-R078 | Vil Profit after exceptional items but before tax (V+VI) | 6 | - | consolidated twin R417-R422; FY27 current columns equal twin
R079-R084 | (I) Current Tax | 6 | - | consolidated twin R423-R428; FY27 current columns equal twin
R085-R090 | (II) Deferred Tax | 6 | - | consolidated twin R429-R434; FY27 current columns equal twin
R091-R096 | IX Profit for the period from continuing operations (VII | 6 | - | consolidated twin R435-R440; FY27 current columns equal twin
R097-R102 | X Profit from discontinued operations | 6 | ZERO_STANDING(all 6) | consolidated twin R441-R446; FY27 current columns equal twin
R103-R108 | XI Tax expense of discontinued operations | 6 | ZERO_STANDING(all 6) | consolidated twin R447-R452; FY27 current columns equal twin
R109-R114 | XII Profit from discontinued operations (after tax) | 6 | ZERO_STANDING(all 6) | consolidated twin R453-R458; FY27 current columns equal twin
R115-R120 | XIII Profit for the period (IX + XII) | 6 | - | consolidated twin R459-R464; FY27 current columns equal twin
R121-R126 | A. (I) Items that will not be reclassified to profit or loss | 6 | - | consolidated twin R465-R470; FY27 current columns equal twin
R127-R132 | (II) Income tax relating to items that will not be | 6 | - | consolidated twin R471-R476; FY27 current columns equal twin
R133-R138 | B. (I) Items that will be reclassified to profit or loss | 6 | ZERO_STANDING(all 6) | consolidated twin R477-R482; FY27 current columns equal twin
R139-R144 | (II) Income tax relating to items that will be | 6 | ZERO_STANDING(all 6) | consolidated twin R483-R488; FY27 current columns equal twin
R145-R150 | Total other comprehensive income /(Loss) (XIV) | 6 | - | consolidated twin R489-R494; FY27 current columns equal twin
R151-R156 | XV Total Comprehensive Income ( Comprising Profit and | 6 | - | consolidated twin R495-R500; FY27 current columns equal twin
R157-R162 | XVI] Paid-up Equity Share Capital (Face Value Rs. 2 per shar | 6 | - | consolidated twin R501-R506; FY27 current columns equal twin
R163-R168 | (1) Basic | 6 | - | consolidated twin R507-R512; FY27 current columns equal twin
R169-R174 | (2) Diluted | 6 | - | consolidated twin R513-R518; FY27 current columns equal twin
R175-R180 | (1) Basic | 6 | ZERO_STANDING(all 6) | consolidated twin R519-R524; FY27 current columns equal twin
R181-R186 | (2) Diluted | 6 | ZERO_STANDING(all 6) | consolidated twin R525-R530; FY27 current columns equal twin
R187-R192 | (1) Basic | 6 | - | consolidated twin R531-R536; FY27 current columns equal twin
R193-R198 | (2) Diluted | 6 | - | consolidated twin R537-R542; FY27 current columns equal twin
R877 | Other Equity excluding revaluation Reserve | 1 | - | consolidated twin R878; FY27 current columns equal twin; OTHER EQUITY ex-revaluation reserve, FY26 column only; duplicates BS Other Equity 31.03.2026 (R240/R584)

### Standalone balance sheet (p4)  | verification: IMAGE-CHECKED (page image)

ROW_IDs | line item (label only) | n_vals | A2 flags | cross-ref / materiality note
---|---|---|---|---
R199-R200 | (a) Property, Plant and Equipment | 2 | - | consolidated twin R543-R544; FY27 current columns equal twin
R201-R202 | (b) Capital work-in-progress | 2 | ZERO_STANDING(1 of 2) | consolidated twin R545-R546; FY27 current columns equal twin
R203-R204 | (c) Right of use assets | 2 | - | consolidated twin R547-R548; FY27 current columns equal twin
R205-R206 | (d) Other Intangible Assets | 2 | - | consolidated twin R549-R550; FY27 current columns equal twin
R207-R208 | (i) Investments | 2 | ZERO_STANDING(all 2) | consolidated twin R551-R552; FY27 current columns equal twin
R209-R210 | (ii) Loans | 2 | - | consolidated twin R553-R554; FY27 current columns equal twin
R211-R212 | (ii) Others Non-Current Financial Assets | 2 | - | consolidated twin R555-R556; FY27 current columns equal twin
R213-R214 | (f) Other Non-Current Assets | 2 | - | consolidated twin R557-R558; FY27 current columns equal twin
R215-R216 | Total Non-Current Assets | 2 | - | consolidated twin R559-R560; FY27 current columns equal twin
R217-R218 | (a) Inventories | 2 | - | consolidated twin R561-R562; FY27 current columns equal twin
R219-R220 | (i) Investments | 2 | ZERO_STANDING(1 of 2) | consolidated twin R563-R564; FY27 current columns equal twin
R221-R222 | (ii) Trade receivables | 2 | - | consolidated twin R565-R566; FY27 current columns equal twin
R223-R224 | (iii) Cash and cash equivalents | 2 | - | consolidated twin R567-R568; FY27 current columns equal twin
R225-R226 | (iv) Bank balances other than (iii) above | 2 | - | consolidated twin R569-R570; FY27 current columns equal twin
R227-R228 | (v) Loans | 2 | - | consolidated twin R571-R572; FY27 current columns equal twin
R229-R230 | (vi) Other Current Financial Assets | 2 | - | consolidated twin R573-R574; FY27 current columns equal twin
R231-R232 | (c) Other Current Assets | 2 | - | consolidated twin R575-R576; FY27 current columns equal twin
R233-R234 | Total Current Assets | 2 | - | consolidated twin R577-R578; FY27 current columns equal twin
R235-R236 | Total Assets | 2 | - | consolidated twin R579-R580; FY27 current columns equal twin
R237-R238 | (a) Equity Share Capital | 2 | - | consolidated twin R581-R582; FY27 current columns equal twin
R239-R240 | (b) Other Equity | 2 | - | consolidated twin R583-R584; FY27 current columns equal twin
R241-R242 | Total Equity | 2 | - | consolidated twin R585-R586; FY27 current columns equal twin
R243-R244 | (i) Borrowings | 2 | - | consolidated twin R587-R588; FY27 current columns equal twin
R245-R246 | (ii) Lease Liabilities | 2 | - | consolidated twin R589-R590; FY27 current columns equal twin
R247-R248 | (b) Provisions | 2 | - | consolidated twin R591-R592; FY27 current columns equal twin
R249-R250 | (c) Deferred Tax Liabilities (Net) | 2 | - | consolidated twin R593-R594; FY27 current columns equal twin
R251-R252 | Total Non-Current Liabilities | 2 | - | consolidated twin R595-R596; FY27 current columns equal twin
R253-R254 | (i) Borrowings | 2 | - | consolidated twin R597-R598; FY27 current columns equal twin
R255-R256 | (ii) Lease Liabilities | 2 | - | consolidated twin R599-R600; FY27 current columns equal twin
R257-R258 | Total outstanding dues of Micro Enterprises | 2 | - | consolidated twin R601-R602; FY27 current columns equal twin
R259-R260 | Total outstanding dues of creditors other than | 2 | - | consolidated twin R603-R604; FY27 current columns equal twin
R261-R262 | (iv) Other Current Financial Liabilities | 2 | - | consolidated twin R605-R606; FY27 current columns equal twin
R263-R264 | (b) Other Current Liabilities | 2 | - | consolidated twin R607-R608; FY27 current columns equal twin
R265-R266 | (c) Provisions | 2 | - | consolidated twin R609-R610; FY27 current columns equal twin
R267-R268 | (d) Current Tax Liability (Net) | 2 | - | consolidated twin R611-R612; FY27 current columns equal twin
R269-R270 | Total Current Liabilities | 2 | - | consolidated twin R613-R614; FY27 current columns equal twin
R271-R272 | Total Equity and Liabilities | 2 | - | consolidated twin R615-R616; FY27 current columns equal twin

### Standalone cash flow (p5)  | verification: IMAGE-CHECKED (page image)

ROW_IDs | line item (label only) | n_vals | A2 flags | cross-ref / materiality note
---|---|---|---|---
R273-R274 | Net Profit before taxation | 2 | - | consolidated twin R617-R618; FY27 current columns equal twin
R275-R276 | Depreciation and amortization expenses | 2 | - | consolidated twin R619-R620; FY27 current columns equal twin
R277-R278 | Interest Expenses/ Finance Cost | 2 | - | consolidated twin R621-R622; FY27 current columns equal twin
R279-R280 | Interest on lease liability | 2 | - | consolidated twin R623-R624; FY27 current columns equal twin
R281-R282 | Reversal of lease rent liability | 2 | - | consolidated twin R625-R626; FY27 current columns equal twin
R283-R284 | Unrealised Exchange (Gain)/Loss | 2 | - | consolidated twin R627-R628; FY27 current columns equal twin
R285-R286 | Profit on sales of Mutual Funds | 2 | - | consolidated twin R629-R630; FY27 current columns equal twin
R287-R288 | (Profit) /Loss on sale of Property, plant & equipments (net) | 2 | ZERO_STANDING(1 of 2) | consolidated twin R631-R632; FY27 current columns equal twin
R289-R290 | Interest Income | 2 | - | consolidated twin R633-R634; FY27 current columns equal twin
R291-R292 | Net (Gain)/ Loss on Derivatives | 2 | - | consolidated twin R635-R636; FY27 current columns equal twin
R293-R294 | Provision for Doubtful debts/ Written back | 2 | - | consolidated twin R637-R638; FY27 current columns equal twin
R295-R296 | Employees share based payment expenses | 2 | - | consolidated twin R639-R640; FY27 current columns equal twin
R297-R298 | Operating Profit before working capital changes | 2 | - | consolidated twin R641-R642; FY27 current columns equal twin
R299-R300 | Decrease / (Increase) in Trade Receivables | 2 | - | consolidated twin R643-R644; FY27 current columns equal twin
R301-R302 | Decrease / (Increase) in Loans & Advances | 2 | - | consolidated twin R645-R646; FY27 current columns equal twin
R303-R304 | Decrease / (Increase) in Inventories | 2 | - | consolidated twin R647-R648; FY27 current columns equal twin
R305-R306 | Decrease / (Increase) in Other financial and non financial A | 2 | - | consolidated twin R649-R650; FY27 current columns equal twin
R307-R308 | (Decrease) / Increase in Trade Payables | 2 | - | consolidated twin R651-R652; FY27 current columns equal twin
R309-R310 | (Decrease) / Increase in Other Liabilities & Provisions | 2 | - | consolidated twin R653-R654; FY27 current columns equal twin
R311-R312 | Cash generated from operation | 2 | - | consolidated twin R655-R656; FY27 current columns equal twin
R313-R314 | Exceptional items | 2 | ZERO_STANDING(all 2) | consolidated twin R657-R658; FY27 current columns equal twin
R315-R316 | Income Tax Paid/ Refund/ Provisions (Net) | 2 | - | consolidated twin R659-R660; FY27 current columns equal twin
R317-R318 | NET CASH FROM OPERATING ACTIVITIES (A) | 2 | - | consolidated twin R661-R662; FY27 current columns equal twin
R319-R320 | Purchase of Property plant & equipments including Capital Wo | 2 | - | consolidated twin R663-R664; FY27 current columns equal twin
R321-R322 | Sale of Property plant & equipments | 2 | ZERO_STANDING(1 of 2) | consolidated twin = M001-M002 (MISSING_FROM_STRUCTURED)
R323-R324 | Interest Received | 2 | - | consolidated twin R665-R666; FY27 current columns equal twin
R325-R326 | Sale of Investments (Mutual Fund) | 2 | - | consolidated twin R667-R668; FY27 current columns equal twin
R327-R328 | Purchase of Investments (Mutual Fund) | 2 | - | consolidated twin R669-R670; FY27 current columns equal twin
R329-R330 | NET CASH FROM INVESTING ACTIVITIES (B) | 2 | - | consolidated twin R671-R672; FY27 current columns equal twin
R331-R332 | Interest Expenses/ Finance Cost | 2 | - | consolidated twin R673-R674; FY27 current columns equal twin
R333-R334 | Increase/(Decrease) in Borrowings from banks / ARC /NBFC ( n | 2 | - | consolidated twin R675-R676; FY27 current columns equal twin
R335-R336 | Net Proceeds from Issue of Equity Shares and Convertibles Eq | 2 | ZERO_STANDING(1 of 2) | consolidated twin = M003-M004 (MISSING_FROM_STRUCTURED)
R337-R338 | NET CASH FROM FINANCING ACTIVITIES (C) | 2 | - | consolidated twin R677-R678; FY27 current columns equal twin
R339-R340 | NET INCREASE/(DECREASE) IN CASH & CASH EQUIVALENTS | 2 | - | consolidated twin R679-R680; FY27 current columns equal twin
R341-R342 | CASH AND CASH EQUIVALENTS AT BEGINNING OF THE YEAR | 2 | - | consolidated twin R681-R682; FY27 current columns equal twin
R343-R344 | CASH AND CASH EQUIVALENTS AT END OF THE PERIOD | 2 | - | consolidated twin R683-R684; FY27 current columns equal twin

### Consolidated P&L (p9)  | verification: IMAGE-CHECKED (page image)

ROW_IDs | line item (label only) | n_vals | A2 flags | cross-ref / materiality note
---|---|---|---|---
R345-R350 | I Revenue from operations | 6 | - | standalone twin R001-R006; FY27 current columns equal twin; prior-year columns include Valens Technologies (note 7); not comparable
R351-R356 | II Other income | 6 | - | standalone twin R007-R012; FY27 current columns equal twin; prior-year columns include Valens Technologies (note 7); not comparable
R357-R362 | III Total Income (I+II) | 6 | - | standalone twin R013-R018; FY27 current columns equal twin; prior-year columns include Valens Technologies (note 7); not comparable
R363-R368 | (a) Cost of materials consumed | 6 | - | standalone twin R019-R024; FY27 current columns equal twin; prior-year columns include Valens Technologies (note 7); not comparable
R369-R374 | (b) Changes in inventories of finished goods, | 6 | - | standalone twin R025-R030; FY27 current columns equal twin
R375-R380 | (c) Employee benefits expense | 6 | - | standalone twin R031-R036; FY27 current columns equal twin; prior-year columns include Valens Technologies (note 7); not comparable
R381-R386 | (d) Finance costs | 6 | - | standalone twin R037-R042; FY27 current columns equal twin; prior-year columns include Valens Technologies (note 7); not comparable
R387-R392 | (e) Depreciation and amortization expense | 6 | - | standalone twin R043-R048; FY27 current columns equal twin; prior-year columns include Valens Technologies (note 7); not comparable
R393-R398 | (f}) Other expenses | 6 | - | standalone twin R049-R054; FY27 current columns equal twin
R399-R404 | Total Expenses (IV) | 6 | - | standalone twin R055-R060; FY27 current columns equal twin; prior-year columns include Valens Technologies (note 7); not comparable
R405-R410 | V Profit before exceptional items and tax (lll -IV) | 6 | - | standalone twin R061-R066; FY27 current columns equal twin
R411-R416 | VI Exceptional items | 6 | ZERO_STANDING(5 of 6) | standalone twin R067-R072; FY27 current columns equal twin
R417-R422 | VII Profit after exceptional items but before tax (V+VI) | 6 | - | standalone twin R073-R078; FY27 current columns equal twin
R423-R428 | (l} Current Tax | 6 | - | standalone twin R079-R084; FY27 current columns equal twin
R429-R434 | (Il) Deferred Tax | 6 | - | standalone twin R085-R090; FY27 current columns equal twin
R435-R440 | IX Profit for the period from continuing operations (VII | 6 | - | standalone twin R091-R096; FY27 current columns equal twin
R441-R446 | X Profit from discontinued operations | 6 | ZERO_STANDING(all 6) | standalone twin R097-R102; FY27 current columns equal twin
R447-R452 | XI Tax expense of discontinued operations | 6 | ZERO_STANDING(all 6) | standalone twin R103-R108; FY27 current columns equal twin
R453-R458 | XII Profit from discontinued operations (after tax) | 6 | ZERO_STANDING(all 6) | standalone twin R109-R114; FY27 current columns equal twin
R459-R464 | XIII Profit for the period (IX + XII) | 6 | - | standalone twin R115-R120; FY27 current columns equal twin
R465-R470 | A. (I) Items that will not be reclassified to profit or loss | 6 | - | standalone twin R121-R126; FY27 current columns equal twin
R471-R476 | (Jl) Income tax relating to items that will not be | 6 | - | standalone twin R127-R132; FY27 current columns equal twin
R477-R482 | B. (I) Items that will be reclassified to profit or loss | 6 | ZERO_STANDING(all 6) | standalone twin R133-R138; FY27 current columns equal twin
R483-R488 | (II) Income tax relating to items that will be | 6 | ZERO_STANDING(all 6) | standalone twin R139-R144; FY27 current columns equal twin
R489-R494 | Total other comprehensive income /(Loss) ( XIV) | 6 | - | standalone twin R145-R150; FY27 current columns equal twin
R495-R500 | XV Total Comprehensive Income ( Comprising Profit and | 6 | - | standalone twin R151-R156; FY27 current columns equal twin
R501-R506 | XVI Paid-up Equity Share Capital (Face Value Rs. 2 per share | 6 | - | standalone twin R157-R162; FY27 current columns equal twin
R507-R512 | (1) Basic | 6 | - | standalone twin R163-R168; FY27 current columns equal twin
R513-R518 | (2) Diluted | 6 | - | standalone twin R169-R174; FY27 current columns equal twin
R519-R524 | (1) Basic | 6 | ZERO_STANDING(all 6) | standalone twin R175-R180; FY27 current columns equal twin
R525-R530 | (2) Diluted | 6 | ZERO_STANDING(all 6) | standalone twin R181-R186; FY27 current columns equal twin
R531-R536 | (1) Basic | 6 | - | standalone twin R187-R192; FY27 current columns equal twin
R537-R542 | (2) Diluted | 6 | - | standalone twin R193-R198; FY27 current columns equal twin
R878 | Other Equity excluding revaluation Reserve | 1 | - | standalone twin R877; FY27 current columns equal twin; OTHER EQUITY ex-revaluation reserve, FY26 column only; duplicates BS Other Equity 31.03.2026 (R240/R584)

### Consolidated balance sheet (p10)  | verification: IMAGE-CHECKED (page image)

ROW_IDs | line item (label only) | n_vals | A2 flags | cross-ref / materiality note
---|---|---|---|---
R543-R544 | (a) Property, Plant and Equipment | 2 | - | standalone twin R199-R200; FY27 current columns equal twin
R545-R546 | (b) Capital work-in-progress | 2 | ZERO_STANDING(1 of 2) | standalone twin R201-R202; FY27 current columns equal twin
R547-R548 | (c) Right of use assets | 2 | - | standalone twin R203-R204; FY27 current columns equal twin
R549-R550 | (d) Other Intangible Assets | 2 | - | standalone twin R205-R206; FY27 current columns equal twin
R551-R552 | (i) Investments | 2 | ZERO_STANDING(all 2) | standalone twin R207-R208; FY27 current columns equal twin
R553-R554 | (ii) Loans | 2 | - | standalone twin R209-R210; FY27 current columns equal twin
R555-R556 | (iii) Others Non-Current Financial Assets | 2 | - | standalone twin R211-R212; FY27 current columns equal twin
R557-R558 | (f) Other Non-Current Assets | 2 | - | standalone twin R213-R214; FY27 current columns equal twin
R559-R560 | Total Non-Current Assets | 2 | - | standalone twin R215-R216; FY27 current columns equal twin
R561-R562 | (a) Inventories | 2 | - | standalone twin R217-R218; FY27 current columns equal twin
R563-R564 | (i) Investments | 2 | ZERO_STANDING(1 of 2) | standalone twin R219-R220; FY27 current columns equal twin
R565-R566 | (ii) Trade receivables | 2 | - | standalone twin R221-R222; FY27 current columns equal twin
R567-R568 | (iii) Cash and cash equivalents | 2 | - | standalone twin R223-R224; FY27 current columns equal twin
R569-R570 | (iv) Bank balances other than (iii) above | 2 | - | standalone twin R225-R226; FY27 current columns equal twin
R571-R572 | (v) Loans | 2 | - | standalone twin R227-R228; FY27 current columns equal twin
R573-R574 | (vi) Other Current Financial Assets | 2 | - | standalone twin R229-R230; FY27 current columns equal twin
R575-R576 | (c) Other Current Assets | 2 | - | standalone twin R231-R232; FY27 current columns equal twin
R577-R578 | Total Current Assets | 2 | - | standalone twin R233-R234; FY27 current columns equal twin
R579-R580 | Total Assets | 2 | - | standalone twin R235-R236; FY27 current columns equal twin
R581-R582 | (a) Equity Share Capital | 2 | - | standalone twin R237-R238; FY27 current columns equal twin
R583-R584 | (b) Other Equity | 2 | - | standalone twin R239-R240; FY27 current columns equal twin
R585-R586 | Total Equity | 2 | - | standalone twin R241-R242; FY27 current columns equal twin
R587-R588 | (i) Borrowings | 2 | - | standalone twin R243-R244; FY27 current columns equal twin
R589-R590 | (ii) Lease Liabilities | 2 | - | standalone twin R245-R246; FY27 current columns equal twin
R591-R592 | (b) Provisions | 2 | - | standalone twin R247-R248; FY27 current columns equal twin
R593-R594 | (c) Deferred Tax Liabilities (Net) | 2 | - | standalone twin R249-R250; FY27 current columns equal twin
R595-R596 | Total Non-Current Liabilities | 2 | - | standalone twin R251-R252; FY27 current columns equal twin
R597-R598 | (i) Borrowings | 2 | - | standalone twin R253-R254; FY27 current columns equal twin
R599-R600 | (ii) Lease Liabilities | 2 | - | standalone twin R255-R256; FY27 current columns equal twin
R601-R602 | Total outstanding dues of Micro Enterprises and | 2 | - | standalone twin R257-R258; FY27 current columns equal twin
R603-R604 | Total outstanding dues of creditors other than | 2 | - | standalone twin R259-R260; FY27 current columns equal twin
R605-R606 | (iv) Other Current Financial Liabilities | 2 | - | standalone twin R261-R262; FY27 current columns equal twin
R607-R608 | (b) Other Current Liabilities | 2 | - | standalone twin R263-R264; FY27 current columns equal twin
R609-R610 | (c) Provisions | 2 | - | standalone twin R265-R266; FY27 current columns equal twin
R611-R612 | (d) Current Tax Liability (Net) | 2 | - | standalone twin R267-R268; FY27 current columns equal twin
R613-R614 | Total Current Liabilities | 2 | - | standalone twin R269-R270; FY27 current columns equal twin
R615-R616 | Total Equity and Liabilities | 2 | - | standalone twin R271-R272; FY27 current columns equal twin

### Consolidated cash flow (p11)  | verification: IMAGE-CHECKED (page image)

ROW_IDs | line item (label only) | n_vals | A2 flags | cross-ref / materiality note
---|---|---|---|---
R617-R618 | Net Profit before taxation | 2 | - | standalone twin R273-R274; FY27 current columns equal twin
R619-R620 | Depreciation and amortization expenses | 2 | - | standalone twin R275-R276; FY27 current columns equal twin
R621-R622 | Interest Expenses/ Finance Cost | 2 | - | standalone twin R277-R278; FY27 current columns equal twin
R623-R624 | Interest on lease liability | 2 | - | standalone twin R279-R280; FY27 current columns equal twin
R625-R626 | Reversal of lease rent liability | 2 | - | standalone twin R281-R282; FY27 current columns equal twin
R627-R628 | Unrealised Exchange (Gain)/Loss | 2 | - | standalone twin R283-R284; FY27 current columns equal twin
R629-R630 | Profit on sales of Mutual Funds | 2 | - | standalone twin R285-R286; FY27 current columns equal twin
R631-R632 | (Profit) /Loss on sale of Property, plant & equipments (net) | 2 | ZERO_STANDING(1 of 2) | standalone twin R287-R288; FY27 current columns equal twin
R633-R634 | interest Income | 2 | - | standalone twin R289-R290; FY27 current columns equal twin
R635-R636 | Net Gain on Derivatives | 2 | - | standalone twin R291-R292; FY27 current columns equal twin
R637-R638 | Provision for Doubtful debts/ Written back | 2 | - | standalone twin R293-R294; FY27 current columns equal twin
R639-R640 | Employees share based payment expenses | 2 | - | standalone twin R295-R296; FY27 current columns equal twin
R641-R642 | Operating Profit before working capital changes | 2 | - | standalone twin R297-R298; FY27 current columns equal twin
R643-R644 | Decrease / (Increase) in Trade Receivables | 2 | - | standalone twin R299-R300; FY27 current columns equal twin
R645-R646 | Decrease / (Increase) in Loans & Advances | 2 | - | standalone twin R301-R302; FY27 current columns equal twin
R647-R648 | Decrease / (Increase) in Inventories | 2 | - | standalone twin R303-R304; FY27 current columns equal twin
R649-R650 | Decrease / (Increase) in Other financial and non financial A | 2 | - | standalone twin R305-R306; FY27 current columns equal twin
R651-R652 | (Decrease) / Increase in Trade Payables | 2 | - | standalone twin R307-R308; FY27 current columns equal twin
R653-R654 | (Decrease) / Increase in Other Liabilities & Provisions | 2 | - | standalone twin R309-R310; FY27 current columns equal twin
R655-R656 | Cash generated from operation | 2 | - | standalone twin R311-R312; FY27 current columns equal twin
R657-R658 | Exceptional items | 2 | ZERO_STANDING(all 2) | standalone twin R313-R314; FY27 current columns equal twin
R659-R660 | Income Tax Paid/ Refund/ Provisions (Net) | 2 | - | standalone twin R315-R316; FY27 current columns equal twin
R661-R662 | NET CASH FROM OPERATING ACTIVITIES (A) | 2 | - | standalone twin R317-R318; FY27 current columns equal twin
R663-R664 | Purchase of Property plant & equipments including Capital Wo | 2 | - | standalone twin R319-R320; FY27 current columns equal twin
R665-R666 | Interest Received | 2 | - | standalone twin R323-R324; FY27 current columns equal twin
R667-R668 | Sale of Investments (Mutual Fund) | 2 | - | standalone twin R325-R326; FY27 current columns equal twin
R669-R670 | Purchase of Investments (Mutual Fund) | 2 | - | standalone twin R327-R328; FY27 current columns equal twin
R671-R672 | NET CASH FROM INVESTING ACTIVITIES (B) | 2 | - | standalone twin R329-R330; FY27 current columns equal twin
R673-R674 | Interest Expenses/ Finance Cost | 2 | - | standalone twin R331-R332; FY27 current columns equal twin
R675-R676 | Increase/(Decrease) in Borrowings from banks / ARC /NBFC ( n | 2 | - | standalone twin R333-R334; FY27 current columns equal twin
R677-R678 | NET CASH FROM FINANCING ACTIVITIES (C) | 2 | - | standalone twin R337-R338; FY27 current columns equal twin
R679-R680 | NET INCREASE/(DECREASE) IN CASH & CASH EQUIVALENTS | 2 | - | standalone twin R339-R340; FY27 current columns equal twin
R681-R682 | CASH AND CASH EQUIVALENTS AT BEGINNING OF THE YEAR | 2 | - | standalone twin R341-R342; FY27 current columns equal twin
R683-R684 | CASH AND CASH EQUIVALENTS AT END OF THE PERIOD | 2 | - | standalone twin R343-R344; FY27 current columns equal twin

### Segment annexure A (p13)  | verification: IMAGE-CHECKED (page image)

ROW_IDs | line item (label only) | n_vals | A2 flags | cross-ref / materiality note
---|---|---|---|---
R685-R690 | Wire and Cables | 6 | - | segment total ties to consolidated P&L line (not tested by A2)
R691-R696 | Pipes | 6 | ZERO_STANDING(3 of 6); SEGMENT_NIL_FY27 (populated in FY26 columns) | segment total ties to consolidated P&L line (not tested by A2)
R697-R702 | Gross Revenue | 6 | - | segment total ties to consolidated P&L line (not tested by A2)
R703-R708 | Less Inter-segment Revenue | 6 | ZERO_STANDING(3 of 6) | segment total ties to consolidated P&L line (not tested by A2)
R709-R714 | Total Revenue from Operations | 6 | - | segment total ties to consolidated P&L line (not tested by A2)
R715-R720 | Wire and Cables | 6 | - | segment total ties to consolidated P&L line (not tested by A2)
R721-R726 | Pipes | 6 | ZERO_STANDING(3 of 6); SEGMENT_NIL_FY27 (populated in FY26 columns) | segment total ties to consolidated P&L line (not tested by A2)
R727-R732 | Total Profit (Loss) before Finance cost, exceptional items, | 6 | - | segment total ties to consolidated P&L line (not tested by A2)
R733-R738 | Finance cost | 6 | - | segment total ties to consolidated P&L line (not tested by A2)
R739-R744 | Unallocated (income) / expenses (net) | 6 | - | segment total ties to consolidated P&L line (not tested by A2)
R745-R750 | Profit /(loss) before tax and Exceptional Item | 6 | - | segment total ties to consolidated P&L line (not tested by A2)
R751-R756 | Add : Exceptional items - income /(Expenses ) | 6 | ZERO_STANDING(5 of 6) | segment total ties to consolidated P&L line (not tested by A2)
R757-R762 | Profit /(loss) before tax | 6 | - | segment total ties to consolidated P&L line (not tested by A2)
R763-R768 | Tax expenses | 6 | - | segment total ties to consolidated P&L line (not tested by A2)
R769-R774 | Profit /(loss) After tax | 6 | - | segment total ties to consolidated P&L line (not tested by A2)
R775-R780 | Wire and Cables | 6 | - | segment total ties to consolidated P&L line (not tested by A2)
R781-R786 | Pipes | 6 | ZERO_STANDING(4 of 6); SEGMENT_NIL_FY27 (populated in FY26 columns) | segment total ties to consolidated P&L line (not tested by A2)
R787-R792 | Unallocated | 6 | ZERO_STANDING(all 6) | segment total ties to consolidated P&L line (not tested by A2)
R793-R798 | Total Segment Assets | 6 | - | segment total ties to consolidated P&L line (not tested by A2)
R799-R804 | Wire and Cables | 6 | - | segment total ties to consolidated P&L line (not tested by A2)
R805-R810 | Pipes | 6 | ZERO_STANDING(4 of 6); SEGMENT_NIL_FY27 (populated in FY26 columns) | segment total ties to consolidated P&L line (not tested by A2)
R811-R816 | Unallocated | 6 | ZERO_STANDING(4 of 6) | segment total ties to consolidated P&L line (not tested by A2)
R817-R822 | Total Segment Liabilities | 6 | - | segment total ties to consolidated P&L line (not tested by A2)
### 2b. MISSING_FROM_STRUCTURED (consolidated cash flow, p11, IMAGE-CHECKED page; fulltext line numbers)
ROW_IDs | line item | A2 flags | claim text (only place A2 writes it)
---|---|---|---
M001 | line 604 Sale of Property plant & equipments, half year 30.09.2026 | MISSING_FROM_STRUCTURED | 1.74
M002 | line 604 same, half year 30.09.2025 | MISSING_FROM_STRUCTURED; ZERO_STANDING | fulltext shows "=" (OCR), read as nil; standalone twin R322 is nil; confirm vs image
M003 | line 612 Proceeds from Issue of Equity Share upon conversion of Equity share warrants (net of issue expenses), half year 30.09.2026 | MISSING_FROM_STRUCTURED | 97.67 (equals standalone R335)
M004 | line 612 same, half year 30.09.2025 | MISSING_FROM_STRUCTURED; ZERO_STANDING | fulltext shows "=" (OCR), read as nil; standalone R336 is nil; confirm vs image
Loop back to A1: the consolidated financing inflow 97.67 and the PPE sale 1.74 are absent from the structured file. Both sit inside subtotals that are present (R661, R671, R677).
Line item total: 235 structured + 2 missing = 237.

## 3. AGENDA ITEMS / BOARD OUTCOME LETTER (p1, RAW OCR)
ROW_IDs | item | A2 flags | note
---|---|---|---
R913, R939 | Item a) approval of standalone and consolidated un-audited results, quarter and half year ended 30 Sep 2026 | - | only item besides item b
R914, R940 | Item b) limited review report of Statutory Auditors on the same results | - |
R912, R911 | Board meeting date Monday 26 Oct 2026; letter date 26.10.2026 | - |
R825 | Meeting start 02.00 p.m. | - |
R826 | Meeting end 3.40 p.m. | - | duration 100 minutes, from the two times
R824, R882, R879, R823, R880, R881 | Regulation 30 and 33 SEBI LODR; NSE symbol; BSE code; addressees BSE and NSE | - |
R908, R885 | Upload commitment to company website | FORWARD |
Not in the letter: AR approval, AGM notice, record date, dividend, director appointment, auditor change, scrutinizer, ESOP grant, capital-raising enabling resolution. The preferential issue and ESOP allotments appear only in notes 4/5 (SA) and 5/6 (CO).

## 4. AUDITOR PARAGRAPHS
ROW_IDs | para | A2 flags | note
---|---|---|---
R886, R918, R914, R889 | SA review report para 1 (scope, Reg 33) p2 | - | RAW_OCR; opinion type: limited review, no audit opinion
R832, R833 | SA para 2 (management responsibility; Ind AS 34, s133, Rule 3) | - |
R831, R942 | SA para 3 (SRE 2410, moderate assurance, no audit opinion) | - |
R943 | SA para 4 (conclusion unmodified) | - | no Emphasis of Matter, Other Matters or Going Concern language in SA report
R887, R888, R828, R829, R917 | SA signature block: FRN 000468N, M.No.080691, dated 26.10.2026 | - |
R830, R941 | SA UDIN (OCR "26O806GIIABTTN5 (83"; structured reading 26080691IIABTTN583) | FOOTNOTE_UNRESOLVED | RAW_OCR; needs image check
R896, R974, R857 | CO review report para 1 and 3 (scope, SRE 2410, moderate assurance) p7 | - | RAW_OCR
R858, R899 | CO unnumbered paragraph: SEBI circular procedures under Reg 33(8) | - |
R897, R898 | CO para 4 entity list reviewed: Paramount Holdings Limited, AEI Power Cables Limited | - |
R851-R856, R973 | CO para 5 (2 subsidiaries not reviewed by their auditors, management-furnished; total assets, revenue, PAT, TCI, net cash flows all NIL) | ZERO_STANDING x5 | the only Other Matter style paragraph
R975, R976 | CO para 5 close (not material to group; conclusion not modified in respect of above matter) | - | opinion stays unmodified
R977 | CO para 6 (conclusion unmodified) p8 | - |
R859, R860, R900, R932, R861 | CO signature block: FRN 000468N, M.No.080691, dated 26.10.2026; UDIN printed as "DIN: 26080691VFYDBU8230" | FOOTNOTE_UNRESOLVED | RAW_OCR; label reads DIN; image check needed
Entity list reviewed: parent plus two subsidiaries; Valens Technologies (divested) not in the list. No Going Concern language in either report.

## 5. ENTITIES (all 29 ENTITY rows; consolidation list cross-check)
ROW_IDs | entity | A2 flags | note
---|---|---|---
R897 | Paramount Holdings Limited (subsidiary) | - | prior-quarter list unavailable; no diff run
R898 | AEI Power Cables Limited (subsidiary) | - | same
R902 | Valens Technologies Private Limited (divested 6 Nov 2025) | ENTITY_CHANGE | in FY26 comparative columns only
R903, R904, R906, R907 | Wires & Cables segment, Pipes segment | - | Pipes nil in FY27 columns
R883, R893, R894 | Paramount Communications Limited (issuer on letter, SA, CO) | - |
R879, R880, R881, R882, R885, R899 | NSE symbol, BSE, NSE, SEBI LODR, website, SEBI | - | exchange and regulator references
R884, R892, R905 | Rashi Goel (CS), Sanjay Aggarwal Chairman and CEO DIN 00001788 (signs SA and CO) | - | section 6
R886, R887, R888, R889, R896, R900 | auditor firm, FRN, partner, ICAI | - | section 4
R890 | non-promoter allottees of preferential equity (unnamed) | - | allottee names NOT DISCLOSED in the filing
R891, R901 | Paramount Communications - Stock Incentive Plan | - |
R895 | registered address, New Delhi | - | no director-profile annexure in this filing

## 6. SIGNATURE BLOCKS
ROW_IDs | signatory | A2 flags | note
---|---|---|---
R884, R915 | Rashi Goel, CS and Compliance Officer; digital signature 2026.10.26 15:52:13 +05:30 | - | 12 minutes after the meeting concluded (3.40 p.m.); no early-signature flag
R892, R924 | Sanjay Aggarwal, Chairman & CEO, DIN 00001788, standalone results 26.10.2026 p6 | - | RAW_OCR
R905, R938 | Sanjay Aggarwal, consolidated results 26.10.2026 p12 | - |
R900, R917, R932 | Pawan Bholusaria, Partner, both review reports 26.10.2026 | - | section 4
Only annexure in the filing: Annexure A segment table (R971). No director-profile or AR annexure.

## 7. DATES
R911-R938 (28 DATE rows) | period, meeting, allotment, EGM, divestment, signing dates | - | R916 1994 is the CIN incorporation year; R937 divestment 6 Nov 2025; R920/R934 EGM 06.06.2026; R921/R922/R935 allotments 01.07.2026; R923/R936 ESOP 14.07.2026

## 8. FORWARD-LOOKING ITEMS
R908 | upload to website | FORWARD |
R909, R910 | 72,00,000 warrants, 75% balance on conversion pending | FORWARD; RESTATED | conversion timing not stated

## 9. QUALIFIERS (all 51 QUALIFIER rows)
ROW_IDs | group | A2 flags | note
---|---|---|---
R939, R940 | results unaudited; limited review not audit | - |
R941 | UDIN OCR illegible | FOOTNOTE_UNRESOLVED |
R942, R943, R973, R974, R975, R976, R977 | review scope and conclusion qualifiers | - | section 4
R944, R945, R946, R950, R951, R978, R979, R980, R981, R984, R985, R986 | note-text qualifiers | - | mapped in section 1
R947, R952, R955, R960, R962, R966, R969, R970 | unit statements (Rs Crores) | - |
R948, R982, R949, R983 | use-of-proceeds footnote and no-deviation statement | RESTATED | section 1
R953, R956 | EPS not annualised for quarters | - |
R954, R957, R961, R963, R972 | audit status of columns (periods unaudited; 31.03.2026 audited) | - |
R958, R959 | face value Rs 2 per share | - |
R964, R965, R967, R968 | cash flow notes | - | section 1
R971 | Annexure-A label | - |
R987, R988, R989 | segment elimination and segment result definitions | - |

## 10. OTHER NUMERIC FACTS (non-table NUMBER rows)
ROW_IDs | group | A2 flags | note
---|---|---|---
R823, R827, R849 | BSE code, CIN (letter and p3) | - |
R850 | company phone (OCR) | - | RAW_OCR
R834-R848, R863-R876 | preferential issue, warrant, use-of-proceeds, ESOP numbers (SA and CO copies) | RESTATED | section 1
R828-R833, R857-R861 | auditor registration, SRE, Ind AS references, UDIN | - | section 4
R851-R856 | subsidiaries not reviewed (NIL) | ZERO_STANDING | section 4
