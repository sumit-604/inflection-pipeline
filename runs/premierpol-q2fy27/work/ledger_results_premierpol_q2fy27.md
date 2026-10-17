=== A2 COUNT TEST (CORRECTION LOOP 1, A5-M1) ===
category: notes          grep_count: 5    sweep_count: 5    match: yes   (Note 1-5 R379-R383; plus 1 unnumbered note R384)
category: line_items     structured_only: 96   additions: 9 (X001,X003,X005,X006,X007,X009,X010,X011,X012; section 10A)   ledger_total: 105   fulltext_recount: 105   match: yes
                         (cells: structured 310 + 27 additions = 337)
category: zero_standing  structured_only: 23   additions: 26   ledger_total: 49   fulltext_recount: 49   match: yes
                         (plus 1 unexplained numeric token "2" at fulltext L96, X003, not counted as zero: no total uses it; reads as OCR of dash)
category: agenda_items   grep_count: 1    sweep_count: 1    match: yes   (results only, R365)
category: auditor_paras  grep_count: 5    sweep_count: 5    match: yes   (R396-R400)
category: entities       grep_count: 23   sweep_count: 23   match: yes   (R320-R342; no consolidation list, Note 5)
category: date_units     grep_count: 19   sweep_count: 19   match: yes   (R343-R361)
category: qualifiers     structured_only: 40   additions: 2 blank rows (X004 L94, X013 L128)   ledger_total: 42   fulltext_recount: 42   match: yes
category: footnote_unresolved grep_count: 4 sweep_count: 4 match: yes (R364,R372,R377,R401)
ids_in_structured: 401 | ids_referenced_in_ledger: 401 | orphan_ids: [] | match: yes
ledger_only_ids (MISSING_FROM_STRUCTURED): 12 rows X001-X012 (own fulltext line)
gate_a2: pass
=== END COUNT TEST ===

# LEDGER: PREMIERPOL Q2 FY27 results (A2 enumerator)
Row format: ROW_ID | category | A2 flags | cross-ref / materiality. Claim text stays in A1 structured file at that ID.

