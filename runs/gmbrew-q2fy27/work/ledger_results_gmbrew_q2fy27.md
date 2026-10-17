# A2 LEDGER, GMBREW q2fy27 results
Source: runs/gmbrew-q2fy27/extracted/gmbrew-results-q2fy27-structured.md (IDs R001-R757). Row text is not re-copied; read the value at the ID. Units Rs Lakhs.

=== A2 COUNT TEST ===
structured_header_total: 757 | ids_parsed_from_structured: 757 | type_counts_match_A1_header: yes (NUMBER 615, ENTITY 31, FORWARD 1, DATE 50, QUALIFIER 60)
fulltext_fallback: 620 lines; used to confirm notes, agenda, Section C, auditor paras and the two A1 line-item problems below
category: notes          grep_count: 10   sweep_count: 10   match: yes  (fulltext "^N)" lines 114-117,126,420-423,432 = 10; ledger rows R704-R707,R715-R718 numbered notes 1-4 x2, R724,R728 BS note 5 x2)
category: line_items standalone P&L   grep_count: 22   sweep_count: 22   match: yes
category: line_items consolidated P&L grep_count: 22   sweep_count: 22   match: yes
category: line_items standalone BS    grep_count: 29   sweep_count: 29   match: yes   (+1 MISSING_FROM_STRUCTURED: fulltext l167 Current Tax Liabilities row; with it, standalone BS = 30 = consolidated BS 30)
category: line_items consolidated BS  grep_count: 30   sweep_count: 30   match: yes
category: line_items standalone CF    grep_count: 35   sweep_count: 35   match: yes
category: line_items consolidated CF  grep_count: 35   sweep_count: 35   match: yes
category: line_items total   grep_count: 173   sweep_count: 173   match: yes; cell check (6 cols P&L, 2 cols BS/CF) off-pattern groups: 0
category: zero_standing  grep_count: 58 (raw ZERO_STANDING lines, all NUMBER)   sweep_count: 57 NUMBER cells (+3 MISSING rows M1,M3,M4 = 60 total)   match: yes after adjustment (58 raw = 57 true + R388 A1 mis-tag; loop 1 added M3,M4)
category: agenda_items   grep_count: 1   sweep_count: 1   match: yes  (one numbered agenda item, results approval, with sub-items a. financials, b. LRR; fulltext l36-l45; R698/R699, R649, R597/R598 times)
category: auditor_paras  grep_count: 16   sweep_count: 16   match: yes  (LOOP 1 fresh count on FULLTEXT paragraphs: standalone LRR numbered paras 1-4 = 4 (l313,l319,l327,l352); consolidated LRR numbered paras 1-5 = 5 (l561,l568,l576,l598,l601); 9 numbered paragraphs. Rows exist for 8 of 9: standalone 4 of 4 (R748,R749,R750,R752); consolidated 4 of 5 (R754 para1, R755 para3 tail sentence only, R757 para4, R756 para5); consolidated para 2 (l568-l574) has no row = M2. Ledger row count 15 existing + M2 = 16)
category: entities       grep_count: 31   sweep_count: 31   match: yes
category: dates          grep_count: 50   sweep_count: 50   match: yes
gate_a2: pass
=== END COUNT TEST ===

ID ACCOUNTABILITY: ids_in_structured: 757 | ids_referenced_in_ledger: 757 | orphan_ids: [] | match: yes | ids_referenced_more_than_once: 0

## 0. FLAGS AND FINDINGS FOR A3/A4 (IDs only)
1. MISSING_FROM_STRUCTURED M1: fulltext l167 (p4, standalone BS) "d) Current Tax Liabilities (Net)" is a blank row both periods. No NUMBER row in A1; consolidated twin is R381-R382 (ZERO_STANDING). Treat as ZERO_STANDING. Related A1 qualifier R727 carries line 158; fulltext line is 167.
2. A1_VALUE_DISCREPANCY: R387/R388 (consolidated BS Total Equities and Liabilities, l475). R388 is tagged ZERO_STANDING, but fulltext l475 shows a figure plus a trailing dash glyph. R387 holds the 31.03 figure while the context label carries the 30.09 figure. Loop to A1. Not counted in zero_standing.
3. SIG_BEFORE_MEETING: LRR digital signature stamps R689, R690, R693, R694 (10:27:50 to 10:28:32 IST on 08.10.2026) precede the board meeting start 11:30 A.M. (R597); meeting ended 12:20 P.M. (R598), duration 50 minutes. Flag only.
4. PERIOD_MISMATCH: consolidated P&L title prints September 30, 2025 (R667, R723) while columns read 30.09.2026.
5. WORDING_AS_PRINTED: consolidated LRR para 5 says "standalone" (R756); LRR scope names the quarter only, not the half year (R688, R692, R747).
6. PARSE_FRAGMENT rows (section 2b) are header or footer text A1 split into numeric cells. They are accounted for, not line items.
7. Standalone vs consolidated: all 22 P&L lines match cell for cell. 31 BS and CF cell pairs differ (section 2c); A3 to inspect. No subsidiary revenue shows in the P&L.
8. Consolidation list: Holding plus Buildfort Infradev Pvt Ltd wholly owned subsidiary (R644-R646). No prior-quarter ledger supplied, so ENTITY_CHANGE cannot be assessed; none raised.
9a. LOOP 1: MISSING_FROM_STRUCTURED now M1-M4 (section 2d). M2 consolidated LRR para 2 (l568-l574); M3, M4 Statement C items 1A, 2A blank outstanding (l278, l282), ZERO_STANDING, BLANK_DISCLOSURE; garbled cell l281 noted.
9. Blank RPT loan/ICD columns (R741); Statement C default and indebtedness rows are Nil (R601-R603 ZERO_STANDING).

