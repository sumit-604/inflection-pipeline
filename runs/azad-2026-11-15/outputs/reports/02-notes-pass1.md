# Stage 2, Notes to Financial Statements, PASS 1 (full extraction)
Company: AZAD (Azad Engineering Ltd). Run date: 2026-11-15. Model: claude-sonnet-5-5.

Source: Annual_Report_2026.pdf (FY2025-26), consolidated notes, Note 1 to Note 46, [page 196] to [page 252] in the PDF page markers. The printed folio is the PDF page minus 3. Prior year is Annual_Report_2025 (comparison only). Standalone statements (pp.121-180) were read only where they test a consolidated figure.
UNIT: INR million (Rs Mn) throughout, as printed on the face of every statement ("All amounts are C in millions", [page 191]). No figure is converted. "Cr" is not used. 100 Mn = 10 Cr, left for stage 10.
Notation: (Note N, p.X) = Note number, PDF page. "[calc]" = my arithmetic on printed figures. "[INFERENCE]" = my reading, not filed text. Ratings: GREEN clean, YELLOW watch, RED red flag.
B00 input_gaps carried: QIP placement document not collected (Note 40 is read against the AR only); the five screener formula sheets are absent (no effect on notes); research/ empty (no effect). No gap blocks this pass.

## LOAD-BEARING FACTS, checked first

### LB1. Cash conversion: operating cash flow, receivables, inventory, WC days, factoring
- Consolidated operating cash flow FY26: (1,189.66) Rs Mn; FY25: 536.67 (Cash flow statement, p.193). RED. OCF turned negative on 31.8% revenue growth [calc].
- Build: operating profit before WC 2,332.96; WC changes net (3,034.45) [calc]: trade receivables (736.91), inventories (1,398.12), other assets (739.76), other financial liabilities (230.00), trade payables +61.05, other (+8.33 net) (p.193). Cash used in operations (701.49); tax paid (488.17).
- Balance sheet: trade receivables 3,116.61 vs 2,234.80 (+39.5%) (Note 8, p.220); inventories 3,291.13 vs 1,893.01 (+73.9%) (Note 7, p.219); revenue +31.8% (P&L, p.192). Inventory grew 2.3x as fast as revenue [calc].
- Working-capital days, revenue basis [calc] (days on COGS, the company definition and the 344 tripwire definition are NOT FOUND IN DOCUMENT; this AR does not print working-capital days):
  | Item | FY26 | FY25 |
  | Receivable days (net, on revenue) | 188.7 | 178.4 |
  | Inventory days (on revenue) | 199.2 | 151.1 |
  | Payable days (on revenue) | 51.6 | 63.9 |
  | Net cycle (rec + inv - pay) | 336.3 | 265.6 |
  The 336 day figure on a revenue basis is not the 344 tripwire and is not comparable until the tripwire definition is supplied (company memory cites 344; AR does not). Direction is a deterioration of about 71 days in one year [calc].
- Factoring / bill discounting / supply-chain finance: grep of the whole AR text for factoring, bill discounting, recourse, non-recourse and supply chain finance found nothing. Note 2P(2) says "The Group does not have any supplier finance arrangements during the reporting period" (p.213). That covers supplier-side programmes only. No disclosure of receivable discounting, derecognition of receivables, or recourse terms: NOT FOUND IN DOCUMENT. Policy only: financial assets derecognised when risks and rewards transfer (Note 2C(iv), p.202). Consequence: the FY26 negative OCF is not helped by any disclosed factoring; the notes cannot rule out undisclosed discounting. Management's bill-discounting WC plan (company memory) is not visible in these notes. YELLOW (silence, not evidence).
- OCF contamination [INFERENCE, from tie-out]: other financial liabilities fell 177.43 (Note 18, p.228) while capital creditors rose 63.31 (57.17 to 120.48); IPO expense payable (44.78 to nil) and QIB expense payable (136.03 to 3.00) fell 177.81 together. The OCF line shows (230.00) for other financial liabilities (p.193) and financing shows no QIP cost in FY26 (p.194). So an amount of the order of 155 to 178 of equity issue-cost payments appears to sit in operating cash flow [INFERENCE; the range is 177.81 less the 22.42 reversal credited to securities premium, Note 12(i), p.224]. Adding it back would leave OCF near (1,010) to (1,035). Still negative. The sign does not change.
- Government balances (GST/duty) in other current assets 1,102.51 vs 554.83 (+98.7%) (Note 10, p.222). Composition (GST refund vs input credit vs customs) NOT FOUND IN DOCUMENT. This is 15.7 percent of the total WC drain on the "other assets" line (739.76) alone being 24% of the drain [calc: 739.76/3,034.45 = 24.4%].
- Verdict on LB1: cash conversion FAILS in FY26 on the filed numbers (OCF negative, WC cycle longer). It is not rescued by factoring. FLAG-CASH.

### LB2. Revenue growth guidance over 25% vs delivered
- Guidance is not in the notes: NOT FOUND IN DOCUMENT (notes carry no guidance). Delivered FY26: consolidated revenue 6,029.75 vs 4,573.54 = +31.8% [calc] (P&L, p.192); standalone 5,903.75 vs 4,529.28 = +30.3% [calc] (standalone P&L p.122; MD&A shows 30.3%). FY26 delivered clears 25%.
- Mix (Note 21/37, pp.229, 248): sale of products 4,751.51 vs 3,742.77 (+26.9% [calc]); sale of services (job work) 1,193.62 vs 695.17 (+71.7% [calc]); scrap sales 55.54 vs 99.64 (-44.3%); export incentives 29.08 vs 35.96. Services are 19.8% of revenue vs 15.2% [calc]. Product growth, the part that is not job work, grew about 27%. Whether job-work growth carries lower margin or lower working capital is NOT FOUND IN DOCUMENT.
- Geography: outside India 5,495.70 (91.1% [calc]) vs 4,185.42; India 534.05 (Note 31 segment, p.237; Note 37, p.248). Customer-country split NOT FOUND IN DOCUMENT.
- Single segment (Note 31, p.236). End-market split (energy, oil and gas, aerospace) NOT FOUND IN DOCUMENT in notes.
- Other income 456.54 vs 105.91 includes FX gain 214.01 and interest 228.49 (Note 22, p.229). Other income is 24.4% of PBT 1,873.06 [calc]. PBT less other income = 1,416.52 vs 1,134.35 (+24.9% [calc]). Core profit growth is below revenue growth. YELLOW.

