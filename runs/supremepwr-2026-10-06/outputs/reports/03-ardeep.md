# STAGE 3: ANNUAL REPORT DEEP DIVE, BACKWARD READ - SUPREME POWER EQUIPMENT LTD (SUPREMEPWR)

Run: runs/supremepwr-2026-10-06 | 2026-10-06 | claude-sonnet-5-5 | Protocol v1.3 (pipeline mode)
Source: Annual_Report_FY2025-26.txt (21st AR, NSE Reg 34 filing 01-Sep-2026). Backward history: screener-Data_Sheet.csv (FY23-FY26, Rs Cr). Prospectus ABSENT (HIGH gap, carried).

## 0. READING RULES FOR THIS REPORT

- Units. Statements and Notes are Rs lakhs (printed on the face, AR p.60-96). MD&A tables, the highlights table (p.12) and the Data_Sheet are Rs Cr. Each number carries its unit. Lakhs / 100 = Cr. Nothing is converted silently.
- GAAP. Indian AS (Companies (Accounting Standards) Rules, 2021), not Ind AS (Note 2.1, p.62). The MD&A mentions "Ind AS 108" (p.18); that is wrong for this filer.
- Anchors. "p.N" is the page marker [page N] in the extracted .txt. Stage 2 (B02) anchors run one page higher (marker + 1). The numbers agree; only the page label differs.
- Tags. DERIVED = arithmetic on anchored AR numbers, formula shown. [INFERENCE] = reasoned reading, not a filed fact. Data_Sheet and operator context are labelled where used and are never AR evidence.
- Danya Electric Company (Danya) is the 90% profit-share partnership firm. Standalone = SPEL alone. Consolidated = SPEL + Danya (Note 2.2, consolidated p.83).

### 0.1 Carried flags and load-bearing facts (B01, B00, operator brief)

| Item | Carried | Result against the AR |
|---|---|---|
| B01 FLAG-GATE0 | History 4 years, classification GOOD, fragile (M3 FAT choice) | Carried unchanged. This stage does not re-score Gate 0. |
| B01 input gaps | Capex and payables FY23-FY24 NOT FOUND; peers not provided | Carried. AR p.12 gives FY24-FY26 payables only. |
| LB1 guidance vs delivery | FY26 guided 225 > 200 > 190 vs actual 181.64; FY27 275-300 vs 250-300 | The AR carries only FY27 Rs 275-300 Cr (MD&A p.19) and the FY26 actual Rs 181.6 Cr (p.12). The FY26 guidance cuts and the "250-300" are NOT FOUND IN DOCUMENT (call content, operator context). Not re-tested here. |
| LB2 Danya structure | Legal form, inter-company sales, minority share | Fully tested below. Danya carries five different labels in one AR (6E-7, 5E-6). |
| LB3 CFO vs capex vs debt | CFO 25.90, capex 57.48, borrowings 18.74 to 49.98 | CONFIRMED. Consolidated CFO 2,590.47, capex 5,748.04, borrowings 1,874.56 to 4,997.30 Rs lakhs (p.82, p.81, notes p.86). |
| LB4 Q1 FY27 revenue +37% vs PAT +10% | Operator context | Not an AR item. Data_Sheet quarters: revenue 48.23 vs 35.07 (+37.5%), net profit 4.90 vs 4.45 (+10.1%) Rs Cr. Mechanism shown in 3C-3 and Phase 7. |

---

## PHASE 1: AUDITOR'S REPORT AND CARO

### 1A Core opinion

| Item | Standalone (p.55-56) | Consolidated (p.76-78) |
|---|---|---|
| Opinion type | Unmodified. "give a true and fair view in conformity with the accounting principles generally accepted in India" | Unmodified, same wording |
| Basis | Standards on Auditing; ICAI Code of Ethics | Same |
| Going concern language | Only the standard management and auditor responsibility paragraphs (p.56). No "Material Uncertainty Related to Going Concern" paragraph. | Same (p.78) |
| CARO xix (standalone) | "no material uncertainty exists ... capable of meeting its liabilities existing at the date of balance sheet as and when they fall due within a period of one year ... We, however, state that this is not an assurance as to the future viability of the company." (p.58-59) | Not repeated; CARO xxi reference only (p.79) |
| IFC opinion | Adequate and operating effectively (p.60) | Same (p.80) |
| Signing | R. Rajaram, Partner, M.No 238452, P P N and Company (FRN 013623S), 27-May-2026. UDIN 26238452RMNJTR8572 | UDIN 26238452NPWLWY2673 |

Going concern: NONE. The only going-concern wording near stress is the AGM Notice line on Danya ("Related Party has sound financial standing and the business is continued as going concern in the last 3 financial years", Item 6, p.32), set beside its rating of Long Term BB-, Short Term A4+ on the same page. That is a management statement outside the audit report.

### 1B Key Audit Matters

| # | Subject | Why key (auditor) | How addressed | Risk |
|---|---|---|---|---|
| 1 | Revenue recognition (AS 9) (p.55; consol p.77) | Despatch volume near the reporting date, varying delivery terms, price variation claims, liquidated damages, warranty under AS 29 | Process and control understanding; sample of POs, despatch papers, e-way bills, customer acknowledgements; cut-off tests | 🟡 |
| 2 | Inventories (AS 2) (p.55; consol p.77) | Size of balance, overhead allocation, NRV judgement incl. "items held against orders that have since been amended or cancelled" | Attended physical verification, test counts, rate testing to supplier invoices and ageing | 🟡 |

Observations on the KAMs (each is a cross-reference, not a finding of misstatement):
1. The text is identical in the standalone and consolidated reports. The consolidated report adds no KAM for Danya, for the Rs 5,017.91 lakh intra-group elimination, or for unrealised profit in Danya inventory of 1,653.47 lakh (DERIVED: 6,209.72 - 4,556.25, Notes 16, p.68 and consol p.89).
2. KAM 1 names liquidated damages and warranty obligations. Notes show no LD or warranty provision in either year (Note 12 p.66 has only tax and gratuity). The KAM raises the exposure; the Notes do not size it.
3. KAM 2 names cancelled or amended orders as an NRV risk. Notes disclose no NRV write-down in either year (Note 16, p.68). Inventory rose 102.2% (4,556.25 vs 2,253.46 lakh).
4. KAM 2 refers to "contract work-in-progress". The Notes policy has no contract accounting and no WIP or finished goods valuation basis (policy 7, p.63). Policy text covers raw materials, consumables and loose tools only.
5. No KAM on the largest event of the year: Rs 4,031.30 lakh of CWIP capitalised, 48.0% of PPE additions booked directly (p.67), a CWIP ageing table that cannot be right (2.10 below), and Rs 2,130.06 lakh of new term debt.

### 1C Emphasis of Matter and Other Matters

| Item | Standalone | Consolidated |
|---|---|---|
| Emphasis of Matter | None | None |
| Other Matters | None | Danya (called "subsidiaries"): total assets Rs 3,195.97 lakh, revenue Rs 4,174.22 lakh. "This financial statements/ financial information is audited and have been furnished to us by the Management ... certified by the Management." Opinion "based solely on such audited financial statements". Material to the Group. (p.78) |

The Danya wording is ambiguous. The firm's auditor is not named. Whether P P N audited Danya or relied on another auditor is NOT FOUND IN DOCUMENT.

### 1D CARO 2020, clause by clause (standalone, p.57-59)

| Clause | Report | Amount / detail | Flag |
|---|---|---|---|
| i PPE, intangibles, titles, revaluation | Records kept; all PPE verified; titles in company name; no revaluation | Land additions 801.23 lakh (p.67) | 🟢 |
| ii(a) Inventory verification | Done at reasonable intervals "except for inventory lying with third parties"; those "substantially been confirmed" | Third-party inventory amount NOT FOUND | 🟡 |
| ii(b) Working capital returns | Quarterly returns "materially in agreement" with books | Note 30.6 (p.71-72): debtors in bank statements run 168.82, 168.82, 168.41, 171.02 lakh below books (3.78% to 4.97%); inventory Mar-26 43.58 lakh above books. Stated reason: provisional books. | 🟡 |
| iii Loans, guarantees | No loans. Guarantee Rs 1,470 lakh for "subsidiary" Danya outstanding. No guarantee "given during the year". | The Board's Report says guarantee "extension" of up to 14.70 Cr was given in FY26 (p.40); Notes say board resolution 28-Mar-2025 (Note 30.1A). CARO iii(b) says "investments made during the year are prima facie not prejudicial" though no investment was made (investment fell 1,276.96 to 1,267.73). Boilerplate. | 🟡 |
| iv Sections 185, 186 | "complied with the provisions of Sections 185 and 186" | AGM Item 9 (p.22, p.33) asks members to approve guarantees "for having given and for continuing to give" for Danya, a firm where the MD and the WTD are partners. Section 185(2) needs a special resolution. The FY26 Secretarial Audit lists no such resolution (p.49). Whether one was passed before 28-Mar-2025 is NOT FOUND. | 🔴 item, see below |
| v Deposits | None | | 🟢 |
| vi Cost records | Maintained; cost audit in progress (Board p.41) | | 🟢 |
| vii(a) Statutory dues | "regular in depositing"; no arrears over six months | Interest on statutory dues 55.34 lakh in P&L (Note 26, p.70), FY25 0.01. Net tax payable 394.25 lakh at year end (provision 530.75 less advance tax asset 136.50, Notes 12 and 19, DERIVED). | 🟡 |
| vii(b) Disputed dues | None | Orphan footnote "TDS Demand (1)" in Note 30.1A (p.71) with nil amounts | 🟢 |
| viii Unrecorded income | None | | 🟢 |
| ix Borrowing default | No default; no wilful defaulter; term loans applied to purpose; no short-term funds used long term | ix(d) cannot be tested: capex creditors inside payables are NOT FOUND | 🟡 |
| x IPO/preferential | Warrants 12,47,000 at Rs 169; Rs 526.86 lakh received; used for purpose | Note 30.2: utilised 441.48, unutilised 85.38 lakh (p.71) | 🟢 |
| xi Fraud, 143(12), whistle-blower | None; no whistle-blower complaints | | 🟢 |
| xiii RPT | Compliant with ss.177, 188; disclosed in Note 30.21 | Note 21 omits guarantees received from promoters and others (2B) | 🟡 |
| xiv Internal audit | Adequate | Internal auditor Jeevan & Associates (p.15) | 🟢 |
| xv Non-cash transactions with directors | None | | 🟢 |
| xvii Cash loss | None in FY26 or FY25 | | 🟢 |
| xviii Auditor resignation | None | | 🟢 |
| xix Going concern | See 1A | | 🟢 |
| xx Unspent CSR | None | Spent 37.00 vs required 36.97 lakh (p.51-52) | 🟢 |

The 🔴 item (clause iv). It is a compliance-timing question, not an audit qualification. Evidence: the guarantee was given on a board resolution of 28-Mar-2025 (Note 30.1A p.71); Item 9 asks approval "for having given" (p.22) and the explanatory statement says the approval "shall also be deemed to cover the Corporate Guarantee(s) already extended" (p.33). If no special resolution existed before the guarantee, section 185 was breached for FY25-FY26 and the CARO iv statement needs a basis. This stage cannot see the FY25 AR or the 20th AGM resolutions. Status: ASK MANAGEMENT; PENDING LIVE VERIFICATION of the 19-Sep-2025 AGM outcome.

Consolidated CARO (p.79): the auditor says it "reviewed the CARO reports of the subsidiary companies" and found no qualifications. Danya is a partnership firm. CARO does not apply to a firm, so no such report can exist. The statement is boilerplate.

Audit trail (Rule 11(g), p.57 and p.79): "has operated throughout the year for all relevant transactions" is followed by "for the periods where audit trail ... was enabled and operated throughout the year ... we did not come across any instance of ... tampering". The second sentence is conditional and hints that some period or software may not have had the feature enabled. NOT FOUND whether any gap exists.

### 1E Auditor continuity

| Item | Finding | Anchor |
|---|---|---|
| Firm | P P N and Company, Chennai, FRN 013623S, peer review cert 020690 | p.15, p.41 |
| Appointment | 18th AGM 29-Sep-2023, five years to the 23rd AGM in 2028 | Board p.41 |
| Tenure before 2023 | NOT FOUND (prospectus absent) | |
| Statutory audit fee | 10.00 lakh FY26 (8.50 FY25); tax audit 1.00 (1.00); total 11.00 (9.50) | Note 28, p.70 |
| Non-audit fee | Nil ("Other matters" nil in consolidated, p.90) | |
| Non-audit to audit ratio | 0.0 | |
| Fee vs size | 11.00 lakh = 0.058% of standalone revenue; fee +15.8% vs revenue +31.3% | DERIVED |
| Internal auditor | Jeevan & Associates (fee NOT FOUND) | p.15, p.20 |
| Cost auditor | N. Sivashankaran & Co., Rs 1.00 lakh plus taxes for FY27 | p.21, p.28 |
| Flag test (non-audit > audit) | Not triggered | |