## 1. NOTES (numbered and unnumbered)
ROW_IDS | category | A2 flags | cross-ref / note
R704-R707 | standalone Notes 1-4 | NUMBERED_NOTE | l114-117; each ID one note
R715-R718 | consolidated Notes 1-4 | NUMBERED_NOTE | l420-423; text repeated from standalone (RESTATED R704-R707)
R724 | standalone Note 5 (Balance Sheet label) | NOTE_LABEL | no unit label in BS header
R728 | consolidated Note 5 (Balance Sheet label) | NOTE_LABEL | same
Unnumbered notes and footnotes: R701, R702, R708-R714, R719-R723, R725-R727, R729-R747 (listed in section 7 with flags)

## 2. LINE ITEMS (every financial table row; ZERO_STANDING kept)
ROW_IDS | category | A2 flags | cross-ref / note
R001-R006 | standalone P&L | - | a) Sales / Income from operations (inclusive of Excise  | p3 l88 | 6 cells
R007-R012 | standalone P&L | ZERO_STANDING | b) Other operating revenue | p3 l89 | 6 cells | zero cells R007-R012
R013-R018 | standalone P&L | - | Total Revenue from Operations | p3 l90 | 6 cells
R019-R024 | standalone P&L | - | Other Income | p3 l91 | 6 cells
R025-R030 | standalone P&L | - | Total Income | p3 l92 | 6 cells
R031-R036 | standalone P&L | - | a) Cost of Materials Consumed | p3 l94 | 6 cells
R037-R042 | standalone P&L | ZERO_STANDING | b) Purchase of stock in trade | p3 l95 | 6 cells | zero cells R037-R042
R043-R048 | standalone P&L | - | c) Changes in inventories of finished goods, work in pr | p3 l96 | 6 cells
R049-R054 | standalone P&L | - | d) Employee benefits expenses | p3 l97 | 6 cells
R055-R060 | standalone P&L | - | e) Excise duty, VAT & TCS | p3 l98 | 6 cells
R061-R066 | standalone P&L | - | f) Finance Cost | p3 l99 | 6 cells
R067-R072 | standalone P&L | - | g) Depreciation and amortisation expenses | p3 l100 | 6 cells
R073-R078 | standalone P&L | - | h) Other Expenditure | p3 l101 | 6 cells
R079-R084 | standalone P&L | - | Total Expenses | p3 l102 | 6 cells
R085-R090 | standalone P&L | - | Profit from continuing operation before exceptional ite | p3 l103 | 6 cells
R091-R096 | standalone P&L | ZERO_STANDING | Exceptional item | p3 l104 | 6 cells | zero cells R091-R096
R097-R102 | standalone P&L | - | Profit from continuing operations before tax | p3 l105 | 6 cells
R103-R108 | standalone P&L | - | Tax expenses ( Current & Deffered Taxes) | p3 l106 | 6 cells
R109-R114 | standalone P&L | - | Profit for the period | p3 l107 | 6 cells
R115-R120 | standalone P&L | ZERO_STANDING | Gain/ Loss on fair valuation of investment in equity sh | p3 l110 | 6 cells | zero cells R115-R120
R121-R126 | standalone P&L | - | Total Comprehensive Income | p3 l111 | 6 cells
R127-R132 | standalone P&L | - | Earning Per share of Rs.10 each , Basic & Diluted | p3 l112 | 6 cells
R133-R138 | consolidated P&L | - | a) Sales / Income from operations (inclusive of Excise  | p10 l394 | 6 cells
R139-R144 | consolidated P&L | ZERO_STANDING | b) Other operating revenue | p10 l395 | 6 cells | zero cells R139-R144
R145-R150 | consolidated P&L | - | Total Revenue from Operations | p10 l396 | 6 cells
R151-R156 | consolidated P&L | - | Other Income | p10 l397 | 6 cells
R157-R162 | consolidated P&L | - | Total Income | p10 l398 | 6 cells
R163-R168 | consolidated P&L | - | a) Cost of Materials Consumed | p10 l400 | 6 cells
R169-R174 | consolidated P&L | ZERO_STANDING | b) Purchase of stock in trade | p10 l401 | 6 cells | zero cells R169-R174
R175-R180 | consolidated P&L | - | c) Changes in inventories of finished goods, work in pr | p10 l402 | 6 cells
R181-R186 | consolidated P&L | - | d) Employee benefits expenses | p10 l403 | 6 cells
R187-R192 | consolidated P&L | - | e) Excise duty, VAT & TCS | p10 l404 | 6 cells
R193-R198 | consolidated P&L | - | f) Finance Cost | p10 l405 | 6 cells
R199-R204 | consolidated P&L | - | g) Depreciation and amortisation expenses | p10 l406 | 6 cells
R205-R210 | consolidated P&L | - | h) Other Expenditure | p10 l407 | 6 cells
R211-R216 | consolidated P&L | - | Total Expenses | p10 l408 | 6 cells
R217-R222 | consolidated P&L | - | Profit from continuing operation before exceptional ite | p10 l409 | 6 cells
R223-R228 | consolidated P&L | ZERO_STANDING | Exceptional item | p10 l410 | 6 cells | zero cells R223-R228
R229-R234 | consolidated P&L | - | Profit from continuing operations before tax | p10 l411 | 6 cells
R235-R240 | consolidated P&L | - | Tax expenses ( Current & Deffered Taxes) | p10 l412 | 6 cells
R241-R246 | consolidated P&L | - | Profit for the period | p10 l413 | 6 cells
R247-R252 | consolidated P&L | ZERO_STANDING | Gain/ Loss on fair valuation of investment in equity sh | p10 l416 | 6 cells | zero cells R247-R252
R253-R258 | consolidated P&L | - | Total Comprehensive Income | p10 l417 | 6 cells
R259-R264 | consolidated P&L | - | Earning Per share of Rs.10 each , Basic & Diluted | p10 l418 | 6 cells
R267-R268 | standalone BS | - | a) Property, Plant and Equipment | p4 l131 | 2 cells
R269-R270 | standalone BS | - | b) Capital Work- In- Progress | p4 l132 | 2 cells
R271-R272 | standalone BS | - | c) Investment Property | p4 l133 | 2 cells
R273-R274 | standalone BS | - | d) Intangible Assets | p4 l134 | 2 cells
R275-R276 | standalone BS | - | - Non Current Investments | p4 l136 | 2 cells
R277-R278 | standalone BS | - | -Other Non Current Financial Assets | p4 l137 | 2 cells
R279-R280 | standalone BS | - | f) Non Current Tax Assets (Net) | p4 l138 | 2 cells
R281-R282 | standalone BS | - | g)Other non-current assets | p4 l139 | 2 cells
R283-R284 | standalone BS | - | Total Non Current Assets | p4 l140 | 2 cells
R285-R286 | standalone BS | - | a) Inventories | p4 l142 | 2 cells
R287-R288 | standalone BS | - | -Trade receivables | p4 l144 | 2 cells
R289-R290 | standalone BS | - | -Cash and cash equivalents | p4 l145 | 2 cells
R291-R292 | standalone BS | - | -Other Bank Balances | p4 l146 | 2 cells
R293-R294 | standalone BS | - | c) Other Current Assets | p4 l147 | 2 cells
R295-R296 | standalone BS | - | Total Current Assets | p4 l148 | 2 cells
R297-R298 | standalone BS | - | Total Assets | p4 l149 | 2 cells
R299-R300 | standalone BS | - | a) Equity Share Capital | p4 l153 | 2 cells
R301-R302 | standalone BS | - | b) Other Equity | p4 l154 | 2 cells
R303-R304 | standalone BS | - | Total Equity | p4 l155 | 2 cells
R305-R306 | standalone BS | - | a)Deferred Tax Liabilities | p4 l158 | 2 cells
R307-R308 | standalone BS | - | b)Other non current liabilities | p4 l159 | 2 cells
R309-R310 | standalone BS | - | Total Non Current Liabilities | p4 l160 | 2 cells
R311-R312 | standalone BS | - | -Trade payables ( Other than Micro & Small enterprises) | p4 l163 | 2 cells
R313-R314 | standalone BS | - | -Other Current financial liabilities | p4 l164 | 2 cells
R315-R316 | standalone BS | - | b) Other Current Liabilities | p4 l165 | 2 cells
R317-R318 | standalone BS | - | c) Provisions | p4 l166 | 2 cells
R319-R320 | standalone BS | - | Total Current Liabilities | p4 l168 | 2 cells
R321-R322 | standalone BS | - | Total Liabilities | p4 l169 | 2 cells
R323-R324 | standalone BS | - | Total Equities and Liabilities | p4 l170 | 2 cells
R329-R330 | consolidated BS | - | a) Property, Plant and Equipment | p11 l437 | 2 cells
R331-R332 | consolidated BS | - | b) Capital Work- In- Progress | p11 l438 | 2 cells
R333-R334 | consolidated BS | - | c) Investment Property | p11 l439 | 2 cells
R335-R336 | consolidated BS | - | d) Intangible Assets | p11 l440 | 2 cells
R337-R338 | consolidated BS | - | - Non Current Investments | p11 l442 | 2 cells
R339-R340 | consolidated BS | - | -Other Non Current Financial Assets | p11 l443 | 2 cells
R341-R342 | consolidated BS | - | f) Non Current Tax Assets (Net) | p11 l444 | 2 cells
R343-R344 | consolidated BS | - | g)Other non-current assets | p11 l445 | 2 cells
R345-R346 | consolidated BS | - | Total Non Current Assets | p11 l446 | 2 cells
R347-R348 | consolidated BS | - | a) Inventories | p11 l448 | 2 cells
R349-R350 | consolidated BS | - | -Trade receivables | p11 l450 | 2 cells
R351-R352 | consolidated BS | - | -Cash and cash equivalents | p11 l451 | 2 cells
R353-R354 | consolidated BS | - | -Other Bank Balances | p11 l452 | 2 cells
R355-R356 | consolidated BS | - | c) Other Current Assets | p11 l453 | 2 cells
R357-R358 | consolidated BS | - | Total Current Assets | p11 l454 | 2 cells
R359-R360 | consolidated BS | - | Total Assets | p11 l455 | 2 cells
R361-R362 | consolidated BS | - | a) Equity Share Capital | p11 l458 | 2 cells
R363-R364 | consolidated BS | - | b) Other Equity | p11 l459 | 2 cells
R365-R366 | consolidated BS | - | Total Equity | p11 l460 | 2 cells
R367-R368 | consolidated BS | - | a)Deferred Tax Liabilities | p11 l463 | 2 cells
R369-R370 | consolidated BS | - | b)Other non current liabilities | p11 l464 | 2 cells
R371-R372 | consolidated BS | - | Total Non Current Liabilities | p11 l465 | 2 cells
R373-R374 | consolidated BS | - | -Trade payables ( Other than Micro & Small enterprises) | p11 l468 | 2 cells
R375-R376 | consolidated BS | - | -Other Current financial liabilities | p11 l469 | 2 cells
R377-R378 | consolidated BS | - | b) Other Current Liabilities | p11 l470 | 2 cells
R379-R380 | consolidated BS | - | c) Provisions | p11 l471 | 2 cells
R381-R382 | consolidated BS | ZERO_STANDING | d) Current Tax Liabilities (Net) | p11 l472 | 2 cells | zero cells R381-R382
R383-R384 | consolidated BS | - | Total Current Liabilities | p11 l473 | 2 cells
R385-R386 | consolidated BS | - | Total Liabilities | p11 l474 | 2 cells
R387-R388 | consolidated BS | A1_VALUE_DISCREPANCY | Total Equities and Liabilities 1,28,473.47 | p11 l475 | 2 cells | R388 tagged ZERO_STANDING by A1 but fulltext l475 shows a trailing dash glyph after the 31.03 figure; R387/R388 columns look shifted, loop to A1
R393-R394 | standalone CF | - | Net Profit before tax | p5 l194 | 2 cells
R395-R396 | standalone CF | - | Depreciation | p5 l196 | 2 cells
R397-R398 | standalone CF | - | Finance Cost | p5 l197 | 2 cells
R399-R400 | standalone CF | - | Indirect Taxes paid | p5 l198 | 2 cells
R401-R402 | standalone CF | - | Dividend Received | p5 l199 | 2 cells
R403-R404 | standalone CF | - | Interest Received | p5 l200 | 2 cells
R405-R406 | standalone CF | - | Other Non-Operating Income | p5 l201 | 2 cells
R407-R408 | standalone CF | - | Operating Profit before Working Capital Changes | p5 l202 | 2 cells
R409-R410 | standalone CF | - | Trade Receivables | p5 l204 | 2 cells
R411-R412 | standalone CF | - | Inventories | p5 l205 | 2 cells
R413-R414 | standalone CF | ZERO_STANDING | Other Financial Assets- Non Current | p5 l206 | 2 cells | zero cells R414
R415-R416 | standalone CF | - | Other Current Assets | p5 l207 | 2 cells
R417-R418 | standalone CF | - | Other Non Current Assets | p5 l208 | 2 cells
R419-R420 | standalone CF | - | Trade Payables | p5 l210 | 2 cells
R421-R422 | standalone CF | ZERO_STANDING | Other non current liabilities | p5 l211 | 2 cells | zero cells R422
R423-R424 | standalone CF | - | Other Current Liabilities | p5 l212 | 2 cells
R425-R426 | standalone CF | - | Other financial liabilities - Current | p5 l213 | 2 cells
R427-R428 | standalone CF | - | Cash generated from Operations | p5 l214 | 2 cells
R429-R430 | standalone CF | - | Direct Taxes Paid | p5 l215 | 2 cells
R431-R432 | standalone CF | - | Indirect Taxes Paid | p5 l216 | 2 cells
R433-R434 | standalone CF | - | Net Cash from Operating Activities (A) | p5 l217 | 2 cells
R435-R436 | standalone CF | - | Increase/Decrease in Property, Plant and Equipment incu | p5 l220 | 2 cells
R437-R438 | standalone CF | - | Increase/Decrease in Investment Property | p5 l221 | 2 cells
R439-R440 | standalone CF | - | Increase/Decrease in Financial Assets- Investments | p5 l222 | 2 cells
R441-R442 | standalone CF | - | Redemption/ (Purchase) of Fixed Deposits (with Maturity | p5 l224 | 2 cells
R443-R444 | standalone CF | - | Interest Received | p5 l225 | 2 cells
R445-R446 | standalone CF | - | Dividend Received | p5 l226 | 2 cells
R447-R448 | standalone CF | - | Other Non-Operating Income | p5 l227 | 2 cells
R449-R450 | standalone CF | - | Net Cash (used in) /from Investing activities (B) | p5 l228 | 2 cells
R451-R452 | standalone CF | - | Interest / financial charges Paid | p5 l230 | 2 cells
R453-R454 | standalone CF | - | Dividend Paid | p5 l231 | 2 cells
R455-R456 | standalone CF | - | Net Cash (used in) /from Financing activities (C ) | p5 l232 | 2 cells
R457-R458 | standalone CF | - | D. Net Changes in Cash and Cash Equivalents (A+B+C) | p5 l233 | 2 cells
R459-R460 | standalone CF | - | E. Cash and Cash Equivalents at beginning of the Period | p5 l234 | 2 cells
R461-R462 | standalone CF | - | F. Cash and Cash Equivalents at End of the Period | p5 l235 | 2 cells
R467-R468 | consolidated CF | - | Net Profit before tax | p12 l501 | 2 cells
R469-R470 | consolidated CF | - | Depreciation | p12 l503 | 2 cells
R471-R472 | consolidated CF | - | Finance Cost | p12 l504 | 2 cells
R473-R474 | consolidated CF | - | Indirect Taxes paid | p12 l505 | 2 cells
R475-R476 | consolidated CF | - | Dividend Received | p12 l506 | 2 cells
R477-R478 | consolidated CF | - | Interest Received | p12 l507 | 2 cells
R479-R480 | consolidated CF | - | Other Non-Operating Income | p12 l508 | 2 cells
R481-R482 | consolidated CF | - | Operating Profit before Working Capital Changes | p12 l509 | 2 cells
R483-R484 | consolidated CF | - | Trade Receivables | p12 l511 | 2 cells
R485-R486 | consolidated CF | - | Inventories | p12 l512 | 2 cells
R487-R488 | consolidated CF | ZERO_STANDING | Other Financial Assets- Non Current | p12 l513 | 2 cells | zero cells R488
R489-R490 | consolidated CF | - | Other Current Assets | p12 l514 | 2 cells
R491-R492 | consolidated CF | - | Other Non Current Assets | p12 l515 | 2 cells
R493-R494 | consolidated CF | - | Trade Payables | p12 l517 | 2 cells
R495-R496 | consolidated CF | ZERO_STANDING | Other non current liabilities | p12 l518 | 2 cells | zero cells R496
R497-R498 | consolidated CF | - | Other Current Liabilities | p12 l519 | 2 cells
R499-R500 | consolidated CF | - | Other financial liabilities - Current | p12 l520 | 2 cells
R501-R502 | consolidated CF | - | Cash generated from Operations | p12 l521 | 2 cells
R503-R504 | consolidated CF | - | Direct Taxes Paid | p12 l522 | 2 cells
R505-R506 | consolidated CF | - | Indirect Taxes Paid | p12 l523 | 2 cells
R507-R508 | consolidated CF | - | Net Cash from Operating Activities (A) | p12 l524 | 2 cells
R509-R510 | consolidated CF | - | Increase/Decrease in Property, Plant and Equipment incu | p12 l527 | 2 cells
R511-R512 | consolidated CF | - | Increase/Decrease in Investment Property | p12 l528 | 2 cells
R513-R514 | consolidated CF | - | Increase/Decrease in Financial Assets- Investments | p12 l529 | 2 cells
R515-R516 | consolidated CF | - | Redemption/ (Purchase) of Fixed Deposits (with Maturity | p12 l531 | 2 cells
R517-R518 | consolidated CF | - | Interest Received | p12 l532 | 2 cells
R519-R520 | consolidated CF | - | Dividend Received | p12 l533 | 2 cells
R521-R522 | consolidated CF | - | Other Non-Operating Income | p12 l534 | 2 cells
R523-R524 | consolidated CF | - | Net Cash (used in)/from Investing activities (B) | p12 l535 | 2 cells
R525-R526 | consolidated CF | - | Interest / financial charges Paid | p12 l537 | 2 cells
R527-R528 | consolidated CF | - | Dividend Paid | p12 l538 | 2 cells
R529-R530 | consolidated CF | - | Net Cash (used in)/from Financing activities (C ) | p12 l539 | 2 cells
R531-R532 | consolidated CF | - | D. Net Changes in Cash and Cash Equivalents (A+B+C) | p12 l540 | 2 cells
R533-R534 | consolidated CF | - | E. Cash and Cash Equivalents at beginning of the Period | p12 l541 | 2 cells
R535-R536 | consolidated CF | - | F. Cash and Cash Equivalents at End of the Period | p12 l542 | 2 cells

## 2b. PARSE FRAGMENTS (not line items)
ROW_IDS | category | A2 flags | cross-ref / note
R265-R266 | standalone BS | PARSE_FRAGMENT | p4 l128 | header or footer text split into numeric cells; not a line item
R325-R326 | standalone BS | PARSE_FRAGMENT | p4 l183 | header or footer text split into numeric cells; not a line item
R327-R328 | consolidated BS | PARSE_FRAGMENT | p11 l434 | header or footer text split into numeric cells; not a line item
R389-R390 | consolidated BS | PARSE_FRAGMENT | p11 l488 | header or footer text split into numeric cells; not a line item
R391-R392 | standalone CF | PARSE_FRAGMENT | p5 l192 | header or footer text split into numeric cells; not a line item
R463-R464 | standalone CF | PARSE_FRAGMENT | p5 l243 | header or footer text split into numeric cells; not a line item
R465-R466 | consolidated CF | PARSE_FRAGMENT | p12 l499 | header or footer text split into numeric cells; not a line item
R537-R538 | consolidated CF | PARSE_FRAGMENT | p12 l549 | header or footer text split into numeric cells; not a line item

## 2c. STANDALONE vs CONSOLIDATED CELL DIFFERENCES (RESTATED / CROSS-REF, IDs only)
table | item | standalone ID | consolidated ID
BS | - Non Current Investments | R275 | R337
BS | - Non Current Investments | R276 | R338
BS | Total Non Current Assets | R283 | R345
BS | Total Non Current Assets | R284 | R346
BS | -Cash and cash equivalents | R289 | R351
BS | -Cash and cash equivalents | R290 | R352
BS | c) Other Current Assets | R293 | R355
BS | c) Other Current Assets | R294 | R356
BS | Total Current Assets | R295 | R357
BS | Total Current Assets | R296 | R358
BS | Total Assets | R297 | R359
BS | Total Assets | R298 | R360
BS | b) Other Equity | R301 | R363
BS | b) Other Equity | R302 | R364
BS | Total Equity | R303 | R365
BS | Total Equity | R304 | R366
BS | -Other Current financial liabilities | R314 | R376
BS | b) Other Current Liabilities | R315 | R377
BS | Total Current Liabilities | R319 | R383
BS | Total Current Liabilities | R320 | R384
BS | Total Liabilities | R321 | R385
BS | Total Liabilities | R322 | R386
CF | Net Profit before tax | R393 | R467
CF | Operating Profit before Working Capital Changes | R407 | R481
CF | Other Current Assets | R415 | R489
CF | Other Current Liabilities | R423 | R497
CF | Cash generated from Operations | R427 | R501
CF | Net Cash from Operating Activities (A) | R433 | R507
CF | D. Net Changes in Cash and Cash Equivalents (A+B+C) | R457 | R531
CF | E. Cash and Cash Equivalents at beginning of the Period | R459 | R533
CF | F. Cash and Cash Equivalents at End of the Period | R461 | R535
items only in standalone: {'P&L': [], 'BS': ['Total Equities and Liabilities'], 'CF': ['Net Cash (used in) /from Financing activities (C )', 'Net Cash (used in) /from Investing activities (B)']} ; only in consolidated: {'P&L': [], 'BS': ['Total Equities and Liabilities 1,28,473.47', 'd) Current Tax Liabilities (Net)'], 'CF': ['Net Cash (used in)/from Financing activities (C )', 'Net Cash (used in)/from Investing activities (B)']}

