# STAGE 2 NOTES PASS 1 (FULL EXTRACTION): SOUTHWEST, FY26 (year ended 31 Mar 2026)

Run date 2026-11-09. Source: inputs/annual-report/Annual_Report_2026.txt (20th AR). Model: claude-sonnet-5-5.

## 0. Read conventions

- Unit on the face of the document: INR Lakhs ("All amounts in INR Lakhs", standalone p.127, consolidated p.169). Nothing below is converted. Stage 10 converts once.
- Page anchors use the "[page N]" markers in the .txt. The marker opens the page, so text after it belongs to that page. Printed folio = page minus 16.
- The AR holds two note sets. STANDALONE Notes 1-66 (pp.116-157) and CONSOLIDATED Notes 1-65 (pp.169-203). Note numbers shift by one or two between the sets after Note 5 (for example standalone Note 48 RPT = consolidated Note 49). Every anchor says "S" (standalone) or "C" (consolidated).
- Column order in the notes: current year (FY26) first, prior year (FY25) second in nearly every table, even where the printed column header reads "2025, 2026" in that order (Notes 31-40 S). I tested this by tying figures: Note 39 S ECL 87.18 = allowance 187.95 less 100.78 (Note 12 S, p.131); Note 33 S closing inventory 5,093.93 = Note 11 S (p.130). Where the order is ambiguous I say so.
- "(derived)" marks arithmetic I performed on anchored figures. It is not a disclosed number. "NOT FOUND IN DOCUMENT" marks an expected disclosure that is absent.
- Extraction gaps in the .txt: standalone Note 41 (contingent liabilities) has a heading only at p.139 with no body in the text. Standalone Note 46 segment table is missing (only geography and customer lines survive, p.146). Consolidated Note 42 and Note 47 are complete and are used instead. The verifier should open the PDF for S Note 41 and S Note 46.
- Rating key: green = Clean, yellow = Watch, red = Red Flag. Written as GREEN / YELLOW / RED.

## 1. ACCOUNTING POLICIES AND CHANGES

| Item | Finding | Anchor | Rating |
|---|---|---|---|
| Basis | Ind AS, Division II Schedule III. Standalone and consolidated authorised for issue 04 May 2026. | Note 1 S p.116; Note 1 C p.169 | GREEN |
| Revenue recognition | Ind AS 115. Services recognised "with reference to the performance of each service in a particular month" under "fixed price contracts, where there is no uncertainty towards measurement or collectability". Uncompleted services at period end go to "Unbilled Revenue" ("no enforceable claim has become due"). Goods at point of shipment or delivery. | Note 1(c) S p.117 | YELLOW: unbilled revenue is a contract asset in substance but is carried inside trade receivables (see Section 4 and 11) |
| Exploration and evaluation (E&E) policy | NOT FOUND IN DOCUMENT. No policy for E&E assets (Ind AS 106), no capitalisation criteria, no impairment trigger, no amortisation start. The asset is carried as "Intangible assets under development" 1,930.58. | Note 5 S p.129; policy list Note 1 S pp.116-125 | RED for disclosure: the single largest non-operating asset has no stated policy |
| Depreciation | PPE depreciated on written down value over Schedule II lives. Residual values and lives reviewed yearly. Leasehold improvements on straight line. Numeric lives per class: NOT FOUND IN DOCUMENT. No change of method or life reported. | Note 1(e)(iv) S p.118; Note 1(i) S p.119 | YELLOW (cannot test lives against rig norms) |
| Capitalisation of borrowing costs | Policy permits capitalisation for qualifying assets. Amount capitalised in FY26: NOT FOUND IN DOCUMENT. Finance cost 842.34 is all expensed (Note 37 S). E&E and rig capex both carried on borrowed money. | Note 1(k) S p.119; Note 37 S p.138 | YELLOW |
| Impairment testing | Generic Ind AS 36 policy only. No CGU, growth rate or discount rate disclosed for E&E 1,930.58, PPE, or investments. | Note 1(g) S p.119 | YELLOW |
| Investments in subsidiaries and JVs (standalone) | At cost (Ind AS 27). Written down only if carrying amount exceeds recoverable amount. | Note 1(h) S p.119 | see Section 6 (SWR) |
| JVs (consolidated) | Equity method. | Note 1(c)(2) C p.170-171 | GREEN |
| ECL | Simplified approach, lifetime ECL, provision matrix "based on its historically observed default rates... adjusted for forward looking estimates". Matrix rates by bucket: NOT FOUND IN DOCUMENT. | Note 1(r) S p.124 | YELLOW |
| Leases (Ind AS 116) | Lessee: buildings only. Lease liability 152.37 (current 25.49, non-current 126.88). ROU asset 114.88 (opening 140.64, charge 25.76). Interest on lease liability 14.56 on opening 175.75. Incremental borrowing rate: NOT FOUND IN DOCUMENT (14.56/175.75 = 8.3%, derived). | Note 6 S p.129; Note 42 S p.140 | GREEN |
| New standards | Ind AS 1 / Ind AS 10 covenant amendment effective 1 Apr 2026. Company states "no impact". | Note 1(u) S p.125 | GREEN |
| Re-grouping | "Previous year figures have been re-grouped/re-classified wherever necessary." No quantified restatement. | Note 66 S p.157 | YELLOW (see Pass 3) |
| Audit trail | Accounting software has audit trail, "operated throughout the year". | Note 65 S p.157 | GREEN |
| Government grants, current/non-current, FVM, FX policy | Standard text. | Note 64 S pp.155-156 | GREEN |

## 2. RELATED PARTY TRANSACTIONS

### 2a. Parties (Note 48 S p.146-147; Note 49 C p.193)