### 1F Standalone vs consolidated

| Point | Finding |
|---|---|
| Extra qualification | None |
| Subsidiaries with different auditors | Danya's auditor NOT FOUND. Other Matters p.78 says its statements were "furnished to us by the Management". |
| Reliance on others | Danya is 22.98% of consolidated gross revenue (4,174.22 / 18,164.04, DERIVED) and 12.2% of consolidated total assets (3,195.97 / 26,139.10, DERIVED) |
| Labels for Danya in this one AR | Subsidiary (consolidated Note 2.2 p.83; CARO iii p.57; Note 30.10 p.72). Associate or JV (AOC-1 Part B, p.48). Related-party partnership firm (AOC-2 p.47; Notice Item 6 p.21). "The Company does not have any Holding or Subsidiaries Company" (Board p.43). "Only one subsidiary ... Danya" (Note 30.10). |

### Phase 1 summary

| Area | Result |
|---|---|
| Opinion | Unmodified, both reports; no EOM; no going-concern paragraph |
| KAMs | Two, both 🟡; none on Danya, capex or CWIP |
| CARO | Clean on face; clause iv timing item 🔴; clauses ii(b), vii(a), ix(d) 🟡 |
| Auditor | Continuity fine; no non-audit fees; Danya auditor unknown |
| Consolidation | Danya labelled five ways; CARO xxi statement is boilerplate |

Phase 1 verdict: 🟡 Watch.
Kill switch assessment: Based on phases so far, a human reviewer would not have reason to stop, because the opinions are unmodified and the CARO shows no default or fraud. The reviewer would have reason to ask for the section 185 resolution trail before relying on the Danya guarantee disclosure.

---

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

### 2.0 Verification of the triple-pass Top 15 (B02) against the AR

| Rank | B02 claim | AR value found | Result |
|---|---|---|---|
| 1 | Danya: 61.3% of its 4,174.22 turnover is SPEL; 95.6% of its growth; 28.6% of SPEL revenue growth; elimination 5,017.91 (FY25 2,443.09); profit share 211.51 = 90.6% of other income | SPEL purchases from Danya 2,558.08 / 4,174.22 = 61.28%. Danya turnover growth 4,174.22 - 2,834.96 = 1,339.26; SPEL purchase growth 2,558.08 - 1,278.20 = 1,279.88 = 95.57%. Sales to Danya growth 1,294.94 / revenue growth 4,527.90 = 28.60%. Elimination 2,558.08 + 2,459.83 = 5,017.91; FY25 1,278.20 + 1,164.89 = 2,443.09 (Note 20 consol p.89). 211.51 / 233.51 = 90.58% (Note 21 p.69). Consolidated profit 2,044.06 = standalone (p.81). | ✓ verified |
| 2 | CFO 2,773.36 vs capex 5,746.46; consolidated 2,590.47 vs 5,748.04; advances +1,445.75; payables +2,489.23; CFO ex advance build 1,327.61 | CFS p.61 and p.82 match. 1,710.36 - 264.61 = 1,445.75 (Note 11, p.67). 2,773.36 - 1,445.75 = 1,327.61. | ✓ verified |
| 3 | Debt 1,633.84 to 4,572.70; consolidated 1,874.56 to 4,997.30; ICICI 3,974.89 = 97.2% of term debt at 9.50%; current maturities 89.90 to 1,095.48; no undrawn lines | 2,993.80 + 1,578.90 = 4,572.70; 863.75 + 770.09 = 1,633.84 (p.60). Consolidated 3,311.60 + 1,685.70 = 4,997.30 (p.81). ICICI 3,500.00 + 474.89 = 3,974.89 / 4,089.28 = 97.20% (Note 6, p.65-66). Note 9 (p.66). Note 25(2) (p.75). Consolidated Note 25 omits the undrawn-facility line. | ✓ verified |
| 4 | ICICI table: current principal 1,005.19 vs 12 months EMI 713.28; balances exceed amortisable by about 701 | (53.03 + 6.41) x 12 = 713.28. 1,095.48 - 90.29 (Canara 63.33, IndusInd 10.60, HDFC about 16.36) = 1,005.19. PV of 53.03 for 72 months and 6.41 for 78 months at 9.50% = about 2,902 + 372 = 3,274; 3,974.89 - 3,274 = about 701. Added: the 3,500.00 balance is a round number under a column headed "EMI / Principal Amount", so it may be the sanctioned amount. | ✓ verified, with the round-number note |
| 5 | DSCR 2.44x (10.47x) = interest plus year-end current maturities; EBITDA +15.2% | (2,691.87 + 165.26 + 128.24) / (128.24 + 1,095.48) = 2,985.37 / 1,223.72 = 2.44. FY25: 2,592.25 / (157.71 + 89.90) = 10.47. EBITDA 2,985.37 / 2,592.25 = +15.2%. Consolidated 2.48x and 8.62x tie the same way (p.96); the consolidated text calls the denominator "repayments", it is next-year maturities. | ✓ verified |
| 6 | Inventory +102.2% vs revenue +31.3%; days 56.8 to 87.5; consolidated 77.4 to 124.8; no NRV write-down | 4,556.25 / 2,253.46 = 2.022; 19,007.73 / 14,479.83 = 1.313. Days on revenue basis tie. KAM wording ties (p.55). | ✓ verified |
| 7 | Guarantee 1,470.00 = 13.0% of net worth, 46% of Danya assets; SBI rows; FY27 Rs 125 Cr / Rs 75 Cr | 1,470 / 11,293.81 = 13.02%; 1,470 / 3,195.97 = 46.0%. Consolidated Note 10 (p.86) shows "Corporate Guarantee by M/s Supreme Power Equipment Limited" on IndusInd and SBI cash-credit rows; consolidated Note 30.1 guarantees nil (p.91). Items 6 and 9 (p.21-22, p.28-33). | ✓ verified |
| 8 | CWIP ageing impossible; 904.53 pre-FY26; 48.0% of additions skipped CWIP; depreciation 165.26 vs run-rate about 496 | 0-1 year 2,471.53 > additions 1,893.45 by 578.08; 2,797.98 - 1,893.45 = 904.53 vs 326.45 shown (Note 30.16, p.72; Note 13, p.67). PPE additions 7,746.30; CWIP transfers 4,031.30; direct 3,715.00 = 47.96%. Gross block / Schedule II lives = 497 (formula in 2A). | ✓ verified |
| 9 | Receivables 4,521.09 nil provision; over one year 588.04 (344.23); Q4 +1,135.32; bank gap 169-171; days 109.8 to 86.8 | Note 17 (p.68-69). 4,521.09 - 3,385.77 = 1,135.32 (+33.5%). Days tie. | ✓ verified |
| 10 | Commitments Nil vs CWIP 2,797.98 and CIF imports 105.34; capitalised interest NOT FOUND; interest 4.13% of average debt | Notes 30.1B (p.71), 29.I(2) (p.75), 17 (p.73). 128.24 / average debt 3,103.27 = 4.13%. CFS interest paid 128.24 = P&L interest 128.24, so no sign of capitalised interest in cash terms. | ✓ verified |
| 11 | Jai Bharath +47.95 on 1.12 sales; guarantees received absent from AS 18; 15.00 director fee vs Board report; promoter loan 311.30 no terms | JB receivable 56.60 vs 8.65 (Note 21, p.74). Guarantors named in Note 6 only. Devaraja Iyer 15.00 (Note 21) vs "other than payment of the sitting fees" (Board p.41). Consolidated Note 21 (p.94) names the 311.30 lender: Vee Rajmohan, "Loan Received from Partners". Terms NOT FOUND. | ✓ verified; lender identity added |
| 12 | Interest on statutory dues 55.34 (0.01) = 22.9% of finance cost; Danya 17.90; net tax unpaid 394.25; orphan TDS footnote | 55.34 / 241.58 = 22.9%; 73.24 - 55.34 = 17.90 (consol Note 26). 530.75 - 136.50 = 394.25 (Notes 12, 19). | ✓ verified |
| 13 | Payables 126.3 days (102.8); MSME 2,879.29 no 45-day split; Danya payable swings class | 5,954.07 / 17,210.72 x 365 = 126.3; 3,464.86 / 12,303.55 x 365 = 102.8. MSMED interest nil (p.67). Class swing is DERIVED from standalone vs consolidated Notes 10 and 11 (consolidated MSME 3,593.03 vs standalone 2,879.29). | ✓ verified |
| 14 | Promoter group 57.16% (Note 3 lists 52.07%); warrants 1,580.57 due about 27-Feb-2027; 63.9% from non-promoters; no pledge | Note 3 lists 52.07% (p.64). 2,107.43 - 526.86 = 1,580.57; 27-Aug-2025 + 18 months = 27-Feb-2027 (p.40, p.65). 57.16%, the 63.9% split and pledge status are NOT FOUND IN THE AR (SHP sourced). | ◐ verified on AR portion only |
| 15 | Clean base: unmodified, CARO clean, no tax disputes, no default, no policy change, CSR met, EPS dilution 4.99%, gratuity ties | Note 27 (p.75), Note 30.13 (p.72), 12.47 / 249.91 = 4.99% full-conversion dilution (reported FY26 diluted EPS 8.15 vs basic 8.18). Gratuity 14.81 + 6.40 + 1.00 + 9.52 = 31.73 vs 31.72. | ✓ verified (CARO iv caveat in 1D) |

Result: 14 of 15 fully verified, 1 verified on the AR portion only (rank 14). No numeric discrepancy. One labelling note: B02 pages are marker + 1.

### 2A Accounting policy aggressiveness (extension)

| Policy | Text found | Assessment | Rating |
|---|---|---|---|
| Revenue recognition | Generic text about "electrical contractors, estimators, planners, designers, research workers ..." and "services rendered" (policy 2, p.62). No wording on transfer of control for transformers, inspection, or price variation. | Policy does not describe how a transformer sale is recognised. The KAM supplies what the policy omits. Services revenue fell 754.90 to 78.75 lakh (Note 20) with no comment. | 🟡 |
| Depreciation lives | SLM, Schedule II lives. Buildings 60 years, P&M 15, testing equipment 15, vehicles 10, electrical 10, computers 3 (policy 4, p.62). | Schedule II gives 30 years for factory buildings; 60 years is the figure for non-factory RCC buildings. Kannur buildings (1,330.85 additions plus 1,258.12 CWIP) on 60 years: charge about 45 lakh a year vs about 90 lakh on 30 years (DERIVED, 2,589 / 60 vs 2,589 / 30). Vehicles 10 years vs 8 for motor cars. Small money, aggressive direction. | 🟡 |
| Depreciation run-rate | FY26 charge 165.26 lakh | Gross block 31-Mar-26 / lives: P&M 4,698.79/15 = 313.3; testing 1,170.34/15 = 78.0; electrical 425.22/10 = 42.5; building 1,450.95/60 = 24.2; computers 48.15/3 = 16.1; vehicles 144.64/10 = 14.5; furniture 72.53/10 = 7.3; software 6.12/5 = 1.2; total about 497 lakh a year before CWIP. Add CWIP once capitalised: 685.85/15 + 776.99/15 + 1,258.12/60 + 46.58/10 + 30.44/10 = about 126; total about 623. Q1 FY27 depreciation was 0.80 Cr (Data_Sheet, consolidated) vs about 1.26 Cr a quarter implied by the gross block. The gap is 0.46 Cr a quarter. [INFERENCE] some Kannur assets are not yet depreciating or Q1 is partial. | 🟡 |
| Inventory | Raw materials, consumables, loose tools at lower of cost and NRV (policy 7, p.63). No basis for WIP (2,834.39 lakh, 62.2% of inventory) or finished goods. | Largest asset movement has no stated valuation basis. | 🟡 |
| Capitalisation | Borrowing costs of qualifying assets capitalised; CWIP "Cost includes ... borrowing costs capitalised" (policy 9, p.63) | Amount NOT FOUND. CFS interest paid equals P&L interest (128.24). | 🟡 |
| Impairment | Generic (policy 5, p.62); nil impairment (Note 29.I(3), p.75) | No assumption disclosed. Kannur runs at low utilisation (AR p.4 states 45-50%; production 1,750 MVA vs 9,000 MVA is 19.4%, DERIVED). | 🟡 |
| Provisioning (ECL) | Indian AS: provision for doubtful debts "based on management's assessment of recoverability and ageing" (policy 8, p.63). No ECL matrix. | Nil provision with 588.04 lakh over one year and 84.29 lakh at 6-12 months. | 🟡 |
| Warranty, LD | Not in policy; KAM names both | No provision (Note 12) | 🟡 |
| Bonus | "The Company has not adopted any policy for payment of Bonus and thus no amount has been charged" (policy 11, p.63) | The Payment of Bonus Act applies to factories with 20 or more employees (112 employees, Board p.43). A zero bonus charge is a statutory gap. Amount NOT FOUND, not estimated. | 🟡 |
| Gratuity | Unfunded, PUC method; salary escalation 5.00%, discount 7.10% (Note 24, p.74) | Realised median pay rise 5.44% but average non-managerial rise 24.33% (Annexure VI, p.54). Obligation 31.72 lakh is small. | 🟡 |
| Deferred tax | AS 22 with prudence (policy 12) | DTL 17.87 to 134.93 lakh on depreciation timing (Note 7, p.66). Reasonable. | 🟢 |
| Policy changes | None (Notes 26, 27, p.75) | | 🟢 |
| Ind AS 116 rate | Not applicable (Indian AS 19). Rent 6.46 lakh (33.27 FY25) | Rent fell 80% as Kannur is owned | 🟢 |