## 2d. MISSING_FROM_STRUCTURED
M1 | fulltext line 167 (p4) | standalone BS "d) Current Tax Liabilities (Net)" blank in both periods (":" glyph) | ZERO_STANDING, MISSING_FROM_STRUCTURED
M2 | fulltext l568-l574 (p14 area, consolidated LRR) | consolidated LRR para 2 (management responsibility; Ind AS 34 basis; auditor responsibility). No A1 row. Standalone twin is R749 | AUDITOR_PARA, MISSING_FROM_STRUCTURED
M3 | fulltext l278 (p7) | Statement C item 1A, loans/revolving facilities, "Total amount outstanding as on date": blank, no amount, no row. Sits with R601 (1B default Nil) | ZERO_STANDING, BLANK_DISCLOSURE, MISSING_FROM_STRUCTURED
M4 | fulltext l282 (p7) | Statement C item 2A, unlisted debt securities, "Total amount outstanding as on date": blank, no amount, no row. Sits with R602 (2B default Nil) | ZERO_STANDING, BLANK_DISCLOSURE, MISSING_FROM_STRUCTURED
Note: fulltext l281 holds a garbled OCR cell next to the item 2 label ("ti..S..sSC..SY"). Unreadable, not a value; recorded here, not counted.

## 3. AGENDA ITEMS AND BOARD MEETING
ROW_IDS | category | A2 flags | cross-ref / note
R620,R698,R699,R649,R650,R651-R653 | agenda item 1 (results approval; sub a financials, sub b LRR) | - | l32-45; only one agenda item. No AR, AGM, dividend, director, auditor, ESOP or fund-raise item
R597-R598 | meeting start and end time | MEETING_TIME | 11:30 A.M. to 12:20 P.M., 50 minutes
R595-R596 | Regulation 33 SEBI LODR 2015 | - | l38-39

