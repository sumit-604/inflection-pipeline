# STAGE 2 NOTES, PASS 1 OF 3: Kwick Forensic Solutions Ltd (KWICK), run 2026-10-04

## Source and scope
- Document: final Prospectus dated 31-Aug-2026 (AR substitute). File `inputs\prospectus\KWICK-Prospectus-2026-08-31.txt`. Cited pages are PDF pages. (Prospectus 31-Aug-2026, pp.221-270.)
- UNIT: every figure below is **Rs lakh** exactly as printed ("Rs. In Lakhs", p.226). No conversion made. Stage 10 converts once. Ratios and percentages marked "computed" are my arithmetic on printed figures.
- Basis: **Indian GAAP (AS), not Ind AS** (Annexure IV, p.229). Standalone, no subsidiaries. No ECL matrix, no Ind AS 116, no fair value hierarchy exist. Where the template asks for them: NOT FOUND IN DOCUMENT.
- Auditor: A B C D & Co LLP (FRN 016415S/S000188), report 25-May-2026 (p.225). FY24 audited by previous auditor Ghewarchand Rathan Kumar, report 05-Sep-2024 (p.222). Reason for auditor change: NOT FOUND IN DOCUMENT in Section V.
- Not available: statutory FY26 AR, directors' report, CARO. Checks that need CARO (PF dues, statutory dues delays, related-party Sec.188 compliance, loans to related parties) are NOT CHECKABLE. Stated where relevant.
- Tied out: Annexure I totals (6,053.09 = 6,053.09, p.226); equity 1,687.48 + 2,453.19 = 4,140.67 (p.226, p.233); cash flow arithmetic for FY26 and FY25 foots (p.228). 🟢

## FIRST VERIFICATION PRIORITIES (LBF-1 to LBF-4), checked before the note sweep

### LBF-1: who are the non-government customers (Rs 4,733.92 lakh FY26)
- **NOT FOUND IN DOCUMENT in the restated notes.** No customer is named in Section V. Top 10 customers are anonymous ("Top Customer 1..10", Rs 8,207.23 lakh, 77.64%; p.160-161, also p.23-24 Risk Factor 2). Top 1 customer Rs 2,493.65 lakh = 23.59% (p.24). The government split of top-10 is NOT FOUND.
- Government Rs 5,837.36 / non-government Rs 4,733.92 lakh FY26; non-government Rs 1,371.18 FY25, Rs 393.03 FY24 (Risk Factor 10, p.29). 🟡
- Computed: FY26 revenue rose Rs 4,068.59 lakh (10,571.28 less 6,502.69, p.227). Non-government supplied Rs 3,362.74 lakh of it (82.7%); government Rs 705.85 lakh (17.3%).
- **Related-party test: no sales to, and no trade receivable from, any related party are disclosed.** Annexure VIII (pp.250-251) lists purchases, remuneration, rent, interest, loans and payables only. The p.57-59 summary of RPT is identical to Annexure VIII. 🟢 on the face; completeness cannot be proven because customers are unnamed.
- Seven group entities, per profile (pp.212-219): Extreme Covet (real estate/e-commerce), Gostocks Fintech (education/training software), Gee Gee Hire Purchase (construction/real estate, run by Duseja family), The Style Salad (e-commerce, partner Saloni Shammer Shah), Shah Infotech, Shah Electronics, Shah Trading Co. (electronics/UPS/transformer trading). None is described as a buyer of forensic products. Group revenue scale: largest is Shah Trading at Rs 579.53 lakh FY25 (p.219).
- B2B vs B2C split: B2B Rs 9,463.21 lakh (89.52%) FY26 vs Rs 4,781.90 FY25; B2C Rs 1,108.08 (10.48%) vs Rs 1,720.79 (p.160). Definition of "B2C": NOT FOUND IN DOCUMENT. B2B (9,463.21) exceeds government (5,837.36) by 3,625.85, so B2B includes non-government buyers (computed). The note does not say whether these are system integrators reselling to government, private labs or others. Disclosure gap, not proof of a problem. 🟡
- Management claim that private customers pay 30-50% advance on delivery (p.92) is not visible in the balance sheet: Advance from customers is only Rs 22.18 lakh (Note I.7, p.234). See finding on unearned revenue below. 🟡

### LBF-2: debtor days basis and receivables ageing
- Prospectus debtor days 83 / 89 / 74 (FY24/25/26) (p.92-93). These equal 365 / Trade Receivable Turnover in Annexure V (4.39 / 4.10 / 4.95, p.245). Formula: 365 / (Net Revenue / **average** trade receivables) (p.245). The FY26 figure uses average of 2,288.07 and 1,979.05 net of provision (computed: 10,571.28 / 2,133.56 = 4.955).
- **Year-end basis (computed, net receivables / revenue x 365):** FY24 1,193.58 / 3,018.33 = 144.3 days; FY25 1,979.05 / 6,502.69 = 111.1; FY26 2,288.07 / 10,571.28 = 79.0 (balance sheet p.226, revenue p.227). So the year-end basis is higher in every year, but it also falls: 144 > 111 > 79. The FY26 improvement is real on both bases. 🟢 on direction. The 83 (FY24) opening is on a sparse average; FY23 receivables are implied at 180.79 (1,193.58 less 1,012.79 change, p.228), computed, not printed.
- FY25 Q4 share of annual sales was 51% (p.92). FY26 Q4 share: NOT FOUND IN DOCUMENT. Year-end receivables are therefore sensitive to Q4 billing timing. 🟡
- Ageing (Note I.14, p.235), gross Rs lakh:

