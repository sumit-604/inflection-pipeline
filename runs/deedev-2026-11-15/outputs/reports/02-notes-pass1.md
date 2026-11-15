# Stage 2 Notes Pass 1 (full extraction) - DEEDEV, run 2026-11-15

Source: Annual_Report_2026.txt (FY2025-26, 352 pages). Unit on the face of the document: INR lacs ("lacs"), standalone and consolidated. No conversion is made here; stage 10 converts once.
Anchor form: (Note N, p.PDF-page). PDF page = printed page minus 20. "Derived" marks my arithmetic on anchored inputs.
Scope: standalone Notes 1-47 (pp.164-251) and consolidated Notes 3-16, 27-31, 38-46 (pp.288-351) are read. Consolidated policy text, consolidated deferred-tax movement table, fair-value/risk notes 32-34 and consolidated Notes 35-37 are NOT read line by line in this pass (see Coverage at the end).
Rating: GREEN clean | YELLOW watch | RED red flag. Written as 🟢 🟡 🔴 in the tables.

## 0. LOAD-BEARING FACTS check (first priority, from companies/DEEDEV.md)

| Fact | What the notes show | Anchor | Rating |
|---|---|---|---|
| Abohar tariff contingency (about Rs 13.85 cr refund to PSPCL, unprovided) | CONFIRMED. PSERC order 15 May 2025 cut tariff from Rs 7.48 to Rs 5.26 per unit retrospectively from 1 Jan 2024, payable Rs 1,682.87 lacs. Review order 20 Aug 2025 set Rs 5.88, payable Rs 1,384.96 lacs, recovery capped at 50% of monthly bills. PSPCL appealed to APTEL. Company filed a writ in the Punjab and Haryana High Court; interim order 23 Sep 2025 stayed the PSERC order. No provision made, "strong likelihood of succeeding" per legal opinion. | Note 46, p.251 (standalone) | 🔴 |
| Same item in the contingent-liability table | NOT FOUND IN DOCUMENT. Note 32B lists income tax 350.62, excise/GST 622.54, customs bond 1,759.76 and export obligation 20,237.29 only. The Rs 1,384.96 lacs sits in Note 46, not in the contingency table. | Note 32B, p.229 | 🟡 |
| Auditor Emphasis of Matter | CONFIRMED on both reports. Standalone: opinion unmodified, EoM on Note 46. Consolidated: QUALIFIED opinion (see Malwa below) plus the same EoM on Note 45(a). | Standalone auditor report, EoM paragraph (text line 9467); consolidated auditor report p.253 | 🔴 |
| Size against profit (derived) | 1,384.96 / PBT 7,235.45 = 19.1%. 1,384.96 / net worth 88,706.85 = 1.56%. | Note 46 p.251; Note 17B p.205; Note 37 p.243 | |
| Standalone and consolidated texts differ | Consolidated Note 45(a) says tariff cut to Rs 5.42, payable "Rs 14 crores", review petition pending before PSERC. It does not mention the Rs 5.88 review order or the High Court stay. Standalone Note 46 gives Rs 5.26 then Rs 5.88, Rs 1,384.96 lacs and the stay. Two filings of the same date state the dispute differently. | Cons. Note 45(a), pp.350-351 vs Note 46, p.251 | 🟡 |
| Billing after 31 Mar 2025 | NOT FOUND IN DOCUMENT. Consolidated text computes the excess for 1 Jan 2024 to 31 Mar 2025 only. The notes do not say what tariff Abohar billed from 1 Apr 2025 or whether any further excess has built up in FY26. | Cons. Note 45(a), p.350 | 🟡 |
| Malwa Power (MPPL) carrying value | Standalone: investment in MPPL 959.01 (FY25 943.83), includes deemed ESOP investment 15.18; loan to MPPL 151.00 at 10% due 30 Jun 2028 (FY25 295.00); guarantee outstanding 527.04 (FY25 768.74); trade receivable 310.05 (FY25 nil). New guarantee of 2,300.00 given in FY26. No impairment booked. Consolidated: group assets of MPPL 4,761.67; auditor cannot assess impairment, giving a QUALIFIED opinion. | Note 5 p.184; Note 31B-C pp.223,225; Note 31F p.228; Cons. auditor report p.253; Cons. Note 45(b) p.351 | 🔴 |
| MPPL tariff and trading | PPA expired 27 Apr 2025. Old tariff Rs 8.59 per kWh. Interim Rs 3.50 (PSERC 24 Apr 2025, APTEL 8 Dec 2025). Final PSERC order 27 Mar 2026 sets Rs 5.22 per kWh with 5% annual escalation on the variable component, subject to the APTEL appeal. Management: "adversely impacted the operational viability" and "uncertainty over its future cash flows"; "unable to assess" carrying value. MPPL FY26 loss 555.04 (FY25 profit 345.10); net assets 2,656.50 (FY25 3,185.89). | Cons. Note 45(b), p.351; Cons. net-asset table, p.344 | 🔴 |
| Loans to subsidiaries and guarantees | Loans 4,181.51 total (FY25 4,477.52): Thailand 3,630.51 at 7.5% due 31 Dec 2028; MPPL 151.00; Fabricom 400.00 at 10% due 30 Jun 2028. All unsecured, no impairment. Guarantees outstanding 668.89 (FY25 5,220.12) = MPPL 527.04 + Fabricom 141.85; Thailand 0 (FY25 4,009.54). No guarantee commission received. | Note 6B p.188; Note 31C p.225; Note 31E(vi) p.227; Note 32C p.230 | 🟡 |
| Related-party notes | See Section 2. | Note 31 pp.222-228 | 🟡 |
| Customer concentration | Numaligarh Refinery 17,268.79 = 18.80% (FY25 4.38%); Dow Chemical Canada 11,048.38 = 12.03% (FY25 0.12%). | Note 33(c), p.234 | 🟡 |
| Inventory, receivables, cash flow | See Sections 4, 5 and 12. Operating cash flow -4,450.03 (FY25 -15,428.58). | Cash flow p.160; Note 6A p.186; Note 8 p.192 | 🔴 |

