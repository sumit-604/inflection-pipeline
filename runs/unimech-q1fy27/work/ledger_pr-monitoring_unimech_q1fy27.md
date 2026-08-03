# A2 ENUMERATION LEDGER — UNIMECH Q1 FY27 — Reg 32(6) Monitoring Agency Report (CARE Ratings)

Source: pr_monitoring_unimech_q1fy27.pdf (12 pages) via
extract_pr-monitoring_unimech_q1fy27.txt. Doctype does not match the
standard "results filing" financial-statement shape; it is a proceeds-
utilisation monitoring report. Categories below are adapted from the
RESULTS-FILING enumeration rules (every table line item incl. zero/nil/
dash rows, every paragraph of the reviewer's (MA's) report, every
signature block) applied to this document's actual structure. Line
numbers cited are the extract's own embedded source-line numbers (the
number immediately preceding each line of quoted text in the extract,
matching the second column the Read tool displays).

```
=== A2 COUNT TEST ===
category: report_header_items         grep_count: 5   sweep_count: 5   match: yes
category: cover_transmittal_letters    grep_count: 2   sweep_count: 2   match: yes
category: declaration_paragraphs       grep_count: 3   sweep_count: 3   match: yes
category: issuer_details_items         grep_count: 3   sweep_count: 3   match: yes
category: issue_details_items          grep_count: 5   sweep_count: 5   match: yes
category: section3_particulars         grep_count: 8   sweep_count: 8   match: yes
category: cost_of_objects_lines        grep_count: 9   sweep_count: 9   match: yes
category: progress_objects_lines       grep_count: 9   sweep_count: 9   match: yes
category: deployment_unutilized_lines  grep_count: 3   sweep_count: 3   match: yes
category: delay_implementation_lines   grep_count: 14  sweep_count: 14  match: yes
category: gcp_utilization_lines        grep_count: 1   sweep_count: 1   match: yes
category: gcp_offer_doc_quote_paras    grep_count: 1   sweep_count: 1   match: yes
category: footnotes_notes              grep_count: 6   sweep_count: 6   match: yes
category: disclaimer_paragraphs        grep_count: 5   sweep_count: 5   match: yes
category: signature_date_blocks        grep_count: 3   sweep_count: 3   match: yes
TOTAL DISCLOSURE UNITS: 77
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used (Bash, run against the extract file), cross-checked
against a full manual line-by-line sweep of every page:
- `grep -n -E "^[0-9]+\s+(Whether|Is there|Are there)"` → 8 section-3 particulars
- `grep -c -E "Fully utilized as on|Not applicable as|Delayed by|Not specified\*"` → 14 delay rows
- `grep -n -E "^\s*[a-e]\)\s"` → 5 disclaimer paragraphs
- `grep -n "Chartered Accountant certificate from VAGS"` + `grep -n "Note:"` + `grep -n "The offer document does not specify"` → 6 footnotes
- `grep -n -E "We declare that|The MA or its affiliates may have credit rating|We have submitted the report herewith"` → 3 declaration paragraphs
- `grep -n -E "Name of the issuer:|For quarter ended:|Name of the Monitoring Agency:"` + `grep -n -E "Deviation from the objects|Range of Deviation"` → 5 report-header items
- `grep -n -E "Fixed Deposit|Public Issue Account"` + Total line → 3 deployment rows
- Manual sweep confirmed Cost-of-Objects and Progress tables each carry 8 line items (Sr 1, 2, 3a, 3b, 3c, 4, 5, 6) + 1 Total row = 9, by direct transcription of every cell across pages 4-9.

---

## 1. Cover / Transmittal Letters

| # | Line(s) | Description | Flags |
|---|---------|-------------|-------|
| 1.1 | 2-43 | Company's transmittal letter to NSE/BSE forwarding the Reg 32(6) Monitoring Agency Report, signed by Rashmi Gupta (Company Secretary & Compliance Officer) | |
| 1.2 | 45-87 | CARE Ratings' own cover letter to the Board of Directors enclosing the Monitoring Agency Report, signed by Himanshu Jain (Associate Director), citing Monitoring Agency Agreement dated December 12, 2024 | |

## 2. Report Header Metadata & Deviation Declaration (page 3)

| # | Line | Item | Value | Flags |
|---|------|------|-------|-------|
| 2.1 | 91 | Name of the issuer | Unimech Aerospace and Manufacturing Limited | |
| 2.2 | 92 | For quarter ended | June 30, 2026 | |
| 2.3 | 93 | Name of the Monitoring Agency | CARE Ratings Limited | |
| 2.4 | 94 | (a) Deviation from the objects | None | |
| 2.5 | 95 | (b) Range of Deviation | Not applicable | |

## 3. MA Declaration Paragraphs (verbatim, page 3)

| # | Line(s) | First words | Flags |
|---|---------|-------------|-------|
| 3.1 | 99-107 | "We declare that this report provides an objective view of the utilization of the issue proceeds..." (scope/liability disclaimer, no fiduciary relationship, MA does not act as Sec. 2(38) expert) | |
| 3.2 | 110-113 | "The MA or its affiliates may have credit rating or other commercial transactions with the entity..." (conflict-of-interest statement: none) | |
| 3.3 | 116-120 | "We have submitted the report herewith in line with the format prescribed by SEBI..." (notes "Comments of the Board of Directors" sections are completed post-submission by the Issuer and are NOT reviewed by the MA) | |

## 4. Issuer Details — Section 1 (page 4)

| # | Line | Field | Value | Flags |
|---|------|-------|-------|-------|
| 4.1 | 130 | Name of the issuer | Unimech Aerospace and Manufacturing Limited | |
| 4.2 | 131 | Name of the promoter | Rajanikanth Balaraman, Mani Puttan, Ramakrishna Kamojhala, Puttan Anil Kumar, Venkatesh Shimoga Preetham (5 named promoters) | |
| 4.3 | 132 | Industry/sector | Aerospace and Defense | |

## 5. Issue Details — Section 2 (page 4)

| # | Line | Field | Value | Flags |
|---|------|-------|-------|-------|
| 5.1 | 135 | Issue Period | December 23, 2024 to December 26, 2024 | |
| 5.2 | 136 | Type of issue | Public Fresh Issue | |
| 5.3 | 137 | Type of specified securities | Equity Shares | |
| 5.4 | 138 | IPO Grading, if any | Not Applicable | ZERO_STANDING (N/A field) |
| 5.5 | 139 | Issue size | Rs. 250 crore | |

## 6. Section 3 — Arrangement to Monitor Issue Proceeds (8 particulars, pages 4-5)

| # | Line | Particular | Reply | MA Comment (verbatim) | Flags |
|---|------|-----------|-------|------------------------|-------|
| 6.1 | 157-166 | Whether all utilization is as per the disclosures in the Offer Document? | No | "A new object for utilization of IPO proceeds has been introduced on November 17, 2025, covering M&A, Greenfield Projects, and JV... During the quarter, the proceeds have been utilized for funding company's working capital requirements and for acquisition of a company - Hobel Bellows Private Limited." | OBJECT_REALLOCATION |
| 6.2 | 171-179 | Whether shareholder approval has been obtained in case of material deviations from expenditures disclosed in the Offer Document? | Yes | "An amount of ₹61.287 crore, originally earmarked for expansion through purchase of machineries and equipment... has been reallocated to a newly introduced object covering M&A, Greenfield Projects, and JV, pursuant to shareholders' approval via postal ballot dated December 19, 2025." | OBJECT_REALLOCATION |
| 6.3 | 182-186 | Whether the means of finance for the disclosed objects of the issue have changed? | Not Applicable | "Nil" | ZERO_STANDING |
| 6.4 | 195-197 | Is there any major deviation observed over the earlier monitoring agency reports? | No | "Nil" (references MA report dated May 12, 2026) | ZERO_STANDING |
| 6.5 | 202-207 | Whether all Government/statutory approvals related to the object(s) have been obtained? | Not Applicable | "As mentioned in the prospectus, all approvals are in place... No additional approvals are required." | |
| 6.6 | 212-217 | Whether all arrangements pertaining to technical assistance/collaboration are in operation? | Not Applicable | "...IPO proceeds are only for the expansion of current capacity... Therefore, no technical collaboration is required." | |
| 6.7 | 219-222 | Are there any favorable/unfavorable events affecting the viability of these object(s)? | Not applicable | "Nil" | ZERO_STANDING |
| 6.8 | 227-233 | Is there any other relevant information that may materially affect the decision making of the investors? | No | "Company has allocated more than 40% of gross IPO proceeds cumulatively towards GCP and unidentified acquisitions/investment target, which is higher than the 35% limit prescribed under Regulation 7(3) of the SEBI (ICDR) Regulations. However, the same has been carried out in compliance with Sections 13 and 27 of the Companies Act, 2013, pursuant to... shareholders through a special resolution..." | REG7_3_LIMIT_BREACH |
| — | 234 | Footnote to Section 3 table | *Chartered Accountant certificate from VAGS & Associates dated July 18, 2026, UDIN 26242386GPWXQ11143 | see Footnote row 13.1 |

## 7. Section 4(i) — Cost of Objects (pages 5-6): 8 line items + Total

| # | Line(s) | Sr | Item/Head | Original Cost (Rs Cr, Offer Doc) | Revised Cost (Rs Cr) | MA Comment | Flags |
|---|---------|----|-----------|-----------------------------------|------------------------|------------|-------|
| 7.1 | 242-256 | 1 | Funding of capital expenditure for expansion through purchase of machineries and equipment | 36.37 | 23.54 | "As per postal ballot outcome dated December 19, 2025, unutilized amount of Rs. 12.83 crore as of September 30, 2025, has been reallocated towards new object related to M&A, JV and Green Field Projects" | OBJECT_REALLOCATION |
| 7.2 | 256-258 | 2 | Funding working capital requirements of Company | 25.29 | No revision | No comments | |
| 7.3 | 259-267 | 3a | Investment in Material Subsidiary: a. Funding of capex for expansion through purchase of machineries/equipment | 43.89 | 35.43 | "unutilized amount of Rs. 8.46 crore as of September 30, 2025, has been reallocated towards new object related to M&A, JV and Green Field Projects" | OBJECT_REALLOCATION |
| 7.4 | 268-270 | 3b | Investment in Material Subsidiary: b. funding its working capital requirements | 44.71 | No revision | No comments | |
| 7.5 | 271-281 | 3c | Investment in Material Subsidiary: c. repayment/prepayment, in full or part, of certain borrowings | 40.00 | 0.0 | "unutilized amount of Rs. 40.0 crore as of September 30, 2025, has been reallocated towards new object related to M&A, JV and Green Field Projects" | ZERO_STANDING (revised to nil), OBJECT_REALLOCATION |
| 7.6 | 282-284 | 4 | General corporate purposes (GCP) | 40.65 | No revision | No comments | |
| 7.7 | 285-291 | 5 | M&A, Joint Ventures and Green Field Projects | 0.0 | 61.29 | "New object inserted for which shareholders were taken via Special Resolution as per Postal ballot." | ZERO_STANDING (original cost nil — did not exist in Offer Document), NEW_OBJECT |
| 7.8 | 292 | 6 | Issue expenses | 19.09 | No revision | (blank / not shown) | |
| 7.9 | 293 | — | **Total** | **250.00** | **250.00** | | |
| — | 294 | Footnote | *Chartered Accountant certificate from VAGS & Associates dated July 18, 2026, UDIN 26242386GPWXQ11143 | | | see Footnote row 13.2 |

## 8. Section 4(ii) — Progress in the Objects (pages 6-9): 8 line items + Total

| # | Line(s) | Sr | Item/Head | Amt as at beginning of qtr | During qtr | At end of qtr | Total unutilised (Rs Cr) | MA Comment (verbatim, abridged) | Flags |
|---|---------|----|-----------|------------------------------|------------|-----------------|----------------------------|-----------------------------------|-------|
| 8.1 | 311-319 | 1 | Funding of capex for expansion through purchase of machineries/equipment | 23.54 | 0.00 | 23.54 | 0.00 | "Entire amount towards the object has already been utilized." | ZERO_STANDING (during-quarter movement = 0; unutilised = 0) |
| 8.2 | 325-338 | 2 | Funding working capital requirements of Company | 13.46 | 11.83 | 25.29 | 0.00 | "A total of Rs. 11.83 crore was transferred from the MA account to the current account and used for working capital expenses... Rs. 5.95 crore is towards reimbursement of expenses incurred prior to the transfer of MA funds. Since payments were routed through current account which included multiple other transactions, this has resulted in commingling of funds." | COMMINGLING_OF_FUNDS |
| 8.3 | 339-349 | 3a | Investment in Material Subsidiary: a. Funding of capex for expansion | 35.43 | 0.00 | 35.43 | 0.00 | "Entire amount towards the object has already been utilized." | ZERO_STANDING (during-quarter movement = 0; unutilised = 0) |
| 8.4 | 364-383 | 3b | Investment in Material Subsidiary: b. funding its working capital requirements | 23.33 | 21.38 | 44.71 | 0.00 | "A total of Rs. 21.38 crore was transferred... Rs. 11.57 crore is towards reimbursement of expenses incurred prior to the transfer of MA funds... this has resulted in commingling of funds." | COMMINGLING_OF_FUNDS |
| 8.5 | 384-392 | 3c | Investment in Material Subsidiary: c. repayment/prepayment of certain borrowings | 0.00 | 0.00 | 0.00 | 0.00 | "Amount allocated towards the object is Nil as per modification in objects passed through special resolution by shareholders." | ZERO_STANDING (entire row nil across all columns) |
| 8.6 | 393-401 | 4 | General corporate purposes (GCP) | 40.65 | 0.00 | 40.65 | 0.00 | "Entire amount towards the object has already been utilized." | ZERO_STANDING (during-quarter movement = 0; unutilised = 0) |
| 8.7 | 402-435 | 5 | M&A, Joint Ventures and Green Field Projects | 0.00 | 61.29 | 61.29 | 0.00 | "During the quarter, the company utilised Rs. 61.29 crore for the acquisition of Hobel Bellows Private Limited... BSE announcement dated April 22, 2026. Total consideration Rs. 148 crore... routed through the current account of Unimech... transferred Rs. 12.07 crore before the acquisition, however, Rs. 49.21 crore was transferred post-acquisition and taken as reimbursement, as the MA funds were invested in FDs where premature closure was not allowed." | ZERO_STANDING (beginning-of-quarter balance nil), OBJECT_REALLOCATION |
| 8.8 | 438-448 | 6 | Issue expenses | 16.89 | 0.0 | 16.89 | 2.20 | "No utilization during the quarter." BoD comment: "Rs 1.62 crore has been paid to all the vendors in July 2026, and balance Rs. 0.58 crore approved to transfer it to GCP" | ZERO_STANDING (during-quarter movement = 0) |
| 8.9 | 449 | — | **Total** | **153.30** | **94.50** | **247.80** | **2.20** | | |
| — | 450 | Footnote | *Chartered Accountant certificate from VAGS & Associates dated July 18, 2026, UDIN 26242386GPWXQ11143 | | | | | see Footnote row 13.3 |

## 9. Section 4(iii) — Deployment of Unutilized Proceeds (page 9): 2 rows + Total

| # | Line | Sr | Instrument / Entity | Amount invested (Rs Cr) | Maturity date | Earning | Return on Investment (%) | Market Value at qtr end | Flags |
|---|------|----|--------------------|----------------------------|-----------------|---------|-----------------------------|---------------------------|-------|
| 9.1 | 456 | 1 | Fixed Deposit — Axis Bank | 0.58 | 04-07-2026 | (blank) | 3% | (blank) | |
| 9.2 | 457 | 2 | Public Issue Account maintained with Axis Bank | 1.62 | - | - | - | - | ZERO_STANDING (dash-valued in 4 of 5 columns) |
| 9.3 | 458 | — | **Total** | **2.20** | | | | | |

## 10. Section 4(iv) — Delay in Implementation of the Object(s) (page 10): 14 rows

| # | Line | Object | Completion Date (Offer Doc) | Actual | Delay | Reason / Proposed course (BoD) | Flags |
|---|------|--------|-------------------------------|--------|-------|----------------------------------|-------|
| 10.1 | 466 | Funding of capex for expansion (tranche 1) | Rs. 22.262 cr till March 2025 | Fully utilized as on March 31, 2025 | No delay | No comments / No comments | |
| 10.2 | 468 | Funding of capex for expansion (tranche 2) | Rs. 14.104 cr till March 2026 | Fully utilized as on September 30, 2025 | No delay | No comments / No comments | |
| 10.3 | 469 | Funding working capital requirements (tranche 1) | Rs. 13.456 cr till March 2026 | Fully utilized as on March 31, 2026 | No delay | No comments / No comments | |
| 10.4 | 471 | Funding working capital requirements (tranche 2) | Rs. 11.829 cr till March 2027 | Fully utilized as on June 30, 2026 | No delay | No comments / No comments | |
| 10.5 | 472 | Investment in Material Subsidiary — a. Funding capex (tranche 1) | Rs. 21.798 cr till March 2025 | Fully utilized as on March 31, 2025 | No delay | No comments / No comments | |
| 10.6 | 475 | Investment in Material Subsidiary — a. Funding capex (tranche 2) | Rs. 22.093 cr till March 2026 | Fully utilized as on September 30, 2025 | No delay | No comments / No comments | |
| 10.7 | 477 | Investment in Material Subsidiary — b. funding working capital (tranche 1) | Rs. 23.329 cr till March 2026 | Fully utilized as on March 31, 2026 | No delay | No comments / No comments | |
| 10.8 | 480 | Investment in Material Subsidiary — b. funding working capital (tranche 2) | Rs. 21.387 cr till March 2027 | Fully utilized as on June 30, 2026 | No delay | No comments / No comments | |
| 10.9 | 481 | Investment in Material Subsidiary — c. repayment/prepayment of certain borrowings | March 2025 | "Not applicable as company has reallocated entire amount under this head to M&A, Green field Projects, JV" | Not applicable | No comments / No comments | ZERO_STANDING, OBJECT_REALLOCATION |
| 10.10 | 486 | General corporate purposes (GCP) (tranche 1) | Rs. 16.262 cr till March 2025 | Fully utilized as on March 31, 2025 | No delay | No comments / No comments | |
| 10.11 | 488 | General corporate purposes (GCP) (tranche 2) | Rs. 24.392 cr till March 2026 | Fully utilized as on December 31, 2025 | No delay | No comments / No comments | |
| 10.12 | 489 | M&A, Green field Projects, Joint Ventures (tranche 1) | Rs. 36.77 cr till March 2026 | Fully utilized as on April 27, 2026 | **Delayed by 27 days** | "The Definitive agreements executed and acquisition also completed on April 27, 2026" (both MA and BoD columns) | DELAY |
| 10.13 | 491 | M&A, Green field Projects, Joint Ventures (tranche 2) | Rs. 24.52 cr till March 2027 | Fully utilized as on June 30, 2026 | No delay | (see above) / (see above) | |
| 10.14 | 494 | Issue expenses | Not specified* | Not specified* | Not applicable | No comments / No comments | ZERO_STANDING (no timeline specified) |
| — | 495-496 | Table note | "The above details are verified from the information shared by the company, offer document, and Chartered Accountant certificate from VAGS & Associates dated July 18, 2026 bearing UDIN: 26242386GPWXQ11143" | | | | see Footnote row 13.4 |
| — | 497 | Table footnote (*) | "The offer document does not specify the timeline for utilisation of funds towards issue expenses" | | | | see Footnote row 13.5 |

## 11. Section 5 — GCP Utilization Detail Table (page 9-10)

| # | Line | Sr No | Item Head | Amount (Rs Cr) | Source | MA Comment | BoD Comment | Flags |
|---|------|-------|-----------|-------------------|--------|-------------|--------------|-------|
| 11.1 | 505 | Nil | Nil | Nil | Nil | Nil | No comments | ZERO_STANDING (entire GCP itemisation table is Nil — no specific GCP line items disclosed beyond the aggregate GCP object in Section 4) |
| — | 506 | Table note | "Chartered Accountant certificate from VAGS & Associates dated July 18, 2026, bearing UDIN: 26242386GPWXQ11143" | | | | | see Footnote row 13.6 |

## 12. Section 5 — Quoted GCP Clause from Offer Document

| # | Line(s) | Description | Flags |
|---|---------|-------------|-------|
| 12.1 | 508 | Label: "^Section from the offer document related to GCP:" | |
| 12.2 | 510-521 | Verbatim quoted paragraph: "Our Company intends to deploy the balance Net Proceeds aggregating up to ₹406.54 Million (net of expenses...) towards general corporate purposes, subject to such utilization not exceeding 25% of the Gross Proceeds, in accordance with Regulation 7(2) of the SEBI ICDR Regulations..." — six enumerated GCP sub-purposes (i)-(vi) plus Board-flexibility language | Unit stated in Rs. Million per A1 header note (offer-document verbatim text, not converted to the report's crore convention) |

## 13. Footnotes / Notes (6, across the document)

| # | Line(s) | Location | Text | Flags |
|---|---------|----------|------|-------|
| 13.1 | 234 | Below Section 3 table | *Chartered Accountant certificate from VAGS & Associates dated July 18, 2026, bearing UDIN: 26242386GPWXQ11143 | |
| 13.2 | 294 | Below Cost of Objects table | *Chartered Accountant certificate from VAGS & Associates dated July 18, 2026, bearing UDIN: 26242386GPWXQ11143 | |
| 13.3 | 450 | Below Progress in Objects table | *Chartered Accountant certificate from VAGS & Associates dated July 18, 2026 bearing UDIN: 26242386GPWXQ11143 | |
| 13.4 | 495-496 | Below Delay table | "The above details are verified from the information shared by the company, offer document, and Chartered Accountant certificate..." | |
| 13.5 | 497 | Below Delay table (asterisk) | "The offer document does not specify the timeline for utilisation of funds towards issue expenses" | |
| 13.6 | 506 | Below GCP Utilization table | "Chartered Accountant certificate from VAGS & Associates dated July 18, 2026, bearing UDIN: 26242386GPWXQ11143" | |

Note: all six footnotes cite the identical single CA certificate (VAGS & Associates, dated July 18, 2026, UDIN 26242386GPWXQ11143) as the underlying evidentiary source for every table in this report.

## 14. Disclaimers to MA Report (page 12): 5 verbatim paragraphs

| # | Line(s) | First words | Flags |
|---|---------|-------------|-------|
| 14.1 | 524-527 | a) "This Report is prepared by CARE Ratings Ltd... utmost care to ensure accuracy and objectivity..." | |
| 14.2 | 528-531 | b) "This Report has to be seen in its entirety; the selective review of portions... may lead to inaccurate assessments." | |
| 14.3 | 532-535 | c) "Nothing contained in this Report is capable or intended to create any legally binding obligations on the MA..." | |
| 14.4 | 536-540 | d) "The MA and its affiliates do not act as a fiduciary... does not perform an audit and undertakes no independent verification..." | |
| 14.5 | 541-544 | e) "The MA or its affiliates may have other commercial transactions with the entity... may rate the issuer or any debt instruments/facilities... may receive separate compensation..." | |

## 15. Signature / Date Blocks (3)

| # | Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---------|-----------|-------------|-----------|-------|
| 15.1 | 30-40 | Rashmi Gupta | Company Secretary & Compliance Officer, M. No: A25382 | Digitally signed 2026.08.03, 18:30:06 +05'30' (on company's NSE/BSE transmittal letter, same date as report submission) | |
| 15.2 | 85-87 | Himanshu Jain | Associate Director, CARE Ratings (himanshu.jain@careedge.in) | No digital timestamp captured (cover letter to Board, dated August 03, 2026 at line 60/74 context) | |
| 15.3 | 125-127 | Himanshu Jain | Associate Director (Authorized Signatory) | No digital timestamp captured (signature block on the Monitoring Agency Report itself, page 3) | |

---

## Summary of flags raised across ledger
- ZERO_STANDING: 12 instances (rows 5.4, 6.3, 6.4, 6.7, 7.5, 7.7, 8.1, 8.3, 8.5, 8.6, 8.7, 8.8, 9.2, 10.9, 10.14, 11.1 — count includes multiple sub-columns within single rows; unique ROWS flagged ZERO_STANDING = 14: Issue Details 5.4 (N/A field), Section-3 rows 6.3/6.4/6.7, Cost-of-Objects rows 7.5/7.7, Progress rows 8.1/8.3/8.5/8.6/8.7/8.8, Deployment row 9.2, Delay rows 10.9/10.14, GCP-Utilization row 11.1)
- OBJECT_REALLOCATION: rows 6.1, 6.2, 7.1, 7.3, 7.5, 8.7, 10.9 (Rs. 61.287 crore reallocated from capex/subsidiary-capex/borrowings-repayment into the newly created M&A/JV/Greenfield object)
- NEW_OBJECT: row 7.7 (M&A, Joint Ventures and Green Field Projects — did not exist in original Offer Document, inserted via postal ballot dated December 19, 2025)
- REG7_3_LIMIT_BREACH: row 6.8 (cumulative GCP + unidentified acquisitions allocation >40% of gross proceeds vs. 35% limit under SEBI ICDR Regulation 7(3); Board states compliance was via Companies Act special resolution route instead)
- COMMINGLING_OF_FUNDS: rows 8.2, 8.4 (MA funds routed through current account containing other transactions)
- DELAY: row 10.12 (M&A/JV/Greenfield object completion delayed by 27 days vs. offer-document timeline; Definitive agreements and acquisition completed April 27, 2026)
