# STAGE 2, FINAL: NOTES TO FINANCIAL STATEMENTS, PASS 3 AND CONSOLIDATION
Company: MMP Industries Ltd (MMP) | Run date: 2026-10-04 | Source: inputs/annual-report/Annual_Report_2026.txt (FY2025-26); comparatives Annual_Report_2025.txt
Detail for every item is in outputs/reports/02-notes-pass1.md and 02-notes-pass2.md. This file holds Pass 3 and the consolidation.

## CONVENTIONS
- UNIT: INR Lakhs (L), as printed ("Amount in Rs in Lakhs"). Nothing converted. Stage 10 converts once. "Rs Cr" appears only where the Directors' report prints it.
- Anchors: S = standalone notes, C = consolidated notes, p.N = "[page N]" marker in the .txt (printed page = N minus 5). "(derived)" = my arithmetic on anchored inputs.
- Ratings in words: GREEN, YELLOW, RED.
- B00 carried: CORPUS GAPPED, no_concall_mode true, sector cap row "Cables / Industrial products". Gaps are listed in the YAML block.

## PASS 3: PATTERN PASS
Method: contradiction scan, tie-out scan, vagueness scan, restatement scan, events after balance sheet, going concern. I re-checked the AR text for the fire, Note 43, the cash flow and the going concern language. Load-bearing facts LBF1 to LBF4 checked first.

### P3-1 Reported EBITDA is before the fire inventory loss (LBF1, LBF2). YELLOW
- The fire-destroyed inventory is taken out of cost of materials (RM 17.87 L, PM 39.16 L; S Note 31 p.133-134) and out of change in inventories (526.00 L; S Note 32 p.134, footnote). Together 583.03 L (derived). The "(Increase)/Decrease in Inventories" credit of 555.60 L therefore contains 526.00 L that is the fire reclass. Underlying FG and WIP build is 29.59 L (9,670.90 less 9,641.31).
- The loss lands in exceptional (S Note 37 p.135) after the insurance claim of 793.05 L, and not in EBITDA.
- C EBITDA with the 583.03 L charged: 6,626.71 - 583.03 = 6,043.68 L = 7.33% of C revenue 82,400.49 L (derived), against 8.04% reported and 9.38% in FY25. That is a 205 bps fall on a fire-inclusive basis (derived), not 133 bps.
- Lost production and sales in Q1 FY26 stay inside EBITDA. The Directors' report (outside the notes, p.27) estimates revenue loss at Rs 45 to 50 Cr and net EBITDA impact at Rs 7 to 8 Cr. Rs 7 to 8 Cr = 700 to 800 L = about 64% to 73% of the 133 bps fall (derived: 133 bps x 82,400.49 L = 1,096 L). The remaining 296 to 396 L (27% to 36% of the fall, derived) is not explained by the fire in the document. The basis of the Rs 7 to 8 Cr estimate and whether it includes the 583.03 L: NOT FOUND IN DOCUMENT.
- Business-interruption (loss of profit) claim: NOT FOUND IN DOCUMENT. A search of the AR for "loss of profit", "business interruption" and "consequential" found only an unrelated consequential-amendments phrase.
- Two readings: (a) the fire explains most of the margin fall and FY27 margin recovers with a full year of Umred; (b) FY25 margin was lifted by a 2.99% stock-build credit and subsidiaries add 50 bps of start-up drag, so the clean base is lower. Separating observation: Q1 to Q4 FY26 gross margin and FG/WIP by quarter, which are outside the notes.

### P3-2 Note 43 ROCE wording: Pass 1 finding softened (LBF1). GREEN
- Pass 1 flagged that Note 43 blames the fire for the ROCE decline though ROCE excludes exceptional items. Re-read: the S footnote (a) cites the fire only for Return on Equity and Net Profit Ratio (S p.145). ROCE is 10.60% vs 13.62% (-22.17%) on "profit before interest, exceptional items and tax". The C footnote does name ROCE (C p.224).
- Lost production sits in EBITDA and so reaches ROCE legitimately. The contradiction is weaker than Pass 1 said. Remaining point: the C footnote does not separate the fire from the 50 bps of subsidiary drag.