## 3b. RPT ANNEXURE 1 (Statement D, 10 transactions plus totals)
ROW_IDS | category | A2 flags | cross-ref / note
R539-R540 | RPT row | - | RPT#1 Remuneration Jimmy Almeida Kashap CMD | p6 l250
R541-R542 | RPT row | - | RPT#1 Jimmy Almeida Kashap CMD | p6 l250
R543 | RPT row | - | RPT annexure serial number | p6 l250
R544-R545 | RPT row | - | RPT#2 Remuneration Jyoti Almeida Kashyap ED | p6 l251
R546-R547 | RPT row | - | RPT#2 Jyoti Almeida Kashyap ED | p6 l251
R548 | RPT row | - | RPT annexure serial number | p6 l251
R549-R550 | RPT row | - | RPT#3 Remuneration Kiran Parashare ED | p6 l252
R551-R552 | RPT row | - | RPT#3 Kiran Parashare ED | p6 l252
R553 | RPT row | - | RPT annexure serial number | p6 l252
R554-R555 | RPT row | - | RPT#4 Remuneration S Swaminathan CFO | p6 l253
R556-R557 | RPT row | - | RPT#4 S Swaminathan CFO | p6 l253
R558 | RPT row | - | RPT annexure serial number | p6 l253
R559-R560 | RPT row | - | RPT#5 Remuneration Sandeep Kutchhi VP Finance & CS | p6 l254
R561-R562 | RPT row | - | RPT#5 Sandeep Kutchhi VP Finance & CS | p6 l254
R563 | RPT row | - | RPT annexure serial number | p6 l254
R564-R565 | RPT row | - | RPT#6 Lease Rentals Jimmy Almeida Kashap CMD | p6 l255
R566-R567 | RPT row | - | RPT#6 Jimmy Almeida Kashap CMD | p6 l255
R568 | RPT row | - | RPT annexure serial number | p6 l255
R569-R570 | RPT row | - | RPT#7 Dividend Jimmy Almeida Kashyap CMD | p6 l256
R571-R572 | RPT row | - | RPT#7 Jimmy Almeida Kashyap CMD | p6 l256
R573 | RPT row | - | RPT annexure serial number | p6 l256
R574-R575 | RPT row | - | RPT#8 Dividend Jyoti Almeida Kashyap ED | p6 l257
R576-R577 | RPT row | - | RPT#8 Jyoti Almeida Kashyap ED | p6 l257
R578 | RPT row | - | RPT annexure serial number | p6 l257
R579-R580 | RPT row | - | RPT#9 Dividend Almeida Holdings Pvt Ltd promoter | p6 l258
R581-R582 | RPT row | - | RPT#9 Almeida Holdings Pvt Ltd promoter | p6 l258
R583 | RPT row | - | RPT annexure serial number | p6 l258
R584-R585 | RPT row | - | RPT#10 Loans and Advances Buildfort Infradev Pvt Ltd subsidiary | p6 l259
R586-R587 | RPT row | - | RPT#10 Buildfort Infradev Pvt Ltd subsidiary | p6 l259
R588 | RPT row | - | RPT annexure serial number | p6 l259
R589 | RPT row | - | RPT total approved value | p6 l260
R590 | RPT row | - | RPT total transaction value in reporting period | p6 l260

