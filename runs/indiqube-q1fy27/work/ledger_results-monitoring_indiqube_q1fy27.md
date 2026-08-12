# A2 ENUMERATION LEDGER — INDIQUBE Q1FY27 — CRISIL Monitoring Agency Report (IPO proceeds utilisation)

Source: extract_results-monitoring_indiqube_q1fy27.txt (15 pages, 744 lines, unit = Rs million)
Prior-quarter ledger: NONE (first pipeline run for INDIQUBE — no ENTITY_CHANGE / DROPPED_SLIDE diffs possible this run)
Doctype note: this is not a standard results filing (no P&L/balance-sheet notes, no board agenda, no auditor's report, no
consolidation entity list, no concall/slide content). Categories below are adapted from the RESULTS FILING template to the
actual disclosure units present in a Regulation 32(6)/Schedule XI Monitoring Agency Report. Standard template categories with
no counterpart in this doctype (agenda_items, auditor_paras, entities, turns, questions, mgmt_numbers, slides) are marked N/A.

```
=== A2 COUNT TEST ===
category: deviation_declaration     grep_count: 2    sweep_count: 2    match: yes
category: report_header_fields      grep_count: 3    sweep_count: 3    match: yes
category: issuer_issue_details      grep_count: 11   sweep_count: 11   match: yes
category: arrangement_table         grep_count: 9    sweep_count: 9    match: yes
category: cost_table                grep_count: 10   sweep_count: 10   match: yes
category: object_descriptions       grep_count: 7    sweep_count: 7    match: yes
category: progress_table            grep_count: 10   sweep_count: 10   match: yes
category: zero_standing (subset)    grep_count: 5    sweep_count: 5    match: yes
category: deployment_items          grep_count: 65   sweep_count: 65   match: yes
category: deployment_summary        grep_count: 3    sweep_count: 3    match: yes
category: delay_implementation      grep_count: 2    sweep_count: 2    match: yes
category: notes                     grep_count: 3    sweep_count: 3    match: yes
category: ca_certificate_references grep_count: 10   sweep_count: 10   match: yes
category: disclaimers               grep_count: 14   sweep_count: 14   match: yes
category: signature_blocks          grep_count: 3    sweep_count: 3    match: yes
category: transmittal_letters       grep_count: 2    sweep_count: 2    match: yes
category: agenda_items              grep_count: N/A  sweep_count: N/A  match: n/a (no board outcome letter in this doctype)
category: auditor_paras             grep_count: N/A  sweep_count: N/A  match: n/a (MA declaration ≠ statutory audit opinion; captured under deviation_declaration/disclaimers)
category: entities                  grep_count: N/A  sweep_count: N/A  match: n/a (no consolidation list in this doctype)
category: turns / questions / mgmt_numbers / slides  grep_count: N/A  sweep_count: N/A  match: n/a (not a concall/deck)
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used (all against the extract file):
- deviation: `grep -n -E "^\(a\)|^\(b\)"`
- report header: `grep -n -E "^Name of the issuer:|^For quarter ended:|^Name of the Monitoring Agency:"`
- issuer/issue fields: `grep -n -E "Name of the issuer:|Names of the promoter:|Industry/sector to which it belongs:|Issue Period:|Type of issue|Type of specified securities:|IPO Grading|Issue size:"` + `grep -n -E "Gross proceeds|Less: Issue Expenses|Net Proceeds"`
- arrangement table: `grep -n "Whether\|Is there any\|Are there any"`
- cost/progress table rows: `sed -n '<range>p' | grep -n -E "^\s*(-|[0-9]+)\s"`
- deployment items: `grep -c -E "^\s*(-|[0-9]+)\s.*(Fixed deposit-|Balance in (Public Issue|Monitoring) Account|Total)"`
- notes: `grep -n -E "^\s*Note [0-9]+"`
- CA certificate: `grep -n -i "peer-reviewed"`
- disclaimers: `grep -n -E "^\s*[a-n]\) "`
- letters: `grep -n -E "^\s*Subject:|Monitoring Agency Report for the quarter ended June 30, 2026 - in relation"`

---

## 1. TRANSMITTAL LETTERS (2)

| # | Line | From -> To | Subject / content | Flags |
|---|------|-----------|--------------------|-------|
| L1 | 15-52 | Indiqube Spaces Ltd (Bhasker Dubey, CS & Compliance Officer) -> BSE Ltd, NSE Ltd | Forwarding cover letter enclosing Reg 32(6) Monitoring Agency Report for quarter ended June 30, 2026; BSE Scrip Code 544454, NSE Symbol INDIQUBE; also references website posting at indiqube.com/investor | — |
| L2 | 77-107 | Crisil Ratings Ltd (Shounak Chakravarty, Director Ratings-LCG) -> Indiqube Spaces Ltd | Ref CRL/MAR/INSPRI/2026-27/1855, dated Aug 12 2026; forwarding MA Report per Reg 41(2) SEBI ICDR Regs and Monitoring Agency Agreement dated July 3, 2025, per Schedule XI SEBI ICDR Regs | — |

## 2. SIGNATURE BLOCKS (3)

| # | Line | Signatory | Designation | Timestamp / date | Flags |
|---|------|-----------|-------------|-------------------|-------|
| S1 | 44-52 | Bhasker Dubey | Company Secretary & Compliance Officer, Indiqube Spaces Ltd | Digitally signed 2026.08.12 18:09:09 +05'30' | — |
| S2 | 100-106 | Shounak Chakravarty | Director, Ratings (LCG), Crisil Ratings Ltd | Letter dated August 12, 2026 (no digital timestamp shown) | — |
| S3 | 151-153 | Shounak Chakravarty | Director, Ratings (LCG), Crisil Ratings Ltd — Authorized Signatory of MA Report declaration | Report dated August 12, 2026; underlying CA certificate referenced dated August 10, 2026 | — |

## 3. REPORT HEADER FIELDS (page 4) (3)

| # | Line | Field | Value | Flags |
|---|------|-------|-------|-------|
| H1 | 116 | Name of the issuer | Indiqube Spaces Limited | — |
| H2 | 118 | For quarter ended | June 30, 2026 | — |
| H3 | 120 | Name of the Monitoring Agency | Crisil Ratings Limited | — |

## 4. DEVIATION DECLARATION (2)

| # | Line | Item | Content | Flags |
|---|------|------|---------|-------|
| D1 | 122-124 | (a) Deviation from the objects | "Utilization different from Objects stated in the offer document but in line with change of objects approved by shareholders' resolution." | DEVIATION_DECLARED |
| D2 | 125 | (b) Range of Deviation | 25-35% | DEVIATION_DECLARED |

Declaration paragraph (MA disclaimer text, lines 127-147) and signature (lines 151-153) captured under Signature Blocks (S3) / Disclaimers context; not double-counted here.

## 5. ISSUER & ISSUE DETAILS (Section 1-2) (11)

| # | Line | Field | Value | Flags |
|---|------|-------|-------|-------|
| I1 | 163 | Name of the issuer | Indiqube Spaces Limited | — |
| I2 | 165 | Names of the promoter | Mr. Rishi Das, Ms. Meghna Agarwal and Mr. Anshuman Das | — |
| I3 | 167 | Industry/sector | Flexible workspace solutions service provider | — |
| I4 | 171 | Issue Period | July 23, 2025 to July 25, 2025 | — |
| I5 | 173 | Type of issue | Initial Public Offer (IPO) | — |
| I6 | 175 | Type of specified securities | Equity Shares | — |
| I7 | 177 | IPO Grading, if any | NA | — |
| I8 | 179 | Issue size | Rs 6,500.00 million* | — |
| I9 | 188 | Gross proceeds | Rs 6,500.00 million# | — |
| I10 | 192 | Less: Issue Expenses | Rs 455.41 million | — |
| I11 | 196 | Net Proceeds | Rs 6,044.59 million | — |

Footnotes: "#Crisil Ratings shall be monitoring the gross proceeds" (line 199).

## 6. DETAILS OF ARRANGEMENT / MONITORING QUESTIONNAIRE (9)

| # | Line | Question | Reply | Source cited | Board comment | Flags |
|---|------|----------|-------|---------------|----------------|-------|
| A1 | 219-226 | Whether all utilization is as per the disclosures in the Offer Document? | Yes | Management undertaking, Peer-reviewed Independent CA Certificate, Prospectus dated July 25, 2025, Bank Statements | "Proceeds were utilized towards capital expenditure and issue expenses" / No comments | CA_CERT_REF |
| A2 | 227-233 | Whether shareholder approval has been obtained in case of material deviations from expenditures disclosed in the Offer Document? | Yes | (not separately stated in row) | "Shareholder approval obtained for deviation in cost of objects. Refer to note 2 on page 7" / No comments | — |
| A3 | 234-238 | Whether the means of finance for the disclosed objects of the issue has changed? | No | — | No comments / No comments | — |
| A4 | 239-243 | Is there any major deviation observed over the earlier monitoring agency reports? | No | — | No comments / No comments | — |
| A5 | 244-248 | Whether all Government/statutory approvals related to the object(s) have been obtained? | NA | Management undertaking, Peer-reviewed Independent CA Certificate | No comments / No comments | CA_CERT_REF |
| A6 | 249-253 | Whether all arrangements pertaining to technical assistance/collaboration are in operation? | NA | (shares source cell with A5) | No comments / No comments | — |
| A7 | 254-258 | Are there any favorable events improving the viability of these object(s)? | No | — | No comments / No comments | — |
| A8 | 259-263 | Are there any unfavorable events affecting the viability of the object(s)? | No | — | No comments / No comments | — |
| A9 | 264-268 | Is there any other relevant information that may materially affect the decision making of the investors? | No | — | No comments / No comments | — |

Footnote line 269: "NA represents Not Applicable." Footnote lines 271-272: first CA certificate reference (dated Aug 10, 2026, S K Patodia & Associates LLP, FRN 112723W/W100962) — counted under CA_CERTIFICATE_REFERENCES table below.

## 7. COST OF THE OBJECT(S) TABLE (Section 4i) (10 rows)

| # | Line | Item head | Original cost (offer doc) | Revised cost | Comment ref | Flags |
|---|------|-----------|----------------------------|---------------|-------------|-------|
| C1 | 294-298 (values line 296) | 1. Funding capital expenditure towards establishment of new centers | 4,626.49 | 2,756.49 | Refer note 2 (both cols) | COST_REVISED_DOWN |
| C2 | 299-305 (values line 302, note ref line 303) | 2. Repayment/pre-payment of certain borrowings | 930.35 | 913.40 | Refer note 1 (both cols) | COST_REVISED_DOWN |
| C3 | 306-308 (values line 307) | 3. General Corporate Purposes# | 487.75 | 504.70 | Refer note 1 (both cols) | COST_REVISED_UP |
| C4 | 309-313 (values line 311) | 4. Funding security deposit for new centers | - (nil, no original allocation) | 520.00 | Refer note 2 (both cols) | NEW_OBJECT, ZERO_STANDING (original col) |
| C5 | 314-320 (values line 317) | 5. Funding capital expenditure towards fit-out and interior in non-Indiqube properties | - (nil) | 550.00 | Refer note 2 (both cols) | NEW_OBJECT, ZERO_STANDING (original col) |
| C6 | 321-325 (values line 323) | 6. Funding capital expenditure towards renewable power infrastructure | - (nil) | 160.00 | Refer note 2 (both cols) | NEW_OBJECT, ZERO_STANDING (original col) |
| C7 | 326-330 (values line 328) | 7. Capital deployment in strategic commercial real estate opportunities | - (nil) | 640.00 | Refer note 2 (both cols) | NEW_OBJECT, ZERO_STANDING (original col) |
| C8 | 331 | Sub-total | 6,044.59 | 6,044.59 | — | — |
| C9 | 334-335 | 8. Issue expenses | 455.41 | 455.41 | "No revision" | — |
| C10 | 337 | Total | 6,500.00 | 6,500.00 | — | — |

Footnotes: line 339-340 CA certificate reference (2nd occurrence); line 342-344 "#The amount utilised for general corporate purposes does not exceed 25% of the Gross Proceeds (amounting to Rs 1,625.00 million) from the Fresh Issue."

Objects 4-7 (rows C4-C7) are the four new objects created by the June 24, 2026 postal-ballot reallocation of proceeds out of Object 1 — flagged NEW_OBJECT. Their "original cost" column is dash/nil because they did not exist in the offer document — flagged ZERO_STANDING in that column per the "never drop a nil row" rule.

## 8. NOTES 1-3 (below cost / progress / delay tables) (3)

| # | Line | Note | First ~15 words | Flags |
|---|------|------|-------------------|-------|
| N1 | 350-355 | Note 1 | "Following the repayment of borrowings outlined in the Offer document, a balance of Rs 16.95 million remains..." — balance rolled into General Corporate Purposes per offer-doc disclaimer | — |
| N2 | 357-362 | Note 2 | "Shareholder's approval has been obtained vide special resolution dated June 24, 2026 through Postal Ballot Notice, for reallocation..." of proceeds from Object 1 to new Objects 4-7 | NEW_OBJECT source, DEVIATION_DECLARED source |
| N3 | 648-656 | Note 3 | "As per Company's Prospectus dated July 25, 2025, the Company had estimated to utilize Rs 2,448.73 million for the aforementioned objects by Fiscal 2026. However...the Company has utilized Rs 1,776.97 million only as at quarter ended June 30, 2026. Hence, there is a delay..." Reason given: "lower operational requirements." Followed by prospectus carry-forward clause (lines 654-656) | DELAY_IN_IMPLEMENTATION |

## 9. OBJECT DESCRIPTIONS ("Brief description of objects", Section 4-footnote table, page 10) (7)

| # | Line | Object | Description content | Flags |
|---|------|--------|----------------------|-------|
| OD1 | 478-484 | Funding capital expenditure towards establishment of new centers | Plan to open new centers covering 1.29 msf (FY26), 1.24 msf (FY27), 0.54 msf (FY28); proposed spend Rs 1,944.03M (FY26), Rs 1,868.68M (FY27), Rs 813.78M (FY28) from Net Proceeds | — |
| OD2 | 489-497 | Repayment/pre-payment of certain borrowings | Repayment of fund-based/non-fund-based facilities incl. term loans and working capital loans; proposed Rs 913.40M from Net Proceeds | — |
| OD3 | 502-506 | General Corporate Purposes | Balance Net Proceeds of Rs 504.70M for GCP/business requirements, capped at 25% of Gross Proceeds per SEBI ICDR | — |
| OD3a | 507 | GCP sub-item (i) | "meeting ongoing general corporate expenses, exigencies and contingencies" | — |
| OD3b | 508 | GCP sub-item (ii) | "marketing, advertising expenditures and business development expenses" | — |
| OD3c | 509 | GCP sub-item (iii) | "payment of salaries and allowances, administration, insurance, repair & maintenance, payment of taxes, duties and meeting expenses..." | — |
| OD3d | 512 | GCP sub-item (iv) | "any other purpose as may be approved by the Board or duly appointed committee from time to time..." | — |

Note: objects 4-7 (the postal-ballot additions) have no corresponding narrative description entry in this table — the description table was not updated to cover the four new objects. Flag DROPPED_DESCRIPTION (analogue of DROPPED_SLIDE — a disclosure present for legacy objects but silently absent for the new ones) for A3/A4 review.

## 10. PROGRESS IN THE OBJECT(S) TABLE (Section 4ii) (10 rows)

| # | Line | Item head | Proposed | As at beginning of qtr | During qtr | At end of qtr | Total unutilized | Board comment / reason | Flags |
|---|------|-----------|----------|--------------------------|------------|-----------------|--------------------|--------------------------|-------|
| P1 | 385-394 (values line 387) | 1. Funding capital expenditure towards establishment of new centers | 2,756.49 | 892.29 | 383.99 | 1,276.28 | 1,480.21 | "Proceeds were utilized towards purchase of plant and machinery, furniture and fixtures, etc." | — |
| P2 | 396-402 (values line 398) | 2. Repayment/pre-payment of certain borrowings | 913.40 | 913.40 | Nil | 913.40 | Nil | "Proceeds fully utilized till quarter ended Sept 30, 2025" | ZERO_STANDING (during-qtr and unutilized cells) |
| P3 | 426-428 (values line 427) | 3. General Corporate Purposes | 504.70 | 500.69 | Nil | 500.69 | 4.01 | (no comment given) | ZERO_STANDING (during-qtr cell) |
| P4 | 432-435 (values line 433) | 4. Funding security deposit for new centers | 520.00 | Nil | Nil | Nil | 520.00 | "No utilization during the reported quarter" (shared note spans P4-P7) | ZERO_STANDING (full row — all utilised columns nil), NEW_OBJECT |
| P5 | 436-441 (values line 438) | 5. Funding capital expenditure towards fit-out and interior in non-Indiqube properties | 550.00 | Nil | Nil | Nil | 550.00 | as above | ZERO_STANDING (full row), NEW_OBJECT |
| P6 | 442-446 (values line 444) | 6. Funding capital expenditure towards renewable power infrastructure | 160.00 | Nil | Nil | Nil | 160.00 | as above | ZERO_STANDING (full row), NEW_OBJECT |
| P7 | 447-449 (values line 448) | 7. Capital deployment in strategic commercial real estate opportunities | 640.00 | Nil | Nil | Nil | 640.00 | as above | ZERO_STANDING (full row), NEW_OBJECT |
| P8 | 450 | Sub-total | 6,044.59 | 2,306.38 | 383.99 | 2,690.37 | 3,354.22 | — | — |
| P9 | 454-457 | 8. Issue expenses | 455.41 | 398.71 | 5.04 | 403.74 | 51.66 | "Proceeds utilized towards IPO related expenses" | — |
| P10 | 458 | Total | 6,500.00 | 2,705.09 | 389.02 | 3,094.11 | 3,405.88 | — | — |

Footnotes: line 460-461 CA certificate reference (3rd occurrence); line 463 "*Refer to note 2 on page 7" (cross-ref to N2).

Four full-nil rows (P4-P7, the same four postal-ballot objects) carry zero utilisation in every one of the three utilised-amount columns for this quarter, consistent with the objects having only just been created on June 24, 2026 (6 days before quarter end) — flagged ZERO_STANDING per operating rule 3, not dropped.

## 11. DEPLOYMENT OF UNUTILISED PROCEEDS TABLE (Section 4iii) (65 rows)

| # | Line | Instrument | Amount invested (Rs M) | Maturity date | Earnings as on 30-Jun-26 (Rs M) | Return on Investment | Market value at qtr end (Rs M) | Flags |
|---|------|-----------|--------------------------|-----------------|-----------------------------------|-------------------------|-----------------------------------|-------|
| FD1 | 536-537 | Balance in Public Issue Account (Axis Bank) | 57.13 | - | - | - | 57.13 | ZERO_STANDING (maturity/earnings/ROI dash-valued, non-FD balance) |
| FD2 | 538-540 | Balance in Monitoring Account (Axis Bank) | 109.49 | - | - | - | 109.49 | ZERO_STANDING (maturity/earnings/ROI dash-valued, non-FD balance) |
| FD3 | 541 | Fixed deposit- 2503269537990082/7 | 104.00 | 06-09-2026 | 1.92 | 7.10% | 105.92 | — |
| FD4 | 542 | Fixed deposit- 2503269537990082/8 | 104.00 | 06-09-2026 | 1.92 | 7.10% | 105.92 | — |
| FD5 | 543 | Fixed deposit- 2503269537990082/9 | 104.00 | 06-09-2026 | 1.92 | 7.10% | 105.92 | — |
| FD6 | 544 | Fixed deposit- 2503269537990082/10 | 104.00 | 06-09-2026 | 1.92 | 7.10% | 105.92 | — |
| FD7 | 545 | Fixed deposit- 2503269537990082/11 | 104.00 | 06-09-2026 | 1.92 | 7.10% | 105.92 | — |
| FD8 | 546 | Fixed deposit- 2503269537990082/12 | 104.00 | 06-09-2026 | 1.92 | 7.10% | 105.92 | — |
| FD9 | 547 | Fixed deposit- 2503269537990082/13 | 104.00 | 06-09-2026 | 1.92 | 7.10% | 105.92 | — |
| FD10 | 548 | Fixed deposit- 2503269537990082/14 | 104.00 | 06-09-2026 | 1.92 | 7.10% | 105.92 | — |
| FD11 | 549 | Fixed deposit- 2503269537990082/15 | 104.00 | 06-09-2026 | 1.92 | 7.10% | 105.92 | — |
| FD12 | 550 | Fixed deposit- 82000105091176/1 | 22.50 | 04-08-2026 | 1.37 | 7.25% | 23.87 | — |
| FD13 | 551 | Fixed deposit- 82000105192321/1 | 26.40 | 05-08-2026 | 1.61 | 7.25% | 28.01 | — |
| FD14 | 552 | Fixed deposit- 82000105193198/1 | 25.60 | 06-08-2026 | 1.56 | 7.25% | 27.16 | — |
| FD15 | 553 | Fixed deposit- 82000105194672/1 | 24.80 | 07-08-2026 | 1.51 | 7.25% | 26.31 | — |
| FD16 | 554 | Fixed deposit- 82000105198007/1 | 26.40 | 08-08-2026 | 1.61 | 7.25% | 28.01 | — |
| FD17 | 555 | Fixed deposit- 82000105096050/1 | 26.20 | 09-08-2026 | 1.60 | 7.25% | 27.80 | — |
| FD18 | 556 | Fixed deposit- 82000105211216/1 | 25.80 | 10-08-2026 | 1.58 | 7.25% | 27.38 | — |
| FD19 | 557 | Fixed deposit- 82000105104654/1 | 24.50 | 11-08-2026 | 1.50 | 7.25% | 26.00 | — |
| FD20 | 558 | Fixed deposit- 82000105104670/1 | 25.40 | 12-08-2026 | 1.55 | 7.25% | 26.95 | — |
| FD21 | 559 | Fixed deposit- 82000105211232/1 | 24.90 | 13-08-2026 | 1.52 | 7.25% | 26.42 | — |
| FD22 | 560 | Fixed deposit- 82000105207067/1 | 26.80 | 14-08-2026 | 1.64 | 7.25% | 28.44 | — |
| FD23 | 561 | Fixed deposit- 82000105207093/1 | 25.50 | 15-08-2026 | 1.56 | 7.25% | 27.06 | — |
| FD24 | 562 | Fixed deposit- 82000105101799/1 | 25.70 | 16-08-2026 | 1.57 | 7.25% | 27.27 | — |
| FD25 | 563 | Fixed deposit- 82000105207614/1 | 24.10 | 17-08-2026 | 1.47 | 7.25% | 25.57 | — |
| FD26 | 564 | Fixed deposit- 82000105207805/1 | 23.80 | 18-08-2026 | 1.45 | 7.25% | 25.25 | — |
| FD27 | 565 | Fixed deposit- 82000105102214/1 | 25.30 | 19-08-2026 | 1.54 | 7.25% | 26.84 | — |
| FD28 | 566 | Fixed deposit- 82000105208991/1 | 23.10 | 20-08-2026 | 1.41 | 7.25% | 24.51 | — |
| FD29 | 567 | Fixed deposit- 82000105102648/1 | 24.90 | 21-08-2026 | 1.52 | 7.25% | 26.42 | — |
| FD30 | 568 | Fixed deposit- 82000105102737/1 | 26.50 | 22-08-2026 | 1.62 | 7.25% | 28.12 | — |
| FD31 | 569 | Fixed deposit- 82000105208722/1 | 25.40 | 23-08-2026 | 1.55 | 7.25% | 26.95 | — |
| FD32 | 570 | Fixed deposit- 82000105102931/1 | 24.80 | 24-08-2026 | 1.51 | 7.25% | 26.31 | — |
| FD33 | 571 | Fixed deposit- 82000105208910/1 | 25.90 | 25-08-2026 | 1.58 | 7.25% | 27.48 | — |
| FD34 | 572 | Fixed deposit- 82000105209162/1 | 25.20 | 26-08-2026 | 1.54 | 7.25% | 26.74 | — |
| FD35 | 573 | Fixed deposit- 82000105103411/1 | 21.30 | 27-08-2026 | 1.30 | 7.25% | 22.60 | — |
| FD36 | 574 | Fixed deposit- 82000105209353/1 | 23.50 | 28-08-2026 | 1.43 | 7.25% | 24.93 | — |
| FD37 | 575 | Fixed deposit- 82000105209531/1 | 24.40 | 29-08-2026 | 1.49 | 7.25% | 25.89 | — |
| FD38 | 576 | Fixed deposit- 82000105103680/1 | 23.90 | 30-08-2026 | 1.46 | 7.25% | 25.36 | — |
| FD39 | 577 | Fixed deposit- 82000105209837/1 | 24.00 | 31-08-2026 | 1.47 | 7.25% | 25.47 | — |
| FD40 | 578 | Fixed deposit- 82000105103855/1 | 24.20 | 01-09-2026 | 1.48 | 7.25% | 25.68 | — |
| FD41 | 579 | Fixed deposit- 82000105209913/1 | 23.60 | 02-09-2026 | 1.44 | 7.25% | 25.04 | — |
| FD42 | 583 | Fixed deposit- 82000105096293/1 | 24.70 | 03-09-2026 | 1.51 | 7.25% | 26.21 | — |
| FD43 | 584 | Fixed deposit- 82000105199355/1 | 25.30 | 04-09-2026 | 1.54 | 7.25% | 26.84 | — |
| FD44 | 585 | Fixed deposit- 82000105199674/1 | 25.80 | 05-09-2026 | 1.58 | 7.25% | 27.38 | — |
| FD45 | 586 | Fixed deposit- 82000105199839/1 | 23.30 | 06-09-2026 | 1.42 | 7.25% | 24.72 | — |
| FD46 | 587 | Fixed deposit- 82000105200402/1 | 23.60 | 07-09-2026 | 1.44 | 7.25% | 25.04 | — |
| FD47 | 588 | Fixed deposit- 82000105097079/1 | 23.90 | 08-09-2026 | 1.46 | 7.25% | 25.36 | — |
| FD48 | 589 | Fixed deposit- 82000105097435/1 | 24.50 | 09-09-2026 | 1.50 | 7.25% | 26.00 | — |
| FD49 | 590 | Fixed deposit- 82000105200823/1 | 24.70 | 10-09-2026 | 1.51 | 7.25% | 26.21 | — |
| FD50 | 591 | Fixed deposit- 82000105097678/1 | 24.80 | 11-09-2026 | 1.51 | 7.25% | 26.31 | — |
| FD51 | 592 | Fixed deposit- 82000105201230/1 | 21.90 | 12-09-2026 | 1.34 | 7.25% | 23.24 | — |
| FD52 | 593 | Fixed deposit- 82000105202217/1 | 26.30 | 13-09-2026 | 1.61 | 7.25% | 27.91 | — |
| FD53 | 594 | Fixed deposit- 82000105202256/1 | 25.00 | 14-09-2026 | 1.53 | 7.25% | 26.53 | — |
| FD54 | 595 | Fixed deposit- 82000105202740/1 | 26.60 | 15-09-2026 | 1.62 | 7.25% | 28.22 | — |
| FD55 | 596 | Fixed deposit- 82000105100119/1 | 23.00 | 16-09-2026 | 1.40 | 7.25% | 24.40 | — |
| FD56 | 597 | Fixed deposit- 82000105205762/1 | 25.10 | 17-09-2026 | 1.53 | 7.25% | 26.63 | — |
| FD57 | 598 | Fixed deposit- 82000105101862/1 | 24.80 | 18-09-2026 | 1.51 | 7.25% | 26.31 | — |
| FD58 | 599 | Fixed deposit- 82000105207041/1 | 21.80 | 19-09-2026 | 1.33 | 7.25% | 23.13 | — |
| FD59 | 600 | Fixed deposit- 926040061624341 | 400.00 | 09-07-2026 | 8.20 | 6.60% | 408.20 | — |
| FD60 | 601 | Fixed deposit- 926040074249012 | 300.00 | 08-04-2027 | 4.97 | 7.20% | 304.97 | — |
| FD61 | 602 | Fixed deposit- 2603269544178650/1 | 50.00 | 26-10-2026 | 0.65 | 6.90% | 50.65 | — |
| FD62 | 603 | Fixed deposit- 2603269544393915/1 | 100.10 | 01-11-2026 | 1.17 | 6.90% | 101.27 | — |
| FD63 | 604 | Fixed deposit- 82000138415605/1 | 250.10 | 11-12-2026 | - (dash) | 7.65% | 250.10 | ZERO_STANDING (Earnings-as-on-date cell dash-valued, unlike all other FD rows which carry a positive earnings figure) |
| FD64 | 605 | Fixed deposit- 2603269545728617/1 | 50.00 | 19-07-2026 | 0.10 | 5.75% | 50.10 | — |
| FD-T | 606 | Total | 3,412.32 | - | 103.15 | - | 3,515.47 | — |

Row count reconciliation: 2 bank-balance rows + 62 fixed-deposit rows = 64 numbered Sr. No. rows (matching the ~64 line items called for in task scope), plus 1 Total row = 65 lines enumerated in this table. FD63 is the only FD row with a dash instead of a positive earnings figure — flagged ZERO_STANDING rather than silently treated as a formatting variant.

Footnote: line 618-619 CA certificate reference (4th occurrence, marked "^" against table title at line 524).

## 12. DEPLOYMENT SUMMARY RECONCILIATION (page 11-12) (3)

| # | Line | Particular | Amount (Rs M) | Flags |
|---|------|-----------|-----------------|-------|
| DS1 | 610-612 | Proceeds parked in fixed deposits, monitoring account and public offer account of the Company | 3,412.32 | — |
| DS2 | 613-615 | Less: Earnings on fixed deposits and proceeds from Offer for Sale (does not form part of the scope of Monitoring Agency) | (6.44) | — |
| DS3 | 616 | Unutilized Gross Proceeds | 3,405.88 | — |

This 3,405.88 ties to the Progress table Total unutilized amount (P10, line 458).

## 13. DELAY IN IMPLEMENTATION OF THE OBJECT(S) TABLE (Section 4iv) (2)

| # | Line | Object | As per offer doc (FY26 estimate) | Actual completion | Delay | Reason of delay | Proposed course of action | Flags |
|---|------|--------|--------------------------------------|----------------------|-------|-------------------|-------------------------------|-------|
| DL1 | 638-641 | Funding capital expenditure towards establishment of new centers | Rs 1,944.03 million | Refer note 3 | Refer note 3 | Refer note 3 | - (none proposed) | DELAY_IN_IMPLEMENTATION |
| DL2 | 642-646 | General Corporate Purposes | Rs 504.70 million | Refer note 3 | Refer note 3 | Refer note 3 | - (none proposed) | DELAY_IN_IMPLEMENTATION |

Combined offer-doc estimate for these two objects by FY26: Rs 1,944.03M + Rs 504.70M = Rs 2,448.73M, matching the Note 3 aggregate figure exactly (line 649). Actual utilised per Note 3: Rs 1,776.97 million (line 651) — a shortfall of Rs 671.76 million against the FY26 estimate, attributed to "lower operational requirements." Footnote CA certificate reference at lines 658-660 (5th occurrence).

## 14. SECTION 5 — GENERAL CORPORATE PURPOSE UTILISATION STATEMENT (1)

| # | Line | Content | Flags |
|---|------|---------|-------|
| G1 | 663-665 | "Details of utilization of proceeds stated as General Corporate Purpose amount in the offer document: No utilization during the reported quarter." | ZERO_STANDING |

Footnote CA certificate reference at lines 667-669 (6th occurrence).

## 15. CA CERTIFICATE REFERENCES ("peer-reviewed") (10)

| # | Line | Context | Flags |
|---|------|---------|-------|
| CA1 | 217 | Arrangement table, Source column, row A1 (utilization vs disclosures) | CA_CERT_REF |
| CA2 | 248-250 | Arrangement table, Source column, rows A5/A6 (statutory approvals / technical assistance) | CA_CERT_REF |
| CA3 | 271-272 | Footnote below arrangement table — full certificate identification: dated Aug 10, 2026, M/s S K Patodia & Associates LLP, FRN 112723W/W100962 | CA_CERT_REF |
| CA4 | 339-340 | Footnote below Cost of the Object(s) table | CA_CERT_REF |
| CA5 | 460-461 | Footnote below Progress in the Object(s) table | CA_CERT_REF |
| CA6 | 618-619 | Footnote below Deployment of unutilised proceeds table | CA_CERT_REF |
| CA7 | 649-651 | Note 3 body text (source of the Rs 1,776.97M utilised figure) | CA_CERT_REF |
| CA8 | 658-660 | Footnote below Delay in implementation table | CA_CERT_REF |
| CA9 | 667-669 | Footnote below Section 5 GCP utilization statement | CA_CERT_REF |
| CA10 | 686 | Disclaimer (b) — generic reference to "Peer-reviewed Independent Chartered Accountants (or from peer reviewed CA firms)" as a third-party source category | — |

All 9 report-specific references (CA1-CA9) cite the same single certificate: dated August 10, 2026, issued by M/s S K Patodia & Associates LLP, Chartered Accountants, FRN 112723W/W100962, Peer-reviewed Independent Chartered Accountant. No second CA firm or certificate appears anywhere in the document.

## 16. DISCLAIMERS (a)-(n) (14)

| # | Line | Letter | First ~12 words | Flags |
|---|------|--------|--------------------|-------|
| DC1 | 679-683 | a) | "This Report is prepared by Crisil Ratings Limited (hereinafter referred to as..." | — |
| DC2 | 684-687 | b) | "This Report has to be seen in its entirety; the selective review..." | — |
| DC3 | 688-691 | c) | "Nothing contained in this Report is capable or intended to create any legally binding obligations..." | — |
| DC4 | 692-696 | d) | "The MA and its affiliates do not act as a fiduciary..." | — |
| DC5 | 697-700 | e) | "The MA or its affiliates may have other commercial transactions with the entity..." | CONFLICT_OF_INTEREST_LANGUAGE |
| DC6 | 701-704 | f) | "The MA report is intended for the jurisdiction of India only..." | — |
| DC7 | 705 | g) | "Access or use of this report does not create a client relationship..." | — |
| DC8 | 706-707 | h) | "CRL is not aware that any user intends to rely on the report..." | — |
| DC9 | 708-712 | i) | "It is made abundantly clear that the report is not intended to and does not constitute an investment advice..." | — |
| DC10 | 713-717 | j) | "The report comprises professional opinion of CRL as of the date they are expressed..." | — |
| DC11 | 718-726 | k) | "Neither CRL nor its affiliates, third-party providers...guarantee the accuracy, completeness or adequacy..." | — |
| DC12 | 733-735 | l) | "CRL has established policies and procedures to maintain the confidentiality of certain non-public information..." | — |
| DC13 | 736-737 | m) | "Unless required under any applicable law, this report should not be reproduced or redistributed..." | — |
| DC14 | 738-739 | n) | "By accepting a copy of this Report, the recipient accepts the terms of this Disclaimer..." | — |

---

## SUMMARY OF FLAGS RAISED

- DEVIATION_DECLARED — D1, D2, N2 (deviation type + 25-35% range, tied to shareholder-approved postal ballot)
- NEW_OBJECT — C4-C7, P4-P7, N2 (four objects added 24-Jun-2026 via postal ballot, reallocated from Object 1)
- ZERO_STANDING — C4-C7 (original-cost column), P2 (partial), P3 (partial), P4-P7 (full row), G1, FD1-FD2 (non-FD balances, dash cells), FD63 (dash earnings cell) — 5 full-row/statement-level instances plus additional cell-level instances noted inline
- COST_REVISED_DOWN / COST_REVISED_UP — C1, C2 (down); C3 (up)
- DELAY_IN_IMPLEMENTATION — N3, DL1, DL2 (Rs 1,776.97M utilised vs Rs 2,448.73M estimated by FY26, shortfall Rs 671.76M)
- DROPPED_DESCRIPTION — object descriptions table (Section 9) not updated for new Objects 4-7
- CA_CERT_REF — CA1-CA9 (single certificate, 9 citations across the report)
- CONFLICT_OF_INTEREST_LANGUAGE — DC5, and MA declaration paragraph lines 138-141

## TOTAL ROW COUNT ACROSS ALL CATEGORIES

2 (letters) + 3 (signatures) + 3 (report header) + 2 (deviation) + 11 (issuer/issue) + 9 (arrangement) + 10 (cost table) + 3 (notes) + 7 (object descriptions) + 10 (progress table) + 65 (deployment items) + 3 (deployment summary) + 2 (delay table) + 1 (GCP statement) + 10 (CA references) + 14 (disclaimers) = **155 enumerated disclosure units**, all carrying a line number.