### 2B RPT map

| Counterparty | Relationship | Purchases FY26 (FY25) | Sales FY26 (FY25) | Closing balance |
|---|---|---|---|---|
| Danya Electric Company | 90% profit-share firm; MD 7.5%, WTD 2.5% (Notice p.28) | 2,558.08 (1,278.20), +100.1% | 2,459.83 (1,164.89), +111.2% | Payable 662.82 (575.64) |
| Jai Bharath Exchangers ("Jai Bharat" in AOC-2) | Firm where MD and WTD are partners | 153.77 (267.56), -42.5% | 1.12 (110.97) | Receivable 56.60 (8.65); consolidated 85.13 (104.47) |
| Guarantee given, Danya | | | | 1,470.00 (1,470.00) |
| KMP pay (incl. sitting fees) | | 156.98 (131.36), +19.5% | | |
| Loan to Danya by Vee Rajmohan | Consolidated only (p.94) | | | 311.30 (nil) |

All in Rs lakh (Note 30.21, p.73-74; consolidated Note 21, p.93-94; AOC-2, p.47).

| Test | Result |
|---|---|
| Danya sales as % of standalone revenue | 2,459.83 / 19,007.73 = 12.94% |
| Danya purchases as % of standalone purchases | 2,558.08 / 17,210.72 = 14.86% |
| SPEL external revenue growth (ex Danya) | 16,547.90 vs 13,314.94 = +24.3% (DERIVED). Danya flows grew about 100%+. |
| Net settlement | Payable roll: 575.64 + (2,558.08 - 2,459.83) = 673.89 vs reported 662.82 (gap 11.07). The balance behaves like a net account: Rs 50.2 Cr of gross trade settles around a net purchase of Rs 0.98 Cr. No Danya receivable is shown although SPEL sold 2,459.83 to it. |
| Danya's own dependence | Danya buys 2,459.83 from SPEL = 64.4% of its expenditure 3,818.06 and sells 61.3% of its turnover to SPEL (DERIVED). Both legs run through SPEL. |
| Danya margin | PAT 235.01 vs 328.03 lakh (-28.4%) on turnover +47.2%; PBT margin 8.9% vs 17.8% (p.43). SPEL's own EBITDA margin fell 15.7% to 15.1% (DERIVED). Both entities lost margin; no margin transfer from Danya to SPEL is visible. |
| Consolidation identity | Standalone EBITDA 2,865.20 + Danya EBITDA 417.22 = 3,282.42 = consolidated EBITDA (DERIVED). Only revenue and purchases are eliminated. No unrealised profit is eliminated on Danya inventory 1,653.47, although Note 2.2 says it is. |
| Pricing evidence | AOC-2 (p.47): terms "conform to the prevailing market rates". Notice Item 6 (p.30-31): "no unrelated comparable business entities from whom potential bids could be obtained"; valuation report "Not Applicable"; "not been evaluated by any external independent person". Both cannot be fully true. |
| Promoter incentive | Promoters hold 52.07% of SPEL (Note 3) and 10% of Danya. A rupee of profit booked in Danya reaches promoters at 10% + 90% x 52.07% = 56.9% vs 52.07% if booked in SPEL (DERIVED). The gap is 4.8 points. [INFERENCE] direction of incentive only; no evidence of use. |
| Direct promoter take from Danya | Minority share of Danya profit 23.50 lakh (32.80 FY25); loan interest on 311.30 NOT FOUND |
| Guarantees received | Personal guarantees from Vee Rajmohan, K V Pradeep Kumar, Saimathy Soupramanien (independent director), Savita Pradeep, V Rajagopalan on bank loans (Note 6, p.65-66). No guarantee commission paid or received is disclosed. Not in the AS 18 table. |
| Orders from Danya | The "Rs.113.61 Cr orders from KSEB, TNPDCL and Danya Electric Company" (p.6, p.13, p.18) put a related party inside order inflow. The Danya share is NOT FOUND. |

### 2C Contingent liabilities

| Item | Amount (lakh) | % of net worth 11,293.81 | % of PAT 2,044.06 | >25% / >100% flag |
|---|---|---|---|---|
| Guarantee to IndusInd for Danya | 1,470.00 | 13.0% | 71.9% | Not triggered |
| SPEL guarantee on Danya SBI and IndusInd cash credit (consol Note 10) | Amount NOT FOUND; drawn about 67.8 | | | Not in any contingent line |
| Tax, ESI, TDS demands | Nil | | | |
| Capital commitments | "Nil" (Notes 30.1B, 29.I) vs CWIP 2,797.98 and CIF capital imports 105.34 | | | Disclosure doubtful |
| FY27 authority sought, RPT (Item 6) | 12,500 incl. 2,500 guarantee | 110.7% | | >100% (authority, not exposure) |
| FY27 authority sought, s.185 (Item 9) | 7,500 | 66.4% | | >25% |
| FY27 authority sought, s.186 (Item 10) | 12,000 | 106.3% | | >100% |
| Borrowing and charge limit (Items 7, 8) | 50,000 vs 30,000 now | 4.4x net worth | | Gross debt today 4,572.70 |

Danya's drawn bank debt is about 113.29 lakh (ECLGS 45.50 plus cash credit 67.79, DERIVED from consolidated Notes 7 and 10) against a 1,470 lakh guarantee, about 13x. Danya also owes Vee Rajmohan 311.30. Total Danya debt about 424.59 lakh. Sanctioned IndusInd limit NOT FOUND. [INFERENCE] As a partner, SPEL is exposed to Danya's liabilities beyond the guarantee under partnership law; the legal position is PENDING LIVE VERIFICATION and is not a filed fact.

### 2D Receivables

| Metric | FY26 | FY25 | Anchor |
|---|---|---|---|
| Trade receivables (lakh) | 4,521.09 | 4,357.29 | Note 17, p.68-69 |
| Days on revenue | 86.8 | 109.8 | DERIVED |
| Over 6 months | 672.33 = 14.87% | 653.08 = 14.99% | Note 17 |
| Over 1 year | 588.04 = 13.0% | 344.23 = 7.9% | Note 17 |
| Provision | Nil | Nil | |
| Q4 jump | +1,135.32 (+33.5%) vs Dec-25 books 3,385.77 | | Note 30.6 |
| Bank-statement gap | 168.4 to 171.0 each quarter | | Note 30.6 |
| Consolidated over 1 year | 604.72 (344.23) | | consol Note 17 |
| Concentration, unbilled | NOT FOUND | | |
| Jai Bharath | 56.60 standalone; 85.13 consolidated | 8.65; 104.47 | Notes 21 |

The 344.23 bucket of FY25 does not appear in the 2-3 year column of FY26, so it was collected, written off, or re-aged. The 588.04 are all invoices issued before 31-Mar-2025.

### 2E Inventory

| Metric | FY26 | FY25 |
|---|---|---|
| Raw material | 1,606.69 | 620.04 |
| Work in progress | 2,834.39 | 1,475.63 |
| Finished goods | 77.32 | 150.58 |
| Consumables | 37.85 | 7.20 |
| Total | 4,556.25 (+102.2%) | 2,253.46 |
| Days on revenue | 87.5 | 56.8 |
| Consolidated total | 6,209.72 (+96.9%); days 124.8 | 3,154.19; 77.4 |
| Danya inventory (consolidated less standalone) | 1,653.47 (+83.6% vs 900.73); WIP 1,042.76, FG 334.49 | |
| NRV write-down | None disclosed | None |

Ratio hygiene: the standalone inventory turnover 5.58 uses Sales as the numerator (the note says "COGS/ Sales"; 19,007.73 / average 3,404.86 = 5.58, p.76). The consolidated 2.89 uses COGS (13,803.30 / 4,681.96 = 2.95 DERIVED, p.96). The two ratios are not comparable.

### 2F Borrowings and maturity wall

| Lender | Rate | Balance (lakh) | Security | Note |
|---|---|---|---|---|
| ICICI term loan 1 | 9.50% | 3,500.00 (EMI 53.03, 72 months left) | Stock, book debts, mortgage of immovable assets; PG Vee Rajmohan, K V Pradeep Kumar | Rate type, covenants NOT FOUND |
| ICICI term loan 2 | 9.50% | 474.89 (EMI 6.41, 78 months left) | Same plus PG Saimathy Soupramanien (independent director) | |
| Canara | 7.50% | 63.33 (12 months left) | Stock, book debts | Consolidated adds ECLGS 45.50 |
| IndusInd | 8.75% | 10.60 (11 months) | PG of two promoters, Savita Pradeep, V Rajagopalan | |
| HDFC | 8.60% | 40.46 (28 months) | Vehicle | |
| Cash credit | StanChart 8.17% | 483.43 (IndusInd 614.48 and ICICI 65.70 repaid) | Stock, debtors | |
| Total standalone | | 4,572.70 | | FY27 maturities 1,095.48 = 26.8% of term debt |

| Liquidity test | Result |
|---|---|
| Cash 973.79 vs FY27 current maturities 1,095.48 | 0.89x |
| FY26 CFO 2,773.36 / FY27 maturities | 2.53x, before interest |
| Warrant balance due by 27-Feb-2027 | 1,580.57 = 1.44x FY27 maturities, if exercised. Share price Rs 239.45 (Data_Sheet) vs exercise Rs 169. |
| Undrawn facilities | None (Note 25(2)). Cash credit drawn 483.43; sanctioned limit NOT FOUND. |
| Pledge of promoter shares, ICDs given | None disclosed in AR. Pledge status NOT FOUND in AR (SHP, per B02: none). |
| Interest on avg debt | 128.24 / 3,103.27 = 4.13% vs stated 7.50% to 11.50% |
| Authority sought | Borrowing and charge limit 300 Cr to 500 Cr (Items 7, 8, p.22, p.33) vs gross debt Rs 45.7 Cr. No project is named. |

### 2G Deferred tax

DTL 134.93 lakh: 142.91 on depreciation less 7.98 on gratuity (Note 7). Total tax charge 647.81 / PBT 2,691.87 = 24.1% standalone; consolidated 784.10 / 2,851.66 = 27.5% (FY25 27.3%). Standalone PBT includes 211.51 profit share from the firm. Rate is steady. 🟢

### 2H Other

| Item | Finding |
|---|---|
| Exceptional items | None FY24-FY26 (p.12) |
| Goodwill | None; investment in firm 1,267.73 equals Danya capital attributable (AOC-1, p.48) |
| ESOP | None. Warrant potential dilution 4.99% (12.47 / 249.91). |
| Lease obligations | NOT FOUND (no AS 19 note); rent 6.46 lakh |
| Post balance sheet events | No note. Events of 13-Aug-2026 (resignation of Devaraja Iyer Krishna Iyer, appointment of Ramesh C Behera, MD and WTD re-appointment) are in the Notice, not the Notes. The Board's Report of 27-May-2026 still recommends the NED's re-appointment (p.41). |
| Danya capital split | SPEL 1,267.73 lakh (75.7%) and other partners 406.76 (24.3%) of Danya net worth 1,674.49, for 90% vs 10% of profit. Deed NOT FOUND. |

### Phase 2 summary and reconciliation

| Area | Rating |
|---|---|
| Triple-pass verification | 14 of 15 ✓, 1 partial; no numeric discrepancy |
| Policies | 🟡 (building life, WIP basis, bonus, capitalised interest) |
| RPT | 🟡 (loop, no benchmark, guarantees received omitted) |
| Contingent | 🟡 (disclosed 13.0% of net worth; exposure wider) |
| Receivables, inventory, borrowings | 🟡 |

Reconciliation with B02 accounting score 6/10: agreed. This stage adds four items (60-year building life, no bonus policy, Danya unrealised profit with Note 2.2 wording, depreciation run-rate gap in Q1 FY27) but also confirms clean statutory hygiene. The score stays at 6.
Cross-reference with Phase 1 KAMs: KAM 1 (LD, warranty) and KAM 2 (cancelled orders, NRV) name risks that the Notes do not provision or size. That is where the Phase 1 and Phase 2 findings meet.

