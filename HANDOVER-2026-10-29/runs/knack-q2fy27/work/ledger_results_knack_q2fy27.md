# A2 COMPLETENESS LEDGER: Knack Packaging Limited (KNACK) results q2fy27
# source: A1 structured extraction runs/knack-q2fy27/extracted/knack-results-q2fy27-structured.md (R001-R921); fulltext used for independent sweep only
# unit: Rs. millions (x0.1 to Rs Crore). Prior ledger: none (first quarterly review). ENTITY_CHANGE not assessable.
# row format: ROW_ID(s) | category | A2 flags | cross-ref / materiality. Verbatim values live in the structured file at the ID (page/line anchor there).

ids_in_structured: 921 | ids_referenced_in_ledger: 921 | orphan_ids: [] | match: yes
(plus 1 ledger-added row M1 flagged MISSING_FROM_STRUCTURED, own line number 79)

```
=== A2 COUNT TEST ===
category: notes_numbered   grep_count: 18   sweep_count: 18   match: yes   (SA 1-9 at lines 343-400; CON 1-9 at lines 685-743; Note 1 CON also yields consolidation list)
category: notes_footnotes  grep_count: 3   sweep_count: 3   match: yes   (EBITDA* asterisk, EPS Not Annualised SA, EPS Not Annualised CON)
category: line_items       grep_count: 198   sweep_count: 198   match: yes   (fulltext pipe-row lines on table pages vs distinct source lines of structured NUMBER rows; SA P&L 23, SA BS 35, SA CF 32, SA Note9 4, CON P&L 27, CON BS 35, CON CF 33, CON Note9 4, press table 5)
category: zero_standing    grep_count: 41   sweep_count: 41   match: yes   (35 dash cells in fulltext table rows + 6 Annexure C 0.00 cells; structured ZERO_STANDING rows = 41)
category: agenda_items     grep_count: 3    sweep_count: 3    match: yes   (structured alone holds 2: R848, R849/R850; item 3 absent from structured, added as M1 below)
category: auditor_paras    grep_count: 10   sweep_count: 12   match: yes   (10 numbered: SA 1-4, CON 1-6; plus 2 unnumbered units: JV sub-paragraph of CON para 6 and the 'conclusion not modified' sentence; reconciled)
category: entities         grep_count: 2    sweep_count: 2    match: yes   (consolidation list: subsidiary + JV; auditor para 4 and CON Note 1 agree)
category: forward_stmts    grep_count: 10   sweep_count: 10   match: yes   (structured FORWARD table R790-R799)
category: id_accountability grep_count: 921 sweep_count: 921   match: yes
category: turns/questions/mgmt_numbers/slides   not applicable (results filing)
gate_a2: pass   (one MISSING_FROM_STRUCTURED row, M1, to loop back to A1; no count mismatch remains)
=== END COUNT TEST ===
```

## 1. BOARD OUTCOME LETTER: agenda items, timings, identifiers (pp1-2)  [18 ids]
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R848 | Agenda item 1: approval of standalone and consolidated unaudited results (Annexure A); press release Annexure B | - | xref R802,R899; Reg 33
R849 | Agenda item 2: Reg 32(1) confirmation, no IPO deviation | MGMT_STMT | xref R911-R918 Annexure C
R850 | Agenda item 2 cont.: Audit Committee and Board review of utilisation statement | MGMT_STMT | xref R803
R002,R804 | Board meeting start 3:30 PM, end 5:30 PM (2h00) | - | xref R801
R001,R003,R733 | Letter identifiers: BSE scrip code, CS membership no, NSE symbol | - | -
R731-R732,R734-R737 | Letter entities: addressees, regulatory basis, company, website, signatory | - | -
R800-R803 | Letter dates and periods | - | -
M1 (line 79, page 2) | Agenda item 3: 'Consideration and approval of other businesses as per agenda circulated.' | MISSING_FROM_STRUCTURED | A1 structured file holds no row for item 3; loop back to A1. No AR approval, AGM, dividend, director, auditor change, ESOP or fund-raise item appears in the letter.

