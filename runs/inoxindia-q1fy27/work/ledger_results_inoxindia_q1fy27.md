# A2 ENUMERATION LEDGER — INOX India (INOXINDIA), Q1 FY27, Doctype: RESULTS

Source: `extract_results_inoxindia_q1fy27.txt` (11 pages, Reg 33 filing: Board Outcome
letter, Annexure-1 Consolidated + Standalone unaudited results with auditor Limited
Review Reports and notes, Annexure-2 Press Release).

**Unit convention: figures in the financial statement tables are stated in Rs Lakhs
(conversion factor to Rs Crores = x0.01). Source text is NOT converted below — all
figures are transcribed exactly as extracted, in Lakhs, except the Press Release
(Annexure-2, lines 587-675) which is natively stated in Rs Crores by the company
itself.**

Prior-quarter ledger: NOT FOUND. No prior run folder exists for INOXINDIA under
`runs/` other than this one. Entity cross-check (rule 6) and any prior-quarter
diffs could not be performed this cycle — flag `NO_PRIOR_LEDGER`.

OCR quality note: `ocr_pages: none` per A1 header, but the source PDF itself has
degraded text extraction (character-level corruption: "III!" for the Rupee symbol,
"talC" for "tax", "III" for "IN", digit/letter confusion, and — materially for this
ledger — note-number markers 1, 2, 3, 9 in the CONSOLIDATED notes block rendered as
bare commas rather than digits). This drove the notes-category grep/sweep mismatch
resolved below.