## 1. Line items (financial tables). One row per line item; IDs carry page and line.
| line item | page | IDs | n | flags | note |
|---|---|---|---|---|---|
| Revenue from Operations (Inclusive of GST) | page 2 | R001..R006 (6) | 6 |  | |
| Other Operating Income | page 2 | R007..R012 (6) | 6 | OCR_AS_READ | |
| TOTAL INCOME | page 2 | R013..R018 (6) | 6 |  | |
| Cost of materials consumed | page 2 | R019..R024 (6) | 6 |  | |
| Purchases of stock-in-trade | page 2 | R025..R030 (6) | 6 |  | |
| Change in inventories of FG, WIP, stock-in-trade | page 2 | R031..R036 (6) | 6 |  | |
| Employee benefits expense | page 2 | R037..R042 (6) | 6 |  | |
| Finance Costs | page 2 | R043..R048 (6) | 6 | OCR_UNREADABLE | |
| Depreciation and amortisation expense | page 2 | R049..R054 (6) | 6 |  | |
| Other expenses: GST | page 2 | R055..R060 (6) | 6 | OCR_AS_READ | |
| Other Expenses (other items) | page 2 | R061..R066 (6) | 6 |  | |
| TOTAL OTHER EXPENSES | page 2 | R067..R072 (6) | 6 |  | |
| TOTAL EXPENSES | page 2 | R073..R078 (6) | 6 |  | |
| Total Profit before Exceptional Items & Tax | page 2 | R079..R084 (6) | 6 |  | |
| Total Profit before Tax | page 2 | R085..R090 (6) | 6 |  | |
| Current Tax | page 2 | R091..R096 (6) | 6 |  | |
| Deferred Tax | page 2 | R097..R098 (2) | 2 | ZERO_STANDING | Q2FY27 nil; only Q2FY27 and FY26 populated in A1 |
| Total tax expenses | page 2 | R099..R104 (6) | 6 |  | |
| Net Profit from continuing Operations | page 2 | R105..R110 (6) | 6 |  | |
| Profit/(loss) from discontinued Operations before tax | page 2 | R111..R116 (6) | 6 | ZERO_STANDING | |
| Total Profit for the period | page 2 | R117..R122 (6) | 6 |  | |
| Other comprehensive Income net of taxes | page 2 | R123..R128 (6) | 6 |  | |
| Total Comprehensive Income for the period | page 2 | R129..R134 (6) | 6 |  | |
| Paid-up Equity Share capital (Rs Lakhs) | page 3 | R135..R140 (6) | 6 |  | |
| Reserve excluding revaluation Reserves | page 3 | R141..R146 (6) | 6 |  | |
| Face Value (Rs) | page 3 | R147..R148 (2) | 2 |  | |
| Basic EPS continuing ops (Rs) | page 3 | R149..R154 (6) | 6 | OCR_AS_READ | |
| Diluted EPS continuing ops (Rs) | page 3 | R155..R160 (6) | 6 | OCR_AS_READ | |
| Basic EPS continuing and discontinued (Rs) | page 3 | R161..R166 (6) | 6 | OCR_AS_READ | |
| Diluted EPS continuing and discontinued (Rs) | page 3 | R167..R172 (6) | 6 | OCR_AS_READ | |
| Debt Equity Ratio (x) | page 3 | R173..R178 (6) | 6 |  | |
| DSCR (x) | page 3 | R179..R184 (6) | 6 |  | |
| ISCR (x) | page 3 | R185..R190 (6) | 6 |  | |
| CF Profit before tax | page 4 | R191..R192 (2) | 2 |  | |
| CF Adjustments for finance costs | page 4 | R193..R194 (2) | 2 |  | |
| CF Adj decrease(increase) trade receivables current | page 4 | R195..R196 (2) | 2 |  | |
| CF Adj decrease(increase) trade receivables non-current | page 4 | R197..R198 (2) | 2 | OCR_AS_READ | |
| CF Adj decrease(increase) other current assets | page 4 | R199..R200 (2) | 2 |  | |
| CF Total adjustments for reconcile profit(loss) | page 4 | R201..R201 (1) | 1 | PERIOD_COLUMN_UNRESOLVED | |
| CF Net cash flows from operations | page 4 | R202..R202 (1) | 1 | PERIOD_COLUMN_UNRESOLVED | |
| CF Income taxes paid (refund), operating | page 4 | R203..R203 (1) | 1 | PERIOD_COLUMN_UNRESOLVED | |
| CF Net cash flows from operating activities | page 4 | R204..R204 (1) | 1 | PERIOD_COLUMN_UNRESOLVED | |
| CF Proceeds from sales of PPE | page 4 | R205..R206 (2) | 2 |  | |
| CF Purchase of PPE | page 4 | R207..R208 (2) | 2 |  | |
| CF Dividends received (investing) | page 5 | R209..R210 (2) | 2 |  | |
| CF Interest received (investing) | page 5 | R211..R212 (2) | 2 |  | |
| CF Other inflows (outflows) investing | page 5 | R213..R214 (2) | 2 |  | |
| CF Net cash flows from investing activities | page 5 | R215..R216 (2) | 2 |  | |
| CF Repayments of borrowings | page 5 | R217..R217 (1) | 1 | PERIOD_COLUMN_UNRESOLVED | |
| CF Interest paid (financing) | page 5 | R218..R218 (1) | 1 | PERIOD_COLUMN_UNRESOLVED | |
| CF Net cash flows from financing activities | page 5 | R219..R220 (2) | 2 |  | |
| CF Net increase(decrease) in cash before FX | page 5 | R221..R222 (2) | 2 |  | |
| CF Cash and equivalents at beginning of period | page 5 | R223..R224 (2) | 2 |  | |
| CF Cash and equivalents at end of period | page 5 | R225..R226 (2) | 2 |  | |
| BS Property, Plant and equipment | page 6 | R227..R228 (2) | 2 |  | |
| BS Capital work-in-progress | page 6 | R229..R230 (2) | 2 |  | |
| BS Other intangible assets | page 6 | R231..R232 (2) | 2 |  | |
| BS Non current financial assets (subtotal) | page 6 | R233..R234 (2) | 2 | LABEL_MISALIGNED_OCR | |
| BS Non-current Investments | page 6 | R235..R236 (2) | 2 |  | |
| BS Trade receivables non current | page 6 | R237..R238 (2) | 2 | OCR_AS_READ,ZERO_STANDING | |
| BS Other non-current financial assets | page 6 | R239..R240 (2) | 2 |  | |
| BS Total non current financial assets | page 6 | R241..R242 (2) | 2 |  | |
| BS Deferred tax assets (net) | page 6 | R243..R244 (2) | 2 |  | |
| BS Other non-current assets | page 6 | R245..R246 (2) | 2 |  | |
| BS TOTAL NON CURRENT ASSETS | page 6 | R247..R248 (2) | 2 |  | |
| BS Inventories | page 6 | R249..R250 (2) | 2 |  | |
| BS Current investments | page 6 | R251..R252 (2) | 2 |  | |
| BS Trade receivables current | page 6 | R253..R254 (2) | 2 |  | |
| BS Cash and cash equivalents | page 6 | R255..R256 (2) | 2 |  | |
| BS Other current financial assets | page 6 | R257..R258 (2) | 2 |  | |
| BS Total current financial assets | page 6 | R259..R260 (2) | 2 |  | |
| BS Current tax assets (net) | page 6 | R261..R262 (2) | 2 | OCR_AS_READ,ZERO_STANDING | |
| BS Other current assets | page 6 | R263..R264 (2) | 2 |  | |
| BS TOTAL CURRENT ASSETS | page 6 | R265..R266 (2) | 2 |  | |
| BS Non current assets held for sale | page 6 | R267..R268 (2) | 2 | ZERO_STANDING | |
| BS TOTAL ASSETS | page 6 | R269..R270 (2) | 2 |  | |
| BS Equity Share Capital | page 6 | R271..R272 (2) | 2 |  | |
| BS Other Equity | page 6 | R273..R274 (2) | 2 |  | |
| BS TOTAL EQUITY | page 6 | R275..R276 (2) | 2 |  | |
| BS Borrowings non current | page 7 | R277..R278 (2) | 2 | ZERO_STANDING | |
| BS Trade payable non current | page 7 | R279..R280 (2) | 2 | ZERO_STANDING | |
| BS Other non current financial liabilities | page 7 | R281..R282 (2) | 2 | ZERO_STANDING | |
| BS Provisions non current | page 7 | R283..R284 (2) | 2 |  | |
| BS Deferred tax liabilities (net) | page 7 | R285..R286 (2) | 2 | LABEL_ON_PRIOR_LINE | |
| BS Other non current liabilities | page 7 | R287..R288 (2) | 2 | ZERO_STANDING | |
| BS TOTAL NON CURRENT LIABILITIES | page 7 | R289..R290 (2) | 2 | OCR_AMBIGUOUS | 6228 vs 603 prior; A3 to check against components |
| BS Borrowings current | page 7 | R291..R292 (2) | 2 | OCR_AS_READ,ZERO_STANDING | |
| BS Trade payable current | page 7 | R293..R294 (2) | 2 |  | |
| BS Other current financial liabilities | page 7 | R295..R296 (2) | 2 |  | |
| BS Total current financial liabilities | page 7 | R297..R298 (2) | 2 |  | |
| BS Other current liabilities | page 7 | R299..R300 (2) | 2 |  | |
| BS Provisions current | page 7 | R301..R302 (2) | 2 |  | |
| BS Current tax liabilities (net) | page 7 | R303..R304 (2) | 2 |  | |
| BS TOTAL CURRENT LIABILITIES | page 7 | R305..R306 (2) | 2 |  | |
| BS TOTAL LIABILITIES | page 7 | R307..R308 (2) | 2 |  | |
| BS TOTAL EQUITY AND LIABILITIES | page 7 | R309..R310 (2) | 2 |  | |

