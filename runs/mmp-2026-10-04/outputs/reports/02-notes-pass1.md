# STAGE 2, PASS 1 of 3: NOTES TO FINANCIAL STATEMENTS, FULL EXTRACTION
Company: MMP Industries Ltd (MMP) | Run date: 2026-10-04 | Source: inputs/annual-report/Annual_Report_2026.txt (FY2025-26), comparatives from Annual_Report_2025.txt (FY2024-25)

## READING CONVENTIONS
- UNIT: every figure is INR Lakhs (L) as printed on the face of the AR ("Amount in Rs in Lakhs"). Nothing converted. Stage 10 converts once. "(derived)" means my arithmetic on printed figures, with inputs anchored.
- ANCHORS: "S" = standalone notes, "C" = consolidated notes. "p.N" = the "[page N]" marker in the .txt (PDF page). The printed AR page number is N minus 5 (checked: S balance sheet p.93 prints 88; C balance sheet p.171 prints 166).
- Notes read: S Notes 1 to 56 (p.99 to p.160), C Notes 1 to 59 (p.176 to p.244), plus the primary statements they tie to. The auditors' Key Audit Matter on the fire (p.~79 printed) was read only to confirm the note is audited; nothing else outside the notes is used.
- RATINGS: GREEN = clean, YELLOW = watch, RED = red flag (words used instead of icons).
- Statement of GROUNDING: items the AR does not disclose are written "NOT FOUND IN DOCUMENT".
- Corpus status carried from B00: CORPUS GAPPED. Gaps that touch this stage: scanned Q4/Q3 FY26 results not read here (notes pass uses the AR only); NSE clarifications of 2026-03-05 and 2026-06-23 have no company reply in the corpus; no ARFIN transcript; screener P&L/BS/CF CSVs empty. None of these change the AR-based extraction below. Full list is in the YAML block.

---------------------------------------------------------------
## LOAD-BEARING FACTS: CHECKED FIRST
### LBF1 FY26 guidance vs delivery (notes view)
- Guidance text itself: NOT FOUND IN DOCUMENT within the notes. The notes carry only the delivery side.
- Revenue: S 82,168.59 L vs 69,185.99 L, +18.77% (derived; S P&L p.94). C 82,400.49 L vs 69,185.99 L, +19.10% (C P&L p.172).
- EBITDA margin (derived, C, profit before exceptional and before associates + D&A + finance cost, so it includes other income of 133.17 L): FY26 = (4,159.15 + 1,134.25 + 1,333.31) = 6,626.71 L, 8.04% of 82,400.49 L. FY25 = (4,497.49 + 970.55 + 1,019.27) = 6,487.31 L, 9.38% of 69,185.99 L. Fall = 133 bps. This ties to the 133 bps in the brief. (C P&L p.172.)
- S view (derived): EBITDA incl. other income 7,045.18 L vs 6,550.50 L, +7.6% against revenue +18.8% (S P&L p.94).
- Where margin fell, per the C segment note (p.226): Aluminium Foils segment result 430.53 L on revenue 21,520.37 L = 2.0% (FY25 303.18 L / 15,441.20 L = 2.0%); Conductors 485.92 L on 9,997.96 L = 4.9% (FY25 799.53 L / 9,666.99 L = 8.3%); Powder and Paste 5,988.44 L on 50,403.67 L = 11.9% (FY25 5,422.66 L / 43,835.43 L = 12.4%); Insulators (329.13) L on 231.94 L; unallocated expenses 1,194.50 L (FY25 1,075.83 L).
- Note 43 ratio table (S p.145; C p.224) explains the fall in ROE, net profit ratio and ROCE by the fire. The ROCE definition there is "profit before interest, exceptional items and tax". An exceptional item cannot lower a ratio that excludes it. See Finding 9.

### LBF2 Umred incident, exceptional item, insurance claim
- Event: explosion and fire, Aluminium Powder Division, Umred plant, 11 April 2025, about 6:45 PM; "certain workmen" lost, "a few" injured (S Note 52, p.159; C Note 56, p.243). Number of deaths: NOT FOUND IN DOCUMENT.
- Gross loss: inventory 671.45 L + PPE 338.92 L + employee compensation and medical 661.64 L (net of debris disposal) = 1,672.01 L (S Note 52 p.159; S Note 37 p.136).
- Insurance claim receivable recognised: 793.05 L (47.4% of the gross loss, derived). Net loss shown as exceptional: 878.96 L (S Note 37 p.135; S Note 52 p.159). Both S and C identical.
- Balance sheet: "Insurance Claim Receivables" 793.05 L, nil last year, inside Other Current Financial Assets 929.51 L (S Note 14 p.122; C Note 14 p.200). That is 85.3% of the line and 14.1x S cash of 56.38 L (derived).
- Basis of recognition: "based on the final claim bill submitted to the insurance company and ... the amount considered recoverable by the management" (S Note 14 footnote, p.122; S Note 32 p.134). Insurer acceptance, surveyor report outcome and any interim payment: NOT FOUND IN DOCUMENT.
- Collection status: no receipt is shown in FY26. Opening balance nil, closing 793.05 L. Subsequent receipt: NOT FOUND IN DOCUMENT (no events-after-reporting-date note beyond the policy, S Note 1.4(t) p.112, and the proposed dividend).
- Date error: Note 14 footnote says the fire happened "on April 11, 2026" (S p.122; C p.200). Notes 32, 37 and 52 say April 11, 2025. April 2026 is after the year end, so this is a typo, but it sits in the note that carries the receivable.
- Where the loss sits in the P&L: "Goods destroyed due to fire" is removed from cost of materials (RM 17.87 L, PM 39.16 L; S Note 31 p.133-134) and from change in inventories (526.00 L; S Note 32 p.134). The three add to 583.03 L (derived) vs the 671.45 L inventory loss in Note 52. Gap 88.42 L (derived) NOT explained in the notes. Reported EBITDA is therefore before the direct fire loss. Lost production and sales during the shutdown stay in EBITDA. A business-interruption claim: NOT FOUND IN DOCUMENT.
- Size: exceptional items total 973.69 L = 21.0% of S profit before exceptional and tax of 4,641.82 L (derived). Fire net 878.96 L = 24.0% of 3,668.13 L PBT... see Finding 1 for the clean ratio: fire net / PBT before exceptional = 18.9% (derived).
- Second exceptional item: Past Service Cost (Gratuity) 94.73 L from the new Labour Codes effective 21 Nov 2025 (S Note 37 p.136). First occurrence; prior year nil.
- RATING: YELLOW. Loss recognition looks full. Recovery is booked at 47% of loss with no cash in and no insurer acceptance shown. Policy tension below.

### LBF3 Associates and promoter-group RPT
- Share of profit of associates: 820.78 L FY26 vs 613.67 L FY25, +33.7% (C P&L p.172). As a share of C PBT of 4,006.25 L = 20.5%; of PBT before associates 3,185.46 L = 25.8%; of C PAT 3,100.93 L = 26.5% (derived). FY25: 12.0% of PBT 5,111.17 L and 15.8% of PAT (derived).
- Split (C Note 46 p.234; Note 49 p.237-238): Star Circlips and Engineering Ltd 742.70 L (PY 567.93 L); Toyal MMP India Pvt Ltd 78.09 L (PY 45.74 L). Star is 90.5% of the line (derived).
- Cash received from associates: dividend from Star 9.98 L (PY 49.91 L) (S Note 30 p.133; S Note 45 p.154). That is 1.3% of the share of Star's profit (derived). Toyal paid no dividend (NOT FOUND in RPT table). Equity-method profit is non-cash to MMP.
- Associate holdings: Star 26.06% (9,98,260 shares, cost 97.83 L; C carrying 4,764.68 L); Toyal 26.00% (70,22,600 shares, cost 702.26 L; C carrying 645.98 L, below cost) (S Note 5 p.118; C Note 5 p.197; C Note 49 p.237-238).
- Cross-holding: Star Circlips holds 11,58,268 MMP shares (4.56%) and is listed as a promoter (S Note 16d p.124). MMP pays Star dividend 23.16 L and receives 9.98 L from it (S Note 45 p.153-154). Any elimination of MMP's share of Star's holding in MMP under equity accounting: NOT FOUND IN DOCUMENT.
- Auditors: reliance on other auditors for two associates stated in the C auditor report (p.170, "Other Matters"). Their opinion type: NOT FOUND IN DOCUMENT in the notes.
- Promoter-group RPT detail is in Section 2 below. Short form: Toyal sales 1,801.51 L = 2.19% of S revenue (PY 2.93%); promoter-family compensation and fees 255.21 L; promoter-entity collateral and personal guarantees support group debt.

