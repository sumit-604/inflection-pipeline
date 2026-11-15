# STAGE 2 NOTES, PASS 1 (FULL EXTRACTION): INVPRECQ, run 2026-11-15

Source: runs/invprecq-2026-11-15/inputs/annual-report/Annual_Report_FY2025-26.txt (called AR below). All figures in Rs lakh ("Rs in Lacs", AR face) unless stated. Nothing converted.

Anchor convention. In the AR text copy the "[page N]" marker closes a page. Anchors use the page whose content ends at that marker. Notes appear twice in the AR: STANDALONE (Notes 1 to 44, pp.112-138, auditor Park & Company, report 19-May-2026) and CONSOLIDATED (Notes 1 to 45, pp.148-176). Standalone note numbers are used unless the finding says "Cons". Where the two sets match, only the standalone is cited.

Page checks. I did not open the PDF. Every figure below was cross-footed against a second line of the AR (marked "foots"). OCR-type garbling found in the AR itself is listed under "Disclosure defects".

---

## 0. LOAD-BEARING FACTS (first priority)

| # | Fact | Result | Evidence |
|---|---|---|---|
| 1 | H1 FY27 cash conversion, WIP absorption, 245 vs 133 day cycle | PARTLY REACHABLE. H1 FY27 figures are not in the AR (NOT REACHABLE). FY26 baseline reported below. | See 0.1 |
| 2 | A&D share 6% FY26 to 11% H1 FY27; HAL, MKU, "monthly supply" | FY26 6% CONFIRMED. H1 FY27 11%, HAL, MKU, monthly supply NOT REACHABLE from the AR notes. | See 0.2 |
| 3 | Rs 100 Cr capex vs TNW, funding, timeline | NOT REACHABLE. The Notes carry no capital commitment, no events-after-date note, no approval of Rs 100 Cr. TNW figure reported. | See 0.3 |
| 4 | FY26 revenue base mismatch | RECONCILED to the AR. Each rival figure maps to a named AR line. | See 0.4 |

### 0.1 Cash conversion, FY26 baseline (AR only)
- CFO Rs 2,577.89 lakh against PAT 1,176.62 (standalone cash flow; AR p.111). That is 2.19x PAT. Cons CFO 2,577.88 (Cons cash flow, p.147).
- Operating profit before WC changes 3,043.80; WC changes net (103.34); tax paid (362.57). Foots: 3,043.80 - 103.34 - 362.57 = 2,577.89 (p.111). The printed line label "Cash generated from operations (103.34)" is the WC subtotal, not cash generated (label defect).
- Capex cash 2,403.28 (p.111). Foots to Note 2: additions 2,321.64 + CWIP rise (142.46 - 60.82 = 81.64) = 2,403.28 (Note 2, p.117). Free cash flow after capex = 2,577.89 - 2,403.28 = 174.61 (derived).
- Inventory rose 298.03 (CF p.111; foots Note 10: 5,170.18 - 4,872.15). WIP +289.53 (2,677.48 vs 2,387.95, +12.1%); finished goods -176.07 (531.97 vs 708.04, -24.9%); stores +209.91 (+18.5%); raw material -25.34 (Note 10, p.121).
- Change in inventories credit (P&L) is Rs 113.46 lakh in FY26 against 141.12 in FY25 (Note 26, p.128). So FY26 absorbed less FG/WIP credit than FY25. The Q2 FY27 credit of Rs 6.04 Cr named in the brief is not in this AR. NOT REACHABLE.
- AR's own working-capital days (Note 39 ratios, p.137): inventory 99.42 days (FY25 108.75); receivables 80.09 (87.63); payables 77.90 (77.60). Foots: avg inventory 5,021.17 / product sales 18,434.29 x 365 = 99.42; avg receivables 4,044.78 / 18,434.29 x 365 = 80.09. Note the inventory ratio is on sales, not cost.
- 245 days (screener) vs 133 days (CARE): neither is in the AR. Derived cross-check on closing balances, crude: cost of sales proxy = materials 5,216.05 - 113.46 + manufacturing expenses 8,400.54 + employee 1,221.75 = 14,724.88. Inventory 128.2 days; receivables 76.1 days (on revenue 18,844.62); payables 69.9 days. Cycle about 134 days. This sits near CARE's 133 and far from 245. It is my arithmetic on AR lines, not a disclosed figure.

### 0.2 A&D share
- Revenue by industry division (Cons Note 38, p.174): Auto 11,835.19 (FY25 9,761.72, +21.2%); Non auto 5,617.90 (5,954.10, -5.7%); Aerospace and Defence 1,086.42 (539.01, +101.6%); total 18,539.51 (16,254.83). Foots to the rupee. A&D = 5.86% of 18,539.51 (FY25 3.32%). The 64/30/6 FY26 mix in the presentation reproduces: 63.84% / 30.30% / 5.86%.
- The total 18,539.51 is 305.11 below revenue from operations 18,844.62. The gap equals energy credits 265.54 + export incentives 39.57 (Note 23, p.127). Foots.
- The Notes name no customer, no programme, no HAL, no MKU, no supply cadence. NOT FOUND IN DOCUMENT.

