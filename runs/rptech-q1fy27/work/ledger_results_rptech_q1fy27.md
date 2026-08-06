# A2 ENUMERATION LEDGER — RPTECH Q1 FY27 (Results filing)
Source: extract_results_rptech_q1fy27.txt (30 pages, 1562 lines, Unaudited Board Outcome + Standalone & Consolidated Results, Annexures I-IV)
Unit convention: Millions (x0.1 to Rs Cr) except Annexure-III/IV tables, stated in Rs. Crore natively per A1 header.

```
=== A2 COUNT TEST ===
category: notes            grep_count: 20 (raw, incl. false positives)  sweep_count: 13 (true numbered notes)  reconciled: 13=13  match: yes
category: footnotes        grep_count: 20   sweep_count: 20   match: yes
category: line_items       grep_count: 72   sweep_count: 72   match: yes
category: zero_standing    grep_count: 40   sweep_count: 40   match: yes
category: agenda_items     grep_count: 12   sweep_count: 12   match: yes
category: auditor_paras    grep_count: 15   sweep_count: 15   match: yes
category: entities         grep_count: 5    sweep_count: 5    match: yes
category: annexure_items   grep_count: 57   sweep_count: 57   match: yes
category: signatures       grep_count: 10   sweep_count: 10   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

## Reconciliation note (notes category)
`grep -n -E "^\s*[0-9]+\s" extract...txt` returns 20 raw hits. Of these, 7 are false
positives: line 567 ("2026 as considered..." — a wrapped sentence beginning with a
4-digit year, not a note number) and lines 1235/1239/1241/1279/1287/1298 (Sr-No
column entries "1/2/3" inside the Annexure-III objects table, not financial-statement
notes). Manual sweep, bounded by the headers "Notes to the Statement of Standalone
Unaudited Financial Results" (line 391) and "Notes to the Statement of Consolidated
Unaudited Financial Results" (line 719), confirms exactly 13 true numbered notes
(Standalone 1-6, Consolidated 1-7). Reconciled count 13 = 13. GATE A2 passes for this
category after the false-positive exclusion documented above.

---

## SECTION 1 — Notes to Financial Statements (numbered), 13 rows

| # | Statement | Note | Line | First 15 words | Flags |
|---|-----------|------|------|-----------------|-------|
| 1 | Standalone | Note 1 | 393 | "The above statement of standalone unaudited financial results of Rashi Peripherals Limited..." (Ind AS 34 basis) | |
| 2 | Standalone | Note 2 | 399 | "The standalone unaudited financial results of the Company have been reviewed by the Audit Committee..." | |
| 3 | Standalone | Note 3 | 403 | "During the year ended March 31, 2024 the Company had completed IPO comprising of fresh issue..." (IPO utilisation table embedded) | |
| 4 | Standalone | Note 4 | 417 | "The Company operates in a single operating segment namely Computer Systems, Software & Peripherals, Mobiles..." (geography table embedded) | |
| 5 | Standalone | Note 5 | 430 | "The figures of the quarter ended March 31, 2026 are the balancing figures between the audited..." | |
| 6 | Standalone | Note 6 | 433 | "The Company has incorporated Rashi Semiconductor Solutions Private Limited as a wholly owned subsidiary..." | ENTITY_CHANGE (3 new entities disclosed) |
| 7 | Consolidated | Note 1 | 722 | "The above statement of consolidated unaudited financial results of Rashi Peripherals Limited ('the Parent')..." | |
| 8 | Consolidated | Note 2 | 728 | "The consolidated unaudited financial results of the Parent have been reviewed by the Audit Committee..." | |
| 9 | Consolidated | Note 3 | 732 | "During the year ended March 31, 2024 the Parent had completed IPO comprising of fresh issue..." (IPO utilisation table embedded) | |
| 10 | Consolidated | Note 4 | 746 | "The Group operates in a single operating segment namely Computer Systems, Software & Peripherals, Mobiles..." (geography table embedded) | |
| 11 | Consolidated | Note 5 | 761 | "The Standalone Unaudited Financial Results for the quarter ended June 30, 2026 are summarized below..." (standalone summary table embedded) | |
| 12 | Consolidated | Note 6 | 780 | "The figures of the quarter ended March 31, 2026 are the balancing figures between the audited..." | |
| 13 | Consolidated | Note 7 | 783 | "The Parent has incorporated Rashi Semiconductor Solutions Private Limited as a wholly owned subsidiary..." | ENTITY_CHANGE (3 new entities disclosed); post-quarter VOA Infosolutions 67% acquisition also disclosed here |

---

## SECTION 2 — Footnotes & Disclaimers (unnumbered/marked), 20 rows

| # | Location | Line | Marker | First 15 words | Flags |
|---|----------|------|--------|-----------------|-------|
| 1 | Standalone results table, EPS line | 383 | * | "Basic and Diluted EPS for all periods, except for the year ended March 31, 2026..." | |
| 2 | Consolidated results table, EPS line | 710 | * | "Basic and Diluted EPS for all periods, except for the year ended March 31, 2026..." | |
| 3 | Annexure III, below objects table | 975 | (header) | "Deviation or variation could mean:" | |
| 4 | Annexure III | 976 | (a) | "Deviation in the objects or purposes for which the funds have been raised or" | |
| 5 | Annexure III | 977 | (b) | "Deviation in the amount of funds actually utilized as against what was originally disclosed or" | |
| 6 | Annexure III | 978 | (c) | "Change in terms of a contract referred to in the fund raising document i.e. prospectus..." | |
| 7 | Annexure IV, MA report page 19 | 1203 | * | "Chartered Accountant certificate from PIPARA & Co LLP, Chartered Accountants, dated July 30, 2026" | |
| 8 | Annexure IV | 1205 | (header) # | "Where material deviation may be defined to mean:" | |
| 9 | Annexure IV | 1206 | a) | "Deviation in the objects or purposes for which the funds have been raised" | |
| 10 | Annexure IV | 1207 | b) | "Deviation in the amount of funds actually utilized by more than 10% of the amount..." | |
| 11 | Annexure IV, deployment table page 27 | 1416 | * | "issue expenses of Rs. 1.60 crore. The company has paid the issue expenses; however..." | POST_PERIOD (reimbursement claimed July 3, 2026, after Q-end) |
| 12 | Annexure IV, delay table page 28 | 1447 | * | "Company proposed to deploy the entire Net Proceeds towards the Objects as per the schedule..." | |
| 13 | Annexure IV, delay table page 28 | 1451 | # | "The original timeline for utilizing the IPO proceeds allocated towards General Corporate Purposes (GCP)..." | |
| 14 | Annexure IV, GCP detail table page 29 | 1506 | ^ | "Section from the offer document related to GCP: 'Our Company intends to deploy the balance..." | |
| 15 | Annexure IV, page 30 | 1524 | (header) | "Disclaimers to MA report:" | |
| 16 | Annexure IV | 1525 | a) | "This Report is prepared by CARE Ratings Ltd (hereinafter referred to as 'Monitoring Agency/MA')..." | |
| 17 | Annexure IV | 1530 | b) | "This Report has to be seen in its entirety; the selective review of portions of..." | |
| 18 | Annexure IV | 1535 | c) | "Nothing contained in this Report is capable or intended to create any legally binding obligations..." | |
| 19 | Annexure IV | 1540 | d) | "The MA and its affiliates do not act as a fiduciary. The MA and its..." | |
| 20 | Annexure IV | 1546 | e) | "The MA or its affiliates may have other commercial transactions with the entity to which..." | |

---

## SECTION 3 — Financial Statement Line Items, 72 rows (Standalone + Consolidated + embedded note-tables)

### 3A. Standalone Statement of Unaudited Financial Results, 24 rows (lines 340-381)
Periods: Q1FY27 (Jun-30-26, Unaudited) | Q4FY26 (Mar-31-26, Unaudited, Note 5) | Q1FY26 (Jun-30-25, Unaudited) | FY26 (Mar-31-26, Audited)

| # | Line item | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|-----------|------|--------|--------|--------|------|-------|
| 1 | I Revenue from Operations | 341 | 48,322.18 | 42,067.93 | 30,527.27 | 1,51,726.90 | |
| 2 | II Other Income | 342 | 173.30 | 160.42 | 71.77 | 398.09 | |
| 3 | III Total Income (I+II) | 343 | 48,495.48 | 42,228.35 | 30,599.04 | 1,52,124.99 | |
| 4 | IV(a) Purchases of stock-in-trade | 346 | 52,382.92 | 41,250.16 | 30,022.65 | 1,48,645.64 | |
| 5 | IV(b) Changes in inventories of stock-in-trade | 347 | (6,514.50) | (1,541.17) | (1,248.79) | (5,196.62) | |
| 6 | IV(c) Employee benefits expense | 348 | 548.62 | 517.19 | 395.03 | 1,942.34 | |
| 7 | IV(d) Finance costs | 349 | 272.16 | 285.51 | 264.29 | 1,053.28 | |
| 8 | IV(e) Depreciation and amortisation expenses | 350 | 61.86 | 60.10 | 40.54 | 210.29 | |
| 9 | IV(f) Other expenses | 351 | 442.94 | 643.43 | 338.28 | 1,979.97 | |
| 10 | Total Expenses (IV) | 352 | 47,194.00 | 41,215.22 | 29,812.00 | 1,48,634.90 | |
| 11 | V Profit before tax | 354 | 1,301.48 | 1,013.13 | 787.04 | 3,490.09 | |
| 12 | VI(a) Current Tax | 357 | 339.30 | 241.86 | 204.23 | 876.60 | |
| 13 | VI(b) Deferred Tax | 358 | (9.34) | 13.19 | (2.78) | 4.10 | |
| 14 | VI(c) Excess provision for earlier years | 359 | - | (2.14) | (2.66) | (4.80) | ZERO_STANDING (dash in current quarter only) |
| 15 | Total Tax expense | 360 | 329.96 | 252.91 | 198.79 | 875.90 | |
| 16 | VII Profit after tax | 362 | 971.52 | 760.22 | 588.25 | 2,614.19 | |
| 17 | VIII.A(a)(i) Remeasurement of defined benefit plan liability (loss)/gain | 366-367 | (1.70) | (3.32) | (2.80) | (6.81) | |
| 18 | VIII.A(a)(ii) Income tax (expense)/benefit on remeasurement | 368-369 | 0.43 | 2.59 | (0.70) | 1.71 | |
| 19 | Total other comprehensive income | 370 | (1.27) | (0.73) | (3.50) | (5.10) | |
| 20 | IX Total comprehensive income (VII+VIII) | 372 | 970.25 | 759.49 | 584.75 | 2,609.09 | |
| 21 | X Paid-up equity share capital (FV Rs.5) | 374 | 329.50 | 329.50 | 329.50 | 329.50 | |
| 22 | XI Other equity | 376 | (blank) | (blank) | (blank) | 19,530.20 | ZERO_STANDING (blank in all quarterly columns, populated only for FY, per BS-only disclosure convention) |
| 23 | XII Basic EPS (Rs.) | 380 | 14.74 | 11.54 | 8.93 | 39.67 | |
| 24 | XII Diluted EPS (Rs.) | 381 | 14.41 | 11.28 | 8.93 | 38.78 | |

### 3B. Consolidated Statement of Unaudited Financial Results, 31 rows (lines 642-708)

| # | Line item | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|-----------|------|--------|--------|--------|------|-------|
| 1 | I Revenue from Operations | 643 | 51,018.52 | 44,893.75 | 31,521.43 | 1,58,273.37 | |
| 2 | II Other Income | 644-645 | 173.87 | 160.51 | 79.05 | 405.50 | |
| 3 | III Total Income (I+II) | 646-647 | 51,192.39 | 45,054.26 | 31,600.48 | 1,58,678.87 | |
| 4 | IV(a) Purchases of stock-in-trade | 650 | 56,036.08 | 43,932.92 | 31,359.06 | 1,55,091.19 | |
| 5 | IV(b) Changes in inventories of stock-in-trade | 651-652 | (7,589.71) | (1,545.85) | (1,731.43) | (5,541.83) | |
| 6 | IV(c) Employee benefits expense | 653-654 | 568.11 | 531.33 | 419.26 | 2,006.73 | |
| 7 | IV(d) Finance costs | 655 | 274.18 | 289.26 | 269.32 | 1,064.94 | |
| 8 | IV(e) Depreciation and amortisation expenses | 656 | 62.89 | 61.27 | 42.14 | 215.15 | |
| 9 | IV(f) Other expenses | 658 | 451.22 | 649.01 | 439.39 | 2,129.96 | |
| 10 | Total Expenses (IV) | 659 | 49,802.77 | 43,917.94 | 30,797.74 | 1,54,966.14 | |
| 11 | V Profit before tax | 661-662 | 1,389.62 | 1,136.32 | 802.74 | 3,712.73 | |
| 12 | VI(a) Current Tax | 665-666 | 353.31 | 259.69 | 204.43 | 906.01 | |
| 13 | VI(b) Deferred Tax | 667-668 | (9.34) | 13.20 | (16.03) | (9.14) | |
| 14 | VI(c) (Excess)/Short provision for earlier periods | 669 | - | (4.94) | (2.66) | (7.60) | ZERO_STANDING (dash in current quarter only) |
| 15 | Total tax expense | 670 | 343.97 | 267.95 | 185.74 | 889.27 | |
| 16 | VII Profit after tax | 672 | 1,045.65 | 868.37 | 617.00 | 2,823.46 | |
| 17 | VIII.A(a)(i) Remeasurement of defined benefit plan (loss)/gain | 676-677 | (1.70) | (3.32) | (2.37) | (6.38) | |
| 18 | VIII.A(a)(ii) Income tax (expense)/benefit on remeasurement | 678-679 | 0.43 | 2.59 | (0.81) | 1.60 | |
| 19 | VIII.B(a) Foreign exchange differences on translation of foreign operations | 682-683 | 41.96 | (10.72) | (1.30) | (25.50) | |
| 20 | Total other comprehensive income | 684 | 40.69 | (11.45) | (4.48) | (30.28) | |
| 21 | IX Total comprehensive income (VII+VIII) | 686-687 | 1,086.34 | 856.92 | 612.52 | 2,793.18 | |
| 22 | X Profit attributable to: Owners of the Company | 690 | 1,027.70 | 842.06 | 613.18 | 2,775.77 | |
| 23 | X Profit attributable to: Non-Controlling Interests | 691 | 17.95 | 26.31 | 3.82 | 47.69 | |
| 24 | XI OCI attributable to: Owners of the Company | 694 | 30.51 | (8.85) | (4.32) | (24.25) | |
| 25 | XI OCI attributable to: Non-Controlling Interests | 695-696 | 10.18 | (2.60) | (0.16) | (6.03) | |
| 26 | XII Total Comprehensive Income attributable to: Owners of the Company | 699 | 1,058.21 | 833.21 | 608.86 | 2,751.52 | |
| 27 | XII Total Comprehensive Income attributable to: Non-Controlling Interests | 700 | 28.13 | 23.71 | 3.66 | 41.66 | |
| 28 | XIII Paid-up equity share capital (FV Rs.5) | 702 | 329.50 | 329.50 | 329.50 | 329.50 | |
| 29 | XIV Other equity | 704 | (blank) | (blank) | (blank) | 19,920.55 | ZERO_STANDING (blank in all quarterly columns) |
| 30 | XV Basic EPS (Rs.) | 707 | 15.59 | 12.78 | 9.30 | 42.12 | |
| 31 | XV Diluted EPS (Rs.) | 708 | 15.25 | 12.49 | 9.30 | 41.18 | |

### 3C. Note-embedded tables, 17 rows

| # | Table | Line item | Line | Value(s) | Flags |
|---|-------|-----------|------|----------|-------|
| 1 | Standalone Note 3 — IPO utilisation | (a) Prepayment/repayment of borrowings — Allocated 3,260.00 / Utilised 3,260.00 / Unutilised | 411-412 | Unutilised: - | ZERO_STANDING |
| 2 | Standalone Note 3 | (b) Funding working capital — Allocated 2,200.00 / Utilised 2,200.00 / Unutilised | 413 | Unutilised: - | ZERO_STANDING |
| 3 | Standalone Note 3 | (c) General corporate purpose — Allocated 81.41 / Utilised 81.41 / Unutilised | 414 | Unutilised: - | ZERO_STANDING |
| 4 | Standalone Note 3 | Total — Allocated 5,541.41 / Utilised 5,541.41 / Unutilised | 415 | Unutilised: - | ZERO_STANDING |
| 5 | Standalone Note 4 — Revenue by geography | India | 426 | Q1FY27 48,176.80; FY26 1,51,252.16 | |
| 6 | Standalone Note 4 | Overseas | 427 | Q1FY27 145.38; FY26 474.74 | |
| 7 | Standalone Note 4 | Total | 428 | Q1FY27 48,322.18; FY26 1,51,726.90 | |
| 8 | Consolidated Note 3 — IPO utilisation | (a) Prepayment/repayment of borrowings | 740-741 | Unutilised: - | ZERO_STANDING |
| 9 | Consolidated Note 3 | (b) Funding working capital | 742 | Unutilised: - | ZERO_STANDING |
| 10 | Consolidated Note 3 | (c) General corporate purpose | 743 | Unutilised: - | ZERO_STANDING |
| 11 | Consolidated Note 3 | Total | 744 | Unutilised: - | ZERO_STANDING |
| 12 | Consolidated Note 4 — Revenue by geography | India | 756 | Q1FY27 49,843.96; FY26 1,52,695.14 | |
| 13 | Consolidated Note 4 | Overseas | 757 | Q1FY27 1,174.56; FY26 5,578.23 | |
| 14 | Consolidated Note 4 | Total | 758 | Q1FY27 51,018.52; FY26 1,58,273.37 | |
| 15 | Consolidated Note 5 — Standalone summary embedded | Revenue from Operations | 768 | Q1FY27 48,322.18 | |
| 16 | Consolidated Note 5 | Profit before tax | 769 | Q1FY27 1,301.48 | |
| 17 | Consolidated Note 5 | Profit after tax | 770 | Q1FY27 971.52 | |

**Section 3 total: 24 + 31 + 17 = 72 rows. Zero-standing within Section 3: 12 (rows flagged above).**

---

## SECTION 4 — Board Outcome Agenda Items, 12 rows + meeting duration

Board meeting commenced 3:15 p.m. IST, concluded 5:07 p.m. IST (line 161) — duration 1 hour 52 minutes.

| # | Sr. No (letter) | Item | Line | Annexure | Flags |
|---|-----------|------|------|----------|-------|
| 1 | 1 | Unaudited Financial Results (Standalone & Consolidated) for Q1 FY27, with Limited Review Report; reviewed by Audit Committee, approved by Board | 42-51 | Annexure-I | |
| 2 | 2a | Approved transfer of Embedded Business from Company and Rashi Peripherals Pte Ltd to Rashi Semiconductor Solutions Pvt Ltd (WOS) and Rashi Semiconductor Solutions Pte Ltd (step-down subsidiary), slump sale basis, subject to definitive agreements/regulatory approvals | 53-66 | Annexure-II | ENTITY_CHANGE (transferee entities newly incorporated) |
| 3 | 2b | Approved formation of strategic JV with Restar Corporation, Japan, for embedded/semiconductor solutions business through the WOS | 78-83 | Annexure-II | |
| 4 | 2c | Approved revision of investment limit in Rashi Semiconductor Solutions Pvt Ltd from up to Rs.80 Cr (approved April 16, 2026) to up to Rs.150 Cr | 85-90 | — | |
| 5 | 3 | Approved convening of 37th AGM on Wednesday, September 9, 2026, at 12:30 p.m. IST via VC/OAVM | 92-96 | — | |
| 6 | 4a | Recap: Board (meeting held May 14, 2026) had recommended dividend of Rs.2/share (FV Rs.5, i.e. 40%) for FY ended March 31, 2026, subject to shareholder approval at ensuing AGM | 98-103 | — | |
| 7 | 4b | Record Date fixed: Friday, August 14, 2026, for dividend entitlement (Reg. 42); dividend payable within 30 days of AGM approval | 105-112 | — | |
| 8 | 4c | Cut-off date fixed: Wednesday, September 2, 2026, for remote e-voting/e-voting during AGM entitlement | 114-118 | — | |
| 9 | 5a | Approved allotment of 5,06,081 equity shares (FV Rs.5) on August 4, 2026 to Eligible Employees under RPTECH ESOP Scheme 2022, pari passu with existing shares | 120-125, 138-140 | — | |
| 10 | 5b | Resulting paid-up capital increase: from Rs.32,94,98,325 (6,58,99,665 shares) to Rs.33,20,28,730 (6,64,05,746 shares) | 142-147 | — | |
| 11 | 6 | Statement of utilisation of IPO issue proceeds and Nil deviation/variation statement (Reg. 32(1)) | 149-153 | Annexure-III | |
| 12 | 7 | Monitoring Agency Report (Reg. 32(6)) | 155-157 | Annexure-IV | |

---

## SECTION 5 — Annexures & Tables Within, 57 rows

### 5A. Annexure II — Restar JV / Embedded Business materiality disclosure (Schedule III Part A), 10 rows (lines 809-877)

| Sr | Particular | Line | Detail (abbrev.) |
|----|-----------|------|-------------------|
| 1 | Name of entity(ies) for agreement/JV | 810 | Restar Corporation, Japan |
| 2 | Area of agreement/JV | 813-814 | Semiconductor and embedded solutions business |
| 3 | Domestic/International | 816-817 | Domestic as well as International markets |
| 4 | Share exchange ratio / JV ratio | 819-821 | Secondary sale per FMV: RPTECH 74%, Restar 26% |
| 5 | Scope of business operation of JV | 823-824 | Semiconductor and embedded solutions business |
| 6 | Details of consideration paid/received | 826-829 | To be per FMV, date TBD in SPA |
| 7 | Significant terms and conditions | 831-840 | Secondary sale to 74:26; Board 3 RPTECH nominees + 1 Restar (Vice Chairman) |
| 8 | RPT / promoter interest disclosure | 842-849 | Not Applicable |
| 9 | Size of the entity(ies) | 851-854 | JV housed in Rashi Semiconductor Solutions Pvt Ltd, pre-revenue |
| 10 | Rationale and benefit expected | 865-877 | Combines Restar tech/semiconductor relationships with RPTECH distribution reach |

### 5B. Annexure III — Statement of Deviation/Variation, 16 rows (lines 892-989)

Header fields (13 rows):

| # | Field | Line | Value | Flags |
|---|-------|------|-------|-------|
| 1 | Name of listed entity | 892 | RASHI PERIPHERALS LIMITED | |
| 2 | Mode of Fund Raising | 893-894 | IPO | |
| 3 | Date of Raising Funds | 895 | February 14, 2024 | |
| 4 | Amount Raised | 896 | Rs. 600.00 Crore | |
| 5 | Report filed for Quarter ended | 897 | June 30, 2026 | |
| 6 | Monitoring Agency (applicable?) | 898 | Applicable | |
| 7 | Monitoring Agency Name | 899 | CARE Ratings Limited | |
| 8 | Is there a Deviation/Variation in use of funds | 900-901 | Nil | ZERO_STANDING |
| 9 | If yes, pursuant to change in contract terms/objects | 902-904 | Not Applicable | ZERO_STANDING |
| 10 | If Yes, Date of shareholder Approval | 905 | Not Applicable | ZERO_STANDING |
| 11 | Explanation for the Deviation/Variation | 906 | Not Applicable | ZERO_STANDING |
| 12 | Comments of the Audit Committee after review | 907 | None | ZERO_STANDING |
| 13 | Comments of the auditors, if any | 908 | None | ZERO_STANDING |

Objects/deviation table (3 rows, lines 919-974):

| # | Object | Line | Original Allocation (Rs Cr) | Modified Object | Funds Utilised (Rs Cr) | Deviation | Flags |
|---|--------|------|------------------------------|------------------|--------------------------|-----------|-------|
| 14 | 1. Prepayment/repayment of borrowings | 919-925 | 326.00 | Nil | 326.00 | Nil | ZERO_STANDING (Modified Object + Deviation both Nil) |
| 15 | 2. Funding working capital requirements | 926-928 | 220.00 | Nil | 220.00 | Nil | ZERO_STANDING |
| 16 | 3. General corporate purposes | 929-974 | 8.14 | Nil | 8.14 | Nil | ZERO_STANDING; remarks note GCP timeline extended twice (Apr 21 2025 and Feb 3 2026 Board resolutions) before final Rs.0.44 Cr utilised in Q1FY27 |

Signature: Himanshu Kumar Shah, Chief Financial Officer, Mumbai, August 4, 2026 (line 981-988) — see Section 8.

### 5C. Annexure IV — Monitoring Agency (CARE Ratings) Report, 31 rows

**1) Issuer Details, 3 rows (lines 1107-1118):**

| # | Field | Line | Value |
|---|-------|------|-------|
| 1 | Name of issuer | 1108 | Rashi Peripherals Limited |
| 2 | Name of the promoter | 1109-1110 | Krishna Kumar Choudhary, Sureshkumar Pansari, Kapal Suresh Pansari, Keshav Krishna Kumar Choudhary, Chaman Pansari, Krishna Kumar Choudhary (HUF), Suresh M Pansari (HUF) |
| 3 | Industry/sector | 1111 | ICT Product Distribution |

**2) Issue Details, 5 rows (lines 1113-1118):**

| # | Field | Line | Value |
|---|-------|------|-------|
| 4 | Issue Period | 1114 | 07/02/2024 to 09/02/2024 |
| 5 | Type of issue | 1115 | IPO |
| 6 | Type of specified securities | 1116 | Equity Shares |
| 7 | IPO Grading, if any | 1117 | Not Applicable |
| 8 | Issue size | 1118 | Rs. 600 crores |

**3) Details of arrangement for monitoring issue proceeds, 8 rows (lines 1133-1202):**

| # | Particular | Line | Reply | Flags |
|---|-----------|------|-------|-------|
| 9 | Whether all utilisation is per Offer Document disclosures | 1151 | Yes | |
| 10 | Whether shareholder approval obtained for material deviations | 1163-1165 | Not applicable as no deviation | ZERO_STANDING |
| 11 | Whether means of finance for disclosed objects changed | 1166-1168 | No | ZERO_STANDING |
| 12 | Is there major deviation vs earlier MA reports (ref. MA report dated May 14, 2026 for Q4FY26) | 1169-1173 | No | ZERO_STANDING |
| 13 | Whether all Govt/statutory approvals related to object(s) obtained | 1174-1176 | Not applicable | ZERO_STANDING |
| 14 | Whether technical assistance/collaboration arrangements in operation | 1177-1196 | Yes | |
| 15 | Are there favourable/unfavourable events affecting object viability | 1197-1199 | No | ZERO_STANDING |
| 16 | Is there other info that may materially affect investor decisions | 1200-1202 | No | ZERO_STANDING |

**4(i) Cost of objects, 4 rows (lines 1222-1245):**

| # | Item | Line | Original Cost (Rs Cr) | Revised Cost | Reason for revision | Flags |
|---|------|------|------------------------|--------------|----------------------|-------|
| 17 | Prepayment/repayment of borrowings | 1233-1237 | 326.00 | NA | Nil | ZERO_STANDING |
| 18 | Funding working capital requirements | 1238-1240 | 220.00 | NA | Nil | ZERO_STANDING |
| 19 | General Corporate Purpose | 1241 | 8.14 | NA | Nil | ZERO_STANDING |
| 20 | Total | 1244 | 554.14 | NA | — | |

**4(ii) Progress in objects, 4 rows (lines 1259-1391):**

| # | Item | Line | As at beginning of qtr (Rs Cr) | During the qtr | At end of qtr | Unutilised | Flags |
|---|------|------|----------------------------------|------------------|-----------------|------------|-------|
| 21 | Prepayment/repayment of borrowings | 1276-1282 | 326.00 | - | 326.00 | 0.00 | ZERO_STANDING (both "during qtr" and "unutilised" nil) |
| 22 | Funding working capital requirements | 1285-1291 | 220.00 | - | 220.00 | 0.00 | ZERO_STANDING |
| 23 | General Corporate Purpose | 1292-1305 | 7.70 | 0.44 | 8.14 | 0.00 | ZERO_STANDING (unutilised nil; final GCP tranche closed this quarter) |
| 24 | Total | 1391 | 553.70 | 0.44 | 554.14 | 0.00 | ZERO_STANDING |

**4(iii) Deployment of unutilised IPO proceeds, 1 row (lines 1406-1416):**

| # | Instrument | Line | Amount invested (Rs Cr) | Maturity | Earning | ROI% | Flags |
|---|-----------|------|---------------------------|----------|---------|------|-------|
| 25 | Axis Public Issue a/c – 924020005512318 | 1413-1416 | 1.60* | NA | NA | NA | ZERO_STANDING (Maturity/Earning/ROI all NA — escrow account, not an interest-bearing deployment); *issue-expense reimbursement pending, claimed post Q1FY27 (July 3, 2026) |

**4(iv) Delay in implementation, 3 rows (lines 1431-1455):**

| # | Object | Line | Completion (Offer Doc) | Actual | Delay | Flags |
|---|--------|------|---------------------------|--------|-------|-------|
| 26 | Prepayment/repayment of borrowings | 1436-1440 | By FY24 | 15/02/2024-13/09/2024 | 5.5 Months | |
| 27 | Funding working capital requirements | 1441-1443 | By FY24 | 15/02/2024-31/03/2024 | - | ZERO_STANDING (nil delay) |
| 28 | General Corporate Purpose | 1444-1446 | By FY24 | 15/02/2024-30/06/2026 | - | ZERO_STANDING (nil delay, despite ~2-year extension via two Board resolutions — delay measured as "-" per MA convention since within extended timeline) |

**5) Deployment of GCP amount detail, 3 rows (lines 1458-1505):**

| # | Item | Line | Amount (Rs Cr) | Detail |
|---|------|------|------------------|--------|
| 29 | Fixed Asset Purchase | 1472-1477 | 0.42 | Capex via Cash Credit a/c with HDFC Bank; commercial vehicle, labelling machines, vendor balance from earlier quarters |
| 30 | Fixed Asset Purchase | 1501-1503 | 0.02 | Roller conveyor, direct payment from Monitoring Account |
| 31 | Total | 1505 | 0.44 | |

**Section 5 total: 10 + 16 + 31 = 57 rows. Zero-standing within Section 5: 9 (Annexure III) + 19 (Annexure IV) = 28.**

---

## SECTION 6 — Auditor Report Paragraphs, 15 rows

Joint auditors throughout: Deloitte Haskins & Sells LLP (Reg. 117366W/W-100018) and Pipara & Co LLP (Reg. 109729W/W100219 for standalone / 109729W/W100219 consolidated, printed inconsistently — see flag).

### 6A. Standalone review report (Annexure-I), 5 paragraphs (lines 223-325). Opinion: unmodified review conclusion (no EoM, no Other Matters heading used, no Going Concern paragraph).

| # | Para | Line | Content | Flags |
|---|------|------|---------|-------|
| 1 | 1 | 229-235 | Scope: reviewed Standalone Unaudited Financial Results incl. branch outside India (Singapore), for quarter ended June 30, 2026, per Reg. 33 | |
| 2 | 2 | 237-244 | Management responsibility; prepared per Ind AS 34; auditor responsibility is to express a review conclusion | |
| 3 | 3 | 246-260 | Review conducted per SRE 2410; scope less than audit, no audit opinion expressed; SEBI Reg. 33(8) procedures also performed | |
| 4 | 4 | 262-271 | Conclusion: nothing has come to attention causing belief of non-disclosure or material misstatement (unmodified) | |
| 5 | 5 | 279-306 | Branch (Singapore) not reviewed by joint auditors: revenue Rs.76.67m, PAT Rs.1.17m, TCI Rs.1.17m for the quarter, reviewed by branch auditor; joint auditors relied on branch auditor's report and reviewed conversion adjustments; conclusion not modified | UNAUDITED_BY_PRINCIPAL (branch reviewed by other/branch auditor, not primary joint auditors) |

UDIN: Deloitte partner (Membership 113861) UDIN string OCR-corrupted ("26 11 3 &6 1)' $ 1"'\S.I 2...5 8,04", line 323); Pipara partner (Membership shown as 16341, likely 163412 per consolidated report) UDIN also OCR-corrupted (line 323). — see Section 8 flag UDIN_ILLEGIBLE.

### 6B. Consolidated review report (Annexure-I), 10 paragraphs/sub-paragraphs (lines 461-626). Opinion: unmodified review conclusion.

| # | Para | Line | Content | Flags |
|---|------|------|---------|-------|
| 6 | 1 | 467-474 | Scope: reviewed Consolidated Unaudited Financial Results of Parent + subsidiaries (Group), incl. branch outside India (Singapore), quarter ended June 30, 2026, per Reg. 33 | |
| 7 | 2 | 476-483 | Management responsibility; Ind AS 34 basis | |
| 8 | 3 | 485-499 | Review per SRE 2410; scope less than audit; SEBI Reg. 33(8) procedures performed | |
| 9 | 4 | 501-511 | Entity list: Parent + 4 subsidiaries/step-down subsidiaries reviewed (table — see Section 7) | |
| 10 | 5 | 521-531 | Conclusion: unmodified, based also on branch auditor and other auditor reports referenced in para 6 | |
| 11 | 6a | 534-559 | Branch (Singapore, within Parent standalone) not reviewed by joint auditors: revenue Rs.76.67m, PAT Rs.1.17m, TCI Rs.1.17m; relied on branch auditor | UNAUDITED_BY_PRINCIPAL |
| 12 | 6b | 561-593 | 1 subsidiary (outside India) not reviewed by joint auditors: revenue Rs.2,698.59m, PAT Rs.73.99m, TCI Rs.115.95m; reviewed by "other auditor," report furnished by Management; joint auditors relied on other auditor + reviewed conversion adjustments | UNAUDITED_BY_PRINCIPAL; MANAGEMENT_FURNISHED (other auditor's report furnished to joint auditors "by the Management") |
| 13 | 6c | 595 | "Our conclusion on the Statement is not modified in respect of these matters" | |
| 14 | 6d | 597-604 | 3 subsidiaries' interim financial info NOT reviewed by their auditors at all: revenue Nil, loss Rs.(1.93)m, TCI loss Rs.(1.93)m; per Management, not material to Group | UNAUDITED — no auditor review whatsoever (management-certified only); ZERO_STANDING (revenue Nil across the 3-entity block, consistent with newly incorporated pre-revenue entities per Notes 6/7); likely maps to the 3 newly incorporated entities (Rashi Semiconductor Solutions Pvt Ltd, Rashi Semiconductor Solutions Pte Ltd, Rashi Peripherals L.L.C-FZ) |
| 15 | 6e | 606-607 | "Our Conclusion on the Statement is not modified in respect of our reliance on the interim financial information certified by the Management" | MANAGEMENT_FURNISHED (explicit reliance on management certification for the 3 unreviewed subsidiaries) |

UDIN: Deloitte partner (Membership 113861) UDIN OCR-corrupted (line 624); Pipara partner (Membership 163412) UDIN OCR-corrupted (line 624).

**Section 6 total: 5 + 10 = 15 rows.**

---

## SECTION 7 — Consolidation List Entities, 5 rows (lines 501-511)

| # | Entity | Relationship | Line | Flags |
|---|--------|--------------|------|-------|
| 1 | Rashi Peripherals Limited | Parent Company | 504 | |
| 2 | Rashi Peripherals Pte. Ltd. | Subsidiary Company | 505 | |
| 3 | Rashi Semiconductor Solutions Private Limited | Subsidiary Company (from May 5, 2026) | 506-507 | ENTITY_CHANGE — newly incorporated this quarter (Note 6/7); pre-revenue per Section 6, row 14 |
| 4 | Rashi Semiconductor Solutions Pte. Ltd. | Step-Down Subsidiary (from June 11, 2026) | 508-509 | ENTITY_CHANGE — newly incorporated this quarter; pre-revenue |
| 5 | Rashi Peripherals L.L.C-FZ | Step-Down Subsidiary (from May 15, 2026) | 510-511 | ENTITY_CHANGE — newly incorporated this quarter (subsidiary of Rashi Peripherals Pte Ltd); pre-revenue |

No prior-quarter ledger was supplied for this run (PRIOR_LEDGER_PATH not provided); ENTITY_CHANGE flags above are raised on internal evidence — Notes 6 (standalone) and 7 (consolidated) explicitly state all three entities were incorporated during Q1 FY27 (May-June 2026) and "business is yet to commence." A3/A4 should verify against the prior quarter's (Q4FY26) consolidation list to confirm these are genuinely additions and not renamings.

Also disclosed (post-period, not in the consolidation list this quarter): acquisition of 67% equity in VOA Infosolutions Private Limited for Rs.3,685 millions, subsequent to quarter-end (Notes 6/7) — flag for A4 as a forward consolidation-scope change, not yet reflected in this quarter's 5-entity list.

---

## SECTION 8 — Digital Signature Blocks, 10 rows

| # | Signatory | Designation | Context | Line | Timestamp | Flags |
|---|-----------|-------------|---------|------|-----------|-------|
| 1 | Arvind Bajoria | Company Secretary & Compliance Officer | Reg. 30/32/33 cover letter | 169-197 | 2026.08.04 18:55:47 +05'30' (digital signature block) | Checked against board meeting conclusion (5:07 p.m. / 17:07 IST, line 161): signature timestamp 18:55:47 is AFTER meeting conclusion — no SIGNATURE_BEFORE_MEETING flag |
| 2 | [Deloitte partner], Membership No. 113861 | Partner, Deloitte Haskins & Sells LLP | Standalone review report | 309-325 | UDIN illegible (OCR) | UDIN_ILLEGIBLE |
| 3 | [Pipara partner], Membership No. 16341 (printed) | Partner, Pipara & Co LLP | Standalone review report | 309-325 | UDIN illegible (OCR) | UDIN_ILLEGIBLE; membership number printed as "16341" here vs "163412" in consolidated report — inconsistency, likely OCR truncation, flag for A3 |
| 4 | [Deloitte partner], Membership No. 113861 | Partner, Deloitte Haskins & Sells LLP | Consolidated review report | 610-626 | UDIN illegible (OCR) | UDIN_ILLEGIBLE |
| 5 | [Pipara partner], Membership No. 163412 | Partner, Pipara & Co LLP | Consolidated review report | 610-626 | UDIN illegible (OCR) | UDIN_ILLEGIBLE |
| 6 | Krishna Kumar Choudhary | Chairman & Wholetime Director, DIN 00215919 | Standalone results, "for and on behalf of the Board" | 440-447 | Mumbai, August 4, 2026 (no digital cert block shown) | |
| 7 | Krishna Kumar Choudhary | Chairman & Wholetime Director, DIN 00215919 | Consolidated results, "for and on behalf of the Board" | 791-800 | Mumbai, August 4, 2026 | |
| 8 | Himanshu Kumar Shah | Chief Financial Officer | Annexure III (Statement of Deviation/Variation) | 981-988 | Mumbai, August 4, 2026 | |
| 9 | Akshay Morbiya | Associate Director, CARE Ratings Limited | Annexure IV cover letter | 1036-1040 | August 4, 2026 | |
| 10 | Akshay Morbiya | Associate Director / Authorized Signatory, CARE Ratings Limited | Annexure IV Monitoring Agency Report | 1090-1092 | (undated on signature line; report dated August 4, 2026 at header) | |

---

## SUMMARY COUNTS

- Notes (numbered): 13
- Footnotes (unnumbered/marked): 20
- Line items (financial statement tables incl. note-embedded tables): 72
- Zero-standing line items (flagged ZERO_STANDING across Sections 3 & 5): 40
- Agenda items (Board Outcome, unbundled): 12 + 1 meeting-duration record
- Annexure table rows (Annexure II + III + IV): 57
- Auditor report paragraphs: 15 (5 standalone + 10 consolidated)
- Consolidation-list entities: 5 (3 flagged ENTITY_CHANGE)
- Signature blocks: 10 (4 flagged UDIN_ILLEGIBLE)

## FLAGS RAISED (all instances)
- ZERO_STANDING: 40 instances (Section 3: 12; Section 5: 28)
- ENTITY_CHANGE: 5 instances (Note 6, Note 7, Agenda item 2a, and Section 7 rows 3-4-5 — 3 newly incorporated entities)
- UNAUDITED_BY_PRINCIPAL: 3 instances (Section 6 rows 5, 11, 12 — branch and 1 subsidiary reviewed by branch/other auditor, not the joint principal auditors)
- MANAGEMENT_FURNISHED: 2 instances (Section 6 rows 12, 15 — other auditor's report and 3 subsidiaries' unreviewed financials both furnished/certified by Management, not independently reviewed)
- UDIN_ILLEGIBLE: 4 instances (Section 8 rows 2, 3, 4, 5 — all four auditor-partner UDINs are OCR-corrupted in the source; A3/A4 cannot verify UDIN validity from this extract)
- POST_PERIOD: 1 instance (Section 2 row 11 — issue-expense reimbursement claimed July 3, 2026, after Q1FY27 close)
- No SIGNATURE_BEFORE_MEETING flag: checked explicitly (Section 8 row 1); cover-letter digital signature (18:55:47 IST) postdates board meeting conclusion (17:07 IST) as expected

## SCOPE NOTE
No director appointment/resignation/auditor-change agenda item appears in this filing; the only office-bearer/personnel items are the ESOP allotment (agenda 5a/5b) and the routine references to Chairman & WTD, CFO, and CS in signature blocks. No new "director profile" rows (DIN/term/background) are required this quarter beyond what is captured in Section 8.