Phase 2 verdict: 🟡 Watch.
Kill switch assessment: Based on phases so far, a human reviewer would not have reason to stop, because no misstatement is proven and no Note contradicts the audit opinion. The reviewer would have reason to hold the Danya terms and the ICICI schedule as unresolved.

---

## PHASE 3: FINANCIAL STATEMENTS (cash flow, balance sheet, P&L)

### 3A Cash flow

Consolidated Rs Cr, FY24-FY26 (Data_Sheet and AR p.12; FY26 matches AR p.82).

| Item | FY24 | FY25 | FY26 |
|---|---|---|---|
| CFO | -10.73 | 37.69 | 25.90 |
| CFI | -22.16 | -39.42 | -57.13 |
| CFF | 27.40 | 7.47 | 35.17 |
| PAT (attributable) | 14.00 | 18.60 | 20.44 |
| CFO / PAT | -0.77 | 2.03 | 1.27 |
| EBITDA (AR p.12) | 23.3 | 29.1 | 33.3 |
| CFO / EBITDA | -0.46 | 1.30 | 0.78 |
| Capex | NOT FOUND (CFI -22.16 as proxy) | 39.78 | 57.48 |
| FCF (CFO - capex) | NOT FOUND | -2.09 | -31.58 |
| Capex / depreciation | NOT FOUND | 84.6x | 33.0x |
| M&A | None | None | None |
| Closing cash | 0.06 | 5.80 | 9.75 |

Three-year view: CFO sum 52.86 vs PAT sum 53.04 (CFO/PAT 1.00); CFI outflow 118.71. FY24's -10.73 came with receivables of Rs 65.66 Cr on revenue Rs 113.46 Cr (about 211 days, DERIVED), and FY25's strong CFO was largely that receivable release (+20.5 Cr). FY26 CFO fell 31.3% while PAT rose 9.9%.

Sources of FY26 capex, consolidated Rs lakh (p.82): operating profit before working capital 3,138.01; cash tax -847.42; working capital net +299.88 (inventory -3,055.54; receivables -169.43; other current assets -749.81; other non-current -265.71; payables +3,066.68; other current liabilities +1,456.16; provisions +17.53); net debt drawn +3,122.75; warrants +526.86. Pre-working-capital cash after tax 2,290.59 covers 39.9% of capex 5,748.04 (DERIVED). Payables plus customer advances added 4,522.84 lakh, 78.7% of capex (DERIVED).

### 3A-CFO quality checks

| Check | Finding |
|---|---|
| One-time inflators | Customer advances +1,445.75 lakh (264.61 to 1,710.36, 6.5x). Timing money that unwinds on delivery. |
| Payable stretching | Days 102.8 to 126.3 (+23.5). At FY25 days, FY26 payables would be about 4,846.8 vs 5,954.07 actual: stretch 1,107.3 (DERIVED). |
| Normalised CFO (sensitivity, not an estimate) | 2,773.36 - 1,107.3 (stretch) - 1,445.75 (advances) = about 220; if advances are scaled with revenue (+31.3% from 264.61 = 347.4) the excess advance is 1,362.96 and the result is about 303. So CFO net of supplier and customer float is about Rs 2.2-3.0 Cr, 11-15% of PAT. |
| Inventory rundown | None; inventory doubled |
| Interest classification | Interest paid (128.24) sits in financing. CFO before interest is the choice made; with interest in operations CFO would be 2,645.12. |
| Capex creditors | The CFS "fixed assets purchased" 5,746.46 equals accrual additions (3,715.00 + 1,893.45 + 137.01 + 6.12 = 5,751.58, within 5.12). Any unpaid capex stays in payables and so inside CFO. Amount NOT FOUND. |
| Danya effect | Group CFO 2,590.47 is 182.89 lower than standalone 2,773.36. Standalone books 211.51 profit share in operations and a 9.23 reduction in investment in investing (net cash from Danya about 220.74, DERIVED: 1,276.96 + 211.51 - 1,267.73). Danya's inventory rose 752.74. |
| GST input credit | 767.63 (233.21), +534.42 lakh, absorbed cash and sits in other current assets |
| Tax | Advance tax paid in year 136.50 vs charge 530.75 (25.7%); FY25 65.37 vs 524.68 (12.5%) (Notes 19, 12; DERIVED) |

FLAG-CASH confirmed. The deterioration is in the quality of CFO (supplier and customer funded), not in profit.

### 3B Balance sheet walk (standalone Rs lakh, p.60)

| Item | FY26 | FY25 | Change |
|---|---|---|---|
| PPE + intangibles | 8,670.55 | 1,088.53 | 8.0x |
| CWIP + intangibles under development | 2,934.99 | 4,935.83 | -40.5% |
| Investment in Danya | 1,267.73 | 1,276.96 | -0.7% |
| Other non-current | 643.50 | 421.42 | +52.7% |
| Inventory | 4,556.25 | 2,253.46 | +102.2% |
| Receivables | 4,521.09 | 4,357.29 | +3.8% |
| Cash | 973.79 | 578.13 | +68.4% |
| Other current assets | 1,305.79 | 367.47 | 3.6x |
| Total assets | 24,873.69 | 15,279.09 | +62.8% |
| Net worth ex warrants | 11,293.81 | 9,249.76 | +22.1% |
| Warrant money | 526.86 | nil | |
| Borrowings | 4,572.70 | 1,633.84 | 2.8x |
| Payables | 5,954.07 | 3,464.86 | +71.8% |
| Customer advances | 1,710.36 | 264.61 | 6.5x |
| Fixed assets and CWIP / total assets | 46.7% | 39.4% | |
| Net operating working capital (inventory + receivables + other current assets - payables - other current liabilities - provisions) | 2,061.62 (10.8% of revenue) | 2,602.33 (18.0%) | Fell while inventory doubled |

Key ratio table:

| Ratio | Standalone FY26 | Standalone FY25 | Consolidated FY26 | Consolidated FY25 | Basis |
|---|---|---|---|---|---|
| D/E | 0.39 | 0.18 | 0.42 | 0.20 | Notes 34(b), 33(b); consolidated debt includes the 311.30 MD loan |
| Net debt / EBITDA | 1.26x | | 1.23x | | (4,572.70 - 973.79) / 2,865.20; (4,997.30 - 974.55) / 3,282.42 (DERIVED) |
| Current ratio | 1.15 | 1.47 | 1.28 | 1.69 | Notes |
| Quick ratio | 0.69 | | 0.68 | | (current assets - inventory) / current liabilities (DERIVED) |
| Interest cover | 22.0x on interest expense; 12.1x on total finance cost | | 20.4x; 10.4x | | (PBT + interest) / interest (DERIVED) |
| DSCR (company definition) | 2.44x | 10.47x | 2.48x | 8.62x | Notes 34(c), 33(c) |
| ROCE (EBIT = PBT + finance cost; CE = assets - current liabilities) | 19.6% | 25.6% | 20.07% | 27.0% | DERIVED; matches B01 for consolidated |
| ROCE ex CWIP and intangibles under development | | | 24.7% | 50.7% | DERIVED: CE 12,779.60 and 5,638.44 |
| ROE (average net worth ex warrants) | 19.9% | | 19.9% | 22.4% | DERIVED; Note 34(d) shows 17.29% on closing equity incl. warrants |
| Goodwill / net worth | Nil | | Nil | | |

Incremental return: consolidated EBIT +295.04 lakh (+10.3%) on capital employed +5,140.32 lakh (+48.6%) = 5.7%. Kannur ran for about five weeks (commercial from 25-Feb-2026, Board p.46), so the return is untested, not failed.

DuPont, consolidated, average balances:

| | FY26 | FY25 | Change |
|---|---|---|---|
| Net margin (20.44 / 181.64; 18.60 / 148.72) | 11.25% | 12.51% | -10.1% |
| Asset turnover (revenue / average assets 209.61; 139.35) | 0.867 | 1.067 | -18.8% |
| Equity multiplier (average assets / average net worth 102.72; 83.20) | 2.04 | 1.675 | +21.8% |
| ROE | 19.9% | 22.4% | -11.2% |

ROE is leverage-supported. Margin and asset turnover both fell; gearing rose. The operating engine did not improve in FY26.

### 3C P&L walk (consolidated, Rs lakh, p.81, Note 20-28)

| Line | FY26 | FY25 | YoY | % revenue FY26 (FY25) |
|---|---|---|---|---|
| Revenue | 18,164.04 | 14,871.70 | +22.1% | |
| Cost of consumption (purchases - inventory change) | 13,539.56 | 11,175.56 | +21.2% | 74.5% (75.1%) |
| Other direct | 263.74 | 166.48 | +58.4% | 1.45% (1.12%) |
| Employee | 454.29 | 327.03 | +38.9% | 2.50% (2.20%) |
| Other expenses | 624.03 | 377.90 | +65.1% | 3.44% (2.54%) |
| EBITDA ex other income | 3,282.42 | 2,824.73 | +16.2% | 18.07% (18.99%) |
| Depreciation | 174.24 | 47.26 | 3.7x | 0.96% (0.32%) |
| Finance cost | 302.64 | 254.26 | +19.0% | 1.67% (1.71%) |
| Other income | 46.12 | 81.80 | -43.6% | |
| PBT | 2,851.66 | 2,605.00 | +9.5% | 15.70% (17.52%) |
| Tax | 784.10 | 712.17 | +10.1% | |
| PAT | 2,067.56 | 1,892.84 | +9.2% | |
| Minority | 23.50 | 32.80 | | |
| Attributable PAT | 2,044.06 | 1,860.04 | +9.9% | 11.25% (12.51%) |

Gross margin rose 0.6 points (25.5% vs 24.9%); the 0.9-point EBITDA margin fall is employee, direct and other expenses, not depreciation (which sits below EBITDA). The MD&A reason ("depreciation and finance costs") explains PBT, not EBITDA. Depreciation plus finance cost took 175 lakh of the 458 lakh EBITDA gain (38%) (DERIVED).

3C-1 Other income: standalone 233.51 lakh = 8.7% of PBT; 211.51 is Danya profit share (7.9% of PBT). Consolidated 46.12 = 1.6% of PBT. Below the 20% flag.
3C-2 Finance cost composition (consolidated): interest 147.06, bank charges 82.33, interest on statutory dues 73.24. Interest on borrowings is 48.6% of the line.
3C-3 Q1 FY27 mechanism (Data_Sheet quarters, Rs Cr, outside the AR): operating profit 8.81 vs 6.63 (+2.18); depreciation 0.80 vs 0.17 (+0.63); interest 1.30 vs 0.41 (+0.89). Depreciation and interest took 1.52 of the 2.18 EBITDA gain (69.7%, DERIVED). PBT 6.79 vs 6.16 (+10.2%).
3C-4 Standalone vs consolidated EBITDA margin: 15.07% vs 18.07%. Consolidated is higher because 5,017.91 lakh of pass-through intra-group revenue is removed from the denominator while the EBITDA of both entities is added (DERIVED). Revenue before elimination 23,181.95; EBITDA / that = 14.16%. MD&A guidance of 15-18% (p.19) spans both readings.
3C-5 Exceptional items: none across FY24-FY26 (p.12).
3C-6 Tax: standalone 24.1% (22.4% FY25); consolidated 27.5% (27.3%). Danya is taxed at 36.6% of PBT (135.53 + 0.76 / 371.30, p.43).
3C-7 EPS: basic 8.18, diluted 8.15 (gap 0.37%). Full-conversion dilution 4.99%.
3C-8 Quarterly shape (Data_Sheet): Q4 FY26 revenue Rs 70.61 Cr = 38.9% of the year (DERIVED: 181.64 - 35.07 - 40.13 - 35.83), against 41.3% in FY25. Revenue is Q4-loaded.

### Phase 3 summary and cross-reference

| Area | Result |
|---|---|
| Cash flow | FCF negative two years; CFO supplier and customer funded; FLAG-CASH |
| Balance sheet | Gearing 0.39-0.42x; liquidity thin; no undrawn lines |
| P&L | Revenue +22.1%, PAT +9.9%; margin pressure from opex and depreciation |
| Cross-reference to Phase 1-2 | KAM inventory risk is the same item as the 4,556 lakh WIP build that consumed cash; the CWIP ageing error (2.10) sits under the capex line; the Danya inventory and elimination point (2B) sits under the consolidated cash flow |

Phase 3 verdict: 🟡 Watch.
Kill switch assessment: Based on phases so far, a human reviewer would not have reason to stop, because profits are real, tax is paid, and gearing is moderate. The reviewer would have reason to size the position for a cash cycle that depends on suppliers and customers.

