# A2 COMPLETENESS LEDGER — GAUDIUMIVF Q1FY27 Monitoring Agency Report
Source: extract_monitoring_gaudiumivf_q1fy27.txt (816 lines, 24 pages, Infomerics MA report, quarter ended June 30 2026)

```
=== A2 COUNT TEST ===
category: objects                       grep_count: 14  sweep_count: 14  match: yes
category: fund_utilization_table_rows   grep_count: 39  sweep_count: 39  match: yes
category: deployment_rows               grep_count: 6   sweep_count: 6   match: yes
category: gcp_subbreakdown              grep_count: 3   sweep_count: 3   match: yes
category: notes_footnotes               grep_count: 11  sweep_count: 11  match: yes
category: deviation_statements          grep_count: 6   sweep_count: 6   match: yes
category: auditor_certificate_refs      grep_count: 3   sweep_count: 3   match: yes
category: signature_blocks              grep_count: 2   sweep_count: 2   match: yes
category: declaration_paragraphs        grep_count: 3   sweep_count: 3   match: yes
category: disclaimer_paragraphs         grep_count: 14  sweep_count: 14  match: yes
category: cover_transmittal_items       grep_count: 2   sweep_count: 2   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Reconciliation note: grep passes used were (1) `grep -n "Note No\.|Note :|\*"` and `grep -n "\^"` for note/footnote
markers and bodies, (2) anchor-phrase greps for each object head (`Funding capital`, `Repayment or pre-`,
`General.*Corporate`, `Issue Expenses`) across all four object-bearing tables, (3) `grep -n "TOTAL"` for summary
rows, (4) `grep -n "HDFC Bank FD|HDFC Current|Axis Bank"` for deployment rows, (5) `grep -n "Advance Payment for
setting|TDS Payment|IPO Commission"` for the GCP sub-breakdown, (6) `grep -n "CA certificate|Certificate dated|S
K G N"` for auditor-certificate references, (7) `grep -c ""` (the Wingdings bullet glyph U+F0D8) for disclaimer
paragraphs, since these are not literal ASCII bullets — a first pass using `^\s{3,}[A-Z]` regex returned 0 because
pdftotext preserved the bullet as a private-use-area character, not whitespace; the python codepoint scan caught
it and reconciled the manual sweep (14) exactly. All eleven categories reconciled grep vs. manual sweep on first
re-sweep after the bullet-glyph correction; GATE A2 passes.

---

## 1. COVER / TRANSMITTAL ITEMS

| # | Item | Lines | Content (first ~15 words) | Flags |
|---|------|-------|---------------------------|-------|
| 1 | Company cover letter to BSE + NSE | 1-54 | "August 13, 2026 ... please find enclosed herewith the Monitoring Agency Report for the quarter ended June 30, 2026" | — |
| 2 | Infomerics forwarding letter to Company | 72-114 | "We write in our capacity of Monitoring Agency for the IPO amount aggregating to Rs.90.00 crore" | — |

## 2. SIGNATURE BLOCKS

| # | Signatory | Designation | Lines | Timestamp | Flags |
|---|-----------|-------------|-------|-----------|-------|
| 1 | Naveen Kumar | Company Secretary & Compliance Officer (Membership A69788) | 36-44 | Digitally signed 2026.08.13 22:20:59 +05'30' | — |
| 2 | Manav Mahajan | Senior Director – Ratings, Infomerics Valuation and Rating Ltd | 172-177 | Dated August 13, 2026 (no time-of-day; not a digital-signature block, seal placeholder) | — |

## 3. DECLARATION PARAGRAPHS (Monitoring Agency, before Section 1)

| # | Lines | First ~15 words | Flags |
|---|-------|------------------|-------|
| 1 | 143-156 | "We declare that this report provides an objective view of the utilization of the issue proceeds..." | — |
| 2 | 162-165 | "We declare that we do not have any direct / indirect interest in or relationship with the issuer..." | — |
| 3 | 167 | "We further declare that this report provides true and fair view of the utilization of issue proceeds." | — |

