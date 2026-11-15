# STAGE 2 NOTES, PASS 1 (FULL EXTRACTION): QLL (Qualitek Labs Ltd), run 2026-11-15

Source: inputs/annual-report/Annual_Report_2026.txt (FY2025-26 AR, 191 pp). Page numbers below are the "[page N]" markers of that text file (PDF pages).
Unit: INR Lakh (face of every financial statement, "All amounts in Rs Lakh", C-BS p.102). 100 Lakh = 1 Cr. No figure below is converted unless marked "Cr (derived)". "Derived" means my arithmetic on filed figures; the inputs carry anchors.
Anchor key: C-Note n = Consolidated note (AR pp.106-143). S-Note n = Standalone note (AR pp.162-190). CARO = auditor annexure.
Framework facts: the AR is Indian GAAP (AS), not Ind AS (C-Note 2, p.106; S-Note 2.1, p.162). Ind AS items (ECL matrix, ROU asset, lease discount rate under Ind AS 116) do not apply. Auditor: J Madan & Associates, unmodified opinion on both sets, "no key audit matters" (p.93, p.146).
B00 input_gaps carried: no rating, no concall, no BSE shareholding filing, no research. None of these change a notes finding. The H1 FY27 presentation gap does not touch the AR. Prior-year AR (Annual_Report_2025.txt) spot-checked: FY25 comparatives in the FY26 AR (revenue 7022.69, PAT 768.36, receivables 2885.75, goodwill on consolidation 3303.78, minority interest 597.53; standalone revenue 4586.48, receivables 1178.75) match the FY25 AR face figures. No restatement of those lines.

## 0. LOAD-BEARING FACTS CHECKED (companies/QLL.md, first priority)

| # | Memory claim | What the AR says | Verdict |
|---|---|---|---|
| 2a | FY26 receivables Rs 42.14 cr on revenue Rs 124.52 cr | Consolidated trade receivables 4214.04 Lakh; revenue 12451.81 Lakh (C-BS p.102; C-P&L p.103; C-Note 15, p.126) | CONFIRMED (consolidated) |
| 2b | Short-term borrowings Rs 16.24 cr at 31 Mar 2026 | 16.24 cr = STANDALONE Note 8 total 1623.61 Lakh (S-Note 8, p.171). Consolidated short-term borrowings are 3285.40 Lakh = Rs 32.85 cr (C-Note 8, p.121) | CONFIRMED but basis is standalone. The memory does not say so. Consolidated is double. |
| 3a | FY26 total PAT Rs 14.60 cr | Consolidated net profit 1460.15 Lakh (C-P&L p.103) | CONFIRMED |
| 3b | PAT to owners Rs 6.30 cr | Consolidated profit to owners 1362.22 Lakh = Rs 13.62 cr (C-P&L p.103; C-Note 4, p.116). Minority share 97.92 Lakh. Standalone PAT 796.44 Lakh (S-P&L p.159). 6.30 cr appears nowhere. | NOT FOUND IN DOCUMENT. The 6.30 figure is wrong for the owners' share. |
| 3c | EPS Rs 13.38 does not reconcile | AR EPS consolidated 12.49 (1362.23 / weighted 1,09,09,702 shares), standalone 7.30 (C-Note 25, p.130; S-Note 26, p.178). Derived: 1460.15 Lakh total PAT / 1,09,09,702 = 13.38. So 13.38 is total PAT incl. minority share over weighted shares. AR EPS excludes minority (C-Note 2 policy I, p.112). | RECONCILED (derived). Use 12.49. |
| 3d | Non-controlling interest | Minority interest at 31 Mar 2026 = 0.00 (FY25 597.53) after ITCPL moved to 100% (C-Note 38, p.141; C-BS p.102). The P&L still deducts 97.92 Lakh minority share for the pre-swap period (C-P&L p.103). | CONFIRMED. NCI is gone from the balance sheet. P&L leakage was only FY26 H1. |
| 3e | Stakes: ITC Labs / Quality & Testing Info Solution / LabOps | Interstellar Testing Centre Pvt Ltd (ITCPL) 100% from 10 Sep 2025 (was 49.99% with board control from 11 Sep 2024); Quality & Testing Infosolution Pvt Ltd (QTIPL) 100% from 9 Sep 2024; LabOps Global Pvt Ltd 74% from 23 May 2025 (C-Note 33a, p.139; C-Note 26, p.131). "ITC Labs" in memory = ITCPL. | CONFIRMED |
| 3f | Goodwill Rs 78.12 cr | Goodwill on consolidation 7811.56 Lakh = 3303.78 (FY25) + 4507.78 added in FY26 (C-Note 11e, p.125; C-BS p.102). Basis: FY25 goodwill = cash 3299.26 for 49.99% of ITCPL plus 500.00 for 100% of QTIPL, net of net assets (C-Note 33d, p.139). FY26 addition = 16,72,531 new shares valued at 10 + 300.89 premium = 310.89 per share = 5199.73 Lakh, less minority interest extinguished 694.56 Lakh (C-Note 38, p.141; C-Note 3 note (i), p.114; S-Note 37, p.188). Derived 5199.73 - 694.56 = 4505.17 against 4507.78 booked: 2.61 Lakh unexplained. A separate 194.21 Lakh purchased goodwill (food lab slump sale) sits in intangibles (C-Note 11b, p.124). | CONFIRMED, see Finding R1 |
| 4a | Promoter warrants, EGM 5 Dec 2026 | After the AR date. Notes carry "no material events" (C-Note 41, p.143; S-Note 43, p.190). | NOT FOUND IN DOCUMENT (expected). |
| 4b | Related-party flows with TIC Services Pvt Ltd | TIC is "Ultimate Holding Company", holds 65,78,375 shares = 56.46% (C-Note 3, p.114). FY26 flows: shares issued to TIC for ITCPL stake 3640.15 Lakh; loan repaid 88.36; guarantee fee 0.20; balance payable 0.24 (C-Note 26, p.131). TIC corporate guarantee covers bank debt with limits 6449.00 and outstanding 5739.65 (C-Note 26 note d, p.133). Promoter-unsecured-loan repayment of 818.16 Lakh used IPO money in FY24 (S-Note 38, p.188). | CONFIRMED, see Finding R2 |

## 1. ACCOUNTING POLICIES AND CHANGES

