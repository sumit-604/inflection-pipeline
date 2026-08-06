# A2 ENUMERATION LEDGER — GEE Limited (GEE) — Q1 FY27 — RESULTS FILING

Source: `runs/gee-q1fy27/work/extract_results_gee_q1fy27.txt`
Doc composition: Board Outcome letter to BSE (p.1) + Standalone Unaudited Financial
Results statement with notes and director signature (p.2) + Auditor's Limited
Review Report, OCR'd (p.3). All line numbers below are the extract file's own
`cat -n` line numbers (as read by the Read/Grep tools), identical across passes.
Prior-quarter ledger: NONE (first pipeline run for this ticker) — no diff/entity
comparison possible this cycle.

```
=== A2 COUNT TEST ===
category: notes           grep_count: 6   sweep_count: 6   match: yes
category: line_items      grep_count: 28  sweep_count: 28  match: yes
category: zero_standing   grep_count: 4   sweep_count: 4   match: yes
category: agenda_items    grep_count: 5   sweep_count: 5   match: yes
category: auditor_paras   grep_count: 5   sweep_count: 5   match: yes
category: signature_blocks grep_count: 3  sweep_count: 3   match: yes
category: entities         grep_count: 0  sweep_count: 0   match: yes  (standalone filing, no consolidation list — N/A this doctype)
category: annexures        grep_count: 0  sweep_count: 0   match: yes  (Board's Report / Corp Gov Report / other FY25-26 annexures referenced but not present in extract — SCOPE_LIMITATION, see below)
gate_a2: pass
=== END COUNT TEST ===
```

### Methodology notes (for the reconciliation above)
- `notes` — grep pattern `^\s*[0-9]+\.` scoped to lines 111-127 (financial-results
  notes block only, excluded from the auditor-report block to avoid conflating
  note-numbering with auditor-paragraph-numbering). Note 6 uses "6.The results"
  (no space after the period) — still caught by this pattern; flagged for the
  record since a stricter pattern (`^\s*[0-9]+\.\s`) would silently drop it.
- `line_items` — raw non-blank-line count in the table body (lines 73-110) is 31,
  not 28, because three lines are word-wrapped continuations of a single caption
  (line 81 "stock-in-trade" continues line 80; lines 104-105 "XII." / "value of
  Rs.2 Per Share)" continue line 103). Grep pass excludes lines whose first
  non-space character is lowercase (continuation text) and lines that are a bare
  roman numeral marker (`^[IVXL]+\.\s*$`) to land on 28, matching the manual
  sweep exactly. Two structural header rows with no value of their own (IV.
  Expenses; VIII. Tax Expense) are retained as line items per instruction 2
  ("every line item… never drop a row").
- `zero_standing` — grep pass counts data rows whose numeric-token count is below
  the 4-period baseline (padded-whitespace dash cells and blank/NA cells).
  Raw dash-token grep initially returned 3 rows (line 89, 95, 96) because the
  4th zero-standing row (line 106, "Other Equity Excluding Revaluation Reserve")
  presents as blank/NA cells rather than literal "-" for three of four periods;
  a second grep pass on numeric-token-count-per-row surfaced it, and one
  false-positive wrap line (105, matched only because "Rs.2" contains a digit)
  was excluded on manual check. Reconciled sweep = grep = 4.
- `auditor_paras` — grep pattern for numbered paragraphs (`^[0-9]+[.,]`, scoped to
  lines 150-201) returns 4 (paragraphs 2-4 use "N." but paragraph 1 uses "1,"
  with a comma, not a period — both caught by the `[.,]` alternation). A second
  targeted grep for the unnumbered concluding sentence (`^Our conclusion`)
  returns 1 more (line 188). Combined grep = 5 = manual sweep.

---

## 1. NUMBERED NOTES — Financial Results (lines 111-127)

| # | Line(s) | First ~15 words | Flags |
|---|---------|------------------|-------|
| 1 | 112-114 | "The Unaudited Financial Results for the quarter ended June 30, 2026, were reviewed by the Audit Committee..." — LRR carried out per Reg 33 SEBI LODR | |
| 2 | 115-118 | "The Unaudited Financial Results of GEE Limited... are prepared in accordance with the recognition and measurement principles..." (Ind AS, Sec 133, Reg 33) | |
| 3 | 119-120 | "The Company operates mainly in one business segment viz., manufacturing and selling of welding consumables..." — Ind AS 108 segment disclosure N/A | |
| 4 | 122-123 | "During the quarter ended June 30, 2026, the Company sold two of its immovable properties. The resultant profit of Rs.369.55 Lakhs..." disclosed as Exceptional item | ANCHOR: ties to line 89 exceptional-item row |
| 5 | 124-125 | "The previous period figures have been restated, regrouped and rearranged wherever necessary to make them comparable..." | |
| 6 | 126-127 | "The results would be uploaded and available for viewing on the Company's website... and on the website of BSE Limited." — numbered "6.The results" (no space after period) | FORMATTING_ANOMALY (non-standard numbering, does not affect count) |