## 1. Accounting policies and changes

- Basis: Ind AS, historical cost. Going-concern basis stated. (Note 2.1, p.164)
- Revenue: goods at a point in time "generally on delivery"; electricity over time per unit delivered; job work at the point goods transfer; erection over time. Company is principal. (Note 2.2(e), pp.166-167) 🟢 policy. Cut-off watch: finished goods in transit 1,593.55 at 31 Mar 2026 (FY25 165.32), which is 50.7% of finished goods 3,141.17 (derived). (Note 8, p.192) 🟡
- Depreciation: straight line. Buildings 15-60 yrs, plant 5-30 yrs, furniture 8-10, office equipment 3-5, vehicles 8-10. Management states some lives differ from Schedule II as per technical assessment. No change in lives disclosed. Items of Rs 5,000 or less fully depreciated in year of purchase. (Note 2.2(g), pp.168-169) 🟡 (wide plant range 5-30 yrs, basis not given)
- Software amortised over 6 years or licence period. (Note 2.2(h), p.169)
- Borrowing cost capitalised 623.19 (FY25 369.23) at 9.20% (FY25 9.65%). Pre-operative expenses capitalised 370.03 (FY25 356.63), of which employee benefits 253.85. (Note 3 v,viii, pp.182-183) 🟡
- Leases (Ind AS 116): ROU assets 1,457.92 (FY25 1,789.53); lease liability 1,684.92 (current 500.28, non-current 1,184.64). Consolidated effective rate 10%, maturity 2025-2034. Land lease terms: renewals assumed in lease term. (Note 38 pp.243-245; Note 29 p.217; Cons. Note 39 p.348) 🟢
- Inventory: lower of cost and NRV, weighted average; finished goods include overheads on normal capacity. (Note 2.2(k), p.171) 🟢
- ECL: simplified approach, provision matrix; allowance is nil in standalone for both years. Consolidated allowance: 1.98 credit-impaired in the 1-2 year bucket, shown as "utilisation/reversal" with closing (1.98). (Note 6A p.186; Note 29 p.219; Cons. Note 4A pp.292-293) 🟡
  - Cash-flow add-back "Provision for doubtful debts and advance 39.74" and Note 25 line 39.74 exist, but Note 6A shows no allowance movement. Where the 39.74 sits on the balance sheet: NOT FOUND IN DOCUMENT. (Cash flow p.160; Note 25, p.213) 🟡
- Impairment assumptions: standalone Note 29 gives no rates. Consolidated goodwill test: VIU, 5-year budget, terminal growth 2% (unchanged), discount rate 9% to 12.5% (FY25 13.00%), no impairment. (Cons. Note 3A, p.291) 🟡 (lower discount rate than last year; which CGU holds the 271.18 legacy goodwill: NOT FOUND IN DOCUMENT)
- Policy changes with P&L impact: none disclosed except the labour-code past service cost (Section 12).
- First-time standards: NOT FOUND IN DOCUMENT in the notes read.

## 2. Related party transactions (standalone, INR lacs; Note 31, pp.222-228)

Related parties: subsidiaries Malwa Power Pvt Ltd (MPPL), Dee Piping Systems (Thailand) Co Ltd, Dee Fabricom India Pvt Ltd, Atul Krishan Bansal Foundation (section 8 company), Molsieve Designs Ltd (70%, from 19 May 2025, new this year). KMP: K.L. Bansal (CMD), Ashima Bansal (WTD till 14 Apr 2025), Shikha Bansal (WTD), Shruti Aggarwal (WTD from 14 Apr 2025), Sameer Agarwal (CFO till 6 Jan 2026), Brham Prakash Yadav (CFO from 7 Jan 2026), Ranjan Sarangi (CS). Relatives of the former CFO on payroll till 6 Jan 2026.

