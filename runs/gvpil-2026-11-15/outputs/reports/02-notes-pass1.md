# Stage 2 Notes Triple Pass: PASS 1 (full extraction)
Company: GE Power India Limited (GVPIL) | Run date: 2026-11-15 | Model: claude-sonnet-5-5
Source: runs/gvpil-2026-11-15/inputs/annual-report/Annual_Report_2026.txt (FY2025-26 AR, 332 pages)

## Conventions

- UNIT: the face of every statement says "All amounts in H million" (the rupee glyph renders as H). That is INR million. Every figure below is INR million ("INR M") unless marked otherwise. Nothing is converted. Stage 10 converts once.
- PAGE: "p.N" is the "[page N]" marker in the text file (PDF page). The printed AR folio is N minus 3 (marker 150 is printed page 147).
- RATING: GREEN = clean, YELLOW = watch, RED = red flag (the three-level scale in the instruction file, written as words).
- ARITHMETIC: figures marked "(calc)" are my sums or ratios from anchored inputs. The company did not print them.
- SCOPE: the standalone notes (Notes 1 to 61, p.136 to p.204) were read in full. The consolidated set (p.218 to p.288) repeats the standalone notes. I read the consolidated statements, Note 7 (JV), Note 39, Notes 47 to 62 and the group table. I did not read every other consolidated note line by line. Differences found are in Section 13.
- PRIOR YEAR: only FY26 and FY25 are in this document. FY24 comparatives are NOT FOUND IN DOCUMENT, so every "3-year trend" below is a 2-year trend.
- Gas, Hydro and Durgapur are "discontinued operations" in the statements. Continuing-operations figures are the headline.

## 0. Load-bearing facts: what the filing shows

### LBF-2 Related party and governance
1. Royalty and trademark fee, FY26: INR M 125.7 in the P&L line (Note 33, p.168). FY25 comparative INR M 121.5 (Note 33, p.168). The related-party table shows a much larger royalty figure: FY26 INR M 305.1 (GE Steam Power Switzerland GmbH) + 110.1 (GE Vernova Infrastructure Technology LLC) + 20.5 (GE Vernova Technology GmbH) = INR M 435.7 (calc) (Note 36, p.180). FY25 INR M 270.0 + 140.3 + 71.2 + 28.9 + 4.1 = INR M 514.5 (calc) (Note 36, p.180).
   - The two sets do not tie (gap INR M 310.0 in FY26, INR M 393.0 in FY25, calc). The notes do not explain the gap. It may be royalty that sits in cost of material and erection services or in discontinued operations. That is an inference. The filing does not say it. Status: UNRECONCILED.
   - The Step-1 lead of "Rs 13.21 cr for FY25" matches neither FY25 figure in the filing (INR M 121.5 in Note 33, INR M 514.5 in Note 36). The lead stands as unverified.
2. Gas sale (Note 47(i), p.194): sold to GE Renewable Energy Technologies Pvt Ltd, a fellow subsidiary under common control, for a lumpsum of INR M 438.6 excluding taxes. Price set on an independent valuer's DCF. Completed 30 Sep 2024. Gain INR M 583.4 booked as an exceptional item in FY25 (Note 47(i), p.194; Note 47(vi), p.198). Note 36 repeats INR M 438.6 as "Slump Sale" for FY25 (p.180).
3. Hydro sale (Note 47(ii), p.194): sold to GE Vernova Hydro Power India Pvt Ltd for INR 1 (one rupee). Completed 31 Mar 2025. Net liability transferred INR M 2,978.9. Independent DCF fair value negative INR M 609.0. Gain INR M 2,369.9 went through the P&L as an exceptional item. INR M 609.0 went to capital reserve (Note 47(ii), p.194; Note 20, p.160). Note 36 shows the price as INR 1.0 (p.180).
4. Durgapur demerger to JSW Energy (Note 47(iii), p.194): Board approved on 18 Sep 2025. Appointed date 1 Jul 2025. Completion expected within 12 months of year end. Presented as held for sale and discontinued from 18 Sep 2025.
   - Consideration is NOT STATED in Note 47. The notes give carrying amounts only. Assets held for sale INR M 344.0. Liabilities INR M 892.7. Net equity INR M (548.7) negative, after "HO current account" INR M 446.9 (Note 47(v)(a), p.195).
   - Outside the notes, the Board's Report states the consideration. JSW issues 10 JSW shares for every 139 GVPIL shares held. The ratio comes from a valuation report and fairness opinion. BSE gave "No Adverse Observations" and NSE a "No Objection" letter, both dated 1 Apr 2026 (Board's Report, p.28). This anchor is outside the notes. How the INR M 548.7 negative net assets will be accounted on demerger is NOT FOUND IN DOCUMENT (notes).
5. Other related-party items to hold (details in Section 2): INR M 4,500.0 inter-corporate deposit (ICD) to LM Wind Power Blades (India) Pvt Ltd; top two customers 38.6% of revenue (Note 35, p.176).

### LBF-3 Earnings quality: one-offs the notes support
FY26 continuing profit before exceptional items is INR M 3,399.0 (P&L, p.132). The notes show these non-recurring or non-operating items inside it:
- Reversal of loss allowance on trade receivables INR M (1,016.6) in Other expenses (Note 33, p.168; cash flow p.133). This is a credit to profit. Tied to the BHEL settlement (Note 53, p.202: INR M 1,050.5 reversed; INR M 3,430.6 received against an agreed INR M 3,400).
- Liabilities and provisions no longer required, written back INR M 240.9 (FY25 INR M 71.6), in Other income (Note 28, p.167).
- Insurance claim INR M 184.2 (FY25 INR M 280.0) in Other income (Note 28, p.167; Notes 51 and 52, p.201 to 202). Notes 51 and 52 say the final payments were INR M 66.1 (Oct 2025, Solapur FGD fire) and INR M 118.2 (FY26, Sipat FGD fire). Both claims are now closed.
- JPVL FGD settlement (Bina and Nigrie): JPVL paid INR M 250 excluding taxes. All project costs to 30 Sep 2025 were already charged to the P&L. The revenue from the settlement was recognised in the quarter (Note 54, p.202). Cost against this revenue is NOT STATED.
- Interest on the ICD to LM Wind Power INR M 199.8 (FY25 INR M 20.4) (Note 28, p.167). Non-operating, tied to a group entity.
- Exceptional item: Labour Code provision. Total INR M 425.7, of which INR M 275.7 is in continuing operations and INR M 150.0 in discontinued (Note 47(iv), p.195). Gratuity past service cost INR M 320.7 in the benefit obligation, INR M 251.7 through P&L (Note 34, p.169 to 170).
- Calc (mine, not company-stated). Profit before exceptional items INR M 3,399.0 + finance costs INR M 219.0 + depreciation INR M 122.8 = INR M 3,740.8. As a share of total income INR M 13,839.1 that is 27.0% (calc). This matches the Step-1 "27.0% reported EBITDA margin". Excluding other income INR M 1,146.4 gives INR M 2,594.4, or 20.4% of revenue INR M 12,692.7. Excluding also the INR M 1,016.6 receivable-loss reversal gives INR M 1,577.8, or 12.4% of revenue (calc). Excluding also the INR M 240.9 write-back gives INR M 1,336.9, or 10.5% (calc). The filing does not compute a "normalised" margin. The 11% in the lead is not in the notes.
- Other income is 33.7% of profit before exceptional items (INR M 1,146.4 / 3,399.0, calc).