- Wholly owned subsidiaries: South West Resources Pvt Ltd (SWR, formerly Pilot Pipelines Pvt Ltd), South West Geo Services Pvt Ltd (SWGS, new, CIN year 2025).
- Subsidiary 74%: South West Oil Field Services Pvt Ltd (SWOFS).
- Jointly controlled entities: Alara Resources LLC (Oman, 35%), South West Samit JV (AOP, 80%), Al Hadeetha Mining LLC (Oman, 17.5%, new this year).
- KMP: Vikas Jain (CMD), Piyush Jain (JMD), Dinesh Agarwal (CFO), Vaishali (CS), four directors.
- Relatives: Gajraj Jain, Hemlata Jain, Ruchi Jain, Rachna Jain, Kasvi Jain.
- Enterprises significantly influenced by KMP or relatives: Alara Resources Ltd (Australia, listed, "ARL"), Chandra Prabhu International Ltd, Thakurji Towers Pvt Ltd, Ravmo Imports LLP, Vikas Jain HUF, Piyush Jain HUF.
- New related party this year: South West Geo Services Pvt Ltd (SWGS), Al Hadeetha Mining LLC. Alara Resources Ltd is a related party that the Company now owns 1.56% of (Note 7 S p.129).

### 2b. Transaction table, standalone (INR Lakhs; current year, prior year in brackets). Note 48 S p.148

The text extraction drops column placement for several rows. Where the party column is not resolvable it is marked "col?".

| Nature | FY26 | FY25 | YoY (derived) | Party column |
|---|---|---|---|---|
| Remuneration (KMP) | 425.29 | 242.71 | +75.2% | KMP |
| Unsecured loan taken | - | 420.00 and 170.00 | n/a | KMP / enterprises |
| Unsecured loan repaid | - | 623.35 and 170.00 | n/a | KMP / enterprises |
| Interest on unsecured loan | - | 31.50 | n/a | KMP |
| Loans and advances given | 140.23 (JCE); 1,100.00 (enterprises) | 10.00; 44.62; 950.00 | n/a | split as printed |
| Repayment of loans and advances given | 90.00 (subsidiary); 1,100.00 (enterprises) | 12.00; 950.00 | n/a | split as printed |
| Other receivable given | 13.79; 23.04 | 6.879; 12.57 | n/a | subsidiary; JCE |
| Interest on loans and advances | 11.42 (JCE); 15.62 (enterprises) | 5.86; 3.30 | +95% / +373% | JCE; enterprises |
| Sale of service | 282.92 | 35.18; 241.97; 13.43 | +704% vs 35.18 | subsidiary (col? for rest) |
| Purchase of drilling services | 632.01 | 748.53 | -15.6% | subsidiary |
| Purchase of geological / 2D seismic services | 60.99 and 45.41 | 47.09 and 445.03 | JCE col? 45.41 vs 445.03 = -89.8% | subsidiary; col? |
| Investments | 327.92 | 1.00 | n/a | col? |

Cross-ties (derived): 327.92 = Al Hadeetha 39.92 + 288.00 purchase of Alara Resources Ltd shares. The 288.00 is in the cash flow as "Investment in other companies (288.00)" and the 39.92 as "Investment in joint venture (39.92)" (Cash flow S p.115). Interest from loans 27.04 (Note 32 S p.137) = 11.42 + 15.62.

Year-end balances (standalone, Note 48 S p.148): remuneration payable 45.89 (PY 11.85); creditors and other payables 450.17 and 85.89 (PY 171.87 and 151.75); debtors 130.24 (PY 34.41); loans and advances asset 431.44, 293.48 and 0.19 (PY 507.04, 103.67, 0.20).

Consolidated table (Note 49 C p.194) drops subsidiary lines. Remuneration prints 420.49 (PY 263.13) while the compensation table (Note 49 C p.195) shows total 425.29, PY 242.71. See Pass 3 for the mismatch.

### 2c. Compensation (Note 48 S p.149; Note 49 C p.195)

Short-term benefits 420.49 (PY 236.13). Sitting fees 4.80 (PY 6.58). Total 425.29 (PY 242.71). No post-employment, no share-based pay.

### 2d. RPT as % of revenue (derived, revenue from operations S = 24,292.95, Note 31 S p.137)

| Item | INR Lakhs | % of revenue |
|---|---|---|
| Remuneration | 425.29 | 1.75% |
| Sale of service to subsidiary | 282.92 | 1.16% |
| Purchase of drilling services from subsidiary | 632.01 | 2.60% |
| Purchase of geological / 2D seismic (60.99 + 45.41) | 106.40 | 0.44% |
| Sum of operating RPT excluding loans | 1,446.62 | 5.95% |

Loans and advances to related parties outstanding: current 410.34 (Note 15 S p.131) + non-current 257.86 (Note 8 S p.130) = 668.20 (matches Note 49a loans 668.20, S p.149). Against standalone equity of 20,251.42 (Note 49c S p.153) this is 3.3% (derived).

### 2e. Non-arm's-length signals and judgements

- RED: Same-year round trip of 1,100.00 lent to and repaid by an enterprise significantly influenced by KMP or relatives, with 15.62 interest. The prior year shows the same shape (950.00 out, 950.00 back, 3.30 interest). The borrower is not named. The six candidates are listed (Note 48 S p.147). Interest 15.62 on a loan that cycles inside a year implies a short tenor or a rate far above bank rates; rate and tenor: NOT FOUND IN DOCUMENT. Note 15 S carries only the SWR balance as a current loan (410.34), so the 1,100.00 left the balance sheet by 31 Mar 2026. Rating RED for opacity, not for loss: no balance remains.
- YELLOW: Loans to SWR 410.34 are 61.41% of the Company's loans and advances (Note 52 S p.154). SWR has accumulated losses of 314.88 that "fully eroded the net worth" (Consolidated auditor's report, going concern paragraph, p.159). Schedule III shows SWR net assets (264.94) (Note 52 C p.202). The Company's investment in SWR is 42.38 at cost (Note 7 S p.129). No impairment of the investment and no ECL on the 410.34 loan: NOT FOUND IN DOCUMENT. SWR also supplies 632.01 of drilling services to the parent (Note 48 S p.148). Rate and tenor of the SWR loan: NOT FOUND IN DOCUMENT.
- YELLOW: Alara Resources Ltd (Australia) is named as an enterprise significantly influenced by KMP or relatives (Note 48 S p.147). In FY26 the Company paid 288.00 for 12,500,000 shares (1.56%), carried at fair value 274.76 (Note 7 S p.129-130; Cash flow S p.115). The Company's own JV partner in Alara Resources LLC is an Alara Resources Ltd-linked party (Board's report p.41: "formed with Alara Resources Ltd., a renowned Australian exploration and mining company"). Fair value loss through OCI: pre-tax 13.24 derived (288.00 less 274.76); the OCI line is (10.21) after tax (Note 19 S p.133). The 13.24 is derived by me, the AR states only the net-of-tax 10.21 and the DTA "Other (3.03)" (Note 44 S p.141). 10.21 + 3.03 = 13.24 ties.
- YELLOW: Promoter personal guarantees secure term loans and working capital lines (Note 20 S p.134; Note 25 S p.135; "Refer note 20 and 25 for personal guarantee given by promoter" Note 48 S p.148). No guarantee fee is disclosed. No royalty or rent to promoter family: NOT FOUND IN DOCUMENT in the table.
- GREEN: No loans to promoters or promoter-family individuals outstanding at year end per the balances table. Unsecured related-party borrowing on the consolidated balance sheet is 0.50 only (Note 26 C p.181).
- Remuneration +75.2% against standalone PAT +107.8% (3,080.05 vs 1,482.51, Note 40 S p.139; derived). Remuneration is 10.3% of standalone PBT 4,130.80 (derived; PBT from Note 44 S p.141).

