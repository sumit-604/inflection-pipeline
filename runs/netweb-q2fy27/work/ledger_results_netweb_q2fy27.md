# A2 COMPLETENESS LEDGER: NETWEB Q2 FY27 results (Reg 33 filing)
Source: A1 structured extraction only (R001-R428). Values stay in the structured file at each ID. Units INR million (x0.1 = Rs Cr).

=== A2 COUNT TEST ===
category: notes (numbered)   grep_count: 5   sweep_count: 5   match: yes
category: footnotes (unnumbered, asterisk)  grep_count: 1   sweep_count: 1   match: yes
category: line_items   grep_count: 107   sweep_count: 107   match: yes   (P&L 26, Balance Sheet 37, Cash Flow 44; grep = distinct page+line+metric groups over R001-R313, sweep = manual metric count)
category: zero_standing_cells   grep_count: 18   sweep_count: 18   match: yes   (grep -c ZERO_STANDING = 18; 8 line items carry at least one zero cell; 2 line items are zero in ALL periods)
category: agenda_items   grep_count: 2   sweep_count: 2   match: yes
category: annexure_ii_rows   grep_count: 8   sweep_count: 8   match: yes
category: auditor_paras   grep_count: 5   sweep_count: 5   match: yes   (4 numbered paragraphs + sign-off block)
category: entities   grep_count: 22   sweep_count: 22   match: yes   (A1 ENTITY rows R346-R367; consolidation list: none, standalone filing)
category: slides/turns/questions/mgmt_numbers: n/a for results doctype
ids_in_structured: 428 | ids_referenced_in_ledger: 428 | orphan_ids: [] | match: yes
gate_a2: pass
=== END COUNT TEST ===

## 1. NOTES (numbered 1-5, plus footnote)
| ROW_ID | category | A2 flags | cross-ref / materiality |
|---|---|---|---|
| R419 | notes header |  | Other Notes 1 to 5 block, p6 L303 |
| R420 | Note 1 basis of prep / review |  | Reg 33, Ind AS; Audit Committee review and Board approval 24-Oct-2026 (R394); links R340 |
| R421 | Note 2 segment |  | one segment "Computer servers" (R358, R342, R344); no segment table exists |
| R422 | Note 3 QIP |  | INR 12,000m raised; R327-R332, R339, R341, R360, R361, R359; dates R388-R391; ties to financing inflow R304 |
| R423 | Note 3 cont. QIP deployment | FOOTNOTE_UNRESOLVED | QIP money parked in FD 3,500m (R333), monitoring 587.88m (R334), escrow 177.00m (R335): sums to 4,264.88m vs 11,755.76m net proceeds (R304); use of the rest not stated. Cross-ref R365, R366, R393 |
| R424 | Note 4 ESOP |  | 4,935 ESOPs, cost 0.62m (R336-R338, R392, R399, R377, R362); R246/R247 cash flow add-back |
| R425 | Note 5 regrouping |  | prior-period figures regrouped; comparatives may differ from earlier filings |
| R402-R404 | Footnote * Not annualised (EPS) |  | Basic R140-R145, Diluted R146-R151 |

