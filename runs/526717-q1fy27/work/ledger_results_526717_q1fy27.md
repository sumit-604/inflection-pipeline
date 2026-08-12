# A2 COMPLETENESS LEDGER — 526717 (HCP Plastene Bulkpack Ltd) — Q1 FY27 — results

Source: `extract_results_526717_q1fy27.txt` (18 pages, 793 lines, Lakhs, OCR pages: none, page coverage 100%)
Filing: Board Outcome letter (Reg 30/33) + Annexures A-D + CFO resignation letter + Standalone Auditor Review Report
+ Standalone Financial Results + Standalone Segment Info + Consolidated Auditor Review Report + Consolidated
Financial Results + Consolidated Segment Info.

=== A2 COUNT TEST ===
category: agenda_items    grep_count: 17   sweep_count: 18   match: yes (post-resweep)
category: line_items      grep_count: 143  sweep_count: 149  match: yes (post-resweep)
category: zero_standing   grep_count: 24   sweep_count: 24   match: yes
category: notes           grep_count: 6    sweep_count: 6    match: yes
category: auditor_paras   grep_count: 9    sweep_count: 9    match: yes
category: entities        grep_count: 3    sweep_count: 3    match: yes
gate_a2: pass
=== END COUNT TEST ===

### Reconciliation notes (mismatches found and resolved)

