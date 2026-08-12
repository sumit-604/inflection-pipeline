# A2 ENUMERATION LEDGER — Scoda Tubes Limited (SCODATUBES), Q1 FY27, Results (RE-ENUMERATION vs corrected A1 extract)

Source: `/home/user/inflection-pipeline/runs/scodatubes-q1fy27/work/extract_results_scodatubes_q1fy27.txt`
Scope: filing body only, lines 1-204. Lines 205-289 are A1 extraction/integrity metadata
(corrections table + footing proof) and are NOT enumerated as Reg 33 filing disclosure units —
they are cited here only as provenance for the CORRECTED flag on affected line items.
Prior-quarter ledger: NONE (first quarterly run for this ticker) — no ENTITY_CHANGE /
DROPPED_SLIDE cross-check possible this cycle.

```
=== A2 COUNT TEST ===
category: notes             grep_count: 7    sweep_count: 7    match: yes
category: line_items        grep_count: 25   sweep_count: 25   match: yes
category: zero_standing     grep_count: 3    sweep_count: 3    match: yes
category: agenda_items      grep_count: 1    sweep_count: 1    match: yes
category: auditor_paras     grep_count: 4    sweep_count: 4    match: yes
category: entities          grep_count: 1    sweep_count: 1    match: yes
category: signatories       grep_count: 3    sweep_count: 3    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used (against the extract file):
- notes: `sed -n '114,204p' extract | grep -n -E "^\s*[0-9]+\s+[A-Z]"` -> 7
- line_items: manual enumeration of lines 80-112 minus 7 pure category-header rows
  (80, 84, 95, 100, 101, 108, 109 carry no values of their own) -> 25 value-bearing rows
- zero_standing: lines 81-112 (excluding the 7 header rows above) containing no digit
  0-9 anywhere in the row -> lines 93, 97, 111 -> 3
- agenda_items: `sed -n '34,45p' extract | grep -n -E "^[0-9]+\."` -> 1
- auditor_paras: `sed -n '154,186p' extract | grep -n -E "^\s*[0-9]+\.\s"` -> 4
- entities: `grep -n -i "subsidiary" extract` -> 1 (Note 5)
- signatories: `grep -n "DIN"` (2 hits, lines 53 and 143) + `grep -n "UDIN"` (1 hit, line 197) -> 3

---

## 1. Numbered Notes (7)

| # | Line | First ~15 words |
|---|------|------------------|
| 1 | 115 | "The above financial results of Scoda Tubes limited ('the Company') for the quarter and year ended June 30, 2026 have been reviewed..." |
| 2 | 118 | "The above financial results have been prepared in accordance with Indian Accounting Standards (Ind AS) notified under Section 133..." |
| 3 | 120 | "The format of the above results as prescribed in SEBI's Circular CIR/CFD/CMD/15/2015 dated 30th November, 2015 has been modified..." |
| 4 | 122 | "The company is dealing in manufacturing of stainless-steel (SS) pipes and tubes only. Hence, segment reporting as defined in Ind AS 108 is not applicable." |
| 5 | 123 | "The company does not have any subsidiary, joint venture or associate company as on June 30, 2026. Hence, the requirement to present consolidated financial results..." |
| 6 | 125 | "The figures for the quarter ended March 31, 2026 are the balancing figures between the audited figures for the year ended March 31, 2026..." |
| 7 | 127 | "Previous Period's figures have been regrouped / restated, wherever considered necessary to confirm current period classification." |

Manual sweep for unnumbered notes/footnotes (asterisks, daggers, "Note:" prefixes below tables):
one stray `*` glyph at line 145, positioned inside the signature/seal block (OCR artifact from the
company round stamp graphic, not a footnote marker; no accompanying text) — flagged `OCR_ARTIFACT`,
not counted as a note. No other unnumbered notes found. Table header cross-references "(Refer Notes
below)" (line 78) and "(Refer Note No 6)" (line 78, Q4FY26 column) are pointers into the 7 notes
above, not separate notes.

## 2. Financial statement line items (25), all 4 periods: Q1FY27 (30/06/2026) | Q4FY26 (31/03/2026, balancing fig. per Note 6) | Q1FY26 (30/06/2025) | FY26 (31/03/2026, audited)

All values in Rs. Millions as filed. `CORRECTED` flag = value on this row/period was corrected by A1
in this re-extraction pass (digit substitution from the embedded-text-layer OCR fault, per A1
CORRECTIONS table, extract lines 230-248); value shown below is the corrected, footed figure now
resident in the body at the cited line.

| Line | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|------|------|--------|--------|--------|------|-------|
| 81 | Revenue from operations | 1,243.45 | 1,235.69 | 974.17 | 5,186.50 | |
| 82 | Other Income | 16.30 | 44.03 | 17.61 | 105.71 | |
| 83 | Total Income | 1,259.75 | 1,279.72 | 991.78 | 5,292.21 | CORRECTED (Q1FY27, Q4FY26, Q1FY26) |
| 85 | Cost of raw materials and components consumed | 1,001.65 | 1,007.73 | 742.49 | 4,143.75 | CORRECTED (Q4FY26, Q1FY26) |
| 86 | Changes in inventories of finished goods and WIP | (156.14) | (183.41) | (52.47) | (611.44) | |
| 87 | Employee benefit expenses | 24.62 | 26.34 | 24.20 | 104.54 | |
| 88 | Finance costs | 64.81 | 81.39 | 51.04 | 248.66 | |
| 89 | Depreciation and amortization expenses | 41.31 | 36.12 | 15.72 | 92.17 | CORRECTED (Q1FY26, footing); Q4FY26 spacing-only artifact cleaned |
| 90 | Other expenses | 213.53 | 217.98 | 118.05 | 787.21 | CORRECTED (Q4FY26) |
| 91 | Total Expenses | 1,189.78 | 1,186.15 | 899.03 | 4,764.89 | CORRECTED (FY26) |
| 92 | Profit/(loss) before exceptional items and tax | 69.97 | 93.57 | 92.75 | 527.32 | CORRECTED (Q1FY27, Q4FY26, FY26) |
| 93 | Exceptional items | — | — | — | — | ZERO_STANDING |
| 94 | Profit/(loss) before tax | 69.97 | 93.57 | 92.75 | 527.32 | CORRECTED (Q1FY27, Q4FY26, FY26) |
| 96 | Current tax | 6.25 | 25.72 | 18.90 | 116.33 | CORRECTED (Q4FY26) |
| 97 | Earlier year taxes | — | — | — | — | ZERO_STANDING |
| 98 | Deferred tax liability/(asset) | 11.22 | 4.66 | 3.02 | 22.56 | |
| 99 | Profit/(loss) for the period (PAT) | 52.50 | 63.19 | 70.83 | 388.43 | CORRECTED (Q1FY26: was 10.83 in prior corrupt pass, now 70.83) |
| 102 | OCI — Re-measurements of defined benefit plans | 1.71 | (1.47) | 1.47 | 1.18 | |
| 103 | OCI — Income tax effects on the above | (0.43) | 0.37 | (0.37) | (0.30) | CORRECTED (Q4FY26) |
| 104 | Total comprehensive income/(loss) for the period | 53.78 | 62.09 | 71.93 | 389.31 | CORRECTED (Q1FY27, Q1FY26) |
| 106 | Paid-up equity share capital (FV Rs.10/share) | 599.09 | 599.09 | 599.09 | 599.09 | |
| 107 | Other Equity | — | — | — | 3,304.00 | populated only in audited annual column; not flagged ZERO_STANDING (has a value in 1 of 4 periods, not all) |
| 110 | EPS — Basic/Diluted, Continuing Operations (Rs., not annualized) | 0.88 | 1.02 | 1.44 | 6.79 | |
| 111 | EPS — Basic/Diluted, Discontinued Operations (Rs.) | — | — | — | — | ZERO_STANDING |
| 112 | EPS — Basic/Diluted, Continued + Discontinued Operations (Rs.) | 0.88 | 1.02 | 1.44 | 6.79 | |

Category-header rows excluded from the 25 (carry no values of their own; content is in the
sub-items already listed): line 80 "Income from Operations", line 84 "Expenses", line 95 "Tax
Expense", line 100 "Other comprehensive income/(expenses)", line 101 "(i) items that will not be
reclassified to profit or loss", line 108 "Earning per share", line 109 "(of Rs. 10/- each) (not
annualized)".

ZERO_STANDING items (3): line 93 Exceptional items, line 97 Earlier year taxes, line 111 EPS from
Discontinued Operation — each blank/dash in all 4 periods; retained as standing template line items
per SEBI format, not dropped.

## 3. Board Outcome letter — agenda items (1) and meeting timing

| Line | Agenda item | Detail |
|------|-------------|--------|
| 38-39 | 1. Considered, approved and taken on record the Unaudited Financial Results for the quarter ended June 30, 2026 along with the Limited Review Report | Sole agenda item. No other items (no AR approval, no AGM notice, no record date, no dividend, no director appointment/resignation, no auditor change, no scrutinizer appointment, no ESOP grant, no capital-raising enabling resolution) found on sweep of lines 34-46. |

Board meeting timing (line 36-37): commenced 04:00 P.M., concluded 05:00 P.M. — 1 hour duration.

## 4. Auditor's Limited Review Report — paragraphs (4) and metadata

| Para | Line | Content |
|------|------|---------|
| 1 | 158-161 | Scope statement: reviewed the Statement of Unaudited Financial Results for the quarter ended June 30, 2026, submitted pursuant to Reg 33 of SEBI LODR 2015. |
| 2 | 162-167 | Responsibility statement: Statement is Management's responsibility, approved by the Board, prepared per Ind AS 34; auditor's responsibility is to express a conclusion based on review. |
| 3 | 169-178 | Review conducted per SRE 2410 (ICAI); review substantially less in scope than an audit under s.143(10); no audit opinion expressed. |
| 4 | 179-185 | Conclusion: unmodified — "nothing has come to our attention that causes us to believe" the Statement is not prepared per Ind AS / has not disclosed required Reg 33 information / contains material misstatement. |

Opinion type: unmodified conclusion. Emphasis of Matter: none present. Other Matters paragraph:
none present. Going Concern paragraph: none present. Entity reviewed: Scoda Tubes Limited,
standalone only (consistent with Note 5, no subsidiary/JV/associate — no unaudited or
management-furnished component entities in scope).

Firm: Dhirubhai Shah & Co LLP, Chartered Accountants, FRN 102511W/W100298 (line 190).
Signing partner: M. No. 134475 (name not printed in the extracted text on the signature block,
lines 188-197; only membership number and firm name are legible/OCR'd).
UDIN: 26134475LRVGGI8483 (line 197).
Report date/place: Rajpur, Mehsana; August 12, 2026 (line 194-195) — same date as the Board meeting.

## 5. Reporting entity (1)

| Line | Entity | Relationship | Note |
|------|--------|--------------|------|
| 123-124 | Scoda Tubes Limited | Standalone reporting entity; no subsidiary, joint venture or associate as on June 30, 2026 | Note 5 — consolidated results requirement not applicable |

No prior-quarter entity list supplied (first quarterly run) — ENTITY_CHANGE cross-check not
performable this cycle; flag as carry-forward task for the next quarterly cycle.

## 6. Signatory / signature blocks (3)

| Line | Signatory (as printed/OCR'd) | Designation | DIN/UDIN | Flags |
|------|-------------------------------|-------------|----------|-------|
| 51-53 | "Jagrutkushar Rameshbhai" (tesseract 400dpi OCR output verbatim; first name atypical for standard Gujarati naming convention, possibly "Jagrutkumar" — NOT independently confirmed elsewhere in the document) | Managing Director | DIN: 06785595 (embedded text layer, clean, not in question) | NAME_OCR_UNCERTAIN |
| 141-143 | "Bharatbhai Patel" (per task-level confirmed reading; raw OCR in extract is garbled: "s~ Bh: :;bhal Patel") | Chairman and Whole-time Director | DIN: 08036100 | OCR_GARBLED_RAW (name resolved via corroborating source outside raw OCR text; treat DIN as primary confirmed identifier) |
| 188-197 | Auditor signature block — partner name not printed/OCR'd; only M. No. and firm given | Partner, for Dhirubhai Shah & Co LLP, Chartered Accountants | M. No. 134475; UDIN 26134475LRVGGI8483 | PARTNER_NAME_NOT_CAPTURED |

No digital-signature timestamp (time-of-day) was captured in the extracted text for any of the
three blocks — only dates (August 12, 2026, matching the Board meeting date for all three). Cannot
test "signature before board meeting concluded" without a captured timestamp; flagged
`NO_SIGNATURE_TIMESTAMP_CAPTURED` for A3/A4 to note as an evidence gap rather than resolve as
clean.

---

## A1 correction cross-reference (provenance only, not itself an enumerated filing unit)

Every line item above flagged CORRECTED was verified in the A1 CORRECTIONS table (extract lines
230-248) and the A1 FOOTING PROOF block (extract lines 257-289): all 4 periods (Q1FY27, Q4FY26,
Q1FY26, FY26) foot cleanly across all 5 identities (Total Income, Total Expenses, PBT, PAT, TCI) —
20/20 checks pass. The single highest-materiality correction: Q1FY26 PAT at line 99 is 70.83 (not
the previously corrupt 10.83) — a 6.5x understatement in the prior pass now resolved.