### P3-3 Cross-note contradictions, consolidated (LBF2, LBF4). YELLOW
| Pattern | Note A | Note B | Effect |
|---|---|---|---|
| Fire date | Note 14 footnote "April 11, 2026" (S p.122; C p.200) | Notes 32, 37, 52 "April 11, 2025" | Typo in the note that carries the 793.05 L receivable |
| Claim recognition | S Note 32 footnote: "expected insurance claim has been recognized" | S Note 1.6(d) p.114: contingent assets "neither recognised nor disclosed"; Note 1.4(r): disclosed where inflow probable | Basis for 793.05 L is management's view of a claim bill; surveyor outcome not stated |
| Hedging | S Note 39B p.140 "has not entered into any hedging" (C p.218 "has entered") | S Note 51 p.158: forwards 1,979.34 L; MTM payable 57.02 L | Three labels (FVTPL, cash flow hedge, debt-instrument OCI) |
| Liens | S Note 7 p.120: 2,000 L collateral with Federal Bank | Term deposits on balance sheet 242.24 L | Liens 2,545.72 L cannot be met from disclosed deposits |
| Repayment terms | Axis loan monthly (S) vs quarterly (C); Citi ends Dec 2028 (S) vs Mar 2028 (C); MEPL loan "monthly" then "quarterly" | | Schedule not reliable |
| Maturity table | C Note 39B nil over 5 years | MEPL loan to Mar 2032, MCPL to Mar 2033 (C Note 18 p.205) | Table also over-adds 54.00 L |
| Gratuity | Note 44 text: contributes to a separately administered fund | Table: unfunded, plan assets nil | Expected contribution 54.15 L |
| Schedule III | C Note 50 FY26 total 34,004.81 L | C equity 34,650.78 L (Note 39C) | 645.97 L gap equals Toyal carrying value |
| FX position | Note 39B EUR liabilities 13.76 / assets 7.33 lakh | Note 51 unhedged payable 0.08 / receivable 2.47 lakh | Opposite signs |
| Cash flow policy | S Note 1.4(u): adjusts profit "excluding exceptional items" | CF starts from PBT after exceptional 3,668.13 L | Presentation inconsistency |

### P3-4 Tie-outs to the primary statements (LBF2, LBF4). YELLOW
- Note 2 net block derecognised 460.28 L (595.77 cost less 135.49 depreciation). Fire PPE loss 338.92 L plus disposal loss 32.53 L = 371.45 L. Cash flow add-back 23.45 L. "Investment in PPE (Net of Disposal)" 2,899.94 L vs additions 3,336.76 L, a 436.82 L offset (Pass 2, P2-1). The statement does not show whether this offset is disposal proceeds or netting of non-cash losses.
- Parent subsidiary receivable: S Note 14 shows "Receivables from Wholly Owned Subsidiary" 234.97 L at 31 Mar 2025 and nil at 31 Mar 2026. Pass 1 used 228.85 L from the RPT table. Rolling forward with the Note 14 figure: 234.97 + 192.49 - 312.46 = 115.00 L for MEPL; MCPL 471.75 L; total about 587 L (derived), against Pass 1 about 581 L. Either way no closing balance is visible. Conversion to equity or preference shares is not stated.
- Reported totals tie in every case checked (balance sheet to Note 39C equity, C PBT, EPS, current tax). The errors sit in supporting tables.

### P3-5 Deliberately vague or thin disclosure. YELLOW
- Fire: loss amounts are precise, but number of deaths, insurer acceptance, interim payments, debris proceeds and any BI claim are absent. A fire with fatalities carries no contingent liability line for compensation, legal action or Factory Act proceedings (S Note 47).
- Other receivables 703.86 L at 40.2% reserve: nature, debtor and age absent.
- Interest income on amortised-cost assets +155% to 33.25 L with no composition.
- Non-deductible expenses implied about 444 L with no description.
- Related-party arm's-length statement without a method; role of two promoter-family salaried relatives not stated.
- Impairment: no CGU assumptions; subsidiaries carried at cost with MEPL cumulative loss 347.72 L (about 70% of its 500 L cash equity).
- Detail is rich where it is mechanical (ageing, gratuity maturity, MSME) and thin where it is judgemental (recovery, impairment, RPT pricing).