## 4. DEVIATION STATEMENT (top of report, Section header before Issuer Details)

| # | Lines | Statement | Value | Flags |
|---|-------|-----------|-------|-------|
| 1 | 125 | (a) Deviation from the objects | Nil | ZERO_STANDING |
| 2 | 127 | (b) Range of Deviation | Nil | ZERO_STANDING |
| 3 | 129-130 | Instructional text on how to indicate range of % deviation (up to 10%, 10-25%, etc.) | n/a (instructional) | — |
| 4 | 132-134 | Footnote *: Range of Deviation computed by weighted average of financial deviation per object | n/a (methodology note) | — |

## 5. ISSUER + ISSUE DETAILS (Section 1 & 2)

| # | Lines | Field | Value | Flags |
|---|-------|-------|-------|-------|
| 1 | 186 | Name of issuer | Gaudium IVF and Women Health Limited | — |
| 2 | 188 | Promoters | Dr. Manika Khanna, Dr. Peeyush Khanna, Vishad Khanna | — |
| 3 | 190 | Industry/sector | Indian fertility and women's healthcare | — |
| 4 | 194 | Issue period | Feb 20 2026 – Feb 24 2026 | — |
| 5 | 196 | Type of issue | Initial Public Offering | — |
| 6 | 198 | Type of specified securities | Equity Shares | — |
| 7 | 200 | Grading | NA | ZERO_STANDING |
| 8 | 202 | Issue size | Fresh Issuance Rs. 90.00 Cr (cross-ref Note No. 1) | — |
| 9 | 218-222 | Offer structure detail: 2,08,86,200 shares (1,13,92,500 fresh @ Rs.79 incl. Rs.74 premium = Rs.90 Cr; OFS 94,93,700 shares = Rs.75 Cr by Dr. Manika Khanna); fully subscribed | — | — |

### 5a. Note 1 — Issue proceeds breakdown table (Section 2, lines 204-213)

| Row | Lines | Particulars | Amount (Rs Cr) | Flags |
|-----|-------|-------------|-----------------|-------|
| 1 | 207 | Total proceeds received from IPO | 90.00* (footnote: gross proceeds monitored) | — |
| 2 | 208 | Less: expenses incurred related to IPO issue | 7.72 | — |
| 3 | 209 | Net Proceeds available for utilisation | 82.28 | — |
| footnote | 211 | *Infomerics Ratings shall be monitoring the Gross proceeds. | — | — |

## 6. SECTION 3 — ARRANGEMENT MADE TO ENSURE MONITORING (9-row Q&A table, lines 227-307)

| Row | Lines | Particulars | Reply | MA Comment | Board Comment | Flags |
|-----|-------|-------------|-------|------------|----------------|-------|
| 1 | 233-239 | Whether all utilization is as per disclosure in Offer Document? | Yes, per Offer Document | Gross proceeds Rs.90.00 Cr; Rs.8.69 Cr spent through Q4FY26, Rs.25.34 Cr cumulative utilised till June 30 2026 | No Comment Received | — |
| 2 | 242-249 | Whether Shareholder approval obtained for material deviations? | No deviations; approval not required | Not applicable | No Comment Received | ZERO_STANDING |
| 3 | 260-264 | Whether means of finance for disclosed objects has changed? | No change | No | No Comment Received | ZERO_STANDING |
| 4 | 266-268 | Any major deviation observed over earlier MA reports? | No | No Deviation | No Comment Received | ZERO_STANDING |
| 5 | 270-272 | Whether all Government/Statutory approvals obtained? | Yes | Listing approval from BSE & NSE; No Comments | No Comment Received | — |
| 6 | 274-276 | Whether arrangements pertaining to technical assistance/collaboration in operation? | Not Applicable | Not Applicable | No Comment Received | ZERO_STANDING |
| 7 | 278-282 | Any favourable events improving object(s) viability? | None | Nil | No Comment Received | ZERO_STANDING |
| 8 | 295-299 | Any unfavourable events affecting object(s) viability? | None | Nil | No Comment Received | ZERO_STANDING |
| 9 | 301-307 | Any other relevant information materially affecting investor decision-making? | None | Nil | No Comment Received | ZERO_STANDING |