## 2. LINE ITEMS (every table row, incl. zero standing). One ledger row per line item; R-range = all period cells
| ROW_ID | statement | location | line item | A2 flags |
|---|---|---|---|---|
| R001-R006 | P&L | p3 L160 | Revenue from operations |  |
| R007-R012 | P&L | p3 L161 | Other income |  |
| R013-R018 | P&L | p3 L162 | Total income |  |
| R019-R024 | P&L | p3 L164 | Cost of materials consumed |  |
| R025-R030 | P&L | p3 L165 | Change in inventories of finished goods and work-in-progress |  |
| R031-R036 | P&L | p3 L166 | Employee benefits expense |  |
| R037-R042 | P&L | p3 L167 | Finance costs |  |
| R043-R048 | P&L | p3 L168 | Depreciation and amortisation expenses |  |
| R049-R054 | P&L | p3 L169 | Other expenses |  |
| R055-R060 | P&L | p3 L170 | Total expenses |  |
| R061-R066 | P&L | p3 L171 | Profit before exceptional items and tax |  |
| R067-R072 | P&L | p3 L172 | Exceptional items (net) | ZERO_STANDING (6 of 6 cells: R067,R068,R069,R070,R071,R072) ALL-PERIOD |
| R073-R078 | P&L | p3 L173 | Profit before tax |  |
| R079-R084 | P&L | p3 L175 | Current tax |  |
| R085-R090 | P&L | p3 L176 | Adjustment of tax relating to earlier period | ZERO_STANDING (5 of 6 cells: R085,R086,R087,R088,R089) |
| R091-R096 | P&L | p3 L177 | Deferred tax charge/(credit) |  |
| R097-R102 | P&L | p3 L178 | Total tax expense |  |
| R103-R108 | P&L | p3 L179 | Profit for the period / year |  |
| R109-R114 | P&L | p3 L182 | -Re-measurement gains / (losses) on defined benefit plans |  |
| R115-R120 | P&L | p3 L183 | -Income Tax relating to Items that will not be reclassified to statement of profit and loss |  |
| R121-R126 | P&L | p3 L184 | Total other comprehensive income/(loss), net of tax |  |
| R127-R132 | P&L | p3 L185 | Total comprehensive income for the period / year |  |
| R133-R138 | P&L | p3 L186 | Paid up equity share capital (face value of INR 2 per share) |  |
| R139 | P&L | p3 L187 | Other equity | SINGLE_COLUMN (only FY26 populated) |
| R140-R145 | P&L | p3 L189 | Basic (in INR)* |  |
| R146-R151 | P&L | p3 L190 | Diluted (in INR)* |  |
| R152-R153 | BalSheet | p4 L199 | (a) Property, plant and equipment |  |
| R154-R155 | BalSheet | p4 L200 | (b) Capital work-in-progress |  |
| R156-R157 | BalSheet | p4 L201 | (c) Right-of-use assets |  |
| R158-R159 | BalSheet | p4 L202 | (d) Other intangible assets |  |
| R160-R161 | BalSheet | p4 L203 | (e) Intangible Assets under development |  |
| R162-R163 | BalSheet | p4 L205 | (i) Investments | ZERO_STANDING (2 of 2 cells: R162,R163) ALL-PERIOD |
| R164-R165 | BalSheet | p4 L206 | (ii) Other financial assets |  |
| R166-R167 | BalSheet | p4 L207 | (g) Deferred tax assets (net) |  |
| R168-R169 | BalSheet | p4 L208 | (h) Other non-current assets |  |
| R170-R171 | BalSheet | p4 L209 | Total non-current assets |  |
| R172-R173 | BalSheet | p4 L211 | (a) Inventories |  |
| R174-R175 | BalSheet | p4 L213 | (i) Trade receivables |  |
| R176-R177 | BalSheet | p4 L214 | (ii) Cash and cash equivalents |  |
| R178-R179 | BalSheet | p4 L215 | (iii) Bank balances other than cash and cash equivalents |  |
| R180-R181 | BalSheet | p4 L216 | (iv) Other financial assets |  |
| R182-R183 | BalSheet | p4 L217 | (c) Other current assets |  |
| R184-R185 | BalSheet | p4 L218 | Total current assets |  |
| R186-R187 | BalSheet | p4 L219 | TOTAL ASSETS |  |
| R188-R189 | BalSheet | p4 L221 | (a) Equity share capital |  |
| R190-R191 | BalSheet | p4 L222 | (b) Other equity |  |
| R192-R193 | BalSheet | p4 L223 | TOTAL EQUITY |  |
| R194-R195 | BalSheet | p4 L227 | (i) Borrowings |  |
| R196-R197 | BalSheet | p4 L228 | (ii) Lease liabilities |  |
| R198-R199 | BalSheet | p4 L229 | (b) Other non current liabilities |  |
| R200-R201 | BalSheet | p4 L230 | (c) Provisions |  |
| R202-R203 | BalSheet | p4 L231 | Total non-current liabilities |  |
| R204-R205 | BalSheet | p4 L234 | (i) Borrowings |  |
| R206-R207 | BalSheet | p4 L235 | (ii) Lease liabilities |  |
| R208-R209 | BalSheet | p4 L237 | -Total outstanding dues of micro enterprises and small enterprises |  |
| R210-R211 | BalSheet | p4 L238 | -Total outstanding dues of creditors other than micro enterprises and small enterprises |  |
| R212-R213 | BalSheet | p4 L239 | (iv) Other financial liabilities |  |
| R214-R215 | BalSheet | p4 L240 | (b) Other current liabilities |  |
| R216-R217 | BalSheet | p4 L241 | (c) Provisions |  |
| R218-R219 | BalSheet | p4 L242 | (d) Current Tax Liabilities (net) |  |
| R220-R221 | BalSheet | p4 L243 | Total current liabilities |  |
| R222-R223 | BalSheet | p4 L244 | TOTAL LIABILITIES |  |
| R224-R225 | BalSheet | p4 L245 | TOTAL EQUITY AND LIABILITIES |  |
| R226-R227 | CashFlow | p5 L252 | Net profit before tax |  |
| R228-R229 | CashFlow | p5 L254 | Depreciation and amortization expense |  |
| R230-R231 | CashFlow | p5 L255 | Depreciation of Right-of-use assets |  |
| R232-R233 | CashFlow | p5 L256 | Finance costs (other than Interest on lease liabilities) |  |
| R234-R235 | CashFlow | p5 L257 | Interest on lease liabilities |  |
| R236-R237 | CashFlow | p5 L258 | Interest income |  |
| R238-R239 | CashFlow | p5 L259 | Unrealised foreign exchange |  |
| R240-R241 | CashFlow | p5 L260 | Liabilities written Back |  |
| R242-R243 | CashFlow | p5 L261 | Provision for doubtful debts |  |
| R244-R245 | CashFlow | p5 L262 | Bad debts written Off |  |
| R246-R247 | CashFlow | p5 L263 | Share-based payments to employees |  |
| R248-R249 | CashFlow | p5 L264 | Loss on discard of property, plant and equipment | ZERO_STANDING (1 of 2 cells: R248) |
| R250-R251 | CashFlow | p5 L265 | Profit on Sale of property, plant and equipment | ZERO_STANDING (1 of 2 cells: R251) |
| R252-R253 | CashFlow | p5 L266 | Cash generated from operations before working capital changes |  |
| R254-R255 | CashFlow | p5 L268 | (Increase)/Decrease in trade receivables |  |
| R256-R257 | CashFlow | p5 L269 | (Increase)/Decrease in other financial assets |  |
| R258-R259 | CashFlow | p5 L270 | (Increase)/Decrease in other assets |  |
| R260-R261 | CashFlow | p5 L271 | (Increase)/Decrease in inventories |  |
| R262-R263 | CashFlow | p5 L272 | (Decrease)/Increase in other liabilities |  |
| R264-R265 | CashFlow | p5 L273 | (Decrease)/Increase in trade payables |  |
| R266-R267 | CashFlow | p5 L274 | (Decrease)/Increase in other financial liabilities |  |
| R268-R269 | CashFlow | p5 L275 | (Decrease)/Increase in provisions |  |
| R270-R271 | CashFlow | p5 L276 | Cash generated/(used) from operating activities |  |
| R272-R273 | CashFlow | p5 L277 | Income Tax Paid (net of refunds) |  |
| R274-R275 | CashFlow | p5 L278 | Net cash generated/(used) from operating activities |  |
| R276-R277 | CashFlow | p5 L280 | Purchase of property, plant and equipment and intangibles |  |
| R278-R279 | CashFlow | p5 L281 | Proceeds from sale of property, plant and equipment | ZERO_STANDING (1 of 2 cells: R279) |
| R280-R281 | CashFlow | p5 L282 | Interest Income |  |
| R282-R283 | CashFlow | p5 L283 | Investment in bank deposits |  |
| R284-R285 | CashFlow | p5 L284 | Proceeds from bank deposits |  |
| R286-R287 | CashFlow | p5 L285 | Net cash generated/(used) in investing activities |  |
| R288-R289 | CashFlow | p5 L287 | Interest paid (other than on lease liabilities) |  |
| R290-R291 | CashFlow | p5 L288 | Interest on lease liabilities |  |
| R292-R293 | CashFlow | p5 L289 | Repayment of long term borrowings |  |
| R294-R295 | CashFlow | p5 L290 | Proceeds from short term borrowings |  |
| R296-R297 | CashFlow | p5 L291 | Principal payments against lease liabilities |  |
| R298-R299 | CashFlow | p5 L292 | Proceeds in monitoring account |  |
| R300-R301 | CashFlow | p5 L293 | Dividends paid |  |
| R302-R303 | CashFlow | p5 L294 | Recovery of IPO & Pre IPO expenses | ZERO_STANDING (1 of 2 cells: R302) |
| R304-R305 | CashFlow | p5 L295 | Proceeds from issuing shares (net of issue expenses) | ZERO_STANDING (1 of 2 cells: R305) |
| R306-R307 | CashFlow | p5 L296 | Net cash generated/(used) in Financing Activities |  |
| R308-R309 | CashFlow | p5 L297 | Net increase/(decrease) in cash and cash equivalents (A+B+C) |  |
| R310-R311 | CashFlow | p5 L298 | Cash and cash equivalents at the beginning of the period |  |
| R312-R313 | CashFlow | p5 L299 | Cash and cash equivalents at the end of the period |  |

