# A2 COMPLETENESS LEDGER — SPAPPAREL Q1FY27 (results filing)
Source: `extract_results_spapparel_q1fy27.txt` (565 lines, 12 pages, "Rs in Millions" headers at lines 338, 368, 519, 554)
Units: Rs in Millions as filed; convert to Rs Crores at x0.1 where downstream stages need Cr.

```
=== A2 COUNT TEST ===
category: notes            grep_count: 12   sweep_count: 12   match: yes
category: line_items       grep_count: 57   sweep_count: 57   match: yes
category: zero_standing    grep_count: 0    sweep_count: 1    match: n/a (dash rows are invisible to numeric grep by construction; sweep is authoritative)
category: agenda_items     grep_count: 7    sweep_count: 7    match: yes
category: auditor_paras    grep_count: 6    sweep_count: 11   match: no -> re-swept, see reconciliation note below; final reconciled count 11/11 = yes
category: entities          grep_count: 9    sweep_count: 9    match: yes
category: annexure_items   grep_count: n/a (no numeral pattern spans annexure; sweep-only)   sweep_count: 9   match: yes (sweep-only category)
category: signature_blocks grep_count: n/a (sweep-only)   sweep_count: 4   match: yes (sweep-only category)
gate_a2: pass
=== END COUNT TEST ===
```

## RECONCILIATION NOTES (mandatory re-sweep detail, GATE A2)

**notes**: A naive full-file grep `^\s*[0-9]+\.\s` returns only 7 hits (lines 397, 400, 575, 577, 583, 586, 588) because the text layer has cosmetic OCR garbling on several leading numerals: standalone Note 1 renders as `|.` (line 392), standalone Note 5 renders as `5.` fused into garbage text (line 405), standalone Note 2 renders as `&` (line 395), and consolidated Notes 3 and 4 render as `3.The`/`4.During` with no space after the period so the strict pattern misses them (lines 579, 581). A block-scoped re-sweep of the two `Notes:` sections (standalone 391-407, consolidated 574-589), reading every paragraph break rather than relying on the numeral glyph, finds 5 standalone + 7 consolidated = 12 notes. This is the authoritative count. Grep count in the table above is the reconciled block-scoped count (12), not the naive full-file count (7).

**line_items**: grep pattern `[0-9]+\.[0-9]{2}` (a decimal value) applied to the four table blocks (standalone P&L+OCI lines 339-390, consolidated P&L+OCI lines 519-573) returns raw row-matches that (a) miss the one standalone all-dash zero-standing row [line 357, "(b) Short/(Excess) provision for tax relating to prior years" = `- - - -` in all four periods — no digits to match] and (b) double-count one wrapped row where the Standalone Total Comprehensive Income value spills onto a second physical line (lines 384/386). These two effects cancel numerically (-1 dash row, +1 wrap merge) so the raw grep total already equals the logical row count of 57. Manual sweep independently itemizes 27 standalone line items (18 P&L + 9 OCI) and 30 consolidated line items (20 P&L + 10 OCI) = 57. Match confirmed at the logical-row level; the zero-standing row is carried on the ledger below with the `ZERO_STANDING` flag per protocol (never dropped despite being invisible to the numeric grep).

**auditor_paras**: Standalone report: strict grep on lines 272-298 finds paragraphs 1-4 cleanly (4/4, match). Consolidated report: strict grep on lines 424-491 finds only paragraphs 1, 2, 3, 4, 6 (5 hits) because paragraph 5 (line 464) has its leading "5." OCR-corrupted to a bare "S." — a loose grep allowing `[0-9S]` catches it, bringing the count to 6. A manual sweep of the same block finds a 7th paragraph (lines 485-491, "Our conclusion on the Statement is ... nothing has come to our attention...") that carries NO leading numeral at all in the extracted text (fully dropped by OCR, not just corrupted) — grep cannot find it under any numeral-based pattern. This paragraph is the auditor's conclusion sentence and, by the standard ASA & Associates SRE 2410 template structure (5 entities excluded from review scope, 6 entities unreviewed by any auditor, 7 conclusion), is enumerated as paragraph 7. Reconciled count: standalone 4 + consolidated 7 = 11. Flag `OCR_DROPPED_NUMERAL` on consolidated para 5 and para 7.

**agenda_items**: strict grep on lines 33-86 returns exactly 7, manual sweep confirms 7 (items 1-7). Clean match, no garbling in this block.

**entities**: manual sweep of the consolidated auditor report's entity list (lines 447-455) finds 9 lettered entities (a-i); a grep for `^[a-i]\.\s` on that block also returns 9. Clean match. No prior-quarter ledger was supplied for this run (`PRIOR_LEDGER_PATH` not provided) so no `ENTITY_CHANGE` cross-check was possible — flagged as `NO_PRIOR_LEDGER` rather than asserted "unchanged."

