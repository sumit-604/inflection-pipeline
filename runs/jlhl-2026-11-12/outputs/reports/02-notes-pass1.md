# STAGE 2 NOTES, PASS 1 (FULL EXTRACTION): JLHL, run 2026-11-12

Source: inputs/annual-report/Annual_Report_2026.pdf (text: Annual_Report_2026.txt). Backward baseline: Annual_Report_2025.pdf.
Notes read: Standalone Note 1 to Note 37 (PDF pp.144-182) and Consolidated Note 1 to Note 36 (PDF pp.196-235). Statements, auditor report and CARO annexure read where a note cross-refers to them.
UNIT RULE: every figure is INR million (Rs mn, 10 million = 1 Crore) as printed on the face of the financial statements, unless marked "Rs" (per-share, per-bed) or "%". Stage 10 converts once. Where the brief quotes Crore, the check line shows the source million figure and says so.
Anchor form: (S = Standalone, C = Consolidated; Note number; Annual_Report_2026.pdf page).
"Derived" = arithmetic on disclosed figures only; the inputs are cited. Nothing is estimated. [INFERENCE] marks reasoning beyond the filed text.
B00 input_gaps carried: none of them touches the AR notes. The AR text is complete (237 pages, no scanned pages in the notes range).

---------------------------------------------------------------------
## 0. SCOPE FACTS THAT CHANGE HOW TO READ THE NOTES

0.1 Two note sets exist. Standalone (parent only) has 37 notes; Consolidated has 36. The group figures (what the market calls "JLHL") are the Consolidated set. Standalone revenue is not comparable year on year, because the pharmacy business moved into subsidiary Jupiter Hospital Pharmacy Pvt Ltd (95%): S pharmacy sales Rs mn 1.15 vs C pharmacy sales Rs mn 391.92 (S Note 25 p.166; C Note 24 p.218; conversion note S Note 37D p.174). 🟡
0.2 Auditors: FY26 report is by two joint auditors, KKC & Associates LLP and Aswin P. Malde & Co. (Auditor's Report para 16, p.130). FY25 was audited by Aswin P. Malde & Co. alone (Annual_Report_2025.pdf p.63 signature block; AR26 p.130 "one of the joint statutory auditors"). Auditor remuneration rose from Rs mn 3.00 to Rs mn 5.70 (S Note 33 p.168) and Rs mn 4.00 to Rs mn 6.70 (C Note 32 p.220). 🟡
0.3 Reporting basis: face value Rs 10, 65,566,022 shares (S Note 13 p.161; C Note 12 p.213). No stock-split reference exists anywhere in the AR text (searched "sub-division", "stock split", "split of": no hits). All per-share figures here are on the Rs 10 basis. 🟡 (basis flag for B00 corporate_action_note)

---------------------------------------------------------------------
## 1. ACCOUNTING POLICIES AND CHANGES

| # | Finding | Anchor | Rating |
|---|---|---|---|
| 1.1 | No policy change disclosed. "The Company has uniformly applied the accounting policies during the year presented." | S Note 1 D p.153; no new-standard adoption; "no standards issued but not yet effective that will impact" (S Note 37P(i) p.182) | 🟢 |
| 1.2 | Useful lives (years): buildings 60; plant and machinery 15; electrical 10; medical equipment and accessories 3-10; medical and surgical instruments 3-5; office equipment 5; furniture 10; IT 3-6; vehicles 8; ambulance 6; wind generator 22; solar 25. Management states some lives are "at variance with Part C of Schedule II", set on past experience and an independent valuation expert. Lives reviewed at least each year, prospective effect. No change in lives disclosed. | S Note 1 C.2 p.145 (C Note 1 C.2 pp.197-198) | 🟢 (medical equipment lives 3-10 are the short end; Schedule II comparison value is external to the document and not tested here) |
| 1.3 | Capitalisation threshold: NOT FOUND IN DOCUMENT. | S/C Note 1 | 🟡 |
| 1.4 | Borrowing-cost policy: costs directly attributable to qualifying assets are capitalised from first expenditure until the asset is ready for use; capitalisation suspends in extended pauses. The AMOUNT capitalised in FY26 or FY25 is NOT FOUND IN DOCUMENT in any note (searched all notes). | S Note 1 C.4 pp.145-146; no quantum anywhere | 🔴 for a hospital build year (see section 12.1) |
| 1.5 | Pre-operative expense policy: NOT FOUND IN DOCUMENT. The only rule is PPE "cost comprises ... any directly attributable cost of bringing the asset to its working condition". No pre-operative amount appears in Note 1.1, CWIP, or Other expenses. | S Note 1 C.1 p.144 | 🟡 |
| 1.6 | Revenue policy has an internal tension. Point-in-time recognition ("when each performance obligation is satisfied at a point in time when inpatient/outpatients has actually received", p.147), but unbilled revenue for patients not yet discharged is recognised "based on the services rendered ... up to the reporting date", and Key Judgements say performance obligation satisfaction is "over time" (p.154). Rev rec for undischarged inpatients is therefore accrual by service rendered. | S Note 1 C.7 pp.147-148; D(i) pp.153-154 | 🟡 |
| 1.7 | Rental income and share of partnership-firm profit are policy items. Policy says firm income is booked "based on audited financials of the firms" (p.148), but the auditor reports one partnership firm's share of net loss, Rs mn 2.62, rests on UNAUDITED statements (Auditor's Report para 17, pp.130-131). Immaterial per auditor. | S Note 1 C.7(vii) p.148; Auditor para 17 | 🟡 |
| 1.8 | ECL: simplified approach, provision matrix built on historical default rates, updated for forward-looking estimates. The matrix rates themselves are NOT FOUND IN DOCUMENT. Auditors made receivables, reconciliation and provisioning a Key Audit Matter (claim adjudication, contractual deductions, TPA denials). | S Note 1 C.20 p.152; KAM at C auditor's report pp.183-184 | 🟡 |
| 1.9 | Impairment policy: VIU with pre-tax discount rate, or FVLCD. No test results, growth rates or discount rates disclosed for any CGU or for the Rs mn 939.00 investment in subsidiary JHPPL. | S Note 1 C.5 p.146; S Note 2 p.158 ("impairment ... nil") | 🟡 |
| 1.10 | Ind AS 116: lessee lease liability discounted at the incremental borrowing rate; the rate is NOT FOUND IN DOCUMENT. Lease term, extension judgement: NOT FOUND. Lease numbers in section 12.7. | S Note 1 C.19 p.151 | 🟡 |
| 1.11 | Gratuity described as "unfunded defined benefit plan" in the Note text, yet the same note shows plan assets of Rs mn 86.83 (S) and Rs mn 103.91 (C) and employer contributions of Rs mn 25.42 (S) and Rs mn 35.91 (C). The wording contradicts the numbers. | S Note 37C p.172 vs table p.173; C Note 36C | 🟡 |
| 1.12 | Hotel: a Fortune Park hotel in Thane for medical tourism sits inside the hospital entity; revenue Rs mn 107.80 (FY25 Rs mn 103.71), below the 10% segment test, so no segment note. Single segment "Medical and Healthcare Services", single geography India. | S Note 1 C.16 p.150; S Note 37M p.181; C Note 36M p.234 | 🟢 |

---------------------------------------------------------------------
## 2. RELATED PARTY TRANSACTIONS