### 0.3 Capex and TNW
- Standalone equity 10,278.09 (BS p.108). Less intangibles 25.66 (Note 4, p.119) gives tangible net worth 10,252.43 (derived). Cons equity 10,260.99 (Cons BS, p.145).
- Rs 100 Cr = 10,000 lakh = 97.3% of standalone equity (derived). Total debt 7,009.87 (Note 34, p.133); lease liabilities 148.88 (Note 5, p.120).
- Capital commitments: NOT FOUND IN DOCUMENT. Events after the balance sheet date: NOT FOUND IN DOCUMENT in the Notes. The Board report states "no material changes and commitments" up to the report date (Board report item 28, line 3187, AR p.58 region; anchor by marker: before [page 60]).
- CWIP at 31-Mar-2026 is only 142.46 (Note 2, p.117).

### 0.4 Revenue base, FY26 (Rs lakh)
| Figure in brief | AR line | Anchor |
|---|---|---|
| 185.79 Cr (P&L slide) | 18,579.08 = product sales 18,434.29 + job work 105.22 + export incentives 39.57. This is "Investment Castings" segment external revenue, so it EXCLUDES wind energy credits 265.54 | Note 23 p.127; Cons Note 38 p.173 |
| 188 Cr (screener) / 188.45 | 18,844.62 revenue from operations (net) | P&L p.109; Note 23 p.127 |
| 189.7 Cr (five-year slide) | 18,968.21 = TOTAL INCOME (revenue 18,844.62 + other income 123.59) | P&L p.109 |
| 189.20 Cr (CARE TOI) | NOT reproduced by any AR line. CARE is not an AR source. | not reachable |
Consolidated revenue is identical to standalone (18,844.62; Cons P&L p.146). Q2 FY27 57.95 vs 58.00: not reachable here.
Base-year fact for projection: audited FY26 revenue from operations is Rs 18,844.62 lakh (Rs 188.45 Cr), prior year 16,507.37 (+14.16%). Foots.

---

## 1. ACCOUNTING POLICIES AND CHANGES

- Basis: Ind AS, historical cost, accrual and going concern basis (Note 1.1, p.112). Accounts approved 19-May-2026 (p.112). 🟢
- No policy change with a quantified P&L effect is disclosed. New-standard adoption disclosure: NOT FOUND IN DOCUMENT. 🟢
- Depreciation: straight line on Schedule II lives. Buildings 60/30 yrs, Plant and equipment 10/15/8 yrs, Dies and tools 10, Office equipment 3/5, Furniture 10, Vehicles 10, Leasehold land 99 (Note 1.2 c(v), p.113). No change in lives disclosed. 🟡 see Pass 1 item below on low plant rate.
  - Plant depreciation 620.55 on gross plant 12,026.20 (opening) rising to 13,900.57 (Note 2, p.117) is 4.8% on average gross 12,963.39 (derived). That implies a life of about 21 years against the stated 8 to 15. Fully depreciated plant stays in gross cost (accumulated depreciation 8,193.24 = 58.9% of gross). The Notes do not disclose fully depreciated cost or residual value. Reason unknown. 🟡
  - Total depreciation 851.90 vs 812.80, +4.8%, while gross block grew 2,321.64 (+12.8%) (Note 29, p.128; Note 2). Most additions came late (see item on solar). 🟡
- Capitalisation threshold: NOT FOUND IN DOCUMENT. Borrowing cost capitalised on qualifying assets per policy (Note 1.2 o, p.115); amount capitalised in FY26: NOT FOUND IN DOCUMENT.
- Intangibles: software and technical know-how at cost, amortised "over a useful period of life", life not stated (Note 1.2 c(vi), p.113). 🟡 minor.
- Impairment: assets tested on indication; no assumptions (growth, discount rate) disclosed. No goodwill. NOT FOUND IN DOCUMENT (Note 1.2 r, p.116; c(ix), p.113). 🟢 given no goodwill.
- ECL: simplified approach, lifetime ECL, "provision matrix" named; matrix rates NOT FOUND IN DOCUMENT (Note 1.2 d(ii), pp.113-114; Note 33 A, p.131). FY26 loss allowance Nil against 57.29 (Note 11, p.121). 🟡
- Revenue recognition: domestic sales "on dispatch from point of sale corresponding to transfer of significant risks and rewards"; exports on mate's receipt/shipped on board (Note 1.2 l(ii), p.115). The key audit matter says control passes "mainly upon delivery" (Independent Auditor's report, Cons KAM, p.139). Dispatch versus delivery is a cut-off question for a business with 1-to-2 day transit. Policy is risks-and-rewards, not the Ind AS 115 control wording. 🟡
- Inventory: raw materials and stores at weighted average cost; FG and WIP at material cost plus direct expenses and "appropriate value of overheads", lower of cost and NRV; obsolete and slow-moving written off or valued at NRV "as per policy" (Note 1.2 e, p.114). Overhead absorption rate not disclosed. Write-down amount: NOT FOUND IN DOCUMENT. 🟡
- Leases (Ind AS 116): ROU and liability recognised; discount rate NOT FOUND IN DOCUMENT; lease term NOT FOUND IN DOCUMENT. FY26 is the first year a lease liability exists (opening Nil). ROU 190.34 (FY25 46.65); lease liability 148.88 (Nil) (Note 5, pp.119-120). Foots: 161.74 + 11.14 - 24.00 = 148.88. 🟡
- Deferred tax: balance sheet approach; DTA only if probable (Note 1.2 p, pp.115-116). 🟢
- EPS: standard basic and diluted wording (Note 1.2 s, p.116). 🟢
- Segment: the standalone says segment disclosure is in the consolidated statements (Note 1.2 t, p.116). See Segment item below.
- Operating cycle: 12 months stated, "based on the project period" (Note 1.1, p.112). 🟢
- Estimates: no sensitivity or key-judgement note beyond generic wording (Note 1.2 b, p.112). 🟡 minor.

