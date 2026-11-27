# STAGE 2 NOTES, PASS 2 OF 3 (WHAT WAS MISSED): Kwality Pharmaceuticals Ltd (KPL)

Run: kpl-2026-11-15 | Model: claude-sonnet-5-5 | Source: Annual_Report_2026.pdf via page-marked .txt (consolidated Notes 1-41 re-read in full, p.194-240; standalone Notes 7, 8, 42 re-checked; AR FY2025 .txt used for prior-year reference).

UNIT: every AR figure is in INR LAKHS (face of each note: "(₹ in lakhs)"). Nothing is converted. "Derived" = my arithmetic on anchored AR figures. Anchors read (Note N, p.PDF-marker). Percentages and ratios are unit-free.

Pass 1 was thorough on the headline items. This pass reports only items Pass 1 did not cover, or covered only in part. Where I resolve a Pass 1 "NOT FOUND" by arithmetic, I say so and mark it derived, not disclosed. One PDF check: the Note 3 "Property" row (p.206 image) is confirmed as a gross block of 1,875.00 + additions 362.52 - disposal 252.98 = 1,984.54, zero depreciation, net = gross. Pass 1 read it correctly. FY24 net of that row was 1,748.05 (AR FY25 Note 3 .txt line 10973), so it is an older holding, not a FY25 purchase.

---

## A. NEW FINDINGS (ranked by investor importance)

### N2.1 FY25 cash flow from operations is on a different basis from FY26. FY25 CFO includes 1,876.75 of bank borrowing. 🔴

This changes the cash-conversion trend that Pass 1 reported (CFO/PAT 182.0% -> 132.4% -> 24.6%).

- FY25 consolidated CFS line "Increase/(Decrease) in Financial Current Liabilities" = 2,054.27 (AR FY25 CFS, .txt line 10298-10299; repeated unchanged as the FY25 comparative in the AR FY26 CFS p.190-191).
- Balance-sheet movement in Note 20 "Other Financial Current Liabilities" FY24 323.06 -> FY25 500.58 = 177.52 (AR FY25 Note 20, .txt line 11954-11961).
- Short-term borrowings FY24 7,855.88 -> FY25 9,732.63 = 1,876.75 (AR FY25 BS p.195, .txt line 10056).
- 177.52 + 1,876.75 = 2,054.27, an exact tie (derived).
- In FY26 the same CFS line is 27.39, which equals the Note 21 movement 500.58 -> 527.96 = 27.38 (Note 21 p.220). The FY26 borrowing movement sits in financing (proceeds 3,169.31, repayments 1,368.31, net +1,801.00 against the balance-sheet change of 1,801.53, CFS p.191; Notes 16, 19).
- So FY25 CFO carried a working-capital borrowing increase and FY26 CFO does not. The FY26 AR repeats the FY25 comparatives without restating.
- Like-for-like FY25 CFO (derived) = 5,271.78 - 1,876.75 = 3,395.03. CFO/PAT FY25 = 3,395.03 / 3,980.27 = 85.3% (Pass 1: 132.4%). Two-year FY25+FY26 CFO 5,053.65 vs PAT 10,714.87 = 47.2% (derived).
- FY24 cannot be tested: the FY23 balance sheet is not in the corpus. FY24 shows the same line at 1,550.77 (AR FY25 CFS .txt line 10298). FY24 like-for-like CFO: NOT COMPUTED.
- [INFERENCE] The label says "Financial Current Liabilities". The exact arithmetic tie is the evidence that borrowings are inside it. The filing does not say so.
- Consequence for stage 11: cash conversion was already below 100% of PAT in FY25 on a consistent basis, and FY26 (24.6%) is the second sub-100% year, not the first.

### N2.2 Foreign-currency receivables doubled and explain most of the receivable build. FY25 comparative was missed in Pass 1. 🔴

Note 37, p.229, unhedged, ₹ lakhs; USD figures are in USD lakh.

| | FY26 | FY25 | Change |
|---|---|---|---|
| USD receivables (USD lakh) | 164.28 | 90.27 | +82.0% |
| USD receivables in ₹ | 15,550.18 | 7,712.22 | +101.6% |
| EUR receivables in ₹ | 5.45 | 266.35 | |
| AED receivables in ₹ | 43.42 | 123.26 | |
| Total FX receivables in ₹ | 15,599.05 | 8,101.83 | +7,497.22 |
| USD payables in ₹ (USD lakh) | 171.24 (1.81) | 80.67 (0.94) | |

