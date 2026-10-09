# STAGE 2 NOTES PASS 2 (WHAT WAS MISSED) - SUPREME POWER EQUIPMENT LTD (SUPREMEPWR)

Run: runs/supremepwr-2026-10-06 | Run date 2026-10-06 | Model claude-sonnet-5-5 | Pass 2 of 3
Source: inputs/annual-report/Annual_Report_FY2025-26.txt (read again, standalone Notes 1-34 and consolidated Notes 1-33, plus the three statements). One cross-check source outside the AR: inputs/shareholding/SHP_31Mar2026.txt (named where used).

Conventions are the same as Pass 1. Unit is Rs. lakhs on the face of every statement and Note. Page numbers follow the Pass 1 rule (the "[page N]" footer closes the block above it). "L" is the line number in the .txt. "DERIVED" is arithmetic on printed figures with the formula shown. "NOT FOUND IN DOCUMENT" is a missing disclosure. Ratings: [GREEN] clean, [YELLOW] watch, [RED] red flag. This pass has no [RED] finding. Only new material is reported; Pass 1 items are cited by number only to correct or extend them.

---

## 0. CORRECTIONS TO PASS 1 (apply these before pass 3)

- 0.1 Pass 1 section 0 says "(see 7.9)". It must read "(see 7.10)". Item 7.10 is the one that says consolidated Note 30.6 reprints the standalone bank-statement figures.
- 0.2 Pass 1 item 7.2 repeats management's reason for the fall in DSCR ("higher repayment of debt"). The ratio does not measure repayments. See N2.
- 0.3 Pass 1 section 8 calls the consolidated MSME rise of 713.74 against a fall in "others" of 447.78 "a reclassification not explained". The gap is mostly Danya's own creditors. See N11. It also shows a class swing in the Danya balance between years.
- 0.4 Pass 1 section 9 doubts the 5.00% salary escalation because headcount was NOT FOUND. The Board report annex (outside the Notes) gives 112 permanent employees and a 5.44% median pay rise (L5090-5092). The 5.00% assumption is near the realised median rise. The cost growth is headcount driven, not escalation driven. Prior-year headcount is still NOT FOUND, so the headcount change cannot be sized. Rating for the escalation point drops to [GREEN].
- 0.5 Pass 1 A(b) says no Note names Kannur. That is still true for the Notes. The Chairman's letter and Board report name it (see N16).
- 0.6 Pass 1 NOT FOUND "promoter vs non-promoter warrant split" is answered by the shareholding pattern, not by the AR (see N13).

---

## 1. THE OPEN ITEMS PASS 1 HANDED OVER

| Open item | Result of this pass | Detail |
|---|---|---|
| Capital commitments "Nil" against CWIP 2,797.98 | Still unreconciled. Five facts sit against "Nil". | N4 |
| Capitalised borrowing cost | Amount still NOT FOUND. Tests are inconclusive in both directions. | N4 |
| Do trade payables include capex creditors? | NOT FOUND IN DOCUMENT. The cash flow statement is built from accrual additions, so any capex creditor sits in operating cash flow. | N4 |
| Interest on statutory dues 55.34 | Nature NOT FOUND. It is group wide (Danya adds 17.90). It sits against a CARO "regular in depositing" statement. A tax-payment pattern in the Notes is consistent with it. | N10 |
| Receivables ageing and provisioning | The 588.04 over-one-year bucket was already outstanding at 31-Mar-25. Nil provision, no bad-debt line. | N8 |
| Promoter group 52.07% (AR) vs 57.16% (SHP) | Reconciled to the share. Gap is two named promoter-group holders. | N13 |
| Pass 1 NOT FOUND list | Status table in section 3. | Section 3 |

---

## 2. NEW FINDINGS, BY NOTE

### N1. ICICI term-loan table does not reconcile to the balance sheet [YELLOW, high priority]
Anchors: standalone Note 6 (p.66-67), Note 9 (p.67), Note 13 not used. Consolidated Note 7 (p.87).

What ties:
- Current maturities 1,095.48 (Note 9) = ICICI 1,005.19 + Canara 63.33 + IndusInd 10.60 + HDFC 16.36. Check: ICICI total per terms table 3,500.00 + 474.89 = 3,974.89; less ICICI non-current on balance sheet 2,969.70 = 1,005.19. HDFC current = 40.46 - 24.10 = 16.36. Sum 1,005.19 + 63.33 + 10.60 + 16.36 = 1,095.48. Ties to the lakh.
- The three small loans tie to their EMI: Canara 12 x 5.28 = 63.36 against 63.33; IndusInd 11 x 0.96 = 10.56 against 10.60.

