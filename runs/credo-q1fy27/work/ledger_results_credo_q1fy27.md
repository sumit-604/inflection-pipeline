=== A2 COUNT TEST ===
category: notes            grep_count: 8    sweep_count: 8    match: yes
category: line_items       grep_count: 34   sweep_count: 34   match: yes
category: zero_standing    grep_count: 4    sweep_count: 4    match: yes
category: agenda_items     grep_count: 10   sweep_count: 10   match: yes
category: auditor_paras    grep_count: 9    sweep_count: 9    match: yes
category: entities         grep_count: 1    sweep_count: 1    match: yes
gate_a2: pass
=== END COUNT TEST ===

RECONCILIATION NOTE (notes category): first grep pass on pattern `^\s*[0-9]+\s` inside
the Notes block (lines 201-231) returned only notes 2-8 (7 hits). Manual sweep read the
paragraph immediately under the "Notes:" header (line 203-204) and found it is Note 1
("The Financial Results for the quarter... were reviewed by the Audit Committee...") with
its leading digit "1" dropped by OCR (the OCR engine also mangled "The" to "Toe" on the
same line, consistent with a scan-quality artifact, not a missing note). Re-grep targeted
at the anchor phrase "were reviewed by the Audit Committee" confirmed exactly one match at
line 203. Final reconciled count: notes = 8 (1-8), grep and sweep now agree. GATE A2 pass
on this category only after the re-sweep; flagged below as OCR_ARTIFACT.

Source document: Un-audited Standalone Financial Results (Q1 FY27, quarter ended June 30,
2026) + Board Outcome cover letter + Independent Auditor's Limited Review Report.
Unit convention per A1 header: Millions (x0.1 to Rs Cr). All amounts below are transcribed
as printed in the extract (Millions), unconverted — conversion is not an A2 function.
No consolidated financials, no investor presentation, no concall transcript in this filing
set (single-segment, standalone-only company per Note 7).

---

## 1. BOARD OUTCOME LETTER — CONTEXT ROWS (not counted toward agenda_items metric)

| # | Item | Line(s) | Detail | Flags |
|---|------|---------|--------|-------|
| C1 | Addressees | 18-24 | To BSE Limited (Scrip Code 544058) and National Stock Exchange of India Limited (Scrip Symbol MUFTI) | |
| C2 | Regulatory basis | 30-31 | Pursuant to Regulations 30 and 33, SEBI LODR Regulations 2015 | |
| C3 | Board meeting timing | 40 | Commenced 4:45 p.m., concluded 6:00 p.m. — duration 1 hr 15 min | |
| C4 | Website upload confirmation | 42 | "This intimation is also being uploaded on the Company's website at www.credobrands.in" | |
| C5 | Digital signature block | 47-55 | Signatory: Sanjay Kumar Mutha, Company Secretary and Compliance Officer. "Digitally signed by Sanjay Kumar Mutha Date: 2026.08.11 18:20:44 +05'30'". Signature timestamp (18:20:44) is AFTER stated board conclusion (18:00) — no timing anomaly. | |
| C6 | Letter enclosure statement | 37-38 | Encloses Un-audited Standalone Financial Results + Independent Auditor's Review Report | |

## 2. BOARD OUTCOME LETTER — AGENDA ITEMS (counted; agenda_items = 10)