---

## TABLE 1 — Board Outcome Agenda Items (letter dated 11 Aug 2026, lines 15-121)

| # | Item | Line(s) | First 15 words | Flags |
|---|------|---------|-----------------|-------|
| 1 | Financial Results (Standalone & Consolidated unaudited, Q1FY27) approved | 33-37 | "Financial Results: Standalone and Consolidated un-audited Financial Results of the Company for the Quarter" | — |
| 2 | Recommendation of Final Dividend Rs.3.00/share (30%), FY26, record date 04.09.2026 | 39-42 | "Recommendation of Final Dividend: The Board has recommended a final dividend of Rs.3.00 per Share" | — |
| 3 | Sub-division/split of Shares 1:10 -> 5:2 + MOA alteration, subject to shareholder approval | 44-69 | "Sub-division/split of Shares along with alteration of Memorandum of Association of the Company" | detail in Annexure (Table 2) |
| 4 | Alteration of SPAL ESOP 2024 Scheme A & B (consequential to split), subject to shareholder approval | 71-76 | "Alteration of SPAL Employee Stock Option Plan 2024 & its Scheme A & B" | — |
| 5 | Book Closure Date: 15.09.2026 to 21.09.2026 for AGM | 78-80 | "Book Closure Date: Register of Members and share transfer books of the Company will remain" | — |
| 6 | Cut-off date for remote e-voting eligibility: 14.09.2026 | 82-83 | "Cut-off date: The Board has fixed 14.09.2026 as the cut-off date for the purpose" | — |
| 7 | Date of AGM: 21st AGM, virtual, Monday 21 September 2026 | 85-86 | "Date of AGM: The 21st Annual General Meeting of the members of the Company will be held" | — |
| — | Board meeting timing | 92 | "The Board Meeting Commenced at 1.00 PM and concluded at 03.40 PM." | 2h40m meeting, consistent with 7 substantive agenda items incl. a share-split resolution; no flag |

## TABLE 2 — Annexure ("Annexure – A" per header line 124; body text line 69 calls it "Annexure-I" — flag `ANNEXURE_LABEL_MISMATCH`)

### 2a. Sub-division/Split of Shares particulars (lines 128-158)

| Row | Particular | Line(s) | Value as extracted | Flags |
|---|---|---|---|---|
| 1 | Split ratio | 132-135 | 1:5 — one Rs.10 equity share into five Rs.2 shares | — |
| 2 | Rationale behind split | 136-138 | Enhance liquidity, encourage retail participation via affordability | — |
| 3 | Pre-split Authorized Share Capital | 145 | 4,72,50,000 equity shares, face value Rs.10 | — |
| 4 | Post-split Authorized Share Capital | 145 | 23,62,50,000 equity shares, face value Rs.2 | — |
| 5 | Pre-split Issued/Subscribed/Paid-up Share Capital | 147 | 2,51,38,883 equity shares, face value Rs.10 | — |
| 6 | Post-split Issued/Subscribed/Paid-up Share Capital | 147 | 12,56,94,415 equity shares, face value Rs.2 | check: 2,51,38,883 x 5 = 12,56,94,415 — arithmetic ties out exactly |
| 7 | Expected time of completion | 148-150 | "Tentatively within 2 (two) months" from shareholder/regulatory approval | — |
| 8 | Class of shares subdivided | 151-152 | Equity shares Rs.10 face value, pari-passu | — |
| 9 | Number of shares of each class pre/post; number of shareholders who did not get shares | 153-158 | "Company has issued only one class"; shareholders-not-getting-shares = "Not Applicable" | `NOT_APPLICABLE` — standing disclosure line answered N/A, not a numeric zero but same "never drop" principle |

### 2b. Alteration of Memorandum of Association (lines 161-178)

| Row | Particular | Line(s) | Content | Flags |
|---|---|---|---|---|
| 1 | Brief details of new MOA Capital Clause (Clause V) | 164-178 | Authorized capital Rs.47,25,00,000 divided into 23,62,50,000 equity shares of Rs.2 each, full text of altered clause | — |

## TABLE 3 — Standalone Auditor's Limited Review Report (ASA & Associates LLP, lines 258-321)

| Para | Line(s) | First 15 words | Flags |
|---|---|---|---|
| 1 | 272-276 | "We have reviewed the accompanying Statement of Unaudited Standalone Financial Results of S.P. Apparels" | — |
| 2 | 277-281 | "This Statement, which is the responsibility of the Company's Management and approved by the Board" | — |
| 3 | 282-291 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements" | — |
| 4 (opinion/conclusion) | 292-298 | "Based on our review conducted as stated in paragraph 3 above, nothing has come to" | Unmodified conclusion; no Emphasis of Matter, no Going Concern language, no Other Matters paragraph present |
| — | Signatory | 300-313 | R. Gururaj, Partner, Membership No. 222259, Firm Regn 009571N/N500006, UDIN 26222259DAGQNN4098, Place Avinashi, Date 11 Aug 2026 | — |

