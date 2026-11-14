# STAGE 3: ANNUAL REPORT DEEP DIVE (BACKWARD READ): Creative Newtech Ltd (CNL), run 2026-11-11

Source: runs/cnl-2026-11-11/inputs/annual-report/CNL_AR_FY2025-26.txt. "AR p.N" is the `[page N]` marker of that text (each marker is one PDF sheet, two printed pages). SA = standalone, CON = consolidated. Unit: Rs. in Lakhs on the face of both statements (SA p.73, CON p.97); Rs. Cr only where the AR itself prints Cr (founders' message, MD&A, rating table). "Derived" = my arithmetic on disclosed numbers. Memory (companies/CNL.md, step1-business-brief.md) was weighed, never used as a source. Rating key: 🟢 Clean | 🟡 Watch | 🔴 Red Flag. Kill switches are informational only.

Reading order followed: back pages first (consolidated auditor's report and annexures, consolidated notes and statements, standalone notes and statements, standalone auditor's report and CARO), then governance, MD&A, Directors' Report, Notice, and the founders' message last.

Input gaps carried (B00): shareholding pattern absent; only the FY2025-26 AR held (no FY24 balance sheet, no prior-year AR, so no 3-year trend and no tone-drift test); screener formula sheets blank; peer CSVs absent.

---------------------------------------------------------------------
## LOAD-BEARING FACT CHECK (memory against the AR)

| # | Memory claim | What the AR shows | Verdict |
|---|---|---|---|
| 1 | HK subsidiaries drive consolidated profit at the same tax as standalone | CON PBT after associate 8,176.20 less SA PBT 4,581.66 = 3,594.54 from the subsidiaries (exact bridge); CON tax 1,146.91 = SA tax 1,146.91; SCL PBT = PAT 3,742.90 with "Provision for taxation Nil"; CPDL (31.04); SCL 77.50% held; NCI share of profit 842.15 = 22.5% x 3,742.90 (AOC-1 p.63; CON P&L p.97; CON Note 30 p.108). CON Note 30 prices the effect: "differences in Tax Rates of subsidiaries operating in other jurisdictions 904.84", which equals 25.17% x 3,594.97, i.e. a nil HK tax rate. The annual FY26 pattern matches the Q2 FY27 pattern in memory | CONFIRMED |
| 1b | Related-party flows with the HK entities | SCL purchases 15,539.15 (FY25 10,008.93), SCL sales 2,208.54 (20.64), CPDL purchases 574.91 (2,150.01), closing SCL balance (3,093.04) payable vs 274.99 receivable (SA Note 36 p.88-89). FY27 SCL approval sought up to Rs 750 Cr (AR p.25, p.30) against an FY26 limit of 25,000 lakh (AR p.43) and FY26 actual volume 17,747.69 lakh | CONFIRMED, larger than memory implied |
| 2 | FY26 CFO -Rs 271.9 Cr, debtor days 76 | CON CFO (27,188.34) lakh, i.e. Rs 271.88 Cr (CON CF p.98); CON closing-basis receivable days 76.3 vs 48.7 (derived from CON p.97). The H1 FY27 turn is outside the AR | CONFIRMED for FY26; H1 FY27 NOT FOUND IN DOCUMENT |
| 3 | Brand gross margin 40-42%, brand 19% of revenue | Reported brand segment result 12,629.19 on revenue 38,085.50 = 33.16% CON (34.57% FY25); SA 10.56%; segment results reconcile to gross profit (21,357.91 = 269,977.25 - (255,227.91 - 6,608.57), derived). Brand share FY26 14.11% (FY25 15.25%) (CON Note 37 p.111-112). 19% is a Q2 FY27 figure, not in the AR | NOT SUPPORTED by AR; 40-42% unreconciled |
| 4 | BSNL BharatNet order Rs 3,194.83 Cr | No hit for BSNL, BharatNet, Odisha, Zicom, consortium, order book or backlog anywhere in the AR text (search repeated this stage). Only Infinova (Directors' Report s.35, AR p.41). The Directors' Report dated 04-Aug-2026 says no material change or commitment other than Infinova and the ESOP. The funding frame that IS in the AR: CRISIL BBB+/Stable and A2, "Rs. 209 crore bank facilities, enhanced from Rs. 144 crore", 04-Dec-2025 (AR p.58), against CON borrowings of Rs 324.26 Cr (AR p.46) | NOT IN AR; funding headroom question is real |

---------------------------------------------------------------------
# PHASE 1: AUDITOR'S REPORT AND CARO

### 1A Core opinion
| Item | Standalone | Consolidated |
|---|---|---|
| Auditor | Gupta Raj & Co., FRN 001687N, partner CA Nikul Jalan, M.No. 112353 (AR p.66-72) | Same firm and partner (AR p.91-94) |
| Opinion | Unmodified: "give a true and fair view in conformity with the accounting principles generally accepted in India" (AR p.66) | Unmodified: "our unmodified opinion" (AR p.91) |
| Date / UDIN | 14-May-2026, 26112353CYGDEF4629 (AR p.69) | 14-May-2026, 26112353YJJILQ4700 (AR p.94) |
| Going concern language | Standard management-responsibility paragraph only (AR p.67-68). CARO clause xix: "nothing has come to our attention ... that the Company is not capable of meeting its liabilities ... within a period of one year" (AR p.71). No material-uncertainty paragraph | Standard paragraph only (AR p.93). None of concern |
| IFC opinion | Adequate and operating effectively (Annexure 2, AR p.72) | Adequate and operating effectively (Annexure B, AR p.96) |

### 1B Key Audit Matters (the same three in both reports; AR p.66-67 SA, p.91-92 CON)
| # | Subject | Why key (auditor) | How addressed | Risk | My cross-check |
|---|---|---|---|---|---|
| 1 | Revenue recognition | Control transfer timing; "rebates and discounts (variable consideration)" judgment | Policy review, controls testing on rebates/discounts, invoice sampling, "confirmations from customers" | 🟡 | Revenue discount line is only 14.81 (FY25 129.50) (SA Note 23.3 p.84) while Sales Promotion 1,098.35 (564.08) and Commission 1,110.71 (344.90) are expensed (SA Note 29 p.84-85). Consideration payable to customers could be sitting in cost. The policy still uses pre-Ind AS 115 "risks and rewards" wording (SA Note 2(l) p.77) |
| 2 | Inventory (NRV provisioning) | "rapid technological changes, short product life cycles" | Count reports by an "independent person", ageing review, test counts | 🟡 | No NRV write-down amount disclosed anywhere (NOT FOUND IN DOCUMENT). CARO ii(b) lists stock-statement gaps up to 749.22 (see 1D) |
| 3 | Contingent liabilities (tax, litigation) | Judgement on probable/possible/remote | Experts, in-house counsel discussions | 🟡 | 600.01 and rising, 85.8% GST, none provided (SA Note 35 p.87-88) |

Omissions worth stating: no KAM on trade receivable recoverability although receivables rose 164.2% (SA) and are 63.9% of SA total assets (55,138.03 / 86,311.16, derived); no KAM on the HK subsidiaries that supply 51.1% of CON PAT; no KAM on borrowings or liquidity. A 🟡 for audit-scope depth.

### 1C Emphasis of Matter and Other Matters
| Item | Detail | Risk |
|---|---|---|
| EoM | None (both reports) | 🟢 |
| Other Matters (CON, AR p.93) | Associate Creative eCommerce Ventures (share of loss 5.40) audited by Gupta Raj. CPDL (assets 1,314.66; revenue 1,681.77; PAT (31.04)) and SCL (assets 13,713.55; revenue 29,773.64; PAT 3,742.90) "not audited by us"; opinion "based solely on the report of such auditors"; the not-modified sentence adds "the financial statements certified by the Management". The HK auditor's name and report are NOT FOUND IN DOCUMENT | 🟡 |

### 1D CARO 2020 (standalone Annexure 1, AR p.69-71)
| Clause | Finding | Amount / anchor | Risk |
|---|---|---|---|
| i | PPE records, title deeds in company name; no revaluation | clean (AR p.69) | 🟢 |
| ii(a) | Inventory verified by management at year end; "no material discrepancies" | (AR p.69) | 🟢 |
| ii(b) | Working-capital limits above Rs 5 crore; quarterly returns agree "except for below month": June 2025 8,705.74 vs 8,539.92 (diff 165.82); Sep 2025 9,282.04 vs 8,721.34 (560.70); Dec 2025 10,347.78 vs 9,598.56 (749.22); Mar 2026 13,188.06 vs 12,680.17 (507.89). Reason given: "Stock in Transit which is not considered in Stock statement" | Differences are 1.9%, 6.0%, 7.2%, 3.9% of book stock (derived). Reporting stock to banks below book is the conservative direction, but four of four quarters mismatch and no receivables-statement test is reported | 🟡 |
| iii | No loans, investments, guarantees or security granted; sub-clauses "not applicable" | (AR p.69-70). Consistent with Note 36: no advances given in FY26 (FY25: CeV 70.94 given) | 🟢 |
| iv-vi | s.185/186 not applicable, no deposits, no cost records | clean | 🟢 |
| vii | Undisputed dues regularly deposited, none >6 months. Disputed dues: income tax AY2008-09 5.26+10.30+3.45+3.96, AY2018-19 6.34, AY2020-21 38.91; GST DGGI 191.44, Hyderabad 7.79, West Bengal 42.59+16.81, Maharashtra 202.61, New Delhi 25.46+28.08; VAT/CST 12.48 (FY2014-15); Customs 4.53 | Total 600.01 = Note 35 total (derived sum). GST 514.78 (85.8%). The forum is not stated in the CARO table (NOT FOUND IN DOCUMENT); Note 35 names the forum for DGGI (Punjab and Haryana High Court) and the old customs matter (CESTAT). The DGGI line has no period in CARO | 🟡 |
| viii | No unrecorded income surrendered | (AR p.70) | 🟢 |
| ix | No default to any lender; term loans applied for purpose; short-term funds not used for long-term purposes; no pledged-subsidiary-share borrowing | (AR p.70) | 🟢 |
| x | No IPO/preferential allotment | (AR p.71) | 🟢 |
| xi | No fraud noticed or reported; no ADT-4; "no whistle blower complaints has been received" | (AR p.71) | 🟢 |
| xii-xvi | Not Nidhi; RPT compliant with s.177/188 per auditor; internal audit commensurate; no non-cash director deals; no CIC | (AR p.71) | 🟢 |
| xvii | "has not incurred cash losses" in FY26 or FY25 | (AR p.71). The clause tests P&L cash losses, not operating cash flow, which is (25,738.12) | 🟢 for the clause, 🔴 for CFO (Phase 3) |
| xviii | No auditor resignation | (AR p.71) | 🟢 |
| xix | No material uncertainty on meeting liabilities within one year | (AR p.71). Sits beside 32,424.87 of on-demand borrowings and a 1.45 current ratio | 🟡 |
| xx | CSR fully spent; no unspent amount | 62.00 spent vs 61.69 required (SA Note 40 p.90) | 🟢 |

CON report: CARO 3(xxi) Annexure A says there are no qualifications in CARO reports of "subsidiary companies (incorporated in India)" (AR p.95). The Group has no Indian subsidiary (two HK subsidiaries, one Indian associate; Annexure 1 list, AR p.95). Annexure B (AR p.96) says IFC reliance applies to "one (1) wholly owned subsidiary, which is incorporated in India". No such subsidiary exists. This is template language that does not match the group structure; the practical effect is that no IFC or CARO assurance reaches the HK entities that earn 51.1% of PAT.

### 1E Auditor continuity and fees
| Item | Detail |
|---|---|
| Firm / tenure | Gupta Raj & Co. approved at the 20th AGM (30-Sep-2024) for five years to the 25th AGM in 2029 (Directors' Report s.14, AR p.38-39). Prior auditor and the reason for change: NOT FOUND IN DOCUMENT. FY26 is at most the second year of tenure |
| Audit fee | Audit 9.00 + certification 1.00 + reimbursements 0.15 = 10.15 (FY25 10.05) (SA Note 29A p.85; governance report p.59) |
| Non-audit ratio | (1.00 + 0.15) / 9.00 = 12.8% (derived). Non-audit does not exceed audit |
| Fee adequacy | Audit fee unchanged at 9.00 while revenue rose 55.2%; 10.15 is 0.004% of CON revenue (derived). Low for a Rs 2,700 Cr group with HK subsidiaries not audited by this firm; a 🟡 observation, not proof of weak audit |
| Rotation | Not due (term to 2029); mandatory rotation year NOT FOUND IN DOCUMENT |

### 1F Standalone vs consolidated differences
| Item | Detail |
|---|---|
| Extra qualifications | None |
| Other auditors | HK subsidiaries (names NOT FOUND); relied on "solely" (AR p.93) |
| Structure errors | Indian-subsidiary template language (see 1D) |
| Perimeter | CON profit 7,029.29 vs SA 3,434.75 (2.05x) with identical tax; CON KAMs are word-for-word the SA KAMs, so the HK consolidation risk never reached KAM status |

### Phase 1 summary
| Test | Result |
|---|---|
| Opinion | Unmodified both |
| KAMs | 3, all 🟡; receivables, HK perimeter and borrowings are not KAMs |
| CARO adverse remarks | None; ii(b) stock-statement exceptions in 4 of 4 quarters |
| Auditor | Low fee, HK components not audited by group auditor, template errors in group report |

**Phase 1 verdict: 🟡 Watch.**
Kill switch (informational): Based on phases so far, a human reviewer would not have reason to stop on the audit report alone, because the opinion is unmodified, there is no CARO adverse remark and no fraud report; the reasons to keep reading are the reliance on unnamed HK auditors for 51.1% of PAT and the template errors in the consolidated annexures.

---------------------------------------------------------------------
# PHASE 2: NOTES TO FINANCIAL STATEMENTS (verify, extend, summarize)

### Triple-pass Top 15 verification
All 15 re-computed from the statements and notes. Result: 15 verified, 0 value discrepancies, with the refinements shown.

| Rank | B02 finding | AR check (Rs. Lakhs) | Mark |
|---|---|---|---|
| 1 | Receivables +164.2% SA / +137.7% CON vs revenue +55.2% / +51.7%; days 78.7 vs 46.3 / 76.3 vs 48.7; build 34,266.83 vs outflow (25,738.12) | 55,138.03 / 20,871.20 = 2.642; 56,511.02 / 23,776.98 = 2.377; 255,600.47 / 164,682.47 = 1.552; 270,461.72 / 178,275.38 = 1.517; days recomputed 78.7, 46.3, 76.3, 48.7; CF lines (SA p.74, CON p.98) | ✓ verified |
| 2 | Short-term borrowings +366.3% to 32,424.87; ND/E 1.01 from 0.10; CON 0.837 from 0.232 | 32,424.87 / 6,953.06 = 4.663; Note 33 SA (p.86) 1.01 vs 0.10; CON 32,426.09 / 38,729.29 = 0.837 vs 7,180.46 / 30,925.56 = 0.232. "On demand": only the cash credit is stated payable on demand (SA Note 17 c, p.83); the CON caption is "Loans repayable on demand" (CON Note 17 p.106); Note 32 shows 100% in 1-12 months | ✓ verified (nuance: buyers-credit and NBFC tenors NOT FOUND) |
| 3 | HK 3,594.54 = 51.1% of CON PAT, nil tax, CON tax = SA tax | 8,176.20 - 4,581.66 = 3,594.54; / 7,029.29 = 51.14%; tax 1,146.91 both; Note 30 rate effect 904.84 (CON p.108) | ✓ verified (refinement: the nil rate is priced in Note 30, but no reason, no DTL, no remittance path) |
| 4 | Subsidiary CFO (1,450.22); FX line 702.68 vs HK opening cash 1,011.37; HK cash 59.99 | (27,188.34) - (25,738.12) = (1,450.22); 4,387.66 - 3,376.29 = 1,011.37; 535.96 - 475.97 = 59.99; CON CF shows "Exchange difference on translation 702.68" below the net change (CON p.98) | ✓ verified |
| 5 | HK not audited by group auditor | AR p.93 | ✓ verified |
| 6 | SCL purchases 15,539.15 (+55.3%), sales 2,208.54, swing 3,368.03 (13.1% of SA CFO), FY27 Rs 750 Cr, Click Retail 4,773.50 vs sales 2,677.91, RPT balances do not tie to Note 8 | 15,539.15 / 10,008.93 = 1.552; 274.99 + 3,093.04 = 3,368.03; / 25,738.12 = 13.09%; positive non-subsidiary balances 6,460.70 (plus CPDL 911.52) vs Note 8 related-party receivables 3,244.81 | ✓ verified |
| 7 | Segment result = gross profit; brand 33.16% CON, 10.56% SA; share 14.11% from 15.25% | 12,629.19 / 38,085.50; 2,453.37 / 23,224.22; 9,356.16 / 27,067.93 = 34.57%; 38,085.50 / 269,977.25 | ✓ verified |
| 8 | Allowance 76.77 on 55,214.80 (0.14%), >6m 1,955.62 (3.54%) vs 517.46 (2.48%), disputed cover 32.4% | 54,978.14 + 236.66 = 55,214.80; 1,258.05 + 431.67 + 29.45 + 149.37 + 87.08 = 1,955.62; 76.77 / 236.66 = 32.4% | ✓ verified |
| 9 | ROCE 22.01% excludes borrowings (10.62% on equity+debt vs 13.01%); 19.33% mixes NCI | 6,624.58 / 62,374.54 = 10.62%; 4,394.70 / 33,781.84 = 13.01%; 7,029.29 / 36,362.89 = 19.33% | ✓ verified |
| 10 | Contingent 600.01 (+84.0%), 85.8% GST; 694.72 asset; DGGI conflicting dates | FY25 sum 326.00; 514.78 / 600.01; Note 12 (p.82); Note 35 iv says order "1st February, 2024" and writ "against the order dated 09.01.2024" | ✓ verified |
| 11 | Discount 14.81 (-88.6%); commission+promotion 2,209.06 (+143%) | 14.81 / 129.50; (1,098.35 + 1,110.71) / (564.08 + 344.90) = 2.43 | ✓ verified |
| 12 | 3,735.40 royalty + service-charge + reimbursement, payees unnamed | 595.73 + 602.65 + 2,537.02 (CON Note 29 p.108); no commitments listed in CON Note 34 | ✓ verified |
| 13 | Share premium +750.78; NCI 298.85 below 22.5% of SCL equity; FCTR 861.98 outside OCI | 13,166.19 - 12,415.41; 22.5% x (1.22 + 11,844.33) = 2,665.25 vs 2,366.40; CON P&L OCI (12.46) only | ✓ verified |
| 14 | Promoter-family pay 236.74; guarantees; mortgaged related-party premises; 12% loan | Ketan 114.07 + Purvi 81.68 + Nidhi 40.99 = 236.74 (Note 36 + Directors' Report p.37-38); Notes 15, 17 | ✓ verified |
| 15 | Notes silent on Infinova, ESOP, FX; 4,493.48 label | Note 44(k) "no significant subsequent events" vs Directors' Report s.35; Note 37 | ✓ verified. New derivation: 45,583.75 + 75.47 + 4,493.48 + 1.21 + 53.98 = 50,207.89 = the FX outgo 50,207.90 in the Directors' Report (AR p.40), so the 4,493.48 "Bank Buyers Credit Expenses" is a settlement of buyers credit, not an expense (finance cost is 2,042.92) |

Accounting quality score reconciliation: B02 scored 5/10. I agree on 5/10 (numbers tie, clean statutory dockets, thin disclosure where exposure is largest). My Phase 2 verdict (🟡) is consistent with it; downside on provisioning (4/10), upside on capitalisation (7/10), as B02 had it.

### 2A Accounting policy aggressiveness
| Policy | Disclosure | Assessment |
|---|---|---|
| Revenue | Point in time, "risks and rewards", "No element of financing is deemed present as the Sales ... are made largely with same credit terms" (SA Note 2(l) p.77). Credit terms themselves never stated | 🟡 With domestic receivable days about 112 (see 2D) a financing element is worth testing |
| Depreciation | WDV; buildings 60 yrs, computers 3 yrs, office equipment 5 yrs (SA Note 2(d) p.76) | 🟢 Schedule II-based |
| Intangibles | Software 3 yrs, customised software 10 yrs; 214.64 CWIP moved to software (SA Notes 3-4 p.80); amortisation 34.03 | 🟡 The 10-year life is a management choice on a 237.44 addition |
| Capitalisation | No borrowing-cost or R&D capitalisation seen | 🟢 |
| Inventory | Lower of cost and NRV, FIFO; no write-down disclosed (SA Note 2(g) p.76; Note 7 p.81) | 🟡 |
| ECL | Policy: "always recognises lifetime expected credit losses" (Note 2(o) p.78); Note 32: "estimate of incurred losses" (p.85); allowance 76.77; no matrix | 🔴 mismatch between policy and practice |
| Leases | All premises treated as short-term, cancellable on 1-3 months notice; rent 327.09 expensed (SA Note 2(q) p.78-79, Note 41 p.90); no Ind AS 116 rate | 🟡 Keeps lease liabilities out of debt metrics for 31 branches and 18 warehouses (AR p.10) |
| Policy changes | None quantified; "regrouped / restated" is generic (Note 45) | 🟢/🟡 |
| Segment | Policy says "geographic segment" (SA Note 2(s) p.79) while segments are Brand and Market Entry (Note 39) | 🟡 internal inconsistency |

### 2B Related-party map (SA Note 36 p.88-89; AOC-2 p.42-43)
| Item | Value | % |
|---|---|---|
| Purchases from related parties (SCL 15,539.15 + CPDL 574.91 + others 1,056.95) | 17,171.01 | 6.90% of SA purchases (248,723.17) |
| Sales to related parties (SCL 2,208.54 + others 5,862.81) | 8,071.35 | 3.16% of SA revenue (255,600.47) |
| Related-party receivables per Note 8 | 3,244.81 | 5.88% of gross receivables |
| Positive RPT balances per Note 36, non-subsidiary | 6,460.70 | does not tie to 3,244.81 (balances may include advances; split NOT FOUND) |
| Promoter-family pay (Ketan, Purvi, Nidhi) | 236.74 | 6.9% of SA PAT (3,434.75) |
| All six KMP/director lines (Directors' Report p.37) | 360.85 | 10.5% of SA PAT |

Value-extraction and governance signals:
- Click Retail Pvt Ltd: sales 770.07 to 2,677.91 (3.5x), receivable balance 222.83 to 4,773.50 (21x), larger than one year's sales to it. Annexure I to the Notice (AR p.35-36) lists Mr. Vijay Advani's other directorships as Click Retail Private Limited and Rinavaa Technologies. A whole-time director of CNL sits on the board of the entity that owes CNL 4,773.50 (8.7% of SA receivables, derived).
- SCL purchases are described as at "arm's length ... pricing basis with reference to prevailing market rates", with no valuation report ("Not Applicable") (Notice p.30). Brand margin earned in India is 10.56% SA vs 33.16% CON: about 22.6 percentage points of the group brand margin is earned outside India at nil tax.
- World EMS: sales 4,991.45 to 2,669.81; balance 733.13. Owner relationship NOT FOUND.
- Collateral: Shilpa Global's Gala No. 1 mortgaged to SBI (SA Note 15 c, p.83); personal guarantees of Ketan and Purvi Patel on term loans and of "Director and Whole-time director" on cash credit and buyers credit (Note 17 d).
- FY27: the Rs 750 Cr SCL approval = 75,000 lakh, 4.2x FY26 actual (17,747.69) and 3.0x the FY26 limit (25,000) (derived).
- Dhvani Ketan Patel is listed as "Relative of Director" (Note 36 p.88; "Business Integration Manager", AR p.4) with no transaction line: compensation NOT FOUND IN DOCUMENT.

### 2C Contingent liabilities (SA Note 35 p.87-88)
| Measure | Value |
|---|---|
| Total ex-guarantees | 600.01 (FY25 326.00, +84.0%) |
| % of SA net worth (29,949.67) | 2.00% |
| % of SA PAT (3,434.75) | 17.5% |
| Bank guarantees | 1,058.13 (FY25 793.01) = 3.5% of net worth |
| >25% / >100% flags | Not triggered |
| Composition | GST 514.78 (85.8%; +112.8% from 241.92), income tax 68.22, VAT/CST 12.48, customs 4.53 |
| Provision | none; customs 694.72 paid under protest is carried in Duties and Taxes Receivable (Note 12 p.82) although CESTAT ruled for the company on 11-Apr-2023 (Note 35 ix) |

### 2D Receivables (SA Note 8 p.81; CON Note 8 p.104)
| Item | FY26 | FY25 |
|---|---|---|
| SA gross | 55,214.80 | 20,893.93 |
| Allowance | 76.77 (0.14%) | 22.73 (0.11%) |
| <6 months | 53,259.18 | 20,376.47 |
| 6-12 months | 1,258.05 | 109.64 |
| 1-2 years | 431.67 + 149.37 disputed | 222.19 |
| >2 years | 29.45 + 87.08 disputed | 8.46 + 90.09 + 76.13 disputed + 10.95 |
| >6 months share | 3.54% | 2.48% |
| Related parties | 3,244.81 (5.88%) | 1,946.25 |
| Concentration / top customers | NOT FOUND IN DOCUMENT (no major-customer disclosure under Ind AS 108) | |
| Unbilled | NOT FOUND IN DOCUMENT | |
| Closing-basis days | SA 78.7 / CON 76.3 | 46.3 / 48.7 |

New derivation (mechanism of the build): SA India sales rose to 179,713.32 from 67,840.68 (+164.9%) while exports fell to 75,402.68 from 96,014.12 (-21.5%) (SA Note 23.2 p.84). India share of SA product sales 70.4% vs 41.4%. Receivables grew +164.2%, in lockstep with India sales. If export receivables are negligible (not disclosed), receivable days on India sales are 112.0 (FY26) vs 112.3 (FY25) (derived). Read: the build is a mix shift toward credit-heavy domestic sales at unchanged credit terms, not slower collection from the same customers. The cost is that growth now consumes cash at about 112 days of domestic sales. This refines, not contradicts, B02's "deteriorating" label.

### 2E Inventory
| Item | SA FY26 | FY25 |
|---|---|---|
| Inventory | 13,188.06 | 8,398.80 (+57.0% vs revenue +55.2%) |
| Days on cost of goods (243,933.91 / 157,238.52, derived) | 19.7 | 19.5 |
| Write-downs / NRV provision | NOT FOUND IN DOCUMENT | |
| Advances to suppliers (Note 12) | 8,595.74 (+51.0%) | 5,692.30 |
| CON advances to suppliers | 13,463.70 | 9,179.91 |
Inventory is not the stress point. Advances to suppliers equal 9.96% of SA total assets (derived).

### 2F Borrowings
| Item | Detail |
|---|---|
| Quantum | SA 32,424.87 (secured banks and NBFC 32,417.28; directors 7.59 at 12%); CON 32,426.09 (SA Note 17 p.83; CON Note 17 p.106) |
| Maturity wall | 100% within 12 months (SA Note 32 p.86). Cash plus margin money 2,158.12 = 6.7% of debt; receivables 55,138.03 = 1.7x debt |
| Rating headroom | CRISIL BBB+/Stable, A2, Rs 209 crore facilities (AR p.58). CON borrowings Rs 324.26 Cr (AR p.46). Sanctioned fund-based limits NOT FOUND IN DOCUMENT; the secretarial audit lists two charge-modification filings with errors, one executed 05-Dec-2025 (AR p.49). AGM 2025 passed "Increase in Overall Borrowing Limits" and "enhancement of borrowing and asset charge limits" (AR p.59); amounts NOT FOUND |
| Covenants | Note 33 refers to "financial covenants" (AR p.86); none disclosed; compliance NOT FOUND |
| Security | Stocks, book debts, movable assets; four flats/offices (Note 15 a) whose ownership is not stated and which do not appear as separate PPE lines (inference: possibly promoter-owned collateral; unverified); FDs 0.83 Cr and 0.42 Cr |
| Pledge of shares | Promoter share pledge NOT FOUND IN DOCUMENT (shareholding pattern absent); CARO ix(f) covers subsidiary shares only |
| ICDs given | None (CARO iii; Note 44(e)) |

### 2G Deferred tax
SA DTA 56.26 (gratuity 53.06, OCI 6.25, PPE (3.05)); expense (6.20) (SA Notes 6, 30). The tax reconciliation is a single line at 25.17% on PBT (SA Note 30 p.85), i.e. SA effective rate 25.03% (derived). CON effective rate 14.03% (1,146.91 / 8,176.20) vs 13.70% FY25 (derived). No deferred tax liability on undistributed HK profits; HK reserves 11,844.33 (AOC-1 p.63). The reason for nil HK tax, and whether it is permanent, are NOT FOUND IN DOCUMENT.

### 2H Other items
| Item | Detail |
|---|---|
| Exceptional items | None FY26 or FY25 (P&L p.73, p.97); FY24 NOT FOUND |
| Goodwill | None |
| ESOP | None in operation in FY26; Creative ESOP Scheme 2026 of 2,00,000 options (about 1.33% of capital), fresh allotment, promoters excluded; the resolution says it "will follow a cash mechanism" while stating fresh allotment (AR p.26, p.31-32): internally unclear |
| Leases | Short-term only (above) |
| Post-balance sheet | Notes say none (Note 44(k) p.91). The Directors' Report adds: Infinova India acquisition pending, "no binding definitive agreement"; CFO change (Kanvinde ceased 14-Apr-2026; Thakur CFO 14-May-2026, the date the accounts were approved); ESOP 2026 on 04-Aug-2026 (AR p.41). Consideration and funding NOT FOUND |
| Dividend | Re 0.50 x 1,50,16,675 = 75.08, 2.2% of SA PAT and 1.2% of CON owners' PAT (derived) |
| FX | Earnings 75,402.68; imports 45,583.75; hedging NOT FOUND IN DOCUMENT; exchange gain 652.71 (SA Note 24 p.84) |
| Restatement | Generic only (Note 45); mislabelled comparatives per B02 P3-3, accepted |

### Phase 2 summary and cross-reference with Phase 1
| Phase 1 KAM | Phase 2 evidence | Consistent? |
|---|---|---|
| Revenue / rebates | Discount line 14.81; promotion + commission 2,209.06 | The KAM tested rebates against approved schemes, not the classification between revenue and cost |
| Inventory | No NRV note; stock-statement gaps | Open |
| Contingent liabilities | 600.01, GST rising; asset 694.72 | Open on the customs asset |
| (no KAM) Receivables | The largest movement on the balance sheet, allowance 0.14% | Gap in KAM selection |

**Phase 2 verdict: 🟡 Watch (bordering 🔴 on receivables provisioning and undisclosed covenants).** Reconciles with B02's 5/10.
Kill switch (informational): Based on phases so far, a human reviewer would not have reason to stop on the notes alone, because numbers tie and no restatement exists, but would require answers on receivables composition, covenants and HK tax before relying on the cash story.

---------------------------------------------------------------------
# PHASE 3: FINANCIAL STATEMENTS

### 3A Cash flow (read first)
| Metric (Rs. Lakhs) | SA FY26 | SA FY25 | CON FY26 | CON FY25 |
|---|---|---|---|---|
| PAT | 3,434.75 | 2,556.44 | 7,029.29 | 5,311.10 |
| EBITDA incl. other income (PBT + finance cost + depreciation, derived) | 6,767.15 | 4,510.77 | 10,400.13 | 7,337.86 |
| CFO | (25,738.12) | 1,399.61 | (27,188.34) | 2,185.92 |
| CFO / PAT | (7.49)x | 0.55x | (3.87)x | 0.41x |
| CFO / EBITDA | (3.80)x | 0.31x | (2.61)x | 0.30x |
| Capex (purchase of PPE/intangibles/CWIP) | 126.07 | 281.66 | 330.04 | 281.66 |
| FCF (CFO - capex) | (25,864.19) | 1,117.95 | (27,518.38) | 1,904.26 |
| Capex / depreciation | 0.88x | 2.43x | 2.17x | 2.43x |
| M&A / investments | nil | 404.15 | nil | 375.61 |
| Financing inflow | 23,423.51 | 2,039.05 | 23,423.64 | 2,008.17 |
| Cash and equivalents, year end (prior year) | 475.97 (3,376.29) | | 535.96 (4,387.66) | |

CFO/PAT was below 0.7 in both years held (0.55 / 0.41 in FY25), then negative: a consistent flag, though FY24 is NOT FOUND.

CFO quality checks:
| Check | Finding |
|---|---|
| One-time inflators | Customer advances rose to 1,772.56 from 238.21 (SA Note 20 p.83), adding 1,534.35 to CFO (6.0% of the deficit, derived). The SCL payable swing of 3,368.03 (13.1%) flatters SA CFO |
| Interest classification | Interest of 1,746.91 (banks 1,494.29 + others 252.62) sits in financing; 296.01 of other finance charges stays in CFO. Moving interest into CFO makes SA CFO (27,485.03) and CON (28,935.25) (derived) |
| Payables stretch | Not the driver: payable days 29.3 vs 27.1 on purchases (derived); payables and other liabilities contributed a 10,719.15 inflow because purchases grew |
| Inventory rundown | None; build of 4,789.26 |
| CON FX line | 702.68 added below the net change in cash is a reconciling figure; the FCTR credit of 861.98 never passed through reported OCI |
Verdict: the growth is financed by banks (+25,471.81 net short-term borrowing), not by operations. The 702.68 FX line against HK opening cash of 1,011.37 means offshore cash is thin (59.99 at year end).

### 3B Balance sheet (CON, Rs. Lakhs; p.97)
| Line | FY26 | FY25 | Change |
|---|---|---|---|
| Total assets | 93,723.64 | 53,174.50 | +76.3% |
| Receivables | 56,511.02 (60.3% of assets) | 23,776.98 | +137.7% |
| Inventory | 17,344.58 | 10,571.32 | +64.1% |
| Other current assets (advances to suppliers 13,463.70) | 16,077.17 | 11,398.35 | +41.0% |
| Cash / margin money | 535.96 / 1,682.15 | 4,387.66 / 1,135.61 | cash -87.8% |
| Non-current assets | 1,557.54 (1.7%) | 1,374.60 | |
| Equity (owners / NCI) | 36,362.89 / 2,366.40 | 29,401.31 / 1,524.25 | |
| Borrowings | 32,426.09 | 7,180.46 | +351.6% |
| Trade payables | 18,511.43 | 13,534.81 | +36.8% |
| Other current liabilities and provisions | 3,901.75 | 1,419.22 | |
Asset-light: PPE 819.52 and intangibles 406.57 together are 1.3% of assets; goodwill nil.

Key ratios (derived unless marked "AR"):
| Ratio | CON FY26 | CON FY25 | SA FY26 | SA FY25 |
|---|---|---|---|---|
| D/E on total equity | 0.837 | 0.232 | 1.08 (AR Note 43) | 0.27 (AR) |
| Net debt/EBITDA (incl. other income) | 2.90x | 0.23x | 4.47x | 0.59x |
| Net debt/EBITDA (ex other income) | 3.32x | 0.30x | 5.53x | 1.01x |
| Current ratio | 1.68 | 2.36 | 1.45 | 2.12 |
| Quick ratio | 1.36 | 1.88 | 1.22 | 1.70 |
| Interest coverage (EBIT incl. OI / finance cost) | 4.96x | 7.11x | 3.24x | 4.42x |
| AR p.46 published interest coverage | 6.09 | 9.96 | | not reproducible from disclosed items |
| ROCE (EBIT / closing equity + debt) | 14.4% | 18.9% | 10.62% | 13.01% |
| ROE (owners' PAT / closing owners' equity) | 17.0% | 15.7% | 11.47% | 9.61% |
| Goodwill % net worth | 0 | 0 | 0 | 0 |

DuPont (CON, total equity, closing balances; derived):
| Component | FY26 | FY25 |
|---|---|---|
| Net margin (PAT / revenue) | 2.60% | 2.98% |
| Asset turnover (revenue / total assets) | 2.89x | 3.35x |
| Equity multiplier (assets / equity) | 2.42x | 1.72x |
| ROE | 18.15% | 17.17% |
Margin and turnover both fell; the ROE increase comes from the equity multiplier, which rose 41%. ROE is leverage-driven, not operational.

### 3C P&L (CON, Rs. Lakhs; p.97)
| Line | FY26 | FY25 | YoY |
|---|---|---|---|
| Revenue from operations | 270,461.72 | 178,275.38 | +51.7% |
| Purchases | 255,227.91 | 165,256.38 | +54.4% |
| Change in inventories | (6,608.57) | (2,670.89) | |
| Employee benefits | 2,129.98 | 1,824.24 | +16.8% |
| Finance costs | 2,066.43 | 1,015.59 | +103.5% |
| Depreciation | 152.10 | 116.07 | +31.0% |
| Other expenses | 10,601.59 | 8,399.19 | +26.2% |
| Other income | 1,289.32 | 1,871.40 | -31.1% |
| PBT before associate | 8,181.60 | 6,206.20 | +31.8% |
| Tax | 1,146.91 | 843.40 | +36.0% |
| PAT | 7,029.29 | 5,311.10 | +32.4% |
| Owners / NCI | 6,187.14 / 842.15 | 4,620.77 / 690.33 | +33.9% / +22.0% |

Margin waterfall (% of CON revenue 270,461.72, derived): gross profit including export entitlements 8.08% (segment-based 7.91% excluding them; FY25 8.38%) less employee 0.79% and other expenses 3.92% = EBITDA excluding other income 3.37% (FY25 3.07%); other income +0.48%; depreciation 0.06%; finance 0.76%; PBT 3.02%; tax 0.42%; PAT 2.60% (FY25 2.98%). Management's EBITDA of Rs 103.95 Cr includes other income.

| Test | Result |
|---|---|
| Other income % of PBT | CON 15.8%; SA 28.1% (1,289.32 / 4,581.66), above the 20% flag on the standalone view. Other income 549.71 has no breakdown; exchange gain 652.71 = 14.2% of SA PBT |
| Exceptional 3-year pattern | nil in both years held; FY24 NOT FOUND |
| Tax rate | SA 25.03% stable; CON 14.03% held down by the HK mix |
| EPS | Basic = diluted 41.04 (FY25 32.18, +27.5%); weighted shares 1,50,16,675 vs 1,43,45,793 (CON Note 31 p.108). No gap because no dilutive instruments; ESOP 2026 would add up to 1.33% |
| Finance cost | Interest on banks 1,494.29 vs 635.21 (+135%); finance cost 0.76% of revenue vs 0.57% |

### Cross-reference with Phases 1-2
- Contradiction: CARO xvii and xix (no cash loss, no uncertainty) sit beside CFO (25,738.12) and 32,424.87 of on-demand debt. Not a false statement (the clauses test narrower things), but the auditor's report does not draw the reader's attention to the CFO.
- Consistent with Phase 2: provisioning looks light while the book more than doubles.

**Phase 3 verdict: 🔴 Red Flag (cash conversion and leverage); the earnings themselves tie.**
Kill switch (informational): Based on phases so far, a human reviewer would have reason to stop and obtain post-balance-sheet cash evidence before proceeding, because CFO is negative Rs 271.88 Cr, bank debt rose 366% to fund receivables, and the ROE improvement is leverage-driven; the pipeline continues regardless.

---------------------------------------------------------------------
# PHASE 4: RISK FACTORS AND MD&A

### 4A Disclosed risks (MD&A, AR p.47)
| Risk | Real or boilerplate | Assessment |
|---|---|---|
| Rapid obsolescence of technology | Real, generic text | Relevant to a distributor with 17,344.58 of inventory; no quantification |
| Credit risk | Boilerplate and contradicted | Claims a "focused and aggressive receivables management system" while turnover fell 27.08% (AR p.46) |
| Interest rate risk | Boilerplate and contradicted | "The Company has judiciously managed the debt-equity ratio ... well managed the working capital to reduce the overall interest cost" while D/E rose 265.13% and finance cost 103.5% |
| Competition | Boilerplate | "we expect to be significantly insulated from this risk" |
| Threats (tariffs, FX, supply chain, project execution) | Partly real | Execution risk for government projects is new; FX not quantified |
| Board opinion | "no risks which may threaten the existence of the Company" (AR p.38) | Unsupported by any stress disclosure |

### 4B Missing risks
| Missing risk | Evidence | Likely reason for omission |
|---|---|---|
| Receivable/working-capital funding | CFO (27,188.34); receivables +137.7%; 32,424.88 on-demand debt (CON p.97-98, Note 17) | The metric that shows the risk flatters least |
| Offshore profit concentration, nil tax, other auditors | 51.1% of PAT; AOC-1 tax "Nil"; AR p.93 | Disclosure would invite tax and transfer-pricing questions |
| Transfer pricing and SCL dependence | Purchases 15,539.15; FY27 limit Rs 750 Cr; brand margin 10.56% SA vs 33.16% CON | Related-party sensitivity |
| Licence dependence | Honeywell: royalty 595.73; term and renewal NOT FOUND; "exclusive" territories stated at AR p.16 | Commercial confidentiality |
| Customer concentration | No major-customer disclosure; Click Retail 4,773.50 (memory suggests a high top-customer share, unverified) | Ind AS 108 omission |
| Rated-limit headroom | Rs 209 Cr rated facilities vs Rs 324.26 Cr borrowings | Rating and sanction detail withheld |
| Promoter-family dependence | Pay 236.74; guarantees; Shilpa Global collateral; Advani director of Click Retail | Governance self-reporting |
| Recurrent indirect-tax disputes | GST 514.78, +112.8% | Presented as "unjustified" |
| Acquisition funding (Infinova) | Directors' Report s.35 only | Not yet binding |
| CFO turnover | Kanvinde out 14-Apr-2026; Thakur CFO 14-May-2026, in the firm since 04-Dec-2025 (AR p.38) | Treated as routine |

### 4C MD&A deep dive
| Claim | Evidence in AR | Judgement |
|---|---|---|
| Growth credited to "Honeywell, Samsung, Cooler Master, ViewSonic" (AR p.45) | Three of four are Market Entry brands; Brand segment +40.7% vs Market Entry +54.2% | Credit-taking on external partners; brand mix fell |
| Industry: global IT market USD 10.04 trillion in 2026, CCTV market USD 14.25 billion by 2031 (AR p.43-44) | Third-party sources | Context, not performance |
| Current ratio fall called "satisfactory short-term liquidity" | 1.68 vs 2.36, all debt on demand | Spin |
| "Net debt to equity ... 0.84" (AR p.46) | 324.26 / 387.29 = 0.84 is gross debt; net of Rs 22.18 Cr cash it is 0.78 (derived) | Mislabel |
| Receivable turnover fall blamed on "proportionately higher rise in the trade receivables" | Tautological | No reason given, no external blame |
| Segment | Two reported segments (Note 37) though MD&A describes three verticals including Solutions (AR p.46) | Solutions revenue not separately reported |

Forward guidance table:
| Claim | Number | Timeframe | Credibility |
|---|---|---|---|
| Honeywell sales "expected to cross 3 million units" (AR p.9) | 3 million units | 2026 | 2/5: no base-year units (8 million cumulative over 9 years averages 0.89 million), no revenue link |
| "Promising likelihood" of securing additional brand rights with "substantial increase in profitability" (AR p.36) | none | FY27 | 2/5: FY26 added ten-plus partners yet net margin fell to 2.60% |
| SCL RPT up to Rs 750 Cr (AR p.30) | 75,000 lakh | FY27 | 2/5: FY26 limit 25,000 lakh, usage 71% |
| Vision 2030: "first Indian consumer technology brand with a meaningful global presence" (AR p.25) | none | 2030 | 1/5: not measurable |
| Infinova acquisition (AR p.41) | none; no definitive agreement | pending | 2/5 |
| ESOP 2,00,000 options | 1.33% of capital | from AGM 30-Sep-2026 | n/a |
| Revenue or margin guidance | NOT FOUND IN DOCUMENT (memory's FY27/FY29 guidance is not in the AR) | | |
Delivery history: the founders' message says the earlier year was spent "strengthening margins" (AR p.6); actual FY26 net margin fell from 2.98% to 2.60% and segment gross margin from 8.38% to 7.91%.

### 4D Tone and credibility (1-5)
| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2 | The ratio table includes the unflattering receivable and leverage moves, but no CFO, no covenants, no customer concentration, no HK tax reason |
| Consistency | 2 | Opening claims of higher-margin mix vs falling brand share; template errors in the auditor annexures |
| Specificity | 3 | Numerous partnership names and some numbers; no guidance numbers |
| Accountability | 2 | No acknowledgement of the cash outflow; explains nothing |
| Capital-allocation sense | 2 | Cash goes to customers (receivables +137.7%) and suppliers (advances +46.7%); dividend payout about 1.2%; offshore cash not repatriated; pay raises of 24-41% |

### Contradictions with Phases 1-3
- MD&A "well managed the working capital" vs Phase 3 CFO (27,188.34).
- Directors' Report "no risks which may threaten the existence" vs Phase 2F 100% on-demand maturity and a Rs 209 Cr rating base.
- MD&A "no long-term borrowings" vs CON term loan 1.21 (immaterial).

**Phase 4 verdict: 🟡 Watch.**
Kill switch (informational): Based on phases so far, a human reviewer would not have reason to stop on the narrative alone, because it is bland rather than false, but the missing-risk list (cash, offshore profit, rated limits) is the substance of the thesis risk.

---------------------------------------------------------------------
# PHASE 5: CORPORATE GOVERNANCE AND BOARD

### 5A Board (AR p.51-52, p.37-38; certificate AR p.62)
| Director | Role | On board since | Years at run date | Other directorships | Attendance |
|---|---|---|---|---|---|
| Ketan C. Patel | CMD, promoter | 22-Sep-2004 | 22.1 | 17 per Notice Annexure I, incl. SCL, CPDL, Secure Connection Pvt Ltd, Shilpa Global, Rinavaa and 11 "PG" entities | 5 of 5 (AR p.35) |
| Vijay Advani | WTD | 30-Jan-2006 | 20.8 | Click Retail Pvt Ltd, Rinavaa (AR p.35-36) | 5 of 5 |
| Mihir Shah | ID | 23-Nov-2017 | 8.97 | Nil | attendance symbols not in text layer |
| Suresh Bhagavatula | ID | 10-Oct-2019 | 7.1 | Nil | NOT FOUND |
| Kurian Chandy | ID | 01-Feb-2020 | 6.8 | Mount Everest Breweries, Kataline, Paramount Speciality Forgings (listed) | NOT FOUND |
| Prachi Jain | ID, woman | 29-Jul-2022 | 4.3 | Nil | NOT FOUND |
Flags: no independent over 10 years (Mihir Shah reaches 10 in Nov 2027); attendance below 75% cannot be tested because the attendance symbols are not in the text layer; no director holds more than 8 listed seats; promoter-group cross-board memberships are extensive (Ketan: SCL, CPDL, Secure Connection Pvt Ltd, Shilpa Global, Rinavaa; Advani: Click Retail, Rinavaa); the Chairman is the executive promoter MD, with 4 of 6 directors independent (67%).
Board changes: Purvi Patel resigned as WTD 11-Aug-2025, became Chief Strategy Officer 26-Aug-2025; the governance report states "none of the Directors ... are related to each other" as on 31-Mar-2026 (true only after her resignation) (AR p.51).

### 5B Committees
| Committee | Composition | Meetings FY26 | Note |
|---|---|---|---|
| Audit | 4 IDs; Kurian Chandy chair | 4 (15-May, 06-Aug, 11-Nov-2025, 05-Feb-2026) | CFO and auditor as invitees; RPT approvals all dated 15-May-2025 (AOC-2) |
| NRC | 4 IDs | 1 (15-May-2025) | No NRC meeting dated after Purvi Patel's CSO appointment on 26-Aug-2025 or Thakur's hiring on 04-Dec-2025; process evidence for those decisions NOT FOUND |
| Stakeholders | 4 IDs | 1 | zero complaints |
| Risk | 3 executive + Kurian Chandy | 4 | the risk committee is promoter-run |
| CSR | Ketan, Advani, Mihir Shah | 1 | spend 62.00 vs 61.69 required |
| Share allotment | Ketan, Advani, Thakur, Doshi | 0 | |

### 5C Compensation
| Person | FY26 (Rs. Lakhs) | FY27 proposed | Change |
|---|---|---|---|
| Ketan Patel | 114.07 | 158.23 | +38.7% |
| Purvi Patel | 81.68 | 115.10 | +40.9% |
| Vijay Advani | 65.92 | 81.48 | +23.6% |
| Executive total | 261.67 | 354.81 | +35.6% |
| All six KMP | 360.85 | 455.75 | +26.3% |
Ratios: Ketan 22.04x median, Purvi 15.78x, Advani 12.74x (AR p.66); implied median about 5.18 lakh (derived); permanent employees 202. Median increase 9.24%, non-managerial 8.85%, managerial 12.96% (AR p.66) against proposed 24-41% for the three executive directors. Promoter-family payroll including Nidhi Patel 40.99: 236.74 (6.9% of SA PAT). ESOP: the new scheme excludes promoters; no dilution yet; 1.33% maximum.

### 5D Shareholding (AR p.82 Note 13; p.57-58)
| Item | Value |
|---|---|
| Promoter and group | 85,02,220 shares, 56.62% (FY25 56.60%): Ketan 56.20%, Purvi 0.39%, Nidhi 0.02% |
| Change | +3,500 shares (Nidhi Patel) |
| Pledge / encumbrance | NOT FOUND IN DOCUMENT (shareholding pattern absent) |
| FII / DII trend | NOT FOUND IN DOCUMENT |
| Holder count | 8,987 holders; 78 holders of 1,00,001+ shares hold 87.26% of capital by value |
| Insider confidence evidence | Ketan converted 5,00,000 warrants on 03-Jan-2025 (Note 13e); total warrant issue 9,03,000 at Rs 450 per share (derived: (3,973.20 + 90.30) / 9.03 lakh); market cap at 31-Mar-2026 of 793.11 Cr implies about Rs 528 per share (derived from AR p.6) |
No promoter selling against a growth narrative. Promoter dividend received 42.20.

### 5E Governance red-flag checklist
| Item | Finding |
|---|---|
| Whistleblower complaints | None (AR p.58) |
| SEBI actions | None; secretarial audit exceptions: CHG-1 date and attachment errors, IEPF-2 and MGT-14 filed with additional fees, results advertisements delayed 7h30m and 2d9h, earnings-call intimation delayed one working day, Reg 74(5) certificate not found on exchange portals (AR p.49) |
| RPT committee | Audit committee approves; independents only vote |
| Auditor fee ratio | 12.8% non-audit; fees very low |
| CSR | Compliant |
| s.143(12) fraud | None |
| Material subsidiary auditor | SCL (HK) is the material subsidiary (AR p.59); auditor not named and not the statutory auditor |
| CFO change | Out on 14-Apr-2026, new CFO on 14-May-2026, who is also the signatory of the 04-Aug-2026 MD/CFO certificate |
| Disclosure of group structure | "Joint venture with CyberPowerPC USA" (AR p.6) while AOC-1 says "no Joint Venture" (AR p.64) |

**Phase 5 verdict: 🟡 Watch.** Promoter-controlled with dense related-party flows, an executive director on a counterparty board, and large proposed pay increases; offset by independent-majority committees, no pledge data to condemn, no whistleblower or fraud items.
Kill switch (informational): Based on phases so far, a human reviewer would not have reason to stop on governance alone, because there is no fraud, qualification or promoter exit, but would need the shareholding pattern (pledge) before any promoter conclusion.

---------------------------------------------------------------------
# PHASE 6: FOUNDERS' MESSAGE AND FRONT MATTER (read last)

### 6A Narrative vs reality
| # | Claim | Reality | Mark |
|---|---|---|---|
| 1 | Total income Rs 2,717.51 Cr (+50.85%), EBITDA +42.66% to Rs 103.95 Cr, PAT +32.35% to Rs 70.29 Cr (AR p.7) | Ties to CON statements (271,751.04; 10,400.13 incl. other income; 7,029.29) | ✅ |
| 2 | FY25 focused on "higher-margin businesses"; "strengthening margins" (AR p.6-7) | Brand share 14.11% vs 15.25%; CON segment margin 7.91% vs 8.38%; net margin 2.60% vs 2.98% | ❌ |
| 3 | "operational discipline" (AR p.7) | CFO (27,188.34); receivable days 76.3 vs 48.7; finance cost +103.5% | ❌ |
| 4 | Government orders of Rs 54.15 Cr "demonstrated our growing capability to deliver ... at scale" (AR p.7) | An order award, not delivery: 54.15 Cr is about 2.0% of CON revenue (derived); revenue booked and cash received NOT FOUND | ❌ unproven |
| 5 | BSE Main Board listing as proof of "transparency" (AR p.7) | Listing happened 09-Dec-2025 (AR p.37), but disclosure is thin where it matters (covenants, HK tax, concentration) | ✅ fact, ❌ inference |
| 6 | "The Company has judiciously managed the debt-equity ratio" (AR p.47) | D/E 0.24 to 0.89 (AR p.46) | ❌ |
| 7 | Global expansion: Southeast Asia, Middle East, "Strong distribution tie-up in Middle East" (AR p.9-10) | Outside-India revenue fell to 90,263.93 from 109,607.00 (-17.6%) (CON Note 23.2 p.107) | ❌ |

### 6B Strategic priorities
Three-pronged: strengthen the core (Market Entry), brand licensing and contract manufacturing, new products and platforms (surveillance with Sparsh and Matrix, drones with PDRL, Kaspersky, EIZO) (AR p.14). Specific enough in naming partners. Capital allocated: PPE/intangibles 330.04 (CON), acquisitions nil in FY26, Rs 54.15 Cr government orders. Execution evidence thin: Solutions segment revenue not reported; no capex for contract manufacturing (fabless, SCL-run).

### 6C Metrics showcased vs absent
Showcased: revenue, EBITDA, PAT, EPS, partnerships, awards, units sold, marketing counts. Absent: CFO, free cash flow, receivable days (only as a turnover in the ratio table), net debt, HK share of profit and tax, customer concentration, brand margin, royalty rate, ROCE definition.

### 6D Tone drift vs prior year
Prior-year AR not held; NOT FOUND IN DOCUMENT. Within this AR the message itself says FY24-25 built the foundation and FY25-26 pivots to "growth and scale" (AR p.7): the priority moved from margin to growth, and the numbers show growth up and margin down.

### 6E Quiet Abandonment Check
| # | Opening claim (quote) | Where it should show up | Class | Materiality |
|---|---|---|---|---|
| 1 | "Those decisions [higher-margin focus] gave us the confidence ..." and "Scale Higher-Value Businesses" (AR p.7, p.14); Brand Licensing "a key big bet and strategic growth lever" (AR p.15) | Segment note: Brand share 14.11% from 15.25%; Brand revenue +40.7% vs Market Entry +54.2%; MD&A credits growth to Samsung, Cooler Master, ViewSonic (AR p.45) | (c) hedged retreat: brand grows but the mix moves the other way and the AR never says so | Changes the thesis: the mix-shift engine is the investment case |
| 2 | "Joint venture with CyberPowerPC USA" (AR p.6) | AOC-1 "no Joint Venture" and one associate (AR p.64); CyberPower appears only as a vendor line (AR p.45) | (a) implicit retraction (or marketing language) | Low to medium; no JV capital or result anywhere |
| 3 | Global/Middle East/Southeast Asia expansion; "Distribution network in 38 countries" (AR p.9-10, p.15) | Outside-India revenue -17.6% CON, -21.5% SA exports | (a) implicit retraction | Medium: all FY26 growth is India (+164.9%) |
| 4 | Three verticals including Solutions as an "integrated technology platform" (AR p.46) | Note 37 reports two segments only; Solutions revenue not reported; no project detail beyond Rs 54.15 Cr of orders | (b) silent drop in operational sections | Medium: the project engine is not measurable |
| 5 | "D2C Play: Rollout planned"; "AI-driven demand planning ... carbon-light warehousing" (AR p.15, p.25) | Directors' Report: "operations do not require significant absorption of technology" and "no additional investment" in energy (AR p.40) | (b) silent drop | Framework noise |

**Phase 6 verdict: 🟡 Watch.** The front matter is long on partnership detail and short on the cash and mix facts the back pages disclose.

---------------------------------------------------------------------
# PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Result | Top 3 reasons |
|---|---|---|
| Value + Quality | FAIL | (1) CFO negative, ROE leverage-driven; (2) ND/E 0.83 CON and all debt on demand; (3) accounting quality 5/10 and thin disclosure. Cheap on the AR date (market cap Rs 793.11 Cr = 12.8x owners' PAT of Rs 61.87 Cr, derived) does not offset |
| GARP | WATCHLIST (fullest) | See below |
| Turnaround | FAIL as a label (no loss, no distress; the issue is growth-financed stress) | (1) PAT up 32.4% in a growth year, not a recovery; (2) no margin trough in the AR (net margin 2.98% to 2.60%, down not up); (3) the "inflection" the operator seeks is cash conversion, which the AR shows moving the wrong way (CFO (27,188.34)); whether H1 FY27 turned is NOT in the AR |
| Capex-Led Growth | FAIL | Asset-light: capex 330.04 vs assets 93,723.64; growth is working-capital led |
| Cash Flow Compounder | FAIL | CFO/PAT 0.41x then negative |
| Contrarian | WATCHLIST | Price history not recoverable from the text layer; 12.8x P/E at 31-Mar-2026 but no sentiment evidence in the AR |
| Insider Confidence | WATCHLIST | Positive: promoter 56.62% flat, Ketan funded 5,00,000 warrants at about Rs 450; negative: 24-41% pay hikes, executive on Click Retail's board, pledge data absent |
| Guidance Divergence | WATCHLIST | AR claims (margin strengthening, operational discipline) diverge from the audited numbers; numeric guidance is not in the AR, so the test needs the Q2 FY27 deck |

GARP, fullest reasoning (operator mandate):
- Growth is real and audited: CON revenue +51.7%, PBT +31.8%, owners' EPS +27.5% to 41.04 (AR p.46, p.97). At the AR's own market cap (Rs 793.11 Cr, 31-Mar-2026), 12.8x trailing owners' PAT is a low multiple against 27.5% EPS growth, a PEG near 0.5 (derived). Memory's current P/E (27.4x at 11-Nov-2026) means the re-rating has already happened; valuation is a later stage's job.
- What breaks GARP is growth quality. Margin fell; ROE rose only through leverage (equity multiplier 1.72x to 2.42x); each Rs 100 of domestic sales needs about Rs 31 of receivables (112 days); and 51.1% of PAT is untaxed HK profit whose cash did not reach India (subsidiary CFO (1,450.22), HK cash 59.99).
- The price paid for growth is rising: finance cost +103.5% vs revenue +51.7%; interest cover 4.96x from 7.11x (derived).
- Sustainability tests for the next stages: SCL transfer-pricing and tax durability; whether SA PAT (3,434.75, with a 2.2% dividend payout) can service Rs 324 Cr of debt; receivable conversion after year end.
- Conclusion: GARP only if cash conversion is proven in later periods; on this AR alone, WATCHLIST.

Turnaround, fullest reasoning:
- The framework needs a trough followed by a measurable inflection. The AR holds no trough: EPS, revenue and PBT rose in both years shown (EPS 32.18 to 41.04). The one stress variable, cash, worsened.
- If the operator reads "inflection" as the cash cycle (CFO -Rs 271.9 Cr to +Rs 351.24 Cr in memory), the AR gives the base but not the turn: closing receivable days 76.3, domestic days about 112 with unchanged credit terms, 100% on-demand debt. Triggers for a positive read: receivable days below 60, short-term debt falling, CFO/PAT above 0.7 with customer advances not the driver. None is evidenced here.
- Verdict: FAIL as a classical turnaround, WATCHLIST for a working-capital inflection pending post-March data.

---------------------------------------------------------------------
# PHASE 8: FINAL VERDICT DASHBOARD

### Company snapshot
Creative Newtech Ltd; NSE CNL, BSE 544631 (listed 09-Dec-2025). IT, imaging and lifestyle technology distribution (Market Entry Specialist 85.89% of CON FY26 segment revenue, AR p.15) plus Brand Business (14.11%), including the Honeywell licence run through Secure Connection Ltd (HK). FY26 CON: revenue 270,461.72; PBT 8,176.20; PAT 7,029.29 (owners 6,187.14); CFO (27,188.34); borrowings 32,426.09; promoter 56.62%; market cap Rs 793.11 Cr at 31-Mar-2026.

### Phase verdicts
| Phase | Verdict |
|---|---|
| 1 Auditor and CARO | 🟡 |
| 2 Notes | 🟡 (borderline 🔴 on provisioning) |
| 3 Financial statements | 🔴 |
| 4 Risk and MD&A | 🟡 |
| 5 Governance | 🟡 |
| 6 Front matter | 🟡 |
| 7 Best-fit | GARP, WATCHLIST |

### Quality score (/10; 25% each)
| Component | Score | Basis |
|---|---|---|
| Governance | 5 | Independent majority and clean dockets vs promoter-dense RPTs, counterparty directorship, pay jumps, minor secretarial exceptions, no pledge visibility |
| Accounting quality | 5 | Reconciles with B02: ties internally, thin where exposure is largest |
| Balance sheet | 4 | D/E 0.837 (from 0.232), 100% on-demand debt, rated base Rs 209 Cr vs borrowings Rs 324 Cr, cash 6.7% of debt |
| Earnings quality | 4 | CFO negative; 51.1% of PAT offshore at nil tax; other income 28.1% of SA PBT; ROE leverage-driven; segment margin down |
| Overall | 4.5 / 10 | Average of the four |

### Top 3 strengths
1. Audited, internally consistent growth: revenue +51.7%, EPS +27.5% (AR p.97, p.46).
2. Asset-light model with unmodified opinions, no CARO adverse remark, no loans to promoter entities, no fraud or whistleblower item (AR p.69-71).
3. Promoter stake stable at 56.62%, and the promoter funded 5,00,000 warrants in FY25 (Note 13, AR p.82).

### Top 3 red flags
1. Operating cash outflow (27,188.34) funded by bank debt that rose 366% on a mostly on-demand footing; receivable allowance 0.14%.
2. 51.1% of group PAT earned in HK at nil tax, not audited by the group auditor, with no cash upstreamed and a transfer-pricing channel (SCL purchases 15,539.15; FY27 limit Rs 750 Cr).
3. Promoter-linked dependence and related-party leakage: Click Retail balance 4,773.50 with a CNL director on its board; executive pay up 35.6%; Rs 209 Cr rated base vs Rs 324 Cr borrowings.

### Monitorables
| Metric | Threshold | Where | Why |
|---|---|---|---|
| CON closing receivable days | below 65 improving; above 80 red (76.3 now) | Half-year balance sheet and ratio table | Test of working-capital inflection |
| CFO / PAT | above 0.7; check that customer advances and the SCL payable swing are not the driver | Half-year cash flow | Cash conversion |
| Short-term borrowings and ND/E | CON ND/E at or below 0.6 (0.83 now); borrowings inside sanctioned limits | Results, CRISIL rationale | Refinancing and covenant risk |
| HK share of PAT and tax | Standalone vs consolidated PAT and tax lines; flag nil tax continuing; any HK dividend or tax disclosure | Quarterly results, annual notes | Durability of 51.1% |
| SCL RPT utilisation | Run-rate against 75,000 lakh; AGM 30-Sep-2026 vote | RPT disclosures, AGM results | Transfer pricing |
| Brand margin and share | CON brand margin 33.16%, share 14.11% | Segment note | Thesis margin claim |
| Click Retail and related-party receivables | Click Retail balance below 3,000 | Note 36 | Related-party credit |
| Allowance / gross; >6 month bucket | Allowance above 0.5%; >6 months below 3.5% | Receivables note | Credit losses |
| Infinova definitive agreement | Consideration and funding disclosed | Exchange filings | Capital need |
| Outside-India revenue | Back to growth from 90,263.93 | Geography note | Global expansion claim |

### One-line verdict
CNL shows audited 52% growth and a low multiple at the AR date, but this AR proves only a receivable-funded, leverage-driven, offshore-tax-sheltered profit stream (CFO -Rs 271.88 Cr, 51.1% of PAT in HK); best-fit strategy is GARP on watchlist, conditional on proven cash conversion in later periods (4.5 / 10).

---------------------------------------------------------------------
## INPUT GAPS CARRIED
Shareholding pattern absent (pledge, FII/DII trend not testable); only FY2025-26 AR held (no 3-year trends, no tone-drift test, "first disclosed in this AR" tests limited to nil FY25 comparatives); screener formula sheets blank; peer CSVs absent.

```yaml
stage: B03-ardeep
company: "CNL"
run_date: "2026-11-11"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "shareholding pattern absent (B00): promoter pledge and FII/DII trend NOT FOUND"
  - "only FY2025-26 AR held: no FY24 balance sheet, no prior-year AR, no 3-year trends or tone-drift test"
  - "screener formula sheets blank (B00)"
  - "peer CSVs absent (B00)"
flags:
  - {type: FLAG-CASH, reason: "CON CFO (27,188.34) lakh (Rs 271.88 Cr) vs PAT 7,029.29; SA CFO (25,738.12); CFO/PAT 0.41x in FY25 then negative; receivable build funded by +25,471.81 short-term bank debt (CON CF AR p.98; SA CF AR p.74)"}
  - {type: FLAG-LEVERAGE, reason: "CON D/E 0.837 from 0.232; borrowings 32,426.09 all within 12 months; CRISIL-rated facilities Rs 209 Cr vs borrowings Rs 324.26 Cr (SA Note 32 AR p.86; AR p.58; AR p.46)"}
  - {type: FLAG-OFFSHORE-PROFIT, reason: "HK subsidiaries 3,594.54 = 51.1% of CON PAT at nil tax (AOC-1 AR p.63; CON Note 30 AR p.108: rate-differential 904.84); not audited by group auditor (AR p.93)"}
  - {type: FLAG-RPT, reason: "SCL purchases 15,539.15 and FY27 approval Rs 750 Cr (AR p.30); Click Retail balance 4,773.50 with CNL WTD Vijay Advani a director of Click Retail (SA Note 36 AR p.89; Notice Annexure I AR p.35-36)"}
phase_verdicts: {p1: "yellow", p2: "yellow", p3: "red", p4: "yellow", p5: "yellow", p6: "yellow", p7_best_fit: "GARP (WATCHLIST)"}
overall_quality: 4.5
quality_components: {governance: 5, accounting: 5, balance_sheet: 4, earnings: 4}
kill_switch_notes:
  - "P1: would not stop on audit report alone; unmodified opinion, no CARO adverse remark; but 51.1% of PAT rests on unnamed HK auditors and consolidated annexures carry Indian-subsidiary template errors (AR p.93-96)"
  - "P2: would not stop; numbers tie; require receivable composition, covenants, HK tax reason before relying on cash story"
  - "P3: would have reason to stop and seek post-balance-sheet cash evidence: CFO (27,188.34), bank debt +366%, ROE gain leverage-driven (AR p.97-98)"
  - "P4: would not stop; MD&A is bland not false, but missing-risk list is the thesis risk"
  - "P5: would not stop; no fraud, qualification or promoter exit; need shareholding pattern for pledge"
triple_pass_verification:
  verified: 15
  discrepancies: []
missing_risks:
  - {risk: "receivable and working-capital funding", evidence: "CFO (27,188.34); receivables +137.7%; borrowings 32,424.88 (CON AR p.97-98, Note 17 AR p.106)"}
  - {risk: "offshore profit concentration, nil tax, other auditors", evidence: "3,594.54 = 51.1% of PAT; AOC-1 tax Nil (AR p.63); Other Matters (AR p.93)"}
  - {risk: "transfer pricing and SCL dependence", evidence: "purchases 15,539.15; FY27 limit Rs 750 Cr (AR p.30); brand margin 10.56% SA vs 33.16% CON (Note 39 AR p.90; Note 37 AR p.112)"}
  - {risk: "Honeywell licence term and royalty", evidence: "royalty 595.73 (CON Note 29 AR p.108); licence term NOT FOUND"}
  - {risk: "customer concentration", evidence: "no major-customer disclosure in Note 37 (AR p.111-112); Click Retail 4,773.50 (Note 36 AR p.89)"}
  - {risk: "rated-limit headroom", evidence: "CRISIL Rs 209 Cr (AR p.58) vs borrowings Rs 324.26 Cr (AR p.46)"}
  - {risk: "promoter-family and counterparty-board dependence", evidence: "pay 236.74 (Note 36 AR p.88); Advani director of Click Retail (AR p.35-36)"}
  - {risk: "recurring GST disputes", evidence: "GST 514.78 of 600.01, +112.8% (SA Note 35 AR p.87)"}
  - {risk: "Infinova acquisition funding", evidence: "Directors' Report s.35 (AR p.41); consideration NOT FOUND"}
guidance_table:
  - {claim: "Honeywell sales expected to cross 3 million units", number: "3 million units", timeframe: "2026", credibility: "2/5: no base-year units, no revenue link (AR p.9)"}
  - {claim: "SCL related-party approval ceiling", number: "Rs 750 Cr (75,000 lakh)", timeframe: "FY27", credibility: "2/5: FY26 limit 25,000 lakh, usage 17,747.69 (AR p.30, p.43)"}
  - {claim: "additional brand rights to lift profitability substantially", number: "none", timeframe: "FY27", credibility: "2/5 (AR p.36)"}
  - {claim: "Vision 2030 first Indian consumer technology brand with meaningful global presence", number: "none", timeframe: "2030", credibility: "1/5 (AR p.25)"}
  - {claim: "Infinova India acquisition", number: "none; no definitive agreement", timeframe: "pending", credibility: "2/5 (AR p.41)"}
monitorables:
  - {metric: "CON closing receivable days", threshold: "below 65 improving; above 80 red (76.3 at Mar-2026)", where: "half-year balance sheet and ratio table", why: "tests working-capital inflection"}
  - {metric: "CFO / PAT", threshold: "above 0.7 without customer advances or SCL payable swing as driver", where: "half-year cash flow statement", why: "cash conversion"}
  - {metric: "Short-term borrowings and CON ND/E", threshold: "ND/E at or below 0.6 (0.83 now); borrowings inside sanctioned limits", where: "results and CRISIL rationale", why: "refinancing and covenant risk"}
  - {metric: "HK share of PAT and tax", threshold: "standalone vs consolidated tax equal and nil HK tax continuing = flag; any HK dividend or tax disclosure", where: "quarterly results and annual notes", why: "durability of 51.1% of PAT"}
  - {metric: "SCL RPT run-rate", threshold: "vs 75,000 lakh FY27 ceiling; AGM vote 30-Sep-2026", where: "RPT disclosures and AGM voting results", why: "transfer pricing and related-party scale"}
  - {metric: "CON brand segment margin and share", threshold: "margin 33.16%, share 14.11% at FY26", where: "segment note", why: "thesis margin claim"}
  - {metric: "Click Retail balance", threshold: "below 3,000 lakh (4,773.50 now)", where: "related-party note", why: "related-party credit and counterparty-board link"}
  - {metric: "Allowance / gross receivables and >6 month bucket", threshold: "allowance above 0.5%; >6 months below 3.5% of gross", where: "receivables note", why: "credit-loss adequacy"}
  - {metric: "Outside-India revenue", threshold: "return to growth from 90,263.93 lakh", where: "geography disclosure (Note 23.2)", why: "global expansion claim"}
ar_new_downstream_entities:
  - {name: "Infinova India Private Limited", where_in_ar: "Directors' Report s.35 (AR p.41)", entity_type: "proposed acquisition target; no binding agreement"}
  - {name: "Lumisynch Private Limited", where_in_ar: "SA Note 36 (AR p.89): purchases 2.52, nil FY25", entity_type: "related-party counterparty (new vs FY25 comparative)"}
  - {name: "Euphoriya Hospitality Private Limited", where_in_ar: "SA Note 36 (AR p.89): sales 0.06, nil FY25", entity_type: "related-party counterparty (new vs FY25 comparative)"}
  - {name: "Samriddhi Automations Private Limited (Sparsh)", where_in_ar: "Key Milestones (AR p.8)", entity_type: "new brand partner, STQC surveillance OEM"}
  - {name: "Matrix", where_in_ar: "Key Milestones (AR p.8)", entity_type: "new brand partner, Pan-India distribution"}
  - {name: "EIZO Private Limited", where_in_ar: "Key Milestones (AR p.8)", entity_type: "new brand partner, Pan-India distribution"}
  - {name: "PDRL", where_in_ar: "Key Milestones (AR p.8)", entity_type: "new brand partner, drone technology (full legal name NOT FOUND)"}
  - {name: "Kaspersky, BRYT, Corsair, Dahua, Colorful, PNY", where_in_ar: "Key Milestones (AR p.8) and vendor list (AR p.45)", entity_type: "new or expanded brand partners"}
strengths_top3:
  - "Audited growth: CON revenue +51.7%, owners' EPS +27.5% to 41.04 (AR p.97, p.46)"
  - "Asset-light, unmodified opinions, no CARO adverse remark, no fraud or whistleblower items, no loans to promoter entities (AR p.69-71)"
  - "Promoter stake steady at 56.62% and promoter funded 5,00,000 warrants in FY25 (Note 13 AR p.82)"
red_flags_top3:
  - "CFO (27,188.34) lakh funded by +25,471.81 short-term bank debt; receivable allowance 0.14% of gross (AR p.98, p.74, Note 8)"
  - "51.1% of CON PAT earned in HK at nil tax, not audited by group auditor, with a transfer-pricing channel via SCL (FY27 limit Rs 750 Cr) (AR p.63, p.93, p.30)"
  - "Related-party and promoter dependence: Click Retail 4,773.50 with CNL director on its board; executive pay +35.6% proposed; Rs 209 Cr rated base vs Rs 324 Cr borrowings (AR p.89, p.35-36, p.58)"
best_fit_strategy: "GARP (WATCHLIST), conditional on proven cash conversion; Turnaround FAIL as a classical label"
one_line_verdict: "Audited 52% growth at a low AR-date multiple, but proven only as receivable-funded, leverage-driven, offshore-tax-sheltered profit (CFO -Rs 271.88 Cr, 51.1% of PAT in HK); GARP on watchlist pending cash-conversion proof, 4.5/10."
analyst_note: "All 15 B02 findings re-verified, zero value discrepancies. New this stage: (1) India sales +164.9%, exports -21.5%; domestic receivable days about 112 in both years, so the build is mix shift at unchanged terms, not slower collection (derived; assumes negligible export receivables). (2) CON Note 30 prices the HK nil-tax effect at 904.84 (=25.17% x 3,594.97). (3) Brand margin gap 10.56% SA vs 33.16% CON is the HK layer. (4) Vijay Advani is a director of Click Retail, the 4,773.50 debtor. (5) FY27 SCL ceiling is 4.2x FY26 actual. (6) The 4,493.48 'buyers credit expenses' is a settlement; FX outgo reconciles to 50,207.90. (7) Consolidated annexures cite an Indian subsidiary that does not exist. BSNL and Zicom are absent from the AR."
```
