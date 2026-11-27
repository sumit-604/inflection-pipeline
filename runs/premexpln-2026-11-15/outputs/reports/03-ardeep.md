# Stage 3 AR Deep Dive (Backward Read): PREMEXPLN, FY2025-26
Run: premexpln-2026-11-15 | Model: claude-sonnet-5-5 | Source: Annual_Report_2026.txt (46th AR, 218 pages), prior year Annual_Report_2025.txt (45th AR)

Conventions. Statements and notes print "INR lakhs" (L). The MD&A, Chairman and MD letters, and the highlights page print "Rs million" (mn). No unit is converted silently. Anchors use p.N = the "[page N]" marker in the .txt; printed page = N minus 3. "(derived)" marks my arithmetic on filed numbers. [INFERENCE] marks a linkage the filing does not state. Verdict labels use the words Clean / Watch / Red Flag.

Reading order followed: auditor and CARO (p.100-108), statements (p.109-112), notes (p.113-153), risk and MD&A (p.24-27, BRSR p.71-99), governance (p.38-57), Directors' Report (p.28-37), then letters and front matter (p.4-23), then prior year for the backward view.

---
## A. LOAD-BEARING FACTS: WHAT THE FILING SHOWS (first verification priority)
| # | Fact to check | What the AR shows | Status |
|---|---|---|---|
| 1 | FY26 operating cash flow Rs -1 cr vs PAT Rs 45.8 cr | CFO (144.14) L vs PAT 4,582.51 L (CFS p.112). Consolidated CFO (127.20) L (p.164). Two prior years were positive: FY25 11,861.66 L, FY24 7,899.69 L (FY25 AR CFS). 3-year cumulative CFO 19,617.21 L vs PAT 10,249.92 L = 1.91x (derived). | CONFIRMED; reversal of an FY25 payables stretch is one reading |
| 2 | Other income | 4,214.49 L (FY25 211.53 L): 3,417.80 L supplier purchase discount "relating to materials procured and consumed in the previous financial year" (Note 22 p.133) + 500.00 L provision reversal (Note 29(c) p.139) = 3,917.80 L = 64.8% of PBT 6,043.17 L (derived) | CONFIRMED |
| 3 | Promoter holding move to AKS Family Trust | Dr. A.N. Gupta 1,63,84,400 + Dr. Kailash Gupta 58,37,335 = 2,22,21,735 shares (41.33%) settled into AKS Family Trust; trust became promoter w.e.f. 18 Feb 2026 under SEBI Exemption Order WTM/KCV/CFD/18/2025-26 dated 8 Jan 2026 (CG p.41; Note 14 p.129). SPA 9 Jul 2026: trustees (Kailash Gupta, Shonika Prasad) sell the same 2,22,21,735 shares to Apollo Micro Systems for about Rs 1,550 Cr cash; open offer 1,39,77,911 shares (26%) at Rs 698 = Rs 975.66 Cr; CCI approval pending (DR p.29). | CONFIRMED. The sale-chain reading (B02 Reading B) is now supported: the trust was the SPA seller 4.7 months after the transfer |
| 4 | Related-party items | RPT ex-dividend about 491.86 L = 1.27% of revenue (derived from Note 38 p.148-150). No promoter loans given. Loan from subsidiary PWPL 423.39 L. AOC-2 shows only rent 1.19 L (p.65). Apollo/IDL related-party terms, non-compete and board changes: NOT FOUND IN DOCUMENT (the SPA text is not in the AR) | PARTIAL |
| 5 | Katepally accident 29 Apr 2025 | Fire and explosion, propellant mixing building, four lives lost, plant "temporarily paused" (DR p.29). TGPCB closure order 7 May 2025, revoked on payment of Rs 6,75,000 environmental compensation, "resumption of production approved" (BRSR p.78, p.95). Restart date NOT FOUND. BRSR p.85 shows FY26 fatalities 5 (employees 1, workers 4), one more than the four in the DR. | CONFIRMED, with one unexplained fatality |
| 6 | Peddakandukur fire, licence suspension and restoration | Chairman mentions "tragic incidents at our Peddakandukuru and Katepally facilities" (p.5). FY25 AR: 4 Jan 2025 fire at Peddakandukuru, one life (FY25 AR DR). PESO licence suspension and restoration: NOT FOUND IN DOCUMENT. Peddakandukuru Consent for Operation expires 31 Oct 2026 (BRSR p.94); renewal NOT FOUND. | PARTIAL |
| 7 | Insurance claim | Assets lost 709.80 L; receivable 609.80 L in note text, 683.59 L on balance sheet (gap 73.79 L); 100.00 L loss; 520.00 L ex-gratia as exceptional; unsettled at 31 Mar 2026 (Note 7(ii) p.125; EoM p.100) | CONFIRMED |
| 8 | Rs 18.9 cr export order cancelled, April 2026 licence refusal | NOT FOUND IN DOCUMENT. DR section 8 (p.29, dated 13 Aug 2026) lists only the SPA as a post-year-end event; Note 45 lists only the dividend (p.153). | NOT FOUND |
| 9 | Order book, segment/product split; sector-cap separator | Order book Rs 15,690 mn as of May 2026 = 4.04x FY26 revenue; Defence about 95%, Explosives about 2%, Services about 3% (MD&A p.25). Revenue: Defence and Space Rs 3,154 mn (81%), Commercial Explosives Rs 729 mn (19%) (MD&A p.25); BRSR 81.22% / 18.78% (p.71). Ind AS 108: one reportable segment, no segment profit (Note 2.2 p.113; consolidated Note 35 p.199). | See sector-cap note below |

Sector-cap separator (B00: Defence / strategic 38x vs Specialty chemicals 35x). The filed revenue split (81/19) and order book split (95/2/3) both favour reading (a), Defence / strategic. The observation B00 named, the filed segment result split, is NOT FOUND IN DOCUMENT in this AR: the company reports one segment and gives no segment profit. Segment profit may sit in the 29 May 2026 investor presentation (cited as the MD&A source, p.27), which is for B04. Caveat that matters: FY26 PAT is 64.8% non-recurring other income and operating EBITDA is 10.0% of revenue, so the earnings that carry the multiple are not yet shown to be defence earnings. "Defence and Space services" also contains O&M services (sale of services 3,593.78 L, 9.3% of revenue, Note 21 p.132).

SEBI order check for stage 0 (freshness pair). The AR names one SEBI order: Exemption Order WTM/KCV/CFD/18/2025-26 dated 8 Jan 2026 under Reg 11(5) of SAST (CG p.41, footnote to table h). It is an exemption order for AKS Family Trust, not an order against the company, promoters or directors. The order text is already in the corpus: inputs/announcements/20260220-61-General-Updates.txt (9 pages), filed with the 20 Feb 2026 SAST disclosures (20260220-59). Pair status stays PASS. A stock-exchange fine for FY25 (delay in member approval for a non-executive director under Reg 17(1A)) is also disclosed (CG p.54); it is an exchange fine, not a SEBI order. Facts from the order text: trust deed 29 Sep 2025, irrevocable discretionary private trust; grounds "streamline succession", "non-commercial transaction", "no change in control" (order pp.2-6).

---
## PHASE 1: AUDITOR'S REPORT AND CARO (read first, back of the book)

### 1A Core opinion
| Item | Finding | Anchor |
|---|---|---|
| Standalone FS opinion | Unmodified ("true and fair view"), dated 29 May 2026, Majeti & Co, partner Kiran Kumar Majeti, UDIN 26220354RSEZVA8030 | p.100, p.103 |
| Consolidated FS opinion | Unmodified, same date | p.154, p.158 |
| Going concern, parent | No material uncertainty; CARO xix: nothing causing belief the company cannot meet liabilities due within one year | p.108 (xix); Note 2.1(ii) p.113 |
| Going concern, subsidiary | Material uncertainty for PELNEXT Defence Systems Pvt Ltd: net assets (6.63) L; current liabilities exceed current assets by 6.63 L; "net worth is eroded completely" | Other Matters (b) p.157; consolidated Note 43 p.204 |
| Internal financial controls (Annexure A) | QUALIFIED opinion, standalone and consolidated. Basis: "the Company is yet to establish adequately designed and operating procurement controls appropriate to its current scale ... Significant procurement decisions and approvals were concentrated with a single authorised individual, resulting in inadequate segregation of duties and increasing the risk of errors, or management override of controls." Auditor calls it a "material weakness" | p.103, p.104-105; consolidated p.159-160 |
| Prior year | FY25 IFC opinion was unmodified (22 May 2025, FY25 AR p.105) | FY25 AR |

The triple-pass notes stage (B02) did not carry the IFC qualification because it sits outside the notes. It is the single most important new fact in this stage. Reading A: a design gap in a company that grew fast (revenue 27,171.67 L in FY24 to 41,745.23 L in FY25); management states new SOPs "since July 2026" (DR p.34). Reading B: the weakness is where the large supplier items sit (3,417.80 L settlement, 11,654.90 L to 4,151.63 L payables swing, supplier advances +98.6%) and the auditor tested an area where something went wrong [INFERENCE]. The observation that separates them: the FY27 auditor's IFC opinion and any disclosure of the whistle-blower complaint's subject (see 1D xi).

### 1B Key Audit Matters
| # | Subject | Why key | How addressed | Risk |
|---|---|---|---|---|
| 1 | Fair value of trade receivables | 29.61% of receivables past due over 180 days (1,582.37 L / net 5,344.57 L, derived); mostly PSU and Government; ECL is a judgement | Confirmations drew no response; alternative procedures: post year-end receipts, source documents, analytics, enquiries; ECL model tested (p.100-101) | Red Flag |
| 2 | Revenue recognition, variable consideration | Powder factor deductions, liquidated damages, rebates, price revisions | Controls, contract sample, back-testing of past estimates to settlements, constraint test (p.101) | Watch |
Observations. (i) No KAM on other income, although 3,917.80 L (64.8% of PBT) is one-off. (ii) No KAM on the insurance receivable; it gets an Emphasis of Matter instead. (iii) The KAM percentage basis changed: FY26 29.61% is on net receivables; FY25 20.50% is on gross (887.36 / 4,329.61). On one basis the move is 20.5% to 25.3% (gross) or 23.3% to 29.6% (net) (derived). The deterioration is real on either basis.

