# STAGE 3 AR DEEP DIVE (BACKWARD READ): QLL (Qualitek Labs Ltd), run 2026-11-15

Model: claude-sonnet-5-5. Document: inputs/annual-report/Annual_Report_2026.txt (FY2025-26 AR, 191 pp). Support: Annual_Report_2025.txt, Qualitek_Final_Prospectus_Jan2024.txt, 58 BSE filings, three results filings, two investor presentations.

Conventions
- Unit: INR Lakh on the face of every AR, results and prospectus table (100 Lakh = 1 Cr). The investor presentation and the 20 May 2026 MD&A filing print INR Crore; those anchors say "Cr". Nothing is converted silently. "Derived" = arithmetic on filed figures.
- "p.N" = the "[page N]" marker in the .txt (PDF page; printed AR page = N minus 5 for the AR body). Stage 2 used the same marker numbering.
- Framework: Indian GAAP (AS), not Ind AS (C-Note 2, p.106). No ECL matrix, ROU asset, fair-value hierarchy or ESOP note exists. These are NOT FOUND IN DOCUMENT, not omissions by this stage.
- Anchor key: C-Note = consolidated note, S-Note = standalone note, CARO = auditor annexure A.
- Verdict labels use GREEN / YELLOW / RED in place of colour icons. Kill-switch lines are informational only; the run continues.

---------------------------------------------------------------------

## 0. FIRST-PRIORITY CHECK: THE FOUR LOAD-BEARING FACTS (companies/QLL.md, memory, unanchored)

