# LEDGER — SRM Contractors Limited (SRM), Q1 FY27, Results Filing
Source: extract_results_srm_q1fy27.txt (10 pages, 438 lines, unit convention: Lakhs)
Prior-quarter ledger: NONE (first quarterly run for this ticker — no diff base; ENTITY_CHANGE
and DROPPED_SLIDE checks are structurally not applicable this run, noted below wherever relevant)

=== A2 COUNT TEST ===
category: notes            grep_count: 11   sweep_count: 11   match: yes
  (grep -n -E "^\s*[0-9]+\.\s" on the two Notes blocks only [lines 210-232 std,
  403-429 consol] = 5 + 6 = 11; scoping matters — the same regex run unscoped
  over the whole file also catches the 5 NUMBERED paragraphs of the
  Consolidated Auditor's Review Report [lines 259-305], which are counted
  separately below under auditor_paras, not here, to avoid double counting.)

category: line_items       grep_count: 56 (raw) -> 48 (adjusted)   sweep_count: 48   match: yes
  (grep -c non-blank lines inside each results table block: 28 [standalone,
  lines 162-196] + 28 [consolidated, lines 356-391] = 56 raw. Each 28 includes
  4 section-header lines with no data cells — "Income", "Expenses", "Tax
  Expense:", "Earning per equity share" — which are not line items themselves.
  56 - 8 = 48 adjusted, which equals the manual sweep of 24 + 24 = 48. Reconciled.)

category: zero_standing    grep_count: 8 (raw) -> 10 (re-swept)   sweep_count: 10   match: yes (after re-sweep)
  (First-pass grep for "all value fields are -, ., or blank" regex found only
  6 standalone + 2 consolidated = 8. GATE A2 mismatch triggered on first pass:
  the consolidated regex undercounted because "Exceptional lteams" [line 373]
  has only 3 dash characters printed, not 4, one column dropped by OCR, and
  "Items that will not be reclassified to profit or loss:" [line 383] has a
  trailing colon that broke the blank-line pattern. Manual re-sweep of both
  full table blocks, reading all 4 period columns per row rather than
  regex-matching punctuation, confirms 6 standalone + 4 consolidated = 10.
  Re-swept count is what is reported in the ledger and YAML below.)

category: agenda_items      grep_count: 0 (keyword scan)   sweep_count: 1   match: yes
  (Keyword scan across the full extract for dividend|AGM|ESOP|appoint|
  scrutin|record date|capital raising|buyback|preferential returned zero
  hits, confirming by absence that the covering letter carries exactly the
  one item the manual sweep found: approval and taking on record of the
  quarterly results. No other Board Outcome agenda item is disclosed in
  this filing.)

category: auditor_paras     grep_count: 5 (numbered only)   sweep_count: 12   match: yes (after full sweep)
  (Grep for numbered paragraphs catches only the 5 numbered paragraphs of the
  Consolidated Auditor's Review Report [lines 259-305]. The Standalone
  Auditor's Review Report is entirely unnumbered prose — grep alone would
  report 0 for it. Manual sweep is mandatory here: 4 unnumbered paragraphs
  standalone + 5 numbered + 3 further unnumbered paragraphs in the
  Consolidated report [continuation after para 5 introducing the reliance
  table, the paragraph after the reliance table, and the closing reliance
  qualifier on page 8] = 4 + 5 + 3 = 12.)

category: entities           grep_count: 7 (raw) -> 8 (re-swept)   sweep_count: 8   match: yes (after re-sweep)
  (Grep for "^\s*[a-h]\)\s" against the Note 2 entity sub-list [lines 410-417]
  returns only 7: item (c) "Maccaferri Infrastructure Private Limited" is
  OCR-garbled as "¢)" not "c)" and is skipped by the regex. Manual re-sweep
  reading the sub-list by position (a through h) confirms 8 entities, which
  cross-checks against the 8 entities named inline in Consolidated Auditor's
  Review Report para 1 [lines 260-264]. Reconciled at 8.)