## 2. SIGNATURE BLOCKS (CS timestamps, CMD, auditor, UDIN, DIN)  [31 ids]
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R805 | CS digital signature 2026.10.27 19:40:08; board concluded 17:30, signed 2h10m after close | - | not a pre-meeting signature; no flag
R775,R834,R837 | Press release covering letter: signed 19:40:49, letter date, signatory ACS-28167 | - | 41 s after results letter signature
R742-R744,R760-R762,R789 | CMD signatory entries on statement pages and Annexure C | - | -
R145,R216,R281,R489,R560,R627,R730 | DIN 06380254 numeric rows on signature lines | OCR_UNCERTAIN (R730 only) | fulltext line 1027 renders DIN as 08380254 (OCR); R730 holds 06380254, consistent with all other pages
R007,R327,R739,R757 | Auditor partner signatory, membership no 129033; consolidated name not legible | OCR_UNCERTAIN | R757 name illegible on consolidated report
R008,R328 | UDINs: standalone 26129033FRTGYW4104, consolidated 26129033ZUWUVF8909 | - | two distinct UDINs
R005-R006,R326,R809,R813,R822,R826 | Auditor LLP id, firm reg no, review report dates, board approval dates | OCR_UNCERTAIN (R005,R006) | R006 garbled; R326 gives clean 110758W/W100377

## 3. AUDITOR REVIEW REPORT PARAGRAPHS (SA pp3-4, CON pp10-11)  [25 ids]
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R738,R806-R807,R851 | SA para 1-2: addressee, reviewed statement, period, unreviewed comparatives caveat | UNREVIEWED_COMPARATIVE | Q2FY26 and H1FY26 comparatives not reviewed (R851); every YoY ratio rests on them
R004,R852 | SA para 3: SRE 2410 scope, no audit opinion | - | -
R853 | SA para 4: unmodified review conclusion | - | no Emphasis of Matter, no Other Matter, no going concern language (fulltext grep)
R753,R821,R873 | CON para 1-2: auditor, review period, unreviewed comparatives caveat | UNREVIEWED_COMPARATIVE | -
R319,R874-R875 | CON para 3: SRE 2410 scope, Reg 33(8) circular procedures | - | -
R754-R755 | CON para 4: entities reviewed (subsidiary, JV) | - | see ENTITIES_CONSOLIDATION
R878 | CON closing sentence: conclusion not modified despite other-auditor reliance | - | -
R320-R323,R756,R876 | CON para 6a: subsidiary interim results NOT reviewed by Talati; other auditor, name NOT DISCLOSED; total assets 122.40, revenue 122.33, PAT 15.58, TCI 16.04 (Rs m) | OTHER_AUDITOR_RELIANCE | other auditor report furnished by Management
R324-R325,R877 | CON para 6b: JV interim results NOT reviewed by Talati; share of net loss 26.15 | OTHER_AUDITOR_RELIANCE | 26.15 ties to CON P&L Q2FY27 JV share line

## 4a. CONSOLIDATION LIST  [4 ids]
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R765-R767,R890 | Consolidation list: Knack Packaging SA (RF) PTY Ltd (Subsidiary); Sayem Knack S.A. de C.V. (JV); consolidated Note 1 | RESTATED (also R754,R755) | no prior ledger, ENTITY_CHANGE not assessable; JV equity-method carrying value nil on CON balance sheet vs 45.59 on SA

## 4b. OTHER ENTITIES  [34 ids]
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R740-R741,R745-R746,R758-R759,R763-R764 | Company, CIN, registered office, product description, factory | RESTATED | standalone and consolidated mirrors
R747-R748,R750-R751,R768-R771 | JV counterparties and OFS sellers | RESTATED | Sacos Y Empaques: key strategic customer and original JV partner; Bessher Holding after 30-Dec-2025 transfer
R749,R752,R772,R785 | JV Sayem Knack; Borisana capex site | RESTATED | -
R773-R774,R776-R784 | Press release entities, speaker, IR agency | - | JV not named in press release (R778)
R786-R788 | Annexure C: listed entity, mode of fund raising, monitoring agency CARE Ratings | - | -

## 5a. NUMBERED NOTES (SA 1-9, CON 1-9)  [18 ids]
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R864-R872 | Standalone Notes 1-9 | RESTATED vs consolidated notes | Note 3 Labour Code 10.77 million; Note 6 JV; Note 7 IPO; Note 8 unreviewed comparatives
R889,R891-R898 | Consolidated Notes 1-9 (Note 1 list text R890 under ENTITIES_CONSOLIDATION) | RESTATED vs standalone notes | -

## 5b. UNNUMBERED NOTES AND FOOTNOTES  [4 ids]
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R901-R902 | EBITDA* footnote marker and definition: EBITDA includes Other Income | - | press release EBITDA margin includes other income 97.04 (CON)
R858,R883 | EPS (Not Annualised) qualifier, SA and CON | - | -

## 5c. NUMBERS EMBEDDED IN NOTES  [34 ids]
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R282-R298 | SA note-embedded numbers (Labour Code, JV stakes, IPO terms) | RESTATED vs R628-R644 | -
R628-R644 | CON note-embedded numbers | RESTATED vs R282-R298 | -

