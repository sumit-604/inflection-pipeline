# STAGE 3: ANNUAL REPORT DEEP DIVE (BACKWARD READ): JLHL, run 2026-11-12

Primary document: inputs/annual-report/Annual_Report_2026.pdf (FY2025-26, 237 pages). Anchor format: (AR26 p.N) where N is the PDF page marker in the .txt file; the printed page number is N minus 3. Baseline documents: Annual_Report_2025.pdf (AR25), Red_Herring_Prospectus_30Aug2023.pdf (RHP, 444 pages, grep only). Cross-checks outside the AR are labelled "secondary" and carry their own unit.

UNIT RULE. AR26, AR25, RHP financial statements and the results filings: INR million (Rs mn; 10 mn = 1 Crore). Investor presentations, the ICRA rationale and the screener sheet: INR Crore (Rs Cr). No figure is converted silently; every figure shows its unit. S = Standalone, C = Consolidated. "Derived" = arithmetic on anchored inputs, not a filed number.

BASIS RULES.
- FY25 base. AR26 re-cut the FY25 comparatives. FY25 C revenue is Rs mn 13,024.02 (AR26 p.192) vs Rs mn 12,615.45 as filed (AR25 p.85). Every FY25 figure below is on the AR26 re-cut base unless marked "AR25 as filed". Section 3C explains the re-cut exactly.
- Per share. AR26 per-share figures are on face value Rs 10, 6,55,66,022 shares (AR26 p.143). The stock split approved 15-May-2026 is NOT FOUND IN DOCUMENT in AR26 (grep: no "split" or "sub-division"). The Q2 FY27 presentation restates FY26 basic EPS to Rs 5.92 (29.59 / 5), so the split is 5 for 1, face value Rs 2 (secondary: Investor_Presentation_Q2FY27 p.8, Rs Cr). The B00 CMP of Rs 287 is on the post-split basis (market cap Rs Cr 9,391 / 287 = 32.7 crore shares).
- B00 input_gaps are carried in the block. None of them touches AR page-level evidence. Two scanned announcements are not used.

---------------------------------------------------------------------
## 0. LOAD-BEARING FACTS, CHECKED FIRST

| # | Fact (COMPANY MEMORY) | Result against filings | Anchor |
|---|---|---|---|
| 1 | Dombivli ramp: EBITDA loss Rs 9.5 Cr (Q1 FY27) to Rs 0.2 Cr (Q2 FY27); commencement January 2026 | Loss figures CONFIRMED (Rs Cr): Q1 FY27 9.5, Q2 FY27 0.2, H1 9.7 (Q2 FY27 presentation p.5, p.8). The date needs a correction. The 30-Jan-2026 filing announces completion; the hospital began 200 beds after inauguration on 15-Feb-2026; "full clinical operations" 25-Feb-2026. So operations started about 6 weeks later than "January 2026". Q4 FY26 already carried a Rs Cr 9.4 Dombivli loss in 5 weeks of operation (Q4 FY26 presentation p.7). | AR26 p.12; inputs/announcements/20260130-Dombivli_Commencement.txt; Q4 FY26 presentation p.4, p.7 |
| 2 | Profit squeeze: PAT flat near Rs 194 Cr; depreciation and interest up; did the mature-hospital margin hold? | CONFIRMED and now split. PAT Rs mn 1,941.87 vs 1,937.54 (+0.2%) (AR26 p.192). Mature margin HELD (derived, secondary): FY26 EBITDA ex-Dombivli = Rs Cr (343.3 + 9.4) = 352.7 on total income 1,499.8 = 23.5% vs 23.0% in FY25; Q4 FY26 ex-Dombivli at least 25.4% (98.6 / 387.8) vs 23.6% in Q4 FY25. The squeeze sits below EBITDA. See section 3C bridge: D&A +305.57 (41% is leasehold-land ROU amortisation, not Dombivli), finance cost +219.57 (84% is one JHPPL loan drawn in FY25), both Rs mn. | AR26 p.192, S Note 1.2 p.156, C Notes 30-31 p.219; Q4 FY26 presentation p.7 |
| 3 | Capex funding and debt: nil (Mar 2024) to Rs mn 5,085 (Mar 2026); Pune South, Mira Road, BKC | Debt CONFIRMED: C gross borrowings Rs mn 5,085.27 = 5,008.97 + 76.30 (AR26 p.191); Mar 2024 nil is B01 and the brief; AR25 Mar 2025 was 3,257.13. Capex: ICRA plan Rs Cr 1,200-1,250 for FY26-FY29, of which Dombivli about 425 done and Rs Cr 890-900 earmarked FY27-FY29 for Pune, Mira Road and Dombivli phase II (ICRA 10-Mar-2026 p.2, p.3). That plan EXCLUDES the BKC lease premium of about Rs Cr 354 (filing of 27-Mar-2026) and the Pune South land purchase Rs Cr 150 (incremental Rs Cr 100, Q2 FY27 presentation p.4). Capital commitments: NOT FOUND IN DOCUMENT in AR26. Internal-accruals claim (AR26 p.22): FY26 C CFO 2,677.08 covered 53% of C capex 5,018.45; FY25+FY26 together 64% (derived). | AR26 p.191, p.193; ICRA p.2-4; MMRDA filing 27-Mar-2026 |
| 4 | Occupancy and ARPOB definitions, hospital-wise split | Definitions NOT FOUND IN DOCUMENT in AR26 (only the numbers, AR26 p.20, p.46). Definitions sit in the presentations and RHP: occupancy = census occupied bed days / census bed days; ARPOB = income from hospital services / census occupied bed days; the FY26 ARPOB excludes unbilled revenue and doctors' provision (Q4 FY26 presentation p.6 footnote; RHP p.128). Hospital-wise split: AR25 gave it (Thane 72.1%, Pune 65.5%, Indore 54.9%; AR25 p.5). AR26 gives none. See Phase 6E. | AR26 p.20, p.46; AR25 p.5 |

---------------------------------------------------------------------
## PHASE 1: AUDITOR'S REPORT AND CARO (read first, back to front)

### 1A Core opinion
| Item | Finding | Anchor |
|---|---|---|
| Opinion type | Unmodified on S and C. True and fair view under Ind AS. | AR26 p.128 para 2; p.183 para 2 |
| Auditors | Joint: KKC & Associates LLP (formerly Khimji Kunverji; partner Hasmukh B Dedhia, M.No. 033494, FRN 105146W/W100621) and Aswin P. Malde & Co. (proprietor Aswin P Malde, M.No. 032662, FRN 100725W). Both signed 15-May-2026. | AR26 p.132 |
| Going concern language | Standard responsibility paragraphs only (paras 10, 12.4). No material-uncertainty paragraph. CARO xix: nothing suggests the company cannot meet liabilities falling due within one year. Basis-of-preparation line "prepared on going concern basis under historical cost". | AR26 p.129-130; p.136; S Note 1B(ii) p.144 |
| Exception inside a clean opinion | Section 143(3)(b) books-of-account paragraph carries an exception (paras 19.2, 19.6, 20.8): HMIS billing software had no database-level audit trail (edits from the backend); another system could not show backup logs. Para 19.6 itself uses the word "modification". Consolidated: HMIS gap in the Parent and 1 subsidiary; backup-log gap in the Parent and 2 subsidiaries (para 22.8). The Directors' Report says the auditors made no "qualifications, reservations, or adverse remarks". Both statements stand side by side. | AR26 p.131-132; p.188; p.90 |

### 1B Key Audit Matters
| KAM | Why key | How addressed | Risk |
|---|---|---|---|
| Receivables, reconciliation and provisioning (S and C) | TPA, insurer, corporate and government payers; claim adjudication, contractual deductions; ECL judgement "including management overlays for known adverse factors" | Control testing on billing, claim submission, sub-ledger to GL reconciliation, ageing, credit notes, write-offs, manual journals; substantive tests on patient files and TPA authorisations; review of ECL method | [YELLOW] |
| Absent KAMs worth naming | No KAM on revenue recognition or unbilled revenue (new Rs mn 191.07), none on capitalisation of Dombivli (Rs mn 3,881.3), none on the HMIS audit-trail gap | n/a | [YELLOW] |
Cross-reference: the KAM mentions "management overlays" but no overlay amount appears in Note 7. Allowance equals the credit-impaired bucket only (C Rs mn 36.83 on gross 792.22, AR26 p.212). Receivables gross +72.3% vs revenue +15.2%.

### 1C Emphasis of Matter and Other Matters
| Item | Detail | Anchor |
|---|---|---|
| Emphasis of Matter | None | AR26 p.128-131 |
| Predecessor | FY25 S and C audited by Aswin P. Malde & Co. alone (reports 09-May-2025, unmodified) | AR26 p.130, p.186 paras 16, 19 |
| Unaudited component (S) | 1 partnership firm, share of loss Rs mn 2.62, on unaudited accounts, "not material" | AR26 p.130-131 para 17 |
| Other auditors (C) | 2 subsidiaries (total assets Rs mn 134.86, revenue 396.68) audited by Aswin P. Malde; 1 subsidiary (total assets 3,344.27, revenue 2,499.08; this is JHPPL, auditor Shah Valera & Associates LLP) audited by another auditor; 1 unaudited partnership firm (revenue 129.77, loss 2.76) | AR26 p.186 paras 17-18; p.109 |
JHPPL revenue Rs mn 2,499.08 is 16.7% of C revenue 14,997.87 (derived), audited by a firm other than the two joint auditors.

