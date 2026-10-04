# STAGE 3: ANNUAL REPORT BACKWARD DEEP DIVE, MMP INDUSTRIES LTD (MMP)
Run date: 2026-10-04 (stage executed 2026-10-05) | Source: Annual_Report_2026.txt (FY2025-26, 247 pages) and Annual_Report_2025.txt (FY2024-25) | Builds on outputs/reports/02-notes.md and B02-notes.yaml

## CONVENTIONS
- UNIT: INR Lakhs (L) as printed in both ARs ("Amount in Rs in Lakhs"). Screener Data_Sheet is INR Cr and is labelled "Cr" where used. Nothing is converted unless shown as "(derived)".
- Anchors: "p.N" = the "[page N]" marker in Annual_Report_2026.txt (printed page = N minus 5). "AR25 p.N" = Annual_Report_2025.txt marker. S = standalone, C = consolidated. "(derived)" = my arithmetic on anchored inputs.
- Ratings: GREEN / YELLOW / RED in words. Kill switch is informational only; the run continues.
- B00 carried: CORPUS GAPPED, no_concall_mode true, sector cap row "Cables / Industrial products". B01 carried: 39/100 core, AVOID classification, FLAG-GATE0, FLAG-CASH.
- EBITDA convention: profit before exceptional item + finance cost + depreciation, other income included, as in B02 (C FY26 6,626.71 L = 8.04%). Ex other income: 6,493.54 L = 7.88% (derived; ties to the screener Quarters operating profit sum of 64.94 Cr).
- Document quality: no Chairman's letter exists in this AR (searched "Dear Shareholders", "Chairman's message"). Phase 6 uses the Board's Report opening and the MD&A opening as the front matter. C auditor's report p.165 has one garbled paragraph (reads "TheSounting records"); check the PDF, not the text.

## LOAD-BEARING FACTS, CHECKED FIRST
| LBF | Result | Anchor |
|---|---|---|
| 1 Guidance vs delivery | FY26 guidance exists in AR25 and is testable. Powders beat (single digit guided, +15.1% delivered). Conductors missed on both revenue momentum and margin (+3.4% revenue, segment margin 4.86% vs 8.27%). MEPL commercial ramp slipped about three quarters. Fire loss landed inside the guided range, but "fully insured" became a 47.4% claim. Phase III powder capacity (2,500 MTPA) is silent in AR26. | AR25 p.18, p.22, p.24; AR26 p.25-26, p.30, p.53; S p.132; C p.226-227 |
| 2 Umred fire and claim | 7 fatalities and 4 injuries (new; B02 had "number of deaths" as NOT FOUND). Gross loss 1,672.01 L = inventory 671.45 + PPE 338.92 + compensation and medical 661.64. Claim 793.05 L recognised, nil received at 31 March 2026. Board's Report says 17.29 Cr, Note 52 says 16.72 Cr. Inventory in Note 52 (671.45) is 88.42 L above what Notes 31 and 32 show leaving EBITDA (583.03). | AR26 p.25; S p.122, p.133-136, p.159 |
| 3 Associates and RPTs | Share of associate profit 820.78 L = 20.5% of C PBT and 26.5% of C PAT. Star Circlips 742.70 L (18.5% of C PBT), Toyal 78.09 L (1.9%). Star carries 4,666.85 L of equity-accounted profit above cost with 9.98 L of dividend received. Promoter family and entity payments 290.34 L with Lalit Bhandari (255.21 L without). Star is unlisted (CIN U24110MH1974PLC017301). | C p.172, p.238; AR26 p.31, p.37-39; S p.151-154 |
| 4 Cash conversion and funding | C CFO 5,328.97 L, of which 1,723.34 L is short-term borrowing and 1,909.56 L is payables build. CFO net of both is 1,696.07 L (derived). Gross capex about 5,560 L (derived). S cash 56.38 L. Commitments C 5,642.27 L. Guarantees 6,688 L. Parent put 1,425 L into subsidiaries in FY26 (equity 400 MEPL, 500 MCPL, 25 MAPL, plus 500 preference in MEPL). | C p.173-174; S p.96, p.119, p.154, p.157; C p.241 |

---------------------------------------------------------------

# PHASE 1: AUDITOR'S REPORT AND CARO

## 1A Core opinion
| Item | Finding | Anchor |
|---|---|---|
| Standalone opinion | Unmodified. "give a true and fair view in conformity with the Indian Accounting Standards" | S Auditor's Report p.80 |
| Consolidated opinion | Unmodified; relies on other auditors for two associates | C Auditor's Report p.161, p.166 |
| Basis | SAs under s.143(10); independence per ICAI Code | p.80 |
| Going concern language | No material uncertainty reported. CARO 3(xix): "nothing has come to our attention ... any material uncertainty ... not capable of meeting its liabilities ... within a period of one year", then "this is not as assurance as to the future viability" | CARO clause xix p.90 |
| IFC (Annexure B) | Unmodified: "adequate internal financial controls ... operating effectively as at March 31, 2026" | p.92 |
| Audit trail | Operated all year, no tampering noticed | p.86 |

## 1B Key Audit Matters
| # | KAM | Why key | How addressed | Risk | Anchor |
|---|---|---|---|---|---|
| 1 | Revenue recognition | Net of discounts and rebates; cut-off | Controls, invoice and dispatch tests, cut-off, rebate review | GREEN. Rebates fell to 97.40 L from 381.41 L (S p.132) and the KAM does not address why | p.80-81 |
| 2 | Existence and valuation of inventories | 15,616.57 L = 28.40% of assets | Attended counts on a sample; reconciled | YELLOW. Counts attended "at selected locations", management representation for others; five plants. Raw material +67.9%, FG fell 20.3% after the FG godown burned (S p.120) | p.81 |
| 3 | Carrying value of trade receivables | 16.05% of assets; ECL matrix | Matrix, ageing, subsequent collections, confirmations | GREEN. Ageing clean (96.3% not due, B02, S Note 41 p.143) | p.82 |
| 4 | CWIP and PPE | Capitalisation, borrowing cost, useful lives | Sample testing | YELLOW. Capitalised interest is NOT FOUND (B02). C CWIP +34.9% to 3,832.49 L | p.82-83 |
| 5 | Loss from fire incidents | Quantum, damaged assets, "estimation of recoverable amounts from insurance claims" | Read policy, claim applications, surveyor reports, insurer correspondence | YELLOW. The KAM lists procedures and gives no conclusion on insurer acceptance. One bullet is printed twice ("Obtained an understanding of the circumstances ..."). "Reviewed the accounting treatment of exceptional items, if any" is hedged. "recognized / assessed insurance claim receivables" does not say which | p.83 |
The C KAMs repeat the same five; the fire KAM cites C Note 55 (C p.164).

## 1C Emphasis of Matter and Other Matters
| Item | Finding | Anchor |
|---|---|---|
| Emphasis of Matter | None in S or C | p.80-86; p.161-168 |
| Other Matter (a) | Three subsidiaries audited by the same firm: total assets 4,618.90 L, revenue 231.91 L, net cash flow 121.34 L | C p.166 |
| Other Matter (b) | Associate share of profit 820.78 L and OCI (167.96) L rely "solely" on other auditors' reports passed on by the Parent's management | C p.166 |
Reading: 20.5% of C PBT and 26.5% of C PAT rest on audits the principal auditor did not perform. Auditor names for Star and Toyal: NOT FOUND IN DOCUMENT.

## 1D CARO 2020, clause by clause (S, Annexure A p.87-90)
| Clause | Remark | Amount | Risk |
|---|---|---|---|
| i (PPE, title deeds) | Clean | none | GREEN |
| ii (inventory) | Verified at reasonable intervals; no discrepancy of 10% or more; stock statements to banks agree with books | none | GREEN (p.87) |
| iii (loans and guarantees) | Loans to WOS 215.00 L in year, outstanding NIL. Guarantees given in year 3,288.00 L, outstanding 6,688.00 L. 3(iii)(f) table shows 215.00 L (100%) under "Promotor's Related Parties" repayable on demand, repaid by year end. Terms "prima facie not prejudicial" | 6,688.00 L guarantees | YELLOW (p.87-88) |
| vii (statutory dues) | Regular, nothing over six months, no disputed dues | none | GREEN (p.88-89) |
| ix (borrowing defaults) | No default, not a wilful defaulter, no term loans raised by the Parent in the year; "funds raised on a short-term basis have, prima facie, not been used for long-term purposes" | none | GREEN (p.89). The qualifier "prima facie, on an overall basis" sits beside 76.6% of group debt being short term (derived) |
| xi (fraud) | No fraud, no ADT-4, no whistle-blower complaint received | none | GREEN (p.89). A fire with 7 deaths produced no whistle-blower complaint |
| xvii (cash loss) | None | none | GREEN (p.90) |
| xx (CSR) | Fully spent; no unspent amount | 68.60 L (S Note 49) | GREEN. The four CSR totals disagree, see 5E |
| xxi (consolidated) | No qualification or adverse remark in any group CARO | none | GREEN (C p.168) |
Adverse or qualified remarks: none.

## 1E Auditor continuity
| Item | Finding | Anchor |
|---|---|---|
| Firm | M/s Manish N Jain & Co., Chartered Accountants, Nagpur, FRN 138430W, peer review certificate 010231; partner Arpit Agrawal, M.No. 175398 | p.86; AR26 p.33 |
| Appointment | At the 49th AGM, 29 August 2022, to the 54th AGM (FY2026-27). Rotation question arises after the FY27 AGM. Tenure before 2022: NOT FOUND IN DOCUMENT | AR26 p.33 |
| Audit fee (S) | Audit 2.30 L, tax audit 0.50 L, certification 0.64 L, total 3.44 L (FY25 2.72 L) | S Note 36.1 p.135 |
| Audit fee (C) | Audit 4.55 L, tax audit 0.50 L, certification 0.64 L, total 5.69 L (derived) | C Note 36.1 (C p.215) |
| Ratio | Non-audit (certification) 0.64 L = 27.8% of the audit fee (derived), below the 100% flag | S p.135 |
| Fee against size | S audit fee 2.30 L on revenue of 82,168.59 L = 0.0028% (derived) | S p.94, p.135 |
| Disagreement | Corporate Governance Report says fees paid "₹2,52,000/-" (2.52 L) against 3.44 L in Note 36.1; 2.52 L equals "Audit Fees Payable" in Note 25 | AR26 p.73; S p.131 |
YELLOW observation: a group with 824 Cr revenue, five plants and 18,452 L of debt pays its principal auditor 2.30 L for the audit. Two readings: (a) a small regional firm priced to a routine mandate, (b) thin audit hours against a fire, an insurance receivable and subsidiary start-ups. The separating observation is an NFRA or ICAI peer-review finding on this firm, NOT FOUND IN DOCUMENT.