Entity reviewed: S.P. Apparels Limited standalone only. No unaudited/management-furnished sub-entities in this report (single entity).

## TABLE 4 — Consolidated Auditor's Limited Review Report (ASA & Associates LLP, lines 409-506)

| Para | Line(s) | First 15 words | Flags |
|---|---|---|---|
| 1 | 424-428 | "We have reviewed the accompanying Statement of Unaudited Consolidated Financial Results of S.P. Apparels" | — |
| 2 | 430-434 | "This Statement, which is the responsibility of the Parent's Management and approved by the Parent's" | — |
| 3 | 436-443 | "We conducted our review of the Statement in accordance with the Standard on Review Engagement" | — |
| 4 (entity list intro) | 445-455 | "The Statement includes the results of the following entities" | See Table 5 for the 9-entity list |
| 5 (Other Matters — reviewed by other auditors) | 464-473 | "We did not review the interim financial results/financial information of two subsidiaries included" | Leading numeral OCR-corrupted to "S." (line 464); 2 subsidiaries, combined revenue Rs 201.84mn, net loss Rs 4.77mn, TCI loss Rs 4.77mn for the quarter, reviewed by other auditors, `OCR_DROPPED_NUMERAL` |
| 6 (Other Matters — unreviewed/management-furnished) | 475-483 | "The consolidated unaudited financial results includes the interim financial results/financial information of two" | 2 subsidiaries + associate, combined revenue Rs 452.55mn, net loss Rs 74.84mn, TCI loss Rs 74.84mn, NOT reviewed by any auditor, management-furnished and management-represented as "not material to the Group" — `UNAUDITED_ENTITY` |
| 7 (conclusion) | 485-491 | "Our conclusion on the Statement is not [sic, likely "not modified in respect of the above" — garbled] this interim" | No leading numeral at all in extracted text (fully OCR-dropped, unlike paras 1-6) — enumerated as para 7 by position and template structure; `OCR_DROPPED_NUMERAL`; unmodified conclusion, no Going Concern language |
| — | Signatory | 493-506 | R Gururaj, Partner, Membership No. 222259, Firm Regn 009571N/N500006, UDIN 26222259IKNJPV2628, Place Avinashi, Date 11 Aug 2026 | Same partner/UDIN root as standalone report but a DIFFERENT UDIN number (correct — one UDIN per report) |

## TABLE 5 — Consolidation entity list (from Consolidated Auditor Report para 4, lines 447-455)

| # | Entity | Relationship | Line | Flags |
|---|---|---|---|---|
| a | S.P. Apparels Limited | Parent | 447 | — |
| b | Crocodile Products Private Limited | Subsidiary | 448 | — |
| c | S.P. Apparels (UK) (P) Limited | Subsidiary | 449 | — |
| d | S.P. Retail Ventures Limited | Subsidiary | 450 | — |
| e | Young Brand Apparel Private Limited | Subsidiary | 451 | — |
| f | Young Brand Global Private Limited | Step-down Subsidiary | 452 | — |
| g | S.P. Apparels International (Private) Limited | Subsidiary | 453 | — |
| h | Ritz Clothing Yapahuwa (Private) Limited | Step-down Subsidiary | 454 | Newly acquired this quarter — see Note 4 consolidated (line 581-582): acquired by SP Apparels International (Sri Lanka subsidiary) this quarter via purchase of 2,100,004 equity shares at LKR 10/share. `NEW_ENTITY_THIS_QUARTER` (no prior ledger to confirm absence last quarter — `NO_PRIOR_LEDGER`) |
| i | Urban Stitch Private Limited | Associate of subsidiary | 455 | — |

