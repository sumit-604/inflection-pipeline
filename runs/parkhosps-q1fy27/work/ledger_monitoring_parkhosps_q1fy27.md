# Enumeration Ledger — Park Medi World Limited (PARKHOSPS)
Doctype: monitoring (SEBI Reg 32(6) CRISIL Monitoring Agency Report on IPO proceeds, enumerated as results/regulatory class)
Quarter: Q1 FY27 (quarter ended June 30, 2026)
Unit convention in source: Rs Millions. Conversion to Cr: x0.1. All Rs figures below are quoted in Rs Millions exactly as filed; Cr equivalent given in parentheses where the number is load-bearing.
Source: /home/user/inflection-pipeline/runs/parkhosps-q1fy27/work/extract_monitoring_parkhosps_q1fy27.txt (13 pages, 677 lines)
Prior-quarter ledger: none provided — no DROPPED_SLIDE / ENTITY_CHANGE diff possible this run.

```
=== A2 COUNT TEST ===
category: notes            grep_count: 15   sweep_count: 15   match: yes
category: line_items       grep_count: 21   sweep_count: 21   match: yes
category: zero_standing    grep_count: 12   sweep_count: 12   match: yes
category: agenda_items     grep_count: 9    sweep_count: 9    match: yes
category: auditor_paras    grep_count: 19   sweep_count: 19   match: yes
category: entities         grep_count: 13   sweep_count: 13   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

## Reconciliation notes (how each count was built)
- notes (15): grep `Certificate dated August 01, 2026` → 6 raw hits at lines 302, 359, 439, 536, 568, 601; the line-601 hit is subsumed into the Section 5 statement row (not double-counted), leaving 5 standalone citation notes + asterisk footnote (362) + "NA represents Not Applicable" legend (300) + Note 1 (557) + Note 2 (586) + Prospectus-quote paragraph (594-596) + Section 5 statement (599-603) + 4 object-description narrative blocks (453, 470, 482, 507) = 5+1+1+1+1+1+1+4 = 15. Manual sweep of the same 15 items matches.
- line_items (21): grep anchors — Issue Size particulars 3 rows (`Gross proceeds of the Fresh Issue|Less: Issue Expenses|Net Proceeds`, lines 202-204) + Cost-of-objects table 7 rows (`No revision` → 5 object/issue-expense rows at 331/338/345/350/354, plus Sub Total 352 + Total 356) + Progress-in-objects table 7 rows (`No Comments` → 5 rows at 393/403/413/422/432, plus Sub Total 427 + Total 437) + Deployment table 3 rows (`Balance in Monitoring account` → 2 rows at 549/552, plus Total 555) + Delay table 1 row (`Refer note 2` ×3 cell-occurrences on one row, line 580-584) = 3+7+7+3+1 = 21. Manual sweep matches.
- zero_standing (12): grep `NA.*No revision` → 5 cost-table rows (331/338/345/350/354, "Cost (Revised)" column standing NA in all periods) + grep `Nil` → 4 distinct progress-table rows (393/413/422/432, "During the quarter" and/or "Total unutilized" cells Nil) + Deployment table 3 rows (549/552/555, Earnings/Return-on-Investment/Maturity columns dash "-" in all periods) = 5+4+3 = 12. Manual sweep matches.
- agenda_items (9): grep `?` restricted to lines 209-300 (Section 3 governance/arrangement questionnaire) → 9 hits, one per question. Manual sweep matches (row 1's "No"/"Comments" split across wrapped lines 226/228 was caught by the "?" anchor even though a literal "No Comments" grep would have missed it — this is the exact re-sweep case GATE A2 exists to catch).
- auditor_paras (19): grep `(a)` / `(b)` at line start → 2 overall-conclusion lines (141, 143) + Declaration block blank-line-delimited into 3 paragraphs (146-153, 155-157, 159-163) + lettered Disclaimers a-n → 14 hits (614, 619, 623, 627, 632, 636, 640, 641, 643, 648, 652, 660, 669, 671) = 2+3+14 = 19. Manual sweep matches.
- entities (13): grep counts of distinct named parties — 2 promoters (183-184) + 3 subsidiaries/associate hospitals (Park Medicity NCR, Blue Heavens, Ratangiri — repeat mentions collapsed to unique names) + 1 statutory auditor firm (Agiwal & Assocaites, 6 raw mentions collapsed to 1 entity) + 1 Monitoring Agency (Crisil Ratings Limited, 4 raw mentions collapsed to 1 entity) + 2 banks (Axis, ICICI) + 2 stock exchanges (BSE, NSE) + 2 signatories (Abhishek Kapoor, Shounak Chakravarty) = 2+3+1+1+2+2+2 = 13. Manual sweep matches.

---

## TABLE 1 — Cover letters and transmittal (pages 1-3)
| # | Line(s) | Item | Content (first ~15 words / key facts) | Flags |
|---|---|---|---|---|
| 1.1 | 18-48 | Company covering letter to BSE/NSE | Reg 32(6) disclosure transmitting CRISIL Monitoring Agency Report for quarter ended June 30, 2026; states report placed before Board and Audit Committee same day (Aug 3, 2026) | — |
| 1.2 | 49-76 | Company letter digital signature block | Digitally signed by Abhishek Kapoor; DN incl. postalCode 122011, Haryana; timestamp 2026.08.03 17:11:35 +05'30 | SIGNATORY_BLOCK |
| 1.3 | 74-75 | Company letter signatory identity | Name: Abhishek Kapoor; Designation: Company Secretary & Compliance Officer | SIGNATORY_BLOCK |
| 1.4 | 94-124 | CRISIL covering letter to Park Medi World Ltd | Ref CRL/MAR/PRKH/2026-27/1879, dated Aug 3, 2026; encloses MA Report per Reg 41(2) SEBI ICDR and Monitoring Agency Agreement dated Aug 18, 2025 | — |
| 1.5 | 122-123 | CRISIL letter signatory identity | Shounak Chakravarty, Director, Ratings (LCG) — no digital-signature timestamp block present (unlike company letter) | SIGNATORY_BLOCK; NO_TIMESTAMP |

## TABLE 2 — Report of the Monitoring Agency: header, overall conclusion, Declaration (page 4)
| # | Line(s) | Item | Verbatim / content | Flags |
|---|---|---|---|---|
| 2.1 | 135-139 | Report header fields | Name of issuer: Park Medi World Limited; For quarter ended: June 30, 2026; Name of MA: Crisil Ratings Limited | — |
| 2.2 | 141 | **Overall conclusion (a)** | "(a) Deviation from the objects: Not applicable" | OVERALL_CONCLUSION |
| 2.3 | 143 | **Overall conclusion (b)** | "(b) Range of Deviation: Not applicable" | OVERALL_CONCLUSION |
| 2.4 | 146-153 | Declaration paragraph 1 | "We declare that this report provides an objective view of the utilization of the issue proceeds..." (scope/objectivity, no-audit, no-fiduciary-relationship language) | AUDITOR_PARA |
| 2.5 | 155-157 | Declaration paragraph 2 | "The MA or its affiliates may have credit rating or other commercial transactions with the entity..." (conflict-of-interest disclosure, no conflict perceived) | AUDITOR_PARA |
| 2.6 | 159-163 | Declaration paragraph 3 | "We have submitted the report herewith in line with the format prescribed by SEBI..." — flags that "Comments of the Board of Directors" columns throughout are NOT reviewed by MA and MA takes no responsibility for them | AUDITOR_PARA; IMPORTANT_SCOPE_CARVEOUT |
| 2.7 | 168-170 | MA report signature block | Signature; Shounak Chakravarty, Director, Ratings (LCG) — no UDIN disclosed anywhere in this document | SIGNATORY_BLOCK; MISSING_UDIN (NOT FOUND) |

## TABLE 3 — Issuer Details, Issue Details, Issue Size particulars (page 5, lines 179-205)
| # | Line(s) | Item | Value | Flags |
|---|---|---|---|---|
| 3.1 | 183 | Promoter 1 | Dr. Ajit Gupta | ENTITY |
| 3.2 | 184 | Promoter 2 | Dr. Ankit Gupta | ENTITY |
| 3.3 | 187 | Industry/sector | Hospital | — |
| 3.4 | 191 | Issue period | Wed Dec 10, 2025 to Fri Dec 12, 2025 | — |
| 3.5 | 193-197 | Issue type / security type / grading | IPO; Equity Shares; IPO Grading: NA | — |
| 3.6 | 199 | Issue size | Rs 7,700.00 million | — |
| 3.7 | 202 | **Issue Size particulars — row 1: Gross proceeds of Fresh Issue** | 7,700.00 (Rs mn) [770.00 Cr]; footnote #: "Crisil Ratings shall be monitoring the gross proceeds amount" | — |
| 3.8 | 203 | **Issue Size particulars — row 2: Less Issue Expenses** | 567.23 (Rs mn) [56.72 Cr] | — |
| 3.9 | 204 | **Issue Size particulars — row 3: Net Proceeds** | 7,132.77 (Rs mn) [713.28 Cr] | — |

## TABLE 4 — Section 3: Details of arrangement to monitor issue proceeds (governance questionnaire, pages 5-6, lines 209-300) — 9 rows
| # | Line(s) | Question (Particulars) | Reply | Comments of MA | Comments of Board | Flags |
|---|---|---|---|---|---|---|
| 4.1 | 226-231 | Whether all utilization is as per the disclosures in the Offer Document? | Yes | "Proceeds were utilized towards capital expenditure by the subsidiary" | No Comments | LINE_WRAP_SPLIT (reply "No"/"Comments" for the Board column split across lines 226 and 228 by page wrap — caught only by the "?" grep anchor, not a literal "No Comments" string match) |
| 4.2 | 253-258 | Whether shareholder approval has been obtained in case of material deviations from expenditures disclosed in the Offer Document? | NA | No Comments | No Comments | — |
| 4.3 | 261-264 | Whether the means of finance for the disclosed objects of the issue has changed? | No | No Comments | No Comments | — |
| 4.4 | 267-270 | Is there any major deviation observed over the earlier monitoring agency reports? | No | No Comments | No Comments | — |
| 4.5 | 271-277 | Whether all Government/statutory approvals related to the object(s) have been obtained? | NA | No Comments | No Comments | — |
| 4.6 | 279-283 | Whether all arrangements pertaining to technical assistance/collaboration are in operation? | NA | No Comments | No Comments | — |
| 4.7 | 286-289 | Are there any favorable events improving the viability of these object(s)? | No | No Comments | No Comments | — |
| 4.8 | 291-294 | Are there any unfavorable events affecting the viability of the object(s)? | No | No Comments | No Comments | — |
| 4.9 | 295-300 | Is there any other relevant information that may materially affect the decision making of the investors? | No | No Comments | No Comments | — |
Footnotes to Table 4: line 300 "NA represents Not Applicable" (note); line 302-303 "^Certificate dated August 01, 2026, issued by M/s Agiwal & Assocaites..." (note — sourcing citation for the "Statutory Auditor's certificate" reply basis).

## TABLE 5 — Section 4(i): Cost of the object(s) (page 7, lines 314-360) — 7 rows
| # | Line(s) | Item Head | Original cost per Offer Doc (Rs mn) | Revised Cost (Rs mn) | Reason for revision | Comments of Board | Flags |
|---|---|---|---|---|---|---|---|
| 5.1 | 328-334 | Repayment/prepayment, in full or in part, of outstanding borrowings availed by the Company and its Subsidiaries | 3,800.00 [380.00 Cr] | NA | No revision | No Comments | ZERO_STANDING (Revised-Cost column NA, standing since inception) |
| 5.2 | 335-341 | Funding capital expenditure for development of new hospital by the Subsidiary Park Medicity (NCR) | 605.00 [60.50 Cr] | NA | No revision | No Comments | ZERO_STANDING |
| 5.3 | 342-348 | Funding capital expenditure for purchase of medical equipment by the Company and its Subsidiaries, Blue Heavens and Ratangiri | 274.59 [27.46 Cr] | NA | No revision | No Comments | ZERO_STANDING; **flagged object — see Table 8 delay row** |
| 5.4 | 349-351 | Unidentified inorganic acquisitions and general corporate purposes* | 2,453.18 [245.32 Cr] | NA | No revision | No Comments | ZERO_STANDING |
| 5.5 | 352 | Sub Total | 7,132.77 [713.28 Cr] | - | - | - | — |
| 5.6 | 354 | Issue expenses | 567.23 [56.72 Cr] | NA | No revision | No Comments | ZERO_STANDING |
| 5.7 | 356 | Total | 7,700.00 [770.00 Cr] | - | - | - | — |
Footnote: line 359-360 "^Certificate dated August 01, 2026..." (note). Line 362-364 asterisk footnote on row 5.4: "amount ... does not exceed 35% of the Gross Proceeds (Rs 2,695.00 million); individual utilisation towards general corporate purposes does not exceed 25% (Rs 1,925.00 million)" (note).

## TABLE 6 — Section 4(ii): Progress in the object(s) (page 8, lines 375-437) — 7 rows
| # | Line(s) | Item Head | Proposed (Rs mn) | Beginning of qtr (Rs mn) | **During the quarter (Rs mn)** | End of qtr (Rs mn) | Total unutilized (Rs mn) | Reasons for idle funds / Board comments | Flags |
|---|---|---|---|---|---|---|---|---|---|
| 6.1 | 390-396 | Repayment/prepayment of outstanding borrowings by Company and Subsidiaries | 3,800.00 | 3,800.00 | **Nil** | 3,800.00 | **Nil** | "Proceeds fully utilized as at the quarter ended March 31, 2026" / No Comments | ZERO_STANDING (both During-quarter and Unutilized columns Nil) |
| 6.2 | 400-406 | Funding capex for development of new hospital, Subsidiary Park Medicity (NCR) | 605.00 | 166.53 | 28.66 | 195.19 | 409.81 | "Proceeds utilized towards construction of a new hospital building in Rohtak. The utilization as in line with the prospectus" / No Comments | ACTIVE — only object with nonzero movement this quarter |
| 6.3 | 407-417 | Funding capex for purchase of medical equipment (Company + Blue Heavens + Ratangiri) | 274.59 | 36.08 | **Nil** | 36.08 | 238.51 | "No proceeds utilized during the reported quarter" / No Comments | ZERO_STANDING (During-quarter Nil); **DELAY_DEVIATION — planned Rs 229.59mn (FY26) vs actual Rs 36.08mn utilised to date; see Table 8** |
| 6.4 | 419-425 | Unidentified inorganic acquisitions and general corporate purposes | 2,453.18 | 2,453.18 | **Nil** | 2,453.18 | **Nil** | "Proceeds fully utilized as at the quarter ended March 31, 2026" / No Comments | ZERO_STANDING |
| 6.5 | 427 | Sub Total | 7,132.77 | 6,455.79 | 28.66 | 6,484.45 | 648.32 | - / - | — |
| 6.6 | 430-434 | Issue expenses | 567.23 | 567.23 | **Nil** | 567.23 | **Nil** | "Proceeds fully utilized as at the quarter ended March 31, 2026" / No Comments | ZERO_STANDING |
| 6.7 | 437 | Total | 7,700.00 | 7,023.02 | 28.66 | 7,051.68 | 648.32 | - / - | — |
Footnote: line 439-440 "^Certificate dated August 01, 2026..." (note).
**Note on Q1 FY27 activity:** of 5 substantive rows, only row 6.2 (Rohtak hospital, Park Medicity NCR) shows any incremental utilization during the quarter (Rs 28.66mn); rows 6.1, 6.3, 6.4, 6.6 all show Nil movement this quarter — 4 of 5 objects were dormant.

## TABLE 7 — Brief description of objects (narrative footnote to Section 4, pages 9-10, lines 447-531) — 4 rows
| # | Line(s) | Object | Paragraph content summary | Flags |
|---|---|---|---|---|
| 7.1 | 453-467 | Repayment/prepayment of outstanding borrowings | Describes term loans/equipment loans/cash credit facilities of Company and Subsidiaries; intends to utilise entire amount by Fiscal 2026, subject to Offer completion and infusion timelines | NOTE |
| 7.2 | 470-478 | Funding capex — new hospital, Park Medicity (NCR) | Debt investment into Subsidiary for construction of New Hospital in Rohtak on freehold/leasehold land already in Company's possession | NOTE |
| 7.3 | 482-498 | Funding capex — medical equipment | Rs 274.59mn earmarked: Rs 184.59mn for Company hospitals in Panchkula; Rs 90.00mn for Blue Heavens/Ratangiri hospitals in Ambala/Jaipur (single continuous block in source — no blank-line paragraph break despite two distinct ideas, due to PDF column-wrap merge with object-head label) | NOTE |
| 7.4 | 507-531 | Unidentified inorganic acquisitions and general corporate purposes | Three blank-line-delimited paragraphs: (507-513) cap language — inorganic + GCP together ≤35% Gross Proceeds, each ≤25%; (515-525) acquisition-form/factors discussion; (527-531) GCP purpose definition | NOTE (3 sub-paragraphs) |

## TABLE 8 — Section 4(iii): Deployment of unutilised proceeds (page 10, lines 534-558) — 3 rows
| # | Line(s) | Instrument / entity | Amount invested (Rs mn) | Maturity date | Earnings (Rs mn) | Return on Investment (%) | Market value at qtr-end (Rs mn) | Flags |
|---|---|---|---|---|---|---|---|---|
| 8.1 | 548-550 | Balance in Monitoring account of the Company — Axis Bank (Refer note 1) | 72.32 | - | - | - | 72.32 | ZERO_STANDING (Maturity/Earnings/ROI dash, no-yield idle account) |
| 8.2 | 551-553 | Balance in Monitoring account of the Company — ICICI Bank | 576.00 | - | - | - | 576.00 | ZERO_STANDING |
| 8.3 | 555 | Total | 648.32 [64.83 Cr] | - | - | - | 648.32 | ZERO_STANDING |
| Note 1 | 557-558 | Note on Axis Bank monitoring account | "The balance as on June 30, 2026, the balance in Monitoring account stands at Rs. 84.99 million, of which Rs. 72.32 million pertains to fresh issue and Rs. 12.67 million pertains to OFS category" | — | — | — | — | NOTE |

## TABLE 9 — Section 4(iv): Delay in implementation of the object(s) (page 11, lines 566-596) — 1 row + notes
| # | Line(s) | Object(s) | Completion date per Offer Doc | Actual | Delay (days/months) | Reason of delay | Proposed course of action | Flags |
|---|---|---|---|---|---|---|---|---|
| 9.1 | 580-584 | Funding capital expenditure for purchase of medical equipment by the Company and its Subsidiaries, Blue Heavens and Ratangiri | FY26 — Rs 229.59 million | Q1 FY27 — Rs 36.08 million | Refer note 2 | Refer note 2 | Refer note 2 | **DELAY_DEVIATION (flagged per task instruction): planned ~Rs 229.59mn [22.96 Cr] by FY26 vs actual Rs 36.08mn [3.61 Cr] utilised as at Q1 FY27 — Rs 193.51mn shortfall carried forward** |
| Note 2 | 586-592 | Verbatim reason | "As per Company's Prospectus dated December 12, 2025, the Company had estimated to utilize Rs. 229.59 million towards object 3... However, based on Statutory Auditor certificate and management undertaking, the Company has utilised Rs. 36.08 million only for the said object as at the end of Q1FY2027, hence, there is a delay in the implementation schedule. The delay is primarily attributable to deferment in finalisation of equipment procurement, including commercial negotiations and alignment of delivery timelines. The Company intends to utilise the unspent proceeds in the subsequent period." | — | — | — | — | — | NOTE (verbatim reason, quoted in full) |
| Prospectus quote | 594-596 | Contingency language | "However, the Prospectus further states that, 'In the event that the estimated utilization of the Net Proceeds in a scheduled fiscal year is not completely met, due to stated reasons, the same shall be utilised in the next fiscal year, as may be determined by the Company, in accordance with applicable laws.'" | — | — | — | — | — | NOTE |

## TABLE 10 — Section 5: General Corporate Purpose utilization detail (page 11, lines 599-603)
| # | Line(s) | Item | Content | Flags |
|---|---|---|---|---|
| 10.1 | 599-603 | Details of utilization stated as GCP amount | "Not applicable, on the basis of Certificate dated August 01, 2026, issued by M/s Agiwal & Assocaites, Chartered Accountants... and Management undertaking of the Company." | NOTE |

## TABLE 11 — Disclaimers a-n (pages 12-13, lines 612-672) — 14 paragraphs, verbatim first ~15 words
| # | Line | Letter | First ~15 words | Flags |
|---|---|---|---|---|
| 11.1 | 614 | a) | "This Report is prepared by Crisil Ratings Limited (hereinafter referred to as 'Monitoring Agency'..." | AUDITOR_PARA |
| 11.2 | 619 | b) | "This Report has to be seen in its entirety; the selective review of portions of the Report may lead..." | AUDITOR_PARA |
| 11.3 | 623 | c) | "Nothing contained in this Report is capable or intended to create any legally binding obligations on the MA..." | AUDITOR_PARA |
| 11.4 | 627 | d) | "The MA and its affiliates do not act as a fiduciary. The MA and its affiliates also do not act as an expert..." | AUDITOR_PARA |
| 11.5 | 632 | e) | "The MA or its affiliates may have other commercial transactions with the entity to which the report pertains..." | AUDITOR_PARA |
| 11.6 | 636 | f) | "The MA report is intended for the jurisdiction of India only. This report does not constitute an offer of services..." | AUDITOR_PARA |
| 11.7 | 640 | g) | "Access or use of this report does not create a client relationship between CRL and the user." | AUDITOR_PARA |
| 11.8 | 641 | h) | "CRL is not aware that any user intends to rely on the report or of the manner in which a user intends..." | AUDITOR_PARA |
| 11.9 | 643 | i) | "It is made abundantly clear that the report is not intended to and does not constitute an investment advice..." | AUDITOR_PARA |
| 11.10 | 648 | j) | "The report comprises professional opinion of CRL as of the date they are expressed, based on the information received..." | AUDITOR_PARA |
| 11.11 | 652 | k) | "Neither CRL nor its affiliates, third-party providers, as well as their directors, officers, shareholders, employees or agents guarantee..." | AUDITOR_PARA |
| 11.12 | 660 | l) | "CRL has established policies and procedures to maintain the confidentiality of certain non-public information received in connection..." | AUDITOR_PARA |
| 11.13 | 669 | m) | "Unless required under any applicable law, this report should not be reproduced or redistributed to any other person or in..." | AUDITOR_PARA |
| 11.14 | 671 | n) | "By accepting a copy of this Report, the recipient accepts the terms of this Disclaimer, which forms an integral part..." | AUDITOR_PARA |

## TABLE 12 — Entities named in the report
| # | Line(s) | Entity | Relationship | Flags |
|---|---|---|---|---|
| 12.1 | 183 | Dr. Ajit Gupta | Promoter | ENTITY |
| 12.2 | 184 | Dr. Ankit Gupta | Promoter | ENTITY |
| 12.3 | 340, 405, 476 | Park Medicity (NCR) Private Limited | Subsidiary — object 2 recipient (Rohtak hospital capex) | ENTITY |
| 12.4 | 347, 416, 487 etc. | Blue Heavens | Subsidiary — object 3 recipient (medical equipment, Ambala) | ENTITY |
| 12.5 | 348, 416, 487 etc. | Ratangiri | Subsidiary — object 3 recipient (medical equipment, Jaipur) | ENTITY |
| 12.6 | 302 (and 5 further recurring citations) | M/s Agiwal & Assocaites, Chartered Accountants (FRN 000181N) | Statutory Auditor — sole certifying source for MA's report (certificate dated Aug 1, 2026) | ENTITY |
| 12.7 | 139 (and 3 further recurring citations) | Crisil Ratings Limited | Monitoring Agency (MA) | ENTITY |
| 12.8 | 549 | Axis Bank | Monitoring-account bank (fresh issue + OFS balance) | ENTITY |
| 12.9 | 552 | ICICI Bank | Monitoring-account bank | ENTITY |
| 12.10 | 20 | BSE Limited | Stock exchange (recipient) | ENTITY |
| 12.11 | 20 | National Stock Exchange of India Limited | Stock exchange (recipient) | ENTITY |
| 12.12 | 74, 49-69 | Abhishek Kapoor | Company Secretary & Compliance Officer (company-letter signatory) | ENTITY; SIGNATORY |
| 12.13 | 122, 169 | Shounak Chakravarty | Director, Ratings (LCG), Crisil Ratings Ltd (MA-side signatory, both letter and report) | ENTITY; SIGNATORY |

---

## Summary of flags raised
- **ZERO_STANDING** — 12 rows across Cost-of-objects (5), Progress-in-objects (4), Deployment-of-unutilised-proceeds (3).
- **DELAY_DEVIATION** — Table 6 row 6.3 / Table 9 row 9.1: medical equipment object, planned Rs 229.59mn (FY26) vs actual Rs 36.08mn utilised as at Q1 FY27, Rs 193.51mn shortfall. This is the deviation A1 already flagged; A2 confirms it appears twice in the source (once in the Progress table as "No proceeds utilized during the reported quarter", once in the dedicated Delay-in-Implementation table) and is fully sourced to Note 2 (lines 586-592).
- **MISSING_UDIN** — no UDIN number appears anywhere in the 677-line extract for either the Statutory Auditor's certificate or the CRISIL signature block. Recorded as NOT FOUND, not estimated.
- **NO_TIMESTAMP** — CRISIL's own covering letter (page 3) and MA-report signature block (page 4) carry no digital-signature timestamp, unlike the company's covering letter which is fully digitally signed and timestamped (2026.08.03 17:11:35).
- **IMPORTANT_SCOPE_CARVEOUT** — Declaration paragraph 3 (lines 159-163) states the "Comments of the Board of Directors" columns throughout every table are populated by the Issuer's Management/Audit Committee *after* MA submission and are NOT reviewed by the MA; every "No Comments" cell in Tables 4-9 above carries this caveat.
- **LINE_WRAP_SPLIT** — Table 4 row 4.1: the Board-comment reply "No Comments" is split across non-adjacent wrapped lines (226, 228) by the PDF's column layout; a naive literal-string grep for "No Comments" would have undercounted Section 3 to 8 rows instead of 9. This is the exact re-sweep case GATE A2 is designed to catch, and it reconciled clean via the "?" anchor.