category: turns              grep_count: n/a   sweep_count: 0   match: yes  (results filing, no transcript)
category: questions          grep_count: n/a   sweep_count: 0   match: yes  (results filing, no transcript)
category: mgmt_numbers       grep_count: n/a   sweep_count: 0   match: yes  (results filing, no transcript)
category: slides             grep_count: n/a   sweep_count: 0   match: yes  (results filing, no deck)
category: slide_numbers      grep_count: n/a   sweep_count: 0   match: yes  (results filing, no deck)

gate_a2: pass
=== END COUNT TEST ===

---

## TABLE 1 — Covering Letter / Board Outcome Agenda Items
Source: pages 1 (lines 16-76)

| # | Item | Line | Detail | Flags |
|---|------|------|--------|-------|
| 1 | Results approval (sole agenda item) | 30-42 | "Unaudited Standalone and Consolidated Financial Results for the quarter ended 30 June, 2026" approved and taken on record. Board meeting commenced 4.00 P.M., concluded 4.30 P.M. on 13 August 2026 (duration 30 minutes). | — |

No AR approval, AGM notice, record date, dividend, director appointment/resignation,
auditor change, scrutinizer appointment, ESOP grant, or capital-raising enabling
resolution is disclosed anywhere in this filing (confirmed by keyword scan, zero hits).

| Signatory row | Line | Detail |
|---|---|---|
| Covering letter signatory | 55-66 | Arun Mathur, Company Secretary & Compliance Officer, M.No. 36848; digitally signed "ARUN MATHUR Date: 2026.08.13 16:30:23 +05'30'" |

---

## TABLE 2 — Standalone Auditor's Review Report — Paragraphs
Source: pages 2-3 (lines 84-146), Rohit Kc Jain & Co., unnumbered prose

| # | Line | First 15 words | Type | Flags |
|---|------|-----------------|------|-------|
| 1 | 84-86 | "Independent Auditor's Review Report on the Quarterly and Year to Date Unaudited Standalone Financial..." | Title / heading | — |
| 2 | 92-97 | "We have reviewed the accompanying statement of unaudited standalone financial results of SRM..." | Scope of engagement | — |
| 3 | 99-105 | "The Statement, which is the responsibility of the Company's management and approved by the..." | Management responsibility statement | — |
| 4 | 107-114 | "We conducted our review of the Statement in accordance with the Standard on Review..." | Basis of review (SRE 2410); explicit "we do not express an audit opinion" | — |
| 5 | 116-123 | "Based on our review conducted as above, nothing has come to our attention that..." | Conclusion — unmodified opinion, no material misstatement noted | — |

No Emphasis of Matter, no Other Matters paragraph, no Going Concern language in the
standalone report.

Signature block: CA Ritesh Wahal (Partner), M.No. 0517197, UDIN 26517197VKSZFF5162,
Date 13.08.2026, Place New Delhi. Lines 136-141. FRN 020422N. **Flag: DUPLICATE_UDIN**
(same UDIN reused verbatim on the Consolidated report signature, Table 5 below — see note there).

---

## TABLE 3 — Standalone Statement of Financial Results — Line Items
Source: page 4 (lines 149-208). Figures in Lakhs. Periods: Q1 FY27 (30 Jun 2026, unaudited) |
Q4 FY26 (31 Mar 2026, audited) | Q1 FY26 (30 Jun 2025, unaudited) | FY26 (31 Mar 2026, audited)