## 2. RELATED PARTY TRANSACTIONS (standalone Note 38, pp.135-136; Cons Note 37, pp.171-173 identical except no subsidiary)

Related parties: Subsidiary I&PCL Vacuum Cast Ltd (wholly owned, India). "Associates" as labelled by the company: Tamboli Foundry Supplies and Services Ltd, Shri Tamboli Foundation, Meche Private Ltd (also promoter shareholder, 16.19%, Note 15, p.124), Piyush I Tamboli HUF. KMP and relatives: Piyush I Tamboli (CMD), B. Pratapkumar (WTD), Vishakha P Tamboli, Jainam P Tamboli (WTD and CFO), independent directors (Akshay Shah w.e.f. 22-May-2025; Mamtadevi L Raol up to 12-Jan-2026; Saurabh Poddar; Pankaj Bhayani; Jatan Shah; Ashwini Doshi), Kavya P Tamboli (relative), Hetal Kapadia (CS). New this year: Akshay Shah (director from 22-May-2025). No new corporate related party.

Transactions, Rs lakh:
| Party | Relationship | Nature | FY26 | FY25 | YoY |
|---|---|---|---|---|---|
| Meche Pvt Ltd | Promoter-group company, 16.19% holder | Purchase of materials and services | 319.88 | 254.93 | +25.5% |
| Shri Tamboli Foundation | Associate (promoter trust) | CSR | 13.86 | 17.56 | -21.1% |
| Piyush I Tamboli HUF | Promoter HUF, 9.66% holder | Rent | 24.00 | 20.00 | +20.0% |
| Piyush I Tamboli | CMD | Remuneration | 347.11 | 229.54 | +51.2% |
| Jainam P Tamboli | WTD and CFO | Remuneration | 46.28 | 27.44 | +68.7% |
| B. Pratapkumar | WTD | Remuneration | 32.00 | 32.55 | -1.7% |
| Hetal Kapadia | CS | Remuneration | 2.40 | 2.40 | 0.0% |
| Piyush I Tamboli | CMD | Guarantee commission | 84.52 | 71.42 | +18.3% |
| Directors (7) | Sitting fees | | 8.87 | 6.33 | +40.1% |
| Kavya P Tamboli | Relative | Salary | 6.00 | 5.00 | +20.0% |
| Subsidiary | | Advance (received back) | (0.92) | (1.87) | |
Sum of flows above excluding the subsidiary advance: 884.92 (FY25 667.17), +32.6%. As % of revenue from operations: 4.70% (FY25 4.04%). Derived; remuneration total 427.79 foots (347.11 + 46.28 + 32.00 + 2.40).

Outstanding balances (31-Mar-2026, FY25 same unless shown):
- Tamboli Foundry Supplies and Services Ltd: capital advance 306.00 (306.00); trade receivables 3.81 (3.81). Both unchanged for a year.
- Meche: security deposit given 100.00 (100.00); trade advances to suppliers 49.75 (61.11).
- Piyush I Tamboli HUF: trade payables 1.80 (1.80).
- Subsidiary: trade payable 6.49 (7.41).
- KMP trade payables 25.15 (19.27): Piyush 19.65, Jainam 5.00, Kavya 0.50.

Findings:
- Directors' remuneration (Note 27, p.128) 425.39 vs 289.53, +46.9%. Foots: 347.11 + 46.28 + 32.00 = 425.39. Profit before exceptional tax rose 107.9% (1,743.49 vs 838.60). The Board report (item at line 4160, AR p.76) gives CMD pay +41.10% and Jainam +50.27%, Pratapkumar +7.00%; Note 38 gives +51.2%, +68.7%, -1.7%. The two do not agree. Basis of the Board table not stated. Median employee increase 7% (p.76). 🟡
- Promoter-family cash take (derived): Piyush + Jainam remuneration 393.39 + guarantee commission 84.52 + HUF rent 24.00 + Kavya salary 6.00 = 507.91 = 29.1% of profit before exceptional and tax. Proposed dividend 100.00 in total; promoter share at 51.97% is about 51.97 (derived; Note 34, p.133; Note 15, p.124). 🟡
- Guarantee commission 84.52 is 1.26% of average total debt (6,729.71; derived) for a personal guarantee on bank facilities (Note 17 text, p.126). Where it is booked (Note 28 "Other borrowing cost" 99.86 is the likely line) is not stated. 🟡
- Rent to the HUF 24.00 and lease payments of 24.00 in the Ind AS 116 table (Note 5, p.120) match; ROU building addition 161.74 is the first lease. Whether it is the HUF lease is an INFERENCE; the Notes do not say.
- Capital advance 306.00 is "towards purchase of property from a company in which some of the directors are interested" (Note 9, p.121). It is the same amount in both years. No completion date. Total capital advances 672.55 (FY25 654.85); the other 366.55 has no stated payee. 🟡
- Security deposit 100.00 "towards factory shed to a company in which some of the directors are interested" (Note 8, p.121); Meche is the only party with a 100.00 deposit in Note 38. No rent to Meche appears in the RPT table. Why a deposit with no rent flow: NOT FOUND IN DOCUMENT. 🟡
- Non-arm's-length test (comparable price, board approval): NOT FOUND IN DOCUMENT. The CARO statement says RPTs comply with Sections 177 and 188 (CARO item 13, p.104). 🟡
- Loans to promoter entities: none. Loans are to employees (12.75 total) and others (47.43): Note 7 p.120 (employees 7.13 + 5.62; others 32.47 + 14.96; total 60.18). CARO: granted 56.88, balance 60.18 (CARO 3(a), AR text before [page 103]). Foots. 🟢
- Meche purchases are 6.2% of raw-material purchases 5,190.71 (Note 25, p.127), though Meche supplies "materials and services" so the base is loose (derived). 🟡
- CSR: 100% of CSR (13.86) goes to the promoter-linked trust (Note 30 CSR block, p.129). Name differs: "Shri Tamboli Foundation" (Note 38) vs "Tamboli Foundation Trust" (Note 30). 🟡 minor.
- Subsidiary: see Section 6.

