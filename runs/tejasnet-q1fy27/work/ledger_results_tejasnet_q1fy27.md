# A2 ENUMERATION LEDGER — Tejas Networks (TEJASNET), Q1 FY27, Results filing
Source: extract_results_tejasnet_q1fy27.txt (486 lines, 8 pages, pages 2-8 OCR'd)
Prior-quarter ledger: none available (first pipeline run for this ticker) — no ENTITY_CHANGE / DROPPED_SLIDE diff possible this run.

```
=== A2 COUNT TEST ===
category: notes             grep_count: 14   sweep_count: 14   match: yes
category: line_items        grep_count: 76   sweep_count: 76   match: yes
category: zero_standing     grep_count: 5    sweep_count: 5    match: yes
category: agenda_items      grep_count: 1    sweep_count: 1    match: yes
category: auditor_paras     grep_count: 11   sweep_count: 11   match: yes
category: entities          grep_count: 4    sweep_count: 4    match: yes
category: signature_blocks  grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

## Reconciliation notes (how each count was built and reconciled)
- **notes**: initial blind grep `^\s*[0-9]+[\. ]` over the whole file returned 26 raw hits, polluted by false positives inside signature-block OCR noise (lines 112, 322, 481 — e.g. "6 ot (A vl /) C", "2015 including...", "2 r % wa m") and it MISSED standalone note 5 because OCR rendered its leading digit as "5S" (line 223: "5S The figures..."), not "5 ". Re-scoped the grep to the two Notes-section line ranges (211-240 standalone, 418-473 consolidated) and loosened the digit-trailer class to `[0-9]+[\.S ]`: this recovered exactly 6 standalone + 8 consolidated = 14, matching the manual line-by-line sweep. Gate re-swept and passes.
- **line_items**: raw non-blank line count in the three table bodies is 39 (standalone P&L, lines 153-191) + 40 (consolidated P&L, lines 359-398) + 13 (consolidated Note 4 summary block, lines 441-453, of which only 3 are data rows, the rest are caption/blank wrap lines). Manual sweep merges wrapped continuation lines that OCR split across raw lines but that belong to one logical row: standalone row "Remeasurements...(expense)/benefit" (177+178) and row "XI Reserves...Balance Sheet" (185+186+187) collapse 39 raw lines to 36 rows; consolidated collapses 40 raw lines to 37 rows (identical two collapses, plus one extra genuine row — "Exchange differences on translation of foreign operations" — that exists only in the consolidated table, not standalone). Summary block sweep = 3 confirmed by targeted grep `^(Revenue from operations|Profit/\(Loss\))`. Total: 36 + 37 + 3 = 76, reconciled both ways.
- **zero_standing**: subset of line_items where a line item reads "-" (dash/nil) in ALL FOUR reporting periods. Standalone: 3 (Current tax expense/benefit; Income tax relating to remeasurement item; Income tax relating to cash-flow-hedge item). Consolidated: 2 (Income tax relating to remeasurement item; Income tax relating to cash-flow-hedge item) — consolidated Current tax expense/(benefit) is NOT all-zero (shows (0.01) in Q1 FY26 and (0.02) in FY26-audited), so it does not qualify and is intentionally excluded, a genuine standalone-vs-consolidated divergence worth carrying to A3/A4. "XI Reserves" is dash in three periods but carries a real audited year-end value, so it is excluded (dash is a structural Ind AS 34 interim-disclosure convention, not zero in ALL periods).
- **agenda_items**: grepped the Board Outcome letter (page 1) for AGM / record date / dividend / scrutinizer / ESOP / director appointment / auditor appointment / capital-raising keywords — zero hits. Manual sweep confirms the letter carries exactly one agenda action: approval of the Unaudited Financial Results (Standalone and Consolidated) for the quarter. Both methods agree at 1.
- **auditor_paras**: grep `^[0-9]\.` inside each review-report region found 4 (standalone, paras 1-4) + 6 (consolidated, paras 1-6) = 10. Manual sweep found an 11th paragraph in the consolidated report with no leading numeral at all in the source (lines 290-292, the SEBI Regulation 33(8) circular-procedures sentence, sitting between numbered para 3 and numbered para 4/entity-list) — not an OCR artifact, the source paragraph itself is unnumbered. Re-swept and the ledger below carries it as its own row; reconciled total both ways = 11.
- **entities**: grep on Holding Company / Subsidiar / Tejas Communications / Saankhya returned hits in two separate places (auditor-report para 4, lines 309-314; consolidated Note 1, lines 420-429) = 8 raw mentions. Manual sweep collapses this to 4 distinct entities (1 holding company + 3 subsidiaries), each named twice (once per list). Reconciled at 4 distinct entities / 8 total list-appearances (both recorded below).
- **signature_blocks**: grep `-i "digitally signed"` returns only 1 hit (page 1, Company Secretary). Manual sweep for signature anchors (Partner / Membership Number / UDIN / Managing Director and CEO / Company Secretary) finds 5 distinct signature blocks total across the filing (2 auditor sign-offs, 2 CEO sign-offs, 1 Company Secretary digital signature). Reconciled at 5; only 1 of the 5 carries an explicit digital timestamp in the OCR text.

---

## 1. Numbered notes — Standalone (page 4, lines 211-240)

| # | Line | First ~15 words | Flags |
|---|------|------------------|-------|
| 1 | 212 | "This Statement of Unaudited Standalone Financial Results for the quarter ended June 30, 2026 has been prepared..." | |
| 2 | 216 | "The Company has identified 'telecom and data networking related products and services' as its only reportable segment..." | |
| 3 | 218 | "Cost of materials consumed include reversal of provision for inventory obsolescence/write down amounting to Rs. 3.10 crore..." | |
| 4 | 221 | "Other expenses for the quarter ended June 30, 2026 include provision for warranty expenses amounting to Rs. 35.11 crore..." | |
| 5 | 223 | "The figures for the quarter ended March 31, 2026 are the balancing figures between the audited figures..." | OCR: leading digit rendered "5S" not "5 " |
| 6 | 225 | "The above Statement of Unaudited Standalone Financial Results was reviewed and recommended by the Audit Committee..." | |

## 2. Numbered notes — Consolidated (page 8, lines 418-472)

| # | Line | First ~15 words | Flags |
|---|------|------------------|-------|
| 1 | 420 | "The Statement of Unaudited Consolidated Financial Results for the quarter ended June 30, 2026 includes the results of Tejas Networks Limited..." | |
| 2 | 431 | "This Statement of Unaudited Consolidated Financial Results for the quarter ended June 30, 2026 has been prepared..." | |
| 3 | 436 | "The Group has identified 'telecom and data networking related products and services' as its only reportable segment..." | |
| 4 | 439 | "Summary of key Unaudited Standalone Financial Results of the Company is as follows:" (embeds its own 3-row table, see Section 5) | |
| 5 | 460 | "Cost of materials consumed include reversal of provision for inventory obsolescence/write down amounting to Rs. 3.10 crore..." | |
| 6 | 464 | "Other expenses for the quarter ended June 30, 2026 include provision for warranty expenses amounting to Rs. 35.11 crore..." | |
| 7 | 467 | "The figures for the quarter ended March 31, 2026 are the balancing figures between the audited figures..." | |
| 8 | 471 | "The above Statement of Unaudited Consolidated Financial Results was reviewed and recommended by the Audit Committee..." | |

Note numbering is NOT parallel between statements: standalone note 3 (segment) = consolidated note 3 (segment) but standalone note 3 ("cost of materials", refer note-3) maps to consolidated note 5 (refer note-5), and standalone note 4 ("other expenses", refer note-4) maps to consolidated note 6 (refer note-6), because consolidated Note 4 is the extra "Summary of key Standalone Results" block that standalone doesn't carry. Numbering divergence is mechanical (extra note), not a content flag.

## 3. Line items — Standalone Statement of Unaudited Financial Results (page 3, lines 153-191)
All four periods per row: Q1 FY27 (Jun-30-2026, Unaudited) | Q4 FY26 (Mar-31-2026, Unaudited, refer note-5) | Q1 FY26 (Jun-30-2025, Unaudited) | FY26 (Mar-31-2026, Audited).

| Row | Line(s) | Label | Q1 FY27 | Q4 FY26 | Q1 FY26 | FY26-audited | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 153 | I Revenue from operations [section header] | — | — | — | — | |
| 2 | 154 | (a) Revenue from sale of goods and rendering of services | 401.61 | 331.46 | 201.93 | 1,094.97 | |
| 3 | 155 | (b) Other operating revenue | 0.34 | 0.30 | - | 5.81 | |
| 4 | 156 | Total Revenue from operations | 401.95 | 331.76 | 201.93 | 1,100.78 | |
| 5 | 157 | II Other income | 8.97 | 10.32 | 9.55 | 33.46 | OCR: "II" rendered "(|" |
| 6 | 158 | III Total income (I + II) | 410.92 | 342.08 | 211.48 | 1,134.24 | OCR: "III" rendered "I", "(1+II)" rendered "(1 + Il)" |
| 7 | 159 | IV EXPENSES [section header] | — | — | — | — | |
| 8 | 160 | (a) Cost of materials consumed (Refer note-3) | 132.08 | 297.07 | 123.10 | 820.23 | |
| 9 | 161 | (b) Purchases of stock-in-trade | 16.04 | 51.53 | 20.02 | 78.06 | |
| 10 | 162 | (c) Changes in inventories of stock-in-trade and finished goods | 109.05 | (139.56) | (26.84) | (131.59) | |
| 11 | 163 | (d) Employee benefit expense | 101.06 | 95.62 | 92.75 | 390.60 | |
| 12 | 164 | (e) Finance costs | 85.04 | 72.01 | 74.69 | 302.61 | |
| 13 | 165 | (f) Depreciation and amortization expense | 94.35 | 100.84 | 96.46 | 402.73 | |
| 14 | 166 | (g) Allowance for expected credit loss | 8.08 | 21.79 | 18.18 | 61.06 | |
| 15 | 167 | (h) Other expenses (Refer note-4) | 136.03 | 130.70 | 110.50 | 572.07 | |
| 16 | 168 | Total expenses (IV) | 681.73 | 630.00 | 508.86 | 2,495.77 | |
| 17 | 169 | V Profit/(Loss) before tax (III - IV) | (270.81) | (287.92) | (297.38) | (1,361.53) | |
| 18 | 170 | VI Income tax expense/(benefit) [section header] | — | — | — | — | |
| 19 | 171 | (1) Current tax expense/(benefit) | - | - | - | - | ZERO_STANDING |
| 20 | 172 | (2) Deferred tax expense/(benefit) | (68.57) | (69.46) | (103.47) | (445.10) | |
| 21 | 173 | Total tax expense/(benefit) | (68.57) | (69.46) | (103.47) | (445.10) | |
| 22 | 174 | VII Profit/(Loss) after tax (V - VI) | (202.24) | (218.46) | (193.91) | (916.43) | |
| 23 | 175 | VIII Other comprehensive income [section header] | — | — | — | — | |
| 24 | 176 | Items that will not be reclassified to profit or loss [sub-header] | — | — | — | — | |
| 25 | 177-178 | Remeasurements of the post-employment benefit obligation (expense)/benefit | 1.08 | (2.38) | 0.56 | 1.59 | OCR: label garbled "RERmeeSUreisiehitx...", value "1.08" rendered "+08" |
| 26 | 179 | Income tax relating to above | - | - | - | - | ZERO_STANDING |
| 27 | 180 | Items that may be reclassified to profit or loss [sub-header] | — | — | — | — | |
| 28 | 181 | Gains/(losses) in cash flow hedges | (7.72) | 6.78 | 4.39 | 11.81 | |
| 29 | 182 | Income tax relating to above | - | - | - | - | ZERO_STANDING |
| 30 | 183 | IX Total comprehensive income for the period (VII + VIII) | (208.91) | (214.06) | (188.96) | (903.03) | |
| 31 | 184 | X Equity share capital (Face value of Rs. 10/- each) | 181.25 | 181.01 | 179.89 | 181.01 | |
| 32 | 185-187 | XI Reserves (excluding Revaluation reserve) as shown in the Audited Balance Sheet | - | - | - | 2,750.70 | dash 3 periods, structural (interim disclosure convention) — not ZERO_STANDING, has a real value in FY26-audited |
| 33 | 188 | XII Earnings/(Loss) per equity share [section header] | — | — | — | — | |
| 34 | 189 | Equity shares of par value Rs. 10 each [sub-header] | — | — | — | — | |
| 35 | 190 | (1) Basic | (11.37) | (12.30) | (10.99) | (51.78) | |
| 36 | 191 | (2) Diluted | (11.37) | (12.30) | (10.99) | (51.78) | |

## 4. Line items — Consolidated Statement of Unaudited Financial Results (page 7, lines 359-398)

| Row | Line(s) | Label | Q1 FY27 | Q4 FY26 | Q1 FY26 | FY26-audited | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 359 | I Revenue from operations [section header] | — | — | — | — | |
| 2 | 360 | (a) Revenue from sale of goods and rendering of services | 401.82 | 332.39 | 201.98 | 1,097.47 | |
| 3 | 361 | (b) Other operating revenue | 0.34 | 0.30 | - | 5.81 | |
| 4 | 362 | Total Revenue from operations | 402.16 | 332.69 | 201.98 | 1,103.28 | |
| 5 | 363 | II Other income | 8.97 | 10.28 | 9.55 | 33.38 | OCR: "II" rendered "ll" |
| 6 | 364 | III Total income (I + II) | 411.13 | 342.97 | 211.53 | 1,136.66 | OCR: "III" rendered "II", "(I+II)" rendered "(1 +1!)" |
| 7 | 365 | IV EXPENSES [section header] | — | — | — | — | |
| 8 | 366 | (a) Cost of materials consumed (Refer note-5) | 132.09 | 297.07 | 123.13 | 820.51 | |
| 9 | 367 | (b) Purchases of stock-in-trade | 16.04 | 51.53 | 20.02 | 78.06 | |
| 10 | 368 | (c) Changes in inventories of stock-in-trade and finished goods | 109.05 | (139.56) | (26.84) | (131.59) | |
| 11 | 369 | (d) Employee benefit expense | 105.24 | 99.78 | 95.82 | 404.60 | |
| 12 | 370 | (e) Finance costs | 85.07 | 72.04 | 74.77 | 302.83 | |
| 13 | 371 | (f) Depreciation and amortization expense | 94.35 | 100.84 | 96.46 | 402.73 | |
| 14 | 372 | (g) Allowance for expected credit loss | 8.08 | 21.79 | 18.18 | 61.06 | |
| 15 | 373 | (h) Other expenses (Refer note-6) | 132.02 | 120.28 | 107.34 | 552.47 | |
| 16 | 374 | Total expenses (IV) | 681.94 | 623.77 | 508.88 | 2,490.67 | |
| 17 | 375 | V Profit/(Loss) before tax (III - IV) | (270.81) | (280.80) | (297.35) | (1,354.01) | |
| 18 | 376 | VI Income tax expense/(benefit) [section header] | — | — | — | — | |
| 19 | 377 | (1) Current tax expense/(benefit) | - | - | (0.01) | (0.02) | NOT ZERO_STANDING — diverges from standalone (standalone row 19 is all-dash; consolidated carries small subsidiary-level current tax in Q1 FY26 / FY26-audited) |
| 20 | 378 | (2) Deferred tax expense/(benefit) | (68.57) | (69.46) | (103.47) | (445.10) | |
| 21 | 379 | Total tax expense/(benefit) | (68.57) | (69.46) | (103.48) | (445.12) | |
| 22 | 380 | VII Profit/(Loss) after tax (V - VI) | (202.24) | (211.34) | (193.87) | (908.89) | OCR: "VII" rendered "Vit" |
| 23 | 381 | VIII Other comprehensive income [section header] | — | — | — | — | OCR: "VIII" rendered "Vill" |
| 24 | 382 | Items that will not be reclassified to profit or loss [sub-header] | — | — | — | — | |
| 25 | 383-384 | Remeasurements of the post-employment benefit obligation (expense)/benefit | 1.68 | (2.38) | 0.56 | 1.59 | OCR: value "1.68" rendered "168" |
| 26 | 385 | Income tax relating to above | - | - | - | - | ZERO_STANDING |
| 27 | 386 | Items that may be reclassified to profit or loss [sub-header] | — | — | — | — | |
| 28 | 387 | Gains/(losses) in cash flow hedges | (7.72) | 6.78 | 4.39 | 11.81 | |
| 29 | 388 | Exchange differences on translation of foreign operations | (0.03) | 0.25 | 0.03 | 0.64 | present only in Consolidated — no standalone counterpart (expected: FX translation only arises on foreign subsidiaries) |
| 30 | 389 | Income tax relating to gains/(losses) in cash flow hedges | - | - | - | - | ZERO_STANDING |
| 31 | 390 | IX Total comprehensive income for the period (VII + VIII) | (208.94) | (206.69) | (188.89) | (894.85) | OCR: "IX" rendered "1X" |
| 32 | 391 | X Equity share capital (Face value of Rs. 10/- each) | 181.25 | 181.01 | 179.89 | 181.01 | |
| 33 | 392-394 | XI Reserves (excluding Revaluation reserve) as shown in the Audited Balance Sheet | - | - | - | 2,749.86 | dash 3 periods, structural — not ZERO_STANDING; note value differs from standalone's 2,750.70 (consolidation adjustment) |
| 34 | 395 | XII Earnings/(Loss) per equity share [section header] | — | — | — | — | |
| 35 | 396 | Equity shares of par value Rs. 10 each [sub-header] | — | — | — | — | |
| 36 | 397 | (1) Basic | (11.37) | (11.90) | (10.99) | (51.35) | |
| 37 | 398 | (2) Diluted | (11.37) | (11.90) | (10.99) | (51.35) | |

## 5. Line items — Consolidated Note 4: "Summary of key Unaudited Standalone Financial Results" (page 8, lines 439-459)
Embedded 3-row extract of the standalone P&L, reproduced inside the consolidated notes for reader convenience; values match Section 3 exactly (cross-checked).

| Row | Line | Label | Q1 FY27 | Q4 FY26 | Q1 FY26 | FY26-audited | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 449 | Revenue from operations | 401.95 | 331.76 | 201.93 | 1,100.78 | matches Section 3 row 4 |
| 2 | 451 | Profit/(Loss) before tax | (270.81) | (287.92) | (297.38) | (1,361.53) | matches Section 3 row 17 |
| 3 | 453 | Profit/(Loss) after tax | (202.24) | (218.46) | (193.91) | (916.43) | matches Section 3 row 22 |

## 6. Board Outcome letter — agenda items and meeting timing (page 1, lines 16-52)

| # | Line | Item | Detail | Flags |
|---|------|------|--------|-------|
| 1 | 29-33 | Agenda item 1 (sole item disclosed) | Board considered and approved the Unaudited Financial Results (Standalone and Consolidated) for the quarter ended June 30, 2026, together with the Limited Review Report | This is the ONLY agenda item in the letter. No AR approval, AGM notice, record date, dividend, director appointment/resignation, auditor change, scrutinizer appointment, ESOP grant, or capital-raising resolution is disclosed anywhere in this filing. |
| 2 | 35 | Board meeting timing | Started 1:30 P.M. (IST), ended 4:40 P.M. (IST) — duration 3h10m | Single-topic (results-only) meeting; 3h10m is a long duration for one agenda item, informational only |

## 7. Auditor report paragraphs — Standalone Limited Review Report (page 2, lines 55-134)
Auditor: Price Waterhouse Chartered Accountants LLP (Firm Reg. No. 012754N/N500016). Partner: Prasanna Padar Mahabala, Membership No. 206477. Entity reviewed: Tejas Networks Limited (standalone only, no subsidiaries in scope).

| Para | Line(s) | Content | Flags |
|---|---|---|---|
| 1 | 73-79 | Scope: reviewed the Standalone Statement for quarter ended June 30, 2026, prepared under Regulation 33; initialled by auditor for identification | |
| 2 | 81-86 | Responsibility: Statement is Management's responsibility, approved by Board; prepared per Ind AS 34; auditor's responsibility is to express a review conclusion | |
| 3 | 88-99 | Review conducted per SRE 2410; moderate assurance, not an audit; auditor does not express an audit opinion | scope-limitation language (standard for a review, not a flag on its own) |
| 4 | 101-107 | Conclusion/opinion: unmodified — nothing came to auditor's attention indicating the Statement was not prepared in accordance with Ind AS 34 / Regulation 33, or contains material misstatement | Opinion type: UNMODIFIED. No Emphasis of Matter paragraph. No Other Matters paragraph. No Going Concern paragraph/language anywhere in this report. |
| — | 109-120 | Signature block: For Price Waterhouse Chartered Accountants LLP; Prasanna Padar Mahabala, Partner; Place: Bengaluru; Date: July 27, 2026; UDIN: 26206477VOPILA4407 | see Section 10 |

## 8. Auditor report paragraphs — Consolidated Limited Review Report (page 5-6, lines 242-341)
Same auditor and partner as standalone. Entities reviewed: Holding Company (Tejas Networks Limited) plus 3 subsidiaries per para 4 (see Section 9).

| Para | Line(s) | Content | Flags |
|---|---|---|---|
| 1 | 260-269 | Scope: reviewed the Consolidated Statement (Group = Holding Company + subsidiaries, refer Note 1) for quarter ended June 30, 2026; initialled for identification | |
| 2 | 271-276 | Responsibility: Holding Company Management's responsibility, approved by Holding Company Board; prepared per Ind AS 34 | |
| 3 | 278-288 | Review conducted per SRE 2410; moderate assurance, not an audit; no audit opinion expressed | |
| (unnumbered) | 290-292 | "We also performed procedures in accordance with the circular issued by the SEBI under Regulation 33(8)..., to the extent applicable" | Paragraph carries no numeral in the source itself (not an OCR artifact — genuinely unnumbered, sits between numbered paras 3 and 4) |
| 4 | 308-315 | Entity list: Holding Company (Tejas Networks Limited, India) + 3 named subsidiaries — see Section 9 | |
| 5 | 316-323 | Conclusion/opinion: unmodified — nothing came to attention indicating Consolidated Statement not prepared per Ind AS 34 / Regulation 33, or contains material misstatement | Opinion type: UNMODIFIED |
| 6 | 325-333 | Other Matters: unaudited consolidated results include 3 subsidiaries NOT reviewed by their own auditors; those subsidiaries' figures (total revenue Rs. 0.86 cr, total net loss after tax Rs. 0.00 cr, total comprehensive income Rs. 0.03 cr for the quarter) are immaterial to the Group per Management representation; conclusion NOT modified in respect of this matter | OTHER MATTERS paragraph. All 3 subsidiaries flagged as unreviewed/management-furnished. No Going Concern paragraph/language anywhere in this report. |
| — | 334-340 | Signature block: For Price Waterhouse Chartered Accountants LLP; Prasanna Padar Mahabala, Partner; Place: Bengaluru; Date: July 27, 2026; UDIN: 26206477ULOFUU1403 | see Section 10 |

Auditor paragraph total: 4 (standalone) + 6 numbered + 1 unnumbered (consolidated) = 11.

## 9. Consolidation entity list — 3 subsidiaries per note (cross-referenced twice in the filing)

| # | Entity | Relationship | Listed at (line) | Flags |
|---|--------|--------------|-------------------|-------|
| 1 | Tejas Networks Limited, India | Holding Company / Parent | auditor report para 4, line 309-310; consolidated Note 1, line 420-423 (referred to as "the Company"/"the Holding Company"/"the Parent") | |
| 2 | Tejas Communications Pte. Limited, Singapore | Subsidiary | auditor report para 4, line 312 ("a) Tejas Communications Pte. Limited, Singapore"); consolidated Note 1, line 426 ("Tejas Communication Pte. Limited, Singapore") | Naming inconsistency between the two lists within THIS SAME filing: "Communications" (auditor report) vs "Communication" (Note 1, singular, missing "s") — same entity, textual discrepancy for A3/A4 to weigh, not flagged as ENTITY_CHANGE (no prior-quarter list exists to diff against this run) |
| 3 | Tejas Communications (Nigeria) Limited, Nigeria | Subsidiary | auditor report para 4, line 313 ("b)..."); consolidated Note 1, line 428 ("-...") | |
| 4 | Saankhya Labs Inc, USA | Subsidiary | auditor report para 4, line 314 ("c)..., USA" no period after "Inc"); consolidated Note 1, line 429 ("Saankhya Labs Inc., USA" with period after "Inc") | minor punctuation variant between the two lists ("Inc" vs "Inc.") |

Auditor report para 6 (Section 8) states all 3 subsidiaries' results are unreviewed by their own auditors and management-furnished (revenue Rs. 0.86 cr, net loss after tax Rs. 0.00 cr [ZERO_STANDING for that subsidiary-level metric this quarter], total comprehensive income Rs. 0.03 cr, aggregate for the quarter, held immaterial to the Group per Management).

Entities: 4 distinct (1 holding + 3 subsidiaries); each named in 2 separate lists = 8 total list-appearances enumerated.

## 10. Digital / physical signature blocks

| # | Page/Line | Signatory | Designation | Timestamp / Date | Flags |
|---|-----------|-----------|-------------|-------------------|-------|
| 1 | p.1, lines 44-49 | Anantha Murthy Narayana (ANANTHA MURTHY NARAYANA) | Company Secretary & Compliance Officer | "Digitally signed by ANANTHA MURTHY NARAYANA, Date: 2026.07.27 17:51:32 +05'30'" | Only signature block with an explicit digital timestamp in the OCR text. 17:51:32 IST is AFTER the board meeting's stated end time of 4:40 P.M. (16:40) IST — consistent (signed after the meeting concluded), no pre-meeting-signature flag warranted |
| 2 | p.2, lines 109-120 | Prasanna Padar Mahabala | Partner, Price Waterhouse Chartered Accountants LLP (Firm Reg. 012754N/N500016) | Place: Bengaluru; Date: July 27, 2026 (no time-of-day captured in OCR); UDIN: 26206477VOPILA4407 | Standalone auditor review report sign-off |
| 3 | p.4, lines 227-230 | Arnob Roy | Managing Director and CEO (DIN: 03176672) | Place: Bengaluru; Date: July 27, 2026 (no time-of-day captured) | Standalone financial results sign-off, "On behalf of the Board of Directors" |
| 4 | p.6, lines 334-340 | Prasanna Padar Mahabala | Partner, Price Waterhouse Chartered Accountants LLP (Firm Reg. 012754N/N500016) | Place: Bengaluru; Date: July 27, 2026 (no time-of-day captured); UDIN: 26206477ULOFUU1403 | Consolidated auditor review report sign-off; UDIN differs from standalone (expected — separate reports) |
| 5 | p.8, lines 474-477 | Arnob Roy | Managing Director and CEO (DIN: 03176672) | Place: Bengaluru; Date: July 27, 2026 (no time-of-day captured) | Consolidated financial results sign-off, "On behalf of the Board of Directors" |

---
## Flags raised (roll-up)
- ZERO_STANDING x5 — Standalone: Current tax expense/(benefit) (Section 3, row 19); Income tax relating to remeasurement OCI item (row 26); Income tax relating to cash-flow-hedge OCI item (row 29). Consolidated: Income tax relating to remeasurement OCI item (Section 4, row 26); Income tax relating to gains/losses in cash-flow-hedge OCI item (row 30).
- Consolidated Current tax expense/(benefit) (Section 4, row 19) explicitly NOT ZERO_STANDING despite being the consolidated counterpart of a standalone ZERO_STANDING row — small non-zero values appear in Q1 FY26 and FY26-audited, attributable to subsidiary-level current tax. Carried forward as a named divergence, not flagged with a formal code.
- Entity-naming inconsistency within this single filing (auditor report vs Note 1) for "Tejas Communications/Communication Pte. Limited, Singapore" and "Saankhya Labs Inc/Inc." — not ENTITY_CHANGE (no prior ledger to diff against on this first run), but named for A3/A4.
- No formal ENTITY_CHANGE, MGMT_ABSENCE, REPEAT_QUESTION, or DROPPED_SLIDE flags applicable — this doctype has no prior-quarter ledger for diffing, and results filings do not carry participant/turn/slide categories (those apply to concall transcripts and investor decks, not enumerated here).
- Only 1 of 5 signature blocks in the filing carries an explicit digital timestamp; that one timestamp postdates the board meeting's stated end time, consistent, not a flag.
- Unnumbered auditor paragraph (SEBI Regulation 33(8) circular procedures, consolidated report only) — genuinely unnumbered in source, not an OCR artifact; carried as its own ledger row.