What does not tie (DERIVED):
- ICICI EMI cash for 12 months = (53.03 + 6.41) x 12 = 713.28. That is principal plus interest. Current maturity of ICICI principal is 1,005.19. Principal due exceeds total EMI cash by 291.91 (40.9%), before any interest.
- ICICI loan A: the terms table shows closing balance 3,500.00 (a round figure) with 72 of 84 instalments left, so 12 instalments were paid. A round balance after 12 EMIs shows no visible amortisation. 72 x 53.03 = 3,818.16, so total future payments would carry only 318.16 of interest on 3,500.00. Present value of 72 monthly payments of 53.03 at 9.50% per year is about 2,902 (annuity formula, monthly rate 0.0079167). The stated 3,500.00 is about 598 above that.
- ICICI loan B: closing balance 474.89 with 78 instalments of 6.41. Present value at 9.50% is about 372. The stated balance is about 103 above that. 78 x 6.41 = 499.98.
- Together the EMI column cannot amortise the stated balances at the stated rate by about 701 (DERIVED, approximate).
- Possible explanations that the document does not give: a balloon or step-up repayment, partial drawdown with 3,500.00 being the sanction, or an EMI column that is not the real schedule. The reason is NOT FOUND IN DOCUMENT. The five-year schedule, fixed or floating rate, covenants and waivers remain NOT FOUND (Pass 1 7.3, 7.5).
- Why it matters: 1,005.19 of ICICI principal falls due within 12 months. That is 25.3% of ICICI debt and 22.0% of total borrowings 4,572.70 (DERIVED). It is the single largest driver of the current ratio fall to 1.15 (Note 34(a), p.76).

### N2. DSCR is a forward-maturity ratio, and management's explanation is wrong [YELLOW]
Anchors: standalone Note 34(c) (p.76); consolidated Note 33(c) (p.96); P&L (p.62); consolidated Notes 10, 26 (p.87, p.91).

DERIVED reconciliation, ties to two decimals in all four cases:

| Case | Earnings for debt service (PBT + depreciation + interest expense) | Debt service used (interest expense + closing current maturities) | Ratio | Printed |
|---|---|---|---|---|
| Standalone FY26 | 2,691.87 + 165.26 + 128.24 = 2,985.37 | 128.24 + 1,095.48 = 1,223.72 | 2.44 | 2.44 |
| Standalone FY25 | 2,395.92 + 38.62 + 157.71 = 2,592.25 | 157.71 + 89.90 = 247.61 | 10.47 | 10.47 |
| Consolidated FY26 | 2,851.66 + 174.24 + 147.06 = 3,172.96 | 147.06 + 1,134.48 = 1,281.54 | 2.48 | 2.48 |
| Consolidated FY25 | 2,605.00 + 47.26 + 202.24 = 2,854.50 | 202.24 + 128.90 = 331.14 | 8.62 | 8.62 |

- The "principal repayment" in the denominator is the year-end current maturity, which is next year's scheduled principal. It is not what was repaid in the year. The management reason ("higher repayment of debt during the year", standalone p.76; "up ~287%", consolidated p.96) describes the wrong thing. 1,281.54 / 331.14 = 3.87, so +287% ties to the maturity jump.
- Standalone says EBITDA "grew only marginally". EBITDA on the same definition rose 15.2% (2,985.37 / 2,592.25). Consolidated rose 11.2%.
- Principal actually repaid in FY26 is NOT FOUND IN DOCUMENT. The cash flow statement nets borrowings (Note N4).
- Meaning for the reader: 2.44x is a cover of FY26 earnings over FY27 scheduled principal plus FY26 interest. It is a forward test already stressed by N1.

### N3. CWIP ageing schedule is arithmetically inconsistent; plant went into use late in the year [YELLOW]
Anchors: standalone Note 13 (p.68-69), Note 30.16 (p.73); consolidated Note 14 (p.88-89, FY25 table), Note 30.16 (p.94).

- CWIP roll (standalone Note 13): opening 4,935.83, additions 1,893.45, transfers to PPE 4,031.30, closing 2,797.98. By class: buildings 933.24 + 1,040.07 - 715.18 = 1,258.13 (printed 1,258.12); plant and machinery 3,101.00 + 325.83 - 2,740.98 = 685.85; testing equipment 326.45 + 450.53 = 776.98 (printed 776.99).
- Disclosed ageing: 0-1 year 2,471.53; 1-2 years 326.45; nothing older (Note 30.16).
- DERIVED test. Items added in FY26 cannot exceed the FY26 additions of 1,893.45. The 0-1 year bucket is 2,471.53, which is 578.08 above that ceiling. So at least 578.08 of the "0-1 year" bucket was already in CWIP at 31-Mar-25.
- DERIVED minimum of pre-FY26 CWIP still open: opening 4,935.83 less all transfers 4,031.30 = 904.53, or 32.3% of closing CWIP. By class: buildings 218.06, plant and machinery 360.02, testing equipment 326.45. The disclosed 1-2 year figure of 326.45 is only the testing equipment. It equals the 31-Mar-25 testing CWIP exactly, with no transfer in the year (consolidated FY25 table: testing CWIP addition 326.45).
- If any transfer drew on FY26 additions, the pre-FY26 balance is larger than 904.53. Either way the schedule understates old CWIP. The ageing basis (invoice date, due date, last addition) is NOT FOUND IN DOCUMENT.
- No schedule of projects overdue or over cost is given (NOT FOUND IN DOCUMENT). The only line is "Project in Progress".
- DERIVED: 3,715.00 of the 7,746.30 PPE additions (48.0%) did not pass through CWIP (7,746.30 - 4,031.30). Land direct 226.09, buildings 615.67, plant and machinery 1,809.81, testing equipment 522.59, electrical fittings 409.45, furniture 67.31, computers 24.78, vehicles 39.30.
- Late-year capitalisation, class by class (DERIVED, straight line at the stated lives, no residual, ignores deletions): in-service months implied by FY26 depreciation on additions are buildings about 1.8, plant and machinery about 2.7, testing equipment about 3.3, electrical fittings about 1.7. Method: depreciation charged less opening gross over life, divided by addition over life. Example for plant and machinery: (78.06 - 153.31/15) = 67.84 against 4,550.79/15 = 303.39, which is 22.4% of a year. This agrees with the Chairman's text that depreciation rose "following the capitalisation of the new facility" (L898-900) and shows the capitalisation was in Q4.
- Cross-reference outside the Notes: the Kannur facility is said to cost about Rs.100 Crore (L858-860, L1445). CFS capex FY25 3,967.65 + FY26 5,746.46 = 9,714.11 lakhs (Rs.97.14 Cr, DERIVED). Closing CWIP 2,797.98 plus software under development 137.01 = 2,934.99 is 29% of Rs.100 Cr still not capitalised, although the same text says the plant is "commissioned". Which parts are still open is NOT FOUND IN DOCUMENT.

