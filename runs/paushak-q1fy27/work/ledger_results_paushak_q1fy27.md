# A2 COMPLETENESS LEDGER — Paushak Limited (PAUSHAK) — Q1 FY27 — Results Filing

Source: `extract_results_paushak_q1fy27.txt` (4 pages, 235 lines, unit convention
Lakhs, conversion x0.01 to Rs Crores, no OCR pages, 100% page coverage).
Prior-quarter ledger: not supplied to this run — no diff/`ENTITY_CHANGE` or
`DROPPED_SLIDE`-style cross-check performed; noted as a coverage gap below.

```
=== A2 COUNT TEST ===
category: agenda_items     grep_count: 1   sweep_count: 1   match: yes
category: line_items       grep_count: 26  sweep_count: 26  match: yes
category: notes            grep_count: 5   sweep_count: 5   match: yes
category: auditor_paras    grep_count: 5   sweep_count: 5   match: yes
category: entities         grep_count: 1   sweep_count: 1   match: yes
category: signature_blocks grep_count: 2   sweep_count: 2   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used for the count test:
- agenda_items: manual sweep of Board Outcome letter body (lines 15-72); grep
  `-iE "approved|Sub:"` isolates the single substantive sentence.
- line_items: `grep -n -E "^\s+[0-9]+\s+[A-Za-z(]"` (11 Sr.-numbered rows) +
  `grep -n -E "^\s*(\([a-h]\)|[A-B]\s*\(i+\))"` (10 lettered/roman sub-rows) +
  `grep -n -E "^\s*\(ii\)"` (2 wrapped roman-ii sub-rows) +
  `grep -n -E "Total Income|Total Expenses"` (2 subtotals) +
  `grep -n "Basic & Diluted"` (1 EPS sub-row) = 11+10+2+2+1 = 26.
- notes: `grep -n -E "^\s+[0-9]+\s+[A-Za-z(]"` restricted to lines >=136 (5 rows,
  lines 137/139/140/142/144).
- auditor_paras: `grep -n -E "^\s*[0-9]+\.\s"` (lines 165, 171, 179, 190, 216).
- entities: manual sweep — no consolidation section present; standalone
  financials for the single reporting entity only.
- signature_blocks: manual sweep — one at the Board Outcome letter close (line
  45), one at the auditor review report close (lines 224-235).

---

## 1. Board Outcome Letter — Agenda Items

| # | Line(s) | Item | Detail | Flags |
|---|---------|------|--------|-------|
| 1 | 27-32 | Approval of unaudited financial results | Board approved Unaudited Financial Results for quarter ended 30 June 2026. Letter uses "inter alia approved" (boilerplate phrasing implying other business may have been transacted) but no other agenda item is itemized anywhere in the 4-page filing. | INTER_ALIA_UNITEMIZED |

Board meeting timing (line 37-38): commencement 3:30 p.m., conclusion 4:05 p.m.
— 35-minute meeting.

No AR approval / AGM notice / record date / dividend / director appointment /
auditor change / scrutinizer / ESOP / capital-raising resolution is disclosed
in this filing (results-only Board Outcome letter).

---

## 2. Statement of Unaudited Financial Results — Line Items

Units Rs in lacs as filed (x0.01 for Rs Cr). Four columns: Q ended 30.06.2026
(Unaudited), Q ended 31.03.2026 (Audited), Q ended 30.06.2025 (Unaudited), Year
ended 31.03.2026 (Audited).

| Sr/Sub | Line | Particular | 30.06.2026 | 31.03.2026 | 30.06.2025 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 89 | Revenue from Operations | 8,355 | 5,514 | 5,588 | 21,860 | |
| 2 | 90 | Other Income | 315 | 821 | 188 | 1,211 | |
| — | 92 | Total Income (subtotal) | 8,669 | 6,335 | 5,777 | 23,071 | SUBTOTAL |
| 3 | 94 | Expenses (header, no own values) | — | — | — | — | HEADER_ROW |
| 3(a) | 95 | Cost of Materials consumed | 2,899 | 1,903 | 1,086 | 5,724 | |
| 3(b) | 96-98 | Change in inventories of finished goods, semi-finished goods and WIP | (280) | (853) | (102) | (1,147) | |
| 3(c) | 99 | Employee benefits expense | 966 | 926 | 984 | 3,976 | |
| 3(d) | 100 | Finance Costs | 136 | 102 | 4 | 111 | |
| 3(e) | 101 | Depreciation and amortisation expense | 842 | 790 | 406 | 2,138 | |
| 3(f) | 102 | Other expenses | 2,203 | 1,866 | 1,835 | 7,228 | |
| — | 104 | Total Expenses (subtotal) | 6,768 | 4,733 | 4,214 | 18,030 | SUBTOTAL |
| 4 | 106 | Profit before Tax | 1,902 | 1,602 | 1,563 | 5,041 | |
| 5 | 108 | Tax Expense (header, no own values) | — | — | — | — | HEADER_ROW |
| 5(a) | 109 | Current Tax | 249 | 363 | 142 | 350 | |
| 5(b) | 110 | Deferred Tax | 142 | (11) | 218 | 759 | |
| 6 | 112 | Profit after tax | 1,510 | 1,251 | 1,203 | 3,933 | |
| 7 | 114 | Other Comprehensive Income (header, no own values) | — | — | — | — | HEADER_ROW |
| 7A(i) | 115 | Item that will not be reclassified to P&L | 2 | (114) | 1 | (103) | |
| 7A(ii) | 116-118 | Income tax relating to item not reclassified | (0) | 17 | (0) | 14 | |
| 7B(i) | 119 | Item that will be reclassified to P&L | - | (785) | - | (785) | ZERO_STANDING (dash in both quarter columns) |
| 7B(ii) | 120-122 | Income tax relating to item reclassified | - | 110 | (11) | 121 | ZERO_STANDING (dash in current-quarter column) |
| 8 | 125 | Total Comprehensive Income for the period | 1,512 | 478 | 1,193 | 3,180 | |
| 9 | 127 | Paid up Equity Share Capital (FV Rs 5/-) | 1,233 | 1,233 | 308 | 1,233 | Note: 30.06.2025 figure (308) not comparable to other columns — pre-subdivision/bonus base; see Note 3 |
| 10 | 130 | Other Equity excluding Revaluation Reserves | (blank) | (blank) | (blank) | 38,363 | ZERO_STANDING (quarter columns blank — annual-only balance-sheet disclosure, standard) |
| 11 | 132 | Earnings per equity share (Refer note 3) (header) | — | — | — | — | HEADER_ROW |
| 11 | 133 | — Basic & Diluted (in Rs.) | 6.13 | 5.07 | 4.88 | 15.95 | |

Line-item count: 26 (11 Sr.-numbered rows [4 of which are non-value headers: 3,
5, 7, 11] + 2 subtotals + 13 sub-rows [6 expense + 2 tax + 4 OCI + 1 EPS]).
ZERO_STANDING flagged rows: 3 (7B(i), 7B(ii), row 10).

---

## 3. Notes to the Financial Results

| Note # | Line(s) | First 15 words | Flags |
|---|---|---|---|
| 1 | 137-138 | "The above results were reviewed by the Statutory Auditors, recommended by the Audit Committee and..." | |
| 2 | 139 | "The Company is engaged in the business of Speciality Chemicals only and therefore..." | Single reportable segment — no segment table required |
| 3 | 140-141 | "The Earning Per Share in respect of the previous quarter has been restated to give effect..." | Explains EPS restatement for sub-division/bonus shares referenced against Sr. 11 |
| 4 | 142-143 | "The figures for quarter ended 31st March 2026 are the balancing figures between the audited..." | Explains derivation of Q4FY26 column |
| 5 | 144-145 | "The previous quarters'/year's figures have been regrouped/rearranged wherever necessary to make it comparable..." | Standard regrouping note |

No unnumbered notes, asterisks, daggers, or footnote markers found below the
Notes block on manual sweep (lines 146-153 are signature block / date /
place only).

---

## 4. Auditor's Limited Review Report — Paragraphs

| Para # | Line(s) | Content type | First 15 words | Flags |
|---|---|---|---|---|
| 1 | 165-169 | Scope statement | "We have reviewed the accompanying Statement of Unaudited Financial results of Paushak Limited..." | |
| 2 | 171-177 | Management responsibility / framework (Ind AS 34, Reg 33) | "This statement, which is the responsibility of the Company's Management and approved by..." | |
| 3 | 179-188 | Basis of review (SRE 2410) — explicit "we do not express an audit opinion" | "We conducted our review of the Statement in accordance with the Standard on Review..." | |
| 4 | 190-196 | Conclusion — unmodified/clean review conclusion, no qualification, no Emphasis of Matter | "Based on our review conducted as above, nothing has come to our attention that causes..." | CLEAN_OPINION |
| 5 (Other Matter) | 216-221 | Other Matter paragraph | "The unaudited financial results for the quarter ended 30th June, 2025 included in these..." | OTHER_MATTER — prior-year comparative reviewed by predecessor auditor (unmodified opinion dated 31 Jul 2025), not by CNK & Associates |

No separate Emphasis of Matter or Going Concern paragraph found. Entity list
reviewed: single entity, Paushak Limited (standalone) — no subsidiaries /
unaudited or management-furnished components named.

---

## 5. Consolidation / Entity Scope

| # | Line(s) | Entity | Relationship | Flags |
|---|---|---|---|---|
| 1 | 81, 161-169 | Paushak Limited | Reporting entity — standalone results only, no consolidation | Prior-quarter ledger not supplied; ENTITY_CHANGE check not performed — NOT_FOUND (comparison basis unavailable) |

No subsidiaries, associates, or joint ventures named anywhere in the filing;
Note 2 confirms single reportable segment (Speciality Chemicals).

---

## 6. Digital / Signature Blocks

| # | Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---|---|---|---|---|
| 1 | 44-50 | Not named in extracted text | "For Paushak Limited" | Date on letter: 30th July, 2026 (line 15); no signature time captured (graphic signature not OCR'd, ocr_pages: none per header, so likely simply absent from face of letter) | SIGNATORY_NAME_NOT_FOUND |
| 2 | 224-235 | Not named in extracted text (Partner) | "For CNK & Associates, LLP", Chartered Accountants, Firm Regn No. 101961W/W-100036, Partner, Membership No. 158289 | Date: 30th July, 2026; UDIN: 26158289NUUQBL1150 (line 235) | SIGNATORY_NAME_NOT_FOUND — cannot verify signature timestamp against board conclusion time (4:05 p.m.) since no time-of-day is stamped on the report, only date |

---

## Coverage notes / gaps carried forward to A3/A4

- INTER_ALIA_UNITEMIZED: Board Outcome letter uses "inter alia approved," a
  standard phrase that can imply unlisted additional business; only one
  agenda item is actually itemized in this filing. Not necessarily a miss —
  flagged for A3/A4 awareness.
- ZERO_STANDING (x3): OCI reclassifiable items (7B(i), 7B(ii)) carry dash
  values in the current and/or comparative quarter columns; Other Equity
  (row 10) is populated only in the annual column, per standard quarterly
  filing convention. All three are template signals per the operating
  rules and must not be dropped from downstream review.
- Entity/prior-ledger cross-check (`ENTITY_CHANGE`) could not be performed —
  no prior-quarter ledger path was supplied to this run.
- Two signature blocks present but no signatory name resolved in the
  extracted text for either (Board Outcome letter closer, auditor Partner) —
  carried as SIGNATORY_NAME_NOT_FOUND, not a mechanical failure, since names
  are typically rendered as image signatures on the source PDF and page
  coverage was reported at 100% text (no OCR pages).
- No annexures, director profiles, dividend/AGM/ESOP/capital-raise agenda
  items, or Emphasis of Matter / Going Concern paragraphs found anywhere in
  the 4-page filing — categories are enumerated as NOT_APPLICABLE / zero
  count for this doctype instance, not silently omitted.