| Party | Nature | FY26 | FY25 | YoY |
|---|---|---|---|---|
| MPPL | Sales of product | 337.21 | 114.28 | +195.1% (derived) |
| MPPL | Interest income | 10.93 | 12.84 | -14.9% |
| MPPL | Interest expense | 14.34 | 0.14 | n.m. |
| MPPL | Loan given / repaid | 276.00 / 420.00 | 625.00 / 520.00 | |
| MPPL | Loan taken / repaid | 760.00 / 760.00 | 60.00 / 60.00 | |
| MPPL | Corporate guarantee given in year | 2,300.00 | 768.74 | |
| Thailand | Sales of product | 655.46 | 690.80 | -5.1% |
| Thailand | Interest income | 255.49 | 549.53 | -53.5% |
| Thailand | Purchase of traded goods | 86.33 | 18.45 | |
| Thailand | Purchase of fixed assets | 169.66 | NOT FOUND (blank) | |
| Thailand | Loan converted to equity | nil | 4,189.34 repayment / 4,169.47 equity | |
| Fabricom | Sales of product | 6.11 | 121.71 | -95.0% |
| Fabricom | Rent paid | 12.00 | 12.00 | 0% |
| Fabricom | Interest income | 64.34 | 106.31 | -39.5% |
| Fabricom | Loan given / repaid | 415.00 / 915.00 | 100.00 / 460.00 | |
| Fabricom | Guarantee given in year | 1,916.33 | 2,328.00 | |
| Fabricom | Purchase / sale of fixed assets | 226.15 / 104.83 | 29.47 / nil | |
| Atul Krishan Bansal Foundation | CSR contribution | 54.29 | 42.50 | +27.7% |
| Molsieve | Rent received / electricity | 2.18 / 1.00 | nil | new |
| K.L. Bansal | Remuneration | 202.51 | 187.79 | +7.8% |
| K.L. Bansal | Loan received / repaid | 110.00 / 765.00 | 1,855.00 / 1,200.00 | |
| K.L. Bansal | Rent | 0.84 | 0.84 | 0% |
| Ashima Bansal | Remuneration | 13.53 | 83.60 | -83.8% (left 14 Apr 2025) |
| Shikha Bansal | Remuneration | 42.81 | 42.09 | +1.7% |
| Shruti Aggarwal | Remuneration | 67.34 | 66.43 | +1.4% |
| Sameer Agarwal (ex-CFO) | Remuneration | 63.44 | 48.23 | +31.5% |
| Charu Agarwal (spouse of ex-CFO) | Remuneration | 42.05 | 40.88 | +2.9% |
| Naveen Kishore Agarwal (brother of ex-CFO) | Remuneration | 27.67 | 32.37 | -14.5% |
(Note 31B, pp.223-224)

Year-end balances (Note 31C, pp.224-225): MPPL loan 151.00, guarantee 527.04, receivable 310.05. Thailand loan 3,630.51, interest receivable (net of withholding tax) 2,894.76 (FY25 2,514.84), receivable 760.52 (FY25 904.81), payable 128.08. Fabricom loan 400.00, guarantee 141.85 (FY25 441.84), interest receivable nil (FY25 95.68). Molsieve receivable 2.56. K.L. Bansal director loan nil (FY25 655.00). New advances to directors: Shikha Bansal 29.46, Shruti Aggarwal 7.69 (total 37.15, FY25 nil). KMP compensation 491.69 (FY25 538.98) (Note 31D, p.225).

- RPT as % of revenue 91,855.73 (derived): sales to subsidiaries 998.78 = 1.09%. 🟢
- Arm's length: company asserts benchmarking for sales, purchases, PPE, job work. No independent evidence. (Note 31E, pp.226-227) 🟡
- Thailand: interest receivable 2,894.76 has grown 379.92 in the year (derived) and is described "net of withholding tax". Total Thailand exposure = equity 9,190.78 + loan 3,630.51 + interest 2,894.76 + receivable 760.52 = 16,476.57 (derived) = 18.6% of net worth 88,706.85. No impairment: "no impairment" per a DCF; "subsidiary has started making profits from current year". (Note 5(b), p.185; Note 31C) 🟡. Thailand interest income fell from 549.53 to 255.49 while the loan rose from 3,282.52 to 3,630.51; the notes do not explain the fall (rate 7.50% per Note 31F). Cash interest received from Thailand: NOT FOUND IN DOCUMENT.
- Guarantees given with no commission received from subsidiaries. (Note 31E(vi), p.227) 🟡
- Promoter security for company debt: personal guarantees of promoters, corporate guarantee of DDE Piping Components Pvt Ltd (10.87% shareholder), second charge on the CMD's Faridabad residence. No fee disclosed. (Note 11A, pp.199-200) 🟡
- CSR: 54.29 of 54.42 (99.8%, derived) routed to the promoter-linked Atul Krishan Bansal Foundation, a wholly owned section 8 subsidiary. (Note 25(b), p.214) 🟡
- Key management turnover: CFO changed 7 Jan 2026. Two relatives of the ex-CFO were on payroll (69.72 combined, derived). (Note 31, p.222) 🟡
- Consolidated vs standalone gaps. Consolidated trade payables include related-party payables of 763.89 (FY25 704.83), of which Shikha Bansal 762.90 (FY25 678.30). The standalone shows Shikha Bansal 26.76. The nature of the 762.90 is NOT FOUND IN DOCUMENT. Consolidated remuneration for Shikha Bansal is 171.04 vs 42.81 standalone. Consolidated KMP pay 1,101.29 vs 491.69 standalone. Consolidated lists K.L. Bansal FY25 loan repayment 1,810.00 vs standalone 1,200.00. (Cons. Note 29, pp.328-329; Cons. Note 15, p.313) 🟡
- Consolidated also says a guarantee of 8,221.69 was given for Thailand in FY2022-23, while standalone Thailand guarantee outstanding is nil at 31 Mar 2026. (Cons. Note 29E(i), p.330 vs Note 31C, p.225) 🟡
- Loans to promoters/directors: none. (Note 6B, p.188) 🟢

## 3. Contingent liabilities (standalone, INR lacs; Note 32B, pp.229-230)