1.1 Framework 🟡. Indian GAAP (AS) throughout, no Ind AS (C-Note 2, p.106). Consolidated note headers still read "year ended March 31, 2025" on the policy pages (pp.106-113). A template carry-over, no numbers affected.
1.2 Revenue recognition 🟡. "Completed service contract method": revenue booked only when the report is issued; unbilled services shown as "Unbilled accounts receivable" inside trade receivables (C-Note 2.4 A, p.107; unbilled 206.67 Lakh consolidated, C-Note 15 ageing, p.127; 140.69 Lakh standalone, S-Note 16, p.176). This is conservative against percentage-of-completion, with a small unbilled stock (4.9% of gross consolidated receivables, derived).
1.3 Depreciation 🟡. Straight-line over Schedule II lives. Plant and machinery 15 years; computers 3-5 years; office equipment 5; vehicles 8-10; furniture 10; leasehold improvements 10 (standalone only) (C-Note 2.4 B, p.108; S-Note 2.4 B, p.163). No change in lives disclosed. The AR gives no testing-equipment-specific life or technology obsolescence basis. Stated as NOT FOUND IN DOCUMENT.
1.4 Goodwill policy 🟡. Two rules in one AR. Purchased goodwill amortised over 5 years (C-Note 2.4 C(a), p.109; 219.86 Lakh from 1 Sep 2025, 25.65 Lakh charged in FY26 = 7 months). Goodwill on consolidation is indefinite-life, not amortised, "tested for impairment annually and whenever there is an indication" (C-Note 2.4 C(b), p.109). Yet Note 40 says "No disclosure is required with regard to Impairment of Assets, since the Group has no indication of a potential impairment loss at present" (C-Note 40, p.143; S-Note 32, p.185). No CGU, growth rate or discount rate is disclosed. Impairment assumptions: NOT FOUND IN DOCUMENT.
1.5 Impairment policy 🟡. Five-year budgets then long-term growth rate (C-Note 2.4 D, p.110). No test result disclosed.
1.6 Capitalisation 🟡. Borrowing costs capitalised on qualifying assets: 143.14 Lakh in FY26 (consolidated and standalone both; FY25 consolidated 64.30, standalone 29.92) (C-Note 32, p.138; S-Note 40, p.189). Derived: 143.14 = 7.8% of consolidated PBT (1832.10) and 14.9% of standalone PBT (959.73). Capitalised interest share of total borrowing cost rose from 17.3% to 36.7% at standalone (derived from S-Note 24 interest 247.08 and 143.14 / 143.30 and 29.92). Without capitalisation, FY26 finance cost would be 623.68 Lakh consolidated against 480.54 booked.
1.7 Lease accounting 🟡. AS 19 style: operating leases expensed, finance leases capitalised (C-Note 2.4 E, p.110; C-Note 31, p.138). No ROU asset or Ind AS discount rate. Operating lease expense 664.89 Lakh (FY25 360.75). Finance lease liability PV 364.43 Lakh (FY25 220.67). Non-cancellable operating commitments 1605.91 Lakh (C-Note 31, p.138). Standalone: expense 465.49, commitments 782.14 (S-Note 39, p.188).
1.8 First-time standards or policy changes with P&L effect. New Labour Codes (notified 21 Nov 2025): impact "not material", booked in employee cost, no amount given (C-Note 27, p.136; S-Note 30, p.184). Quantified P&L impact: NOT FOUND IN DOCUMENT. Past service cost of 34.11 Lakh (gratuity 13.62 + leave 20.49) appears in the consolidated actuarial table (C-Note 27, p.136), likely related, but the AR does not link them.
1.9 EPS policy 🟡. Standalone policy says EPS uses "closing number of equity shares" (S-Note 2.4 K, p.166). The actual EPS note uses weighted average shares, 1,09,09,702 (S-Note 26, p.178). Policy text and practice disagree. Practice is the correct one.
1.10 Reclassifications 🟡. Advance income tax moved from short-term loans and advances to other non-current assets (226.22 Lakh) and employee recoverables (18.49) from loans and advances to other current assets, "for better presentation". Prior-year columns are not restated (FY25 still shows advance income tax 126.54 under short-term loans) (C-Notes 13, 17, 18, pp.126-128). Direct expense lines also differ: consolidated FY25 shows Tools & Fixtures nil and Transportation 137.74 (C-Note 21, p.129), while standalone FY25 shows Tools & Fixtures 91.50 and Transportation 29.53 (S-Note 22, p.177). Presentation only.
1.11 Presentation errors 🟡. Consolidated Note 9 and Note 15 balance sheet columns show "0.00 / 0.01 / 0.03" against FY25 totals 728.34 and 2885.75 (C-Note 9, p.122; C-Note 15, p.126). The ageing tables carry the right totals. Extraction or typesetting error, not a numbers error.

## 2. RELATED PARTY TRANSACTIONS

### 2.1 Parties
Control: TIC Services Pvt Ltd (ultimate holding company, 56.46%). Subsidiaries: ITCPL, QTIPL, LabOps Global. KMP: Antaryami Nayak (MD), Kamal Grover (WTD), Mangesh Bhosale (WTD, from 29 Mar 2025), Alok Kumar Agarwal (Director), Navneet Gupta (CFO), company secretaries Ashima Bhatnagar (to 10 Apr 2025), Mayank Garg (29 May 2025 to 7 Feb 2026), Mohit Bhardwaj (from 20 Apr 2026). Independent directors Sulabh Jain, Manish Wahi, Shubhangi Agarwal, Ajay Agarwal. KMP-influence entities: ASC Consulting Pvt Ltd, ASC Outsourcing Pvt Ltd, A S C B S R And Company LLP, SKM Realcon Pvt Ltd, AAL Biosciences Research Pvt Ltd, AAL Research and Solution Pvt Ltd. Relatives: Divya Grover, Kishan Chand Grover (C-Note 26, p.131); Anju Agarwal (relative of KMP, standalone list, S-Note 27, p.179).
New this year: LabOps Global (23 May 2025), AAL Research and Solution Pvt Ltd (first appears with transactions), ASC Outsourcing, Divya and Kishan Chand Grover. Three company secretaries in 14 months 🟡.

### 2.2 Consolidated table (INR Lakh, C-Note 26, pp.131-134)

