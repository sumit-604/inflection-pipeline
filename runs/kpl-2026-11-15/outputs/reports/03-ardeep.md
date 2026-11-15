# STAGE 3: ANNUAL REPORT DEEP DIVE (BACKWARD READ): Kwality Pharmaceuticals Ltd (KPL)

Run: kpl-2026-11-15 | Model: claude-sonnet-5-5 | Source: Annual_Report_2026.pdf via page-marked .txt (AR FY2025-26, 242 pages). Prior-year AR (Annual_Report_2025.txt) used for backward comparison only.

UNIT RULE. Every AR figure is INR LAKHS on the face of each statement and note (100 lakh = 1 Cr). Nothing is converted here except where a line says "converted for comparison". Stage 10 converts once. "Derived" means arithmetic on anchored figures. "p.N" is the [page N] marker in the .txt (printed page number = N minus 3). Verdict symbols are written as GREEN / YELLOW / RED (text labels for the traffic-light marks).

Reading order followed: auditor's reports and CARO (p.98-112, p.174-183), financial statements (p.184-193), notes (p.194-241, via B02), MD&A (p.88-97), governance (p.59-87), Board report and annexures (p.30-58), MD letter and notice (p.4-29). Standalone and consolidated were both read.

## 0. LOAD-BEARING FACTS: WHAT THE AR CAN AND CANNOT REACH (checked before any phase)

| # | Load-bearing fact (B00; web brief, NOT anchored) | AR result | Status |
|---|---|---|---|
| 1 | Guidance vs delivery. FY27 revenue Rs 720 Cr+, EBITDA Rs 189-196 Cr, PAT Rs 122 Cr+. Q2 FY27 PAT and tax rate | AR carries one FY27 number: "revenue of over Rs 700 crore, up from our earlier guidance of Rs 650 crore", "profitability expected to scale in tandem" (MD letter, p.4). No FY27 EBITDA or PAT number: NOT FOUND IN DOCUMENT. Q2 FY27 results are outside the AR. FY26 delivery against the FY25 AR target: revenue 50,308.34 vs "Rs 500 crores" (AR FY25 p.105-106); EBITDA margin 23.50% vs "22-25%" (derived; see Phase 3C) | Partly reachable. Brief's 720 / 189-196 / 122 unverifiable here |
| 2 | Governance. Auditor (and per an analyst the company secretary) resigned 12 Nov 2026 | AR is dated 8 Aug 2026 (Board report p.46) and audit report 19 May 2026 (p.103), so it pre-dates the event. CARO (xviii): "no resignation of the statutory auditors during the year" (p.108). Auditor appointed 24 Sep 2024 for five years to the 46th AGM (Board report p.40). Company secretary named in AR: Ms Gurpreet Kaur (p.43, p.173) | Event NOT in AR. B00 notes the auditor filing is in the results pack; read it outside this stage |
| 3 | Cash conversion. CFO Rs 17 Cr vs PAT Rs 67 Cr; debtor days 203-208; Rs 60-70 Cr Middle East debtors stuck | CFO 1,658.62 vs PAT 6,734.60 (CFS p.191; P&L p.189) = 24.6% (derived). Year-end receivable days 203.2 (derived). Converted for comparison: CFO Rs 16.6 Cr, PAT Rs 67.3 Cr: matches the brief. Middle East debtor amount and country split: NOT FOUND IN DOCUMENT (Note 37 gives currency only) | Core claim CONFIRMED. Middle East sub-claim unreachable |
| 4 | Own-registration revenue vs partner-held; concentration | Only "asset-light out-licensing and supply model (90%)" as a label (MD&A p.91). No revenue split by registration holder, customer, partner or country. Export 24,979.72 vs domestic 25,326.18 (Note 25, p.222). Customers above 10% of revenue: NOT FOUND IN DOCUMENT | NOT FOUND. Open to B04 and the Role 5.5 extraction annex |

---

## PHASE 1: AUDITOR'S REPORT AND CARO

### 1A Core opinion

| Item | Standalone | Consolidated |
|---|---|---|
| Firm / partner | Vijay Mehra & Co, FRN 001051N; CA Amit Handa, M.No 502400; UDIN 26502400OKQXSI9034 (p.98, p.103) | Same firm and partner; UDIN 26502400RQHPPT7813 (p.174, p.180) |
| Opinion | Unmodified: "give a true and fair view in conformity with the Indian Accounting Standards" (p.98) | Unmodified, "based on the consideration of information of the subsidiary as referred to in the Other Matters paragraph" (p.174) |
| Date and place | 19-05-2026, Amritsar (p.103) | 19-05-2026, Amritsar (p.180) |
| Going concern language | Standard responsibility paragraphs only (p.99-100). No material uncertainty paragraph | Standard paragraphs (p.176-177). No material uncertainty paragraph |
| CARO (xix) | "no material uncertainty exists as on the date of the audit report that company is capable of meeting its liabilities existing at the date of balance sheet as and when they fall due within a period of one year" (p.108-109) | CARO is not repeated; consolidated 3(xxi) says no qualifications in the holding company CARO (p.180) |