### LB3. Customer concentration
- Ind AS 108 major-customer note (Note 31(c), p.237): "revenue from 2 customers (March 31, 2025: 1) which amounts to 10% or more". Rupee amounts are not given there.
- Amounts are in Note 34 A(ii) (p.242), consolidated: top customer 1,123.97 (FY25: 648.81); "top 5 customers" 1,711.10 (FY25: 1,703.84).
- Share [calc]: top-1 = 1,123.97 / 6,029.75 = 18.6% (FY25 648.81 / 4,573.54 = 14.2%). Standalone basis 1,123.97 / 5,903.75 = 19.0%; Standalone FY25 631.30/4,529.28 = 13.9%.
- Top-5 definition conflict. The standalone note labels the 1,711.10 line "top 5 customers (other than above customer)" (standalone Note on credit risk, Annual_Report_2026 line-level p.~164, label "other than above customer"). The consolidated label drops the qualifier. Proof it excludes the top customer: two customers are at least 10% (>= 603), so top-2 >= 1,726.95 > 1,711.10, so 1,711.10 cannot include the top customer [calc/INFERENCE]. FY25 cross-check: 648.81 + 1,703.84 = 2,352.65, which equals the FY25 AR's consolidated "top 5" figure of 2,352.65 (Annual_Report_2025, consolidated credit-risk note). So the FY26 AR re-split the prior year into top-1 plus others.
- Top-5 (incl. top-1) therefore = 1,123.97 + 1,711.10 = 2,835.07 = 47.0% of revenue (FY25: 2,352.65 = 51.4%) [calc, INFERENCE on label]. Whether the "others" line holds four or five names is NOT FOUND IN DOCUMENT, so true top-5 is 47.0% if four, a little higher if five.
- Against tripwire (top-1 about 20%, top-5 65%): top-1 at 18.6% (19.0% standalone) is 1.4 points under. It rose 4.4 points in one year. Top-5 at about 47.0% is well under 65%. Concentration is rising at the top and falling in the tail. Receivables: customer-wise receivable concentration NOT FOUND IN DOCUMENT. RATING YELLOW.
- Restatement flag: the FY25 comparative top-5 was relabelled between ARs (see Restatements below).

### LB4. QIP deployment and capex commissioning
- QIP: 5,468,750 shares at Rs 1,280 = 7,000.00 raised in Q4 FY25 (Note 40, p.249). Use of proceeds to 31 Mar 2026:
  | Object | To be used | Used | Unused |
  | Capex | 5,250.00 | 3,686.65 | 1,563.35 |
  | General corporate purposes | 1,562.10 | 1,562.10 | nil |
  | Issue expenses | 187.90 | 153.98 | 33.92 |
  | Total | 7,000.00 | 5,402.73 | 1,597.27 |
  Capex object 70.2% used [calc]. GCP is 100% used, 22.3% of issue [calc]. Unused 1,597.27 sits in bank deposits; earmarked balances 1,599.99 (Note 9(b), p.221). Tie within 2.72, plausibly interest. GREEN on parking; no deviation disclosed in the note.
- Footnote: 31.22 of QIP expenses (with GST) paid from the company's own account, not yet reimbursed from monitoring account (Note 40, p.249). YELLOW (small).
- Prior year: only 436.72 used to 31 Mar 2025 and 6,375.38 unused (Annual_Report_2025 Note 40). FY26 drawdown of QIP money ≈ 4,778 (6,375.38 - 1,597.27) [calc]. Note 40 does not say when the remaining 1,563.35 capex is due. NOT FOUND IN DOCUMENT.
- Issue-cost mismatch: issue expenses used 153.98 + 31.22 = 185.20 per Note 40; equity charge for share issue expenses is 159.33 in FY25 less a 22.42 credit in FY26 = 136.91 net [calc] (Note 12(i), p.224). The two do not match (diff 48.29 [calc]). GST or accrual basis could explain it; not stated. YELLOW.
- CWIP (Note 4, pp.217-218): 2,566.82 vs 797.80 (3.2x). Additions 3,347.49; capitalised (1,578.47); opening 797.80.
  | Ageing 31 Mar 2026 | <1y | 1-2y | 2-3y | >3y | Total |
  | Projects in progress | 2,223.71 | 251.46 | 2.52 | 89.13 | 2,566.82 |
  Prior: <1y 682.47, 1-2y 19.63, 2-3y 95.70, >3y nil. Temporarily suspended: nil. Note states no project is overdue or over the original cost (p.218). 86.6% of CWIP is under one year old [calc]. The 89.13 over 3 years looks like the prior 95.70 (2-3y) aged forward [calc]; an April 2022 TSIIC land parcel of 75.17 in CWIP (Mangampet) is under a High Court writ petition (No. 18735 of 2024, by local residents) with the case pending (p.218). Whether the 89.13 is this land is NOT FOUND IN DOCUMENT [INFERENCE only]. RATING YELLOW (litigation on land held in CWIP).