| Party | Relationship | Nature | FY26 | FY25 | YoY |
|---|---|---|---|---|---|
| TIC Services | Ultimate holding | Shares issued, non-cash (ITCPL stake) | 3640.15 | nil | new |
| TIC Services | Ultimate holding | Loan repaid | 88.36 | 96.50 | -8% |
| TIC Services | Ultimate holding | Loan taken | nil | 35.00 | |
| TIC Services | Ultimate holding | Guarantee service charge | 0.20 | nil | new |
| TIC Services | Ultimate holding | Balance payable / loan payable at year end | 0.24 / nil | nil / 88.36 | |
| SKM Realcon | KMP-influence | Lease rent | 153.60 | 21.60 | +611% |
| SKM Realcon | KMP-influence | Guarantee service charge; payable | 0.20; 0.24 | nil; 9.72 | |
| ASC Consulting | KMP-influence | Consulting fee and other | 22.77 | 7.64 | +198% |
| ASC Consulting | KMP-influence | Loan taken / repaid | 715.00 / 715.00 | 120.00 / 120.00 | |
| ASC Consulting | KMP-influence | Interest paid; loan payable at year end | 4.79; 20.00 | 2.05; 20.00 | |
| ASC Outsourcing | KMP-influence | Manpower supply | 5.26 | 0.60 | +777% |
| A S C B S R And Co LLP | KMP-influence | Professional fees | 3.21 | 3.21 | 0% |
| AAL Biosciences Research | KMP-influence | Sale of services | 37.30 | 5.15 | +624% |
| AAL Biosciences Research | KMP-influence | Outsourcing expenses | 19.12 | 0.65 | +2841% |
| AAL Biosciences Research | KMP-influence | Advance given / recovered | 262.00 / 262.00 | nil | new |
| AAL Biosciences Research | KMP-influence | Loan taken / repaid; payable at year end | 148.00 / 60.00; 88.00 | nil | new |
| AAL Biosciences Research | KMP-influence | Trade receivable / payable at year end | 77.82 / 6.53 | 33.80 / 0.11 | |
| AAL Research and Solution | KMP-influence | Purchase of PPE | 24.78 | 9.50 | +161% |
| AAL Research and Solution | KMP-influence | Advance given / recovered | 148.00 / 8.00 | 21.80 / nil | |
| AAL Research and Solution | KMP-influence | Advance recoverable at year end | 151.06 | 11.48 | +1216% |
| Antaryami Nayak | MD | Employee benefit expense | 143.12 | 64.26 | +123% |
| Kamal Grover | WTD | Employee benefit expense | 46.36 | 19.50 | +138% |
| Mangesh Bhosale | WTD | Employee benefit expense | 159.15 | 92.89 | +71% |
| Navneet Gupta | CFO | Employee benefit expense | 39.41 | 20.36 | +94% |
| Divya Grover | Relative of KMP | Employee benefit expense | 26.72 | 14.00 | +91% |
| Kishan Chand Grover | Relative of KMP | Employee benefit expense | 10.02 | 7.00 | +43% |
| Independent directors (4) | | Sitting fees | 1.40 | 2.35 | -40% |

Derived totals: KMP and relatives' remuneration 430.82 Lakh vs 222.81 (+93%), 3.46% of revenue vs 3.17% (derived). Recurring non-remuneration RPT cost lines (SKM rent 153.60 + ASC 22.77 + ASC Outsourcing 5.26 + ASCBSR 3.21 + AAL Bio outsourcing 19.12 + AAL Research outsourcing 0.41 = 204.37) = 1.64% of revenue. Related-party revenue (AAL Biosciences 37.30 + ASC 0.19) = 0.30% of revenue. Related-party trade receivable at year end 77.95 (C-Note 15 note, p.126), 1.8% of receivables.
Standalone table (S-Note 27, pp.179-181) shows ITCPL, QTIPL and LabOps flows that eliminate on consolidation: loans given to ITCPL 1559.53 (recovered 2315.76, balance 162.67 vs 918.90); QTIPL 100.68 (balance 143.13); LabOps 6.20; ITCPL revenue from parent 177.58; ITCPL receivable 198.59.

### 2.3 Signals
- 🔴 R2 Share swap with promoter. 11,70,881 shares at 310.89 each to TIC Services (the promoter holding company) = 3640.15 Lakh for 1,78,488 ITCPL shares, and 5,01,650 shares to Mr. Sanjiv Khullar for 76,471 ITCPL shares (C-Note 3 note (i), p.114; C-Note 26 note k, p.134). Derived: 5199.73 Lakh for 2,54,959 ITCPL shares = Rs 2,039 per ITCPL share, against Rs 1,294.6 per share paid in cash for 2,54,845 shares in FY25 (3299.26; C-Note 33d(iii), p.139). The price per ITCPL share rose 57.5% in 12 months (derived). Implied 100% ITCPL value: about 6,600 Lakh (FY25) vs about 10,397 Lakh (FY26) (derived). Valuation report, fairness opinion, independent valuer: NOT FOUND IN DOCUMENT. The seller on the other side, TIC, is the controlling shareholder of QLL. The CARO standalone says the issue complied with sections 42 and 62 (p.154).
- 🔴 R3 Advances to and from KMP-influence entities that contradict the note's own claim. C-Note 39 (xii?) says "During the year, the Group has not granted any loans or advances in the nature of loans to its directors, KMPs and related parties" (p.141, first line of Note 39(i)... the sentence sits under "Additional Regulatory Information"). The RPT table records 148.00 advance given to AAL Research and Solution (balance 151.06 Lakh) and 262.00 given to AAL Biosciences (recovered in full the same year) (C-Note 26, p.133). The consolidated balance sheet notes show related-party loans and advances of nil (C-Note 12, p.126; C-Note 17, p.128), so where the 151.06 sits is NOT FOUND IN DOCUMENT; "Other loans and advances 283.37" (C-Note 12, p.126; S-Note 13, p.175) is the only unexplained candidate and is not described.
- 🟡 Interest terms conflict. Consolidated Note 8 says related-party loans carry 8.50% p.a. and the lenders "waived the interest" for FY26 (C-Note 8 note (iv), p.121). Consolidated Note 26 note l says "Loans payable to related parties are unsecured, interest-free" (p.134). The same table shows interest paid to ASC Consulting 4.79 (p.133). Standalone says interest-free (S-Note 8, p.171; S-Note 27 note j, p.181).
- 🟡 Interest waived on loans to subsidiaries. Board resolution dated 20 May 2026 (the audit sign-off date) waived 8.50% interest for 1 Apr 2025 to 31 Mar 2026 on loans to related parties (S-Note 13 note, p.175; S-Note 27, p.181). The CARO calls the loans to subsidiaries "unsecured and interest for the year is waived" and flags it as an adverse remark: Clause 3(iii)(b) qualified for the holding company and for ITCPL (CARO consolidated Annexure A, p.99; CARO standalone clause (iii)(a)/(b), p.152). Interest foregone amount: NOT FOUND IN DOCUMENT. Eliminates on consolidation.
- 🟡 SKM Realcon is landlord, mortgagor of key properties and guarantor. Rent rose from 21.60 to 153.60 Lakh (7.1x). It is 33% of standalone operating lease expense 465.49 (derived 153.60/465.49; S-Note 39, p.188). Market rent benchmark: NOT FOUND IN DOCUMENT. Guarantee fee charged: 0.20 Lakh (SKM) and 0.20 (TIC) against guarantee limits of 7664.00 and 6449.00.
- 🟡 Remuneration. Mangesh Bhosale 159.15 Lakh (+71%) and Nayak 143.12 (+123%); Nayak is paid 27.00 at the parent and the balance (116.12, derived) by the subsidiary (S-Note 27, p.180). Section 197 compliance affirmed by the auditor (p.96).
- 🟡 Auditor fee. Group audit remuneration 3.84 Lakh (C-Note 24, p.130) = 0.031% of revenue (derived). A related entity A S C B S R And Company LLP bills 3.21 Lakh professional fees every year.
- Promoter loan from IPO money 🟡. 818.16 Lakh (44.7% of net IPO proceeds 1831.18, derived) was used in FY24 to repay an unsecured promoter loan (S-Note 38, p.188).
- Guarantees by promoters and promoter-group entities (all RPT, stated in C-Note 26 notes d-j, pp.133-134): TIC Services limit 6449.00 / outstanding 5739.65; ASC Consulting 7446.00 / 6718.98; SKM Realcon 7664.00 / 6874.29; Nayak 7583.71 / 6295.50; Grover 7525.84 / 6243.14; Alok Agarwal 7244.00 / 6212.63; Anju Agarwal 7664.00 / 6874.29. Derived: the largest outstanding covered amount, 6874.29, equals 84% of consolidated bank debt (8,159.37, built from C-Notes 5 and 8). Debt is substantially personally and promoter-entity backed. This is also a dependence flag.