Derived:
- Implied closing USD rate: FY26 15,550.18 / 164.28 = 94.66; FY25 7,712.22 / 90.27 = 85.43 (+10.8% rupee move). Payables imply the same 94.6, so the rates are consistent. Of the +101.6% rupee rise, about 18 points came from the rate and the rest from USD volume (+82.0%).
- FX receivables / share of total receivables: 55.7% (FY26) vs 52.5% (FY25). FX receivables explain 7,497.22 of the 12,574.66 total receivable build = 59.6%.
- FX receivables over export turnover (Note 25 p.222: 24,979.72; 19,543.82): 62.4% = 227.9 days (FY26) vs 41.5% = 151.3 days (FY25). This assumes all FX balances sit in the export line. USD receivables +82.0% against export turnover +27.8% (INR) is the gap.
- Non-FX receivables: 12,406.19 vs 7,328.75 (+69.3%) against domestic turnover +44.9%. Over domestic turnover that is 178.8 days vs 153.1 days (derived). This assumes all non-FX balances are domestic.
- Both domestic and export receivable days lengthened. The deterioration is not an export-only story.
- FX line in P&L is small: loss 4.37 in Note 32 p.225; FY25 gain 7.73 in Note 26 p.222; the Note 37 text (p.229) confirms both. No sensitivity table. Country, customer and credit-insurance cover: NOT FOUND IN DOCUMENT.

### N2.3 About two-thirds of FY25's one-year-plus overdue receivables left the ledger in FY26 with no provision and no bad-debt line. 🔴

This extends Pass 1 section 4, which found "about 600" gone from the over-2-year buckets. The bucket roll-forward is tighter.

- Ageing is from due date and buckets only age (Note 9(a) p.212; Note 9(b) p.212). FY26 "2-3 years" can only come from FY25 "1-2 years"; FY26 "more than 3 years" can only come from FY25 "2-3 years" plus "more than 3 years".
- FY25 1-2y 566.17 -> FY26 2-3y 89.74: at least 476.43 gone (84.2%).
- FY25 2-3y 517.50 + more than 3y 646.94 = 1,164.44 -> FY26 more than 3y 474.55: at least 689.89 gone (59.2%).
- Combined: of 1,730.61 that was 1 year or more past due at FY25, at most 564.29 can remain; at least 1,166.32 (67.4%) left the ledger in FY26 (derived).
- Route out: NOT FOUND IN DOCUMENT. Notes show no provision (Note 9 p.211), no write-off, no ECL charge, no bad-debt line in Note 32 (p.225).
- [INFERENCE] Kaler Biopharmachem (a "Director Interested" party, nil in FY25) shows sale 121.48 and sale return 262.75 (Note 40 p.239). A return larger than the year's sale means some goods sold before FY26 came back. A credit note could therefore have cleared an older receivable. The filing links neither. This is a question, not a finding of fact.
- Standalone check: standalone Note 10 p.140-141 buckets differ from consolidated only by the subsidiary debtor 116.73 (>3y: 591.28 vs 474.55), as in Pass 1.

### N2.4 Operating margin gain is from fixed-cost lines. Gross margin fell 2.1 points. 🟡

Derived from Notes 25, 27-29, 30, 32 (p.222-225); P&L tie shown.

| ₹ lakhs | FY26 | FY25 |
|---|---|---|
| Revenue (Note 25) | 50,308.34 | 37,019.70 |
| Materials consumed (Note 27) | 24,081.02 | 16,541.24 |
| Stock-in-trade purchases (Note 28) | 1,734.63 | 1,590.16 |
| Change in inventories (Note 29) | 27.77 | 117.24 |
| Net cost of goods | 25,843.42 | 18,248.64 |
| Employee cost (Note 30) | 5,404.26 | 4,378.39 |
| Other expenses (Note 32) | 7,236.28 | 6,353.93 |
| Operating profit before other income (derived) | 11,824.38 | 8,038.74 |