Follow-on lines: 308-309 auditor verification statement (S K G N & Associates LLP, CA cert dated Aug 05 2026) — see Auditor Certificate References table (§12). Line 311: Auditor's remark "No deviations from expenditure disclosed in the Offer document." — deviation statement #5 (see §4 continuation below, listed in Deviations master list). Lines 312-314: footnote ^ defining "Material Deviation" (a) deviation in objects/purposes, (b) deviation >10% of projected amount.

## 7. SECTION 4(i) — COST OF OBJECT(S) TABLE (lines 316-380)

| Row | Lines | Item Head | Original Cost (Rs Cr) | Revised Cost | Reason/Financing/Arrangement cols | Flags |
|-----|-------|-----------|------------------------|--------------|-------------------------------------|-------|
| 1 | 337-341 | Funding capital expenditure towards establishment of New IVF Centres | 50.00 | Not Applicable | N.A / N.A / N.A | ZERO_STANDING (no cost revision) |
| 2 | 344-348 | Repayment or pre-payment of certain borrowings | 20.00 | Not Applicable | N.A / N.A / N.A | ZERO_STANDING |
| 3 | 351-354 | General Corporate Purpose | 12.28 | Not Applicable | N.A / N.A / N.A | ZERO_STANDING |
| 4 | 366-370 | Issue Expenses | 7.72 | Not Applicable | N.A / N.A / N.A | ZERO_STANDING |
| TOTAL | 373 | TOTAL | 90.00 | - | — | ZERO_STANDING (revised-cost column dash across the board) |
| note | 377 | Certificate dated August 05, 2026 issued by S K G N & Associates LLP (FRN: 023403N/N500052) | — | — | — | auditor cert ref (§12) |
| note | 380 | GCP utilised does not exceed 25% of Gross Proceeds (Rs 12.28 Cr) from Fresh Issue | — | — | — | — |

Arithmetic cross-check: 50.00 + 20.00 + 12.28 + 7.72 = 90.00 = TOTAL row. Reconciles.

## 8. SECTION 4(ii) — PROGRESS IN THE OBJECT(S) TABLE (lines 383-463)

| Row | Lines | Item Head | Proposed | Raised till Jun 30 26 | Utilised: Beginning | Utilised: During Qtr | Utilised: At End | Unutilised | Flags |
|-----|-------|-----------|----------|------------------------|----------------------|------------------------|---------------------|------------|-------|
| 1 | 410-419 | Funding capital exp. — New IVF Centres | 50.00 | 50.00 | - (0) | 1.03 | 1.03 | 48.97 | ZERO_STANDING (beginning-of-quarter = nil); cross-ref Note No.1 |
| 2 | 427-436 | Repayment/pre-payment of borrowings | 20.00 | 20.00 | - (0) | 18.07 | 18.07 | 1.93 | ZERO_STANDING (beginning = nil) |
| 3 | 438-446 | General Corporate Purpose | 12.28 | 12.28 | 0.97 | 6.24 | 7.21 | 5.07 | cross-ref Note No.2 (Lucknow Hospital) |
| 4 | 448-455 | Issue Expenses | 7.72 | 7.72 | 7.72 | 0 (Nil) | 7.72 | - (0) | ZERO_STANDING (nil utilisation during quarter; nil unutilised balance — fully spent pre-quarter) |
| TOTAL | 463 | TOTAL | 90.00 | 90.00 | 8.69 | 25.34 | 34.03 | 55.97 | — |