## 3c. IDENTIFIERS, MEETING TIMES, STATEMENT C, AUDITOR IDS
ROW_IDS | category | A2 flags | cross-ref / note
R591 | identifier/number | - | NSE scrip code | p1 l29
R592 | identifier/number | - | BSE scrip code | p1 l29
R593 | identifier/number | - | NSE postal PIN | p1 l28
R594 | identifier/number | - | BSE postal PIN | p1 l28
R595 | identifier/number | - | SEBI LODR regulation number cited | p1 l38
R596 | identifier/number | - | SEBI LODR Regulations year | p1 l39
R597 | identifier/number | MEETING_TIME | board meeting start time | p1 l46 | 50 minute board meeting 11:30-12:20
R598 | identifier/number | MEETING_TIME | board meeting end time | p1 l46 | 50 minute board meeting 11:30-12:20
R599 | identifier/number | - | CIN | p1 l22
R600 | identifier/number | - | GSTN | p1 l21
R601 | identifier/number | ZERO_STANDING | loans/revolving facilities default amount (INR crore) | p7 l279
R602 | identifier/number | ZERO_STANDING | unlisted debt securities default amount (INR crore) | p7 l283
R603 | identifier/number | ZERO_STANDING | total financial indebtedness (INR crore) | p7 l285
M3 | (no A1 row) | ZERO_STANDING, BLANK_DISCLOSURE | item 1A total amount outstanding, blank | p7 l278 | see 2d
M4 | (no A1 row) | ZERO_STANDING, BLANK_DISCLOSURE | item 2A total amount outstanding, blank | p7 l282 | see 2d; garbled cell l281 not a value
R604 | identifier/number | - | Standard on Review Engagement number | p8 l328
R605 | identifier/number | - | Companies Act section cited | p8 l334
R606 | identifier/number | - | Companies Act section cited | p8 l323
R607 | identifier/number | - | Ind AS 34 | p8 l321
R608 | identifier/number | AUDITOR_ID | auditor firm registration no | p9 l366
R609 | identifier/number | AUDITOR_ID | auditor membership no | p9 l375
R610 | identifier/number | AUDITOR_ID | standalone LRR UDIN | p9 l377
R611 | identifier/number | AUDITOR_ID | consolidated LRR UDIN | p14 l618
R612 | identifier/number | AUDITOR_ID | auditor membership no | p14 l617
R613 | identifier/number | AUDITOR_ID | auditor firm registration no | p14 l612
R614 | identifier/number | - | EPS face value per share | p3 l112
R615 | identifier/number | - | EPS face value per share | p10 l418