---

## PHASE 4: RISK FACTORS AND MD&A

### 4A Disclosed risks (MD&A section 9, p.20; threats p.17)

| Disclosed risk | Real vs boilerplate | Evidence |
|---|---|---|
| CRGO, copper, oil price and availability | Real. Import dependence cited from GTRI (p.17). Mitigation "price variation clauses ... where commercially feasible". Share of order book with price variation NOT FOUND in AR (operator context 80-85%, unanchored). | p.17, p.20 |
| Execution in 200 MVA / 220 kV class | Real, specific (type testing, first-article approvals) but silent that CPRI type tests cover only up to 25 MVA/110 kV (Board p.39) | p.14, p.20 |
| Working capital and receivables | Real. Mitigation cites "reduced receivable days to 94", a year-end figure (2D). | p.20 |
| Customer and geographic concentration | Boilerplate. No customer share, no state split anywhere in the AR. | p.17, p.20 |
| Competition and tender pricing | Partly real (LD exposure named) | p.17 |
| Capacity under-utilisation | Real. Mitigation: order book "weighted towards power transformers". | p.20 |
| Regulatory and efficiency labelling | Boilerplate | p.20 |

Board's Report (p.42): "In the opinion of the Board, there is no such risk, which may threaten the existence of the Company."

### 4B Missing risks (obvious from Phases 1-3, absent from the risk section)

| # | Missing risk | Evidence (anchor) | Likely reason for omission |
|---|---|---|---|
| 1 | Danya loop and credit: rated BB-/A4+, 61.3% of turnover to SPEL, Rs 50.2 Cr gross flows, no benchmark, guarantee 1,470 lakh with authority for 2,500 and 7,500 | Notes 20, 21, 30.1A; Notice Items 6, 9 (p.28-33) | Framed as "synergy" in the RPT notice, so it never reaches the risk table |
| 2 | Financing risk: debt 2.8x, DSCR 2.44x on next-year maturities, no undrawn lines, one lender 97.2%, covenants not disclosed | Notes 6, 9, 25(2), 34(c) | MD&A calls gearing "conservative" (p.19) |
| 3 | Supplier and customer funded working capital that can reverse (payable days 126.3, advances 6.5x) | Notes 10, 11 | The working capital risk row looks only at receivables |
| 4 | Fixed cost step-up: depreciation run-rate about 497 vs 165.26 lakh; Q1 FY27 interest +217%, depreciation +371% (Data_Sheet) | 2A; 3C-3 | The Chairman's letter admits it (p.13) but the risk table omits it |
| 5 | Warrant exercise: 1,580.57 lakh balance due by 27-Feb-2027 | Note 5 (p.65) | Treated as a funding event |
| 6 | Key-person and technical depth: two promoter-directors run operations; 112 staff for 9,000 MVA; the one board member with long transformer-design history (Devaraja Iyer Krishna Iyer, TELK, AREVA, Prime Meiden, p.11) left on 13-Aug-2026 [INFERENCE on impact]; R&D spend nil | Board p.43, p.53; Notice p.25 | Not a recognised risk category in the template |
| 7 | Receivable tail: 588.04 lakh over one year, nil provision, bank-statement gap about 169 lakh every quarter | Notes 17, 30.6 | MD&A leads with "receivable days 94" |
| 8 | Compliance: section 185 timing (1D), no bonus policy, statutory dues interest 55.34, MSMED interest not accrued with payable days 126.3 | Notes 26, 10; policy 11; Item 9 | Seen as routine |
| 9 | Product qualification gap: type test coverage up to 25 MVA/110 kV only | Board p.39 | Positioned as "phased entry" |
| 10 | Interest rate and FX: rate type not stated; capital imports CIF 105.34 lakh | Notes 6, 17 | Small today |

### 4C MD&A deep dive

Industry claims. The sector section (p.16-17) leans on third-party sources (Mordor Intelligence, Kotak Neo, GTRI, CREA, CBRE, InVed, Wood Mackenzie). Growth case: National Electricity Plan transmission outlay above Rs 9.15 lakh Cr to 2032; 1,274 GVA of transformation; Indian transformer market USD 3.25 bn (2026) to 4.82 bn (2031) at 8.2%. SPEL's share and win rate against the plan are NOT FOUND. The stated barrier to entry is qualification, "not capital" (p.17); that sentence is the key to the thesis and sits against the type-test gap in 6E.

Growth and margin explanations (credit and blame):

| Management statement | What the numbers show |
|---|---|
| Revenue +22.1% credited to capacity and demand | Revenue before Kannur was already +22%; Kannur was commercial for about five weeks. SPEL external revenue +24.3%, Danya external +3.8% (DERIVED). |
| Margin compression "structural rather than operational", due to depreciation, finance cost and manpower | EBITDA margin fell on opex lines (2.5 pts of cost growth vs revenue); depreciation is below EBITDA. Danya PBT margin halved (17.8% to 8.9%) with no comment. |
| "Raw material cost as a proportion of revenue was broadly stable" | True: 74.5% vs 75.1% |
| Debtors turnover 3.95 (+47%) from "stronger collections" | Year-end balance +33.5% vs December; over-one-year bucket 588.04 vs 344.23; no provision |
| Inventory 2.89 turns (-33%) from "strategic build" | KAM names cancelled or amended orders; no NRV test shown |
| DSCR 2.48x down 71% | The denominator is year-end next-year maturities, not repayments (2.0) |
| "Funding ... internal accruals and borrowings" (p.19) | Payables plus advances funded 78.7% of capex (3A) |
| "Capacity utilisation 45 to 50%" (p.4) | 1,750 MVA / 9,000 MVA = 19.4% (DERIVED); the basis is not stated |
| Net cash flow positive (p.19) | True (+3.95 Cr) only because financing brought +35.17 Cr |

Segment analysis: one reportable segment. The MD&A heading "Product-wise Performance" (p.18) gives cumulative units only (e.g., power transformers 450+, distribution tail 9,750+ energy efficient). FY26 revenue by product, customer, state or export is NOT FOUND. Order book mix 72% power, 20% distribution, 7-8% inverter duty (p.18) is a stock figure with no revenue bridge.

Forward guidance table:

| Claim | Number | Timeframe | Credibility check |
|---|---|---|---|
| FY27 consolidated revenue | Rs 275-300 Cr (MD&A p.19) | FY27 | LOW to MEDIUM. Needs Q2-Q4 average 75.6 to 83.9 Cr vs the best quarter so far 70.61 Cr (Q4 FY26) and Q1 FY27 48.23 (Data_Sheet, DERIVED). Order book 588.17 Cr is 2.0-2.1x the guide. FY26 guidance cuts (225 > 200 > 190) and the later "250-300" are outside the AR (operator and B00). |
| EBITDA margin | 15-18% (MD&A p.19) | FY27 | MEDIUM. Below the FY26 reported 18.3% (p.19) and spanning the standalone 15.1% and consolidated 18.1% (3C-4). The "18-20%" in operator context conflicts; verify at stage 5. |
| Kannur utilisation | About 90% over 2-3 years (p.14, p.18) | FY28-FY29 | LOW. No interim milestone in the AR. Reported 45-50% vs derived 19.4% (p.4). |
| Peak revenue potential | About Rs 550 Cr (MD&A p.18) | Not stated | LOW. 3.0x FY26 revenue; ramp and qualification both unproven. |
| Order book | Rs 588.17 Cr at 27-May-2026; "more than three times" FY26 revenue (p.13) | Conversion timetable NOT FOUND | MEDIUM. 588.17 / 181.64 = 3.24x (DERIVED). Includes Danya orders (amount NOT FOUND). Dated 57 days after year end. |
| FY28 "further step-up" | Unquantified (p.19) | FY28 | NOT TESTABLE |
| Offset of better realisation by overheads | Qualitative (p.19) | FY27 | MEDIUM. Consistent with Q1 FY27 employee cost 1.92 vs 0.81 Cr (operator context). |
| Capex plan after Kannur | NOT FOUND in AR | | The 500 Cr borrowing and charge limits (Items 7, 8) imply a plan the AR does not describe |

### 4D Tone and credibility (1-5)

| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 3 | Full statutory tables and a candid letter on cost build; but Danya has five labels, the Danya deed, auditor and loan terms are missing, and no customer or product revenue split |
| Consistency | 3 | DSCR 2.44 vs 2.48 (basis differs by entity); utilisation 45-50% vs 19.4%; NED "retires by rotation" (Item 3, Board p.41) vs "resigned" (Notice p.25); "more than three decades" (p.16) vs founded 2005; "Ind AS 108" in an AS filing; guarantee date FY25 vs FY26 |
| Specificity | 4 | Numbers in MD&A and Notes; thin on forward capex and order timing |
| Accountability | 3 | Misses are attributed to "expansion"; the Danya margin halving, the FY26 guidance cuts and the receivable tail are not owned in the AR |
| Capital allocation sense | 3 | Rs 100 Cr Kannur is about 4.9x FY26 attributable PAT (100 / 20.44, DERIVED), funded 54% by debt; ROCE 27% to 20%; capacity 3.6x vs 1,750 MVA produced; no dividend; borrowing limit asked 5x gross debt |

Drafting quality is a separate signal. Published text includes: "These figures ... are to be reconciled with the audited financial statements before publication" (p.19); a Danya contribution table whose "Total Revenue" row (75.27%, 45.25%) is the sum of two other rows (22.98 + 52.29; 19.06 + 26.19) (Board p.43); Secretarial report headed "FOR THE FINANCIAL YEAR ENDED MARCH 31, 2025" (p.49); "her", "Mrs." for a male director (p.34); a Schedule V "reasons for loss" paragraph describing a loss-making growth company (p.36); 112 employees "including contract" (p.43) vs "permanent" (p.54); Annexure VI ratios imply a CFO pay of 8.59 and CS pay of 8.81 lakh vs Note 21's 8.53 and 8.59.

Phase 4 contradictions with Phases 1-3: utilisation vs production (3A, 2A impairment); "internal accruals" vs supplier funding (3A); "conservative gearing" vs ND/EBITDA 1.23x with no undrawn lines; receivable days 94 vs tail.

Phase 4 verdict: 🟡 Watch.
Kill switch assessment: Based on phases so far, a human reviewer would not have reason to stop, because the MD&A is specific and the risks named are real. The reviewer would have reason to treat the risk section as incomplete (10 missing items) and to discount the forward numbers until the Kannur ramp and 220 kV qualification show up in quarterly data.

---

## PHASE 5: CORPORATE GOVERNANCE AND BOARD

### 5A Board composition (31-Mar-2026; p.11, p.15, p.41, p.51)

| Director | Role | On Board since | Tenure | Other directorships | Attendance FY26 |
|---|---|---|---|---|---|
| Vee Rajmohan | Chairman and MD, founder, promoter, 31.51% | 21-Jun-2005 | 21 years | Nil (partner in Danya and Jai Bharath) | 9 of 9 |
| V N Pradeep Kumar (K V Pradeep Kumar) | WTD, promoter, 20.56% | 29-Jun-2023 | 3 years | Nil | 9 of 9 |
| Devaraja Iyer Krishna Iyer | NED, non-independent | 31-Aug-2023 | 3 years | NOT FOUND | 9 of 9; resigned 13-Aug-2026 |
| Saimathy Soupramanien | Independent, Audit Committee chair | 31-Aug-2023 | 3 years | NOT FOUND | 9 of 9 |
| Perumal Ravikumar | Independent, NRC chair | 31-Aug-2023 | 3 years | NOT FOUND | 9 of 9 |
| Ramesh C Behera (from 13-Aug-2026) | Independent (additional), Item 13 | 13-Aug-2026 | New | QMax Test Equipments Ltd (Audit and NRC chair) | n/a |

Flags: independents over 10 years none; attendance below 75% none; seats above 8 none; promoter-group cross-board memberships: none on boards, but two promoter-directors are partners in two firms that trade with the company. Independents are 40% of a five-member Board (2 of 5); after the 13-Aug-2026 changes 3 of 5.

The Notice says Behera holds "Nil" listed directorships (p.37) yet lists him as Audit and NRC chairman of QMax Test Equipments Ltd (p.38). Listing status of that company is PENDING LIVE VERIFICATION.

### 5B Committees

| Committee | Members | Meetings FY26 | Note |
|---|---|---|---|
| Audit | Saimathy S (chair, ID), Ravikumar (ID), Vee Rajmohan (MD) | 4 (22-May-25, 13-Aug-25, 12-Nov-25, 9-Feb-26), all attend | The MD sits on the committee that approved the Danya RPT (9-Feb-2026) where he is a 7.5% partner. Abstention not stated. |
| NRC | Ravikumar (chair), Saimathy S, Devaraja Iyer | 1 (22-May-25) | The NED paid 15.00 lakh in FY26 sits on the committee. One meeting a year. |
| Stakeholders' | Ravikumar, Saimathy S, Devaraja Iyer | 1 (26-Mar-26) | |
| Risk | Vee Rajmohan (chair), two IDs | 2 | The promoter chairs the risk committee |
| CSR | Vee Rajmohan (chair), two IDs | 2 | |