## 3. CONTINGENT LIABILITIES AND COMMITMENTS

| Nature | FY26 | FY25 | Stage | Assessment |
|---|---|---|---|---|
| Income tax demand AY 2018-19 | 5.48 | 5.48 | Pending CIT(A) | "no provision required" |
| Income tax demand AY 2023-24 | nil | 7.99 | Cleared or dropped, status not given | |
| GST demand FY 2017-18 to 2021-22 | 91.21 | 91.21 | Pending GST Commissioner (Appeals) | "no provision required" |
| GST paid under protest (asset) | 8.29 | 8.29 | | C-Note 17, p.128 |
| Bank guarantee by QLL for ITCPL loans/OD | 2133.00 (outstanding 1728.59) | nil | Intra-group | |
| Bank guarantee by ITCPL for QLL loans/OD | 4911.00 (outstanding 4284.04) | | Intra-group | |

(C-Note 28, p.137; S-Note 27 III(c), p.182; S-Note 30, p.184.)
- Tax and GST claims total 96.69 Lakh = 0.63% of consolidated net worth 15,242.60 (derived). No single item above 10% of net worth. 🟢
- 🟡 Cross-guarantees. QLL guarantees ITCPL's bank debt (2133.00) and ITCPL guarantees QLL's (4911.00). They are listed as consolidated contingent liabilities though they are intra-group. The real signal: bank credit rests on mutual guarantees plus promoter and promoter-entity guarantees.
- 🟡 Standalone Note 30 says no significant claims and no litigation against the company; the GST and income tax demands sit therefore at a subsidiary. The entity holding the GST demand is NOT FOUND IN DOCUMENT.
- Capital commitments: Note 28(ii) says "does not have any long term commitments or material non-cancellable contractual commitments" (C-Note 28, p.137). Yet CWIP stands at 4528.25 Lakh (FY25 1566.34, +189%), capital creditors 390.75 (FY25 83.04), capital advances 342.59 (C-Notes 11c, 10, 12, pp.124-126). Estimated capital contracts remaining: NOT FOUND IN DOCUMENT 🟡.
- Going concern CARO: Clause 3(xix) is listed as qualified or adverse for QTIPL and LabOps Global (CARO consolidated Annexure A, p.99). Clause 3(xix) is the clause on whether the company can meet its liabilities within a year. Detail of the subsidiaries' own reports: NOT FOUND IN DOCUMENT. Group-level auditor opinion is unmodified.

## 4. TRADE RECEIVABLES

Consolidated ageing (C-Note 15, p.127), INR Lakh:

| Bucket | 31 Mar 2026 | % gross | 31 Mar 2025 | % gross |
|---|---|---|---|---|
| Unbilled | 206.67 | 4.9% | 177.49 | 6.2% |
| < 6 months | 3069.35 | 72.7% | 2066.73 | 71.6% |
| 6 months to 1 year | 312.41 | 7.4% | 232.55 | 8.1% |
| 1-2 years | 310.86 | 7.4% | 140.88 | 4.9% |
| 2-3 years | 100.37 | 2.4% | 40.38 | 1.4% |
| > 3 years | 220.46 | 5.2% | 227.72 | 7.9% |
| Gross | 4220.12 | | 2885.75 | |
| Provision | (6.08) | 0.14% | nil | |
| Net | 4214.04 | | 2885.75 | |

Percentages derived. Over 6 months (excl. unbilled): 944.10 Lakh = 22.4% of gross (FY25 641.53 = 22.2%). Over 1 year: 631.69 = 15.0% (FY25 409.00 = 14.2%). Over 3 years 220.46 is 5.2% (FY25 7.9%).
- 🔴/🟡 R4 Provision cover. Provision 6.08 Lakh is 2.8% of the over-3-year bucket and 0.96% of the over-1-year bucket (derived). Bad debts written off in P&L 39.70 (FY25 34.35) plus provision charge 2.99 (C-Note 24, p.130). No ECL matrix (not required under AS). Policy basis for provisioning: NOT FOUND IN DOCUMENT. Rated 🟡 because the auditor's opinion is unmodified and write-offs run at 0.32% of revenue, but the aged stock is far above the provision.
- Where the aged stock sits (derived by subtraction). Standalone over-6-month receivables 148.73 Lakh = 7.5% of 1970.42 (S-Note 16, p.176), standalone over-3-year nil (disputed 0.70 aside). Consolidated over-6-month is 944.10. So about 795 Lakh of the aged stock, including all of the 220.46 over 3 years, sits in subsidiaries (mainly ITCPL). 🟡
- Days trend. Consolidated year-end receivables 4214.04 / revenue 12451.81 x 365 = 123.5 days (derived). FY25 comparison is distorted because FY25 revenue includes ITCPL only from 11 Sep 2024. Standalone is clean: 1970.42 / 6762.45 x 365 = 106.4 days vs 1178.75 / 4586.48 x 365 = 93.8 days (derived), +12.6 days. Standalone receivables rose 67.2% against revenue +47.4% (S-BS p.158; S-P&L p.159; derived). The AR's own ratio on average receivables: turnover 4.29 vs 4.67 (S-Note 34 F, p.186). Direction: deteriorating at standalone, large aged stock at group level. Three-year trend beyond FY25: NOT FOUND IN DOCUMENT (the FY25 AR gives FY24 standalone receivables 785.39 and revenue 2918.38, i.e. 98.2 days, derived; Annual_Report_2025.txt lines 4822, 4856).
- Consolidated cash flow shows receivables increase 1371.36 against CFO 1387.16 (C-CF p.104). 🟡
- Customer concentration above 10%: NOT FOUND IN DOCUMENT.
- Related-party receivables: 77.95 Lakh consolidated (AAL Biosciences 77.82 + AAL Research 0.13), 77.95 vs 33.93 prior (C-Note 15 note, p.126). Standalone 199.03, of which ITCPL 198.59 (S-Note 16 note, p.175; S-Note 27, p.180).
- Foreign debtors. Outside India 100.85 Lakh (FY25 16.77) = 2.4% of receivables (C-Note 29, p.137). Unhedged USD 100,827 = 95.44 Lakh and EUR 4,970 = 5.42 Lakh (C-Note 30, p.137). Standalone says no unhedged exposure (S-Note 33, p.185), so the exposure is subsidiary-level.
- Disputed receivables 13.87 Lakh gross (good 10.78; doubtful 3.09) (C-Note 15, p.127).