### N4. Capex funding, classification and the three Pass 1 open items [YELLOW]
Anchors: standalone CFS (p.62), Notes 2.4 and 2.9 (p.62-63), Note 26 (p.71), Note 30.1B (p.72), Note 30.17 (p.74), Note 29.I (p.76), Note 30.25 (p.76); consolidated Note 30.1B (p.93), CFS (p.83).

Capital commitments "Nil":
- Five facts in the same document sit against "Nil" at both dates: (a) CWIP 2,797.98 and software under development 137.01 added in FY26; (b) imports of capital goods CIF 105.34 in FY26, nil in FY25 (Note 30.17); (c) the expansion wording in the AGM borrowing-limit item (Pass 1 7.9); (d) the Board report text that the company expects to take Kannur to about 90% utilisation over two to three years (L1457-1459) and priorities for FY27 (L1068-1078); (e) Note 29.I(2) repeating "no contractual commitments" for PPE. No document reconciles "Nil" with these. Reason NOT FOUND IN DOCUMENT.

Capex creditors:
- The CFS capex line is the accrual addition, not a cash figure. Standalone: Note 13 additions net of CWIP transfers = 7,746.30 + 6.12 + 137.01 + 1,893.45 - 4,031.30 = 5,751.58 against CFS 5,746.46 (difference 5.12, 0.09%). Consolidated FY25: additions 4,403.24 - transfers 425.71 = 3,977.53 against CFS 3,977.54.
- Result: any unpaid capex creditor inside trade payables (up 2,489.23) and any capex advance inside advances to suppliers (320.30, up 302.30) is carried in operating cash flow. That raises CFO and lowers reported cash capex by the same amount. The amount is NOT FOUND IN DOCUMENT. Note 10 has no capital-creditor line. Direction of the bias is known, size is not.

Capitalised borrowing cost:
- Policy permits it (Notes 2.4, 2.9). No amount is disclosed. Interest paid in the CFS equals the P&L interest expense to the paisa in both years (128.24 and 157.71), and Note 11 has no accrued-interest line.
- DERIVED: interest expense 128.24 / average of opening and closing total borrowings 3,103.27 = 4.13%. The stated rates run 7.50% to 11.50%. At the lowest stated rate, 7.50%, interest on the average balance would be 232.74. The 104.50 gap is open. Late-year drawdown would explain it. So could capitalisation into CWIP (average CWIP about 3,867). The document gives drawdown dates nowhere. The test is inconclusive in both directions.

Cash flow split of borrowings:
- CFS shows long-term borrowings +2,130.06 and short-term +808.82. These are balance-sheet differences, so the reclassification of 1,005.58 of extra current maturities (1,095.48 - 89.90 = 1,005.58) moves money from the "long-term" line to the "short-term" line. Term debt rose by 3,135.63 (4,089.28 - 953.65), cash credit fell by 196.75 (483.43 - 680.18). Total 2,938.88 ties to the balance sheet change 2,938.86. Gross drawdown and gross repayment are NOT FOUND IN DOCUMENT.

### N5. The Danya trade loop drives most of Danya's growth and a large share of SPEL's growth [YELLOW]
Anchors: standalone Note 20 (p.70), Note 30.21 (p.74-75); consolidated Note 20 (p.90), Notes 16, 17 (p.89-90), Note 11 (p.87).

