# Stage 2, Pass 1 of 3: Notes to Financial Statements, full extraction
Company: ACCORD (Accord Transformer & Switchgear Ltd, BSE SME 544710). Run date 2026-10-06. Model claude-sonnet-5-5.
Source: runs/accord-2026-10-06/inputs/annual-report/Annual_Report_2026.txt (FY2025-26 AR, 12th AR, standalone). Prospectus used only for one lease fact.

Conventions
- Unit: Rs lakh as printed on the face ("All amounts are in lakhs of Indian Rupees", p.77, p.85). No conversion in this pass. 100 lakh = 1 Cr; stage 10 converts.
- Anchors: (Note N, p.X). p.X is the "[page X]" marker of the text file. Printed AR page = p.X + 18 (for example p.85 is printed "Annual Report 25-26 103"). Statement pages: Balance Sheet p.77, P&L p.78, Cash Flow p.79.
- Ratings: [GREEN] clean, [YELLOW] watch, [RED] red flag. Calculations by this pass are marked (calc).
- Framework: Indian GAAP with Accounting Standards (AS), not Ind AS (Note 1A, p.80). Ind AS 116, ECL matrix and Ind AS 36 items are not applicable. No consolidation: no subsidiaries, JVs or associates (CARO ix(e), p.73).
- Structure defects in the notes: Note 12 (fixed assets schedule) is absent from the text layer between Note 11 and Note 13 (p.88). PDF page rendering was not available in this session (pdftoppm missing), so page images were not checked. Two different notes are numbered "Note 28" (Other Expenses p.92; Employee Benefits p.93). Notes 2.1 to 2.11 sit under a heading "2. Notes to Financial Statements" (p.81-84) before Note 3.

---------------------------------------------------------------------

## A. LOAD-BEARING FACTS FIRST (LBF-2 and LBF-4)

### LBF-2: short-term loans and advances Rs 63.86 lakh -> Rs 890.45 lakh
Operator context says 0.64 -> 8.90 Cr, purpose unknown. HOLDS: 63.86 -> 890.45 lakh (Balance Sheet, p.77; Note 17, p.90).

Note 17 composition (Note 17, p.90), Rs lakh:
| Component | 31-Mar-26 | 31-Mar-25 | Change | Share of FY26 total |
|---|---|---|---|---|
| Balance with revenue authorities | 194.64 | 22.29 | +172.35 | 21.9% (calc) |
| Vendor advances | 624.41 | 31.17 | +593.24 | 70.1% (calc) |
| Loan & Advances | 15.23 | 3.01 | +12.22 | 1.7% (calc) |
| Prepaid expenses for IPO | 0 | 6.23 | -6.23 | 0 |
| Retention money | 56.17 | 1.16 | +55.01 | 6.3% (calc) |
| Total | 890.45 | 63.86 | +826.59 | 100% |

Findings
1. The jump is 70% vendor advances (624.41). The note gives no vendor names, no ageing and no related-party tag. Counterparty: NOT FOUND IN DOCUMENT. Purpose beyond the label "Vendor advances": NOT FOUND IN DOCUMENT. Size: 20x YoY and 8.9% of revenue (calc 624.41 / 7,006.92). [RED for disclosure gap, because unexplained and large]
2. Related-party link: the related-party note (Note 2.3, p.81-82) lists no advance to any related party. The AOC-2 table has a column "Amount paid as Advances" and shows "-" for both related parties (AOC-2, p.54). On filed evidence no related-party advance exists. Whether a vendor is an unlisted related party cannot be tested from the document.
3. CARO clause (iii): the auditor reports Nil guarantees, security, loans and advances in the nature of loans to any party, both "provided during the year" and "outstanding" (CARO iii(a), p.72; iii(b) to (f), p.73). The table header reads "(Rs in Thousands)" while the statements are in lakh. The (iii)(b) text says "as at 31st March, 2025", a stale year reference. Reading: the auditor treats the Rs 890.45 lakh as trade or operating advances, not loans. [YELLOW: the CARO text is template quality]
4. The "Loan & Advances" head, Rs 15.23 lakh, is the only item that could be a loan (employee or other). No party named. Small.
5. Cross-link to stock: Stock in Transit Rs 619.50 lakh (Note 14, p.89) is new (FY25 nil) and sits within 0.8% of vendor advances Rs 624.41 lakh. The notes do not say whether the advances and the in-transit stock are the same purchases. Open question for the verifier and the operator, not a finding of double counting. [YELLOW]
6. Revenue-authority balance Rs 194.64 lakh (Note 17) is 8.7x last year. Composition (GST input credit, advance tax, TDS/TCS) NOT FOUND IN DOCUMENT. Direct taxes paid in the cash flow (253.77, p.79) equal the FY25 provision 99.93 plus FY26 current tax 153.84 (Note 11, p.88; P&L p.78) (calc), so the rise is not advance-tax over-payment; GST or other credits are likely (inference, not stated).
7. Cash flow shows "Changes in Loan & Advances (909.34)" (p.79). This ties to Note 17 +826.59, Note 18 +56.05, Note 13 +26.69 = 909.33 (calc). Reconciled.

### LBF-4: CFO Rs 869.50 lakh vs PAT Rs 450.43 lakh; cash; inventory days
Operator context: CFO 8.70 Cr, PAT 4.50 Cr, cash 22.3 Cr, inventory days about 179. HOLDS on CFO, PAT and cash. Inventory days: see finding 7.

Cash-flow bridge (Cash Flow, p.79), Rs lakh:
| Line | FY26 | FY25 |
|---|---|---|
| Operating profit before WC | 705.54 | 900.23 |
| Inventories | (626.82) | (745.26) |
| Trade receivables | +1,349.33 | (2,173.28) |
| Loans and advances | (909.34) | (114.64) |
| Provisions | +19.95 | +31.15 |
| Trade payables | +345.37 | +739.86 |
| Other current liabilities | +239.23 | +717.17 |
| Direct taxes paid | (253.77) | (173.33) |
| CFO | 869.50 | (818.10) |

