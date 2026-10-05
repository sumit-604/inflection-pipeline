# AVANA Stage 2, Notes Triple-Pass: PASS 1 (full extraction)
Run date 2026-10-05. Model claude-sonnet-5-5. Company: Avana Electrosystems Ltd. Mode: NO-CONCALL.

## 0. CRITICAL INPUT LIMIT (read first)
The Notes to Financial Statements of the FY2025-26 AR are NOT READABLE in this run.
- AR text file: [page 99] to [page 127] (printed pp.88-116; the Balance Sheet, P&L, Cash Flow, significant accounting policies and Notes 1 to last) carry NO text. Only the page markers exist (AR txt lines 5146-5202). Auditor report, CARO Annexure A and Annexure B (pdf pp.89-98) have text.
- Page-image route failed: the Read tool on the PDF returned "pdftoppm is not installed". No Bash or OCR tool is available in this stage.
- Consequence: every note-level item below that needs the FY26 note body is marked "NOT FOUND IN DOCUMENT (AR notes image-only, pdf pp.99-127)". Nothing is estimated.
- What Pass 1 could read: (a) AR auditor report and CARO (pdf pp.89-97); (b) AR Board report, AOC-2, MD&A ratios, going concern lines; (c) face statements and certificates in the legible results re-filing (Balance Sheet, P&L, Cash Flow, WC certificate, IPO utilisation certificate, RPT Annexure D); (d) RHP restated notes for FY23-FY25 and Sep-2025 (context only).
- Action for orchestrator: Pass 2 and Pass 3 cannot recover the AR notes either unless the PDF pages are rendered to images (operator machine) or an OCR text file is supplied. Recommend an input_gap and a Halt 1 dossier line. The same figures re-filed on face statements (results file) are the only FY26 numbers in hand.
- Unit: all figures INR lakh as printed (AR, RHP, results header "Amount in INR lakhs"). Not converted. Results file is OCR text: some digits are damaged. Where a figure is cross-checked by arithmetic it is marked [ties]; where damaged and not checkable it is marked [OCR].

Anchor key: AR-aud = AR auditor report, pdf p.89-92 (printed pp.78-81); CARO = AR pdf pp.93-96 (printed pp.82-85); AR-BR = Board report; RES-p# = results re-filing 23-Jun-2026, page marker; RHP-p# = RHP page marker.

## 1. ACCOUNTING POLICIES AND CHANGES
- Framework: auditor opines under "Accounting Standards prescribed under section 133" (AR-aud, pdf p.89). RHP notes cite AS 3 and AS 20 (RHP p.232, p.16748 area, Note 22). Company reports on the AS (IGAAP) basis, not Ind AS. Ind AS 116 ROU, lease liability, ECL matrix: not applicable on this basis; the Ind AS items are NOT FOUND IN DOCUMENT. 🟢 (SME norm).
- Depreciation lives, capitalisation threshold, revenue recognition policy, impairment: NOT FOUND IN DOCUMENT (AR notes image-only). Context from RHP: inventories at lower of cost (standard weighted average) and NRV; cost includes transit insurance (RHP Note 9, p.232). 🟢
- Policy change or restatement visible on face: FY25 comparative P&L carries a "Prior period expenses, Gratuity and Leave encashment adjustment 60.17" below PBT, cutting FY25 profit to 847.08 from 907.25 pre-adjustment (PBT 1,229.88 less tax 322.64 = 907.24; less 60.17 = 847.07) (RES-p10, P&L item XI; cash flow FY25 column line "Prior Period Items" (60.17), RES-p12). This is a catch-up of employee benefit provision in FY25. Whether it is also in the RHP restated FY25 numbers: NOT checked in Pass 1. 🟡
- Depreciation fell 75.63 (FY25) to 64.63 (FY26) while gross block and CWIP rose (PPE net 317.26 to 520.10; RES-p10, p11). H1 FY26 35.21, H2 FY26 29.42 (RES-p10). Cause NOT FOUND (no PPE note). 🟡
- Audit trail: operated throughout the year for all relevant transactions, no tampering found (AR-aud 2(A)(h)(vi), pdf p.92). 🟢
- Cost records contradiction: CARO vi says the Central Government has prescribed cost records for the company's products and the auditor "broadly reviewed" them (CARO, pdf p.94). Board report says the company "is not required to maintain the cost records and accordingly ... has not maintained the Cost record" (AR-BR, printed p.40, AR txt line 2440-2444). The two statements conflict. 🟡