- Capital advances 1,237.18 vs 1,108.04 (+11.7%) (Note 6, p.219). The cited "note below" is missing; vendor split, ageing, related-party content NOT FOUND IN DOCUMENT. Capital commitments 1,182.77 vs 523.34 (+126%) (Note 28(b), p.233).
- Commissioned in FY26: PPE additions 3,961.55 (plant 3,047.63; buildings 477.71) (Note 3(a), p.214). Gross PPE 8,991.30 vs 5,029.75 (+78.8%) [calc]. Uncommissioned/unpaid capex pool: CWIP 2,566.82 + capital advances 1,237.18 + commitments 1,182.77 = 4,986.77 [calc]. This is 82.7% of FY26 revenue [calc].
- Capex tie-out [calc]: PPE additions 3,961.55 + CWIP increase 1,769.02 + capital-advance increase 129.14 - capital creditor increase 63.31 - capitalised borrowing costs 92.04 = 5,704.36 vs cash flow "purchase of PPE including CWIP and capital advances" 5,724.80 (p.193). Gap 20.44. GREEN.
- Capex funding: deposits matured 4,795.34 (QIP money) plus net borrowings 2,130.57 [calc: 1,542.43 - 116.98 + 705.12] funded capex 5,724.80 and OCF burn 1,189.66 (p.193-194).
- Title: Tunkibollaram land 259.02 held in TSIIC's name; transfer subject to full payment, project implementation in full and 50% land use (Note 3, p.215). YELLOW (conditions outstanding; the 3-year agreement from Sep 2021 has lapsed by its own terms; extension NOT FOUND IN DOCUMENT).

## 1. ACCOUNTING POLICIES AND CHANGES (Note 2, pp.196-213)
- Going concern basis stated (Note 2.1(i), p.196). GREEN.
- Revenue (Note 2A, pp.200-201): point-in-time on delivery; job work recognised on completion. Bill-and-hold style criteria listed (p.200). No contract assets. Single performance obligation. GREEN on form; YELLOW that services (job work) grew 71.7% and bill-and-hold wording appears, but no bill-and-hold amount is disclosed: NOT FOUND IN DOCUMENT.
- Export incentives in operating revenue 29.08 (p.229). Recognised when assurance exists. GREEN.
- Depreciation (Note 2D, p.205): plant and machinery 15 years vs 7.5 years under Schedule II. Double the statutory life (all other classes match Schedule II). Change in lives this year: none stated. Depreciation on PPE 495.70 on average gross PPE ≈ 7,010.5 [calc] = 7.1% [calc]. A 7.5 year life would roughly double plant depreciation [calc, indicative only]. Plant is 6,885.05 of 8,991.30 gross (76.6% [calc]) (Note 3(a), p.214). RATING YELLOW: flatters EBIT; no technical-evaluation detail disclosed (NOT FOUND IN DOCUMENT).
- Tools: depreciated by quantity, max 5 years (p.206); tools expense 270.42 in other expenses (Note 27, p.231). Not capitalised. GREEN.
- Capitalisation: borrowing costs capitalised 92.04 in total (36.33 in PPE + 35.51 in CWIP + 20.20 in capital advances, Notes 3, 4, 6) matching Note 25 (p.231) [calc: sum = 92.04]. Prior: 8.30 + 6.34 + 30.96 = 45.60 = 45.60. Gross interest 400.23 [calc] of which 23.0% capitalised. Interest on capital advances capitalised (20.20) is unusual: capital advances are not qualifying assets until work starts. YELLOW.
- Inventory policy (Note 2E, pp.206): weighted average; obsolescence provision by management estimate; scrap at NRV. Amount of provision NOT FOUND IN DOCUMENT.
- ECL: provision matrix on days past due (Note 34, p.242). Rates NOT FOUND IN DOCUMENT.
- Impairment test assumptions (growth, discount rate): NOT FOUND IN DOCUMENT; no goodwill in group (none on the balance sheet, p.191).
- Leases (Note 2H and 3(b), pp.208, 216): ROU land 161.13; lease liability 176.84; incremental borrowing rate NOT FOUND IN DOCUMENT. Interest on lease 16.50 on opening 197.83 = 8.3% [calc].
- New standards: Ind AS 21 amendment, no impact; no supplier finance; Pillar Two not applicable (p.213). Ind AS 1 amendment from 1 Apr 2026: no impact expected. GREEN.
- Note 2.1(vii) subsidiary table prints "March 31, 20225" (typo, p.199); Notes headings say "standalone financial statements" on the consolidated statements (pp.191-195). GREEN, clerical.

## 2. RELATED PARTY TRANSACTIONS (Note 31, pp.233-235; Rs Mn)
Cross-reference defect: Notes 8 and 15 point to "Note 29" for related parties; Note 29 does not exist in the consolidated set (RPT is Note 31, which is also the number of the segment note). YELLOW (clerical).

KMP and relatives:
| Party | Relationship | Nature | FY26 | FY25 | YoY |
| Rakesh Chopdar | Chairman and CEO, promoter | Remuneration | 48.00 | 48.00 | 0.0% |
| Jyoti Chopdar | Whole time director | Remuneration | 12.00 | 12.00 | 0.0% |
| Vishnu P. Malpani | WTD | Remuneration | 7.20 | 7.42 | -3.0% |
| Murali Krishna Bhupatiraju | MD (from 3 Jan 2025) | Remuneration | 16.71 | 9.99 | +67.3% |
| Ful Kumar Gautam | CS (to 28 Nov 2025) | Remuneration | 2.56 | 2.13 | +20.2% |
| Ronak Jajoo | CFO | Remuneration | 5.55 | 5.28 | +5.1% |
| Praneeth Abhishek Gunda | CS (from 29 Nov 2025) | Remuneration | 1.03 | nil | new |
| Kartik Chopdar | Relative of KMP | Remuneration | 5.75 | 4.87 | +18.1% |
| Satwik Chopdar | Relative of KMP | Remuneration | 0.92 | 0.48 | +91.7% |
| Directors | Sitting fees | | 5.56 | 2.09 | +166% |
| Directors | Reimbursement | | 2.10 | nil | new |
Totals [calc]: KMP remuneration 93.05 vs 84.82 (+9.7%); relatives 6.67 vs 5.35. Figures exclude gratuity and mediclaim (footnote, p.234).

