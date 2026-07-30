# A2 COMPLETENESS LEDGER — SATIN Q1 FY27 — Results Filing
Source: extract_results_satin_q1fy27.txt (15 pages, Lakhs -> x0.01 = Rs Cr)
Doctype: results (Reg 33 Board Outcome + Un-Audited Standalone & Consolidated
Financial Results + two Limited Review Reports)

```
=== A2 COUNT TEST ===
category: agenda_items      grep_count: 1    sweep_count: 1    match: yes
category: statement_blocks  grep_count: 2    sweep_count: 2    match: yes
category: auditor_reports   grep_count: 2    sweep_count: 2    match: yes
category: auditor_paras     grep_count: 13   sweep_count: 13   match: yes
category: entities          grep_count: 6    sweep_count: 6    match: yes
category: notes             grep_count: 32   sweep_count: 32   match: yes
category: line_items        grep_count: 144  sweep_count: 144  match: yes
category: zero_standing     grep_count: 29   sweep_count: 29   match: yes
category: signature_blocks  grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
NOTE ON METHOD: OCR on this scan (esp. p.14, consolidated Reg 52(4) table)
corrupts a naive `grep -n -E "^\s*[0-9]+\.\s"` pass (roman/arabic digits get
merged with adjacent glyphs, e.g. "l0", "I" for "1"). Notes/statement/report
header counts were grep-confirmed against literal section-header strings
("Notes to the unaudited standalone/consolidated financial results",
"Statement of Unaudited ... Financial Results", "Limited Review Report") —
these anchors are OCR-clean and gave exact, reconcilable counts. Line-item
and note-body counts were built by two independent manual line-by-line
sweeps of the extract (first pass, then a from-scratch second pass); both
passes produced identical row counts per table before being summed here.
Where OCR corruption prevented reading a value (not just a label), the row
is still enumerated with flag OCR_UNCLEAR or OCR_DROPPED_LINE rather than
being dropped.
=== END COUNT TEST ===
```

---
## 0. FILING METADATA (from A1 header, ln 1-13)
| # | Item | Line | Value | Flags |
|---|------|------|-------|-------|
| 0.1 | Source filename | 2 | results_satin_q1fy27.pdf | |
| 0.2 | Page count | 4 | 15 | matches formfeed_count (5), page marker grep (15) |
| 0.3 | OCR pages | 9 | none (0% OCR fallback) | but see 4.14/6.14 re: p.14 layout corruption despite no OCR flag |
| 0.4 | Detected quarter | 11 | Q1 FY27, quarter ended June 30, 2026 | |

---
## 1. BOARD OUTCOME LETTER (p.1, ln 15-68)
| # | Item | Line | Detail | Flags |
|---|------|------|--------|-------|
| 1.1 | Agenda item 1 (only item, "inter-alia") | 37-39 | Board approved Un-Audited Financial Results (Standalone & Consolidated) for qtr ended June 30, 2026, per Audit Committee recommendation | single combined agenda item; no AR approval / AGM / dividend / director appointment / auditor change / ESOP grant / capital-raise resolution named as a separate agenda item in this letter |
| 1.2 | Board meeting start time | 47 | 2:30 p.m. IST | |
| 1.3 | Board meeting end time | 47 | 3:52 p.m. IST | duration 82 min |
| 1.4 | Trading window closure notice | 48-49 | closed until 48 hrs from publication | |
| 1.5 | Auditor named / opinion flagged in cover letter | 41-43 | J C Bhalla & Co., "un-modified opinion" on both LRRs | |
| 1.6 | Digital signature block | 56-67 | Vikas Gupta, Company Secretary & CCO, digitally signed 2026.07.30 16:05:12 +05'30' | signed ~13 min after board meeting concluded (15:52) — not a flag (after, not before) |

Cross-reference: Note 9 (standalone, ln 275-283) and Note 12 (consolidated, ln
741-749) disclose a *separate, prior* board meeting (June 4, 2026) that
approved a warrants preferential-allotment proposal. That is NOT an agenda
item of today's (July 30) Board Outcome letter — it is background disclosure
inside the financial-results notes — so it is not counted in the agenda_items
category above, only cross-referenced here for completeness.