Note count: **6** (all six numbered; no unnumbered footnotes, asterisks, or
daggers found below the financial table in this extract).

---

## 2. FINANCIAL TABLE LINE ITEMS (all 4 periods; lines 73-110)

Rs. in Lakhs. Columns: Q1FY27 (30-Jun-26, Unaudited) | Q4FY26 (31-Mar-26, Audited)
| Q1FY26 (30-Jun-25, Unaudited) | FY26 (31-Mar-26, Audited, Year Ended).

| # | Line(s) | Item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Type | Flags |
|---|---------|------|--------|--------|--------|------|------|-------|
| 1 | 73 | I. Revenue from operations | 10,285.66 | 11,216.46 | 7,917.70 | 36,913.88 | value | |
| 2 | 74 | II. Other income | 30.89 | 112.49 | 2.27 | 119.75 | value | |
| 3 | 75 | III. Total income (I+II) | 10,316.55 | 11,328.95 | 7,919.97 | 37,033.63 | subtotal | |
| 4 | 77 | IV. Expenses | — | — | — | — | header (no own value) | |
| 5 | 78 | Cost of Raw materials consumed | 6,649.85 | 6,963.08 | 6,535.99 | 25,564.81 | value | |
| 6 | 79 | Purchase of Stock in Trade | 1,360.83 | 1,165.25 | 6.14 | 1,713.82 | value | |
| 7 | 80-81 | Changes in inventories of finished goods, WIP and stock-in-trade | (76.73) | (181.25) | (405.18) | (141.51) | value | word-wrapped caption |
| 8 | 82 | Employee benefit expense | 525.32 | 705.47 | 441.36 | 2,079.18 | value | |
| 9 | 83 | Finance costs | 184.82 | 182.12 | 224.49 | 846.07 | value | |
| 10 | 84 | Depreciation and amortisation expense | 100.74 | 76.64 | 101.55 | 383.08 | value | |
| 11 | 85 | Other Expenses | 1,026.48 | 1,451.17 | 885.21 | 4,357.88 | value | |
| 12 | 86 | Total Expenses (IV) | 9,771.31 | 10,362.48 | 7,789.56 | 34,803.33 | subtotal | |
| 13 | 88 | V. Profit/(Loss) before exceptional items & Tax (III-IV) | 545.25 | 966.47 | 130.41 | 2,230.30 | subtotal | |
| 14 | 89 | VI. Less/(Add): Exceptional items | (369.55) | 333.77 | **-** | 333.77 | value | **ZERO_STANDING** — dash in Q1FY26 col |
| 15 | 90 | VII. Profit/(Loss) after exceptional items before tax (V-VI) | 914.79 | 632.70 | 130.41 | 1,896.53 | subtotal | |
| 16 | 93 | VIII. Tax Expense | — | — | — | — | header (no own value) | |
| 17 | 94 | Current tax | 230.24 | 173.08 | 32.82 | 491.16 | value | |
| 18 | 95 | Previous Year Tax | **-** | 1.04 | **-** | 1.04 | value | **ZERO_STANDING** — dash in Q1FY27 & Q1FY26 cols |
| 19 | 96 | Deferred tax | **-** | 104.47 | **-** | 104.47 | value | **ZERO_STANDING** — dash in Q1FY27 & Q1FY26 cols |
| 20 | 97 | [Tax Expense total, unlabeled] | 230.24 | 278.59 | 32.82 | 596.67 | subtotal | unlabeled row (sum of 17-19) |
| 21 | 99 | IX. Profit/(Loss) for the period (VII-VIII) | 684.55 | 354.11 | 97.59 | 1,299.86 | subtotal | |
| 22 | 100 | X. Other comprehensive income/(Expenses)-net of tax | 0.84 | (1.04) | 0.08 | (0.72) | value | |
| 23 | 101 | XI. Total Comprehensive Income (IX+X) | 685.40 | 353.07 | 97.67 | 1,299.14 | subtotal | |
| 24 | 103-105 | XII. Paid-up equity share capital, Equity shares of Rs.2/- Each (Face value of Rs.2 Per Share) | 1,039.54 | 1,039.54 | 519.77 | 1,039.54 | value | word-wrapped caption; note Q1FY27 share capital = 2x Q1FY26 (₹519.77L → ₹1,039.54L), consistent with a capital event between the two June quarters — anchor check for A4 |
| 25 | 106 | XIII. Other Equity Excluding Revaluation Reserve | (blank) | (blank) | (blank) | 13,475.96 | value | **ZERO_STANDING** — blank/NA for all three non-annual columns; standard practice (balance-sheet item, annual-only disclosure) but flagged so it is not silently skipped |
| 26 | 108 | Earnings per equity share (in Rs.) | — | — | — | — | header (no own value) | |
| 27 | 109 | Basic earnings/(loss) per share | 1.32 | 0.68 | 0.19 | 2.50 | value | |
| 28 | 110 | Diluted earnings/(loss) per share | 1.30 | 0.67 | 0.19 | 2.46 | value | |

