# COMPLETENESS LEDGER: Aequs Limited (AEQUS) results Q2 FY27 (quarter ended 30-Sep-2026)
source: runs/aequs-q2fy27/extracted/aequs-results-q2fy27-structured.md (A1 structured, R001-R1438); prior-quarter ledger: none available (ENTITY_CHANGE and DROPPED checks use in-document evidence only)
agent: A2 enumerator (claude-sonnet-5-5). Rs Mn as printed; x0.1 = Rs Cr. Claim text lives at the row ID in the structured file; this ledger adds category, flags and cross-references only.

ids_in_structured: 1438 | ids_referenced_in_ledger: 1438 | orphan_ids: [] | match: yes

=== A2 COUNT TEST ===
category: notes          grep_count: 21   sweep_count: 21   match: yes   (grep = distinct "note N" tokens by page in A1 contexts, p5 notes 1-10 and p12 notes 1-8,10-12; sweep = ledger note rows; consolidated note 5 has no qualifier row, found via "consolidation list, note 5" context)
category: line_items     grep_count: 311   sweep_count: 311   match: yes   (grep = distinct page:line pairs over R001-R1180; sweep = line-number transitions in ID order; a label-only sweep gives 304 because A1 truncates labels and 7 lines on p8/p11 collide, namely p8 lines 412-414 and p11 lines 578-580 and 581-584; the line anchor resolves them)
category: zero_standing  grep_count: 90   sweep_count: 90   match: yes   (grep = ZERO flag in A1; sweep = NUMBER values of "-" , 0.00 or (0.00): 72 dashes + 18 zero decimals)
category: agenda_items   grep_count: 1   sweep_count: 1   match: yes   (grep = QUALIFIER "Approval of Un-audited Financial Results" R1376; sweep = letter reading; board meeting 14:50 to 15:35 = 45 min)
category: auditor_paras  grep_count: 12   sweep_count: 12   match: yes   (standalone LRR units S-LRR-1..5; consolidated LRR units C-LRR-1..7; units are A2 groupings of the LRR rows on p6-7 and p13-14, A1 has no paragraph numbering)
category: entities       grep_count: 22   sweep_count: 22   match: yes   (note 5 consolidation list 22 rows vs Annexure I 22 rows; same 22 names, 16 subsidiaries + parent + 4 JVs + 1 associate; plus 37 non-consolidation entity rows R1237-R1273 and 4 status rows)
category: signatures     grep_count: 5   sweep_count: 5   match: yes   (letter, standalone LRR, consolidated LRR, standalone notes, consolidated notes)
category: footnotes      grep_count: 3   sweep_count: 3   match: yes   (standalone EPS asterisk R1381-83, consolidated EPS asterisk R1392-93, segment-results definition R1399)
gate_a2: pass
=== END COUNT TEST ===

## ARITHMETIC TIE-OUTS (A1 pages 2-5 and 8-12 are model-transcribed from images; scratch scripts a2-results-*)
Method: tolerance 0.035 Rs Mn for sums of 2-decimal rows. 346 checks run: standalone and consolidated P&L subtotals (total income, total expenses, EBITDA, PBT before exceptional, PBT, tax, PAT, OCI, TCI), standalone and consolidated balance sheets (non-current assets, current assets, total assets, equity, non-current and current liabilities, total liabilities, assets = equity and liabilities, both dates), standalone and consolidated cash flows (adjustments subtotal, working capital, cash from operations, A, B, C, net change, opening plus net change (plus FX) = closing, closing = components, standalone closing = balance sheet cash), segment sums (revenue, results, finance cost, D&A, assets, liabilities, eliminations, total assets, unallocated, segment results bridge to PBT and PAT). 344 tie. 2 do not tie, both in the consolidated 6M 30-Sep-2025 column:
1. TIE_FAIL C-P&L Total expenses (B) 6M 30-Sep-2025: R441 printed 4,814.39 vs R411 2,326.94 + R417 (154.35) + R423 927.57 + R429 2.26 + R435 1,709.97 = 4,812.39. Gap 2.00. R441 is consistent with the EBITDA row (EBITDA tie passes using R441), so one of R411, R417, R423, R429 or R435 is likely mistranscribed by 2.00 (cannot localise from A1 alone; needs a render check).
2. TIE_FAIL C-CF Cash from operations 6M 30-Sep-2025: R843 printed 541.96 vs components (R758.. through R839 band) 539.70. Gap 2.26 equals the P&L impairment charge R429 (2.26) while the CF add-back R777 reads nil ("-", flagged ZERO_STANDING). R777 is likely a transcription error and should read 2.26. This also supports R429 being right and the 2.00 gap in item 1 sitting in another expense row.
All other statements tie, including all balance sheets (assets = equity and liabilities at both dates for standalone 20,516.21 / 19,968.17 and consolidated 27,739.36 / 26,904.70), all standalone cash flow columns, segment-to-P&L bridges, and the standalone closing cash 712.48 = balance sheet cash. Eliminations and rounding residuals: segment 6M Sep-2025 liabilities R1155 reads 14,396.12 vs R1153 14,396.11 and R1179 13,298.63 vs R1177 13,298.62 (0.01 rounding, within tolerance, not flagged).

Other A2 observations (no interpretation): (a) consolidated note 9 absent in printed numbering (R1421); (b) subsidiary reviewed by an unnamed other auditor, report furnished by Parent management (R1431-R1433, R1254); (c) ATHPL dissolved/liquidated 17-Sep-2026 (R1290, R1310, R1342, R1367) and AMPL formerly Aequs Toys (R1280, R1301): ENTITY_CHANGE, no prior list to diff; (d) spelling differences between lists: R1276 "Manufactuiring" as printed, R1281 "Moulding" vs R1311 "Molding"; (e) standalone note 4 (SQuAD impairment reversal) has no consolidated twin, and consolidated notes carry extra items (notes 4 special-purpose interim statements, R1366/R1414); (f) comparatives for Q2 FY26 are unreviewed in both LRRs (R1333, R1337, R1403, R1413) but the 6M Sep-2025 consolidated column is labelled audited via IPO special-purpose statements (R1414, R1386).

## 1. LINE ITEMS (every row of every financial table; one ledger row per line, column IDs grouped)