### P3-6 Restatements and reclassifications. GREEN
- FY25 comparatives differ from AR2025 by under 2 L (S total assets 50,553.98 vs 50,554.05; MSME payables 833.86 vs 832.28; others 1,878.78 vs 1,880.42). S Note 56 states previous figures are regrouped. No material restatement. The FY25 loss on disposal 11.37 L (Note 36) vs cash flow surplus (0.17) L is a tie error, not a restatement.

### P3-7 Events after the balance sheet date and going concern. GREEN
- Events: only the board's dividend recommendation of 23 May 2026 (S Notes 17, 50). No insurance receipt, drawdown, litigation or covenant event is disclosed. Policy 1.4(t) p.112 is boilerplate.
- Going concern: no material uncertainty. The only text is the capital management objective (S Note 39C p.142) and boilerplate. The Directors' report states no order of any court or tribunal impacts going concern. Covenants complied with throughout (S Note 39C p.142). No default (S Note 46 p.156).
- PASS 3: material new findings exist (P3-1, P3-4 range, P3-5 pattern list). pass_3_empty is false.

---------------------------------------------------------------
# CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES

## A. TOP 15 FINDINGS BY INVESTOR IMPORTANCE
| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Umred fire: gross loss 1,672.01 L; claim receivable 793.05 L (47.4%) booked on a claim bill, nil received, acceptance not shown; net exceptional 878.96 L (18.9% of S pre-exceptional PBT) | S 14, 32, 37, 52 (p.122, 134-136, 159); S 1.6(d) p.114 | YELLOW | Recovery unproven and 14.1x S cash (derived); sits against own contingent-asset policy |
| 2 | S CFO 5,438.30 L includes 789.11 L borrowing increase; ex-borrowings 4,649.19 L vs 1,121.30 L (66% vs 17% of EBITDA); payables +70.2%; CF PPE add-back 23.45 L vs 371.45 L losses | S CF p.95; S 2, 24, 36, 52 | YELLOW | LBF4: conversion rests on payables and a cash flow that does not tie |
| 3 | EBITDA is before 583.03 L fire inventory loss; C margin 8.04% vs 9.38%, about 7.33% with the loss (derived); parent -83 bps, subsidiaries -50 bps; stock-build credit 0.68% vs 2.99% | S 31-36; C 36; S 52 | YELLOW | LBF1: margin fall wider than headline; Directors' report puts fire EBITDA hit at Rs 7 to 8 Cr (outside notes) |
| 4 | Associate profit 820.78 L = 20.5% of C PBT, 26.5% of PAT; Star 90.5%; dividend 9.98 L; Star OCI (168.32) L; Star holds 4.56% of MMP; Toyal 2,551 L moved to current | C 46, 49; S 16, 45 | YELLOW | LBF3: non-cash, concentrated earnings |
| 5 | Guarantees 6,688 L = 22.0% of net worth; MEPL 11.2%, MCPL 10.8%; commitments S 3,278.31 L, C 5,642.27 L vs undrawn subsidiary lines 3,126.32 L and liquidity 298.62 L | S 47, 48; C 18, 52; S 39B | YELLOW | LBF4: funding and guarantee risk of new capex on the parent |
| 6 | Group debt 18,452.46 L (+18.1%); C DSCR 2.51 vs 4.55; ND/EBITDA 2.75x vs 2.24x (derived); S cash 56.38 L | S 39B, 43; C 18, 43 | YELLOW | Cover weakens as capex ramps |
| 7 | Subsidiary losses 352.81 L; Insulators (329.13) L on 231.94 L revenue; DTA 125.62 L; no impairment test | C 4, 20, 44, 50 | YELLOW | Start-up drag and DTA realism |
| 8 | Liens 2,545.72 L vs term deposits 242.24 L; liquidity is margin money | S 7, 14, 23d, 39B | YELLOW | Cushion overstated or text wrong |
| 9 | Other receivables 703.86 L at 40.2% reserve; 77% of credit-loss charge | S 7, 11, 36 | YELLOW | Receivable risk outside clean trade ageing |
| 10 | Promoter family and entity payments 255.21 L (5.5% of pre-exceptional PBT); promoter collateral and guarantees; 280 L interest-free promoter loans; about 587 L reimbursement flows with no closing balance | S 18, 45; C 18, 23, 46 | YELLOW | LBF3: scale small, disclosure thin |
| 11 | Gratuity DBO +75% to 611.39 L, unfunded; 94.73 L Labour Code exceptional; salary base +68.7% vs headcount +8.0% | S 37, 44 | YELLOW | Unfunded liability with unexplained input |
| 12 | Hedge trail: three labels, 57.02 L MTM vs 10.12 L OCI, 39B vs Note 51 contradiction | S 1.4(h), 25, 39A, 39B, 51 | YELLOW | Incomplete derivative trail; small rupee size |
| 13 | Supporting tables do not tie: Schedule III 645.97 L; maturity table +54 L; Note 2 vs cash flow | C 50, 39B; S 2, CF | YELLOW | Lowers confidence in notes precision |
| 14 | Segment returns: foils 3.2%, conductors 13.7% (21.1% PY), insulators (9.4%), powder 18.4% | C 44 | YELLOW | Mix and capital intensity behind margin |
| 15 | Clerical slips (fire date 2026, wrong table headers, 70 bps on total debt, names) | various | GREEN | Disclosure transparency only |