Arithmetic cross-check (object rows sum to TOTAL row, all four columns):
- Beginning: 0 + 0 + 0.97 + 7.72 = 8.69 = TOTAL. Reconciles.
- During quarter: 1.03 + 18.07 + 6.24 + 0 = 25.34 = TOTAL. Reconciles.
- At end of quarter: 1.03 + 18.07 + 7.21 + 7.72 = 34.03 = TOTAL. Reconciles.
- Unutilised: 48.97 + 1.93 + 5.07 + 0 = 55.97 = TOTAL. Reconciles.
All four column sums tie exactly to the TOTAL row. No arithmetic break found.

### Notes attached to Section 4(ii)

| Note | Lines | Content (summary) | Flags |
|------|-------|--------------------|-------|
| Note No. 1 | 467-478 | Utilisation verified based on documents furnished; payments to Luxen Interior and Décor LLP and Shinelife Meditec LLP supported by vendor quotations (not tax invoices) pending receipt; MA relied on management representation and vendor quotations for Rs 0.30 Cr (29.14% of Rs 1.03 Cr capex utilisation reviewed this quarter) where tax invoices pending | EVIDENCE_GAP (unaudited/pending invoices for 29.14% of quarter capex) |
| Note No. 2 | 480-504 | Board approved Gaudium Women Hospital, Lucknow (30-yr lease, 15-yr lock-in, 10% monthly net revenue + taxes, Rs 3.00 Cr refundable security deposit); expenditure funded under GCP head, NOT under earmarked IVF-centre capex object; Rs 5.76 Cr confirmed funded from GCP proceeds, in addition to (not from) the New-IVF-Centres object; MA notes amount remains within GCP 25% limit | RECLASSIFICATION flag — new-facility spend routed through GCP rather than the dedicated capex object |

## 9. BRIEF DESCRIPTION OF OBJECT(S) TABLE (lines 505-552)

| Row | Lines | Item Head | Description (summary) | Flags |
|-----|-------|-----------|-------------------------|-------|
| 1 | 510-521 | Funding capital exp. — New IVF Centres | 30+ locations (7 hubs + spokes via Infertility Expert alliance); plan to add 19 new IVF centres: 10 in FY27, 8 in FY28, 1 in FY29; Rs 50.00 Cr earmarked | — |
| 2 | 528-543 | Repayment/pre-payment of borrowings | HDFC Bank term loans + working capital; outstanding borrowings Rs 22.51 Cr as at Sep 30 2025 (restated consolidated basis); up to Rs 20.00 Cr earmarked; prepayment charges may apply | — |
| 3 | 545-552 | General Corporate Purpose | Rs 12.28 Cr for strategic initiatives, partnerships, JVs, acquisitions, exigencies, renovation/refurbishment, brand promotion, or other Board-approved purposes | — |

(Issue Expenses has no brief-description row — consistent absence, not a miss; it is a use-of-proceeds category rather than a growth "object.")

## 10. SECTION 4(iii) — DEPLOYMENT OF UNUTILIZED IPO PROCEEDS TABLE (lines 560-597)

| Row | Lines | Instrument | Amount (Rs Cr) | Maturity | Earnings | ROI % | Market Value at Jun 30 26 | Flags |
|-----|-------|-----------|------------------|----------|----------|-------|------------------------------|-------|
| 1 | 568-569 | HDFC Bank FD – 50301327584350 | 1.50 | Apr 03, 2027 | - | 7.27% | 1.50 | — |
| 2 | 572-573 | HDFC Bank FD – 50301327584541 | 27.00 | Apr 05, 2027 | - | 7.20% | 27.00 | — |
| 3 | 576-577 | HDFC Bank FD – 50301329234960 | 27.00 | Apr 05, 2027 | - | 7.20% | 27.00 | — |
| 4 | 580-582 | HDFC Current account – 50200119652282 | 0.38* | - | - | - | 0.38 | ZERO_STANDING (no maturity/earnings/ROI, operating cash) |
| 5 | 585-586 | Axis Bank – Public offer account | 0.23 | - | - | - | 0.23 | ZERO_STANDING (no maturity/earnings/ROI) |
| TOTAL | 589 | TOTAL | 56.11 | - | - | - | 56.11 | — |
| footnote | 596-597 | *O/s balance includes net interest on FDR of Rs 0.14 Cr; Rs 56.11 Cr deployment balance reconciles to Rs 55.97 Cr unutilised IPO proceeds (Section 4(ii) TOTAL) + Rs 0.14 Cr accrued interest | — | — |