DERIVED from printed figures (Danya turnover = consolidated gross sales less standalone sales):
- Danya turnover: FY26 23,181.95 - 19,007.73 = 4,174.22 (ties to auditor Other Matters p.78). FY25 17,314.79 - 14,479.83 = 2,834.96. Growth 1,339.26 (+47.2%).
- Danya sales to SPEL (SPEL purchases from Danya): 2,558.08 against 1,278.20, a rise of 1,279.88. That is 95.6% of Danya's turnover growth. Danya external turnover: 1,616.14 against 1,556.76, +3.8%.
- Danya's dependence on SPEL: 61.3% of turnover in FY26 against 45.1% in FY25 (Pass 1 showed FY26 only).
- SPEL sales to Danya: 2,459.83 against 1,164.89, a rise of 1,294.94. That is 28.6% of SPEL's standalone revenue growth of 4,527.90. Consolidated revenue grew 3,292.34 (+22.1%).
- Danya inventory (consolidated less standalone): 1,653.47 against 900.73 (+83.6%). On Danya turnover that is 144.6 days against 116.0 days.
- Danya's external trade payables (consolidated less standalone, plus the eliminated balance): FY26 6,220.03 - 5,954.07 + 662.82 = 928.78. FY25 3,153.35 - 3,464.86 + 575.64 = 264.13. That is 3.5 times.
- The "payable to Danya" 662.82 looks like a netted current account. Roll-forward: 575.64 + purchases 2,558.08 - sales 2,459.83 = 673.89, against 662.82 shown. Gap 11.07 (cash settlements or GST, NOT FOUND). No receivable from Danya is shown despite 2,459.83 of sales, which fits a net balance. The document does not say it is netted. This partly answers the Pass 1 open point (section 2, observation 3).
- Reading for pass 3: two thirds of Danya's order growth is SPEL's own spend and over a quarter of SPEL's reported growth is sales into Danya. Both are removed in consolidation. The consolidated order book (Rs.588.17 Cr, L1469) and the "orders from KSEB, TNPDCL and Danya" line (L1464-1465) do not split out the Danya share. Whether intra-group orders sit inside the order book is NOT FOUND IN DOCUMENT.

### N6. Consolidated profit and reserves show no consolidation adjustment at all [YELLOW]
Anchors: consolidated P&L (p.82), Notes 2.2 (p.83), 4 (p.85), 13 (p.88), 22 (p.95), 26 (p.91); AOC-1 (p.49, via Pass 1).

- Consolidated reserves 8,794.70 (FY25 6,750.65) equal standalone reserves to the lakh. Consolidated attributable profit 2,044.06 (FY25 1,860.04) equals standalone profit.
- DERIVED proof of zero adjustment: Danya PBT = consolidated PBT 2,851.66 - (SPEL PBT 2,691.87 - profit share 211.51) = 371.30. Danya tax = consolidated current tax 666.28 - 530.75 = 135.53, plus deferred 117.45 - 117.06 = 0.39, plus earlier years 0.37 = 136.29. Danya PAT = 371.30 - 136.29 = 235.01, which is the AOC-1 figure to the paisa.
- So no unrealised intra-group profit was eliminated from profit in FY26 or FY25, although 5,017.91 of intra-group sales (FY25 2,443.09) were eliminated and Danya holds 1,653.47 of inventory (FY25 900.73). Policy text says unrealised profit is eliminated (Note 2.2). Amount eliminated: NOT FOUND (Pass 1 section 1). Now it is derived as nil, or fully offset. Rating YELLOW because the margin on goods that SPEL sold to Danya and Danya has not sold on stays in group profit.
- Tax effect (DERIVED): Danya effective tax rate 136.29 / 371.30 = 36.7%. Consolidated effective rate 27.5% against SPEL standalone 24.07% (Pass 1 section 10). The reconciliation to a statutory rate remains NOT FOUND.

### N7. Corporate guarantee exposure in the consolidated Notes is wider than the contingent liability note [YELLOW]
Anchors: consolidated Note 10 (p.87); standalone Note 30.1 (p.72); consolidated Note 30.1 (p.92).

- Standalone Note 30.1 discloses one guarantee: 1,470.00 to IndusInd Bank for Danya (board resolution 28-Mar-2025).
- Consolidated Note 10 lists two State Bank of India cash-credit rows at 11.65%, each with "Corporate Guarantee by M/s Supreme Power Equipment Limited" (L8636-8647). Balances 0.07 (FY25 -10.36) and nil (FY25 0.05). Pass 1 recorded the SBI cash credit but not its guarantee. "State Bank" and "SBI" appear nowhere else in the AR (searched).
- So SPEL's guarantee covers an SBI facility to Danya that standalone Note 30.1 and AOC-2 do not show. Sanctioned limit of the SBI facility: NOT FOUND IN DOCUMENT. Whether the 14.70 Cr guarantee is meant to cover SBI as well: NOT FOUND IN DOCUMENT.
- The FY27 authority sought for guarantees up to Rs.25 Cr (Pass 1 A(a)) should be read against this.

### N8. Receivables: the over-one-year bucket was already outstanding a year ago [YELLOW]
Anchors: standalone Note 17 (p.69-70), Note 30.6 (p.72), Note 30.4 (p.72), Note 31 (p.76), Note 28 (p.71).