## 3. CONTINGENT LIABILITIES (Note 35, p.133)
| Item | FY26 | FY25 | Stage |
|---|---|---|---|
| VAT liabilities | 11.94 | 11.94 | stage not stated in Note |
| GST liabilities | Nil | 19.61 | cleared or dropped, not explained |
- Total 11.94 vs 31.55. 0.12% of standalone net worth 10,278.09 (derived). No single item above 10%. 🟢
- CARO 7(b) lists VAT 8.95 for FY2002-03, before the Commissioner of Gujarat Commercial Tax (CARO 7(b), p.104). 11.94 vs 8.95 gap of 2.99 unexplained. 🟡 minor.
- Company assessment (remote or possible): NOT FOUND IN DOCUMENT. Guarantees for the subsidiary: none disclosed. Bank guarantee amounts: NOT FOUND IN DOCUMENT, though term deposits are "under lien for guarantee and towards margin money" (35.22 non-current, Note 8, p.121; 164.91 other bank balances, Note 13, p.122).
- Income-tax dispute: none disclosed. 🟢

## 4. TRADE RECEIVABLES (Note 11, pp.121-122)
- Gross and net 3,931.23 (FY25 4,158.33), all "undisputed, considered good". FY25 also had 57.29 credit impaired and a matching allowance. FY26 allowance Nil. Allowance movement table: NOT FOUND IN DOCUMENT. Where 57.29 went (write-off against receivable?) is not stated; cash flow adds back sundry written off 12.96 only (p.111). 🟡
- Ageing 31-Mar-2026: not due 3,453.95 (87.9%); under 6 months past due 471.45 (12.0%); 6-12 months 5.83 (0.15%); over 1 year Nil. Foots to 3,931.23.
- Ageing 31-Mar-2025: not due 3,062.25 (72.6% of 4,215.62 gross); under 6 months 1,021.28; 6-12 months 74.80; 1-2 yrs 38.96; 2-3 yrs 18.33. Over 6 months past due 132.09 (3.13%).
- Over 6 months FY26: 5.83 = 0.15% of total, against 3.13% a year ago. 🟢
- Receivable days (Note 39 ratio, p.137): 80.09 vs 87.63. Only two years are in the AR Notes. Third year: NOT FOUND IN DOCUMENT. 🟢 improving.
- Receivables fell 5.5% (3,931.23 vs 4,158.33) while revenue rose 14.2%. Factoring or bill discounting: NOT FOUND IN DOCUMENT. Note 30 shows "Bank discount, commission and other charges" 13.35 (12.72), small (p.129). 🟡 to ask.
- Single customer above 10%: NOT FOUND IN DOCUMENT in the Notes. Related-party receivables: 3.81 (Tamboli Foundry), Note 38 p.136. 🟢
- Foreign currency receivables unhedged: USD 3.33, EUR 0.66 (Note 33, p.132); see Section 12.
- Note 33 text says maximum credit exposure "represents trade receivables, work in progress and other receivables" (p.131): WIP is not a financial asset. Wording defect.

## 5. INVENTORY (Note 10, p.121; Note 26, p.128)
| Category | 31-Mar-26 | 31-Mar-25 | Change |
|---|---|---|---|
| Stores and spares | 1,347.41 | 1,137.50 | +18.5% |
| Raw materials | 613.32 | 638.66 | -4.0% |
| Finished goods | 531.97 | 708.04 | -24.9% |
| Work-in-progress | 2,677.48 | 2,387.95 | +12.1% |
| Total | 5,170.18 | 4,872.15 | +6.1% |
Foots. Revenue +14.2%. FG fell; WIP grew 12.1%, below revenue. Stores and spares 26.1% of inventory (1,347.41/5,170.18); stores consumed in P&L 722.54 (Note 30, p.129), so stores on hand equal 1.9 years of consumption at the FY26 rate (derived). 🟡 Note 1.2 c(vii) says stores that meet PPE definition are capitalised (p.113); whether the 1,347.41 holds slow stock: NOT FOUND IN DOCUMENT.
- Write-downs: NOT FOUND IN DOCUMENT. Obsolete stock disclosure: NOT FOUND IN DOCUMENT beyond policy.
- Inventory days 99.42 vs 108.75 (Note 39, p.137), basis sales. Three-year trend: NOT FOUND IN DOCUMENT.
- Closing stock change in P&L: WIP +289.53, FG -176.07, net +113.46 credit (Note 26). Foots.
- Inventory is pledged (Note 17 text, p.126).