## 5d. DATES EMBEDDED IN NOTES  [14 ids]
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R814-R820,R827-R833 | Note-embedded dates (JV 28-Apr-2025, 6-Aug-2025, 30-Dec-2025; listing 8-Jul-2026; unreviewed comparatives) | RESTATED | -

## 6a. STATEMENT UNITS, AUDIT STATUS, PERIOD HEADERS, CROSS-STATEMENT DIFFERENCES  [24 ids]
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R854-R857,R859-R862,R879-R882,R884-R887 | Units, audit status of columns, exceptional item line, face value | - | FY26 column audited, all other columns unaudited; Rs million
R863,R888 | Cross-statement PBT differences 0.01 (SA CF 752.09 v P&L 752.08; CON CF H1FY26 557.67 v P&L 557.68) | SOURCE_AS_PRINTED | rounding level
R810-R812,R823-R825 | Reporting period headers | - | -

## 6b. LINE ITEMS IN EVERY FINANCIAL TABLE (one row per source line; ZERO_STANDING shown)  [640 ids]
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R009-R014 | SA P&L: Revenue from operations | - | line 187; 6 period cells
R015-R020 | SA P&L: Other Income | - | line 188; 6 period cells
R021-R026 | SA P&L: Total Income | - | line 189; 6 period cells
R027-R032 | SA P&L: Cost of materials consumed | - | line 191; 6 period cells
R033-R038 | SA P&L: Changes in inventories of finished goods and work-in-progress | - | line 192; 6 period cells
R039-R044 | SA P&L: Employee Benefits Expense | - | line 193; 6 period cells
R045-R050 | SA P&L: Finance Cost | - | line 194; 6 period cells
R051-R056 | SA P&L: Depreciation and Amortisation Expense | - | line 195; 6 period cells
R057-R062 | SA P&L: Other Expenses | - | line 196; 6 period cells
R063-R068 | SA P&L: Total Expenses | - | line 197; 6 period cells
R069-R074 | SA P&L: Profit before exceptional items and tax | - | line 198; 6 period cells
R075-R080 | SA P&L: Impact of Labour Codes | ZERO_STANDING | line 200; 6 period cells; 5 nil/dash cells R075-R079
R081-R086 | SA P&L: Profit before Tax | - | line 201; 6 period cells
R087-R092 | SA P&L: (a) Current Tax | - | line 203; 6 period cells
R093-R098 | SA P&L: (b) Deferred Tax | - | line 204; 6 period cells
R099-R104 | SA P&L: Total tax expenses (Net) | - | line 205; 6 period cells
R105-R110 | SA P&L: Net Profit for the period after tax | - | line 206; 6 period cells
R111-R116 | SA P&L: Items that will not be reclassified to profit or loss (net of tax) | - | line 208; 6 period cells
R117-R122 | SA P&L: Other comprehensive income/(loss) (net of tax) | - | line 209; 6 period cells
R123-R128 | SA P&L: Total comprehensive income (net of tax) | - | line 210; 6 period cells
R129-R135 | SA P&L: Paid-up Equity Share Capital (Face value Rs. 10/- per share) | - | line 211; 7 period cells
R136-R138 | SA P&L: Other Equity | - | line 212; 3 period cells
R139-R144 | SA P&L: Basic and Diluted Earnings per share | - | line 214; 6 period cells
R146-R147 | SA balance sheet: (a) Property, Plant and Equipment | - | line 231; 2 period cells
R148-R149 | SA balance sheet: (b) Other Intangible Assets | - | line 232; 2 period cells
R150-R151 | SA balance sheet: (c) Right-of-use Assets | - | line 233; 2 period cells
R152-R153 | SA balance sheet: (d) Investments accounted for using equity method | - | line 234; 2 period cells
R154-R155 | SA balance sheet: (e) Financial Assets: (i) Other Financial Assets | - | line 235; 2 period cells
R156-R157 | SA balance sheet: (f) Deferred Tax Assets (Net) | ZERO_STANDING | line 236; 2 period cells; 1 nil/dash cells R157
R158-R159 | SA balance sheet: (g) Other Non-current Assets | - | line 237; 2 period cells
R160-R161 | SA balance sheet: Total Non-current Assets | - | line 238; 2 period cells
R162-R163 | SA balance sheet: (a) Inventories | - | line 240; 2 period cells
R164-R165 | SA balance sheet: (b) Financial Assets: (i) Trade Receivables | - | line 241; 2 period cells
R166-R167 | SA balance sheet: (b) Financial Assets: (ii) Cash and Cash Equivalents | - | line 242; 2 period cells
R168-R169 | SA balance sheet: (b) Financial Assets: (iii) Other balances with banks | - | line 243; 2 period cells
R170-R171 | SA balance sheet: (b) Financial Assets: (iv) Loans | - | line 244; 2 period cells
R172-R173 | SA balance sheet: (b) Financial Assets: (v) Other Financial Assets | - | line 245; 2 period cells
R174-R175 | SA balance sheet: (c) Other Current Assets | - | line 246; 2 period cells
R176-R177 | SA balance sheet: Total Current Assets | - | line 247; 2 period cells
R178-R179 | SA balance sheet: TOTAL ASSETS | - | line 248; 2 period cells
R180-R181 | SA balance sheet: (a) Equity Share Capital | - | line 251; 2 period cells
R182-R183 | SA balance sheet: (b) Other Equity | - | line 252; 2 period cells
R184-R185 | SA balance sheet: Total Equity | - | line 253; 2 period cells
R186-R187 | SA balance sheet: (a) Financial Liabilities: (i) Borrowings | - | line 256; 2 period cells
R188-R189 | SA balance sheet: (a) Financial Liabilities: (ii) Lease Liabilities | - | line 257; 2 period cells
R190-R191 | SA balance sheet: (b) Deferred Tax Liabilities (Net) | ZERO_STANDING | line 258; 2 period cells; 1 nil/dash cells R190
R192-R193 | SA balance sheet: (c) Provisions | ZERO_STANDING | line 259; 2 period cells; 1 nil/dash cells R193
R194-R195 | SA balance sheet: Total Non-current Liabilities | - | line 260; 2 period cells
R196-R197 | SA balance sheet: (a) Financial Liabilities: (i) Borrowings | - | line 262; 2 period cells
R198-R199 | SA balance sheet: (a) Financial Liabilities: (ii) Lease Liabilities | - | line 263; 2 period cells
R200-R201 | SA balance sheet: (a) Financial Liabilities: (iii) Trade Payables - dues of micro and sm | - | line 264; 2 period cells
R202-R203 | SA balance sheet: (a) Financial Liabilities: (iii) Trade Payables - dues of creditors ot | - | line 265; 2 period cells
R204-R205 | SA balance sheet: (a) Financial Liabilities: (iv) Other Financial Liabilities | - | line 266; 2 period cells
R206-R207 | SA balance sheet: (b) Other Current Liabilities | - | line 267; 2 period cells
R208-R209 | SA balance sheet: (c) Provisions | - | line 268; 2 period cells
R210-R211 | SA balance sheet: (d) Current Tax Liabilities | - | line 269; 2 period cells
R212-R213 | SA balance sheet: Total Current Liabilities | - | line 270; 2 period cells
R214-R215 | SA balance sheet: TOTAL EQUITY AND LIABILITIES | - | line 271; 2 period cells
R217-R218 | SA cash flow: Profit before tax | - | line 286; 2 period cells
R219-R220 | SA cash flow: Interest income | - | line 288; 2 period cells
R221-R222 | SA cash flow: Net (gain)/loss on sale of Property, Plant & Equipment | - | line 289; 2 period cells
R223-R224 | SA cash flow: Unrealised foreign exchange differences (net) | - | line 290; 2 period cells
R225-R226 | SA cash flow: Expected credit loss (net) | - | line 291; 2 period cells
R227-R228 | SA cash flow: Depreciation and amortisation expense | - | line 292; 2 period cells
R229-R230 | SA cash flow: Finance cost | - | line 293; 2 period cells
R231-R232 | SA cash flow: Operating profit before working capital changes | - | line 294; 2 period cells
R233-R234 | SA cash flow: Inventories | - | line 296; 2 period cells
R235-R236 | SA cash flow: Trade and other receivables | - | line 297; 2 period cells
R237-R238 | SA cash flow: Trade and other payables | - | line 298; 2 period cells
R239-R240 | SA cash flow: Cash generated from operating activities | - | line 299; 2 period cells
R241-R242 | SA cash flow: Income tax payment (net) | - | line 300; 2 period cells
R243-R244 | SA cash flow: Net cash generated from operating activities | - | line 301; 2 period cells
R245-R246 | SA cash flow: Payments for property, plant and equipment | - | line 303; 2 period cells
R247-R248 | SA cash flow: Proceed from sale of property, plant and equipment | - | line 304; 2 period cells
R249-R250 | SA cash flow: Purchase of equity investment measured at cost | ZERO_STANDING | line 305; 2 period cells; 1 nil/dash cells R249
R251-R252 | SA cash flow: Investment in FD | ZERO_STANDING | line 306; 2 period cells; 1 nil/dash cells R252
R253-R254 | SA cash flow: Loan (given) / received back (net) | - | line 307; 2 period cells
R255-R256 | SA cash flow: Interest income | - | line 308; 2 period cells
R257-R258 | SA cash flow: Net cash (used in) investing activities | - | line 309; 2 period cells
R259-R260 | SA cash flow: Proceed from long term borrowings | ZERO_STANDING | line 311; 2 period cells; 1 nil/dash cells R259
R261-R262 | SA cash flow: Repayment of long term borrowings | - | line 312; 2 period cells
R263-R264 | SA cash flow: Proceeds from issue of share capital | ZERO_STANDING | line 313; 2 period cells; 1 nil/dash cells R264
R265-R266 | SA cash flow: Share Issue Expense (net of tax) | ZERO_STANDING | line 314; 2 period cells; 1 nil/dash cells R266
R267-R268 | SA cash flow: Proceed from short term borrowings (net) | - | line 315; 2 period cells
R269-R270 | SA cash flow: Payment of lease liabilities | - | line 316; 2 period cells
R271-R272 | SA cash flow: Interest paid | - | line 317; 2 period cells
R273-R274 | SA cash flow: Net cash generated / (used in) from financing activities | - | line 318; 2 period cells
R275-R276 | SA cash flow: Net increase / (decrease) in cash and cash equivalents | - | line 319; 2 period cells
R277-R278 | SA cash flow: Cash and cash equivalents at the beginning of the period | - | line 320; 2 period cells
R279-R280 | SA cash flow: Cash and cash equivalents at the end of the period | - | line 321; 2 period cells
R299-R303 | SA Note 9 IPO utilisation: 1. Partial funding of capital expenditure towards setting up of new ma | ZERO_STANDING | line 404; 5 period cells; 1 nil/dash cells R300
R304-R308 | SA Note 9 IPO utilisation: 2. General Corporate Purposes | ZERO_STANDING | line 405; 5 period cells; 1 nil/dash cells R305
R309-R313 | SA Note 9 IPO utilisation: 3. Issue Expenses | ZERO_STANDING | line 406; 5 period cells; 1 nil/dash cells R310
R314-R318 | SA Note 9 IPO utilisation: Total | ZERO_STANDING | line 407; 5 period cells; 1 nil/dash cells R315
R329-R334 | CON P&L: Revenue from operations | - | line 526; 6 period cells
R335-R340 | CON P&L: Other Income | - | line 527; 6 period cells
R341-R346 | CON P&L: Total Income | - | line 528; 6 period cells
R347-R352 | CON P&L: Cost of materials consumed | - | line 530; 6 period cells
R353-R358 | CON P&L: Purchase of stock-in-trade | - | line 531; 6 period cells
R359-R364 | CON P&L: Changes in inventories of finished goods, work-in-progress and Stock-i | - | line 532; 6 period cells
R365-R370 | CON P&L: Employee Benefits Expense | - | line 533; 6 period cells
R371-R376 | CON P&L: Finance Cost | - | line 534; 6 period cells
R377-R382 | CON P&L: Depreciation and Amortisation Expense | - | line 535; 6 period cells
R383-R388 | CON P&L: Other Expenses | - | line 536; 6 period cells
R389-R394 | CON P&L: Total Expenses | - | line 537; 6 period cells
R395-R400 | CON P&L: Profit before exceptional items and tax | - | line 538; 6 period cells
R401-R406 | CON P&L: Impact of Labour Codes | ZERO_STANDING | line 540; 6 period cells; 5 nil/dash cells R401-R405
R407-R412 | CON P&L: Profit before profit of joint venture and tax | - | line 541; 6 period cells
R413-R418 | CON P&L: Share of profit/(loss) of joint venture, net of tax | - | line 542; 6 period cells
R419-R424 | CON P&L: Profit before Tax | - | line 543; 6 period cells
R425-R430 | CON P&L: (a) Current Tax | - | line 545; 6 period cells
R431-R436 | CON P&L: (b) Deferred Tax | - | line 546; 6 period cells
R437-R442 | CON P&L: Total tax expenses (Net) | - | line 547; 6 period cells
R443-R448 | CON P&L: Net Profit for the period after tax | - | line 548; 6 period cells
R449-R454 | CON P&L: Items that will not be reclassified to profit or loss (net of tax) | - | line 550; 6 period cells
R455-R460 | CON P&L: Items that will be reclassified to profit or loss (net of tax) | - | line 551; 6 period cells
R461-R466 | CON P&L: Other Comprehensive Income/(loss) (net of tax) | - | line 552; 6 period cells
R467-R472 | CON P&L: Total Comprehensive Income (net of tax) | - | line 553; 6 period cells
R473-R479 | CON P&L: Paid-up Equity Share Capital (Face value Rs. 10/- per share) | - | line 554; 7 period cells
R480-R482 | CON P&L: Other Equity | - | line 555; 3 period cells
R483-R488 | CON P&L: Basic and Diluted Earnings per share | - | line 557; 6 period cells
R490-R491 | CON balance sheet: (a) Property, Plant and Equipment | - | line 574; 2 period cells
R492-R493 | CON balance sheet: (b) Other Intangible Assets | - | line 575; 2 period cells
R494-R495 | CON balance sheet: (c) Right-of-use Assets | - | line 576; 2 period cells
R496-R497 | CON balance sheet: (d) Investments accounted for using equity method | ZERO_STANDING | line 577; 2 period cells; 1 nil/dash cells R496
R498-R499 | CON balance sheet: (e) Financial Assets: (i) Other Financial Assets | - | line 578; 2 period cells
R500-R501 | CON balance sheet: (f) Deferred Tax Assets (Net) | ZERO_STANDING | line 579; 2 period cells; 1 nil/dash cells R501
R502-R503 | CON balance sheet: (g) Other Non-current Assets | - | line 580; 2 period cells
R504-R505 | CON balance sheet: Total Non-current Assets | - | line 581; 2 period cells
R506-R507 | CON balance sheet: (a) Inventories | - | line 583; 2 period cells
R508-R509 | CON balance sheet: (b) Financial Assets: (i) Trade Receivables | - | line 584; 2 period cells
R510-R511 | CON balance sheet: (b) Financial Assets: (ii) Cash and Cash Equivalents | - | line 585; 2 period cells
R512-R513 | CON balance sheet: (b) Financial Assets: (iii) Other balances with banks | - | line 586; 2 period cells
R514-R515 | CON balance sheet: (b) Financial Assets: (iv) Loans | - | line 587; 2 period cells
R516-R517 | CON balance sheet: (b) Financial Assets: (v) Other Financial Assets | - | line 588; 2 period cells
R518-R519 | CON balance sheet: (c) Other Current Assets | - | line 589; 2 period cells
R520-R521 | CON balance sheet: Total Current Assets | - | line 590; 2 period cells
R522-R523 | CON balance sheet: TOTAL ASSETS | - | line 591; 2 period cells
R524-R525 | CON balance sheet: (a) Equity Share Capital | - | line 594; 2 period cells
R526-R527 | CON balance sheet: (b) Other Equity | - | line 595; 2 period cells
R528-R529 | CON balance sheet: Total Equity | - | line 596; 2 period cells
R530-R531 | CON balance sheet: (a) Financial Liabilities: (i) Borrowings | - | line 599; 2 period cells
R532-R533 | CON balance sheet: (a) Financial Liabilities: (ii) Lease Liabilities | - | line 600; 2 period cells
R534-R535 | CON balance sheet: (b) Deferred Tax Liabilities (Net) | ZERO_STANDING | line 601; 2 period cells; 1 nil/dash cells R534
R536-R537 | CON balance sheet: (c) Provisions | ZERO_STANDING | line 602; 2 period cells; 1 nil/dash cells R537
R538-R539 | CON balance sheet: Total Non-current Liabilities | - | line 603; 2 period cells
R540-R541 | CON balance sheet: (a) Financial Liabilities: (i) Borrowings | - | line 605; 2 period cells
R542-R543 | CON balance sheet: (a) Financial Liabilities: (ii) Lease Liabilities | - | line 606; 2 period cells
R544-R545 | CON balance sheet: (a) Financial Liabilities: (iii) Trade Payables - dues of micro and sm | - | line 607; 2 period cells
R546-R547 | CON balance sheet: (a) Financial Liabilities: (iii) Trade Payables - dues of creditors ot | - | line 608; 2 period cells
R548-R549 | CON balance sheet: (a) Financial Liabilities: (iv) Other Financial Liabilities | - | line 609; 2 period cells
R550-R551 | CON balance sheet: (b) Other Current Liabilities | - | line 610; 2 period cells
R552-R553 | CON balance sheet: (c) Provisions | - | line 611; 2 period cells
R554-R555 | CON balance sheet: (d) Current Tax Liabilities | - | line 612; 2 period cells
R556-R557 | CON balance sheet: Total Current Liabilities | - | line 613; 2 period cells
R558-R559 | CON balance sheet: TOTAL EQUITY AND LIABILITIES | - | line 614; 2 period cells
R561-R562 | CON cash flow: Profit before tax | - | line 629; 2 period cells
R563-R564 | CON cash flow: Interest income | - | line 631; 2 period cells
R565-R566 | CON cash flow: Share of (profit)/ loss of Joint Venture (net of tax) | - | line 632; 2 period cells
R567-R568 | CON cash flow: Net (gain)/loss on sale of Property, Plant & Equipment | - | line 633; 2 period cells
R569-R570 | CON cash flow: Unrealised foreign exchange differences (net) | - | line 634; 2 period cells
R571-R572 | CON cash flow: Expected credit loss | - | line 635; 2 period cells
R573-R574 | CON cash flow: Depreciation and amortisation expense | - | line 636; 2 period cells
R575-R576 | CON cash flow: Finance cost | - | line 637; 2 period cells
R577-R578 | CON cash flow: Operating profit before working capital changes | - | line 638; 2 period cells
R579-R580 | CON cash flow: Inventories | - | line 640; 2 period cells
R581-R582 | CON cash flow: Trade and other receivables | - | line 641; 2 period cells
R583-R584 | CON cash flow: Trade and other payables | - | line 642; 2 period cells
R585-R586 | CON cash flow: Cash generated from operating activities | - | line 643; 2 period cells
R587-R588 | CON cash flow: Income tax payment (net) | - | line 644; 2 period cells
R589-R590 | CON cash flow: Net cash generated from operating activities | - | line 645; 2 period cells
R591-R592 | CON cash flow: Payments for property, plant and equipment | - | line 647; 2 period cells
R593-R594 | CON cash flow: Proceed from sale of property, plant and equipment | - | line 648; 2 period cells
R595-R596 | CON cash flow: Purchase of equity investment measured at cost | ZERO_STANDING | line 649; 2 period cells; 1 nil/dash cells R595
R597-R598 | CON cash flow: Investment in FD | ZERO_STANDING | line 650; 2 period cells; 1 nil/dash cells R598
R599-R600 | CON cash flow: Loan (given) / received back (net) | - | line 651; 2 period cells
R601-R602 | CON cash flow: Interest income | - | line 652; 2 period cells
R603-R604 | CON cash flow: Net cash (used in) investing activities | - | line 653; 2 period cells
R605-R606 | CON cash flow: Proceed from long term borrowings | ZERO_STANDING | line 655; 2 period cells; 1 nil/dash cells R605
R607-R608 | CON cash flow: Repayment of long term borrowings | - | line 656; 2 period cells
R609-R610 | CON cash flow: Proceeds from issue of share capital | ZERO_STANDING | line 657; 2 period cells; 1 nil/dash cells R610
R611-R612 | CON cash flow: Share Issue Expense (net of tax) | ZERO_STANDING | line 658; 2 period cells; 1 nil/dash cells R612
R613-R614 | CON cash flow: Proceed from short term borrowings (net) | - | line 659; 2 period cells
R615-R616 | CON cash flow: Payment of lease liabilities | - | line 660; 2 period cells
R617-R618 | CON cash flow: Interest paid | - | line 661; 2 period cells
R619-R620 | CON cash flow: Net cash generated / (used in) from financing activities | - | line 662; 2 period cells
R621-R622 | CON cash flow: Net increase / (decrease) in cash and cash equivalents | - | line 663; 2 period cells
R623-R624 | CON cash flow: Cash and cash equivalents at the beginning of the period | - | line 664; 2 period cells
R625-R626 | CON cash flow: Cash and cash equivalents at the end of the period | - | line 665; 2 period cells
R645-R649 | CON Note 9 IPO utilisation: 1. Partial funding of capital expenditure towards setting up of new ma | ZERO_STANDING | line 747; 5 period cells; 1 nil/dash cells R646
R650-R654 | CON Note 9 IPO utilisation: 2. General Corporate Purposes | ZERO_STANDING | line 748; 5 period cells; 1 nil/dash cells R651
R655-R659 | CON Note 9 IPO utilisation: 3. Issue Expenses | ZERO_STANDING | line 749; 5 period cells; 1 nil/dash cells R656
R660-R664 | CON Note 9 IPO utilisation: Total | ZERO_STANDING | line 750; 5 period cells; 1 nil/dash cells R661
R668-R675 | Press release highlights table: Revenue from Operations | - | line 817; 8 period cells
R676-R683 | Press release highlights table: Total EBITDA* | - | line 818; 8 period cells
R684-R688 | Press release highlights table: EBITDA Margin (%) | - | line 819; 5 period cells
R689-R696 | Press release highlights table: PAT | - | line 820; 8 period cells
R697-R701 | Press release highlights table: PAT Margin (%) | - | line 821; 5 period cells