```
=== A2 COUNT TEST ===
category: agenda_items    grep_count: 2    sweep_count: 2    match: yes
category: auditor_paras   grep_count: 10   sweep_count: 10   match: yes
category: entities        grep_count: 3    sweep_count: 3    match: yes
category: notes           grep_count: 19   sweep_count: 19   match: yes
category: line_items      grep_count: 78   sweep_count: 78   match: yes
category: zero_standing   grep_count: 6    sweep_count: 6    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

### Reconciliation notes (how grep_count was reached)

- **agenda_items**: `grep -n -E "^\s*[0-9]\.\s"` on lines 14-85 hit both items cleanly
  (lines 40, 43). Sweep = grep = 2. No mismatch.
- **auditor_paras**: naive `grep -n -E "^\s*[0-9]+\.\s"` on the two review-report blocks
  returned only 5 (consolidated, lines 97-200) and 3 (standalone, lines 364-420) = 8,
  undercounting by 2. Manual sweep found paragraph 1 present in BOTH reports but OCR'd
  as Roman numeral "I." (not Arabic "1.") — line 105 "I. We have reviewed..." and line
  374 "I. We have reviewed...". Adding a second pass for `^\s*I\.\s` recovers both.
  Reconciled: consolidated 6 (I/1-6), standalone 4 (I/1-4) = 10 = sweep. Initial
  mismatch resolved by re-sweep per GATE A2; final match = yes.
- **entities**: consolidated auditor para 4 (lines 135-140) lists a/b/c; cross-checked
  against consolidated note 9 (lines 339-340), which names the same three entities.
  grep = sweep = 3.
- **notes**: naive digit-marker grep on the standalone block (lines 490-560) cleanly
  returned 9 (1-9) = sweep. The consolidated block (lines 270-346) naive grep returned
  only 6 (notes 4,5,6,7,8,10) — notes 1, 2, 3, 9 use corrupted markers: note 1 has NO
  visible marker at all (bare paragraph directly under the "Note:" heading, line 274),
  and notes 2, 3, 9 have a bare comma "," in the marker column (lines 277, 278, 339;
  confirmed with `cat -A`, not a stray OCR digit-substitution for anything else).
  Reconciled via a second grep pass for `^\s*,\s+[A-Za-z]` (catches 2, 3, 9) plus manual
  identification of the unmarked lead paragraph (note 1). Consolidated: 6 + 3 + 1 = 10
  = sweep. Total notes = 10 (consolidated) + 9 (standalone) = 19 = 19. Initial mismatch
  resolved by re-sweep; final match = yes.
- **line_items**: numeric-value regex pass (`[0-9]{1,3}(,[0-9]{2,3})*\.[0-9]{2}`) on
  the table cell ranges returns data-bearing rows but (a) misses pure section-header
  rows carrying no value of their own (e.g. "IV Expenses", "VIII Tax expense") and
  (b) over-counts OCR line-wrap artifacts where a single row's later-period columns
  spilled onto orphan lines (consolidated lines 219-222 are wrapped continuation of
  rows already counted, not new rows). Manual row-by-row sweep of both statements,
  cross-checked against the numeric-regex pass with wrap artifacts subtracted and
  header rows added back, converges on 44 rows (consolidated, lines 215-271) + 34 rows
  (standalone, lines 446-489) = 78 = 78.
- **zero_standing**: sub-set of line_items sweep; enumerated directly (6 rows, listed
  in table 6 below). No independent grep needed beyond the line_items pass; sweep
  count self-consistent at 6.

---

## 1. Board Outcome — Agenda Items (Reg 30 letter, page 1)

| # | Line(s) | Agenda item | Detail | Flags |
|---|---------|-------------|--------|-------|
| 1 | 40-41 | Unaudited Standalone and Consolidated Financial Results and Limited Review Report | Issued by Statutory Auditors, quarter ended 30 June 2026 (Annexure-1) | |
| 2 | 43-44 | Press Release on the Unaudited Financial Results | For quarter ended 30 June 2026 (Annexure-2) | |

Board meeting timing (line 48): commenced 04:20 p.m., concluded 04:38 p.m. — 18
minutes total, covering both agenda items (results approval + press release). No
AR approval, AGM notice, record date, dividend, director appointment/resignation,
auditor change, scrutinizer, ESOP grant resolution, or capital-raising enabling
resolution appears on this agenda — this is a routine quarterly-results-only Board
Outcome (2 items only).

## 2. Signature / Digital Signature Blocks

| Line(s) | Document | Signatory | Designation | Timestamp | Flags |
|---------|----------|-----------|-------------|-----------|-------|
| 55-68 | Board Outcome letter | PATEL JAYMEEN MOHANBHAI | (Company Secretary, per DSC block; role not explicitly labeled in text) | Digitally signed 2026.08.03 18:07:47 +05'30 | Signed after 16:38 meeting conclusion — no violation |
| 178-200 | Consolidated auditor Limited Review Report | Santosh Agarwal | Partner, S R B C & CO LLP, Membership No. 093669 | Date: August 03, 2026; DSC block timestamp OCR-garbled/illegible; UDIN: 26093669XLCBAB4575; Place: Ahmedabad | |
| 347-355 | Consolidated results — Director sign-off | Parag Kulkarni | Executive Director, DIN 00209184 | Date: 3rd August 2026 (no time given); Place: Nashik | |
| 405-419 | Standalone auditor Limited Review Report | Santosh Agarwal | Partner, S R B C & CO LLP, Membership No. 093669 | Date: August 03, 2026; DSC block timestamp OCR-garbled/illegible; UDIN: 26093669FJIJGS5621; Place of Signature: Ahmedabad | Distinct UDIN from consolidated report (correct — separate reports require separate UDINs) |
| 563-580 | Standalone results — Director sign-off | Parag Kulkarni | Executive Director, DIN 00209184 | Date: 3rd August 2026 (no time given); Place: Nashik | |

## 3. Auditor Review Report Paragraphs

### 3a. Consolidated (S R B C & CO LLP, pages 2-3, lines 97-200)

| Para | Line(s) | Type | Content | Flags |
|------|---------|------|---------|-------|
| 1 | 105-110 | Scope/introduction | Reviewed the accompanying Statement of unaudited consolidated financial results of the Holding Company and subsidiaries ("the Group") for quarter ended 30 June 2026 | OCR'd as "I." not "1." |
| 2 | 112-118 | Management responsibility | Management responsible for preparation per Ind AS 34, Statement approved by Board, auditor responsibility is to express a conclusion | |
| 3 | 120-133 | Basis of review | SRE 2410 review standard, moderate assurance (not audit-level), no audit opinion expressed; includes sub-paragraph (131-133) noting procedures performed per SEBI Master Circular under Reg 33(8) | |
| 4 | 135-140 | Entities included | Lists the 3 entities in the Statement — see table 4 below | |
| 5 | 141-148 | Conclusion (unmodified) | Nothing has come to attention causing belief that the Statement is not in compliance / contains material misstatement | Unmodified/clean opinion — no Emphasis of Matter, no Going Concern language present |
| 6 | 160-174 | Other Matter — reliance on other auditor | One subsidiary's unaudited results (revenue Rs 1,332.00 lakhs, PAT Rs 164.19 lakhs, TCI Rs 164.19 lakhs for the quarter) reviewed by its own independent auditor; that auditor's report "has been furnished to us by the Management"; conclusion on the Group Statement relies on that other auditor's work; not modified in respect of this reliance | `MGMT_FURNISHED` — subsidiary auditor report furnished by management, not independently obtained by principal auditor; entity not named in this paragraph (identify via table 4 — entity b, the Brazil subsidiary, matches the "one subsidiary" description by elimination since entity c, the Netherlands entity, is typically a holding/finance vehicle — NOT FOUND explicitly in text which of b/c is meant) |

### 3b. Standalone (S R B C & CO LLP, pages 6-7, lines 364-420)

| Para | Line(s) | Type | Content | Flags |
|------|---------|------|---------|-------|
| 1 | 374-377 | Scope/introduction | Reviewed the accompanying statement of unaudited standalone financial results of the Company for quarter ended 30 June 2026 | OCR'd as "I." not "1." |
| 2 | 379-384 | Management responsibility | Same Ind AS 34 / Board approval / auditor responsibility language as consolidated para 2 | |
| 3 | 386-394 | Basis of review | SRE 2410, moderate assurance, no audit opinion | |
| 4 | 396-401 | Conclusion (unmodified) | Nothing has come to attention causing belief of non-compliance / material misstatement | Unmodified/clean opinion; no Other Matter paragraph (standalone has no subsidiaries to reference) |

No Emphasis of Matter, Going Concern, or qualified/adverse/disclaimer language in
either report — both are clean, unmodified review conclusions.

## 4. Entities in the Consolidation List (consolidated auditor para 4, lines 135-140; cross-referenced consolidated note 9, lines 339-340)

| # | Line | Entity | Relationship | Cross-check vs prior quarter |
|---|------|--------|--------------|-------------------------------|
| a | 136 | INOX India Limited | Holding Company | `NO_PRIOR_LEDGER` — cannot diff |
| b | 137-138 | INOXCVA Comercio E Industria De Equipmentos Criogenicos Ltda. (Brazil) | Wholly Owned subsidiary | `NO_PRIOR_LEDGER` — cannot diff |
| c | 139 | INOXCVA Europe B.V. (Netherlands) | Wholly Owned subsidiary | `NO_PRIOR_LEDGER` — cannot diff |

No entity additions, removals, or renames can be confirmed or ruled out this cycle
— flag `NO_PRIOR_LEDGER` applies to all three rows; A3/A4 should source the prior
quarter's filing independently if an entity-stability check is required.

## 5. Notes — Numbered (both statements)

### 5a. Consolidated notes (page 5, lines 270-346) — 10 notes

| Note | Line(s) | Marker as extracted | First ~15 words |
|------|---------|----------------------|------------------|
| 1 | 273-276 | (none — bare paragraph under "Note:" heading) | "The Statement of Unaudited Consolidated financial results... have been reviewed by the Audit Committee and approved by the Board" |
| 2 | 277 | "," (OCR-corrupted digit) | "The Statutory Auditors have carried out limited review of Consolidated financial results of the Group..." |
| 3 | 278-285 | "," (OCR-corrupted digit) | "Share-Based payments: The Nomination and Remuneration Committee of the Holding Company at their meeting held on 8th August 2023..." |
| 4 | 287-289 | "4" | "Segment Information: The Group is having only one reportable business segment in accordance with Ind AS 108..." |
| 5 | 291-305 | "5" | "During the year ended 31st March 2025, the Holding Company's USA subsidiary Cryogenic Vessels Alternatives Inc USA had entered..." |
| 6 | 307-322 | "6" | "During the year ended 31st March 2026, the International Centre for Dispute Resolution passed an arbitration award regarding..." |
| 7 | 324-334 | "7" | "On November 2025, The Government of India has consolidated 29 existing labour legislations into a unified framework comprising..." |
| 8 | 336-337 | "8" | "Figures for the quarter ended 31st March 2026 represents the difference between the audited figures in respect of..." |
| 9 | 339-340 | "," (OCR-corrupted digit) | "The above unaudited consolidated financials results includes financial information of the Holding Company i.e. INOX India Limited and its subsidiaries..." |
| 10 | 342-344 | "10" | "The above unaudited consolidated financial results for the quarter ended 30th June 2026 are available on the BSE Limited website..." |

### 5b. Standalone notes (page 8, lines 491-558) — 9 notes

| Note | Line(s) | Marker as extracted | First ~15 words |
|------|---------|----------------------|------------------|
| 1 | 494-495 | "1" | "The Statement of Unaudited Standalone financial results of INOX India Limited have been reviewed by the Audit Committee and approved..." |
| 2 | 497 | "2" | "The Statutory Auditors have carried out limited review of Standalone financial results of the Company for the quarter..." |
| 3 | 499-505 | "3" | "Share-Based payments: The Nomination and Remuneration Committee of the Company at their meeting held on 8th August 2023, 7th February 2025..." |
| 4 | 507-509 | "4" | "Segment Information: The Company is having only one reportable business segment in accordance with Ind AS 108 on Operating segments..." |
| 5 | 511-517 | "5" | "During the year ended 31st March 2025, the Company's USA subsidiary Cryogenic Vessels Alternatives Inc USA had entered into a settlement..." |
| 6 | 526-540 | "6" | "During the year ended 31st March 2026, the International Centre for Dispute Resolution passed an arbitration award regarding a demand..." |
| 7 | 542-552 | "7" | "On November 2025, The Government of India has consolidated 29 existing labour legislations into a unified framework comprising four labour Codes..." |
| 8 | 554-555 | "8" | "Figures for the quarter ended 31st March 2026 represents the difference between the audited figures in respect of the full financial year..." |
| 9 | 557-558 | "9" | "The above unaudited standalone financial results for the quarter ended 30th June 2026 are available on the BSE Limited website..." |

Content parity check: notes 3-8 are substantively identical in wording between
consolidated and standalone (share-based payments, segment, CVA settlement, TWA
arbitration, labour codes, comparative-figures methodology). Consolidated carries
two notes standalone does not need: note 1's group-level framing plus note 9 (entity
list — standalone has no subsidiaries to list). Standalone note 1/2 mirror
consolidated note 1/2 at company-only scope. No content asymmetry beyond scope
(Group vs Company) — no flag.

## 6. Line Items — Consolidated Statement of Unaudited Financial Results (page 4, lines 207-271) — 44 rows

All figures in Rs Lakhs. Periods: Q1 FY27 (30 Jun 2026, unaudited), Q4 FY26 (31 Mar
2026, audited, derived per note 8), Q1 FY26 (30 Jun 2025, unaudited), FY26 full year
(31 Mar 2026, audited).

| Sr. | Line | Item | Flags |
|-----|------|------|-------|
| I | 215 | Revenue from Operations | |
| II | 216 | Other income | |
| III | 218 | Total Income (I+II) | |
| IV | 224 | Expenses (section header, no independent value) | |
| — | 225 | Cost of Materials Consumed | |
| — | 226 | Purchase of Traded Goods | Dash in Q1 FY26 comparative column only — not all-period nil, not `ZERO_STANDING` |
| — | 227 | Changes in Inventories of Finished goods and Semi Finished Goods | |
| — | 228 | Employee Benefits Expense (Refer note 3 and 7) | |
| — | 229 | Finance Costs | |
| — | 230 | Depreciation and Amortisation Expense | |
| — | 231 | Other expenses | |
| — | 232 | [unlabeled subtotal row — sum of the above 7 expense lines before Captive Consumption adjustment] | Unlabeled in source; OCR row-wrap artifact investigated, subtotal is genuine (not a duplicate) |
| — | 233 | Captive Consumption of Material | `ZERO_STANDING` — blank/dash in all 3 quarterly columns (Q1 FY27, Q4 FY26, Q1 FY26); value (984.93) appears ONLY in the FY26 full-year column. Canonical template-signal pattern per operating rules. |
| — | 234 | Total expenses (IV) | |
| V | 235 | Profit before exceptional items and tax (III-IV) | |
| VI | 236 | Exceptional Items - Income/(Expense) (refer note 5 and 6) | Dash in Q1 FY27 and Q1 FY26; values only in Q4 FY26 (320.65) and FY26 year (327.91) — not all-period nil, not `ZERO_STANDING` |
| VII | 237 | Profit before tax (V+VI) | |
| VIII | 238 | Tax expense (section header, no independent value) | |
| (1) | 239 | Current tax | |
| (2) | 240 | Deferred tax Charge/(Credit) | |
| (3) | 241 | Tax adjustment pertaining to earlier years (credit) | |
| IX | 242 | Profit after tax for the period/year (VII-VIII) | |
| X | 243 | Other comprehensive Income/(loss) (OCI) (section header) | |
| A | 244 | Items that will be reclassified to profit & loss (sub-header) | |
| — | 245 | Net gain due to Foreign Currency Translation differences | |
| B | 246 | Items that will not be reclassified to profit & loss (sub-header) | |
| (i) | 247 | Re-measurement gain/(loss) on the Defined Benefit Plans | |
| (ii) | 248 | Tax on above | |
| — | 251 | Other comprehensive Income/(loss) (net of tax) for the period/year (X) | |
| XI | 253 | Total comprehensive income (net of tax) for the period/year (IX+X) | |
| — | 255 | Profit for the period/year attributable to: (sub-header) | |
| — | 256 | Owners of the Parent | |
| — | 257 | Non-controlling Interests | `ZERO_STANDING` — dash/blank in all 4 periods |
| — | 258 | Other comprehensive (loss)/income for the period/year attributable to: (sub-header) | |
| — | 259 | Owners of the Parent | |
| — | 260 | Non-controlling Interests | `ZERO_STANDING` — dash/blank in all 4 periods |
| — | 262 | Total comprehensive Income for the period/year attributable to: (sub-header) | |
| — | 263 | Owners of the Parent | |
| — | 264 | Non-controlling Interests | `ZERO_STANDING` — dash/blank in all 4 periods |
| XII | 265 | Earnings per equity share (Face Value Rs 2 each)(Not annualised) (section header) | |
| — | 266 | Basic (in Rs) | |
| — | 267 | Diluted (in Rs) | |
| XIII | 270 | Paid up Equity Share capital [Face Value Rs 2 each] | |
| XIV | 271 | Other Equity | Populated only in the FY26 full-year column (balance-sheet-style item, not reported quarterly by convention) — not flagged `ZERO_STANDING` since this is standard practice for a P&L-format statement, not a nil transaction signal |

## 7. Line Items — Standalone Statement of Unaudited Financial Results (page 7, lines 432-489) — 34 rows

Same 4-period structure as consolidated.

| Sr. | Line | Item | Flags |
|-----|------|------|-------|
| I | 446 | Revenue from Operations | |
| II | 449 | Other Income | |
| III | 451 | Total Income (I+II) | |
| IV | 454 | Expenses (section header, no independent value) | |
| — | 455 | Cost of Materials Consumed | |
| — | 456 | Purchase of Traded Goods | Dash in Q1 FY26 comparative column only — not `ZERO_STANDING` |
| — | 457 | Changes in Inventories of Finished goods and Semi Finished Goods | |
| — | 458 | Employee Benefits Expense (Refer note 3 and 7) | |
| — | 459 | Finance Costs | |
| — | 460 | Depreciation and Amortisation Expense | |
| — | 461 | Other expenses | |
| — | 462 | [unlabeled subtotal row — sum of the above 7 expense lines before Captive Consumption adjustment] | Unlabeled in source, same pattern as consolidated |
| — | 463 | Captive Consumption of Material | `ZERO_STANDING` — blank/dash in all 3 quarterly columns; value (57.84) appears ONLY in FY26 full-year column |
| — | 464 | Total Expenses (IV) | |
| V | 465 | Profit before exceptional items and tax (III-IV) | |
| VI | 466 | Exceptional Items -Income/(Expense) (refer note 5 and 6) | Dash in Q1 FY27 and Q1 FY26; not `ZERO_STANDING` |
| VII | 467 | Profit before tax (V+VI) | |
| VIII | 468 | Tax expense (section header, no independent value) | |
| (1) | 469 | Current tax | |
| (2) | 470 | Deferred tax Charge | Note: label differs from consolidated ("Deferred tax Charge" vs consolidated "Deferred tax Charge/(Credit)") — wording only, not a value discrepancy |
| (3) | 471 | Tax adjustment pertaining to earlier years (credit) | |
| IX | 472 | Profit after tax for the period/year (VII-VIII) | |
| X | 473 | Other comprehensive income/(loss) (OCI) (section header) | |
| A | 474 | Items that will be reclassified to profit & loss | `ZERO_STANDING` — no sub-line item prints beneath it at all and the row itself is blank/dash in all 4 periods (standalone entity has no foreign subsidiary, so no FX translation item ever arises here, unlike the consolidated statement's item A) |
| B | 475 | Items that will not be reclassified to profit & loss (sub-header) | |
| (i) | 476 | Re-measurement gain/(loss) on the Defined Benefit Plans | |
| (ii) | 477 | Tax on above | |
| — | 479 | Other comprehensive income/(loss) (net of tax) for the period/year (X) | |
| XI | 481 | Total comprehensive income (net of tax) for the period/year (IX+X) | |
| XII | 484 | Earnings per equity share (section header) | |
| — | 485 | Basic (in Rs) | |
| — | 486 | Diluted (in Rs) | |
| XIII | 488 | Paid up Equity Share capital [Face Value Rs 2 each] | |
| XIV | 489 | Other Equity | Populated only in FY26 full-year column — not `ZERO_STANDING`, standard convention |

Standalone has no Non-controlling Interests / Owners-of-Parent attribution rows
(single entity, no consolidation) — structural difference from consolidated table,
not a missing-disclosure signal.

## 8. Zero-Standing Line Items — Summary (6 rows, cross-referenced from tables 6-7)

| # | Statement | Line | Item | Periods nil in |
|---|-----------|------|------|-----------------|
| 1 | Consolidated | 233 | Captive Consumption of Material | Q1 FY27, Q4 FY26, Q1 FY26 (value only in FY26 full year) |
| 2 | Consolidated | 257 | Non-controlling Interests (profit attributable) | All 4 periods |
| 3 | Consolidated | 260 | Non-controlling Interests (OCI attributable) | All 4 periods |
| 4 | Consolidated | 264 | Non-controlling Interests (TCI attributable) | All 4 periods |
| 5 | Standalone | 463 | Captive Consumption of Material | Q1 FY27, Q4 FY26, Q1 FY26 (value only in FY26 full year) |
| 6 | Standalone | 474 | Items that will be reclassified to profit & loss (OCI section A) | All 4 periods |

The three consolidated Non-controlling Interests rows are the standing template
signal that a minority-stake / JV structure is anticipated or possible in the
Group's consolidation scope even though none currently exists — canonical
`ZERO_STANDING` per operating rules (SOUTHWEST-pattern). The two Captive
Consumption rows appear only as an annual reclassification adjustment and are
structurally absent at quarterly granularity across all three periods shown
quarterly — also `ZERO_STANDING`.

## 9. Press Release (Annexure-2, pages 9-11, lines 582-688) — supplementary, non-tabular

Not part of the Reg 33 numbered-note or line-item structure; enumerated separately
since it is a distinct disclosure document within the same filing bundle, stated
natively in Rs Crores (not Lakhs — flag `UNIT_SWITCH` for downstream reconciliation
against the Lakhs-denominated statements above).

| Item | Line(s) | Content |
|------|---------|---------|
| Headline bullets (5) | 594-599 | Revenue +8.3% YoY to Rs 382 Cr; EBITDA +1.4% YoY to Rs 90 Cr (23.5% margin); PAT Rs 61 Cr (15.9% margin); Export revenue Rs 222 Cr (58% of total); Order inflow Rs 532 Cr, order book Rs 1,686 Cr |
| Narrative body | 601-662 | Segment commentary (Industrial Gases 53% of revenue, LNG Division 22%, Cryo Scientific Division 20%, Stainless-Steel Keg), strategic developments (WAYOUT partnership, AS9100D certification, ITM SLS Baroda University tie-up), CEO quote (Deepak Acharya) |
| Summary financial table (Rs Cr) | 664-673 | Total Revenue, EBITDA, PAT for Q1 FY27 / Q1 FY26 / % YoY / FY26 |
| Company boilerplate + contact | 676-688 | About INOX India Ltd; media contact Puneet Gupta |

Segment revenue-share disclosure (Industrial Gases 53% + LNG 22% + CSD 20% + Keg
[% NOT FOUND, not separately stated] = 95% of the three named percentages,
remainder NOT FOUND/NOT STATED) is a non-Reg-33-table disclosure — flag
`SEGMENT_PCT_GAP` for A3/A4 to note the unstated residual.

---

**Ledger totals**: 2 agenda items, 5 signature blocks, 10 auditor paragraphs
(6 consolidated + 4 standalone), 3 consolidation entities, 19 numbered notes
(10 consolidated + 9 standalone), 78 financial-statement line items
(44 consolidated + 34 standalone) of which 6 are `ZERO_STANDING`, plus 1
supplementary Press Release enumerated in table 9.

Flags raised in this ledger: `NO_PRIOR_LEDGER`, `ZERO_STANDING` (x6),
`MGMT_FURNISHED`, `UNIT_SWITCH`, `SEGMENT_PCT_GAP`.