| Bucket | FY26 | FY25 | FY24 |
|---|---|---|---|
| <6 months | 2,045.06 | 1,669.30 | 1,046.53 |
| 6-12 months | 109.36 | 194.47 | 109.03 |
| 1-2 years | 30.12 | 135.30 | 33.12 |
| 2-3 years | 130.54 | 6.66 | 0.95 |
| >3 years | 4.94 | 4.66 | 3.95 |
| Gross | 2,320.02 | 2,010.39 | 1,193.58 |
| Provision | (31.94) | (31.34) | nil |
| Net | 2,288.07 | 1,979.05 | 1,193.58 |

- Computed shares of gross: >6 months 274.96 = 11.85% FY26 (FY25 341.09 = 16.97%; FY24 147.05 = 12.32%). >1 year 165.60 = 7.14% FY26 (FY25 146.62 = 7.29%; FY24 34.02 = 2.85%).
- **Stuck balance.** The 1-2 year bucket of FY25 (135.30) became the 2-3 year bucket of FY26 (130.54): only 4.76 lakh collected in a year. Provision on it is Rs 27.00 lakh (20.7%). In FY25 the 2-3 year bucket (6.66) was provided 100% and the 1-2 year bucket (135.30) was provided 20.02 (14.8%). Provision rates are not applied on a stated rule. Unprovided portion of the 2-3 year bucket: Rs 103.54 lakh (computed) = 5.7% of FY26 PBT of 1,821.45. 🟡
- Roll-forward anomaly: FY25 1-2 year bucket (135.30) is larger than the FY24 6-12 month bucket that could have aged into it (109.03), by 26.27 (computed). Buckets should not grow without a new invoice aged that way. Basis of ageing (invoice date or due date): NOT FOUND IN DOCUMENT. 🟡
- Provision policy / ECL: NOT FOUND IN DOCUMENT (accounting policies pp.229-231 contain no doubtful-debt rule). P&L provision charge: FY26 0.60, FY25 31.34, FY24 nil; bad debts written off 0.17 / 0.22 / 1.34 (Note II.8, p.240). 🟡
- Disputed receivables: nil all years. Receivables from related parties: none disclosed (p.251). Single customer >10% of receivables: NOT FOUND IN DOCUMENT. Government vs private split of receivables: NOT FOUND IN DOCUMENT.

### LBF-3: CFO vs PAT (Annexure III, p.228)

| Rs lakh | FY26 | FY25 | FY24 |
|---|---|---|---|
| PBT | 1,821.45 | 1,121.12 | 378.64 |
| Op profit before WC | 1,910.41 | 1,242.34 | 541.57 |
| Trade payables | (172.01) | 717.33 | 149.83 |
| Other current liabilities | 338.60 | 80.21 | 68.92 |
| Inventories | (287.08) | (427.90) | (9.40) |
| Trade receivables | (309.02) | (785.47) | (1,012.79) |
| Other current assets | (394.15) | (234.93) | 21.64 |
| Other non-current assets | (42.71) | (28.60) | 41.53 |
| Cash from operations | 1,044.04 | 562.98 | (198.70) |
| Income tax paid | 281.74 | 97.90 | 61.87 |
| **CFO** | **762.30** | **465.09** | **(260.57)** |
| PAT (p.227) | 1,350.77 | 855.94 | 283.47 |
| EBITDA (p.248) | 1,906.49 | 1,224.89 | 544.51 |

- Computed: CFO/PAT 56.4% FY26, 54.3% FY25, negative FY24. CFO/EBITDA 40.0% FY26, 38.0% FY25. Three-year CFO 966.82 vs three-year PAT 2,490.18 (38.8%) and EBITDA 3,675.89 (26.3%). Three-year receivable build 2,107.28 = 84.6% of three-year PAT.
- **Tax timing flatters CFO.** Current tax accrued FY26 470.02 (p.241) but cash tax paid 281.74. Paid equals the FY25 provision (279.80 plus 1.93 earlier-year tax, pp.227, 235). The whole FY26 charge of 470.02 sits unpaid as "Provision for current tax" (Note I.8, p.235). Computed: tax accrued less paid = 188.28. Taxes are being paid in arrears. Interest u/s 234A/B/C shown nil for FY25 and FY26 (Annexure IX, p.252); whether advance tax was paid in-year: NOT FOUND IN DOCUMENT. 🟡
- CFO also carries IPO costs: IPO expenses in other current assets rose 10.00 to 41.52 (Note I.16, p.236). Other current assets' rise of 394.15 also includes balances with government authorities up 234.45 (218.60 to 453.05); split between GST credit and advance tax: NOT FOUND IN DOCUMENT. 🟡
- Payables drove FY25 CFO (+717.33) and reversed in FY26 (-172.01): MSME payables 587.50 to 402.30 (p.234). The FY25 CFO was flattered by supplier credit.
- Free cash flow (computed): CFO 762.30 less PPE 206.59 less software CWIP 75.47 = 480.24 FY26.
- Tie-out: MD&A narrative of FY26 financing (p.268, "proceeds from short-term borrowings of Rs 325.61 lakh, repayment of long-term borrowings of Rs 8.69 lakh") contradicts Annexure III (p.228): short-term borrowings were **repaid** (325.61) and long-term repayment is nil in FY26 (8.69 was FY25). Narrative error. 🟡
- Note IV disclosure only: the 1-year cash conversion is still below 60% after the FY26 receivables improvement. Pass 3 to size.