## 7a. ANNEXURE C (IPO deviation statement, pp20-21)  [25 ids]
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R716-R729 | Annexure C object table: allocation, modified allocation, funds utilised, deviation | ZERO_STANDING (6 cells: modified allocation, deviation x3 objects) | Borisana capex utilised 7.04 of 3,200.00
R911-R921 | Annexure C text fields: deviation No, monitoring agency, audit committee comment, project recently commenced, definition | MGMT_STMT (R916,R920) | -

## 7b. ANNEXURE B PRESS RELEASE NUMBERS (pp17-19)  [17 ids]
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R667,R702,R704,R706,R708 | Headline/narrative restatements of table figures: revenue +52.52%, PAT +21.24%, EBITDA margin 16.35%, PAT margin 8.22% | RESTATED | ties to highlights table lines 817-821
R665-R666 | Press release letter identifiers | - | -
R703,R705,R707,R709-R715 | Prose numbers: headline revenue, PAT, 75 countries, JV loss 60.60 Mn, H1 growth, 28 sectors, IR phones | - | JV loss 60.60 ties to CON P&L H1FY27 JV line

## 7c. PRESS RELEASE MANAGEMENT STATEMENTS AND DISCLAIMER  [10 ids]
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R899-R900,R903-R910 | Management statements, annexure heading, table unit, safe harbour | MGMT_STMT | R906 'highest ever quarterly revenue'