- Gross margin 48.63% vs 50.70% (-2.07 points). Materials consumed as % of revenue 47.87% vs 44.68%.
- Operating margin before other income 23.50% vs 21.71% (+1.79 points); operating profit +47.1%.
- Tie: 11,824.38 + other income 285.86 - depreciation 1,981.04 - finance 1,097.04 - exceptional 82.94 = 8,949.22 against PBT 8,949.21. FY25: 8,038.74 + 192.01 - 1,828.96 - 987.79 = 5,414.00 against 5,413.99.
- Where the leverage came from (% of revenue, FY26 vs FY25): employee 10.74% vs 11.83%; other expenses 14.38% vs 17.16%. Inside other expenses: distribution 2.81% vs 4.04% (rupees -5.5%); power and fuel 5.31% vs 6.31%; testing and laboratory 0.26% vs 0.74% (rupees -51.5%); factory expense 0.30% vs 0.58% (rupees -29.2%).
- Distribution cost against export turnover: 5.67% vs 7.66%. Why freight fell in rupees while exports rose 27.8%: NOT FOUND IN DOCUMENT. Shipment terms (Incoterms) NOT FOUND IN DOCUMENT; Pass 1 already noted this for revenue recognition.
- Testing and laboratory charges halving while revenue rose 35.9% also has no stated reason.
- Reading: the notes support a margin bridge in which cost-of-goods pressure was offset by four lines that fell in rupees. Which of these repeat is not answerable from the notes.

### N2.5 Customer advances fell from 6.0% to 1.7% of revenue. FY24 shown here for the first time. 🟡

- "Advances from Customers" (contract liability): FY24 1,847.50 (AR FY25 Note 21, .txt line 11973); FY25 497.03; FY26 879.23 (Note 22 p.221).
- As % of revenue: FY24 6.01% (on 30,717.18); FY25 1.34%; FY26 1.75% (derived).
- Pass 1 gave FY25 to FY26 (+76.9%) only. Over three years the advance-funded share of sales fell sharply as receivables rose (135.9 -> 152.1 -> 203.2 days, Pass 1).
- [INFERENCE] Advance terms were replaced by credit terms. The notes give no term-mix disclosure, so this is a reading, not a fact.

### N2.6 Other current assets +89.4%: advances to suppliers doubled, staff advances up 11.6x. 🟡

Note 13 p.214 (₹ lakhs), against Pass 1, which cited only "balances with revenue authorities":

| Line | FY26 | FY25 | Change |
|---|---|---|---|
| Balances with revenue authorities | 1,785.21 | 995.03 | +790.18 |
| Advances to suppliers | 1,581.25 | 791.13 | +790.12 (+99.9%) |
| Advances to staff | 72.39 | 6.22 | +66.17 (11.6x) |
| Other advances | 56.08 | 52.97 | |
| Security deposits | 1.10 | 0.36 | |
| Total | 3,496.04 | 1,845.70 | +1,650.34 (+89.4%) |

- Advances to suppliers = 22.8 days of FY26 purchases (25,317.25, Note 39 p.236) vs 15.4 days FY25 (derived). Purchases rose 35.0%.
- Unlike capital advances (Note 7 p.210), Note 13 has no secured/unsecured/doubtful split and no ageing. Supplier identity and related-party status: NOT FOUND IN DOCUMENT.
- Advances to staff rising from 6.22 to 72.39 is unexplained. Whether any advance goes to directors or relatives: NOT FOUND IN DOCUMENT (Note 7 "Loans and advances to related parties" is nil; Note 13 does not split).
- The CFS carries this as a 1,650.34 outflow in a line labelled "Other Financial Assets, Current" (label swap per Pass 1).

### N2.7 Non-current security deposits fell 333.35 (-71.6%). Cause not stated. 🟡

- Note 7 p.210-211: security deposits (secured, considered good) 132.45 vs 465.80; capital advances 1,012.78 vs 1,152.96; total 1,145.23 vs 1,618.76.
- CFS "(Increase)/Decrease in Other Long term Assets" 473.53 = 333.35 + 140.18 exactly (CFS p.191; derived tie). The refund of deposits is booked as investing inflow.
- What the deposits were for (lessor, utility, bank, a property deal) and why they were returned: NOT FOUND IN DOCUMENT. The year also had a property sale (252.98 at book, proceeds 324.20) and a new 594.50 capital advance liability (Note 18); no link is disclosed.

### N2.8 Lease liability fits the promoter factory lease. This is an inference. [INFERENCE] 🟡

Pass 1 recorded the lease discount rate as NOT FOUND. A rate can be derived. A likely identity of the lease can be tested.