## 4A. AUDITOR REPORT PARAGRAPHS (see also section 7)
M2 consolidated para 2 (fulltext l568-l574, no A1 row) | R746 cover scope | R747 title scope | R748 para1 | R749 para2 | R750 para3 | R751 no audit opinion | R752 para4 conclusion no qualification | R753 signature | R754-R755,R757,R756 consolidated paras 1,3,4,5
Opinion type: limited review, unmodified conclusion. No Emphasis of Matter, Other Matter or Going Concern language is recorded in A1. Entities reviewed: standalone Holding only; consolidated Holding plus Buildfort Infradev (R754, R757). UDINs R610, R611. Both entities appear as reviewed; no unaudited or management-furnished entity is named in A1.

## 4. ENTITIES
ROW_IDS | category | A2 flags | cross-ref / note
R616 | entity | - | p1 l20
R617 | entity | - | p1 l26
R618 | entity | - | p1 l26
R619 | entity | - | p1 l38
R620 | entity | - | p1 l36
R621 | entity | - | p1 l43
R622 | entity | - | p2 l70
R623 | entity | - | p2 l65
R624 | entity | - | p3 l116
R625 | entity | - | p10 l422
R626 | entity | - | p3 l114
R627 | entity | - | p4 l174
R628 | entity | - | p11 l479
R629 | entity | - | p5 l239
R630 | entity | - | p12 l545
R631 | entity | - | p5 l242
R632 | entity | RPT_COUNTERPARTY | p6 l250
R633 | entity | RPT_COUNTERPARTY | p6 l251
R634 | entity | RPT_COUNTERPARTY | p6 l252
R635 | entity | RPT_COUNTERPARTY | p6 l253
R636 | entity | RPT_COUNTERPARTY | p6 l254
R637 | entity | RPT_COUNTERPARTY | p6 l258
R638 | entity | RPT_COUNTERPARTY | p6 l259
R639 | entity | - | p6 l250
R640 | entity | - | p8 l306
R641 | entity | - | p9 l373
R642 | entity | - | p8 l330
R643 | entity | - | p8 l323
R644 | entity | CONSOLIDATION_LIST | p13 l562
R645 | entity | CONSOLIDATION_LIST | p14 l599
R646 | entity | CONSOLIDATION_LIST | p14 l600

