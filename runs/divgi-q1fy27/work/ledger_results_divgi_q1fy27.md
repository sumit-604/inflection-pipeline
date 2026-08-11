# A2 COMPLETENESS LEDGER — DIVGI TORQTRANSFER SYSTEMS LIMITED, Q1 FY27 (Results Filing)

Source: `extract_results_divgi_q1fy27.txt` (A1 extract). All line numbers below are the
extract file's own physical line numbers (first column, as returned by Read/grep -n on the
extract file — verified identical between the two tools). The extract also carries a second,
internal body-line count (offset -26 from the physical number, since the 25-line A1 header
block plus the `=== END HEADER ===` line precede body line 1); that internal count is shown
in parentheses where useful for cross-reference to the header's `page_map`.

Prior-quarter ledger: NOT PROVIDED to this run (no `PRIOR_LEDGER_PATH` given in task). Entity
and slide/line diffs against prior quarter could not be run; noted as a gap, not silently
skipped.

```
=== A2 COUNT TEST ===
category: notes            grep_count: 7    sweep_count: 7    match: yes
category: line_items       grep_count: 29   sweep_count: 29   match: yes
category: zero_standing    grep_count: 1    sweep_count: 1    match: yes
category: agenda_items     grep_count: 5    sweep_count: 5    match: yes
category: annexure_items   grep_count: 4    sweep_count: 4    match: yes
category: auditor_paras    grep_count: 4    sweep_count: 4    match: yes
category: entities         grep_count: 2    sweep_count: 2    match: yes
category: signatories      grep_count: 4    sweep_count: 4    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Method note on `line_items` (29): grep pass 1 — `grep -E "[0-9]+\.[0-9]{2}"` inside lines
254-304 (the Statement of Financial Results table) isolates every value-bearing row = 22
matches. grep pass 2 — inverse pattern (non-blank lines in the same range NOT matching a
decimal value) isolates every header/label row with no standalone value (section headers,
subheaders, the "not annualised" note line) = 7 matches. 22 + 7 = 29, independently
confirmed against a manual top-to-bottom read of the table = 29 rows. Both methods agree;
GATE A2 passes for this category.

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS (5 items)

Letter ref DTTS/Sec/26-27/29, dated August 11, 2026 (line 37). Board meeting: **commenced
02:03 P.M., concluded 04:45 P.M. on August 11, 2026** (line 110) — a 2 hour 42 minute
meeting.

| # | Agenda item | Line(s) | First 15 words | Flags |
|---|---|---|---|---|
| 1 | Financial Results | 58-63 | "Financial Results — The Unaudited Financial Statements for the quarter ended June 30, 2026." | |
| 2 | Annual General Meeting | 65-67 | "Annual General Meeting — The 61st Annual General Meeting of the Members of the Company will be held on Friday, September 18, 2026." | |
| 3 | Appointment of Scrutinizer | 69-74 | "Appointment of Scrutinizer — CS Mrunmayee Sathaye (ACS No.: A51169, CP No. 19264) Partner Kanj. And Co. LLP appointed as e-voting Scrutinizer." | |
| 4 | Record date and Cut-off date | 87-94 | "Record date and Cut-off date — Board fixed Thursday, September 10, 2026 as cut-off date; final dividend ₹3.27/share for FY 2025-26." | |
| 5 | Appointment of M/s. Kirtane & Pandit LLP, Chartered Accountants as Statutory Auditors | 96-106 | "Board approved appointment of M/s. Kirtane & Pandit LLP as Statutory Auditors for five years, 61st AGM to 66th AGM, subject to shareholder approval." | |

Meeting timing fact: line 110. Letter closing / signatory block: lines 116-125 (see §8,
Signatories).

---

## 2. ANNEXURE I — STATUTORY AUDITOR APPOINTMENT DISCLOSURE (Reg. 30), 4 rows

| Sr | Requirement | Line(s) | Disclosure (first 15 words) | Flags |
|---|---|---|---|---|
| 1 | Reason for change (appointment/resignation/removal/death/otherwise) | 142-143 | "Appointment of Statutory Auditors" | |
| 2 | Date of appointment/cessation and Term of appointment | 147-156 | "Based on the recommendation of the Audit Committee, the Board has approved the appointment..." five-year term, 61st to 66th AGM | |
| 3 | Brief Profile (in case of appointment) | 158-165 | "Kirtane & Pandit LLP, Chartered Accountants, is a 70+ year-old accounting, auditing, and consulting firm..." | |
| 4 | Disclosure of relationships between directors (in case of appointment of a director) | 167-168 | "Not Applicable" | ZERO_STANDING (N/A disclosure, template row retained because auditor appointment ≠ director appointment) |

---

## 3. INDEPENDENT AUDITORS' REVIEW REPORT — paragraphs and structural elements

Report title/heading: lines 182-184. Addressee: "To The Board of Directors of Divgi
TorqTransfer Systems Limited" — line 188.

| Para | Line(s) | First 15 words | Flags |
|---|---|---|---|
| 1 (scope statement) | 191-194 | "We have reviewed the accompanying Statement of unaudited Financial Results for the quarter ended June 30, 2026..." | |
| 2 (management responsibility / basis) | 196-201 | "The Company's Management is responsible for the preparation of the Statement in accordance with..." | |
| 3 (review standard, SRE 2410, scope limitation) | 203-210 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410..." | |
| 4 (conclusion) | 212-217 | "Based on our review conducted and procedures performed as stated in paragraph 3 above nothing has come to our attention..." | |

**Opinion type: unmodified/clean review conclusion** ("nothing has come to our attention...
has not disclosed the information required... or that it contains any material
misstatement"). This is a Limited Review (moderate assurance), NOT an audit — auditor
explicitly states "we do not express an audit opinion" (line 210).

Structural elements checked and their status (enumerated per protocol; absence of an
expected paragraph type is itself a ledger fact, not an omission):

| Element | Status | Line evidence |
|---|---|---|
| Emphasis of Matter paragraph | NOT PRESENT | none found in paras 1-4 |
| Other Matters paragraph | NOT PRESENT | none found in paras 1-4 |
| Going Concern paragraph | NOT PRESENT | none found in paras 1-4 |
| Entity/entities reviewed | Single entity — Divgi TorqTransfer Systems Limited, standalone only | line 165-166 |
| Unaudited / management-furnished sub-entities | N/A — no subsidiaries reviewed (standalone filing) | — |
| UDIN | Present but OCR-corrupted: "2 6 1 'L 50 s-, (,l...8 N PQO S' 0-1 ~" | line 229 — flag OCR_GARBLED |

Auditor signature block: For B. K. Khare & Co., Chartered Accountants — lines 220-231
(Amit Mahadik, Partner, Membership No. 125657, Place: Pune, Date: August 11, 2026). See §8.

---

## 4. STATEMENT OF FINANCIAL RESULTS FOR THE QUARTER ENDED 30 JUNE 2026 (P&L only) — 29 rows

Units: ₹ in million (line 248). Conversion to Cr per A1 header: x0.1. Four columns: Q ended
30-Jun-26 (Unaudited), Q ended 31-Mar-26 (Unaudited, "Refer note 6"), Q ended 30-Jun-25
(Unaudited), Year ended 31-Mar-26 (Audited). **No consolidated column exists anywhere in
this statement — this is a STANDALONE-ONLY filing (A1 header, lines 13-14).**

| Sr | Line item | Line(s) | 30-Jun-26 | 31-Mar-26 (Q) | 30-Jun-25 | FY26 (Audited) | Flags |
|---|---|---|---|---|---|---|---|
| 1 | Income (section header) | 254 | — | — | — | — | header row, no standalone value |
| 1(a) | Revenue from operations | 255 | 1,371.42 | 1,076.22 | 716.76 | 3,528.88 | |
| 1(b) | Other income | 256 | 46.22 | 61.76 | 50.94 | 222.83 | |
| — | Total Income (a+b) | 257 | 1,417.64 | 1,137.98 | 767.70 | 3,751.71 | subtotal |
| 2 | Expenses (section header) | 259 | — | — | — | — | header row |
| 2(a) | Cost of materials consumed | 260 | 536.26 | 415.45 | 306.33 | 1,448.73 | |
| 2(b) | Changes in inventories of finished goods and work-in-progress | 261-263 | (4.59) | (8.94) | (21.71) | (807.6)* | *OCR_GARBLED: extract shows "(8076)" — missing decimal, likely (807.60) |
| 2(c) | Employee benefit expense | 264 | 134.77 | 142.98 | 82.72 | 415.41 | |
| 2(d) | Finance Cost | 265 | 0.69 | 0.84 | 0.65 | 3.10 | |
| 2(e) | Depreciation and amortization expense | 266 | 78.20 | 75.51 | 69.44 | 292.37 | |
| 2(f) | Other expenses | 267 | 334.80 | 310.00 | 209.48 | 1,045.37 | |
| — | Total expenses (a+b+c+d+e+f) | 268 | 1,080.13 | 935.84 | 646.91 | 3,124.22 | subtotal; OCR_GARBLED label text "Totalexpenses(a+b+c+d+e+ij" |
| 3 | Profit before tax (1-2) | 270 | 337.51 | 202.14 | 120.79 | 627.49 | subtotal |
| 4 | Tax expenses (section header) | 272 | — | — | — | — | header row |
| 4(a) | Current Tax | 273 | 85.76 | 64.76 | 27.39 | 159.44 | |
| 4(b) | Deferred Tax | 274 | (0.65) | (17.43) | 4.11 | (1.21) | OCR_GARBLED: extract shows "(0.65'" and "(17.43'" and "(1 21)" |
| — | Total tax expenses (a+b) | 275 | 85.11 | 47.33 | 31.50 | 158.23 | subtotal |
| 5 | Net profit for the period/year (3-4) | 277 | 252.40 | 154.81 | 89.29 | 469.26 | subtotal |
| 6 | Other comprehensive Income/(loss) (OCI) (section header) | 279 | — | — | — | — | header row |
| 6.i | Items that will not be reclassified subsequently to P&L (subheader) | 280-281 | — | — | — | — | subheader, no standalone value |
| 6.i.a | Gain/(loss) on remeasurement of defined benefit plans (net of tax) | 282-284 | (0.72) | 3.16 | (0.03) | (2.89) | |
| — | Other comprehensive Income/(loss) for the period/year, net of tax | 285-287 | (0.72) | 3.16 | (0.03) | (2.89) | subtotal (single-item OCI, same value as above) |
| 7 | Total comprehensive Income for the period/year (5+6) | 289-291 | 251.68 | 157.97 | 89.26 | 466.37 | subtotal |
| 8 | Paid up equity share capital (Face value of ₹5 each) | 293-295 | 152.91 | 152.91 | 152.91 | 152.91 | |
| 9 | Other equity (excluding revaluation reserve) | 297 | (blank) | (blank) | (blank) | 6,201.65 | **ZERO_STANDING** — quarter columns carry no value in any of the three quarter periods; only the FY-end audited column is populated (standard practice, but the row exists and must be ledgered nil for quarters) |
| 10 | Earnings per equity share of face value ₹5 each (section header) | 300 | — | — | — | — | header row |
| 10.i | (Not annualised for the quarters) | 302 | — | — | — | — | note line, no standalone value |
| 10(a) | Basic EPS (in ₹) | 303 | 8.25 | 5.06* | 2.92 | 15.34 | *OCR_GARBLED: extract shows "506" (missing decimal) |
| 10(b) | Diluted EPS (in ₹) | 304 | 8.25 | 5.06* | 2.92 | 15.34 | *OCR_GARBLED: extract shows "5 06" (missing decimal, spurious space) |

Statement signature block: For Divgi TorqTransfer Systems Limited — Jitendra Bhaskar Divgi,
Managing Director, DIN 00471531 — lines 327-329 (Place: Pune, Date line garbled by OCR
around 325-326). See §8.

---

## 5. NOTES TO STATEMENT OF FINANCIAL RESULTS — 7 notes

| Note | Line(s) | First 15 words | Flags |
|---|---|---|---|
| 1 | 344-346 | "The above results were reviewed and recommended to the Board of Directors by the Audit Committee..." | |
| 2 | 349-353 | "The above financial results of Divgi TorqTransfer Systems Limited have been prepared in accordance with and complied..." | |
| 3 | 356-369 | "Details of utilisation of net Initial Public Offer (IPO) proceeds of INR 1,696 million, are as follows:" — includes 4-row sub-table (Objects of issue / Amount to be utilised per prospectus / Utilisation upto 30-06-2026 / Unutilised upto 30-06-2026): row "Funding capital expenditure requirements..." (361-363, 1,507.07 / 915.27 / 591.80), row "General corporate purposes*" (364, 189.55 / 189.54 / 0.01), row "Total" (365, 1,696.62 / 1,104.81 / 591.81), footnote on GCP revision (366-367), and a further explanatory sentence on temporary investment of unutilised proceeds (368-369) | sub-table is itself 3 line-item rows + 1 total row + 2 footnote/explanatory lines, all captured here under Note 3 |
| 4 | 372 | "The Company operates in a single reportable business segment, 'Auto Components and Parts'." | single-segment disclosure |
| 5 | 374-375 | "These Financial Results are also available on the stock exchange websites www.bseindia.com, www.nseindia.com and on our website..." | |
| 6 | 378-379 | "Figures for the quarter ended March, 2026 as reported in the financial results are balancing figures between audited..." | explains the "(Refer note 6)" tag on the 31-Mar-26 quarter column in §4 |
| 7 | 382-383 | "On June 4, 2026, Divgi Transmission Technologies and Systems Ltd. (the 'Foreign Entity') was incorporated. As of June 30, 2026, the equity shares subscription agreement..." | governs the entity/consolidation gap — see §6 |

Notes-page signature block: Jitendra Bhaskar Divgi, Managing Director, DIN 00471531 —
lines 388-390. See §8.

---

## 6. ENTITY / CONSOLIDATION LIST — 2 entities

No consolidated financial statement is present in this filing at all (mechanical fact, A1
header lines 13-14). The following entities are named in the document:

| # | Entity | Relationship | Line(s) | Flags |
|---|---|---|---|---|
| 1 | Divgi TorqTransfer Systems Limited | Reporting entity (standalone results only) | throughout (letterhead x8 occurrences, e.g. 28, 51, 78, 104, 217, 311) | |
| 2 | Divgi Transmission Technologies and Systems Ltd. ("the Foreign Entity") | Newly incorporated June 4, 2026; equity subscription agreement not completed as of June 30, 2026; explicitly NOT considered for consolidation this period | 381-383 | **ENTITY_CHANGE** — first appearance of this entity in the filing; no prior-quarter ledger available to confirm this is genuinely new vs. previously undisclosed (prior ledger not provided to this run) |

**Mechanical fact for the record (per orchestrator instruction, not an omission to hide):**
this filing is STANDALONE-ONLY. No consolidated Statement of Financial Results, no
consolidated Balance Sheet, no consolidated Cash Flow Statement appears anywhere in the six
pages. The standalone-vs-consolidated gap (i.e., how the Foreign Entity or any other group
entity would move consolidated numbers) **cannot be computed this quarter** because no
consolidated baseline exists in this document to compute a gap against. This is recorded
here as a structural fact of the filing, to be carried forward by A3/A4, not flagged as a
missed extraction.

---

## 7. UNITS / CONVERSION FACT (mechanical, not a flag)

Extract-wide unit convention: **Millions**. Conversion factor to Crores: **x0.1** (per A1
header, line 8 of header block). Every rupee figure in §4 above and the IPO utilisation
sub-table in §5 Note 3 is stated in ₹ million as printed; A3/A4 must apply x0.1 before any
cross-document comparison against filings stated in Crores.

---

## 8. SIGNATORY / DIGITAL SIGNATURE BLOCKS — 4 blocks

| # | Signatory | Designation | Document | Line(s) | Timestamp | Flags |
|---|---|---|---|---|---|---|
| 1 | Aniket Kokane | Company Secretary and Compliance Officer (A51571) | Board Outcome letter | 116-125 | Digitally signed 2026.08.11 17:42:29 +05'30' | Timestamp is AFTER board meeting conclusion (04:45 P.M. / 16:45, line 110) — expected sequencing, no flag warranted |
| 2 | Amit Mahadik | Partner, B. K. Khare & Co., Chartered Accountants (Membership No. 125657) | Independent Auditors' Review Report | 220-231 | Place: Pune, Date: August 11, 2026 (no intraday timestamp given); UDIN present but OCR-garbled | OCR_GARBLED (UDIN, line 229) |
| 3 | Jitendra Bhaskar Divgi | Managing Director (DIN 00471531) | Statement of Financial Results | 300-329 | Place: Pune, Date: August 11 (date block OCR-garbled around 325-326) | OCR_GARBLED (signature block graphics/date, lines 306-326) |
| 4 | Jitendra Bhaskar Divgi | Managing Director (DIN 00471531) | Notes to Statement of Financial Results | 388-390 | Place: Pune, Date: August 11, 2026 | clean, no OCR issue |

---

## SUMMARY OF FLAGS RAISED

- **ZERO_STANDING** — Statement of Financial Results, Sr. 9 "Other equity (excluding
  revaluation reserve)" (line 297): quarter columns blank in all three quarterly periods,
  only FY-end audited column populated.
- **ENTITY_CHANGE** — Divgi Transmission Technologies and Systems Ltd., Foreign Entity,
  newly incorporated June 4, 2026, first appearance this filing, not consolidated (lines
  381-383); no prior-quarter ledger available to confirm novelty.
- **OCR_GARBLED** — five instances of corrupted numeric/text extraction requiring source-PDF
  re-verification before any downstream arithmetic check: UDIN (line 229), Deferred Tax
  values (line 274, "(0.65'" / "(17.43'" / "(1 21)"), Changes in inventories FY26 total
  (line 262, "(8076)"), Total expenses formula label (line 268, "Totalexpenses(a+b+c+d+e+ij"),
  Basic/Diluted EPS 31-Mar-26 quarter values (lines 303-304, "506" / "5 06").
- **STANDALONE_ONLY** (mechanical, not company-quality) — no consolidated statement present
  in this filing at all; standalone-vs-consolidated gap not computable this quarter.
- **PRIOR_LEDGER_UNAVAILABLE** (mechanical) — no prior-quarter ledger path supplied to this
  run; entity and line-item diffs against Q4 FY26 could not be performed.

---

```yaml
stage: A2-enumerator
company: "Divgi TorqTransfer Systems Limited"
ticker: "divgi"
quarter: "q1fy27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/divgi-q1fy27/work/ledger_results_divgi_q1fy27.md"
counts:
  notes: 7
  line_items: 29
  zero_standing: 1
  agenda_items: 5
  annexure_items: 4
  auditor_paras: 4
  entities: 2
  signatories: 4
flags_raised: [ZERO_STANDING, ENTITY_CHANGE, OCR_GARBLED, STANDALONE_ONLY, PRIOR_LEDGER_UNAVAILABLE]
gate_a2: pass
mismatch_note: ""
```