- Interest on lease liabilities 2.11 (Note 31 p.224) on a liability of 24.05 (23.99 non-current Note 18 p.218 + 0.06 current Note 22 p.221) gives about 8.8% (derived; not a disclosed rate).
- Note 40 p.239: rent to the two promoter directors 1.08 + 1.08 = 2.16 a year. CARO (i)(c) p.104: factory and registered office are on promoter-owned land, initial lease term 49 years.
- PV of 2.16 a year for 49 years at 8.8% is about 24.2 (derived annuity). Lease liability 24.05 is close. ROU depreciation 0.52 (Note 3 p.206) against 24.2 / 49 = 0.49 also fits.
- CARO also names a Kangra plot leased from the Government of Himachal Pradesh (p.104). The "upfront lease" ROU of 10.03 (Note 2.2(n) p.201-202) could be that plot. The filing names neither lease.
- Why it matters: if this holds, the entire Ind AS 116 balance is the promoter lease, which Ind AS 116 should have recognised from FY20. The "prior period adjustment" was a seven-year omission corrected through opening reserves (Pass 1 1.3) with no restated comparatives and no third balance sheet. The amount is small (4.47 net). The signal is about close-process control, not size.
- Total additions in Note 3 are 2,788.09, which counts the 10.03 opening ROU as an addition at total level; the class rows show it as opening. Closing ties at 25,520.70 (class sum checked). Capex tie: 2,788.09 + CWIP 1,700.62 - non-cash ROU 28.56 = 4,460.15 = CFS "Purchase of PPE" (CFS p.190). So CFS capex equals book additions plus CWIP, with no adjustment for capital creditors.

### N2.9 Penalty equals 100% of tax in the GST demands. Section 74 track. 🟡

- Note 34 p.226-227: Item 1 tax 315.03 + penalty 315.03; Item 2 ITC 1,513.03 + penalty 1,513.03; Item 3 DRC-07 FY20 6.75 + 6.75. Each is a Section 74 matter in the text, and Item 2 also cites Section 122.
- [External recollection, NOT in the document; verifier to check] Section 74 is the CGST provision for fraud, wilful misstatement or suppression; Section 73 is the non-fraud track. A document-only reading: the filing itself cites Section 74 and penalty equal to tax, and does not say what the department alleges beyond "erroneous refund" and "wrongly availed ITC".
- Pass 1 sized the exposure (3,697.75). This adds that the exposure is stated at the high-penalty case and with interest unquantified for Item 1 (p.226). A lower final amount would come only through the appeal or writ.
- No provision, and no bank guarantee or deposit under protest disclosed against any item. Pre-deposit under Section 107 for the lost appeal: NOT FOUND IN DOCUMENT.

### N2.10 Board report and Note 40 are not aligned on related-party conflict. 🟡

- Board report item 30 (p.41-42): "There were no related party transactions made by the Company with the Promoters, Directors and Key Managerial Personnel which may have a potential conflict with the interest of the Company at large." No AOC-2 because no material RPT.
- Note 40 (p.238-239) lists two "Director Interested" entities with 410.88 of gross flows (Pass 1) and a sale return larger than the sale.
- [INFERENCE] The Board's statement is consistent only if the Board judged these flows free of conflict. The filing gives the basis for that judgement in neither place. Ownership of Iair Infocom and Kaler Biopharmachem and the "interested" director: NOT FOUND IN DOCUMENT (also in Pass 1). Neither name appears anywhere in AR FY2025 (grep clean), confirming both are new.
- Board composition: sitting-fee table in Note 40 shows three independent directors with no FY25 fee: Preetmohinder Singh Bedi 1.00, Vinod Kumar Sharma 3.00, Bhavesh Mahajan 0.30 (4.30 of 7.50). Pass 1 recorded the 7.50 total and "8 names" only.

### N2.11 Gratuity: implied discount rate and size of the Labour Code step. 🟢 / 🟡