Cross-refs (RESTATED): Net profit R105-R110 = Total profit R117-R122; PBT R079-R084 = R085-R090; BS Equity share capital R271/R272 = R135-R140 (1,059); BS Other Equity 31/03/2026 R274 (13,661) = Reserve excl. reval R141/R142/R144 (13,661, repeated across Q2FY27, Q1FY27, H1FY27 columns while FY26 R146 shows 10,728; column misread or restatement, A3 check); BS cash R255/R256 = CF closing/opening R225/R226 (690/504); BS TOTAL ASSETS R269/R270 = TOTAL E&L R309/R310.
Observations (no interpretation): Debt/equity R173-R178 non-zero while BS borrowings R277,R278,R291,R292 are nil/dash. Deferred tax P&L Q2FY27 nil R097 while BS DTA/DTL R243-R244, R285-R286 are non-nil. Revenue is GST-inclusive (R369) with GST shown within expenses (R370, R055-R060).

## 2. Zero-standing items (23 cells, 13 line items), flag ZERO_STANDING
R097 Deferred Tax Q2FY27
R111-R116 Discontinued ops PBT, all 6 periods (template line, all nil)
R237,R238 Trade receivables non current (R237 OCR '=')
R261,R262 Current tax assets (net)
R267,R268 Non current assets held for sale
R277,R278 Borrowings non current
R279,R280 Trade payable non current
R281,R282 Other non current financial liabilities
R287,R288 Other non current liabilities
R291,R292 Borrowings current (R291 OCR ':')
Blank-in-source rows (A1): regulatory deferral balances R373, owners/NCI attribution R376, CF applicability R388.

