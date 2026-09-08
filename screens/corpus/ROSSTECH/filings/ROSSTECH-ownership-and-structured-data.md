# ROSSTECH — ownership, market transactions, guidance and counterparties

RETRIEVED 2026-09-08 from Bull AI structured tools and one filings search. This file holds
what the first pass of this screen recorded as NOT FOUND.

## 1. PROMOTER SALE, 31 JULY 2026 — Rs 166 crore at Rs 900 a share
Source: get_company_market_transactions, recorded as bulk, block AND insider on BSE and NSE.

| Date | Party | Side | Quantity | Price | Value |
|---|---|---|---:|---:|---:|
| 2026-07-31 | Harsh Mohan Gupta & Son HUF | SELL | 15,07,859 | Rs 900 | Rs 135.71 cr |
| 2026-07-31 | Rishab Mohan Gupta (Managing Director) | SELL | 3,39,258 | Rs 900 | Rs 30.53 cr |
| 2026-07-31 | KOTAK MAHINDRA MUTUAL FUND | BUY | 18,47,117 | Rs 900 | Rs 166.24 cr |

The same two sales appear separately under event_type "insider" on both exchanges, so they
are promoter/insider disposals, not third-party trades.

**This is the only observed transaction price for this company in the whole corpus.**
It is a block trade price on 31 July 2026, not a quoted CMP on the analysis date, and must
not be treated as one.

## 2. SHAREHOLDING, pre and post that sale
Source: Disclosures under Reg. 29(2) of SEBI (SAST) Regulations 2011, Bull AI label FY2027
Q2, page 3 (documents HqjyHI, NKvu5K, nlCweK — three filings carrying the same table).

Pre-transaction:
| Holder | Shares | % |
|---|---:|---:|
| Harsh Mohan Gupta | 1,48,87,913 | 39.49 |
| Rishab Mohan Gupta | 66,62,598 | 17.68 |
| Vinita Gupta | 36,40,635 | 9.66 |
| Harsh Mohan Gupta & Son HUF | 28,75,180 | 7.63 |
| Samara Gupta | 15,536 | 0.04 |
| Harsh Samara Gupta Trust | 100 | 0.00 |
| Harsh Rishab Gupta Trust | 100 | 0.00 |
| Harvin Estate P Ltd | 1,03,724 | 0.27 |
| Bmg Investments Pvt Ltd | 12,447 | 0.03 |
| **Rossell India Limited** | **0** | **0** |
| **Total promoter and promoter group** | **2,81,98,233** | **74.80** |
| Total public | 94,98,242 | 25.20 |
| **Total shares** | **3,76,96,475** | **100.00** |

Post-transaction (same filings): Rishab Mohan Gupta 63,23,330 (16.77%); Harsh Mohan Gupta
& Son HUF 13,67,331 (3.63%); Harsh Mohan Gupta unchanged at 39.49%.
DERIVED by the reader: promoter group falls from 2,81,98,233 (74.80%) to 2,63,51,116
(69.90%).
A separate Reg. 29(1) filing (document qB5Pn3, Bull AI label FY2027 Q1) records an
"Off market - inter-se transfer by way of gift" of 200 shares.
Note: **Rossell India Limited, the former parent, holds zero shares.**

## 3. TOTAL DEBT AND RELATED PARTY, as at 31 March 2026
Source: results filing, Bull AI label "Dividend, FY2027, Q1", pages 16 (documents ToRJEk
and In3Cfi).
"C. FORMAT FOR DISCLOSING OUTSTANDING DEFAULT ON LOANS AND DEBT SECURITIES:
Loans/revolving facilities like cash credit from banks/financial institutions — Total
amount outstanding as on date (31st March 2026) — Working Capital Loans Rs. 40,940.54 Lakhs
Of the total amount outstanding, amount default as on date — Nil
Unlisted debt securities i.e. NCDs and NCRPS — Nil
**Total financial indebtedness of the listed entity including short term and long term debts
— 40,940.54 [Rs lakh, i.e. Rs 409.41 crore]**"
Related party disclosure, same page:
| Name | Relationship | Nature of transaction | Rs lakh |
|---|---|---|---:|
| Rossell Techsys Inc. | Wholly Owned Subsidiary | Sale of goods or services | 22.81 |
| Rossell Techsys Inc. | Wholly Owned Subsidiary | Purchase of goods or services | 1,721.89 |