Entities under KMP influence (Note 31(d), (e), p.235):
| Party | Nature | FY26 | FY25 | YoY |
| Atlas Fasteners | Sale of goods/services | 17.19 | 2.24 | +667% |
| Atlas Fasteners | Purchase of PPE | 5.31 | nil | new |
| Atlas Fasteners | Job work expense | 0.59 | 1.11 | -46.8% |
| Agrima Logipark | Rent expense | 13.06 | 12.20 | +7.0% |
| Swastik Coaters | Rent expense | 1.56 | 1.48 | +5.4% |
| Rouland Chemicals | Rent expense | 1.56 | 1.48 | +5.4% |
| Swastik Coaters | Reimbursement | 0.71 | nil | new |
| Swastik / Rouland | Interest income (each) | 0.20 | 0.20 | 0.0% |
Balances: Atlas trade receivable 23.98 (3.90); Atlas advance to supplier 10.80 (12.40); security deposits Swastik 4.96, Rouland 4.96, Forgen 2.00; payables Rouland 1.29, Agrima 6.86 (nil).
- RPT ex-KMP pay = 40.38 [calc] = 0.67% of revenue 6,029.75; sale to Atlas = 0.29% of revenue. GREEN on scale.
- Rent: promoter-linked entities charge 16.18 [calc] of the 16.36 short-term lease cost (Note 3(b)(ii), p.217; Note 27, p.232), 98.9% [calc]. Arm's-length evidence NOT FOUND IN DOCUMENT. YELLOW, small.
- Atlas Fasteners: both customer (17.19, +667%) and supplier (5.31 PPE; 0.59 job work), receivable 23.98 grew 6x [calc]; recoverability fine at this size. YELLOW (watch).
- Loans to promoter entities: none shown; deposits only (Notes 5, 31). Interest on 4.96 deposits at 0.20 = 4.0% [calc].
- Related party transactions with subsidiaries are eliminated; guarantee for subsidiary 50.59 (Note 28(a)) equals ICICI loans of Azad VTC (33.03 + 17.56 = 50.59 [calc]) (Notes 13, 14, pp.226-227). Personal guarantee by VTC's co-promoter. GREEN.
- Promoter shareholding fell from 3,83,30,255 shares (59.35%) to 3,54,44,988 (54.88%): 28,85,267 shares sold [calc] (Note 11(v), p.223). The note prints "-7.53%" which is the relative change [calc]. Pledge of promoter shares: NOT FOUND IN DOCUMENT in notes. Reason/buyer of the sale NOT FOUND IN DOCUMENT. YELLOW.

## 3. CONTINGENT LIABILITIES (Note 28, pp.232-233; Rs Mn)
| Nature | FY26 | FY25 | Stage | Company view |
| Direct tax | 19.67 | 19.67 | Intimation u/s 143(1) demands AY 2022-23 (15.71) and AY 2021-22 (3.96); 80JJAA denial and challan mismatch | Relief expected, applications filed |
| GST | 2.13 | 13.20 | FY20 and FY21 demands; FY20 tax dropped, interest/penalty 0.09; FY21 tax 0.98 + interest/penalty 1.04 confirmed | Strong case, appeal to tribunal |
| Customs duty | 220.94 | 75.11 | Advance Authorisation/EPCG export obligation discharge certificate not obtained; intimation to pay 218.57; plus drawback recovery 2.37 (FY15 exports, FEMA timeline) | Export obligation "largely met"; certificate pending norm fixing |
| Guarantees for subsidiary | 50.59 | 52.45 | | |
| Total | 293.33 [calc] | 160.43 [calc] | | |
- Total 293.33 = 1.9% of equity 15,288.36 [calc]. No single item >10% of net worth. Largest item customs 220.94 = 1.4% of net worth [calc].
- Customs duty up 194% [calc]. It is 11.8% of FY26 PBT [calc]. No provision stated: Note 16 holds only employee provisions (p.228). Cash-out risk if EODC is not closed. RATING YELLOW. Cause is regulatory (norms committee delay) per the note; "largely met" has no percentage: NOT FOUND IN DOCUMENT.
- Interest on delayed duty if payable: NOT FOUND IN DOCUMENT.

