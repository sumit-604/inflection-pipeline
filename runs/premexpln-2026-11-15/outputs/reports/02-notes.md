# Stage 2 Notes, Pass 3 and Consolidation: PREMEXPLN, FY2025-26
Run: premexpln-2026-11-15 | Model: claude-sonnet-5-5 | Source: Annual_Report_2026.txt (46th AR)
Unit: INR lakhs ("L") as printed ("All amounts in INR lakhs"). No conversion; stage 10 converts once. Anchors: (Note N, p.P, L); p. = "[page N]" marker in the .txt (printed page = p. minus 3).

B00 input_gaps carried forward: shareholding folder empty (repaired at /step1 with limits); screener P&L/Quarters/BS/CF sheets empty; Q2 FY27 concall transcript absent (freshness FAIL); no research; BSE API 403 (NSE used); OCR results scans need PDF-page checks; unidentified Reg 29(1) acquirer; peer transcripts 8 of 12. None blocks a filed, audited notes read. The AR is a text PDF and reads cleanly.

## PASS 3: PATTERN PASS
Method: pattern re-read against Pass 1 and Pass 2, using targeted searches (going concern, material uncertainty, restated) and cross-note ties.

Result: PASS 3: NO MATERIAL NEW FINDINGS

Every contradiction, tie-out failure, vague disclosure, comparative check and going concern item the pattern search turns up is already in Pass 1 or Pass 2:
- Contradictions between notes: insurance receivable 609.80 L vs 683.59 L (P1 4); KMP loan rate 8.95% vs 10% (P1 2); ratio-note reason "increase in Revenue" vs revenue down 6.97% (P2 N8); Note 18 vs Note 30 deferred tax row (P2 N9); auditor JV loss 2.22 L vs note 1.21 L (P1 6).
- Numbers that do not match the statements: receivable ageing that does not roll (P2 N2); payable ageing that does not roll (P1 8); NCI at 25.4% vs 20% holding (P2 N13).
- Deliberately thin disclosure: supplier finance Note 15(e) (two sentences); discount Note 22 (no supplier, date or terms); contingent items (no forum or stage); variable consideration rate change (no reason).
- Restated prior year: none found on 18 checked lines (P2 N15). Note 46 says "regrouped/reclassified" without amounts.
- Events after balance sheet date: Note 45 lists only the proposed dividend 268.81 L (p.153). April 2026 licence refusal and cancelled export order are not in the notes (P2 N16).
- Going concern: parent none (Note 2.1(ii), p.113). Material uncertainty only for PELNEXT, net assets (6.63) L (auditor Other Matters (b) p.157; consolidated Note 43, p.204).

Cross-note pattern (synthesis of anchored facts, not a new filed fact): the 3,417.80 L supplier discount, the payables fall (11,654.90 to 4,151.63 L), the supplier advances rise (+98.6%) and operating cash flow of (144.14) L all sit in the same supplier relationship space. The notes never tie them. This is the one linkage a downstream stage should test. [INFERENCE]

---
# CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