### 1D CARO 2020, clause by clause (S report, Annexure A)
| Clause | Result | Anchor |
|---|---|---|
| i PPE, title | Clean; no revaluation | AR26 p.133 |
| ii inventory | Discrepancies under 10%; working-capital limits over Rs 5 crore secured on current assets; no quarterly returns required (per management) | p.133 |
| iii loans, guarantees | During year: guarantee Rs mn 2,500.00 and loans 120.00 to subsidiaries. Outstanding: guarantee 2,500.00, loans 322.21. All loans repayable on demand, no schedule, no interest rate stated (NOT FOUND). | p.133-134 |
| vii disputed dues | Service tax Rs mn 4.42, Apr 2019 to Mar 2024, CESTAT Mumbai. Parent only. (C adds Indore property tax 13.04.) | p.134 |
| ix defaults | None; term-loan use as intended | p.134-135 |
| xi fraud | None; no whistle-blower complaints received in the year | p.135 |
| xiii RPT | Sections 177 and 188 complied | p.135 |
| xvii cash losses | None | p.135 |
| xix liquidity | No material uncertainty | p.135-136 |
| xx unspent CSR | None | p.136 |
Consolidated para 23: no qualifications or adverse remarks in any group CARO report (AR26 p.188).

### 1E Auditor continuity and fees
| Item | Finding | Anchor |
|---|---|---|
| Firms and tenure | Aswin P. Malde & Co.: appointed at the 20th AGM for 5 years, to the 25th AGM; start year NOT FOUND. KKC & Associates LLP: joint auditor from the 23rd AGM (11-Jul-2025) to the 28th AGM. | AR26 p.89 |
| Audit fees | S Rs mn 5.40 + 0.30 out-of-pocket = 5.70 (FY25 3.00): audit fee +80%. C 6.40 + 0.30 = 6.70 (FY25 4.00). | S Note 33 p.168; C Note 32 p.220 |
| Non-audit | Total fees for all services to statutory auditors on a consolidated basis Rs mn 6.70, equal to C audit fee plus out-of-pocket. So non-audit fees are nil (derived). Ratio non-audit : audit = 0. | AR26 p.109 |
| Rotation | The joint-audit entry of KKC is the first auditor change shown since the AR25 baseline; the proprietor firm remains. | AR26 p.89 |

### 1F Standalone vs consolidated
Consolidated adds reliance on other auditors for 3 subsidiaries (IFC report para 9, AR26 p.190), extends the audit-trail exception to 1 subsidiary and the backup-log exception to 2 subsidiaries, and carries one more disputed item (Indore property tax Rs mn 13.04, subsidiary has paid 12.37 under dispute, C Note 36B p.223).

Phase 1 verdict: [YELLOW]. Clean opinion and clean CARO. Two watch items: the HMIS audit-trail exception (the revenue source system) and the new joint-audit arrangement.
Kill switch (informational): Based on phases so far, a human reviewer would not have reason to stop, because there is no qualification, default, fraud or going-concern language; the audit-trail exception needs a named fix date.

---------------------------------------------------------------------
## PHASE 2: NOTES TO FINANCIAL STATEMENTS

### Verification of the B02 Top 15 (unit Rs mn unless marked)
| Rank | B02 claim | Check against AR26 | Result |
|---|---|---|---|
| 1 | Parent term-loan interest expensed 15.15; loan 750.00 to 2,610.32; Dombivli capitalised 3,881.3; capitalised interest unquantified | S Note 31 p.167 (15.15); S Note 37H p.176 (gross debt 2,610.32 vs 750.00); S Note 1.1 p.156 (3,881.3). 15.15 / (2,610.32 x 7.61% / 12) = 0.92 month. No capitalised-interest figure anywhere. | verified |
| 2 | No capital commitments; capital advances S 1,169.36 vs 3.69; three projects named; BKC price absent | S Note 4 p.158; S Note 1A p.144; Note 37B p.171 has contingents only. Grep for "commitment" finds no capital-commitment figure. The BKC premium is in a Reg 30 filing (Rs Cr 354, 27-Mar-2026), not in the AR. | verified |
| 3 | FY25 re-cut: C revenue +408.57 (+3.2%), PBT +29.75, PAT +2.54, assets +308.61; ~3,980 cash to investments | C revenue 13,024.02 (AR26 p.192) vs 12,615.45 (AR25 p.85); PBT 2,606.76 vs 2,577.01; PAT 1,937.54 vs 1,935.00; assets 19,357.50 vs 19,048.89; S cash 845.39 vs 3,674.10 (AR25). Numbers verified. The CAUSE is traceable and B02 left it open: see 3C. | verified, cause resolved |
| 4 | HMIS audit-trail gap | Auditor paras 19.2, 19.6, 20.8 (p.131-132); S Note 37Q p.182 | verified |
| 5 | Receivables +72.3%; unbilled 191.07; days 12.1 to 18.4; impaired <6m 5.2x | C gross 792.22 vs 459.67 (+72.3%); unbilled 191.07 = 24.1% of gross; 755.39/14,997.87 x 365 = 18.4; 432.33/13,024.02 x 365 = 12.1; 7.02 vs 1.36 = 5.2x (C Note 7 p.212) | verified |
| 6 | Debt 5,085.27 floating Repo + 200 bps; 92.5% after year 3; net cash 353.45 "vs 2,763.67" | 5,008.97 + 76.30 = 5,085.27 (p.191, p.215); >3 years 4,701.77 / 5,085.27 = 92.5% (p.222); liquid 5,438.72 - 5,085.27 = 353.45. The comparison figure 2,763.67 cannot be reproduced from any statement; the AR's own adjusted net debt (cash and bank only) is 4,503.59 (C Note 36H p.229). Covenants: NOT FOUND. | discrepancy (minor) |
| 7 | 89.3% of liquid assets is one issuer's CP | CP JM Financials Services Rs mn 4,857.04 / (4,857.04 + 547.61 + 34.07) = 89.3% (C Note 6 p.211). Credit-risk text says "bank deposits" (C Note 35 p.221) | verified |
| 8 | JHPPL loss 34.29; cost 939.00 vs net assets 242.60; loan 293.37; guarantee 2,500 | C Note 36D p.226 (loss 34.29, net assets 242.60); S Note 2 p.158 (939.00); S Note 37K p.180 (loan 293.37); S Note 37B p.172 guarantee outside the contingent table. AOC-1 shows JHPPL reserves (557.40), PBT (45.70) (AR26 p.116). | verified |
| 9 | Doctor fees 24.27% (23.44%); inventory days 48.7 (37.8); patient food +106%; other income 16.3% of PBT; pre-OI profit -4.0% | 3,640.29 / 14,997.87 = 24.27%; 3,052.82 / 13,024.02 = 23.44%; 383.36 / 2,872.68 x 365 = 48.7; 118.22 vs 57.18 = +106.7%; 423.68 / 2,604.36 = 16.3%; (2,653.23 - 423.68) vs (2,606.76 - 283.47) = -4.0% | verified |
| 10 | Leasehold-land ROU addition 221.41, no lease liability | S Note 1.2 p.156 (221.41). Lease liability additions FY26 169.93 track building and plant ROU additions (154.31 + 18.17 = 172.48); the land addition carries no liability (S Note 37J p.177) | verified |
| 11 | Payables +38.3%; MSME +188%; MSME past due 69.90; nil MSMED interest | 955.39 / 690.98; 303.75 / 105.48; MSME "less than 1 year" bucket 69.90 (C Note 20 p.217); S Note 37E p.175 shows nil interest | verified |
| 12 | Subsidiary revenue +24.7% vs parent +13.0% | (14,997.87 - 11,976.24) = 3,021.63 vs (13,024.02 - 10,600.65) = 2,423.37 = +24.7%; S 11,976.24 / 10,600.65 = +13.0% | verified |
| 13 | Promoter pay S +25.0%; Dr. Ankit S 39.00 vs 25.92 and C 31.91; Anshul Sethi not in any related-party list; RPT 1.15% | (41.99 + 39.00) / (38.88 + 25.92) = +24.98%; C Note 36K p.232 shows Ankit FY25 31.91; Anshul Sethi Rs mn 3.06 and Rajendra Thakkar 3.38 appear as professional-fee payees but not in the 36K(i) list; RPT total 172.30 / 14,997.87 = 1.15% | verified |
| 14 | Joint auditors from FY26; audit fee +80%; firm loss 2.62 unaudited | p.89, p.168, p.130-131 | verified |
| 15 | Gratuity assets gross; Labour Codes 48.87 vs past service cost 37.52; leave encashment liability NOT FOUND | S Note 4 shows "Gratuity Fund Plan Asset 86.82" though S Note 37C says "unfunded"; C Note 36A p.222 (48.87) vs C Note 36C p.223 (37.52); gap 11.35 | verified |

Verified 14 of 15. Rank 6 carries a minor discrepancy (2,763.67 not reproducible). Rank 3 numbers verify; its explanation is resolved in 3C and changes the reading B02 gave ("base choice drives every trend").

### 2A Accounting policy aggressiveness
| Area | Finding | Anchor | Read |
|---|---|---|---|
| Revenue | Point-in-time; unbilled revenue for undischarged inpatients now recorded (C Rs mn 191.07, FY25 nil). Pharmacy now gross (see 3C). | S Note 1C(7) p.146-147 | [YELLOW] |
| Depreciation lives | Buildings 60 yrs; plant 15; medical equipment 3-10 (Schedule II 13); wind 22 | S Note 1C(2) p.145 | [GREEN] shorter than Schedule II for equipment |
| Capitalisation of interest | Policy exists (policy 4). Amount NOT FOUND for FY26 or FY25. Dombivli Rs mn 3,881.3 capitalised in the year. | S Note 1C(4) p.145-146 | [RED] opacity |
| ROU leasehold land | Amortisation Rs mn 101.17 (S) and lease interest charged to P&L while the plots may be construction sites. Whether any was capitalised: NOT FOUND. If none was, this is conservative by up to about Rs mn 170 [INFERENCE: plot identity NOT FOUND]. | S Note 1.2 p.156; Note 32 p.168 | [GREEN] if expensed |
| Impairment | Policy language only; inputs NOT FOUND. JHPPL carried at 939.00 vs net assets 242.60; no impairment | S Note 1C(5) p.146; C Note 36D p.226 | [YELLOW] |
| ECL | "Provision matrix" claimed; allowance = credit-impaired bucket only; good balances carry no allowance; no overlay amount | S Note 1C(13) p.152; S Note 7 p.159 | [YELLOW] |
| Ind AS 116 rate | NOT FOUND | S Note 37J p.177 | n/a |
| Policy changes quantified | None stated; presentation changes via "regrouped" only | S Note 37R p.182 | [YELLOW] |

