# A2 ENUMERATOR LEDGER — Uni Abex Alloy Products Limited (UNIABEX) — Q1 FY27 — RESULTS

Source: `/home/user/inflection-pipeline/runs/uniabex-q1fy27/work/extract_results_uniabex_q1fy27.txt`
Prior-quarter ledger: none (new coverage)

```
=== A2 COUNT TEST ===
category: notes             grep_count: 7   sweep_count: 7   match: yes
category: line_items        grep_count: 33  sweep_count: 33  match: yes
category: agenda_items      grep_count: 2   sweep_count: 2   match: yes
category: annexure_ii_rows  grep_count: 4   sweep_count: 4   match: yes
category: auditor_paras     grep_count: 4   sweep_count: 4   match: yes
category: entities           grep_count: 0   sweep_count: 0   match: yes (note 7 explicitly states no subsidiary/associate/JV)
category: signature_blocks  grep_count: 3   sweep_count: 3   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used (reproducible):
- notes: `grep -n -E "^ *[0-9]{1,2} {2,}" extract... | grep -v <table-line-range>` (isolated to page-5 notes section, lines 260-290)
- line_items: `awk 'NR==203,NR==250' extract... | grep -n -E "^( *[0-9]{1,2}[ \t]+[A-Za-z(]|    \([a-z]\)|        \([iv]+\)|    Total|    Items that|    Basic and diluted)"`
- agenda_items: `grep -n -E "^ *[a-z]\)" extract...` (isolated to board outcome letter, lines 42-63)
- annexure_ii_rows: `grep -n -E "^ +[0-9]\s+(\||[A-Za-z])" extract...` (isolated to page 6, lines 314-330)
- auditor_paras: `grep -n -E "^[0-9]\.\s" extract...`
- signature_blocks: manual sweep for "Digitally signed", "Place:"/"Date:" pairs, "Chairman" + "DIN"

---

## 1. STATEMENT OF UNAUDITED FINANCIAL RESULTS — LINE ITEMS (33 rows, Sr. No. 1-12 + sub-items + totals)

Columns: Q1 FY27 (30 Jun 2026, Unaudited) | Q4 FY26 (31 Mar 2026, Unaudited, refer note 4) | Q1 FY26 (30 Jun 2025, Unaudited) | FY26 (31 Mar 2026, Audited). Units: Rs. lakhs except EPS.

| # | Sr.No | Particulars | Line | Q1 FY27 | Q4 FY26 | Q1 FY26 | FY26 | Flags |
|---|-------|-------------|------|---------|---------|---------|------|-------|
| 1 | 1 | Income (section header) | 203 | — | — | — | — | — |
| 2 | 1(a) | Revenue from operations | 204 | 4,103.25 | 7,829.03 | 3,918.27 | 21,878.41 | — |
| 3 | 1(b) | Other income | 205 | 681.20 | 303.93 | 211.76 | 949.73 | — |
| 4 | 1 | Total income | 206 | 4,784.45 | 8,132.96 | 4,130.03 | 22,828.14 | — |
| 5 | 2 | Expenses (section header) | 208 | — | — | — | — | — |
| 6 | 2(a) | Cost of materials consumed | 209 | 2,933.41 | 3,151.26 | 2,052.49 | 9,732.36 | — |
| 7 | 2(b) | Changes in inventories of finished goods and work-in-progress | 210-211 | (1,417.69) | (23.13) | (464.58) | (632.69) | — |
| 8 | 2(c) | Employee benefits expense | 212 | 540.16 | 530.43 | 450.96 | 2,051.18 | — |
| 9 | 2(d) | Finance costs | 213 | 16.47 | 19.01 | 18.59 | 70.25 | — |
| 10 | 2(e) | Depreciation and amortisation expense | 214 | 120.30 | 131.74 | 125.49 | 503.46 | — |
| 11 | 2(f) | Other expenses (sub-header) | 215 | — | — | — | — | — |
| 12 | 2(f)(i) | Manufacturing and operating expense (Consumption of stores and spares, power and fuel, job work charges, etc.) | 216-218 | 913.95 | 929.73 | 597.44 | 2,825.07 | — |
| 13 | 2(f)(ii) | Others | 219 | 704.05 | 816.95 | 600.62 | 2,747.67 | — |
| 14 | 2 | Total expenses | 220 | 3,810.65 | 5,555.99 | 3,381.01 | 17,297.30 | — |
| 15 | 3 | Profit before exceptional item and tax (1-2) | 222 | 973.80 | 2,576.97 | 749.02 | 5,530.84 | — |
| 16 | 4 | Exceptional item - gain (refer note no 6) | 223 | - | 27,353.05 | - | 27,353.05 | ZERO_STANDING (current qtr and Q1 FY26 nil; the Thane land-sale gain booked only in Q4 FY26 / FY26) |
| 17 | 5 | Profit before tax (3+4) | 224 | 973.80 | 29,930.02 | 749.02 | 32,883.89 | — |
| 18 | 6 | Tax expense (section header) | 226 | — | — | — | — | — |
| 19 | 6(a) | Current tax | 227 | 197.41 | 4,152.31 | 211.49 | 4,928.14 | — |
| 20 | 6(b) | Deferred tax charge/(credit) | 228 | 50.94 | 14.76 | (18.31) | (8.84) | — |
| 21 | 6(c) | Prior period tax adjustments | 229 | - | - | - | (21.62) | ZERO_STANDING (nil in all quarterly columns; only the FY26 annual column carries a value) |
| 22 | 6 | Total tax expense | 230 | 248.35 | 4,167.07 | 193.18 | 4,897.68 | — |
| 23 | 7 | Net profit for the period/year (5-6) | 232 | 725.45 | 25,762.95 | 555.84 | 27,986.21 | — |
| 24 | 8 | Other comprehensive income (net of taxes) (section header) | 234 | — | — | — | — | — |
| 25 | 8 | Items that will not be reclassified to profit or loss: (sub-header) | 235 | — | — | — | — | — |
| 26 | 8(a) | Remeasurement of the defined employee benefit plan - gain | 236-237 | - | 3.63 | - | 3.63 | ZERO_STANDING (nil in Q1 FY27 and Q1 FY26) |
| 27 | 8(b) | Income tax charge relating to the above | 238 | - | (0.91) | - | (0.91) | ZERO_STANDING (nil in Q1 FY27 and Q1 FY26) |
| 28 | 8 | Total other comprehensive income | 239 | - | 2.72 | - | 2.72 | ZERO_STANDING (nil in Q1 FY27 and Q1 FY26) |
| 29 | 9 | Total comprehensive income for the period/year (7+8) | 241 | 725.45 | 25,765.67 | 555.84 | 27,988.93 | — |
| 30 | 10 | Paid up equity share capital (Face value of Rs. 10 each) | 243-244 | 197.50 | 197.50 | 197.50 | 197.50 | — |
| 31 | 11 | Other equity | 246 | (blank) | (blank) | (blank) | 41,262.09 | ZERO_STANDING (interim quarterly columns are blank by convention; only the audited annual column is populated) |
| 32 | 12 | Earnings per equity share (Face value of Rs. 10 each) (section header) | 248 | — | — | — | — | — |
| 33 | 12 | Basic and diluted (Rs.) *Not annualised | 249-250 | 36.73* | 1,304.45* | 28.14* | 1,417.02 | — |

ZERO_STANDING count: 6 (rows 16, 21, 26, 27, 28, 31).

---

## 2. NOTES TO THE UNAUDITED FINANCIAL RESULTS (7 notes, page 5)

| Note # | Line(s) | First 15 words | Flags |
|--------|---------|-----------------|-------|
| 1 | 260-263 | "The unaudited financial results (Statement) has been prepaed in accordance with the recognition and measurement" | — |
| 2 | 264-266 | "The above Statement is reviewed and recommended to the Board of Directors by the Audit" | — |
| 3 | 267-269 | "Consideding the nature of operations and the manner in which the chief operating decision maker" | — |
| 4 | 270-271 | "The figures for the quarter cnded 31 March 2026 are the balancing figures between the" | — |
| 5 | 272-284 | "The Board of Directors had recommended final equity dividend of Rs. 40 per share (400%" | Text-layer reading order scrambled at source (raw fragments at 272-276); clean OCR re-extraction at 278-284 used for this row. Discloses aggregate FY26 dividend recommendation of Rs. 100/share (1000% of face value), comprising Rs. 40/share final + Rs. 60/share special (Thane land sale), subject to AGM shareholder approval. |
| 6 | 286-289 | "During the previous quacter and year ended 31 March 2026, the Company had disposed of" | Explains the exceptional gain (Rs. 27,353.05 lakhs) referenced at line-item row 16 above; cross-references Sr. No. 4 of the Statement. |
| 7 | 290 | "The Company does not have any subsidiary/associate /joint venture, hence consolidated financial results is" | ZERO_STANDING (explicit nil-consolidation disclosure); indentation differs from notes 1-6 (starts further right, "         7   " vs "     N       "), consistent with note 6 running long and pushing note 7's number out of the standard left margin — flagged for A3 to confirm this is a formatting artifact, not a mis-numbering. |

---

## 3. BOARD OUTCOME LETTER — AGENDA ITEMS (page 1)

Board meeting: held 06 August 2026, started 03:15 p.m. (IST), concluded 5:50 p.m. (IST). Duration: approx. 2 hours 35 minutes.

| Item | Line(s) | Description | Flags |
|------|---------|-------------|-------|
| a | 50-54 | Approved the Unaudited Financial Results of the Company for Q1 FY27 (quarter ended 30 June 2026) per Reg. 33; Financial Results + Limited Review Report attached as Annexure I. | — |
| b | 56-63 | Accepted and took on record the resignation of Mr. Bhautesh Shah as Company Secretary and Compliance Officer (KMP), effective from closing hours of 15 September 2026; Board placed on record appreciation for his tenure; Reg. 30 read with Schedule III disclosure enclosed as Annexure II (text truncated at source page break; continues on page 6). | Only two substantive agenda items in this outcome letter; no AR approval, AGM notice, record date, dividend declaration (dividend is a Board *recommendation* disclosed in Note 5, not a board-outcome-letter agenda item), director appointment/reappointment, auditor change, scrutinizer appointment, ESOP grant, or capital-raising resolution appears in this letter. |

---

## 4. ANNEXURE II — REGULATION 30 / SCHEDULE III DISCLOSURE TABLE (4 rows, page 6)

Re: resignation of Mr. Bhautesh Shah, Company Secretary & Compliance Officer.

| Row | Line(s) | Field | Content | Flags |
|-----|---------|-------|---------|-------|
| 1 | 317-321 | Reason for change viz. appointment / resignation | Resignation of Mr. Bhautesh Shah from the post of Company Secretary and Compliance Officer (KMP) w.e.f. closing hours of 15 September 2026, to pursue growth opportunities outside the organization. | — |
| 2 | 322-324 | Date of appointment/cessation (as applicable) & term of appointment | Mr. Bhautesh Shah will be relieved from his responsibilities w.e.f. closing hours of 15 September 2026. | — |
| 3 | 325-326 | Brief Profile (in case of appointment) | Not applicable | ZERO_STANDING (template field n/a for a resignation, not an appointment) |
| 4 | 327-329 | Disclosure of Relationship between Directors (in case of appointment of Director) | Not applicable | ZERO_STANDING (template field n/a; Mr. Shah is CS/KMP, not a Director, and this is a resignation) |

---

## 5. AUDITOR'S LIMITED REVIEW REPORT (pages 2-3)

Auditor: Walker Chandiok & Co LLP, Chartered Accountants, FRN 001076N/N500013. Partner: Murad D. Daruwalla, Membership No. 043334. UDIN: 26043334EKKUPA4264. Place: Mumbai. Date: 06 August 2026 (lines 162-178).

| Para # | Line(s) | Type | First 15 words |
|--------|---------|------|-----------------|
| 1 | 116-119 | Scope statement | "We have reviewed the accompanying statement of unaudited financial results (the 'Statement') of Uni-" |
| 2 | 121-127 | Management responsibility / basis of preparation | "The Statement, which is the responsibility of the Company's management and approved by the" |
| 3 | 129-137 | Basis of review (SRE 2410) | "We conducted our review of the Statement in accordance with the Standard on Review Engagements" |
| 4 | 154-159 | Conclusion | "Based on our review conducted as above, nothing has come to our attention that causes us to believe" — unmodified/clean conclusion, no material misstatement noted. |

Report structure notes:
- No Emphasis of Matter paragraph present.
- No Other Matters paragraph present.
- No Going Concern language present.
- Entity list reviewed: Uni-Abex Alloy Products Limited (standalone only; the Company has no subsidiary/associate/JV per Note 7, so this is inherently a single-entity, non-consolidated review — no entities are described as "unaudited" or "management-furnished" since there is no consolidation).
- Conclusion type: unmodified / clean (no qualification, adverse conclusion, or disclaimer).

---

## 6. CONSOLIDATION ENTITY LIST

| Entities | Line | Status | Flags |
|----------|------|--------|-------|
| None — standalone only | 290 (Note 7) | "The Company does not have any subsidiary/associate/joint venture, hence consolidated financial results is not applicable to the Company." | ZERO_STANDING (explicit nil-entity disclosure; no prior-quarter ledger available to cross-check for ENTITY_CHANGE — new coverage) |

---

## 7. DIGITAL SIGNATURE / SIGN-OFF BLOCKS

| # | Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---------|-----------|-------------|-----------|-------|
| 1 | 76-82 | Bhautesh Ashwin Shah | Company Secretary & Compliance Officer (signing the BSE cover letter, i.e. the outgoing CS himself transmitting his own resignation outcome) | Digitally signed; Date: 2026.08.06 18:11:53 +05'30' | Signature timestamp (18:11:53 IST) is after the board meeting's stated conclusion (17:50 IST) — consistent, no BEFORE_CONCLUSION flag. Notable: the resigning CS is the signatory transmitting the letter disclosing his own resignation. |
| 2 | 162-178 | Murad D. Daruwalla | Partner, Walker Chandiok & Co LLP, Chartered Accountants (Membership No. 043334) | Place: Mumbai; Date: 06 August 2026 (no intraday timestamp in extract) | — |
| 3 | 297-306 [OCR page 5] | F.D. Neterwala | Chairman, DIN: 00008332 (signing the Statement of unaudited financial results itself) | Place: Mumbai; Date: 6 August 2026 (no intraday timestamp; signature block image recovered via OCR, entirely absent from raw text layer) | Signature image absent from text layer; recovered by 300dpi rasterisation per A1 header — flagged only as an extraction-quality note, not a filing defect. |

---

## 8. ENCLOSURES / SUPPORTING DOCUMENTS

| # | Line(s) | Document | Flags |
|---|---------|----------|-------|
| 1 | 92-306 | Annexure I: Limited Review Report + Statement of unaudited financial results (Sections A and B) | — |
| 2 | 308-340 | Annexure II: Regulation 30 / Schedule III disclosure table (resignation) | — |
| 3 | 342-378 | Enclosed resignation letter of Mr. Bhautesh Shah, dated 7 July 2026, addressed to Mr. A.F. Neterwala (Vice Chairman) | Resignation letter is dated 7 July 2026, i.e. approx. 1 month before the Board's formal acceptance on 6 August 2026 — enumerated as-is; interpretation left to A3/A4. |

---

## SUMMARY COUNTS

- Notes: 7
- Line items (financial statement, all Sr. No. rows + sub-items + section headers + totals): 33
- Zero-standing line items: 6
- Board outcome agenda items: 2
- Annexure II table rows: 4
- Auditor report paragraphs: 4
- Consolidation entities: 0 (explicit nil)
- Digital signature blocks: 3
- Enclosures/documents: 3