## 3. CONTINGENT LIABILITIES AND COMMITMENTS (Note 42 C p.185-186; S Note 41 body not in text)

| Nature | FY26 | FY25 | Stage | Company assessment |
|---|---|---|---|---|
| Bank guarantees | 2,250.08 (total printed 2,250.07) | 2,253.79 (total printed 2,253.78) | Issued | Not stated |
| Income tax | 115.85 (AY 2010-11, ITAT) | 184.16 (AY 2014-15 92.31 and AY 2016-17 91.85, both ITAT) | ITAT | Not stated |
| VAT / WCT / Entry tax / GST, total | 446.77 | 28.88 | Mixed | Not stated |
| of which GST FY 2021-22 Appellate Authority | 397.59 | nil | Appellate | Not stated |
| of which GST 2018-19 | 1.33 | 1.33 | Appellate | Not stated |
| of which GST 2020-21 | 3.47 | nil | Appellate | Not stated |
| of which GST 2021-22 (second line) | 2.39 | nil | Appellate | Not stated |
| of which Entry tax FY2008-09 to Jun 2018 | 18.24 | 18.24 | not stated | Not stated |
| of which Entry tax FY2010-11 to FY2014-15 | 4.81 | 4.81 | not stated | Not stated |
| of which Entry tax Apr-Jun 2017 | 12.71 | nil | not stated | Not stated |
| of which VAT FY2010-11 to FY2014-15 | 4.50 | 4.50 | not stated | Not stated |
| of which VAT Apr-Jun 2017 | 1.73 | nil | not stated | Not stated |
| Other contingent total | 562.62 | 213.04 | | |
| Capital commitments | 1,720.64 | 2,497.60 | | |

Tax-dispute sum check (derived): GST 1.33+3.47+397.59+2.39 = 404.78; entry tax 35.76; VAT 6.23; total 446.77 ties to the printed total.

- Total contingent (guarantees 2,250.07 + other 562.62) = 2,812.69, which is 13.8% of consolidated net assets of 20,352.94 (Note 52 C p.202; derived).
- Bank guarantees alone are 11.1% of net assets (derived). It is the only single item above 10%.
- Largest dispute: GST FY2021-22 397.59, 1.95% of net assets (derived). It is new this year and is 71% of the other-contingent total (derived).
- The company gives no probability assessment, no provision, and no reason for the swing in income tax items (the two older AY matters left the list and an AY 2010-11 matter of 115.85 appears). Reason: NOT FOUND IN DOCUMENT. Rating YELLOW (GST 397.59 appeal pending).
- Guarantees for subsidiaries: NOT FOUND IN DOCUMENT. Corporate guarantee for ARL or Al Hadeetha: NOT FOUND IN DOCUMENT. Note 52 S p.154 lists loans to specified persons only.
- Undrawn committed facility: 3,463.38 (PY 4,211.00); availed fund and non-fund based limits 6,510.62 (PY 5,750.50) (Note 42C C p.186; Note 43 S p.140). Utilisation = 6,510.62 / (6,510.62 + 3,463.38) = 65.3% (PY 57.7%) (derived).
- Capital commitments fell 776.96 (derived), consistent with the rig purchases landed in FY26 (Note 2 S p.127).

## 4. TRADE RECEIVABLES

### 4a. Ageing from due date, standalone (Note 12 S p.131; INR Lakhs). All "undisputed, considered good". Disputed and doubtful rows are nil.

| Bucket | 31 Mar 2026 | % | 31 Mar 2025 | % |
|---|---|---|---|---|
| Unbilled | 2,613.79 | 22.1% | 2,958.08 | 39.3% |
| Not due | 8,452.45 | 71.4% | 4,241.45 | 56.3% |
| Overdue less than 6 months | 496.12 | 4.2% | 25.42 | 0.3% |
| 6 months to 1 year | 80.77 | 0.7% | 4.68 | 0.1% |
| 1 to 2 years | - | 0.0% | 131.90 | 1.8% |
| 2 to 3 years | 16.21 | 0.1% | 173.14 | 2.3% |
| More than 3 years | 173.13 | 1.5% | - | 0.0% |
| Gross total | 11,832.46 | | 7,534.67 | |
| Loss allowance | (187.95) | 1.59% of gross | (100.78) | 1.34% |
| Net | 11,644.51 | | 7,433.89 | |

Percent columns are derived. Row sums tie to the printed totals (I added them).

