# STAGE 3: ANNUAL REPORT DEEP DIVE (BACKWARD READ): ONWARD TECHNOLOGIES LTD (ONWARDTEC)

Run date 2026-11-12. Model claude-sonnet-5-5. Pipeline mode: every kill switch is informational and the run continues.

Sources. AR26 = runs/onwardtec-2026-11-12/inputs/annual-report/Annual_Report_2026.pdf (FY2025-26). AR25 = Annual_Report_2025.pdf (FY2024-25, prior-year read). Page numbers are the "[page N]" markers of the .txt beside each PDF (PDF page, not the printed page). SHP = inputs/shareholding/SHP_Q2FY27_Sep2026.pdf. Screener = inputs/screening/screener-Data_Sheet.csv (Rs Cr). B02 = outputs/reports/02-notes-pass3.md and outputs/blocks/B02-notes.yaml.

Units. AR financial statements and notes are INR lakhs ("All amounts in ` lakhs", AR26 p.65). AR narrative, KPI page and Screener are INR Crore. Every figure keeps its source unit; "(derived)" marks my arithmetic from anchored inputs. No figure is converted silently. Where a Crore figure sits beside a lakh figure the unit is written out.

Reading order. Auditor's report and CARO (p.60-64, p.96-101), notes, cash flow, balance sheet, P&L (p.65-95), MD&A (p.44-48), governance (p.49-60), then Directors' report and front matter (p.1-26), with AR25 side by side.

Company memory (companies/ONWARDTEC.md, step1 brief) was weighed, never cited as evidence.

---------------------------------------------------------------------
## 0. B00 CARRY AND LOAD-BEARING FACTS (checked before my own work)

B00 input_gaps carried that fall in this stage's scope: shareholding/ holds only the Sep 2026 pattern (no pledge or FII/DII trend beyond one quarter; the AR gives promoter and 5% holders at Mar 2024, Mar 2025, Mar 2026); Screener P&L, Quarters, Balance Sheet and Cash Flow exports are empty, only the Data_Sheet was used; ICRA rating withdrawn 2023-11-13, no live rating; the announcements folder is not the full Reg 30 record. Other B00 gaps (Q1 FY27 scan, prospectus, research) do not touch this stage.

| # | Load-bearing fact (B00) | In scope of the AR? | What the AR shows |
|---|---|---|---|
| 1 | Q2 FY27 EBITDA margin 15.6% vs FY27 guide 13.8-14.3%; Rs 2.9 Cr R&D credit | Partly. Q2 FY27 is outside the AR. The AR shows how the credit is booked. | UK R&D expenditure credit of 135.94 lakhs (FY25 171.33) is booked as a reduction of employee cost, inside EBITDA, on an accrual basis; the claim "is in the process of" being filed (AR26 Note 21 p.86). Receivable 272.63 lakhs vs 366.58 (Note 11 p.79). Derived: FY26 EBITDA margin 13.21% reported, 12.96% without the credit; FY25 9.10% reported, 8.75% without. Margin gain ex-credit +421 bps vs +411 bps reported (derived). The credit is not what drove FY26. Rs 2.9 Cr in Q2 FY27 stays OPEN for the results and concall stages. |
| 2 | Guidance history vs delivery | Partly (FY26 only). | AR25 p.16: "Over the next three years, we are targeting double-digit growth in both revenue and EBITDA". FY26 delivered revenue +10.7% and EBITDA +60.7% (derived from p.65). AR26 p.11: guidance "reiterated" as "sustained double-digit growth". The 15-18% raise and H1 FY27 delivery are NOT FOUND IN DOCUMENT (outside the AR). |
| 3 | Concentration, clients >USD 1 mn, DSO | Yes | One customer 9,965.52 lakhs = 18.3% of revenue (Note 34 p.93; derived). Top 5 / 10 / 25 = 48% / 64% / 87% (AR26 p.46 KPI table; FY25 50 / 66 / 84). Clients above USD 1 mn: 16 vs 13. Active clients 72 vs 80. Management DSO (billed + unbilled) 75 days vs 76 (p.46); my year-end calculation 80.5 days (11,999.70 / 54,385.24 x 365); average-balance basis 77.0 days (reported debtors turnover 4.74 reproduces on average billed + unbilled, p.47). The Sep 2026 DSO of about 80 days is outside the AR. |
| 4 | Promoter holding 61.71% (Mar 2021) to 38.12% (Mar 2024) | Partly. | The 38.12% ties exactly in AR25 Note 13 p.147: JHM Enterprises 33.74% + Harish 0.96% + Jigar 1.67% + Heral 1.08% + Prachi 0.67% = 38.12% (derived). Infinity Direct Holdings (Mauritius) held 39,00,000 shares = 17.32% at Mar 2024. The path from 61.71% is NOT FOUND IN DOCUMENT (the FY21 to FY23 annual reports are not in the corpus). Since Mar 2024 the promoters rose: 38.65% (Mar 2025), 39.61% (Mar 2026), 40.20% (Sep 2026, SHP row A). Detail in Phase 5D. |

---------------------------------------------------------------------
# PHASE 1: AUDITOR'S REPORT AND CARO

## 1A Core opinion

| Item | Consolidated | Standalone |
|---|---|---|
| Auditor | B S R & Co. LLP, FRN 101248W/W-100022, partner Swapnil Dakshindas, signed 05 May 2026 (AR26 p.63) | Same firm, same date (p.98) |
| Opinion | Unmodified. "give a true and fair view in conformity with the accounting principles generally accepted in India" (AR26 p.60) | Unmodified (p.96) |
| Going concern | No material uncertainty paragraph. The words appear only in the standard responsibilities text (p.61). Standalone CARO clause (xix): "nothing has come to our attention, which causes us to believe that any material uncertainty exists" (p.100). | Same |
| Carve-out inside the report | Para 2A(b): proper books of account kept "except for the matters stated in the paragraph 2(B)(f) below on reporting under Rule 11(g)"; para 2A(f): "the modification relating to the maintenance of accounts and other matters connected therewith are as stated in the paragraph 2A(b) above ... and paragraph 2B(f)" (p.62). | Same wording (p.98) |
| Internal financial controls (Annexure B) | "adequate internal financial controls ... operating effectively as at 31 March 2026" (p.64) | p.101 |

Plain reading: the opinion on the numbers is clean. The books-of-account paragraph is not clean (see 1C).

## 1B Key audit matters

| # | Subject | Why key | How addressed | Risk |
|---|---|---|---|---|
| 1 | Revenue recognition, Note 2(e) and 19 (AR26 p.60-61; standalone p.96-97) | "presumed fraud risk around existence of revenue"; judgement on fulfilment of performance obligations; T&M and fixed-price contracts | Read MSAs; tested time-sheets with customer acceptances, invoicing, trends of collection and disputes; tested IFC design and operation | 🟡 |

Only one KAM, same in AR25. No KAM on unbilled revenue (3,429.35 lakhs, 28.6% of total receivables, derived from Note 6 p.78), on ECL, on impairment, on fair value, or on the gratuity deficit. Revenue is T&M at 88% (MD&A p.46), so the time-sheet test is the right test. Cross-reference: the revenue billing system is the system the auditor cannot fully vouch for (1C).

## 1C Emphasis of Matter and Other Matters

| Item | Detail | Risk |
|---|---|---|
| Emphasis of Matter | None in AR26 or AR25. | 🟢 |
| Other Matter (a) | 4 subsidiaries not audited by BSR: total assets 2,917 lakhs, total revenues 4,939 lakhs, net cash outflows 64 lakhs (AR26 p.62). Derived: 9.1% of consolidated revenue (54,385.24) and 7.9% of consolidated assets (37,056.82). The four are not named. | 🟡 |
| Rule 11(g) audit trail (second year) | "the feature of audit trail (edit log) was not enabled in full at the application layer ... in respect of general ledger system"; database of general ledger, revenue billing and consolidation systems "is operated by a third party software service provider. In the absence of reporting on compliance with the audit trail requirements at database layer in the independent auditor's report of the service organisation, we are unable to comment"; "Due to system limitations, we are unable to comment on instances of audit trail feature being tampered with during the year in respect of general ledger system and revenue billing system." (AR26 p.63; standalone p.98.) Same text in AR25 (consolidated p.108-109, standalone p.180). | 🟡 |
| Board's response | Directors' Report: the report "contains an unmodified opinion without any qualification, reservation or adverse remark ... self-explanatory and hence do not call for any further explanations" (AR26 p.18). No remediation plan or date: NOT FOUND IN DOCUMENT. | 🟡 |

Contradiction at the point of contradiction: the Board says "no adverse remark" while the auditor's own legal-requirements section says the books-of-account paragraph is subject to a "modification". The opinion is unmodified; the Board's wording is technically defensible and still unhelpful to a reader.

## 1D CARO 2020 clause by clause (standalone Annexure A, AR26 p.99-100; consolidated adds only para (xxi), p.63)

| Clause | Finding | Amount / note |
|---|---|---|
| (i) PPE, intangibles, titles, revaluation, benami | Clean; all PPE verified in year; title deeds in company name (p.99) | none |
| (ii) Inventory / working capital limits | Service company, no inventory; no WC limit above Rs 5 crore (p.99). Cross-check: Note 8 shows ICICI and HSBC facilities (400.00 lakhs undrawn at Mar 2025) lapsed in FY26 (p.79, p.90). | none |
| (iii) Loans to related parties | No investments, guarantees or loans in the year (p.99). Repayment reality: not applicable. | none |
| (iv), (v), (vi) | Not applicable (p.99) | none |
| (vii)(a) Undisputed dues | "slight delays in a few cases of provident fund and profession tax"; nothing in arrears over six months (p.99) | amount NOT FOUND |
| (vii)(b) Disputed dues | Income tax 102.61 (AY 2022-23, National Faceless Appeals Centre), 7.53 (AY 2014-15, CIT(A) New Delhi), 21.17 (AY 2024-25, DCIT Mumbai); GST Tamil Nadu 64.89, 50.24, 30.86 (FY 2018-19 and 2019-20). Total 277.30 lakhs (derived: 131.31 income tax + 145.99 GST). Paid under protest 6.35 (2.49 + 2.23 + 1.63). | 1.30% of standalone net worth 21,390.70 and 8.6% of standalone PAT 3,215.88 (derived; Note 36 p.94). Prior-year list differed: AR25 p.182 showed 102.61, 75.45 (AY 2023-24), 64.89, 7.20, 50.24, 37.30 = 337.69 (derived). |
| (viii) Unrecorded income | None | none |
| (ix) Borrowings, default | No loans or borrowings; not a wilful defaulter; no short-term funds used long term (p.99-100) | none |
| (x) Public issue / preferential | None (p.100) | none |
| (xi) Fraud | (a) no fraud noticed; (b) no ADT-4 filed; (c) "no whistle blower complaints received" (p.100) | none |
| (xii)-(xvi) | Not Nidhi; RPT per ss.177 and 188 (xiii); internal audit adequate (xiv); no s.192 transactions (xv); not NBFC or CIC (xvi) | none |
| (xvii) Cash losses | None in current and preceding year (p.100) | none |
| (xviii) Auditor resignation | None | none |
| (xix) Ability to meet liabilities | No material uncertainty | none |
| (xx) Unspent CSR | None; CSR 62.47 spent in full (Note 24(b) p.86) | none |
| (xxi) Consolidated | No qualifications in subsidiaries' CARO reports (p.63) | none |

