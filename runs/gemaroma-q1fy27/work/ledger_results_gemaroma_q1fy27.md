# A2 ENUMERATION LEDGER — Gem Aromatics Limited (GEMAROMA), Q1 FY27, Results (Reg 33)
Source: /home/user/inflection-pipeline/runs/gemaroma-q1fy27/work/extract_results_gemaroma_q1fy27.txt (466 lines, 8 pages, 100% page coverage per A1 header)
Prior-quarter ledger: NONE (first-time coverage of this company — no diff baseline; ENTITY_CHANGE cannot be tested against history this run)

```
=== A2 COUNT TEST ===
category: notes            grep_count: 17   sweep_count: 17   match: yes
  (15 numbered notes [7 standalone + 8 consolidated, corrected grep pattern to
  admit stray leading quote before "(5)" at line 437] + 2 unnumbered asterisk
  footnotes [EPS non-annualization, lines 219 & 417])
category: line_items       grep_count: 59   sweep_count: 59   match: yes
  (29 standalone table rows [lines 167-218] + 30 consolidated table rows
  [lines 369-416]; raw grep hits were 30 and 32 respectively, adjusted by
  -1 each: standalone raw 30 includes 1 footnote reclassified to `notes`;
  consolidated raw 32 includes 1 footnote reclassified to `notes` AND 1
  false-positive wrapped continuation string "(loss)" at line 401->404 wrap
  (label "...to profit/(loss)" wraps to a bare "(loss)" line 404 that
  matches the `\([a-z]+\)` pattern but is not a distinct line item))
category: zero_standing    grep_count: 1    sweep_count: 1    match: yes
category: agenda_items     grep_count: 1    sweep_count: 1    match: yes
category: auditor_paras    grep_count: 11   sweep_count: 11   match: yes
  (5 standalone numbered paras + 6 consolidated numbered paras)
category: entities          grep_count: 2    sweep_count: 2    match: yes
  (2 unique entities, each appearing in 2 independent lists = 4 mentions;
  grep -n "Gem Aromatics LLC|Krystal Ingredients" returns 4 line hits,
  unique-entity sweep = 2, both lists agree on relationship type)
category: signature_blocks grep_count: 5    sweep_count: 5    match: yes
  (1 "Digitally signed by" text block + 4 Place:/Date: signatory pairs)
gate_a2: pass
=== END COUNT TEST ===
```

---

## 1. NUMBERED NOTES + UNNUMBERED FOOTNOTES (17)

