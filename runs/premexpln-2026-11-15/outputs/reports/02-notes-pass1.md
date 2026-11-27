# Stage 2 Notes, Pass 1 (full extraction): PREMEXPLN, FY2025-26
Run: premexpln-2026-11-15 | Model: claude-sonnet-5-5 | Source: Annual_Report_2026.txt (46th AR, FY2025-26)

## Conventions (read first)
- Unit: the AR prints "All amounts in INR lakhs" (Notes p.113 onward). Every figure below is INR lakhs ("L" in anchors). No conversion done; stage 10 converts once. Where the AR prints crores (loan covenant), the text says so.
- Anchor form: (Note N, p.P, L). "p." is the PDF page marker in the .txt. Printed page number = p. minus 3 (Note 3 sits on p.123, printed 120).
- Standalone notes: Notes 1-46, pp.113-153. Consolidated notes: Notes 3-46 renumbered, pp.175-205. Where the two agree, the standalone anchor is given and the consolidated one named only if it differs.
- "Derived" = my arithmetic on anchored numbers, shown so a verifier can redo it. "[INFERENCE]" = reading, not a filed fact. Anything absent = "NOT FOUND IN DOCUMENT".
- FY26 = year to 31 Mar 2026. FY25 = prior year. FY24 comparatives come from Annual_Report_2025.txt, anchored to that file.
- B00 input_gaps carried forward: Q2 FY27 concall transcript absent; screener P&L/BS/CF sheets empty; no research. None of these blocks a notes read. The notes are a filed audited document, so these gaps do not touch this pass. One carried caution: B00 says OCR text for results PDFs is imperfect; the AR is a text PDF and reads cleanly.