### LBF4 Cash conversion, working capital, borrowings, funding of new-subsidiary capex
- S CFO 5,438.30 L (PY 5,530.99 L; FY24 4,275.02 L) (S CF p.95; AR2025 CF). The CFO includes "Increase in Short-Term Borrowings" of 789.11 L (PY 4,409.69 L; FY24 2,677.74 L). Working capital loans are a financing item. CFO excluding that line (derived): FY26 4,649.19 L; FY25 1,121.30 L; FY24 1,597.28 L.
- C CFO 5,328.97 L includes 1,723.34 L of short-term borrowing increase (C CF p.173). Excluding it: 3,605.63 L vs 1,252.33 L in FY25 (derived).
- CFO excluding borrowings as share of S EBITDA (derived): FY26 66.0% (4,649.19 / 7,045.18); FY25 17.1% (1,121.30 / 6,550.50); FY24 33.6% (1,597.28 / 4,756.10). Reported CFO / EBITDA: 77.2%, 84.4%, 89.9%.
- Working capital days on S revenue (derived): receivables 39.2 / 47.2 / 36.0 (FY26 / FY25 / FY24); inventory 69.4 / 71.1 / 70.0; trade payables 20.5 / 14.3 / 14.7. FY26 working capital days improved to 88.1 from 104.0 mainly because payables rose 70% (4,615.71 L vs 2,712.65 L) and receivables fell 1.4% on revenue +18.8%.
- Borrowings: S 15,163.24 L (PY 15,207.40 L), flat; C 18,452.46 L (PY 15,625.41 L), +18.1% (S Note 39B p.141-142; C Note 39B p.220). All the growth in group debt sits in the subsidiaries: term loans drawn MEPL 2,348.98 L of 2,800 L sanctioned and MCPL 512.70 L of 3,188 L sanctioned (C Note 18 p.205) = 2,861.68 L.
- Funding of subsidiaries by the parent (S CF p.95, Note 45 p.153, Note 5 p.118): equity into MEPL 400 L, MCPL 500 L, MAPL 25 L, plus 500 L of 7% preference shares in MEPL = 1,425 L cash in FY26 (investing outflow 1,425.00 L). Plus corporate guarantees 6,688 L (Note 47 p.157). Plus 3 subsidiaries run through parent-paid expense reimbursements (see Section 2).
- Capex commitments not provided: S 3,278.31 L (PY 350.75 L); C 5,642.27 L (PY 537.34 L) (S Note 48 p.157; C Note 52 p.241). Against S liquidity of 298.62 L (PY 1,276.79 L), which counts pledged deposits (S Note 39B p.141).
- Debt service cover (EBITDA / (finance cost + repayments)): S 3.29 vs 4.24; C 2.51 vs 4.55 (S Note 43 p.145; C Note 43 p.224). Current ratio S 1.29 vs 1.41; C 1.26 vs 1.39.
- Solar: Citi term loan for Shahpur solar, 60 L per quarter from March 2025 (S Note 18e p.127); Axis term loan covers factory and "solar power equipment" at Umred, 33.33 L instalments from Feb 2026 (S Note 18c p.127). A 7 MW, Rs 30 Cr captive solar plan from the brief: NOT FOUND IN DOCUMENT in the notes beyond these loans.
- Wire rod (MMP Cables) and insulators (MMP Electricals) are funded as above. Insulators segment capex 2,128.27 L in FY26 (C Note 44 p.227).

---------------------------------------------------------------
## 1. ACCOUNTING POLICIES AND CHANGES (S Note 1, p.99-115; C Note 1, p.176-194)
| Item | Finding | Anchor | Rating |
|---|---|---|---|
| Policy changes with P&L impact | None disclosed. Only new standards: Ind AS 21 amendment (May 2025) and Aug 2025 amendments to Ind AS 1, 7, 12; "no material impact". The Ind AS 7 supplier-finance disclosure is declared not material; supplier-finance balance NOT FOUND IN DOCUMENT. | S Note 1.2, 1.5 p.99, p.113 | GREEN |
| Revenue recognition | Point in time "generally upon dispatch ... or upon delivery" in the policy; "generally upon delivery" in Note 29. Variable consideration by expected value. Export incentives (drawback, RoDTEP 73.74 L) sit inside revenue. Rebates and discounts fell to 97.40 L from 381.41 L (0.12% of contract price vs 0.55%); reason NOT FOUND IN DOCUMENT. | S Note 1.4(d) p.103; Note 29 p.132-133 | YELLOW |
| Depreciation lives vs norm | Straight line. Factory building 30 y, other building 60 y, plant and machinery "including continuous process plant" 25 y, office equipment 10 y, furniture 10 y, electrical 10 y, vehicles 8 y, computers 3 y. The company states some lives differ from Schedule II. Plant at 25 y and office equipment at 10 y are at the long end. No change in lives disclosed. | S Note 1.4(a) p.101 | YELLOW |
| Capitalisation | Policy allows administrative, financing and general overhead directly attributable to construction to be capitalised. Capitalised interest amount: NOT FOUND IN DOCUMENT. C CWIP carries "Pre-Operative Expenditures" 210.64 L (PY 56.59 L). | S Note 1.4(a),(o) p.100-101, p.110; C Note 4 p.197 | YELLOW |
| Impairment | Generic. No CGU assumptions, growth or discount rate given. Investments in subsidiaries carried at cost with nil impairment while MEPL shows a net deficit (C Note 50 p.239). | S Note 1.4(c) p.102; Note 5.1 p.119 | YELLOW |
| ECL | Simplified approach, provision matrix keyed to >365 days and collection % (matrix is described in words, no rates). | S Note 1.4(g) p.106; Note 39B p.141 | GREEN |
| Leases | Policy still reads as finance/operating lessee (Ind AS 17 wording). Leasehold land carried as PPE under Ind AS 16 (S Note 1.6(g) p.115). Right-of-use assets, lease liability, discount rate: NOT FOUND IN DOCUMENT. Rent, rates and taxes 106.43 L (PY 57.60 L, +84.8%). | S Note 1.4(n) p.109; Note 36 p.135 | YELLOW |
| Hedge accounting | Policy says fair value hedge of foreign currency financial liabilities (p.107). The equity reserve is "Cash Flow Hedge Reserve" (7.57) L (p.98). Note 39B says the company "has not entered into any hedging arrangements" (p.140) while Note 51 shows forwards to sell USD 5.76 and EUR 13.68 (Rs 1,979.34 L) and Note 25 shows forward contract payable 57.02 L. See Finding 10. | S Note 1.4(h) p.107; Note 39B p.140; Note 51 p.158 | YELLOW |
| Contingent assets | Policy 1.4(r) says contingent assets are "disclosed where an inflow is probable"; key judgement 1.6(d) says contingent assets are "neither recognised nor disclosed". An insurance receivable is booked on a claim bill. See LBF2. | S Note 1.4(r) p.112; Note 1.6(d) p.114 | YELLOW |
| Cash flow policy | Policy 1.4(u) says cash flow adjusts profit "excluding exceptional items". The statement starts from PBT after exceptional items (3,668.13 L). | S Note 1.4(u) p.112-113; CF p.95 | YELLOW |
| Key estimates | Tax, PPE lives, fair value, provisions, impairment, deferred tax, leasehold land, receivable recoverability, defined benefit. No sensitivity beyond gratuity. | S Note 1.6 p.114-115 | GREEN |
| Subsidiary and associate policy (C) | Subsidiaries line by line; associates by equity method; same lives and policies as parent. | C Note 1.2 p.177-178 | GREEN |