Findings
1. FY26 CFO is a release of FY25's receivable build. Receivables fell 1,349.33 (Note 15, p.89) after rising 2,173.28 in FY25. Without that release, CFO would be (479.83) (calc 869.50 - 1,349.33). The release does not repeat unless receivables fall again. [YELLOW]
2. Two-year view: CFO FY25 (818.10) + FY26 869.50 = +51.40; PAT FY25 594.37 + FY26 450.43 = 1,044.80 (calc). Two-year cash conversion is 4.9% of PAT. [RED for repeatability; supports FLAG-CASH]
3. Supplier and customer funding: MSME dues rose 637.28 -> 1,494.94 (+857.66) while other creditors fell 874.12 -> 361.82 (-512.30) (Note 9, p.87). Total payables +345.37. Customer advances rose 248.42 -> 449.36 (+200.94) (Note 10, p.88). FY26 CFO carries +546.31 of payables and customer-advance funding (calc 345.37 + 200.94). [YELLOW]
4. Cash Rs 2,232.80 lakh (Note 16, p.90) breaks into: cash 2.05; current accounts 740.65; FD under 3 months 600.00 = 1,342.70 cash and equivalents (ties to Cash Flow closing, p.79); FD over 3 months 890.11 (including collateral). Operator "cash 22.3 Cr" is the total of all four. HOLDS, but it is a broad figure.
5. IPO money inside that cash: the auditor reports Rs 2,040.21 lakh of IPO proceeds still "lying in fixed deposits/current accounts" at 31-Mar-26 (CARO x(a), p.73). That is 91.4% of Rs 2,232.80 lakh (calc). Cash not tied to IPO: 192.59 lakh (calc 2,232.80 - 2,040.21). [RED for a "cash-rich" reading: the cash is IPO money earmarked for objects]
6. FD collateral: margin money FDR against bank guarantees Rs 181.95909 lakh (FY25 118.67561) (Note 2.5, p.83); Note 2.11(g) writes the prior year as 1,18,68,561, a Rs 1,000 mismatch (p.84). Immaterial. [GREEN]
7. Inventory days. The AR's Note 30 inventory turnover is 2.51 vs 5.51 (p.95), which is 145 days vs 66 days (calc 365/2.51; 365/5.51). Closing inventory 2,434.87 over raw materials consumed 4,930.72 gives 180 days (calc), which matches the operator's "about 179". The operator's figure reproduces only on a closing-stock over raw-material-consumed basis. Stage 10 must fix the basis. [YELLOW]
8. The MD&A text (p.65, "The improvement in receivables turnover indicates better working capital management") contradicts its own ratio table (p.64): receivables turnover fell 4.48 -> 3.22 and the table reason reads "relatively slower conversion". The same table says current ratio improved "particularly trade receivables", while receivables fell from 2,850.81 to 1,501.48. [YELLOW: management narrative contradicts the notes]
9. Contingent liabilities for LBF-4: see section 3.

---------------------------------------------------------------------

## 0. OPERATOR-CONTEXT CHECK (operator-notes.md, 2026-10-06) against the AR
| Operator figure | AR figure (Rs lakh) | Anchor | Status |
|---|---|---|---|
| Revenue 70.07 Cr | 7,006.92 | P&L p.78; Note 19 p.90 | HOLDS |
| Other income 0.29 Cr | 28.78 | Note 20 p.90 | HOLDS |
| D&A 0.63 Cr | 62.60 | Note 26 p.92 | HOLDS |
| Finance cost 0.55 Cr | 55.04 | Note 25 p.91 | HOLDS |
| PBT 6.06 Cr | 605.75 | P&L p.78 | HOLDS |
| PAT 4.50 Cr | 450.43 | P&L p.78 | HOLDS |
| Operating EBITDA 6.95 Cr (9.9%) | 694.61 = PBT 605.75 + finance 55.04 + D&A 62.60 - other income 28.78 (calc); 9.91% of revenue (calc). Management EBITDA incl. other income 723.39, 10.39% (MD&A p.64) | p.64, p.78 | HOLDS (basis: excl. other income) |
| CFO 8.70 Cr | 869.50 | Cash Flow p.79 | HOLDS |
| Cash 22.3 Cr | 2,232.80 incl. FDs; 2,040.21 is unspent IPO money | Note 16 p.90; CARO x(a) p.73 | HOLDS, with IPO caveat |
| Shares 2.057 Cr | 2,05,73,289 | Note 3 p.85 | HOLDS |
| Short-term L&A 0.64 -> 8.90 Cr | 63.86 -> 890.45 | Note 17 p.90 | HOLDS |
| Inventory days 179 | 145 (Note 30 basis); 180 (closing / RM consumed basis) | Note 30 p.95; Notes 14, 21 | HOLDS on one basis only |
| ~31 Cr order deferred (site dispute) | NOT FOUND in the notes | n/a | NOT TESTABLE here; for stages 4 and 5 |
| Land Rs 8.85 + 1.82 Cr | NOT FOUND in the notes; no land addition in FY26 (see 12.8) | n/a | NOT IN NOTES |
| FY27 guidance, H1 FY27, NHEV, Aditya Birla | outside the Notes | n/a | not tested here |

---------------------------------------------------------------------