### LBF-4: related-party and group-entity exposure
- Related parties (Annexure VIII, pp.250-251): MD Shammer Saralal Shah; Sejal Shammer Shah (promoter, director); Ashok Hinduja (COO, shareholder, promoter-holder per p.232); Sangeetha Hinduja; Punita Shah; CFO, CS, WTD (new FY26); two independent additional directors; seven group entities listed above.
- **Remuneration (all RPT, ties to Note II.5 "Managerial Remuneration" 281.35, p.239):** Shah 126.72, Sejal Shah 8.40, Hinduja 77.83, Jhaveri 49.15 (includes pre-appointment salary, p.251), Vishal Jain 17.55, Krithika 1.70. FY25 185.60, FY24 44.40. Promoter-family cluster (Shah + Sejal Shah + Hinduja) 213.0 lakh FY26 (computed) = 11.7% of PBT. Managerial remuneration +51.6% vs PBT +62.5% (computed). 🟡
- **Purchases from related parties** FY26 67.00 (Style Salad 1.56, Shah Infotech 35.68, Shah Electronics 17.83, Shah Trading 11.93); FY25 53.43; FY24 0.42 (computed from p.250). 0.90% of Note II.3 purchases of 7,446.06 FY26 (p.239). Arm's-length evidence: NOT FOUND IN DOCUMENT. Risk Factor 32 claims arm's length without evidence (p.50ff text twin line 2908). 🟡
- **Software purchased from Gostocks Fintech** (education software firm): asset purchases 20.00 FY26, 58.70 FY25; programming fees 3.00 / 0.25 / 6.50; payable 2.16 / 27.47 (p.250-251). Software CWIP is 137.17 lakh at FY26 and 61.70 at FY25, not amortised yet (p.237). Which vendors built the remaining CWIP (FY26 addition 75.47 vs RPT 20.00): NOT FOUND IN DOCUMENT. Capitalised software the company has no product for is hard to test. Purpose of the software: NOT FOUND IN DOCUMENT in Section V. 🟡
- **Promoter funding of working capital, now repaid.** MD borrowed 560.15 / 587.69 / 101.89 and repaid 689.00 / 480.20 / 246.18 (FY24 / FY25 / FY26); Sejal Shah and Extreme Covet also churned (p.250). Interest paid to related parties: FY24 96.17, FY25 20.38, FY26 2.04 (computed from p.250). Loan rate: NOT FOUND IN DOCUMENT. Year-end related party loans: nil FY26 (p.251). Zero debt at FY26 end (Capitalisation, p.254). 🟢 for FY26 position; 🟡 on history.
- **Rent to MD:** 7.88 FY26, 15.00 FY25, nil FY24 (p.250). Total rent expense 25.19 (p.240); MD's share 31.3% (computed). Property and lease terms: NOT FOUND IN DOCUMENT. 🟡
- **Personal guarantees and collateral** for IOB facilities (CC Rs 200 lakh, LG Rs 800 lakh): property owned by Sejal Shah and Shammer Shah, personal guarantees from Shammer Shah, Sejal Shah, Bina Shah and Saloni Shah (Note I.5 text, p.234). Bina Shah and Saloni Shah are **not** in the related-party list. Saloni Shammer Shah is a 50% partner of related party The Style Salad (p.216). No guarantee fee is disclosed. 🟡
- Ashok Hinduja holds 7.69% as promoter at 31-Mar-2024 (p.233) but his FY24 line says "Not a related party" and he became KMP w.e.f. 01-Aug-2024 (p.250). Pattern for Pass 3. 🟡
- Group entities and sales/purchases: p.219 text says transactions are "as mentioned in Annexure-XXVIII"; no such annexure exists, Annexure VIII is the RPT annexure. Cross-reference error, not substance. 🟢/🟡
- Sitting fees 1.24 FY26 (p.240, p.250) match.
- Section 185/186 loans and Sec.188 compliance: NOT CHECKABLE without directors' report/CARO. Annexure V (ii) says no loans to related parties (p.244). 🟢

## EXTRACTION BY TEMPLATE AREA (Pass 1)