- **agenda_items**: mechanical grep for `^\s*[0-9]+\.\s|bullet markers|"The Board...approved/considered/took note"`
  found 17 of 18 items (line-numbered command run against lines 1-145). Missed: the paid-up capital
  consequent-increase disclosure at line 132 ("Consequent to the aforesaid allotment, the paid-up equity share
  capital... stands increased...") because it is phrased declaratively, not as a Board-action sentence and carries
  no item number. Confirmed by manual resweep of lines 1-145 and added as item 10a. Final count 18/18, reconciled.
- **line_items**: mechanical grep (Sr.No./lettered/roman-numeral/keyword pattern) run separately against each of
  the four financial tables found 22/25 (standalone segment), 44/44 (standalone P&L, after regex fix for `9 _|`
  underscore-prefixed row), 49/54 (consolidated P&L), 23/26 (consolidated segment) = 138 raw, revised to 143 after
  the standalone P&L regex fix. Gaps traced to OCR artifacts: (a) unlabeled numeric subtotal rows with no "Total"
  text (segment Assets/Liabilities totals), (b) a garbled "(¢)" glyph standing in for "(c) Unallocated" that broke
  the `\(c\)` pattern, (c) NCI/OCI-attribution rows wrapped across a page break (line 709-710). All gaps confirmed
  present by manual line-by-line resweep against the raw extract (see tables below); manual sweep count of 149 is
  authoritative and mechanically corroborated row-by-row.
- **zero_standing, notes, auditor_paras, entities**: grep and manual sweep agreed on first pass, no resweep needed.

---

## 1. BOARD OUTCOME — AGENDA ITEMS (Board meeting held 12 Aug 2026)

| # | Line | Item | Detail (first ~15 words) | Flags |
|---|------|------|---------------------------|-------|
| 1 | 42-44 | Item 1 | Approved Unaudited Standalone and Consolidated Financial Results for period ended June 30, 2026 | |
| 2 | 46-48 | Item 2 | Approved Limited Review Report (Reg 33) for Standalone and Consolidated results from Statutory Auditors | |
| 3 | 51-54 | Item 3 | Re-appointment of Mr. Prakash Parekh (DIN 00158264) as Director retiring by rotation, recommended to shareholders | |
| 4 | 56-57 | Item 4 | Approved Board Report together with all Annexures for FY ended March 31, 2026 | |
| 5 | 60-61 | Item 5 (header) | Considered and approved matters connected with 42nd AGM (sub-items below) | |
| 5a | 72-75 | AGM notice | Notice of 42nd AGM via VC/OAVM on 25 September 2026 | |
| 5b | 77 | E-voting agent | Appointment of NSDL for Remote E-Voting and E-Voting on day of AGM | |
| 5c | 79-80 | Scrutinizer | Appointment of Ketan Vyas & Co., Practicing Company Secretaries, as Scrutinizer for remote/AGM-day e-voting | |
| 5d | 82-84 | Register closure | Register of Members and Share Transfer Books closed 19 Sept - 25 Sept 2026 for 42nd AGM | |
| 5e | 86-87 | Record date | Record date for 42nd AGM: 18 September 2026 | |
| 5f | 89-91 | Cut-off / e-voting window | Cut-off date 18 Sept 2026; remote e-voting 9:00 AM 19 Sept to 5:00 PM 24 Sept 2026 | |
| 6 | 93-96 | MD re-appointment | Re-appointment of Mr. Prakash Hiralal Parekh as Managing Director for 3 years w.e.f. 1 Nov 2026, subject to shareholder approval (Annexure A) | UNNUMBERED_ITEM |
| 7 | 98-100 | ID re-appointment | Re-appointment of Mr. Sandeep Shah (DIN 01850151) as Non-Executive Independent Director for 5 years w.e.f. 9 Aug 2026 (Annexure B) | UNNUMBERED_ITEM |
| 8 | 102-105 | CFO resignation noted | Board noted resignation of Mr. Dhrumil Shah, CFO, effective 12 Aug 2026 (Annexure C) | UNNUMBERED_ITEM |
| 9 | 107-109 | Subsidiary dissolution noted | Board noted dissolution of HCP Plastene Bulkpack PLT, Malaysia LLP, subsidiary of the Company | UNNUMBERED_ITEM, ENTITY_CHANGE |
| 10 | 111-114 | Item 10 | Allotment of 16,780 equity shares (Rs 10 each) to employees on exercise of ESOP Scheme 2022 options | |
| 10a | 132-135 | Capital increase (consequent) | Paid-up equity capital increased from Rs 106,748,370 to Rs 106,916,170 (Annexure C referenced — appears to be wrong annexure letter; ESOP detail is Annexure D) | ANNEXURE_MISMATCH |
| 11 | 139-141 | Item 11 | Adoption of new set of Articles of Association (AOA), subject to shareholder approval at ensuing AGM | |
| meta | 145 | Meeting timing | Board meeting commenced 4:00 PM, concluded 4:20 PM (20-minute meeting) | SHORT_MEETING (info, not counted in agenda_items total) |
| meta | 151-158 | CS sign-off | Letter signed by Rishabh Kumar Jain, Company Secretary & Compliance Officer, Membership No. F7271 | |

Numbering observation: source jumps from item 5 straight to unnumbered board actions (items 6-9 by ledger order)
then resumes explicit numbering at "10." — flag **NUMBERING_GAP** (items 6-9 carry no printed item number in
the source; content confirms they are genuine, distinct Board resolutions, not sub-clauses of item 5 or 10).

---

## 2. ANNEXURE A (lines 172-218) — Reg 30 disclosure: Prakash Hiralal Parekh (MD re-appointment)

| Row | Line | Field | Value | Flags |
|-----|------|-------|-------|-------|
| A1 | 180 | Name of Director/KMP | Mr. Prakash Hiralal Parekh | |
| A2 | 181-187 | Reason for change | Appointed MD w.e.f. 1 Nov 2026 for further 3 years, subject to shareholder approval | |
| A3 | 188-192 | Date of appointment & term | Board noted appointment effective November 1, 2026 | |
| A4 | 193-205 | Brief profile | 25 years' experience in plastics industry; established flexible packaging plant; member IFIBCA | |
| A5 | 206-210 | Relationship disclosure | YES — Father of Mr. Aman Prakash Parekh (Executive Director of the Company) | |
| A6 | 211 | Any other information | NA | |

## 3. ANNEXURE B (lines 222-268) — Reg 30 disclosure: Sandeep Motilal Shah (Independent Director re-appointment)

| Row | Line | Field | Value | Flags |
|-----|------|-------|-------|-------|
| B1 | 231 | Name of Director/KMP | Mr. Sandeep Motilal Shah | |
| B2 | 232-239 | Reason for change | Appointed NED Independent Director w.e.f. 9 Aug 2026 for further 5 years, subject to shareholder approval | |
| B3 | 240-244 | Date of appointment & term | Board noted appointment from 9 August 2026 | |
| B4 | 245-257 | Brief profile | Chartered Accountant, 19+ years in taxation/audit; concurrent/statutory auditor of PSU Banks | |
| B5 | 258-260 | Relationship disclosure | NO | |
| B6 | 261 | Any other information | NA | |

## 4. ANNEXURE C (lines 274-300) — Reg 30 disclosure: Dhrumil Pranavkumar Shah (CFO resignation)

| Row | Line | Field | Value | Flags |
|-----|------|-------|-------|-------|
| C1 | 282 | Name of Director/KMP | Mr. Dhrumil Pranavkumar Shah | |
| C2 | 283-286 | Reason for change | Resigned as CFO w.e.f. 12 Aug 2026, cited further career opportunity | |
| C3 | 287-288 | Date of cessation | 12 August 2026 | |
| C4 | 289 | Brief profile | NA | |
| C5 | 290-292 | Relationship disclosure | NA | |
| C5(dup) | 293 | Resignation letter | Attached | DUPLICATE_ROW_NUMBER (row labelled "5" used twice — relationship disclosure and resignation-letter rows both printed as row 5) |

## 5. ANNEXURE D (lines 306-349) — Reg 30 r/w Schedule III disclosure: ESOP allotment

| Row | Line | Field | Value | Flags |
|-----|------|-------|-------|-------|
| D1 | 311-313 | Brief details of options granted | Not Applicable — this instance is allotment on exercise of options under ESOP Scheme 2022 | |
| D2 | 314-317 | Scheme under SEBI (SBEB) Regulations 2021 | Yes | |
| D3 | 318-320 | Total shares covered by options | 2,50,000 options in scheme; 16,780 equity shares (FV Rs 10) exercised for current allotment | |
| D4 | 321-322 | Exercise price | Rs 10 per option | |
| D5 | 324-325 | Exercise period | As per ESOP scheme | |
| D6 | 327-328 | Significant terms | As per ESOP Scheme of the Company | |
| D7 | 330-332 | Subsequent changes/cancellation | Not Applicable | |
| D8 | 333-334 | Options vested | 17,680 options | |
| D9 | 336-337 | Options exercised | 16,780 options | |
| D10 | 338-339 | Money realized on exercise | Rs 167,800 | |
| D11 | 341-343 | Total shares arising from exercise | 16,780 equity shares, FV Rs 10 each | |
| D12 | 344-345 | Options lapsed | 29,450 options | |

Annexure total rows: A(6) + B(6) + C(6, incl. duplicate row-5) + D(12) = **30 rows**.

---

## 6. CFO RESIGNATION LETTER (standalone document, page 8, lines 351-386)

| Row | Line | Content | Flags |
|-----|------|---------|-------|
| R1 | 351-361 | Header — Date 12/08/2026, addressed to Board of Directors, subject: resignation from office of CFO | |
| R2 | 364-367 | Body — tenders resignation from CFO post w.e.f. 12/08/2026, cites "further career opportunity" | |
| R3 | 369-370 | Body — confirms no material reason other than that mentioned for resignation | |
| R4 | 372-375 | Body — thanks Company, shareholders, Board for the opportunity and cooperation extended | |
| R5 | 377-386 | Signature block — Dhrumil Shah, Chief Financial Officer, countersigned by a Director | |

---

## 7. AUDITOR REVIEW REPORTS

### 7a. Standalone Review Report (Ashok Dhariwal & Co., pages 9-10, lines 391-450)

| Para | Line | Content (first ~15 words) | Flags |
|------|------|----------------------------|-------|
| Title | 391-393 | Independent Auditor's Review Report on Quarterly Unaudited Standalone Financial Results, Reg 33 | |
| 1 | 399-402 | Reviewed accompanying Statement of Unaudited Standalone Financial Results for quarter ended June 30, 2026 | |
| 2 | 404-410 | Management responsibility; prepared per Ind AS 34, Companies Act s.133, Reg 33 | |
| 3 | 412-422 | Review conducted per SRE 2410; scope less than an audit; no audit opinion expressed | |
| 4 | 424-431 | Conclusion: nothing has come to attention causing belief of non-disclosure or material misstatement (clean/unmodified) | |
| Sig | 438-450 | For Ashok Dhariwal & Co. (Reg No. 100648W); CA Harit Dhariwal, Partner, Membership No. 130279; UDIN 26130279VUHUHG3379; Ahmedabad, 12.08.2026 | |

### 7b. Consolidated Review Report (Ashok Dhariwal & Co., pages 14-15, lines 581-653)

| Para | Line | Content (first ~15 words) | Flags |
|------|------|----------------------------|-------|
| Title | 581-583 | Independent Auditor's Review Report on Quarterly Unaudited Consolidated Financial Results, Reg 33 | |
| 1 | 590-594 | Reviewed accompanying Statement of Consolidated Unaudited Financial Results, parent + subsidiary ("the Group") | |
| 2 | 596-602 | Parent's management responsibility; Ind AS 34, Companies Act s.133, Reg 33 | |
| 3 | 605-613 | Review conducted per SRE 2410; scope less than audit; no audit opinion | |
| 4 | 616-623 | Conclusion: nothing has come to notice causing belief of non-disclosure or material misstatement (clean/unmodified) | |
| 5 (Other Matters) | 625-637 | Subsidiary K P Woven Private Limited — unaudited interim info furnished by Management; total assets Rs 37,246.46 lakhs, revenue Rs 8,636.10 lakhs, PAT Rs 934.56 lakhs, TCI Rs 1.72 lakhs; conclusion not modified | UNAUDITED_ENTITY (subsidiary figures management-furnished, not independently reviewed by principal auditor) |
| Sig | 641-653 | For Ashok Dhariwal & Co. (Reg No. 100648W); CA Harit Dhariwal, Partner, Membership No. 130279; UDIN 26130279DHJZQB2407; Ahmedabad, 12.08.2026 | |

Auditor paragraph total: standalone 4 + consolidated 5 = **9 substantive paragraphs** (title and signature block logged
separately, not double-counted in the auditor_paras total).

---

## 8. DIGITAL SIGNATURE BLOCKS

| # | Line | Document | Signatory | Designation | Timestamp | Flags |
|---|------|----------|-----------|-------------|-----------|-------|
| S1 | 151-158 | Board Outcome letter | Rishabh Kumar Jain | Company Secretary & Compliance Officer (Membership F7271) | not digitally timestamped (wet/scan signature) | |
| S2 | 438-450 | Standalone Review Report | CA Harit Dhariwal | Partner, Ashok Dhariwal & Co. (Membership 130279) | 12.08.2026, UDIN 26130279VUHUHG3379 | |
| S3 | 519-523 | Standalone Financial Results | Prakash Hiralal Parekh | Managing Director (DIN 00158264) | 2026.08.12 17:23:28 +0530 | |
| S4 | 570-576 | Standalone Segment Information | Prakash Parekh | Managing Director (DIN 00158264) | 12th Aug 2026 (exact time garbled by OCR) | |
| S5 | 641-653 | Consolidated Review Report | CA Harit Dhariwal | Partner, Ashok Dhariwal & Co. (Membership 130279) | 12.08.2026, UDIN 26130279DHJZQB2407 | |
| S6 | 731-735 | Consolidated Financial Results | Prakash Hiralal Parekh | Managing Director (DIN 00158264) | 2026.08.12 17:24:04 +0530 | |
| S7 | 786-793 | Consolidated Segment Information | Prakash Parekh | Managing Director (DIN 00158264) | 2026.08.12 17:24:17 +0530 | |
| S8 | 379-386 | CFO Resignation Letter | Dhrumil Shah (+ Director countersign) | Chief Financial Officer | undated on face (letter dated 12/08/2026) | |

All digitally-timestamped signatures (S3, S6, S7 — 17:23:28, 17:24:04, 17:24:17) post-date the board meeting
conclusion (16:20 per line 145). No BEFORE-meeting-conclusion flag applies.

---

## 9. STANDALONE UNAUDITED FINANCIAL RESULTS — every line item (lines 466-514)

Columns: Q ended 30.06.2026 (Unaud.) | Q ended 31.03.2026 (Aud.) | Q ended 30.06.2025 (Unaud.) | FY ended 31.03.2026 (Aud.)

| Sr | Line | Particular | Flags |
|----|------|------------|-------|
| 1 | 466 | Revenue From Operation | |
| 2 | 467 | Other Income | |
| 3 | 468 | Total Income (1+2) | |
| 4 | 469 | Expenditure (header) | |
| 4a | 470 | a) Cost of Material Consumed | |
| 4b | 471 | b) Purchase of Stock in Trade | ZERO_STANDING (dash all 4 periods) |
| 4b(dup) | 472 | b) Changes in inventories of finished goods, WIP | DUPLICATE_LABEL ("b" reused) |
| 4c | 473 | c) Employees Benefits Expenses | |
| 4d | 474 | d) Finance Costs | |
| 4e | 475 | e) Depreciation & amortisation Expenses | |
| 4f | 476 | f) Other Expenses | |
| — | 477 | Total Expenditure (subtotal) | |
| 5 | 478 | Profit before exceptional items and tax (3-4) | |
| 6 | 479 | Exceptional Items | |
| 7 | 480 | Profit/(Loss) before tax (5-6) | |
| 8 | 481 | Tax Expenses (header) | |
| 8a | 482 | a) Current Tax | ZERO_STANDING (dash all 4 periods) |
| 8b | 483 | b) Tax for Earlier Years | ZERO_STANDING (dash all 4 periods) |
| 8b(dup) | 484 | b) Deferred Tax (Income)/Expense | DUPLICATE_LABEL ("b" reused) |
| 9 | 485 | Profit (Loss) for period from continuing operations (7-8) | |
| 10 | 486 | Profit (Loss) from discontinuing operations before tax | ZERO_STANDING (dash all 4 periods) |
| 11 | 487 | Tax expense of discontinuing operations | ZERO_STANDING (dash all 4 periods) |
| 12 | 488 | Profit/(loss) from Discontinuing operations after tax (10-11) | ZERO_STANDING (dash all 4 periods) |
| 13 | 489 | Profit/(Loss) for the period (9+12) | |
| 14 | 490 | Other Comprehensive Income (header) | |
| 14a | 491 | Items not reclassified subsequently to P&L | |
| 14a-i | 492 | Remeasurement gain/(loss) of Defined Benefit Plan | value shown only in current quarter col, others blank |
| 14a-ii | 493 | Income tax relating to Remeasurement gain of DBP | ZERO_STANDING (dash all 4 periods) |
| 14a-iii | 494-495 | Net change (Loss)/Gain in FV of investment in equity instruments | ZERO_STANDING (dash all 4 periods) |
| 14b | 496 | Items to be reclassified subsequently to P&L | ZERO_STANDING (dash all 4 periods) |
| 14b-i | 497 | Income tax relating to items reclassified to P&L | ZERO_STANDING (dash/blank all 4 periods) |
| — | 498 | Other Comprehensive Income, net of tax (subtotal) | |
| 15 | 499 | Total Comprehensive Income for the period (13+14) | |
| 16 | 500 | Paid-up Equity Shares Capital (FV Rs 10) | |
| 17 | 501 | Other Equity excluding revaluation reserve | ZERO_STANDING (no value printed in any of the 4 columns) |
| 18 | 502-503 | EPS (Continuing Operations) (header) | |
| 18a | 504 | (a) Basic | |
| 18b | 505 | (b) Diluted | |
| 19 | 506-507 | EPS (Discontinuing Operations) (header) | |
| 19a | 508 | (a) Basic | ZERO_STANDING (blank all 4 periods) |
| 19b | 510 | (b) Diluted | ZERO_STANDING (blank all 4 periods) |
| 20 | 511-512 | EPS (Continuing & Discontinuing Operations) (header) | |
| 20a | 513 | (a) Basic | |
| 20b | 514 | (b) Diluted | |