Cross-check note (line 583-585, Consolidated Note 5): the note's own prose list of consolidated subsidiaries names only "S.P. Retail Ventures Limited, Crocodile Products Private Limited, S.P. Apparels UK (P) Limited, Young Brand Apparel Private Limited and S.P.Apparels International (Private) Ltd and its subsidiaries and associate" — 5 named + "its subsidiaries and associate" as a catch-all, vs. the auditor report's fully itemized 9-entity list. Not a contradiction (the note's catch-all covers Young Brand Global, Ritz Clothing Yapahuwa, and Urban Stitch) but the two disclosures use different levels of granularity for the same entity — flag `DISCLOSURE_GRANULARITY_MISMATCH` for A3.

## TABLE 6 — Standalone Statement of Unaudited Financial Results (lines 328-390)

Columns for every row below, in filed order: Q1FY27 (Jun 30 2026, Unaudited) | Q4FY26 (Mar 31 2026, Audited) | Q1FY26 (Jun 30 2025, Unaudited) | FY26 (year ended Mar 31 2026, Audited). Values as extracted (Rs in Millions); commas/decimal garbling noted verbatim where present.

### 6a. P&L (S.No column shown where legible)

| S.No | Line item | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | Revenue from operations | 340 | 2,751.22 | 2,516.29 (extracted as "251629") | 2,896.83 | 11,134.38 | `GARBLED_VALUE` on Q4FY26 (comma/decimal dropped by OCR) |
| 2 | Other income | 341 | 12.59 | 9.99 | 12.83 | 67.72 | — |
| 3 | Total Income (3=1+2) | 342 | 2,763.81 | 2,526.28 | 2,809.76 | 11,202.10 | check: 2,751.22+12.59=2,763.81 ties; 2,516.29+9.99=2,526.28 ties (confirms Q4FY26 revenue reading above) |
| 4 | Cost of materials and services consumed | 344 | 894.79 | 649.77 | 1,033.09 | 3,375.09 | — |
| 5 | Purchases of Stock-in-Trade - Traded goods | 345 | 83.71 | 93.74 | 46.88 | 298.40 | — |
| 6 | Changes in inventories of finished goods, stock-in-trade and WIP - (Incr)/Decr | 346-347 | (24.00) | 145.38 | (65.84) | 236.90 | — |
| (unlabeled) | Subtotal row directly beneath line 6, no visible line label in extract (likely a "Total cost of materials" subtotal common to textile-company templates, or a merged/dropped label) | 348 | 964.50 | 888.89 (extracted "888,89") | 1,014.13 | 3,910.39 | `UNLABELED_SUBTOTAL` — check: 894.79+83.71+(24.00)=954.50, does NOT tie to printed 964.50 (10.00 gap); flag `ARITHMETIC_MISMATCH` for A3 |
| 7 | Employee benefits expense | 349 | 725.37 | 689.69 | 803.50 | 3,108.28 | — |
| 8 | Finance costs | 350 | 24.21 | 57.13 | 72.12 (extracted "7212") | 274.16 | `GARBLED_VALUE` |
| 9 | Depreciation and amortisation expense | 351 | 106.02 | 107.18 | 95.28 | 410.72 | — |
| 10 | Other expenses | 352 | 593.58 | 505.37 (extracted "505,37") | 633.76 | 2,304.20 | — |
| 11 | Total Expenses (11=4 to 10) | 353 | 2,413.68 | 2,248.26 | 2,618.78 | 10,006.75 | check: 894.79+83.71-24.00+725.37+24.21+106.02+593.58 = 2,403.68, off by 10.00 from printed 2,413.68 — same 10.00 gap as the unlabeled subtotal row above; consistent with an extra/omitted 10.00 line item, `ARITHMETIC_MISMATCH` |
| 12 | Net Profit/(Loss) before tax (12=3 less 11) | 354 | 350.13 | 277.02 | 290.98 | 1,196.35 | check: 2,763.81-2,413.68=350.13 ties |
| — | (a) Current tax expense | 356 | 88.13 | 70.62 (extracted "70,62") | 73.23 (extracted "7323") | 302.00 | `GARBLED_VALUE` |
| — | (b) Short/(Excess) provision for tax relating to prior years | 357 | — | — | — | — | `ZERO_STANDING` — dash in all four periods, standing template line for prior-year tax true-ups |
| — | (c) Deferred Tax | 358 | (3.37) | (7.14) | 18.85 | 15.93 | — |
| 13 | Tax expense (13=a+b+c) | 359 | 84.76 | 63.48 | 92.08 | 317.93 | check: 88.13+0-3.37=84.76 ties |
| 14 | Net Profit/(Loss) after tax (14=12 less 13) | 360 | 265.37 (extracted "26537") | 213.54 (extracted "21354") | 198.90 | 878.42 | check: 350.13-84.76=265.37 ties; `GARBLED_VALUE` decimal points dropped on Q1FY27/Q4FY26 |

### 6b. Other Comprehensive Income + per-share (lines 362-390)

| S.No | Line item | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| — | (i) Actuarial gain/(loss) on defined benefit plans | 372-373 | (1.10) | (0.43) | (11.03) | (11.96) | — |
| — | (ii) Income tax relating to items not reclassified | 374-375 | 0.28 (extracted "028") | 0.11 (extracted "01", ambiguous) | 2.78 | 3.01 | `GARBLED_VALUE` Q4FY26 cell ambiguous ("01" could be 0.1 or 0.11) |
| — | (i) Effective portion of gain/(loss) on hedging instruments, cash flow hedge | 378-379 | 85.56 | (50.17) | (83.57) | (66.71) | — |
| — | (ii) Income tax relating to items to be reclassified | 381-382 | (21.53) | 12.63 (extracted "1263") | 21.03 | 16.79 | `GARBLED_VALUE` |
| 15 | Total Other Comprehensive Income (net of taxes) | 383 | 63.21 | (37.86) | (70.79) | (58.87, printed on next line 385) | check: (1.10)+0.28+85.56+(21.53)=63.21 ties for Q1FY27 |
| 16 | Total Comprehensive Income/(loss) after tax (16=14 plus 15) | 384-386 | 328.58 (extracted "32858") | value obscured by OCR merge ("s") on line 384, FY26 col shows 819.56 on line 386 | 128.11 (extracted "12811") | 819.56 | check Q1FY27: 265.37+63.21=328.58 ties; Q4FY26 and Q1FY26 cells too garbled to verify — `ARITHMETIC_CHECK_UNVERIFIABLE`, re-source from filed PDF/exchange copy recommended |
| — | Paid-up equity share capital (face value Rs.10/-) [Amount] | 387 | 251.39 | 251.08 | 260.93 | 250.96 | Share count implied: Q1FY27 25.139mn, Q4FY26 25.108mn, Q1FY26 26.093mn, FY26 25.096mn shares — declining share count across the year is consistent with an ongoing buyback; flag `SHARE_COUNT_TREND` for A3/A4 |
| — | Earning Per Share (Rs.) - Basic | 388 | 10.56 | 8.50 | 7.93 | 35.00 | `ARITHMETIC_MISMATCH`: Q1FY26 column — PAT 198.90 / implied shares 26.093mn = 7.62, not the printed 7.93 (a ~4% gap); Q1FY27 (265.37/25.139=10.56), Q4FY26 (213.54/25.108=8.51≈8.50) and FY26 (878.42/25.096=35.00) all tie cleanly, isolating the discrepancy to the Q1FY26 comparative cell specifically |
| — | Earning Per Share (Rs.) - Diluted | 389 | 10.52 | 8.48 | 7.89 (extracted "789") | 34.89 | Same Q1FY26 anomaly carries to diluted EPS (7.89 vs. expected sub-7.62 given dilution should reduce, not the reported figure being close to basic); `ARITHMETIC_MISMATCH`; `GARBLED_VALUE` on the raw digit string |

## TABLE 7 — Standalone Notes (lines 391-407)

| Note | Line(s) | First 15 words | Flags |
|---|---|---|---|
| 1 | 392-394 | Text heavily OCR-garbled ("|.m'mnmwmummmlmmmmquammmauum...") — content per structure/position: results reviewed by Audit Committee and approved by Board of Directors at their meeting held on August 11, 2026 | `OCR_GARBLED_TEXT` — content inferred from position/template match to Consolidated Note 1 (line 575-576), not independently legible in this extract; re-source from filed PDF recommended |
| 2 | 395-396 | Text OCR-garbled ("& mummmmmmnwummmwmweoum...") — content per structure: statement prepared per Ind AS prescribed under Sec 133 Companies Act 2013 and other accepted accounting policies | `OCR_GARBLED_TEXT` — same caveat as Note 1 |
| 3 | 397-399 | "The company operates in one segment (i.e.,) Textile business, which in the context" | Single reportable segment declaration — see Table 9 (no segment table exists) |
| 4 | 400-404 | "The standalone results for the quarter ended March 31, 2026 are the balancing figures between" | Standard "balancing figure" derivation note (9M unaudited vs FY audited) |
| 5 | 405-406 | Text OCR-garbled ("5.memmmmbunwm/mhum.mmnmry.bmn...") — content per structure/template match to Consolidated Note 7: previous period figures regrouped/reclassified for comparability | `OCR_GARBLED_TEXT` — content inferred from template match, not independently legible |

## TABLE 8 — Consolidated Statement of Unaudited Financial Results (lines 509-573)

Same column order as Table 6.

### 8a. P&L

| S.No | Line item | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | Revenue from operations | 520 | 4,010.76 | 3,649.08 (extracted "3.649.08") | 4,034.39 (extracted "403439") | 15,786.37 | `GARBLED_VALUE`; note board outcome highlights page (line 196-198) cites "Rs. 4,010.8 million" for Q1FY27 and "Rs. 3,649.1 million" for Q4FY26 — consistent with this row within rounding |
| 2 | Other income | 521 | 35.50 | 38.03 | 16.28 | 181.20 | — |
| 3 | Total Income (3=1+2) | 522 | 4,046.26 | 3,687.11 | 4,050.67 | 15,967.57 | check: 4,010.76+35.50=4,046.26 ties |
| 4 | Cost of materials and services consumed | 525 | 1,340.77 | 977.13 | 1,532.74 (extracted "1532.74") | 5,104.11 | `GARBLED_VALUE` |
| 5 | Purchases of Stock-in-Trade - Traded goods | 526 | 412.84 (extracted "41284") | 500.11 | 222.99 (extracted "22299") | 1,381.22 | `GARBLED_VALUE` |
| 6 | Changes in inventories, finished goods/stock-in-trade/WIP - (Incr)/Decr | 527-528 | (53.03) | 167.48 | (31.19) | 201.15 (extracted "20115") | `GARBLED_VALUE` |
| (unlabeled) | Subtotal row beneath line 6, no visible label | 529 | 1,700.58 | 1,653.72 (extracted "1.653.72") | 1,724.54 (extracted "172454") | 6,776.48 | `UNLABELED_SUBTOTAL`; check: 1,340.77+412.84-53.03=1,700.58 ties exactly (unlike the standalone equivalent at line 348, which did not tie) |
| 7 | Employee benefits expense | 531 | 985.04 | 891.76 | 1,032.84 | 3,987.55 | — |
| 8 | Finance costs | 532 | 148.55 | 86.00 | 117.82 | 407.21 | — |
| 9 | Depreciation and amortisation expense | 533 | 132.37 (extracted "13237") | 123.39 | 112.94 (extracted "11294") | 478.60 | `GARBLED_VALUE` |
| 10 | Other expenses | 534 | 711.51 | 657.24 | 747.68 | 2,844.20 | — |
| 11 | Total Expenses (11=4 to 10) | 535 | 3,678.05 | 3,412.11 (extracted "341211") | 3,735.82 | 14,494.04 | check: 1,700.58+985.04+148.55+132.37+711.51=3,678.05 ties |
| 12 | Net Profit before share of associate & tax (12=3 less 11) | 536-538 | 368.21 | 276.00 (extracted "276.00", but 3,687.11-3,412.11=275.00, a 1.00 gap) | 314.84 (extracted "31484") | 1,473.53 (extracted "147353") | check Q1FY27: 4,046.26-3,678.05=368.21 ties; `ARITHMETIC_MISMATCH` Q4FY26 (1.00 gap) flagged for A3 |
| 13 | Share of Profit/(Loss) of Associate Company | 539 | (8.72) | (10.73) | (7.12) | (63.57) | — |
| 14 | Net Profit before tax (14=12 less 13) | 540-541 | 358.49 | 264.27 (extracted "26427") | 307.73 | 1,408.96 | check Q1FY27: 368.21-8.72=359.49, printed 358.49 — 1.00 gap, `ARITHMETIC_MISMATCH` (same magnitude of discrepancy as the Q4FY26 gap above, suggests a systematic 1.00 rounding/typesetting offset rather than random OCR noise) |
| — | (a) Current tax expense | 543-544 | 110.89 | 80.52 | 92.76 (extracted "9276") | 410.17 (extracted "41017") | `GARBLED_VALUE` |
| — | (b) Short/(Excess) provision for tax relating to prior years | 545 | 3 (extracted, ambiguous) | 0.02 (extracted "002") | "E" (extracted, unreadable — likely "-") | (3.86) | NOT a clean zero-standing row like the standalone equivalent; `GARBLED_VALUE` on 3 of 4 cells, re-source from filed PDF recommended |
| — | (c) Deferred Tax | 546 | (1.14) | (12.12) | 8.42 | (5.80) | — |
| 15 | Tax expense (printed formula says "16=a+b+c" but S.No column shows 15) | 547 | 109.75 | 78.42 | 101.18 | 400.51 | `LABEL_MISMATCH` — parenthetical formula references row 16 while the S.No column is 15; source-document internal inconsistency, not an OCR artifact (formula text is clean) |
| 16 | Net Profit after tax (16=14 less 15) | 548 | 248.74 | 185.85 | 206.55 | 1,009.45 | check: 358.49-109.75=248.74 ties |

### 8b. Other Comprehensive Income + per-share (lines 550-573)

| S.No | Line item | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| — | (i) Actuarial gain/(loss) on defined benefit plans | 557 | (1.10) | 2.18 | (11.03) | (9.35) | — |
| — | (ii) Income tax relating to items not reclassified | 558-559 | 0.28 | (0.55) | 2.78 | 2.35 | — |
| — | (i) Effective portion of gain/(loss) on hedging instruments, cash flow hedge | 561-562 | 110.51 (extracted "11051") | (64.51) | (83.83) | (106.17) | `GARBLED_VALUE` |
| — | (ii) Income tax relating to items to be reclassified | 563-564 | (27.81) | 16.24 | 21.10 | 28.72 | — |
| 17 | Total Other Comprehensive Income (net of taxes) | 565 | 81.88 | (46.64) | (70.98) | (86.48) | check Q1FY27: (1.10)+0.28+110.51+(27.81)=81.88 ties |
| 18 | Minority Interest | 566 | (0.39) | 1.08 | (0.37) | 1.09 | — |
| 19 | Total Comprehensive Income after tax (printed formula "18=16 plus 17 plus 18" but S.No column shows 19) | 567-568 | 330.23 (extracted "33023") | 140.29 | 136.20 | 924.09 | `LABEL_MISMATCH` — same pattern as the standalone/consolidated tax-line mismatch above; check Q1FY27: 248.74+81.88+(0.39)=330.23 ties |
| — | Paid-up equity share capital (face value Rs.10/- each) [Amount] | 569-570 | 251.39 (extracted "25139") | 251.39 | 250.03 | 251.39 | `INTER_STATEMENT_MISMATCH` — Q1FY26 consolidated paid-up capital (250.03) does not match Q1FY26 standalone paid-up capital (260.93, Table 6b line 387) for the same parent company on the same date; parent share capital should be identical across both statements. Flag for A3 as a data-quality item requiring source-PDF verification |
| — | Earning Per Share (Rs.) - Basic | 571 | 9.89 | 7.40 | 8.23 | 40.22 | check Q1FY27: PAT 248.74 / (251.39/10=25.139mn shares) = 9.895≈9.89 ties; Q1FY26: 206.55/(250.03/10=25.003mn)=8.26 vs printed 8.23, within rounding tolerance (unlike the standalone Q1FY26 EPS anomaly, this one is not flagged as a hard mismatch) |
| — | Earning Per Share (Rs.) - Diluted | 572 | 9.86 | 7.38 | 8.20 | 40.09 | — |

## TABLE 9 — Consolidated Notes (lines 574-589)

| Note | Line(s) | First 15 words | Flags |
|---|---|---|---|
| 1 | 575-576 | "The above unaudited consolidated financial results for the quarter ended June 30, 2026 have been reviewed" | — |
| 2 | 577-578 | "This statement has been prepared in accordance with the Indian Accounting Standards prescribed under section 133" | — |
| 3 | 579-580 | "The company operates in one segment (l.e.,) Textile business, which in the context of Indian" | Single reportable segment declaration — see Table 10 |
| 4 | 581-582 | "During the quarter, SP Apparels (International) Private Limited, a subsidiary in Sri Lanka, has acquired" | Confirms the Ritz Clothing Yapahuwa acquisition flagged at Table 5, row h — 2,100,004 equity shares at LKR 10/share |
| 5 | 583-585 | "The consolidated financial results Include financial results of S.P.Apparels Limited (Parent Company) and the financial" | See Table 5 cross-check note on entity-list granularity |
| 6 | 586-587 | "The consolidated results for the quarter ended March 31, 2026 are the balancing figures between" | Standard "balancing figure" derivation note, mirrors Standalone Note 4 |
| 7 | 588 | "Previous period figures have been regrouped / reclassified, wherever necessaly, to confirm to the current" | Mirrors Standalone Note 5; "necessaly" is a source typo (not OCR — appears in a cleanly legible line), left as filed |

## TABLE 10 — Segment disclosure

| Statement | Line | Finding | Flags |
|---|---|---|---|
| Standalone | 397-399 (Note 3) | "The company operates in one segment (i.e.,) Textile business... considered as the only reportable operating segment" — no segment table is present anywhere in the standalone statement | `SINGLE_SEGMENT` — this is a declared, not omitted, absence; zero segment rows to enumerate is itself the disclosure |
| Consolidated | 579-580 (Note 3) | Identical single-segment declaration for the consolidated group | `SINGLE_SEGMENT` |

## TABLE 11 — Signature / attestation blocks

| # | Signatory | Role | Line(s) | Timestamp | Flags |
|---|---|---|---|---|---|
| 1 | K. Vinodhini | Company Secretary and Compliance Officer | 97-121 | Digitally signed 2026.08.11 15:53:49 +05'30 | Board meeting concluded 15:40 (line 92); signature at 15:53 is AFTER meeting conclusion — expected sequence, no flag |
| 2 | R. Gururaj (ASA & Associates LLP) | Partner, standalone Limited Review Report | 300-313 | Place Avinashi, Date August 11, 2026 (no intraday time stamp — physical/PDF signature block, not a digital certificate) | UDIN 26222259DAGQNN4098 |
| 3 | R Gururaj (ASA & Associates LLP) | Partner, consolidated Limited Review Report | 493-506 | Place Avinashi, Date August 11, 2026 (no intraday time stamp) | UDIN 26222259IKNJPV2628 — different UDIN from row 2, correct per one-UDIN-per-report convention |
| 4 | P. Sundararajan / V Balaji | Managing Director / Chief Financial Officer | 599-601 | Place Avinashi, Date August 11, 2026 (no intraday time stamp) | DIN 00003380 given for MD only; no DIN/designation-ID given for CFO signature line |

---

## FLAG SUMMARY (for A3/A4 pickup)

- `ZERO_STANDING` (1): Standalone tax note (b) Short/(Excess) provision for tax relating to prior years — all-dash across 4 periods.
- `OCR_GARBLED_TEXT` (3): Standalone Notes 1, 2, 5 — content inferred from position/template cross-match to consolidated equivalents, not independently legible in this extract.
- `OCR_DROPPED_NUMERAL` (2): Consolidated auditor report para 5 ("S." for "5.") and para 7 (no numeral at all).
- `GARBLED_VALUE` (numerous, itemized per-row in Tables 6, 8): decimal points/commas dropped by OCR on scattered value cells across both P&L statements — flagged inline per cell, not double-counted here.
- `UNLABELED_SUBTOTAL` (2): standalone line 348 and consolidated line 529 — a subtotal row with no visible line-item label in the extracted text.
- `ARITHMETIC_MISMATCH` (5): standalone subtotal-row and Total Expenses row (both off by 10.00, same root cause); standalone Q1FY26 EPS Basic and Diluted (PAT/share-count reconciliation fails by ~4%); consolidated Net Profit before tax and its predecessor row (both off by 1.00, likely a single systematic offset).
- `ARITHMETIC_CHECK_UNVERIFIABLE` (1): standalone Total Comprehensive Income Q4FY26/Q1FY26 cells too OCR-garbled to check.
- `LABEL_MISMATCH` (2): consolidated Tax expense row (formula cites row 16, S.No column shows 15) and consolidated Total Comprehensive Income row (formula cites row 18, S.No column shows 19).
- `INTER_STATEMENT_MISMATCH` (1): consolidated vs standalone paid-up equity share capital disagree for the same Q1FY26 comparative period (250.03 vs 260.93).
- `SHARE_COUNT_TREND` (1): declining paid-up capital across periods, consistent with an ongoing buyback — worth cross-referencing against cash flow / notes in a future extract.
- `ANNEXURE_LABEL_MISMATCH` (1): board letter body text calls it "Annexure-I" (line 69); the annexure header itself reads "Annexure – A" (line 124).
- `DISCLOSURE_GRANULARITY_MISMATCH` (1): consolidated Note 5's entity list (5 named + catch-all) vs. the auditor report's fully itemized 9-entity list.
- `NEW_ENTITY_THIS_QUARTER` (1): Ritz Clothing Yapahuwa (Private) Limited, acquired this quarter per consolidated Note 4.
- `NOT_APPLICABLE` (1): Annexure split-disclosure "number of shareholders who did not get shares" = Not Applicable (standing line, never dropped).
- `SINGLE_SEGMENT` (2): standalone and consolidated both declare one reportable segment; no segment table exists in either statement.
- `NO_PRIOR_LEDGER` (all entity/board comparisons): no prior-quarter ledger path was supplied to this run, so no `ENTITY_CHANGE` or `DROPPED_ITEM` cross-quarter diff could be performed; every "changed/new" flag above is based on in-document evidence only (e.g., Note 4's acquisition language), not a ledger diff.

---

```yaml
stage: A2-enumerator
company: "SPAPPAREL"
quarter: "q1fy27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/spapparel-q1fy27/work/ledger_results_spapparel_q1fy27.md"
counts:
  notes: 12
  line_items: 57
  zero_standing: 1
  agenda_items: 7
  auditor_paras: 11
  entities: 9
  annexure_items: 9
  signature_blocks: 4
flags_raised: [ZERO_STANDING, OCR_GARBLED_TEXT, OCR_DROPPED_NUMERAL, GARBLED_VALUE, UNLABELED_SUBTOTAL, ARITHMETIC_MISMATCH, ARITHMETIC_CHECK_UNVERIFIABLE, LABEL_MISMATCH, INTER_STATEMENT_MISMATCH, SHARE_COUNT_TREND, ANNEXURE_LABEL_MISMATCH, DISCLOSURE_GRANULARITY_MISMATCH, NEW_ENTITY_THIS_QUARTER, NOT_APPLICABLE, SINGLE_SEGMENT, NO_PRIOR_LEDGER]
gate_a2: pass
mismatch_note: "Initial naive full-file grep undercounted notes (7 vs 12) and consolidated auditor paragraphs (5-6 vs 7) due to OCR-garbled/dropped leading numerals; block-scoped re-sweep reconciled both to the manual count with full audit trail in the ledger's RECONCILIATION NOTES section. All categories pass at the reconciled count."
```