## 1. ACCOUNTING POLICIES AND CHANGES (Note 1, p.80; Notes 2.x p.81-84)
- Basis: historical cost, accrual, Indian GAAP and AS under Section 133 (Note 1A, p.80). [GREEN]
- Policies present: A basis, B estimates, C fixed assets and depreciation, D investments, E revenue, F taxation, G impairment, H provisions, I EPS (Note 1, p.80). Policies ABSENT from Note 1, each NOT FOUND IN DOCUMENT: inventory valuation; employee benefits (the AS-15 disclosure sits in Note 28); foreign currency (a Rs 4.32 lakh FX loss is booked, Note 28 p.92); borrowing costs; lease accounting (a lease rent equalisation reserve of Rs 11.12 lakh exists, Note 10 p.88); government grants (duty drawback Rs 1.62 lakh, Note 20). [YELLOW] The inventory valuation gap matters because FG is up 252% and Stock in Transit is Rs 619.50 lakh (Note 14).
- Revenue recognition: Note 1E cites AS-9 and states recognition "to the extent that it is probable that the economic benefits will flow" (p.80). The KAM adds that control passes "generally upon dispatch or delivery of goods as per the contractual terms" (KAM 1, p.67-68). The policy does not say whether recognition is on dispatch or on delivery. For a transformer maker with "stock in transit" and "dispatch clearance obtained from the customer" (p.67), that fork sets the cut-off. [YELLOW]
- No policy change disclosed and no quantified P&L impact of any change. Note 2.9 says prior-year figures were "regrouped / rearranged wherever necessary", with no amounts (p.83). [YELLOW]
- Depreciation: Schedule II useful lives (Note 1C, p.80), "reviewed periodically". Life-by-class table NOT FOUND (Note 12 absent). Depreciation rose 40.50 -> 62.60 (+54.6%, calc). Net block incl. intangibles under development 711.03 -> 794.62 (calc, Balance Sheet p.77). Capitalisation: "capitalizes all costs relating to acquisition and installation" with no threshold (Note 1C). [YELLOW]
- Impairment: generic text only, no growth or discount-rate assumptions (Note 1G). No goodwill. [GREEN]
- ECL / bad debt provisioning policy: NOT FOUND. Provision for bad and doubtful debts is nil in both years (Note 15, p.89). [YELLOW] See section 4.
- Provisions policy (Note 1H, p.80) ends: "no provision for contingencies is made in the financial statements of current year". No warranty provision exists in Notes 7 or 11 (only gratuity and leave), although bank guarantees of Rs 532.46 lakh are given "to cover the warranty period of Goods" (Note 2.5, p.83). Warranty provision for a transformer maker: NOT FOUND IN DOCUMENT. [YELLOW]
- Ind AS 116: not applicable (AS framework). Lease evidence sits outside the AR notes: the prospectus restated notes record a lease with KMD Transworld (India) Pvt Ltd at Rs 6,00,000 a month with 5% escalation after each 12 months, 58.5 month term (Prospectus, restated-financials notes, lease paragraph). Rent expense is Rs 79.37 lakh in both FY26 and FY25 (Note 28, p.92), flat despite the escalator; the lease rent equalisation reserve moved 9.56 -> 11.12 (Note 10, p.88). The flat rent line against an escalating lease is unexplained. [YELLOW, small]
- Auditor fee: statutory audit Rs 1.39 lakh (FY25 0.45), tax audit 0.11 (Note 28, p.92), for a Rs 70 Cr listed company. Low; observation only. [YELLOW]

