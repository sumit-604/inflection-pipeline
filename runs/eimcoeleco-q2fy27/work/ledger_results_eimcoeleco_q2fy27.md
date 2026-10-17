# A2 LEDGER: results | Eimco Elecon (India) Ltd (EIMCOELECO) | q2fy27
Source: runs/eimcoeleco-q2fy27/extracted/eimcoeleco-results-q2fy27-structured.md (IDs R001-R470). Line numbers refer to the fulltext, per A1 header. No prior ledger (ND), so no ENTITY_CHANGE or DROPPED_SLIDE diff is possible.

=== A2 COUNT TEST ===
category: notes          grep_count: 7    sweep_count: 7    match: yes   (numbered Notes 1-6 + one unnumbered cash-flow Note)
category: line_items     grep_count: 98   sweep_count: 99   match: yes   (grep = 98 distinct line items present in structured; sweep = 98 + 1 MISSING_FROM_STRUCTURED row M001, net financing cash flow; reconciled)
category: zero_standing  grep_count: 11   sweep_count: 11   match: yes
category: agenda_items   grep_count: 2    sweep_count: 2    match: yes   (fulltext lines 35, 41; sub-elements of item 2 listed in section 4)
category: auditor_paras  grep_count: 4    sweep_count: 4    match: yes   (fulltext lines 94, 100, 108, 119)
category: entities       grep_count: 29   sweep_count: 29   match: yes   (R375-R403; consolidation list = none, Note 3)
category: annexures      grep_count: 3    sweep_count: 3    match: yes   (A, B, C)
category: signatures     grep_count: 4    sweep_count: 4    match: yes
category: pr_numbers     grep_count: 10   sweep_count: 10   match: yes   (R347-R356)
category: chart_labels   grep_count: 36   sweep_count: 36   match: yes   (R311-R346, all CHART_UNMAPPED)
gate_a2: pass
=== END COUNT TEST ===
ids_in_structured: 470 | ids_referenced_in_ledger: 470 | orphan_ids: [] | match: yes
(turns, questions, mgmt_numbers, slides, slide_numbers: not applicable to results doctype; press-release management numbers are in section 9.)

## 1. NOTES (results notes, p4-6)
note | ROW_ID | A2 flags | cross-ref
N1 | R447 | - | Audit Committee/Board 13 Oct 2026; unmodified conclusion. See R430, R384, R385
N2 | R448 | - | Single segment Machinery and Spares. See R392
N3 | R449 | ZERO_STANDING | No subsidiary/associate/JV. See R393
N4 | R450 | - | Prior-period regrouping; lines not named
N5 | R451 | - | BS attached. See R454
N6 | R452 | - | Cash flow attached (fulltext line 266). See R455
N-CF (unnumbered, p6 "Note:") | R453 | - | Indirect method, Ind AS 7. See R371
Footnotes and qualifiers swept: R443-R446 (units, status labels, EPS not annualised, notes header); R454-R455 column status; R461-R464 press release (R462, R463, R464 FOOTNOTE_UNRESOLVED); R465-R470 annexure and signature qualifiers.