### 2B Related-party map (C, Rs mn, FY26)
| Group | Items | Amount |
|---|---|---|
| Promoter executive pay | Dr. Ajay Thakker 41.99 (+8%); Dr. Ankit Thakker 39.00 (+50%) | 80.99 = 4.17% of C PAT |
| Other KMP | Dr. Rajesh Kasliwal (MD, JHPPL) 15.41; S. Sen 12.21 (part year); H. Purani 8.24; S. Upparatti 3.80 | 39.66 |
| Professional fees to NEDs and related | V. Raghavan 5.66; Dr. Bhaskar Shah 4.93; Devang Gandhi (brother-in-law of Dr. Ajay) 3.00; Anshul Sethi 3.06 (new, relationship not stated); Rajendra Thakkar 3.38 (new) | 20.03 |
| Promoter-linked entities and rent | Jupiter Foundation donation and CSR 15.69; Entisi Hospitality purchases 8.71; Jupiter Scan & Imaging rent paid 0.48; rent received 3.38 | 28.26 |
| Sitting fees; Gait Lab profit | 0.52; 2.84 | 3.36 |
| Total | 172.30 = 1.15% of revenue | |
Anchors: C Note 36K p.231-233; S Note 37K p.178-180. Value-extraction signals: the one 50% pay rise went to the Joint MD who took the role on 11-Jul-2025 (AR26 p.88); two NEDs who sit on the Audit, Risk, Stakeholder and CSR committees draw professional fees (Phase 5); donations to the promoter foundation are 39% of the Rs mn 40.00 CSR spend. None breaks a law on the face of the AR.

### 2C Contingent liabilities
| Item | Rs mn | % of net worth | % of PAT | Anchor |
|---|---|---|---|---|
| C total | 49.26 (claims 31.80, indirect tax 4.42, Indore property tax 13.04) | 0.32% | 2.54% | C Note 36B p.222-223 |
| Guarantee for JHPPL (outside the table) | 2,500.00 | 16.2% of C equity 15,440.93 | 128.7% of C PAT | S Note 37B p.172 |
Flags: the contingent table is under 25%; the guarantee is under 25% of net worth but is 1.29x annual PAT. RHP listed 9 material civil cases against the company, aggregate Rs mn 150.68 (RHP p.31), while the AR carries claims of 31.80 against the company and a Rs mn 250 insurance cover (S Note 37B p.171). The Rs mn 118.88 gap is unexplained; the RHP date is Aug 2023, so cases may have closed. Guarantee release test: JHPPL Debt/EBITDA below 3.5x for four consecutive quarters, or 50% repayment (AR26 p.92).

### 2D Receivables (C)
Gross 792.22 (FY25 459.67). Over 6 months: 29.13 + 18.64 + 6.15 = 53.92 = 6.8% of gross (FY25 10.4%). Unbilled 191.07 = 24.1%. Credit-impaired under 6 months 7.02 (1.36). Net days 18.4 (12.1). MD&A debtor days 20.64 vs 17.82 (AR26 p.47, different basis). Payer mix: insurance and others 55.4%, self-pay 43.6%, government 1.0% of revenue (AR26 p.20). No single payer share stated: NOT FOUND. Cross-check outside the AR: Sep-2026 trade receivables Rs Cr 118.3 vs 75.5 at Mar-2026 (+57% in six months) on Q2 revenue Rs Cr 436.3, which is about 24.7 receivable days (derived; Q2 FY27 presentation p.9, p.8). The build continues.

### 2E Inventory
C inventory 383.36 (FY25 264.61, +44.9%) vs revenue +15.2%. Days 48.7 vs 37.8. FIFO, lower of cost and NRV. Write-downs: NOT FOUND. MD&A attributes the turnover drop to the new hospital (AR26 p.47).

### 2F Borrowings
| Item | Finding | Anchor |
|---|---|---|
| Parent loan | HDFC term loan drawn Rs mn 2,620 of 3,500 sanctioned (880 undrawn), Repo + 200 bps, 180 monthly instalments Apr 2025 to Mar 2040, exclusive mortgage on the Dombivli hospital, second charge on current assets | S Note 15 p.163 |
| JHPPL loan | HDFC Rs mn 2,500 (fully drawn), Repo + 200 bps, 144 instalments Apr 2025 to Mar 2037, first mortgage on all JHPPL immovable property; parent guarantee | C Note 14 p.215 |
| Maturity (C, FY26) | under 1 yr 76.30; 1-3 yrs 307.20; over 3 yrs 4,701.77 | C Note 35 p.222 |
| Rate sensitivity | +/-0.5% = Rs mn 25.43 PBT (C); 13.05 (S) | C Note 35 p.222; S Note 36 p.171 |
| Covenants | NOT FOUND (the ICRA downgrade trigger is TD/OPBDITA above 1.8x, ICRA p.4) | |
| Pledge of shares | None reported by the company (CARO ix(f)) | p.135 |
| ICDs given | JHPPL 293.37; Medulla 28.85 (other receivable); no rate stated | S Note 37K p.180 |

### 2G Deferred tax
S DTL 295.70 (FY25 257.51); FY26 charge 37.54, of which depreciation timing 76.08 (S Note 34 p.169). Enacted rate 25.17%; C effective 25.44% (662.49 / 2,604.36). No MAT credit or unrecognised DTA disclosure: NOT FOUND.

### 2H Exceptional items, goodwill, ESOP, leases, post balance sheet
- Exceptional: Labour Codes past service cost Rs mn 48.87 (C), 43.89 (S). No other year since FY23 (RHP FY22 loss 1.98, FY23 loss 22.04, RHP p.76; AR25 shows nil).
- Goodwill: none in the AR (a Rs Cr 5.1 goodwill line appears at Sep-2026, secondary: Q2 FY27 presentation p.9; an acquisition closed in H1 FY27).
- ESOP: none (AR26 p.92). Dilution nil: basic EPS equals diluted EPS 29.59.
- Leases (C): liability 757.13 (655.33 + 101.80); Rs mn 656.19 falls beyond 5 years (C Note 36J p.231).
- Post balance sheet: interim dividend Re 1 per share (Rs mn 65.57, 3.4% of C PAT) declared 15-May-2026 (S Note 37O p.181); Medulla merger pending NCLT (S Note 37N p.181). Stock split: NOT FOUND IN DOCUMENT. The MMRDA lease award (27-Mar-2026, premium about Rs Cr 354) is not in the notes as a commitment or event, while the Directors' Report states "no material changes or commitments" after year-end (AR26 p.93).

### Reconciliation with the triple-pass score
B02 accounting quality 6/10. This stage agrees: no policy change, no covenant default, no going-concern language; weaknesses are disclosure gaps (borrowing cost, commitments, ECL) and the HMIS control exception. One point moves up: the re-cut is explained by pharmacy grossing (3C), which removes the fear of a hidden restatement of profit. One point stays down: nothing in the AR told the reader that.
Phase 2 verdict: [YELLOW].
Kill switch (informational): a human reviewer would not have reason to stop, because no breach is found; they would want capitalised interest and commitments from management before sizing.

---------------------------------------------------------------------
## PHASE 3: FINANCIAL STATEMENTS (cash flow, balance sheet, P&L)

### 3A Cash flow (C, Rs mn; AR26 p.193-194)
| Line | FY26 | FY25 | Note |
|---|---|---|---|
| Operating profit before WC | 3,529.99 | 3,099.30 | +13.9% |
| Working capital movement | (214.27) | +210.10 | swing -424.37; receivables (343.98), inventories (118.75), payables +268.27 |
| Cash from operations | 3,315.72 | 3,309.40 | |
| Tax paid | (638.64) | (642.01) | |
| CFO | 2,677.08 | 2,667.39 | +0.4% |
| CFO / PAT | 1.38 | 1.38 | stable |
| CFO / EBITDA (EBITDA ex-OI, pre-exceptional: 3,432.58 and 3,001.18) | 78.0% | 88.9% | down 10.9 pts |
| Capex (PPE, CWIP, intangibles) | (5,018.45) | (3,275.87) | 5.73x D&A (5.74x) |
| FCF (CFO - capex) | (2,341.37) | (608.48) | derived |
| Financing flows | +1,364.69 | +2,967.05 | borrowings in 1,860.43 less repaid 32.55 |
| Interest paid (financing) / received (investing) | (235.44) / +235.33 | (77.41) / +195.83 | CFO excludes both |
| Cash and equivalents | 547.61 | 925.16 | |
| Liquid assets (cash, bank, current investments) | 5,438.72 | 6,020.80 | -9.7% |
M&A spend: none. CFO quality: no one-time inflator; payables rose 38.3% (MSME past due 69.90); capital creditors rose to 509.70 from 355.43 (C Note 21 p.217), so cash capex understates what is owed. Verdict on quality: CFO converts earnings at 1.38x but conversion of EBITDA fell, receivables absorb cash, and FCF turned more negative. FLAG-CASH stays on (mild).

Funding of FY26 capex (derived): CFO covered 53%. Net debt raised 1,827.88 and a Rs mn 582.08 fall in liquid assets covered most of the rest. FY25+FY26: CFO 5,344.47 vs capex 8,294.32 = 64%. The chairman's line "internal accruals combined with prudent leverage will fund the bulk" (AR26 p.22) tests as follows for the forward plan: ICRA's FY27-FY29 plan Rs Cr 890-900 plus the BKC premium Rs Cr 354 plus the Pune land step-up Rs Cr 100 is about Rs Cr 1,344-1,354, against three years of CFO near Rs Cr 800 at the FY26 level plus liquid assets Rs Cr 544 and Rs mn 880 undrawn sanction [INFERENCE, arithmetic not projection; stage 11 owns projections]. The plan closes only with flat-to-higher CFO and some new debt.

