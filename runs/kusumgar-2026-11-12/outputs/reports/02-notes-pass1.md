# 02 NOTES, PASS 1 (FULL EXTRACTION): KUSUMGAR (Kusumgar Ltd), run 2026-11-12

Source: IPO Prospectus dated 2026-07-10, Restated Consolidated Financial Information (FY2024 combined, FY2025 and FY2026 consolidated). Text twin: runs/kusumgar-2026-11-12/inputs/prospectus/Kusumgar_Prospectus_2026-07-10.txt.
Unit: INR million, as printed on the face of every statement and note (Prospectus p.279 onward). No conversion. Anchor form: (Prospectus p.N, Note X), N = PDF page = printed page + 4.
Pages read: 80-81, 271-338 (auditor report, Annexures I-VII, Notes 1-56, other financial information, capitalisation, indebtedness). Nothing else read.
Input gaps carried: annual report ABSENT; three fiscal years only; FY2025-26 standalone audited statements not consumed; CARO report not in corpus (only the CARO extracts reproduced in Annexure VI Part C, p.297).
Rating key: 🟢 clean, 🟡 watch, 🔴 red flag.
Derived figures (ratios, days, percentages) are computed here from anchored inputs and are marked "derived". They are not company disclosures.

---

## 0. ANSWERS TO THE FOUR LOAD-BEARING FACTS

### LB1. Receivables, their ageing FY25 to FY26, and the Mar-2024 "other liabilities"

Receivables (Prospectus p.279 Annexure I; p.302 Note 15):
| | Mar 2026 | Mar 2025 | Mar 2024 |
|---|---|---|---|
| Gross (good + SICR) | 2,395.23 | 629.77 | 453.01 |
| ECL allowance | (62.45) | (68.67) | (30.62) |
| Net receivables | 2,332.79 | 561.10 | 422.39 |
| Revenue from operations (p.280) | 6,920.03 | 7,789.97 | 4,679.08 |
| Debtor days, net / revenue x 365 (derived) | 123.0 | 26.3 | 32.9 |

The 123 vs 26 pair from the brief reproduces. Net receivables rose 1,771.69 (4.2x, derived) while revenue fell 11.2% (derived).

Ageing, "outstanding for following periods from due date of receipts" (Note 15, p.302). Column order as printed: Not Due, Less than 6 months, 6 months to 1 year, 1-2 years, 2-3 years, More than 3 years, Total. The seven-number rows only fit this order.
| Bucket | Mar 2026 | Mar 2025 | Mar 2024 |
|---|---|---|---|
| Not due | 1,719.06 | 453.86 | nil |
| Overdue under 6 months | 648.08 | 130.08 | 425.91 |
| 6 months to 1 year | 7.94 | 26.92 | 10.18 |
| 1-2 years | 9.25 | 6.67 | 8.17 |
| 2-3 years | 2.72 | 5.78 | 6.65 (2.38 + disputed 4.27) |
| More than 3 years | 8.19 (3.92 + disputed SICR 4.27) | 6.46 (2.19 + disputed SICR 4.27) | 2.10 |
| Total gross | 2,395.23 | 629.77 | 453.01 |
Mar 2026 undisputed good row: 1,719.06 / 648.08 / 7.94 / 9.25 / 2.72 / 3.92 = 2,390.96; disputed SICR 4.27 in the over-3-years column (p.302).

- Derived: overdue at Mar 2026 = 648.08 + 7.94 + 9.25 + 2.72 + 8.19 = 676.18, or 28.2% of gross. Mar 2025: 175.91, or 27.9%. Mar 2024: 453.01, or 100% (no "not due" balance printed). Overdue more than 6 months: 28.10 (1.2%) at Mar 2026; 45.83 (7.3%) at Mar 2025; 27.10 (6.0%) at Mar 2024.
- Reading: the overdue SHARE is flat (about 28%), but overdue rupees quadrupled (175.91 to 676.18), and 1,719.06 (71.8%) is "not due". Credit terms are "generally 30 to 45 days" (Note 44(c), p.321). A not-due balance of 1,719.06 on 45-day terms means roughly 1,719 of invoices raised in the last 45 days of the year, equal to 24.8% of full-year revenue 6,920.03 (derived). Either the final weeks were very heavily billed, or the effective terms are longer than 45 days. Quarterly revenue is not in these notes. NOT FOUND IN DOCUMENT. 🔴 (build and terms mismatch)
- ECL cover on gross: Mar 2024 6.8%, Mar 2025 10.9%, Mar 2026 2.6% (derived); allowance as % of overdue balance at Mar 2026 9.2% (derived). FY26 ECL movement: addition 0.04, reversal (6.23) credited to Other income (Note 48(b), p.325; Note 31, p.310). The matrix is "based on the Group's historical observed default rates" and "no adjustment for forward looking factors is carried" (Note 48(b), p.325). The allowance fell as receivables quadrupled. 🔴
- Cash flow: receivables absorbed (1,616.28) in FY26 (p.283 Annexure IV).
- Foreign currency receivables, unhedged (Note 48(a)(ii), p.324): USD receivables 13.23 million USD = INR 1,627.72 at Mar 2026 (Mar 2025: 3.22 million = 281.49; Mar 2024: 2.04 million = 169.90). INR 1,627.72 is 69.8% of net receivables (derived). Internal check (derived): 1,627.72 / 13.23 = 123.0 INR per USD, against 87.4 (Mar 2025), 83.3 (Mar 2024), 92.8 (Mar 2026 USD payables: 306.11 / 3.30) and 95.3 (Mar 2026 USD forwards: 142.97 / 1.50). The 123 figure does not match the other FY26 rates in the same note. Cause NOT FOUND IN DOCUMENT. Intra-group trade receivable from Kusumgar Middle East FZ LLC is 377.27 at Mar 2026 (Note 43, p.319); 1,627.72 less 377.27 = 1,250.45, or 94.5 per USD, which would fit the other rates. This is an arithmetic observation only. 🟡
- FX gain 147.91 in Other income (Note 31, p.310) equals, to the paisa, "unrealized foreign exchange gain (147.91)" deducted in the cash flow (p.283). All of the FY26 FX gain is unrealised. 10% USD move = +/-146.46 on PBT (Note 48(a), p.325). 🟡
- Single-customer receivables: no table. NOT FOUND IN DOCUMENT. Related-party receivables: only 17.70 from Siddharth Kusumgar (IPO cost reimbursement; Note 43, p.318; Note 19, p.303).
- Same window, other assets: current "Loans" 155.69 to "other parties" at Mar 2025, nil at Mar 2026 (no counterparty, rate or tenor, Note 18, p.303); current security deposits 234.43 at Mar 2025 falling to 48.02 (Note 19, p.303). Cash flow shows (380.76) outflow in FY25 and 320.36 inflow in FY26 on "loans and other financial assets" (p.283). Counterparty NOT FOUND IN DOCUMENT. 🟡