## 8. FORWARD-LOOKING STATEMENTS  [10 ids]
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R790-R799 | Forward statements: Labour Code (2), price pass-through from Q3FY27, JV breakeven reversal, price revision benefits, priorities, Borisana fund utilisation | FORWARD | R793/R794 conditional on JV breakeven, no date; R792 'subject to market stabilization'

## 9. REMAINING DATES  [13 ids]
ROW_ID(s) | category | A2 flags | cross-ref / materiality
R808,R835-R836,R838-R847 | Letterhead years, press release periods, IPO allotment date 6-Jul-2026 | - | -

## ZERO_STANDING REGISTER (41 rows)
SA P&L Impact of Labour Codes Q2FY27/Q1FY27/Q2FY26/H1FY27/H1FY26 nil: R075-R079 | SA BS: R157, R190, R193 | SA CF: R249, R252, R259, R264, R266 | SA Note 9: R300, R305, R310, R315 | CON P&L Labour Codes: R401-R405 | CON BS: R496, R501 (JV equity-method investment nil at 30-Sep-2026 v 34.55), R534, R537 | CON CF: R595, R598, R605, R610, R612 | CON Note 9: R646, R651, R656, R661 | Annexure C: R719, R721, R723, R725, R727, R729. Total 41.

## RAISED FLAG TOTALS
ZERO_STANDING 41 | MISSING_FROM_STRUCTURED 1 (M1) | RESTATED (SA/CON mirrors, Notes, press vs table) | OTHER_AUDITOR_RELIANCE 2 units (subsidiary, JV) | UNREVIEWED_COMPARATIVE 2 (R851, R873) | SOURCE_AS_PRINTED 2 (R863, R888) | OCR_UNCERTAIN 4 (R005, R006, R730 DIN, R757) | MGMT_STMT rows per structured | ENTITY_CHANGE 0 (no prior ledger) | DROPPED_SLIDE, REPEAT_QUESTION, MGMT_ABSENCE not applicable