## 1F Standalone vs consolidated differences
| Item | Finding | Anchor |
|---|---|---|
| Extra qualifications | None | C p.161-168 |
| Subsidiary auditors | The same firm audits the three subsidiaries (Other Matter a) | C p.166 |
| Associates | Other auditors, unnamed | C p.166 |
| AOC-1 in Board's Report | Does not agree with the C statements (see Phase 2, E1) | AR26 p.37 |
| Fire reference | S KAM cites Note 52, C KAM cites Note 55 | p.83; C p.164 |

## Phase 1 summary
| Metric | Result |
|---|---|
| Opinion | Unmodified, both |
| KAMs | 5 (same in S and C) |
| CARO adverse remarks | 0 |
| Principal-auditor coverage gap | 820.78 L associate profit |
| Audit fee | 3.44 L S, 5.69 L C |
**Phase 1 Verdict: YELLOW.** Clean opinion and clean CARO. The yellow is the fire KAM without a stated conclusion, the other-auditor reliance on 20.5% of PBT, and the audit fee.
**Kill Switch Assessment (informational):** Based on phases so far, a human reviewer would not have reason to stop, because no qualification, going concern doubt or CARO default exists.

---------------------------------------------------------------

# PHASE 2: NOTES TO FINANCIAL STATEMENTS

## Triple-pass Top 15 verification
| Rank | B02 finding | AR check | Result |
|---|---|---|---|
| 1 | Fire: gross 1,672.01 L, claim 793.05 L, net exceptional 878.96 L | 1,672.01 (S p.136, p.159); 793.05 (S p.122); 878.96 (S p.135). Note 52 split: inventory 671.45, PPE 338.92, compensation net of debris 661.64 (sums to 1,672.01). Note 14 footnote says "April 11, 2026" (p.122) | ✓ verified |
| 2 | S CFO 5,438.30 L, borrowing +789.11 L, payables +70.2%, add-back 23.45 vs 371.45 | CFO and borrowing (S p.95); payables 4,615.71 vs 2,712.65 (S p.130); 338.92 + 32.53 = 371.45 (S p.159, p.135) | ✓ verified |
| 3 | EBITDA before 583.03 L fire inventory write-off | RM 17.87 + PM 39.16 (S p.133-134) + 526.00 (S p.134) = 583.03. Note 52 says inventory loss is 671.45 L (S p.159). Gap 88.42 L (derived) | ✗ discrepancy on the inventory base. See E2 |
| 4 | Associate profit 820.78 L, Star 90.5%, dividend 9.98 L, Star OCI (168.32), Star "listed" | 820.78 (C p.172); Star 742.70 of 820.78 = 90.5% (C p.238, derived); dividend 9.98 (S p.133); OCI (168.32) Star and (167.96) group (C p.172, p.238). Star CIN begins "U" = unlisted (AR26 p.31) | ✗ discrepancy: Star is unlisted, not listed |
| 5 | Guarantees 6,688 L = 22.0% of NW; commitments S 3,278.31, C 5,642.27 | 3,400 + 3,288 (S p.157); 6,688 / 30,403.36 = 22.0% (derived); 3,278.31 (S p.157); 5,642.27 (C p.241) | ✓ verified |
| 6 | Group debt 18,452.46 L; C DSCR 2.51 vs 4.55 | 18,452.46 (C p.220); DSCR (C p.224) | ✓ verified |
| 7 | Subsidiary losses 352.81 L; Insulators (329.13) L; DTA 125.62 L | Insulators result (329.13) on revenue 231.94 (C p.226); DTA 125.62 (C p.207, B02 anchor); 352.81 not re-derived here | ✓ verified for the two anchored numbers |
| 8 | Liens 2,545.72 L vs term deposits 242.24 L | Deposits 113.16 (S p.120) + 129.08 (S p.122) = 242.24 ✓. But 2,000.00 L in Note 7 is the borrowing the deposit secures, 445.72 L in Note 14 is the bank guarantee amount (equals Note 47a, S p.157), and the Federal Bank deposit lien in Note 23d is 100.00 L (S p.130). 2,000 + 445.72 + 100 = 2,545.72, so B02 added obligations to a deposit lien | ✗ discrepancy: the "lien exceeds deposits ten times" reading does not hold. See E3 |
| 9 | Other receivables 703.86 L, allowance 283.19 L (40.2%), 77% of charge | 703.86 and 283.19 (S p.120); 53.26 of 68.81 (derived) | ✓ verified |
| 10 | Promoter family and entity payments 255.21 L | 134.40 + 61.98 + 25.83 + 30.00 + 3.00 = 255.21 (AR26 p.38-39; S p.151-152). Lalit Bhandari 35.13 L is excluded; with him 290.34 L | ✓ verified, base stated |
| 11 | Gratuity DBO 611.39 L (+75%), 94.73 L Labour Code | 611.39 vs 349.40 (S p.147); 94.73 (S p.136) | ✓ verified |
| 12 | Hedge trail, 57.02 L MTM, 1,979.34 L forwards | 57.02 (S p.131); 1,979.34 (S p.157) | ✓ verified |
| 13 | Tables do not tie: Schedule III 645.97, maturity +54.00 | 4,371.62 vs 4,317.62 = 54.00 (C p.220, C BS p.171); Toyal carrying 645.98 (C p.197) | ✓ verified |
| 14 | Segment returns foils 3.2%, conductors 13.7%, insulators (9.4%), powder 18.4% | 430.53 / 13,511.96 = 3.19%; 485.92 / 3,541.78 = 13.72%; (329.13) / 3,489.42 = (9.43%); 5,988.44 / 32,473.91 = 18.44% (C p.226-227, derived) | ✓ verified |
| 15 | Clerical slips | Fire date (S p.122) | ✓ verified |
Result: 12 verified, 3 discrepancies (ranks 3, 4, 8). Every headline total ties; the discrepancies sit in how supporting numbers were read.