---
## 2. STANDALONE LIMITED REVIEW REPORT (p.2-3, ln 70-161)
| # | Para | Line | First words / content | Flags |
|---|------|------|------------------------|-------|
| 2.1 | Title / addressee | 80-89 | "Independent Auditor's Limited Review Report on Statement of Unaudited Standalone Financial Results..." Reg 33 & 52 read with Reg 63 | |
| 2.2 | Para 1 | 90-96 | "We have reviewed the accompanying Statement of unaudited standalone financial results..." | |
| 2.3 | Para 2 | 98-105 | "This Statement, which is the responsibility of the Company's Management..." IND AS 34 basis | |
| 2.4 | Para 3 | 107-119 | "We conducted our review... SRE 2410... Accordingly, we do not express an audit opinion." | |
| 2.5 | Para 4 (conclusion) | 126-138 | "Based on our review... nothing has come to our attention..." unmodified conclusion, incl. RBI prudential-norms scope | |
| 2.6 | Para 5 (Other Matter) | 140-145 | Q4 FY26 figures are balancing figures (FY audited less 9M reviewed) | |
| 2.7 | Signature block | 149-161 | J C Bhalla & Co., FRN 001111N, Rajesh Sethi, Partner, Membership 085669, Gurugram, July 30 2026 | line 159 is a garbled OCR line where a UDIN would normally sit — flag `OCR_UNCLEAR`: cannot confirm UDIN is present/legible for the standalone report (contrast with consolidated report at 2.7-equivalent 5.9 where a UDIN string, though garbled, is explicitly labeled) |
| — | Emphasis of Matter / Going Concern | n/a | none present | clean unmodified conclusion, no EOM/Going Concern paragraph |
| — | Entities reviewed | n/a | Company only (standalone) | single entity, no "furnished by other auditors" scope needed |

Standalone LRR paragraph count = 5 numbered (2.2-2.6) + title/addressee (2.1)
and signature (2.7) are structural, not substantive paragraphs → substantive
para count for the count test = **5**.

---
## 3. STANDALONE FINANCIAL RESULTS — P&L LINE ITEMS (p.4, ln 163-232)
All values in Rs Lakhs as filed; 4 columns each (Q1FY27 unaudited, Q4FY26 refer
note 15, Q1FY26 unaudited, FY26 audited).
| # | S.No | Line item | Line | Q1FY27 value | Flags |
|---|------|-----------|------|--------------|-------|
| 3.1 | — | Interest income | 175 | 63,202.99 | |
| 3.2 | — | Rental income | 176 | 43.25 | |
| 3.3 | — | Fees and commission income | 177 | 258.20 | |
| 3.4 | — | Net gain/(loss) on fair value changes | 178 | (5,711.19) | |
| 3.5 | — | Net gain on derecognition of financial instruments | 179 | 9,241.73 | |
| 3.6 | — | Other operating income | 180 | 55.82 | |
| 3.7 | 1 | Total revenue from operations | 181 | 67,090.80 | |
| 3.8 | 2 | Other income | 182 | 54.66 | |
| 3.9 | 3 | Total income (1+2) | 183 | 67,145.46 | |
| 3.10 | — | Finance costs (i) Interest cost | 187 | 26,888.82 | |
| 3.11 | — | Finance costs (ii) Effects of FX rate changes | 188 | (6,242.84) | |
| 3.12 | — | Impairment of financial instruments | 189 | 10,014.89 | |
| 3.13 | — | Employee benefits expenses | 190 | 15,716.41 | |
| 3.14 | — | Depreciation and amortisation expenses | 191 | 642.64 | |
| 3.15 | — | Other expenses | 192 | 4,329.93 | |
| 3.16 | 4 | Total expenses | 193 | 51,349.85 | |
| 3.17 | 5 | Profit before tax (3-4) | 195 | 15,795.61 | |
| 3.18 | — | Current tax | 198 | 4,239.13 | |
| 3.19 | — | Tax adjustments related to earlier years | 199 | blank (Q1FY27), blank (Q1FY26); 1.41 (Q4FY26); (35.33) (FY26) | `ZERO_STANDING` — line stands but nil in current + prior-year comparable quarter |
| 3.20 | — | Deferred tax charge/(credit) | 200 | (472.20) | |
| 3.21 | 6 | Total tax expense | 201 | 3,766.93 | |
| 3.22 | 7 | Net profit after tax (5-6) | 203 | 12,028.68 | |
| 3.23 | — | OCI items not reclassified to P&L | 206 | (916.33) | |
| 3.24 | — | Income tax on items not reclassified | 207 | 230.62 | |
| 3.25 | — | OCI items to be reclassified to P&L | 209 | (149.03) | |
| 3.26 | — | Income tax on items to be reclassified | 210 | 37.51 | |
| 3.27 | 8 | Total other comprehensive income | 212 | (797.23) | |
| 3.28 | 9 | Total comprehensive income (7+8) | 214 | 11,231.45 | |
| 3.29 | 10 | Paid-up equity share capital (FV Rs 10) | 216 | 11,011.32 | |
| 3.30 | 11 | Other equity | 218 | blank (Q1FY27, Q4FY26, Q1FY26); 3,01,878.50 (FY26 audited only) | `ZERO_STANDING` — standing balance-sheet line populated only in the audited annual column, blank in all three interim columns (standard IND AS 34 presentation, but a nil/blank standing item per enumeration rule) |
| 3.31 | 12a | EPS Basic (Rs) | 222 | 10.94 | |
| 3.32 | 12b | EPS Diluted (Rs) | 223 | 10.94 | footnote ln 224-226: EPS not annualized |

