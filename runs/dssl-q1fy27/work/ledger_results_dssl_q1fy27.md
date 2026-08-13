# A2 COMPLETENESS LEDGER — Dynacons Systems & Solutions Ltd (DSSL) — Results Filing — Q1 FY27

Source: `extract_results_dssl_q1fy27.txt` (6 pages, 409 lines, 100% page coverage, no OCR pages flagged in header — but see OCR_MISALIGNMENT flag below re: the combined P&L statement table on page 5, whose column alignment is visibly scrambled in the raw extract).

Prior-quarter ledger: not provided to this run. Entity-list / dropped-slide / dropped-note diffing against Q4 FY26 could not be performed. Flag: `PRIOR_LEDGER_UNAVAILABLE`.

```
=== A2 COUNT TEST ===
category: notes            grep_count: 5    sweep_count: 5    match: yes
category: agenda_items     grep_count: 2    sweep_count: 2    match: yes
category: auditor_paras    grep_count: 11   sweep_count: 11   match: yes   (3 standalone + 8 consolidated)
category: entities         grep_count: 3    sweep_count: 3    match: yes   (1 holding + 2 subsidiaries)
category: line_items       grep_count: 36   sweep_count: 36   match: yes   (combined Standalone+Consolidated statement, page 5)
category: segment_rows     grep_count: 13   sweep_count: 13   match: yes   (consolidated segment table, page 6)
category: signature_blocks grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Reconciliation notes on method (shown for audit trail, per GATE A2 discipline):
- **notes**: first grep pass `^\s*[0-9]\)` found only 4 of 5 (missed note 2, which the OCR rendered as `2}` not `2)` — a curly-brace glyph substitution). Re-ran with `^\s*[0-9][\)}]` → 5/5, matching manual sweep of lines 315–331.
- **auditor_paras**: naive blank-line-block count on the Consolidated LRR (lines 137–198) returned 9 blocks; one block (lines 165–169) was the page-4 letterhead reprint (firm name/address), a pagination artifact, not a paragraph. Excluding it, both grep block-count and manual read converge on 8 Consolidated paragraphs (+3 Standalone = 11 total).
- **line_items**: first regex pass over the page-5 statement (lines 237–312) caught 29 of 36 rows; missed the three repeated "Shareholders of the Company" / "Non/Nan Controlling Interest" sub-rows (anchored regex over-specified on leading whitespace) and the "Basic" EPS row (trailing `$` anchor broken by trailing value text on the same line). Loosened patterns → 36/36, matching manual sweep.
- **segment_rows**: first regex `[0-9],[0-9]{3}\.[0-9]{2}` (comma-grouped values only) caught 11 of 13; missed two rows whose values are under 1,000 and therefore have no comma ("Technology Workforce Augmentation Services" segment result, 142.92; "Other income", 155.65). Widened to `[0-9]+\.[0-9]{2}` → 13/13.

---

## 1. BOARD OUTCOME LETTER — agenda items (page 1)

| # | Line | Item | Detail | Flags |
|---|------|------|--------|-------|
| 1 | 38–40 | Financial results approval | IND-AS compliant Standalone and Consolidated Un-Audited Financial Results along with Limited Review Report for Q1 FY27 (quarter ended June 30, 2026), Reg. 33 | — |
| 2 | 41 | Interim Dividend | Rs. 0.50 per equity share of Rs. 10 each (5% of face value) | — |

Categories checked and confirmed **absent** from this Board Outcome letter (swept for, not present): AR/annual accounts approval, AGM notice, director appointment/resignation, auditor appointment/change, scrutinizer appointment, ESOP grant, capital-raising enabling resolution. This is a narrow, two-item results+dividend outcome letter.

Supporting board-meeting mechanics (not agenda items themselves, logged as data points):
| Line | Data point | Value | Flags |
|------|-----------|-------|-------|
| 43–46 | Record date | Wednesday, August 19, 2026 | — |
| 43 | Dividend payment date | Thursday, August 27, 2026 | — |
| 320 (Note 3) | Cash outgo on interim dividend | Rs. 63.69 lakhs | cross-ref to Note 3 |
| 48 | Board meeting start | 05:00 p.m. | — |
| 48 | Board meeting end | 07:00 p.m. | Duration 2h — substantive, not a rubber-stamp short meeting |

---

## 2. STANDALONE + CONSOLIDATED FINANCIAL RESULTS TABLE (page 5, lines 237–312)

Single physical table with parallel Standalone and Consolidated column blocks (4 periods each: 3M Jun-26 unaudited, preceding 3M Mar-26 audited, corresponding 3M Jun-25 unaudited, year-to-date/FY26 audited). Every row below is a line item in **both** the Standalone and the Consolidated table.

| # | Line | Line item | Standalone 3M Jun-26 | Consolidated 3M Jun-26 | Flags |
|---|------|-----------|----------------------:|------------------------:|-------|
| 1 | 237 | Income from Operations (header) | — | — | header row |
| 2 | 239 | a) Net Sales/Income from operations | value present | value present | OCR_MISALIGNMENT — value/label row-shift suspected, see below |
| 3 | 241 | b) Other Income | 155.65 | 213.01 | — |
| 4 | 243 | Total Income from Operations | ~31,274.98 | 31,368.83 | delta vs consolidated — see §5 |
| 5 | 244 | Expenses (header) | — | — | header row |
| 6 | 246 | a) Cost of material consumed | (361.18) | 1,978.62 | — |
| 7 | 248 | b) Changes in Inventories | 1,310.58 | 1,356.43 | — |
| 8 | 251 | c) Employee benefits expense | 720.40 | 673.87 | — |
| 9 | 253 | d) Finance Costs | 808.92 | 626.83 | — |
| 10 | 255 | e) Depreciation and amortization expense | 705.02 | 689.73 | label "e)" dropped by OCR, only ")" visible |
| 11 | 257 | f) Other expenses | 28,656.08 | 37,914.79 | — |
| 12 | 259 | Total expenses (a to f) | ~25,472.34 | 32,589.27 | — |
| 13 | 262 | Profit before tax | 2,618.89 | 2,645.19 | — |
| 14 | 263 | Tax expense | 662.56 | 665.64 | — |
| 15 | 266 | Net Profit for the period | 1,956.34 | 1,979.55 | delta vs consolidated — see §5 |
| 16 | 267 | Other comprehensive income (header) | — | — | header row |
| 17 | 268 | A(i) Items that will not be reclassified to P&L | 0.21 | 0.21 | — |
| 18 | 270 | — Remeasurement of defined Benefit Plans | 5.49 | 5.89 | — |
| 19 | 272–275 | — Gains and losses from investments in equity instruments | 0.00 | 0.00 | **ZERO_STANDING** — nil in all 4 periods, both books |
| 20 | 276 | — Foreign Exchange Gains or loss | (blank/nil visible) | (blank/nil visible) | possible ZERO_STANDING, confirm against source PDF (OCR too degraded to be certain of value) |
| 21 | 279–280 | A(ii) Income tax relating to items that will not be reclassified | (1.23) | (1.23) | — |
| 22 | 281 | *(unlabeled row — all "=" / "−" across periods)* | — | — | **ZERO_STANDING + EXTRACTION_GAP** — this is almost certainly the standard "B(ii) Income tax relating to items that will be reclassified to profit or loss" line (nil in all periods); its text label did not survive OCR. Flag for A3/A4: verify against source PDF before treating as a genuine omission. |
| 23 | 283 | B(i) Items that will be reclassified to profit or loss | 4.87 | 4.87 | — |
| 24 | 285 | Total other comprehensive income (A(i-ii)+B(i-ii)) | 1,956.38 (approx, garbled) | 1,984.42 | label OCR'd as "Tatal" |
| 25 | 286 | Total comprehensive income | 1,961.20 | 1,978.36 (approx, garbled) | — |
| 26 | 288 | Profit for the year attributable to (header) | — | 1,961.74 / 8,475.32 (YTD cols) | header row; Standalone columns blank — structural, standalone entity has no NCI |
| 27 | 290 | — Shareholders of the Company | blank/dash on Standalone | 1,973.49 | **NOT_APPLICABLE (standalone)** |
| 28 | 291 | — Non Controlling Interest (OCR: "Nan") | blank/dash on Standalone | 6.07 (approx) | **NOT_APPLICABLE (standalone)** |
| 29 | 294 | OCI for the year, net of tax, attributable to (header) | — | — | header row |
| 30 | 297 | — Shareholders of the Company | blank/dash (all "=" shown) | 19.71 / (4.79) / (1.00) | **ZERO_STANDING/NOT_APPLICABLE (standalone)** |
| 31 | 298 | — Non Controlling Interest | 4.87 | 4.87 | — |
| 32 | 299 | Total comprehensive income for the year attributable to (header) | — | — | header row |
| 33 | 301 | — Shareholders of the Company | blank/dash on Standalone | 1,978.36 (approx) | **NOT_APPLICABLE (standalone)** |
| 34 | 302 | — Non Controlling Interest | blank/dash on Standalone | 6.07 (approx) | **NOT_APPLICABLE (standalone)** |
| 35 | 306 | Paid up equity share capital | 1,273.71 | 1,273.71 | — |
| 36a | 307–310 | Earnings Per Share (Face value Rs.10) — Basic | 15.36 | 15.54 | delta vs consolidated — see §5 |
| 36b | 311–312 | Earnings Per Share (Face value Rs.10) — Diluted | 15.36 | 15.54 | — |

**OCR_MISALIGNMENT flag (table-wide):** the raw extract of this statement (lines 237–312) has numeric values and row labels visibly interleaved out of column order in several places (e.g., row 239 "a) Net Sales" appears to carry values that read more consistently as the "b) Other Income" row's data, and several totals such as line 243/259/285/300 show numbers materially larger than any plausible sum of the rows above them — e.g. Total Income from Operations at line 241 shows "1,42,839.81" which is a year-to-date-scale figure bleeding into a quarterly cell). **A3/A4 should re-derive all Standalone P&L values from the source PDF table directly rather than trust the OCR'd numeric-to-label mapping in this extract.** The row *labels* themselves (what is enumerated above) are reliable; the *values* attached to each label in the raw extract are not, due to column-shift OCR corruption.

---

## 3. NOTES TO THE RESULTS (page 5, lines 315–331)

| Note # | Line | First ~15 words | Flags |
|--------|------|------------------|-------|
| 1 | 315–316 | "The above unaudited financial results were reviewed by the Audit Committee at its meeting held on…" | — |
| 2 | 318–319 | "The unaudited financial results of the Company for the quarter ended June 30, 2026 have…" (subject to limited review by Statutory Auditors) | OCR rendered numeral as "2}" not "2)" |
| 3 | 320 | "The Board of Directors have declared a Interim dividend of Rs.0.50 per equity share of…" (cash outgo Rs. 63.69 lakhs) | cross-ref Board Outcome item 2 |
| 4 | 321–322 | "The figures for the previous period have been regrouped and re-arranged, wherever necessary, to…" | standard boilerplate |
| 5 | 322–331 | "The Company operates in the segment of Systems integration and Services. The Company…" (identifies Technology Workforce Augmentation Services as a new focus business segment; two operating segments now reported; prior period restated) | **new reportable segment introduced this quarter — segment comparatives restated. Flag for A3: new-segment disclosure is a material structural change worth forensic attention.** |

No unnumbered footnotes, asterisked notes, or "Note:"-prefixed items found below either table on manual sweep (one stray unattached asterisk artifact at line 293/307 is an OCR table-border remnant, not a footnote marker — confirmed by absence of any corresponding footnote text).

---

## 4. AUDITOR REVIEW REPORTS (pages 2–4)

### 4a. Standalone LRR (MSP & CO., pages 2) — 3 paragraphs
| Para | Line | Content |
|------|------|---------|
| 1 | 86–90 | Scope statement — reviewed unaudited Standalone results for quarter ended June 30, 2026, Board-approved statement, management responsibility |
| 2 | 92–99 | Basis of review — SRE 2410, moderate assurance, less than an audit, no audit opinion expressed |
| 3 | 101–106 | Conclusion — unmodified: nothing came to attention indicating non-disclosure per Reg. 52 or material misstatement |

Opinion type: **unmodified/clean**. No Emphasis of Matter, no Other Matters, no Going Concern language. UDIN: 26008684 GRIDZ7853 (line 121). Signatory block: For MSP & CO., Firm Regn. No. 107565W, Membership No. 08684, Mumbai, August 13, 2026 (lines 111–120) — partner name not printed in this block (only membership number); partner identified by name only in the Consolidated report signature.

### 4b. Consolidated LRR (MSP & CO., pages 3–4) — 8 paragraphs
| Para | Line | Content |
|------|------|---------|
| 1 | 137–141 | Scope — reviewed Consolidated results of Holding Company + subsidiaries ("the Group") for Q1 FY27 |
| 2 | 143–148 | Basis of preparation — Ind AS 34, Companies Act 2013 Sec. 133 |
| 3 | 150–158 | Basis of review — SRE 2410, scope less than audit, no audit opinion |
| 4 | 161–163 | Additional SEBI Reg. 33(8) circular procedures performed |
| 5 | 172–175 | Entity list (Other Matter component) — see §6 below |
| 6 | 177–184 | Conclusion — unmodified: nothing came to attention re: non-disclosure per Reg. 33 or material misstatement (explicitly cross-references "paragraph 3" and "paragraph 6" in its own text — confirms source PDF numbering ran at least to para 6; extract only captured explicit numerals for paras 1 and 3, para 2 rendered as "Ds," by OCR) |
| 7 | 186–197 | Other Matter — 2 unaudited subsidiaries (1 domestic, 1 foreign); aggregate revenue Rs. 249.50 lakhs, aggregate PAT Rs. 23.22 lakhs for the quarter; domestic subsidiary reviewed directly by MSP&CO; foreign subsidiary financials management-furnished and prepared under foreign GAAP, converted to Ind AS by Holding Company management, conversion adjustments audited by MSP&CO |
| 8 | 198 | Closing sentence — "Our opinion on the Statement is not modified in respect of the above matter." |

Opinion type: **unmodified/clean**, with an explicit **Other Matter** paragraph (para 7) covering the two unaudited subsidiaries — standard, not a red flag by itself, but the identity of "which entities are unaudited/management-furnished" is exactly the fact A3 should carry forward (foreign subsidiary = management-furnished, not independently reviewed by MSP&CO; only the Ind-AS conversion adjustments were audited). UDIN: 26008684W VDLLB7870 (line 211). Signatory: Madhusudan Parikh, Partner, Membership No. 08684, Mumbai, August 13, 2026 (lines 201–210).

Flag: `EXTRACTION_GAP` on paragraph numbering — paras 2, 4, 5 lost their source numerals to OCR (confirmed via the report's own internal cross-reference to "paragraph 6"); content is intact, only the numeral labels are missing from the extract.

---

## 5. CONSOLIDATION ENTITY LIST (Consolidated LRR, lines 172–175)

| # | Line | Entity | Relationship | Flags |
|---|------|--------|--------------|-------|
| i | 173 | Dynacons Systems and Solutions Ltd | Holding Company | — |
| ii | 174 | Dynacons Systems and Solutions PTE Limited | Subsidiary Company (foreign, unaudited/management-furnished) | — |
| iii | 175 | Cybercons Infosec Private Limited | Subsidiary Company (domestic, reviewed by MSP&CO) | — |

Total entities in consolidation: 3 (1 holding + 2 subsidiaries). Cross-referenced against Other Matter paragraph (line 186: "unaudited financial results in respect of 2 subsidiaries, one subsidiary in India and other subsidiary outside India") — consistent, 2 subsidiaries confirmed twice in the document.

No prior-quarter entity list was supplied to this run, so `ENTITY_CHANGE` cannot be tested. Flag: `PRIOR_LEDGER_UNAVAILABLE` — A3/A4 should pull the Q4 FY26 consolidated LRR entity list independently to check for additions/removals/renames.

---

## 6. SEGMENT INFORMATION — Consolidated (page 6, lines 358–389)

| # | Line | Row | 3M Jun-26 | Flags |
|---|------|-----|----------:|-------|
| 1 | 369 | Segment Revenue — System Integration | 31,061.06 | — |
| 2 | 370 | Segment Revenue — Technology Workforce Augmentation Services | 307.77 | new segment (Note 5) |
| 3 | 371 | Segment Revenue — Total Income from Operations | 31,368.83 | ties to consolidated statement total, page 5 |
| 4 | 375 | Segment Results — System Integration | 3,875.95 | — |
| 5 | 376 | Segment Results — Technology Workforce Augmentation Services | 142.92 | new segment (Note 5) |
| 6 | 377 | Segment Results — Total (unlabeled subtotal row) | 4,018.87 | label itself not printed, only the total figure |
| 7 | 379 | Finance Costs | 720.40 | — |
| 8 | 380 | Unallocable Expenses (OCR: "Expences") | 808.92 | — |
| 9 | 381 | Other income | 155.65 | — |
| 10 | 382 | Profit before tax | 2,645.19 | ties to consolidated statement, page 5 |
| 11 | 383 | Tax expense | 665.64 | ties to consolidated statement, page 5 |
| 12 | 384 | Profit after tax | 1,979.55 | ties to consolidated statement, page 5 |
| 13 | 386–389 | Segment Assets and Liabilities | narrative — **not disclosed**: "not identified with any of the operating segments… currently not practicable to provide segment disclosures relating to total assets and total liabilities" | `DISCLOSURE_NOT_PROVIDED` — a standing non-disclosure, flagged for A3/A4 rather than dropped |

Note: this segment table cross-checks cleanly against the (garbled) page-5 consolidated statement for Total Income from Operations, PBT, Tax expense and PAT — useful as the reliable numeric anchor for A3/A4 given the OCR_MISALIGNMENT flag on the page-5 table itself.

---

## 7. STANDALONE-VS-CONSOLIDATED DELTAS (first-class ledger entries)

| Metric | Line(s) | Standalone 3M Jun-26 | Consolidated 3M Jun-26 | Delta | Flags |
|--------|---------|----------------------:|------------------------:|------:|-------|
| Revenue (Total Income from Operations) | 243 (Standalone, garbled) vs 371 (segment table, clean) | ~31,274.98 | 31,368.83 | ~93.85 lakhs | Standalone figure sourced from OCR-degraded cell — treat as approximate; consolidated figure is clean (segment table cross-check) |
| Net Profit (PAT) | 266 | 1,956.34 | 1,979.55 | ~23.21 lakhs | Delta is consistent with the auditor's Other Matter disclosure of aggregate subsidiary PAT = Rs. 23.22 lakhs (line 189) — internally coherent despite table OCR noise |
| EPS Basic | 308–310 | 15.36 | 15.54 | 0.18 | — |
| EPS Diluted | 311–312 | 15.36 | 15.54 | 0.18 | — |

---

## 8. DIGITAL SIGNATURE / SIGNATORY BLOCKS

| # | Line | Signatory | Designation | Document | Timestamp | Flags |
|---|------|-----------|-------------|----------|-----------|-------|
| 1 | 54–63 | Pooja Girish Patwa | Company Secretary & Compliance Officer (Mem. No. A60986) | Board Outcome letter | Digitally signed 2026.08.13 19:07:53 +05'30' | Meeting concluded 19:00; signature 7 minutes later — consistent, **no premature-signature flag** |
| 2 | 111–121 | [MSP & CO., Membership No. 08684 — partner name not printed in this block] | Chartered Accountants, Firm Regn. 107565W | Standalone LRR | Mumbai, August 13, 2026 (no digital timestamp captured, UDIN present) | — |
| 3 | 201–211 | Madhusudan Parikh, Partner (Mem. No. 08684) | Chartered Accountants, Firm Regn. 107565W | Consolidated LRR | Mumbai, August 13, 2026 (no digital timestamp captured, UDIN present) | — |
| 4 | 333–343 | Dharmesh Anjaria | Whole-time Director, DIN 00445009 | Standalone/Consolidated Results statement | Mumbai, August 13, 2026 (no digital timestamp captured) | — |
| 5 | 394–396 | Dharmesh S. Anjaria | Whole-time Director & CEO (title truncated in OCR) | Segment Information table | Mumbai, August 13, 2026 (no digital timestamp captured) | — |

Only signature block 1 (Company Secretary, Board Outcome letter) carries an explicit digital-signature timestamp in the extract; the LRRs and results statement/segment table show only date, no time-of-day — consistent with how these particular signature blocks are typically rendered (not necessarily an extraction gap, but noted for completeness).

---

## SUMMARY OF FLAGS RAISED FOR A3

1. `ZERO_STANDING` — Gains/losses from investments in equity instruments, nil across all periods and both books (row 19, line 272–275).
2. `ZERO_STANDING` + `EXTRACTION_GAP` — unlabeled all-dash OCI row (line 281), almost certainly "B(ii) Income tax relating to items that will be reclassified to P&L," nil in all periods; label lost to OCR — verify against source PDF.
3. `NOT_APPLICABLE` (recurring, standalone side) — Shareholders-of-Company / NCI attribution rows are structurally blank on the Standalone columns (rows 27, 28, 30, 33, 34) since the standalone entity has no NCI; not a disclosure gap, a structural feature.
4. `OCR_MISALIGNMENT` (table-wide) — page-5 combined Standalone+Consolidated statement has visibly scrambled column-to-value mapping in the raw extract; row labels are reliable, attached values are not. A3/A4 must re-derive P&L values from source PDF, not this extract, for anything beyond the segment-table-corroborated figures (revenue, PBT, tax, PAT).
5. `EXTRACTION_GAP` — Consolidated LRR paragraph numerals 2, 4, 5 lost to OCR (paragraph 2 rendered "Ds,"); content intact; confirmed via the report's own internal cross-reference to "paragraph 6."
6. `DISCLOSURE_NOT_PROVIDED` — Segment Assets and Liabilities not disclosed (page 6, lines 386–389); management states not practicable to allocate.
7. New reportable segment — "Technology Workforce Augmentation Services" introduced this quarter per Note 5 (line 322–331); prior-period comparatives restated. Material structural change, flagged for forensic (A3) and analytical (A4) attention, not just a completeness item.
8. `PRIOR_LEDGER_UNAVAILABLE` — no prior-quarter ledger was supplied to this run; entity-list changes and note/line-item continuity vs Q4 FY26 could not be diffed. A3/A4 should source the Q4 FY26 filing independently if entity-continuity or note-continuity matters to the review.