## 2. RELATED PARTY TRANSACTIONS (FY26; source: RPT Annexure D filed with results, RES-p18-19; AR notes RPT note NOT FOUND, image-only)
Annexure D table (INR lakh). Opening and closing balance columns are partly OCR-damaged; closing shown where legible.
| Party | Relationship | Nature | FY26 value | Opening bal | Closing bal |
|---|---|---|---|---|---|
| Panish Anantharamaiah | MD, KMP | Remuneration | 88.54 | 2.43 | 2.82 [OCR] |
| KN Sreenath | KMP | Remuneration | 62.86 | 2.17 | 2.42 |
| Gururaj Dambal | KMP | Remuneration | 74.62 | 2.63 | 2.79 |
| S Vinod Kumar | KMP | Remuneration | 63.46 | 1.64 | 2.47 |
| Amrutha Naveen | KMP (CS) | Remuneration | 4.05 | 0.00 | 0.50 |
| Ravi Kumar S | KMP (CFO) | Remuneration | 8.18 | 0.00 | 1.12 |
| Smita Dambal | Relative of director | Professional fees | 18.00 | 1.35 | 1.35 |
| Nithya M | Relative of director | Consultancy fees | 18.00 | 1.35 | 1.35 |
| G Usha | Relative of director | Consultancy fees | 18.00 (col shows 13.00 [OCR]) | 1.35 | 1.35 |
| Rama Subramanyam | Relative of director | Consultancy fees | 18.00 | 1.35 | 1.35 |
| Ramabai Dambal | Relative of director | Consultancy fees | 6.00 | 0.45 | 0.45 |
| Panish, Sreenath, Gururaj | KMP | Recovery of IPO issue expenses | 22.66 each | 0 | 0 |
| S Vinod Kumar | KMP | Recovery of IPO issue expenses | 21.15 | 0 | 0 |
| 3 independent directors | KMP | Sitting fees | 2.40 each (7.20) | 0 | 0 |
Total value of transactions reported: 476.04 (RES-p19). Sum check: remuneration 301.71 + fees to relatives 78.00 + issue-expense recoveries 89.13 + sitting fees 7.20 = 476.04 [ties].
- RPT as % of FY26 revenue from operations 8,385.88 (H1 3,574.71 + H2 4,811.17; RES-p10): 476.04 / 8,385.88 = 5.68% (derived). 🟡 (family consultancy, see below).
- Professional/consultancy fees to four relatives of directors, 18.00 each (plus 6.00 to Ramabai Dambal) = 78.00 for FY26 (RES-p18). RHP shows these relatives paid 9.00 each for the half to Sep-2025 (RHP Note 23 area, p.16978-16981, text order scrambled; per-person annual 18.00-18.60 appears at p.16972, 16989). Scope of services and arm's-length basis: NOT FOUND IN DOCUMENT. AOC-2: "no contracts ... not at arm's length basis" and material arm's-length transactions "NIL" (AR AOC-2, printed p.56, AR txt 3425-3428). 🟡
- "Recovery of issue expenses of IPO" 89.13 from four executive directors: the company recovered IPO costs from promoters (RES-p19). It indicates part of the issue expense is promoter-borne (an offer-for-sale share is implied, INFERENCE, see section 12). 🟢/🟡 neutral.
- New related parties this year: CS Amrutha Naveen and CFO Ravi Kumar S appear (RHP p.16944, 16956: CFO from 1-Sep-2025, CS from 29-Aug-2025, replacing KN Sreenath as CFO). The B00 inventory records CS resignation 30-Mar-2026 and a new CS 10-Apr-2026 (outside notes). 🟡
- Sitting fees waived 1-Apr to 30-Sep-2025 by independent directors (RHP p.16990), paid 2.40 each post listing (RES-p19). 🟢
- Loans to promoter entities: none seen. CARO iii/iv: no loans, guarantees, investments made (CARO, pdf p.94). 🟢
- Board report says no RPT with promoters/KMP that may conflict "other than the remuneration paid to the Executive Director/s and the payments made to some of the Related Parties" (AR-BR, AR txt 2709-2713). Consistent with the table. 🟢
- Remuneration to 4 executive promoter directors 289.48 combined (88.54+62.86+74.62+63.46 = 289.48, derived) = 3.45% of revenue and 24.7% of PAT 1,172.28. 🟡 (derived; Section 197 compliance confirmed by auditor, AR-aud 2(A)(g) pdf p.91.)

