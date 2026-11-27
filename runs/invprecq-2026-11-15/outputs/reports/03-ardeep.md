# STAGE 3: ANNUAL REPORT DEEP DIVE (BACKWARD READ), INVPRECQ, run 2026-11-15

Source: runs/invprecq-2026-11-15/inputs/annual-report/Annual_Report_FY2025-26.txt (181 pages, Rs lakh unless stated; "Cr" = Rs crore as printed in the narrative pages). Input B02: outputs/reports/02-notes.md and blocks/B02-notes.yaml.

## 0. READING CONVENTIONS AND LOAD-BEARING FACTS

**Page convention (verifier please read).** The text copy writes "[page N]" at the START of page N. I anchor "AR p.N" to PDF page N, the content that follows the marker. I confirmed this by opening the PDF: PDF page 110 is the standalone cash flow statement (printed page 107), PDF page 74 is Annexure 4 (printed 71), PDF page 75 is Annexure 5 (printed 72). Printed page = PDF page minus 3. The B02 reports anchor each item at PDF page plus 1 (they treated the marker as the page end). Every B02 page anchor therefore reads one higher than mine (example: B02 "CF p.111" = AR p.110 here). Note numbers in B02 are right; only the page digit is off. The correction table is in Phase 2.

**Not read from the AR:** the three results filings, the CARE rationale, the presentations. This stage is AR only, plus the screener Data Sheet for a ten-year cross-check (third party, Rs Cr, labelled where used), plus a narrow search of the FY2024-25 AR (inputs/other, not a run input) only to test whether a named entity is new in this AR.

**PDF pages opened to settle a reading:** 110 (cash flow), 23, 24, 25 (KPI charts), 30 (capacity), 74 (Annexure 4), 75 (Annexure 5).

### Load-bearing facts (first verification priority)

| # | Fact | Result | Evidence |
|---|---|---|---|
| 1 | Cash conversion of the margin jump; 245 vs 133 day cycle | H1 FY27 parts NOT REACHABLE (the AR ends 31-Mar-2026). FY26 baseline CONFIRMED: CFO 2,577.89 = 2.19x PAT 1,176.62 (CF p.110). Own cycle arithmetic: Note 39 days give inventory 99.42 + receivables 80.09 minus payables 77.90 = 101.61 days net (179.51 gross) (Note 39, p.136). That is neither 133 nor 245, and it differs from the "about 134 days" in B02 Pass 1 0.1 (a closing-balance cost-proxy method). Method difference, not an error: stages 5 and 11 should state which basis they use. | CF p.110; Note 39 p.136 |
| 2 | A&D share 6% to 11%; HAL, MKU; monthly supply | FY26 6% CONFIRMED: A&D 1,086.42 of industry revenue 18,539.51 = 5.86% (Cons Note 38, p.173); KPI p.21 and p.24 show 5.86%, defence 7.90 Cr, aerospace 2.97 Cr. H1 FY27 11% NOT REACHABLE. HAL appears only as "HAL Maharatna CPSE was awarded to IPCL in recognition of ... Indigenisation of Aerospace Materials" (Year at Glance, p.77) and "components ... recognized by Hindustan Aeronautics Limited" (p.14): no programme, no value, no volume. MKU: NOT FOUND IN DOCUMENT. "Monthly supply": NOT FOUND IN DOCUMENT. Named A&D orders in the AR: PLR Systems (IWI-Adani JV) Jul 2025 and GTRE (DRDO) Feb 2026, no order value for either (p.77). | p.14, p.77, p.173 |
| 3 | Rs 100 Cr capex vs tangible net worth | NOT REACHABLE. No capital commitment line anywhere (searched "commitment"): only "no material changes and commitments" (Board report item 28, p.58). Events after the balance sheet date: "N.A." (p.55, p.56). TNW check: equity 10,278.09 (BS p.107); Rs 100 Cr = 10,000 lakh = 97.3% (derived). New point: FY26 capex of 2,403.28 cash (23.23 Cr on KPI p.25) was mostly the solar plant (derived, see 3A), so the AR shows no precedent of A&D-capacity capex at any scale. | BS p.107; p.55-58 |
| 4 | Revenue basis mismatch | RECONCILED. Revenue from operations 18,844.62 (P&L p.108; Note 23 p.126). 185.79 Cr = castings segment 18,579.08 (Cons Note 38, p.172). 189.68 Cr = total income 18,968.21 (P&L p.108; KPI p.22). 188.45 Cr screener = 18,844.62. New: the AR itself labels 189.68 Cr "Revenue from Operations" with "14.40%" growth (KPI p.32). That is total income; revenue from operations grew 14.16% (derived: 18,844.62 / 16,507.37). The Board report says total income "increased by 12.58%" (p.55); the true figure is 14.40% (18,968.21 / 16,581.26). | p.32, p.55, p.108, p.126, p.172 |

---

## PHASE 1: AUDITOR'S REPORT AND CARO