| # | Location | Line | Note/Footnote no. | First 15 words | Flags |
|---|---|---|---|---|---|
| 1 | Standalone Notes | 227-229 | Note 1 | "These Standalone Financial Results for the quarter ended June 30, 2026 of the Company have been reviewed..." | |
| 2 | Standalone Notes | 231-233 | Note 2 | "These Standalone Financial Results has been prepared in accordance with the recognition and measurement principles..." | |
| 3 | Standalone Notes | 234-235 | Note 3 | "The Company's business activity falls within a single segment i.e. manufacturing and sale of specialty..." | Single-segment disclosure (Ind AS 108) |
| 4 | Standalone Notes | 236-251 | Note 4 | "Change in Accounting Policy — Valuation of Inventories. During the year, the Company has changed..." | Referenced by standalone auditor EoM (para 4); WAC to FIFO change, prospective application only, prior-period impact "not ascertainable" |
| 5 | Standalone Notes | 253-254 | Note 5 | "The figures for the quarter ended March 31, 2026 are the balancing figures between audited..." | |
| 6 | Standalone Notes | 256 | Note 6 | "Figures for the previous periods/year are re-classified/re-arranged/re-grouped, wherever necessary." | |
| 7 | Standalone Notes | 257-258 | Note 7 | "These standalone financial results are available on Stock Exchange websites www.nseindia.com and www.bseindia.com..." | |
| 8 | Standalone P&L footnote | 219 | Unnumbered (asterisk) | "*Earning per share are not annualized for the quarters." | Qualifies EPS line at line 212-215 |
| 9 | Consolidated Notes | 425-427 | Note 1 | "These Standalone Financial Results for the quarter ended June 30, 2026 of the Company have been reviewed..." | Mislabeled: heading says "Standalone" in the Consolidated notes block (copy-paste artifact, not corrected for consolidated context) |
| 10 | Consolidated Notes | 428-430 | Note 2 | "These Standalone Financial Results has been prepared in accordance with the recognition and measurement principles..." | Same mislabeling as Note 1 above |
| 11 | Consolidated Notes | 431-433 | Note 3 | "The Consolidated Financial Results comprise results of following entities as group: i) Krystal Ingredients..." | Entity list — see section 6 |
| 12 | Consolidated Notes | 435-436 | Note 4 | "The Group's business activity falls within a single segment i.e. manufacturing and sale of specialty..." | |
| 13 | Consolidated Notes | 437-449 | Note 5 | "Change in Accounting Policy = Valuation of Inventories. During the year, the Company has changed..." | Referenced by consolidated auditor EoM (para 5); missed by first-pass grep due to stray leading `"` character at line 437 before "(5)" — required corrected regex to catch, see COUNT TEST note |
| 14 | Consolidated Notes | 452-453 | Note 6 | "The figures for the quarter ended March 31, 2026 are the balancing figures between audited..." | |
| 15 | Consolidated Notes | 455 | Note 7 | "Figures for the previous periods/year are re-classified/re-arranged/re-grouped, wherever necessary." | |
| 16 | Consolidated Notes | 457-458 | Note 8 | "These consolidated financial results are available on Stack Exchange websites www.nseindia.com and www.bseindia.com..." | |
| 17 | Consolidated P&L footnote | 417 | Unnumbered (asterisk) | "*Earning per share are not annualized for the quarters." | Qualifies EPS line at line 411-413 |

---

## 2. STANDALONE FINANCIAL RESULTS — EVERY LINE ITEM (29 rows, lines 167-218)

| # | Line | Item | Jun-26 | Mar-26(Q) | Jun-25 | Mar-26(FY) | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 167 | (1) INCOME [header] | — | — | — | — | |
| 2 | 168 | (a) Revenue from operations | 829.86 | 1,122.44 | 763.96 | 3,709.41 | |
| 3 | 170 | (b) Other income | 41.57 | 38.34 | 25.82 | 122.58 | |
| 4 | 171 | TOTAL INCOME | 871.43 | 1,160.78 | 789.78 | 3,831.99 | |
| 5 | 174 | (2) EXPENSES [header] | — | — | — | — | |
| 6 | 175 | (a) Cost of materials consumed | 708.11 | 691.94 | 729.81 | 3,208.83 | |
| 7 | 177 | (b) Changes in inventories of finished goods and WIP | (25.11) | 168.36 | (157.12) | (244.37) | |
| 8 | 179 | (c) Employee benefits expense | 30.53 | 26.20 | 33.94 | 101.53 | |
| 9 | 180 | (d) Finance costs | 13.34 | 15.17 | 29.28 | 94.61 | |
| 10 | 182 | (e) Depreciation and amortisation expense | 16.06 | 13.86 | 14.39 | 63.11 | |
| 11 | 183 | (f) Other expenses | 31.19 | 85.42 | 52.19 | 249.79 | |
| 12 | 184 | TOTAL EXPENSES | 774.12 | 1,000.95 | 702.49 | 3,473.50 | |
| 13 | 187 | (3) Profit before tax (1-2) | 97.31 | 159.83 | 87.29 | 358.49 | |
| 14 | 190 | (4) Tax expenses [header] | — | — | — | — | |
| 15 | 191 | (a) Current tax | 25.38 | 49.47 | 21.00 | 106.47 | |
| 16 | 193 | (b) Deferred tax | (0.59) | (8.32) | 1.06 | (15.07) | |
| 17 | 194 | (c) Tax relating to prior years | dash | dash | dash(blank) | dash | **ZERO_STANDING** — OCR renders dash glyphs as garbled "B"/"S" characters but all 4 periods carry no numeric value; row exists as a template line for prior-year tax true-ups that have not occurred in any period shown |
| 18 | 196 | Total Tax expense | 24.79 | 41.15 | 22.06 | 91.40 | |
| 19 | 199 | (5) Profit for the period/year (3-4) | 72.52 | 118.68 | 65.23 | 267.09 | |
| 20 | 201 | (6) Other comprehensive income [header] | — | — | — | — | |
| 21 | 202 | (a) Items that will not be reclassified to P&L [sub-header] | — | — | — | — | |
| 22 | 203 | (i) Remeasurement of defined employee benefit plans | 0.51 | (1.29) | (0.22) | (1.04) | |
| 23 | 204-205 | (b) Income tax relating to items that will not be reclassified to profit/(loss) | (0.13) | 0.32 | 0.06 | 0.26 | |
| 24 | 206 | Total other comprehensive income for the period/year | 0.38 | (0.97) | (0.16) | (0.78) | |
| 25 | 209 | (7) Total comprehensive income for the period/year (5+6) | 72.90 | 117.71 | 65.07 | 266.32 | |
| 26 | 212 | Earnings per equity share of face value of Rs 2 each* [header] | — | — | — | — | Footnote-qualified, see Notes row 8 |
| 27 | 214 | (1) Basic (in Rs) | 1.39 | 2.33 | 1.39 | 5.33 | Source OCR shows "233"/"139" — read as 2.33/1.39, digit-run OCR artifact, not a value discrepancy |
| 28 | 215 | (2) Diluted (in Rs) | 1.39 | 2.33 | 1.39 | 5.33 | Same OCR artifact as row 27 |
| 29 | 218 | Paid up Equity Share Capital (Face value Rs 2 each) | 104.47 | 104.47 | 93.71 | 104.47 | |