Line-item annotations (enumeration notes only, no interpretation):
- Other equity (R139) carries a single value (Year ended 31-03-2026); the five other P&L columns are not populated.
- Exceptional items (R067-R072): dash in all six columns. Template signal, ZERO_STANDING ALL-PERIOD.
- Adjustment of tax relating to earlier period: dash in five columns, (0.68) in FY26 (R090).
- Non-current Investments (R162, R163): dash at both dates, ZERO_STANDING ALL-PERIOD.
- Cash flow lines with a dash in one half: Loss on discard of PPE (R248 dash, R249 0.39), Profit on sale of PPE (R251 dash vs R250), Proceeds from sale of PPE (R279 dash, R278 1.20), Recovery of IPO expenses (R302 dash, R303 1.25), Proceeds from issuing shares (R305 dash vs R304 11,755.76).
- Mechanical tie-outs in the structured file: Q1+Q2 revenue R002+R001 = R004; H1 PBT R226 = 2,967.87.

## 3. BOARD OUTCOME AGENDA ITEMS AND MEETING DATA
| ROW_ID | category | A2 flags | cross-ref / materiality |
|---|---|---|---|
| R412 | Agenda 1: unaudited Q2/H1 results with limited review report (Annexure 1) |  | R380 period, R427 enclosures |
| R368 | Agenda 2: proposal to incorporate wholly owned Taiwan subsidiary | FORWARD ENTITY_CHANGE (proposed) | R350, R369, R413, R414, R415; details in Annexure II. Only two agenda items: no AR/AGM/dividend/auditor/director/ESOP/capital resolutions listed |
| R378 | Letter date 24.10.2026 |  |  |
| R379 | Board meeting date Saturday 24-Oct-2026 |  | weekend meeting |
| R398 | Board meeting day (Saturday) | RESTATED | restates R379 |
| R316 | Meeting commencement 11:45 A.M |  |  |
| R428 | Meeting conclusion time | ILLEGIBLE | scan unreadable; duration cannot be computed; also blocks the signature-timing check |
| R314-R315 | CIN and BSE scrip code |  | header identifiers |
| R317-R321 | Registered office PIN, phone, exchange PINs, SEBI circular no. |  | R381 circular date, R397 same circular in Annexure II (RESTATED), R349 LODR, R401 year |
| R351 | Signatory: Company Secretary and Compliance Officer | FOOTNOTE_UNRESOLVED | name not legible; stamp and signature only; no digital-signature timestamp (scan) |
| R346-R348 | Reporting company and exchange addressees |  |  |
| R352 | Statutory Auditors of the Company (limited review issuer) |  |  |