- Gross receivables +57.0% against revenue +35.6% (24,292.95 vs 17,919.32, Note 31 S p.137; derived).
- Closing gross receivables / revenue x 365 = 177.8 days (FY26) vs 153.5 days (FY25) (derived). The company's own ratio: receivable turnover 2.55 vs 2.74, -7.20% (Note 51 S p.154). Three-year trend: FY24 NOT FOUND IN DOCUMENT in these notes.
- Billed receivables only (trade receivables ex unbilled): 9,218.67 vs 4,576.59 (Note 12 S p.131). Days on revenue: 138.5 vs 93.2 (derived). This is +101% against revenue +35.6%.
- Overdue more than 6 months: 270.11 (80.77+16.21+173.13) = 2.28% of gross vs 309.72 = 4.11% in FY25 (derived). Overdue at all: 766.23 = 6.5% (derived).
- Old tail: 173.13 over 3 years (FY25: 173.14 sat in 2-3 years). The same sum did not move in a year. It is classed "considered good". The allowance of 187.95 exceeds it, but the allowance is a matrix and is not tied to named debtors.
- The credit risk text says "All debtors are good and realizable within the current financial year" (Note 49 S p.150). The 173.13 over three years and the 16.21 at 2-3 years contradict that sentence.
- Single customer above 10%: customer names and individual shares NOT FOUND IN DOCUMENT. Three customers together = 72.27% of revenue (PY 48.00%) (Note 46 S p.146; Note 47 C p.192). The credit risk text rates concentration "low, as its major customers are Public Sector Undertakings" (Note 49 S p.150).
- Receivables from related parties: debtors 130.24 (PY 34.41) in the RPT table (Note 48 S p.148). The sale-of-service line to subsidiary is 282.92. Separate ageing of these: NOT FOUND IN DOCUMENT.
- Retention money receivable and contract assets as separate lines: NOT FOUND IN DOCUMENT. The policy list mentions "retention money" only as a payable item (Note 1(r) S p.124). The term "mobilisation advance" appears only under liabilities (Note 30 S p.136): advance from customers incl. mobilisation 0.00 (PY 342.23).
- Consolidated differs slightly: gross 11,843.17; overdue less than 6 months 438.22; 6-12 months 135.55; allowance 187.95 (Note 12 C p.178).
- Rating: RED for working-capital stress (days up, billed receivables doubled, advances from customers fell to nil); YELLOW for the 173.13 tail; feeds FLAG-CASH.

### 4b. ECL

Allowance 187.95 = 100.78 opening + 87.17 charge (derived; Note 39 S shows 87.18, p.138). No write-offs from the allowance in FY26 disclosed. Deferred tax asset on loss allowance 47.30 (PY 25.36) (Note 44 S p.141). First recognised in FY25 (DTA movement from nil, Note 44 S p.141 prior-year table). ECL matrix: NOT FOUND IN DOCUMENT.

## 5. INVENTORY (Note 11 S p.130; Note 33 S p.137)

| Item | FY26 | FY25 |
|---|---|---|
| Stores, spares and diesel | 5,093.93 | 4,624.04 |
| Opening | 4,624.04 | 4,342.36 |
| Purchases | 4,128.52 | 3,140.16 |
| Consumed (cost of materials) | 3,658.63 | 2,858.48 |

- Single category only; there is no finished goods or WIP line, so "finished goods vs revenue growth" does not apply. Inventory +10.2% vs revenue +35.6% (derived).
- Closing inventory is 139% of annual consumption (5,093.93 / 3,658.63; derived), or about 508 days. FY25: 4,624.04 / 2,858.48 = 162%, about 590 days (derived). A stock of spares and diesel above one year of use is large for a contractor. No stock ageing, no slow-moving split, no NRV test or write-down is disclosed: NOT FOUND IN DOCUMENT.
- The company's inventory turnover is 5.00 vs 4.00 (Note 51 S p.154), computed on revenue, not on consumption.
- Hypothecated to working capital lenders (Note 11 S note). Rating YELLOW.
- "Sundry assets written off" 197.79 (PY 43.86) is a separate other-expense line (Note 39 S p.138). What was written off: NOT FOUND IN DOCUMENT. Cash flow adds it back (Cash flow S p.115). It is 4.5x the prior year. YELLOW.

## 6. INVESTMENTS

### 6a. Note 7 S p.129-130 (cost basis, INR Lakhs); consolidated carrying values from Note 7 C p.176

| Entity | Holding | Standalone carrying FY26 | FY25 | Consolidated carrying FY26 | FY25 | Basis |
|---|---|---|---|---|---|---|
| South West Resources Pvt Ltd (SWR) | 100% (5,00,000 sh) | 42.38 | 42.38 | eliminated | | Cost |
| South West Oil Field Services Pvt Ltd (SWOFS) | 74% (7,400 sh) | 0.74 | 0.74 | eliminated | | Cost |
| South West Geo Services Pvt Ltd (SWGS) | 100% (10,000 sh) | 1.00 | 1.00 | eliminated | | Cost. Note 7 S shows 1.00 in both years although the cash flow shows the 1.00 invested in FY25 and Note 7(c) gives a 2025 CIN. |
| Alara Resources LLC (Oman) | 35% (52,500 sh) | 111.66 | 111.66 | 500.97 | 339.90 | Cost S; equity method C |
| South West Samit JV (AOP) | 80% | 0.08 | 0.08 | 10.70 | 24.87 | Cost S; equity method C |
| Al Hadeetha Mining LLC (Oman) | 17.5% (17,500 sh) | 39.92 | nil | 39.92 | nil | Cost S; equity method C (nil share of profit) |
| Alara Resources Ltd (Australia, listed) | 1.56% (1,25,00,000 sh) | 274.76 | nil | 274.76 | nil | FVOCI, Level 1 |
| Other investments | | 69.85 | 162.53 | 69.85 | 162.53 | FVOCI, Level 1 |
| Total | | 540.39 | 318.39 | 896.20 | 527.30 | |

