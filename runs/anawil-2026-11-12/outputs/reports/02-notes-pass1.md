# Stage 2, Pass 1: Notes extraction. ANAWIL (Anawil Wire and Engineering Ltd). Run 2026-11-12

## 0. Source basis, units, anchors

- NO annual report exists (listed 2026-08-10). Notes source = Prospectus restated financial information (FY24, FY25, FY26). Second source = FY2025-26 statutory audited financial statements (G.B. Laddha & Co. LLP, OCR).
- UNIT: every Prospectus and audited figure below is in **INR lakh** unless stated. Figures in "(Rs X Cr)" are my arithmetic (lakh / 100) and labelled "derived". Nothing is converted in the anchor.
- Framework: Accounting Standards (AS), Indian GAAP, not Ind AS. Restated by S.R. Goyal & Co. (Jaipur, FRN 001537C), report dated 20 June 2026, from audits by previous auditor G.B. Laddha & Co. LLP (Prospectus PDF p.167-168).
- Anchor convention: "Pros p.N" = the `[page N]` marker in Prospectus_2026-08-06.txt (marker N is the PDF page; the printed page number is N minus 3). Annexure letters are the restated notes' own numbering (the Prospectus has no "Note 1..N" numbering; Annexure IV carries policies 2.1-2.26 and notes B1-B12).
- Audited FS file: "AFS p.N" = marker in Audited_Financial_Statements_FY2025-26.txt.