## A. TOP 15 FINDINGS
| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Other income 4,214.49 L (FY25 211.53 L) includes a 3,417.80 L supplier purchase discount for materials "procured and consumed in the previous financial year" plus a 500.00 L onerous-provision reversal. Together 3,917.80 L = 64.8% of PBT 6,043.17 L. PBT without them ~2,125.37 L (derived). Company ROCE 8.03% ties only with all other income stripped: EBIT 2,713.63 L, EBITDA 3,882.18 L (10.0% of revenue). | Note 22, p.133; 29(c), p.139; 43, p.152 | 🔴 | Reported profit is mostly non-operating. Reading A: one-off true-up of a prior-year cost. Reading B: a cost cut that belongs in FY25 cost of materials. Separator: settlement terms and date, not filed. |
| 2 | Cash conversion failed: operating cash flow (144.14) L vs PAT 4,582.51 L. Working capital absorbed 5,863.23 L net. Cash fell 9,309.24 to 5,057.21 L. | CFS p.112; Note 36, p.146 | 🔴 | FLAG-CASH. If the discount was settled by credit note, it is non-cash profit. Not stated. |
| 3 | Receivables over one year old did not clear: 887.36 L (FY25) vs 888.35 L (FY26). Over 6 months 1,582.37 L = 25.3% of gross 6,250.04 L (FY25 20.5%). Over-3-year bucket exceeds its feeder by 20.33 L. Confirmations got no response. | Note 11(c),(d), p.127-128; KAM p.154 | 🔴 | Old dues do not collect. Payers are described as PSU and Government bodies. ECL 905.47 L covers 57.2% of over-6-month balance. |
| 4 | Net receivable days 50.2 vs 33.3 (FY25) vs 97.6 (FY24). Ratio note blames "increase in Revenue" though revenue fell 6.97%. | Note 11, p.127; Note 43, p.152 | 🔴 | Direction worsens; the stated reason is false. |
| 5 | Accident accounting: 709.80 L assets lost; claim booked 609.80 L in text vs 683.59 L on balance sheet (73.79 L gap); 100.00 L loss + 520.00 L ex-gratia. Claim unsettled. Notes name no plant, fatalities, licence or fines. Auditor Emphasis of Matter. | Note 7(ii), p.125; Note 29, p.138-139; EoM p.154 | 🟡 | Unlocated 73.79 L; insurance receivable lifts current ratio from 1.56 to 1.60. |
| 6 | Revenue estimate softened: variable consideration deduction fell to 5.99% (2,476.47 L) from 9.37% (4,316.26 L). Adds ~1,396 L revenue vs FY25 rate (derived). Auditor KAM on powder factor. | Note 21, p.133; KAM p.154-155 | 🟡 | Revenue quality; no reason given. |
| 7 | FX loss 591.64 L (FY25 2.53 L) = 9.8% of PBT, realised ~613.15 L; rupee moved ~10.6%; foreign payables 2.5x foreign receivables vs "natural hedging". No hedges. | Note 29, p.138; Note 32(B), p.142-143; CFS p.112 | 🟡 | Stated policy not supported by tables. |
| 8 | Working-capital swing: payables 11,654.90 to 4,151.63 L; supplier finance 747.56 L with no terms; payable ageing does not roll (2-3y 457.12 L vs 8.36 L feeder); FG +88.9% vs revenue -7.0%. | Notes 10, 15(e), 36, p.126, 130, 146 | 🟡 | Supplier finance can hide debt; ageing basis unclear. |
| 9 | Advances to suppliers +98.6% to 2,115.95 L (domestic part 4.8x). | Note 9(ii), p.126 | 🟡 | Reading A: prepayment for FY27 ramp. Reading B: cash tied to the discount settlement. |
| 10 | Contingent liabilities 8,343.60 L = 28.9% of net worth; LCs and guarantees 7,607.05 L (+28.0%); new GST claim 98.88 L; no forum or stage; nothing on accident claims. | Note 34, p.145 | 🟡 | Disclosure thin against size. |
| 11 | Control: AKS Family Trust 2,22,21,735 shares (41.33%) equals exact sum of three promoter holdings; transfer after dividend record date. Date, consideration not disclosed. KMP pay +30.5% to 445.29 L vs revenue -7.0%. | Note 14(iii),(iv), p.129; Note 38, p.147-150 | 🟡 | Reading A: inter-se restructuring. Reading B: sale-chain step. Separator: trust deed and SPA seller. |
| 12 | Customer advances: domestic -35.0%, foreign +163.2% (2,546.28 L). Export cancellation (April 2026) and any refund obligation absent from notes. | Note 19, p.132; Note 32(B); Note 45, p.153 | 🟡 | Possible undisclosed liability. |
| 13 | Notes silent on post-year-end licence refusal, cancelled export order, recommissioning. | Note 45, p.153 | 🟡 | Events window 1 Apr to 29 May 2026. |
| 14 | Disclosure gaps: no segment or product split (single segment), no contract assets or order book, no ECL matrix, no lease liability, no 10%-customer name, gratuity funded 38.9% with 4% salary growth vs 10.1% salary cost growth. | Notes 2.2, 2.10, 21, 25(a), 35 | 🟡 | Sector-cap separator not in notes. |
| 15 | Capital employed defined two ways (standalone with DTL, consolidated without); land at 2016 deemed cost 39.2% of PPE, revaluation reserve 5,570.59 L = 19.3% of net worth. | Note 43, p.152; consolidated Note 42, p.203; SOCE p.111 | 🟡 | ROCE comparability and base quality. |