## 4. ANNEXURE II (Taiwan subsidiary) table, 8 rows
| ROW_ID | Sr.No / particular | A2 flags | cross-ref |
|---|---|---|---|
| R371,R370,R367 | 1 Name, date, country of incorporation | FORWARD | name "as may be approved", date "To be incorporated"; country Taiwan at fulltext L350 (not a standalone structured row) |
| R376 | 2 Holding company and relation | FORWARD | WOS |
| MISSING-1 | 3 Industry of the entity | MISSING_FROM_STRUCTURED | fulltext L356: "Same industry in which we operate." Not in A1 structured. Loop back to A1. |
| R372 | 4 Background | FORWARD | yet to be incorporated |
| R375 | 5 Governmental/regulatory approvals | FORWARD | approval of competent authority, if required |
| R373 | 6 Nature of consideration | FORWARD | cash |
| R374 | 7 Cost of subscription / price | FORWARD | To be determined |
| R345 | 8 Percentage of shareholding / control | FORWARD | 100%; number of shares allotted not stated (blank) |
| R426 | Annexure II title |  | R397 SEBI circular date, R415, R413, R414 qualifiers |
| R369,R350 | Incorporation not yet initiated (p1) | FORWARD |  |

## 5. AUDITOR REPORT PARAGRAPHS (limited review, SS Kothari Mehta & Co. LLP)
| ROW_ID | paragraph | A2 flags | cross-ref |
|---|---|---|---|
| R353,R354,R355,R356 | Header: addressee, auditor firm, partner, ICAI, Companies Act |  | R382 review period |
| R416 | Paras 1-3 scope: reviewed Statement; SRE 2410; moderate assurance |  | R325 SRE 2410 number |
| R417 | Para 3 limitation (inquiries and analytical procedures) |  | less assurance than audit |
| R418 | Para 4 conclusion: unmodified, nothing came to attention |  | opinion type: unmodified conclusion. No Emphasis of Matter, no Other Matter, no Going Concern language present |
| R322,R323,R324,R326,R383,R384 | Sign-off block: ICAI reg no, membership, UDIN, address, date, place | FOOTNOTE_UNRESOLVED | R322 registration number reading uncertain (OCR spacing); UDIN 26528799JGDTWG4403; report date 24-Oct-2026 same day as board meeting; entities reviewed: Company only (standalone), no unaudited or management-furnished entity carve-out |