---

## 3. CONSOLIDATED FINANCIAL RESULTS — EVERY LINE ITEM (30 rows, lines 369-416)

| # | Line | Item | Jun-26 | Mar-26(Q) | Jun-25 | Mar-26(FY) | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 369 | (1) INCOME [header] | — | — | — | — | |
| 2 | 370 | (a) Revenue from operations | 988.50 | 1,104.11 | 876.33 | 3,664.73 | |
| 3 | 371 | (b) Other income | 1.61 | 3.00 | 12.69 | 8.96 | OCR shows "161" (units millions, read as 1.61) |
| 4 | 372 | TOTAL INCOME | 990.11 | 1,107.11 | 889.02 | 3,673.69 | |
| 5 | 375 | (2) EXPENSES [header] | — | — | — | — | |
| 6 | 376 | (a) Cost of materials consumed | 990.38 | 762.39 | 716.20 | 3,235.20 | |
| 7 | 377 | (b) Changes in inventories of finished goods and WIP | (167.02) | 4.51 | (98.63) | (473.71) | OCR shows "451" for Mar-26(Q), read as 4.51 |
| 8 | 378 | (c) Employee benefits expense | 70.64 | 61.56 | 40.60 | 164.13 | |
| 9 | 379 | (d) Finance costs | 28.83 | 29.73 | 35.21 | 126.95 | |
| 10 | 380 | (e) Depreciation and amortisation expenses | 51.27 | 90.03 | 18.19 | 225.89 | OCR shows "5127" for Jun-26, read as 51.27 |
| 11 | 381 | (f) Other expenses | 61.44 | 118.53 | 69.59 | 331.59 | |
| 12 | 382 | TOTAL EXPENSES | 1,075.54 | 1,066.81 | 781.16 | 3,610.05 | |
| 13 | 385 | (3) Profit before tax (1-2) | (85.43) | 40.30 | 107.86 | 63.64 | |
| 14 | 388 | (4) Tax expenses [header] | — | — | — | — | |
| 15 | 389 | (a) Current tax | 26.63 | 55.80 | 31.87 | 121.45 | |
| 16 | 390 | (b) Deferred tax | (33.32) | (25.44) | (3.85) | (66.04) | |
| 17 | 391 | (c) Tax expense relating to prior years | dash | (0.19) | dash | (6.02) | NOT zero-standing — 2 of 4 periods carry non-zero values (Mar-26 Q and Mar-26 FY); dash only in Jun-26 and Jun-25 |
| 18 | 392 | Total Tax expense | (6.69) | 30.17 | 28.02 | 49.39 | |
| 19 | 395 | (5) Profit for the period/year (3-4) | (78.74) | 10.13 | 79.84 | 14.25 | |
| 20 | 398 | (6) Other comprehensive income [header] | — | — | — | — | |
| 21 | 399 | (a) Items that will not be reclassified to P&L [sub-header] | — | — | — | — | |
| 22 | 400 | (i) Exchange differences on translation of foreign operations | (3.38) | (10.42) | (0.26) | (5.83) | No standalone equivalent — consolidated-only line (foreign subsidiary translation) |
| 23 | 401 | (ii) Remeasurement of defined employee benefits plan | 1.02 | (1.29) | (0.22) | (1.04) | |
| 24 | 403-404 | (b) Income tax relating to items that will not be reclassified to profit/(loss) | (0.26) | 0.32 | 0.06 | 0.26 | Label wraps to a bare "(loss)" continuation at line 404 — not a separate line item (see COUNT TEST note) |
| 25 | 405 | Total other comprehensive income for the period/year | (2.62) | (11.39) | (0.42) | (6.61) | |
| 26 | 408 | (7) Total comprehensive income for the period/year (5+6) | (81.36) | (1.26) | 79.42 | 7.64 | |
| 27 | 411 | Earnings per equity share of face value of Rs 2 each* [header] | — | — | — | — | Footnote-qualified, see Notes row 17 |
| 28 | 412 | (1) Basic (in Rs) | (1.56) | 0.19 | 1.70 | 0.28 | |
| 29 | 413 | (2) Diluted (in Rs) | (1.56) | 0.19 | 1.70 | 0.28 | OCR shows "170" for Jun-25, read as 1.70 |
| 30 | 416 | Paid up Equity Share Capital (Face value Rs 2 each) | 104.47 | 104.47 | 93.71 | 104.47 | |

