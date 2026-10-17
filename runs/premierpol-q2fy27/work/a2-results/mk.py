import re
base = "runs/premierpol-q2fy27/"
li = open(base + "work/a2-results/lineitems.md").read()
li = li.replace("| Deferred Tax | page 2 | R097..R098 (2) | 2 | ZERO_STANDING | |",
 "| Deferred Tax | page 2 | R097..R098 (2) | 2 | ZERO_STANDING | Q2FY27 nil; only Q2FY27 and FY26 populated in A1 |")
li = li.replace("| BS TOTAL NON CURRENT LIABILITIES | page 7 | R289..R290 (2) | 2 | OCR_AMBIGUOUS | |",
 "| BS TOTAL NON CURRENT LIABILITIES | page 7 | R289..R290 (2) | 2 | OCR_AMBIGUOUS | 6228 vs 603 prior; A3 to check against components |")
li = li.replace("| group | page | IDs | count | flags | note |", "| line item | page | IDs | n | flags | note |")
head = """=== A2 COUNT TEST ===
category: notes          grep_count: 5    sweep_count: 5    match: yes   (Note 1-5 R379-R383; plus 1 unnumbered note R384)
category: line_items     grep_count: 96   sweep_count: 96   match: yes   (310 value cells R001-R310; P&L 23, p3 10, CF 21, BS 42 line items)
category: zero_standing  grep_count: 23   sweep_count: 23   match: yes   (cells; 13 line items)
category: agenda_items   grep_count: 1    sweep_count: 1    match: yes   (results only, R365)
category: auditor_paras  grep_count: 5    sweep_count: 5    match: yes   (R396-R400)
category: entities       grep_count: 23   sweep_count: 23   match: yes   (R320-R342; no consolidation list, Note 5: no subsidiary/associate/JV)
category: date_units     grep_count: 19   sweep_count: 19   match: yes   (R343-R361)
category: qualifiers     grep_count: 40   sweep_count: 40   match: yes   (R362-R401)
category: footnote_unresolved grep_count: 4 sweep_count: 4 match: yes (R364,R372,R377,R401)
ids_in_structured: 401 | ids_referenced_in_ledger: 401 | orphan_ids: [] | match: yes
gate_a2: pass
=== END COUNT TEST ===

# LEDGER: PREMIERPOL Q2 FY27 results (A2 enumerator)
Row format: ROW_ID | category | A2 flags | cross-ref / materiality. Claim text stays in A1 structured file at that ID.

## 1. Line items (financial tables). One row per line item; IDs carry page and line.
"""
rest = """

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

## 11. Flags raised
ZERO_STANDING (23 cells), FOOTNOTE_UNRESOLVED (4), OCR_UNREADABLE R046, PERIOD_COLUMN_UNRESOLVED (R201-R204, R217, R218), CIN_OCR_MISMATCH, UDIN_UNRESOLVED, OCR_AMBIGUOUS R289.
"""
open(base + "work/ledger_results_premierpol_q2fy27.md", "w", encoding="utf8").write(head + li + rest)
cov = set()
for a, b in re.findall(r"R(\d{3})\.\.R(\d{3})", li):
    cov |= set(range(int(a), int(b) + 1))
for a, b in [(311, 319), (320, 342), (343, 361), (362, 401)]:
    cov |= set(range(a, b + 1))
print(len(cov), [i for i in range(1, 402) if i not in cov])