| Nature | FY26 | FY25 | Stage / company view |
|---|---|---|---|
| Income tax demand | 350.62 | 252.46 | Appellate levels; "confident", no provision. Penalty proceedings notices issued. |
| Excise / GST demand | 622.54 | 350.64 | Appellate; "not tenable"; no provision. |
| Customs demand (table shows "-") | nil in table | nil | Note (e) states duty 815.09 plus penalty 305.00 = 1,120.09 (derived), appeal before CESTAT, 7.5% of 815.09 paid under protest. The table line does not carry the amount. 🟡 |
| Customs duty if export obligation unmet | 1,759.76 | 880.44 | +99.9% |
| Export obligation (duty-free imports) | 20,237.29 | 10,033.38 | +101.7%; company "able to fulfil". |
| HMMIPL dispute | claim 127.89, counterclaim 178.49 | n/a | Litigation, no provision |
| Antidumping duty | 72.43 demand; provision 38.15 | | Remaining 34.28 "not payable" under advance authorisation |
| ED FEMA notice (19 May 2023) | no amount | | Information furnished 25 Aug 2023. Outcome: NOT FOUND IN DOCUMENT |
| Customs BRC / export proceeds request | no amount | | NOT FOUND IN DOCUMENT |
| Abohar PSPCL excess revenue | 1,384.96 | | Not in the table. See Section 0 and Note 46. |

- Net worth 88,706.85 (Note 37, p.243). Ratios (derived): table total 22,970.21 = 25.9%; export obligation alone 22.8%; all items except the export obligation 2,732.92 = 3.1%. No single item above 10% except the export obligation. Add Abohar 1,384.96 = 1.6%.
- Provisions made: litigation 188.21 (FY25 91.64); created 96.57. (Note 14, p.204) 🟡
- Corporate guarantees: carrying amount 668.89 (FY25 5,220.12). (Note 32C, p.230)
- Capital commitments 1,257.57 net of advances 1,337.92 (FY25 4,713.19). (Note 32A, p.228) 🟢
- Rating: export obligation doubling follows duty-free import growth; an unmet obligation triggers the 1,759.76 duty bond. 🟡

## 4. Trade receivables (standalone, INR lacs)

- Total 34,304.28 vs 20,307.13, +68.9% (derived) against revenue +43.8% (91,855.73 vs 63,887.26). Related-party portion 1,073.13 (FY25 904.81). (Note 6A p.186; Note 19 p.209)
- Derecognised under supply-chain finance, non-recourse: 15,938.75 (FY25 4,186.33), 3.8x. Receivables plus sold = 50,243.03 vs 24,493.46, +105.1% (derived). (Note 6A, p.186)
- Ageing (from due date), FY26: not due 24,725.49 (72.1%); under 6 months overdue 6,427.85; 6 months to 1 yr 2,915.00; 1-2 yrs 177.71; 2-3 yrs 52.33; over 3 yrs 5.90. FY25: not due 17,301.52; under 6 months 1,925.43; 6m-1y 741.49; 1-2 yrs 323.52; 2-3 yrs 15.17. (Note 6A ageing, p.187)
- Over 6 months overdue: 3,150.94 = 9.2% of total vs 1,080.18 = 5.3% (derived).
- Impairment allowance nil both years, no disputed dues, no credit-impaired. 🟡 given the growth in aged balances.
- Terms: 30 to 180 days. (Note 6A, p.186)
- Concentration: 25 customers over 200 each = about 96% of receivables (FY25 19 customers, 87%); 8 customers over 1,000 each = just over 71% (FY25 6 customers, 33%). The same note says receivables carry no significant credit risk "as the business is majorly cash based". The two statements conflict. (Note 36, p.241) 🔴
- Geography: India 25,842.50 (FY25 12,394.05, +108.5% derived); outside India 8,461.78 (FY25 7,913.08). USD receivables per the FX table: 1,113.63 only. The currency of the remaining foreign balance: NOT FOUND IN DOCUMENT. (Note 33, p.233; Note 36, p.239)
- Receivable days on year-end balance and revenue (derived): 136.3 days vs 116.0. Adding sold receivables: 199.6 vs 139.9. 
- Bank stock-statement tie-out: books 34,304.28 vs bank return 33,001.08, difference 1,303.20 at Mar-26 (FY25 909.06); Sep-25 -517.87, Dec-25 298.06. Reason given: provisional unaudited returns. (Note 11B, pp.201-202) 🟡
- Consolidated: receivables 38,334.05 vs 24,815.67; over-6-month 3,330.28 = 8.7% (derived); consolidated bank-return "books" figure 36,265.63 does not equal the balance sheet 38,334.05 (gap 2,068.42, derived). (Cons. Note 4A p.293; Cons. Note 9B p.306) 🟡
- Verdict for FLAG-CASH: receivables deteriorating.

## 5. Inventory (standalone, INR lacs; Note 8, p.192)

| | FY26 | FY25 | YoY (derived) |
|---|---|---|---|
| Raw materials (incl. in transit 2,355.33; FY25 1,888.84) | 34,054.96 | 35,212.83 | -3.3% |
| Finished goods (incl. in transit 1,593.55; FY25 165.32) | 3,141.17 | 1,500.17 | +109.4% |
| Work in progress | 11,998.87 | 11,853.16 | +1.2% |
| Stores and spares | 1,876.93 | 2,195.38 | -14.5% |
| Packing | 272.60 | 424.58 | -35.7% |
| Total | 51,344.53 | 51,186.12 | +0.3% |