---

## 4. BOARD OUTCOME — AGENDA ITEMS (1 row — no items beyond item 1 found)

| # | Line | Agenda item | Detail | Flags |
|---|---|---|---|---|
| 1 | 43-54 | Item 1: Approval of Unaudited Standalone and Consolidated Financial Results for Q1 FY27 | Board "considered and approved" the results; also took on record the Limited Review Report dated Aug 13, 2026, from Chhajed & Doshi (enclosures (i) and (ii), not independent agenda items) | Sole agenda item |

Board meeting timing (line 56): commenced 3:19 p.m., concluded 4:07 p.m. — 48-minute meeting.
Full manual sweep of all 8 pages found no other agenda items: no AR approval, no AGM notice/record date, no dividend, no director appointment/resignation, no auditor change, no scrutinizer appointment, no ESOP grant, no capital-raising enabling resolution. Absence explicitly confirmed via grep (`approved|considered|resolved|agenda|dividend|AGM|record date|auditor|scrutinizer|ESOP|director|appointment|resignation|capital raise|preferential|rights issue|buyback`) — no hits beyond the results-approval language and standard report boilerplate.

---

## 5. AUDITOR REVIEW REPORTS — EVERY PARAGRAPH (11 numbered paragraphs + 2 signature blocks)

### 5A. Standalone Limited Review Report (Chhajed & Doshi, pages 2, lines 86-154)