What the large Mar-2024 "other liabilities" balance was (balance sheet p.279):
- Other current liabilities 1,307.87 at Mar 2024 (Note 28, p.309) = Advance from customers (contract liabilities) 1,264.61 + CSR liability 8.22 + statutory dues 35.04. The large balance was CUSTOMER ADVANCES, 1,264.61 (96.7% of the line, derived).
- Why it fell by Mar 2025: the contract liability roll-forward (Note 44(c), p.321) shows FY25 opening 1,264.61, "revenue recognised during the year (1,264.61)", closing 27.44. The whole advance was converted into FY25 revenue, 16.2% of FY25 revenue from operations 7,789.97 (derived). FY24 opening was 29.18, so the 1,264.61 was received in FY24.
- Second large item at Mar 2024, Other financial liabilities 1,337.32 (Note 26, p.309): Purchase consideration payable 1,118.53 plus expense payables 159.37. The 1,118.53 is the cash consideration for the common-control acquisition of Engineered Coated Fabric Private Limited (ECFPL) from the two promoters (Note 51, p.330). Cash flow FY25 shows "Increase/(Decrease) in other financial liabilities (1,260.89)" and "other liabilities (1,211.02)" inside OPERATING activities (p.283), with no acquisition line in investing. FY24 operating cash flow of 2,009.64 carried +1,265.54 from the other-liabilities line. Other bank balances (fixed deposits) were 1,106.13 at Mar 2024 and 106.93 at Mar 2025 (Note 17, p.303); FY25 "proceeds from bank deposits" 1,030.99 (p.283). [INFERENCE: the FY24 customer advance was parked in fixed deposits, and those deposits paid the promoters' consideration in FY25. The notes do not state this chain.]

### LB2. Revenue disaggregation and customer concentration

Revenue from operations (Note 30, p.310): FY26 6,920.03 / FY25 7,789.97 / FY24 4,679.08.
By product (Note 44(a), p.320):
| | FY26 | FY25 | FY24 |
|---|---|---|---|
| Fabrics and solutions | 5,709.72 | 7,377.18 | 4,485.46 |
| Ancillary products and others | 515.29 | 308.80 | 60.19 |
| Services | 523.13 | 14.97 | 11.29 |
| Gross revenue from contracts | 6,748.15 | 7,700.94 | 4,556.94 |
| Other operating income | 171.89 | 89.02 | 122.14 |
Fabrics and solutions fell 22.6% in FY26 (derived). Services rose from 14.97 to 523.13. Nature of the services, customers and contract terms: NOT FOUND IN DOCUMENT. Cost of service 84.47 appears as a new P&L line (p.280), so service margin before other costs is 83.9% (derived). Services are recognised over time (Note 3.14, p.292). Of the services, 312.61 is an intra-group sale to Kusumgar Middle East FZ LLC (eliminated, Note 43, p.319); the external 523.13 is all booked as India (Note 44(a), p.320). 🟡

Geography (Note 44(a), p.320; Note 45(a), p.321):
| | FY26 | FY25 | FY24 |
|---|---|---|---|
| India (incl. services) | 4,049.70 | 5,912.88 | 3,389.51 |
| Outside India | 2,698.44 | 1,788.07 | 1,167.43 |
India fabrics and solutions: 3,126.09 vs 5,622.29, down 44.4% (derived). India sales excluding services: 3,526.57 vs 5,897.91, down 40.2% (derived). Outside India fabrics and solutions: 2,583.63 vs 1,754.89, up 47.2% (derived). Outside India is 40.0% of FY26 contract revenue (derived), 23.2% in FY25. Country detail FY26 / FY25 / FY24: USA 628.03 / 678.94 / 465.58; Germany 757.24 / 403.52 / 276.60; Sri Lanka 349.63 / 102.79 / nil; France 193.37 / 208.24 / 72.35; Turkey 101.33 / nil / nil; Singapore 93.84 / nil / nil; Bangladesh 92.91 / nil / 41.70; South Africa 70.43 / 62.55 / 67.20; Others 411.66 / 332.02 / 243.99.

Customer concentration (Note 45(c), p.321), customers above 10% of revenue from operations:
| | FY26 | FY25 | FY24 |
|---|---|---|---|
| Customer one | 0.00% | 24.97% | 46.00% |
| Customer two | 0.00% | 27.97% | none printed |
Customers are not named; no sector or product is given. FY25 top two = 52.9% of revenue (derived), about 1,945 and 2,179 (derived from 24.97% and 27.97% of 7,789.97). FY24 customer one about 2,152 on 4,679.08 (derived). In FY26 no customer exceeds 10%. 🔴 for the concentration history. The India fabrics decline of 2,496 (derived) is of the same order as the two FY25 customers' combined size. [INFERENCE: the FY26 revenue fall comes from those customers; the notes do not say so.]
Contract balances (Note 44(c), p.321): trade receivable terms 30 to 45 days; advances from customers 87.59 / 27.44 / 1,264.61 (Mar 26/25/24); no contract assets. No unsatisfied performance obligations; contracts are "for a shorter duration" (p.321). No order-book figure in the notes.

Segment reporting: Note 3.18 (p.293) and Note 45 (p.321) say a single operating segment (manufacturing of technical textile fabrics). The same Note 45 paragraph also says "Within India" and "Outside India" "have been identified as operating and reportable segments". The two statements conflict in the printed text. 🟡 (disclosure quality).

### LB3. Related party transactions and anything tied to the selling shareholders
Full table in Section 2. In short:
- The promoters (Siddharth Kusumgar 60.98%; Sapna Kusumgar 29.13%) were the sellers of ECFPL to the company for cash 1,118.53 (Note 51, p.330), the largest related-party flow in the 3 years (settled in FY25 per the cash flow, see LB1).
- Promoter loans to the company: FY26 Siddharth 250.00 taken and 250.00 repaid; Sapna 50.00 and 50.00; FY25 Siddharth 194.09 and 194.09; Sapna 90.08 and 90.08; interest paid 5.83 (FY26) and 2.26 (FY25) (Note 43, p.318; Note 35, p.310). Taken and repaid inside each year; rate and tenor NOT FOUND IN DOCUMENT.
- IPO costs: professional fees 73.17 and auditors 8.31 = 81.48 were kept out of expenses as "recovered from selling shareholders" (Note 37, p.311) and 81.48 was reimbursed by Siddharth Kusumgar (Note 43, p.318). A further 7.03 prepaid IPO cost at Mar 2025 was recovered in FY26 (Note 20, p.303). 17.70 was still receivable from Siddharth Kusumgar at Mar 2026 (Note 19, p.303; Note 43, p.318).
- Promoter shareholding fell in FY26 with the equity share count unchanged at 10,14,90,000 (Note 21, pp.304-305): Siddharth 6,56,94,630 to 6,18,84,021 (-38,10,609); Sapna 3,13,99,170 to 2,95,61,148 (-18,38,022); promoter-group "Siddharth Y" 43,35,000 to 34,85,000 (-8,50,000). Total 64,98,631 shares, 6.40% of equity (derived). Buyer(s) NOT FOUND IN DOCUMENT in the notes. The 35,01,372 CCPS were new issues (primary), not these transfers.
- Credit support: HDFC term loans secured by personal guarantees of Yogesh Kusumgar and Siddharth Kusumgar and a corporate guarantee of 4S Holding (Note 23 Note 1, p.307; p.337). No guarantee fee disclosed.
- Every related-party transaction is stated to be at arm's length (pp.317, 319), with no benchmark cited. 🟡

### LB4. Borrowings, security, covenants
In Section 7 below.

---

## 1. ACCOUNTING POLICIES AND CHANGES (Notes 1-5, Annexure VI)

1. Basis of preparation (Note 2, pp.285-286): FY26 and FY25 are consolidated Ind AS statements; FY24 is an AUDITED SPECIAL PURPOSE COMBINED statement (parent standalone Ind AS plus ECFPL special-purpose Ind AS), approved by the board 4 Sept 2025 (auditor report pp.273-274; Note 2(a), p.285). ECFPL was acquired 5 Dec 2024 under common control (Note 2, p.286; Note 51, p.330) and pooled from the earliest period (transition date 1 Apr 2022 elected for ECFPL; statutory date 1 Apr 2023). FY24 is not a company-audited consolidated year. 🟡
2. Restatement: Annexure VI Part A shows NIL adjustments to equity and total comprehensive income in all three years (audit qualifications, prior-period items, accounting-policy changes, deferred tax) (p.296). Part B: no regroupings (p.296). "Restated" equals audited. 🟢
3. Auditor opinions: no qualification; Emphasis of Matter on the FY24 special-purpose basis only (pp.276-277, p.296). Predecessor auditor for FY24 and earlier was Mamta K Mehta and Associates; MSKA & Associates LLP audits from FY25 (p.277). Other auditors: Chaturvedi Sohan & Co (ECFPL), Parikh & Majmudar (Kusumgar Composites Private Limited, FY26) (pp.273-274). Who audited Kusumgar Middle East FZ LLC: NOT FOUND IN DOCUMENT (MSKA says it did not audit "2 subsidiaries", p.275). 🟡
4. Audit trail (Annexure VI Part C, p.297; auditor report p.275): FY26 audit trail enabled at database level only from 27 July 2025; FY25 application-level trail enabled from 25 Jun 2024 (Sales), 11 Jan 2025 (Purchase), 12 Feb 2025 (Customer module), not at database level through the year, prior-year trail not preserved; FY24 not enabled throughout. The FY25 auditor was also "unable to comment" whether daily backups were taken (p.297). 🟡
5. CARO extracts (p.297): (a) FY25 quarterly stock statements filed with banks disagreed with books: Jun-24 945 vs 955 (difference (10)); Sep-24 1,112 vs 1,049 (63); Dec-24 1,168 vs 1,289 (121). The FY26 remark says differences "are primarily due to changes in the valuation of closing inventories". (b) "funds raised on short term basis in the form of cash credit facility from banks aggregating to INR 657.27 millions has been used for long-term purposes" (clause ix(d); the year is not clear from the printed layout). (c) statutory dues: "slight delay in a few cases" in all years. 🟡
   Note 23 (p.307) says quarterly returns filed with banks "are in agreement with the books of account", while the CARO extract lists differences. The two cover different periods and are not reconciled in the notes.
6. Revenue recognition (Note 3.14, p.292): goods at a point in time on shipment or delivery; services over time; net of variable consideration. Export incentives (RoDTEP, duty drawback) and government grants sit in Revenue from operations as Other operating income, accrued post-export (Note 3.14, p.293). FY26: grants 77.15, duty drawback 44.05, RoDTEP 27.40, scrap 23.29 = 171.89 (Note 30, p.310). 🟡 Grants on assets may also be netted from asset cost (Note 3.03, p.287): FY26 subsidy of 88.22 was deducted from plant and machinery gross block (Note 6, p.298).
7. Depreciation lives (Note 3.01, p.287): buildings 3-30 years; plant and machinery 7.5-15; electrical 10; furniture 10; vehicles 8-10; office and factory equipment 5; computers 3; leasehold improvements lower of lease term and life. Software 6 years (Note 3.03, p.287). No change in lives disclosed. 🟢
8. Capitalisation (Notes 3.02-3.03, p.287; Note 3.19, p.294): borrowing cost capitalised on qualifying assets: 27.52 FY26, 0.29 FY25, 13.70 FY24 (Note 6, p.298). Lease interest 0.76 and ROU depreciation 0.50 capitalised to CWIP (Note 7, p.299). No capitalisation threshold stated. 🟢
9. Impairment (Note 3.04, p.288): standard Ind AS 36 text; no CGU growth or discount assumptions; no impairment recorded. NOT FOUND IN DOCUMENT for CGU-level assumptions. No goodwill. 🟢
10. ECL (Note 3.10, p.290; Note 48(b), p.325): lifetime ECL, simplified approach, provision matrix on historical default rates, no forward-looking adjustment. Matrix percentages by bucket: NOT FOUND IN DOCUMENT. 🟡 (see LB1)
11. Leases (Note 3.12, p.291; Note 7, p.299): weighted average incremental borrowing rate 8.60%. ROU asset 705.76 / 605.92 / 491.58; lease liability 648.76 / 556.86 / 422.69 (Mar 26/25/24). FY26 additions 213.43 (ROU) and 206.68 (liability); deletion 38.81; gain on lease termination 2.96 (Note 31, p.310). Variable lease payments 21.48; short-term lease rent 4.27 (FY26) (Note 7(c), p.299). 🟢
12. Transaction costs on long-term borrowings amortised straight line, not EIR, because "all at a variable interest rate" (Note 3.10, p.291). Immaterial (unwinding 0.60). 🟢
13. Corporate guarantees given are deferred income, amortised (Note 3.11, p.291). 🟢
14. New standards (Note 5, p.295): no supplier finance; Ind AS 1 and 21 amendments no effect; Pillar Two not in scope. New Labour Codes (effective 21 Nov 2025) "has not resulted in any material increase" in obligations (Note 24.1, p.308). 🟢
15. Tax posture (Note 38 footnote, p.312): Indian entities on s.115BAA at 25.17%. Kusumgar Middle East FZ LLC (Dubai) is treated as tax resident in India on place of effective management and taxed at 38.30%. 🟡 (Section 10)
16. Foreign currency (Note 3.07, p.288): monetary items at closing rate; exchange differences to P&L (Other income). Forwards not hedge-designated; FVTPL (Note 3.10, p.291; Note 26, p.309). 🟢
17. Going concern (Note 2(f), p.287): going-concern basis, "no material uncertainty exists". No other going-concern language in pp.271-338. 🟢
18. Inventory (Note 3.05, p.288): lower of cost and NRV; overheads on normal capacity. Cost formula (FIFO, weighted average) NOT FOUND IN DOCUMENT. 🟡 (minor)

---

## 2. RELATED PARTY TRANSACTIONS (Note 43, pp.317-319; summary pp.80-81)

Unit INR million. % of revenue from operations uses 6,920.03 / 7,789.97 / 4,679.08 (p.280) and matches the prospectus summary column (p.81).

### Related parties (Note 43(a)-(b), p.317)
Subsidiaries: Engineered Coated Fabric Private Limited (100%); Kusumgar Composites Private Limited (100%, wholly owned subsidiary w.e.f. 27 March 2026, new this year); Kusumgar Middle East FZ LLC (100%, UAE).
KMP-influenced enterprises: Specialty Fabrics Pvt Ltd; Concord Weaving & Preparatory Pvt Ltd; Kusumgar Technomic Fabrics Pvt Ltd; V B Kusumgar & Co Pvt Ltd; 4S Holdings; Kusumgar Holdings LLP; Paraborne Systems LLP; Toray Kusumgar Advanced Textile Pvt Ltd; Pertex Solution LLP.
KMP and relatives: Yogesh Kusumgar (Director until 4 Mar 2025; close family member of KMP), Siddharth Kusumgar (Chairman and MD), Kiran Shah (Director until 4 Mar 2025), Ankur Kothari (Executive Director and CEO), Sapna Kusumgar (MD), Kinnar Mehta (CFO from 1 Jan 2025), Naresh Patel (CFO until 9 Dec 2024), Devanand Mojidra (CS from 22 Feb 2025), independent directors Deepti Gupta and Kaushal Sampat (from 17 Mar 2025) and Nihar Parikh (from 10 Jun 2025); relatives Amita Soni, Babita Kusumgar, Sushmi Doshi.
Only Specialty Fabrics, 4S Holdings, Paraborne Systems LLP and Toray Kusumgar carry transactions or balances. The other listed enterprises show none.

### Transactions (Note 43(f), p.318)
| Party | Relationship | Nature | FY26 | % rev | FY25 | % rev | FY24 | % rev | YoY FY26/FY25 |
|---|---|---|---|---|---|---|---|---|---|
| Specialty Fabrics Pvt Ltd | KMP-influenced | Job work sales | nil | | 3.33 | 0.04% | 4.89 | 0.10% | n/a |
| Specialty Fabrics Pvt Ltd | same | Yarn purchase | 39.84 | 0.58% | 4.28 | 0.05% | 0.17 | 0.00% | 9.3x |
| Specialty Fabrics Pvt Ltd | same | Plant and machinery purchase | 25.70 | 0.37% | nil | | nil | | new |
| Specialty Fabrics Pvt Ltd | same | Rent paid | 2.00 | 0.03% | 6.00 | 0.08% | 6.00 | 0.13% | -66.7% |
| Paraborne Systems LLP | KMP-influenced | Fabric sales | nil | | nil | | 0.88 | 0.02% | n/a |
| Paraborne Systems LLP | same | Stores and spares sale | nil | | nil | | 2.76 | 0.06% | n/a |
| Paraborne Systems LLP | same | Stores and spares purchase | nil | | nil | | 19.40 | 0.41% | n/a |
| Paraborne Systems LLP | same | Interest received | nil | | nil | | 0.08 | 0.00% | n/a |
| 4S Holdings | KMP-influenced | Rent paid | 12.89 (p.81 summary shows 12.98) | 0.19% | 11.73 | 0.15% | 9.66 | 0.21% | +9.9% |
| Amita Soni | Relative of KMP | Rent paid | 2.40 | 0.03% | 1.43 | 0.02% | 1.39 | 0.03% | +67.8% |
| Babita Kusumgar | Relative of KMP | Rent paid | 2.40 | 0.03% | 1.43 | 0.02% | 1.39 | 0.03% | +67.8% |
| Sushmi Doshi | Relative of KMP | Rent paid | 2.40 | 0.03% | 1.43 | 0.02% | 1.39 | 0.03% | +67.8% |
| Yogesh Kusumgar | Former Director / relative of KMP | Consultant fees | 6.00 | 0.09% | nil | | nil | | new |
| Kinnar Mehta | CFO (from 1 Jan 2025) | Consultant fees (pre-appointment) | nil | | 3.60 | 0.05% | nil | | n/a |
| Kiran Shah | Former Director | Consultant fees | nil | | 6.25 | 0.08% | nil | | n/a |
| Siddharth Kusumgar | CMD, promoter | Loan taken | 250.00 | 3.61% | 194.09 | 2.49% | nil | | +28.8% |
| Sapna Kusumgar | MD, promoter | Loan taken | 50.00 | 0.72% | 90.08 | 1.16% | nil | | -44.5% |
| Siddharth Kusumgar | | Interest paid | 4.83 | 0.07% | 2.19 | 0.03% | nil | | 2.2x |
| Sapna Kusumgar | | Interest paid | 1.00 | 0.01% | 0.07 | 0.00% | nil | | 14.3x |
| Siddharth Kusumgar | | Loan repaid | 250.00 | 3.61% | 194.09 | 2.49% | nil | | |
| Sapna Kusumgar | | Loan repaid | 50.00 | 0.72% | 90.08 | 1.16% | nil | | |
| 4S Holdings | | Deposit given | nil | | 0.10 | 0.00% | nil | | |
| Amita Soni, Babita Kusumgar, Sushmi Doshi | | Deposit given (each) | nil | | 0.10 each | 0.00% | nil | | |
| 4S Holdings | | Deposit received | nil | | 17.50 | 0.22% | nil | | |
| Siddharth Kusumgar | | Reimbursement of IPO expenses received | 81.48 | 1.18% | nil | | nil | | new |
| Total as printed | | | 780.94 | | 627.98 | | 48.01 | | |
Percentages per the prospectus summary (p.81). The printed total 780.94 includes loans taken AND repaid (600.00 gross, circular). Excluding loans taken and repaid (derived): 180.94 in FY26 (2.6% of revenue) and 59.64 in FY25 (627.98 less 568.34). Corporate guarantee given to a related party: 75.00 at Mar 2024, nil afterwards (Note 40, p.314); beneficiary NOT FOUND IN DOCUMENT.

### Balances (Note 43(g), pp.318-319)
- Deposit given: 4S Holdings 6.10 / 6.00 / 23.50 (Mar 26/25/24); Amita Soni, Babita Kusumgar, Sushmi Doshi 0.10 each (FY26, FY25). Total 6.40 / 6.30 / 23.50.
- Receivable: Siddharth Kusumgar 17.70 (Mar 26 only).
- Other investment: Toray Kusumgar Advanced Textile Pvt Ltd 154.19 / 149.66 / 121.79, FVTOCI Level 3. 72,000 equity shares of face value INR 1,000 (Note 10, p.301); ownership % NOT FOUND IN DOCUMENT. Purchase cost 108.00 in FY24 (cash flow, p.283). FVTOCI gains 4.52 (FY26) and 27.87 (FY25) (p.280).
- Payables: Paraborne Systems LLP 19.18 / 19.19 / 19.19 (unchanged at three year-ends; FY24 purchase from it was 19.40); 4S Holdings 4.43; Yogesh Kusumgar 0.45. Total 24.06 / 19.19 / 19.19. 🟡

### KMP remuneration (Note 43(c)-(e), p.317)
Short-term benefits 66.29 / 66.91 / 51.61; share-based payment 199.16 / 34.57 / nil; others nil / 9.85 / 5.4; total 265.45 / 111.33 / 57.01. FY26 individuals: Siddharth Kusumgar 14.64; Sapna Kusumgar 14.64; Ankur Kothari 25.42; Kinnar Mehta 7.96; Devanand Mojidra 3.63. All KMP share-based payment (199.16) is Ankur Kothari's, 97.5% of the FY26 ESOP expense 204.33 (derived).

### Intra-group items eliminated (Note 43(h), p.319)
ECFPL: job work expenses 11.76 / 72.71 / 110.71; fabric sales to ECFPL 111.52 / 277.38 / 360.47; fabric purchase 262.71 / 365.48 / 111.47; chemical and packing sales 5.48 / 30.20 / 29.59.
Kusumgar Middle East FZ LLC: sale of service 312.61 (FY26; nil prior); loan given 204.33 (FY26), loan balance 213.81 (Mar 26) vs 9.48 (Mar 25); interest received 12.64 / 0.47; interest accrued 14.18; trade receivable 377.27 (Mar 26). FZ LLC net assets are 70.73 at Mar 2026 against 605.26 due from it (377.27 + 213.81 + 14.18, derived; Note 50, p.328). 🟡

Signals:
- Revenue from promoter-linked entities: only job work with Specialty Fabrics, ended after FY25. Non-arm's-length signals provable from the notes: none. A blanket arm's-length statement with no benchmarking. 🟡
- Related-party purchases are small: Specialty Fabrics yarn and machinery FY26 65.54, 0.9% of revenue (derived).
- Rent to promoter family: 4S Holdings 12.89 + Specialty Fabrics 2.00 + three relatives 7.20 = 22.09 FY26 (derived), against total rent expense 25.75 (Note 37, p.311). Rent to relatives rose 67.8%.
- A former Director (Yogesh Kusumgar) received 6.00 as consultant in FY26 and is a personal guarantor of the HDFC term loans (Note 23, p.307).
- Royalty expense 88.61 / 129.64 / 325.08 (Note 37, p.311). The payee is not named and no royalty counterparty is in the related-party list. NOT FOUND IN DOCUMENT. 🟡 (royalty fell from 6.9% to 1.3% of revenue, derived).
- New related parties this year: Kusumgar Composites Private Limited (investment 0.10, net assets 0.08; pp.319, 328); consultant arrangement with Yogesh Kusumgar (6.00).
- Loans to promoter entities: none. Loans taken from promoters: gross 300.00 FY26 and 284.17 FY25, each repaid the same year.

---

## 3. CONTINGENT LIABILITIES AND COMMITMENTS (Notes 40-41, p.314; summary p.80)
| Nature | Mar 2026 | Mar 2025 | Mar 2024 | Stage / assessment |
|---|---|---|---|---|
| Bank guarantee | 1,038.77 | nil | nil | Beneficiary and purpose NOT FOUND IN DOCUMENT |
| Letter of credit | 40.79 | 53.11 | 47.12 | Not stated |
| Income tax demand | 10.14 | nil | nil | Stage and forum NOT FOUND IN DOCUMENT |
| Corporate guarantee given to related party | nil | nil | 75.00 | Beneficiary NOT FOUND IN DOCUMENT |
| Total contingent liabilities (derived) | 1,089.70 | 53.11 | 122.12 | |
| Capital commitments (plant and machinery, Note 41) | 58.33 | 852.70 | 570.19 | |
| Total as shown on p.80 | 1,148.03 | | | |
- Derived: contingent liabilities 1,089.70 = 21.7% of net worth 5,029.54 (Mar 2026). The bank guarantee alone = 20.7%, a single item above 10% of net worth. 🔴 on size, newness and absent narrative. The prospectus shows bank guarantees outstanding 967.81 at 31 May 2026 against a 1,600 sub-limit, and letters of credit 22.86 (p.336).
- Fixed deposits are pledged against these: against bank guarantees 53.83 (non-current) + 5.54 (other bank balances) + 19.53 (current) at Mar 2026; against letters of credit 8.21 + 17.50 (Notes 11, 17, 19, pp.301, 303).
- Tax disputes: no composition beyond the 10.14. Litigation provisions: none disclosed in these pages. Guarantees for subsidiaries: none disclosed in FY26.
- Capital commitments fell 93% from 852.70 to 58.33 (derived); the capex programme is largely complete. 🟢
- Ratings: bank guarantee 🔴; income tax demand 🟢; capital commitments 🟢.

---

## 4. TRADE RECEIVABLES: see LB1. Additional items.
- Pledge: receivables are security for lenders (Note 15, p.302; Note 23 note 3, p.307).
- Allowance reconciliation (Note 48(b), p.325): opening 20.78 (FY24) / 30.62 (FY25) / 68.67 (FY26); additions 9.84 / 38.05 / 0.04; reversal nil / nil / (6.23); closing 30.62 / 68.67 / 62.48. Note 15 balance-sheet figure is 62.45 (0.03 difference). 🟢 Bad debts 3.67 (FY25); sundry balances written off 1.23 / 2.50 / 3.05 (Note 37, p.311).
- A 4.27 disputed receivable older than 3 years carries "significant increase in credit risk" in all three years (Note 15, p.302). 🟡 (minor)
- Security deposits: "credit risk on certain aged security deposits has increased significantly and these balances are considered credit-impaired" (Note 48(b), p.325), with allowance nil in FY25 and FY26 and 0.80 written off in FY24. A 6.27 provision for doubtful advances was booked in FY26 (Note 37, p.311). 🟡
- Receivable days trend (derived): 32.9 (FY24), 26.3 (FY25), 123.0 (FY26).
- Cash conversion (derived from p.283): cumulative operating cash flow FY24-FY26 = 2,009.64 + (1,549.76) + 282.58 = 742.46 against cumulative profit 2,945.84 = 25.2%. FY26 alone: operating cash flow 282.58 vs EBITDA 1,878.50 (p.333) = 15.0%. 🔴

---

## 5. INVENTORY (Note 14, p.301; Note 33, p.310)
| | Mar 2026 | Mar 2025 | Mar 2024 |
|---|---|---|---|
| Raw material | 488.12 | 510.56 | 726.11 |
| Semi-finished fabric | 318.04 | 235.27 | 234.95 |
| Finished fabric | 993.10 | 556.75 | 445.31 |
| Stores and spares | 149.32 | 66.44 | 30.74 |
| Total | 1,948.58 | 1,369.02 | 1,437.11 |
- Finished fabric +78.4% (derived) in FY26 while revenue fell 11.2%. Total inventories +42.3%. Stores and spares up 2.2x. Raw material includes stock in transit 31.94 / 16.30 / 151.13. Change in FG and semi-finished inventories (P&L): (519.12) FY26, (111.76) FY25, (232.62) FY24 (Note 33).
- Inventory days on revenue (derived): 102.8 (FY26), 64.1 (FY25), 112.1 (FY24).
- Write-down of inventory in P&L: 117.73 FY26, 39.57 FY25, 180.45 FY24 (Note 14(a), p.301): 1.7% of FY26 revenue and 3.9% of FY24 revenue (derived). P&L line carrying it and the reason for the write-downs: NOT FOUND IN DOCUMENT. Obsolescence breakdown: NOT FOUND IN DOCUMENT. 🟡
- FY25 bank stock statement differences up to 121 against books (Section 1, item 5). 🟡
- Rating: finished goods build on falling sales with repeated write-downs 🟡; with the receivable build, working-capital absorption is the central issue 🔴 (Section 4).

---

## 6. INVESTMENTS (Notes 10, 18, 19, 46, 50; pp.301, 303, 322-329)
- Non-current investments 154.20 / 149.67 / 121.80; all unquoted; no impairment (Note 10, p.301). Toray Kusumgar Advanced Textile Pvt Ltd 72,000 shares 154.19 / 149.66 / 121.79 (FVTOCI, Level 3); bank co-operative shares (Saraswat Co-operative Bank 1,000 shares; SVC Bank 100; Shamrao Vithal 100) 0.00 to 0.01.
- Toray valuation (Note 46, p.323): DCF; discount rate 14.00% (Mar 26) vs 17.60% (Mar 25) vs 13.30% (Mar 24); growth 5.00% / 5.00% / 0.50%; beta 1.36 / 1.5 / 1.2; market premium 6.80% / 6.84% / 6.50%. Sensitivities printed: discount rate +/-1% moves fair value by -31.41 / +40.33 for one year-end and -13.68 / +16.15 and -9.06 / +10.60 for others; the year-to-block mapping is garbled in the text layer. Gains through OCI: 4.52 (FY26), 27.87 (FY25). 🟡 (Level 3; investee is a related party).
- Subsidiaries (Note 50, p.328): ECFPL 100% (manufacturing and trading of fabrics); Kusumgar Composites Private Limited 100% (FRP, carbon fibre composites for aerospace, automotive, marine; investment 0.10); Kusumgar Middle East FZ LLC 100% (textile trading; investment 2.37). Standalone carrying value of ECFPL 1,118.53 (eliminated).
- FY26 profit by entity: Parent 881.26; ECFPL 42.28; FZ LLC 67.60; Kusumgar Composites (0.02); consolidation adjustment (9.13); total 981.99 (Note 50.2, p.328). FY25: Parent 1,089.12; ECFPL 31.85; FZ LLC (1.08). FY24: Parent 811.44; ECFPL 33.85; FZ LLC (1.37) (p.329). Net assets Mar 2026: Parent 5,928.16 (117.87%); ECFPL 154.18; FZ LLC 70.73; consolidation adjustments (1,123.63).
- Loans and ICDs: "Loans to other parties" 155.69 at Mar 2025, nil Mar 2026 (Note 18, p.303); lender names, rate and tenor NOT FOUND IN DOCUMENT. Intra-group loan to FZ LLC 213.81. Bank deposits with maturity above 12 months: non-current 105.87, current 75.00 (Notes 11, 19). 🟡 for the unexplained 155.69.
- New entity: Kusumgar Composites (27 Mar 2026). Loss-making subsidiaries: FZ LLC lost 1.08 (FY25) and 1.37 (FY24), earned 67.60 in FY26; Kusumgar Composites (0.02).

---

## 7. BORROWINGS (Note 23, p.307; Notes 47-48, pp.324-325; pp.335-338)

Totals (Note 23, p.307):
| | Mar 2026 | Mar 2025 | Mar 2024 |
|---|---|---|---|
| Term loan from bank (gross) | 1,173.73 | 881.68 | 462.47 |
| Vehicle loan (gross) | 21.45 | 33.49 | 17.79 |
| Non-current borrowings (net of current maturities) | 851.19 | 757.64 | 348.05 |
| Working capital demand loan | 328.39 | 1,430.50 | 35.52 |
| Packing credit foreign currency loans | 279.52 | 73.80 | 245.44 |
| Buyers credit | nil | 16.02 | nil |
| Cash credit | 423.69 | 18.48 | nil |
| Current maturities, term loan (incl. bank interest payable) | 340.12 | 156.53 | 131.74 |
| Current maturities, vehicle loan | 12.91 | 12.04 | 4.58 |
| Current borrowings | 1,384.63 | 1,707.37 | 417.28 |
| Total borrowings (Note 47, p.324) | 2,235.83 | 2,465.01 | 765.33 |
Note 23 reconciles to the capitalisation statement: current 1,040.63 (1,031.60 plus 9.03 interest) and non-current incl. current maturities 1,195.19, total 2,235.82 (p.335).
- Term loans, all HDFC Bank (Note 23 Note 1, p.307), rates 7.20% to 8.34% (four loans) and 7.60% to 8.60% (fifth). Outstanding Mar 26 / Mar 25 / Mar 24: loan 1: 38.54 / 69.36 / 100.18; loan 2: nil / 3.00 / 9.00; loan 3: 5.18 / 12.08 / 18.99; loan 4: 180.01 / 269.92 / 334.30; loan 5: 950.00 / 527.32 / nil. Total sanctioned term loans 1,665 (p.307). Instalment periods printed: 29 Jun 2020 to 05 May 2027; 18 Jun 2020 to 13 Sep 2025; 31 Dec 2021 to 31 Dec 2026; 31 Mar 2022 to 31 Mar 2028; 28 Jan 2025 to 28 Jan 2031 (the mapping of period to loan is by print order and is not labelled). Year-by-year principal schedule for five years: NOT FOUND IN DOCUMENT. Nearest: current maturities 331.08 (term) + 12.91 (vehicle) within 12 months; borrowings 1,384.63 within 1 year, 851.19 in 1-5 years, nil beyond (Note 48(c), p.325).
- Vehicle loans: 6.7%, 7.6%, 7.9%, 8.6%; lenders Daimler Financial Services India and HDFC Bank; outstanding 21.45 / 33.49 / 17.79; maturities 04-May-27 and 05-Nov-27 (p.307).
- Working capital loans 7.80% to 8.60%, secured by hypothecation of raw material, finished and semi-finished goods and book debts (Note 3, p.307).
- Fixed vs floating: long-term borrowings "all at a variable interest rate" (Note 3.10, p.291); rate range 6.5% to 8.60% (p.336).
- Security (Note 23 Note 1, p.307; p.337): exclusive charge on land and buildings at Tadkeshwar and Mahuvej (Surat); exclusive charge on plant and machinery bought from the term loan; second pari passu charge on current assets; corporate guarantee of 4S Holding; fixed deposit of INR 125 million to bring collateral to INR 450 million; personal guarantees of Yogesh Kusumgar and Siddharth Kusumgar. At 31 May 2026: pari passu charges on movable fixed assets and current assets, lien on fixed deposits equal to 15% of released limits, demand promissory note and letter of continuity INR 350 million, the same personal guarantees and the 4S Holding corporate guarantee (p.337).
- Covenants (Note 23 Note 4, p.307): INR 842.65 of non-current borrowings carry covenants "which, if not met, would result in the borrowings becoming repayable on demand". The company says it met all covenants due on or before 31 March 2026 and keeps the debt non-current. The financial covenants (ratios, thresholds): NOT FOUND IN DOCUMENT. Prior-approval covenants listed in the prospectus (p.337): change in management or shareholding, capital structure, MOA/AOA, asset sales, mergers, loans to group companies or subsidiaries, prepayment, capex outside estimates, and any change or reduction in Promoter ownership. Events of default include cross-default, change of ownership and material adverse change (pp.337-338). Lenders may convert debt to equity (p.338). Consents for the Offer obtained (p.338). No breach or waiver disclosed. "There is no default in terms of repayment of Principle and Interest" (p.307). 🟡
- Revolving usage: proceeds from borrowings 8,145.81 and repayments (8,375.00) in FY26 (p.283); FY25 proceeds 1,832.33 vs repayments 139.99.
- Post year-end: at 31 May 2026 working-capital loans were 1,697.68 (including interest) against sanctioned 2,900; term loans 1,141.17; vehicle loans 19.35; total secured fund-based 2,858.20, against total borrowings of 2,235.82 at Mar 2026 (pp.335-336). Working-capital borrowings at Mar 2026 were 1,031.60 (WCDL + PCFC + CC, derived). The May figure is about 666 higher (derived); definitions differ (May includes interest), so direction rather than exact size is the point. Total secured including non-fund-based: 3,848.87 (p.336). 🔴 for liquidity direction.
- Gearing (Note 47, p.324): net adjusted debt 1,755.23 / 2,053.15 / (667.60); gearing 0.26 / 0.44 / 0.00. Total borrowings to equity 0.44 (p.335).
- Finance costs (Note 35, p.310): borrowings 180.71; lease interest 55.77; unsecured director loans 5.83; bank and other charges 17.47; total 259.78 (FY25 146.31).
- Interest rate sensitivity (Note 48(a)(i), p.324): PBT effect of 1% = (1.81)/1.81 (FY26). All long-term debt is floating; 1% of 2,235.83 is 22.36 (derived). The disclosed figure is about 8% of that. Base used: NOT FOUND IN DOCUMENT. 🟡
- Related-party borrowings: promoter loans taken and repaid within each year (Section 2). Credit support from 4S Holding and personal guarantees, no fee disclosed.
- Equity funding: 35,01,372 CCPS issued 15 and 24 Sept 2025, net cash 1,244.94 (p.283), converted 1:1 into equity on 21 Jun 2026 (p.335). Price per CCPS = (17.51 + 1,260.48) / 3,501,372 = INR 365.0 (derived). Holders above 5%: Motilal Oswal Finvest 31.30%, Edelweiss Discovery Fund 19.56%, Spark Midas 15.65%, WhiteOak 10.95%, Ashoka India Equity Investment Trust 10.95%, Frangipani 7.82% (Note 21(e), p.305).

---

## 8. TRADE PAYABLES (Note 25, pp.308-309)
- Total 667.62 / 472.07 / 522.72 (Mar 26/25/24): MSME 26.13 / 50.42 / 14.32; other 641.49 / 421.65 / 508.40 (p.279). Related-party payables 24.06 / 19.19 / 19.19.
- Ageing Mar 2026 (columns: Unbilled, Not due, <1 yr, 1-2, 2-3, >3, assigned by position): MSME 26.13 (not due 18.23; <1 yr 7.38; 1-2 yrs 0.52). Others undisputed 608.49 (unbilled 31.94; not due 137.62; <1 yr 425.34; 1-2 yrs 9.54; 2-3 yrs 0.08; >3 yrs 3.97). DISPUTED others 33.00 (<1 yr 13.82; 1-2 yrs 19.13; >3 yrs 0.05); nil in FY25 and FY24. Total 667.62 (sum of column totals checks).
- MSME: principal 26.13 / 50.42 / 14.32; interest paid, due, accrued, payable all nil. Over-45-day split: NOT FOUND IN DOCUMENT. 🟢 on what is disclosed.
- Payable days (derived on purchases, Note 32): 79.7 (FY26), 49.3 (FY25), 75.5 (FY24).
- New disputed payables 33.00 in FY26 with no description. 🟡
- Related-party payable to Paraborne Systems LLP static for three year-ends. 🟡
- Capital creditors 43.13 / 53.15 / 25.59 (Note 26, p.309); advances to capital creditors 37.95 / 195.53 / 83.14 (Note 13, p.301).

---

## 9. PROVISIONS AND EMPLOYEE BENEFITS (Notes 24, 26, 27, 42; pp.308-316)
- Gratuity (funded; Note 42(c), p.315): obligation 58.02 / 55.82 / 40.04; plan assets 55.41 / 38.14 / 24.09; net liability 2.60 / 17.68 / 15.95. Employer contributions 18.30 (FY26), 13.46, 4.46. Discount rate 7.25% to 7.29% (FY26), 6.59% to 6.61% (FY25), 6.97% (FY24); salary escalation 6.00%; withdrawal 6.00%; duration 9.20 years; mortality Indian Assured Lives 2012-14. Sensitivity (FY26): discount rate +1% 53.15, -1% 63.66; salary +1% 62.88, -1% 53.71 (p.316). OCI actuarial gain 9.34 FY26 (loss 5.61 FY25; loss 11.11 FY24). 🟢
- Compensated absences: provision 17.43 non-current + 1.48 current (FY26) vs 15.07 + 1.84 (FY25), 6.12 + 1.14 (FY24) (Note 42(b), p.314); expense 13.29 FY26 vs 0.11 FY25, unexplained. 🟡 (minor)
- Defined contribution: provident fund 22.59, superannuation and NPS 0.87 (FY26) (Note 42(a), p.314).
- Warranty provision 1.02, first time in FY26 (Note 26, p.309; Note 37, p.311). Movement table NOT FOUND IN DOCUMENT. 🟢 (immaterial)
- Decommissioning, onerous contracts, litigation provisions: none disclosed in these pages.
- Other current liabilities (Note 28, p.309): advance from customers 87.59 / 27.44 / 1,264.61; CSR liability 37.93 / 20.38 / 8.22; statutory dues 22.58 / 49.03 / 35.04.
- CSR: expense 20.29 / 12.46 / 6.92 (Note 37, p.311). The CSR liability grew 8.22 to 20.38 to 37.93. Ring-fenced balances: earmarked bank balance 13.05 (Note 16, p.302) plus 7.50 in Other bank balances (Note 17 footnote, p.301) = 20.55 against the liability 37.93 (difference 17.38, derived). Required CSR amount: NOT FOUND IN DOCUMENT. 🟡 (minor)

---

## 10. DEFERRED TAX AND CURRENT TAX (Notes 29, 38; pp.309, 312-313)
- Income tax expense 367.58 / 387.95 / 306.75; effective rate on PBT 27.2% / 25.7% / 26.7% (derived). Statutory 25.17%. FY26 reconciliation (p.312): at 25.17% 339.66; non-deductible expenses 6.00; short provision for earlier years 0.23; effect of differential tax rate 14.28; others 7.41. The 14.28 arises because the Dubai subsidiary is treated as India-resident on place of effective management and taxed at 38.30% (p.312). Whether any UAE tax is also paid: NOT FOUND IN DOCUMENT. 🟡
- Deferred tax: net DTL 24.69 / 16.54 / 34.97; balance sheet DTL 25.45 less DTA 0.76 (pp.312-313). Mar 2026 components: DTA on lease liabilities 163.28, ECL 15.72, employee benefits 5.42; DTL on ROU assets 177.62, PPE 30.47, FVTOCI gain 6.61. MAT entitlement 0.36 at Apr 2023 was used in FY24 (p.313). No unrecognised DTA disclosed. 🟢
- Current tax: payable 354.68 (FY26) less taxes paid 198.39 leaves a 156.29 liability at Mar 2026 (nil at Mar 2025; 29.70 at Mar 2024) (Note 29, p.309). Cash flow shows net tax paid 174.95 (FY26) and 438.66 (FY25) (p.283). Income tax demand 10.14 (Note 40). 🟢

---

## 11. REVENUE DETAILS: see LB2. Additional.
- Contract liabilities roll: opening 27.44 (FY26), 1,264.61 (FY25), 29.18 (FY24); additions 87.59, 27.44, 1,264.61; revenue recognised from opening (27.44), (1,264.61), (29.18) (Note 44(c), p.321).
- No contract assets or unbilled revenue line. No remaining performance obligation (p.321).
- Other income quality (Note 31, p.310): total 197.75 / 112.15 / 66.43; FX gain 147.91 / 46.95 / 32.40; fixed-deposit interest 21.89 / 57.57 / 29.52; ECL reversal 6.23; sundry balance written back 6.28; gain on lease cancellation 2.96. FX gain = 74.8% of FY26 other income and 11.0% of FY26 PBT (derived). Company EBITDA excludes other income (p.333: 1,878.50 / 1,883.89 / 1,318.47). EBITDA before the ESOP charge FY26 = 1,878.50 + 204.33 = 2,082.83 (derived).
- Expense side (Note 37, p.311): royalty 88.61 / 129.64 / 325.08; job work and labour 397.74 / 362.57 / 186.91; power and fuel 362.74 / 333.31 / 211.14; professional and legal 94.95 / 88.96 / 45.05 (excludes IPO cost 73.17 recoverable from selling shareholders).

---

## 12. OTHER CRITICAL NOTES

### Exceptional items
None presented as exceptional in the P&L (p.280). Recurring one-offs to track: inventory write-downs (180.45 / 39.57 / 117.73), ECL charge 38.05 in FY25, ESOP charge 204.33 in FY26, FX gain 147.91 in FY26.

### Property, plant and equipment, CWIP, intangibles (Notes 6-9, pp.298-300)
- Net block 2,356.68 / 1,718.63 / 1,367.20; gross additions 1,118.88 (FY26), 613.69 (FY25), 669.04 (FY24). PPE depreciation 358.79 / 255.45 / 123.97.
- Freehold land: gross 37.08 at Mar 2025 is 6.00 at Mar 2026 with an "Adjustment 31.08" on the same line; the ROU asset has a matching "Adjustments 31.08" (Note 7, p.299). The arithmetic works only if 31.08 of freehold land was reclassified to right-of-use. No narrative. Note 53(i) says title deeds of all immovable properties, other than leased ones, are in the Group's name (p.331). 🟡
- Subsidy received 88.22 netted against plant and machinery gross block in FY26 (p.298), in addition to grant income 77.15 in revenue.
- CWIP 262.64 / 451.94 / 84.34. Mar 2026 ageing: in progress 224.84 (217.98 under one year; 6.86 in 1-2 years); temporarily suspended 37.80 (23.64 under one year; 14.16 in 1-2 years), "will be resumed and completed in the financials year end 2026-27" (Note 8, p.300). 🟡 (minor)
- Intangibles: software only, net 2.92 / 1.33 / 2.21. No goodwill.

### Capital commitments: Section 3.

### Foreign currency exposure and hedging (Note 48(a)(ii), pp.324-325)
Unhedged balances at Mar 2026: USD receivables 13.23 million (INR 1,627.72), EUR receivables 0.42 million (INR 44.10); USD payables 3.30 million (INR 306.11), EUR payables 0.04 million (INR 4.54); USD forwards 1.50 million (INR 142.97) vs 8.50 million (INR 714.56) at Mar 2024 and none at Mar 2025. Forward contract asset at fair value 5.72 (Level 2, p.323). Sensitivity of PBT to a 10% USD move: +146.46 (FY26), (15.81) (FY25), 2.49 (FY24); EUR 3.96 / 2.19 / 3.44 (p.325). See the rate inconsistency under LB1. 🟡

### Segment reporting: see LB2. Single segment.

### EPS (Note 39, p.314)
Basic EPS 9.68 / 11.03 / 8.32; diluted 9.31 / 10.81 / 8.32. Weighted shares 101.49 million; diluted 105.49 million FY26 (4.00 million CCPS-weighted plus 2.06 million options) and 103.55 million FY25. EPS restated for the 1:100 split (1 Oct 2024), 3:1 bonus (20 Feb 2025) and 11:40 bonus (25 Mar 2025) (Note 21, p.305). Dilution gap 3.8% FY26 (derived). 🟢

### Share capital (Notes 21-22, pp.304-306)
Equity 101.49 (10,14,90,000 shares of INR 1) plus CCPS 17.51 (35,01,372 of INR 5, 0.01% cumulative dividend, 1:1 conversion). Authorised capital raised from 30 to 240 (Jan 2025). Bonus issues used general reserve 57.91 and retained earnings 23.68 (total 81.59) (p.306). Securities premium 1,496.82 after CCPS premium 1,260.48 less transaction cost 33.05. The board recommended the 0.01% CCPS dividend (Note 54, p.331). Option overhang 21,72,712 = 2.14% of equity (derived).

### Reserves bypassing the P&L
- Common control adjustment deficit (1,107.62), unchanged in all years (Note 22(f), p.306; Note 51, p.330): purchase consideration 1,118.53 less ECFPL net assets 10.91 (derived). Net worth 5,029.54 is after this debit. 🟡 (cash left the company to the promoters; no P&L effect)
- Remeasurement of defined benefit in retained earnings; FVTOCI gains in OCI reserve 39.57; ESOP reserve 238.90 (non-cash).

### ESOP (Note 49, pp.326-327)
- ESOP 2024 approved 22 Oct 2024. Options outstanding 21,72,712 at Mar 2026 (20,71,222 at Mar 2025), exercise price INR 1.00; exercisable 2,99,914; none exercised or forfeited. Grants: Oct 2024 4,06,122; Feb 2025 12,18,366 and Mar 2025 4,46,734 (additional options from the bonus issues); Sept 2025 1,01,490 (1.00% of equity). Ten tranches vesting over 7 to 115 months; service condition only.
- Expense 204.33 (FY26) vs 34.57 (FY25); reserve 238.90 (Note 49(d)-(e), p.327). Ankur Kothari took 199.16 of the FY26 charge.
- Per-option fair values: INR 281.53 to 281.61 for the Oct 2024, Feb and Mar 2025 grants and 286.88 to 287.29 for Sept 2025 (Note 49(b), p.326). The Black-Scholes table shows weighted average fair values of 207.91, 79.27, 143.59 to 143.62 (totals 1,436.04) for one scheme and 28.62 to 28.64 (total 286.27) for another, and a "weighted average share price" column printed as 1.00 (Note 49(c), p.327). These cannot be reconciled from the note. The CCPS price in the same month as the Sept 2025 grant was INR 365.0 (derived). 🟡

### Events after the balance sheet date (Note 56, p.332)
"No other items to disclose" beyond earlier notes. Items found elsewhere in pages read: CCPS converted into equity on 21 Jun 2026 (p.335); working-capital borrowings at 31 May 2026 (p.336); Kusumgar Composites formed 27 Mar 2026 (Note 43, p.317). Nothing on post-year-end receivable collection. 🟡

### Additional regulatory information (Note 53, p.331)
No wilful defaulter, benami property, struck-off company, ROC charge, layer or fund-utilisation exceptions. No investment property. No revaluation. Borrowings applied for the purposes taken. 🟢

### Cash flow structure (pp.283-284)
- Operating cash flow 282.58 / (1,549.76) / 2,009.64; investing (1,026.59) / 20.62 / (1,995.80); financing 697.47 / 1,507.49 / 211.84.
- The 1,118.53 consideration runs through FY25 operating working-capital changes and the matching customer advance through FY24; operating cash flow swings with these items, not only with trading. 🟡
- Capex net of subsidy 693.81 / 1,066.12 / 780.42. Interest paid on borrowings 185.78; on leases 56.53.
- Reconciliation of financing liabilities: 3,021.87 (1 Apr 2025) to 2,884.59 (31 Mar 2026) (p.284).

### Fair value and risk (Notes 46-48, pp.322-325)
Level 3: Toray Kusumgar 154.19. Level 2: forward asset 5.72 (FY26), liability 1.82 (FY24). Liquidity table (p.325): financial liabilities due within 1 year 2,257.56; current financial assets 3,002.13 (p.322). Credit risk on cash and bank balances stated as negligible.

---

## PASS 1 SUMMARY: TOP 10 FINDINGS, RANKED BY INVESTOR IMPORTANCE

| Rank | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | Receivables up 4.2x (561.10 to 2,332.79) while revenue fell 11.2%; debtor days 26 to 123; 71.8% of gross is "not due" (1,719.06) against 30 to 45 day terms, which means about 25% of annual revenue was invoiced in the last 45 days or terms are longer; overdue rupees 175.91 to 676.18; ECL cover fell to 2.6% with a 6.23 reversal taken to income; FY26 operating cash flow 282.58 vs EBITDA 1,878.50 (15%); 3-year CFO 25% of cumulative profit. | Note 15 (p.302); Note 44(c) (p.321); Note 48(b) (p.325); Annexure IV (p.283) | 🔴 |
| 2 | Customer concentration and revenue shape: customer one 46.00% of FY24 and 24.97% of FY25, customer two 27.97% of FY25; none above 10% in FY26; India fabrics and solutions down 44.4% while exports up 47.2%. Customers unnamed. | Note 45(c) (p.321); Note 44(a) (p.320) | 🔴 |
| 3 | FY24 customer advance 1,264.61 (96.7% of other current liabilities) was entirely recognised as FY25 revenue (16.2% of FY25 revenue); the 1,118.53 acquisition consideration owed to promoters sat in FY24 other financial liabilities and was paid through FY25 operating cash flow; FY24 and FY25 cash flows are distorted. | Note 28 (p.309); Note 44(c) (p.321); Note 26 (p.309); Note 51 (p.330); Annexure IV (p.283) | 🔴 |
| 4 | Bank guarantee contingent liability 1,038.77 (nil prior) = 20.7% of net worth; total contingent liabilities 21.7% of net worth; beneficiary and purpose not disclosed; working-capital debt rose from 1,031.60 (Mar 2026) to 1,697.68 (31 May 2026, with interest). | Note 40 (p.314); p.80; p.336 | 🔴 |
| 5 | Unhedged USD receivable 13.23 million carried at INR 1,627.72 (implied 123.0 per USD) against 92.8 (payables) and 95.3 (forwards) in the same note; FX gain 147.91 fully unrealised and 11.0% of PBT; the intra-group FZ LLC receivable 377.27 may sit in the figure (not stated). | Note 48(a)(ii) (p.324); Note 31 (p.310); Annexure IV (p.283) | 🟡 |
| 6 | New services line: revenue 523.13 (14.97 prior), all booked as India, 83.9% margin before other costs, no description; 312.61 sold intra-group to FZ LLC, whose net assets are 70.73 against 605.26 due to the parent. | Note 30 (p.310); Note 44(a) (p.320); Note 43(h) (p.319); Note 50 (p.328) | 🟡 |
| 7 | Related-party flows tied to the selling shareholders: promoters sold ECFPL for 1,118.53; they lent 300.00 and 284.17 in FY26 and FY25 (repaid inside each year); 81.48 IPO costs recovered from Siddharth Kusumgar with 17.70 outstanding; promoter-group shares fell by 64,98,631 (6.40% of equity) in FY26, buyer not given; former Director consultant fee 6.00 and personal guarantee on bank debt; blanket arm's-length statement. | Note 43 (pp.317-319); Note 51 (p.330); Note 21 (p.305); Note 23 (p.307) | 🟡 |
| 8 | Finished goods +78.4% on falling sales; inventory write-downs 117.73 / 39.57 / 180.45; FY25 bank stock statements differed from books by up to 121; audit trail not enabled at database level until 27 Jul 2025 and absent in FY24. | Note 14 (p.301); Annexure VI Part C (p.297); auditor report (p.275) | 🟡 |
| 9 | ESOP charge 204.33 (FY26) vs 34.57, 97.5% to the CEO; per-option fair values inconsistent within Note 49; overhang 2.14%; Sept 2025 option fair value INR 286.88 vs CCPS price INR 365.0 in the same month. | Note 49 (pp.326-327); Note 34 (p.310); Note 43(e) (p.317) | 🟡 |
| 10 | Debt terms: 842.65 of non-current debt carries on-demand-if-breached covenants (ratios not disclosed); lender approval needed for change in promoter ownership or management; personal guarantees of Siddharth and Yogesh Kusumgar and a 4S Holding corporate guarantee; no principal schedule. | Note 23 (p.307); pp.337-338 | 🟡 |

Rated 🟢: no restatement adjustments (Annexure VI, p.296); gratuity funded (Note 42, p.315); capital commitments down to 58.33; no MSME interest; no going-concern doubt (Note 2(f), p.287); deferred tax.

NOT FOUND IN DOCUMENT (pp.80-81, 271-338): ECL matrix rates; royalty payee; counterparty for the 155.69 loan and the 234.43 security deposit; bank guarantee beneficiary; nature of services revenue 523.13; customer names; covenant ratios; year-wise repayment schedule; auditor of Kusumgar Middle East FZ LLC; CSR required amount; buyer of the 64,98,631 promoter-group shares; quarterly revenue pattern; inventory write-down reasons.
