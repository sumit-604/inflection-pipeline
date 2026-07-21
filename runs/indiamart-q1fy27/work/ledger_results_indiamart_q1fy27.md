# A2 ENUMERATION LEDGER — IndiaMART InterMESH Limited (INDIAMART), Q1 FY27, Results Filing
Source: extract_results_indiamart_q1fy27.txt (16 pages, 727 source-numbered lines)
Prior-quarter ledger: NONE (first quarterly run for this ticker; entity-change flags below are self-evident within this single filing's own text markers — "formerly known as", "till", "w.e.f." — not cross-run diffs)

```
=== A2 COUNT TEST ===
category: notes            grep_count: 14   sweep_count: 14   match: yes
category: line_items       grep_count: 65   sweep_count: 65   match: yes
category: zero_standing    grep_count: 1    sweep_count: 1    match: yes
category: agenda_items     grep_count: 2    sweep_count: 2    match: yes
category: auditor_paras    grep_count: 16   sweep_count: 16   match: yes
category: entities         grep_count: 13   sweep_count: 13   match: yes
category: annexure_rows    grep_count: 8    sweep_count: 8    match: yes
category: signature_blocks grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Methodology note: grep_count for notes = numbered-note markers within the two "Notes to the Statement..." sections (5 consolidated + 6 standalone, matched via `^(I|[0-9]+)\s+[A-Z]`, note 1 in both sections OCR-extracts as roman "I" not digit "1") plus unnumbered lettered footnotes under the Segment Information table (a/b/c, 3 total) = 14. grep_count for line_items used a column-gap value-pattern regex restricted to the three financial-statement table line ranges, reconciled against a full manual line-by-line read of each table = 65. grep_count for auditor_paras counts the six recurring structural headings (report title, Opinion, Basis for Opinion, Management's Responsibilities, Auditor's Responsibilities, Other Matter(s)) times 2 reports, plus the lettered Other-Matters sub-items (3 consolidated + 1 standalone) = 16; this maps 1:1 to a manual read of both auditor's reports at section granularity (finer semantic paragraph splits within "Management's Responsibilities" and "Auditor's Responsibilities" were considered but the source text does not blank-line-delimit them, so section-level is the reconcilable unit and finer content, e.g. Going Concern language and the group-audit responsibility clause, is called out in the row detail/flags instead of forced into separate rows).

---

## 1. BOARD OUTCOME — AGENDA ITEMS
Board meeting: commenced 11:00 a.m., concluded 15:15 p.m. (line 34) — approx. 4hr15min meeting.

| # | Line | Agenda item | Detail | Flags |
|---|------|-------------|--------|-------|
| 1 | 17-25 | I. Audited Consolidated and Standalone Financial Results | Approved Q1 FY27 (quarter ended June 30, 2026) results + Auditors' Reports, Annexure A. Results to be disseminated on company website. | — |
| 2 | 26-32 | II. Incorporation of a Wholly Owned Subsidiary | Approved incorporation of "IndiaMART Finance Limited" (WOS), subject to necessary approvals. Regulation 30 disclosure detail as Annexure B. | NEW_ENTITY_PENDING |

No other agenda items present: no AR approval, no AGM notice, no record date, no dividend, no director appointment/resignation, no auditor change, no scrutinizer, no ESOP grant, no capital-raising enabling resolution in this Board Outcome letter — this is a two-item, results-plus-one-corporate-action meeting.

## 2. SIGNATURE BLOCKS
| # | Line | Signatory | Designation | Timestamp | Flags |
|---|------|-----------|-------------|-----------|-------|
| 1 | 44-52 | Vasudha Bagri | Compliance Officer (Membership No. A28500) | 2026.07.21 15:16:52 +05'30' | — (after 15:15 meeting conclusion; expected sequence for covering letter) |
| 2 | 442-452 | Dinesh Chandra Agarwal | Managing Director and Chief Executive Officer | 2026.07.21 12:25:31 +05'30' (consolidated results) | SIGNATURE_BEFORE_MEETING_CONCLUDED — signed ~2h50m before the 15:15 board conclusion that was to approve these results |
| 3 | 677-687 | Dinesh Chandra Agarwal | Managing Director and Chief Executive Officer | 2026.07.21 12:24:43 +05'30' (standalone results, OCR-garbled as "12,24,43+os•30•") | SIGNATURE_BEFORE_MEETING_CONCLUDED — same issue, standalone results |
| 4 | 244-255 | David Jones | Partner, B S R & Co. LLP (Membership No. 098113), signed at Bali | 21 July 2026, UDIN:26098113QZDUTA5455 | — (consolidated auditor's report; no time given) |
| 5 | 586-598 | David Jones | Partner, B S R & Co. LLP (Membership No. 098113), signed at Bali | 21 July 2026, UDIN:26098113OWPLAA6395 | — (standalone auditor's report; no time given) |

## 3. AUDITOR'S REPORTS — PARAGRAPH-LEVEL ENUMERATION

### 3A. Consolidated Financial Results — Independent Auditors' Report (pages 3-7, lines 66-305)
| # | Line(s) | Section | Content summary | Flags |
|---|---------|---------|------------------|-------|
| 1 | 66-69 | Title / addressee | "Independent Auditors' Report", to Board of Directors, "Report on the audit of the Consolidated Financial Results" | — |
| 2 | 70-88 | Opinion | Unmodified opinion; results include entities per Annexure I; presented per Reg 33; true and fair view for quarter ended 30 June 2026 (items a, b, c) | opinion_type: unmodified |
| 3 | 89-101 | Basis for Opinion | Audit per SAs u/s 143(10); independence per ICAI Code of Ethics; sufficiency of evidence incl. other auditors' reports referenced in Other Matters (a) | — |
| 4 | 102-141 | Management's and BoD Responsibilities | Preparation basis (Ind AS 34); responsibility for accounting records, internal controls; going-concern assessment responsibility (135-139); oversight of financial reporting process (140-141) | GOING_CONCERN_LANGUAGE (management-responsibility boilerplate only — no material uncertainty raised) |
| 5 | 143-201 | Auditor's Responsibilities | Objectives/materiality (145-151); 6 bulleted procedures (154-191) incl. going-concern conclusion bullet (165-172, GOING_CONCERN_LANGUAGE — boilerplate, no uncertainty flagged) and group-audit responsibility bullet unique to consolidated report (176-191, describes reliance on other auditors, cross-refs Other Matters (a)); communication with those charged with governance (192-198); Reg 33(8) SEBI circular procedures (199-200) | — |
| 6 | 202-203 | Other Matters (heading, plural) | — | — |
| 7 | 204-214 | Other Matters (a) | 4 subsidiaries: unaudited BY US but audited by their own independent auditors; total revenue (pre-consolidation) Rs 27.25 mn, total net loss after tax (pre-consolidation) Rs 64.75 mn for the quarter; their auditors' reports furnished to B S R; opinion not modified | ENTITY_AUDITED_BY_OTHERS (4 subsidiaries) |
| 8 | 215-227 | Other Matters (b) | 7 associates: Group share of net loss after tax Rs 127.84 mn, audited-info basis. PLUS 1 associate (IB MonotaRO, period 1 Apr–29 May 2026): Group share of net loss Rs 17.69 mn, UNAUDITED by B S R or any other auditor, furnished by Board of Directors, deemed not material; opinion not modified | ENTITY_UNAUDITED_MGMT_FURNISHED (IB MonotaRO Private Limited) |
| 9 | 228-243 | Other Matters (c) | Q4 FY26 (3 months ended 31 March 2026) comparative figures are balancing figures (audited FY26 full year less published 9M audited YTD) — standard methodology note, not a new issue | — |
| 10 | 244-260 | Signature block | For B S R & Co. LLP, Chartered Accountants, Firm's Reg. No. 101248W/W-100022; David Jones, Partner, Bali, 21 July 2026, UDIN:26098113QZDUTA5455 | — |
| 11 | 267-305 | Annexure I — entity list | List of 13 entities in consolidation (enumerated separately, Section 4 below) | see Section 4 |

Auditor_paras count basis for Section 3A (rows counted toward the 16-row grep/sweep test): title(1), Opinion(1), Basis for Opinion(1), Mgmt Resp(1), Auditor Resp(1), Other Matters heading's 3 lettered sub-items (a,b,c = 3), signature(1) = 9. (Annexure I is counted under Entities, not auditor_paras.)

### 3B. Standalone Financial Results — Independent Auditor's Report (pages 11-13, lines 464-604)
| # | Line(s) | Section | Content summary | Flags |
|---|---------|---------|------------------|-------|
| 1 | 464-467 | Title / addressee | "Independent Auditors' Report", to Board of Directors, "Report on the audit of the Standalone Financial Results" | — |
| 2 | 468-483 | Opinion | Unmodified opinion; presented per Reg 33; true and fair view, quarter ended 30 June 2026 (items a, b) | opinion_type: unmodified |
| 3 | 484-494 | Basis for Opinion | Audit per SAs u/s 143(10); auditor independence; sufficiency of evidence | — |
| 4 | 495-527 | Management's and BoD Responsibilities | Preparation basis (Ind AS 34); responsibility for records/controls; going-concern assessment responsibility (523-525); oversight of financial reporting (526) | GOING_CONCERN_LANGUAGE (boilerplate only) |
| 5 | 528-568 | Auditor's Responsibilities | Objectives/materiality (530-536); 5 bulleted procedures (539-560) incl. going-concern bullet (550-557, GOING_CONCERN_LANGUAGE — boilerplate); communication with those charged with governance (561-563); ethical-requirements statement (564-567). NOTE: standalone report has only 5 bullets vs 6 in consolidated — lacks the group-audit-reliance bullet and lacks the Reg 33(8) circular paragraph present in the consolidated report | STRUCTURAL_ASYMMETRY vs consolidated report (expected: standalone has no group to consolidate) |
| 6 | 569-570 | Other Matter (heading, singular — note singular vs consolidated's plural "Other Matters") | — | — |
| 7 | 571-584 | Other Matter (a) | Same balancing-figures methodology note as consolidated Other Matters (c): Q4 FY26 comparatives are balancing figures | — |
| 8 | 585-604 | Signature block | For B S R & Co. LLP, Chartered Accountants, Firm's Reg. No. 101248W/W-100022; David Jones, Partner, Bali, 21 July 2026, UDIN:26098113OWPLAA6395 | — |

Auditor_paras count basis for Section 3B: title(1), Opinion(1), Basis for Opinion(1), Mgmt Resp(1), Auditor Resp(1), Other Matter's single lettered sub-item (1), signature(1) = 7.

Total auditor_paras = 9 + 7 = 16.

UDIN numbers: 26098113QZDUTA5455 (consolidated), 26098113OWPLAA6395 (standalone) — both by same partner (David Jones, Membership 098113) same date, different UDIN as required per report.

## 4. ENTITIES — ANNEXURE I, LIST OF ENTITIES IN CONSOLIDATED FINANCIAL RESULTS (lines 267-305)
| Sr. | Line | Entity | Relationship | Flags |
|-----|------|--------|---------------|-------|
| 1 | 273 | Tradezeal Online Private Limited | Subsidiary | — |
| 2 | 275 | Pay With Indiamart Private Limited | Subsidiary | — |
| 3 | 277-278 | Busy Infotech Private Limited (Formerly known as Tolexo Online Private Limited) | Subsidiary | ENTITY_CHANGE — renamed from Tolexo Online Private Limited |
| 4 | 280-281 | Livekeeping Technologies Private Limited (Formerly known as Finlite Technologies Private Limited) | Subsidiary | ENTITY_CHANGE — renamed from Finlite Technologies Private Limited |
| 5 | 283 | IIL Digital Private Limited | Subsidiary | — |
| 6 | 285 | Simply Vyapar Apps Private Limited | Associate | — |
| 7 | 287 | IB MonotaRO Private Limited (till 29 May 2026) | Associate | ENTITY_CHANGE — ceased to be an associate during the quarter (29 May 2026); also the UNAUDITED, management-furnished associate referenced in Other Matters (b) of the consolidated auditor's report |
| 8 | 289 | Truckhall Private Limited | Associate | — |
| 9 | 291 | Agillos E-Commerce Private Limited | Associate | — |
| 10 | 293 | Edgewise Technologies Private Limited | Associate | — |
| 11 | 295 | Adansa Solutions Private Limited | Associate | — |
| 12 | 297 | Mobisy Technologies Private Limited | Associate | — |
| 13 | 299-300 | Fleetex Technologies Private Limited (w.e.f 11 April 2025) | Associate | ENTITY_CHANGE — added w.e.f. 11 April 2025 (prior FY date; first appearance in this ledger since no prior-quarter ledger was supplied) |

Entities count for GATE reconciliation = 13 (the Annexure I list only). Total subsidiaries = 5, associates = 8.

Not yet in the consolidation list — tracked separately, do NOT count toward the 13/13 gate:
| — | 28-29, 690-727 | IndiaMART Finance Limited | Proposed Wholly Owned Subsidiary (India), not yet incorporated | NEW_ENTITY_PENDING — Annexure B gives full incorporation detail (see Section 6) |

4 of 13 listed entities (31%) carry an ENTITY_CHANGE flag this quarter (2 renames, 1 exit, 1 addition) — a higher-than-typical churn rate in the consolidation perimeter worth surfacing to A3/A4.

## 5. FINANCIAL STATEMENT LINE ITEMS

### 5A. Consolidated Financial Results (page 8, lines 320-351) — 21 line items
Columns: Q1 FY27 (Jun 30, 2026) | Q4 FY26 (Mar 31, 2026, refer note 3) | Q1 FY26 (Jun 30, 2025) | FY26 (Mar 31, 2026 year)

| # | Line | Particular | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-----------|--------|--------|--------|------|-------|
| 1 | 321 | a) Revenue from operations | 4,144 | 4,043 | 3,721 | 15,690 | — |
| 2 | 322 | b) Other income | 1,067 | (339) | 924 | 2,041 | — |
| 3 | 323 | Total income | 5,211 | 3,704 | 4,645 | 17,731 | — |
| 4 | 326 | a) Employee benefits expense | 1,740 | 1,780 | 1,610 | 6,928 | — |
| 5 | 327 | b) Finance costs | 5 | 6 | 10 | 30 | — |
| 6 | 328 | c) Depreciation and amortisation expense | 64 | 70 | 69 | 284 | — |
| 7 | 329 | d) Other expenses | 939 | 937 | 776 | 3,462 | — |
| 8 | 330 | Total expenses | 2,748 | 2,793 | 2,465 | 10,704 | — |
| 9 | 332 | 3. Profit before share of loss in associates and tax (1-2) | 2,463 | 911 | 2,180 | 7,027 | — |
| 10 | 333 | 4. Share in net loss of associates | (146) | (127) | (141) | (548) | — |
| 11 | 334 | 5. Profit before tax (3+4) | 2,317 | 784 | 2,039 | 6,479 | — |
| 12 | 337 | 6a) Current tax | 430 | 404 | 389 | 1,626 | — |
| 13 | 338 | 6b) Deferred tax | 165 | (122) | 115 | 106 | — |
| 14 | 339 | Total tax expense | 595 | 282 | 504 | 1,732 | — |
| 15 | 341 | 7. Net Profit for the period/year [5-6] | 1,722 | 502 | 1,535 | 4,747 | — |
| 16 | 343 | 8. -Items that will not be reclassified to profit or loss (OCI) | 6 | 24 | (22) | 37 | — |
| 17 | 344 | 9. Total comprehensive income for the period/year [7+8] | 1,728 | 526 | 1,513 | 4,784 | — |
| 18 | 345 | 10. Paid up equity share capital (FV INR 10) | 601 | 601 | 600 | 601 | — |
| 19 | 346 | 11. Other equity for the year | (blank) | (blank) | (blank) | 23,403 | Quarterly columns structurally blank (balance-sheet item, disclosed annually only) — not dash/nil, no ZERO_STANDING |
| 20 | 348 | 12. Basic EPS (INR 10 per share) | 28.66 (Not annualised) | 8.36 (Not annualised) | 25.59 (Not annualised) | 79.07 (Annualised) | — |
| 21 | 350 | 12. Diluted EPS (INR 10 per share) | 28.56 (Not annualised) | 8.33 (Not annualised) | 25.52 (Not annualised) | 78.77 (Annualised) | — |

### 5B. Segment Information — Consolidated (page 9, lines 366-410) — 25 line items
Two reportable segments: "Web and Related Services", "Accounting Software Services".

| # | Line | Particular | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-----------|--------|--------|--------|------|-------|
| 1 | 367 | Segment Revenue a) Web and related services | 3,759 | 3,683 | 3,463 | 14,430 | — |
| 2 | 368 | Segment Revenue b) Accounting Software services | 385 | 361 | 258 | 1,261 | — |
| 3 | 369 | Segment Revenue Total | 4,144 | 4,044 | 3,721 | 15,691 | — |
| 4 | 371 | Less: Inter-Segment Revenue a) Web and related services | - | (1) | - | (1) | — |
| 5 | 372 | Less: Inter-Segment Revenue b) Accounting Software services | - | - | - | - | ZERO_STANDING — dash in all four periods; template line for a transaction type (inter-segment sale of accounting-software services) that has not occurred |
| 6 | 373 | Less: Inter-Segment Revenue Total | - | (1) | - | (1) | — |
| 7 | 375 | Revenue from ops from external customers a) Web and related services | 3,759 | 3,682 | 3,463 | 14,429 | — |
| 8 | 376 | Revenue from ops from external customers b) Accounting Software services | 385 | 361 | 258 | 1,261 | — |
| 9 | 377 | Revenue from ops from external customers Total | 4,144 | 4,043 | 3,721 | 15,690 | — |
| 10 | 380 | Segment Result a) Web and related services | 1,492 | 1,333 | 1,340 | 5,328 | — |
| 11 | 381 | Segment Result b) Accounting Software services | (27) | (7) | (6) | (28) | — |
| 12 | 382 | Segment Result Total | 1,465 | 1,326 | 1,334 | 5,300 | — |
| 13 | 383 | Finance Cost | (5) | (6) | (10) | (30) | — |
| 14 | 384 | Depreciation and amortisation expense | (64) | (70) | (69) | (284) | — |
| 15 | 385 | Other income | 1,067 | (339) | 925 | 2,041 | note: 925 vs 924 in main statement Q1FY26 col — 1 mn rounding diff between statement 5A row 2 and this row, worth an A3/A4 arithmetic check |
| 16 | 386 | Profit before share of loss in associates and tax | 2,463 | 911 | 2,180 | 7,027 | — |
| 17 | 387 | Share in net loss of associates | (146) | (127) | (141) | (548) | — |
| 18 | 388 | Profit before tax | 2,317 | 784 | 2,039 | 6,479 | — |
| 19 | 392 | Segment Assets a) Web and related services | 33,739 | 31,410 | 26,396 | 31,410 | — |
| 20 | 393 | Segment Assets b) Accounting Software services | 7,473 | 7,207 | 6,914 | 7,207 | — |
| 21 | 394 | Segment Assets Unallocable | 7,412 | 7,629 | 6,919 | 7,629 | — |
| 22 | 395 | Segment Assets Total | 48,624 | 46,246 | 40,229 | 46,246 | — |
| 23 | 398 | Segment Liabilities a) Web and related services | 24,673 | 20,708 | 18,548 | 20,708 | — |
| 24 | 399 | Segment Liabilities b) Accounting Software services | 1,755 | 1,534 | 1,246 | 1,534 | — |
| 25 | 400 | Segment Liabilities Total | 26,428 | 22,242 | 19,794 | 22,242 | — |

Segment table footnotes (unnumbered, lettered — counted in Notes category, Section 7):
- a) (402-403): definition of operating segments basis
- b) (405-406): two reportable segments identified, basis for determination
- c) (408-410): description of each segment's business

### 5C. Standalone Financial Results (page 14, lines 617-644) — 19 line items
| # | Line | Particular | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-----------|--------|--------|--------|------|-------|
| 1 | 618 | a) Revenue from operations | 3,759 | 3,682 | 3,463 | 14,428 | — |
| 2 | 619 | b) Other income | 881 | (339) | 844 | 1,908 | — |
| 3 | 620-621 | Total income | 4,640 | 3,343 | 4,307 | 16,336 | — |
| 4 | 623 | a) Employee benefits expense | 1,571 | 1,620 | 1,485 | 6,344 | — |
| 5 | 624 | b) Finance costs | 5 | 6 | 8 | 27 | — |
| 6 | 625 | c) Depreciation and amortisation expense | 26 | 32 | 35 | 139 | — |
| 7 | 626 | d) Other expenses | 695 | 716 | 631 | 2,881 | — |
| 8 | 627 | Total expenses | 2,297 | 2,374 | 2,159 | 9,391 | — |
| 9 | 628 | 3. Profit before tax (1-2) | 2,343 | 969 | 2,148 | 6,945 | — |
| 10 | 630 | 4a) Current tax | 423 | 398 | 384 | 1,606 | — |
| 11 | 631 | 4b) Deferred tax | 159 | (125) | 104 | 87 | — |
| 12 | 632 | Total tax expense | 582 | 273 | 488 | 1,693 | — |
| 13 | 633 | 5. Net Profit for the period/year (3-4) | 1,761 | 696 | 1,660 | 5,252 | — |
| 14 | 636 | 6. -Items that will not be reclassified to profit or loss (OCI) | 6 | 24 | (22) | 37 | — |
| 15 | 637 | 7. Total comprehensive income for the period/year (5+6) | 1,767 | 720 | 1,638 | 5,289 | — |
| 16 | 638 | 8. Paid up equity share capital (FV INR 10) | 601 | 601 | 600 | 601 | — |
| 17 | 639 | 9. Other equity for the year | (blank) | (blank) | (blank) | 24,816 | Quarterly columns structurally blank, same as consolidated — no ZERO_STANDING |
| 18 | 641 | 10. Basic EPS (INR 10 per share) | 29.29 (Not annualised) | 11.58 (Not annualised) | 27.66 (Not annualised) | 87.49 (Annualised) | — |
| 19 | 643 | 10. Diluted EPS (INR 10 per share) | 29.20 (Not annualised) | 11.54 (Not annualised) | 27.59 (Not annualised) | 87.15 (Annualised) | — |

## 6. ANNEXURE B — DETAILS OF PROPOSED WHOLLY OWNED SUBSIDIARY (page 16, lines 690-727) — 8 rows
| # | Line | Particular | Description |
|---|------|-----------|-------------|
| 1 | 693-699 | Name, date and country of incorporation | IndiaMART Finance Limited; not yet incorporated; India |
| 2 | 700-702 | Holding company / relationship | Wholly Owned Subsidiary of IndiaMART InterMESH Limited |
| 3 | 703-704 | Industry | Financial Services |
| 4 | 705-711 | Brief background / line of business | To strengthen trust, engagement and retention of platform users by enabling short-term working-capital/financial-needs access |
| 5 | 712-716 | Regulatory approvals required | Ministry of Corporate Affairs and other relevant statutory/regulatory authorities |
| 6 | 717-720 | Nature of consideration | 100% subscription to initial paid-up share capital, in cash |
| 7 | 721-723 | Cost of subscription | Paid-up Capital: 50,000 equity shares of Rs. 10/- each = Rs. 5,00,000 (Five Lakhs) |
| 8 | 724-726 | Shareholding/control by listed entity | 100% |

## 7. NOTES — NUMBERED AND UNNUMBERED (14 total)

### 7A. Notes to Consolidated Financial Results (page 10, lines 413-437) — 5 numbered notes
| # | Line | First ~15 words |
|---|------|------------------|
| 1 | 415-416 | "The above consolidated financial results for the quarter ended June 30, 2026 were reviewed and recommended by the Audit Committee..." (unmodified audit opinion confirmed) |
| 2 | 419-420 | "The above consolidated financial results have been prepared in accordance with the Indian Accounting Standards..." |
| 3 | 423-424 | "The results for quarter ended March 31, 2026 are the balancing figures prepared on the basis of the consolidated financial statements..." |
| 4 | 425-426 | "The results for the quarter ended June 30, 2026 are available on the BSE Limited website..." |
| 5 | 428-437 | "The Government of India has notified provisions of The Code on Wages, 2019, The Industrial Relations Code, 2020..." (Labour Codes impact assessed in FY26; rules pending in remaining states, Group to evaluate consequential effect when notified) |

### 7B. Notes to Standalone Financial Results (page 15, lines 647-672) — 6 numbered notes
| # | Line | First ~15 words |
|---|------|------------------|
| 1 | 649-651 | "The above standalone financial results for the quarter ended June 30, 2026 were reviewed and recommended by the Audit Committee..." |
| 2 | 653-654 | "The above standalone financial results have been prepared in accordance with the Indian Accounting Standards..." |
| 3 | 656 | "As per IND AS 108 'Operating Segments', the Company has disclosed the segment information only as a part of consolidated financial results." |
| 4 | 658-659 | "The results for quarter ended March 31, 2026 are the balancing figures prepared on the basis of the standalone financial results..." |
| 5 | 660-661 | "The results for the quarter ended June 30, 2026 are available on the BSE Limited website..." |
| 6 | 663-672 | "The Government of India has notified provisions of The Code on Wages, 2019..." (same Labour Codes note as consolidated note 5, standalone-entity version) |

### 7C. Unnumbered footnotes — Segment Information table (page 9, lines 402-410) — 3 lettered footnotes
| # | Line | First ~15 words |
|---|------|------------------|
| a | 402-403 | "Operating segments are defined as components of an enterprise for which discrete financial information is available..." |
| b | 405-406 | "The Group had identified two business segments namely 'Web and Related Services' and 'Accounting Software Services'..." |
| c | 408-410 | "Web and related services pertains to online B2B marketplace for business products and services..." |

No asterisk/dagger footnotes and no "Note:" prefixes found elsewhere in the document; the only other footnote-like markers are the inline "(Not annualised)" / "(Annualised)" EPS qualifiers, which are treated as part of their respective EPS line items (Section 5A rows 20-21, 5C rows 18-19), not standalone notes.

## 8. CONCALL / INVESTOR PRESENTATION CATEGORIES
Not applicable — this A1 extract is a results filing only (Board Outcome letter + auditors' reports + financial statements + annexures). No transcript or investor-presentation content is present in the source document, so Sections "ENUMERATE — CONCALL TRANSCRIPT" and "ENUMERATE — INVESTOR PRESENTATION" of the operating rules yield zero rows for this doctype.

## SUMMARY FLAGS RAISED
- SIGNATURE_BEFORE_MEETING_CONCLUDED (x2): both consolidated and standalone results signed by MD/CEO Dinesh Chandra Agarwal at ~12:24-12:25 p.m., roughly 2h50m before the board meeting that approved them concluded at 15:15 p.m.
- ZERO_STANDING (x1): Segment Information, "Less: Inter-Segment Revenue, b) Accounting Software services" — dash in all four periods.
- ENTITY_CHANGE (x4 of 13 listed entities): 2 renames (Busy Infotech f/k/a Tolexo Online; Livekeeping Technologies f/k/a Finlite Technologies), 1 exit (IB MonotaRO, associate till 29 May 2026), 1 addition (Fleetex Technologies, w.e.f. 11 April 2025).
- NEW_ENTITY_PENDING (x1): IndiaMART Finance Limited, WOS approved for incorporation this board meeting, not yet part of the 13-entity consolidation list.
- ENTITY_UNAUDITED_MGMT_FURNISHED (x1): IB MonotaRO Private Limited — associate financial info for 1 Apr-29 May 2026 unaudited by any auditor, furnished by Board of Directors, deemed not material to Group (consolidated Other Matters, para b).
- ENTITY_AUDITED_BY_OTHERS (x4 subsidiaries): consolidated Other Matters, para a.
- GOING_CONCERN_LANGUAGE: standard boilerplate in both auditor reports (Management's Responsibilities and Auditor's Responsibilities sections) — no material uncertainty raised in either report.