### 1C Emphasis of Matter and Other Matters
| Item | Content | Anchor |
|---|---|---|
| EoM | Accident at manufacturing facility; assets NBV 709.80 L; claim receivable 609.80 L; 100 L charged; claim pending with insurer at 31 Mar 2026 | p.100; consolidated p.154 |
| Other Matters (a) | Two subsidiaries (PWPL, PELNEXT) audited by other auditors: total assets 706.81 L, income 27.73 L, PAT 0.25 L | p.157 |
| Other Matters (a) JV loss | Auditor states share of JV loss 2.22 L; consolidated P&L shows 1.21 L; AOC-1 shows 2.47 L total of which 1.21 L considered, 1.26 L not considered. Immaterial but a three-way mismatch | p.157, p.162, p.37 |
| Other Matters (b) | PELNEXT going concern uncertainty (above) | p.157 |

### 1D CARO 2020, clause by clause (adverse or qualified remarks)
| Clause | Finding | Amount (L) | Anchor | Risk |
|---|---|---|---|---|
| i(b) | Physical verification; unserviceable assets written off | NBV 37.50 | p.106 | Clean |
| ii | Inventory verified; differences under 10% per class; bank returns agree with books | n/a | p.106; Note 10(b) p.126 | Clean |
| iii(b),(c),(e) | Loan to subsidiary PELNEXT has no repayment schedule; auditor "unable to comment on the regularity" | 6.66 (100% of loans, related party) | p.106; Note 8 p.125-126 | Watch (small) |
| vii(a) | Regular in undisputed dues. Also states sales tax, service tax, VAT and excise are "not applicable" | n/a | p.107 | Watch: contradicted by vii(b) listing CST and VAT |
| vii(b) | Disputed dues: CST 2007-08 Telangana High Court 151.31; Tamil Nadu VAT 2009-10 to 2015-16 Madras High Court 424.52; GST 2017-19 Singrauli tax office 98.88. Total 674.71 | 674.71 | p.107 | Watch. Income tax 61.84 is in Note 34 (p.145) but missing from vii(b) |
| ix | No default. "Loans includes Rs 423.39 lakhs repayable on demand and terms and conditions for payment of interest have not been stipulated" (loan from subsidiary PWPL); Note 15 shows a rate band of 7 to 8.95% and interest paid 26.48 L | 423.39 | p.107; Note 15 p.130; Note 38 p.149 | Watch: CARO and note disagree on whether interest terms exist |
| xi(a),(b) | No material fraud; no ADT-4 | n/a | p.107-108 | Clean |
| xi(c) | "one whistle-blower complaint was received by the Company during the year and up to the date of this report ... the special audit carried out by the Internal auditors under the oversight of TCWG ... no fraud on or by the Company has been identified ... The matters arising from the complaint resulted in identification of deficiencies in internal financial controls" | n/a | p.108 | Red Flag |
| xvii | No cash losses | n/a | p.108 | Clean |
| xx | CSR spent 59.38 vs required 58.32; nothing unspent | 59.38 | p.108; CSR p.66-67 | Clean |

Contradiction raised at the point it appears. CARO xi(c) says one whistle-blower complaint was received and a special audit was run. The Corporate Governance report says "The designated person had not received any complaint during the financial year ended 31st March, 2026" (p.54), and BRSR shows no employee or worker complaints (p.73, p.86). The Directors' Report does not mention the complaint or the special audit. The audit committee terms of reference include review of the whistle-blower mechanism (p.43). Either the complaint reached the auditor by another channel, or the governance report is wrong. The AR does not say which.

### 1E Auditor continuity
| Item | Finding | Anchor |
|---|---|---|
| Firm and tenure | Majeti & Co (FRN 015975S), second 5-year term from the 42nd AGM (16 Sep 2022) to the conclusion of the 47th AGM (2027). First term implies about 9 years of tenure at FY26 (derived from "second term") | DR p.33 |
| Rotation year | Term ends at the 47th AGM (Sep 2027) | DR p.33 |
| Fees (L) | Statutory audit 9.35; quarterly reviews 8.25; GST matters 3.00; certification 3.00; reimbursement 2.45; total 26.05 (FY25 25.12) | Note 29(a) p.139; CG p.54 |
| Audit vs non-audit | Audit-type 17.60; non-audit (GST matters plus certification) 6.00; ratio 34.1% (derived). Does not exceed audit. GST advisory by the statutory auditor is a watch item | Note 29(a) p.139 |
| Other | Audit fee 9.35 L is 0.02% of revenue. Same auditor issued the CG certificate (p.58), engagement letter 11 Oct 2025 | p.58 |

### 1F Standalone vs consolidated
Consolidated EoM, KAMs and IFC qualification repeat the standalone wording (p.154-160). Subsidiaries PWPL and PELNEXT and the JV are audited by other auditors; one subsidiary and the JV are exempt from IFC reporting (p.157). Consolidated CFO (127.20) L vs standalone (144.14) L (p.164, p.112). PAT 4,581.55 L vs 4,582.51 L. NCI 135.52 L (p.161) is 25.4% of PWPL net assets 532.94 L (p.203) against an 80% holding: a 5.4 point gap (derived), unexplained. PWPL has no revenue and has closed its factory (DR p.29-30).

### Phase 1 summary
| Test | Result |
|---|---|
| Opinion on FS | Unmodified, with EoM |
| IFC opinion | Qualified; single-approver procurement; material weakness |
| Whistle-blower and special audit | Present in CARO; absent from governance report |
| KAM receivables | Red Flag |
| Fraud | None reported by auditor |
Phase 1 verdict: Red Flag.
Kill switch assessment (informational): Based on phases so far, a human reviewer would have reason to pause, because the auditor qualified internal financial controls over procurement in the same year a 3,417.80 L supplier settlement drives 64.8% of PBT, and a whistle-blower complaint plus special audit exist. The pipeline continues.

---
## PHASE 2: NOTES TO FINANCIAL STATEMENTS (verify, extend, summarise)

### 2.0 Verification of the triple-pass Top 15 against the document
| Rank | Triple-pass claim | AR check | Result |
|---|---|---|---|
| 1 | Other income 4,214.49 L incl. 3,417.80 + 500.00; 64.8% of PBT; PBT without ~2,125.37; EBIT 2,713.63, ROCE 8.03% | Note 22 p.133; Note 29(c) p.139; Note 43 p.152. 3,917.80 / 6,043.17 = 64.83%. 3,882.18 EBITDA less 1,168.55 depreciation = 2,713.63; / capital employed 33,790.99 (28,903.17 + 3,656.71 + 1,231.11) = 8.03% | Verified |
| 2 | CFO (144.14) vs PAT 4,582.51; WC absorbed 5,863.23; cash 9,309.24 to 5,057.21 | CFS p.112: (3,446.92) + 5,048.20 + (7,464.51) = (5,863.23) | Verified |
| 3 | Over-1-year receivables 887.36 L (FY25) to 888.35 L (FY26); over-6-month 1,582.37 L = 25.3% (FY25 20.5%); over-3-year exceeds feeder by 20.33 L; ECL covers 57.2% | Over-6-month, 25.3%, 20.5%, 20.33 L, 57.2% verified (Note 11(c),(d) p.127-128). The over-1-year figure is wrong: FY26 over-1-year = 298.38 + 556.28 + 332.07 = 1,186.73 L. 888.35 L is 556.28 + 332.07, the over-2-year sum. FY25 over-1-year is 887.36 L (575.62 + 123.87 + 187.87). Like for like: +299.37 L, +33.7% | DISCREPANCY (direction worse than stated) |
| 4 | Net receivable days 50.2 vs 33.3 vs 97.6; note blames "increase in Revenue" | 5,344.57 / 38,834.14 x 365 = 50.2; 3,807.81 / 41,745.23 x 365 = 33.3; FY24 7,265.33 (FY25 AR) / 27,171.67 x 365 = 97.6. Note 43 p.152 reason text confirmed; revenue fell 6.97% | Verified |
| 5 | Accident: 709.80; 609.80 vs 683.59 (gap 73.79); 100 + 520; current ratio 1.56 to 1.60 | Note 7(ii) p.125; BS p.109; (25,811.91 - 683.59) / 16,093.65 = 1.56 | Verified. Plant, deaths and TGPCB order are in DR p.29 and BRSR p.78, not in the notes |
| 6 | Variable consideration 5.99% (2,476.47) vs 9.37% (4,316.26); about 1,396 L | Note 21 p.133: 2,476.47 / 41,310.61 = 5.99%; 4,316.26 / 46,061.49 = 9.37%; (9.37% - 5.99%) x 41,310.61 = about 1,394 L | Verified |
| 7 | FX loss 591.64 (FY25 2.53) = 9.8% of PBT; realised ~613.15; rupee 10.6%; payables 2.5x receivables | Note 29 p.138; CFS p.112 (591.64 + 21.51); Note 32(B) p.142-143: 94.66 vs 85.58 per USD; 2,804.73 / 1,101.50 = 2.55 | Verified |
| 8 | Payables 11,654.90 to 4,151.63; supplier finance 747.56; 2-3y 457.12 vs feeder 8.36; FG +88.9% | Note 31 p.141; Note 15 p.130; Note 36 p.146; Note 10 p.126 (1,229.36 / 650.58) | Verified |
| 9 | Supplier advances 2,115.95 vs 1,065.61 (+98.6%); domestic 4.8x | Note 9(ii) p.126; domestic = 2,115.95 - 921.69 = 1,194.26 vs 246.46 = 4.85x (Note 32(B) p.142-143) | Verified |
| 10 | Contingent 8,343.60 = 28.9% of NW; LCs 7,607.05 (+28.0%); GST 98.88 | Note 34 p.145: 7,607.05 + 575.83 + 98.88 + 61.84 = 8,343.60 | Verified |
| 11 | Trust 2,22,21,735 (41.33%) equals three holdings; KMP pay +30.5% to 445.29 | Note 14 p.129; CG p.41 footnote; Note 38 p.148. Extension: date is 18 Feb 2026 (CG p.41); SPA seller is the trust (DR p.29). B02 listed both as undisclosed | Verified, with extension |
| 12 | Advances: domestic -35.0% to 4,075.98; foreign +163.2% to 2,546.28 | Note 19 p.132; Note 32(B): 6,622.26 - 2,546.28 = 4,075.98; 2,546.28 / 967.39 = 2.63 | Verified |
| 13 | Note 45 lists only the dividend 268.81 L | Note 45 p.153 | Verified |
| 14 | Single segment; no order book, ECL matrix, lease liability, customer name; gratuity 38.9% funded; 4% salary growth vs 10.1% | Note 2.2 p.113; Note 32(A) p.141; Note 21 p.133; Note 25 p.135-136: 598.79 / 1,538.88 = 38.9%; 6,113.51 / 5,550.26 = +10.15%. Extension: MD&A (not the notes) gives the segment revenue split and order book | Verified |
| 15 | ROCE capital employed defined two ways; land 39.2% of PPE; reserve 19.3% of NW | Standalone 8.03% ties with DTL (Note 43 p.152). Consolidated 8.35% ties only without DTL: EBIT 2,694.60 / (29,042.78 + 3,233.32) = 8.35%, though the printed formula includes DTL (Note 42 p.203). Land 7,012.62 / 17,907.14 = 39.2%; 5,570.59 / 28,903.17 = 19.3% (SOCE p.111) | Verified |
Result: 14 of 15 verified; 1 discrepancy (rank 3).

