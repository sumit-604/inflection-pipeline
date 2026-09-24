# ORCHPHARMA: FY2025-26 Annual Report extraction (Halt 1 stress-test)

Requested by: Claude web, 24-Sep-2026. Answered by: Claude Code, 24-Sep-2026.
Run folder: runs/orchpharma-2026-09-06

## STEP 0. Corpus check

| Item | Value |
|---|---|
| Folder | runs/orchpharma-2026-09-06/inputs/annual-report/ |
| Files | Annual_Report_2024.pdf, Annual_Report_2025.pdf, 9173803d-c576-421f-8c50-d8a9d14f5590.pdf (new) |
| New file | 9173803d-c576-421f-8c50-d8a9d14f5590.pdf, 20,406,223 bytes, on origin/main at commit 85a89b6 ("Add files via upload") |
| Pages | 353 |
| Report | Orchid Pharma Limited, 33rd Annual Report, FY2025-26 |
| Board's report | PDF p.37 to p.72. Signed "Place: Gurugram / Date: September 03, 2026" (PDF p.72) |
| Annexures | AOC-2 and remuneration annexure dated August 14, 2026 (PDF p.126, p.185) |
| Financial statements | Revised standalone and revised consolidated FS, auditor's revised reports dated August 14, 2026 (PDF p.200). The first reports were dated May 25, 2026 and are superseded |
| AGM | September 29, 2026, 12:00 noon; e-voting cut-off September 22, 2026 (PDF p.105) |
| AGM notice | **NOT IN THE PDF.** The contents page (PDF p.3) lists "04 NOTICE", but the file ends at p.353 with the consolidated notes. H3 and the E1 ceilings cannot be answered from the corpus |

OCR audit. The PDF is image-only. Page 1 has a thin text layer; pages 2 to 353 have none. Every page was re-OCR'd (tesseract 5.3.4, 200 dpi). OCR garbles table digits, so every table figure below was read from the rendered page image, not from OCR text.

Conventions. "AR26" = 9173803d-c576-421f-8c50-d8a9d14f5590.pdf. Page = PDF page index. The printed footer is one less (PDF p.270 prints "269"). Figures are Rs lakhs unless marked cr. "SA" = STANDALONE, which includes merged Dhanuka Laboratories from the appointed date 1-Apr-2024. "CON" = CONSOLIDATED. FY25 = restated comparative. [computed] = my arithmetic on quoted figures. [inference] = my reading, not filed.

---

## SECTION A. The merger

**A1. Scheme accounting.**
> "The Transferee Company has recorded all the assets, liabilities and reserves of the Transferor Company vested in it pursuant to this Scheme, at their book values and in the same form as appearing in the books of the Transferor Company as on the Appointed Date, by applying the principles as set out in Appendix C of IND AS 103 'Business Combinations'" (AR26, SA Note 58(b)(i), p.270; CON Note 57(b)(i), p.351)

- Net identifiable assets acquired 28,669.54, less cost of investments in merged undertaking 4,458.60, gives net impact on Other Equity 24,210.94 (AR26, SA Note 58, p.271-272; CON Note 57, p.351-352).
- Goodwill: none. No goodwill line exists.
- SOCE split (AR26, SA SOCE, p.216):

| Reserve line | Amount |
|---|---|
| Capital Reserve on Amalgamation | (5,353.03) |
| Securities Premium | +5,120.69 |
| Capital Redemption Reserve | +195.05 |
| OCD equity component | (6,856.06) |
| General Reserve | +7,223.90 |
| Retained earnings | +23,880.39 |

Comment: this is pooling at book value. A negative capital reserve of 5,353.03 arose. Policy text is at p.233.