- Finished goods +109.4% vs revenue +43.8%. 🟡
- Write-downs to NRV and obsolescence: NOT FOUND IN DOCUMENT.
- Inventory days on revenue (derived): 204.0 vs 292.4. Raw material is 66.3% of inventory. Inventory is pledged to Bank of India and others. (Note 11B, p.200)
- Bank-return gap: 519.91 at Mar-26 (FY25 -130.82). (Note 11B, p.201) 🟡
- Cash-flow: standalone inventory increase 158.41 (FY25 17,106.97). (Cash flow p.160) 🟢 on trend
- Consolidated total 57,601.52 vs 58,496.46; consolidated bank-return "books" 52,604.54 does not equal 57,601.52 (gap 4,996.98 derived). (Cons. Note 6, p.296; Cons. Note 9B, p.306) 🟡

## 6. Investments (standalone, INR lacs; Note 5, pp.184-185)

| Entity | Holding | Carrying FY26 | FY25 |
|---|---|---|---|
| Malwa Power Pvt Ltd | 100%, 1,22,09,680 shares | 959.01 | 943.83 |
| Dee Fabricom India Pvt Ltd | 100%, 90,00,000 shares | 900.00 | 900.00 |
| Dee Piping Systems (Thailand) | 100%, 8,20,00,000 shares THB 5 | 9,190.78 | 9,190.78 |
| Atul Krishan Bansal Foundation | 100% | 1.00, fully provided | 1.00 provided |
| Molsieve Designs Ltd (new) | 70%, 35,000 shares | 658.82 | nil |
| Total | | 11,708.61 | 11,034.61 |

- All at cost, unquoted. No impairment booked other than the foundation. Thailand: "accumulated losses envisaged", profits "from current year", DCF supports no impairment. (Note 5(b), p.185) 🟡
- Molsieve: consideration 658.82; identifiable net assets 80.37; 70% share 56.26; goodwill 602.56 = 91.5% of consideration (derived). Implied 100% price 941.17 = 11.7x net assets (derived). Acquired assets 291.90. Date 19 May 2025. Advance for shares 100.00 was outstanding at FY25. No contingent consideration. Others payable 75.00 non-current includes "deferred purchase consideration and customer claim", split not given. (Note 43, p.250; Note 12, p.203) 🟡
- Loans given: see Section 2; all unsecured, 7.5% to 10%, repayment 2028 to 2030. (Note 6B, p.188)
- Other investments with unrealised gains: none; company holds no quoted equity. (Note 36, p.240)
- Fair value: related-party loans and interest 7,076.27 carried at Level 3, "DCF" with undisclosed inputs. (Note 35, p.236) 🟡

## 7. Borrowings (standalone, INR lacs; Note 11, pp.197-203)

- Non-current: bank term loans 12,498.52 (FY25 5,699.07) plus current maturities 3,177.81; vehicle loans 96.31 plus 129.66; NBFC (Cisco Capital) 84.04 plus 18.94. Total long-term 16,005.28 (derived) vs 7,829.91.
- Current: cash credit 5,366.23 (FY25 3,957.64); bill discounting 3,200.05 (nil); working capital demand loan 30,309.00 (18,078.23); buyer's credit 8,783.03 (4,316.97); current maturities 3,307.47. Total 50,984.72 vs 28,987.73, +75.9% (derived). Director loan nil (FY25 655.00, interest-free).
- Total borrowings per financing table 63,663.58 (FY25 34,837.75). Trade credits from banks 6,577.63 (8,120.50). (Note 6D, p.190; Note 11C, p.203)
- Rates: term loans linked to 3-month T-bill plus 2.96% to 3.39% (8.34% to 8.77%), repo plus 3.25% to 3.70% (8.5% to 8.95%), MCLR plus 1%, LTLR minus 9.80% (6.96%). Working-capital facilities 4.08% to 10.75% (FY25 3.36% to 11.75%). Largely floating. 0.50% rate move = 141.72 PBT (FY25 90.72). (Note 11A, pp.198-199; Note 36, p.238)
- Security: first pari-passu on piping unit fixed and current assets, Palwal land and buildings, Abohar 8 MW net block, new Anjar (Kutch) and Numaligarh-linked project assets, a fixed deposit of 350, second charge on CMD's Faridabad house; personal guarantees of promoters; corporate guarantee of DDE Piping Components Pvt Ltd. (Note 11A(i)-(b), pp.199-200)
- Covenants: security cover and debt-equity; "satisfied all"; no default; no waivers disclosed. 🟢 (Note 11A ii-iii, p.200)
- Maturity (undiscounted): under 12 months 59,870.60; 1-5 yrs 13,241.34; over 5 yrs 1,067.48. About 21% of long-term borrowings mature within a year. (Note 36, pp.241-242)
- Undrawn facilities 1,304.77 (FY25 4,964.13), -73.7% (derived). Cash and equivalents 1,588.57. (Note 6D, p.189) 🔴 for liquidity headroom
- Gearing: net debt/(equity + net debt) 41.89% vs 30.63%. Debt-equity 0.72 vs 0.42. Current ratio 1.28 vs 1.39. DSCR 2.18 vs 1.78. (Note 37, p.243; Note 41, p.247) 🟡
- Finance cost 5,266.41 vs 3,498.70, +50.5% (derived). Finance cost includes 291.01 exchange difference treated as borrowing cost (FY25 105.00) while FX gain 594.00 sits in other income. (Note 26, p.215; Note 20, p.211) 🟡
- Derived interest cover: (PBT 7,235.45 + finance cost 5,266.41) / 5,266.41 = 2.37x.
- Related-party borrowing: director loan repaid in full; consolidated shows directors' interest-free loans 736.14 (FY25 1,330.55). (Cons. Note 9B, p.305)
- Supplier finance: settlement 60-90 days vs supplier terms 30-75 days. Consolidated note describes the scheme and says terms were not renegotiated. (Note 11C, p.203; Cons. Note 15, p.313) 🟡