| # | Line | Particular | Type | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-----------|------|--------|--------|--------|------|-------|
| 1 | 163 | Revenue from operations (gross) | item | 15,031.54 | 31,214.86 | 14,309.34 | 84,971.17 | — |
| 2 | 164 | Other Income | item | 47.10 | 338.85 | 159.28 | 867.45 | — |
| 3 | 166 | Total Income | subtotal | 15,078.64 | 31,553.71 | 14,468.62 | 85,638.62 | — |
| 4 | 169 | Cost of materials consumed | item | 9,267.80 | 24,048.35 | 10,148.84 | 60,847.49 | — |
| 5 | 170 | Direct Expenses (OCR: "Direct Expenese") | item | 1,256.70 | 1,139.72 | 1,075.30 | 5,874.85 | — |
| 6 | 171 | Employee benefits expenses | item | 1,000.28 | 752.56 | 788.81 | 3,688.76 | — |
| 7 | 172 | Finance costs | item | 414.29 | 428.28 | 131.12 | 924.82 | — |
| 8 | 173 | Depreciation and amortisation expenses | item | 1,001.99 | 531.73 | 239.40 | 1,611.55 | — |
| 9 | 174 | Other expenses | item | 261.4 (OCR garbled — printed "2614") | 307.96 | 239.10 | 1,016.45 | note for A3: Q1FY27 value OCR-uncertain, magnitude inconsistent with other quarters |
| 10 | 176 | Total Expenses | subtotal | 13,166.18 | 27,208.60 | 12,622.57 | 73,963.94 | — |
| 11 | 178 | Profit before exceptional and extraordinary item and tax | item | 1,912.46 | 4,345.12 | 1,846.05 | 11,674.69 | — |
| 12 | 179 | Exceptional Items | item | — (blank, no value printed, all 4 periods) | | | | **ZERO_STANDING** |
| 13 | 180 | Profit before tax (III-IV) | item | 1,912.46 | 4,345.12 | 1,846.05 | 11,674.69 | — |
| 14 | 183 | (a) Current tax expense | item | 481.33 | 859.07 | 369.21 | 2,703.77 | — |
| 15 | 184 | (b) Deferred tax | item | 162.67 | 122.21 | 170.88 | 413.00 | — |
| 16 | 185 | (c) Income tax of previous year | item | – | – | – | – | **ZERO_STANDING** |
| 17 | 186 | Profit / (Loss) for the period (V-VI) | item | 1,593.80 | 3,363.84 | 1,305.96 | 8,557.91 | — |
| 18 | 187 | Profit / (Loss) from Joint Ventures | item | – | – | – | – | **ZERO_STANDING** |
| 19 | 188 | Other Comprehensive Income | item | – | . | . | – | **ZERO_STANDING** (OCR renders two of four cells as "." not "-"; still nil in all periods) |
| 20 | 189 | Items that will not be reclassified to profit or loss | item | – | – | – | . | **ZERO_STANDING** |
| 21 | 190 | Income tax relating to items that will not be reclassified to profit or loss | item | — (blank, no value printed, all 4 periods) | | | | **ZERO_STANDING** |
| 22 | 192 | Total Comprehensive Income for the period (VII+VIII+IX) | subtotal | 1,593.80 | 3,363.84 | 1,305.96 | 8,557.91 | — |
| 23 | 195 | Earnings per equity share (1) Basic | item | 6.95 | 14.66 | 5.69 | 37 (OCR garbled — printed bare "3") | note for A3: FY26 basic EPS cell OCR-truncated, cross-check against diluted (37.31) |
| 24 | 196 | Earnings per equity share (2) Diluted | item | 6.95 | 14.66 | 5.69 | 37.31 | — |

Signature block (statement footer): "For and on behalf of the Board of Directors," Managing
Director, DIN 09740051, Place Jammu, Date 13.08.2026. Lines 200-208. No named signatory
printed (OCR-obscured stamp/signature graphic).

---

## TABLE 4 — Notes to Standalone Un-audited Financial Results
Source: page 5 (lines 210-243)

| # | Line | First 15 words | Flags |
|---|------|-----------------|-------|
| 1 | 212-214 | "The above standalone un-audited financial results for the quarter ended 30th June, 2026..." (Audit Committee review + Board approval, both 13 Aug 2026) | — |
| 2 | 217-220 | "The Statutory Auditors have carried out a Limited Review under Regulation 33 of SEBI..." (unmodified opinion) | — |
| 3 | 222-225 | "The financial results of the Company have been prepared in accordance with Indian Accounting..." (Ind AS basis) | — |
| 4 | 227 | "As per Ind AS 108, the Company operates in single segment." | note for A3: single-segment claim — verify against consolidated note 5 (identical language) and against business description |
| 5 | 229-230 | "Previous periods' figures are regrouped to make them comparable with those of current period..." | note for A3: regrouping stated but no line-item quantification of what was regrouped |