### LBF-4 Concentration and cash
1. Top two customers: 38.6% of revenue in FY26; 34.8% in FY25 (Note 35, p.176). Names NOT DISCLOSED. Receivable from them NOT DISCLOSED. The related-party NTPC GE Power Services JV alone billed INR M 1,111.6 in FY26 (8.8% of revenue, calc) against INR M 265.1 in FY25 (Note 36, p.181).
2. CFO FY26: INR M 4,692.5 (FY25 INR M 3,790.4) against profit after tax INR M 2,363.6 (cash flow p.133; P&L p.132).
   - Working capital release: trade receivables decrease INR M 5,136.0 (FY25 INR M 542.5). Offsets: other current liabilities decrease INR M (2,158.3) (FY25 +1,543.1), inventories increase INR M (625.9), non-current provisions decrease INR M (380.1) (cash flow p.133).
   - Receivables fell in step with BHEL cash of INR M 3,430.6 (Note 53, p.202) and a fall in project retention receivables from INR M 8,574.1 to INR M 4,751.7 (Note 13, p.156). Note 53 does not name FGD as the contract behind the BHEL settlement. NOT STATED. The "FGD working-capital release" idea in the lead is plausible but the notes do not confirm the contract link.
   - Customer contract liabilities fell: advances from customers INR M 1,764.0 to INR M 677.9; billing in excess of contract revenue INR M 4,420.4 to INR M 3,399.9 (Note 25, p.164). Together INR M (2,106.6) (calc). The CFO therefore reflects collection of old receivables net of an unwind of customer prepayments.
3. Net cash: cash and equivalents INR M 4,244.6 (Note 14, p.157) + other bank balances INR M 58.5 (Note 15, p.157) + ICD to LM Wind INR M 4,500.0 (Note 16, p.158) = INR M 8,803.1 (calc). Once stage 10 converts, this is the only combination in the notes that gives the Step-1 "net cash 880 cr". Two cautions from the notes:
   - INR M 4,500.0 of it is a demand loan to a fellow subsidiary, not bank cash.
   - INR M 1,607.0 "amount held in trust" (HPGC arbitration, Supreme Court stay) is carried as a liability (Note 24, p.163 to 164). Whether the matching cash sits inside the INR M 4,244.6 is NOT STATED.
   - Debt is nil (Note 43, p.190; Note 46, p.193).

---

## 1. Accounting policies and changes

| # | Finding | Anchor | Rating |
|---|---|---|---|
| 1.1 | Basis: Ind AS; accounts approved 11 May 2026. Operating cycle 12 months, projects business uses contract duration. | Note 2.1.1, p.136 | GREEN |
| 1.2 | Revenue on construction contracts is over time, percentage of completion on cost-to-cost. Management states the method "may involve estimates on the scope of deliveries" and changes in estimates move revenue. The auditor's key audit matter is "estimation of cost to complete". Method is standard for the industry; judgement load is high. | Note 2.12, p.146; Auditor's report KAM, p.206 to 207 | YELLOW |
| 1.3 | Revenue recognised in FY26 from performance obligations satisfied in earlier periods, through contract modifications or estimate changes: INR M +70.3 (FY25 INR M (501.0) reversal). A swing of INR M 571.3 (calc). | Note 27, p.165 | YELLOW |
| 1.4 | Variable consideration and escalation claims are recognised only if the contract allows or the customer has accepted. Liquidated damages provided on management estimate. | Note 2.12, p.146 | GREEN |
| 1.5 | Depreciation: SLM. Management lives: plant and equipment up to 50 years against 15 in Schedule II; office equipment up to 10 against 5; buildings 30 and 60 (same as Schedule II). Net block of plant and equipment is only INR M 93.8, so the P&L effect is small. | Note 2.2, p.139; Note 3, p.150 | YELLOW |
| 1.6 | Intangibles: software 5 years, fully amortised, nil carrying value. | Note 2.3, p.139; Note 5, p.152 to 153 | GREEN |
| 1.7 | Capitalisation: PPE additions INR M 37.9 (FY25 INR M 39.3). Capex outflow INR M 21.3 (cash flow p.133). Capital commitments INR M 0.1 (FY25 INR M 14.3). | Note 3, p.150; Note 38, p.184 | GREEN |
| 1.8 | Impairment of non-financial assets: policy text only, no growth or discount rate disclosed. No impairment charge. Investment in the subsidiary GE Power Boilers Services Ltd impaired in full, INR M 3.4. | Note 2.5, p.140; Note 7, p.153 | GREEN |
| 1.9 | ECL: lifetime ECL on trade receivables on "historical credit loss experience". Stated loss-rate range 7.3% to 13.1%. Allowance INR M 635.9 on gross INR M 8,260.5 = 7.7% (calc), at the bottom of that range. Other financial assets (including the INR M 4,500.0 ICD): "negligible credit risk", no ECL. | Note 43(A)(ii), p.189; Note 13, p.156 | YELLOW |
| 1.10 | Ind AS 116: weighted average incremental borrowing rate 9% (both years). ROU assets INR M 155.4 (FY25 INR M 272.1). Lease liabilities INR M 175.9 (FY25 INR M 288.3). Cash outflow for leases INR M 143.3. Depreciation of ROU INR M 100.9 = 82% of total depreciation INR M 122.8 (calc). | Note 6, p.153; Note 22, p.162; Note 32, p.168 | GREEN |
| 1.11 | Policy for sale or transfer of business under common control (Note 2.20): fair value method chosen by management "in absence of guidance in Ind AS 103". Gain or loss against independent valuer fair value goes to P&L. Difference between fair value and price paid goes to equity. This policy let the INR 1 hydro sale book an INR M 2,369.9 profit with INR M 609.0 to capital reserve. A policy choice, not a mandated treatment. | Note 2.20, p.148; Note 47(ii), p.194 | YELLOW |
| 1.12 | New standards adopted for the first time (effective 1 Apr 2025): Ind AS 21, Ind AS 7 and 107 (supplier finance), Ind AS 1 (classification), Ind AS 12 (Pillar Two). "No impact" on each. Ind AS 19 amendment: no material impact. | Note 2.21(a), p.148 to 149; Note 2.8, p.142 | GREEN |
| 1.13 | Income-Tax Act 2025 effective for years from 1 Apr 2026: "no material impact" per management. | Note 2.21(c), p.149 | GREEN |
| 1.14 | Inventory: lower of cost and NRV; raw materials weighted average; WIP at cost. Packing materials, loose tools and consumables expensed on purchase. | Note 2.7, p.140 to 141 | GREEN |
| 1.15 | Derivatives hold FX hedges; carried at fair value through P&L (no hedge accounting). | Note 2.9(ii)(f), p.145 | GREEN |
| 1.16 | Estimation uncertainty list: ECL, employee benefits, litigation, PPE lives, leases, cost to complete and contract-loss provisions, warranty. Warranty term 18 to 24 months, provision as "certain percentages of cost". | Note 2.1.4, p.137 to 138 | GREEN |
| 1.17 | No change in depreciation lives or revenue policy disclosed for FY26. Depreciation on Durgapur assets stopped from 18 Sep 2025 (Ind AS 105). | Note 47(iii), p.194 | GREEN |

## 2. Related party transactions (Note 36, p.177 to 183)

Relationship: ultimate holding company GE Vernova Inc. Immediate holding company GE Steam Power International B.V., 46,102,083 shares, 68.6% (Note 19, p.159 to 160). Subsidiary GE Power Boilers Services Ltd (100%, no operations; consolidated Note 62, p.287). Joint venture NTPC GE Power Services Pvt Ltd (NGSL), 50%. Fellow subsidiaries: the long list at p.177 to 179 (about 90 entities).

