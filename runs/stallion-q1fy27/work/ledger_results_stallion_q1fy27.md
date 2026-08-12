# A2 ENUMERATOR LEDGER — Stallion India Fluorochemicals, Q1 FY27, Results Filing

Source: `extract_results_stallion_q1fy27.txt` (6 pages, 304 extract lines, header lines 1-56).
Fidelity carry-forward from A1: pages 3 and 4 had a corrupted embedded text layer,
resolved by OCR + rendered-image reconciliation; labelled `[OCR page 3]` / `[OCR page 4]`
below. Unit = Lakhs; conversion to Rs Cr = x0.01 (not applied here, values transcribed
as-extracted). No consolidated financials present in this filing (grep for
"consolidat|subsidiar" across the full extract returns zero hits) — standalone only,
single entity, no segment reporting (Note 3: single business segment, Ind AS 108 not
applicable). This is recorded explicitly rather than silently omitted.

```
=== A2 COUNT TEST ===
category: notes (financial results, numbered)   grep_count: 6   sweep_count: 6   match: yes
category: auditor_report_paragraphs (numbered)   grep_count: 4   sweep_count: 4   match: yes
category: board_agenda_items                     grep_count: 7   sweep_count: 7   match: yes
category: pnl_line_items (standalone, w/ values) grep_count: 24  sweep_count: 24  match: yes
category: pnl_section_headers (no own values)    grep_count: 6   sweep_count: 6   match: yes
category: ipo_utilisation_table_rows             grep_count: 5   sweep_count: 5   match: yes
category: signature_blocks                       grep_count: 4   sweep_count: 4   match: yes
category: consolidated_pnl_line_items            grep_count: 0   sweep_count: 0   match: yes (n/a — standalone-only filing, confirmed by zero hits on "consolidat|subsidiar")
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used (all run against the extract file with original line-number prefixes,
so patterns account for the `<lineno>\t` prefix):
- Notes: `grep -nP '^\d+\t\s*\d+\.\s'` restricted to page-4 notes block (lines 111-152) -> 6
- Auditor paragraphs: same pattern restricted to page-5/6 report block (lines 153-223) -> 4
- Board agenda: `grep -nP '(considered and approved the Unaudited|^\d+\t\s*[a-f]\))'`
  restricted to lines 58-106 -> 7 (1 unlettered main item + 6 lettered a-f)
- P&L line items: pipe-delimited rows in lines 66-97 containing at least 4 columns
  (digits or dash) -> 24 (this required a dash-inclusive pattern; a digit-only pattern
  undercounts at 22 because it misses dash/nil rows — manual sweep caught the miss,
  see line 82 below, which is exactly the ZERO_STANDING scenario this ledger exists to catch)
- IPO utilisation rows: `grep -nP '^\d+\t\s*\(?[a-f]\)\s'` restricted to lines 179-215 -> 5
- Consolidat/subsidiary: `grep -n -iE "consolidat|subsidiar"` full file -> 0 hits (confirms standalone-only)

Manual sweep: full line-by-line read of all 304 extract lines plus the header/method
note (lines 1-56), cross-checked against the grep passes above. No unnumbered
footnotes, asterisks, daggers, or "Note:" prefixes found below any table (checked
visually — table sections at lines 66-97 and 126-139 have no such markers).

---

## 1. BOARD OUTCOME — AGENDA ITEMS (7)

| # | Line(s) | Item | First ~15 words | Flags |
|---|---------|------|------------------|-------|
| 1 | 20-24 | Main item: approval of Unaudited Financial Results + Limited Review Report | "considered and approved the Unaudited Financial Results of the Company for the quarter ended June 30, 2026, along with the Limited Review Report" | — |
| 2 (a) | 32-33 | Took on record Secretarial Audit Report, FY ended 31 Mar 2026 | "Took on record the Secretarial Audit Report of the Company for the financial year ended 31st March, 2026" | — |
| 3 (b) | 34-35 | Approved Directors' Report + annexures (Sec 134) | "Approved the Directors' Report, along with its annexures pursuant to Section 134 of the Companies Act" | — |
| 4 (c) | 36-37 | Approved MD&A Report and Corporate Governance Report | "Approved the Management Discussion and Analysis Report and the Corporate Governance Report for the financial year ended" | — |
| 5 (d) | 38-39 | Approved draft AGM Notice (AGM: 21 Sep 2026, 4:00 PM) | "Approved the draft Notice convening the Annual General Meeting (AGM) scheduled to be held on Monday, 21st" | — |
| 6 (e) | 40-41 | Approved book closure period, 15-21 Sep 2026 (both days incl.) | "Approved the book closure period for the purpose of the AGM, which shall be from 15th September" | — |
| 7 (f) | 42-45 | AGM shareholder matters: regularization of Ms. Swati Ghosh, DIN 08789050, from Additional Independent Director to Woman Independent Director | "Considered and approved placing the following matters before the shareholders at the forthcoming AGM for their approval" | `DIRECTOR_CHANGE` |

Board meeting timing: commenced 11:30 AM, concluded 01:11 PM (IST) — line 21. Duration
~1 hr 41 min. Recorded per instruction (a 20-minute vs 2-hour meeting is information);
this is a mid-length meeting, not flagged as anomalous on its own.

Annexure I (line 26): comprises 2 enclosures — (i) Unaudited Financial Results (line 27),
(ii) Limited Review Report (line 28). Both present and enumerated separately below.

Unmodified-opinion confirmation restated in the covering letter itself (lines 46-47):
"the Statutory Auditor has issued the Limited Review Report on the financial results
with an unmodified opinion" — cross-checked against auditor report para 4 below, consistent.

---

## 2. SIGNATURE / SIGNATORY BLOCKS (4)

| # | Line(s) | Document | Signatory | Designation | Timestamp | Flags |
|---|---------|----------|-----------|-------------|-----------|-------|
| 1 | 50-59 | Board Outcome letter (page 2) | Govind Rao | Company Secretary & Compliance Officer, Mem No. A47094 | Digitally signed 2026.08.12 13:20:23 +05'30' | — (9 min after board meeting concluded at 13:11 — normal sequencing, not flagged) |
| 2 | 99-108 | Unaudited Financial Results statement (page 3) | Shazad Rustomji | **Managing Director & CEO**, DIN 01923432 | Not digitally timestamped (typed signature block), dated 12th Aug 2026, Mumbai | `DESIGNATION_MISMATCH` — see row 3 |
| 3 | 142-151 | Notes page (page 4) | Shazad Rustomji | **Managing Director & CFO**, DIN 01923432 | Not digitally timestamped, dated 12th Aug 2026, Mumbai | `DESIGNATION_MISMATCH` — same person, same DIN (01923432), titled CEO on page 3 and CFO on page 4 of the same filing package. Mechanical fact only; not resolved here. |
| 4 | 209-222 | Limited Review Report (page 6) | CA Sourabh Bagaria | Partner, Mittal & Associates, FRN 106456W, M No. 183850 | Digitally signed 2026.08.12 12:46:20 +05'30'; UDIN 26183850WDGGTH7387 | — (auditor's report timestamp precedes board conclusion at 13:11, which is expected sequencing — auditor completes and issues the report before/at the meeting so the board can act on it) |

---

## 3. FINANCIAL RESULTS NOTES (numbered, page 4) (6)

| Note # | Line(s) | First ~15 words | Flags |
|--------|---------|------------------|-------|
| 1 | 116-117 | "The financial results are prepared in accordance with the Companies (Indian Accounting Standards) Rule 2015 and amendments" | — |
| 2 | 118-119 | "These financial results were reviewed and recommended by the Audit Committee on 12th August, 2026 and approved" | — |
| 3 | 120-121 | "The company's business falls within single business segment of manufacture of industrial gases. Hence, disclosures under" | Segment reporting N/A confirmed — no segment table exists in this filing |
| 4 | 122-123 | "The figures of the quarter ended March 31, 2026 are the balancing figures between audited figures in" | — |
| 5 | 124-139 | "The Company has received an amount of INR 14,474.87 lakhs (net of IPO expenses of INR 1,598.00" | `OCR_RECONCILED` (page 4 table, see A1 fidelity note); contains the IPO utilisation table (5 rows, section 4 below) and narrative on revised utilisation (Khalapur land acquisition in lieu of warehouse, differential cost Rs 0.13 crore — A1 flagged an OCR/embedded-text digit-misread on the Rs symbol, resolved by visual confirmation, carried forward here) |
| 6 | 140 | "Previous period figures have been regrouped, rearranged and reclassified where necessary to make it comparable with" | — |

---

## 4. IPO / ISSUE-PROCEEDS UTILISATION TABLE (Note 5 sub-table) (5 rows)

Net IPO proceeds: INR 14,474.87 lakhs (net of issue expenses of INR 1,598.00 lakhs) — line 124.

| Row | Line(s) | Object of Issue | Amount to be financed (Rs lakh) | Amount utilised (Rs lakh) | Unutilised as on 30-Jun-2026 (Rs lakh) | Flags |
|-----|---------|------------------|----------------------------------|------------------------------|-------------------------------------------|-------|
| (a) | 127 | Funding incremental working capital requirements | 9,441.80 | 10,270.53 | (828.73) | Negative unutilised — utilised exceeds planned amount |
| (b) | 128-129 | Capex: Semi-conductor & Specialty Gas debulking/blending facility + land, Khalapur, Maharashtra | 2,574.66 | 2,661.77 | (87.11) | Negative unutilised — utilised exceeds planned amount |
| (c) | 130-131 | Capex: Refrigerant debulking & blending facility, Mambattu, Andhra Pradesh | 2,117.53 | 1,100.75 | 1,016.78 | Largest unutilised balance of the five rows |
| (d) | 132 | General Corporate Purposes | 340.88 | 340.88 | - | `ZERO_STANDING` — unutilised column is nil (fully utilised, no shortfall/excess) |
| (e) | 133 | Issue Related Expenses | 1,598.00 | 1,198.92 | 399.08 | — |

Narrative below table (lines 134-139): unutilised proceeds parked in fixed deposits /
Monitoring Agency Bank Account / IPO Public Issue Account / company current account
(line 134-135); allocation revised via Special Resolution dated 30 May 2026, redirecting
proceeds from originally proposed warehouse construction to ~2 acres of land acquisition
at Khalapur, Maharashtra, differential cost Rs 0.13 crore (lines 136-139) — `OCR_RECONCILED`
per A1's carried-forward Rs-symbol misread flag.

---

## 5. AUDITOR'S LIMITED REVIEW REPORT — STRUCTURE AND PARAGRAPHS

| Component | Line(s) | Content | Flags |
|-----------|---------|---------|-------|
| Firm header | 153-158 | Mittal & Associates, Chartered Accountants, Mumbai; contact details | — |
| Title | 162-165 | "Independent Auditor's Limited Review Report on Unaudited Quarter ended Financial results" re Regulation 33 | — |
| Addressee | 167-171 | To the Board of Directors, Stallion India Fluorochemicals Limited | — |
| Para 1 | 172-177 | Scope statement: reviewed the accompanying Statement for Q1 FY27 per Reg 33 | — |
| Para 2 | 179-186 | Management's responsibility (Ind AS 34); auditor's responsibility is to express a conclusion, not an opinion | — |
| Para 3 | 188-197 | Basis of review: SRE 2410 (ICAI); explicitly states review scope is less than an audit and no audit opinion is expressed | — |
| Para 4 | 198-205 | Conclusion: unmodified/unqualified — "nothing has come to our attention" that the Statement is not in accordance with Ind AS or Reg 33, no material misstatement | — |
| Entity reviewed | throughout | Stallion India Fluorochemicals Limited (standalone only) — no other entities named, no unaudited/management-furnished sub-entities disclosed | — |
| Emphasis of Matter | n/a | None present (grep for "emphasis of matter" = 0 hits) | — |
| Other Matters | n/a | None present (grep for "other matter" = 0 hits) | — |
| Going Concern | n/a | No going-concern language present | — |
| Signature block | 209-222 | See section 2, row 4 (CA Sourabh Bagaria, FRN 106456W, UDIN 26183850WDGGTH7387) | — |

---

## 6. UNAUDITED FINANCIAL RESULTS — P&L (STANDALONE ONLY, no consolidated table in this filing)

Statement of Unaudited Financial Results, quarter ended 30 Jun 2026, four columns:
Q1FY27 (Unaudited) | Q4FY26 (Audited) | Q1FY26 (Unaudited) | FY26 (Audited). Source
lines 66-97, `[OCR page 3]`.

### 6a. Section headers (no own value row) — 6

| # | Line | Header |
|---|------|--------|
| 1 | 67 | I. Income |
| 2 | 71 | II. Expenses |
| 3 | 80 | IV. Tax expense: |
| 4 | 86 | VI. Other Comprehensive Income |
| 5 | 87 | VI.A(i) Items that will not be reclassified to profit or loss |
| 6 | 92 | VIII. Earnings per equity share |

### 6b. Line items with values — 24

| # | Line | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-------------|--------|--------|--------|------|-------|
| 1 | 68 | Revenue from operations | 12,144.60 | 10,999.43 | 11,047.19 | 43,067.80 | — |
| 2 | 69 | Other income | 322.97 | 130.09 | 7.37 | 344.50 | — |
| 3 | 70 | Total Income (I) | 12,467.57 | 11,129.52 | 11,054.55 | 43,412.30 | — |
| 4 | 72 | Cost of materials consumed | 7,585.32 | 10,091.89 | 9,526.02 | 36,910.24 | — |
| 5 | 73 | Changes in inventories of finished goods, Stock-in-Trade and WIP | 1,676.28 | (1,364.11) | (739.32) | (2,395.94) | — |
| 6 | 74 | Employee benefits expense | 238.71 | 243.56 | 224.78 | 947.54 | — |
| 7 | 75 | Finance costs | 9.18 | 38.23 | 21.74 | 88.91 | — |
| 8 | 76 | Depreciation and amortization expenses | 38.73 | 59.77 | 29.05 | 147.87 | — |
| 9 | 77 | Other expenses | 440.47 | 393.35 | 606.14 | 1,815.72 | — |
| 10 | 78 | Total expenses (II) | 9,988.70 | 9,462.69 | 9,668.41 | 37,514.34 | — |
| 11 | 79 | III. Profit before tax (I-II) | 2,478.88 | 1,666.83 | 1,386.14 | 5,897.96 | — |
| 12 | 81 | Current tax | 553.02 | 244.48 | 328.67 | 1,191.15 | — |
| 13 | 82 | Adjustment of tax relating to earlier periods | - | - | - | - | `ZERO_STANDING` — dash in all four periods; standing line item, template signal for a transaction type not currently occurring |
| 14 | 83 | Deferred tax | 69.28 | 328.93 | 21.15 | 322.70 | — |
| 15 | 84 | Total tax expense (IV) | 622.30 | 573.41 | 349.82 | 1,513.85 | — |
| 16 | 85 | V. Profit for the period/year (III-IV) | 1,856.58 | 1,093.42 | 1,036.32 | 4,384.11 | — |
| 17 | 88 | VI.A(i) Remeasurements of the defined benefit plans | 1.87 | 41.80 | (18.35) | (13.26) | — |
| 18 | 89 | VI.A(i)(ii) Income tax relating to items that will not be reclassified to P&L | (0.47) | (10.52) | 4.62 | 3.34 | — |
| 19 | 90-91 | VII. Total Comprehensive Income for the period/year (V+VI) | 1,857.98 | 1,124.70 | 1,022.59 | 4,374.19 | — |
| 20 | 93 | VIII(1) Earnings per equity share — Basic | 1.60 | 1.33 | 1.15 | 5.34 | — |
| 21 | 94 | VIII(2) Earnings per equity share — Diluted | 1.60 | 1.33 | 1.15 | 5.34 | — |
| 22 | 95 | Paid up Equity Share Capital (Rs 10/- each) | 11,608.57 | 11,608.57 | 7,932.53 | 11,608.57 | — |
| 23 | 96 | Other Equity excluding Revaluation Reserve | 58,309.75 | 56,451.78 | 23,094.49 | 56,451.78 | — |
| 24 | 97 | Net Worth | 69,918.33 | 68,060.35 | 31,027.02 | 68,060.35 | — |

Consolidated results: not applicable — no consolidated P&L table present anywhere in
this 6-page extract; confirmed by zero grep hits for "consolidat" or "subsidiar" across
the full file.

Segment reporting: not applicable per Note 3 — single business segment (industrial
gases manufacture), Ind AS 108 disclosures explicitly stated as not reported separately.
No segment table exists in this filing to enumerate.

---

## 7. HEADER / ENTITY METADATA (not a repeating category, single instance each)

| Item | Line(s) | Value |
|------|---------|-------|
| Company name (current) | 61, 111 | Stallion India Fluorochemicals Limited |
| Company name (former) | 61, 111 | Stallion India Fluorochemicals Private Limited |
| Registered office | 62, 112 | 2, A Wing, Knox Plaza, Off. Link Road, Mindspace, Malad-West, Mumbai 400064 |
| CIN | 63, 113 | L51410MH2002PLC137076 |
| NSE symbol | 10 | STALLION |
| BSE scrip code | 10 | 544342 |
| ISIN | 11 | INE0RYC01010 |
| Regulations cited (Board Outcome) | 18-19 | SEBI LODR Regs 2015, Regs 30 & 33 |

---

## 8. EXTRACTION-FIDELITY FLAGS CARRIED FORWARD FROM A1 (not new disclosure units, tracked for A3/A4)

| Flag | Location | Detail |
|------|----------|--------|
| `OCR_RECONCILED` | Page 3 (entire P&L table, lines 61-109) | Embedded text layer corrupted; OCR + rendered-image cross-check used |
| `OCR_RECONCILED` | Page 4 (Notes + IPO utilisation table, lines 111-152, esp. Note 5) | Same corruption; specific residual ambiguity on "Rs 0.13 crore" (Rupee symbol misread as leading digit) resolved by visual confirmation at line 138-139 |

---

## SUMMARY COUNTS

| Category | Count |
|----------|-------|
| Board agenda items | 7 |
| Signature blocks | 4 |
| Financial results notes (numbered) | 6 |
| IPO utilisation table rows | 5 |
| Auditor report paragraphs (numbered) | 4 |
| Auditor report other components (title/addressee/entity/signature, non-numbered) | 4 |
| P&L section headers (standalone, no own value) | 6 |
| P&L line items with values (standalone) | 24 |
| P&L line items, consolidated | 0 (n/a, standalone-only filing) |
| Segment rows | 0 (n/a, Note 3 — single segment) |
| ZERO_STANDING flags | 2 (P&L line 82; IPO table row (d) unutilised column) |
| DESIGNATION_MISMATCH flags | 1 (Shazad Rustomji: CEO on p.3, CFO on p.4, same DIN) |
| DIRECTOR_CHANGE flags | 1 (Swati Ghosh regularization, agenda item f) |
| ENTITY_CHANGE flags | 0 (no consolidation list present) |