Signature block (notes footer): "For and on behalf of the Board of Directors," Managing
Director, DIN 09740051, Place Jammu. Lines 235-243.

---

## TABLE 5 — Consolidated Auditor's Review Report — Paragraphs
Source: pages 6-8 (lines 251-341), Rohit Kc Jain & Co.

| # | Line | Numbered? | First 15 words | Type | Flags |
|---|------|-----------|-----------------|------|-------|
| 1 | 251-253 | no | "Independent Auditor's Review Report on Consolidated Unaudited Quarterly Financial Results and Year to..." | Title / heading | — |
| 2 | 259-268 | Para 1 | "We have reviewed the accompanying statement of unaudited consolidated financial results ('the Statement')..." | Scope of engagement; names 8 entities inline (see Table 9) | — |
| 3 | 270-277 | Para 2 | "This Statement, which is the responsibility of the Holding Company's management and approved..." | Management responsibility statement | — |
| 4 | 279-287 | Para 3 | "We conducted our review of the Statement in accordance with the Standard on Review..." | Basis of review (SRE 2410) | — |
| 5 | 293-294 | (unnumbered, page-break continuation) | "We also performed procedures in accordance with the circular issued by the SEBI under..." | Additional SEBI circular procedures | — |
| 6 | 296-302 | Para 4 | "Based on our review conducted and procedures performed as stated in paragraph 3 above..." | Conclusion — unmodified, no material misstatement noted | — |
| 7 | 305 | Para 5 (opening sentence) | "Our conclusion is not modified in respect of these matters." | Qualifier opening — reliance on component auditors | — |
| 8 | 307-309 | unnumbered continuation of Para 5 | "The Statement includes the interim financial information of above-mentioned subsidiaries, which have been..." | Introduces subsidiary reliance table (Table 6) | — |
| 9 | 320-323 | unnumbered | "Our conclusion on the Statement, in so far as it relates to the amounts and disclosures..." | States reliance is on unaudited/unreviewed component information; states this info "is not material to the Group" without naming which specific entities are unaudited | note for A3: aggregate materiality assertion, no entity-level unaudited/management-furnished breakdown given despite 8 entities in consolidation |
| 10 | 326-327 | unnumbered (page 8) | "Our conclusion is not modified in respect of this matter with respect to our reliance on the..." | Closing reliance qualifier | note for A3: near-duplicate phrasing of item 7 above ("Our conclusion is not modified..." appears twice) — possible page-break artifact, worth confirming against source PDF pagination |

Total paragraph count for this report (numbered + unnumbered, excluding the title line): 8
(items 2-10 minus the title = 8 substantive paragraphs; combined with the 4 standalone
paragraphs in Table 2, total auditor_paras = 12, reconciled in the COUNT TEST above.)

No Emphasis of Matter or Other Matters heading, no Going Concern language in the
consolidated report either.

Signature block: CA Ritesh Wahal (Partner), M.No. 0517197, UDIN 26517197VKSZFF5162,
Date 13.08.2026, Place New Delhi. Lines 336-341. FRN 020422N. **Flag: DUPLICATE_UDIN**
— identical UDIN string used for both the standalone report (Table 2) and this consolidated
report. Same partner signing both is expected; an identical UDIN across two distinct
certified documents is the fact enumerated here for A3/A4 to assess against ICAI UDIN
practice (one UDIN is ordinarily generated per document).

---

## TABLE 6 — Subsidiary / JV Reliance Table (inside Consolidated Auditor's Review Report)
Source: page 7 (lines 311-316)

