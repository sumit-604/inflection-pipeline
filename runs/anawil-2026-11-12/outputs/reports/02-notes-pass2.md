# Stage 2, Pass 2: What was missed. ANAWIL (Anawil Wire and Engineering Ltd). Run 2026-11-12

Scope: new findings only. Pass 1 items are not repeated. Where pass 2 corrects or closes a pass 1 item, it says so (section 2).

## 0. Basis, units, anchors

- UNIT: INR lakh unless stated. "Rs X Cr" in brackets is my arithmetic (lakh / 100), marked "derived". No figure is converted inside an anchor.
- "Pros p.N" = the `[page N]` marker in Prospectus_2026-08-06.txt. "AFS p.N" = marker in Audited_Financial_Statements_FY2025-26.txt. "H1 p.N" = marker in H1FY27_Results_Outcome_of_Board_Meeting_2026-11-06.txt. "CRISIL p.N" and "NSE p.N" = markers in the rating rationale and the 2026-11-07 NSE intimation (CARE monitoring agency report).
- Framework: Accounting Standards (Indian GAAP), not Ind AS. No Ind AS ECL, fair value hierarchy or financial instruments risk note applies. The financial instruments, fair value and risk management heading of the pass 2 brief is therefore NOT APPLICABLE (AS framework: H1 p.5 notes 2 and 3; Pros Annexure IV).