## 5. INVENTORY

Consumables and chemicals only: 318.19 Lakh (FY25 264.51), +20.3% against revenue +77.3% (C-Note 14, p.126; derived). Method: lower of cost and NRV, FIFO (C-Note 2.4 O, p.113). Consumption 587.04 = opening 264.51 + purchases 640.72 - closing 318.19 (C-Note 21, p.129). Standalone inventory 35.63 vs nil, new (S-Note 15, p.175); the AR standalone inventory turnover ratio 379.62 is meaningless on a one-year stock (S-Note 34 E, p.185). Write-downs or obsolescence: NOT FOUND IN DOCUMENT. Inventory is a service-business input, not finished goods. 🟢 Inventory days: 318.19 / consumption-and-direct basis not meaningful; skip.

## 6. INVESTMENTS, SUBSIDIARIES, LOANS

Standalone non-current investments, all at cost, unquoted, no provision (S-Note 12, p.175):

| Subsidiary | Holding | Carrying FY26 | FY25 |
|---|---|---|---|
| ITCPL | 5,09,804 shares, 100% | 8498.99 | 3299.26 |
| QTIPL | 2,34,000 shares, 100% | 500.00 | 500.00 |
| LabOps Global | 740 shares, 74% | 0.07 | nil |
| Total | | 8999.06 | 3799.26 |

- 🔴 R1 Carrying value versus net assets. ITCPL's share of consolidated net assets is 752.02 Lakh and its FY26 net profit 710.83 Lakh (C-Note 34, p.140). Standalone cost 8498.99 is 11.3x those net assets (derived). Consolidated goodwill on consolidation is 7811.56 Lakh = 51.2% of consolidated equity 15,242.60; tangible equity derived 7,431.04 before other intangibles. ITCPL FY26 profit 710.83 is 8.4% of the 8498.99 carrying cost (derived). 48.7% of consolidated net profit comes from ITCPL (C-Note 34, p.140). No impairment test, discount rate or growth rate is disclosed; Note 40 says "no indication" (p.143). Loss-making subsidiaries: QTIPL net assets -61.41, FY26 loss 24.94 (FY25 loss 36.47); LabOps net assets/loss -23.07 (C-Notes 33d, 34, pp.139-140). QTIPL carried at 500.00 in standalone against net assets of -61.41: the difference is carried in goodwill. Total goodwill split by entity: NOT FOUND IN DOCUMENT.
- Acquisition effects (C-Note 33d, p.139): ITCPL acquisition raised consolidated assets by 4788.77 and liabilities by 4036.75; post-acquisition revenue 5651.73 and net profit 613.80 (the AR applies these to the post-control period, which for FY25 began 11 Sep 2024; wording ambiguous).
- Food testing lab, Mumbai, slump sale from 1 Sep 2025: price 882.00, net assets 662.14, goodwill 219.86 (C-Note 33d(iv), p.140; S-Note 36, p.187). Goodwill is 24.9% of the price (derived). Seller NOT FOUND IN DOCUMENT.
- LabOps Global: 740 shares for 0.07 Lakh at face value, 74% (C-Note 33d(i), p.139). Negative minority interest absorbed by the holding company: 6.66 Lakh (C-Note 38, p.141).
- Control without majority: until 10 Sep 2025 QLL held 49.99% of ITCPL and consolidated it through control of the board (C-Note 33c(ii), p.139). The other holders were TIC Services (35.01%, derived 1,78,488 / 5,09,804) and Mr. Khullar (15.0%, derived).
- Loans to subsidiaries (S-Note 27 III(b), p.182): ITCPL balance 162.67 (max in year 1019.64); QTIPL 143.13; LabOps 6.20; total 311.99, standalone LT loans and advances to related parties 312.00 (S-Note 13, p.175). Rate 8.50%, repayable after three years, interest waived. "given for general business purposes (including investment purposes)".
- Consolidated long-term loans and advances 625.96 (capital advances 342.59; other loans and advances 283.37 with no description) (C-Note 12, p.126). 🟡
- Other investments, ICDs to third parties, unrealised gains: none disclosed. NOT FOUND IN DOCUMENT.

## 7. BORROWINGS

Consolidated (C-Notes 5 and 8, pp.117-121), INR Lakh:

| Instrument | FY26 | FY25 |
|---|---|---|
| Term loans from banks (LT) | 5019.39 | 2248.91 |
| Term loan from NBFC, secured (LT) | 356.19 | nil |
| Vehicle loans (LT) | 102.25 | 107.38 |
| Working capital loans (LT, secured) | nil | 271.16 |
| Unsecured bank term loan | 3.87 | 14.37 |
| Unsecured NBFC term loan | 138.89 | nil |
| Loans from related parties (LT) | nil | 224.32 |
| Loans from others | 93.06 | 30.00 |
| Finance lease (LT) | 298.50 | 189.95 |
| Long-term total | 6012.15 | 3086.09 |
| Bank overdrafts | 1450.10 | 933.30 |
| Current maturities of LT debt | 917.30 (727.49 + 82.43 + 35.78 + 10.49 + 61.11) | 665.56 |
| Working capital demand loans | 810.00 | 293.50 |
| Related-party loans, unsecured (ST) | 108.00 | 20.00 |
| Short-term total | 3285.40 | 1912.36 |
| Finance lease current (Other CL) | 65.93 | 30.72 |