## 4. TRADE RECEIVABLES (Note 8, pp.220-221; Rs Mn)
- Gross 3,206.54 vs 2,306.95 (+39.0%); allowance 89.93 vs 72.15 (2.8% of gross [calc]); net 3,116.61. Allowance movement: opening 72.15 + 17.78 = 89.93; P&L charge shows 17.87 in Note 27 and the cash flow (p.193, p.232) vs 17.78 in Note 8: 0.09 gap, immaterial.
- Terms "30 to 180 days" (p.220).
| Ageing | Not due | <6m | 6m-1y | 1-2y | 2-3y | >3y | Total |
| 31 Mar 2026 | 2,219.30 | 704.94 | 122.53 | 130.20 | 12.93 | 16.64 | 3,206.54 |
| share [calc] | 69.2% | 22.0% | 3.8% | 4.1% | 0.4% | 0.5% | 100% |
| 31 Mar 2025 | 1,144.39 | 982.17 | 115.45 | 35.57 | 18.14 | 11.23 | 2,306.95 |
| share [calc] | 49.6% | 42.6% | 5.0% | 1.5% | 0.8% | 0.5% | 100% |
- Over 6 months: 282.30 (8.8%) vs 180.39 (7.8%) [calc]. Over 1 year: 159.77 (5.0%) vs 64.94 (2.8%) [calc]. The 1-2 year bucket rose 3.7x [calc]. Allowance 89.93 covers 56.3% of the over-1-year balance [calc].
- Past due total 987.24 (30.8%) vs 1,162.56 (50.4%) [calc]. The "not due" share jumped 19.6 points. Reading: either collections on invoiced debts improved or invoice terms lengthened (180-day terms); the note cannot separate them [INFERENCE]. Not-due balance rose 94% against revenue +32% [calc].
- Ageing schedule defect: credit-impaired receivables 89.93 are in the gross total but the ageing shows credit impaired "-" in every bucket and all 3,206.54 as "considered good" (p.221). The note's own face says gross includes 89.93 credit impaired (p.220). YELLOW (disclosure inconsistency).
- Single customer >10%: two customers are >= 10% of revenue (Note 31(c)); customer-wise receivable NOT FOUND IN DOCUMENT.
- Related party receivables: Atlas Fasteners 23.98 (Note 31(e)).
- FC-denominated receivables: USD 24.18 Mn = 2,293.38; EUR 5.68 Mn = 618.85; together 2,912.23 = 93.4% of net receivables [calc] (Note 34, p.244).
- Receivable days (net, revenue basis) [calc]: FY26 188.7; FY25 178.4. FY24 not available in this AR's notes; NOT FOUND IN DOCUMENT here.
- Trend call: deteriorating on days (+10.3) and on the 1-2 year bucket; improving on past due under 6 months. Net call: DETERIORATING (see YAML note for CALL 3). RATING YELLOW.

## 5. INVENTORY (Note 7, p.219; Rs Mn)
| Category | FY26 | FY25 | YoY |
| Raw material | 1,188.05 | 626.91 | +89.5% |
| Work in progress | 1,531.74 | 967.53 | +58.3% |
| Finished goods | 107.23 | 42.75 | +150.8% |
| Scrap inventory | 199.13 | 104.32 | +90.9% |
| Stores, spares, fixtures | 264.98 | 151.50 | +74.9% |
| Total | 3,291.13 | 1,893.01 | +73.9% |
[YoY by calc.] Revenue +31.8%. Total inventory = 54.6% of revenue vs 41.4% [calc].
- Raw material days on purchases 1,865.87: 232 vs 199 days [calc] (Note 23(a), p.230).
- Scrap inventory doubled while scrap sales fell 44.3% (Note 21, p.229). Scrap inventory increase of 94.81 is a credit in "changes in inventories" [calc] (Note 23(b), p.230). YELLOW.
- Total change in inventories credit (723.50) offsets expense; 38% of total inventory build (1,398.12) is raw material and stores, which do not flow through that line [calc].
- Write-downs / provision amounts: NOT FOUND IN DOCUMENT. Obsolete inventory disclosure: NOT FOUND IN DOCUMENT.
- Inventory pledged under secured borrowings (Notes 13, 14). Statement agrees with bank stock statements per Note 41(m) (p.250), no variance given. GREEN.
- Rating: RED for the working-capital consequence (OCF), YELLOW for quality (no write-down disclosure).

## 6. INVESTMENTS (Notes 2.1, 5, 42, 43, 44; Rs Mn)
- Subsidiaries: Azad Prime Private Limited 51% (49% Leo Primecomp); Azad VTC Private Limited 51% (49% other shareholder) (p.199). Both 51% in both years. No associates, no JVs, no investments in listed or unlisted securities, no ICDs or loans to anyone (Note 41(e), p.249).
- Note 42 (pp.250-251): Azad Prime call/put option with Leo Prime; price is higher of fair market value or 225.63. Holding company paid 54.13 non-refundable advance (Dec 2024). Redemption liability 171.50 (Note 18, p.228) = 225.63 - 54.13 [calc]. Debit 225.63 to "derivative financial instrument" reserve in equity (Note 12(v), p.224). Bypasses P&L. The liability is FVTPL level 3 held flat at 171.50 for two years (Note 34, p.240); no fair-value work or sensitivity disclosed. If FMV exceeds 225.63 the liability steps up through P&L. Prime net assets 173.84 (Note 44, p.251). YELLOW.
- Note 43 (p.251): Azad VTC call option; refundable advance 23.3 paid. Note 5 shows advance towards purchase of investments 20.78 (19.11 prior) (p.219), not 23.3 or 54.13. Mismatch, NOT FOUND IN DOCUMENT to reconcile. YELLOW, small.
- Loss-making subsidiary: Azad VTC loss (41.97) vs (8.73) prior (Note 44, p.251, 252) = 4.8x. Azad Prime profit 13.89 vs (7.27). VTC net assets 66.97. VTC bank debt 50.59 guaranteed by the parent. YELLOW.
- NCI check [calc]: 49% of subsidiary net assets (173.84 + 66.97) = 118.0 vs reported NCI (0.62) (p.191). NCI profit share is 6.86 against a 49% share of Prime profit of 6.81 and a 49% share of VTC loss of (20.57) [calc]; total expected (13.76). It appears VTC's loss is not shared with NCI and the Prime NCI is effectively treated as a liability [INFERENCE]. Mechanics NOT FOUND IN DOCUMENT. YELLOW.
- Note 44 parent PAT 1,363.71 vs parent standalone PAT 1,321.61 (standalone P&L p.122): +42.10 [calc]. The shares of profit sum to the consolidated 1,335.63 only with that parent figure. Consolidation adjustment of +42.10, about the size of the VTC loss (41.97), is unexplained. NOT FOUND IN DOCUMENT. YELLOW. (FY25 gap was (3.91) [calc].)