## 2. RELATED PARTY TRANSACTIONS (S Note 45, p.150-155; C Note 46, p.232-235)
Related parties (S p.150-151): subsidiaries MMP Electricals (MEPL), MMP Cables (MCPL, new), MMP Alutech (MAPL, new), all 100%; associates Star Circlips 26.06%, Toyal MMP India 26.00%; promoter-linked companies Mayank Fasteners Pvt Ltd, Rohini Farms and Agriculture Pvt Ltd; KMP and relatives. New related parties this year: MCPL and MAPL, Ms. Rohini Bhandari joined as non-executive director 8 Aug 2025, Sachin Nirgudkar joined 8 Aug 2025 (Karan Verma retired same day).

### 2a Transaction table, standalone (L)
| Party and relationship | Nature | FY26 | FY25 | YoY | Anchor |
|---|---|---|---|---|---|
| Toyal MMP India (associate) | Sales of goods | 1,801.51 | 2,027.19 | -11.1% | S p.152 |
| Toyal MMP India | Purchases | NIL | 4.52 | | S p.151 |
| Star Circlips (associate) | Job work receipts | 277.06 | 262.49 | +5.6% | S p.152 |
| Star Circlips | Purchases | 1.49 | 3.68 | -59.5% | S p.151 |
| Star Circlips | Dividend income | 9.98 | 49.91 | -80.0% | S p.154 |
| Star Circlips | Dividend paid to it (holds 4.56% of MMP) | 23.16 | 17.37 | +33.3% | S p.153 |
| MEPL (WOS) | Reimbursement of expenses incurred by MMP | 192.49 | 553.85 | -65.2% | S p.152 |
| MEPL | Repayment of reimbursement | 312.46 | 325.00 | | S p.152 |
| MCPL (WOS, new) | Reimbursement incurred / repaid | 1,139.54 / 667.79 | NIL | new | S p.152 |
| MAPL (WOS, new) | Reimbursement incurred | 3.60 | NIL | new | S p.152 |
| MAPL | Unsecured loan received / repaid by MMP | 24.00 / 20.40 | NIL | new | S p.152-153 |
| MEPL | Loans granted / repaid | 125.00 / 125.00 | 285.00 / NIL | | S p.153 |
| MCPL | Loans granted / repaid | 90.00 / 90.00 | NIL | new | S p.153 |
| MEPL | Equity investment | 400.00 | 100.00 | | S p.153 |
| MCPL / MAPL | Equity investment | 500.00 / 25.00 | NIL | new | S p.153 |
| MEPL | 7% preference shares | 500.00 | NIL | new | S p.153 |
| MEPL, MCPL | Services offered | NIL / 5.92 | 6.12 / NIL | | S p.153-154 |
| Mayank Fasteners Pvt Ltd (promoter co.) | Office rent paid | 3.00 | 0.90 | +233% | S p.151 |
| Mayank Fasteners; Rohini Farms | Dividend paid | 95.69; 2.48 | 71.77; 1.86 | +33% | S p.153 |
| Arun Bhandari (MD) | Remuneration | 134.40 | 134.40 | 0% | S p.151 |
| Lalit Bhandari (WTD) | Remuneration | 35.13 | 35.37 | | S p.151 |
| N. M. Tenneti (WTD), S. Khandelwal (CFO), M. Singh (CS) | Remuneration | 23.69; 31.71; 10.67 | 23.68; 31.64; 10.36 | | S p.151 |
| Saroj Bhandari (wife of MD) | Salary and perquisites | 61.98 | 61.98 | 0% | S p.151 |
| Sakshi Bhandari (wife of non-exec director) | Salary and perquisites | 25.83 | 25.78 | | S p.152 |
| Rohini Bhandari (non-exec director) | Legal and professional charges | 30.00 | 30.00 | 0% | S p.152 |
| Independent directors | Sitting fees | 9.05 total | 7.75 | +16.8% | S p.152; Note 36 p.135 |
| Promoter family and entities | Dividends paid (9 holders) | 378.43 | (derived) | | S p.153 |

Dividend check (derived): promoter group 74.48% x 508.05 L = 378.4 L, which ties to the nine promoter holders in the table.

### 2b Closing balances, standalone (L) (S p.154-155)
Trade receivable from Toyal 3.45 (PY 43.77). Remuneration payable: Arun 5.46, Lalit 1.60, Tenneti 0.97, Khandelwal 1.03, Singh 0.82, Saroj 2.77, Sakshi 1.30. Sitting fees payable 2.66. Legal and professional payable to Rohini 2.25. Investment balances: MEPL 500, MCPL 500 ("net of corporate guarantee liabilities"), MAPL 25, Toyal 702.26, Star 97.83. Preference shares MEPL 500. Guarantees: MEPL 3,400, MCPL 3,288.