```yaml
stage: A2-enumerator
company: "KNACK"
quarter: "q2fy27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/knack-q2fy27/work/ledger_results_knack_q2fy27.md"
counts:
  notes: 21
  line_items: 198
  zero_standing: 41
  agenda_items: 3
  auditor_paras: 12
  entities: 2
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, MISSING_FROM_STRUCTURED, RESTATED, OTHER_AUDITOR_RELIANCE, UNREVIEWED_COMPARATIVE, SOURCE_AS_PRINTED, OCR_UNCERTAIN]
ids_in_structured: 921
ids_referenced: 921
orphan_ids: []
missing_from_structured: ["M1: Board agenda item 3 'Consideration and approval of other businesses as per agenda circulated' (page 2, line 79)"]
gate_a2: pass
mismatch_note: ""
analyst_note: "Only miss: agenda item 3 (other businesses) lacks a structured row; ledger row M1 carries it, A1 should add it. Notes count is 21 = 18 numbered (SA 1-9, CON 1-9) + 3 footnotes. Two Rs-million comparatives are unreviewed (Q2FY26, H1FY26), so every YoY figure rests on unreviewed numbers. Subsidiary and JV were reviewed by an unnamed other auditor. The JV equity-method investment is nil on the consolidated balance sheet at 30-Sep-2026 (34.55 at March 2026) and shows 45.59 standalone; this is a ZERO_STANDING row (R496) A3 should read with the JV loss lines. Annexure C shows 6 zero cells (no deviation). Borisana capex used 7.04 of 3,200.00. No prior ledger, so ENTITY_CHANGE could not be tested. Press release EBITDA margin includes other income (R902). Signature timestamps (19:40) follow the 17:30 meeting close, no flag."
```