### 3B Balance sheet (C, Rs mn; AR26 p.191)
| Item | Mar-26 | Mar-25 | Change |
|---|---|---|---|
| PPE | 12,768.59 | 8,994.19 | +42.0% (Dombivli 3,881.3) |
| CWIP | 1,292.12 | 1,851.10 | -30.2% |
| ROU assets | 990.61 | 740.26 | +33.8% |
| Capital advances (in other non-current assets) | 1,195.90 | 4.34 | new |
| Liquid assets | 5,438.72 | 6,020.80 | -9.7% |
| Receivables | 755.39 | 432.33 | +74.7% |
| Total assets | 23,831.29 | 19,357.50 | +23.1% |
| Equity | 15,440.93 | 13,563.04 | +13.8% |
| Borrowings | 5,085.27 | 3,257.13 | +56.1% |
| Lease liabilities | 757.13 | 674.32 | +12.3% |
| Trade payables | 955.39 | 690.98 | +38.3% |
| Other financial liabilities | 709.33 | 513.14 | +38.2% |

| Ratio | FY26 | FY25 | Source |
|---|---|---|---|
| Debt / equity | 0.33 | 0.24 | AR26 p.47 (verified) |
| Total debt / EBITDA (ex-OI), no leases | 1.48x | n/a | derived 5,085.27 / 3,432.58 |
| With leases | 1.70x | n/a | derived 5,842.40 / 3,432.58; ICRA trigger 1.8x, ICRA expected 1.4-1.6x |
| Net debt / EBITDA, CP counted | 0.12x | | derived (5,842.40 - 5,438.72) / 3,432.58 |
| Net debt / EBITDA, cash and bank only | 1.53x | | derived (5,842.40 - 581.68) / 3,432.58; matches B01 |
| Current ratio | 3.02 | 4.37 | AR26 p.47 |
| Quick ratio | 2.85 | | derived (6,849.00 - 383.36) / 2,265.75 |
| Interest coverage (EBIT ex-OI / finance cost) | 7.83x | 22.70x | derived; AR26 p.47 shows 7.82 and 22.70 |
| ROCE (S, AR definition) | 18.11% | 19.87% | S Note 37L p.181 |
| ROCE (C, EBIT incl. OI over year-end TA less CL) | 13.8% | 15.3% | derived; B01 cross-check 13.77% |
| ROE | 13.4% on average equity | | derived; AR26 p.47 shows 13% |
| Goodwill % net worth | 0% | 0% | none in AR |

DuPont (C, year-end basis, derived): ROE 12.6% = net margin 12.95% x asset turnover 0.629 x equity multiplier 1.543. FY25: 14.3% = 14.88% x 0.673 x 1.427. Net margin fell 1.93 pts and turnover fell 0.044; leverage rose 0.116 and adds to ROE. The ROE decline is operational (margin and idle assets in CWIP, capital advances and CP), not leverage-driven.

### 3C P&L (C, Rs mn; AR26 p.192)
| Line | FY26 | FY25 (re-cut) | YoY |
|---|---|---|---|
| Revenue from operations | 14,997.87 | 13,024.02 | +15.2% |
| Other income | 423.68 | 283.47 | +49.5% |
| Purchases net of inventory change | 2,872.68 | 2,554.82 | +12.4% |
| Employee benefit | 2,563.25 | 2,252.36 | +13.8% |
| Professional fees (doctors) | 3,640.29 | 3,052.82 | +19.2% |
| Other expenses | 2,489.07 | 2,162.84 | +15.1% |
| EBITDA ex-OI, pre-exceptional (derived) | 3,432.58 | 3,001.18 | +14.4% |
| Depreciation and amortisation | 876.40 | 570.83 | +53.5% |
| Finance cost | 326.63 | 107.06 | +205.1% |
| PBT before exceptional | 2,653.23 | 2,606.76 | +1.8% |
| Exceptional | (48.87) | nil | |
| PBT | 2,604.36 | 2,606.76 | -0.1% |
| Tax | 662.49 | 669.22 | effective 25.4% vs 25.7% |
| PAT | 1,941.87 | 1,937.54 | +0.2% |
| EPS basic = diluted (Rs 10 FV, pre-split) | 29.59 | 29.47 | +0.4% |
Margin waterfall (% of revenue): materials 19.15 (19.62); employee 17.09 (17.29); doctor fees 24.27 (23.44); other 16.60 (16.61); EBITDA 22.89 (23.04); D&A 5.84 (4.38); finance 2.18 (0.82); other income 2.82 (2.18); PAT 12.95 (14.88). Like for like, the EBITDA margin moved -0.15 pt; doctor fees cost +0.83 pt and were offset by materials -0.47 and employee -0.20.

Profit bridge, PBT before exceptional, Rs mn: EBITDA +431.40; D&A -305.57; finance -219.57; other income +140.21; net +46.47 (check: 2,653.23 - 2,606.76 = 46.47).
- D&A +305.57: ROU assets +126.25 (165.08 vs 38.83: a full year of the leasehold land added in FY25); PPE +170.53 (696.67 vs 526.14; S medical equipment +79.21); intangibles +8.79 (C Note 31 p.219; S Note 1.1 p.155). S buildings depreciation rose only 4.94 (47.79 vs 42.85), against a full-year equivalent of about 34.66 for Dombivli buildings at 60 years (2,079.63 / 60) [derived]: FY26 holds a stub of Dombivli depreciation.
- Finance cost +219.57: interest on term loans +199.88 (204.40 vs 4.52, C Note 30 p.219). Parent expensed 15.15; the rest, about 189.25, is JHPPL on its Rs mn 2,500 loan (about 7.6%) [derived: C minus S]. JHPPL drew that loan in FY25 and repaid the parent's Rs mn 2,500 intercompany loan (S cash flow FY25 +2,499.74, AR26 p.142). So 84% of the finance step-up is the refinancing of an existing hospital, not new-hospital debt. Lease interest +38.95; bank charges -19.30.
- Other income +140.21: gain on sale of investments 131.46 (FY25 44.64) and interest 294.36 (FY25 199.63). Gain on sale is 5.0% of PBT and not repeatable by design. Other income is 16.3% of PBT: below the 20% flag, above FY25's 10.9%.
- Exceptional: AR26 p.31 calls it "one-time exceptional provision of Rs 6.4 Crore". The statements show Rs mn 48.87 (Rs Cr 4.89). Q3 FY26 booked a loss of Rs Cr 6.4 and Q4 reversed Rs Cr 1.5 (Q4 FY26 presentation p.7), so 6.4 is the gross quarter figure; the AR does not say so.

The FY25 re-cut, resolved. FY25 C revenue rose from 12,615.45 to 13,024.02 (+408.57). Lines (Rs mn): pharmacy sales now shown at 338.57 (AR25: none); cafeteria sales 116.76 (AR25: none); share in profit of partnership firms -0.35 (AR25 +47.08); medical services 1.00 (0.33). Net: 338.57 + 116.76 - 47.43 + 0.67 = 408.57, an exact match (AR26 p.218 Note 24 vs AR25 p.97 Note 22). The pharmacy partnership became JHP Pvt Ltd in March 2025 and is now consolidated line by line. Consequences:
1. Hospital services growth is the clean comparator: inpatient + outpatient 14,355.69 vs 12,454.16 = +15.3% on both bases. The "+18.9% on the AR25 base" in B02 mixes a base that held pharmacy profit as net with a numerator that holds it gross. Use +15.2% (total) or +15.3% (hospital services).
2. The cover chart (AR26 p.19) shows FY25 EBITDA margin 23.50% beside FY26 22.89%. 23.50% is the AR25 as-filed margin (2,965.64 / 12,615.45, derived). The MD&A (p.47) shows 23.04% for FY25, which is the like-for-like figure (3,001.18 / 13,024.02). The headline margin fall of 0.61 pt is 0.15 pt like for like; the rest is low-margin pharmacy revenue entering the denominator. ICRA's FY25 figure of 23.6% is also the old basis (ICRA p.2).
3. The pharmacy and cafeteria gross-up raises revenue and lowers every ratio built on it; it does not change PAT (FY25 PAT +2.54 only).