Standalone P&L: **44 rows enumerated, 13 ZERO_STANDING**.

## 10. STANDALONE SEGMENT INFORMATION — every line item (lines 533-567)

| Sr | Line | Particular | Flags |
|----|------|------------|-------|
| 1 | 533 | Segment Revenue (header) | |
| 1a | 534 | Woven Sacks Division | |
| 1b | 535 | Label Division | |
| — | 536 | Total | |
| — | 537-538 | Less: Inter Segment Revenue | ZERO_STANDING (dash all 4 periods) |
| — | 539 | Net Sales/Income from Operations | |
| 2 | 540-542 | Segment Results (EBIT) — Profit before Interest & Tax incl. Extraordinary Items (header) | |
| 2a | 543 | Woven Sacks Division | |
| 2b | 544 | Label Division | |
| — | 545 | Total | |
| i | 546-547 | Less: Interest | |
| — | 548 | Profit before Tax | |
| ii | 549 | Less: Provision for Tax/Deferred Tax (Income)/Expense | |
| iii | 550-551 | Other Comprehensive/unallocable Income | |
| — | 552 | Net Profit | |
| 3 | 553 | Segment Assets (header) | |
| 3a | 554 | (a) Woven Sacks Division | |
| 3b | 555 | (b) Label Division | |
| 3c | 556 | (c) Unallocated | |
| — | 557 | Total (unlabeled subtotal row) | |
| 4 | 558 | Segment Liabilities (header) | |
| 4a | 559 | (a) Woven Sacks Division | |
| 4b | 560 | (b) Label Division | |
| 4c | 561 | (c) Unallocated (OCR renders as "(¢) Unallocated") | |
| — | 562 | Total (unlabeled subtotal row) | |