- Roll-forward on the printed ageing (the ageing basis, due date or invoice date, is NOT FOUND IN DOCUMENT; the logic needs only the same basis in both years): an amount in the 1-2 year bucket at 31-Mar-26 was in the under-one-year buckets at 31-Mar-25. Those buckets were 3,704.21 + 308.85 = 4,013.06. So the 588.04 now over one year (13.0% of 4,521.09) is 14.65% of what stood in those buckets a year ago, still unpaid, with no provision.
- The FY25 1-2 year bucket of 344.23 does not reappear in 2-3 years (nil). It was collected or cleared. There is no provision, no write-off and no bad-debt line in Note 28 (DERIVED: none listed). The over-one-year bucket rose 70.8% (588.04 against 344.23).
- Quarter-end books balances (Note 30.6): Mar-25 4,357.29; Jun-25 4,261.93; Sep-25 3,697.01; Dec-25 3,385.77; Mar-26 4,521.09. The Q4 rise is 1,135.32 (+33.5%). This matches the KAM risk of "volume of despatches around the reporting date" (p.56). Year-end balance therefore overstates the average level (Pass 1 days figures use year-end).
- Inventory quarter-end series (Note 30.6): Mar-25 2,253.46; Jun-25 3,125.96 (+872.50); Sep-25 3,154.44; Dec-25 3,910.10; Mar-26 4,556.25. The build is stepwise, with Q1 the largest step. It is not a year-end spike.
- Management's blanket statement (Note 30.4) says current assets realise at the amount stated. The same Notes carry "subject to confirmation" (Note 31), nil provision, and a debtor block of about 169-171 that the bank statements exclude every quarter (Pass 1 section 4). The three statements sit uneasily together. No contradiction is provable from the document.
- Related receivable: see N9.

### N9. Jai Bharath Exchangers balance roll-forward and AS 18 listing gaps [YELLOW]
Anchors: standalone Note 30.21 (p.74-75), Note 6 (p.66-67); consolidated Notes 10, 21 (p.87, p.94); CARO iii (Pass 1 section 12.2).

- Roll-forward (DERIVED, before GST): opening receivable 8.65 + sales 1.12 - purchases 153.77 - net settlements = 56.60. Rearranged, SPEL's net payments to Jai Bharath beyond FY26 purchases were at least 56.60 - 8.65 - 1.12 = 46.83. The balance rose 47.95 in a year with 1.12 of sales. The document does not say whether this is a trade advance or a loan. Pass 1 flagged the mismatch; this puts a floor on it.
- Group level: consolidated receivable from Jai Bharath 85.13 (FY25 104.47) against group sales 1.12 (FY25 110.97). FY25 balance was 94% of FY25 sales. At least 84.0 of 85.13 is not FY26 trade.
- CARO iii(a), (c) report no loans or advances in the nature of loans. If any of the 46.83 is a non-trade advance to a firm in which directors are partners, it sits beside Item 9 (Section 185, Rs.75 Cr) now put to members. Classification NOT FOUND IN DOCUMENT.
- AS 18 listing gaps in Note 30.21: (a) guarantees received from KMP and others (Vee Rajmohan, K V Pradeep Kumar, Saimathy Soupramanien, Savita Pradeep, V Rajagopalan) appear only in the security column of Notes 6 and 10, not in the related-party table; (b) Savita Pradeep guarantees the IndusInd term loan and appears in the shareholding pattern as a promoter-group holder (1.13%), yet is not in the related-party list; (c) V Rajagopalan guarantees the same loan and his relationship is NOT FOUND IN DOCUMENT.

### N10. Interest on statutory dues: group wide, against a CARO statement, and a tax-payment pattern [YELLOW]
Anchors: standalone Note 26 (p.71), Note 19 (p.70), Note 12 (p.68), Note 30.1A (p.72), CFS (p.62), CARO vii(a) (L5462-5467); consolidated Note 26 (p.91).

- Group: standalone 55.34 + Danya 17.90 = consolidated 73.24 (DERIVED, 73.24 - 55.34). FY25 0.01 in both. So both entities paid statutory interest in FY26.
- CARO vii(a) says the company "is regular in depositing" undisputed statutory dues, including income tax and GST, with none over six months. A 55.34 interest charge (22.9% of finance cost, Pass 1) is not obviously compatible with "regular". The nature (income tax, GST, TDS) is NOT FOUND IN DOCUMENT.
- Pattern in the Notes that fits (inference, not stated): FY25 current tax 524.68 against advance tax 65.37 at 31-Mar-25 (12.5%). CFS tax paid FY26 661.18 = 524.68 (opening provision settled) + 136.50 (FY26 advance tax). FY26 current tax 530.75 against advance tax 136.50 (25.7%). Net tax unpaid at 31-Mar-26: 530.75 - 136.50 = 394.25, or 74.3% of the year's charge. If the interest relates to advance-tax shortfall, the same pattern repeats in FY27. The Notes do not confirm the link; it is for management to answer.
- Small print: standalone Note 30.1A shows "TDS Demand (1)" with a footnote marker and no footnote text (L6790). The consolidated copy has no marker. The footnote is NOT FOUND IN DOCUMENT.
- Tie-out noted for completeness: the 65.37 opening advance tax is carried in the "other current assets" movement (CFS 801.82), not in "taxes paid". The total of the two lines is identical either way (1,463.00), so CFO is unaffected.

