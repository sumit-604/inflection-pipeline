# STAGE 2, PASS 1 (FULL EXTRACTION): Creative Newtech Ltd (CNL), run 2026-11-11

Source: runs/cnl-2026-11-11/inputs/annual-report/CNL_AR_FY2025-26.txt (page-marked text; marker `[page N]` precedes its page, so "AR p.N" is the marker number).
Unit on the face of both sets of statements: **Rs. in Lakhs** (standalone p.73, consolidated p.97). Everything below is in Rs. Lakhs unless stated. Nothing is converted; stage 10 converts once (100 Lakhs = 1 Cr is a unit identity only).
Standalone Notes 1-46 (AR p.75-91) and Consolidated Notes 1-39 (AR p.99-112) were both read in full, with sub-notes and footnotes. Standalone is "SA", consolidated is "CON". Where the CON note is identical to the SA note, that is stated.
Items taken from outside the notes (AOC-1, auditor's Other Matters, notice) are labelled "OUTSIDE NOTES" and are there only to test the load-bearing facts.
Company memory (companies/CNL.md, step1-business-brief.md) was weighed, never used as a source. Figures in memory given in Cr are compared by identity only.

Rating key: 🟢 Clean | 🟡 Watch | 🔴 Red Flag. Derived figures (my arithmetic on disclosed numbers) are marked "derived".

---------------------------------------------------------------------
## A. LOAD-BEARING FACTS: VERIFICATION RESULT (first priority)

**LB1. Hong Kong subsidiaries: profit, tax, minority.** PARTLY VERIFIED FROM FY26 AR. Q2 FY27 data is not in the AR.
- OUTSIDE NOTES, Form AOC-1 (AR p.63, Rs. Lakhs, HK$ = INR 12):

| Item | Creative Peripherals & Distribution Ltd (CPDL, 100%) | Secure Connection Ltd (SCL, 77.50%) |
|---|---|---|
| Turnover / total income | 1,681.77 | 29,773.63 |
| Profit/(loss) before tax | (31.04) | 3,742.90 |
| Provision for taxation | Nil | Nil |
| Profit/(loss) after tax | (31.04) | 3,742.90 |
| Reserves & surplus | 237.17 | 11,844.33 |
| Total assets / total liabilities | 1,314.66 / 1,028.68 | 13,713.55 / 1,868.00 |
| Proposed dividend | Nil | Nil |

- Auditor's Other Matters (AR p.93) repeats the same revenue and PAT, and says these two subsidiaries' statements are "not audited by us" (see F42).
- CON Note 34-30 tax reconciliation (CON Note 30, AR p.108): tax at 25.17% on CON PBT 8,176.20 = 2,057.95; "Effect of differences in Tax Rates of subsidiaries operating in other jurisdictions" (904.84); tax recognised 1,153.11. SA current tax is also 1,153.11 (SA Note 30, AR p.85). So CON tax equals SA tax to the rupee: the HK profit is untaxed in the numbers. Derived: 904.84 / 25.17% = 3,594.9 of pre-tax profit carries zero tax, near SCL PBT 3,742.90 plus CPDL loss.
- Minority: NCI profit share 842.15 (CON P&L, AR p.97) = 22.5% x 3,742.90 (derived, exact). NCI balance 1,524.25 to 2,366.40, a rise of 842.15 (CON BS, AR p.97). Minority is 11.98% of CON PAT 7,029.29 (derived).
- SA PAT 3,434.75 vs CON PAT 7,029.29 (AR p.73, p.97): subsidiaries and eliminations add 3,594.54 = 51.1% of CON PAT (derived). Memory's Q2 FY27 pattern (same tax in both, PAT doubling) is the same pattern as the FY26 full year.
- Identity of the 22.5% holder: NOT FOUND IN DOCUMENT in the notes.
- Reason for nil HK tax (offshore exemption or loss set-off): NOT FOUND IN DOCUMENT. DTL on undistributed subsidiary earnings (Ind AS 12.39) and India tax on remittance: NOT FOUND IN DOCUMENT.
- Dividend received from either subsidiary: NOT FOUND IN DOCUMENT (SA Note 24 has none; AOC-1 proposed dividend Nil).
- Derived reconciliation of CON PBT: SA PBT 4,581.66 + SCL 3,742.90 + CPDL (31.04) + associate loss (5.40) - unrealised-profit adjustment 164.69 (CON Note 26) = 8,123.43, vs CON PBT 8,176.20. Unexplained residual 52.77 (0.65% of CON PBT); the notes give no bridge.

**LB2. Receivables ageing and FY26 operating cash outflow.** VERIFIED. CFO is CON (27,188.34) (AR p.98) and SA (25,738.12) (AR p.74). Memory's -Rs 271.9 Cr matches the CON figure by unit identity. Drivers are in F23 and F43. Receivables ageing in F21-F22. H1 FY27 turn: outside the AR, not testable here.

**LB3. Brand segment reported with its own result?** YES, in the notes. Brand Business and Market Entry Specialist are reported segments with revenue, result, assets and liabilities (CON Note 37, AR p.111-112; SA Note 39, AR p.89-90). Segment result is "net revenue after deducting allocable cost", not gross margin. The 40-42% brand gross margin: NOT FOUND IN DOCUMENT (no segment cost of goods). Brand share of FY26 CON segment revenue is 14.11%, against 15.25% in FY25 (derived). See F40.

**LB4. BSNL BharatNet order.** NOT FOUND in the notes. "BSNL" and "BharatNet" do not appear anywhere in the AR text. SA Note 44(k) and CON Note 38(k) say no significant subsequent events. Contracting entity, guarantees and funding need: NOT FOUND IN DOCUMENT.

---------------------------------------------------------------------
## B. NOTE-BY-NOTE EXTRACTION (findings F1 to F54)

### 1. ACCOUNTING POLICIES AND CHANGES

**F1. Leases treated as short-term; no ROU asset or lease liability.** 🟡 SA Note 2(q) (AR p.78-79), SA Note 41 (AR p.90); CON Note 2(p) (AR p.102-103). Premises are accounted "as a short term lease", cancellable on 1 to 3 months' notice; rent charged straight-line. SA rent, rates and taxes 327.09 (FY25 316.36) (SA Note 29, AR p.85); CON 327.34. ROU asset, lease liability, discount rate: NOT FOUND IN DOCUMENT. Branch premises that are renewed continuously sit awkwardly with the short-term exemption; cost of the choice is not quantified.

**F2. Depreciation and amortisation.** 🟢 SA Note 2(d)/(e) (AR p.76-77): written-down-value method, Schedule II lives. Buildings 60 yrs, vehicles 8, furniture 10, electrical 10, office equipment 5, computers 3. Residual value up to 5%. Software 3 yrs, customised software 10 yrs. No change in lives or method disclosed. Capitalisation threshold: NOT FOUND IN DOCUMENT. SA depreciation 142.57 = 108.54 PPE (SA Note 2, AR p.79) + 34.03 amortisation (SA Note 4, AR p.80). Software in CWIP 214.64 transferred to intangibles in FY26 (SA Note 3, AR p.80). PPE impairment: management concluded none required (SA Note 2 note ii, AR p.79). Impairment test assumptions (growth, discount rate): NOT FOUND IN DOCUMENT.

**F3. ECL policy.** 🟡 SA Note 2(o) (AR p.78): lifetime ECL on trade receivables, "12-month ECL" otherwise. No provision matrix or loss rates by age bucket. Allowance is judgemental: "on the best estimate basis" (SA Note 32, AR p.86). Allowance 76.77 against gross 55,214.80 (54,978.14 + 236.66) = 0.14% (derived).

**F4. Revenue recognition wording.** 🟡 SA Note 2(l) (AR p.78), CON Note 2(k) (AR p.101-102). Policy uses pre-Ind AS 115 "risks and rewards" language. Point-in-time recognition (SA Note 23.1, AR p.84). "No element of financing is deemed present". Export entitlements recognised in revenue from operations: 484.47 (FY25 827.67). Principal vs agent judgement (relevant to a pass-through distributor booking gross): NOT FOUND IN DOCUMENT. Key audit matter on revenue and rebates exists (OUTSIDE NOTES, AR p.91-92).

**F5. Policy changes and first-time adoptions.** 🟢 None quantified in the notes. Prior-period figures "regrouped / restated wherever necessary" (SA Note 45, AR p.91; CON Note 39, AR p.112) with no amounts. Code on Social Security 2020 impact deferred (SA Note 44(i), AR p.91).

### 2. RELATED PARTY TRANSACTIONS (SA Note 36, AR p.88-89; CON Note 35, AR p.110-111)

Full SA table, Rs. Lakhs. YoY is derived. CON table is the SA table with the SCL and CPDL rows removed; every other row is identical.

| Party | Relationship | Nature | FY26 | FY25 | YoY |
|---|---|---|---|---|---|
| Secure Connection Ltd (HK) | Subsidiary 77.50% (also listed under KMP-influence entities) | Purchases | 15,539.15 | 10,008.93 | +55.3% |
| Secure Connection Ltd (HK) | same | Sales | 2,208.54 | 20.64 | +10,600% |
| Creative Peripherals & Distribution Ltd (HK) | Subsidiary 100% (also listed under KMP-influence entities) | Purchases | 574.91 | 2,150.01 | -73.3% |
| Click Retail Pvt Ltd | KMP-influence entity | Purchases | 522.20 | 128.39 | +306.7% |
| Click Retail Pvt Ltd | same | Sales | 2,677.91 | 770.07 | +247.8% |
| World EMS Pvt Ltd | same | Sales | 2,669.81 | 4,991.45 | -46.5% |
| Secure Connection Pvt Ltd (India) | same | Purchases | 303.80 | 371.25 | -18.2% |
| Secure Connection Pvt Ltd (India) | same | Sales | 256.45 | 620.31 | -58.7% |
| Compunics Technologies LLC | same | Sales | 173.12 | 2.30 | +7,427% |
| 1008 Digital Health Pvt Ltd | same | Purchases / Sales | 115.01 / 2.72 | 105.02 / 107.17 | +9.5% / -97.5% |
| Creative eCommerce Ventures Pvt Ltd | Associate 49% | Purchases / Sales | 59.28 / 17.82 | nil / 49.56 | new / -64.0% |
| Exfaq Systems Pvt Ltd | KMP-influence | Sales | 50.12 | 121.53 | -58.8% |
| Bittech Services | same | Purchases / Sales | 47.12 / 14.74 | 165.11 / 52.92 | -71.5% / -72.1% |
| Shilpa Global Pvt Ltd | same | Purchases (premises) | 6.72 | 6.72 | 0% |
| Lumisynch Pvt Ltd | same | Purchases | 2.52 | nil | new |
| Citizencenter Tech / World Goods Mkt / World EMS / Euphoriya Hospitality | same | Purchases / Sales (small) | 0.30 / 0.06 / nil / 0.06 | 0.24 / 0.84+35.21 / 1.03 / nil | n.m. |
| Ketan C Patel (CMD, promoter) | KMP | Remuneration incl. bonus | 112.23 | 102.58 | +9.4% |
| Vijay Advani (WTD) | KMP | Remuneration | 64.71 | 58.23 | +11.1% |
| Purvi K Patel (spouse) | Director to 11-Aug-2025, then Chief Strategy Officer from 26-Aug-2025 | Director remuneration / Salary | 22.88 / 58.31 | 68.20 / nil | -66.5% / new |
| Nidhi Patel | Relative of director | Salary | 40.99 | 30.75 | +33.3% |
| Abhijit Kanvinde (CFO to 14-Apr-2026) | KMP | Remuneration | 50.12 | 45.92 | +9.1% |
| Tejas Doshi (CS) | KMP | Remuneration | 34.76 | 32.27 | +7.7% |
| Ketan C Patel | Promoter | Dividend paid | 42.20 | 39.70 | +6.3% |
| Ketan C Patel | Promoter | Loan received / repaid | 341.61 / 353.74 | 1,671.36 / 1,676.52 | -79.6% / -78.9% |
| Ketan C Patel | Promoter | Interest paid | 4.49 | 20.97 | -78.6% |
| Creative eCommerce Ventures | Associate | Investment | nil | 404.15 | n.m. |

Outstanding balances (positive = receivable, bracket = payable), SA, FY26 / FY25: Click Retail 4,773.50 / 222.83; Secure Connection Pvt Ltd 452.97 / 1,542.20; Bittech 336.00 / 15.54; CPDL (HK) 911.52 / 959.48; World EMS 733.13 / 1,128.71; SCL (HK) (3,093.04) / 274.99; Compunics 70.26 / 2.30; Exfaq 50.17 / 48.11; Creative eCommerce 44.59 / 20.12; 1008 Digital 0.08 / 302.21; Rinavaa (91.48) / (91.50); Shilpa Global (8.48) / nil; Lumisynch (1.52) / nil; Ketan Patel unsecured loan (7.59) / (15.68).

**F6. HK subsidiary flows grew sharply and reversed direction.** 🟡 SA Note 36 (AR p.88-89). Purchases from SCL 15,539.15 = 6.25% of SA purchases of stock in trade 248,723.17 (derived) and 52.2% of SCL's total turnover 29,773.63 (AOC-1, derived). Sales to SCL rose from 20.64 to 2,208.54. Purchases from CPDL fell 73.3%. SCL is the Honeywell licence holder (OUTSIDE NOTES, AR p.30). Transfer-pricing basis and any intra-group margin policy: NOT FOUND IN DOCUMENT. Only one consolidation elimination is quantified: unrealised profit adjustment 164.69 (FY25 125.32) (CON Note 26, AR p.107).

**F7. Balance with SCL swung from receivable to payable.** 🟡 SA Note 36 (AR p.89): from 274.99 receivable to (3,093.04) payable. CNL's growth in purchases from SCL appears to be financed on supplier credit from the 77.5% sub, while SCL's own cash is small: CON cash 535.96 minus SA cash 475.97 = 59.99 for both subsidiaries (derived; CON Note 9 / SA Note 9, AR p.105 / p.81), against SCL reserves of 11,844.33 (AOC-1). Profit is booked in the sub but is not sitting in cash there.

**F8. Click Retail balance exceeds a year of sales.** 🟡 SA Note 36 (AR p.88-89). Balance 4,773.50 (from 222.83) vs FY26 sales to Click Retail 2,677.91 and purchases 522.20. Balance is 1.78x annual sales (derived), so part is non-trade or very long-dated. Click Retail is one entity in the promoter-family influence list.

**F9. RPT receivable table does not tie to Note 8.** 🟡 Sum of positive SA balances excluding SCL payable is 7,372.22 (derived), against "Trade receivables from Related Parties" 3,244.81 (SA Note 8, AR p.81). FY25: 4,522.27 vs 1,946.25. CON: positive balances 6,460.70 vs CON Note 8 related-party receivables 3,244.81 (AR p.104), which is the same figure as SA even though SCL/CPDL balances are eliminated. The difference (3,215.89 in CON, derived) is not explained; likely advances or other-asset balances, but the notes do not say.

**F10. RPT as % of revenue and purchases.** 🟡 Derived, SA. Sales to related parties FY26 8,071.35 = 3.16% of revenue from operations 255,600.47 (FY25 6,736.79 = 4.09% of 164,682.47). Purchases from related parties FY26 17,171.01 = 6.90% of purchases 248,723.17 (FY25 12,971.91 = 8.15% of 159,078.57). Of FY26 related-party sales, 27.4% is to SCL (2,208.54) and 33.2% to Click Retail (2,677.91); World EMS 33.1% (2,669.81).

**F11. Pay to the promoter family.** 🟡 SA Note 36 (AR p.88). Ketan Patel 112.23 plus 1.84 benefits; Purvi Patel 22.88 plus 0.49 plus new salary 58.31 as Chief Strategy Officer; Nidhi Patel salary 40.99. Promoter-family compensation total 236.74 (derived), vs director remuneration expense 200.61 (SA Note 29, AR p.85). Purvi Patel moved from director to employee-officer in August 2025 and her pay stayed in the family; salary of Nidhi Patel rose 33.3%. Royalty, rent to the promoter family: only Shilpa Global purchases 6.72 and an SBI mortgage on Shilpa Global's premises (F12).

**F12. Promoter support to the company.** 🟡 Personal guarantees by Ketan and Purvi Patel on term loans (SA Note 15(d), AR p.83) and by "Director and Whole-time director" on cash credit and buyer's credit (SA Note 17(d), AR p.83). Gala No. 1, 2nd Floor, Charkop, owned by Shilpa Global Pvt Ltd (related party), is mortgaged to SBI as security (SA Note 15(c), AR p.83). Unsecured loan from Ketan Patel 7.59 at 12% p.a. (SA Note 17(e)), above the 9% to 11% bank range. Guarantee fee paid to promoters: none shown. Loans to promoter entities: NONE FOUND (SA Note 44(e), AR p.90). Shilpa Global appears in RPT purchases at 6.72, unchanged from FY25, so the mortgage is provided without disclosed consideration.

**F13. Related-party universe and new parties.** 🟡 28 entities plus KMP listed (SA Note 36 A, AR p.88): includes 11 "PG" companies (Patel Growth, PG Arise, PG Blooming, PG Gem, PG Goals, PG Infinite, PG Shine, PG Upswing, PG Vision, Sustainable PG, Uptrend PG) with no transactions shown, plus Lumisynch and Euphoriya Hospitality that transact in FY26 only (nil in FY25). Two entities named Secure Connection exist: the Indian Pvt Ltd (arm of KMP-influence) and the HK Ltd (subsidiary). SCL and CPDL appear both as subsidiaries and as entities "where KMP or relatives have significant influence", so the KMP also has a personal interest in the subsidiaries; the holder of the 22.5% SCL minority is not named. Prior-year related-party list, to say which entities are newly added: NOT FOUND IN DOCUMENT.

**F14. CFO turnover.** 🟡 SA Note 36 A (AR p.88): CFO Abhijit Kanvinde ceased 14-Apr-2026; Ajit Kumar Thakur appointed 14-May-2026, the same day the board approved the accounts (SA Note 46, AR p.91). A new CFO signed accounts on his first day.

**F15. FY27 SCL transaction approval (OUTSIDE NOTES).** 🟡 Notice item 4 (AR p.30): aggregate transactions with SCL up to Rs. 750 Crores for FY27, material RPT under Reg 23. FY26 actual purchases plus sales with SCL were 17,747.69 Lakhs (derived), so the ask is a large multiple of FY26 actuals (Rs. 750 Crores vs 17,747.69 Lakhs; stage 10 converts).

### 3. CONTINGENT LIABILITIES (SA Note 35, AR p.87; CON Note 34, AR p.109-110; identical)

| Nature | FY | FY26 | FY25 | Stage / company view |
|---|---|---|---|---|
| Income tax demand | 2007-08 | 5.26 | 5.26 | Portal error, correction sought |
| Income tax interest | 2007-08 | 10.30 | 10.00 | same |
| Income tax incl. interest | 2017-18 | 6.34 | 6.09 | same |
| Income tax interest / penalty (bogus purchase allegation) | 2008-09 | 3.45 / 3.96 | 3.22 / 3.96 | Appeal pending, "unjustified" |
| Income tax and interest | 2019-20 | 38.91 | 37.39 | CPC clerical error, follow-up |
| GST DGGI Delhi (ITC) | order 2024 | 191.44 | 191.44 | Writ in Punjab and Haryana HC |
| GST New Delhi | 2018-19 | 28.08 | nil | Appeal filed 28-Mar-2026 (incl penalty 14.04) |
| GST Hyderabad | 2020-21 | 7.79 | 7.90 | Appeal filed |
| GST West Bengal | 2018-19 / 2019-20 | 42.59 / 16.81 | 4.00 / 16.81 | Appeal filed FY27 |
| GST Maharashtra | 2021-22 | 202.61 | nil | Appeal filed FY26 |
| GST New Delhi | 2020-21 | 25.46 | nil | Appeal filed |
| GST Uttar Pradesh | 2019-20 / 2020-21 | nil | 12.55 / 9.22 | Deleted in company's favour |
| VAT/CST Gujarat | 2014-15 | 12.48 | 18.16 | VAT 6.67 paid in FY27 |
| Customs duty demand | 2018-19 | 4.53 | nil | Disputed, no provision |
| Bank guarantee | n/a | 1,058.13 | 793.01 | Given by banks for the company |

**F16. Totals and net-worth test.** 🟡 Derived. Excluding bank guarantees: FY26 600.01 (income tax 68.22, GST 514.78, VAT 12.48, customs 4.53); FY25 326.00; up 84.0%. Including bank guarantees: FY26 1,658.14, FY25 1,119.01. Against SA total equity 29,949.67: 2.00% (5.54% with guarantees). Against CON total equity 38,729.29: 1.55% (4.28%). Largest single item 202.61 (Maharashtra GST) = 0.68% of SA equity. No item exceeds 10% of net worth.

**F17. Tax dispute composition has moved to GST.** 🟡 GST share 514.78 of 600.01 = 85.8% (FY25 241.92 of 326.00 = 74.2%) (derived). New in FY26: Maharashtra 202.61, Delhi 28.08 and 25.46, Customs 4.53, West Bengal 2018-19 up from 4.00 to 42.59. Cumulative GST orders cover wrong SGST/CGST rate, excess ITC, short payment (SA Note 35 notes v-vi, AR p.87). No provision is held for any. GST audit orders from four states in one year suggest the product-rate classification issue is recurring.

**F18. Customs duty paid under protest sits in assets.** 🟡 Duties and taxes receivable includes custom duty 694.72 paid under protest (SA Note 12, AR p.82, cross-referring to Note 35). Note 35(ix) (AR p.87-88) describes an Order-in-Original of 28-Feb-2019 for duty 2,30,33,813 and penalties 4,61,38,438 and 20,00,000, says CESTAT ruled for the company on 11-Apr-2023, yet the same paragraph also says the company "believed that this position will likely be upheld", and the item is not in the table (customs shown only as 4.53). Derived: 230.34 + 461.38 = 691.72, close to 694.72. The recoverable status after the 2023 order, and why it is still an asset three years on, is not stated. The text also gives the penalty as ...438 once and ...428 once.

**F19. Guarantees and commitments.** 🟡 Bank guarantee 1,058.13 (FY25 793.01), +33.4%, backed by margin money 1,670.99 (SA Note 10, AR p.81). Corporate guarantees for subsidiaries: NOT FOUND IN DOCUMENT. Capital commitments: NOT FOUND IN DOCUMENT. Letters of credit outstanding amount: NOT FOUND IN DOCUMENT (Note 10 says margin money also covers LCs). Any guarantee or bank guarantee tied to a BSNL project: NOT FOUND IN DOCUMENT.

**F20. Litigation provisions.** 🟢 None made; only provisions are employee benefits (SA Note 16 and 21, AR p.83).

### 4. TRADE RECEIVABLES (SA Note 8, AR p.81; CON Note 8, AR p.104)

SA ageing, Mar-2026 (from due date): undisputed good <6m 53,258.97; 6m-1y 1,258.05; 1-2y 431.67; 2-3y nil; >3y 29.45; total 54,978.14. Disputed good: <6m 0.21; 2-3y 149.37; >3y 87.08; total 236.66. Allowance (76.77). Net 55,138.03.
SA ageing, Mar-2025: <6m 20,376.47; 6m-1y 109.64; 1-2y 222.19; 2-3y 8.46; >3y 90.09 (undisputed 20,806.85); disputed 1-2y 10.95, >3y 76.13 (87.08). Allowance (22.73). Net 20,871.20.
CON ageing Mar-2026: <6m 54,632.17; 6m-1y 1,258.05; 1-2y 431.67; 2-3y 149.37; >3y 116.53; net 56,511.02. Mar-2025: <6m 23,282.25; 6m-1y 109.64; 1-2y 222.19; 2-3y 19.41; >3y 166.22; net 23,776.98. The extra CON balance is all in the <6m bucket (HK sub receivables).

**F21. Over-6-month balance rose.** 🟡 Derived, SA. >6 months FY26 1,955.62 = 3.54% of gross 55,214.80; FY25 517.46 = 2.48% of gross 20,893.93. The 6m-1y bucket grew 11.5x (109.64 to 1,258.05). The headline is still dominated by <6m (96.5% of gross). CON: >6m 1,955.62 (3.40% of gross 56,587.79, derived).

**F22. Disputed receivables and thin allowance.** 🟡 Disputed 236.66 (FY25 87.08), of which 149.37 now sits in 2-3 years and 87.08 is >3 years old, against an allowance of 76.77: coverage 32.4% (derived). Incremental provision charged in FY26 is 54.04 (SA Note 29 and Note 32, AR p.85-86) against a 149.58 rise in disputed balance (36.1%). Undisputed 1-2 year balance 431.67 carries no allowance. The 2-3 year disputed 149.37 cannot have been under one year old at Mar-2025 (FY25 disputed 1-2y was only 10.95), which implies reclassification of earlier undisputed balances (FY25 undisputed 1-2y 222.19) into "disputed"; the notes do not say so.

**F23. Receivable days and growth.** 🔴 Derived on revenue from operations (ex-GST) vs receivables (inclusive of GST): SA FY26 78.7 days, FY25 46.3 days; CON FY26 76.3 days, FY25 48.7 days (matches memory's 76 and 49). Three-year trend: FY24 balance sheet NOT FOUND IN DOCUMENT; only two years are available. Receivables +164.2% SA (+137.7% CON) vs revenue +55.2% SA (+51.7% CON). Note 43 turnover ratio 6.71 vs 10.05, -33.24%, "proportionately higher rise in the trade receivables" (SA Note 43, AR p.90). The increase in receivables, 34,266.83 SA / 32,734.04 CON (cash flow, AR p.74 / p.98), exceeds the whole operating outflow.

**F24. Concentration and related-party receivables.** 🟡 Single customer above 10%: NOT FOUND IN DOCUMENT (no concentration note). Related-party receivables 3,244.81 = 5.9% of gross SA receivables (derived), up from 1,946.25.

**F25. Factoring, bill discounting, TReDS.** 🟡 NOT FOUND IN DOCUMENT. No disclosure of receivables transferred, discounted or derecognised (policy on derecognition exists at SA Note 2(i), AR p.77, but there is no transaction note). Borrowing type split (cash credit, buyer's credit, WCDL, NBFC): NOT FOUND IN DOCUMENT. The FY26 CFO source test in LB2 cannot be settled from the notes on this point.

### 5. INVENTORY (SA Note 7, AR p.81; CON Note 7, AR p.104)

**F26. Inventory.** 🟡 Single line "Stock in Trade": SA 13,188.06 (FY25 8,398.80); CON 17,344.58 (10,571.32). No category split, no write-down, no obsolescence disclosure: NOT FOUND IN DOCUMENT. Valued at lower of cost (FIFO) and NRV; "as taken, valued and certified by Management". Growth: SA +57.0% vs revenue +55.2%; CON +64.1% vs revenue +51.7% (derived). Inventory days on cost of goods sold (purchases plus change in stock): SA 19.7 (FY25 19.5); CON 25.5 (23.7) (derived). Inventory turnover 22.60 vs 21.02 (SA Note 43). Inventory is a key audit matter (OUTSIDE NOTES, AR p.92). The faster CON inventory rise points to the HK subsidiaries holding the extra stock (CON minus SA = 4,156.52, derived).

### 6. INVESTMENTS (SA Note 5, AR p.80; CON Note 5, AR p.104)

**F27. Subsidiaries and associate, SA carrying value.** 🟢 Creative Peripherals & Distribution Ltd (HK): 5,46,000 shares of HKD 1, 100%, 48.81. Secure Connection Ltd (HK): 10,333 shares of HKD 1, 77.50%, 3,060.65. Creative eCommerce Ventures Pvt Ltd: 49%, 405.15 (8,18,300 shares at Rs. 50, premium Rs. 40; FY25 purchase of 8,08,300 shares for 404.15). Total 3,514.61, unchanged year on year, no impairment (SA Note 5 and p.80 table). The 3,060.65 carrying value for SCL sits against SCL equity of 11,845.55 (1.22 + 11,844.33, AOC-1, derived).

**F28. Associate.** 🟡 Share of loss in CON (5.40) FY26 and (51.70) FY25; CON carrying 275.18 (from 280.58) (CON Note 5, AR p.104). AOC-1 reports associate loss (11.08), net worth attributable 314.34, which is 39.16 above the CON carrying value (derived, unexplained; a 72.87 loss transfer on reclassification to associate is shown in CON Note 5). The company went from 100% to 49% when two other investors paid 425.85 for 8,51,700 shares (SA Note 5 note). Two related parties trading with the associate: purchases 59.28, sales 17.82.

**F29. ICDs and loans given; other investments.** 🟢 None: SA Note 44(e) (AR p.90). No quoted investments, no FVTPL/FVTOCI gains or losses (SA Note 5). Cash flow mentions "Interest on FD and ICD" but no ICD balance exists in any note.

### 7. BORROWINGS (SA Note 15 and 17, AR p.83; CON Note 15 and 17, AR p.106)

**F30. Borrowing instruments.** 🔴 Current borrowings SA 32,424.87 (FY25 6,953.06; +366.4%); CON 32,424.88. Of this, secured loans from banks and NBFCs 32,417.28 (6,937.38) and unsecured loans from directors/related parties 7.59 (15.68). Non-current term loan: SA nil (FY25 226.31, ECLGS from Axis and SBI); CON 1.21 (227.40). All cash credit "payable on demand", rate 9% to 11% p.a.; ECLGS 9% to 11%; director loan 12%. Security: hypothecation of stock and book debts, movable assets, four Mumbai flats/offices, FDs of 0.83 Cr (HDFC) and 0.42 Cr (Axis) as collateral, building and Charkop premises with SBI. Maturity/repayment schedule, covenants, waivers, fixed vs floating, amount per bank, sanctioned limits: NOT FOUND IN DOCUMENT. Five-year repayment schedule: NOT FOUND IN DOCUMENT (liquidity table shows all of it due in 1 to 12 months, SA Note 32, AR p.86). Borrowing funded 25,471.81 of net inflow in FY26 (SA cash flow, AR p.74).

**F31. Gearing.** 🔴 SA gross debt 32,424.87; adjusted net debt 30,266.75 (from 2,667.47); adjusted net debt/equity 1.01 (from 0.10) (SA Note 33, AR p.86). CON 0.83 (0.06) on owners' equity (CON Note 33, AR p.109); gross debt over total equity including NCI = 0.837 (FY25 0.232) (derived; memory's 0.84 and 0.23 match). Note 43 SA debt/equity 1.08 vs 0.27, +301% (AR p.90). Current ratio 1.45 vs 2.12; DSCR 3.67 vs 5.59.

**F32. Finance cost.** 🟡 SA 2,042.92 (994.86); interest to banks 1,494.29 (635.21), others 252.62 (157.62), bank charges 121.96, processing 37.05, BG/buyer's credit charges 125.43 (SA Note 28, AR p.84). Interest as a share of average gross debt: 1,746.91 / 19,802.12 = 8.82% (derived), lower than the stated 9 to 11% range because the borrowing is back-ended. Finance cost is 44.6% of SA PBT (derived). Bank buyers credit expenses in foreign currency 4,493.48 (296.26) (SA Note 37, AR p.89).

### 8. TRADE PAYABLES (SA Note 18, AR p.83; CON Note 18, AR p.106)

**F33. Payables and MSME.** 🟡 SA total 19,963.54 (11,801.62); MSME 3,021.95 (1,192.01), +153.5%. Other 16,941.59. Ageing: all MSME under one year; others 16,888.89 <1y and 52.70 in 1-2 years (FY25 had 28.83 over one year). Disputed dues nil. CON total 18,511.43 (13,534.81). Interest due to MSME vendors 116.76 (14.68), +695% (SA Note 42, AR p.90). Payables >45 days split and whether the 116.76 is accrued in P&L: NOT FOUND IN DOCUMENT. Payable days on purchases: SA 29.3 (27.1); CON 26.5 (29.9) (derived). Payables turnover 15.66 vs 20.18 (SA Note 43). Trade payables rose 69.2% SA vs purchases +56.4% (derived).

### 9. PROVISIONS

**F34. Gratuity (unfunded).** 🟢 SA Note 34 (AR p.86-87). DBO 210.82 (166.92); service cost 20.03 (16.37); interest cost 11.57 (10.40); actuarial loss 16.65 (6.00) to OCI; benefits paid 4.35 (9.91). Discount rate 7.70% (6.93%); salary escalation 7.00%; mortality 100% IALM; attrition 24% / 19% / 14% by age band (FY25 29% / 27% / 19%). No plan assets ("manage from own liquidity"). Sensitivity +/-0.5% discount rate (3.90)/+4.06; salary +4.07/(3.95). Benefit ceiling 2,000,000. Current 55.74, non-current 155.08. Lower attrition assumptions raised DBO, so the actuary moved in the conservative direction.

**F35. Other provisions.** 🟢 Warranty, decommissioning, onerous contracts, litigation: NONE disclosed. Distributor model, no warranty provision.

### 10. DEFERRED AND CURRENT TAX

**F36. Tax rate reconciliation and HK income.** 🔴 SA effective rate: 1,146.91 / 4,581.66 = 25.03% against statutory 25.17% (SA Note 30, AR p.85). CON effective rate: 1,146.91 / 8,176.20 = 14.03% (FY25 13.70%) (derived), with the reconciling item 904.84 labelled "differences in tax rates of subsidiaries" (CON Note 30, AR p.108) and AOC-1 showing nil provision (AR p.63). This is the structural source of the CON versus SA tax pattern in LB1. The CON note shows tax "Income Tax Expense 2,057.95" and "Income tax expense recognised ... 1,153.11" under the same heading; current tax in CON P&L is 1,153.11, the SA figure.

**F37. Deferred tax and MAT.** 🟢 DTA net 56.26 (45.88), almost all on gratuity provision 53.06 and OCI 6.25 (SA Note 6, AR p.80). Deferred tax credit 6.20 (12.27). MAT credit: NOT FOUND IN DOCUMENT (none). Unrecognised DTA: NOT FOUND IN DOCUMENT. Current tax liability 233.85 (95.01) (SA Note 22). Tax paid 1,014.27 vs charge 1,146.91 (cash flow).

### 11. REVENUE DETAILS (SA Note 23, AR p.84; CON Note 23, AR p.107)

**F38. Disaggregation.** 🟡
- By segment (sale of products): SA Brand 23,224.22 (13,475.02), +72.3%; MES 231,891.78 (150,379.78), +54.2%. CON Brand 38,085.50 (27,067.93), +40.7%; MES 231,891.75 (150,379.78). Brand share of CON product sales 14.11% (15.25%) (derived).
- By geography: SA India 179,713.32 (67,840.68); outside India 75,402.68 (96,014.12), -21.5%. India share of product sales 70.4% (41.4%) (derived). CON outside India 90,263.93 (109,607.00). CON India is identical to SA India, so all of the HK subsidiaries' sales are outside India.
- CON revenue less SA revenue = 14,861.25, and CON brand revenue less SA brand revenue = 14,861.28 (derived): the entire subsidiary net contribution to revenue is brand sales. SCL gross turnover 29,773.63 less intra-group sales means about half is eliminated.
- Customer-level revenue, top customers: NOT FOUND IN DOCUMENT.

**F39. Contract balances.** 🟡 Advances from customers SA 1,772.56 (238.21), +644%; CON 1,856.31 (538.76) (SA Note 20, AR p.83; CON Note 20, AR p.107). Within the CON working-capital line, the change in customer advances is 1,317.55, 18.0% of the 7,317.05 payable-side inflow (derived). Unsatisfied performance obligations, contract assets: NOT FOUND IN DOCUMENT. Advances to suppliers SA 8,595.74 (5,692.30), +51.0%; CON 13,463.70 (9,179.91), +46.7% (SA Note 12, CON Note 12). Supplier advances were 15.6% of SA revenue-related current assets; ageing of these advances: NOT FOUND IN DOCUMENT.

### 12. OTHER CRITICAL NOTES

**F40. Segment reporting and the brand margin.** 🟡 CON Note 37 (AR p.111-112), SA Note 39 (AR p.89-90).
| Rs. Lakhs | FY26 | FY25 |
|---|---|---|
| CON Brand revenue | 38,085.50 | 27,067.93 |
| CON Brand segment result | 12,629.19 | 9,356.16 |
| CON MES revenue | 231,891.75 | 150,379.78 |
| CON MES segment result | 8,728.72 | 5,506.07 |
| Total segment result | 21,357.91 | 14,862.23 |
| Less finance cost | 2,066.43 | 1,015.59 |
| Less "unallowable" cost | 11,115.28 | 7,692.13 |
| PBT | 8,176.20 | 6,154.51 |
| SA Brand result / revenue | 2,453.37 / 23,224.22 | 1,110.21 / 13,475.02 |
Derived: CON brand segment result margin 33.2% (FY25 34.6%); MES 3.76% (3.66%); SA brand 10.6% (8.2%). Brand is 59.1% of total segment result (63.0%). Implied overseas brand segment result = 12,629.19 - 2,453.37 = 10,175.82, which is 2.7 times SCL's reported PBT of 3,742.90 (the difference is not explained). Unallocated cost is 52.0% of total segment result and is not itemised. The 40-42% brand gross margin: NOT FOUND IN DOCUMENT. Segment assets total 70,132.00 vs balance sheet 93,723.64 (unallocated 23,591.64). Segment liabilities FY25 brand shows (2,558.37), a negative liability that is unexplained. SA and CON segment tables foot (SA 11,182.07 - 2,042.92 - 4,557.49 = 4,581.66, checked). CODM basis: SA policy says "geographic segment" (SA Note 2(s), AR p.79) while the segments reported are brand/MES: policy wording inconsistent with the note.

**F41. Consolidation reserve movements bypass OCI.** 🟡 CON SOCIE (AR p.98) credits foreign currency translation 861.98 (237.74) to the FCTR reserve (CON Note 14, AR p.106: 1,229.09 to 2,091.07), but the CON statement of profit and loss shows total OCI of only (12.46) and total comprehensive income 7,016.83 (AR p.97). The translation gain is outside reported comprehensive income. Also the NCI balance moves by exactly the profit share (842.15), so no translation share is allocated to NCI. Direct credit to reserves, not through P&L or the OCI statement, equals 12.3% of CON PAT (derived).

**F42. HK subsidiaries not audited by the group auditor.** 🟡 OUTSIDE NOTES but material to F36: auditor's Other Matters (AR p.93) says the two subsidiaries' financial statements are "not audited by us" and consolidated figures reflect "the report of such auditors" and "financial statements certified by the Management". Whether the HK entities have an independent audit report is not stated. Those entities supply 51.1% of CON PAT. Statutory audit fee SA 9.00 for a 255,600.47 revenue business (0.0035% of revenue, derived).

**F43. FY26 operating cash flow (verification of LB2).** 🔴 CON cash flow (AR p.98): operating profit before working capital 10,015.55; receivables (32,734.04); other assets (4,164.06); inventories (6,608.57); payables, other financial and current liabilities +7,317.05; cash used in operations (26,174.07); tax paid (1,014.27); net operating outflow (27,188.34). Investing (789.68); financing +23,423.64 (short-term borrowing +25,471.82; finance cost paid (1,746.91); dividend (75.08)). Cash closes at 535.96 (4,387.66) including a +702.68 FX translation effect. SA: operating (25,738.12), receivables (34,266.83), payables +10,719.15. Derived: receivables build is 120.4% of the operating outflow; short-term borrowing covers 93.7% of it. CON payable-side inflow of 7,317.05 = trade payables +4,976.62, other financial liabilities +1,040.94, other current liabilities +1,299.49 (of which customer advances +1,317.55), which ties to the balance sheet exactly (derived). Odd items: "OCI amount (16.65)" is adjusted against profit before tax in operating activities although OCI never entered PBT; bank charges and BG charges (about 295) are left in operating cash flow while only 1,746.91 interest is classed as finance cost paid.

**F44. Foreign currency exposure and hedging.** 🟡 SA Note 37 (AR p.89) shows only flows: export earnings 75,402.68 (96,014.12); imports 45,583.75 (27,629.82); buyer's credit expenses 4,493.48 (296.26); interest on buyers credit 53.98 (172.06). Year-end unhedged exposure, hedge instruments, sensitivity: NOT FOUND IN DOCUMENT. Note 32 financial risk covers only credit and liquidity risk (AR p.85-86). The directors' corporate-governance section points to the notes for "details of foreign currency exposure" (OUTSIDE NOTES, AR p.52 region; lines 4957-4960), but the notes contain no such table. Net exchange gain in other income 652.71 (1,180.45) = 14.2% of SA PBT (derived).

**F45. EPS.** 🟡 Basic = diluted: SA 22.87 (17.82), CON 41.04 (32.18); weighted shares 15,016,675 (14,345,793) (SA Note 31, AR p.85; CON Note 31, AR p.108). SA recomputes (3,434.75 / 15,016,675 = 22.87). CON does not: 6,187.14 / 15,016,675 = 41.20 vs reported 41.04; FY25 4,620.77 / 14,345,793 = 32.21 vs reported 32.18 (derived). Differences are small but unexplained. No dilutive instruments outstanding (no warrants at Mar-2026; AR p.82). The new Creative ESOP Scheme 2026 approved by the board 04-Aug-2026 awaits member approval (OUTSIDE NOTES, AR p.30-31) and is a future dilution source.

**F46. Share capital, dividend.** 🟢 Unchanged at 15,016,675 shares (1,501.67) in FY26 (SA Note 13, AR p.82). FY25: 9,03,000 shares from warrant conversion, including 5,00,000 by Ketan Patel. Promoters 85,02,220 shares = 56.62% (56.60%); Ketan 56.20%; Nidhi Patel 3,500 shares new. Dividend Re 0.50 per share paid (75.08) and Re 0.50 recommended (SA Note 38, AR p.89).

**F47. CSR.** 🟢 Required 61.69 (54.27), spent 62.00 (55.00), no shortfall; no related-party trust (SA Note 40, AR p.90).

**F48. Events after the balance sheet date.** 🟡 SA Note 44(k) (AR p.91): no significant subsequent events. Nothing on BSNL BharatNet or the Zicom/Infinova acquisitions appears in the notes (the AR was approved 14-May-2026; the Zicom filing is dated 04-Nov-2026 per memory). Going concern: SA Note 2(a) (AR p.75) "continue to operate as a going concern"; CON Note 2(a) similar; no uncertainty language anywhere. Audit report emphasis of matter or qualification: none found by search (unmodified opinion, AR p.91).

**F49. Intra-group profit elimination.** 🟡 CON Note 26 (AR p.107) adjusts opening stock for unrealised profit 164.69 (125.32); it reduces profit by that amount in each year. This is 4.4% of SCL's PBT (derived). Basis and cumulative unrealised profit in inventory: NOT FOUND IN DOCUMENT. With SA purchases from SCL of 15,539.15 flowing into SA inventory of 13,188.06, the elimination is small.

**F50. CON note presentation errors.** 🟡 (a) CON Note 11 (AR p.105) labels 529.98 as "Accrued Interest" for FY25, whereas SA Note 11 splits it 11.15 interest and 518.83 incentive and commission receivable; the incentive receivable of 518.83 fell to nil in FY26 with no disclosure of collection. (b) CON Note 25 is titled "Cost of Materials Consumed" for traded goods. (c) CON Note 23.3 bracket missing in "(129.50". (d) Note 15 and Note 14 in CON are interleaved on p.105-106. Presentation quality is mediocre but numbers foot.

**F51. Other expense items that changed sharply.** 🟡 SA Note 29 (AR p.84-85): commission expense 1,110.71 (344.90), +222% with no payee disclosed (not in the RPT table); sales promotion 1,098.35 (564.08), +94.7%; service expenses 600.14 (499.78); stamp duty 45.54 (7.81); consultancy fees 259.26 (450.72); director remuneration 200.61 (228.79). CON-only heads (subsidiary costs): royalty expense 595.73 (587.55), service charges reimbursement 2,537.02 (3,025.85), reimbursement of expenses 602.65 (495.61) (CON Note 29, AR p.108). Payee of royalty (Honeywell licensor) and reimbursements: NOT FOUND IN DOCUMENT.

**F52. Ratios (SA Note 43, AR p.90).** 🟡 Current ratio 1.45 vs 2.12; debt-equity 1.08 vs 0.27; DSCR 3.67 vs 5.59; inventory turnover 22.60 vs 21.02; receivable turnover 6.71 vs 10.05; payables turnover 15.66 vs 20.18; net capital turnover 10.00 vs 7.34; ROE 11.47% vs 9.61%; net profit ratio 1.35% vs 1.56%; ROCE 22.01% vs 16.31%. Management explains variances over 25%. Net margin down while ROCE up.

**F53. Cash and bank.** 🟡 SA cash and cash equivalents 475.97 (3,376.29), -85.9%; margin money 1,670.99 (1,126.78), +48.3%. Balances in other bank accounts are not restricted beyond margin money. Cash at CON 535.96.

**F54. Audit trail, other statutory disclosures.** 🟢 SA Note 44 (AR p.90-91): no benami property, struck-off company transactions, crypto, wilful default, unregistered charges; layers compliance; audit trail feature operated throughout.

---------------------------------------------------------------------
## C. ITEMS EXPECTED BUT NOT FOUND IN DOCUMENT
- Customer concentration, top-customer revenue.
- Factoring, bill discounting, TReDS, receivable derecognition.
- Borrowing covenants, sanctioned limits, repayment schedule, fixed/floating split, breakup by instrument.
- Corporate guarantees for subsidiaries; capital commitments; LC outstanding.
- ROU assets and lease liabilities; ECL matrix; goodwill (none exists); impairment test assumptions.
- Year-end FX exposure, hedging; market risk note.
- MSME interest accrual, payables above 45 days.
- Inventory categories, write-downs.
- Tax treatment of HK profit, DTL on undistributed earnings, identity of 22.5% SCL minority.
- 40-42% brand gross margin; any BSNL BharatNet disclosure.
- Prior-year related party list; transfer-pricing basis.

---------------------------------------------------------------------
## PASS 1 SUMMARY: TOP 10 FINDINGS BY INVESTOR IMPORTANCE

| Rank | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | FY26 operating outflow (27,188.34 CON) is driven by receivables, which rose 137.7% (CON) on revenue +51.7%; debtor days 76.3 vs 48.7; funded by 25,471.82 of extra short-term bank debt (gearing 0.83 net, 1.01 SA). No factoring/TReDS disclosure | SA/CON cash flow, AR p.74, p.98; SA Note 8 p.81; Note 17 p.83; Note 33 p.86 | 🔴 |
| 2 | Half of CON PAT (3,594.54 of 7,029.29) comes from two HK subsidiaries at nil tax; CON tax equals SA tax to the rupee; reason for nil tax, DTL on undistributed profit, and remittance path not disclosed | CON Note 30 p.108; AOC-1 p.63; CON P&L p.97 | 🔴 |
| 3 | HK subsidiaries' statements not audited by the group auditor ("certified by the Management") while they supply 51.1% of CON PAT | Auditor Other Matters p.93 (outside notes) | 🟡 |
| 4 | Related party exposure to SCL: purchases 15,539.15 (+55%), sales 2,208.54 (from 20.64), balance swung to (3,093.04) payable; FY27 approval sought up to Rs. 750 Cr; Click Retail balance 4,773.50 exceeds a year of sales; RPT balances do not tie to Note 8 | SA Note 36 p.88-89; Note 8 p.81; Notice p.30 | 🟡 |
| 5 | Brand segment is reported with its own result (CON 12,629.19 on 38,085.50 = 33.2%), but no gross margin disclosed; brand share fell to 14.11% from 15.25%, and brand growth +40.7% lags MES +54.2% | CON Note 37 p.111-112; Note 23 p.107 | 🟡 |
| 6 | Over-6-month receivables rose to 1,955.62 (3.54% of gross) from 517.46; disputed 236.66 against allowance 76.77 (32.4% cover); no ECL matrix | SA Note 8 p.81; Note 32 p.86 | 🟡 |
| 7 | Contingent liabilities (ex-guarantees) up 84% to 600.01, 85.8% GST, none provided; customs duty 694.72 paid under protest still carried as an asset after a 2023 CESTAT win | SA Note 35 p.87-88; Note 12 p.82 | 🟡 |
| 8 | Promoter-family pay and support: 236.74 pay; personal guarantees on bank lines; related-party premises mortgaged to SBI; 12% promoter loan | SA Note 36 p.88; Note 15/17 p.83 | 🟡 |
| 9 | Foreign currency translation gain of 861.98 credited to equity outside the reported OCI/total comprehensive income | CON SOCIE p.98; CON P&L p.97; Note 14 p.106 | 🟡 |
| 10 | Branch leases treated as short-term (no ROU/lease liability); no FX exposure or hedging disclosure despite 75,402.68 exports and 45,583.75 imports | SA Note 2(q) p.78-79; Note 37 p.89 | 🟡 |

No going-concern language beyond the standard basis-of-preparation statement (SA Note 2(a), AR p.75; CON Note 2(a), AR p.99).