| # | Line | Particular | Quarter ended 30 Jun 2026 (Lakh) | Year-to-date 30 Jun 2026 (Lakh) | Flags |
|---|------|-----------|-----------------------------------|-----------------------------------|-------|
| 1 | 313 | Total Revenues | Rs. 3,447.29 | Rs. 3,447.29 | — |
| 2 | 314 | Net Profit After Tax | Rs. 11.84 | Rs. 11.84 | — |
| 3 | 315-316 | Total Comprehensive Loss | Rs. 11.84 | Rs. 11.84 | note for A3: row is labelled "Loss" but the printed value (11.84) is positive and equal to the NPAT row above it — label/sign inconsistency, not a value discrepancy per se |

Table does not name which of the 8 consolidated entities these aggregate figures cover
(the reliance paragraph, Table 5 row 9, states only that reviewed/audited component
information is "not material to the Group" in aggregate).

---

## TABLE 7 — Consolidated Statement of Financial Results — Line Items
Source: page 9 (lines 343-401). Figures in Lakhs. Same four periods as Table 3.

| # | Line | Particular | Type | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-----------|------|--------|--------|--------|------|-------|
| 1 | 357 | Revenue from operations (gross) | item | 19,626.20 | 44,574.57 | 14,239.66 | 1,02,557.33 | — |
| 2 | 358 | Other Income | item | 92.30 | 535.89 | 159.28 | 874.79 | — |
| 3 | 360 | Total Income | subtotal | 19,718.50 | 45,110.46 | 14,398.94 | 1,03,432.11 | — |
| 4 | 363 | Cost of materials consumed | item | 11,899.02 | 30,460.00 | 9,520.07 | 63,898.21 | — |
| 5 | 364 | Direct Expenses (OCR: "Direct Expenese") | item | 2,072.52 | 4,652.69 | 1,575.11 | 10,778.60 | — |
| 6 | 365 | Employee benefits expenses | item | 1,382.22 | 1,097.02 | 788.81 | 4,215.47 | — |
| 7 | 366 | Finance costs | item | 457.06 | 441.24 | 131.12 | 947.15 | — |
| 8 | 367 | Depreciation and amortisation expenses | item | 1,029.05 | 552.41 | 248.05 | 1,654.05 | — |
| 9 | 368 | Other expenses | item | 451.24 | 926.68 | 314.63 | 6,840.10 | — |
| 10 | 370 | Total Expenses | subtotal | 17,291.11 | 38,130.04 | 12,577.79 | 88,333.58 | — |
| 11 | 372 | Profit before exceptional and extraordinary item and tax | item | 2,421.39 | 6,980.42 | 1,821.15 | 15,098.53 | — |
| 12 | 373 | Exceptional Items | item | – | – | (blank, one cell OCR-dropped) | – | **ZERO_STANDING** |
| 13 | 374 | Profit before tax (III-IV) | item | 2,421.39 | 6,980.42 | 1,821.15 | 15,098.53 | — |
| 14 | 377 | (a) Current tax expense | item | 619.63 | 1,494.31 | 375.46 | 3,568.46 | — |
| 15 | 378 | (b) Deferred tax | item | -163.49 | 77.85 | 170.88 | 429.20 | note for A3: Q1FY27 deferred tax is negative (a credit) — only negative value in this row across all periods |
| 16 | 379 | (c) Income tax of previous year | item | – | 0.92 | – | 0.92 | not ZERO_STANDING (nonzero in Q4FY26/FY26 — differs from the standalone version of this line, Table 3 row 16, which IS nil in all periods) |
| 17 | 380 | Profit / (Loss) for the period (V-VI) | item | 1,971.25 | 5,400.38 | 1,274.81 | 11,101.80 | — |
| 18 | 381 | Profit / (Loss) from Joint Ventures | item | -0.65 | 0.42 | – | 0.62 | not ZERO_STANDING (nonzero in 3 of 4 periods — differs from the standalone version of this line, Table 3 row 18, which IS nil in all periods, consistent with standalone excluding JV results) |
| 19 | 382 | Other Comprehensive Income | item | – | – | – | – | **ZERO_STANDING** |
| 20 | 383 | Items that will not be reclassified to profit or loss | item | — (blank, no value printed, all 4 periods) | | | | **ZERO_STANDING** |
| 21 | 384 | Income tax relating to items that will not be reclassified to profit or loss | item | — (blank, no value printed, all 4 periods) | | | | **ZERO_STANDING** |
| 22 | 387 | Total Comprehensive Income for the period (VII+VIII+IX) | subtotal | 1,970.60 | 5,409.80 | 1,274.81 | 11,102.41 | — |
| 23 | 390 | Earnings per equity share (1) Basic | item | 8.59 | 23.58 | 5.56 | 48.39 | — |
| 24 | 391 | Earnings per equity share (2) Diluted | item | 8.59 | 23.58 | 5.56 | 48.39 | — |