## Extensions
**E1. AOC-1 does not agree with the consolidated statements (new, YELLOW).**
| Item | AOC-1 (Board's Report) | Consolidated statements | Anchor |
|---|---|---|---|
| MEPL total assets / liabilities | 1,038.75 L / 949.09 L; turnover nil | MEPL HDFC term loan availed alone 2,348.98 L; Insulators segment revenue 231.94 L | AR26 p.37; C p.205, p.226 |
| MCPL total assets / liabilities | 1,031.47 L / 510.81 L | MCPL term loan availed 512.70 L; parent reimbursements to MCPL 1,139.54 L | AR26 p.37; C p.205; S p.153 |
| Subsidiary PAT, three together | (25.77) L | Insulators segment result (329.13) L; subsidiary total assets 4,618.90 L, revenue 231.91 L | AR26 p.37; C p.166, p.226 |
| Internal tie | MEPL: 500 + (10.34) + 949.09 = 1,438.75, against total assets 1,038.75. Gap 400.00 L | n/a | AR26 p.37 (derived) |
AOC-1 looks like an earlier-date or wrongly built table. Reported C totals are internally consistent, so the risk is disclosure control, not a misstated total. The AOC-1 associate "net worth attributable" shows whole-company net worth (Star 182.8 Cr, Toyal 24.85 Cr), not the 26% share (AR26 p.37; C carrying 4,764.68 L and 645.98 L, C p.197).

**E2. EBITDA base for the fire (extends B02 P3-1).** Notes 31 and 32 take 583.03 L out of materials (S p.133-134). Note 52 reports inventory loss of 671.45 L (S p.159). The 88.42 L gap is either stores and spares charged inside "Other Expenses" (so inside EBITDA) or an unexplained difference. Stores stock moved 456.77 L to 447.58 L (S p.120). Two readings: (a) 88.42 L of stores sits in EBITDA, so EBITDA with the whole inventory loss charged is 6,626.71 - 671.45 = 5,955.26 L = 7.23% of C revenue (derived); (b) the 88.42 L is a presentation slip and the 7.33% in B02 stands. Separating observation: the stores and spares line in the Q4 FY26 results, which are image scans outside the corpus text.

**E3. Lien reading corrected.** Note 7 and Note 14 print a rupee amount after "against borrowings" and "against bank guarantees". Those amounts are the obligations secured, not the deposit values. The real collateral issue is thinner: Federal Bank working capital of 2,000.00 L is cash-secured by a 100.00 L deposit and "the remaining portion ... unsecured" (S p.130). Liquidity of 298.62 L (cash 56.38 + deposits 242.24) is still mostly margin money. B02 FLAG-COLLATERAL should read as thin cash collateral, not a text contradiction.

**E4. Accounting policy aggressiveness (kept from B02, 6 of 10).** Plant life up to 25 years (S Note 1.4(a)); overhead capitalisation permitted; capitalised interest NOT FOUND; trade ECL 0.7%; revenue recognised at a point in time on delivery (S p.133). Assessment: moderate, not aggressive, with the judgemental areas thinly disclosed.

**E5. RPT percentages and value-extraction signals.**
| Item | L | % of S revenue 82,168.59 L | Anchor |
|---|---|---|---|
| Sales to Toyal (JV) | 1,801.51 (PY 2,027.19) | 2.19% | S p.153 |
| Job work receipts from Star | 277.06 (PY 262.49) = 84.4% of total job work receipts 328.40 | 0.34% | S p.153, p.132 |
| Promoter family and entities (255.21 + Lalit 35.13) | 290.34 | 0.35%; 6.25% of S PBT before exceptional 4,641.82; 11.0% of S PAT | AR26 p.38-39 |
| CMD pay (unchanged three years, S p.151) | 134.40 | 5.1% of S PAT 2,642.94 | S p.151 |
| Dividend to promoter group (derived at 74.49% of 508.05) | 378.43 | payout 19.2% of S PAT | S p.153, p.158 |
| Parent funding of subsidiaries in FY26 | 1,425.00 (equity 925, preference 500) | 1.7% | S p.119, p.154 |
| Reimbursements MCPL: incurred 1,139.54, repaid 667.79 | net 471.75, no closing balance shown | n/a | S p.153 |
Signals: Rohini Bhandari is paid 30.00 L as legal adviser (flat from PY) and became a Non-Executive Director on 8 August 2025 (AR26 p.28, p.38). Two promoter-family salaries total 87.81 L. The CG Report says "no materially significant transactions ... that had potential conflict" (AR26 p.73). Star Circlips, an associate that MMP holds at 26.06%, is also a promoter-group shareholder in MMP at 4.56% (S p.124); the two cross-hold. RPT pricing method: "terms equivalent to those applicable to unrelated parties" with no method (S p.151).

**E6. Contingent liabilities.** Total 7,133.72 L (BG 445.72 + guarantees 3,400.00 + 3,288.00), up from 3,917.57 L (S p.157).
| Test | Result |
|---|---|
| % of S net worth 30,403.36 L | 23.5% (below the 25% flag) |
| Guarantees alone | 22.0% |
| % of S PAT 2,642.94 L | 270% (above the 100% flag) |
| Tax disputes | None disclosed (CARO vii) |
| Fire litigation or compensation claims | None disclosed, with 7 deaths (AR26 p.25) |

**E7. Debt maturity wall.**
| Item | L | Anchor |
|---|---|---|
| C borrowings due under one year | 14,134.83 (76.6% of 18,452.46, derived) | C p.220 |
| C borrowings 1 to 5 years | 4,371.62 (balance sheet shows 4,317.62) | C p.220, p.171 |
| Over 5 years | nil in the table, but MEPL loan runs to March 2032 and MCPL to March 2033 | C p.205 |
| Scheduled term instalments | COVID loan 18.17 L a month to March 2027; Umred TL 33.33 L an instalment from February 2026 to January 2031; Citi solar 60.00 L a quarter to December 2028; MEPL 31.34 L a quarter from January 2026; MCPL 57.47 L a quarter from March 2027 | S p.126-127; C p.205 |
| S current maturities FY27 | 839.83 | S p.129 |
| Covenants | Complied throughout (B02, S p.142). No default (CARO ix) | p.89 |
| Pledge and personal guarantees | Promoters Arun and Lalit Bhandari guarantee parent loans; Arun and Mayank Bhandari guarantee subsidiary loans; Mayank Fasteners (promoter company) mortgages its Nagpur property for MEPL's HDFC loan | S p.126-127, p.130; C p.205 |
| Cost of debt | S finance cost 1,303.14 / average S borrowings 15,185 = 8.6% (derived). The parent funded MEPL with 7.00% non-cumulative preference shares | S p.135, p.119 |
Observation: the parent borrows near 8.6% and puts money into MEPL at 7.00%, redeemable at par in March 2031. That is a carry cost on the parent (derived).

**E8. Deferred tax.** S DTL 1,825.20 L; WDV difference 2,084.64 L after a 355.48 L charge. S effective rate 27.95% against 25.168% statutory because of 111.79 L tax on non-deductible items (S p.128; base about 444 L, derived). C DTA on losses 125.62 L (C p.207).

**E9. Exceptional pattern, goodwill, ESOP, leases, events after the date.** Exceptional items: FY26 973.69 L (fire net 878.96 + Labour Code 94.73); FY25 nil (S p.94). No goodwill (C intangibles 3.37 L, C p.171). No ESOP or dilution (AR26 p.28). Share count unchanged at 25,402,613. After-date events in the AR: dividend recommendation of 23 May 2026 (S p.158) and the 10 August 2026 board changes (Phase 5).

## Phase 2 reconciliation with B02
B02 scored accounting quality 6 of 10 with no RED. My Phase 2 verdict agrees. One finding is withdrawn (lien), two are refined (EBITDA base, Star unlisted), and one new disclosure-control item is added (AOC-1). The net effect on the score is nil.

## Cross-reference with Phase 1 KAMs
- KAM 5 (fire) and Note 52: the KAM does not say whether the insurer accepted 793.05 L. Note 52 says "based on the final claim assessment", Note 14 says "based on the final claim bill submitted ... considered recoverable by the management". These are two different bases (S p.122, p.159). Contradiction called out here.
- KAM 2 (inventories): FG at 2,956.75 L (-20.3%) after the godown fire, raw material 5,356.24 L (+67.9%), WIP 6,713.37 L (+13.3%) (S p.120).

**Phase 2 Verdict: YELLOW.**
**Kill Switch Assessment (informational):** Based on phases so far, a human reviewer would not have reason to stop, because totals tie and no item is RED, but the recovery, funding and AOC-1 items need operator attention.

---------------------------------------------------------------

# PHASE 3: FINANCIAL STATEMENTS (cash flow first)

## 3A Cash flow (C unless noted; L)
| Item | FY26 | FY25 | Anchor |
|---|---|---|---|
| PAT | 3,100.93 | 3,887.55 | C p.172 |
| CFO | 5,328.97 | 5,678.74 | C p.173 |
| CFO / PAT | 1.72x | 1.46x | derived |
| EBITDA (incl. other income) | 6,626.71 | 6,487.31 | derived |
| CFO / EBITDA | 80.4% | 87.5% | derived |
| Short-term borrowing increase inside CFO | 1,723.34 | 4,426.41 | C p.173 |
| Payables increase inside CFO | 1,909.56 | 388.26 | C p.173 |
| CFO net of borrowing and payables | 1,696.07 | 864.07 | derived |
| CFO net of borrowing only | 3,605.63 | 1,252.33 | derived |
| Gross capex: PPE 3,923.03 + CWIP 991.83 + advances 663.86 less capex liabilities 18.22 | 5,560.50 | 5,178.02 | C p.173; derived |
| Capex / depreciation | 4.9x (1,134.25) | 5.3x (970.55) | derived |
| FCF (CFO less gross capex) | (231.53) | 500.72 | derived |
| FCF net of borrowing inside CFO | (1,954.87) | (3,925.69) | derived |
| M&A | none outside the group | none | C p.173 |
| Financing: non-current borrowings | +1,103.71 | +1,876.63 | C p.174 |
| Interest paid (shown in financing) | (1,333.31) | (1,019.27) | C p.174 |
| Dividend paid | (508.05) | (381.04) | C p.174 |
| Closing cash (C / S) | 196.52 / 56.38 | 1,095.22 / 1,076.42 | C p.174; S p.96 |

Ten-year screener check (INR Cr, Data_Sheet FY17 to FY26): CFO sum 297.83 against PAT sum 246.72, ratio 1.21x. Years below 0.7: FY19 (10.38 / 22.61 = 0.46) and FY22 (18.96 / 28.99 = 0.65). Investing outflow sum 318.22. Cumulative CFO less investing is (20.39) Cr; borrowings rose from 40.76 to 184.52 Cr. Share count flat at 25,402,613 since FY20; the FY18 and FY19 reserve jumps exceed PAT (46.25 to 89.10 to 156.53 Cr), consistent with an equity raise whose amount is NOT FOUND in these documents.

CFO quality checks:
| Check | Result |
|---|---|
| One-time inflators | Payables stretch: year-end payable days 24.8 against 17.8 (derived on purchases of 68,009.78 L and 55,585.28 L). Payables turnover 18.83x against 22.39x (C p.224). 68.2% of CFO is borrowing plus payables (derived) |
| Interest classification | Interest paid sits in financing. CFO after interest would be 3,995.66 L (derived) |
| Working-capital borrowing inside CFO | Yes: "Increase / (Decrease) in Short - Term Borrowings" is an operating line (C p.173). An accepted but generous classification |
| Inventory rundown | None; inventory build 2,320.60 L |
| Receivables | Improved: DSO 39.4 days (year end) against 47.2 (derived). Note 43 average basis 9.24x against 9.44x (C p.224) |
| Cash cycle | Year-end DIO 87.9 + DSO 39.4 less DPO 24.8 = 102.5 days against 121.5 (derived). 7 of the 19 days gained is payables |
Reading: reported CFO looks strong. Strip borrowing and payables and 1,696.07 L remains against 5,560.50 L of capex. FLAG-CASH stays.

## 3B Balance sheet walk (C, L)
| Line | 31.03.2026 | 31.03.2025 | Change | Anchor |
|---|---|---|---|---|
| Total assets | 62,493.66 | 54,903.01 | +13.8% | C p.171 |
| PPE | 25,019.43 | 22,250.36 | +12.4% | p.171 |
| CWIP | 3,832.49 | 2,840.66 | +34.9% | p.171 |
| Investments (all equity-accounted associates: Star 4,764.68 + Toyal 645.98) | 5,410.66 | 4,767.81 | +13.5% | p.171; C p.197 |
| Inventories | 15,809.91 | 13,489.31 | +17.2% | p.171 |
| Trade receivables | 8,884.99 | 8,951.34 | -0.7% | p.171 |
| Cash | 196.52 | 1,095.22 | -82.1% | p.171 |
| Other current financial assets (793.05 is the insurance claim) | 929.99 | 102.67 | +805.7% | p.171; S p.122 |
| Other non-current assets (capital advances) | 1,090.64 | 328.30 | +232.2% | p.171 |
| Equity | 34,650.78 | 32,344.20 | +7.1% | p.171 |
| Borrowings (4,317.62 non-current + 14,134.83 current) | 18,452.46 | 15,625.41 | +18.1% | p.171 |
| Trade payables | 4,622.21 | 2,712.64 | +70.4% | p.171 |
| DTL | 1,701.84 | 1,552.00 | +9.7% | p.171 |
Equity-accounted investments of 5,410.66 L = 15.6% of C equity (derived). Star alone carries 4,666.85 L above cost, 13.5% of C equity, against 9.98 L of dividend received (C p.238; S p.133).

Key ratios:
| Ratio | FY26 | FY25 | Anchor |
|---|---|---|---|
| D/E | 0.53 | 0.48 | C p.224 |
| Net debt / EBITDA | 2.75x | 2.24x | B02; derived |
| Current ratio | 1.26 | 1.39 | C p.224 |
| Quick ratio | 0.51 | NOT FOUND (not derived) | derived |
| Interest coverage (EBIT 5,492.46 / interest 1,333.31) | 4.12x | 5.41x | C p.226; derived |
| DSCR | 2.51 | 4.55 | C p.224 |
| ROCE | 10.12% | 13.66% | C p.224 (B01 shows 10.06%) |
| ROE | 9.26% | 12.70% | C p.224 |
| Goodwill % of net worth | nil | nil | C p.171 |

DuPont (C, average balances, derived): net margin 3.76% x asset turnover 1.404x x equity multiplier 1.752x = ROE 9.25%. FY25 (screener, INR Cr): 5.62% x 1.406x x 1.607x = 12.70%. Margin fell 186 bps, turnover was flat, leverage rose 9%. ROE is margin-driven and leverage is propping it, so it is not operational improvement.

## 3C P&L line walk (S, L; C where stated)
| Line | FY26 | FY25 | YoY | Anchor |
|---|---|---|---|---|
| Revenue | 82,168.59 | 69,185.99 | +18.8% | S p.94 |
| Cost of materials | 66,005.58 | 55,543.77 | +18.8% | S p.94 |
| Change in inventories (credit) | (555.60) | (2,069.76) | n/a | S p.94 |
| Employee | 4,680.15 | 4,395.32 | +6.5% | S p.94 |
| Finance | 1,303.14 | 1,019.26 | +27.9% | S p.94 |
| Depreciation | 1,100.22 | 970.01 | +13.4% | S p.94 |
| Other expenses | 5,139.84 | 4,912.31 | +4.6% | S p.94 |
| PBT before exceptional | 4,641.82 | 4,561.23 | +1.8% | S p.94 |
| Exceptional | (973.69) | nil | n/a | S p.94 |
| PAT | 2,642.94 | 3,334.13 | -20.7% | S p.94 |
| C PAT | 3,100.93 | 3,887.55 | -20.2% | C p.172 |

Margin waterfall (C, derived): revenue 82,400.49 → EBITDA ex other income 6,493.54 (7.88%) → less depreciation 1,134.25 → plus other income 133.17 → less finance 1,333.31 → PBT before exceptional 4,159.15 (5.05%) → less exceptional 973.69 → 3,185.46 → plus associates 820.78 → PBT 4,006.25 → tax 905.32 → PAT 3,100.93 (3.76%). FY25 PAT margin 5.62%.

What drives the margin fall (S, derived):
| Component, % of revenue | FY26 | FY25 |
|---|---|---|
| Materials consumed (before inventory change) | 80.33% | 80.28% |
| Inventory change credit | 0.68% (0.04% underlying, after the 526.00 L fire reclass) | 2.99% |
| Other expenses | 6.26% | 7.10% |
| Employee | 5.70% | 6.35% |
The raw material cost ratio is flat. The FY25 inventory credit of 2,069.76 L was 45.4% of FY25 S PBT of 4,561.23 L (derived). FY26 has almost none. Two readings: (a) FY25 margin was lifted by building stock at rising aluminium prices, so FY26 is the cleaner base; (b) FY26 margin is depressed by the fire and subsidiary start-up and recovers. Separating observation (screener Quarters, INR Cr, consolidated): operating margin by quarter was Q1 FY26 6.96%, Q2 6.85%, Q3 8.70%, Q4 8.66%, Q1 FY27 8.94%, against FY25 quarters of 11.22%, 7.81%, 9.88% and 8.26%. Q2 FY26 was also weak after Umred restarted, so the fire does not explain the whole fall. Q3 FY26 to Q1 FY27 sit at 8.7% to 8.9%, still under the FY25 average of 9.22%.

Other income: S 150.25 L = 3.2% of pre-exceptional S PBT, below the 20% flag; FX gain 55.32 L is the largest part (S p.133). Other income plus associate share = (133.17 + 820.78) / 4,006.25 = 23.8% of C PBT, above the 20% flag (derived).
Exceptional items: single year (FY26). Tax: S effective rate 27.95% (FY25 26.90%), C 22.6% because associate profit enters after tax. EPS: basic = diluted, 12.21 C and 10.40 S (C p.172; S p.94), no gap.

## Cross-reference with Phases 1 to 2
- Phase 2's fire-recovery flag and Phase 3's cash-flow tie-out gap meet here: Note 2 derecognised net block 460.28 L against a cash-flow add-back of 23.45 L (S p.95; B02 P3-4).
- Phase 1's "prima facie not used for long-term purposes" (CARO ix d) sits beside C capex of 5,560.50 L, funded in part by 14,134.83 L of short-term debt. Contradiction called out: debt is rising faster than the working-capital assets it funds (C: debt +18.1%, inventory plus receivables +10.0%, derived).
- Dividend 508.05 L was paid in a year when S cash fell 1,020.04 L (1,076.42 to 56.38) even with 789.11 L of short-term borrowing counted inside CFO (S p.95-96).

**Phase 3 Verdict: YELLOW.**
**Kill Switch Assessment (informational):** Based on phases so far, a human reviewer would not have reason to stop, because the business is solvent and rated BBB+/Stable (AR26 p.29), but cash conversion depends on borrowing and payables.

---------------------------------------------------------------

# PHASE 4: RISK FACTORS AND MD&A

## 4A Disclosed risks
The AR has no risk-factor section. The MD&A "Threats" list (p.55) is the disclosed set. The Board's Report risk paragraph is generic (p.32).
| Disclosed risk | Real or boilerplate | Evidence |
|---|---|---|
| Aluminium price and input volatility | Real: material cost is 80.3% of revenue (derived) and inventory +17.2% | MD&A p.55; S p.94 |
| Geopolitics, trade policy, export demand | Real in part: exports 3,836.87 L, +66.8% (S p.132) | p.55 |
| Competition | Boilerplate, no market share or pricing data | p.55 |
| Delays in infrastructure capex | Real for conductors: segment margin 4.86% against 8.27% (C p.226) | p.55 |
| FX | Real, small: 55.32 L gain, forwards 1,979.34 L (S p.133, p.157) | p.55 |
| Hazardous aluminium powder process | Real: 7 fatalities (AR26 p.25). The MD&A says "unfortunate industrial accident" with no number | p.55 |

## 4B Missing risks (also in the YAML)
| # | Risk absent from the risk section | Evidence | Likely reason for omission |
|---|---|---|---|
| 1 | Subsidiary funding and guarantee exposure: guarantees 6,688 L (22.0% of net worth), commitments C 5,642.27 L against undrawn 3,126.32 L (B02), parent cash 56.38 L | S p.157, p.96; C p.241, p.205 | Group strategy; the capex is the growth story |
| 2 | Insurance recovery gap: AR25 said "fully insured" at 150 to 200 Mn; AR26 recognises 793.05 L of 1,672.01 L, 47.4%, nil received | AR25 p.24; S p.122, p.159 | Claim unsettled |
| 3 | Promoter and key-person dependence: MD and WTD both 70; MD continuation to 31 Jan 2028 and WTD re-appointment to 2032 are AGM items; promoters personally guarantee parent and subsidiary debt; a promoter company mortgages property | AR26 p.6-7; S p.126-127; C p.205 | Family-run company |
| 4 | Foil raw-material dependence: AR25 named Hindalco as "our key supplier" of foil stock; AR26 never names a supplier | AR25 p.18; AR26 p.26 | Dropped from the narrative |
| 5 | Cash conversion rests on supplier credit and working-capital borrowing | S p.95, p.130 | Presented as "better working capital utilisation" (C p.224) |
| 6 | Associate earnings are non-cash: 26.5% of C PAT; Star is unlisted and promoter-linked | C p.172, p.238; AR26 p.31 | Equity-method accounting is standard |
| 7 | Legal and regulatory aftermath of the fire: no contingent liability, no root cause or inspection finding. AR25 said "A detailed investigation is currently underway" | S p.157; AR26 p.25; AR25 p.143 | Likely no case yet, or not disclosed |
| 8 | Disclosure control: AOC-1, CSR figures and the fire date do not agree across sections | AR26 p.37, p.40-42; S p.122 | Clerical process |

## 4C MD&A deep dive
What the MD&A is: seven pages (p.49 to 55) of macro, industry and company description. It contains no revenue, margin, debt, capex or capacity number for MMP. Every FY26 and FY27 quantitative statement sits in the Board's Report (p.25-26, p.30-31). Stage 5 should read the Board's Report pages, not the MD&A, for guidance.

**Industry claims.** Anti-dumping duty on Chinese foil imports (p.51, p.52, p.55); aluminium powder demand from AAC blocks, explosives, defence (p.51); transmission build-out (p.52-53). None carries a market size or a source in AR26. AR25 gave market sizes (Indian aluminium powder market 43,977 tons in 2023 growing to 71,142 tons, AR25 MD&A) and AR26 dropped them.

**Growth and margin explanations.** "Resilient performance ... revenue growing 21% YoY in Q4FY26 and 15% for the full year ... driven by healthy domestic demand, improved exports, and higher value product mix along with better realisations" (AR26 p.25). Volume against price split: NOT FOUND IN DOCUMENT. Foils: "driven by healthy volume growth and better realisations" (p.25). Conductors: demand "sustained", yet revenue +3% (p.25).

**Credit-taking and blaming.** Fire: "Excluding the impact of the incident, the net positive contribution to PAT would have been ₹11 to ₹12 Cr" (p.26). Derived check: EBITDA hit 7 to 8 Cr plus net exceptional 8.79 Cr = 15.8 to 16.8 Cr pre-tax, about 11.8 to 12.6 Cr after 25.168% tax, so the claim is internally consistent. Conductors weakness is blamed on "prolonged payment cycles and elevated metal prices" and government project speed (p.26), all external.

**Forward guidance table with credibility check** (also in the YAML)
| # | Statement | Stated in | Number and timeframe | Delivery test | Credibility |
|---|---|---|---|---|---|
| G1 | Powders FY26 "single-digit growth" | AR25 p.18 | single digit, FY26 | Delivered +15.1% (50,403.54 vs 43,793.05, S p.132) | High (conservative). Beat includes price |
| G2 | Powders Phase III 2,500 MTPA fully operational by end Q2FY26 | AR25 p.18 | 2,500 MTPA, Q2 FY26 | AR26 is silent; segment capex fell to 1,570.86 L from 3,959.69 L (C p.227) | Cannot test. NOT FOUND IN DOCUMENT |
| G3 | Conductors "positive momentum ... with further improved margins" | AR25 p.18 | FY26 | Revenue +3.4% (9,997.96 vs 9,666.99); segment margin 4.86% vs 8.27% (C p.226; derived) | Low: missed both |
| G4 | MEPL Phase I commercial production Q2FY26, "full capacity by end of FY 25-26"; Phase II by Q2 FY26-27 | AR25 p.18, p.22 | Q2 FY26, Q4 FY26, Q2 FY27 | AR26: "commenced commercial production of selected products" (p.53); Phase II "now fully operational" (p.30); "meaningful sales ramp up from Q3FY27" (p.30); FY26 segment revenue 231.94 L, loss (329.13) L (C p.226) | Mixed: capacity ahead, commercial ramp about three quarters behind |
| G5 | Fire loss "150 to 200 Mn ... fully insured" | AR25 p.24 | one-off | Loss 1,672.01 L = 167.2 Mn, inside range; claim 793.05 L = 47.4% (S p.122, p.159). Board's Report says "17.29 Crs" (p.25) | Quantum good, insurance statement not borne out |
| G6 | "Export volumes have also declined due to the economic slowdown in Europe" | AR25 p.18 | FY26 | Exports +66.8% (S p.132) | Conservative |
| G7 | FY27: Powders revenue +13% to 15% with better EBITDA margin; exports +50% | AR26 p.26 | FY27 | Open. Implied powder revenue 56,956 to 57,965 L (derived) | Track record on powders: good |
| G8 | FY27: Foils +15%, "meaningful improvement in EBITDA margins both YoY and QoQ"; Security Printing and Lidding Foil launch "early Q3FY27" with "minimal incremental capital expenditure" | AR26 p.26 | FY27 | Open. FY26 foil margin 2.00% vs 1.96% (C p.226; derived) is the base | Medium; margin claim is soft |
| G9 | Conductors: AL59 BIS approval, traction from H1FY27; LT cable pilot launched July 2026 | AR26 p.26 | H1 FY27 | Open | Low to medium after G3 |
| G10 | MEPL "meaningful sales ramp up from Q3FY27" | AR26 p.30 | Q3 FY27 | Open | Medium; G4 slipped once |
| G11 | MCPL 18,000 MTPA wire rod: "initial machinery installation ... from July 2027" and "plant trials ... during H2FY27" | AR26 p.30 | July 2027; H2 FY27 | The two dates conflict: H2 FY27 ends March 2027, before July 2027. One is a typo | Unreliable until clarified |
Group-level FY27 numbers (B00 notes "+15-18% revenue" and a margin rise) are not in this AR. They come from another source; stage 5 should not credit them to the AR.

**Segment analysis (C p.226-227; S p.132).**
| Segment | Revenue FY26 | FY25 | Growth | Segment result | Margin FY26 | FY25 | Assets | Return on assets |
|---|---|---|---|---|---|---|---|---|
| Powder and paste | 50,403.67 | 43,835.43 | +15.0% | 5,988.44 | 11.88% | 12.37% | 32,473.91 | 18.4% |
| Foils | 21,520.37 | 15,441.20 | +39.4% | 430.53 | 2.00% | 1.96% | 13,511.96 | 3.2% |
| Conductors | 9,997.96 | 9,666.99 | +3.4% | 485.92 | 4.86% | 8.27% | 3,541.78 | 13.7% |
| Insulators (MEPL) | 231.94 | nil | n/a | (329.13) | (141.9%) | n/a | 3,489.42 | (9.4%) |
| Others | 261.73 | 257.38 | +1.7% | 111.20 | 42.5% | 26.3% | 1,101.65 | 10.1% |
Segment capex FY26: powders 1,570.86, foils 35.47, conductors 583.04, insulators 2,128.27, unallocated 597.22, total 4,914.87 L (C p.227). Powders carry 89.6% of the group's segment result (5,988.44 of 6,686.96, derived). Foils hold 25.0% of segment assets and give 6.4% of segment result.

## 4D Tone and credibility ratings (1 to 5)
| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 3 | Fire quantified and fatalities stated; but AOC-1 mismatch, MD&A has no financials, recovery basis thin |
| Consistency | 2 | AR25 to AR26: capacity and Hindalco references vanish; wire-rod dates conflict; fire date typo; four CSR amounts |
| Specificity | 3 | Specific FY27 growth rates and launch quarters; no capacity, margin or capex numbers |
| Accountability | 2 | Conductors weakness placed on government payment cycles and metal prices; no root cause for the fire; "robust ... frameworks" language (p.55) |
| Capital allocation sense | 2 | 5,560 L capex with negative FCF, 508 L dividend, 7.00% preference into MEPL against 8.6% debt, 6,688 L guarantees |

**Contradictions against Phases 1 to 3.** (1) MD&A: "Following the unfortunate industrial accident ... strengthened its safety framework" (p.55) against the Corporate Governance goal of "Zero Failure, Zero Defect, and Zero Accident" (p.52) and 7 deaths (p.25). (2) MD&A p.54 says backward integration is "expected to improve ... margins"; conductors margin fell 341 bps in the year (C p.226, derived). (3) Board's Report says foils margin "improved both YoY and QoQ" (p.25); the annual change is +4 bps (derived).
**Phase 4 Verdict: YELLOW.**
**Kill Switch Assessment (informational):** Based on phases so far, a human reviewer would not have reason to stop, because guidance is partly delivered and the risks are visible in the notes, but the qualitative MD&A and the date conflict need verification.

---------------------------------------------------------------

# PHASE 5: CORPORATE GOVERNANCE AND BOARD

## 5A Board composition (31 March 2026, with 10 August 2026 changes)
| Director | Role | Meetings attended | Other boards (listed) | Flag |
|---|---|---|---|---|
| Arun Bhandari | CMD, promoter, age 70, 27.40% holder | 6/6 | 7 (0) | MD continuation past 70 to 31 Jan 2028 is an AGM item (AR26 p.6) |
| Lalit Bhandari | WTD, promoter, age 70 | 6/6 | 1 | Re-appointment to 31 March 2032 is an AGM item (AR26 p.6-7) |
| T N Murthy | WTD, non-promoter | 3/6 = 50% | 0 | Attendance below 75% |
| Mayank Bhandari | NED, promoter, age 41 | 3/6 = 50% | 8 (2 listed) | Attendance below 75%; 9 board seats including MMP, above the 8-seat flag |
| Rohini Bhandari | NED, promoter family, appointed 8 Aug 2025 | 3/4 = 75% | 2 | Paid 30.00 L as legal adviser; relative of three directors |
| Vijay Bapna | ID, AC chair | 6/6 | 3 (2 listed) | Second term ran to the 53rd AGM; resigned 10 Aug 2026 |
| Sunil Khanna | ID | 6/6 | 1 | Same; resigned 10 Aug 2026 |
| Sanjay Sacheti | ID | 6/6 | 4 | AC chair from 10 Aug 2026 |
| Ulka Kulkarni | ID | 4/6 = 66.7% | 2 | Attendance below 75% |
| Sachin Nirgudkar | ID, appointed 8 Aug 2025 | 4/4 | 0 | none |
| Raj Sethia, Sanjay Arora | ID, appointed 10 Aug 2026 | NA | 0 | New; appointment is an AGM item |
Anchors: AR26 p.57-58, p.28-29, p.6-8. Karan Varma, ID, resigned 8 August 2025 "owing to preoccupation" after attending 1 of 3 meetings (AR26 p.57-58).
Tenure flags: Bapna and Khanna were in a second five-year term ending at the 53rd AGM, which began at the 48th AGM (AR26 p.28), so each had served about ten years (derived; first appointment date NOT FOUND IN DOCUMENT). Their resignation on 10 August 2026 came 33 days before the 12 September 2026 AGM and two new independents were appointed the same day. A reason beyond term expiry is not stated. Reading (a): normal end of term. Reading (b): early exit of both the Audit Committee chair and the NRC chair. Separating observation: the stock-exchange resignation filings, outside this AR. Promoter-group cross-board membership: Arun and Mayank sit on the Star and Toyal boards.
Related directors: Arun is father of Mayank and Rohini and cousin of Lalit (AR26 p.58). At 31 March 2026 the board had 10 directors: 5 independent, 2 executive promoters, 1 executive non-promoter and 2 promoter-family non-executives (derived from p.57).

## 5B Committees
| Committee | Meetings | Composition note | Anchor |
|---|---|---|---|
| Audit | 4 | Four members listed. From 10 Aug 2026 Arun Bhandari (CMD, executive) joins and promoter NED Mayank leaves. The text says "All other members including Chairman ... are the Non-executive, Independent Directors" and then lists Arun Bhandari. Three of four independent (75%) | AR26 p.63-65 |
| Nomination and Remuneration | 1 (8 Aug 2025) | Independents; chair changes 10 Aug 2026 | p.65-66 |
| Stakeholders' Relationship | 1 | Includes Lalit Bhandari | p.67-68 |
| CSR | 2 | Arun chairs; Mayank attended 1 of 2 | p.68 |
| Risk Management | NOT FOUND (meeting count not stated) | Lalit chairs | p.70 |
| Project Monitoring | NOT FOUND (meetings not stated); mandate refers to "Objects of the IPO" | Arun chairs | p.70 |
| Whistle-blower | Policy exists; no complaint received (CARO xi, p.89) | | p.70-71 |
Reading: an executive promoter on the Audit Committee weakens its independence. The Audit Committee met four times in a year with a fatal fire and a 793.05 L receivable, and the board met six times (AR26 p.57). The Risk Management Committee meeting count is not disclosed.

## 5C Compensation
| Person | Pay (L) | Note |
|---|---|---|
| Arun Bhandari (CMD) | 134.40 | 5.1% of S PAT; unchanged three years (S p.151) |
| Lalit Bhandari (WTD) | 35.13 | FY25 35.37 |
| T N Murthy (WTD) | 23.69 | |
| CFO Sharad Khandelwal | 31.71 | |
| CS Madhura Singh | 10.67 | |
| Saroj Bhandari (relative, Unit Head) | 61.98 | Flat |
| Sakshi Bhandari (relative, Manager) | 25.83 | Flat |
| Rohini Bhandari (adviser and NED) | 30.00 | Flat |
Anchors: AR26 p.66-67, p.72; S p.151-152. Whole-time directors total 193.22 L = 4.2% of pre-exceptional S PBT (derived), well inside Schedule V. CEO-to-median multiple: NOT FOUND ("will be available at Corporate office", AR26 p.29). Independent directors' sitting fees 1.00 to 2.35 L each (AR26 p.67). ESOP or dilution: none (AR26 p.28).

## 5D Shareholding (NSE XBRL, 30 June 2026, inputs/shareholding/SHP_MMP_2026-06-30.md)
| Item | Result |
|---|---|
| Promoter and group | 74.49% (74.48% every quarter from 30 Sep 2024 to 31 Mar 2026). Flat; no selling |
| Pledge and encumbrance | None declared (all six encumbrance flags false) |
| FPI | 2 holders, 4,995 shares = 0.02% |
| DII and mutual funds | None listed |
| Public | 25.51%; 11,192 holders |
| Large holders (S p.123-124) | Arun 27.40%, Mayank Fasteners Pvt 18.83%, Saroj 12.81%, Vivaan (minor) 5.74%, Star Circlips 4.56% |
Low institutional ownership is not treated as a risk (house rule). Observation: Star Circlips, an associate, owns 4.56% of MMP and is counted inside the promoter 74.49%. The promoter group received about 378.43 L of the 508.05 L dividend (derived from S p.153).

## 5E Governance red-flag checklist
| Check | Result |
|---|---|
| Whistle-blower complaints | None (CARO xi p.89) |
| SEBI actions | None in three years (AR26 p.72-73) |
| RPT committee | Audit Committee approves; omnibus approval dated 23.05.2025 for all AOC-2 items (AR26 p.38-39). A single approval date covers every item, including 1,139.54 L of MCPL reimbursements for a company incorporated in June 2025 |
| Auditor fee ratio | 27.8% non-audit; fee amount very low (Phase 1) |
| CSR compliance | Spent in full, but the AR prints four totals: 68.55 L (CG Report p.69), 68.56 L (Annex C item 8f), 68.60 L (S Note 49) and 60.07 L (Annex C item 7a, AR26 p.40-41). "Average net profit 10,383.62 L" times 2% is 207.67 L, not 68.56 L; 68.56 L equals 2% of the 3,427.87 L printed in the CG Report (derived). Annex C turnover 69,340.54 L and net worth 28,368.82 L are FY25 figures (S p.93-94). Projects: 47.42 L spent directly on education, 6.00 L "Religious and other activities" shown under environment |
| Section 143(12) fraud | None (p.89) |
| Material subsidiary auditor | No material subsidiary (AR26 p.73); the same firm audits the subsidiaries |
| Secretarial audit | Exceptions: website data not updated "due to technical glitches", some e-forms filed late with fees; Secretarial Auditor appointment not yet approved by the AGM (AR26 p.46-47) |
| Board independence | 5 of 10 directors independent at year end (derived; half, as the chair is executive); executive promoter joins the AC |
| Fire accountability | No governance statement on safety audit findings or board review of the fire |
**Phase 5 Verdict: YELLOW.** No pledge, no selling, small RPTs, no fraud. Yellow for an executive promoter on the Audit Committee, two committee chairs rotated in one day, low attendance by one executive and one promoter director, personal guarantees, an unlisted promoter associate cross-holding MMP, and CSR and AOC-1 disclosures that do not tie.
**Kill Switch Assessment (informational):** Based on phases so far, a human reviewer would not have reason to stop, because the governance gaps are procedural and the promoter stake is unpledged.

---------------------------------------------------------------

# PHASE 6: FRONT MATTER (read last)

No Chairman's letter exists. Front matter used: Board's Report state of affairs and future plans (p.25-26), MD&A opening and strategy (p.49-55), Corporate Governance vision (p.52).

## 6A Narrative against reality
| # | Claim | Reality | Mark |
|---|---|---|---|
| 1 | Powders "resilient performance ... 15% for the full year despite the operational disruption" (p.25) | Segment revenue +15.0% (C p.226) | ✅ |
| 2 | Foils "Margin performance improved both YoY and QoQ" (p.25) | Segment margin 2.00% vs 1.96%, +4 bps; return on segment assets 3.2% (C p.226-227) | ✅ in direction, trivial in size |
| 3 | Conductors "supported by sustained demand" (p.25) | +3.4% revenue; margin 4.86% vs 8.27% (C p.226) | ❌ |
| 4 | MEPL "made significant progress ... commenced commercial production of selected products" (p.53); "healthy margin potential" (p.30) | Revenue 231.94 L, loss (329.13) L, segment assets 3,489.42 L (C p.226-227) | ❌ not yet evidenced |
| 5 | "FY26 profitability would have been materially higher excluding the impact of the incident"; PAT +11 to 12 Cr (p.26) | Derived 11.8 to 12.6 Cr after tax from the stated EBITDA hit and the net exceptional | ✅ |
| 6 | Goals of "Zero Failure, Zero Defect, and Zero Accident" (p.52) | 7 fatalities, 4 injuries (p.25) | ❌ |
| 7 | "no materially significant transactions with the related parties ... that had potential conflict" (p.73) | Promoter-family and entity payments 290.34 L; promoter company mortgage backs MEPL debt (C p.205) | ✅ on scale, with the collateral caveat |

## 6B Strategic priorities
| Priority | Specific enough | Capital allocated | Execution evidence |
|---|---|---|---|
| Integrated electrical products (insulators, LVPC, covered conductors, wire rod) | Medium: product names, no revenue or margin target | Group capex FY26 4,914.87 L by segment (C p.227); commitments C 5,642.27 L (C p.241); guarantees 6,688 L | MEPL revenue 231.94 L; LVPC greenfield has no timeline; wire-rod dates conflict |
| Exports +50% in FY27 | High (a number) | none stated | FY26 exports +66.8% |
| Value-added foil products (Security Printing, Lidding) | Medium (launch quarter) | "minimal incremental capital expenditure" | Not started |
| Safety strengthening | Low | none stated | No metric |

## 6C Metrics showcased and missing
Showcased: segment growth percentages, subsidiary PAT and revenue in Mn, macro indicators. Conspicuously absent in AR26: EBITDA or margin numbers, ROCE, debt, capex amounts, capacity and utilisation (only the wire-rod 18,000 MTPA), order books, volumes, working-capital days, insurance recovery status, and customer concentration (the notes say only "No customer represents more than 10% of the total trade receivables balance", S p.140).

## 6D Tone and priority drift against AR25
AR25 gave quarterly growth rates (Q4 powders +25%, foils +89%, conductors +39%), a market-size section, a named foil supplier and a capacity number (AR25 p.18). AR26 keeps growth rates but drops the capacity, supplier and market-size numbers, and adds fire detail and FY27 growth targets. The tone moves from capacity-led to product-led.

## 6E Quiet Abandonment Check
| # | Opening claim | Where it should appear | Class | Materiality |
|---|---|---|---|---|
| 1 | AR25: "Phase III capacity expansion of 2,500 MTPA (Pyro and Flake) ... fully operational by the end of Q2FY26" (AR25 p.18) | AR26 Board's Report powders section (p.25-26) and MD&A. Not mentioned at all | (b) silent drop | Medium. It is the capacity base for the powder growth guide of 13 to 15% |
| 2 | MD&A: MCPL "is implementing a Greenfield manufacturing facility for Low Voltage Power Cables (LVPC) and Covered Conductors ... executed in phases" (AR26 p.54) | Board's Report MCPL update (p.30-31) covers only the wire rod. The LT cable item is described as a "strategic pilot ... at the Bhandara facility", which is a Parent plant (p.26). MCPL's Kotak loan of 3,188 L is for "factory building and ... plants and machinery" with instalments from March 2027 (C p.205) | (c) hedged retreat: the greenfield LVPC plant becomes a parent pilot with no scale-back named | High: MCPL guarantee 3,288 L and capex commitments are tied to it |
| 3 | AR25: MEPL "full capacity by end of FY 25-26" (AR25 p.18) | AR26: "meaningful sales ramp up from Q3FY27 onwards" (p.30) | (c) hedged retreat | High: the first proof gate for the transition |
| 4 | MD&A p.54: wire-rod backward integration "expected to improve ... margins" | Board's Report p.30: machinery installation from July 2027, plant trials H2 FY27 (conflict) | (c) hedged retreat on timing | Medium |
| 5 | AR25: "A detailed investigation is currently underway to determine the root cause of the explosion" (AR25 p.143) | AR26 reports no root cause and no inspector finding (p.25; S p.159) | (b) silent drop | Medium: safety and liability |
| 6 | Board's Report p.26 says MAPL was formed "to strengthen business integration" | MD&A lists no MAPL activity; "The company is not functional yet" (p.31); 25.00 L capital | (b) silent drop | Low |
| 7 | "Zero Accident" goal (p.52) | Seven deaths (p.25), no review of the goal | (a) implicit retraction | Medium |
**Phase 6 Verdict: YELLOW.** The front matter claims progress; the operating sections show slippage on the transition items without naming it.

---------------------------------------------------------------

# PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION
| Strategy | Call | Top reasons |
|---|---|---|
| GARP (fullest) | WATCHLIST | (1) Growth is revenue, not earnings: revenue CAGR FY22 to FY26 16.4% against PAT CAGR 1.7% (screener, INR Cr 448.26 to 824.00 and 28.99 to 31.01, derived). (2) Valuation: screener shows price 449.6 and market cap 1,142.1 Cr (capture date NOT FOUND), about 36.8x C PAT of 31.01 Cr and about 26.9x if the 11 to 12 Cr fire PAT hit is added back (derived). The FY26 year-end price in the same sheet is 189.11, so the price is up 137.7% if 449.6 is current. (3) Recovery proof: Q3 FY26 to Q1 FY27 operating margin 8.7% to 8.9% against 9.22% in FY25 |
| Turnaround (fullest) | WATCHLIST | (1) The "transition" is the climb from powder converter (segment return on assets 18.4%) into electrical products. MEPL return on segment assets is (9.4%) on revenue of 231.94 L (C p.226-227). (2) The proof gate (MEPL ramp from Q3 FY27, AL59 conductor traction H1 FY27) has not fired. (3) Funding runs on short-term debt and guarantees. Not a classic turnaround: the core is not loss-making |
| Value + Quality | FAIL | ROCE 10.12%, ROE 9.26%, both down about 3.5 to 4 points (C p.224); FCF negative; net debt / EBITDA 2.75x |
| Capex-Led Growth | WATCHLIST | Capex 4.9x depreciation (derived); commitments 5,642.27 L; incremental ROCE not yet visible and conductors margin fell |
| Cash Flow Compounder | FAIL | 10-year CFO less investing is (20.39) Cr (screener); FY26 FCF (231.53) L |
| Contrarian | FAIL on price | If 449.6 is current, the stock sits well above its FY26 year-end level; date NOT FOUND |
| Insider Confidence | WATCHLIST | 74.49% promoter, no pledge, flat; promoters give guarantees and take 378.43 L of dividends; no open-market buying data in the corpus |
| Guidance Divergence | WATCHLIST | Powders guided low and beat; conductors guided high and missed; MEPL slipped; FY27 targets quantified for three of five lines |
**Best fit: WATCHLIST on the transition (GARP and Turnaround overlap). No strategy passes.**

---------------------------------------------------------------

# PHASE 8: FINAL VERDICT DASHBOARD

## Company snapshot
| Item | Value |
|---|---|
| Business | Aluminium powder and paste (61% of revenue), foils (26%), conductors (12%), new insulator business (0.3%) (S p.132; C p.226) |
| Revenue FY26 | S 82,168.59 L, C 82,400.49 L, +18.8% |
| PAT FY26 | S 2,642.94 L, C 3,100.93 L, -20.2% |
| Net debt / EBITDA | 2.75x (derived) |
| Rating | CRISIL BBB+/Stable, A2 (AR26 p.29) |
| Promoter | 74.49%, no pledge |
| Price | 449.6, market cap 1,142.1 Cr (screener, capture date NOT FOUND) |

## Phase verdicts
| Phase | Verdict |
|---|---|
| 1 Auditor and CARO | YELLOW |
| 2 Notes | YELLOW |
| 3 Financials | YELLOW |
| 4 Risk and MD&A | YELLOW |
| 5 Governance | YELLOW |
| 6 Front matter | YELLOW |
| 7 Best fit | WATCHLIST (transition) |

## Overall quality score
| Component (25% each) | Score /10 | Basis |
|---|---|---|
| Governance | 5 | Unpledged 74.49%, no fraud, small RPTs; executive promoter on Audit Committee, thin audit fee, attendance, AOC-1 and CSR errors |
| Accounting quality | 6 | B02 score, unchanged after verification |
| Balance sheet | 5 | D/E 0.53, ND/EBITDA 2.75x, 76.6% short-term debt, DSCR 2.51, 6,688 L guarantees, BBB+ |
| Earnings quality | 5 | ROCE 10.12%, FY25 stock-build lift, 26.5% of PAT from non-cash associates, borrowed CFO |
| **Overall** | **5.25 of 10** | |

## Top 3 strengths
1. Revenue +18.8% through a 50-day plant stop, exports +66.8%, powders +15.0% against single-digit guidance (S p.132; AR25 p.18).
2. Trade receivables clean (96.3% not due, 1.18% over six months, B02), no covenant breach, no default, no pledge.
3. Full recognition of the fire loss, and a segment note that shows which lines earn and which do not (C p.226-227).

## Top 3 red flags
1. Funding of subsidiary capex: S cash 56.38 L, guarantees 6,688 L, commitments 5,642.27 L against 3,126.32 L undrawn, 76.6% of debt due inside a year.
2. Earnings and cash quality: 68.2% of CFO is borrowing plus payables; the margin fall is wider than the fire explains (Q2 FY26 6.85%); associates carry 26.5% of PAT with 9.98 L of dividend.
3. Disclosure and guidance reliability: AOC-1 does not tie to the C statements, wire-rod dates conflict, the insurance claim is 47.4% of a "fully insured" loss, and MEPL slipped about three quarters.

## Key monitorables
| Metric | Threshold | Where | Why |
|---|---|---|---|
| Insurance receipt against 793.05 L | At least 80% (634 L) received by 31 Mar 2027 | Other current financial assets, Q2 and Q3 FY27 notes | A write-down would hit exceptional items |
| MEPL (Insulators segment) revenue and result | One quarter above FY26 full-year revenue (231.94 L) by Q4 FY27; quarterly loss under 80 L (one quarter of the (329.13) L annual loss) | Segment note, quarterly results | Proof gate for the transition |
| Quarterly operating margin | At or above 8.7% for three straight quarters; FY25 base 9.22% | Quarterly results | Separates fire and stock-build readings |
| Conductors segment margin | At or above 8.27% (FY25) | Segment note | G3 miss |
| CFO net of borrowing and payables / EBITDA | Above 50% (FY26 25.6%) | Cash flow, Notes 23-24 | Cash quality |
| Year-end payable days | Not above 24.8 | Note 24, Note 43 | Stretch check |
| Gross debt, DSCR, ND/EBITDA | Debt at or below 18,452.46 L; C DSCR at or above 2.5; ND/EBITDA at or below 3.0x | Note 18, Note 43 | Funding stress |
| Subsidiary reimbursement closing balances | Disclosed; MCPL 471.75 L expected | RPT note | Hidden parent funding |
| Star dividend and share of profit | Dividend above 9.98 L; associate profit under 20% of PBT | C Notes 46 and 49 | Cash backing of associate profit |
| Wire-rod and LVPC timeline | One consistent date set | Board's Report, Q2 FY27 presentation | Resolves G11 |
| Fire legal items | Any compensation, inspection or prosecution disclosed | Contingent liabilities | None disclosed against 7 deaths |

## One-line verdict
Best fit is a WATCHLIST on the transition: revenue and exports grew, but earnings fell 20%, cash conversion leans on borrowing and payables, and the electrical-products climb has not yet shown revenue or margin.

---------------------------------------------------------------

# ANCHOR INDEX FOR STAGE 5 (no-concall mode, open only these pages)
| Need | Pages in Annual_Report_2026.txt |
|---|---|
| FY26 delivery by segment, fire statement, FY27 guidance | p.25-26 |
| Subsidiary status (MEPL ramp, MCPL wire rod, Star, Toyal) | p.30-31 |
| MD&A (qualitative only; expansion, exports, threats) | p.49-55 |
| FY26 guidance as given a year earlier | Annual_Report_2025.txt p.18, p.22, p.24, p.143 |
| Working capital: inventory, receivables, payables | S p.120-121 (Notes 10-11), p.130 (Note 24), p.143-144 (Notes 41-42), p.145 and C p.224 (Note 43) |
| Cash flow | S p.95-96, C p.173-174 |
| Segment revenue, result, assets, capex (KPI table) | C p.225-228; S p.132 (Note 29) |
| Debt, security, schedules | S p.126-130; C p.204-205, p.220 |
| Capex commitments and guarantees | S p.157; C p.241 |
| Fire note | S p.122, p.133-136, p.159 |
| RPT | S p.150-154; AR26 p.38-39; C p.197, p.238 |
| Governance and Audit Committee | AR26 p.57-58, p.63-67 |

```yaml
stage: B03-ardeep
company: "MMP"
run_date: "2026-10-04"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "B00 CORPUS GAPPED: screener P&L, Quarters, Balance Sheet, Cash Flow, Customization sheets are empty (no CSV); Data_Sheet.csv only (used here for FY17-FY26 and quarterly margins)"
  - "B00: scanned Q4 FY26, Q3 FY26 and FY26 audited results are image scans with no OCR; not used in this stage (AR FY26 text used)"
  - "B00: ARFIN transcripts absent; peer transcripts only APARINDS and MAANALU; no-concall mode (concalls May 2026 and Jul 2022 only)"
  - "B00: NSE results clarifications of 2026-03-05 and 2026-06-23 have no company reply in the corpus"
  - "B00: announcements and shareholding repaired by hand; selection, not full list; collector warnings on BSE scrip code, empty research/ and prospectus/"
  - "Stage-level NOT FOUND: insurer acceptance and receipt of the 793.05 L claim, business-interruption claim, fire root cause and inspector findings, auditor names of Star and Toyal, statutory auditor tenure before 2022, CEO-to-median pay multiple, Risk Management and Project Monitoring Committee meeting counts, volume-versus-price split of powder growth, installed capacity (AR26 gives none), Phase III 2,500 MTPA status, capitalised interest, date of screener price 449.6, first appointment date of Bapna and Khanna, reason for their 10 Aug 2026 resignations"
flags:
  - {type: FLAG-CASH, reason: "C CFO 5,328.97 L includes 1,723.34 L short-term borrowing and 1,909.56 L payables build (68.2% of CFO); CFO net of both 1,696.07 L against gross capex about 5,560.50 L; payable days 24.8 vs 17.8; FCF (231.53) L (C p.173-174; S p.130; derived)"}
  - {type: FLAG-FIRE-RECOVERY, reason: "AR25 p.24 says loss 150-200 Mn 'fully insured'; AR26 recognises 793.05 L of 1,672.01 L (47.4%), nil received; KAM gives no insurer-acceptance conclusion; Note 14 and Note 52 give different bases (S p.122, p.159, p.83)"}
  - {type: FLAG-FUNDING, reason: "S cash 56.38 L; guarantees 6,688 L (22.0% of NW); commitments C 5,642.27 L vs undrawn subsidiary lines 3,126.32 L (B02); 76.6% of C debt due within a year; parent 7.00% preference into MEPL against about 8.6% own borrowing cost (S p.119, p.157; C p.220, p.241)"}
  - {type: FLAG-DISCLOSURE-INTEGRITY, reason: "AOC-1 subsidiary totals and PAT (25.77 L combined loss) do not tie to C statements (Insulators result (329.13) L, subsidiary assets 4,618.90 L); four CSR totals; wire-rod dates conflict (installation July 2027, trials H2 FY27); Board says 17.29 Cr vs Note 52 16.72 Cr (AR26 p.30, p.37, p.25; S p.159)"}
phase_verdicts: {p1: "YELLOW", p2: "YELLOW", p3: "YELLOW", p4: "YELLOW", p5: "YELLOW", p6: "YELLOW", p7_best_fit: "WATCHLIST (transition, GARP and Turnaround overlap; no strategy passes)"}
overall_quality: 5.25
quality_components: {governance: 5, accounting: 6, balance_sheet: 5, earnings: 5}
kill_switch_notes:
  - "P1: no reason to stop; unmodified opinion and clean CARO; yellow for fire KAM without a stated conclusion, other-auditor reliance on 820.78 L associate profit, audit fee 3.44 L"
  - "P2: no reason to stop; totals tie; recovery, funding and AOC-1 items need operator attention"
  - "P3: no reason to stop; BBB+/Stable and solvent; cash conversion rests on borrowing and payables"
  - "P4: no reason to stop; guidance partly delivered; MD&A has no financial numbers and wire-rod dates conflict"
  - "P5: no reason to stop; no pledge or selling; executive promoter joins Audit Committee, two committee chairs rotated on 10 Aug 2026"
  - "P6: no reason to stop; transition items slipped without being named (MEPL ramp, LVPC greenfield, Phase III)"
triple_pass_verification:
  verified: 12
  discrepancies:
    - {finding_rank: 3, triple_pass_value: "fire inventory removed from EBITDA 583.03 L (17.87 + 39.16 + 526.00)", ar_value: "Note 52 inventory loss 671.45 L; gap 88.42 L not located (stores and spares in other expenses or slip)", note_ref: "S Note 31-32 p.133-134; S Note 52 p.159"}
    - {finding_rank: 4, triple_pass_value: "Star described as a listed associate", ar_value: "Star CIN U24110MH1974PLC017301 = unlisted; OCI (168.32) Star vs (167.96) group is consistent", note_ref: "AR26 p.31; C p.172, p.238"}
    - {finding_rank: 8, triple_pass_value: "liens 2,545.72 L vs term deposits 242.24 L", ar_value: "2,000 L is the borrowing secured, 445.72 L is the BG amount (equals Note 47a), Federal Bank deposit lien is 100 L; deposits 242.24 L confirmed; no lien-over-deposit contradiction", note_ref: "S Note 7 p.120; Note 14 p.122; Note 23d p.130; Note 47 p.157"}
missing_risks:
  - {risk: "Subsidiary funding and guarantee exposure not in MD&A threats", evidence: "guarantees 6,688 L (S p.157); commitments C 5,642.27 L (C p.241); parent cash 56.38 L (S p.96)"}
  - {risk: "Insurance recovery gap: 'fully insured' became 47.4% claim, nil received", evidence: "AR25 p.24; S p.122, p.159"}
  - {risk: "Promoter and key-person dependence: MD and WTD age 70, personal guarantees, promoter-company mortgage", evidence: "AR26 p.6-7; S p.126-127; C p.205"}
  - {risk: "Foil raw-material supplier dependence (Hindalco named in AR25, absent in AR26)", evidence: "AR25 p.18; AR26 p.26"}
  - {risk: "Cash conversion rests on supplier credit and working-capital borrowing", evidence: "S p.95, p.130; C p.173"}
  - {risk: "Associate profit non-cash, 26.5% of C PAT, Star unlisted and promoter-linked", evidence: "C p.172, p.238; AR26 p.31"}
  - {risk: "Legal and regulatory aftermath of 7 fatalities not disclosed (no contingent liability, no root cause)", evidence: "AR26 p.25; S p.157; AR25 p.143"}
  - {risk: "Disclosure control: AOC-1, CSR and date inconsistencies", evidence: "AR26 p.37, p.40-42; S p.122"}
guidance_table:
  - {claim: "Powders FY26 single-digit growth", number: "single digit; delivered +15.1% (S p.132)", timeframe: "FY26 (AR25 p.18)", credibility: "high, conservative"}
  - {claim: "Powders Phase III 2,500 MTPA fully operational", number: "2,500 MTPA", timeframe: "end Q2 FY26 (AR25 p.18)", credibility: "untestable, AR26 silent (NOT FOUND IN DOCUMENT)"}
  - {claim: "Conductors positive momentum with further improved margins", number: "delivered +3.4% revenue, margin 4.86% vs 8.27% (C p.226)", timeframe: "FY26 (AR25 p.18)", credibility: "low, missed"}
  - {claim: "MEPL Phase I commercial production and full capacity", number: "Q2 FY26 start, full capacity end FY26; delivered revenue 231.94 L, loss (329.13) L", timeframe: "FY26 (AR25 p.18, p.22; AR26 p.30, p.53)", credibility: "mixed, ramp about three quarters late"}
  - {claim: "Fire loss 150-200 Mn, fully insured", number: "loss 1,672.01 L inside range; claim 793.05 L = 47.4%", timeframe: "FY26 (AR25 p.24; S p.159)", credibility: "quantum good, insurance claim not borne out"}
  - {claim: "Powders FY27 revenue growth with higher EBITDA margin", number: "+13% to 15%", timeframe: "FY27 (AR26 p.26)", credibility: "medium-high on revenue, margin unproven"}
  - {claim: "Exports growth in FY27", number: "+50%", timeframe: "FY27 (AR26 p.26)", credibility: "medium; FY26 exports +66.8%"}
  - {claim: "Foils FY27 growth and margin improvement; Security Printing and Lidding Foil launches", number: "+15% revenue; launches early Q3 FY27", timeframe: "FY27 (AR26 p.26)", credibility: "medium; margin claim soft (FY26 2.00% vs 1.96%)"}
  - {claim: "MEPL sales ramp", number: "meaningful ramp", timeframe: "from Q3 FY27 (AR26 p.30)", credibility: "medium, slipped once"}
  - {claim: "MCPL wire rod 18,000 MTPA", number: "installation from July 2027 and plant trials H2 FY27 (dates conflict)", timeframe: "FY27 to FY28 (AR26 p.30)", credibility: "unreliable until dates clarified"}
monitorables:
  - {metric: "Insurance receipt against 793.05 L", threshold: "at least 80% (634 L) received by 31 Mar 2027", where: "other current financial assets, Q2/Q3 FY27 notes", why: "write-down would hit exceptional items"}
  - {metric: "Insulators segment revenue and result", threshold: "one quarter above FY26 full-year 231.94 L by Q4 FY27; quarterly loss under 80 L", where: "segment note, quarterly results", why: "transition proof gate"}
  - {metric: "Quarterly operating margin", threshold: "at or above 8.7% for three straight quarters (FY25 base 9.22%)", where: "quarterly results", why: "separates fire and stock-build readings"}
  - {metric: "Conductors segment margin", threshold: "at or above 8.27% (FY25)", where: "segment note", why: "FY26 guidance miss"}
  - {metric: "CFO net of borrowing and payables / EBITDA", threshold: "above 50% (FY26 25.6%)", where: "cash flow, Notes 23-24", why: "cash quality"}
  - {metric: "Year-end payable days", threshold: "not above 24.8", where: "Note 24, Note 43", why: "payables stretch"}
  - {metric: "Gross debt, DSCR, ND/EBITDA", threshold: "debt at or below 18,452.46 L; DSCR at or above 2.5; ND/EBITDA at or below 3.0x", where: "Note 18, Note 43", why: "funding stress"}
  - {metric: "Subsidiary reimbursement closing balances", threshold: "disclosed; MCPL 471.75 L expected", where: "RPT note", why: "hidden parent funding"}
  - {metric: "Associate profit share of PBT and Star dividend", threshold: "under 20% of PBT; dividend above 9.98 L", where: "C Notes 46 and 49", why: "cash backing"}
  - {metric: "Wire-rod and LVPC timeline", threshold: "one consistent date set", where: "Board's Report, Q2 FY27 presentation", why: "resolves date conflict"}
ar_new_downstream_entities:
  - {name: "MMP Cables Private Limited", where_in_ar: "RPT note S p.152-154 (reimbursements 1,139.54 L, equity 500 L); C Note 18 p.205 (Kotak term loan, guarantee 3,288 L)", entity_type: "wholly owned subsidiary and RPT counterparty; first appears in financials this year"}
  - {name: "MMP Alutech Private Limited", where_in_ar: "S p.153 (loan received 24.00 L, repaid 20.40 L; equity 25.00 L); AR26 p.31 ('not functional yet')", entity_type: "wholly owned subsidiary and RPT counterparty"}
  - {name: "Kotak Mahindra Bank Limited (as lender to MCPL, term loan 3,188 L sanctioned, 512.70 L drawn)", where_in_ar: "C Note 18 p.205; S Note 47 p.157", entity_type: "lender and guarantee beneficiary for a subsidiary"}
  - {name: "AVL Metal Powders (technology and sales partner for AAC grade powder, 'four decade old')", where_in_ar: "Annex D, AR26 p.43; not in AR25 text", entity_type: "technology and sales partner"}
  - {name: "NOT NAMED: Nepal commercial customer for MEPL insulators", where_in_ar: "Board's Report p.30", entity_type: "export customer, unnamed"}
  - {name: "NOT NAMED: prospective United States customers for MEPL", where_in_ar: "Board's Report p.30", entity_type: "export prospects, unnamed"}
strengths_top3:
  - "Revenue +18.8% through a 50-day Umred stop; exports +66.8%; powders +15.0% against single-digit guidance (S p.132; AR25 p.18)"
  - "Trade receivables clean (96.3% not due), no covenant breach, no default, promoter 74.49% unpledged (B02; NSE SHP 30 Jun 2026)"
  - "Fire loss recognised in full and segment note shows which lines earn (C p.226-227)"
red_flags_top3:
  - "Funding of subsidiary capex: S cash 56.38 L, guarantees 6,688 L, commitments 5,642.27 L vs 3,126.32 L undrawn, 76.6% of debt due within a year"
  - "Earnings and cash quality: 68.2% of CFO is borrowing plus payables; margin fall wider than the fire explains; associates 26.5% of PAT with 9.98 L dividend"
  - "Disclosure and guidance reliability: AOC-1 does not tie, wire-rod dates conflict, claim is 47.4% of a 'fully insured' loss, MEPL ramp slipped about three quarters"
best_fit_strategy: "WATCHLIST on the transition (GARP and Turnaround overlap); no strategy passes"
one_line_verdict: "Revenue and exports grew, but PAT fell 20%, cash conversion leans on borrowing and payables, and the electrical-products climb has not yet shown revenue or margin: WATCHLIST."
analyst_note: "No Chairman's letter exists; the MD&A (p.49-55) has no company numbers, so stage 5 must read Board's Report p.25-26 and p.30-31 for guidance. Three corrections to B02: (1) the lien-exceeds-deposit finding is a reading error (2,000 L and 445.72 L are the obligations secured; the real deposit lien is 100 L); (2) Star Circlips is unlisted; (3) Note 52 inventory loss is 671.45 L, 88.42 L above what Notes 31-32 move out of EBITDA, so fire-inclusive EBITDA is 7.23% to 7.33%. The margin story has two readings: fire plus start-up drag, or a FY25 base lifted by a 2,069.76 L stock-build credit (45% of FY25 S PBT). Q2 FY26 operating margin of 6.85% (screener) supports the second. Separator: Q3 and Q4 FY27 margin and the Insulators segment ramp. AOC-1 conflicts with the C statements. Screener price 449.6 versus FY26 year-end 189.11 has no capture date."
```