Strengths: net cash 2,314.50 L (derived), covenants complied (Note 33(b), p.145), no ESOP dilution, no restated FY25 amounts found, KMP/promoter loans nil, RPT under 2% of revenue ex-dividend.

## B. ACCOUNTING QUALITY SCORE: 5 / 10
| Dimension | Score | Basis |
|---|---|---|
| Revenue recognition conservatism | 5 | Variable-consideration rate fell to 5.99% from 9.37% with no reason; KAM |
| Expense capitalisation honesty | 7 | R&D expensed; no capitalised borrowing cost shown; CWIP 2,639.23 L, no overrun stated |
| Provisioning adequacy | 5 | ECL 14.5% of gross but old dues static; 500.00 L provision reversed into income; no contingent-liability provisions |
| RPT fairness | 7 | Small, no promoter loans; KMP pay +30.5%; control change undisclosed; rate mismatch 8.95% vs 10% |
| Disclosure transparency | 4 | Discount, supplier finance, accident, post-year-end events and contingents thin; stated ratio reason false |
| Consistency with prior years | 5 | No restatement found; ageing buckets do not roll; ROCE definitions differ |
| OVERALL | 5 | Honest balance sheet and covenants; earnings quality and cash conversion weak |

## C. KEY RISKS FROM NOTES
| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Profit rests on 3,917.80 L non-recurring other income | High | FY27 other income, quarterly operating margin, settlement terms | H1 FY27 results |
| Cash conversion: operating cash flow (144.14) L | High | Operating cash flow, receivable days, supplier payment mode | Next two quarters |
| Old receivables (1,582.37 L over 6 months) become bad debt | High | Over-1-year bucket, ECL charge, PSU payments | FY27 audit |
| Insurance claim 683.59 L / 609.80 L not settled | Medium | Settlement, write-off, pending status | FY27 |
| Licence/export-order effects not in notes | Medium | Exchange filings, export revenue, customer advance refunds | FY27 H1 |
| FX loss repeat (payables USD, rupee move) | Medium | Net unhedged USD, hedge policy | Each quarter |
| Contingent liabilities 28.9% of net worth, LCs +28.0% | Medium | Forum and stage of tax claims, LC growth | FY27 |
| Control change / SPA | Medium | Trust deed, SPA seller, open offer | Per exchange filings |
| Supplier finance 747.56 L undisclosed terms | Low-Medium | Note 15(e) detail | FY27 |
| Gratuity underfunded 940.09 L (38.9% funded) | Low | Assumptions vs salary growth | FY27 |

## D. FIVE QUESTIONS FOR MANAGEMENT
1. Who is the supplier behind the 3,417.80 L discount, when was it agreed, and was it settled in cash or by credit note?
2. Why did the variable-consideration deduction fall from 9.37% to 5.99% of contract price, and what customer evidence supports it?
3. Which customers hold the 1,582.37 L over 6 months, how much is Government or PSU, and what is the collection plan for the 888.35 L aged over one year?
4. What explains the 73.79 L gap between the insurance receivable (683.59 L) and the booked claim (609.80 L), and when does the insurer settle?
5. What is the refund or claim exposure on the 2,546.28 L foreign customer advances after the April 2026 licence refusal and export order cancellation, and why is this not in Note 45?