### 1. Accounting policies and changes (Annexure IV, pp.229-231)
- Framework: Indian GAAP under AS notified under Sec.133 (Note 2.A(a)(i), p.229). MD&A text refers to Ind AS (p.264, "in accordance with Ind AS and Schedule II"): wrong standard. 🟡
- Only change: retirement benefits were on cash basis, restated to actuarial AS 15 basis (Auditor report 7(k), p.223; Annexure VII, p.249). FY24 PAT 287.16 to 283.47 (gratuity -4.93, deferred tax +1.24). Opening FY24 reserves reduced 10.78 and FY24 P&L adjustment 3.69 (p.249). Unfunded plan since inception. FY25 and FY26 books carry no restatement adjustments. 🟡
- Revenue (Note 2.A(v), pp.229-230): AS 9. Supply, integration and commissioning of equipment treated as a single obligation, recognised on delivery or commissioning (risks and rewards). Where installation is essential, percentage-of-completion (cost-to-cost or milestone). Rental recognised straight line. The policy allows two bases (delivery vs POC). Which contracts use POC, and the POC revenue amount: NOT FOUND IN DOCUMENT. Unearned revenue appears first in FY26 (166.50, p.234). 🟡
- Depreciation: WDV, Schedule II lives. Computers 3, electrical 5, furniture 10, vehicles 8, intangibles 10, plant and machinery 15 years (p.230). No change in lives. 🟢
- Capitalisation threshold: NOT FOUND IN DOCUMENT. Policy capitalises financing costs till commercial production; none capitalised in the P&L (finance cost 36.71 all charged, p.239).
- Impairment: policy only, no test assumptions (p.230). Nothing impaired. 🟢
- Operating cycle 12 months (p.231).
- Provident fund: policy says "Presently, the company has not deducted any amount towards Provident fund" (p.231) yet P&L carries "Contribution to Provident and Other fund" 23.26 / 27.24 / 9.17 (Note II.5, p.239). Contradictory. PF compliance cannot be checked without CARO. 🟡
- Leave encashment: no policy or liability disclosed. Restatement table shows nil leave adjustment (p.249); deferred tax table cites "Gratuity & Leave encashment" (p.241). NOT FOUND IN DOCUMENT. 🟡
- Ind AS 116, ECL: not applicable under AS; no lease liability or ROU; machine lease cost 22.48 / 127.48 / 160.78 in Note II.3 (p.239), falling as owned scanners were bought. 🟢

### 2. Related party transactions
See LBF-4 above for the table and sizing. Computed totals from Annexure VIII, excluding loans, rupees lakh: FY26 384.19 = 3.63% of revenue (remuneration 281.35 + other 102.84); FY25 351.78 = 5.41% of revenue (remuneration 185.60 + other 166.18). Loans borrowed from related parties FY26 114.46, repaid 382.39 (computed from p.250). New related parties FY26: Jhaveri (WTD), Jain (CFO), Krithika (CS), Venkatesh, Vaid. New transaction counterparties FY25: Sangeetha Hinduja (consultancy 12.00, FY25 only), Punita Shah commission 1.50 / 3.50 / 7.00. Dependency of sales on related parties: none disclosed.

### 3. Contingent liabilities (Annexure V xiii, p.244; also p.56, p.255)
| Nature | FY26 | FY25 | FY24 | Stage / view |
|---|---|---|---|---|
| Performance bank guarantees to customers | 592.85 | 394.20 | 119.82 | None invoked up to 26-Jun-2026 (auditor certificate, p.56) |
- Computed: 592.85 = 14.3% of net worth 4,140.67 (FY25 14.1% of 2,789.90; FY24 12.2% of 985.99). Above the 10%-of-net-worth line. Fund-based borrowings nil, non-fund IOB limit 800 with 592.85 used (74.1%) (p.255). Guarantee growth +50.4% vs revenue +62.6%. The LG facility has 207.15 headroom (computed). 🟡
- Tax disputes: GST 1 case Rs 6.28 lakh; income tax 5 cases Rs 8.59 lakh (including interest and pending payment) = 14.87 (p.244, litigation table). These are **not** in the contingent liability table (only BG listed). 0.36% of net worth. 🟡
- Guarantees for subsidiaries: no subsidiaries. Capital commitments: NOT FOUND IN DOCUMENT.
- Litigation (Section VI) is outside the notes universe for this pass; the group-company suit against Gee Gee (suit value 112.75 lakh, p.272ff text twin line 16918) is noted for stage 8.

### 4. Trade receivables
Covered under LBF-2. Receivable days trend (average basis) 83, 89, 74; year-end 144, 111, 79.

### 5. Inventory (Note I.13, II.4)
- Traded goods only: 1,043.71 / 756.63 / 328.73 (p.235). No raw material, WIP or finished goods lines, though MD&A says changes in inventories include "work-in-progress relating to vehicle fabrication" (p.263). Inconsistent. 🟡
- Growth FY26 +37.9% vs revenue +62.6%; FY25 +130.2% vs revenue +115.4% (computed). FY25 build includes about 400 lakh of DNA equipment per MD&A (p.267).
- Days on COGS (7,998.16 less 287.08 = 7,711.08, p.239) computed: year-end 49 / 62 / 63 days (FY26 / FY25 / FY24). Company ratio 8.57x = 42.6 days average (p.245). 🟢 trend.
- Write-downs, NRV provision, obsolescence: NOT FOUND IN DOCUMENT; none shown. Inventory valuation: lower of cost or NRV (p.229). 🟢

### 6. Investments
- No subsidiaries, JVs, investments or ICDs given (Annexure V ii, ix, p.244). Annexure I title lists "Non-current investment I.12" but I.12 prints Other Non-Current Assets (security deposits 112.79, p.235): note numbering is off by one (I.9 fixed assets, I.10 deferred tax, I.11 loans and advances, I.12 labelled differently). 🟢 clerical.

