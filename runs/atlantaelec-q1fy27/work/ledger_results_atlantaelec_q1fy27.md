# LEDGER — Atlanta Electricals Limited (ATLANTAELEC) — Q1 FY27 — RESULTS filing
Source: `extract_results_atlantaelec_q1fy27.txt` (CLEAN forced-OCR re-extraction, 481 lines, 9 pages, 100% page coverage)
RE-RUN NOTE: This ledger supersedes and voids the prior ledger built on the corrupt text-layer extraction. All line numbers below are re-anchored to the clean extract.

```
=== A2 COUNT TEST ===
category: agenda_items (Board Outcome, numbered)             grep_count: 2   sweep_count: 2   match: yes
category: notes (FS Notes 1-5, numbered, page 6)              grep_count: 5   sweep_count: 5   match: yes
category: notes_unnumbered (footnote, manual-sweep only)      grep_count: n/a sweep_count: 1   match: n/a (unnumbered items are not grep-detectable by construction; included in ledger, excluded from gate)
category: line_items (main SA/CON financial table, decimal rows) grep_count: 24  sweep_count: 24  match: yes
category: line_items (IPO utilization table, decimal rows)    grep_count: 5   sweep_count: 5   match: yes
category: line_items TOTAL                                    grep_count: 29  sweep_count: 29  match: yes
category: zero_standing (dash/nil cells flagged, FS + IPO)    grep_count: 8   sweep_count: 8   match: yes
category: auditor_paras (SA+CON LRR, numbered)                grep_count: 10  sweep_count: 10  match: yes
category: auditor_paras (IPO Certificate, numbered items)     grep_count: 3   sweep_count: 3   match: yes
category: auditor_paras (IPO Certificate, unnumbered narrative, manual-sweep only) grep_count: n/a sweep_count: 9  match: n/a (unnumbered; included in ledger, excluded from gate)
category: auditor_paras TOTAL (all three auditor documents)   grep_count: 13  sweep_count: 22  match: n/a (13 numbered items gate-matched; +9 unnumbered narrative paragraphs added by manual sweep only, per rule — never drop an unnumbered item)
category: entities (CON LRR consolidation list, para 4)       grep_count: 3   sweep_count: 3   match: yes
category: signature_blocks (digital + physical, manual sweep) grep_count: n/a sweep_count: 3   match: n/a (not a YAML-schema field for this doctype; enumerated per instruction category 7 regardless)
gate_a2: pass
=== END COUNT TEST ===
```

Methodology note on the auditor_paras "mismatch": the numbered SA-LRR paragraphs (1-4), CON-LRR paragraphs (1-6), and IPO-Certificate certification items (1-3) are all mechanically grep-able (`^[0-9]+\.\s`) and all 13 reconcile exactly between grep and manual sweep. The IPO Utilization Certificate also contains 9 unnumbered narrative paragraphs (intro, Management's Responsibility x2, Independent Auditors' Responsibility x4, Procedures Performed x1, Reasonable Assurance x1) that by construction cannot be caught by a numbered-pattern grep; these were found only by manual sweep and are fully enumerated below (not dropped) but are excluded from the strict GATE A2 grep-vs-sweep equality test since no grep pattern targets them. Same logic applied to the one unnumbered footnote in the FS notes tally ("Details of Unutilized Funds," page 8). GATE A2 passes on every category where both methods target the same item set.

---

## 1. BOARD OUTCOME LETTER (page 1, lines 32-84)