- Level 1 investments 344.61 = 69.85 + 274.76 (Note 49 S p.149). Fixed deposits are not in this table.
- Al Hadeetha: new this year, 39.92 paid in FY26 (Cash flow S p.115). Group share of profit nil (Note 52 C p.202). Summarised statement (100% basis): current assets 427.40, current liabilities 207.14, non-current assets 743.68, non-current liabilities 720.79, net assets 243.14 (Note 51 C p.201). Non-current liabilities of 720.79 against 17.5% equity holding: the lenders to the JV are not named (NOT FOUND IN DOCUMENT). The Note 1 narrative says the JV "has recently been allocated a mining block... 1448 Sq Km" (Note 1 S p.116). A 17.5% holding is treated as a jointly controlled entity. The judgement on joint control: NOT FOUND IN DOCUMENT.
- Alara Resources LLC, 100% basis (Note 50 C p.200): total income 14,960.25 (PY 6,444.12, +132%, derived); profit 460.20 (PY 365.38); net assets 1,184.83 (PY 627.40); current assets 9,139.05 (PY 17,681.84); current liabilities 7,658.10 (PY 17,056.08). Net margin 3.1% vs 5.7% (derived). Share of profit 161.07 (PY 127.88). Carrying 500.97 = cost 111.66 plus cumulative share of profit 389.31 (the 389.31 appears in Note 52 C p.202; the sum is derived). Carrying exceeds 35% of net assets (414.69) by 86.28 (derived); no goodwill is disclosed. Cash dividends from the JV: none in other income (Note 32 S p.137), so the group profit from this JV is non-cash to date.
- South West Samit JV: loss (17.71), group share (14.17) (Note 51 C p.201).
- Impairments: none disclosed. SWR has negative net worth (264.94) while the parent holds it at 42.38 (see Section 2e).
- Loans given (ICDs): current loans to related parties 410.34 (all SWR, Note 52 S p.154); non-current loans to related parties 257.86 (Note 8 S p.130), OMR-denominated (1.06 million OMR, 257.86 INR, FX table Note 49 S p.152). Which Omani JV owes this: NOT FOUND IN DOCUMENT. Non-current loan +183% (91.09 to 257.86; derived). Interest on loans total 27.04 (Note 32 S p.137). Rate and tenor of each loan: NOT FOUND IN DOCUMENT.
- Unrealised gains/losses: OCI reserve 105.45 (PY 115.66); FY26 movement (10.21) (Note 19 S p.133).
- Share warrants outstanding by promoter group: see Section 12.

## 7. BORROWINGS

### 7a. Instrument table, standalone

| Instrument | FY26 | FY25 | Rate | Security | Anchor |
|---|---|---|---|---|---|
| Term loans, banks (non-current) | 1,559.30 | 1,073.67 | Fixed at drawdown, 8.00-9.00% | Hypothecation of vehicles, rigs, mud pumps, compressors, commercial vehicles and excavators, plus personal guarantees of directors | Note 20 S p.134 |
| Term loans, NBFC (non-current) | 40.14 | 146.95 | Fixed at drawdown, 8.70-9.75% | Rigs, logging unit, misc assets | Note 20 S p.134 |
| Total non-current | 1,599.44 | 1,220.62 | | | |
| Current maturities, banks | 1,937.06 | 1,204.89 | | | Note 25 S p.135 |
| Current maturities, NBFC | 87.79 | 369.58 | | | Note 25 S p.135 |
| CC, WCDL, drop-line overdraft (banks) | 4,237.05 | 3,496.30 | 8.00-9.00% | Entire stock and book debts, FDs as collateral, promoter guarantees, equitable mortgages at Gurugram, Ranchi (HDFC) and Nagpur (Axis) | Note 25 S p.135 |
| Total current | 6,261.90 | 5,070.77 | | | |
| Total borrowings | 7,861.34 (1,599.44 + 6,261.90) | 6,291.39 | | | Note 49a S p.149 |

- Repayment profile as disclosed: next one year 2,024.84; one to five years 1,599.44; total 3,624.28 (PY 1,574.48; 1,220.62; 2,795.10) (Note 20 S p.134). A year-by-year 5-year schedule: NOT FOUND IN DOCUMENT. Nothing falls beyond five years.
- Covenants, breaches and waivers: NOT FOUND IN DOCUMENT. Statement: "There is no default as on balance sheet date in repayment of loans and servicing of interest" (Note 20 S p.134; Note 25 S p.135).
- Fixed versus floating: Note 49 S p.152 reports fixed 1,132.21 (PY 1,184.23) and floating 6,729.13 (PY 5,107.16). A 50 bp move = 33.65 on profit before tax (Note 49 S p.153). This conflicts with Note 20, which states term loans are fixed. See Pass 3.
- Borrowings grew 24.9% (7,861.34 vs 6,291.39; derived). Term loan proceeds 2,908.66, repayments 2,079.48, net short-term +740.74 (Cash flow S p.115, financing reconciliation).
- Finance cost 842.34 (interest 777.45 + other 64.89) vs 868.73 (Note 37 S p.138). Interest 777.45 on average gross borrowings of 7,076.37 ((7,861.34 + 6,291.39)/2) is 10.99% (derived). The stated rate range is 8.00-9.75%. The gap is unexplained: NOT FOUND IN DOCUMENT. YELLOW.
- Net debt 6,730.01 (PY 2,309.53); gearing 33.23% (PY 13.44%); total equity 20,251.42 (Note 49c S p.153). Net debt deducts 1,042.52 of fixed deposits, which the notes call margin money against fund and non-fund facilities (Note 14 S p.131). Margin money is not free cash. Net debt without that deduction: 7,772.53 (derived).
- Related party borrowings: none standalone. Consolidated unsecured loan from related parties 0.50 (Note 26 C p.181).
- Ratios: debt-equity 0.39 (PY 0.37); debt service cover 1.79 (PY 1.05); current ratio 1.86 (PY 2.17) (Note 51 S p.154).
- Rating YELLOW. Debt rose while the cash-and-bank line fell, see Section 12.

## 8. TRADE PAYABLES (Note 26 S p.136; Note 43 S p.140)

| Bucket | MSME | Others | Total |
|---|---|---|---|
| Not due | 184.43 | 2,009.60 | 2,194.03 |
| Due, under 1 year | 1.78 | 131.43 | 133.21 |
| 1-2 years | - | 28.74 | 28.74 |
| 2-3 years | - | 12.37 | 12.37 |
| Over 3 years | - | 18.91 | 18.91 |
| Total FY26 | 186.21 | 2,201.06 | 2,387.27 |
| Total FY25 | 462.34 | 1,361.46 | 1,823.80 |

- Payables +30.9% (derived), against revenue +35.6%.
- Past due and over a year: 60.02 (28.74+12.37+18.91; derived). FY25 equivalent 39.09 (20.18+18.91; derived). No disputed dues.
- MSME: principal 186.21 outstanding; "Principal amount overdue more than 45 days" shown as nil; interest due, paid and accrued all nil (Note 43 S p.140). The MSME ageing shows 1.78 past due in the under 1 year bucket, so the under-45-days or over-45-days split is not visible. Disclosure is "to the extent such parties have been identified", a limiting phrase. YELLOW (minor).
- Payables turnover 7.33 vs 9.79, -25.16% (Note 51 S p.154). 365/7.33 = 49.8 days vs 37.3 days (derived). Payment days lengthened.
- Payables are described as "usually paid within 30 to 120 days" (Note 1(r) S p.124).