## 3. CONTINGENT LIABILITIES
- FY26 contingent liability note: NOT FOUND IN DOCUMENT (AR notes image-only).
- Auditor: "The Company does not have any pending litigations which would impact on its financial position" (AR-aud 2(A)(h)(i), pdf p.92). CARO vii(b): no disputed statutory dues unpaid (CARO, pdf p.94). 🟢
- Prior context (RHP summary, Sep-2025 / FY25): bank guarantees 451.91 / 485.33; letters of credit 83.92 / 509.51; TDS defaults 1.79 / 1.68; income tax outstanding demand 5.71 / 5.71; GST demand 29.33 / 29.33; total 572.67 / 1,031.56; claims not acknowledged 0.00 (RHP p.33, lines 2196-2214). Total FY25 1,031.56 = 48.7% of FY25 net worth 2,180.00 (79.41 + 2,100.59 from RES-p11 FY25 column; derived). Mostly bank guarantees and LCs (performance and supply security), not litigation. 🟡
- Cross-note tension: RHP lists income-tax demand 5.71 and GST demand 29.33 as contingent, while CARO vii(b) states no disputed dues unpaid. May mean the demands are not formally disputed or were settled; FY26 position NOT FOUND. 🟡
- Margin money against these guarantees: bank balances other than cash equivalents rose from 505.55 (FY25) to 919.17 (FY26) [derived: BS cash 2,782.78 less cash-flow cash equivalents 1,863.61; RES-p11, p13; FY25 RHP Note 11 shows margin money 505.55 held with HDFC Bank and SBI against BGs/LCs, RHP p.16587, 16615]. 🟡
- Guarantees for subsidiaries: no subsidiary (CARO ix(e), pdf p.95). 🟢

## 4. TRADE RECEIVABLES (LBF2)
- FY26 ageing schedule: NOT FOUND IN DOCUMENT (AR notes image-only). Total only: 2,221.29 at 31-Mar-2026 vs 2,119.08 at 31-Mar-2025 (+4.8%) (RES-p11; WC certificate RES-p4 agrees).
- Revenue grew 36.4% (8,385.88 vs 6,148.58; RES-p10) so closing receivables lagged revenue. Closing-balance days (derived): FY26 96.7 days; FY25 125.8 days. Management ratio: debtor turnover 3.86x vs 3.41x (AR MD&A ratios, printed p.63, AR txt 3803-3804) = about 94.6 vs 107.0 days. Direction: IMPROVING on both measures. 🟢
- Ageing history from RHP (INR lakh; the extracted schedule headers are displaced, columns re-mapped from Note 10 totals, RHP p.232, lines 16502-16568):
  - 31-Mar-2023: under 6 months 783.66; 6m-1yr 273.39; 1-2 yr 58.51; total 1,115.56. (>6 months 29.7%)
  - 31-Mar-2024: under 6m 1,187.97; 6m-1yr 295.68; total 1,483.64. (>6 months 19.9%)
  - 31-Mar-2025: under 6m 1,876.55; 6m-1yr 242.54; total 2,119.08. (>6 months 11.4%)
  - 30-Sep-2025: under 6m 1,574.30; over 6m 246.47; total 1,820.77. (>6 months 13.5%)
  - All "considered good"; doubtful and disputed nil; no unbilled or not-due debtors (RHP Note 10 footnote 3).
- ECL or provision for doubtful debts: none visible in RHP history (doubtful nil). FY26 provision NOT FOUND. Under AS there is no ECL matrix (see section 1). 🟡
- Single customer above 10% and top-5 concentration for FY26: NOT FOUND IN DOCUMENT in the AR text. RHP: top-5 customers 38.79% of H1 FY26 revenue (Sep-2025), 22.42% FY25, 22.76% FY24, 36.01% FY23 (RHP p.12056 and risk factor line 2515). H1 FY26 concentration is much higher than FY25. 🟡 (LBF2 stays open; identity of customers not in the notes read.)
- Receivables from related parties: none in Annexure D (RES-p18). Closing RPT balances are small payables to directors. 🟢
- MD&A: "stringent credit control policies for trade debtors" (AR-BR risk section, AR txt 2321). 🟢