## 7. BORROWINGS (Notes 13, 14, 34, 35; pp.225-227, 243-245; Rs Mn)
- Total debt 4,566.39 vs 2,435.82 (+87.5% [calc]) (Note 35, p.245). Long-term 3,373.12 gross (2,809.47 + current maturities 563.65 [calc]); working capital loans 1,193.27 vs 488.15 (+144% [calc]). Net debt 2,720.48 vs net cash (4,534.45) (Note 35, p.245). Gearing 0.15 vs (0.48).
- Instruments (all secured, Note 13): 
  | Lender | Outstanding FY26 | Rate | Tenor |
  | Consortium UBI | 400.33 | 6.5%-10.9% | 66 monthly |
  | Consortium IndusInd | 477.25 | same | 22 quarterly |
  | Consortium ICICI | 417.81 | same | 66 monthly |
  | HDFC equipment | 383.51 | 8.05%-9.05% | 72 monthly |
  | Yes Bank equipment | 489.16 | 8.15%-9.30% | 60 monthly |
  | Tata Capital | 163.53 | 9.32%-14.05% | 48-60 |
  | Bandhan | 537.18 | 8.25% | 52 |
  | Bajaj Finance | 399.16 | 8.45%-8.70% | 60 |
  | ICICI (Azad VTC) | 33.03 | 9.85% | 20 quarterly |
  | Vehicle loans | 72.16 (Yes 0.37, HDFC 36.54, BoB 5.94, ICICI 29.31) | 8.06%-11.04% | 24-60 |
  Bank + FI term loans 2,738.27 + 562.69 = 3,300.96 = sum of lines above [calc]. GREEN tie-out. Plus working capital demand loans: UBI 491.82, IndusInd 385.66, ICICI 298.23 (6.3%-9.75%) and VTC 17.56 (Note 14, p.226) [sum 1,193.27 calc].
- Security: first pari-passu on all PPE, second on current assets for term loans; first pari-passu on current assets for WC lines; collateral plots in Telangana (p.225-226). Equipment loans hypothecate the machine. Personal guarantee of VTC's co-promoter for VTC loans (p.226). No promoter personal guarantees on parent loans stated. GREEN.
- Fixed vs floating: variable 3,501.19 (76.7% [calc]) vs 1,398.02 prior; fixed 1,065.20 (Note 34, p.243). 1% rate move = 35.01 pre-tax (1.9% of PBT [calc]). Note: variable plus fixed = 4,566.39 = total debt [calc]. YELLOW (floating rate share up).
- FC borrowings: EUR 8.26 Mn = 900.28 (EUR 8.93 Mn, 821.99 prior); USD 1.13 Mn = 107.16 (Note 34, p.244). 22.1% of debt is FC [calc]. Hedging contracts: NOT FOUND IN DOCUMENT.
- Covenants: "loan covenants" exist, "no breaches" (Note 34 p.243; Note 35 p.245). Covenant terms (ratios, thresholds) NOT FOUND IN DOCUMENT. No waivers disclosed.
- Maturity: the undiscounted table (Note 34, p.243) shows long-term borrowings 2,809.47 all in "1-5 years" (nil beyond 5 years, vs 50.20 in FY25) and puts current maturities 563.65 inside short-term borrowings 1,756.92. A year-by-year 5-year repayment schedule is NOT FOUND IN DOCUMENT. Carrying values are used as "undiscounted" amounts, so interest is not included. YELLOW (table understates cash outflow).
- Related party borrowings: none. Interest cover: EBIT proxy (PBT + finance costs - other income) 1,724.71 / 308.19 = 5.6x [calc] vs 3.4... computed FY25 (1,240.26 + 183.89 - 105.91 = 1,318.24) / 183.89 = 7.2x [calc]. Falling.
- Finance cost components (Note 25, p.231): term loans 132.75, WC 64.16, lease 16.50, other 6.68, FX adjustment 13.23, bank charges 8.56, "other borrowing costs" 66.31 (66.26 prior). The 66.31 is unexplained (LC charges, processing fees?) NOT FOUND IN DOCUMENT. YELLOW.
- Cash flow check: finance costs paid 351.61 vs P&L 308.19 + capitalised 92.04 = 400.23 [calc]; difference within accrual movement of 11.68 and capitalised interest (interest accrued 3.51 to 15.19).

## 8. TRADE PAYABLES (Notes 15, 32; pp.227, 237)
- 852.74 vs 801.08 (+6.5%) [calc]; MSME 181.12 vs 299.81 (-39.6%); others 671.62 vs 501.27 (+34.0%). Terms 30-90 days (p.227).
- Ageing FY26: not due 315.17 (37.0% [calc]); overdue <1y 522.96; 1-2y 14.02; 2-3y 0.11; >3y 0.48. Overdue share 63.0% [calc]; prior 57.6% (452.97 + 8.17 + 0.44 + 0.05 = 461.63 / 801.08 [calc]). Payables run beyond the due date for most of the book.
- MSME overdue: 83.54 + 7.35 + 0.07 = 90.96 of 181.12 (50.2% [calc]) past due, including 7.42 over one year (prior 0.10) (p.227). Yet Note 32 (p.237) reports payments beyond the appointed day: nil, and interest due 0.66 unchanged vs prior (0.66, equal to the FY25 figure). MSMED Act requires payment inside 45 days and compound interest on overdue. An unchanged 0.66 beside 90.96 overdue suggests interest is not being accrued [INFERENCE]. Statutory exposure small but a disclosure gap. YELLOW.
- Payable days (revenue basis) [calc]: 51.6 vs 63.9. Falling payable days adds to the WC strain.
- Capital creditors 120.48 vs 57.17 (Note 18, p.228).