## 8. Trade payables (standalone, INR lacs; Note 18, pp.207-208)

- Total 7,863.20 vs 14,218.39, -44.7% (derived). MSME 314.93 (468.54). No interest due on MSME arrears. 🟢
- Ageing FY26: unbilled 1,242.44; not due 4,688.20; under 1 yr overdue 1,870.55; 1-2 yrs 28.61; 2-3 yrs 0.46; over 3 yrs 32.95. FY25: not due 468.54; under 1 yr 12,904.65; unbilled 754.59. The FY25 column pushed almost everything into "overdue under 1 year"; FY26 into "not due". The notes do not explain the reclassification basis. 🟡
- Acceptances (LC-backed) 257.70 (FY25 1,360.67). Related-party payables 27.75. Terms 0 to 75 days. 
- Payable days on revenue (derived): 31.2 vs 81.2. Cash flow shows trade payables decreased 6,896.73 (FY25 3,412.19). With trade credits 6,577.63 and buyer's credit 8,783.03 (current borrowings), supplier funding moved from payables into bank-financed lines. 🟡

## 9. Provisions (standalone, INR lacs; Notes 14 and 30)

- Gratuity: funded through LIC trust, plan assets 100% LIC. DBO 1,297.21 (FY25 1,173.30), assets 1,048.07 (920.46), net liability 249.14 (252.84). Funded ratio 80.8% (derived).
- Assumptions: discount rate 7.32% (6.99%), salary escalation 8.00% (8.00%), attrition 3%/2%/1% by age band, mortality IALM 2012-14, duration 16.97 yrs. Sensitivity: -0.5% discount rate adds 82.03. (Note 30, pp.219-222) 🟢
- Past service cost 116.10 sits in the DBO roll-forward but not in the service plus net interest expense of 150.89 (which equals 136.35 + 14.54). Note 39 puts the labour-code charge at 119.23 and the segment note says employee expense includes it. Three figures (116.10, 119.23, 150.89 base) do not tie. (Note 30 p.220; Note 39 p.246; Note 33 p.231) 🟡
- Compensated absences 197.23 (FY25 354.12), -44.3% (derived), no explanation. 🟡
- Litigation provision 188.21 (91.64); FY25 movement shows "created: -" while P&L and cash flow show 9.49 charged in FY25. Consolidated FY25 movement is 82.15 to 91.64 with 9.49 created. (Note 14, p.204; Cash flow p.160; Cons. Note 11, p.308) 🟡
- Warranty, decommissioning, onerous contracts: NOT FOUND IN DOCUMENT as separate provisions.

## 10. Deferred tax (standalone, INR lacs; Note 17, pp.205-206)

- Tax expense 1,613.67 on PBT 7,235.45: effective 22.3% vs statutory 25.168%; FY25 866.03 on 3,201.17 = 27.05% (derived). Earlier-year adjustment is a credit of 156.90 (FY25 charge 46.76); without it the rate is 24.5% (derived). The credit adds 2.8% to PAT 5,621.78 (derived). 🟡
- Net deferred tax liability 1,559.26 (FY25 1,576.20). DTA on employee benefits 112.34 and leases 424.06. DTL on PPE 2,170.59.
- A deferred tax asset of 348.12 on IPO/due-diligence expenses was credited straight to securities premium and not to P&L (statement of changes in equity p.163; Note 17C p.206; Note 10, p.196). Direct reserve credit. 🟡
- MAT credit: NOT FOUND IN DOCUMENT (none recognised). Unrecognised DTA: NOT FOUND IN DOCUMENT.
- Consolidated reconciliation shows losses utilised (373.06) and tax-rate difference items; consolidated effective rate 19.8% (1,908.18 / 9,624.89, derived). (Cons. Note 14, p.309-310) 🟡

## 11. Revenue details (standalone, INR lacs; Note 19, pp.209-210)

| Line | FY26 | FY25 | YoY (derived) |
|---|---|---|---|
| Finished goods | 71,408.15 | 51,750.00 | +38.0% |
| Traded goods | 1,631.51 | nil | new |
| Electricity | 3,134.89 | 4,206.13 | -25.5% |
| Job work | 15,030.39 | 6,835.68 | +119.9% |
| Erection and design | 127.15 | 300.03 | -57.6% |
| Scrap | 431.48 | 711.77 | -39.4% |
| Export incentive | 91.54 | 83.65 | |
| Total | 91,855.73 | 63,887.26 | +43.8% |

