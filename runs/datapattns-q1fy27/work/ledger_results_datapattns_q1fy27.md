# LEDGER — DATAPATTNS Q1FY27 RESULTS FILING
Source: extract_results_datapattns_q1fy27.txt (224 lines, 4 pages, standalone only —
Note 5 confirms no subsidiary/associate/JV as on 30 June 2026, so no consolidated
statement exists in this filing).
Prior-quarter ledger: NONE on file — no diff possible this run.

```
=== A2 COUNT TEST ===
category: agenda_items      grep_count: 1    sweep_count: 1    match: yes
category: auditor_paras     grep_count: 4    sweep_count: 4    match: yes
category: line_items        grep_count: 27   sweep_count: 27   match: yes
category: notes             grep_count: 8    sweep_count: 8    match: yes
category: entities           grep_count: 0    sweep_count: 0    match: yes
category: signature_blocks  grep_count: 3    sweep_count: 3    match: yes
category: annexures         grep_count: 0    sweep_count: 0    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Method notes on how each grep_count was built (so the reconciliation is auditable):
- agenda_items: grep for approval-phrase `considered and approved` in the Board
  Outcome letter (line 34) = 1 hit; keyword sweep for AGM/dividend/appoint/ESOP/
  auditor/scrutinizer/record date/capital-raising terms in lines 17-56 = 0 hits.
  Manual read of the full letter body confirms exactly one substantive agenda
  item. 1 = 1, match.
- auditor_paras: `grep -n -E "^\s*[0-9]+\.\s"` restricted to the auditor report
  region (lines 71-119) = 4 hits (lines 76, 82, 89, 98); the same regex run
  unrestricted also snags two false positives (lines 35, 175 — mid-sentence
  "2026." at start of a wrapped line, not list markers) which manual sweep
  discards. Manual paragraph-by-paragraph read of the report = 4. Match.
- line_items: grep for numeric-value-pattern lines (`[0-9]+\s*\.\s*[0-9]+`)
  within the main statement body (lines 132-169) = 20; same pattern within the
  QIP table body (lines 199-207) = 7. Total 27. Manual line-by-line read of
  both tables (accounting for labels that wrap across 2 physical lines with the
  Roman numeral/values on the adjoining line) = 20 + 7 = 27. Match.
- notes: `grep -n -E "^[0-9]+[[:space:]]"` on the page-4 notes region = 6
  (numbered notes 2-7); `grep -n "Notes:"` anchors the section header and the
  unnumbered text immediately below it (Note 1, no digit prefix in the
  extracted text) = +1; `grep -n "\*"` finds the EPS footnote marker (table,
  line 168) and its footnote text (line 170) = +1 footnote. Grep total = 8.
  Manual top-to-bottom read of the Notes section and the EPS footnote = 8.
  Match.
- entities: `grep -n -iE "subsidiary|associate|joint venture"` = 2 hits, one of
  which (line 13) is the A1 header metadata note, not filing body text; the
  body-text hit is Note 5 (line 209), which states zero entities. Manual sweep
  of the filing body confirms 0 subsidiaries/associates/JVs. Both = 0. Match.
- signature_blocks: `grep -n -iE "digitally signed|Membership No|UDIN|Place:|Date:"`
  clusters into 3 blocks (Company Secretary line 47-54; Statutory Auditor line
  106-119; Chairman & Managing Director line 219-225). Manual sweep confirms 3
  distinct signatories. Match.
- annexures: `grep -n -iE "annexure|director.*profile|DIN[: ]|brief resume"` = 1
  hit but it is a substring false-positive (UDIN contains "DIN"); no true
  annexure content exists in this 4-page filing. Manual sweep confirms 0
  annexures. Match.

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS
| # | Line | Item | Detail | Flags |
|---|------|------|--------|-------|
| 1 | 34 | Results approval | Board "considered and approved the Unaudited Financial Results for the quarter ended June 30, 2026" along with the Limited Review Report of the Statutory Auditors | — |

No other agenda items disclosed in this letter: no AR/annual accounts approval,
no AGM notice, no record date, no dividend, no director appointment/
resignation, no auditor change, no scrutinizer appointment, no ESOP grant, no
capital-raising enabling resolution. This is a single-item, results-only Board
Outcome letter.

**Board meeting timing** (line 40-41): commenced 2:30 p.m., concluded 6:30
p.m. IST on 30 July 2026 — 4-hour meeting.

---

## 2. AUDITOR'S REVIEW REPORT — PARAGRAPHS
| # | Line | Type | First 15 words | Flags |
|---|------|------|-----------------|-------|
| 1 | 76 | Introduction | "We have reviewed the accompanying Statement of Unaudited Financial Results of Data Patterns..." | — |
| 2 | 82 | Management's responsibility / scope basis | "This Statement, which is the responsibility of the Company's Management and approved by the..." | — |
| 3 | 89 | Basis of review (SRE 2410) | "We conducted our review of the Statement in accordance with the Standard on Review..." | — |
| 4 | 98 | Conclusion (unmodified) | "Based on our review conducted as stated in paragraph 3 above, nothing has come..." | — |

No Emphasis of Matter paragraph. No Other Matters paragraph. No Going Concern
paragraph. Entity list reviewed: Company (standalone) only — no
unaudited/management-furnished entities (none exist; standalone-only filing).
Firm: Deloitte Haskins & Sells, FRN 008072S (line 106-108). Signatory: Ananthi
Amarnath, Partner, Membership No. 209252 (line 114-116). UDIN:
26209252LUDGSU3734 (line 117).

---

## 3. STATEMENT OF UNAUDITED FINANCIAL RESULTS — LINE ITEMS (Q1FY27, standalone)
Columns: Q1FY27 (30 Jun 2026, unaudited) | Q4FY26 (31 Mar 2026, balancing fig.,
refer note 3) | Q1FY26 (30 Jun 2025, unaudited) | FY26 (31 Mar 2026, audited).

| # | S.No | Line | Line no. | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|------|----------|--------|--------|--------|------|-------|
| 1 | I | Revenue from Operations | 132 | 116.03 | 344.85 | 99.33 | 924.77 | — |
| 2 | II | Other income | 133 | 7.31 | 5.66 | 10.55 | 27.96 | — |
| 3 | III | Total Income (I+II) | 134 | 123.34 | 350.51 | 109.88 | 952.73 | — |
| 4 | IV(a) | Cost of materials consumed | 137 | 30.73 | 88.06 | 57.16 | 306.06 | — |
| 5 | IV(b) | Changes in inventories of WIP and finished goods | 138-139 | (6.21) | 3.65 | (37.06) | 33.84 | — |
| 6 | IV(c) | Employee benefits expenses | 140 | 42.53 | 40.72 | 36.38 | 154.26 | — |
| 7 | IV(d) | Finance costs | 141 | 3.28 | 4.65 | 3.19 | 12.45 | — |
| 8 | IV(e) | Depreciation and amortization expenses | 142 | 5.92 | 5.89 | 5.49 | 22.95 | — |
| 9 | IV(f) | Other expenses | 143 | 17.61 | 19.58 | 10.77 | 56.62 | — |
| 10 | IV | Total Expenses (IV) | 144 | 93.86 | 162.55 | 75.93 | 586.18 | — |
| 11 | V | Profit before exceptional items and tax (III-IV) | 147-149 | 29.48 | 187.96 | 33.95 | 366.55 | — |
| 12 | VI | Exceptional items: Statutory impact of new Labour Codes (Refer note 6) | 150-153 | - | . (dash, OCR artifact) | - | 3.01 | ZERO_STANDING |
| 13 | VII | Profit before tax (V-VI) | 154 | 29.48 | 187.96 | 33.95 | 363.54 | — |
| 14 | VIII | Tax expense (including deferred tax) | 155 | 7.42 | 49.58 | 8.45 | 92.17 | — |
| 15 | IX | Profit for the period/year (VII-VIII) | 156 | 22.06 | 138.38 | 25.50 | 271.37 | — |
| 16 | X | Other Comprehensive Income (net of tax) | 157 | (0.41) | 1.13 | 0.13 | 0.61 | — |
| 17 | XI | Total Comprehensive Income for the period/year (IX+X) | 158-160 | 21.65 | 139.51 | 25.63 | 271.98 | — |
| 18 | XII | Paid up equity share capital (Face value of Rs 2 each) | 162-163 | 11.20 | 11.20 | 11.20 | 11.20 | — |
| 19 | XIII | Other Equity | 166 | (blank) | (blank) | (blank) | 1,724.77 | Quarterly columns blank by standard convention (balance-sheet item, annual disclosure only); not zero/dash so no ZERO_STANDING |
| 20 | XIV | Earnings per equity share (EPS), face value Rs 2 each, Basic and Diluted | 167-169 | 3.94 | 24.71 | 4.55 | 48.47 | Footnoted * (not annualised for quarters) |

Row 12 (Exceptional items) is dash/nil in all three quarterly columns and
carries value only in the annual FY26 column — a standing template line that
exists because a transaction of that type (statutory Labour Code impact) was
recognized once at year-end; flagged ZERO_STANDING for the quarter columns per
rule, not dropped.

---

## 4. NOTE 4 — QIP UTILIZATION TABLE LINE ITEMS
Columns: Amount to be utilised as per prospectus | Utilisation upto 30 June
2026 | Unutilised amount as on 30 June 2026.

| # | Line | Object of the issue | Amt per prospectus | Utilised upto 30-Jun-26 | Unutilised | Flags |
|---|------|----------------------|--------------------|--------------------------|-----------|-------|
| 1 | 199 | Funding Working Capital Requirements | 168.00 | 168.00 | - | Fully utilised |
| 2 | 200 | Investment in Product Development | 167.24 | 142.59 | 24.65 | — |
| 3 | 201 | Prepayment or Repayment of Borrowings | 25.00 | 25.00 | - | Fully utilised |
| 4 | 202-204 | Funding capital expenditure towards setting up an EMI-EMC Testing Facility | 15.23 | 13.63 | 1.60 | — |
| 5 | 205 | Funding acquisition of land (including building) | 7.75 | 7.75 | - | Fully utilised |
| 6 | 206 | General corporate purposes | 104.52 | 104.52 | (blank — cell missing in extract) | NOT_FOUND: unutilised cell absent in source table; Total row (row 7) arithmetically implies 0/dash for this line (26.25 total unutilised = 24.65 + 1.60 + 0) |
| 7 | 207 | Total | 487.74 | 461.49 | 26.25 | Reconciles: sum of rows 1-6 in each column = Total column value |

---

## 5. NOTES TO THE FINANCIAL RESULTS
| # | Line | Numbered? | First 15 words | Flags |
|---|------|-----------|------------------|-------|
| 1 | 174-178 | Unnumbered in extract (implicit Note 1, immediately below "Notes:" header, line 173) | "The financial results have been reviewed and recommended by the Audit Committee and Board..." | Confirms unmodified auditor conclusion |
| 2 | 180-181 | Note 2 | "The Company operates only in one business segment i.e. manufacture, sale and service of..." | Single-segment company, no segment note required |
| 3 | 183-184 | Note 3 | "The figures for the quarter ended 31 March 2026 represents the balancing figures between..." | Explains Q4FY26 balancing-figure column |
| 4 | 187-207 | Note 4 | "During the financial year 2022-23, the Company allotted Equity shares through Qualified Institutional..." | Contains QIP utilization table (Section 4 above) |
| 5 | 209 | Note 5 | "The Company does not have any subsidiary/associate/joint ventures as on 30 June 2026." | ZERO_STANDING — zero-entity consolidation-scope disclosure (see Section 6) |
| 6 | 211-212 | Note 6 | "Exceptional Item in the statement of profit and loss for the year ended 31..." | Cross-referenced by main-statement row 12 (Exceptional items) |
| 7 | 214 | Note 7 | "Figures for the previous period/year have been regrouped/rearranged wherever necessary." | Standard regrouping boilerplate |
| 8 | 168, 170 | Footnote (asterisk, below EPS row) | "*EPS is not annualised for the quarter ended 30 June 2026, 31 March 2026 and..." | Qualifies row 20 of Section 3 |

---

## 6. ENTITIES / CONSOLIDATION SCOPE
| # | Line | Entity | Relationship | Flags |
|---|------|--------|---------------|-------|
| 1 | 209 | None — "does not have any subsidiary/associate/joint ventures as on 30 June 2026" | N/A | ZERO_STANDING (standing consolidation-scope disclosure, zero entities this period; no consolidated statement accompanies this filing) |

Prior-quarter ledger not on file, so no ENTITY_CHANGE cross-check is possible
this run — carried forward as an open item for the next quarter's diff.

---

## 7. DIGITAL / PHYSICAL SIGNATURE BLOCKS
| # | Line | Signatory | Designation | Timestamp | Flags |
|---|------|-----------|-------------|-----------|-------|
| 1 | 47-54 | Prakash R | Company Secretary and Compliance Officer, Membership No. F13620 | Digitally signed; date/time not captured in extract (letter dated 30 July 2026 at header, line 18) | NOT_FOUND: signature timestamp not present in extracted text |
| 2 | 106-119 | Ananthi Amarnath | Partner, Deloitte Haskins & Sells, FRN 008072S, Membership No. 209252, UDIN 26209252LUDGSU3734 | Digitally signed 2026.07.30 16:34:57 +05'30' | SIGNATURE_BEFORE_BOARD_CONCLUSION — auditor's digital signature timestamp (4:34:57 p.m.) precedes the Board meeting's stated conclusion time (6:30 p.m., line 41) by ~1h56m, even though the Board Outcome letter states the review report was considered together with the results at that meeting |
| 3 | 219-225 | Srinivasagopalan Rajan | Chairman and Managing Director | Not digitally timestamped; dated 30 July 2026 only (OCR-garbled name rendering, line 220-223) | — |

---

## 8. ANNEXURES
None present in this filing. This is a standalone-only, 4-page quarterly
results package (Board Outcome letter + auditor review report + financial
statement + notes); no director-profile annexures, no separate schedules
beyond the QIP table embedded in Note 4. Confirmed by grep sweep (Section
header above) and manual read of all 224 lines.

---

## RECONCILIATION SUMMARY
All 224 lines of the extract have been accounted for across Sections 1-8:
page 1 (Board Outcome letter, Section 1) → page 2 (auditor report, Section 2
and part of Section 7) → page 3 (financial statement, Section 3) → page 4
(notes, QIP table, entity note, signature block; Sections 4-8). No content
band was skipped.

Flags raised this run: ZERO_STANDING (x2: exceptional-items row, entity-scope
note), NOT_FOUND (x2: QIP "General corporate purposes" unutilised cell, CS
signature timestamp), SIGNATURE_BEFORE_BOARD_CONCLUSION (x1: auditor digital
signature time vs board conclusion time).