### 2A Accounting policy aggressiveness
| Policy | Finding | Read |
|---|---|---|
| Revenue (Note 2.5 p.115) | Point-in-time on delivery; O&M on output basis; powder factor and liquidated damages as variable consideration. Deduction rate 9.37% to 5.99% with no reason. Revenue estimate gain about 1,394 L (derived), 65.6% of PBT ex-one-offs 2,125.37 | Aggressive drift |
| Depreciation (2.6 p.116) | Straight line, Schedule II, residual up to 5%. FY26 depreciation 1,168.55 L vs 1,147.42 L on gross block cost of 25,930.38 L | Neutral |
| Capitalisation (2.11 p.119) | Policy allows borrowing-cost capitalisation. CWIP rose 284.73 to 2,639.23 L, but Note 3 shows no capitalised borrowing cost | Watch |
| Inventory (2.12 p.119) | FIFO, lower of cost and NRV; obsolete stock provision 13.72 L on 10,301.26 L | Light |
| ECL (2.10 p.118; Note 32(A) p.141) | Simplified approach; matrix named but not shown; 905.47 L = 14.5% of gross; charge 383.67 L (FY25 389.66 L) | Watch |
| Ind AS 116 | ROU 85.66 L land only; no lease liability; short-term lease exemption; rent 3.17 L vs 32.14 L | Neutral |
| Policy change | Ind AS 1 and Ind AS 7/107 amendments adopted; supplier-finance disclosure added in Note 15(e) (two sentences) | Thin |
| Grants | Export entitlements reduce cost of materials (2.22 p.121) | Neutral |
| Labour codes | Impact "not likely to be material" (p.145) | Neutral |

### 2B RPT map (Note 38 p.147-150; L)
| Item | FY26 | FY25 | % of revenue FY26 | Signal |
|---|---|---|---|---|
| KMP managerial remuneration | 445.29 | 341.33 | 1.15% | +30.5% vs revenue -7.0% |
| Sitting fees | 11.98 | 16.13 | 0.03% | Normal |
| Interest paid to subsidiary PWPL | 26.48 | 27.92 | 0.07% | Eliminates on consolidation |
| Loan payable to PWPL | 423.39 | 399.56 | n/a | On demand |
| Other (rent 1.19, loan to PELNEXT 2.00, JV 4.90, reimbursements) | 8.10 | | | Small |
| Total ex-dividend (derived) | about 491.86 | | 1.27% | Below 2% |
| Dividends to promoter family | 112.42 | 112.51 | | Same terms as others |
| Repayment of promoter loans | nil | 519.05 | | FY25 repaid |
Value-extraction signals: none in volumes. Payables to KMP of 173.03 L (employee benefits, Note 38(f) p.149) rose 58.5% from 109.14 L. Standalone Note 38(g) states KMP loans at 8.95%; consolidated Note 37(g) states 10% (p.201); no KMP loan is outstanding. The MD gives a personal guarantee for bank facilities (Note 15(a),(c) p.130).

### 2C Contingent liabilities
| Item | L | % of NW 28,903.17 | % of PAT 4,582.51 | Flag |
|---|---|---|---|---|
| LCs and bank guarantees | 7,607.05 | 26.3% | 166.0% | >25% of NW; backed by margin money 914.00 L (12.0%) |
| Sales tax disputes | 575.83 | 2.0% | 12.6% | No change from FY25 |
| GST | 98.88 | 0.3% | 2.2% | New |
| Income tax | 61.84 | 0.2% | 1.3% | Not in CARO vii(b) |
| Total | 8,343.60 | 28.9% | 182.1% | >25% of NW; <100% |
Excluding bank-issued LCs and guarantees, contested statutory claims are 736.55 L = 2.5% of NW (derived). No contingent liability for accident claims, compensation or the Katepally closure (Note 34 p.145). Capital commitments 1,708.70 L (Note 35).

### 2D Receivables
Gross 6,250.04 L (+44.4%) vs revenue -7.0%. Not due and unbilled 3,724.82 L (59.6%, FY25 62.4%); under 6 months 942.85 L; 6m-1y 395.64 L; 1-2y 298.38 L; 2-3y 556.28 L; over 3y 332.07 L (Note 11(c) p.127). The 1-2y bucket of 298.38 L has no feeder: FY25 6m-1y was nil (Note 11(d) p.128), so the ageing does not roll. Unbilled 141.60 L. One customer is 10% or more of revenue, unnamed (Note 21 p.133). Payers are described as PSU and Government (KAM p.100).

### 2E Inventory
10,301.26 L vs 15,349.46 L (-32.9%): raw material 6,067.25 (-24.4%), WIP 2,388.07 (-60.4%), finished goods 1,229.36 (+88.9%), against revenue -7.0% (Note 10 p.126). Inventory turnover 2.72x vs 3.22x (Note 43). WIP conversion fits a strong Q4 delivery; finished goods build is unexplained. No write-down beyond 13.72 L.

### 2F Borrowings
Total 3,656.71 L. Term loans 2,125.97 L: 6 quarterly instalments of 125.00 L at 10.60% (750.00); 12 of 103.32 L at 8.75% (1,239.84); 16 of 8.51 L at 8.60% (136.16) (Note 15(b) p.130). Wall: 809.97 L within 12 months; 1,316.00 L at 1-3 years. Note 32 shows nothing beyond 3 years although the 16-quarter loan runs 4 years (about 34 L, derived). Working capital 359.79 L; supplier-finance bank loans 747.56 L (Note 15(e)); PWPL loan 423.39 L on demand. No pledge by promoters disclosed. Covenants (Note 33(b) p.145): net worth over Rs 220 cr; outside liabilities under 1.00x net worth; debt under 2.0x EBITDA; DSCR over 1.25. FY26 year-end: 19,657.44 / 28,903.17 = 0.68x; debt / EBITDA 0.94x; DSCR 7.59x (Note 43). Opening total liabilities / net worth was 28,479.63 / 24,575.11 = 1.16x (derived, face totals). The covenant definition is not given and quarter-end FY26 data is NOT FOUND, so the statement "complied throughout the reporting period" cannot be tested here.
Finance cost 364.95 L vs 1,109.55 L: on average borrowings of 4,060.59 L that is 9.0%; FY25 on average 5,516.67 L was 20.1% (derived). FY25 cost sat well above coupon rates. [INFERENCE] Part of FY25 finance cost financed trade credit outside the borrowings line.

### 2G Deferred tax
DTL 1,231.11 L (PPE 1,785.80; ECL asset (227.89); payment-basis asset (326.80)). Effective rate 24.17% vs statutory 25.168% (Section 115BAA adopted). Items: remeasurement credit (69.29) L and prior-period (44.09) L. Note 18 movement to P&L (115.42) vs Note 30 (120.25): gap 4.83 L is the OCI tax (p.131, p.140). MAT credit of 472.83 L was used or written off in FY25.

### 2H Exceptional items, ESOP, leases, post balance sheet
Exceptional: 520.00 L ex-gratia in FY26 (Note 29(d) p.139); pattern from the 10-year table: 58.15 L gain FY17, (908.01) L FY21, nil FY22-FY25, (520.00) L FY26 (p.23). No goodwill. No ESOP or dilution (CG p.53). Leases: see 2A. Post balance sheet: only the dividend (Note 45); SPA (9 Jul 2026) is after board approval of the accounts (29 May 2026) and sits in the DR (p.29). The April 2026 licence refusal and export order cancellation, if they occurred before 29 May 2026, are NOT FOUND in the notes or the DR.

### Cross-reference to Phase 1 and reconciliation
The triple-pass score is 5/10. Reconciled Phase 2 verdict: Watch, with the accounting component set to 4/10 for Phase 8. Reason for the lower number: Phase 1 adds the qualified IFC opinion on procurement, the whistle-blower complaint and special audit (CARO xi(c)), and the receivable ageing discrepancy. Those facts sit outside the notes, so B02 could not score them. Agreement with B02: no restatement, covenants reported met, thin disclosure.
Kill switch assessment (informational): Based on phases so far, a human reviewer would not stop on the notes alone, because balance sheet items reconcile and covenants are reported met; the pause reason stays in Phase 1.