Related parties named (C Note 36K pp.231-233; S Note 37K pp.178-180): subsidiaries JHPPL (96.56%), Medulla Healthcare Pvt Ltd (100%), Jupiter Hospital Pharmacy Pvt Ltd (95%) (C Note 1 B(iii) p.196); partnership firms Jupiter Gait Lab (dissolved 3-Jun-2025), Mangleshwar Hospitality and Vishesh Jupiter Pharmacy (both dissolved 1-Aug-2025), Katyayini Hospitality, Jupiter Pharmacy (converted to Jupiter Hospital Pharmacy Pvt Ltd, Mar 2025); KMP and directors; promoter-controlled Entisi Hospitality Pvt Ltd, Jupiter Scan & Imaging Centre Pvt Ltd, Jupiter Foundation; relative Mr. Devang Gandhi (brother-in-law of Dr. Ajay Thakker).

### 2.1 Consolidated RPT table (Rs mn), C Note 36K(ii) p.232

| Party | Relationship | Nature | FY26 | FY25 | YoY |
|---|---|---|---|---|---|
| Entisi Hospitality Pvt Ltd | Promoter-controlled | Purchase of goods | 8.71 | 4.98 | +74.9% |
| Mr. Harshad Purani | CFO (to 12-May-25) | KMP remuneration | 8.24 | 8.21 | +0.4% |
| Ms. Suma Upparatti | Company Secretary | KMP remuneration | 3.80 | 3.53 | +7.6% |
| Mr. Sivasis Sen | CFO (from 12-May-25) | KMP remuneration | 12.21 | nil | new |
| Dr. Ajay Thakker | Chairman and MD (promoter, 20.74%) | Director remuneration | 41.99 | 38.88 | +8.0% |
| Dr. Ankit Thakker | MD and CEO (promoter, 6.67%) | Director remuneration | 39.00 | 31.91 | +22.2% |
| Dr. Rajesh Kasliwal | MD of JHPPL | Director remuneration | 15.41 | 14.24 | +8.2% |
| Jupiter Hospital Pharmacy Pvt Ltd | Subsidiary | Space given on lease | 2.45 | 1.65 | +48.5% |
| Katyayini Hospitality | Partnership firm (95%) | Space given on lease | 0.93 | 0.48 | +93.8% |
| Mr. V. Raghavan | Non-exec director | Professional fees | 5.66 | 5.37 | +5.4% |
| Dr. Bhaskar Shah | Non-exec director | Professional fees | 4.93 | 5.09 | -3.1% |
| Mr. Devang Gandhi | Relative of promoter | Professional fees | 3.00 | 2.40 | +25.0% |
| Mr. Anshul Sethi | not described | Professional fees | 3.06 | nil | new party |
| Mr. Rajendra Thakkar | Director, Jupiter Hospital Pharmacy | Professional fees | 3.38 | nil | new party |
| Five independent directors | Independent directors | Sitting fees | 0.52 (0.09+0.08+0.14+0.15+0.06) | 0.47 | +10.6% |
| Jupiter Scan & Imaging Centre | Promoter-controlled | Space taken on lease | 0.48 | 0.48 | 0% |
| Jupiter Gait Lab | Partnership firm | Profit transfer from firm | 2.84 | 2.84 | 0% |
| Jupiter Foundation | Promoter-controlled | Donation and CSR | 15.69 | 28.30 | -44.6% |

(YoY % derived.) Consolidated FY25 prior-year figure for Dr. Ankit Thakker is Rs mn 31.91, but the Standalone FY25 figure is Rs mn 25.92 (S Note 37K(ii) p.179), a Rs mn 5.99 gap in one person's remuneration across two sets of statements for the same year. Reason NOT FOUND. 🟡

### 2.2 Standalone-only RPT lines (Rs mn), S Note 37K(ii)-(iii) pp.179-180
- Loans given to subsidiary JHPPL: FY26 120.00, FY25 173.37. Repayment of loan by JHPPL: FY26 nil, FY25 2,500.00.
- Outstanding loan/receivable, JHPPL: 293.37 (FY25 173.37). Medulla Healthcare: 28.85 (FY25 28.84). Katyayini Hospitality: 9.50 (FY25 6.24). Sum JHPPL + Medulla = 322.22 = "Loan to related parties" 322.21 (S Note 10 p.160).
- Reimbursement received from Jupiter Hospital Pharmacy: 5.00 (FY25 11.45). Current-support advances to Jupiter Hospital Pharmacy 5.00 (FY25 nil) and to Katyayini 9.50 (FY25 nil).
- Profit transfer from Jupiter Pharmacy partnership: 46.34 (FY25 nil in this table; closing FY25 other receivable 46.34).
- Purchases from Entisi Hospitality: 6.47 (4.98). Sale to JHPPL: 1.11 (2.07).
- Investment in JHPPL: 939.00 unchanged (S Note 2 p.158).