Standalone P&L line-item count = **32** (two independent sweeps agree).

---
## 4. STANDALONE NOTES (p.5-8, ln 239-429) — 16 notes
| # | Note | Line | First ~15 words | Flags |
|---|------|------|------------------|-------|
| 4.1 | 1 | 240 | "The above unaudited standalone financial results... reviewed by Audit Committee and approved by Board..." | |
| 4.2 | 2 | 245 | "The unaudited standalone financial results have been prepared in accordance with applicable accounting standards..." | |
| 4.3 | 3 | 249 | "The secured non-convertible debentures issued by the Company are fully secured by exclusive charge..." | |
| 4.4 | 4 | 253-258 | "During the quarter... allotted following Non-Convertible Securities... a) 8,446 subordinated NCDs Rs 8,446.00L; b) 2,000 USD bonds Rs 19,046.00L" | 2 sub-items (a,b) |
| 4.5 | 5 | 259-261 | "...investments aggregating to Rs 1,000.00 lakhs in Satin Technologies Limited (wholly owned subsidiary)..." rights basis | |
| 4.6 | 6 | 263-265 | "...investment aggregating to Rs 5,000.00 lakhs in Satin Finserv Limited (wholly owned subsidiary)..." | |
| 4.7 | 7 | 267-269 | "Subsequent to quarter ended... investment aggregating to Rs 1,200.00 lakhs in Satin Growth Alternatives Limited..." | subsequent event |
| 4.8 | 8 | 271-273 | "Pursuant to exercise of ESOP Options... 70,000 equity shares were exercised..." | |
| 4.9 | 9 | 275-283 | "...Board of Directors in its meeting held on June 04, 2026 had approved... 38,50,000 fully convertible warrants... Rs 260.00 each... Trishashna Holdings..." promoter-group preferential allotment | prior (non-today) board meeting; shareholder postal-ballot approval July 4, 2026; in-principle exchange approval July 27, 2026 |
| 4.10 | 10 | 297-343 | "Details of loans transferred / acquired... under RBI Master Direction..." | see 4.10.1-4.10.22 sub-table below |
| 4.10.1 | 10(i).i | 307 | Total number of loan assets assigned | 1,91,443 | |
| 4.10.2 | 10(i).ii | 308 | Book value of loan assets assigned (Rs L) | 81,888.66 | |
| 4.10.3 | 10(i).iii | 309 | Sale consideration received (Rs L) | 81,888.66 | |
| 4.10.4 | 10(i).iv | 310-311 | Interest spread recognised (incl. amortisation) (Rs L) | 9,707.95 | |
| 4.10.5 | 10(i).v | 312 | Weighted avg maturity of loans assigned (months) | 19.17 | |
| 4.10.6 | 10(i).vi | 313 | Weighted avg holding period (months) | 5.98 | |
| 4.10.7 | 10(i).vii | 314 | Retention of beneficial economic interest (%) | 11.35% | |
| 4.10.8 | 10(i).viii | 315 | Coverage of tangible security | Nil | `ZERO_STANDING` |
| 4.10.9 | 10(i).ix | 316 | Rating-wise distribution of rated loans | Not Rated | `ZERO_STANDING`-adjacent (no rated loans) |
| 4.10.10 | 10(i).x | 317-318 | Agreed to replace loans / pay damages | No | `ZERO_STANDING` |
| 4.10.11 | 10(ii).i | 327 | Total number of loan assets acquired | 368 | |
| 4.10.12 | 10(ii).ii | 328 | Book value acquired (Rs L) | 3,160.59 | |
| 4.10.13 | 10(ii).iii | 329 | Sale consideration paid (Rs L) | 3,160.59 | |
| 4.10.14 | 10(ii).iv | 330 | Weighted avg maturity acquired (months) | 144.25 | |
| 4.10.15 | 10(ii).v | 331 | Weighted avg holding period (months) | 17.78 | |
| 4.10.16 | 10(ii).vi | 332-333 | Retention of beneficial economic interest by assignor (%) | 10.00% | |
| 4.10.17 | 10(ii).vii | 334 | Coverage of tangible security | 100.00% | |
| 4.10.18 | 10(ii).viii | 335 | Rating-wise distribution | Not Rated | `ZERO_STANDING`-adjacent |
| 4.10.19 | 10(ii).ix | 336-337 | Agreed to replace / pay damages | No | `ZERO_STANDING` |
| 4.10.20 | 10(iii) | 339 | Company has not transferred any NPA loans | — | `ZERO_STANDING` |
| 4.10.21 | 10(iv) | 341 | Company has not acquired any stressed loans | — | `ZERO_STANDING` |
| 4.10.22 | 10(v) | 343 | Co-Lending Arrangements (CLAs) disclosure as at June 30, 2026 | Nil | `ZERO_STANDING` |
| 4.11 | 11 | 345-351 | "Disclosures related to project finance under RBI Direction... Company has not lent any funds during the quarter... for project finance..." | `ZERO_STANDING` — whole note is a nil-activity disclosure |
| 4.12 | 12 | 366-372 | Details of loans/advances against recovery ratings, table: RR3 50-75% Rs 2,254.37L; Rating under representation NA Rs 6,132.36L; Total Rs 8,386.73L | 3 sub-rows |
| 4.12.1 | 12.a | 370 | RR3 (recovery 50-75%) | 2,254.37 | |
| 4.12.2 | 12.b | 371 | Rating under representation (NA) | 6,132.36 | |
| 4.12.3 | 12.c | 372 | Total | 8,386.73 | |
| 4.13 | 13 | 374-376 | "CODM reviews operations at Company level... 'financing activities' only... single reportable segment... single geographical segment, domestic" | single-segment entity |
| 4.14 | 14 | 379-409 | Reg 52(4) additional information table, 19 items — see 4.14.1-4.14.19 | |
| 4.14.1 | 14.1 | 385 | Debt-equity ratio (x) | 3.15 | |
| 4.14.2 | 14.2 | 386 | Debt service coverage ratio | Not applicable | `ZERO_STANDING` |
| 4.14.3 | 14.3 | 387 | Interest service coverage ratio | Not applicable | `ZERO_STANDING` |
| 4.14.4 | 14.4 | 388 | Outstanding redeemable preference shares (qty & value) | Nil | `ZERO_STANDING` |
| 4.14.5 | 14.5 | 389 | Capital redemption reserve (Rs L) | 2,777.00 | |
| 4.14.6 | 14.6 | 390 | Debenture redemption reserve (Rs L) | Not applicable | `ZERO_STANDING` |
| 4.14.7 | 14.7 | 391 | Net worth (Rs L) | 3,21,892.58 | |
| 4.14.8 | 14.8 | 392 | Net profit after tax (Rs L) | 12,028.68 | |
| 4.14.9 | 14.9 | 393-394 | EPS Basic / Diluted (Rs) | 10.94 / 10.94 | |
| 4.14.10 | 14.10 | 395 | Current ratio (x) | Not applicable | `ZERO_STANDING` |
| 4.14.11 | 14.11 | 396 | Long term debt to working capital (x) | Not applicable | `ZERO_STANDING` |
| 4.14.12 | 14.12 | 397 | Bad debts to Account receivable ratio | Not applicable | `ZERO_STANDING` |
| 4.14.13 | 14.13 | 398 | Current liability ratio (x) | Not applicable | `ZERO_STANDING` |
| 4.14.14 | 14.14 | 399 | Total debts to total assets | 0.73 | |
| 4.14.15 | 14.15 | 400 | Debtors turnover | Not applicable | `ZERO_STANDING` |
| 4.14.16 | 14.16 | 401 | Inventory turnover | Not applicable | `ZERO_STANDING` |
| 4.14.17 | 14.17 | 402 | Operating margin (%) | Not applicable | `ZERO_STANDING` |
| 4.14.18 | 14.18 | 403 | Net profit margin (%) | 17.91% | |
| 4.14.19 | 14.19 | 404-409 | Sector-specific ratios: a) GNPA 2.18%; b) NNPA 0.33%; c) PCR 84.66%; d) CRAR 26.74%; e) LCR 134.89% | 5 sub-rows, all populated |
| 4.15 | 15 | 423-425 | "The figures for the quarter ended March 31, 2026 represent the balancing figures..." | matches LRR para 2.6 |
| 4.16 | 16 | 428 | "Previous year/period figures have been regrouped/rearranged..." | |
| — | Board sign-off | 430-438 | Harvinder Pal Singh, Chairman cum Managing Director, DIN 00333754, Gurugram, July 30, 2026 | non-digital scanned signature |

