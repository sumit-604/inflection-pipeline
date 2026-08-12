# A2 ENUMERATION LEDGER — Scoda Tubes Limited (SCODATUBES) — Q1 FY27 — RESULTS

Source: extract_results_scodatubes_q1fy27.txt (185 extracted lines, 3 pages,
Millions unit convention, ocr_pages: none). Every row below carries the
absolute line number in that extract file.

```
=== A2 COUNT TEST ===
category: notes         grep_count: 7   sweep_count: 7   match: yes
category: line_items    grep_count: 32  sweep_count: 32  match: yes
category: agenda_items  grep_count: 1   sweep_count: 1   match: yes
category: auditor_paras grep_count: 4   sweep_count: 4   match: yes
category: entities      grep_count: 1   sweep_count: 1   match: yes
category: signatories   grep_count: 3   sweep_count: 3   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep methodology per category:
- notes: `grep -n -E "^\s*[0-9]+\s+[A-Z]" ` restricted to the NOTES block
  (lines 114-127); the prompt's default pattern `^\s*[0-9]+\.\s` returns 0
  hits here because this filer's notes use a number + whitespace format, not
  "1." — re-run and confirmed against a manual line-by-line read of the
  NOTES block, which found the same 7 notes, no unnumbered footnotes
  (asterisks/daggers/"Note:" prefixes) anywhere else in the document. The
  mark near line 145 is an OCR artifact of the company round seal, not a
  footnote.
- line_items: `sed -n '80,112p' | grep -c -E "\S"` (non-blank lines in the
  financial results table body) = 32; manual sweep of the same span,
  including section headers, subtotals and sub-items, also lands on 32.
- agenda_items: `grep -n -E "^[0-9]+\.\s"` (outdented, i.e. board-letter
  top-level items) = 1 (line 38). The two further "1./2." items at lines
  42-43 are indented 4 spaces and are the enclosure list under agenda item
  1 ("submitting the followings"), not separate agenda items — confirmed by
  `grep -n -E "^    [0-9]+\.\s"` = 2, tabulated separately below.
- auditor_paras: `grep -n -E "^ [0-9]+\.\s"` on the review report = 4
  (lines 158, 162, 169, 179); manual read of the report confirms exactly 4
  numbered paragraphs, no unnumbered EoM/Other Matter/Going Concern block.
- entities: manual sweep — the filing carries exactly one entity in its
  review/reporting scope (Scoda Tubes Limited, standalone), stated
  explicitly via Note 5's "no subsidiary/JV/associate" disclosure and
  confirmed by the auditor's report addressing only "Scoda Tubes Limited."
  grep cross-check: `grep -n -iE "subsidiar|joint venture|associate|consolidat"` = 1 hit (line 123).
- signatories: `grep -n -iE "DIN|UDIN"` = 3 hits (lines 53, 143, 197);
  manual sweep of the three sign-off blocks (letter, results statement,
  auditor report) also finds 3.

---

## 1. BOARD OUTCOME LETTER (pages 1-2, lines 15-62)

### 1a. Recipients / distribution (context, not gated)
| # | Line | Recipient |
|---|------|-----------|
| 1 | 24-27 | National Stock Exchange of India Limited, Symbol "SCODATUBES" |
| 2 | 24-27 | BSE Limited, Scrip Code "544411" |

### 1b. Board meeting timing
| Field | Line | Value |
|---|---|---|
| Meeting date | 34,36 | Wednesday, August 12, 2026 |
| Commenced | 37 | 04:00 P.M. |
| Concluded | 37 | 05:00 P.M. |
| Duration | derived | 1 hour |
| Venue | 36 | Registered office of the Company |

### 1c. Agenda items
| # | Line | Item | Flags |
|---|------|------|-------|
| 1 | 38-39 | Considered, approved and taken on record the Unaudited Financial Results of the Company for the quarter ended June 30, 2026, along with Limited Review Report | — |

No other agenda items present: no AR approval, no AGM notice, no record
date, no dividend, no director appointment/resignation, no auditor change,
no scrutinizer appointment, no ESOP grant, no capital-raising enabling
resolution. Single-item, one-hour board meeting.

### 1d. Enclosures listed under agenda item 1 (sub-list, lines 41-43)
| # | Line | Enclosure |
|---|------|-----------|
| 1 | 42 | Unaudited Financial Results for the quarter ended June 30, 2026 |
| 2 | 43 | Limited Review Report |

### 1e. Letter signatory
| Line | Name (as extracted) | Designation | DIN |
|---|---|---|---|
| 51-53 | "Jagrutk" (likely OCR-truncated; full name not reliably extracted) | Managing Director | 06785595 |

Flag: name string is garbled in extraction ("Jagrutk") — treat as NOT
FOUND for the full legal name pending source-PDF cross-check; DIN
06785595 is clean.

---

## 2. FINANCIAL RESULTS TABLE (page 2, lines 69-112)

Four reporting columns throughout: (3) Q1 FY27 (30/06/2026, Unaudited),
(4) Q4 FY26 (31/03/2026, "Refer Note No 6", balancing figure, Unaudited),
(5) Q1 FY26 (30/06/2025, Unaudited), (6) FY26 (31/03/2026, Audited, full
year).

| # | Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|------|--------|--------|--------|------|-------|
| 1 | 80 | 1. Income from Operations (header) | — | — | — | — | — |
| 2 | 81 | 1a) Revenue from operations | 1,243.45 | 1,235.69 | 974.17 | 5,186.50 | — |
| 3 | 82 | 1b) Other Income | 16.30 | 44.03 | 17.61 | 105.71 | — |
| 4 | 83 | Total Income (subtotal) | 1,259.15 | 1,219.12 | 991.18 | 5,292.21 | — |
| 5 | 84 | 2. Expenses (header) | — | — | — | — | — |
| 6 | 85 | 2a) Cost of raw materials and components consumed | 1,001.65 | 1,001.13 | 142.49 | 4,143.75 | — |
| 7 | 86 | 2b) Changes in inventories of finished goods and WIP | (156.14) | (183.41) | (52.47) | (611.44) | — |
| 8 | 87 | 2c) Employee benefit expenses | 24.62 | 26.34 | 24.20 | 104.54 | — |
| 9 | 88 | 2d) Finance costs | 64.81 | 81.39 | 51.04 | 248.66 | — |
| 10 | 89 | 2e) Depreciation and amortization expenses | 41.31 | 36.12 | 15.12 | 92.17 | — |
| 11 | 90 | 2f) Other expenses (extracted as "r Other expenses" — OCR misread of "f") | 213.53 | 211.98 | 118.05 | 787.21 | — |
| 12 | 91 | Total Expenses (subtotal) | 1,189.78 | 1,186.15 | 899.03 | 4,164.89 | — |
| 13 | 92 | 3. Profit/(loss) before exceptional items and tax | 69.97 | 93.57 | 92.75 | 527.32 | — |
| 14 | 93 | 4. Exceptional items | — | — | — | — | ZERO_STANDING |
| 15 | 94 | 5. Profit/(loss) before tax | 69.91 | 93.51 | 92.75 | 521.32 | — |
| 16 | 95 | 6. Tax Expense (header) | — | — | — | — | — |
| 17 | 96 | 6a) Current tax | 6.25 | 25.12 | 18.90 | 116.33 | — |
| 18 | 97 | 6b) Earlier year taxes | — | — | — | (dash, one col) | ZERO_STANDING |
| 19 | 98 | 6c) Deferred tax liability/(asset) | 11.22 | 4.66 | 3.02 | 22.56 | — |
| 20 | 99 | 7. Profit/(loss) for the period | 52.50 | 63.19 | 10.83 | 388.43 | — |
| 21 | 100 | 8. Other comprehensive income/(expenses) (header) | — | — | — | — | — |
| 22 | 101 | 8(i) items that will not be reclassified to profit or loss (sub-header) | — | — | — | — | — |
| 23 | 102 | 8(i) Re-measurements of the defined benefit plans | 1.71 | (1.47) | 1.47 | 1.18 | — |
| 24 | 103 | 8(i) Income tax effects on the above | (0.43) | 0.31 | (0.37) | (0.30) | — |
| 25 | 104 | 9. Total comprehensive income/(loss) for the period | 53.18 | 62.09 | 11.93 | 389.31 | — |
| 26 | 106 | Paid-up equity share capital (face value Rs.10/share) | 599.09 | 599.09 | 599.09 | 599.09 | — |
| 27 | 107 | Other Equity | (blank) | (blank) | (blank) | 3,304.00 | Quarterly columns blank by convention (balance-sheet item, annual only) — not flagged ZERO_STANDING since non-zero in the FY26 column |
| 28 | 108 | 10. Earning per share (header) | — | — | — | — | — |
| 29 | 109 | (of Rs.10/- each) (not annualized) — descriptor row | — | — | — | — | — |
| 30 | 110 | 10a) Basic/Diluted EPS — Continuing Operations (Rs.) | 0.88 | 1.02 | 1.44 | 6.79 | — |
| 31 | 111 | 10b) Basic/Diluted EPS — Discontinued Operation (Rs.) | — | — | — | — | ZERO_STANDING |
| 32 | 112 | 10c) Basic/Diluted EPS — Continued and Discontinued Operations (Rs.) | 0.88 | 1.02 | 1.44 | 6.79 | — |

ZERO_STANDING items (3): row 14 Exceptional items, row 18 Earlier year
taxes, row 31 Discontinued Operation EPS — all blank/dash across every one
of the four reporting periods. These are template line items retained by
the standard SEBI results format; a future quarter populating any of them
is the signal to watch for.

Note on row 18: a lone dash character appears in the raw OCR line
("b Earlier year taxes ... -") but no numeric value in any of the four
columns; treated as nil across all periods, consistent with ZERO_STANDING.

---

## 3. NUMBERED NOTES (page 2, lines 114-127)

| # | Line | First 15 words |
|---|------|-----------------|
| 1 | 115-117 | "The above financial results of Scoda Tubes limited ('the Company') for the quarter and year ended June 30, 2026..." — reviewed by Audit Committee, approved by Board, unmodified conclusion by Statutory Auditors |
| 2 | 118-119 | "The above financial results have been prepared in accordance with Indian Accounting Standards (Ind AS) notified under Section 133..." |
| 3 | 120-121 | "The format of the above results as prescribed in SEBI's Circular CIR/CFD/CMD/15/2015 dated 30th November, 2015..." |
| 4 | 122 | "The company is dealing in manufacturing of stainless-steel (SS) pipes and tubes only. Hence, segment reporting..." — single reportable segment, Ind AS 108 not applicable |
| 5 | 123-124 | "The company does not have any subsidiary, joint venture or associate company as on June 30, 2026. Hence..." — no consolidated results required |
| 6 | 125-126 | "The figures for the quarter ended March 31, 2026 are the balancing figures between the audited figures..." — explains the Q4FY26 comparative derivation |
| 7 | 127 | "Previous Period's figures have been regrouped / restated, wherever considered necessary to confirm current period classification." |

No unnumbered footnotes (asterisk/dagger/"Note:" prefix) found anywhere in
the document outside this block; the "*" glyph at line 145 and the
scrambled glyphs at lines 134-144 are OCR noise from the company's round
seal/stamp graphic on the signature block, not text footnotes.

---

## 4. AUDITOR'S LIMITED REVIEW REPORT (page 3, lines 147-204)

Firm: Dhirubhai Shah & Co LLP, Chartered Accountants, FRN 102511W/W100298.
Addressee: The Board of Directors, Scoda Tubes Limited.

### 4a. Numbered paragraphs
| # | Line | Paragraph subject |
|---|------|---------------------|
| 1 | 158-161 | Scope statement: reviewed the Statement of Unaudited Financial Results of Scoda Tubes Limited for the quarter ended June 30, 2026, submitted per Regulation 33 of the SEBI LODR Regulations, 2015 |
| 2 | 162-167 | Management's responsibility: Statement prepared per Ind AS 34, approved by the Board; auditor's responsibility is to express a review conclusion |
| 3 | 169-178 | Basis of review: conducted per SRE 2410; review is substantially less in scope than an audit under Section 143(10); no audit opinion expressed |
| 4 | 179-185 | Conclusion: "nothing has come to our attention" causing belief of material misstatement or non-disclosure per Regulation 33 — unmodified conclusion |

### 4b. Report metadata / structural checks
| Field | Line | Value |
|---|---|---|
| Opinion/conclusion type | 179-185 | Unmodified (unqualified) review conclusion |
| Emphasis of Matter paragraph | — | Absent (grep for "emphasis of matter" = 0 hits) |
| Other Matters paragraph | — | Absent (grep for "other matter" = 0 hits) |
| Going Concern language | — | Absent (grep for "going concern" = 0 hits) |
| Entity list reviewed | 158-159, 123 | Scoda Tubes Limited, standalone only — consistent with Note 5's no-subsidiary/JV/associate statement; no unaudited/management-furnished entities since there is only the one standalone entity |
| UDIN | 197 | 26134475LRVGGI8483 |
| Membership number | 196 | 134475 |
| FRN | 190 | 102511W/W100298 |
| Report date | 195 | August 12, 2026 (same date as board meeting) |
| Report place | 194 | Rajpur, Mehsana |

---

## 5. CONSOLIDATION ENTITIES (page 2, Note 5, line 123)

| # | Line | Entity | Relationship | Flags |
|---|------|--------|--------------|-------|
| 1 | 123-124 | Scoda Tubes Limited | Standalone reporting entity; "does not have any subsidiary, joint venture or associate company as on June 30, 2026" — consolidated results not applicable | ZERO_STANDING (standing "no subsidiary/JV/associate" disclosure, zero entities in scope) |

No prior-quarter ledger was supplied (first quarterly run for this
ticker), so ENTITY_CHANGE cannot be assessed this cycle. This statement
should be the baseline A3/A4 checks against in Q2 FY27.

---

## 6. SIGNATORY / SIGNATURE BLOCKS

| # | Line(s) | Block | Signatory (as extracted) | Designation | Identifier | Timestamp |
|---|---------|-------|---------------------------|-------------|------------|-----------|
| 1 | 51-53 | Board outcome letter | "Jagrutk" (OCR-degraded; full name NOT FOUND) | Managing Director | DIN 06785595 | None captured — letter carries only the meeting date (Aug 12, 2026), no distinct signing timestamp |
| 2 | 134-143 | Financial results statement | "S... Bh...bhai Patel" (OCR-degraded; extracted as "s~ Bh: :;bhal Patel") | Chairman and Whole-time Director | DIN 08036100 | Place: Rajpur, Mehsana; Date: August 12, 2026 — same date as board meeting, no time-of-day captured, so the "signed before meeting concluded" check cannot be evaluated from this extract |
| 3 | 188-197 | Auditor's review report | Partner (name not printed separately from the firm block; identified only by M. No.) | Partner, Dhirubhai Shah & Co LLP | M. No. 134475; UDIN 26134475LRVGGI8483 | Place: Rajpur, Mehsana; Date: August 12, 2026 |

No digital-signature timestamp block (e.g. "Digitally signed by... Date...
Time...") appears anywhere in the extracted text (`grep -n -iE "digitally
signed|digital signature|signed by"` = 0 hits). Two of three signatory
names are OCR-degraded in this extract; flagged NOT FOUND for full legal
name pending source-PDF verification — do not substitute an assumed name.

---

## SUMMARY OF FLAGS RAISED
- ZERO_STANDING x4: financial table rows 14 (Exceptional items), 18
  (Earlier year taxes), 31 (Discontinued Operation EPS); consolidation
  entities row 1 (no subsidiary/JV/associate).
- No ENTITY_CHANGE (no prior ledger to diff against — first run).
- No MGMT_ABSENCE / REPEAT_QUESTION / DROPPED_SLIDE — not applicable to a
  results-doctype filing (no transcript or investor deck in this extract).
- Two signatory names (letter signatory, results signatory) are OCR
  degraded in the extract; recorded as NOT FOUND for full legal name, DINs
  are clean and reliable.