| # | Memory claim | What the filings show | Verdict |
|---|---|---|---|
| 1 | FY27 guidance 35-40% revenue growth and 15-17% PAT margin; H1 FY27 +33.3% revenue, 9.1% PAT margin; H1 FY27 PAT Rs 6.60 cr vs Rs 9.83 cr in H2 FY26 | Revenue and PAT confirmed. H1 FY27 revenue 7226.65 Lakh (results p.11) vs H1 FY26 5,424.38 (FY26 results filing 20260520-dc0311a3 p.5) = +33.2% derived (the H1 FY27 filing's OCR text reads the base as 5421.38, which gives 33.3%). H1 FY27 PAT 660.01 = 9.13% of revenue (derived). H2 FY26 PAT 983.21 (20260520-dc0311a3 p.5). **The 15-17% PAT margin is the May 2026 text only** (MD&A filing 20260520-78cbc582 p.3 and presentation p.25). **The AR (dated 29 Aug 2026) says PAT margin 14-15%** (Chairman letter p.23; MD&A Outlook p.73). EBITDA margin: 25-27% (MD&A filing p.3, AR p.23, p.73) but 25-26% in the presentation p.25. So the PAT guide was lowered by 1 to 2 points between May and August 2026 with no acknowledgement. Memory is right on the figure and wrong on the date: it is the pre-AR figure. | CONFIRMED, with a correction |
| 2 | H1 FY27 standalone CFO Rs 2.48 cr vs PBT Rs 6.36 cr; receivables up Rs 8.78 cr; short-term borrowings Rs 31.75 cr vs Rs 16.24 cr; FY26 receivables Rs 42.14 cr on revenue Rs 124.52 cr | Standalone H1 FY27 CFO 248.20, PBT 635.50 (39.1% conversion, derived), receivables increase 878.06 (results 20261113-190e3152 pp.7-8). Standalone short-term borrowings 3174.91 vs 1623.61 at 31 Mar 2026 (p.6). FY26 receivables 4214.04 consolidated (BS p.102; C-Note 15 p.126) on revenue 12451.81 (P&L p.103). The 31.75 and 16.24 figures are STANDALONE; consolidated short-term borrowings are 3285.40 at 31 Mar 2026 (BS p.102) and 4854.48 at 30 Sep 2026 (results p.12). Consolidated H1 FY27 CFO is 359.17 vs PBT 855.11 (42.0%, p.14). | CONFIRMED |
| 3 | PAT to owners Rs 6.30 cr vs total PAT Rs 14.60 cr; EPS 13.38 does not reconcile; verify NCI, stakes, goodwill Rs 78.12 cr | NCI at 31 Mar 2026 is nil (BS p.102; C-Note 38 p.141). PAT total 1460.15; minority share 97.92; **owners 1362.22; EPS 12.49** (AR P&L p.103). **6.30 is NOT FOUND IN DOCUMENT.** **EPS 13.38 is a filed figure**: the audited results of 20 May 2026 show all 1460.15 attributable to owners, minority nil, EPS 13.38 (results 20260520-dc0311a3 p.5), and the presentation prints Rs 13.4 (p.9). So the same audited year carries two EPS figures: 13.38 in the results filing and 12.49 in the AR statements (same auditor, same 20 May 2026 sign-off date). The H1 FY27 filing prints FY26 EPS as 12.49 (p.11), which suggests the AR figure is the one the company now treats as final. Stakes: ITCPL 100% from 10 Sep 2025 (Board report pp.49-50), QTIPL 100% (cost 500.00), LabOps Global 74% (740 shares for Rs 7,400, from 23 May 2025) (Board report p.50). Goodwill 7811.56 = Rs 78.12 cr (BS p.102). | CONFIRMED; 13.38 vs 12.49 is a filing-versus-AR conflict (see 3C) |
| 4 | 520,000 warrants at Rs 518.55 to promoter TIC Services; 5 Dec 2026 objects-clause EGM | **Open point settled.** The 22 Sep 2026 board approved TWO separate instruments (outcome p.1): (a) up to 3,86,000 equity shares at Rs 518.55 = up to 2001.60 Lakh (Rs 20,01,60,300), cash, to 26 allottees: 25 non-promoters (Ashish Kacholia 1,73,200; Kushal Khandwala 40,000; Jagattaraini Tieup replaced Vibha Singhi on 23 Sep, filing 20260923-7bb8e0c3 p.1; others 4,800 to 18,000 each) and one promoter, Kamal Grover, 1,200; (b) up to 5,20,000 fully convertible warrants at Rs 518.55 = up to 2696.46 Lakh to ONE allottee, TIC Services Pvt Ltd (Promoter); 25% (674.12 Lakh, derived) payable at allotment, 75% on exercise, 18-month tenor, forfeiture on lapse (Annexure B, p.3). Total raise up to 4698.06 Lakh (EGM notice 20260924-fd526286 p.12). Both passed at the 16 Oct 2026 EGM; 100% of votes polled in favour; 58.41% of shares polled; the promoter group voted 6,578,375 in favour on both items although TIC is the warrant allottee and the form says promoters are "not interested" (20261018-d0ca2f7e pp.5-8). BSE in-principle approval was still awaited on 13 Nov 2026 (H1 FY27 results note 9, p.5). Memory and stage 1 are both right: they describe different instruments of one board action. The 5 Dec 2026 second EGM is a separate item: alteration of the Objects clause to add inspection-body, certification, social audit, lab-operation and training activities (20261113-c4dee558 pp.2-3); it carries no money. Pricing: floor Rs 518.53 (10-day VWAP) vs 448.87 (90-day VWAP), relevant date 16 Sep 2026 (EGM notice p.14). The 12 Oct 2026 corrigendum fixes the shareholding table "pursuant to discrepancies identified in the shareholding pattern" (20261012-7e45c616 p.2): TIC pre-issue 65,78,375 (56.46%), 54.65% after the equity issue, 56.52% after warrant conversion (pp.2-3). Dilution: 9,06,000 new shares = 7.78% of the existing 1,16,52,031 shares (derived). Use of proceeds (EGM notice p.12): unidentified acquisitions in Food, Pharma and **Cybersecurity** 2200.00; automotive expansion 600.00; working capital 800.00; general corporate purposes 1098.06 (23.4% of 4698.06, derived); all within 24 months; no monitoring agency (issue below Rs 100 Cr). | CONFIRMED; open point closed |

SEBI order search (all filings and the three corpus documents). No SEBI order, show-cause notice or adjudication order is referenced in any of the 58 announcements, the FY26 AR, the FY25 AR or the prospectus. Items found that sit near it:
- Stock-exchange penalty, not a SEBI order: the FY25 Secretarial Audit (AR 2025, p.92) records a 342-day delay in submitting the FY2023-24 annual report under Reg 34 LODR; penalty Rs 6,65,520 paid to the exchange on 2 Jul 2025 (AR 2025 p.96, management reply). The FY26 Secretarial Audit (AR pp.82-84) carries no deviation.
- Prospectus (p.287): NIL SEBI or stock-exchange disciplinary action against promoters in the last five years; NIL regulatory actions against the company. Prospectus risk factors (pp.40-52) admit past Section 185 director loans (Rs 11.59 Lakh to Kamal Grover, Rs 31.00 Lakh to Antaryami Nayak), missing CHG-1/CHG-4 filings and an unfiled MBP-1 by Alok Agarwal. No notice had been issued.
- Board report (p.62) states no material order by any regulator, court or tribunal.

---------------------------------------------------------------------

## PHASE 1: AUDITOR'S REPORT AND CARO

### 1A Core opinion
- Standalone and consolidated: unmodified, "true and fair view in conformity with the accounting principles generally accepted in India" (consolidated p.93; standalone p.145). Basis: SAs under s.143(10). Auditor J Madan & Associates, FRN 025913N, partner Naveen Kumar, signed 20 May 2026 (consolidated p.98; standalone p.150).
- Going concern: no material-uncertainty paragraph in either report. The standalone CARO (xix) states nothing suggests material uncertainty "as on the date of this audit report" and adds that this "is not an assurance as to the future viability" (p.155). The consolidated report carries no going-concern emphasis.
- The sign-off date 20 May 2026 is also the date of the board meeting that approved the results and waived intercompany interest (C-Note 26 note p.134).
- Both reports say "The other information is expected to be made available to us after the date of this auditor's report" (consolidated p.94; standalone p.146). The Board report and MD&A are dated 29 Aug 2026, so the auditor never read them. Standard wording, but it means the MD&A claims and the Board's "no adverse remark" line (Board report p.51) were not checked by the auditor.

### 1B Key Audit Matters
| Subject | Why key | How addressed | Risk |
|---|---|---|---|
| None. "We have determined that there are no key audit matters to communicate" (consolidated p.93; standalone p.146, p.148) | n/a | n/a | YELLOW by absence: goodwill of 7811.56 (51.2% of equity, derived) and a 5199.73 related-party share swap would be natural KAMs; the auditor chose none. |

### 1C Emphasis of Matter and Other Matters
None in either report (pp.93-101; pp.145-157).

### 1D CARO 2020 clause by clause (consolidated Annexure A lists qualified or adverse clauses, p.99)
| Entity | Clauses flagged adverse or qualified (p.99) |
|---|---|
| Qualitek Labs Ltd (holding) | 3(iii)(b) and **3(v)** |
| Interstellar Testing Centre Pvt Ltd | 3(iii)(b) |
| Quality & Testing Infosolution Pvt Ltd | 3(xix) |
| LabOps Global Pvt Ltd | 3(xix) |

Standalone CARO detail (pp.151-155):
| Clause | Finding (amount, anchor) | Note |
|---|---|---|
| (ii) inventory | Physical verification done, no material discrepancy; working-capital limit above Rs 5 Cr but no quarterly statements required (p.151) | Inventory is 318.19, immaterial |
| (iii)(a)/(b) loans to subsidiaries | Guarantees given 2,133; loans given in year 1,666.41; balances outstanding: guarantees 1,728.59, loans 311.99. "Loans provided to the subsidiaries are unsecured and interest for the year is waived" (p.152). Board report p.58 lists loans outstanding: ITCPL 162.67, QTIPL 143.13, LabOps 6.20 = 312.00 (ties) | The auditor treats the waiver as prejudicial to the company. The Board report (p.51) still states "no ... adverse remark". |
| (v) deposits | "Delay in repayment of excess application money pending for allotment on issue of shares ... Rs 2.27 Lacs" (p.152); C-Note 39 says Rs 2.28 Lakh pending since 31 Oct 2024, "not traceable" (p.141) | **Stage 2 omitted clause 3(v).** Amount is small. A refund of share application money unpaid for over two years. |
| (vii) statutory dues | Regular; no arrears above six months; no disputed dues (p.153) | But C-Note 28 lists GST demand 91.21 pending at GST Commissioner (Appeals) for FY2017-18 to 2021-22 and income tax 5.48 (p.137). Clause (vii)(b) says none disputed. Contradiction at group level; the matter probably sits in a subsidiary. |
| (ix)(a) default | Axis Bank vehicle loan: principal 1.57 and interest 0.61 not paid on due date, 6 delays (p.153) | Even-one-day rule: this is a lender default. Amount trivial; six delays is a treasury-discipline signal. |
| (xi) fraud / whistle-blower | No fraud; no ADT-4 filed; no whistle-blower complaints (p.154) | Zero complaints in a 1,200-employee group (and in two years per C-Note 39 p.142) is a low-information statement. |
| (xv) non-cash transactions with directors | "Has not entered into any non-cash transactions with its directors or persons connected with them" (p.154) | **Contradicted by the filings**: 11,70,881 shares (3640.15) were issued to TIC Services, the promoter holding company, for ITCPL shares (Board report p.49; C-Note 26 p.131). TIC's ultimate beneficial owners are Alok Agarwal and Antaryami Nayak (EGM notice 20260924-fd526286 p.16). Section 192 applies to directors' connected persons. |
| (xvii) cash losses | None in current and prior year (p.154) | |
| (xix) going concern | No material uncertainty (p.155). Subsidiaries QTIPL and LabOps are flagged on 3(xix) in Annexure A (p.99); the underlying text is NOT FOUND IN DOCUMENT | QTIPL net worth is -11.25 (23.40 less 34.65) and LabOps -15.71 (10 less 25.71) (AOC-1, p.66). Parent loans: QTIPL 143.13, LabOps 6.20. |
| (xx) CSR | Fully spent: required 11.27, spent 11.27 (p.155; CSR report pp.86-88) | Clean. |

### 1E Auditor continuity
| Item | Detail (anchor) |
|---|---|
| Firm | J Madan & Associates (FRN 025913N), New Delhi (p.93) |
| Appointment | 6th AGM, 29 Sep 2023, five years to the 11th AGM (Board report p.50). FY26 is the third audit year. Rotation not due before FY2028-29. |
| Statutory audit fee | Standalone note: statutory 0.55, limited review 0.25, tax audit 0.30, consolidation audit 0.25, consolidation limited review 0.10, other services nil; total 1.45 (FY25 1.06) (S-Note, AR line 8794). Fees of subsidiary audits NOT FOUND IN DOCUMENT. |
| Audit vs non-audit | Non-audit nil (FY25 0.06). Ratio under 5%. |
| Scale check | A fee of 1.45 Lakh is 0.012% of consolidated revenue (derived). The same firm audits all four group entities, including ITCPL which supplies 47.1% of consolidated revenue (AOC-1 turnover 5867.41 of 12451.81, derived, before eliminations). No "reliance on other auditors" exists (consolidated p.95: "All the entities ... have been audited by us"). |
| Peer review status | NOT FOUND IN DOCUMENT |

### 1F Standalone vs consolidated differences
- No extra qualification in either opinion. Differences sit in CARO only (above).
- Consolidated CARO Annexure A (p.99) adds ITCPL 3(iii)(b) and the two small subsidiaries' 3(xix). Standalone CARO text for those entities is not in the AR.
- Group-level contingent liabilities (C-Note 28, p.137): income tax 5.48 (A.Y. 2018-19), GST 91.21 (FY2017-18 to 2021-22); total 96.69 = 0.63% of net worth and 6.6% of PAT (derived). The standalone report says the company has no pending litigations (p.149); the consolidated report says litigation impact is disclosed in Note 28 (p.97).

**Phase 1 summary**
| Item | Result |
|---|---|
| Opinion | Unmodified, no KAM, no EoM |
| CARO adverse clauses | Holding: 3(iii)(b), 3(v); ITCPL 3(iii)(b); QTIPL and LabOps 3(xix); standalone (ix)(a) default and (xv) statement contradicted by the TIC allotment |
| Auditor | Small firm, fee 1.45 Lakh, signs all four entities |
| Board report reading | Says the reports contain no adverse remark (p.51); Annexure A (p.99) lists them |

Phase 1 verdict: YELLOW.
Kill switch (informational): Based on phases so far, a human reviewer would not have reason to stop on the audit report alone, because the opinion is unmodified; but would note that the Board report denies adverse CARO remarks that Annexure A prints, and that the (xv) statement conflicts with the TIC share allotment.

---------------------------------------------------------------------

## PHASE 2: NOTES TO FINANCIAL STATEMENTS (verify, extend, summarise)

### 2.0 Verification of the stage 2 Top 15 against the document
Result: 12 verified in full, 3 verified in part (not fully re-derived here), 1 labelling qualifier, 1 omission, 1 new conflict that stage 2 reconciled differently.

| Rank | Stage 2 finding | Re-check in this pass | Status |
|---|---|---|---|
| 1 | Goodwill 7811.56 = 51.2% of equity 15,242.60; ITCPL cost 8,498.99; "ITCPL net assets 752.02"; profit 710.83; Note 40 "no indication" | BS p.102 (7811.56; 15242.60); 7811.56/15242.60 = 51.25% derived. Cost 8,498.99 (Board report pp.50, 58; H1 FY27 note 5). Profit 710.83 (AOC-1, p.66). Note 40 text confirmed: "No disclosure is required ... since the Group has no indication of a potential impairment loss at present" (p.143). Policy says goodwill is "tested for impairment annually" (C-Note 2 policy, p.109). **752.02 reproduces C-Note 34 (p.140, "share in consolidated net assets", 4.93%), not ITCPL's own net worth. AOC-1 (p.66) shows ITCPL share capital 50.98 + reserves 1,854.67 = 1,905.65 (total assets 6,206.55 less liabilities 4,300.90 ties).** Cost is 4.46x ITCPL's own net worth (derived). Also AOC-1 PBT 936.53 less provision 237.91 = 698.62, not the 710.83 PAT shown (gap 12.21, unexplained; possibly deferred tax). | VERIFIED with a labelling qualifier |
| 2 | Share swap 16,72,531 x 310.89 = 5,199.73; 3,640.15 to TIC; implied 2,039 vs 1,294.6 (+57.5%); 4,507.78 goodwill | Secretarial Audit p.84: Rs 51,99,73,162. Allottees TIC 11,70,881 and Sanjiv Khullar 5,01,650 (Board report p.49). 11,70,881 x 310.89 = 3,640.15 (derived, ties to C-Note 26 p.131). 4,507.78 (C-Note 11e p.125). 5,199.73 / 2,54,959 ITCPL shares = Rs 2,039 per share; 3,299.26 / 2,54,845 = Rs 1,294.6; +57.5% (all derived). Goodwill on the swap is the swap value less minority interest extinguished 694.56 (C-Note 38 p.141): 5,199.73 - 694.56 = 4,505.17 (derived), within 2.61 of 4,507.78. No valuation report for the FY26 swap in the AR: NOT FOUND IN DOCUMENT (the EGM item 17 "not applicable" concerns the FY27 cash issue only). | VERIFIED |
| 3 | Promoter-group credit support; SKM cover 6,874.29; debt +86%; fee 0.20 | C-Note 26 notes (pp.133-134): TIC guarantee facilities 6,449.00 (outstanding 5,739.65); ASC Consulting 7,446.00 (6,718.98); SKM guarantee plus mortgage 7,664.00 (6,874.29); personal guarantees of Nayak 6,295.50, Grover 6,243.14, Alok Agarwal 6,212.63, Anju Agarwal 6,874.29 outstanding. Fee 0.20 for TIC and for SKM (p.132). Borrowings on the face: LT 6,012.15 + ST 3,285.40 = 9,297.55 vs 4,998.45 (+86.0% derived). 9,363.48 and the "84%" ratio were not re-derived (they include lease obligations and an unspecified bank-debt base). | VERIFIED (core); two derived ratios not re-run |
| 4 | AAL entities; "no loans to related parties" | C-Note 26 (p.133): AAL Biosciences advance given 262.00, recovered 262.00; loan taken 148.00, repaid 60.00, payable 88.00; receivable 77.82; sale of services 37.30 (2.09x). AAL Research advance given 148.00, recovered 8.00, **outstanding 151.06** (FY25 11.48). C-Note 39(ii): "not granted any loans or advances in the nature of loans to its directors, KMPs and related parties" (p.141). Contradiction confirmed. | VERIFIED |
| 5 | Receivables 4220.12 gross; over 6 months 944.10; over 3 years 220.46; provision 6.08 | Ageing row (C-Note 15, p.127): 206.67 unbilled, 3069.35 under 6m, 312.41, 310.86, 100.37, 220.46; sub-total 4220.12. 312.41+310.86+100.37+220.46 = 944.10 (22.4% derived). The 6.08 provision figure was not re-read here. Days 123.5 (derived, 4214.04/12451.81 x 365). | VERIFIED (provision figure not re-read) |
| 6 | CFO/PBT 75.7%; capex 4636.21; FCF -3249.05; CWIP +189%; 26.9% over 1 year; capitalised interest 143.14 | CF pp.104-105: CFO 1387.16 / PBT 1832.10 = 75.7%; FY25 1049.93/1041.84 = 100.8%. Capex = 1192.97 + 3391.53 + 51.71 = 4636.21. FCF = 1387.16 - 4636.21 = -3249.05. CWIP 4528.25 vs 1566.34 = +189.1%; ageing (p.142): 834.84 + 232.00 + 151.81 = 1218.65 = 26.9%. Capitalised borrowing cost 143.14 (p.138) = 7.8% of PBT. | VERIFIED |
| 7 | Intercompany interest waived 20 May 2026; CARO 3(iii)(b), 3(xix) | Waiver text: C-Note 26 note (p.134) and CARO (iii)(a) (p.152). **Also CARO 3(v) for the holding company (p.99) and 3(ix)(a) default (p.153), neither in the stage 2 finding.** The C-Note 26 waiver sentence sits in the RELATED-PARTY note of the consolidated statements, where intra-group loans are eliminated; it reads "Loans and advances to related parties are unsecured, carry 8.50%, repayable after three years ... the Group has waived the interest". [INFERENCE] The waiver may cover the AAL Research advance (151.06), not only subsidiary loans. Separating observation: the interest-waived amount by borrower, which the AR does not give. | VERIFIED; OMISSIONS added |
| 8 | SKM rent 21.60 to 153.60; KMP and relatives' pay 222.81 to 430.82; three CS in 14 months | C-Note 26 (pp.132-133): SKM lease rent 153.6 vs 21.60. KMP lines: Nayak 143.12, Grover 46.36, Bhosale 159.15, Gupta 39.41, Bhatnagar 0.13, Garg 5.91, relatives Divya Grover 26.72 and Kishan Chand Grover 10.02 = 430.82 (derived; FY25 same lines = 222.81; +93.4%). Sitting fees 1.40 excluded. CS departures: Bhatnagar (10 Apr 2025), Garg (7 Feb 2026), Mohit (30 Jul 2026), then no appointment found (Phase 5). | VERIFIED |
| 9 | Revenue +77.3% includes ITCPL for a full year; intra-group sales 242.13 not eliminated | +77.3% (Board report p.48: 77.31%). ITCPL consolidated from 11 Sep 2024 in FY25. AOC-2 (p.80) shows QLL revenue from ITCPL 177.58 and software fees to QTIPL 26.45. 242.13 and the "not visibly eliminated" inference were not re-derived. | PARTIAL |
| 10 | Gratuity P&L charge below actuarial (28.90 vs 50.68) | Standalone CF gratuity and leave provision 28.90 (S-CF, AR line 7459); consolidated 111.52 (p.104). 50.68 and 133.31 were not located by string search. | PARTIAL |
| 11 | Current ratio 1.04; cash 555.40 incl 348.28 OD-debit; 310.00 loan on mutual funds | BS: 5875.55 / 5625.13 = 1.04 (FY25 1.31). Cash row p.105: current accounts 206.92, "debit balance in overdraft account" 348.28 (62.7% of cash). 310.00 working-capital demand loan "secured against pledge of" mutual funds (C-Note 5, AR line 5257). | VERIFIED |
| 12 | Statutory dues +224%; interest on late TDS/GST 7.98 vs 0.78; capital creditors 390.75 vs 83.04; vendor advances +119% | Interest on TDS and GST 7.98 vs 0.78 (C-Note 24); capital creditors 390.75 vs 83.04 (C-Note 10). Other current liabilities 1308.54 vs 559.22 (+134% derived). The +224% sub-line was not re-read. | VERIFIED (sub-line not re-read) |
| 13 | Legal and professional 205.27 vs 71.38 | C-Note 24 (p.130) confirmed. | VERIFIED |
| 14 | Text and table contradictions | Re-confirmed: C-Note 28 states no long-term commitments (p.137); C-Note 31 non-cancellable lease table 1,605.91 (p.138); CARO (xv) vs TIC allotment (this stage, 1D). | PARTIAL (software totals not re-run) |
| 15 | IPO money: 818.16 repaid promoter loan = 44.7% of net 1,831.18 | Prospectus Objects of the Issue (PDF p.103): net proceeds 1,831.18; repayment of unsecured loan to Promoter 818.16 (44.7% derived); capex 622.38; working capital 250.00; GCP 140.64. Standalone IPO utilisation note shows 818.16 repaid (S-Note 38). Prospectus risk factor (p.40): the loan was owed to TIC Services. | VERIFIED |

Discrepancies recorded in the YAML: rank 1 (net-assets label), rank 7 (CARO 3(v) and 3(ix) omitted), memory fact 3 (EPS 13.38 vs 12.49 is a filing-versus-AR conflict, not an unreconciled derivation), plus ranks 9 and 10 not re-derived.

### 2A Accounting policy aggressiveness (extends stage 2; Ind AS items NOT FOUND)
| Area | Position (anchor) | Reading |
|---|---|---|
| Revenue | Completed-service-contract method (C-Note 2, p.107) | Conservative; unbilled 206.67 = 4.9% of gross receivables |
| Borrowing costs | Capitalised on qualifying assets: 143.14 FY26 vs 64.30 FY25 (consolidated, p.138); standalone 143.14 vs 29.92 (S-Note, AR line 9594) | Aggressive in direction: all of the consolidated capitalisation sits in the parent. Interest cover 4.81x reported, 3.71x if expensed (derived) |
| CWIP | 4528.25, 26.9% over one year, yet C-Note 39(iii)(b) says no project is overdue (p.142) | Self-contradicting |
| Goodwill | Not amortised; annual test; no inputs disclosed (p.109, p.143) | Aggressive by omission |
| Depreciation | Rates and lives: not re-read in this pass. D&A 668.62 = 5.4% of revenue (FY25 6.1%) | Neutral |
| Employee benefits | AS 15; gratuity and leave provision 111.52 (C-Note 27) | Parent charge below actuarial per stage 2 |
| Prior-period items | 5.92 charged in FY26, nil in FY25 (P&L p.103) | Small; MD&A EBITDA 2,928 is after this item (2,934.44 - 5.92 = 2,928.52 derived) |
| Policy change | None disclosed (MD&A K, p.78) | |
| ECL / Ind AS 116 / ESOP | NOT FOUND IN DOCUMENT (Indian GAAP; no ESOP, Board report p.64) | |

### 2B Related-party map (percent of consolidated revenue 12,451.81, derived)
| Flow | FY26 | % of revenue | Anchor |
|---|---|---|---|
| KMP and relatives' pay | 430.82 | 3.46% | C-Note 26 pp.132-133 |
| SKM Realcon rent | 153.60 | 1.23% | p.133; AOC-2 p.80 |
| ASC Consulting fees | 22.77 (AOC-2 shows 17.60 plus 0.18 reimbursement) | 0.18% | p.133; AOC-2 p.80 |
| Other RPT costs (ASC Outsourcing 5.26; ASC BSR 3.21; AAL outsourcing 19.12 + 0.41 + PPE purchase 24.78) | 52.78 | 0.42% | p.133 |
| Issuance of shares to TIC (non-cash) | 3,640.15 | n/a | p.131 |
| AAL money flows | 148.00 + 262.00 advances given; 148.00 loan taken | 3.7x AAL Biosciences sales (stage 2) | p.133 |
| Guarantee cover (bank debt secured on promoter assets) | 7,664.00 facilities (SKM), 7,446.00 (ASC), 6,449.00 (TIC) | n/a | pp.133-134 |
Value-extraction signals: related-party rent up 7.1x (from 21.60), pay up 93%; two KMP relatives on payroll (Divya Grover 26.72, +91%; Kishan Chand Grover 10.02, +43%); guarantee fees 0.20 against 6,874.29 secured; interest waived on loans. Counter-signal: fees to ASC and rent are small as a percent of revenue; no cash loan to promoters in FY26.
New: **LabOps Global (74%) was bought from Kishan Chand Grover (500 shares) and Divya (240 shares) for Rs 7,400** (Secretarial Audit p.84). Both are named "Relative of Key Managerial Personnel" and are on payroll (C-Note 26 pp.131-132). The AR does not call it a related-party acquisition. The company has lent LabOps 6.20; LabOps has nil turnover and a loss of 31.09 (AOC-1 p.66).

### 2C Contingent liabilities
| Item | Amount | % of net worth 15,242.60 | % of PAT 1,460.15 |
|---|---|---|---|
| Tax and GST demands (C-Note 28, p.137) | 96.69 | 0.63% | 6.6% |
| Bank guarantees, intra-group (2,133.00 by QLL for ITCPL; 4,911.00 stated, outstanding 4,284.04, by ITCPL for QLL) | 7,044.00 | 46.2% | 482% |
Flags: the >25% net-worth flag trips only on the intra-group guarantees; these are not external claims but they show cross-collateralisation of debt. No external contingent liability above 1% of net worth. **Missing:** the ITC Ltd trade-mark suit against ITCPL (Calcutta High Court CS/159/2022, perpetual injunction and Rs 50,00,00,000 punitive damages claimed over the "ITC Labs" name and itclabs.com domain), disclosed in the prospectus (PDF p.289) as litigation involving a group company. It is not in the FY26 or FY25 AR contingent-liability notes, risk text or Board report. The company still markets the brand "ITC Labs" (presentation p.20, May 2026). Current status NOT FOUND IN DOCUMENT.

### 2D Receivables (consolidated, C-Note 15, pp.126-127)
| Bucket | Amount | Share |
|---|---|---|
| Unbilled | 206.67 | 4.9% |
| Under 6 months | 3,069.35 | 72.7% |
| 6 months to 1 year | 312.41 | 7.4% |
| 1 to 2 years | 310.86 | 7.4% |
| 2 to 3 years | 100.37 | 2.4% |
| Over 3 years | 220.46 | 5.2% |
| Gross | 4,220.12 | 100% |
Over 6 months 944.10 = 22.4% (FY25 641.53 = 22.2%, per stage 2). Concentration: NOT FOUND IN DOCUMENT (no customer above 10% is named; the segment note gives only India 12,118.75 revenue / 4,113.19 receivables and outside India 333.06 / 100.85, C-Note 29 p.137). Days trend: consolidated 123.5 (distorted by part-year ITCPL in FY25); standalone 93.8 to 106.4 per stage 2. Bad debts written off 39.70 (FY25 34.35, p.130). H1 FY27 standalone: receivables 2846.03 vs 1970.42 at March (+44.4% in six months, results p.6, derived).

### 2E Inventory
318.19 (FY25 264.51); +20.3%; immaterial (2.6% of revenue). Method FIFO (p.113). Inventory turnover 379.62 in the MD&A ratio table (p.77) is a meaningless figure for a services business.

### 2F Borrowings
- Face: LT 6,012.15 (FY25 3,086.09) + ST 3,285.40 (1,912.36) = 9,297.55 (4,998.45). MD&A filing p.3: Rs 92.97 Cr. 30 Sep 2026: LT 6,612.40 + ST 4,854.48 = 11,466.88 (+23.3% in six months, derived; results p.12).
- Maturity: stage 2 gives FY27 current maturities 917.30. A term loan in C-Note 5 shows "77 EMIs of Rs 28.33 Lakh starting 10th April 2027" (p.117): repayment on that loan starts after a one-year gap, so debt service rises from FY28.
- Security: pledge of mutual funds of a former ITCPL shareholder for a 310.00 working-capital demand loan; hypothecation of current and movable assets; mortgages on SKM-owned Noida properties.
- Covenants: NOT FOUND IN DOCUMENT.
- New facilities after year end: HDFC Bank Rs 91.31 Cr sanction dated 26 May 2026, outstanding Rs 12.80 Cr at 3 Jun 2026; security is the Barwala plots 297 and 298, SKM Realcon's Noida property, and guarantees of SKM Realcon, TIC Services, ASC Consulting and Anju Agarwal (promoter group) (20260603-77c97589, pp.1-2). On 20 Dec 2025 the board approved a private placement of secured NCDs up to Rs 65 Cr with mortgage, pledge of shares, DSRA and promoter personal guarantees (20251220-0fab5880 pp.1-3). Whether the NCDs were issued is NOT FOUND in the filings or the AR.
- ICDs given: none external; intra-group loans 311.99 from the parent.

### 2G Deferred tax and tax
Deferred tax liability 60.33 (74.33); deferred tax credit 14.00 in FY26 (charge 5.73 FY25); prior-year tax credit 47.66 (charge 2.92). Effective rate 20.3% (FY25 26.2%); excluding the prior-year credit, 22.9% (derived). Cash tax paid 485.65 = 26.5% of PBT (derived).

### 2H Exceptional items, post balance sheet, other
- Exceptional items nil in all periods (results p.5).
- C-Note 41: no subsequent events (p.143). Board report (p.64) lists only the ITCPL swap and the LabOps investment. Items after 20 May 2026 are properly outside the notes; the 26 May HDFC sanction is the nearest event.
- Slump sale: Navi Mumbai food lab 882.00 cash, net assets 662.14, goodwill 219.86 (H1 FY27 results note 7); effective 1 Sep 2025.
- **Bengaluru USFDA lab**: the Chairman letter (p.22) and MD&A (pp.70, 72, 76) call it an FY26 acquisition. No note, no cash-flow line, no secretarial-audit event and no results-filing note records a Bengaluru purchase. The May 2026 presentation says "Acquisition of USFDA lab underway, commercial by June 2026" (p.23). Completion is not evidenced in the filings.
- ESOP: none (p.64). Lease obligations: non-cancellable 1,605.91 (354.91 / 770.68 / 480.32, p.138).

**Phase 2 summary and cross-reference to Phase 1.** The auditor chose no KAM, yet the notes hold three audit-grade matters: the untested 7,811.56 goodwill, the TIC share swap, and unmeasured interest waiver. Notes quality scores 4.5 of 10 here (stage 2: 5.0). The reasoning of stage 2 stands. The omitted CARO 3(v)/(ix), the CARO (xv) conflict, the EPS conflict between the results filing and the AR, and the unrecorded Bengaluru acquisition cost half a point. This is a difference of detail, not of direction: stage 2 saw the notes; this pass saw the notes, the auditor's annexures and the filings.
Phase 2 verdict: RED (goodwill, swap and related-party cluster).
Kill switch (informational): Based on phases so far, a human reviewer would not have reason to stop (flags only), but would want the ITCPL valuation report and the goodwill test inputs before any value is placed on 7,811.56 of goodwill.

---------------------------------------------------------------------

## PHASE 3: FINANCIAL STATEMENTS (cash flow, then balance sheet, then P&L)

### 3A Cash flow (consolidated, pp.104-105)
| Line | FY26 | FY25 |
|---|---|---|
| PBT | 1,832.10 | 1,041.84 |
| Operating profit before WC | 3,108.45 | 1,698.34 |
| Less "Minority interest" | (97.92) | none |
| Change in receivables | (1,371.36) | (913.14) |
| Tax paid | (485.65) | (176.72) |
| **CFO** | **1,387.16** | **1,049.93** |
| Purchase of PPE | (1,192.97) | (1,180.66) |
| Purchase of CWIP | (3,391.53) | (1,154.55) |
| Development of intangibles | (51.71) | nil |
| Non-current investments (ITCPL stake) | nil | (3,764.70) |
| Capital advances / LT loans and advances | (85.62) / (276.87) | nil |
| "Acquisition of goodwill" | +94.42 (inflow) | nil |
| Net investing | (4,973.72) | (6,017.05) |
| Long-term loans taken / repaid | 4,941.86 / (2,124.35) | 1,199.23 / (1,122.38) |
| Short-term loans, net | +1,373.04 | +680.69 |
| Interest paid (in financing) | (433.63) | (197.34) |
| Net financing | 3,710.97 | 5,357.24 |
| Net change in cash | 124.42 | 390.12 |

Ratios (derived): CFO/PAT 95.0% (FY25 136.7%); CFO/PBT 75.7% (100.8%); CFO/EBITDA 46.4% on EBITDA 2,987.18 incl other income (Board report p.47). Capex 4,636.21 = 6.9x D&A (668.62). FCF -3,249.05; after interest paid (433.63), -3,682.68. Financing funds the whole gap: net debt raised 4,190.55 (4,941.86 - 2,124.35 + 1,373.04) against an FCF gap of 3,249.05.
CFO quality checks:
- Interest paid sits in financing, lifting CFO by 433.63 against a CFO-after-interest of 953.53 (derived). CFO after interest over PBT is 52.0%.
- "Less: Minority Interest (97.92)" is deducted from operating profit. Minority share of profit is an allocation, not a cash item, and the statement starts from PBT before the allocation. The line understates CFO by 97.92 or mixes a non-cash item into it; the effect is unexplained. NOT RESOLVED.
- "Acquisition of goodwill +94.42" is an inflow with a positive sign. Not explained.
- No one-time inflator found. Liabilities written back 17.06 is deducted (conservative).
- Payables and other liabilities stretch: other current liabilities +393.90 and payables +210.92 add 604.82 to CFO (derived), 43.6% of CFO. Stretch supports CFO more than collections do.
- Cash 555.40 includes 348.28 shown as a "debit balance in overdraft account" (62.7%). Cash on current accounts is 206.92 (p.105).
- H1 FY27 does not improve it: consolidated CFO 359.17 vs PBT 855.11 (42.0%); receivables +912.65; net cash change (400.55); cash 154.89 (results pp.14-15).
FLAG-CASH applies and is carried forward.

### 3B Balance sheet and ratios (consolidated, p.102)
Asset walk (31 Mar 2026 vs 2025): PPE 7,145.72 (5,899.81); intangibles 228.87 (3.83); CWIP 4,528.25 (1,566.34); intangibles under development 44.21; **goodwill 7,811.56 (3,303.78)**; LT loans and advances 625.96; other non-current 834.56; inventory 318.19; receivables 4,214.04 (2,885.75); cash 555.40; other bank 49.37; ST loans and advances 619.76; other current 118.79. Total 27,094.68 (+71.6%). Goodwill is 28.8% and CWIP 16.7% of total assets (derived).
Liabilities: equity 15,242.60 (minority nil); LT borrowings 6,012.15; deferred tax 60.33; LT provisions 154.47; ST borrowings 3,285.40; payables 939.26; other current liabilities 1,308.54; ST provisions 91.93.

| Ratio | FY26 | FY25 | Derivation |
|---|---|---|---|
| Debt / equity | 0.61 | 0.54 | 9,297.55 / 15,242.60; 4,998.45 / 9,278.17 |
| Net debt / EBITDA | 2.96x | 2.76x | (9,297.55 - 555.40 - 49.37) / 2,934.44; FY25 4,481.05 / 1,624.47 |
| Current ratio | 1.04 | 1.31 | 5,875.55 / 5,625.13 |
| Quick ratio | 0.99 | 1.23 | (5,875.55 - 318.19) / 5,625.13 |
| Interest cover (EBIT / finance cost) | 4.81x | 5.98x | 2,312.64 / 480.54; 1,250.88 / 209.04 |
| Interest cover if capitalised interest were expensed | 3.71x | n/a | 2,312.64 / (480.54 + 143.14) |
| ROCE | 10.8% | 10.0% | EBIT / (total assets - current liabilities) |
| ROE (average equity) | 11.9% | n/a | 1,460.15 / 12,260.39 |
| Goodwill / net worth | 51.2% | 35.6% | |
| Tangible net worth (equity less goodwill) | 7,431.04 | 5,974.39 | derived |

Company-published ratios do not tie. Presentation p.13 prints ROE 22%, ROCE 17%, D/E 1.25 for FY26 (ROE 50%, 20%, 17%, 22% over FY23 to FY26). The AR MD&A ratio table, standalone, prints RoNW 6.9%, ROCE 7.4%, D/E 0.45, current ratio 0.92 (pp.77-78). My derived consolidated figures (ROE 11.9%, ROCE 10.8%, D/E 0.61) match neither set. The presentation's 22% ROE and 1.25 D/E are not reproducible from any statement in the AR.
DuPont (average balances, derived): net margin 11.73% x asset turnover 0.58x x equity multiplier 1.75x = 11.9%. ROE is margin-led and held back by low turnover (goodwill and CWIP carry no revenue yet). Leverage is a rising contributor (equity multiplier 1.70 to 1.78 at year end).

### 3C P&L walk (consolidated, p.103; unit Lakh)
| Line | FY26 | % revenue | FY25 | % revenue | YoY |
|---|---|---|---|---|---|
| Revenue | 12,451.81 | | 7,022.69 | | +77.3% |
| Direct expenses | 1,663.78 | 13.4% | 1,020.23 | 14.5% | +63.1% |
| Employee benefits | 4,474.36 | 35.9% | 2,413.06 | 34.4% | +85.4% |
| Other expenses | 3,379.23 | 27.1% | 1,964.93 | 28.0% | +72.0% |
| EBITDA excl other income (before prior period item) | 2,934.44 | 23.6% | 1,624.47 | 23.1% | +80.6% |
| Depreciation | 668.62 | 5.4% | 425.17 | 6.1% | +57.3% |
| Finance cost | 480.54 | 3.9% | 209.04 | 3.0% | +129.9% |
| Other income | 52.74 | 0.4% | 51.58 | 0.7% | +2.2% |
| PBT before prior period | 1,838.02 | 14.8% | 1,041.84 | 14.8% | +76.4% |
| Tax | 371.95 | | 273.48 | | |
| PAT | 1,460.15 | 11.7% | 768.36 | 10.9% | +90.0% |
| Minority share | 97.92 | | 138.28 | | |
| PAT to owners | 1,362.22 | 10.9% | 630.08 | 9.0% | +116.2% |
Other income is 2.9% of PBT (well under the 20% flag). Tax is 20.3% (FY25 26.2%). EPS: 12.49 in the AR; 13.38 in the 20 May 2026 results and the presentation. Reserves reconcile to the AR: 7,682.69 + 1,362.22 + 5,032.48 securities premium (Board report p.48) = 14,077.39 vs 14,077.40.
H2 versus H1 FY26 (results p.5; derived): H2 revenue 7,027.43 vs H1 5,424.38 (+29.6%); EBITDA excl other income 1,805.81 (25.7%) vs 1,122.71 (20.7%). **H2 PAT 983.21 includes a 47.80 prior-year tax credit and a 29.71 deferred-tax credit**; H2 current tax is 283.09 on PBT 1,188.79 (23.8%). Excluding the prior-year credit, H2 PAT is 935.41 = 13.3% of revenue vs 14.0% reported (derived). The Chairman's "H2 PAT margin 14%" (p.22) therefore flatters the exit run-rate by 0.7 points.
H1 FY27 versus H2 FY26 (results p.11; derived): revenue +2.8% sequentially (7,226.65 vs 7,027.43); EBITDA excl other income 1,558.30 = 21.6% (down from 25.7%); finance cost 387.02 = 5.4% of revenue (4.1% in H2 FY26); depreciation 397.11; PBT 855.11 = 11.8%; PAT 660.01 = 9.1%. H1 FY27 interest cover is 3.21x ((855.11 + 387.02) / 387.02). Standalone H1 FY27 EBITDA excl other income is 1,156.26 = 25.9% of 4,472.08 (derived, results p.4), so the consolidated margin gap versus the standalone entity is carried by the subsidiaries (ITCPL and the two small ones), at roughly 14.6% on pre-elimination revenue of 2,754.57 (approximate; intra-group sales are not eliminated in this arithmetic).

**Phase 3 summary and cross-reference.** Growth is real and large. It rests on a full year of ITCPL (47.1% of revenue before eliminations), debt-funded capex and a goodwill stack. Cash conversion falls (75.7% CFO/PBT), interest cover is lower, and the exit run-rate used for guidance carries tax credits. This agrees with the Phase 2 reading.
Phase 3 verdict: YELLOW.
Kill switch (informational): Based on phases so far, a human reviewer would not have reason to stop; they would want the cash flow restated for the minority line, an elimination schedule, and an explanation of the 22% ROE.

---------------------------------------------------------------------

## PHASE 4: RISK FACTORS AND MD&A

### 4A Disclosed risks (MD&A pp.71-72, p.74; Board report p.61)
| Risk (as stated) | Real or boilerplate | Anchor |
|---|---|---|
| Competition | Boilerplate; no share, price or win-rate data | MD&A p.71 |
| Skilled manpower and attrition | Real in substance (stage 2: 45% attrition assumed in the gratuity note) but no rate in the MD&A | pp.71, 76 |
| Regulatory and accreditation | Real; accreditation is a licence to operate (NABL, NABCB) but no list of dates or at-risk labs | p.71 |
| Integration and execution | Real and specific to two acquisitions; no integration KPI | pp.71, 74 |
| Cybersecurity | Boilerplate; yet the FY27 raise names Cybersecurity acquisitions (EGM notice p.12) | pp.71, 74 |
| Capital requirements and working capital | Named, no number | p.72 |
| Financial risk "monitored through prudent management of liquidity, leverage" | Boilerplate against 9,297.55 of debt and a current ratio of 1.04 | p.74 |

### 4B Missing risks (carried to the YAML)
| Missing risk | Evidence | Likely reason for omission |
|---|---|---|
| ITC Ltd trade-mark suit against ITCPL, Rs 50 Cr punitive damages claimed | Prospectus PDF p.289; absent from C-Note 28 (p.137), risk text and Board report; the company still uses "ITC Labs" (presentation pp.20-21) | Status unknown; likely treated as non-quantifiable. Status NOT FOUND. |
| Dependence on promoter balance sheets for credit | C-Note 26 guarantees (pp.132-134); HDFC sanction security (20260603-77c97589 p.2); AGM item 3 seeks FY27 guarantee limits (pp.33-35) | Disclosed as RPT, not as a risk |
| Goodwill impairment | 7,811.56, 51.2% of equity; Note 40 (p.143) | Management reads "no indication" |
| Related-party valuation conflict (swap, warrants, rent, AAL) | Phase 2 | Disclosed as "arm's length" |
| Leverage and refinancing: net debt/EBITDA 2.96x, borrowings +86%, +23% more by 30 Sep 2026 | BS p.102; results p.12 | Framed as "front-loaded acquisition cycle" (MD&A filing p.3) |
| Customer concentration and government/PPP dependence | Six PPP labs (MD&A p.70), government work orders (p.78); no top-10 or >10% disclosure; segment note p.137 | NOT FOUND, so cannot be sized |
| Compliance-function churn: three company-secretary departures (10 Apr 2025, 7 Feb 2026, 30 Jul 2026), post vacant since 30 Jul 2026, and one independent director resigned 29 Oct 2026 | C-Note 26 p.131; announcements 20260209-0b4f223a, 20260730-44102f7e, 20261029-5e7edc16 | Omitted from the Board report (p.53 says the Company "shall disclose all other changes ... based on the final statutory records") |
| Receivable ageing and cash conversion | C-Note 15 (p.127); CF (p.104) | Not mentioned in MD&A |
| Unspecified-acquisition risk: Rs 2,200 Lakh of the FY27 raise is for acquisitions "unidentified" in Food, Pharma and Cybersecurity | EGM notice p.12 | Strategy drift, new vertical |

### 4C MD&A deep dive
Industry claims (p.70): all qualitative; no market size, no growth rate, no peer comparison, no share. Standard TIC drivers only.
Growth and margin explanations: FY26 growth credited to ITCPL consolidation, capacity and "operating leverage" (p.75). Honest on part of it: standalone organic growth +47% (p.75). Silent on the ITCPL-versus-organic split and on the 242.13 of intra-group sales.
External-factor credit or blame: no external blame in either direction; the standalone H2 margin dip is blamed on "planned" pre-operative costs (MD&A filing p.3). H2 consolidated margin is credited to "operating leverage" while H1 FY27 reverses it.
Segment: single reportable segment "Testing Services" (MD&A p.72; C-Note 29 p.137); the May 2026 deck says transport/defence/mechanical 40-45%, pharma 15-20%, food and feed 25-30% of consolidated revenue (presentation p.23), a mix that is not in the AR.
Capex per presentation (p.24): Rs 51.3 Cr in FY26 (cash-flow capex 46.36 Cr; difference 4.94 Cr unreconciled); plan Rs 63 Cr for FY27.

Forward guidance table (also in YAML):
| Claim | Number | Timeframe | Anchor | Credibility |
|---|---|---|---|---|
| Revenue growth | 35% to 40% on 12,451.81 = 16,810 to 17,433 | FY27 | AR pp.23, 73; filing p.3; deck p.25 | LOW to MEDIUM: H1 FY27 was 7,226.65 (+33.2% YoY, only +2.8% on H2 FY26). To hit 35%, H2 FY27 needs 9,583 (+36% YoY, +33% sequential); for 40%, 10,206 (+45% YoY, +41% sequential) (derived) |
| EBITDA margin | 25% to 27% (deck: 25% to 26%) | FY27 | AR pp.23, 73; filing p.3; deck p.25 | LOW: H1 FY27 21.6%; H2 FY27 would need about 27.5% to reach 25% for the year (derived) |
| PAT margin | 15% to 17% in the May filing and deck; 14% to 15% in the AR | FY27 | filing p.3; deck p.25; AR pp.23, 73 | LOW: H1 FY27 9.1%; for 14% for the year H2 needs about 17.7%, for 15% about 19.4% (derived). The range was cut between May and August without comment |
| Arithmetic check on the margin pair | EBITDA 26% less D&A plus interest of about 9.2% of revenue (FY26) leaves PBT near 16.8%; at 22% tax that is PAT near 13.1% | FY27 | derived | The 15% to 17% PAT band cannot be reached with FY26 D&A and interest ratios; the AR's 14% to 15% is closer but still above |
| Revenue ambition | Rs 500+ Cr by FY31 (about 32% CAGR for five years from 124.52 Cr, derived) | FY31 | AR p.24; filing p.3 | LOW to MEDIUM: depends on M&A; organic standalone growth was 47% in FY26 |
| Operating margin | Above 30% over the next three years | FY29 | filing p.3 only | LOW: FY26 23.6%. Dropped from the AR |
| Overseas share | At least 30% of revenue | FY31 | filing p.3 only | LOW: FY26 exports are 333.06 = 2.7% of revenue (C-Note 29 p.137, derived). Dropped from the AR |
| Debt-free, cash surplus | Debt-free and cash-surplus | FY32 | filing p.3 only | LOW: borrowings 9,297.55 now, 11,466.88 at 30 Sep 2026; NCD up to Rs 65 Cr approved; HDFC Rs 91.31 Cr sanctioned. Dropped from the AR |
| Net debt / EBITDA | "compress meaningfully" in FY27 | FY27 | filing p.3 | LOW: 2.96x at March; about 3.6x on annualised H1 FY27 EBITDA (derived) |
| Double revenue every two years; 30% EBITDA margin | 2x per two years; 30% | FY26 to FY27 | FY25 deck p.13 (May 2025) | MIXED: revenue FY24 29.18 Cr to FY26 124.52 Cr = 4.3x (acquisition-led); EBITDA margin 23.6% vs the 30% promised |
| USFDA lab commercial; Hyderabad acquisition done | n/a | June 2026 | deck p.23 | LOW: no completion filed through 14 Nov 2026 |
| Standalone margin re-converges to historical | about 26% to 29% | FY27 | filing p.3 | HIGH so far: standalone H1 FY27 EBITDA 25.9% (derived) |

### 4D Tone and credibility ratings (1 to 5)
| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2 | Guarantees and RPT amounts itemised; impairment inputs, valuation, covenants, customers, ITC suit, intercompany elimination all silent |
| Consistency | 2 | Two EPS figures; guidance cut between May and August; presentation ROE 22% vs derived 11.9%; Board "no adverse remark" vs CARO Annexure A |
| Specificity | 3 | Capex, lab list and growth bands are specific; no segment revenue, no utilisation, no customer data |
| Accountability | 2 | No acknowledgement of the PAT guide cut or the dropped FY29/FY31/FY32 targets |
| Capital-allocation sense | 2 | Debt-funded capex at 6.9x D&A, 7,811.56 goodwill from a related-party swap, a Rs 91.31 Cr facility and NCD plan, unidentified acquisitions in Cybersecurity |
Average 2.2 of 5.

**Phase 4 summary and contradictions with Phases 1 to 3.** The MD&A says internal controls are "adequate and operating effectively" (p.75) and RPTs are "at arm's length" (AOC-2 p.80), while the CARO lists adverse clauses and the notes hold contradictory statements. The MD&A names the margin improvement but not the cash-conversion decline.
Phase 4 verdict: YELLOW.
Kill switch (informational): Based on phases so far, a human reviewer would not have reason to stop; a reviewer should treat the FY27 guidance as unproven after H1.

---------------------------------------------------------------------

## PHASE 5: CORPORATE GOVERNANCE AND BOARD

SME exemption: the Corporate Governance Report under Regs 17 to 27 is not published (Board report p.63). Items below come from the Board report, Annexure B, the committee tables and the filings.

### 5A Board composition (Board report p.52; Non-disqualification certificate p.91)
| Director | Role | On board since | Attendance FY26 | Notes |
|---|---|---|---|---|
| Antaryami Nayak | Chairman and MD | 09/01/2023 | 8 of 8 (100%) | Ultimate owner of TIC Services with Alok Agarwal (EGM notice p.16) |
| Kamal Grover | WTD | 18/05/2018 | 8 of 8 | Promoter; relatives on payroll |
| Mangesh Vitthal Bhosale | WTD | 29/03/2025 | 7 of 8 (87.5%) | Remuneration 159.15; the Non-disqualification certificate (p.91) lists him as "Non-Executive, Non-Independent" |
| Alok Kumar Agarwal | Non-executive promoter | 17/05/2018 | **4 of 8 (50%)** | Ultimate owner of TIC Services; ASC Consulting and ASC Group are RPT counterparties; acts as insolvency professional (prospectus pp.287-288) |
| Sulabh Jain | Independent, Audit Chair | 02/05/2023 | 6 of 8 (75%) | |
| Manish Wahi | Independent | 02/05/2023 | 6 of 8 (75%) | |
| Shubhangi Agarwal | Independent | 02/05/2023 | 6 of 8 (75%) | |
| Ajay Agarwal | Independent | 29/03/2025 | 8 of 8 | **Resigned 29 Oct 2026**, "personal reasons", not on any committee (20261029-5e7edc16 pp.1-4) |
Flags: no independent director exceeds 10 years. Attendance below 75%: Alok Agarwal (50%). Three independent directors sit at exactly 75%. Other-board seat counts: NOT FOUND IN DOCUMENT in the AR (Ajay Agarwal confirms none in listed entities). After the resignation: 7 directors, 3 executive, 1 non-executive promoter, 3 independent (42.9%).
Matrix conflicts: the committee reports say "all members were present" at Audit Committee meetings of 29 May, 29 Aug, 12 Nov, 20 Dec 2025, NRC meetings of 29 May, 29 Aug, 12 Nov 2025, and the CSR committee of 16 Mar 2026 (Board report pp.55-56; CSR report p.86 shows Alok Agarwal 1 of 1). The Board attendance matrix (p.54) shows Alok Agarwal ABSENT at the board meetings of 29 Aug 2025, 20 Dec 2025 and 16 Mar 2026. Same days, opposite records. The 10 Sep 2025 board meeting that allotted 16,72,531 shares to the promoter holding company was attended by Nayak, Grover, Bhosale and Ajay Agarwal only; Jain, Wahi, S. Agarwal and Alok Agarwal were absent. One independent director was present.
Also: the NRC table lists Alok Agarwal as "Whole-Time Director" (p.55); elsewhere he is non-executive.

### 5B Committees (pp.55-56)
| Committee | Members | Meetings | Note |
|---|---|---|---|
| Audit | Jain (Chair, ID), Alok Agarwal (non-exec promoter), S. Agarwal (ID) | 4 | A promoter-director with interests in ASC, TIC and SKM-related flows reviews the RPTs |
| Nomination and Remuneration | S. Agarwal (Chair), Alok Agarwal, Wahi | 3 | |
| Stakeholders' Relationship | Alok Agarwal (Chair), Grover, Jain | 1 | |
| CSR | Nayak (Chair), Wahi, Alok Agarwal | 1 | Obligation 11.27, spent 11.27 |
No risk-management committee is listed. The four Audit Committee meetings fall on result dates; none is recorded for the 10 Sep 2025 share allotment. The 20 May 2026 interest waiver is described as a resolution of the boards of the respective entities (C-Note 26 note p.134); no Audit Committee meeting for it is shown.

### 5C Compensation
| Person | FY26 | FY25 | Change | Anchor |
|---|---|---|---|---|
| Antaryami Nayak (MD) | 143.12 (C-Note 26) vs **27.00 in Annexure B** | 64.26 | +122.7% | pp.132, 68 |
| Kamal Grover (WTD) | 46.36 (C-Note 26) vs **6.60 in Annexure B** | 19.50 | +137.7% | pp.132, 68 |
| Mangesh Bhosale (WTD) | 159.15 | 92.89 | +71.3% | pp.132, 68 |
| Navneet Gupta (CFO) | 39.41 | 20.36 | +93.6% | |
| Relatives: Divya Grover, Kishan Chand Grover | 26.72, 10.02 | 14.00, 7.00 | +91%, +43% | p.132 |
| Independent directors' sitting fees | 1.40 total | 2.35 | down | p.132 |
Annexure B (p.68) puts the MD at 15.64x median and Bhosale at 92.21x median; the implied median remuneration is about 1.73 Lakh (27.00 / 15.64). Permanent employees 677 (p.68). Managerial remuneration rose 73.13% against 12.08% for other staff (p.68). The three executive directors in C-Note 26 total 348.63 (143.12 + 46.36 + 159.15) = 19.0% of consolidated PBT (derived); the note does not say which entity pays. The Annexure B figures for Nayak and Grover do not tie to C-Note 26; the gaps (116.12 and 39.76) are unexplained. Possible commission not in Annexure B (p.68 mentions commission inside managerial remuneration).
**The 8th AGM notice proposed lifting the managerial pay ceiling from 28% to 35% of net profits** (AGM item 4, p.29; Explanatory Statement p.36). The Board withdrew it by circular resolution on 7 Sep 2026 (20260907-d2d6e19d p.1). The existing 28% limit from the 7th AGM stays. Reason for withdrawal: NOT FOUND. A 28% ceiling is well above the usual 11% of net profit. Promoter family payroll: Divya Grover and Kishan Chand Grover (relatives of the WTD) 36.74 total. ESOP: none (p.64). CEO-to-median flag: Bhosale 92.2x; Nayak 15.6x on the Annexure B figure, or 82.9x on the C-Note 26 figure (143.12 / 1.73, derived).

### 5D Shareholding (screener extract, secondary; BSE filing NOT FETCHED, B00)
| | Mar 2024 | Mar 2025 | Mar 2026 | Sep 2026 |
|---|---|---|---|---|
| Promoters | 73.35% | 54.19% | 56.46% | 56.46% |
| FII | 0.00% | 1.77% | 1.60% | 1.54% |
| DII | 0.00% | 0.26% | 0.10% | 0.15% |
| Public | 26.65% | 43.79% | 41.84% | 41.85% |
| Holders | 646 | 750 | 876 | 1,014 |
The promoter share fell 19.2 points in FY25 through new issues (a preferential allotment of 26,07,600 shares at Rs 198.33 = Rs 51.72 Cr, AR 2025 p.93), not through selling. It rose 2.3 points in FY26 through the swap. TIC Services Pvt Ltd alone holds 65,78,375 shares = 56.46% (EGM corrigendum p.2); the promoter block was 6,578,379 shares at the EGM (20261018-d0ca2f7e p.5). Pledge: Nayak's Reg 31(4) declaration for FY26 states no encumbrance by Nayak, Alok Agarwal, Grover, TIC Services or Anju Agarwal (20260406-e7da577b p.1). The December 2025 NCD approval contemplated "pledge of shares" (20251220-0fab5880 p.1) but whose shares is not stated. No promoter selling. The equity and warrant issue takes promoters to 54.65% before conversion and 56.52% after. Price ladder: IPO Rs 100 (Jan 2024), FY25 preferential Rs 198.33, swap Rs 310.89 (May 2025), cash issue Rs 518.55 (Sep 2026): each new issue priced above the last.
UA qualifier (CLAUDE.md): low institutional ownership is not treated as a risk.

### 5E Governance red-flag checklist
| Item | Result |
|---|---|
| Whistle-blower complaints | None (CARO xi(c) p.154; C-Note 39 p.142) |
| SEBI actions | None found (Section 0). Exchange penalty Rs 6.66 lakh in FY25 for the late FY24 annual report |
| RPT committee | Audit Committee reviews; omnibus approval under Reg 23; AGM item 3 passed with only public votes 500,400 (promoters abstained) (20260926-97e33b16 p.9). Item 3's RPT table is lost in the text extraction; the limits cannot be read |
| Auditor fee ratio | Non-audit nil |
| CSR | Compliant |
| Section 143(12) fraud | None (Board report p.51) |
| Material subsidiary auditor | Same auditor for all |
| Related-party swap vote | Passed; valuation report NOT FOUND |
| KMP churn | CFO stable (Navneet Gupta); company secretary: three departures in 16 months. Mohit Kumar resigned 30 Jul 2026 for "pre-occupation and health issues" (20260730-44102f7e p.2). **No successor appears in the 58 filings through 14 Nov 2026**, and the 13 Nov EGM notice authorises "any Director and/or the Company Secretary" (20261113-c4dee558 p.3). The three-month window for filling a compliance-officer vacancy ended 30 Oct 2026 (statutory timing; verify) |
| Name inconsistency | The balance sheet signatory is "Mohit Bhardwaj" (p.102) and the filings say "Mohit Kumar", same ACS 38142 |
| Independent director exit | Ajay Agarwal, 29 Oct 2026, 13 days after the EGM that approved the issues |
| Board versus auditor | Board says no adverse remark; CARO says otherwise |

**Phase 5 summary.** Promoter control is complete: one holding company with 56.46%, three promoter-executive directors, and a non-executive promoter on all four committees. Credit support, rent, consulting, leasing and a share swap all run through promoter entities. Positives: no pledge, no promoter selling, clean FY26 secretarial audit, full CSR, no SEBI action. The attendance record contradicts the committee record on three dates.
Phase 5 verdict: YELLOW.
Kill switch (informational): Based on phases so far, a human reviewer would not have reason to stop, because no pledge, no selling and no regulator action exist; a reviewer would need the swap valuation report and the AAL receivable collection first.

---------------------------------------------------------------------

## PHASE 6: CHAIRMAN'S LETTER AND FRONT MATTER (read last)

### 6A Narrative versus reality
| # | Claim (anchor) | Check | Result |
|---|---|---|---|
| 1 | "FY26 delivered our strongest financial performance since listing ... revenue 124.52 Cr vs 70.23 Cr, EBITDA 29.28 Cr, PAT 14.60 Cr" (p.22) | P&L p.103; EBITDA 29.28 equals 2,928.52 after the prior-period item | Supported. Growth is acquisition-heavy (Phase 3) |
| 2 | "Second half ... EBITDA margin 26% and PAT margin 14% ... operating leverage" (p.22) | H2 PAT includes a 47.80 prior-year tax credit; H1 FY27 EBITDA margin is 21.6% | Supported for H2, flattered at PAT; reversed in H1 FY27 |
| 3 | "Disciplined capital allocation" (p.22); "growth must be accompanied by financial discipline ... operating cash flows" (p.24) | CFO/PBT 75.7%, FCF -3,249.05, borrowings +86%, goodwill from a promoter swap | Not supported on the evidence |
| 4 | "Acquisition of ... a USFDA-approved pharmaceutical laboratory in Bengaluru" in FY26 (p.22; MD&A pp.70, 72, 76) | No note, no cash flow line; deck says "underway" | Unverified in the financials |
| 5 | "10 owned laboratories and 6 PPP laboratories, 1,200 employees, 450 scientists" (p.22) | 677 permanent employees on the rolls (Annexure B p.68); the deck (p.19) counts 450 scientists, 363 field staff, 180 support staff | Headcount basis is not defined; permanent employees are 56% of the claim |
| 6 | "NABCB accreditation ISO/IEC 17020 in June 2026 ... scalable and relatively asset-light inspection business" (p.23) | AR gives no inspection revenue; single segment; the second EGM (5 Dec 2026) is still extending the Objects clause | Milestone is post year-end; economics not shown |
| 7 | "74% investment in LabOps Global ... create long-term value" (p.23) | Cost Rs 7,400; loss 31.09; nil turnover; sellers are KMP relatives (Secretarial Audit p.84; AOC-1 p.66) | Strategic claim; evidence is a start-up with a related-party seller |
| 8 | "Clients include TATA, Cipla, Reliance, Sun Pharma, Dr Reddy's, Patanjali" (Director profile p.19) | No revenue by customer | Unverifiable |

### 6B Strategic priorities
Specific enough: yes for geography (South India), EMI/EMC in Pune, USFDA/EU pharma, Inspection. Capital allocated: Rs 63 Cr FY27 plan (deck p.24); up to Rs 46.98 Cr new raise. Execution evidence: CWIP 4,528.25, of which 3,309.59 is under one year (p.142); lab count 16; no utilisation or revenue-per-lab number is given.

### 6C Metrics showcased versus absent
Showcased: revenue, EBITDA, PAT, number of labs, tests per year ("more than 5 million", p.70), headcount. Absent: utilisation, revenue per lab, customer concentration, customer retention, repeat revenue share, ROE and ROCE (the deck prints them; the AR does not), cash conversion, segment margins, organic growth, order book for the government and PPP work.

### 6D Tone and priority drift versus the prior year
FY25 deck (May 2025, p.13): "2X revenue in every 2 years and 30% EBITDA margin". May 2026 filing: still "double revenue every two years" plus operating margin above 30% over three years. AR Aug 2026: the margin ambition becomes "improving operating margins". Priority drift: from "30% EBITDA margin" to "25-27% for FY27"; from "a cash-surplus, debt-free basis by FY32" to "progressively strengthening our cash-generation capabilities".

### 6E Quiet Abandonment Check (mandatory)
| # | Opening claim (quoted) | Where it should show up | Class | Materiality |
|---|---|---|---|---|
| 1 | MD&A filing 20 May 2026: "operating the business on a cash-surplus, debt-free basis by FY32" | AR Chairman letter (p.24) and Outlook (p.73): "progressively strengthening our cash-generation capabilities"; no debt-free target; borrowings 9,297.55 | (c) hedged retreat | Material: capital-allocation credibility and valuation basis |
| 2 | Same filing: "lifting consolidated operating margin above 30% over the next three years" | AR p.24: "improving operating margins" | (c) hedged retreat | Material: the 30% EBITDA margin is the central bull case in the FY25 deck |
| 3 | Same filing: "generating at least 30% of revenue from overseas customers by FY31" | AR p.24: "increasing international business"; export revenue 333.06 = 2.7% (C-Note 29 p.137) | (c) hedged retreat | Material: a tenfold change in export share is not shown anywhere |
| 4 | May 2026 deck and filing: PAT margin 15-17% for FY27 | AR pp.23, 73: 14-15% | (a) implicit retraction (number cut, not announced) | Material to guidance credibility |
| 5 | AR p.22 and p.76: acquisition of a USFDA pharma lab in Bengaluru completed in FY26 | Notes, cash flow, secretarial audit | (b) silent drop of evidence; deck calls it "underway" | Medium: capacity claim |
| 6 | Deck p.23: "Hyderabad acquisition expected to complete by June 2026" | AR p.78 subsequent developments; nothing | (b) silent drop | Low to medium |
| 7 | AR p.23: Inspection as a "scalable and relatively asset-light" growth engine | Segment disclosure: one segment; no inspection revenue (MD&A p.72) | (b) silent drop of measurability | Medium |
These are separate from Phase 4B, which lists what the AR never covers.

**Phase 6 summary.** Claims that rest on numbers shrink between May and August 2026. No claim is retracted by name.
Phase 6 verdict: YELLOW.
Kill switch (informational): Based on phases so far, a human reviewer would not have reason to stop; they should treat the FY29 margin, FY31 overseas and FY32 debt-free targets as withdrawn.

---------------------------------------------------------------------

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Call | Top reasons |
|---|---|---|
| GARP (fullest) | WATCHLIST | (1) Growth is large: revenue +77.3%, PAT +90.0%, standalone organic +47% (P&L p.103; MD&A p.75). (2) Price to earnings on owners' PAT: market cap Rs 643 Cr (B00 collector gate) over FY26 owners' PAT 13.62 Cr is 47x, and about 49x on annualised H1 FY27 PAT of 13.20 Cr (derived), a premium multiple for ROE near 12% and ROCE near 11%. (3) The growth engine is M&A funded by debt and share issues to related parties; per-share growth is lower than headline: owners' EPS 12.49 vs 7.08 (+76%) while the share count rose 16.8% (99.795 lakh to 116.52 lakh). (4) H1 FY27 PAT 660.01 is below H2 FY26 983.21 and below the guided 14-15% margin. GARP turns PASS only if H2 FY27 shows margin recovery and CFO/PBT above 90% |
| Turnaround (fullest) | FAIL | Not a turnaround. Revenue and profit rose for four years (deck p.11: PAT 3.00 to 14.60 Cr, FY23 to FY26). The transition under test is scale and mix, not recovery. The two small subsidiaries are loss-making: QTIPL -24.94, LabOps -22.44 (AOC-1 p.66) |
| Value + Quality | FAIL | ROE 11.9%, ROCE 10.8% (derived), goodwill 51.2% of equity, CFO/PBT 75.7% |
| Capex-led growth | WATCHLIST | CWIP 4,528.25 (+189%); capex 6.9x D&A; FY27 plan Rs 63 Cr; returns not yet visible: asset turnover 0.58x; 26.9% of CWIP older than one year |
| Cash-flow compounder | FAIL | FCF -3,249.05; interest in financing; H1 FY27 CFO/PBT 42% |
| Contrarian | FAIL | Priced at a premium; no distress signal |
| Insider confidence | WATCHLIST | Promoters are buying: a warrant allotment of 5,20,000 at Rs 518.55 (25% upfront = 674.12 Lakh), no pledge, no selling. Against: the warrants are an 18-month option with forfeiture, the promoters take their own paper at the market price after a swap at Rs 310.89, and the same promoter group sold ITCPL to the company |
| Guidance divergence | FAIL (currently) | H1 FY27 EBITDA margin 21.6% vs guide 25% to 27%; PAT margin 9.1% vs 14% to 15%; PAT guide cut in the AR; FY29/FY31/FY32 targets dropped |

**Phase 7 best fit:** none passes cleanly. Closest: Capex-led growth on WATCHLIST, with GARP on WATCHLIST.

---------------------------------------------------------------------

## PHASE 8: FINAL VERDICT DASHBOARD

### Company snapshot (FY26 consolidated, Lakh unless noted)
Revenue 12,451.81 (+77.3%); EBITDA excl other income 2,934.44 (23.6%); PAT 1,460.15 (owners 1,362.22); EPS 12.49 (AR) / 13.38 (results filing); equity 15,242.60; goodwill 7,811.56; borrowings 9,297.55; CFO 1,387.16; capex 4,636.21; CWIP 4,528.25. H1 FY27: revenue 7,226.65; PAT 660.01; borrowings 11,466.88; cash 154.89.

### Phase-wise verdicts
| Phase | Verdict |
|---|---|
| 1 Auditor and CARO | YELLOW |
| 2 Notes | RED |
| 3 Financials | YELLOW |
| 4 Risk and MD&A | YELLOW |
| 5 Governance | YELLOW |
| 6 Front matter | YELLOW |
| 7 Strategy fit | none passes cleanly |

### Overall quality score: 4.5 / 10
| Component (25% each) | Score | Basis |
|---|---|---|
| Governance | 4.0 | Full promoter control, RPT-heavy structure, three attendance contradictions, CS vacancy, ID exit, withdrawn pay-limit increase; offset by no pledge, no selling, no SEBI action |
| Accounting quality | 4.5 | Stage 2 gave 5.0; half a point off for omitted CARO items, the EPS conflict, the unrecorded Bengaluru acquisition and the cash-flow minority line |
| Balance sheet | 4.0 | Goodwill 51.2% of equity, net debt/EBITDA 2.96x rising to about 3.6x, current ratio 1.04, FCF -3,249.05, promoter-backed credit |
| Earnings quality | 5.5 | High reported margins and strong growth; CFO/PBT 75.7%, receivables over 6 months 22.4%, H2 PAT flattered by tax credits, growth acquisition-led |

### Top 3 strengths
1. Real growth with margins: revenue 12,451.81 (+77.3%), EBITDA margin 23.6%, standalone organic +47% (P&L p.103; MD&A p.75).
2. Clean on regulators and promoter share behaviour: no pledge, no promoter selling, no SEBI action, FY26 secretarial audit with no deviation (pp.82-84; 20260406-e7da577b).
3. Standalone margin discipline: standalone H1 FY27 EBITDA margin 25.9% (derived) and a diversified lab network of 16 sites (MD&A p.70).

### Top 3 red flags
1. Goodwill 7,811.56 (51.2% of equity) built partly through a 5,199.73 share swap with the promoter holding company, no valuation report, no impairment inputs (C-Notes 11e, 26, 38, 40).
2. Cash and leverage: CFO/PBT 75.7% (H1 FY27 42%), FCF -3,249.05, borrowings +86% then +23% in six months, credit resting on promoter guarantees and mortgages.
3. Disclosure conflicts: two EPS figures for one audited year; Board "no adverse remark" vs CARO Annexure A; CARO (xv) vs the TIC allotment; "no related party loans" vs the 151.06 AAL advance; committee attendance vs board attendance; PAT guide cut without comment.

### Key monitorables (next quarter and H2 FY27)
| Metric | Threshold | Where | Why |
|---|---|---|---|
| Consolidated EBITDA margin, H2 FY27 | 27% or higher needed for a 25% year (H1 FY27 21.6%) | H2 FY27 results; 24 Nov 2026 call | Tests the 25-27% guide |
| PAT margin | Above 15% in H2 (H1 FY27 9.1%) | H2 FY27 results | Tests the 14-15% guide |
| CFO / PBT, consolidated | Above 90% (H1 FY27 42%) | H2 cash flow statement | FLAG-CASH |
| Receivables over 6 months | Below 20% of gross (FY26 22.4%) | Annual Note 15 | Collection quality |
| Net debt / EBITDA | Below 3.0x (about 3.6x annualised H1) | Balance sheet at 31 Mar 2027 | Leverage |
| Interest cover | Above 4x (H1 FY27 3.21x) | H2 P&L | Debt service |
| ITCPL profit and goodwill test inputs | ITCPL PAT at or above 710.83; test inputs disclosed | FY27 AR notes, AOC-1 | 8,498.99 cost |
| Use of the 4,698.06 raise | 2,200 for unidentified acquisitions: named target, price, valuation report | BSE filings after in-principle approval | Capital allocation |
| AAL Biosciences receivable 77.82 and AAL Research advance 151.06 | Collected; no new advances | FY27 RPT note | Insider financing |
| Company secretary appointment | Appointed and filed | BSE Reg 30 filings | Compliance function |
| Independent director replacement | Replacement within 3 months | BSE filings | Board independence |
| ITC Ltd suit | Status disclosed | FY27 AR contingent liabilities | Up to Rs 50 Cr claim |
| EPS | One EPS figure of record | H1 FY27 results and FY27 AR | Per-share base |

### One-line verdict
Fast, mostly acquired growth with strong reported margins on a promoter-linked, goodwill-heavy balance sheet whose cash conversion and H1 FY27 margins do not yet support the FY27 guidance; best-fit lens is GARP on WATCHLIST, not a pass.

---------------------------------------------------------------------

## ANCHOR INDEX FOR STAGE 5 (NO-CONCALL MODE; stage 5 reads only these pages)
Page numbers are "[page N]" markers in the named .txt file.

| Topic | File and page |
|---|---|
| Chairman letter, FY27 guidance, Rs 500 Cr FY31 | Annual_Report_2026.txt pp.22-24 |
| MD&A (Annexure C) full text | Annual_Report_2026.txt pp.70-79; outlook and FY27 guide p.73; performance p.75; ratios pp.77-78; subsequent developments p.78 |
| MD&A filing, H2 FY26 (guidance, FY31/FY32 targets, net debt 3.0x) | announcements/20260520-78cbc582-e5c2-400d-b9a9-0e6e2cd444b1.txt pp.2-3 |
| Investor presentation May 2026 (guidance, capex, growth drivers, ROE/ROCE/D-E) | presentation/Investor_Presentation_May2026_H2FY26.txt pp.4, 6-13, 19-25, 41 |
| Investor presentation May 2025 ("2X revenue every 2 years, 30% EBITDA") | presentation/Investor_Presentation_May2025_H2FY25.txt p.13 (text line 270) |
| Objects of issue and use of proceeds (IPO) | prospectus/Qualitek_Final_Prospectus_Jan2024.txt PDF pp.103-104 (printed 100-101); basis for issue price from p.119 |
| Objects and use of proceeds (Sep 2026 preferential issue and warrants) | announcements/20260924-fd526286-de9e-4a0a-ba14-9e05bdd71682.txt pp.12-14, 16; outcome 20260922-b4cbe4e6 pp.1-3; corrigendum 20261012-7e45c616 pp.2-3 |
| Working capital: receivables ageing | Annual_Report_2026.txt C-Note 15 pp.126-127 |
| Working capital: payables, other liabilities, short-term borrowings | C-Notes 8, 9, 10 pp.121-123; cash note 16 p.127 |
| Working capital: loans and advances, other current assets | C-Notes 17, 18 pp.127-128 |
| Cash flow, consolidated | pp.104-105 |
| Standalone cash flow, FY26 | standalone statements pp.160-161 |
| KPI pages: financial highlights (images; no text) | pp.25-26 |
| KPI table (FY23 to FY26 P&L, ROE/ROCE/D-E) | presentation pp.11-13 |
| H1 FY27 results, balance sheet, cash flow | results/20261113-190e3152-723f-4dd6-b960-3db581435d45.txt pp.4-8 (standalone), pp.11-15 (consolidated) |
| FY26 audited results | results/20260520-dc0311a3-a98d-4699-a9a5-cc8f0292bda1.txt p.5 (consolidated), standalone nearby |
| Related parties, guarantees | C-Note 26 pp.131-134; AOC-2 pp.80-81 |
| Board attendance, committees | pp.54-56 |
| Remuneration | Annexure B pp.68-69 |
| Contingent liabilities, segment, FX | C-Notes 28-30 p.137 |
| CWIP ageing, MSME, minority interest | C-Notes 38-39 pp.141-142 |
| Borrowing terms and security | C-Note 5 pp.117-121 |
| Sector and business descriptions | AR pp.6-12; MD&A pp.70-73 |
| New borrowing and security (HDFC Rs 91.31 Cr; NCD up to Rs 65 Cr) | announcements/20260603-77c97589 pp.1-2; 20251220-0fab5880 pp.1-3 |
| Shareholding | shareholding/screener-shareholding-pattern-extract-2026-11-15.txt; EGM corrigendum pp.2-3 |
| Litigation history (ITC Ltd suit, promoters' insolvency roles) | prospectus pp.287-290 |

---------------------------------------------------------------------

```yaml
stage: B03-ardeep
company: "QLL"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "Concall transcripts absent (declared): guidance read from the AR (pp.22-24, 73), the 20 May 2026 MD&A filing and the May 2026 deck only"
  - "Shareholding: screener extract only; BSE shareholding filing not fetched (B00); Sep 2026 pledge not filing-anchored; the FY26 Reg 31(4) no-encumbrance declaration is filing-anchored"
  - "AR is Indian GAAP: ECL matrix, ROU asset, fair-value hierarchy, ESOP notes NOT FOUND IN DOCUMENT"
  - "AGM item 3 RPT limits table lost in text extraction (AR p.34); FY27 guarantee limits unreadable; PDF check needed"
  - "Customer concentration, covenants, interest-waived amount, goodwill test inputs, swap valuation report, ITC Ltd suit status, CARO 3(xix) text for QTIPL and LabOps: NOT FOUND IN DOCUMENT"
  - "NCD (up to Rs 65 Cr) issue status, Bengaluru USFDA lab acquisition cost, company secretary successor after 30 Jul 2026: NOT FOUND in AR or filings"
  - "Peer-review status of the statutory auditor and group-wide audit fees (subsidiaries) NOT FOUND IN DOCUMENT"
flags:
  - "FLAG-CASH: CFO/PBT 75.7% consolidated (FY25 100.8%); FCF -3249.05; H1 FY27 consolidated 42.0% and standalone 39.1%; receivables over 6 months 22.4%; interest paid sits in financing (CFO after interest 953.53)"
  - "FLAG-DISCLOSURE-CONFLICT: two EPS figures for one audited year (13.38 results/presentation vs 12.49 AR); Board report says no adverse remark vs CARO Annexure A (p.99); CARO (xv) says no non-cash director transactions vs 3640.15 TIC share allotment; Board vs committee attendance for Alok Agarwal on 29 Aug 2025, 20 Dec 2025, 16 Mar 2026"
  - "FLAG-GUIDANCE: PAT margin guide lowered from 15-17% (May 2026 filing/deck) to 14-15% (AR, Aug 2026); H1 FY27 EBITDA margin 21.6% and PAT margin 9.1% vs guide 25-27% and 14-15%; FY29/FY31/FY32 numeric targets dropped in AR"
phase_verdicts: {p1: "YELLOW", p2: "RED", p3: "YELLOW", p4: "YELLOW", p5: "YELLOW", p6: "YELLOW", p7_best_fit: "GARP WATCHLIST / Capex-led growth WATCHLIST; no strategy passes cleanly"}
overall_quality: 4.5
quality_components: {governance: 4.0, accounting: 4.5, balance_sheet: 4.0, earnings: 5.5}
kill_switch_notes:
  - "p1: reviewer would not stop; Board report denies adverse CARO remarks that Annexure A (p.99) lists (3(iii)(b), 3(v), 3(xix)); CARO (xv) conflicts with the TIC allotment"
  - "p2: reviewer would not stop; needs the ITCPL swap valuation report and goodwill test inputs before valuing 7811.56 of goodwill"
  - "p3: reviewer would not stop; needs cash flow restated for the minority-interest line (97.92), an elimination schedule and an explanation of presentation ROE 22%"
  - "p4: reviewer would not stop; treat FY27 guidance as unproven after H1 FY27"
  - "p5: reviewer would not stop; no pledge, no selling, no regulator action; needs swap valuation and AAL collection"
  - "p6: reviewer would not stop; treat FY29 margin, FY31 overseas and FY32 debt-free targets as withdrawn"
triple_pass_verification:
  verified: 12
  discrepancies:
    - {finding_rank: 1, triple_pass_value: "ITCPL net assets 752.02", ar_value: "752.02 is ITCPL share in consolidated net assets (C-Note 34); ITCPL own net worth 1905.65 (AOC-1 p.66: 50.98 + 1854.67); cost 8498.99 = 4.46x own net worth", note_ref: "C-Note 34 p.140; Board report Annexure A p.66"}
    - {finding_rank: 7, triple_pass_value: "CARO adverse: 3(iii)(b) QLL and ITCPL; 3(xix) QTIPL and LabOps", ar_value: "Annexure A also lists 3(v) for QLL (excess application money 2.27 not refunded); standalone CARO (ix)(a) reports Axis Bank vehicle-loan default 1.57 principal and 0.61 interest, 6 delays", note_ref: "Consolidated Annexure A p.99; standalone CARO pp.152-153"}
    - {finding_rank: 0, triple_pass_value: "EPS 13.38 'does not reconcile'; 13.38 derived as total PAT over weighted shares", ar_value: "13.38 is the EPS filed in the audited results of 20 May 2026 (minority shown nil, owners 1460.15) and in the presentation p.9; AR statements show 12.49 and owners 1362.22; H1 FY27 filing prints FY26 EPS 12.49", note_ref: "Results 20260520-dc0311a3 p.5; AR P&L p.103; H1 FY27 results p.11"}
    - {finding_rank: 9, triple_pass_value: "Intra-group sales 242.13 not eliminated", ar_value: "Not re-derived in this pass; AOC-2 shows QLL revenue from ITCPL 177.58 and QTIPL software fees 26.45", note_ref: "AOC-2 pp.80-81"}
    - {finding_rank: 10, triple_pass_value: "Gratuity actuarial expense 50.68 vs P&L 28.90", ar_value: "28.90 confirmed on standalone cash flow; 50.68 not located by string search", note_ref: "S-CF; C-Note 27 pp.135-136"}
missing_risks:
  - {risk: "ITC Ltd trade-mark suit against ITCPL, Rs 50 Cr punitive damages claimed; status unknown, not in contingent liabilities or risk text", evidence: "Prospectus PDF p.289 (CS/159/2022 Calcutta HC); absent from AR C-Note 28 p.137; deck p.20 still uses ITC Labs"}
  - {risk: "Dependence on promoter balance sheets for credit (guarantees, mortgages, HDFC sanction)", evidence: "C-Note 26 pp.132-134; announcement 20260603-77c97589 p.2; AGM item 3 pp.33-35"}
  - {risk: "Goodwill impairment, 51.2% of equity, no test inputs", evidence: "BS p.102; Note 40 p.143"}
  - {risk: "Leverage and refinancing: net debt/EBITDA 2.96x, borrowings +86% then 11466.88 at 30 Sep 2026; NCD up to Rs 65 Cr", evidence: "BS p.102; H1 FY27 results p.12; 20251220-0fab5880 pp.1-3"}
  - {risk: "Customer concentration and government/PPP dependence not disclosed", evidence: "C-Note 29 p.137; MD&A pp.70, 78"}
  - {risk: "Compliance-function churn: three company-secretary departures (Apr 2025, Feb 2026, Jul 2026), vacancy since 30 Jul 2026, independent director resigned 29 Oct 2026", evidence: "C-Note 26 p.131; announcements 20260209-0b4f223a, 20260730-44102f7e, 20261029-5e7edc16"}
  - {risk: "Receivable ageing and cash conversion not discussed in MD&A", evidence: "C-Note 15 p.127; CF p.104; MD&A p.75"}
  - {risk: "Unidentified acquisitions incl. Cybersecurity use 2200.00 of the 4698.06 raise (strategy drift)", evidence: "EGM notice 20260924-fd526286 p.12"}
guidance_table:
  - {claim: "FY27 consolidated revenue growth", number: "35-40% on 12451.81 Lakh = 16810 to 17433; H2 FY27 needs 9583 to 10206 (+36% to +45% YoY)", timeframe: "FY27", credibility: "LOW-MEDIUM; H1 FY27 7226.65 Lakh (+33.2% YoY, +2.8% on H2 FY26); AR pp.23, 73; filing 20260520-78cbc582 p.3"}
  - {claim: "FY27 consolidated EBITDA margin", number: "25-27% (deck 25-26%)", timeframe: "FY27", credibility: "LOW; H1 FY27 21.6% (derived); H2 FY27 needs about 27.5%; AR pp.23, 73; deck p.25"}
  - {claim: "FY27 PAT margin", number: "15-17% (May 2026 filing and deck); 14-15% (AR)", timeframe: "FY27", credibility: "LOW; H1 FY27 9.1%; H2 needs about 17.7% for 14% and 19.4% for 15% (derived); range cut in AR; filing p.3, deck p.25, AR pp.23, 73"}
  - {claim: "Consolidated revenue ambition", number: "Rs 500+ Cr by FY31 (about 32% CAGR from 124.52 Cr, derived)", timeframe: "FY31", credibility: "LOW-MEDIUM; acquisition dependent; AR p.24; filing p.3"}
  - {claim: "Operating margin above 30%", number: ">30%", timeframe: "next three years (FY29)", credibility: "LOW; FY26 23.6%; filing p.3 only, dropped in AR"}
  - {claim: "Overseas share of revenue", number: ">=30%", timeframe: "FY31", credibility: "LOW; FY26 exports 333.06 Lakh = 2.7% (C-Note 29 p.137); filing p.3 only, dropped in AR"}
  - {claim: "Debt-free and cash-surplus", number: "debt-free", timeframe: "FY32", credibility: "LOW; borrowings 9297.55 (FY26), 11466.88 (30 Sep 2026); NCD Rs 65 Cr and HDFC Rs 91.31 Cr; filing p.3 only, dropped in AR"}
  - {claim: "Net debt/EBITDA to compress meaningfully", number: "about 3.0x at FY26", timeframe: "FY27", credibility: "LOW; about 3.6x on annualised H1 FY27 EBITDA (derived); filing p.3"}
  - {claim: "Double revenue every two years; 30% EBITDA margin", number: "2x per 2 years; 30%", timeframe: "FY25-FY27 (May 2025 deck)", credibility: "MIXED; revenue 4.3x FY24 to FY26 via acquisitions; EBITDA margin 23.6% vs 30%; deck May 2025 p.13"}
  - {claim: "USFDA pharma lab commercial; Hyderabad acquisition complete", number: "n/a", timeframe: "June 2026", credibility: "LOW; no completion filed through 14 Nov 2026; deck p.23"}
  - {claim: "Standalone margin re-converges to historical", number: "about 26-29%", timeframe: "FY27", credibility: "HIGH so far; standalone H1 FY27 EBITDA 25.9% (derived); filing p.3"}
monitorables:
  - {metric: "Consolidated EBITDA margin H2 FY27", threshold: ">=27% for a 25% year (H1 FY27 21.6%)", where: "H2 FY27 results; 24 Nov 2026 call", why: "Tests the 25-27% guide"}
  - {metric: "Consolidated PAT margin H2 FY27", threshold: ">15% (H1 FY27 9.1%)", where: "H2 FY27 results", why: "Tests the cut 14-15% guide"}
  - {metric: "CFO/PBT consolidated", threshold: ">90% (H1 FY27 42%)", where: "Cash flow statement H2/FY27", why: "FLAG-CASH"}
  - {metric: "Receivables over 6 months share", threshold: "<20% of gross (FY26 22.4%)", where: "Annual Note 15", why: "Collection quality"}
  - {metric: "Net debt/EBITDA", threshold: "<3.0x (about 3.6x annualised H1)", where: "Balance sheet 31 Mar 2027", why: "Leverage"}
  - {metric: "Interest cover (EBIT/finance cost)", threshold: ">4x (H1 FY27 3.21x)", where: "H2 P&L", why: "Debt service"}
  - {metric: "ITCPL PAT and goodwill test inputs", threshold: "ITCPL PAT >= 710.83 Lakh; test inputs disclosed", where: "FY27 AR AOC-1 and notes", why: "8498.99 cost, 7811.56 goodwill"}
  - {metric: "Use of 4698.06 Lakh raise; named target for 2200 Lakh acquisitions", threshold: "Named target, priced, with valuation report", where: "BSE filings after in-principle approval", why: "Capital allocation, related-party warrants"}
  - {metric: "AAL Biosciences receivable 77.82 and AAL Research advance 151.06", threshold: "Collected; no new advances", where: "FY27 RPT note", why: "Insider financing"}
  - {metric: "Company secretary and independent director appointments", threshold: "Both filled and filed", where: "BSE Reg 30 filings", why: "Compliance function and board independence"}
  - {metric: "ITC Ltd v ITCPL suit status", threshold: "Status and exposure disclosed", where: "FY27 AR contingent liabilities", why: "Up to Rs 50 Cr claim"}
ar_new_downstream_entities:
  - name: "LabOps Global Private Limited (formerly Protomation Technologies)"
    where_in_ar: "Board report pp.49-50; Secretarial Audit p.84; AOC-1 p.66"
    entity_type: "Subsidiary (74%); acquired 23 May 2025 for Rs 7,400"
  - name: "Kishan Chand Grover and Divya Grover"
    where_in_ar: "Secretarial Audit p.84 (sellers of LabOps); C-Note 26 pp.131-132 (relatives of KMP on payroll 10.02 and 26.72)"
    entity_type: "RPT counterparties / KMP relatives"
  - name: "ASC BSR And Company LLP"
    where_in_ar: "C-Note 26 pp.131, 133; AOC-2 p.81 (professional fees 3.21)"
    entity_type: "RPT counterparty (KMP-influenced enterprise); first-time status not found in FY25 AR text by name search"
  - name: "Quality Council of India (work order, coal sampling at Western Coalfields loading points)"
    where_in_ar: "MD&A L p.78"
    entity_type: "Institutional customer (post year-end order)"
  - name: "Indian Oil Corporation Limited (2G Ethanol QC lab operation and testing, awarded to ITCPL)"
    where_in_ar: "MD&A L p.78"
    entity_type: "Institutional customer (post year-end order)"
  - name: "Tata, Cipla, Reliance, Sun Pharma, Dr Reddy's, Patanjali"
    where_in_ar: "Director profile, Kamal Grover p.19"
    entity_type: "Named customer claims; no revenue share disclosed; no customer above 10% disclosed"
strengths_top3:
  - "Real growth with margins: revenue 12451.81 Lakh (+77.3%), EBITDA margin 23.6%, standalone organic revenue +47% (P&L p.103; MD&A p.75)"
  - "No promoter pledge, no promoter selling, no SEBI action, clean FY26 secretarial audit (pp.82-84; announcement 20260406-e7da577b)"
  - "Standalone margin holds: standalone H1 FY27 EBITDA margin 25.9% (derived); 16-lab network across sectors (MD&A p.70)"
red_flags_top3:
  - "Goodwill 7811.56 (51.2% of equity) built partly via a 5199.73 Lakh share swap with the promoter holding company; no valuation report, no impairment inputs (C-Notes 11e, 26, 38, 40)"
  - "Cash and leverage: CFO/PBT 75.7% (H1 FY27 42%), FCF -3249.05, borrowings +86% then +23% in six months, credit resting on promoter guarantees and mortgages"
  - "Disclosure conflicts: two EPS figures; Board 'no adverse remark' vs CARO Annexure A; CARO (xv) vs TIC allotment; 'no related party loans' vs 151.06 AAL advance; PAT guide cut without comment"
best_fit_strategy: "GARP WATCHLIST (closest), Capex-led growth WATCHLIST; no strategy passes cleanly"
one_line_verdict: "Fast, mostly acquired growth with strong reported margins on a promoter-linked, goodwill-heavy balance sheet whose cash conversion and H1 FY27 margins do not yet support the FY27 guidance; GARP on WATCHLIST, not a pass."
analyst_note: "Open point settled: the 22 Sep 2026 board approved two instruments, 3,86,000 equity shares at Rs 518.55 (up to 2001.60 Lakh, 26 allottees, one promoter, Kamal Grover 1,200) and 5,20,000 warrants at Rs 518.55 (up to 2696.46 Lakh, TIC Services only, 25% upfront). Memory is right on warrants. The 15-17% PAT margin guide is the May 2026 figure; the AR says 14-15%. EPS 13.38 is the filed results EPS (minority shown nil); AR statements give 12.49 and owners PAT 1362.22. Memory's 6.30 cr NOT FOUND. No SEBI order exists; the only penalty is an exchange penalty of Rs 6.66 lakh (FY25 secretarial audit). Competing readings of the swap: arm's-length price for a business that earned 710.83 Lakh, or insider-priced paper tracking the buyer's own price; separating observation is the missing valuation report and goodwill test inputs. Page numbers use the [page N] markers."
```