| # | Agenda item | Line(s) | Status | Flags |
|---|------|---------|--------|-------|
| A1 | Approval of Un-audited Standalone Financial Results, quarter ended June 30, 2026, as recommended by the Audit Committee at its meeting held the same day | 28-38 | PRESENT — the sole substantive item in this outcome letter | |
| A2 | Annual Report (AR) approval | — | NOT DISCLOSED in this letter (grep for "AR"/"annual report" approval keyword: 0 hits) | AGENDA_NOT_DISCLOSED |
| A3 | AGM notice | — | NOT DISCLOSED (grep "agm": 0 hits) | AGENDA_NOT_DISCLOSED |
| A4 | Record date | — | NOT DISCLOSED (grep "record date": 0 hits) | AGENDA_NOT_DISCLOSED |
| A5 | Dividend | — | NOT DISCLOSED (grep "dividend": 0 hits) | AGENDA_NOT_DISCLOSED |
| A6 | Director appointment / resignation | — | NOT DISCLOSED (grep "director" within letter body beyond boilerplate "Board of Directors": 0 substantive hits) | AGENDA_NOT_DISCLOSED |
| A7 | Auditor change | — | NOT DISCLOSED (grep "auditor" in letter: 0 hits; auditor referenced only as reviewer of results, not a change event) | AGENDA_NOT_DISCLOSED |
| A8 | Scrutinizer appointment | — | NOT DISCLOSED (grep "scrutin": 0 hits) | AGENDA_NOT_DISCLOSED |
| A9 | New ESOP grant (distinct from exercise reported in Note 4) | — | NOT DISCLOSED as a board-outcome agenda item (grep "esop" in letter: 0 hits; ESOP allotment on exercise is reported only in financial-statement Note 4, not as a board agenda item in this letter) | AGENDA_NOT_DISCLOSED |
| A10 | Capital-raising enabling resolution | — | NOT DISCLOSED (grep "capital rais": 0 hits) | AGENDA_NOT_DISCLOSED |

## 3. NUMBERED NOTES (notes = 8)

| Note # | Line(s) | First ~15 words |
|---|---|---|
| 1 | 203-204 | "The Financial Results for the quarter ended June 30, 2026 were reviewed by the Audit Committee..." (leading digit OCR-dropped; see reconciliation note) — OCR_ARTIFACT |
| 2 | 206-208 | "The Financial Results have been prepared in accordance with the recognition and measurement principles..." |
| 3 | 210-211 | "The figures for the quarter ended March 31, 2026 are the balancing figures between the audited..." |
| 4 | 213-214 | "During the quarter under review, the Company has allotted an aggregate of 24,000 Equity Shares..." |
| 5 | 216-223 | "During the year ended March 31, 2026, the Central Government of India has notified the Code on Wages, 2019..." |
| 6 | 225-226 | "Based on the 'management approach' as defined in Ind AS 108-Operating Segments, the Chief Operating Decision Maker..." |
| 7 | 228 | "During the period under review, the company doesn't have any subsidiary, associate and joint venture company." |
| 8 | 230-231 | "These financial results are available on the website of the Company viz. www.credobrands.in..." |

## 4. FINANCIAL TABLE LINE ITEMS (line_items = 34; zero_standing = 4)

Columns per source: Q1 FY27 (Jun 30, 2026, Unaudited) / Q4 FY26 (Mar 31, 2026, balancing fig. per Note 3) / Q1 FY26 (Jun 30, 2025, Unaudited) / FY26 (Mar 31, 2026, Audited). Values as printed in Millions (unconverted).