## 5. INVENTORY (LBF3)
- FY26 category breakdown (RM, WIP, FG): NOT FOUND IN DOCUMENT (AR notes image-only). Total inventory 2,243.25 (31-Mar-2026) vs 1,470.95 (31-Mar-2025), +772.30, +52.5% (RES-p11, p4). Cash-flow inventory increase 772.30 [ties] (RES-p12).
- Inventory grew 52.5% against revenue 36.4% (derived). 🟡 Inventory turnover 2.68x vs 2.41x (AR MD&A, AR txt 3806) is computed on cost of goods (4,980.34 / average inventory 1,857.10 = 2.68, derived [ties]). 
- Pre-IPO breakdown (RHP Note 9, p.232): at 30-Sep-2025 RM 1,063.25, WIP 262.01, FG 780.35, total 2,105.61; at 31-Mar-2025 RM 1,055.67, WIP 84.66, FG 330.62, total 1,470.95. FG rose 449.73 in H1 FY26 alone. So most of the FY26 build had occurred by Sep-2025 (2,105.61 at Sep vs 2,243.25 at Mar). 🟡
- P&L movement: "Changes in inventory of FG and WIP" (329.69) for FY26 (build) vs (102.06) FY25; H1 FY26 (634.67), H2 FY26 +304.98 (a draw-down) (RES-p10). Inventory was built in H1 and partly released in H2 on the P&L line. 🟡
- Write-downs, obsolescence: NOT FOUND IN DOCUMENT. Physical verification: no discrepancy of 10% or more per class (CARO ii(a), pdf p.93). Quarterly bank stock returns agree with books (CARO ii(b)). 🟢
- Funding of the build: auditor's WC certificate shows total WC gap 2,438.93 (FY26) vs 2,255.47 (FY25), funded by IPO proceeds 123.03, internal accrual 2,315.90 (FY25 1,976.11) (RES-p4; a short-term borrowing figure 279.36 appears in the FY25 column [OCR]). The inventory build was funded from internal accrual and cash, not from IPO money. See section 12 (IPO use). 🟡

## 6. INVESTMENTS
- No subsidiaries, associates, JVs; no investments, loans or ICDs given during FY26 (CARO iii, iv, ix(e), pdf pp.94-95). 🟢
- Fixed deposits with banks: 1,502.00 included in cash equivalents (RES-p13). Cash and bank per balance sheet 2,782.78 (RES-p11). Implied cash outside unutilised IPO: 2,782.78 less 2,103.98 unutilised IPO funds = 678.80 (derived; includes the 919.17 margin-money bank balances, so free cash is below that). 🟡
- Advance to KIADB towards land 165.23 sat in short-term loans and advances in RHP (RHP Note 12, p.16598). FY26 short-term loans and advances 124.96 vs 254.71 (RES-p11), so the 165.23 land advance appears to be gone or reclassified (probably to CWIP or lease). Exact treatment NOT FOUND. 🟡 (LBF1)

## 7. BORROWINGS
- Instrument table, rates, security, covenants, repayment schedule: NOT FOUND IN DOCUMENT (AR notes image-only).
- Balance sheet: long-term borrowings 55.60 (126.16 FY25); short-term borrowings 20.54 (442.35 FY25) (RES-p11). Total debt 76.14 vs 568.51 (derived). Cash flow: repayment of long-term (103.25), proceeds 32.70, net short-term decrease (421.81) (RES-p12). Debt to equity 0.01x vs 0.26x (AR MD&A, AR txt 3817). 🟢
- Management says current ratio 3.34x vs 2.10x because of IPO liquidity and "repayment of unsecured working capital loans" (AR MD&A, AR txt 3813-3815). 🟢
- Finance costs 85.68 (FY26) vs 91.25 (FY25) (RES-p10) despite debt falling to 76.14: cost line is large against residual debt. Likely includes bank guarantee and LC commissions and interest earlier in the year; split NOT FOUND. 🟡
- Cash credit facility 275.41 appears inside the cash-and-cash-equivalents component table (RES-p13, OCR). Treatment NOT FOUND. 🟡
- Default: none (CARO ix(a), pdf p.94). Short-term loans used for stated purpose; no short-term funds used long term (CARO ix(c),(d)). Not a wilful defaulter (CARO ix(b)). 🟢
- Related party borrowings: none visible in Annexure D (RES-p18). 🟢
- MD&A interest coverage ratio printed as 0.05x vs 0.07x (AR MD&A, AR txt 3809-3811). With PBIT 1,665.31 (1,579.63+85.68) over finance cost 85.68 the cover is 19.4x (derived). The printed ratio is wrong or inverted and its "lower operating earnings" explanation contradicts the P&L. 🟡 (disclosure quality)

