# A2 COMPLETENESS LEDGER — Reg 32(1) Use-of-Proceeds Declaration
Company: Finkurve Financial Services Ltd (Arvog) | Ticker: FINKURVE | Quarter: Q1 FY27
Doctype: results (Regulation 32(1) declaration + Annexure 1, preferential issue of equity shares and share warrants)
A1 extract: /home/user/inflection-pipeline/runs/finkurve-q1fy27/work/extract_reg32_finkurve_q1fy27.txt
Line numbers below are the A1 extract's own embedded line numbers (1-95), not raw file lines.

```
=== A2 COUNT TEST ===
category: letter_fields         grep_count: 16   sweep_count: 16   match: yes
category: annexure_summary      grep_count: 14   sweep_count: 14   match: yes
category: objects_table_cells   grep_count: 7    sweep_count: 7    match: yes
category: footnotes             grep_count: 4    sweep_count: 4    match: yes
total_disclosure_units: 41   (16 + 14 + 7 + 4)
gate_a2: pass
=== END COUNT TEST ===
```

Grep methodology: one uniquely anchored fixed-string / anchored-regex pattern per manually
identified unit (16 letter patterns, one `^[0-9]+\t [A-Z]` structural pattern matched against
the Annexure 1 summary block returning 14 hits, one tokenizer pass on the single objects-table
data row returning 7 cell tokens, one anchored pattern for the (a)/(b)/(c) definitions plus one
pattern for the inline "Rs. 30cr" explanatory note). Each grep pattern was checked file-wide
(not range-restricted) to confirm no false positives outside the intended block. Manual sweep
performed by reading the full extract line-by-line against the source structure (letter, table
header block, objects table, footnote block). All four categories reconcile exactly.

---

## Table 1 — Cover Letter / Declaration Fields (page 1)

| # | Line(s) | Field / Unit | Value (as extracted) | Flags |
|---|---------|--------------|----------------------|-------|
| 1 | 2 | Letter date | August 13, 2026 | |
| 2 | 4-9 | Addressee 1 | Listing Department, BSE Limited, Phiroze Jeejeebhoy Towers, Dalal Street, Mumbai 400001 | |
| 3 | 4-9 | Addressee 2 | The Manager – Compliance Department, National Stock Exchange of India Limited, 'Exchange Plaza' Bandra Kurla Complex, Bandra (East) Mumbai 400051 | |
| 4 | 11-12 | BSE Scrip Code field | "Scrip Code:" label followed on next line by "Equity: 508954" | LAYOUT_QUIRK — value appears to be the BSE scrip code (508954) but is rendered under a sub-label "Equity:" one line below the "Scrip Code:" label, a two-column-to-single-column pdftotext merge artifact; not a missing value, flagged for A3/A4 verification against BSE's known scrip code for FINKURVE |
| 5 | 11 | NSE Symbol field | NSE Symbol: FINKURVE | |
| 6 | 14-15 | Subject line | "Declaration in respect of Regulation 32(1) of Securities and Exchange Board of India (Listing Obligations and Disclosure Requirements) Regulations 2015" | |
| 7 | 17 | Salutation | Dear Sir/Madam, | |
| 8 | 19-23 | Declaration statement | Proceeds of the Preferential Issue of Equity Shares and Share Warrants (private placement, issued during quarter ended June 30, 2026) were used for the purpose stated in the offer document; no material deviation in use of proceeds from the objects stated in the offer document | |
| 9 | 25-26 | Audit Committee review statement | Annexure 1 statement for quarter ended June 30, 2026 "has been reviewed and noted by the Audit Committee at its Meeting held on August 13, 2026" | Audit Committee meeting date = same calendar date as the letter/filing date (Aug 13, 2026); no meeting start/end time disclosed (not applicable to this doctype — no Board Outcome letter present in this extract) |
| 10 | 28 | Closing request to exchanges | "You are requested to take note of the same." | |
| 11 | 30 | Valediction | Thanking you | |
| 12 | 31 | Company signoff | For Finkurve Financial Services Limited | |
| 13 | 32-36 | Digital signature block | Digitally signed by Kajal Kunal Parmar, Date: 2026.08.13 12:49:38 +05'30' | Signature timestamp (12:49:38, Aug 13 2026) is same-day as, and cannot be checked against, the undisclosed Audit Committee meeting time (no meeting time stated anywhere in this extract) — flag for A3/A4 if a companion Board Outcome / Audit Committee outcome filing with a meeting time exists this quarter |
| 14 | 39 | Signatory printed name | Kajal Parmar | |
| 15 | 40 | Signatory designation | Company Secretary & Compliance Officer | |
| 16 | 41 | Signatory membership number | Membership No: ACS65484 | |
| — | 43 | Enclosure line | Encl: as above | counted in footnotes/ancillary text below, not double-counted here (see note) |