Line item count: **28**. Zero/nil/dash-standing rows: **4** (rows 14, 18, 19, 25
above — all flagged `ZERO_STANDING`, none dropped).

---

## 3. BOARD OUTCOME LETTER — AGENDA ITEMS (lines 29-48)

| # | Line(s) | Agenda item | Flags |
|---|---------|-------------|-------|
| 1 | 34-35 | Standalone Un-audited Financial Results for quarter ended June 30, 2026, along with Limited Review Report, enclosed as "Annexure I" | |
| 2 | 36-37 | Adoption and approval of the Board's Report along with the Corporate Governance Report and other annexure(s) for FY 2025-26 | **SCOPE_LIMITATION** — Board's Report / Corp Gov Report / "other annexure(s)" text not present in this extract (see Annexures section below) |
| 3 | 38-39 | Notice of 65th Annual General Meeting, to be held 7th September, 2026 | |
| 4 | 40-43 | Book Closure for 65th AGM: Register of Members / Share Transfer books closed 01st September, 2026 to 7th September, 2026 (Sec 91 Companies Act 2013, Reg 42 SEBI LODR) | |
| 5 | 44-46 | Appointment of Mr. Deep Shukla, Proprietor, M/s. Deep Shukla & Associates (Practicing Company Secretary), as Scrutinizer for e-voting at the 65th AGM | |
| — | 48 | Board meeting timing (not an agenda item; recorded separately per instruction): started 3:45 PM (IST), concluded 4:47 PM (IST) — duration ≈62 minutes for a meeting approving 5 substantive agenda items including AR/AGM/book-closure/scrutinizer | INFORMATIONAL — duration record, not counted in agenda_items total |

Agenda item count: **5**.

---

## 4. DIGITAL SIGNATURE BLOCKS

| # | Line(s) | Signatory | Designation | Timestamp / Date | Context | Flags |
|---|---------|-----------|-------------|-------------------|---------|-------|
| 1 | 52-62 | Sumedha More | Company Secretary & Compliance Officer, Mem. No. 69980 | Digitally signed; 2026.08.06 18:51:30 +05'30' | Board Outcome letter to BSE | Signed ~2h04m after board meeting concluded (4:47 PM) — after, not before, so no timing flag |
| 2 | 129-140 | Umesh Agarwal | Whole Time Director, designated Joint Managing Director, DIN 01209962 | Digitally signed; 2026.08.06 18:46:05 +05'30' — but the adjacent typed date reads "Date : 06th July, 2026" (line 140) | Financial Results statement | **DATE_INCONSISTENCY** — typed date (06 July 2026) contradicts both the digital-certificate timestamp (06 Aug 2026) and the board meeting date (06 Aug 2026) |
| 3 | 190-201 | CA Sankar Garg | SAPD & Associates, Chartered Accountants; FRN 327271E; Membership No. 069240; UDIN 26069240AKMFHN3898 | "Date: The 6th day of August, 2026"; Place: Kolkata; no digital-certificate metadata block (OCR renders the signature image as "Xtra Gn") | Auditor's Limited Review Report | **NO_DIGITAL_TIMESTAMP** — unlike blocks 1 and 2, no "Digitally signed by / Date: YYYY.MM.DD HH:MM:SS" metadata is present; cannot verify signing time against board meeting conclusion |

Signature block count: **3**.

---

## 5. AUDITOR'S LIMITED REVIEW REPORT — PARAGRAPHS (lines 150-201, OCR page 3)