### N11. Payables: the Danya balance flips between MSME and Others across years [YELLOW]
Anchors: standalone Note 10 (p.67-68); consolidated Note 11 (p.87-88); Note 30.21 (p.74-75).

- Pass 1 gave the consolidated-minus-standalone differences. The algebra, if the only eliminated payable is the one in Note 30.21: consolidated MSME = SPEL MSME - e(MSME) + Danya's own MSME, with Danya's own MSME not negative.
- FY26: SPEL others 3,074.78, consolidated others 2,627.00, so at least 447.78 of the 662.82 Danya balance sits in SPEL's "Others" (67.6%). The remainder, at most 215.04, is in MSME. Danya's own creditors are 928.78, of which MSME is 713.74 to 928.78.
- FY25: SPEL MSME 1,936.17, consolidated MSME 1,528.64, so at least 407.53 of the 575.64 Danya balance sat in SPEL's MSME class (70.8%).
- So the same counterparty balance appears to move from mostly MSME (FY25) to mostly Others (FY26). The company says prior-year figures are "regrouped / reclassified wherever necessary" (Note 33). The MSME class grew 48.7% and Others grew 101.1% in FY26 (Pass 1 table), so the two are not like for like. This feeds the MSME 45-day interest question (nil interest disclosed, Pass 1 section 8) because a class change can move an amount in or out of the 45-day test. Danya's status as MSME or not: NOT FOUND IN DOCUMENT.
- Danya's own creditors rising 3.5 times (N5) is mostly MSME by the same algebra.

### N12. A non-executive director was paid 15.00 against the Board report; resigned after year end [YELLOW]
Anchors: standalone Note 30.21 (p.74), Note 28 (p.71); consolidated Note 21 (p.94). Outside the Notes: Board report L3830-3831, L3835-3839; Notice L2188-2193, L1731-1737; profile L701-707; committees L1198-1203, L1225-1230.

- Note 30.21 shows Devaraja Iyer Krishna Iyer, non-executive non-independent director, paid 15.00 (FY25 nil). The Note 28 sitting fees of 5.60 (3.20) are only the two independent directors at 2.80 and 2.80 (1.60 each). So the 15.00 is not a sitting fee. Where it is booked is NOT FOUND (likely professional fees, 71.67 against 65.02, which rose only 6.65). The nature of services is NOT FOUND IN DOCUMENT.
- The Board report states the company "did not have any pecuniary relationship or transactions with the Non-Executive Directors ... other than payment of the sitting fees" (L3830-3831). This contradicts Note 30.21.
- He resigned with effect from 13-Aug-2026 (Notice L2188-2193). The same AR still says in the Board report that he "retires by rotation" and the Board recommended his re-appointment (L3835-3839), while Notice Item 3 resolves not to fill the vacancy (L1731-1737). The profile credits him with over four decades in transformer engineering, with TELK, AREVA, ECE Transformers and Prime Meiden roles (L701-707). He sat on the Nomination and Remuneration and Stakeholders Relationship committees. The board falls from five directors to four (L3802-3814).
- Neither set of Notes has a subsequent-events note. Pass 1 section 12.3 said the Board report shows no material change after year end. This resignation is after year end and is not in the Notes. Rating YELLOW on disclosure; the business meaning belongs to later stages.

### N13. Promoter group and warrants reconciled with the shareholding pattern [YELLOW for Note 3(f) wording, GREEN for encumbrance]
Anchors: standalone Note 3 (p.65), Note 5 (p.66), Note 30.2 (p.72), Note 30.21 (p.74); SHP 31-Mar-2026 (inputs/shareholding/SHP_31Mar2026.txt L9-29, L148-179).

- AR Note 3(f) lists two "Promoters": Vee Rajmohan 78,75,430 (31.51%) and K.V. Pradeep Kumar 51,37,905 (20.56%), total 1,30,13,335 (52.07%).
- SHP promoter and group: 14,284,665 shares (57.16%). DERIVED exact tie: 7,875,430 + 5,137,905 + R Sasikala 988,785 (3.96%) + Savita Pradeep, named "Sudhakaranpillai Savitapradeep" in the SHP, 282,545 (1.13%) = 14,284,665. Gap to the AR figure 1,271,330 shares (5.09 points) is those two holders. Their relationship to the directors is NOT FOUND IN DOCUMENT. Neither is in the Note 30.21 related-party list (see N9).
- No shares pledged or encumbered (SHP L3-8, "false"). 35% of group shares locked in (SHP L15).
- Warrants (Note 5 says "Promoter & Promoter Group" and "Non-Promoter" with no split; AR split NOT FOUND). SHP gives it: promoter side 449,500 warrants, all Vee Rajmohan (36.05% of 12,47,000); non-promoter 797,500 (613,000 resident individuals above Rs.2 lakh, 184,500 NRI). DERIVED balance due on exercise at Rs.126.75: promoter 569.74, non-promoter 1,010.83, total 1,580.57 (ties to Pass 1). Upfront 25% received: promoter 189.91, non-promoter 336.94, total 526.85 (printed 526.86). So 63.9% of the 1,580.57 yet to come rests on non-promoter holders. Exercise window ends about 26-27 Feb 2027 (18 months from 27-Aug-2025).
- Fully diluted promoter group holding: 56.16% (SHP L21).