- Net interest 5.24 = DBO interest 13.20 - plan-asset interest 7.95 (Note 38 p.233; ties). Plan-asset return 7.95 / opening assets 117.45 = 6.77% (FY25: 5.93 / 83.70 = 7.09%). FY25 DBO interest 8.06 / 113.65 = 7.09%.
- A discount rate is not disclosed (Pass 1: NOT FOUND). The plan-asset yield implies about 6.8% for FY26 and 7.1% for FY25 (derived). FY26 DBO interest of 13.20 / 159.11 = 8.30% is higher because the 82.94 past service cost accrues interest in the year (derived; [INFERENCE]).
- The 82.94 past service cost is 52.1% of the opening DBO (159.11) and 29.3% of the closing DBO (283.52) (derived). Ex the Labour Code item, DBO would have been about 200.6.
- Sensitivity as % of DBO: discount +100bp -5.6% (FY25 -6.2%); salary +100bp +6.9% (FY25 +7.6%) (Note 38 p.235; derived).
- Fund size stated as Rs 12,590,013 = 125.90 lakh (p.235), matching plan assets. Employer contribution 0.50 (FY25 20.29), so the funded ratio fell to 44.4% from 73.8% (117.45/159.11) (derived).
- Remaining Labour Code cost on non-gratuity items (leave encashment, bonus definitions): NOT FOUND IN DOCUMENT.

### N2.12 Other financial current liabilities: unexplained "Others" 315.88. 🟡

- Note 21 p.220: Others 315.88 (FY25 390.21; FY24 64.56 per AR FY25 Note 20). Statutory dues 190.51 (FY25 94.24; FY24 234.86). Interest accrued but not due 21.58.
- "Others" is 59.8% of the note total (527.96) and has no breakdown. It rose 6x in FY25 and fell 19% in FY26.
- Statutory dues doubled to 190.51 (+102%). CARO (vii)(a) p.105-106 reports delays in GST and TDS deposits in the year, regularised with interest and late fees, and none outstanding beyond six months. The amount of late fees and interest: NOT FOUND IN DOCUMENT.

### N2.13 CSR requirement swing needs a reconciliation. 🟡

- Standalone Note 42(g) p.172-173: required FY26 74.30; FY25 145.94; FY25 spend 145.96; FY26 spend 74.30 plus 30.93 from the unspent account.
- Requirement is 2% of the average of the prior three years' net profit (my knowledge of the rule, not in the document). FY26 74.30 implies an average base of 3,715 (derived). FY25 145.94 implies 7,297, which exceeds FY24 PBT 3,109.89 and FY25 PBT 5,413.99 (Pass 1 anchors). FY22 and FY23 profits are not in the corpus.
- [INFERENCE] One of the two requirements includes something other than the plain 2% (a carried-forward amount, or a different profit base). The note shows no computation. Low severity in rupees, and it bears on disclosure quality.

### N2.14 Policy text changes and gaps vs AR FY2025. 🟡

- Intangible policy (Note 2.2(f) p.198) dropped the FY25 paragraph on initial measurement at cost, nil residual value and annual review of life and method (AR FY25 policy "e", .txt lines 7074-7079). The FY26 intangible adds are 433.89 (Bioequivalence Study), 2.5x the FY25 technical know-how (171.00).
- Intangible life for the two assets differs: know-how 10 years (FY25), bioequivalence 5 years (Note 2.2(g) p.198; AR FY25 .txt line 7100). Which costs qualify for capitalisation (Ind AS 38 research vs development test): NOT FOUND IN DOCUMENT (also in Pass 1).
- Useful-life table is identical year on year. WDV depreciation as % of opening net block: plant 16.4% FY26 vs 17.2% FY25; building 9.6% vs 7.3%; vehicles 50.5% (177.58 / 351.48) vs 35.8% (100.92 / 282.03) (derived from Note 3 p.206 and AR FY25 Note 3 .txt lines 10960-11030). Building depreciation +41.8% (393.17 vs 277.35) without an explained cause.
- Vehicles: gross block 1,094.79 -> 1,635.46 (+49.4%); additions 540.67; net block 351.48 -> 714.57 (+103%) (Note 3 p.206). Pass 1 covered the vehicle loans (486.11), not the block growth.
- Policies not found in the notes: borrowing costs (CWIP 1,700.62 and all finance cost expensed, Note 31); government grants and export incentives (duty drawback 202.10 is recognised under "other claims" accrual, Note 2.2(o) p.202); translation of the foreign subsidiary (policy 2.2(c) p.197 covers transactions only; FCTR reserve -3.16, Note 15 p.217); EPS.
- Note 2.1 p.194 states comparatives "as at and for the year ended March 31, 2023". This is stale template text (the year is FY25). Note 2.2(m) p.201 describes the exceptional item as presented "in the standalone financial results for the quarter and nine months ended 31 December 2025", which is quarterly-results wording in an annual-report note. Note 37 p.228 refers to "Note No.9 of Notes forming Part of Standalone Financial Statements"; in the standalone set the receivables note is Note 10 (Pass 1 cites standalone Note 10 p.140), so the cross-reference points to the wrong note. Pass 1 caught the Note 6 template text and the Note 30 versus Note 2.2(m) conflict only.
- Revaluation reserve of 80.00 (Note 15 p.217; SOCE p.193) sits beside a cost-model PPE policy (Note 2.2(e) p.197). Origin of the reserve: NOT FOUND IN DOCUMENT.