Going concern result: no going-concern doubt language anywhere in either report or the notes. The Board states accounts are on a going-concern basis (Directors' responsibility, p.44-45).

### 1B Key Audit Matters

| Subject | Why key | How addressed | Risk |
|---|---|---|---|
| NONE REPORTED | The standalone report (p.98-103) and the consolidated report (p.174-180) contain no "Key Audit Matters" section and no sentence stating that there are none | n/a | YELLOW |

Reading. The two largest judgement areas in this company are revenue recognition on export shipments and receivable recoverability (28,005.24, nil provision). Neither is flagged as a KAM. SA 701 requires KAMs for listed entities, and a report with none should say so; that is an external-law recollection, NOT in the document, and flagged for the verifier. The absence of any KAM paragraph on a book where receivables are 69.0% of current assets (derived: 28,005.24 / 40,567.75) is itself a signal that the audit narrative is thin.

### 1C Emphasis of Matter and Other Matters

| Item | Detail | Anchor |
|---|---|---|
| Emphasis of Matter | NONE in either report | p.98-103; p.174-180 |
| Other Matters (consolidated) | Subsidiary KWALITY PHARMACEUTICALS AFRICA LIMITADA NOT audited by the group auditor: total assets 126.36 lakh (PY 169.34), revenue 29.12 (PY nil), net loss 0.06 (PY 8.71), net cash outflow 41.37. Opinion rests "solely on such unaudited Financial Results", "not material to the group" | Consolidated auditor's report p.178 |
| Other Information | Standalone report says the other information "is expected to be made available to us after the date of this audit report" (p.98). The Board report and MD&A are dated 8 Aug 2026, 81 days after the 19 May 2026 audit report | p.98; p.46 |
| Boilerplate | Consolidated responsibility text refers to "the Group and its associate" (p.175-176). The AR has no associate (AOC-1 Part B "Not applicable", p.241) | p.175-176; p.241 |
| Audit trail | Standalone report states edit-log feature "operated throughout the year" (Rule 11(g), p.103). The consolidated report's Rule 11 list ends at clause (g) = CARO and has no audit-trail statement (p.180) | p.103; p.180 |

### 1D CARO 2020 clause by clause (standalone Annexure A, p.104-109)

| Clause | Auditor statement | Adverse or qualified? | Risk |
|---|---|---|---|
| (i)(a)-(e) PPE | Records proper. Management "did not conduct a physical verification of all" PPE; "systematic verification program". Registered office and Amritsar plant on 49-year lease from promoters Mr Ramesh Arora and Mr Ajay Arora; HP unit on government lease (p.104) | Not adverse. Promoter-owned land under the main plant | YELLOW |
| (ii)(a) Inventory | Physical verification at reasonable intervals; "no material discrepancy" (p.105) | Clean | GREEN |
| (ii)(b) Bank statements | Working-capital limits above Rs 5 crore. Monthly statements "though have insignificant difference, are largely in agreement" with books (p.105). Difference not quantified | Hedged wording, no amount | YELLOW |
| (iii) Loans to related parties | "has not made any investments in, provided any guarantee or security or granted any loans" (p.105). Note 1 says the company "granted loans" to the subsidiary (B02 Pass 2 N2.16) | Not adverse; wording conflict is small | GREEN |
| (v) Deposits | None accepted (p.105) | Clean | GREEN |
| (vii)(a) Undisputed statutory dues | "During the year, there were delays in the deposit of certain GST and TDS dues and in filing the related statutory returns", regularised "through payment of the applicable interest and late fees". None over six months outstanding (p.105-106) | Adverse remark on timeliness. Amount of delay and interest NOT FOUND IN DOCUMENT | YELLOW |
| (vii)(b) Disputed dues | GST order 14/GST/ADC/JAL/2024-2025: 630.06 (tax 315.03 + equal penalty; interest unquantified); Commissioner (Appeals) dismissed; writ CWP-12033-2026 in P&H High Court. SCN AE/51/2024-25: 3,026.07 (ITC 1,513.03 + equal penalty); writ CWP-34165-2024, adjudication stayed. DRC-07 orders 30/12/2024: penalty 2.81 (FY18), 6.75 tax + 6.75 penalty (FY20), 12.62 tax + 12.70 penalty (FY21), appeals pending (p.106-107) | Adverse: total 3,697.75 disputed (Note 34, p.226); ties to the three components (630.06 + 3,026.07 + 41.63 = 3,697.76, derived) | RED/YELLOW |
| (viii) Unrecorded income | None surrendered (p.107) | Clean | GREEN |
| (ix) Borrowings | No default to bank, FI, government or debenture holders; term loans applied to purpose; no short-term funds used long term (p.107) | Clean | GREEN |
| (x) Capital raised | No IPO/FPO or preferential allotment (p.107) | Clean | GREEN |
| (xi) Fraud | (a) none noticed; (b) no ADT-4; (c) "has not received any whistler blower complaints" (p.107-108) | Clean | GREEN |
| (xiii) RPT | "all transactions with related parties are in compliance with sections 177 and 188" (p.108) | Clean on its face. Test against Note 40 in Phase 2B | YELLOW |
| (xiv) Internal audit | Adequate system; internal auditor reports considered (p.108) | Clean | GREEN |
| (xv) Non-cash with directors | None (p.108) | Clean | GREEN |
| (xvii) Cash loss | None in current or prior year (p.108) | Clean | GREEN |
| (xviii) Auditor resignation | None during the year (p.108) | Clean for FY26; event after AR | GREEN |
| (xix) Material uncertainty | Quoted in 1A (p.108-109) | Clean | GREEN |
| (xx) CSR | No unspent amount; nil ongoing-project balance at 31 Mar 2026 (p.109) | Clean. Required 74.30 = spent 74.30 (Annexure D, p.56-58; Note 42(g) standalone p.172) | GREEN |

### 1E Auditor continuity

| Item | Detail | Anchor |
|---|---|---|
| Firm and tenure | Vijay Mehra & Co, appointed at the 41st AGM on 24 Sep 2024 for five years to the 46th AGM. FY26 is year 2 | Board report p.40 |
| Rotation | Due at the 46th AGM (about Sep 2029) | Board report p.40 |
| Audit fee | Rs 8,00,000 in FY26 and Rs 8,00,000 in FY25 (flat) = 8.00 lakh | Corporate governance disclosure 8, p.79; Note 32, p.225 |
| Other services | Rs 5,42,000 FY26 (Rs 4,50,000 FY25) = 5.42 lakh, +20.4% | Same |
| Ratio | Non-audit 5.42 / audit 8.00 = 0.68; non-audit is 40.4% of total fees 13.42 (derived). Non-audit does NOT exceed audit | Derived |
| Fee against scale | Audit fee 8.00 is 0.016% of revenue 50,308.34 (derived). Fee flat while revenue rose 35.9% and receivables 81.5% | Derived |
| What "other services" are | NOT FOUND IN DOCUMENT | Note 32 |
| Network firm fees | "Neither Company nor its wholly owned subsidiary company has paid fees to network firm" (p.79). The subsidiary is 51% owned (Note 14(a), p.215), not wholly owned | p.79 |
| Subsequent resignation | 12 Nov 2026 per web brief. NOT in AR. Reasons unknown here | B00 |

### 1F Standalone vs consolidated

| Item | Standalone | Consolidated | Reading |
|---|---|---|---|
| Revenue from operations | 50,305.89 | 50,308.34 | Gap 2.45 = subsidiary revenue 29.12 less intra-group sale 26.68 (derived) |
| PAT | 6,734.66 | 6,734.60 | Gap 0.06 = subsidiary loss |
| FY25 PAT | 3,988.97 | 3,980.27 | Gap 8.70 = subsidiary FY25 loss (auditor Other Matters p.178) |
| Subsidiary revenue | n/a | 29.12, of which 26.68 is a sale by KPL (Note 40, p.239) | 91.6% of the subsidiary's revenue came from the parent (derived) |
| Subsidiary net liabilities | n/a | 256.68 (126.36 assets less 383.04 outside liabilities, AOC-1 p.241) | Investment 354.78 is carried at cost, no impairment |
| Subsidiary audit | n/a | Unaudited input, not audited by anyone named | Control gap, small in size |
| Audit-trail statement | Yes | None | Disclosure gap |
| Other-auditor reliance | n/a | None; the subsidiary has no reported auditor | Gap |

### Phase 1 summary

| Area | Finding | Risk |
|---|---|---|
| Opinion | Unmodified both sets. No going-concern doubt | GREEN |
| KAMs | None reported on a book with 28,005.24 of unprovided receivables | YELLOW |
| CARO | One adverse item: late GST/TDS deposits and returns (vii)(a). One large disputed-dues item (vii)(b): 3,697.75 | YELLOW |
| Auditor | Two-year tenure; non-audit fees 40% of total, below audit; flat audit fee | YELLOW |
| Consolidated | Subsidiary unaudited; no audit-trail statement; "associate" boilerplate | YELLOW |

**Phase 1 verdict: YELLOW.**
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop on the audit opinion alone, because both opinions are unmodified and CARO reports no fraud, default or going-concern doubt. The thin audit narrative (no KAM on receivables) is a reason to read Phase 2 and 3 closely. Continue.

---

## PHASE 2: NOTES TO FINANCIAL STATEMENTS (verify, extend, reconcile)

### 2.0 Verification of the stage 2 Top 15 against the document

I re-opened each number at its source page. All 15 hold. Four needed a wording refinement; none changes a number or a rating.

| Rank | Finding (short) | Re-check at source | Result |
|---|---|---|---|
| 1 | CFO 1,658.62 vs PAT 6,734.60 = 24.6%; receivables +12,574.66; FCF -3,235.42; FY25 like-for-like 85.3% | CFS p.190-191: CFO 1,658.62; receivables change -12,574.66; capex 4,460.15 + 433.89 = 4,894.04; 1,658.62 - 4,894.04 = -3,235.42. FY25: ST borrowing 7,855.88 to 9,732.63 = +1,876.75 (AR FY25 Note 18); other financial liabilities 323.06 to 500.58 = +177.52; sum 2,054.27 = CFS line "Financial Current Liabilities" FY25 (p.190). 5,271.78 - 1,876.75 = 3,395.03; / 3,980.27 = 85.3%. Two-year 5,053.65 / 10,714.87 = 47.2% | ✓ verified |
| 2 | Receivable days 135.9 / 152.1 / 203.2; receivables 69.0% of CA | Receivables 11,438.57 (FY24, AR FY25 Note 9), 15,430.58, 28,005.24; revenue 30,717.18 / 37,019.70 / 50,308.34. Days on year-end basis reproduce. 28,005.24 / 40,567.75 = 69.0% | ✓ verified |
| 3 | No ECL; 3,030.29 over six months; 564.29 over two years; subsidiary debtor 116.73 over three years | Note 9(a) p.212: 1,463.91 + 1,002.09 + 89.74 + 474.55 = 3,030.29; 89.74 + 474.55 = 564.29. Standalone Note 10(a) p.141 more-than-3-years 591.28 vs consolidated 474.55: gap 116.73 = subsidiary debtor | ✓ verified |
| 4 | At least 1,166.32 of FY25 one-year-plus balances left the ledger | FY25 1-2y 566.17 + 2-3y 517.50 + >3y 646.94 = 1,730.61 (Note 9(b) p.212). FY26 2-3y + >3y = 564.29. 1,730.61 - 564.29 = 1,166.32. Arithmetic holds | ✓ verified. Refinement: cash collection is the ordinary exit route and is not excluded. The point is that nothing in the notes lets a reader tell collection from credit note or set-off |
| 5 | FX receivables 8,101.83 to 15,599.05, unhedged, 55.7%; USD lakh 90.27 to 164.28 | Note 37 p.229: USD 15,550.18 + EUR 5.45 + AED 43.42 = 15,599.05; FY25 7,712.22 + 266.35 + 123.26 = 8,101.83. 15,599.05 / 28,005.24 = 55.7%. (15,599.05 - 8,101.83) / 12,574.66 = 59.6%. USD 164.28 / 90.27 = +82.0% | ✓ verified. Refinement: the 55.7% counts foreign-currency balances; INR-denominated export invoices, if any, would sit in the remainder |
| 6 | GST contingent 3,697.75 = 11.2% of net worth, 54.9% of PAT | 3,697.75 / 32,992.09 = 11.2%; / 6,734.60 = 54.9%. Components tie (Phase 1D). The same 3,697.75 appears in FY25 (Note 34, p.226) | ✓ verified. Refinement: total unchanged year on year despite the Commissioner (Appeals) dismissal; interest unquantified |
| 7 | Payables 5,579.34 to 10,168.66; days 108.6 to 146.6; CFO -2,930.69 ex payables | Note 20 p.219. Note 39 payables turnover 3.22 on purchases 25,317.25 (p.236). 10,168.66 / 25,317.25 x 365 = 146.6. 1,658.62 - 4,589.31 = -2,930.69 | ✓ verified. Refinement: "Others" payables rose 3,461.35 to 8,252.41 (+138.4%) while MSME payables fell 2,117.99 to 1,916.25. Capital creditors inside trade payables: NOT FOUND IN DOCUMENT |
| 8 | Cash 73.64; borrowings 13,046.06; WC lines 67.4% drawn | Note 10 p.213: 73.64 vs 1,202.02 (incl. cheque in hand 1,050.00). Borrowings 2,940.02 + 10,106.04 = 13,046.06. Standalone Note 17 p.147-148: sanctioned HDFC 7,185 + Axis 4,000 + ICICI EPC 1,500 = 12,685; drawn 5,331.30 + 1,958.12 + 1,256.72 = 8,546.14 vs Note 19 8,546.17; 8,546.17 / 12,685 = 67.4% | ✓ verified |
| 9 | Kaler and Iair flows; Board says no conflict RPT | Note 40 p.238-239: Kaler sale 121.48, return 262.75; Iair services 20.25, sale of machine 6.40; both prior year nil. Board report para 30 (p.41-42): "no related party transactions ... which may have a potential conflict" | ✓ verified |
| 10 | Gross margin 48.63% vs 50.70%; operating 23.50% vs 21.71% | (50,308.34 - 25,843.42) / 50,308.34 = 48.63%; (37,019.70 - 18,248.64) / 37,019.70 = 50.70%. EBITDA 11,824.38 / 50,308.34 = 23.50%; 8,038.73 / 37,019.70 = 21.71%. MD&A EBITDA "Rs 118 Crore" (p.91) matches 11,824.38 | ✓ verified |
| 11 | Capex 4,894.04 (2.0x FY25); CWIP 1,700.62; BE study 433.89; capital advance 594.50 | CFS p.190-191; BS p.184; Note 18 p.218. FY25 capex 2,329.27 + 171.00 = 2,500.27; ratio 1.96x | ✓ verified |
| 12 | Customer advances 6.01% / 1.34% / 1.75% of revenue | FY24 1,847.50 / 30,717.18 = 6.01% (AR FY25 Note 21); FY25 497.03 / 37,019.70 = 1.34%; FY26 879.23 / 50,308.34 = 1.75% (Note 22 p.221) | ✓ verified |
| 13 | Gratuity DBO 283.52 (+78.2%); past service 82.94 | Note 38 p.231: 283.52 vs 159.11 = +78.2%; plan assets 125.90 / 283.52 = 44.4% (FY25 117.45 / 159.11 = 73.8%). Exceptional item 82.94: Note 33 (p.226) cites Note 2.2(m); footnote to Note 30 (p.224) says "pursuant to a court order" | ✓ verified, conflicting cause confirmed |
| 14 | Ind AS 116 via opening reserves, +4.47 | Note 15 p.216: "Prior-period adjustment ... Ind AS 116 ... 4.47". Rent to Ramesh and Ajay 1.08 each (Note 40) | ✓ verified. [INFERENCE] on promoter lease stands |
| 15 | Subsidiary net liabilities 256.68; NCI -167.47; investment 354.78 | AOC-1 p.241: assets 1,26,36,109 less outside liabilities 3,83,03,966 = -2,56,67,857 Rs = -256.68 lakh. BS p.182 NCI -167.47. Note 40 p.238 investment 354.78 | ✓ verified |

triple_pass_verification: verified 15 of 15. Discrepancies: none material (four wording refinements above).

### 2A Accounting policy aggressiveness (extended)

| Policy | Position | Aggressive or conservative | Anchor |
|---|---|---|---|
| Revenue | "substantial risk and rewards" (old IAS 18 wording); dispatch / shipped-on-board. Revenue net of returns. Kaler return 262.75 exceeds its sale 121.48 | Neutral to aggressive: no control-transfer test; return netting hides gross volume | Note 2.2(o) p.202; B02 |
| Receivable impairment | Incurred-loss wording ("objective evidence"); no ECL matrix; nil provision FY24 to FY26 | AGGRESSIVE. The single largest policy risk | Note 2.2(p) p.202-203; Note 9 |
| Depreciation | WDV; plant 20 years, building 20 to 30, vehicles 8; table unchanged year on year | Plant life longer than the 15 years I recall from Schedule II (external recollection, NOT in the document; flagged for verifier). Depreciation is 3.9% of revenue (1,981.04 / 50,308.34, derived) | Note 2.2(g) p.198 |
| Capitalisation | Bioequivalence study 433.89 capitalised, 5-year life; Ind AS 38 test not stated. Amortisation charged 2.96 in year | Mildly aggressive: R&D-type cost moved from P&L to the balance sheet. Effect on FY26 PBT: 433.89 less 2.96 = 430.93, 4.8% of PBT 8,949.21 (derived, if expensed) | Note 2.2(g); Note 4 p.208 |
| Borrowing cost | No capitalisation policy. All finance cost 1,097.04 expensed although CWIP is 1,700.62 | Conservative on this item (no interest taken to the balance sheet) | Note 31 p.224 |
| Inventory | Lower of cost and NRV, weighted average; stock written off nil both years | Neutral; inventory fell 6.2% as revenue rose 35.9% | Note 8 p.211 |
| Ind AS 116 | First recognised FY26 through reserves, FY25 not restated; rate NOT FOUND | Small (net +4.47) but a method error signal | Note 2.2(n) p.201-202 |
| Duty drawback | 202.10 booked in other income (70.7% of 285.86) | Neutral; recognised on accrual of claims | Note 26 p.222; Note 2.2(o) |
| Deferred tax | Method change to balance-sheet approach with unfilled template text | Presentation defect | Note 6 p.210 |
| Cash definition | FY25 cash 1,202.02 includes cheque in hand 1,050.00 (87.4%) | A cheque not yet banked counted as cash at FY25. FY26 cash is 73.64 with no such item | Note 10 p.213 |

### 2B RPT map (extended percentages)

| Counterparty | Nature | FY26 | FY25 | % of FY26 revenue 50,308.34 | Signal |
|---|---|---|---|---|---|
| Five executive directors | Remuneration | 294.00 | 252.00 | 0.58% | +16.67%; PAT +69.2% |
| Three relatives (Kanika Arora 3.00, Aastha Seth 4.20, Geetika Thukral 6.00) | Remuneration | 13.20 | 13.20 | 0.03% | Roles NOT FOUND IN DOCUMENT |
| Promoters Ramesh Kumar and Ajay Kumar Arora | Rent, 1.08 each | 2.16 | 2.16 | 0.004% | Nominal rent on the main plant land (49-year lease, CARO (i)(c)) |
| Independent directors | Sitting fees | 7.50 | 4.37 | 0.015% | Note 32 p.225 shows 7.50; Note 40 lines add to 7.50 |
| Kaler Biopharmachem Pvt Ltd ("Director Interested") | Sale of goods 121.48; sale return 262.75 | 384.23 gross | nil | 0.76% | Return is 2.16 times the sale. First year. Owner and director NOT FOUND |
| Iair Infocom Pvt Ltd ("Director Interested") | Purchase of services 20.25; sale of machine and spares 6.40 | 26.65 gross | nil | 0.05% | First year. Owner and director NOT FOUND |
| Kwality Pharmaceuticals Africa Limitada (51% subsidiary) | Sale of goods 26.68; debtor 116.73; investment 354.78 | 26.68 | nil | 0.05% | Eliminates on consolidation but listed in a consolidated note; debtor over three years old |

Totals. Executive pay plus relatives 307.20 = 3.43% of PBT 8,949.21 and 4.56% of PAT. New director-interested flows 410.88 gross (Kaler 384.23 + Iair 26.65) = 0.82% of revenue. Net of the return, Kaler is a net sale of -141.27 (derived): KPL took back more goods than it sold.

Value-extraction signals: (1) a sale return larger than the sale to a director-interested party, in its first year; (2) Board report and Corporate Governance disclosure 1 (p.77) both say no RPT conflicts, while Note 40 labels two parties "Director Interested"; (3) Annexure B pay-to-median ratio of 56.39 for the MD, with the implied median pay about Rs 1.49 lakh (84.00 / 56.39, derived). No loans to related parties (Corporate Governance disclosure 11, p.79). Promoter-owned properties are mortgaged as collateral for company loans (standalone Note 17 p.149), which is alignment, not extraction.

### 2C Contingent liabilities

| Item | Amount | % of net worth 32,992.09 | % of PAT 6,734.60 | Flag |
|---|---|---|---|---|
| GST disputes (all three items) | 3,697.75 | 11.2% | 54.9% | Neither >25% of net worth nor >100% of PAT. No provision. Interest on the 630.06 order unquantified |
| Of which tax only (SCN 1,513.03 + order 315.03 + DRC tax 19.37) | 1,847.43 (derived) | 5.6% | 27.4% | Equal penalty doubles the exposure |
| Other contingent items (bank guarantees, LCs, bills discounted, capital commitments) | NOT FOUND IN DOCUMENT | n/a | n/a | Facility list implies BG, FLC (B02 N2.17) |

Balance-sheet link: IGST refundable on exports 852.37 (FY25 1,279.37) sits in other financial assets (Note 12, p.213) while the Commissioner's order alleges "erroneous refund of IGST" for FY18 to FY23 (Note 34). The exposure to that receivable is not discussed.

### 2D Receivables

| Metric | FY24 | FY25 | FY26 | Anchor |
|---|---|---|---|---|
| Total | 11,438.57 | 15,430.58 | 28,005.24 | Note 9; AR FY25 |
| Over 6 months | 3,205.61 (28.0%) | 2,883.08 (18.7%) | 3,030.29 (10.8%) | Note 9(a)/(b) p.212; AR FY25 Note 9 |
| Over 1 year | 2,666.26 (1,768.15 + 648.46 + 249.65) | 1,730.61 | 1,566.38 (1,002.09 + 89.74 + 474.55) | Note 9 |
| Over 2 years | 898.11 | 1,164.44 | 564.29 | Note 9 |
| Provision | nil | nil | nil | Note 9 |
| Year-end days | 135.9 | 152.1 | 203.2 | Derived |
| Management ratio: debtors turnover | 3.25 | 2.72 | 2.30 | MD&A ratio table p.96; AR FY25 MD&A |

Split of days (derived; assumes foreign-currency receivables = export, which is approximate):

| Segment | FY25 receivable | FY25 days | FY26 receivable | FY26 days |
|---|---|---|---|---|
| Export (FX balances) | 8,101.83 | 151.3 on 19,543.82 | 15,599.05 | 227.9 on 24,979.72 |
| Domestic (balance) | 7,328.75 | 153.1 on 17,475.88 | 12,406.19 | 178.8 on 25,326.18 |

Export days rose 76.6 and domestic days rose 25.7. Both segments lengthened, export far more. Domestic is not clean: 178.8 days is long for domestic sales. Domestic customer identity is NOT FOUND (no concentration table). Unbilled receivables: none shown. The >6-month share fell because the denominator doubled, not because balances cleared (3,030.29 vs 2,883.08 in rupees).

### 2E Inventory

| Metric | FY25 | FY26 | Anchor |
|---|---|---|---|
| Inventory | 8,346.57 | 7,825.23 (-6.2%) | Note 8 p.211 |
| Finished goods | 968.88 | 932.31 | Note 8 |
| Raw + packing | 7,134.00 (5,239.29 + 1,894.64) | 6,635.53 (4,799.12 + 1,836.41) | Note 8 |
| Write-downs | nil | nil | Note 8 |
| Days on COGS (derived) | 167.0 | 110.5 | COGS 18,248.64 and 25,843.42 |

Finished goods fell while revenue rose 35.9%. That fits a sold-out or made-to-order flow, or a deliberate rundown. The AR does not say which.

### 2F Borrowings (maturity wall, covenants, pledge, ICDs)

| Item | Detail | Anchor |
|---|---|---|
| Total | 13,046.06 = long-term 2,940.02 + short-term 10,106.04 (of which working capital 8,546.17 and current maturities 1,559.87) | BS p.185; Note 19 p.219 |
| Debt / equity | 0.395 (AR ratio 0.39) | Derived; p.96 |
| Net debt / EBITDA | (13,046.06 - 73.64 - 285.59) / 11,824.38 = 1.07x (FY25 1.22x) | Derived |
| Maturity wall | Current maturities 1,559.87 within 12 months. Long-term 2,940.02: year-wise table NOT FOUND IN DOCUMENT | Note 16 p.218 |
| Covenants, interest rates | NOT FOUND IN DOCUMENT | |
| Security | Stock, book debts, plant, FDR margin; equitable mortgage on six properties including promoter-owned Nag Kalan land and a residential house owned by Ramesh and Ajay (standalone Note 17 p.149) | Standalone p.149 |
| Vehicle loans | Five luxury-car loans total 486.11 (B02): includes a Range Rover loan of 251 financed, 228.71 outstanding, and two Mercedes loans (92.97 and 122.75 outstanding) | Standalone Note 17 p.147-148 |
| ICDs given | None. CARO (iii) nil; Corporate Governance disclosure 11 nil | p.105; p.79 |
| Defaults | None, CARO (ix)(a) | p.107 |
| Limit utilisation | 8,546.17 of 12,685 sanctioned = 67.4% | Derived |

### 2G Deferred tax and tax rate

Deferred tax asset 250.18 (FY25 161.48), deferred tax credit 88.70 (FY25 158.94) (BS p.184; P&L p.189). Total tax 2,214.62 / PBT 8,949.21 = 24.7% (FY25 1,433.72 / 5,413.99 = 26.5%), derived. No reconciliation of statutory to effective rate: NOT FOUND IN DOCUMENT. Tax for earlier years 23.29 (FY25 123.19).

### 2H Exceptional items, goodwill, ESOP, leases, post balance sheet events

| Item | Detail | Anchor |
|---|---|---|
| Exceptional | One item, 82.94 past service cost; nil FY25. Cause stated two ways: Labour Codes (Note 2.2(m)) and a "court order" (Note 30 footnote). Three-year pattern: single occurrence | Note 33 p.226; Note 30 p.224 |
| Goodwill | None | BS p.184 |
| ESOP | None; no dilution; basic EPS = diluted EPS 64.90 | Board report para 38 (p.43); Note 35 |
| Leases | Liability 23.99 non-current + 0.06 current; ROU 28.04 net | Notes 18, 22 |
| Post balance sheet events | No Ind AS 10 note. The Board report records events after year end: Kartik Kapur resigned 2 Jun 2026; Swanith Kapoor appointed 2 Jun 2026; HP plant head resigned 14 Mar 2026 and replaced 2 Apr 2026 | Board report p.33-34; Corporate Governance p.64 |
| Board report on material changes | "No material changes and commitments affecting the financial position ... between the end of the financial year ... and the date of this Report" (8 Aug 2026) | p.42 |

### Phase 2 summary and reconciliation with stage 2

| Dimension | Stage 2 score | This stage |
|---|---|---|
| Revenue recognition | 5 | Agree |
| Capitalisation | 6 | Agree |
| Provisioning | 3 | Agree. Nil ECL on 28,005.24 and nil on 3,697.75 contingent items |
| RPT fairness | 5 | Agree; I add the sale-return-over-sale point and the "Director Interested" label against the Board report |
| Disclosure | 4 | Agree |
| Consistency | 5 | Agree |
| Overall | 5 | 5 |

My Phase 2 verdict is YELLOW with a RED on provisioning. It matches the stage 2 score of 5/10 (moderate). No disagreement to explain.

Cross-reference with Phase 1 KAMs. Phase 1 reports no KAM. Phase 2 shows the two items a KAM would normally cover (receivable recoverability, and the GST contingencies) are the two weakest areas in the notes. This is a contradiction between a clean audit narrative and the notes. It is called out here.

**Phase 2 verdict: YELLOW (RED on provisioning).**
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because nothing indicates a misstatement of a size that breaks the accounts. A reviewer would have reason to demand the receivable ageing by customer and country before relying on reported profit. Continue.

---

## PHASE 3: FINANCIAL STATEMENTS (cash flow first)

### 3A Cash flow

| Line | FY26 | FY25 (as reported) | FY25 like-for-like | Anchor |
|---|---|---|---|---|
| PBT | 8,949.21 | 5,413.99 | | CFS p.190 |
| Operating profit before WC | 12,075.77 | 8,214.28 | | p.190 |
| Receivables | -12,574.66 | -3,992.01 | | p.190 |
| Inventories | +521.34 | -507.83 | | |
| Other financial assets, current | -1,650.34 | +359.86 | | |
| Trade payables | +4,589.31 | +1,147.63 | | |
| Financial current liabilities | +27.39 | +2,054.27 | +177.52 (ex 1,876.75 borrowing) | |
| Working capital total | -8,340.48 | -1,363.51 | -3,240.26 | derived |
| Cash generated from operations | 3,735.30 | 6,850.77 | 4,974.02 | |
| Tax paid | -2,076.67 | -1,578.99 | | |
| CFO | 1,658.62 | 5,271.78 | 3,395.03 | p.191 |
| CFO / PAT | 24.6% | 132.4% | 85.3% | Derived |
| CFO / EBITDA (11,824.38; 8,038.73) | 14.0% | 65.6% | 42.2% | Derived |
| Capex (PPE + intangibles) | -4,894.04 | -2,500.27 | | p.191 |
| FCF (CFO - capex) | -3,235.42 | +2,771.51 (reported); +894.76 (like-for-like) | | Derived |
| Capex / depreciation | 2.47x (4,894.04 / 1,981.04) | 1.37x | | Derived |
| M&A | none | none | | |
| Borrowings raised / repaid | +3,169.31 / -1,368.31 | +879.41 / -1,335.65 | | p.191 |
| Interest paid | -1,097.04 | -987.79 | | |
| Closing cash | 73.64 | 1,202.02 | | |

CFO quality checks.
1. One-time inflators in FY26 CFO: none identified. Positive items are payable stretch (+4,589.31) and inventory release (+521.34).
2. Interest classification: interest paid is in financing in both years (p.191). Clean.
3. FY25 CFO carries 1,876.75 of short-term borrowing inside operating cash (exact tie shown in 2.0). FY25 was therefore overstated against a like-for-like basis. FY26 is clean on this line (financial current liabilities +27.39 equals the balance sheet change 527.96 - 500.58 = 27.38).
4. Payables stretch is the main support: without the payables increase FY26 CFO is -2,930.69.
5. Investing inflows that flatter FCF: capital advances received 592.81 shown in investing (Note 18 "Capital Advances 594.50"; counterparty and purpose NOT FOUND IN DOCUMENT); decrease in other long-term assets +473.53; disposal proceeds 324.20. Net investing outflow is -3,490.96, less than capex of 4,894.04.
6. Cash pile: 73.64 plus FDR 285.59 = 359.23 against borrowings 13,046.06. The FY25 cash of 1,202.02 included a cheque in hand of 1,050.00; excluding it, FY25 cash was 152.02 (derived), so the FY26 cash decline is mostly the cheque clearing.

Two-year CFO / PAT on a consistent basis is 47.2%. The deterioration is the FLAG-CASH trigger.

### 3B Balance sheet

| Line | FY26 | FY25 | Change | Anchor |
|---|---|---|---|---|
| PPE | 14,972.59 | 14,398.45 | +4.0% | BS p.184 |
| Intangibles | 584.54 | 170.72 | +242% | |
| CWIP | 1,700.62 | nil | new | |
| Other non-current assets | 1,145.23 | 1,618.76 | -29.3% | |
| Inventories | 7,825.23 | 8,346.57 | -6.2% | |
| Trade receivables | 28,005.24 | 15,430.58 | +81.5% | |
| Cash + FDR | 359.23 | 1,475.53 | -75.7% | |
| Other current financial assets | 882.01 | 1,279.37 | -31.1% | |
| Other current assets | 3,496.04 | 1,845.70 | +89.4% | |
| Total assets | 59,220.91 | 44,727.16 | +32.4% | |
| Total equity | 32,992.09 | 26,239.59 | +25.7% | BS p.185 |
| Borrowings | 13,046.06 | 11,244.52 | +16.0% | |
| Trade payables | 10,168.66 | 5,579.34 | +82.3% | |
| Total liabilities | 26,228.82 | 18,487.57 | +41.9% | derived |

Key ratios.

| Ratio | FY26 | FY25 | Basis |
|---|---|---|---|
| Debt / equity | 0.395 | 0.429 | derived (AR shows 0.39 and 0.42) |
| Net debt / EBITDA | 1.07x | 1.22x | derived |
| Current ratio | 1.80 | 1.67 | 40,567.75 / 22,552.00; 28,377.75 / 16,950.50 |
| Quick ratio | 1.45 | 1.18 | derived, ex inventory |
| Interest coverage (PBT + finance cost) / finance cost | 9.16x | 6.48x | AR p.96 shows 9.15 and 6.48 |
| ROCE | 21.8% on EBIT 10,046.25 / (equity 32,992.09 + borrowings 13,046.06) | 17.1% on 6,401.78 / 37,484.11 | derived; AR Note 39 shows 21.94% on a capital base of 45,787.97 that I cannot rebuild, and ROCE and ROI show identical figures (B02) |
| ROE (year-end equity) | 20.41% | 15.17% | Note 39 p.236 |
| Goodwill / net worth | nil | nil | |

DuPont (year-end balances, derived):

| Component | FY26 | FY25 |
|---|---|---|
| Net margin (6,734.60 / 50,308.34; 3,980.27 / 37,019.70) | 13.39% | 10.75% |
| Asset turnover (revenue / total assets) | 0.849 | 0.828 |
| Equity multiplier (total assets / equity) | 1.795 | 1.705 |
| ROE | 20.4% | 15.2% |

ROE gain comes mainly from margin (+24.5% relative) with small help from turnover (+2.6%) and leverage (+5.3%). It is operational, not leverage-led. The current ratio of 1.80 is flattered by receivables (69.0% of current assets). Of 40,567.75 current assets, 28,005.24 is receivables that carry no provision and are 203 days old.

### 3C P&L

| Line | FY26 | FY25 | YoY | % of revenue FY26 / FY25 |
|---|---|---|---|---|
| Revenue from operations | 50,308.34 | 37,019.70 | +35.9% | |
| COGS (materials 24,081.02 + stock-in-trade 1,734.63 + inventory change 27.77) | 25,843.42 | 18,248.64 | +41.6% | 51.37% / 49.30% |
| Gross profit | 24,464.92 | 18,771.06 | +30.3% | 48.63% / 50.70% |
| Employee benefits | 5,404.26 | 4,378.39 | +23.4% | 10.74% / 11.83% |
| Other expenses | 7,236.28 | 6,353.93 | +13.9% | 14.38% / 17.16% |
| EBITDA (ex other income) | 11,824.38 | 8,038.73 | +47.1% | 23.50% / 21.71% |
| Depreciation | 1,981.04 | 1,828.96 | +8.3% | |
| Other income | 285.86 | 192.01 | +48.9% | |
| Finance cost | 1,097.04 | 987.79 | +11.1% | |
| PBT before exceptional | 9,032.16 | 5,413.99 | +66.8% | |
| Exceptional | 82.94 | nil | | |
| PBT | 8,949.21 | 5,413.99 | +65.3% | 17.79% / 14.62% |
| Tax | 2,214.62 | 1,433.72 | +54.5% | effective 24.7% / 26.5% |
| PAT | 6,734.60 | 3,980.27 | +69.2% | 13.39% / 10.75% |
| EPS basic = diluted | 64.90 | 38.36 | +69.2% | no dilution |

Other income composition. 285.86 = 3.19% of PBT (flag threshold 20% not met). Duty drawback 202.10 is 70.7% of other income; profit on sale of assets 71.22 (one-off, FY25 2.84); FDR interest 12.54 (Note 26, p.222). Excluding the asset-sale gain, other income would be 214.64.

Margin waterfall. Gross margin fell 2.07 points. EBITDA margin rose 1.79 points. The bridge comes from lines that fell as a share of revenue: other expenses -2.78 points (distribution 1,415.15 vs 1,496.78, -5.5% in rupees, 2.81% vs 4.04% of revenue; testing and laboratory 132.97 vs 273.91, -51.5%; factory expense 151.31 vs 213.65, -29.2%) and employee cost -1.09 points. Lines that rose: commission 363.97 vs 157.25 (+131.5%), travelling 173.79 vs 57.27 (+203.5%), advertising 324.52 vs 168.10 (+93.1%), power 2,669.12 vs 2,337.31 (+14.2%) (Note 32 p.225). Distribution cost fell in rupees while sales grew 35.9% in value. No reason is given in the AR. I cannot say whether freight moved to the buyer (selling terms changed) or whether it is a reclassification. Both readings and the observation that separates them: if selling terms moved to ex-works or buyer-arranged freight, gross price realisation per unit would fall, which matches the 2.07 point gross margin drop. The separating observation is the Incoterms mix by customer, NOT FOUND IN DOCUMENT. [INFERENCE]

Exceptional items, three-year pattern: FY24 nil (AR FY25 P&L), FY25 nil, FY26 82.94 (single). Tax rate consistent at about 25% to 26.5%. EPS gap: none.

### Phase 3 summary and cross-reference

| Area | Finding | Risk |
|---|---|---|
| Cash flow | CFO/PAT 24.6%; two-year 47.2%; FCF -3,235.42; FY25 CFO inflated by borrowing | RED |
| Balance sheet | Moderate leverage; receivables and payables both +80%; cash 73.64; WC lines 67.4% drawn | YELLOW |
| P&L | Growth and margin real in the accounts; margin gain from cost lines that fell in rupees, no reasons | YELLOW |

Cross-reference. Phase 1 gave an unmodified opinion and no KAM. Phases 2 and 3 show profit that has not turned into cash for two years, with no loss allowance. The unmodified opinion does not contradict this because the receivables are legally recoverable on the face of the ledger. The contradiction is with the MD letter (Phase 6A): the letter says cash conversion improved.

**Phase 3 verdict: RED.**
**Kill switch (informational):** Based on phases so far, a human reviewer would have reason to pause and not to treat reported PAT as cash earnings, because CFO was 14.0% of EBITDA, FCF was negative by 3,235.42 and the funding came from supplier credit (+4,589.31) and bank lines. The pipeline continues; the reviewer decides.

---

## PHASE 4: RISK FACTORS AND MD&A

### 4A Disclosed risks (MD&A p.93-94, Board report para 21 p.39)

| Risk disclosed | Real or boilerplate | Evidence |
|---|---|---|
| Regulatory | Real. 20+ audits in two years; EU-GMP approvals for General and Beta Lactam units | MD&A p.91-92 |
| Market competition and pricing | Generic wording; no price-erosion number | MD&A p.94 |
| Raw material and supply chain | Boilerplate; raw materials are 47.9% of revenue (24,081.02 / 50,308.34, derived), import outgo 2,862.18 (Annexure A p.49) | |
| Foreign exchange: "Natural hedging through diversified export markets and prudent treasury management" | Contradicted by the notes. Unhedged USD receivables 164.28 lakh vs USD payables 1.81 lakh: payables cover 1.1% of receivables (Note 37 p.229, derived). A 1% INR move on 15,599.05 is about 156 (derived) | Note 37 |
| Operational / R&D / cyber | Boilerplate | MD&A p.94 |
| "Board is of the opinion that there are no risks which ... may threaten the existence of the Company" | Boilerplate | Board report p.39 |

### 4B Missing risks (risks the numbers show but the risk section omits)

| # | Missing risk | Evidence | Likely reason for omission |
|---|---|---|---|
| 1 | Credit and collection risk | Receivables 28,005.24 (+81.5%), 203 days, nil provision, 3,030.29 over six months (Note 9). The MD letter itself cites payment delays (p.4), but the MD&A risk table has no credit risk row (p.94) | The risk table is generic; it uses the same sector template as FY25 |
| 2 | Working-capital funding / liquidity | CFO 1,658.62, cash 73.64, limits 67.4% drawn, payables +82.3% | Admitting it would contradict "improvement in working capital cycle" (MD&A p.91) |
| 3 | GST demands 3,697.75, 11.2% of net worth | Note 34; CARO (vii)(b). Board report para 43 (p.44) says no significant order "could impact the going concern", and para 32 (p.42) says no material changes | Legal framing as disputed, not as a risk |
| 4 | Promoter-family control and key-person risk | All five executive directors are one family (Corporate Governance p.62: brothers, wives, son); promoters hold 54.87%; MD has been on the board since 1983 (p.85) | Not treated as a risk by convention |
| 5 | Independent director churn / board oversight | Of eight independents who served in FY26, three left within FY26 (Verma resigned; Takkar and Singh ended second terms) and one resigned after year end (Board report p.33-34); three independents attended 1 meeting each (p.61-62) | Described as "other professional commitments" and "term completion" |
| 6 | Related-party conduct | Kaler sale return 262.75 vs sale 121.48; "Director Interested" parties (Note 40) | Board report asserts no conflict (para 30) |
| 7 | Customer, partner and geography concentration | Not disclosed anywhere. Out-licensing and supply is "90%" of the model (MD&A p.91) | Disclosure choice. The thesis depends on it |
| 8 | Biologics execution and funding | EPO timeline slipped (Phase 6E); Unit 6 hormone facility under construction, cost and completion NOT FOUND; capex funded from payables and bank lines | Growth narrative |
| 9 | Subsidiary / Africa | Net liabilities 256.68, unaudited, 91.6% of revenue from the parent | Immaterial in rupees |

### 4C MD&A deep dive

Industry claims (global pharma market US$1.74 trillion in 2025, US$1.84 trillion in 2026, over US$2.6 trillion by 2030; IMF growth 3.1%; India GDP about 6.3%) are generic, repeated twice in the text (p.89-90), and carry no source table. They do not touch company-specific demand. Not testable here.

Growth and margin explanations. The MD letter credits "a richer product mix, growing contribution from regulated and semi-regulated markets, operating leverage, and increasing traction in registration-led business" (p.4). Tests: (a) richer mix would lift gross margin; gross margin fell 2.07 points (Phase 3C). (b) Regulated-market contribution is not quantified; export is 49.7% of revenue (24,979.72 / 50,308.34) and grew 27.8% while domestic grew 44.9% (25,326.18 vs 17,475.88). Domestic is now the larger and faster line, which cuts against an export-led story. (c) Registration-led business is not quantified: NOT FOUND IN DOCUMENT.

External-factor pattern. The Middle East conflict is credited with delayed customer payments (p.4) but is not mentioned in the notes, the risk table or the Board report. The company takes credit for audits, exhibitions and pipeline decisions. It blames external conflict for receivable days. No internal control or credit-policy action is named.

Product mix (MD&A p.95): Injectables 48%, Tablets 38%, Capsules 5%, others 9%. No revenue split by therapy, by registration holder or by customer.

Segment: single segment (MD&A p.94-95; Note 2.2(d)). No geographic table beyond export vs domestic.

MD&A ratio table (p.96): debtors turnover 2.30 vs 2.72 (worse); inventory turnover 2.98 vs 2.04 (better); interest coverage 9.15 vs 6.48; debt/equity 0.39 vs 0.42; operating margin 19.97% vs 14.65%; net margin 13.39% vs 10.78%; return on net worth 20.20% vs 15.00%. The MD&A "Operating Profit Margin" of 19.97% does not equal the 23.50% EBITDA margin of the MD letter and Phase 3; basis not stated. I cannot reproduce 19.97%.

Forward guidance table with credibility check:

| Claim | Number | Timeframe | Where | Delivery history | Credibility |
|---|---|---|---|---|---|
| Revenue | "over Rs 700 crore", up from "Rs 650 crore" | FY27 | MD letter p.4 | FY26 target Rs 500 crore (AR FY25 p.105-106) delivered 503.08. FY23 Rs 250 crore to FY26 Rs 503 crore "doubled" per letter. Needs +39.1% on FY26 (700 / 503.08, derived) vs +35.9% achieved | MODERATE. Revenue guidance has been met; cash funding of it is the issue |
| Revenue | "Rs 1,000 crore plus" | FY29 | MD letter p.4 | Implied CAGR 25.7% from 503.08 (derived). FY24 to FY26 CAGR was 28.0% (30,717.18 to 50,308.34) | MODERATE |
| Profitability | "scale in tandem" | FY27 | MD letter p.4 | No number. FY25 AR gave a 22-25% EBITDA range for FY26 and it was met (23.50%). FY26 AR gives no range | LOW specificity. The brief's EBITDA 189-196 and PAT 122 are NOT FOUND IN DOCUMENT |
| EPO (Kwalipoietin) launch | CY2027, subject to approvals | CY2027 | MD letter p.4; MD&A p.91 | AR FY25 (p.105): "undergoing clinical trials ... expect to commercialize this product within the ongoing financial year" (FY26). Slipped at least one year and the described stage went back (Phase 6E) | LOW |
| Three monoclonal antibody biosimilars | Under development, "first wave of generic entrants" on patent expiry | No date | MD letter p.4 | No history | NOT FOUND (timeline) |
| BE programme | More than 40 oral solid molecules; 16 BE studies "nearing completion" | No date | MD letter p.4; Annexure A p.48 | 433.89 capitalised in FY26 | Spend verified; filings timeline NOT FOUND |
| Oncology registrations | "approximately 30-40 oncology products" registered in the year | FY26 | Annexure A p.48 | FY25 AR target "50+ product approvals" not reported against | MODERATE; total approvals NOT DISCLOSED |
| Hormone unit (Unit 6) | "under construction" | No date | MD&A p.91-92 | CWIP 1,700.62; amount and completion NOT FOUND | NOT FOUND |
| Cash conversion cycle | 208 days to 170 days; "improved further in Q1 FY27" | FY26, Q1 FY27 | MD letter p.4 | Reproduced within about 3 days for FY26 (below). Q1 FY27 is outside the AR | See 6A |

CCC reproduction (derived, year-end balances): FY26 receivable days 203.2 + inventory days 110.5 (COGS basis) - payable days 146.6 (Note 39 basis) = 167.1. FY25: 152.1 + 167.0 - 108.6 = 210.5. Management says 170 and 208, so its figures reproduce within about 3 days. Bridge FY25 to FY26: inventory -56.5 days, payables +38.0 days, receivables +51.1 days. The reduction is funded by suppliers and an inventory rundown. Receivables made it worse.

Arithmetic sensitivity, not a forecast. At FY26 receivable days of 203.2 and the guided revenue of 700 crore (70,000 lakh), receivables would be about 38,970 lakh, a rise of about 10,965 lakh over 28,005.24. Borrowings today are 13,046.06. The guidance therefore needs either faster collection or more funding.

### 4D Tone and credibility ratings (1 low to 5 high)

| Dimension | Rating | Evidence |
|---|---|---|
| Transparency | 2 | No customer, country, registration-holder or ECL disclosure; template residue in Notes 2.1, 6 and 37; risk table omits credit risk |
| Consistency | 2 | Letter says payables tightened, notes show +82.3%; MD&A says working capital cycle improved, ratio table shows debtors turnover fell; Board report says no conflict RPT, Note 40 says "Director Interested"; subsidiary "wholly owned" vs 51% |
| Specificity | 3 | Specific on revenue, PAT, margin; vague on FY27 profit, Unit 6, antibody dates |
| Accountability | 2 | External conflict credited with receivable delay; no internal action named |
| Capital allocation sense | 3 | Capex 2.47x depreciation funded by payables and bank lines; no dividend ("deployed back the profits", p.81); BE capitalised; luxury vehicle loans 486.11 |

**Phase 4 verdict: YELLOW.**
**Contradictions vs Phases 1 to 3:** the "natural hedging" claim vs 1.1% payable cover; the "improvement in working capital cycle" claim vs the debtors-turnover fall; the "richer mix" claim vs a lower gross margin; the "no risk threatens existence" statement vs Phase 3's funding profile.
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because the omissions are disclosure weaknesses, not evidence of concealed loss. The reviewer would have reason to treat management's cash-conversion narrative as unproven until Q2 FY27 data. Continue.

---

## PHASE 5: CORPORATE GOVERNANCE AND BOARD

### 5A Board composition (Corporate Governance Report p.59-64)

12 board meetings were held on 19-05-2025, 30-06-2025, 26-07-2025, 11-08-2025, 16-08-2025, 26-09-2025, 13-11-2025, 01-01-2026, 28-01-2026, 12-02-2026, 21-02-2026, 31-03-2026 (p.60). The AR gives meetings attended only. Eligible meetings below are derived from these dates and the appointment or cessation dates.

| Director | Role | In office since | Other boards | Attended / eligible (derived) | Attendance | Flag |
|---|---|---|---|---|---|---|
| Ramesh Kumar | MD | 04/05/1983 | 3 | 12 / 12 | 100% | Age-70 continuation approved Sep 2024 (p.75) |
| Ajay Kumar Arora | WTD, brother | 01/08/1995 | 1 | 12 / 12 | 100% | Promoter family |
| Aditya Arora | WTD and CFO, son of Ajay | 22/10/2015 | nil | 12 / 12 | 100% | Promoter family; Audit Committee member |
| Geeta Arora | WTD, wife of Ajay | 01/10/2010 | nil | 12 / 12 | 100% | Promoter family; chairs CSR |
| Anju Arora | WTD, wife of Ramesh | 01/10/2010 | nil | 12 / 12 | 100% | Promoter family |
| Kiran Kumar Verma | Independent | start NOT FOUND | nil | 2 / 3 | 67% | Left 26/07/2025; absent last AGM |
| Pankaj Takkar | Independent, Audit chair | start NOT FOUND; second term ended 31/01/2026 | nil | 7 / 9 | 78% | Up to ten years served |
| Ravi Shanker Singh | Independent | start NOT FOUND; second term ended 31/01/2026 | 2 | 1 / 9 | 11% | Attendance below 75% |
| Kartik Kapur | Independent | 16/01/2021; second term from 16/01/2026 | nil | 1 / 12 | 8% | Resigned 02/06/2026, 4.5 months into second term; absent last AGM |
| Prashanth Vellanki | Independent | 16/03/2023 | 8 | 1 / 12 | 8% | Eight other directorships (at, not above, the 8-seat flag); absent last AGM |
| Vinod Kumar Sharma | Independent, NRC chair | 26/07/2025 | 1 | 6 / 10 | 60% | |
| Preetmohinder Singh Bedi | Independent | 01/01/2026 | nil | 4 / 5 | 80% | |
| Bhavesh Mahajan | Independent, Audit chair | 28/01/2026 | 1 | 2 / 4 | 50% | Chairs Audit Committee from 01/02/2026, four days after joining |
| Swanith Kapoor | Independent, additional | 02/06/2026 | NOT FOUND | n/a | n/a | Special resolution at 31 Aug 2026 AGM (Notice item 4) |

Findings. (1) Five of five executive directors are one family. Board of 10 at 31 Mar 2026: 5 executive family, 5 independent (p.59). (2) Six of eight independents who served in FY26 fall below 75% attendance on the derived basis; three attended one meeting in the year. (3) Independent turnover: Verma resigned (Jul 2025), Takkar and Singh completed terms (Jan 2026), Kapur resigned (Jun 2026), three new independents joined between Jul 2025 and Jan 2026 and a fourth in Jun 2026. (4) Kapur was reappointed for a second term at the 9 Sep 2025 AGM (Board report p.33) after attending one of twelve board meetings that year, then resigned within five months of the new term. (5) Independents with more than ten years: Takkar and Singh served two consecutive terms to Jan 2026; start dates NOT FOUND, so a ten-year finding is not confirmed. (6) Postal ballot of 28 Mar 2026 approved Bedi and Mahajan with 33,18,924 votes for and 12 against (p.76).

### 5B Committees

| Committee | Composition at 31 Mar 2026 | Meetings | Reading |
|---|---|---|---|
| Audit | Mahajan (chair, independent), Sharma (independent), Aditya Arora (executive, CFO) | 5 (19-05-25, 11-08-25, 16-08-25, 13-11-25, 12-02-26) | Majority independent. Reconstituted twice (26 Jul 2025, 1 Feb 2026). The CFO sits on the committee that reviews his own function. Mahajan attended 1 of 1 after joining; Sharma 4; Aditya 5; Takkar (chair to 31 Jan 2026) 4; Verma 1 (p.65-66) |
| NRC | Sharma (chair), Bedi, Mahajan | 4 | Fully independent. Sharma attended 3 of the 3 meetings held after he joined (p.67-68) |
| Stakeholders Relationship | Bedi (chair), Geeta Arora, Anju Arora | 2 | Two of three members are executive family (p.72) |
| CSR | Geeta Arora (chair), Aditya Arora, Mahajan | 1 on 30-03-2026 | One meeting, the day before the year closed |
| Risk management | None constituted (not named among the four, p.64) | | NOT FOUND whether required for this company |
| RPT | Approved by the Audit Committee; omnibus approval used (Board report p.41-42) | | No separate RPT committee |

The year-end audit (audit report 19 May 2026) was supported by an Audit Committee chair who had joined on 28 Jan 2026.

### 5C Compensation

| Name | FY26 | FY25 | Increase | Ratio to median | % of PAT 6,734.60 |
|---|---|---|---|---|---|
| Ramesh Kumar, MD | 84.00 | 72.00 | 16.67% | 56.39 | 1.25% |
| Ajay Kumar Arora | 84.00 | 72.00 | 16.67% | 56.39 | 1.25% |
| Aditya Arora, WTD and CFO | 54.00 | 48.00 | 12.50% | 36.25 | 0.80% |
| Geeta Arora | 36.00 | 30.00 | 20.00% | 24.17 | 0.53% |
| Anju Arora | 36.00 | 30.00 | 20.00% | 24.17 | 0.53% |
| Total executive | 294.00 | 252.00 | 16.67% | | 4.37% |
| Relatives of directors | 13.20 | 13.20 | 0.00% | | 0.20% |
| Company secretary | NOT FOUND (increase 19.04%) | | | | |

Source: Annexure B (p.50-51) and Note 40 (p.238). Employee salaries and wages 4,685.21 vs 3,797.12 (+23.39%); median employee pay up 3.73%; 1,137 employees on roll. Implied median pay about Rs 1.49 lakh (derived); average salary per head 4.12 lakh (4,685.21 / 1,137, derived). Executive pay rose 16.67% against PAT +69.2%, so it is modest relative to profit. Pay share of PBT is 3.29% (294.00 / 8,949.21). The multiple of 56 to the median is high but is driven by a low median, not by a high CEO figure. Aditya Arora is proposed for re-appointment for five years from 30 Sep 2026 at Rs 4,50,000 a month (Rs 54 lakh a year, unchanged) with minimum-remuneration protection under Schedule V Part II if profits are inadequate (Notice item 5, p.6-7). ESOP: none. Independent director sitting fees 7.50.

### 5D Shareholding

| Category | 31 Mar 2025 | 31 Mar 2026 | Change | Anchor |
|---|---|---|---|---|
| Promoters and promoter group | 5,688,972 (54.83%) | 5,693,069 (54.87%) | +4,097 sh (+0.04 pt) | p.82; AR FY25 |
| Foreign portfolio investors | none listed | 289,485 (2.79%) | new category | p.82 |
| Alternate investment funds | 32,704 (0.32%) | 37,122 (0.36%) | +0.04 pt | |
| Mutual funds | none listed | 197 (0.00%) | | |
| NRIs | 771,971 (7.44%) | 777,438 (7.49%) | +0.05 pt | |
| Indian public | 3,583,334 (34.53%) | 3,352,108 (32.30%) | -2.23 pt | |
| Bodies corporate | 198,361 (1.91%) | 126,121 (1.22%) | -0.69 pt | |
| IEPF | 100,540 (0.97%) | 100,540 (0.97%) | nil | |

Named holders above 5% (Note 14, p.215-216): Ramesh Kumar 26.03% (26.01%), Ajay Kumar Arora 13.60% (13.59%), Aditya Arora 11.96% (11.95%), Deepak Bansal 9.24% (10.63%). Bansal is not in the promoter group (the promoter total 5,693,069 is below the sum with Bansal, derived). He sold 144,428 shares (-1.39 point) in FY26. Reason and buyer NOT FOUND.

Promoter pledge: not disclosed in the AR (NOT FOUND IN DOCUMENT); B00 records the BSE summary of Sep 2026 as promoter 54.86%, no pledge. No promoter selling is visible; the promoter group added 4,097 shares. Institutions (FPI + AIF + MF) hold 3.15% at 31 Mar 2026 vs 0.32% a year earlier (derived). This is evidence for the UA institutional-absence qualifier only; it is not a risk. FII and DII trend beyond this year-end pair: NOT FOUND (B00 gap). No FLAG-PROMOTER-PRELIM.

### 5E Governance red-flag checklist

| Check | Result | Anchor |
|---|---|---|
| Whistle-blower complaints | None (CARO (xi)(c)); no investor complaints | p.108; p.73 |
| SEBI / exchange actions | Two small exchange penalties: Rs 4,720 (FY24, 2-day delay filing annual report) and Rs 2,360 (FY25, 1-day delay secretarial compliance XBRL), both paid | p.77-78 |
| RPT committee | Audit Committee approves; omnibus approval | Board report p.41-42 |
| Auditor fee ratio | Non-audit 0.68 of audit; not above 1.0 | Phase 1E |
| CSR compliance | 74.30 required and spent; capital asset 15.75 (school building, IBADAT, CSR00043848). FY25 required 145.94 moved to 74.30 with no computation shown | p.56-58; Note 42(g) |
| Section 143 fraud | None reported | Board report p.40, p.46 |
| Material subsidiary auditor | No material subsidiary; subsidiary unaudited | p.80 |
| Delay in statutory deposits | GST and TDS late-deposit remark in CARO (vii)(a) | p.105-106 |
| Senior management exits | HP plant head resigned 14 Mar 2026; replacement 2 Apr 2026 | p.64 |
| Related-party disclosure conflict | Board report and governance report vs Note 40 | Phase 2B |
| "Wholly owned subsidiary" wording | Governance report p.79 vs 51% in Note 14(a) | |

### Phase 5 summary

| Area | Finding | Risk |
|---|---|---|
| Board structure | Family executive bloc; independent bench rebuilt in 11 months; low attendance among independents | YELLOW |
| Committees | Independent majority on Audit and NRC; Audit chair two months old at the audit | YELLOW |
| Pay | Modest vs profit; high multiple to median; family relatives on payroll 13.20 | GREEN |
| Ownership | Promoters steady at 54.87%, no pledge in B00; no selling | GREEN |
| Disclosure | Board report conflicts with Note 40 | YELLOW |

**Phase 5 verdict: YELLOW.**
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because there is no pledge, no promoter selling, no SEBI action beyond two small penalties and no fraud. The reviewer would have reason to read the 12 Nov 2026 auditor-resignation filing in full before sizing, because the independent bench has been replaced almost entirely in one year and the audit chair was new at signing.

---

## PHASE 6: MD'S LETTER AND FRONT MATTER (read last)

There is no separate Chairman's letter. The front matter is "From the Managing Director's Desk" (p.4). The contents page lists it at page 1 (p.3).

### 6A Narrative vs reality

| # | Claim | What the accounts show | Result |
|---|---|---|---|
| 1 | "FY26 closed with consolidated revenue from operations of Rs 503 crore", doubled from Rs 250 crore in FY23 | 50,308.34 (P&L p.187-188). FY23 base of Rs 250 crore: NOT FOUND in either AR (AR FY25 shows FY24 30,717.18) | Yes for FY26. FY23 base unverified |
| 2 | "FY26 revenue grew nearly 36% over FY25's Rs 370 crore" | +35.9% (50,308.34 vs 37,019.70) | Yes |
| 3 | PAT "rose almost 69% ... from Rs 39.8 crore to Rs 67.3 crore", margins "from 10.8% to 13.4%" | 6,734.60 vs 3,980.27 = +69.2%; 13.39% vs 10.75% | Yes |
| 4 | EBITDA margin "from 22% to 24%" | 21.71% to 23.50%, +179 points | Yes, rounded up |
| 5 | Margin due to "a richer product mix" | Gross margin fell 2.07 points; the gain came from distribution, testing, factory and employee lines | No |
| 6 | "tightening inventory management and payables ... cash conversion cycle down from 208 days to 170 days" | Inventory yes (-6.2%, days 167.0 to 110.5). Payables rose 82.3%, days 108.6 to 146.6. CCC reproduces (210.5 to 167.1, derived) but via suppliers | Half: inventory yes, payables no |
| 7 | "debtor days elevated at 208" | Year-end receivable days 203.2 (derived). The letter's 208 also equals the FY25 CCC. Not reproduced exactly | Roughly; basis unclear |
| 8 | "That cycle has improved further in Q1 FY27" | Outside the AR. The web brief says receivables rose in H1 FY27 (not anchored) | Not testable here |
| 9 | "building direct relationships with customers rather than depending on intermediaries" | Commission expense 363.97 vs 157.25 (+131.5%). Commission may relate to agents on partner-led sales; the AR does not say [INFERENCE] | Not supported |
| 10 | "asset-light out-licensing and supply model (90%)" (MD&A) | Capex 4,894.04 is 2.47x depreciation; CWIP 1,700.62; hormone unit under construction; net PPE 14,972.59 | Hedged: the model label sits beside a heavy build |
| 11 | MD&A: "Improvement in working capital cycle (cash conversion days reduced significantly)" | Debtors turnover 2.72 to 2.30 and working-capital turnover 3.24 to 2.79 in the same report (p.96; Note 39 p.236) | No |
| 12 | Board report: no related-party transactions "which may have a potential conflict" | Note 40 lists two "Director Interested" parties, 410.88 gross | No |

### 6B Strategic priorities

| Priority | Specific enough | Capital allocated | Execution evidence |
|---|---|---|---|
| Doubling revenue in three years to Rs 1,000 crore+ by FY29 | Yes (number and year) | Capex 4,894.04 in FY26; Unit 6 cost NOT FOUND | FY23 to FY26 doubling delivered |
| Biologics (EPO, three mAbs) | Partly (CY2027 for EPO; none for mAbs) | BE and intangibles 433.89; R&D machinery about 60 lakh (Annexure A p.48) | Regression in stage description (6E) |
| Direct customer relationships | Vague | Travelling +203%, advertising +93% | 15+ exhibitions claimed; no customer data |
| Regulated-market push | Moderate (EU-GMP on two units) | Audit and registration cost not split | Four EU-GMP units claimed (MD&A p.91) |

### 6C Metrics showcased vs absent

Showcased: revenue, PAT, EBITDA margin, 70+ countries, 1,000+ products, 20+ audits, 80+ scientists, product mix by dosage form. Absent: customer and partner concentration, own-registration share, export by country, receivable ageing commentary, CFO, ROCE, bank utilisation, Unit 6 cost and date, number of registrations granted, R&D expense, promoter pledge.

### 6D Tone and priority drift vs FY25 AR

| Topic | AR FY25 | AR FY26 |
|---|---|---|
| Risk stance | "does not currently perceive any significant risks that could materially impact its operational or financial performance" (p.106) | Risk table with six rows; "no risks which ... may threaten the existence" (Board report) |
| FY margin guidance | "Projecting margins between 22-25%" (p.105) | No FY27 margin figure |
| Product count | "more than 3,000 formulations" (MD desk p.4) | "1,000+ products" (MD&A p.91) |
| Country footprint | "over 80 countries" | "70+ countries" |
| Tone on collections | Debtors turnover 3.25 to 2.72, no comment | Delay credited to Middle East conflict |
| FY priorities | Biologics launch in India, Rs 500 crore, peptide supplier, 50+ approvals, EU-GMP audit | Revenue, EU-GMP, biologics, hormone unit |

### 6E Quiet Abandonment Check (mandatory)

| # | Opening claim (quote) | Where it should show in operations | Finding | Class | Materiality |
|---|---|---|---|---|---|
| 1 | AR FY25 priority: "Establishing KPL as global peptide based product supplier" and "peptide-based oncology products" (AR FY25 p.105-106) | FY26 MD&A and Annexure A | Peptide appears only as research ("peptide-based therapeutics aimed at addressing various diseases", p.48). No supply, revenue or filing statement | (b) silent drop | Moderate: a named FY26 priority vanished |
| 2 | AR FY25 priority: "Achieving 50+ product approvals from markets" | FY26 MD&A and Annexure A | Only "approximately 30-40 oncology products" registered (p.48). No total, no comparison to 50+ | (c) hedged retreat | Moderate: delivery against the stated bar is not reported |
| 3 | AR FY25: EPO "has successfully completed preclinical studies and is currently undergoing clinical trials. We expect to commercialize this product within the ongoing financial year" (p.105) | FY26 Annexure A and MD letter | FY26 Annexure A says the company "completed the characterization of the protein chain" and "the pre-clinical study has been submitted to the Review Committee on Genetic Manipulation" (p.48). MD letter: "achieved successful pre-clinical outcomes during the year ... planned CY2027 launch". The stage described in FY26 is earlier than in FY25, and the launch moved from FY26 to CY2027 without saying the FY25 statement was wrong | (a) implicit retraction | HIGH: biologics is the re-rating story |
| 4 | MD letter: "tightening inventory management and payables" | Note 20 | Payables +82.3% | (a) implicit retraction | Moderate: the CCC improvement is supplier-funded |
| 5 | MD&A highlight: "Improvement in working capital cycle (cash conversion days reduced significantly)" | MD&A ratio table, Note 39 | Debtors turnover fell, WC turnover fell | (a) implicit retraction | Moderate |
| 6 | MD letter: "direct relationships with customers rather than depending on intermediaries" | Note 32 | Commission expense more than doubled | (a) possible, [INFERENCE] | Moderate for the own-vs-partner thesis |
| 7 | MD&A: "asset-light out-licensing and supply model (90%)" | Note 3-5, CFS | Capex 2.47x depreciation, new plant | (c) hedged retreat | Moderate: capital intensity |
| 8 | AR FY25: "over 80 countries", "3,000 formulations" | FY26 MD&A | 70+ countries, 1,000+ products, no explanation | (c) hedged retreat | Low to moderate: credibility of scale claims |

Phase 4 catches missing coverage (what the AR omits). 6E catches present-but-withdrawn content. They are kept separate.

### Phase 6 summary

Of 12 narrative claims: 4 hold, 2 hold with qualification, 1 untestable, 5 do not hold or are contradicted. The growth and profit claims hold. The cash, working-capital and mix explanations do not.

**Phase 6 verdict: YELLOW.**
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because the headline growth claims are accurate. The reviewer would have reason to discount the narrative on cash conversion and biologics timing.

---

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Call | Top reasons |
|---|---|---|
| GARP (full reasoning) | WATCHLIST | (1) Growth is real in the accounts: revenue +35.9%, PAT +69.2%, EPS 64.90 vs 38.36, two-year revenue CAGR FY24 to FY26 28.0%; guided FY27 +39% and FY29 25.7% CAGR (Phase 4C). (2) The AR carries no price, so the "reasonable price" half cannot be tested here (NOT FOUND IN DOCUMENT). (3) Quality of growth is the open question: CFO/PAT 24.6%, receivables +81.5%, gross margin down 2.07 points. A GARP buyer pays for earnings that become cash; two years of cash conversion at 47.2% does not yet qualify. (4) ROE 20.4% and ROCE 21.8% on year-end bases are acceptable and operational (DuPont). (5) The re-rating story rests on biologics and own-registration mix. Biologics shows a regression in stage (6E #3) and the mix split is NOT FOUND. Needs: ageing by customer and country, H1 FY27 CFO, registration-holder split |
| Turnaround (full reasoning) | FAIL as a classic turnaround; WATCHLIST as a transition | (1) No distress to turn around: PAT rose from 2,398.39 (FY24, AR FY25 p.107) to 3,988.97 to 6,734.66 (standalone). (2) The transition on offer is a mix and quality climb (regulated markets, own registrations, biologics), not a recovery. Evidence for it in this AR: EU-GMP on two more units (MD&A p.92), 30 to 40 oncology registrations, but no revenue split. (3) Test for the transition: whether own-registration revenue (28-32% EBITDA in the brief) is rising as a share. NOT FOUND in the AR; this is B04's job. (4) The climb is not yet visible in gross margin, which fell. (5) Ugliness check: the optic that looks ugly now is cash conversion; whether it is an artifact of a growth spurt (receivables funding new sales) or structural (aged balances not collected) is the reading that separates them: next two half-year ageing tables |
| Value + Quality | FAIL | Cash conversion fails; no ECL; flags in governance |
| Capex-Led Growth | WATCHLIST | Capex 2.47x depreciation, CWIP 1,700.62, Unit 6 and biologics capacity under way; but FCF -3,235.42 and capex funded by supplier and bank credit; outputs from the new capacity are 12 to 24 months away [INFERENCE: no commissioning dates in the AR] |
| Cash Flow Compounder | FAIL | CFO/PAT 24.6%; FCF negative |
| Contrarian | WATCHLIST | Price not in AR. Low institutional ownership (3.15%) is not a risk and is a UA qualifier candidate; contrarian case needs a price and sentiment read from outside the AR |
| Insider Confidence | WATCHLIST | Promoters 54.83% to 54.87%, no pledge (B00), mortgage of promoter-owned property for company loans; but promoter-family pay up 16.67% and new director-interested trades |
| Guidance Divergence | WATCHLIST | Revenue guidance has been met (FY26 500 vs 503.08). FY27 profit guidance is not in the AR. The brief's EBITDA and PAT guide, and Q2 FY27 results, can be set against delivery at stage 5 and 9 |

---

## PHASE 8: FINAL VERDICT DASHBOARD

### Company snapshot (consolidated, INR lakhs, FY26)

| Item | Value |
|---|---|
| Revenue | 50,308.34 (+35.9%); export 24,979.72 (49.7%) / domestic 25,326.18 |
| EBITDA | 11,824.38 (23.50%) |
| PAT | 6,734.60 (13.39%); EPS 64.90 |
| CFO | 1,658.62 (24.6% of PAT) |
| Receivables | 28,005.24 (203 days); FX receivables 15,599.05 unhedged |
| Borrowings | 13,046.06; ND/EBITDA 1.07x |
| Net worth | 32,992.09; ROE 20.4% |
| Contingent | 3,697.75 (11.2% of net worth) |
| Promoters | 54.87%; no pledge (B00) |

### Phase verdicts

| Phase | Verdict |
|---|---|
| 1 Auditor and CARO | YELLOW |
| 2 Notes | YELLOW (RED on provisioning) |
| 3 Financial statements | RED |
| 4 Risk and MD&A | YELLOW |
| 5 Governance | YELLOW |
| 6 MD letter | YELLOW |
| 7 Best fit | GARP, WATCHLIST |

### Quality score (each component /10, 25% weight)

| Component | Score | Basis |
|---|---|---|
| Governance | 4 | Family executive board; independents' attendance weak; independent bench rebuilt; Audit chair two months in role at signing; Board report vs Note 40. Offsets: no pledge, no fraud, no SEBI action beyond two small fines, modest pay |
| Accounting quality | 5 | Matches stage 2. Nil ECL, no KAM, template residue; clean inventory, CSR and statutory pay |
| Balance sheet | 5 | Leverage moderate (D/E 0.39, ND/EBITDA 1.07x, interest cover 9.2x); but 69.0% of current assets are unprovided receivables, cash 73.64, limits 67.4% drawn, payables stretched |
| Earnings quality | 4 | PAT growth is real in the P&L; CFO 14.0% of EBITDA; margin gain from cost lines with no reasons; one-off asset gain 71.22 |
| Overall | 4.5 / 10 | Mean of the four |

### Top 3 strengths
1. Growth and operating leverage are evidenced in the accounts: revenue +35.9%, EBITDA +47.1%, PAT +69.2% (P&L p.187-189).
2. Moderate leverage and no defaults: D/E 0.39, interest cover 9.15, CARO (ix) clean (p.96, p.107).
3. Clean ownership signals: promoters 54.87%, +4,097 shares, no promoter selling; mortgaged promoter property supports company loans (p.82; standalone p.149).

### Top 3 red flags
1. Profit not turning into cash: CFO/PAT 24.6%, two-year 47.2%, FCF -3,235.42, with no loss allowance on 28,005.24 of receivables at 203 days (CFS p.191; Note 9).
2. Credit quality is opaque: at least 1,166.32 of aged balances left the ledger with no disclosed route; 15,599.05 of FX receivables unhedged with no country or customer split (Note 9, Note 37).
3. Governance conduct: Board report asserts no conflict RPT while Note 40 shows two director-interested parties (a sale return of 262.75 against a sale of 121.48); independents' attendance is low and the bench turned over (Board report p.41-42; Note 40; p.61-62).

### Key monitorables for next quarter

| Metric | Threshold (analyst, to be confirmed at stage 11) | Where | Why |
|---|---|---|---|
| Year-end and half-year receivable days | Below 203.2; red if above 215 | H1 FY27 balance sheet and note on ageing | Core of FLAG-CASH |
| CFO / PAT, half-year | At or above 60% to clear; red below 35% | H1 FY27 cash flow statement | Tests the "cycle improved in Q1 FY27" claim |
| First ECL or doubtful provision, or write-off | Any such line; or over-one-year bucket (1,566.38) above its FY26 level | Notes to H1 FY27 results; next AR Note 9 | Provisioning is the weakest area |
| Working-capital utilisation | Above 85% of 12,685 sanctioned (now 67.4%), or a limit enhancement | Rating rationale, bank disclosures | Funding of 700 crore guidance |
| Kaler and Iair flows, ownership, repeat sales | Any repeat return; any disclosure of owner and director | Half-yearly RPT filing, AGM notice | Director-interested counterparty |
| Auditor change: reasons, new auditor, any CARO or emphasis change | Any qualification, emphasis or KAM added; any independent director exit | BSE announcements; Form ADT-3 content; next AR | 12 Nov 2026 event |
| GST: P&H High Court CWP-12033-2026 and CWP-34165-2024 | Any pre-deposit, provision or adverse order | Court records; next AR Note 34 | 3,697.75 exposure |
| Gross margin and distribution cost ratio | Gross margin below 48.6% with distribution above 2.8% of revenue would test the EBITDA gain | Quarterly results | Whether FY26 margin gain repeats |
| EPO regulatory step (RCGM, DBT, DCGI) | A named approval or trial start by mid-2027 | Company announcements | CY2027 launch |
| FX share of receivables | Above 55.7% or hedging policy stated | Next AR Note 37 | Unhedged exposure |

### One-line verdict
Growth is real but unproven as cash: best fit is a GARP WATCHLIST name where the position-size and entry decision wait for H1 FY27 cash conversion, receivable ageing by customer and country, and the auditor-resignation filing.

---

```yaml
stage: B03-ardeep
company: "KPL"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "KPL Q2 FY27 concall transcript ABSENT: call held 13 Nov 2026; freshness pair 1 FAILS. Re-collect after about 20 Nov 2026 (B00)."
  - "KPL Q3 FY26 (Feb 2026) concall transcript ABSENT (B00)."
  - "research/ empty (non-anchored; leads only) (B00)."
  - "shareholding/: BSE summary only, no FII/DII category breakdown beyond the AR year-end pair (B00)."
  - "screening/: screener export sheets Profit & Loss, Quarters, Balance Sheet, Cash Flow absent for KPL and peers (B00)."
  - "peer-concalls 10 of 12 (B00)."
  - "AR FY2026: customer, partner, country and product split; revenue by registration holder (own vs partner); customers above 10% of revenue; Middle East debtor amount and age; ECL model; interest rates and covenants; 5-year repayment table; tax reconciliation; leave encashment; CWIP ageing; capital commitments; Ind AS 10 events note; ownership and director link of Iair Infocom and Kaler Biopharmachem; Unit 6 cost and completion date; promoter pledge: NOT FOUND IN DOCUMENT."
  - "FY27 EBITDA (Rs 189-196 Cr) and PAT (Rs 122 Cr+) guidance and the Rs 720 Cr revenue figure are in the web brief only; the AR states revenue over Rs 700 crore and no profit number. Q2 FY27 PAT and tax rate are outside the AR."
  - "12 Nov 2026 statutory auditor resignation post-dates the AR (audit report 19 May 2026; Board report 8 Aug 2026); read the BSE filing outside this stage."
flags:
  - {type: FLAG-CASH, reason: "CFO 1,658.62 vs PAT 6,734.60 = 24.6% (INR lakhs); CFO/EBITDA 14.0%; FCF -3,235.42 after capex 4,894.04; two-year CFO/PAT 47.2% on a consistent basis (FY25 CFO includes 1,876.75 of short-term borrowing, exact tie 177.52 + 1,876.75 = 2,054.27); CFO would be -2,930.69 without the payables increase of 4,589.31; receivables +81.5% to 28,005.24 at 203.2 days (derived) with nil provision (CFS p.190-191; Note 9 p.211-212; Note 20 p.219)"}
phase_verdicts: {p1: "yellow: unmodified opinions, no going-concern doubt; no KAM section in either report; CARO (vii)(a) late GST/TDS deposits; GST disputes 3,697.75; subsidiary unaudited", p2: "yellow with red on provisioning: nil ECL on 28,005.24; matches stage 2 score 5/10; 15 of 15 triple-pass findings verified", p3: "red: CFO/PAT 24.6%, FCF -3,235.42, supplier-funded working capital, FY25 CFO inflated by borrowing", p4: "yellow: risk table omits credit risk, GST and liquidity; natural-hedge claim contradicted by 1.1% payable cover; guidance specific on revenue, silent on FY27 profit", p5: "yellow: five-member family executive bloc; six of eight FY26 independents under 75% attendance; independent bench rebuilt; Audit chair joined 28 Jan 2026; no pledge, no promoter selling; Board report vs Note 40 conflict", p6: "yellow: growth claims hold; cash-conversion, payables, richer-mix and no-conflict claims do not; EPO stage regressed vs FY25 AR", p7_best_fit: "GARP WATCHLIST"}
overall_quality: 4.5
quality_components: {governance: 4, accounting: 5, balance_sheet: 5, earnings: 4}
kill_switch_notes:
  - "P1: no reason to stop; thin audit narrative (no KAM on 28,005.24 of receivables) warrants close reading of Phase 2-3"
  - "P2: no reason to stop; reviewer needs receivable ageing by customer and country before relying on reported profit"
  - "P3: reason to pause; CFO 14.0% of EBITDA, FCF -3,235.42, funding from supplier credit and bank lines; do not treat PAT as cash earnings"
  - "P4: no reason to stop; treat the cash-conversion narrative as unproven until H1 FY27 data"
  - "P5: no reason to stop; read the 12 Nov 2026 auditor-resignation filing before sizing; independent bench replaced in 11 months and Audit chair two months in role at signing"
  - "P6: no reason to stop; discount the narrative on cash conversion and biologics timing"
triple_pass_verification:
  verified: 15
  discrepancies: []   # none material; four wording refinements recorded in report section 2.0 (ranks 4, 5, 6, 7)
missing_risks:
  - {risk: "Credit and collection risk absent from the MD&A risk table", evidence: "Receivables 28,005.24 (+81.5%), 203.2 days, nil provision, 3,030.29 over six months (Note 9 p.211-212); MD letter cites payment delays (p.4); risk table p.94 has no credit row"}
  - {risk: "Working-capital funding and liquidity", evidence: "CFO 1,658.62; cash 73.64; limits 67.4% drawn of 12,685 (standalone Note 17 p.147-148); payables +82.3% (Note 20 p.219)"}
  - {risk: "GST demands 3,697.75 (11.2% of net worth) not in risk section", evidence: "Note 34 p.226-227; CARO (vii)(b) p.106-107; Board report para 43 p.44 says no order could impact going concern"}
  - {risk: "Promoter-family control and key-person", evidence: "All five executive directors are one family (Corporate Governance p.62); MD on board since 04/05/1983 (p.85)"}
  - {risk: "Independent director turnover and low attendance", evidence: "Board report p.33-34; attendance table p.61-62 (Kapur 1 of 12, Vellanki 1 of 12, Singh 1 of 9 eligible, derived)"}
  - {risk: "Related-party conduct with director-interested parties", evidence: "Note 40 p.238-239: Kaler sale 121.48, return 262.75; Iair 26.65; Board report para 30 p.41-42 asserts no conflict"}
  - {risk: "Customer, partner and geography concentration not disclosed", evidence: "No concentration table in AR; out-licensing and supply 90% label only (MD&A p.91); NOT FOUND IN DOCUMENT"}
  - {risk: "Biologics and Unit 6 execution and funding", evidence: "EPO described at earlier stage than AR FY25 and launch moved to CY2027 (Annexure A p.48; AR FY25 p.105); CWIP 1,700.62 with no ageing (BS p.184); Unit 6 cost NOT FOUND"}
  - {risk: "Unhedged FX receivables with natural-hedge claim", evidence: "USD receivables 164.28 lakh vs payables 1.81 lakh (Note 37 p.229, derived 1.1% cover); MD&A p.94 claims natural hedging"}
guidance_table:
  - {claim: "FY27 revenue over Rs 700 crore, raised from Rs 650 crore", number: "700 crore (70,000 lakh); needs +39.1% on FY26 50,308.34", timeframe: "FY27", credibility: "moderate: FY26 target Rs 500 crore delivered at 503.08; cash funding of growth unproven"}
  - {claim: "Revenue Rs 1,000 crore plus", number: "1,000 crore; implied CAGR 25.7% from 503.08", timeframe: "FY29", credibility: "moderate: FY24 to FY26 CAGR 28.0%"}
  - {claim: "Profitability to scale in tandem", number: "no number in AR; brief's EBITDA 189-196 and PAT 122 NOT FOUND IN DOCUMENT", timeframe: "FY27", credibility: "low specificity; FY26 22-25% EBITDA range met at 23.50%, but no FY27 range given"}
  - {claim: "EPO (Kwalipoietin) launch", number: "CY2027, subject to approvals", timeframe: "CY2027", credibility: "low: AR FY25 said commercialise within FY26 and described clinical trials; AR FY26 describes pre-clinical study submitted to RCGM"}
  - {claim: "Three monoclonal antibody biosimilars", number: "NOT FOUND (no date)", timeframe: "on patent expiry", credibility: "not testable"}
  - {claim: "BE programme over 40 molecules; 16 BE studies nearing completion", number: "433.89 capitalised in FY26", timeframe: "no date", credibility: "spend verified; filing timeline NOT FOUND"}
  - {claim: "Hormone unit (Unit 6) under construction", number: "cost NOT FOUND; CWIP 1,700.62", timeframe: "no date", credibility: "not testable"}
  - {claim: "Cash conversion cycle 208 to 170 days, improved further in Q1 FY27", number: "reproduced 210.5 to 167.1 (derived)", timeframe: "FY26, Q1 FY27", credibility: "FY26 reproducible but supplier-funded (payable days +38.0, inventory days -56.5, receivable days +51.1); Q1 FY27 outside AR"}
monitorables:
  - {metric: "Receivable days, year-end and half-year", threshold: "below 203.2; red above 215 (analyst threshold)", where: "H1 FY27 balance sheet and ageing note", why: "Core of FLAG-CASH"}
  - {metric: "CFO / PAT, half-year", threshold: "at or above 60% to clear; red below 35% (analyst threshold)", where: "H1 FY27 cash flow statement", why: "Tests the Q1 FY27 improvement claim"}
  - {metric: "First ECL or doubtful provision; over-one-year receivable bucket", threshold: "any provision line; bucket above 1,566.38 is adverse", where: "H1 FY27 notes; next AR Note 9", why: "Provisioning is the weakest area"}
  - {metric: "Working-capital limit utilisation", threshold: "above 85% of 12,685 sanctioned (now 67.4%) or a limit enhancement", where: "Rating rationale; bank disclosures", why: "Funding of the Rs 700 crore guidance"}
  - {metric: "Kaler and Iair flows, ownership and director link", threshold: "any repeat return; any ownership disclosure", where: "Half-yearly RPT filing; AGM notice; AOC-2", why: "Director-interested counterparties"}
  - {metric: "Auditor change reasons; CARO, emphasis or KAM changes; independent director exits", threshold: "any qualification, emphasis or further independent exit", where: "BSE announcements; next AR", why: "12 Nov 2026 resignation; bench churn"}
  - {metric: "GST writs CWP-12033-2026 and CWP-34165-2024", threshold: "any pre-deposit, provision or adverse order", where: "Court records; next AR Note 34", why: "3,697.75 exposure"}
  - {metric: "Gross margin and distribution cost ratio", threshold: "gross margin below 48.6% with distribution above 2.8% of revenue", where: "Quarterly results", why: "Whether the FY26 EBITDA gain repeats"}
  - {metric: "EPO regulatory step", threshold: "a named RCGM, DBT or DCGI step by mid-2027", where: "Company announcements", why: "CY2027 launch claim"}
  - {metric: "FX share of receivables and hedging", threshold: "above 55.7% of receivables, or hedging policy stated", where: "Next AR Note 37", why: "Unhedged 15,599.05"}
ar_new_downstream_entities:
  - name: "Kaler Biopharmachem Private Limited"
    where_in_ar: "Note 40 consolidated p.238-239 and standalone Note 41 p.170-171: sale of goods 121.48 and sale return 262.75 (INR lakhs), prior year nil; labelled Director Interested"
    entity_type: "RPT counterparty (director interested); owner and director NOT FOUND IN DOCUMENT"
  - name: "Iair Infocom Private Limited"
    where_in_ar: "Note 40 consolidated p.238-239 and standalone Note 41 p.170-171: purchase of services 20.25 and sale of machine and spares 6.40 (INR lakhs), prior year nil; labelled Director Interested"
    entity_type: "RPT counterparty (director interested); owner and director NOT FOUND IN DOCUMENT"
strengths_top3:
  - "Growth and operating leverage evidenced in the accounts: revenue +35.9%, EBITDA +47.1%, PAT +69.2%, EPS 64.90 vs 38.36 (P&L p.187-189)"
  - "Moderate leverage and no defaults: D/E 0.39, interest cover 9.15, CARO (ix) clean (MD&A p.96; CARO p.107)"
  - "Promoters at 54.87% (+4,097 shares), no promoter selling, promoter-owned property mortgaged for company loans (Corporate Governance p.82; standalone Note 17 p.149)"
red_flags_top3:
  - "CFO/PAT 24.6% (two-year 47.2%), FCF -3,235.42, with nil loss allowance on 28,005.24 of receivables at 203 days (CFS p.191; Note 9 p.211-212)"
  - "At least 1,166.32 of aged receivables left the ledger with no disclosed route; 15,599.05 of FX receivables unhedged with no country or customer split (Note 9 p.212; Note 37 p.229)"
  - "Board report asserts no conflict RPT while Note 40 shows two director-interested parties and a sale return (262.75) above the sale (121.48); independents' attendance low and bench turned over (Board report p.41-42; Note 40 p.239; Corporate Governance p.61-62)"
best_fit_strategy: "GARP (WATCHLIST)"
one_line_verdict: "Growth is real but not yet cash: GARP WATCHLIST until H1 FY27 cash conversion, receivable ageing by customer and country, and the auditor-resignation filing are read."
analyst_note: "All AR figures are INR lakhs; stage 10 converts once. Page anchors are .txt [page N] markers (printed page = N minus 3). Derived items: receivable days (year-end basis), export vs domestic days (assumes FX balances = export), attendance ratios (eligible meetings counted from the 12 meeting dates and appointment dates), CCC reproduction, ROCE (AR Note 39 capital base 45,787.97 not rebuilt). The 12 Nov 2026 auditor event, FY27 EBITDA and PAT guidance and the Rs 60-70 Cr Middle East debtors come from the web brief and are not anchored. SA 701 KAM duty and the 15-year Schedule II plant life are external-law recollections flagged for the verifier. Commission +131.5% as a sign of partner-led sales and the freight-terms reading of the distribution cost fall are [INFERENCE]; each has a named separating observation."
```