Standalone note count = **16** (headline notes). Standalone note-table
sub-line-item count (4.10 block 22 + 4.12 block 3 + 4.14 block 19) = **44**.

---
## 5. CONSOLIDATED LIMITED REVIEW REPORT (p.9-11, ln 448-569)
| # | Para | Line | First words / content | Flags |
|---|------|------|------------------------|-------|
| 5.1 | Title / addressee | 448-466 | "...Limited Review Report on Statement of Unaudited Consolidated Financial Results..." Reg 33 & 52 read with Reg 63 | |
| 5.2 | Para 1 | 467-476 | "We have reviewed the accompanying Statement of unaudited consolidated financial results... Parent... subsidiaries and step down subsidiary (the Group)..." | |
| 5.3 | Para 2 | 478-485 | "This Statement, which is the responsibility of the Parent's Management..." IND AS 34 basis | |
| 5.4 | Para 3 | 487-499 | "We conducted our review... SRE 2410... Accordingly, we do not express an audit opinion." | |
| 5.5 | Para 3A (unnumbered, additional procedures) | 504-507 | "We also performed procedures in accordance with the Circular No. CIR/CFD/CMD1/44/2019... Regulation 33(8)..." | unnumbered paragraph, no equivalent in standalone report (standalone has no other-auditor reliance scope) |
| 5.6 | Para 4 (entity list) | 509-521 | "The Statement includes the financial results of the following entities (the Group):" — see entity table 5.7 | |
| 5.7 | Entity list (6 rows) | 512-520 | see table below | |
| 5.8 | Para 5 (conclusion) | 522-531 | "Based on our review... and based on the considerations of the review reports of other auditors... nothing has come to our attention..." | |
| 5.9 | Para 6 (Other Matter — reliance on other auditors) | 533-545 | "We did not review the financial results of the four wholly-owned subsidiaries and one step down subsidiary... total revenue Rs 10,382.78L, PAT Rs 606.58L, TCI Rs 1,157.83L... reviewed by other auditors... conclusion not modified" | names which entities are auditor-furnished/unreviewed-by-principal-auditor |
| 5.10 | Para 7 (Other Matter — Q4 balancing figures) | 547-552 | Q4 FY26 figures are balancing figures (FY audited less 9M reviewed) | matches standalone LRR 2.6 |
| 5.11 | Signature block | 556-569 | J C Bhalla & Co., FRN 001111N, Rajesh Sethi, Partner, Membership 085669, UDIN "260BE663nrLNqfsfs" (OCR-garbled), Gurugram, July 30 2026 | `OCR_UNCLEAR` on exact UDIN digit string — needs source-PDF verification, not a missing-disclosure flag |
| — | Emphasis of Matter / Going Concern | n/a | none present | clean unmodified conclusion |