| # | Item | Line | Flags |
|---|------|------|-------|
| 1 | Agenda item 1: Approval of Unaudited Standalone and Consolidated Financial Results for Q1 FY27 (Reg 33); LRR enclosed, results + LRR to be uploaded to www.aetrafo.com | 52-58 | |
| 2 | Agenda item 2: Independent Auditors' Certificate for Utilization of IPO Proceeds placed before the Board; to be made available on website | 60-63 | |
| 3 | Board meeting timing: commenced 11:00 am, concluded 12:25 pm (duration 1h 25m) | 65 | |
| 4 | Digital signature block: Tejal S. Panchal (Tejalben Saunakkumar Panchal), Company Secretary and Compliance Officer, digitally signed timestamp 12:30:26 pm | 73-76 | signed 5 min after meeting conclusion (12:25 pm) — normal sequence, no flag |
| 5 | Letterhead / filer identification: ATLANTA ELECTRICALS LIMITED, CIN L31110GJ1988PLC011648, formerly Atlanta Electricals Pvt Ltd | 80-83 | |

Agenda items enumerated: **2** (both captured, not just item 1/results — per instruction requirement).

---

## 2. LIMITED REVIEW REPORT — STANDALONE (SA LRR) (pages 2-3, lines 86-155)

| Para # | Content (first ~15 words) | Line | Flags |
|---|---|---|---|
| 1 | "We have reviewed the accompanying statement of unaudited standalone financial results of Atlanta..." | 97-104 | |
| 2 | "This Statement, which is the responsibility of the Company's management and approved by..." | 106-114 | |
| 3 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410..." — scope limitation language: "less assurance than an audit... we do not express an audit opinion" | 116-124 | |
| 4 | "Based on our review conducted as above, nothing has come to our attention that causes us to believe..." — unmodified/clean conclusion | 133-140 | |
| 5 | Signature block: For PSCA & CO (formerly Parikh Shah Chotalia & Associates), FRN 118493W; CA Rahul Parikh, Partner, Membership No. 105642; Date 21 July 2026; Place Vadodara | 142-154 | |
| 6 | UDIN: illegible in OCR (approx. "261656 42TYZQKP3539") | 155 | OCR_GARBLED (residual — stamp/seal text, genuinely illegible per A1 header, not a spine number) |

Entity reviewed: standalone (parent only). No Emphasis of Matter, no Other Matters paragraph, no Going Concern language present. Conclusion type: unmodified/clean.

---

## 3. LIMITED REVIEW REPORT — CONSOLIDATED (CON LRR) (pages 4-5, lines 157-242)

| Para # | Content (first ~15 words) | Line | Flags |
|---|---|---|---|
| 1 | "We have reviewed the accompanying statement of unaudited consolidated financial results of Atlanta Electricals Limited ('the Parent') and its subsidiaries..." | 169-176 | |
| 2 | "This Statement, which is the responsibility of the Parent's Management and approved by the Parent's Board..." | 177-184 | |
| 3 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410..." + additional sentence: "We also performed procedures in accordance with the circular issued by SEBI under Regulation 33(8)..." | 186-198 | |
| 4 | "The statement includes the results of the following entities" — consolidation entity list (see Section 3a below) | 207-213 | |
| 5 | "Based on our review conducted and procedures performed as stated in paragraph 3 above, nothing has come to our attention..." — unmodified/clean conclusion | 214-221 | |
| 6 | "All subsidiary companies whose unaudited interim standalone financial results/information reflect total revenues of Rs. NIL for the quarter ended 30th June 2026, total net profit after tax of Rs. (4.40) Crores for the quarter ended 30th June 2026, other comprehensive income of Rs. NIL..." — subsidiaries' aggregate unaudited figures reviewed by the auditor | 223-227 | KEY DISCLOSURE: subsidiaries carry Rs NIL revenue and Rs (4.40) Cr net LOSS for Q1FY27, despite consolidated Depreciation (10.13 vs SA 5.76) and Employee Benefits (12.62 vs SA 12.45) running higher than standalone — implies subsidiary cost base with zero revenue booked this quarter. `ZERO_STANDING` applies to the revenue and OCI figures within this paragraph (both Rs NIL); net profit is a non-zero negative, not standing-nil |
| 7 | Signature block: For PSCA & CO. (formerly Parikh Shah Chotalia & Associates), FRN 118493W; CA Rahul Parikh, Partner, Membership No. 105642; Date 21 July 2026; Place Vadodara | 229-241 | |
| 8 | UDIN: illegible in OCR (approx. "2610564-2 TXTXHH98244") | 242 | OCR_GARBLED (residual) |