## 8. TRADE PAYABLES
- Ageing and MSME interest note: NOT FOUND IN DOCUMENT (AR notes image-only).
- Balance sheet: MSME dues 365.29 (266.62 FY25); other creditors 963.55 (660.55); total 1,328.84 (927.17) (RES-p11; certificate RES-p4 shows 1,328.84 [ties]). +43.3% vs revenue +36.4%. 🟢/🟡
- Payable days on cost of materials 5,310.03: 1,328.84 / 5,310.03 x 365 = 91.3 days (derived); FY25: 927.17 / 3,311.35 x 365 = 102.2 days. 🟢
- MSME share 27.5% of payables (derived). Interest on delayed MSME payments: NOT FOUND.

## 9. PROVISIONS
- Employee benefit funded status, actuarial assumptions, warranty movement: NOT FOUND IN DOCUMENT (AR notes image-only).
- Long-term provisions 294.41 vs 404.55 (fell 110.13); short-term provisions 458.87 vs 427.44 (+31.43) (RES-p11). Cash-flow line "Increase/(Decrease) in long-term provisions" (110.13) [ties] (RES-p12). A 27% fall in long-term provisions in a year with employee cost up 19.6% (1,059.98 vs 886.46) is unexplained in the notes read. May be a reclassification to short-term, a payout, or a reversal. 🟡
- FY25 gratuity and leave encashment catch-up 60.17 charged below PBT (section 1). 🟡
- Warranty: no warranty provision visible on the balance sheet face; products are custom panels and relays and the MD&A names warranty/rework as a risk (AR MD&A, AR txt 4125). Provision policy NOT FOUND. 🟡
- Litigation provisions: none disclosed; auditor says no pending litigation (section 3). 🟢

## 10. DEFERRED TAX
- FY26 tax expense 407.35 on PBT 1,579.63 = 25.79% (current 426.01, earlier years (0.78), deferred credit (17.88)) (RES-p10). Statutory rate used in the RHP computation: 25.0% (RHP deferred tax note, p.16453). FY25: 322.64 / 1,229.88 = 26.23%. Reconciliation NOT FOUND (note image-only). 🟢
- Net deferred tax asset 25.27 at FY26 vs 7.39 FY25 (RES-p11). The asset is mostly the 43B/gratuity timing difference (RHP p.16450-16457). Unrecognised DTA: NOT FOUND. MAT credit: none (not applicable). 🟢
- Income taxes paid 382.02 in FY26 vs 219.52 in FY25 (RES-p12). 🟢

## 11. REVENUE DETAILS
- Disaggregation, contract assets and liabilities, unsatisfied performance obligations, top customer revenue: NOT FOUND IN DOCUMENT in the AR (notes image-only). The company reports one segment (reply to NSE item 2, RES-p1). Segment note NOT FOUND in AR.
- Revenue from operations FY26 8,385.88 (H1 3,574.71; H2 4,811.17) vs FY25 6,148.58 (+36.4%); other income 97.01 vs 144.81 (RES-p10; the P&L OCR shows total income 8,483.09). Check: H1+H2 revenue 8,385.88 vs 8,386.08 implied by total income less other income, a 0.20 gap that is likely OCR damage [OCR]. 🟢
- Order book: NOT FOUND in AR notes. RHP order book 5,223.65 at the RHP date (RHP p.12232, area). Context only.
- H2 revenue is 34.6% above H1 (4,811.17 vs 3,574.71; derived). Revenue recognition timing (point in time at dispatch vs milestone) NOT FOUND. 🟡