### N2.15 Net-worth bridge details. 🟢

- Note 15 p.216-217: Other equity 32,121.94 = securities premium 846.77 + retained earnings 31,198.33 (31,030.66 + "NCI in retained earnings" 167.67) + FCTR -3.16 + revaluation reserve 80.00. The NCI is then deducted as (167.47) in total equity (SOCE p.193: owners 33,159.56, NCI -167.47, total 32,992.09).
- SOCE retained earnings closing is 31,196.78 vs Note 15 31,198.33 (1.55 gap); FY25 24,444.01 vs 24,443.38 (0.63 gap). Totals tie. Immaterial.
- SOCE shows a 2.20 transfer from NCI to owners ("Reclassification Adjustment", FY26) with no note text. Pass 1 covered the FY25 reclassification 1.94 only. Basis NOT FOUND IN DOCUMENT.
- Note 15 FY25 OCI -1.78 = gratuity -0.97 + FCTR -0.81 (SOCE p.193). Pass 1 quoted -0.97 only.
- Profit attributable to owners is 6,734.63; NCI share -0.03 (SOCE p.193). EPS numerator uses 6,734.60 (Note 35 p.227). No effect on EPS at two decimals.

### N2.16 Subsidiary: paid-in amount against share capital, and outside liabilities. 🟡

- AOC-1 p.241 (Rs, converted to lakhs, derived): share capital 88.68; KPL's 51% = 45.23. Investment carried by the parent is 354.78 (Note 40 p.238; standalone Note 7 p.138), 7.8x its 51% of share capital.
- [INFERENCE] The 309.55 gap above face value is premium or capitalised funding. Note 1 p.194 says the company "granted loans" to the subsidiary; standalone Note 8 p.139 and Note 40 show no loan balance. Which of these is the 354.78: NOT FOUND IN DOCUMENT.
- Subsidiary outside liabilities 383.04 less the 116.73 owed to KPL leaves 266.31 owed elsewhere (derived). Creditor identity NOT FOUND IN DOCUMENT.
- KPL's debtor from the subsidiary fell 159.42 -> 116.73 while KPL sold 26.68 to it, so about 69.4 was collected or adjusted in the year (derived; includes any currency effect).
- Board report and corporate governance section describe the subsidiary as "wholly owned" (corporate governance text, .txt line 4472); notes say 51% (Note 14(a) p.215). Outside the notes; flagged for the verifier.

### N2.17 Disclosures absent that the facility list implies. 🟡

- Note 19 p.219 describes facilities as "Cash Credit, Pre-shipment, Post Shipment, FLC, PSL, PCFC and BG". Note 34 shows no bank guarantee or letter of credit outstanding, and nothing on export bills discounted with recourse. Amounts of BG, FLC and discounted bills: NOT FOUND IN DOCUMENT.
- CARO (ii)(b) p.105: bank statements show "insignificant difference" against books; the difference is not quantified.
- Note 41 (Schedule III, p.239-240) has no CWIP ageing, no title-deed table, and no item on current-asset statements filed with banks. CWIP is 1,700.62, all added in FY26.

### N2.18 Smaller tie-outs and presentation points. 🟢 / 🟡