| # | Line | Para | Classification | First 15 words | Flags |
|---|---|---|---|---|---|
| 1 | 97-100 | Para 1 | Scope | "We have reviewed the accompanying statement of Unaudited Standalone Financial Results of Gem Aromatics..." | |
| 2 | 102-107 | Para 2 | Management responsibility / auditor responsibility | "This Statement, which is the responsibility of Company's management and approved by the Company's board..." | |
| 3 | 109-117 | Para 3 | Review standard (SRE 2410) — explicit "we do not express an audit opinion" | "We conducted our review in accordance with Standard on Review Engagements (SRE) 2410..." | |
| 4 | 120-128 | Para 4 | **Emphasis of Matter** — Note 4 FIFO accounting-policy change; conclusion not modified | "We draw attention to Note 4 to the accompanying Statement regarding the change in the Company's..." | EoM |
| 5 | 130-134 | Para 5 | Conclusion — unmodified/unqualified review conclusion | "Based on our review conducted as stated in paragraph 3 above, nothing has come to our attention..." | Opinion type: unmodified |
| — | 90-92 | Report title/heading | Metadata (not a numbered para) | "Independent Auditor's Review Report on Unaudited Standalone Financial Results for the quarter ended June 30, 2026..." | |
| — | 94-95 | Addressee | Metadata | "To the Board of Directors of Gem Aromatics Limited" | |
| — | 137-149 | Signature block | Firm: Chhajed & Doshi, FRN 101794W; Partner name NOT printed (blank between firm block and "Partner" line); Membership No. 196452; UDIN 26196452LLUWIQ2829; Place: Mumbai; Date: Aug 13, 2026 | | Partner signatory name omitted in standalone report (present by name — Abhinav Chhajed — in the consolidated report, same Membership No. 196452, confirming same individual); no formal flag category applies but noted for A3/A4 review |

Entities reviewed (standalone): Gem Aromatics Limited only. No subsidiaries in standalone scope. No Other Matters paragraph. No Going Concern language. No unaudited/management-furnished sub-entity disclosure (single-entity review).

### 5B. Consolidated Limited Review Report (Chhajed & Doshi, pages 5-6, lines 271-355)

| # | Line | Para | Classification | First 15 words | Flags |
|---|---|---|---|---|---|
| 1 | 282-287 | Para 1 | Scope | "We have reviewed the accompanying statement of Unaudited Consolidated Financial Results of Gem Aromatics Limited..." | |
| 2 | 289-295 | Para 2 | Management responsibility / auditor responsibility | "This Statement, which is the responsibility of Holding Company's management and approved by the Holding..." | |
| 3 | 298-308 | Para 3 | Review standard (SRE 2410) — "we do not express an audit opinion" | "We conducted our review in accordance with Standard on Review Engagements (SRE) 2410..." | |
| 4 | 310-315 | Para 4 | **Entity list reviewed** — Gem Aromatics LLC (Subsidiary), Krystal Ingredients Private Limited (Subsidiary) | "The Statement includes the financial results of the following entities:" | Entity list — see section 6; both entities within Group scope of this review (no unaudited/management-furnished carve-out disclosed) |
| 5 | 316-325 | Para 5 | **Emphasis of Matter** — Note 5 FIFO accounting-policy change (Group level); conclusion not modified | "We draw attention to Note 5 to the accompanying Statement regarding the change in the Group's..." | EoM |
| 6 | 331-336 | Para 6 | Conclusion — unmodified/unqualified review conclusion | "Based on our review conducted as stated in paragraph 3 above, nothing has come to our..." | Opinion type: unmodified |
| — | 275-277 | Report title/heading | Metadata | "Independent Auditor's Review Report on Unaudited Consolidated Financial Results for the quarter ended June 30, 2026..." | |
| — | 279-280 | Addressee | Metadata | "To the Board of Directors of Gem Aromatics Limited" | |
| — | 338-350 | Signature block | Firm: Chhajed & Doshi; Partner: Abhinav Chhajed; Membership No. 196452; UDIN 26196452MVIQUT6191; Place: Mumbai; Date: Aug 13, 2026 | | Same partner (Membership No. matches standalone) but different UDIN, as expected (UDIN is per-report/per-signoff) |

No Other Matters paragraph. No Going Concern language. No entity flagged as unaudited or management-furnished — both subsidiaries reviewed within the same Group-level engagement per para 4's plain reading (no carve-out language present).

---

## 6. CONSOLIDATION ENTITY LIST (2 unique entities, 4 list-mentions)

| # | Line | Source list | Entity | Relationship | Flags |
|---|---|---|---|---|---|
| 1 | 313 | Consolidated auditor report, para 4 | Gem Aromatics LLC | Subsidiary | |
| 2 | 314 | Consolidated auditor report, para 4 | Krystal Ingredients Private Limited | Subsidiary | |
| 3 | 432 | Consolidated financial results, Note 3 | Krystal Ingredients Private Limited | Subsidiary (order: i) | Listed first here vs. second in auditor report list — order differs, relationship type consistent |
| 4 | 433 | Consolidated financial results, Note 3 | Gem Aromatics LLC | Subsidiary (order: ii) | |