ROW_ID(S) | statement | page:line | line item | A2 flags | note
--- | --- | --- | --- | --- | ---
R001-R006 | S-P&L | p2:l86 | Revenue from operations |  |
R007-R012 | S-P&L | p2:l87 | Other income |  |
R013-R018 | S-P&L | p2:l88 | Total income (A) |  |
R019-R024 | S-P&L | p2:l89 | Cost of materials consumed |  |
R025-R030 | S-P&L | p2:l90 | Changes in inventories of finished goods and work-in-progress |  |
R031-R036 | S-P&L | p2:l91 | Employee benefit expense |  |
R037-R042 | S-P&L | p2:l92 | Impairment (reversals)/losses on financial assets | ZERO_STANDING R039,R040 |
R043-R048 | S-P&L | p2:l93 | Other expenses |  |
R049-R054 | S-P&L | p2:l94 | Total expenses (B) |  |
R055-R060 | S-P&L | p2:l95 | Earnings before finance cost, depreciation and amortisation, exception |  |
R061-R066 | S-P&L | p2:l96 | Finance costs |  |
R067-R072 | S-P&L | p2:l97 | Depreciation and amortisation expense |  |
R073-R078 | S-P&L | p2:l98 | Profit before exceptional items and tax |  |
R079-R084 | S-P&L | p2:l99 | Exceptional items gain | ZERO_STANDING R079,R080,R081,R082,R083 |
R085-R090 | S-P&L | p2:l100 | Profit before tax |  |
R091-R096 | S-P&L | p2:l101 | Income tax expense - Current tax |  |
R097-R102 | S-P&L | p2:l102 | Income tax expense - Deferred tax |  |
R103-R108 | S-P&L | p2:l103 | Total tax expense |  |
R109-R114 | S-P&L | p2:l104 | Profit for the period / year |  |
R115-R120 | S-P&L | p2:l105 | Other comprehensive income - Remeasurements of post-employment benefit | ZERO_STANDING R116,R117,R119 |
R121-R126 | S-P&L | p2:l106 | Other comprehensive income - Income tax relating to these items | ZERO_STANDING (all 6 periods) |
R127-R132 | S-P&L | p2:l107 | Other comprehensive income for the period/year, net of tax | ZERO_STANDING R128,R129,R131 |
R133-R138 | S-P&L | p2:l108 | Total comprehensive income for the period/year, net of tax |  |
R139-R144 | S-P&L | p2:l109 | Paid-up equity share capital (face value: INR 10 each) |  |
R145-R147 | S-P&L | p2:l110 | Other equity |  |
R148-R153 | S-P&L | p2:l111 | Earnings per equity share (face value: INR 10 each) - Basic* | ZERO_STANDING R150 |
R154-R159 | S-P&L | p2:l112 | Earnings per equity share (face value: INR 10 each) - Diluted* | ZERO_STANDING R156 |
R160-R161 | S-BS | p3:l125 | Property, plant and equipment |  |
R162-R163 | S-BS | p3:l126 | Right of use assets |  |
R164-R165 | S-BS | p3:l127 | Intangible assets |  |
R166-R167 | S-BS | p3:l128 | Financial assets - Investments in subsidiaries, associates and joint v |  |
R168-R169 | S-BS | p3:l129 | Financial assets - Loans |  |
R170-R171 | S-BS | p3:l130 | Financial assets - Other financial assets (non-current) |  |
R172-R173 | S-BS | p3:l131 | Deferred tax assets (net) |  |
R174-R175 | S-BS | p3:l132 | Current tax assets |  |
R176-R177 | S-BS | p3:l133 | Other non-current assets |  |
R178-R179 | S-BS | p3:l134 | Total non-current assets |  |
R180-R181 | S-BS | p3:l135 | Inventories |  |
R182-R183 | S-BS | p3:l136 | Financial assets - Trade receivables |  |
R184-R185 | S-BS | p3:l137 | Financial assets - Cash and cash equivalents |  |
R186-R187 | S-BS | p3:l138 | Financial assets - Bank balances other than above |  |
R188-R189 | S-BS | p3:l139 | Financial assets - Other financial assets (current) |  |
R190-R191 | S-BS | p3:l140 | Contract assets |  |
R192-R193 | S-BS | p3:l141 | Other current assets |  |
R194-R195 | S-BS | p3:l142 | Total current assets |  |
R196-R197 | S-BS | p3:l143 | Total assets |  |
R198-R199 | S-BS | p3:l144 | Equity share capital |  |
R200-R201 | S-BS | p3:l145 | Other equity |  |
R202-R203 | S-BS | p3:l146 | Total equity |  |
R204-R205 | S-BS | p3:l147 | Non-current financial liabilities - Borrowings | ZERO_STANDING R205 |
R206-R207 | S-BS | p3:l148 | Non-current financial liabilities - Lease liabilities |  |
R208-R209 | S-BS | p3:l149 | Non-current financial liabilities - Other financial liabilities |  |
R210-R211 | S-BS | p3:l150 | Provision for employee benefits (non-current) |  |
R212-R213 | S-BS | p3:l151 | Total non current liabilities |  |
R214-R215 | S-BS | p3:l152 | Current financial liabilities - Borrowings |  |
R216-R217 | S-BS | p3:l153 | Current financial liabilities - Lease liabilities |  |
R218-R219 | S-BS | p3:l154 | Trade Payables a. Total outstanding dues of micro enterprises and smal |  |
R220-R221 | S-BS | p3:l155 | Trade Payables b. Total outstanding dues of creditors other than micro |  |
R222-R223 | S-BS | p3:l156 | Other financial liabilities (current) |  |
R224-R225 | S-BS | p3:l157 | Provision for employee benefits (current) |  |
R226-R227 | S-BS | p3:l158 | Other current liabilities |  |
R228-R229 | S-BS | p3:l159 | Contract liabilities |  |
R230-R231 | S-BS | p3:l160 | Total current liabilities |  |
R232-R233 | S-BS | p3:l161 | Total liabilities |  |
R234-R235 | S-BS | p3:l162 | Total equity and liabilities |  |
R236-R238 | S-CF | p4:l174 | Profit before income tax |  |
R239-R241 | S-CF | p4:l175 | Depreciation and amortisation expense |  |
R242-R244 | S-CF | p4:l176 | Unrealized foreign exchange gain |  |
R245-R247 | S-CF | p4:l177 | Realised loss on lease payment | ZERO_STANDING R246 |
R248-R250 | S-CF | p4:l178 | Equity-settled share-based payment transactions |  |
R251-R253 | S-CF | p4:l179 | Impairment (gain)/loss on long term investments | ZERO_STANDING R251,R252 |
R254-R256 | S-CF | p4:l180 | Impairment loss on loans and interest accrued thereon | ZERO_STANDING R256 |
R257-R259 | S-CF | p4:l181 | Interest income from financial asset at amortised cost |  |
R260-R262 | S-CF | p4:l182 | Liabilities no longer required written back |  |
R263-R265 | S-CF | p4:l183 | Impairment (reversals) / losses on financial assets | ZERO_STANDING R263 |
R266-R268 | S-CF | p4:l184 | Provision for slow moving inventory |  |
R269-R271 | S-CF | p4:l185 | Financial guarantee income |  |
R272-R274 | S-CF | p4:l186 | Finance cost |  |
R275-R277 | S-CF | p4:l187 | Unwinding of discount on security deposits |  |
R278-R280 | S-CF | p4:l188 | Financial guarantee expense |  |
R281-R283 | S-CF | p4:l189 | Operating cash subtotal before working capital adjustments |  |
R284-R286 | S-CF | p4:l190 | Working capital - (Increase) in trade receivables |  |
R287-R289 | S-CF | p4:l191 | Working capital - (Increase) in inventories |  |
R290-R292 | S-CF | p4:l192 | Working capital - (Increase)/ decrease in other financial assets |  |
R293-R295 | S-CF | p4:l193 | Working capital - (Increase) in other assets |  |
R296-R298 | S-CF | p4:l194 | Working capital - (Increase) in contract assets |  |
R299-R301 | S-CF | p4:l195 | Working capital - Increase in trade payables |  |
R302-R304 | S-CF | p4:l196 | Working capital - Increase in provision for employee benefit |  |
R305-R307 | S-CF | p4:l197 | Working capital - (Decrease)/ increase in other financial liabilities |  |
R308-R310 | S-CF | p4:l198 | Working capital - (Decrease)/ increase in other liabilities |  |
R311-R313 | S-CF | p4:l199 | Working capital - Increase in contract liabilities |  |
R314-R316 | S-CF | p4:l200 | Cash (used in)/ generated from operations |  |
R317-R319 | S-CF | p4:l201 | Income taxes paid (net of refunds) |  |
R320-R322 | S-CF | p4:l202 | Net cash used in operating activities (A) |  |
R323-R325 | S-CF | p4:l203 | Acquisition of property, plant and equipment |  |
R326-R328 | S-CF | p4:l204 | Loans given to related parties | ZERO_STANDING R326 |
R329-R331 | S-CF | p4:l205 | Interest received |  |
R332-R334 | S-CF | p4:l206 | Investments in bank deposits | ZERO_STANDING R332,R333 |
R335-R337 | S-CF | p4:l207 | Proceeds from maturity of bank deposits | ZERO_STANDING R336,R337 |
R338-R340 | S-CF | p4:l208 | Investments in subsidiaries, associates and joint ventures |  |
R341-R343 | S-CF | p4:l209 | Net cash used in investing activities (B) |  |
R344-R346 | S-CF | p4:l210 | Proceeds from Issue of equity shares | ZERO_STANDING R344 |
R347-R349 | S-CF | p4:l211 | Share issue expenses (net) | ZERO_STANDING R348 |
R350-R352 | S-CF | p4:l212 | Proceeds from long-term borrowings | ZERO_STANDING R351,R352 |
R353-R355 | S-CF | p4:l213 | Exercise of share option |  |
R356-R358 | S-CF | p4:l214 | Principal payment of lease liabilities |  |
R359-R361 | S-CF | p4:l215 | Proceeds from /(repayment of) short term borrowing (net) |  |
R362-R364 | S-CF | p4:l216 | Finance costs paid |  |
R365-R367 | S-CF | p4:l217 | Net cash generated from financing activities (C) |  |
R368-R370 | S-CF | p4:l218 | Net (decrease)/ increase in cash and cash equivalents (A + B + C) |  |
R371-R373 | S-CF | p4:l219 | Cash and cash equivalents at the beginning of the period/ year |  |
R374-R376 | S-CF | p4:l220 | Cash and cash equivalents at end of the period/ year |  |
R377-R379 | S-CF | p4:l221 | Cash and cash equivalents comprise: Balances with banks - current acco |  |
R380-R382 | S-CF | p4:l222 | Cash and cash equivalents comprise: Balances with banks - deposits wit |  |
R383-R385 | S-CF | p4:l223 | Cash and cash equivalents comprise: Cash on hand |  |
R386-R388 | S-CF | p4:l224 | Total cash and bank balance at the end of the period/ year |  |
R389-R394 | C-P&L | p8:l375 | Continuing operations: Revenue from operations |  |
R395-R400 | C-P&L | p8:l376 | Other income |  |
R401-R406 | C-P&L | p8:l377 | Total income (A) |  |
R407-R412 | C-P&L | p8:l378 | Cost of materials consumed | TIE_FAIL C-P&L total expenses 6M Sep-2025 (R441) vs components |
R413-R418 | C-P&L | p8:l379 | Changes in inventories of finished goods and work-in-progress | TIE_FAIL (component of R441) |
R419-R424 | C-P&L | p8:l380 | Employee benefit expense | TIE_FAIL (component of R441) |
R425-R430 | C-P&L | p8:l381 | Impairment (reversals)/losses on financial assets | TIE_FAIL (component of R441); CF twin R777 shows nil |
R431-R436 | C-P&L | p8:l382 | Other expenses | TIE_FAIL (component of R441) |
R437-R442 | C-P&L | p8:l383 | Total expenses (B) | TIE_FAIL R441 printed 4,814.39 vs components 4,812.39 (diff 2.00) |
R443-R448 | C-P&L | p8:l384 | Earnings from continuing operations before finance costs, depreciation |  |
R449-R454 | C-P&L | p8:l385 | Finance costs |  |
R455-R460 | C-P&L | p8:l386 | Depreciation and amortisation expense |  |
R461-R466 | C-P&L | p8:l387 | Profit / (loss) from continuing operations before share of net profit/ |  |
R467-R472 | C-P&L | p8:l388 | Share of net profit / (loss) of associate and joint ventures accounted |  |
R473-R478 | C-P&L | p8:l389 | Exceptional items loss | ZERO_STANDING R473,R474,R475,R476,R477 |
R479-R484 | C-P&L | p8:l390 | Profit / (loss) before tax from continuing operations |  |
R485-R490 | C-P&L | p8:l391 | Income tax expense - Current tax |  |
R491-R496 | C-P&L | p8:l392 | Income tax expense - Deferred tax |  |
R497-R502 | C-P&L | p8:l393 | Total tax expense |  |
R503-R508 | C-P&L | p8:l394 | Profit / (loss) from continuing operations |  |
R509-R514 | C-P&L | p8:l395 | Discontinued operations: (Loss)/ profit from discontinued operations b | ZERO_STANDING R510 |
R515-R520 | C-P&L | p8:l396 | Tax expense of discontinued operations | ZERO_STANDING (all 6 periods) |
R521-R526 | C-P&L | p8:l397 | (Loss)/ profit from discontinued operations | ZERO_STANDING R522 |
R527-R532 | C-P&L | p8:l398 | Profit / (loss) for the period / year |  |
R533-R538 | C-P&L | p8:l399 | Other comprehensive income - Exchange differences on translating finan |  |
R539-R544 | C-P&L | p8:l400 | Other comprehensive income - Remeasurements of post-employment benefit | ZERO_STANDING R540 |
R545-R550 | C-P&L | p8:l401 | Other comprehensive (loss) / income for the period / year, net of tax |  |
R551-R556 | C-P&L | p8:l402 | Total comprehensive (loss) / income for the period / year, net of tax |  |
R557-R562 | C-P&L | p8:l403 | (Loss) / income attributable to: Owners of Aequs Limited |  |
R563-R568 | C-P&L | p8:l404 | (Loss) / income attributable to: Non controlling interests | ZERO_STANDING R563,R564,R565,R566,R567 |
R569-R574 | C-P&L | p8:l405 | (Loss) / income attributable to: Total |  |
R575-R580 | C-P&L | p8:l406 | Other comprehensive (loss) / income attributable to: Owners of Aequs L |  |
R581-R586 | C-P&L | p8:l407 | Other comprehensive (loss) / income attributable to: Non controlling i | ZERO_STANDING (all 6 periods) |
R587-R592 | C-P&L | p8:l408 | Other comprehensive (loss) / income attributable to: Total |  |
R593-R598 | C-P&L | p8:l409 | Total comprehensive (loss)/ income attributable to: Owners of Aequs Li |  |
R599-R604 | C-P&L | p8:l410 | Total comprehensive (loss)/ income attributable to: Non controlling in | ZERO_STANDING R599,R600,R601,R602,R603 |
R605-R610 | C-P&L | p8:l411 | Total comprehensive (loss)/ income attributable to: Total |  |
R611-R616 | C-P&L | p8:l412 | Total comprehensive (loss)/ income attributable to owners arising from |  |
R617-R622 | C-P&L | p8:l413 | Total comprehensive (loss)/ income attributable to owners arising from | ZERO_STANDING R618 |
R623-R628 | C-P&L | p8:l414 | Total comprehensive (loss)/ income attributable to owners arising from |  |
R629-R634 | C-P&L | p8:l415 | Paid up equity share capital (Face value Rs 10 per share) |  |
R635-R637 | C-P&L | p8:l416 | Other equity |  |
R638-R643 | C-P&L | p8:l417 | EPS from continuing operations attributable to owners (Basic and dilut |  |
R644-R649 | C-P&L | p8:l418 | EPS from discontinued operations attributable to owners (Basic and dil | ZERO_STANDING R644,R645,R646,R647,R649 |
R650-R655 | C-P&L | p8:l419 | EPS from discontinued & continuing operations attributable to owners ( |  |
R656-R657 | C-BS | p9:l432 | Property, plant and equipment |  |
R658-R659 | C-BS | p9:l433 | Right of use assets |  |
R660-R661 | C-BS | p9:l434 | Capital work in progress |  |
R662-R663 | C-BS | p9:l435 | Goodwill |  |
R664-R665 | C-BS | p9:l436 | Other intangible assets |  |
R666-R667 | C-BS | p9:l437 | Investments accounted for using the equity method |  |
R668-R669 | C-BS | p9:l438 | Financial assets - Investments |  |
R670-R671 | C-BS | p9:l439 | Financial assets - Other financial assets (non-current) |  |
R672-R673 | C-BS | p9:l440 | Contract assets (non-current) |  |
R674-R675 | C-BS | p9:l441 | Deferred tax assets (net) |  |
R676-R677 | C-BS | p9:l442 | Current tax assets |  |
R678-R679 | C-BS | p9:l443 | Other non-current assets |  |
R680-R681 | C-BS | p9:l444 | Total non-current assets |  |
R682-R683 | C-BS | p9:l445 | Inventories |  |
R684-R685 | C-BS | p9:l446 | Financial assets - Trade receivables |  |
R686-R687 | C-BS | p9:l447 | Financial assets - Cash and cash equivalents |  |
R688-R689 | C-BS | p9:l448 | Financial assets - Bank balances other than above |  |
R690-R691 | C-BS | p9:l449 | Financial assets - Other financial assets (current) |  |
R692-R693 | C-BS | p9:l450 | Contract assets (current) |  |
R694-R695 | C-BS | p9:l451 | Other current assets |  |
R696-R697 | C-BS | p9:l452 | Assets classified as held for sale |  |
R698-R699 | C-BS | p9:l453 | Total current assets |  |
R700-R701 | C-BS | p9:l454 | Total assets |  |
R702-R703 | C-BS | p9:l455 | Equity share capital |  |
R704-R705 | C-BS | p9:l456 | Other equity |  |
R706-R707 | C-BS | p9:l457 | Equity attributable to owners of Aequs Limited (Formerly known as Aequ |  |
R708-R709 | C-BS | p9:l458 | Non controlling interest |  |
R710-R711 | C-BS | p9:l459 | Total Equity |  |
R712-R713 | C-BS | p9:l460 | Non-current financial liabilities - Borrowings |  |
R714-R715 | C-BS | p9:l461 | Non-current financial liabilities - Lease liabilities |  |
R716-R717 | C-BS | p9:l462 | Non-current financial liabilities - Other financial liabilities |  |
R718-R719 | C-BS | p9:l463 | Provision for employee benefits (non-current) |  |
R720-R721 | C-BS | p9:l464 | Other non-current liabilities |  |
R722-R723 | C-BS | p9:l465 | Contract liabilities (non-current) |  |
R724-R725 | C-BS | p9:l466 | Total non current liabilities |  |
R726-R727 | C-BS | p9:l467 | Current financial liabilities - Borrowings |  |
R728-R729 | C-BS | p9:l468 | Current financial liabilities - Lease liabilities |  |
R730-R731 | C-BS | p9:l469 | Trade Payables a. Total outstanding dues of micro and small enterprise |  |
R732-R733 | C-BS | p9:l470 | Trade Payables b. Total outstanding dues to creditors other than micro |  |
R734-R735 | C-BS | p9:l471 | Other financial liabilities (current) |  |
R736-R737 | C-BS | p9:l472 | Provision for employee benefits (current) |  |
R738-R739 | C-BS | p9:l473 | Other current liabilities |  |
R740-R741 | C-BS | p9:l474 | Current tax liabilities (net) |  |
R742-R743 | C-BS | p9:l475 | Contract liabilities (current) |  |
R744-R745 | C-BS | p9:l476 | Liabilities directly associated with assets classified as held for sal | ZERO_STANDING (all 2 periods) |
R746-R747 | C-BS | p9:l477 | Total current liabilities |  |
R748-R749 | C-BS | p9:l478 | Total liabilities |  |
R750-R751 | C-BS | p9:l479 | Total equity and liabilities |  |
R752-R754 | C-CF | p10:l491 | Loss before income tax from continuing operations |  |
R755-R757 | C-CF | p10:l492 | (Loss) / profit before tax from discontinuing operations |  |
R758-R760 | C-CF | p10:l493 | Loss before tax |  |
R761-R763 | C-CF | p10:l494 | Depreciation and amortisation expense |  |
R764-R766 | C-CF | p10:l495 | Equity-settled share-based payment transactions |  |
R767-R769 | C-CF | p10:l496 | Net (profit) / loss on disposal of property, plant and equipment / inv |  |
R770-R772 | C-CF | p10:l497 | Interest income from financial asset at amortised cost |  |
R773-R775 | C-CF | p10:l498 | Liabilities no longer required written back |  |
R776-R778 | C-CF | p10:l499 | Impairment (reversals)/ losses on financial assets | ZERO_STANDING R777; TIE_FAIL C-CF cash from operations 6M Sep-2025 R843 gap 2.26 equals P&L impairment R429; R777 nil is a likely transcription error |
R779-R781 | C-CF | p10:l500 | Provision for slow moving inventory |  |
R782-R784 | C-CF | p10:l501 | Interest expense |  |
R785-R787 | C-CF | p10:l502 | Finance guarantee income |  |
R788-R790 | C-CF | p10:l503 | Unwinding of discount on security deposits |  |
R791-R793 | C-CF | p10:l504 | Realized exchange loss on lease payments |  |
R794-R796 | C-CF | p10:l505 | Finance guarantee expense |  |
R797-R799 | C-CF | p10:l506 | Unrealised exchange (gain) / loss |  |
R800-R802 | C-CF | p10:l507 | Share of net profit / (loss) of associate and joint ventures accounted |  |
R803-R805 | C-CF | p10:l508 | Provision for doubtful advances and advance written off |  |
R806-R808 | C-CF | p10:l509 | Government grant |  |
R809-R811 | C-CF | p10:l510 | Gain on derecognition of lease | ZERO_STANDING R810,R811 |
R812-R814 | C-CF | p10:l511 | Working capital - (Increase) in trade receivables |  |
R815-R817 | C-CF | p10:l512 | Working capital - (Increase) in inventories |  |
R818-R820 | C-CF | p10:l513 | Working capital - (Increase) / decrease in other financial assets |  |
R821-R823 | C-CF | p10:l514 | Working capital - Decrease / (increase) in other assets |  |
R824-R826 | C-CF | p10:l515 | Working capital - (Increase) in contract assets |  |
R827-R829 | C-CF | p10:l516 | Working capital - Increase in trade payables |  |
R830-R832 | C-CF | p10:l517 | Working capital - Increase in employee benefit obligations |  |
R833-R835 | C-CF | p10:l518 | Working capital - Increase / (decrease) in other financial liabilities |  |
R836-R838 | C-CF | p10:l519 | Working capital - Increase / (decrease) in other liabilities |  |
R839-R841 | C-CF | p10:l520 | Working capital - (Decrease) / increase in contract liabilities |  |
R842-R844 | C-CF | p10:l521 | Cash (used in) / generated from operations | TIE_FAIL R843 printed 541.96 vs components 539.70 (diff 2.26) |
R845-R847 | C-CF | p10:l522 | Income taxes paid (net of refunds) |  |
R848-R850 | C-CF | p10:l523 | Net cash (used in) / generated from operating activities (A) |  |
R851-R853 | C-CF | p10:l524 | Acquisition of property, plant and equipment |  |
R854-R856 | C-CF | p10:l525 | Proceeds from sale of property, plant and equipment / investment prope |  |
R857-R859 | C-CF | p10:l526 | Investment in bank deposits |  |
R860-R862 | C-CF | p10:l527 | Proceeds from maturity of bank deposits |  |
R863-R865 | C-CF | p10:l528 | Government grants received |  |
R866-R868 | C-CF | p10:l529 | Interest received |  |
R869-R871 | C-CF | p10:l530 | Assets classified as held for sale | ZERO_STANDING R870 |
R872-R874 | C-CF | p10:l531 | Investments in joint ventures and associate | ZERO_STANDING R873 |
R875-R877 | C-CF | p10:l532 | Net cash used in investing activities (B) |  |
R878-R880 | C-CF | p10:l533 | Proceeds from issue of equity shares (net of treasury shares) | ZERO_STANDING R878 |
R881-R883 | C-CF | p10:l534 | Proceeds from exercise of share options |  |
R884-R886 | C-CF | p10:l535 | Proceeds from issue of non-convertible debentures | ZERO_STANDING R884,R885 |
R887-R889 | C-CF | p10:l536 | Redemption of non-convertible debentures | ZERO_STANDING R888,R889 |
R890-R892 | C-CF | p10:l537 | Share issue expenses (net) | ZERO_STANDING R891 |
R893-R895 | C-CF | p10:l538 | Proceeds from long term borrowing |  |
R896-R898 | C-CF | p10:l539 | Repayment of long term borrowing |  |
R899-R901 | C-CF | p10:l540 | Principal payment of lease liabilities |  |
R902-R904 | C-CF | p10:l541 | Proceeds from / (repayment of) short term borrowing (net) |  |
R905-R907 | C-CF | p10:l542 | Finance costs paid |  |
R908-R910 | C-CF | p10:l543 | Net cash generated from financing activities (C) |  |
R911-R913 | C-CF | p10:l544 | Net (decrease) / increase in cash and cash equivalents ( A + B + C) |  |
R914-R916 | C-CF | p10:l545 | Cash and cash equivalents at the beginning of the period / year |  |
R917-R919 | C-CF | p10:l546 | Effects of exchange rate changes on cash and cash equivalents |  |
R920-R922 | C-CF | p10:l547 | Cash and cash equivalents at the end of the period / year |  |
R923-R925 | C-CF | p10:l548 | Cash and cash equivalents comprise: Balances with banks - In current a |  |
R926-R928 | C-CF | p10:l549 | Cash and cash equivalents comprise: Balances with banks - Deposits wit |  |
R929-R931 | C-CF | p10:l550 | Cash and cash equivalents comprise: Cash on hand |  |
R932-R934 | C-CF | p10:l551 | Total cash and cash equivalents |  |
R935-R940 | C-SEG | p11:l563 | Segment revenue - Aerospace |  |
R941-R946 | C-SEG | p11:l564 | Segment revenue - Consumer |  |
R947-R952 | C-SEG | p11:l565 | Total external revenue |  |
R953-R958 | C-SEG | p11:l566 | Segment results - Aerospace |  |
R959-R964 | C-SEG | p11:l567 | Segment results - Consumer |  |
R965-R970 | C-SEG | p11:l568 | Segment results - Total |  |
R971-R976 | C-SEG | p11:l569 | Less: Eliminations (segment results) |  |
R977-R982 | C-SEG | p11:l570 | Total segment results before finance cost, depreciation and amortisati |  |
R983-R988 | C-SEG | p11:l571 | Less: Finance cost - Aerospace |  |
R989-R994 | C-SEG | p11:l572 | Less: Finance cost - Consumer |  |
R995-R1000 | C-SEG | p11:l573 | Less: Finance cost - Elimination |  |
R1001-R1006 | C-SEG | p11:l574 | Less: Finance cost - Total |  |
R1007-R1012 | C-SEG | p11:l575 | Less: Depreciation and amortisation expense - Aerospace |  |
R1013-R1018 | C-SEG | p11:l576 | Less: Depreciation and amortisation expense - Consumer |  |
R1019-R1024 | C-SEG | p11:l577 | Less: Depreciation and amortisation expense - Total |  |
R1025-R1030 | C-SEG | p11:l578 | Add: Share of profit/ (loss) of associate and joint ventures, net of t |  |
R1031-R1036 | C-SEG | p11:l579 | Add: Share of profit/ (loss) of associate and joint ventures, net of t |  |
R1037-R1042 | C-SEG | p11:l580 | Add: Share of profit/ (loss) of associate and joint ventures, net of t |  |
R1043-R1048 | C-SEG | p11:l581 | (Loss)/ profit before exceptional items, unallocated corporate expense |  |
R1049-R1054 | C-SEG | p11:l582 | (Loss)/ profit before exceptional items, unallocated corporate expense |  |
R1055-R1060 | C-SEG | p11:l583 | (Loss)/ profit before exceptional items, unallocated corporate expense |  |
R1061-R1066 | C-SEG | p11:l584 | (Loss)/ profit before exceptional items, unallocated corporate expense |  |
R1067-R1072 | C-SEG | p11:l585 | Add/less: Exceptional items loss | ZERO_STANDING R1067,R1068,R1069,R1070,R1071 |
R1073-R1078 | C-SEG | p11:l586 | Less: Unallocated corporate expenses net of unallocated income |  |
R1079-R1084 | C-SEG | p11:l587 | Loss before tax |  |
R1085-R1090 | C-SEG | p11:l588 | Less: Tax expense |  |
R1091-R1096 | C-SEG | p11:l589 | Loss after tax for the period/year |  |
R1097-R1102 | C-SEG | p11:l590 | Segment assets - Aerospace |  |
R1103-R1108 | C-SEG | p11:l591 | Segment assets - Consumer |  |
R1109-R1114 | C-SEG | p11:l592 | Segment assets - Total |  |
R1115-R1120 | C-SEG | p11:l593 | Segment assets - Less: Eliminations |  |
R1121-R1126 | C-SEG | p11:l594 | Total segment assets |  |
R1127-R1132 | C-SEG | p11:l595 | Unallocated corporate assets |  |
R1133-R1138 | C-SEG | p11:l596 | Total assets |  |
R1139-R1144 | C-SEG | p11:l597 | Segment liabilities - Aerospace |  |
R1145-R1150 | C-SEG | p11:l598 | Segment liabilities - Consumer |  |
R1151-R1156 | C-SEG | p11:l599 | Segment liabilities - Total |  |
R1157-R1162 | C-SEG | p11:l600 | Segment liabilities - Less: Eliminations |  |
R1163-R1168 | C-SEG | p11:l601 | Total segment liabilities |  |
R1169-R1174 | C-SEG | p11:l602 | Unallocated corporate liabilities |  |
R1175-R1180 | C-SEG | p11:l603 | Total liabilities |  |

## 2. AGENDA ITEMS AND BOARD OUTCOME LETTER

ROW_ID(S) | category | description | A2 flags | cross-ref / materiality
--- | --- | --- | --- | ---
R1376 | agenda_items | Agenda item 1: approval of un-audited standalone and consolidated results |  | only agenda item in structured file; no AR/AGM/dividend/director/auditor/ESOP/capital-raising item present (those rows absent from A1 extract; not a miss on its own)
R1330,R1377 | agenda_items | Results period and limited review report enclosure |  | xref R1376
R1327-R1328 | agenda_items | Letter date and board meeting date |  | both 26-Oct-2026
R1186-R1187,R1329 | agenda_items | Board meeting start 14:50 and end 15:35 IST (45 minutes) | RESTATED | three rows carry the same times; short results-only meeting
R1318 | agenda_items | Undertaking to post intimation on company website | FORWARD | 
R1181,R1183-R1185,R1188,R1380 | agenda_items | Letter header: scrip code, telephones, CIN, regulations cited, name change (formerly Aequs Private Limited) |  | 
R1378 | agenda_items | Enclosures reference |  | 

## 3. SIGNATURE BLOCKS

ROW_ID(S) | category | description | A2 flags | cross-ref / materiality
--- | --- | --- | --- | ---
R1331,R1379 | signatures | Letter e-signature: Ravi Mallikarjun Hugar, Company Secretary, 2026-10-26 16:09:14 +05:30 | SIGNATURE_AFTER_BOARD_CLOSE | board closed 15:35; signature 34 minutes later; ordinary, no timestamp-before-close flag
R1182,R1242 | signatures | CS membership A20823 and signatory name |  | 
R1193-R1195,R1252,R1335 | signatures | Standalone LRR signature: BSR & Co LLP, partner Sampad Guha Thakurta, membership 060573, UDIN 26060573JYKDQR9325, dated 26-Oct-2026 |  | 
R1212-R1214,R1255,R1341 | signatures | Consolidated LRR signature: BSR & Co LLP, partner Sampad Guha Thakurta, membership 060573, UDIN 26060573PSWXHT1975, dated 26-Oct-2026 |  | two UDINs differ as expected
R1226,R1261,R1363 | signatures | Standalone notes signature: Rajeev Kaul, Co-Founder and MD, DIN-01468590, 26-Oct-2026 |  | signs notes; the letter is signed by the CS
R1235,R1269,R1375 | signatures | Consolidated notes signature: Rajeev Kaul, Co-Founder and MD, DIN-01468590, 26-Oct-2026 |  | xref R1261

## 4. AUDITOR REPORT PARAGRAPHS (standalone and consolidated limited review reports)

ROW_ID(S) | category | description | A2 flags | cross-ref / materiality
--- | --- | --- | --- | ---
R1189-R1192,R1248,R1250,R1437 | auditor_paras | S-LRR-1 Title, addressee, auditor identity and letterhead (standalone) |  | 
R1202,R1249,R1332,R1422 | auditor_paras | S-LRR-2 Scope: standalone results incl. Aequs Stock Option Plan Trust interim information; Ind AS 34 basis |  | 
R1201,R1251,R1424-R1425 | auditor_paras | S-LRR-3 Review standard SRE 2410; review is not an audit; no audit opinion |  | 
R1333,R1423 | auditor_paras | S-LRR-4 Comparative quarter and half year Sep-2025 approved by Board but not reviewed | COMPARATIVES_UNREVIEWED | 
R1334 | auditor_paras | S-LRR-5 BSR & Co conversion to LLP, 14-Oct-2013 |  | 
R1196-R1199,R1438 | auditor_paras | C-LRR-1 Title and auditor letterhead (consolidated) |  | 
R1253,R1336,R1430 | auditor_paras | C-LRR-2 Scope: Group, associate and joint ventures; periods reviewed |  | 
R1200,R1203,R1427-R1429 | auditor_paras | C-LRR-3 SRE 2410, Ind AS 34, SEBI Reg 33(8) circular procedures; review is not an audit |  | 
R1337,R1426 | auditor_paras | C-LRR-4 Comparative quarter Sep-2025 not reviewed | COMPARATIVES_UNREVIEWED | 
R1204-R1211,R1254,R1339-R1340,R1431-R1433 | auditor_paras | C-LRR-5 Para 6: unnamed subsidiary reviewed by other auditor, reliance on report furnished by Parent management; total assets 1,293.62, revenue 324.99 (Q) and 712.44 (6M), net loss 30.81 (Q) and 73.86 (6M), net cash outflow 5.98, all Rs Mn | OTHER_AUDITOR_UNNAMED; MGMT_FURNISHED_REPORT | subsidiary unaudited by group auditor; unnamed in text
R1434 | auditor_paras | C-LRR-6 Conclusion not modified in respect of matter | EMPHASIS_OR_OTHER_MATTER_UNMODIFIED | 
R1215,R1338 | auditor_paras | C-LRR-7 BSR conversion to LLP date; LRR page count 4 |  | 

## 5. NOTES (numbered notes, standalone 1-10, consolidated 1-8, 10-12)

ROW_ID(S) | category | description | A2 flags | cross-ref / materiality
--- | --- | --- | --- | ---
R1352,R1401 | notes | Note standalone 1 |  | 
R1353,R1402 | notes | Note standalone 2 |  | 
R1354,R1403 | notes | Note standalone 3 |  | 
R1217,R1355,R1404 | notes | Note standalone 4 | STANDALONE_ONLY | impairment reversal on SQuAD investment FY26 only; no consolidated twin note
R1218-R1220,R1356,R1405 | notes | Note standalone 5 |  | 
R1221-R1223,R1357,R1406 | notes | Note standalone 6 |  | 
R1319,R1325,R1358-R1359,R1410 | notes | Note standalone 7 | RESTATED | scheme of amalgamation rejected 12-Oct-2026; same as C8 R1417
R1224-R1225,R1320-R1321,R1360-R1362,R1407 | notes | Note standalone 8 | RESTATED | warrants Rs 6,500 Mn; same as C10
R1408 | notes | Note standalone 9 |  | 
R1409 | notes | Note standalone 10 |  | 
R1411 | notes | Note consolidated 1 |  | 
R1364,R1412 | notes | Note consolidated 2 |  | 
R1365,R1413 | notes | Note consolidated 3 |  | 
R1366,R1414 | notes | Note consolidated 4 |  | 
R1367 | notes | Note consolidated 5 | ENTITY_CHANGE | consolidation list, 22 entries; see entities table
R1227-R1229,R1368,R1415 | notes | Note consolidated 6 |  | 
R1230-R1232,R1369,R1416 | notes | Note consolidated 7 |  | 
R1322,R1326,R1370-R1371,R1417 | notes | Note consolidated 8 |  | 
R1233-R1234,R1323-R1324,R1372-R1374,R1418 | notes | Note consolidated 10 | NOTE_RENUMBERED | same warrant subject as standalone S8
R1236,R1419 | notes | Note consolidated 11 |  | 
R1420 | notes | Note consolidated 12 |  | 
R1421 | notes | Note consolidated -GAP | NOTE_NUMBERING_GAP | printed numbering jumps from note 8 to note 10; no note 9 in consolidated notes

## 6. ENTITIES (consolidation lists, Annexure I, other named entities)

ROW_ID(S) | category | description | A2 flags | cross-ref / materiality
--- | --- | --- | --- | ---
R1274 | entities | Note 5 consolidation list entry |  | 
R1275 | entities | Note 5 consolidation list entry |  | 
R1276 | entities | Note 5 consolidation list entry | SPELLING_AS_PRINTED | 
R1277 | entities | Note 5 consolidation list entry |  | 
R1278 | entities | Note 5 consolidation list entry |  | 
R1279 | entities | Note 5 consolidation list entry |  | 
R1280 | entities | Note 5 consolidation list entry | ENTITY_CHANGE (renamed, formerly Aequs Toys Pvt Ltd) | 
R1281 | entities | Note 5 consolidation list entry | SPELLING_VARIANT (Moulding vs Molding R1311) | 
R1282 | entities | Note 5 consolidation list entry |  | 
R1283 | entities | Note 5 consolidation list entry |  | 
R1284 | entities | Note 5 consolidation list entry |  | 
R1285 | entities | Note 5 consolidation list entry |  | 
R1286 | entities | Note 5 consolidation list entry |  | 
R1287 | entities | Note 5 consolidation list entry |  | 
R1288 | entities | Note 5 consolidation list entry |  | 
R1289 | entities | Note 5 consolidation list entry |  | 
R1290 | entities | Note 5 consolidation list entry | ENTITY_CHANGE (dissolved w.e.f. 17-Sep-2026) | 
R1291 | entities | Note 5 consolidation list entry |  | 
R1292 | entities | Note 5 consolidation list entry |  | 
R1293 | entities | Note 5 consolidation list entry |  | 
R1294 | entities | Note 5 consolidation list entry |  | 
R1295 | entities | Note 5 consolidation list entry |  | 
R1296 | entities | Annexure I entity |  | xref note 5 list; 22 vs 22 entries
R1297 | entities | Annexure I entity |  | 
R1298 | entities | Annexure I entity |  | 
R1299 | entities | Annexure I entity |  | 
R1300 | entities | Annexure I entity |  | 
R1301 | entities | Annexure I entity | ENTITY_CHANGE (renamed, formerly Aequs Toys Pvt Ltd) | 
R1302 | entities | Annexure I entity |  | 
R1303 | entities | Annexure I entity |  | 
R1304 | entities | Annexure I entity |  | 
R1305 | entities | Annexure I entity |  | 
R1306 | entities | Annexure I entity |  | 
R1307 | entities | Annexure I entity |  | 
R1308 | entities | Annexure I entity |  | 
R1309 | entities | Annexure I entity |  | 
R1310 | entities | Annexure I entity | ENTITY_CHANGE (Liquidated w.e.f. 17-Sep-2026) | 
R1311 | entities | Annexure I entity | SPELLING_VARIANT (Molding vs Moulding R1281) | 
R1312 | entities | Annexure I entity |  | 
R1313 | entities | Annexure I entity |  | 
R1314 | entities | Annexure I entity |  | 
R1315 | entities | Annexure I entity |  | 
R1316 | entities | Annexure I entity |  | 
R1317 | entities | Annexure I entity |  | 
R1216,R1342,R1435-R1436 | entities | Annexure I status / liquidation date / list title / count 22 | ENTITY_CHANGE | xref R1290, R1310
R1237-R1241,R1243-R1247,R1256-R1260,R1262-R1268,R1270-R1273 | entities | Non-consolidation entities: exchanges, addresses, regulators, auditors, promoter allottee, signatories, CODM, JV/subsidiaries named in notes |  | includes Melligeri Private Family Foundation (promoter, warrant allottee) R1256/R1266 and SQuAD Forging JV R1257

## 7. TABLE HEADERS AND QUALIFIERS

ROW_ID(S) | category | description | A2 flags | cross-ref / materiality
--- | --- | --- | --- | ---
R1343-R1351 | table_headers | Statement period/date headers for standalone P&L,BS,CF and consolidated P&L,BS,CF,segment |  | 
R1384-R1391,R1394-R1398,R1400 | table_headers | Unit conventions, unaudited/audited column labels, exceptional item FY26-only marker |  | R1386: five columns Unaudited, FY column Audited

## 8. FOOTNOTES (asterisk and definition notes)

ROW_ID(S) | category | description | A2 flags | cross-ref / materiality
--- | --- | --- | --- | ---
R1381-R1383 | footnotes | Standalone EPS asterisk: not annualised |  | 
R1392-R1393 | footnotes | Consolidated EPS asterisk: not annualised; diluted EPS anti-dilutive |  | 
R1399 | footnotes | Segment results subtotal definition (excludes finance cost, D&A, associate/JV share, exceptional items, unallocated corporate, tax) |  | 

## 9. ZERO_STANDING ROWS (nil, dash, 0.00; each also appears in section 1 under its line)

ROW_ID | statement | line | column | value
--- | --- | --- | --- | ---
R039 | S-P&L | Impairment (reversals)/losses on financial assets | Q 30-Sep-2025 | -
R040 | S-P&L | Impairment (reversals)/losses on financial assets | 6M 30-Sep-2026 | -
R079 | S-P&L | Exceptional items gain | Q 30-Sep-2026 | -
R080 | S-P&L | Exceptional items gain | Q 30-Jun-2026 | -
R081 | S-P&L | Exceptional items gain | Q 30-Sep-2025 | -
R082 | S-P&L | Exceptional items gain | 6M 30-Sep-2026 | -
R083 | S-P&L | Exceptional items gain | 6M 30-Sep-2025 | -
R116 | S-P&L | Other comprehensive income - Remeasurements of post-employment benefit | Q 30-Jun-2026 | -
R117 | S-P&L | Other comprehensive income - Remeasurements of post-employment benefit | Q 30-Sep-2025 | -
R119 | S-P&L | Other comprehensive income - Remeasurements of post-employment benefit | 6M 30-Sep-2025 | -
R121 | S-P&L | Other comprehensive income - Income tax relating to these items | Q 30-Sep-2026 | -
R122 | S-P&L | Other comprehensive income - Income tax relating to these items | Q 30-Jun-2026 | -
R123 | S-P&L | Other comprehensive income - Income tax relating to these items | Q 30-Sep-2025 | -
R124 | S-P&L | Other comprehensive income - Income tax relating to these items | 6M 30-Sep-2026 | -
R125 | S-P&L | Other comprehensive income - Income tax relating to these items | 6M 30-Sep-2025 | -
R126 | S-P&L | Other comprehensive income - Income tax relating to these items | FY 31-Mar-2026 | -
R128 | S-P&L | Other comprehensive income for the period/year, net of tax | Q 30-Jun-2026 | -
R129 | S-P&L | Other comprehensive income for the period/year, net of tax | Q 30-Sep-2025 | -
R131 | S-P&L | Other comprehensive income for the period/year, net of tax | 6M 30-Sep-2025 | -
R150 | S-P&L | Earnings per equity share (face value: INR 10 each) - Basic* | Q 30-Sep-2025 | 0.00
R156 | S-P&L | Earnings per equity share (face value: INR 10 each) - Diluted* | Q 30-Sep-2025 | 0.00
R205 | S-BS | Non-current financial liabilities - Borrowings | As at 31-Mar-2026 | -
R246 | S-CF | Realised loss on lease payment | 6M 30-Sep-2025 | -
R251 | S-CF | Impairment (gain)/loss on long term investments | 6M 30-Sep-2026 | -
R252 | S-CF | Impairment (gain)/loss on long term investments | 6M 30-Sep-2025 | -
R256 | S-CF | Impairment loss on loans and interest accrued thereon | FY 31-Mar-2026 | -
R263 | S-CF | Impairment (reversals) / losses on financial assets | 6M 30-Sep-2026 | -
R326 | S-CF | Loans given to related parties | 6M 30-Sep-2026 | -
R332 | S-CF | Investments in bank deposits | 6M 30-Sep-2026 | -
R333 | S-CF | Investments in bank deposits | 6M 30-Sep-2025 | -
R336 | S-CF | Proceeds from maturity of bank deposits | 6M 30-Sep-2025 | -
R337 | S-CF | Proceeds from maturity of bank deposits | FY 31-Mar-2026 | -
R344 | S-CF | Proceeds from Issue of equity shares | 6M 30-Sep-2026 | -
R348 | S-CF | Share issue expenses (net) | 6M 30-Sep-2025 | -
R351 | S-CF | Proceeds from long-term borrowings | 6M 30-Sep-2025 | -
R352 | S-CF | Proceeds from long-term borrowings | FY 31-Mar-2026 | -
R473 | C-P&L | Exceptional items loss | Q 30-Sep-2026 | -
R474 | C-P&L | Exceptional items loss | Q 30-Jun-2026 | -
R475 | C-P&L | Exceptional items loss | Q 30-Sep-2025 | -
R476 | C-P&L | Exceptional items loss | 6M 30-Sep-2026 | -
R477 | C-P&L | Exceptional items loss | 6M 30-Sep-2025 | -
R510 | C-P&L | Discontinued operations: (Loss)/ profit from discontinued operations b | Q 30-Jun-2026 | (0.00)
R515 | C-P&L | Tax expense of discontinued operations | Q 30-Sep-2026 | -
R516 | C-P&L | Tax expense of discontinued operations | Q 30-Jun-2026 | -
R517 | C-P&L | Tax expense of discontinued operations | Q 30-Sep-2025 | -
R518 | C-P&L | Tax expense of discontinued operations | 6M 30-Sep-2026 | -
R519 | C-P&L | Tax expense of discontinued operations | 6M 30-Sep-2025 | -
R520 | C-P&L | Tax expense of discontinued operations | FY 31-Mar-2026 | -
R522 | C-P&L | (Loss)/ profit from discontinued operations | Q 30-Jun-2026 | (0.00)
R540 | C-P&L | Other comprehensive income - Remeasurements of post-employment benefit | Q 30-Jun-2026 | -
R563 | C-P&L | (Loss) / income attributable to: Non controlling interests | Q 30-Sep-2026 | (0.00)
R564 | C-P&L | (Loss) / income attributable to: Non controlling interests | Q 30-Jun-2026 | (0.00)
R565 | C-P&L | (Loss) / income attributable to: Non controlling interests | Q 30-Sep-2025 | -
R566 | C-P&L | (Loss) / income attributable to: Non controlling interests | 6M 30-Sep-2026 | (0.00)
R567 | C-P&L | (Loss) / income attributable to: Non controlling interests | 6M 30-Sep-2025 | -
R581 | C-P&L | Other comprehensive (loss) / income attributable to: Non controlling i | Q 30-Sep-2026 | -
R582 | C-P&L | Other comprehensive (loss) / income attributable to: Non controlling i | Q 30-Jun-2026 | -
R583 | C-P&L | Other comprehensive (loss) / income attributable to: Non controlling i | Q 30-Sep-2025 | -
R584 | C-P&L | Other comprehensive (loss) / income attributable to: Non controlling i | 6M 30-Sep-2026 | -
R585 | C-P&L | Other comprehensive (loss) / income attributable to: Non controlling i | 6M 30-Sep-2025 | -
R586 | C-P&L | Other comprehensive (loss) / income attributable to: Non controlling i | FY 31-Mar-2026 | -
R599 | C-P&L | Total comprehensive (loss)/ income attributable to: Non controlling in | Q 30-Sep-2026 | (0.00)
R600 | C-P&L | Total comprehensive (loss)/ income attributable to: Non controlling in | Q 30-Jun-2026 | (0.00)
R601 | C-P&L | Total comprehensive (loss)/ income attributable to: Non controlling in | Q 30-Sep-2025 | -
R602 | C-P&L | Total comprehensive (loss)/ income attributable to: Non controlling in | 6M 30-Sep-2026 | (0.00)
R603 | C-P&L | Total comprehensive (loss)/ income attributable to: Non controlling in | 6M 30-Sep-2025 | -
R618 | C-P&L | Total comprehensive (loss)/ income attributable to owners arising from | Q 30-Jun-2026 | (0.00)
R644 | C-P&L | EPS from discontinued operations attributable to owners (Basic and dil | Q 30-Sep-2026 | (0.00)
R645 | C-P&L | EPS from discontinued operations attributable to owners (Basic and dil | Q 30-Jun-2026 | (0.00)
R646 | C-P&L | EPS from discontinued operations attributable to owners (Basic and dil | Q 30-Sep-2025 | 0.00
R647 | C-P&L | EPS from discontinued operations attributable to owners (Basic and dil | 6M 30-Sep-2026 | (0.00)
R649 | C-P&L | EPS from discontinued operations attributable to owners (Basic and dil | FY 31-Mar-2026 | 0.00
R744 | C-BS | Liabilities directly associated with assets classified as held for sal | As at 30-Sep-2026 | 0.00
R745 | C-BS | Liabilities directly associated with assets classified as held for sal | As at 31-Mar-2026 | 0.00
R777 | C-CF | Impairment (reversals)/ losses on financial assets | 6M 30-Sep-2025 | -
R810 | C-CF | Gain on derecognition of lease | 6M 30-Sep-2025 | -
R811 | C-CF | Gain on derecognition of lease | FY 31-Mar-2026 | -
R870 | C-CF | Assets classified as held for sale | 6M 30-Sep-2025 | -
R873 | C-CF | Investments in joint ventures and associate | 6M 30-Sep-2025 | -
R878 | C-CF | Proceeds from issue of equity shares (net of treasury shares) | 6M 30-Sep-2026 | -
R884 | C-CF | Proceeds from issue of non-convertible debentures | 6M 30-Sep-2026 | -
R885 | C-CF | Proceeds from issue of non-convertible debentures | 6M 30-Sep-2025 | -
R888 | C-CF | Redemption of non-convertible debentures | 6M 30-Sep-2025 | -
R889 | C-CF | Redemption of non-convertible debentures | FY 31-Mar-2026 | -
R891 | C-CF | Share issue expenses (net) | 6M 30-Sep-2025 | -
R1067 | C-SEG | Add/less: Exceptional items loss | Q 30-Sep-2026 | -
R1068 | C-SEG | Add/less: Exceptional items loss | Q 30-Jun-2026 | -
R1069 | C-SEG | Add/less: Exceptional items loss | Q 30-Sep-2025 | -
R1070 | C-SEG | Add/less: Exceptional items loss | 6M 30-Sep-2026 | -
R1071 | C-SEG | Add/less: Exceptional items loss | 6M 30-Sep-2025 | -

```yaml
stage: A2-enumerator
company: "AEQUS"
quarter: "q2fy27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/aequs-q2fy27/work/ledger_results_aequs_q2fy27.md"
counts:
  notes: 21
  line_items: 311
  zero_standing: 90
  agenda_items: 1
  auditor_paras: 12
  entities: 22
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, ENTITY_CHANGE, TIE_FAIL, NOTE_NUMBERING_GAP, NOTE_RENUMBERED, RESTATED, STANDALONE_ONLY, COMPARATIVES_UNREVIEWED, OTHER_AUDITOR_UNNAMED, MGMT_FURNISHED_REPORT, SPELLING_VARIANT]
ids_in_structured: 1438
ids_referenced: 1438
orphan_ids: []
missing_from_structured: []
gate_a2: pass
mismatch_note: ""
analyst_note: "Image-transcribed statements were checked arithmetically: 344 of 346 tie-outs pass. Two non-ties both sit in the consolidated 6M 30-Sep-2025 column. (1) Total expenses R441 4,814.39 vs component sum 4,812.39 (gap 2.00; a component among R411, R417, R423, R429, R435 is probably mistranscribed). (2) Cash from operations R843 541.96 vs components 539.70 (gap 2.26); R777 (impairment add-back) reads nil but should likely be 2.26, equal to P&L R429. Downstream stages should not lean on the 6M Sep-2025 consolidated expense and operating cash lines until A1 re-checks these renders. The line-item label sweep gives 304 vs 311 line anchors because A1 truncates labels; line anchors govern. Consolidated note 9 is absent from the printed numbering. No prior ledger exists, so ENTITY_CHANGE (ATHPL dissolved 17-Sep-2026, AMPL renamed) rests on in-document wording only. One subsidiary is reviewed by an unnamed other auditor with the report furnished by Parent management."
```