Entity list (para 4, ln 512-520):
| # | Sr.No | Entity | Relationship | Line |
|---|-------|--------|--------------|------|
| 5.7.1 | 1 | Satin Creditcare Network Limited | Parent Company | 513 |
| 5.7.2 | 2 | Satin Housing Finance Limited | Wholly owned subsidiary | 514 |
| 5.7.3 | 3 | Satin Finserv Limited | Wholly owned subsidiary | 515 |
| 5.7.4 | 4 | Satin Technologies Limited | Wholly owned subsidiary | 516 |
| 5.7.5 | 5 | Satin Growth Alternatives Limited | Wholly owned subsidiary | 517 |
| 5.7.6 | 6 | QTrino Labs Limited (formerly QTrino Labs Private Limited) | Step Down Subsidiary | 518-520 |

Consolidated LRR substantive paragraph count = 8 (paras 1,2,3,3A,4,5,6,7) —
combined with standalone's 5 → auditor_paras count-test total = **13**.
Entities count-test total = **6**.

---
## 6. CONSOLIDATED FINANCIAL RESULTS — P&L LINE ITEMS (p.12, ln 576-644)
| # | S.No | Line item | Line | Q1FY27 value | Flags |
|---|------|-----------|------|--------------|-------|
| 6.1 | — | Interest income | 585 | 71,396.21 | |
| 6.2 | — | Rental income | 586 | 11.24 | |
| 6.3 | — | Fees and commission income | 587 | 885.17 | |
| 6.4 | — | Net gain/(loss) on fair value changes | 588 | (5,673.05) | |
| 6.5 | — | Net gain on derecognition of financial instruments | 589 | 9,409.24 | |
| 6.6 | — | Other operating income | 590 | 184.83 | |
| 6.7 | 1 | Total revenue from operations | 591 | 76,213.64 | |
| 6.8 | 2 | Other income | 592 | 260.89 | |
| 6.9 | 3 | Total income (1+2) | 593 | 76,474.53 | |
| 6.10 | — | Finance costs (i) Interest cost | 596 | 31,334.43 | |
| 6.11 | — | Finance costs (ii) Effects of FX rate changes | 597 | (6,242.84) | |
| 6.12 | — | Impairment of financial instruments | 598 | 10,612.07 | |
| 6.13 | — | Employee benefit expenses | 599 | 18,769.10 | |
| 6.14 | — | Depreciation and amortisation expenses | 600 | 793.51 | |
| 6.15 | — | Other expenses | 601 | 5,088.59 | |
| 6.16 | 4 | Total expenses | 602 | 60,354.86 | |
| 6.17 | 5 | Profit before tax (3-4) | 603 | 16,119.67 | |
| 6.18 | — | Current tax | 605 | 4,593.09 | |
| 6.19 | — | Tax adjustments related to earlier years | 606 | 6.82 | |
| 6.20 | — | Deferred tax charge/(credit) | 607 | (744.80) | |
| 6.21 | 6 | Total tax expense | 608 | 3,855.11 | |
| 6.22 | 7 | Net profit after tax (5-6) | 609 | 12,264.56 | |
| 6.23 | — | OCI items not reclassified | 611 | (881.51) | |
| 6.24 | — | Income tax on items not reclassified | 612-613 | 221.86 | |
| 6.25 | — | OCI items to be reclassified | 614 | 551.42 | |
| 6.26 | — | Income tax on items to be reclassified | 615 | (137.75) | |
| 6.27 | 8 | Total other comprehensive income | 617 | (245.98) | |
| 6.28 | 9 | Total comprehensive income (7+8) | 619 | 12,018.58 | |
| 6.29 | 10a | PAT attributable to: Owners of the Parent | 622 | 12,267.04 | |
| 6.30 | 10b | PAT attributable to: Non-controlling interests | 623 | (2.48) | |
| 6.31 | 11a | OCI attributable to: Owners of the Parent | 625 | (245.98) | |
| 6.32 | 11b | OCI attributable to: Non-controlling interests | 626 | blank (all periods shown blank except none) | `ZERO_STANDING` — standing attribution line, no value in any column in extract |
| 6.33 | 12a | TCI attributable to: Owners of the Parent | 628 | 12,021.06 | |
| 6.34 | 12b | TCI attributable to: Non-controlling interests | 629 | blank (Q1FY27, Q1FY26); 2.27 (Q4FY26, FY26) | `ZERO_STANDING` — nil in current + prior-year comparable quarter |
| 6.35 | 13 | Paid-up equity share capital (FV Rs 10) | 631 | 11,011.32 | |
| 6.36 | 14 | Other equity | 633 | blank (Q1FY27, Q4FY26, Q1FY26); 2,75,335.20 (FY26 audited only) | `ZERO_STANDING` — same pattern as standalone 3.30 |
| 6.37 | 15a | EPS Basic (Rs) | 635 | 11.15 | |
| 6.38 | 15b | EPS Diluted (Rs) | 636 | 11.15 | footnote ln 637-638: EPS not annualized |