Standalone Segment: **25 rows enumerated, 1 ZERO_STANDING**.

### Standalone Segment — Notes (lines 564-567)

| Note | Line | Content | Flags |
|------|------|---------|-------|
| 1 | 564-565 | Audit Committee reviewed, Board of Directors approved the results and release at meetings held 12th Aug 2026 | |
| 2 | 566 | Company operates mainly two segments: Woven Sack Division and Woven Label Division | |
| 3 | 567 | Figures for corresponding previous quarter/year regrouped/reclassified whenever necessary for comparability | |

---

## 11. CONSOLIDATED UNAUDITED FINANCIAL RESULTS — every line item (lines 668-727)

| Sr | Line | Particular | Flags |
|----|------|------------|-------|
| 1 | 668 | Revenue From Operation | |
| 2 | 669 | Other Income | |
| 3 | 670 | Total Income (1+2) | |
| 4 | 671 | Expenditure (header) | |
| 4a | 672 | a) Cost of Material Consumed | |
| 4b | 673 | b) Changes in inventories of finished goods, WIP | note: standalone P&L has a separate "Purchase of Stock in Trade" sub-line not present here — DROPPED_LINE_VS_STANDALONE |
| 4c | 674 | c) Employees Benefits Expenses | |
| 4d | 675 | d) Finance Costs | |
| 4e | 676 | e) Depreciation & amortisation Expenses | |
| 4f | 677 | f) Other Expenses | |
| — | 678 | Total Expenditure (subtotal) | |
| 5 | 679 | Profit before exceptional items and tax (3-4) | |
| 6 | 680 | Exceptional Items | DATA_QUALITY (Q1 FY27 column blank rather than explicit dash) |
| — | 681 | Share of Profit/(Loss) of Joint Venture using Equity Method | DATA_QUALITY (FY column blank); UNNAMED_ENTITY (JV not identified anywhere in filing) |
| 7 | 682 | Profit/(Loss) before tax (5-6) | |
| 8 | 683 | Tax Expenses (header) | |
| 8a | 684 | a) Current Tax | |
| 8b | 685 | b) Tax for Earlier Years | ZERO_STANDING (dash/blank all periods) |
| 8b(dup) | 687 | b) Deferred Tax (Income)/Expense | DUPLICATE_LABEL ("b" reused) |
| 9 | 688 | Profit (Loss) for period from continuing operations (7-8) | |
| 10 | 689 | Profit (Loss) from discontinuing operations before tax | ZERO_STANDING (blank/dash all periods) |
| 11 | 690 | Tax expense of discontinuing operations | ZERO_STANDING (blank/dash all periods) |
| 12 | 691 | Profit/(loss) from Discontinuing operations after tax (10-11) | ZERO_STANDING (dash all periods) |
| 13 | 692 | Profit/(Loss) for the period (9+12) | |
| 14 | 693 | Other Comprehensive Income (header) | |
| 14a | 694 | Items not reclassified subsequently to P&L | |
| 14a-i | 695 | Remeasurement gain/(loss) of Defined Benefit Plan | |
| 14a-ii | 696 | Income tax related to Remeasurement gain/(loss) of DBP | |
| 14a-iii | 697-698 | Net change (Loss)/Gain in FV of investment in equity instruments | |
| 14a-iv | 699 | Income tax related to Net change in FV of investment in equity instruments | |
| 14b | 700 | Items to be reclassified subsequently to P&L | ZERO_STANDING (blank all periods) |
| 14b-i | 701 | Income tax relating to items reclassified to P&L | ZERO_STANDING (dash/blank all periods) |
| — | 702 | Other Comprehensive Income, net of tax (subtotal) | |
| 15 | 703 | Total Comprehensive Income for the period (13+14) | |
| 16 | 704 | Net Profit Attributable to: (header) | |
| 16a | 705 | a) Owners of the Company | |
| 16b | 706 | b) Non-Controlling Interest | |
| — | 707 | Other Comprehensive Income attributable to: (sub-header) | |
| 16c | 708 | a) Owners of the Company | |
| 16d | 710 | b) Non-Controlling Interest (wraps across page break to page 17) | |
| — | 711 | Total comprehensive income attributable to: (sub-header) | |
| 16e | 712 | a) Owners of the Company | |
| 16f | 713 | b) Non-Controlling Interest | |
| 17 | 714 | Paid-up Equity Shares Capital (FV Rs 10) | |
| 18 | 715 | Other Equity excluding revaluation reserve | ZERO_STANDING (no value printed in any column) |
| 19 | 716-717 | EPS (Continuing Operations) (header) | |
| 19a | 718 | (a) Basic | |
| 19b | 719 | (b) Diluted | |
| 20 | 720-721 | EPS (Discontinuing Operations) (header) | |
| 20a | 722 | (a) Basic | ZERO_STANDING (blank all periods) |
| 20b | 723 | (b) Diluted | ZERO_STANDING (blank all periods) |
| 21 | 724-725 | EPS (Continuing & Discontinuing Operations) (header) | |
| 21a | 726 | (a) Basic | |
| 21b | 727 | (b) Diluted | |