### 2c Ratios and signals
- Toyal sales 1,801.51 L = 2.19% of S revenue (PY 2.93%) (derived). Toyal's own cost of materials is 5,923.51 L (C Note 49 p.238), so MMP supplies about 30% of it (derived).
- Star job work 277.06 L is 84.4% of S services revenue 328.40 L (derived; S Note 29 p.132).
- Compensation and fees to promoter family and entities, excluding dividends: Arun 134.40 + Saroj 61.98 + Sakshi 25.83 + Rohini 30.00 + Mayank Fasteners rent 3.00 = 255.21 L (derived) = 5.5% of S profit before exceptional and tax. Including professional KMP pay (Lalit, Tenneti, Khandelwal, Singh) and sitting fees, all KMP and relative payments are 365.46 L (derived).
- Arm's-length: the notes assert terms "equivalent to those applicable to unrelated parties" (S p.151). No pricing method, no benchmark, no audit-committee approval reference. Role of Saroj and Sakshi Bhandari: NOT FOUND IN DOCUMENT.
- No royalty to promoters. No loan to promoters or directors (S Note 6 p.119; Note 8 p.120; Note 13 p.121-122).
- Guarantee commission: only a notional 8.28 L credit in other income from subsidiaries (S Note 30 p.133).
- Promoter support to group debt: personal guarantees by Arun and Lalit Bhandari on parent term loans and working capital (S Note 18 p.126-127; Note 23 p.129-130); by Arun and Mayank Bhandari on MEPL and MCPL (C Note 18l p.205). MEPL's HDFC facility is also secured by a commercial property in Shri Mohini Complex "held in the name of Mayank Fasteners Private Limited" (C Note 18f p.205). Fees for these guarantees: NOT FOUND IN DOCUMENT.
- Loans from promoters: C only. MEPL took 280.00 L from Arun Bhandari (150.00 L) and Mayank Bhandari (130.00 L), unsecured, interest free, repayable on demand (C Note 23h p.209; Note 46 p.234-235). This supports the subsidiary at no cost.
- Parent loan from related parties 30.00 L, unsecured, repayable on demand, shown as non-current (S Note 18 p.126). The lender is NOT FOUND in the RPT balance table (S p.154-155). A demand loan shown as non-current is also a classification question.
- Unreconciled subsidiary balances (derived): MEPL reimbursement: PY closing receivable 228.85 L + FY26 incurred 192.49 L - repaid 312.46 L = 108.88 L, but the FY26 closing balance is NIL (S p.155; Note 14 p.122). MCPL: 1,139.54 L - 667.79 L = 471.75 L, no closing balance shown. Total about 580.63 L not visible as a balance (MAPL's 3.60 L nets against its loan flows). Possible conversion into equity is not stated. YELLOW.
- Name inconsistency: dividend table lists "Rohini Horticulture Private Limited" (S p.153; C p.234 uses "Rohini Farms and Agriculture"); "Mayank Fasteners" vs "Mayank Fastners" in Note 16 (p.123). C Note 46 heads the associates as "Wholly Owned Subsidiary Company (WOS)" (p.232). Clerical.
- New C related-party items vs S: share of associate profit and OCI; directors' loans to MEPL.
- RATING: YELLOW. Scale is small (compensation 0.4% of revenue) and governance disclosure is thin.

## 3. CONTINGENT LIABILITIES (S Note 47, p.156-157; C Note 51, p.241)
| Item | FY26 | FY25 | Stage / assessment | Anchor |
|---|---|---|---|---|
| Bank guarantees for MSEDCL deposits and others | 445.72 | 413.13 | Backed by term deposits 445.72 L (Note 14) | S p.157, p.122 |
| Bills discounted under LC | NIL | 104.43 | Closed | S p.157 |
| Corporate guarantee, MEPL (HDFC Bank) | 3,400.00 | 3,400.00 | In force | S p.157 |
| Corporate guarantee, MCPL (Kotak Mahindra Bank) | 3,288.00 | NIL | In force, new | S p.157 |
| TOTAL | 7,133.72 | 3,917.57 | FY24 590.41 | S p.157; AR2025 |

- Total = 23.5% of S net worth of 30,403.36 L (derived; S BS p.93). Guarantees alone 6,688.00 L = 22.0%. MEPL guarantee = 11.2% and MCPL guarantee = 10.8% of net worth: each is above 10% (derived).
- The notes say "an amount of 3,400.00 L ... remains outstanding" under MEPL's facilities and "3,288.00 L ... outstanding" under MCPL's (S p.157). The C notes show MCPL has drawn only 512.70 L of a 3,188 L term loan (C Note 18k p.205). The 3,288 L figure looks like sanctioned limits (term 3,188 + 100), described as "outstanding". Drawn working-capital lines at MCPL: NOT FOUND IN DOCUMENT.
- Corporate guarantee liability recognised at fair value 58.60 L (PY 34.00 L) (S Note 19 p.126). It was also added to the carrying value of the investments: 66.88 L (MEPL 34.00 L, MCPL 32.88 L) less 8.28 L notional commission = 58.60 L (derived; S Note 5 p.118; Note 30 p.133). Reconciles.
- Tax, GST, customs and legal disputes: none disclosed, "NOT FOUND IN DOCUMENT". No contingent liability for the fire (workmen compensation, legal claims, factory-act proceedings): NOT FOUND IN DOCUMENT.
- Associates' contingent liabilities: Star nil. The Toyal paragraph repeats the sentence about "Star Circlips" (C Note 49 p.238), so Toyal's contingent liabilities are NOT FOUND IN DOCUMENT.
- C contingent liabilities 445.72 L = 1.3% of C net worth 34,650.78 L, after eliminating intra-group guarantees (C p.241).
- Contingent assets: none disclosed (see Section 1).
- Derivative commitments 1,979.34 L = forward cover (USD 522.15 L + EUR 1,457.19 L) (S Note 48 p.157; Note 51 p.158) (derived tie).
- RATING: YELLOW. Size is real, two items each exceed 10% of net worth, and the wording on "outstanding" is loose.

## 4. TRADE RECEIVABLES (S Notes 11, 41, 39B; C Notes 11, 41)
Ageing S, gross 8,886.02 L (FY26) vs 8,999.20 L (FY25) (S Note 41 p.143):
| Bucket | FY26 | % | FY25 | % |
|---|---|---|---|---|
| Not due | 8,554.23 | 96.3% | 8,357.52 | 92.9% |
| Under 6 months | 226.90 | 2.6% | 609.65 | 6.8% |
| 6 months to 1 year | 78.53 | 0.9% | 1.80 | 0.0% |
| 1 to 2 years (doubtful) | 26.36 | 0.3% | 30.24 | 0.3% |
| Over 2 years | NIL | | NIL | |
- Over 6 months total 104.89 L = 1.18% of gross (FY25 32.04 L = 0.36%) (derived). Disputed dues: none. Unbilled: none (p.143).
- Net receivables 8,822.61 L vs 8,951.34 L: down 1.4% while S revenue rose 18.8%. C net 8,884.99 L (C Note 11 p.199; ageing p.222).
- Receivable days (derived, on S revenue): FY26 39.2; FY25 47.2; FY24 36.0 (FY24 receivables 5,706.17 L, AR2025 BS; revenue 57,854.35 L, AR2025 P&L). Credit period 30 to 60 days (S Note 39B p.140). Note 43 turnover 9.25x vs 9.44x (S p.145).
- Concentration: "No customer represents more than 10% of the total trade receivables balance" (S Note 39B p.140). Customer share of revenue: NOT FOUND IN DOCUMENT (S has no segment note; C Note 44 gives none).
- ECL: allowance on trade receivables 63.41 L (0.7% of gross) (S Note 11 p.121). Total ECL pool 346.61 L = 63.41 L trade + 283.19 L on non-current "Other Receivables" (S Note 7 p.120; Note 39B p.141). Movement: opening 277.80 + charge 68.81 L - write-off nil = 346.61 L. Note 39B prints the charge as 69.81 L, which would not add up (clerical, S p.141). FY25 write-off 82.80 L.
- Non-current "Other Receivables" 703.86 L (PY 700.86 L) carry a 283.19 L allowance (40.2%; PY 229.93 L, 32.8%) (S Note 7 p.120). Debtor identity, age and nature: NOT FOUND IN DOCUMENT. Allowance rose 53.26 L in the year (derived). YELLOW.
- Receivables from related parties: Toyal 3.45 L (PY 43.77 L) (S Note 11 p.121). Falls to near nil.
- Factoring or receivable discounting: bills discounted under LC fell to NIL from 104.43 L (S p.157). Other receivable financing: NOT FOUND IN DOCUMENT.
- RATING: GREEN on ageing and ECL for trade debtors. YELLOW on the 703.86 L other receivable.

## 5. INVENTORY (S Note 10, p.120; Note 32, p.134; C Note 10, p.199)
| Category | FY26 | FY25 | YoY |
|---|---|---|---|
| Finished goods | 2,956.75 | 3,711.73 | -20.3% |
| Work in progress | 6,713.37 | 5,927.18 | +13.3% |
| Raw material | 5,356.24 | 3,190.68 | +67.9% |
| Packing material | 141.85 | 183.40 | -22.7% |
| Stores, spares, consumables | 447.58 | 456.77 | -2.0% |
| Trading stock | 0.78 | 2.40 | -67.5% |
| TOTAL | 15,616.57 | 13,472.16 | +15.9% |
- Total inventory grew 15.9% against revenue +18.8%. Finished goods fell 20.3% while revenue rose, partly because 526.00 L of goods were destroyed (Note 32). Raw material rose 67.9% against purchases +23.0% (66,836.99 L vs 54,321.18 L, S Note 31 p.133). The notes give no reason (price or stock-up). NOT FOUND IN DOCUMENT.
- Write-down to NRV: NIL both years (S Note 10 p.120). Valuation: weighted average, lower of cost and NRV, item by item (S Note 1.4(f) p.103).
- Inventory days (derived, on S revenue): 69.4 (FY26), 71.1 (FY25), 70.0 (FY24; inventory 11,099.96 L). Note 43 turnover 4.91x vs 4.83x (S p.145).
- Obsolete or slow-moving: policy exists; provision amount NOT FOUND IN DOCUMENT.
- C inventory 15,809.91 L (+192.34 L vs S, in subsidiaries) (C p.199).
- RATING: GREEN on days and write-offs. YELLOW watch on raw material build with nil NRV test disclosure.

## 6. INVESTMENTS (S Notes 5, 6, 13; C Notes 5, 48 to 50)
| Entity | % | Cost / carrying (S) | C carrying | Note |
|---|---|---|---|---|
| MMP Electricals Pvt Ltd (insulators) | 100% | 534.00 (PY 134.00); 50,00,000 shares | n/a (consolidated) | Plus 500.00 L 7% non-cumulative preference, redeemable at par 9 Mar 2031, allotted 9 Mar 2026 (S p.118) |
| MMP Cables Pvt Ltd (wire rod) | 100%, new | 532.88 (PY nil) | n/a | S p.118 |
| MMP Alutech Pvt Ltd | 100%, new | 25.00 (PY nil) | n/a | S p.118 |
| Star Circlips and Engineering Ltd | 26.06% | 97.83 | 4,764.68 (PY 4,200.29) | C p.197 |
| Toyal MMP India Pvt Ltd | 26.00% | 702.26 | 645.98 (PY 567.52) | C p.197 |
| TOTAL S | | 2,391.97 (PY 934.09) | C 5,410.66 | |
- Subsidiary carrying values include deemed investment from guarantees, 34.00 L (MEPL) and 32.88 L (MCPL) (S Note 5 footnote p.118). Preference shares are described as "cost" in policy (S Note 1.4(k) p.108) but classified "amortised cost" in Note 5.4 (p.119). Policy mismatch.
- Impairment: nil (S Note 5.1 p.119). No indicator test shown for MEPL, which lost 337.37 L in FY26 and shows a deficit (C Note 50 p.239).
- Loss-making subsidiaries (C Note 50, p.239): MEPL (337.37) L, MCPL (12.22) L, MAPL (3.22) L; total 352.81 L (derived). FY25 MEPL (10.34) L. The Insulators segment lost 329.13 L on revenue of 231.94 L (C Note 44 p.226).
- Net assets as shown in the Schedule III table are negative for MEPL (347.72) L and Toyal (702.25) L; the table appears to deduct cost, so read it as post-cost reserve movement (C p.239). Toyal's balance sheet equity is positive at 2,484.54 L (C p.238).
- ICDs and loans: MEPL 125.00 L and MCPL 90.00 L advanced and repaid within the year; closing NIL (S Note 53 p.159); on demand, unsecured. Section 186 totals: loans given 215.00 L, guarantees 6,688.00 L, investments made 2,325.09 L (S p.160).
- Associates, key figures (C Note 49 p.237-238):
  - Star: revenue 19,301.14 L (+16.1%), PBT 3,880.07 L (20.1% margin), PAT 2,849.67 L, employee cost 4,348.95 L (+28.6%), equity 18,281.73 L. Carrying 4,764.68 L = 26.06% of equity.
  - Toyal: revenue 7,434.19 L (+22.0%), PBT 408.90 L (5.5%), PAT 300.33 L, equity 2,484.54 L. Current liabilities 4,698.45 L (PY 1,480.80 L) against current assets 3,690.62 L; non-current liabilities fell to 35.02 L from 2,586.25 L. About 2,551 L of long-term liabilities moved into current (derived). Reason and maturity: NOT FOUND IN DOCUMENT. Toyal current ratio 0.79 (derived).
- Classification: C notes call the associates "measured at costs" (C Note 5 p.197) and "amortized costs" (C Note 38 p.215), though accounting is by equity method. Clerical.
- RATING: YELLOW (associate profit is large, cash-light and rises with a leveraged-up Toyal; subsidiaries lose money).

## 7. BORROWINGS (S Notes 18, 23, 39B, 39C; C Notes 18, 23)
Instrument table, standalone (L):
| Instrument | FY26 | FY25 | Terms / security | Anchor |
|---|---|---|---|---|
| Non-current term loans (banks) | 1,949.35 | 2,782.62 | Axis, Citi: first pari-passu on PPE, mortgages on Bhandara, Mohadi, Hingna land; personal guarantees of Arun and Lalit Bhandari | S p.126-127 |
| - Axis COVID term loan | | | EMI 18.17 L monthly from Mar 2024, ends Mar 2027 | S p.126 |
| - Axis loan for Umred factory and solar | | | 33.33 L from Feb 2026 to Jan 2031 ("monthly" in S, "quarterly" in C) | S p.127; C p.204 |
| - Citi solar loan, Shahpur | | | 60.00 L per quarter from Mar 2025; ends "December 2028" in S, "March 2028" in C | S p.127; C p.204 |
| Unsecured loan from related parties | 30.00 | 30.00 | Repayable on demand, shown non-current | S p.126 |
| Short-term, secured (cash credit, WC) | 9,348.06 | 8,957.69 | Pari-passu on current assets; same mortgages | S p.129-130 |
| Export packing credit | NIL | 403.20 | | |
| Short-term unsecured WC (incl. Shinhan, Federal, PBF) | 2,996.00 | 2,509.23 | PBF 9.05%; Shinhan 7.55% in S, 7.25% in C | S p.130; C p.209 |
| Current maturities of term loans | 839.83 | 524.67 | | S p.129 |
| TOTAL | 15,163.24 | 15,207.40 | | S p.141-142 |
- Mix: variable 12,344.05 L (81.4%), fixed 2,819.18 L (S p.139). Interest sensitivity at 70 bps is printed 106.14 L, which equals 70 bps on total borrowings 15,163 L, not on the variable book of 12,344 L (derived; S p.139). Gross interest on bank borrowings 1,199.38 L = about 7.9% on average borrowings (derived).
- Finance cost 1,303.14 L, +27.8% (S Note 34 p.134-135). "Other interest expenses" 100.07 L (PY 76.08 L): nature NOT FOUND IN DOCUMENT.
- Covenants: "complied with all covenants ... throughout" (S Note 39C p.142). No breach, waiver or term change disclosed. Covenant terms: NOT FOUND IN DOCUMENT. No default on principal or interest (S Note 46 p.156).
- Five-year repayment schedule: NOT FOUND IN DOCUMENT in the contractual form. Liquidity table shows <1 year 13,183.89 L and 1 to 5 years 1,979.35 L, nothing beyond (S p.141-142). Current maturities in the next 12 months 839.83 L.
- Security: pledged term deposits 2,000 L with Federal Bank against borrowings (S Note 7 p.120) and 445.72 L against bank guarantees. Total deposits pledged and treated as "liquidity" 298.62 L figure includes them (S p.141). Note: Note 7 text says deposits of 113.16 L back 2,000 L of borrowings; these amounts do not match (113.16 vs 2,000). NOT FOUND IN DOCUMENT how 2,000 L is covered.
- Capital management note: "has a low level of debt" (S p.142). Its "Net Debt" is Total Liabilities less cash: 24,522.69 L, ratio 0.81x (PY 0.74x). That is a liabilities-to-equity ratio, not net debt. Actual borrowings less cash: 15,106.86 L, 0.50x (derived; Note 43 D/E 0.50 vs 0.54).
- Related party borrowings: S 30.00 L; C adds 280.00 L directors' loans at MEPL (C p.209).
- C borrowings 18,452.46 L: non-current 4,317.62 L; current 14,134.83 L; MEPL HDFC term loan 2,348.98 L drawn of 2,800 L; MCPL Kotak 512.70 L drawn of 3,188 L (C Note 18 p.205). C D/E 0.53; net debt / EBITDA 2.75x vs 2.24x (derived: (18,452.46 - 196.52) / 6,626.71; (15,625.41 - 1,095.22) / 6,487.31). C interest cover on EBIT before associates: 4.12x vs 5.41x (derived).
- Rating of the company: capital management text states BBB+ stable domestic rating target (S p.142). Rating agency detail is outside the notes.
- RATING: YELLOW. No default, but debt cost and group debt rise while cash is thin.

## 8. TRADE PAYABLES (S Notes 24, 42; C Notes 24, 42)
- Total S 4,615.71 L vs 2,712.65 L, +70.2%. MSME 874.78 L (PY 833.86 L). Others 3,740.93 L vs 1,878.78 L (+99.1%) (S p.130).
- Ageing: not due 4,542.84 L (98.4%); under one year 63.14 L; 1 to 2 years 9.73 L; none beyond (S Note 42 p.143). Last year not due 2,496.42 L (92.0%), under one year 213.89 L, 1 to 2 years 2.34 L. No disputed dues. No unbilled dues.
- MSME dues past 45 days and interest: "interest due ... NIL", "principal paid beyond stipulated day NIL" (S p.130). One MSME bucket of 1.52 L was under one year last year, none this year. GREEN. The MSME identification relies on management information (p.130).
- Acceptance arrangements: NIL (p.130). Purchase Bill Financing is shown inside borrowings at 9.05% (S Note 23f p.130); the amount is NOT FOUND IN DOCUMENT.
- Payable days (derived, on S revenue): 20.5 (FY26), 14.3 (FY25), 14.7 (FY24). Note 43 payable turnover 18.75x vs 22.39x (S p.145). Note 43 shows the same direction (days longer).
- Other payables: capital creditors 148.56 L (PY 456.59 L), liabilities for expenses 692.47 L (PY 411.93 L), liabilities towards services 391.01 L, payable towards indirect tax 82.63 L (PY 279.90 L) (S Note 25 p.131).
- C trade payables 4,622.21 L (C p.209).
- RATING: GREEN on ageing and MSME. The 70% rise is a working capital finding (Section 4 cross reference and LBF4).

## 9. PROVISIONS AND EMPLOYEE BENEFITS (S Notes 21, 27, 44; C Notes 21, 27, 45)
- Warranty, decommissioning, onerous contract, litigation provisions: NONE disclosed. NOT FOUND IN DOCUMENT.
- Only provisions: gratuity and leave encashment. S non-current 483.95 L (PY 291.23 L); current 215.01 L (PY 136.73 L) (S p.129, p.131).
- Gratuity: unfunded; plan assets nil; present value of obligation 611.39 L vs 349.40 L (+75.0%) (S Note 44 p.146). Movement: opening 349.40 + interest 23.10 + current service 42.27 + past service 94.73 - benefits paid 46.12 + actuarial loss 148.01 = 611.39 L. Actuarial split: financial assumptions (103.96) L gain; experience loss 251.97 L (PY 23.42 L) (p.146). OCI charge 148.01 L pre-tax.
- Labour Code past service cost 94.73 L taken as exceptional (S Note 37 p.136). The experience loss 251.97 L went to OCI.
- Valuation data (p.147): employees 565 (PY 523, +8.0%); total monthly salary 97.86 L (PY 58.02 L, +68.7%); average monthly salary 0.17 L vs 0.11 L. The P&L salary line rose only 6.4% (4,302.80 L vs 4,044.49 L) (S Note 33 p.134). The notes do not explain the jump in the valuation salary base. NOT FOUND IN DOCUMENT.
- Assumptions (p.148): discount rate 7.00% (PY 6.61%); salary growth 5.00%; mortality IALM 2012-14; withdrawal 15% / 5% / 2% by age band. Weighted duration 6 years. Sensitivity 1%: discount -4% / +5%, salary +5% / -4% (p.149).
- Maturity: next 12 months 190.25 L (31.1% of obligation) vs 116.33 L; then 60.92, 51.92, 57.80, 40.07 L; beyond 210.42 L (S p.149). Expected contribution next year 54.15 L although plan assets are nil; the text says the plan "requires contributions to a separately administered fund" while the table says unfunded (p.145-146, p.148). Inconsistent.
- Pension and post-retirement medical plans are described (p.146) but no separate numbers appear: NOT FOUND IN DOCUMENT.
- Cross-note slips: S Note 27 shows PY gratuity current 74.48 L; Note 44 and C Note 27 show 116.33 L (the S total 136.73 L only ties with 116.33 L) (S p.131, p.148). Leave encashment liability 31.33 L (Note 44 p.150) vs balance sheet 87.58 L (62.81 L + 24.77 L; PY 78.55 L vs 27.57 L). Unreconciled.
- Provident fund: defined contribution; employer 148.32 L (PY 133.96 L); "no shortfall" (S p.150).
- RATING: YELLOW. Unfunded and up 75%. Labour Code change is real but small in rupees. Inconsistent note details.

## 10. DEFERRED TAX AND TAX (S Note 20, p.127-128; C Note 20, p.206-207)
- Tax expense S 1,025.19 L on PBT 3,668.13 L = 27.95% effective vs 25.168% statutory (FY25 26.90%) (derived). Current 715.68 L; deferred 309.51 L.
- Reconciliation (S p.128): tax at 25.168% = 923.20 L; "non-deductible expenses" 111.79 L (PY 19.44 L), which implies about 444.2 L of disallowed expense (derived). The nature is NOT FOUND IN DOCUMENT. CSR is 68.60 L; the fire compensation of 661.64 L may be involved but the note does not say. FY25 had a land base item 85.36 L (nil in FY26).
- Deferred tax liability S 1,825.20 L (PY 1,555.48 L), mostly PPE written-down value difference 2,084.64 L, offset by allowances and provisions (S p.128). C DTL 1,701.84 L (C p.207).
- Deferred tax asset on subsidiary tax losses: 125.62 L recognised (PY 1.82 L); FY26 credit 123.81 L (C p.207). The note says the asset is recognised "to the extent probable" but gives no evidence of future profit at MEPL, which shows a FY26 loss of 337.37 L. YELLOW.
- MAT credit: NOT FOUND IN DOCUMENT (company on 25.168% regime). Unrecognised DTA: NONE disclosed.
- Current tax: payable 715.11 L less advance tax 550.00 L less TDS 53.10 L less TCS 0.20 L = net liability 111.80 L (S Note 28 p.131). Tax paid in cash flow 623.71 L.
- C effective rate on PBT before associates: 905.32 L / 3,185.46 L = 28.4% (derived). Share of associate profit is taken post-tax.
- RATING: YELLOW (the disallowed expense and the loss DTA are unexplained).

## 11. REVENUE DETAILS (S Note 29, p.132-133; C Note 29, p.211-212; C Note 44, p.224-227)
| Disaggregation (S, L) | FY26 | FY25 | YoY |
|---|---|---|---|
| Aluminium Powder and Paste | 50,403.54 | 43,793.05 | +15.1% |
| Aluminium Foils | 21,520.37 | 15,417.53 | +39.6% |
| Aluminium Conductors | 9,997.96 | 9,666.99 | +3.4% |
| Others | 246.73 | 308.42 | -20.0% |
| TOTAL | 82,168.59 | 69,185.99 | +18.8% |
- Mix FY26 (derived): powder and paste 61.3%, foils 26.2%, conductors 12.2%. C adds Insulators 231.91 L (first revenue; C p.211).
- Geography: domestic 77,923.52 L (+17.1%); export 3,836.87 L (+66.8%), 4.7% of revenue (S p.132). Export 40-50% growth is the FY27 guide in the brief; the notes show FY26 +66.8% from a small base.
- Contract price 82,192.26 L less rebates and discounts 97.40 L = 82,094.85 L, plus export incentives 73.74 L (S p.132-133). Rebates fell 74% (381.41 L in FY25).
- Contract assets and liabilities: advances from customers 268.86 L (PY 269.33 L) (S Note 26 p.131). No contract assets. No remaining performance obligations (short contracts) (p.133).
- Top customer revenue: NOT FOUND IN DOCUMENT.
- Segment (C Note 44 p.224-227): five segments (Powder and Paste, Foils, Conductors, Insulators, Others). Segment results L: 5,988.44; 430.53; 485.92; (329.13); 111.20; total 6,686.96 (PY 6,592.59). Segment assets L: 32,473.91; 13,511.96; 3,541.78; 3,489.42; 1,101.65. Capex L: 1,570.86; 35.47; 583.04; 2,128.27; nil; plus unallocated 597.22; total 4,914.87 (PY 5,066.81). Standalone segment note: NOT FOUND IN DOCUMENT (company-level only).
- Revenue growth by segment vs segment result growth: Foils revenue +39.6% and segment result +42.0% at a 2.0% margin. Conductors revenue +3.4% and result -39.2%.
- RATING: YELLOW (lower rebates and thin segment margins in foils and conductors).

## 12. OTHER CRITICAL NOTES
### 12a Exceptional items and recurrence
Both items are first-time: fire net 878.96 L and Labour Code past service cost 94.73 L; FY25 nil (S Note 37 p.135-136). Total 973.69 L. No history of recurrence in the notes. Fire note: see LBF2. RATING: YELLOW.

### 12b PPE, CWIP, capital commitments (S Notes 2 to 4, 40, 48; C same)
- PPE net 23,825.88 L (PY 22,042.52 L). Additions 3,336.76 L (plant 1,577.88; factory building 1,208.50; freehold land 307.01; leasehold land 60.67) and deductions 595.77 L (factory building 383.41; plant 175.43) (S p.116). Depreciation 1,093.12 L on average gross block 27,229 L = 4.0% (derived).
- Table slip: the Factory Building closing cost shows 8,134.36 L, which is the opening cost, while additions and deductions imply 8,959.45 L; the net carrying value 7,611.89 L only ties to 8,959.45 L (derived; S p.116). Clerical.
- Title deeds in company name (p.117). The note says gross block "regrouped and netted ... deemed cost exemption opted out" (p.117), which reads oddly and is unexplained.
- Intangibles: software fully amortised, net nil (S Note 3 p.117).
- CWIP S 1,708.46 L (PY 2,258.62 L): under one year 1,021.44 L; one to two years 687.02 L; no suspended projects; no overdue or over-budget projects (S Note 40 p.142-143). C CWIP 3,832.49 L incl. pre-operative 210.64 L (C p.197; ageing p.221).
- Capital advances S 595.98 L (PY 198.30 L); C 988.88 L (S p.120; C p.198).
- Capital commitments S 3,278.31 L; C 5,642.27 L. The C table headers read 31.03.2025 and 31.03.2024, which are wrong dates (C Note 52 p.241). Clerical.
- C PPE additions 4,356.12 L, of which leasehold land 616.62 L (subsidiary plots at MIDC Umred) (C p.195).

### 12c Foreign currency and hedging (S Notes 39B, 51)
- Forward contracts to sell USD 5.76 lakh (Rs 522.15 L) and EUR 13.68 lakh (Rs 1,457.19 L) (S p.158). MTM payable 57.02 L, Level 2 (S p.138). Net hedge reserve (7.57) L after tax (S p.98).
- Unhedged: EUR payable 0.08 lakh (Rs 9.06 L) and EUR receivable 2.47 lakh (Rs 269.66 L); USD nil in S. C unhedged USD payable 0.49 lakh (Rs 46.13 L) (C p.243). Note 39B in S says no hedge was entered into (p.140). The C FX table prints USD liabilities "51.89" against 5.76 in S without a unit (C p.218). Unexplained.
- Exports 3,836.87 L (4.7% of revenue). FX gain 55.32 L (PY 63.09 L) in other income (S Note 30 p.133).

### 12d EPS, share capital, ESOP
- Basic and diluted EPS S 10.40 (PY 13.13); C 12.21 (PY 15.30). 2,54,02,613 shares unchanged (S Note 54 p.160; C Note 57 p.244). No ESOP, no convertible, no buyback: none disclosed.
- Face cross-reference slip: the P&L cites Note 55 for EPS; EPS is Note 54 (S p.94, p.160).
- Promoter holding 74.48% (18,920,779 shares), including Star Circlips at 4.56% (S p.124). Pledge: NOT FOUND IN DOCUMENT in the notes.
- Dividend: final 2.00 per share = 508.05 L proposed for FY26 (same as FY25), payout 19.2% of S PAT (derived; S Note 50 p.158).

### 12e CSR
Required and spent 68.60 L (PY 59.82 L); education 55.80 L; none through related parties (S Note 49 p.157-158). GREEN.

### 12f Direct reserve entries
No bypass of P&L beyond OCI items: remeasurement (110.76) L net and cash flow hedge (7.57) L net (S p.98). The FY25 equity roll-forward shows "Transferred from Statement of Profit and Loss (15.90) retained earnings / 10.81 OCI" (S p.97), carried unexplained in the comparative; amount 5.10 L net. The FY26 equity roll-forward is mislabelled "Balance as at March 31, 2025 (G)" on the closing line (S p.98). GREEN, clerical.

### 12g Events after balance sheet date
Only the board dividend recommendation of 23 May 2026 is mentioned (S Note 17 p.124; Note 50 p.158). No other event, no insurance receipt, no loan event. NOT FOUND IN DOCUMENT beyond that.

### 12h Cash flow statement presentation (S p.95-96; C p.173-174)
- Short-term borrowings movement is inside operating activities (789.11 L; PY 4,409.69 L).
- Non-current borrowings and finance cost are in financing. Dividend received 9.98 L sits in investing.
- C statement presents "(Increase)/Decrease in Non-Current Investments 9.98 L" as the dividend (C p.173).
- Prior year note: "EIR on Employee Loans 54.15" in FY25 duplicates the doubtful debt provision figure (S p.95). Clerical.

### 12i Going concern and related language
No going-concern doubt, material uncertainty or covenant waiver. The only going-concern text is a capital management objective ("safeguard the ability to continue as a going concern") (S Note 39C p.142; C p.221). Auditors' standard going-concern paragraph only (not a notes item). GREEN.

### 12j Other quality items
- Prior-year figures vs AR2025: S balance sheet total at 31 Mar 2025 is 50,553.98 L in AR2026 against 50,554.05 L in AR2025 (-0.07 L); receivables 8,951.34 L vs 8,951.40 L; MSME payables 833.86 L vs 832.28 L; others 1,878.78 L vs 1,880.42 L. These are sub-2 L reclassifications. Note 56 says previous figures "regrouped / recasted". No material restatement.
- Face of BS and P&L shows UDIN ending MIDGDW6526 while the auditor's pages show MZDGDW6526 (S p.93, p.94, p.91). Clerical.
- Internal financial controls: auditors' opinion is clean (S p.92). Not a notes item.

---------------------------------------------------------------
## PASS 1 SUMMARY: TOP 10 FINDINGS BY INVESTOR IMPORTANCE
| Rank | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | Umred fire: gross loss 1,672.01 L; insurance claim receivable 793.05 L (47% of loss) booked on a claim bill, no cash in FY26, no insurer acceptance shown; net exceptional 878.96 L = 18.9% of S pre-exceptional PBT; Note 14 dates the fire "April 11, 2026". | S Notes 14, 32, 37, 52, p.122, 134-136, 159 | YELLOW |
| 2 | Cash flow quality: CFO 5,438.30 L includes 789.11 L (C 1,723.34 L) of short-term borrowing increase. CFO excluding it was 4,649.19 L vs 1,121.30 L in FY25 (66% vs 17% of EBITDA), helped by trade payables +70%. | S CF p.95; Note 24 p.130; C CF p.173 | YELLOW |
| 3 | Associates carry the profit: share of profit 820.78 L = 20.5% of C PBT, 26.5% of PAT; cash dividend 9.98 L (1.3% of Star's share); Star is 90.5%; Star cross-holds 4.56% of MMP; Toyal moved about 2,551 L of liabilities to current. | C P&L p.172; C Notes 46, 49, p.234, 237-238; S Note 16 p.124 | YELLOW |
| 4 | Subsidiary guarantees 6,688 L = 22.0% of net worth, each of two above 10%; MCPL's 3,288 L is called "outstanding" though only 512.70 L is drawn; capital commitments 3,278.31 L (S) and 5,642.27 L (C) vs liquidity 298.62 L. | S Notes 47, 48, p.157; C Note 18 p.205; S Note 39B p.141 | YELLOW |
| 5 | Debt and cover: group debt 18,452.46 L (+18.1%); DSCR C 2.51 vs 4.55; S cash 56.38 L; capital management calls debt "low" and calls total liabilities less cash "net debt". | S Notes 39B, 39C, 43, p.141-145; C Note 43 p.224 | YELLOW |
| 6 | Subsidiary start-up losses 352.81 L (Insulators segment (329.13) L on 231.94 L revenue); DTA of 125.62 L recognised on those losses; pre-operative cost 210.64 L in CWIP; no impairment test shown. | C Notes 4, 20, 44, 50, p.197, 207, 226, 239 | YELLOW |
| 7 | Gratuity obligation +75% to 611.39 L, unfunded; 94.73 L Labour Code cost taken as exceptional; experience loss 251.97 L to OCI; valuation salary base +68.7% vs headcount +8.0%. | S Notes 37, 44, p.136, 146-147 | YELLOW |
| 8 | Promoter-group economics: 255.21 L to promoter family and entities (5.5% of pre-exceptional PBT); promoter-entity collateral and personal guarantees back group debt; 280 L interest-free promoter loans to MEPL (supportive); about 580.63 L of subsidiary reimbursement flows without a closing balance; a 30.00 L related-party loan missing from the RPT table. | S Notes 18, 45, p.126, 150-155; C Notes 18, 23, 46, p.205, 209, 234 | YELLOW |
| 9 | Margin story: EBITDA margin 8.04% vs 9.38% (C, derived); foils at 2.0% and conductors 4.9% (PY 8.3%) at segment level; Note 43 blames the fire for a ROCE decline although the ROCE definition excludes exceptional items. | C Note 44 p.226; S Note 43 p.145; C Note 43 p.224 | YELLOW |
| 10 | Disclosure consistency: hedge policy (fair value) vs reserve (cash flow) vs "no hedging" text vs 1,979.34 L forwards; contingent-asset policy vs claim receivable; non-deductible expense about 444 L unexplained; non-current "other receivables" 703.86 L at 40% reserve; clerical slips in dates, rates, repayment schedules, table rows. | S Notes 1, 7, 20, 39B, 51, p.98, 107, 120, 128, 140, 158 | YELLOW |

Strengths seen (GREEN): trade receivable ageing is clean (96.3% not due; over 6 months 1.18%); no write-offs in FY26; MSME dues paid on time with no interest; no covenant breach or default; no going-concern language; no tax disputes disclosed; no ESOP or dilution; CSR fully spent; related-party sales to Toyal are 2.2% of revenue; auditors' control opinion clean; no material restatement of prior year.

## OPEN POINTS FOR PASS 2 (not findings)
- Re-read Notes 5, 14, 18, 23, 45 and 49 for sub-note and footnote detail.
- Re-check the Toyal long-term liability reclassification, the 703.86 L other receivable, and the Pre-operative 210.64 L.
- Look for any statement of insurer acceptance or interim payment on the 793.05 L.

```yaml
stage: B02-notes-pass1
company: "MMP"
run_date: "2026-10-04"
model: claude-sonnet-5-5
status: pass1_complete
input_gaps:
  - "B00 CORPUS GAPPED: screener P&L, Quarters, Balance Sheet, Cash Flow, Customization sheets are empty (no CSV); Data_Sheet.csv only"
  - "B00: scanned Q4 FY26 and Q3 FY26 results are image scans with no OCR; not used in this pass (AR FY26 text used instead)"
  - "B00: ARFIN transcripts absent; peer transcripts only APARINDS and MAANALU"
  - "B00: NSE results clarifications of 2026-03-05 and 2026-06-23 have no company reply in the corpus"
  - "B00: announcements and shareholding were repaired by hand; selection, not full list"
  - "Notes-level: insurer acceptance and collection of the 793.05 L claim, FY26 guidance text, number of fire deaths, nature of 703.86 L other receivables, Toyal contingent liabilities, capitalised interest, 5-year repayment schedule are NOT FOUND IN DOCUMENT"
flags:
  - {type: FLAG-CASH, reason: "CFO includes short-term borrowing increase (S 789.11 L, C 1,723.34 L); CFO ex-borrowings S 4,649.19 L vs 1,121.30 L; payables +70.2%; trade receivable ageing itself clean"}
  - {type: FLAG-INSURANCE-RECEIVABLE, reason: "793.05 L receivable booked on claim bill, 47% of 1,672.01 L loss, nil received in FY26, acceptance not shown (S Notes 14, 37, 52)"}
  - {type: FLAG-ASSOCIATE-PROFIT, reason: "Share of associate profit 820.78 L = 20.5% of C PBT; cash dividend 9.98 L (S Note 45 p.154)"}
  - {type: FLAG-GUARANTEES, reason: "Corporate guarantees 6,688 L = 22.0% of S net worth; two items each above 10% (S Note 47 p.157)"}
accounting_quality: 6   # preliminary, pass 1 only, /10
pass_2_empty: null      # not yet run
pass_3_empty: null      # not yet run
top_findings:
  - {rank: 1, finding: "Umred fire: gross loss 1,672.01 L, claim receivable 793.05 L booked on claim bill with no cash in FY26, net exceptional 878.96 L", note_ref: "S Notes 14, 32, 37, 52 (p.122, 134-136, 159)", rating: "YELLOW", why: "Recovery is 47% of loss and unproven; Note 14 date typo; policy on contingent assets conflicts"}
  - {rank: 2, finding: "CFO includes short-term borrowing increase; CFO ex-borrowings 4,649.19 L vs 1,121.30 L; payables +70%", note_ref: "S CF p.95; Note 24; C CF p.173", rating: "YELLOW", why: "Cash conversion quality rests on payables and borrowing classification"}
  - {rank: 3, finding: "Associate profit 820.78 L = 20.5% of C PBT, 26.5% of PAT; dividend 9.98 L; Star 90.5%; Star cross-holds 4.56% of MMP", note_ref: "C Notes 46, 49; S Note 16", rating: "YELLOW", why: "Earnings are non-cash and concentrated; Toyal liabilities moved to current"}
  - {rank: 4, finding: "Subsidiary guarantees 6,688 L = 22.0% of net worth; MCPL 3,288 L called outstanding vs 512.70 L drawn; commitments 3,278.31 L S and 5,642.27 L C", note_ref: "S Notes 47, 48; C Note 18", rating: "YELLOW", why: "Parent carries funding risk of new capex vs liquidity of 298.62 L"}
  - {rank: 5, finding: "Group debt 18,452.46 L +18.1%; DSCR C 2.51 vs 4.55; S cash 56.38 L; debt called low in capital note", note_ref: "S Notes 39B, 39C, 43; C Note 43", rating: "YELLOW", why: "Leverage and cover weaken as capex ramps"}
  - {rank: 6, finding: "Subsidiary losses 352.81 L; DTA 125.62 L on losses; pre-operative 210.64 L; no impairment test", note_ref: "C Notes 4, 20, 44, 50", rating: "YELLOW", why: "Start-up drag and capitalisation judgement"}
  - {rank: 7, finding: "Gratuity DBO +75% to 611.39 L unfunded; 94.73 L Labour Code exceptional; salary base +68.7% vs headcount +8%", note_ref: "S Notes 37, 44", rating: "YELLOW", why: "Rising unfunded liability and unexplained valuation input"}
  - {rank: 8, finding: "Promoter-group payments 255.21 L; promoter collateral and guarantees; 280 L interest-free promoter loans to MEPL; about 580.63 L reimbursement flows without closing balance; 30.00 L related-party loan absent from RPT table", note_ref: "S Notes 18, 45; C Notes 18, 23, 46", rating: "YELLOW", why: "RPT scale small but disclosure thin; promoter support is visible"}
  - {rank: 9, finding: "C EBITDA margin 8.04% vs 9.38%; foils 2.0%, conductors 4.9% vs 8.3%; Note 43 blames fire for ROCE although ROCE excludes exceptional items", note_ref: "C Note 44; S Note 43; C Note 43", rating: "YELLOW", why: "Margin fall is wider than the fire explanation"}
  - {rank: 10, finding: "Disclosure inconsistencies: hedge policy vs reserve vs text vs 1,979.34 L forwards; non-deductible expense about 444 L; 703.86 L other receivable at 40% reserve; clerical slips", note_ref: "S Notes 1, 7, 20, 39B, 51", rating: "YELLOW", why: "Lowers confidence in note precision; none changes reported totals"}
red_flags: []
questions_for_mgmt:
  - "Has the insurer accepted the 793.05 L claim, and how much has been received since 31 March 2026?"
  - "What explains the 580.63 L of subsidiary reimbursement flows with no closing balance?"
  - "What is the nature and age of the 703.86 L non-current other receivables?"
  - "What caused the 67.9% rise in raw material stock?"
receivables_trend: "stable to improving: trade receivables net 8,822.61 L vs 8,951.34 L (-1.4%) on revenue +18.8%; days 39.2 vs 47.2 (FY24 36.0); not due 96.3% (PY 92.9%); over 6 months 104.89 L = 1.18% of gross (PY 32.04 L = 0.36%); other non-current receivables 703.86 L at 40% reserve is a separate watch item"
restatements_found:
  - "None material. FY25 comparatives differ from AR2025 by under 2 L in several lines (S total assets 50,553.98 L vs 50,554.05 L; MSME payables 833.86 L vs 832.28 L); Note 56 says regrouped"
going_concern_language: "NONE as doubt. Only objective text: 'Safeguard the Company's ability to continue as going a going concern' (S Note 39C, p.142)"
analyst_note: "Pass 1 only; accounting_quality is preliminary. Anchors use the [page N] marker of the .txt; printed page = N minus 5. All figures INR Lakhs. Derived ratios flagged in the report. Statement of load-bearing facts: LBF1 guidance text is not in the notes; LBF2 claim is recognised but not shown collected; LBF3 associate profit is 20.5% of C PBT with 1.3% cash payout; LBF4 CFO includes borrowing increases and group capex rests on 6,688 L of parent guarantees."
```