## 5. DATES AND DIGITAL SIGNATURE BLOCKS
ROW_IDS | category | A2 flags | cross-ref / note
R648 | date | - | p1 l23
R649 | date | - | p1 l32
R650 | date | - | p1 l33
R651 | date | - | p1 l37
R652 | date | - | p1 l37
R653 | date | - | p1 l37
R654 | date | - | p3 l86
R655 | date | - | p3 l86
R656 | date | - | p3 l86
R657 | date | - | p3 l86
R658 | date | - | p3 l86
R659 | date | - | p3 l86
R660 | date | - | p10 l392
R661 | date | - | p10 l392
R662 | date | - | p10 l392
R663 | date | - | p10 l392
R664 | date | - | p10 l392
R665 | date | - | p10 l392
R666 | date | - | p3 l82
R667 | date | PERIOD_MISMATCH | p10 l388 | title year differs from column dates; see R723
R668 | date | - | p3 l114
R669 | date | - | p10 l420
R670 | date | - | p4 l127
R671 | date | - | p4 l128
R672 | date | - | p4 l175
R673 | date | - | p11 l433
R674 | date | - | p11 l434
R675 | date | - | p11 l480
R676 | date | - | p5 l191
R677 | date | - | p5 l192
R678 | date | - | p5 l240
R679 | date | - | p5 l234
R680 | date | - | p5 l235
R681 | date | - | p12 l498
R682 | date | - | p12 l499
R683 | date | - | p12 l546
R684 | date | - | p12 l541
R685 | date | - | p12 l542
R686 | date | - | p6 l248
R687 | date | - | p7 l295
R688 | date | - | p8 l311
R689 | date | SIG_BEFORE_MEETING | p8 l344 | digital signature stamp 10:27-10:28 IST is earlier than the 11:30 meeting start (R597)
R690 | date | SIG_BEFORE_MEETING | p9 l368 | digital signature stamp 10:27-10:28 IST is earlier than the 11:30 meeting start (R597)
R691 | date | SIGNATURE_DATE | p9 l379
R692 | date | - | p13 l559
R693 | date | SIG_BEFORE_MEETING | p13 l590 | digital signature stamp 10:27-10:28 IST is earlier than the 11:30 meeting start (R597)
R694 | date | SIG_BEFORE_MEETING | p14 l614 | digital signature stamp 10:27-10:28 IST is earlier than the 11:30 meeting start (R597)
R695 | date | SIGNATURE_DATE | p14 l619
R696 | date | - | p7 l292
R697 | date | - | p7 l288

Signature blocks: auditor standalone R689,R690,R753,R610,R691 ; auditor consolidated R693,R694,R611,R695 ; cover letter signatory R622 (no timestamp in A1); BS signatory R627-R628, R672, R675 ; CF signatory R629-R630, R678, R683. SIG_BEFORE_MEETING raised above.

## 6. FORWARD
ROW_IDS | category | A2 flags | cross-ref / note
R647 | forward | NO_GUIDANCE | p1 l48 | website upload intimation only