Consolidated P&L: **54 rows enumerated, 9 ZERO_STANDING**.

## 12. CONSOLIDATED SEGMENT INFORMATION — every line item (lines 748-782)

| Sr | Line | Particular | Flags |
|----|------|------------|-------|
| 1 | 748 | Segment Revenue (header) | |
| 1a | 749 | Woven Sacks Division | |
| 1b | 750 | Label Division | |
| — | 751 | Total | |
| — | 752-753 | Less: Inter Segment Revenue | ZERO_STANDING (dash all 4 periods) |
| — | 754 | Net Sales/Income from Operations | |
| 2 | 755-757 | Segment Results — Profit before Interest & Tax incl. Extraordinary Items (header) | |
| 2a | 758 | Woven Sacks Division | |
| 2b | 759 | Label Division | |
| — | 760 | Total | |
| i | 761-762 | Less: Interest | |
| — | 763 | Profit before Tax | |
| ii | 764 | Add: Share of Profit/(Loss) of Joint Venture using Equity Method | UNNAMED_ENTITY (same unnamed JV as consolidated P&L line 681); DATA_QUALITY (FY col blank) |
| iii | 765 | Less: Provision for Tax/Deferred Tax (Income)/Expense | |
| iv | 766 | Other Comprehensive/unallocable Income | |
| — | 767 | Net Profit | |
| 3 | 768 | Segment Assets (header) | |
| 3a | 769 | (a) Woven Sacks Division | |
| 3b | 770 | (b) Label Division | |
| 3c | 771 | (c) Unallocated | |
| — | 772 | Total (unlabeled subtotal row) | |
| 4 | 773 | Segment Liabilities (header) | |
| 4a | 774 | (a) Woven Sacks Division | |
| 4b | 775 | (b) Label Division | |
| 4c | 776 | (c) Unallocated | |
| — | 777 | Total (unlabeled subtotal row) | |