## 6. INVESTMENTS
- Single holding: 250,000 equity shares of I&PCL Vacuum Cast Ltd, face Rs 10, 100% owned, carrying 25.00 at cost, unquoted (Note 6, p.120). No impairment recorded.
- Consolidated: subsidiary net assets 7.90 (0.08% of group), share in profit (0.47) (Cons Note 39, p.174). Net assets 7.90 vs cost 25.00 means 17.10 of accumulated losses (derived). The standalone carries 25.00 with no impairment although its own policy tests for impairment (Note 1.2 d(i), p.113). Brief says the unit is dormant (not from AR). 🟡 low in size, but an unrecorded impairment indicator.
- ICDs and loans to related parties: none. Loans in Section 2. Other investments with unrealised gains: none; no FVTPL or FVOCI assets (Note 32, p.130). 🟢
- Joint ventures: none. CARO 9(e): no associate or JV.

## 7. BORROWINGS (Note 17, pp.125-126; Note 33, pp.131-132; Note 34, p.133)
| Instrument | 31-Mar-26 | 31-Mar-25 |
|---|---|---|
| Term loans from banks (non-current) | 1,617.00 | 545.82 |
| Hire purchase finance (non-current) | 81.82 | 98.83 |
| Non-current total | 1,698.82 | 644.65 |
| Working capital finance from banks | 4,808.99 | 5,166.55 |
| Current maturities of long-term debt | 502.06 | 638.35 |
| Current total | 5,311.05 | 5,804.90 |
| Total borrowings | 7,009.87 | 6,449.55 |
Foots. Net rise 560.32 = proceeds 1,054.17 - repayments 493.85 (CF p.111). Foots.
- Short-term share 75.8% (5,311.05/7,009.87; derived). Working capital finance alone 68.6%.
- Security: equitable mortgage of land and buildings; hypothecation of plant and equipment, inventories, book debts, fixed deposits; personal guarantee of one director. Hire purchase against vehicles (Note 17 text, p.126). Unsecured: Nil. 🟡
- Interest rate per instrument, lender names, maturity dates, covenants, covenant breaches or waivers, term changes: NOT FOUND IN DOCUMENT. 5-year repayment schedule: NOT FOUND IN DOCUMENT; the liquidity table shows the 1,698.82 non-current as one block "more than one year" (Note 33, p.131). 🟡
- Fixed vs floating: text says "balanced portfolio of fixed and variable" (Note 33(a), p.131). The sensitivity of 70.10 for 100 bps (FY25 64.50) implies a floating base of 7,010 (FY25 6,450), the whole debt (Note 33(b), p.132). Derived. Hire purchase of 81.82 would normally be fixed. 🟡
- Bank finance cost 477.84 on average debt 6,729.71 = 7.10% (derived, Note 28, p.128). Total finance cost 617.97 vs 672.38 (-8.1%).
- Related-party borrowings: none. Wilful defaulter: no (Note 39 E, p.137). Charges not registered: none (Note 39 M, p.138). Borrowings used for stated purpose (Note 39 L, p.138; CARO 9, p.104). 🟢
- Total debt to equity 0.68 (0.71) (Note 34, p.133). Lease liability of 148.88 is outside "total debt".
- DSCR 2.36 vs 1.59 (Note 39 A3, p.137). 🟢

## 8. TRADE PAYABLES (Note 22, pp.126-127; Note 37, pp.134-135)
- Total 2,821.07 (2,737.68). MSE 997.30 (1,269.00); others 1,823.77 (1,468.68) (Note 22, p.126).
- Ageing FY26: not due 1,814.13; under 1 year past due 966.27; 1-2 yrs 40.68. MSE: not due 584.11, under 1 year 413.17, 1-2 yrs 0.03. Past due total 1,006.95 = 35.7% of payables (FY25 1,232.41 = 45.0%) (Note 22.1, p.127). Foots.
- MSMED disclosure (Note 37, pp.134-135) shows principal 997.30 and "interest due on above: Nil" under a heading that reads "remaining unpaid... (but within due date as per MSMED Act)". The ageing shows 413.20 of MSE dues past the due date. Items usually disclosed (interest paid beyond the appointed day, interest due and payable for delay, accrued and unpaid interest) are NOT FOUND IN DOCUMENT. The two notes do not agree. 🟡
- Payable days 77.90 vs 77.60 (Note 39, p.137). 🟢 stable.
- Other financial liabilities: "payable towards services received" 183.50 current vs 59.08 (+210%) (Note 18, p.126). Nature (capex creditors?) NOT FOUND IN DOCUMENT. 🟡
- Related-party payables: Section 2.

