# A2 ENUMERATOR — Completeness Ledger
Company: C.E. Info Systems Limited / MapMyIndia (MAPMYINDIA)
Quarter: Q1 FY27
Doctype: results (Reg 33 filing, 9 pages: Board Outcome letter, Consolidated LRR,
Consolidated Statement + Notes, Standalone LRR, Standalone Statement + Notes, Annexure-B)
Source: runs/mapmyindia-q1fy27/work/extract_results_mapmyindia_q1fy27.txt (608 displayed
lines incl. 13-line header; line numbers below are the file's own Read/grep line numbers)
Prior-quarter ledger: NOT PROVIDED — no ENTITY_CHANGE / DROPPED-item diff possible this run.

```
=== A2 COUNT TEST ===
category: agenda_items      grep_count: 2    sweep_count: 2    match: yes
category: auditor_paras     grep_count: 11   sweep_count: 11   match: yes
category: notes             grep_count: 12   sweep_count: 12   match: yes  (see note below)
category: entities           grep_count: 6    sweep_count: 6    match: yes
category: line_items        grep_count: 77   sweep_count: 77   match: yes
category: zero_standing     grep_count: 0    sweep_count: 0    match: yes
category: signature_blocks  grep_count: 7    sweep_count: 7    match: yes
category: annexure_rows     grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

**Reconciliation note on `notes`:** first-pass grep `^\s*[0-9]+\.\s` (dot + required
whitespace) over the whole file returned 25 hits, but that pattern conflates agenda
items (2) + auditor paragraphs (11) + notes (11, one short by an OCR artifact) + one
false positive (line 36, "2015." — a year, not a numbered item). Re-swept with a
relaxed pattern `^\s*[0-9]+\.` restricted to the two notes blocks (lines 290-326 and
485-521) to catch Consolidated Note 2 at line 307, which OCR rendered as
`2.The above statement...` with no space after the dot (strict pattern missed it).
Relaxed-pattern grep = 12, manual line-by-line sweep = 12. Match confirmed; gate
passes only after this re-sweep — recorded per Rule 4.

**Reconciliation note on `line_items`:** 65 main-statement rows (39 consolidated +
26 standalone, grep-confirmed by counting numeric-bearing lines in the statement
line ranges) + 12 note-embedded breakup-table rows (6 consolidated + 6 standalone,
grep on `Sale|Total|Hardware|Software` in the Note 1 sub-tables, manually pruned of
2 sub-table title lines that matched "Total" but carry no value) = 77. Manual sweep
of every row in both statements and both Note-1 sub-tables independently produced 77.

---

## 1. Board Outcome Letter — Agenda Items (page 1)

| # | Line | Item | Detail | Flags |
|---|------|------|--------|-------|
| Meta | 23 | Letter date | August 04, 2026 | |
| Meta | 25-30 | Addressees | BSE Limited (Scrip 543425); NSE (Symbol MAPMYINDIA) | |
| Meta | 32-36 | Subject | Outcome of Board Meeting held Aug 04, 2026, under Reg 30 SEBI LODR | |
| Meta | 42 | Board meeting timing | Commenced 10:30 AM, concluded 3:05 PM (duration ~4h35m for 2 agenda items) | |
| 1 | 45-50 | Agenda item 1 | Board approved Un-Audited Standalone and Consolidated Financial Results + Limited Review Report for Q1 FY27 (qtr ended 30 June 2026), as reviewed/recommended by Audit Committee; attached as Annexure-A | |
| 2 | 53-56 | Agenda item 2 | Mr. Nikhil Kumar (DIN 08583817) stepped down as Whole Time Director of Mappls DT Private Limited (Material WOS) w.e.f. close of business Aug 3, 2026; detail annexed as Annexure-B | |
| Meta | 58 | Closing | "Kindly acknowledge the receipt of the same" | |
| Sig | 62-70 | Signature block | Saurabh Surendra Somani, Company Secretary & Compliance Officer, "For C.E. Info Systems Limited" — no timestamp given, only signatory name/designation | |

Standard Board Outcome categories checked and found ABSENT this quarter (no line
number to cite — confirmed by full-letter read, only 2 numbered items present):
AR approval, AGM notice, record date, dividend declaration, new director
appointment (only a subsidiary WTD cessation is present, not a Company-board
appointment/resignation), statutory auditor change, scrutinizer appointment, ESOP
grant, capital-raising enabling resolution.

agenda_items count = 2 (items 1, 2 only; letter meta/signature rows tracked
separately, not counted toward this category).

---

## 2. Auditor Reports — Paragraph-by-Paragraph (Independent Auditor's Limited Review Reports)

### 2a. Consolidated LRR (pages 2-3, MSKA & Associates LLP)

| Para | Line | First ~15 words | Type | Flags |
|------|------|------------------|------|-------|
| 1 | 94-100 | "We have reviewed the accompanying Statement of consolidated unaudited financial results..." | Scope statement | |
| 2 | 102-107 | "This Statement, which is the responsibility of the Holding Company's Management..." | Management responsibility / Ind AS 34 basis | |
| 3 | 109-118 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410..." | Review basis (no audit opinion expressed) | |
| 4 | 119-132 | "This Statement includes the results of the Holding Company and the following entities:" | Entity list (table, 6 entities — see Section 3) | |
| 5 | 153-158 | "Based on our review conducted and procedures performed as stated in paragraph 3 above..." | Conclusion — unmodified | |
| 6 | 159-167 | "The Statement includes the Group's share of net loss after tax of Rs. 37 lacs..." | Other Matter — 2 associates' interim info NOT reviewed by MSKA, reviewed by other auditors; loss Rs.37 lacs relied upon | `OTHER_MATTER`, `UNAUDITED_BY_PRIMARY_AUDITOR` |
| 7 | 168-181 | "The Statement includes the interim financial information of 1 subsidiary which is not subject to review..." | Other Matter — 1 subsidiary (revenue Nil, net loss Rs.11 lacs) unaudited/unreviewed, mgmt-furnished; JV share of loss Rs.27 lacs also mgmt-furnished/unreviewed; both stated "not material to the Group" | `OTHER_MATTER`, `MGMT_FURNISHED_UNAUDITED` |
| Sig | 182-194 | For M S KA & Associates LLP; Nishit Jain, Partner, Membership No. 409461, UDIN 26409461GMURRF7707 (OCR: "UD IN...GMU RRF7707"), Place New Delhi, Date Aug 4, 2026 | Signature block | `OCR_ARTIFACT` (UDIN spacing) |

### 2b. Standalone LRR (pages 6-7, MSKA & Associates LLP)

| Para | Line | First ~15 words | Type | Flags |
|------|------|------------------|------|-------|
| 1 | 365-369 | "We have reviewed the accompanying statement of standalone unaudited financial results..." | Scope statement | |
| 2 | 371-376 | "This Statement, which is the responsibility of the Company's Management..." | Management responsibility / Ind AS 34 basis | |
| 3 | 377-384 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410..." | Review basis (no audit opinion expressed) | |
| 4 | 385-389 | "Based on our review conducted as stated in paragraph 3 above, nothing has come to our attention..." | Conclusion — unmodified | |
| Sig | 390-402 | For M S KA & Associates LLP; Nishit Jain, Partner, Membership No. 409461, UDIN 26409461XJANAF5754, Place New Delhi, Date Aug 4, 2026 | Signature block | |

Note: standalone report has no Other Matter / entity-list paragraphs (single entity,
no consolidation) — structurally expected, not a gap.

auditor_paras count = 7 (consolidated) + 4 (standalone) = 11.
UDINs differ between the two reports (expected — separate engagements/reports by
the same partner, same date); no red flag.

---

## 3. Entities in the Consolidation (from Consolidated LRR, para 4, lines 119-132)

| Sr.No | Line | Entity | Relationship | Flags |
|-------|------|--------|---------------|-------|
| 1 | 123 | Gtropy Systems Private Limited | Subsidiary | |
| 2 | 125 | Mappls DT Private Limited | Wholly Owned Subsidiary | cross-ref: this is the entity named in Board Outcome agenda item 2 / Annexure-B (WTD Nikhil Kumar cessation) |
| 3 | 126 | C.E. Info Systems International Inc., USA | Wholly Owned Subsidiary | |
| 4 | 128 | Koga Tech Labs Private Limited | Associate | one of the 2 "associates" referenced unreviewed in LRR para 6 (specific which 2 of the listed associates not individually named) |
| 5 | 130 | M/S Prashant Advanced Survey LLP | Associate | see note above |
| 6 | 131 | PT Terra Link Technologies, Indonesia | Joint Venture | this is the JV referenced as mgmt-furnished/unreviewed in LRR para 7 |

entities count = 6. No prior-quarter list supplied — ENTITY_CHANGE comparison not
performed this run (flag would require prior ledger).

Cross-check against auditor paras: para 6 says "2 associates" unreviewed by MSKA —
statement lists exactly 2 associates (rows 4, 5), consistent. Para 7 says "1
subsidiary" not reviewed and "joint venture" (singular) mgmt-furnished — statement
lists exactly 1 JV (row 6); the 3 subsidiaries listed (rows 1-3) are not
individually identified as to which one is the "1 subsidiary" not subject to
review — enumeration gap A3 should chase (cannot be resolved by A2 from this extract).

---

## 4. Consolidated Statement of Unaudited Financial Results — Line Items (page 4, lines 219-282)

Unit: Rupees in lakhs. Columns: Q1FY27 (30.06.2026, Unaudited) | Q4FY26 (31.03.2026,
Audited) | Q1FY26 (30.06.2025, Unaudited) | FY26 (31.03.2026, Audited).

| # | Line | Item | Q1FY27 value | Flags |
|---|------|------|---------------|-------|
| H | 225 | I Revenue (section header, no own value) | — | structural header |
| 1 | 226 | Revenue from operations | 13,972 | |
| 2 | 227 | Other income | 1,965 | |
| 3 | 228 | Total income (subtotal) | 15,937 | |
| H | 229 | II Expenses (section header; OCR "ll Expenses") | — | `OCR_ARTIFACT` |
| 4 | 230 | Cost of materials consumed | 1,483 | |
| 5 | 231 | Purchase of stock in trade | 704 | |
| 6 | 232 | Changes in inventories of finished goods | (20) | negative all periods, not zero |
| 7 | 233 | Employee benefits expense | 2,556 | |
| 8 | 234 | Technical services outsource and project software | 1,325 | |
| 9 | 235 | Finance cost | 18 | |
| 10 | 236 | Depreciation and amortisation expense | 915 | |
| 11 | 237 | Other expenses | 2,312 | |
| 12 | 238 | Total expenses (subtotal) | 9,293 | |
| 13 | 239 | III Profit before tax (header+value combined; OCR "Ill") | 6,644 | `OCR_ARTIFACT` |
| H | 240 | IV Tax expense: (section header, no own value) | — | structural header |
| 14 | 241 | Current tax | 1,699 | |
| 15 | 242 | Deferred tax charge / (benefit) | (93) | |
| 16 | 243 | Taxation related to earlier years | blank | value present only in Q4FY26 (364) and FY26 (374) columns; blank in Q1FY27 and Q1FY26 — not all-period zero, so not `ZERO_STANDING`, but noted |
| 17 | 244 | Total tax expense (subtotal) | 1,606 | |
| 18 | 245 | V Net profit after tax (header+value combined) | 5,038 | |
| H | 246-247 | VI Share of profit/(loss) of associates and JV, equity method (after tax) (section header, no own value) | — | structural header |
| 19 | 248 | Share of profit/(loss) of associates | (37) | |
| 20 | 249 | Share of profit/(loss) of joint venture | (27) | |
| 21 | 250 | Total share of profit/(loss) of associates and JV (subtotal) | (64) | |
| 22 | 251-252 | VII Net Profit after tax incl. share of profit/(loss) of associates and JV | 4,974 | |
| H | 253 | VIII Other comprehensive income, net of taxes (section header, no own value) | — | structural header |
| Sub | 254 | "Items that will not be reclassified to profit and loss" (subheader) | — | structural subheader |
| 23 | 255 | Remeasurements gain/(loss) on defined benefit plans | (12) | |
| 24 | 256 | Income tax effect | 3 | |
| 25 | 257 | IX Total other comprehensive income, net of taxes | (9) | |
| 26 | 258 | X Total comprehensive income | 4,965 | |
| Sub | 259 | "Net profit after tax for the period/year attributable to:" (subheader) | — | |
| 27 | 260 | Owners of the Company | 4,977 | |
| 28 | 261 | Non-controlling interests | (1) [OCR "(J)"] | `OCR_ARTIFACT` |
| 29 | 262 | Total (unlabeled subtotal repeating NPAT) | 4,974 | unlabeled row |
| Sub | 263 | "Other comprehensive income attributable to:" (subheader) | — | |
| 30 | 264 | Owners of the Company | (9) | |
| 31 | 265 | Non-controlling interests | (0) | value shown as "(0)" — near-zero not literal zero across all periods (has 1 in Q4FY26) |
| 32 | 266 | Total (unlabeled subtotal) | (9) | unlabeled row |
| Sub | 267 | "Total comprehensive Income attributable to:" (subheader) | — | |
| 33 | 268 | Owners of the Company | 4,968 | |
| 34 | 269 | Non-controlling interests | (1) [OCR "(J)"] | `OCR_ARTIFACT` |
| 35 | 270 | Total (unlabeled subtotal) | 4,965 | unlabeled row |
| 36 | 271 | Paid-up equity share capital (FV Rs.2, fully paid) | 1,095 | |
| 37 | 272 | Other equity attributable to owners of the Company | blank | only FY26 year-end column populated (89,400); blank in all 3 interim columns — standard interim-reporting convention (balance-sheet item disclosed at year-end only), not `ZERO_STANDING` since not literally zero/nil/dash, simply not disclosed at interim |
| Sub | 273 | "Earnings per equity share (in Rs.)..." (subheader) | — | |
| 38 | 274 | -Basic | 9.09 | |
| 39 | 275 | -Diluted | 9.05 | |
| Sig | 276-282 | Signature block | For and on behalf of the Board, Rakesh Kumar Verma, Managing Director, DIN 01542842, Place New Delhi, Date Aug 4, 2026 | |

Consolidated main-statement line_items = 39 (data rows) + 5 structural headers
(tracked, not counted toward line_items gate figure).

---

## 5. Standalone Statement of Unaudited Financial Results — Line Items (page 7, lines 424-469)

| # | Line | Item | Q1FY27 value | Flags |
|---|------|------|---------------|-------|
| H | 430 | I Revenue (section header) | — | structural header |
| 1 | 431 | Revenue from operations | 12,448 | |
| 2 | 432 | Other income | 1,838 | |
| 3 | 433 | Total Income (subtotal) | 14,286 | |
| H | 434 | II Expenses (section header) | — | structural header |
| 4 | 435 | Cost of materials consumed | blank | value present only in Q4FY26 (7) and FY26 (7) columns; blank in Q1FY27 and Q1FY26 — not all-period, so not `ZERO_STANDING`, noted |
| 5 | 436 | Purchase of stock in trade | 2,118 | |
| 6 | 437 | Changes in inventories of finished goods | (118) | |
| 7 | 438 | Employee benefits expense | 1,353 | |
| 8 | 439 | Technical services outsource and project software | 1,981 | |
| 9 | 440 | Finance cost | 17 | |
| 10 | 441 | Depreciation and amortisation expense | 544 | |
| 11 | 442 | Other expenses | 1,084 | |
| 12 | 443 | Total expenses (subtotal) | 6,979 | |
| 13 | 444 | III Profit before tax (header+value; OCR "Ill") | 7,307 | `OCR_ARTIFACT` |
| H | 445 | IV Tax expense: (section header) | — | structural header |
| 14 | 446 | Current tax | 1,692 | |
| 15 | 447 | Deferred tax charge / (benefit) | 73 | |
| 16 | 448 | Taxation related to earlier years | blank | value present only Q4FY26 (363) and FY26 (363); blank Q1FY27/Q1FY26, noted |
| 17 | 449 | Total tax expense (subtotal) | 1,765 | |
| 18 | 450 | V Net profit after tax | 5,542 | |
| H | 451 | VI Other comprehensive income, net of taxes (section header) | — | structural header |
| Sub | 452 | "Items that will not be reclassified to profit and loss" (subheader) | — | |
| 19 | 453 | Remeasurements gain/(loss) on defined benefit plans | (11) | |
| 20 | 454 | Income tax effect | 3 | |
| 21 | 455 | VII Total other comprehensive income, net of taxes | (8) | |
| 22 | 456 | VIII Total comprehensive income | 5,534 | |
| 23 | 457 | Paid-up equity share capital (FV Rs.2, fully paid) | 1,095 | |
| 24 | 458 | Other equity | blank | only FY26 year-end column populated (92,027); interim convention, not `ZERO_STANDING` |
| Sub | 459 | "Earnings per equity share (in Rs.)..." (subheader) | — | |
| 25 | 460 | -Basic | 10.12 | |
| 26 | 461 | -Diluted | 10.08 | |
| Sig | 462-469 | Signature block | For and on behalf of the Board, Rakesh Kumar Verma, Managing Director, DIN 01542842, Place New Delhi | `MISSING_DATE_LINE` — no "Date:" line present in this block, unlike the parallel Consolidated Statement (line 282), Consolidated Notes (line 326) and Standalone Notes (line 521) signature blocks, all of which carry "Date: August 4, 2026" |

Standalone main-statement line_items = 26 (data rows) + 4 structural headers
(tracked, not counted toward line_items gate figure).

Structural difference (expected, not a gap): standalone statement has no
"Share of profit/(loss) of associates and JV" section and no NCI attribution
splits — correct, standalone is single-entity.

---

## 6. Notes to the Financial Results

### 6a. Consolidated Notes (page 5, lines 290-326)

| Note | Line | First ~15 words | Flags |
|------|------|------------------|-------|
| 1 | 291-306 | "The figures of revenue from operations consist of Sale of hardware and Sale of Map data..." — includes 2 embedded breakup tables (see below) | |
| 2 | 307-311 | "The above statement of unaudited consolidated financial results...prepared in accordance with the Indian Accounting Standards..." — Board approval dates Aug 3 & Aug 4, 2026; unmodified LRR | `OCR_ARTIFACT` (rendered "2.The" with no space, missed by strict grep) |
| 3 | 312-313 | "The consolidated annual financial results include the results for the quarter ended March 31, 2026 being the balancing figure..." | referenced by "(refer note J)" at line 224 — OCR garble for "note 3" |
| 4 | 314-315 | "The above audited Consolidated Financials Results...are available on Company's website...and also on the website of BSE...and NSE..." | |
| 5 | 316-318 | "As the Group's business activities fall within a single primary business segment viz. 'Map data and Map data related services and devices...'" — Ind AS 108 segment disclosure not applicable | |
| 6 | 319 | "The previous periods'/year's figures have been regrouped/rearranged wherever necessary to conform to the current period's presentation." | |
| Sig | 320-326 | For and on behalf of the Board, Rakesh Kumar Verma, Managing Director, DIN 01542842, Place New Delhi, Date Aug 4, 2026 | |

**Note 1 embedded breakup tables (Consolidated):**

| Table | Line | Row | Q1FY27 value |
|-------|------|-----|---------------|
| Revenue from operations | 297 | Sale of devices | 2,311 |
| Revenue from operations | 298-299 | Sale of Map data and services (incl. royalty, annuity, subscription, software, MAAS/PAAS/SAAS) | 11,661 |
| Revenue from operations | 300 | Total (subtotal, ties to statement line 226) | 13,972 |
| Total cost of material | 304 | Hardware material | 1,524 |
| Total cost of material | 305 | Software material including SIM rental | 643 |
| Total cost of material | 306 | Total (subtotal) | 2,167 |

### 6b. Standalone Notes (page 8, lines 485-521)

| Note | Line | First ~15 words | Flags |
|------|------|------------------|-------|
| 1 | 486-501 | "The figures of revenue from operations consist of Sale of hardware and Sale of Map data..." — includes 2 embedded breakup tables (see below) | |
| 2 | 502-506 | "The above statement of unaudited standalone financial results...prepared in accordance with the Indian Accounting Standards..." — Board approval dates Aug 3 & Aug 4, 2026; unmodified LRR | |
| 3 | 507-508 | "The standalone annual financial results include the results for the quarter ended March 31, 2026 being the balancing figure..." | referenced by "(refer note 3)" at line 429 (this one legible, unlike consolidated's line 224 OCR garble) |
| 4 | 509-510 | "The above unaudited Standalone Financials Results...are available on Company's website...and also on the website of BSE...and NSE..." | |
| 5 | 511-513 | "As the Company's business activities fall within a single primary business segment viz. 'Map data and Map data related services and devices...'" — Ind AS 108 segment disclosure not applicable | |
| 6 | 514 | "The previous periods'/year's figures have been regrouped/rearranged wherever necessary to conform to the current period's presentation." | |
| Sig | 515-521 | For and on behalf of the Board, Rakesh Kumar Verma, Managing Director, DIN 01542842, Place New Delhi, Date Aug 4, 2026 | |

**Note 1 embedded breakup tables (Standalone):**

| Table | Line | Row | Q1FY27 value |
|-------|------|-----|---------------|
| Revenue from Operations | 492 | Sale of Devices | 1,983 |
| Revenue from Operations | 493-494 | Sale of Map data and services (incl. royalty, annuity, subscription, software, MAAS/PAAS/SAAS) | 10,465 |
| Revenue from Operations | 495 | Total (subtotal, ties to statement line 431) | 12,448 |
| Total cost of material | 499 | Hardware material | 1,884 |
| Total cost of material | 500 | Software material including SIM rental | 116 |
| Total cost of material | 501 | Total (subtotal) | 2,000 |

notes count = 6 (consolidated) + 6 (standalone) = 12.
Both note sets are textually near-identical in structure/wording (Consolidated vs
Standalone mirror each other note-for-note 1-6) — expected, not a gap.

---

## 7. Annexure-B — Director/KMP Change Disclosure (page 9, lines 551-582)

Subject: Cessation of Mr. Nikhil Kumar (DIN 08583817) as Whole Time Director of
Mappls DT Private Limited (Material Wholly Owned Subsidiary), per Reg 30 SEBI LODR
and SEBI Circular HO/49/14/14(7)2025-CFD-POD2/I/3762/2026 dated 30 Jan 2026.

| Row | Line | Particular | Detail | Flags |
|-----|------|------------|--------|-------|
| a | 565-567 | Reason for change | Stepped down as WTD of Mappls DT Private Limited | |
| b | 568-569 | Date of appointment/cessation & terms | Closure of business hours of August 03, 2026 | |
| c | 571-572 | Brief profile in case of appointment | NA | this is a cessation, not appointment — NA is correct, not a gap |
| d | 574-577 | Disclosure of relationships between directors | NA | |
| e | 578-582 | Info per BSE Circular LIST/COMP/14/2018-19 and NSE Circular NSE/CM/2018/24 (both dated 20 June 2018) | NA | |

annexure_rows count = 5. Note: this is a subsidiary-level WTD change, not a Company
board-level director appointment/resignation — no Company-level KMP change disclosed
this quarter.

---

## 8. Digital / Physical Signature Blocks — Full Sweep

| # | Line | Signatory | Designation | Timestamp | Flags |
|---|------|-----------|-------------|-----------|-------|
| 1 | 69-70 | Saurabh Surendra Somani | Company Secretary & Compliance Officer | none given (letter dated Aug 4, 2026 at top of letter, line 23; no time-of-day) | |
| 2 | 188-194 | Nishit Jain (MSKA & Associates LLP) | Partner | Date Aug 4, 2026; Place New Delhi; UDIN 26409461GMURRF7707 | `OCR_ARTIFACT` |
| 3 | 276-282 | Rakesh Kumar Verma | Managing Director (DIN 01542842) | Date Aug 4, 2026; Place New Delhi | Consolidated Statement sign-off |
| 4 | 320-326 | Rakesh Kumar Verma | Managing Director (DIN 01542842) | Date Aug 4, 2026; Place New Delhi | Consolidated Notes sign-off |
| 5 | 396-402 | Nishit Jain (MSKA & Associates LLP) | Partner | Date Aug 4, 2026; Place New Delhi; UDIN 26409461XJANAF5754 | |
| 6 | 462-469 | Rakesh Kumar Verma | Managing Director (DIN 01542842) | none given | `MISSING_DATE_LINE` |
| 7 | 515-521 | Rakesh Kumar Verma | Managing Director (DIN 01542842) | Date Aug 4, 2026; Place New Delhi | Standalone Notes sign-off |

signature_blocks count = 7. No signature block carries a time-of-day timestamp, so
none can be checked against the board meeting's 10:30 AM-3:05 PM window (line 42)
for a before-meeting-concluded anomaly — data limitation, not a finding.

---

## 9. Zero / Nil / Dash Standing Line Items — Explicit Check

No line item in either statement is zero, nil, or dash across ALL FOUR reporting
periods. Three items are blank in 2-of-4 columns ("Taxation related to earlier
years" in both statements, "Cost of materials consumed" in standalone) and two
items are populated in only the FY26 year-end column ("Other equity" in both
statements, standard for interim reporting) — none qualify as `ZERO_STANDING`
under the all-periods rule; each is annotated in Sections 4-5 above with its exact
line number so the partial-blank pattern is not silently lost.

zero_standing count = 0.

---

```yaml
stage: A2-enumerator
company: "MAPMYINDIA"
quarter: "Q1 FY27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/mapmyindia-q1fy27/work/ledger_results_mapmyindia_q1fy27.md"
counts:                      # per applicable category
  notes: 12
  line_items: 77
  zero_standing: 0
  agenda_items: 2
  auditor_paras: 11
  entities: 6
  signature_blocks: 7
  annexure_rows: 5
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [OTHER_MATTER, UNAUDITED_BY_PRIMARY_AUDITOR, MGMT_FURNISHED_UNAUDITED, OCR_ARTIFACT, MISSING_DATE_LINE]
gate_a2: pass                # pass | fail
mismatch_note: ""            # non-empty only if gate_a2 fail
```