Consolidated Segment: **26 rows enumerated, 1 ZERO_STANDING**.

### Consolidated Segment — Notes (lines 779-782)

| Note | Line | Content | Flags |
|------|------|---------|-------|
| 1 | 779-780 | Audit Committee reviewed, Board of Directors approved the results and release at meetings held 12th Aug 2026 | OCR renders note number "1" as garbled "N" |
| 2 | 781 | Company operates mainly two segments: Woven Sack Division and Woven Label Division | |
| 3 | 782 | Figures for corresponding previous quarter/year regrouped/reclassified whenever necessary for comparability | |

---

## 13. ENTITIES REFERENCED IN CONSOLIDATION (whole-document sweep)

| # | Line(s) | Entity | Relationship | Flags |
|---|---------|--------|--------------|-------|
| E1 | 626-635 | K P Woven Private Limited | Subsidiary; interim financials unaudited, furnished by Management, auditor's conclusion relies on that report (Other Matters para) | UNAUDITED_ENTITY |
| E2 | 107-109 | HCP Plastene Bulkpack PLT (Malaysia LLP) | Subsidiary — Board noted its dissolution this quarter | ENTITY_CHANGE (removed from group) |
| E3 | 681, 764 | Joint Venture (unnamed) | Equity-method JV; "Share of Profit/(Loss) of Joint Venture" appears in both consolidated P&L and segment tables with no entity name disclosed anywhere in the filing | UNNAMED_ENTITY |