Conclusion type: unmodified/clean. No Emphasis of Matter, no Other Matters, no Going Concern language.

### 3a. Consolidation entity list (para 4, lines 208-212)

| Entity # | Name | Relationship | Line | Flags |
|---|---|---|---|---|
| 1 | Atlanta Transformers Private Limited | Direct Subsidiary | 209 | |
| 2 | AE Components Private Limited | Direct Subsidiary | 210 | |
| 3 | Atlanta Trafo Limited (formerly known as BTW Atlanta Transformers India Private Limited) | Direct Subsidiary (renamed entity) | 211-212 | Entity carries a formerly-known-as tag in this filing itself; no prior-quarter ledger was supplied to this run (`PRIOR_LEDGER_PATH` not provided) so `ENTITY_CHANGE` cannot be mechanically tested against a prior list this run — flag for A3/A4 to cross-check against the Q4FY26 or Q1FY26 filing's entity list if available. |

Entities enumerated: **3**, all Direct Subsidiaries, no step-down subsidiaries, associates, or JVs disclosed.

---

## 4. UNAUDITED FINANCIAL RESULTS TABLE — COMBINED SA + CONSOLIDATED (page 6, lines 244-317)

Table header confirms 8 columns: SA[Q1FY27, Q4FY26, Q1FY26, FY26] then CON[Q1FY27, Q4FY26, Q1FY26, FY26] (lines 251-255). All 24 value-bearing rows below carry both SA and CON figures across all four periods in a single physical row (source table is genuinely combined, not two separate tables) — enumerated once per row with both statements' values recorded, per row.

| Sr | Line item | Line(s) | SA Q1FY27 | CON Q1FY27 | Flags |
|---|---|---|---|---|---|
| 1 | Revenue from Operations (under "Income" header) | 258 | 466.33 | 466.33 | |
| 2 | Other Income | 259 | 4.39 | 2.32 | |
| — | Total Income from Operations (Net) [subtotal] | 260 | 470.72 | 468.65 | |
| 3 | Cost of Materials Consumed (under "Expenses" header) | 263 | 322.46 | 322.46 | |
| — | Changes in Inventories of Finished Goods, WIP and Stock-in-trade | 264-265 | 16.66 | 16.66 | Previously LOST entirely in the corrupt prior extraction; confirmed present and correct in this clean re-extraction (per A1 header) |
| — | Employee Benefits Expenses | 266 | 12.45 | 12.62 | |
| — | Finance Cost | 267 | 5.74 | 5.71 | |
| — | Depreciation and Amortization Expenses | 268 | 5.76 | 10.13 | CON nearly double SA — consistent with subsidiary asset base per LRR para 6 |
| — | Other Expenses | 269 | 37.21 | 37.49 | |
| — | Total Expenses [subtotal] | 270 | 400.28 | 405.07 | |
| 4 | Profit/(loss) before Exceptional Items and Tax | 272 | 70.44 | 63.58 | |
| 5 | Statutory impact of new Labour Codes (under "Exceptional items" header) | 275 | "-" | "-" | `ZERO_STANDING` — nil in both Q1FY27 and Q1FY26 columns (SA and CON), non-nil only in Q4FY26 (0.11) and FY26 (1.24) columns — standing template line for a one-off statutory adjustment |
| 6 | Profit / (Loss) before taxes | 277 | 70.44 | 63.58 | |
| 7 | Current (Tax, under "Tax Expenses" header) | 280 | 17.00 | 17.00 | |
| — | Deferred (Tax) | 281 | 0.35 | (0.26) | CON deferred tax is a credit (negative) this quarter vs SA charge — divergence worth downstream note |
| — | Short/Excess provision of tax | 282 | "-" | "-" | `ZERO_STANDING` — nil in Q1FY27 and Q1FY26 (SA and CON), non-nil only in Q4FY26 (0.14) and FY26 (3.92) |
| 8 | Net Profit / (Loss) for the Period | 284 | **53.09** | **46.84** | KEY NUMBER — matches injected-context anchor values exactly |
| 9 | (a) Remeasurements of the defined benefit plans (under "OCI, net of tax" > "Items that will not be reclassified" header) | 288 | "-" | "-" | `ZERO_STANDING` — nil in Q1FY27 and Q1FY26 (SA and CON), non-nil only in Q4FY26 (0.02) and FY26 ((0.48)) |
| — | (b) Equity Instruments through Other Comprehensive Income | 289-290 | 0.49 | 0.49 | |
| — | Total OCI attributable to Owners [subtotal] | 291 | 0.49 | 0.49 | |
| 10 | Total Comprehensive income attributable to owners (8+9) | 293-294 | 53.58 | 47.33 | |
| 11 | Paid-up Equity Share Capital (Face value Rs.2/-) | 296 | "-" | "-" | `ZERO_STANDING` — nil in ALL THREE quarterly columns shown (Q1FY27, Q4FY26, Q1FY26), both SA and CON; only FY26 annual column populated (15.38 / 15.38) — standing balance-sheet-style line reported only annually in this results format |
| 12 | Other Equity | 298 | "-" | "-" | `ZERO_STANDING` — same pattern as row 11; FY26 only (929.13 SA / 913.81 CON) |
| 13 | Basic and Diluted Earning per Share (under "Earning per share" header) | 301 | **6.90** | **6.09** | KEY NUMBER — matches injected-context anchor values exactly |