Cross-reference with Phase 2: the 277.30 lakhs of disputed dues is not in the contingent liability note. Note 26 (p.87) says tax demand notices are "remote" and not disclosed. In AR25 the AY 2022-23 matter was removed from contingent liabilities because the assessing officer set it off against refunds (AR25 Note 26 p.158). The same AY 2022-23 matter (102.61) still appears as disputed and unpaid in AR26 CARO. Two readings: (a) set-off was real and CARO lists a stale item; (b) the dispute is live and the Note 26 "remote" call is an assessment, not a fact. One observation separates them: the FY27 CARO list (item gone, or still there).

## 1E Auditor continuity and fees

| Item | Evidence |
|---|---|
| Firm and term | B S R & Co. LLP appointed "for the period of 5 years starting from conclusion of 31st AGM till the conclusion of 36th AGM ... to be held in calendar year 2027" (AR26 p.18). FY26 is the fourth year of that term (derived: the 32nd AGM was 17 July 2023, p.56). Whether BSR audited before the 31st AGM: NOT FOUND IN DOCUMENT. |
| Partner | Swapnil Dakshindas, Membership 113896. Partner tenure NOT FOUND. |
| Fees (consolidated Note 24(a), p.86) | Statutory audit 32.00 (FY25 29.00); limited reviews 3.00; certificates 2.00; out-of-pocket 3.54; total 40.54 (FY25 36.81). |
| Ratio | Non-audit (certificates) 2.00 = 6.3% of audit fee (derived); with limited reviews 5.00 = 15.6%. Non-audit does not exceed audit. Total fee = 0.075% of revenue (derived). No tax or advisory fee appears. |
| Disclosure oddity | The governance report gives total fees "on a consolidated basis" as 40.54 (p.55), identical to the parent's own note. Fees paid to the other auditors of the four unaudited subsidiaries are NOT FOUND IN DOCUMENT. |
| Rotation | Final year of the first 5-year term is FY27; rotation or re-appointment falls at the 2027 AGM. |

## 1F Standalone vs consolidated

- Both opinions unmodified; same single KAM; same audit-trail wording (consolidated also covers the Indian subsidiary OT Park). Source: AR26 p.60-63 vs p.96-98.
- Reliance on other auditors: 4 subsidiaries, 9.1% of revenue (1C). Which auditors: NOT FOUND IN DOCUMENT.
- AOC-1 (AR26 p.20): US subsidiary turnover 17,679.29 lakhs before elimination (equal to 32.5% of consolidated revenue, derived) with profit after tax 574.40; Canada 369.45; GmbH 95.55; BV 15.87; OT Park 175.41. All five profitable in FY26. Whether the US subsidiary is among the four unaudited by BSR is NOT FOUND IN DOCUMENT; the sum GmbH + Canada + BV + OT Park turnover is 4,971.00 (derived) vs the stated 4,939, so the identity is a probable inference, not a fact, and total assets for those four (3,441.83 derived) do not match 2,917.
- Material subsidiary: Onward Technologies Inc., USA (AR26 p.55). The Reg 24 independent director on its board: NOT FOUND IN DOCUMENT.

## Phase 1 summary

| Check | Result |
|---|---|
| Opinion | Unmodified, both reports |
| KAM | One (revenue), 🟡 |
| EoM | None |
| Control carve-out | Audit trail, second year, covers GL and revenue billing, no remediation date |
| CARO | No adverse remark. Disputed dues 277.30 not in contingent liabilities |
| Fees | Clean ratio |

**Phase 1 verdict: 🟡 Watch.** The numbers are signed clean. The system that bills revenue is not fully vouched for, for the second year, and the Board gives no date to fix it.

**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because the opinion is unmodified, there is no fraud report, and the carve-out is a control-evidence limit, not a finding of tampering. It would have reason to ask for the service organisation (SOC) report timeline.

---------------------------------------------------------------------
# PHASE 2: NOTES TO FINANCIAL STATEMENTS

Method. I verified the 15 triple-pass findings against AR26, then extended where B02 is thin: policy aggressiveness, RPT percentages, contingent liability ratios and the maturity wall. Pass 2 corrections C1-C9 govern; I used the Pass 3 text.

## 2.0 Verification of the Top 15 (B02 pass 3)

| Rank | B02 claim | AR26 check | Result |
|---|---|---|---|
| 1 | Customer 18.3% = 9,965.52 of 54,385.24; FY25 17.2%, FY24 12.7% | Note 34 p.93: 9,965.52 (FY25 8,447.58). AR25 Note 34 p.170: FY24 6,020.21. 9,965.52/54,385.24 = 18.32%; 8,447.58/49,131.61 = 17.19%; 6,020.21/47,239 = 12.74% (FY24 revenue 472.39 Cr, Screener). | ✓ verified |
| 2 | Sub-contracting 3,407.42, +36.6% vs revenue +10.7%, payroll +4.1% | Note 24 p.86: 3,407.42 vs 2,494.19 = +36.6%; revenue 54,385.24 vs 49,131.61 = +10.7%; employee cost 39,582.25 vs 38,011.83 = +4.1% (p.65). | ✓ verified |
| 3 | Parent billed days 52.6 to 43.4; subsidiary 70.1 to 81.3; standalone fall 93.5% intra-group; RPT receivables exceed Note 8 by 345.60 | Standalone Note 8 p.115: third-party billed 4,032.38 (FY25 4,324.54); related 261.80 (FY25 1,603.33); total fell 8,439.65 to 7,005.54 (1,434.11), related fell 1,341.53 = 93.5%. Parent third-party revenue = 41,677.36 less subsidiary revenue 6,368.59 + 1,237.13 + 149.07 (standalone Note 26 p.124) = 33,922.57; 4,032.38/33,922.57 x 365 = 43.4. FY25 4,324.54/29,983.58 x 365 = 52.6. Subsidiary: (8,588.79 - 4,032.38)/(54,385.24 - 33,922.57) x 365 = 81.3; FY25 70.1. RPT table p.125: 443.89 + 136.39 + 16.52 + 10.60 = 607.40. | ✓ verified, one refinement below (D1) |
| 4 | Unbilled 3,429.35 (+13.2%), 40.0% of net billed, 23.0 days | Note 6 p.78: 3,429.35 vs 3,029.65 = +13.2%; 3,429.35/8,570.35 = 40.0%; 3,429.35/54,385.24 x 365 = 23.0. Ageing: none; ECL on unbilled "insignificant" (Note 30 p.90). | ✓ verified |
| 5 | Gratuity deficit 1,062.86; funded 11.5%; contribution 10.00 vs benefits paid 130.82; labour code 315.50; salary growth 5.00%; FY27 contribution 1,339.10 | Note 17 p.83-84: 1,062.86 (986.23 + 76.63); funded 137.84/1,200.70 = 11.5%; 10.00; 130.82; 315.50; 5.00%; 1,339.10. | ✓ verified. New point: expected FY27 contribution (1,339.10) exceeds the whole deficit by 276.24 (derived); basis NOT FOUND. Plan assets fell 244.15 to 137.84 because benefits paid (130.82) exceed contributions (10.00). |
| 6 | CFO includes 994.95 of accrued pay net of labour code (15.3%); KMP unpaid pay 506.29 | Cash flow p.66: +692.41 other financial liabilities, +618.04 employee benefit obligations; 692.41 + (618.04 - 315.50) = 994.95; 994.95/6,507.73 = 15.3%. KMP payables Note 27 p.88: 224.83 + 275.78 + 4.72 + 0.96 = 506.29. | ✓ verified |
| 7 | Forward sell 2,673.14 vs parent net exposure 891.69; GBP 766.47; not designated; MTM liability 129.78; sensitivity omits derivatives | Note 38 p.95: USD 2,097.99 + EUR 575.15 = 2,673.14. Standalone net exposure p.128: USD 59.91 + EUR 65.31 + GBP 766.47 = 891.69. Note 29 p.89: "not designated as hedges", liability 129.78. Sensitivity p.92: Euro 17.99 = 5% of 359.85, GBP 38.49 = 5% of 769.83, CAD 12.68 = 5% of 253.59, so the table is 5% of net balance gross of forwards; 5% of forward notional = 133.7 (derived). | ✓ verified |
| 8 | ETR 22.3% vs 25.4%; 23.7% ex 53.25 prior-period and 28.04 loss line; 71.70 swing in non-deductible line | Note 12(b) p.80: 1,272.19/5,704.58 = 22.30%; 922.21/3,629.98 = 25.41%; (1,272.19 + 53.25 + 28.04)/5,704.58 = 23.73%; non-deductible line (48.54) vs 23.16 = 71.70 swing. | ✓ verified |
| 9 | ESOP 2024 grant cost 454.68; FY26 expense 89.79; Trust bought at about Rs 325 vs exercise 253.48; gap 214.6; Trust loan 1,007.77; dilution 1.9% | Note 35 p.94: 3,00,000 x 151.56 = 454.68; expense 89.79; cash flow p.66: 1,006.47 / 3,09,679 = Rs 325.0; 325.0 - 253.48 = 71.5 x 3.0 lakh = 214.6; Annexure III-A p.23: loan "Rs 10,07,77,000"; dilution (3,00,000 + 1,24,800)/2,24,44,191 = 1.89%. | ✓ verified |
| 10 | Audit trail carve-out, second year | AR26 p.63, p.98; AR25 p.108-109, p.180. | ✓ verified |
| 11 | Cook County suit; 394.68 disclosed; 1,130.64 frozen, vacated; tax demands remote | Note 26 p.87: USD 12.6 lakhs (1,130.64) restricted then lifted; contingent 394.68 (USD 4.20 lakhs); tax demands "remote". Implied rates: 1,130.64/12.6 = 89.7 and 394.68/4.20 = 94.0 per USD, vs AOC-1 closing 94.8325 and average 88.3739 (p.20). | ✓ verified |
| 12 | Standalone ROCE 23.48% includes other income 906.69; 19.17% without | MD&A p.47 and standalone Note 33 p.131: 23.48%; other income 906.69 (p.102). The 19.17% is B02 arithmetic, not printed. | ✓ verified (23.48%); 19.17% not reproduced here |
| 13 | Independent director's firm billed 9.76 (+190.5%); Infinity Direct 195.00 two readings; Canada 358.63; Trust trustee was subsidiary director | Note 27 p.88: Desai & Diwanji 9.76 vs 3.36 = +190.5%. Dividend rows 99.00 (FY25 195.00) and 96.00. Standalone Note 26 p.125: Canada "Advance from customers" 358.63 (FY25 286.84) is a LIABILITY of the parent to its Canadian subsidiary, not an asset. Secretarial audit p.25: trustee was a subsidiary director, resigned. | ✓ verified. The Infinity "two readings" resolve: see D3. |
| 14 | PP&E additions 2,156.00 (FY25 228.76); cash 1,804.97; vehicles 360.49; facilities lapsed | Note 3 p.77; cash flow p.66; Note 8 p.79. | ✓ verified |
| 15 | Zero borrowings; no inventory, goodwill; subsidiaries profitable; past due over 6 months 12.41 | Note 31 p.92; Note 6 p.78: 0.33 + 6.82 + 5.26 = 12.41; AOC-1 p.20. | ✓ verified. Page ref: B02 cites Note 31 at p.93; it is p.92 (page-only slip). |

**Verified: 15 of 15 on number and note reference.** Discrepancies are refinements, none changes a rating:

- D1 (rank 3): B02 gap 345.60 = 607.40 - 261.80. The 607.40 includes JNTL 10.60, a third-party customer that sits inside "billed" (Note 26 p.125). Subsidiary-only gap = 596.80 - 261.80 = 335.00 (derived). FY25 gap on the same basis = 1,664.37 - 1,603.33 = 61.04 (derived from p.125). The mismatch widened from 61.04 to 335.00.
- D2 (rank 15): Note 31 page p.92, not p.93.
- D3 (rank 13): the Infinity dividend reading is closed by arithmetic. AR25 Note 13 p.147: Infinity Direct 39,00,000 shares at Mar 2024; Mar 2025 19,80,000 + Infinity Portfolio 19,20,000 = 39,00,000. FY25 dividend 195.00 = 39 lakh x Rs 5; FY26 99.00 + 96.00 = 195.00. Reading 1 (inter-se transfer on 27 Sep 2024, same beneficial block) is confirmed; reading 2 (two separate holders) is not needed. Combined block 17.37% at Mar 2026 (8.82% + 8.55%, p.81).

## 2A Accounting policy aggressiveness

| Area | Policy / evidence | Aggressiveness |
|---|---|---|
| Revenue | T&M 88%, fixed time/fixed price 12% (p.46). Payment terms up to 60 days (Note 19 p.85). Discounts 246.00 (FY25 317.70). RPO nil for T&M (Note 19). | Conservative. Unbilled unaged and unprovided is the soft spot. |
| Depreciation | Computers 3-6 yrs, furniture 5-10, office equipment 5-7, electrical 10, vehicles 4-8, buildings 40-60 yrs "lesser than those specified by Schedule II" (p.74); the same note later says lives "are in line with ... Schedule II" (p.74). Software 2-6 yrs. | Mild contradiction on buildings. Building is 2,564.87 of 4,782.72 PP&E, charge 48.67, so the stakes are small. |
| Capitalisation | Development costs capitalised only when feasible (p.75). FY26 "Internally Generated (Software)" 264.57, of which IAUD 165.23 carried from FY25, so new spend about 99.34 (derived) = 1.7% of PBT 5,704.58. Amortisation 27.92 started. No borrowing cost capitalised (no debt). | Low. New in FY26 and small. |
| Impairment | Goodwill: none on the balance sheet. IAUD tested annually (p.75). | Not a lever here. |
| ECL | Matrix: not due 0.04%, 0-90 days 0.25%, 90-180 days 5.83%, over 450 days 99.02% (Note 30 p.90). Allowance 18.44 vs 91.23: the 91.23 cohort (77.54 in the 1-2 year bucket) was written off. Cash flow p.66: bad debts 74.89 written off, loss allowance (75.20) released, P&L net nil (derived: 74.89 - 75.20 = -0.31). | Neutral in P&L; the old problem receivable is now gone. Unbilled "insignificant". |
| Ind AS 116 | Incremental borrowing rate used; the rate is NOT FOUND IN DOCUMENT. Implied rate 289.05 / average lease liability (3,984.33 + 3,215.97)/2 = 8.0% (derived). ROU additions 1,577.63. | Normal. EBITDA before leases is flattered: lease cash outflow 1,004.98 (p.89); EBITDA less lease outflow = 6,179.61 = 11.4% of revenue (derived) vs reported 13.2%. |
| Policy changes | None quantified. The labour code treated as past service cost in "exceptional items" (315.50, p.84). | Presentation choice: moves a people cost below EBITDA once. |
| Share-based pay | Black-Scholes; volatility 48%; expected life 4 years (p.94). | Normal. |

Cross-check against B02: the accounting policy view (7/10) stands.

## 2B RPT map (consolidated Note 27 p.87-88; standalone Note 26 p.124-126)