## 4. AUDITOR "OTHER MATTER" — demerger not fully unwound
Source: same filing, page 5.
"Pursuant to the demerger, the Company, in the course of the financial year, has completed
the transfer of its registrations, assets and liabilities, including bank accounts and loan
facilities to its own name. **However, agreements for supply of goods and services to some
customers are yet to be transferred to the company from the demerged entity. Accordingly,
supplies of goods and rendering of services in respect of such customers have been routed
through the demerged entity pending amendment of agreement by the customers.**"

## 5. CORPORATE ACTIONS
Source: get_company_corporate_actions. One record only:
Dividend Re 0.20 per share, face value Rs 2, ex-date and record date 2025-09-17 (NSE).
No bonus, split, rights or restructuring recorded.

## 6. CUSTOMERS AND GROUP COMPANIES
Source: get_company_counterparties, 26 records. All disclosed in company filings.
Aerospace and defence customers: Boeing; Lockheed Martin (fighter wing industrialisation);
BAE Systems (777X howitzers, heavy duty electric vehicles); Honeywell Automation India Ltd
(HONAUT); Thales; Israel Aerospace Industries / IAI; Airbus; Hindustan Aeronautics Ltd
(HAL); Bharat Electronics Ltd (BEL); DRDO; Tata Advanced Systems; AGSS; Albatros;
InterConnect.
Space customers: SpaceX; Blue Origin.
Semiconductor and industrial customers: LAM Research, Jabil, ICHOR, TCM (all described as
"Gas Boxes / Vapor Deposition Equipment"); Amazon; GTS Global Technical Systems; Cummins
India Ltd (fossil fuel generators / offsite power units).
Group companies: Rossell India Ltd (ROSSELLIND), "Parent company from which Rossell Techsys
was demerged in August 2024"; Rossell Techsys Inc, wholly owned US subsidiary.

## 7. MANAGEMENT GUIDANCE not previously held
Source: get_company_guidance. Bull AI's own guardrail applies: "Deliveries are
self-reported statements by company management... They are not independently verified and
must not be used to confirm, verify, or corroborate whether earlier guidance targets were
met."
- Semiconductor long-term: "the target is we can do up to even US$200 million in three years
  or four years from now." (Q4FY26 call, page 14.)
- Inventory: "The idea is to keep reducing that moving forward and eventually be a 4 month
  inventory company." (Q4FY26 call, page 7.)
- CFO Jayanth V: "we are advancing focused capital initiatives aimed at reducing debt,
  strengthening the balance sheet, improving cash flows, and enhancing near-term
  profitability." (FY26 Q4 presentation, page 9.)
- FY26 delivery, from a presentation not previously held (document mskraR): "EPS FY26 Rs
  5.50 vs Rs 1.96 in FY25", "Rs 5.50 EPS on face value of Rs 2", "EBITDA FY26 Rs 66.6 Cr up
  73% YoY".
- Q1FY26 presentation (document tMDgD3): "our headcount has increased from 680 to 950";
  "Our customer base has grown from just 2 in 2022 to around 30 today, with 26+ active
  engagements"; Q1FY26 EBITDA margin 13.52% vs -1.19% a year earlier.

## 8. READER DERIVATIONS from the above, arithmetic shown
- Market capitalisation at the 31 July 2026 block price: 3,76,96,475 shares x Rs 900 =
  **Rs 3,393 crore.**
- Trailing price to earnings on FY26 EPS of Rs 5.50: 900 / 5.50 = **164x.**
- Promoter group after the sale: 2,81,98,233 less 18,47,117 = 2,63,51,116 = **69.90%.**
- Total debt of Rs 409.41 crore against FY26 standalone revenue of Rs 485.23 crore = **84%
  of one year's revenue.**
All four are derived, not disclosed. The Rs 900 is a transaction price on one date.