## 9. PROVISIONS

- Employee benefits (Note 45 S pp.142-145; Note 46 C pp.187-190): gratuity is "Funded" via an HDFC Life trust. Obligation 212.55 (PY 200.05). Plan assets 2.83 (PY 0.66). Net liability 209.72 (balance sheet 209.73; Note 22 S 12.67 + Note 28 S 197.06 = 209.73 derived). Funded ratio 1.3% (derived). Employer contribution 40.00 (PY 43.01). Benefits paid 37.91 (PY 52.47). Expense to P&L 47.10 (PY 42.73); OCI loss 3.23 (PY 21.40).
- Actuarial assumptions: discount rate 7.78% (PY 6.89%); salary escalation 2.00% (both years); attrition 2.68% (both years); mortality IALM 2012-14 urban. Active members 802 (PY 558, +43.7%; derived). Salary escalation of 2% and attrition of 2.68% are both low for a field workforce that grew 43.7% in a year. The effect, if both were set higher, is not shown. YELLOW (not a quantified risk: sensitivity +1% salary = +18.51, -1% discount = +19.93).
- Sensitivity: +1% discount rate (17.21); -1% 19.93; +1% salary 18.51; -1% (16.54); +1% turnover 11.10; -1% (12.59) (Note 45 S p.144).
- Table labels: "Per Month Salary For Active Members 197.06" and "Prescribed Contribution For Next Year 197.06" repeat the current gratuity provision figure exactly (Note 45 S p.144). Those labels do not match a salary figure. PBO "on current assumptions" for the prior year is shown as 211.82 against 200.05 reported (Note 45 S p.144). Actuarial table quality YELLOW.
- Leave encashment: unfunded; liability 23.73 (current 4.43, non-current 19.29/19.30); discontinuance liability 37.47; discount rate 7.78% (Note 45 S p.145).
- Warranty, decommissioning, onerous contracts: NOT FOUND IN DOCUMENT. No provision note exists beyond employee benefits.
- Litigation provisions: NOT FOUND IN DOCUMENT. All disputes are contingent, none provided (Section 3).
- Current tax liability (net of advance tax and TDS) 561.35 (PY 125.28), 4.5x (Note 29 S p.136; derived). Current tax charge 1,091.24; taxes paid in cash flow 655.17 (Cash flow S p.115).
- Statutory liabilities 579.69 (PY 382.86) (Note 30 S p.136). YELLOW only because it rose with payroll and GST; ageing: NOT FOUND IN DOCUMENT.

## 10. DEFERRED TAX AND TAX EXPENSE

- Standalone (Note 44 S p.141): current tax 1,091.24 (PY 506.23); earlier-year adjustment nil (PY (63.34)); deferred (40.49) (PY 52.36); total 1,050.75 (PY 495.25). PBT 4,130.80 (PY 1,977.76). Applicable rate 25.17%; computed tax 1,039.64; non-deductible items 10.47; other 0.64; effective rate 25.44% (PY 25.04%).
- Consolidated: PBT 4,206.55 before JV share; tax 1,050.75; effective 24.98% (Note 45 C p.187). Share of JV profit 146.90 is taxed outside this.
- Net DTL 470.36 (PY 514.69): DTL 638.09, DTA 167.73. DTL on PPE 449.66 (PY 412.42). DTA on loss allowance 47.30; on gratuity and leave 79.04; on ROU liability 38.35 (Note 44 S p.141 and Note 23 S p.135).
- A "Deferred expense" DTL of 57.81 reversed to nil in FY26 (Note 44 S p.141). The nature of this deferred expense: NOT FOUND IN DOCUMENT.
- MAT credit: NOT FOUND IN DOCUMENT (not in use, standard 25.17% rate). Unrecognised DTA: NOT FOUND IN DOCUMENT.
- Rating GREEN. DTA is small and backed by a profitable standalone.

## 11. REVENUE DETAILS

- Standalone (Note 31 S p.137): sale of services 24,266.75 (PY 13,316.53); sale of products 26.20 (PY 4,602.79); total 24,292.95 (PY 17,919.32, +35.6%; derived). Consolidated: services 24,275.97 (PY 13,426.71); products 26.20 (PY 4,602.79); total 24,302.17 (PY 18,029.50) (Note 32 C p.183).
- Services revenue +82.2% (24,266.75 vs 13,316.53; derived). The FY25 base held 4,602.79 of product sales, which the segment note ties to coal trading: Coal Mining & Trading revenue nil in FY26 vs 4,533.92 in FY25, segment profit nil vs 43.00 (Note 47 C p.192). Matching stock-in-trade purchase 4,490.92 in FY25, nil in FY26 (Note 35 S p.137). Coal trading earned about 0.9% on sales (43.00/4,533.92; derived) and has stopped.
- Segments: Drilling & Exploration revenue 24,302.17 (PY 13,495.58); Coal Mining & Trading nil (PY 4,533.92). Segment assets: Drilling 31,281.15 (PY 26,174.20); Coal 1,930.58 (PY 1,430.81), which is the E&E asset only. Segment liabilities: Drilling 12,858.78 (PY 10,542.16) (Note 47 C p.192). Segment assets less liabilities = 20,352.95, ties to Schedule III net assets 20,352.94 (Note 52 C p.202).
- Geography: domestic 24,286.80 (S) / 24,296.02 (C); overseas 6.15 (PY 37.21) (Note 46 S p.146; Note 47 C p.192).
- Customer concentration: three customers = 72.27% of revenue (PY 48.00%) (Note 46 S p.146). On standalone revenue that is about 17,556 (derived: 0.7227 x 24,292.95). Names: NOT FOUND IN DOCUMENT in the notes. Board's report names CMPDI among PSU clients (p.40); not a note.
- Contract assets and contract liabilities: contract assets are inside "Unbilled" 2,613.79 (PY 2,958.08). Contract liabilities: advance from customers incl. mobilisation advance nil (PY 342.23) (Note 30 S p.136). Separate Ind AS 115 contract balance reconciliation: NOT FOUND IN DOCUMENT.
- Unsatisfied performance obligations / remaining performance obligation disclosure: NOT FOUND IN DOCUMENT. The Board's report states "robust order book of over approx. Rs. 761 crores" and 15% to 20% revenue growth (p.40). This is outside the notes and is not a disclosed note figure.
- Operating expenses (Note 35 S p.137): cost of sub-contract work and technical fees 8,109.98 (PY 2,539.14, +219%; derived). That is 33.4% of FY26 revenue vs 14.2% in FY25 (derived). Total operating expenses 10,407.30 (PY 3,967.08). Hire charges 950.94 (PY 607.77). Consultancy charges (operations) 360.99 (PY 63.97). The sub-contractors' identity and the related-party share: NOT FOUND IN DOCUMENT beyond the subsidiary drilling purchases of 632.01 (Section 2). RED/YELLOW: revenue growth was bought with outside labour at lower implied margin; this is a margin-mix signal, not a violation. Rating YELLOW.
- Other income 358.66 (PY 467.94): interest on FDs 143.25; gain on sale of assets 26.52 (PY 206.22); FX gain 39.34 (PY 2.07, unrealised per cash flow add-back); rental income 120.12; sundry liabilities written off nil (PY 40.83) (Note 32 S p.137). The FX gain is unrealised (Cash flow S p.115).