Derived: total debt incl. current finance lease 9363.48 vs 5029.17 (+86%). Debt/equity 0.61 (derived); against derived tangible equity 7,431.04, 1.26x. Debt/EBITDA about 3.1x using EBITDA 2987.18 (PBT before prior-period item 1838.02 + depreciation 668.62 + finance cost 480.54, includes other income 52.74). EBIT/finance cost 4.8x; with 143.14 capitalised interest added back to cost, 3.7x. Consolidated current ratio 5875.55/5625.13 = 1.04 (FY25 1.31); standalone 0.92 (S-Note 34 A, p.185). Standalone DSCR 1.92 (2.21), debt/equity 0.45 (0.33) (S-Note 34, p.185). Standalone ROCE 7.4% (10.7%), ROE 6.9% (8.9%) as the company states them (S-Note 34 D, J, pp.185-186).
- Rates: floating 7.60% to 11.05% (spread over repo, 6-month CD, "LTPR") for banks and NBFCs; fixed 9.75% on some loans; unsecured NBFC working capital loan 14.36 at fixed 16.50% (C-Note 5, pp.117-120).
- Security: hypothecation of current and movable assets; equitable mortgage on SKM Realcon properties at C-40 Sector 57 and C-100 Sector 2 Noida; on QLL's own Panchkula Barwala plots 297/298 for the 1300.30 loan; corporate guarantees of TIC Services, SKM Realcon, ASC Consulting and ITCPL; personal guarantees of Nayak, Grover, Alok Agarwal, Anju Agarwal (C-Note 5, p.117-119). Working capital demand loan of 310.00 is secured against equity mutual funds owned by Mr. Sanjiv Khullar, the former 15% ITCPL shareholder (C-Note 8 note (iii), p.121) 🟡.
- Covenants, breaches, waivers: NOT FOUND IN DOCUMENT. Term changes: none disclosed.
- Defaults: Standalone Note 5 reports one 6-day delay on a vehicle loan, 2.19 Lakh (S-Note 5, p.170). CARO clause (ix)(a) lists Axis Bank vehicle loan, 1.57 principal and 0.61 interest, "number of delays: 6" (p.153). The note says one instance, the CARO says six delays. 🟡 minor.
- Repayment pattern: individual EMIs are listed (C-Note 5, pp.117-119). One loan repays 77 EMIs of 28.33 Lakh starting 10 April 2027 (= 339.96 Lakh a year, derived); another 96 EMIs of 18.73 starting 7 Feb 2026; the loan-to-EMI mapping is lost in the text extraction (PDF check needed). A consolidated five-year repayment schedule: NOT FOUND IN DOCUMENT. Current maturities FY27: 917.30 Lakh.
- Cash and equivalents includes "Debit balance in overdraft account" 348.28 Lakh = 62.7% of reported 555.40 (C-Note 16, p.127; C-CF p.105) while bank overdraft liabilities are shown separately at 1450.10. The AR does not explain the item. 🟡
- Related-party borrowings: 108.00 Lakh ST (ASC 20.00; AAL Biosciences 88.00) (C-Note 26, p.133).
- NCD plan (board approvals Dec 2025, per B00 announcements): no NCD in the notes at 31 Mar 2026. NOT FOUND IN DOCUMENT; not expected.

## 8. TRADE PAYABLES

Consolidated 939.26 Lakh (FY25 728.34): MSME 144.24 (138.09), others 795.02 (590.25) (C-Note 9, p.122). Ageing (INR Lakh): unbilled 128.11; under 1 year 739.21; 1-2 years 15.23; 2-3 years 11.45; over 3 years 45.27. MSME over 1 year: 1.49 + 7.72 + 8.90 = 18.11. No disputed dues.
- MSME: principal outstanding 129.18 (FY25 125.40), interest due and unpaid 15.07 (12.69) (C-Note 36, p.141). 129.18 + 15.07 = 144.25 equals the MSME payable (derived), so the balance includes accrued interest. Interest on MSME dues charged to finance cost 2.37 (2.87) (C-Note 23, p.129). MSME dues over 45 days as a separate figure: NOT FOUND IN DOCUMENT. MSME status rests on vendor confirmation only (note, p.141) 🟡. Payable older than 1 year is 71.95 Lakh (7.7%, derived).
- Payable days: standalone credit purchases 3058.88 and average payables 477.67 give turnover 6.40 (5.93), about 57 days (derived) (S-Note 34 G, p.186). Consolidated payable days: NOT FOUND (no consolidated ratio table).

## 9. PROVISIONS AND EMPLOYEE BENEFITS