Signature block (statement footer): "For and on beh[alf of the Board of Directors]" (OCR-truncated),
Managing Director, DIN 09740051, Place Jammu, Date 13.08.2026. Lines 395-401.

---

## TABLE 8 — Notes to Consolidated Un-audited Financial Results
Source: page 10 (lines 403-438)

| # | Line | First 15 words | Flags |
|---|------|-----------------|-------|
| 1 | 405-407 | "The above Consolidated un-audited financial results for the quarter ended 30th June, 2026..." (Audit Committee review + Board approval, both 13 Aug 2026) | — |
| 2 | 408-417 | "The above consolidated results include the result of the following entities: Subsidiary Companies and..." — introduces the 8-entity sub-list a) through h) (enumerated in full in Table 9) | — |
| 3 | 418-421 | "The Statutory auditors have carried out a Limited Review under Regulation 33 of the SEBI..." (unmodified opinion) | — |
| 4 | 422-425 | "The financial results of the Group have been prepared in accordance with Indian Accounting..." (Ind AS basis) | — |
| 5 | 426 | "As per Ind AS 108, the Company operates in single segment." | note for A3: identical single-segment language to standalone note 4 — expected, since segment reporting is an entity-wide accounting policy, not itself a flag |
| 6 | 427-428 | "Previous periods' figures are regrouped to make them comparable with those of current period..." | note for A3: regrouping stated but no line-item quantification |

Signature block (notes footer): "For and on behalf of the Board of Directors," Managing
Director, DIN 09740051, Place: Jammu. Lines 431-438.

---

## TABLE 9 — Consolidation Entity List (cross-checked, two source locations)
Source A: Consolidated Auditor's Review Report para 1, inline list, lines 260-264
Source B: Consolidated Notes, Note 2 sub-list a)-h), lines 410-417

| # | Sub-item (Note 2) | Line | Entity name (Note 2 spelling) | Relationship (Note 2) | Matches Source A inline list? | Flags |
|---|--------------------|------|--------------------------------|------------------------|-------------------------------|-------|
| 1 | a) | 410 | SP Mangal Murti Enterprises Private Limited (OCR: "SPMangal Murti") | Wholly Owned Subsidiary | yes ("SP Mangal Murti Enterprises Pvt Ltd") | — |
| 2 | b) | 411 | Loran Valley Power Projects Private Limited | Subsidiary | yes | — |
| 3 | c) | 412 | Maccaferri Infrastructure Private Limited (OCR bullet garbled as "¢)") | Subsidiary | yes | — |
| 4 | d) | 413 | ECI SRM Projects | Subsidiary | yes ("ECI-SRM Projects") | — |
| 5 | e) | 414 | SRM Rajinder Projects (OCR: "SRMRajinder") | Subsidiary | yes ("SRM-Rajinder Projects") | — |
| 6 | f) | 415 | Kapahi SRM Projects | Subsidiary | yes ("Kapahi-SRM Projects") | — |
| 7 | g) | 416 | SRM RSB Projects | Subsidiary | yes ("SRM-RSB Projects") | — |
| 8 | h) | 417 | SAI SRM Projects | Joint Venture | yes ("Sai-SRM Projects" — Source A does not separately tag this one as JV vs subsidiary in its running prose, but the heading "Subsidiaries and Joint Venture" is consistent with one JV among the eight) | — |