## 9. PROVISIONS (Note 19, p.126; Note 36, pp.133-134)
- Leave encashment 35.66 + 5.76; gratuity 88.08 + 35.05; bonus 46.43 (43.45). Total 123.74 + 87.24 (75.94 + 76.73). Foots. No warranty, decommissioning, onerous contract or litigation provision, and no movement table: NOT FOUND IN DOCUMENT. 🟢 (no warranty provision disclosed for a built-to-print castings maker; no claims data).
- Gratuity (funded): PV of obligation 266.52 (226.12); plan assets 143.39 (150.19); net 123.13 (75.93). Funded ratio 53.8% (66.4%). Foots to provision 88.08 + 35.05 = 123.13. No employer contribution in FY26 (5.00 in FY25). 🟡
- Gratuity P&L charge 58.93 vs 14.69: past service cost 43.10 (Nil) + current service 9.92 + interest 5.91. Foots. The 43.10 past service cost is the Labour Codes effect on gratuity. The exceptional item is 52.51 (Note 40, p.138). Whether 43.10 is inside the 52.51 or in employee cost is not stated. Gap 9.41 may be leave. INFERENCE only. 🟡
- Assumptions: discount rate 7.16% (6.65%); salary escalation 7.00% (7.00%) (Note 36, p.134). Mortality and attrition rates: NOT FOUND IN DOCUMENT. Sensitivity: discount -1% +13.25, +1% (11.86); salary +1% 12.15 (Note 36, p.134). Expected payments: within 12 months 54.18; 2-5 yrs 133.02; beyond 5 yrs 224.54. 🟢
- OCI label defect: the OCI block labels (10.13) as "return on plan assets" and (1.60) as "obligation" but the movement tables show the 10.13 gain is on the obligation (6.40 + 3.73) and the 1.60 gain is on assets. Total 11.73 foots (p.133-134).
- Employee benefit expense (Note 27, p.128): salaries 667.60 (599.16); directors 425.39 (289.53); PF and other 103.39 (96.11); welfare 25.37 (19.01); total 1,221.75 (1,003.81), +21.7%. Foots.

## 10. DEFERRED TAX AND INCOME TAX (Notes 14, 20, pp.123, 126; P&L p.109)
- P&L tax FY26: current 428.00 + earlier years 7.61 + deferred 78.75 = 514.36 (FY25 165.00 + 0.24 + 66.74 = 231.98). Effective rate 514.36/1,690.98 = 30.4% (derived); statutory rate used 29.12% (27.82% in FY25, "rate under MAT").
- The Note 14 reconciliation starts from PBT 1,690.98: 29.12% = 492.41; expenses not allowed +511.91; income not considered (576.32); net (64.41); lands at 428.00, labelled "income tax expense charged to P&L". It reconciles current tax only, not 514.36. Deferred tax 78.75 and earlier-years 7.61 sit outside it. The "not allowed" figure of 511.91 is 30% of PBT and unexplained. 🟡
- MAT credit utilised: Nil (224.39 in FY25). Remaining MAT credit asset or its timeline: NOT FOUND IN DOCUMENT (no MAT credit asset on the balance sheet, p.108). 🟡 note: the FY25 low cash tax is gone; FY26 current tax is 25.3% of PBT (derived), against 19.7%.
- Deferred tax liability (net) 743.85 (661.69): depreciation 1,051.48 (890.63); section 43B disallowances (307.63) (228.94) (Note 20, p.126). Foots. Rise 82.16 = P&L 78.75 + OCI 3.42 = 82.17 (rounding 0.01). Opening and charge by component: NOT FOUND IN DOCUMENT. The Board report (item 36, AR p.60 area) says the 78.75 DTL was "debited from the amount available for appropriation"; the P&L shows it as a tax charge (p.109), so the report wording is loose. 🟡
- Unrecognised DTA: none disclosed. Net current tax asset 157.25 (230.29): tax asset 278.54, liability 121.29 (Note 14, p.123). Tax paid 362.57 vs expense 435.61 (Note 14). Foots.
- Wind energy credits and 80-IA type holidays: NOT FOUND IN DOCUMENT.

## 11. REVENUE DETAILS (Note 23, p.127; Cons Note 38, pp.173-174)
- Export sales 2,227.15 (1,634.56), +36.3%; domestic 16,207.14 (14,611.29), +10.9%; product sales 18,434.29 (16,245.85). Job work income 105.22 (8.98). Energy credits from wind mills 265.54 (205.00), +29.5%. Export incentives 39.57 (47.54). Revenue from operations 18,844.62 (16,507.37). Foots.
- Exports = 11.82% of revenue from operations; "outside India" 2,227.15 (Cons Note 38, p.174). India 16,617.47 foots (16,207.14 + 105.22 + 265.54 + 39.57).
- By industry: see 0.2.
- Segments: Two reportable segments in the consolidated Note 38 (p.173): Investment Castings and Power Generation. The Board report names "Investment Activity and Power Generation Activities" (item 35, line 3248, AR p.60 area). The brief says the Q2 FY27 filing shows one segment; that is a difference between the AR and the later filing. Segment figures:
  - Revenue: castings 18,579.08 (16,302.37); power 265.54 (205.00). Segment PBIT: castings 2,212.22 (1,414.29); power 148.78 (95.79). Power margin 56.0% (derived). Foots to 2,361.00.
  - Segment assets: castings 19,752.80 (19,281.29), power 1,903.97 (188.59); total 21,656.77 = consolidated balance sheet (p.145). Foots. Segment liabilities: power 1,126.48 (Nil); castings 10,269.30 (10,343.35); total 11,395.78 (FY25 total printed 10,343.55 against segment sum 10,343.35, a 0.20 slip) (p.174).
  - Power Generation assets grew 10.1x (+1,715.38) while its revenue is wind credits only. The Board report says a 4 MW captive solar plant was installed and commissioned in the year (AR line 4278, p.74-75 area). INFERENCE: the solar assets and the loan behind them sit in the Power segment, so captive-solar savings appear in castings power cost while the asset base sits in Power. The Notes do not say this. 🟡