---
## PHASE 3: FINANCIAL STATEMENTS (cash flow, balance sheet, P&L)

### 3A Cash flow (standalone, L; CFS p.112)
| Metric | FY26 | FY25 | FY24 |
|---|---|---|---|
| PBT | 6,043.17 | 3,754.24 | 4,024.65 |
| Operating profit before WC | 7,352.54 | 6,131.02 | |
| Working capital change | (5,863.23) | 6,834.49 | |
| CFO | (144.14) | 11,861.66 | 7,899.69 |
| PAT | 4,582.51 | 2,855.26 | 2,812.15 |
| CFO / PAT | -0.03x | 4.15x | 2.81x |
| CFO / EBITDA (3,882.18; 5,799.68) | -3.7% | 204.5% | |
| Capex payments | (2,783.15) | (1,305.95) | |
| FCF (CFO less capex) | (2,927.29) | 10,555.71 | |
| Capex / depreciation | 2.38x | 1.14x | |
| M&A | JV 4.90 | nil | |
Three-year cumulative CFO 19,617.21 L vs PAT 10,249.92 L = 1.91x (derived). The flag is FY26 alone: CFO / PAT below 0.7 in the current year, with the prior year inflated.
Financing: net term borrowing +875.97; current borrowings (1,683.73); interest (364.95); dividends (268.81); total (1,441.52). Cash and equivalents 9,309.24 to 5,057.21 L (-45.7%); bank balances 923.48 L.

CFO quality checks:
| Check | Result |
|---|---|
| One-time inflators | Operating profit before WC includes 3,917.80 L non-recurring. If the 3,417.80 L was settled by credit note, profit is non-cash and the payables line (7,464.51) already absorbs it, so CFO is unchanged and the "real" payables paydown is 4,046.71 L [INFERENCE]. If settled in cash, the cash is inside CFO |
| Interest classification | Finance costs 364.95 L are in financing, interest received 236.27 L in investing. On an operating classification CFO would be (144.14) - 364.95 + 236.27 = (272.82) L (derived) |
| Payable stretching | FY25 payables +8,566.41 L (DPO 134 days); FY26 reversed (DPO 88) (BRSR p.79). Unwind, not stretch |
| Inventory run-down | Inventories released 5,048.20 L. Without it CFO would be (5,192.34) L (derived) |
| Accruals | Employee benefits payable 1,248.26 L vs 680.06 L (+83.6%, +568.20 L) (Note 16 p.131) |
| Customer advances | 6,622.26 L (FY25 7,242.69) = 17.1% of revenue. Cash plus bank 5,980.69 L covers 90% of it. Net of advances the company holds -641.57 L (derived) |
Trend: FLAG-CASH stands. Reading A: FY26 CFO is the unwind of FY25 payables and advances; the two-year sum is positive. Reading B: working capital is structurally heavier (receivable days 50 vs 33, finished goods up 88.9%) and cash is largely customer money. Separator: FY27 CFO with payables at about 88 days and advances stable.

### 3B Balance sheet walk (L; BS p.109)
| Line | FY26 | FY25 | Change |
|---|---|---|---|
| PPE | 17,907.14 | 19,059.97 | -6.0% |
| CWIP | 2,639.23 | 284.73 | +826.9% |
| Other non-current (capital advances 821.20 vs 334.61) | 1,037.61 | 557.12 | +86.2% |
| Inventories | 10,301.26 | 15,349.46 | -32.9% |
| Trade receivables (net) | 5,344.57 | 3,807.81 | +40.4% |
| Cash and equivalents | 5,057.21 | 9,309.24 | -45.7% |
| Insurance receivable | 683.59 | nil | new |
| Other current assets (supplier advances 2,115.95) | 3,495.14 | 2,635.64 | +32.6% |
| Total assets | 48,560.61 | 53,054.74 | -8.5% |
| Borrowings | 3,656.71 | 4,464.47 | -18.1% |
| Trade payables | 4,151.63 | 11,654.90 | -64.4% |
| Other current liabilities (customer advances 6,622.26) | 6,699.36 | 7,313.24 | -8.4% |
| Net worth | 28,903.17 | 24,575.11 | +17.6% |

Key ratios (derived unless noted):
| Ratio | FY26 | FY25 |
|---|---|---|
| Debt / equity | 0.13 (Note 43) | 0.18 |
| Net debt / EBITDA | net cash 2,314.50 L (Note 33) | net cash 5,649.78 |
| Current ratio | 1.60 | 1.26 |
| Quick ratio (CA less inventory) / CL | 0.96 | 0.65 |
| Liquid ratio (cash, bank, receivables, loans, insurance) / CL | 0.75 | 0.55 |
| Interest cover, EBIT incl. other income 6,928.12 / 364.95 | 19.0x | 4.4x |
| Interest cover, EBIT ex all other income 2,713.63 / 364.95 | 7.4x | 4.2x |
| ROCE as filed (ex other income) | 8.03% | 14.66% |
| ROCE incl. other income 6,928.12 / 33,790.99 | 20.5% | |
| ROE (Note 43) | 17% | 12% |
| Goodwill / NW | nil | nil |
DuPont (average balances): net margin 11.80% x asset turnover 0.764 x equity multiplier 1.90 = ROE 17.1%. The multiplier of 1.90 comes from customer advances and payables, not bank debt (debt / equity 0.13). On PBT ex-one-offs (2,125.37 L, tax at 25.168%) net margin would be about 4.1% and ROE about 6% (derived). ROE is operational on paper, but non-recurring income, not leverage, lifts it.

### 3C P&L walk (L; p.110)
| Line | FY26 | FY25 | YoY | % of revenue FY26 (FY25) |
|---|---|---|---|---|
| Revenue | 38,834.14 | 41,745.23 | -7.0% | |
| Material cost incl. stock change and purchases | 22,386.49 | 23,888.70 | -6.3% | 57.65% (57.23%) |
| Employee | 6,890.82 | 6,192.83 | +11.3% | 17.74% (14.84%) |
| R&D | 49.71 | 43.86 | +13.3% | 0.13% (0.11%) |
| Other expenses | 5,624.94 | 5,820.16 | -3.4% | 14.48% (13.94%) |
| EBITDA before other income | 3,882.18 | 5,799.68 | -33.1% | 10.0% (13.9%) |
| Other income | 4,214.49 | 211.53 | +1,892% | |
| Depreciation | 1,168.55 | 1,147.42 | +1.8% | |
| Finance cost | 364.95 | 1,109.55 | -67.1% | |
| PBT before exceptional | 6,563.17 | 3,754.24 | +74.8% | |
| Exceptional ex-gratia | (520.00) | nil | | |
| PBT | 6,043.17 | 3,754.24 | +61.0% | |
| Tax | 1,460.66 | 898.98 | | 24.17% (23.95%) |
| PAT | 4,582.51 | 2,855.26 | +60.5% | 11.80% (6.84%) |
Other income = 69.7% of PBT (4,214.49 / 6,043.17); the one-offs alone 64.8%. Margin waterfall, 390 bps EBITDA fall: material cost -42 bps, employee cost -290 bps, R&D -2 bps, other expenses -54 bps (derived). Operating EBIT (ex all other income) fell 41.7%: 4,652.26 L to 2,713.63 L, margin 11.1% to 7.0% (derived). The filed "EBIT +42.4% to Rs 692.8 mn, margin 17.8%" includes Rs 421.4 mn of other income (MD&A p.25; highlights p.21). Basic and diluted EPS are equal at 8.52 (Note 40 p.151). Tax rate is consistent with statutory.
FX loss 591.64 L sits inside other expenses (Note 29 p.138): EBITDA already bears it.
Cross-reference: Phase 2 ECL and revenue-estimate findings feed 3C. Phase 1 IFC qualification applies to the procurement line that sets material cost (22,386.49 L, 57.65% of revenue).
Phase 3 verdict: Red Flag.
Kill switch assessment (informational): Based on phases so far, a human reviewer would have reason to pause, because operating cash flow is negative while reported PAT rises 60.5%, and 64.8% of PBT is non-recurring.

---
## PHASE 4: RISK FACTORS AND MD&A

### 4A Disclosed risks (MD&A section 10, p.26)
| Risk | Real or boilerplate | Evidence |
|---|---|---|
| Safety and process | Real | Katepally four deaths; 5 FY26 fatalities (BRSR p.85); closure order 7 May 2025 |
| Execution and schedule | Real | Defence 9M FY26 revenue 2,477 mn vs 2,901 mn (-14.6%); Q4 677 mn +43.1% (derived from p.12, p.25) |
| Raw material | Partly real | Material cost ratio flat (57.65% vs 57.23%); MD&A cites raw material pressure for the margin drop |
| Regulatory and licensing | Boilerplate in text | Closure order and CFO expiry not named |
| Concentration | Boilerplate | Order book 95% defence; one customer 10% or more, unnamed |
| Technology and qualification | Boilerplate | |
| Working capital | Real, understated | Milestone timing cited; 1,582.37 L over 6 months not cited |
| People | Boilerplate | |
| Cyber | Boilerplate | |