**1A Core opinion.** Unmodified standalone opinion: "give a true and fair view ... of the state of affairs of the Company as at 31st March 2026" (Auditor's Report, p.99). Unmodified consolidated opinion (p.138). Internal financial controls: "adequate ... operating effectively as at 31st March, 2026" (Annexure B, p.106). Going concern: no material uncertainty paragraph. Closest language: CARO clause 19, "nothing has come to our attention ... any material uncertainty exists" (p.104). Board report: no regulator order affecting going concern (item 25, p.58). Report date 19 May 2026, partner Ashish Dave, Park & Company, FRN 116825W, UDIN 26170275RHAGNJ3699 (p.101).

**1B Key Audit Matters.**

| KAM | Why key | How addressed | Risk |
|---|---|---|---|
| Revenue from sale of goods (only KAM, standalone and consolidated) (p.99; p.138) | Timing of recognition; "control ... transferred ... mainly upon delivery" | Tests of controls and substantive procedures; no cut-off test named, no quantification (p.99) | YELLOW. The KAM says "delivery"; Note 1.2 l(ii) recognises domestic sales "on dispatch" (p.114) and exports on mate's receipt or shipped on board. Dispatch vs delivery is a cut-off gap on a 14% growth year. |

No KAM on inventory (5,170.18, 23.8% of assets, derived), on capitalisation of 2,321.64 PPE additions including the new solar asset (Note 2, p.116), on related-party balances (306.00 capital advance, 100.00 deposit), or on borrowing classification. Absence of a capex or RPT KAM is a thin-scope signal, not a violation.

**1C Emphasis of Matter / Other Matters.** None standalone. Consolidated Other Matters: the subsidiary (total assets 8.31 lakh, revenue 0.44 lakh, net loss 0.47 lakh) is audited by other auditors and relied on "solely" (p.140). Opinion not modified.

**1D CARO 2020 clause by clause (Annexure A, pp.102-104).**

| Clause | Remark | Risk |
|---|---|---|
| i (PPE) | Records kept; title deeds in company name; no revaluation; no benami | GREEN |
| ii(a) | Inventory verified; differences under 10% per class | GREEN |
| ii(b) | Working capital limits above Rs 5 crore; quarterly returns "generally in agreement"; "average under reported difference is not material", attributed to "valuation, provisions". Difference amount NOT FOUND IN DOCUMENT | YELLOW (unquantified) |
| iii | Loans granted 56.88 in year; outstanding 60.18; repayments regular; no overdue (p.102). 60.18 ties to Note 7 (39.60 + 20.58, p.119) | GREEN |
| vii(a)/(b) | Undisputed dues regular. Disputed: VAT 8.95, FY2002-03, Commissioner of Gujarat Commercial Tax (p.103). Note 35 shows VAT 11.94 (p.132): gap 2.99 unexplained (likely interest; INFERENCE). Contingent 11.94 = 0.12% of equity and 1.0% of PAT (derived) | GREEN |
| ix | No default; no wilful default; term loans applied to purpose; short-term funds "prima facie, not ... used for long-term purposes" (p.103). Test: term debt rose 917.88 while capex was 2,403.28 and working capital finance fell 357.56 (Note 17, p.124): CFO funded the balance, so the statement holds on the numbers | GREEN |
| xi | No fraud; no ADT-4; no whistle-blower complaint (p.103) | GREEN |
| xiii | RPTs comply with s.177/188 and are disclosed (p.103). Compliance statement only, no arm's-length test | YELLOW |
| xvii | No cash losses standalone (p.103). The consolidated report flags clause (xvii) at I&PCL Vacuum Cast Limited: qualified or adverse in the subsidiary's CARO (p.140). NEW vs B02, which did not name it | YELLOW (small) |
| xix | No material uncertainty on meeting liabilities within one year (p.104) | GREEN |
| xx | No unspent CSR (p.104) | GREEN |
| Others (iv, v, vi, viii, x, xii, xiv to xvi, xviii) | Not applicable or clean | GREEN |

**1E Auditor continuity.** Park & Company, Bhavnagar, FRN 116825W. The Board report says the Board approved a "second consecutive term of 5 years" with member approval at the 47th AGM (Board report item 16, p.57). Derived: first term 2017 to 2022, second term to the 52nd AGM (2027), so a mandatory firm rotation falls due in 2027. First appointment year NOT FOUND IN DOCUMENT. Fees (Note 30, p.128): audit 6.95 (includes quarterly review), other services 1.69, total 8.64 (FY25 6.40 / 0.49 / 6.89). Other services = 24.3% of audit fees; they do not exceed audit fees, no flag. Consolidated: audit 7.30, taxation 0.13, other 1.77, total 9.20 (Cons Note 29, p.165). Other services rose 3.4x (0.49 to 1.69) and the AR does not name them. Auditor's governance certificate: unqualified (p.98).

**1F Standalone vs consolidated.** Same KAM, same opinion. Difference: subsidiary under other auditors; CARO clause (xvii) at the subsidiary. Subsidiary is immaterial: cost 25.00, reserves (17.11), total assets 8.31, turnover nil, loss 0.47 (AOC-1, p.65). AOC-1 shows a 99.99% holding while the Notes and the auditor call it "wholly-owned" (Note 6, p.119; p.138). Consolidated equity 10,260.99 vs standalone 10,278.09; the 17.10 gap is the subsidiary loss, so the parent has not impaired a 25.00 investment now worth 7.90 (Cons Note 39, p.173).

**Phase 1 verdict: GREEN (Clean), with three yellow watch items:** KAM wording (delivery vs dispatch), unquantified quarterly-return differences (clause ii(b)), and a 2027 audit-firm rotation. **Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because the opinion is unmodified, CARO standalone is clean, and there is no going concern language.

---

## PHASE 2: NOTES TO FINANCIAL STATEMENTS (verify, extend, summarise)

### 2-V. Verification of the B02 Top 15 against the AR

All 15 numbers and note references re-checked. Result: 15 of 15 VERIFIED on numbers and note numbers. Page anchors in B02 are one higher than PDF pages (convention above). No value discrepancy.

| Rank | B02 claim | My check (page = PDF page) | Mark |
|---|---|---|---|
| 1 | Revenue ops 18,844.62 (16,507.37), +14.16%; 185.79 Cr castings; 189.7 Cr total income | Note 23 p.126; P&L p.108; Cons Note 38 pp.172-173. 18,579.08 + 265.54 wind credits = 18,844.62 foots | VERIFIED |
| 2 | RPT flows 884.92 = 4.70% of revenue; family take 29.1% of PBT | 319.88 + 13.86 + 24.00 + 427.79 + 84.52 + 8.87 + 6.00 = 884.92; /18,844.62 = 4.70%. 393.39 + 84.52 + 24.00 + 6.00 = 507.91; /1,743.49 = 29.1% (Note 38, pp.134-135) | VERIFIED |
| 3 | CMD +51.2%, Jainam +68.7%; Board report +41.10% / +50.27%; ceiling 4.2x | 347.11/229.54; 46.28/27.44; Notes 27 and 38 pp.127, 134; Annexure 5 p.75; Notice item 4 pp.45, 52. 1,800/425.39 = 4.23x | VERIFIED |
| 4 | Capex 2,403.28; plant additions 1,977.42; power assets 1,903.97 (188.59); depreciation step 131.83 to 247.18 | CF p.110; Note 2 p.116; Cons Note 38 p.173. 1,977.42/15 = 131.83; /8 = 247.18 | VERIFIED |
| 5 | CF receivables 135.64 vs 227.10; 77.84 lien build; 99.86 | CF p.110. 4,158.33 - 3,931.23 = 227.10. 35.22 - 3.80 + 164.91 - 118.49 = 77.84 (Notes 8, 13, pp.120-121) | VERIFIED (77.84 placement is INFERENCE) |
| 6 | Debt 7,009.87; short-term 75.8%; term 2,200.88 (31.4%) vs 1,283.00 (19.9%) | Note 17 p.124: 1,617.00 + 502.06 + 81.82 = 2,200.88; 545.82 + 638.35 + 98.83 = 1,283.00; 5,311.05/7,009.87 = 75.8% | VERIFIED |
| 7 | Receivables over 6 months 0.15% (3.13%); days 80.09 (87.63) | Note 11.1 p.121: 5.83/3,931.23; 132.09/4,215.62; Note 39 p.136 | VERIFIED |
| 8 | A&D 1,086.42 (539.01) = 5.86% | Cons Note 38 p.173; foots to 18,539.51 | VERIFIED |
| 9 | Inventory 5,170.18; WIP +12.1%; stores +18.5%; FG -24.9% | Notes 10, 26 pp.120, 127. Stores 1,347.41 / stores consumed 722.54 = 1.86 years | VERIFIED |
| 10 | MSE past due 413.20 vs "within due date" heading | Note 22.1 p.126: 413.17 + 0.03; Note 37 p.133 | VERIFIED |
| 11 | Labour codes 52.51; funded 53.8% (66.4%) | Note 36 p.132; Note 40 p.137. 143.39/266.52; 150.19/226.12 | VERIFIED |
| 12 | Tax: 30.4%; 511.91 unexplained; MAT 224.39 | Note 14 p.122: 492.41 + 511.91 - 576.32 = 428.00 foots; 514.36/1,690.98 = 30.4% | VERIFIED |
| 13 | Ind AS 116: ROU 190.34; liability 148.88; HUF rent 24.00 | Notes 5, 38 pp.118-119, 134. Lease payments 24.00 = HUF rent 24.00; CF lease repayment 12.86 = 24.00 - 11.14 interest | VERIFIED (link is INFERENCE) |
| 14 | Subsidiary cost 25.00, net assets 7.90, turnover nil | Note 6 p.119; AOC-1 p.65 | VERIFIED |
| 15 | Print defects (Cons FY25 EPS 3.03; 6,47.71; CF label; 0.20; 3.03 vs 3.05) | Cons P&L p.145; Note 33 p.130; CF p.110; Cons Note 38 p.173; Notes 13, 18 pp.121, 125 | VERIFIED |

**Anchor correction table (B02 page to PDF page):** CF p.111 = 110; P&L p.109 = 108; BS p.108 = 107; Note 2 p.117 = 116; Notes 8-9 p.121 = 120; Note 11 pp.121-122 = 120-121; Note 14 p.123 = 122; Note 17 pp.125-126 = 124-125; Note 23 p.127 = 126; Notes 27, 28 p.128 = 127; Note 30 p.129 = 128; Notes 33-34 pp.131-133 = 130-132; Note 35 p.133 = 132; Note 36 pp.133-134 = 132-133; Note 38 pp.135-136 = 134-135; Note 39 p.137 = 136; Note 40 p.138 = 137; Board report p.76 = 75; Annexure 4 p.75 = 74; Year at Glance p.78 = 77; Cons Note 38 p.173/174 = 172/173.

### 2A. Accounting policy aggressiveness (extend)

| Item | Finding | Rating |
|---|---|---|
| Revenue | Dispatch-based domestic recognition; export on mate's receipt; export incentives "if ... estimated with reasonable accuracy" (Note 1.2 l, p.114). No contract assets or liabilities note | YELLOW |
| Depreciation lives | Plant 10/15/8 years, buildings 60/30, dies 10 (Note 1.2 c(v), p.112). Plant depreciation 620.55 on average gross plant 12,963.4 = 4.79%, an implied 20.9 year life (derived; Note 2, p.116). Stated lives imply 6.7% to 12.5%. Either much plant is fully depreciated (accumulated 8,193.24 of 13,900.57 = 59%) or a long-life class dominates. Not provable from the AR | YELLOW |
| Capitalisation | Borrowing costs "added to the cost" of qualifying assets (Note 1.2 c(i), o; p.111, p.114). Amount capitalised on the solar plant NOT FOUND IN DOCUMENT. No capitalisation threshold stated | YELLOW |
| Inventory | Weighted average cost; WIP and FG at material plus direct expense plus "appropriate value of overheads", or NRV (Note 1.2 e, p.113). No write-down amount disclosed | YELLOW |
| ECL | Note 1.2 d says simplified approach; Note 33 says "provision matrix" (p.130). No matrix, no rates, allowance now Nil (Note 11, p.120) | YELLOW |
| Allowance movement | FY25 allowance 57.29 (over 1 year, credit impaired, Note 11.1) vs FY26 Nil. Note 30 shows "Provision for doubtful debts/sundry balances written off" 60.03 in FY25 and 12.96 in FY26 (p.128). Fit: the 57.29 was provided in FY25 (the 60.03 line) and written off against the allowance in FY26 (INFERENCE; the FY24 allowance is NOT FOUND in this AR). This answers B02 question 5 in part | GREEN-YELLOW |
| Ind AS 116 | First lease of a building: ROU 161.74 added; discount rate NOT FOUND IN DOCUMENT (Notes 5, p.118-119) | YELLOW |
| Policy changes | None quantified; CEO/CFO certificate: "No significant changes in accounting policies" (p.95) | GREEN |

### 2B. Related-party map (extend)

All figures Rs lakh (Note 38, pp.134-135; unchanged in Cons Note 37, pp.170-172).

| Counterparty | Relationship (AR label "Associates") | FY26 | FY25 | Comment |
|---|---|---|---|---|
| Meche Private Limited | Promoter body corporate, 16.19% holder (MGT-9, p.68); director Vishakha Tamboli sits on its board (Notice Annexure A, p.53) | Purchases 319.88; security deposit 100.00; trade advances 49.75 | 254.93; 100.00; 61.11 | Supplier, landlord ("factory shed", Note 8, p.120) and shareholder. Purchases rose 25.5%; the 100.00 deposit is unchanged. FY24 purchases 159.63 (FY2024-25 AR comparative, not a run input): purchases doubled in two years |
| Tamboli Foundry Supplies and Services Ltd | Promoter-linked | Capital advance 306.00; trade receivable 3.81 | 306.00; 3.81 | "advances towards purchase of property" (Note 9, p.120). Unchanged for a year; no completion date. 306.00 = 45.5% of capital advances 672.55 |
| Shri Tamboli Foundation (Trust) | Promoter-linked | CSR 13.86 | 17.56 | 100% of CSR spend goes to this trust; the CSR report names "Tamboli Foundation" as implementing agency (p.97) |
| Piyush I Tamboli HUF | Promoter group | Rent 24.00 | 20.00 | Rent +20% |
| KMP remuneration | CMD 347.11; Jainam 46.28; Pratapkumar 32.00; CS 2.40 | 427.79 | 291.93 | +46.5% |
| Guarantee commission to CMD | Personal guarantee on bank debt | 84.52 | 71.42 | 1.26% of average debt (derived) |
| Relatives | Kavya Tamboli salary 6.00 | 6.00 | 5.00 | |
| Total | | 884.92 | n/a | 4.70% of revenue from operations |

Value-extraction signals: (i) promoter-family cash take 507.91 = 29.1% of pre-exceptional PBT and about 9.8x the promoter share of the proposed dividend (51.97% of 100.00 = 51.97, derived); (ii) the Board report says all RPTs were "at arm's length basis" (item 21, p.58) with no benchmark; (iii) RPT balances do not move.

### 2C. Contingent liabilities

VAT 11.94 (FY25 11.94), GST nil (19.61) (Note 35, p.132). 11.94 = 0.12% of net worth and 1.0% of PAT. Below both flags (25% and 100%). Stage of each matter, bank guarantee amounts and any income-tax disputes: NOT FOUND IN DOCUMENT. GREEN.

### 2D. Receivables, 2E. Inventory

Receivables 3,931.23 (4,158.33): not due 87.9% (72.6%); 6 months to 1 year 5.83; over 1 year nil; days 80.09 (87.63) (Notes 11.1, 39, pp.121, 136). Concentration: NOT FOUND IN DOCUMENT (no customer split). Unbilled: none disclosed. Inventory days 99.42 (108.75); WIP 2,677.48 (+12.1% vs revenue +14.2%); FG 531.97 (-24.9%); stores 1,347.41 (+18.5%, 1.86 years of consumption) (Note 10, p.120). Change in inventories credit 113.46 (141.12). FG down with revenue up reads as better dispatch; the stores build is a cash tie-up of 209.91.

### 2F. Borrowings (maturity wall, covenants, pledge)

Total 7,009.87 (6,449.55). Term loans 1,617.00 non-current plus 502.06 current maturities, hire purchase 81.82, working capital finance 4,808.99 (Note 17, p.124). All secured: land and building mortgage, plant, inventories, book debts and fixed deposits, plus a director's personal guarantee (p.125). Maturity buckets beyond one year: NOT FOUND IN DOCUMENT (Note 33 shows one bucket, 1,698.82 "more than one year", p.130). Rates, lenders, covenants: NOT FOUND IN DOCUMENT. Floating exposure: +100 bps = 70.10 pre-tax, which implies about 7,010 of floating debt, i.e. all debt (Note 33, p.131; derived). Bank finance cost 477.84 on average debt 6,729.71 = 7.10% (derived). Promoter share pledge: nil (MGT-9, p.68). ICDs given: none (CARO iii, p.102). Rating: CARE BBB- long term, A3 short term (Board report item 32, p.59). Maturity wall in the next 12 months: 5,311.05 (75.8%), of which 4,808.99 is revolving working capital and 502.06 term repayments (derived). A rating at the bottom rung of investment grade plus a short-term bulk is the key financing fact for stage 11.

### 2G. Deferred tax

DTL 743.85 (661.69): depreciation 1,051.48, less 43B disallowances 307.63 (Note 20, p.125). Movement 82.16 = P&L 78.75 + OCI 3.42 (derived, foots to rounding). Board report item 36 says the DTL "has been debited from the amount available for appropriation" (p.59), but the P&L charges it (p.108). Wording defect, no amount effect.

### 2H. Exceptional items, goodwill, ESOP, leases, post balance sheet

Exceptional 52.51 (labour codes), first in three years (Note 40, p.137). Goodwill: none. ESOP and sweat equity: none (KMP table p.72). Leases: liability 148.88, current 24.00 (Note 5, p.119). Post balance sheet events: "N.A." (Board report items 6 and 10, pp.55-56). The Rs 100 Cr approval in the Q2 FY27 filing sits outside this AR.

### 2-X. Triple-pass reconciliation

B02 accounting quality score 7/10. My Phase 2 verdict: YELLOW (moderate), consistent with 7/10. I agree on statutory hygiene (clean ageing, audit trail on, no qualification). I add three points B02 did not: (1) the 57.29 allowance fits a FY25 provision followed by a FY26 write-off (reduces concern); (2) other borrowing cost 99.86 and the increase in other current assets 99.86 (586.11 less 486.25) carry the identical figure on unrelated lines (derived; no inference drawn, verifier please check); (3) the CFO label "Cash generated from operations (103.34)" is the sum of working capital movements, and true cash from operations is 2,940.46 before tax (3,043.80 - 103.34, derived).

**Phase 2 verdict: YELLOW (Watch).** **Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because no note shows earnings management; each yellow is a disclosure gap or an RPT question.

---

## PHASE 3: FINANCIAL STATEMENTS (cash flow first)

### 3A. Cash flow (Standalone CF, p.110; Rs lakh)

| Line | FY26 | FY25 |
|---|---|---|
| Net profit | 1,176.62 | 606.62 |
| Operating profit before working capital | 3,043.80 | 2,216.66 |
| Working capital movements (sum) | (103.34) | (167.72) |
| Tax paid | (362.57) | (148.99) |
| CFO | 2,577.89 | 1,899.95 |
| Capex (payments for PPE) | (2,403.28) | (444.84) |
| FCF after capex (derived) | 174.61 | 1,455.11 |
| Interest paid | (512.21) | (594.68) |
| Dividend paid | (51.12) | (50.33) |
| Net borrowings | +560.32 | (974.41) |
| Net change in cash | +197.54 | (120.27) |

Ratios (derived): CFO/PAT 2.19x (3.13x); CFO/EBITDA 81.6% (81.8%) on company EBITDA 3,160.85 (see 3C); capex/depreciation 2.82x (0.55x); capex 12.75% of revenue. After interest paid and dividend, FY26 free cash was (349.92) once the 8.51 asset sale and 30.29 interest received are counted; borrowings of 560.32 closed the gap.

**CFO quality checks.**
- Inflators: receivables fall (net 227.10); payables and other financial liabilities up (payable towards services received 183.50 vs 59.08, Note 18, p.125; whether capex creditors sit in this line is not stated: INFERENCE risk of capex creditors inside CFO); the capital advance rise of 17.70 sits in the "other assets" line (586.11 - 486.25 + 672.55 - 654.85 = 117.56, derived; CF shows 117.57).
- Deflators: inventory build 298.03; lien deposits 77.84 (INFERENCE, inside CFO); other borrowing cost 99.86 left in CFO while only 518.11 finance cost is added back (CF p.110; Note 28, p.127).
- Interest classification: interest paid sits in financing (512.21); other borrowing cost 99.86 sits in CFO. Fit: other borrowing cost includes the 84.52 guarantee commission to the CMD (84.52 + 15.34 = 99.86; INFERENCE, classification not stated).
- Payable stretching: payable days 77.90 vs 77.60 (Note 39, p.136); no stretching.
- Inventory rundown: none; inventory built.
- Solar capex vs segment: Power segment assets 1,903.97 (188.59) and liabilities 1,126.48 (nil) (Cons Note 38, p.173). Segment assets rose 1,715.38 (derived), against plant additions of 1,977.42 (Note 2, p.116): about 87% of plant additions is the power segment (INFERENCE; assumes the wind assets did not move). Segment liabilities of 1,126.48 are 66% of the asset step, so the solar plant looks mostly debt funded (INFERENCE; term debt rose 917.88).
- Multi-year cross-check (screener Data Sheet, Rs Cr, third party): CFO FY17 to FY26 sums to 138.98; investing to (112.62); PAT 53.08. FY26 CFO 25.78 is the ten-year high. Cumulative CFO/PAT 2.6x. FY26 investing (23.64) is 2.4x the FY17-FY25 average of 9.9 (derived). (screener-Data_Sheet.csv, rows Cash from Operating and Investing Activity, Net profit.)

No deterioration in CFO quality: FLAG-CASH not raised. The weak point is free cash after capex, interest and dividend, and the unreconciled composition.

### 3B. Balance sheet walk (BS p.107; Rs lakh)

| Item | 31-Mar-26 | 31-Mar-25 | Change |
|---|---|---|---|
| PPE net | 9,866.35 | 8,379.66 | +17.7% |
| CWIP | 142.46 | 60.82 | |
| ROU | 190.34 | 46.65 | |
| Other non-current assets (capital advances 672.55) | 672.55 | 654.85 | |
| Inventories | 5,170.18 | 4,872.15 | +6.1% |
| Trade receivables | 3,931.23 | 4,158.33 | -5.5% |
| Cash and bank | 387.51 (219.57 + 167.94) | 144.69 | |
| Total assets | 21,679.96 | 19,493.06 | +11.2% |
| Equity | 10,278.09 | 9,143.16 | +12.4% |
| Debt (non-current 1,698.82 + current 5,311.05) | 7,009.87 | 6,449.55 | +8.7% |
| Lease liabilities | 148.88 | nil | |
| Trade payables | 2,821.07 | 2,737.68 | +3.0% |
| DTL | 743.85 | 661.69 | |

Key ratios (derived unless marked): D/E 0.68 (0.71) (Note 34, p.132); net debt on free cash 6,790.30 (7,009.87 - 219.57), ND/EBITDA 2.15x (FY25 2.77x, on 6,427.52 / 2,323.78); current ratio 1.20 (1.12) (Note 39); quick ratio 0.60 (0.57); EBIT/finance cost 3.82x (2.25x) (EBIT = pre-exceptional PBT + finance cost = 2,361.46); EBITDA/finance cost 5.20x (3.46x); DSCR 2.36 (1.59) (Note 39, p.136); equity/assets 47.4% (46.9%). ROCE: three figures, none reconciles. Note 39 12.80% (9.30%), KPI chart 13.10% (9.30%) (p.24), and my EBIT/(equity + debt) of 13.7% (9.7%). Goodwill: none. Debt cost of 7.10% sits below ROCE of about 13%, but the spread is thin once the 29% tax rate and a BBB- risk premium are counted.

**DuPont (closing balances; derived).** ROE 11.45% (6.63%) = net margin 6.24% (3.67%) x asset turnover 0.869 (0.847) x equity multiplier 2.109 (2.132). Note 39 reports ROE 12.12% (6.84%) on average equity (p.136). The ROE gain is almost entirely margin (+70%); turnover +2.6%; leverage -1.1%. ROE is operational, not leverage-driven.

### 3C. P&L (p.108; Notes 23-30, pp.126-128; Rs lakh)

| Line | FY26 | FY25 | YoY |
|---|---|---|---|
| Revenue from operations | 18,844.62 | 16,507.37 | +14.16% |
| Other income | 123.59 | 73.89 | +67.3% |
| Materials consumed less inventory credit | 5,102.59 | 4,690.40 | +8.8% |
| Employee benefits | 1,221.75 | 1,003.81 | +21.7% |
| Power and fuel | 1,950.68 | 1,985.20 | -1.7% |
| Fettling and external processing | 5,158.98 | 4,380.79 | +17.8% |
| Other expenses (total) | 9,430.51 | 8,563.27 | +10.1% |
| Depreciation | 851.90 | 812.80 | +4.8% |
| Finance cost | 617.97 | 672.38 | -8.1% |
| PBT before exceptional | 1,743.49 | 838.60 | +107.9% |
| Exceptional | 52.51 | nil | |
| PAT | 1,176.62 | 606.62 | +93.9% |

**Other income** 123.59 = 7.1% of pre-exceptional PBT (8.8%): below the 20% flag. FX gain 75.30 (39.98) = 4.3% of PBT; it is a volatile line.

**Margin waterfall (derived, operating EBITDA excluding other income and exceptional).** FY26 3,089.77 = 16.40% of revenue from operations; FY25 2,249.89 = 13.63%. Gain 277 bp. Company EBITDA 31.61 Cr = 16.66% (KPI p.23) is a different base: 3,160.85 = PBT after exceptional + finance + depreciation, on total income 18,968.21, so it includes other income and bears the 52.51 charge. Drivers as percent of revenue, FY25 to FY26: materials net of inventory credit 28.42% to 27.08% (-134 bp); power and fuel 12.03% to 10.35% (-168 bp); stores and spares 4.44% to 3.83% (-61 bp); admin 3.72% to 3.24% (-48 bp); partly offset by external processing 26.54% to 27.38% (+84 bp) and employee cost 6.08% to 6.48% (+40 bp). Components net to -278 bp (foots to 277 within rounding). Power and fuel plus materials explain 302 bp, more than the whole gain. Volume vs price: dispatch 1,557 t (1,372 t) +13.5% (KPI p.23); revenue per tonne 12.10 lakh vs 12.03 lakh, +0.6% (derived). Growth was volume; no price or mix premium shows in the average realisation. Whether the solar plant explains any of the power and fuel drop cannot be tested: commissioning date, generation and cost NOT FOUND IN DOCUMENT.

**Tax:** effective 30.4% (27.7%); FY25 used the MAT rate 27.82% and a 224.39 MAT credit (Note 14, p.122). **EPS:** basic = diluted 11.77 (6.07) standalone; consolidated 11.76 and a misprinted consolidated FY25 3.03 (should be 6.06) (p.145).

**Phase 3 verdict: YELLOW (Watch).** Quality of CFO holds; funding of capex, the weight of the solar asset, and a thin ROCE spread keep it yellow. **Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because CFO is 81.6% of EBITDA and interest cover rose to 3.8x.

---

## PHASE 4: RISK FACTORS AND MD&A

### 4A. Disclosed risks (MD&A p.76; Board report item 19, p.57)

The AR has no risk-factor section. Risk management in the Board report is one generic paragraph (item 19, p.57). The MD&A (one page, p.76) carries a SWOT:

| Disclosed item | Real or boilerplate |
|---|---|
| Challenge: "High capital intensity and elevated fixed-cost structure" | Real (capex/depreciation 2.82x; depreciation 851.90) |
| Challenge: "Sector concentration risk in top revenue contributors" | Real but unquantified: no customer or percentage anywhere (see 4B) |
| Challenge: recruitment of casting metallurgists | Boilerplate; no attrition figure (165 permanent staff, p.75) |
| Challenge: nascent A&D supply ecosystem | Real |
| Threats: US tariffs, geopolitics, commodity (nickel, cobalt, copper, aluminium), foreign low-cost foundries, European and North American slowdown, additive manufacturing | Mostly boilerplate. Exports are 11.82% of revenue (2,227.15, Note 23, p.126); the US share is NOT FOUND IN DOCUMENT. The commodity list omits steel and alloy scrap, the main input of a steel castings maker (INFERENCE; product mix is "Carbon Steels, Stainless Steels", p.30) |

### 4B. Missing risks (obvious from Phases 1-3, absent from the risk text)

| # | Missing risk | Evidence | Likely reason for omission |
|---|---|---|---|
| 1 | Dependence on external processing: "Fettling and other external processing charges" 5,158.98 = 27.4% of revenue, +17.8% (Note 30, p.128), while the AR says "fully integrated, one-stop-shop" (p.33) and "vertically integrated" (p.30) | Note 30 p.128; p.30, p.33 | Contradicts the integration pitch; vendors unnamed (Meche purchases 319.88 may sit here, not stated) |
| 2 | Funding structure: 75.8% short-term floating debt, BBB- / A3 rating, no covenant disclosure | Note 17 p.124; Note 33 pp.130-131; Board report item 32, p.59 | Rating is reported as a fact, not as a risk |
| 3 | Promoter-related counterparties: unmoved 306.00 and 100.00; supplier, landlord, trust and guarantor all family-linked | Note 38 pp.134-135; Notes 8-9 p.120 | Board report states "arm's length" (p.58) |
| 4 | Customer concentration unquantified; no Ind AS 108 major-customer line | Cons Note 38 pp.172-173 shows geography and industry only; MD&A names the risk without numbers (p.76) | A disclosure is not required if no customer exceeds 10%, but the AR does not say so (NOT FOUND IN DOCUMENT) |
| 5 | Auto concentration and powertrain transition: auto 63.84% (60.05%); components listed are transmission, engine, clutch and EGR parts (p.26) | Cons Note 38 p.173; p.24; p.26 | Threat list omits electrification (INFERENCE: whether these parts are ICE-specific is not stated) |
| 6 | Solar execution and depreciation step: 1,903.97 segment assets, date and cost not filed; four places say commissioned or installed and one says in development | p.14, p.18, p.19, p.74, p.77, p.173 | Annexure 4 text looks carried over from earlier drafting |
| 7 | Single-site exposure: only one factory address given | CG general information (p.89): "Nari Road, Bhavnagar" | Not discussed |
| 8 | Labour-code follow-on and gratuity underfunding: funded 53.8%, no FY26 contribution | Note 36 p.132; Note 40 p.137 | Company says more clarity is awaited |
| 9 | Key-person and family control: CMD, spouse and son on the Board and in executive roles; CMD also the SIDM Gujarat chair (p.18) | p.78; p.18 | Succession compliance table says "Yes" (p.91) with no detail |

### 4C. MD&A deep dive

**Industry claims (p.76):** global investment casting market "approximately $18-20 billion in 2025-26", CAGR 4.7-5.4% to 2032-34; A&D 36-46% of global revenue; Asia-Pacific over 42%. Source: "Independent industry research", unnamed. India: "FY 2025-26 defense capital allocation ... approx. Rs 1.48 lakh crore, with around 75% reserved for domestic procurement"; defence exports "Rs 159 billion in FY23 ... projected to grow at a CAGR of ~17% to reach Rs 538 billion by FY30". My arithmetic on those endpoints gives 19.0% a year ((538/159)^(1/7) - 1), not 17% (derived). The Chairman cites a "defence budget exceeding Rs 7.85 lakh crore" (p.18); this is the total budget and the 1.48 lakh crore is the capital outlay: both can be right, but they are unlabelled.

**Growth and margin explanations.** CFO letter: revenue +14%, EBITDA +36%, PAT +93%; margin from 14.01% to 16.66% "as a result of our sustained efforts towards diversification into high-value segments" (p.19). Credit-taking pattern: the company credits itself (diversification, cost discipline) and cites no external factor either way. Test: of the increase in revenue by industry division of 2,284.68 (18,539.51 - 16,254.83), auto gave 2,073.47 (90.8%), A&D 547.41 (24.0%), non-auto fell 336.20 (-14.7%) (Cons Note 38, p.173; derived). Auto share rose from 60.05% to 63.84% (p.24). The margin gain is explained by power and fuel and materials (3C), not by mix toward A&D, which is 5.86% of revenue. The CFO's attribution is unproven by the AR's own numbers.

**Forward guidance table.** The AR contains no numeric guidance on revenue, margin, capex, order book or capacity.

| Claim | Number | Timeframe | Credibility |
|---|---|---|---|
| Solar plant "operational targeted for the second half of FY 2026" (Annexure 4, p.74) | 4 MW | H2 FY26 (Oct 2025 to Mar 2026) | LOW. The period had ended on the report date 19 May 2026; p.77 says "installed and commissioned"; date NOT FOUND |
| Solar "expected to deliver tangible financial benefits through lower energy costs and improved operating margins" (CFO, p.19) | none | "coming years" | UNSCORABLE; no kWh, no Rs saving |
| "Positioned to enter a decisive phase of growth" in civil aviation castings (p.36) | none | none | LOW specificity; no civil order named in Year at Glance (p.77) |
| "Turn Mill Centres on order" (p.28) | none (counts conflict, see 6E) | none | UNSCORABLE |
| Dividend 10%, Rs 1 per share = 100.00 (Board report item 5, p.55; Notice p.45) | 100.00 | AGM 13 Aug 2026 | HIGH (payout 8.5% of PAT, derived) |
| Rs 18.00 Cr managerial pay ceiling in loss or low-profit years (Notice item 4, p.45) | 1,800 | per year | Not guidance; a permission |

**Segment analysis.** Two reportable segments: investment castings (revenue 18,579.08, PBIT 2,212.22 = 11.9%, FY25 8.7%) and power generation (265.54 wind credits, PBIT 148.78 = 56.0%) (Cons Note 38, p.172). Castings PBIT +56.4%. The power segment has no external revenue from solar; any captive saving sits in castings and is not visible. The brief says Q2 FY27 shows one segment: a change from the AR, to be checked in stage 4.

### 4D. Tone and credibility (1 to 5)

| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2 | Debt terms, solar cost and date, capacity, customers, capex commitments all absent (Phase 2) |
| Consistency | 2 | Capacity 3,060 t (p.30 graphic) vs 1,500 t (p.30 text); CNC machines 21, 51, 446 (pp.28, 31); board "six directors" (p.78) vs nine on the certificate (p.92); solar "development" vs "commissioned"; consolidated PAT 1,176.15 set beside standalone total income in the Board report table (p.55) |
| Specificity | 2 | No guidance figure; benefits stated without numbers |
| Accountability | 2 | No miss acknowledged; BSE fine mentioned with no amount (p.89) |
| Capital allocation sense | 3 | Deleveraged ratio-wise and dividend raised to Rs 1, but 306.00 and 100.00 parked with related parties and a debt-funded solar asset |

**Contradictions vs Phases 1-3.** "Healthy cash generation" supports D/E 0.68 (p.19), but debt rose 560.32 and free cash after interest and dividend was negative (349.92). The "diversification" claim sits against auto-led growth (Phase 3C).

**Phase 4 verdict: YELLOW (Watch).** **Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because the gaps are disclosure and narrative, not evidence of misstatement.

---

## PHASE 5: CORPORATE GOVERNANCE AND BOARD

### 5A. Board composition (CG report pp.78-80, p.92)

| Director | Role | Meetings (of 5) | Other public boards | Flags |
|---|---|---|---|---|
| Piyush I Tamboli | CMD, promoter | 5 | 1 | Chairman is executive |
| Vishakha P Tamboli | Non-executive, promoter spouse | 5 | 1 | Also on boards of Meche, Tamboli Foundry, I&PCL Vacuum Cast (Notice Annexure A, p.53): promoter-group cross-board seats |
| Jainam P Tamboli | WTD and CFO, son | 5 | 1 | CFO sits on the Audit Committee (p.81) |
| B Pratapkumar | WTD, professional | 4 (80%) | 1 | |
| Saurabh Poddar | Independent, since Nov 2022 | 5 | 2 | Audit chair |
| Jatan G Shah | Independent, since Apr 2024 | 4 | 1 | |
| Pankaj N Bhayani | Independent, since Sep 2023 | 3 (60%) | 2 | Attendance below 75%; NRC chair, attended 0 of 1 NRC meeting (p.82) |
| Ashwini R Doshi | Independent, since May 2024 | 5 | 1 | |
| Akshay R Shah | Independent, since 22 May 2025 | 4 | 1 | Attended 0 of 1 NRC meeting |
| Mamta Devi Raol | Independent, to 12 Jan 2026 | 3 (60%) | 1 | Attendance below 75%; did not attend last AGM (p.79) |

Flags: no independent above 10 years (longest about 4 years); two below 75% attendance (Bhayani, Raol); promoter-group cross-board seats (Vishakha); no director above 8 seats. Composition text conflict: "six Directors ... three Non-Executive (independent) and one Non Executive Woman Director" (p.78) vs nine directors on the 4-May-2026 non-disqualification certificate (p.92) and five independents on the committee tables. At 31 March 2026 nine directors, five independent (55.6%), meets the 50% rule for an executive chairman (derived).

### 5B. Committees

- Audit Committee (p.81): 8 members at year start: six independents, CMD and CFO. Four meetings; Poddar, Piyush, Doshi and Jainam attended all four. The CMD and the CFO sit on the committee that oversees their own reporting. Quorum and an independent majority are met; independence in substance is weaker.
- NRC (pp.82-83): one meeting in the year, 22 May 2025; the chair attended 0 of 1; the CMD is a member and so is the CMD's spouse (p.82). The text says the NRC "presently consists of eight member's i.e. six (6) Non-executive Independent Directors, one non independent, one executive" while the table shows five independents plus CMD and spouse. The FY26 pay step-ups were set in a year with one NRC meeting that the chair did not attend.
- SRC (p.84), CSR committee (p.85) and the independent directors' meeting (p.85) each met once, all on 22 May 2025, the same day as the first Board and Audit meetings (pp.79, 82). Five governance bodies on one day.
- No complaints received (p.84). No risk management committee (marked NA, p.91; basis not stated).

### 5C. Compensation (Note 38, pp.134-135; Annexure 5, p.75; MGT-9, pp.72-73)

| KMP | FY26 | FY25 | Change | % of PAT |
|---|---|---|---|---|
| CMD salary and commission | 347.11 (283.41 + 63.70) | 229.54 | +51.2% | 29.5% |
| CMD guarantee commission | 84.52 | 71.42 | +18.3% | 7.2% |
| Jainam (WTD, CFO) | 46.28 | 27.44 | +68.7% | 3.9% |
| Pratapkumar (WTD) | 32.00 | 32.55 | -1.7% | 2.7% |
| CS | 2.40 | 2.40 | 0% | |
| Directors total (Note 27) | 425.39 | 289.53 | +46.9% | 36.2% |
| Family cash take (CMD, guarantee, Jainam, HUF rent, Kavya) | 507.91 | n/a | | 43.2% of PAT; 29.1% of PBT pre-exceptional |

Context: pre-exceptional PBT rose 107.9%, so director pay lagged profit but ran 6.7x the median employee pay growth of 7% (Annexure 5, p.75). Annexure 5 puts CMD pay at 95.57x the median (printed "1:95:57"). The three ratios printed imply three different medians (CMD 431.63 / 95.57 = 4.52 lakh; Jainam 46.28 / 13.13 = 3.52; Pratapkumar 32.00 / 10.39 = 3.08; derived): the table is not on one base. The Board report percentages (+41.10%, +50.27%, +7.00%) differ from Note 38 (+51.2%, +68.7%, -1.7%) with no basis stated. The Notice asks members to approve a ceiling of Rs 18.00 Cr in loss or inadequate-profit years, 4.2x FY26 director pay (Notice item 4, pp.45, 52). AGM held 13 Aug 2026; voting result NOT FOUND in the corpus. The auditor states pay "is in accordance with ... section 197 read schedule V" (p.101). ESOP dilution: none. Promoter family payroll: Kavya Tamboli 6.00.

### 5D. Shareholding (MGT-9, pp.66-68; Note 15, p.123)

Promoter and group 51.97% at both dates, 5,197,314 shares post bonus; pledge nil; no change in the year apart from the 1:1 bonus (1 July 2025 per MGT-9, allotted 27 June 2025 per Note 41; the dates differ by days) and a transmission of R K Menon's 3,200 shares to Vishakha Tamboli. No promoter selling. Print defect: P I Tamboli's year-end holding is printed 1,317,992 (p.68) vs 1,311,930 elsewhere (pp.70, 123); the printed rows sum to 5,203,376 against the printed total 5,197,314, a difference of 6,062 that disappears with 1,311,930. Public: Rekha N Shah 10.00% (1,000,000); institutions nil (IEPF 0.41% only); FIIs 11,000 shares to nil (p.67). Dividend recommended Rs 1 (100.00), promoter share 51.97 (derived). Low institutional ownership is not treated as a risk. Share price (p.87): Mar-26 close Rs 502.90, Apr-25 high Rs 834, Jun-25 high Rs 1,100 (month highs are printed without bonus adjustment). Collector CMP Rs 1,322 (B00 collector_defect_gate, not AR evidence) is 2.6x the 31-Mar-2026 close (derived).

### 5E. Governance red-flag checklist

| Item | Finding |
|---|---|
| Whistle-blower complaints | None (p.103, p.89) |
| SEBI actions | None named. "A fine ... was imposed by Bombay Stock Exchange for delay in appointment of Independent Director" under Regulation 17 (p.89); amount and date NOT FOUND IN DOCUMENT. The same paragraph says "no penalty was imposed" |
| RPT committee | Audit Committee grants omnibus approval; "None of the transactions ... in conflict with the Company's interest" (p.89) |
| Auditor fee ratio | Non-audit 24.3% of audit; no flag (Note 30, p.128) |
| CSR compliance | Spent 13.86 = obligation 13.86 after set-off 4.92 (CSR report p.96); 100% to the promoter trust (Note 30, p.128). Inside the CSR report: item 7(c) shows 12.64 and the project table 13.85; the committee table lists Jainam Tamboli twice, once as independent (pp.96-97) |
| Section 143(12) fraud | None (p.60; CARO xi, p.103) |
| Material subsidiary auditor | Not material (assets 8.31); other auditors (p.140) |
| Secretarial audit | Clean in substance; e-forms were "filed with additional fees" (late) and the Board report says the observation is "self explanatory" (pp.57, 61, 63). The number and form NOT FOUND |
| Other print defects | Proxy form names the "50th" AGM (p.176); Annexure 5 median basis; KMP table totals the CS at 2.35 vs 2.40 (p.73) |

**Phase 5 verdict: YELLOW (Watch), close to RED on pay governance.** FLAG-PROMOTER-PRELIM is not raised: no pledge, no selling. The concern is value flow to the promoter family and a thin NRC process, not holding behaviour. **Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because there is no pledge, fraud, or adverse regulatory finding. A reviewer would want the AGM vote on Item 4 and the NRC record before sizing.

---

## PHASE 6: CHAIRMAN'S LETTER AND FRONT MATTER (read last)

### 6A. Narrative vs reality

| Claim | Source | Result |
|---|---|---|
| "Highest-ever turnover" | Chairman p.18 | YES. Total income 18,968.21; prior peak FY24 172.08 Cr (KPI p.22) |
| Revenue +14%, EBITDA +36%, PAT +93% | CFO p.19 | YES, on the company's bases (14.16%, 36.0% on 31.61 vs 23.24 Cr, 93.9%) |
| EBITDA margin 14.01% to 16.66% "as a result of ... diversification into high-value segments" | CFO p.19 | NUMBERS YES; ATTRIBUTION NO. The gain is power, fuel and materials; A&D is 5.86%; auto share rose |
| ROCE 9% to 13% | CFO p.19 | PARTLY. KPI 9.30 to 13.10 (p.24); Note 39 says 12.80 (p.136) |
| D/E 0.71 to 0.68 "supported by healthy cash generation" | CFO p.19 | RATIO YES; absolute debt +560.32; FCF after capex 174.61, negative after interest and dividend |
| "Broad-based acceleration across all five business segments" | KPI p.21 | NO for non-auto. Industrials 37.60 Cr vs about 43.2 Cr (-12.9%, derived from 26.55% x 162.55 on p.24); non-auto plus farm 56.18 vs 59.54 (Cons Note 38, p.173) |
| Defence "more than doubling" to 7.90 Cr; aerospace "strongest-ever" 2.97 Cr | KPI p.21 | YES (3.29 to 7.90, +140%; 2.10 to 2.97, +41%); but defence is lumpy: 5.65 in FY24, 3.29 in FY25 (p.24) |
| Solar "successfully commissioned" "during the current financial year" | Chairman p.18 | UNPROVEN. Annexure 4 contradicts; date NOT FOUND. "Current financial year" is ambiguous for a report dated May 2026 |
| "Multi-sector positioning acts as a key risk mitigant" | p.29 | NO in numbers: auto 63.84%, concentration rising |

### 6B. Strategic priorities

Stated (p.18): expand international footprint, deepen core manufacturing, digitalisation, customer value. Specific enough? No target for any. Capital allocated: FY26 capex 23.23 Cr (3.4x the FY22-FY25 average of 6.8 Cr, KPI p.25) went mostly to the solar plant (derived). Execution evidence: exports 22.27 Cr (+36.3%; still below FY22 25.66 Cr, p.23), defence 7.90 Cr, two named defence orders (p.77). Digitalisation and "AI/ML" appear (p.18, p.76) with no spend, system, or result.

### 6C. Metrics showcased vs conspicuously absent

Showcased: records, EBITDA margin, ROCE, D/E, dispatch tonnes, EPS, dividend. Absent: capacity utilisation (and two capacity figures), order book and book-to-bill, customer concentration, capex plan and commitments, borrowing terms, cash conversion, ND/EBITDA, FCF, R&D spend, solar generation and savings, A&D order values, rejection rates.

### 6D. Tone and drift

Prior-year tone comparison not inferable from this run's inputs (the FY2024-25 AR is not a run input).

### 6E. Quiet Abandonment Check

| # | Opening claim (quote) | Operational section | Class | Materiality |
|---|---|---|---|---|
| 1 | "broad-based acceleration across all five business segments" (KPI, p.21) | Cons Note 38 p.173: non-auto -5.7%; industrials about -12.9% | (a) implicit retraction | MATERIAL: shows the growth is auto-led |
| 2 | Civil aviation "decisive phase of growth" and "secure incremental volume orders" (p.36) | Year at Glance lists two orders, both defence (p.77); aerospace revenue 2.97 Cr, 1.60% of revenue (p.24); no civil order, customer or value | (b) silent drop | MODERATE: the A&D step-up is the thesis core; this part has no evidence |
| 3 | "fully integrated, one-stop-shop" (p.33); "vertically integrated" (p.30) | Note 30 p.128: external processing 5,158.98 = 27.4% of revenue | (c) hedged retreat | MODERATE: cost structure and margin durability |
| 4 | Capacity "3,060 metric tonnes across all plants" (p.30 graphic) | Same page text: "total annual casting capacity of 1,500 metric tonnes"; dispatch 1,557 t (p.23) | (a) implicit retraction (one of two claims) | MATERIAL for utilisation: 50.9% of 3,060 or 103.8% of 1,500 (derived); undecidable here |
| 5 | CNC "21 machines" (p.28), "51 machines" (p.28, p.31), "446 CNC machines comprising 31 VMCs, 16 Turning Centres, and 5 Turn Mill Centres" (p.31); 31 + 16 + 5 = 52 | Counts do not agree | (c) hedged | FRAMEWORK NOISE |
| 6 | Solar "in the development phase, with operational targeted for the second half of FY 2026" (p.74) | "installed and commissioned" (p.77); "successful commissioning" (p.18) | (a) implicit retraction of the older text; no acknowledgement | MATERIAL for the depreciation step and cost saving |
| 7 | R&D "institutionalised function" (p.37) | Board report item 3: one line (p.55); no spend, no capitalised R&D (Note 4: intangibles only 25.66, no additions, p.118) | (b) silent drop | LOW to MODERATE |
| 8 | Vacuum casting as capability and expert hire (Annexure 4, p.74) | Vacuum Cast subsidiary: nil turnover, 16 years after incorporation (CIN year 2010), cash losses flagged by the auditor (AOC-1 p.65; p.140) | (b) silent drop | LOW |
| 9 | Carbon credit monetisation and AI/ML in opportunities (p.76) | No revenue or spend line in Notes 23, 24, 30 | (b) silent drop | FRAMEWORK NOISE |

**Phase 6 verdict: YELLOW (Watch).** **Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because the narrative gaps change how growth is read (auto-led, not A&D-led), not whether the numbers are real.

---

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Call | Top 3 reasons |
|---|---|---|
| GARP | WATCHLIST | (1) Earnings recovery is real: PAT +93.9%, EPS 11.77, operating margin +277 bp, ROE 12.12% on average equity vs 6.84% (p.108; Note 39 p.136). (2) The growth base is volume only (+13.5% dispatch, +0.6% price); the 4-year revenue CAGR FY22 to FY26 is 9.3% on total income (KPI p.22) and FY23 to FY26 is 3.6% (derived). (3) Price: collector CMP Rs 1,322 vs FY26 EPS 11.77 is about 112x trailing (derived, B00 CMP, not AR); GARP cannot be tested without the forward base from stages 5 and 11. |
| Turnaround | WATCHLIST | (1) Not a classic turnaround: profit in every year except FY20 (screener: PAT FY20 (0.72) Cr; FY22 0.17 Cr; FY26 11.76 Cr). (2) FY26 PAT 11.76 Cr is only 18% above FY19's 9.93 Cr (screener, rupee PAT, unaffected by the bonus): a rebound to a prior peak, not a new level. (3) ROCE 4.67% (FY22) to 13.10% (FY26) (KPI p.24) shows the recovery; sustainability is the question. |
| Value + Quality | FAIL | ROCE 12.8% to 13.1% below a 15% quality bar; BBB- rating; P/B on collector market cap Rs 1,322 Cr vs equity 102.78 Cr is 12.9x (derived, B00 + BS p.107). |
| Capex-led growth | WATCHLIST | Capex 23.23 Cr vs 6.8 Cr average (p.25), but derived as mostly solar; no A&D capacity capex, commitments or plan in the AR; the Rs 100 Cr plan is not in the AR. |
| Cash flow compounder | FAIL | FCF after capex 174.61; negative after interest and dividend; ten-year FCF (CFO less investing, screener) about Rs 26.4 Cr cumulative on PAT of Rs 53.1 Cr. CFO/EBITDA 81.6% is steady. |
| Contrarian | FAIL | Collector CMP is 2.6x the Mar-26 close; nothing is out of favour at this price. |
| Insider confidence | WATCHLIST | Promoter 51.97% flat, pledge nil, no buying or selling (p.68); against that: family take 29.1% of PBT, pay +47%, and 100% of CSR to a family trust. |
| Guidance divergence | WATCHLIST | No numeric guidance in the AR to diverge from; the solar date target (H2 FY26) is the only dated claim and it is stale. |

**GARP and Turnaround fuller reasoning.** The operator mandate is transition alpha. What the AR supports: a margin step (13.63% to 16.40% operating) caused by cost lines that can be named (power and fuel, materials), an A&D line that doubled from a small base (5.39 Cr to 10.87 Cr), exports +36%, deleveraging in ratio terms, and clean receivables. What it does not support: that the climb is A&D-led (A&D is 24% of the revenue increment), that the climb is repriced or unpriced (price is outside the AR), or that working capital and cash conversion improved beyond the receivable fall (net cycle 101.6 days, inventory 99.4 days). One observation separates the two readings: whether H1 FY27 operating margin holds above about 16% without the inventory credit. If the power and materials savings persist and A&D share reaches the claimed 11% with named orders, the climb is real; if margin tracks the inventory credit, the FY26 step is partly absorption. Both tests sit outside the AR and belong to stages 4 and 5.

**Phase 7 best fit:** GARP (transition) WATCHLIST. No strategy PASSES on AR evidence alone.

---

## PHASE 8: FINAL VERDICT DASHBOARD

**Snapshot.** Investment & Precision Castings Ltd, Bhavnagar; listed on BSE since 1976 (p.59); 165 permanent employees (p.75); revenue 188.45 Cr, PAT 11.77 Cr, equity 102.78 Cr, total debt 70.10 Cr, rating CARE BBB-/A3. Segments: castings and power (wind).

| Phase | Verdict | Informational kill switch |
|---|---|---|
| 1 Auditor, CARO | GREEN | Would not stop |
| 2 Notes | YELLOW | Would not stop |
| 3 Financials | YELLOW | Would not stop |
| 4 Risk, MD&A | YELLOW | Would not stop |
| 5 Governance | YELLOW (near red on pay) | Would not stop; want the AGM vote and NRC record before sizing |
| 6 Narrative | YELLOW | Would not stop |
| 7 Strategy | GARP WATCHLIST | n/a |

**Quality score: 6.25 / 10.** Governance 5 (family cash take 29.1% of PBT, pay +47%, NRC chair absent, executives on the Audit Committee and NRC, CSR to a family trust; offset by an independent majority and no pledge). Accounting 7 (agree with B02; hygiene clean, disclosure thin). Balance sheet 6 (D/E 0.68 and ND/EBITDA 2.15x, but 75.8% short term, BBB-, quick ratio 0.60, terms undisclosed). Earnings quality 7 (CFO/EBITDA 81.6%, 7.1% other income share, named cost drivers; one-off labour code charge; margin gain not tied to mix).

**Top 3 strengths.** (1) Operating margin up 277 bp to 16.40% on nameable lines; EBIT cover 3.82x from 2.25x. (2) Clean receivables (0.15% over 6 months, days 80.09) and a clean statutory record. (3) A&D and exports growing from a small base with named customers (GTRE, PLR, HAL award).

**Top 3 red flags.** (1) Promoter-family value flow: 507.91 cash take, CMD pay +51.2%, Rs 18 Cr ceiling, 306.00 and 100.00 unmoved, NRC process. (2) Funding opacity: 75.8% short-term floating debt, no covenants or rates, a solar asset with contradictory disclosure, a Rs 100 Cr plan equal to 97% of equity and absent from the AR. (3) Narrative vs operations: growth is auto-led (90.8% of the increment) while the AR credits diversification; capacity, board size and machine counts conflict.

**Key monitorables for next quarter.**

| Metric | Threshold | Where | Why |
|---|---|---|---|
| Operating EBITDA margin excl. other income | Holds at or above 16.0%; below 15.0% is reversal | Q3 FY27 results P&L (total expenses, depreciation, finance cost) | FY26 step was 13.63% to 16.40% |
| Change in inventories credit and WIP | WIP growth above revenue growth for two quarters = absorption risk | Results P&L and half-year balance sheet; Notes 10, 26 in the next AR | Fact 1; WIP 2,677.48 (+12.1%) |
| Debt and funding mix | D/E above 0.80 or ND/EBITDA above 2.5x; term loan additions against the Rs 100 Cr plan | Half-year balance sheet; sanction announcements | Plan is 97% of equity; rating BBB- |
| A&D share and named programmes | The 11% claim needs filed order values; below 8% weakens the thesis | Investor presentation; Reg 30 order announcements | Fact 2; AR share 5.86%; defence lumpy (5.65, 3.29, 7.90) |
| Receivables over 6 months | Above 1% of receivables | Next AR Note 11.1 | Currently 0.15% |
| Related-party balances | 306.00 and 100.00 unchanged for a third year; family flows above 5% of revenue | Next AR Note 38 | Stuck balances and 4.70% flows |
| Solar commissioning date, cost, generation | Filed with the next results or AR | Q3 FY27 notes, FY27 AR Note 2 | Depreciation step 131.83 to 247.18 |
| AGM 13 Aug 2026 voting on Item 4 | Dissent above 20% signals minority pushback | BSE voting result (not in corpus) | Rs 18 Cr ceiling |

**One-line verdict.** Real margin recovery and clean receivables on an auto-led base, held back by promoter-family cash flow, opaque short-term funding, and an A&D line that is 5.86% of revenue; best fit is GARP transition on WATCHLIST.

---

## NO-CONCALL ANCHOR INDEX FOR STAGE 5 (PDF pages)

| Need | Where |
|---|---|
| MD&A (industry, SWOT, no numeric guidance) | p.76 |
| Year at Glance (solar, two orders, awards) | p.77 |
| Chairman's Communique (priorities, solar, SIDM) | pp.17-18 |
| CFO message (EBITDA, ROCE, D/E, solar benefit) | p.19 |
| A&D Strategic Outlook (civil aviation, no numbers) | p.36 |
| R&D pillars, import substitution | p.37 |
| KPI pages: numbers that define us p.20; KPI text p.21; revenue, PAT, segments p.22; dispatch, export, EBITDA, EPS p.23; ROCE, D/E, defence, aerospace, mix p.24; DPS and capex p.25 | pp.20-25 |
| Capacity (3,060 t graphic and 1,500 t text); infrastructure | p.30; CNC counts p.28, p.31 |
| Product portfolio and end-use list | pp.26-29 |
| Working capital: days Note 39 p.136; ageing Note 11.1 p.121; payables Note 22.1 p.126; inventory Note 10 p.120; cash flow p.110 | as listed |
| Capex and completion: Note 2 and CWIP ageing p.116 ("no projects ... overdue"); Annexure 4 p.74; Cons Note 38 segment assets p.173; capex chart p.25; no capital commitments (Board report item 28, p.58) | as listed |
| Debt: Note 17 pp.124-125; Note 33 pp.130-131; Note 34 p.132; rating p.59 | as listed |
| Segment, industry, geography split | Cons Note 38 pp.172-173 |
| Board report financials and share capital; events after balance sheet date | pp.55-56, 58 |
| Related parties, pay | Note 38 pp.134-135; Annexure 5 p.75; Notice pp.45, 52 |
| Shareholding | MGT-9 pp.66-68; Note 15 p.123 |

---

## DERIVED-NUMBER REGISTER (for the verifier)

Operating EBITDA FY26 3,089.77 = 1,743.49 + 617.97 + 851.90 - 123.59 (16.40% of 18,844.62); FY25 2,249.89 = 838.60 + 672.38 + 812.80 - 73.89 (13.63%). Company EBITDA 3,160.85 = 1,690.98 + 617.97 + 851.90, on total income 18,968.21 = 16.66%. Net debt 6,790.30 = 7,009.87 - 219.57. Industry-split increment 2,284.68 = 18,539.51 - 16,254.83; auto 2,073.47 = 11,835.19 - 9,761.72. Cycle 101.61 = 99.42 + 80.09 - 77.90. Revenue per tonne 18,844.62 / 1,557 = 12.10 lakh; 16,507.37 / 1,372 = 12.03 lakh. Segment asset step 1,715.38 = 1,903.97 - 188.59. Defence export CAGR check (538/159)^(1/7) = 1.190.

```yaml
stage: B03-ardeep
company: "INVPRECQ"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "H1 FY27 cash conversion, 11% A&D share, HAL and MKU programmes and monthly-supply ramp: not in the AR (AR ends 31-Mar-2026). HAL appears only as an award; MKU and monthly supply NOT FOUND IN DOCUMENT"
  - "Rs 100 Cr capex approval, funding mix, timeline and any capital commitment: NOT FOUND IN DOCUMENT (no commitment note; events after balance sheet date 'N.A.')"
  - "Borrowing rates, lenders, maturity buckets beyond one year, covenants; ECL matrix; lease discount rate; capitalised borrowing cost on solar: NOT FOUND IN DOCUMENT"
  - "Solar plant commissioning date, cost, generation and saving: NOT FOUND IN DOCUMENT; AR contradicts itself (Annexure 4 p.74 vs p.77)"
  - "Customer concentration, order book, capacity utilisation (capacity printed as 3,060 t and 1,500 t on the same page, AR p.30), US share of exports: NOT FOUND IN DOCUMENT"
  - "BSE Regulation 17 fine amount and date; AGM 13-Aug-2026 voting result on Item 4: NOT FOUND IN DOCUMENT"
  - "FY2024-25 AR is not a run input; used only to test whether named entities are new; prior-year tone drift not assessed"
  - "Page convention: B02 anchors run one page higher than PDF pages (marker precedes content); this report anchors to PDF page"
flags: []
phase_verdicts: {p1: "GREEN", p2: "YELLOW", p3: "YELLOW", p4: "YELLOW", p5: "YELLOW (near red on pay governance; FLAG-PROMOTER-PRELIM not raised: no pledge or selling)", p6: "YELLOW", p7_best_fit: "GARP (transition) WATCHLIST; no strategy passes on AR evidence alone"}
overall_quality: 6.25
quality_components: {governance: 5, accounting: 7, balance_sheet: 6, earnings: 7}
kill_switch_notes:
  - "p1: would not stop; unmodified opinion, clean standalone CARO, no going concern language"
  - "p2: would not stop; no note shows earnings management, gaps are disclosure and RPT questions"
  - "p3: would not stop; CFO/EBITDA 81.6%, EBIT cover 3.82x"
  - "p4: would not stop; gaps are narrative and disclosure"
  - "p5: would not stop; no pledge, fraud or adverse order; want AGM Item 4 vote and NRC record before sizing"
  - "p6: would not stop; narrative changes how growth is read (auto-led), not whether numbers are real"
triple_pass_verification:
  verified: 15
  discrepancies:
    - {finding_rank: "all", triple_pass_value: "page anchors N (marker read as page end)", ar_value: "PDF page N minus 1 (marker precedes content; confirmed on PDF pages 110, 74, 75)", note_ref: "convention only; note numbers and values all correct"}
    - {finding_rank: "P1-0.1 (not Top 15)", triple_pass_value: "cycle about 134 days (closing-balance cost-proxy method)", ar_value: "101.61 days net on Note 39 basis (99.42 + 80.09 - 77.90); 179.51 gross", note_ref: "Note 39 p.136; method difference, neither equals CARE 133 or screener 245"}
missing_risks:
  - {risk: "External processing dependence 27.4% of revenue vs 'fully integrated' claim", evidence: "Note 30 p.128; AR p.30, p.33"}
  - {risk: "75.8% short-term floating debt, BBB-/A3 rating, no covenant disclosure", evidence: "Note 17 p.124; Note 33 pp.130-131; Board report item 32 p.59"}
  - {risk: "Promoter-related counterparties: unmoved 306.00 capital advance and 100.00 deposit; guarantee commission 84.52", evidence: "Note 38 pp.134-135; Notes 8-9 p.120"}
  - {risk: "Customer concentration unquantified; no major-customer disclosure", evidence: "Cons Note 38 pp.172-173; MD&A p.76"}
  - {risk: "Auto 63.84% and ICE-linked product list; electrification not in threats (INFERENCE)", evidence: "Cons Note 38 p.173; AR p.26; p.76"}
  - {risk: "Solar execution, cost and depreciation step; contradictory commissioning disclosure", evidence: "AR p.18, p.19, p.74, p.77; Cons Note 38 p.173"}
  - {risk: "Single-site exposure (one factory address)", evidence: "CG general information p.89"}
  - {risk: "Labour-code follow-on and gratuity funded ratio 53.8% with no FY26 contribution", evidence: "Note 36 p.132; Note 40 p.137"}
  - {risk: "Key-person and family control; CMD pay +51.2%, Rs 18 Cr ceiling, NRC chair absent", evidence: "Note 38 p.134; Notice p.45, p.52; CG p.82"}
guidance_table:
  - {claim: "4 MW solar 'operational targeted for the second half of FY 2026' (Annexure 4)", number: "4 MW", timeframe: "H2 FY26", credibility: "LOW: period elapsed at report date; p.77 says commissioned; date NOT FOUND"}
  - {claim: "Solar to deliver lower energy costs and improved operating margins (CFO message, p.19)", number: "none", timeframe: "coming years", credibility: "UNSCORABLE: no kWh or Rs figure"}
  - {claim: "Civil aviation 'decisive phase of growth', incremental volume orders (p.36)", number: "none", timeframe: "none", credibility: "LOW specificity: no civil order in Year at Glance"}
  - {claim: "Dividend Rs 1 per share, 100.00 lakh (p.55; Notice p.45)", number: "100.00 lakh", timeframe: "AGM 13-Aug-2026", credibility: "HIGH: payout 8.5% of PAT"}
  - {claim: "India defence exports CAGR about 17% from Rs 159 bn FY23 to Rs 538 bn FY30 (MD&A p.76)", number: "17%", timeframe: "FY23-FY30", credibility: "LOW: own arithmetic on the endpoints gives 19.0%; source unnamed"}
monitorables:
  - {metric: "Operating EBITDA margin excl. other income", threshold: "at or above 16.0%; below 15.0% is reversal", where: "Q3 FY27 results P&L", why: "FY26 step 13.63% to 16.40%"}
  - {metric: "Change in inventories credit and WIP", threshold: "WIP growth above revenue growth for two quarters", where: "results P&L and half-year balance sheet; Notes 10, 26", why: "absorption risk; fact 1"}
  - {metric: "D/E and ND/EBITDA with term-loan additions", threshold: "D/E above 0.80 or ND/EBITDA above 2.5x", where: "half-year balance sheet; sanction announcements", why: "Rs 100 Cr plan is 97% of equity; BBB-"}
  - {metric: "A&D share and named programmes", threshold: "11% claim needs filed order values; below 8% weakens thesis", where: "investor presentation; Reg 30 order announcements", why: "fact 2; FY26 5.86%; defence lumpy 5.65, 3.29, 7.90"}
  - {metric: "Receivables over 6 months", threshold: "above 1% of receivables", where: "next AR Note 11.1", why: "currently 0.15%"}
  - {metric: "Related-party balances and flows", threshold: "306.00 and 100.00 unchanged a third year; flows above 5% of revenue", where: "next AR Note 38", why: "4.70% of revenue today"}
  - {metric: "Solar commissioning date, cost, generation", threshold: "filed in next results or AR", where: "Q3 FY27 notes; FY27 AR Note 2", why: "depreciation step 131.83 to 247.18 lakh"}
  - {metric: "AGM Item 4 voting result", threshold: "dissent above 20%", where: "BSE voting result (not in corpus)", why: "Rs 18 Cr managerial pay ceiling"}
ar_new_downstream_entities:
  - name: "PLR Systems Private Limited (Adani Group and Israel Weapon Industries JV)"
    where_in_ar: "Year at Glance, AR p.77 (contract Jul 2025, precision castings for defence; no order value)"
    entity_type: "customer"
  - name: "Gas Turbine Research Establishment (GTRE), DRDO, Ministry of Defence"
    where_in_ar: "Year at Glance, AR p.77 (supply order Feb 2026, HP turbine super alloy castings; no order value)"
    entity_type: "customer"
  - name: "Adani Defence and Aerospace"
    where_in_ar: "Year at Glance, AR p.77 (appreciation certificate for first lot of LMGs)"
    entity_type: "customer"
  - name: "Festo India"
    where_in_ar: "Year at Glance, AR p.77 (Award of Excellence 2026, DFPD localisation project)"
    entity_type: "customer"
  - name: "Hindustan Aeronautics Limited (HAL)"
    where_in_ar: "Year at Glance AR p.77 (Maharatna CPSE award for indigenisation); AR p.14 (components recognised by HAL)"
    entity_type: "customer or recognising body (relationship and programme not stated)"
  - name: "Mahindra and Mahindra"
    where_in_ar: "Year at Glance AR p.77 (appreciation for timely supply); AR p.11 (2009 award); not found in FY2024-25 AR text"
    entity_type: "customer"
strengths_top3:
  - "Operating EBITDA margin excluding other income up 277 bp to 16.40% on nameable lines (power and fuel -168 bp, materials -134 bp); EBIT cover 3.82x from 2.25x (P&L p.108; Notes 25, 26, 30)"
  - "Clean receivables (over 6 months 0.15%, days 80.09) and clean statutory record: unmodified opinion, no wilful default, pledge nil (Note 11.1 p.121; CARO p.102-104; MGT-9 p.68)"
  - "A&D and exports growing from a small base with named customers: A&D 10.87 Cr from 5.39 Cr, exports +36.3%, GTRE and PLR orders (AR p.24, p.77; Cons Note 38 p.173)"
red_flags_top3:
  - "Promoter-family value flow: cash take 507.91 lakh = 29.1% of pre-exceptional PBT, CMD pay +51.2%, Rs 18 Cr ceiling, 306.00 and 100.00 unmoved, NRC chair absent (Note 38 pp.134-135; Notice p.45; CG p.82)"
  - "Funding opacity: 75.8% short-term floating debt, BBB-, no rates or covenants, solar asset with contradictory disclosure, Rs 100 Cr plan equal to 97% of equity and absent from the AR (Note 17 p.124; p.74, p.77)"
  - "Narrative vs operations: growth auto-led (90.8% of industry-split increment, auto share 60.05% to 63.84%) while the AR credits diversification; capacity 3,060 t vs 1,500 t, board size and machine counts conflict (Cons Note 38 p.173; p.30; p.78)"
best_fit_strategy: "GARP (transition) WATCHLIST"
one_line_verdict: "Real margin recovery and clean receivables on an auto-led base, held back by promoter-family cash flow, opaque short-term funding and an A&D line that is 5.86% of revenue; best fit GARP transition on WATCHLIST."
analyst_note: "Page convention: markers precede content, so AR p.N here is PDF page N; B02 anchors read one higher. All 15 B02 findings verify on number and note. New points: (1) the 277 bp margin gain is explained by power and fuel and materials, not A&D mix; auto gave 90.8% of the revenue increment. (2) Solar likely absorbed about 87% of plant additions (derived from power segment assets) and looks mostly debt funded, so FY26 capex is not A&D capacity. (3) Other borrowing cost and the other-current-assets rise both equal 99.86; guarantee commission 84.52 probably sits inside borrowing cost (INFERENCE). (4) The NRC met once, the chair was absent, CMD and spouse are members. (5) Capacity is printed as 3,060 t and 1,500 t on one page; dispatch is 1,557 t, so utilisation is undecidable. (6) Own cycle on the Note 39 basis is 101.6 days, not 134. The H1 FY27 parts of facts 1 to 3 and the Rs 100 Cr plan are not in the AR."
```
