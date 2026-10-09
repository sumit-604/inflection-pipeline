# STAGE 2 NOTES PASS 1 (FULL EXTRACTION) - SUPREME POWER EQUIPMENT LTD (SUPREMEPWR)

Run: runs/supremepwr-2026-10-06 | Run date 2026-10-06 | Model claude-sonnet-5-5 | Pass 1 of 3
Source: inputs/annual-report/Annual_Report_FY2025-26.txt (AR FY2025-26, 21st AGM notice + statements)

## 0. READING CONVENTIONS

- Unit: financial statements and every Note are in "Rs. lakhs" (face of each statement: "All amounts are in ` lakhs unless stated", standalone BS p.61, consolidated BS p.82). Figures below are Rs. lakhs unless the line says Crore. No conversion done. AGM notice items quote Rs. Crore as printed.
- Page anchors: "p.N" is the PDF page of the "[page N]" footer marker that closes the text block in the .txt (the marker is a page footer, text above it belongs to that page). Where I give "L" it is the line number in the .txt file. Notes at p.63-77 are standalone, p.83-97 consolidated.
- Rating tags: [GREEN] = clean, [YELLOW] = watch, [RED] = red flag (text tags used for the pipeline's three ratings).
- "DERIVED" = arithmetic on printed figures, formula shown. Not a company figure. "NOT FOUND IN DOCUMENT" = the disclosure is absent.
- GAAP: Indian GAAP (Accounting Standards under s.133, Companies (Accounting Standards) Rules 2021), NOT Ind AS (standalone Note 2.1, p.63; consolidated Note 2.1, p.84). So no ECL matrix, no Ind AS 116 lease liability, no fair-value hierarchy note exist. Statutory auditor: P P N and Company, Chennai, FRN 013623S, partner R. Rajaram, report dated 27-May-2026.
- Two sets read: standalone Notes 1-34 (p.63-77) and consolidated Notes 1-33 (p.83-97). The standalone and consolidated Note 30.6 (bank stock statements) carry identical standalone numbers (see 7.9).

---

## A. LOAD-BEARING FACTS FROM THE TASK (settled where the AR allows)

### A(a) Danya Electric Company

| Item | What the AR says | Anchor |
|---|---|---|
| Legal form | Partnership firm (not a company). Registration "FR/CHENNAI SOUTH/930/1983"; SPEL "associated or acquired" 01-Apr-2022 | AOC-1 Part B, p.49 (L4480-4486); AGM Item 6, p.29 (L2433, L2498) |
| SPEL stake | 90% share of PROFITS (not shares/votes). Investment carried Rs. 12,67,72,967 (Rs. 1,267.73 lakhs). SPEL's initial capital contribution Rs. 1,00,000; balance is retained profit ploughed back | Note 14, p.69; AGM notice A(2), p.29 (L2446-2450); AOC-1, p.49 |
| Other 10% | Vee Rajmohan (MD) 7.5% and K V Pradeep Kumar (WTD) 2.5%, as partners. Both are promoter-directors and 52.07% shareholders of SPEL | AGM Item 6 B(7), p.31 (L2712-2714); Item 9, p.34 (L2957-2960); Note 3(f), p.65 |
| Accounting treatment | Standalone: "Investment in Partnership Firm" 1,267.73 (FY25 1,276.96), share of profit booked in Other Income 211.51 (FY25 295.22). Consolidated: treated as SUBSIDIARY line by line under AS 21 (control by "more than one-half" of control); Note 30.10 "only one subsidiary which is a partnership firm" | Notes 14, 21, p.69-70; consolidated Note 2.2, p.83 (L8042-8056); Note 30.10, p.92 |
| Inconsistency | AOC-1 (Board report annexure) files Danya under Part B "Associates and Joint Ventures" with "Reason why not consolidated: Not applicable" and says "significant influence ... Voting power", while the accounts consolidate it as a subsidiary and the AGM notice calls it a related party under Reg 2(1)(zb). Three labels (subsidiary / associate-JV / related party) for one entity | AOC-1, p.49; Note 2.2 p.83; Item 6 p.29 | [YELLOW]
| Standalone revenue vs consolidated | Standalone revenue 19,007.73 vs consolidated 18,164.04, gap 843.69. Cause: consolidation adds Danya revenue 4,174.22 and deducts "Mutual Owings" 5,017.91 (consolidated Note 20, p.90). 19,007.73 + 4,174.22 - 5,017.91 = 18,164.04, ties to the lakh. | Consolidated Note 20, p.90; Auditor Other Matters p.78 (L7640 "revenue from operations of Rs.4,174.22 lakhs"); standalone Note 20, p.70 |
| Inter-company sales | Elimination 5,017.91 = standalone purchases from Danya 2,558.08 + standalone sales to Danya 2,459.83 (Note 30.21, p.74). DERIVED: Danya's sales to SPEL 2,558.08 / Danya turnover 4,174.22 = 61.3%; Danya external revenue = 4,174.22 - 2,558.08 = 1,616.14. Purchases elimination is 5,017.74 (consolidated Note 22), 0.17 below the revenue elimination 5,017.91 (small unreconciled gap) | Notes 20, 22, p.90; Note 30.21, p.74 |
| Direction of flow | SPEL both sells to Danya (24.60 Cr, AOC-2 Rs. 24,59,82,532) and buys from Danya (25.58 Cr, Rs. 25,58,08,295). Danya buys from SPEL and sells transformers back. No bidding; "no unrelated comparable business entities"; no external valuation or benchmarking | AOC-2, p.48 (L4403,4417); AGM Item 6 B(1), p.31 (L2621-2641, L2715-2717, L2883) |
| Minority interest line | 406.76 (FY25 368.57). Roll: 368.57 + share of profit 23.50 + additions 17.30 - transfer 2.61 = 406.76. P&L "Less: Share of Minority Interest" 23.50 (FY25 32.80). 23.50 = 10% of Danya PAT 235.01 (AOC-1 L4507 "2,35,01,161") | Consolidated Note 6, p.86; consolidated P&L p.82 |
| Danya size | Turnover 41.74 Cr, PAT 2.35 Cr, net worth 16.74 Cr (AGM). Total assets 3,195.97 lakhs (auditor Other Matters). Check: SPEL investment 1,267.73 + minority 406.76 = 1,674.49 = 16.74 Cr, ties. Check: consolidated assets 26,139.10 - standalone 24,873.69 + investment 1,267.73 + intergroup 662.82 = 3,195.96, ties to auditor's 3,195.97 | AGM Item 6 A(4)6, p.30; auditor p.78 |
| Danya rating | Long term BB-, short term A4+ (rating agency NOT NAMED in notice) | AGM Item 6 C(1), C(3), p.33 (L2902-2930) |
| Cash realisation | Net cash from firm FY26 = 211.51 (inside CFO via PBT) + 9.23 (decrease in investment, investing) = 220.74 = 104% of profit share. FY25: 295.22 + 99.78 = 395.00 = 134% | Standalone CFS p.62; Notes 14, 21 |
| Danya borrowings (DERIVED from consolidated minus standalone) | Consolidated borrowings 4,997.30 - standalone 4,572.70 = 424.60 = promoter loan 311.30 + Canara ECLGS 45.50 + IndusInd CC 67.72 + SBI CC 0.07 (sum 424.59). Danya's own bank debt is about 113 lakhs; the Rs. 14.70 Cr SPEL guarantee backs IndusInd facilities, drawn amount at year end only 67.72 (consolidated Note 10, p.87) | Consolidated Notes 7, 10, p.86-87 |
| Promoter loan into Danya | Unsecured "From Related Party" 311.30 (consolidated Note 7, p.86); RPT table "Loan Received from Partners: Vee Rajmohan 311.30" (Note 30.21, p.95). Note 7 leaves "From Directors" at nil, so the loan is labelled "Related Party" in the balance sheet note but is a director loan in the RPT table. Interest rate, tenor and repayment terms: NOT FOUND IN DOCUMENT | consolidated Notes 7, 21, p.86, p.95 | [YELLOW]
| Danya's auditor | Audit report "Other Matters" says subsidiary statements are "audited and have been furnished by the Management" and "material to the Group". The firm/auditor of Danya is NOT NAMED. | p.78 (L7638-7649) | [YELLOW]
| Partnership deed terms | Profit ratio change rights, retirement, admission, SPEL's withdrawal rights, partner capital terms: NOT FOUND IN DOCUMENT | - |
| FY27 authority sought | Material RPT with Danya up to Rs. 125 Cr for FY27 (Rs. 25 Cr guarantee + Rs. 100 Cr sale, purchase, advances, inter-corporate loans, borrowings); 68.82% of consolidated turnover, 299.47% of Danya turnover. FY26 actual purchase + sale was Rs. 50.18 Cr (25.58 + 24.60) plus 14.70 Cr guarantee. RPT 1-Apr-2026 to notice date Rs. 15.54 Cr. Source of funds for any loan: "internal accruals". | AGM Item 6, p.29-33 |
| Section 185 | Item 9 special resolution to give loans, guarantees, security to entities where directors are interested up to Rs. 75 Cr, inclusive of the 14.70 Cr already given | Item 9, p.34 (L2944-2980) |

Verdict on (a): the legal form is a partnership firm, 90% profit share held by SPEL, 10% by the two promoter-directors. CRISIL's "90% stake" matches the AR profit share. The AR does not disclose a capital ratio matching 90:10: minority capital is 406.76 of 1,674.49 total (24.3%, DERIVED) against a 10% profit share. [YELLOW]

### A(b) FY26 cash flow, debt and working capital (standalone | consolidated, Rs. lakhs)

| Item | Standalone FY26 | FY25 | Consolidated FY26 | FY25 | Anchor |
|---|---|---|---|---|---|
| Net cash from operations (CFO) | 2,773.36 | 3,530.62 | 2,590.47 | 3,768.81 | CFS p.62; consol CFS p.83 |
| Purchase of fixed assets incl. CWIP (capex) | (5,746.46) | (3,967.65) | (5,748.04) | (3,977.54) | same |
| Net cash used in investing | (5,715.19) | (3,840.98) | (5,713.05) | (3,941.66) | same |
| Net cash from financing | 3,337.49 | 885.20 | 3,517.23 | 747.23 | same |
| Net change in cash | 395.66 | 574.83 | 394.65 | 574.38 | same |
| DERIVED CFO less capex | (2,973.10) | (437.03) | (3,157.57) | (208.73) | formula CFO - capex |

Consolidated CFO 2,590.47 lakhs = Rs. 25.90 Cr; capex 5,748.04 = Rs. 57.48 Cr, matching the load-bearing figures in B00.

CFO build (standalone): PBT 2,691.87; operating profit before WC 2,963.37; inventories (2,302.79); trade receivables (163.81); other current assets (801.82); other non-current assets (222.08); trade payables +2,489.23; other current liabilities +1,455.53; provisions +16.91 (-5.21 and +22.12); cash from operations 3,434.54; tax paid (661.18). Of the 1,455.53 rise in other current liabilities, customer advances account for 1,445.75 (Note 11: 1,710.36 vs 264.61). DERIVED: CFO excluding the advance build = 2,773.36 - 1,445.75 = 1,327.61. [YELLOW]

Capex "Kannur plant": no Note names Kannur. Note 13 shows additions to CWIP/PPE that tie to the CFS: gross block + CWIP 12,050.68 (31-Mar-26) - 6,305.03 (31-Mar-25) = 5,745.65 vs CFS 5,746.46 (0.81 = deletion depreciation 0.78 plus rounding). Land additions 801.23 (of which 575.14 transferred from CWIP), buildings 1,330.85, plant and machinery 4,550.79, testing equipment 522.59, electrical fittings 409.45 (Note 13, p.68-69). CWIP closing 2,797.98 (buildings 1,258.12, P&M 685.85, testing 776.99, furniture 46.58, electrical 30.44) plus intangible under development 137.01 (software) (Note 13, p.69; Note 30.16, p.73). CWIP age: 0-1 yr 2,471.53, 1-2 yr 326.45, none older (FY25: 3,635.58 / 1,297.70 / 2.56).

Borrowings by lender/type (standalone, Notes 6, 9, p.66-67):

| Lender / instrument | 31-Mar-26 | 31-Mar-25 | Rate | Security / guarantee |
|---|---|---|---|---|
| ICICI term loan A (84 months, 72 instalments left, EMI 53.03) | 3,500.00 (per terms table) | n/d | 9.50% | Hypothecation of inventories and book debts, mortgage of immovable assets, personal guarantee Vee Rajmohan, K V Pradeep Kumar |
| ICICI term loan B (84 months, 78 left, EMI 6.41) | 474.89 | n/d | 9.50% | as above plus personal guarantee of Saimathy Soupramanien |
| ICICI long-term (BS line, non-current part) | 2,969.70 | 749.37 | | |
| Canara Bank term loan (60 months, 12 left, EMI 5.28) | 63.33 | 63.33 (non-current) | 7.50% | Hypothecation of inventories and book debts |
| IndusInd term loan (60 months, 11 left, EMI 0.96) | 10.60 | 10.60 (non-current) | 8.75% | + personal guarantees: K V Pradeep Kumar, Vee Rajmohan, Savita Pradeep, V Rajagopalan |
| HDFC vehicle loan (60 months, 28 left, EMI 1.60) | 40.46 (24.10 non-current) | 40.46 | 8.60% | Hypothecation of vehicle |
| Subtotal term debt | 4,089.28 | | | |
| Less current maturities (shown in short-term borrowings) | (1,095.48) | (89.90) | | |
| Long-term borrowings on BS | 2,993.80 | 863.75 | | |
| Cash credit Standard Chartered | 483.43 | nil | 8.17% | Hypothecation of stock and debtors |
| Cash credit IndusInd | nil | 614.48 | 11.25% (FY25) | stock and debtors |
| Cash credit ICICI | nil | 65.70 | 11.50% (FY25) | stock and debtors |
| Short-term borrowings on BS | 1,578.90 | 770.09 | | |
| TOTAL borrowings (LT + ST) | 4,572.70 | 1,633.84 | | DERIVED sum; rise 2,938.86 |

Consolidated: LT 3,311.60 (FY25 909.25) + ST 1,685.70 (FY25 965.31) = 4,997.30 vs 1,874.56 (matches 49.98 and 18.74 Cr). Additional consolidated lines: Canara ECLGS term loan 45.50 at 7.90% (100% NCGTC guarantee), promoter loan 311.30 (unsecured), IndusInd CC 67.72 at 9.50% (promoter personal guarantees and SPEL corporate guarantee), SBI CC 0.07 at 11.65% (FY25 (10.36) credit balance) (consolidated Notes 7, 10, p.86-87). Whether the ICICI rate is fixed or floating, covenants, covenant waivers, and a five-year repayment schedule beyond the current-maturity split: NOT FOUND IN DOCUMENT. No loan from directors in standalone (Note 6 "Director's Loan" nil). Standalone Note 30.25(2) says "Company does not have undrawn borrowing facilities that may be available for future operating activities" (p.76). [YELLOW]

Working capital lines (standalone, then consolidated):
- Inventory: 4,556.25 vs 2,253.46 (+102.2%); consolidated 6,209.72 vs 3,154.19 (+96.9%). Revenue growth standalone +31.3%, consolidated +22.1%. Detail 7 below.
- Trade payables: 5,954.07 vs 3,464.86 (+71.8%); consolidated 6,220.03 vs 3,153.35 (+97.3%). Detail 8.
- Trade receivables: 4,521.09 vs 4,357.29 (+3.8%); consolidated 4,684.51 vs 4,515.08. Detail 4.

### A(c) Related-party transactions in full

See section 2 (table and percentages).

### A(d) CARO, contingent liabilities, commitments, auditor

See sections 3, 12.2 and 12.3. Short answer: unmodified opinions on standalone (p.56) and consolidated (p.77), no emphasis of matter paragraph, two key audit matters (revenue recognition; inventories), CARO 2020 standalone with no adverse remark, IFC opinion unmodified, guarantee 1,470.00 is the only contingent liability, capital commitments reported "Nil".

---

## 1. ACCOUNTING POLICIES AND CHANGES

- Framework: Indian GAAP / AS, historical cost, accrual (Note 2.1, p.63). No policy changes and no estimate changes in FY26 (Notes 26, 27, p.76). [GREEN]
- Revenue: AS 9. Policy text covers "fixed price contracts ... based on contract activity" and "time-and-material contracts ... unbilled revenues", but P&L shows sale of goods 18,928.97 and sale of services 78.75 (Note 20, p.70). Revenue is on transfer of goods ("only after transfer of services to the customer" in the policy, p.63). The policy wording (electrical contractors, designers, research workers, automobiles, railway equipment) is generic and does not describe a transformer maker. Basis of revenue for goods (dispatch vs delivery vs acceptance) is given only inside the auditor's KAM (p.56) not in the policy note. [YELLOW]
- Services revenue fell to 78.75 from 754.90 (-89.6%); consolidated 93.61 vs 765.56 (Note 20, p.70; p.90). [YELLOW] (Reason NOT FOUND IN DOCUMENT.)
- Depreciation: SLM at Schedule II lives (computers 3 yrs, furniture 10, testing equipment 15, buildings 60, plant and machinery 15, electrical fittings 10, vehicles 10, software 5) (p.63). No change in lives. Residual value policy: NOT FOUND IN DOCUMENT. Depreciation on new assets "from the date of acquisition" (p.63).
- Depreciation step-up: FY26 depreciation 165.26 (FY25 38.62) on gross block that rose from 1,369.20 to 9,109.57 (PPE, Note 13, p.68). DERIVED run-rate on closing depreciable gross block (excluding land 1,098.93), straight line by the stated lives with no residual: buildings 1,450.95/60 = 24.2; plant and machinery 4,698.79/15 = 313.3; testing 1,170.34/15 = 78.0; computers 48.15/3 = 16.1; furniture 72.53/10 = 7.3; electrical 425.22/10 = 42.5; vehicles 144.64/10 = 14.5; total about 496 vs 165.26 charged. This is arithmetic illustration from printed lives, not a company figure. P&M depreciation 78.06 on additions 4,550.79 implies most plant was capitalised late in the year (DERIVED: about 1.5% of additions charged). [YELLOW]
- Capitalisation: CWIP carried at cost including "borrowing costs capitalised" (Note 2.4, p.63; 2.9, p.64). Amount of borrowing cost capitalised in FY26: NOT FOUND IN DOCUMENT. Interest expense in P&L 128.24 (FY25 157.71) while total borrowings rose 1,633.84 to 4,572.70, and "Interest Paid" in the CFS equals the P&L figure to the paisa in both years (128.24; 157.71) (p.62). [YELLOW]
- Impairment: policy only, no test assumptions; "no impairment loss" (Note 29, p.76). [GREEN]
- Inventories policy: lower of cost and NRV stated for "raw materials, consumables/spares and loose tools" only (Note 2.7, p.63). The policy does not state the valuation basis for work-in-progress (2,834.39) or finished goods (77.32), although the auditor's KAM says overhead is allocated to WIP and FG on normal capacity (p.56). [YELLOW]
- Receivables policy: provision "where there is objective evidence" (Note 2.8, p.63-64). No ECL (not Ind AS). Provision recorded: nil (Note 17, p.70).
- Employee benefits: gratuity unfunded, projected unit credit; "the Company has not adopted any policy for payment of Bonus and thus no amount has been charged to profit and loss account or provisioned in the balance sheet" (Note 2.11, p.64). Statutory bonus obligation and quantum: NOT FOUND IN DOCUMENT. Leave encashment / compensated absences: NOT FOUND IN DOCUMENT. [YELLOW]
- Warranty / liquidated damages: the auditor's KAM names "liquidated damages for delayed delivery, and provision for warranty obligations under AS 29" and the policy lists "post-sales customer support" as an estimate (p.56, p.63), yet no warranty or LD provision exists in Notes 8 and 12 (only gratuity and income tax). [YELLOW]
- Labour Codes (21-Nov-2025): impact "not material", no amount (Note 28, p.76). [GREEN]
- Ind AS 116, ROU, lease liability, discount rate: NOT APPLICABLE (AS framework). Rent expense 6.46 (FY25 33.27) (Note 28, p.71).
- Basis of consolidation: line by line; intra-group balances and unrealised gains eliminated (consolidated Note 2.2, p.83). Amount of unrealised profit eliminated in inventory: NOT FOUND IN DOCUMENT.

## 2. RELATED PARTY TRANSACTIONS (Note 30.21 standalone, p.74-75; consolidated p.94-95)

Related parties listed (standalone): Danya Electric Company (partnership firm, "Supreme have Significant Control"); Jai Bharath Exchangers (partnership firm, partners have "significant / common control", consolidated says "directors of the company are partners"); Vee Rajmohan (MD); K.V. Pradeep Kumar (WTD); Perumal Ravikumar (independent director); Devaraja Iyer Krishna Iyer (non-executive non-independent director); Saimathy Soupramanien (independent director); Priyanka Bansal (CS); Thulasiraman Boologa Nathan (CFO); R Sribarati (daughter of MD); Tarun Pradeep (son of WTD).

| Party | Relationship | Nature | FY26 (Rs. lakhs) | FY25 | YoY % (DERIVED) |
|---|---|---|---|---|---|
| Danya | 90% profit-share firm; directors are partners | Purchase of goods (standalone) | 2,558.08 | 1,278.20 | +100.1% |
| Jai Bharath Exchangers | firm where promoter-directors are partners | Purchase | 153.77 | 267.56 | -42.5% |
| Total purchases | | | 2,711.86 | 1,545.76 | +75.4% |
| Danya | | Sales | 2,459.83 | 1,164.89 | +111.2% |
| Jai Bharath | | Sales | 1.12 | 110.97 | -99.0% |
| Total sales | | | 2,460.95 | 1,275.86 | +92.9% |
| Danya | | Corporate guarantee given (IndusInd Bank, board resolution 28-Mar-2025) | 1,470.00 | 1,470.00 | 0% |
| Danya | | Outstanding PAYABLE | 662.82 | 575.64 | +15.1% |
| Jai Bharath | | Outstanding RECEIVABLE | 56.60 | 8.65 | +554.3% |
| Vee Rajmohan | MD | Remuneration | 60.00 | 60.00 | 0% |
| K.V. Pradeep Kumar | WTD | Remuneration | 54.00 | 54.00 | 0% |
| Priyanka Bansal | CS | Remuneration | 8.59 | 7.62 | +12.7% |
| Thulasiraman Boologa Nathan | CFO | Remuneration | 8.53 | 6.54 | +30.4% |
| Perumal Ravikumar | independent director | Sitting fees | 2.80 | 1.60 | +75% |
| Saimathy Soupramanien | independent director | Sitting fees | 2.80 | 1.60 | +75% |
| Devaraja Iyer Krishna Iyer | non-executive director | Fees (nature "Professional Fees & Sitting Fees") | 15.00 | nil | new |
| R Sribarati | daughter of MD | Pay | 2.46 | nil | new |
| Tarun Pradeep | son of WTD | Pay | 2.80 | nil | new |
| Total KMP/directors/relatives | | | 156.98 | 131.36 | +19.5% |

Consolidated additions (p.94-95): Jai Bharath purchases 166.19 (FY25 282.27), sales 1.12 (110.97), rental income from Jai Bharath 1.95 (5.85), receivable from Jai Bharath 85.13 (104.47), loan received from partner Vee Rajmohan 311.30 (nil). Danya drops out of the consolidated RPT table (eliminated).

RPTs as % of revenue (DERIVED, standalone): purchases from RPs 2,711.86 / purchases 17,210.72 = 15.76%; sales to RPs 2,460.95 / revenue 19,007.73 = 12.95%; Danya alone: purchases 14.86%, sales 12.94%. Gross two-way flow with RPs 5,172.81 = 27.2% of standalone revenue. Consolidated external RPT (Jai Bharath only): purchases 166.19 / 16,595.10 = 1.0%.

Observations:
- Danya flows doubled in FY26 (purchases +100%, sales +111%) while its balance sheet and the guarantee stayed flat. Pricing "conform to the prevailing market rates", no benchmarking or external valuation, no bidding (AOC-2, p.48; AGM p.31). [YELLOW]
- Payable to Danya 662.82 is shown, but NO receivable from Danya appears although SPEL sold 2,459.83 to Danya. Whether balances are netted: NOT FOUND IN DOCUMENT. Check: Danya's intergroup receivable eliminated on consolidation is 662.82 (derived in A(a)). [YELLOW]
- Jai Bharath receivable 56.60 vs FY26 sales to it of only 1.12: the balance is not explained by current-year sales. Trade vs advance, ageing: NOT FOUND IN DOCUMENT. [YELLOW]
- Loans to promoter entities by SPEL: none (CARO iii(a), p.58). Promoter loan INTO Danya 311.30 (consolidated).
- Guarantee commission payable to promoters who gave personal guarantees on ICICI and IndusInd loans: NOT FOUND IN DOCUMENT. Commission received by SPEL on its Danya guarantee: "Nil" (AGM Item 6 B(4), p.32 L2744-2746). [YELLOW]
- New related parties FY26: relatives of KMP (Sribarati, Tarun Pradeep) on payroll; non-executive director Devaraja Iyer Krishna Iyer paid 15.00 (nature of services not stated). Independent director Saimathy Soupramanien gave a personal guarantee on ICICI loan B (Note 6, p.66-67) while listed as "Independent Director"; independence consequences not discussed in the Notes. [YELLOW]
- Auditor says RPTs comply with s.177 and s.188 and are disclosed in Note 30.21 (CARO xiii, p.59). AOC-2 section 1 (not at arm's length) "NOT APPLICABLE" (p.48). Audit Committee approved Danya RPT on 09-Feb-2026 (AGM p.29 L2522-2525). Shareholder approval Item 6 pending at the 25-Sep-2026 AGM.
- Director remuneration 114.00 flat for two years and 26.4% of employee cost 431.84 (Note 25, p.71). Remuneration payable 30.19 (FY25 62.28) (Note 11).

## 3. CONTINGENT LIABILITIES AND COMMITMENTS (Note 30.1, standalone p.72; consolidated p.92)

| Nature | Standalone 31-Mar-26 | 31-Mar-25 | Stage | Company assessment |
|---|---|---|---|---|
| Claims not acknowledged as debt (IT, ESI, TDS demands) | nil | nil | n/a | n/a |
| Corporate guarantee for Danya Electric Company, IndusInd Bank, board resolution 28-Mar-2025 | 1,470.00 | 1,470.00 | continuing | AGM: "continual guarantee", extendable to Rs. 25 Cr |
| Total | 1,470.00 | 1,470.00 | | |

- DERIVED: 1,470.00 / net worth (share capital 2,499.11 + reserves 8,794.70 = 11,293.81) = 13.0% of standalone net worth, so above the 10% single-item line. Against Danya's total assets 3,195.97 it is 46%. Against Danya's drawn bank debt at year end of about 113 (DERIVED above) the guarantee is about 13 times larger. Sanctioned limit of the IndusInd facilities: NOT FOUND IN DOCUMENT. [YELLOW]
- Consolidated: guarantees nil (intra-group, eliminated) (p.92). Consolidated Danya IndusInd CC lists "Corporate Guarantee by M/s SPEL" (p.87).
- Promoter personal guarantees: ICICI loans (Vee Rajmohan, K V Pradeep Kumar, plus Saimathy Soupramanien on loan B), IndusInd term loan (four persons), IndusInd/SBI cash credit of Danya (Notes 6, 10, p.66, p.87).
- Tax disputes: none disclosed; CARO vii(b) "no dues ... not deposited on account of any dispute" (p.59). [GREEN]
- Capital commitments: "Estimated amount of contracts remaining to be executed on capital account and not provided for: Nil" at both dates; Note 29.I(2) "no contractual commitments for the acquisition of Property, Plant & Equipment" (p.72, p.76), in a year with CWIP 2,797.98 and software under development 137.01 and an AGM raising the borrowing limit for "expansion plans" (Item 7, p.34 L3011-3014). Nil looks hard to reconcile with ongoing construction and equipment orders; reason NOT FOUND IN DOCUMENT. [YELLOW]
- Other commitments, uncalled liability: Nil. Letters of credit and bank guarantees outstanding: NOT FOUND IN DOCUMENT as a note (margin money on inland LC 43.31 and BG deposits 215.75 appear as assets, Note 15, p.69). [YELLOW]

## 4. TRADE RECEIVABLES (Note 17, standalone p.69-70; consolidated p.89-90)

Standalone, undisputed, considered good, unsecured; doubtful and disputed all nil; provision nil.

| Bucket | 31-Mar-26 | 31-Mar-25 |
|---|---|---|
| Less than 6 months | 3,848.76 | 3,704.21 |
| 6 months - 1 year | 84.29 | 308.85 |
| 1 - 2 years | 588.04 | 344.23 |
| 2 - 3 years / over 3 years | nil | nil |
| Total | 4,521.09 | 4,357.29 |

Consolidated: <6m 3,972.67 (FY25 3,464.91); 6m-1y 107.12 (705.93); 1-2y 604.72 (344.23); total 4,684.51 (4,515.08).

DERIVED ratios: standalone over 6 months 672.33 / 4,521.09 = 14.87% (FY25 15.0%); over 1 year 588.04 = 13.0% (FY25 7.9%). Consolidated over 6 months 15.2% (FY25 23.3%); over 1 year 12.9% (FY25 7.6%). Receivable days on year-end balance / revenue x 365: standalone 86.8 (FY25 109.8); consolidated 94.1 (FY25 110.8). A third year (FY24) cannot be built: FY24 revenue NOT FOUND IN DOCUMENT (FY24 closing receivable derives to 5,721.75 from the FY25 CFS decrease of 1,364.46, but no FY24 revenue is printed).

- Headline improved (days down ~23 standalone) but the over one year bucket rose 588.04 vs 344.23, and nothing was provided. Provision for doubtful debts: nil in both years (Note 17). [YELLOW]
- Single customer above 10% and customer concentration: NOT FOUND IN DOCUMENT in the Notes (revenue is described as largely State electricity utility orders in the KAM, p.56). Receivables from related parties: Jai Bharath 56.60 (standalone), 85.13 (consolidated); Danya none shown (see 2).
- Balances "subject to confirmation" (Note 31, p.76; consolidated Note 31, p.97). [YELLOW]
- Bank stock-statement reconciliation (Note 30.6, p.72): book debtors exceed what was submitted to banks by 168.82 (Jun-25), 168.82 (Sep-25), 168.41 (Dec-25), 171.02 (Mar-26), 3.78%-4.97%. The company explains it as "adjustments relating to provisions and valuations recorded only upon finalisation", but no receivable provision exists, and the near-constant 168.8 gap suggests a fixed block excluded from the bank statement. [YELLOW]
- DSO and ECL adequacy: no matrix (AS framework). The reported trade receivables turnover 4.28x (FY25 2.87x), attributed to "improved collection efficiency" (Note 34(e), p.77). [GREEN] for the headline, see ageing caveat above.

## 5. INVENTORY (Note 16, standalone p.69; consolidated p.89)

| Category | Standalone 31-Mar-26 | 31-Mar-25 | YoY (DERIVED) | Consolidated 31-Mar-26 | 31-Mar-25 |
|---|---|---|---|---|---|
| Raw material | 1,606.69 | 620.04 | +159.1% | 1,920.76 (raw material and consumables) | 879.78 |
| Work in progress | 2,834.39 | 1,475.63 | +92.1% | 3,877.15 | 2,038.54 |
| Finished goods | 77.32 | 150.58 | -48.7% | 411.81 | 235.86 |
| Consumables, stores, spares | 37.85 | 7.20 | +425.7% | in raw material | |
| Total | 4,556.25 | 2,253.46 | +102.2% | 6,209.72 | 3,154.19 |

- Revenue growth +31.3% standalone, +22.1% consolidated. Closing inventory / revenue x 365 (DERIVED): standalone 87.5 days (FY25 56.8); consolidated 124.8 days (FY25 77.4). The company's own ratio: inventory turnover 5.58x vs 8.01x standalone, 2.89x vs 4.32x consolidated, "higher average inventory" (Note 34(f), p.77; consolidated Note 33(e), p.97). [YELLOW]
- Inventory carries finished goods only 77.32 standalone, so the build is raw material and WIP, in line with an order book not yet dispatched, but order backlog is not in the Notes: NOT FOUND IN DOCUMENT.
- Write-downs / NRV provisions / obsolescence: NOT FOUND IN DOCUMENT (none disclosed). The KAM names "slow-moving, non-moving and obsolete components, including items held against orders that have since been amended or cancelled" as a risk area (p.56). [YELLOW]
- Danya holds WIP and FG at group level: consolidated minus standalone WIP 1,042.76 and FG 334.49 (DERIVED).
- Auditor: inventory with third parties "substantially confirmed"; no discrepancies of 10% or more (CARO ii(a), p.58).
- Stock statement to banks: Mar-26 submitted 4,599.83 vs books 4,556.25 (+43.58, 0.96%) (Note 30.6, p.72).

## 6. INVESTMENTS (Note 14, p.69; Note 30.30)

- Only investment: "Investment in Partnership Firm" 1,267.73 (FY25 1,276.96): this is Danya (AOC-1: Rs. 12,67,72,967). Carrying value movement = capital contribution (initial Rs. 1,00,000) plus accumulated profit share less withdrawals (Notice p.29). No impairment. FY26 profit share booked 211.51 vs FY25 295.22 (-28.4%) (Note 21, p.70). Share of profit = 10.3% of standalone PAT 2,044.06 (DERIVED).
- Subsidiary count: one (Danya). JVs and associates: none other. New entities: none. Loss-making subsidiaries: none (Danya PAT 235.01).
- ICDs / loans given: none during year (CARO iii(a), p.58); Note 30.12 no intermediary lending (p.72-73). Consolidated has no non-current investments line.
- Unrealised gains/losses on investments: not applicable. Note 30.30 is a template list with no figures (p.76).
- Proposed: Section 186 limit increase (Item 10, notice) and Section 185 Rs. 75 Cr (Item 9, p.34): authority, not usage. [YELLOW]

## 7. BORROWINGS (Notes 6, 9 standalone p.66-67; Notes 7, 10 consolidated p.86-87)

Instrument table: see A(b). Further points:

- 7.1 Debt tripled in a year: standalone 1,633.84 to 4,572.70 (DERIVED +179.9%), consolidated 1,874.56 to 4,997.30 (+166.6%). Company's own ratio: debt/equity 0.39 vs 0.18 standalone (+119.0%), 0.42 vs 0.20 consolidated (Note 34(b), p.76; Note 33(b), p.96). [YELLOW]
- 7.2 Debt service coverage ratio 2.44x vs 10.47x standalone, 2.48x vs 8.62x consolidated, "higher repayment of debt ... while EBITDA grew only marginally" (Note 34(c), p.76). [YELLOW]
- 7.3 ICICI is now the dominant lender: 3,974.89 of 4,089.28 term debt (97.2%, DERIVED). Both ICICI loans 84 months at 9.50%, fully secured by hypothecation and mortgage of immovable assets. Fixed vs floating: NOT FOUND IN DOCUMENT. Covenants and any waiver: NOT FOUND IN DOCUMENT. No breach disclosed; CARO ix(a) no default in principal or interest, no wilful defaulter (p.59). [GREEN] for default status.
- 7.4 Term loans were applied to purpose; no short-term funds used long term (CARO ix(c)-(d), p.59). Yet standalone current ratio fell to 1.15 from 1.47 and capex 5,746.46 was financed by term debt 2,130.06, cash credit 808.82, warrants 526.86 and supplier/customer float (CFS p.62). [YELLOW]
- 7.5 Current maturities rose to 1,095.48 from 89.90, a 12x step-up in next-year scheduled repayment. The five-year schedule: NOT FOUND IN DOCUMENT beyond instalment counts. [YELLOW]
- 7.6 Cash credit moved from IndusInd 11.25% / ICICI 11.50% (FY25) to Standard Chartered 8.17% (FY26); drawn 483.43. No undrawn facilities per Note 30.25(2). [YELLOW]
- 7.7 Related party borrowings: none standalone; consolidated 311.30 unsecured from partner Vee Rajmohan (see A(a)). [YELLOW]
- 7.8 Promoter personal guarantees on all term debt (see 3). An independent director also guarantees loan B. [YELLOW]
- 7.9 Section 180(1)(c) borrowing limit: existing Rs. 300 Cr, proposed Rs. 500 Cr; charge limit 180(1)(a) existing Rs. 300 Cr, proposed Rs. 500 Cr (Items 7, 8, p.34). Against standalone net worth 11,293.81 lakhs (Rs. 112.94 Cr). Authority only. [YELLOW]
- 7.10 Consolidated Note 30.6 reprints the standalone bank statement figures (debtors 4,521.09, inventory 4,556.25), not consolidated balances (4,684.51 and 6,209.72) (p.92-93). [YELLOW]

## 8. TRADE PAYABLES (Note 10 standalone p.67-68; Note 11 consolidated p.87-88)

| | 31-Mar-26 | 31-Mar-25 |
|---|---|---|
| MSME | 2,879.29 | 1,936.17 |
| Others | 3,074.78 | 1,528.69 |
| Total | 5,954.07 | 3,464.86 |
| Ageing 0-1 year | 5,902.39 | 3,462.23 |
| 1-2 years (others) | 51.68 | 2.63 |
| over 2 years, disputed | nil | nil |

Consolidated: MSME 3,593.03 (FY25 1,528.64), others 2,627.00 (1,624.71), total 6,220.03 (3,153.35); 1-2 yrs 61.98 (12.81).

- DERIVED payable days on purchases: standalone 126.3 (FY25 102.8); consolidated 136.8 (FY25 93.5). Company ratio: trade payables turnover 3.65x vs 4.15x (Note 34(g), p.77). [YELLOW]
- MSME share of payables 48.4% standalone, 57.8% consolidated (DERIVED). The ageing shows MSME dues entirely 0-1 year, no split at 45 days. MSMED section 16 interest paid or due: nil in both years (Note 10, p.68). Because 2,879.29 of MSME dues sit alongside an average payable period of about 126 days, whether any exceeded the 45-day statutory limit is NOT FOUND IN DOCUMENT; the note says MSME status was determined "to the extent such parties have been identified". [YELLOW]
- Payable to Danya 662.82 inside payables (class MSME or other: NOT FOUND IN DOCUMENT).
- Consolidated MSME 3,593.03 is 713.74 above standalone while "others" is 447.78 below: a reclassification between standalone and group not explained. [YELLOW]
- Balances subject to confirmation (Note 31, p.76).
- Trade payables growth (+71.8%) vs purchases growth (+39.9%, 17,210.72 vs 12,303.55) (DERIVED).

## 9. PROVISIONS

- Provisions on BS: long-term gratuity 23.87 (1.75), short-term gratuity 7.85 (13.06), short-term income tax 530.75 (524.68) (Notes 8, 12, p.67-68). Provision for income tax equals the full-year current tax charge in both years (530.75; 524.68); advance tax 136.50 is shown as other current asset, not netted (Note 19, p.70).
- Gratuity (Note 30.24, p.75-76): unfunded; obligation 31.72 (FY25 14.81, DERIVED +114%): current service cost 6.40, interest cost 1.00, actuarial loss 9.52 (FY25 0.94), expense 16.92 (3.92), benefits paid nil (0.75). Actuarial loss 9.52 is 64% of opening obligation. Assumptions: discount rate 7.10% (6.75%), salary escalation 5.00% (5.00%), attrition 10.00%, mortality IALM 2012-14. Actuary certified. Plan assets nil. Actuarial gains and losses are taken to P&L (AS 15). Consolidated obligation 33.33 (15.80). [GREEN] size, [YELLOW] 5% salary escalation looks low against a workforce growing 40%+ (employee cost 431.84 vs 307.10); headcount NOT FOUND IN DOCUMENT.
- Warranty, LD, onerous contracts, decommissioning, litigation provisions: none disclosed (see 1). [YELLOW]
- Bonus: no policy, no provision (see 1). [YELLOW]
- Provision for tax consolidated 666.50 (700.27); gratuity 7.88 (1.77) (Note 13, p.88).

## 10. DEFERRED TAX AND INCOME TAX

- Standalone DTL net 134.93 (17.87): depreciation 142.91 (21.59), gratuity -7.98 (-3.73) (Note 7, p.66). Consolidated DTL 150.11 (32.66) (Note 8, p.86). No DTA recognised or unrecognised. DTL rose by 117.06 = deferred tax charge (Note 7; P&L p.62).
- Tax expense: current 530.75 + deferred 117.06 = 647.81 on PBT 2,691.87 = 24.07% standalone (FY25 536.0 / 2,395.92 = 22.4%, DERIVED: 524.68 + 11.20 = 535.88). Consolidated 666.28 + 117.45 + 0.37 = 784.10 / 2,851.66 = 27.5% (FY25 712.17 / 2,605.00 = 27.3%). Statutory rate not stated; Note 30.22 says "Company has opted for special rate of tax of the Income Tax Act, 1961. Hence, MAT asset is not recognised" (p.75). Effective vs statutory reconciliation: NOT FOUND IN DOCUMENT. The Danya profit share 211.51 is inside standalone PBT. [YELLOW]
- MAT credit: not recognised (special rate regime). No tax dispute.
- Interest on statutory dues: 55.34 in finance cost (FY25 0.01); consolidated 73.24 (0.01) (Note 26, p.71; p.91). Which statute (income tax advance tax, GST, TDS), period, and whether paid: NOT FOUND IN DOCUMENT. CARO vii(a) reports no undisputed dues outstanding over six months (p.59). Interest on statutory dues = 22.9% of standalone finance cost 241.58 (DERIVED). [YELLOW]
- GST input tax credit 767.63 (233.21) in other current assets, +534.42, 4.0% of revenue (DERIVED); consolidated 872.89 (260.82); GST payable nil (Notes 19, 11, p.68-70). Utilisation or refund timeline: NOT FOUND IN DOCUMENT. [YELLOW]

## 11. REVENUE DETAILS

- Disaggregation: sale of goods 18,928.97 (13,724.93), sale of services 78.75 (754.90), total 19,007.73 (14,479.83) (Note 20, p.70). Consolidated gross goods 23,088.34 (16,549.23), services 93.61 (765.56), less mutual owings (5,017.91) (2,443.09) = 18,164.04 (14,871.70) (p.90). FY25 intra-group elimination was 2,443.09, FY26 5,017.91: elimination more than doubled (DERIVED +105.4%) against consolidated revenue +22.1%.
- Standalone revenue growth +31.3% vs consolidated +22.1% (DERIVED): the gap is the larger intra-group volume.
- Product, geography, customer disaggregation, top-customer revenue, order backlog, unsatisfied performance obligations: NOT FOUND IN DOCUMENT. Single segment (transformers and electrical transmission equipment) (Note 32, p.76; policy 2.19, p.64). Note 30.15 says "gross income derived from goods & services" 19,007.73, same as revenue (p.73).
- Contract liabilities (customer advances): 1,710.36 vs 264.61 (6.5x); consolidated 1,719.15 vs 276.37 (Note 11, p.67; Note 12, p.87). Advances equal 9.0% of standalone revenue (DERIVED). Terms (milestone, utility advance) NOT FOUND IN DOCUMENT. [YELLOW]
- Advances paid to suppliers: 320.30 vs 18.00 (Note 19, p.70). [YELLOW]
- Exports: FOB 103.83 shown in the foreign earnings table with total "-" for FY26 and 103.83 for FY25 (the layout is ambiguous; forex loss on exports was in FY25) (Note 30.17, p.74). Imports of capital goods CIF 105.34 in FY26 (nil FY25). Hedging policy and unhedged exposure: NOT FOUND IN DOCUMENT.
- Other income: standalone 233.51 (355.61) = share of Danya profit 211.51, interest 20.43, other 1.57 (Note 21, p.70). Consolidated 46.12 (81.80) (p.90). Danya profit share is 90.6% of standalone other income (DERIVED).

## 12. OTHER CRITICAL NOTES

### 12.1 Share capital, warrants, EPS
- Share capital unchanged at 2,49,91,135 shares of Rs. 10 (2,499.11). Promoters hold 1,30,13,335 shares (52.07%): Vee Rajmohan 31.51%, K.V. Pradeep Kumar 20.56%, no change in the year (Note 3, p.65). Listed on NSE SME 29-Dec-2023, IPO 71,80,000 shares at Rs. 65 (premium Rs. 55) (Note 1, p.63).
- Preferential warrants: 12,47,000 allotted 27-Aug-2025 at Rs. 169 each (Rs. 42.25 upfront = 25%; Rs. 126.75 on exercise), total consideration 2,107.43, received 526.86, 18-month exercise window (Note 5, p.66; Note 30.2, p.72; CARO x(b), p.59). DERIVED: balance receivable 12,47,000 x 126.75 = 1,580.57 lakhs, due by about 26-Feb-2027 (18 months from 27-Aug-2025); dilution 12.47 lakh / 249.91 lakh shares = 4.99%. Utilisation: 441.48 used, 85.38 unutilised, no deviation (Note 30.2). Where the unutilised 85.38 is held: NOT FOUND IN DOCUMENT. Split between promoter group and non-promoter allottees: NOT FOUND IN DOCUMENT. [GREEN] utilisation, [YELLOW] 1,580.57 not yet received while capex already spent.
- EPS: basic 8.18 (7.44), diluted 8.15 (7.44); dilutive warrants 0.76 lakh weighted shares; same standalone and consolidated because attributable profit is the same 2,044.06 (Note 29, p.71; p.92). No ESOP. [GREEN]
- No direct debits or credits to reserves bypassing P&L: reserves roll shows only profit (Note 4, p.66). Securities premium 3,465.83 unchanged. [GREEN]

### 12.2 Auditor, CARO, internal control (load-bearing d)
- Auditor: P P N and Company, FRN 013623S, peer review certificate 020690, partner R. Rajaram (M. No 238452). Appointed at the 18th AGM (29-Sep-2023) for five years to the 23rd AGM in 2028 (Board report p.42 L3755-3758). Reports dated 27-May-2026, UDIN standalone 26238452RMNJTR8572, consolidated 26238452NPWLWY2673 (p.58, p.80).
- Opinion: unmodified, true and fair (standalone p.56; consolidated p.77). No emphasis of matter, no qualification, no going-concern uncertainty paragraph. Board report: no qualification, reservation or adverse remark (p.42 L3763-3765). [GREEN]
- KAMs: (1) revenue recognition (price variation claims, liquidated damages, warranty, cut-off); (2) inventories (existence, valuation, NRV for slow-moving components, "items held against orders that have since been amended or cancelled") (p.56). Same two KAMs consolidated (p.77). [YELLOW] for the KAM text on amended or cancelled orders.
- CARO 2020 (standalone Annexure A, p.58-60): PPE and title deeds in company name, no revaluation; inventory verified, no 10% discrepancy; working-capital quarterly returns "materially in agreement" (ii(b)); guarantee 1,470 lakhs to Danya, no loans (iii); no deposits; cost records maintained; statutory dues regular, none over six months, none disputed; no default to lenders, not a wilful defaulter; term loans applied to purpose; warrants utilised for stated purpose; no fraud, no ADT-4, no whistle-blower complaints; RPTs compliant; internal audit system adequate; no cash loss in two years; xix no material uncertainty on meeting liabilities within one year, with the usual not-an-assurance sentence; CSR no unspent. [GREEN]
- Note: CARO ii(b) says returns "materially in agreement" while Note 30.6 shows debtor variance of 3.78%-4.97% every quarter (see 4). [YELLOW]
- Consolidated: only the clause (xxi) statement that CARO reports of "subsidiary companies" contain no qualification, though the only subsidiary is a partnership firm (not a company) (p.80 L7731-7736). Danya's auditor not named. [YELLOW]
- IFC: adequate and operating effectively (p.60-61 standalone; p.81 consolidated). Audit trail feature operated throughout (p.58). [GREEN]

### 12.3 Going concern, liquidity, subsequent events
- Going-concern language: only the basis-of-preparation line and the standard audit boilerplate; no material uncertainty anywhere (Note 2.1, p.63; CARO xix, p.59-60). Going concern: NONE flagged.
- Standalone Note 30.25(2): no undrawn borrowing facilities (p.76). [YELLOW]
- Liquidity ratios: current ratio 1.15 (1.47) standalone, 1.28 (1.69) consolidated; ROCE 17% (23%); ROE 17.29% (20.11%); net profit margin 10.75% (12.85%) (Note 34, p.76-77; Note 33, p.96-97).
- Events after balance sheet date: no note on subsequent events in either set of Notes. Board report: no material changes or commitments between year end and report date (p.40 L3594-3599). [GREEN]
- Cash and cash equivalents 973.79 (578.13), all in current accounts (Note 18, p.70). Non-current fixed deposits 224.63 (61.19) held as margin or BG deposits within other non-current assets (Note 15, p.69). Restricted nature of the FDs and the 43.31 LC margin: not shown as restricted cash; classification as non-current only.

### 12.4 CSR
- Required 36.97, spent 37.00, excess 0.03 (FY25 21.47 = 21.47); no related-party trust; no unspent (Note 30.13, p.73). [GREEN]

### 12.5 Property, plant and equipment and other balance sheet items
- Gross PPE 9,109.57 (1,369.20) incl. land 1,098.93; net PPE 8,664.94 (1,088.53); intangible software 5.61; CWIP 2,797.98; IAUD 137.01 (Note 13, p.68-69).
- Deletions: gross 5.92 (P&M 5.30, vehicles 0.62), depreciation on deletion 0.78. Sale proceeds 1.60, profit 1.57 (CFS, Note 21). Vehicle: NBV 0.03, so 1.60 - 0.03 = 1.57 ties. The P&M deletion (NBV 5.30 - 0.19 = 5.11, DERIVED) has no proceeds and no loss visible in P&L; disposition NOT FOUND IN DOCUMENT. Small. [YELLOW]
- Other non-current assets 643.50 (421.42): EMD 143.91, bank guarantee deposits 215.75, FD 224.63, margin money 43.31 and small items (Note 15, p.69). Consolidated 823.19 (557.48). EMD and BG deposits rising with tender activity (consolidated 536.71 vs 423.46).
- Other current liabilities 1,828.83 (373.29): customer advances 1,710.36; salary payable 45.02; director remuneration payable 30.19 (Note 11, p.67).
- Other expenses 557.70 (333.13): business promotion 98.16 (30.11), transport 120.77 (63.14), miscellaneous 111.18 (55.70), professional fees 71.67 (65.02) (Note 28, p.71). Finance cost components: interest 128.24, bank charges 58.00, interest on statutory dues 55.34 (Note 26). Audit fees 11.00 (9.50): statutory 10.00, tax audit 1.00.
- Struck-off companies, charges registration, layers, schemes, crypto, benami, undisclosed income: all nil or compliant (Note 30.5, 30.8-30.11, 30.18-30.19, p.72-74).
- Segment reporting: single segment (Note 32, p.76).

---

## PASS 1 SUMMARY: TOP 10 FINDINGS RANKED BY INVESTOR IMPORTANCE

| Rank | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | Danya Electric Company is a partnership firm, 90% profit share SPEL, 10% promoter-directors (7.5% Vee Rajmohan, 2.5% K V Pradeep Kumar). It is a related party AND consolidated as a subsidiary AND filed as an associate/JV in AOC-1. 61.3% of Danya's 4,174.22 turnover is sold to SPEL. Standalone revenue 19,007.73 exceeds consolidated 18,164.04 by 843.69 because intra-group sales of 5,017.91 are removed (ties to the lakh); intra-group elimination more than doubled (2,443.09 to 5,017.91). SPEL's initial capital was Rs. 1,00,000; profit share 211.51 is 10.3% of PAT. | Notes 14, 20, 21, 30.10, 30.21, p.69-75; consolidated Notes 2.2, 6, 20, p.83, p.86, p.90; AOC-1 p.49; AGM Item 6, p.29-33 | YELLOW |
| 2 | FY26 CFO 2,773.36 (consolidated 2,590.47) is propped by customer advances +1,445.75 and trade payables +2,489.23. CFO less capex is -2,973.10 standalone, -3,157.57 consolidated. CFO ex advance build 1,327.61. | CFS p.62, p.83; Notes 10, 11 | YELLOW |
| 3 | Borrowings 1,633.84 to 4,572.70 standalone (consolidated 1,874.56 to 4,997.30); ICICI 3,974.89 at 9.50%, all promoter-guaranteed (one guarantor is an independent director); no undrawn facilities; DSCR 10.47x to 2.44x; current maturities 89.90 to 1,095.48. Covenants, fixed/floating rate, schedule NOT FOUND. | Notes 6, 9, 30.25, 34; consolidated Notes 7, 10, 33 | YELLOW |
| 4 | Inventory +102.2% vs revenue +31.3% (days 56.8 to 87.5 standalone; 77.4 to 124.8 consolidated); no NRV write-down disclosed; WIP and FG valuation basis missing from policy; inventory is a KAM including "items held against orders amended or cancelled". | Notes 16, 2.7, 34(f); KAM p.56 | YELLOW |
| 5 | Corporate guarantee 1,470.00 for Danya = 13.0% of standalone net worth and 46% of Danya's total assets (3,195.97) against about 113 lakhs of Danya bank debt drawn; FY27 authority sought: RPT up to Rs. 125 Cr, guarantees to Rs. 25 Cr, Section 185 up to Rs. 75 Cr, borrowing limit to Rs. 500 Cr. | Note 30.1, 30.21; AGM Items 6, 7, 8, 9, p.29-34 | YELLOW |
| 6 | Receivables: nil provision; 1-2 year bucket 588.04 (7.9% to 13.0% of total); related-party receivable from Jai Bharath 56.60 not explained by current sales (1.12); bank stock statements run 168.82 (about 4%) below books every quarter with an explanation (provisions) that does not match a nil-provision book. | Notes 17, 30.6, 30.21, p.69-73, p.74 | YELLOW |
| 7 | Payables 126.3 days (102.8); MSME dues 2,879.29 (48.4% of payables) with no 45-day split and nil MSMED interest; consolidated MSME 713.74 above standalone while others fall 447.78. | Note 10; consolidated Note 11 | YELLOW |
| 8 | Interest on statutory dues 55.34 (FY25 0.01) = 22.9% of finance cost, unexplained; no bonus policy or provision; no warranty/LD provision despite KAM naming them; capital commitments "Nil" against CWIP 2,797.98. | Notes 26, 2.11, 12, 30.1B, p.71, p.64, p.72 | YELLOW |
| 9 | Depreciation about to step up: closing depreciable gross block implies about 496 a year (DERIVED) vs 165.26 charged; capitalised borrowing cost NOT FOUND while interest paid equals interest expense exactly; P&M depreciation implies late-year capitalisation. | Notes 13, 26, 2.3-2.9, CFS | YELLOW |
| 10 | Clean points: auditor unmodified on both sets, no emphasis of matter, CARO clean, no tax disputes, no default or wilful-defaulter, warrants proceeds used for stated purpose (441.48 of 526.86; balance 1,580.57 due by about Feb-2027), CSR met, no going-concern doubt, no accounting-policy change. | p.56-60, p.77; Notes 5, 26, 27, 30.2, 30.13 | GREEN |

Pass 1 verdict on rating balance: no [RED] finding. Ten [YELLOW] clusters, mostly disclosure gaps and growth-driven balance-sheet stretch, with the Danya structure and the debt-funded capex the two items a downstream stage must carry.

## NOT FOUND IN DOCUMENT (consolidated list for the next passes)

Partnership deed terms and capital ratio of Danya; Danya's auditor; Danya sanctioned limits at IndusInd; interest, tenor, repayment terms on the promoter loan 311.30; ICICI fixed or floating, covenants, waivers, five-year schedule; capitalised borrowing cost; residual value policy; any inventory write-down or NRV provision; warranty or LD provision; statutory bonus and leave encashment provisions; customer concentration, backlog, geography; ECL method; nature (trade vs advance) and ageing of Jai Bharath receivable; receivable from Danya; MSME dues beyond 45 days; effective-to-statutory tax rate reconciliation; nature of interest on statutory dues; FY24 revenue (3-year receivable days); restatement specifics ("regrouped / reclassified wherever necessary", Note 33 p.76, consolidated Note 32 p.97); location of the 85.38 unutilised warrant money; promoter vs non-promoter warrant split; hedging and unhedged FX exposure; headcount; where Kannur appears in the Notes (nowhere).
