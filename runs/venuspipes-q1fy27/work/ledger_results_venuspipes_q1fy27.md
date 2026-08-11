# A2 ENUMERATOR LEDGER — Venus Pipes & Tubes (VENUSPIPES), Q1 FY27, RESULTS filing

Source: `extract_results_venuspipes_q1fy27.txt` (A1 output, 5 pages, 230 embedded
lines). All line numbers below are the EMBEDDED sequential line numbers written
into the extract file by A1 (first tab-delimited field of each content line),
not raw physical file line numbers, per A1's instruction that this numbering
is final. Units as stated in source: Rs Millions (x0.1 to Cr), except EPS (Rs).

SCOPE NOTE (carried forward from A1, restated here for the record): this
filing contains a SINGLE set of financial results. The strings "consolidated"
and "standalone" do not appear anywhere in the source (A1 grep = 0 matches).
There is no subsidiary/associate disclosure and only one Auditor's Review
Report, addressed to Venus Pipes & Tubes Limited alone. The task briefing's
description of a standalone+consolidated filing does not match the source as
supplied. This ledger therefore enumerates ONE statement set, ONE auditor
report, and a single-entity (no-consolidation-list) scope. Flag: `SCOPE_DISCREPANCY`.

```
=== A2 COUNT TEST ===
category: notes             grep_count: 6   sweep_count: 6   match: yes
category: line_items        grep_count: 35  sweep_count: 35  match: yes
category: agenda_items      grep_count: 1   sweep_count: 1   match: yes
category: auditor_paras     grep_count: 4   sweep_count: 4   match: yes
category: signature_blocks  grep_count: 3   sweep_count: 3   match: yes
category: entities           grep_count: 1   sweep_count: 1   match: yes
category: annexures         grep_count: 0   sweep_count: 0   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep methodology per category (reproducible):
- notes: `awk -F'\t' '$1>=127 && $1<=161'` restricted to the "Notes to
  Statement" section (page 3), then `grep -nE "^[0-9]+\t\s*[0-9]+\.\s"` on the
  embedded-number field. 6 matches (embedded lines 129, 135, 138, 142, 145, 148).
- line_items: `awk -F'\t' '$1>=65 && $1<=119 && $2 !~ /^[ \t]*$/'` (all
  non-blank content lines inside the financial-results table, page 2), minus
  lines tagged `OCR CROSS-CHECK` (supplementary annotation lines, not table
  rows: embedded 71, 82, 109) and minus one stray glyph-only text-layer
  artifact line (embedded 68, content "Mi"/"M" fragment, not a line item).
  35 matches.
- agenda_items: `grep -c "•"` inside the Board Outcome letter body (embedded
  lines 1-46, page 1). 1 match.
- auditor_paras: `awk -F'\t' '$1>=170 && $1<=229'` (auditor report body)
  matched against numbered-paragraph markers ("N." alone on its own line, or
  "N. " followed by text). 4 matches (embedded lines 178, 186, 194, 209).
- signature_blocks: grep for `Digitally signed|Place:|Membership No|DIN:`
  across the full extract, then manually grouped into distinct sign-off
  blocks by page/context. 3 blocks (CS on page 1, Director on page 3,
  Auditor's Partner on page 5).
- entities: grep for all name variants of "Venus Pipes" / "VENUS PIPES" /
  OCR-variant "Venus Pip6" — all 5 mentions resolve to the same single legal
  entity. 1 entity.
- annexures: `grep -ni "annexure|appendix|schedule"` on the full extract. 0 matches.

---

## 1. Notes to Statement of Unaudited Financial Results (page 3)

| # | Line | First 15 words | Flags |
|---|------|-----------------|-------|
| N1 | 129 | "in terms of Regulation 33 of the SEBI (Listing Obligations and Disclosure Requirements) Regulations 2015," | — |
| N2 | 135 | "The figure for the quarter ended March 31, 2026 are balancing figures between the" | — |
| N3 | 138 | "These financial results have been prepared in accordance with Indian Accounting Standard (Ind'AS)" | — |
| N4 | 142 | "As the Company operates in a single operating segment, it did not give rise" | SINGLE_SEGMENT |
| N5 | 145 | "The previous period numbers have been regrouped/re-cast & rearranged wherever necessary to confirm the" | — |
| N6 | 148 | "The above Unaudited Financial Results of the Company are available on Company's website" | TEXT_GARBLED (website URL string is glyph-corrupted / unreadable in text layer: ",=_,',:,_::ds,u,r_ =~_.;1'=;"; not covered by A1's OCR cross-check pass) |

Manual sweep for unnumbered notes/footnotes below tables: one found, see
line item #31 in section 2 below (the "(Face value Rs. 10 per share)"
parenthetical under "Paid up equity share capital", embedded line 111) — a
footnote-style qualifier, not an independently numbered note. No asterisk-
or dagger-marked footnotes present anywhere in the extract (grep for `\*|†`
on the full file returns no footnote markers of that kind).

---

## 2. Financial Table Line Items (Statement of Unaudited Financial Results, page 2)

Columns: Q1 FY27 (qtr ended Jun 30, 2026, CURRENT) | Q4 FY26 (qtr ended Mar 31,
2026) | Q1 FY26 (qtr ended Jun 30, 2025) | FY26 (year ended Mar 31, 2026,
audited). All figures Rs Millions unless noted. "blank" = cell not populated
in source (dash/nil), not zero-with-a-printed-zero.

| # | Line | Item (as printed, garbling noted) | Q1 FY27 | Q4 FY26 | Q1 FY26 | FY26 | Flags |
|---|------|-----|--------:|--------:|--------:|-----:|-------|
| 1 | 65 | I. Revenue (section header) | — | — | — | — | — |
| 2 | 66 | Revenue from operations | 3,20S.37 | 3,021.95 | 2,764.14 | 11,668.48 | TEXT_GARBLED_UNRESOLVED (Q1FY27 cell "3,20S.37" — glyph-corrupted digit, likely "3,205.37" but NOT confirmed by A1's OCR pass; do not treat as confirmed) |
| 3 | 69 | Other Income | 26.90 | 21.43 | 39.16 | 116.32 | — |
| 4 | 70/71 | Total Income (A) | 3,232.27 | 3,043.38 | 2,803.30 | 11,784.80 | OCR_USED (text-layer row 70 truncated/column-garbled; values taken from A1's OCR cross-check at line 71 per A1 instruction) |
| 5 | 74 | II. Expenses (section header) | — | — | — | — | — |
| 6 | 75 | Cost of materials consumed | 2,320.58 | 1,960.11 | 1,551.82 | 7,783.59 | — |
| 7 | 76 | Changes in inventories of finished goods and work-in-progress | (244.02) | (11.44) | 304.53 | (78.30) | — |
| 8 | 77 | Employee benefits expense | 157.67 | 134.93 | 117.12 | 504.27 | — |
| 9 | 78 | Finance costs | 112.83 | 104.85 | 97.90 | 408.41 | — |
| 10 | 79 | Depreciation and amortisation expense | 72.16 | 62.91 | 52.16 | 235.82 | — |
| 11 | 80 | Other expenses | 455.99 | 444.29 | 342.63 | 1,553.13 | — |
| 12 | 81/82 | Total expenses (B) | 2,875.21 | 2,695.65 | 2,466.16 | 10,406.92 | OCR_USED (text-layer row 81 fully glyph-corrupted for 3 of 4 cells; values taken from A1's OCR cross-check at line 82 per A1 instruction) |
| 13 | 85 | III. Profit before exceptional items and tax (A-B) | 357.06 | 347.73 | 337.14 | 1,377.88 | label garbled ("In.Pram"), values clean |
| 14 | 87 | Exceptional Item (Impact of Labour Codes) | blank | (1.87) | blank | 4.58 | ZERO_STANDING — nil in current period (Q1FY27) and in the year-ago quarter (Q1FY26); populated only in Q4FY26 and FY26 columns |
| 15 | 89 | IV. Profit before tax (A-B-C) | 357.06 | 349.60 | 337.14 | 1,373.30 | label garbled ("fA.B.C"), values clean |
| 16 | 91 | V. Tax expense: (section header) | — | — | — | — | — |
| 17 | 92 | Current tax expenses | 71.70 | 84.07 | 77.40 | 307.98 | — |
| 18 | 93 | Adjustments of earlier years | blank | (2.72) | blank | (10.01) | ZERO_STANDING — nil in current period (Q1FY27) and in the year-ago quarter (Q1FY26); populated only in Q4FY26 and FY26 columns |
| 19 | 94 | Deferred tax | 21.28 | 13.29 | 12.10 | SS.71 | TEXT_GARBLED_UNRESOLVED — FY26 cell "SS.71" is glyph-corrupted and was NOT part of A1's supplementary OCR cross-check (that pass covered only Total Income / Total Expenses / Total Comprehensive Income rows); value cannot be confirmed downstream, do not estimate |
| 20 | 96 | Total tax expense | 92.98 | 94.64 | 89.50 | 353.68 | — |
| 21 | 98 | VI. Net Profit after tax | 264.08 | 254.96 | 247.64 | 1,019.62 | — |
| 22 | 100 | VII. Other Comprehensive Income / (Loss) (section header) | — | — | — | — | label garbled ("FVII...£Loss)") |
| 23 | 101 | Items that will not be reclassified to profit or loss (sub-header) | — | — | — | — | — |
| 24 | 102 | Remeasurements of the defined benefit plans | 0.13 | 2.49 | (0.43) | 0.52 | — |
| 25 | 103 | Income Tax impact on above [remeasurements] | (0.03) | (0.63) | 0.11 | (0.13) | — |
| 26 | 104 | Items that will be reclassified to profit or loss (sub-header) | — | — | — | — | — |
| 27 | 105 | Foreign exchange fluctuation in respect of cash flow hedge | 0.94 | (2.86) | 3.26 | 9.73 | — |
| 28 | 106 | Income Tax impact on above [FX hedge] | (0.24) | 0.72 | (0.82) | (2.45) | text-layer shows "(0,82)" (comma for period), unambiguous |
| 29 | 108/109 | VIII. Total comprehensive income for the period / year | 264.88 | 254.68 | 249.76 | 1,027.29 | OCR_USED for FY26 column only (text-layer col shows "Wg5"); label garbled ("VIn"); Q1FY27/Q4FY26/Q1FY26 columns match between text layer and OCR per A1 |
| 30 | 110 | IX. Paid up equity share capital | 207.16 | 207.16 | 204.92 | 207.16 | — |
| 31 | 111 | (Face value Rs. 10 per share) [footnote to #30] | n/a | n/a | n/a | n/a | footnote, not a value row |
| 32 | 113 | X. Other Equity | blank | blank | blank | 6,477.63 | ZERO_STANDING — nil in all three quarterly columns (Q1FY27, Q4FY26, Q1FY26); this is standard SEBI-format treatment (Other Equity is disclosed only against the audited year-end column), noted per "never drop a nil row," not an anomaly |
| 33 | 116 | XI. Earnings per equity share (not annualised for quarters) (section header) | — | — | — | — | — |
| 34 | 118 | Basic EPS (Rs.) | 12.75 | 12.38 | 12.12 | 49.51 | — |
| 35 | 119 | Diluted EPS (Rs.) | 12.75 | 12.38 | 12.08 | 49.51 | — |

ZERO_STANDING rows: 3 (#14 Exceptional Item, #18 Adjustments of earlier
years, #32 Other Equity). None of the 35 rows are zero/blank across ALL
four columns; the three flagged above are nil in the current reporting
period (and, for #14/#18, also nil in the year-ago quarter) while carrying
values elsewhere, so they are flagged per the "never drop a nil row"
principle rather than the strict all-periods-zero definition.

---

## 3. Board Outcome Letter — Agenda Items (page 1)

Board meeting: started 12:00 P.M., concluded 01:15 P.M. (embedded line 31) —
duration 1 hour 15 minutes.

| # | Line | Agenda item | Detail | Flags |
|---|------|-------------|--------|-------|
| A1 | 23-24 | Unaudited Financial Results of the Company for the quarter ended June 30, 2026 | Approved; accompanied by Limited Review Report from Statutory Auditors (embedded lines 26-29) | — |

Only one bullet item ("•") appears in the letter. Manual sweep of the full
page-1 text (embedded lines 1-46) found no additional agenda items: no AR
approval, no AGM notice, no record date, no dividend, no director
appointment/resignation, no auditor change, no scrutinizer appointment, no
ESOP grant, no capital-raising enabling resolution. Confirmed by targeted
grep (`dividend|AGM|ESOP|scrutinizer|record date|appointment|resignation|
auditor.*change` = 0 matches anywhere in the extract). This is a routine,
single-item quarterly-results board meeting.

---

## 4. Annexures

None present. Grep (`annexure|appendix|schedule`, case-insensitive, full
extract) returns 0 matches; manual sweep of all 5 pages confirms no
annexure, exhibit, or schedule is attached to or embedded in this filing.
No director-profile table, no ESOP annexure, no scrutinizer report annexure.

---

## 5. Auditor's Limited Review Report (pages 4-5) — Paragraph-by-Paragraph

Auditor: Maheshwari & Co., Chartered Accountants, Firm Registration No.
105834W, Surat. Addressed to: The Board of Directors of Venus Pipes & Tubes
Limited (single entity — no consolidated report, no other entity addressed).

| Para | Line | Content type | First 15 words | Flags |
|------|------|--------------|-----------------|-------|
| 1 | 178-183 | Scope of engagement | "We have reviewed the accompanying Statement of Unaudited Financial Results of Venus Pip6 &" | entity name OCR-variant "Venus Pip6" (glyph corruption, unambiguous) |
| 2 | 186-191 | Management's responsibility / basis of preparation (Ind AS 34) | "This Statement which is the responsibility of the Company's Management and approved by the" | — |
| 3 | 194-202 | Basis for conclusion (SRE 2410, moderate assurance, review not audit) | "We conducted our review of the Statement in accordance with the Standard on Review" | explicit statement "we do not express an audit opinion" (line 202) |
| 4 | 209-214 | Conclusion (the opinion paragraph) | "Based on our review conducted as stated above, nothing has come to our attention" | UNMODIFIED / UNQUALIFIED review conclusion |

Attributes required by A2 instructions:
- Opinion type: Unmodified (clean) Limited Review conclusion under SRE 2410 —
  moderate assurance, explicitly NOT an audit opinion.
- Emphasis of Matter paragraph: NONE present.
- Other Matters paragraph: NONE present.
- Going Concern language: NONE present (no going-concern paragraph or
  qualifying language anywhere in the report).
- Entity list reviewed: ONE entity — Venus Pipes & Tubes Limited (standalone/
  entity-only; no subsidiaries, no consolidated scope, consistent with A1's
  scope note).
- Unaudited / management-furnished entities: N/A — single entity, no such
  carve-out language present.
- UDIN: `ILLEGIBLE IN SOURCE` (embedded line 229, cross-checked via OCR at
  line 230; text-layer reading "UDrN: 261qqolq ]Nt)Fl<NII q 8" and OCR
  reading "UDIN: 26A GAODAIAIN DEKNAF4S" disagree and neither is reliable
  per A1). Flag: `ILLEGIBLE_UDIN`.

---

## 6. Consolidation List Entities

| # | Entity | Relationship | Flags |
|---|--------|--------------|-------|
| E1 | Venus Pipes & Tubes Limited (CIN L24311GJ2015PLC082306) | Reporting entity (sole entity in filing) | SCOPE_DISCREPANCY (see header note); no consolidation list exists — filing is single-entity only |

No prior-quarter ledger was supplied ("none available") so no `ENTITY_CHANGE`
diff is possible this cycle; noted for A3/A4 to carry forward for next
quarter's comparison once a prior ledger exists.

---

## 7. Digital / Physical Signature Blocks

| # | Line | Signatory | Designation | Timestamp | Flags |
|---|------|-----------|-------------|-----------|-------|
| S1 | 36-46 | Pavan Kumar Jain | Company Secretary and Compliance Officer, Membership No. A66752 | Digitally signed 2026.08.10 13:19:00 +05'30' | Board meeting concluded 01:15 P.M. (13:15); signature timestamp (13:19) is 4 minutes AFTER conclusion — no TIMING flag, but the margin is tight (noted for awareness, not itself a violation) |
| S2 | 152-161 | [name glyph-corrupted: "&M lg DirectorI"] | Director, DIN 00926613 | Date only: August 10, 2026 (no time stamp); Place: Dhaneti, Bhuj | NAME_GARBLED — signatory's printed name is not legible in the text layer and was not covered by A1's supplementary OCR pass (only page 2 and the page-5 UDIN were OCR-cross-checked); DIN 00926613 is legible |
| S3 | 219-229 | Abhishek Choudhary | Partner, Maheshwari & Co., Chartered Accountants, Firm Regn No. 105834W, Membership No. 149019 | Date only: August 10, 2026 (no time stamp); Place: Surat | UDIN illegible, see section 5 |

---

## COMPANY MEMORY / A1 CARRYOVER NOTES (for A3/A4 reference, not enumerated as separate ledger rows)

- Single operating segment (Note 4, embedded line 142-143) — no segment
  breakout table exists in this filing (consistent, nothing dropped).
- No standalone/consolidated split exists in this filing at all (SCOPE_DISCREPANCY,
  see header).
- Prior-period (Q4 FY26, embedded Note 2 / line 135-136) figures are stated
  as balancing figures (audited FY less 9M unaudited), standard practice,
  noted not flagged.

```yaml
stage: A2-enumerator
company: "VENUSPIPES"
quarter: "Q1 FY27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/venuspipes-q1fy27/work/ledger_results_venuspipes_q1fy27.md"
counts:
  notes: 6
  line_items: 35
  zero_standing: 3
  agenda_items: 1
  auditor_paras: 4
  entities: 1
  annexures: 0
  signature_blocks: 3
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [SCOPE_DISCREPANCY, ZERO_STANDING, TEXT_GARBLED_UNRESOLVED, OCR_USED, ILLEGIBLE_UDIN, NAME_GARBLED, SINGLE_SEGMENT]
gate_a2: pass
mismatch_note: ""
```