### AFS page status at the time of this read (OCR still filling)
- TEXT PRESENT and read in full: AFS p.1-7 (auditor's report and the first page of the CARO annexure), p.36-41 (CWIP ageing note 12 tail, notes 37 EPS and 38 ratios, signature page, FY2025 auditor's report pages), p.71-78 (G.B. Laddha FY2024 engagement letter and FY2024 auditor's report pages). That is 21 pages.
- "OCR PENDING" (82 pages): p.8-35, p.42-70, p.79-103. This covers the rest of the CARO annexure (clauses after 2(a)), the balance sheet, P&L, cash flow statement, notes 1-10 and 13-36, the FY2025 and FY2024 statements and CARO. Pass 3 must re-read them.
- Pass 1 listed p.1-2 as the only text in the auditor's report. Pages 3-7, 38-41 and 74-78 are new since then.
- OCR caution carried: the AFS drops word spaces and can misread digits. Every AFS number used below is checked against the Prospectus or the H1 audited comparative column, and both are reported.

---

## 1. Load-bearing fact (a), cash flow: the FY26 gap test (1843.94 vs 1246.70)

Result: both numbers are filed, both are arithmetically sound, and both give the same net cash movement of 147.14 lakh. The 597.24 lakh gap is classification, not cash. This closes the pass 1 line "Rs 12.5 Cr is NOT in the restated cash flow" (it is in the audited cash flow, see below).

Sources: Restated cash flow, Pros p.174 (Annexure III, INR lakh). Audited cash flow with FY26 column marked "Audited", H1 p.8 (INR lakh).

| Block | Restated (Pros p.174) | Audited (H1 p.8) | Audited less restated |
|---|---|---|---|
| Operating cash flow | 1843.94 | 1246.70 | (597.24) |
| Investing cash flow | (9727.16) | (9300.56) | +426.60 |
| Financing cash flow | 8030.36 | 8201.00 | +170.64 |
| Net change in cash | 147.14 | 147.14 | 0.00 |
| Closing cash and equivalents | 159.72 | 159.72 | 0.00 |

The 597.24 lakh operating gap, line by line (derived, INR lakh; sign = audited less restated):

| Item | Restated | Audited | Effect on audited CFO | Where it moves to |
|---|---|---|---|---|
| Profit before tax | 4450.47 | 4450.25 | (0.22) | Preliminary expense adjustment 0.22 (Annexure V, Pros p.187) |
| Interest add-back | 564.27 | 420.86 | (143.41) | Audited keeps 143.41 of finance cost inside operating; financing interest also lower by 143.41 (H1 p.8: interest paid 420.86 vs Pros p.174: 564.27) |
| Gratuity, loss on sale, bad debt add-backs | 10.57 + 4.77 + 9.81 | not shown | (25.15) | Offset: audited receivables outflow is 9.81 smaller (1377.93 vs 1387.74); loss on sale 4.76 sits in audited investing |
| Other current assets change | (179.20) | (600.82) | (421.62) | Audited puts the other non-current asset movement 421.84 (retention money 297.44, FD with BOB 75.18, deposits 49.22; Annexure L, Pros p.203) into operating; restated has it in investing |
| Other liabilities change | 1281.91 + 2.00 | 1267.23 | (16.68) | Not traced (small) |
| Loans and advances + provisions + tax paid (net) | (3565.64) + (406.86) = (3972.50) | (3472.82) + 351.52 + (851.19) = (3972.49) | 0.01 | Pure presentation, see tax note below |
| Residual of small lines (derived) | | | about (32.0) | Sum of the unexplained 0.22, 25.15, 9.81 and 16.68 items above |

Share of the gap (derived): other non-current assets 421.84 = 70.6%; interest 143.41 = 24.0%; residual about 32.0 = 5.4%.

- TAX LINE. The audited "Direct Taxes Paid (Net)" of 851.19 is the P&L tax charge, not a payment: current tax 767.78 + earlier year tax 83.40 = 851.18 (H1 p.4). The same pattern holds in H1 FY27: tax "paid" 360.01 equals current tax 360.01 (H1 p.4, p.8). The audited statement then offsets it with a +351.52 "provisions" line. The restated 406.86 is a true payment figure: 770.34 + 11.69 less the rise in net tax payable 375.17 (186.61 to 561.78, Annexure H, Pros p.199) = 406.86. So the 444.33 tax difference is fully offset inside the audited working capital lines. No cash effect.
- INTEREST. Restated interest 564.27 equals the sum of Annexure W interest lines 498.93 + 44.55 + 4.82 + 15.96 = 564.26 (Pros p.208). Audited P&L finance cost is 578.58 (H1 p.4) vs restated 594.71, a difference of 16.13. Audited cash flow interest is 420.86, so 157.72 of the audited finance cost is not treated as interest paid, against 30.44 (bank charges 24.71 + other charges 5.74) in the restated version. What the extra 127.28 is: NOT FOUND IN DOCUMENT. Two candidates that do NOT tie exactly: Darpan guarantee commission 97.60 plus bank and other charges 30.44 = 128.04 (gap to 127.28 is 0.76); or interest on unsecured loans 44.55 + guarantee commission 97.60 = 142.15 (gap to 143.41 is 1.26). [INFERENCE: the guarantee commission 97.60 (pass 1 item, Annexure ZA, Pros p.210) may be in audited finance cost; unproven.] The audited P&L line detail (note on finance costs) is on OCR-pending pages.
- THE 27.24 PLUG. Audited financing shows borrowings net +7341.12 (5973.82 + 1367.30) against a balance sheet debt movement of +7313.88 (12824.76 less 5510.88; restated Annexure B, Pros p.189-190, and restated cash flow 9029.27 - 2030.05 + 314.66 = 7313.88). The 27.24 excess is an unexplained plug in the audited financing block. 🟡
- WHICH CFO IS "RIGHT". Neither is a clean operating measure. Both still carry the capex creditor rise 832.88 (pass 1) in operating inflow, because investing equals accrual capex in both statements (restated 9305.37; audited 9300.61).

Common-basis operating cash flow (derived, INR lakh), interest in financing, retention money in operating, capex creditors out:

| Basis | FY26 CFO | Rs Cr | % of PAT |
|---|---|---|---|
| Restated as filed | 1843.94 | 18.44 | 50.3% of 3662.83 |
| Audited as filed | 1246.70 | 12.47 | 34.7% of audited PAT 3595.25 |
| Restated less capex creditors 832.88 | 1011.06 | 10.11 | 27.6% |
| Restated less capex creditors less retention money 297.44 | 713.62 | 7.14 | 19.5% |
| Audited basis, interest back to financing (+143.41), less capex creditors, FD 75.18 back to investing | 632.41 | 6.32 | 17.6% of audited PAT |

The audited-basis and restated-basis common figures differ by about 81 lakh (the 49.22 of deposits plus the 32 residual). Range for stage 10: Rs 6.3 to 10.1 Cr, FY26 (derived). 🔴 for earnings-to-cash quality, classification driven. FLAG-CASH stands.

FY26 free cash flow (CFO less accrual capex, derived): restated 1843.94 - 9305.37 = (7461.43); audited 1246.70 - 9300.61 = (8053.91). Net cash was funded by debt 7313.88 and equity 1280.75 (Pros p.174).

H1 FY27 (H1 p.8, INR lakh): CFO 2828.40 on PAT 1438.69 (196.6%, derived) but this is working capital unwinding: inventory +1838.24, payables (2090.24), short-term loans and advances (429.88). Capex (5339.49) exceeds CFO by 2511.09 (derived). Treat H1 FY27 CFO as a timing reversal, not a run-rate. 🟡

---

## 2. Corrections and closures to pass 1 (new facts)

C1. The 12.5 CFO is found. Audited FY26 CFO is 1246.70 (H1 p.8). Pass 1 said NOT FOUND; superseded by section 1.

C2. Customer concentration is NOT absent. Pass 1 said "NOT FOUND in the restated notes". It is in the Prospectus risk factors, so it is outside the notes but filed: top five customers 78.75% / 88.57% / 85.70% of revenue for FY26 / FY25 / FY24; Customer 1 29.32% (FY25 22.70%), Customer 2 16.35%, Customer 3 12.64%, Customer 4 11.61%, Customer 5 8.84% (Pros p.23-24). Top ten customers 97.31% / 99.93% / 99.98% (13,940.77 of 14,326.69 in FY26); top ten suppliers 90.11% / 80.19% / 72.44% of purchases (7,561.76 of 8,392.06 in FY26) (Pros p.114). CRISIL: top five "more than 70%" (CRISIL p.2). Receivable by customer: NOT FOUND IN DOCUMENT. 🔴 for concentration, 🟡 for receivable exposure (3894.54 total, no named-customer split).

C3. The 7.32 difference between Annexure B(A) and Annexure B is closed. Pass 1 left 7.32 unexplained (12308.01 vs 12315.33). Risk factor 37 says unsecured loans recallable at any time are 516.76 (Pros p.34): promoter loans 433.89 + Cosmos Bank loan 82.86 = 516.75. Annexure B shows the Cosmos loan non-current as 75.53; 82.86 - 75.53 = 7.33 is its current maturity inside the 1796.07 line. No error.

C4. The tax regime is confirmed and is a live exposure, not just an inference (finding N1 below). Pass 1 said the 17.160% rate was "INFERENCE" for section 115BAB. The Prospectus names it (Pros p.91).

C5. Who is the statutory auditor. Pass 1: "current statutory auditor NOT FOUND". G.B. Laddha and Co LLP is the current auditor: it signed the FY26 report (AFS p.6, dated 18/06/2026), the H1 FY27 limited review (H1 p.3, dated 06/11/2026) and the CA certificate on IPO fund use dated 4 November 2026 (NSE p.5 footnote). "Previous Auditors" in the restated report (Pros p.167-168) means the auditor of the underlying audited statements, not a change of auditor. No change of statutory auditor is evidenced. 🟢

C6. "Traded goods sold with nil trading purchases" (pass 1 item). No new data; still unexplained. The MD&A says a third tower model (base tower plus steel plates and internals) began in FY26, four towers supplied (Pros p.232). See N3.

C7. Pass 1 item "statutory audit fee 4.80". The audit engagement letter for FY24 fixes the fee at Rs 2,50,000 (AFS p.75) vs Annexure ZG4 FY24 statutory audit 1.50 and tax audit 0.50 = 2.00 lakh (Pros p.217). Gap 0.50 to 1.00. Small. 🟢

---

## 3. New findings by note area

Ratings: 🟢 clean, 🟡 watch, 🔴 red flag.

### N1. Income tax: concessional regime under challenge, demand 367.25 after year end (Contingent liabilities / events after balance sheet / deferred tax) 🔴
- Prospectus litigation section, tax proceedings: assessment year 2025-26 (FY25), one case, 367.25 lakh. Demand order dated 17 July 2026 under section 143(1)(a), "on account of non-grant of the concessional tax rate regime under Section 115BAB ... due to a procedural delay in filing Form No. 10-ID". Rectification application filed 22 July 2026; "currently pending for rectification order" (Pros p.240-241). The company also cites an older section 119(2)(b) condonation application dated 23.08.2023 that was approved.
- The special tax benefit statement says the option was exercised from FY2020-21 and Form 10-ID was filed on 31 March 2022 (Pros p.91). The company was incorporated on 2 January 2021 (Pros p.176).
- The restated accounts apply 17.160% (15% + 10% surcharge + 4% cess) on business income and 25.168% on other sources (Annexure ZB, Pros p.212). Contingent liabilities at 31 March 2026 are nil, and the 226.93 earlier demand is marked disposed (Annexure Z, Pros p.209-210). The 367.25 demand came after the balance sheet date and before the Prospectus date (6 Aug 2026). It is NOT in the list of post balance sheet developments (that list has only corporate approvals, Pros p.236-237) and not in any restated note. No provision exists for it.
- Size (derived): 367.25 = 10.0% of restated FY26 PAT 3662.83; 4.1% of FY26 net worth 8951.16. If the concessional rate were denied for all three restated years, the extra tax at the Annexure ZB rate gap (25.168% - 17.160% = 8.008%) on business PBT is: FY26 4415.22 x 8.008% = 353.57; FY25 1487.76 x 8.008% = 119.14; FY24 534.36 x 8.008% = 42.79; total 515.50 lakh (Rs 5.2 Cr), before interest. That is 14.1% of FY26 PAT. Method uses the Prospectus's own rates only.
- Pattern: the two earlier demands (AY 2022-23 97.06 + 24.26 interest, AY 2023-24 88.75 + 16.86 interest, total 226.93) were also tax-portal demands (Annexure Z note 2, Pros p.210). Their cause is not stated. [INFERENCE: they may have the same 10-ID origin; not stated.] Result: three of four recent assessment years drew a portal demand.
- Forward link: the tax rate is part of every PAT figure the company guides to. At 25.168% instead of 17.160% the tax bill is 46.7% higher (derived: 25.168 / 17.160 - 1), and PAT per rupee of PBT falls from 0.8284 to 0.7483, a 9.7% cut (derived). Eligibility conditions of the section (manufacturing commencement date and no reconstruction) are NOT tested anywhere in the notes.

### N2. Trade payables: two creditors hold 85.7% of payables; MSME disclosures contradict each other (Trade payables) 🔴
- Material creditors table at 31 March 2026 (threshold 233.32 = 5% of payables): 55 creditors, 4,666.33 total. MSME: 14 creditors, 821.94, one material creditor 455.11 (55.4% of MSME dues). Others: 41 creditors, 3,844.39, ONE material creditor 3,545.82 (92.2% of "other" dues). Two material creditors = 4,000.93 = 85.7% of all trade payables (Pros p.243). The single 3,545.82 creditor is 76.0% of payables and equals 42.3% of FY26 raw material purchases 8,392.06 (derived). Names are on the company website, not in the Prospectus: NOT FOUND IN DOCUMENT.
- Raw material purchases by state (Pros p.124): Gujarat 6,196.80 (74.03% of 8,371.08) in FY26 against 820.16 in FY25. [INFERENCE: the 3,545.82 creditor is most likely a Gujarat steel source; not stated.] Vendor advances of 3,063.21 (pass 1) may sit with the same supplier. The notes do not say. Test for management: are the 3,063.21 vendor advances and the 3,545.82 payable the same counterparty (a net 482.61 payable if so, derived)?
- CONTRADICTION. The same page says: "our Company has not received any intimation from suppliers regarding their status under the MSMED Act and hence disclosure in relation to amount unpaid together with interest payable has not been furnished" (Pros p.243). Annexure F gives a 14-creditor MSME split of 821.94 and Annexure ZG1 gives 735.61 unpaid principal with "generally within 45 days" (Pros p.198, 216). Three versions of MSME dues in one document. 🔴 (small money, credibility; pass 1 had two versions).
- H1 FY27 (H1 p.7): MSME dues 1,785.48 (up from 821.94) while other creditors fell from 3,844.38 to 790.61; total payables 4,666.33 to 2,576.09 (derived). MSME share rose from 17.6% to 69.3% (derived). The 43B(h) timing (pass 1: 263.45 disallowed at 31 March 2026) becomes larger, not smaller, if the MSME payables are not paid within 45 days. 🟡

### N3. Customer-supplied or integrated steel: per-tower order values show the three models (Revenue details) 🟡
Pass 1 said the notes cannot test the three-model split. The Prospectus order book (not a note) does give per-tower values, derived here (order amount / towers, INR lakh, Pros p.114):
- Customer A Sany 7,224.15 / 123 = 58.73 (Envision 58.34 / 1 = 58.34); Customer B 5,209.97 / 47 = 110.85; Customer C 1,753.54 / 40 = 43.84; Customer D 10,760.44 / 34 = **316.48**; Customer E 6,021.54 / 54 = 111.51; Customer F 2,461.62 / 40 = 61.54 and 2,492.12 / 40 = 62.30. Total 35,981.72 for 379 towers (359.82 Cr; CRISIL quotes 359 Cr, CRISIL p.1).
- Customer D at 316.48 lakh per tower is 5.4x Customer A (derived), consistent with a tower sold with steel plates and internals. Customer D is 29.9% of the order book (derived). MD&A: a third model "base tower along with steel plates and internals" was introduced in FY26, four towers supplied that year (Pros p.232).
- This anchors, but does not prove, the link between the inventory build (raw material 3,930.40, pass 1) and the integrated-supply orders. [INFERENCE: the steel in stock is bought ahead of integrated-model orders like Customer D's 34 towers due by 31-03-2027; the notes do not say.] Customer-supplied material (free issue) remains NOT FOUND IN DOCUMENT in the Prospectus (a search for job work, free issue and customer supplied found only process descriptions and a transport line for job work, Pros p.126).
- Revenue by state (Pros p.112): Karnataka 13,448.96 (93.87%), Gujarat 877.73 (6.13%; MD&A says 16 towers, Pros p.232). Matches the load-bearing "Karnataka 93.9%".

### N4. Restated vs audited FY26 P&L: classification and re-timing, fully reconciled (Accounting policies, restatement) 🟡
The FY26 audited P&L in the H1 comparative column (H1 p.4) differs from the restated P&L (Pros p.173) as follows (INR lakh):

| Line | Audited (H1 p.4) | Restated (Pros p.173) | Difference | Explanation found |
|---|---|---|---|---|
| Cost of materials consumed | 4372.06 | 4731.58 | (359.52) | Restated includes stores and spares consumed 359.53 (Annexure ZF2, Pros p.215-216); audited carries them in other expenses |
| Other expenses | 3623.75 | 3244.03 | +379.72 | Stores 359.52 + finance cost 16.13 + employee cost 3.83 + 0.22 = 379.70 (derived) |
| Employee benefits | 411.20 | 415.03 | (3.83) | Not traced |
| Finance cost | 578.58 | 594.71 | (16.13) | Close to interest on delayed payment of taxes 15.96 (Annexure W); not confirmed |
| Profit before tax | 4450.25 | 4450.47 | (0.22) | Preliminary expense adjustment 0.22 (Pros p.187) |
| Current tax | 767.78 | 770.34 | (2.56) | Short provision of income tax (2.56), Pros p.187 |
| Deferred tax | 3.81 | 5.61 | (1.80) | Deferred tax adjustment (1.80), Pros p.187 |
| Earlier year taxes | 83.40 | 11.69 | +71.71 | Restated reverses the 83.40 earlier-year charge and re-books 11.69 |
| Profit after tax | 3595.25 | 3662.83 | (67.58) | 3595.25 - 1.80 - 2.56 + 83.40 + 0.22 - 11.69 = 3662.82 (derived); ties to Pros p.187 |

- The audited accounts charged 83.40 of earlier-year tax through FY26 profit (H1 p.4: PAT 3595.25 is after it; H2 FY26 column 3370.22 = 4152.45 - 702.51 + 3.68 - 83.40). Restated profit adds it back. Cumulative reserves at 31 March 2026 are identical (6979.66) in both (Pros p.186), so the +67.58 is re-timing of tax into earlier years, not new profit. Restated FY25 PAT is lower by 167.83 as the mirror (Pros p.187). For a run-rate base, the audited FY26 PAT 3595.25 includes a non-recurring earlier-year tax 83.40; the restated 3662.83 is the more comparable but both are filed. Stage 10 should name which basis it uses.
- Rent income 35.00 (Annexure S, Pros p.207) is a first-half item: other income was 35.43 in the six months to 30.09.2025 and 0.55 in H2 FY26 (H1 p.4, derived). It is not recurring. Pass 1 asked who pays it; still NOT FOUND, but it stopped after Sep 2025 (FY26 PBT includes 35.00, 0.8% of PBT, derived).
- Audited FY26 EPS 18.78 is confirmed by two sources (AFS p.37 and H1 p.4), weighted shares 191.48 lakh = 19,147,548 (Pros p.213). Restated EPS 19.13.

### N5. Inventory held with third parties (CARO) 🟡
- CARO 2(a): physical verification was done "except for inventory lying with third parties ... these have substantially been confirmed by the third parties" (AFS p.7). The amount lying with third parties is NOT FOUND IN DOCUMENT in the pages read. The Prospectus mentions semi-finished goods sent for job work (Pros p.126). FY26 inventory is 5,068.78 (raw material 3,930.40, WIP 1,039.64), and fabrication work cost is 1,282.41 (Annexure Y, Pros p.209). The following CARO lines (verification differences of 10% or more, quarterly returns filed with banks, clause 3(ii)(b)) are on OCR-pending pages. 🟡
- Cross-check of the raw material days. Pass 1 used consumption 4,731.58 (incl. stores) for 303 days. On the audited basis consumption of 4,372.06 (H1 p.4) the closing raw material 3,930.40 is 328 days (derived). Both are far above 39 days (FY25 on 2,500.72). CRISIL gives inventory 226 days and receivables 99 days at 31 March 2026 (CRISIL p.2); CRISIL's receivable days equal the pass 1 year-end figure (99).
- H1 FY27: inventory fell to 3,230.54 from 5,068.78 (H1 p.7), a 1,838.24 release (H1 p.8). The build was partly a timing item.

### N6. Depreciation, amortisation and gearing run-rate (Accounting policies, PPE, borrowings) 🟡
- Intangible (pollution control licence): FY26 amortisation 0.01 vs 2.03 (Annexure X, Pros p.208). The audited H1 FY27 balance sheet shows intangibles falling 31.87 to 28.83 in six months = 3.04 (H1 p.7), a run rate of about 6.1 a year (derived). FY26 amortisation of about 6 lakh looks unbooked in the year (small money). Policy says 30-year straight line (pass 1).
- Depreciation run-rate. FY26 depreciation was 1,130.14 although PPE additions were 8,850.77 (Pros p.200-202, pass 1), because Kutch assets were capitalised late (Kutch commercial operations March 2026, Pros p.232). H1 FY27 depreciation is 1,286.53 for six months (H1 p.4) = 113.8% of the full FY26 charge; annualised 2,573.06 (derived), 2.28x FY26. H1 FY27 CWIP is 3,069.27 vs 584.80 (H1 p.7), so more capitalisation follows. Any FY27 earnings base built on FY26 depreciation will overstate PAT. This is a notes-level arithmetic fact, not a forecast. 🟡
- Gearing check against CRISIL: CRISIL expects gearing "below 0.05 time" and total outside liabilities to tangible net worth 0.25 at 31 March 2027 (CRISIL p.1). At 30 Sep 2026 debt is 3,360.79 (2,701.83 + 658.96) on equity 22,634.51 = 0.148 (derived; H1 p.7). Debt is 2,036.03 above the post-issue pro forma of 1,324.76 (Annexure ZC, Pros p.212-213), so about Rs 20.4 Cr of new debt was drawn net after the Rs 115 Cr repayment (derived).

### N7. IPO proceeds and the equity-side cash flow (Share capital, reserves, events) 🟡
- Gross issue: 52,84,800 shares at Rs 270 = 14,268.96 lakh (Pros p.238, derived 5,284,800 x 270). Cash flow "proceeds on issue of shares" in H1 FY27 is 12,244.66 (H1 p.8) = capital 528.48 + premium net 11,716.18 (reserves 20,134.53 - 6,979.66 - H1 PAT 1,438.69, derived, H1 p.7). So 2,024.30 of issue cost was charged to securities premium (derived: 14,268.96 - 12,244.66).
- The CARE monitoring agency report shows offer-related expenses utilised 23.87 Cr (2,387 lakh) vs 24.05 Cr allowed (NSE p.6-7). 2,387 - 2,024.30 = 362.70 lakh of offer cost did not go through premium. 2,387 / 1.18 = 2,022.9, which matches the 2,024.30 within 1.4. [INFERENCE: 362.70 is GST at 18% on offer expenses, held as recoverable and probably inside short-term loans and advances (rose 429.88 in H1, H1 p.8); not stated.] If true, GST receivable grows by about 3.6 Cr from IPO costs.
- Monitoring agency flags: "(a) Deviation from the objects: Yes", "Range of Deviation: Not Applicable" (NSE p.3); "Whether all utilization is as per the disclosures in the Offer Document? No" (NSE p.4), though another line says no shareholder approval was needed because "there is no material deviation" (NSE p.4). Unutilised 0.13 Cr: 0.09 in the public offer account and 0.04 "with the selling shareholder due to excess amount transferred", received back on 4 November 2026 (NSE p.3). The offer is described as "fresh issue" only (NSE p.4), so a "selling shareholder" holding money is unexplained. Utilisation: debt repayment 115.00 Cr (113 Cr car loan and term loan, 2 Cr working capital); general corporate purposes 3.69 vs 3.64 allowed, of which 2.80 Cr repaid long term debt and 0.89 Cr bought machinery. For the 0.89 Cr: "funds were transferred to the CC account ... numerous other debits and credits ... resulting in comingling of funds, and we have relied on management declarations and CA certificate" (NSE p.6, p.8). The monitoring agency did not independently verify. 🟡
- Pre-IPO placements: 6.80 + 7.00 lakh shares at Rs 101 raised 138.00 + 1,255.80 = 1,393.80; placement expenses of 113.05 were charged to premium (Annexure A, Pros p.188) = 8.1% of the raise (derived). Allottees: NOT FOUND in the restated notes. The IPO price is 2.67x the placement price within about 11 months (derived: 270 / 101). 🟡
- Chronology: the monitoring agency agreement is dated 31 January 2026 (NSE p.2). The Prospectus gives the Board authorisation of the Offer as 13 June 2026 and the shareholder resolution as 15 June 2026 (Pros p.236-237, p.241), and the DRHP Board approval as 25 June 2026. The litigation materiality policy is dated 20 June 2025 (Pros p.239). Earlier approvals are not recorded in the pages read. 🟢/🟡 (ask for dates).
- The Board approved the audited FY26 statements on 13 June 2026 (Pros p.237), but the FY26 auditor's report and the director signatures are dated 18/06/2026 (AFS p.6, p.37). The audit report is dated five days after Board approval. The CS signature shows "Date: 18/06/2025" on AFS p.37, which may be OCR or a typo (check the page image). 🟡

### N8. Compliance, related party and disclosure links not in pass 1 (RPT / Borrowings / Provisions) 🟡
- Past Board reports "omitted disclosures of funds accepted from directors/relatives and a report on CSR applicability along with the formation of the CSR Policies" and DPT-3 forms "were also filed with some clerical mistakes ... cannot be revised" (Pros p.27). Promoter and relative loans at 31 March 2026 are 433.89 (Annexure B, Pros p.190) and Vipul Vashi (relative) lent 100.00 in FY24 and FY25 (Annexure ZA, Pros p.210). Link: director and relative loan reporting under the Companies Act was defective in the past, on the same loans that fund the capex bridge. 🟡
- Delayed ROC filings listed, FY22 to FY26, 20 forms, the longest 78 days (PAS-3); FY26: MGT-14 48 days, DIR-12 33 days, AOC-4 XBRL 22 days (Pros p.27). Late fees paid; no show cause notice received. 🟢/🟡
- CSR: required 11.28 in FY24, nil in FY25 ("threshold not met"), 17.81 in FY26 (Annexure ZK, Pros p.217-218), swings that sit alongside the Board report omission above. FY26 spend 18.00 is booked as "Provision for CSR Exp" (Annexure Y) and no CSR liability line appears in provisions (Annexure H holds only tax 561.78 and gratuity 0.03, Pros p.199). Paid or unpaid: NOT FOUND. 🟡
- Civil litigation: one suit at Bhachau, Kutch (Regular Civil Suit 107/2022) over a promised plot and a service station building, 4.00 lakh claimed, pending at the plaintiff evidence stage (Pros p.239-240). Not in Annexure Z (nil). Immaterial in size. 🟢
- Group company: criminal complaint against Darpan Infrastructure Pvt Ltd (IPC 420 and 406), Kolkata, filed 2015, amount "unascertainable", the company has no case papers (Pros p.241-242). Darpan is the guarantor, collateral owner (Plot 201, also the registered office), lender and construction contractor (pass 1). 🟡
- Warranty and defect liability: a search of the Prospectus for warranty, defect liability and liquidated damages found only a generic sale-of-goods legal passage (Pros line 8612, about p.129-130) and a bank guarantee list (Pros line 14254, p.224-225). No warranty provision, policy or claim history is disclosed. NOT FOUND IN DOCUMENT. 🟡
- Foreign exchange: capital goods imports 890.21 in FY26 (nil in FY25) with capital creditors 1,036.39 at year end (Pros p.215, 199). The Annexure ZG3 exposure table lists only receivables and advances, both nil (Pros p.217), so unhedged payable exposure is not disclosed. NOT FOUND IN DOCUMENT. 🟡
- Imports of raw material: Annexure ZF2 reports raw material 100% indigenous (Pros p.216), but the purchase table shows imported goods 20.98 (0.25%) (Pros p.124) and ZF1 shows component and spares imports 24.29. Small mismatch. 🟢

### N9. Audited ratios note: what does and does not reproduce (AFS note 38) 🟡
Pass 1 flagged debt-equity and inventory turnover. Additional checks (AFS p.37 vs Pros p.213-214 vs derived):

| Ratio (FY26 / FY25) | AFS note 38 | Restated Annexure ZE | Derived |
|---|---|---|---|
| Debt-equity | 1.10 / 0.95 | 1.43 / 1.38 | AFS 1.10 = long term borrowings 9,844.37 / 8,951.16; FY25 3,897.78 / 4,075.16 = 0.96 |
| DSCR | 3.94 / 2.55 | 2.29 / 2.12 | Audited basis: (4,450.25 + 578.58 + 1,130.14) / (578.58 + 2,030.05) = 2.36 using cash flow repayments. Restated basis: (3,662.83 + 1,130.14 + 564.27) / (564.27 + 2,030.05) = 2.07. Neither published DSCR reproduces. FY25 repayments 2,138.73 include refinancing churn (proceeds 2,250.36), so FY25 DSCR on the cash flow is 1.04 |
| Return on equity | 55.20% / 41.42% | 56.53% / 36.28% | Both reproduce on their own PAT and average equity |
| Return on capital employed | 18.50% / 11.25% | 23.05% / 21.84% | Different capital employed definitions |
| Inventory turnover | 117.56 / 63.85 times | 252.85 / 175.06 days | AFS implies an average inventory of 121.9 and 123.1 (derived), almost flat, against true average inventory of 3,136.9 and 1,134.3 |
| Receivables turnover | 4.47 / 5.42 | 82 / 67 days | Reproduces |
| Net profit ratio | 25.09% / 17.79% | 25.57% / 15.66% | AFS uses audited PAT 3,595.25 / 14,326.69; ties |

- The audited note's own words: the current ratio decline "reflects an increase in both current assets and current liabilities"; the receivable turnover decline is due to "extended credit terms offered to customers"; the payable turnover decline is due to "longer credit periods obtained from suppliers" (AFS p.37). These are management's own reasons for the working capital stretch.
- CRISIL's figures are on audited PAT (35.95 Cr, CRISIL p.2), so CRISIL, AFS and the H1 comparatives all use 3,595.25. The Prospectus restated figures use 3,662.83. CRISIL adjusted debt/net worth 1.44 and interest coverage 10.24 (CRISIL p.2), against 1.43 restated and a derived EBITDA / finance cost of 6,108.90 / 594.71 = 10.27. 🟢

### N10. Other items opened by the cross-check documents 🟡
- CRISIL: rated facilities 135 Cr, of which cash credit 12, bank guarantee 3, term loans 7.26 (Bank of Baroda) + 0.80 (Cosmos), and "proposed working capital facility" 111.94 Cr split 66 + 45.94 with no lender named (CRISIL p.3-4). The rating therefore covers 111.94 Cr of unsanctioned working capital debt, 83% of the rated amount (derived). Liquidity "adequate": bank limit utilisation about 84% over the 12 months to 30 June 2026 (CRISIL p.2) against the Prospectus cash credit at 98.7% (31 March 2026) and 99.5% (31 May 2026), pass 1. Different bases (12 month average vs point), not a conflict. CRISIL expects "promoters ... to extend timely, need-based funds (such as equity and unsecured loans)" (CRISIL p.2), the same reliance on promoter money the notes show (433.89 of recallable loans).
- CRISIL projects cash accrual of Rs 80 crore a year (CRISIL p.2) against FY26 PAT + depreciation of 4,792.97 lakh (derived; restated). This is a rating agency projection, not a filed fact. CRISIL's operating income 143.41 Cr (CRISIL p.2) is 14 lakh above the filed revenue 14,326.69. Operating margin "around 40%" is a CRISIL expectation, not a note. 🟡
- H1 FY27 balance sheet items against the March 2026 comparative (H1 p.7): short-term loans and advances 5,431.40 (+429.88); other non-current assets 623.77 (+162.83); trade receivables 3,985.78 (+91.24); cash 19.61. The vendor advance split is not available in H1. 🟡
- H1 results notes: AS 17 segment reporting "not applicable"; "figures of the half-year ended 31 March 2026 are the difference between audited full year and the six months to 30 Sep 2025 which were subject to limited review" (H1 p.3, p.5). The limited review conclusion is "not modified" (H1 p.3). No related party disclosure or contingent liability note is given in the H1 results (H1 p.5-6). 🟢/🟡

---

## 4. Items checked and found to need no new comment (no manufactured findings)
- Deferred tax roll: depreciation timing movement (189.97) vs 116.53 = 306.50 ties to the tax shelter 306.51 (Pros p.184-185, p.212). The 43B(h) DTA 45.21 = 263.45 x 17.16% (derived). Net DTA 17.02 ties (4.37 + 0.04 + 45.21 - 32.60). Audited deferred tax asset is 14.46 vs restated 17.02, difference 2.56 = the current tax difference (H1 p.7). 🟢
- Gratuity AS 15 table: DBO roll-forward ties (14.92 + 15.95 + 1.46 - 6.85 = 25.48 vs 25.49 shown, rounding); pass 1 covered the substance (Pros p.182-184, 218-220). 🟢
- Share counts: 9,650,000 + 8,685,000 bonus + 680,000 + 700,000 = 19,715,000 (Pros p.188, 213). After the IPO: 19,715,000 + 5,284,800 = 24,999,800 = H1 share capital 2,499.98 / 10 (H1 p.4). 🟢
- Trade receivable ageing (40.43 vs 40.44), contingent liability and borrowing tables are pass 1.
- Financial instruments, fair value hierarchy, hedging, ESOP, leases (Ind AS 116), goodwill, subsidiaries, JVs: not applicable or nil under the AS framework and the Prospectus (Pros p.221 Annexure ZN-D; no subsidiaries).

---

## 5. Open items carried to pass 3 (need the pending AFS pages)
1. AFS balance sheet, P&L and audited cash flow (p.8-35 area): confirm 1246.70 on the audited statement itself, not only on the H1 comparative; read the audited finance cost note (to place the 127.28 and the guarantee commission 97.60) and the "Other non-current assets" and "Short-term loans and advances" notes (counterparties of vendor advances).
2. CARO clauses after 2(a): 3(ii)(b) quarterly returns to banks, 3(iii) loans and advances, 3(vii) statutory dues, 3(ix) default, 3(x) IPO fund diversion (the offer was after year end, so likely "not applicable"), 3(xiii) related party compliance, 3(xvii) cash losses.
3. Audited notes 1-10 and 13-36 (policies, related parties, contingent liabilities, MSME, tax), compared with the restated annexures reported in pass 1 and here.
4. FY25 and FY24 audited statements (p.42-70, p.79-103) for the restated vs audited bridge.
5. Page image check for AFS p.37 CS date "18/06/2025".

---

## PASS 2 NEW FINDINGS SUMMARY (new items only)

| # | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | FY26 CFO gap test closed: audited 1246.70 vs restated 1843.94. The 597.24 gap is classification: other non-current assets 421.84 in operating (audited) vs investing (restated) = 70.6%; interest 143.41 in operating vs financing = 24.0%; residual 32. Net cash change is the same 147.14. Audited "tax paid" 851.19 is the P&L charge, offset in working capital. Common-basis CFO is Rs 6.3 to 10.1 Cr (derived), 17.6% to 27.6% of PAT. | H1 p.8; Pros p.174, p.199, p.203 | 🔴 |
| 2 | Section 115BAB concessional tax is under challenge: demand 367.25 for AY 2025-26 dated 17 Jul 2026, after year end, no provision, absent from the post balance sheet list. Derived exposure if denied for FY24 to FY26 is 515.50 lakh (Rs 5.2 Cr) before interest. Two earlier demands (226.93) were also portal demands. | Pros p.240-241, p.91, p.212, p.236-237 | 🔴 |
| 3 | Two trade creditors hold 4,000.93 = 85.7% of payables; one holds 3,545.82 = 76.0% (42.3% of FY26 purchases). The Prospectus says no MSME intimations were received, yet notes show MSME dues 821.94 and 735.61. At 30 Sep 2026 MSME dues are 1,785.48 (69.3% of payables). | Pros p.243, p.198, p.216, p.124; H1 p.7 | 🔴 |
| 4 | Customer concentration is filed (top five 78.75%, Customer 1 29.32%, top ten 97.31%; top ten suppliers 90.11%). Pass 1 NOT FOUND is closed. | Pros p.23-24, p.114 | 🔴 |
| 5 | Order book gives per-tower value: Customer D at 316.48 lakh per tower, 5.4x Customer A, consistent with the integrated model; FY26 had four such towers. Links the inventory build to integrated-supply orders (INFERENCE). | Pros p.114, p.232 | 🟡 |
| 6 | Restated vs audited FY26 P&L fully reconciled: materials 359.52 reclassified, PBT 0.22, tax 2.56 + 1.80, earlier-year tax 83.40 charged in audited FY26 and added back in restated. The choice of 3595.25 vs 3662.83 must be named. Rent income 35.00 is a first-half FY26 item. | H1 p.4; Pros p.173, p.187, p.207 | 🟡 |
| 7 | CARO 2(a): inventory lying with third parties, amount NOT FOUND, against inventory 5,068.78 and fabrication cost 1,282.41. | AFS p.7; Pros p.209 | 🟡 |
| 8 | FY27 depreciation run-rate: H1 FY27 D&A 1,286.53 = 113.8% of FY26 full year (1,130.14); annualised 2.28x. Intangible amortisation 0.01 in FY26 vs about 6 a year run-rate. CWIP 3,069.27 at Sep 2026. | H1 p.4, p.7; Pros p.208 | 🟡 |
| 9 | IPO proceeds: premium absorbed 2,024.30 vs monitoring agency offer cost 2,387 (362.70 difference, INFERENCE GST). Monitoring agency flags "Deviation from the objects: Yes", "utilisation as per Offer Document: No", comingling of funds on 0.89 Cr and a "selling shareholder" in a fresh-only issue. Debt is 20.4 Cr above the post-issue pro forma at 30 Sep 2026; gearing 0.148 vs CRISIL 0.05 expected by March 2027. | NSE p.3-4, p.6-8; H1 p.7-8; CRISIL p.1 | 🟡 |
| 10 | Governance chronology and compliance: audited FS Board approval 13 Jun 2026 vs auditor report 18/06/2026; past Board reports omitted director/relative funds and CSR disclosure; 20 delayed ROC forms; DPT-3 errors "cannot be revised"; Darpan criminal case (2015). Warranty provision and FX payable exposure NOT FOUND. | Pros p.27, p.237, p.241-242; AFS p.6, p.37 | 🟡 |
| 11 | Audited ratio note 38: DSCR 3.94 and 2.55 not reproducible (derived 2.36 on audited basis); inventory turnover implies an average inventory near 122 (flat), not 3,137. Management's own reasons name longer supplier credit and extended customer credit. | AFS p.37; Pros p.214 | 🟡 |
| 12 | CRISIL rates 111.94 Cr of "proposed working capital" (83% of 135 Cr rated), expects promoter funds as needed, and leans on audited PAT 35.95 Cr. | CRISIL p.1-4 | 🟡 |