New related-party names versus last year: GE Vernova (Switzerland) GmbH shows FY26 other income INR M 188.6 (FY25 nil) (p.180). GE Vernova T&D India Ltd is on the related-party list (p.179) but no transaction is printed against it. A full new-name test is NOT FOUND IN DOCUMENT, because the FY25 list is not in this filing.

### 2a. Transaction table (INR M; FY26 | FY25 | YoY calc)

| Nature | Party | FY26 | FY25 | YoY | Anchor |
|---|---|---|---|---|---|
| Revenue | GE Power Systems India | 74.2 | 140.8 | -47% | p.180 |
| Revenue | GE Steam Power Switzerland | 40.1 | 91.3 | -56% | p.180 |
| Revenue | GE Energy Switzerland | 31.1 | 82.7 | -62% | p.180 |
| Revenue | GE Steam Power Inc. | 72.9 | 10.5 | +594% | p.180 |
| Revenue | Powerstatic Solutions India | 59.2 | 9.5 | +523% | p.180 |
| Revenue | GE Vernova Global Services | 27.4 | 30.1 | -9% | p.180 |
| Revenue | GE Hydro France | 4.2 | 548.7 | -99% | p.180 |
| Revenue | GE Vernova Operations LLC | nil | 273.6 | n/a | p.180 |
| Revenue | GE Power Services (India) | 3.9 | 58.9 | -93% | p.180 |
| Revenue | Others | 63.8 | 301.8 | -79% | p.180 |
| Revenue | Fellow subsidiaries subtotal (calc) | 376.8 | 1,547.9 | -76% | p.180 |
| Revenue | NTPC GE Power Services (JV) | 1,111.6 | 265.1 | +319% | p.181 |
| Revenue | GE Power Boilers Services (subsidiary) | 0.4 | nil | n/a | p.182 |
| Revenue | Total related-party revenue (calc) | 1,488.8 | 1,813.0 | -18% | |
| Other income | GE Steam Power Switzerland | 106.0 | 82.2 | +29% | p.180 |
| Other income | GE Vernova Technology GmbH | 156.7 | 77.6 | +102% | p.180 |
| Other income | GE Renewable Technologies | 78.7 | 15.6 | +405% | p.180 |
| Other income | GE Vernova (Switzerland) GmbH | 188.6 | nil | n/a | p.180 |
| Other income | Powerstatic Solutions India | 30.6 | 8.7 | +252% | p.180 |
| Other income | Other | 72.5 | 21.2 | +242% | p.180 |
| Other income | NGSL (JV) | 19.0 | 10.5 | +81% | p.181 |
| Other income | Subtotal (calc) | 652.1 | 215.8 | +202% | |
| Royalty and trademark fee | GE Steam Power Switzerland | 305.1 | 270.0 | +13% | p.180 |
| Royalty and trademark fee | GE Vernova Infrastructure Technology LLC | 110.1 | 140.3 | -22% | p.180 |
| Royalty and trademark fee | GE Hydro France | nil | 71.2 | n/a | p.180 |
| Royalty and trademark fee | GE Vernova Technology GmbH | 20.5 | 28.9 | -29% | p.180 |
| Royalty and trademark fee | GE Renewable Technologies | nil | 4.1 | n/a | p.180 |
| Royalty and trademark fee | Subtotal (calc) | 435.7 | 514.5 | -15% | |
| Purchase of materials | Fellow subsidiaries (10 lines, calc) | 699.1 | 1,131.6 | -38% | p.181 |
| Purchase of materials | NGSL (JV) | 225.0 | 60.3 | +273% | p.182 |
| Purchase of services | Fellow subsidiaries (7 lines, calc) | 241.0 | 990.1 | -76% | p.181 |
| Purchase of services | NGSL (JV) | 181.1 | 139.4 | +30% | p.182 |
| Other expenses and reimbursements (payments) | GE Power Systems India, GE Renewable Energy Technologies, Others | 318.4 | 40.3 | +690% | p.180 |
| Provident fund | ACC Babcock Staff Provident Fund | 169.4 | 306.0 | -45% | p.181 |
| Interest expense | LM Wind Power Blades (India) | nil | 117.8 | n/a | p.181 |
| Interest income on ICD | LM Wind Power Blades (India) | 199.8 | 20.4 | +880% | p.181 |
| ICD given | LM Wind Power Blades (India) | 4,500.0 | nil | n/a | p.181 |
| Borrowings repaid | LM Wind Power Blades (India) | nil | 1,019.0 | n/a | p.181 |
| Gratuity payment due to business combination | GE Vernova Hydro Power India | 226.2 | nil | n/a | p.181 |
| Slump sale (Gas) | GE Renewable Energy Technologies | nil | 438.6 | n/a | p.180 |
| Slump sale (Hydro) | GE Vernova Hydro Power India | nil | INR 1 | n/a | p.180 |
| Corporate guarantee | GE Vernova Inc. | 7,977.6 | 28,100.0 | -72% | p.182 |

Subtotals are my sums of the printed lines (calc). Example: the FY25 purchase-of-services subtotal is 107.0 + 260.8 + 106.6 + 115.2 + 69.9 + 161.9 + 168.7 = 990.1.

### 2b. Findings

2.1 RED. ICD to a group company. INR M 4,500.0 lent to LM Wind Power Blades (India) Pvt Ltd under the cash-pool arrangement in place since 22 Nov 2023. Repayable on demand, interest 5.49% to 6.35%, no security stated (Note 16, p.158; Note 36, p.181 and p.183).
- It is 21.4% of total assets INR M 20,995.6 (calc), 106% of cash and equivalents INR M 4,244.6 (calc) and 82.8% of total equity INR M 5,437.7 (calc).
- A year ago the same entity was a lender: INR M 1,019.0 repaid in FY25 and INR M 117.8 interest paid (Note 36, p.181). The company went from net borrower to a INR M 4,500.0 lender to a group entity in one year.
- Note 43 states "undrawn credit limits with cash pool arrangement" of INR M 2,860.0 in both years (Note 43(B)(i), p.190). That reads as a borrowing line, while the company is a net depositor. The cash-pool terms, the counterparty's credit rating and any parent support are NOT FOUND IN DOCUMENT.
- No ECL on it; "high quality assets with negligible credit risk" (Note 43(A)(ii)(a), p.189).

2.2 YELLOW. Royalty and trademark: the P&L line (INR M 125.7) and the related-party table (INR M 435.7) differ (see LBF-2).

2.3 YELLOW. Corporate guarantee INR M 7,977.6 (FY25 INR M 28,100.0) under "Transactions with Ultimate holding company" and "Outstanding balances with ultimate holding company" (Note 36, p.182 to 183). The note does not say who issued it or for whom. Direction: NOT STATED. The balance fell INR M 20,122.4 (calc) with no explanation.

2.4 YELLOW. JV NGSL revenue INR M 1,111.6 is 8.8% of company revenue (calc) and 4.2 times FY25. NGSL receivable INR M 703.0 (FY25 INR M 247.9) and advances received from NGSL INR M 833.0 (FY25 INR M 718.4) (Note 36, p.183). NGSL is a revenue source and a customer-advance source at once.

2.5 YELLOW. Related-party revenue as a share of revenue from operations INR M 12,692.7: 11.7% in FY26 (calc), 17.3% in FY25 on INR M 10,471.0 (calc).