### 5C Compensation

| Person | FY26 lakh | FY25 | Ratio to median | Comment |
|---|---|---|---|---|
| Vee Rajmohan, MD | 60.00 | 60.00 | 22.48x | Flat for FY24-FY26 (Annexure A p.35) |
| K V Pradeep Kumar, WTD | 54.00 | 54.00 | 20.23x | Flat for FY24-FY26 |
| CS (Priyanka Bansal) | 8.59 | 7.62 | 3.30x (Annexure VI) | |
| CFO (T B Nathan) | 8.53 | 6.54 | 3.22x (Annexure VI) | +30.4% per Note 21; +26.47% per Annexure VI |
| Devaraja Iyer (NED) | 15.00 | nil | | Board's Report says only sitting fees (p.41); NED fee nature NOT FOUND |
| Independents | 2.80 each | 1.60 | | Sitting fees |
| Promoter family | R Sribarati 2.46; Tarun Pradeep 2.80 | nil | | New in FY26, 5.26 total |

Total director pay 114.00 = 5.58% of standalone PAT (DERIVED). Median employee pay about 2.67 lakh a year (60.00 / 22.48, DERIVED). CEO-to-median 22.5x, below any usual flag. Average non-managerial pay rise 24.33% vs median 5.44% (p.54).

Proposed new terms from 31-Aug-2026 (p.22, p.34): MD Rs 6.5 to 12.0 lakh a month = 78 to 144 lakh a year (+30% to +140%); WTD Rs 5.85 to 10.0 lakh a month = 70.2 to 120 lakh (+30% to +122%). The top of the range is 264 lakh a year, 2.3x the present 114.00, or 12.9% of FY26 standalone PAT (DERIVED). Flat pay for three years is a positive; the open range is the step. ESOP: none (p.39).

### 5D Shareholding

| Item | AR value | Anchor |
|---|---|---|
| Promoter holding (two named) | 52.07% (Vee 31.51%, Pradeep 20.56%), change 0.00% | Note 3, p.64 |
| Promoter group per SHP | 57.16% | Not in AR (B01, B02) |
| Pledge | NOT FOUND IN AR (B02 from SHP: none) | |
| FII, DII trend | NOT FOUND IN AR | |
| Warrants | 12,47,000 at Rs 169; 25% paid; 75% (Rs 126.75) due within 18 months of 27-Aug-2025 | Note 5, p.65 |
| IPO | 71,80,000 shares at Rs 65 (Dec-2023) | Note 1, p.62 |
| Promoter selling | None in FY26 | |

No promoter selling against the growth narrative. FLAG-PROMOTER-PRELIM is not raised.

### 5E Governance red-flag checklist

| # | Item | Result |
|---|---|---|
| 1 | Whistle-blower complaints | None (CARO xi(c)) |
| 2 | SEBI or exchange action | None (Board p.45) |
| 3 | RPT committee | Audit Committee reviews; interested MD is a member |
| 4 | Auditor fee ratio | Non-audit nil |
| 5 | CSR compliance | Spent 37.00 vs 36.97 lakh; no unspent |
| 6 | Section 143(12) fraud | None |
| 7 | Material subsidiary auditor | Danya's auditor NOT FOUND |
| 8 | Independence of the Audit Committee chair | Saimathy Soupramanien is a personal guarantor on the ICICI loan of 474.89 lakh (Note 6, p.66) while the Board states there is no pecuniary relationship with non-executive directors beyond sitting fees (p.41). A personal guarantee to the company's lender is a financial interest in the company's solvency. [INFERENCE] it weakens the independence reading for the chair of the committee that reviews the Danya RPT. Whether SEBI LODR and the Companies Act independence tests are met is PENDING LIVE VERIFICATION. |
| 9 | Section 185 timing | 1D, red item |
| 10 | Notice contradictions | Item 3 says the NED retires by rotation and does not seek re-appointment; Note 26 says he resigned on 13-Aug-2026; the Board's Report (27-May) recommended his re-appointment |
| 11 | Related lending | MD lent Danya 311.30 lakh; terms NOT FOUND |
| 12 | Board skills | Design depth sat with the departing NED (p.11) |
| 13 | SME governance | Regulations 17-27 do not apply (p.43); only Reg 23 does. Voluntary adoption claimed. |

Phase 5 verdict: 🟡 Watch.
Kill switch assessment: Based on phases so far, a human reviewer would not have reason to stop, because attendance is full, pay is flat, promoter holding is unchanged and nothing is pledged per B02. The reviewer would have reason to ask for the independence analysis of the audit chair, the Danya partnership deed and the section 185 trail.

---

## PHASE 6: CHAIRMAN'S LETTER AND FRONT MATTER (read last)

### 6A Narrative vs reality

| # | Claim (anchor) | Evidence | Verdict |
|---|---|---|---|
| 1 | "The capacity has been built. The growth has started." (p.3) | Capacity: PPE 8,670.55 lakh and CWIP 2,934.99 are real, Kannur commercial from 25-Feb-2026 (Board p.46). Growth: revenue +22.1% was largely pre-Kannur; production 1,750 MVA vs 9,000 MVA installed. | ✅ capacity, ❌ "growth started" as a Kannur effect |
| 2 | Order book Rs 588.17 Cr, "more than three times the revenue" (p.13) | 588.17 / 181.64 = 3.24x. Includes Danya orders (amount NOT FOUND). Dated 27-May-2026. Not an audited figure. | ✅ arithmetic, ⚠ quality |
| 3 | Largest capex "while maintaining positive net cash flow and a conservative gearing level of 0.42 times" (p.13) | Net cash flow +3.95 Cr is true; CFO - capex = -31.58 Cr; financing +35.17 Cr; payables and advances funded 78.7% of capex; D/E includes a 3.11 Cr MD loan | ✅ literal, ❌ substance |
| 4 | "receivable days reducing to 94" (p.13) | 4,684.51 / 18,164.04 x 365 = 94.1 consolidated. Year-end loaded (+33.5% on December), over-one-year bucket 604.72 vs 344.23, nil provision | ✅ number, ❌ as a quality signal |
| 5 | "none of the transformers supplied ... has recorded a field failure" (p.4, p.13) | Not testable in the AR. No warranty provision though the KAM names warranty. Type-test coverage up to 25 MVA/110 kV (Board p.39). | ⚠ unverified |
| 6 | CRISIL upgrade to BBB/Stable, A3+ (p.14) | Stated in Board p.46 and MD&A p.18. Danya's BB-/A4+ sits in the same AR (p.32). | ✅ |
| 7 | "profitability grew at a slower pace than revenue ... depreciation and finance costs" (p.13) | Depreciation and finance cost took 38% of the EBITDA gain; the rest is operating cost lines (3C) | ✅ partly |
| 8 | "strengthened ... governance and internal control framework, including inventory management, plant-level authorisation controls and fixed asset management" (p.14) | CWIP ageing arithmetically impossible; bank-statement variances every quarter; no NRV test despite the KAM | ❌ not evidenced |
| 9 | "supplied in excess of 20,800 transformer units ... over more than three decades" (p.16) | Incorporated 21-Jun-2005; AR p.4 says "2 Decades" | ❌ |

### 6B Strategic priorities (p.14)

Priorities: raise Kannur output, win higher-voltage approvals, deepen utility and EPC ties, widen geography, secure critical raw materials, hold working capital discipline. Specificity: moderate, no targets. Capital allocated: Kannur done; next capex NOT FOUND; borrowing limit asked to 500 Cr. Execution evidence: capacity done, order book stated, qualification NOT FOUND, raw-material sourcing NOT FOUND.

### 6C Metrics showcased vs absent

Showcased: order book, capacity (9,000 MVA), zero field failure, ratings, awards, receivable days 94, gearing 0.42.
Conspicuously absent: revenue by product, customer, state, export; customer concentration; Danya share of orders and revenue; Kannur utilisation basis; type-test status above 25 MVA/110 kV; order delivery timetable; LD and warranty cost; cash conversion; ROCE; FY27 capex; R&D spend (nil, p.53).

### 6D Tone and priority drift vs prior year

NOT FOUND. The FY25 annual report was not supplied to this stage (inputs/other preserved, not consumed). Within this AR the tone moves from "growth has started" (p.3) to "approach optimal utilisation over a two-to-three-year period" (p.14).

### 6E Quiet Abandonment Check

| # | Opening claim (quote, anchor) | Where it should show up | Class | Materiality |
|---|---|---|---|---|
| 1 | "Capacity Created. Growth Unlocked" and "The capacity has been built. The growth has started." (p.3) | Key Facts p.4: "1,750 MVA Actual Production", "45 to 50% Capacity Utilization", against 9,000 MVA installed. Letter p.14: "approach optimal utilisation over a two-to-three-year period". | (c) hedged retreat. The 45-50% and the 19.4% (1,750 / 9,000) cannot both be right; the basis is not stated. | Changes the thesis: the return on the Rs 100 Cr rests on this ramp |
| 2 | "Eligible Transformer Class: Up to 200 MVA / 220 kV" (p.4); "Enables production of transformers up to 200 MVA / 220 kV" (p.9) | Board p.39: "CPRI ... has type tested our transformers upto 25MVA/110kV Voltage Class". MD&A p.20: "phased entry beginning with ratings adjacent to established capability". Letter p.14: capability "cannot be established through manufacturing capacity alone". | (c) hedged retreat. The headline says capability exists; the operational sections say qualification is pending. No type test above 25 MVA/110 kV is disclosed. | Changes the thesis: 72% of the order book is power transformers |
| 3 | Data centres: "Industrial & Data Centre Applications" (p.9); "markets in which the Company already has an established presence" (p.17) | No data-centre order, product, customer or revenue in the Notes, order list (p.6) or segment note | (b) silent drop. Operator context (unanchored): no orders, 165 MVA type test pending. | Optionality only; noise to moderate |
| 4 | MD "actively involved in exploring growth opportunities in international markets" (Notice p.35) | Foreign exchange earnings nil in FY26 vs 103.83 lakh in FY25 (Annexure V p.53; Note 17 p.73). Annexure V calls the FY25 item "consulting service overseas"; Note 17 calls it "Exports of Goods". | (b) silent drop | Low |
| 5 | Product scope includes "repair, refurbishment, erection, commissioning and testing" (KAM, p.55; Board outlook p.39) | Sale of services 754.90 lakh to 78.75 lakh (-89.6%), no comment (Note 20, p.69) | (b) silent drop | Low (0.4% of FY26 revenue vs 5.2%) |
| 6 | MSME Ratna Award "for Electronics Innovation and Engineering Excellence" (Board p.39); "investment in design and testing capability" (MD&A p.20) | R&D expenditure "Nil" (Annexure V p.53); intangibles under development 137.01 lakh of software only (p.67) | (c) hedged retreat | Moderate: 220 kV design depends on external expertise and the senior NED has left |

Phase 6 summary: the opening sections sell capacity and capability; the operational sections hold back on utilisation, type testing and R&D. Two of the six items (1 and 2) change the thesis and both sit on the same proof gate: the Kannur ramp and 220 kV qualification.

Phase 6 verdict: 🟡 Watch.

---

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

Market inputs: price Rs 239.45, market cap Rs 598.41 Cr, 2.499 Cr shares (Data_Sheet). Trailing P/E 598.41 / 20.44 = 29.3x. P/B 598.41 / 112.94 = 5.3x. EV about 638.6 Cr (598.41 + 49.97 - 9.75) and EV/EBITDA 19.5x on 32.83 (all DERIVED). Revenue CAGR FY23-FY26 22.1%; attributable PAT CAGR 23.6% (Data_Sheet, DERIVED).