## 12. OTHER CRITICAL NOTES

- Exceptional items: none reported. Share of JV profit sits below PBT in consolidated (146.90, Note 47 C p.192).
- Goodwill: consolidated goodwill policy only; the consolidated balance carries "Goodwill 11.21" (balance sheet line near p.166); no impairment test described. Not a note finding.
- Intangibles: only the E&E item. Ageing (Note 5 S p.129): under 1 year 499.77; 1-2 years 348.91; 2-3 years 324.17; over 3 years 757.73; total 1,930.58 (PY 1,430.81). Cash outflow in FY26 499.77 (Cash flow S p.115). The note states no project is "overdue or has exceeded its cost compared to its original plan". The coal block was allocated in 2021-22 (Note 1 S p.116); 757.73 of the asset is older than three years. Note 1 says the PL cum ML process "is presently underway" (Note 1 S p.116), while the Board's report says exploration is "completed" (p.40-41). No impairment trigger test is disclosed. YELLOW.
- Capital commitments 1,720.64 (PY 2,497.60) (Note 42B C p.185). Capital advances 226.11 (PY 312.49) (Note 10 S p.130).
- PPE (Note 2 S p.127): gross block 16,440.01 (PY 12,606.49). Additions 4,281.38, of which plant and equipment 3,900.25 (PY 46.19 total additions in plant). Disposals gross 447.86; accumulated depreciation reversal 185.74; gain on sale 26.52 (Note 32 S p.137). Net block 9,177.91 (PY 6,250.13); net plant 8,488.25 (PY 5,762.30). Depreciation for the year 1,091.49 (PY 904.17).
- CWIP 40.42 (PY 67.17): a core drilling project in Rajasthan (Note 3 S p.128).
- Investment property: gross 743.82, net 257.85; rental income 120.12; "Fair market value of properties is INR 1,406 Lakhs, ... valuations carried out by the bank and shared with the Company" (Note 4 S p.128), while the policy says an independent valuer is used (Note 1(f) S p.118). YELLOW (minor).
- Lease equalisation reserve 438.30 (PY 422.44), shown as other non-current financial asset (Note 9 S p.130). Nature: NOT FOUND IN DOCUMENT. It exceeds the investment property net block (257.85), so straight-lining of own rent cannot explain it. YELLOW.
- Other current assets include "Accrued expenses 384.32" (PY 585.40) as an asset (Note 17 S p.132). Label unclear; probably accrued income. YELLOW (minor).
- Foreign currency (Note 49 S p.152): exposures not hedged by derivatives. USD liabilities 0.17 million (16.10 INR); EUR 0.32 INR; OMR asset 1.06 million (257.86 INR). 5% move on OMR = 12.89. Hedging policy: "follows established risk management policies"; instruments: none. GREEN (small).
- EPS (Note 40 S p.139): basic 10.33 (PY 5.27); diluted 10.09 (PY 5.26). Weighted shares 2,98,30,011 (PY 2,81,08,364) basic and 3,05,35,364 diluted. Gap 0.24 per share = 2.3% (derived). Source: warrants. Consolidated basic 11.07, diluted 10.82 (Note 41 C p.184).
- Share capital (Note 18 S p.132-133): 2,98,30,011 shares of Rs 10 = 2,983.00; no change in FY26; in FY25, 19,27,611 shares issued on preferential basis at Rs 132.20, receiving 2,548.30. Promoter and promoter group hold 2,05,38,783 shares = 68.85% at 31 Mar 2026 and at 31 Mar 2025 (Note 18(e) S p.133). Vikas Jain 1,18,18,922 (39.62%); Piyush Jain 69,19,861 (23.20%). Bonus shares: cumulative 1,86,01,200 (Note 18(d) S p.133). Pledge of promoter shares: NOT FOUND IN DOCUMENT in the notes.
- Warrants (Note 19 S p.134): 28,21,411 warrants at Rs 132.20 to promoter and non-promoter groups, total 3,729.91; 25% received = 932.48 (held as "Share warrant" in equity); 18 months from allotment on 21 Feb 2025 to pay the balance 75%. Balance due = 3,729.91 - 932.48 = 2,797.43 (derived). Split between promoter and non-promoter: NOT FOUND IN DOCUMENT. Dividend: none in FY26 (PY 36.82) (Note 19 S p.133).
- Reserves: OCI direct credits/debits bypassing P&L: FV loss on investments (10.21); actuarial loss (2.42) net of tax in retained earnings (Note 19 S p.133).
- CSR (Note 47 S p.146; Note 48 C p.193): required 27.03 (PY 24.80); spent 24.26 (PY 27.69); opening excess 4.91; closing excess 2.14 (4.91 + 24.26 - 27.03 = 2.14, derived). Shortfall nil after carry-forward of the prior excess. GREEN. The standalone text of this table is scrambled; the consolidated table reads cleanly.
- Segment (Note 46 S p.146 / Note 47 C p.192): see Section 11.
- Events after the balance sheet date: NOT FOUND IN DOCUMENT as a note. No subsequent events note in the standalone or consolidated set.
- Cash conversion cross-read (Cash flow S p.115; outside the notes, shown because load-bearing fact 4): operating profit before working capital 6,045.46 (PY 3,484.68); receivables increase (4,456.25) (PY (1,950.76)); inventory (469.89); payables +563.48; cash generated from operations 1,889.04 (PY 2,900.31); taxes paid (655.17); CFO 1,233.87 (PY 2,604.58). Capex (PPE) (4,254.36) and E&E (499.77). CFO less those two = (3,520.26) (derived). Cash and cash equivalents 88.81 (PY 1,824.50); fixed deposits with banks (Note 14) 1,042.52 (PY 2,157.36) and non-current FDs 348.05 (PY 71.96) (Note 9). All FDs are margin money (Notes 9 and 14 S). Receivables absorbed 73.7% of pre-working-capital operating profit (derived).
- Ratios stated by the company (Note 51 S p.154): current ratio 1.86 (2.17); DSCR 1.79 (1.05); ROE 16.46% (10.01%); inventory turnover 5.00 (4.00); receivable turnover 2.55 (2.74); payable turnover 7.33 (9.79); net capital turnover 2.57 (2.27); net profit ratio 12.68% (8.27%); ROCE 22.06% (11.94%); ROI 12.03% (4.54%). Management comment on payables ("reduction in Trade Payables") contradicts the numbers; see Pass 3.