Strengths (GREEN): trade ageing 96.3% not due, over 6 months 1.18% (S Note 41 p.143); no FY26 write-offs; MSME dues paid on time (S p.130); no covenant breach, default or going concern doubt; no tax disputes disclosed; no ESOP or dilution; CSR spent 68.60 L (S Note 49); Toyal sales 2.19% of revenue; no loans to promoters; loss recognition on the fire taken in full.

## B. ACCOUNTING QUALITY SCORE: 6 of 10
| Dimension | Score | Basis |
|---|---|---|
| Revenue recognition conservatism | 7 | Point in time at dispatch or delivery; rebates fell to 97.40 L from 381.41 L with no reason; export incentives inside revenue (S Note 29) |
| Expense capitalisation honesty | 6 | Overhead capitalisation allowed; capitalised interest NOT FOUND; pre-operative 210.64 L; plant lives 25 y at long end (S Note 1.4(a)) |
| Provisioning adequacy | 6 | Trade ECL 0.7% with clean ageing; other receivable reserve rising to 40.2%; no litigation provisions; gratuity unfunded; claim receivable booked at 47% of loss |
| RPT fairness | 6 | 2.19% of revenue; small compensation; no pricing method; reimbursement balances not visible; promoter collateral |
| Disclosure transparency | 5 | Fire recovery, other receivable, impairment and lien detail missing; many internal table errors |
| Consistency with prior years | 7 | No policy change; comparatives within 2 L; hedge and fire items new |
| OVERALL | 6 | Totals tie and trade quality is clean. Judgement items (recovery, EBITDA reclass, cash flow tie-out, funding) are thinly disclosed. Unchanged from the preliminary 6 after Passes 2 and 3 |

## C. KEY RISKS FROM NOTES
| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Insurance claim recovered below 793.05 L or late | Medium | Insurer settlement, interim receipts, other current financial assets | FY27 |
| Funding gap for subsidiary capex (commitments 5,642.27 L vs undrawn lines 3,126.32 L, parent cash 56.38 L) | High | MCPL and MEPL drawdowns, further parent equity, WC lines | FY27 to FY28 |
| Guarantee crystallisation (6,688 L, 22% of net worth); MCPL instalments from Mar 2027 | Medium | Subsidiary results, MEPL instalments from Jan 2026 | FY27 to FY28 |
| Margin: FY25 stock-build inflation and foils at 2.0% | Medium to High | Quarterly gross margin, foils and conductors segment results, FG/WIP | Next four quarters |
| Associate profit non-cash, Star OCI losses, Toyal current liabilities 4,698.45 L vs current assets 3,690.62 L | Medium | Star dividend (1.3% payout), Toyal liquidity, carrying values | FY27 |
| Liquidity: liens 2,545.72 L vs deposits 242.24 L | Medium | Federal Bank terms, true collateral | Next filing |
| Reversal of payables rise (+70.2%) and raw material stock +67.9% | Medium | Payable days 20.5 vs 14.3, stock days | FY27 |
| Other receivable 703.86 L at 40.2% reserve | Low to Medium | Annual credit-loss charge about 53 L | Annual |
| Unfunded gratuity +75% | Low | Next valuation, salary base | Annual |
| Hedge accounting error or FX loss | Low | MTM on 1,979.34 L forwards | Quarterly |