### 4B Missing risks (obvious from Phases 1-3, absent from the risk table)
| # | Missing risk | Evidence | Likely reason for omission |
|---|---|---|---|
| 1 | Procurement control weakness, single approver | Auditor IFC qualification p.103-105; MD&A section 11 says internal control is "commensurate" (p.27) | Auditor finding landed after MD&A drafting; DR p.34 answers it only as a management reply |
| 2 | Whistle-blower complaint and special audit | CARO xi(c) p.108 vs CG p.54 | Complaint not disclosed in governance text |
| 3 | Change of control and promoter exit | SPA p.29; MD&A risk table has no ownership risk and no mention of Apollo | MD&A written from the May investor presentation (p.27 sources) |
| 4 | Dependence on non-recurring income | 3,917.80 L, 64.8% of PBT | Presented as "higher other income" and "favourable mix" (p.4) |
| 5 | FX and unhedged USD liabilities | FX loss 591.64 L; net USD liabilities 17.99 lakh; "no hedging" (CG p.53) | MD&A omits FX entirely |
| 6 | Licence expiry: Peddakandukuru Consent for Operation expires 31 Oct 2026 | BRSR p.94. Peddakandukur supports countermeasures and pyro devices (p.20) | Not mentioned in risk table; renewal NOT FOUND |
| 7 | Insurance recovery | 683.59 L unsettled; 73.79 L unexplained | Treated as settled in tone ("appropriately insured", DR p.29) |
| 8 | Refund exposure on customer advances | Foreign advances 2,546.28 L, +163.2% | Not discussed |
| 9 | Independent director quorum after 31 Jul 2026 resignation | 4 of 9 directors independent after Kumuda Raghavan's exit (p.31, p.38) | Post year-end event |
| 10 | Capital project execution | CWIP 2,639.23 L, commitments 1,708.70 L, no project named | Vision 2030 text is generic |

### 4C MD&A deep dive
Industry claims. Defence production Rs 1.78 lakh crore (+15.6%); exports Rs 38,424 crore (+62.66%) (MD&A p.24, press releases cited p.27). These are sector facts, not company results.
Growth and margin explanations:
| Claim | Test | Result |
|---|---|---|
| Revenue fell "largely linked to stoppage of electric detonator production" (Chairman p.5; MD p.7) | Revenue fell 291.1 mn: Commercial -72 mn (24.7%), Defence -220 mn (75.3%) (p.25) | Contradicted by segment data. The MD&A itself explains the defence fall by timing and FY25 chaff and flare volume (p.25) |
| Margin fall due to "elevated raw-material prices" (MD&A p.25) | Material cost ratio +42 bps; employee cost +290 bps | Not supported; DR p.28 says supplies and prices "were stabilized" |
| "Profitability improved substantially, supported by higher other income and favourable mix" (p.4) | Other income 4,214.49 L carries 64.8% of PBT; EBITDA ex other income fell 33.1% | Other income disclosed, one-off nature not |
| Q4 "momentum" (p.12) | Q4 revenue 892.1 mn, +20.4% YoY, 23.0% of the year; 9M average 997.1 mn per quarter (derived) | YoY true; below the 9M average |
Credit-taking and blaming: external factors (detonator "ban", raw materials, execution timing) get the blame; improvement (EBIT, PAT) is credited to the "operating model" (p.5).

Forward guidance table (filed statements only):
| Claim | Number | Timeframe | Credibility |
|---|---|---|---|
| Order book Rs 15,690 mn, 4.04x FY26 revenue; Defence 95%, Explosives 2%, Services 3% | 15,690 mn | As of May 2026 | Medium: FY25 AR claimed Rs 7,500 mn (1.8x) gave "14-18 months" visibility and "most scheduled for delivery over the next 12 months"; FY26 revenue fell 7.0% |
| Revenue "may remain uneven across quarters" | none | FY27 | Honest, non-numeric |
| Raw material supplies and prices "stabilized ... positive impact in near future" | none | near term | Low: same sentence appears in FY25 DR (FY25 AR p.26) and FY26 DR (p.28), while MD&A reports price pressure |
| Expand defence exports; "advanced negotiations for overseas supply" (FY25 AR) | none | | Low: foreign revenue 5,168.78 L vs 7,848.01 L (-34.1%) (Note 21 p.133); not mentioned in FY26 |
| Capacity for RDX, HMX, TNT, ammonium perchlorate; mines, ammunition, warheads, missile integration, Vision 2030 | none | 2030 | Unquantified |
| Revenue and margin guide (FY26 Rs 500 cr; FY27 Rs 600-700 cr at 15-20%) | n/a | | NOT FOUND IN DOCUMENT in the AR (web leads in the brief, not anchored) |
Segment analysis: Defence and Space 3,154 mn (81%; FY25 3,374 mn); Commercial 729 mn (19%; FY25 801 mn) (p.25). FY25 AR printed 3,380 and 802 mn (FY25 AR p.25), a 6 mn restatement of comparatives not explained. Geography: India 33,665.36 L, abroad 5,168.78 L (13.3%, BRSR p.72). Production: detonators 4.56 mn pieces vs 10.36 mn (-56%); bulk explosives 9,592 t vs 8,557 t (+12.1%) (DR p.28).

### 4D Tone and credibility (1-5)
| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2 | One-off other income called "higher other income"; whistle-blower complaint absent from governance text; licence refusal and export cancellation absent |
| Consistency | 2 | DR vs MD&A on raw materials; letter vs segment data on detonators; MD&A "controls commensurate" vs qualified IFC |
| Specificity | 3 | Order book split, segment revenue and platforms are specific; guidance is not |
| Accountability | 3 | Safety incidents named; ex-gratia booked and shown as exceptional; cause analysis and fatalities mismatch |
| Capital allocation sense | 3 | Debt cut 18%, dividend 0.50/share held; CWIP 2,639.23 L with no named project; 1,000 Cr borrowing power sought against 36.57 Cr debt (Notice p.206, p.214) |
Phase 4 verdict: Watch.
Contradictions vs Phases 1-3: MD&A section 11 (controls) vs Annexure A; letter's "balanced portfolio" vs 81% defence concentration.
Kill switch assessment (informational): Based on phases so far, a human reviewer would not stop on the MD&A alone, because the numbers are disclosed even when the explanations are weak; the pause reason stays in Phase 1.

---
## PHASE 5: CORPORATE GOVERNANCE AND BOARD

### 5A Board composition (p.38-41)
| Director | Role | Other boards | Attendance FY26 | Note |
|---|---|---|---|---|
| Dr. A.N. Gupta, 81 | Promoter, Non-Exec Chairman | 1 (PELNEXT) | 5/5 | Founder; spouse and daughter on board |
| T.V. Chowdary | MD | 4 | 4/5 | 41 years of service; holds 1,57,290 shares (0.29%) (p.69) |
| Y. Durga Prasad Rao | Director Operations | 1 | 3/5 (60%) | Below the 75% flag |
| Dr. Kailash Gupta, 80 | Promoter NED | 1 | 5/5 | Retires by rotation; Item 3 |
| Mrs. Shonika Prasad | Promoter NED | 0 | 5/5 | Trustee of AKS Family Trust and seller under the SPA |
| Dr. N.K. Nanda | Independent | 4 | 5/5 | Audit Committee chair |
| Dr. V.G. Sekaran | Independent | 2 (MTAR listed) | 5/5 | RMC and NRC chair; NRC 1/2 attended |
| Mr. Ch. Seshagiri Rao | Independent | 0 | 5/5 | CA |
| Dr. Kumuda Raghavan | Independent | 0 | 5/5 | Resigned 31 Jul 2026 (personal and health reasons) |
| Lt Gen P.R. Kumar | Independent | 1 (RKEC listed) | 5/5 | |
Flags. (i) No independent director over 10 years. Four of five independents were appointed at the 44th AGM (27 Sep 2024) after four earlier independents left on 12 Aug 2024 (p.50; Note 38 p.147). A fresh independent bench was in place by September 2024, then the Jan 2025 and Apr 2025 fatal accidents followed. Lt Gen Kumar's appointment date: NOT FOUND IN DOCUMENT. (ii) Promoter-family cross-board: Chairman, wife and daughter are 3 of 10 directors; MD sits on PWPL, Octane Chemicals Pvt Ltd and PELNEXT, Global Premier (p.40). Octane Chemicals is not in the related-party list (Note 38); its link to the company, if any, is NOT FOUND. (iii) Attendance under 75%: Y. Durga Prasad Rao 3/5. (iv) No director above 8 seats. (v) After the 31 Jul 2026 resignation, 4 of 9 directors are independent (44%). Where the chairperson is non-executive and promoter-related, the Listing Regulations call for at least half independent; the 3-month fill period ended about 30 Oct 2026; appointment NOT FOUND (AR dated 13 Aug 2026). The CG report says "Reasons for resignation ... Not Applicable" (p.42) though the same report notes the resignation (p.38). (vi) Reg 17(1A): Dr. Kailash Gupta (80) is up for rotation by ordinary resolution (Item 3, p.206); a special resolution for continuing a non-executive director over 75 is not in the notice. The FY25 exchange fine was for the same regulation (p.54). Verify.

### 5B Committees
| Committee | Members | Meetings | Observation |
|---|---|---|---|
| Audit | Nanda (chair), Rao, Kumar, Dr. A.N. Gupta | 4; all 4/4 | Promoter Chairman is a member; 3 independents |
| NRC | Sekaran (chair, 1/2), Rao, Kumar, Dr. Gupta | 2 (May and Aug 2025) | No meeting after August 2025 |
| Stakeholders | Kumar (chair), Rao, Chowdary, Kailash Gupta | | 5 complaints, nil pending |
| CSR | Raghavan (chair), Chowdary, K. Gupta | 2 | Chair resigned; reconstituted 25 Jul 2026 (p.66) |
| Risk | Sekaran (chair), Chowdary (1/2), Rao, CFO | 2 (18 Oct 2025, 12 Feb 2026) | First meeting 5.5 months after Katepally |