## 12. OTHER CRITICAL NOTES
### 12a. Capex, CWIP and KIADB (LBF1)
- Capital work-in-progress at 31-Mar-2026: 466.79 (nil at 31-Mar-2025; 15.62 at 30-Sep-2025 per RHP p.16004) (RES-p11; RHP). CWIP ageing and project note: NOT FOUND (image-only). 🟡
- RHP plan: Rs 1,155.38 lakh capex from fresh issue for civil construction, internal electric work and internal plumbing of the integrated unit, plus Rs 150.00 lakh from internal accruals from October 2025 (RHP p.37, lines 2492-2493). Plot: 4,020 sq m leasehold from KIADB, allotted 25-Feb-2016, 99-year lease, possession 2-Jun-2017, lease-cum-sale agreement 19-Mar-2018 (RHP p.37).
- Utilised by 31-Mar-2026: capex object 275.83 of 1,155.38 (23.9%); unutilised 879.55 (auditor-certified, RES-p16, p17). CWIP 466.79 exceeds IPO capex used 275.83 by 190.96, which the company met from internal accruals (RHP plan 150.00; derived gap 40.96 above that plan). 🟡
- KIADB deadline: commercial production due by 26-Oct-2026 after a one-year extension granted 27-Oct-2025; "no further extension may be granted" if missed; original deadline was 1-Jun-2020 (RHP p.31-37, lines 2469-2491). The AR notes the unit is unfinished at balance sheet date (CWIP only). Status after 31-Mar-2026: NOT FOUND in notes. 🔴 (single point of failure for the land; LBF1 stays open.)
- Cash-flow check: capex purchases (including intangibles and CWIP) 750.23 in FY26 vs 23.47 in FY25 (RES-p12). Roll-forward: net PPE +202.84, intangibles +2.49, CWIP +466.79, depreciation 64.63, disposals at book 13.48 (15.06 proceeds less 1.58 gain) = 750.23 [ties exactly]. So the 750.23 contains about 467 of CWIP and about 283 of plant additions in year. 🟢
- Capital commitments at year end: NOT FOUND IN DOCUMENT. RHP showed 0.00 estimated contracts on capital account at Sep-2025 (RHP p.33).
- Title: leasehold land allotted by government held as lessee, lease agreement in the company's name (CARO i(c), pdf p.93). 🟢

### 12b. IPO proceeds utilisation (LBF3)
- Auditor certificate dated 21-May-2026: fresh-issue proceeds 3,053.84, used 949.86, unutilised 2,103.98 at 31-Mar-2026 (RES-p16, p17). By object: capex 1,155.38 allocated, 275.83 used, 879.55 unutilised; working capital 860.00 allocated, 123.03 used, 736.97 unutilised; general corporate purposes 457.00, nil used, 457.00 unutilised; issue expenses 581.46, 551.01 used, 30.45 unutilised. Sum of used 275.83+123.03+0+551.01 = 949.87 [ties within 0.01]. 🟢
- Conclusion in the certificate: no deviation from the objects in the Prospectus dated 14-Jan-2026 (RES-p15). Board report states no deviation or variation (AR-BR, printed p.40). CARO x(a): proceeds used for the purposes raised; refers to "note 2(iii)" of the financial statements (CARO, pdf p.95); that note is image-only, NOT FOUND. 🟢
- The WC certificate says "The Company has utilised the stated amount accordingly. The unutilised remaining balance will be utilized subsequently" (RES-p4). Only 14.3% of the 860.00 working-capital object was used (123.03 / 860.00) although inventory rose 772.30 and the certificate shows a WC gap of 2,438.93. The remaining 736.97 sits in deposits (fixed deposits 1,502.00 on the cash-flow components, RES-p13). 🟡
- Issue size per AR: 59,70,000 shares at 59 each = 3,522.30 (AR MD&A, printed p.64, AR txt 3836-3838). Fresh issue per certificate = 3,053.84. The gap 468.46 (derived) points to an offer-for-sale component. INFERENCE (not stated in the pages read); consistent with promoters reimbursing 89.13 of issue expenses (RES-p19).
- Equity reconciliation (derived): share capital rose 79.41 to 2,264.54 (+2,185.13); reserves rose 2,100.59 to 3,643.49 (+1,542.90) of which PAT 1,172.28, leaving +370.62 from other movements. 2,185.13 + 370.62 = 2,555.75, which equals the cash-flow line "Proceeds from IPO net of issue expenses" 2,555.75 [ties] (RES-p11, p12). Gross fresh issue 3,053.84 less 2,555.75 implies issue costs of 498.09 netted in equity, against 581.46 budgeted and 551.01 paid per certificate. A 52.92 difference between 551.01 paid and 498.09 implied is NOT explained in the pages read (may be promoter recovery 89.13 less other items). 🟡
- Share capital rise beyond the IPO (597.00 face value if all 59.70 lakh shares were fresh, or less if part is OFS) indicates a bonus issue funded from reserves; bonus note NOT FOUND (image-only). EPS FY26 6.34 basic = diluted (RES-p10); weighted shares about 184.9 lakh (1,172.28 / 6.34, derived) vs 226.45 lakh shares in issue at year end. Basic and diluted equal: no dilution source seen. 🟢