## 9. PROVISIONS (Notes 16, 33; pp.228, 237-239)
- Provisions 70.05 vs 52.14: gratuity 69.24 (non-current 61.90) and leave 0.81. No warranty, no onerous contract, no decommissioning, no litigation provision. GREEN on form; note that customs 220.94 and subsidiary guarantees carry no provision (Section 3).
- Gratuity: unfunded, plan assets nil (Note 33, p.238). Obligation 50.69 to 69.24 (+36.6% [calc]); service cost 17.68 vs 8.84; interest 3.26. Assumptions: discount 7.29%-7.40% vs 6.66%; salary escalation 3%-12% vs 3% flat; attrition 5%; retirement 58; IALM 2012-14. Sensitivity: discount 1% down = 75.61 (+9.2% [calc]); salary 1% up = 75.44. Experience adjustment loss 4.34 (p.238). Note 33 OCI actuarial gain 0.04 and Note 12(iv) actuarial loss (0.12) (p.224) differ by 0.16; the 0.16 matches NCI OCI (P&L p.192). Trivial. Salary escalation range 3%-12% is unusual (prior single 3%). YELLOW, small.
- Employee benefit expense 1,355.23 vs 928.66 (+45.9% [calc]), ahead of revenue +31.8% (Note 24, p.230). Plus outsourced manpower 166.55 vs 85.96 (+93.8% [calc]) (Note 27). Combined people cost 1,521.78 vs 1,014.62 (+50.0% [calc]). YELLOW (cost build ahead of ramp; consistent with capacity ahead of revenue).

## 10. DEFERRED TAX (Notes 17, 36; pp.228, 246-247; Rs Mn)
- Tax expense 537.43 on PBT 1,873.06 = 28.7% [calc] vs statutory 29.12%. Reconciliation: expected 545.00; disallowed (2.94); earlier years (4.58); others (0.05) (p.246). Earlier-year line in the reconciliation is (4.58) vs (3.96) in the P&L; 0.62 difference unexplained. Statutory-rate arithmetic prints 545.00 (29.12% × 1,873.06 = 545.4 [calc]). Immaterial.
- Deferred tax liability net 492.02 vs 274.38 (+79.3% [calc]); PPE 541.25. Deferred tax charge 217.71 vs current tax 323.68: deferred is 40.3% of total tax [calc]. Cause: accelerated tax depreciation on the capex wave. Current tax liability net 10.26 vs 178.64 (Note 20, p.229); tax paid 488.17 (p.193).
- MAT credit: 16.58 used in FY25, nil now. DTAs: credit-impaired receivables (26.19), employee benefits (19.56). No unrecognised DTA disclosed. GREEN.
- The 15-year plant life is for books; tax depreciation is faster. The deferred tax build is sensitive to the book life (Section 1).

## 11. REVENUE DETAILS (Notes 21, 31, 37; pp.229, 236-237, 248)
- Done in LB2. Contract assets: none. Contract liabilities: advances from customers 9.46 vs 44.76 (-78.9% [calc]). Unsatisfied performance obligations / order book: NOT FOUND IN DOCUMENT. Discounts and disallowances: nil.
- Point in time: goods 4,807.05, services 1,222.70 (these figures include scrap/incentive allocation; the split differs from Note 21) [calc: 4,751.51 + 55.54 = 4,807.05; 1,193.62 + 29.08 = 1,222.70].
- Top customer revenue: see LB3.

## 12. OTHER CRITICAL NOTES
- Exceptional items: none shown in the P&L (p.192). GREEN.
- Goodwill: none. Intangibles: none shown on the balance sheet (p.191). NOT FOUND IN DOCUMENT for an intangibles note.
- Capital commitments: 1,182.77 vs 523.34; plus unquantified purchase-of-investment commitment (Notes 42, 43) (p.233).
- Foreign currency: net open USD position; 5% USD move = 104.07 pre-tax (5.6% of PBT [calc]), EUR (14.39) (Note 34, p.245). FX gain 214.01 in other income (11.4% of PBT [calc]); unrealised portion 158.16 (8.4% of PBT [calc]) (p.193). Without hedge disclosure the FX gain is a rupee-weakness gain, not operating profit. YELLOW. Forward contracts: NOT FOUND IN DOCUMENT.
- Other income 456.54 (see LB2): interest 228.49 on QIP deposits will fall as 4,795.34 of deposits matured. Interest from QIP deposits on 1,599.99 remaining is the base.
- Segment: single segment (Note 31, p.236). Geography in LB2.
- EPS: basic = diluted 20.57 vs 14.66 (Note 30, p.236). No potential shares outstanding. EPS growth 40.3% [calc]. Weighted shares 6,45,81,743 vs 5,95,47,496 (QIP weighted).
- Events after balance sheet date (Note 39, p.249): NRC approved 80,000 options at Rs 1,050 on 12 May 2026; 0.12% of shares [calc]. Exercise price vs QIP price of Rs 1,280. Existing ESOP outstanding: none disclosed; "No potential equity shares" (p.236). GREEN.
- CSR: expense 14.01 vs 8.19 (Note 27, p.232). Prescribed amount and shortfall NOT FOUND IN DOCUMENT in the notes.
- Share capital: no change in FY26 (Note 11, p.222); authorised 7,50,00,000 shares. Bonus issue FY24 only (p.223). Single class.
- Reserves bypassing P&L: derivative-instrument reserve (225.63) (Note 12(v)); securities premium credit 22.42 of share-issue-expense reversal (Note 12(i), p.224). GREEN with note.
- Statutory (Note 41, pp.249-250): audit trail not enabled at database level in the parent's accounting software; subsidiaries' audit trail not enabled throughout the year, so the auditor could not assess tampering (p.250). RATING YELLOW (control weakness, repeating? FY25 comparison NOT assessed in this pass).
- Labour codes (Note 45, p.252): no material impact assessed. GREEN.
- Going concern language: only the basis-of-preparation statement (Note 2.1(i), p.196) and capital management objective (Note 35, p.245). No material-uncertainty language anywhere in the notes. NONE.
- Restatements / reclassifications: (1) FY25 top-1/top-5 customer split changed between ARs, from "top customer 648.81, top 5 2,352.65" to "top 648.81, top-5 1,703.84" (Note 34, p.242 vs Annual_Report_2025). (2) FY25 depreciation prints 294.84 in P&L (p.192) and 294.85 in the cash flow (p.193), 0.01. (3) FY25 note-44 net assets total 13,930.68 vs balance-sheet 13,930.26 (p.252) 0.42. (4) FY25 customs contingent 75.11 shown unchanged. None changes a headline number.
- Auditor's remuneration 5.70 vs 5.82; auditor-type opinion: unmodified per the report on pp.183-190 (not part of notes; not read in this pass).