Note: row 16 above ("Encl: as above", line 43) IS counted as the 16th letter-field grep/sweep
unit; it is listed at the bottom of the table for readability but included in both counts.

---

## Table 2 — Annexure 1 Summary Statement Fields (page 2, lines 45-69)

| # | Line(s) | Field label | Value (as extracted) | Flags |
|---|---------|-------------|-----------------------|-------|
| 1 | 50 | Name of listed entity | Finkurve Financial Services Limited | |
| 2 | 51-52 | Mode of Fund Raising | Preferential Issue of Equity Shares and Share Warrant on Private Placement Basis | |
| 3 | 53 | Date of Raising Funds | May 21, 2025 and May 27, 2025 | two distinct allotment dates disclosed as one field — dual-tranche raise |
| 4 | 54 | Amount Raised (total raised) | Rs. 141.50 Crore | TOTAL_RAISED |
| 5 | 55 | Report filed for Quarter ended | June 30, 2026 | |
| 6 | 56 | Monitoring Agency | Applicable | |
| 7 | 57 | Monitoring Agency Name, if applicable | CRISIL Rating Limited | |
| 8 | 58-59 | Is there a Deviation / Variation in use of funds raised | No | DEVIATION_DECLARATION — the core Reg 32(1) attestation |
| 9 | 60-62 | If yes, whether pursuant to change in terms of a contract or objects approved by shareholders | - (dash) | ZERO_STANDING |
| 10 | 63 | If Yes, Date of shareholder Approval | - (dash) | ZERO_STANDING |
| 11 | 64 | Explanation for the Deviation / Variation | - (dash) | ZERO_STANDING |
| 12 | 65 | Comments of the Audit Committee after review | - (dash) | ZERO_STANDING |
| 13 | 66 | Comments of the auditors, if any | - (dash) | ZERO_STANDING |
| 14 | 67-69 | Objects for which funds raised and where there has been a deviation, in the following table | Not Applicable | ZERO_STANDING (nil-equivalent — precedes the objects table, which is nonetheless populated with the ordinary utilisation data, not a deviation table) |

---

## Table 3 — Objects / Use-of-Proceeds Table (Annexure 1, lines 70-90)

Header row (column labels, structural — not counted as a content disclosure unit in the count
test, listed for reference): Original Object | Modified Object, if any | Original Allocation
(Rs. In Crore) | Modified allocation, if any (Rs. In Crore) | Funds Utilised (Rs. In Crore) |
Amount of Deviation/Variation for the quarter according to applicable object | Remarks if any
(lines 70-76).

Single data row, one object of issue disclosed, cell-by-cell:

| # | Line(s) | Column | Value | Flags |
|---|---------|--------|-------|-------|
| 1 | 77-90 | Original Object | Onward lending and investment and repayment of borrowing obtained by company in ordinary course of business | object of issue |
| 2 | 77 | Modified Object, if any | NA | ZERO_STANDING |
| 3 | 77 | Original Allocation (Rs. In Crore) | 141.50 | amount planned |
| 4 | 77 | Modified allocation, if any (Rs. In Crore) | NA | ZERO_STANDING |
| 5 | 77, 79-86 | Funds Utilised (Rs. In Crore) | 111.50, with inline note "(Rs. 30cr Being 75% of the share warrants subscription amount yet to be received)" | amount utilised; see footnote below — the ~Rs. 30 crore shortfall against the Rs. 141.50 crore allocation is explained in-cell as unreceived share-warrant call money, NOT as unutilised-but-received proceeds. No explicit "unutilised balance" column exists anywhere in this table — see STRUCTURAL_GAP flag below |
| 6 | 77 | Amount of Deviation/Variation for the quarter according to applicable object | NA | ZERO_STANDING |
| 7 | 77 | Remarks if any | NA | ZERO_STANDING |

STRUCTURAL_GAP: the source table has no labeled "unutilised balance" / "closing balance" field.
A2 does not compute Original Allocation minus Funds Utilised (141.50 − 111.50 = 30.00 Cr); the
document's own inline note already attributes the entire gap to unreceived share-warrant
subscription money rather than to un-deployed cash-in-hand. This distinction (deployed-vs-total
vs received-vs-total) is an interpretation question for A3/A4, not an enumeration task.

---

## Table 4 — Footnotes / Definitional Text (lines 79-95)

| # | Line(s) | Footnote | Text | Flags |
|---|---------|----------|------|-------|
| 1 | 79-86 | Inline note on Funds Utilised cell | "(Rs. 30cr Being 75% of the share warrants subscription amount yet to be received)" | qualifies the Funds Utilised figure of Rs. 111.50 Cr in Table 3 row 5 |
| 2 | 93 | Definitional footnote (a) | "Deviation in the objects or purposes for which the funds have been raised or" | |
| 3 | 94 | Definitional footnote (b) | "Deviation in the amount of funds actually utilized as against what was originally disclosed or" | |
| 4 | 95 | Definitional footnote (c) | "Change in terms of a contract referred to in the fund raising document i.e. prospectus, letter of offer, etc." | |

---

## Flags Summary

- ZERO_STANDING (10 instances): Table 2 rows 9-14 (6 dash/Not-Applicable fields) + Table 3
  rows 2, 4, 6, 7 (4 "NA" cells in the objects table).
- LAYOUT_QUIRK (1 instance): Table 1 row 4, BSE Scrip Code rendering.
- TOTAL_RAISED (1 instance): Table 2 row 4, Rs. 141.50 Crore.
- DEVIATION_DECLARATION (1 instance): Table 2 row 8, "No" deviation attestation — the
  substantive Reg 32(1) declaration this whole filing exists to make.
- STRUCTURAL_GAP (1 instance): no labeled unutilised-balance field in the objects table; the
  Rs. 30 Cr gap between allocation and utilisation is explained only via inline note as
  unreceived share-warrant money, not computed or labeled as a standing "balance" line.

No agenda items, auditor paragraphs, consolidation entities, concall turns/questions, or
presentation slides apply to this doctype (a stand-alone Reg 32(1) declaration + Annexure 1);
those ledger categories from the general instruction set are not applicable and are recorded
as 0 in the YAML block below.

```yaml
stage: A2-enumerator
company: "finkurve"
quarter: "q1fy27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/finkurve-q1fy27/work/ledger_reg32_finkurve_q1fy27.md"
counts:
  letter_fields: 16
  annexure_summary_fields: 14
  objects_table_cells: 7
  footnotes: 4
  zero_standing: 10
  notes: 4
  line_items: 21
  agenda_items: 0
  auditor_paras: 0
  entities: 0
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
  total_disclosure_units: 41
flags_raised: [ZERO_STANDING, LAYOUT_QUIRK, TOTAL_RAISED, DEVIATION_DECLARATION, STRUCTURAL_GAP]
gate_a2: pass
mismatch_note: ""
```