| Strategy | Call | Top 3 reasons |
|---|---|---|
| Value + Quality | FAIL | 1) 29.3x trailing P/E and 5.3x book for a business growing PAT 9.9%. 2) ROCE 27% to 20% and ROE 19.9% leverage-supported (3B). 3) FCF negative in both years where capex is known. |
| GARP | WATCHLIST | See below |
| Turnaround | FAIL | All four years profitable; no loss-to-profit swing; this is a capacity transition, not a recovery. ROCE is falling, not rebuilding. |
| Capex-Led Growth | PASS (best fit) | 1) Rs 100 Cr Kannur, installed capacity 2,500 to about 9,000 MVA, capability to 220 kV. 2) Order book Rs 588.17 Cr, 3.24x revenue, BBB/Stable. 3) Gearing manageable (ND/EBITDA 1.23x). Proof still open: utilisation and returns on the new capital. |
| Cash Flow Compounder | FAIL | 1) FCF -2.09 then -31.58 Cr. 2) CFO net of supplier and customer float about Rs 2.2-3.0 Cr. 3) Net debt rising, no dividend. |
| Contrarian | FAIL | Price Rs 151.45 at Mar-26 to 239.45 now (+58%, Data_Sheet); 29x earnings; no neglect signal |
| Insider Confidence | WATCHLIST | 1) Promoter holding unchanged (52.07%) and warrants taken (split NOT FOUND in AR). 2) Pay flat three years; MD lent Danya 311.30 lakh. 3) Against it: no open-market buying data, large pay range sought, no pledge data in AR. |
| Guidance Divergence | WATCHLIST | 1) FY27 Rs 275-300 Cr needs Q2-Q4 average 75.6-83.9 Cr vs best quarter 70.61 Cr. 2) FY26 cuts and the later 250-300 are outside the AR (B00, operator). 3) AR margin guide 15-18% sits below the delivered 18.3%, a cautious element. |

GARP, fullest reasoning. For: revenue CAGR 22.1% and attributable PAT CAGR 23.6% over three years; order book 588.17 Cr covers about 2.0-2.1x the FY27 guide; capacity is in place; BBB/Stable; ROCE ex-CWIP 24.7%. Against: FY26 EPS growth 9.9% and Q1 FY27 PAT growth 10.1% on revenue +37.5%; depreciation and interest absorb 69.7% of Q1's EBITDA gain, and the depreciation charge has not yet reached the gross-block run-rate (2A), so the drag can rise; PEG on FY26 growth 29.3 / 9.9 = 3.0 vs 1.2 on the three-year CAGR (DERIVED); the growth quality is partly Danya loop revenue (12.9% of standalone revenue) and supplier-funded working capital. Missing evidence: Q2-Q3 FY27 margin after full depreciation, Kannur utilisation and type-test status. Observation that separates the two readings: whether PAT growth catches up with revenue growth by H2 FY27 without an increase in payable days. Position size, not an adjusted input, carries the caution (CLAUDE.md, A26.3).

Turnaround, fullest reasoning. It does not fit. There is no loss year, no margin trough and no balance-sheet repair in FY23-FY26. Net profit rose every year (10.82, 14.00, 18.60, 20.44 Cr). What looks like a transition is a capacity and product step (50 MVA/132 kV to 200 MVA/220 kV). ROCE fell (28.1% FY24, 27.0% FY25, 20.1% FY26, B01 and 3B), gearing rose, FCF turned negative. If the thesis is a rung climb from distribution supplier to power-transformer supplier, the proof gate is qualification and utilisation, both open (6E-1, 6E-2).

Phase 7 best fit: Capex-Led Growth, with GARP held on WATCHLIST.

---

## PHASE 8: FINAL VERDICT DASHBOARD

### Company snapshot (consolidated unless stated; Rs Cr)

| Item | Value | Anchor |
|---|---|---|
| Business | Power, distribution and inverter-duty transformers; Chennai; two plants | p.4, p.16 |
| Revenue FY26 | 181.64 (+22.1%); standalone 190.08 | p.81; p.38 |
| EBITDA FY26 | 32.82 ex other income (18.07%); standalone 15.07% | DERIVED |
| PAT attributable | 20.44 (+9.9%) | p.81 |
| Net debt | 40.23 (49.97 debt, 9.75 cash) | p.81 |
| Order book | 588.17 at 27-May-2026 | p.13 |
| Capacity | 9,000 MVA; production 1,750 MVA | p.4 |
| Rating | BBB/Stable, A3+ (CRISIL, 20-Mar-2026); Danya BB-/A4+ | p.46, p.32 |
| Price, market cap | Rs 239.45; Rs 598.41 Cr | Data_Sheet |

### Phase-wise verdict summary

| Phase | Verdict | One-line reason |
|---|---|---|
| 1 Auditor and CARO | 🟡 | Clean opinions; section 185 timing item; Danya auditor unknown |
| 2 Notes | 🟡 | 14 of 15 verified; RPT loop, guarantee, ICICI and CWIP do not reconcile |
| 3 Financials | 🟡 | CFO funded by suppliers and customers; FLAG-CASH |
| 4 Risk and MD&A | 🟡 | Specific MD&A but 10 missing risks; forward numbers need the ramp |
| 5 Governance | 🟡 | Full attendance, flat pay; audit chair guarantees company debt; notice contradictions |
| 6 Letter | 🟡 | Capacity claims outrun utilisation and type-test evidence |
| 7 Best fit | Capex-Led Growth | GARP on WATCHLIST |

### Quality score (25% each)

| Component | Score /10 | Basis |
|---|---|---|
| Governance | 5 | Unmodified audit, full attendance, flat pay; but Danya structure, MD on the audit committee, independent director as guarantor, section 185 timing, notice contradictions, drafting errors |
| Accounting quality | 6 | Matches B02 6/10; clean hygiene against 60-year building life, no WIP basis, no bonus, no unrealised-profit elimination |
| Balance sheet | 5 | ND/EBITDA 1.23x and BBB/Stable against 2.8x debt, no undrawn lines, current ratio 1.15, DSCR 2.44x, supplier-funded |
| Earnings quality | 6 | Three-year CFO/PAT 1.00 and ROCE 20% against normalised CFO 11-15% of PAT and a Q4-loaded, Danya-assisted revenue line |
| Overall | 5.5 / 10 | Equal weights |

### Top 3 strengths
1. Real growth and a real backlog: revenue CAGR 22.1% and PAT CAGR 23.6% over FY23-FY26; order book 3.24x FY26 revenue; capacity and 220 kV capability built (p.4, p.13; Data_Sheet).
2. Statutory hygiene: unmodified opinions, no tax disputes, no default, CSR met, no whistle-blower complaints, flat promoter pay for three years (p.55-59, p.35, p.51).
3. Serviceable leverage today: ND/EBITDA 1.23x, interest cover about 20x on interest expense, BBB/Stable with an upgrade in March 2026 (p.81, p.46).

### Top 3 red flags
1. Danya loop: BB-/A4+ firm, 61.3% of its turnover to SPEL, Rs 50.2 Cr gross flows netting to Rs 0.98 Cr, no benchmark, guarantee 1,470 lakh with authority up to 7,500, MD loan 311.30, no unrealised-profit elimination, five labels in one AR (2B, 1F).
2. Cash: CFO 25.90 vs capex 57.48 Cr; payables plus advances funded 78.7% of capex; CFO net of float about Rs 2.2-3.0 Cr; debt 2.8x; no undrawn lines; DSCR 2.44x on next-year maturities (3A, 2F).
3. Returns and governance gaps: depreciation and interest took 69.7% of Q1 FY27's EBITDA gain, depreciation has not reached the gross-block run-rate, ROCE 27% to 20%, utilisation 19.4% to 50% (AR conflict); section 185 retrospective approval, audit-chair guarantee, NED exit (3C-3, 6E, 5E).

### Key monitorables for next quarter

| Metric | Threshold | Where | Why |
|---|---|---|---|
| Q2 FY27 revenue | At least 55 Cr (floor for the 250 guide) and 65 Cr (for 275) if FY27 follows the FY26 shape (H1 share 41.4%) | Q2 results, Nov-2026 | Tests the guide (DERIVED: (35.07 + 40.13) / 181.64 = 41.4%) |
| Share of EBITDA gain absorbed by depreciation and interest | At most 50% (Q1 FY27: 69.7%) | Q2 results | Tests PAT catching revenue |
| Quarterly depreciation | Near 1.26 Cr a quarter (gross-block run-rate); below 0.9 Cr needs an explanation | Q2 results | In-service date of Kannur assets |
| Kannur utilisation and MVA produced | Disclosed with basis; 30% by Q3 (operator context, unanchored) | Q2 call and presentation | Resolves 45-50% vs 19.4% |
| Danya gross trade | At most Rs 50.2 Cr a year (FY26 level), so at most 25.1 Cr per half; the 15.54 Cr to 13-Aug (p.29) is the base | RPT disclosure, H1 results | Loop shrinks or grows |
| SPEL guarantee for Danya | Stay at 14.70 Cr; any move toward 25 Cr is a flag | Reg 30, AGM result | Authority 25 Cr, s.185 75 Cr |
| Customer advances and payable days | Advances 17.10 Cr, payables 59.54 Cr (standalone); advances below about 10 Cr with payables above 59 Cr signals reversal | H1 balance sheet | CFO float |
| Receivables over one year | At most 5.88 Cr (standalone); provision introduced if higher | FY27 AR Note 17 | Tail |
| Warrant exercise | Rs 15.81 Cr balance received by 27-Feb-2027 | Exchange allotment filings | Funding |
| Type-test and qualification news above 25 MVA/110 kV | Any filing | Reg 30, presentation | Thesis gate |
| Section 185 resolution trail | Special resolution date for the Danya guarantee | AGM 25-Sep-2026 outcome; 20th AGM | Compliance |
| DSCR on the company definition | At least 2.0x (FY26 2.44x) | FY27 AR Note 34(c) | Debt service |

### One-line verdict

Capex-led growth with a real order book, held at 5.5 of 10 by a Danya loop, supplier-funded cash flow and a ramp and qualification gate that the AR itself hedges; best fit Capex-Led Growth, GARP on WATCHLIST.

Phase 8 note on the Never rules: no number in this report is an estimate. Derived values show their formula. Missing items are NOT FOUND.

---

## BLOCK