2.6 Non-arm's-length signals: Hydro sold for INR 1 with net liabilities INR M 2,978.9 moved to a fellow subsidiary; Gas sold at an independent DCF price. Management states that related-party transactions are at arm's length (transfer pricing documentation, Note 56, p.203). No transfer-pricing adjustment is disclosed. YELLOW (common-control transfers; independent valuer, but the accounting policy choice lets management book the gain).

2.7 KMP remuneration (INR M): Managing Director Puneet Bhatla 48.4 (FY25 30.9, includes RSU and ESOP exercised); Aashish Ghai, Whole-Time Director and CFO, 10.1 (FY25 5.8); company secretary Kamna Tiwari 5.4 (FY25 5.3); directors' fees 11.5 (FY25 12.3) (Note 36, p.182). The CFO resigned effective 13 May 2026 and the company secretary effective 2 Apr 2026 (Note 36, p.177). YELLOW: two statutory KMP posts were vacant or ending at the date of the accounts. Note 60 (p.204) says the company is "in the process of appointing" a designated company secretary.

2.8 Loans to promoter-family entities: none. The promoter is a corporate parent chain. The ICD in 2.1 is the only loan. Royalty is paid to group entities, not to promoter family.

2.9 Share-based payments: GE Vernova Inc. RSUs and options; expense INR M 14.08, recharged by the ultimate holding company (Note 49, p.200). RSUs outstanding 451; options outstanding 3,901 (Note 49, p.201). No dilution of GVPIL equity. GREEN.

## 3. Contingent liabilities (Note 39, p.185)

| Item (INR M) | 31 Mar 2026 | 31 Mar 2025 | Change | Company assessment |
|---|---|---|---|---|
| Sales tax matters | 2,036.7 | 1,925.4 | +5.8% | "good cases", no provision |
| GST matters | 132.6 | 122.8 | +8.0% | same |
| Income tax matters | 1,105.8 | 1,049.6 | +5.4% | same |
| Amounts not acknowledged as debts | 1,300.8 | 1,176.4 | +10.6% | same |
| Total (calc) | 4,575.9 | 4,274.2 | +7.1% | |

- Total contingent liabilities are 84.2% of net worth INR M 5,437.7 (calc). The largest single item (sales tax INR M 2,036.7) is 37.5% of net worth (calc), above the 10% test. The company says no provision is needed and expects no reimbursement. YELLOW.
- Stage and forum of each case: NOT FOUND IN DOCUMENT. The note gives category totals only. The composition of "amounts not acknowledged as debts" INR M 1,300.8 is NOT DISCLOSED.
- Guarantees for subsidiaries: NOT FOUND IN DOCUMENT in Note 39. Bank guarantees against deposits: INR M 55.5 pledged (Note 15, p.157).
- Provision already booked for contingencies and others: INR M 1,901.3 (FY25 INR M 1,793.0), "mainly probable claims arising out of litigations / disputes pending with various authorities" (Note 26, p.165). Includes the Alstom Transport tax-demand mirror: a recoverable of INR M 110.6 matched by a provision (Note 50, p.201; Note 8, p.154).
- Interest on uncertain tax positions sits in finance costs, "Interest on others" INR M 113.4 (FY25 INR M 116.8) (Note 31, p.168).
- Tax deposits paid under protest INR M 54.9 (FY25 INR M 80.0) (Note 11, p.155).

## 4. Trade receivables (Note 13, p.156 to 157)

| INR M | 31 Mar 2026 | 31 Mar 2025 |
|---|---|---|
| Good, unsecured | 7,624.6 | 11,729.5 |
| Credit impaired | 635.9 | 1,759.7 |
| Gross (calc) | 8,260.5 | 13,489.2 |
| Allowance | (635.9) | (1,759.7) |
| Net | 7,624.6 | 11,729.5 |
| Retention receivables (inside gross) | 4,751.7 | 8,574.1 |

Ageing, FY26 gross INR M 8,260.5: not due 6,067.5 (73.5%); under 6 months 879.0; 6 to 12 months 292.0; 1 to 2 years 554.5; 2 to 3 years 213.7; over 3 years 253.9 (Note 13, p.156).
Ageing, FY25 gross INR M 13,489.2: not due 10,137.2; under 6 months 1,219.1; 6 to 12 months 370.8; 1 to 2 years 799.4; 2 to 3 years 426.4; over 3 years 536.3 (Note 13, p.157).

- Over 6 months, gross: INR M 1,314.1 = 15.9% of gross FY26 (calc); INR M 2,132.9 = 15.8% FY25 (calc). The aged share is flat.
- Of the FY26 over-6-month balance, INR M 976.1 (calc) is classed "good" (no allowance). Credit-impaired over 6 months: 15.9 + 60.5 + 30.9 + 230.4 = INR M 337.7 (calc). The two parts sum to 1,313.8 against the 1,314.1 printed total, a rounding gap of 0.3. The allowance of INR M 635.9 exceeds the impaired over-6-month balance by INR M 298.2 (calc) because it also covers INR M 272.1 not-due and INR M 25.9 under-6-month impaired balances (Note 13, p.156).
- Retention receivables are 57.5% of gross in FY26 (calc) against 63.6% in FY25 (calc). Retention fell INR M 3,822.4 (calc).
- Disputed receivables: nil in FY26; INR M 139.6 impaired over 3 years in FY25 (Note 13, p.157).
- Receivable days (calc, on continuing revenue): net receivables INR M 7,624.6 / revenue INR M 12,692.7 x 365 = 219 days. FY25: INR M 11,729.5 / INR M 10,471.0 x 365 = 409 days. FY24: NOT FOUND IN DOCUMENT. The company's own ratio: receivables turnover 1.31 against 0.86 (Note 44, p.192).
- Allowance movement (Note 43(A)(ii)(b), p.189): opening INR M 1,759.7; reversal INR M (1,123.8); closing INR M 635.9. FY25: opening INR M 1,959.1; charge INR M 271.0; transferred in slump sale INR M (470.4).
   - Cross-check: P&L and cash flow show a reversal of INR M (1,016.6) (Note 33, p.168). Note 53 says INR M 1,050.5 reversed (p.202). Note 43 says INR M 1,123.8. Three numbers for one item. The INR M 107.2 gap between Note 43 and the P&L line (calc) is unexplained. YELLOW.
- Single customer above 10% of receivables: NOT DISCLOSED. Related-party receivables: GE Steam Power Switzerland 216.0, GE Power Systems India 74.8, Powerstatic 25.5, GE Renewable Energy Technologies 22.4, others 26.7; NGSL 703.0 (Note 36, p.182 to 183). Total INR M 1,068.4 (calc) = 14.0% of net receivables.
- ECL adequacy: the BHEL settlement released allowance at once. The remaining allowance INR M 635.9 is 7.7% of gross. Note 53 says the carrying value "will continue to be reviewed" (p.202). GREEN on the improvement, YELLOW on the reversal being a profit item.
- Drafting slip: Note 53 mentions "Consolidated profit and loss" inside the standalone accounts (p.202). No effect on figures.

## 5. Inventory (Note 12, p.156)

| INR M | 31 Mar 2026 | 31 Mar 2025 | Change |
|---|---|---|---|
| Raw materials and components | 901.4 | 408.4 | +120.7% |
| Work in progress | 594.3 | 472.1 | +25.9% |
| Total | 1,495.7 | 880.5 | +69.9% |

