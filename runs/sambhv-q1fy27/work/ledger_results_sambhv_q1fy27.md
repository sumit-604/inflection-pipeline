# A2 ENUMERATION LEDGER — Sambhv Steel Tubes Ltd (SAMBHV) — Q1 FY27 — Results Filing

Source: `extract_results_sambhv_q1fy27.txt` (11 pages, 1944 extraction lines, unit convention Millions)
Prior-quarter ledger: NONE (first quarterly pipeline run for this ticker) — no ENTITY_CHANGE / DROPPED_ITEM diff possible this cycle.

OCR note (applies to all tables below): pages 6-7 (standalone statement) and pages 10-11 (consolidated
statement) print each cell twice per the source PDF's layout — a garbled OCR pass and a clean OCR pass
interleaved line-by-line. All values below are transcribed from the clean pass. Where the clean pass
itself was ambiguous, the value was cross-footed against the printed sub-totals in the same table (shown
as "[reconstructed, footed against Total row]") rather than estimated — this is arithmetic reconciliation
of a printed number, not an invented number.

```
=== A2 COUNT TEST ===
category: agenda_items      grep_count: 7    sweep_count: 7    match: yes
category: annexure_items    grep_count: 14   sweep_count: 14   match: yes
category: notes             grep_count: 14   sweep_count: 14   match: yes
category: line_items        grep_count: 62   sweep_count: 62   match: yes
category: zero_standing     grep_count: 6    sweep_count: 6    match: yes
category: auditor_paras     grep_count: 10   sweep_count: 10   match: yes
category: entities          grep_count: 3    sweep_count: 3    match: yes
category: signature_blocks  grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used (Bash, on extract file):
- `grep -n -E "^\s*[a-e]\.\s"` + `grep -n -i "commenced\|concluded"` → agenda_items
- `grep -n -i "Annexure"` + row-number anchors (`^\s*[1-8]\s+(Existing|Proposed|...)`, Annexure B `1..6` markers) → annexure_items
- `grep -n -i "notes to"` / numbered-note anchors (`^\s*[0-9]\s`) + `grep -n -E "^\s*[*#]"` for footnotes → notes
- Roman-numeral / lettered row-marker anchors (`^\s*(I|II|...|XII)\.|^\s*\([a-g]\)`) run separately over the
  standalone (lines 456-728) and consolidated (lines 1312-1710) statement ranges, de-duplicated for the
  garbled/clean OCR twin-passes → line_items
- `grep -n -i "Non Controlling Interests"` + `grep -n -i -E "xceptional"` + manual nil-across-all-periods
  check → zero_standing
- `grep -n -E "^\s*[0-9]\.\s*(We |This |We conducted|Based on)"` + `grep -n "We also"` → auditor_paras
- `grep -n -E "^\s*(i\.|il\.|u\.)\s*(Holding|Subsidiary)"` + standalone report scope sentence → entities
- `grep -n -i "digitally signed\|Managing Director\|DIN"` + `grep -n "Membership Number"` → signature_blocks

---

## TABLE 1 — Board Outcome Letter: Agenda Items & Meeting Times (lines 15-88)

| # | Item | Line(s) | Content (first 15 words / detail) | Flags |
|---|------|---------|-------------------------------------|-------|
| 1 | Agenda (a) — Results approval | 40-44 | Approved Unaudited Standalone and Consolidated Financial Results for quarter ended June 30, 2026 | |
| 2 | Agenda (b) — Limited Review Report approval | 45-49 | Approved 'Limited Review Report' on Unaudited Standalone and Consolidated Financial Results issued by Statutory Auditors | |
| 3 | Agenda (c) — 8MW captive solar plant | 51-55 | Approved setting up 8MW Captive Behind-The-Meter Solar Power Plant at Kuthrel, est. cost up to ₹250 mn; detail at Annexure A | |
| 4 | Agenda (d) — Director change | 56-64 | Board approved (on NRC recommendation) Bikash Agrawal (DIN 09231728) as Additional Director w.e.f. May 09, 2026; ceased SMP; detail at Annexure B | DATE_DISCREPANCY — see Table 3 row 3 |
| 5 | Agenda (e) — 9th AGM | 65-68 | Approved convening 9th AGM on Thursday, September 10, 2026 via VC/OAVM; notice to follow | |
| 6 | Board meeting — start time | 75 | "commenced on Monday, August 03, 2026 at 05:05 P.M" | |
| 7 | Board meeting — end time | 76 | "concluded at 06:20 P.M." — total meeting duration 1 hr 15 min | |

## TABLE 2 — Annexure A: 8MW Captive Solar Power Plant (lines 90-116), 8 rows

| S.No | Particulars | Line | Detail | Flags |
|------|-------------|------|--------|-------|
| 1 | Existing Capacity | 96 | Nil MW | ZERO_STANDING |
| 2 | Existing Capacity Utilization | 98-99 | N.A. (New Project) | |
| 3 | Proposed Additional Capacity | 100-101 | 8.0 MW (Phase I up to 3.2 MW; Phase II up to 4.8 MW) | |
| 4 | Total Capacity After Proposed Addition | 102-103 | 8.0 MW | |
| 5 | Period Within Which Capacity To Be Added | 104-106 | Phase I - FY2028; Phase II - FY2029 (subject to implementation schedule) | |
| 6 | Investment Proposed | 107-108 | ₹250 million (up to) | |
| 7 | Mode of Finance | 109-110 | Internal Accruals / Debt / Lease, as deemed fit | |
| 8 | Rationale | 111-116 | To meet power requirement of manufacturing facilities via captive rooftop solar, optimising power cost | |

## TABLE 3 — Annexure B: Director Change Disclosure — Bikash Agrawal (lines 118-142), 6 rows

| Sr.No | Disclosure Requirement | Line | Detail | Flags |
|-------|------------------------|------|--------|-------|
| 1 | Name | 124 | Mr. Bikash Agrawal | |
| 2 | Reason for change | 126-128 | Ceases to hold SMP position upon Director appointment, per Reg 16(1)(d) | |
| 3 | Date of Re-appointment & Term of Appointment | 130-134 | "cessation shall be effective from May 08, 2026, being the date on which the board...approved the appointment" | DATE_DISCREPANCY — Agenda item (d) (Table 1 row 4, line 58-59) states the Director appointment itself is effective May 09, 2026; this row states the board approval date / cessation-as-SMP effective date is May 08, 2026. Two different dates for what is described as a simultaneous appointment/cessation event; not reconciled anywhere in the filing |
| 4 | Brief Profile (in case of appointment) | 136 | Not Applicable | |
| 5 | Disclosure of relationships between directors | 137-139 | Not Applicable | |
| 6 | Information under BSE circular LIST/COMP/14/2018-19 | 140-142 | Not debarred from holding office of Director by SEBI or other authority | (row label garbled to "6s" in extract, content is item 6) |

## TABLE 4 — Standalone Statement of Unaudited Financial Results, Q1 FY27 (lines 456-681), clean-copy values
Columns: Q1 FY27 (Jun-30-2026, Unaudited) | Q4 FY26 (Mar-31-2026, Audited, Refer Note 4) | Q1 FY26 (Jun-30-2025, Unaudited) | FY26 (Mar-31-2026, Audited) — amounts in ₹ million

| # | Line item | Line(s) | Q1 FY27 | Q4 FY26 | Q1 FY26 | FY26 | Flags |
|---|-----------|---------|---------|---------|---------|------|-------|
| 1 | I(a) Revenue from operations | 474-480 | 7,321.73 | 6,853.10 | 5,586.29 | 24,132.43 | |
| 2 | I(b) Other income | 481-488 | 49.48 | 39.55 | 7.73 | 72.88 | |
| 3 | Total income (I) | 489-494 | 7,371.21 | 6,892.65 | 5,594.02 | 24,205.31 | |
| 4 | II(a) Cost of materials consumed | 496-502 | 5,292.75 | 5,126.52 | 3,681.53 | 17,383.77 | |
| 5 | II(b) Purchases of stock-in-trade | 503-508 | 72.67 | 82.00 | 61.76 | 163.41 | |
| 6 | II(c) Changes in inventories of stock-in-trade and finished goods | 509-517 | (164.04) | (401.32) | 171.37 | (328.03) | |
| 7 | II(d) Employee benefits expense | 518-525 | 375.21 | 359.67 | 289.89 | 1,344.18 | |
| 8 | II(e) Finance costs | 526-531 | 107.21 | 98.63 | 164.37 | 433.16 | |
| 9 | II(f) Depreciation and amortization expense | 532-538 | 125.30 | 120.70 | 120.03 | 485.08 | |
| 10 | II(g) Other expenses | 539-544 | 793.16 | 764.10 | 654.64 | 2,806.11 | |
| 11 | Total expenses (II) | 545-551 | 6,602.46 | 6,150.30 | 5,143.59 | 22,287.68 | |
| 12 | III. Profit before exceptional item and tax (I-II) | 553-560 | 768.75 | 742.35 | 450.43 | 1,917.63 | |
| 13 | IV. Exceptional item | 562-565 | — | — | — | — | ZERO_STANDING (nil all four periods) |
| 14 | V. Profit before tax (III-IV) | 566-572 | 768.75 | 742.35 | 450.43 | 1,917.63 | |
| 15 | VI(a) Current tax | 578-583 | 181.64 | 157.52 | 93.64 | 398.69 | |
| 16 | VI(b) Current tax on earlier year | 584-586 | — | (0.01) | 2.58 | 2.57 | nil in one period only, not standing-nil |
| 17 | VI(c) Deferred tax | 587-591 | 20.99 | 27.09 | 20.22 | 83.69 | |
| 18 | Total tax expense (VI) | 592-597 | 202.63 | 184.60 | 116.44 | 484.95 | |
| 19 | VII. Profit for the year (V-VI) | 599-606 | 566.12 | 557.75 | 333.99 | 1,432.68 | |
| 20 | VIII(a) Remeasurement gains/(losses) on defined benefit plans | 612-621 | (23.53) | 4.95 | 1.22 | 0.95 | |
| 21 | VIII(b) Income tax relating to above | 622-628 | 5.92 | (1.25) | (0.31) | (0.24) | |
| 22 | Other comprehensive income for the year, net of tax (VIII) | 629-635 | (17.61) | 3.70 | 0.91 | 0.71 | |
| 23 | IX. Total comprehensive income for the year (VII+VIII) | 637-644 | 548.51 | 561.45 | 334.90 | 1,433.39 | |
| 24 | X. Paid up Equity Share Capital | 646-652 | 2,946.71 | 2,946.71 | 2,410.02 | 2,946.71 | |
| 25 | XI. Other Equity | 654-657 | (blank) | (blank) | (blank) | 7,607.58 | Quarter columns intentionally blank (balance-sheet item disclosed for annual/audited column only — standard practice, not a nil transaction) |
| 26 | XII(a) Basic EPS (INR)** | 668-673 | 1.92 | 1.89 | 1.39 | 5.09 | |
| 27 | XII(b) Diluted EPS (INR)** | 674-678 | 1.92 | 1.89 | 1.39 | 5.09 | |

Footnote: ** "Not annualised for interim periods" (lines 679-681), qualifies row 26-27.

## TABLE 5 — Consolidated Statement of Unaudited Financial Results, Q1 FY27 (lines 1312-1625), clean-copy values
Same four columns as Table 4. Consolidated Other expenses / PBT figures below were cross-footed against the
printed Total income / Total expenses / PBT rows on the same page where the OCR clean-pass digit string was
ambiguous (see file note at top of ledger); footing arithmetic shown inline.

| # | Line item | Line(s) | Q1 FY27 | Q4 FY26 | Q1 FY26 | FY26 | Flags |
|---|-----------|---------|---------|---------|---------|------|-------|
| 1 | I(a) Revenue from operations | 1344-1349 | 7,321.73 | 6,853.10 | 5,586.29 | 24,132.43 | |
| 2 | I(b) Other income | 1350-1355 | 48.13 | 38.85 | 7.75 | 72.18 | |
| 3 | Total income (I) | 1356-1362 | 7,369.86 | 6,891.98 | 5,594.04 | 24,204.61 | |
| 4 | II(a) Cost of materials consumed | 1369-1376 | 5,292.75 | 5,126.52 | 3,681.53 | 17,383.77 | |
| 5 | II(b) Purchases of stock-in-trade | 1377-1382 | 72.67 | 82.00 | 61.76 | 163.41 | |
| 6 | II(c) Changes in inventories of stock-in-trade and finished goods | 1383-1391 | (164.04) | (401.32) | 171.37 | (328.03) | |
| 7 | II(d) Employee benefits expense | 1392-1397 | 375.21 | 359.67 | 289.89 | 1,344.18 | |
| 8 | II(e) Finance costs | 1398-1404 | 106.20 | 97.23 | 157.96 | 413.32 | |
| 9 | II(f) Depreciation and amortization expense | 1405-1411 | 124.77 | 120.16 | 119.90 | 483.93 | |
| 10 | II(g) Other expenses | 1412-1417 | 793.70 [footed: Total expenses 6,601.26 less rows 4-9] | 663.66 [footed] | 654.92 | 2,807.05 | OCR clean-pass digit string ambiguous/truncated a leading digit; value footed against printed Total expenses row and confirmed to foot exactly |
| 11 | Total expenses (II) | 1418-1425 | 6,601.26 | (see note) [footed: 6,147.95 implied by printed PBT row 12 = Total income 6,891.98 minus 744.03] | 5,137.33 | 22,267.63 | Mar-26 total-expenses cell in OCR clean pass is internally inconsistent with the printed PBT row on the same page (component-sum path gives 6,047.92; PBT-row-implied path gives 6,147.95); flagged rather than resolved — A3/A4 to reconcile against source PDF image |
| 12 | III. Profit before exceptional item and tax (I-II) | 1427-1433 | 768.60 | 744.03 | 456.71 | 1,936.98 | see row 11 flag |
| 13 | IV. Exceptional item | 1435-1439 | — | 35.10 | — | 35.10 | EXCEPTIONAL_ITEM_DIVERGENCE — standalone equivalent row (Table 4, row 13) is nil in all four periods; consolidated carries 35.10 in Q4 FY26 and FY26 columns only (subsidiary-level item eliminated at standalone, retained at consol) |
| 14 | V. Profit before tax and share of net profits of investments accounted for using equity method (III-IV) | 1441-1448 | 768.60 | 708.93 | 456.71 | 1,901.88 | |
| 15 | VI. Share of profit/(loss) of equity accounted investees | 1452-1458 | — | — | (0.01) | (0.01) | ZERO_STANDING (nil in 3 of 4 periods; (0.01) in Q1 FY26 only — canonical "template line" per instructions) |
| 16 | VII. Profit before tax (V+VI) | 1460-1465 | 768.60 | 708.93 | 456.70 | 1,901.87 | |
| 17 | VIII(a) Current tax | 1471-1477 | 181.64 | 157.64 | 99.59 | 403.25 | |
| 18 | VIII(b) Current tax on earlier year | 1478-1484 | — | (0.01) | 2.58 | 2.57 | nil in one period only, not standing-nil |
| 19 | VIII(c) Deferred tax | 1485-1489 | 21.73 | 18.19 [OCR-ambiguous, best clean read] | 20.22 | 74.54 | |
| 20 | Total tax expense (VIII) | 1490-1496 | 203.37 | 175.81 | 117.99 | 480.36 | |
| 21 | IX. Profit for the period/year (VII-VIII) | 1498-1505 | 565.23 | 533.12 | 338.71 | 1,421.51 | |
| 22 | X(a) Remeasurement gains/(losses) on defined benefit plans | 1509-1519 | (23.53) | 4.95 | 1.22 | 0.95 | |
| 23 | X(b) Income tax relating to above | 1520-1529 | 5.92 | (1.25) | (0.31) | (0.24) | |
| 24 | Other comprehensive income, net of tax (X) | 1530-1539 | (17.61) | 3.70 | 0.91 | 0.71 | |
| 25 | XI. Total comprehensive income for the period/year (IX+X) | 1541-1547 | 547.62 | 536.82 | 339.62 | 1,422.22 | |
| 26 | Net Profit/(Loss) attributable to: Owners of the Company | 1549-1558 | 565.23 | 533.12 | 338.71 | 1,421.51 | |
| 27 | Net Profit/(Loss) attributable to: Non-Controlling Interests | 1559-1560 | — | — | — | — | ZERO_STANDING (nil all four periods) |
| 28 | OCI attributable to: Owners of the Company | 1561-1570 | (17.61) | 3.70 | 0.91 | 0.71 | |
| 29 | OCI attributable to: Non-Controlling Interests | 1571-1572 | — | — | — | — | ZERO_STANDING (nil all four periods) |
| 30 | Total Comprehensive Income attributable to: Owners of the Company | 1573-1583 | 547.62 | 536.82 | 339.62 | 1,422.22 | |
| 31 | Total Comprehensive Income attributable to: Non-Controlling Interests | 1584-1585 | — | — | — | — | ZERO_STANDING (nil all four periods) |
| 32 | X. Paid up Equity Share Capital | 1587-1596 | 2,946.71 | 2,946.71 | 2,410.02 | 2,946.71 | |
| 33 | XI. Other Equity | 1598-1601 | (blank) | (blank) | (blank) | 7,589.36 | Quarter columns intentionally blank, annual audited column only (standard practice); note consol Other Equity (7,589.36) differs from standalone (7,607.58, Table 4 row 25) — expected, reflects consolidation adjustments |
| 34 | XII(a) Basic EPS (INR)* | 1609-1615 | 1.92 | 1.81 [OCR-ambiguous; standalone equivalent is 1.89] | 1.41 [OCR-ambiguous; standalone equivalent is 1.39] | 5.05 [OCR-ambiguous, best clean read; standalone is 5.09] | OCR_AMBIGUOUS on 3 of 4 cells — flagged for A3/A4 to verify against source PDF rather than assumed equal to standalone |
| 35 | XII(b) Diluted EPS (INR)* | 1616-1621 | 1.92 | 1.81 [OCR-ambiguous] | 1.41 [OCR-ambiguous] | 5.05 [OCR-ambiguous] | OCR_AMBIGUOUS, same as row 34 |

Footnote: * "Not annualised for interim periods" (lines 1622-1624), qualifies rows 34-35.

## TABLE 6 — Notes to Financial Results: Standalone + Consolidated (10 numbered + 4 footnotes = 14 rows)

| # | Note | Statement | Line(s) | First ~15 words | Flags |
|---|------|-----------|---------|-----------------|-------|
| 1 | Note 1 | Standalone | 780-793 | Results reviewed by Audit Committee, approved by Board on Aug 03, 2026; Limited Review carried out by Statutory Auditors | |
| 2 | Note 2 | Standalone | 795-800 | Results prepared per Ind AS notified under Section 133 of Companies Act 2013, read with Companies (Ind AS) Rules 2015 | NOTE_LABEL_ANOMALY — printed marker is "*" in the extract, not "2"; content and position match the consolidated Note 2 (row 7 below), which does carry a "2" label |
| 3 | Note 3 | Standalone | 802-853 | IPO proceeds INR 4,400 mn; utilisation table — Prepayment of borrowings 3,900.00, General corporate purposes# 224.55, Offer issue expenses# 275.45, Total 4,400.00 fully utilised as of June 30, 2026 | |
| 4 | Note 4 | Standalone | 856-863 | Mar-31-2026 quarter figures are balancing figures between audited FY figures and unaudited 9-month YTD figures, subjected to limited review | |
| 5 | Note 5 | Standalone | 865-866 | Company is in steel products manufacturing with similar economic characteristics, primarily India operations; hence one operating segment | |
| 6 | Note 1 | Consolidated | 1717-1756 | Consolidated results reviewed by Audit Committee, approved by Board on Aug 03, 2026; Limited Review carried out by Statutory Auditors | |
| 7 | Note 2 | Consolidated | 1776-1801 | Results prepared per Ind AS notified under Section 133 of Companies Act 2013, read with Companies (Ind AS) Rules 2015 | Marker printed as "2" (garbled to "[=]" in one OCR pass); see row 2 anomaly note |
| 8 | Note 3 | Consolidated | 1802-1842 | IPO proceeds INR 4,400 mn; utilisation table — Prepayment of borrowings (Holding Co) 3,900.00, General corp purposes# 224.55, Offer issue expenses# 275.45, Total 4,400.00 fully utilised | |
| 9 | Note 4 | Consolidated | 1843-1859 | Mar-31-2026 quarter figures are balancing figures between audited FY figures and unaudited 9-month YTD figures, subjected to limited review | |
| 10 | Note 5 | Consolidated | 1860-1867 | Group is in steel products manufacturing with similar economic characteristics, primarily India operations; hence one operating segment | Note number itself not legible in extract (garbled to stray "we" at line 1860); content and position confirm it is Note 5 |
| 11 | Footnote (IPO table, standalone) | Standalone | 851-853 | "Amount including GST" — qualifies "General corporate purposes" and "Offer issue expenses" rows | |
| 12 | Footnote (EPS, standalone) | Standalone | 679-681 | "Not annualised for interim periods" — qualifies Basic/Diluted EPS rows | |
| 13 | Footnote (IPO table, consolidated) | Consolidated | 1840-1842 | "Amount including GST" — qualifies "General corporate purposes" and "Offer issue expenses" rows | |
| 14 | Footnote (EPS, consolidated) | Consolidated | 1622-1624 | "Not annualised for interim periods" — qualifies Basic/Diluted EPS rows | |

## TABLE 7 — Independent Auditor's Limited Review Reports: Paragraphs (2 reports, 10 rows)

| # | Report | Para | Line(s) | Content | Flags |
|---|--------|------|---------|---------|-------|
| 1 | Standalone | 1 (scope) | 195-230 | Reviewed accompanying statement of unaudited standalone financial results of the Company for quarter ended June 30, 2026 | |
| 2 | Standalone | 2 (mgmt responsibility) | 232-265 | Statement is responsibility of Company's management, approved by Board, prepared per Ind AS 34 | |
| 3 | Standalone | 3 (review standard / scope limitation) | 267-324 | Review conducted per SRE 2410; review is substantially less in scope than an audit; accordingly, no audit opinion expressed | |
| 4 | Standalone | 4 (conclusion) | 326-355 | "nothing has come to our attention that causes us to believe" statement is not prepared in accordance with Ind AS / not disclosed per Reg 33 — unmodified/unqualified conclusion | |
| 5 | Consolidated | 1 (scope) | 1001-1033 | Reviewed accompanying statement of unaudited consolidated financial results of the Holding Company and its subsidiary (together "the Group") for quarter ended June 30, 2026 | |
| 6 | Consolidated | 2 (mgmt responsibility) | 1035-1067 | Statement is responsibility of Holding's management, approved by Holding's Board, prepared per Ind AS 34 | |
| 7 | Consolidated | 3 (review standard / scope limitation) | 1069-1122 | Review conducted per SRE 2410; review is substantially less in scope than an audit; accordingly, no audit opinion expressed | |
| 8 | Consolidated | 3b (unnumbered — Reg 33(8) procedures) | 1124-1137 | "We also performed procedures in accordance with the circular issued by SEBI under Regulation 33(8)...to the extent applicable" | Unnumbered sub-paragraph, no equivalent in standalone report |
| 9 | Consolidated | 4 (entity list) | 1139-1163 | Statement includes financial results of: i. Holding Company (Sambhv Steel Tubes Ltd); ii. Subsidiary (Sambhv Tubes Ltd, formerly Sambhv Tubes Private Ltd) | see Table 8 |
| 10 | Consolidated | 5 (conclusion) | 1187-1235 | "nothing has come to our attention" — unmodified/unqualified conclusion, same construction as standalone para 4 | |

Opinion type for both reports: unmodified/unqualified review conclusion (no Emphasis of Matter, no Other
Matters, no Going Concern language, no qualification identified in either report as extracted).

## TABLE 8 — Consolidation Entity List (3 rows)

| # | Entity | Relationship | Report | Line(s) | Flags |
|---|--------|--------------|--------|---------|-------|
| 1 | Sambhv Steel Tubes Limited (formerly Sambhv Steel Tubes Private Limited and Sambhv Sponge Power Private Limited) | Reporting entity | Standalone review report, para 1 | 201-211 | |
| 2 | Sambhv Steel Tubes Limited (formerly Sambhv Steel Tubes Private Limited and Sambhv Sponge Power Private Limited) | Holding Company | Consolidated review report, para 4(i) | 1144-1153 | |
| 3 | Sambhv Tubes Limited (formerly Sambhv Tubes Private Limited) | Subsidiary | Consolidated review report, para 4(ii) | 1156-1161 | ENTITY_CHANGE not assessable — no prior-quarter ledger provided (first pipeline run for this ticker) |

## TABLE 9 — Digital Signature Blocks (5 rows)

| # | Signatory | Designation | Document | Line(s) | Timestamp | Flags |
|---|-----------|-------------|----------|---------|-----------|-------|
| 1 | Niraj Shrivastava (Membership No. F8459) | Company Secretary & Compliance Officer | Board Outcome letter to BSE/NSE | 82-88 | 2026.08.03 19:11:15 +05'30' | Board meeting concluded 06:20 PM (18:20); signature timestamp 19:11:15 is after conclusion — ordering checked, no anomaly |
| 2 | Vikas Kumar Goyal (DIN 00318182) | Managing Director | Standalone financial results, "For and on behalf of Board" block | 869-903 | Date: August 03, 2026 (no time) | Garbled OCR pass shows "2020" — clean pass confirms 2026 |
| 3 | Vikas Kumar Goyal (DIN 00318182) | Managing Director | Consolidated financial results, "For and on behalf of Board" block | 1869-1903 | Date: August 03, 2026 (no time) | |
| 4 | Vijay Kumar (Membership No. 092671) | Partner, S S Kothari Mehta & Co LLP (FRN 000756N/N500441) | Standalone Limited Review Report | 357-385 | Date: August 03, 2026, Place: New Delhi (no time); UDIN 26092671RWBLNI3546 | |
| 5 | Vijay Kumar (Membership No. 092671) | Partner, S S Kothari Mehta & Co LLP (FRN 000756N/N500441) | Consolidated Limited Review Report | 1239-1268 | Date: August 03, 2026, Place: New Delhi (no time); UDIN 26092671QYMDDT2909 | |

---

## SUMMARY ROW COUNT

7 (agenda/meeting) + 8 (Annexure A) + 6 (Annexure B) + 27 (standalone line items) + 35 (consolidated line
items) + 14 (notes/footnotes) + 10 (auditor paragraphs) + 3 (entities) + 5 (signature blocks) = **115 ledger
rows**, every row carrying an extract line number.

## FLAGS RAISED — INDEX

- **ZERO_STANDING** (6 instances): Annexure A row 1 (Existing Capacity — Nil); Standalone Table 4 row 13
  (Exceptional item, nil all periods); Consolidated Table 5 row 15 (Share of profit/(loss) of equity
  accounted investees, nil in 3 of 4 periods); Consolidated Table 5 rows 27, 29, 31 (Non-Controlling
  Interests attribution rows, nil all periods across Net Profit / OCI / Total Comprehensive Income).
- **EXCEPTIONAL_ITEM_DIVERGENCE** (1 instance, custom flag): Consolidated Exceptional item is 35.10 in
  Q4 FY26 and FY26 columns while the standalone equivalent is nil in all four periods (Table 4 row 13 vs
  Table 5 row 13).
- **DATE_DISCREPANCY** (1 instance, custom flag): Board Outcome letter agenda item (d) states Bikash
  Agrawal's Director appointment is effective May 09, 2026; Annexure B row 3 states the cessation-as-SMP /
  board-approval date is May 08, 2026 (Table 1 row 4; Table 3 row 3).
- **NOTE_LABEL_ANOMALY** (1 instance, custom flag): Standalone Note 2 is printed with a "*" marker instead
  of "2" in the extract; content and position match consolidated Note 2, which does carry the numeral
  (Table 6 rows 2, 7).
- **OCR_AMBIGUOUS** (multiple instances, custom flag): Consolidated Table 5 rows 10, 11, 19, 34, 35 — clean
  OCR pass values reconstructed via cross-footing against printed sub-totals or flagged as unresolved for
  A3/A4 verification against the source PDF image, per row-level notes.
- **ENTITY_CHANGE**: not assessable this cycle — no prior-quarter ledger provided (first quarterly run for
  SAMBHV).