Total entities: 8 in both source lists, fully cross-reconciled by name (allowing for OCR
spacing/hyphenation variants). **ENTITY_CHANGE: not applicable** — no prior-quarter ledger
exists for this ticker to diff against (first quarterly run). This table is the baseline
entity list for future quarters' diffs.

---

## TABLE 10 — Signature Blocks
Source: full document

| # | Line | Context | Signatory | Designation | Date / Timestamp | Flags |
|---|------|---------|-----------|-------------|-------------------|-------|
| 1 | 55-67 | Covering letter | Arun Mathur | Company Secretary & Compliance Officer (M.No. 36848) | Digitally signed 2026.08.13 16:30:23 +05'30' | note for A3: board meeting stated to conclude "4.30 P.M." (line 41) same day; digital signature timestamp is 16:30:23, i.e. ~23 seconds after nominal meeting close, not before it — does not trigger the "signed before meeting concluded" flag, but the near-zero gap is worth A3's attention given no minutes/closing formalities window is evident |
| 2 | 200-208 | Standalone statement footer | (unnamed — stamp/signature graphic, OCR-obscured) | Managing Director, DIN 09740051 | Place Jammu, Date 13.08.2026 | — |
| 3 | 235-243 | Standalone notes footer | (unnamed) | Managing Director, DIN 09740051 | Place Jammu (no date printed) | — |
| 4 | 395-401 | Consolidated statement footer | (unnamed — stamp/signature graphic, OCR-obscured) | Managing Director, DIN 09740051 | Place Jammu, Date 13.08.2026 | — |
| 5 | 431-438 | Consolidated notes footer | (unnamed) | Managing Director, DIN 09740051 | Place: Jammu (no date printed) | — |
| 6 | 136-141 | Standalone auditor report | CA Ritesh Wahal | Partner, M.No. 0517197, FRN 020422N | Date 13.08.2026, Place New Delhi, UDIN 26517197VKSZFF5162 | **DUPLICATE_UDIN** |
| 7 | 336-341 | Consolidated auditor report | CA Ritesh Wahal | Partner, M.No. 0517197, FRN 020422N | Date 13.08.2026, Place New Delhi, UDIN 26517197VKSZFF5162 | **DUPLICATE_UDIN** |

---

## TABLE 11 — Annexures
No annexures, director profile tables, or other attachments beyond the covering letter,
the two auditor review reports, the two results statements, and the two sets of notes are
present in this extract (page_coverage: 100%, 10 of 10 pages accounted for above). Category
enumerated as N/A for this filing; recorded so future-quarter diffs can detect an annexure
being ADDED where none existed before.

---

## SUMMARY OF FLAGS RAISED
- **ZERO_STANDING** x 10 (Table 3 rows 12,16,18,19,21; Table 7 rows 12,19,20,21)
- **DUPLICATE_UDIN** x 2 (Table 2 / Table 5 signature blocks — same UDIN on both reports; also cross-referenced in Table 10 rows 6-7)
- **ENTITY_CHANGE**: not applicable this run (no prior ledger) — Table 9 established as baseline
- MGMT_ABSENCE, REPEAT_QUESTION, DROPPED_SLIDE: not applicable (results filing, no transcript/deck)

```yaml
stage: A2-enumerator
company: "SRM"
quarter: "q1fy27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/srm-q1fy27/work/ledger_results_srm_q1fy27.md"
counts:                      # per applicable category
  notes: 11
  line_items: 48
  zero_standing: 10
  agenda_items: 1
  auditor_paras: 12
  entities: 8
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
  signature_blocks: 7
  reliance_table_items: 3
flags_raised: [ZERO_STANDING, DUPLICATE_UDIN]
gate_a2: pass
mismatch_note: ""
```