## ACCOUNTING-QUALITY TIE-OUTS PERFORMED (GREEN)
Borrowing totals tie (3,300.96); borrowing costs capitalised tie (92.04; 45.60); capex cash flow ties within 20.44; lease liability roll-forward ties (197.83 + 16.50 - 37.49 = 176.84); gratuity roll-forward ties (50.69 + 17.68 + 3.26 - 4.38 + 4.34 - 2.36 = 69.23, vs 69.24); equity roll-forward ties; QIP deposits tie within 2.72; redemption liability ties; Note 28 subsidiary guarantee ties to Notes 13 and 14.

## PASS 1 SUMMARY: TOP 10 FINDINGS BY INVESTOR IMPORTANCE
| Rank | Finding | Anchor | Rating |
| 1 | Operating cash flow (1,189.66) Rs Mn vs +536.67 prior on +31.8% revenue; WC drain 3,034.45; no factoring or bill-discounting disclosure | Cash flow statement p.193; Notes 7, 8, 10 | RED |
| 2 | Inventory +73.9% vs revenue +31.8%; inventory days 199 vs 151; receivable days 189 vs 178; payable days 52 vs 64 (revenue basis, calc) | Notes 7, 8, 15, pp.219-227 | RED |
| 3 | Top customer 1,123.97 = 18.6% of revenue (14.2% prior), two customers over 10%; top-5 about 47.0% (label conflict between standalone and consolidated, FY25 comparative re-split) | Note 31(c) p.237; Note 34 p.242 | YELLOW |
| 4 | QIP: 4,778 drawn in FY26, 1,597.27 unspent (capex object 70.2% used); CWIP 2,566.82 (3.2x), capital advances 1,237.18, commitments 1,182.77; 86.6% of CWIP under one year old | Notes 40, 4, 6, 28(b), pp.249, 217-219, 233 | YELLOW |
| 5 | Debt 4,566.39 (+87.5%); net cash 4,534.45 turned to net debt 2,720.48; 76.7% floating; maturity table shows no spread of repayments | Notes 13, 14, 34, 35, pp.225-227, 243-245 | YELLOW |
| 6 | Plant and machinery depreciated over 15 years vs 7.5 years under Schedule II; plant is 76.6% of gross PPE; interest of 20.20 capitalised on capital advances | Note 2D p.205; Note 6 p.219 | YELLOW |
| 7 | Receivables past one year 159.77 (5.0%) vs 64.94 (2.8%); 1-2 year bucket 3.7x; "not due" jumped to 69.2% (longer terms or better collection); ageing schedule shows credit-impaired as good | Note 8, pp.220-221 | YELLOW |
| 8 | Other income 456.54 (24.4% of PBT) includes FX gain 214.01 (unrealised 158.16) and QIP-deposit interest; core PBT +24.9% vs revenue +31.8% | Note 22 p.229; cash flow p.193 | YELLOW |
| 9 | Customs duty contingency 220.94 (+194%), EPCG/Advance Authorisation discharge certificates pending, no provision; total contingents 293.33 (1.9% of equity) | Note 28(a) pp.232-233 | YELLOW |
| 10 | Azad Prime put/call: redemption liability 171.50 held flat at the floor, FVTPL level 3, 225.63 debited to equity; Azad VTC loss (41.97) 4.8x; NCI (0.62) does not match 49% of subsidiary net assets (118.0); parent PAT in Note 44 exceeds standalone PAT by 42.10 | Notes 42, 43, 44, pp.250-252; Note 12(v) p.224 | YELLOW |

Also noted (ranked below top 10): promoter stake down 59.35% to 54.88% (Note 11 p.223); MSME overdue 90.96 with unchanged interest 0.66 (Notes 15, 32); audit trail not enabled at database level (Note 41(n) p.250); promoter-linked entities are 98.9% of short-term rent (Notes 27, 31); equity issue-cost payments of roughly 155 to 178 appear inside OCF (Notes 18, 12(i)).

## CARRY-FORWARD FOR PASS 2 (not findings)
Items I could not close from the consolidated notes and that Pass 2 should re-check against the standalone notes (pp.121-180): ECL matrix rates; inventory write-down amount; composition of "balance with government authorities" 1,102.51; capital advances detail; derivative/forward contract disclosure; factoring or discounting wording in standalone Note on trade receivables; whether the standalone customer note defines top-5 as incl. or excl. top-1.


---
ERRATA (appended by the orchestrator 2026-11-15 from the stage's own hand-back; the stage has no edit tool):
- Line 24, garbled sentence on the "other assets" line. Correct reading per the stage: 739.76 is 24.4% of the 3,034.45 total working-capital drain (Rs Mn).
- Line 186, stray "vs 3.4... computed" in the interest-cover sentence. Correct figures per the stage: 5.6x in FY26 against 7.2x in FY25.
- The anchor "p.~164" for the standalone customer note should read [page 172].