## PASS 1 SUMMARY: TOP 10 FINDINGS BY INVESTOR IMPORTANCE

| Rank | Finding | Note anchor | Rating |
|---|---|---|---|
| 1 | Cash conversion under rig capex is weak. Gross receivables +57.0% vs revenue +35.6%. Billed receivables 9,218.67 vs 4,576.59 (+101%). Receivable days (derived) 177.8 vs 153.5. CFO 1,233.87 vs PAT 3,080.05. Cash and cash equivalents fell to 88.81 from 1,824.50 while borrowings rose 1,569.95. Customer advance of 342.23 went to nil. | Note 12 S p.131; Note 30 S p.136; Note 25 S p.135; Cash flow S p.115 | RED |
| 2 | Customer concentration moved up: three customers = 72.27% of revenue (PY 48.00%). Names not disclosed. The credit-risk note calls concentration "low" because customers are PSUs. | Note 46 S p.146; Note 49 S p.150 | RED |
| 3 | Subsidiary SWR has net worth (264.94) and a going-concern emphasis from its auditor. The parent holds a 410.34 loan to it (61.41% of all loans) and a 42.38 investment, and buys 632.01 of drilling services from it. No ECL and no impairment disclosed. | Note 52 S p.154; Note 7 S p.129; Auditor's report C p.159; Note 52 C p.202 | RED |
| 4 | E&E asset 1,930.58 (Jharkhand coal block) with 757.73 older than three years, no E&E policy, no impairment test disclosed, and a segment with nil revenue. | Note 5 S p.129; Note 47 C p.192; Note 1 S p.116 | YELLOW (RED for policy gap) |
| 5 | Related-party and promoter-linked capital: 288.00 spent on 1.56% of Alara Resources Ltd (a KMP-influenced enterprise), fair value 274.76 at year end; a 1,100.00 loan to an unnamed KMP-influenced enterprise cycled in the year (PY 950.00); 39.92 into the 17.5% Al Hadeetha JV; loan to Omani JV 257.86 (+183%). | Note 48 S p.148; Note 7 S p.129-130; Note 8 S p.130; Cash flow S p.115 | RED (loan opacity) / YELLOW |
| 6 | Fixed or floating contradiction: Note 20 says term loans are fixed at 8.00-9.75%, but Note 49 puts 6,729.13 of 7,861.34 borrowings in floating. Implied interest on average debt is 10.99% against the 8.00-9.75% stated range. | Note 20 S p.134; Note 49 S p.152; Note 37 S p.138 | YELLOW |
| 7 | Contingent liabilities 2,812.69 = 13.8% of net assets. New GST demand of 397.59 for FY2021-22 at the appellate stage. Bank guarantees 2,250.07 alone = 11.1% of net assets. | Note 42 C p.185 | YELLOW |
| 8 | Cost mix: sub-contract and technical fees 8,109.98, up 219%, now 33.4% of revenue. Coal trading (revenue 4,533.92, thin margin) ended. Services revenue +82.2%. Revenue quality depends on outsourced execution. | Note 35 S p.137; Note 47 C p.192 | YELLOW |
| 9 | Inventory of spares and diesel 5,093.93 equals 139% of one year of consumption (derived), with no ageing or NRV note. "Sundry assets written off" 197.79 (PY 43.86) unexplained. | Note 11 S p.130; Note 33 S p.137; Note 39 S p.138 | YELLOW |
| 10 | Rig capex of 4,281.38 landed in FY26 (plant net block +47.3%, derived), 1,720.64 more committed, funded by net bank debt. Gearing 33.23% vs 13.44% (and the net debt nets off margin-money FDs of 1,042.52). 75% balance on 28,21,411 warrants (2,797.43) is the identified equity inflow. | Note 2 S p.127; Note 42B C p.185; Note 49c S p.153; Note 19 S p.134 | YELLOW |

Near misses not ranked: Alara Resources LLC carrying 500.97 exceeds 35% of its net assets by 86.28 (derived), with no cash dividends; remuneration +75.2%; investment property valuation by bank not independent valuer; 15 notes flagged as NOT FOUND IN DOCUMENT are listed inline.

## NOT FOUND IN DOCUMENT register (expected disclosures absent)

E&E accounting policy; numeric useful lives; capitalised borrowing cost amount; ECL matrix rates; related-party ageing of receivables; loan terms (rate, tenor) for SWR, Omani JV loans and the 1,100.00 loan; name of the 1,100.00 borrower; names of top-3 customers; remaining performance obligations; contract asset/liability reconciliation; retention receivable; financial covenants and waivers; year-by-year repayment schedule; stock ageing and NRV; reason for tax contingencies changing; probability of outflow on any contingency; warranty and decommissioning provisions; subsequent events note; pledge of promoter shares; split of warrants between promoter and non-promoter; basis for joint control at 17.5% (Al Hadeetha); standalone Note 41 body and Note 46 segment table (text extraction gap).