- Other non-cash items in the CFS (132.23): equals gratuity cost 130.13 (Note 38 p.231) + lease interest 2.11 = 132.24, within 0.01 (derived tie). This resolves Pass 1's "composition NOT FOUND" by arithmetic; the filing does not state it. Lease interest then appears in both the finance-cost add-back and this line (2.11 double add-back; financing "Interest paid" 1,097.04 equals the P&L charge, so accrued MSME interest 11.02 and accrued interest 21.58 are treated as paid).
- Ratio note ties: current ratio numerator 40,567.75 = inventories 7,825.23 + receivables 28,005.24 + cash 73.64 + bank 285.59 + other financial assets 882.01 + other current assets 3,496.04. Denominator 22,552.00 ties to Notes 19-24. Receivables are 69.0% of current assets. Excluding receivables over six months (3,030.29) the ratio is 1.66 against 1.80 (derived).
- ROCE capital employed 45,787.97 = equity 32,992.09 + debt 13,046.06 - DTA 250.18; lease liabilities excluded. ROE uses closing equity, not average (Note 39 p.235-237).
- DSCR denominator 2,465.35 = interest 1,097.04 + repayments 1,368.31. Numerator 9,824.41 vs PAT + depreciation + finance cost 9,812.68 (gap 11.73, composition NOT FOUND IN DOCUMENT).
- Trade payable ageing FY25 (Note 20(b) p.220): the "Others" row (1-2y 61.39, 2-3y 0.33, >3y 0.21) does not agree with its total row (2-3y 1.07, >3y 7.70). The FY26 ">3 years" others figure 7.97 cannot come from the row values (0.54) but can from the total row. The FY25 comparative ageing is mis-keyed by about 8. MSME dues older than one year (67.29 at FY25) are nil at FY26.
- Auditor's non-audit fee 5.42 is 67.8% of the audit fee 8.00 (FY25 4.50 / 8.00 = 56.3%) (Note 32 p.225; derived).
- Cash: Note 10 components tie to the CFS split (cash in hand 46.97 + 0.53 = 47.50 vs 47.51; bank 26.14 vs 26.13; CFS p.192).
- Standalone UDIN differs from the consolidated UDIN (26502400OKQXSI9034 vs 26502400RQHPPT7813, p.173 and p.190); one partner, same date 19-05-2026. Normal.

---

## B. WHAT PASS 1 GOT RIGHT (checked, no change)

Receivable ageing, zero ECL, GST contingent liabilities (3,697.75), RPT table and totals, PPE "Property" row, CFS capex tie, borrowing table, gratuity roll-forward, deferred tax, revenue split, current-ratio claim and ROCE-equals-ROI observation all re-tie to the document. Pass 1's receivables-days trend (135.9, 152.1, 203.2) stands on year-end revenue. Pass 1's "OCI FY25 -0.97" is the gratuity element only (see N2.15).

## C. STILL NOT FOUND AFTER THE SECOND READ

Customer concentration; country or product split; own versus partner registration split; ECL model; lease identity and any discount rate disclosure; interest rates and covenants on all debt; 5-year repayment table; leave-encashment liability; tax rate reconciliation; CWIP ageing; capital commitments; Ind AS 10 events note; reason for the Kaler return; ownership of the two new related parties; reason for distribution and testing cost falls; supplier and staff advance detail; BG, FLC and bill-discounting amounts; exit route for 1,166.32 of aged receivables.

---

## PASS 2 NEW FINDINGS SUMMARY (new items only)

| # | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | FY25 CFO includes 1,876.75 of short-term bank borrowing (exact tie 177.52 + 1,876.75 = 2,054.27); like-for-like FY25 CFO 3,395.03 = 85.3% of PAT, not 132.4%; two-year CFO/PAT 47.2%; FY24 not testable | AR FY25 CFS and BS; AR FY26 CFS p.190-191; Notes 16, 19, 21 | 🔴 |
| 2 | FX receivables 8,101.83 -> 15,599.05; USD +82.0%; 59.6% of the receivable build; 227.9 export-receivable days (derived) vs 151.3; non-FX days also up (178.8 vs 153.1) | Note 37 p.229; Note 25 p.222 | 🔴 |
| 3 | At least 1,166.32 (67.4%) of FY25's one-year-plus overdue receivables left the ledger with no provision or write-off line; Kaler sale return 262.75 > sale 121.48 is a candidate route [INFERENCE] | Note 9(a)/(b) p.212; Note 40 p.239; Note 32 p.225 | 🔴 |
| 4 | Gross margin -2.07 points; operating margin +1.79 points from distribution, power, testing, factory lines that fell in rupees; reasons not given | Notes 25, 27-30, 32 p.222-225 | 🟡 |
| 5 | Customer advances 6.01% -> 1.34% -> 1.75% of revenue | Note 22 p.221; AR FY25 Note 21 | 🟡 |
| 6 | Supplier advances 791.13 -> 1,581.25; staff advances 6.22 -> 72.39; other current assets +89.4% | Note 13 p.214 | 🟡 |
| 7 | Security deposits -333.35 (-71.6%), booked as investing inflow, cause unstated | Note 7 p.210-211; CFS p.191 | 🟡 |
| 8 | Lease liability 24.05 fits PV of 2.16 promoter rent over 49 years at about 8.8%; seven-year omission corrected via opening reserves [INFERENCE] | Notes 2.2(n), 3, 18, 22, 31, 40; CARO (i)(c) p.104 | 🟡 |
| 9 | GST penalties at 100% of tax under Section 74 wording; no pre-deposit or interest quantum disclosed | Note 34 p.226-227 | 🟡 |
| 10 | Board report says no conflict RPT; Note 40 shows director-interested flows; three new independent directors this year | Board report p.41-42; Note 40 p.238-239 | 🟡 |
| 11 | Gratuity: implied discount rate about 6.8%; Labour Code cost = 52.1% of opening DBO; funded ratio 44.4% from 73.8% | Note 38 p.231-235 | 🟡 |
| 12 | Other financial liabilities "Others" 315.88 unexplained; statutory dues doubled to 190.51 | Note 21 p.220; CARO (vii)(a) p.105 | 🟡 |
| 13 | CSR requirement 145.94 (FY25) vs 74.30 (FY26) not reconcilable to a plain 2% base | Standalone Note 42(g) p.172-173 | 🟡 |
| 14 | Intangible policy text trimmed vs FY25; building and vehicle depreciation swings; vehicles net block +103%; policy gaps (borrowing cost, grants, translation); template and cross-reference errors in Notes 2.1, 2.2(m), 37 | Notes 2.1, 2.2, 3, 37 p.194-229 | 🟡 |
| 15 | SOCE and Note 15 retained earnings differ by 1.55 (FY25 0.63); 2.20 NCI transfer unexplained | Note 15; SOCE p.193 | 🟢 |
| 16 | Subsidiary investment 354.78 is 7.8x KPL's 51% of share capital; loans to subsidiary mentioned but not shown; 266.31 of outside liabilities to unnamed creditors | AOC-1 p.241; Note 1 p.194; Note 40 | 🟡 |
| 17 | BG, FLC, bill-discounting amounts absent despite facility list; Schedule III items missing | Note 19 p.219; Note 34; Note 41 p.239-240 | 🟡 |
| 18 | Other non-cash 132.23 = gratuity 130.13 + lease interest 2.11 (derived tie); ratio, ROCE, DSCR, payables-ageing tie-outs and defects | CFS p.190; Notes 38, 39, 20 | 🟢 / 🟡 |

```yaml
stage: B02-notes-pass2
company: "KPL"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
pass: 2
input_gaps: []
report_path: runs/kpl-2026-11-15/outputs/reports/02-notes-pass2.md
unit: "INR lakhs (AR face); derived percentages and ratios unit-free"
pass_2_empty: false
new_findings_count: 18
headline_new_findings:
  - "FY25 CFO includes 1,876.75 ST borrowing (177.52 + 1,876.75 = 2,054.27); like-for-like FY25 CFO 3,395.03 = 85.3% of PAT; AR FY25 CFS line 10298 and BS; AR FY26 CFS p.190-191"
  - "FX receivables 8,101.83 -> 15,599.05 (59.6% of receivable build); USD lakh 90.27 -> 164.28; Note 37, p.229"
  - "At least 1,166.32 (67.4%) of FY25 one-year-plus overdue receivables left the ledger, no provision; Note 9(a)/(b), p.212"
flag_candidates:
  - {type: FLAG-CASH, reason: "CFO/PAT below 100% two years running on a like-for-like basis (FY25 85.3% derived, FY26 24.6%); FX receivables 59.6% of build; aged-balance exit route not disclosed"}
corrections_to_pass_1:
  - "FY25 CFO/PAT 132.4% overstated by 1,876.75 of borrowing inside CFO; like-for-like 85.3% (derived)"
  - "Pass 1 OCI FY25 -0.97 is gratuity only; Note 15 total OCI -1.78 includes FCTR -0.81"
```