## LOAD-BEARING FACTS: what the notes show (checked first)
| B00 fact | What the notes show | Rating |
|---|---|---|
| FY26 operating cash flow about -1 cr against PAT 45.8 cr | Cash flow statement: net cash from operations (144.14) L against PAT 4,582.51 L (p.112; Note 40, p.151). Operating profit before working capital 7,352.54 L, then working capital outflow: receivables and other assets (3,446.92), inventories +5,048.20, payables and provisions (7,464.51). Tax paid (1,633.45). Details in findings 2, 3, 6. | 🔴 |
| H1 FY26 PAT included other income | FY26 other income 4,214.49 L vs 211.53 L (Note 22, p.133). 3,417.80 L is a supplier purchase discount for materials "procured and consumed in the previous financial year"; 500.00 L is a provision reversal. Together 3,917.80 L = 64.8% of PBT 6,043.17 L (derived). | 🔴 |
| Receivables, contract assets | Receivables ageing and ECL in Note 11. Contract assets: NOT FOUND IN DOCUMENT as a line. Unbilled receivables 141.60 L sit inside Note 11 (p.127). | 🔴 / NOT FOUND |
| Related-party notes, Apollo / IDL | No Apollo or IDL Explosives party appears in Note 38 (p.147-150). Promoters' direct holdings are 0 at 31 Mar 2026; AKS Family Trust holds 41.33% (Note 14(iii),(iv), p.129). Date of transfer: NOT FOUND IN DOCUMENT. Note 45 events after the period lists only the proposed dividend (p.153). The SPA of 9 Jul 2026 post-dates board approval on 29 May 2026 (Note 1.3, p.113), so its absence is consistent. | 🟡 |
| Accident losses, insurance claims | Note 7(ii) (p.125), Note 29 (p.138), Note 29(d) (p.139). Details in finding 4. The notes never name Katepally or Peddakandukur. Plant, date, deaths, licence suspension, export-licence status, fines: NOT FOUND IN DOCUMENT in the notes. For context only (outside notes, Directors' Report, line 1785 of the .txt): fire and explosion at Katepally on 29 Apr 2025, four lives lost. Flares plant at Peddakandukur: NOT FOUND IN DOCUMENT anywhere in the notes. | 🟡 |
| Licence and contingent-liability notes | Note 34 (p.145) has no licence, PESO, accident-claim or export-order item. | 🟡 |

---
## 1. ACCOUNTING POLICIES AND CHANGES
- Basis: Ind AS, historical cost, going concern basis (Note 2.1, p.113). One reportable segment, "High Energy Materials" (Note 2.2, p.113; Note 35, p.199). 🟢
- Revenue (Note 2.5, p.114): point in time on delivery; services on output basis. Variable consideration is a named critical estimate: powder factor provision (percentage of blast output achieved at the customer site, measured at a later date), liquidated damages, volume discounts. The policy says "The Group estimates" in a standalone note (carry-over wording). 🟡 This is the soft spot in revenue: the deduction is estimated, and settled after the period. See finding 5.
- Depreciation (Note 2.6, p.115): straight line, Schedule II lives; residual not more than 5%; items costing Rs. 5,000 or below fully depreciated in the year. Specific useful lives in years: NOT FOUND IN DOCUMENT. No change in estimates reported. Derived: depreciation 1,000.89 L over average gross PPE ((26,668.00+25,930.38)/2 = 26,299.19 L) is 3.8%; plant and machinery 658.47 L over average gross 10,594.05 L is 6.2% (Note 3, p.123). 🟡 low (long implied lives; not a reported change).
- Intangibles (Note 2.7, p.115): software 3 years, other licences 5 years, technology transfer over licence period. Other licences amortise 57.75 L per year on gross 288.78 L = 5 years (Note 6, p.124). 🟢
- Capitalisation: R&D expensed (Note 2.19, p.121; Note 28 R&D expense 49.71 L, p.137). Borrowing cost capitalised only on qualifying assets (Note 2.11, p.118). Capitalised borrowing cost amount: NOT FOUND IN DOCUMENT. 🟢
- ECL (Note 2.10, p.117; Note 32(A), p.141): simplified approach, "historical default rates", provision matrix. Matrix rates by bucket: NOT FOUND IN DOCUMENT. Only the total is disclosed. 🟡
- Leases (Note 2.14, p.119): policy present (IBR for lease liability). Lease liability, IBR and maturity analysis: NOT FOUND IN DOCUMENT. Right-of-use land 85.66 L (Note 4, p.124). 🟡 low.
- Impairment test assumptions (growth, discount rate): NOT FOUND IN DOCUMENT (no impairment recorded; investments impairment nil, Note 7(i), p.125). Goodwill: none.
- Government grants (Note 2.22, p.121): export entitlements are netted from "Cost of materials consumed". Amount: NOT FOUND IN DOCUMENT. 🟡 low.
- New standards (Note 2.24, p.121-122): Ind AS 1 amendment on covenants adopted, no change to classification. Supplier finance amendment (Ind AS 7/107) adopted, "new disclosures in note 15(e)". Note 15(e) is two sentences with no carrying amounts, payment terms or due-date ranges (p.130). 🟡 See finding 9.
- Labour codes effective 21 Nov 2025: impact "not likely to be material" (Note 35, p.145). Quantification: NOT FOUND IN DOCUMENT. 🟢
- First-time adoptions with quantified P&L impact: none reported.

## 2. RELATED PARTY TRANSACTIONS (Note 38, p.147-150; consolidated Note 37, p.200-201)
Related parties (Note 38(a)-(d), p.147): subsidiaries PELNEXT Defence Systems Pvt Ltd (100%) and Premier Wire Products Ltd (80%); JV Global Premier Ltd (49%, from 7 Mar 2025); KMP incl. Dr. A.N. Gupta (Chairman), Mr. T.V. Chowdary (MD), Mr. Y. Durga Prasad Rao (WTD), Dr. (Mrs.) Kailash Gupta, independent directors; relatives Mrs. T. Malati, Mrs. T. Shruti; significant-interest entities A.N. Gupta (HUF) and AKS Family Trust.

| Party | Relationship | Nature | FY26 L | FY25 L | YoY |
|---|---|---|---|---|---|
| KMP (3 executives) | KMP | Managerial remuneration | 445.29 | 341.33 | +30.5% (derived) |
| Dr. A.N. Gupta | Chairman | Remuneration | 87.60 | 62.12 | +41.0% (derived) |
| Mr. T.V. Chowdary | MD | Remuneration | 240.89 | 189.31 | +27.2% (derived) |
| Mr. Y. Durga Prasad Rao | WTD | Remuneration | 116.80 | 89.90 | +29.9% (derived) |
| KMP | KMP | Dividend paid (standalone) | 95.49 | 95.58 | -0.1% |
| KMP (Gupta family) | KMP | Unsecured loan repaid | nil | 519.05 | n.m. |
| KMP | KMP | Interest paid | nil | 3.53 | n.m. |
| Directors | KMP | Sitting fees | 11.98 | 16.13 | -25.7% |
| Relatives of KMP | Relatives | Dividend paid | 0.51 | 0.51 | 0% |
| A.N. Gupta (HUF) | Significant interest | Dividend paid | 16.42 | 16.42 | 0% |
| Premier Wire Products Ltd | 80% subsidiary | Interest paid | 26.48 | 27.92 | -5.2% |
| Premier Wire Products Ltd | 80% subsidiary | Rent paid | 1.19 | 1.19 | 0% |
| Premier Wire Products Ltd | 80% subsidiary | Reimbursement of expenses | 0.01 | 0.91 | n.m. |
| PELNEXT Defence Systems | 100% subsidiary | Loan given | 2.00 | nil | n.m. |
| PELNEXT Defence Systems | 100% subsidiary | Interest income | 0.31 | 0.29 | +6.9% |
| Global Premier Ltd | JV | Investment | 4.90 | nil | n.m. |
Balances (Note 38(f), p.149): employee benefits payable to Dr. Gupta 65.07 (39.74), Mr. Chowdary 71.40 (46.70), Mr. Rao 36.56 (22.70). Loan payable to Premier Wire Products Ltd 423.39 (399.56), unsecured, repayable in cash. Loan receivable from PELNEXT 6.66 (4.38). Loans payable to Dr. Gupta and Dr. Kailash Gupta: nil both years. Receivables from related parties: none shown.

Findings:
- RPT as % of revenue (derived, revenue 38,834.14 L, Note 21, p.132): KMP remuneration 445.29 L = 1.15%; all non-dividend flows (445.29 + 11.98 + 26.48 + 1.19 + 0.01 + 0.31 + 2.00 + 4.90) well below 2%. 🟢
- KMP pay rose 30.5% in a year when revenue fell 6.97% (38,834.14 vs 41,745.23 L, Note 21, p.132) and employee cost rose 11.3% (6,890.82 vs 6,192.83 L, Note 25, p.134). Pay is 7.4% of PBT 6,043.17 L (derived). Breakdown into fixed and variable: NOT FOUND IN DOCUMENT in the notes. 🟡
- Promoter family loans fully repaid in FY25 (519.05 L). Nothing outstanding. 🟢
- Subsidiary-to-parent loan: Premier Wire Products Ltd lends 423.39 L to the parent at "7 to 8.95%" (Note 15, p.130). Interest paid 26.48 L is 6.4% on the 411.5 L average balance (derived), below the stated range floor. Terms not explained. Eliminated on consolidation (consolidated current borrowings 1,917.32 L vs standalone 2,340.71 L, Note 13, p.182). 🟡 low
- Rate inconsistency: KMP loans carry "8.95% per annum" in the standalone note (Note 38(g)(ii), p.150) and "10% per annum" in the consolidated note (Note 37(g)(ii), p.201). KMP dividend paid is 95.49 L standalone vs 95.58 L consolidated. 🟡 low (small, but two filed notes disagree)
- Control change: individual promoter holdings (Dr. A.N. Gupta 1,31,00,915 shares 24.37%; Dr. (Mrs.) Kailash Gupta 58,37,335 shares 10.86%; A.N. Gupta HUF 32,83,485 shares 6.11% at 31 Mar 2025) show nil at 31 Mar 2026; AKS Family Trust shows 2,22,21,735 shares, 41.33% (Note 14(iii),(iv), p.129; consolidated Note 12, p.181). 100% change recorded. FY26 dividends were still paid to Dr. Gupta (65.50 L), Dr. Kailash Gupta (29.19 L) and the HUF (16.42 L) (Note 38(f), p.150). Date of transfer, consideration, whether this is an inter-se family trust transfer: NOT FOUND IN DOCUMENT in the notes. [INFERENCE] The 41.33% in the pending Apollo SPA (B00) matches this trust holding; the notes do not say so. 🟡
- New related parties this year: Global Premier Ltd (JV, 49%, effective 7 Mar 2025 per Note 38(a); 4.90 L invested in FY26, share application money 4.90 L at FY25 in Note 9, p.126). AKS Family Trust appears as a related party for the first time as a holder. 🟡
- Non-arm's-length signals: loans to promoter entities none; royalty, fee to promoter family none shown; rent only to the subsidiary (1.19 L). "Purchase of land" from KMP: nil both years. 🟢

## 3. CONTINGENT LIABILITIES (Note 34, p.145; consolidated Note 32, p.197) and COMMITMENTS (Note 35, p.145)
| Nature | Mar-26 L | Mar-25 L | Stage | Company view |
|---|---|---|---|---|
| Letters of credit and guarantees issued by bankers | 7,607.05 | 5,945.21 | not given | not given |
| Sales tax claims | 575.83 | 575.83 | not given | "not practicable to estimate timings" |
| GST claims | 98.88 | nil (blank) | not given | same |
| Income tax | 61.84 | 61.84 | not given | same |
| Others (consolidated only) | 10.00 | 10.00 | not given | not given |
| Total standalone (derived) | 8,343.60 | 6,582.88 | | |
- Total standalone 8,343.60 L = 28.9% of net worth 28,903.17 L (Note 33, p.144) (derived). LCs and guarantees alone are 26.3% of net worth and grew 28.0% (derived: 1,661.84 / 5,945.21). They are secured in part by margin money deposits of 914.00 L (Note 13, p.128). No single tax item exceeds 10% of net worth (sales tax 575.83 L = 2.0%). 🟡
- New GST claim 98.88 L in FY26: authority, year and forum NOT FOUND IN DOCUMENT. 🟡
- Forum, assessment year and case stage for sales tax claim (unchanged 575.83 L both years): NOT FOUND IN DOCUMENT. No provision made for any item. 🟡
- Guarantees for subsidiaries: NOT FOUND IN DOCUMENT. No guarantee to or for PELNEXT, Premier Wire or Global Premier is listed.
- Accident-related claims (fatalities, regulator, PESO or pollution board, third party): NOT FOUND IN DOCUMENT in Note 34. Note 34 is silent although the Directors' Report records four deaths (outside notes). 🟡
- Commitments: capital contracts not provided for, net of advances, 1,708.70 L vs 1,441.54 L (Note 35, p.145). Capital advances 821.20 L vs 334.61 L (Note 9, p.126). 🟢

## 4. TRADE RECEIVABLES (Note 11, p.127-128; consolidated Note 9, p.179-180)
Balance: billed 6,108.44 + unbilled 141.60 = 6,250.04 L gross, less ECL 905.47 = 5,344.57 L net (FY25: 4,191.11 + 138.50 = 4,329.61 gross, ECL 521.80, net 3,807.81). All "considered good - unsecured"; disputed, doubtful, credit impaired: nil both years (Note 11(b), p.127).

Ageing from due date (Note 11(c),(d), p.127-128; checked: both rows sum to the total):
| Bucket | Mar-26 L | % gross | Mar-25 L | % gross |
|---|---|---|---|---|
| Not due and unbilled | 3,724.82 | 59.6% | 2,701.88 | 62.4% |
| Less than 6 months | 942.85 | 15.1% | 740.37 | 17.1% |
| 6 months - 1 year | 395.64 | 6.3% | nil | 0% |
| 1-2 years | 298.38 | 4.8% | 575.62 | 13.3% |
| 2-3 years | 556.28 | 8.9% | 123.87 | 2.9% |
| More than 3 years | 332.07 | 5.3% | 187.87 | 4.3% |
| Total | 6,250.04 | | 4,329.61 | |
- Over 6 months (derived): 395.64 + 298.38 + 556.28 + 332.07 = 1,582.37 L = 25.3% of gross (FY25: 887.36 L = 20.5%). The auditor's KAM prints "29.61%" past due over 180 days (p.154); that equals 1,582.37 / 5,344.57 net (derived), so the auditor divides by net receivables. Over 1 year: 1,186.73 L = 19.0% of gross (FY25: 887.36 L = 20.5%). All overdue (any age): 2,525.22 L = 40.4% (FY25: 1,627.73 L = 37.6%). 🔴
- Old balances are not clearing: FY25's 1-2 year bucket (575.62 L) is 556.28 L in the 2-3 year bucket a year later (only 19.34 L gone); the over-3-year bucket rose from 187.87 to 332.07 L (derived). Bad debts written off in FY26 only 30.13 L (Note 29, p.138). 🔴
- ECL: 905.47 L = 14.5% of gross (FY25 12.1%; FY24 opening 132.14 L); charge 383.67 L in FY26 and 389.66 L in FY25 (Note 32(A), p.141). ECL covers 57.2% of the over-6-month balance (derived). The charge has been near 385 L two years running; rates by bucket not disclosed. 🟡
- Who owes: the auditor's KAM says "the most significant portion" over 180 days is Public Sector companies and Government organisations "within their historic payment patterns" (p.154). Customer names and the amount: NOT FOUND IN DOCUMENT. Audit confirmations drew "non-response"; the auditor used subsequent receipts and alternative procedures (p.154). 🟡
- Single customer 10% or more of revenue: one customer in both years (Note 21, p.133; Note 35, p.145). Name and amount: NOT FOUND IN DOCUMENT. Share of receivables: NOT FOUND IN DOCUMENT. 🟡
- Receivable days, closing net receivables over revenue x 365 (derived): FY26 50.2 days (5,344.57 / 38,834.14); FY25 33.3 days (3,807.81 / 41,745.23); FY24 97.6 days (7,265.33 / 27,171.67; FY24 balances from Annual_Report_2025.txt, trade receivables note p.125 and revenue p.130). Trend: FY25 was the low; FY26 deteriorates by 16.9 days. Gross basis FY26: 58.7 days (derived). Company's own ratio: turnover 8.49 vs 7.54 (Note 43, p.152), which uses average balances and so hides the year-end rise. 🔴 on direction, not on level (FY24 was higher).
- Related-party receivables: none (Note 38(f), p.149). 🟢
- Receivables are pledged as primary security for working capital (Note 41, p.151). 🟢

## 5. INVENTORY (Note 10, p.126; consolidated Note 8, p.178)
| L | Mar-26 | Mar-25 | Mar-24 (AR2025) | Change FY26 |
|---|---|---|---|---|
| Raw materials | 6,067.25 | 8,026.15 | n/a | -24.4% |
| Work-in-progress | 2,388.07 | 6,024.82 | 3,342.94 | -60.4% |
| Finished goods | 1,229.36 | 650.58 | 239.93 | +88.9% |
| Stores and spares | 616.07 | 647.09 | n/a | -4.8% |
| Scrap | 0.51 | 0.82 | 1.02 | |
| Total | 10,301.26 | 15,349.46 | 8,787.01 | -32.9% |
(FY24 total from AR2025 trade note p.125 area, total inventories 8,787.01; WIP and FG FY24 from Note 24 opening balances, p.134.)
- Finished goods grew 88.9% while revenue fell 6.97% (derived). FG equals 11.6 days of revenue (derived). Small in rupees; the direction is the point. 🟡
- Write-downs: provision for obsolete stock 13.72 L (FY25 15.23 L) (Note 10(c), p.126). No NRV write-down beyond this reported. 🟢
- Inventory days on revenue, closing (derived): FY26 96.8, FY25 134.2, FY24 118.0. Company turnover 2.72 vs 3.22 (Note 43, p.152). 🟢 on level; the FY25 build (RM +3,377.60, WIP +2,681.88 L) has now unwound.
- Inventory pledged as security; quarterly returns agree with books (Note 10(b), p.126). 🟢

## 6. INVESTMENTS AND LOANS (Note 7(i), p.125; Note 8, p.125-126; Note 37, p.147)
| Entity | Stake | Carrying L (Mar-26 / Mar-25) | Note |
|---|---|---|---|
| Premier Wire Products Ltd | 80% (52,00,000 shares of Rs. 10) | 520.00 / 520.00 | subsidiary, cost |
| PELNEXT Defence Systems Pvt Ltd | 100% (10,000 shares) | 1.00 / 1.00 | subsidiary, cost |
| Global Premier Ltd | 49% (48,980 shares) | 4.90 / nil | JV, cost; consolidated at equity 3.69 after share of loss 1.21 (Note 4(b), p.176) |
| Total | | 525.90 / 521.00 | impairment nil |
- PELNEXT: net assets (6.63) L, loss before tax 0.80 L, current liabilities exceed current assets by 6.63 L; auditor reports "material uncertainty" on going concern (Other Matters (b), p.157; consolidated Note 43, p.204). The 1.00 L investment is carried unimpaired and the parent lent 6.66 L (Note 8, p.125). Size is trivial; the filing still shows an unimpaired investment in an entity with negative net worth. 🟡 low
- JV loss: the auditor's Other Matters says "share of Loss of Joint venture ... Rs.2.22 Lakhs" (p.157); Note 4(b) and Note 41 show 1.21 L (p.176, p.203). A 1.01 L disagreement between auditor report and note. 🟡 low
- Loans given: only to PELNEXT, 6.66 L (4.38 L), 100% of loans, repayable on demand, interest-bearing, rate NOT FOUND IN DOCUMENT (Note 8(a),(b), p.125-126). 🟢
- Premier Wire Products Ltd: net assets 532.94 L, profit 0.84 L (Note 41, p.203) against a 520.00 L cost. Non-controlling interest 135.52 L. Return on the 520.00 L is nil; the subsidiary is also a lender to the parent (see section 2). 🟡 low
- Other investments (quoted, mutual funds, unrealised gains): none; "Aggregate amount of unquoted investments 525.90" (Note 7(i), p.125). 🟢
- Subsidiary financials audited by other auditors, total assets 706.81 L (p.157). 🟢

## 7. BORROWINGS (Note 15, p.130; Note 33, p.144-145; Note 41, p.151)
| Instrument | Mar-26 L | Mar-25 L | Rate | Security |
|---|---|---|---|---|
| Term loans from banks (total) | 2,125.97 | 1,250.00 | 8.60% to 10.60% | first charge on non-current assets, second charge on current assets, MD personal guarantee |
| less current maturities | (809.97) | (500.00) | | |
| Non-current borrowings | 1,316.00 | 750.00 | | |
| Working capital loans | 359.79 | 1,986.56 | 8.50% to 10.45% | stocks, receivables, PPE, MD personal guarantee |
| Current maturities | 809.97 | 500.00 | 8.60% to 10.60% | |
| Loans from related parties (Premier Wire Products Ltd) | 423.39 | 399.56 | 7% to 8.95% | unsecured |
| Loans from banks (supplier finance, Note 15(e)) | 747.56 | 828.35 | 8.95% to 9.95% | unsecured |
| Total current | 2,340.71 | 3,714.47 | | |
| Total borrowings | 3,656.71 | 4,464.47 | | |
- Term loan terms (Note 15(b), p.130): six quarterly instalments of 125.00 L at 10.60% (750.00 L); twelve quarterly instalments of 103.32 L at 8.75% from HDFC Bank (1,239.84 L); sixteen quarterly instalments of 8.51 L at 8.60% from SBI (136.16 L). Sum 2,126.00 L vs carrying 2,125.97 L (derived, ties). Current maturities of 809.97 L equal 500.00 L + 3 x 103.32 L = 809.96 L (derived); four quarters of all three loans would be 947.32 L. The note does not say which instalments fall due in FY27. Treat the 5-year repayment schedule as not disclosed beyond these instalment counts. 🟡 low
- Net debt negative: borrowings 3,656.71 L against cash and cash equivalents 5,057.21 L plus margin money 914.00 L (Note 33, p.144). Net cash 2,314.50 L (derived). Gearing 0.00%. Debt/equity 0.13 (Note 43, p.152). 🟢
- Covenants (Note 33(b), p.145): net worth above "Rs. 220 crores" including deferred tax liabilities; total outside liabilities below 1.00x net worth; total debt below 2.00x EBITDA; DSCR above 1.25. "The company has complied with these covenants throughout the reporting period." Net worth is 28,903.17 L (Note 33, p.144); the AR prints the covenant in crores (220 crores; stage 10 converts). No breach, waiver or term change reported. 🟢
- Interest check (derived): "Interest and finance charges on financial liabilities at amortised cost" 152.35 L (Note 26, p.137) on average borrowings of 4,060.59 L = 3.8%, below every stated rate (8.50% to 10.60%). Other borrowing costs 212.60 L carry the balance. Finance costs fell 67.1% (364.95 vs 1,109.55 L). The split between interest and bank charges is not explained. 🟡 low
- Fixed versus floating: NOT FOUND IN DOCUMENT as a split. Note 32(B) says rates are "fixed ... linked to marginal cost of lending rate" (p.142). Related-party borrowings from directors: nil outstanding. Borrowings reconciliation (Note 33(c), p.145): opening 4,464.47, proceeds 875.97, repayment (1,683.73), closing 3,656.71. Ties. 🟢
- Security: all current and non-current assets pledged; 45,682.71 L carrying value pledged against current borrowings (Note 41, p.151). MD personal guarantee on both loan types. 🟡 low
- Supplier finance: see finding 9.

## 8. TRADE PAYABLES (Note 36, p.146; Note 32(C), p.143-144)
| L | Mar-26 | Mar-25 | Mar-24 (AR2025) |
|---|---|---|---|
| MSME | 56.34 | 566.05 | n/a |
| Others | 4,095.29 | 11,088.85 | n/a |
| Total | 4,151.63 | 11,654.90 | 1,557.87 |
| Not due | 1,559.34 | 1,467.29 | |
| Less than 1 year | 1,769.80 | 10,056.11 | |
| 1-2 years | 272.04 | 8.36 | |
| 2-3 years | 457.12 | 42.27 | |
| More than 3 years | 93.33 | 80.87 | |
(FY24 total payables: Annual_Report_2025.txt financial-instruments note, p.138.)
- Payables fell 7,503.27 L (-64.4%) while purchases fell 43.3% (17,127.79 vs 30,197.68 L, Note 23, p.133). Payable days on purchases (derived): FY26 88.5; FY25 140.9; FY24 48.3 (purchases FY24 11,764.09 L, AR2025 Note 23, p.131). The FY25 balance was the outlier. 🟡
- Over 1 year old: 822.49 L = 19.8% of payables (FY25 131.50 L, 1.1%) (derived). Ageing roll check: the FY26 2-3 year bucket (457.12 L) cannot arise from the FY25 1-2 year bucket (8.36 L). Either the ageing basis changed or items were reclassified. The note gives no reason. 🟡
- MSME dues: principal unpaid 56.34 L, interest due nil, interest paid nil (Note 36(a), p.146). The list of MSME suppliers is "determined ... on the basis of information available". MSME dues over 45 days: NOT FOUND IN DOCUMENT as a separate figure. 🟢 low
- Foreign-currency payables for supplies USD 29,63,126 = 2,804.73 L vs USD 1,14,41,660 = 9,791.93 L (Note 32(B), p.142-143). 🟡 see section 12.

## 9. PROVISIONS (Notes 17, 25, 29(c); p.131, p.134-137, p.139)
| L | Mar-26 | Mar-25 |
|---|---|---|
| Gratuity non-current / current | 789.83 / 150.26 | 836.25 / 100.38 |
| Leave encashment non-current / current | 219.20 / 131.93 | 224.30 / 78.76 |
- Gratuity (Note 25(a), p.135-137): DBO 1,538.88 L, plan assets 598.79 L, deficit 940.09 L (FY25 936.63 L). Plan assets cover 38.9% of DBO (derived). Balance sheet provision 789.83 + 150.26 = 940.09 L, ties. Net cost 142.01 L; actuarial gain 19.19 L in OCI. "The company does not fully fund the liability." Next-year contribution: NOT FOUND IN DOCUMENT. 🟡
- Assumptions: discount 7.49% (6.79%); salary growth 4% (4%); withdrawal 2%; retirement age 58; mortality LIC 2012-14; duration 6.00 years (7.00). Sensitivity: salary +1% raises DBO to 1,639.35 L (+6.5%); discount -1% to 1,628.02 L (+5.8%). Against the filing: salaries, wages and bonus rose 10.1% (6,113.51 vs 5,550.26 L, Note 25, p.134) and KMP pay rose 30.5% (derived), while the actuarial salary growth stays at 4%. 🟡
- Leave encashment assumptions: NOT FOUND IN DOCUMENT as separate. Warranty, decommissioning: none disclosed (NOT FOUND IN DOCUMENT).
- Litigation provisions: none. Onerous contracts: a 500.00 L provision for "expected loss on long term contracts" booked in FY25 (Note 29, p.138; FY25 other expense 500.00 L) was reversed to other income in Q1 FY26 "pursuant to reassessment of the expected contract income" (Note 29(c), p.139; Note 22, p.133). The contract, customer and reassessment basis: NOT FOUND IN DOCUMENT. 🟡 See finding 5.
- Provision for doubtful advances 82.00 L in FY25, nil in FY26 (Note 29, p.138). 🟢

## 10. DEFERRED TAX AND INCOME TAX (Note 18, p.131-132; Note 30, p.139-140; Note 20, p.132)
- Net deferred tax liability 1,231.11 L (FY25 1,346.53 L): PPE and intangibles 1,785.80 L, ECL asset (227.89) L, allowable-on-payment items (326.80) L. No MAT credit, no tax-loss asset. Consolidated DTL 1,266.00 L (Note 16, p.183). 🟢
- Tax expense 1,460.66 L on PBT 6,043.17 L = 24.2% effective (derived). Statutory 25.168% (FY25: 29.12%). Company "exercised the option permitted under Section 115BAA" during the year (Note 30(b), p.140). Re-measurement of deferred tax at the revised rate gave a (69.29) L credit. Current tax 1,625.00 L = 26.9% of PBT (derived). Tax paid 1,633.45 L (p.112). 🟢
- MAT credit: 472.83 L at 1 Apr 2024 was taken to profit or loss in FY25 deferred tax (Note 18 movement, p.132) and stands nil since; FY25 total deferred tax was (2.25) L only because PPE and ECL movements offset it. Utilisation timeline and why the credit was written off in FY25 when the 115BAA option is described as exercised "during the year" FY26: NOT FOUND IN DOCUMENT. 🟡 low
- Unrecognised DTA: NOT FOUND IN DOCUMENT (none stated). DTA realism: ECL DTA 227.89 L is 25.2% of the ECL stock, consistent with the rate. 🟢
- FY25 effective-rate reconciliation carried a (281.26) L item for "change in tax rate of Long term Capital Gain" and (45.71) L for voluntary retirement scheme (Note 30(b), p.140). Voluntary retirement expense in the FY25 P&L: NOT FOUND IN DOCUMENT (cash flow line is nil both years, p.112). 🟡 low

## 11. REVENUE DETAILS (Note 21, p.132-133; Note 19, p.132)
| L | FY26 | FY25 | YoY (derived) |
|---|---|---|---|
| Sale of products | 34,874.95 | 38,844.07 | -10.2% |
| Sale of traded goods | 238.41 | 160.75 | +48.3% |
| Sale of services | 3,593.78 | 2,622.00 | +37.1% |
| Other operating revenue | 127.00 | 118.41 | +7.3% |
| Total revenue from operations | 38,834.14 | 41,745.23 | -7.0% |
| India | 33,665.36 | 33,897.22 | -0.7% |
| Other countries | 5,168.78 | 7,848.01 | -34.1% |
- Exports are 13.3% of revenue (FY25 18.8%) (derived). 🟡
- Product and segment split (explosives versus defence): NOT FOUND IN DOCUMENT. Single segment, CODM sees "overall financial information ... together" (Note 2.2, p.113; Note 35, p.199). The sector-cap separator that B00 names (filed segment revenue and segment result split) does not exist in the notes; it must come from elsewhere. 🟡
- Variable consideration (Contract Price Reconciliation, Note 21, p.133): contract price 41,310.61 L less variable consideration 2,476.47 L = 38,834.14 L. FY25: 46,061.49 L less 4,316.26 L. Deductions fell from 9.37% to 5.99% of contract price (derived). That drop adds about 1,400 L of revenue against FY25's deduction rate (derived: 41,310.61 x (9.37% - 5.99%) = 1,396). The note does not explain the rate change; the auditor flags powder factor, liquidated damages and rebates as a KAM (p.154-155). 🔴/🟡 (🟡 rating, see finding 5)
- Contract assets and unsatisfied performance obligations (Ind AS 115 disclosures): NOT FOUND IN DOCUMENT. Order book is not in the notes. Policy cites "timing of recognition" in Note 21 but the note gives geography only. 🟡
- Contract liabilities: "Advance from customers" 6,622.26 L (FY25 7,242.69 L) (Note 19, p.132) = 17.1% of revenue (derived). Of which foreign-currency advances USD 29,05,584 = 2,546.28 L (FY25 967.39 L) (Note 32(B), p.142-143). Revenue recognised from the opening balance: NOT FOUND IN DOCUMENT. 🟡
- Top customer: one customer above 10% of revenue in both years; name, amount NOT FOUND IN DOCUMENT (Note 21, p.133). 🟡

## 12. OTHER CRITICAL NOTES
**Other income and exceptional items (Note 22, p.133; Note 29(c),(d), p.139)**
- Other income 4,214.49 L vs 211.53 L: interest 221.51; excess liabilities no longer required 32.71; provision reversal 500.00; credit balances written back 0.84; other non-operating income 3,459.43 (of which purchase discount 3,417.80 "arising from a commercial settlement with a supplier relating to materials procured and consumed in the previous financial year"). 🔴
- Recurrence: purchase discount nil in FY25 (other non-operating income was 73.26 L). Supplier name, settlement date, whether settled in cash or by credit note, whether prior-year cost of materials consumed was restated: NOT FOUND IN DOCUMENT. FY25 cost of materials consumed (26,820.08 L) is unchanged in the FY26 comparative (Note 23, p.133). The discount equals 11.3% of FY25 purchases of 30,197.68 L (derived).
- Exceptional item: ex-gratia compensation 520.00 L to employees affected by the accident (Note 29(d), p.139; statement of profit and loss, p.110). PBT before exceptional 6,563.17 L; after 6,043.17 L.
- Ratio tie (derived): the company's FY26 ROCE of 8.03% (Note 43, p.152) reproduces exactly as EBIT of 2,713.63 L (PBT before exceptional 6,563.17 + finance costs 364.95 - other income 4,214.49) over capital employed of 33,791.00 L (net worth 28,903.17 + debt 3,656.71 + deferred tax liability 1,231.11). So the company's own ratio strips out all other income. EBITDA on the same basis is 3,882.18 L (2,713.63 + depreciation 1,168.55), 10.0% of revenue (derived). FY25 ROCE (14.66%) does not tie to the same formula (my reconstruction gives 15.3%), so the definition is not fully stable between years. 🟡
- PBT quality (derived): removing the 3,417.80 L discount and the 500.00 L reversal leaves 2,125.37 L of PBT, 35.2% of reported 6,043.17 L. PAT would still be reported 4,582.51 L; no tax effect applied here. 🔴

**Accident, insurance and loss (Note 7(ii), p.125; Note 3 note 4, p.123; Note 29, p.138; auditor Emphasis of Matter, p.154)**
- Damage to plant and machinery and buildings of 709.80 L. Insurance claim receivable "recognized" 609.80 L; balance 100.00 L charged to P&L as "Loss on destruction of PPE" (Note 29, p.138). The claim was booked in Q1 and "remains pending settlement" at 31 Mar 2026. Assets "adequately insured".
- Contradiction: the balance sheet note shows "Insurance receivable 683.59 L" (Note 7(ii), p.125; consolidated Note 4(c), p.176), not 609.80 L. The 73.79 L gap is unexplained. 🟡
- Total P&L cost of the accident that the notes identify: 100.00 + 520.00 = 620.00 L (derived). Lost-production, business-interruption claims and fines: NOT FOUND IN DOCUMENT. PPE disposals include the lost assets: gross 1,391.14 L, accumulated depreciation 585.68 L, net 805.46 L (Note 3, p.123).
- Auditor draws attention to the matter as an Emphasis of Matter; opinion not modified (p.154). 🟡
- [INFERENCE] Employee benefits payable rose to 1,248.26 L from 680.06 L (+83.5%, Note 16(ii), p.131) and staff welfare rose 44.8% (426.07 vs 294.25 L, Note 25, p.134). Some of the 520.00 L ex-gratia may sit unpaid in that balance; the notes do not say.
- Repairs to buildings jumped to 202.58 L from 60.08 L (+237%, Note 29, p.138). Whether accident restoration was expensed: NOT FOUND IN DOCUMENT. 🟡

**Foreign currency (Note 32(B), p.142-143; Note 29, p.138)**
- Net FX loss in other expenses 591.64 L vs 2.53 L (Note 29, p.138). The note says the company "is not significantly exposed to this risk because of natural hedging" (p.142). Net unhedged foreign-currency liabilities 1,798.63 L at Mar-26 (USD (17,99,419) and EURO (92,400)) vs 9,551.80 L at Mar-25. A 2.5% move is shown as USD (42.65) L (FY25 (234.83) L). No hedging instruments disclosed. The 591.64 L loss equals 9.8% of PBT (derived). 🟡
- Non-monetary foreign items: advances from customers 2,546.28 L, advances to suppliers 921.69 L (p.142).

**Capital items**
- Capex: PPE additions 653.52 L; CWIP additions 2,486.93 L; CWIP at year end 2,639.23 L, of which under 1 year 2,557.87 L (Note 3, p.123); no overdue or over-budget project stated. Payments for PPE in the cash flow 2,783.15 L (p.112). Capital advances 821.20 L (p.126). Capital creditors 205.42 L (53.44 L) (p.131). 🟢
- Intangibles: technology transfer rights net 440.50 L from DRDO, HEMRL, Balkan Novoteh DOO, Adron R&D Company Limited and ISRO (Note 6, p.124). Additions 90.64 L. 🟢

**Equity and per share (Notes 14, 40, 45; p.129, p.151, p.153)**
- Shares 5,37,61,195 of Rs. 2 after a 1:5 split on 21 Jun 2024 (Note 14(v), p.129). No ESOP, no dilutive securities; basic = diluted EPS Rs. 8.52 (Rs. 5.31). PAT 4,582.51 L. 🟢
- Dividend: Rs. 0.50 per share, 268.81 L, proposed (both years) (Note 45, p.153) = 5.9% of PAT (derived). Reserves bypassing P&L: none other than OCI remeasurement 14.36 L (p.111). 🟢
- HDFC Trustee Company (HDFC Defence fund) 48,88,455 shares, 9.09% (8.02%) (Note 14(iii), p.129).
- Share capital changes: none in FY26. Events after reporting date: dividend only (Note 45, p.153). 🟢

**Other**
- CSR: required 58.32 L, spent 59.38 L; environmental sustainability 45.00 L (FY25 2.50 L) (Note 29(b), p.139). Nature of the 45.00 L spend: NOT FOUND IN DOCUMENT. 🟢
- Auditor fees 26.05 L, incl. non-audit GST and certification work 6.00 L (Note 29(a), p.139). 🟢
- Political donation 3.00 L to Communist Party of India (Note 39, p.150). 🟢
- Ratio note (Note 43, p.152): current ratio 1.60 (1.26, +27%), DSCR 7.59 (3.00, +153%), payables turnover 2.17 (4.57, -53%), net capital turnover 4.00 (6.32, -37%), debt-equity -30%. The note gives reasons only for debt-equity, DSCR, receivables turnover and payables turnover. Reasons missing for current ratio (+27%) and net capital turnover (-37%). The "% Change" column mixes relative changes with percentage-point changes (ROE 17% vs 12% shown as "5%"). 🟡 low
- Going concern language: parent none. Subsidiary PELNEXT: material uncertainty (p.157; consolidated Note 43, p.204). Immaterial (6.63 L negative net assets). 🟢
- Standalone Note 14(iii) labels the FY25 share counts "Face Value Rs. 10" while the counts are post-split Rs. 2 shares (the consolidated note says Rs. 2, p.181). 🟢 low.

---
# PASS 1 SUMMARY: TOP 10 FINDINGS BY INVESTOR IMPORTANCE
Unit INR lakhs. Two readings are named where the filing is open to both.

| # | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | Other income 4,214.49 L (FY25 211.53 L) includes a 3,417.80 L supplier purchase discount for materials "procured and consumed in the previous financial year", plus a 500.00 L provision reversal. Together 3,917.80 L, 64.8% of PBT 6,043.17 L. Without them PBT is about 2,125.37 L (derived). The company's own ROCE (8.03%) reproduces only when all other income is removed: operating EBIT 2,713.63 L, EBITDA 3,882.18 L, 10.0% of revenue (derived). Reading A: a one-off true-up of a prior-year cost. Reading B: a cost-reduction that belongs in cost of materials and in FY25. The separating observation is the settlement terms and date, which the note does not give. | Note 22, p.133; Note 29(c), p.139; Note 43, p.152; L | 🔴 |
| 2 | Cash conversion failed. Net cash from operations (144.14) L against PAT 4,582.51 L. Working capital absorbed 5,863.23 L net (receivables and other assets (3,446.92), inventories +5,048.20, payables and provisions (7,464.51)). Cash and equivalents fell from 9,309.24 to 5,057.21 L. [INFERENCE] If the 3,417.80 L discount was settled as a credit against payables, it is a non-cash item inside operating profit of 7,352.54 L and an offsetting non-cash reduction in payables; underlying supplier payments would then be about 4,046.71 L (derived). The notes do not say. | Cash flow statement p.112; Note 36, p.146; L | 🔴 |
| 3 | Receivables ageing worsened at the old end. Over 6 months 1,582.37 L = 25.3% of gross 6,250.04 L (FY25 20.5%); 2-3 years 556.28 L and over 3 years 332.07 L barely moved from FY25 balances. Net receivable days 50.2 (FY25 33.3; FY24 97.6). ECL 905.47 L (14.5% of gross). Audit confirmations got no response. Main overdue payers are described as Public Sector and Government bodies. | Note 11, p.127-128; Note 32(A), p.141; KAM p.154; L | 🔴 |
| 4 | Accident accounting. 709.80 L of assets lost; insurance receivable stated as 609.80 L in text but 683.59 L on the face (73.79 L gap); 100.00 L loss and 520.00 L ex-gratia charged (620.00 L together). Claim unsettled at year end; auditor Emphasis of Matter. Notes name no plant, no licence status, no fines, no contingent liability; the Directors' Report (outside notes) records four deaths at Katepally on 29 Apr 2025. | Note 7(ii), p.125; Note 29, 29(d), p.138-139; EoM p.154; L | 🟡 |
| 5 | Revenue estimate softened. Variable consideration deducted from contract price fell to 5.99% (2,476.47 L) from 9.37% (4,316.26 L). At the FY25 rate revenue would be about 1,396 L lower (derived). The 500.00 L onerous-contract provision of FY25 was reversed into FY26 other income. Auditor made powder factor and variable consideration a KAM. The notes give no reason for the lower rate. | Note 21, p.133; Note 29(c), p.139; KAM p.154-155; L | 🟡 |
| 6 | Working-capital swing and supplier finance. Trade payables fell to 4,151.63 L from 11,654.90 L (payable days 88.5 vs 140.9); purchases fell 43.3%; WIP fell 60.4% while finished goods rose 88.9% against revenue down 7.0%. Supplier finance of 747.56 L (828.35 L) sits inside "loans from banks"; Note 15(e) has two sentences and no terms. Payable ageing does not roll (2-3 year bucket 457.12 L vs 8.36 L a year earlier). | Notes 10, 15(e), 36, p.126, 130, 146; L | 🟡 |
| 7 | Contingent liabilities 8,343.60 L (standalone) = 28.9% of net worth 28,903.17 L; bank LCs and guarantees 7,607.05 L (+28.0%). New GST claim 98.88 L. No forum, stage, assessment year or company view. Nothing on accident claims. | Note 34, p.145; Note 33, p.144; L | 🟡 |
| 8 | Promoter holdings moved to AKS Family Trust (41.33%, 2,22,21,735 shares) by 31 Mar 2026; promoters show nil direct. No date, consideration or related-party transaction disclosed. KMP pay up 30.5% (445.29 L) against revenue down 7.0%. Rate on KMP loans differs between standalone (8.95%) and consolidated (10%) notes. | Note 14(iii),(iv), p.129; Note 38, p.147-150; Note 37(g), p.201; L | 🟡 |
| 9 | Foreign exchange: net loss 591.64 L (FY25 2.53 L), 9.8% of PBT, against the statement that the company "is not significantly exposed" through natural hedging. Net unhedged liabilities 1,798.63 L; no hedges disclosed. Exports fell 34.1% to 5,168.78 L. | Note 29, p.138; Note 32(B), p.142-143; Note 21, p.133; L | 🟡 |
| 10 | Disclosure gaps that bear on valuation: no segment or product split, no contract assets or order book, no ECL matrix, no customer names for the 10% customer, no lease liability, no hedging, gratuity funded only 38.9% with salary growth set at 4% against 10.1% salary cost growth. Balance sheet is strong (net cash 2,314.50 L; covenants met), and going concern doubt is limited to the 6.63 L-negative PELNEXT subsidiary. | Notes 2.10, 4, 11, 21, 25(a), 32, 35, 43; L | 🟡 / 🟢 |

Pass 1 does not emit a YAML block. The B02-notes block comes from Pass 3.