Entity reviewed: GEE LIMITED, standalone only (no subsidiaries / JVs / associates
named — nothing to mark unaudited or management-furnished). Opinion type:
**unmodified / unqualified review conclusion**. No Emphasis of Matter paragraph,
no Other Matters paragraph, no Going Concern paragraph present.

| # | Line(s) | Numbering as printed | Content | Flags |
|---|---------|----------------------|---------|-------|
| 1 | 158-161 | "1," (comma, not period) | Scope: reviewed the Statement of Unaudited Financial Results for quarter ended June 30, 2026, submitted per Reg 33 SEBI LODR | FORMATTING_ANOMALY (comma not period; still counted) |
| 2 | 163-168 | "2." | Management's responsibility: Statement is Management's responsibility, approved by the Board, prepared per Ind AS 34 / Sec 133; auditor's responsibility is to issue a report based on review | |
| 3 | 170-179 | "3." | Basis of review: SRE 2410, moderate assurance, review is less in scope than an audit, no audit opinion expressed | OCR_ARTIFACT: "Weconducted" (missing space), "the causes" (grammar, likely OCR misread of "that causes") |
| 4 | 181-186 | "4." | Conclusion: nothing came to attention causing belief the Statement is not prepared per applicable standards / Reg 33 or contains material misstatement | |
| 5 | 188 | unnumbered | "Our conclusion on the Statement is not modified in respect of the above matters." | Unnumbered concluding sentence — must not be dropped just because it lacks a paragraph number |

Auditor report title/header (lines 150-152, "Independent Auditor's Review
Report on...") and salutation block (154-156, "To / The Board of Directors /
GEE LIMITED") are structural, not counted as paragraphs.

Auditor paragraph count: **5**.

Firm letterhead OCR quality note (lines 144-148): "CHARTERED ACCOUNTANTS decal
ae", "SAPD &ASSOCIATES 6.Litfe Russel Street" — street address is OCR-garbled
and not reliably legible from this extract. Flag `OCR_ARTIFACT`.

---

## 6. CONSOLIDATION ENTITY LIST

Not applicable this filing — the Statement is explicitly **Standalone** (line
34: "Standalone Un-audited Financial Results"). No subsidiary, associate, or
JV list appears anywhere in the extract. Entity count: **0**. No prior-quarter
list available for diff (first pipeline run) — `ENTITY_CHANGE` not applicable.

---

## 7. ANNEXURES

Only "Annexure I" (the Standalone Financial Results + Notes + LRR, already
enumerated in full above in sections 1, 2, and 5) is present in this extract.
Agenda item 2 (section 3 above) references a Board's Report, Corporate
Governance Report, and "other annexure(s) thereto for the Financial Year
2025-26" as separately approved at the same meeting — none of that text,
including any director-profile / DIN / term-date tables, is present in this
A1 extract. Flag **SCOPE_LIMITATION**: A3/A4 should treat the Board's
Report / Corporate Governance Report content as NOT YET REVIEWED rather than
assume it was screened, since it was not captured upstream.

---

## FLAGS RAISED (summary)

- `ZERO_STANDING` — line-item table rows 14, 18, 19, 25 (lines 89, 95, 96, 106)
- `DATE_INCONSISTENCY` — signature block 2 (line 140), typed date 06 July 2026
  vs digital cert / board meeting date 06 Aug 2026
- `NO_DIGITAL_TIMESTAMP` — signature block 3 (auditor, lines 190-201), no
  digital-certificate metadata unlike blocks 1 and 2
- `OCR_ARTIFACT` — auditor letterhead street address (lines 144-148) and
  paragraph-3 text glitches (line 170, 181)
- `FORMATTING_ANOMALY` — note 6 numbering "6.The results" (line 126); auditor
  paragraph 1 numbered with a comma "1," (line 158)
- `SCOPE_LIMITATION` — Board's Report / Corporate Governance Report / other
  FY25-26 annexures referenced at agenda item 2 but absent from this extract

```yaml
stage: A2-enumerator
company: "GEE"
quarter: "Q1 FY27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/gee-q1fy27/work/ledger_results_gee_q1fy27.md"
counts:
  notes: 6
  line_items: 28
  zero_standing: 4
  agenda_items: 5
  auditor_paras: 5
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, DATE_INCONSISTENCY, NO_DIGITAL_TIMESTAMP, OCR_ARTIFACT, FORMATTING_ANOMALY, SCOPE_LIMITATION]
gate_a2: pass
mismatch_note: ""
```