## 2. RELATED PARTY TRANSACTIONS (Note 2.3, p.81-82; AOC-2, p.54)
Related parties named (Note 2.3 A and C, p.81): KMP Pradeep Kumar Verma (MD), Shalini Singh (WTD), CFOs Ranjan Kumar Samal (21-Jun-25 to 16-Jan-26) and Nitin Gupta (from 16-Jan-26), CS Tulsi Sharma (from 1-Aug-25). Enterprises: ABL Electricals (KMP significant influence; AOC-2 calls it a proprietorship of Pradeep Kumar Verma, and the PAN printed against ABL, AEKPV6479J, equals Mr Verma's own PAN, p.82) and Accord Global Infra Private Limited (no transaction disclosed).

Full transaction table, Rs lakh (Note 2.3 D, p.81-82):
| Party | Relationship | Nature | FY26 | FY25 | YoY (calc) |
|---|---|---|---|---|---|
| Pradeep Kumar Verma | MD, promoter | Remuneration | 32.00 | 18.00 | +77.8% |
| Pradeep Kumar Verma | MD | Repayment of unsecured loan | 4.50 | 100.90 | -95.5% |
| Shalini Singh | WTD, promoter | Remuneration | 32.00 | 18.00 | +77.8% |
| Shalini Singh | WTD | Repayment of unsecured loan | 7.50 | 2.30 | +226% |
| Nitin Gupta | CFO | Remuneration | 12.00 | NIL | new |
| Nitin Gupta | CFO | Expense reimbursement | 0.38 | NIL | new |
| Tulsi Sharma | CS | Remuneration | 1.51 | NIL | new |
| Neelam, D. C. Thakkar, A. N. Shukla | Independent directors | Sitting fees | 0.80, 0.80, 0.70 (total 2.30) | NIL | new |
| Antelp Corporation Pvt Ltd | "KMP relative has an interest" (AOC-2) | Sale of goods/services | 29.44 | NIL | new party |
| ABL Electricals | Proprietorship of MD | Acceptance of unsecured loan | 150.00 | 117.60 | +27.6% |
| ABL Electricals | | Repayment of unsecured loan | 80.36 | 146.47 | -45.1% |
| ABL Electricals | | Purchase of goods | 64.15 | 24.25 | +164.5% |
| ABL Electricals | | Sale of goods | NIL | 40.63 | -100% |

Outstanding balances, 31-Mar-26 vs 31-Mar-25 (Note 2.3 E, p.82), Rs lakh: P. K. Verma unsecured loan 54.42 / 58.92; S. Singh unsecured loan 58.71 / 66.21; ABL Electricals unsecured loan 69.64 / NIL; ABL creditors 67.59 / NIL; Antelp debtors 29.44 / NIL; director remuneration payable P. K. Verma 0.39 / 1.29, S. Singh 29.52 / 30.43; CFO 2.98; CS 0.22.

Reconciliations (calc): director loans 54.42 + 58.71 + ABL 69.64 = 182.77 vs Note 8 "From directors repayable on demand" 182.78 (p.87). Opening 58.92 + 66.21 = 125.13 = Note 8 prior year. Director remuneration payable 0.39 + 29.52 = 29.91 = Note 10 (p.88). Remuneration 32 + 32 = 64.00 = Note 24 (p.91). Sitting fees 2.30 = Note 28 (p.92). All tie.

Findings
1. Promoter-side funding: Rs 182.78 lakh (3.7% of net worth 4,886.85; 21.9% of short-term borrowings 836.24; calc) is repayable on demand, including Rs 69.64 lakh net owed to a proprietorship of the MD, who also supplies Rs 64.15 lakh of goods. Rs 150.00 lakh was accepted from ABL in FY26. Interest rate, terms and security on all director and ABL loans: NOT FOUND IN DOCUMENT. [YELLOW]
2. ABL is both lender and supplier: purchases rose 2.6x (24.25 -> 64.15). ABL creditors 67.59 exceed ABL purchases 64.15 by 3.44 (GST would explain part; inference). Prior-year sales to ABL 40.63 vanished. [YELLOW]
3. Remuneration: promoter pay rose 78% to Rs 64.00 lakh while PBT fell 24.1% (calc 605.75 vs 798.05). Remuneration is 10.6% of PBT (calc). Auditor reports Section 197 compliance (p.71, item 2(g)). Promoters hold 61.97% (Note 3). [YELLOW]
4. Antelp Corporation: sale Rs 29.44 lakh, entire amount outstanding at year end (debtors 29.44). Antelp is not listed in Note 2.3 C (only ABL and Accord Global Infra). AOC-2 calls it "KMP relative has an interest", while Note 2.3 B states "Relative of Individual Exercising Control Over the Company - NIL". Internal inconsistency. [YELLOW]
5. RPT as % of revenue (calc on 7,006.92): sales to related parties 29.44 = 0.42%; purchases from related parties 64.15 = 1.29% of purchases 4,966.72; remuneration 64.00 = 0.91%. Trade RPT is small. [GREEN on size]
6. AOC-2: Section 1 (not at arm's length) is blank; Section 2 lists only the Antelp sale and the ABL purchase at "prevailing market prices", Board approval date 21-06-2025 (p.54). The ABL loan flows are not shown there. Arm's-length support beyond that wording: NOT FOUND. [YELLOW]
7. Loans to promoters: none (CARO iii nil; Note 2.3 shows inflows only). [GREEN]
8. CFO and CS pay (12.00, 1.51) is part-year; the CFO changed in January 2026, about six weeks before listing (Note 2.3 A). Noted for stage 8. [YELLOW]
9. Struck-off company dealings: none (Note 2.11(d), p.84). [GREEN]

## 3. CONTINGENT LIABILITIES AND GUARANTEES (Note 2.5, p.83; Note 2.11(g), p.84)
| Nature | 31-Mar-26 | 31-Mar-25 | Stage / company view |
|---|---|---|---|
| (A) CST demand, FY2016-17, non-submission of C forms, Gurugram (West) | NIL | 2.23 | Demand deposited in FY26 "but action pending on Officer hand" |
| (B) Bank guarantees to customers (warranty period) | 532.46 | 205.99 | Normal course; margin money FDR 181.96 (FY25 118.68) |
- Total contingent liabilities 532.46 = 10.90% of net worth 4,886.85 (calc); a single item above 10% of net worth. Growth +158.5% against revenue -11.3% (calc). [YELLOW]
- BG as % of FY26 revenue: 7.6% (calc). Margin money covers 34.2% (calc 181.96 / 532.46). Bank limit utilisation: NOT FOUND.
- CST item: the note says the liability was "deposited in F.Y. 2025-26 but action pending", while the contingent figure is NIL and the P&L shows a GST demand charge of Rs 2.01 lakh (Note 28, p.92). Where the Rs 2.23 lakh deposit was booked: NOT FOUND. Minor. [GREEN]
- The auditor states "no impact of pending litigations" (p.70, 2(h)(i)) and no disputed statutory dues (CARO vii(b), p.73). [GREEN]
- Guarantees for subsidiaries: none (no subsidiaries). Customer-claim or LD contingencies: NOT FOUND. Detention and Late Delivery Charges expensed: Rs 81.77 lakh (FY25 81.99), 1.17% of revenue vs 1.04% (calc, Note 28, p.92). Not contingent; a delivery-performance signal. [YELLOW]
- Bills discounted: interest on bills discounting Rs 7.74 lakh (FY25 1.72, +350%, Note 25, p.91). Discounted bills outstanding and recourse: NOT FOUND in the contingent-liability note or elsewhere. If discounted bills carry recourse they are an undisclosed contingent liability. [YELLOW]

## 4. TRADE RECEIVABLES (Note 15, p.89)
Ageing from due date, Rs lakh (undisputed, considered good; no disputed items):
| Bucket | 31-Mar-26 | % (calc) | 31-Mar-25 | % (calc) |
|---|---|---|---|---|
| Not due | 1,029.32 | 68.6% | 2,454.22 | 86.1% |
| Under 6 months | 389.08 | 25.9% | 370.14 | 13.0% |
| 6 months to 1 year | 57.28 | 3.8% | 7.03 | 0.2% |
| 1 to 2 years | 23.73 | 1.6% | 7.80 | 0.3% |
| 2 to 3 years | 2.07 | 0.1% | 11.62 | 0.4% |
| Total | 1,501.48 | | 2,850.81 | |
The FY25 ageing table in the AR lists seven values under eight headings; the split above is confirmed by the Note 15 header totals (under-6-month 2,824.36 = 2,454.22 + 370.14).
- Over 6 months: 83.08 (5.53% of total) vs 26.45 (0.93%): up 214% while the total halved (calc). Over 1 year 25.80 vs 19.42 (calc). [YELLOW]
- Provision for doubtful debts: NIL both years; "considered doubtful" nil (Note 15). The over-6-month balance of 83.08 is unprovided, 13.7% of PBT (calc). [YELLOW]
- Single customer above 10% of receivables: NOT FOUND. Related-party receivable: Antelp 29.44 (Note 2.3 E), 2.0% of receivables (calc).
- Receivable days (calc): closing 78.2 days in FY26 vs 131.7 in FY25 (on revenue 7,006.92 and 7,902.25). Average-based turnover 3.22 vs 4.48 (Note 30, p.95), which is 113 vs 81 days. Three-year trend: FY24 NOT FOUND in the AR (the prospectus holds restated FY24; not read in this pass). Closing days fell, average days rose. Because the FY25 balance was very high, the fall is an unwind, not a structural cut. [YELLOW]
- Retention money (receivable-like): Note 18 holds 443.69 (FY25 401.36) and Note 17 holds 56.17 (FY25 1.16): total 499.86 vs 402.52 (calc), 7.1% of revenue. Release terms and ageing: NOT FOUND. [YELLOW]
- Unbilled receivables: nil (ageing column "Unbilled" blank, p.89). Customer advances 449.36 (Note 10) act as contract liabilities. [GREEN]

## 5. INVENTORY (Note 14, p.89; Notes 21 and 23, p.91)
| Category | 31-Mar-26 | 31-Mar-25 | YoY (calc) |
|---|---|---|---|
| Raw materials and components | 665.36 | 629.36 | +5.7% |
| Work in progress | 820.94 | 1,085.17 | -24.3% |
| Finished goods | 329.07 | 93.51 | +251.9% |
| Stock in transit | 619.50 | NIL | new |
| Total | 2,434.87 | 1,808.05 | +34.7% |
- Finished goods +252% against revenue -11.3%. This fits management's account of finished sets made for a deferred order (operator context; not in the notes). Stock in transit Rs 619.50 lakh is 25.4% of inventory (calc): a new head, undefined in the notes. [YELLOW]
- Reconciliation question. Note 23 shows FG +235.56 and WIP -264.23, net 28.67 decrease (calc), and ties to the Note 14 closing balances. Note 21 uses closing raw material 665.36, which equals the Note 14 RM line only. So the +619.50 stock in transit does not appear as a credit in Note 21 or Note 23. The balance-sheet inventory rise of 626.82 (cash flow p.79) is RM +36.00, WIP -264.23, FG +235.56, SIT +619.50 (calc, sums to 626.83). Two readings: (a) the stock in transit was paid for by an advance and never run through purchases (then it links to vendor advances 624.41); (b) it sits inside purchases 4,966.72 with no closing-stock credit, which would overstate material cost. The notes do not say which. Verifier question: which account holds the offset to Stock in Transit. [YELLOW, open reconciliation]
- Write-downs, obsolescence, NRV: NOT FOUND IN DOCUMENT. [YELLOW]
- Inventory days (calc): 145 (turnover 2.51, Note 30) vs 66 (5.51). On closing stock over RM consumed: 180 vs 97 (calc 1,808.05 / 6,836.42 x 365 = 96.5). Direction: sharply worse. Physical verification: no discrepancy of 10% or more (CARO ii(a), p.72). [YELLOW]
- Sales over closing inventory: 2.9x (calc 7,006.92 / 2,434.87).

## 6. INVESTMENTS
- No investments. Policy 1D: "There are no long-term investments in the company" (p.80). Note 2.6 refers to no provision for diminution in "Investments" being of long-term nature (p.83), though none exist; orphan text. No subsidiaries, JVs or associates (CARO ix(e)). [GREEN]
- Investment in FD Rs 766.90 lakh in investing flows (p.79) equals the rise in "Other Bank Balance" FDs (890.11 - 123.21 = 766.90, calc, Note 16). Not an investment in securities. [GREEN]
- ICDs and loans given: none (CARO iii nil). Unrealised gains or losses: none.

## 7. BORROWINGS (Notes 5 and 8, p.86-87; Cash Flow p.79)
| Instrument | 31-Mar-26 | 31-Mar-25 |
|---|---|---|
| LT: HDFC Bank term loan | 30.02 | 38.15 |
| LT: Mercedes-Benz Financial Services (vehicle loan) | 17.20 | 41.17 |
| LT total (Note 5) | 47.22 | 79.32 |
| ST: directors and ABL, repayable on demand | 182.78 | 125.13 |
| ST: HDFC inventory funding and cash credit | 621.37 | 1,516.86 |
| ST: current maturities, HDFC term loan | 8.13 | 6.85 |
| ST: current maturities, Mercedes-Benz | 23.97 | 21.94 |
| ST total (Note 8) | 836.24 | 1,670.79 |
| Total borrowings (calc) | 883.46 | 1,750.11 |
- Total borrowings halved (-49.5%, calc); the cash credit fell 895.49 (calc). Debt/equity 0.18 vs 0.55 (Note 30, p.95). DSCR 0.81 vs 0.75: below 1.0 in both years (Note 30). Management calls it "comfortable debt servicing capability" (p.65). [YELLOW]
- Interest rate, maturity, repayment schedule, security, covenants, covenant breaches or waivers, sanctioned limit amount, fixed vs floating: NOT FOUND IN DOCUMENT in any note. Five-year repayment schedule: NOT FOUND.
- Contradiction on current-asset security: Note 2.11(b) says "The company has no borrowings with banks and financial institution on the basis of Security of current assets, hence no quarterly statement is required to be field" (p.84). The auditor says the company was "sanctioned working capital limits in excess of Rs 5 crore" on security of current assets and compared the quarterly returns with the books, no material discrepancy (CARO ii(b), p.72). Note 8 shows "Inventory Funding & Cash Credit Facility from HDFC Bank" Rs 621.37 lakh. The note statement conflicts with Note 8 and with CARO. [RED for note reliability]
- Related-party borrowing: 182.78 as in section 2. [YELLOW]
- Interest expense: borrowings 37.30 + bills discounting 7.74 = 45.04 (Note 25, p.91); the cash flow uses 45.05; bank charges and other 9.99 complete the 55.04. An implied rate on average debt is not meaningful because the cash credit was repaid late in the year (inference).
- CARO ix: no default, no wilful default, short-term funds not used for long-term purposes (p.73). [GREEN]

## 8. TRADE PAYABLES (Note 9, p.87; MSME note p.88)
- Total 1,856.77 (FY25 1,511.40): MSME 1,494.94 (80.5%, calc; FY25 637.28, 42.2%); others 361.82 (874.12). All under 1 year; no disputed dues (Note 9 ageing). [YELLOW]
- Payable days (calc): closing 136 days on purchases 4,966.72 (FY25 81 days on 6,783.91). Turnover 3.40 vs 6.43 (Note 30); management reason "higher average credit period availed from suppliers" (p.64). [YELLOW]
- MSME disclosure: principal unpaid 1,494.94; interest due 1.40 (FY25 1.04). Interest on delayed payment booked 1.40 (Note 28; FY25 0.53) and payable 1.40 (Note 10). Section 16 interest paid: nil (clauses b to d dashes, p.88). The 45-day MSME limit cannot be tested against an average of 136 days without a due-date split. NOT FOUND: MSME dues beyond 45 days. [YELLOW]
- The prior-year MSME principal is printed as "63,727.76" under a rupee column header, against 637.28 lakh in Note 9. Unit mismatch (appears to be Rs thousand). [YELLOW, disclosure quality]
- Tax angle: payments to MSME suppliers beyond 45 days are deductible only when paid (Section 43B(h)). The notes show no disallowance or reconciliation. NOT FOUND. [YELLOW]

## 9. PROVISIONS AND EMPLOYEE BENEFITS (Notes 7, 11, p.86, 88; Note 28 AS-15, p.93-95)
- Gratuity: unfunded; obligation 36.04 (FY25 22.07) = Note 7 33.29 + Note 11 2.75 (ties). Expense 13.97 vs 4.72 (current service 7.97, interest 1.48, actuarial loss 4.52 vs gain 1.66). No benefits paid, no plan assets (Note 28, p.93-94). [GREEN on tie; unfunded]
- Assumptions: discount rate 7.00% (6.70%), salary escalation 8%, withdrawal 10%, IALM 2012-14, retirement age 60 (Note 28, p.93). Experience adjustment on plan liability loss 5.32 vs gain 2.36 (p.94). [GREEN]
- Leave encashment: obligation 15.06 (9.08) = Note 7 13.16 + Note 11 1.90 (ties); expense 7.49; paid 1.51 (p.94-95). [GREEN]
- Defined contribution: PF and ESIC 18.40 vs 11.23 (p.93). Statutory dues in arrears over 6 months: none (CARO vii(a), p.73). [GREEN]
- Employee cost: total 578.46 vs 361.86 (+59.9%); salaries and bonus 459.32 vs 293.13 (+56.7%) while revenue fell 11.3% (Note 24, p.91, calc). Employee cost 8.26% of revenue vs 4.58% (calc). Headcount: NOT FOUND in the notes. [YELLOW]
- Warranty, litigation, onerous-contract and decommissioning provisions: NOT FOUND IN DOCUMENT (see section 1). Provision for taxation net of advance tax: nil vs 99.93 (Note 11).
- CSR: required 7.70 and spent 7.70, nothing unspent (CARO xx, p.74; Note 27, p.92). [GREEN]

## 10. DEFERRED TAX AND TAX (Note 6 p.86; Note 2.1 p.81; P&L p.78)
- Deferred tax liability (net) 4.74 (3.25): arises only from depreciation timing; no deferred tax asset recognised on gratuity and leave provisions (36.04 + 15.06 = 51.10, allowable on payment). Note 6 layout is sign-confused ("Gross deferred tax assets (3.25)" used for a liability; an item "(1.49)" under deferred tax assets whose FY25 value 12.51 has the opposite sign). Note 2.1 shows FY25 movement 12.52 against 12.51 in the P&L. Net balances tie (4.74, 3.25). [YELLOW, presentation]
- Tax rate: total tax 155.33 on PBT 605.75 = 25.64% (calc); current tax 153.84 = 25.40%; FY25 25.52% (calc 203.68 / 798.05). Reconciliation to the statutory rate: NOT FOUND IN DOCUMENT. [YELLOW]
- Unrecognised DTA, MAT credit: none disclosed; NOT FOUND. Tax paid 253.77 (p.79) = FY25 provision 99.93 + FY26 current tax 153.84 (calc). [GREEN]
- Interest on delayed payment of income tax, TDS and TCS: Rs 4.40 lakh (FY25 7.71) (Note 28, p.92): repeats two years running. [YELLOW]

## 11. REVENUE DETAILS (Note 19 p.90; Note 2.4 p.83)
- Sale of goods 6,883.17 (7,778.97, -11.5%); sale of services 123.75 (123.28) (Note 19). Segment table (Note 2.4) matches: manufacturing 6,883.17; service 123.75.
- Segment oddities: "Segment Result" is 336.03 + 114.40 = 450.43, which is PAT, not segment operating profit. The service segment shows result 114.40 (FY25 228.29) on turnover 123.75 plus other income 26.76 (calc 123.75 + 26.76 = 150.51). Nature of service revenue: NOT FOUND. Segment assets are all in manufacturing (8,365.58); segment liabilities 3,473.98 vs balance-sheet liabilities 3,478.73 (gap 4.75, close to the deferred tax liability 4.74; calc). Segment capex 151.08 vs cash-flow purchase of PPE 146.19 (gap 4.89). [YELLOW]
- Disaggregation by product (distribution, power, inverter-duty transformers, switchgear), geography or customer: NOT FOUND IN DOCUMENT. Top customer share: NOT FOUND. Unsatisfied performance obligations: not in the notes (AS framework).
- Customer advances (contract liability) 449.36 vs 248.42, +80.9% (Note 10, calc). [GREEN]
- Other income 28.78 = 4.75% of PBT (calc): FD interest 11.25, warehouse charges 12.96 (new, FY25 nil), duty drawback 1.62, discount received 0.69, electricity deposit interest 0.24, sundry balances written back 2.02 (FY25 9.55) (Note 20, p.90). Warehouse charges: counterparty not named; if Antelp or ABL, it would be an RPT (not stated). [YELLOW, small]

## 12. OTHER CRITICAL NOTES
12.1 Exceptional items: none. Prior-period expense Rs 19.39 lakh in FY25 shown below total expenses (P&L p.78), nil in FY26. [GREEN]
12.2 Share capital (Note 3, p.85): authorised 2,30,00,000 shares (Rs 2,300 lakh), issued 2,05,73,289 (Rs 2,057.33 lakh). Movement: opening 2,94,339 + fresh 55,62,000 + bonus 1,47,16,950 = 2,05,73,289 (calc, ties). IPO: 55,62,000 shares at Rs 46 (Directors' report, AR p.55 text near the listing paragraph) = Rs 2,558.52 lakh = Note 4 premium 2,002.32 + capital 556.20 (calc). Promoters 63,75,000 each = 30.99% each, 61.97% together (calc 1,27,50,000 / 2,05,73,289). The 5% holders table prints the total "% Holding" as 84.94% for FY26, which is the FY25 percentage. The promoter table shows "0.00% change" on share count, although the holding fell from 84.94% to 61.97% through the IPO. [YELLOW, printing error]
12.3 Bonus: 1,47,16,950 shares (50 for 1 on 2,94,339) funded 940.41 from securities premium and 531.28 from the P&L surplus (Note 4, p.86; Rs 1,471.69 here vs 1,471.70 in Note 3, rounding). A bonus charged to surplus is a direct debit to reserves outside the P&L, and it is disclosed. [GREEN]
12.4 Reserves (Note 4): premium closing 1,726.12 = 940.41 + 2,002.32 - 276.20 - 940.41 (ties, calc). IPO issue expense charged to premium Rs 276.20 lakh, versus Rs 255.85 lakh allocated and utilised for issue expenses in the AR object-alteration table (AR Item 3, p.32-33). Excess 20.35 lakh (+8.0%, calc). [YELLOW]
12.5 EPS (Notes 2.2 and 29, p.81, 95): basic equals diluted at Rs 2.90 (FY25 4.27 post-bonus; 217.94 pre-bonus). Weighted average shares 1,55,29,393. EPS on year-end shares 2,05,73,289 would be Rs 2.19 (calc 450.43 / 205.73). Diluted = basic: no dilutive instruments at year end. ESOP: no ESOP note exists, which is consistent with no grant at the balance sheet date (the 2026 scheme was approved at the AGM of 26-Sep-2026; operator context). ESOP terms in the notes: NOT FOUND. [GREEN]
12.6 Foreign currency: unrealised FX loss 4.32 (FY25 0.86) in the cash flow (p.79) and Note 28; hedging, import share and exposure amounts: NOT FOUND IN DOCUMENT. The auditor says no derivative trading (p.70, 2(h)(ii)). [YELLOW, small]
12.7 Capital commitments: NOT FOUND IN DOCUMENT. Expansion plans (building Rs 700 lakh, machinery 602.67 lakh) post-date the balance sheet (AR p.32-33).
12.8 Events after the balance sheet date: NOT FOUND IN DOCUMENT as a note. Facts outside the notes: (a) the Board on 3-Sep-2026 proposed to move Rs 700.00 lakh of IPO money from machinery to building (AR Item 3, p.32-33); (b) the Directors' report and MD&A say the Company "during the year" acquired land at Khairthal (AR text near lines 1714 and 3021), yet PPE rose only Rs 64.15 lakh net (769.90 vs 705.75) and capex was 146.19 (Cash Flow p.79). The land is not booked at 31-Mar-26, and no capital-commitment or subsequent-event note covers a purchase the operator dates to a 3-Jul-2026 filing. [YELLOW]
12.9 IPO utilisation (outside the numbered notes: KAM 2 p.68-69; CARO x(a) p.73; AR Item 3 p.32-33): raised 2,558.52; utilised to 2-Sep-2026: working capital 931.59 (93.2% of its 1,000.00), issue expenses 255.85, machinery 0.00 (of 1,302.67); unutilised 1,371.08 (53.6%, calc) on 2-Sep-2026; unutilised at 31-Mar-2026 2,040.21 (79.7%, calc). The auditor's KAM wording is "considerably consistent" (p.69), a softened phrase. [YELLOW]
12.10 Key ratios (Note 30, p.95): current ratio 2.23 (1.41); D/E 0.18 (0.55); DSCR 0.81 (0.75); ROE 12.79% (42.93%); inventory turnover 2.51 (5.51); receivable turnover 3.22 (4.48); payable turnover 3.40 (6.43); net capital turnover 2.46 (9.21); net profit 6.43% (7.51%); ROCE shown as 0.13 (0.35). ROE reproduces (calc 450.43 / average equity 3,520.48 = 12.79%). The MD&A summary line gives PAT margin 6.40% (on total income) vs 6.43% (on revenue) in the table (p.64). [YELLOW, narrative vs table]
12.11 Audit report facts that colour the notes: unmodified opinion; two KAMs (revenue recognition; IPO fund utilisation) (p.67-69); CARO xix: no material uncertainty on meeting liabilities for one year, with a disclaimer of assurance (p.74); IFC opinion adequate and operating effectively (p.76); audit trail operated all year (p.71). No going-concern language in any note. [GREEN]
12.12 Other note-level observations (Note 28 p.92; Note 22 p.91): legal and professional 58.36 (24.12, +142%), tour and travelling 40.03 (19.40, +106%) and repairs and maintenance 43.99 (18.44, +139%) rose while revenue fell. Part of legal and professional may be IPO-linked; the note does not say. Jobwork 206.34 vs 111.17 (+86%); direct expenses 360.27 vs 236.60 (+52%); freight 111.00 vs 85.76. Brokerage and commission 11.27 vs 25.32 (-55%). ROC fees 3.11 vs 16.21. [YELLOW]
12.13 Cost lines versus revenue (calc): materials consumed 4,930.72 = 70.4% of revenue (FY25 86.5%). Because FY25 carried a WIP build of 797.77, the like-for-like measure is materials plus direct expenses plus change in inventories: FY26 4,930.72 + 360.27 + 28.67 = 5,319.66 (75.9% of revenue); FY25 6,836.42 + 236.60 - 797.77 = 6,275.25 (79.4%). Gross margin on this basis rose about 3.5 points. [GREEN]

---------------------------------------------------------------------

## PASS 1 SUMMARY: TOP 10 FINDINGS, ranked by investor importance
| # | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | Cash conversion is a one-year receivable unwind: CFO +869.50 vs PAT 450.43, but CFO ex-receivable release is (479.83); two-year CFO +51.40 vs two-year PAT 1,044.80. | Cash Flow p.79; Note 15 p.89 | RED |
| 2 | Short-term loans and advances 63.86 -> 890.45; 70% is vendor advances 624.41 with no vendor, ageing or related-party disclosure; CARO (iii) reports nil loans. Stock in transit 619.50 (new) sits beside it with no visible offset in Notes 21 or 23. | Note 17 p.90; Note 14 p.89; CARO iii p.72 | RED |
| 3 | Of cash Rs 2,232.80, Rs 2,040.21 is unspent IPO money (91.4%); free cash about 192.59. Machinery object unspent (0 of 1,302.67 by 2-Sep-26); Rs 700 lakh moved to building. | Note 16 p.90; CARO x(a) p.73; AR Item 3 p.32-33 | RED for a cash-rich reading; YELLOW otherwise |
| 4 | Note 2.11(b) says no borrowing on security of current assets, but Note 8 shows HDFC inventory funding and cash credit 621.37 and the auditor reports current-asset security with quarterly returns. Rate, maturity, covenants NOT FOUND. | Note 2.11(b) p.84; Note 8 p.87; CARO ii(b) p.72 | RED |
| 5 | Promoter-linked funding: Rs 182.78 lakh on-demand loans (incl. ABL Electricals, the MD's proprietorship, 150.00 raised in FY26) while ABL also sells Rs 64.15 lakh of goods to Accord; terms NOT FOUND; promoter pay +78% on PBT -24%. | Note 2.3 p.81-82; Note 8 p.87 | YELLOW |
| 6 | Inventory +34.7% on revenue -11.3%: FG +252%, stock in transit 619.50 new; turnover 5.51 -> 2.51 (145 days; 180 on the operator's basis); no write-down or NRV disclosure. | Note 14 p.89; Note 30 p.95 | YELLOW |
| 7 | Receivables over 6 months tripled to 83.08 (5.5%); no ECL or doubtful provision; retention money 499.86 (7.1% of revenue) with no ageing; bills-discounting interest +350% with discounted bills undisclosed. | Note 15 p.89; Notes 17, 18; Note 25 p.91 | YELLOW |
| 8 | MSME payables 1,494.94 (80.5% of payables, +135%) and payable days 136; 45-day compliance and Section 43B(h) effect not disclosed; prior-year MSME principal printed in the wrong unit. | Note 9 p.87; MSME note p.88 | YELLOW |
| 9 | Bank guarantees 532.46 (+158%) are 10.9% of net worth; no warranty provision exists despite BGs "to cover the warranty period". | Note 2.5 p.83; Notes 7, 11 | YELLOW |
| 10 | Management narrative contradicts the notes: "improvement in receivables turnover" vs ratio fall 4.48 -> 3.22; DSCR 0.81 called "comfortable"; promoter table prints 84.94% for FY26 (actual 61.97%); Note 12 missing and Note 28 numbered twice. | MD&A p.64-65; Note 3 p.85; Note 30 p.95 | YELLOW |

Pass 1 verdict on LBF-2: composition known (vendor advances 624.41, revenue authorities 194.64, retention 56.17, loans and advances 15.23); counterparty and purpose NOT FOUND IN DOCUMENT; no related-party record; CARO (iii) nil. Pass 1 verdict on LBF-4: CFO figure holds; quality is weak on repeatability; free cash is small once IPO money is separated.

## INPUT GAPS CARRIED FROM B00
rating ABSENT; shareholding ABSENT; results pp3-19 scan-only; listing-period announcements not staged; VOLTAMP no transcripts; one concall only. For the notes: AR Note 12 is missing from the text layer, and PDF page rendering was unavailable in this session. Verifier action: open PDF pages p.88-89 and confirm Note 12.