No prior-quarter ledger was supplied for this run (PRIOR_LEDGER_PATH not provided), so the E2 dissolution and any
other entity-list changes could not be cross-checked against a prior list; flagged for A3/A4 to verify against
last quarter's filing if available.

---

## SUMMARY OF FLAGS RAISED

ZERO_STANDING (24 instances across the four financial tables) · DUPLICATE_LABEL (3 instances: standalone P&L
"b)" x2 twice over, consolidated P&L "b)" x2) · DUPLICATE_ROW_NUMBER (Annexure C, row 5 used twice) ·
NUMBERING_GAP (Board Outcome items 6-9 unnumbered) · ANNEXURE_MISMATCH (item 10a cites Annexure C, likely should
be Annexure D) · UNNUMBERED_ITEM (4 board actions, items 6-9) · SHORT_MEETING (20-minute board meeting) ·
ENTITY_CHANGE (Malaysia LLP subsidiary dissolved) · UNAUDITED_ENTITY (K P Woven Pvt Ltd interim financials
management-furnished, not independently reviewed) · UNNAMED_ENTITY (equity-method JV never named) ·
DATA_QUALITY (blank vs dash inconsistency in Exceptional Items / JV share rows, consolidated P&L) ·
DROPPED_LINE_VS_STANDALONE ("Purchase of Stock in Trade" sub-line present in standalone Expenditure breakup,
absent in consolidated breakup) · MISSING_VALUE ("Other Equity excluding revaluation reserve" printed as a bare
header row with no value in any of the 4 columns, both standalone and consolidated).

```yaml
stage: A2-enumerator
company: "526717"
quarter: "q1fy27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "runs/526717-q1fy27/work/ledger_results_526717_q1fy27.md"
counts:
  notes: 6
  line_items: 149
  zero_standing: 24
  agenda_items: 18
  auditor_paras: 9
  entities: 3
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, DUPLICATE_LABEL, DUPLICATE_ROW_NUMBER, NUMBERING_GAP, ANNEXURE_MISMATCH, UNNUMBERED_ITEM, SHORT_MEETING, ENTITY_CHANGE, UNAUDITED_ENTITY, UNNAMED_ENTITY, DATA_QUALITY, DROPPED_LINE_VS_STANDALONE, MISSING_VALUE]
gate_a2: pass
mismatch_note: ""
```