- Geography: India 57,421.78; outside India 34,433.95 (37.5% of revenue; FY25 35.6%, derived).
- Segments: Piping revenue 88,387.84 (FY25 59,662.39); Power 3,467.89 (4,224.87). Piping profit before tax 8,234.78 (2,531.45); Power loss -526.89 (profit 609.38). Power depreciation 381.11 vs 187.51 (+103.3%, derived); explanation NOT FOUND IN DOCUMENT. Power gross profit 1,186.00 vs 2,242.40. (Note 33B, pp.231-232) 🟡
- Contract liabilities (customer advances) 11,433.31 vs 7,150.46, +59.9% (derived), 12.4% of revenue. No contract assets. Remaining performance obligation on erection: nil. Order book / unsatisfied obligation on products: NOT FOUND IN DOCUMENT. (Note 19, pp.209-211) 🟢
- Customers over 10%: Numaligarh Refinery 17,268.79 (18.80%; FY25 2,798.38, 4.38%); Dow Chemical Canada 11,048.38 (12.03%; FY25 74.47). Combined 30.8% (derived). FY25's two 10% customers (GAIL 10.24%, John Zink 10.10%) fell to 4.79% and 0.61%. (Note 33(c), p.234) 🟡
- Consolidated: revenue 114,199.92 (82,736.22); three segments (piping, power, heavy fabrication 8,042.75); Punjab power sales 5,138.78 = 4.50% (FY25 10.09%). (Cons. Note 16 p.314; Cons. Note 31, pp.333-336)

## 12. Other critical notes

- Exceptional items: none. Other income 1,374.70 (1,602.87) = 19.0% of PBT (derived): FX gain 594.00 (8.2% of PBT), interest from related parties 330.76, bank interest 341.94, written-back balances 87.06. (Note 20, p.211) 🟡
- Cost lines: raw material consumed 43,409.51 (25,958.30); change in inventory -1,786.71 (+446.06). Employee cost 13,637.06 (11,596.60), +17.6%. Other expenses 19,989.87 (17,347.63): selling commission 1,026.19 vs 446.78 (+129.7%), legal and professional 1,169.63 vs 890.90, claims and deductions 202.39 vs 517.11. (Notes 21-25, pp.211-214) 🟡
- Depreciation 3,808.69 (3,441.67), +10.7% while gross PPE rose 55.7% (71,851.27 vs 46,149.94, derived). Building additions 15,529.03; CWIP transfers 24,506.76; CWIP left 7,986.46 (ageing 1-2 yrs 2,339.42, 2-3 yrs 511.69). Depreciation will step up. (Note 3, pp.181-182; Note 24, p.212) 🟡
- Capex funding: purchase of PPE and CWIP 16,374.53 (cash flow). Capital advances 1,337.92 (4,130.39). (Cash flow p.160; Note 7, p.192)
- Operating cash flow: profit before working capital changes 15,260.20; receivables -13,520.24; payables -6,896.73; other assets -2,592.38; other liabilities +4,274.65; cash used in operations -2,851.50; tax paid -1,598.53; net operating -4,450.03 (FY25 -15,428.58). Investing -16,153.19. Financing +21,632.09: long-term borrowings +10,376.40, short-term +20,650.47. Consolidated operating cash flow +1,954.84 (FY25 -11,845.73). (Cash flow pp.160-161; Cons. cash flow p.264) 🔴
- Goodwill (consolidated): 873.74 (271.18 + 602.56 Molsieve). (Cons. Note 3A, p.290)
- EPS: basic 8.13 (3.58), diluted 8.11 (3.56); dilution from options 1,20,733 shares (0.17% of 6,91,70,090, derived). (Note 28, pp.215-216) 🟢
- ESOP-2023: expense 117.46 (308.16); options outstanding 1.25 lakh (3.64); exercised 2.09 lakh at exercise price Rs 10; ESOP reserve 246.24 after transferring 488.95 to securities premium. Fair value per option 233.47 in both years. (Note 42, pp.248-249; Note 10, p.196) 🟢
- Share capital: 692.63 lakh shares, 6,926.34. 2.09 lakh shares issued on ESOP exercise. No other change. Promoter holding 70.17% (70.29%); K.L. Bansal 50.82%. Pledged shares: NOT FOUND IN DOCUMENT. (Note 9, pp.193-195)
- Direct reserve movements bypassing P&L: DTA on IPO expense 348.12 to securities premium; ESOP transfer 488.95. OCI gain on gratuity 181.64 after tax. (SOCE p.162; Note 10 p.196)
- Capital management and covenants: see Section 7.
- FX: unhedged exposure. Buyer's credit USD 94.38 lakh = 8,933.14; loan to Thailand USD 38.36 lakh = 3,630.51; interest receivable USD 30.58 lakh = 2,894.76. 5% move on buyer's credit = 446.66 PBT. Forward contracts are not hedge-designated; fair value liability 303.43 (FY25 asset 10.99). (Note 36, pp.239-240; Note 12, p.203) 🟡
- CSR: required 54.42 = spent 54.42 (FY25 43.84). No shortfall. (Note 25(b), p.214) 🟢
- Auditor fees 100.68 (82.11), of which statutory audit 80.50, reimbursements 18.18 (6.36). (Note 25(a), p.214) 🟢
- Audit trail and books: three accounting software. In one application audit trail not enabled for certain master data (database layer from 5 Jun 2025); second application audit trail not enabled; third not enabled for certain master data. One software backed up not daily. Consolidated adds a subsidiary application with no database-level log. (Note 44-45, pp.250-251; Cons. Notes 42-43, p.350) 🟡
- Segment reporting: standalone two segments, consolidated three. (Note 33, p.230; Cons. Note 31, p.332)
- Events after the balance sheet date: no dedicated note. EPS note states no share transactions after the reporting date. NOT FOUND IN DOCUMENT as a separate disclosure. (Note 28, p.216)
- Going concern: none in the notes except Note 2.1 stating preparation on a going-concern basis (p.164). Consolidated Note 45(b) states MPPL "operational viability" and cash flows are uncertain (p.351). Group-level doubt: none stated.
- Ratios (Note 41, p.247): ROCE 9.25% (6.50%); ROE 6.57% (3.54%); net margin 6.12% (3.66%). Explanations in the ratio note read backwards in two places: inventory turnover up 36.0% "due to increase in inventories", and debt-equity up 69.8% "due to increase in shareholder equity". 🟡 disclosure quality.
- Regrouping of prior year: Note 47 says figures were regrouped or reclassified "wherever considered necessary" with no amounts. (Note 47, p.251) 🟡 (see also payables ageing in Section 8)
- Labour code: standalone 119.23, consolidated 194.44 past service cost taken to P&L. (Note 39, p.246; Cons. Note 40, p.349) 🟡