Arithmetic cross-check: 1.50 + 27.00 + 27.00 + 0.38 + 0.23 = 56.11 = TOTAL row. Reconciles.
Cross-table cross-check: 56.11 (deployment TOTAL) − 0.14 (accrued interest per footnote) = 55.97 = Section 4(ii) Unutilised TOTAL. Reconciles.

## 11. SECTION 4(iv) — DELAY IN IMPLEMENTATION OF THE OBJECT(S) TABLE (lines 599-699)

| Row | Lines | Object | Completion date (Offer Doc) | Actual status | Delay | Reason of delay (summary) | Proposed course of action | Flags |
|-----|-------|--------|-------------------------------|-----------------|-------|------------------------------|------------------------------|-------|
| 1 | 617-666 | Funding capex — New IVF Centres | Upto FY29 | Ongoing | timing variance (deferment from FY25-26 to FY26-27) | Listing was Feb 27 2026; IPO proceeds reached company bank a/c only 3rd week of March 2026; limited time before Mar 31 2026 made it impracticable to establish planned centres and deploy capex on original schedule; Board on May 28 2026 noted deferment; no change in end-use/object of issue | Company ensures utilisation within stipulated timeline | DELAY flag |
| 1a | 622 | — embedded sub-row: Cost to be Incurred | FY27: 26.31 / FY28: 21.05 / FY29: 2.63 | — | — | — | — | — |
| 1b | 624 | — embedded sub-row: No. of Centres | FY27: 10 / FY28: 8 / FY29: 1 | — | — | — | — | — |
| 2 | 669-673 | Repayment/pre-payment of borrowings | Upto FY27 | Ongoing | Nil | No Comment Received | No Comment Received | ZERO_STANDING |
| 3 | 676-677 | General Corporate Purpose | Upto FY27 | Ongoing | Nil | No Comment Received | No Comment Received | ZERO_STANDING |

### Notes attached to Section 4(iv)

| Note | Lines | Content (summary) | Flags |
|------|-------|--------------------|-------|
| unlabeled "Note :" | 685-694 | Prospectus extract (Page 99): if scheduled-year utilisation not fully met, balance carried to next fiscal year per applicable law; over-utilisation met from internal accruals/additional equity or debt; under-utilisation redeployed to other objects or GCP (subject to 25% GCP cap) | — |
| Board meeting note | 696-699 | Board of Directors, meeting held 28 May 2026, took note of delay in utilisation of capex (new IVF centres) and repayment/pre-payment objects; originally FY25-26 spend now proposed for FY26-27 | DELAY flag |

## 12. SECTION 5 — GCP SUB-BREAKDOWN TABLE (lines 702-732)

| Row | Lines | Item Head | Amount (Rs Cr) | Source/Certification | MA Comment | Board Comment | Flags |
|-----|-------|-----------|------------------|------------------------|------------|-----------------|-------|
| 1 | 708-711 | Advance Payment for setting up, development, operation and management of "Gaudium Women Hospital, Lucknow" | 5.76 | Bank Statement, CA Certificate & Board resolution, Management Undertaking | Company has utilised proceeds towards the objective | No Comment Received | RECLASSIFICATION (new-facility capex routed via GCP; cross-ref Note No. 2 §8) |
| 2 | 712-714 | TDS Payment | 0.42 | Bank Statement, CA Certificate, Management Undertaking | (same MA comment row, spans rows 1-2) | No Comment Received | — |
| 3 | 718-719 | IPO Commission | 0.06 | Bank Statement, CA Certificate, Invoices, Management Undertaking | — | No Comment Received | — |
| footnote | 720-721 | * verified by S K G N & Associates LLP, CA certificate dated Aug 05 2026 | — | — | — | auditor cert ref (§12 below) |
| restated paragraph | 723-732 | Verbatim restatement of the Note No. 2 Lucknow-Hospital GCP-classification narrative (identical to lines 495-504) | — | — | — | DUPLICATE_NOTE (restates Note No. 2 content, not new information) |