### AFS pages read vs blank (state at read time)
- TEXT PRESENT and read: AFS p.1-2 (auditor's opinion, other-information paragraph), p.36 (notes 11-12 tail), p.37 (note 37 EPS, note 38 analytical ratios, signatures), p.38 (a FY2025 auditor's report opening), p.71-73 (G.B. Laddha FY2024 audit engagement letter, not financial content).
- BLANK ("OCR PENDING"): p.3-35 (rest of auditor's report, CARO annexure, balance sheet, P&L, cash flow, notes 1-10 and 13-36), p.39-70, p.74-103.
- Consequence: the audited statements could be used only as a cross-check on EPS and the ratio note (notes 37-38). Every other finding rests on the Prospectus. Passes 2 and 3 and stage 3 should re-read AFS when OCR completes (balance sheet p.~4-6 area, cash flow, CARO clauses on loans, RPT, defaults, fund diversion are the priority pages).
- OCR caution: AFS text drops spaces and misreads digits (e.g. "05`96" for the FY25 weighted share count; "Date 18/06/2025" for 2026). Where a figure matters it is cross-checked below.

---

## 1. Load-bearing facts: priority verification (a) to (f)

### (a) FY26 cash flow from operations and the gap to PAT
Restated Cash Flow Statement (Annexure III, Pros p.174), INR lakh, FY26 / FY25 / FY24:

| Line | FY26 | FY25 | FY24 |
|---|---|---|---|
| PBT | 4450.47 | 1487.76 | 534.36 |
| Depreciation | 1130.14 | 1005.13 | 1134.00 |
| Interest paid (added back) | 564.27 | 585.66 | 555.19 |
| Gratuity provision / loss on sale / bad debts w/off / dividend | 10.57 / 4.77 / 9.81 / (0.05) | 7.40 / - / - / (0.01) | 6.64 / - / - / - |
| Operating profit before WC | 6169.98 | 3085.94 | 2230.19 |
| Inventory | (3863.77) | (141.41) | (887.20) |
| Trade receivables | (1387.74) | (2133.67) | (378.11) |
| Loans and advances and provisions | (3565.64) | (396.66) | 39.21 |
| Other current assets | (179.20) | (83.80) | (89.23) |
| Trade payables | 3793.27 | 434.94 | 161.26 |
| Other current liabilities | 1281.91 | 323.23 | (32.30) |
| Other long term liability | 2.00 | 10.00 | - |
| Cash generated from operations | 2250.79 | 1098.56 | 1043.82 |
| Income taxes paid | (406.86) | (132.25) | (154.49) |
| **Net cash from operating activities** | **1843.94** | **966.31** | **889.33** |

- FY26 CFO = 1843.94 lakh (derived Rs 18.44 Cr). This matches the "Rs 18 Cr" in the presentation. The "Rs 12.5 Cr" figure is NOT in the restated cash flow. NOT FOUND IN DOCUMENT as a reported CFO. Nearest derived figure: CFO after interest paid = 1843.94 - 564.27 = 1279.67 lakh (derived Rs 12.80 Cr); not equal to 12.5, do not treat as the source. Reconciliation of the 12.5 stays open for the orchestrator. 🟡
- PAT (restated) 3662.83 (Annexure II, Pros p.173). Gap PAT less CFO = 1818.89 lakh (derived). CFO/PAT = 50.3%; CFO/EBITDA(6108.90) = 30.2% (derived). FY25: 966.31/1230.58 = 78.5%. FY24: 889.33/439.18 = 202%. 🟡 (declining conversion in the high-growth year)
- What drives the gap (WC absorbed 3919.19 lakh derived; tax 406.86): inventory 3863.77 (raw material 269.92 to 3930.40), advances/GST in "Loans and advances" 3565.64, receivables 1387.74, offset by payables +3793.27 and other current liabilities +1281.91.
- CLASSIFICATION DISTORTION in CFO (derived, labelled):
  - "Other current liabilities" change 1281.91 includes Sundry Creditor for Capital Goods rising 203.51 to 1036.39 (+832.88) (Annexure G, Pros p.199). Capex creditors are an investing item. Investing outflow (9305.37) equals the accrual capex (net fixed assets + depreciation + loss on sale), so the unpaid capex sits in operating inflow.
  - "Other non-current assets" (421.84 outflow) is in INVESTING and includes Retention Money 297.44 (nil in FY25) and FD with BOB 75.18 (Annexure L, Pros p.203). Retention money is a contract receivable, an operating item.
  - CFO ex capital creditors = 1843.94 - 832.88 = 1011.06 lakh (derived Rs 10.1 Cr). CFO ex both = 1011.06 - 297.44 = 713.62 lakh (derived Rs 7.1 Cr), 19.5% of PAT. 🔴 for earnings-to-cash quality, classification-driven; flag to stage 10/FLAG-CASH.
- Interest on delayed taxes 15.96 and TDS late fee 1.10 (Annexure W, Y) plus net tax provision unpaid 561.78 vs 186.61 (Annexure H) show taxes paid behind accrual: current tax 770.34 + earlier year 11.69 less tax paid 406.86. 🟡

### (b) Short-term loans and advances 5001.52 lakh at 31 Mar 2026 (derived Rs 50.0 Cr)
Annexure P (Pros p.206), INR lakh, FY26 / FY25 / FY24:
- Advance to Vendors 3063.21 / 657.72 / 73.64
- GST Receivable 1878.59 / 734.55 / 953.96
- Loans and Advances to Employees 36.93 / 23.56 / 8.20
- Prepaid rent 16.94, prepaid insurance 5.36, other prepaid 0.49
- Total 5001.52 / 1435.89 / 1039.22. Ties to balance sheet (Annexure I, Pros p.172) and to the CFO line (5001.52 - 1435.89 = 3565.63 vs 3565.64).
- COMPOSITION: 61.3% vendor advances, 37.6% GST receivable (derived). Vendor advances = 21.4% of FY26 revenue (derived) and up 4.66x in one year. 🔴
- COUNTERPARTIES: NOT FOUND IN DOCUMENT. The vendor names, the purpose (steel plate, capex, sub-contract), age of advances and whether any are related are not disclosed. Notes P-2/P-3 state the company has granted no loans or advances to promoters, directors, KMP or related parties (Pros p.206) and Annexure K note 2 repeats it (Pros p.203). The related party list (ZA) shows Darpan Infrastructure only as a payable (87.27), not as an advance holder. Auditors state they did not test promoter/group lists (Annexure P note 2, Pros p.206). 🟡
- Advances are "unsecured, considered good"; no provision. Annexure ZQ: balances "subject to confirmation" (Pros p.221). Annexure IV B5: "unsecured and considered as good are subject to confirmations" (Pros p.186). 🟡
- Classification: these are current, but if any part is a capital advance for the Kutch plant it is mis-classified. Policy 2.24 says "does not have any capital advance except as disclosed in the balance sheet" (Pros p.181), yet the balance sheet shows none. NOT FOUND whether capital advances sit inside vendor advances. 🟡
- GST receivable 1878.59 (13.1% of FY26 revenue, derived), +1144.04 YoY. The notes do not say whether this is accumulated input credit or a refund claim. NOT FOUND IN DOCUMENT. Policy 2.19 (Pros p.181): unused credit carried forward; charged off if not available. [INFERENCE: a credit balance this large against a 5.0 to 5.6% rise in GST on output and steel input is consistent with an input-heavy position; not stated in the notes.]
- Management says all current assets and advances will realise "approximately" book (B9 and Annex IV note 6, Pros p.185/186). 🟡
- Fixed deposit with BOB 75.18 (Annexure L) and 150.03 FD in cash equivalents (Annexure O): lien status NOT FOUND. Bank Guarantee limit 300 requires 20% cash margin (Note 10, Pros p.226), implying ~60 margin; FD 75.18 plausibly is it. [INFERENCE]

### (c) Inventory, trade receivables and payables ageing
INVENTORY (Annexure M, Pros p.203), INR lakh, FY26 / FY25 / FY24:
- Raw materials 3930.40 / 269.92 / 264.16; WIP 1039.64 / 777.38 / 799.44; stores and spares 90.29 / 69.44 / -; scrap 8.45 / 6.80 / -; finished goods 0.00 / 81.47 / -; total 5068.78 / 1205.01 / 1063.60.
- Raw material = 77.5% of FY26 inventory (derived), 14.6x YoY while revenue rose 82.3% and purchases (Annexure T) rose 3.35x (8392.06 vs 2506.49). Raw material at year-end / FY26 consumption (4731.58) = 303 days (derived), vs 39 days FY25. 🔴 for the working-capital step-change; the notes do not explain the build (bulk steel buying ahead of the order book is a hypothesis, NOT in the notes).
- Finished goods: nil at FY26 (81.47 FY25). WIP +33.7% vs revenue +82.3%. No write-down, no obsolete stock disclosed; NRV test stated as policy only (policy 2.5, Pros p.177). WIP valued by "management estimate according to stage of completion" (policy 2.5). 🟡
- Company's own inventory turnover (Annexure ZE, Pros p.214): 252.85 / 175.06 / 202.69 days. Year-end inventory to revenue x365 (derived): 129 / 56 / 72 days.
- Customer-supplied material: NOT FOUND IN DOCUMENT. Inventory note, policy 2.5 and the revenue annexure carry no mention of free-issue or customer-owned steel, and no memorandum record of it.
- Scrap in inventory 8.45 while revenue from "others" (789.93) includes scrap sales (Annexure R footnote, Pros p.207). Scrap income recognised in revenue not as by-product credit. 🟢/🟡

TRADE RECEIVABLES (Annexure N, Pros p.204-205), INR lakh:
- Total 3894.54 / 2516.61 / 382.94. All "unsecured considered good". Provision for doubtful debts: blank in all three years (no ECL / allowance). Bad debts written off FY26 9.81 (CFO addback and Annexure Y "Write Off"). 🟡
- Ageing FY26 from due date: Not due 3841.82; <6 months 12.29; 6m-1y 23.79; 1-2y 16.65; >2y 0. FY25: not due 1978.89; <6m 500.59; 6m-1y 14.98; 1-2y 22.16. FY24: not due 380.11; 1-2y 2.83.
- > 6 months: FY26 40.44 (face statement 40.43) = 1.04% of total (derived); FY25 37.14 = 1.48%; FY24 2.83 = 0.74%. Related-party receivables: nil (Annexure N, ZA). 🟢 on ageing; but 98.6% of FY26 balance is reported as "not due". 🟡 since ageing is "based on date of transaction in case there is no credit period agreed" (Annexure N note 3, Pros p.204): the 'not due' bucket then depends on contractual terms not given.
- Receivable days: company basis (average) 82 / 67 / 13 (Annexure ZE, Pros p.214). Year-end basis (derived) 99 / 117 / 26. Receivables as % of revenue 27.2% / 32.0% / 7.1% (derived). Trend: stable-elevated since the FY25 step-up; year-end days down from FY25.
- Customer concentration: NOT FOUND IN DOCUMENT in the restated notes. Segment note: 100% domestic (ZF5, Pros p.216).
- Retention money receivable (current 338.54 + non-current 297.44 = 635.98 at FY26 vs 173.03 FY25) (Annexures L and Q, Pros p.203, 206): 4.4% of revenue, shown outside trade receivables, not aged. 🟡
- Advances received from customers 309.23 vs 0.03 (Annexure G, Pros p.199).

TRADE PAYABLES (Annexure F, Pros p.197-198):
- Total 4666.33 / 873.06 / 438.12; MSME 821.94 / 62.47 / 23.42; others 3844.38 / 810.59 / 414.70 (balance sheet; FY24 splits 281.78 plus 132.91 related-party in Annexure F).
- Ageing FY26: MSME not due 570.95, <1 year 251.00; others not due 3703.04, <1 year 141.34; no disputes; nothing past 1 year. FY25: not due 428.75, <1 year 444.31.
- Payable days (company, Annexure ZE): 120 / 95 / 65. Rising, i.e. suppliers fund part of the build. Audited note 38 gives the reason as "longer credit periods obtained from suppliers" (AFS p.37). 🟡
- MSME > 45 days: ZG1 (Pros p.216) says the company pays MSME dues "generally within stipulated period of 45 days" and shows unpaid principal 735.61 and interest nil. But Annexure F shows MSME dues 821.94 of which 251.00 are past due. The two figures disagree by 86.33. Tax shelter adds back "expenses disallowed under Section 43B" 263.45 (Annexure ZB, Pros p.212), with DTA 45.21 (Annexure C, Pros p.197). Section 43B(h) disallows MSME purchases unpaid beyond the statutory limit; 263.45 is near the 251.00 past-due MSME. [INFERENCE: the 43B(h) item and the 251.00 are the same dues.] No interest under MSMED Act s.16 accrued. 🔴 (disclosure conflict; small money)
- FY25 related-party payables: Annexure F shows nil related-party dues for FY26 and FY25, while ZA shows Darpan trade payable (87.27) FY26 and (467.67) FY25, (132.91) FY24 (Pros p.211). Classification conflict. See RPT below. 🔴
- Sundry creditor for capital goods 1036.39 (Annexure G) is separate; imports of capital goods in FY26 were 890.21 (Annexure ZF1, Pros p.215). Payable currency NOT FOUND (ZG3 shows only receivables and advances, nil).

### (d) Related party transactions and balances (Annexure ZA, Pros p.210-211; INR lakh)
Related parties named: Nimish Kumar Rameshchandra Vashi (MD, promoter), Ayush Nimish Vashi (WTD, promoter), Bijal Nimesh Vashi (director from 1 Feb 2025), Bhavin Navinchandra Desai (director), independent directors, CFO Chiragkumar Patel (from 28 Mar 2025), CS Sakshi Vijay (from 1 May 2025), SMP Debasish Maiti (from 1 Jun 2025), Vipul Vashi (relative of director), Darpan Infrastructure Private Limited (common director). Auditors rely on management's list (ZA note 1).

| Party | Nature | FY26 | FY25 | FY24 |
|---|---|---|---|---|
| Ayush Vashi | Remuneration | 14.04 | 12.00 | 12.00 |
| Nimish Vashi | Remuneration | 16.94 | 2.50 | 0.00 |
| Bijal Vashi / Bhavin Desai | Remuneration/fees | 1.70 / 1.70 | 0 / 0 | 0 / 0 |
| Independent directors (Bhagat, N. Desai, Tayal, Bhurat) | Fees | 1.50 / 1.50 / 0.30 / 0.30 | 0 | 0 |
| CFO / CS / SMP | Salary | 9.93 / 10.18 / 2.75 | 0 | 0 |
| Darpan Infrastructure | Interest on loan | 32.22 | 27.23 | 0.00 |
| Darpan | Loan received / repaid | 108.50 / 576.17 | 1018.67 / 551.00 | 1389.52 / 1574.57 |
| Darpan | Commission for corporate guarantee | **97.60** | 0.00 | 0.00 |
| Darpan | Construction of fixed asset | 127.67 | 0 | 0 |
| Darpan | Fixed asset sold to Darpan | 1.94 | 0 | 0 |
| Darpan | Rent expense | 0.65 | 0.65 | 0.00 |
| Darpan | Sales / receipt of services | 0 / 0 | 0 / 0 | 338.15 / 498.71 |
| Nimish Vashi | Loan taken / repaid | 1442.24 / 1039.58 | 81.50 / 380.70 | 1208.10 / 891.81 |
| Ayush Vashi | Loan taken / repaid | 6.00 / 54.79 | 20.00 / 20.00 | 4.43 / 10.03 |
| Vipul Vashi | Loan taken / repaid | 0 / 0 | 100.00 / 100.00 | 100.00 / 100.00 |
| Bhavin Desai | Loan taken / repaid | 30.65 / 30.65 | 67.55 / 67.55 | 9.92 / 9.92 |

Balances at year end: Nimish Vashi loan 414.75 / 12.09 / 311.29; Ayush Vashi 19.15 / 67.40 / 67.40; Darpan loan 0.00 / 494.90 / 0.00 (Annexure B(B), Pros p.196); Darpan payable (87.27) / (467.67) / (132.91). Director/KMP remuneration payable ~11 in total.
- RPTs as % of FY26 revenue (derived, using the transaction lines, excluding loan churn): remuneration lines ~73 = 0.5%; Darpan commission + construction + interest + rent + asset sale = 260.08 = 1.8%. Including Darpan loan flows (684.67) and Nimish loan flows (2481.82) the gross volume is ~3.4 + 17.3 = large vs revenue but is financing.
- Promoter loans are interest-free "taken without any preconditions towards repayments", on demand (Annexure B(B) note, Pros p.196): 433.89 outstanding at FY26 (Annexure B, Pros p.190), subordinated to bank only by practice. Nimish Vashi routed 1442.24 in during FY26 (founder funding of the capex bridge) and took back 1039.58. 🟡 (a post-IPO repayment would show in the proceeds uses). Darpan loan carried 11.00% interest (B(B)).
- ROLL-FORWARD TESTS (derived): Nimish: 12.09+1442.24-1039.58 = 414.75 ties. Ayush: 67.40+6.00-54.79 = 18.61 vs 19.15 shown (0.54 unexplained). Darpan: FY25 1018.67-551.00 = 467.67 principal, plus 27.23 interest = 494.90 loan shown; and 467.67 is shown AGAIN as the trade payable in ZA. FY26: 494.90+108.50-576.17 = 27.23 before FY26 interest 32.22 and the loan is shown nil; the (87.27) payable is not explained. The Darpan loan/payable do not reconcile across ZA, B(B) and Annexure F. 🔴 (disclosure integrity)
- GUARANTEE COMMISSION 97.60 to Darpan in FY26 (first year; zero before). It does not appear as a named line in Other Expenses (Annexure Y), Finance Cost (Annexure W) or Employee costs. Where it was booked is NOT FOUND IN DOCUMENT. Possibilities that the notes do not settle: capitalised in PPE or CWIP (policy 2.26 allows borrowing-cost capitalisation), or buried in a bucket. This is 2.2% of PBT (derived). 🔴
- Interest on unsecured loans in P&L 44.55 (Annexure W) vs Darpan 32.22 + Cosmos Co-op Bank ~8-9 (9.50% on ~86) = ~40-41 (derived), consistent.
- Cosmos Co-operative Bank: unsecured loan 82.86 (9.50%, "from Bank") and shares 0.50 (Annexure J). Not a related party per ZA.
- Rent income 35.00 in FY26 (Annexure S, Pros p.207) with no counterparty; it is not in the RPT table. NOT FOUND IN DOCUMENT who pays it. Yet policy 2.23/ZG2 says no leased assets and nil lease rentals. Meanwhile "Machine Rent Expenses" 142.43 (207.15 FY25) and prepaid rent 16.94 appear in Annexures Y and P. The lease note says nothing in force while rent items exist. 🟡
- Omission check: Vipul Vashi appears as relative of director and personal guarantor and as collateral owner, but has no remuneration or guarantee fee. Personal guarantors (5 individuals) receive no fee; only the corporate guarantor Darpan is paid. [INFERENCE: fee pricing is not benchmarked in the notes.] Policy 2.22 asserts all RPTs are arm's length (Pros p.181); no benchmarking is disclosed. 🟡
- Director remuneration total ZA ≈ 37.98 vs Annexure V "Directors Remuneration" 37.50 (Pros p.208). Small mismatch (0.48). Bhavin Desai is listed twice in the balance table. 🟢/🟡
- Remuneration of MD Nimish Vashi is 16.94 on a business with PAT 3662.83 (low pre-IPO; Chairman/MD "associated with the Company since February 2025", MD&A, Pros p.229). 🟡 (re-set risk post listing)

### (e) Borrowings, security, promoter guarantees
Annexure B (Pros p.189-190), INR lakh, FY26 / FY25 / FY24:
- Long-term: secured term loans 9334.94 / 3240.78 / 3516.90; unsecured from bank 75.53 / 82.62 / 89.72; from directors 433.89 / 79.49 / 378.69; from related parties 0 / 494.90 / 0; total 9844.37 / 3897.78 / 3985.32.
- Short-term: cash credit 1184.32 / 869.66 / 656.10 plus current maturities 1796.07 / 743.44 / 544.27 = 2980.40 / 1613.10 / 1200.37. Total debt 12824.76 / 5510.88 / 5185.69.
- Lender: Bank of Baroda is the only secured lender named. Annexure B(A) (Pros p.191-194), outstanding at 31 Mar 2026 / 31 Mar 2025:

| Facility | Sanction | Rate | Repayment | 31-Mar-26 | 31-Mar-25 |
|---|---|---|---|---|---|
| Vehicle loan | 10.40 | 9.15% | 84 EMI 0.17 | 6.67 | 8.07 |
| Term loan, Koppal construction + P&M | 4158.00 | MCLR+SP+2.00 = 11.05% | 72 ballooning, 18-month moratorium, EMI 37.70* | 2852.43 | 3508.83 |
| Cash credit | 700.00 | 11.05% | n/a | 1184.32 | 869.66 |
| Sany crane loan | 490.00 | BRLLR+SP+1.50 = 10.65% | 60 EMI 10.57 | 376.11 | 460.00 |
| TL 2652 Kutch shed | 2169.00 | BRLLR+SP+0.85 = 9.25% | 72 balloon, EMI 20.00 | 2167.09 | 0 |
| TL 2654 Kutch P&M | 4850.00 | 9.25% | 72 balloon, EMI 40.00 | 3975.56 | 0 |
| TL 2584 Koppal expansion | 1385.00 | 9.25% | 72 balloon, EMI 17.00, 6m moratorium | 1299.17 | 0 |
| TL 2657 Bharat Benz truck | 51.81 | 10.00% | 60 EMI 1.10 | 44.38 | 0 |
| TL 2703 and 2704 truck cranes (2 rows) | 416.00 | 9.40% | 60 EMI 4.36 each | 201.14 + 201.14 | 0 |
| Total | | | | 12308.01 | 4846.56 |
(* ballooning installment changes every year.) Total ties to the sum of rows. It differs from Annexure B secured items (9334.94+1796.07+1184.32 = 12315.33) by 7.32 (derived); also 7.32 at FY25. 🟢/🟡

- Floating vs fixed: all bank rates are MCLR- or BRLLR-linked (floating); the vehicle loan rate is stated as 9.15% p.a. (type not stated). Cosmos Bank unsecured at 9.50%, 120 months (Pros p.227).
- RATE RESET: the Financial Indebtedness statement at 31 May 2026 (Pros p.223-224) shows the Koppal term loan "modified sanction 27.10.2025" at BRLLR+SP+0.85 = 9.25% and sanction 3180 (vs 4158 and 11.05% in B(A)); the cash credit limit is 1200 (vs 700 in B(A)). So B(A) shows stale terms. Cash credit utilisation: 1184.32 / 1200 = 98.7% at March 2026, and 1193.82 at 31 May 2026 = 99.5% (derived). 🟡
- Sanction vs book: at 31 Mar 2025 the CC balance 869.66 exceeded the 700 limit shown in B(A) (124%, derived); either the limit was raised earlier or the limit is stale. NOT FOUND. 🟡
- 5-YEAR REPAYMENT SCHEDULE: NOT FOUND IN DOCUMENT. Derived from the EMI column: monthly term EMIs 135.26 (sum of 0.17+37.70+10.57+20+40+17+1.10+4.36+4.36) = 1623 lakh a year, vs current maturities 1796.07 at FY26 (Annexure B). "Ballooning" instalments mean the back-ended balance is large. [INFERENCE for the back-end; schedule absent.] DSCR in the note: 2.29 (FY26) (Annexure ZE, Pros p.214).
- Post-issue capitalisation (Annexure ZC, Pros p.212-213): total debt 12824.76 pre-issue vs 1324.76 post-issue; long-term debt 11640.44 vs 340.44; short-term 1184.32 vs 984.32; equity 8951.16 vs 23220.12. A debt reduction of 11500 lakh (derived Rs 115 Cr), i.e. about 80% of the net new equity (14268.96, derived). Ties to LBF-4 "IPO money used" by 30 Sep 2026; the prospectus objects are outside this stage. 🟡
- SECURITY (Note 2 and 3, Pros p.194-195): hypothecation of entire current assets and plant and machinery; equitable mortgage of Koppal land and factory shed; collateral = Kutch factory land (company), **Plot 201 Vibrant Business Park, Vapi, owned by Darpan Infrastructure Pvt Ltd (also the registered office)**, residential sub-plot land at Paria, Pardi, Valsad owned by **Nimish Vashi and Vipul Vashi**, and company land Sy. No. 12/1 and 12/3. Vehicle loans carry first charge on the vehicle (no collateral).
- PERSONAL GUARANTEES from: Ayush Nimish Vashi, Bhavin Navinchandra Desai, Nimish Rameshchandra Vashi, Vipul Rameshchandra Vashi, Bijal Nimish Vashi, plus **corporate guarantee of Darpan Infrastructure Pvt Ltd** (Pros p.195, 225-227). Five security cheques also drawn on operative account for crane/truck loans (Note 3/8/9). 🔴 for dependence: all term and working capital facilities rest on the promoter family and Darpan.
- Charges registered: no charge pending creation or satisfaction at MCA (ZP, Pros p.221). Not a wilful defaulter. 🟢
- Covenants, breaches, waivers: NOT FOUND IN DOCUMENT in the restated notes. No default disclosed. Unclassified: current maturities.
- Non-fund based: BG limit 300 with 20% cash margin (Pros p.224, 226). Outstanding BG: "Total (Non-Fund Based)" blank (Pros p.225). NOT FOUND.
- Related-party borrowings: Nimish Vashi 414.75, Ayush Vashi 19.15 (interest free, on demand); Darpan nil at FY26 (11.00%). 31 May 2026: Nimish 441.75, Ayush 10.15, Cosmos 81.62 = 533.52 (Pros p.227).
- Interest cost effect: interest on secured loans 498.93 vs average secured debt (4846.56 + 12308.01)/2 = 8577.29 gives 5.8% (derived), against 11.4% in FY25 (546.99 on average 4778.59). Most FY26 drawings (9029.27 of long-term proceeds) were late in the year or part of the interest was capitalised. Capitalisation amount NOT FOUND IN DOCUMENT although policy 2.26 allows it (Pros p.181) and AS 16 requires disclosure. 🟡

### (f) Revenue recognition and the three contract models
- Policy 2.4 (Pros p.177): sale of goods recognised "when the significant risks and rewards of ownership ... have been transferred ... and there are no longer unfulfilled obligations. The performance obligations ... are fulfilled at the time of dispatch, delivery or upon formal customer acceptance depending on the customer terms." Services: "when services have been rendered and there should be no uncertainty regarding consideration." Interest: time proportion. 
- NOT FOUND IN DOCUMENT: any separate policy for (1) pure conversion / job work on customer-supplied steel, (2) conversion plus internals, (3) integrated supply with company-procured steel; any statement on how customer-supplied material is recorded (off-balance-sheet, memorandum, or nil), whether conversion revenue is shown gross or net of steel, any AS 7 construction-contract method, any contract asset or liability, any unsatisfied performance obligations or order book. Segment note: one segment (ZF5, Pros p.216). The Prospectus restated notes cannot test the three-model revenue split. The brief's 64.3% integrated-supply mix is an unanchored claim relative to these notes. 🟡
- Revenue disaggregation (Annexure R, Pros p.206): tower manufacturing and fabrication 13518.76 / 7854.55 / 4391.81 (94.4% / 99.9% / 81.2% of revenue, derived); boiler accessories and paper machinery 18.00 / 0 / 706.32; others 789.93 / 4.31 / 308.51 (includes scrap, "supply of safety items to contractors" and "sale of traded goods"). Purchases of stock in trade are nil in all years (Annexure II). "Traded goods sold" with nil trading purchases is an unexplained inconsistency. 🟡
- FY26 revenue 14326.69 (+82.3%; FY25 +45.4%) all domestic (ZF5).
- Cost structure consistent with some steel-supplied-by-company: purchases of raw material 8392.06 in FY26 (58.6% of revenue) and consumption 4731.58 (33.0%); but if the bulk of towers were steel-in-conversion, material would not be 33% of revenue. The notes do not state the model split. [INFERENCE only]
- Retention money, advances from customers 309.23, and "performance BG" (Pros p.224) show contract-style terms; revenue policy is at dispatch/acceptance. A WIP of 1039.64 is carried at cost. 🟡
- Other operating costs that reflect outsourcing: fabrication work 1282.41 (9.0% of revenue), labour charges 444.27, machine rent 142.43, rifilling charges 149.74 (Annexure Y, Pros p.208-209). Employee cost only 415.03 (2.9% of revenue). Counterparties not disclosed. 🟡

---

## 2. Extraction by the 12 headings

### 1. Accounting policies and changes
- Basis: AS under Section 133, historic cost, accrual, going concern; operating cycle 12 months (policy 2.1, Pros p.176). Examination states "no change in accounting policies" (Annexure IV A, Pros p.181; auditor report item 6g, Pros p.168).
- CONTRADICTION within the restatement: Annexure V explanation (c) (Pros p.187) says depreciation was recalculated on WDV per Schedule II in the restatement, giving a depreciation adjustment of +142.50 to FY24 profit and (144.49) to FY25 (PAT reconciliation, Pros p.187). A basis change is an accounting policy change, and the audited accounts must have used a different basis. Also gratuity was not provided in the audited accounts (adjustment 6.64 FY24; opening 0.89) and deferred tax was recomputed. 🟡
- Depreciation (policy 2.7, Pros p.178): WDV, Schedule II lives: P&M 15 yrs, building 30, vehicles 8, furniture 10, computers 3, office equipment 5; pollution control licence amortised over 30 years. Heavy fabrication plant at 15 years WDV is in line with Schedule II norm; no change in lives disclosed. 🟢
- Capitalisation: no stated threshold. Borrowing cost capitalised for qualifying assets (policy 2.26). 
- Impairment (policy 2.17): no assumptions, no test disclosed. Goodwill: none.
- ECL: none; no matrix. 🟡
- Lease policy 2.23: no leases; Ind AS 116 not applicable (AS 19). Contradicted by rent lines, see above.
- Employee benefits (policy 2.12): gratuity unfunded, actuarial; leave encashment short-term undiscounted (expense 6.03 FY26, nil prior; liability not visible in Annexure H). 🟡
- Government grants policy 2.14 exists; no grant disclosed.
- Restated net profit versus audited (Annexure V, Pros p.187), INR lakh: FY26 3595.25 to 3662.83 (+67.58); FY25 1398.41 to 1230.58 (-167.83, -12.0%); FY24 333.55 to 439.18 (+105.62). Within FY26 the adjustment includes +83.40 "income tax adjustment for earlier years adjusted in reserve and surplus" brought into restated profit and (11.69) earlier year tax. Reserve reconciliation shows FY26 audited reserves = restated 6979.66 with no net adjustment, while profit moved +67.58 (Pros p.186). Internal inconsistency. 🟡
- Examination report refers to "our examination report dated September 10, 2025" and engagement letter of Aug 2025 inside a report dated June 20, 2026 (Pros p.167-168). Boilerplate carry-over; not material. 🟢/🟡
- Statutory audit change: audited FY24-FY26 signed by G.B. Laddha ("Previous Auditors"); restatement by S.R. Goyal. Who is the current statutory auditor and the reason for change: NOT FOUND IN RESTATED NOTES.
- Audited FS opinion (AFS p.1-2): unqualified opinion for FY26; "KAM not applicable as unlisted company." CARO annexure: AFS p.3+ blank, not read.

### 2. Related party transactions
See (d) above. New related parties this year: Bijal Vashi (director from 1 Feb 2025), independent directors Nirav Desai and Digant Bhagat (from 20 Jun 2025), CS, SMP. Loans to promoters: none (K and P). Royalty, rent to promoter family: rent 0.65 to Darpan. 

### 3. Contingent liabilities (Annexure Z, Pros p.209-210)
| Nature | FY26 | FY25 | FY24 | Stage |
|---|---|---|---|---|
| Income tax demand per portal, AY 2022-23 (97.06 + 24.26 interest) and AY 2023-24 (88.75 + 16.86 interest) | 0.00 | 226.93 | 226.93 | appeal filed 29.05.2025; "demand has been disposed as on 31.03.2026" |
| Pending litigation, TDS defaults, capital commitments, uncalled liability | nil | nil | nil | |
- 226.93 = 5.7% of FY25 net worth (4007.59) and 8.2% of FY24 (2776.75) (derived). Outcome of disposal (paid, deleted, rectified) NOT FOUND; no FY26 P&L line carries it (earlier-year tax only 11.69). 🟡
- Notes B4 text says contingent liabilities "during F.Y. 2024-25 amounting to 2,26,93,443" (Pros p.184), consistent.
- Capital commitments reported nil though Kutch plant is in CWIP 585.00 and Sundry creditor for capital goods is 1036.39 at year end; undrawn sanction exists (Koppal expansion 1385 vs 1299.17). Commitment nil looks understated. 🟡
- Guarantees for subsidiaries: no subsidiaries.

### 4 to 5 and 8. See (c).

### 6. Investments
- Non-current investment: shares of Cosmos Bank 0.50 (FY25, FY26) (Annexure J, Pros p.203). Dividend income 0.05 / 0.01 (Annexure S). No subsidiaries, JVs, associates, ICDs or loans given (ZN-D, Pros p.221). Layers compliant. 🟢
- Advances to others: none apart from Annexure P.

### 7. Borrowings: see (e).

### 9. Provisions (Annexures E, H, ZL; Pros p.182-184, 199, 218-220)
- Gratuity (unfunded): DBO 25.49 / 14.92 / 7.52. Service cost 15.95, interest 1.46, actuarial gain (6.85) credited to P&L; net expense 10.57. Plan assets nil. Discount rate 7.93% / 6.96% / 7.10%; salary escalation 15.00% (company-provided); withdrawal 3.00%; retirement 58; mortality IALM 2012-14; term 21.21 years. Salary escalation and attrition "have been provided by the Company" (Pros p.220). 🟡 (actuarial gains of 6.85 offset 39% of the service cost; AS 15 allows P&L recognition).
- Warranty provision: NOT FOUND IN DOCUMENT (no warranty or defect-liability provision for towers). Decommissioning, onerous contracts, litigation provisions: none. 🟡 for a structural-fabrication maker with performance BGs.
- Short-term provisions 561.81 = income tax net of advance tax 561.78 + gratuity 0.03. CSR provision 18.00 charged in FY26 (Annexure Y).
- Contract liability: advances from customers 309.23.

### 10. Deferred tax and tax (Annexures C, ZB; Pros p.197, 211-212)
- Net DTA 17.02 / 22.63 / 0.39. FY26 components: depreciation (32.60) DTL (flipped from 20.00 DTA), gratuity 4.37, preliminary 0.04, 43B(h) 45.21.
- Tax rate applied 17.160% on business income; 25.168% on other sources (Annexure ZB). [INFERENCE: 17.16% = 15% + 10% surcharge + 4% cess, i.e. the concessional new-manufacturing-company regime (s.115BAB); the notes never name the section or test eligibility conditions.] Eligibility NOT FOUND. 🟡
- Effective rate (derived): total tax 787.65 / 4450.47 = 17.70% FY26; 257.18 / 1487.76 = 17.29% FY25; 95.18/534.36 = 17.81% FY24. A move to the 25.168% rate would cut FY26 PAT by about 8.0 percentage points of PBT (derived, not a projection).
- MAT: nil; tax paid under "Normal". No unrecognised DTA. Tax paid 406.86 vs current tax 770.34 (see above).
- Tax shelter timing differences: tax depreciation exceeded book by 306.51 in FY26; 43B disallowance 263.45.

### 11. Revenue details: see (f). No contract assets. No top customer disclosure. No export. 

### 12. Other critical notes
- Exceptional items: none (Annexure II). Other income 35.98 (FY25 80.98 incl. misc income 68.38 non-recurring-looking). 
- EBITDA definition (Annexure ZD, Pros p.213): PBT + depreciation + "interest expenses" - other income = 6108.90 (derived tie: 4450.47+1130.14+564.27-35.98). EBITDA bears bank charges 24.71 and other charges 5.74 (they sit in finance cost 594.71 but are not added back). 42.64% margin (MD&A Pros p.229). 🟢
- Intangibles: pollution control licence 36.00 gross, WDV 31.87 (FY26 additions 6.00; amortisation only 0.01 in FY26 vs 2.03 prior; Annexure I, X). Amortisation collapse unexplained: policy says 30-year straight line, giving about 1.2 a year. 🟡
- PPE (Annexure I, Pros p.200-202): FY26 additions 8850.77 (P&M 5806.80, building 2449.97, vehicles 538.59); CWIP closing 584.80 (additions 4142.59, transfers 3682.26); gross block 17162.17. P&M deduction 30.53; loss on sale 4.77. CWIP ageing note ZM shows 589.35 split building 288.52 and P&M/intangibles 300.84 (Pros p.220-221) versus 584.80 all "Building WIP" (Annexure I, policy 2.9) and AFS note 12 showing CWIP 585.00 (AFS p.36). Small split conflict. 🟡
- Foreign currency: none receivable; imports of capital goods 890.21 in FY26 (24.29 spares) (Annexure ZF1); FX gain 0.40; no hedge policy disclosed, no payable exposure disclosure. Raw material 100% indigenous (ZF2). 🟡
- EPS: basic = diluted 19.13 / 6.71 / 2.40 on 19,147,548 weighted shares after 9:10 bonus (Annexure IV B7, Pros p.185). Audited EPS 18.78 and 14.49 (AFS p.37) differ because audited PAT is 3595.25 (not 3662.83) and FY25 isn't bonus-adjusted. No dilutive instruments, no ESOP. 🟢
- Share capital: 96.5 lakh shares, bonus 86.85 lakh (9:10, board 25 Apr 2025, from surplus 868.50), private placements 6.80 lakh (23 Aug 2025) and 7.00 lakh (4 Sep 2025) at Rs 101 (premium 91): 138.00 face + 1255.80 premium, less 113.05 placement expenses charged to securities premium (Annexure A, Pros p.188-189). Authorised 2,500 lakh. Promoters 89.35% (Nimish 88.92%) pre-IPO. 🟢
- Dividends: none FY24 to FY26 (Annexure IV 6i). 
- CSR (Annexure ZK, Pros p.217-218): required 17.81, "spent" 18.00 FY26, though booked as "Provision for CSR Exp 18.00" in expenses (Annexure Y). Whether paid or transferred to an unspent account: NOT FOUND. FY24 required 11.28 spent 11.50. 🟡
- Events after balance sheet date: policy 2.20 only. No post-balance-sheet note appears in the restated notes. The IPO, bonus and placements preceded or followed the year; post-issue capitalisation is shown in ZC. NOT FOUND as a dedicated note.
- Going concern: stated as a basis (policies 2.1, 2.2). No uncertainty language anywhere. 🟢
- Direct debits to reserves: bonus 868.50 and placement expenses 113.05 (premium) go through reserves; earlier-year tax (0.26)/(0.75) debited to surplus (Annexure A). 🟢
- Auditor remuneration 6.00 (statutory 4.80, tax audit 1.20); the statutory audit fee is below the 5.00 of FY25. 🟡 low relative to a 143 Cr turnover. (derived Rs 143.3 Cr)
- Director personal expenses not separable (ZO). 🟡
- Ratios (Annexure ZE, Pros p.214): current 1.40 / 1.52 / 1.18; debt equity 1.43 / 1.38 / 1.87; DSCR 2.29 / 2.12 / 1.94; ROE 56.53% / 36.28% / 17.18%; RoCE 23.05% / 21.84% / 13.68%; net capital turnover 4.79 / 7.08 / 169.68. Audited note 38 (AFS p.37) reports different values for the same year: debt-equity 1.10 vs 1.43, DSCR 3.94 vs 2.29, RoCE 18.50% vs 23.05%, ROE 55.20% vs 56.53%, net profit ratio 25.09% vs 25.57%. The audited debt-equity 1.10 equals long-term borrowings only (9844.37 / 8951.16), contradicting its own formula (long-term + short-term borrowings; derived 1.43). Audited inventory turnover "117.56 times" cannot be reproduced (14326.69 / average inventory 3136.9 = 4.57 times, derived). OCR could have misread a digit, but FY25's 63.85 is also impossible (6.93 derived), so the error is in the source. Receivables turnover 4.47 and 5.42 reproduce. 🟡
- Restated vs audited net worth FY25: restated 4007.59 vs audited 3110.16 + 965.00 = 4075.16 (Pros p.186). 

---

## PASS 1 SUMMARY: top 10 findings ranked by investor importance

| # | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | FY26 CFO 1843.94 lakh (Rs 18.44 Cr) is 50% of PAT 3662.83 and 30% of EBITDA. CFO is flattered by classification: capex creditors 832.88 sit in operating inflow and retention money 297.44 in investing. Adjusted CFO is 713.62 to 1011.06 lakh (Rs 7.1 to 10.1 Cr, derived). Rs 12.5 Cr not found in the statement. | Annexure III Pros p.174; Annexure G p.199; Annexure L p.203 | 🔴 |
| 2 | Working capital absorbed 3919 lakh: raw material 3930.40 (up 14.6x, 303 days of consumption), vendor advances 3063.21 (up 4.7x, 21% of revenue), GST receivable 1878.59. Counterparties and purpose of vendor advances NOT FOUND; no provision. | Annexure M p.203; Annexure P p.206 | 🔴 |
| 3 | All debt rests on Bank of Baroda with guarantees from five promoter-family individuals and Darpan Infrastructure (corporate guarantee plus its Plot 201 as collateral); family land in Paria mortgaged. 97.60 guarantee commission paid to Darpan in FY26 with no visible P&L line. | Annexure B(A) notes Pros p.194-195; Annexure ZA p.210 | 🔴 |
| 4 | Darpan loan and payable do not reconcile across ZA, B(B) and Annexure F (467.67 loan principal shown also as trade payable; 87.27 FY26 payable unexplained; Annexure F shows nil related-party dues). Disclosure integrity weak on the one material group counterparty. | ZA p.210-211; B(B) p.196; F p.197 | 🔴 |
| 5 | Debt 12824.76 (D/E 1.43) with ballooning instalments, current maturities 1796.07, cash credit 98.7% used of 1200 and rate reset from 11.05% to 9.25% in Oct 2025. IPO pro forma cuts debt by 11500 lakh. 5-year schedule and covenants NOT FOUND. | Annexure B p.189-190; ZC p.212; Indebtedness p.223-224 | 🟡 |
| 6 | Revenue policy is dispatch/acceptance for sale of goods; nothing on the three contract models, customer-supplied steel, contract assets, or order book. Revenue "others" 789.93 includes traded goods though trade purchases are nil. | Policy 2.4 p.177; Annexure R p.206 | 🟡 |
| 7 | Receivable ageing clean (>6m 1.04%) but no ECL provision, no customer concentration and 99% shown as "not due"; receivable days 82 (avg basis) vs 13 in FY24; retention money 635.98 outside trade receivables. | Annexure N p.204-205 | 🟡 |
| 8 | MSME disclosure conflict: payables note shows 821.94 MSME (251.00 past due), ZG1 shows 735.61 unpaid and "generally within 45 days"; 43B(h) addback 263.45 implies delay; no s.16 interest. | Annexure F p.198; ZG1 p.216; ZB p.212 | 🔴 (small money, credibility) |
| 9 | Restatement changed profits materially: FY25 PAT -12% (1398.41 to 1230.58); depreciation basis and gratuity moved between years while the report states "no change in accounting policy"; FY26 includes +83.40 earlier-year tax credit; reserves reconciliation shows no FY26 net adjustment. | Annexure V p.186-187; IV A p.181 | 🟡 |
| 10 | Tax rate 17.16% (derived as the concessional regime) is undisclosed as to section and eligibility; effective 17.7%. Tax payable unpaid 561.78; late-payment interest 15.96. Income tax demand 226.93 "disposed" with outcome not disclosed. Also: audited note 38 ratios (D/E 1.10, inventory turnover 117.56) disagree with restated and with their own formulas. | Annexure ZB p.211-212; Z p.209-210; AFS p.37 | 🟡 |

Other items for pass 2: warranty provision absent; capital commitments nil despite Kutch build; amortisation collapse; rent items vs nil lease note; CSR "provision" vs "spent"; leave encashment liability not visible; FD lien; forex payable disclosure; who pays rent income 35.00; who are the fabrication-work payees (1282.41); statutory audit fee 4.80.

### Flags for downstream
- FLAG-CASH candidate: yes (CFO/PAT 50%, adjusted 19.5% to 28%; WC days up).
- Input gaps carried from B00: Annual report absent (HIGH); concall transcripts absent; screener P&L/BS/CF sheets absent; AFS OCR incomplete (pages above); no shareholder-letter or MD&A in AFS.