Revenue growth split (secondary, derived): ARPOB +11.7% (Rs 67,700 vs 60,600, AR26 p.20) implies occupied bed days grew about 3% (1.153 / 1.117) [INFERENCE: ARPOB basis excludes unbilled and doctors' provision]. Inpatient discharges rose 52.9k to 53.9k (+1.9%), outpatient bills 926.4k to 1,022.5k (+10.4%) (Q4 FY26 presentation p.6). Fifteen percent revenue growth is mostly price and case mix.

Other income composition (C Note 25 p.218): interest 294.36 (bank 27.49, investments 245.15, other assets 18.71, deposits 0.33, tax refund 2.68); gain on sale of investments 131.46; fair-value loss (18.57); dividend 0.08; rent 1.23; scrap 4.99; wind 5.20; misc 4.93.
Exceptional items three-year pattern: FY24 nil, FY25 nil, FY26 48.87. Tax rate consistent. Basic EPS equals diluted EPS (no dilutive instruments).

Phase 3 verdict: [YELLOW]. Profit quality is sound on a like-for-like basis (margin held, CFO/PAT 1.38). Cash is weaker: FCF negative, CFO/EBITDA down, receivables +72%.
Kill switch (informational): a human reviewer would not have reason to stop, because the build is financed with room left (liquid assets exceed debt), but would want the capex commitment schedule before sizing.

---------------------------------------------------------------------
## PHASE 4: RISK FACTORS AND MD&A

### 4A Disclosed risks (AR26 p.47-48, MD&A risk framework)
| Risk | Real or boilerplate | Evidence |
|---|---|---|
| Geographic concentration (Western India) | Real | ICRA p.3 lists it as a rating factor |
| Human resources (doctors, nurses) | Real | doctor fees 24.27% of revenue; turnover 24.1% for permanent staff (BRSR AR26 p.53) |
| Regulatory | Boilerplate | no specific price-control or licence item |
| Technology (includes "cost-reimbursement gap in insurance") | Misfiled | the payer risk sits under Technology |
| Reputational | Boilerplate | |
| Competitive | Boilerplate | |

### 4B Missing risks
| Risk absent from the risk section | Evidence | Likely reason |
|---|---|---|
| Capex funding, leverage and rate risk for a 1,700-bed programme | Debt 5,085.27 floating at Repo + 200 bps; +/-0.5% = 25.43 PBT (C Note 35 p.222); FY26 capex 5.7x D&A; the CEO letter itself calls greenfield "hard" with "delay and cost overrun" (p.22) | the template covers operations, not strategy |
| Project execution and approvals (Mira Road, BKC) | Mira Road in "regulatory approval and planning stage"; BKC "documentation and registration"; BKC date moved from 2030 (AR26 p.7) to CY31 (Q2 FY27 presentation p.11) | management frames delays as phasing |
| New-hospital ramp-up losses | Dombivli opex loss Rs Cr 9.4 in Q4 FY26 (Q4 FY26 presentation p.7); AR26 p.12 mentions breakeven timing only as outlook | optimism in outlook text |
| Receivable and TPA risk | Receivables +72.3%; unbilled new; ECL on impaired bucket only; the KAM | framed as accounting, not business risk |
| Mature-hospital occupancy decline | Network occupancy 65.3% to 61.2% (62.3% ex-Dombivli), ex-Dombivli beds 1,061 to 1,048 after 100 beds were added during FY25 (AR25 p.4); hospital-wise data dropped | disclosure withdrawn |
| Liquidity concentration in one CP issuer | 89.3% of liquid assets in JM Financials Services paper (C Note 6 p.211) | treated as treasury, not risk |
| Revenue-system control gap (HMIS) | Auditor paras 19.2, 20.8 | Technology row mentions only equipment failure and cybersecurity |
| Medical-negligence litigation | RHP p.31: 9 material civil cases, Rs mn 150.68; AR contingent 31.80; insurance Rs mn 250 | litigation is not discussed |
| Subsidiary exposure | Guarantee 2,500 + loan 293.37 + cost 939.00 = 3,732.37 on a loss-making subsidiary | omitted as intra-group |
Management omission is itself a signal: the six-row table is a general hospital list and was not updated for a year in which debt rose 56% and receivables 72%.

### 4C MD&A deep dive
- Industry claims. Hospital market USD 193.42 bn (CY2025) to USD 364.55 bn by CY2034 at 7.3% (AR26 p.39). Sourced from third parties; no company-specific market share.
- Growth and margin explanation. Net margin fall (14.88% to 12.95%) attributed to "the new wage code and operationalisation of the new unit" (AR26 p.47). The statements show finance cost +205% and ROU amortisation +325% as larger drivers (3C). The wage code is Rs mn 48.87, 0.33% of revenue. The explanation is true but incomplete.
- Credit-taking and blame. Credits the team for Dombivli being "ahead of schedule and on budget" (p.22). Blames no external factor. Silent on the occupancy drop.
- The internal control section (p.49) reads "strong" and is silent on the HMIS exception.
- Segment: single reportable segment (S Note 37M p.181). Revenue mix (C): inpatient 78.3%, outpatient 17.5%, pharmacy 2.6%, cafeteria 0.9%, hotel 0.7% (C Note 24 p.218).

Forward guidance and credibility
| Claim | Number | Timeframe | Credibility |
|---|---|---|---|
| Dombivli opening (AR25 p.11) | commissioning Q1 FY27 | delivered 15-Feb-2026 | High: ahead by 1.5-4 months |
| Dombivli "just over 25 months" (AR26 p.11) | 25 months | RHP p.209, p.212 and AR25 p.4: construction began April 2023; to 15-Feb-2026 is 34 months; RHP said 30-36 months is usual | Low as worded; the schedule claim holds only against the AR25 guidance |
| Dombivli "on budget", Rs Cr 425 | 425 vs capitalised Rs mn 3,881.3 (Rs Cr 388.1) | FY26 | Unverifiable: no budget in RHP or AR25 (NOT FOUND); ICRA also cites about 425 |
| Dombivli EBITDA breakeven (AR26 p.12) | by end of year 2 of operations | Feb 2028 | Medium-high: Q2 FY27 loss already Rs Cr 0.2, helped by an infectious-disease season (secondary) |
| Pune South (p.22, p.43) | on track, 500 beds | CY2028 | High so far: AR25 said construction "after monsoon" and AR26 shows excavation done |
| Mira Road (p.22, p.43, p.7) | "excavation expected before year end"; 300 beds, Rs Cr 400; online 2029 | excavation CY2026 | Low-medium: Oct-2026 presentation still says regulatory approval and planning stage |
| BKC (p.7) | 400 beds | 2030 | Medium-low: Q2 FY27 presentation moves it to CY31 |
| Network size (p.4, p.5, p.43) | "~3,000 beds" | multi-year | Sum of the listed capacities is 2,881; presentation says 2,900; AR25 target was 2,500 (raised) |
| Funding (p.22) | "internal accruals combined with prudent leverage will fund the bulk" | FY27-FY30 | Medium: FY26 was 53% accrual-funded |
| Growth pace (p.22) | "We are not trying to grow fast" | | Tone only: beds +136% on the 1,248 base |

### 4D Tone and credibility (1 to 5)
| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 3 | project-by-project dates and beds; but no capitalised interest, no commitments, no hospital-wise occupancy |
| Consistency | 3 | cover chart mixes margin bases; "25 months" vs April 2023 start; Rs 6.4 Cr vs Rs 4.89 Cr exceptional; CAGR labels not reproducible (6A) |
| Specificity | 4 | bed counts, phases, years per site, cost for Dombivli and Mira Road; BKC cost absent |
| Accountability | 3 | takes credit for early opening; explains the margin fall by the wage code and the new unit only |
| Capital allocation sense | 3 | owned real estate by choice; IPO money used to clear debt (RHP p.108-109: Rs mn 5,104.06 for repayment) then re-levered to 5,085.27; liquid assets Rs mn 5,438.72 parked 89% in one CP issuer; payout 3.4% |

Contradictions with Phases 1-3: the MD&A "internal control strong" (p.49) vs the HMIS exception (Phase 1); "unbilled revenue reporting" and "conservative provision" listed as governance improvements (p.32) vs ECL on impaired bucket only (Phase 2).
Phase 4 verdict: [YELLOW].
Kill switch (informational): a human reviewer would not have reason to stop; the omissions are of emphasis, not of fact.

---------------------------------------------------------------------
## PHASE 5: CORPORATE GOVERNANCE AND BOARD

### 5A Board (31-Mar-2026; AR26 p.97-98)
| Director | Category | Other directorships | Shares | Board attendance |
|---|---|---|---|---|
| Dr. Ajay Thakker | CMD, promoter | 4 | 1,35,97,829 (20.74%) | 4 of 4 |
| Dr. Ankit Thakker | Joint MD and CEO, promoter (since 11-Jul-2025); related to Dr. Ajay under the Act | 6 | 43,75,789 (6.67%) | 4 of 4 |
| Dr. Bhaskar Shah | NED | 5 | nil | 4 of 4 |
| Mr. Vadapatra Raghavan | NED | 1 | 3,10,000 | 4 of 4 |
| Dr. Darshan Vora | ID | nil | nil | 3 of 4 (75%) |
| Dr. Jasmin Patel | ID | 2 | nil | 4 of 4 |
| Ms. Urmi Popat | ID | 1 | 1,00,000 | 4 of 4 |
| Mr. Satish Utekar | ID | 1 | nil | 4 of 4 |
| Mr. Amar Manjrekar | ID (postal ballot Oct-2024) | 2 | nil | 2 of 4 (50%); 0 of the 1 Risk Committee meeting he was entitled to attend |
Flags: attendance under 75%: Manjrekar. Independents over 10 years: none (Vora and Patel are in a second term, 25-Sep-2023 to 24-Sep-2028, RHP p.239 footnote; the first term therefore began about Sept 2018 [INFERENCE]). Promoter-group cross-board seats: Western Medical Solutions LLP is a promoter (8.70%); its partners are NOT FOUND. Seats above 8: none. Five of nine are independent (55.6%); the chair is an executive promoter.

### 5B Committees (AR26 p.99-107)
| Committee | Members | Meetings | Note |
|---|---|---|---|
| Audit | Utekar (chair), Raghavan (NED, paid professional fees Rs mn 5.66), Vora, Popat | 4 | Raghavan also chairs the Risk and Stakeholders committees |
| Nomination and Remuneration | Vora (chair), Raghavan, Utekar, Popat | 1 (9-May-2025) | one meeting in a year that changed the CFO and made the CEO Joint MD with a 50% pay rise |
| Stakeholders | Raghavan (chair), Popat, Dr. Ankit | 1 | nil complaints |
| Risk | Raghavan (chair), Utekar, Manjrekar | 2 | Manjrekar absent |
| CSR | Popat (chair), Patel, Dr. Bhaskar Shah (paid professional fees Rs mn 4.93) | 2 | promoters left the committee on 1-Aug-2025 |
Independent directors met alone on 30-Jan-2026. The Audit Committee meets the auditors without management quarterly (p.99).

### 5C Compensation
| Item | Finding | Anchor |
|---|---|---|
| Promoter pay | Rs mn 80.99 (S) = 4.23% of S PAT; 4.17% of C PAT | S Note 37K p.179 |
| KMP total (C) | Rs mn 120.65 = 6.2% of C PAT | C Note 36K p.232 |
| Ratio to median employee | Dr. Ajay 110x, Dr. Ankit 103x; median pay rose 3.8%, non-KMP average 9.3%; Dr. Ankit +50%, Dr. Ajay +8% | AR26 p.126-127 |
| Promoter family on payroll | Devang Gandhi (brother-in-law) professional fees 3.00 (+25%) | S Note 37K p.179 |
| ESOP | none | AR26 p.92 |
| Employees | 3,002 permanent; 1,945 other than permanent; turnover 24.1% (26.2% FY25) | BRSR AR26 p.52-53 |

### 5D Shareholding (AR26 p.111 vs AR25 p.50, as of 31-Mar-2025)
| Holder | Mar-2026 | Mar-2025 |
|---|---|---|
| Promoters and promoter group | 40.91% (2,68,25,623 shares) | 40.91% |
| Mutual funds | 10.97% | 11.09% |
| Banks, FIs, insurers | 2.45% | 0.94% |
| FPIs | 8.48% | 10.03% |
| Bodies corporate and LLPs | 6.07% | 5.71% |
| Individuals | 24.36% | 24.39% |
| Directors, relatives, KMP | 2.00% | 2.05% |
Promoter holding unchanged; pledge: NOT FOUND IN DOCUMENT (the AR reports none; only a bank margin-money lien of Rs mn 33.95). Promoter selling: none in the AR window. FPIs -1.55 pts; domestic banks, FIs and insurers +1.51 pts. Promoters named in the notes hold 36.11% (three promoters); the 40.91% includes the wider promoter group (S Note 13E p.162). Sep-2026 data sits in inputs/shareholding and belongs to B08. No FLAG-PROMOTER-PRELIM.

### 5E Red-flag checklist
| Check | Result |
|---|---|
| Whistle-blower complaints | nil (CARO xi(c)); with about 4,950 people on roll or retainer (BRSR), nil is notable |
| POSH complaints | nil (AR26 p.93) |
| SEBI or exchange action | none in the year (AR26 p.108) |
| RPT committee | Audit Committee approves; RPTs 1.15% of revenue |
| Auditor fee ratio | non-audit nil |
| CSR | Rs mn 40.00 spent vs 40.60 required; prior set-off 8.77 leaves 8.17 (S Note 37F p.175); beneficiaries a medical college and a sports trust; the college is unnamed (NOT FOUND) |
| Section 143(12) fraud | none |
| Material subsidiary auditor | Shah Valera & Associates LLP, appointed 5-Sep-2024 (AR26 p.109) |
| Secretarial audit | no qualification (AR26 p.117-121) |
| Directors disqualified | none; PCS certificate (AR26 p.112) |
Phase 5 verdict: [YELLOW]. Strong form, thin independence at the committees that matter: two NEDs who take professional fees sit on Audit, Risk, Stakeholders and CSR; one independent attends half the board meetings.
Kill switch (informational): a human reviewer would not have reason to stop.

---------------------------------------------------------------------
## PHASE 6: CHAIRMAN'S LETTER AND FRONT MATTER (read last)

### 6A Narrative against reality
| Claim | Evidence | Mark |
|---|---|---|
| "Dombivli opened in February, ahead of schedule and on budget... completed in just over 25 months" (p.22) | Opened 15/25-Feb-2026 against Q1 FY27 guidance: ahead. "25 months" conflicts with construction start April 2023 (34 months; RHP p.209). Budget baseline NOT FOUND. | partly supported (ahead); contradicted (25 months); budget unverified |
| "Internal accruals combined with prudent leverage will fund the bulk" (p.22) | FY26 CFO 53% of capex; net debt raised 1,827.88 | contradicted for FY26; open for FY27+ |
| "We are not trying to grow fast" (p.22) | ~1,700 new beds on 1,248 operational; capex 5.7x D&A | contradicted (tone vs scale) |
| "Current hospitals continue to generate strong cash flows" (p.22) | CFO 2,677.08 flat; mature margin held (derived) | supported |
| "15% CAGR revenue, 17% EBITDA, 31% PAT, FY21 to FY26" (p.19) | RHP: FY21 revenue 4,861.64 (RHP p.76) to 14,997.87 is 25.3% over 5 years; hospital services only 24.3%; FY22 733.1 to 1,499.78 is 19.6% over 4 years; PAT from a FY21 loss (22.97) gives no CAGR; FY22 to FY26 PAT is 39.6% | contradicted: labels not reproducible; the 15% matches the single-year growth |
| EBITDA margin 22.89 vs 23.50 (p.19) | 23.50 is the old basis; like for like 23.04% | contradicted: mixed bases |
| "One-time exceptional provision Rs 6.4 Crore" (p.31) | Statements: Rs mn 48.87 | contradicted (gross vs net unstated) |
| "Transition to reporting of unbilled revenue; conservative provision policy for professional fees" (p.32) | Unbilled 191.07 shown; ECL on impaired bucket only | partly supported |
| Occupancy 61.2% (62.3% ex-Dombivli); ARPOB Rs 67,700 (+11.7%) (p.20, p.46) | Match Q4 FY26 presentation p.6 | supported |

### 6B Strategic priorities
Specific: yes, per site with bed counts, years and cost for Dombivli and Mira Road (p.7, p.43). Capital allocated: Dombivli Rs Cr 425 (done); Mira Road Rs Cr 400; Pune South and BKC costs NOT FOUND in the AR (the BKC premium is in a filing; Pune capex per bed is in the presentation). Execution evidence: Dombivli ahead of guidance; Pune South excavation done.

### 6C Metrics showcased vs absent
Showcased: revenue, EBITDA, PAT, ARPOB, ALOS, network occupancy, payor mix, awards. Absent: hospital-wise occupancy, ARPOB or EBITDA; Dombivli revenue and loss; capitalised interest; capital commitments; ROCE (only ROE 13%); net debt; cash conversion; IPD and OPD volumes (in presentations, not in the AR).

### 6D Tone and priority drift against AR25
- AR25 (p.11): "six-hospital network was our initial target... merely a stepping stone... exploring additional greenfield and acquisition opportunities". AR26 (p.22): "Every project in our pipeline is greenfield... we own, or will own, substantially all of the real estate". Acquisitions are no longer mentioned, yet a Rs Cr 5.1 goodwill line appears by Sep-2026 (secondary).
- Goal moved from 2,500 beds (AR25 p.7: 2,494 total capacity across six hospitals) to ~3,000 (seven hospitals).
- AR25 hospital table showed Thane at 377 operational beds (AR25 p.7); AR26 shows 364 (AR26 p.7, p.13). ICRA's 1,048 beds (Thane 364 + Pune 375 + Indore 309) agrees with AR26. The 13-bed fall is not explained in AR26. AR25 p.11 describes removing a 22-bed unit for theatres and cath labs.
- Message signature: the AR26 message is titled "Combined Message from the CMD and the CEO" but is written in the first person and signed by Dr. Ankit Thakker alone (p.22).

### 6E Quiet Abandonment Check
| Opening claim | Where it should show | Class | Materiality |
|---|---|---|---|
| AR25 hospital-wise occupancy (Thane 72.1%, Pune 65.5%, Indore 54.9%, AR25 p.5) | AR26 operating review, p.20 and p.46 show network only | (b) silent drop | Material: network occupancy fell 4.1 pts, 62.3% ex-Dombivli; the split would show which hospital lost it. ICRA says 9M occupancy was 61.9% vs 67.5% (ICRA p.2). Ask the company. |
| AR25 "actively exploring additional greenfield and acquisition opportunities" (p.11) | AR26 strategy text says all greenfield | (b) silent drop | Moderate: goodwill appears by Sep-2026 (Rs Cr 5.1, secondary) |
| "Combined message from the CMD and the CEO" | Only the CEO speaks | (c) hedged retreat in form | Low: governance optic of a generational hand-off; Joint MD pay +50% |
| "Strong cash flows... internal accruals will fund the bulk" (p.22) | Cash flow statement p.193 | (c) hedged retreat | Moderate: 53% in FY26 |
| Dombivli 300+ bed fit-out and 500-bed capacity (p.11) | Operational beds 200 (p.7) | consistent, phased | none |
| Thane 377 beds (AR25 p.7) | Thane 364 (AR26 p.7) | (a) implicit retraction | Low: 1% of beds |
No other opening claim is withdrawn.

Phase 6 verdict: [YELLOW]. The story is mostly backed by the filings. The chart labels, the 25-month claim and the dropped occupancy split make the front pages less reliable than the notes.

---------------------------------------------------------------------
## PHASE 7: MULTI-STRATEGY SIGNALS

Basis for market numbers: B00 manifest CMP Rs 287 and market cap Rs Cr 9,391 (post-split basis), with AR26 figures (derived): P/E 48.4x on FY26 PAT Rs Cr 194.2; P/B 6.1x on equity Rs Cr 1,544.1 (Q4 FY26 presentation p.8).

| Strategy | Call | Top reasons |
|---|---|---|
| GARP (full reasoning) | WATCHLIST | (1) Trailing: EPS +0.4% in FY26 (29.59 vs 29.47 pre-split) against revenue +15.2%; P/E 48.4x gives no usable PEG on trailing numbers. (2) Forward depends on the Dombivli ramp: Q2 FY27 EBITDA loss Rs Cr 0.2, but H1 FY27 PAT Rs Cr 93.9 vs 101.4 (-7.4%) (secondary). The mature base margin held (23.5% vs 23.0%). (3) D&A and finance cost run higher in FY27 (Q2 FY27 Rs Cr 28.5 and 13.8 a quarter vs FY26 quarterly average 21.9 and 8.2). The ~1,700-bed pipeline is a multi-year earnings base only if each hospital reaches the mature margin; ROCE already fell (S 19.87% to 18.11%). |
| Turnaround (full reasoning) | FAIL as a company-level turnaround | (1) Nothing to turn around: no loss year since FY21 (RHP p.76), margin 22.9-23.0%, CFO/PAT 1.38. (2) The only turnaround is unit-level: Dombivli from a Rs Cr 9.5 loss to 0.2 in one quarter, which is a ramp, not a recovery. (3) The profit squeeze is capital-structure and amortisation driven (3C), mechanical, and reverses only through volume growth at the new beds. |
| Capex-Led Growth | WATCHLIST (best fit) | (1) Capex 5.73x D&A, 1,248 to ~2,900-3,000 beds; Dombivli ahead of AR25 guidance. (2) Land is owned or on long lease (BKC 80 years). (3) Returns not yet visible; commitments undisclosed; FCF -2,341.37 Rs mn. |
| Value + Quality | FAIL | P/E 48.4x; ROE 13.4%; ROCE falling |
| Cash Flow Compounder | FAIL today | FCF negative two years; CFO/EBITDA 78% |
| Contrarian | FAIL | FPIs trimmed 1.55 pts but the multiple is high; no panic |
| Insider Confidence | WATCHLIST | promoters flat at 40.91%, no pledge reported, no ESOP; no open-market buying evidence in the AR; Joint MD pay +50% |
| Guidance Divergence | WATCHLIST | Dombivli and Pune on or ahead; Mira Road and BKC drifting; chart-label and 25-month inconsistencies |

---------------------------------------------------------------------
## PHASE 8: FINAL VERDICT DASHBOARD

Snapshot (C, FY26, Rs mn): revenue 14,997.87; EBITDA ex-OI 3,432.58 (22.89%); PAT 1,941.87; CFO 2,677.08; capex 5,018.45; debt 5,085.27; liquid assets 5,438.72; equity 15,440.93; 4 hospitals, 1,248 operational beds; promoter 40.91%.

| Phase | Verdict |
|---|---|
| 1 Auditor and CARO | [YELLOW] |
| 2 Notes | [YELLOW] |
| 3 Financials | [YELLOW] |
| 4 Risk and MD&A | [YELLOW] |
| 5 Governance | [YELLOW] |
| 6 Front matter | [YELLOW] |
| 7 Best fit | Capex-Led Growth (WATCHLIST) |

Quality score 6.4 / 10 (each component 25%): governance 6.5 (clean form, committee independence thin, attendance gap, Joint MD pay +50%); accounting 6.0 (agrees with B02); balance sheet 7.0 (net liquid position positive, ICRA AA- Stable, floating debt and CP concentration); earnings 6.0 (like-for-like margin held; ROCE, FCF and cash conversion fell).

Top 3 strengths
1. Mature margin held: derived ex-Dombivli EBITDA margin 23.5% vs 23.0% while ARPOB rose 11.7% (Q4 FY26 presentation p.7; AR26 p.20).
2. Delivery against guidance: Dombivli opened 1.5-4 months ahead of the AR25 date; Pune South construction started on the AR25 schedule (AR25 p.11; AR26 p.43).
3. Clean statutory record: unmodified opinion, no CARO adverse remark, no default, contingent liabilities 0.32% of net worth, ICRA upgrade to AA- (AR26 p.92, p.133-136).

Top 3 red flags
1. Capital commitments, capitalised interest and the BKC premium (about Rs Cr 354) are absent from the notes while debt is up 56% (S Note 37B p.171; C Note 14 p.215).
2. Hospital-wise occupancy dropped in the year network occupancy fell 4.1 pts; receivables +72.3%; the HMIS audit-trail exception sits on the revenue system (AR25 p.5; C Note 7 p.212; AR26 p.132).
3. Front pages mix bases and misstate facts: FY25 margin 23.50% vs 23.04%; "25 months" vs April 2023 start; Rs 6.4 Cr vs Rs mn 48.87 (AR26 p.19, p.11, p.31).

Key monitorables
| Metric | Threshold | Where | Why |
|---|---|---|---|
| Dombivli quarterly EBITDA | positive by Q4 FY27; AR26 promise is breakeven by Feb 2028 | quarterly presentation, EBITDA footnote | tests the ramp |
| Ex-Dombivli occupancy | at least 65% (H1 FY27: 64.8%; FY25: 65.3%) | quarterly presentation | tests mature demand against the 100 beds added in FY25 and the dropped split |
| Capital commitments and capitalised borrowing cost | disclosed in the FY27 notes; commitments at least Rs Cr 890-900 plus BKC 354 and Pune land 100 | FY27 AR notes 36/37 | sizes funding |
| Total debt / EBITDA | stay under 1.8x; Sep-2026 is 1.64x ex-leases and 1.86x with leases (derived: Rs Cr 588.8 and 668.6 vs LTM EBITDA 358.8) | quarterly balance sheet and EBITDA | ICRA trigger 1.8x |
| Receivable days | at or below 18.4; Sep-2026 is about 24.7 (derived) | quarterly balance sheet | cash conversion |
| CFO / EBITDA | at least 80% (FY26 78.0%) | half-year cash flow | quality of profit |
| D&A and finance cost per quarter | D&A Rs Cr 28.5 and finance Rs Cr 13.8 (Q2 FY27) as the base; further rise only with new beds | results | squeeze run-rate |
| HMIS audit trail | no exception in the FY27 auditor report | FY27 AR auditor report | revenue system control |
| Promoter holding and pledge | at least 40.91%, no pledge | quarterly shareholding pattern | alignment |
| CP issuer concentration | JM Financials share under 50% of liquid assets (FY26 89.3%) | AR Note 6 | liquidity buffer |

Best-fit strategy: Capex-Led Growth.
One-line verdict: A well-run hospital operator whose mature margin held and whose build is on schedule, but whose commitments, hospital-wise data and front-page labels are thinner than the notes.

---------------------------------------------------------------------
## CONTRADICTION REGISTER (cross-phase)
1. B02 "growth 18.9% on AR25 base" vs 15.2% (and 15.3% hospital services): resolved; the re-cut is the pharmacy and cafeteria gross-up (3C).
2. AR26 p.19 FY25 EBITDA margin 23.50% vs AR26 p.47 23.04%: different bases.
3. AR26 p.11 "25 months" vs RHP p.209/p.212 and AR25 p.4: construction began April 2023.
4. Brief "commencement January 2026" vs the filing of 30-Jan-2026 (completion) and AR26 p.12 (15 and 25 Feb 2026).
5. AR26 p.31 Rs 6.4 Cr exceptional vs statements Rs mn 48.87.
6. AR26 p.5/p.20 "61.2% occupancy" with no hospital split vs AR25 p.5 split.
7. Directors' Report p.90 "no qualifications" vs auditor para 19.6 "modification" (audit trail).
8. Directors' Report p.93 "no material changes or commitments" after year-end vs the MMRDA premium (about Rs Cr 354) accepted on 27-Mar-2026.
9. S Note 37C "unfunded" gratuity vs plan assets Rs mn 86.83.
10. C Note 35 p.221 "insignificant interest bearing borrowings" vs Rs mn 5,085.27.

## B00 gaps carried: see block. AR-specific NOT FOUND IN DOCUMENT list: Dombivli depreciation start; capitalised borrowing cost and pre-operative cost; capital commitments; BKC premium in the AR; covenants; ECL matrix rates and overlay; impairment inputs; Ind AS 116 rate; interest rate on JHPPL and Medulla loans; CP yield; stock split; promoter pledge series; hospital-wise occupancy, ARPOB and EBITDA; occupancy and ARPOB definitions; Dombivli revenue; payer concentration; auditor tenure start; Western Medical Solutions LLP partners; CSR medical college name; MAT credit and unrecognised DTA.

```yaml
stage: B03-ardeep
company: "JLHL"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "B00: shareholding/ was empty; REPAIRED at /step1 with NSE XBRL for 30-Sep-2026 (one quarter, no pledge trend). Promoter pledge series NOT FOUND in AR26."
  - "B00: screener export sheets empty; only the four Data_Sheet CSVs populated. No effect on AR evidence."
  - "B00: results PDFs and rating PDF absent at collection; REPAIRED at /step1. Results text layers garbled; this stage used presentations and ICRA only as labelled secondary cross-checks (Rs Cr)."
  - "B00: research and other folders EMPTY; no broker notes."
  - "B00: final Prospectus 11-Sep-2023 not in corpus; RHP used for FY21-FY23 baseline."
  - "B00: announcements are a selection, not the complete 12-month record; two scanned announcements not used."
  - "AR-specific NOT FOUND IN DOCUMENT: Dombivli depreciation start; capitalised borrowing cost; capital commitments; BKC premium in AR; covenants; ECL matrix and overlay; impairment inputs; Ind AS 116 rate; JHPPL and Medulla loan rates; CP yield; stock split; hospital-wise occupancy, ARPOB, EBITDA; occupancy and ARPOB definitions; Dombivli revenue; payer concentration; auditor tenure start; Western Medical Solutions LLP partners; CSR medical college name."
flags:
  - {type: FLAG-CASH, reason: "C CFO/EBITDA 78.0% vs 88.9%; FCF Rs mn (2,341.37) vs (608.48); receivables gross +72.3%, net days 12.1 to 18.4 (AR26 p.193, p.212); Sep-2026 receivable days about 24.7 (secondary, derived). CFO/PAT stable 1.38."}
  - {type: FLAG-CAPEX-DISCLOSURE, reason: "No capital commitments or capitalised interest in AR26; BKC lease premium about Rs Cr 354 accepted 27-Mar-2026 not in notes; Directors' Report p.93 says no material commitments."}
  - {type: FLAG-CONTROL, reason: "HMIS audit-trail exception in Parent and 1 subsidiary; backup-log exception in Parent and 2 subsidiaries (AR26 p.131-132, p.188)."}
  - {type: FLAG-LIQUIDITY-CONCENTRATION, reason: "89.3% of liquid assets (Rs mn 4,857.04 of 5,438.72) in one CP issuer (C Note 6 p.211)."}
  - {type: FLAG-NARRATIVE-CONSISTENCY, reason: "AR26 p.19 mixes FY25 margin bases (23.50 vs 23.04); '25 months' vs April 2023 start (RHP p.209); Rs 6.4 Cr vs Rs mn 48.87 exceptional; hospital-wise occupancy dropped vs AR25 p.5."}
phase_verdicts: {p1: "YELLOW", p2: "YELLOW", p3: "YELLOW", p4: "YELLOW", p5: "YELLOW", p6: "YELLOW", p7_best_fit: "Capex-Led Growth (WATCHLIST)"}
overall_quality: 6.4
quality_components: {governance: 6.5, accounting: 6.0, balance_sheet: 7.0, earnings: 6.0}
kill_switch_notes:
  - "P1: a human reviewer would not stop; no qualification or default; name a fix date for the HMIS audit trail."
  - "P2: would not stop; wants capitalised interest and capital commitments from management before sizing."
  - "P3: would not stop; FCF negative but liquid assets exceed debt; wants the commitment schedule."
  - "P4: would not stop; omissions are of emphasis, not fact."
  - "P5: would not stop; committee independence is thin and one independent attends 50% of board meetings."
  - "P6: would not stop; front pages are less reliable than the notes."
triple_pass_verification:
  verified: 14
  discrepancies:
    - {finding_rank: 6, triple_pass_value: "net cash comparison 2,763.67 (Rs mn)", ar_value: "not reproducible from any statement; AR adjusted net debt (cash and bank only) is 4,503.59 (Rs mn)", note_ref: "C Note 36H p.229; C Note 6 p.211"}
    - {finding_rank: 3, triple_pass_value: "growth 18.9% on AR25 base; base choice drives every trend", ar_value: "numbers verify; cause is pharmacy 338.57 and cafeteria 116.76 now gross, partnership profit 47.43 removed, medical 0.67: exact 408.57. Like-for-like growth 15.2% total, 15.3% hospital services (Rs mn)", note_ref: "C Note 24 p.218 vs AR25 Note 22 p.97"}
missing_risks:
  - {risk: "Capex funding, leverage and floating-rate risk", evidence: "Debt Rs mn 5,085.27, +/-0.5% = 25.43 PBT (C Note 35 p.222); capex 5.73x D&A (AR26 p.193)"}
  - {risk: "Project execution and approvals (Mira Road, BKC)", evidence: "BKC 2030 (AR26 p.7) vs CY31 (Q2 FY27 presentation p.11); Mira Road excavation promise (AR26 p.22)"}
  - {risk: "New-hospital ramp-up losses", evidence: "Dombivli opex loss Rs Cr 9.4 in Q4 FY26 (Q4 FY26 presentation p.7)"}
  - {risk: "Receivable and TPA risk", evidence: "Gross +72.3%, unbilled Rs mn 191.07, ECL on impaired bucket only (C Note 7 p.212; KAM AR26 p.128-129)"}
  - {risk: "Mature-hospital occupancy decline and withdrawn hospital split", evidence: "Occupancy 65.3% to 61.2% (AR26 p.20); AR25 p.5 split dropped"}
  - {risk: "Liquidity concentration in one CP issuer", evidence: "Rs mn 4,857.04 JM Financials Services (C Note 6 p.211)"}
  - {risk: "Revenue-system control gap (HMIS)", evidence: "Auditor paras 19.2, 19.6, 20.8 (AR26 p.131-132)"}
  - {risk: "Medical-negligence litigation vs contingent table", evidence: "RHP p.31: 9 civil cases Rs mn 150.68; AR26 S Note 37B p.171: claims 31.80, insurance 250"}
  - {risk: "Subsidiary exposure on a loss-making JHPPL", evidence: "Cost 939.00 + loan 293.37 + guarantee 2,500 = 3,732.37 Rs mn vs net assets 242.60 (S Note 2, 37K, 37B; C Note 36D p.226)"}
guidance_table:
  - {claim: "Dombivli commissioning (AR25 p.11)", number: "Q1 FY27", timeframe: "delivered 15-Feb-2026", credibility: "high"}
  - {claim: "Dombivli built in just over 25 months (AR26 p.11)", number: "25 months", timeframe: "to Feb 2026", credibility: "low: construction began April 2023 (RHP p.209, AR25 p.4), 34 months"}
  - {claim: "Dombivli on budget, Rs Cr 425 (AR26 p.11)", number: "Rs Cr 425 vs capitalised Rs mn 3,881.3", timeframe: "FY26", credibility: "unverifiable: no budget baseline (NOT FOUND)"}
  - {claim: "Dombivli EBITDA breakeven (AR26 p.12)", number: "end of year 2", timeframe: "Feb 2028", credibility: "medium-high: Q2 FY27 loss Rs Cr 0.2"}
  - {claim: "Pune South on track (AR26 p.22)", number: "500 beds", timeframe: "CY2028", credibility: "high so far"}
  - {claim: "Mira Road excavation before year end (AR26 p.22)", number: "300 beds, Rs Cr 400", timeframe: "excavation CY2026, open 2029", credibility: "low-medium: Oct-2026 still in approval stage"}
  - {claim: "BKC hospital (AR26 p.7)", number: "400 beds", timeframe: "2030", credibility: "medium-low: moved to CY31 in Q2 FY27 presentation"}
  - {claim: "Network of about 3,000 beds (AR26 p.4)", number: "3,000 vs listed sum 2,881", timeframe: "multi-year", credibility: "medium: AR25 target was 2,500"}
  - {claim: "Internal accruals fund the bulk (AR26 p.22)", number: "FY26 CFO 53% of capex", timeframe: "FY27-FY30", credibility: "medium"}
  - {claim: "CAGR 15% revenue, 17% EBITDA, 31% PAT FY21-FY26 (AR26 p.19)", number: "RHP-based 5-year revenue CAGR 25.3%", timeframe: "FY21-FY26", credibility: "low: labels not reproducible"}
monitorables:
  - {metric: "Dombivli quarterly EBITDA", threshold: "positive by Q4 FY27; breakeven by Feb 2028 per AR26 p.12", where: "quarterly presentation EBITDA footnote", why: "tests the ramp"}
  - {metric: "Ex-Dombivli occupancy", threshold: "at least 65% (H1 FY27 64.8%)", where: "quarterly presentation operating metrics", why: "mature-hospital demand and dropped split"}
  - {metric: "Capital commitments and capitalised borrowing cost", threshold: "disclosed; commitments at least Rs Cr 890-900 plus BKC 354 plus Pune land 100", where: "FY27 AR notes", why: "funding need"}
  - {metric: "Total debt / EBITDA", threshold: "under 1.8x (Sep-2026 1.64x ex-leases, 1.86x with leases, derived)", where: "quarterly balance sheet and EBITDA", why: "ICRA downgrade trigger"}
  - {metric: "Receivable days", threshold: "at or below 18.4 (Sep-2026 about 24.7, derived)", where: "quarterly balance sheet", why: "cash conversion"}
  - {metric: "CFO / EBITDA", threshold: "at least 80% (FY26 78.0%)", where: "half-year cash flow", why: "profit quality"}
  - {metric: "Quarterly D&A and finance cost", threshold: "D&A Rs Cr 28.5 and finance Rs Cr 13.8 as base", where: "quarterly results", why: "squeeze run-rate"}
  - {metric: "HMIS audit trail", threshold: "no exception in FY27 auditor report", where: "FY27 AR auditor report", why: "revenue system control"}
  - {metric: "Promoter holding and pledge", threshold: "at least 40.91%, no pledge", where: "quarterly shareholding pattern", why: "alignment"}
  - {metric: "CP issuer share of liquid assets", threshold: "under 50% (FY26 89.3%)", where: "AR Note 6", why: "liquidity buffer"}
ar_new_downstream_entities:
  - {name: "Mumbai Metropolitan Region Development Authority (MMRDA)", where_in_ar: "S Note 1A p.144 (agreement to take BKC land on 80-year lease); lease premium about Rs Cr 354 is in the 27-Mar-2026 Reg 30 filing, not the AR", entity_type: "land lessor, statutory authority"}
  - {name: "KKC & Associates LLP", where_in_ar: "Directors' Report p.89; Auditor's Report p.132", entity_type: "joint statutory auditor from FY26"}
  - {name: "Mr. Anshul Sethi", where_in_ar: "C Note 36K p.232 (professional fees Rs mn 3.06; relationship not stated)", entity_type: "related-party payee"}
  - {name: "Mr. Rajendra Thakkar", where_in_ar: "C Note 36K p.231-232 (Director of Jupiter Hospital Pharmacy Pvt Ltd; professional fees Rs mn 3.38)", entity_type: "related-party payee"}
  - {name: "Medical college (unnamed CSR beneficiary)", where_in_ar: "Annexure V p.122; CSR text p.30", entity_type: "CSR recipient, name NOT FOUND"}
strengths_top3:
  - "Mature-hospital EBITDA margin held: derived ex-Dombivli 23.5% vs 23.0% while ARPOB rose 11.7% (Q4 FY26 presentation p.7; AR26 p.20)"
  - "Delivery against guidance: Dombivli opened ahead of the AR25 Q1 FY27 date; Pune South construction on the AR25 schedule (AR25 p.11; AR26 p.43)"
  - "Clean statutory record: unmodified opinion, no CARO adverse remark, no default, contingent liabilities 0.32% of net worth, ICRA AA- Stable (AR26 p.92, p.133-136)"
red_flags_top3:
  - "No capital commitments, capitalised interest or BKC premium (about Rs Cr 354) in the notes while debt rose 56% to Rs mn 5,085.27 (S Note 37B p.171; C Note 14 p.215)"
  - "Hospital-wise occupancy dropped in the year network occupancy fell 4.1 pts; receivables +72.3%; HMIS audit-trail exception on the revenue system (AR25 p.5; C Note 7 p.212; AR26 p.132)"
  - "Front pages mix bases and misstate facts: FY25 EBITDA margin 23.50% vs 23.04%; 25 months vs April 2023 start; Rs 6.4 Cr vs Rs mn 48.87 exceptional (AR26 p.19, p.11, p.31)"
best_fit_strategy: "Capex-Led Growth (WATCHLIST)"
one_line_verdict: "A well-run hospital operator whose mature margin held and whose build is on schedule, but whose commitments, hospital-wise data and front-page labels are thinner than the notes."
analyst_note: "The FY25 re-cut is fully explained: pharmacy 338.57 and cafeteria 116.76 now gross, partnership profit 47.43 removed, medical 0.67, total 408.57 Rs mn. Like-for-like growth is 15.2%, not 18.9%. The p.19 chart compares FY25 margin on the old basis (23.50%) with FY26 on the new (22.89%); like for like it is 23.04% vs 22.89%. The profit squeeze sits below EBITDA: 41% of the D&A rise is leasehold-land amortisation and 84% of the finance rise is JHPPL's Rs mn 2,500 loan drawn in FY25. Derived ex-Dombivli margin rose to 23.5%. Dombivli completion was announced 30-Jan-2026 and ran from 15/25-Feb-2026; 25 months conflicts with the April 2023 start. BKC's Rs Cr 354 premium and the Pune land purchase sit outside ICRA's Rs Cr 890-900 plan. Per-share figures are pre-split (FV Rs 10); split is 5 for 1."
```
