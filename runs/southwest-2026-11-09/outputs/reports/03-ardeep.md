# STAGE 3: ANNUAL REPORT DEEP DIVE (BACKWARD READ), SOUTHWEST, FY26

Run date 2026-11-09. Model: claude-sonnet-5-5. Source: inputs/annual-report/Annual_Report_2026.txt (20th AR, FY ended 31 Mar 2026). Prior-year comparison: Annual_Report_2025.txt. Notes baseline: outputs/reports/02-notes.md (B02).

Unit: INR Lakhs on the face of the AR (S p.113 to p.115, C p.166 to p.168). Nothing converted. Where the AR prints INR Mn or crore, the anchor says so. Anchors use the "[page N]" marker in the .txt. "S" = standalone, "C" = consolidated. "(derived)" = my arithmetic on anchored figures. "[INFERENCE]" = reading beyond the printed number, with the confirming observation named. FY25 AR anchors use its own page markers.

Read order: back pages first (consolidated and standalone auditors, then CG report, MD&A, Board's report), Chairman and JMD letters last.

Load-bearing facts carried from the Spear / COMPANY MEMORY and checked first: (1) guidance against delivery, (2) order book quality and concentration, (3) Jharkhand coal block, (4) cash conversion under rig capex. Each is answered in Phase 4C, 6E and 8.

Input gaps carried from B00 (input_gaps) are listed on the block. Stage-specific gaps: standalone Note 41 body and Note 46 segment table are missing from the .txt (B02); consolidated Notes 42 and 47 used instead. Shareholding pattern files are not held, so pledge data is NOT FOUND IN DOCUMENT in the AR.

---

## PHASE 1: AUDITOR'S REPORT AND CARO

### 1A Core opinion
| Item | Finding | Anchor |
|---|---|---|
| S opinion | Unmodified: "give a true and fair view in conformity with the Indian Accounting Standards" | S Auditor's Report, p.101 |
| S going concern | Basis paragraph only; CARO xix finds no material uncertainty for the parent: "nothing has come to our attention ... Company is not capable of meeting its liabilities ... within one year" with a non-assurance caveat | S Annexure A cl. xix, p.109 (resolves B02's unresolved page) |
| C opinion | Unmodified, based "on the reports of the other auditors" | C Auditor's Report, p.159 |
| C going concern | Section "Material Uncertainty Related to Going Concern": South West Resources Private Limited (formerly Pilot Pipelines) "accumulated losses amounting to INR 314.88 Lakhs ... fully eroded the net worth ... current liabilities exceeded its current assets by INR 266.40 Lakhs ... material uncertainty that may cast significant doubt ... results ... prepared on a going concern basis as the Company has letter of financial support from Holding Company" | C p.159 |
| Letter of support elsewhere | grep of the full .txt finds the phrase only at C p.159. Amount, term, enforceability: NOT FOUND IN DOCUMENT | whole AR |
| Internal financial controls | Adequate and effective, unmodified (S and C) | S p.112, C p.165 |
| Audit trail | Operated all year, no tampering | S p.104, C p.163 |
| Date | Both opinions dated 4 May 2026, same day as Board approval | S p.105, C p.163, Note 1 p.116 |

### 1B Key Audit Matters
| KAM | Why key | How addressed | Risk |
|---|---|---|---|
| Revenue recognition: revenue "for the completed performance obligation which is part of incomplete contract" on stage of completion | Management estimates of stage of completion and price allocation | Policy assessed, controls tested, "samples of revenue transactions" compared to documents (S p.101-102; C p.159-160) | Yellow. Procedure text is generic. S cites "note 32" for revenue policy; revenue is Note 31 and the policy is Note 1(c) (S p.116-117). Unbilled 2,613.79 sits inside receivables (Note 12 S p.131). |
| Not raised as KAMs but larger than revenue judgement | E&E asset 1,930.58 (9.5% of S equity, derived); ECL 187.95 against 11,832.46 gross; interest-free SWR loan 410.34; JV profit 146.90 | None | Yellow. Largest estimates carry no KAM. |

### 1C Emphasis of Matter and Other Matters
| Item | Detail | Anchor |
|---|---|---|
| Emphasis of Matter | None in S. In C, the going concern paragraph above is the only emphasis-type item | S p.101-105; C p.159 |
| Other Matter (C) | "Group's share of net income ... INR 146.90 Lakhs ... in respect of joint ventures, whose financial information have not been audited by us ... unaudited and furnished by management" | C p.161 |
| Other Matter vs CG report | C opinion cites "reports of the other auditors on separate financial statements", yet the CG report states Doogar & Associates is the auditor of all three subsidiaries (fees 0.25, 0.20, 0.15 lakh) (CG p.86). Boilerplate or a true split is unclear. | C p.159; CG p.86 |

### 1D CARO 2020 clause by clause (standalone, Annexure A, S p.106-110)
| Clause | Finding | Amount / flag |
|---|---|---|
| i PPE | Records kept, physically verified, titles in company name | Clean |
| ii inventory | Verified, no 10% discrepancy; quarterly bank returns "generally in agreement" with books | Yellow word "generally"; no reconciliation difference quantified (p.106) |
| iii loans | Granted during year: JV 140.23, Others 1,100.00, Subsidiaries nil. Outstanding: subsidiaries 410.15, JV 257.86, others 0.19. Related-party loans 410.34 = 61.41% of loans. Repayable on demand; "payment of interest has been regular" | Red for opacity. Note 52 (S p.154) assigns the whole 410.34 to SWR, CARO splits it 410.15 / 0.19 (0.19 mismatch, hygiene). SWR loan is interest-free (B02) yet CARO says interest regular |
| iii(c) | Loans demanded during year "have been received": the 1,100.00 round trip | Note 48 S p.148 |
| vii disputed dues | Income tax ITAT New Delhi FY2009-10 115.85 (deposit 23.17); GST Appellate FY2021-22 397.59 (deposit 23.34); entry tax 18.24 + 4.81 + 12.71; VAT 4.50 + 1.73; GST FY2018-19 1.33, FY2020-21 3.47, FY2025-26 2.39 | Yellow. Total of the table 562.62 (derived) ties to Note 42 C other contingent liabilities 562.62 (C p.185) |
| ix borrowings | No default, not wilful defaulter, term loans applied for purpose, no short-term funds for long-term use | Clean (p.108). Yellow nuance: current borrowings rose to fund 3,900.25 plant additions (Phase 3) |
| xi fraud | No material fraud; ADT-4 not required; no whistle-blower complaints | Clean (p.109) |
| xiii | s.177 and s.188 complied | Clean as printed; Board's report says no s.188 contracts (Board p.49) while Note 48 shows large related-party flows. Contradiction logged (Phase 5E) |
| xvii cash losses | Parent: none in FY26 or FY25 | Clean (p.109) |
| xix | See 1A | Clean |
| xx CSR | No unspent amount. Required 27.03, spent 24.26 after opening excess 4.91, closing excess 2.14 (Note 47 S p.146) | Clean |
| xxi (consolidated) | Adverse remarks: South West Oil Field Services Pvt Ltd and South West Geo Services Pvt Ltd, both **clause xvii** (cash losses) | C p.162. New versus B02. Immaterial in rupees (SWOFS loss 0.64, SWGS loss 0.50, AOC-1 p.54) but shows two group entities with no revenue and cash losses |

### 1E Auditor continuity
| Item | Finding | Anchor |
|---|---|---|
| Firm | Doogar & Associates, FRN 000561N, partner Vardhman Doogar | S p.105 |
| Tenure | Re-appointed at the 18th AGM (27 Sep 2024) for 5 years until the 23rd AGM. First appointment year: NOT FOUND IN DOCUMENT | Board p.45 |
| Rotation | Not due before the 23rd AGM | Board p.45 |
| Fees (S) | Audit 5.00 (PY 4.80), limited review and other 1.00 (PY 0.20), reimbursement 0.65; total 6.65 (PY 5.00) | Note 39 S p.138 |
| Fees (C) | Total 7.25 (PY 5.35); audit 5.60 | Note 40 C p.184 area; CG p.86 |
| Non-audit to audit | 1.00 / 5.00 = 20% (derived), no flag | |
| Scale | 6.65 lakh is 0.027% of revenue 24,292.95 (derived) for a group with 33,146.25 of assets | Capacity question, not a finding |
| Network entity fees | NIL | CG p.86 |

### 1F Standalone vs consolidated
| Item | Finding |
|---|---|
| Extra items in C | Going concern paragraph (SWR); JV unaudited 146.90; two subsidiary CARO xvii remarks (C p.159, p.161, p.162) |
| Profit gap | C PAT 3,302.70 vs S 3,080.05 = 222.65 (derived): JV share 146.90, rest subsidiaries and eliminations (SWR profit 76.88, AOC-1 p.54) |
| Reliance on other auditors | Statement present, auditor identity for JV Alara LLC and Al Hadeetha NOT FOUND IN DOCUMENT |

**Phase 1 verdict: 🟡 Watch.** Clean parent opinion; the weight sits in the SWR going concern paragraph with an unquantified parent letter, unaudited JV profit, and no KAM on E&E or ECL.
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop on Phase 1, because the parent opinion is unmodified and the going concern doubt is confined to a subsidiary with 42.38 invested and 410.34 lent (total 452.72, derived, 2.2% of S equity).

---

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

### 2-V. Verification of the B02 Top 15 against the AR

| Rank | B02 claim | AR check | Result |
|---|---|---|---|
| 1 | Gross receivables 11,832.46 vs 7,534.67 (+57.0%); billed 9,218.67 vs 4,576.59; advances 342.23 to nil; cash 88.81 vs 1,824.50; CFO 1,233.87; capex 4,254.36; E&E 499.77 | Note 12 S p.131 (11,832.46; 7,534.67; billed = 11,832.46 less 2,613.79 = 9,218.67 and 7,534.67 less 2,958.08 = 4,576.59, derived); Note 30 S p.136; Note 13 S p.131; CF S p.115. +57.04% (derived) | ✓ verified |
| 2 | Three customers 72.27% (PY 48.00%); credit-risk text calls concentration low | Note 46 S p.146; Note 49 S p.150 "evaluates the concentration of risk ... as low, as its major customers are Public Sector Undertakings. All debtors are good and realizable within the current financial year" | ✓ verified |
| 3 | SWR: net assets (264.94), loan 410.34 (61.41%), investment 42.38, 632.01 purchases, only 66.53 removed on consolidation | Note 52 C p.202 (264.94); CARO iii S p.107 (410.34, 61.41%); Note 7 S p.129 (42.38); Note 48 S p.148 (632.01); S opex 10,407.30 less C opex 10,340.77 = 66.53 (derived) | ✓ verified. Extension in 2B below |
| 4 | Commentary contradicts figures (payables, receivables, ROCE, ROE, margin bases) | Note 51 S p.154 text; MD&A p.62; payables 2,387.27 vs 1,823.80 (+30.9%, derived); ROCE 22.06% vs MD&A 23.00%; ROE 16.46% vs 16.21%; margin 12.68% vs 13.58% | ✓ verified. New: MD&A interest cover 5.90 equals standalone EBIT incl. other income 4,973.14 / 842.34 (derived), so MD&A mixes standalone and consolidated bases |
| 5 | 1,100.00 (PY 950.00) round trip; interest 15.62 (PY 3.30) | Note 48 S p.148; CARO iii(a) S p.106 | ✓ verified |
| 6 | E&E 1,930.58; 757.73 older than 3 years; no policy; "PL cum ML underway" vs "completed" | Note 5 S p.129 (499.77 / 348.91 / 324.17 / 757.73); Note 1 S p.116 ("process of obtaining PL cum ML ... presently underway"); Board p.40 ("exploration activities ... have since been completed"); MD&A p.60. Full-text search finds no E&E policy | ✓ verified |
| 7 | Term loans "fixed" 3,624.28 vs fixed borrowings 1,132.21; implied interest 10.99%; gearing 38.4% vs 33.23% | Note 20 S p.134; Note 49 S p.152-153; interest 777.45 / average borrowings 7,076.37 = 10.99% (derived); gearing 6,730.01 / 20,251.42 = 33.23% printed, 7,772.53 / 20,251.42 = 38.4% on its own definition (derived) | ✓ verified |
| 8 | ECL 187.95 covers over-one-year tail 189.34; 173.13 over three years | Note 12 S p.131 (16.21 + 173.13 = 189.34; allowance 187.95 = 1.59% of gross, derived). B02's "115.69 of old balances left ageing unexplained": 131.90 (1-2y) less 16.21 (2-3y) = 115.69 left that bucket; the AR does not say if collected or written off. See bridge in 3A | ✓ verified, interpretation tightened |
| 9 | Contingent 2,812.69 = 13.8% of net assets; margin-money cover fell 98.9% to 61.2% | 2,250.07 + 562.62 = 2,812.69 (Note 42 C p.185); 2,812.69 / 20,352.94 = 13.8% (derived). Cover: FY25 (2,157.36 + 71.96) / 2,253.78 = 98.9%; FY26 (1,042.52 + 348.05) / 2,250.07 = **61.8%** (Note 14, Note 9 S p.131, p.130; derived) | ✗ discrepancy: triple-pass 61.2%, AR 61.8%. FDs also back fund-based lines (Note 9 footnote S p.130), so ratio is indicative only |
| 10 | Related-party exposure 855.35 (4.2% of equity); Alara Resources Ltd 288.00, FV 274.76; Al Hadeetha 39.92; Omani loan 257.86 (+183%); JV profit 146.90 unaudited | 288.00 and 39.92 CF S p.115; 274.76 Note 7 S p.129; 257.86 vs 91.09 +183.1% (derived); 146.90 C p.161. Visible components (288.00 + 39.92 + 257.86 + 111.66 + 0.08) = 697.52 (derived). I cannot reproduce 855.35 | ✗ discrepancy: total 855.35 not reproducible from stated parts; rest verified |
| 11 | Sub-contract 8,109.98 (+219%) = 33.4% of revenue; coal trading 4,533.92 stopped; depreciation +150.50 on additions 3,900.25 | Note 35 S p.137 (8,109.98 vs 2,539.14 = +219.4%; 33.4% derived); segment note C p.192 (4,533.92 to nil); Note 2 S p.127 (additions 3,900.25). Depreciation total 1,144.33 vs 959.85 = **+184.48** (PPE 1,089.92 vs 902.60 = +187.32), Note 38 S p.138 | ✗ discrepancy: +150.50 not reproduced; AR shows +184.48 total |
| 12 | Remuneration +75.2% to 425.29; PY digits transposed | Note 48 S p.149 (425.29 vs 242.71 = +75.2% derived); C table 263.13 vs 236.13 | ✓ verified |
| 13 | Warrants: 2,797.43 inflow 10 Jul 2026, no subsequent-event note; dilution 9.46% | Board p.41; CG p.82 (279,742,900 rupees); 2,821,411 / 29,830,011 = 9.46% (derived); no events-after note found in S or C | ✓ verified |
| 14 | Inventory 5,093.93 = 139% of consumption; sundry assets written off 197.79 (4.5x) | Note 11 S p.130; Note 33 S p.137 (consumption 3,658.63; 139.2% derived); CF S p.115 (197.79 vs 43.86) | ✓ verified. Nature of write-off partly bridged in 3A |
| 15 | Samit: carrying 10.70, net assets (13.51), unexplained 35.79 | Note 51 C p.201 (10.70 vs 24.87; net assets (13.51) vs 39.99; loss 17.71); 53.50 less 17.71 = 35.79 (derived); AOC-1 prints Samit net worth "as on June 30, 2025" (p.55) | ✓ verified |

**Verified 12 of 15; 3 discrepancies** (ranks 9, 10, 11), all in derived or summary figures, none changes a rating.

### 2A Accounting policy aggressiveness (extension)
| Area | Policy / evidence | Read |
|---|---|---|
| Revenue | Ind AS 115, stage of completion on completed performance obligations (Note 1(c) S p.116-117) | Yellow. Unbilled 2,613.79 = 22.1% of gross receivables (derived), PY 2,958.08 = 39.3% |
| Depreciation | Written down value over Schedule II lives (Note 1 S p.117, text near line 6515); rigs on WDV; no life disclosure for rigs | Neutral to conservative (WDV front-loads). FY27 step-up not disclosed |
| Capitalisation | Borrowing costs capitalised "if any" (Note 1 policy); finance cost fully expensed in FY26 (Note 37 S p.138: 842.34) | Yellow. 3,900.25 plant additions plus 499.77 E&E, zero capitalised interest |
| E&E | Carried as "Intangible assets under development" 1,930.58; no E&E policy, no impairment trigger | Red policy gap |
| ECL | Lifetime ECL on provision matrix (Note 49 S p.150); 187.95 allowance | Yellow, tail-sized |
| Ind AS 116 | Lease liability 152.37 (S p.113). Discount rate NOT FOUND IN DOCUMENT in my read | Low weight |
| Policy change | None quantified; Note 66 S p.157 "re-grouped/re-classified" | Neutral |

### 2B Related-party map (extension, percentages of revenue 24,292.95)
| Item | FY26 | PY | % of revenue | Signal |
|---|---|---|---|---|
| Remuneration (KMP) | 425.29 | 242.71 | 1.75% | Staff cost growth 19% median 22% vs KMP +86% (Board p.51) |
| Loans given to KMP-influenced enterprise | 1,100.00 given, 1,100.00 repaid | 950.00 / 950.00 | 4.5% | Interest 15.62 = 1.4% of principal, so average tenor under 2 months at 8.5% (derived). [INFERENCE] bridge or quarter-end financing; confirming observation: borrower name and dates |
| Sale of service to subsidiaries | 282.92 | 35.18 | 1.16% | |
| Purchase of drilling services (subsidiary column) | 632.01 | 748.53 | 2.60% | |
| Purchase of geological / 2D seismic services | 60.99 (subsidiaries); 45.41 (JV Samit) | 47.09; 445.03 (JV, PY) | 0.43% | Samit JV total income 45.41 = 100% parent purchases (Note 51 C p.201) |
| Interest on loans to JV | 11.42 | 5.86 | | |
| Creditors due to subsidiaries/JV | 450.17 and 85.89 | 171.87 and 151.75 | | Parent owes subsidiaries 450.17 while it lent SWR 410.34 |
| Loans (asset) at year end | 431.44 / 293.48 / 0.19 | 507.04 / 103.67 / 0.20 | | |

**Extension, intercompany tie [INFERENCE grade: strong arithmetic].** C revenue 24,302.17 less S revenue 24,292.95 = 9.22 (derived). SWR revenue is 985.15 (AOC-1 p.54, row order reading). Intercompany elimination = 282.92 + 632.01 + 60.99 = 975.92 (Note 48 S p.148; derived), and 985.15 less 975.92 = 9.23 = the group revenue gap. So the RPT columns map to the subsidiaries and SWR books about 99% of its revenue from the parent (derived). The 66.53 net cost elimination equals 10.5% of 632.01, which fits a markup on pass-through drilling. Confirming observation: SWR's own cost split, not in the AR.

Other significant promoter-adjacent lines: 288.00 for 1.56% of Alara Resources Ltd, a KMP-influenced enterprise (Note 7 S p.129; Note 48 p.147), at FV 274.76 (so a 13.24 mark-down in the first year, derived). Personal guarantees by promoters back borrowings (Note 48 S p.149, Notes 20 and 25).

### 2C Contingent liabilities (extension)
| Item | FY26 | % of net worth | % of PAT | Flag |
|---|---|---|---|---|
| Bank guarantees | 2,250.07 | 11.1% (S equity 20,251.42) | 73.1% (S PAT 3,080.05) | Under 25% |
| Tax and indirect tax disputes | 562.62 | 2.8% | 18.3% | Under 25% |
| Total | 2,812.69 | 13.9% on S equity (13.8% on C equity 20,352.94) | 91.3% | Under 25% of net worth and 100% of PAT; no flag by the rule. Probability and cash outflow: NOT FOUND IN DOCUMENT |

(all derived; Note 42 C p.185-186; CARO vii S p.108.) Income tax disputes changed shape: FY25 184.16 (AY2014-15 92.31; AY2016-17 91.85) to FY26 115.85 (ITAT 2009-10). Both older matters left the list and an older year appears; the AR does not explain (C p.185).

### 2D Receivables
| Metric | FY26 | FY25 |
|---|---|---|
| Gross | 11,832.46 | 7,534.67 |
| Not due | 8,452.45 (71.4%) | 4,241.45 (56.3%) |
| Unbilled | 2,613.79 (22.1%) | 2,958.08 (39.3%) |
| Under 6 months overdue | 496.12 | 25.42 |
| 6m to 1y | 80.77 | 4.68 |
| 1 to 2 years | nil | 131.90 |
| 2 to 3 years | 16.21 | 173.14 |
| Over 3 years | 173.13 | nil |
| Share over 6 months | 270.11 = 2.28% | 309.72 = 4.11% |
| Allowance | 187.95 (1.59%) | 100.78 (1.34%) |
| Gross receivable days | 177.8 | 153.5 |
| Concentration | Three customers 72.27% of revenue | 48.00% |

(Note 12 S p.131; Note 46 S p.146; days derived on revenue 24,292.95 and 17,919.32.) The share over six months fell, but the under-six-month overdue bucket rose 19.5x (496.12 vs 25.42). Overdue now sits in the fresh bucket where the ECL matrix applies almost no loss rate (allowance 187.95 against over-one-year tail 189.34).

### 2E Inventory
Stores, spares and diesel only: 5,093.93 (PY 4,624.04), +10.2% (derived) against revenue +35.6% (Note 11 S p.130). 139.2% of annual consumption, about 508 days (derived). Valued "at cost or NRV whichever is lower"; no ageing, no write-down figure. Inventory turnover printed 5.00 (PY 4.00) uses revenue / inventory (Note 51 S p.154), so it flatters. Yellow.

### 2F Borrowings
| Item | FY26 | FY25 | Anchor |
|---|---|---|---|
| Term loans, non-current | 1,599.44 | 1,220.62 | Note 20 S p.134 |
| Current maturities | 2,024.84 | 1,574.48 | Note 20/25 |
| Working capital and demand loans | 4,237.06 | 3,496.29 | Note 25 S p.135 |
| Total | 7,861.34 | 6,291.39 | Note 49 S p.153 |
| Maturity wall | 2,024.84 due within 12 months, 1,599.44 in years 1 to 5, nil after 5 years | | Note 20 S p.134 |
| Covenants | Note 49(c) says the company monitors financial covenants; terms NOT FOUND IN DOCUMENT | | S p.153 |
| Pledge/security | Rigs, vehicles, plant hypothecated; stock and book debts; FDs; promoter personal guarantees; equitable mortgage Gurugram, Ranchi (HDFC) and Nagpur (Axis) | | Note 20, 25 S p.134-135 |
| Rate | Term loans 8.00% to 9.75% fixed at drawdown; CC/WCDL 8.00% to 9.00% | | S p.134-135 |
| Fixed / floating | 1,132.21 / 6,729.13 (PY 1,184.23 / 5,107.16); 50 bp = 33.65 | | Note 49 S p.153 |
| ICDs given | Loans to SWR 410.34, JV 257.86 | | Note 8, 15 |

Wall read: 2,024.84 current maturities plus 4,237.06 working capital lines roll within a year against cash and bank balances of 1,131.33 (88.81 + 1,042.52) at year end. The 2,797.43 warrant money received 10 Jul 2026 (Board p.41) covers the term maturities on a gross basis (2,797.43 vs 2,024.84, derived), but that money was earmarked for capex in the issue terms (utilisation statement covers the FY25 raise only, CG p.86).

### 2G Deferred tax and tax
Effective tax 25.4% (1,050.75 / 4,130.80, derived; PY 25.0%). Deferred tax liability 470.36 (PY 514.69) (Note 23 S p.135). Current tax liability (net) 561.35 vs 125.28 (+436.07) (BS S p.113) while tax paid was 655.17 against a current charge of 1,091.24 (CF S p.115; derived 436.07 difference ties exactly). Interest on taxes, demands and penalties doubled to 16.87 (PY 8.27) (Note 39 S p.138). [INFERENCE] advance tax was paid late or short; confirming observation: Note 44 tax reconciliation and challan dates, not in the AR text I hold.

### 2H Exceptionals, goodwill, ESOP, leases, post-balance-sheet events
Exceptional items: none (S p.114). Goodwill: 11.21 in C only (0.06% of C equity, derived). ESOP/share-based payment: nil (Note 48 S p.149). Leases: 152.37 liability, payments 37.95. Post balance sheet: the 10 Jul 2026 warrant allotment (2,821,411 shares, 2,797.43 received) and the CMD/JMD re-appointments sit in the Board's report (p.41, p.47); no events-after note in S or C. Board's report adds "no material changes and commitments ... except as disclosed elsewhere" (p.42). The promoter Reg 29(2) disposals Jun to Sep 2026 sit outside the AR (B00 manifest: announcements of 25 Jun, 10 Jul, 12 Aug, 11 Sep 2026).

### 2-X. Phase 2 reconciliation with B02 accounting quality 6/10
My Phase 2 verdict is **🟡 Watch, 6/10**, same as B02. Both agree numbers foot and the weakness is disclosure. Two things push me to hold at 6 and not raise it: the tax-deferral and write-off bridge in Phase 3 (CFO is weaker than it looks), and the E&E policy gap. One thing keeps me from cutting to 5: no restatement, no auditor qualification, and the cash-flow receivable line ties to the balance sheet once the write-off is included.

**Phase 2 cross-reference with Phase 1:** the revenue KAM is mirrored in the unbilled balance. The largest estimates (E&E, ECL, SWR) carry no KAM. The SWR going concern paragraph links to the interest-free loan and the unquantified support letter.
**Kill switch (informational):** Based on phases so far, a human reviewer would not have reason to stop, because there is no restatement and the arithmetic ties. The reviewer would want the borrower of the 1,100.00 loan and the SWR letter before sizing.

---

## PHASE 3: FINANCIAL STATEMENTS (cash flow first)

### 3A Cash flow (standalone, S p.115)
| Line | FY26 | FY25 |
|---|---|---|
| PBT | 4,130.80 | 1,977.76 |
| Operating profit before WC | 6,045.46 | 3,484.68 |
| Receivables | (4,456.25) | (1,950.76) |
| Inventories | (469.89) | (281.67) |
| Payables | +563.48 | +1,213.82 |
| Taxes paid | (655.17) | (295.73) |
| **CFO** | **1,233.87** | **2,604.58** |
| Capex (PPE) | (4,254.36) | (221.29) |
| E&E | (499.77) | (348.91) |
| Sale of PPE | 288.91 | 1,151.20 |
| FD (net) | +838.75 | (1,168.83) |
| Investments (ARL 288.00, Al Hadeetha 39.92) | (327.92) | (1.00) |
| Loans to subs/JV (net) | (76.76) | (49.32) |
| LT borrowings net | +829.18 | (1,830.07) |
| ST borrowings net | +740.74 | (949.18) |
| Equity / warrants | nil | 3,321.88 gross (2,548.30 + 932.48 less 158.90) |
| Net change in cash | (1,735.69) | +1,786.03 |

Ratios (derived): CFO / PAT 0.40 (PY 1.76). CFO / EBITDA 21.4% (EBITDA ex other income 5,758.81; PY 78.0%). FCF (CFO less PPE capex less E&E) = (3,520.26) (PY +2,034.38). Capex / depreciation 3.72x (PY 0.23x). Cash plus FDs 1,131.33 vs 3,981.86 (down 2,850.53).

**CFO quality checks.**
1. **Working-capital cause, bridged.** CF receivable line 4,456.25 vs gross movement 4,297.79: 4,297.79 + sundry assets written off 197.79 − unrealised FX gain 39.34 = 4,456.24 (derived, ties to 0.01). [INFERENCE] the 197.79 "sundry assets written off" were receivable-type balances, which closes B02 P3-5's bridge. Confirming observation: the write-off schedule. Credit-type cost then is 87.18 + 197.79 = 284.97 (1.17% of revenue) vs 144.64 PY, 1.97x.
2. **Tax deferral.** Net current tax liability rose 436.07 and statutory liabilities rose 196.83 (579.69 vs 382.86, Note 30 S p.136). Together 632.90 (derived) of CFO is deferral of payments, 51% of reported CFO. [INFERENCE] adjusted CFO is about 600 (1,233.87 − 632.90 = 600.97); confirming observation: tax payments in H1 FY27 cash flow (Q2 FY27 CF statement).
3. **Customer advances** fell 342.23 to nil (Note 30), a 342.23 CFO drag.
4. **Interest classification:** finance cost 838.31 paid shown in financing, not CFO; CFO is flattered by that choice relative to a lender-style presentation (CFO less interest 395.56, derived).
5. **Margin-money release** 838.75 and cash drawdown of 1,735.69 funded capex alongside debt +1,569.92 (derived).
6. **One-time inflators in PBT:** gain on asset sales 26.52 (PY 206.22), FX gain 39.34, no large one-offs. Other income 358.66 = 8.7% of PBT (PY 23.7%), no flag.

CFO deterioration is clear. FLAG-CASH confirmed.

### 3B Balance sheet (S p.113; C p.166) and ratios
| Ratio | FY26 | FY25 | Anchor |
|---|---|---|---|
| Total assets | 33,146.25 | 27,536.91 (+20.4%) | S p.113 |
| Net PPE | 9,177.91 | 6,250.13 (+46.8%) | |
| E&E | 1,930.58 | 1,430.81 (+34.9%) | |
| Net trade receivables | 11,644.51 | 7,433.89 (+56.6%) | |
| Receivables as % of assets | 35.1% | 27.0% | derived |
| Equity | 20,251.42 | 17,184.00 (+17.9%) | |
| Borrowings | 7,861.34 | 6,291.39 (+24.9%) | |
| D/E (gross) | 0.39 | 0.37 | Note 51 S p.154 |
| Net debt / EBITDA | 1.17x | 0.69x | derived, net of cash and FDs |
| Current ratio | 1.86 | 2.17 | Note 51 |
| Quick ratio | 1.38 | 1.61 | derived |
| Interest coverage (EBIT incl. other income / finance cost) | 5.90x | 3.28x | derived; equals MD&A p.62 |
| ROCE | 22.06% | 11.94% | Note 51; MD&A says 23.00% / 16.00% |
| ROE | 16.46% | 10.01% | Note 51; MD&A 16.21% |
| Goodwill / net worth (C) | 0.06% | 0.07% | derived |

DuPont (derived, S): net margin 12.68% × asset turnover 0.80x (revenue / average assets 30,341.58) × equity multiplier 1.62x (average assets / average equity 18,717.71) ≈ 16.4%, matching printed 16.46%. ROE is driven by margin, not leverage; leverage is flat-to-slightly-up.

Net worth walk: equity +3,067.42 equals total comprehensive income 3,067.42 (S p.114); no equity raise in FY26; warrants 25% already in equity.

Liabilities: current borrowings 6,261.90 (+23.5%), trade payables 2,387.27 (+30.9%), current tax liability 561.35 (4.5x). Cash-based liquidity is thin: 88.81 in hand.

### 3C P&L walk (S p.114)
| Line | FY26 | FY25 | YoY |
|---|---|---|---|
| Revenue | 24,292.95 | 17,919.32 | +35.6% |
| Other income | 358.66 | 467.94 | −23.4% |
| Materials consumed | 3,658.63 | 2,858.48 | +28.0% |
| Stock-in-trade | nil | 4,490.92 | |
| Operating expenses | 10,407.30 | 3,967.08 | +162.3% |
| Employee | 3,570.88 | 2,743.87 | +30.1% |
| Finance cost | 842.34 | 868.73 | −3.0% |
| Depreciation | 1,144.33 | 959.85 | +19.2% |
| Other expenses | 897.33 | 520.57 | +72.4% |
| PBT | 4,130.80 | 1,977.76 | +108.9% |
| PAT | 3,080.05 | 1,482.51 | +107.8% |
| Basic / diluted EPS | 10.33 / 10.09 | 5.27 / 5.26 | gap 2.3% |

**Margin waterfall.** Standalone EBITDA ex other income 5,758.81 = 23.70% (PY 3,338.40 = 18.63%). Consolidated EBITDA 5,832.93 (24.00%, derived) ties to the Chairman's 583 Mn and 23.99% (Chairman p.5; MD&A p.61).

**The headline growth hides a mix change.** C segment note (C p.192): Drilling and Exploration revenue 24,302.17 vs 13,495.58 = **+80.1%** (derived), while "Coal Mining and Trading" went from 4,533.92 (segment result 43.00, 0.95% margin) to nil. Core PBT margin before JV share and group-level items: 17.3% (4,206.55 / 24,302.17) vs 14.5% (1,962.92 / 13,495.58) (derived). The 35% headline understates core growth and overstates the quality of the optics since trading revenue was near-zero margin.

**Cost-side change.** Operating expenses +162.3% on revenue +35.6%, driven by Sub-contract Work and Technical Fees 8,109.98 (+219.4%) (Note 35). That is 33.4% of revenue. Together with hire charges 950.94 (+56.5%) and consultancy 360.99 (+464%), outsourced execution is the swing factor in the margin. Rig fleet: 36 (FY25 AR Board p.30) to 45+ (MD&A p.58); but revenue growth leaned on sub-contractors.

Tax rate 25.4% consistent; no exceptional items; depreciation grew only 19.2% against net PPE +46.8% (additions late in the year, Note 2).

**Phase 3 summary:** Profit is real in the P&L but weak in cash. FY26 CFO is about half of what it looks after adjusting for 632.90 of payment deferral (derived).
**Cross-reference with Phases 1-2:** the unbilled balance (KAM), the write-off (Note 39) and the ECL tail (Note 12) all point to the same receivable story; the SWR loan (Note 15) and the Alara investment (Note 7) are the other uses of cash.
**Phase 3 verdict: 🔴 Red Flag on cash conversion** (earnings quality), 🟡 on balance sheet.
**Kill switch (informational):** Based on phases so far, a human reviewer would have reason to pause sizing, not to stop, because CFO / PAT of 0.40 and FCF of (3,520.26) funded by debt and FD release is the load-bearing cash fact, and the 2,797.43 warrant money arrived after year end.

---

## PHASE 4: RISK FACTORS AND MD&A

### 4A Disclosed risks (MD&A p.63-64, SWOT and Risk Management Framework)
| Risk disclosed | Real or boilerplate | Evidence |
|---|---|---|
| Tender pricing pressure | Real but generic | Mitigation "shifting asset weight toward high-barrier segments", no number |
| Statutory clearances | Real, ties to coal block | No dates or counts |
| Weather and monsoon | Real | JMD p.7 says monsoon continuity improved |
| Environmental / macro-policy | Boilerplate | |
| Localized field obstacles | Boilerplate | |
| Macro-currency exposure | Mismanaged: "handled by framing ... dollar-denominated copper assets in Oman" is not a hedge | FX expenditure 4,732.52 vs earnings 6.19 lakh (Board p.46, Rs 47,32,51,899 vs Rs 6,19,082) |

### 4B MISSING RISKS (absent from the risk section)
| # | Missing risk | Evidence | Likely reason for omission |
|---|---|---|---|
| 1 | Customer concentration, 72.27% in three | Note 46 S p.146; the MD&A lists only tender pricing | Rated "low" in Note 49 as PSUs; management treats PSU as risk-free |
| 2 | Receivable build-up and liquidity | Gross +57.0%, cash 88.81, CFO / PAT 0.40 (Phase 3) | MD&A debtor commentary p.62 calls collections "stable" |
| 3 | SWR going concern and unquantified parent letter | C p.159 | Board's report addresses going concern only at group level (Board p.52) |
| 4 | Promoter-linked capital (ARL share 288.00, Al Hadeetha 39.92, Omani loans 257.86) | Note 7, 48 S | Presented as "strategic investment" (Chairman p.6) |
| 5 | Coal block funding and capex | MD&A p.60 gives revenue 700 to 800 crore and EBITDA 40% to 42% but no capex or funding line; E&E 1,930.58 carries no policy | NOT FOUND IN DOCUMENT: capex, mine plan cost, funding source, EC / forest clearance status |
| 6 | Sub-contractor dependence (33.4% of revenue) | Note 35 S p.137 | Presented as "efficient cost management" (MD&A p.61) |
| 7 | Credit-line stress: MD&A welcomes ECLGS 5 "to extend financial support to the companies like us, in the wake of ongoing conflict in the Middle East" (p.58) | Whether the company applied or drew: NOT FOUND IN DOCUMENT | Rare direct hint of liquidity need, with Oman exposure of 257.86 + 500.97 (C Note 7, p.176) |
| 8 | Middle East geopolitical exposure of the Oman JVs | MD&A p.56 cites the Iran-America conflict as a tailwind only | One-sided framing |
| 9 | Promoter pay and key-person dependence | Both promoters re-appointed with higher pay (Notice p.17-18) | |
| 10 | Tax payment lag | Phase 2G | Not discussed |

### 4C MD&A deep dive and forward guidance vs historical delivery
**Guidance table.** FY25 AR (dated 2025) vs FY26 AR vs delivery.

| Claim | Number | Timeframe | Said in | Delivery / change | Credibility |
|---|---|---|---|---|---|
| Revenue growth | 15% to 20% CAGR | Next 3 years | FY25 AR Chairman p.5-6; Board p.31 | FY26 +34.8% (C 24,302.17 vs 18,029.50) headline; +80.1% on core drilling (C p.192). H1 FY27 standalone +16.3% (11,928.33 vs 10,253.48), Q2 FY27 −7.9% (5,750.03 vs 6,242.18) (Results_Q2FY27, filed 2026-11-06) | Exceeded in FY26; H1 FY27 inside the band |
| EBITDA margin | 20% to 22% | Near to medium term | FY25 AR MD&A p.55 | FY26 23.99%. FY26 AR now says 24% to 25% (MD&A p.64). B00 records Q2 FY27 margin 14.38% against 24.00% FY26 (B00 load_bearing_facts); not recomputed here | FY26 exceeded; next quarter diverges |
| Coal block production start | "operationalisation by FY 28" | FY28 | FY25 AR Chairman p.6 | FY26 AR: "commencement of coal production by start of FY 28-29" (Chairman p.6; MD&A p.60) | Slipped about one year, unacknowledged |
| Coal block steps | PL cum ML applied, awaited | | FY25 Board p.31 | FY26: Note 1 S p.116 still "PL cum ML ... presently underway"; Board p.40 "exploration ... completed", GR "underway". No grant of PL cum ML stated | Milestone not met, sequence changed |
| Coal block economics | Rs 700 to 800 crore revenue over first 3 years; EBITDA 40% to 42% | From start | FY25 AR MD&A p.55; FY26 MD&A p.60 | Unchanged word for word; capex, funding, price per tonne NOT FOUND IN DOCUMENT | Low |
| Oman JV 1 net margin | 5% to 6% | Annual | FY25 AR MD&A p.55; FY26 p.60 | JV revenue not disclosed; JV profit share 146.90 (C p.161), unaudited | Cannot test |
| Order book | 332 crore (FY25) | | FY25 AR | 761 crore, +129% (derived); single order over 300 crore | Delivered |
| Next growth | "around 20% growth" short to medium term | | Chairman p.6 | Core guide 15% to 20% (MD&A p.64); order book / FY26 revenue 3.13x (derived) | Plausible |
| ROCE / ROE | 16% to 23% / 10% to 16% | | Chairman p.6 | Note 51: 11.94% to 22.06% / 10.01% to 16.46% | Basis drift, no bridge |

**Credit-taking and blaming.** All FY26 outperformance is credited to "high capacity utilization", "efficient cost management" and "disciplined expense management" (MD&A p.61-62). No external factor blamed. Sub-contractor use, which explains a large share of the revenue and cost change, is not named. The JMD attributes the order book to execution and trust (p.7).

**Industry claims.** Indian exploration services market INR 15,000 to 18,000 crore at 8% to 10% CAGR (MD&A p.57), sourced to a market-research link (MD&A p.65). Company revenue 243 crore would be about 1.4% to 1.6% of that (derived). Revenue growth 35% against market growth 8% to 10% is share gain or sub-contract pass-through.

**Segments.** Single operating revenue line (Drilling and Exploration); coal "segment" holds only E&E 1,930.58 (C p.192). MD&A "operational capabilities" list nine domains A to I (p.58-59); the Chairman cites "six active domains" and "eight states" (p.5).

**Internal consistency of MD&A.** Four contradictions with the notes: payables (+30.9% vs "reduction"), collections ("stable", turnover 2.55 vs 2.74), capital employed ("without corresponding increase", net PPE +46.8%), and ratio bases (interest cover on standalone; margin on consolidated). Note 51 text and MD&A text disagree on ROCE and margin (P3-3 in B02, verified).

### 4D Tone and credibility (1 to 5)
| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2 | Customer names, SWR letter, round-trip borrower, covenant terms, E&E policy, capex for the coal block all withheld; heavy detail elsewhere (gratuity, ageing) |
| Consistency | 2 | Four commentary contradictions; ROCE 23.00 / 22.06; "exploration completed" vs "PL cum ML underway" |
| Specificity | 3 | Numbers given for margin, growth, coal revenue; missing price, capex, timeline of approvals |
| Accountability | 2 | Slip in coal timeline not acknowledged; stale CRISIL rating in CG report (p.82 shows BBB/Positive, A3+ though the 10 Jul 2026 upgrade to BBB+/Stable and A2 pre-dates the 3 Sep 2026 filing, B00 corpus manifest); "strong parentage" is lifted text, the company has no parent |
| Capital allocation sense | 3 | Rig capex backed by order book and warrants; offset by promoter-linked equity and loans |

**Phase 4 summary:** the MD&A is detailed on opportunity and silent on the four items the notes flag.
**Contradictions vs Phases 1-3:** collections, payables, capital employed, order-book private mix vs PSU credit text.
**Phase 4 verdict: 🔴 Red Flag on credibility** of narrative, 🟢 on historical delivery of revenue and margin guidance (FY26 exceeded).
**Kill switch (informational):** Based on phases so far, a human reviewer would not stop, because FY26 guidance was beaten. The reviewer would treat forward statements as unverified until the PL cum ML grant and the Q2 FY27 call are seen.

---

## PHASE 5: CORPORATE GOVERNANCE AND BOARD

### 5A Board composition (CG p.66-70)
| Director | Category | Since | Board meetings attended (of 7) | Other public cos. / committees | Flag |
|---|---|---|---|---|---|
| Vikas Jain | CMD, promoter | Inception; elder brother of Piyush | 7 | none | Re-appointed from 20 Nov 2026 |
| Piyush Jain | JMD, promoter | 2009 | 7 | none | |
| R P Ritolia | Non-exec, non-independent (professional; 75+ years) | 12 Aug 2024 | **4 (57%)** | 6 boards; Jai Balaji Industries Ltd and GP Eco Solutions India Ltd as ID | Attendance below 75%; CG p.74 sitting-fee table mislabels him "Independent" |
| Meenakshi Anand | ID | 14 Aug 2023 | 7 | none | Second term from 14 Aug 2026 |
| Shivi Sabharwal | ID | 14 Aug 2023 | 7 | none | Second term from 14 Aug 2026 |
| H N S Rajpoot | ID | 30 Jun 2024 | **4 (57%)** | 4 other public cos, 6 committees, 4 as chair; Summit Securities Ltd, FGP Ltd as non-exec | Attendance below 75%; Audit Committee chair |

Board of 6: 3 independent (exactly 50%), 2 executive promoters, 1 non-independent non-executive. No independent director over 10 years. Seats all below 8. Promoter-group cross-board: none found. Shares held: Vikas Jain 1,18,18,922; Piyush Jain 69,19,861; no other director holds shares (CG p.70).

### 5B Committees
| Committee | Members | Meetings | Issue |
|---|---|---|---|
| Audit (CG p.71-72) | Rajpoot (chair), Sabharwal, **Vikas Jain** (CMD) | 4, all attended | An executive promoter sits on the committee that reviews his own company's statements and RPTs |
| NRC (CG p.72-73) | Anand (chair), Sabharwal, **Vikas Jain** | 1 (30 Mar 2026) | SEBI LODR Reg 19(1)(a) requires all NRC members to be non-executive; the AR table shows an executive director as member. The PCS certificate says compliant (CG p.85). Reading is from the printed table; please confirm on the filed composition. One meeting a year for a company that set promoter pay and two ID re-appointments in July 2026 |
| Stakeholders (CG p.74-75) | Sabharwal (chair), V Jain, P Jain | 1 | Fine |
| CSR (CG p.76) | Anand (chair), V Jain, P Jain | 1 | CSR spend 24.26 vs required 27.03 after set-off; compliant |

### 5C Compensation
| KMP | Salary | Commission | Total | Anchor |
|---|---|---|---|---|
| Vikas Jain | 120.00 | 120.25 | 240.25 | CG p.74 (derived total) |
| Piyush Jain | 90.00 | 60.12 | 150.12 | CG p.74 |
| CFO Dinesh Agarwal | 21.53 | | 21.53 | CG p.74 |
| CS Vaishali | 8.57 | | 8.57 | CG p.74 |
| Total | | | 420.47 (table ties to Note 48's 420.49) | |

(All in lakhs; commission FY26 first taken after years of non-payment "due to cash flow constraints", Board p.51.) Promoter pay 390.37 = 9.5% of S PBT (derived). Median employee pay +22%, average +19%, managerial +86% (Board p.51). 803 employees (Board p.51). CEO-to-median multiple: median remuneration NOT FOUND IN DOCUMENT (the ratio row is blank in the .txt).

**Forward step-up.** Re-appointment terms from 20 Nov 2026: CMD Rs 15,00,000 a month plus 0.50% of turnover; JMD Rs 12,00,000 a month plus 0.40% (Notice p.17-18). At FY26 turnover this is 180.00 + 121.46 = 301.46 for the CMD and 144.00 + 97.17 = 241.17 for the JMD, total 542.63 (derived), 13.1% of FY26 S PBT versus 390.37 today. Monthly salary rises 50% and 60%. Q2 FY27 standalone PAT is 277.35 against 760.05 a year earlier (−63.5%) (Results_Q2FY27). Alignment test: the raise is tied to turnover, not profit.

ESOP / dilution: none; promoter warrant conversion added 9.46% to the share count.

### 5D Shareholding (CG p.81)
| Holder | 31 Mar 2026 | Source |
|---|---|---|
| Promoters | 68.65% (2,04,78,783 shares) | CG p.81 |
| Promoters HUF | 0.20% | |
| Public | 25.42% | |
| FPI (two classes) | 0.39% + 0.37% = 0.76% | |
| Others | LLP 0.99%, bodies corporate 2.24%, HUF 1.11%, NRI 0.47%, KMP 0.01%, clearing members 0.12% | |

FY25 AR (Note 18 text near its line 6936): promoter total 68.85% at 31 Mar 2025 (73.61% a year earlier). FY26 year end 68.85% (68.65 + 0.20), so **no promoter selling inside FY26**; the FY25 fall was dilution from the preferential issue. Pledge: **NOT FOUND IN DOCUMENT**; shareholding folder empty (B00). Held by top 133 holders: 85.03% of shares (CG p.80). After year end: 2,821,411 shares allotted on warrant conversion on 10 Jul 2026 to promoter and non-promoter allottees (Board p.41); B00 corpus manifest records promoter open-market disposals (Reg 29(2) letters of 24 Jun, 10 Jul, 12 Aug and 11 Sep 2026). Amounts and prices: NOT FOUND in the AR; B08 settles. **FLAG-PROMOTER-PRELIM** raised on timing (conversion at Rs 132.20 and sales close together), not on a quantified pattern.

### 5E Governance red-flag checklist
| Item | Finding | Anchor |
|---|---|---|
| Whistle-blower | "0 (zero) complaint was received in last quarter" (odd wording); CARO says none in the year | CG p.83; S p.109 |
| SEBI / exchange action | None | CG p.83 |
| RPT committee | RPTs placed before Audit Committee; Board's report says no s.188 transactions and no material RPT | CG p.83; Board p.49. Note 48 shows 1,100.00 loans, 632.01 purchases, 855-scale exposure. Contradiction with "no conflict" language |
| Auditor fee ratio | 20% | Phase 1E |
| CSR | Compliant | Note 47 |
| Section 143 fraud | None | Board p.50 |
| Material subsidiary auditor | All three subsidiaries audited by the same firm per CG p.86 | |
| Secretarial audit | Clean, "all decisions carried unanimously" | Annexure VI p.93 |
| Attendance below 75% | Two directors | CG p.69 |
| Executive director on NRC | Yes per table | CG p.72 |
| Rating text | Stale in CG report | CG p.82 |
| Utilisation of funds | FY25 raise Rs 34,80,77,807 "fully utilized" as per offer document; no line-by-line table | CG p.86 |

**Phase 5 summary:** no regulatory action, no pledge data, no selling inside FY26. Process quality is weak: promoter on Audit and NRC, two directors under 75% attendance, one NRC meeting, step-up in promoter pay, "no conflict" language against material related-party flows.
**Phase 5 verdict: 🟡 Watch** (🔴 on committee design).
**Kill switch (informational):** Based on phases so far, a human reviewer would not stop, because there is no regulatory action or fraud report. The reviewer would want B08's promoter verdict before finalising governance.

---

## PHASE 6: CHAIRMAN'S LETTER AND FRONT MATTER (read last)

### 6A Narrative vs reality
| # | Claim | What the financials show | |
|---|---|---|---|
| 1 | "Operating revenue INR 243 crores ... +35%"; EBITDA 58 crore +74%, 23.99%; PAT 33 crore +101% (Chairman p.5) | C revenue 24,302.17 vs 18,029.50 (+34.8%); EBITDA 5,832.93 (derived, 24.00%); PAT 3,302.70 vs 1,642.58 (+101.1%) | ✅ |
| 2 | "Return on Equity improving from 10% to 16%, ROCE from 16% to 23%" (p.6) | Note 51: ROE 10.01 to 16.46; ROCE 11.94 to 22.06 | ❌ ROCE as stated; ROE ✅ |
| 3 | "Exploration activities at our coal block ... completed ... coal production by start of FY 28-29" (p.5) | FY25 AR said FY28; Note 1 says PL cum ML underway; E&E 1,930.58 unpoliced | ❌ timeline slipped |
| 4 | "All three verticals ... going on well and smoothly" (p.6) | SWR going concern, Samit JV negative net assets, JV earnings unaudited and non-cash | ❌ |
| 5 | JMD: order book "approximately Rs 761 crore"; "more than two-thirds ... private-sector clients ... stronger cash flows, improved working-capital efficiency" (p.7) | Order book ✅ (MD&A p.59). Cash flows and working-capital efficiency: receivables +57%, receivable turnover 2.55 vs 2.74, CFO / PAT 0.40, Note 49 calls the book PSU | ❌ for FY26; open for FY27 |
| 6 | "Largest-ever single order valued at over Rs 300 crores" (p.7) | At least 39.4% of the 761 crore order book (derived) | ✅ but concentration |
| 7 | "Strong Balance Sheet ... conservative 0.39 Debt/Equity" (MD&A p.63) | D/E 0.39 ✅; net-debt gearing 33.23% vs 13.44% a year ago; cash 88.81 | 🟡 half true |
| 8 | "Zero injuries / zero LTI" (p.5, 15) | Not testable from filings | not testable |

### 6B Strategic priorities
Seven priorities (MD&A p.64): capacity and technology, emerging segments, safety, margins "through better execution efficiency", Oman focus, operationalise coal block, shareholder value. Specific enough: coal block (date, revenue, margin) and Oman (contract value USD 125 million, block area 1,448 sq km). Capital allocated: rigs 4,254.36 capex and E&E 499.77 in FY26. Execution evidence: order book growth, accreditation (Board p.40). Missing: capex and funding for the coal block; margin priority runs against 33.4% sub-contract cost share.

### 6C Metrics showcased vs absent
Showcased: revenue, EBITDA margin, PAT, ROE, ROCE, D/E, order book, rig count (45+), projects (165+, 20 ongoing), 3.5 million metres. Absent: operating cash flow, receivable days, customer concentration, utilisation percentage per rig, revenue per rig, sub-contract share, order book split by client and tenor, coal block capex.

### 6D Tone and priority drift vs FY25 (FY25 AR pages 5-6, 30-31, 55)
Constant: 15 to 20% growth, coal revenue 700 to 800 crore at 40 to 42% EBITDA, Oman 5 to 6% net margin. New in FY26: Underground Coal Gasification (JMD p.8), accredited prospecting agency (Ministry of Coal), a 300 crore single order, ECLGS mention. Drifted: coal start FY28 to FY28-29; EBITDA guide 20 to 22% to 24 to 25%; rigs 36 to 45+; manpower 800+ to 1000+ (Snapshot p.12) vs 803 on rolls (Board p.51).

### 6E Quiet Abandonment Check
| # | Opening claim (quote) | Where it should show | Class | Materiality |
|---|---|---|---|---|
| 1 | FY25 Chairman: "operationalisation of coal block by FY 28 will add sizeable value" (FY25 AR p.6); FY26: "commencing the coal production by start of FY 28-29" (Chairman p.6) | Notes: no E&E policy, Note 1 still "PL cum ML underway" | (c) hedged retreat: one-year slip and a changed sequence without naming it | **High**, load-bearing fact 3 |
| 2 | JMD: "stronger cash flows, improved working-capital efficiency" from the private-sector order mix (p.7) | Note 49 credit text still says customers are PSUs and "all debtors are good" (S p.150); Note 51 receivable turnover down | (a) implicit retraction: the notes say the opposite with no acknowledgement | **High**, facts 2 and 4 |
| 3 | FY25 segment "Coal Mining and Trading" revenue 4,533.92 (C p.192) | Chairman and MD&A on revenue growth of 35% | (b) silent drop: trading revenue ended and the growth bridge is not given | Medium: raises true core growth to 80%, lowers optics risk, but the 35% headline is not the right base |
| 4 | Chairman: "All in all, all three verticals ... going on well and smoothly" (p.6) | SWR going concern (C p.159), Samit loss (Note 51 C), JV profit unaudited | (a) implicit retraction | Medium |
| 5 | JMD: Underground Coal Gasification "can emerge as an important new growth vertical" (p.8); MD&A lists UCG as capability I without milestones (p.59) | Chairman's priority list (p.6) and MD&A priorities (p.64) | (b) silent drop in the priorities lists | Low, framework noise |
| 6 | MD&A: "We maintain a low employee attrition rate ... head-count standing at dedicated corporate and field employees" (p.64); the head-count figure is blank | HR section | (b) silent drop of the number | Low |

**Phase 6 summary:** the letters are mostly arithmetically honest on the P&L and silent on cash.
**Phase 6 verdict: 🟡 Watch.**

---

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Verdict | Top reasons |
|---|---|---|
| **GARP** (fullest) | **WATCHLIST** | (1) Growth is real: core drilling revenue +80.1% (C p.192), PAT +101%, order book 761 crore (3.13x FY26 revenue), FY26 guidance beaten. (2) Price of growth: CFO / PAT 0.40, FCF (3,520.26), receivables +57%, 51% of CFO is payment deferral; the growth is bought with working capital and debt. (3) The transition thesis hangs on the coal block (E&E 1,930.58, no policy, start FY28-29, no capex or funding line) and Oman JVs (146.90 unaudited, non-cash), neither evidenced as cash. Reading A: FY26 is a scale step with working capital catching up in H2 FY27. Reading B: sub-contracted, PSU-dependent growth that needs more receivable funding than it earns. The observation that separates them: billed receivables and CFO in the Q2/Q3 FY27 filings and the three customer names. Flag only; sizing belongs in position size. |
| **Turnaround** (fullest) | **FAIL as defined** | (1) Not a distressed turnaround; PBT margin moved 11.0% to 17.0% on a business that was already profitable (derived). (2) The "turnaround" is margin reset to ~24% EBITDA after FY25's 18.6%; the H1/Q2 FY27 results (Q2 PAT −63.5%) say the reset is not yet steady (outside AR; Results_Q2FY27). (3) SWR is a true turnaround case (negative net worth, profitable +76.88) but it is a pass-through of parent markup, not an independent recovery (derived). |
| Value + Quality | FAIL | CFO / PAT 0.40; ROCE 22.06% good; accounting quality 6/10; no dividend |
| Capex-led growth | WATCHLIST | Capex 4,254.36 = 3.7x depreciation; but revenue growth also came from sub-contractors, so the revenue effect of the new rigs is not isolable |
| Cash flow compounder | FAIL | FCF negative, net debt / EBITDA 1.17x from 0.69x |
| Contrarian | WATCHLIST | Q2 FY27 reset in profit may create a gap; AR gives no price anchor |
| Insider confidence | FAIL (preliminary) | Promoters bought via warrants at Rs 132.20 and also sold in the open market Jun to Sep 2026 (B00 manifest); no pledge data |
| Guidance divergence | WATCHLIST | FY26 delivered above guide; coal timeline slipped; Q2 FY27 margin 14.38% vs 24.00% (B00) |

---

## PHASE 8: FINAL VERDICT DASHBOARD

### Snapshot (S unless stated; INR Lakhs)
Revenue 24,292.95 (C 24,302.17); EBITDA ex other income 5,758.81; PAT 3,080.05 (C 3,302.70); equity 20,251.42; borrowings 7,861.34; cash and bank 1,131.33; E&E 1,930.58; order book Rs 761 crore (MD&A p.59). Shares 2,98,30,011 at FY26 end; 3,26,51,422 after 10 Jul 2026 (Board p.44).

### Phase verdicts
| Phase | Verdict |
|---|---|
| 1 Auditor | 🟡 |
| 2 Notes | 🟡 |
| 3 Financials | 🔴 (cash) |
| 4 MD&A / risks | 🔴 (credibility) |
| 5 Governance | 🟡 |
| 6 Front matter | 🟡 |

### Quality score
| Component (25% each) | Score /10 | Basis |
|---|---|---|
| Governance | 5 | Clean regulatory record; weak process (promoter on Audit and NRC, two directors at 57% attendance, one NRC meeting, pay +86% vs staff +19%, "no conflict" language) |
| Accounting quality | 6 | Reconciles to B02: ties arithmetically, E&E and ECL gaps, write-off nature withheld |
| Balance sheet | 6 | D/E 0.39, current 1.86, coverage 5.90x, CRISIL upgrade; offset by cash 88.81, receivables 35% of assets, short debt 6,261.90 |
| Earnings quality | 5 | CFO / PAT 0.40, FCF negative, 51% of CFO is deferral; PAT is real and core margin up |
| **Overall** | **5.5 / 10** | |

### Top 3 strengths
1. Core drilling revenue +80.1% and EBITDA margin 23.99% against FY25 guidance of 20% to 22% (C p.192; MD&A p.61).
2. Order book 761 crore, up 129% from 332 crore, with a 300 crore single order (MD&A p.59; FY25 AR p.31).
3. Parent opinion unmodified, no covenant breach or default, no promoter selling inside FY26 (S p.108; CG p.81).

### Top 3 red flags
1. Cash conversion: CFO 1,233.87 vs PAT 3,080.05, FCF (3,520.26), 632.90 of CFO is deferred payments (derived).
2. Concentration 72.27% in three undisclosed customers, with a PSU-based "low risk" credit note while the order book is claimed two-thirds private (Note 46, 49; JMD p.7).
3. SWR and promoter-linked capital: going concern paragraph with unquantified support letter, 1,100.00 round-trip loan, coal block E&E 1,930.58 with no policy and a slipped timeline.

### Key monitorables for next quarter
| Metric | Threshold | Where | Why |
|---|---|---|---|
| Billed receivables / gross receivables, CFO | Billed under 9,218.67 and H1 CFO / PAT above 0.7 | Q2 and Q3 FY27 results, CF statement | Decides reading A vs B |
| Names and shares of the top three customers | Disclosed; no single above 30% | Q2 FY27 call (11 Nov 2026); investor deck | Fact 2 |
| PL cum ML grant and GR submission date | Grant on record; GR filed | Exchange filings, Jharkhand authority | Fact 3, FY28-29 start |
| Coal block capex and funding | A figure | Q2 FY27 call; next AR | NOT FOUND today |
| SWR support letter amount and term | A figure; no top-up beyond 410.34 | Note on related-party loans, next filing | Hidden obligation |
| EBITDA margin | At or above 20% | Quarterly results | Q2 FY27 reported 14.38% vs 24.00% (B00) |
| Promoter holding and pledge | No further net disposals; pledge nil | SHP, Reg 29 filings | FLAG-PROMOTER-PRELIM |
| NRC / Audit committee composition | No executive member | Reg 27 corporate governance filing | Process quality |
| Tax paid vs current tax | Cash tax within 20% of charge | H1 FY27 CF | 436.07 gap |

### One-line verdict
Growth is real and beat guidance, but cash does not follow profit and the coal block and SWR hold the disclosures a buyer most needs; best fit is GARP on a WATCHLIST basis, sized for a concentration and receivable reading that FY27 filings will settle.

---

```yaml
stage: B03-ardeep
company: "SOUTHWEST"
run_date: "2026-11-09"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "shareholding/ is empty: no source is automated yet. Push the latest quarterly shareholding pattern by hand; it closes the FII+DII UA qualifier and the promoter pledge trend."
  - "screener export sheets came out EMPTY (formulas with no cached values), so no CSV was written for them: screener, ASIANENE, DEEPINDS, JINDRILL Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization. Open Financials.xlsx once in Excel or LibreOffice, save it, then run --push-again."
  - "no results PDFs yet (screener has none): add later on github or locally + --push-again"
  - "no rating PDF yet: add later the same way"
  - "HIGH (freshness): inputs/concalls/ has no Q2 FY27 transcript. The call is scheduled for 11 Nov 2026 at 16:00 IST, after this run."
  - "shareholding/ is empty: COLLECTOR gap, not evidence. FII+DII UA qualifier and pledge trend stay open."
  - "Screener export: Data_Sheet is populated for main and peers; Profit & Loss, Quarters, Balance Sheet and Cash Flow CSVs are ABSENT. Stages use Data_Sheet and filings."
  - "results/ and rating/ were cured by /step1: three BSE results filings and the CRISIL rationale of 10 Jul 2026 (text capture; no PDF)."
  - "Q3 FY26 concall transcript (Feb 2026) is not in the corpus."
  - "annual-report/ holds FY26 and FY25; FY26 governs; FY25 is prior-year comparison only. FY24 and earlier ARs not held."
  - "announcements/ cover Nov 2025 to Nov 2026; pre-Nov 2025 filings are not held."
  - "inputs/announcements/20261107-eaf4e423-6c28-4f7f-b374-694a12c96ee9.txt: newspaper-advert pages garbled; not material."
  - "inputs/announcements/20260929-ae2f036b-6e7c-4543-a22d-9a2188e91ab7.txt: AGM voting results; 15 of 32 pages carry text."
  - "research/ is empty: no broker notes supplied."
  - "EMPTY-FOLDER CONFIRMATION suppressed by /step1 AUTONOMY CONTRACT. Standing default taken: proceed with the gaps."
  - "Stage 3 text extraction gaps: standalone Note 41 (contingent liabilities) body and Note 46 segment table are missing from the .txt; consolidated Notes 42 and 47 used instead; verifier to open the PDF. Median remuneration ratio row in Board's report p.51 is blank in the .txt."
flags:
  - {type: FLAG-CASH, reason: "CFO 1,233.87 vs PAT 3,080.05 (0.40; PY 1.76); FCF (3,520.26); net current tax liability +436.07 and statutory liabilities +196.83 defer 632.90 (51% of CFO); customer advances 342.23 to nil; cash 88.81 vs 1,824.50 (INR Lakhs; CF S p.115, BS S p.113, Note 30 S p.136)"}
  - {type: FLAG-PROMOTER-PRELIM, reason: "Promoter holding flat 68.85% through FY26 (CG p.81; FY25 AR Note 18) so no in-year selling; but 28,21,411 warrant shares allotted 10 Jul 2026 (Board p.41) and promoter open-market disposals Jun-Sep 2026 per B00 manifest announcements; pledge NOT FOUND IN DOCUMENT; full verdict from B08"}
  - {type: FLAG-GOING-CONCERN-SUBSIDIARY, reason: "SWR net worth (264.94), auditor material uncertainty rests on unquantified parent letter (C p.159); parent loan 410.34 interest-free (CARO iii S p.107)"}
  - {type: FLAG-CONCENTRATION, reason: "Three customers 72.27% of revenue (PY 48.00%), names withheld, credit note rates risk low as PSU while JMD claims two-thirds private order book (Note 46 S p.146; Note 49 S p.150; JMD p.7)"}
  - {type: FLAG-GUIDANCE-SLIP, reason: "Coal block production start moved FY28 (FY25 AR p.6) to FY28-29 (FY26 Chairman p.6, MD&A p.60); PL cum ML still underway (Note 1 S p.116); no capex or funding stated"}
  - {type: FLAG-GOVERNANCE-PROCESS, reason: "Executive CMD sits on Audit and NRC (CG p.71-72); two directors at 4 of 7 board meetings (CG p.69); one NRC meeting; promoter pay +86% vs staff +19% (Board p.51)"}
  - {type: FLAG-RPT-OPACITY, reason: "1,100.00 (PY 950.00) loan to unnamed KMP-influenced enterprise repaid within year, interest 15.62; Board's report says no s.188 contracts (Note 48 S p.148; Board p.49)"}
  - {type: FLAG-DISCLOSURE-CONFLICT, reason: "MD&A and Note 51 contradict figures; MD&A ratios mix standalone and consolidated bases (MD&A p.62; Note 51 S p.154)"}
phase_verdicts: {p1: "YELLOW: parent unmodified, SWR going concern paragraph, JV profit 146.90 unaudited, no KAM on E&E or ECL", p2: "YELLOW: 12 of 15 B02 findings verified, notes foot, E&E and ECL policy gaps, accounting 6/10", p3: "RED on cash conversion: CFO/PAT 0.40, FCF (3,520.26), 632.90 of CFO is deferral; balance sheet YELLOW", p4: "RED on narrative credibility, GREEN on FY26 revenue and margin delivery; four commentary contradictions", p5: "YELLOW: no regulatory action, no FY26 promoter selling, exec director on Audit and NRC, 57% attendance for two directors", p6: "YELLOW: P&L claims true, cash and coal timeline claims not", p7_best_fit: "GARP on WATCHLIST"}
overall_quality: 5.5
quality_components: {governance: 5, accounting: 6, balance_sheet: 6, earnings: 5}
kill_switch_notes:
  - "P1: human would not stop; going concern doubt is confined to SWR (exposure 452.72, 2.2% of S equity)"
  - "P2: human would not stop; wants borrower of the 1,100.00 loan and SWR letter before sizing"
  - "P3: human would pause sizing; CFO/PAT 0.40, FCF (3,520.26) funded by debt and FD release"
  - "P4: human would not stop; treat forward statements as unverified until PL cum ML grant and Q2 FY27 call"
  - "P5: human would not stop; wants B08 promoter verdict"
triple_pass_verification:
  verified: 12
  discrepancies:
    - {finding_rank: 9, triple_pass_value: "margin-money cover of guarantees 61.2%", ar_value: "61.8% ((1,042.52+348.05)/2,250.07, derived); FDs also back fund-based lines", note_ref: "Note 14 S p.131; Note 9 S p.130; Note 42 C p.185"}
    - {finding_rank: 10, triple_pass_value: "related-party financial exposure 855.35", ar_value: "visible components 288.00+39.92+257.86+111.66+0.08 = 697.52; 855.35 not reproducible", note_ref: "Note 7 S p.129; Note 8 S p.130; Note 48 S p.148"}
    - {finding_rank: 11, triple_pass_value: "depreciation rose 150.50", ar_value: "total depreciation +184.48 (1,144.33 vs 959.85); PPE depreciation +187.32", note_ref: "Note 38 S p.138"}
missing_risks:
  - {risk: "Customer concentration 72.27% in three customers", evidence: "Note 46 S p.146; MD&A risk list p.63 omits it"}
  - {risk: "Receivable build-up and liquidity", evidence: "Note 12 S p.131; CF S p.115; MD&A p.62 calls collections stable"}
  - {risk: "SWR going concern and unquantified parent support letter", evidence: "C p.159"}
  - {risk: "Promoter-linked capital: ARL shares 288.00, Al Hadeetha 39.92, Omani loans 257.86", evidence: "Note 7 S p.129; Note 48 S p.147-148"}
  - {risk: "Coal block capex, funding and clearances not stated; E&E 1,930.58 without policy", evidence: "MD&A p.60; Note 5 S p.129"}
  - {risk: "Sub-contractor dependence 8,109.98 = 33.4% of revenue", evidence: "Note 35 S p.137"}
  - {risk: "Credit-line stress: MD&A welcomes ECLGS 5 'for companies like us' amid Middle East conflict; use unknown", evidence: "MD&A p.58"}
  - {risk: "Middle East exposure of Oman JVs framed as tailwind only", evidence: "MD&A p.56; Note 7 C p.176"}
  - {risk: "Promoter pay step-up and key-person dependence", evidence: "Notice p.17-18; Board p.51"}
  - {risk: "Tax payment lag: current tax liability +436.07, interest on taxes 16.87 (PY 8.27)", evidence: "BS S p.113; Note 39 S p.138"}
guidance_table:
  - {claim: "Revenue growth 15-20% CAGR next 3 years", number: "15-20%", timeframe: "FY25-FY28", credibility: "FY26 +34.8% headline, +80.1% core (C p.192); H1 FY27 standalone +16.3%, Q2 FY27 -7.9% (Results_Q2FY27); delivered, medium-high"}
  - {claim: "EBITDA margin 20-22%, later 24-25% core", number: "20-22% then 24-25%", timeframe: "near to medium term", credibility: "FY26 23.99% beat 20-22%; Q2 FY27 14.38% per B00; medium"}
  - {claim: "Coal block production start", number: "FY28 then FY28-29", timeframe: "slipped about one year", credibility: "low; PL cum ML still underway (Note 1 S p.116)"}
  - {claim: "Coal block revenue Rs 700-800 crore in first three years at 40-42% EBITDA", number: "700-800 crore; 40-42%", timeframe: "from production start", credibility: "low; unchanged text, no capex, funding or price"}
  - {claim: "Oman JV1 net margin 5-6%", number: "5-6%", timeframe: "annual", credibility: "cannot test; JV profit 146.90 unaudited (C p.161)"}
  - {claim: "Order book", number: "332 crore to 761 crore", timeframe: "FY25 to FY26", credibility: "delivered; includes single order over 300 crore"}
  - {claim: "ROCE 16% to 23%, ROE 10% to 16% (Chairman)", number: "ROCE 22.06 vs 23.00 stated", timeframe: "FY26", credibility: "basis drift between Chairman, MD&A and Note 51"}
monitorables:
  - {metric: "Billed receivables and H1 FY27 CFO/PAT", threshold: "billed under 9,218.67; CFO/PAT above 0.7", where: "Q2/Q3 FY27 results and CF statement", why: "separates growth-with-working-capital from cash-generative growth"}
  - {metric: "Top three customer names and shares", threshold: "disclosed; none above 30%", where: "Q2 FY27 call 11 Nov 2026; investor deck", why: "load-bearing fact 2"}
  - {metric: "PL cum ML grant and GR submission", threshold: "grant on record; GR filed", where: "exchange filings", why: "FY28-29 production start"}
  - {metric: "Coal block capex and funding plan", threshold: "a stated figure", where: "call; next AR", why: "NOT FOUND today"}
  - {metric: "SWR support letter amount and loan 410.34", threshold: "quantified; no top-up", where: "related-party note next filing", why: "hidden obligation"}
  - {metric: "EBITDA margin", threshold: "20% or above", where: "quarterly results", why: "Q2 FY27 14.38% vs 24.00%"}
  - {metric: "Promoter holding and pledge", threshold: "no further net disposals; pledge nil", where: "SHP and Reg 29 filings", why: "FLAG-PROMOTER-PRELIM"}
  - {metric: "Executive director on Audit/NRC", threshold: "none", where: "Reg 27 governance filing", why: "process quality"}
  - {metric: "Cash tax paid vs charge", threshold: "within 20%", where: "H1 FY27 CF", why: "436.07 gap"}
ar_new_downstream_entities: []     # Top-3 customer names NOT FOUND IN DOCUMENT. Every named client, JV partner and RPT counterparty in the FY26 AR (CMPDI, Hindustan Copper, Oil India, CGWB, RIL, Vedanta, Hindalco, Hindustan Zinc, Samit Spectrum, Chandra Prabhu International, Thakurji Towers, Ravmo Imports, Alara Resources Ltd) also appears in the FY25 AR.
strengths_top3:
  - "Core drilling revenue +80.1% and EBITDA margin 23.99% beat FY25 guidance of 20-22% (C p.192; MD&A p.61)"
  - "Order book 761 crore, +129% from 332 crore, including a single order over 300 crore (MD&A p.59; FY25 AR p.31)"
  - "Parent opinion unmodified, no default, no promoter selling inside FY26 (S p.108; CG p.81)"
red_flags_top3:
  - "Cash conversion: CFO 1,233.87 vs PAT 3,080.05, FCF (3,520.26), 632.90 of CFO is deferred payments (derived)"
  - "72.27% revenue from three undisclosed customers with a PSU low-risk credit note against a claimed two-thirds private order book"
  - "SWR going concern with unquantified support letter, 1,100.00 round-trip loan, coal block E&E 1,930.58 with no policy and slipped timeline"
best_fit_strategy: "GARP (WATCHLIST)"
one_line_verdict: "Growth is real and beat guidance, but cash does not follow profit and the coal block and SWR hold the disclosures a buyer most needs; GARP on a watchlist basis, sized for a concentration and receivable reading FY27 filings will settle."
analyst_note: "New versus B02: (1) consolidated CARO clause xxi lists SWOFS and SWGS with clause xvii adverse remarks (C p.162); (2) intercompany elimination 975.92 equals the RPT columns 282.92+632.01+60.99, so SWR books about 99% of revenue from the parent and the 66.53 net cost elimination is a 10.5% markup [INFERENCE]; (3) CF receivable line ties to the balance sheet only if the 197.79 write-off and 39.34 FX gain are included (4,297.79+197.79-39.34=4,456.24), so write-off is receivable-type [INFERENCE]; (4) CFO is flattered by 632.90 of tax and statutory deferral; (5) core drilling revenue grew 80.1% since 4,533.92 of low-margin trading ended; (6) MD&A interest cover is on standalone numbers; (7) CMD sits on NRC, Reg 19 reading to confirm. Three B02 numbers did not reproduce (ranks 9, 10, 11). Q2 FY27 data used only as backward check of AR claims."
```