## D. FIVE QUESTIONS FOR MANAGEMENT
1. Has the insurer accepted the 793.05 L claim, how much has been received since 31 March 2026, and is a business-interruption claim lodged for lost Q1 FY26 production?
2. What were the PPE disposal and debris proceeds from the fire, and why does the cash flow add back only 23.45 L against 371.45 L of non-cash PPE losses?
3. How will the 5,642.27 L of group capital commitments be funded against 3,126.32 L of undrawn subsidiary term loans, and what collateral stands behind the 2,000 L Federal Bank lien when term deposits total 242.24 L?
4. What is the nature and age of the 703.86 L non-current other receivables, and why is 77% of the FY26 credit-loss charge on them?
5. Why did Star's OCI share fall by 168.32 L, is unrealised profit on sales to Toyal (1,801.51 L) eliminated, and what explains the roughly 580 L of subsidiary reimbursement flows with no closing balance?

## E. NOTES-BASED RED FLAGS
No RED item. Watch signals, each with its alternative reading:
- Earnings presentation signal: fire inventory loss moved below EBITDA (583.03 L). Alternative: standard exceptional-item presentation with a clear note. Separator: Q4 filed cash flow and quarterly margins.
- Aggressive recognition signal: 793.05 L claim recognised as a receivable on a claim bill, against the company's own policy on contingent assets. Alternative: surveyor-assessed claim, which the auditors' key audit matter says they examined (outside the notes, AR p.~79 printed). Separator: insurer settlement.
- Undisclosed-risk indicators: lien text exceeds deposits 10x; fire fatalities with no compensation contingent liability; cash flow add-back mismatch; 580 to 587 L of subsidiary balances with no closing figure.
- Not found: capitalised interest, impairment assumptions, associate unrealised-profit policy.

## F. ONE-LINE NOTES VERDICT
The notes reveal moderate accounting practices. Key concern: the 793.05 L insurance receivable, the fire loss taken below EBITDA, and a cash flow that does not tie to the PPE note, while the parent carries 6,688 L of guarantees and 5,642.27 L of group capex commitments on 298.62 L of liquidity. Key strength: trade receivable ageing is clean (96.3% not due), with no write-offs, no covenant breach and no going concern doubt. Overall accounting quality: 6/10.