**A2. The 3,54,19,957 cross-held shares.**
> "Less: Cancellation of 3,54,19,957 Existing Shares ... (3,542.00)" (AR26, SA Note 19, p.240-241)
> "Additionally the Cross holding of 35419957 equity shares of DLL was cancelled pursuant to the terms and conditions of the Scheme." (AR26, Board's report, p.53)

Comment: the shares were cancelled. Note 58(b)(iv) (p.271) states that shares held by the transferor are adjusted against share capital. The Board's report says "equity shares of DLL". The shares were Orchid shares held by DLL. This is a drafting error in the report.

**A3. The 14,300 OCDs.**
> "the Optionally convertible debentures held by the Transferor Company were nullified and the balance was transferred to the General Reserve" (AR26, SA Note 20(d), p.243)

- OCD equity component 6,856.06 was removed and the General Reserve took the balance (SOCE p.216).
- Note 58(b)(iii) says intercompany obligations are discharged on merger.
- Note 21 (p.244), unsecured "Others": 1,000.00 at FY25, nil at FY26.
- Carrying value of the liability component at extinguishment: NOT DISCLOSED. It would sit in the Note 58 appointed-date balance sheet or the Note 20(d) reconciliation.

Comment: the OCDs no longer exist. They carry no holder, conversion terms or redemption premium.

**A4. Share count.**

| Line | Shares | Source |
|---|---|---|
| Outstanding before scheme | 50,719,105 | SA Note 19, p.241 |
| Less cancelled cross-holding | (35,419,957) | SA Note 19, p.241 |
| Add allotted to DLL shareholders, August 1, 2026 | 44,586,052 | SA Note 19, p.241; Board's report p.53 |
| Total | 59,885,200 | SA Note 19, p.241; Note 42 (EPS), p.250 |

> "Accordingly, 44586052 equity shares ... were allotted to the eligible shareholders of DLL in the ratio of 161 equity shares of the Company for every 5 equity shares held in DLL ... the issued, subscribed and paid-up share capital of the Company stood increased to Rs 598852000/- comprising 59885200 equity shares" (AR26, Board's report, p.53)

- Share capital suspense at 31-Mar-2026: Rs 4,458.61 lakhs, "Shares since allotted on August 1, 2026" (SA Note 19, p.241).
- Weighted shares for FY26 EPS: 59,885,200 (SA Note 42, p.250).
- Top holders after allotment (SA Note 19, p.241): Triveni Trust 32.62%, Manish Dhanuka 10.94%, Pushpa Dhanuka Trust 9.68%, Mamta Dhanuka 5.20%, Arjun Dhanuka 4.82%, Quant MF 5.79%.

Comment: reconciles exactly to 5,98,85,200.

**A5. Valuer and fairness opinion.** NOT DISCLOSED. Would be in the scheme document, the NCLT first-motion filing, or the stock-exchange scheme filing of December 2023.

**A6. DLL's own contribution.** NOT DISCLOSED. The report gives only the appointed-date balance sheet (p.271-272). DLL's own FY26 or FY25 revenue, EBITDA or profit would be in DLL's standalone filings or the scheme valuation report.

---

## SECTION B. Other income and EBITDA

**B1. Other income, line by line.**

| Line | SA FY26 | SA FY25 | CON FY26 | CON FY25 |
|---|---|---|---|---|
| Interest on bank deposits "etc." | 2,353.37 | 2,448.89 | 805.04 | 2,025.88 |
| Interest on income tax refunds | 89.11 | 29.95 | 89.11 | 29.95 |
| Profit on sale of PPE | 844.85 | – | 844.85 | – |
| Foreign exchange gain (net) | 1,499.95 | 886.54 | 1,499.95 | 886.54 |
| Corporate guarantee commission | 456.53 | 22.43 | not a line | not a line |
| Other non-operating income | 404.88 | 255.37 | 402.88 | 255.37 |
| **Total** | **5,648.69** | **3,643.18** | **3,641.83** | **3,197.74** |

Sources: AR26, SA Note 32, p.247; CON Note 30, p.324.

- Interest from Orchid Bio-Pharma: not a separate line. The RPT note gives interest received from OBPL 1,412.02 (FY26) and 466.35 (FY25) (SA related-party note (e), p.260). [inference] It sits inside "Interest on bank deposits etc." in SA, and it is eliminated in CON. That explains why SA 2,353.37 falls to CON 805.04.
- Guarantee commission: Note 32 books 456.53. The RPT table shows "Corporate Guarantee commission received" 834.10 (FY25: 527.72) (p.260). Receivable 195.51 (p.261). Unearned liability 211.55 (Note 24, p.245). [inference] The gap is Ind AS 109 amortisation over the guarantee life.
- Government grants: no other-income line. Export promotion incentives sit in revenue: 318.61 / 347.75 (SA Note 31, p.247; CON Note 29, p.324).
- Unrealised forex gain in SA cash flow: 739.71 / 430.67 (p.213).

**B2. EBITDA and margin as stated.**
> "During the year ended March 31, 2026, EBITDA of the Company stood at Rs 94.27 crore as compared to Rs 187.14 crore during the previous year" (AR26, MD&A, p.83)

| Rs cr (SA) | FY24 | FY25 | FY26 | Source |
|---|---|---|---|---|
| Operating revenue | 819.37 | 1,397.61 | 1,232.78 | MD&A p.83 |
| EBITDA | 141.07 | 187.14 | 94.27 | MD&A p.83 |
| PBT before exceptional | 91.52 | 132.45 | 41.95 | MD&A p.83 |
| EPS Rs | 19.59 | 23.69 | 5.78 | MD&A p.83 |
| Operating profit margin % | – | 11.07 | 3.54 | MD&A p.86 |
| Net profit margin % | – | 10.20 | 2.81 | MD&A p.86 |

- Board's report table (p.38): PBDIT SA 94.27 / 187.14 cr; CON 69.99 / 176.33 cr.
- Definition: none given. The figures include other income. SA 94.27 cr includes Note 32 other income of 56.49 cr.
- EBITDA ex other income [computed]: SA FY26 37.78 cr (3.1% of revenue); SA FY25 150.71 cr (10.8%). CON FY26 33.57 cr; CON FY25 144.35 cr.
- "Operating profit margin 3.54%" matches neither 94.27 cr (7.6%) nor 37.78 cr (3.1%). Its definition is NOT DISCLOSED.
- Exceptional item: Rs 7.33 cr for Labour Code gratuity and leave (MD&A p.83; Note 55, p.269-270: 733.29 lakhs).
- Guidance in the report: Rs 1,400-1,500 cr revenue and Rs 200-250 cr EBITDA (p.16, p.22).

Comment: Correction 14/15 holds. Operating EBITDA is about 38 cr, not 94 cr, and the reported margin mixes in treasury income and guarantee fees.

**B3. Inventory write-down or liquidation loss.** NOT DISCLOSED.
- Inventories (SA Note 11, p.238) show no write-down line. The policy (lower of cost and NRV) gives no amount.
- Inventories fell from 45,736.53 to 37,231.10 (SA Note 11, p.238). The cash-flow release was 8,505.43 (SA CF, p.213).
- An NRV write-down, if booked, would appear in Note 11 or in the Note 34 changes-in-inventories line. The CARE rationale is outside the corpus.

---

## SECTION C. Orchid Bio-Pharma and the 7-ACA project

**C1. Corporate guarantee.**

| Line | FY26 | FY25 | Source |
|---|---|---|---|
| Corporate guarantees for loans availed/to be availed by wholly owned subsidiary | 57,962.74 | 44,722.00 | SA Note 45, p.252 |
| Guarantee issued during year | 13,240.74 | 44,722.00 | RPT (c), p.259 |
| Unearned financial guarantee commission (liability) | 211.55 | – | SA Note 24, p.245 |

- A financial-guarantee liability IS recognised under Ind AS 109 (policy p.228; carrying amount 211.55).
- The guarantee (579.63 cr) exceeds the OBPL term-loan sanction (447.22 cr) by 132.41 cr [computed]. The facility behind the extra 132.41 cr is NOT DISCLOSED. It would be in the OBPL sanction letters or the guarantee resolution.

**C2. Loan to OBPL.**
> "The Company has not granted any loan or advance in the nature of loan to promoters, directors, KMPs and other related parties that are repayable on demand or without specifying any terms or period of repayment except loan given to Orchid Bio Pharma Limited of Rs.17,858.81 lacs (previous year: Rs. 10824.32 lacs) and Orchid Pharma Europe GMBH of Rs.390.29 lacs" (AR26, SA Note 7, p.237)

- Balance 17,858.81 / 10,824.32. Loans given in FY26: 6,622.47 (RPT (e), p.260).
- Interest booked: 1,412.02 / 466.35 (RPT (e), p.260).
- Rate, tenure, security, repayment schedule: NOT DISCLOSED. The note itself places this loan in the "repayable on demand or without specifying terms" category.
- Implied yield about 9.8% on the average balance [computed, inference].

**C3. 7-ACA project cost.** Every mention found:
- "Disclosed investment of approx. 600-700 crore, facilitated by BIRAC under the Dept. of Biotechnology" (AR26, corporate section, p.23).
- PLI: "committed capacity of 1,000 Metric Tonnes Per Annum and for a total incentive of up to Rs 600 Crores" (AR26, Board's report, p.54).
- Land: 19.79 acres, Rs 18.84 cr (p.55).
- Rs 596 cr: not found. Rs 750 cr: not found. No explanation of any cost change appears.

**C4. CWIP.**

| CON CWIP ageing | <1 yr | 1-2 yr | 2-3 yr | >3 yr | Total |
|---|---|---|---|---|---|
| 31-Mar-2026 | 31,736.25 | 2,315.86 | – | – | 34,052.11 |
| 31-Mar-2025 | 5,542.26 | 906.67 | – | – | 6,448.93 |

Source: AR26, CON Note 51(a), p.343. Overdue projects: NIL (Note 51(c), p.344).

- SA CWIP 9,499.77 (p.265).
- Split by project (Jammu 7-ACA vs cefiderocol FDF): NOT DISCLOSED.
- [inference] CON minus SA = about 24,552, most of which is the Jammu project in OBPL. The SA 9,499.77 holds the Alathur cefiderocol FDF work.
- Intangible under development (CON, p.343): 7,307.98 / 1,622.36.

**C5. Borrowing costs, PLI, COD.**
- Borrowing costs capitalised: none shown. SA Note 38 (p.248) shows "–". OBPL drew 17,790 at 9.09-9.16% during construction. [inference] Either OBPL expensed the interest or the disclosure is missing.
- PLI or interest subvention recognised or receivable: NOT DISCLOSED.
- COD: "The facility is progressing towards commercial operations in the first quarter of calendar year 2027" (AR26, MD letter, p.12).

**C6. OBPL borrowings.**
> "During the year ended March 31 2026, Orchid Bio-Pharma Limited, a subsidiary, obtained sanction of Rupee term loans from various Banks aggregating to Rs. 44,722 Lakhs with tenure of 10 years and a moratorium of 24 to 30 months. The availment of the loans as on 31.03.2026 is Rs.17790 lakhs. The rate of interest for these loans are ranging from 9.09% to 9.16%." (AR26, CON Note 47, p.330)

- Lenders: "various Banks", not named.
- Security: exclusive charge on funded assets, first pari passu on Jammu land and buildings, corporate guarantee from Orchid, personal guarantees of Manish Dhanuka and Mridul Dhanuka.
- First repayment date: NOT DISCLOSED. [inference] It falls 24-30 months after first drawal.
- OBPL other auditor (CON Other Matters, p.278): total assets 38,813.94; revenue nil; profit 7.92.
- Cross-check [computed]: CON rupee term loans 21,355.25 = OBPL 17,790 + HDFC cefiderocol 3,562 + car loan 3.26.

**C7. Capital commitments.**

| | FY26 | FY25 | Source |
|---|---|---|---|
| SA | 7,174.03 | 9,024.80 | SA Note 45, p.252 |
| CON | 37,902.13 | 29,842.89 | CON Note 43, p.328 |

**C8. QIP utilisation at 31-Mar-2026.**

| Object | Amount (Revised) | Utilised | Balance in FDs |
|---|---|---|---|
| Investment in OBPL for Jammu facility | 13,500 | 7,302 | 6,198 |
| Repayment/prepayment of borrowings | 19,546 | 19,546 | – |
| Capex, new block at Alathur API facility | 36 | 36 | – |
| General corporate purposes | 6,372 | 6,372 | – |
| **Total** | **39,454** | **33,256** | **6,198** |

Source: AR26, SA Note 57, p.270; CON Note 56, p.350.

> "the surplus amount of Rs 274 Lakhs has been included in the GCP Balance as on March 31, 2026. The Allocation among the objects has been revised vide Shareholder's resolution dated September 20, 2025" (p.270)

- Reason for the revision: NOT DISCLOSED. It would be in the 32nd AGM notice (September 20, 2025) explanatory statement.
- Pre-revision allocation per object: NOT DISCLOSED in this report.
- Earmarked FDs: SA 6,221.60 (Note 14, p.239); CON 7,345.37 (Note 13, p.316).

---

## SECTION D. Cash, working capital and debt

**D1. Trade receivables.**

| | SA FY26 | SA FY25 | CON FY26 | CON FY25 |
|---|---|---|---|---|
| Considered good | 38,135.01 | 35,305.26 | 38,135.01 | 35,305.26 |
| Credit impaired | 3,851.77 | 6,855.68 | 4,552.45 | 7,490.03 |
| ECL allowance | (3,851.77) | (6,855.68) | (4,552.45) | (7,490.03) |
| Net | 38,135.01 | 35,305.26 | 38,135.01 | 35,305.26 |

Sources: SA Note 12, p.238; CON Note 11, p.315.

Ageing at 31-Mar-2026, gross:

| Bucket | SA (p.266) | CON (p.344) |
|---|---|---|
| Not due | 26,738.47 | 26,738.47 |
| < 6 months | 8,593.86 | 8,593.86 |
| 6 months-1 year | 1,874.85 | 1,874.85 |
| 1-2 years | 1,573.82 (927.83 good + 645.99 impaired) | 1,573.82 |
| 2-3 years | 175.81 (impaired) | 175.81 |
| > 3 years | 3,029.97 (impaired) | 3,730.65 |
| Total | 41,986.78 | 42,887.46 |

SA ageing at 31-Mar-2025 (p.266): not due 25,116.10; <6m 10,120.56; 6m-1y 65.94; 1-2y 23.45; 2-3y 1.13; >3y 6,833.76; total 42,160.94.

- Bad debts written off 3,096.13 against an ECL release of 3,003.91 (SA CF, p.213).
- Comment: good receivables past 6 months rose from 68.60 to 2,802.68 [computed]. That is new slow money, not legacy CIRP debt. Receivable days 109 vs 71 (p.267).

**D2. Inventories.**

| | SA FY26 | SA FY25 | CON FY26 | CON FY25 |
|---|---|---|---|---|
| Raw materials | 13,303.22 | 14,875.69 | 13,303.22 | 14,875.69 |
| Intermediates and WIP | 13,601.98 | 19,262.98 | 13,601.98 | 19,262.98 |
| Traded goods | 317.95 | 166.76 | 317.95 | 166.76 |
| Finished goods | 8,699.47 | 10,505.64 | 8,699.47 | 10,494.81 |
| Stores, chemicals, packing | 1,308.48 | 925.46 | 1,308.48 | 925.46 |
| **Total** | **37,231.10** | **45,736.53** | **37,231.10** | **45,736.53** |

Sources: SA Note 11, p.238; CON Note 10, p.315. CON FY25 lines sum to 45,725.70 [computed], not 45,736.53, and SA Note 34 opening FG is 10,328.05 (p.247). Three different FY25 finished-goods figures exist.

**D3. Trade payables.**
- SA 27,638.05 / 28,454.95 (Note 27, p.246); MSME 1,029.75 / 1,384.89.
- CON 34,670.88 / 33,616.27 (Note 25, p.323).
- Payable days, SA: 132 / 87 (p.267).

**D4. Borrowings and cash.**

| | SA FY26 | SA FY25 | CON FY26 | CON FY25 |
|---|---|---|---|---|
| Long-term (net of current maturities) | 3,562.98 | 1,003.26 | 18,473.70 | 1,003.26 |
| Current borrowings | 8,790.88 | 14,326.23 | 11,670.17 | 14,330.63 |
| of which working capital (secured) | 6,641.68 | 7,020.70 | 6,641.68 | 7,020.70 |
| of which loans from related parties (unsecured) | 2,146.94 | 7,278.94 | 2,146.94 | 7,283.34 |
| **Total debt** [computed] | **12,353.86** | **15,329.49** | **30,143.87** | **15,333.89** |
| Cash and equivalents | 130.46 | 1,594.17 | 707.30 | 2,117.77 |
| Other bank balances (mostly QIP FDs) | 6,520.83 | 16,933.92 | 7,644.60 | 17,945.30 |

Sources: SA Notes 13, 14, 21, 25 (p.238-239, 244-245); CON Notes 12, 13, 20, 23 (p.316, 322). Lease liabilities are separate: 472.48 + 38.54.

- Lenders named: HDFC Bank (Rs 14,250 lakh term loan for the cefiderocol FDF project at Alathur, 9.10%, 12-month moratorium, 20 quarterly instalments, drawn 3,562) (SA Note 49, p.253). OBPL lenders: "various Banks" (p.330).
- Working capital lines carry personal guarantees of Manish, Arjun, Seema, Rahul, M. K. and Mridul Dhanuka (SA Note 49, p.253).
- Covenant breach: none disclosed. CARO: "the Company has not defaulted in repayment of loans or borrowings" (p.203).
- CARE rating (p.111-112): long-term bank facilities Rs 207.50 cr "Downgraded from CARE A-" to CARE BBB+; Stable. LT/ST Rs 75.00 cr to CARE BBB+ / CARE A2. ST Rs 84.00 cr CARE A2 reaffirmed.

**D5. Cash flow.**

| | SA FY26 | SA FY25 | CON FY26 | CON FY25 |
|---|---|---|---|---|
| CFO | 14,242.02 | 6,353.67 | 12,563.73 | 5,137.07 |
| of which inventory release | 8,505.43 | (6,117.97) | 8,505.43 | (6,117.97) |
| Purchase of PPE incl. CWIP | (17,182.46) | (7,202.68) | (38,962.06) | (15,359.31) |
| CFO less capex [computed] | (2,940.44) | (849.01) | (26,398.33) | (10,222.24) |

Sources: SA CF, p.213-214; CON CF, p.290-291.

Comment: FY26 CFO is inflated by a one-time inventory release of 8,505.43. Without it SA CFO is 5,736.59 [computed]. The CON CF adjustment rows are shifted by one row (for example "Interest income (0.08)", "Dividend income (818.76)"). Treat CON CF line items with care; the totals reconcile.

**D6. Schedule III ratios (SA only; the CON statements carry no ratio table).**

| Ratio | FY26 | FY25 | Change | Explanation given |
|---|---|---|---|---|
| Current ratio | 2.23 | 2.34 | (5%) | – |
| Debt-equity | 0.075 | 0.100 | (25%) | – |
| Debt service coverage | 61.55 | 66.10 | (7%) | lower profits |
| ROE | 2.2% | 10.0% | (78%) | lower profits |
| Inventory days | 123 | 94 | 31% | higher inventory, lower turnover |
| Receivable days | 109 | 71 | 54% | higher receivables, lower turnover |
| Payable days | 132 | 87 | 52% | higher payables, lower purchases |
| Net capital turnover | 2.24 | 1.45 | 54% | lower net working capital |
| Net profit ratio | 2.81% | 10.20% | (72%) | lower profits |
| ROCE | 2.54% | 9.88% | (74%) | lower profits |
| Return on investment | 1.72% | 8.49% | (80%) | lower profits |

Source: AR26, SA Note 53(j), p.267; formulae p.268. The MD&A (p.85) labels interest coverage "4.86% / 12.10%" in percent; the unit is wrong.

---

## SECTION E. Related parties

**E1. Otsuka Chemical (India).**

| | FY26 | FY25 | Source |
|---|---|---|---|
| Purchases | 24,498.98 | 35,091.23 | RPT (e), p.260 |
| Payable at year end | 6,852.38 | 9,483.68 | RPT (f), p.261 |

> "Otsuka Chemical (India) Private Limited is the only approved source of the Key Raw Material GCLE for the Company. The aggregate amount of transactions entered into during the financial year ended on March 31, 2026 was Rs. 244.98 Crore" (AR26, Form AOC-2, p.126)

- AOC-2 (p.126): relationship "two Directors of the Company are Members and one Director is a director". Nature: purchase of raw materials. Board approval February 12, 2025. Advances nil. Declared at arm's length.
- Pricing basis, benchmarking or valuation report: NOT DISCLOSED.
- FY26 approval ceiling and FY27 ceiling: NOT DISCLOSED here. They would be in the AGM notice, which is not in the PDF.
- Comment: payable 6,852.38 against purchases 24,498.98 is about 102 days [computed].

**E2. Other related-party transactions over Rs 1 cr (100 lakhs), FY26 / FY25** (RPT (e), p.260-261):

| Party | Transaction | FY26 | FY25 |
|---|---|---|---|
| Synmedic Laboratories | Sale of goods | 198.09 | 128.88 |
| Synmedic Laboratories | Lease rent received | 131.91 | 125.66 |
| Orchid Bio-Pharma | Loan given | 6,622.47 | 10,035.35 |
| Orchid Bio-Pharma | Interest received | 1,412.02 | 466.35 |
| Orchid Bio-Pharma | Guarantee commission | 834.10 | 527.72 |
| Orchid Bio-Pharma | Guarantee issued | 13,240.74 | 44,722.00 |
| Orchid Pharma Europe GmbH | Loan given | 384.09 | – |
| Dhanuka Agritech | Interest paid | 22.54 | 158.16 |
| Dhanuka Agritech | Loan repaid | 1,000.00 | 725.00 |
| Shashwat Dhanuka | Interest paid | 156.82 | 44.38 |
| Shashwat Dhanuka | Loan repaid | 2,400.00 | – |
| Mahendra Kumar Dhanuka | Interest paid | 127.83 | 130.88 |
| Mahendra Kumar Dhanuka | Loan repaid | 400.00 | – |
| Mridul Dhanuka | Interest paid | 115.66 | 130.88 |
| Mridul Dhanuka | Loan repaid | 1,745.00 | – |
| Manish Dhanuka | Loan repaid / taken | 197.00 / 130.00 | 30.00 / 300.00 |
| Arjun Dhanuka | Loan repaid / taken | 482.00 / 116.00 | 196.64 / 316.00 |
| Seema Dhanuka | Loan repaid | 154.00 | 137.00 |
| Orchid Pharma Inc | Receivable written off | – | 1,337.52 |

- Promoter-family unsecured loans outstanding (p.261): 2,146.94 (FY25: 7,278.94). Largest: Mahendra Kumar Dhanuka 1,345.00; Manish Dhanuka 670.28.
- Orbion Pharmaceuticals: sale of goods 27.27 / 10.20 (below Rs 1 cr). Share of partnership-firm loss in SA CF: 1,322.02 / 555.99; investment in partnership firm 2,290.72 (SA CF, p.213-214). The firm is not named on these pages.
- Lease rent paid to Dhanuka Agritech: 66.23 / 62.28.

**E3. KMP pay and median ratio.**

| KMP | FY26 | FY25 | Source |
|---|---|---|---|
| Manish Dhanuka, MD | 329.44 | 385.30 | RPT (e), p.261 |
| Mridul Dhanuka, WTD | 329.44 | 385.30 | p.261 |
| Arjun Dhanuka | 54.60 | 54.00 | p.261 |
| Sunil Kumar Gupta, CFO | 56.87 | 57.55 | p.261 |
| Kapil Dayya, CS | 16.45 | 15.71 | p.261 |

> MD: gross salary 168.03 lakhs, commission 161.41 lakhs; "Median remuneration of employees for the FY 2025-2026 (in Rs.)" 32300; ratio 520.22 (salary) + 499.72 (commission) = 1019.94 (AR26, Rule 5(1) annexure, p.186)

Comments:
- The ratio divides 168.03 lakhs by Rs 32,300, so it treats Rs 32,300 as an annual median. That is Rs 2,692 a month. [inference] Rs 32,300 is likely a monthly median, which would put the true ratio near 85x, not 1,020x.
- The annexure says MD total pay rose 35.96% (salary +62.41%, commission -26.45%). The RPT note shows it fell from 385.30 to 329.44. The two disclosures contradict each other.
- Median employee pay change is also stated as "(26.45%) due to the merger effect", the same figure as the commission change.
- Commission of 161.41 lakhs each was paid in a year when SA PBT fell 74%.

---

## SECTION F. Business mix and concentration

**F1. Revenue split.** The MD&A gives API only, SA:

| | FY26 MT | FY26 value | FY25 MT | FY25 value | Source |
|---|---|---|---|---|---|
| Oral API | 400.44 | 53,610 | 421.33 | 64,698.08 | MD&A p.79 |
| Sterile API | 128.54 | 23,805.96 | 154.94 | 24,609.79 | MD&A p.80 |
| API total [computed] | 528.98 | 77,415.96 | 576.27 | 89,307.87 | |

> "Oral API volumes stood at 400.44 MT ... a decline of approximately 5%, while the corresponding sales value stood at Rs 536.10 crore, compared with Rs 646.98 crore ... Sterile API volumes stood at 128.54 MT ... a decline of approximately 17%; however, sales value remained relatively resilient at Rs 238.06 crore" (AR26, MD&A, p.80)

- Realisation [computed]: oral Rs 13,388/kg vs 15,356/kg (down 12.8%). Sterile Rs 18,520/kg vs 15,883/kg (up 16.6%).
- API is 64.0% of sale of products (FY25: 64.5%) [computed].
- The remaining 43,627 (FY25: 49,084) of sale of products has no split [computed]. Formulations, trading and DLL product revenue: NOT DISCLOSED.
- Cephalosporin vs NPNC split: NOT DISCLOSED.

**F2. Top products.** NOT DISCLOSED. The MD&A names products added for new customers (Cefuroxime Axetil, Ceftibuten, Cefixime, Cefazolin, Cefepime, Ceftazidime + Avibactam) (p.80) without shares.

**F3. Geography** (SA Note 46, p.252):

| | FY26 | FY25 |
|---|---|---|
| India | 41,465.34 | 38,780.38 |
| Rest of world | 79,577.74 | 99,611.52 |
| Sale of products | 121,043.08 | 138,391.90 |
| Export share [computed] | 65.7% | 72.0% |

- Regulated vs non-regulated share: NOT DISCLOSED. The MD letter says "we expect the recovery in regulated market demand to be gradual rather than sharp" (p.13).
- New customers were added in Bangladesh, Vietnam, India, Argentina, Greece, UAE, Iran, Russia, Syria, Nigeria and Egypt (MD&A p.80).

**F4. Customer concentration.**
> "The Company does not have higher concentration of credit risks to a single customer." (AR26, SA Note 50, p.257)
> "The Company's business remains significantly dependent on strong relationships with a limited number of key customers." (AR26, MD&A risks, p.82)

Top customer and top-10 share: NOT DISCLOSED.

---

## SECTION G. Enmetazobactam and other growth lines

**G1. Allecra assets.**
- Acquisitions: Allecra SAS on 1-Aug-2025; Allecra GmbH on 29-Oct-2025, later renamed Orchid Pharma Europe GmbH (SA Note 5A, p.235; Board's report p.51, p.55).
- Consideration: NOT DISCLOSED. Board's report says it was funded from internal accruals (p.51).
- Intangible under development (CON): 7,307.98 / 1,622.36 (Note 51(b), p.343).
- Useful life and FY26 amortisation: none. The asset is still "under development", so it is not amortised.
- Patents: 141 Enmetazobactam patents (p.42). Expiry dates: NOT DISCLOSED.

**G2. Exblifep / Orblicef revenue or royalty.** NOT DISCLOSED. The report says "Early commercialisation has begun in India and Europe" (MD letter, p.12).

**G3. AMS division.** NOT DISCLOSED as numbers.
> "AMS remains small in revenue terms and its deficit are narrowing" (MD letter, p.12)

**G4. Cefiderocol.**
- Project cost and spend to date: NOT DISCLOSED.
- Debt: HDFC Bank term loan Rs 14,250 lakh sanctioned, Rs 3,562 lakh drawn at 31-Mar-2026, 9.10% (SA Note 49, p.253).
- Status: "progressing towards commissioning, with validation and regulatory submissions to follow" (MD letter, p.12). Trial batches and formulation development of Fetroja were completed (MD&A p.81).

---

## SECTION H. Audit, governance and AGM notice

**H1. Audit opinions.** Auditor: Singhi & Co., FRN 302049E, partner Sudesh Choraria, revised reports dated August 14, 2026 (p.200).
- SA: unmodified. Emphasis of matter on Note 58, the merger and the revision of the FS: "Our opinion is not modified in respect of above matter" (p.194-195).
- CON: **QUALIFIED.** Basis: Orchid Pharmaceuticals Inc, Bexel Pharmaceuticals Inc and Diakron Pharmaceuticals Inc (USA) are unaudited. Total assets 385.59 lakhs. "This has also been qualified in the Limited Review reports of the earlier quarters and audit reports of the earlier years." (p.273-274). Emphasis of matter on Note 57, the merger (p.274).
- Other matters (CON, p.278): OBPL audited by another auditor (total assets 38,813.94, profit 7.92). A second subsidiary with total assets 47.54 and a loss of 428.30 was also audited by another auditor.
- Key audit matter: one only in both reports, revenue recognition with export terms of sale (p.195, p.275).
- Audit trail: the DLL division "has used accounting software ... wherein the audit trail (edit log) feature was not enabled throughout the year under audit" (p.200).
- CARO clause (i)(b): for the DLL division, PPE "reconciliation thereof with the books of account was still in process as at year end and to that extent we are unable to comment on the discrepancies, if any" (p.200).
- CARO: no default in repayment (p.203). Statutory dues "generally regular" (p.202). Disputed dues are listed on p.202-203, including Customs Rs 14.64 lakh for FY2008-09.

**H2. Board attendance FY26.** Five meetings: May 26, 2025; July 16, 2025; August 12, 2025; November 11, 2025; February 11, 2026 (p.90).

| Director | Entitled | Attended | AGM |
|---|---|---|---|
| Ram Gopal Agarwal | 5 | 1 | No |
| Manish Dhanuka | 5 | 5 | Yes |
| Mridul Dhanuka | 5 | 5 | Yes |
| Arjun Dhanuka | 5 | 5 | Yes |
| Dr. Dharam Vir | 5 | 5 | Yes |
| Manoj Kumar Goyal | 5 | 5 | Yes |
| Tanu Singla | 5 | 4 | Yes |

Source: AR26, Corporate Governance report, p.91. Shubha Singh is listed on the board (p.90) but is missing from the attendance table. Her attendance: NOT DISCLOSED.

**H3. AGM notice resolutions.** NOT IN CORPUS. The uploaded PDF does not contain the notice. The Board's report confirms two agenda items only:
- Arjun Dhanuka's appointment as Whole-Time Director and his remuneration "are being placed before the Members for their consideration and approval at the ensuing Annual General Meeting" (p.57). Amount: NOT DISCLOSED.
- Mridul Dhanuka retires by rotation and seeks re-appointment (p.57).
- Section 180 borrowing limits, QIP/preferential/warrant enablers, and RPT ceilings: NOT DISCLOSED. They would be in the AGM notice filed with BSE/NSE for September 29, 2026.

**H4. Rs 38.72 cr lessor claim; new contingent liabilities.**
- Rs 38.72 cr: not found in this report.
- DBS lease dispute: "the Hon'ble NCLT, Chennai Bench, passed an order on June 2, 2025 disposing of the proceedings" after a Joint Memo of Compromise (Board's report, p.52). Settlement amount: NOT DISCLOSED.
- Contingent liabilities (SA Note 45, p.251-252):

| Item | FY26 | FY25 |
|---|---|---|
| Income tax dispute pending in appeal | 611.60 | – |
| GST dispute | – | 144.22 |
| Electricity Department claim | 142.11 | 112.44 |
| Customs demand at Kandla | 14.64 | 14.64 |
| Unexpired LCs and bank guarantees | 894.00 | 773.20 |
| Corporate guarantee for OBPL | 57,962.74 | 44,722.00 |

The income tax appeal of 611.60 is new in FY26.

**H5. Subsequent events** (Board's report, p.52-53, p.57):
- NCLT sanction order June 5, 2026. Scheme effective July 10, 2026, from appointed date April 1, 2024.
- Allotment of 44,586,052 shares on August 1, 2026; paid-up capital Rs 59,88,52,000.
- Arjun Dhanuka approved as Whole-Time Director, subject to members.
- Revised FS approved August 14, 2026.

**H6. Outlook.**
> "I will not offer you a forecast. I will tell you what we are watching and what we are doing." (MD letter, p.13)
> "the first quarter of the current financial year showed the direction ... Revenue grew and margins recovered meaningfully over the corresponding quarter, and the Company returned to profit. One quarter does not establish a trend" (p.13)

- Targets elsewhere in the report: revenue Rs 1,400-1,500 cr, EBITDA Rs 200-250 cr (p.16, p.22). No year is attached.
- Project dates: 7-ACA commercial operations Q1 CY2027 (p.12). Cefiderocol: validation and approvals, no date (p.12).
- Priorities: several "will contribute to earnings only from the following year" (p.13).
- Capex guidance: NOT DISCLOSED.

---

## Filing defects found (for the Halt 1 file)

1. Board's report p.38/39 gives consolidated revenue Rs 1,312.77 cr and a 6.1% decline. Tables and FS give Rs 1,232.77 cr.
2. Authorised capital 16,541 lakhs (Note 19) vs 16,451 lakhs (Note 58).
3. Guarantee commission: 456.53 in other income vs 834.10 in the RPT note.
4. FY25 finished goods: 10,505.64 (SA Note 11), 10,494.81 (CON Note 10), 10,328.05 (Note 34 opening). CON FY25 inventory lines do not cast to the total.
5. CON cash-flow adjustment rows are misaligned by one row.
6. Board's report capex passage is stale: "As on March 31, 2025 ... Rs 35.63 Crore" (p.50).
7. Snapshot (p.16) says EBITDA "up from" when it fell.
8. No borrowing cost capitalised despite 17,790 drawn by OBPL for construction.
9. MD pay: +35.96% in the Rule 5 annexure vs a fall from 385.30 to 329.44 in the RPT note. The median ratio uses an implausible Rs 32,300 annual median.
10. Board's report p.53 dates the second-motion petition "July 09, 2026", after the June 5, 2026 sanction order.
11. Shubha Singh is missing from the attendance table.
12. MD&A interest coverage is shown in percent.

---

Quoted from 9173803d-c576-421f-8c50-d8a9d14f5590.pdf, 33rd Annual Report FY2025-26 (Orchid Pharma Limited), Board's report dated September 03, 2026, 353 pages; OCR-corrupt pages rendered and read directly: the whole PDF is image-only with no usable text layer (no page carries an embedded-CORRUPT tag because none has embedded text); all 353 pages were re-OCR'd, and every figure above was read from the rendered page image at PDF p.3, 12-13, 16, 22-23, 37-44, 50-57, 72, 78-86, 90-92, 105, 111-112, 126, 186, 194-196, 200-203, 213-214, 216, 228, 233, 235, 237-241, 243-248, 250-253, 257, 259-261, 265-272, 273-275, 278, 290-291, 315-316, 322-324, 328, 330, 343-344, 350-352. The AGM notice is not in this file.