## 6. ENTITIES (22 A1 entity rows; consolidation list = none, standalone)
| ROW_ID | category | A2 flags | note |
|---|---|---|---|
| R357 | reporting entity (results header) |  | standalone; no subsidiaries, associates or JVs listed |
| R367 | Proposed Taiwan WOS (Annexure II) | ENTITY_CHANGE | new entity proposed; no prior list to diff against (no prior NETWEB run) |
| R358-R366 | segment, QIBs, ICDR, committees (Fund Raising, NRC, Audit), MD signatory, monitoring and escrow accounts |  | R364 Sanjay Lodha DIN R343; QIBs not individually named |

## 7. SIGNATURE BLOCKS
| ROW_ID | block | flags | note |
|---|---|---|---|
| R395,R396,R364,R343 | Results sign-off: Sanjay Lodha, Managing Director, DIN 00461913, Faridabad, 24-Oct-2026 | FOOTNOTE_UNRESOLVED | no digital timestamp (scan). Sign-off date equals board date; conclusion time illegible (R428), so the signed-before-conclusion test cannot run |
| R351,R378 | Board outcome letter signature, Company Secretary |  | name illegible |

## 8. DATES, QUALIFIERS, REMAINING NUMBERS (grouped; completes accountability)
| ROW_ID | group | flags | note |
|---|---|---|---|
| R385-R387 | Column period/date headers P&L, BS, CF |  | R406, R408, R409 audit status per column |
| R388-R394 | Note 3/4 dates (QIP approvals, ESOP grant, balances date) |  | R388 1-Jul-26 board, R389 1-Aug-26 postal ballot, R390 17-Aug, R391 20-Aug FRC |
| R400 | ICDR year |  |  |
| R405-R407 | Unit, audit-status and face value INR 2 qualifiers |  | R133-R138 share capital; R329 |
| R408-R409 | BS and CF audit-status qualifiers |  |  |
| R410,R411 | Finance cost and interest paid definitions (excl. lease interest) |  | R232, R234, R288, R290 |
| R377 | ESOP vesting forward statement | FORWARD | R337 |
| R342,R344,R340,R341,R339 | Note section/standard references (Ind AS 108, Section 133, Section 42, Rule 14) |  |  |
| R327-R338 | Note 3/4 numbers |  | see Notes section |