## E. NOTES-BASED RED FLAGS
- Earnings management risk: 3,917.80 L (64.8% of PBT) from a prior-year supplier discount and a provision reversal; variable-consideration rate drop adds ~1,396 L revenue (derived). Two readings stand; the notes do not separate them.
- Cash conversion: operating cash flow (144.14) L vs PAT 4,582.51 L; FLAG-CASH.
- Receivable ageing does not roll and old dues do not clear; ratio-note reason is false.
- Undisclosed risk indicators: post-year-end licence refusal and export cancellation absent from Note 45; accident not in contingent liabilities; supplier finance terms absent.
- Not found: any restatement; any parent going concern doubt.

## F. ONE-LINE NOTES VERDICT
The notes reveal moderate accounting practices. Key concern: 64.8% of PBT comes from a prior-year supplier discount and a provision reversal, while operating cash flow is (144.14) L and old receivables do not clear. Key strength: net cash 2,314.50 L (derived), covenants met, no restated comparatives, no promoter loans. Overall accounting quality: 5/10.

```yaml
stage: B02-notes
company: "PREMEXPLN"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "B00: shareholding folder empty at collection (repaired at /step1 via NSE XBRL Sep 2026 and screener capture, with limits); not a notes input"
  - "B00: screener P&L/Quarters/Balance Sheet/Cash Flow sheets empty; Data_Sheet carries the series; not a notes input"
  - "B00: Q2 FY27 concall transcript ABSENT (call held 13 Nov 2026); freshness pair RESULTS to CONCALL FAIL"
  - "B00: no research folder content; no broker notes"
  - "B00: BSE API 403, announcements from NSE; nine open-offer .zip files not opened; Reg 29(1) acquirer name illegible in OCR"
  - "B00: results PDFs are OCR scans; check load-bearing figures on the PDF page. The AR is a text PDF and read cleanly"
  - "B00: BDL peer transcripts absent; 8 of 12 peer transcripts present"
  - "NOTES: not found in the notes (NOT FOUND IN DOCUMENT): supplier and terms of 3,417.80 L discount; ECL matrix; lease liability; contract assets and order book; segment or product split; 10%-customer name; hedging policy; date of promoter-to-trust transfer; post-year-end licence and export-order events"
flags:
  - {type: FLAG-CASH, reason: "Operating cash flow (144.14) L vs PAT 4,582.51 L (CFS p.112); receivables over 6 months 1,582.37 L = 25.3% of gross 6,250.04 L (FY25 20.5%); over-1-year balances 887.36 L to 888.35 L with nothing collected net (Note 11, p.127-128); net receivable days 50.2 vs 33.3 (derived); all units INR lakhs"}
  - {type: FLAG-EARNINGS-QUALITY, reason: "Other income 4,214.49 L includes 3,417.80 L prior-year supplier discount and 500.00 L provision reversal = 64.8% of PBT 6,043.17 L (Note 22, p.133; Note 29(c), p.139); two readings, separator is settlement terms not filed"}
accounting_quality: 5
pass_2_empty: false
pass_3_empty: true
top_findings:
  - {rank: 1, finding: "Other income 4,214.49 L (FY25 211.53 L) includes 3,417.80 L supplier purchase discount for prior-year materials and 500.00 L provision reversal; 3,917.80 L = 64.8% of PBT 6,043.17 L; PBT without them ~2,125.37 L (derived)", note_ref: "Note 22, p.133; Note 29(c), p.139; Note 43, p.152", rating: "RED", why: "Reported profit mostly non-operating. Reading A one-off true-up; Reading B belongs in FY25 cost. Separator: settlement terms and date, not filed"}
  - {rank: 2, finding: "Operating cash flow (144.14) L vs PAT 4,582.51 L; working capital absorbed 5,863.23 L; cash fell 9,309.24 to 5,057.21 L", note_ref: "CFS p.112; Note 36, p.146", rating: "RED", why: "Cash conversion failure; discount may be non-cash if settled by credit note (not stated)"}
  - {rank: 3, finding: "Receivables over one year 887.36 L (FY25) to 888.35 L (FY26), nothing collected net; over 6 months 1,582.37 L = 25.3% of gross 6,250.04 L (FY25 20.5%); over-3-year bucket exceeds feeder by 20.33 L; confirmations unanswered", note_ref: "Note 11(c),(d), p.127-128; KAM p.154", rating: "RED", why: "Old dues static; ECL 905.47 L covers 57.2% of over-6-month balance; payers described as PSU and Government"}
  - {rank: 4, finding: "Net receivable days 50.2 (FY25 33.3, FY24 97.6); ratio note gives 'increase in Revenue' as reason though revenue fell 6.97%", note_ref: "Note 11, p.127; Note 43, p.152", rating: "RED", why: "Direction deteriorates; stated reason false; average balance hides year-end rise"}
  - {rank: 5, finding: "Accident: 709.80 L assets lost; insurance receivable 609.80 L in text vs 683.59 L on face (73.79 L gap); 100.00 L loss and 520.00 L ex-gratia; claim unsettled; auditor Emphasis of Matter; notes silent on plant, deaths, licence, fines", note_ref: "Note 7(ii), p.125; Note 29, p.138-139; EoM p.154", rating: "YELLOW", why: "Unlocated 73.79 L; receivable lifts current ratio 1.56 to 1.60; no contingent liability for accident claims"}
  - {rank: 6, finding: "Variable consideration deduction fell to 5.99% (2,476.47 L) from 9.37% (4,316.26 L); adds ~1,396 L revenue at FY25 rate (derived); KAM on powder factor", note_ref: "Note 21, p.133; KAM p.154-155", rating: "YELLOW", why: "Revenue estimate softened with no reason in the notes"}
  - {rank: 7, finding: "FX loss 591.64 L (FY25 2.53 L) = 9.8% of PBT, realised ~613.15 L (derived); rupee ~10.6% move; foreign payables 2.5x receivables; no hedges", note_ref: "Note 29, p.138; Note 32(B), p.142-143; CFS p.112", rating: "YELLOW", why: "'Natural hedging' statement not supported by the tables"}
  - {rank: 8, finding: "Payables 11,654.90 to 4,151.63 L; supplier finance 747.56 L with two-sentence Note 15(e); payable ageing does not roll; finished goods +88.9% vs revenue -7.0%", note_ref: "Notes 10, 15(e), 36, p.126, 130, 146", rating: "YELLOW", why: "Working-capital swing and possible debt-like supplier finance"}
  - {rank: 9, finding: "Advances to suppliers 2,115.95 L vs 1,065.61 L (+98.6%); domestic part 4.8x", note_ref: "Note 9(ii), p.126", rating: "YELLOW", why: "Reading A prepayment for FY27 ramp; Reading B cash tied to discount settlement. Separator: FY27 raw material receipts"}
  - {rank: 10, finding: "Contingent liabilities 8,343.60 L = 28.9% of net worth 28,903.17 L; LCs and guarantees 7,607.05 L (+28.0%); new GST claim 98.88 L; no forum or stage; no accident claim item", note_ref: "Note 34, p.145; Note 33, p.144", rating: "YELLOW", why: "Large vs net worth with thin disclosure"}
  - {rank: 11, finding: "AKS Family Trust 2,22,21,735 shares (41.33%) equals exact sum of three promoter holdings; transfer after dividend record date; date and consideration not disclosed; KMP pay +30.5% to 445.29 L vs revenue -7.0%", note_ref: "Note 14(iii),(iv), p.129; Note 38, p.147-150", rating: "YELLOW", why: "Reading A inter-se restructuring; Reading B sale-chain step. Separator: trust deed and SPA seller"}
  - {rank: 12, finding: "Customer advances: domestic -35.0% to 4,075.98 L (derived), foreign +163.2% to 2,546.28 L; April 2026 export cancellation and refund exposure absent from notes", note_ref: "Note 19, p.132; Note 32(B), p.142-143; Note 45, p.153", rating: "YELLOW", why: "Possible undisclosed obligation"}
  - {rank: 13, finding: "Note 45 lists only proposed dividend 268.81 L; licence refusal, export cancellation, recommissioning status not in notes", note_ref: "Note 45, p.153", rating: "YELLOW", why: "Events in 1 Apr to 29 May 2026 window undisclosed in the notes"}
  - {rank: 14, finding: "Single segment, no contract assets or order book, no ECL matrix, no lease liability, no 10%-customer name; gratuity funded 38.9% with 4% salary growth vs 10.1% salary cost growth", note_ref: "Notes 2.2, 2.10, 21, 25(a), 35", rating: "YELLOW", why: "Valuation-relevant disclosures missing; sector-cap separator not in notes"}
  - {rank: 15, finding: "ROCE capital employed defined two ways (standalone includes DTL, consolidated excludes); land at 2016 deemed cost 7,012.62 L = 39.2% of net PPE; revaluation reserve 5,570.59 L = 19.3% of net worth", note_ref: "Note 43, p.152; consolidated Note 42, p.203; SOCE p.111", rating: "YELLOW", why: "ROCE comparability and base quality"}
red_flags:
  - "Earnings quality: 3,917.80 L (64.8% of PBT) from prior-year supplier discount plus provision reversal (Note 22, p.133; Note 29(c), p.139)"
  - "Cash conversion: operating cash flow (144.14) L vs PAT 4,582.51 L (CFS p.112)"
  - "Receivable ageing: over-1-year balances static at ~888 L; confirmations unanswered; over-3-year bucket exceeds feeder by 20.33 L (Note 11, p.127-128)"
  - "Stated reason for receivables turnover change is contradicted by revenue (Note 43, p.152)"
  - "Post-year-end licence refusal and export order cancellation not in Note 45 (p.153); accident not in Note 34 (p.145)"
questions_for_mgmt:
  - "Who is the supplier behind the 3,417.80 L discount, when was it agreed, and was it settled in cash or by credit note?"
  - "Why did the variable-consideration deduction fall from 9.37% to 5.99% of contract price, and what evidence supports it?"
  - "Which customers hold the 1,582.37 L over 6 months, how much is Government or PSU, and what is the plan for the ~888 L aged over one year?"
  - "What explains the 73.79 L gap between the insurance receivable 683.59 L and the booked claim 609.80 L, and when does the insurer settle?"
  - "What is the refund or claim exposure on 2,546.28 L foreign customer advances after the April 2026 licence refusal and export cancellation, and why is it not in Note 45?"
receivables_trend: "deteriorating: gross 6,250.04 L (FY25 4,329.61 L); over 6 months 1,582.37 L = 25.3% (FY25 887.36 L = 20.5%); 6m-1y 395.64 L, 1-2y 298.38 L, 2-3y 556.28 L, over 3y 332.07 L; over-1-year 888.35 L vs 887.36 L (nothing collected net); ECL 905.47 L = 14.5% of gross; net days 50.2 vs 33.3 (FY24 97.6) (Note 11, p.127-128; INR lakhs)"
restatements_found: []
going_concern_language: "NONE for the parent (Note 2.1(ii), p.113: going concern basis). Subsidiary only: material uncertainty for PELNEXT Defence Systems Pvt Ltd, net assets (6.63) L (auditor Other Matters (b), p.157; consolidated Note 43, p.204)"
analyst_note: "Units are INR lakhs; stage 10 converts once. Pass 3 found no new filed facts. One linkage for downstream testing [INFERENCE]: the 3,417.80 L discount, the payables fall to 4,151.63 L from 11,654.90 L, supplier advances +98.6% and operating cash flow (144.14) L sit in one supplier space, and the notes never tie them. If the discount was a credit note, operating profit before working capital 7,352.54 L carries a non-cash item. Notes carry no segment split, so the sector-cap separator must come from outside the notes. The notes never name Katepally or the licence status; those come from the Directors' Report and B00."
```