Cross-check: both lists agree on the 2 entities and both classify them as "Subsidiary." No entity present in one list and absent from the other. **ENTITY_CHANGE: not applicable this run** — prior-quarter ledger path is NONE (first-time coverage of GEMAROMA); no historical entity list exists to diff against. Flag this ledger's entity table as the baseline for the next quarter's A2 diff.

---

## 7. DIGITAL SIGNATURE / SIGNATORY BLOCKS (5)

| # | Line | Signatory | Designation | Timestamp/Date | Context | Flags |
|---|---|---|---|---|---|---|
| 1 | 64-74 | Akshita Deepak Gohil | Company Secretary & Compliance Officer | Digitally signed; "Date: 2026.08.13 17:46:32 +05'30'" | Board Outcome letter to BSE/NSE | Timestamp is 1h39m AFTER board meeting concluded (4:07 p.m. / 16:07) — signed after conclusion, consistent, no early-signature flag |
| 2 | 137-149 | (Partner — name not printed) | Partner, Chhajed & Doshi (Membership No. 196452) | Place: Mumbai; Date: Aug 13, 2026 (no time-of-day given) | Standalone Limited Review Report sign-off | No "Digitally signed by" OCR text captured (image-stamp likely, unlike CS block); partner name omitted, see section 5A flag |
| 3 | 260-269 | Kaksha Vipul Parekh | Whole Time Director & CFO, DIN 00235998 | Place: Dahej (Gujarat); Date: Aug 13, 2026 (no time-of-day) | "For and on behalf of the Board of Directors" — standalone results authorization | |
| 4 | 338-350 | Abhinav Chhajed | Partner, Chhajed & Doshi (Membership No. 196452) | Place: Mumbai; Date: Aug 13, 2026 (no time-of-day) | Consolidated Limited Review Report sign-off | |
| 5 | 459-466 | Kaksha Vipul Parekh | Whole Time Director & CFO, DIN 00235998 | Place: Dahej (Gujarat); Date: Aug 13, 2026 (no time-of-day) | "For and on behalf of the Board of Directors" — consolidated results authorization | Duplicate of row 3's signatory/designation, separate physical block on consolidated notes page |

---

## 8. ANNEXURES

None present. Full manual sweep of all 8 pages (page markers confirmed 1-8, matching A1 header page_count_pdfinfo: 8, formfeed_count: 8, page_coverage: 100%) found no director-profile annexure, no ESOP annexure, no dividend-policy annexure, no scrutinizer report, and no Annual Report. This is a lean, results-only Reg 33 filing consisting of: Board Outcome letter, Standalone Review Report, Standalone Financial Results + Notes, Consolidated Review Report, Consolidated Financial Results + Notes.

---

## RECONCILIATION SUMMARY (GATE A2)

| Category | Grep count | Sweep count | Match |
|---|---|---|---|
| Notes (numbered + footnotes) | 17 | 17 | yes |
| Line items (standalone + consolidated tables) | 59 | 59 | yes |
| Zero-standing line items | 1 | 1 | yes |
| Agenda items | 1 | 1 | yes |
| Auditor report paragraphs | 11 | 11 | yes |
| Consolidation entities (unique) | 2 | 2 | yes |
| Signature blocks | 5 | 5 | yes |

Two reconciliation issues were found and resolved during the sweep, both documented above:
1. Consolidated Note 5 (line 437) was missed by the naive `^\s*\([0-9]+\)\s` grep pattern because of a stray leading `"` character preceding the paragraph marker; a corrected pattern (`^\s*"?\s*\([0-9]+\)\s`) recovered it, bringing grep and sweep to parity at 17.
2. The consolidated table's raw grep for lettered line items produced a false positive at line 404 (`(loss)`), a wrapped continuation of the "(b) Income tax relating to items..." label rather than an independent line item; excluding it (and reclassifying both EPS footnotes from `line_items` into `notes`) brought grep and sweep to parity at 59.

gate_a2: PASS