- Goods in transit INR M 119.0 (FY25 INR M 2.7).
- No finished goods line (contract business). Inventory grew 69.9% while revenue grew 21.2% (calc).
- Inventory days (calc, on material cost INR M 7,643.0 [7,765.2 - 122.2] for FY26; INR M 7,042.8 [7,048.3 - 5.5] for FY25): 71 days against 46 days. The company's inventory turnover fell to 6.46 from 8.69 (Note 44, p.192).
- Provision for slow-moving INR M 152.9 (FY25 INR M 149.0), 10.2% of inventory (calc). Write-downs for the year: NOT FOUND IN DOCUMENT (only the closing provision is given).
- Raw-material consumption INR M 5,237.2 (FY25 INR M 3,373.5, +55%); project materials and erection services INR M 2,528.0 (FY25 INR M 3,674.8, -31%) (Note 29, p.167). The mix moved from erection services to product materials. YELLOW (stock build outpaces sales; consistent with a ramp in product orders, but the notes do not say why).

## 6. Investments (Notes 7 and 8, p.153 to 154; consolidated Note 7, p.236 to 237)

- Subsidiary GE Power Boilers Services Ltd: 34,000 equity shares of INR 100, 100%, at cost INR M 3.4, fully impaired, carrying value nil (FY25 nil). No operations (Note 7, p.153; Note 62, p.287). Net assets INR M 0.3 (consolidated Note 62, p.287). GREEN.
- JV NTPC GE Power Services Pvt Ltd (NGSL): 3,000,000 shares, 50%, cost INR M 72.0 (acquired 15 Apr 2021 from GE Power Systems GmbH) (Note 7, p.154). Standalone at cost. Consolidated at equity method: INR M 459.3 (FY25 INR M 299.2). Group share of profit INR M 161.7 (FY25 INR M 111.9) (consolidated P&L, p.214; Note 7, p.237).
   - NGSL summary (100% basis): revenue INR M 7,663.4 (FY25 INR M 7,225.3); profit before tax INR M 454.1 (FY25 INR M 301.9); equity INR M 861.1; current liabilities INR M 3,696.0; current assets INR M 4,440.9 (consolidated Note 7, p.237).
   - Group share in equity INR M 430.6 against carrying INR M 459.3. The INR M 28.7 difference is not explained (calc) (consolidated Note 7, p.237). YELLOW (minor).
   - The footnote under Note 7 reads "share of profit of Joint venture amounting to H124.8 million has been recorded for year ended 31 March 2025 (Previous year : H 57.5 million)" (consolidated p.237). That does not match the P&L figures INR M 161.7 and INR M 111.9. It looks like a stale footnote. YELLOW.
   - The roll-forward 299.2 + 161.7 - 1.5 = 459.4 (calc) against 459.3 shows no dividend from NGSL. The INR M 12.0 dividend income in both standalone and consolidated cash flows is not attributed to a source (Note 28, p.167). NOT FOUND IN DOCUMENT.
- ICDs and loans given: INR M 4,500.0 to LM Wind Power Blades (India) Pvt Ltd (see 2.1). No other loans.
- Other investments with unrealised gains or losses: none. Exposure to unlisted equity at fair value nil (Note 43(C)(ii), p.192).
- Other financial assets: security deposits INR M 45.0, recoverable from others INR M 110.6 (Alstom Transport mirror) (Note 8, p.154). Current: derivative assets INR M 173.6 (FY25 INR M 3.0), interest accrued INR M 69.1 (FY25 INR M 6.1), earnest money INR M 12.0 less allowance INR M 5.1 (Note 17, p.158).

## 7. Borrowings (Notes 43, 46; p.190, p.193)

- Borrowings: nil at both year ends. Total debt nil, gearing nil (Note 46, p.193). Interest accrued on group borrowings nil (FY25 INR M 12.3).
- The Durgapur held-for-sale block carries INR M 330.0 of borrowings (Note 47(v)(a), p.195). Lender not named. The discontinued-operations cash flow shows "Borrowings from bank / group companies" INR M 330.0 (Note 47(vii), p.199). NOT STATED whether the lender is GVPIL itself, a group company or a bank. YELLOW.
- Undrawn limits: bank limits INR M 280.0 (FY25 INR M 2,850.0); cash-pool limits INR M 2,860.0 (both years) (Note 43(B)(i), p.190). Bank limits fell by INR M 2,570.0 (calc). Reason NOT FOUND IN DOCUMENT.
- Rate, tenor, security, covenants and 5-year repayment schedule: no borrowings, so nothing to report (NOT FOUND, no instrument exists). No covenant breach disclosed.
- Related-party borrowings: FY25 LM Wind Power borrowings INR M 1,019.0 repaid with INR M 117.8 interest (Note 36, p.181); FY26 nil.
- Lease liabilities contractual maturity: under 1 year INR M 123.4, 1 to 5 years INR M 68.0, total INR M 191.4 undiscounted (Note 22, p.162).
- GREEN on leverage.

## 8. Trade payables (Note 23, p.162 to 163; Note 40, p.185)

| INR M | 31 Mar 2026 | 31 Mar 2025 |
|---|---|---|
| MSME dues | 494.8 | 540.0 |
| Others | 5,034.7 | 4,692.3 |
| Total | 5,529.5 | 5,232.3 |
| Not due | 3,244.3 | 1,783.4 |
| Overdue (calc) | 2,285.2 | 3,448.9 |
| Overdue share (calc) | 41.3% | 65.9% |

- "Others" ageing FY26 (from due date): not due 2,749.5; under 1 year 1,841.5; 1 to 2 years 80.0; 2 to 3 years 107.8; over 3 years 255.9. Over 1 year: INR M 443.7 (calc). FY25 over 1 year: INR M 1,266.6 (calc: 166.5 + 664.1 + 436.0).
- MSME: principal outstanding INR M 494.8, all not due. Interest due on delayed payments INR M 4.2 (FY25 INR M 3.0), accrued and unpaid (Note 40, p.185). Interest paid in the year: nil. GREEN to YELLOW.
- Payable days (calc, on material cost): INR M 5,529.5 / INR M 7,643.0 x 365 = 264 days; FY25 INR M 5,232.3 / INR M 7,042.8 x 365 = 271 days.
- Foreign currency payables of INR M 535.9 (FY25 INR M 1,117.6) have been outstanding more than 6 months. RBI rules need bank or RBI extension approval. The company says it "will obtain approval as and when required" (Note 23 footnote, p.163). It does not say that approval exists for the current balance. YELLOW (regulatory exposure; mitigated by the fall in the balance and by prior approvals "in past").
- Related-party payables FY26: GE Steam Power Switzerland INR M 319.6 (FY25 INR M 796.3), GE Vernova Infrastructure Technology INR M 408.9 (FY25 INR M 308.4), GE Vernova Technology GmbH INR M 86.0 (FY25 INR M 511.9), others per Note 36 (p.182 to 183). Sum of the fellow-subsidiary payable lines printed: INR M 2,075.6 (calc), 37.5% of trade payables. It excludes LM Wind Power INR M 56.4 and NGSL INR M 70.5.
- Supplier finance (Ind AS 7 amendment): "no impact". GREEN.

## 9. Provisions (Notes 21 and 26, p.161, p.164 to 165)

| INR M | 31 Mar 2026 | 31 Mar 2025 |
|---|---|---|
| Non-current: compensated absences | 128.2 | 159.4 |
| Non-current: other employee benefits | nil | 30.6 |
| Non-current: decommissioning | 1.4 | 1.3 |
| Non-current: warranty | 109.2 | 427.8 |
| Non-current total | 238.8 | 619.1 |
| Current: compensated absences | 40.5 | 40.9 |
| Current: other employee benefits | 281.6 | 263.5 |
| Current: warranty | 470.7 | 451.3 |
| Current: loss orders | 223.8 | 216.9 |
| Current: contingencies and others | 1,901.3 | 1,793.0 |
| Current total | 2,917.9 | 2,765.6 |

