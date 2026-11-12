> ERRATA (pass 1's own corrections from its hand-back, applied by the orchestrator, no new analysis): (1) "both auditors' KAMs" reads "the auditor's key audit matters". (2) The exchange fines in the Note 19 bullet (INR 2,12,400 NSE and INR 1,88,800 BSE) are in rupees, not lakhs. Pass 2 corrections to pass 1 are in 02-notes-pass2.md.

# STAGE 2, PASS 1 (CALL 1 of 3): NOTES TO FINANCIAL STATEMENTS, FULL EXTRACTION
Company: Walchandnagar Industries Ltd (WALCHANNAG) | Run date: 2026-11-12 | Run: runs/walchannag-2026-11-12
Source: inputs/annual-report/Annual_Report_2026.txt (FY2025-26 standalone, audited, approved 20 May 2026). Company has no subsidiaries, associates or JVs (CARO 3(ix)(e), PDF p.63), so standalone is the only statement.

UNIT AND ANCHOR CONVENTION
- Unit on the face of every note: INR Lakhs (the notes print "` in Lakhs"). Nothing converted here. Stage 10 converts once (100 Lakhs = 1 Cr). Per-share and EPS figures are in INR.
- Anchors read (Note N, PDF p.X). X is the [page N] marker of the .txt, which equals the PDF page. The printed page number in the PDF footer is X minus 3. Example: Note 21 is PDF p.108-110, printed p.105-107.
- Ratings: GREEN = clean, YELLOW = watch, RED = red flag. (Text labels used in place of colour symbols.)
- Verified on the PDF page: PDF p.121 (ECL matrix absent) and PDF p.125 (EPS denominators). The .txt matched the PDF on both.
- "Derived" marks a number I computed from anchored figures. The inputs are anchored beside it. It is arithmetic, not a filed figure.

INPUT GAPS CARRIED FORWARD FROM B00 (those that touch the notes)
1. Company files standalone only. No consolidated view exists. Every note below is standalone.
2. Shareholding filing absent (screener table capture only). The pledge percentage below comes from Note 21 of the AR (a filed source), so it can be compared with screener's 49.2%.
3. No concall transcripts (no-concall mode). Management explanations for the items flagged below cannot be checked against a call.
4. OCR text layer on results PDFs is unreliable. Not relevant to the AR text, which was clean on the two PDF pages I opened.
5. Screener export sheets empty. FY24 balances for a 3-year trend are therefore not in this pass (see receivables and inventory days).

LOAD-BEARING FACTS COVERED BY THE NOTES (first verification priority)
| B00 load-bearing item | What the notes show | Anchor |
|---|---|---|
| Borrowings and finance cost | Borrowings 21,891 (non-current 3,338 + current 18,552). Finance cost 3,845 vs 4,389 prior. 17.5% NCD with a pledge of promoter shares. | Balance sheet PDF p.67; Notes 21, 24, 35 |
| Warrant issue and share capital movements | One warrant issue only: 2,17,18,023 warrants at 114 each (247.59 Cr in the CG report), allotted 16 Nov 2023, fully converted by 24 May 2025. Closing warrant money 0. No FY27 or later warrant issue in the notes: NOT FOUND IN DOCUMENT. | Note 19 PDF p.98; Note 20 PDF p.100; CG report PDF p.45 (cross-reference) |
| Promoter pledge | Pledge of "15.63% of paid-up capital" secures the NCDs. Promoter holding 31.59%. Derived: 15.63/31.59 = 49.5% of promoter holding. Consistent with screener's 49.2%. | Note 21 PDF p.109; Note 19 PDF p.99 |
| Related parties | Table below. | Note 50 PDF p.125-130 |
| Contingent liabilities | Table below. | Note 54 PDF p.138-139 |
| Order-related contract assets and receivables | Unbilled revenue (contract assets) 12,050; trade receivables 15,351 net; advances from customers 10,675. Order book and unsatisfied performance obligations: NOT FOUND IN DOCUMENT in the notes. | Notes 9, 13, 16, 23, 28, 29 |
| CFO change Nov 2026 | Post-dates the AR. Note 50 shows CFO Nishant Saigal from 14.04.2025 and Sandeep Jain to 28.02.2025. Nov 2026 change: NOT FOUND IN DOCUMENT. | Note 50 PDF p.126 |
| Order book, guidance, Q2 FY27 EBITDA | Not in the notes (outside this pass). | n/a |

---------------------------------------------------------------------
## 1. ACCOUNTING POLICIES AND CHANGES (Notes 1, 2, 2.1 to 2.25; PDF p.73-85)
| Item | Finding | Anchor | Rating |
|---|---|---|---|
| Framework | Ind AS under Companies Act 2013. Policy text still cites "Ind AS 17 Leases" in the basis of preparation. | Note 2.2, PDF p.73 | YELLOW (stale text) |
| Revenue, products | Point in time on dispatch. Exports on bill of lading. "Income on items delivered directly by suppliers/sub-contractors to the client is recognized on dispatch and receipt of suppliers'/sub-contractors' invoices." Price variation recognised "on the acceptance of the claim by the client and on certainty of its realization". | Note 2.7 A(ii),(v),(vi), PDF p.76 | YELLOW (direct-delivery revenue; principal versus agent not discussed) |
| Revenue, contracts | Over time using the Input (cost) method. Escalation claims counted as variable consideration using the expected value method. If outcome cannot be estimated, revenue only to extent of recoverable cost. Expected loss booked at once. | Note 2.7 B, PDF p.76-77 | YELLOW (estimate-heavy; both auditors' KAMs are on this and on receivables, PDF p.57) |
| Liquidated damages | Revenue cut by LD where delivery is late. Where revenue is not yet booked, LD charged as expense. Impact: NIL FY26, 169.69 FY25 (Note 41). | Note 2.8, PDF p.77; Note 41, PDF p.119 | GREEN |
| Depreciation | Straight line on Schedule II lives, residual value 5%. "The company has taken technical report on balance useful life of assets. Accordingly, depreciation has been calculated based on such revised useful life." No quantified effect of the revision: NOT FOUND IN DOCUMENT. | Note 2.5-2.5 Depreciation, PDF p.75-76 | YELLOW |
| Software and know-how | Software 3 years. Technical know-how 6 years. | Note 2.5, PDF p.75 | GREEN |
| Capitalisation threshold | NOT FOUND IN DOCUMENT. | Note 2.5 | n/a |
| Borrowing cost | Capitalised only for qualifying assets. FY26 amount capitalised: NOT FOUND IN DOCUMENT. | Note 2.14, PDF p.82 | n/a |
| Impairment test | Policy text only (recoverable amount, pre-tax discount rate). No CGU test, no growth or discount rate, no sensitivity disclosed. Foundry segment lost money in both years (segment result -313 FY26, -872 FY25; segment assets 5,010). NOT FOUND IN DOCUMENT. | Note 2.6, PDF p.76; Note 53, PDF p.136 | YELLOW |
| ECL | Simplified approach, provision matrix "based on the receivables bifurcated based on the division". The text says "The provision matrix at the end of the reporting period is as follows" and the matrix is not printed (checked on the PDF page). Rates: NOT FOUND IN DOCUMENT. | Note 44 PDF p.121 | RED (conservatism cannot be tested) |
| Ind AS 116 | No ROU asset, no lease liability, no discount rate. Lease policy is written in Ind AS 17 terms (finance versus operating). Rent expense 14 FY26, 9 FY25 only. | Note 2.25 PDF p.85; Note 37 PDF p.117 | YELLOW (disclosure gap; amounts look immaterial) |
| First-time adoption | Labour Codes notified 21 Nov 2025 adopted in FY26. Incremental cost: gratuity 115, compensated absences 21 (total 136), shown under Exceptional Items. | Note 34 PDF p.116; Note 38 PDF p.118 | YELLOW (new; see exceptional items) |
| Operating cycle | Project-linked assets and liabilities classed current up to realisation of receivables including retention "within the agreed credit period". | Note 2.4, PDF p.75 | YELLOW (long cycle lets long-dated receivables sit in current assets; see section 4) |
| Inventory valuation | Lower of cost and NRV. FIFO for Heavy Engineering Division, weighted average elsewhere. WIP "amortized over the period of the contract on the basis of sales booked". | Note 2.9, PDF p.77 | GREEN |
| Grants | Industrial Promotion Subsidy sanctioned by Maharashtra, 549, recognised in Other Income, for investment made in FY2013-14 to FY2016-17. | Note 30 footnote, PDF p.115 | YELLOW (one-off, prior-period; see section 12) |
| Policy changes with quantified P&L effect | None stated other than Labour Codes (136) and the depreciation-life revision (not quantified). | Notes 2, 34 | n/a |

## 2. RELATED PARTY TRANSACTIONS (Note 50; PDF p.125-130)
Related parties named in the note (Note 50 i to iii, PDF p.125-126): Chairman Chakor L. Doshi, wife Champa, MD and CEO Chirag Doshi, daughter Kanika Sanger, Chirag's wife Tanaz; KMP Chirag Doshi, G. S. Agrawal (WTD and CS), CFO Nishant Saigal (from 14.04.2025), former CFO Sandeep Jain (to 28.02.2025); about 20 enterprises including Bombay Cycle & Motor Agency Ltd, Walchand Great Achievers Pvt Ltd, Walchand Kamdhenu Commercials Pvt Ltd, Walchand Chiranika Trading, Rodin Holdings Inc, Olsson Holdings Inc, Walchand Advanced Composites Pvt Ltd, Janta Travels Pvt Ltd, Trust Finlease Pvt Ltd and two Seth Hirachand Nemchand trusts.

| Party | Relationship | Nature | FY26 (INR Lakhs) | FY25 (INR Lakhs) | YoY |
|---|---|---|---|---|---|
| Chakor L. Doshi | Chairman | Receiving of services | 8 | 8 | 0% |
| Walchand Advanced Composites Pvt Ltd | Enterprise under significant influence | Receiving of services | 129 | 0 (not shown) | new |
| Bombay Cycle & Motor Agency Ltd | Enterprise (also the quoted investee, Note 8) | Receiving of services | 30 | 38 | -21% |
| Sub-total services | | | 167 | 45 | +271% (derived) |
| Janta Travels Pvt Ltd | Enterprise | Interest on unsecured loan | 128 | 41 | +212% (derived) |
| Seth Hirachand Nemchand Smarak Trust | Enterprise (trust) | Interest on unsecured loan | 3 | 16 | -81% (derived) |
| Sub-total interest | | | 131 | 57 | +130% (derived) |
| Reimbursement of expenses | various | | 0 | 0 | n/a |
| Chirag C. Doshi | MD and CEO | Managerial remuneration, short term | 128 | 127 | +1% |
| G. S. Agrawal | WTD and CS | Managerial remuneration | 58 | 61 | -5% |
| Nishant Saigal | CFO | Managerial remuneration | 55 | 0 | new |
| Sandeep Jain | Former CFO | Managerial remuneration | 0 | 92 | n/a |
| KMP total | | Short term benefits | 241 | 280 | -14% |
| Share-based payments to KMP (amortised cost) | | G. S. Agrawal 34 (FY25: 1), Nishant Saigal 13 (FY25: 0) | 47 | 2 | large |
| Unsecured loan received in the year | | all parties | 0 | 0 | n/a |

Outstanding balances at year end (Note 50, PDF p.129-130):
| Balance | FY26 | FY25 |
|---|---|---|
| Payable to Bombay Cycle & Motor Agency Ltd (services) | 44 | 26 |
| Unsecured loan, Janta Travels | 931 | 903 |
| Unsecured loan, Seth Hirachand Nemchand Digambar Jain Dharmshala & Arogya Bhuvan Trust | 400 | 400 |
| Unsecured loan, Seth Hirachand Nemchand Smarak Trust | 650 | 650 |
| Unsecured loans total (Note 50) | 1,981 | 1,953 |
| Managerial remuneration payable | 60 | 87 |
| Advances receivable, Walchand Advanced Composites Pvt Ltd | 48 | 0 |

Derived ratios (revenue 27,519, PDF p.68):
- Services from related enterprises plus chairman 167 = 0.61% of revenue. Interest to related enterprises 131 = 0.48%. Both together 298 = 1.08% of revenue. Including KMP pay 241: 539 = 1.96%.
- Related party loans 1,981 = 9.0% of total borrowings 21,891.

Findings:
- RED: the Note 50 loan table shows 1,981 of related-party unsecured loans, but the borrowings notes carry only 931 from a related party (Note 21 "From related party **", Janta Travels, PDF p.108). The Dharmshala trust 400 and Smarak trust 650 (1,050 together) do not appear in Note 21 or Note 24, and total borrowings in Note 51 (21,891) equal Note 21 plus Note 24 exactly (3,338 + 18,552 = 21,890). Where the 1,050 sits is NOT FOUND IN DOCUMENT. One candidate is the 600 "Equity Component-Unsecured Loan" in Other Equity (Note 20, PDF p.100), which the note does not link to these loans. I do not assert the link.
- YELLOW: Janta Travels interest 128 against an average loan of about 917 (903 to 931) is 14% on the average. Finance cost note shows "Notional interest on unsecured loans from related parties" of only 28 (Note 35, PDF p.117), and the carrying amount of the loan rose by 28 (903 to 931). So the 128 of interest in Note 50 is not visible as a P&L line or a payable (no accrued interest to Janta in the payables table). Reconciliation: NOT FOUND IN DOCUMENT.
- YELLOW: Janta Travels loan term was extended by three years (original due 30 Mar 2025, new 29 Mar 2028). A gain of 96.61 was booked in finance cost in FY25 on that modification (Note 21 item 2, PDF p.109-110). This is a modification gain with no cash. The FY25 notional interest line was -59.
- YELLOW: new related party in services, Walchand Advanced Composites Pvt Ltd: 129 of services plus a 48 advance receivable, both nil the year before. Nature of services and pricing basis: NOT FOUND IN DOCUMENT. Note 50 asserts "in the ordinary course of business". No arm's length statement.
- YELLOW: Promoter shares are pledged to secure the NCD. This is a promoter-linked security, not a loan to promoters (Note 21, PDF p.109). Pledge detail in the related party note: NOT FOUND IN DOCUMENT.
- GREEN: no loans to promoter entities. Note 56 shows nil loans to subsidiaries, associates and firms where directors are interested (PDF p.139). Note 60(9): no Section 186 loans, investments or guarantees given (PDF p.140). No royalty, rent or fee to promoter family other than the services above.
- GREEN: CG report states no material related party transactions in FY26 (PDF p.45, cross-reference).
- Other cross-reference: SEBI Adjudicating Officer order of 2015 on promoter entities, penalties 21.25 lakh, pending (CG report PDF p.45). Not a note item. B00 freshness pair already FAIL on the order text.

## 3. CONTINGENT LIABILITIES AND COMMITMENTS (Note 54; PDF p.138-139)
Net worth: 35,879 (balance sheet PDF p.67).
| # | Nature | Amount (INR Lakhs) | Stage | Company view | Paid under protest |
|---|---|---|---|---|---|
| (i) | NA tax, Tahsildar Indapur | 74.76 (PY 74.76) | sub-judice | Liability not accepted; no provision | 20 |
| (ii) | Annual Rateable Value, Pune property, FY2008-12 | 99.02 plus interest/penalty (PY 99.02) | Mumbai High Court | Not accepted; no provision | not stated |
| (iii) | Central Sales Tax FY2013-14 | 367.14 (PY 367.14) | Sales Tax Appellate Tribunal, Pune | Disputed | 204.78 |
| (iv) | Customs, Chennai | 64.50 (PY 64.50) | Madras High Court | "does not expect any liability" per legal opinion | 53.75 |
| (v) | Service Tax, Mar 2013 to Dec 2015: demand 667.33 plus equal penalty 667.33 | 1,334.66 (PY same) | CESTAT Mumbai | Disputed | 50.05 |
| (vi) | Hyderabad Commercial Tax, refund of 2011 clawed back | 313.66 (PY 313.66) | High Court, stay granted | Disputed | not stated |
| (vii) | EPF office demand | 50.68 (PY 50.68) | Mumbai High Court | No provision, legal advice | not stated |
| (viii) | TN Commercial Tax FY2018-19 | 68.99 | Appellate Authority, Chennai (appeal admitted) | Disputed | 10% pre-deposit |
| (ix) | TN Commercial Tax FY2019-20 | 36.70 | same | Disputed | 10% pre-deposit |
| (x) | TN Commercial Tax FY2020-21 | 2.57 | same | Disputed | 10% pre-deposit |
| (xi) | TN Commercial Tax FY2019-20 (second) | 6.96 | same | Disputed | 10% pre-deposit |
| (xii) | Ex-employee compensation claims, labour courts | unascertained | pending | not stated | n/a |
| | Total of quantified claims (derived) | 2,419.64 | | | at least 328.58 stated (derived: 20 + 204.78 + 53.75 + 50.05) |

Other commitments and guarantees (PDF p.139):
| Item | FY26 | FY25 |
|---|---|---|
| Counter guarantees by the company for bank guarantees issued by banks | 18,235 | 21,625 |
| Open LCs, acceptance pending | 1,301 | 4,050 |
| Capital commitments not provided for (net of advance) | 478 | 2,396 |

Derived ratios:
- Quantified claims 2,419.64 = 6.7% of net worth. No income tax demand appears (accumulated losses).
- Largest single item: service tax plus penalty 1,334.66 = 3.7% of net worth. No single item exceeds 10% of net worth.
- Bank guarantee counter-guarantees 18,235 = 50.8% of net worth and 66.3% of FY26 revenue. They fell 15.7% (derived: 21,625 to 18,235).
- Guarantees are covered in part by margin money and escrow deposits: "Balances held as Margin Money/Security towards obtaining Bank Guarantees" 5,020 (Note 15, PDF p.95) = 27.5% of 18,235 (derived). Bank guarantee charges in finance cost: 531 (FY25: 719), 2.9% of 18,235 (derived).
- The company says it "has adequately provided for where provisions are required" (Note 54 closing para, PDF p.139). The only large specific provision is the TNEB provision (section 9).
- No guarantees for subsidiaries (no subsidiaries).
Ratings: tax and duty disputes GREEN (6.7% of net worth, mostly old, partly pre-deposited). Bank guarantees YELLOW (size relative to net worth is the dependency on bank limits; see section 7). Service tax item YELLOW (penalty equals demand, ruling not yet out). Unquantified labour claims YELLOW (amounts unascertained).

## 4. TRADE RECEIVABLES (Notes 9, 13, 16, 44; PDF p.92-96, 121)
Carrying amounts (INR Lakhs):
| Item | 31 Mar 2026 | 31 Mar 2025 |
|---|---|---|
| Non-current trade receivables, gross | 10,644 | 11,922 |
| less allowance, credit impaired | (3,913) | (3,903) |
| Non-current, net | 6,731 | 8,019 |
| Current trade receivables, gross | 9,453 | 7,920 |
| less allowance | (832) | (925) |
| Current, net | 8,621 | 6,995 |
| Total net | 15,351 (Note 18 break-up, PDF p.97) | 15,014 |
| Total allowance | 4,746 (Note 44) | 4,829 (opening FY26) |
| Unbilled revenue (contract assets), current | 12,050 (Note 16) | 11,424 |
| Related party receivables | nil | nil |

Ageing, combined non-current plus current, gross before allowance (derived by adding the two Note 9 and Note 13 schedules, PDF p.92-95):
| Bucket | FY26 | FY25 |
|---|---|---|
| Less than 6 months | 7,556 (1,805 + 5,751) | 4,969 (1,395 + 3,574) |
| 6 months to 1 year | 293 (52 + 241) | 394 (28 + 366) |
| 1 to 2 years | 423 (338 + 85) | 1,060 (778 + 282) |
| 2 to 3 years | 524 (475 + 49) | 76 (52 + 24) |
| More than 3 years | 11,300 (7,973 + 3,327) | 13,344 (9,670 + 3,674) |
| Total gross | 20,096 | 19,843 |
Percentages (derived): over 6 months 62.4% of gross (FY25: 75.0%). Over 3 years 56.2% (FY25: 67.3%). Allowance 4,746 covers 42.0% of the over-3-year gross (FY25: 36.2%).
Disputed and credit-impaired lines: undisputed credit impaired 881 (FY25: 802), disputed credit impaired 1,367 (both years), all non-current and all over 2 years (Note 9, PDF p.92-93). Allowance of non-current 3,913 exceeds the labelled credit-impaired 2,248 (881 + 1,367) by 1,665 (derived), so the allowance covers some balances labelled "considered good".

Receivable days (derived, on revenue; FY24 balance NOT FOUND in this AR, so only two points, not three):
- Net trade receivables 15,351 / 27,519 x 365 = 204 days (FY25: 15,014 / 25,918 x 365 = 211 days).
- Net receivables plus unbilled revenue: 27,401 / 27,519 x 365 = 363 days (FY25: 26,438 / 25,918 x 365 = 372 days).
- The company's own ratio (Note 40, PDF p.119): receivables turnover 1.81 (FY25 1.60), which is about 202 days (FY25: 228 days, derived).

Findings:
- RED: over half of gross receivables (11,300 of 20,096) are older than 3 years and are carried at 58% net. The "current" schedule alone holds 3,327 over 3 years, shown as undisputed good. The headline receivable days of 204 mask that only 7,556 of 20,096 (37.6%) is under 6 months.
- RED: the Note 13 summary lists 832 as "Credit Impaired" while the Note 13 ageing shows nothing in the credit-impaired rows (PDF p.94-95). The allowance of 832 is therefore a general allowance on balances classed as undisputed good. The matrix that sets it is not disclosed (section 1).
- YELLOW: improvement is real but partly mechanical. Over-3-year gross fell by 2,044 (13,344 to 11,300) while the allowance fell only 83. FY26 other expenses show an ECL write-back (83) and no bad-debt write-off, against bad debts written off 1,323 and write-back (667) in FY25 (Note 37, PDF p.118). The fall in old balances is therefore mostly collection, set-off or reclassification, not write-off. The note does not say which. NOT FOUND IN DOCUMENT.
- YELLOW: Note 44 says "no single customer contributes to more than 10% of outstanding accounts receivable and unbilled revenue" (PDF p.121). Revenue by customer is not disclosed in Note 53 (no major-customer line under Ind AS 108). NOT FOUND IN DOCUMENT.
- YELLOW: receivables, payables and loan balances are "subject to confirmation by concerned parties" (Note 59, PDF p.140).
- Auditors list receivable recoverability as a key audit matter (15,351 = 17.42% of total assets, PDF p.57, cross-reference).
- Unbilled revenue 12,050 (13.7% of total assets 88,142, derived): no ageing, no separate ECL, no retention split. The ECL policy says lifetime ECL covers "all contract assets" (Note 44). NOT FOUND IN DOCUMENT for contract-asset ageing.

## 5. INVENTORY (Note 12 and Note 33; PDF p.94, 116)
| Category | FY26 | FY25 | Change |
|---|---|---|---|
| Goods in transit, at cost | 2,154 | 45 | +2,109 (derived) |
| Raw materials and components | 4,240 | 3,775 | +12.3% |
| Stores and spares | 990 | 1,018 | -2.8% |
| Dies, jigs, tools, moulds | 605 | 618 | -2.1% |
| Work in progress | 4,709 | 5,895 | -20.1% |
| Finished products | 1,074 | 1,014 | +5.9% |
| Total | 13,772 | 12,364 | +11.4% |
Derived: total excluding goods in transit 11,618 against 12,319, down 5.7%. Finished goods +5.9% against revenue +6.2% (27,519 vs 25,918): in line.
Days (derived): on revenue 183 days (FY25: 174). Company ratio (Note 40): inventory turnover 1.09 (FY25 1.22), about 335 days (FY25: 299 days).
- Write-downs with amounts: NOT FOUND IN DOCUMENT. Obsolescence provision: NOT FOUND IN DOCUMENT.
- YELLOW: goods in transit rose from 45 to 2,154. Letter of credit borrowings rose from 1,528 to 3,853 (Note 24) and EUR forward contracts of EUR 28,34,584 (INR 3,089.03 Lakhs) are outstanding for payables (Note 54(e), PDF p.139). The note does not say what the goods are, nor who the customer is. [Derived link, not stated by the company.]
- GREEN: WIP fell 1,186 while the Note 33 change in inventories of FG and WIP shows a 1,126 decrease charged to cost (PDF p.116). The two tie (opening 6,909, closing 5,783). The Note 33 column headings print "March 31, 2025 / March 31, 2024" instead of FY26 / FY25, but the values match the FY26 and FY25 balances.

## 6. INVESTMENTS (Note 8, PDF p.91; Note 56, PDF p.139; Note 55, PDF p.139)
- No subsidiaries, associates or JVs (CARO 3(ix)(e), PDF p.63).
- Non-current investments total 20 (FY25: 19): Bombay Cycle & Motor Agency Ltd, 1,200 shares of 10, quoted, fair value 20 (FY25: 19), at FVOCI. A related party (Note 50 iii).
- Actis Biologics Pvt Ltd: 1,04,250 shares, cost 103, fully impaired (103). Carrying nil. GREEN (already written off).
- Co-operative society shares: each rounds to 0.
- Loans and ICDs given: none (Note 56; Note 60(9)). Other loans and advances 100 in current assets is the Aicitta settlement receivable (Note 17 footnote refers to Note 38(2)).
- Aicitta Intelligent Technology Pvt Ltd: Board approved up to 1,600 for about 60.3% fully diluted in March 2025. Not consummated. Petition filed in High Court May 2025. Settled: Aicitta pays 100 in five instalments of 20, April to August 2026 (Note 55, PDF p.139; Note 38(2), PDF p.118). Rating GREEN (no capital out), YELLOW for the strategy signal: the diversification attempt failed.
- Investment property: land, carrying 153 (both years), fair value 3,157 (unchanged), valuer D. K. Nagarseth & Associates. Rental income nil in the table (Note 6, PDF p.89-90). Road widening Dalaj to Walchandnagar enters the land; suit 444/2025 filed; High Court writ contemplated; no adjustment to carrying value. YELLOW (title dispute with authorities; value realisable is 20 times the carrying amount only if the land is saleable).
- Assets held for sale: 2,648 (FY25: 2,488): Bhigwan land 33, Dharwad land and building 2,455, Mumbai flat 160 (Note 18, PDF p.96-97). Held beyond 12 months for Bhigwan and Dharwad. Company received advances from buyers. YELLOW (see section 12).

## 7. BORROWINGS (Notes 21, 24, 35, 43, 44; PDF p.108-111, 117, 120-123)
Instrument table (INR Lakhs):
| Instrument | FY26 | FY25 | Rate | Maturity | Security |
|---|---|---|---|---|---|
| 17.5% NCDs, non-current | 2,407 | 4,241 | 17.50% | repayable to 30 Jun 2028 | see below |
| NCDs, current maturity | 1,900 | 338 | 17.50% | within 12 months | same |
| Unsecured, related party (Janta Travels) | 931 | 903 | rate NOT FOUND IN DOCUMENT | 29 Mar 2028 (extended from 30 Mar 2025) | none |
| Working capital loan, banks | 12,799 | 12,340 | 12.00% Bank of India, 11.70% SBI | renewable, date NOT FOUND IN DOCUMENT | charge on HED current assets, plant, flat in Airoli, Walchandnagar land and buildings, Pune offices; second charge on assets given to the NCD lender |
| Letters of credit, banks | 3,853 | 1,528 | rate NOT FOUND IN DOCUMENT | NOT FOUND IN DOCUMENT | same |
| Total borrowings | 21,891 | 19,350 | | | Note 51, PDF p.131 |
Non-current 3,338 and current 18,552 (balance sheet PDF p.67). Current borrowings are 84.7% of the total (derived: 18,552 / 21,891).

NCD detail (Note 21, PDF p.108-109): 740 NCDs of 10,00,000 face (7,400 Lakhs), issued FY25, lender Neo Special Credit Opportunities Fund. Purpose: refinance ACRE debt (2,092 as at 30 Jun 2024) and working capital. Security: (1) first charge on specified non-factory land and buildings at Walchandnagar, Mumbai flats and Dharwad land and building; (2) first charge by pledge of promoter and affiliate shares of 15.63% of paid-up capital; (3) first charge on a designated SBI account and an HDFC escrow account.
Repayment schedule, all NCDs (Lakhs, Note 21 PDF p.109): 30 Jun 2026 400; 30 Sep 2026, 31 Dec 2026, 31 Mar 2027 500 each; 30 Jun 2027 to 30 Jun 2028 500 each; total 4,400. Repaid in Dec 2025: 338. The 4,400 less an EIR adjustment of 93 and 4,400 (1,900 + 2,407 = 4,307) ties to the balance sheet (derived).
Five-year schedule (derived from the table, by fiscal year): FY27 1,900 (400 + 500 + 500 + 500); FY28 2,000; FY29 500; FY30 and after nil. Janta Travels 931 due 29 Mar 2028 (FY28). Bank facilities have no stated repayment schedule.

Finance cost (Note 35, PDF p.117): total 3,845 (FY25: 4,389), down 12.4%.
| Component | FY26 | FY25 |
|---|---|---|
| Interest on debentures and fixed loans | 979 | 1,129 |
| Interest on short term loans and cash credits | 1,628 | 2,228 |
| Notional interest, related party loans | 28 | -59 |
| Bank guarantee charges | 531 | 719 |
| Others | 679 | 372 |
| Total | 3,845 | 4,389 |
Interest paid in cash 3,669 (cash flow statement, PDF p.70). Interest payable 89 (FY25: 6) (Note 26).
Derived: finance cost over average borrowings (21,891 + 19,350) / 2 = 20,620.5 is 18.6%. Interest cover: operating profit 2,446 (segment note, PDF p.136) over finance cost 3,845 is 0.64x. "Others" rose 82% (372 to 679); its content is NOT FOUND IN DOCUMENT. A further 99 sits as "Interest (Others)" in other expenses (FY25: 0) (Note 37, PDF p.118).

Covenants: "There have been no breaches in the financial covenants of any interest-bearing loans" (Note 43, PDF p.120). Covenant terms and ratios are NOT FOUND IN DOCUMENT. "The Company continues to comply with the terms and conditions of the debenture trust deed" (Note 21). CARO 3(ix)(a): no default in repayment or interest (PDF p.63). Quarterly statements to banks agree with books (Note 24 item 5, PDF p.111).
Term changes: the NCD was part-prepaid in FY25; classified as a modification, loss 30.70 in FY25 finance cost. Janta Travels loan extended three years, gain 96.61 in FY25. The present value test for each was "less than 10%".
Fixed versus floating: sensitivity of 1% = 166.52 (FY25: 138.68) implies floating-rate borrowings of 16,652 (= bank 12,799 + 3,853 LC, ties exactly; derived) (Note 44, PDF p.121). The NCD at 17.5% and the Janta loan are not in that base.
Related party borrowings: see section 2.

Findings:
- RED: cost of capital. NCD at 17.5% fixed with promoter share pledge, bank lines at 11.70% to 12.00%, all-in finance cost 18.6% of average borrowings (derived).
- RED: 84.7% of debt is current and the cash 2,009 included warrant money still unspent. The CG report states 13.29 Cr (1,329 Lakhs) of warrant proceeds unutilised at 31 Mar 2026 (PDF p.45, cross-reference), and Note 14 says the unutilised warrant money sits in a short term deposit counted as cash equivalent (PDF p.95). Cash less that amount is about 680 (derived) against 1,900 of NCD instalments due in the next 12 months.
- YELLOW: current borrowings rose by 4,346 (14,206 to 18,552) while the NCD balance fell. Short-term net borrowing 2,785 in the cash flow (PDF p.70).
- YELLOW: Note 44 liquidity table (PDF p.123) shows borrowings of 19,483.60 (1 to 12 months 18,552.31; 1 to 5 years 931.29). The balance sheet total is 21,891, so the 2,407 non-current NCD is missing from the table (FY25: 15,109 versus 19,350, missing 4,241). Trade payables, other financial liabilities and guarantees are also absent.
- GREEN: Pledge is disclosed. Pledge covers 15.63% of paid-up capital, which is 49.5% of the 31.59% promoter holding (derived).

## 8. TRADE PAYABLES (Notes 25 and 57; PDF p.111-112, 139)
| Item | FY26 | FY25 |
|---|---|---|
| MSME principal outstanding | 1,858 | 1,224 |
| Others | 4,857 | 5,126 |
| Total | 6,715 | 6,350 |
Ageing (FY26): MSME less than 1 year 1,509, 1-2 years 111, 2-3 years 238. Others less than 1 year 2,502, 1-2 years 1,400, 2-3 years 197, over 3 years 758. Total less than 1 year 4,010, 1-2 years 1,511, 2-3 years 435, over 3 years 758. FY25: less than 1 year 3,756, 1-2 years 804, 2-3 years 218, over 3 years 1,572. No disputed dues.
Derived: amounts older than 1 year are 2,704 (40.3% of payables) against 2,594 (40.9%) in FY25. The over-3-year bucket halved (1,572 to 758) while "Sundry balances written back" in other income rose from 464 to 708 (Note 30, PDF p.115). [INFERENCE: old creditor balances are being written back to income; the notes do not say so.]
MSME: interest due and unpaid 221 (FY25: 202). "Interest paid" nil, "payments made beyond the appointed date" nil (Note 57, PDF p.139). The ageing does not separate dues over the 45-day limit. NOT FOUND IN DOCUMENT. [INFERENCE: the deferred tax note carries an asset of 468 (FY25: 282) for "Unpaid SME creditors disallowed u/s 43B(h)" (Note 45, PDF p.124). At 25.168% that tax effect corresponds to about 1,860 of disallowed dues, which is the whole MSME principal of 1,858. This suggests nearly all MSME dues were beyond the statutory payment period. It is arithmetic, not a company statement.]
Payable days (derived): on cost of materials plus sub-contracting (11,495 + 1,661 = 13,156) 6,715 / 13,156 x 365 = 186 days (FY25: 6,350 / 14,955 x 365 = 155 days). Company ratio: payables turnover 1.83 both years (Note 40), about 199 days.
Ratings: YELLOW (MSME interest 221 unpaid and not provided in the P&L as a visible line; stretch of suppliers).

## 9. PROVISIONS (Notes 22, 26, 27, 52; PDF p.110, 112, 131-135)
- Provision for expected contract losses, TNEB projects: one-time provision 5,431 in FY25 (4,362 expected contract losses plus 1,069 procurement and erection expenses). Used in FY26: 1,545. Balance 3,886 at 31 Mar 2026. It sits inside "Other financial liabilities - Others" 5,853 (FY25: 6,896) (Note 26, PDF p.112). The balance of that line, 1,967 (derived: 5,853 - 3,886), is not described. Completion timetable for the TNEB projects: NOT FOUND IN DOCUMENT. Management says it is "confident that the proposed provision will be adequate". The note itself says the delays arose from "various issues with the Customer" and are "resolved to a certain extent". RED (a customer-driven, still-open loss contract of material size; the second KAM on revenue concerns estimated cost to complete, PDF p.57).
- Warranty provision: NOT FOUND IN DOCUMENT. Decommissioning: none. Onerous contract: the TNEB item above.
- Employee benefits (Note 52; PDF p.131-135):
  - Gratuity (funded): defined benefit obligation 2,090 (FY25: 1,385), plan assets 99 (FY25: 46), net liability 1,991 (FY25: 1,339). Funded ratio is 4.7% (derived: 99 / 2,090), so "funded" is nominal. Employer contribution 185. Past service cost 115 from Labour Codes. Actuarial loss 557 on the obligation, of which experience loss 695 and financial assumption gain 138.
  - Compensated absences (non-funded): obligation 282 (FY25: 209). Past service cost 21. Actuarial gain 59.
  - Assumptions: discount rate 7.43% (FY25: 6.67%), salary escalation 3.50% (both years), IALM 2012-14 mortality. Salary escalation of 3.50% is low against a rising wage bill; the discount rate rose 76 bp, which cut the liability by 138.
  - Sensitivity: 1% discount rate up gives 1,929, down gives 2,276 (base 2,090). Salary escalation 1% up gives 2,273, down 1,927.
  - Weighted average duration: the heading is present and the value is blank. NOT FOUND IN DOCUMENT.
  - Net remeasurement loss in OCI: (500) (balance sheet statement PDF p.68). Balance in other equity for remeasurement fell from 737 to 237.
  - Table error: the funded status line for compensated absences prints "282 (209)" with a sign slip (Note 52, PDF p.133). Minor.
  - Gratuity expense 291 (FY25: 237), up 23% from the Labour Codes charge.
  YELLOW (obligation up 51% in a year, plan nearly unfunded, experience loss 695 points to higher wages or tenure than assumed).
- Litigation provisions and the cases behind them: no specific litigation provision. All contingent items sit in Note 54. GREEN to YELLOW.
- Other provision: "Provision against supplier advances" 220 (new in FY26); advances to suppliers credit impaired 406 (FY25: 186) (Note 17, PDF p.96; Note 37, PDF p.118). YELLOW (advances to suppliers 2,148 net remain; the 406 impaired has doubled).

## 10. DEFERRED TAX (Note 45; PDF p.123-124)
- Tax expense nil both years. Reconciliation: loss before tax (1,468) x 25.168% = (370), offset by "effect of unrecognized deferred tax assets" 370 (FY25: (2,165) and 2,165). Effective rate nil against a statutory rate of 25.168%.
- Deferred tax assets recognised only to the extent of the deferred tax liability: DTA 3,005 equals DTL (3,005), net nil (FY25: 3,099).
- Gross timing-difference table: employee benefits 572, unpaid SME creditors 468, provisions 1,296, provision for expected contract losses 979 (FY25: 1,367), unabsorbed losses 2,495, unabsorbed depreciation 2,638, PPE (3,005). Net 5,443 (FY25: 5,300). So the unrecognised deferred tax asset is 5,443 (derived: gross DTAs 8,448 less DTL 3,005).
- Derived: unabsorbed losses of 2,495 and unabsorbed depreciation of 2,638 at 25.168% imply taxable losses of about 9,914 and about 10,482 (this is arithmetic only). Expiry schedule of losses: NOT FOUND IN DOCUMENT. MAT credit: none disclosed.
- GREEN on conservatism: no DTA is booked beyond the DTL. YELLOW on reconciliation: the movement shown in profit and loss in the timing table is 143 (FY26) and 1,464 (FY25), against the unrecognised effect in the rate reconciliation of 370 and 2,165. The tables use different bases and the difference is not explained. The TNEB provision line fell by 388, which equals 1,545 x 25.168% (derived, ties).
- Future tax shield: at 25.168%, tax losses and depreciation give a shield that protects future profit from cash tax. This is an asset not on the balance sheet.

## 11. REVENUE DETAILS (Note 29 and Note 53; PDF p.113-115, 136-137)
Revenue from operations 27,519 (FY25: 25,918), up 6.2%. Sales of products 26,368; services 859; other operating 292.
By segment (Note 29 and Note 53):
| Segment | FY26 | FY25 | Share FY26 (derived) |
|---|---|---|---|
| Heavy Engineering (goods 22,764; service 783; other 254) | 23,801 | 19,911 | 86.5% |
| Foundry and Machine Shop (goods 1,342; other 25) | 1,367 (Note 53: 1,366 net of inter-segment 0) | 3,663 | 5.0% |
| Others (goods 2,262; service 76; other 13) | 2,351 | 2,344 | 8.5% |
Heavy Engineering rose 19.5% (derived: 23,801 / 19,911). Foundry fell 62.7% (derived) because of the suspension from 20 Mar 2025, the lockout from 12 Apr 2025 and the restart on 17 Nov 2025 (Note 58, PDF p.140).
By geography, Note 29 (PDF p.114): India 21,582 (FY25: 24,945); outside India 5,936 (FY25: 973). Note 53 secondary segments (PDF p.137): domestic 21,739 (FY25: 24,992), export 5,780 (FY25: 925). Note 46 export of goods on FOB: 5,564 (FY25: 933). Three different export figures. Export share of revenue 21.6% in Note 29 (derived: 5,936 / 27,519).
Timing (PDF p.114): point in time 26,893 (FY25: 23,919); over time 626 (FY25: 1,999).
Contract balances:
- Contract assets (unbilled revenue) 12,050 (FY25: 11,424) (Note 16).
- Contract liability: nil (FY25: 170) (Note 26, PDF p.112).
- Advances from customers: non-current 2,642 (FY25: 4,622) (Note 23); current 8,033 (FY25: 6,680) (Note 28). Total 10,675 (FY25: 11,302). The current 8,033 includes 3,175 (FY25: 2,724) for partial sale of land in Maharashtra (Note 28 footnote, PDF p.113).
- Unsatisfied performance obligations and order book: NOT FOUND IN DOCUMENT.
- Top customer revenue: NOT FOUND IN DOCUMENT.
Segment result (Note 53, PDF p.136): Heavy Engineering 2,584 (FY25: -6,067); Foundry -313 (FY25: -872); Others 528 (FY25: 578). Segment total 2,800 (FY25: -6,361); after unallowable expense 354, operating profit 2,446 (FY25: -6,684). Heavy Engineering margin on revenue 10.9% (derived). The FY25 Heavy Engineering loss includes the 5,431 TNEB provision.
Sector row note for B00: the AR notes split revenue into Heavy Engineering, Foundry and Machine Shop, and Others. The notes do not split Heavy Engineering into nuclear, defence, aerospace, sugar or gearbox lines. The defence and nuclear share: NOT FOUND IN DOCUMENT in the notes.
Findings:
- RED: the segment note discloses revenue concentration in one segment (86.5%) but not by product line or customer.
- YELLOW: over-time revenue is only 626 (2.3% of revenue) but contract assets are 12,050, which is 19 times that figure (derived). The notes do not reconcile the two.
- YELLOW: export revenue differs across three notes (5,936, 5,780 and FOB 5,564), and the domestic figure differs across two (21,582 and 21,739).

## 12. OTHER CRITICAL NOTES
Exceptional items (Note 38, PDF p.118; P&L PDF p.68):
- FY26 exceptional is a net charge of 69 (profit before tax before exceptional items (1,399); after (1,468)). Components: Labour Codes statutory impact 136 (gratuity 115 + compensated absences 21) and an Aicitta settlement gain of 68 (receivable 100 net of expenses). 136 - 68 = 68, shown as 69 (rounding).
- FY25 exceptional 412 appears as a gain (profit before tax (9,015) becomes (8,603)). Its nature is NOT FOUND IN DOCUMENT in the FY26 notes.
- The P&L prints "Exceptional Items" 69 and 412 on one line with one sign convention for a loss in FY26 and a gain in FY25. The segment note prints "(69)" and "412" (PDF p.136). The cash flow statement subtracts 69 in FY26 (PDF p.69). Flag for Pass 3.
- Recurrence: FY25 and FY26 both carry an exceptional line. Labour Codes is stated as non-recurring.
Other income 2,107 (FY25: 3,566) (Note 30, PDF p.115): interest 608; sundry balances written back 708 (FY25: 464); FX gain 390 (FY25: 105); profit on sale of assets 93; miscellaneous 292; rent 9. FY25 included profit on sale of held-for-sale assets 1,802 and on investment property 253. The footnote says an industrial promotion subsidy of 549 for FY2013-14 to FY2016-17 investments was recognised in other income, but no line carries it and the lines already add to 2,107. Which line holds the 549: NOT FOUND IN DOCUMENT. YELLOW (derived: other income is 7.7% of revenue; of 2,107, items that are one-off or non-operating are sundry write-backs 708, subsidy 549 if inside, FX 390, asset sale 93).
Derived operating view: profit before tax and exceptional (1,399) + finance cost 3,845 + depreciation 1,103 = 3,549; less other income 2,107 = 1,442 (this is operating EBITDA excluding other income, FY26; derived, not a filed figure).
Goodwill: none. Intangibles: net 42 (IP rights 21, software 22) plus intangibles in progress 2 (embossed canister assembly technology transfer) (Notes 5 and 7, PDF p.89-90). Remaining life of IP rights is short (amortisation 11 a year on net 21). GREEN.
PPE (Note 3, PDF p.86): gross 45,057, accumulated depreciation 18,821, net 26,238 (FY25: 24,269). Land 8,380 is 31.9% of net PPE (derived). Plant additions 3,193; plant disposals 2,259 gross at an accumulated depreciation of 2,163. Capital work in progress 1,711 (FY25: 811), of which Gear Hobbing Machine 1,622; no project suspended; no ageing over 2 years (Note 4, PDF p.87). Capital advances 968 (FY25: 2,167) (Note 11). CWIP completion schedule FY25 sums to 811 on all lines and FY26 sums to 1,711. GREEN.
Capital commitments: 478 (FY25: 2,396) (Note 54(d)).
Foreign currency (Notes 44, 46 to 48, 54(e); PDF p.122-123, 125-126, 139):
- Hedged: EUR forward contracts payables EUR 28,34,584 = INR 3,089.03 Lakhs; FY25 nil. Note 44 prints "28.35" in the rupee column.
- Unhedged, USD financial assets 6,050 (FY25: 5,172), EUR 2,232 (3,129), others 102 (137). Unhedged liabilities USD 2,853 (3,793), EUR 647 (74), others 182 (109). The note has no unit label for this table; the 2% sensitivities (USD 64, EUR 32) tie to INR Lakhs (derived).
- Note 54(e) says "Unhedged Exposure: EUR Nil" while Note 44 shows EUR unhedged assets of 2,232. Contradiction. "Above foreign currency exposures is not hedged" also contradicts the forward contract in the same note.
- Foreign exchange gain 390 (FY25: 105) in other income; unrealised gain 472 in the cash flow statement.
- Earnings in foreign currency (FOB exports) 5,564 (FY25: 933); imports CIF 2,419 (FY25: 1,645), of which capital goods 1,864 (FY25: nil).
Segment reporting: covered in section 11. Segment assets 87,969 and segment liabilities 49,992 (Note 53). Heavy Engineering carries 78,908 of segment assets (89.7%).
EPS (Note 49, PDF p.125; verified on the PDF page): basic and diluted EPS (2.17) for FY26, (14.73) for FY25. The note shows weighted average shares of 5,83,88,207 for both years, dilutive shares 60,71,388 for both years and a diluted count of 6,44,59,595 for both years. The FY26 figure (2.17) does not come from these counts: 1,468 Lakhs / 5,83,88,207 = 2.51 and 1,468 Lakhs / 6,44,59,595 = 2.28 (derived). 2.17 implies about 6.76 crore shares, close to the actual 6,74,59,595 opening and 6,78,42,060 closing shares (Note 19). The FY26 denominator looks like a copy of FY25 text. FY25's (14.73) ties to 5,83,88,207. For a loss-making company, dilutive shares are anti-dilutive and are excluded, so basic equals diluted. RED on disclosure, low on value.
Dilution sources:
- Share capital moved 6,74,59,595 to 6,78,42,060: +3,82,465 shares = 58,784 ESOP exercised plus 3,23,681 warrants converted (Note 19, PDF p.98).
- Warrants: all 2,17,18,023 allotted on 16 Nov 2023 at 114; 93,93,862 converted 19 Mar 2024; 1,20,00,480 on 1 Jan 2025; 3,23,681 on 24 May 2025. Outstanding warrants at 31 Mar 2026: nil. Share warrant application money closed at nil (Note 20, PDF p.100). The last conversion on 24 May 2025 fell after the 18-month warrant life from 16 Nov 2023, and the CG report says NSE (212,400) and BSE (188,800) fined the company for the delay under ICDR Regulation 162 (PDF p.45, cross-reference). 31.59 Cr of the 247.59 Cr was set against promoter loans converted (CG report PDF p.45).
- ESOP 2020 (Note 20, PDF p.101-108): scheme size 10,00,000 options, exercise price 2 (face value), maximum term 7 years, five tranches. Outstanding at 31 Mar 2026: tranche 2 1,04,076; tranche 3 1,61,812; tranche 4 1,20,000; tranche 5 1,12,500; tranche 1 nil. Total outstanding 3,98,388 = 0.59% of shares (derived). ESOP expense 307 (FY25: 113), of which tranche 5 125, tranche 4 94, tranche 3 66, tranche 2 26, tranche 1 1. Grant-date prices 189.89 to 233.20. Options are granted at par: dilution is the full share count. Tranche headings in the note disagree with their own tables (tranche 3 heading "2,47,500" granted, movement table 1,78,470; tranche 2 heading "2,18,390"; tranche 5 heading "2,47,500", movement 1,12,500). YELLOW on presentation.
- Promoters hold 2,14,30,945 shares, 31.59% (FY25: 31.77%). No change in share count in the year. The percentage fell only through dilution (Note 19, PDF p.99). 5% holders: Walchand Kamdhenu Commercials 14.48%, Walchand Great Achievers 8.52%. No bonus, buy-back or non-cash allotment in the last five years.
Direct debits and credits to reserves: remeasurement of defined benefit (500) in OCI; FVOCI equity +1; ESOP reserve +307 less 51 on exercise; warrant issue expenses deducted from retained earnings 111 in FY25, nil in FY26 (Note 20, PDF p.100; statement of changes PDF p.71-72). Securities premium +363 from warrants and +51 from ESOP. Equity component of unsecured loan 600, unchanged. GREEN.
Events after the balance sheet date: Aicitta settlement (instalments from April to August 2026) is the only one (Note 55). No subsequent warrant issue, CFO change or order win appears in the notes: NOT FOUND IN DOCUMENT.
CSR: company "does not meet the applicability threshold" (Note 60(8), PDF p.140). Required CSR: nil. GREEN.
Assets held for sale (Note 18, PDF p.96-97): 2,648 (FY25: 2,488). No impairment on reclassification. Bhigwan (33) and Dharwad (2,455) are past their 12-month window; "unforeseen market conditions" is the reason; buyer advances received. Advances from customers for land total 3,175 (Note 28), which exceeds the carrying 2,648 of the held-for-sale pool (derived; the Note 28 land is described as "partial Land situated at Maharashtra" and Dharwad is in Karnataka, so the two are not the same pool). YELLOW: the sale has not closed for over a year despite advances, and Ind AS 105's 12-month test is relied on through an exception clause.
Ratios (Note 40, PDF p.119): current ratio 1.13 (FY25: 1.22); debt-equity 0.61 (0.52); DSCR 1.16 (0.03); ROE (0.04) ((0.23)); inventory turnover 1.09 (1.22); receivables turnover 1.81 (1.60); payables turnover 1.83 (1.83); net working capital turnover 3.98 (2.66); net profit ratio (0.05) ((0.33)); ROCE 0.04 ((0.08)). The reasons given for a variance over 25% are brief. DSCR variance is printed as "-3733%".
Capital management (Note 43): total capital 35,878 (balance sheet 35,879).
Other statutory (Note 60-61): audit trail enabled throughout; no benami, no struck-off company dealings, no wilful default, no Section 186 activity. GREEN.
Cash flow statement cross-check (PDF p.69-70, cross-reference): cash from operations (1,320); net operating cash flow (1,108) (FY25: 1,562); investing (1,403); financing (975); cash fell 3,487 to 2,009. Capex 2,511. Proceeds from equity and warrants 247 (FY25: 9,010). Cash flow is negative in the operating line in FY26 with a PBT loss of 1,468.

---------------------------------------------------------------------
## PASS 1 SUMMARY: TOP 10 FINDINGS BY INVESTOR IMPORTANCE
| Rank | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | Debt structure and cost: borrowings 21,891 (84.7% current), 17.5% NCD secured on a pledge of 15.63% of paid-up capital (49.5% of promoter holding, derived), all-in finance cost 18.6% of average debt (derived), interest cover 0.64x (derived). NCD instalments of 1,900 fall in FY27 and cash net of unspent warrant money is about 680 (derived). | Notes 21, 24, 35, 14; CG report PDF p.45 | RED |
| 2 | Receivable quality: 56.2% of gross receivables (11,300 of 20,096) are older than 3 years; only 37.6% are under 6 months. Allowance 4,746 covers 42.0% of the over-3-year balance. The ECL provision matrix is not printed. Unbilled revenue adds 12,050 with no ageing. | Notes 9, 13, 16, 44 | RED |
| 3 | TNEB loss contract: provision 5,431 booked in FY25, 3,886 left after 1,545 used. Customer-driven delays "resolved to a certain extent". Completion timetable not given. | Note 26 | RED |
| 4 | Related party loans: Note 50 shows 1,981 of unsecured related party loans, Notes 21 and 24 carry 931. The 1,050 owed to two trusts has no stated home. Janta Travels interest 128 is not visible in Note 35 (notional interest 28). | Notes 50, 21, 35 | RED |
| 5 | Earnings quality: FY26 loss before tax (1,468). Other income 2,107 includes sundry write-backs 708, a 549 prior-period subsidy and FX gain 390. Derived operating EBITDA before other income 1,442. FY25 exceptional 412 gain unexplained. | Notes 30, 38 | YELLOW |
| 6 | Revenue concentration and disclosure: Heavy Engineering is 86.5% of revenue. Order book, unsatisfied obligations, top customer, defence and nuclear share are NOT FOUND IN DOCUMENT in the notes. Export revenue differs across three notes (5,936, 5,780, 5,564). Over-time revenue is only 626 against contract assets of 12,050. | Notes 29, 46, 53 | YELLOW |
| 7 | Warrant and share capital: the single 247.59 Cr warrant issue is fully converted (last on 24 May 2025, with an exchange fine for late allotment). Warrant money closed at nil. Shares 6,78,42,060. ESOP outstanding 3,98,388 (0.59%). No later warrant issue in the notes. EPS denominators are stale (2.17 does not tie to the disclosed share counts). | Notes 19, 20, 49 | YELLOW |
| 8 | Employee obligations: gratuity obligation 2,090 (+51%), plan assets 99 (4.7% funded), experience loss 695, salary escalation 3.50%. Labour Codes added 136 and was taken to exceptional items. | Notes 34, 38, 52 | YELLOW |
| 9 | Liquidity disclosure and guarantees: bank guarantees 18,235 (50.8% of net worth), margin money 5,020 (27.5% cover, derived), Note 44's liquidity table omits the 2,407 non-current NCD. Open LCs 1,301. | Notes 15, 44, 54 | YELLOW |
| 10 | Contingent liabilities: 12 items, 2,419.64 quantified (6.7% of net worth), none above 10%, 328.58 paid under protest. Land at Dalaj road under dispute (suit 444/2025). Held-for-sale land of 2,648 unsold beyond 12 months. | Notes 6, 18, 54 | GREEN to YELLOW |

Going concern language in the notes: NONE found in Notes 1 to 62. The grep found going-concern text only in the auditor's responsibility paragraphs (PDF p.58) and the Board report (PDF p.28), outside the notes. Note 43 states no covenant breach.

Counts: 62 notes read, Note 1 to Note 62 plus 2.1 to 2.25 and the five-year statistical sheet (PDF p.142-146). Notes with an item I could not fill: impairment test, ECL matrix, Ind AS 116, warranty, inventory write-downs, WAD of DBO, unbilled ageing, order book. Each is marked NOT FOUND IN DOCUMENT above.