### 2.3 Signals
- RPTs as % of consolidated revenue (derived): promoter, KMP, director, relative and promoter-entity items in 2.1 sum to Rs mn 172.30 against revenue Rs mn 14,997.87 = 1.15%. Intra-group items eliminate on consolidation and are excluded.
- Promoter-family pay (Ajay + Ankit): C Rs mn 80.99 FY26 vs 70.79 FY25 (+14.4%, consolidated FY25 basis); S Rs mn 80.99 vs 64.80 (+25.0%). Consolidated PAT moved +0.2% (Rs mn 1,941.87 vs 1,937.54). Auditor states Section 197 limits are met (Auditor's Report para 19.8, p.131). 🟡
- Loans to promoter entities: none. CARO iii(f) confirms no loans to promoters; loans to related parties Rs mn 120.00 given in the year, all repayable on demand (CARO p.134). Interest rate, if any, on the loans to JHPPL (293.37) and Medulla (28.85): NOT FOUND IN DOCUMENT. 🟡
- Medulla Healthcare: loan Rs mn 28.85 against a subsidiary net asset of Rs mn (0.16) (C Note 36D p.226); recoverability note NOT FOUND; merger into parent pending NCLT (S Note 37N p.181). 🟡
- Corporate guarantee: Rs mn 2,500 for JHPPL's HDFC loan (S Note 37B p.172; CARO iii(a) p.133, also "balance outstanding 2,500.00"). Release if 50% repaid or JHPPL Debt/EBITDA below 3.5x for four straight quarters. 🟡
- Lease payments to promoter entity: Rs mn 0.48 per year at Jupiter Scan & Imaging. Immaterial. 🟢
- Auditor CARO xiii: RPTs comply with Sections 177 and 188 (p.135). 🟢
- Related-party trade payables: Rs mn 0.14 (FY25 Rs mn 0.30) (S Note 21 p.165). 🟢

---------------------------------------------------------------------
## 3. CONTINGENT LIABILITIES

### 3.1 Table (Rs mn), C Note 36B pp.222-223 (S Note 37B pp.171-172)

| Nature | C FY26 | C FY25 | S FY26 | S FY25 | Stage | Company assessment |
|---|---|---|---|---|---|---|
| Claims against the Company (not provided for) | 31.80 | 31.80 | 31.80 | 31.80 | "various pending litigations"; nature and forum NOT FOUND IN DOCUMENT | "possible but not probable"; insurance of Rs mn 250 held "towards such matter" |
| Indirect tax (service tax) | 4.42 | 4.42 | 4.42 | 4.42 | Appeal at CESTAT Mumbai; hearing not yet scheduled; Apr 2019 to Mar 2024 (CARO vii(b), p.134) | No material adverse impact expected |
| Indore Municipal Corporation property tax | 13.04 | 13.04 | n/a | n/a | Notice to subsidiary; Rs mn 12.37 paid under dispute, shown as deposit with government authority | Decision pending |
| Total | 49.26 | 49.26 | 36.22 | 36.22 | | |

- Total as % of net worth (derived): C 49.26 / 15,440.93 = 0.32%; S 36.22 / 16,075.57 = 0.23%. No single item above 10% of net worth in the table. 🟢
- The Rs mn 2,500 guarantee for JHPPL is NOT in the contingent table; it is disclosed in prose (S Note 37B p.172) and CARO. As % of standalone net worth: 2,500 / 16,075.57 = 15.55% (derived). It repays through a loan already on the consolidated balance sheet (C Note 14 p.215). 🟡
- All three amounts are identical to FY25. No movement for a full year, no stage progress on the claims, and the claim's nature is not stated. 🟡
- Tax dispute composition: service tax only. No income-tax or GST disputes listed (CARO vii(b)). 🟢
- Capital commitments: heading reads "Contingent liabilities and commitments" but NO commitment figure appears (S Note 37B; C Note 36B). NOT FOUND IN DOCUMENT. See 12.3. 🔴

---------------------------------------------------------------------
## 4. TRADE RECEIVABLES

### 4.1 Ageing, consolidated (Rs mn), C Note 7 p.212

| Bucket (from due date) | FY26 good | FY26 credit-impaired | FY25 good | FY25 credit-impaired |
|---|---|---|---|---|
| Unbilled | 191.07 | nil | nil (no unbilled column populated) | nil |
| Not due | nil | nil | nil | nil |
| Less than 6 months | 540.21 | 7.02 | 410.41 | 1.36 |
| 6 months to 1 year | 24.11 | 5.02 | 21.92 | 4.22 |
| 1-2 years | nil | 18.64 | nil | 20.31 |
| 2-3 years | nil | 6.15 | nil | 1.45 |
| More than 3 years | nil | nil | nil | nil |
| Gross | 755.39 + 36.83 = 792.22 | | 432.33 + 27.34 = 459.67 | |
| ECL allowance | (36.83) | | (27.34) | |
| Net | 755.39 | | 432.33 | |

Standalone (S Note 7 pp.159-160): gross 704.45 (FY25 396.18); allowance 33.06 (FY25 18.42); net 671.39 (FY25 377.76); unbilled 191.07 (all the unbilled sits in the parent).

Derived metrics, consolidated:
- Gross receivables +72.3% (792.22 vs 459.67) against revenue +15.2% (14,997.87 vs 13,024.02, C Note 24 p.218). Net receivables +74.7% (755.39 vs 432.33).
- Net receivable days on year-end balance: 755.39 / 14,997.87 x 365 = 18.4 days; FY25 432.33 / 13,024.02 x 365 = 12.1 days. Company's own turnover ratio on average balances: 17.68x (20.6 days) vs 20.35x (17.9 days) (C Note 36L p.233).
- Share of gross over 6 months: (29.13 + 18.64 + 6.15) = 53.92 = 6.8% of 792.22; FY25 (26.14 + 20.31 + 1.45) = 47.90 = 10.4% of 459.67.
- ECL stock as % of gross: 4.65% (FY25 5.95%). Credit-impaired under 6 months rose from 1.36 to 7.02 (5.2x).
- Unbilled Rs mn 191.07 = 24.1% of gross receivables. The FY25 ageing table shows no unbilled amount although the policy says unbilled revenue sits in current financial assets. Either FY25 unbilled sat inside "less than 6 months", or it did not exist. Comparability gap. 🟡
- Three-year trend: Mar 2024 net receivables C Rs mn 572.13, S Rs mn 463.54 (Annual_Report_2025.pdf: C BS p.85, S BS p.63); Mar 2025 C 432.33 and S 377.76 as printed in the FY26 AR (but see section 11.2, FY25 AR printed C 418.90 and S 365.56); Mar 2026 C 755.39 and S 671.39. Direction: down in FY25, sharply up in FY26. 🟡
- No customer above 10%: NOT FOUND IN DOCUMENT for customers by name or payer class; Note 35 says "no significant concentration of credit risk" (C Note 35 p.221). Payer mix (insurer, TPA, government scheme, self-pay) NOT FOUND IN DOCUMENT. 🟡
- Related-party receivables: C Rs mn 1.31 total (Katyayini 0.22, Jupiter Pharmacy 0.30, Mangleshwar 0.10, Vishesh 0.69) (C Note 36K(iii) pp.232-233). 🟢
- Reconciliation of ECL: allowance movement C 36.83 - 27.34 = 9.49, equal to the cash-flow add-back "Allowance and provision for doubtful debts" 9.49 (C CF p.193), but Note 32 P&L line "Provision for doubtful debts" is 12.37 (p.220); S: movement 14.64 = CF 14.64, P&L line 17.52 (S Note 33 p.168). The same Rs mn 2.88 gap in both sets is unexplained. Bad debts written off: C 10.49, S 3.87 (separate P&L line). 🟡

---------------------------------------------------------------------
## 5. INVENTORY

| Item | C FY26 | C FY25 | S FY26 | S FY25 | Anchor |
|---|---|---|---|---|---|
| Pharmacy, medical, surgical, consumables stock (single category) | 383.36 | 264.61 | 285.13 | 181.73 | C Note 5 p.211; S Note 5 p.159 |
| Change in inventories (P&L) | (118.75) | (26.88) | (103.40) | (14.08) | C Note 27 p.219; S Note 28 p.167 |
| Purchases of consumables | 2,991.43 | 2,581.70 | 2,236.18 | 1,925.91 | C Note 26; S Note 27 |

- Inventory +44.9% (C) and +56.9% (S) against revenue +15.2% (C) and +13.0% (S, 11,976.24 vs 10,600.65). 🟡
- Consumption (derived) C 2,991.43 - 118.75 = 2,872.68 (FY25 2,554.82). Inventory days on consumption: 48.7 (FY25 37.8). 🟡
- No finished-goods category; hospital stock only. Write-downs, NRV adjustments, obsolescence: NOT FOUND IN DOCUMENT. Valuation FIFO, lower of cost and NRV (S Note 1 C.6 p.146).
- Cause of the build (Dombivli opening stock, new pharmacy) is NOT FOUND IN DOCUMENT in the notes. [INFERENCE] a new 287-bed site needs initial stock; not confirmed by a note.
- Auditor: physical verification discrepancies below 10% per class (CARO ii(a), p.133). 🟢

---------------------------------------------------------------------
## 6. INVESTMENTS, SUBSIDIARIES, LOANS

### 6.1 Subsidiaries and firms (S Note 2 p.158; S Note 37D p.174; C Note 36D pp.226-227)

| Entity | Holding | Parent carrying value (Rs mn, cost) | FY26 share of group profit (Rs mn) | Net assets (Rs mn) |
|---|---|---|---|---|
| Jupiter Hospital Projects Pvt Ltd (JHPPL), "material subsidiary" | 96.56% (77,250,000 sh; face Rs 772.5 mn of Rs 800 mn) | 939.00 | (34.29) loss; FY25 +88.01 | 242.60 (FY25 276.28) |
| Medulla Healthcare Pvt Ltd | 100% | 0.10 | (0.02) | (0.16) |
| Jupiter Hospital Pharmacy Pvt Ltd | 95% | 0.10 | 62.52; FY25 48.52 | 63.62 (FY25 48.52) |
| Katyayini Hospitality (partnership, net-income basis) | 95% | 0.10 | (2.76); FY25 +1.51 | 5.24 |
| Jupiter Gait Lab, Mangleshwar Hospitality, Vishesh Jupiter Pharmacy | dissolved 2025 | nil | nil | nil |

- JHPPL: parent cost Rs mn 939.00 against subsidiary net assets Rs mn 242.60 (3.9x, derived) and a FY26 loss of Rs mn 34.29. Impairment assessment, recoverable amount, or business description of JHPPL: NOT FOUND IN DOCUMENT in the notes ("Aggregate amount of impairment ... nil", S Note 2 p.158). 🟡
- JHPPL swing: profit 88.01 to loss (34.29). Consolidated term-loan interest 204.40 less parent 15.15 = 189.25 sits in the subsidiaries (derived, from C Note 30 p.219 and S Note 31 p.167); that matches JHPPL's Rs mn 2,500 HDFC loan, Repo + 200 bps, 144 monthly instalments from Apr 2025 to Mar 2037 (C Note 14 p.215). 🟡
- Consolidated NCI is negligible: Rs mn 0.09 (FY25 0.62). NCI profit 1.81 (FY25 5.54) (C P&L p.192).
- Medulla merger: scheme with parent, effective 1-Apr-2025, "pending final sanction" of NCLT Mumbai; effect not given, "being not material" (S Note 37N p.181; C Note 36N p.234). The 18-Nov-2025 NCLT order in inputs/announcements modified creditor-notice directions only; the scheme is not sanctioned. Consistent. 🟢

### 6.2 Other investments
- Non-current: co-operative bank shares at cost: New India Co-operative Bank Rs mn 0.50 (50,000 sh), Thane Janta Sahakari Bank Rs mn 0.50 (9,999 sh) (S Note 2 p.158; C Note 2 p.210). 🟢
- Current investments (C Note 6 p.211): commercial papers of JM Financial Services Ltd (quoted) Rs mn 4,857.04 (FY25 3,981.17); mutual fund Tata Ultra Short Term Fund nil (FY25 1,086.42). Total C Rs mn 4,857.04 vs 5,070.98.
- Concentration (derived): C Rs mn 4,857.04 / (4,857.04 + cash 547.61 + other bank balances 34.07 = 5,438.72) = 89.3% of group liquid assets sits in one issuer's paper. Note 35 says "other financial assets are bank deposits with banks and hence the Group does not expect any credit risk" (C Note 35 p.221), which does not describe commercial paper. 🟡
- Fair-value movement: gain on sale of investments Rs mn 131.46 (FY25 44.64); fair-value loss (18.57) reversing FY25 gain 18.57 (C Note 25 p.218). 🟡
- Fair value hierarchy (Level 1/2/3) table: NOT FOUND IN DOCUMENT. Note 36I presents only classification by category, with CPs at "amortised cost" (C p.229) while Note 6 heads them "carried at Fair Value through Profit and Loss". Contradiction. 🟡

### 6.3 ICDs and loans given
- Only intra-group: S Note 10 p.160 loans Rs mn 322.21 (FY25 202.47), 100% related parties, unsecured, repayable on demand. Advance to JHPPL for "business support". Rate and tenure NOT FOUND. Auditor: terms "not prejudicial" (CARO iii(b), p.133). Consolidated: nil (eliminated).

---------------------------------------------------------------------
## 7. BORROWINGS

### 7.1 Instrument table (Rs mn), C Note 14 p.215, S Note 15 p.163

| Instrument | Lender | Sanctioned | Drawn at 31-Mar-26 | Rate | Tenor | Security |
|---|---|---|---|---|---|---|
| Term loan, parent | HDFC Bank | 3,500 | 2,620 "availed" (S carrying 2,584.12 non-current + 26.20 current = 2,610.32) | Repo + 200 bps, floating | 180 monthly instalments, Apr 2025 to Mar 2040 | Exclusive mortgage/charge on Dombivli hospital immovables; exclusive hypothecation of Dombivli movables; second pari passu on current assets and receivables |
| Term loan, JHPPL | HDFC Bank | 2,500 | 2,500 | Repo + 200 bps, floating | 144 monthly instalments, Apr 2025 to Mar 2037 | First mortgage on JHPPL immovables; exclusive hypothecation of tangible movables; second pari passu on current assets. Parent corporate guarantee Rs mn 2,500 (S Note 37B p.172) |

- Consolidated: non-current 5,008.97 (FY25 3,217.45); current 76.30 (FY25 39.68); gross debt 5,085.27 (FY25 3,257.13) (C Note 36H p.229). Standalone gross debt 2,610.32 (FY25 750.00) (S Note 37H p.176).
- Parent roll-forward ties: 750.00 + proceeds 1,867.82 - repayment 7.50 = 2,610.32 (S CF p.142). The 2,620 "availed" vs 2,610.32 carrying leaves Rs mn 2.18 net after repayment; presumed unamortised cost, not stated. Undrawn on parent sanction: 3,500 - 2,620 = 880 (derived).
- Mar 2024 balance nil: Annual_Report_2025.pdf standalone BS p.63 ("Borrowings 16: nil"). Check on the brief: Rs 0 (Mar 2024) agrees.
- Check on the brief's "about Rs 584 Cr" (March 2026): gross debt 5,085.27 + lease liabilities 757.13 (C Note 36J p.230) = 5,842.40 Rs mn, which is the figure the brief reads as Rs 584 Cr. Borrowings alone are Rs mn 5,085.27 (the brief figure includes leases). 🟡 flag for B00 fact 3.
- Floating, both loans. Interest sensitivity +/-0.50% = Rs mn 13.05 (S) and Rs mn 25.43 (C) on PBT (S Note 36 p.171; C Note 35 p.222). Consolidated text just above says "Since the Group has insignificant interest bearing borrowings, the exposure ... is minimal" (C Note 35 p.222), contradicting Rs mn 5,085 of floating debt. 🟡
- Covenants: NOT FOUND IN DOCUMENT (generic reference to "financial covenants" in capital management only, S Note 37H p.176). Breach or waiver: none disclosed; CARO ix(a) says no default on repayment (p.134). Term changes: none disclosed.
- Maturity buckets (C Note 35 p.222): non-current borrowings 1-3 years 307.20; over 3 years 4,701.77; current 76.30. S (p.170): 1-3 years 157.20; over 3 years 2,426.92; current 26.20. Year-wise five-year schedule: NOT FOUND IN DOCUMENT. The repayment profile is back-ended: FY26 repayment was Rs mn 7.50 (S) or 32.55 (C CF p.194) on a loan that began instalments in Apr 2025.
- Related-party borrowings: none (CARO ix(e): no funds taken to meet subsidiaries' obligations, p.135).
- Use of proceeds: term loans applied for purpose (CARO ix(c), p.135); no short-term funds used long-term (ix(d)).
- Working-capital limits above Rs 5 crore secured on current assets exist; no quarterly returns required (CARO ii(b), p.133). Sanctioned amount, utilisation: NOT FOUND.
- Debt service coverage ratio: C 36.58 vs 87.01; S 87.27 vs 363.52 (C Note 36L p.233; S Note 37L p.180). Net debt as company defines it (debt less cash and bank, excluding the commercial paper): C Rs mn 4,503.59 (FY25 2,307.31), ratio 0.29x (0.17x) (C Note 36H p.229). With the CP counted as liquid, group is net cash: 4,857.04 + 547.61 + 34.07 - 5,085.27 = Rs mn 353.45 (derived), against Rs mn 2,763.67 net cash at Mar 2025 (6,020.80 - 3,257.13, derived). 🟡
- Negative carry [INFERENCE]: the group holds Rs mn 4,857.04 of CP while carrying Rs mn 5,085.27 of Repo + 200 bps debt. Interest income on investments Rs mn 245.15 (C Note 25) against term-loan interest Rs mn 204.40 (C Note 30) are both in the filed numbers; the yield on CP is not stated.

---------------------------------------------------------------------
## 8. TRADE PAYABLES

### 8.1 Table, C Note 20 p.216 (Rs mn)

| | Not due + unbilled | Overdue less than 1 year | 1-2 years | 2-3 years | Total |
|---|---|---|---|---|---|
| MSME FY26 | 2.96 unbilled + 230.89 not due | 69.90 | nil | nil | 303.75 |
| Others FY26 | 0.49 + 539.81 | 97.49 | 13.85 | nil | 651.64 |
| Total FY26 | 3.45 + 770.70 | 167.39 | 13.85 | nil | 955.39 |
| Total FY25 (as printed in FY26 AR) | 67.98 not due | 622.80 | 0.20 | nil | 690.98 |

- Payables +38.3% (955.39 vs 690.98) against revenue +15.2%. MSME dues +188% (303.75 vs 105.48). 🟡
- Overdue (past due date) 181.24 = 19.0% of payables (derived: 167.39 + 13.85). MSME overdue 69.90 = 23.0% of MSME dues.
- MSMED interest: nil on every line, both years, despite Rs mn 69.90 MSME dues sitting past their due date (C Note 36E p.228; S Note 37E p.175: S MSME overdue 68.15). Either "due date" in the ageing table is not the statutory 45-day date, or interest is not provided. 🟡
- FY25 ageing shows everything as "less than 1 year" with no "not due" split; FY26 introduces the split. Comparability gap. 🟡
- Payable turnover (company ratio, purchases / average payables): C 3.63x vs 4.32x, i.e. 100.6 days vs 84.5 days (derived from ratio) (C Note 36L p.233). 🟡
- MSME classification "based on information available with the Company" (S Note 21 p.165). Related-party payable Rs mn 0.14. Capital creditors are NOT in trade payables: they sit in other financial liabilities, C Rs mn 509.70 (FY25 355.43) (C Note 21 p.217); this is a reclassification versus FY25 AR (section 11.2).

---------------------------------------------------------------------
## 9. PROVISIONS

- Only employee-benefit provisions exist. No warranty, decommissioning, onerous-contract or litigation provision. Litigation: contingent only (section 3). NOT FOUND IN DOCUMENT for any other provision.
- C non-current provisions 164.61 (FY25 112.21); current 92.01 (FY25 20.23) (C Notes 16, 23 pp.216, 218). S non-current 152.24 (105.42); current 62.88 (56.14) (S Notes 17, 24).
- Mismatch to flag now, detail in 11.3: FY25 consolidated current provision 20.23 is lower than the parent's own FY25 current provision 56.14. A consolidation cannot be lower than the parent. 🟡
- Gratuity (S Note 37C pp.172-174; C Note 36C pp.223-225), Rs mn:

| | S FY26 | S FY25 | C FY26 | C FY25 |
|---|---|---|---|---|
| Defined benefit obligation, year end | 128.29 | 86.97 | 149.20 | 96.13 |
| Plan assets | 86.83 | 66.57 | 103.91 | 66.57 |
| Net liability | 41.46 | 20.40 | 45.29 | 29.56 |
| Past service cost in year | 34.44 | 2.98 | 37.52 | 2.98 |
| Employer contributions | 25.42 | 0.40 | 35.91 | 0.40 |
| Discount rate | 7.22% | 6.72% | 7.11-7.22% | 6.72-6.75% |
| Salary escalation | 7.00% | 7.00% | 7.00% | 7.00% |
| Expected return on assets | 6.50% | 6.50% | 6.50% | 6.50% |

- Sensitivity: discount rate +1% gives obligation 118.13 (S) / 139.48 (C); -1% gives 139.85 (S) / 160.61 (C). Salary +1% gives 140.27 (S) / 163.17 (C). (S p.174; C p.225.) Maturity: above 10 years bucket 172.33 (S) / 207.04 (C). Average expected future working life 6.84 years (S) vs 8.56 (FY25). 🟢
- Labour Codes (notified 21-Nov-2025): past service cost booked as an Exceptional Item, S Rs mn 43.89 and C Rs mn 48.87, "net of subsequent reversal upon actualisation of charge", treated as non-recurring (S Note 37A p.171; C Note 36A p.222). The gratuity table's past service cost is S 34.44 and C 37.52; the remaining S 9.45 and C 11.35 is not reconciled in any note. [INFERENCE] it may be leave-encashment past service cost, as leave encashment follows the same method (S Note 37C p.172); not confirmed. 🟡
- Leave encashment expense S 16.49 (FY25 9.01); C 26.16 (15.21) (S Note 29 p.167; C Note 28 p.219).

---------------------------------------------------------------------
## 10. DEFERRED TAX AND INCOME TAX

- Effective tax rate (derived): S 651.56 / 2,565.36 = 25.40% (FY25 616.42 / 2,463.44 = 25.02%); C 662.49 / 2,604.36 = 25.44% (FY25 669.22 / 2,606.76 = 25.67%). Statutory rate used 25.17% (S Note 34 p.169).
- Rate reconciliation (S only): tax at 25.17% on PBT 2,565.36 = 645.65; add non-taxable income effect 0.66; add non-deductible expenses 12.67; less earlier-year adjustment (7.42); total 651.56. The Consolidated note gives NO rate reconciliation (C Note 33 p.221): NOT FOUND IN DOCUMENT. 🟡
- Deferred tax (S Note 34(iii) p.169): depreciation difference +76.08 (FY25 +12.14); accrued expenses (29.11) ((16.65)); Ind AS adjustments (9.43) (16.60); total P&L deferred 37.54 (12.09). The depreciation timing jump matches the Dombivli capitalisation (accelerated tax depreciation on a newly capitalised asset base). [INFERENCE] timing; the note does not name Dombivli.
- DTL net: S 295.70 (FY25 257.51) (S Note 18 p.164). Consolidated shows a separate DTA of Rs mn 198.34 (FY25 186.33) alongside the same DTL 295.70 (C Note 17 p.216). DTA composition and entity: NOT FOUND IN DOCUMENT. 🟡
- Consolidated deferred-tax roll does not close: Note 17 opens FY26 DTA at 187.13 while the FY25 balance sheet shows 186.33 (diff 0.80); the P&L deferred tax 25.00 plus OCI deferred tax 1.18 = 26.18 vs movement DTL +38.19 less DTA +11.21 = 26.98 (diff 0.80). Immaterial; consistent with each other. 🟡
- MAT credit: NOT FOUND IN DOCUMENT. Unrecognised DTA and reasons: NOT FOUND IN DOCUMENT. Tax losses in JHPPL (FY26 loss 34.29) and DTA recognition: NOT FOUND.
- Prior-year current-tax adjustment: credit of Rs mn 7.42 in FY26 (S and C). Current-tax liability net: C 34.12 (34.92); S 31.09 (8.45).
- Income taxes paid, C CF Rs mn 638.64 (FY25 642.01) (p.193).

---------------------------------------------------------------------
## 11. REVENUE DETAILS, AND COMPARATIVES

### 11.1 Disaggregation (Rs mn), C Note 24 p.218

| Line | FY26 | FY25 (as printed in FY26 AR) | YoY (derived) |
|---|---|---|---|
| Inpatient income | 11,738.52 | 10,110.45 | +16.1% |
| Outpatient income | 2,617.17 | 2,343.71 | +11.7% |
| Hotel | 107.80 | 103.71 | +3.9% |
| Cafeteria | 129.54 | 116.76 | +10.9% |
| Pharmacy | 391.92 | 338.57 | +15.8% |
| Academic services | 10.87 | 10.17 | +6.9% |
| Medical services | 2.04 | 1.00 | +104% |
| Share of partnership firms | 0.01 | (0.35) | n/m |
| Total | 14,997.87 | 13,024.02 | +15.2% |

- No geography or payer-class split, no hospital-wise revenue: NOT FOUND IN DOCUMENT (single segment, p.234). Top customer revenue: NOT FOUND.
- Contract liabilities (patient advances) C 195.64 (FY25 152.10, +28.6%); S 174.38 (132.76) (C Note 22 p.217; S Note 23 p.165). Unsatisfied performance obligations: NOT FOUND IN DOCUMENT.
- Occupancy and ARPOB definitions: the notes contain NO definition and no figure. Outside the notes, the AR states average occupancy 61.20% FY26 vs 65.30% FY25, ARPOB Rs 67,700 vs Rs 60,600 (+11.70%), ALOS 3.87 days vs 3.89 (Annual_Report_2026.pdf p.20 operational parameters; MD&A p.46). The MD&A gives occupancy 62.3% excluding Dombivli and 61.2% including it (p.46). Only the label "ARPOB (Average Revenue Per Occupied Bed)" is printed (p.20); census versus bed-day basis, and in-patient versus blended revenue basis, are NOT FOUND IN DOCUMENT. Brief fact 4 (H1 FY27 59.5% and ARPOB Rs 71,800) is not in this AR. 🟡
- Bed count inside Note 1A: parent note says 1,248 operational beds across four hospitals (Thane, Pune, Dombivli, Indore) (S Note 1 A p.144); the consolidated note opens with "961 across three hospitals" and then repeats "1248 across four" in the next paragraph (C Note 1 A p.196). Dombivli beds = 1,248 - 961 = 287 (derived). The 961 sentence is stale boilerplate. 🟡

### 11.2 FY25 comparatives were re-cut in the FY26 AR (restatement check against Annual_Report_2025.pdf)

| Consolidated, Rs mn | FY25 as filed in AR25 (p.85) | FY25 as comparative in AR26 (pp.191-192) | Gap |
|---|---|---|---|
| Revenue from operations | 12,615.45 | 13,024.02 | +408.57 (+3.2%) |
| Other income | 286.75 | 283.47 | -3.28 |
| Purchases of consumables | 2,329.19 | 2,581.70 | +252.51 |
| Employee benefits | 2,144.99 | 2,252.36 | +107.37 |
| Professional fees | 3,121.23 | 3,052.82 | -68.41 |
| Finance costs | 105.54 | 107.06 | +1.52 |
| Depreciation and amortisation | 569.84 | 570.83 | +0.99 |
| Other expenses | 2,081.96 | 2,162.84 | +80.88 |
| Profit before tax | 2,577.01 | 2,606.76 | +29.75 |
| Profit for the year | 1,935.00 | 1,937.54 | +2.54 |
| Total assets | 19,048.89 | 19,357.50 | +308.61 |

| Standalone, Rs mn | AR25 (p.63) | AR26 comparative | Gap |
|---|---|---|---|
| Revenue | 10,599.98 | 10,600.65 | +0.67 |
| Professional fees | 2,523.95 | 2,461.49 | -62.46 |
| Other expenses | 1,699.78 | 1,762.24 | +62.46 |
| Profit for the year | 1,847.02 | 1,847.02 | nil |
| Trade receivables | 365.56 | 377.76 | +12.20 |
| Cash and cash equivalents | 3,674.10 | 845.39 | -2,828.71 |
| Bank balances other than cash | 1,203.47 | 24.54 | -1,178.93 |
| Current investments | 1,142.68 | 5,122.59 | +3,979.91 |
| Trade payables (MSME + other) | 821.56 | 541.75 | -279.81 (equals FY25 capital creditors 279.81 now in other financial liabilities, S Note 22 p.165) |

The only disclosure is "Previous year's figures have been regrouped wherever applicable" (S Note 37R p.182; C Note 36R p.235). No restatement note, no reconciliation. A consolidated revenue base that moves 3.2% and a PAT that moves Rs mn 2.54 is more than regrouping. Growth for FY26 on the AR25-printed base would be 14,997.87 / 12,615.45 = +18.9%; on the AR26 base +15.2% (both derived). Use the AR26 comparatives; cause of the re-cut NOT FOUND IN DOCUMENT. 🔴
The cash and investment reclassification (about Rs mn 3,980 moved into current investments) also changes the prior-year consolidated cash flow base; the FY25 consolidated closing cash in the AR26 CF is Rs mn 925.16 (C CF p.194).

### 11.3 Other number mismatches seen in pass 1
- C PPE note shows closing CWIP Rs mn 1,286.99 (C Note 1.1 p.208), but the balance sheet and CWIP ageing show 1,292.12 (BS p.191; ageing p.209). Difference Rs mn 5.13. S ties (1,127.05). 🟡
- C FY25 provisions (non-current 112.21 + current 20.23 = 132.44) are lower than the parent's own FY25 (105.42 + 56.14 = 161.56): gap 29.12. AR25 consolidated shows non-current 49.69 and current 153.67 (Annual_Report_2025.pdf p.85), so the FY26 AR re-split them. 🟡
- Lease payments: C CF 162.18 vs lease note 177.24 (diff 15.06); S CF 172.10 vs note 171.44 (C CF p.194; C Note 36J p.230; S CF p.142; S Note 37J p.177). 🟡
- Lease maturity table shows "less than one year" 11.59 (S) and 18.31 (C) against current lease liability 96.04 (S) and 101.80 (C) (S Note 37J p.178; C Note 36J p.231). FY25 shows all 674.32 in "more than five years" against a current liability of 50.91. The table is not a usable maturity profile. 🟡
- Security deposits (non-current, S) fell from 527.70 to 324.80 (-202.90) while the CF line "(Increase)/decrease in deposits" is (9.41) (S Note 3 p.158; S CF p.141). Reason NOT FOUND. 🟡

---------------------------------------------------------------------
## 12. OTHER CRITICAL NOTES

### 12.1 Dombivli, depreciation and finance cost (load-bearing facts 1 and 2)
- Dombivli capitalisation: "During the year capitalisation includes Dombivli Hospital capitalisation of Rs mn 3,881.3" (S Note 1.1 CWIP note p.156; C Note 1.1 p.209). Transfers out of CWIP: S Rs mn 3,892.19, C Rs mn 3,962.95 (S Note 1.1 p.155; C p.208). Dombivli is therefore about 98% of the CWIP transfers (derived: 3,881.3 / 3,962.95).
- Breakdown of FY26 PPE additions (S, Rs mn): buildings 2,079.63; plant and machinery 793.39; medical equipment 1,046.72; furniture 116.41; electrical 190.10; office 58.87; computers 45.53; freehold land 10.35 (S Note 1.1 p.155). C buildings 2,083.02; plant 849.34; medical equipment 1,097.13; electrical 191.47 (p.208).
- Date Dombivli commenced operations, date of capitalisation, and the date depreciation began: NOT FOUND IN DOCUMENT in the notes (Dombivli is listed as an operating hospital in the bed count, S Note 1 A p.144). The brief's January 2026 start is from outside this document.
- Pre-operative costs: NOT FOUND IN DOCUMENT (policy 1.5). Items that rose in a way a launch would explain but are not attributed to it in any note: advertisement and business promotion S Rs mn 65.35 vs 35.50 (+84%); C 86.76 vs 46.40 (+87%) (S Note 33 p.168; C Note 32 p.220). Items that fell sharply: staff welfare S 110.19 vs 158.05 (-30%); building repairs S 25.03 vs 47.18 (-47%); miscellaneous S 32.27 vs 74.17 (-56%). Cause NOT FOUND; a question for management on cost capitalisation into Dombivli CWIP. 🟡
- Consolidated depreciation and amortisation: 876.40 vs 570.83 (+53.5%) (C Note 31 p.219). Components: PPE 696.67 vs 526.14 (note 1.1 shows 526.02); right-of-use 165.08 vs 38.83; intangible 14.65 vs 5.86. Check on the brief: Rs 57 Cr to Rs 88 Cr agrees with 570.83 mn to 876.40 mn (10 million = 1 Crore, check only).
- Consolidated finance costs: 326.63 vs 107.06 (+205%) (C Note 30 p.219): interest on term loans 204.40 vs 4.52; interest on lease liabilities 68.60 vs 29.65; bank commission and finance charges 53.57 vs 72.87; other loans 0.06 vs 0.02. Check on the brief: Rs 11 Cr to Rs 33 Cr agrees with 107.06 mn to 326.63 mn (check only). Of the Rs mn 219.57 rise, the term-loan interest rise is 199.88 (91%) (derived).
- Standalone: interest on term loans only 15.15 (FY25 nil) (S Note 31 p.167) against a loan that opened at 750.00, took 1,867.82 of drawdowns and closed at 2,610.32, at Repo + 200 bps. Interest charged equals 2.02% of the opening balance alone (15.15 / 750.00, derived), and the margin alone is 200 bps before Repo. [INFERENCE] most parent term-loan interest was capitalised into Dombivli CWIP, which would move cost from finance cost into PPE and later into depreciation. The capitalised amount, the capitalisation rate, and the drawdown dates are NOT FOUND IN DOCUMENT. Finance cost paid in the parent CF is 48.47 against interest-plus-charges expense of 60.27 (15.15 + 45.12) (S CF p.142). 🔴 (a missing number the profit-squeeze fact depends on)
- Group EBITDA bridge (derived from C P&L p.192: profit before exceptional items + finance costs + D&A - other income): FY26 2,653.23 + 326.63 + 876.40 - 423.68 = 3,432.58; FY25 (AR26 comparative) 2,606.76 + 107.06 + 570.83 - 283.47 = 3,001.18; +14.4%; margin 22.89% vs 23.04%. EBITDA +431.40; D&A +305.57; finance cost +219.57; other income +140.21; PBT before exceptional +46.47 (+1.8%). Profit before exceptional and before other income: 2,229.55 vs 2,323.29 (-4.0%). Other income is 16.3% of PBT (423.68 / 2,604.36). 🟡
- Cost lines (derived, % of C revenue): doctor professional fees 24.27% (FY25 23.44%) (C Note 29 p.219); employee 17.09% (17.29%); consumables consumption 19.15% (19.62%). S doctor fees 23.92% (23.22%). 🟡

### 12.2 CWIP ageing and suspended projects (load-bearing fact 3)
- C CWIP total 1,292.12: projects in progress less than 1 year 819.18; 1-2 years 316.81; 2-3 years 28.51; temporarily suspended more than 3 years 127.62 (same 127.62 in FY25) (C Note 1.1 ageing p.209). S CWIP 1,127.05 (less than 1 year 810.24; 1-2 years 316.81), no suspended projects (S p.156). The suspended 127.62 sits in a subsidiary. Impairment review of it: NOT FOUND IN DOCUMENT. 🟡
- Roll-forward C: opening 1,851.10 + additions 3,398.84 - transfers 3,962.95 = 1,286.99 (see 11.3 mismatch).
- Capital advances (other non-current assets): S 1,169.36 (FY25 3.69); C 1,195.90 (FY25 4.34) (S Note 4 p.158; C Note 4 p.211). Counterparty and project: NOT FOUND IN DOCUMENT. The BKC land (MMRDA tender, about Rs 354 Cr in the brief) is mentioned only as "an agreement for buying land from MMRDA on 80 year lease term ... BKC, Mumbai with potential capacity of 400 beds" (S Note 1 A p.144; C Note 1 A p.196). Price, amount paid, balance payable: NOT FOUND IN DOCUMENT in any note. Right-of-use leasehold land additions FY26 Rs mn 221.41 (S Note 1.2 p.156; C p.209); which plot is NOT FOUND.
- Pipeline named in Note 1A: Bibvewadi Pune (500 beds potential), Mira Road Thane (300 beds), BKC (400 beds) (S Note 1 A p.144).
- Cash capex check (derived): C cash outflow for PPE, CWIP and intangibles Rs mn 5,018.45 (C CF p.193). Build-up: CWIP additions 3,398.84 + direct PPE additions (4,475.65 - 3,962.95 = 512.70) + intangibles 48.68 + rise in capital advances (1,195.90 - 4.34 = 1,191.56) - rise in capital creditors (509.70 - 355.43 = 154.27) = 4,997.51; gap to CF 20.94 (0.4%). So capex includes about Rs mn 1,192 of advances for future sites.
- Group free cash flow (derived): CFO 2,677.08 - capex 5,018.45 = (2,341.37). CFO to EBITDA 78% (2,677.08 / 3,432.58) vs 89% in FY25 (2,667.39 / 3,001.18). Net borrowing in the year 1,860.43 - 32.55 = 1,827.88 (C CF p.194). Internal-accruals funding: FY26 capex exceeded CFO by Rs mn 2,341.37, met by Rs mn 1,827.88 net borrowing and run-down of cash and CP (liquid assets C 6,020.80 to 5,438.72, derived). 🟡
- Cash-flow note on the investing section: C "Interest received" 235.33 equals the parent figure to the paisa in both years, while the subsidiaries also earn interest (C CF p.193; S CF p.141). 🟡

### 12.3 Capital commitments (load-bearing fact 3)
NOT FOUND IN DOCUMENT. No estimated amount of contracts remaining to be executed on capital account, no MMRDA payment schedule, no Pune or Mira Road commitment. The Directors' Report says no material commitments arose between year end and the report date (p.~66, lines 6385-6394 of the text; "MATERIAL CHANGES AND COMMITMENTS" section), which is a post-year-end statement, not a capital-commitment disclosure. Given capital advances of Rs mn 1,169.36 and three named projects, the omission is material to sizing remaining capex. 🔴

### 12.4 Exceptional items
One item, New Labour Codes past service cost: S Rs mn 43.89, C Rs mn 48.87; labelled non-recurring; FY25 nil (S Note 37A; C Note 36A). Recurrence pattern: single-year. 🟡 (the exceptional line sits below PBT before exceptional; clean PAT effect after tax NOT FOUND).

### 12.5 EPS, dilution, ESOP, share capital
- Basic = diluted: S Rs 29.19 (FY25 28.17), C Rs 29.59 (29.47) on 65,566,022 shares (S Note 35 p.170; C Note 34 p.221). No dilutive instruments. The Directors' Report says the Company has no ESOP scheme in place (line 6326-6327 of the text). 🟢
- No change in share capital; no bonus, buyback or preferential allotment in five years (S Note 13 F-G p.162). Promoters: Dr. Ajay Thakker 20.74%, Western Medical Solutions LLP 8.70%, Dr. Ankit Thakker 6.67%, total 36.11%, unchanged (S Note 13 D-E p.162). Pledge: NOT FOUND IN DOCUMENT in the notes. 🟢
- Reserves: no direct debits or credits to reserves bypassing P&L, other than dividends 65.57 and transfer to general reserve 191.38 (S SOCE p.143). Consolidated FY25 reserves show "Distribution of profits" (37.13) and "Adjustment for prior period" +17.39 (C Note 13 pp.214-215; C SOCE p.195): a prior-period adjustment taken to equity in FY25, nature NOT FOUND IN DOCUMENT. 🟡

### 12.6 Events after the balance sheet date
- Interim dividend Rs 1 per share declared 15-May-2026 (Rs mn 65.57, derived 65,566,022 x Rs 1) (S Note 37O p.181; C Note 36O p.234). That is about 3.4% of standalone PAT (65.57 / 1,913.80). Dividend paid in FY26: 65.57 (FY25 65.57), flat.
- Stock split (approved 15-May-2026, per B00 corporate_action_note): NOT FOUND IN DOCUMENT in the notes or AR text. 🟡
- Directors' Report: no material changes or commitments between year end and report date; no regulator orders affecting going concern (lines 6385-6400 of the text). 🟢

### 12.7 Leases (Ind AS 116)
- Right-of-use assets C Rs mn 990.61 (FY25 740.26): leasehold land 860.50, buildings 116.11, plant 14.00 (C Note 1.2 p.209). Depreciation on ROU C 165.08 (38.83); S 159.55 (38.83). Additions FY26 C 415.43 (leasehold land 221.41, building 174.64, plant 19.38); FY25 779.09, all leasehold land.
- Lease liabilities C 757.13 (FY25 674.32): current 101.80, non-current 655.33. Interest on leases C 68.60 (29.65) (C Note 36J p.230). Implied rate: 68.60 / average liability (674.32 + 757.13) / 2 = 9.6% (derived). Discount rate disclosed: NOT FOUND.
- Short-term and low-value lease expense: rent including lease rentals C 36.09 (44.24) (C Note 32 p.220). Lessor income: rental C 1.23 (1.67); space given to Jupiter Hospital Pharmacy and Katyayini (section 2). 🟡

### 12.8 Foreign currency
Earnings S and C 83.98 (FY25 99.05; hotel nil vs 13.77); expenditure C 71.00 (1.73) including import of capital goods 67.29 (nil) (C Note 36G p.228). No hedging or derivatives; "no material foreign currency exposure" (S Note 36 p.171; C Note 35 p.222). 🟢

### 12.9 CSR
Required S/C Rs mn 40.60 (FY25 31.23); spent 40.00 (40.00); prior excess set-off 8.77; carry-forward 8.17 (8.77); education and sports; no shortfall (S Note 37F p.175; C Note 36F p.228). Donations to Jupiter Foundation (promoter-linked) 15.69 (28.30), 39% of CSR spend in the year (derived: 15.69 / 40.00). Pre-spent CSR 8.17 shown as an asset (S Note 12 p.161). 🟢

### 12.10 Segment, MSME, auditor-report items tied to notes
- Segment: one (S Note 37M p.181). MSMED: see section 8.
- Audit trail: the Company's accounting software "HMIS" (hospital management system, the billing source) had the audit-trail feature for database-level edits NOT enabled; backup logs for record retention could not be produced for one other accounting software. The auditor says it "did not notice any instance of the audit trail feature being disabled or tampered with". The finding is carried into para 19.2 (books of account) and 19.6 as a modification (Auditor's Report paras 19.2, 19.6, 20.8, pp.129-132) and into S Note 37Q p.182 and C Note 36Q p.235, where management concludes internal controls were effective. The IFC opinion in Annexure B is unmodified (p.137). HMIS carries patient billing, so this touches the revenue system. 🔴
- KAM: receivables, reconciliation and provisioning (pp.183-184 of the consolidated report, from the standalone KAM). Other matter: one partnership firm's share of loss Rs mn 2.62 is from unaudited statements (para 17, pp.130-131).
- CARO: no fraud, no whistle-blower complaints, no cash losses, no auditor resignation, no unspent CSR, no default (CARO xi, xvii, xviii, xx, ix; pp.135-136). Going concern: auditor reports no material uncertainty on liabilities due within a year (CARO xix, pp.135-136). 🟢
- Going concern language in the notes: "prepared on going concern basis" only (S Note 1 B(ii) p.144; C Note 1 B(ii) p.196). No stress language, no material uncertainty.

---------------------------------------------------------------------
## PASS 1 SUMMARY: TOP 10 FINDINGS BY INVESTOR IMPORTANCE

| Rank | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | Borrowing-cost capitalisation, pre-operative cost and Dombivli depreciation start are all unquantified, while parent term-loan interest is only Rs mn 15.15 on a loan that rose from 750.00 to 2,610.32 and Dombivli capitalised Rs mn 3,881.3. The profit-squeeze story (D&A +305.57, finance cost +219.57, group Rs mn) cannot be split between expensed and capitalised cost from the notes. | S Note 31 p.167; S Note 1.1 p.156; policy C.4 pp.145-146; C Notes 30-31 p.219 | 🔴 |
| 2 | No capital-commitment disclosure although capital advances reached Rs mn 1,169.36 (S) and three projects (Pune 500 beds, Mira Road 300, BKC 400) are named; BKC land price and payment schedule absent. | S Note 37B p.171; S Note 4 p.158; S Note 1 A p.144 | 🔴 |
| 3 | FY25 comparatives re-cut with no restatement note: C revenue +408.57, PBT +29.75, PAT +2.54, total assets +308.61; about Rs mn 3,980 moved from cash and bank balances into current investments; capital creditors moved out of payables. | S Note 37R p.182; C Note 36R p.235; Annual_Report_2025.pdf pp.63, 85 | 🔴 |
| 4 | HMIS billing software lacks database-level audit trail; backup logs for another system missing; auditor treats it as a books-of-account matter, management calls controls effective. | Auditor's Report paras 19.2, 19.6, 20.8 pp.129-132; S Note 37Q p.182 | 🔴 |
| 5 | Receivables up 72.3% gross against revenue up 15.2%; unbilled bucket Rs mn 191.07 (24% of gross) newly shown; net days 12.1 to 18.4; ECL 4.65% of gross vs 5.95%; KAM on receivables. | C Note 7 p.212; S Note 7 pp.159-160; KAM pp.183-184 | 🟡 |
| 6 | Debt Rs mn 5,085.27 (C), all floating at Repo + 200 bps, repayment back-ended, covenants not disclosed, JHPPL guarantee Rs mn 2,500; 89.3% of group liquidity is one issuer's commercial paper; text says "bank deposits ... no credit risk". Group net cash only Rs mn 353.45 if the CP counts. | C Note 14 p.215; C Note 36H p.229; C Notes 6, 35 pp.211, 221 | 🟡 |
| 7 | Doctor fees 24.27% of revenue (23.44%), consumables inventory days 48.7 (37.8), operating profit before other income -4.0%, other income 16.3% of PBT. | C Notes 29, 5, 25, 27 | 🟡 |
| 8 | JHPPL: loss Rs mn 34.29 (FY25 profit 88.01), parent cost 939.00 vs net assets 242.60, no impairment test, intra-group loan 293.37 on demand with no stated rate, suspended CWIP Rs mn 127.62 over 3 years. | C Note 36D p.226; S Note 2 p.158; C Note 1.1 p.209 | 🟡 |
| 9 | Payables +38.3%, MSME dues +188%, Rs mn 69.90 MSME past due with nil MSMED interest; overdue 19.0% of payables; current ratio fell 4.37 to 3.02. | C Notes 20, 36E, 36L pp.216, 228, 233 | 🟡 |
| 10 | Governance and RPT: promoter pay S +25.0% (Ankit Thakker S 39.00 vs 25.92; C FY25 comparative 31.91 conflicts), RPTs 1.15% of revenue, two new professional-fee parties, Entisi purchases +74.9%; auditor joint-appointment change and audit fee +90%. | C Note 36K p.232; S Note 37K p.179 | 🟡 |

Clean points: no policy change; useful lives disclosed with no change; contingent liabilities 0.32% of net worth; no MAT or unrecognised-DTA issue disclosed; CSR met; no ESOP; labour-code cost isolated as exceptional; Medulla merger pending is consistent with the 18-Nov-2025 NCLT order (creditor-notice change only).

Load-bearing fact status after pass 1:
1. Dombivli: capitalised Rs mn 3,881.3 (confirmed, S Note 1.1 p.156); commencement date, pre-operative costs, depreciation start NOT FOUND IN DOCUMENT.
2. Profit squeeze: D&A and finance cost movements confirmed (876.40 vs 570.83; 326.63 vs 107.06, C); borrowing-cost capitalisation amount NOT FOUND IN DOCUMENT; parent interest pattern suggests material capitalisation [INFERENCE].
3. Capex and debt: gross debt Rs mn 5,085.27 (C); the brief's Rs 584 Cr reads as debt plus leases (5,842.40). Capital commitments NOT FOUND IN DOCUMENT. CWIP ageing disclosed; BKC land price NOT FOUND IN DOCUMENT. Related-party items and NCLT scheme covered.
4. Occupancy and ARPOB: no definitions in AR notes; operational data at AR pp.20 and 46 only.