- Warranty movement (current plus non-current): opening INR M 879.1, net addition/(reversal) INR M (114.2), "liabilities transferred under slump sale" INR M (185.0), closing INR M 579.9. FY25 column: opening INR M 1,189.3, INR M (125.2), INR M (185.0), closing INR M 879.1 (Note 26, p.164).
   - The same INR M (185.0) "slump sale" deduction appears in both years. The slump sales completed on 30 Sep 2024 and 31 Mar 2025, both in FY25. A FY26 slump-sale transfer is not logical. Either the FY26 column repeats the FY25 line (a presentation error) or INR M 185.0 left the provision in FY26 for another reason (for example the Durgapur transfer). The balance sheet ties to the FY26 arithmetic (109.2 + 470.7 = 579.9), so the deduction sits in the totals. The P&L effect is NOT STATED. YELLOW. Pass 2 and 3 to test.
   - Same pattern in loss orders: the line "Less: liabilities transferred under slump sale" INR M (137.7) appears in both years (Note 26, p.165). The FY26 column reads opening 216.9, reversal net of addition 144.6, transfer (137.7), closing 223.8.
- Warranty provision fell 34.0% (calc) from INR M 879.1 to INR M 579.9 while revenue grew 21.2% (calc). Non-current warranty fell INR M 318.6 (calc). Warranty term is 18 to 24 months (Note 2.1.4, p.138). YELLOW.
- Contingencies provision: opening INR M 1,744.1 (FY25), INR M 1,793.0 (FY26 opening), closing INR M 1,901.3; net additions INR M 108.3 (FY26), INR M 48.9 (FY25) (Note 26, p.165). It is 35.0% of total equity and the largest provision (calc).
- Decommissioning: INR M 1.4, restoration of rental premises (Note 21, p.161).
- Litigation cases behind the INR M 1,901.3: NOT FOUND IN DOCUMENT. The note says "mainly for probable claims arising out of litigations / disputes".
- Employee benefits (Note 34, p.169 to 175):
   - Gratuity (funded via LIC): DBO INR M 611.6 (FY25 INR M 431.8); plan assets INR M 668.1 (FY25 INR M 752.2); net asset INR M 56.5 (FY25 INR M 211.5). Asset ceiling nil in FY26 (INR M 108.9 in FY25). Past service cost INR M 320.7 in the DBO roll (INR M 251.7 through P&L) from the Code on Social Security 2020, effective 21 Nov 2025 (p.169 to 171). Expected contribution next year INR M 80 (p.171).
   - Assumptions FY26: discount rate 7.05% (FY25 6.80%); attrition 5.58% (FY25 8.09%); salary growth up to 8.25%, then 8.2% (FY25 up to 8.5%, then 8.0%). The fall in attrition from 8.09% to 5.58% moves the obligation. Sensitivity: -3.30% for +50 bps in discount rate, +3.50% for -50 bps (p.172). YELLOW only because attrition fell by a third in a year when staff left with the sold businesses; the notes do not say why.
   - Disaggregation of plan assets shows INR M 677.1 (p.171) against INR M 668.1 in the roll-forward (p.170). A INR M 9.0 gap (calc). YELLOW (minor).
   - Provident fund trust: DBO INR M 2,180.6 (FY25 INR M 3,330.6); assets INR M 2,356.5 (FY25 INR M 3,601.5); surplus INR M 175.9 not recognised (asset ceiling) (p.173 to 174). Liabilities assumed or settled INR M (1,218.6) (FY25 INR M (509.5)). The company surrendered its EPFO exemption; from 1 Apr 2026 it becomes an unexempted establishment; transfer of records and accumulations is still to be done (Note 59, p.204). Trust asset mix: government debt INR M 927.4, other debt INR M 883.7, equity INR M 401.5, others INR M 143.9 (p.174). Risk: a shortfall on transfer. The trust shows a surplus at year end. YELLOW.
   - Defined contribution: employer provident fund INR M 31.4, superannuation INR M 17.8 (p.175).
- Onerous contracts: loss-order provision INR M 223.8 (Note 26, p.165). The deferred-tax note lists "provision for loss orders" INR M 6.5 as a tax-effected figure (Note 9, p.154).

## 10. Deferred tax and tax (Notes 9, 10, 48; p.154 to 155, p.199 to 200)

- Deferred tax asset recognised: nil in both years. Gross DTAs INR M 1,895.2 (FY25 INR M 2,430.5) less DTL INR M 88.4 (FY25 INR M 152.1) = INR M 1,806.8 (calc). The table shows "Unrecognised deferred tax assets" INR M (1,983.6) (FY25 INR M (2,582.6)) (Note 9, p.154 to 155).
   - Components: brought-forward losses INR M 1,147.4 (FY25 INR M 1,399.8), loss allowance on credit-impaired assets INR M 270.8 (FY25 INR M 507.9), other timing items INR M 477.0 (FY25 INR M 522.8).
   - Reason for non-recognition: Board considered "recent financial performance, delay in order backlog execution and also changing business demands such as a lower order intake than expected"; "absence of reasonable certainty of realization" (Note 9 footnote, p.155). This is Board language about weak order intake in a year with an INR M 3,061.0 continuing profit. YELLOW (the DTA stance is conservative and conflicts with the earnings optics).
   - The note says brought-forward losses are "to be carried forward for more than 5 years". Expiry schedule: NOT FOUND IN DOCUMENT.
- Tax rate reconciliation (continuing plus discontinued, profit before tax INR M 2,425.3): statutory 25.168% gives INR M 610.4; change in unrecognised DTA INR M (599.0); permanent items INR M 36.3; others INR M 14.0; total INR M 61.7 (Note 48, p.200). Effective rate 2.5% (calc). Continuing operations current tax INR M 62.3 on profit before tax INR M 3,123.3 = 2.0% (calc) (P&L p.132). Low cash tax comes from the unrecognised loss pool. The INR M 599.0 reduction in the unrecognised pool reflects loss use or lapse; the note does not say which.
- Tax assets (advance tax and TDS, net of provision INR M 6,216.3): INR M 679.4 (FY25 INR M 493.5) (Note 10, p.155). Tax paid in cash flow INR M (389.7) (FY25 INR M +244.8, a refund) (p.133).
- FY25 comparative: effect of change in tax rate INR M (235.1) (Note 48, p.200).
- MAT credit: NOT FOUND IN DOCUMENT.

## 11. Revenue details (Notes 27 and 35; p.165 to 166, p.176)

| INR M | FY26 | FY25 | YoY (calc) |
|---|---|---|---|
| Construction contracts (over time) | 7,640.3 | 6,215.2 | +22.9% |
| Sale of products (point in time) | 4,911.7 | 4,130.8 | +18.9% |
| Sale of services | 109.5 | 111.7 | -2.0% |
| Other operating income | 31.2 | 13.3 | +134.6% |
| Revenue from operations | 12,692.7 | 10,471.0 | +21.2% |