### 7. Borrowings (Notes I.3, I.5, p.233-234; Indebtedness p.255)
| Rs lakh | FY26 | FY25 | FY24 |
|---|---|---|---|
| Bank term loan | nil | 57.68 | 14.46 |
| Bank OD | nil | nil | 35.93 |
| Bill discounting | nil | nil | 150.00 |
| Related-party unsecured loans | nil | 267.93 | 123.32 |
| Total (short-term incl. current maturity) | nil | 325.61 | 315.02 |
- Facilities: IOB Cash Credit 200.00 at RLLR+0.50%, secured by current assets and promoter-family property; IOB LG 800.00; NSIC term loan 150.00 at 10.75%, max 180 days, nil outstanding (p.255). Covenants, breaches, waivers: NOT FOUND IN DOCUMENT. Repayment schedule: nil debt. Lender consent for IPO and change in promoter holding obtained (p.255).
- Floating-rate share: only the IOB CC (nil drawn). Related party borrowings: see LBF-4.
- Interest expense 13.99 plus "Other borrowing cost" 22.72 = 36.71 (Note II.6, p.239). Other borrowing cost is mostly bank guarantee commission, per MD&A definition (p.264). EBITDA (p.248) adds back all 36.71 so EBITDA includes about 22.72 of guarantee cost add-back (computed, 1.2% of EBITDA). 🟡
- Cash 1,316.32, all in bank current accounts and cash (Note I.15, p.236). MD&A ties interest income (8.94) to "fixed deposits" (p.265); no FD is on the balance sheet. Implied yield 0.7% on cash (computed). Pass 3 to follow. 🟡

### 8. Trade payables (Note I.6, p.234)
- 870.56 / 1,042.57 / 325.24: MSME 402.30 / 587.50 / 20.00; others 468.26 / 455.07 / 305.24. All FY26 balances <1 year except 0.77 in 1-2 years. No disputed items. MSME interest due: nil all years; amount beyond the 45-day mark: NOT FOUND IN DOCUMENT. 🟢 on disclosure, 🟡 on MSME share (46.2% of payables, up from 6.1% FY24).
- Payable days (average, company ratio 8.06x, p.245): 45 FY26, 56 FY25 (computed). Year-end on COGS: 41 / 85 / 63 days (computed).
- Payable-turnover and receivables together (computed year-end days): FY26 79 + 49 - 41 = 87; FY25 111 + 62 - 85 = 88; FY24 144 + 63 - 63 = 144. MD&A KPI "net working capital days" 124 / 141 / 98 (p.257) is a different measure.

### 9. Provisions
- Gratuity (Note II.12, pp.242-243): unfunded, plan assets nil. Present value of obligation 50.54 / 41.11 / 19.34. Discount rate 7.30% / 6.65% / 7.22%; salary growth 8%; attrition 10%; mortality IALM 2012-14 at 100%. Expense 9.43 / 21.77 / 4.93 including actuarial gain (3.61) FY26 and loss 11.29 FY25. Benefits paid nil in all three years despite 10% attrition (likely under the five-year vesting rule). 🟡 (small).
- Warranty provision: NOT FOUND IN DOCUMENT; no warranty provision line, though MD&A cites warranty/AMC service inputs (p.264). Employee benefits: current 22.68, non-current 27.87 (p.243). Current tax provision 470.02 (p.235). Litigation provisions: none.

### 10. Deferred tax (Notes I.10, II.10, Annexure IX; pp.235, 241, 252)
- Net DTA 24.85 / 23.58 / 8.95. Drivers: gratuity (2.37), bad-debt provision (0.15), fixed assets +1.25. DTA recognised only with "reasonable/virtual certainty" (p.230).
- Tax rate 25.17% under Sec.115BAA; no MAT. Effective (current plus deferred plus earlier year) = 470.69 / 1,821.45 = 25.84% computed. Tax-shelter reconciliation shows 41.00 of Sec.37 disallowed expenses FY26 vs 4.82 FY25 (p.252). CSR 12.00 is not allowable under Sec.37(1) and plausibly forms part of it (inference). 🟢
- Unrecognised DTA: none disclosed.

### 11. Revenue details (Note II.1, p.239)
- Goods 9,620.04 / 5,608.52 / 2,253.45; services 951.24 / 894.17 / 763.50; other operating nil / nil / 1.37. Services grew 6.4% FY26 vs goods 71.5% (computed), so services share fell from 25.3% FY24 to 9.0% (computed). Segment reporting: one segment (p.245).
- Product-line revenue is in MD&A only (p.265-267): Forensic Science & Physical Evidence 3,910.84 FY26 vs 1,859.28 FY25 vs 1,178.74 FY24; Cyber & Digital 3,522.83 vs 1,507.05; Mobile CSI vehicles 1,640.66 FY25 vs 405.08 FY24; DNA 615.72 FY25 vs 42.66 FY24. FY26 vehicle and DNA revenue: NOT FOUND IN DOCUMENT in the pages read. Vehicles sold 25 / 47 / 21 (p.259). Customers served 95 / 124 / 128 (p.259), so customers fell 23.4% while revenue rose 62.6% (computed). 🟡
- Contract assets/liabilities: **Unearned revenue 166.50 first appears FY26** (nil FY25 and FY24); advance from customers 22.18 / 8.72 / 6.33 (Note I.7, p.234). Unsatisfied performance obligations and top-customer disclosure: NOT FOUND IN DOCUMENT (AS 9, not AS 7 / Ind AS 115 basis). 🟡
- Exports 17.04 / 13.04 / 1.13 (0.16% of revenue, p.246).