```yaml
stage: B03-ardeep
company: "SUPREMEPWR"
run_date: "2026-10-06"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "COLLECTOR: BSE scrip code not found on the screener page, so announcements/ is empty. This is a collector gap, not evidence that the company files nothing. (Filled by hand from the NSE API: 17 filings Mar-Sep 2026; Oct-2025 to Feb-2026 order intimations not pulled under the operator cap.)"
  - "COLLECTOR: shareholding/ is empty: no source is automated yet. (Filled by hand: NSE SHP XBRL 31-Mar-2026; the Sep-2026 half-year pattern is not yet filed as of 2026-10-06.)"
  - "COLLECTOR: screener export sheets came out EMPTY (formulas with no cached values): screener/INDOTECH/531201/DANISH Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization. ABSENT documents. Data_Sheet CSVs carry FY23-FY26 raw values and are present."
  - "COLLECTOR: no results PDFs (screener has none). (Filled by hand: Q1 FY27 and FY26 audited results from NSE.)"
  - "COLLECTOR: no rating PDF. (Filled by hand: CRISIL full rationale 20-Mar-2026 as text.)"
  - "HIGH: prospectus/ empty. Company listed Dec-2023, within 3 years of run_date. Not pulled: operator 12-document cap 2026-10-06 (inputs/operator-notes.md). Backward baseline runs on FY23-FY26 AR/screener only; promoter and group map from AR and web."
  - "research/ empty (non-anchored; no effect on evidence)."
  - "Peer INDOTECH: no transcripts on screener; peer-concalls cover SHILCHAR (4) and DANISH (2) only."
  - "No Q2 FY27 business update filed as of 2026-10-06 (NSE announcement list checked through 26-Sep-2026)."
  - "Operator document cap: Q3 FY26 transcript (concalls/Concall_Feb_2026) and the shareholding XBRL are over the 12-document cap, kept because stage 5 requires three transcripts and the UA qualifier needs the SHP; flagged for operator ruling."
  - "Results PDFs carry an OCR-quality text layer (e.g. 'R, Lakhs'); read the page before taking a number."
  - "STAGE 3: FY25 annual report not supplied, so Phase 6D tone drift is NOT FOUND; Danya partnership deed, Danya auditor, ICICI covenants and rate type, section 185 resolution trail and customer concentration are NOT FOUND IN DOCUMENT."
flags:
  - {type: FLAG-CASH, reason: "FY26 CFO 2,773.36 lakh (consolidated 2,590.47) vs capex 5,746.46 (5,748.04); payables plus customer advances added 4,522.84 lakh = 78.7% of consolidated capex; CFO net of payable stretch and advance excess about 220-303 lakh (11-15% of PAT, DERIVED sensitivity); FCF -2.09 then -31.58 Cr; no undrawn facilities (Note 25(2))."}
  - {type: FLAG-GATE0, reason: "Carried from B01: history 4 years, classification GOOD downgraded one tier; fragile on the M3 CWIP choice. Not re-scored here."}
  - {type: FLAG-RPT-STRUCTURE, reason: "Danya: BB-/A4+ firm, 61.3% of turnover to SPEL, 5,017.91 lakh gross elimination, no unrealised-profit elimination, guarantee 1,470 lakh with FY27 authority 2,500 and 7,500, MD loan 311.30 lakh, five labels in one AR; AGM Item 9 seeks approval 'for having given' the guarantee (section 185 timing vs CARO iv)."}
phase_verdicts: {p1: "YELLOW", p2: "YELLOW", p3: "YELLOW", p4: "YELLOW", p5: "YELLOW", p6: "YELLOW", p7_best_fit: "Capex-Led Growth (GARP on WATCHLIST)"}
overall_quality: 5.5
quality_components: {governance: 5, accounting: 6, balance_sheet: 5, earnings: 6}
kill_switch_notes:
  - "P1: would not stop (unmodified opinions, no default or fraud); would ask for the section 185 resolution trail on the Danya guarantee."
  - "P2: would not stop (no misstatement proven); hold Danya terms and ICICI schedule as unresolved."
  - "P3: would not stop (profits real, gearing moderate); size for a cash cycle funded by suppliers and customers."
  - "P4: would not stop; treat the risk section as incomplete (10 missing risks) and discount forward numbers until the Kannur ramp and 220 kV qualification show in quarterly data."
  - "P5: would not stop; ask for the independence analysis of the audit chair (personal guarantor on ICICI loan), the Danya deed and the section 185 trail."
triple_pass_verification:
  verified: 14
  discrepancies:
    - {finding_rank: 14, triple_pass_value: "Promoter group 57.16%; 63.9% of warrants from non-promoters; no pledge", ar_value: "Note 3 lists 52.07% (Vee 31.51%, Pradeep 20.56%); warrant allottee split, 57.16% and pledge status not in the AR", note_ref: "Note 3 p.64; Note 5 p.65; SHP outside AR. Not an arithmetic discrepancy: untestable in the AR. Warrant arithmetic 1,580.57 and the 27-Feb-2027 date verified."}
missing_risks:
  - {risk: "Danya loop and credit (BB-/A4+, 61.3% of its turnover to SPEL, no benchmark, guarantee authority to 7,500 lakh)", evidence: "Notes 20, 21, 30.1A; Notice Items 6 and 9 (AR p.28-33); absent from MD&A risk table p.20"}
  - {risk: "Financing risk: debt 2.8x, DSCR 2.44x on next-year maturities, no undrawn lines, ICICI 97.2% of term debt, covenants undisclosed", evidence: "Notes 6, 9, 25(2), 34(c) (p.65-66, p.75-76)"}
  - {risk: "Supplier and customer funded working capital that can reverse (payable days 126.3, advances 6.5x)", evidence: "Notes 10, 11 (p.66-67)"}
  - {risk: "Fixed cost step-up: depreciation run-rate about 497 lakh vs 165.26; Q1 FY27 interest +217%, depreciation +371% (Data_Sheet)", evidence: "Note 13 (p.67), Note 27 (p.70); Chairman letter p.13 admits the cost build"}
  - {risk: "Warrant exercise: 1,580.57 lakh due by 27-Feb-2027", evidence: "Note 5 (p.65); Board p.40"}
  - {risk: "Key-person and technical depth: 112 staff for 9,000 MVA, R&D nil, NED with transformer-design history resigned 13-Aug-2026", evidence: "Board p.43; Annexure V p.53; Notice p.25; Directors profile p.11"}
  - {risk: "Receivable tail 588.04 lakh over one year with nil provision; bank-statement gap about 169 lakh each quarter", evidence: "Notes 17, 30.6 (p.68-72)"}
  - {risk: "Compliance: section 185 timing, no bonus policy, interest on statutory dues 55.34 lakh, MSMED interest not accrued at 126.3 payable days", evidence: "Notice Item 9 p.22; policy 11 p.63; Notes 26, 10"}
  - {risk: "Product qualification gap: type tests cover up to 25 MVA/110 kV only", evidence: "Board's Report p.39; MD&A p.17, p.20"}
  - {risk: "Interest rate type and FX on capital imports (CIF 105.34 lakh) not disclosed", evidence: "Notes 6, 17 (p.65-66, p.73)"}
guidance_table:
  - {claim: "FY27 consolidated revenue", number: "Rs 275-300 Cr (MD&A p.19)", timeframe: "FY27", credibility: "LOW-MEDIUM: needs Q2-Q4 average 75.6-83.9 Cr vs best quarter 70.61 Cr; order book 588.17 Cr is 2.0-2.1x the guide; FY26 guide cuts 225>200>190 and later 250-300 are outside the AR (B00, operator)"}
  - {claim: "EBITDA margin", number: "15-18% (MD&A p.19)", timeframe: "FY27", credibility: "MEDIUM: below FY26 reported 18.3%; spans standalone 15.1% and consolidated 18.1%; operator-context 18-20% conflicts and needs stage 5 check"}
  - {claim: "Kannur optimal utilisation", number: "about 90% (MD&A p.18; letter p.14)", timeframe: "2-3 years", credibility: "LOW: no interim milestone; AR says 45-50% utilisation (p.4) vs 1,750/9,000 MVA = 19.4%"}
  - {claim: "Peak revenue potential", number: "about Rs 550 Cr (MD&A p.18)", timeframe: "NOT STATED", credibility: "LOW: 3.0x FY26 revenue; ramp and 220 kV qualification unproven"}
  - {claim: "Order book conversion", number: "Rs 588.17 Cr at 27-May-2026, 3.24x FY26 revenue (p.13)", timeframe: "NOT STATED in AR", credibility: "MEDIUM: includes Danya orders (amount NOT FOUND); dated after year end"}
  - {claim: "FY28 further step-up", number: "unquantified (MD&A p.19)", timeframe: "FY28", credibility: "NOT TESTABLE"}
  - {claim: "Capex after Kannur", number: "NOT FOUND; borrowing and charge limit asked 300 Cr to 500 Cr (Items 7, 8)", timeframe: "NOT STATED", credibility: "NOT TESTABLE: limit is 10x gross debt, no project named"}
monitorables:
  - {metric: "Q2 FY27 consolidated revenue", threshold: "at least 55 Cr (floor for 250 guide) and 65 Cr (for 275) if FY27 follows FY26 shape (H1 share 41.4%)", where: "Q2 FY27 results, Nov-2026", why: "Tests the FY27 guide"}
  - {metric: "Share of EBITDA gain absorbed by depreciation plus interest", threshold: "at most 50% (Q1 FY27 was 69.7%)", where: "Q2 FY27 results", why: "Tests PAT growth catching revenue growth"}
  - {metric: "Quarterly depreciation", threshold: "near 1.26 Cr (gross-block run-rate); below 0.9 Cr needs explanation", where: "Q2 FY27 results", why: "In-service date and depreciation of Kannur assets"}
  - {metric: "Kannur utilisation and MVA produced", threshold: "disclosed with basis; 30% by Q3 (operator context, unanchored)", where: "Q2 call and presentation", why: "Resolves 45-50% vs 19.4%"}
  - {metric: "Danya gross trade with SPEL", threshold: "at most Rs 50.2 Cr a year (FY26 level), 25.1 Cr per half", where: "RPT disclosure, H1 results", why: "Loop shrinks or grows"}
  - {metric: "SPEL guarantee for Danya", threshold: "stay at 14.70 Cr; move toward 25 Cr is a flag", where: "Reg 30 filings, AGM result", why: "Authority sought 25 Cr, s.185 75 Cr"}
  - {metric: "Customer advances and payable days (standalone)", threshold: "advances 17.10 Cr, payables 59.54 Cr; advances below about 10 Cr with payables above 59 Cr signals reversal", where: "H1 FY27 balance sheet", why: "CFO float"}
  - {metric: "Receivables over one year (standalone)", threshold: "at most 5.88 Cr; provision introduced if higher", where: "FY27 AR Note 17", why: "Collection tail"}
  - {metric: "Warrant exercise", threshold: "Rs 15.81 Cr balance received by 27-Feb-2027", where: "Exchange allotment filings", why: "Funding of capex and debt service"}
  - {metric: "Type-test or qualification news above 25 MVA/110 kV", threshold: "any filing", where: "Reg 30 filings, presentation", why: "Thesis gate for 72% power-transformer order book"}
  - {metric: "Section 185 resolution date for the Danya guarantee", threshold: "special resolution dated before 28-Mar-2025", where: "20th AGM (19-Sep-2025) and 21st AGM (25-Sep-2026) results", why: "Compliance timing vs CARO iv"}
  - {metric: "DSCR on company definition", threshold: "at least 2.0x (FY26 2.44x)", where: "FY27 AR Note 34(c)", why: "Debt service"}
ar_new_downstream_entities:
  - {name: "Siemens Gamesa Renewable Power Private Limited", where_in_ar: "Marquee clients testimonial, p.8 (inverter duty transformers for solar projects); first-time status NOT VERIFIABLE, FY25 AR not read", entity_type: "customer (named platform)"}
  - {name: "PSG & Sons Charities (Metallurgy & Foundry Division)", where_in_ar: "Marquee clients testimonial, p.8; first-time status NOT VERIFIABLE", entity_type: "customer"}
  - {name: "Kerala State Electricity Board / TNPDCL / TANGEDCO / KPTCL", where_in_ar: "Orders Rs 113.61 Cr (KSEB, TNPDCL, Danya) p.6, p.13, p.18; empanelment p.14, p.18", entity_type: "utility customers"}
  - {name: "Unnamed Navratna PSE (Rs 60.90 Cr inverter duty order)", where_in_ar: "p.6, p.13, p.18", entity_type: "customer, name NOT FOUND"}
  - {name: "Danya Electric Company", where_in_ar: "Notice Item 6 p.21, p.28-33; Notes 20, 21; AOC-1 p.48; AOC-2 p.47; also an order counterparty p.6", entity_type: "RPT counterparty, 90% profit-share firm, BB-/A4+"}
  - {name: "Jai Bharath Exchangers", where_in_ar: "Note 21 p.73-74; AOC-2 p.47 (as Jai Bharat Exchangers)", entity_type: "RPT counterparty, firm where MD and WTD are partners"}
  - {name: "Savita Pradeep; V Rajagopalan", where_in_ar: "Note 6 p.66 (personal guarantors on IndusInd loan)", entity_type: "guarantors, related persons not in the AS 18 table"}
  - {name: "QMax Test Equipments Ltd", where_in_ar: "Notice Annexure A p.37-38 (new independent director Ramesh C Behera chairs Audit and NRC)", entity_type: "other board seat; listing status PENDING LIVE VERIFICATION"}
strengths_top3:
  - "Real growth and backlog: revenue CAGR 22.1% and PAT CAGR 23.6% FY23-FY26 (Data_Sheet); order book Rs 588.17 Cr = 3.24x FY26 revenue; 9,000 MVA / 220 kV capability built (AR p.4, p.13)"
  - "Statutory hygiene: unmodified opinions, no tax disputes, no default, CSR met, no whistle-blower complaints, promoter pay flat three years (AR p.35, p.51, p.55-59)"
  - "Serviceable leverage today: ND/EBITDA 1.23x, interest cover about 20x on interest expense, CRISIL BBB/Stable upgrade 20-Mar-2026 (AR p.46, p.81)"
red_flags_top3:
  - "Danya loop: BB-/A4+ firm, 61.3% of its turnover to SPEL, Rs 50.2 Cr gross flows netting to Rs 0.98 Cr, no benchmark, guarantee 1,470 lakh with authority up to 7,500, MD loan 311.30 lakh, no unrealised-profit elimination, five labels in one AR"
  - "Cash: CFO 25.90 vs capex 57.48 Cr; payables plus advances funded 78.7% of capex; CFO net of float about Rs 2.2-3.0 Cr; debt 2.8x; no undrawn lines; DSCR 2.44x on next-year maturities"
  - "Returns and governance: depreciation and interest took 69.7% of Q1 FY27 EBITDA gain; ROCE 27% to 20%; utilisation 19.4% vs 45-50% stated; section 185 retrospective approval; audit-chair guarantees company debt; NED exit"
best_fit_strategy: "Capex-Led Growth (GARP on WATCHLIST)"
one_line_verdict: "Capex-led growth with a real order book, held at 5.5 of 10 by a Danya loop, supplier-funded cash flow and a Kannur ramp and 220 kV qualification gate that the AR itself hedges."
analyst_note: "Three AR-only findings a later stage cannot rebuild from the fields. (1) Gross SPEL-Danya trade of Rs 50.2 Cr nets to Rs 0.98 Cr; consolidated EBITDA equals standalone plus Danya EBITDA exactly, so no unrealised profit is removed, and the 18.1% consolidated margin vs 15.1% standalone is a denominator effect from removing pass-through revenue. (2) Utilisation: AR p.4 states 45-50% but 1,750 MVA produced vs 9,000 MVA installed is 19.4%; headline capacity claims depend on the basis. (3) AGM Item 9 asks approval for guarantees already given to a firm where the MD and WTD are partners; CARO iv says sections 185 and 186 were complied with. Stage 2 page anchors run marker+1 vs this report. Q1 FY27 and market data come from the Data_Sheet, not the AR."
```