### 12c. Cost structure behind FY26 margin (LBF4), derived from face P&L (RES-p10)
| Line | FY26 | % rev | FY25 | % rev | H1 FY26 | H2 FY26 |
|---|---|---|---|---|---|---|
| Cost of materials consumed | 5,310.03 | 63.3% | 3,311.35 | 53.9% | 2,565.24 | 2,744.79 |
| Change in FG and WIP | (329.69) | | (102.06) | | (634.67) | 304.98 |
| Net material cost | 4,980.34 | 59.4% | 3,209.29 | 52.2% | 1,930.57 | 3,049.77 |
| Employee benefits | 1,059.98 | 12.6% | 886.46 | 14.4% | 500.13 | 559.85 |
| Other expenses | 712.83 | 8.5% | 800.87 | 13.0% | 381.39 | 331.44 |
| Depreciation | 64.63 | 0.8% | 75.63 | 1.2% | 35.21 | 29.42 |
| Finance costs | 85.68 | | 91.25 | | 47.22 | 38.46 |
| PBT | 1,579.63 | 18.8% | 1,229.88 | 20.0% | 733.79 | 845.84 |
- Net material cost share rose from 52.2% to 59.4% of revenue; H1 FY26 (revenue 3,574.71) 54.0%, H2 FY26 (4,811.17) 63.4% (derived). Gross margin fell about 7 points; employee and other costs fell 1.8 and 4.5 points of revenue and offset it. PBT margin H1 20.5% (733.79/3,574.71) vs H2 17.6% (845.84/4,811.17) (derived). 🟡
- Other expenses fell in rupee terms (800.87 to 712.83) while revenue grew 36%: the notes that would show what is in this line (freight, commission, warranty, R&D, CSR, FX, bad debts) are NOT FOUND. 🟡 This line and depreciation are the two places where cost could be shifted to CWIP or held low; no capitalised-expense disclosure was read.
- MD&A operating profit margin 19.86% vs 21.49% = (PBT + finance cost) / revenue [ties: 1,665.31/8,385.88 = 19.86%; FY25 1,321.13/6,148.58 = 21.49%] (AR MD&A, AR txt 3821); net margin 13.98% vs 13.78% [ties 1,172.28/8,385.88]. MD&A calls the 1.63-point change "no significant change". 🟢
- Foreign exchange: FY26 cash flow carries a (gain)/loss on FX of (0.57) (RES-p12); no hedging or exposure disclosure read. NOT FOUND.

### 12d. Cash conversion
- Cash flow from operations: operating profit before working capital 1,644.01; cash generated from operations 1,177.46; tax paid (382.02); net operating cash flow 795.44 (FY25 573.22) (RES-p12; OCR lines checked: 1,177.46 less 382.02 = 795.44 [ties]). CFO / PAT = 67.9%; CFO / EBITDA (EBITDA 1,632.93 = PBT 1,579.63 + finance 85.68 + depreciation 64.63 less other income 97.01, derived) = 48.7%. Driver: inventory build (772.30) and receivables increase (102.20), partly offset by payables +401.66 [OCR 40166] (RES-p12). 🟡
- Cash-flow tie: bank balances classed outside cash (413.61 increase) is the largest investing outflow after capex; margin money for guarantees is growing with the order book. 🟡