Arithmetic cross-check: 5.76 + 0.42 + 0.06 = 6.24 = Section 4(ii) Row 3 (GCP) "During quarter" utilised value (line 438-446). Reconciles — the GCP sub-breakdown fully accounts for the quarter's Rs 6.24 Cr GCP utilisation.

## 13. AUDITOR CERTIFICATE REFERENCES

| # | Lines | Context | Flags |
|---|-------|---------|-------|
| 1 | 308-309 | "The above details are verified by S K G N & Associates LLP, Chartered Accountants statutory auditor... vide its CA certificate dated Aug 05, 2026" (Section 3 arrangement table) | — |
| 2 | 377 | "Certificate dated August 05, 2026, issued by S K G N & Associates LLP... Statutory auditor of the Company" (Section 4(i) cost table) | — |
| 3 | 720-721 | "* The above details are verified by S K G N & Associates LLP... vide its CA certificate dated Aug 05, 2026" (Section 5 GCP breakdown) | — |

All three references point to the single underlying CA certificate (S K G N & Associates LLP, FRN 023403N/N500052, dated Aug 05 2026); no distinct additional certificates identified.

## 14. DEVIATION / VARIATION STATEMENTS (master cross-reference list)

| # | Lines | Statement | Flags |
|---|-------|-----------|-------|
| 1 | 125 | (a) Deviation from the objects: Nil | ZERO_STANDING |
| 2 | 127 | (b) Range of Deviation: Nil | ZERO_STANDING |
| 3 | 242-249 | Section 3 row: no material deviations from disclosed expenditure; shareholder approval not required | ZERO_STANDING |
| 4 | 266-268 | Section 3 row: no major deviation vs earlier MA reports | ZERO_STANDING |
| 5 | 311 | Auditor's remark: "No deviations from expenditure disclosed in the Offer document" | — |
| 6 | 656-666 | Section 4(iv) timing-variance language: "timing variance exists; however, no change in end-use or object of issue has been observed" (Funding-capex delay row) | DELAY flag (timing, not financial, deviation) |

## 15. DISCLAIMERS (Wingdings-bulleted paragraphs, lines 740-810)

| # | Line | First ~15 words | Flags |
|---|------|------------------|-------|
| 1 | 742 | "This Report is prepared by Infomerics Valuation and Rating Limited (hereinafter referred to as..." | — |
| 2 | 748 | "This Report has to be seen in its entirety; the selective review of portions..." | — |
| 3 | 753 | "Nothing contained in this Report is capable or intended to create any legally binding obligations..." | — |
| 4 | 758 | "The MA and its affiliates do not act as a fiduciary. The MA and its affiliates also..." | — |
| 5 | 764 | "The MA or its affiliates may have other commercial transactions with the entity to which..." | — |
| 6 | 769 | "The MA report is intended for the jurisdiction of India only. This report does not..." | — |
| 7 | 774 | "Access or use of this report does not create a client relationship between MA and..." | — |
| 8 | 776 | "MA is not aware that any user intends to rely on the report or of the manner..." | — |
| 9 | 779 | "It is made abundantly clear that the report is not intended to and does not constitute..." | — |
| 10 | 787 | "The report comprises professional opinion of MA as of the date they are expressed..." | — |
| 11 | 793 | "Neither MA nor its affiliates, third-party providers, as well as their directors, officers..." | — |
| 12 | 804 | "MA has established policies and procedures to maintain the confidentiality of certain non-public..." | — |
| 13 | 807 | "Unless required under any applicable law, this report should not be reproduced or redistributed..." | — |
| 14 | 809 | "By accepting a copy of this Report, the recipient accepts the terms of this Disclaimer..." | — |

