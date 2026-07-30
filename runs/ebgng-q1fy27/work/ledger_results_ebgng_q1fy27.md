# A2 ENUMERATION LEDGER — GNG Electronics Limited (EBGNG) — Q1 FY27 (results filing)
Source: /home/user/inflection-pipeline/runs/ebgng-q1fy27/work/extract_results_ebgng_q1fy27.txt
Units: Rs Million as filed (x0.1 = Rs Cr). Line numbers below are the extract file's own line numbers (cat -n), verified against pymupdf born-digital extraction.

```
=== A2 COUNT TEST ===
category: agenda_items       grep_count: 1    sweep_count: 1    match: yes
category: line_items         grep_count: 43   sweep_count: 43   match: yes
category: zero_standing      grep_count: 0    sweep_count: 0    match: yes
category: notes              grep_count: 10   sweep_count: 10   match: yes
category: auditor_paras      grep_count: 12   sweep_count: 12   match: yes
category: entities           grep_count: 6    sweep_count: 6    match: yes
category: signature_blocks   grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Methodology note on counts:
- `line_items`: grep -n -E over both P&L keyword labels (21 standalone + 22 consolidated = 43); manual sweep read every row label under I Income through IX EPS in both statements; identical count.
- `notes`: grep -n -E "^[0-9S]\.?$" scoped to each "Notes" block (lines 316-333 standalone, 683-711 consolidated) = 5+5=10, matching manual sweep; note the standalone Note 5 marker is OCR-garbled as the letter "S" rather than digit "5" (pymupdf artifact), confirmed by content match, not a missing note.
- `auditor_paras`: anchor-phrase grep against known paragraph-opening text (5 standalone incl. 3 unnumbered narrative paragraphs + numbered "4." + "Other Matters"; 7 consolidated incl. numbered 1-4, 6, 7 plus one unnumbered conclusion paragraph between 4 and 6 — an extraction numbering gap, not a missing paragraph) = 12, matching manual sweep.
- `entities`: grep -n -iE "subsidiary" filtered to the page-6 list only = 6, matching manual sweep of the named subsidiary/stepdown-subsidiary list.
- `signature_blocks`: grep on unique block-anchor phrases ("FOR GNG ELECTRONICS LIMITED"/"Company Secretary & Compliance Officer" merged as one block, "FOR SHANKARLAL JAIN..." x2, "r GNG"/"For GNG Electroni" x2) = 5, matching manual sweep of 5 distinct signature blocks.
- `zero_standing`: no line in either P&L carries a 0.00, dash, or "Nil" value in any of the four columns; no template row (e.g. exceptional items, non-controlling interest, share of associates) is present with a blank/zero value either — these rows are simply absent from the template altogether (see flags/observations below), which is a structural non-presence, not a ZERO_STANDING case.

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS (page 1)

| # | Line(s) | Item | Detail | Flags |
|---|---------|------|--------|-------|
| 1 | 42-50 | Standalone and Consolidated Unaudited Financial Results + Limited Review Reports, Q1 FY27 (qtr ended June 30 2026) | Approved by Board based on Audit Committee recommendation; attached as Annexure-1 | — |

Board meeting timing (line 57): commenced 03:15 P.M. IST, concluded 03:24 P.M. IST — 9 minutes total, single-item meeting.
Reference context (lines 35-36, not an agenda item): prior intimation letter dated July 27, 2026 announcing this meeting date.
No other agenda items present: no AR/AGM approval, no record date, no dividend, no director appointment/resignation, no auditor change, no scrutinizer, no ESOP grant, no capital-raising enabling resolution in this letter.

---

## 2. STANDALONE STATEMENT — P&L LINE ITEMS (page 4, Rs Million)

Columns: Q1FY27 (Jun-30-26) | Q4FY26 (Mar-31-26) | Q1FY26 (Jun-30-25) | FY26 (Audited, YE Mar-31-26)

| # | Label line | Value lines | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|---|
| 1 | 197 | 198-201 | Revenue from operations | 2,297.56 | 2,993.23 | 1,721.38 | 9,174.97 | — |
| 2 | 202 | 203-206 | Other income | 35.10 | 15.61 | 26.79 | 49.55 | — |
| 3 | 207 | 208-211 | Total income | 2,432.66 | 3,008.84 | 1,748.18 | 9,224.52 | — |
| 4 | 214 | 215-218 | Direct cost | 2,643.58 | 2,135.31 | 2,303.68 | 9,123.24 | — |
| 5 | 219 | 220-223 | Changes in inventory | (754.05) | 364.40 | (921.21) | (1,460.32) | — |
| 6 | 224 | 225-228 | Employee benefits expense | 146.37 | 149.96 | 107.33 | 477.74 | — |
| 7 | 229 | 230-233 | Finance costs | 85.16 | 89.38 | 70.44 | 263.96 | — |
| 8 | 234 | 235-238 | Depreciation and amortisation expense | 21.19 | 22.32 | 16.67 | 74.14 | — |
| 9 | 239 | 240-243 | Other expenses | 70.64 | 87.36 | 33.03 | 213.72 | — |
| 10 | 244 | 245-248 | Total expenses | 2,212.88 | 2,848.73 | 1,609.95 | 8,692.48 | — |
| 11 | 250-251 | 252-255 | Profit before tax (I-II) | 219.78 | 160.11 | 138.23 | 532.04 | — |
| 12 | 258 | 259-262 | Current tax | 56.00 | 41.00 | 36.00 | 136.00 | — |
| 13 | 263 | 264-267 | Deferred tax | 4.40 | (2.21) | 0.42 | (3.22) | — |
| 14 | 268 | 269-272 | Total tax expenses | 60.40 | 38.79 | 36.42 | 132.78 | — |
| 15 | 274 | 275-278 | Profit for the period/year (III-IV) | 159.38 | 121.31 | 101.81 | 399.26 | — |
| 16 | 281 | 282-285 | OCI: Re-measurement gains/(losses) on defined benefit plans | (0.66) | (2.23) | 0.08 | (1.99) | — |
| 17 | 286 | 287-290 | Total other comprehensive income (net of tax) | (0.66) | (2.23) | 0.08 | (1.99) | — |
| 18 | 292 | 293-296 | Total comprehensive income (V+VI) | 158.72 | 119.08 | 101.89 | 397.27 | — |
| 19 | 298-299 | 300-303 | Paid-up equity share capital (FV Rs 2/- each) | 228.02 | 228.02 | 194.27 | 228.02 | share count change Q1FY26->Q4FY26; not interpreted here |
| 20 | 306 | 307-310 | EPS Basic (Rs, not annualised except year-end) | 1.40 | 1.06 | 1.05 | 3.50 | — |
| 21 | 311 | 312-315 | EPS Diluted (Rs, not annualised except year-end) | 1.40 | 1.12 | 1.05 | 3.68 | — |

Structural observation: standalone statement has only ONE OCI sub-head ("Items that will not be reclassified to profit or loss"); there is no "Items that will be reclassified to profit or loss" sub-head at all (row absent, not zero-valued) — consistent with a standalone entity having no foreign-currency translation exposure. Not a ZERO_STANDING row since the row does not exist in this statement's template.

## 3. CONSOLIDATED STATEMENT — P&L LINE ITEMS (page 8, Rs Million)

Columns: Q1FY27 (Jun-30-26) | Q4FY26 (Mar-31-26) | Q1FY26 (Jun-30-25) | FY26 (Audited, YE Mar-31-26)

| # | Label line | Value lines | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|---|
| 1 | 559 | 560-563 | Revenue from operations | 4,124.61 | 6,516.55 | 3,122.79 | 18,910.75 | — |
| 2 | 564 | 565-568 | Other income | 35.12 | 6.26 | 28.54 | 43.32 | — |
| 3 | 569 | 570-573 | Total income | 4,159.73 | 6,522.81 | 3,151.33 | 18,954.07 | — |
| 4 | 576 | 577-580 | Direct cost | 2,726.46 | 5,500.69 | 3,100.02 | 17,306.00 | — |
| 5 | 581 | 582-585 | Changes in inventory | 381.61 | (236.76) | (644.27) | (2,204.72) | — |
| 6 | 586 | 587-590 | Employee benefits expense | 318.60 | 330.24 | 222.92 | 1,046.22 | — |
| 7 | 591 | 592-595 | Finance costs | 138.57 | 143.56 | 106.56 | 424.10 | — |
| 8 | 596 | 597-600 | Depreciation and amortisation expense | 32.80 | 32.45 | 20.40 | 103.52 | — |
| 9 | 601 | 602-605 | Other expenses | 204.26 | 288.84 | 121.00 | 801.52 | — |
| 10 | 606 | 607-610 | Total expenses | 3,802.32 | 6,059.02 | 2,926.63 | 17,476.65 | — |
| 11 | 612-613 | 614-617 | Profit before tax (I-II) | 357.41 | 463.78 | 224.70 | 1,477.42 | — |
| 12 | 620 | 621-624 | Current tax | 63.71 | 44.51 | 39.08 | 160.48 | — |
| 13 | 625 | 626-629 | Deferred tax | 4.40 | (2.21) | 0.42 | (3.22) | — |
| 14 | 630 | 631-634 | Total tax expenses | 68.11 | 42.31 | 39.50 | 157.26 | — |
| 15 | 636 | 637-640 | Profit for the period/year (III-IV) | 289.30 | 421.48 | 185.20 | 1,320.16 | — |
| 16 | 643 | 644-647 | OCI: Re-measurement gains/(losses) on defined benefit plans | (11.49) | (43.83) | 0.20 | (43.23) | — |
| 17 | 649 | 650-653 | OCI: Foreign Exchange Difference on Translation of Foreign operations | 6.02 | 299.06 | 11.96 | 295.33 | present only in consolidated (subsidiaries abroad) |
| 18 | 654 | 655-658 | Total other comprehensive income (net of tax) | (5.47) | 255.23 | 12.16 | 252.10 | — |
| 19 | 660 | 661-664 | Total comprehensive income (V+VI) | 283.83 | 676.71 | 197.36 | 1,572.26 | — |
| 20 | 665 | 666-669 | Paid-up equity share capital (FV Rs 2/- each) | 228.02 | 228.02 | 194.27 | 228.02 | — |
| 21 | 673 | 674-677 | EPS Basic (Rs, not annualised except year-end) | 2.54 | 3.70 | 1.91 | 11.58 | — |
| 22 | 678 | 679-682 | EPS Diluted (Rs, not annualised except year-end) | 2.54 | 3.89 | 1.91 | 12.17 | — |

Structural observation: no "Non-controlling interest" / "attributable to owners of the Parent" split line and no "Exceptional items" or "Share of profit of associates" line appear anywhere in the consolidated statement (checked via grep, zero hits) — implies all listed subsidiaries are treated as wholly owned with no minority interest and no associate/exceptional items in the period. Rows absent from template entirely, not ZERO_STANDING.

---

## 4. NOTES — STANDALONE STATEMENT (page 4, lines 316-333)

| Note # | Line(s) | First ~15 words | Flags |
|---|---|---|---|
| 1 | 317-320 | "The Statement...has been reviewed by the Audit Committee and recommended for approval to the Board..." | — |
| 2 | 321-324 | "The Statement...have been prepared in accordance with Indian Accounting Standards (Ind AS)...Regulation 33..." | — |
| 3 | 325-328 | "The Company operates in a single line of business...ICT Device...no reportable business segments..." | — |
| 4 | 329-331 | "The Figures for the quarter ended 31st March 2026 are the balancing figures between audited..." | — |
| 5 | 332-333 | "Figures pertaining to previous quarters/year have been reclassified wherever necessary to confirm to the classification..." | text truncated at line333 by extraction/signature-block overlap; note marker itself OCR-garbled as "S" not "5" |

## 5. NOTES — CONSOLIDATED STATEMENT (page 8, lines 683-711)

| Note # | Line(s) | First ~15 words | Flags |
|---|---|---|---|
| 1 | 684-687 | "The Statement of unaudited consolidated financial results...has been reviewed by the Audit Committee..." | — |
| 2 | 688-694 | "The Statement of unaudited consolidated financial results...prepared in accordance with Indian Accounting Standards (Ind AS)..." | — |
| 3 | 695-698 | "The Company operates in a single line of business...ICT Device...no reportable business segments..." | — |
| 4 | 699-701 | "The Figures for the quarter ended 31st March 2026 are the balancing figures between audited..." | — |
| 5 | 709-711 | "Figures pertaining to previous quarters/year have been reclassified wherever necessary to conform to the classification..." | text truncated at line711 by extraction/signature-block overlap |

Both notes blocks are textually parallel (Note 1-4 near-identical wording standalone vs consolidated, substituting "standalone"/"consolidated"); no additional/removed note between the two statements.

---

## 6. AUDITOR REPORT PARAGRAPHS — STANDALONE (Shankarlal Jain & Associates LLP, pages 2-3, lines 86-165)

| Para | Line(s) | Numbered in source? | Content (first ~15 words) | Flags |
|---|---|---|---|---|
| 1 | 86-109 | No (title + engagement description, fragmented one-word-per-line by extraction) | "Independent Auditors Limited Review Report...We have reviewed the accompanying statement of Unaudited Standalone Financial Results..." | — |
| 2 | 110-117 | No | "The preparation of the Statement in accordance with the recognition and measurement principles...is the responsibility of the Company..." | — |
| 3 | 118-124 | No | "We conducted our review of the Statement in accordance with the Standard on Review Engagement (SRE) 2410..." | — |
| 4 | 135-142 | Yes ("4.") | "Based on our review, conducted as above, nothing has come to our attention that causes us to believe..." — conclusion/opinion | — |
| 5 | 143-152 | No, headed "Other Matters" | "The Statement includes the results for the quarter ended March 31, 2026 being the balancing figure..." | Other Matters paragraph — Q4FY26 balancing-figure qualifier |

Opinion type: unmodified/clean review conclusion ("nothing has come to our attention..."). No Emphasis of Matter, no Going Concern language. Entity reviewed: GNG Electronics Limited (standalone only). UDIN (line165): 26...GGTV216} (partially garbled in extraction).

## 7. AUDITOR REPORT PARAGRAPHS — CONSOLIDATED (Shankarlal Jain & Associates LLP, pages 5-7, lines 370-498)

| Para | Line(s) | Numbered in source? | Content (first ~15 words) | Flags |
|---|---|---|---|---|
| 1 | 380-391 | Yes ("1.") | "We have reviewed the accompanying statement of unaudited consolidated financial results of GNG Electronics Limited...and its subsidiaries..." | — |
| 2 | 392-404 | Yes ("2.") | "This Statement...is the responsibility of the Parent's Management and approved by the Parent's Board...Our responsibility is to issue a report..." | — |
| 3 | 406-449 | Yes ("3."), spans page 5->6 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410...also performed procedures per SEBI circular 33(8)..." | — |
| 4 | 450-462 | Yes ("4.") | "The Statement includes the unaudited standalone financial results of the following Subsidiaries:" [entity list, see section 8] | — |
| 5 | 463-473 | No — numbering gap (should logically follow "4." but no marker present; extraction artifact, not a dropped paragraph) | "Based on our review conducted and procedures performed as stated in paragraph 3 above, nothing has come to our attention..." — conclusion/opinion | numbering gap noted; content is continuous and complete |
| 6 | 474-480 | Yes ("6.") | "The statement includes consolidated financial statement of subsidiary company Electronics Bazaar FZC incorporated in UAE which is limited reviewed by auditor NBN Auditing..." | names entities that are unaudited/management-furnished — see section 8 |
| 7 | 490-498 | Yes ("7."), headed "Other Matters" | "The Statement includes the results for the quarter ended March 31, 2026 being the balancing figure..." | Other Matters paragraph — identical Q4FY26 balancing-figure qualifier as standalone report |

Opinion type: unmodified/clean review conclusion. No Emphasis of Matter, no Going Concern language. Entity reviewed: GNG Electronics Limited + 6 subsidiaries listed (Group). UDIN (line516): 2.6 1G02Q INKLWWG1206 (partially garbled in extraction; differs from standalone-report UDIN as expected — two distinct engagements/reports).

Per para 6: Electronics Bazaar FZC (UAE) is limited-reviewed by NBN Auditing & Accounts (UAE), report dated July 29, 2026. The US-incorporated step-down subsidiaries (Bright World Technologies Inc., Kay Kay Overseas Corporation, Sun Electronics Corporation, Electronic Bazaar B.V. [sic, incorporated entity type per list], I-lectronic Bazar Inc.) have no statutory audit requirement in their jurisdiction; their figures are management-furnished and adopted by NBN Auditing & Accounts.

---

## 8. CONSOLIDATED SUBSIDIARIES LIST (page 6, lines 451-461)

| # | Line(s) | Entity | Relationship | Audit/review status | Flags |
|---|---|---|---|---|---|
| 1 | 452 | Electronics Bazaar FZC (UAE) | Subsidiary | Limited-reviewed by NBN Auditing & Accounts, UAE (report dated Jul 29, 2026) | — |
| 2 | 453-454 | Bright World Technologies Inc. | Stepdown subsidiary | Unaudited (no statutory audit requirement, USA); figures management-furnished, adopted by NBN | management-furnished/unaudited |
| 3 | 455 | Kay Kay Overseas Corporation | Stepdown subsidiary | Unaudited (no statutory audit requirement, USA); figures management-furnished, adopted by NBN | management-furnished/unaudited |
| 4 | 456-457 | Sun Electronics Corporation | Stepdown subsidiary | Unaudited (no statutory audit requirement, USA); figures management-furnished, adopted by NBN | management-furnished/unaudited |
| 5 | 458-459 | Electronic Bazaar B.V. | Stepdown subsidiary | Unaudited (no statutory audit requirement, USA per report text — note entity name suggests Dutch B.V. form, jurisdiction as stated in auditor para 6 text is USA); figures management-furnished, adopted by NBN | management-furnished/unaudited; jurisdiction/entity-name inconsistency (B.V. suffix typically Netherlands, auditor text says USA) not resolved by extraction — carry forward to A3/A4 |
| 6 | 460-461 | I-lectronic Bazar Inc. (name OCR-garbled, likely "Electronic Bazaar Inc.") | Stepdown subsidiary | Unaudited (no statutory audit requirement, USA); figures management-furnished, adopted by NBN | management-furnished/unaudited; entity name garbled in extraction, verify against source PDF |

Prior-quarter ledger not supplied in this task's injected inputs — ENTITY_CHANGE cross-check could not be performed. No flag raised for this reason (cross-check is conditional on prior ledger availability per instructions); note as an open item for A3.

---

## 9. DIGITAL SIGNATURE / SIGNATORY BLOCKS

| # | Line(s) | Signatory | Designation | Timestamp / Date | Context | Flags |
|---|---|---|---|---|---|---|
| 1 | 62-75 | Sarita Vishwakarma (digital cert name rendered "SARITA TUFANI VISHWAKARMA") | Company Secretary & Compliance Officer, Membership No. A59547 | Digitally signed 2026.07.30 15:37:48 +05'30 | Board Outcome letter to NSE/BSE | Signature is 13 minutes AFTER board meeting concluded (15:24 IST per line 57) — normal sequencing, no flag |
| 2 | 338-351 | Name illegible/garbled in extraction | Director (signing standalone financial results) | Place: Dubai; Date: 30th July 2026 (no time-stamp); "DIN: 03" (truncated, full DIN not legible) | Standalone statement of financial results, page 4 | name and DIN garbled in extraction — verify against source PDF |
| 3 | 153-165 | Kunal Padhya | Partner, Shankarlal Jain & Associates LLP, Firm Reg No. 109901W/W100082, Membership No. 160291 | Place: Mumbai; Date: July 30, 2026; UDIN: 26...GGTV216} (garbled) | Standalone Limited Review Report | — |
| 4 | 499-516 | Kunal Padhya | Partner, Shankarlal Jain & Associates LLP, Firm Reg No. 109901W/W100082, Membership No. 160291 | Place: Mumbai; Date: July 30, 2026; UDIN: 2.6 1G02Q INKLWWG1206 (garbled) | Consolidated Limited Review Report | UDIN differs from standalone report UDIN — expected (separate engagements), not a flag |
| 5 | 709-718 | Name illegible/garbled in extraction ("For GNG Electroni...") | Director (signing consolidated financial results) | Place: Dubai; Date: 30th July 2026 (no time-stamp) | Consolidated statement of financial results, page 8 | name garbled in extraction — verify against source PDF |

---

## SUMMARY COUNTS

| Category | Count |
|---|---|
| Agenda items | 1 |
| Line items (standalone) | 21 |
| Line items (consolidated) | 22 |
| Line items (total) | 43 |
| Zero-standing rows | 0 |
| Notes (standalone) | 5 |
| Notes (consolidated) | 5 |
| Notes (total) | 10 |
| Auditor paragraphs (standalone) | 5 |
| Auditor paragraphs (consolidated) | 7 |
| Auditor paragraphs (total) | 12 |
| Entities (consolidation list) | 6 |
| Signature blocks | 5 |

No ZERO_STANDING, ENTITY_CHANGE, MGMT_ABSENCE, REPEAT_QUESTION, or DROPPED_SLIDE conditions triggered on this filing (concall/presentation-specific flags not applicable to this doctype). Open items carried to A3/A4: (a) Electronic Bazaar B.V. jurisdiction/name inconsistency (line 458-459 vs auditor para 6 USA reference), (b) garbled director names/DIN/UDIN in three places requiring source-PDF verification, (c) auditor-paragraph numbering gap in the consolidated report (para 5 unnumbered, line 463-473) — content-complete but a source-fidelity item, (d) no prior-quarter ledger was supplied so subsidiary-list ENTITY_CHANGE comparison is outstanding.