### 12e. Other
- Events after balance sheet date, CSR required vs actual, ESOP: events/CSR notes NOT FOUND (image-only). CARO xx: no unspent CSR and no ongoing CSR projects (CARO, pdf p.96). No ESOP seen; basic = diluted EPS. 🟢
- Going concern: Board: "no elements of risk that threaten the immediate existence or going concern status" (AR-BR printed p.38, AR txt 2323-2325); Directors prepared accounts on a going concern basis (AR txt 2744). Auditor: no material uncertainty (CARO xix, pdf p.96) with the standard disclaimer that this is not an assurance of future viability. No emphasis of matter, no KAM section in the report (AR-aud). Going concern language of concern: NONE. 🟢
- Auditor: Vasanth & Co (Bangalore), unmodified opinion on financials and on internal financial controls (AR-aud pdf p.89-92; CARO Annexure B pdf p.98); no fraud, no ADT-4, no whistle-blower complaints (CARO xi); no auditor resignation (CARO xviii); no cash losses (CARO xvii). 🟢
- Audit report date 21-05-2026 equals the board approval date (RES-p5 and AR-aud). 🟢
- Dividend: none declared or paid (AR-aud 2(A)(h)(v)). 🟢
- Statutory dues paid regularly; none over 6 months in arrears (CARO vii(a), pdf p.94). 🟢
- Title deeds, internal audit adequate, section 177/188 compliance (CARO xiii, xiv). 🟢

## PASS 1 SUMMARY: TOP 10 FINDINGS (ranked by investor importance)
| Rank | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | AR notes pp.99-127 (financial statements and Notes 1 to last) are image-only; FY26 ageing, contingencies, borrowings, RPT note, concentration and policies cannot be read. All note-level items beyond the face statements are NOT FOUND | AR txt [page 99]-[page 127] | 🔴 (evidence gap, not an accounting finding) |
| 2 | KIADB integrated unit: capex 275.83 of 1,155.38 used (23.9%); CWIP 466.79; commercial production deadline 26-Oct-2026 with "no further extension" | RES-p16, p11; RHP p.31-37 | 🔴 |
| 3 | Inventory +52.5% (2,243.25 vs 1,470.95) against revenue +36.4%; FG build in H1 (FG 330.62 to 780.35 by Sep-2025); funded from internal accrual, IPO WC object used only 123.03 of 860.00 | RES-p11, p4, p16; RHP Note 9 | 🟡 |
| 4 | Net material cost share 52.2% to 59.4% of revenue (H2 63.4%); H2 PBT margin 17.6% vs H1 20.5%; margin held up by lower employee and other expense shares (other expense down in rupees) | RES-p10 (derived) | 🟡 |
| 5 | Cash conversion weak: CFO 795.44 = 48.7% of EBITDA; margin-money bank balances up 413.61 to 919.17 | RES-p12, p13 | 🟡 |
| 6 | Receivables ageing: total 2,221.29 (+4.8%), closing days 96.7 vs 125.8 improving; FY26 ageing and customer concentration NOT FOUND; H1 FY26 top-5 was 38.79% vs 22.42% FY25 | RES-p11; RHP p.232, p.12056 | 🟡 |
| 7 | RPT 476.04 = 5.68% of revenue; 78.00 family consultancy and professional fees (18.00 per relative) at arm's length per AOC-2 but scope NOT FOUND; 289.48 to 4 promoter directors = 24.7% of PAT | RES-p18-19; AR AOC-2 | 🟡 |
| 8 | Cost-records conflict: CARO says cost records prescribed and reviewed; Board says not required and not maintained | CARO vi pdf p.94; AR-BR printed p.40 | 🟡 |
| 9 | MD&A interest coverage 0.05x vs 0.07x contradicts the P&L (19.4x derived); long-term provisions fell 27% (404.55 to 294.41) unexplained; FY25 60.17 gratuity catch-up below PBT | AR MD&A txt 3809; RES-p11, p10 | 🟡 |
| 10 | Clean base: unmodified opinion and IFC opinion, audit trail on, no default, debt 76.14 (0.01x equity), no going concern doubt, no subsidiaries, IPO certificate shows no deviation; equity inflow 2,555.75 ties to cash flow | AR-aud; CARO; RES-p12 | 🟢 |

## Hand-off notes for Pass 2 and Pass 3
- Pass 2 must start by retrying the AR notes pages as images. If still unreadable, state PASS 2: NO MATERIAL NEW FINDINGS on the readable set and carry the input gap into B02 (do not invent note content).
- Items worth a second look if any note text appears: Note on capital work-in-progress (ageing, KIADB), trade receivables ageing and top-customer disclosure, contingent liabilities, RPT note vs Annexure D (476.04), share capital and bonus note, "note 2(iii)" IPO utilisation, other expenses breakup, long-term provisions.