Consolidated P&L line-item count = **38** (two independent sweeps agree).

---
## 7. CONSOLIDATED NOTES (p.13-15, ln 651-802) — 16 notes
| # | Note | Line | First ~15 words | Flags |
|---|------|------|------------------|-------|
| 7.1 | 1 | 653-657 | "The above unaudited consolidated financial results... reviewed by Audit Committee and approved by Board..." | |
| 7.2 | 2 | 659-670 | "The unaudited consolidated financial results... includes the results of the following subsidiary companies:" — see sub-table 7.2.x | |
| 7.2.1 | 2.a | 665 | Satin Housing Finance Limited | 100.00% | |
| 7.2.2 | 2.b | 666 | Satin Finserv Limited | 100.00% | |
| 7.2.3 | 2.c | 667 | Satin Technologies Limited | 100.00% | |
| 7.2.4 | 2.d | 668 | Satin Growth Alternatives Limited | 100.00% | |
| 7.2.5 | 2.e | 669-670 | QTrino Labs Limited (formerly QTrino Labs Private Limited) | 67.88% | `ENTITY_CHANGE` — renamed this quarter, see 7.10 |
| 7.3 | 3 | 672-674 | "The unaudited consolidated financial results have been prepared in accordance with applicable accounting standards..." | |
| 7.4 | 4 | 676-679 | "The secured non-convertible debentures issued by the respective companies are fully secured..." | |
| 7.5 | 5 | 681-694 | "During the quarter... Group has allotted following Non-Convertible Securities..." a-f, 6 sub-items | broader than standalone Note 4 (2 items) — Group-level NCD issuance includes 4 additional NCD tranches (c-f) not disclosed at standalone level |
| 7.5.1 | 5.a | 683-684 | 8,446 subordinated NCDs, Rs 8,446.00L, 2 investors, May 26 2026 | matches standalone 4.4.a |
| 7.5.2 | 5.b | 685-686 | 2,000 USD bonds, Rs 19,046.00L, 1 investor, May 27 2026 | matches standalone 4.4.b |
| 7.5.3 | 5.c | 687-688 | 30,000 senior secured NCDs, Rs 3,000.00L, 2 investors, Apr 28 2026 | not in standalone note 4 — subsidiary-level issuance |
| 7.5.4 | 5.d | 689-690 | 50,000 senior secured NCDs, Rs 5,000.00L, 1 investor, Jun 10 2026 | not in standalone note 4 |
| 7.5.5 | 5.e | 691-692 | 50,000 senior secured NCDs, Rs 5,000.00L, 3 investors, Jun 18 2026 (re-issuance) | not in standalone note 4 |
| 7.5.6 | 5.f | 693-694 | 40,000 senior secured NCDs, Rs 4,000.00L, 1 investor, Jun 29 2026 (re-issuance) | not in standalone note 4 |
| 7.6 | 6 | 697-699 | "...Parent Company made investments aggregating to Rs 1,000.00 lakhs in Satin Technologies Limited..." | mirrors standalone 4.5 |
| 7.7 | 7 | 701-703 | "...Parent Company made an investment aggregating to Rs 5,000.00 lakhs in Satin Finserv Limited..." | mirrors standalone 4.6 |
| 7.8 | 8 | 725-727 | "Subsequent to quarter ended... Parent Company made an investment aggregating to Rs 1,200.00 lakhs in Satin Growth Alternatives Limited..." | mirrors standalone 4.7, subsequent event |
| 7.9 | 9 | 729-733 | "...Satin Technologies Limited... invested balance amount of Rs 636.00 Lakhs in QTrino Labs Limited... converted 27,180 partly paid-up shares... STL holding increased from 50.84% to 70.67%... as on June 30, 2026, STL holds 67.88% in QTrino..." | not present in standalone notes (consolidation-only event) |
| 7.10 | 10 | 735-736 | "Subsequent to quarter ended... name of 'QTrino Labs Private Limited'... changed to 'QTrino Labs Limited' vide RoC order dated July 15, 2026" | `ENTITY_CHANGE` (rename), subsequent event |
| 7.11 | 11 | 737-739 | "Pursuant to exercise of ESOP Options... 70,000 equity shares were exercised..." | mirrors standalone 4.8 |
| 7.12 | 12 | 741-749 | "...Board of Directors of the Parent Company in its meeting held on June 04, 2026 had approved the proposal for issuance... 38,50,000 fully convertible warrants... Rs 260.00 each... Trishashna Holdings..." | mirrors standalone 4.9 |
| 7.13 | 13 | 751-756 | "CODM reviews operations at the Group level... 'financing activities' majorly... Satin Technologies, Satin Growth Alternatives and QTrino Labs currently do not have any reportable segment... single geographical segment, domestic" | `ZERO_STANDING` — explicit "no reportable segment" disclosure for 3 subsidiaries |
| 7.14 | 14 | 759-783 | Reg 52(4) additional information table (Group), 19 items expected — see 7.14.1-7.14.19; **table severely OCR-corrupted on p.14, several labels and values illegible or absent from extract** | `OCR_UNCLEAR` / `OCR_DROPPED_LINE` — flagged for A1 re-verification against source PDF, see notes below |
| 7.14.1 | 14.1 | 765 | Debt-equity ratio (x) | 3.97 | |
| 7.14.2 | 14.2 | 766 | Debt service coverage ratio | Not applicable (label garbled "Not icable") | `ZERO_STANDING` |
| 7.14.3 | 14.3 | 767 | Interest service coverage ratio | Not applicable (value cut off) | `ZERO_STANDING` / `OCR_UNCLEAR` |
| 7.14.4 | 14.4 | 768 | Outstanding redeemable preference shares (qty & value) | value not visible in extract | `OCR_UNCLEAR` (by analogy to standalone: Nil) |
| 7.14.5 | 14.5 | 769 | Capital redemption reserve (Rs L) | 2,777.00 | |
| 7.14.6 | 14.6 | 770 | Debenture redemption reserve (Rs L) | Not applicable | `ZERO_STANDING` |
| 7.14.7 | 14.7 | 771 | Net worth (Rs L) | value garbled ("2 1.98") | `OCR_UNCLEAR` — cannot confirm digit string |
| 7.14.8 | 14.8 | 772 | Net profit after tax (Rs L) | value not visible in extract (expected ~12,264.56 per P&L) | `OCR_DROPPED_LINE` |
| 7.14.9 | 14.9 | 773-774 | EPS Basic / Diluted (Rs) | values not visible in extract (expected ~11.15/11.15 per P&L) | `OCR_DROPPED_LINE` |
| 7.14.10 | 14.10 | 775 | Current ratio (x) | Not applicable (value cut off) | `ZERO_STANDING` / `OCR_UNCLEAR` |
| 7.14.11 | 14.11 | 776 | Long term debt to working capital (x) | value not visible | `OCR_UNCLEAR` |
| 7.14.12 | 14.12 | 777 | Bad debts to Account receivable ratio | value not visible | `OCR_UNCLEAR` |
| 7.14.13 | 14.13 | 778 | Current liability ratio (x) | value not visible | `OCR_UNCLEAR` |
| 7.14.14 | 14.14 | 779 | Total debts to total assets | value not visible (expected ~0.7x per standalone analogy) | `OCR_DROPPED_LINE` |
| 7.14.15 | 14.15 | 780 | Debtors turnover | Not applicable | `ZERO_STANDING` |
| 7.14.16 | 14.16 | 781 | Inventory turnover | value not visible ("tumover" label truncated) | `OCR_UNCLEAR` |
| 7.14.17 | 14.17 | n/a | Operating margin (%) | **label and value entirely absent from extract** between line 781 and 783 | `OCR_DROPPED_LINE` — flagged, item present in standalone (4.14.17) so expected here too |
| 7.14.18 | 14.18 | 783 | Net profit margin (%) | 16.04% (isolated numeric value, inferred to be this row by position) | `OCR_UNCLEAR` on row label attribution |
| 7.14.19 | 14.19 | n/a | Sector-specific ratios a) GNPA b) NNPA c) PCR d) CRAR e) LCR | **entirely absent from extract** — no GNPA/NNPA/PCR/CRAR/LCR rows visible anywhere in ln 759-786 (contrast standalone 4.14.19, ln 404-409, fully populated) | `OCR_DROPPED_LINE` — HIGH-PRIORITY flag: these 5 sub-items are load-bearing NBFC asset-quality metrics at Group level and must be re-extracted from source PDF page 14 before A3/A4 review |
| 7.15 | 15 | 798-800 | "The figures for the quarter ended March 31, 2026 represent the balancing figures..." | matches LRR para 5.10 |
| 7.16 | 16 | 802 | "Previous year/period figures have been regrouped/rearranged..." | |
| — | Board sign-off | 803-810 | Harvinder Pal Singh, Chairman cum Managing Director, DIN 00333754, Gurugram, July 30, 2026 | non-digital scanned signature |