## 2. LINE ITEMS (one row per line; IDs = one per period column)
LI | statement/page/line | label | ROW IDs | A2 flags
LI001 | P&L p4 L154 | (a) Revenue from Operations | R001-R006 | 
LI002 | P&L p4 L155 | (bl Other Income | R007-R012 | 
LI003 | P&L p4 L156 | Total Income | R013-R018 | 
LI004 | P&L p4 L158 | (a) Cost of materials consumed | R019-R024 | 
LI005 | P&L p4 L159 | (bl Purchase of stock-in-trade | R025-R030 | 
LI006 | P&L p4 L160 | (cl Changes in inventories of finished goods and work-in-pro | R031-R036 | 
LI007 | P&L p4 L161 | (d) Manufacturing expense | R037-R042 | 
LI008 | P&L p4 L162 | (e) Employee benefits expense | R043-R048 | 
LI009 | P&L p4 L163 | (f) Finance Cost | R049-R054 | 
LI010 | P&L p4 L164 | (g) Depreciation, Impairment and amortisation expense | R055-R060 | 
LI011 | P&L p4 L165 | (h) Compensation to Distributors | R061-R066 | 
LI012 | P&L p4 L166 | (i) Other Expenses | R067-R072 | 
LI013 | P&L p4 L167 | Total Expenses | R073-R078 | 
LI014 | P&L p4 L168 | 3 Profit before tax (1·2) | R079-R084 | 
LI015 | P&L p4 L170 | • Current Tax | R085-R090 | 
LI016 | P&L p4 L171 | • Adjustment of tax relating to earlier periods | R091 | ZERO_STANDING (blank Q/H1 cells)
LI017 | P&L p4 L172 | • Deferred Tax | R092-R097 | 
LI018 | P&L p4 L173 | Total Tax Expense | R098-R103 | 
LI019 | P&L p4 L174 | 5 Net Profit for the period after tax {3-4) | R104-R109 | 
LI020 | P&L p4 L177 | (i) Remeasurements of defined benefit plan | R110 | ZERO_STANDING (blank Q/H1 cells)
LI021 | P&L p4 L178 | (ii) Income tax related to items no (i) above | R111 | ZERO_STANDING (blank Q/H1 cells)
LI022 | P&L p4 L179 | Other Comprehensive Income for the period (net of tax) | R112 | ZERO_STANDING (blank Q/H1 cells)
LI023 | P&L p4 L180 | 7 Total Comprehensive Income for the period (net of tax) (5+ | R113-R118 | 
LI024 | P&L p4 L181 | 8 Paid-up Equity Share Capital ( Face Value~ 10/· per share} | R119-R124 | 
LI025 | P&L p4 L182 | 9 Other Equity | R125 | 
LI026 | P&L p4 L185 | • Basic (in ~) | R126-R131 | 
LI027 | P&L p4 L186 | • Diluted (in~) | R132-R137 | 
LI028 | BS p5 L204 | (a) Property, plant and equipment | R138-R139 | 
LI029 | BS p5 L205 | (b) Capital work-in-progress | R140-R141 | 
LI030 | BS p5 L206 | (c) Investment property | R142-R143 | 
LI031 | BS p5 L207 | (d) Intangible assets | R144-R145 | 
LI032 | BS p5 L209 | (i) Investments | R146-R147 | 
LI033 | BS p5 L210 | (ii) Other financial assets | R148-R149 | 
LI034 | BS p5 L211 | (f) Other non-current assets | R150 | ZERO_STANDING (31.03.26 blank); COLUMN_UNRESOLVED
LI035 | BS p5 L212 | Total Non-current assets | R151-R152 | 
LI036 | BS p5 L214 | (a) Inventories | R153-R154 | 
LI037 | BS p5 L216 | (i) Investments | R155-R156 | 
LI038 | BS p5 L217 | (ii) Trade receivables | R157-R158 | 
LI039 | BS p5 L218 | (iii) Cash and cash equivalents | R159-R160 | 
LI040 | BS p5 L219 | (iv) Bank balances other than (iii) above | R161-R162 | 
LI041 | BS p5 L220 | (v) Other financial assets | R163-R164 | 
LI042 | BS p5 L222 | (c) Other current assets | R165-R166 | 
LI043 | BS p5 L223 | Total Current assets | R167-R168 | 
LI044 | BS p5 L224 | Total Assets | R169-R170 | 
LI045 | BS p5 L229 | (a)Equity share capital | R171-R172 | 
LI046 | BS p5 L230 | (b) Other equity | R173-R174 | 
LI047 | BS p5 L231 | Total equity | R175-R176 | 
LI048 | BS p5 L235 | (i) lease liabilities | R177-R178 | 
LI049 | BS p5 L236 | (Ii) Other Financial Liabilities | R179 | ZERO_STANDING (31.03.26 blank)
LI050 | BS p5 L237 | (b) Other non-current liabilities | R180 | ZERO_STANDING (31.03.26 blank)
LI051 | BS p5 L238 | ( c) Provisions | R181-R182 | 
LI052 | BS p5 L239 | (d) Deferred tax liabilities (net) | R183-R184 | 
LI053 | BS p5 L240 | Total Non--c:urrent llabillties | R185-R186 | 
LI054 | BS p5 L243 | (i) Borrowing | R187-R188 | 
LI055 | BS p5 L244 | (ii) Lease liabilities | R189-R190 | 
LI056 | BS p5 L260 | (iv) Other financial liabilities | R191-R192 | 
LI057 | BS p5 L261 | (b) Other current liabilities | R193-R194 | 
LI058 | BS p5 L262 | (c) Provisions | R195-R196 | 
LI059 | BS p5 L263 | (d) Current tax liabilities (net) | R197-R198 | 
LI060 | BS p5 L264 | Total Current liabilities | R199-R200 | 
LI061 | BS p5 L265 | Total equity and liabilities | R201-R202 | 
LI062 | CF p6 L273 | Profit before Tax | R203-R205 | 
LI063 | CF p6 L275 | Depreciation, Impairment and Amortisation of Property, Plant | R206-R208 | 
LI064 | CF p6 L277 | Finance Cost | R209-R211 | 
LI065 | CF p6 L278 | Gain on sale/ fair valuation of Investment (Net) | R212-R214 | 
LI066 | CF p6 L279 | loss/(Profit) on Sale of Property, Plant and Equipment (Net) | R215-R217 | 
LI067 | CF p6 L280 | Interest Income | R218-R220 | 
LI068 | CF p6 L281 | Dividend Income | R221-R223 | 
LI069 | CF p6 L282 | Provision for Doubtful receivable/sundry ba lances written o | R224-R226 | 
LI070 | CF p6 L283 | Unrealised foreign exchange (gain)/loss (Net) | R227-R229 | 
LI071 | CF p6 L285 | Operating Profit before changes in working capital | R230-R232 | 
LI072 | CF p6 L288 | Trade and other receivables | R233-R235 | 
LI073 | CF p6 L289 | Inventories | R236-R238 | 
LI074 | CF p6 L290 | Other financial assets | R239-R241 | 
LI075 | CF p6 L291 | Other current and non-current assets {308.64) | R242-R244 | 
LI076 | CF p6 L292 | Trade payables | R245-R247 | 
LI077 | CF p6 L293 | Other payables | R248-R250 | 
LI078 | CF p6 L294 | Other financial liabilities | R251-R253 | 
LI079 | CF p6 L296 | Cash generated from operations | R254-R256 | 
LI080 | CF p6 L298 | Net Direct taxes (paid)/refunded | R257-R259 | 
LI081 | CF p6 L300 | NET CASH GENERATED FROM OPERATING ACTIVITIES (A) | R260-R262 | 
LI082 | CF p6 L303 | Payments for purchase of property plant and equipment and CW | R263-R265 | 
LI083 | CF p6 L304 | Proceeds from sale of property, plant and equipment 5.40 121 | R266-R268 | 
LI084 | CF p6 L305 | Proceeds from sale/(Purchase) of investments (Net) | R269-R271 | 
LI085 | CF p6 L306 | Interest income | R272-R274 | 
LI086 | CF p6 L307 | Divide nd income | R275-R277 | 
LI087 | CF p6 L308 | Bank balance not considered as cash and cash equivalent (Net | R278-R280 | 
LI088 | CF p6 L311 | NET CASH (USED IN) /GENERATEO FROM INVESTING ACTIVITIES (B) | R281-R283 | 
LI089 | CF p6 L314 | Finance Cost | R284-R286 | 
LI090 | CF p6 L315 | Borrowing | R287-R288 | ZERO_STANDING (H1 FY26 blank)
LI091 | CF p6 L317 | Interest on lease liability | R289-R291 | 
LI092 | CF p6 L318 | Principal Payment of lease liability | R292-R294 | 
LI093 | CF p6 L319 | Dividend Paid | R295-R297 | 
LI094 | CF p6 L324 | Net increase/ (decrease) in cash and cash equivalents (A+B+C | R298-R300 | 
LI095 | CF p6 L325 | Cash and cash equivalents at beginning of the year | R301-R303 | 
LI096 | CF p6 L326 | Cash and cash equivalents at the end of the period | R304-R306 | 
LI097 | BS p5 L252,L255 | Trade payables: MSME dues | R307,R309 | ASSIGNMENT_BY_LAYOUT (from A1)
LI098 | BS p5 L254,L257 | Trade payables: other than MSME | R308,R310 | ASSIGNMENT_BY_LAYOUT (from A1)
LI099 | CF p6 L322 | NET CASH (USED IN)/GENERATED FROM FINANCING ACTIVITIES (C): (0.93) H1FY27, (128.42) FY26, (327.09) H1FY26 | M001 (own line number 322) | MISSING_FROM_STRUCTURED
Statement line counts: P&L 27, BS 36, CF 36 (incl. M001). Period movement is left to A3/A4.
Layout flag for A3: the H1 FY26 investing column (R265, R268, R271, R274, R277, R280) looks shifted against its labels (interest income 10.15 equals the H1 FY26 dividend add-back; dividend line shows (572.17); PPE payments show +0.40). COLUMN_MISALIGNMENT_SUSPECT; check fulltext lines 303-308 before use.

## 3. ZERO_STANDING (blank, nil or none cells; 11)
Z | ROW_ID | flag | note
Z1 | R091 | ZERO_STANDING | Tax adjustment for earlier periods blank in all five Q/H1 columns, (10.54) FY26 only
Z2 | R110 | ZERO_STANDING | OCI remeasurements blank Q/H1, (35.22) FY26 only
Z3 | R111 | ZERO_STANDING | OCI tax blank Q/H1, 8.86 FY26
Z4 | R112 | ZERO_STANDING | OCI total blank Q/H1, (26.36) FY26. See R118 (TCI differs from PAT in FY26 only)
Z5 | R150 | ZERO_STANDING, COLUMN_MISLABEL | Other non-current assets 4,824.68: A1 labels it 30.09.26, but 31.03.26 NCA components sum to 31,717.32 only with it (6,410.76+156.65+236.73+853.46+19,067.76+167.28+4,824.68) and 30.09.26 components sum to 33,502.99 without it. So it belongs to 31.03.26; 30.09.26 cell is blank. Loop back to A1
Z6 | R179 | ZERO_STANDING | Other NC financial liabilities nil at 31.03.26
Z7 | R180 | ZERO_STANDING | Other NC liabilities nil at 31.03.26
Z8 | R287 | ZERO_STANDING | CF Borrowing blank for H1 FY26 (R288 FY26 270.39)
Z9 | R393 | ZERO_STANDING | Note 3 entity row: no subsidiary/associate/JV
Z10 | R468 | ZERO_STANDING | Annexure B brief profile: Not applicable
Z11 | R469 | ZERO_STANDING | Annexure B director relationships: Not applicable
Absent by design (no row, none enumerable): exceptional items, EoM/Other Matter/Going Concern paragraphs, dividend, ESOP, auditor change.

## 4. AGENDA ITEMS (Board Outcome letter, p1-2)
AG | ROW_IDs | flag | note
AG1 | R404,R419,R420,R421,R460,R380 | - | Item 1: approve unaudited Q2/H1 results + LRR + press release (Reg 33), Annexure A
AG2 | R381,R402,R405,R406,R423 | TIMING_GAP | Item 2: note CFO resignation w.e.f. close of 30 Oct 2026. Letter dated 5 Sep 2026 (R441), board noted 13 Oct 2026 (R419): 38 days
AG2a | R405 | - | Ceases as KMP for materiality determination
AG2b | R406,R382 | - | Ceases as Risk Committee member
AG2c | R465,R358,R422 | - | Reg 30 disclosures in Annexure B; SEBI circular 30 Jan 2026
AG2d | R466 | - | CFO confirms no other material reasons; letter is Annexure C
Meeting time: R420 (11:30 a.m. to 1:00 p.m., 90 minutes); R359 restates it (RESTATED).
Agenda items absent: dividend, AR/AGM, record date, director appointments, auditor change, ESOP, fund raise. Successor CFO: NOT FOUND (no ID).

## 5. ANNEXURES AND DIRECTOR PROFILES
Annexure | ROW_IDs | note
A: results (statement p4, BS p5, CF p6, auditor report p3) | R001-R306, R447-R459 | main content
B: Reg 30 table p10 | R407,R408,R440,R468,R469,R402 | profile and relationships Not applicable
C: resignation letter p11 | R402,R409,R410,R411,R441,R442 | addressed to Executive Director, not Board or Chair. See R466
Director profiles: none (no appointment). Rows: 0.

## 6. AUDITOR REPORT PARAGRAPHS (p3)
Para | ROW_IDs | note
P1 scope | R459,R426,R368 | limited review, Reg 33
P2 management responsibility | R388,R369,R403 | Ind AS 34, s.133
P3 review standard | R387,R386,R456,R457,R370 | SRE 2410 moderate assurance; no audit opinion
P4 conclusion | R458,R447 | nothing came to attention; unmodified
Signature block | R385,R389,R362,R363,R364,R400,R425 | UDIN 26045027DECSCP3663 (R363)
Footer | R365,R401,R372,R374,R470 | LLPIN, branches, phone
Emphasis of Matter, Other Matters, Going Concern: none present. Entities reviewed: Company only (Note 3). Unaudited or management-furnished entities: none.

## 7. ENTITIES (R375-R403, 29 rows; no prior list, so no ENTITY_CHANGE possible)
R375-R403 | entities | R375 filer; R381 Mr. Vishal C. Begwani CFO/KMP resigning; R385 K C Mehta & Co LLP auditor; R390 Kamlesh N. Shah ED/signatory; R393 no subsidiary/associate/JV (ZERO_STANDING); R383 CS signatory; R391 investor contact; R392 single segment. Others: exchanges, regulators, standards, locations, product lines.

## 8. SIGNATURES
Sig | ROW_IDs | flag | note
S1 CS Rikenkumar Dalwadi, digital | R383,R424,R467 | - | 13 Oct 2026 13:05:56 +05:30, after meeting end 13:00 (R420). No pre-meeting flag
S2 Auditor partner | R389,R425,R363,R362 | - | 13 Oct 2026, Vadodara
S3 Executive Director Kamlesh N. Shah (p6) | R390,R431,R367 | - | 13 Oct 2026, Vallabh Vidyanagar
S4 CFO resignation letter | R441,R442 | TIMING_GAP | dated 5 Sep 2026. No CFO signature block on the results statement in A1 rows (NOT FOUND)

## 9. PRESS RELEASE (p7-9) AND MANAGEMENT NUMBERS
Item | ROW_IDs | flags | note
Revenue Rs 57 cr, YoY 70.9% | R347,R348,R349 | RESTATED | restates R001, R003
EBITDA Rs 11 cr, 18.8%, YoY 108.8% | R350,R351,R352,R464 | RESTATED, FOOTNOTE_UNRESOLVED | EBITDA definition not stated
PAT Rs 8 cr, YoY 46.5% | R353,R354 | RESTATED | restates R104, R106
Targeted margin 18-20% | R355,R412 | - | forward, no date
Open order pipeline Rs 133 cr | R356,R415,R435,R463 | FOOTNOTE_UNRESOLVED | basis not given
Chart labels | R311-R346 | CHART_UNMAPPED | 36 labels, series and period unresolved
Dates and periods | R432-R434,R436-R439,R461,R462 | FOOTNOTE_UNRESOLVED (R462) |
Qualitative forwards | R413,R414,R416,R417,R418 | - |
Identifiers | R357,R358,R359,R360,R361,R364,R365,R366,R369,R370,R371,R372,R373,R374 | - | registration numbers and references

## 10. DATES, FORWARDS, QUALIFIERS (accounted)
R404-R411 forwards (cessation 30 Oct 2026; handover commitments). R412-R418 press release forwards. R419-R442 dates. R443-R470 qualifiers (sections 1, 6, 8, 9).
TEXT_LAYER_GLITCH rows from A1: R014, R153, R242, R267.

## 11. MISSING_FROM_STRUCTURED
M001 | CF p6, fulltext line 322 | NET CASH (USED IN)/GENERATED FROM FINANCING ACTIVITIES (C): H1 FY27 (0.93); FY26 (128.42); H1 FY26 (327.09). Loop back to A1: no financing-total row, though operating (A) and investing (B) totals exist. Also unlisted: "Financial liability" sub-header (line 316, label only, no values).

```yaml
stage: A2-enumerator
company: "EIMCOELECO"
quarter: "q2fy27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "runs/eimcoeleco-q2fy27/work/ledger_results_eimcoeleco_q2fy27.md"
counts:
  notes: 7
  line_items: 99
  zero_standing: 11
  agenda_items: 2
  auditor_paras: 4
  entities: 29
  turns: 0
  questions: 0
  mgmt_numbers: 10
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, RESTATED, TIMING_GAP, FOOTNOTE_UNRESOLVED, CHART_UNMAPPED, COLUMN_MISLABEL, COLUMN_MISALIGNMENT_SUSPECT, MISSING_FROM_STRUCTURED]
ids_in_structured: 470
ids_referenced: 470
orphan_ids: []
missing_from_structured: ["M001: CF net cash from financing activities (C) (0.93) / (128.42) / (327.09), fulltext line 322"]
gate_a2: pass
mismatch_note: ""
analyst_note: "A1 error: R150 (other non-current assets 4,824.68) is labelled 30.09.26 but belongs to 31.03.26; NCA sums confirm it, so 30.09.26 is blank and PPE rose 6,410.76 to 11,154.88. A1 omitted the financing total (C), added as M001. H1 FY26 investing column (R265-R280) looks shifted against labels; check before any cash-flow arithmetic. CFO resignation letter is dated 5 Sep 2026 but the board noted it 13 Oct 2026 (38 days); successor CFO not named. No EoM or going-concern language. Block path assumed as work/blocks/a2-results.yaml (none given in task)."
```