### 5C Compensation
| Person | FY26 (L) | FY25 (L) | Change | Ratio to median 5.07 L (as printed) |
|---|---|---|---|---|
| Dr. A.N. Gupta (incl. commission) | 87.60 | 62.12 | +41.0% | 2.05x |
| T.V. Chowdary | 240.89 | 189.31 | +27.3% | 5.64x |
| Y. Durga Prasad Rao | 116.80 | 89.90 | +29.9% | 2.73x |
| CFO B.M. Vijay Kumar | 79.00 | 27.33 (part year, joined Oct 2024) | | 1.85x |
| Company Secretary | 22.51 | 18.96 | +18.7% | 0.53x |
Source: Annexure 10 p.69. The printed ratios do not equal remuneration / median 5.07 L (87.60 / 5.07 = 17.3x; 240.89 / 5.07 = 47.5x); the ratio column is unreliable and the true CEO-to-median multiple is 47.5x (derived). Executive commissions total 95.40 L (MD 63.60, Dir Ops 31.80) and the Chairman's commission is 1% of net profits (p.46). These are profit-linked, and profit includes 3,917.80 L of non-recurring income. The commission rate on executives is not given (NOT FOUND). KMP remuneration 445.29 L is 7.4% of PBT (derived), within the Section 197 opinion at p.103. Promoter family payroll: Chairman 87.60 L plus sitting fees 2.54 L to wife and daughter. No ESOP.

### 5D Shareholding (CG p.52; Note 14 p.129)
| Holder | Mar-26 | % |
|---|---|---|
| Promoter (AKS Family Trust) | 2,22,21,735 | 41.33 |
| Mutual funds (HDFC Defence 9.09%) | 48,94,455 | 9.10 |
| FPIs | 6,33,742 | 1.18 |
| Resident individuals | 1,95,13,477 | 36.3 |
| Bodies corporate | 38,91,317 | 7.24 |
| IEPF | 5,41,941 | 1.01 |
Shareholders 92,900 vs 83,951 vs 24,933 (FY24) (p.23). Pledge: NOT FOUND IN DOCUMENT; the SEBI exemption order says the beneficial interest will not be encumbered (order p.5). Promoter movement in FY26: none by number (inter-se to trust). After year-end, the trust agreed to sell the whole 41.33% at about Rs 697.5 per share (1,550 Cr / 2,22,21,735, derived) with an open offer at Rs 698. Whether the sale was planned when the 29 Sep 2025 trust deed and the 29 Oct 2025 exemption application were made is NOT FOUND; the stated grounds were succession and "no change in control". FLAG-PROMOTER-PRELIM: this is a promoter exit through a control sale, not a pledge pattern; full verdict comes from B08.

### 5E Governance red-flag checklist
| Check | Result | Anchor |
|---|---|---|
| Whistle-blower complaints | One per auditor; nil per governance report | p.108 vs p.54 |
| SEBI actions | Exemption order only; exchange fine FY25 | p.41, p.54 |
| RPT committee | Audit committee approves; omnibus approval | p.35 |
| Auditor fee ratio | 34.1% non-audit | Note 29(a) |
| CSR compliance | Met (59.38 vs 58.32) | p.66-68 |
| Section 143(12) fraud | None | DR p.34 |
| Material subsidiary auditor | None material; other auditors for two small subsidiaries | p.55, p.157 |
| Regulatory fines | TGPCB Rs 6,75,000 | p.78 |
| Grievance mechanism | No web mechanism for employees and workers | p.75 |
| Workforce | 855 permanent per Annexure 10, 844 per BRSR; plus 508 non-permanent workers (BRSR p.72): 1,352 people in total | p.69, p.72 |
Phase 5 verdict: Red Flag.
Kill switch assessment (informational): Based on phases so far, a human reviewer would have reason to pause, because the governance report and the auditor disagree on a whistle-blower complaint, the independent bench was rebuilt in 2024 and has since shrunk to 44%, and the promoter family plans to exit.

---
## PHASE 6: CHAIRMAN'S LETTER AND FRONT MATTER (read last)

### 6A Narrative vs reality
| Claim | Page | Test | Mark |
|---|---|---|---|
| "stronger bottom-line performance ... resilience of our operating model" | p.5 | PAT +60.5%, but operating EBITDA -33.1%, CFO negative, 64.8% of PBT non-recurring | Not supported |
| Revenue fall "largely linked to stoppage of electric detonator production" | p.5, p.7 | 24.7% of the decline is Commercial | Not supported |
| "highest-ever order book Rs 15,690 mn, 4.04x" | p.6 | Arithmetic ties; date is May 2026, not year-end | Supported |
| "Defence and Space 81% of revenue" | p.4 | 81.22% BRSR; 3,154 / 3,883 | Supported |
| "current liabilities reduced to Rs 1,609.4 mn" | p.8 | 16,093.65 L vs 25,314.90 L, because payables fell 7,503 L | Supported, with the cause unstated |
| "Cash profit improved to Rs 575.1 mn" | p.5 | PAT 458.3 + depreciation 116.9; CFO negative | Misleading |
| "safety ... uncompromising priority" | p.5 | LTIFR employees 1.73 vs 0, workers 3.27 vs 0.34; fatalities 5 vs 1 (BRSR p.85) | Supported as intent, not as results |
| "Raw material supplies and prices were stabilized" | p.28 | MD&A p.25 cites elevated prices | Not supported |

### 6B Strategic priorities
Stated: execute order book, safety, capacity utilisation, high-explosive raw materials, defence exports, missile integration, strategic partners (p.8). Specific enough: order book split yes; priorities no (no capacity, capex amount or return). Capital allocated: CWIP 2,639.23 L, commitments 1,708.70 L, capital advances 821.20 L; no project named. Execution evidence: new mines (Ulka, Viraj), canopy severance system "almost completed", loitering munitions entered (DR p.30); no revenue or order for these in the notes.

### 6C Metrics showcased vs absent
Showcased: EBIT, PAT, cash profit, order book, other equity, current ratio. Absent: operating cash flow, EBITDA ex other income in the letters (it appears only in MD&A p.25), receivable ageing, supplier settlement, IFC qualification, promoter exit price effect, segment profit, customer concentration.

### 6D Tone and drift vs FY25 AR
FY25 AR: "Strong cash flows have fortified our balance sheet", "order book Rs 750 crore ... 14-18 months" visibility, "advanced negotiations for overseas supply contracts", "order book dominated by high-margin defence contracts, 81%" (FY25 AR p.8). FY26 AR: safety replaces growth as the lead theme; order book doubled in rupees (Rs 7,500 mn to Rs 15,690 mn) and rose from 81% to 95% defence; cash flow language is gone; export language narrows to a capability claim.

### 6E Quiet Abandonment Check
| # | Opening claim | Where it should appear | Class | Materiality |
|---|---|---|---|---|
| 1 | FY25 AR: "advanced negotiations for overseas supply contracts ... diversify revenue" (FY25 AR p.8). FY26 MD: "expand defence exports" (p.8) | Geography note and segment: foreign revenue fell 34.1% (5,168.78 L vs 7,848.01 L, Note 21 p.133); no export order or contract mentioned in FY26 | (b) silent drop | Moderate; ties to the cancelled export order (outside AR) |
| 2 | Chairman: detonator stoppage is the cause of lower revenue (p.5) | Segment results: Commercial -72 mn vs Defence -220 mn (p.25); MD&A attributes defence fall to timing | (a) implicit retraction | Moderate: the Katepally closure effect on defence deliveries is never quantified |
| 3 | Chairman and MD: safety systems "reinforced" (p.5, p.7) | BRSR: closure order 7 May 2025, Rs 6.75 lakh compensation, restart date absent; fatalities 5 in FY26; no summary of PESO licence status | (c) hedged retreat | High: the restart date and licence status drive FY27 defence revenue |
| 4 | Chairman: Peddakandukuru and Katepally incidents (p.5) | Notes and DR describe only Katepally; the Peddakandukuru fire (4 Jan 2025) loss and claim are not tracked in FY26 notes | (b) silent drop | Low to moderate |
| 5 | MD&A section 11: internal controls "commensurate" (p.27) | Annexure A: qualified, procurement controls not commensurate (p.103) | (a) implicit retraction | High |
| 6 | "Profit improved on favourable mix" (p.4) | Note 22: 3,417.80 L settlement and 500 L reversal | (c) hedged retreat | High |
Materiality: items 3, 5, 6 change the thesis (operating base, controls, earnings quality). Items 1, 2, 4 are narrative drift.
Phase 6 verdict: Watch.

---
## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION
| Strategy | Call | Top reasons |
|---|---|---|
| Value + Quality | FAIL | (1) ROCE 8.03% ex other income vs 14.66%; (2) accounting 4/10 and qualified IFC; (3) CFO negative |
| GARP | WATCHLIST | See below |
| Turnaround | WATCHLIST | See below |
| Capex-Led Growth | WATCHLIST | Capex 2,783.15 L = 2.38x depreciation; CWIP 2,639.23 L; commitments 1,708.70 L; but no project, capacity or return disclosed; borrowing power of Rs 1,000 Cr sought |
| Cash Flow Compounder | FAIL | CFO (144.14) L; FCF (2,927.29) L; the 3-year sum is positive only because of FY24-FY25 advances and payables |
| Contrarian | FAIL | Open offer at Rs 698 means the price already carries a control premium; nothing is unloved |
| Insider Confidence | FAIL | Promoter family agrees to sell 41.33%; MD holds 0.29%; no insider buying disclosed |
| Guidance Divergence | WATCHLIST | AR carries no numeric guide (NOT FOUND); FY25 visibility claim vs FY26 revenue -7.0%; web leads (FY26 guide Rs 500 cr vs Rs 388 cr delivered) are unanchored |