## PASS 1 SUMMARY: top 10 findings by investor importance

| # | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | Consolidated QUALIFIED opinion: Malwa Power assets 4,761.67 cannot be tested for impairment after the PPA expired 27 Apr 2025 (tariff Rs 8.59 to Rs 5.22). MPPL FY26 loss 555.04. Standalone exposure: investment 959.01, loan 151.00, guarantee 527.04 (2,300.00 given in year), receivable 310.05. | Cons. auditor report p.253; Cons. Note 45(b) p.351; Note 5 p.184; Note 31 p.225 | 🔴 |
| 2 | Abohar excess-revenue payable 1,384.96 unprovided (19.1% of PBT), High Court stay, auditor EoM. Not in the contingent-liability table. Standalone and consolidated texts state different tariffs and amounts. | Note 46 p.251; Cons. Note 45(a) p.350; Note 32B p.229 | 🔴 |
| 3 | Receivables 34,304.28 (+68.9%) plus 15,938.75 sold (3.8x); over-6-month share 9.2% vs 5.3%; nil ECL; 8 customers hold 71% (FY25 33%). Statement that business is "majorly cash based" conflicts. | Note 6A pp.186-187; Note 36 p.241 | 🔴 |
| 4 | Operating cash flow -4,450.03 (FY25 -15,428.58) funded by debt: current borrowings 50,984.72 (+75.9%), gearing 41.89%, finance cost +50.5%, undrawn lines down to 1,304.77 from 4,964.13. | Cash flow pp.160-161; Note 11B p.200; Note 37 p.243; Note 6D p.189 | 🔴 |
| 5 | Thailand subsidiary: total exposure 16,476.57 (18.6% of net worth), interest receivable 2,894.76 accrued and rising, interest income halved, no impairment, Level 3 DCF. | Note 5 p.185; Note 31C p.225; Note 35 p.236 | 🟡 |
| 6 | Customer concentration shift: Numaligarh 18.80% and Dow Canada 12.03% of revenue, both near zero or 4% a year earlier. | Note 33(c) p.234 | 🟡 |
| 7 | Contingent liabilities: export obligation 20,237.29 (2.0x; 22.8% of net worth), customs bond 1,759.76 (2.0x), customs demand 1,120.09 described in a note but not in the table, FEMA notice open. | Note 32B pp.229-230 | 🟡 |
| 8 | Bank stock-statement gaps: receivables 1,303.20, inventory 519.91 at Mar-26. Consolidated "books" figures do not equal the consolidated balance sheet (gaps 2,068.42 and 4,996.98). | Note 11B pp.201-202; Cons. Note 9B p.306 | 🟡 |
| 9 | Related-party pattern: consolidated related-party payables 763.89 (Shikha Bansal 762.90) vs 27.75 standalone; new advances to directors 37.15; promoter security and guarantees on bank debt; 99.8% of CSR to the promoter foundation. | Cons. Note 29C p.329; Note 31C p.225; Note 25(b) p.214 | 🟡 |
| 10 | Accounting controls: audit trail not enabled on two of three applications (in part), no daily backup on one; gratuity past service cost figures (116.10, 119.23) do not tie; tax-rate help of 156.90 prior-year credit and 348.12 DTA taken straight to reserves. | Notes 44-45 pp.250-251; Note 30 p.220; Note 39 p.246; Note 17 p.205-206 | 🟡 |

## Coverage (what Pass 1 did and did not read)

Read in full: standalone cash flow statement and changes in equity (pp.160-163); Notes 1-2.2(m start) pp.164-171; Notes 3-47 pp.181-251. Consolidated: Notes 3 (PPE, goodwill), 4, 6, 9, 11-16, 27, 28 (first lines), 29, 30, 31, 38-46, selected tables of 7-8 and the cash flow.
Not read line by line in Pass 1: standalone Note 2.2(m) end to 2.2(z) policy text (text lines 11460-12285, about 800 lines; ECL/policy terms located by search); consolidated Note 2 policies; consolidated Notes 17-26, 32-37 detail beyond the tables quoted; consolidated deferred tax movement table; consolidated ESOP/EPS/fair value. Pass 2 should take these first.
Nothing in this report is estimated. Each "NOT FOUND IN DOCUMENT" is an absence in the notes read.