```yaml
stage: A2-enumerator
company: "NETWEB"
quarter: "q2fy27"
doctype: "results"
model: claude-sonnet-5-5
status: complete
ledger_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-netweb-q2fy27-a60c5c/runs/netweb-q2fy27/work/ledger_results_netweb_q2fy27.md"
counts:
  notes: 5
  line_items: 107
  zero_standing: 18
  agenda_items: 2
  auditor_paras: 5
  entities: 22
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, ENTITY_CHANGE, FORWARD, FOOTNOTE_UNRESOLVED, ILLEGIBLE, RESTATED, SINGLE_COLUMN, MISSING_FROM_STRUCTURED]
ids_in_structured: 428
ids_referenced: 428
orphan_ids: []
missing_from_structured: ["Annexure II row 3 'Industry to which entity belongs: Same industry in which we operate' (fulltext L356)"]
gate_a2: pass
mismatch_note: ""
analyst_note: "ZERO_STANDING counts 18 cells across 8 line items; Exceptional items (R067-R072) and non-current Investments (R162-R163) are zero in every period. Five cash-flow lines are dash in one half only (loss on discard PPE, profit on sale PPE, proceeds from sale PPE, IPO expense recovery, share issue proceeds). Board outcome has only two agenda items (results, Taiwan WOS); no dividend, AGM, director or auditor items. Meeting conclusion time and Company Secretary name are illegible, so the signed-before-conclusion test cannot run. Auditor report is an unmodified limited review: no EoM, Other Matter or Going Concern paragraph; ICAI registration reading uncertain. Standalone filing, so no consolidation list to diff; Taiwan WOS is the only ENTITY_CHANGE. Note 3 QIP parking balances (FD 3,500m, monitoring 587.88m, escrow 177.00m) total 4,264.88m against 11,755.76m net proceeds; deployment of the rest is not stated in the filing. Other equity (R139) has a single column."
```

## ORCHESTRATOR ADDENDUM (mechanical ID reconciliation, 2026-10-28, after A1 follow-up)
A1 was resumed once (not a correction loop) to read the page 1 image and to add the A2 MISSING_FROM_STRUCTURED row. Effects on this ledger, no re-classification:
- R428: value now "Board meeting concluded at 2:40 PM (handwritten, read from image)". The ILLEGIBLE flag at ledger line 158 is superseded; the signed-before-conclusion test can now run (start 11:45 AM per R316; conclusion 2:40 PM).
- R351: signatory now read as "Lohit Chhabra, Company Secretary & Compliance Officer". The FOOTNOTE_UNRESOLVED on the CS name is superseded.
- R429 (new, ENTITY, page 7, fulltext line 356) = ledger row MISSING-1 (Annexure II item 3, "Same industry in which we operate"). MISSING-1 is now resolved to R429.
ids_in_structured: 429. ids_referenced: 429. orphan_ids: [].