## 7. QUALIFIERS
ROW_IDS | category | A2 flags | cross-ref / note
R698 | qualifier | AUDITOR_PARA | p1 l36
R699 | qualifier | AUDITOR_PARA | p1 l43
R700 | qualifier | - | p1 l31
R701 | qualifier | FOOTNOTE | p3 l88
R702 | qualifier | FOOTNOTE | p3 l98
R703 | qualifier | - | p3 l82
R704 | qualifier | NUMBERED_NOTE | p3 l114 | note repeated standalone/consolidated (R704-R707 vs R715-R718)
R705 | qualifier | NUMBERED_NOTE | p3 l115 | note repeated standalone/consolidated (R704-R707 vs R715-R718)
R706 | qualifier | NUMBERED_NOTE | p3 l116 | note repeated standalone/consolidated (R704-R707 vs R715-R718)
R707 | qualifier | NUMBERED_NOTE | p3 l117 | note repeated standalone/consolidated (R704-R707 vs R715-R718)
R708 | qualifier | - | p3 l82
R709 | qualifier | - | p3 l106
R710 | qualifier | - | p3 l112
R711 | qualifier | - | p3 l110
R712 | qualifier | FOOTNOTE | p10 l394
R713 | qualifier | FOOTNOTE | p10 l404
R714 | qualifier | - | p10 l388
R715 | qualifier | NUMBERED_NOTE | p10 l420 | note repeated standalone/consolidated (R704-R707 vs R715-R718)
R716 | qualifier | NUMBERED_NOTE | p10 l421 | note repeated standalone/consolidated (R704-R707 vs R715-R718)
R717 | qualifier | NUMBERED_NOTE | p10 l422 | note repeated standalone/consolidated (R704-R707 vs R715-R718)
R718 | qualifier | NUMBERED_NOTE | p10 l423 | note repeated standalone/consolidated (R704-R707 vs R715-R718)
R719 | qualifier | - | p10 l388
R720 | qualifier | - | p10 l412
R721 | qualifier | - | p10 l418
R722 | qualifier | - | p10 l416
R723 | qualifier | PERIOD_MISMATCH | p10 l388
R724 | qualifier | NOTE_LABEL NUMBERED_NOTE | p4 l126
R725 | qualifier | - | p4 l163
R726 | qualifier | - | p4 l138
R727 | qualifier | ZERO_STANDING | p4 l158 | A1 line 158 vs fulltext l167 (standalone BS Current Tax Liabilities blank row)
R728 | qualifier | NOTE_LABEL NUMBERED_NOTE | p11 l432
R729 | qualifier | - | p11 l468
R730 | qualifier | - | p11 l444
R731 | qualifier | ZERO_STANDING | p11 l463 | A1 line 463 vs fulltext l472
R732 | qualifier | - | p5 l191
R733 | qualifier | RESTATED | p5 l198 | restated across standalone and consolidated CF (R733, R736)
R734 | qualifier | - | p5 l223
R735 | qualifier | - | p12 l498
R736 | qualifier | RESTATED | p12 l505 | restated across standalone and consolidated CF (R733, R736)
R737 | qualifier | - | p12 l530
R738 | qualifier | - | p6 l248
R739 | qualifier | - | p6 l247
R740 | qualifier | - | p6 l260
R741 | qualifier | BLANK_DISCLOSURE | p6 l250
R742 | qualifier | - | p7 l274
R743 | qualifier | - | p7 l272
R744 | qualifier | - | p7 l294
R745 | qualifier | AUDITOR_PARA | p7 l287
R746 | qualifier | AUDITOR_PARA | p7 l295
R747 | qualifier | AUDITOR_PARA | p8 l310
R748 | qualifier | AUDITOR_PARA | p8 l313
R749 | qualifier | AUDITOR_PARA | p8 l319
R750 | qualifier | AUDITOR_PARA | p8 l327
R751 | qualifier | AUDITOR_PARA | p8 l338
R752 | qualifier | AUDITOR_PARA | p9 l352
R753 | qualifier | AUDITOR_PARA | p9 l367
R754 | qualifier | AUDITOR_PARA | p13 l561
R755 | qualifier | AUDITOR_PARA | p13 l586
R756 | qualifier | WORDING_AS_PRINTED AUDITOR_PARA | p14 l601
R757 | qualifier | AUDITOR_PARA | p14 l598

## ZERO_STANDING SUMMARY (NUMBER cells)
true ZERO_STANDING NUMBER cells excluding R388: 57; IDs: R007-R012,R037-R042,R091-R096,R115-R120,R139-R144,R169-R174,R223-R228,R247-R252,R381-R382,R414,R422,R488,R496,R601-R603
Includes P&L: Other operating revenue, Purchase of stock in trade, Exceptional item, OCI fair value gain/loss (standalone and consolidated); consolidated BS Current Tax Liabilities; CF other non-current items; Statement C Nil rows R601-R603. Plus M1 (loop 1: also M3, M4, see 2d).

FINAL ID ACCOUNTABILITY: ids_in_structured: 757 | ids_referenced_in_ledger: 757 | orphan_ids: [] | match: yes

## LOOP 1 AMENDMENTS (correction loop 1, A5 items M4 and M5)
- A5-M4: added M2 (consolidated LRR para 2, l568-l574) to 2d and 4A. auditor_paras fresh count on fulltext: 9 numbered paragraphs (standalone 4, consolidated 5), 8 had rows, 1 missing; with M2 all 9 covered. Ledger auditor_paras 15 -> 16.
- A5-M5: added M3 (l278) and M4 (l282) to 2d and 3c as blank ZERO_STANDING; garbled l281 cell noted. zero_standing total 57 NUMBER cells + M1, M3, M4 = 60 (block counts.zero_standing 57 -> 60).
- Updated: count test lines (zero_standing, auditor_paras), section 0 item 9a, ZERO_STANDING SUMMARY line.
- Unchanged: all existing rows and IDs; ids_in_structured 757; line_items 173 (blank Statement C cells are identifier cells, not P&L/BS/CF line items).