GARP, fullest reasoning. Growth evidence: order book 15,690 mn = 4.04x revenue, 95% defence; defence Q4 +43.1% YoY; the sector tailwind is filed. Quality evidence against: PAT growth of 60.5% comes from other income and a lower revenue deduction rate; underlying PBT ex-one-offs 2,125.37 L is 43.4% below FY25's 3,754.24 L (derived: 2,125.37 / 3,754.24 - 1 = -43.4%). Price context from filed deal terms only: Rs 698 x 5,37,61,195 shares = Rs 3,752.6 Cr (derived), 82x reported PAT 45.83 Cr and about 236x PAT on 2,125.37 L PBT at 25.168% tax (about Rs 15.9 Cr, derived). The growth needed to justify that multiple is not in the filed numbers. This is context for stage 11, not a valuation. Verdict: the growth leg is plausible, the earnings leg is unproven, the price leg is a takeover price.
Turnaround, fullest reasoning. The transition (commercial to defence) is real in mix: 81% defence of revenue, 95% of order book vs 81% a year earlier. The margin leg has gone the other way: EBITDA margin 21.5% (FY24), 13.9% (FY25), 10.0% (FY26) (p.23). Recovery evidence: Q4 defence revenue +43.1%, WIP converted from 6,024.82 L to 2,388.07 L, finished goods 1,229.36 L waiting to ship, debt cut 18.1%. Against: IFC qualified, accident aftermath, FX loss, employee cost +11.3% on lower revenue. What would separate recovery from drift: EBITDA ex other income margin back above the FY25 13.9% level by H2 FY27 with positive CFO.
Best fit: Turnaround, on WATCHLIST. No strategy passes on the FY26 filed evidence.
Phase 7 kill switch (informational): a reviewer would not stop here; the cell is WATCH, not exit.

---
## PHASE 8: FINAL VERDICT DASHBOARD

### Company snapshot (standalone, L unless stated)
| Item | Value |
|---|---|
| Revenue | 38,834.14 (-7.0%) |
| EBITDA before other income | 3,882.18 (10.0%) |
| Other income | 4,214.49 |
| PBT / PAT | 6,043.17 / 4,582.51 |
| CFO | (144.14) |
| Net worth | 28,903.17 |
| Borrowings / net cash | 3,656.71 / 2,314.50 |
| Order book (May 2026) | Rs 15,690 mn |
| Control | Promoter 41.33% under sale to Apollo (about Rs 1,550 Cr), open offer Rs 698 |

### Phase-wise verdicts
| Phase | Verdict |
|---|---|
| 1 Auditor and CARO | Red Flag |
| 2 Notes | Watch |
| 3 Financials | Red Flag |
| 4 Risk and MD&A | Watch |
| 5 Governance | Red Flag |
| 6 Front matter | Watch |
| 7 Strategy | Turnaround, Watchlist |

### Overall quality score: 4.5 / 10
| Component (25% each) | Score | Basis |
|---|---|---|
| Governance | 4 | Qualified IFC on procurement; whistle-blower inconsistency; independents 44% after resignation; promoter exit. Positives: audit committee 4/4, CSR compliance, no loans to promoters, small RPT |
| Accounting quality | 4 | Triple-pass 5, lowered for Phase 1 findings (see Phase 2) |
| Balance sheet | 7 | D/E 0.13, net cash 2,314.50 L, current ratio 1.60, covenants reported met; offset by customer advances 6,622.26 L, receivable ageing |
| Earnings quality | 3 | 64.8% of PBT non-recurring; operating EBIT -41.7%; CFO negative; revenue estimate softer |

### Top 3 strengths
1. Order book Rs 15,690 mn = 4.04x revenue, 95% defence (MD&A p.25), with platform positions at 100% of propellant requirement on MRSAM, LRSAM, Astra (p.13-14).
2. Low leverage: debt 3,656.71 L, D/E 0.13, net cash 2,314.50 L (Note 33 p.144), no restatement found, no promoter loans.
3. Disclosure of a hard fact set that allows testing: segment revenue split, order book split, safety statistics, TGPCB fine, auditor's own IFC finding printed in full.

### Top 3 red flags
1. Qualified IFC opinion: procurement approvals concentrated in one person (Annexure A p.103-105), plus a whistle-blower complaint and special audit (CARO xi(c) p.108) that the governance report denies (p.54).
2. Earnings quality: 3,917.80 L of prior-year supplier discount and provision reversal = 64.8% of PBT; operating EBIT -41.7%; CFO (144.14) L.
3. Control change with weak minority protection signals: the trust created on 29 Sep 2025 for "succession" agreed to sell all 41.33% on 9 Jul 2026; independent directors 44% after the 31 Jul 2026 resignation; licence and consent status unverified (Peddakandukuru Consent expires 31 Oct 2026).

### Key monitorables for the next quarter
| Metric | Threshold | Where | Why |
|---|---|---|---|
| Operating cash flow | Positive for H1 FY27; CFO / EBITDA above 0.7 | Half-year cash flow, results filing | FY26 CFO (144.14) L |
| Other income as % of PBT | Below 20% | Quarterly results, Note 22 equivalent | FY26 69.7% |
| Settlement terms of the 3,417.80 L discount | Cash or credit note named; supplier named | Exchange filing, Q3 concall | Separates Reading A from B |
| Receivables over 1 year | Below 888 L (FY25 level 887.36 L); over 6 months below 20% of gross | Annual Note 11 ageing; half-year trade receivable disclosure | FY26 1,186.73 L and 25.3% |
| IFC opinion | Unmodified with two-level procurement approval | FY27 auditor Annexure A | FY26 qualified |
| Whistle-blower complaint subject | Disclosed and closed | Board, Audit Committee minutes, exchange filing | CARO vs CG mismatch |
| Peddakandukuru and Katepally licences | Consent renewal after 31 Oct 2026; PESO licence valid | TGPCB portal, exchange filings | Defence products made at both plants |
| Independent directors | At least 5 of 9 (half) | Reg 17 compliance filing | 4 of 9 after 31 Jul 2026 |
| Apollo open offer and CCI approval | Completion date; board changes; RPT with Apollo group | Letter of offer, SAST filings | 41.33% control sale |
| Defence quarterly revenue | At least 700 mn per quarter | Quarterly segment disclosure | Q4 FY26 677 mn; order book conversion |
| EBITDA margin ex other income | At least 13.9% (FY25 level) | Quarterly results | FY26 10.0% |
| Foreign customer advances | Below 2,546.28 L; no refunds | Next balance sheet note | Export cancellation, April 2026 |
| Net unhedged USD | Below 17.99 lakh USD liabilities, or hedged | Note 32(B) equivalent | FX loss 591.64 L |

### One-line verdict
Best-fit strategy is Turnaround on WATCHLIST: the defence order book (Rs 15,690 mn, 4.04x revenue) is real, but FY26 profit is 64.8% non-recurring, operating cash flow is (144.14) L and the auditor qualified procurement controls.

---
## ANALYST LINKAGE NOTE [INFERENCE]
One chain a downstream stage should test: whistle-blower complaint and special audit (CARO xi(c)) -> auditor's procurement-control material weakness (Annexure A) -> 3,417.80 L settlement with a supplier for prior-year materials (Note 22) -> payables from 11,654.90 L to 4,151.63 L and supplier advances +98.6% -> operating cash flow (144.14) L. The AR links only the first two steps (the auditor says the complaint's matters produced the IFC deficiencies). The later steps are linked by proximity, not by filing. If the 3,417.80 L (11.3% of FY25 purchases of 30,197.68 L, derived) had been booked in FY25, FY25 EBITDA would have been about 9,217.48 L, a 22.1% margin, close to FY24's 21.5%; that fits a pricing correction for FY25 purchases (Reading B) but the filing does not state it.