- Geography: India INR M 12,343.2 (97.2%), outside India INR M 349.5 (2.8%) (FY25 INR M 10,109.3 and INR M 361.7) (Note 35, p.176).
- Single segment: "Power generation equipment and related services". No segment profit disclosed (Note 35, p.176). Services versus projects margin split: NOT FOUND IN DOCUMENT. "Sale of services" is only INR M 109.5, so the core-services business in the Step-1 brief is mostly booked inside construction contracts and product sales; the notes do not split it.
- Remaining performance obligation (RPO): INR M 16,278 at 31 Mar 2026 against INR M 26,623 at 31 Mar 2025, down 38.9% (calc). Cover: 1.28 times FY26 revenue (calc). Conversion timing: "not practical to define" (Note 27, p.166). Whether RPO includes Durgapur or intra-group orders: NOT STATED. YELLOW to RED: the order base shrank by about two-fifths in one year while revenue rose 21%.
- Contract balances (INR M): contract revenue in excess of billing (asset) 343.4 (FY25 157.7); advances from customers 677.9 (FY25 1,764.0); billing in excess of revenue (liability) 3,399.9 (FY25 4,420.4); net contract liability 3,056.5 (FY25 4,262.7) (Note 27, p.166; Note 18, p.158; Note 25, p.164).
- Revenue recognised from the opening contract-liability balance: INR M 2,445.5 (FY25 INR M 1,520.8) (Note 25 footnote, p.164).
- Para 105 netting: INR M 890.8 of revenue-in-excess-of-billing was netted against customer advances (FY25 INR M 336.1) (Note 25, p.164). Gross contract assets are understated by this amount.
- Top customer revenue: top two customers 38.6% (FY25 34.8%) (Note 35, p.176). Names and individual shares NOT DISCLOSED.
- Revenue from related parties INR M 1,488.8 = 11.7% (Section 2).

## 12. Other critical notes

### 12.1 Exceptional items and discontinued operations (Note 47, p.194 to 199)
- FY26 continuing: exceptional item INR M (275.7) for the Labour Codes. Notified 21 Nov 2025; management "estimated the financial implications" on draft rules and FAQs. Final rules are pending; further provision is possible (p.195). Recurrence: rule-driven, "non-recurring" per management. YELLOW (open ended).
- FY26 discontinued (Durgapur): loss before exceptional INR M (548.0), exceptional INR M (150.0) Labour Codes, net loss INR M (697.4) (Note 47(vi), p.198). Gross revenue INR M 247.0, all internal and eliminated. Costs: employee INR M 374.4, other INR M 153.7, materials INR M 15.1.
   - Whether continuing cost of materials INR M 7,765.2 includes the INR M 247.0 internal purchase from Durgapur is NOT STATED. If it does, the continuing margin carries a cost that leaves with the demerger. If the elimination also removed the purchase, it does not. Question for management.
- FY25: gain on sale of Gas INR M 583.4 and Hydro INR M 2,369.9 (INR M 2,953.3); tax on the gain INR M 326.3. Discontinued net profit FY25 INR M 1,693.5 (Note 47(vi), p.198).
- Durgapur balance sheet at 31 Mar 2026: assets INR M 344.0 (PPE 119.9, CWIP 60.2, other assets 155.6, inventories 4.4); liabilities INR M 892.7 (borrowings 330.0, trade payables 277.3, provisions 280.3, other 5.1); equity INR M (995.6) plus HO current account INR M 446.9, total (548.7) (Note 47(v)(a), p.195). The divisional equity is negative; the demerger removes a net liability.
- Gas business at 30 Sep 2024: total assets INR M 489.7, liabilities INR M 634.5, equity INR M (144.8) (Note 47(v)(b), p.196). Hydro at 31 Mar 2025: assets INR M 5,766.2; liabilities INR M 8,745.0; equity INR M (2,978.9) (Note 47(v)(c), p.197).
- Cash flow of discontinued: operating INR M (366.6), investing INR M (65.0), financing INR M 431.6 (net nil) (Note 47(vii), p.198 to 199). Group funding for Durgapur flows through "movement in owner's investment (pursuant to Scheme)" INR M (349.5) in the main cash flow (p.134).

### 12.2 Goodwill and impairment
No goodwill. No impairment test assumptions disclosed. GREEN.

### 12.3 Foreign currency exposure and hedging (Note 43(C), p.191 to 192)
- Unhedged: receivables USD 319.1, EUR 22.8; bank "other" 115.3; payables EUR 80.5, other 175.3 (INR M). FY25 receivables USD 312.1, EUR 284.9.
- Forward contracts to buy foreign currency: USD 674.1, EUR 1,151.0, other 939.7 (FY25 624.0, 926.1, 489.7); sell forwards nil (FY25 USD 600.4).
- 10% sensitivity on profit after tax: USD +/-23.88, EUR +/-7.73, other +/-21.75 (INR M).
- The cash flow adds back an unrealised FX loss of INR M 492.2 (FY25 gain INR M (110.8)) (p.133). Note 33 shows a net FX loss of only INR M 42.5 after an INR M 173.6 mark-to-market gain on derivatives (p.168). The INR M 492.2 add-back is not matched in the notes. NOT FOUND IN DOCUMENT as a reconciliation. YELLOW.

### 12.4 Segment reporting
See Section 11. One segment. GREEN on rules, YELLOW on opacity.

### 12.5 EPS
Basic equals diluted: continuing INR 45.53 (FY25 INR 3.34), discontinued INR (10.37) (FY25 INR 25.20), total INR 35.16 (FY25 INR 28.54). Weighted shares 67,227,471 (Note 41, p.186). No dilutive instruments. GREEN.

### 12.6 Events after balance sheet date
- Dividend: Board recommended a final INR 7 per share, INR M 470.6, on 11 May 2026 (Note 61, p.204). The equity statements for FY26 and FY25 show no dividend line (p.135).
- CFO resignation effective 13 May 2026 (Note 36, p.177); company secretary resignation effective 2 Apr 2026.
- BSE and NSE letters for the JSW scheme dated 1 Apr 2026 (Board's Report p.28, outside the notes).
- There is no separate subsequent-events note. No event is stated to change the figures.

### 12.7 CSR
Not applicable (net profit test not met). Voluntary spend INR M 0.8 (FY25 INR M 0.6) (Note 37, p.184). GREEN.

### 12.8 ESOP and share-based payments
GE Vernova Inc. plans; expense INR M 14.08; no GVPIL dilution (Note 49, p.200 to 201). GREEN.

### 12.9 Share capital and equity
- 67,227,471 shares of INR 10, INR M 672.3, unchanged. Immediate holding company 68.6% (Note 19, p.159 to 160).
- Authorised preference capital INR M 4,050.0 (40.5 million shares of INR 100), none issued (Note 19, p.159).
- Equity bridge FY26: other equity opening INR M 2,267.5; continuing profit INR M 3,061.0; discontinued loss INR M (697.4); OCI INR M 134.3; closing INR M 4,765.4 (Statement of changes in equity, p.135). Direct credit to reserves bypassing P&L: capital reserve INR M 609.0 (hydro sale, FY25) and OCI remeasurements (Note 20, p.160).

### 12.10 Other disclosures worth keeping
- Title deeds: Shahabad (Kalaburagi, Karnataka) freehold land and building, gross INR M 108.7, in the name of ACC Vickers Babcock Ltd / Alstom Projects India Ltd, held since 1 Aug 1974. The Tahsildar asked for records of rights 1953 to 1998 in Jul 2025; documents submitted Oct 2025; no update (Note 3, p.151). YELLOW (small, long-running).
- Insurance claims: Solapur FGD fire loss INR M 997.5, insurer paid INR M 646.1, salvage INR M 14.0 (Note 51, p.201). Sipat FGD fire loss INR M 694, surveyor assessed INR M 355, insurer paid INR M 318.2 (Note 52, p.202). Booked costs not recovered: about INR M 337.4 on Solapur (997.5 - 646.1 - 14.0, calc) and INR M 339.0 on Sipat (694 - 355, calc).
- Amount held in trust INR M 1,607.0: HPGC contracts with Alstom, terminated 17 Apr 2000; arbitral award May 2010 for the Alstom entities, upheld by the district court and High Court; HPGC special leave petition in the Supreme Court pending since 2016; interim stay conditional on payment of INR M 1,000 by HPGC; interest earned INR M 607.0 (FY25 INR M 553.3). Held as a liability under "other current financial liabilities". Interest cost on it INR M 53.7 (Note 24 footnote, p.163 to 164; Note 31, p.168). YELLOW: a contingent gain or loss of INR M 1,607.0 that depends on the Supreme Court. The company's share versus the other Alstom entity: NOT FOUND IN DOCUMENT.
- Audit trail: SAP audit trail on all year; the payroll vendor is covered by an independent SOC report; the employee-database vendor's audit trail is not covered by an independent SOC report (Note 57, p.203). YELLOW (minor).
- IEPF: INR M 0.91 deposited late on 16 Oct 2024 (due 29 Sep 2024) (Note 55, p.202).
- Transfer pricing documentation maintained (Note 56, p.203). Note 58 (no intermediary funds) GREEN.
- Financial ratios (Note 44, p.192 to 193), FY26 against FY25: current ratio 1.34 (1.14); debt service coverage 28.22 (2.64); return on equity 0.73 (0.13); inventory turnover 6.46 (8.69); receivables turnover 1.31 (0.86); payables turnover 1.58 (1.50); net capital turnover 2.62 (4.63); net profit ratio 0.24 (0.02); ROCE 0.69 (0.20). Reasons given only for movements above 25%, all "due to increase in profit after tax from continuing operations" or working capital.
- Standalone auditor's report, CARO 2020 clause (xvii): "had incurred cash losses amounting to Rs. 824.15 millions in the immediately preceding financial year" (auditor's report p.130, outside the notes). Clause (xix): no material uncertainty about meeting liabilities for a year (p.130 to 131).