### 12. Other critical notes
- **Exceptional items:** none (p.227). Prior-period items: none.
- **Intangibles:** software 11.00 gross, amortised 10 years (p.237); software under development 137.17, ageing: 75.47 under 1 year, 61.70 1-2 years (p.237). No amortisation until commissioned; completion timetable NOT FOUND IN DOCUMENT. 🟡
- **PPE:** FY26 additions 206.59 of which plant and machinery 164.50 (handheld X-ray scanners for liquor detection, MD&A p.266) and vehicles 32.18. FY25 plant additions nil (p.237). Gross block 429.55, net 293.45. Fixed asset turnover 32.77x (p.257). 🟢
- **Foreign currency:** expenditure labelled "Import of services" 643.03 / 632.14 / 507.70 (p.246) against goods purchases; the label does not match a traded-goods importer, and equals 8.0% of FY26 purchases (computed). Hedging: policy mentions forward contracts but no contracts or unhedged exposure disclosed. Forex loss 0.41 only. 🟡
- **EPS:** Basic equals diluted. FY26 8.00. FY25 reported 43.31, bonus-adjusted 5.41; FY24 68.59 vs 8.57 (p.242). Weighted-average share counts FY25 19,76,235 (x8 = 1,58,09,880 vs printed 1,58,09,877). Dilution sources: none (no ESOP disclosed). 🟢
- **Share capital:** 7:1 bonus on 16-Sep-2025, 1,47,65,485 shares, Rs 1,476.55 lakh capitalised from securities premium 1,090.05 and surplus 386.50 (p.233). Authorised capital raised 225.00 to 2,500.00 lakh. Private placements: FY24 16,00,050 shares for 320.01 net (Rs 20 per pre-bonus share, computed); FY25 1,79,295 shares for 947.97 net (Rs 569 per pre-bonus share, computed, p.228, p.233). A 28x jump in placement price in one year; investors named: NOT FOUND IN DOCUMENT in Section V. 🟡
- Promoter holding: 90.25% FY24, 78.08% FY25 and FY26 (p.232-233); Shammer Shah 53.76%.
- **CSR:** required 11.55, spent 12.00, no shortfall (first applicable year), "Construction of the college building" (p.240). Beneficiary institution and any link to promoters: NOT FOUND IN DOCUMENT; RPT item "NA". 🟢/🟡
- **Auditor fees:** 2.91 (audit 2.00, other certifications 0.91) vs 3.28 FY25 (p.240). Small relative to Rs 105 Cr revenue. 🟡
- **Events after balance sheet:** NOT FOUND IN DOCUMENT in Section V; the notes carry no subsequent events note. Approval date 25-May-2026 (p.247). Bonus issue and IPO (Sep-2025 onward) lie within FY26.
- **Reserves bypass:** none beyond bonus capitalisation and IPO expense charged to securities premium (72.22 FY25, p.233). Share issue expenses of 72.22 were also deducted as "Allowable Issue Related Expenses" in the tax computation (p.252).
- **Audit trail:** edit log operated throughout (Annexure V xviii, p.247). 🟢
- **Operating costs:** Commission expense 111.22 (vs 54.64 FY25; 1.1% of revenue), Business development 31.50, Exhibition 31.62 (vs 5.34), Contract services 43.27 (vs 10.32), Rates and taxes 18.65 (vs 0.02), Legal 21.60 (vs 8.02), Legal/rates jump is IPO-linked (inference). Commission payees: NOT FOUND IN DOCUMENT. Other expenses 466.91 fell to 4.4% of revenue from 13.7% FY24 (computed). Employee cost 495.85 is 4.7% of revenue. 🟡
- **Other current liabilities:** statutory dues payable 183.03 (38.91 FY25), accrued expenses 75.52 identical in FY25 and FY26 (no movement), interest payable 1.06 (p.234). Statutory dues outstanding at year end: NOT CHECKABLE without CARO. 🟡

## PASS 1 SUMMARY: top 10 findings by investor importance

| # | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | CFO is 56.4% of PAT (Rs 762.30 vs 1,350.77 lakh); three-year CFO 38.8% of PAT. FY26 cash tax 281.74 vs accrued 470.02, so CFO benefits from 188.28 of unpaid tax. | Annexure III p.228; Note I.8 p.235; II.9 p.241 | 🟡 |
| 2 | Non-government customers (Rs 4,733.92 lakh, 82.7% of FY26 revenue growth) are unnamed. No related-party sale or receivable disclosed; completeness untestable. B2C undefined. | Risk Factor 10 p.29; top-10 pp.160-161; Annexure VIII pp.250-251 | 🟡 |
| 3 | Debtor days 74 is an average-balance figure; year-end days 79 (144, 111, 79). Improvement is real on both bases; Q4 share unknown for FY26 (51% in FY25). | pp.92-93, p.245, p.226-227 | 🟢 |
| 4 | Rs 130.54 lakh at 2-3 years barely moved (135.30 a year earlier); provision 27.00 (20.7%) while FY25's 2-3 year bucket was 100% provided. No ECL policy. Ageing roll-forward anomaly of 26.27. | Note I.14 p.235; policies pp.229-231 | 🟡 |
| 5 | Unearned revenue 166.50 appears for the first time; customer advances only 22.18 against a management claim of 30-50% advance from private buyers. | Note I.7 p.234; p.92 | 🟡 |
| 6 | Related-party stack: remuneration 281.35 (+51.6%), Gostocks software purchases 78.70 over two years vs software CWIP 137.17 unamortised, rent to MD 7.88, purchases from group partnerships 67.00. Arm's-length evidence absent. | Annexure VIII pp.250-251; Note I.9 p.237 | 🟡 |
| 7 | Promoter funding repaid: MD borrowed 1,249.73 lakh over FY24-26; all related party debt nil at FY26. Debt nil, cash 1,316.32. | Annexure VIII p.250; Capitalisation p.254 | 🟢 |
| 8 | Guarantees and collateral from promoter family including two persons not in the RPT list (Bina Shah, Saloni Shah); no fee disclosed. Performance BG 592.85 = 14.3% of net worth. | Note I.5 text p.234; Annexure V xiii p.244 | 🟡 |
| 9 | Internal contradictions: PF "not deducted" vs PF expense; MD&A cites Ind AS and says FY26 borrowings were "proceeds"; only traded-goods inventory vs WIP language; FD interest vs no FD; "Import of services" label. | pp.231, 239, 263-264, 268, 236, 246 | 🟡 |
| 10 | Indian GAAP basis, auditor change in FY25, FY24 gratuity restated from cash basis (PAT 287.16 to 283.47), unfunded gratuity, tax demands (14.87) outside contingent table. Placement price Rs 20 to Rs 569 per share in one year. | pp.223, 249, 243, 244, 233 | 🟡 |

Greens worth recording: zero borrowings; MSME interest nil; CSR compliant; audit trail on; no qualifications in audit reports; inventory trend improving; closing balance sheet foots.

## Handover to Pass 2 (items to re-read with the cross-reference lens)
Inventory build vs DNA; Q4 revenue share; purchase of asset vs CWIP; other-current-asset movement; tax paid vs advance tax; ratio tables in Annexure V against base statements; ROCE and ROE formula arithmetic; "accrued expenses" frozen at 75.52; the unearned-revenue origin; Note numbering (I.12).