| # | Line item | Line(s) | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | Income (header, item 1) | 140 | — | — | — | — | |
| 2 | a) Revenue from operations | 141 | 1,252.69 | 1,623.04 | 1,199.39 | 5,921.03 | |
| 3 | b) Other Income | 142 | 20.95 | 42.19 | 16.15 | 108.50 | |
| 4 | Total Income | 143 | "11273.64" (OCR-garbled, likely 1,273.64) | "11665.23" (likely 1,665.23) | 1,215.54 | "61029.53" (likely 6,029.53) | OCR_ARTIFACT |
| 5 | Expenses (header, item 2) | 144 | — | — | — | — | |
| 6 | (a) Cost of materials consumed | 145 | 51.70 | 25.48 | 48.06 | 135.00 | |
| 7 | (b) Purchases of stock-in-trade | 146 | 618.67 | 624.83 | 566.41 | 2,414.14 | |
| 8 | (c) Changes in inventories of stock-in-trade | 147 | (189.50) | 18.14 | (153.12) | (83.08) | |
| 9 | (d) Employee benefits expense | 148 | 94.29 | 90.99 | 83.87 | 354.22 | |
| 10 | (e) Finance costs | 149 | 62.94 | 63.42 | 61.98 | 254.73 | |
| 11 | (f) Depreciation and amortization expense | 150 | 192.36 | 187.82 | 182.27 | 743.70 | |
| 12 | (g) Other expenses | 151 | 411.75 | 448.48 | 343.72 | "1 558.85" (likely 1,558.85) | OCR_ARTIFACT |
| 13 | Total expenses | 152 | "11242.21" (likely 1,242.21) | "11459.16" (likely 1,459.16) | "11133.19" (likely 1,133.19) | "51377.56" (likely 5,377.56) | OCR_ARTIFACT |
| 14 | Profit before exceptional items and tax (item 3) | 153 | 31.43 | 206.07 | 82.35 | "651,97" (likely 651.97) | OCR_ARTIFACT |
| 15 | Exceptional Item (refer Note 5) (item 4) | 154 | blank | blank | blank | 13.97 | ZERO_STANDING (blank in all three quarterly columns; only annual FY26 column populated) |
| 16 | Profit before tax (item 5) | 155 | 31.43 | 206.07 | "82,35" (likely 82.35) | 638.00 | OCR_ARTIFACT |
| 17 | Tax expense (header, item 6) | 156 | — | — | — | — | |
| 18 | Current tax | 157 | blank | 78.64 | 23.73 | 211.80 | ZERO_STANDING (blank in current reporting quarter only) |
| 19 | Excess provision of Income tax in relation to earlier years | 158-159 | blank | blank | blank | (0.31) | ZERO_STANDING (blank in all three quarterly columns; only annual FY26 column populated) |
| 20 | Deferred Tax charge/(credit) | 160 | 8.58 | (24.87) | (4.41) | (47.73) | |
| 21 | Total tax expense | 161 | 8.58 | 53.77 | 19.32 | 163.76 | |
| 22 | Net profit after tax (item 7) | 162 | "22,85" (likely 22.85) | 152.30 | 63.03 | 474.24 | OCR_ARTIFACT |
| 23 | Other comprehensive income (header, item 8) | 163 | — | — | — | — | |
| 24 | Items that will not be reclassified to profit or loss (sub-header) | 164 | — | — | — | — | |
| 25 | Re-measurement gain/(loss) on defined benefit liability | 165-166 | 0.24 | 2.38 | (0.13) | 1.88 | |
| 26 | Tax related to above item | 167 | (0.06) | (0.60) | 0.03 | (0.48) | |
| 27 | [unlabeled subtotal row — subtotal of #25+#26, no caption printed] | 168 | 0.18 | 1.78 | (0.10) | 1.40 | OCR_ARTIFACT (caption apparently dropped/duplicated ahead of "Total other comprehensive Income" on next line; flagged for A3 review, not resolved here) |
| 28 | Total other comprehensive Income (net of tax) | 169-170 | 0.18 | 1.78 | (0.10) | 1.40 | |
| 29 | Total comprehensive income (item 9) | 171 | 23.03 | 154.08 | 62.93 | 475.64 | |
| 30 | Paid-up equity share capital (face value ~2 per share) (item 10) | 172-173 | 130.79 | 130.74 | 130.74 | 130.74 | |
| 31 | Other Equity (item 11) | 174 | blank | blank | blank | "4 255.26" (likely 4,255.26) | ZERO_STANDING (blank in all three quarterly columns; only annual FY26 column populated — standard SEBI-format convention of reporting Other Equity only against the last audited annual balance sheet, still flagged per the never-drop-a-nil-row rule); OCR_ARTIFACT |
| 32 | Earning per share (face value ~2 per share) (not annualised) (header, item 12) | 175-176 | — | — | — | — | |
| 33 | a) Basic in ~ | 177 | 0.35 | 2.33 | 0.97 | 7.26 | |
| 34 | b) Diluted in ~ | 178 | 0.35 | 2.33 | 0.97 | 7.25 | |