## 3. Identifiers and meeting times (R311-R319)
R311 BSE scrip | identifier
R312 CIN p1 | identifier | cross-ref R314 (p2 CIN reads 152109 vs L52109; flag CIN_OCR_MISMATCH)
R313 telephone | identifier
R314 CIN p2 | identifier | see R312
R315 auditor membership no. | identifier
R316 UDIN | identifier | garbled, UDIN_UNRESOLVED
R317 MD DIN | identifier | cross-ref R333
R318 meeting commenced 13.30 Hrs | board timing | cross-ref R319, R347
R319 meeting terminated 14.30 Hrs | board timing | 60-minute meeting

## 4. Notes
Note 1 R379 | Note 2 R380 | Note 3 R381 | Note 4 R382 | Note 5 R383 (no subsidiary/associate/JV; ties to entities section)
Header R378 | Unnumbered website note R384
Footnote markers with no footnote: R364 (results link missing), R372, R377, R401 | FOOTNOTE_UNRESOLVED
OCR note R389 (unclosed parenthesis, ties R198)

## 5. Agenda items (Board Outcome letter)
Item 1: standalone unaudited results R365 | cross-ref R345 (intimation 03-10-2026), R346 (meeting 10-10-2026), R347 (13.30-14.30), R343 letter date
No other agenda items (dividend, AR, AGM, appointments, auditor change, ESOP, capital raise) in structured file. Single-item agenda.

## 6. Auditor report paragraphs (limited review)
R396 title/scope: Limited Review on unaudited standalone results (cross-ref R363); opinion type is limited review conclusion, not audit
R397 management responsibility
R398 review per SRE 2410 (cross-ref R341)
R399 conclusion fragment, no adverse text visible; fragmentary OCR
R400 paragraphs 3-4 garbled | OCR_GARBLED | no Emphasis of Matter, Other Matter or Going Concern language visible; absence cannot be confirmed
Supporting: R338 ADV AND CO LLP, R342 ICAI, R315 membership no., R316 UDIN garbled, R361 report date 10-10-2026, R340 Ind AS 34, R339 LODR Reg 33
Entities reviewed: standalone only; no unaudited or management-furnished component entities (Note 5).