```yaml
stage: B02-notes
company: "KWICK"
run_date: "2026-10-04"
model: claude-sonnet-5-5
status: pass1_complete
input_gaps:
  - "No annual report: AR substitute is Prospectus 31-Aug-2026 restated financial information, Rs lakh, Indian GAAP (AS), pp.221-270"
  - "No CARO or directors report: PF, statutory dues, Sec.185/188 checks not possible"
  - "Customers unnamed: non-government buyers (Rs 4,733.92 lakh FY26) not identified, B2C undefined"
  - "No ECL or doubtful-debt policy, no ageing basis, no govt vs private receivable split"
  - "FY26 Q4 revenue share, advance tax detail, commission payees, placement investors: not disclosed"
flags:
  - {type: FLAG-CASH, reason: "CFO/PAT 56.4% FY26 (762.30 vs 1350.77 Rs lakh), 54.3% FY25, negative FY24; FY26 cash tax 281.74 vs accrued 470.02; 3-yr receivable build 2107.28 = 84.6% of 3-yr PAT. Receivable days improving, conversion still weak (Annexure III p.228)"}
  - {type: FLAG-CUSTOMER-ID, reason: "Non-government customers 4733.92 Rs lakh (44.78%) unnamed; no RPT sale or receivable disclosed but completeness untestable (p.29, pp.160-161, pp.250-251)"}
  - {type: FLAG-RPT, reason: "Remuneration 281.35 +51.6%; Gostocks software 78.70 over FY25-26 vs software CWIP 137.17 unamortised; promoter-family guarantees incl. Bina Shah and Saloni Shah not in RPT list (pp.234, 237, 250)"}
  - {type: FLAG-RECEIVABLE-QUALITY, reason: "130.54 Rs lakh at 2-3 years, barely collected in a year, provided 20.7%; no ECL policy; ageing roll-forward anomaly 26.27 (Note I.14 p.235)"}
accounting_quality: 5
pass_2_empty: false
pass_3_empty: false
top_findings:
  - {rank: 1, finding: "CFO 762.30 Rs lakh is 56.4% of PAT 1350.77; cash tax 281.74 vs accrued 470.02 flatters CFO by 188.28", note_ref: "Annexure III p.228; Note I.8 p.235; II.9 p.241", rating: "YELLOW", why: "Profit is not converting to cash at the pace of growth; the unpaid FY26 tax is a coming outflow"}
  - {rank: 2, finding: "Non-government customers Rs 4733.92 lakh (82.7% of FY26 revenue growth) unnamed; no related-party sale or receivable disclosed", note_ref: "Risk Factor 10 p.29; top-10 pp.160-161; Annexure VIII pp.250-251", rating: "YELLOW", why: "Largest growth driver cannot be traced to counterparties; completeness of RPT untestable"}
  - {rank: 3, finding: "Debtor days 83/89/74 are average-balance; year-end days 144/111/79; FY26 improvement real on both bases", note_ref: "pp.92-93; Annexure V p.245; pp.226-227", rating: "GREEN", why: "Stated metric is understated vs year-end but trend is genuinely improving"}
  - {rank: 4, finding: "Rs 130.54 lakh receivable at 2-3 years provided 27.00 (20.7%) vs 100% on FY25 2-3 year bucket; no ECL policy; roll-forward anomaly 26.27", note_ref: "Note I.14 p.235; policies pp.229-231", rating: "YELLOW", why: "Provisioning follows no stated rule; stuck government or private dues"}
  - {rank: 5, finding: "Unearned revenue 166.50 first appears FY26; customer advances only 22.18 vs claimed 30-50% advance from private buyers", note_ref: "Note I.7 p.234; p.92", rating: "YELLOW", why: "Management narrative for faster collections not visible in balance sheet; revenue timing policy has two bases"}
  - {rank: 6, finding: "Related-party stack: remuneration 281.35, Gostocks software 78.70, group purchases 67.00, rent to MD 7.88; arm's-length evidence absent", note_ref: "Annexure VIII pp.250-251; Note I.9 p.237", rating: "YELLOW", why: "3.63% of revenue excluding loans; software CWIP 137.17 unamortised"}
  - {rank: 7, finding: "Promoter loans repaid: MD borrowed 1249.73 over FY24-26; related-party debt nil, total borrowings nil, cash 1316.32 at FY26", note_ref: "p.250; Capitalisation p.254", rating: "GREEN", why: "Balance sheet funding no longer depends on promoters"}
  - {rank: 8, finding: "Promoter-family collateral and personal guarantees incl. two persons not in RPT list; performance BG 592.85 = 14.3% of net worth", note_ref: "Note I.5 text p.234; Annexure V xiii p.244", rating: "YELLOW", why: "Credit support still promoter-dependent; unpriced; guarantee headroom 207.15 of 800"}
  - {rank: 9, finding: "Internal contradictions: PF not deducted vs PF expense; Ind AS cited vs AS used; MD&A calls FY26 borrowings proceeds not repayment; WIP vs traded-goods-only inventory", note_ref: "pp.231, 239, 263-264, 268", rating: "YELLOW", why: "Disclosure quality weak; PF compliance uncheckable without CARO"}
  - {rank: 10, finding: "Indian GAAP, FY25 auditor change, FY24 gratuity restated from cash basis, unfunded gratuity, tax demands 14.87 outside contingent table, placement price Rs 20 to Rs 569 per share in a year", note_ref: "pp.223, 233, 243, 244, 249", rating: "YELLOW", why: "Accounting infrastructure pre-IPO was thin"}
red_flags: []
questions_for_mgmt:
  - "Name the top 10 customers FY26 split government vs private, and say which non-government buyers resell to government."
  - "What is the ageing basis and the provisioning rule? Why is the 2-3 year bucket of Rs 130.54 lakh 20.7% provided?"
  - "Why was FY26 cash tax 281.74 against accrued 470.02? Was FY26 advance tax paid and is there interest exposure?"
  - "What is the software under development (Rs 137.17 lakh), who built it, and when is it commissioned?"
  - "What is behind the Rs 166.50 lakh unearned revenue and the claimed 30-50% advance from private customers?"
receivables_trend: "improving: average-basis days 83 / 89 / 74 (company), year-end days 144 / 111 / 79 (computed); receivables Rs lakh 1193.58 / 1979.05 / 2288.07; >6 months 11.85% of gross FY26 vs 16.97% FY25 vs 12.32% FY24; >1 year 165.60 (7.14%) FY26, with 130.54 aged 2-3 years and 27.00 provided (Note I.14 p.235, pp.92-93)"
restatements_found:
  - "FY24 PAT 287.16 restated to 283.47 Rs lakh: gratuity moved from cash to AS 15 actuarial basis (-4.93), deferred tax +1.24; reserves adjusted -3.69 FY24 P&L and -10.78 opening (Annexure VII p.249)"
going_concern_language: "NONE in Section V notes pp.221-270 (a later section table states no audit qualification w.r.t. going concern; page not located)"
analyst_note: "Units are Rs lakh as printed; stage 10 converts once. Basis is Indian GAAP, standalone, no subsidiaries. Receivable days improvement is real but the stated 74 is an average-balance figure; year-end is 79. The cash story is weaker than the days story: CFO/PAT 56.4%, helped by 188.28 of unpaid FY26 tax. Customer-identity gap on non-government buyers (82.7% of FY26 growth) is a disclosure gap, not evidence of a related-party customer; no related-party sale or receivable appears anywhere in Annexure VIII. Score 5 reflects thin policies (no ECL rule, two revenue bases, PF contradiction), anonymous customers, and unsupported arm's-length claims, offset by zero debt, clean audit reports and full RPT listing."
```