### N14. Other expenses grew twice as fast as revenue; one line has no breakdown [YELLOW, low]
Anchors: standalone Notes 24, 25, 28 (p.70-71).

- Other expenses 557.70 against 333.13, +67.4% (revenue +31.3%). Four lines carry 198.68 of the 224.57 increase (88.5%): business promotion 98.16 (30.11, +226%), insurance 24.36 (6.84, +256%), miscellaneous 111.18 (55.70, +99.6%), transport 120.77 (63.14, +91.3%). Pass 1 listed amounts only.
- "Miscellaneous expenses" 111.18 is 19.9% of other expenses and larger than professional fees 71.67. No breakdown is given.
- Staff welfare 43.96 against 16.24 (+170.7%) while salaries rose 48.6%. Rent fell 80.6% (33.27 to 6.46) with rent advance down 17.33 to 5.93. Reason NOT FOUND (Kannur may be owned premises; not stated).

### N15. Working capital "reduction" is liability funded [YELLOW, low]
Anchors: standalone Note 34(h) (p.77); consolidated Note 33(h) (p.97).

- Net capital turnover 13.05x (FY25 6.01x) ties: sales 19,007.73 / working capital 1,456.51. Working capital = current assets 11,356.92 - current liabilities 9,900.41. FY25 7,556.35 - 5,145.98 = 2,410.37.
- Current assets rose 50.3%, current liabilities rose 92.4%. Working capital fell 39.6% only because customer advances (+1,445.75), payables (+2,489.21) and current maturities (+1,005.58) grew faster than inventory (+2,302.79) and receivables. The Note 34 text ("reduction in net working capital") and "improved collection efficiency" (Note 34(e)) describe outcomes funded by suppliers and customers. Not a mis-statement; a framing point.
- Other ratio tie-outs checked and clean: current ratio 1.15 (11,356.92 / 9,900.41); debt-equity 0.39 (4,572.70 / equity including warrant money 11,820.67); ROE 17.29% on closing equity including warrant money; trade payable turnover 3.65x; receivables turnover 4.28x (19,007.73 / average 4,439.19). The "inventory turnover (COGS/Sales)" 5.58x is sales over average inventory (19,007.73 / 3,404.86), not cost of goods sold. ROCE 17% could not be re-derived from printed definitions (derived 18.0% to 19.6% on closing capital employed); definition NOT FOUND for the standalone ratio.

### N16. Facts outside the Notes that settle Pass 1 gaps (listed so pass 3 does not treat them as Note evidence) [info]
- Kannur plant: Rs.100 Cr investment, commercial production began in FY26, capacity 2,500 to about 9,000 MVA (L858-866, L1443-1450). Notes never name it.
- Order book Rs.588.17 Cr consolidated at 27-May-2026; mix 72% power, 20% distribution, 7-8% inverter duty (L1469-1470). FY26 inflow over Rs.437 Cr (L1463-1464). Customer concentration: NOT FOUND IN DOCUMENT.
- Headcount 112 permanent, median pay rise 5.44% (L5090-5092).
- CRISIL upgrade to BBB/Stable and A3+ on 20-Mar-2026 (L1487-1488).
- The MD&A refers to segment reporting "under Ind AS 108" (L1491-1492) while the accounts are Indian GAAP (AS 17); loose wording.

---

## 3. STATUS OF THE PASS 1 NOT FOUND LIST

| Item | Status after Pass 2 |
|---|---|
| Partnership deed terms, capital ratio of Danya | Still NOT FOUND |
| Danya's auditor | Still NOT FOUND. Consolidated tax audit fees 2.00 against standalone 1.00 imply a 1.00 Danya tax audit fee inside the table (Notes 28, p.71 and p.91). No Danya statutory audit fee. |
| Danya sanctioned limits at IndusInd, and now SBI | Still NOT FOUND (N7) |
| Interest, tenor, terms of promoter loan 311.30 | Still NOT FOUND |
| ICICI fixed or floating, covenants, waivers, five-year schedule | Still NOT FOUND; table fails to reconcile (N1) |
| Capitalised borrowing cost | NOT FOUND; inconclusive tests (N4) |
| Residual value policy; inventory write-downs; warranty or LD provision; bonus; leave encashment | Still NOT FOUND |
| Customer concentration | Still NOT FOUND |
| Order backlog | Not in Notes; Rs.588.17 Cr in Board report (N16) |
| Nature and ageing of Jai Bharath receivable | NOT FOUND; floor of 46.83 non-sales movement derived (N9) |
| Receivable from Danya | Not shown; roll-forward fits a netted account (N5) |
| MSME dues beyond 45 days | Still NOT FOUND; class swing noted (N11) |
| Effective to statutory tax reconciliation | Still NOT FOUND; Danya effective rate 36.7% derived (N6) |
| Nature of interest on statutory dues | Still NOT FOUND; pattern noted (N10) |
| FY24 revenue | Not in this AR |
| Restatement specifics | Still NOT FOUND ("regrouped / reclassified", Note 33); one class swing seen in N11 |
| Location of 85.38 unutilised warrant money | Still NOT FOUND |
| Promoter and non-promoter warrant split | Answered by SHP (N13) |
| Hedging, unhedged FX | Still NOT FOUND |
| Headcount | Answered outside the Notes: 112 (N16, 0.4) |
| Kannur in Notes | Nowhere in Notes; named outside (N16) |

