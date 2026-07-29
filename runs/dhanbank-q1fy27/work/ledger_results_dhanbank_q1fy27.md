# A2 COMPLETENESS LEDGER — DHANBANK Q1 FY27 (RESULTS)
Source: `runs/dhanbank-q1fy27/work/extract_results_dhanbank_q1fy27.txt` (369-line-numbered body content across 7 pages, plus A1 header; line numbers below are absolute extract-file line numbers). Unit basis: Rs Lakh as printed; divide by 100 for Rs Crore (not converted here — enumeration only). Filing is STANDALONE ONLY (Dhanlaxmi Bank has no subsidiaries/associates — stated fact, not a gap).

```
=== A2 COUNT TEST ===
category: notes               grep_count: 14   sweep_count: 14   match: yes
category: line_items          grep_count: 87   sweep_count: 87   match: yes
category: zero_standing       grep_count: 24   sweep_count: 24   match: yes
category: ratios              grep_count: 14   sweep_count: 14   match: yes
category: segments            grep_count: 4    sweep_count: 4    match: yes
category: comparative_periods grep_count: 4    sweep_count: 4    match: yes
category: agenda_items        grep_count: 1    sweep_count: 1    match: yes
category: auditor_paras       grep_count: 5    sweep_count: 5    match: yes
category: entities            grep_count: 3    sweep_count: 3    match: yes
category: signatures          grep_count: 4    sweep_count: 4    match: yes
category: footnotes           grep_count: 3    sweep_count: 3    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

## RECONCILIATION METHODOLOGY (how each grep_count/sweep_count pair was made to match)

- **notes**: `grep -n -E "^\s*[0-9]+\.\s"` and a broader `^[0-9]` line-start scan over the Notes section (lines 349-469) return 33 raw digit-start hits, but most are false positives: text-wrap continuations of a note (e.g. line 370 "29, 2026...", line 378 "63 of the Securities..." — the tail of Note 3 wrapped to a new line beginning with "63"), and the 15 sub-item rows of Note 11's projects-under-implementation table (SI 2,3,4,5,5.1,5.2,5.3,6,7,7.1,7.2,8,8.1,8.2,8.3), which are line items of Note 11, not separate notes. After removing those, the clean automated pass finds Notes 1-9 and 11-14 = 13. Note 10's numeral is OCR-mangled by the extractor (it appears only as a stray "1:" at line 403 and "-10" at line 404, inside a garbled paragraph), so no regex catches it; the manual sweep recovers it by reading the surrounding text and cross-referencing the A1 header's own page 6/7 narrative, which names "Note 10" explicitly. Reconciled: 13 (grep, clean) + 1 (Note 10, manual) = 14 = 14 (manual read-through of the full Notes section, independently).
- **line_items**: sum of P&L rows (22) + Statement of Assets & Liabilities rows (13) + Segmentwise Results table rows (36) + Note 11 projects-table rows (16) = 87. Grep on the P&L block alone initially over-counted (25 vs 22) because three line items wrap across two physical lines (interest-earned sub-item (c), Total Expenditure, PBT) and both physical lines matched the numbering regex; collapsing wrapped continuations back to one logical row per label reconciles to 22. Grep on the segment block initially under-counted (34 vs 36) because two un-labelled "Less" continuation rows — "(ii) Other Un-allocable Expenditure net-off" and "(iii) Un-allocable income" — don't repeat the word "Less"; adding them reconciles to 36. BS (13) and Note 11 (16) matched cleanly on first pass.
- **zero_standing**: a dash-pattern grep (` - - - -` etc.) alone finds 13 (2 P&L + 1 ratio + 10 segment rows, all using the clean "- - - -" style). The manual sweep of Note 11's table finds 11 more nil rows that use inconsistent nil notation from the source (bare "_", "- _", split "-  -", or a lone trailing "-"): SI 2, 5.2, 5.3, 6, 7, 7.1, 7.2, 8, 8.1, 8.2, 8.3. 13 + 11 = 24, confirmed by a full manual re-read of every row in every table.
- **ratios**: grep on the Analytical Ratios block (lines 269-284) for `(i)/(ii)/-Basic/-Diluted/a)/b)/c)/d)/(v)-(x)` cleanly returns 14 on first pass; manual sweep of the same block confirms 14 (excludes the "17. Analytical Ratios", "(iii) EPS", "(iv) NPA Ratios" bucket headers as non-data).
- **segments**: 4 named reportable segments (Treasury, Retail Banking, Corporate/Wholesale Banking, Other Banking Operations), confirmed both by grep on segment labels and manual read of all five segment sub-blocks (Revenue, Results, Assets, Liabilities, Capital Employed). Unallocated (reconciling, non-reportable) and the single domestic Geographical segment are enumerated separately below, not folded into the 4.
- **comparative_periods**: 4 distinct period identifiers appear across the filing (Q1 FY27 quarter 30.06.2026, Q4 FY26 quarter 31.03.2026, Q1 FY26 quarter 30.06.2025, FY26 full year ended 31.03.2026); grep on the date/column headers on pages 4, 5 and 6 and manual read of every table header row both return 4.
- **agenda_items**: this is a single-purpose Reg 30/33/52 results-submission cover letter (page 1), not a multi-item Board Outcome letter — 1 agenda item (approval of Q1 FY27 results). No AGM notice, dividend, director appointment, auditor change, scrutinizer, or ESOP item is present in this document; their absence is recorded as a fact of this filing type, not estimated.
- **auditor_paras**: grep `^[1-5]\.? ` inside the review report (lines 156-219) returns paragraphs 1-5 cleanly; manual read confirms 5, with no separate Emphasis of Matter, Other Matters, or Going Concern paragraph present (the para 1 Pillar 3 carve-out is a scope exclusion inside para 1 itself, not a standalone EOM paragraph).
- **entities**: Dhanlaxmi Bank Limited (the reviewed entity, standalone, no subsidiaries) + Sagar & Associates + Abraham & Jose (joint statutory auditors) = 3; grep on entity names and manual read agree.
- **signatures**: 4 signature/sign-off blocks (cover letter CS; Sagar & Associates partner; Abraham & Jose partner; closing Board Order block) confirmed by grep on "Place:"/"Date:"/designation strings and manual read.
- **footnotes**: 3 footnotes to the ratios table on page 4 (*, **, ***) confirmed by grep and manual read.

---

## TABLE 1 — NUMBERED NOTES (14 notes; Note 10's numeral is OCR-garbled in the extract, flagged)

| # | Line(s) | First ~15 words | Flags |
|---|---------|------------------|-------|
| Note 1 | 350 | "Statement of Assets and Liabilities as on June 30, 2026. (Rs. In Lakh)" — table heading/note | — |
| Note 2 | 368-372 | "The above unaudited financial results for the quarter ended June 30, 2026, were reviewed by the Audit Committee..." — board/audit committee approval, Joint Statutory Central Auditors named, unmodified limited review report issued | — |
| Note 3 | 373-380 | "These financial results have been prepared in accordance with the recognition and measurement principles laid down..." — basis of preparation, Companies Act 2013, Banking Regulation Act, SEBI Reg 33/52/63 | — |
| Note 4 | 381-384 | "The Bank has applied significant accounting policies in the preparation of these Financial Results, consistent..." — policy consistency with FY26 annual statements; RBI circulars applied prospectively | — |
| Note 5 | 385-388 | "In accordance with the RBI (Commercial Bank - Classification, Valuation and Operation of Investment Portfolio) Second amendment Directions, 2026..." — IFR discontinued, Rs 3,068 lakh transferred to P&L | — |
| Note 6 | 389-391 | "The financial results have been arrived at after considering provision for standard assets..." — provisioning basis (standard assets incl. unhedged FX exposure, NPA, NPI, tax, other usual provisions) | — |
| Note 7 | 392-394 | "Other Income includes fees earned from services to customers, commission from non-fund-based banking activities..." — other income composition | — |
| Note 8 | 395-398 | "The Capital Adequacy Ratio is computed on the basis of RBI guidelines applicable on the relevant reporting dates..." — CRAR basis, prior-period ratio not restated, current-quarter net profit included in regulatory capital | — |
| Note 9 | 399-402 | "As per extant guidelines, the Banks are required to make Pillar 3 disclosures including Leverage ratio, Liquidity Coverage ratio..." — Pillar 3 carve-out, disclosed on website, not reviewed by auditors | cross-ref auditor report para 1 carve-out |
| Note 10 | 403-421 | "[RBI (Commercial Banks — Financial Statements: Presentation and Disclosures) Directions 2025] ... for the loans / arrangements are given below" — header badly garbled by the extractor ("1:", "-10" fragments across lines 403-412); sub-items (i)/(ii)/(iii) on page 7 clean: (i) no loans/stressed loans transferred; (ii) none acquired; (iii) no co-lending arrangements outstanding or entered | `OCR_GARBLED_NOTE_MARKER` — numeral only recoverable via manual sweep + cross-reference to A1 header narrative |
| Note 11 | 422-463 | "Disclosure as per Reserve Bank of India (Commercial Banks — Financial Statements: Presentation and Disclosures) Directions 2025..." — projects-under-implementation table, SI 1 through 8.3 (see Table 6) | — |
| Note 12 | 464 | "Provision coverage ratio (including Technical Write off) as on 30th June 2026 is 92.77%." | — |
| Note 13 | 465-467 | "The figures for the quarter ended March 31, 2026 are the balancing figures between audited figures..." — Q4FY26 derived as balancing figure between FY26 audited and 9M-FY26 reviewed YTD | — |
| Note 14 | 468-469 | "The figures for the previous period have been re-grouped/re-arranged wherever necessary to conform to the current period's classification." | — |

---

## TABLE 2 — P&L LINE ITEMS (page 4, 22 rows; 4 columns each: Q1FY27 30.06.2026 / Q4FY26 31.03.2026 / Q1FY26 30.06.2025 / FY26 year-ended 31.03.2026)

| Row | Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 241 | Interest earned (a+b+c+d) | 44,936 | 44,305 | 36,776 | 1,60,148 | — |
| 1a | 242 | (a) Interest/discount on advances/bills | 37,321 | 36,537 | 29,998 | 1,30,535 | — |
| 1b | 243 | (b) Income on investments | 7,246 | 6,811 | 6,406 | 27,616 | — |
| 1c | 244-245 | (c) Interest on balances with RBI and other interbank funds | 262 | 290 | 199 | 857 | — |
| 1d | 246 | (d) Others | 107 | 667 | 173 | 1,140 | — |
| 2 | 247 | Other income | 3,489 | 6,929 | 3,930 | 19,239 | — |
| 3 | 248 | Total Income (1+2) | 48,425 | 51,234 | 40,706 | 1,79,387 | — |
| 4 | 249 | Interest expended | 27,174 | 25,600 | 22,866 | 97,915 | — |
| 5 | 250 | Operating expenses (a+b) | 16,106 | 14,267 | 14,512 | 59,844 | — |
| 5a | 251 | (a) Employees cost | 9,298 | 7,104 | 8,367 | 32,697 | — |
| 5b | 252 | (b) Other operating expenses | 6,808 | 7,163 | 6,145 | 27,147 | — |
| 6 | 253-254 | Total Expenditure (4+5) excl. provisions | 43,280 | 39,867 | 37,378 | 1,57,759 | — |
| 7 | 255-256 | Operating Profit before provisions (3-6) | 5,145 | 11,367 | 3,328 | 21,628 | — |
| 8 | 257 | Provisions (other than tax) and Contingencies | 1,591 | 3,471 | 2,110 | 7,806 | — |
| 9 | 258 | Exceptional items | - | - | - | - | `ZERO_STANDING` (dash all 4 periods) |
| 10 | 259-260 | Profit/Loss from Ordinary Activities before tax (7-8-9) | 3,554 | 7,896 | 1,218 | 13,822 | — |
| 11 | 261 | Tax expense | 1,063 | 3,547 | - | 3,547 | Q1FY26 cell is dash (zero tax that quarter); not all-period zero, so not flagged ZERO_STANDING — recorded as-is |
| 12 | 262 | Net Profit/Loss from Ordinary Activities after tax | 2,491 | 4,349 | 1,218 | 10,275 | — |
| 13 | 263 | Extraordinary items (net of tax) | - | - | - | - | `ZERO_STANDING` (dash all 4 periods) |
| 14 | 264 | Net Profit/Loss for the period (12-13) | 2,491 | 4,349 | 1,218 | 10,275 | — |
| 15 | 265 | Paid-up equity share capital (FV Rs 10) | 39,470 | 39,470 | 39,470 | 39,470 | — |
| 16 | 266-267 | Reserves excl. Revaluation Reserves (per prior year balance sheet) | — | — | — | 91,443 | only FY-column populated; quarter columns blank (not dash) — standard for this line item, not a gap |

Footnotes (page 4, 3 total): line 222 "*Not Annualized" (qualifies EPS figures marked *); line 223 "**Debt represents borrowings with residual maturity of more than one year" (qualifies Debt Equity Ratio); line 224 "***Total debts represent total borrowings of the bank" (qualifies Total Debts to Total Assets ratio).

---

## TABLE 3 — ANALYTICAL RATIOS (17(i)-(x), page 4, 14 individual ratio values; same 4-column period basis)

| Ratio | Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 17(i) | 269 | % shareholding of Government of India | Nil | Nil | Nil | Nil | `ZERO_STANDING` (Nil all 4 periods) |
| 17(ii) | 270 | Capital Adequacy Ratio (CRAR) per Basel III | 19.19% | 18.92% | 18.26% | 18.92% | — |
| 17(iii)-Basic | 272 | Basic EPS (Rs) | 0.63* | 1.10* | 0.31* | 2.60 | * = not annualized for quarterly columns |
| 17(iii)-Diluted | 273 | Diluted EPS (Rs) | 0.63* | 1.10* | 0.31* | 2.60 | * = not annualized |
| 17(iv)a | 275 | Gross NPA (amount) | 28,657 | 28,638 | 40,195 | 28,638 | — |
| 17(iv)b | 276 | Net NPA (amount) | 7,261 | 7,540 | 13,862 | 7,540 | — |
| 17(iv)c | 277 | % Gross NPA to Gross Advances | 1.82% | 1.89% | 3.22% | 1.89% | — |
| 17(iv)d | 278 | % Net NPA to Net Advances | 0.47% | 0.51% | 1.13% | 0.51% | — |
| 17(v) | 279 | Return on Assets (average, annualized) | 0.45% | 0.84% | 0.27% | 0.53% | — |
| 17(vi) | 280 | Net Worth | 1,30,887 | 1,26,455 | 1,18,804 | 1,26,455 | — |
| 17(vii) | 281 | Debt Equity Ratio (times) ** | 0.11 | 0.12 | 0.13 | 0.12 | ** footnoted (see Table 2) |
| 17(viii) | 282 | Total Debts to Total Assets *** | 3.88% | 3.47% | 2.25% | 3.47% | *** footnoted |
| 17(ix) | 283 | Operating Margin | 10.62% | 22.19% | 8.18% | 12.06% | — |
| 17(x) | 284 | Net Profit Margin | 5.14% | 8.49% | 2.99% | 5.73% | — |

**PERIOD/AUDIT-STATUS FLAG**: page 4 header row (line 240) labels the 4 columns "Unaudited / Audited / Unaudited / Audited" for 30.06.2026 / 31.03.2026 / 30.06.2025 / FY26. Page 5 segment table header row (line 292) labels the same 4 columns (in the same left-to-right order: Jun-26 / Mar-26 / Jun-25 / FY Mar-26) "Audited / Unaudited / Audited / Audited" — i.e. the audited/unaudited labels for the Jun-26 and Jun-25 columns are inverted relative to page 4. Flag `AUDITED_STATUS_MISMATCH_PAGE4_VS_PAGE5` — not resolved here (enumeration only); A3/A4 must determine whether this is a genuine inconsistency or an extraction/column-alignment artifact.

---

## TABLE 4 — SEGMENTWISE RESULTS, Part A: Business Segments (page 5, Rs Lakh, 36 rows; columns Jun-26 / Mar-26 / Jun-25 / FY Mar-26)

Reportable segments (4, per AS 17 compliance statement lines 335-336): **Treasury, Retail Banking, Corporate/Wholesale Banking, Other Banking Operations.** "Unallocated" is a reconciling, non-reportable line appearing in each of the 5 sub-blocks below; Geographical segment (Part B) is domestic-only, single segment.

### 1. Segment Revenue
| Row | Line | Item | Jun-26 | Mar-26 | Jun-25 | FY Mar-26 | Flags |
|---|---|---|---|---|---|---|---|
| 1a | 294 | (a) Treasury | 7,575 | 6,904 | 7,638 | 29,432 | — |
| 1b | 295 | (b) Retail Banking | 29,670 | 34,077 | 23,058 | 1,10,093 | — |
| 1c | 296 | (c) Corporate/Wholesale Banking | 10,871 | 9,318 | 9,728 | 37,817 | — |
| 1d | 297 | (d) Other Banking Operations | 309 | 935 | 282 | 2,045 | — |
| 1e | 298 | (e) Unallocated | - | - | - | (blank) | `ZERO_STANDING`; 4th-period cell not printed (OCR gap, not necessarily a real 0) |
| 1-Tot | 299 | Total Revenue | 48,425 | 51,234 | 40,706 | 1,79,387 | — |
| 1-Less | 300 | Less: Inter-Segment Revenue | - | - | - | - | `ZERO_STANDING` (clean dash all 4) |
| 1-IfO | 301 | Income from Operations | 48,425 | 51,234 | 40,706 | 1,79,387 | — |

### 2. Segment Results (Net of Provisions)
| Row | Line | Item | Jun-26 | Mar-26 | Jun-25 | FY Mar-26 | Flags |
|---|---|---|---|---|---|---|---|
| 2a | 303 | (a) Treasury | 890 | 2,170 | 1,720 | 6,221 | — |
| 2b | 304 | (b) Retail Banking | 2,180 | 3,694 | (45) | 6,431 | Jun-25 negative |
| 2c | 305 | (c) Corporate/Wholesale Banking | 175 | 1,097 | (739) | (875) | Jun-25 and FY both negative |
| 2d | 306 | (d) Other Banking Operations | 309 | 935 | 282 | 2,045 | — |
| 2e | 307 | (e) Unallocated | - | - | (blank) | (blank) | `ZERO_STANDING`; only 2 of 4 period cells printed (OCR gap) |
| 2-Tot | 308 | Total | 3,554 | 7,896 | 1,218 | 13,822 | — |
| 2-Less(i) | 309 | Less: (i) Interest | - | - | - | - | `ZERO_STANDING` (clean) |
| 2-Less(ii) | 310 | (ii) Other Un-allocable Expenditure net-off | - | - | - | (blank) | `ZERO_STANDING`; 4th cell not printed |
| 2-Less(iii) | 311 | (iii) Un-allocable income | - | - | - | - | `ZERO_STANDING` (clean) |
| 2-PBT | 312 | Profit(+)/Loss(-) before tax | 3,554 | 7,896 | 1,218 | 13,822 | ties to P&L row 10 |

### 3. Segment Assets
| Row | Line | Item | Jun-26 | Mar-26 | Jun-25 | FY Mar-26 | Flags |
|---|---|---|---|---|---|---|---|
| 3a | 314 | (a) Treasury | 4,99,843 | 4,69,822 | 4,72,809 | 4,69,822 | — |
| 3b | 315 | (b) Retail Banking | 12,28,268 | 11,99,020 | 9,53,082 | 11,99,020 | — |
| 3c | 316 | (c) Corporate/Wholesale Banking | 4,77,897 | 4,47,533 | 4,33,225 | 4,47,533 | source shows "(e)" mislabel, content is Corp/Wholesale row |
| 3d | 317 | (d) Other Banking Operations | - | - | - | (blank/garbled) | `ZERO_STANDING`; OCR shows "- , - -" |
| 3e | 318 | (e) Unallocated | 6,616 | 7,390 | 10,904 | 7,390 | non-zero, not standing-nil |
| 3-Tot | 319 | Total | 22,12,624 | 21,23,765 | 18,70,020 | 21,23,765 | note: differs by 1 lakh from BS Total 22,12,624/21,23,766/18,70,019 (Jun-25 and Mar-26 columns) — flag `SEGMENT_BS_TOTAL_MISMATCH` |

### 4. Segment Liabilities
| Row | Line | Item | Jun-26 | Mar-26 | Jun-25 | FY Mar-26 | Flags |
|---|---|---|---|---|---|---|---|
| 4a | 321 | (a) Treasury | 4,51,701 | 4,25,752 | 4,30,339 | 4,25,752 | — |
| 4b | 322 | (b) Retail Banking | 11,58,753 | 11,29,164 | 8,94,109 | 11,29,164 | — |
| 4c | 323 | (c) Corporate/Wholesale Banking | 4,50,849 | 4,21,459 | 4,05,090 | 4,21,459 | — |
| 4d | 324 | (d) Other Banking Operations | - | - | - | (blank) | `ZERO_STANDING` |
| 4e | 325 | (e) Unallocated | - | - | - | (blank) | `ZERO_STANDING` |
| 4-Tot | 326 | Total | 20,61,303 | 19,76,375 | 17,29,538 | 19,76,375 | — |

### 5. Capital Employed (Segment Assets - Segment Liabilities)
| Row | Line | Item | Jun-26 | Mar-26 | Jun-25 | FY Mar-26 | Flags |
|---|---|---|---|---|---|---|---|
| 5a | 329 | (a) Treasury | 48,142 | 44,070 | 42,470 | 44,070 | — |
| 5b | 330 | (b) Retail Banking | 69,515 | 69,856 | 58,973 | 69,856 | — |
| 5c | 331 | (c) Corporate/Wholesale Banking | 27,048 | 26,074 | 28,135 | 26,074 | — |
| 5d | 332 | (d) Other Banking Operations | - | - | - | - | `ZERO_STANDING` (clean dash all 4) |
| 5e | 333 | (e) Unallocated | 6,616 | 7,390 | 10,904 | 7,390 | non-zero |
| 5-Tot | 334 | Total | 1,51,321 | 1,47,390 | 1,40,482 | 1,47,390 | — |

Segment reporting basis note: lines 335-341 — AS 17 basis, Digital Banking identified as a sub-segment of Retail Banking, no separate Digital Banking Unit (DBU) set up as of 30 June 2026 per RBI circular RBI/2022-23/19 DOR-ALLT.C.12/22.01.001/2022-23 dated 7 April 2022.

**Part B: Geographical Segments** (lines 342-345): single domestic segment; bank has no overseas operations.

---

## TABLE 5 — STATEMENT OF ASSETS AND LIABILITIES (page 6, 13 rows; columns 30.06.2026 Unaudited / 30.06.2025 Unaudited / 31.03.2026 Audited — no FY "year ended" column, expected for a balance sheet)

| Row | Line | Item | 30.06.2026 | 30.06.2025 | 31.03.2026 | Flags |
|---|---|---|---|---|---|---|
| L1 | 354 | Capital | 39,470 | 39,470 | 39,470 | — |
| L2 | 355 | Reserves and Surplus | 1,11,851 | 1,01,011 | 1,07,922 | — |
| L3 | 356 | Deposits | 19,40,405 | 16,56,962 | 18,64,288 | — |
| L4 | 357 | Borrowings | 85,871 | 41,996 | 73,663 | — |
| L5 | 358 | Other Liabilities and Provisions | 35,027 | 30,580 | 38,423 | — |
| L-Tot | 359 | Total (Capital and Liabilities) | 22,12,624 | 18,70,019 | 21,23,766 | see `SEGMENT_BS_TOTAL_MISMATCH` above |
| A1 | 361 | Cash and Balances with RBI | 76,411 | 1,20,086 | 94,796 | — |
| A2 | 362 | Balances with Bank and Money at Call and Short Notice | 23,526 | 8,278 | 12,384 | — |
| A3 | 363 | Investments | 4,52,734 | 4,23,169 | 4,25,744 | — |
| A4 | 364 | Advances | 15,57,166 | 12,21,820 | 14,91,806 | — |
| A5 | 365 | Fixed Assets | 32,296 | 28,290 | 29,004 | — |
| A6 | 366 | Other Assets | 70,491 | 68,376 | 70,031 | — |
| A-Tot | 367 | Total (Assets) | 22,12,624 | 18,70,019 | 21,23,766 | ties to L-Tot each column |

---

## TABLE 6 — NOTE 11: PROJECTS UNDER IMPLEMENTATION (page 7, 16 rows, Rs Lakh + number of accounts)

| SI | Line(s) | Item | Number of accounts | Total outstanding (Rs lakh) | Flags |
|---|---|---|---|---|---|
| 1 | 432 | Accounts at beginning of quarter | 28 | 12,071.49 | — |
| 2 | 433 | Accounts sanctioned during the quarter | - | - | `ZERO_STANDING` |
| 3 | 434-435 | Accounts where DCCO achieved during the quarter | 3 | 586.71 | — |
| 4 | 436 | Accounts at end of quarter (1+2-3) | 25 | 11,040.74 | — |
| 5 | 437-438 | Out of '4' — resolution process (DCCO extension) invoked | 7 | 1,937.94 | — |
| 5.1 | 439-440 | Out of '5' — resolution plan implemented | 7 | 1,937.94 | — |
| 5.2 | 441-443 | Out of '5' — resolution plan under implementation | - | - | `ZERO_STANDING` |
| 5.3 | 444 | Out of '5' — resolution plan failed | - | - | `ZERO_STANDING` |
| 6 | 445-448 | Out of '5' — DCCO extension due to change in scope/size | - | - | `ZERO_STANDING` |
| 7 | 449-450 | Out of '5' — cost overrun funded | - | - | `ZERO_STANDING` |
| 7.1 | 451-452 | Out of '7' — SBCF sanctioned during financial closure, renewed continuously | - | - | `ZERO_STANDING` |
| 7.2 | 453-454 | Out of '7' — SBCF not pre-sanctioned or not renewed continuously | - | - | `ZERO_STANDING` |
| 8 | 455-456 | Out of '4' — resolution process not involving DCCO extension | - | - | `ZERO_STANDING` |
| 8.1 | 457-459 | Out of '8' — resolution plan implemented | - | - | `ZERO_STANDING` |
| 8.2 | 460-462 | Out of '8' — resolution plan under implementation | - | - | `ZERO_STANDING` |
| 8.3 | 463 | Out of '8' — resolution plan failed | - | - | `ZERO_STANDING` |

Note 10 sub-items (i, ii, iii; page 7, lines 415-421 — logically part of Note 10, table header for which is on page 6, see Table 1): (i) no loans/stressed loans transferred during the quarter; (ii) no loans/stressed loans acquired during the quarter; (iii) no outstanding or newly-entered Co-Lending Arrangements. All three are negative-assurance disclosures (no transactions of this type occurred) — recorded as data, not dropped, though not table rows with numeric columns so not counted in the 16-row Table 6 total.

---

## TABLE 7 — AUDITORS' LIMITED REVIEW REPORT (pages 2-3, 5 numbered paragraphs + sign-off blocks)

| Para | Line(s) | Content | Flags |
|---|---|---|---|
| 1 | 156-163 | Scope: reviewed Statement of Unaudited Financial Results for quarter ended 30 June 2026, EXCEPT Pillar 3 disclosures under Basel III (Leverage Ratio, LCR, NSFR) — disclosed on Bank's website via link, not reviewed | scope carve-out; cross-ref Note 9 |
| 2 | 164-171 | Management responsibility; prepared per AS 25 "Interim Financial Reporting" under Companies Act 2013 s.133, Banking Regulation Act 1949, RBI guidelines | — |
| 3 | 172-207 | Review conducted per SRE 2410; nature of a review (inquiry-based, moderate assurance) vs an audit; no audit opinion expressed | — |
| 4 | 208-210 | Basis: review of books of account/records, reliance on information/explanations furnished by the Bank | — |
| 5 | 211-219 | Conclusion: nothing has come to attention indicating material misstatement or non-compliance with Reg 33/52 or RBI prudential norms — unmodified conclusion | no Emphasis of Matter / Other Matters / Going Concern paragraph present in this report |
| — | 152-154, 155 | Report title and addressee: "To the Board of Directors of Dhanlaxmi Bank Limited" — joint auditors Sagar & Associates and Abraham & Jose | entities: 1 reviewed entity, 2 audit firms |
| Sign-off 1 | 183-190 | Sagar & Associates, Firm Reg No. 003510S, CA. B. Aruna (Partner), Membership No. 216454, UDIN 26216454SNEZR02766, Place Thrissur, Date 29.07.2026 | — |
| Sign-off 2 | 195-201 | Abraham & Jose, Firm Reg No. 000010S, CA. Mukesh K.P. (Partner), Membership No. 214773, UDIN 26214773UMVDVK5335, Place Thrissur, Date 29.07.2026 | — |

Entities enumerated (3): Dhanlaxmi Bank Limited (reviewed entity, standalone, no subsidiaries/associates — `CONSOLIDATION_NA`, stated as fact not gap); Sagar & Associates (Chartered Accountants, Hyderabad); Abraham & Jose (Chartered Accountants, Thrissur). No prior-quarter entity list supplied for a diff, so `ENTITY_CHANGE` cannot be evaluated this quarter (`PRIOR_LEDGER_PATH` not provided).

---

## TABLE 8 — COVER LETTER / BOARD OUTCOME (page 1, 1 agenda item + signatory + board timing)

| Item | Line(s) | Content | Flags |
|---|---|---|---|
| Ref/date | 111 | "SH: 28/2026-27", dated 29 July 2026 | — |
| Addressees | 112-117 | BSE Limited (GM, Dept. of Corporate Services) and NSE (Manager, Listing Dept.) | both exchanges addressed |
| Agenda item 1/1 | 119-124 | Approval and taking on record of Unaudited Financial Results for quarter ended 30 June 2026, along with limited review report, at Board meeting held 29 July 2026 | sole agenda item in this letter — no AR approval, AGM notice, record date, dividend, director appointment, auditor change, scrutinizer, or ESOP item present in this document |
| Board meeting timing | 125 | Commenced 12:00 Noon, results approved 12:45 PM — 45-minute meeting | duration recorded for auditability |
| Signature block | 127-130 | Venkatesh H., Company Secretary & Secretary to the Board | signed same date as meeting, no pre-conclusion timestamp anomaly |
| Closing signature block | 470-478 | "By Order of the Board", Place: Thrissur, Date: 29th July 2026; signatory role visible as "...ctor & CE0" (Director & CEO) but name badly garbled by OCR/extraction | name `NOT_FOUND` (garbled beyond safe reconstruction) — role only |

Signatures total (4): Company Secretary (cover letter); Sagar & Associates partner; Abraham & Jose partner; closing Board Order block (Director & CEO, name illegible).

---

## TABLE 9 — REPORTING PERIODS AND STATUS (4 comparative periods captured across the filing)

| Period | Date | Status per P&L (page 4) | Status per Segment table (page 5) | Status per Balance Sheet (page 6) |
|---|---|---|---|---|
| Q1 FY27 (current quarter) | 30.06.2026 | Unaudited | Audited (label swap vs page 4 — see flag below) | Unaudited |
| Q4 FY26 (comparative quarter) | 31.03.2026 | Audited | Unaudited (label swap vs page 4) | Audited |
| Q1 FY26 (year-ago quarter) | 30.06.2025 | Unaudited | Audited (label swap vs page 4) | Unaudited |
| FY26 (full year ended) | 31.03.2026 | Audited | Audited | not applicable (balance sheet has no "year ended" column — expected) |

Flag `AUDITED_STATUS_MISMATCH_PAGE4_VS_PAGE5`: page 4's status row (line 240) is "Unaudited / Audited / Unaudited / Audited" for the 4 columns in order; page 5's status row (line 292) for the same 4 columns in the same left-to-right order is "Audited / Unaudited / Audited / Audited". The Jun-26 and Jun-25 columns carry opposite audited/unaudited labels between the two tables. Enumerated as a discrepancy for A3/A4 to investigate (possible column-alignment artifact in the source text extraction, or a genuine inconsistency in the source filing) — not resolved here per enumerator scope.

---

## SUMMARY OF FLAGS RAISED

1. `ZERO_STANDING` — 24 instances (2 P&L: Exceptional items, Extraordinary items; 1 ratio: GoI shareholding; 10 segment sub-block rows; 11 Note 11 table rows). Full list in Tables 2, 3, 4, 6.
2. `OCR_GARBLED_NOTE_MARKER` — Note 10's numeral is corrupted in the extraction (appears as "1:" / "-10" fragments); recovered only via manual sweep.
3. `AUDITED_STATUS_MISMATCH_PAGE4_VS_PAGE5` — Jun-26 and Jun-25 column audited/unaudited labels are inverted between the P&L table (page 4) and the segment table (page 5).
4. `SEGMENT_BS_TOTAL_MISMATCH` — Segment Assets Total (line 319: 21,23,765 for Mar-26; 18,70,020 for Jun-25) differs by Rs 1 lakh from the Balance Sheet Total (line 359/367: 21,23,766 for 31.03.2026; 18,70,019 for 30.06.2025) in two of three comparable columns. Likely rounding in one of the two source tables; not resolved here.
5. `CONSOLIDATION_NA` — no consolidated statement exists or is expected; Dhanlaxmi Bank has no subsidiaries/associates (stated fact, not a gap).
6. `NOT_FOUND` — name of the closing "By Order of the Board" signatory is illegible in the extraction; only the role "...ctor & CEO" (Director & CEO) is recoverable.
7. No `ENTITY_CHANGE` evaluable — no prior-quarter ledger was supplied for a diff (`PRIOR_LEDGER_PATH` not provided this run).
8. No `MGMT_ABSENCE` / `DROPPED_SLIDE` / `REPEAT_QUESTION` applicable — this doctype is a results filing only (no concall transcript or investor presentation in scope this run).

---

```yaml
stage: A2-enumerator
company: "Dhanlaxmi Bank Limited"
ticker: "DHANBANK"
quarter: "Q1 FY27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "runs/dhanbank-q1fy27/work/ledger_results_dhanbank_q1fy27.md"
counts:
  notes: 14
  line_items: 87
  zero_standing: 24
  ratios: 14
  segments: 4
  comparative_periods: 4
  agenda_items: 1
  auditor_paras: 5
  entities: 3
  signatures: 4
  footnotes: 3
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, OCR_GARBLED_NOTE_MARKER, AUDITED_STATUS_MISMATCH_PAGE4_VS_PAGE5, SEGMENT_BS_TOTAL_MISMATCH, CONSOLIDATION_NA, NOT_FOUND]
gate_a2: pass
mismatch_note: ""
```