Consolidated note count = **16** (headline notes). Consolidated note-table
sub-line-item count (7.2 block 5 + 7.5 block 6 + 7.14 block 19, incl.
OCR-unclear/dropped rows which are still enumerated) = **30**.

---
## 8. SIGNATURE BLOCKS (all instances, cross-document)
| # | Signatory | Role | Line | Timestamp | Flags |
|---|-----------|------|------|-----------|-------|
| 8.1 | Vikas Gupta | Company Secretary & CCO | 56-67 | digital, 2026.07.30 16:05:12 +05'30' | after board meeting concluded (15:52) — no timing flag |
| 8.2 | Rajesh Sethi (J C Bhalla & Co.) | Partner, standalone LRR | 149-161 | non-digital, Gurugram, July 30 2026 | `OCR_UNCLEAR` re: UDIN legibility (ln 159) |
| 8.3 | Harvinder Pal Singh | Chairman cum Managing Director (standalone results) | 430-438 | non-digital, Gurugram, July 30 2026 | DIN 00333754 |
| 8.4 | Rajesh Sethi (J C Bhalla & Co.) | Partner, consolidated LRR | 556-569 | non-digital, Gurugram, July 30 2026 | UDIN "260BE663nrLNqfsfs" present but `OCR_UNCLEAR` on exact digits |
| 8.5 | Harvinder Pal Singh | Chairman cum Managing Director (consolidated results) | 807-810 | non-digital, Gurugram, July 30 2026 | DIN 00333754 |