---

## 4. NOTES RE-READ WITH NO NEW FINDING

Standalone Notes 1, 2 (policies not already covered), 4, 5, 7, 8, 12, 14, 15, 18, 21, 22, 23, 27, 29 (EPS arithmetic checked, no new point), 30.3, 30.5, 30.7 to 30.14, 30.18 to 30.20, 30.22 to 30.24 (gratuity roll ties: 14.81 + 6.40 + 1.00 + 9.52 = 31.72), 32, 33. Consolidated Notes 1, 3, 5, 6 (minority roll ties), 8, 9, 12, 13, 15, 16, 18, 19, 23 to 25, 27 to 29, 31, 32. No contradiction or unflagged movement found in these beyond what is reported above.

---

## PASS 2 NEW FINDINGS SUMMARY (new items only)

| Rank | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | ICICI term-loan table does not reconcile: current principal 1,005.19 exceeds 12 months of EMI cash 713.28 by 291.91; stated balances 3,500.00 and 474.89 exceed what the EMIs can amortise at 9.50% by about 701; schedule, rate type, covenants NOT FOUND. | Notes 6, 9; consol 7 | YELLOW |
| 2 | DSCR 2.44x is interest plus year-end current maturities; ties to two decimals in four cases. Management's "repayment" explanation is wrong. EBITDA rose 15.2%, not "marginally". | Note 34(c); consol 33(c) | YELLOW |
| 3 | CWIP ageing is impossible: 0-1 year bucket exceeds FY26 additions by 578.08. At least 904.53 (32.3%) of CWIP is pre-FY26 against 326.45 disclosed. 48.0% of PPE additions bypassed CWIP. Plant capitalised in Q4. No overdue-project schedule. | Notes 13, 30.16 | YELLOW |
| 4 | Capex cash flow is accrual additions, so capex creditors and supplier advances sit in CFO. Commitments "Nil" against five contrary facts. Borrowing cost capitalisation cannot be proven or ruled out. | CFS; Notes 30.1B, 30.17, 29.I, 26 | YELLOW |
| 5 | 95.6% of Danya's turnover growth is sales to SPEL. 28.6% of SPEL's revenue growth is sales to Danya. Danya inventory +83.6%, external payables 3.5x. Danya balance looks like a netted account. | Notes 20, 30.21; consol 11, 16, 17, 20 | YELLOW |
| 6 | Consolidated profit and reserves equal standalone to the lakh. Danya PBT, tax and PAT derive to the AOC-1 figure. No unrealised profit eliminated. Danya effective tax 36.7%. | Consol Notes 2.2, 4, 22, 26 | YELLOW |
| 7 | SPEL corporate guarantee also appears on two SBI cash-credit rows in consolidated Note 10 and not in contingent liabilities. | Consol Note 10; Note 30.1 | YELLOW |
| 8 | Receivables: 588.04 over one year was already outstanding at 31-Mar-25 (14.65% of that cohort), nil provision. Q4 receivables jumped 1,135.32 (+33.5%). Inventory built stepwise from Q1. | Notes 17, 30.6, 30.4, 31 | YELLOW |
| 9 | Jai Bharath balance rose 47.95 on 1.12 of sales: at least 46.83 non-sales movement. Guarantees received and Savita Pradeep absent from the AS 18 list. | Notes 30.21, 6; consol 10 | YELLOW |
| 10 | Interest on statutory dues is group wide (55.34 + 17.90), set against CARO "regular in depositing". Tax paid late in FY26 (FY25 advance tax 12.5%) fits; net tax unpaid at year end 394.25. Orphan "TDS Demand (1)" footnote. | Notes 26, 19, 12, 30.1A; CARO vii | YELLOW |
| 11 | Danya payable flips class: at least 70.8% MSME in FY25, at least 67.6% Others in FY26. Not like for like. | Note 10; consol 11 | YELLOW |
| 12 | Director paid 15.00 against Board report "sitting fees only"; resigned 13-Aug-2026; Board report and Notice disagree; no subsequent-events note. | Note 30.21, 28; L3830, L2188 | YELLOW |
| 13 | Promoter group reconciles exactly: 57.16% = 52.07% + R Sasikala 3.96% + Savita Pradeep 1.13%. Promoter warrants 449,500, all Vee Rajmohan; 63.9% of pending warrant money rests on non-promoters. No pledge. | Notes 3, 5, 30.2; SHP | YELLOW / GREEN |
| 14 | Other expenses +67.4% against revenue +31.3%; four lines carry 88.5% of the rise; "miscellaneous" 111.18 has no breakdown. | Notes 24, 25, 28 | YELLOW (low) |
| 15 | Working capital "reduction" and the 13.05x net capital turnover come from liability growth; other ratios tie; ROCE not re-derivable. | Note 34(e), (h) | YELLOW (low) |