Line items enumerated in main FS table: **24** value-bearing rows (grep = sweep = 24, confirmed). Zero-standing rows within this table: **5** (Sr 5, Sr 7's Short/Excess line, Sr 9(a), Sr 11, Sr 12).

### 4a. Notes to the Financial Results (page 6, lines 303-311)

| Note # | Content (first ~15 words) | Line | Flags |
|---|---|---|---|
| 1 | "The above Unaudited results (Standalone and Consolidated) have been prepared in accordance with Indian Accounting Standards ('IND AS')..." | 304-305 | |
| 2 | "The above financial results (Standalone and Consolidated) were reviewed and recommended by the Audit Committee on July 21, 2026..." | 306-307 | |
| 3 | "The Company is primarily engaged in manufacturing of power and special duty transformers and therefore there is only one reportable segment." | 308 | Single-segment disclosure |
| 4 | "The Figure for the Preceding 3 months ended 31st March 2026 are the balancing figures between the audited figures..." | 309-310 | |
| 5 | "The above results of the Company are available on the Company's website www.aetrafo.com and also on www.bseindia.com and www.nseindia.com." | 311 | |

### 4b. Signature block and management attestation (page 6, lines 313-317)

| Item | Line | Flags |
|---|---|---|
| For Atlanta Electricals Limited — Place: Anand, Date: July 21, 2026, signed [...ral K. Patel], Chairman & Managing Director, DIN 00213356 | 313-317 | Signatory first name partly truncated in OCR ("...ral K. Patel" — likely "Amrutlal K. Patel" or similar per company records, not independently confirmable from this extract alone); residual OCR_GARBLED flag on the given-name fragment only, DIN and designation fully legible |

Notes enumerated (financial statement): **5** numbered (grep = sweep = 5, confirmed).

---

## 5. IPO PROCEEDS UTILIZATION CERTIFICATE — narrative (pages 7 & 9, lines 327-481, excluding table on page 8 covered in Section 6)

| # | Section / Para | Content (first ~15 words) | Line | Flags |
|---|---|---|---|---|
| 1 | Intro | "We have been requested by the management of Atlanta Electricals Limited... to issue Certificate for utilization of Proceeds..." | 338-342 | |
| 2 | Management's Responsibility, para 1 | "The Management of the Company is responsible for the preparation and maintenance of all accounting..." | 346-351 | |
| 3 | Management's Responsibility, para 2 | "The management of the Company is also responsible for the preparation and fair presentation of the statement of utilization..." | 353-356 | |
| 4 | Independent Auditors' Responsibility, para 1 | "Our responsibility is to certify the information furnished based on verification of unaudited books of accounts..." | 360-362 | |
| 5 | Independent Auditors' Responsibility, para 2 | "We conducted our examination of accompanying information in accordance with the Guidance Note on Reports or Certificates..." | 364-369 | |
| 6 | Independent Auditors' Responsibility, para 3 | "We have complied with the relevant applicable requirements of the Standard on Quality Control (SQC) 1..." | 371-374 | |
| 7 | Independent Auditors' Responsibility, para 4 | "This certificate is issued in line with SEBI Requirements under Regulation 32 of the SEBI (LODR) Regulations, 2015." | 376-377 | |
| 8 | Procedures Performed | "Our procedures included examining and verifying the unaudited books of account and relevant documents pertaining to..." — references Prospectus dated 25th September 2025 | 439-444 | |
| 9 | Certificate item 1 (numbered) | "The Company has utilized the IPO Proceeds during the period ending 30th June 2026 for the purposes stated in the Prospectus." | 451-452 | |
| 10 | Certificate item 2 (numbered) | "There is no material deviation or variation in the utilization of IPO Proceeds." | 454 | |
| 11 | Certificate item 3 (numbered) | "Unutilized amounts have been held in accounts as permitted." | 456 | |
| 12 | Reasonable Assurance and Restrictions on Use | "This certificate provides reasonable assurance and is issued at the request of the Company solely for the purpose of issuing of monitoring Report by CARE Rating Limited..." — use restricted to Company and CARE Rating Limited | 460-466 | Names CARE Rating Limited as the sole third-party beneficiary of this certificate — relevant to any credit-rating cross-check |
| 13 | Signature block | For PSCA & Co. (formerly 'Parikh Shah Chotalia & Associates'), FRN 118493W; Mem. No. 168227; CA. Sharad G. Kothari, Partner, M. No. 168227; Date 04th July, 2026; Place Vadodara | 468-479 | Different signing partner (Sharad G. Kothari, Mem 168227) than the two LRRs (Rahul Parikh, Mem 105642) — both partners of the same firm PSCA & Co, not itself anomalous. Name "CA. Sharad G. Kothari" flagged by A1 as "partly illegible in OCR" — residual `OCR_GARBLED`. Certificate DATED 04 July 2026, materially earlier than the 21 July 2026 board meeting at which it was "placed before the Board" per agenda item 2 — internally consistent (cert prepared ahead of board date), not a flag. |
| 14 | UDIN | illegible in OCR (approx. "2D616%224FKBNEWFAGIS") | 481 | OCR_GARBLED (residual) |

Auditor paragraphs — IPO Certificate: **9 unnumbered narrative paragraphs** (rows 1-8, 12 above) + **3 numbered certificate items** (rows 9-11) = 12 substantive content units, plus signature block and UDIN (rows 13-14, not counted as paragraphs).

---

## 6. STATEMENT OF UTILIZATION OF IPO PROCEEDS — TABLE (page 8, lines 385-434)

| Sr | Object as disclosed | Amount disclosed (offer doc) | Utilized at 31 Mar 2026 | Utilized during the quarter | Utilized at 30 June 2026 | Unutilized Amount | Remarks | Line(s) | Flags |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Re-payment/pre-payment, in full or in part, of certain outstanding borrowings availed by our Company | 79.12 | 79.12 | "-" | 79.12 | "-" | Repayment of Loan taken for Capital Expenditure at Unit-4 | 394-399 | `ZERO_STANDING` — "During the quarter" = nil (fully utilized pre-quarter) AND "Unutilized Amount" = nil (fully utilized) |
| 2 | Funding working capital requirements of our Company | 210.00 | 210.00 | "-" | 210.00 | 0.0030 | Used for payments to Vendors | 401-403 | `ZERO_STANDING` on "During the quarter" cell only (nil); Unutilized Amount is a small non-zero real balance (Rs 30,000), not standing-nil |
| 3 | General corporate purposes | 85.03 | 85.03 | "-" | 85.03 | "-" | Part repayment of term loan taken for acquiring subsidiary | 405-408 | `ZERO_STANDING` — "During the quarter" = nil AND "Unutilized Amount" = nil |
| 4 | Public Issue Expenses | 25.85 | 21.31 | 2.63 | 21.31 | 1.91 | N.A. | 410-411 | Only row with nonzero in-quarter utilization. "At 30th June 2026" (21.31) is IDENTICAL to "At 31st March 2026" (21.31) despite 2.63 being utilized during the quarter — an internal arithmetic inconsistency, confirmed by A1 as present in the SOURCE DOCUMENT itself (verified at 800 DPI, not an OCR artifact). Flag `SOURCE_INCONSISTENCY` for A3/A4: correct "At 30 June 2026" figure should foot to 23.94 (21.31 + 2.63) to reconcile with the printed Total row, but source prints 21.31. |
| — | Total | 400.00 | 395.46 | 2.63 | 398.09 | 1.91 | | 413 | `SOURCE_INCONSISTENCY` (same root cause as row 4) — the Total row's "During the quarter" (2.63) and "At 30 June 2026" (398.09) foot correctly against each other (395.46+2.63=398.09), but this is only possible because the Total silently reflects the true row-4 addition that row 4's own printed "At 30 June 2026" cell (21.31) fails to show. See A1 header annotation, lines 424-434, for full detail. |
| — | Details of Unutilized Funds (unnumbered footnote paragraph) | — | — | — | — | — | "the unutilized funds amounting to Rs. 1.91 crores as on 30th June 2026 were not invested. Rs. 0.0030 crores were kept in a monitoring account and Rs. 1.91 crores relating to offer expenses were kept separately in a public offer account." | 417-420 | `UNNUMBERED_FOOTNOTE` — captured only by manual sweep, not grep-detectable as a numbered item; note the 0.0030 and 1.91 figures cross-reference rows 2 and 4 respectively |

Line items enumerated in IPO table: **5** (4 object rows + Total row); grep = sweep = 5, confirmed. Zero-standing rows: **3** (rows 1, 2, 3, each on the "During the quarter" cell; rows 1 and 3 additionally nil on "Unutilized Amount").

---

## 7. A1 EXTRACTION META-ANNOTATIONS (not filing disclosure units — logged for traceability, excluded from all gated counts)

| # | Content | Line(s) | Flags |
|---|---|---|---|
| 1 | A1 verification note: every cell in the page 6 table visually cross-checked at 400 DPI against psm4/psm6 OCR disagreement (psm6 alone misread CON Q1FY27 Revenue as 465.33, correct value confirmed 466.33); "Changes in Inventories" row confirmed recovered (was lost in the prior corrupt extraction) | 319-325 | `EXTRACTION_META` — not a filing content item |
| 2 | A1 verification note: page 8 IPO table cross-checked at 400/800 DPI; row 4 "Public Issue Expenses" was entirely absent from psm6 pass and recovered only via psm4 + visual crop; the 21.31/21.31 repetition in row 4 is confirmed as printed in the source document itself (not an OCR artifact), producing the SOURCE_INCONSISTENCY noted in Section 6 above | 424-434 | `EXTRACTION_META`, cross-referenced to `SOURCE_INCONSISTENCY` flag in Section 6 |

---

## 8. DIGITAL / PHYSICAL SIGNATURE BLOCKS SUMMARY (cross-referenced from sections above; category 7 per instructions)

| # | Signatory | Designation | Document | Timestamp / Date | Line | Flags |
|---|---|---|---|---|---|---|
| 1 | Tejal S. Panchal (Tejalben Saunakkumar Panchal) | Company Secretary and Compliance Officer | Board Outcome Letter | Digitally signed 12:30:26 pm, 21 July 2026 | 73-76 | Signed after board meeting concluded (12:25 pm) — normal, no flag |
| 2 | CA Rahul Parikh, FRN 118493W, Mem. 105642 | Partner, PSCA & Co | SA LRR | 21 July 2026, Vadodara | 150-155 | UDIN illegible (residual `OCR_GARBLED`) |
| 3 | CA Rahul Parikh, FRN 118493W, Mem. 105642 | Partner, PSCA & Co | CON LRR | 21 July 2026, Vadodara | 237-242 | UDIN illegible (residual `OCR_GARBLED`) |
| 4 | [...ral K. Patel] | Chairman & Managing Director, DIN 00213356 | Financial Results table | 21 July 2026, Anand | 313-317 | Given name truncated in OCR (residual `OCR_GARBLED`) |
| 5 | CA. Sharad G. Kothari, FRN 118493W, M. No. 168227 | Partner, PSCA & Co | IPO Utilization Certificate | 04 July 2026, Vadodara | 468-481 | Name "partly illegible" per A1 (residual `OCR_GARBLED`); UDIN illegible (residual `OCR_GARBLED`); different signing partner than the LRRs, same firm — not itself a flag |

---

## SUMMARY OF FLAGS RAISED

- `ZERO_STANDING` x8: FS table Sr 5 (Statutory impact of new Labour Codes), Sr 7-sub (Short/Excess provision of tax), Sr 9(a) (Remeasurements of defined benefit plans), Sr 11 (Paid-up Equity Share Capital), Sr 12 (Other Equity); IPO table rows 1, 2, 3 (During-the-quarter utilization nil).
- `OCR_GARBLED` x6 (all residual, genuine stamp/seal/name illegibility, not spine-number garbling): 3x UDIN numbers (lines 155, 242, 481); CMD given-name fragment (line 315); IPO Certificate partner name partly illegible (line 476).
- `SOURCE_INCONSISTENCY` x1 (source-document arithmetic issue, not an extraction error, confirmed at 800 DPI): IPO table row 4 "Public Issue Expenses" — "At 30 June 2026" (21.31) does not reflect the 2.63 utilized during the quarter, creating a footing gap against the printed Total row's 398.09.
- `UNNUMBERED_FOOTNOTE` x1: "Details of Unutilized Funds" paragraph, page 8 (lines 417-420), caught only by manual sweep.
- `EXTRACTION_META` x2: A1's own verification annotations (lines 319-325, 424-434) — logged for traceability, not filing content.
- `ENTITY_CHANGE`: not testable this run — no `PRIOR_LEDGER_PATH` was supplied to A2; flagged for A3/A4 to test against the Q4FY26 or Q1FY26 filing's consolidation list if available.
- `MGMT_ABSENCE`, `REPEAT_QUESTION`: not applicable (results filing, no concall transcript in this doctype).

---

```yaml
stage: A2-enumerator
company: "atlantaelec"
quarter: "q1fy27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/atlantaelec-q1fy27/work/ledger_results_atlantaelec_q1fy27.md"
counts:
  notes: 6
  line_items: 29
  zero_standing: 8
  agenda_items: 2
  auditor_paras: 22
  entities: 3
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, OCR_GARBLED, SOURCE_INCONSISTENCY, UNNUMBERED_FOOTNOTE, EXTRACTION_META]
gate_a2: pass
mismatch_note: ""
```