- Contract assets and liabilities: advances from customers 8.82 (31.81) (Note 21, p.126). Unsatisfied performance obligations and top-customer revenue: NOT FOUND IN DOCUMENT.
- Cost structure for margin cross-check (Note 30, p.129; Note 25): fettling and other external processing 5,158.98 (4,380.79), +17.8%, 27.4% of revenue from operations (26.5%); power and fuel 1,950.68 (1,985.20), -1.7%; stores 722.54 (733.45); materials consumed 5,216.05 (4,831.52), 27.7% of revenue (29.3%). The jump in external processing is the largest cost line. Power cost fell while revenue rose 14.2%, consistent with solar and wind. Foots: manufacturing 8,400.54.

## 12. OTHER CRITICAL NOTES
- Exceptional item: 52.51 for the New Labour Codes (21-Nov-2025), described as "regulatory-driven and non-recurring"; the company "continues to monitor" other aspects, so more could follow (Note 40, p.138; Cons Note 41, p.175). First exceptional item in the two years shown. 🟡
- Other income 123.59 (73.89): FX gain 75.30 (39.98); interest 30.29 (20.56); misc 17.71 (2.57); no rent (2.69); no disposal gain (8.09) (Note 24, p.127). Other income is 7.1% of PBT before exceptional. FX gain is 4.3% of it. 🟡
- Finance cost: banks 477.84 (589.96); "Others" 39.96 (3.95), a ten-fold rise; income-tax interest 0.31; other borrowing cost 99.86 (78.47) (Note 28, p.128). Lease interest is 11.14 so about 28.8 of "Others" is unexplained. Could include interest on delayed payments. NOT FOUND IN DOCUMENT. 🟡
- Foreign currency (Note 33, p.132): unhedged receivables USD 3.33 (3.67), EUR 0.66 (1.09); payables USD Nil (0.01); hedged EUR option "buy" 0.50 with one column only (year unclear). The table header says "Rs in Lacs" but the 5% sensitivity (USD 15.75; EUR 3.62) implies foreign-currency lakh (USD 3.33 x about Rs 94.6 = 315). Unit label unreliable. 🟡 minor.
- EPS (Note 31, p.130): standalone 11.77 vs 6.07; weighted shares 10,000,000; basic = diluted. Cons EPS 11.76 and FY25 shown as 3.03 on 605.72 profit and 1,00,00,000 shares (Cons Note 30, p.166; Cons P&L p.146). 605.72/10,000,000 = 6.06, not 3.03. Printed prior-year Cons EPS is wrong by half. 🟡 (data-feed risk if a screener takes the consolidated line)
- Share capital (Note 15, p.123-124): 1:1 bonus 5,000,000 shares issued 27-Jun-2025 out of general reserve 474.80 and securities premium 25.20 (Note 16, p.125). Issued 10,000,000 x Rs 10 = 1,000.00. Authorised 10,400,000 equity shares (so 400,000 shares of headroom). ESOP and dilution sources: NOT FOUND IN DOCUMENT (none stated). 🟢
- Promoter holding 31-Mar-2026 (Note 15c, p.124): Meche 16.19%, Piyush Tamboli 13.12%, HUF 9.66%, Vishakha 6.70%, Jainam 5.92%, Kavya 0.26%, Kasturi Kamdar 0.12% = 51.97% (foots). Rekha N Shah 10.00% (non-promoter, above 5%). Late R K Menon, 1,600 shares at March-2025, Nil now.
- Dividends (Note 34, p.133): paid 50.00 (50.00); recommended Rs 1 per share = 100.00. Payout 8.5% of FY26 PAT (derived).
- Reserves: no direct debits bypassing P&L except bonus (500.00) and OCI remeasurement 8.31 net (Note 16, p.125; SOCIE p.109). Equity roll foots: 8,643.16 + 1,176.62 - 50.00 - 500.00 + 8.31 = 9,278.09.
- CSR (Note 30, p.129): required 13.86, spent 13.86; FY25 required 12.64, spent 17.56, shortfall printed "(4.92)" meaning excess. Cumulative carry-forward of excess: NOT FOUND IN DOCUMENT. CARO 20: no unspent CSR (p.105). 🟢
- Auditor payments (Note 30): audit 6.95, other services 1.69, total 8.64 (6.89). Other services are 19.6% of the total. Cons total 9.20 (7.63) including taxation matters 0.13 (Cons Note 29, p.165). 🟢
- Capital management (Note 34, p.133): total debt 7,009.87, equity 10,278.09, 0.68x (0.71x). Net debt after cash 219.57 and other bank balances 167.94 = 6,622.36 (derived).
- Fair value (Note 32, p.130): all financial instruments at amortised cost; carrying = fair value; no hierarchy needed. 🟢
- Ratios (Note 39 A, p.137): current 1.20 (1.12) foots (10,420.71/8,703.22); ROE 12.12% (6.84%) foots; ROCE 12.80% (9.30%); net profit 6.24% (3.67%) foots; net capital turnover 10.97x (15.71x). Foots.
- Audit trail: edit log operated throughout (Note 39 N, p.138). Related disclosures in Note 39 (benami, struck-off, layers, wilful defaulter): all clean. 🟢
- Going concern: Note 1.1 "prepared on accrual and going concern basis" (p.112). CARO item 19: nothing brings "a material uncertainty" (p.105). No going-concern doubt anywhere in the Notes. 🟢
- Quarterly returns to banks: "generally in agreement"; "average under reported difference is not material... on account of valuation, provisions etc." (CARO 2(b), AR before [page 103]). The difference amount is not stated. 🟡
- Consolidated vs standalone: Cons PBT 1,690.51 vs 1,690.98; cash 221.03 vs 219.57; trade payable (others) 1,817.68 vs 1,823.77; other expenses 9,430.98 vs 9,430.51 (Cons P&L p.146; Cons BS p.145). Differences all come from the dormant subsidiary.
- Q4 FY26 results (two filings) are not part of this pass.