Consolidated (C-Notes 7, 27, pp.120, 135-136), INR Lakh: gratuity 190.40 (FY25 133.41); leave encashment 56.00 (20.47). Both unfunded, no plan assets. Gratuity current 71.18, non-current 119.22.
- Assumptions: discount rate 7.78% (FY25 6.99%); salary escalation 4.00%; attrition 45% in every age band; IALM 2012-14; retirement 58. 🟡 A 45% attrition rate across all ages and a 4% pay growth rate both shorten expected service and lower the liability. The AR gives no sensitivity analysis: NOT FOUND IN DOCUMENT.
- Consolidated gratuity movement: opening 133.41, interest 9.38, current service 25.52, past service 13.62, benefits paid 23.65, actuarial loss 32.11, closing 190.40. Leave: 20.47, 1.43, 26.79, 20.49, 17.14, 3.97, closing 56.00.
- 🟡 R5 P&L versus actuarial charge. The actuarial tables show expense of 80.63 + 52.68 = 133.31 Lakh (C-Note 27 V, p.136). The P&L line "Gratuity & Leave Encashment" is 111.52 (C-Note 22, p.129). Gap 21.79 Lakh, unexplained. Standalone shows the same gap: tables 24.48 + 26.20 = 50.68 against P&L 28.90, gap 21.78 (S-Note 29 V, p.184; S-Note 23, p.177). The balance sheet liability follows the actuarial table (it rolls forward to the table's closing), so the gap is not in the liability. Where the 21.8 Lakh was charged: NOT FOUND IN DOCUMENT (possible capitalisation or another expense line; not stated).
- Provision count: PF contribution 216.98 (FY25 142.59). Next-year expected expense: gratuity 38.01, leave 30.60 (C-Note 27 VIII, p.136).
- Warranty, decommissioning, onerous contracts, litigation provisions: none disclosed. NOT FOUND IN DOCUMENT.
- Acquisition adjustment in FY25 gratuity: 99.86 Lakh (C-Note 27 II, p.135).

## 10. DEFERRED TAX AND TAX

- Consolidated tax: current 433.61, deferred (14.00), prior-year (47.66), total 371.95 on PBT 1832.10 = 20.3% effective (derived) (C-P&L p.103). Current tax alone is 23.7%. The prior-year credit is 3.3% of consolidated PAT (derived). Standalone: current 195.70, deferred 7.69, prior-year (40.10), total 163.29 on PBT 959.73 = 17.0% (S-P&L p.159); prior-year credit is 5.0% of standalone PAT (derived).
- 🟡 Statutory-to-effective rate reconciliation, MAT credit, tax regime: NOT FOUND IN DOCUMENT.
- Deferred tax (consolidated, C-Note 6, p.120): gross DTL 321.06 (FY25 208.87) from the net block difference; DTA 260.73 (134.54); net DTL 60.33 (74.33). DTA includes a line for "Brought forward business losses and unabsorbed depreciation"; the extraction cannot assign the 96.59 / 91.72 values to rows with confidence (PDF check recommended). Unrecognised DTA: NOT FOUND IN DOCUMENT. Policy: DTA on losses only with virtual certainty (C-Note 2.4 H, p.112).
- Standalone net DTL 69.47 (S-Note 6, p.171); the standalone DTA in the extraction is partly scrambled; stated net figures only.
- Advance income tax 226.22 Lakh net of provision 460.08 (C-Note 13, p.126).

## 11. REVENUE DETAILS

- Revenue 12451.81 Lakh (FY25 7022.69, +77.3%): testing services 12414.17 and IT services 37.64 (FY25 2.26) (C-Note 19, p.129). The +77.3% includes ITCPL for the full year versus 11 Sep 2024 onward (C-Note 33d, p.139). Like-for-like growth: NOT FOUND IN DOCUMENT.
- Standalone revenue 6762.45 (4586.48), +47.4% (S-Note 20, p.177). Contribution from subsidiaries (derived): consolidated 12451.81 less standalone 6762.45 = 5689.36 before eliminations of 177.58 intra-group sales. ITCPL post-control revenue contribution 5651.73 (C-Note 33d, p.139).
- Geography: India 12118.75 (97.3%), outside India 333.06 (2.7%); FY25 6981.50 and 41.19. Standalone exports 111.12 (31.09) FOB (C-Note 29, p.137; S-Note 28, p.182).
- Segments: one primary segment, testing and inspection (C-Note 29, p.137; S-Note 41, p.189). No sector-wise or sub-vertical breakup: NOT FOUND IN DOCUMENT.
- Contract assets: unbilled 206.67 Lakh in receivables. Contract liabilities: customer advances 151.18 (140.72) (C-Note 10, p.122). Unsatisfied performance obligations: not applicable (completed-service method), NOT FOUND IN DOCUMENT.
- Top customer revenue: NOT FOUND IN DOCUMENT.
- Other income 52.74 Lakh = 2.9% of PBT; liabilities written back 17.06 (FY25 25.95), interest on tax refund 13.60, FX gain 8.61 (C-Note 20, p.129). 🟢

## 12. OTHER CRITICAL NOTES

12.1 Share capital and dilution 🟢/🟡. Share count 1,16,52,031 (FY25 99,79,500). The +16,72,531 are the swap shares (C-Note 3, p.114). Authorised 1,50,00,000 shares. Authorised headroom 33,47,969 shares (derived). Basic = diluted EPS (no dilutive instruments in the notes). ESOP: NOT FOUND IN DOCUMENT. Warrants: none at 31 Mar 2026 (events after the AR date).
 Promoter holding: TIC 56.46% (+2.27 points); public holders over 5%: Ashish Kacholia 4.35% (5.07%), Madhulika Agarwal 4.35% (5.07%), both diluted by the swap (C-Note 3 D, p.114). Nominee shares held by Alok Agarwal, Nayak, Grover and Anju Agarwal for TIC (1 share each).
12.2 Preferential issue FY25: 26,07,600 shares at 198.33, gross 5171.65, net 4805.65 after 366.00 expenses (C-Note 35, p.140; C-Note 4, p.116). Utilisation statement for this issue: NOT FOUND IN DOCUMENT. Cash flow suggests use for 3299.26 (ITCPL) plus 500.00 (QTIPL) = 3799.26 (S-Note 12, p.175; S-CF p.160).
12.3 IPO proceeds (standalone, S-Note 38, p.188): net 1831.18 Lakh. Capex 622.38 (spent 210.16 in FY24, 412.22 in FY25); promoter loan repayment 818.16 (FY24); working capital 250.00 (196.60; 53.40); general corporate purposes 140.64 (52.91; 87.73). Unutilised nil. 🟡 Note (i): machines of "higher configuration/capability were purchased instead of those mentioned in the prospectus". IPO expenses stated at 139.84 (against securities premium) vs gross 1964.40 less net 1831.18 = 133.22: 6.62 Lakh unreconciled (derived) 🟡.
12.4 Capex and CWIP 🟡. Consolidated CWIP 4528.25 (1566.34): owned 4356.12 and leased 172.13. Ageing: under 1 year 3309.59; 1-2 years 834.84; 2-3 years 232.00; over 3 years 151.81 (C-Note 39(iii), p.142). 26.9% of CWIP is older than one year (derived). CWIP includes land and building under development 1813.01, mortgaged against the 1300.30 bank loan (C-Note 11c, p.124). The statement "no projects overdue or over cost" (p.142). Intangible assets under development 44.21. Capital advances 342.59.
12.5 Fixed assets. Consolidated PPE net 7145.72 (5899.81); gross block 9458.87; additions 767.54 + acquisition 541.95 + capitalised 590.67 (C-Note 11a, p.123). Acquired PPE 541.95 relates to the Mumbai lab slump sale. Depreciation 668.62 (425.17).
12.6 Cash flow quality (C-CF pp.104-105; S-CF pp.160-161). Consolidated CFO 1387.16 vs PBT 1832.10 = 75.7% (derived); against EBITDA 2987.18, 46.4% (derived). FY25 CFO 1049.93 / PBT 1041.84 = 100.8%. Standalone CFO 715.00 / PBT 959.73 = 74.5% (FY25 801.35 / 710.68 = 112.8%). Consolidated capex (PPE 1192.97 + CWIP 3391.53 + intangibles 51.71) = 4636.21; derived free cash flow -3249.05. Financing inflow 3710.97 (term loans 4941.86 taken, 2124.35 repaid, short-term +1373.04). 🟡 Oddities: (a) the consolidated CFO deducts "Minority Interest (97.92)" from operating profit although it is a non-cash allocation; (b) "Acquisition of Goodwill" is a +94.42 inflow in consolidated investing against a (219.86) outflow standalone; no explanation (C-CF p.104; S-CF p.160); (c) an FY26 working capital build of 1872.82 labelled as subtotal is the post-WC figure.
12.7 Equity bridge. Reserves: securities premium 11,264.75 (6232.27) after 5032.48 added from the swap; consolidated surplus 2812.65 (1450.42) (C-Note 4, p.116). No direct debit/credit to reserves other than share issue items. 🟢
12.8 Foreign exchange: exposure small, 100.86 Lakh unhedged receivables; no hedging policy disclosed (C-Note 30, p.137). 🟢
12.9 CSR: required 11.27, spent 11.27 (2% of average net profit 563.44) (CSR Annexure F, p.87; S-Note 42, p.189). No shortfall. 🟢
12.10 Events after balance sheet date: none (C-Note 41, p.143; S-Note 43, p.190). Note audit sign-off 20 May 2026 precedes the AR date of 29-30 Aug 2026. Board waiver of intercompany interest is dated 20 May 2026.
12.11 Segment/geography: above. Going concern: basis stated in C-Note 2 (p.106) and S-Note 2.1 (p.162); no material uncertainty language anywhere. CARO clause (xix) adverse listing for QTIPL and LabOps (see section 3). Standalone CARO (xix) text: nothing causes the auditor to believe a material uncertainty exists (p.155).
12.12 Standalone Reg 34 / ratio table: current ratio 0.92; ROE 6.9%; ROCE 7.4%; the company explains a 31% ROCE fall as due to equity issue and borrowings (S-Note 34 J, p.186). The standalone EBIT figure used there is 1206.80.
12.13 CARO (standalone) issues: delay in refunding excess share application money 2.27 Lakh (Clause 3(v); consolidated Note 37 says 2.28 Lakh, "not traceable", pending since 31 Oct 2024; C-Note 37, p.141; CARO p.152). Same item in Other current liabilities (C-Note 10, p.122). 🟡 small.
12.14 Audit trail: accounting software with audit trail operated throughout (p.98; p.150). IFC opinion unmodified (pp.100-101; pp.156-157). 🟢

## PASS 1 SUMMARY: TOP 10 FINDINGS (ranked by investor importance)

| Rank | Finding | Anchor | Rating |
|---|---|---|---|
| 1 | Goodwill on consolidation 7811.56 Lakh = 51.2% of consolidated equity; standalone cost of ITCPL 8498.99 vs ITCPL net assets 752.02 and FY26 profit 710.83; no impairment test, rates or CGU disclosed ("no indication") | C-Notes 11e, 33, 34, 40 (pp.125, 139-140, 143); S-Note 12 (p.175) | 🔴 |
| 2 | Promoter share swap: 5199.73 Lakh of new shares at 310.89 (3640.15 to TIC Services) for the remaining 50.01% of ITCPL; implied ITCPL price per share +57.5% in 12 months; no valuation report in the notes | C-Notes 3, 26, 38 (pp.114, 131, 141); C-Note 33d (p.139) | 🔴 |
| 3 | Promoter-group credit support: 6874.29 Lakh covered of about 8,159 bank debt (84%); corporate guarantees of TIC, SKM Realcon, ASC; personal guarantees; mortgages on SKM-owned properties; cross-guarantees QLL/ITCPL; debt up 86% to 9363.48 | C-Notes 5, 8, 26 (pp.117-121, 133-134); C-Note 28 (p.137) | 🔴 |
| 4 | Advances to AAL Research and Solution 148.00 (balance 151.06) and AAL Biosciences 262.00 given and recovered, loans of 148.00 taken, while the same notes state no loans to related parties; the destination line in the balance sheet is not identifiable | C-Note 26 (p.133); C-Note 39 (p.141); C-Notes 12, 17 (pp.126, 128) | 🔴 |
| 5 | Receivables: aged stock 944.10 Lakh over 6 months (22.4% of gross), 220.46 over 3 years, provision only 6.08; standalone days 93.8 to 106.4; about 795 Lakh of the aged stock sits in subsidiaries | C-Note 15 (p.127); S-Note 16 (p.176) | 🟡 (FLAG-CASH candidate) |
| 6 | Cash conversion: CFO/PBT 75.7% consolidated (74.5% standalone), CFO/EBITDA 46%; capex 4636 Lakh; CWIP 4528 (+189%) of which 26.9% older than 1 year; borrowing cost capitalised 143.14 = 7.8% of PBT | C-CF pp.104-105; C-Notes 11c, 32, 39(iii) (pp.124, 138, 142) | 🟡 |
| 7 | Related-party cost and pay growth: SKM rent 21.60 to 153.60; KMP and relatives' remuneration 222.81 to 430.82 (+93%); guarantee fees only 0.20 each | C-Note 26 (pp.131-134) | 🟡 |
| 8 | Intercompany loans interest waived (8.50%) by resolution dated 20 May 2026; CARO flags clause 3(iii)(b) for QLL and ITCPL; clause 3(xix) adverse listing for QTIPL and LabOps | CARO consolidated Annex A (p.99); S-Note 13 (p.175) | 🟡 |
| 9 | Employee benefit charge in P&L is 21.8 Lakh lower than the actuarial expense (consolidated 111.52 vs 133.31; standalone 28.90 vs 50.68); attrition 45% and pay rise 4% flatter the liability | C-Notes 22, 27 (pp.129, 135-136); S-Notes 23, 29 (pp.177, 183-184) | 🟡 |
| 10 | Load-bearing facts: NCI nil; owners' PAT 1362.22 Lakh (not 6.30 cr); EPS 12.49 (13.38 is total PAT over weighted shares); consolidated short-term borrowings 3285.40 (the 16.24 cr is standalone); IPO money 818.16 Lakh repaid the promoter loan | C-P&L p.103; C-Note 38 (p.141); S-Note 8 (p.171); S-Note 38 (p.188) | 🟢 reconciled, 🟡 for IPO use |

Ratings count in this pass: 🔴 4, 🟡 about 30, 🟢 minor items (CSR, FX, CARO audit trail, contingent tax 0.63% of net worth).
Interim leaning only: FLAG-CASH candidate (receivable ageing and CFO/PBT), pending Pass 3 consolidation. Auditor fee 3.84 Lakh on a group of 12,452 Lakh revenue is a disclosure-quality marker, not a finding of fault.