| Counterparty | Flow FY26 (lakhs) | % of consolidated revenue 54,385.24 | Signal |
|---|---|---|---|
| JHM Enterprises (promoter holding company) | dividend 392.50 | n/a | Same terms as all shareholders |
| Infinity Direct and Portfolio | dividend 99.00 + 96.00 | n/a | Same terms |
| PHM Growth Pvt Ltd (KMP-controlled) | rent 53.58; reimbursements 9.12; lease liability 49.79; deposit 18.82 | 0.10% | Small; arm's length stated, no benchmark |
| Desai & Diwanji (independent director's firm) | professional fees 9.76 (FY25 3.36) | 0.02% | Independence test, see 5A |
| JNTL Consumer Health (India) (common director, from 8 May 2025) | revenue 160.63; receivable 10.60 | 0.30% | New customer in FY26; the common director is not named in the AR |
| CSR donation to a trust a director is interested in | 10.00 (FY25 15.00) | 0.02% | Small |
| KMP pay | Harish 383.17, Jigar 459.80, CFO 60.92, CS 5.41 + 8.36 = 917.66 | 1.69% | See 5C |
| Sitting fees | 14.00 | 0.03% | |

Non-dividend, non-pay related-party flows: 160.63 + 62.70 + 9.76 + 10.00 = 243.09 (0.45% of revenue, derived). Promoter-family outflow in rent, fees and CSR 73.34 (0.13%) ties to B02.

Standalone intra-group flows are large: sales to subsidiaries 6,368.59 + 1,237.13 + 149.07 = 7,754.79 = 18.6% of standalone revenue (derived); marketing fees paid to subsidiaries 513.66 + 290.82 + 34.58 = 839.06 (FY25 998.12); management fee income 207.42 (FY25 351.50, -41%). Transfer pricing: "arm's length" with the last accountants' report "post March 31, 2025" (Note 37 p.94, standalone Note 34 p.131). Value-extraction signal toward the promoter family: none found. Intra-group pricing is an unbenchmarked area, not a promoter leak.

## 2C Contingent liabilities

| Item | Amount | % consolidated net worth 25,350.70 | % consolidated PAT 4,432.39 | Flag |
|---|---|---|---|---|
| Cook County suit vs US sub (disclosed) | 394.68 | 1.56% | 8.9% | Under 25% |
| Cash freeze (vacated) | 1,130.64 | 4.5% | 25.5% | The frozen sum equalled 30.7% of group cash and equivalents 3,685.66 (derived) |
| Tax demand notices | "remote", no amount (Note 26 p.87) | n/a | n/a | Disclosure gap |
| Disputed dues per CARO | 277.30 | 1.1% | 6.3% | Not in Note 26 |
| Capital commitments | 331.11 (FY25 786.07) | 1.3% | | |
| Guarantees | nil | | | |

No item reaches the 25% or 100% flag on net worth. The cash freeze reached the 25% mark of PAT while it lasted. The disclosure is thin, not large.

## 2D Receivables (AR26 Note 6 p.78, Note 30 p.90)

- Billed 8,588.79 gross; not due 7,825.94 (91.1%); past due under 6 months 750.44; 6 months to 1 year 0.33; 1-2 years 6.82; 2-3 years 5.26. Over 6 months 12.41 = 0.14% (FY25: 17.44 + 5.74 + 6.32 + 77.54 = 107.04, 1.3% of 8,002.93, derived).
- Days (derived): consolidated billed 57.5, billed plus unbilled 80.5 (FY24 77.9, FY25 81.3 per B02). Unbilled 23.0 days (21.1, 22.5).
- Concentration: customer 18.3% of revenue; share of receivables NOT FOUND IN DOCUMENT. USD receivables 4,074.12 of billed 8,588.79 = 47.4% (derived, Note 30 p.91).
- Split: parent 43.4 days (from 52.6), subsidiaries 81.3 (from 70.1). Closing rates exceed average rates by 7.3% (USD 94.8325 vs 88.3739), 6.3% (EUR 108.9958 vs 102.4962), 6.6% (CAD 68.1668 vs 63.9580) (AOC-1 p.20). Translation can explain at most about 5 days of the 11.2-day subsidiary rise (derived); about 6 days look real. [INFERENCE] The parent pulled 1,341.53 of cash from its subsidiaries while the subsidiaries lengthened collections.
- Cash flow tie: change in receivables per cash flow -612.32 vs balance sheet change +1,058.35 (11,999.70 - 10,941.35); the 446.03 difference is close to the foreign translation reserve gain of 470.88 (p.67), so most non-cash drift is translation.

## 2E Inventory

None. Service company (CARO ii, p.99). Not applicable.

## 2F Borrowings and maturity wall

- Borrowings nil; no covenants; no pledge; ICDs given nil (Note 31 p.92; CARO ix p.99-100). Working capital lines (ICICI, HSBC) expired and not renewed; secured by deposits of 15.93 (Note 8 p.79). Note 30 p.90 still says the Group maintains "availability under committed credit lines" and refers to "debt covenants": text outlives the facts.
- Lease maturity table (Note 30 p.91): 284.77 + 276.36 + 546.58 + 1,916.26 + 572.91 = 3,596.88 against carrying value 3,984.33. Undiscounted cash flows cannot be below the discounted liability. Short by 387.45 (derived; the FY25 table ties exactly at 3,215.97). New finding (not in B02). 🟡 presentation error or one omitted lease.
- Wall: obligations due within 12 months 4,913.80 (employee payables 3,220.22, payables 1,170.85, capital creditors 353.68, derivative 129.78, dividend 39.27) against liquid assets 12,849.24 (derived: 3,685.66 + 7,408.88 + 1,701.39 + 53.31). Coverage 2.6x. Plus lease cash of about 1,107.71 within 12 months (derived from the three short buckets). No wall.

## 2G Deferred tax

Net DTA 480.18 (FY25 334.67); gross DTA 1,373.57, of which lease liability 910.96 and gratuity 361.18; DTL 893.39, of which ROU 825.68 (Note 12(a) p.79-80). Lease DTA and DTL nearly offset. Deferred tax credit 168.53 (3.0% of PBT). The reconciliation shows a (28.04) line for "deferred tax asset not recognized on losses incurred by subsidiaries": negative sign means a benefit this year; amount of unrecognised losses NOT FOUND IN DOCUMENT.

## 2H Exceptional items, goodwill, ESOP, leases, post balance sheet

- Exceptional: one item, 315.50, the labour code past service cost on draft central rules (Note 17D p.84). None in FY25 or FY24 (AR25 P&L has no exceptional line). Single and disclosed as "non-recurring" while the rules are not final; it can move.
- Goodwill: none. Intangibles 371.23 = 1.5% of net worth (derived).
- ESOP: expense 89.79 (FY25 124.02; FY24 542.54 per AR25 Note 13(b) p.147). Potential dilution 1.9%. The Trust holds 3,09,679 shares (1.37% of capital, Annexure III-A p.23) funded by a 1,007.77 company loan. Note 35 says the 2024 scheme was approved at an EGM on 6 February 2026 (p.93); the Directors' Report says members approved it on 23 January 2025 (p.18). Date conflict, 🟡 drafting.
- Leases: liability 3,984.33 (+23.9%); ROU assets 3,732.53; interest 289.05 (the only finance cost).
- Post balance sheet: no events note. The Board approved a buyback at Rs 328 up to Rs 18,00,00,000 on 12 May 2026 (inputs/announcements/Buyback_Board_Outcome_2026-05-12.pdf, p.1); 5,48,780 shares were bought and extinguished by 15 June 2026 (Buyback_Extinguishment_2026-06-15.pdf; 548,780 x 328 = Rs 18.00 Cr, derived). The financial statements were approved on 05 May 2026, before the buyback, so Ind AS 10 does not strictly require a note. The AR went to the exchanges on 22 June 2026 (AR26 p.1) with the buyback already complete and no mention of it (the Secretarial Audit even lists the buyback regulations as "Not applicable", p.25). Readers of the AR see 128.5 Cr of liquid assets that were about 14% (derived: 18.00/128.49) smaller a month before publication.

## Phase 2 summary

| Area | View |
|---|---|
| Triple-pass | 15 of 15 verified; 2 refinements, 1 resolved open item |
| New findings | Lease maturity table short by 387.45; CARO disputed dues 277.30 outside Note 26; RPT receivable gap widened to 335.00 from 61.04; FY27 gratuity contribution exceeds deficit |
| Policy aggressiveness | Low to moderate; unbilled is the one soft area |
| RPT | 0.45% of revenue ex pay; no leakage found |
| Contingents | Small |
| Maturity wall | None; liquid assets 2.6x short-term obligations |

Reconciliation with the triple-pass score (7/10): I agree. A 7 is fair: balances are detailed, causes are thin, and three non-ties (RPT receivables, cash tax 1,194.41 vs 1,699.47, lease table) point to presentation weakness, not manipulation.

**Phase 2 verdict: 🟡 Watch.**

Cross-reference with Phase 1: the single revenue KAM and the billing-system audit-trail gap are the same risk seen from two sides. The notes show the unbilled and subsidiary-collection drift on precisely the revenue the auditor cannot fully trace.

**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because nothing in the notes is a break. The lease table error and the CARO-versus-Note-26 gap deserve one question each.

---------------------------------------------------------------------
# PHASE 3: FINANCIAL STATEMENTS (cash flow, balance sheet, P&L)

## 3A Cash flow (AR26 p.66)

| Item (lakhs) | FY26 | FY25 | Note |
|---|---|---|---|
| PAT | 4,432.39 | 2,707.77 | p.65 |
| CFO | 6,507.73 | 3,152.30 | +106.5% (derived) |
| CFO / PAT | 146.8% | 116.4% | derived |
| EBITDA (revenue less employee and other expense) | 7,184.59 | 4,469.61 | derived; ties to MD&A p.46 |
| CFO / EBITDA | 90.6% | 70.5% | derived |
| Capex (PP&E 1,804.97 + intangibles 106.10) | 1,911.07 | 367.01 | |
| FCF (CFO - capex) | 4,596.66 | 2,785.29 | |
| Lease repayments | 1,004.98 | 1,034.88 | Ind AS 116 sends this to financing |
| FCF after leases | 3,591.68 | 1,750.41 | 81.0% of PAT (FY25 64.6%) |
| Capex / depreciation ex-ROU (573.74) | 3.33x | 0.87x | Step-up; against total D&A 1,579.69 it is 1.21x |
| M&A | nil | nil | |
| Dividends paid | 1,134.25 | 1,119.54 | 25.6% of PAT |
| ESOP Trust purchase | 1,006.47 | nil | |
| Net cash movement | +1,217.35 | -687.35 | |

CFO history, Screener Rs Cr (Data_Sheet "Cash from Operating Activity"): FY22 -3.93, FY23 5.75, FY24 62.35, FY25 31.52, FY26 65.08. PAT Rs Cr: 23.68, 11.48, 33.92, 27.08, 44.32. Five-year CFO/PAT = 160.77/140.48 = 114% (derived); FY24-FY26 = 151%. The record before FY24 is weak (FY22 negative, FY23 half of PAT), so "consistent cash conversion" would be a three-year claim, not a five-year one. CFO/PAT was never below 0.7 in FY24-FY26.

CFO quality checks:

| Check | Result |
|---|---|
| One-time inflators | None one-off. Labour code 315.50 is non-cash and is added back (net nil). |
| Working capital contribution | +1,069.23 of CFO (16.4%): payables +393.76, other financial liabilities +692.41, provisions +618.04 against receivables -612.32. CFO before working capital and after tax = 7,137.97 - 1,699.47 = 5,438.50 = 122.7% of PAT (derived). |
| Payable stretching | Employee benefit payable +28.8% (3,220.22 vs 2,499.95) against payroll +4.1%: 29.7 days of employee cost vs 24.0 (derived). KMP unpaid pay 506.29. Trade payables +28.2% (1,192.23 vs 929.71). Some stretch; reverses when paid. |
| Interest classification | Interest received 728.52 is in investing; lease interest and principal are in financing. Standard choice; it moves 728.52 of cash out of CFO. |
| Ind AS 116 effect | Lease-adjusted CFO = 6,507.73 - 1,004.98 = 5,502.75, 124.1% of PAT and 76.6% of EBITDA (derived). Headline 146.8% overstates by about 22.7 points. |
| Cash tax | 1,699.47 paid = 29.8% of PBT, above the 22.3% book rate. Note 12(b) line 1,194.41 does not tie (505.06 gap; B02). Cash tax above book tax is the conservative direction. |
| Inventory rundown | Not applicable. |

FLAG-CASH assessment: the headline CFO shows no deterioration. The deterioration sits in composition: subsidiary billed days 70.1 to 81.3, unbilled +13.2% against revenue +10.7%, 15.3% of CFO from unpaid pay accruals, and a 22.7-point Ind AS 116 uplift. I carry FLAG-CASH forward from B02 as a quality flag, not a cash-conversion failure.

## 3B Balance sheet walk (AR26 p.65, lakhs)

| Line | Mar 2026 | Mar 2025 | Change / comment |
|---|---|---|---|
| PP&E | 4,782.72 | 3,111.79 | +53.7%; computers 791.74, leasehold improvements 733.52 (new Chennai and Pune build-out, p.7) |
| ROU assets | 3,732.53 | 3,138.94 | +18.9% |
| Intangibles + IAUD | 371.23 | 369.59 | internal software 236.65 net |
| Trade receivables billed + unbilled | 11,999.70 | 10,941.35 | +9.7%; 45.6% of current assets |
| Cash and equivalents | 3,685.66 | 2,434.46 | |
| Bank balances | 7,408.88 | 37.71 | deposits 7,369.61 moved from "other financial assets" (6,979.48 to 1,746.21) |
| Total assets | 37,056.82 | 31,375.51 | +18.1% |
| Equity | 25,350.70 | 22,430.10 | +13.0%; treasury shares -1,006.47 |
| Lease liabilities | 3,984.33 | 3,215.97 | +23.9% |
| Provisions (gratuity 1,062.86, leave 484.71) | 1,547.57 | 1,008.44 | +53.5% |
| Employee benefit payable | 3,220.22 | 2,499.95 | +28.8% |
| Trade payables | 1,192.23 | 929.71 | +28.2% |
| Borrowings | nil | nil | |

Liquid assets (derived): 3,685.66 + 7,408.88 + 1,701.39 + 53.31 = 12,849.24, versus management "cash and bank reserves Rs 127.3 Crore" (AR26 p.4) and "net cash position of Rs 127.3 Crore" (p.10). Not reproduced exactly (difference about 1.2 Cr); Screener shows Rs 110.95 Cr "Cash & Bank". "Net cash" ignores lease liabilities of 3,984.33: net of leases the figure is 8,864.91 (derived), and after the proposed dividend of 1,795.54 (Note 32 p.92) it is 7,069.37. After the Rs 18.00 Cr buyback (June 2026, outside the AR) about 5,269 (derived).

Key ratios (consolidated, derived unless stated):

| Ratio | FY26 | FY25 | Comment |
|---|---|---|---|
| D/E (borrowings) | 0 | 0 | Note 31 p.92 |
| D/E with leases | 0.16 | 0.14 | 3,984.33/25,350.70 |
| Net debt / EBITDA | net cash; lease-adjusted -1.23x | | (3,984.33 - 12,849.24)/7,184.59 |
| Current ratio | 3.66 (reported 3.66, p.47) | 3.87 | ties |
| Quick ratio | 3.66 | 3.87 | no inventory |
| Interest coverage | EBIT 5,604.90/289.05 = 19.4x; EBITDA basis 24.9x | 14.1x | MD&A reports 1.68 (p.47), not reproducible; definition NOT FOUND |
| ROE | 18.55% reported (p.47); ties on average equity 23,890.40 (derived) | 12.55% | |
| ROCE | reported 25.42% (p.47); my rebuild on the stated formula: PBIT 6,309.13 / (net worth 25,350.70 - intangibles 371.23 + DTL 315.80) = 24.9% | 17.34% | 0.5 point unreconciled; includes other income 704.23 |
| Operating pre-tax return on operating capital | 5,604.90/(25,350.70 + 3,984.33 - 12,849.24) = 34.0% | | strips cash and other income |
| Goodwill / net worth | 0% | 0% | none |

DuPont (average balances, derived): net margin 8.15% x asset turnover 1.589 (54,385.24/34,216.17) x equity multiplier 1.432 (34,216.17/23,890.40) = 18.55%. The multiplier is not financial leverage (borrowings are nil): it comes from operating liabilities and leases. ROE is operational, helped by margin expansion (FY25 net margin 5.51%).

## 3C P&L line walk (AR26 p.65, lakhs)

| Line | FY26 | FY25 | YoY | % revenue FY26 / FY25 |
|---|---|---|---|---|
| Revenue | 54,385.24 | 49,131.61 | +10.7% | |
| Employee cost | 39,582.25 | 38,011.83 | +4.1% | 72.8% / 77.4% |
| Sub-contracting (inside other expenses) | 3,407.42 | 2,494.19 | +36.6% | 6.27% / 5.08% |
| Other expenses ex sub-contracting | 4,210.98 | 4,155.98 | +1.3% | 7.74% / 8.46% |
| EBITDA | 7,184.59 | 4,469.61 | +60.7% | 13.21% / 9.10% |
| Depreciation | 1,579.69 | 1,338.69 | +18.0% | 2.9% / 2.7% |
| EBIT | 5,604.90 | 3,130.92 | +79.0% | 10.31% / 6.37% |
| Other income | 704.23 | 721.31 | -2.4% | |
| Finance cost | 289.05 | 222.25 | +30.1% | |
| PBT before exceptional | 6,020.08 | 3,629.98 | +65.8% | |
| Exceptional | 315.50 | nil | | |
| PBT | 5,704.58 | 3,629.98 | +57.2% | 10.5% / 7.4% |
| Tax | 1,272.19 | 922.21 | +38.0% | ETR 22.3% / 25.4% |
| PAT | 4,432.39 | 2,707.77 | +63.7% | 8.15% / 5.51% |

Margin bridge, EBITDA % of revenue FY25 to FY26 (derived): employee cost +4.59 points, sub-contracting -1.19, other expenses +0.72, total +4.11 = 13.21 - 9.10. Productivity: headcount 2,485 vs 2,581 (-3.7%, AR26 p.46); revenue per head Rs 21.88 lakhs vs 19.04 (+15.0%); employee cost per head Rs 15.93 lakhs vs 14.73 (+8.1%). Onsite share 29% vs 28% (p.46), so the gain is not an offshore shift despite the MD's "more efficient offshore-led delivery model" (p.10). The gain came from billing more revenue on fewer employees plus more sub-contractor delivery; whether price per hour rose is NOT FOUND IN DOCUMENT.

Other income = 704.23: bank deposit interest 536.02, security deposit unwinding 34.16, tax-refund interest 55.30, disposal gain 3.58, FX gain/(loss) (20.02), miscellaneous 95.19 (Note 20 p.85). Share of PBT: 12.3% on PBT 5,704.58 (11.7% on pre-exceptional PBT); FY25 19.9%. Under the 20% flag; FY25 was 0.1 point below it. Interest income on deposits is 76% of the line and will shrink with the Rs 18 Cr buyback and Rs 17.96 Cr dividend outflows (derived).

Exceptional pattern, 3 years: FY24 none, FY25 none, FY26 315.50. Tax rate: 22.3% vs 25.4%, 23.7% ex two one-way items (Note 12(b) p.80). Basic EPS 19.64 vs 11.97 (+64.1%); diluted 19.52 vs 11.81; gap 0.12 (0.6%) vs 0.16 (1.3%) (p.65, Note 25 p.87). Weighted shares 2,25,66,773 basic, 2,27,01,875 diluted, treasury shares excluded.

Screener 10-year margin context (Rs Cr; operating profit = sales less the listed expense rows, derived): FY20 8.6%, FY21 7.2%, FY22 7.0%, FY23 6.2%, FY24 11.1%, FY25 9.1%, FY26 13.2%. FY24 ties to AR25 EBITDA 52.2 Cr and FY26 to AR26 71.9 Cr. The base year for the company's "EBITDA CAGR 35.4%" (AR26 p.10) is the FY22 trough (7.0%).

## Phase 3 summary

| Check | Result |
|---|---|
| Cash | CFO 6,507.73 (146.8% of PAT); FCF after leases 3,591.68; no debt |
| Earnings | EBITDA +60.7% on revenue +10.7%; payroll leverage did the work |
| Quality caveats | Unbilled, subsidiary days, unpaid pay, Ind AS 116 uplift, tax rate help of about 1.4 points |
| Balance sheet | Very strong |

**Phase 3 verdict: 🟡 Watch (balance sheet and cash are green; the earnings step is one year old and part of it is tax and timing).**

Cross-reference with Phases 1-2: the unbilled and subsidiary-day drift (Phase 2) is the working-capital line that Phase 3 shows absorbing 612.32 of cash. The audit-trail carve-out (Phase 1) covers the system that produces these receivables.

**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because cash, balance sheet and coverage are sound. They would want the margin to be proven net of tax and R&D credit before they pay for it.

---------------------------------------------------------------------
# PHASE 4: RISK FACTORS AND MD&A

## 4A Disclosed risks (MD&A p.47-48, nine rows)

| Risk | Real or boilerplate | Evidence |
|---|---|---|
| Attrition | Real but unquantified | Names no rate. MD letter says LTM attrition 14.85% (p.11); BRSR says permanent employee turnover 37.93% (p.27). |
| Compliance | Boilerplate | No incident, no number |
| Strategic | Partly real | Names "leadership succession" and "deep, long-term engagement with clients"; no concentration |
| Technological | Boilerplate | Cyber controls listed; BRSR p.28 lists cyber as a material issue |
| Business continuity | Boilerplate | |
| Currency | Real | "Board-approved policy"; forwards and options. But forwards are undesignated and MTM goes through P&L (Note 29 p.89). |
| Tax-related | Boilerplate | Does not mention disputed dues of 277.30 |
| Geopolitical | Boilerplate | |
| Rivalry | Boilerplate | |

The cautionary statement (p.48) does list "client concentration risks" and "cost and time overruns in fixed-price contracts". That is the only place concentration is named, and it sits in the legal boilerplate.

## 4B Missing risks (obvious from Phases 1-3, absent from the risk section)

| # | Missing risk | Evidence anchor | Likely reason for omission |
|---|---|---|---|
| 1 | Single-customer dependence | 18.3% (Note 34 p.93), top 5 at 48% (p.46), IEHM vertical 63% (p.46) | Management frames concentration as "deeper engagement" (p.10) |
| 2 | Controls over the revenue billing system | Audit trail carve-out, second year (p.63) | Opinion is unmodified; the item is in the legal-requirements section |
| 3 | Credit and collection risk | Subsidiary billed days 81.3; unbilled 3,429.35 unaged (Notes 6, 30) | Consolidated ageing is clean (0.14% over 6 months) |
| 4 | Cost-mix shift to sub-contractors | +36.6% (Note 24 p.86) | Sits inside "other expenses"; not discussed in MD&A |
| 5 | Pay accruals, gratuity underfunding, labour code | Employee benefit payable 3,220.22; deficit 1,062.86; 315.50 on draft rules (Notes 15, 17) | Treated as a one-time exceptional |
| 6 | US legal and cash-freeze exposure | Ex parte freeze of 1,130.64 at the US subsidiary (Note 26 p.87); Directors' Report item 23 says no significant orders by courts (p.19) | Order vacated; classed as not probable |
| 7 | Europe shrinkage | Europe revenue 1,920.10 vs 3,359.11 (-42.8%, Note 34 p.93); MD&A "demand from the United States and Europe remains resilient" (p.47) | Offset by "Others" (UK and Canada) +17.8% (derived) |
| 8 | Disputed tax dues | 277.30 (CARO vii) outside Note 26 | "Remote" assessment |
| 9 | Headcount falling while revenue grows: -3.7% vs +10.7% | p.46, p.65 | Framed as productivity |
| 10 | Capital return pressure on cash: buyback Rs 18 Cr after year end | Announcements, not in AR | Post-approval event |

Management omission is itself a signal: items 1, 2 and 3 are the three most decision-relevant and all are missing from the risk table.

## 4C MD&A deep dive

- Industry claims (p.44-45): Nasscom figures for India IT (USD 315.4 Bn, +6.1%), ER&D outsourcing USD 81-82 Bn (CY24) to USD 133-135 Bn (CY30), growth 8.5-9.5%. Sourced; not tied to Onward's share. Market share NOT FOUND IN DOCUMENT.
- Growth and margin explanation: every ratio change (ROE, ROCE, operating margin, net margin) carries the same sentence, "Increased revenue and decrease in operating cost has resulted in increase in net profit" (p.47). Operating cost did not fall: employee cost +4.1% and other expenses +14.6% rose in rupees. Boilerplate, and wrong as written.
- Credit-taking and blaming: management takes credit ("disciplined execution, strong operational leverage, improving account quality", p.10). External factors appear only as tailwinds. No blame pattern. The UK R&D credit (135.94) and the FX swing (other income FX line from +79.58 to -20.02) are not discussed.
- Segment analysis: single segment (Note 34 p.93). Verticals: IEHM 63% (57%), T&M 34% (38%), HCLS 3% (4%) (p.46). Contract: T&M 88%. Geography in MD&A: India 52%, USA 36%, Europe 12% (p.46); Note 34: India 29,815.23 (54.8%), USA 16,177.39 (29.7%), Europe 1,920.10 (3.5%), Others 6,472.52 (11.9%) (derived). Differences are large and unexplained: Europe 12% in MD&A vs 3.5% in the note.
- Statement vs note on India: the MD letter says "approximately 70% from North America and 30% from Europe-headquartered customers, with no direct dependence on India-based demand" (p.10). Note 34 says the split "is based on the locations of the customers" (p.93) and shows 54.8% in India. Two readings: (A) India-located invoices go to Indian arms of global OEMs for global programmes (a GCC or ODC model), so the MD's phrase refers to the parent decision-makers; (B) real Indian-domestic demand. One observation separates them: the customer-level geography split in the earnings presentation or concall. NOT FOUND IN DOCUMENT in the AR.

Forward guidance table (also in the block):

| Claim | Number | Timeframe | Source | Credibility vs delivery |
|---|---|---|---|---|
| Double-digit growth in both revenue and EBITDA | "double-digit" | next three years from FY26 | AR25 p.16 | FY26: revenue +10.7%, EBITDA +60.7%. Met; revenue at the floor |
| Reiterated sustained double-digit revenue and EBITDA growth | "double-digit" | FY27 | AR26 p.11 | Forward; FY27 numbers outside AR |
| Capex budget Rs 12 crore for FY26 | 12 Cr | FY26 | AR25 p.16 | Cash capex 19.11 Cr (1,911.07 lakhs, p.66): exceeded by 59% (derived) |
| Client count to "consolidate further" | about 80 clients | FY26 | AR25 p.16 | 72 at FY26. Met |
| Offshore development capacity ahead of client demand; Chennai centre | no number | FY26-27 | AR26 p.7, p.11 | PP&E additions 2,156.00 (p.77). Revenue effect not yet visible |
| Expand international workforce | no number | "next few years" | AR26 p.46 | Total headcount fell 3.7%; split NOT FOUND IN DOCUMENT |
| AI: no material impact on scope, pricing or budgets | no number | current | AR26 p.11 | Untestable from the AR |
| Utilisation above 90% in Pune and Hyderabad | 90% | current | AR26 p.11 | NOT FOUND IN DOCUMENT to verify |

## 4D Tone and credibility (1-5)

| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 3 | Detailed notes and a KPI page (top 5/10/25, clients above USD 1 mn, DSO); but no named top customer, no customer share of receivables, no remediation date for the audit trail, buyback absent |
| Consistency | 2 | Attrition 14.85% vs turnover 37.93%; India 54.8% vs "no direct dependence"; Europe 12% vs 3.5%; Annexure IV pay increase 0% vs Note 27 +19.7% for the MD; "stable headcount" vs -3.7%; ESOP 2024 approval date; Directors' Report consolidated PAT typo 4,432.49 vs 4,432.39 (p.16) |
| Specificity | 3 | Good on KPIs and verticals; the ratio explanations are copy-paste |
| Accountability | 2 | Board calls the audit-trail items "self-explanatory"; a 50% attendance director proposed for a second term; concentration framed as strength |
| Capital allocation sense | 4 | No debt; dividend Rs 8 vs Rs 5; payout 55.8% of standalone PAT (p.16); capex into delivery capacity; buyback at Rs 328; the Trust loan and the Trust buying at Rs 325 for options struck at Rs 253.48 are mildly generous to employees |

**Phase 4 verdict: 🟡 Watch.** The disclosures are detailed. The narrative is selective and contradicts the notes in four places.

Contradictions vs Phases 1-3 (stated at the point): (1) Board "no adverse remark" vs the books-of-account carve-out (Phase 1). (2) MD&A "decrease in operating cost" vs Phase 3 cost lines. (3) Risk table silent on concentration, which Phase 2 ranked first. (4) "Debt covenants" and "committed credit lines" in Note 30 vs lapsed facilities in Note 8 (Phase 2F).

**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop; they would want the attrition and geography contradictions answered before relying on any management ratio.

---------------------------------------------------------------------
# PHASE 5: CORPORATE GOVERNANCE AND BOARD

## 5A Board composition (AR26 p.49-50; DIN dates p.60; other boards Annexure A p.58)

| Director | Category | On board since | Tenure (derived, to Mar 2026) | Listed boards | Board attendance | Flag |
|---|---|---|---|---|---|---|
| Harish Mehta | Promoter, Executive Chairman, father of MD | 18 Jul 1991 | 34.7 yrs | 1 | 4/4 | Founder-executive |
| Jigar Mehta | Promoter, MD | 16 May 2016 | 9.9 yrs | 1 | 4/4 | |
| Jay Sonawala | Independent, Audit Chair | 15 May 2020 | 5.9 yrs | 1 | 3/4 (75%) | Second term (approved 17 Jul 2023, p.56); term ends in 2026 by derivation; no succession in the AR |
| Harsha Raghavan | Non-executive, non-independent | 30 Jun 2021 | 4.8 yrs | 4 | 3/4 (75%) | No sitting fee paid (p.54); nominating shareholder NOT FOUND IN DOCUMENT; retires by rotation |
| Niranjani Chandramouli | Independent, RMC chair | 29 Sep 2022 | 3.5 yrs | 1 | 3/4 (75%) | RMC 2/3 (66.7%), NRC 1/2 (50%) |
| Dhanpal Jhaveri | Independent, NRC chair | 12 May 2023 | 2.9 yrs | 1 | 2/4 (50%) | Below 75% on Board, Audit Committee (2/4) and NRC (1/2); proposed for a second term (p.16) |
| Jai Diwanji | Independent, SRC chair | 12 May 2023 | 2.9 yrs | 5 | 4/4 | Desai & Diwanji fees 9.76; proposed for a second term |

Board meetings: 4 held (16 May 2025, 16 Jul, 17 Oct, 16 Jan 2026) at 71.43%, 71.43%, 85.71%, 100% attendance (p.50). Total attendance 23 of 28 seats = 82.1% (derived).
Flags tested: independents over 10 years: none. Attendance under 75%: Jhaveri (50%). Promoter-group cross-board seats: none beyond Onward. More than 8 seats: none (maximum 5). Women: 1 of 7 (BRSR p.27).
Independence test: the Governance Report says "There was no pecuniary relationship or transactions of the Non-Executive Directors vis-a-is the Company, which has potential conflict" (p.54). Note 27 shows professional fees of 9.76 to Desai & Diwanji, an "Entity controlled by Key Management Personnel" (p.88). Jai Diwanji's sitting fees were 3.20, so the firm's billing is 3.05x his fees (derived). The firm's size and the Reg 16(1)(b) 2% test: NOT FOUND IN DOCUMENT. 🟡.

## 5B Committees

| Committee | Members | Meetings | Remark |
|---|---|---|---|
| Audit (p.51) | Sonawala (chair), Raghavan, Chandramouli, Jhaveri | 4 (15 May 2025, 15 Jul, 17 Oct, 16 Jan 2026) | 3 of 4 independent; Jhaveri 50%; gaps under 120 days |
| NRC (p.52) | Jhaveri (chair), Chandramouli, Raghavan | 2 (14 May 2025, 15 Jul 2025) | Administers ESOPs; the ESOP 2019 grant of 19 Jan 2026 and the ESOP 2024 grant of 6 Feb 2026 (Note 35 p.94) fall after the last NRC meeting. [INFERENCE] Approval by circulation or another route; NOT FOUND IN DOCUMENT. |
| SRC (p.52) | Diwanji (chair), Jigar Mehta, Sonawala | 1 | 2 complaints, 0 pending |
| RMC (p.53) | Chandramouli (chair), Diwanji, Jigar Mehta | 3 (last 17 Oct 2025) | Chair attended 2 of 3 |
| CSR (p.53) | Harish (chair), Jigar, Chandramouli | 1 (17 Oct 2025) | Spent 62.47 = required |

Secretarial audit: Nilesh A. Pradhan & Co. LLP, one observation: the ESOP Trust had a trustee who was a director of the subsidiary, against SBEB Reg 3(4); the trustee resigned before signing (p.25). Remedied, but it shows Trust governance was set up after the Trust bought shares (Trust effective 2 April 2025, Note 27 p.87).

## 5C Compensation

| Item | FY26 | FY25 | Note |
|---|---|---|---|
| Harish Mehta | 383.17 (salary 142.00, allowances 28.17, incentive 213.00) | 372.24 | p.54, Note 27 p.88 |
| Jigar Mehta | 459.80 (salary 200.00, allowances 0.40, incentive 259.40) | 384.16 | |
| Together | 842.97 | 756.40 | |
| % of consolidated PAT | 19.0% | 27.9% | derived |
| % of standalone PAT 3,215.88 | 26.2% | 31.0% | derived |
| CFO Nathani | 60.92 | 48.80 | +24.8% (derived); Annexure IV says +16% (p.24) |
| CEO-to-median multiple | Harish 40.08x, Jigar 48.10x of median 9.56 lakhs (p.24) | | Both above 40x |
| Median pay growth | +12.53% | | Gratuity salary-growth assumption is 5.00% (Note 17 p.84), below this |
| Incentive share of pay | 55.6% / 56.4% | | Metric NOT FOUND IN DOCUMENT |

Inconsistency: Annexure IV shows 0% increase for both promoters (p.24); Note 27 shows +2.9% for Harish and +19.7% for Jigar (p.88). [INFERENCE] Annexure IV compares fixed pay only. 🟡. Special resolutions revised both promoters' pay at the 33rd AGM (19 Jul 2024, p.56).
Promoter-family payroll: Heral Mehta and Prachi Mehta (relatives) appear only as dividend recipients (12.50, 7.50); no payroll. Unpaid pay: Harish's payable rose from 54.69 to 224.83, Jigar's from 218.49 to 275.78 (KMP payable 506.29).
ESOP dilution 1.9% (Phase 2); the 2024 plan covers up to 11,25,000 shares (p.18), 3,00,000 granted.

## 5D Shareholding

| Holder | Mar 2024 | Mar 2025 | Mar 2026 | Sep 2026 (SHP) |
|---|---|---|---|---|
| JHM Enterprises | 75,97,866 (33.74%) | 77,50,000 (34.16%) | 78,50,000 (34.98%) | 78,75,000 (35.39%) |
| Harish + Jigar + Heral + Prachi | 9,85,923 (4.38%) | 10,20,059 (4.49%) | 10,40,059 (4.63%) | 10,70,186 (4.81%) |
| Promoter total | 85,83,789 (38.12%) | 87,70,059 (38.65%) | 88,90,059 (39.61%) | 89,45,186 (40.20%) |
| Infinity Direct | 39,00,000 (17.32%) | 19,80,000 (8.73%) | 19,80,000 (8.82%) | not named |
| Infinity Portfolio | nil | 19,20,000 (8.46%) | 19,20,000 (8.55%) | not named |

Sources: AR25 Note 13 p.147; AR26 Note 13 p.81; SHP Table II. Percentages are as printed. The Mar 2026 and Sep 2026 denominators exclude 3,09,679 Trust shares and the Sep 2026 base is after the buyback (SHP: total 2,22,49,390), so the percentage rise overstates the share-count rise. Share counts rose at every date (derived: +1,86,270, +1,20,000, +55,127). Promoters are accumulating, not selling.
Pledge: "No" for promoter encumbrance (SHP row 7). FII/DII: SHP Sep 2026 shows mutual funds 1.44%, AIF 0.29%, FPI Category I 8.52%, FPI Category II 0.75%, foreign companies 8.55%; earlier quarters NOT FOUND IN DOCUMENT (single-quarter corpus gap). Public holders: 21,314 holders at Mar 2026; 90.4% hold under 500 shares (p.57).
Dividends to promoters and relatives FY26: 392.50 + 11.00 + 20.00 + 12.50 + 7.50 = 443.50 (Note 27); 39.1% of the 1,134.25 paid (derived).
Promoter selling against the growth narrative: none. FLAG-PROMOTER-PRELIM: not raised.
Fact 4 trace: the Mar 2024 line also shows JHM "Percentage of change during the year" 100.00% and Heral -1.50%, Prachi -0.42% (AR25 p.147), consistent with the family consolidating holdings into JHM during FY24. [INFERENCE] The route from 61.71% (Mar 2021) is outside this corpus.

## 5E Governance red-flag checklist

| Check | Result | Anchor |
|---|---|---|
| Whistleblower complaints | None | CARO xi(c) p.100 |
| SEBI/exchange actions, 3 years | None | p.55 |
| RPT committee | Audit Committee approves; Board report says no material RPT | p.54, p.18 |
| Auditor fee ratio | 6.3% non-audit | Note 24(a) p.86 |
| CSR compliance | Fully spent, 62.47 | p.86 |
| s.143(12) fraud | None | p.18 |
| Material subsidiary auditor / independent director on its board | NOT FOUND IN DOCUMENT | p.55 |
| Audit trail | Carve-out | p.63 |
| ESOP Trust set-up | Remedied breach | p.25 |
| Independent director fees | 9.76 vs statement of "no pecuniary relationship" | p.54, p.88 |
| Audit Chair term | Ends 2026 by derivation; no replacement named | p.56, p.60 |

**Phase 5 verdict: 🟡 Watch.** No pledge, promoters buying, 4 of 7 independent, clean CSR and compliance record. Against that: one director at 50% attendance up for a second term, an independent director's firm paid 9.76 against a "no pecuniary relationship" statement, the Audit Chair's term, a thin NRC calendar, and promoter pay of 19% of PAT.

**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because there is no pledge, no sell-down and no regulatory action. They would want the Infinity block's rights and the Audit Chair succession checked at B08.

---------------------------------------------------------------------
# PHASE 6: CHAIRMAN'S LETTER AND FRONT MATTER (read last)

## 6A Narrative vs reality

| # | Claim (AR26) | Reality | ✅/❌ |
|---|---|---|---|
| 1 | "record EBITDA of Rs 71.9 Crore, up 60.9%" and margin "13.2% ... 412 basis points" (MD, p.10) | 7,184.59 lakhs (derived +60.7%); 13.21% vs 9.10% = +411 bps (p.65) | ✅ |
| 2 | "robust operating cash flows, resulting in a net cash position of Rs 127.3 Crore" (p.10) | CFO 6,507.73 vs 3,152.30. Liquid assets 12,849.24 (derived), 127.3 not reproduced; "net" omits leases of 3,984.33 | ✅ with caveat |
| 3 | "stable headcount of approximately 2,485" with "significant gains in productivity" (p.10) | Headcount 2,581 to 2,485 (-3.7%); revenue per head +15.0% | ❌ on "stable", ✅ on productivity |
| 4 | "top 25 clients contribute 87% ... deeper engagement" (p.10); "customer portfolio has also become stronger" | Top 25 87% vs 84%; single customer 18.3% vs 17.2% vs 12.7%; active clients 80 to 72. AR25 said "actively nurturing a broader customer base to balance growth with diversification" (AR25 p.20). | ❌ |
| 5 | "approximately 70% from North America and 30% from Europe ... no direct dependence on India-based demand" (p.10) | Note 34 customer location: India 54.8%, USA 29.7%, Europe 3.5% | ❌ pending reconciliation |
| 6 | "LTM attrition reduced to 14.85%, one of the lowest levels" (p.11) | BRSR turnover 37.93% (FY25 40.40%, FY24 31.54%), p.27. Definitions differ and are not reconciled. | ❌ |
| 7 | "revenue CAGR of 15.3% and EBITDA CAGR of 35.4%" over four years (p.10) | Revenue FY22 307.27 to FY26 543.85 Rs Cr gives 15.3% (derived, Screener). EBITDA endpoint is the FY22 trough margin of 7.0% | ✅ on revenue; the EBITDA CAGR flatters |
| 8 | "efficient offshore-led delivery model" (p.10) | Offshore 71% vs 72% (p.46) | ❌ |

## 6B Strategic priorities

"Deepening strategic account relationships; scaling offshore delivery and efficiency; moving up the value chain in digital, software and AI-led services" (p.10). Specific enough: moderately (no targets). Capital allocated: capex 19.11 Cr (derived), Chennai centre and Pune upgrade (p.7), ESOP Trust Rs 10.06 Cr, Rs 18 Cr buyback after year end. Execution evidence: revenue per head +15.0%; software share about 50% (p.11); offshore share not rising; HCLS shrinking (6E).

## 6C Metrics showcased vs absent

Showcased: total income, EBITDA, margin, PAT ex exceptional, cash, top 25 share, attrition 14.85%, utilisation above 90%, CAGR. Absent: single-customer share (only in Note 34), order or deal wins, revenue from new vs existing clients, pricing or rate-card change, onshore headcount, sub-contractor share, DSO trend discussion, buyback, remediation of audit trail, receivable share of the large customer.

## 6D Tone and priority drift vs prior year

AR25: "double-digit growth in revenue and EBITDA over three years", capex budget Rs 12 Cr, "serve around 80 clients ... consolidate", "diversification", "new project offices next to large clients in USA, UK, Germany", HCLS "newly created" vertical (AR25 p.16, p.20). AR26: the guidance is "reiterated"; concentration reframed as strength; AI and a Global Leadership Team added; headcount "stable"; the "diversification" language and the HCLS growth language have dropped out of the MD letter. The tone moves from building (AR25) to harvesting (AR26).

## 6E Quiet Abandonment Check

| # | Opening claim (quote) | Where it should show | What it shows | Class | Materiality |
|---|---|---|---|---|---|
| 1 | AR25 p.16: HCLS "newly created ... will continue to drive our long-term success"; AR26 MD&A p.46: "continued to invest in strengthening its Healthcare & Life Sciences (HCLS) vertical" | Revenue by industry, p.46; AR25 chart p.20 | HCLS 8% of revenue (FY24), 4% (FY25), 3% (FY26) = about 3,779, 1,965, 1,632 lakhs (derived from rounded percentages; range for the two-year fall is about 46% to 66%) | (a) implicit retraction, no acknowledgement | Moderate: 3% of revenue, but it was a named growth vertical |
| 2 | AR25 p.20: "actively nurturing a broader customer base to balance growth with diversification" | KPI p.46, Note 34 p.93 | Top 25 from 84% to 87%; one customer 18.3%; active clients 80 to 72 | (a) implicit retraction | High: bears on thesis risk |
| 3 | AR25 p.16 and p.19: Europe "grown through client expansion and targeted investments"; "new project offices ... in USA, UK, and Germany" | Note 34 p.93; RPT p.124-125 | Europe revenue 3,359.11 to 1,920.10; sales to GmbH 2,303.30 to 1,237.13; management fee from GmbH 116.19 to 22.94 | (c) hedged retreat: MD&A says Europe "resilient" (p.47) without the number | Moderate to high |
| 4 | AR26 p.7, p.10: "Global Leadership Team" and "seasoned leaders across our three core verticals" | Governance Report senior management, p.55 | Senior management listed as only the CFO and the Company Secretary; no named vertical heads anywhere | (b) silent drop in governance disclosure | Moderate: governance, and who runs the verticals is unknown |
| 5 | AR26 p.10: "no direct dependence on India-based demand" | Note 34 p.93 | India 54.8% of revenue | (a) implicit retraction | High until reconciled |

Five abandonments or contradictions found. Phase 4 catches what the AR leaves out; 6E catches what it says and then withdraws. They are kept apart.

**Phase 6 verdict: 🟡 Watch.** Five of the eight tested claims fail in whole or in part (3, 4, 5, 6, 8); the financial claims (1, 2, 7) hold and the operating narrative is selective.

---------------------------------------------------------------------
# PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

Price data. Screener meta: current price Rs 375.65, market capitalisation Rs 841.82 Cr (date of capture NOT FOUND IN DOCUMENT). Derived: trailing P/E 19.0x on PAT 44.32 Cr (18.0x on Rs 46.7 Cr ex-exceptional, AR26 p.10); EV/EBITDA about 9.9x on market cap less Rs 127.3 Cr and EBITDA Rs 71.9 Cr. This stage reads the past; no valuation is formed.

| Strategy | Call | Top 3 reasons |
|---|---|---|
| Value + Quality | WATCHLIST | (1) Quality passes: ROE 18.55%, ROCE 25.42%, no debt, liquid assets about 15% of market cap (derived). (2) Not deep value: P/E about 19x, EV/EBITDA about 9.9x after a 61% EBITDA step. (3) Quality is capped by an 18.3% customer and a margin that ranged 6.2% to 13.2% over FY20-FY26. |
| **GARP** | **WATCHLIST** | See below. |
| **Turnaround** | **PASS (completed phase), durability open** | See below. |
| Capex-Led Growth | WATCHLIST | (1) Capex stepped up 5.2x to 19.11 Cr (derived) with PP&E additions 2,156.00 (p.77). (2) Revenue is not capex-led: headcount fell 3.7% and offshore share slipped. (3) Payoff test: FY27 revenue per head and utilisation of the Chennai centre. |
| Cash Flow Compounder | WATCHLIST | (1) CFO/PAT 151% over FY24-FY26. (2) FY22 and FY23 CFO were -3.93 and 5.75 Rs Cr. (3) FCF after leases 3,591.68 lakhs is 81% of PAT and the business is asset-light; the FY27 buyback (Rs 18.00 Cr) plus final dividend (Rs 17.96 Cr) take about Rs 36 Cr of cash. |
| Contrarian | FAIL | (1) FY26 BSE range was 206.80 to 382.00 (p.56); the Screener price of 375.65 sits at the top of that range. (2) Results are at record levels, not distressed. (3) No negative sentiment is visible to fade at this price. |
| Insider Confidence | PASS | (1) Promoter share count up at every date, 85,83,789 to 89,45,186 (Phase 5D). (2) No pledge (SHP row 7). (3) Caution: promoter pay of 842.97 lakhs and unpaid pay of 506.29 sit alongside; buyback tender behaviour NOT FOUND IN DOCUMENT. |
| Guidance Divergence | WATCHLIST | (1) FY26 guided as double-digit growth; delivered +10.7% revenue and +60.7% EBITDA. (2) B00 reports the FY27 revenue guide later raised to 15-18% and Q2 FY27 margin above guide: outside the AR. (3) Baseline for the concall stage only. |

**GARP, fullest reasoning.** Growth is real but narrow: revenue +10.7% and EPS +64.1%. The EPS jump rests on two things. First, an EBITDA margin gain of 4.1 points that came from payroll leverage on 3.7% fewer people (Phase 3). Second, a lower tax rate (22.3% vs 25.4%), of which about 1.4 points come from two one-way items (Note 12(b)). The growth an investor should pay for is the repeatable part, and the AR gives one year at a 13% margin against a FY20-FY26 range of 6.2% to 13.2% (Screener, derived). At about 19x trailing P/E the price already assumes part of the new margin lasts. The quality side of "reasonable price" passes: ROE 18.55% and ROCE 25.42% with no debt. Evidence that would move GARP to PASS: FY27 H1 margin held net of the R&D credit and a tax-rate reversion; a stated customer share of receivables; sub-contract share steady. Evidence that would move it to FAIL: the top customer above 20%, or billed-plus-unbilled days above 85 with no growth in revenue per head. Concentration (18.3% in one name, 48% in five) is the main limit on any "growth at a reasonable price" label. It is a WATCHLIST because the growth quality is unproven, not because the multiple is high.

**Turnaround, fullest reasoning.** The numbers show a completed margin turnaround: EBITDA from Rs 27.27 Cr (FY23, 6.2%) to Rs 71.85 Cr (FY26, 13.2%), 2.6x in three years (derived from Screener); PAT from Rs 11.48 Cr to Rs 44.32 Cr; CFO from -3.93 Cr (FY22) to 65.08 Cr (FY26). Operating levers named in the AR: vertical-led organisation (AR25 p.16), phase-out of non-core legacy services (AR25 p.19), account-centric model, productivity per head; a Global Leadership Team is announced (AR26 p.10). The turnaround is not linear: FY25 fell back to 9.1% from 11.1%. What the AR does not show is whether the recovered margin is a new base or a peak: sub-contract mix is rising, the UK R&D credit (135.94) and the tax rate sit under it, and the Rs 2.9 Cr Q2 FY27 credit adds a further question. The "PASS" is for the recovery, not for durability.

---------------------------------------------------------------------
# PHASE 8: FINAL VERDICT DASHBOARD

## Company snapshot (consolidated, lakhs unless stated)

| Item | Value |
|---|---|
| Revenue FY26 | 54,385.24 (+10.7%) |
| EBITDA / margin | 7,184.59 / 13.21% (FY25 9.10%) |
| PAT | 4,432.39 (+63.7%); EPS 19.64 basic |
| CFO / FCF after leases | 6,507.73 / 3,591.68 |
| Liquid assets / borrowings | 12,849.24 (derived) / nil |
| Net worth | 25,350.70 |
| ROE / ROCE | 18.55% / 25.42% (reported) |
| Headcount | 2,485 (-3.7%) |
| Top customer / top 5 / top 25 | 18.3% / 48% / 87% |
| Promoters | 39.61% (Mar 2026), 40.20% (Sep 2026), no pledge |

## Phase verdicts

| Phase | Verdict |
|---|---|
| 1 Auditor and CARO | 🟡 |
| 2 Notes | 🟡 |
| 3 Financials | 🟡 |
| 4 Risk and MD&A | 🟡 |
| 5 Governance | 🟡 |
| 6 Front matter | 🟡 |
| 7 Best-fit strategy | Turnaround (PASS), GARP (WATCHLIST) |

## Overall quality score: 7.0 / 10

| Component (25% each) | Score | Basis |
|---|---|---|
| Governance | 6.0 | No pledge, promoters accumulating, clean CSR and compliance; but a 50% attendance director up for a second term, an independent director's firm paid, audit trail carve-out, family-led board with pay at 19% of PAT, Audit Chair term gap |
| Accounting quality | 7.0 | Agrees with B02 (7/10). Detailed notes, conservative ECL; thin causes, three non-ties, lease table error, unbilled unaged |
| Balance sheet | 8.5 | Zero debt, 12,849.24 liquid, current ratio 3.66; less for leases 3,984.33, gratuity 11.5% funded, no committed lines |
| Earnings quality | 6.5 | CFO above PAT, other income 12.3% of PBT, small capitalisation; against it a one-year margin step, tax help, concentration, sub-contract shift |

## Top 3 strengths

1. Balance sheet and cash: no borrowings, liquid assets 12,849.24 lakhs, CFO 6,507.73 lakhs (AR26 p.65-66, Notes 7-8).
2. Operating leverage with fewer people: EBITDA margin 9.10% to 13.21%, revenue per head +15.0%, ROE 18.55% (p.46, p.47, p.65).
3. Promoter alignment in the register: share count up at every date, no pledge, dividend lifted to Rs 8 (AR25 p.147, AR26 p.81, SHP).

## Top 3 red flags

1. One customer at 18.3% (up from 12.7% in two years), top 5 at 48%, top 25 at 87%; unnamed, receivable share unknown, absent from the risk table (Note 34 p.93, p.46, p.48).
2. Revenue-system control and collection drift together: audit trail carve-out on the GL and billing system for the second year with no remediation date (p.63), subsidiary billed days 70.1 to 81.3, unbilled +13.2% and unaged (Notes 6, 30).
3. The narrative contradicts the notes: attrition 14.85% vs 37.93%, "no India dependence" vs 54.8%, Europe 12% vs 3.5%, promoter pay increase 0% vs +19.7%, plus an independent director's firm paid 9.76 against a "no pecuniary relationship" statement (p.10-11, p.27, p.93, p.24, p.88, p.54).

## Key monitorables for the next quarter

| Metric | Threshold | Where | Why |
|---|---|---|---|
| Top customer share of revenue | Any rise above 18.3%; red above 20% | Earnings deck, AR27 Note 34 | One name is the largest thesis risk |
| DSO billed + unbilled | Above 80.5 days (year-end FY26), target 65-70 per B00 | Quarterly KPI page | Subsidiary billed days rose 11.2 days |
| Unbilled revenue growth vs revenue growth | Unbilled growth above revenue growth two quarters in a row | Balance sheet, Note 6 | Unaged, unprovided |
| Sub-contracting % of revenue | Above 7.0% (FY26 6.27%) | P&L other expenses note | Mix shift behind the margin gain |
| EBITDA margin ex R&D credit | Below 13.0% (FY26 12.96%); check the Rs 2.9 Cr Q2 FY27 credit | Results filing, concall | Durability of the turnaround |
| Revenue per employee | Growth below 10% | Presentation, headcount | Tests that productivity is not one-off |
| Audit trail paragraph | Repeat in FY27 report | AR27 auditor's report | Closure or third year |
| Promoter holding and pledge | Below 39.5% or any pledge | Quarterly SHP | Insider signal |
| Gratuity contribution | Below 1,000 of the 1,339.10 expected | AR27 Note 17 | Plan assets fell to 137.84 |
| Clients above USD 1 mn | Below 16 | Presentation | Account depth |

## One-line verdict

A completed margin turnaround on a clean balance sheet, held back by one 18.3% customer, a second year of audit-trail limits on the billing system, and a front section that does not match the notes: best fit is Turnaround, with GARP on watch until margin and cash conversion repeat.

---------------------------------------------------------------------
## Output block

```yaml
stage: B03-ardeep
company: "ONWARDTEC"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "shareholding/ holds only the Sep 2026 pattern: FII/DII and pledge trend beyond one quarter NOT FOUND; AR gives promoter and 5% holders at Mar 2024, Mar 2025, Mar 2026 only"
  - "screener P&L, Quarters, Balance Sheet, Cash Flow exports empty; only Data_Sheet used"
  - "ICRA rating withdrawn 2023-11-13; no live rating"
  - "announcements folder is hand-filled, not the full Reg 30 record (buyback filings read from it)"
  - "FY21 to FY23 annual reports not in corpus: path of promoter holding from 61.71% (Mar 2021) to 38.12% (Mar 2024) NOT FOUND"
  - "AR does not give: customer share of receivables, names of the 4 unaudited subsidiaries and their auditors, Reg 24 independent director on the US material subsidiary, Ind AS 116 discount rate, definition of management DSO 75 and interest coverage 1.68, nominator of Harsha Raghavan, remediation date for audit trail"
flags:
  - {type: FLAG-CASH, reason: "carried from B02 as a quality flag: headline CFO 6,507.73 lakhs (146.8% of PAT) shows no deterioration, but subsidiary billed days 70.1 to 81.3, unbilled +13.2%, 15.3% of CFO from pay accruals, Ind AS 116 uplift of 22.7 points (AR26 p.66, Notes 6, 15)"}
  - {type: FLAG-CONCENTRATION, reason: "one customer 18.3% (9,965.52 lakhs), top 5 48%, top 25 87%; absent from risk table (AR26 Note 34 p.93, p.46, p.48)"}
  - {type: FLAG-CONTROLS, reason: "auditor unable to comment on audit trail tampering in GL and revenue billing system, second year, no remediation date (AR26 p.63, AR25 p.108-109)"}
  - {type: FLAG-COSTMIX, reason: "sub-contracting 3,407.42 lakhs +36.6% vs revenue +10.7% (Note 24 p.86)"}
  - {type: FLAG-FX, reason: "forward sell book 2,673.14 vs parent net exposure 891.69, undesignated, MTM liability 129.78 through P&L (Notes 29, 38; standalone p.128)"}
  - {type: FLAG-DISCLOSURE-CONFLICT, reason: "attrition 14.85% (p.11) vs BRSR turnover 37.93% (p.27); India 54.8% of revenue (Note 34 p.93) vs 'no direct dependence on India-based demand' (p.10); Europe 12% (p.46) vs 3.5% (Note 34); Annexure IV promoter pay +0% (p.24) vs Note 27 +19.7% for MD (p.88)"}
  - {type: FLAG-INDEPENDENCE, reason: "Desai & Diwanji, entity controlled by KMP, billed 9.76 lakhs (+190.5%) (Note 27 p.88) while Governance Report states no pecuniary relationship (p.54); Dhanpal Jhaveri attendance 50% on board and Audit Committee, proposed for second term (p.50-51, p.16)"}
phase_verdicts: {p1: "YELLOW Watch: unmodified opinion, audit trail carve-out second year", p2: "YELLOW Watch: 15 of 15 verified, lease table short 387.45, CARO disputed dues outside Note 26", p3: "YELLOW Watch: cash and balance sheet green, earnings step one year old", p4: "YELLOW Watch: risk table omits concentration, controls, collections; four contradictions", p5: "YELLOW Watch: no pledge, promoters buying; attendance, independence and Audit Chair term items", p6: "YELLOW Watch: five of eight narrative claims fail in whole or part; 5 quiet abandonments or contradictions", p7_best_fit: "Turnaround (PASS, completed phase); GARP WATCHLIST"}
overall_quality: 7.0
quality_components: {governance: 6.0, accounting: 7.0, balance_sheet: 8.5, earnings: 6.5}
kill_switch_notes:
  - "P1: human reviewer would not stop; asks for SOC report timeline on billing system"
  - "P2: would not stop; asks one question each on lease table (387.45 short) and CARO 277.30 vs Note 26"
  - "P3: would not stop; wants margin proven net of tax and R&D credit"
  - "P4: would not stop; wants attrition and geography contradictions answered"
  - "P5: would not stop; wants Infinity block rights and Audit Chair succession checked at B08"
triple_pass_verification:
  verified: 15
  discrepancies:
    - {finding_rank: 3, triple_pass_value: "RPT receivables exceed standalone Note 8 by 345.60", ar_value: "335.00 on subsidiary-only basis (607.40 includes JNTL 10.60 that sits in billed); FY25 gap 61.04", note_ref: "standalone Note 8 p.115; Note 26 p.125"}
    - {finding_rank: 15, triple_pass_value: "Note 31 at p.93", ar_value: "Note 31 at p.92", note_ref: "Note 31 p.92"}
    - {finding_rank: 13, triple_pass_value: "Infinity Direct 195.00 dividend, two readings", ar_value: "closed: 39,00,000 shares at Mar 2024 split 19,80,000 + 19,20,000 at Mar 2025; 195.00 = 39 lakh x Rs 5 in both years", note_ref: "AR25 Note 13 p.147; AR26 Note 13 p.81, Note 27 p.88"}
missing_risks:
  - {risk: "single-customer dependence", evidence: "18.3% (Note 34 p.93), top 5 48% (p.46); risk table p.47-48 silent"}
  - {risk: "control over revenue billing system", evidence: "audit trail carve-out (p.63)"}
  - {risk: "credit and collection drift", evidence: "subsidiary billed days 70.1 to 81.3, unbilled 3,429.35 unaged (Notes 6, 30 p.78, p.90)"}
  - {risk: "cost-mix shift to sub-contractors", evidence: "+36.6% (Note 24 p.86)"}
  - {risk: "pay accruals, gratuity underfunding, labour code", evidence: "employee benefit payable 3,220.22, deficit 1,062.86, 315.50 on draft rules (Notes 15, 17 p.82-84)"}
  - {risk: "US legal and cash-freeze exposure", evidence: "1,130.64 frozen ex parte (Note 26 p.87); Directors' Report item 23 p.19"}
  - {risk: "Europe shrinkage", evidence: "1,920.10 vs 3,359.11 (Note 34 p.93) vs MD&A 'resilient' p.47"}
  - {risk: "disputed tax dues outside contingent liabilities", evidence: "277.30 (CARO vii p.99) vs Note 26 p.87"}
guidance_table:
  - {claim: "double-digit growth in both revenue and EBITDA", number: "double-digit", timeframe: "three years from FY26 (AR25 p.16)", credibility: "met in FY26: revenue +10.7% (at the floor), EBITDA +60.7%"}
  - {claim: "sustained double-digit revenue and EBITDA growth reiterated", number: "double-digit", timeframe: "FY27 (AR26 p.11)", credibility: "forward; FY27 outside AR"}
  - {claim: "capex budget Rs 12 crore", number: "12 Cr", timeframe: "FY26 (AR25 p.16)", credibility: "exceeded: cash capex 1,911.07 lakhs (p.66)"}
  - {claim: "client count to consolidate", number: "about 80", timeframe: "FY26 (AR25 p.16)", credibility: "met: 72 active clients"}
  - {claim: "expand international workforce", number: "none", timeframe: "next few years (AR26 p.46)", credibility: "unproven: headcount -3.7%, split NOT FOUND"}
monitorables:
  - {metric: "top customer share of revenue", threshold: "above 18.3% flag, above 20% red", where: "earnings deck, AR27 Note 34", why: "one name is the largest thesis risk"}
  - {metric: "DSO billed + unbilled", threshold: "above 80.5 days; target 65-70 per B00", where: "quarterly KPI page", why: "subsidiary days rose 11.2"}
  - {metric: "unbilled growth vs revenue growth", threshold: "unbilled faster two quarters running", where: "balance sheet Note 6", why: "unaged and unprovided"}
  - {metric: "sub-contracting % of revenue", threshold: "above 7.0% (FY26 6.27%)", where: "other expenses note", why: "mix shift behind margin gain"}
  - {metric: "EBITDA margin ex R&D credit", threshold: "below 13.0% (FY26 12.96%)", where: "results filing, concall", why: "durability of turnaround; check Rs 2.9 Cr Q2 FY27 credit"}
  - {metric: "revenue per employee growth", threshold: "below 10%", where: "presentation, headcount", why: "productivity not one-off"}
  - {metric: "audit trail paragraph in FY27 auditor's report", threshold: "repeated", where: "AR27 auditor's report", why: "closure or third year"}
  - {metric: "promoter holding and pledge", threshold: "below 39.5% or any pledge", where: "quarterly SHP", why: "insider signal"}
  - {metric: "gratuity employer contribution", threshold: "below 1,000 lakhs of 1,339.10 expected", where: "AR27 Note 17", why: "plan assets fell to 137.84"}
  - {metric: "clients above USD 1 mn", threshold: "below 16", where: "presentation", why: "account depth"}
ar_new_downstream_entities:
  - name: "JNTL Consumer Health (India) Private Limited"
    where_in_ar: "Note 27 related party (common director from 8 May 2025), revenue 160.63 lakhs, receivable 10.60 (AR26 p.87-88)"
    entity_type: "customer and related party"
  - name: "Onward Technologies Employees Welfare Trust (trustee Qapita Equitytech Limited)"
    where_in_ar: "Note 27 (effective 2 April 2025, p.87); Annexure III-A (loan 1,007.77 lakhs, p.23); Secretarial Audit (p.25)"
    entity_type: "employee benefit trust and ESOP counterparty"
strengths_top3:
  - "no borrowings, liquid assets 12,849.24 lakhs (derived), CFO 6,507.73 lakhs"
  - "EBITDA margin 9.10% to 13.21% with revenue per head +15.0%, ROE 18.55%"
  - "promoter share count up at every date, no pledge, dividend Rs 8 vs Rs 5"
red_flags_top3:
  - "one customer 18.3% (up from 12.7%), top 5 48%, top 25 87%, absent from risk table"
  - "audit trail carve-out on GL and revenue billing system (second year) plus subsidiary billed days 70.1 to 81.3 and unaged unbilled"
  - "narrative contradicts notes (attrition, India share, Europe share, promoter pay) and an independent director's firm paid 9.76 against a no-pecuniary-relationship statement"
best_fit_strategy: "Turnaround (PASS, completed phase); GARP on WATCHLIST"
one_line_verdict: "A completed margin turnaround on a clean balance sheet, held back by one 18.3% customer, a second year of audit-trail limits on the billing system and a front section that does not match the notes."
analyst_note: "AR-side checks on the load-bearing facts. (1) The UK R&D credit (135.94 lakhs FY26) sits inside EBITDA by lowering employee cost; margin ex-credit 12.96% vs 13.21% reported. The Rs 2.9 Cr Q2 FY27 credit is outside this AR. (2) Promoter 38.12% at Mar 2024 ties to AR25 p.147; since then promoter share count rose at each date (85.84 lakh, 87.70, 88.90, 89.45 lakh shares). Infinity block (17.37%) is one 39 lakh share holding split in Sep 2024, not two buyers. Path from 61.71% is outside corpus. (3) Closing-vs-average FX gap of 6.3 to 7.3% explains up to about 5 of the 11.2-day rise in subsidiary billed days. (4) Buyback of Rs 18.00 Cr completed 15 Jun 2026 is absent from the AR published 22 Jun 2026 (statements approved 5 May). Use revenue/head, margin ex-credit and tax-adjusted PAT, not reported ROCE 25.42% or interest cover 1.68, which are not reproducible."
```