## 7. Entities (R320-R342, 23); no ENTITY_CHANGE testable (no prior ledger, no consolidation)
R320 reporting company | R321 BSE | R322 NSE | R323 scrip | R324 CS Heena Soni | R325 auditor ref | R326 factory | R327-R330 products (4) | R331 registered office | R332 main business | R333 MD & CEO Amitaabh Goenka | R334 Ind AS rules | R335 Companies Act s133 | R336 Audit Committee | R337 Board | R338 ADV AND CO LLP | R339 LODR Reg 33 | R340 Ind AS 34 | R341 SRE 2410 | R342 ICAI
Note: four products R327-R330 vs Note 3 R381 single business product.

## 8. Signature blocks
R333 signatory MD & CEO, DIN R317, signing date R353 (10-10-2026); R356 CF signing date; R359 BS signing date; R361 auditor date. No clock timestamps in structured file; all dates equal board date R346/R352, so signature-before-meeting is not testable.

## 9. Dates (R343-R361, 19)
R343,R344,R345,R346,R347,R348,R349,R350,R351 (reads 32-03-2026, OCR for 31-03-2026),R352,R353,R354,R355,R356,R357,R358,R359,R360,R361

## 10. Qualifiers (R362-R401, 40)
Unaudited / limited review: R362,R363,R366,R368,R375,R385,R387,R391,R393,R396
Basis, format, units: R365,R367,R369,R370,R371,R374,R386,R392,R394
Blank or absent: R373,R376,R388,R390 (most CF rows lack values in text layer),R395
Notes / website: R378-R384
OCR: R389,R400
Footnote unresolved: R364,R372,R377,R401
Auditor: R397,R398,R399
Forward-looking statements: none (A1 FORWARD = 0).

## 10A. MISSING_FROM_STRUCTURED additions (A5-M1, loop 1). Fulltext line numbers are the numbered prefixes in extracted/premierpol-results-q2fy27-fulltext.md. These rows carry claim text because the structured file lacks them.
| ID | fulltext line | page | label / tokens as read | cells | flags | note |
|---|---|---|---|---|---|---|
| X001 | L86 | page 2 | (g) Other Expenses, header row: "-", "-" | 2 | MISSING_FROM_STRUCTURED, ZERO_STANDING | nil header cells; follows GST / Other Expenses rows R055-R060 and sub-items |
| X002 | L94 | page 2 | 4 Exceptional Items: no values (blank row) | 0 | MISSING_FROM_STRUCTURED, BLANK_IN_SOURCE | blank standing line; A4 relies on this row by fulltext reading; qualifier |
| X003 | L96 | page 2 | 6 Tax Expenses, header row: "2", "-" | 2 | MISSING_FROM_STRUCTURED, ZERO_STANDING (the "-" cell), OCR_AMBIGUOUS ("2") | "2" feeds no total (current tax = total tax in every interim column, L97 vs L99); reads as OCR of a dash |
| X004 | L98 | page 2 | Deferred Tax third token "-" (tokens "0", "-", "13"; "0" = R097, "13" = R098) | 1 | MISSING_FROM_STRUCTURED, ZERO_STANDING | cross-ref R097, R098; the uncaptured cell |
| X005 | L104 | page 2 | 13 Tax Expenses of discontinued Operations: "-" x5 | 5 | MISSING_FROM_STRUCTURED, ZERO_STANDING | template nil line; adjacent L103 captured as R111-R116 |
| X006 | L105 | page 2 | 14 Net Profit/(Loss) from discontinued Operations after tax: "-","-","-","f","“","=" | 6 | MISSING_FROM_STRUCTURED, ZERO_STANDING, OCR_AMBIGUOUS | nil; glyphs f, quote, = are OCR of dashes |
| X007 | L106 | page 2 | 15 Share of Profit/(Loss) of associates and JVs: "-","S","a","z","a" | 5 | MISSING_FROM_STRUCTURED, ZERO_STANDING, OCR_AMBIGUOUS | nil; letters are OCR glyphs; consistent with Note 5 (no subsidiary/associate/JV) R383 |
| X008 | L128 | page 3 | Details of debt securities: no values (blank row) | 0 | MISSING_FROM_STRUCTURED, BLANK_IN_SOURCE | qualifier; bears on F-01: no listed debt securities shown |
| X009 | L373 | page 7 | TOTAL NON CURRENT FINANCIAL LIABILITIES: ".", "‘i" | 2 | MISSING_FROM_STRUCTURED, ZERO_STANDING, OCR_AMBIGUOUS | nil subtotal; sits under Borrowings/Trade payable/Other NC financial liabilities R277-R282 (all nil); bears on F-01 |
| X010 | L377 | page 7 | Deferred government grants non current: "_" | 1 | MISSING_FROM_STRUCTURED, ZERO_STANDING | nil |
| X011 | L390 | page 7 | Deferred government grants, current: "us", "=" | 2 | MISSING_FROM_STRUCTURED, ZERO_STANDING, OCR_AMBIGUOUS | nil; OCR glyphs |
| X012 | L393 | page 7 | Liabilities in disposal group held for sale: "“" | 1 | MISSING_FROM_STRUCTURED, ZERO_STANDING, OCR_AMBIGUOUS | nil; label wraps from line above ("sale") |
Cell total: 2+0+2+1+5+6+5+0+2+1+2+1 = 27. Zero-standing cells added: 2+0+1+1+5+6+5+0+2+1+2+1 = 26 (X003 "2" excluded). Line items added: X001, X003, X005, X006, X007, X009, X010, X011, X012 = 9. Blank rows added to qualifiers: X002, X008 = 2.
The A5 table lists L98 as one extra cell, folded here as X004 (not a new line item). 12 rows X001-X012, one per named fulltext line.