---

## SUMMARY COUNTS

| Category | Count |
|---|---|
| Cover/transmittal items | 2 |
| Signature blocks | 2 |
| Declaration paragraphs | 3 |
| Deviation statement (top-of-report, 2 items + instructional note + footnote) | 4 line units |
| Issuer/Issue detail fields | 9 |
| Note 1 issue-proceeds table rows (+footnote) | 3 rows + 1 footnote |
| Section 3 arrangement table rows | 9 |
| Section 4(i) cost table rows | 4 objects + 1 TOTAL + 2 notes |
| Section 4(ii) progress table rows | 4 objects + 1 TOTAL + 2 notes |
| Brief description table rows | 3 |
| Section 4(iii) deployment table rows | 5 instruments + 1 TOTAL + 1 footnote |
| Section 4(iv) delay table rows | 3 objects + 2 embedded sub-rows + 2 notes |
| Section 5 GCP sub-breakdown rows | 3 + 1 footnote + 1 duplicate restated paragraph |
| Auditor certificate references | 3 |
| Deviation/variation statements (master list) | 6 |
| Disclaimer paragraphs | 14 |
| **Object-of-the-issue rows across all 4 object tables** | **14** |
| **All fund-utilization table rows, every table (incl. TOTALs, sub-rows)** | **39** |
| **Distinct notes/footnotes (bodies)** | **11** (+1 flagged duplicate restatement) |

## ARITHMETIC CROSS-CHECKS (all reconciled — no breaks found)

1. Section 4(i) Cost table: 50.00 + 20.00 + 12.28 + 7.72 = 90.00 = TOTAL. PASS.
2. Section 4(ii) Progress table, Beginning column: 0 + 0 + 0.97 + 7.72 = 8.69 = TOTAL. PASS.
3. Section 4(ii) Progress table, During-quarter column: 1.03 + 18.07 + 6.24 + 0 = 25.34 = TOTAL. PASS.
4. Section 4(ii) Progress table, At-end column: 1.03 + 18.07 + 7.21 + 7.72 = 34.03 = TOTAL. PASS.
5. Section 4(ii) Progress table, Unutilised column: 48.97 + 1.93 + 5.07 + 0 = 55.97 = TOTAL. PASS.
6. Section 4(iii) Deployment table: 1.50 + 27.00 + 27.00 + 0.38 + 0.23 = 56.11 = TOTAL. PASS.
7. Cross-table: Deployment TOTAL 56.11 − 0.14 accrued interest = 55.97 = Progress-table Unutilised TOTAL. PASS.
8. Cross-table: GCP sub-breakdown (5.76 + 0.42 + 0.06 = 6.24) = Progress-table GCP "During quarter" utilised value. PASS.
9. Note 1 (issue-proceeds): 90.00 − 7.72 = 82.28 = stated Net Proceeds. PASS.

No arithmetic mismatches were found anywhere across the report's tables.

## FLAGS RAISED (roll-up)

- ZERO_STANDING — 19 instances (top-of-report deviation Nil x2, Section 3 rows 2/3/4/6/7/8/9, cost-table revised-cost column x4 + TOTAL, progress-table beginning-of-quarter nils x2, progress-table Issue-Expenses during/unutilised nils, deployment-table current a/c and public-offer a/c rows x2, delay-table Repayment/GCP rows x2)
- EVIDENCE_GAP — 1 instance (Note No. 1: Rs 0.30 Cr / 29.14% of quarter capex verified only via vendor quotations, tax invoices pending)
- RECLASSIFICATION — 2 instances (Note No. 2 and Section 5 Row 1: Lucknow Hospital Rs 5.76 Cr routed through GCP rather than the dedicated New-IVF-Centres capex object)
- DELAY — 2 instances (Section 4(iv) Funding-capex row; Board meeting note on deferment)
- DUPLICATE_NOTE — 1 instance (lines 723-732 restate Note No. 2's Lucknow narrative verbatim within Section 5)