## 13. DISCLOSURE DEFECTS (typos and slips that a user could copy into a model)
1. Cons EPS FY25 3.03 (should be about 6.06). Cons P&L p.146; Cons Note 30 p.166.
2. Liquidity table FY25 (Note 33, p.131): long-term borrowings printed 644.65 with total 1,227.99, and "6,47.71" for total; Note 32 prints "6,44.65" (p.130). Right figure 644.65.
3. Standalone BS foot line reads "TOTAL LIABILITIES 21,679.96" but is equity plus liabilities (p.108).
4. Segment liabilities FY25 total 10,343.55 vs sum 10,343.35 (Cons Note 38, p.174).
5. Unclaimed dividend 3.03 (Note 13) vs 3.05 (Note 18), 0.02 gap (pp.122, 126).
6. "Cash generated from operations (103.34)" label (p.111).
7. Directors' remuneration percentages in Board report differ from Note 38 (Section 2).

---

# PASS 1 SUMMARY: TOP 10 FINDINGS BY INVESTOR IMPORTANCE

| Rank | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | FY26 audited revenue base is Rs 18,844.62 lakh (Rs 188.45 Cr). The 185.79 slide figure is the castings segment (excludes 265.54 wind credits); 189.7 is total income. Base year can be fixed. | Note 23 p.127; Cons Note 38 p.173; P&L p.109 | 🟢 |
| 2 | Related-party web with promoters: Meche purchases 319.88 plus Rs 100.00 deposit; capital advance 306.00 to Tamboli Foundry (unchanged, no completion date); guarantee commission 84.52; HUF rent 24.00; CMD and WTD pay +51% and +69%. Flows 884.92, 4.70% of revenue. Promoter-family cash take 29.1% of pre-exceptional PBT. | Note 38 pp.135-136; Notes 8-9 p.121 | 🟡 |
| 3 | A&D revenue doubled to 1,086.42 (539.01), 5.86% of segment-industry revenue. Notes name no customer or programme. Auto (63.8%) still drives the year (+21.2%); non-auto fell 5.7%. | Cons Note 38 p.174 | 🟢 (confirmed) / 🟡 (no programme detail) |
| 4 | Capex burst: Rs 2,403.28 cash capex in FY26 (plant additions 1,977.42), funded by CFO 2,577.89 and net debt +560.32. Power Generation segment assets jumped 10x to 1,903.97 with liabilities 1,126.48. Notes carry no capital commitment and no events-after note for the Rs 100 Cr plan. | Note 2 p.117; CF p.111; Cons Note 38 p.174 | 🟡 |
| 5 | Debt Rs 7,009.87: 75.8% short term, all floating by sensitivity maths, personal guarantee of a director, no rates, maturities or covenants disclosed. | Note 17 pp.125-126; Note 33 p.132 | 🟡 |
| 6 | Receivables improved: 5.83 over 6 months (0.15%) vs 132.09 (3.13%); days 80.09 vs 87.63; ECL allowance Nil. Cash conversion CFO 2.19x PAT in FY26. Inventory days 99.42 vs 108.75. | Note 11 pp.121-122; Note 39 p.137; CF p.111 | 🟢 |
| 7 | Inventory build in WIP (+12.1%) and stores (+18.5%) with FG down 24.9%. P&L inventory credit only 113.46. No write-down or overhead absorption disclosed. | Notes 10, 26 pp.121, 128 | 🟡 |
| 8 | MSME note says dues are within the due date, yet 413.20 of MSE payables are past due; interest on delay shown Nil; standard interest items missing. | Notes 22.1, 37 pp.127, 134-135 | 🟡 |
| 9 | Labour-code hit: exceptional 52.51, gratuity past service cost 43.10, gratuity funded ratio 53.8% (66.4%), no FY26 contribution. Company flags more clarity pending. | Notes 36, 40 pp.133-134, 138 | 🟡 |
| 10 | Tax and EPS quality: effective rate 30.4%, reconciliation covers current tax only with 511.91 of unexplained disallowances, MAT credit use ended; Cons FY25 EPS misprinted 3.03 vs about 6.06. | Note 14 p.123; Cons Note 30 p.166 | 🟡 |

Revenue-recognition aggressiveness: moderate. Dispatch-based recognition with a "delivery" KAM. No contract assets. 🟡
No red flags found in Pass 1. No going-concern language.

Receivables trend for the FLAG-CASH test (FY26 notes only): improving. Not due 87.9% (72.6%); over 6 months 0.15% (3.13%); days 80.09 (87.63).

END PASS 1