## 11. Flags raised
ZERO_STANDING (49 cells: 23 structured + 26 MISSING_FROM_STRUCTURED), MISSING_FROM_STRUCTURED (12 rows X001-X012), BLANK_IN_SOURCE (X002, X008), FOOTNOTE_UNRESOLVED (4), OCR_UNREADABLE R046, PERIOD_COLUMN_UNRESOLVED (R201-R204, R217, R218), CIN_OCR_MISMATCH, UDIN_UNRESOLVED, OCR_AMBIGUOUS R289.

```yaml
stage: A2-enumerator
loop: 1
company: "PREMIERPOL"
quarter: "Q2 FY27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/premierpol-q2fy27/work/ledger_results_premierpol_q2fy27.md"
counts:
  notes: 5
  line_items: 105
  zero_standing: 49
  qualifiers: 42
  agenda_items: 1
  auditor_paras: 5
  entities: 23
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [MISSING_FROM_STRUCTURED, BLANK_IN_SOURCE, ZERO_STANDING, FOOTNOTE_UNRESOLVED, OCR_UNREADABLE, PERIOD_COLUMN_UNRESOLVED, CIN_OCR_MISMATCH, UDIN_UNRESOLVED, OCR_AMBIGUOUS]
ids_in_structured: 401
ids_referenced: 401
orphan_ids: []
missing_from_structured: [L86, L94, L96, L98, L104, L105, L106, L128, L373, L377, L390, L393]  # ledger rows X001-X012; 27 cells, 2 blank rows
gate_a2: pass
mismatch_note: ""
analyst_note: "Loop 1 (A5-M1): 12 fulltext lines added as X001-X012; line_items 96 to 105, zero_standing 23 to 49, qualifiers 40 to 42, cells 310 to 337. L373 nil NC financial liabilities and L128 blank debt securities bear on the nil-borrowings vs D/E 0.11 question below. Original note: Single-item board agenda, 60-minute meeting, standalone only (Note 5: no subsidiary), so no ENTITY_CHANGE test. 23 nil cells across 13 line items: borrowings nil on BS while Debt/Equity ratio 0.11 is non-zero (R173-R178 vs R277,R291), worth A3 attention. Reserve excl. reval R141/R142/R144 repeats 13,661 across three period columns while FY26 shows 10,728, likely column misread. Total non-current liabilities R289 reads 6228 vs 603 prior (OCR ambiguous). Cash flow period columns unresolved for R201-R204, R217, R218. Auditor paras 3-4 garbled, so absence of EoM or Going Concern language cannot be confirmed. Four footnote markers lack footnotes; results link missing."
```