```yaml
stage: B02-notes
company: "MMP"
run_date: "2026-10-04"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "B00 CORPUS GAPPED: screener P&L, Quarters, Balance Sheet, Cash Flow, Customization sheets are empty (no CSV); Data_Sheet.csv only"
  - "B00: scanned Q4 FY26 and Q3 FY26 results are image scans with no OCR; not used in this stage (AR FY26 text used instead)"
  - "B00: ARFIN transcripts absent; peer transcripts only APARINDS and MAANALU"
  - "B00: NSE results clarifications of 2026-03-05 and 2026-06-23 have no company reply in the corpus"
  - "B00: announcements and shareholding were repaired by hand; selection, not full list"
  - "B00: collector warnings on BSE scrip code, empty research/ and prospectus/, no-concall mode (concalls May 2026 and Jul 2022 only)"
  - "Notes-level: insurer acceptance and collection of the 793.05 L claim, business-interruption claim, number of fire deaths, FY26 guidance text, nature and age of 703.86 L other receivables, Toyal contingent liabilities, capitalised interest, contractual 5-year repayment schedule are NOT FOUND IN DOCUMENT"
  - "Notes-level: fire debris and disposal proceeds, Star OCI cause, counter-entry of 46.90 L forward MTM, MEPL own balance sheet, subsidiary headcount and gratuity, composition of interest income, preliminary expenditure policy, associate unrealised profit elimination, collateral behind the 2,000 L Federal Bank lien are NOT FOUND IN DOCUMENT"
flags:
  - {type: FLAG-CASH, reason: "CFO includes short-term borrowing increase (S 789.11 L, C 1,723.34 L); CFO ex-borrowings S 4,649.19 L vs 1,121.30 L; payables +70.2%; CF add-back for fire PPE loss 23.45 L vs 371.45 L non-cash PPE losses so CFO/investing split uncertain by 348 to 437 L. Trade receivable ageing itself is clean (96.3% not due; days 39.2 vs 47.2): this is a WC and classification flag, not a receivables deterioration flag"}
  - {type: FLAG-INSURANCE-RECEIVABLE, reason: "793.05 L receivable booked on final claim bill and management view, 47.4% of 1,672.01 L gross loss, nil received in FY26, insurer acceptance not shown; policy 1.6(d) says contingent assets are not recognised (S Notes 14, 32, 37, 52; S Note 1.6(d) p.114)"}
  - {type: FLAG-EBITDA-FIRE-RECLASS, reason: "Reported EBITDA excludes fire inventory write-off of 583.03 L moved to exceptional (0.71% of S revenue, derived); C EBITDA incl. it about 7.33% vs 8.04% reported (derived). Lost production stays inside EBITDA; no BI claim disclosed (S Notes 31, 32, 37, 52)"}
  - {type: FLAG-ASSOCIATE-PROFIT, reason: "Share of associate profit 820.78 L = 20.5% of C PBT, 26.5% of PAT; cash dividend 9.98 L (S Note 45 p.154); Star OCI share (168.32) L cuts comprehensive share to 574.37 L (C Note 49 p.237); no unrealised profit policy for associates"}
  - {type: FLAG-GUARANTEES, reason: "Corporate guarantees 6,688 L = 22.0% of S net worth; MEPL 11.2% and MCPL 10.8% each above 10%; MCPL 3,288 L called outstanding vs 512.70 L drawn on term loan (S Note 47 p.157; C Note 18 p.205)"}
  - {type: FLAG-FUNDING, reason: "Undrawn sanctioned subsidiary term loans 3,126.32 L vs C capital commitments 5,642.27 L; parent commitments 3,278.31 L with no undrawn parent loan disclosed; parent cash 56.38 L; C maturity table nil over 5 years though loans run to 2032 and 2033 (C Notes 18, 39B, 52; S Note 48)"}
  - {type: FLAG-COLLATERAL, reason: "Stated liens 2,545.72 L vs all term deposits 242.24 L; liquidity 298.62 L = cash 56.38 L + those deposits (S Notes 7, 14, 23, 39B)"}
accounting_quality: 6
pass_2_empty: false
pass_3_empty: false
top_findings:
  - {rank: 1, finding: "Umred fire: gross loss 1,672.01 L; insurance claim receivable 793.05 L (47.4% of loss) booked on claim bill, no cash in FY26, no insurer acceptance shown; net exceptional 878.96 L = 18.9% of S pre-exceptional PBT; Note 14 dates the fire April 11, 2026", note_ref: "S Notes 14, 32, 37, 52 (p.122, 134-136, 159); S Note 1.6(d) p.114", rating: "YELLOW", why: "Recovery unproven; recognition basis sits against the company's own contingent-asset policy"}
  - {rank: 2, finding: "Cash conversion: S CFO 5,438.30 L includes 789.11 L short-term borrowing increase; ex-borrowings 4,649.19 L vs 1,121.30 L (66% vs 17% of EBITDA), helped by payables +70.2%; fire PPE add-back 23.45 L vs 371.45 L leaves CFO/investing split uncertain by 348 to 437 L", note_ref: "S CF p.95; S Notes 2, 24, 36, 52; C CF p.173", rating: "YELLOW", why: "LBF4: cash conversion quality rests on payables, borrowing classification and a cash flow that does not tie to Note 2"}
  - {rank: 3, finding: "Reported EBITDA is before the fire inventory write-off (583.03 L moved to exceptional); C EBITDA margin 8.04% vs 9.38% (-133 bps), incl. the write-off about 7.33% (derived); parent fall 83 bps, subsidiaries about 50 bps; stock-build credit 0.68% vs 2.99% of revenue", note_ref: "S Notes 31-36 p.133-135; C Note 36 p.214; S Note 52 p.159", rating: "YELLOW", why: "LBF1: margin fall is wider than reported once the fire reclass is counted; FY25 margin carried a stock-build credit"}
  - {rank: 4, finding: "Associate profit 820.78 L = 20.5% of C PBT, 26.5% of PAT; Star 90.5%; dividend 9.98 L (1.3% of Star share); Star OCI (168.32) L; Star holds 4.56% of MMP; Toyal about 2,551 L liabilities moved to current; no unrealised profit policy for associates", note_ref: "C Notes 46, 49 p.234, 237-238; S Note 16 p.124; S Note 45 p.154", rating: "YELLOW", why: "LBF3: earnings are non-cash and concentrated in one listed associate that is also a promoter"}
  - {rank: 5, finding: "Subsidiary guarantees 6,688 L = 22.0% of net worth, two items each above 10%; MCPL 3,288 L called outstanding vs 512.70 L drawn; commitments S 3,278.31 L, C 5,642.27 L vs undrawn subsidiary lines 3,126.32 L and parent liquidity 298.62 L", note_ref: "S Notes 47, 48 p.157; C Notes 18, 52 p.205, 241; S Note 39B p.141", rating: "YELLOW", why: "LBF4: parent carries funding and guarantee risk of new-subsidiary capex"}
  - {rank: 6, finding: "Group debt 18,452.46 L (+18.1%), all growth in subsidiaries; C DSCR 2.51 vs 4.55; net debt/EBITDA 2.75x vs 2.24x (derived); S cash 56.38 L; capital note calls debt low and total liabilities less cash 'net debt'", note_ref: "S Notes 39B, 39C, 43; C Notes 18, 43", rating: "YELLOW", why: "Leverage and cover weaken as capex ramps"}
  - {rank: 7, finding: "Subsidiary start-up losses 352.81 L (Insulators segment (329.13) L on 231.94 L revenue); DTA 125.62 L on losses; MEPL loss about 70% of 500 L cash equity; no impairment test shown", note_ref: "C Notes 4, 20, 44, 50 p.197, 207, 226, 239", rating: "YELLOW", why: "Start-up drag, DTA realism, carrying value at cost"}
  - {rank: 8, finding: "Liens 2,545.72 L vs all term deposits 242.24 L; liquidity 298.62 L is mostly margin money", note_ref: "S Notes 7, 14, 23d, 39B", rating: "YELLOW", why: "Liquidity cushion overstated or lien text carried over in error"}
  - {rank: 9, finding: "Non-current other receivables 703.86 L carry 283.19 L allowance (40.2%); 77% of FY26 credit-loss charge (53.26 of 68.81 L) sits on them; debtor and age NOT FOUND", note_ref: "S Notes 7, 11, 36 p.120-121, 135", rating: "YELLOW", why: "Receivable risk sits outside the clean trade ageing"}
  - {rank: 10, finding: "Promoter-group economics: 255.21 L paid to promoter family and entities (5.5% of pre-exceptional PBT); promoter-entity collateral and personal guarantees back group debt; 280 L interest-free promoter loans to MEPL; about 580 to 587 L of subsidiary reimbursement flows with no closing balance; 30.00 L related-party loan absent from RPT table; arm's-length method not stated", note_ref: "S Notes 18, 45 p.126, 150-155; C Notes 18, 23, 46", rating: "YELLOW", why: "LBF3: RPT scale small but disclosure thin; promoter support visible"}
  - {rank: 11, finding: "Gratuity DBO +75% to 611.39 L, unfunded; 94.73 L Labour Code cost taken as exceptional; experience loss 251.97 L to OCI; valuation salary base +68.7% vs headcount +8.0% and P&L salary +6.4%", note_ref: "S Notes 37, 44 p.136, 146-149", rating: "YELLOW", why: "Rising unfunded liability with an unexplained valuation input"}
  - {rank: 12, finding: "Hedge trail: policy says fair value hedge, reserve is cash flow hedge, Note 39B says no hedging (C text says 'has entered'), Note 51 shows 1,979.34 L forwards; MTM payable 57.02 L vs OCI 10.12 L gross; 39B and Note 51 unhedged EUR positions have opposite signs", note_ref: "S Notes 1.4(h), 25, 39A, 39B, 51", rating: "YELLOW", why: "Derivative accounting trail incomplete; low rupee size"}
  - {rank: 13, finding: "Cash flow and Schedule III do not tie: Note 2 derecognised net block 460.28 L vs add-back 23.45 L; C Note 50 FY26 table misses C equity by 645.97 L (Toyal row); C maturity table over-adds 54.00 L", note_ref: "S CF p.95; S Note 2 p.116; C Note 50 p.239; C Notes 39B, 39C", rating: "YELLOW", why: "Reported totals tie but the supporting tables carry errors; lowers confidence in note precision"}
  - {rank: 14, finding: "Segment returns on segment assets: foils 3.2%, conductors 13.7% (21.1% PY), insulators (9.4%), powder 18.4%; foils holds 25% of segment assets for 6.4% of segment result", note_ref: "C Note 44 p.226-227", rating: "YELLOW", why: "Mix and capital intensity behind the margin fall"}
  - {rank: 15, finding: "Clerical and consistency slips: fire date April 11, 2026 in Note 14; lender of 30.00 L missing from RPT table; table headers with wrong dates; 70 bps sensitivity applied to total not variable debt; name inconsistencies. None changes a reported total", note_ref: "various, see Pass 1 and Pass 2 reports", rating: "GREEN", why: "Lowers the disclosure transparency score only"}
red_flags: []
questions_for_mgmt:
  - "Has the insurer accepted the 793.05 L claim, how much has been received since 31 March 2026, and is any business-interruption claim lodged for the lost Q1 FY26 production?"
  - "What were the PPE disposal and debris proceeds from the fire, and why does the cash flow add back only 23.45 L against 371.45 L of non-cash PPE losses?"
  - "How will the 5,642.27 L of group capital commitments be funded against 3,126.32 L of undrawn subsidiary term loans and parent liquidity of 298.62 L, and what collateral stands behind the 2,000 L Federal Bank lien when term deposits total 242.24 L?"
  - "What is the nature and age of the 703.86 L non-current other receivables, and why is 77% of the credit-loss charge on them?"
  - "Why did Star's OCI share fall by 168.32 L, is unrealised profit on sales to Toyal (1,801.51 L) eliminated, and what explains the 580 L of subsidiary reimbursement flows with no closing balance?"
receivables_trend: "stable to improving (trade): net 8,822.61 L vs 8,951.34 L (-1.4%) on revenue +18.8%; days 39.2 vs 47.2 (FY24 36.0); not due 96.3% (PY 92.9%); over 6 months 104.89 L = 1.18% of gross (PY 32.04 L = 0.36%, higher but small); other non-current receivables 703.86 L at 40.2% reserve is a separate watch item carrying 53.26 L of the 68.81 L FY26 credit-loss charge (S Notes 11, 41, 7, 36)"
restatements_found:
  - "None material. FY25 comparatives differ from AR2025 by under 2 L in several lines (S total assets 50,553.98 L vs 50,554.05 L; MSME payables 833.86 L vs 832.28 L); S Note 56 says regrouped"
  - "Not a restatement: C Note 50 FY26 Schedule III table misstates Toyal net assets by 645.97 L; reported equity, profit and OCI tie"
going_concern_language: "NONE as doubt. Only the capital management objective 'Safeguard the Company's ability to continue as going a going concern' (S Note 39C p.142; C p.221); no material uncertainty, no covenant waiver"
analyst_note: "Pass 3 found three new items: reported EBITDA excludes the 583.03 L fire inventory write-off (moved to exceptional); the Pass 1 Note 43 ROCE criticism is softened because lost production does sit in EBITDA and ROCE; the Directors' report (outside the notes, p.27) estimates the net EBITDA hit at Rs 7 to 8 Cr, about 64% to 73% of the 133 bps fall on C revenue (derived), leaving about 300 to 400 L unexplained by the fire. Two readings stay open: fire disruption vs FY25 stock-build inflation for margin, and omitted add-back vs undisclosed proceeds for the cash flow. Both resolve only with the Q4 FY26 filed cash flow and quarterly FG/WIP. No RED. Score 6 of 10: loss recognition and trade ageing are clean; recovery booking, cash flow tie-outs and funding disclosure are thin. All figures INR Lakhs."
```