```yaml
stage: B03-ardeep
company: "PREMEXPLN"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "B00: shareholding folder empty at collection (repaired at /step1 via NSE XBRL Sep 2026 and screener capture, with limits); not an AR input"
  - "B00: screener P&L/Quarters/Balance Sheet/Cash Flow sheets empty; Data_Sheet carries the series"
  - "B00: Q2 FY27 concall transcript ABSENT (call held 13 Nov 2026); freshness pair RESULTS to CONCALL FAIL"
  - "B00: no research folder content; no broker notes"
  - "B00: BSE API 403, announcements from NSE; nine open-offer .zip files not opened; Reg 29(1) acquirer name illegible in OCR"
  - "B00: results PDFs are OCR scans; check load-bearing figures on the PDF page. The AR is a text PDF and read cleanly"
  - "B00: BDL peer transcripts absent; 8 of 12 peer transcripts present"
  - "AR: NOT FOUND IN DOCUMENT: segment profit or result split (single segment, Note 2.2 p.113; consolidated Note 35 p.199); needed to separate the Defence/strategic 38x and Specialty chemicals 35x readings"
  - "AR: NOT FOUND IN DOCUMENT: supplier name, date, terms and cash or credit-note settlement of the 3,417.80 L discount; subject of the CARO xi(c) whistle-blower complaint; Rs 18.9 cr export order cancellation and April 2026 licence refusal; PESO licence suspension and restoration; Katepally restart date; Peddakandukuru Consent renewal after 31 Oct 2026; Apollo SPA terms, non-compete and board changes; promoter pledge; name of the 10%-customer; ECL matrix; commission rate on executive pay; Lt Gen P R Kumar appointment date; replacement for the 31 Jul 2026 independent director resignation; Octane Chemicals link to the company"
flags:
  - {type: FLAG-CASH, reason: "CFO (144.14) L vs PAT 4,582.51 L (CFS p.112, INR lakhs); FY25 CFO 11,861.66 L, FY24 7,899.69 L, so 3-year CFO/PAT 1.91x; FY26 working capital absorbed 5,863.23 L; receivables over 1 year 1,186.73 L vs 887.36 L (+33.7%) and over 6 months 25.3% of gross vs 20.5% (Note 11 p.127-128)"}
  - {type: FLAG-EARNINGS-QUALITY, reason: "3,917.80 L (3,417.80 L prior-year supplier discount, Note 22 p.133, plus 500.00 L provision reversal, Note 29(c) p.139) = 64.8% of PBT 6,043.17 L; operating EBIT ex all other income 2,713.63 L vs 4,652.26 L (-41.7%, derived)"}
  - {type: FLAG-ICFR-QUALIFIED, reason: "Auditor qualified IFC opinion (standalone p.103-105, consolidated p.159-160): procurement approvals concentrated with a single authorised individual; CARO xi(c) p.108 records one whistle-blower complaint and a special audit, while CG report p.54 says no complaint received"}
  - {type: FLAG-PROMOTER-PRELIM, reason: "Promoter holding 41.33% moved to AKS Family Trust w.e.f. 18 Feb 2026 under SEBI exemption order WTM/KCV/CFD/18/2025-26 dated 8 Jan 2026 (CG p.41) for stated succession reasons; trustees agreed on 9 Jul 2026 to sell all 2,22,21,735 shares to Apollo Micro Systems for about Rs 1,550 Cr (DR p.29). No pledge data in the AR. Full promoter verdict from B08"}
phase_verdicts: {p1: "Red Flag", p2: "Watch", p3: "Red Flag", p4: "Watch", p5: "Red Flag", p6: "Watch", p7_best_fit: "Turnaround (WATCHLIST); no strategy passes"}
overall_quality: 4.5
quality_components: {governance: 4, accounting: 4, balance_sheet: 7, earnings: 3}
kill_switch_notes:
  - "P1: reviewer would have reason to pause: qualified IFC over procurement, whistle-blower complaint plus special audit (p.103-108)"
  - "P2: reviewer would not stop on the notes alone; balance sheet reconciles and covenants reported met; pause reason sits in Phase 1"
  - "P3: reviewer would have reason to pause: CFO (144.14) L against PAT 4,582.51 L, 64.8% of PBT non-recurring"
  - "P4: reviewer would not stop on MD&A alone; weak explanations, numbers disclosed"
  - "P5: reviewer would have reason to pause: CARO vs governance report mismatch on whistle-blower, independent directors 4 of 9 after 31 Jul 2026, promoter family exit"
triple_pass_verification:
  verified: 14
  discrepancies:
    - {finding_rank: 3, triple_pass_value: "over-1-year receivables 887.36 L (FY25) to 888.35 L (FY26), nothing collected net", ar_value: "FY26 over-1-year = 298.38 + 556.28 + 332.07 = 1,186.73 L (+299.37 L, +33.7% vs FY25 887.36 L); 888.35 L is the over-2-year sum only", note_ref: "Note 11(c),(d), p.127-128 (INR lakhs)"}
missing_risks:
  - "Procurement control weakness with single approver; MD&A calls controls commensurate (Annexure A p.103-105 vs MD&A p.27)"
  - "Whistle-blower complaint and special audit absent from governance report (CARO xi(c) p.108 vs CG p.54)"
  - "Change of control and promoter exit absent from MD&A risk table (SPA DR p.29)"
  - "Dependence on non-recurring other income 3,917.80 L, 64.8% of PBT (Note 22 p.133)"
  - "FX loss 591.64 L and unhedged USD liabilities, no hedging, absent from MD&A (Note 29 p.138; CG p.53)"
  - "Peddakandukuru Consent for Operation expires 31 Oct 2026, renewal not found (BRSR p.94)"
  - "Insurance recovery 683.59 L unsettled, 73.79 L unexplained (Note 7(ii) p.125)"
  - "Refund exposure on foreign customer advances 2,546.28 L (Note 32(B) p.143)"
  - "Independent directors 4 of 9 after 31 Jul 2026 resignation (DR p.31; CG p.38)"
  - "Capex 2,783.15 L and CWIP 2,639.23 L with no named project (CFS p.112; Note 3 p.123)"
guidance_table:
  - {claim: "Order book Rs 15,690 mn, 4.04x FY26 revenue; Defence 95%, Explosives 2%, Services 3%", number: "Rs 15,690 mn", timeframe: "as of May 2026", credibility: "Medium: FY25 AR claimed Rs 7,500 mn gave 14-18 months visibility; FY26 revenue fell 7.0%"}
  - {claim: "Revenue may remain uneven across quarters", number: "none", timeframe: "FY27", credibility: "Honest, non-numeric"}
  - {claim: "Raw material supplies and prices stabilized, positive impact in near future", number: "none", timeframe: "near term", credibility: "Low: same sentence in FY25 and FY26 Directors' Reports; MD&A reports price pressure"}
  - {claim: "Defence exports expansion; FY25 AR advanced negotiations for overseas supply", number: "none", timeframe: "n/a", credibility: "Low: foreign revenue 5,168.78 L vs 7,848.01 L (-34.1%)"}
  - {claim: "Capacity for RDX, HMX, TNT, AP; mines, ammunition, warheads, missile integration; Vision 2030", number: "none", timeframe: "2030", credibility: "Unquantified"}
  - {claim: "Revenue and margin guide (FY26 Rs 500 cr; FY27 Rs 600-700 cr at 15-20%)", number: "NOT FOUND IN DOCUMENT", timeframe: "FY26, FY27", credibility: "Not in the AR; web leads only"}
monitorables:
  - {metric: "Operating cash flow", threshold: "positive for H1 FY27; CFO/EBITDA above 0.7", where: "half-year cash flow in results filing", why: "FY26 CFO (144.14) L"}
  - {metric: "Other income as % of PBT", threshold: "below 20%", where: "quarterly results; other income note", why: "FY26 69.7%"}
  - {metric: "Settlement terms of 3,417.80 L supplier discount", threshold: "supplier named; cash or credit note stated", where: "exchange filing; Q3 concall", why: "separates one-off true-up from FY25 cost correction"}
  - {metric: "Receivables over 1 year and over 6 months", threshold: "over 1 year below 888 L; over 6 months below 20% of gross", where: "Note 11 ageing in FY27 AR", why: "FY26 1,186.73 L and 25.3%"}
  - {metric: "Auditor IFC opinion", threshold: "unmodified; two-level procurement approval", where: "FY27 auditor Annexure A", why: "FY26 qualified"}
  - {metric: "Whistle-blower complaint subject and outcome", threshold: "disclosed and closed", where: "audit committee, exchange filings", why: "CARO vs CG mismatch"}
  - {metric: "Peddakandukuru and Katepally licences", threshold: "consent renewed after 31 Oct 2026; PESO licence valid", where: "TGPCB portal; exchange filings", why: "defence products made at both plants"}
  - {metric: "Independent directors", threshold: "at least half of board", where: "Reg 17 compliance filing", why: "4 of 9 after 31 Jul 2026"}
  - {metric: "Apollo open offer and CCI approval", threshold: "completion date; board changes; related-party terms", where: "letter of offer; SAST filings", why: "41.33% control sale"}
  - {metric: "Defence quarterly revenue", threshold: "at least Rs 700 mn per quarter", where: "quarterly segment disclosure", why: "Q4 FY26 Rs 677 mn; order book conversion"}
  - {metric: "EBITDA margin before other income", threshold: "at least 13.9%", where: "quarterly results", why: "FY26 10.0%"}
  - {metric: "Foreign customer advances", threshold: "below 2,546.28 L; no refunds", where: "next balance sheet note", why: "export cancellation, April 2026"}
ar_new_downstream_entities:
  - {name: "Apollo Micro Systems Limited", where_in_ar: "Chairman's letter p.6; Directors' Report section 8 p.29 (SPA 9 Jul 2026, 22221735 shares, about Rs 1,550 Cr, open offer Rs 698 for 26%)", entity_type: "acquirer, prospective controlling shareholder"}
  - {name: "AKS Family Trust", where_in_ar: "CG report p.41 footnote; Note 14 p.129; Note 38 p.147", entity_type: "promoter holding trust and SPA seller (first appears as promoter in this AR)"}
  - {name: "Beerla Foundation", where_in_ar: "CSR report p.67 (CSR Reg 00107631, 15.00 L)", entity_type: "CSR implementing agency"}
  - {name: "Sathwik Rural and Youth Integrated Association", where_in_ar: "CSR report p.67 (CSR Reg 00010965, 30.00 L)", entity_type: "CSR implementing agency"}
  - {name: "Astramile Aerospace Private Limited", where_in_ar: "CG report p.40 (Dr. V.G. Sekaran directorship)", entity_type: "independent director's other board"}
strengths_top3:
  - "Order book Rs 15,690 mn = 4.04x FY26 revenue, 95% defence (MD&A p.25); 100% of propellant requirement on MRSAM, LRSAM, Astra (p.13-14)"
  - "Low leverage: debt 3,656.71 L, D/E 0.13, net cash 2,314.50 L (Note 33 p.144); no restatement; no promoter loans"
  - "Testable disclosure: segment revenue split, order book split, safety statistics, TGPCB fine and the auditor's IFC finding all printed"
red_flags_top3:
  - "Qualified IFC opinion on procurement (single approver) plus whistle-blower complaint and special audit that the governance report denies (p.103-105, p.108, p.54)"
  - "3,917.80 L non-recurring items = 64.8% of PBT; operating EBIT -41.7%; CFO (144.14) L (Note 22 p.133; CFS p.112)"
  - "Trust formed for succession on 29 Sep 2025 agreed to sell all 41.33% on 9 Jul 2026; independent directors 4 of 9 after 31 Jul 2026; licence and consent status unverified (p.29, p.41, p.94)"
best_fit_strategy: "Turnaround (WATCHLIST)"
one_line_verdict: "Turnaround on WATCHLIST: the defence order book (Rs 15,690 mn, 4.04x revenue) is real, but FY26 profit is 64.8% non-recurring, operating cash flow is (144.14) L and the auditor qualified procurement controls."
analyst_note: "Units: statements INR lakhs, MD&A Rs million; stage 10 converts once. Largest new fact vs B02: the auditor qualified IFC over procurement (single approver), plus CARO xi(c) whistle-blower complaint and special audit, which CG p.54 denies. B02 rank 3 over-1-year receivables is 1,186.73 L (+33.7%), not 888.35 L. Sector-cap: revenue 81/19 and order book 95/2/3 favour Defence/strategic 38x; segment profit NOT FOUND, so the earnings-based separator stays open for B04. SEBI exemption order text is already in inputs/announcements/20260220-61. Linkage [INFERENCE]: complaint -> procurement weakness -> 3,417.80 L supplier settlement -> payables swing; AR links only the first two."
```