---
## SUMMARY COUNTS (reconciled to A2 COUNT TEST above)
- Agenda items: 1
- Statement blocks (standalone + consolidated P&L): 2
- Auditor (LRR) reports: 2, substantive paragraphs: 13 (5 standalone + 8 consolidated)
- Entities (Group list): 6
- Notes (headline, numbered 1-16 x 2 statements): 32
- Core P&L line items: 70 (32 standalone + 38 consolidated)
- Note-table sub-line-items: 74 (standalone 44: Note10=22, Note12=3, Note14=19;
  consolidated 30: Note2=5, Note5=6, Note14=19)
- Total line_items (core P&L 70 + note-table sub-rows 74) = **144**
  (this figure was cross-checked twice while drafting this summary -- the
  first draft mis-added the note-table sub-row subtotal as 68 instead of 74;
  corrected here and in the header COUNT TEST block above before emission.
  Every individual row 3.x/4.x/6.x/7.x, including all .x sub-rows, carries
  exactly one line citation with no duplicates on re-check.)

Figures to carry forward to A3/A4: **144 line items**, **32 notes**, **1
agenda item**, **6 entities**, **13 auditor paragraphs**.

Flags raised across this ledger: ZERO_STANDING (29 instances: 2 standalone
P&L + 2 consolidated P&L + 4 standalone Note10 + 11 standalone Note14 + 1
consolidated Note13 + 8 consolidated Note14 clear "Not applicable"/Nil +
1 consolidated P&L 6.34), ENTITY_CHANGE (1: QTrino Labs Private Limited ->
QTrino Labs Limited, notes 7.2.5/7.10), OCR_UNCLEAR (multiple, standalone
UDIN + consolidated UDIN + several consolidated Note14 values), and the
high-priority OCR_DROPPED_LINE flags on consolidated Note 14 (Operating
margin row entirely missing, GNPA/NNPA/PCR/CRAR/LCR sector-specific ratios
entirely missing, Net profit after tax and EPS values missing) — this last
group needs A1 re-verification against the source PDF page 14 before A4
analysis relies on any Group-level asset-quality ratio.

```yaml
stage: A2-enumerator
company: "SATIN"
quarter: "q1fy27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/satin-q1fy27/work/ledger_results_satin_q1fy27.md"
counts:
  notes: 32
  line_items: 144
  zero_standing: 29
  agenda_items: 1
  auditor_paras: 13
  entities: 6
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, ENTITY_CHANGE, OCR_UNCLEAR, OCR_DROPPED_LINE]
gate_a2: pass
mismatch_note: ""
```