## 5. INDEPENDENT AUDITOR'S REVIEW REPORT (auditor_paras = 9)

| # | Item | Line(s) | Content | Flags |
|---|---|---|---|---|
| P1 | Paragraph 1 — scope of engagement | 73-78 | Reviewed the accompanying statement of unaudited financial results for quarter ended June 30, 2026, submitted per Reg 33 SEBI LODR | |
| P2 | Paragraph 2 — management responsibility | 79-84 | Statement is Management's responsibility, approved by the Board, prepared per Ind AS 34, Section 133 Companies Act 2013; auditor's responsibility is to express a conclusion | |
| P3 | Paragraph 3 — basis of review | 86-93 | Review conducted per SRE 2410; review is substantially less in scope than an audit; no audit opinion expressed | |
| P4 | Paragraph 4 — conclusion | 95-99 | "nothing has come to our attention that causes us to believe that the accompanying Statement... has not disclosed the information required... or that it contains any material misstatement" — UNMODIFIED / CLEAN review conclusion | |
| P5 | Emphasis of Matter paragraph | — | NOT PRESENT (grep "emphasis of matter": 0 hits) | ABSENT |
| P6 | Other Matters paragraph | — | NOT PRESENT (grep "other matter": 0 hits) | ABSENT |
| P7 | Going Concern paragraph | — | NOT PRESENT (grep "going concern": 0 hits) | ABSENT |
| P8 | Entity(ies) reviewed | 66-70, 73-74 | Credo Brands Marketing Limited — standalone only, no consolidation | |
| P9 | Firm / signature / registration block | 102-112 | For MSKC & Associates LLP, Chartered Accountants; Firm Registration Number 001595S/S000168 (OCR-garbled prefix, digits legible); Membership No. 109752; UDIN: 26109752XMVUNP9536; Place: Mumbai; Date: August 11, 2026. No explicit "digitally signed" tag captured by OCR for this block (contrast with CS signature block C5, which does carry one) | OCR_ARTIFACT |

## 6. CONSOLIDATION ENTITIES (entities = 1)

| # | Entity | Relationship | Line(s) | Flags |
|---|---|---|---|---|
| E1 | Credo Brands Marketing Limited (standalone reporting entity; fka Credo Brands Marketing Private Limited) | Self — sole reporting entity | 122-133, 228 | Note 7 explicitly states: "the company doesn't have any subsidiary, associate and joint venture company" — no consolidated financials filed this quarter |

No prior-quarter ledger available (first coverage per injected inputs) — ENTITY_CHANGE cross-check not applicable this run.

## 7. NON-SUBSTANTIVE PAGE FURNITURE (excluded from counts, logged for transparency)

| Line(s) | Content | Disposition |
|---|---|---|
| 184, 243 | Social-media footer icon/handle strings ("Mufti Jeans", "@MuftiJeans", "@muftijeans") repeated at foot of pages 3 and 4 | Reviewed, judged non-substantive branding footer, excluded from enumerated disclosure counts (not a disclosure unit) |
| 122-133, 186-196 | Repeated company letterhead (CIN, address, website, tel/email) on pages 3 and 4 | Reviewed, letterhead metadata only, not a disclosure unit |

---

## CATEGORY COUNT SUMMARY

- notes: 8
- line_items: 34 (of which zero_standing: 4)
- agenda_items: 10 (1 present, 9 flagged AGENDA_NOT_DISCLOSED)
- auditor_paras: 9 (4 numbered paragraphs + 3 confirmed-absent paragraph types + entity row + signature/UDIN row)
- entities: 1
- digital signature blocks identified: 1 (CS Sanjay Kumar Mutha; see row C5)
- board meeting duration: 1 hr 15 min (4:45 p.m. to 6:00 p.m.)

Flags raised in this ledger: ZERO_STANDING (4), AGENDA_NOT_DISCLOSED (9), OCR_ARTIFACT (multiple, both in numbers and in the note-1 numbering), ABSENT (3, auditor report paragraph types).