## 13. Consolidated set: differences found

- Consolidated revenue INR M 12,693.9 against standalone INR M 12,692.7 (INR M 1.2 gap, subsidiary) (p.214 vs p.132). Other expenses INR M 616.6 against INR M 616.2.
- Share of profit of JV INR M 161.7 (FY25 INR M 111.9) is added below operating profit: continuing profit INR M 3,223.5 against INR M 3,061.0 standalone. Total profit INR M 2,526.1 (FY25 INR M 2,030.0). Consolidated EPS INR 37.58 against INR 35.16 standalone (p.214).
- Consolidated other equity INR M 5,153.1 (INR M 4,765.4 standalone). Consolidated net assets INR M 5,825.5; parent 93% (INR M 5,437.8), JV 7% (INR M 387.3), subsidiary INR M 0.3 (Note 62, p.287).
- CFO consolidated INR M 4,693.6 (standalone INR M 4,692.5). Cash INR M 4,245.7 (standalone INR M 4,244.6) (p.215 to 216). The INR M 1.1 gap is the subsidiary's cash.
- Consolidated Notes 39, 47, 48, 49 to 61 repeat the standalone numbers (checked: p.282 to 287). Tax reconciliation: profit before tax INR M 2,587.8; share of JV profit INR M (40.9) in the reconciliation (Note 48, p.283).

---

## PASS 1 SUMMARY: top 10 findings by investor importance

| Rank | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | INR M 4,500.0 ICD to LM Wind Power Blades (India), a fellow subsidiary. Repayable on demand, 5.49% to 6.35%, no ECL. It equals 21.4% of total assets and 106% of cash. A year ago the same entity was a lender to GVPIL. | Note 16, p.158; Note 36, p.181, p.183; Note 43, p.189 | RED |
| 2 | FY26 profit before exceptional items INR M 3,399.0 carries an INR M 1,016.6 receivable-loss reversal (BHEL settlement: INR M 3,430.6 cash against INR M 3,400 agreed) and INR M 240.9 of write-backs. Without those two, profit falls to INR M 2,141.5 (calc); EBITDA excluding other income and the reversal is 12.4% of revenue (calc). | Notes 33, 28, 53, p.167 to 168, p.202 | RED |
| 3 | CFO INR M 4,692.5 is a working-capital release: receivables INR M +5,136.0 against an INR M (2,106.6) fall in customer advances and billing in excess. Retention receivables fell INR M 3,822.4. A settlement-led collection cannot repeat at that scale. | Cash flow p.133; Note 13, p.156; Note 25, p.164 | RED |
| 4 | Remaining performance obligation INR M 16,278 against INR M 26,623, down 38.9%, while revenue grew 21.2%. Cover 1.28 times revenue. | Note 27, p.166 | RED |
| 5 | Royalty and trademark fee: P&L INR M 125.7 against related-party table INR M 435.7. The INR M 310.0 gap is unexplained. FY25 gap INR M 393.0. The Step-1 lead of Rs 13.21 cr FY25 matches neither figure. | Note 33, p.168; Note 36, p.180 | YELLOW |
| 6 | Hydro business sold to a fellow subsidiary for INR 1 with net liabilities INR M 2,978.9; a policy choice (Note 2.20) booked an INR M 2,369.9 gain and INR M 609.0 capital reserve. Durgapur demerger to JSW Energy: share swap 10 for 139 per the Board's Report (not in the notes); the undertaking carries net liabilities INR M 548.7; demerger accounting not stated. | Notes 2.20, 47(ii), 47(iii), 47(v), p.148, p.194 to 195; Board's Report p.28 | YELLOW |
| 7 | Contingent liabilities INR M 4,575.9 = 84.2% of net worth; the sales-tax item alone INR M 2,036.7 = 37.5% of net worth; no provision. Provision for contingencies and others already INR M 1,901.3. | Note 39, p.185; Note 26, p.165 | YELLOW |
| 8 | Customer concentration: top two customers 38.6% of revenue (34.8% in FY25). NGSL (JV) alone INR M 1,111.6 (8.8%), up 4.2 times. Names not disclosed. | Note 35, p.176; Note 36, p.181 | YELLOW |
| 9 | Provision movements carry an INR M (185.0) warranty and an INR M (137.7) loss-order deduction labelled "slump sale" in FY26, though the slump sales closed in FY25. Warranty provision fell 34.0%. The allowance reversal is quoted three ways (1,016.6 / 1,050.5 / 1,123.8). | Note 26, p.164 to 165; Notes 33, 43, 53 | YELLOW |
| 10 | Inventory up 69.9% against revenue up 21.2% (71 days against 46 days, calc). Raw materials up 120.7%. Overdue payables fell from 65.9% to 41.3% of payables. The Step-1 net cash of 880 cr is only reached by counting the ICD; INR M 1,607.0 held in trust (a liability) is not netted. | Notes 12, 23, 16, 24; p.156, p.162 to 164 | YELLOW |

Other items to carry: DTA not recognised (INR M 1,983.6 unrecognised; Board cites "lower order intake than expected"); Labour Codes provision open ended (INR M 425.7 so far); CFO and company secretary posts vacant; PF trust exemption surrendered from 1 Apr 2026; FX payables over 6 months INR M 535.9 without stated RBI approval.

Gaps recorded: no stage and forum for contingent liabilities; no customer names; no FY24 comparatives; no impairment inputs; no covenant data (no debt); MAT credit and loss expiry schedule not disclosed; Durgapur consideration not in the notes.
